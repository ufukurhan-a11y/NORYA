import base64
import json
import logging
import secrets
import threading
import time
import uuid
from datetime import datetime, timedelta, timezone
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen
from urllib.error import URLError

from dotenv import load_dotenv

# Uvicorn nereden çalışırsa çalışsın .env proje kökünden yüklensin (norya/)
_PROJ_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJ_ROOT / ".env")

from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, Query, Request, UploadFile
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from app.core.templating import Jinja2Templates
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from sqlalchemy import or_, text
from sqlalchemy.exc import IntegrityError as SQLIntegrityError
from sqlmodel import Session, select

from app.admin import admin_router as new_admin_router
from app.api.admin import get_admin_html, router as admin_router
from app.api.auth import router as auth_router
from app.api.institution import router as institution_api_router, page_router as institution_page_router
from app.enterprise import enterprise_router
from app.api.deps import get_current_user, get_current_user_optional, get_current_user_or_dev_guest, security
from app.cache_db import cache_get, cache_set, get_conn as get_cache_conn, init_cache as init_ai_cache, purge_expired as purge_ai_cache_expired
from app.cache_utils import expires_iso, make_cache_key, now_iso
from app.core.config import is_openai_configured, settings
from app.core.database import engine, get_db, init_db
from app.core.rate_limit import limiter
from app.core.geo import get_geo_from_ip
from app.legal_i18n import LEGAL_HREFLANG_LANGS, LEGAL_LANGS, get_legal_content, get_legal_ui
from app.core.security import (
    create_pdf_access_token,
    decode_access_token,
    decode_pdf_access_token,
    hash_password,
    verify_report_verification_token,
)
from app.models import (  # noqa: F401
    AnalysisJob,
    AnalysisRecord,
    AuditLog,
    DiscountCode,
    EmailLead,
    EnterpriseLead,
    ErrorLog,
    PaymentOrder,
    Presence,
    ReportVerification,
    PushSubscription,
    SecurityLog,
    UploadLog,
    EmailVerifyToken,
    GuestLoginToken,
    PasswordResetToken,
    ShareToken,
    User,
)
from app.enterprise_i18n import ENTERPRISE_LANGS, get_enterprise_ui
from app.how_it_works_i18n import (
    DEFAULT_HOW_IT_WORKS_LANG,
    HOW_IT_WORKS_LANGS,
    get_how_it_works_meta,
    get_how_it_works_ui,
)
from app.base_i18n import get_base_ui
from app.landing_i18n import (
    LANDING_ROUTES,
    get_landing_meta,
    get_landing_ui,
)
from app.seo_landing_i18n import (
    get_related_links,
    get_seo_landing_content,
    get_seo_landing_hreflang,
    get_seo_landing_meta,
    iter_seo_landing_urls,
    OG_LOCALE_MAP as SEO_OG_LOCALE_MAP,
)
from app.pay_i18n import get_pay_ui, get_plan_display_name, get_plan_benefits
from app.pricing_page_i18n import PRICING_HREFLANG_LANGS, enrich_pricing_context
from app.blog_i18n import BLOG_LANGS, BLOG_LANGS_PREMIUM, BLOG_UI, DEFAULT_BLOG_LANG, get_article, get_blog_icon_paths, get_related_articles, iter_all_article_paths, list_articles_for_lang
from app.core.config import BRAND_NAME
from app.services.coupon import apply_coupon_use, get_active_campaign_for_checkout, validate_coupon
from app.services.pricing import (
    get_base_prices_cents,
    get_plan_code_to_product_cents,
    get_active_campaign_with_display,
)
from app.services.report_pdf import build_doctor_pdf, build_report_pdf, extract_trend_from_results
from app.services.report_verification import get_or_create_verification
from app.services.storage import upload_report_pdf
from app.schemas.analyze import (
    AnalysisDetail,
    AnalysisHistoryItem,
    AnalyzeResponse,
    HealthScoreSchema,
    PdfInfoSchema,
    UiHintsSchema,
    UploadJsonRequest,
)
from app.schemas.payment import CreateSessionRequest, GrantPaymentRequest, GuestSessionRequest, PaytrInitRequest
from app.services.analyze import analyze_blood_test, analyze_blood_test_from_image
from app.services.pdf_extract import extract_text_from_pdf
from app.logging import setup_logging

setup_logging(level=logging.INFO)
log = logging.getLogger("norya")

RATE_LIMIT_STR = f"{settings.rate_limit_per_minute}/minute"

def _cors_origins_list() -> list[str]:
    if not settings.cors_origins or settings.cors_origins.strip() == "*":
        return ["*"]
    return [o.strip() for o in settings.cors_origins.split(",") if o.strip()]

ALLOWED_UPLOAD_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MIME_MAP = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}
ALLOWED_UPLOAD_MIME_TYPES = {"application/pdf", "image/jpeg", "image/jpg", "image/png"}

# Kısa süreli PDF cache: aynı rapor için tekrarlayan isteklerde yeniden üretim engellenir (TTL 2 dk)
_pdf_cache: dict[tuple, tuple[bytes, float]] = {}
_pdf_cache_lock = threading.Lock()
_PDF_CACHE_TTL_SEC = 120


def _max_upload_bytes() -> int:
    try:
        mb = int(getattr(settings, "upload_max_mb", 10) or 10)
    except (TypeError, ValueError):
        mb = 10
    return max(mb, 1) * 1024 * 1024


def _detect_magic_type(content: bytes) -> str | None:
    if not content or len(content) < 4:
        return None
    # PDF: %PDF-
    if content.startswith(b"%PDF"):
        return "pdf"
    # JPEG: FF D8 FF
    if content[0:2] == b"\xFF\xD8":
        return "jpeg"
    # PNG: 89 50 4E 47 0D 0A 1A 0A
    if content.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    return None

# Proje kökü: app/main.py -> app/ -> norya/
_ROOT = Path(__file__).resolve().parent.parent
_APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = _ROOT / "static"
UPLOADS_DIR = _ROOT / "data" / "uploads"  # Yüklenen orijinal belgeler (admin: hastanın gönderdiği)
# Çalışma dizininden de dene (uvicorn farklı yerden çalıştırılırsa)
if not STATIC_DIR.is_dir():
    STATIC_DIR = Path.cwd() / "static"

# Jinja2: yasal sayfalar (örn. /iade-iptal) app/templates kullanır
templates = Jinja2Templates(directory=str(_APP_DIR / "templates"))
templates.env.globals["getattr"] = getattr


def _seed_default_coupon():
    """INDIRIM20 kuponu yoksa oluşturur (%20 indirim, tüm planlar). Render/Production'da bar görünsün diye auto_show_on_checkout=True."""
    try:
        from app.core.database import engine
        with Session(engine) as session:
            existing = session.exec(select(DiscountCode).where(DiscountCode.code == "INDIRIM20")).first()
            if not existing:
                coupon = DiscountCode(
                    code="INDIRIM20",
                    discount_type="percent",
                    discount_value=20,
                    valid_from=None,
                    valid_until=None,
                    products=None,
                    is_active=True,
                    auto_show_on_checkout=True,
                )
                session.add(coupon)
                session.commit()
                log.info("Varsayılan kupon INDIRIM20 oluşturuldu (%20 indirim, checkout bar açık).")
            elif getattr(existing, "auto_show_on_checkout", False) is False:
                existing.auto_show_on_checkout = True
                session.add(existing)
                session.commit()
                log.info("INDIRIM20 checkout bar açıldı (auto_show_on_checkout=True).")
    except Exception as e:
        log.warning("INDIRIM20 seed atlandı (ilk kupon doğrulamasında oluşturulacak): %s", e)


def _seed_pricing_plan():
    """PricingPlan tablosu boşsa varsayılan single/monthly/yearly fiyatlarını ekler (merkezi fiyat kaynağı)."""
    try:
        from app.models import PricingPlan
        with Session(engine) as session:
            existing = session.exec(select(PricingPlan).limit(1)).first()
            if existing:
                return
            for code, product, cents, order in (
                ("single_13eur", "single", 1404, 0),
                ("monthly_50eur", "monthly", 5400, 1),
                ("yearly_99eur", "yearly", 10692, 2),
            ):
                session.add(PricingPlan(code=code, product=product, price_cents=cents, display_order=order))
            session.commit()
            log.info("Merkezi fiyat planları seed edildi (single/monthly/yearly).")
    except Exception as e:
        log.warning("PricingPlan seed atlandı: %s", e)


def _reset_institution_quotas_if_due():
    """Kurum kotalarını reset günü geldiyse sıfırla (başlangıçta ve günlük)."""
    try:
        from app.models.institution import Institution
        today = datetime.now().day
        with Session(engine) as db:
            institutions = list(db.exec(
                select(Institution).where(
                    Institution.is_active == True,
                    Institution.quota_reset_day == today,
                    Institution.quota_used_this_month > 0,
                )
            ).all())
            for inst in institutions:
                inst.quota_used_this_month = 0
                db.add(inst)
            if institutions:
                db.commit()
                log.info("Institution quota reset: %d institution(s) reset", len(institutions))
    except Exception as e:
        log.warning("Institution quota reset check failed: %s", e)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    _seed_pricing_plan()
    _seed_default_coupon()
    _reset_institution_quotas_if_due()
    key_ok = is_openai_configured()
    if key_ok:
        log.info("OPENAI_API_KEY: ok (sk-... ile yüklendi)")
    else:
        log.error(
            "OPENAI_API_KEY EKSİK VEYA GEÇERSİZ — Analiz çalışmaz. .env dosyasına OPENAI_API_KEY=sk-... ekleyin (başında/sonunda boşluk olmasın)."
        )
        if getattr(settings, "environment", "").lower() == "production":
            raise RuntimeError(
                "OPENAI_API_KEY tanımlı değil. Production'da analiz servisi açılamaz. .env veya ortam değişkenine OPENAI_API_KEY=sk-... ekleyin."
            )
    env_prod = getattr(settings, "environment", "").lower() == "production"
    if env_prod and (not settings.secret_key or settings.secret_key == "change-me-in-production"):
        raise RuntimeError(
            "SECRET_KEY production'da değiştirilmeli. .env içinde SECRET_KEY=<güçlü-rastgele-key> ekleyin (örn. openssl rand -hex 32)."
        )
    from app.services.email_sender import is_mail_configured
    if is_mail_configured():
        log.info("E-posta (şifre sıfırlama): SMTP yapılandırıldı, gerçek mail gönderilecek.")
    else:
        log.warning("E-posta (şifre sıfırlama): SMTP yapılandırılmadı — .env içinde SMTP_HOST, SMTP_USER, SMTP_PASSWORD ayarlayın; şifre sıfırlama mailleri GÖNDERİLMEYECEK.")
    # Blog ikonları: referans verilen dosyalar static altında yoksa uyar (404 olmasın diye); eksik olsa bile sunucu başlasın (deploy kırılmasın)
    try:
        icon_paths = get_blog_icon_paths()
        missing = []
        for rel in icon_paths:
            full = STATIC_DIR / rel
            if not full.is_file():
                missing.append(rel)
        if missing:
            log.error(
                "Blog ikonları eksik (sayfada 404 olabilir). Eksik: %s. "
                "static/images/blog/icons/ altına ekleyin veya ilgili makaleden icon referansını kaldırın.",
                ", ".join(missing),
            )
        elif icon_paths:
            log.info("Blog ikonları doğrulandı (%d dosya).", len(icon_paths))
    except Exception as e:
        log.warning("Blog ikon doğrulaması atlandı: %s", e)
    yield


app = FastAPI(
    title="Norya API",
    description="Kan tahlili açıklama SaaS API",
    lifespan=lifespan,
)

# Statik dosyalar: proje kökünde /static klasöründen servis edilir
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Tarayıcı varsayılan isteği /favicon.ico → mevcut PNG favicon'a yönlendir (konsol 404'ü giderir)."""
    return RedirectResponse(url="/static/icons/favicon-32x32.png", status_code=302)


@app.get("/googlec8b372359ba47dd3.html", include_in_schema=False)
def google_site_verification():
    """Google Search Console doğrulama dosyasını kökten servis et."""
    verification_file = STATIC_DIR / "googlec8b372359ba47dd3.html"
    if not verification_file.is_file():
        verification_file = Path.cwd() / "static" / "googlec8b372359ba47dd3.html"
    return FileResponse(str(verification_file), media_type="text/html; charset=utf-8")


app.state.limiter = limiter

# AI response cache: aynı analiz girdisi (normalize metin + dil + plan + model) tekrar gelirse OpenAI çağrılmaz
AI_CACHE_TTL_DAYS = 30
AI_CACHE_PROMPT_VERSION = 3  # 3 = risk_summary + explanation + tables; cache'de risk_summary dahil
OPENAI_ANALYZE_MODEL = "gpt-4o-mini"
# Şimdilik ücretsiz kullanıcı da premium grafikleri ve PDF'i görsün (test için; sonra False yapın)
PREMIUM_VISIBLE_FOR_FREE = True
_cache_db_path = str(_PROJ_ROOT / "norya.db")
if getattr(settings, "database_url", "").startswith("sqlite:///"):
    _p = settings.database_url.replace("sqlite:///", "", 1).strip()
    if _p.startswith("./"):
        _cache_db_path = str(_PROJ_ROOT / _p[2:].lstrip("./"))
    else:
        _cache_db_path = _p
_cache_conn = get_cache_conn(_cache_db_path)
init_ai_cache(_cache_conn)


def _error_response(request: Request, status_code: int, detail: str) -> JSONResponse:
    rid = getattr(request.state, "request_id", None)
    body = {"error": detail, "status_code": status_code}
    if rid:
        body["request_id"] = rid
    return JSONResponse(status_code=status_code, content=body)


def _rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded) -> JSONResponse:
    """Production format: {"error":"Too many requests","detail":"..."}"""
    try:
        ip = (request.headers.get("x-forwarded-for") or "").split(",")[0].strip() or (request.client.host if request.client else "")
        with Session(engine) as db:
            db.add(SecurityLog(event="rate_limit", ip=ip or None, endpoint=request.url.path, detail="Rate limit exceeded"))
            db.commit()
    except Exception as e:
        log.warning("SecurityLog rate_limit write failed: %s", e)
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests", "detail": "Rate limit exceeded. Please try again later."},
    )


def _validation_error_message(exc: RequestValidationError) -> str:
    errs = exc.errors()
    if not errs:
        return "Geçersiz istek."
    first = errs[0]
    msg = (first.get("msg") or "").lower()
    loc = list(first.get("loc") or [])
    field = str(loc[-1]) if len(loc) > 0 else None
    if "field required" in msg or first.get("type") == "missing":
        if field == "password":
            return "Lütfen şifre girin (en az 6 karakter)."
        if field == "email":
            return "Lütfen e-posta adresinizi girin."
        if field == "body":
            return "Veriler sunucuya ulaşmadı. Sayfayı yenileyip şifre alanını tekrar doldurarak deneyin."
        if field == "full_name":
            return "Lütfen adınızı girin."
        if field == "file":
            return "Dosya gönderilmedi. Lütfen dosyayı tekrar seçip Analiz Et'e tıklayın."
        if field == "text":
            return "Lütfen tahlil metnini girin veya PDF/görsel yükleyin."
        if field == "file_base64" or field == "filename":
            return "Dosya verisi eksik veya geçersiz. Lütfen tekrar dosya seçip deneyin."
        return "E-posta ve şifreyi girin."
    if "şifre" in msg or "6 karakter" in msg or "at least 6" in msg or "password" in msg:
        return "Şifre en az 6 karakter olmalı."
    return first.get("msg") or "Geçersiz istek."


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    errs = exc.errors()
    log.exception(
        "Request validation error (422): path=%s method=%s detail=%s",
        request.url.path,
        request.method,
        errs,
    )
    user_msg = _validation_error_message(exc)
    rid = getattr(request.state, "request_id", None)
    body = {"error": user_msg, "status_code": 422, "detail": errs}
    if rid:
        body["request_id"] = rid
    return JSONResponse(status_code=422, content=body)


app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)  # custom handler for {"error":"Too many requests","detail":"..."}

# Tüm istekler için IP bazlı rate limit (SlowAPI middleware)
app.add_middleware(SlowAPIMiddleware)


def _accepts_html(request: Request) -> bool:
    """İstek tarayıcıdan mı (HTML tercih ediyor mu) kontrol eder."""
    accept = (request.headers.get("accept") or "").lower()
    return "text/html" in accept and ("application/json" not in accept or accept.index("text/html") < accept.index("application/json"))


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 429:
        detail = exc.detail if isinstance(exc.detail, str) else "Rate limit exceeded. Please try again later."
        return JSONResponse(
            status_code=429,
            content={"error": "Too many requests", "detail": detail},
        )
    if exc.status_code == 404 and _accepts_html(request):
        _404_path = _APP_DIR / "templates" / "404.html"
        if _404_path.is_file():
            return HTMLResponse(status_code=404, content=_404_path.read_text(encoding="utf-8"))
        return HTMLResponse(status_code=404, content="<html><body><h1>404 Not Found</h1></body></html>")
    return _error_response(request, exc.status_code, exc.detail if isinstance(exc.detail, str) else str(exc.detail))


@app.exception_handler(Exception)
def unhandled_exception_handler(request: Request, exc: Exception):
    log.exception("Unhandled exception: path=%s %s", request.url.path, exc, exc_info=True)
    import traceback
    try:
        from app.core.database import engine
        with Session(engine) as db:
            db.add(ErrorLog(
                user_id=None,
                endpoint=request.url.path,
                method=request.method,
                error_message=str(exc)[:2000],
                stack_trace=traceback.format_exc()[:10000],
            ))
            db.commit()
    except Exception as e:
        log.warning("ErrorLog write failed: %s", e)
    path = (request.url.path or "").strip()
    if path.startswith("/analyze"):
        user_msg = "Analiz sırasında hata oluştu."
    else:
        user_msg = "Beklenmeyen sunucu hatası."
    # Admin panel isteklerinde HTML döndür (JSON yerine)
    if path.startswith("/admin"):
        html = (
            "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Hata</title></head><body style='"
            "font-family:system-ui;max-width:32rem;margin:2rem auto;padding:1rem;background:#1e293b;color:#e2e8f0;'>"
            "<h1 style='color:#f87171;'>Sunucu hatası</h1><p>" + user_msg + "</p>"
            "<p><a href='/admin' style='color:#38bdf8;'>Admin paneline dön</a></p>"
            "</body></html>"
        )
        return HTMLResponse(status_code=500, content=html)
    return JSONResponse(status_code=500, content={"error": user_msg})


# Google Ads için gevşek CSP'ler
# 1) /payment/success: conversion/remarketing isteği, inline script ve Tag Assistant badge'i çalışmalı
# script-src-elem: 'unsafe-inline' gtag/conversion inline script'leri için; style-src: googletagmanager Tag Assistant badge için
_CSP_PAYMENT_SUCCESS = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.tailwindcss.com "
    "https://www.googletagmanager.com https://googletagmanager.com "
    "https://www.googleadservices.com https://googleadservices.com https://pagead2.googlesyndication.com "
    "https://googletag.g.doubleclick.net https://googleads.g.doubleclick.net https://www.google.com; "
    "script-src-elem 'self' 'unsafe-inline' https://www.googletagmanager.com https://googletagmanager.com "
    "https://www.googleadservices.com https://googleadservices.com https://pagead2.googlesyndication.com "
    "https://googletag.g.doubleclick.net https://googleads.g.doubleclick.net https://www.google.com; "
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://www.googletagmanager.com https://googletagmanager.com; font-src 'self' https://fonts.gstatic.com; "
    "img-src 'self' data: blob: https://www.google.com https://google.com https://www.google.com.tr https://google.com.tr "
    "https://www.googleadservices.com https://googleadservices.com "
    "https://www.googletagmanager.com https://googletagmanager.com https://pagead2.googlesyndication.com https://tpc.googletagmanager.com "
    "https://googleads.g.doubleclick.net https://googletag.g.doubleclick.net; "
    "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com "
    "https://www.google.com https://google.com https://www.google.com.tr https://google.com.tr "
    "https://*.google.com "
    "https://www.googletagmanager.com https://googletagmanager.com "
    "https://www.googleadservices.com https://googleadservices.com https://pagead2.googlesyndication.com "
    "https://googletag.g.doubleclick.net https://googleads.g.doubleclick.net "
    "https://www.google-analytics.com https://region1.google-analytics.com https://tpc.googletagmanager.com; "
    "frame-src 'self' https://www.google.com https://google.com https://www.googletagmanager.com https://googletagmanager.com "
    "https://googleads.g.doubleclick.net https://googletag.g.doubleclick.net https://www.googleadservices.com; "
    "frame-ancestors 'self';"
)

# 2) /payment: ödeme formu (PayTR iFrame + Google Ads/GA4/Tag Assistant scriptleri)
_CSP_PAYMENT_PAGE = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.tailwindcss.com "
    "https://www.googletagmanager.com https://googletagmanager.com "
    "https://www.googleadservices.com https://googleadservices.com "
    "https://googleads.g.doubleclick.net https://www.google.com; "
    "script-src-elem 'self' 'unsafe-inline' https://www.googletagmanager.com https://googletagmanager.com "
    "https://www.googleadservices.com https://googleadservices.com "
    "https://googleads.g.doubleclick.net https://www.google.com; "
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://www.gstatic.com https://www.googletagmanager.com https://googletagmanager.com; "
    "font-src 'self' https://fonts.gstatic.com https://www.gstatic.com; "
    "img-src 'self' data: blob: https://www.google.com https://www.google.com.tr "
    "https://googleads.g.doubleclick.net https://www.google-analytics.com "
    "https://www.googletagmanager.com; "
    "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com "
    "https://www.google.com https://www.googletagmanager.com "
    "https://googleads.g.doubleclick.net https://www.googleadservices.com; "
    "frame-src 'self' https://www.googletagmanager.com https://www.google.com; "
    "frame-ancestors 'self';"
)


@app.middleware("http")
async def security_headers(request: Request, call_next):
    """Production güvenlik başlıkları: CSP, X-Content-Type-Options, X-Frame-Options, HSTS (HTTPS)."""
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    path = (request.url.path or "").strip().rstrip("/") or "/"
    is_payment_success = path == "/payment/success"
    is_payment_page = path == "/payment"
    # Önce /payment/success: Google Ads conversion için CSP her ortamda aynı (ENVIRONMENT'dan bağımsız)
    if is_payment_success:
        response.headers["Content-Security-Policy"] = _CSP_PAYMENT_SUCCESS
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        response.headers["X-Norya-CSP"] = "payment-success"  # Debug: bu sayfada gevşek CSP uygulandığını doğrula
        # Cloudflare: Bu URL cache'lenmesin. Sorun sürerse Rules → Page Rules → *noryaai.com/payment/success* → Cache Level: Bypass
    elif is_payment_page:
        # Ödeme formu: Google Ads / GA4 / Tag Assistant script ve istekleri izinli
        response.headers["Content-Security-Policy"] = _CSP_PAYMENT_PAGE
    if getattr(settings, "environment", "development") == "production":
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
        if not is_payment_success and not is_payment_page:
            # Genel sayfalar için CSP (landing, blog, vs.). GA + Google Ads / Tag Assistant isteklerine izin ver.
            _csp = (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.tailwindcss.com "
                "https://www.googletagmanager.com https://googletagmanager.com "
                "https://www.googleadservices.com https://googleadservices.com "
                "https://googleads.g.doubleclick.net https://www.google.com; "
                "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; "
                "img-src 'self' data: blob: https://www.google.com https://www.google.com.tr "
                "https://googleads.g.doubleclick.net https://www.google-analytics.com https://www.googletagmanager.com; "
                "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com "
                "https://www.google.com https://www.googletagmanager.com "
                "https://googleads.g.doubleclick.net https://www.googleadservices.com; "
                "frame-ancestors 'self';"
            )
            response.headers["Content-Security-Policy"] = _csp
    return response


@app.middleware("http")
async def inject_tracking_ids(request: Request, call_next):
    """Şablonlarda kullanılmak üzere GA ve Google Ads kimliklerini request.state'e yazar."""
    request.state.ga_measurement_id = (getattr(settings, "ga_measurement_id", "") or "").strip()
    request.state.google_ads_conversion_id = (getattr(settings, "google_ads_conversion_id", "") or "").strip()
    request.state.google_site_verification = (getattr(settings, "google_site_verification", "") or "").strip()
    return await call_next(request)


@app.middleware("http")
async def request_id_and_latency(request: Request, call_next):
    request.state.request_id = str(uuid.uuid4())
    start = time.perf_counter()
    response = await call_next(request)
    latency_ms = (time.perf_counter() - start) * 1000
    response.headers["X-Request-ID"] = request.state.request_id
    log.info(
        "request_id=%s method=%s path=%s status=%s latency_ms=%.2f",
        request.state.request_id,
        request.method,
        request.url.path,
        response.status_code,
        latency_ms,
    )
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ForceHTTPSRedirectMiddleware:
    """Production'da HTTP istekleri HTTPS'e 302 ile yönlendirir (proxy: X-Forwarded-Proto/Host). PayTR güvenli site görsün."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope.get("type") != "http":
            await self.app(scope, receive, send)
            return
        if getattr(settings, "environment", "").lower() != "production":
            await self.app(scope, receive, send)
            return
        if not getattr(settings, "force_https_redirect", True):
            await self.app(scope, receive, send)
            return
        h = {k: v for k, v in (scope.get("headers") or [])}
        proto = (h.get(b"x-forwarded-proto") or b"").decode("utf-8", errors="ignore").strip().lower()
        if proto == "https":
            await self.app(scope, receive, send)
            return
        host = (h.get(b"x-forwarded-host") or h.get(b"host") or b"").decode("utf-8", errors="ignore").strip()
        # Local geliştirme: localhost / 127.0.0.1 için HTTPS yönlendirme yapma (yerelde SSL yok)
        if not host or host.startswith("127.0.0.1") or host.startswith("localhost") or host == "[::1]":
            await self.app(scope, receive, send)
            return
        if not host:
            host = scope.get("server") and f"{scope['server'][0]}:{scope['server'][1]}" or "localhost"
        path = (scope.get("path") or "/").strip() or "/"
        query = scope.get("query_string")
        if query:
            path = path + "?" + (query.decode() if isinstance(query, bytes) else query)
        redirect_url = f"https://{host}{path}"
        response = RedirectResponse(url=redirect_url, status_code=302)
        await response(scope, receive, send)


app.add_middleware(ForceHTTPSRedirectMiddleware)

app.include_router(auth_router)
app.include_router(auth_router, prefix="/v1")  # Geriye uyumlu: /v1/auth/login vb.
app.include_router(institution_api_router)
app.include_router(institution_page_router)
app.include_router(enterprise_router)
app.include_router(new_admin_router)  # Yeni modüler admin (Jinja2); /admin/ -> login/dashboard
# GET /admin (slash yok) için her zaman önce login sayfası açılsın
@app.get("/admin")
def admin_redirect():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/admin/login", status_code=302)

app.include_router(admin_router)  # Eski API paneli: /admin/stats, /admin/analyses, vb.


# Ana sayfa (/) en başta kaydedilsin; GET, HEAD, OPTIONS, POST desteklensin, 405 önlensin
@app.get("/")
@app.get("")
def index(request: Request):
    """Ana sayfa: tarayıcı GET ile açıldığında index.html döner."""
    return _index_response(request)


@app.head("/")
@app.head("")
def index_head():
    """HEAD / : CDN/proxy health check; aynı yanıt başlıkları, gövde yok."""
    return Response(status_code=200)


@app.options("/")
@app.options("")
def index_options():
    """OPTIONS / : CORS preflight; 200 döndür, Method Not Allowed önlenir."""
    return Response(status_code=200)


@app.post("/")
@app.post("")
def index_post(request: Request):
    """Ana sayfa POST: form veya yönlendirme bazen POST gönderir; 405 yerine aynı sayfayı döndür."""
    return _index_response(request)


# Country-based landing: /tr, /en, /en-ca, /de, /it — aynı component, locale'den beslenen içerik
@app.get("/tr", response_class=HTMLResponse)
def landing_tr(request: Request):
    return _landing_response("tr", request)


@app.get("/en", response_class=HTMLResponse)
def landing_en(request: Request):
    return _landing_response("en", request)


@app.get("/en-ca", response_class=HTMLResponse)
def landing_en_ca(request: Request):
    return _landing_response("en-ca", request)


@app.get("/de", response_class=HTMLResponse)
def landing_de(request: Request):
    return _landing_response("de", request)


@app.get("/de/faq", response_class=HTMLResponse)
def faq_de(request: Request):
    """
    Almanca FAQ sayfası: /de/faq
    Landing'deki DE FAQ içeriğini tek sayfada gösterir.
    """
    lang = "de"
    base_url = str(request.base_url).rstrip("/")
    t = get_landing_ui(lang)
    meta_landing = get_landing_meta(lang)
    meta = {
        "meta_title": meta_landing.get("faq_title") or meta_landing.get("meta_title", f"{BRAND_NAME} FAQ"),
        "meta_description": meta_landing.get("faq_subtitle") or meta_landing.get("meta_description", ""),
    }
    canonical_url = f"{base_url}/de/faq"
    og_image = f"{base_url}/static/images/og-default.png"
    faq_entities = []
    for i in range(1, 7):
        q = t.get(f"faq_q{i}")
        a = t.get(f"faq_a{i}")
        if q and a:
            faq_entities.append(
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            )
    faq_schema_json = json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_entities},
        ensure_ascii=False,
    ) if faq_entities else None
    return templates.TemplateResponse(
        "faq.html",
        {
            "request": request,
            "lang": lang,
            "t": t,
            "meta": meta,
            "canonical_url": canonical_url,
            "og_locale": "de_DE",
            "og_image": og_image,
            "base_url": base_url,
            "faq_schema_json": faq_schema_json,
        },
    )


@app.get("/it", response_class=HTMLResponse)
def landing_it(request: Request):
    return _landing_response("it", request)


@app.get("/yonetim", response_class=HTMLResponse)
@app.get("/yonetim/", response_class=HTMLResponse)
def admin_yonetim():
    """Eski URL: /yonetim -> /admin yönlendir."""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/admin", status_code=302)


# PWA: Service worker kökten sunulur (scope / için)
if STATIC_DIR.is_dir():
    _sw_path = STATIC_DIR / "sw.js"
    if _sw_path.is_file():
        @app.get("/sw.js", response_class=PlainTextResponse)
        def serve_sw():
            return PlainTextResponse(
                _sw_path.read_text(encoding="utf-8"),
                media_type="application/javascript; charset=utf-8",
            )
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/ping")
def ping():
    """Hafif keep-alive: dış ping servisleri (UptimeRobot vb.) bu URL'yi periyodik çağırarak
    Render free tier servisin uyumasını önler. DB/OpenAI yok, sadece 200 döner."""
    return {"status": "ok"}


@app.get("/health")
def health():
    openai_configured = is_openai_configured()
    database_status = "ok"
    try:
        with Session(engine) as s:
            s.execute(text("SELECT 1"))
    except Exception as e:
        database_status = "error"
        log.warning("Health check DB failed: %s", e)
    return {
        "status": "ok",
        "openai_configured": openai_configured,
        "database": database_status,
    }


# /health/ai: OpenAI erişim kontrolü, 60 sn TTL cache (admin dashboard için)
_AI_HEALTH_CACHE: dict = {"ts": 0.0, "data": None}
_AI_HEALTH_CACHE_TTL = 60.0


@app.get("/health/ai")
def health_ai():
    """AI (OpenAI) durumu: status, provider, latency_ms, error. 60 sn cache."""
    import time as _time
    from app.services.analyze import ping_openai

    now = _time.time()
    cache = _AI_HEALTH_CACHE
    if cache["data"] is not None and (now - cache["ts"]) < _AI_HEALTH_CACHE_TTL:
        return cache["data"]

    ok, latency_ms, err = ping_openai()
    if ok:
        data = {"status": "ok", "provider": "openai", "latency_ms": latency_ms}
    else:
        data = {
            "status": "fail",
            "provider": "openai",
            "latency_ms": latency_ms,
            "error": err or "Bilinmeyen hata",
        }
    cache["ts"] = now
    cache["data"] = data
    return data


# Ülke kodu -> dil kodu. Global: tr, en, de, ar, he, hi, it, es, fr
COUNTRY_TO_LANG = {
    "TR": "tr",
    "US": "en", "GB": "en", "AU": "en", "CA": "en", "IE": "en", "NZ": "en",
    "DE": "de", "AT": "de", "CH": "de",
    "IL": "he",
    "SA": "ar", "EG": "ar", "AE": "ar", "QA": "ar", "JO": "ar", "LB": "ar", "SY": "ar", "IQ": "ar", "KW": "ar", "BH": "ar", "OM": "ar", "YE": "ar", "PS": "ar", "MA": "ar", "DZ": "ar", "TN": "ar",
    "IN": "hi",
    "FR": "fr", "ES": "es", "IT": "it", "NL": "nl", "PL": "pl", "RU": "ru",
    "GR": "el", "CY": "el",
    "CZ": "cs",
    "RS": "sr", "BA": "sr", "ME": "sr",
}
DEFAULT_LANG = "en"

# Ülke kodu -> para birimi (sizin tahsilat EUR; ziyaretçiye kendi para biriminde gösterilir)
COUNTRY_TO_CURRENCY = {
    "TR": "TRY", "US": "USD", "GB": "GBP", "AU": "AUD", "CA": "CAD", "SA": "SAR", "AE": "AED",
    "QA": "QAR", "KW": "KWD", "BH": "BHD", "OM": "OMR", "EG": "EGP", "JO": "JOD", "IL": "ILS",
    "IN": "INR", "RU": "RUB", "CH": "CHF", "PL": "PLN", "MA": "MAD", "DZ": "DZD", "TN": "TND",
    "GR": "EUR", "CY": "EUR", "CZ": "CZK", "RS": "RSD", "BA": "BAM", "ME": "EUR",
}
# Varsayılan EUR fiyatları (pricing service DB'den döndüremezse kullanılır)
EUR_BASE_FALLBACK = {"single": 14.04, "monthly": 54, "yearly": 106.92}
# Varsayılan kurlar (API yanıt vermezse kullanılır)
EUR_RATES_FALLBACK = {
    "EUR": 1.0, "USD": 1.08, "GBP": 0.85, "TRY": 34.5, "SAR": 4.05, "AED": 3.97, "QAR": 3.94,
    "KWD": 0.33, "BHD": 0.41, "OMR": 0.42, "EGP": 33.0, "JOD": 0.77, "ILS": 4.0, "INR": 90.0,
    "RUB": 100.0, "CHF": 0.95, "AUD": 1.65, "CAD": 1.47, "PLN": 4.3, "MAD": 10.8, "DZD": 145.0, "TND": 3.35,
    "CZK": 27.0, "RSD": 117.0, "BAM": 1.96,
}
CURRENCY_SYMBOLS = {
    "EUR": "€", "USD": "$", "GBP": "£", "TRY": "₺", "SAR": "ر.س", "AED": "د.إ", "QAR": "ر.ق",
    "KWD": "د.ك", "BHD": "د.ب", "OMR": "ر.ع", "EGP": "E£", "JOD": "د.أ", "ILS": "₪", "INR": "₹",
    "RUB": "₽", "CHF": "CHF", "AUD": "A$", "CAD": "C$", "PLN": "zł", "MAD": "DH", "DZD": "DA", "TND": "DT",
    "CZK": "Kč", "RSD": "дин.", "BAM": "KM",
}

# Otomatik kur: Frankfurter API (ECB kurları, günlük). Cache 6 saat.
_EUR_RATES_CACHE: dict[str, float] = {}
_EUR_RATES_CACHE_TIME: float = 0
_EUR_RATES_CACHE_TTL = 6 * 3600  # 6 saat saniye


def _fetch_eur_rates_live() -> dict[str, float]:
    """Frankfurter API ile güncel EUR kurlarını çeker. Hata/yanıt yoksa fallback döner."""
    global _EUR_RATES_CACHE, _EUR_RATES_CACHE_TIME
    now = time.time()
    if _EUR_RATES_CACHE and (now - _EUR_RATES_CACHE_TIME) < _EUR_RATES_CACHE_TTL:
        return _EUR_RATES_CACHE
    try:
        with urlopen("https://api.frankfurter.app/latest?from=EUR", timeout=4) as r:
            import json
            data = json.loads(r.read().decode())
        rates = data.get("rates") or {}
        if isinstance(rates, dict) and rates:
            rates["EUR"] = 1.0
            _EUR_RATES_CACHE = {k: float(v) for k, v in rates.items()}
            _EUR_RATES_CACHE_TIME = now
            return _EUR_RATES_CACHE
    except (URLError, OSError, ValueError, KeyError):
        pass
    return EUR_RATES_FALLBACK.copy()


def _parse_accept_language(header: str | None) -> str:
    """Accept-Language başlığından tercih edilen dili döner."""
    if not header:
        return DEFAULT_LANG
    for part in header.split(","):
        part = part.strip().split(";")[0].strip().lower()
        if part.startswith("tr"): return "tr"
        if part.startswith("en"): return "en"
        if part.startswith("de"): return "de"
        if part.startswith("he"): return "he"
        if part.startswith("ar"): return "ar"
        if part.startswith("hi"): return "hi"
        if part.startswith("it"): return "it"
        if part.startswith("es"): return "es"
        if part.startswith("fr"): return "fr"
        if part.startswith("el"): return "el"
        if part.startswith("cs"): return "cs"
        if part.startswith("sr"): return "sr"
    return DEFAULT_LANG


def _get_country_from_request(request: Request) -> str | None:
    client_ip = request.client.host if request.client else None
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()
    if not client_ip or client_ip in ("127.0.0.1", "::1", "localhost"):
        return None
    try:
        with urlopen(f"http://ip-api.com/json/{client_ip}?fields=countryCode", timeout=2) as r:
            import json
            data = json.loads(r.read().decode())
            return data.get("countryCode")
    except (URLError, OSError, ValueError, KeyError):
        return None


def _report_lang_from_request(request: Request, site_lang: str | None) -> str:
    """
    Rapor dili: önce sitede seçilen dil (site_lang), yoksa isteğin geldiği ülkeye (IP) göre.
    """
    if site_lang and site_lang.strip():
        return site_lang.strip().lower()
    country = _get_country_from_request(request)
    if country and country.upper() in COUNTRY_TO_LANG:
        return COUNTRY_TO_LANG[country.upper()]
    return DEFAULT_LANG


@app.get("/api/locale")
def get_locale(request: Request):
    """
    Kullanıcının dilini önerir: IP ülkesi veya Accept-Language.
    Döner: { "suggested": "tr" | "en" | ... , "countryCode": "TR" | null }
    """
    accept = request.headers.get("accept-language")
    lang_from_browser = _parse_accept_language(accept)
    country = _get_country_from_request(request)
    if country and country in COUNTRY_TO_LANG:
        return {"suggested": COUNTRY_TO_LANG[country], "countryCode": country}
    return {"suggested": lang_from_browser, "countryCode": country}


def _pricing_response(currency: str, rate: float, eur_base: dict[str, float] | None = None) -> dict:
    """Tek bir para birimi ve kur için fiyat yanıtı. eur_base yoksa EUR_BASE_FALLBACK kullanılır."""
    base = eur_base or EUR_BASE_FALLBACK
    symbol = CURRENCY_SYMBOLS.get(currency, currency + " ")
    decimals = 0 if currency in ("JPY", "KRW") else 2
    return {
        "currency": currency,
        "symbol": symbol,
        "single": round(base["single"] * rate, decimals),
        "monthly": round(base["monthly"] * rate, decimals),
        "yearly": round(base["yearly"] * rate, decimals),
        "note": "pricing_note_" + currency.lower(),
    }


@app.get("/api/pricing")
def get_pricing(
    request: Request,
    country: str | None = None,
    db: Session = Depends(get_db),
):
    """
    Merkezi fiyat kaynağı (PricingPlan). Ülkeye göre yerel para biriminde döner.
    Kampanya aktifse campaign_* alanları dolu döner (landing/payment aynı veriyi kullanır).
    """
    try:
        base_cents = get_base_prices_cents(db)
        eur_base = {k: v / 100.0 for k, v in base_cents.items()}
    except Exception:
        eur_base = dict(EUR_BASE_FALLBACK)
    currency, rate = "EUR", 1.0
    try:
        country = (country or _get_country_from_request(request) or "DE").upper()[:2]
        currency = COUNTRY_TO_CURRENCY.get(country, "EUR")
        rates = _fetch_eur_rates_live()
        rate = float(rates.get(currency, EUR_RATES_FALLBACK.get(currency, 1.0)))
    except Exception:
        rates = {}
    out = _pricing_response(currency, rate, eur_base)
    # Kampanya: her plan için original/discounted (landing’de üstü çizili + yeni fiyat)
    decimals = 0 if out.get("currency") in ("JPY", "KRW") else 2
    for product, plan_code in (("single", "single_13eur"), ("monthly", "monthly_50eur"), ("yearly", "yearly_99eur")):
        base_val = out.get(product, 0)
        out[f"{product}_original"] = base_val
        out[f"{product}_discounted"] = base_val
    out["campaign_active"] = False
    out["campaign_badge"] = ""
    out["campaign_discount_value"] = 0
    out["campaign_discount_type"] = ""
    out["campaign_promo_code"] = ""
    try:
        for plan_code in ("yearly_99eur", "monthly_50eur", "single_13eur"):
            campaign = get_active_campaign_with_display(db, plan_code)
            if campaign:
                product = (get_plan_code_to_product_cents(db).get(plan_code) or (None, 0))[0]
                if not product:
                    continue
                old_c = campaign.get("old_price_cents")
                new_c = campaign.get("new_price_cents")
                if old_c is not None and new_c is not None:
                    out["campaign_active"] = True
                    out["campaign_badge"] = (campaign.get("campaign_badge") or "").strip()
                    out["campaign_discount_value"] = campaign.get("discount_value") or 0
                    out["campaign_discount_type"] = campaign.get("discount_type") or "percent"
                    out["campaign_promo_code"] = (campaign.get("code") or "").strip()
                    out[f"{product}_original"] = round(old_c / 100.0 * rate, decimals)
                    out[f"{product}_discounted"] = round(new_c / 100.0 * rate, decimals)
                break
    except Exception:
        pass
    return out


@app.get("/api/push/vapid-public")
def get_push_vapid_public():
    """PWA push bildirimleri için VAPID public key (base64url). Boşsa push kullanılamaz."""
    key = (getattr(settings, "vapid_public_key", None) or "").strip()
    if not key:
        return JSONResponse(content={"publicKey": None}, status_code=200)
    return {"publicKey": key}


@app.post("/api/push/subscribe")
async def push_subscribe(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Kullanıcının push aboneliğini kaydeder (PWA bildirimleri için)."""
    try:
        body = await request.json()
    except Exception:
        body = {}
    if not isinstance(body, dict):
        raise HTTPException(status_code=400, detail="Geçersiz istek.")
    endpoint = (body.get("endpoint") or "").strip()
    keys = body.get("keys") or {}
    p256dh = (keys.get("p256dh") or keys.get("p256dh") or "").strip()
    auth = (keys.get("auth") or "").strip()
    if not endpoint:
        raise HTTPException(status_code=400, detail="endpoint gerekli.")
    user_id = user.id or 0
    existing = db.exec(select(PushSubscription).where(PushSubscription.user_id == user_id, PushSubscription.endpoint == endpoint)).first()
    if existing:
        existing.p256dh = p256dh
        existing.auth = auth
        db.add(existing)
    else:
        db.add(PushSubscription(user_id=user_id, endpoint=endpoint, p256dh=p256dh, auth=auth))
    db.commit()
    return {"ok": True}


@app.get("/api-check")
def api_check():
    """OpenAI ve PayTR ayarları yüklü mü kontrol et (anahtarlar gösterilmez)."""
    key_ok = is_openai_configured()
    paytr_ok = _paytr_enabled()
    return {
        "openai_ayarli": key_ok,
        "paytr_ayarli": paytr_ok,
        "mesaj": "Anahtar tanımlı (sk-...)." if key_ok else "OPENAI_API_KEY .env'de eksik veya geçersiz (sk- ile başlamalı, boşluksuz).",
    }


# Test raporu: development'ta bu URL ile seçenek sayfası (PDF/HTML) veya yardım
@app.get("/dev/test-report")
async def dev_test_report():
    """Test raporu seçenek sayfası (PDF / HTML) veya rapor yoksa yardım. Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    report_path = _PROJ_ROOT / "test-reports" / "report.html"
    if report_path.is_file():
        # Rapor var: tek sayfada butonlarla PDF ve HTML linkleri (yanlış URL yazılmasın)
        index_html = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Test raporu</title>
<style>
  body { font-family: system-ui, sans-serif; padding: 2rem; max-width: 32rem; margin: 0 auto; }
  h1 { font-size: 1.5rem; margin-bottom: 0.5rem; }
  .sub { color: #64748b; font-size: 0.9375rem; margin-bottom: 1.5rem; }
  .links { display: flex; flex-wrap: wrap; gap: 0.75rem; }
  .btn { display: inline-block; padding: 0.75rem 1.25rem; border-radius: 8px; text-decoration: none; font-weight: 600; transition: opacity 0.2s; }
  .btn:hover { opacity: 0.9; }
  .btn-pdf { background: #0f172a; color: #fff; }
  .btn-html { background: #e2e8f0; color: #0f172a; }
  .back { margin-top: 1.5rem; font-size: 0.875rem; }
  .back a { color: #64748b; }
</style></head>
<body>
<h1>Test raporu</h1>
<p class="sub">Raporu aşağıdaki butonlarla açın (adres çubuğuna ek karakter yazmayın).</p>
<div class="links">
  <a href="/dev/test-report.pdf" class="btn btn-pdf" target="_blank" rel="noopener">PDF olarak aç</a>
  <a href="/dev/test-report/html" class="btn btn-html" target="_blank" rel="noopener">HTML raporu aç</a>
</div>
<p class="back"><a href="/">← Ana sayfa</a></p>
</body></html>"""
        return HTMLResponse(index_html)
    # Rapor yoksa açıklayıcı sayfa (tek satır komutlar, kopyala-yapıştır güvenli)
    help_html = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Test raporu</title></head>
<body style="font-family:sans-serif; padding:2rem; max-width:600px;">
<h1>Test raporu henüz yok</h1>
<p><strong>1.</strong> Terminali proje kökünde açın (Cursor: Terminal → New Terminal; veya <code>cd</code> ile norya klasörüne gidin).</p>
<p><strong>2.</strong> Aşağıdaki komutlardan <strong>birini</strong> tek satır olarak yapıştırıp Enter'a basın:</p>
<pre style="background:#f0f0f0; padding:1rem; border-radius:6px; overflow-x:auto;">cd /Users/ufukurhan/norya && ./scripts/run_tests_with_report.sh</pre>
<p>pytest kurulu değilse önce sanal ortam ve bağımlılıklar (bir kez):</p>
<pre style="background:#f0f0f0; padding:1rem; border-radius:6px; overflow-x:auto;">cd /Users/ufukurhan/norya && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt</pre>
<p>Sonra rapor için:</p>
<pre style="background:#f0f0f0; padding:1rem; border-radius:6px; overflow-x:auto;">cd /Users/ufukurhan/norya && ./scripts/run_tests_with_report.sh</pre>
<p>Bu sayfayı yenileyin; <strong>PDF olarak aç</strong> butonu görünecek.</p>
<p><a href="/">← Ana sayfa</a></p>
</body></html>"""
    return HTMLResponse(help_html)


@app.get("/dev/test-report/html")
async def dev_test_report_html():
    """Ham pytest HTML raporu (sayfa içi linklerden açılır). Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    report_path = _PROJ_ROOT / "test-reports" / "report.html"
    if not report_path.is_file():
        raise HTTPException(status_code=404, detail="Test raporu yok. Önce: pytest")
    return FileResponse(str(report_path), media_type="text/html")


@app.get("/dev/test-report.pdf")
async def dev_test_report_pdf():
    """Test raporunu PDF olarak döndürür (WeasyPrint ile). Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    report_path = _PROJ_ROOT / "test-reports" / "report.html"
    if not report_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Test raporu yok. Önce: pytest veya ./scripts/run_tests_with_report.sh",
        )
    try:
        from weasyprint import HTML
        pdf_doc = HTML(filename=str(report_path))
        pdf_bytes = pdf_doc.write_pdf()
    except Exception as e:
        log.exception("Test report PDF conversion failed: %s", e)
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=test-report.pdf"},
    )


# Örnek müşteri raporu (kan tahlili PDF) — şablonu buradan açıp düzenleyebilirsiniz
_DEV_SAMPLE_RESULT_TEXT = """
**Özet**:
Genel durum iyi. Bazı parametreler referans sınırında. Beslenme ve hareket önerilir.

**Risk göstergeleri**:
LDL ve glukoz takip edilmeli.

**Değerler**:
**LDL**: 118 mg/dL Reference: 0-100. Normal.
**HDL**: 52 mg/dL Reference: 40-. Normal.
**Glucose**: 95 mg/dL Reference: 70-100. Normal.
**CRP**: 2.2 mg/L Reference: 0-3. Normal.
**Vitamin D**: 28 ng/mL Reference: 30-. Düşük.

**Olası nedenler**:
- D vitamini güneş ve diyetle desteklenebilir.

**Öneriler**:
- Düzenli kontrole devam edin. Doktorunuzla paylaşın.
"""
_DEV_SAMPLE_TREND_DATA = {
    "dates": ["01.01.2025", "15.01.2025", "01.02.2025"],
    "ldl": [128, 122, 118],
    "glucose": [98, 96, 95],
    "crp": [2.8, 2.5, 2.2],
}


@app.get("/dev/single-report-preview")
async def dev_single_report_preview(request: Request):
    """Tek analiz (single) rapor ekranı önizlemesi — giriş/ödeme olmadan tarayıcıda görüntülemek için. Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url="/?demo=single", status_code=302)


@app.get("/dev/sample-report")
async def dev_sample_report_page(request: Request):
    """Müşteri raporu önizleme sayfası (PDF/şablon düzenlerken buradan açın). Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    base = str(request.base_url).rstrip("/")
    index_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Müşteri raporu önizleme</title>
<style>
  body {{ font-family: system-ui, sans-serif; padding: 2rem; max-width: 32rem; margin: 0 auto; }}
  h1 {{ font-size: 1.35rem; margin-bottom: 0.5rem; }}
  .sub {{ color: #64748b; font-size: 0.9375rem; margin-bottom: 1.5rem; }}
  .btn {{ display: inline-block; padding: 0.75rem 1.25rem; border-radius: 8px; text-decoration: none; font-weight: 600; background: #0f172a; color: #fff; margin-right: 0.5rem; margin-bottom: 0.5rem; }}
  .btn:hover {{ opacity: 0.9; }}
  .back {{ margin-top: 1.5rem; font-size: 0.875rem; }}
  .back a {{ color: #64748b; }}
</style></head>
<body>
<h1>Müşteri raporu önizleme</h1>
<p class="sub">Kan tahlili raporu PDF’i (report_premium.html). Şablonu düzenleyip sayfayı yenileyin.</p>
<a href="/dev/sample-report.pdf" class="btn" target="_blank" rel="noopener">PDF olarak aç</a>
<a href="/dev/single-report-preview" class="btn" target="_blank" rel="noopener">Tek analiz rapor önizlemesi (SPA)</a>
<p class="back"><a href="/">← Ana sayfa</a> · <a href="/dev/test-report">Test raporu</a></p>
</body></html>"""
    return HTMLResponse(index_html)


@app.get("/dev/sample-report.pdf")
async def dev_sample_report_pdf(request: Request):
    """Müşteri kan tahlili raporu örnek PDF (report_premium.html ile). Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    base_url = str(request.base_url).rstrip("/")
    report_id = "dev-sample-12345"
    token = "dev-token"
    verification_url = f"{base_url}/verify/{report_id}?token={token}"
    verification_info = None
    try:
        from app.services.report_verification import _qr_png_base64
        qr_b64 = _qr_png_base64(verification_url)
        verification_info = {
            "report_id": report_id,
            "verification_code": "DEV-SAMPLE",
            "verification_url": verification_url,
            "qr_image_base64": qr_b64 or "",
        }
    except Exception as e:
        log.debug("Dev sample report: QR skipped: %s", e)
    try:
        pdf_bytes = build_report_pdf(
            result_text=_DEV_SAMPLE_RESULT_TEXT,
            report_date=datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M"),
            lang="tr",
            report_id="DEV-001",
            user_identifier="dev@norya.com",
            patient_name="Örnek Kullanıcı",
            plan_name="premium",
            source_type="text",
            trend_data=_DEV_SAMPLE_TREND_DATA,
            verification_info=verification_info,
        )
    except Exception as e:
        log.exception("Dev sample report PDF failed: %s", e)
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=norya-ornek-rapor.pdf"},
    )


@app.get("/dev/monthly-sample-report.pdf")
async def dev_monthly_sample_report_pdf(request: Request):
    """Aylık (monthly) paket için örnek PDF (report_premium.html ile). Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")

    base_url = str(request.base_url).rstrip("/")
    report_id = "dev-monthly-sample-12345"
    token = "dev-token"
    verification_url = f"{base_url}/verify/{report_id}?token={token}"
    verification_info = None
    try:
        from app.services.report_verification import _qr_png_base64
        qr_b64 = _qr_png_base64(verification_url)
        verification_info = {
            "report_id": report_id,
            "verification_code": "DEV-MONTHLY-SAMPLE",
            "verification_url": verification_url,
            "qr_image_base64": qr_b64 or "",
        }
    except Exception as e:
        log.debug("Dev monthly sample report: QR skipped: %s", e)

    try:
        pdf_bytes = build_report_pdf(
            result_text=_DEV_SAMPLE_RESULT_TEXT,
            report_date=datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M"),
            lang="tr",
            report_id="DEV-MONTHLY-001",
            user_identifier="dev-monthly@norya.com",
            patient_name="Örnek Kullanıcı (Aylık)",
            plan_name="monthly",
            source_type="text",
            trend_data=_DEV_SAMPLE_TREND_DATA,
            verification_info=verification_info,
        )
    except Exception as e:
        log.exception("Dev monthly sample report PDF failed: %s", e)
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=norya-ornek-rapor-aylik.pdf"},
    )


@app.get("/dev/single-plan-test.pdf")
async def dev_single_plan_test_pdf(request: Request):
    """Single plan PDF testi — aynı örnek metinle plan_name='single' ile PDF. Production'da 404."""
    if getattr(settings, "environment", "development").strip().lower() == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    verification_info = None
    try:
        base_url = str(request.base_url).rstrip("/")
        report_id = "single-plan-test"
        token = "dev-token"
        verification_url = f"{base_url}/verify/{report_id}?token={token}"
        from app.services.report_verification import _qr_png_base64

        verification_info = {
            "report_id": report_id,
            "verification_code": "DEV-SAMPLE",
            "verification_url": verification_url,
            "qr_image_base64": _qr_png_base64(verification_url) or "",
        }
    except Exception:
        verification_info = None

    try:
        pdf_bytes = build_report_pdf(
            result_text=_DEV_SAMPLE_RESULT_TEXT,
            report_date=datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M"),
            lang="tr",
            report_id="single-plan-test",
            user_identifier="test@norya.com",
            # Standart SINGLE/STANDARD akışını test etmek için premium şablon yerine standart PDF şablonu kullanılsın.
            plan_name="free",
            source_type="text",
            verification_info=verification_info,
        )
    except Exception as e:
        log.exception("Single plan test PDF failed: %s", e)
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=norya-single-plan-test.pdf"},
    )


# DEBUG ONLY: Rate limit + GA debug — production'da kapalı
if getattr(settings, "environment", "development") != "production":
    @app.get("/debug/rate-test")
    @limiter.limit("5/minute")
    async def debug_rate_test(request: Request):
        """Rate limit'i test etmek için basit endpoint. Global SlowAPI limitine tabidir."""
        return {"ok": True}

    @app.get("/debug/ga", response_class=HTMLResponse)
    async def debug_ga(request: Request):
        """GA4 Measurement ID ve CSP bilgisini gösterir (doğrulama için). Production'da 404."""
        ga_id = (getattr(settings, "ga_measurement_id", "") or "G-1FLMLJH3Q0").strip()
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.tailwindcss.com https://www.googletagmanager.com; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data: blob: https:; "
            "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com; frame-ancestors 'self';"
        )
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Debug GA</title></head>
<body style="font-family:sans-serif; padding:1.5rem; max-width:640px;">
<h1>GA4 Debug</h1>
<p><strong>Measurement ID:</strong> <code>{ga_id}</code></p>
<p>Bu sayfada tag yüklü olmalı. Realtime test için gizli sekmede site açıp 1-2 sayfa gezin.</p>
<h2>Content-Security-Policy (production)</h2>
<pre style="background:#f0f0f0; padding:0.75rem; overflow-x:auto; font-size:0.85rem;">{csp}</pre>
<p><a href="/">← Ana sayfa</a></p>
</body></html>"""
        return HTMLResponse(html)


# Google Ads global site tag — tüm sayfalarda tek gtag yüklemesi için kullanılır
GOOGLE_ADS_GLOBAL_TAG_ID = "AW-18004536281"


# Placeholder in static/index.html (and any HTML served with _inject_ga); replaced by real gtag script.
_GTAG_INJECT_PLACEHOLDER = "  <!-- NORYA_GTAG_INJECT -->"


def _inject_ga(html: str) -> str:
    """Google Ads (AW-18004536281) ve isteğe bağlı GA4 gtag'ini placeholder yerine koyar. Tek script, tek yükleme."""
    ga_id = (getattr(settings, "ga_measurement_id", "") or "").strip()
    aw_id = (getattr(settings, "google_ads_conversion_id", "") or "").strip() or GOOGLE_ADS_GLOBAL_TAG_ID
    first_id = ga_id or aw_id
    configs = []
    if ga_id:
        configs.append(f'gtag("config","{ga_id}");')
    configs.append(f'gtag("config","{aw_id}");')
    inject = (
        f'<script async src="https://www.googletagmanager.com/gtag/js?id={first_id}"></script>\n'
        f'  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());{" ".join(configs)}</script>\n  '
    )
    return html.replace(_GTAG_INJECT_PLACEHOLDER, inject)


WHATSAPP_GREETINGS: dict[str, str] = {
    "tr": "Merhaba, Norya hakkında soru sormak istiyorum.",
    "en": "Hello, I would like to ask a question about Norya.",
    "de": "Hallo, ich möchte eine Frage zu Norya stellen.",
    "fr": "Bonjour, je voudrais poser une question sur Norya.",
    "it": "Ciao, vorrei fare una domanda su Norya.",
    "es": "Hola, me gustaría hacer una pregunta sobre Norya.",
    "he": "שלום, אני רוצה לשאול שאלה על Norya.",
    "hi": "नमस्ते, मैं Norya के बारे में एक सवाल पूछना चाहता/चाहती हूँ।",
    "ar": "مرحبًا، أود طرح سؤال حول Norya.",
    "el": "Γεια σας, θα ήθελα να κάνω μια ερώτηση σχετικά με το Norya.",
    "sr": "Zdravo, želim da postavim pitanje o Norya.",
    "cs": "Dobrý den, chtěl/a bych se zeptat na Norya.",
    "en-ca": "Hello, I would like to ask a question about Norya.",
}


def _whatsapp_url_and_style(locale: str = "tr") -> tuple[str, str]:
    """WhatsApp iletişim: (href, style). Numara yoksa varsayılan kullanılır, yine de gizlenmez. Mesaj locale'e göre çevrilir."""
    num = (getattr(settings, "whatsapp_contact", None) or "905071703564").strip().replace("+", "").replace(" ", "")
    if not num or len(num) < 10:
        num = "905071703564"
    greeting = WHATSAPP_GREETINGS.get(locale, WHATSAPP_GREETINGS["en"])
    text = quote(greeting)
    return f"https://wa.me/{num}?text={text}", ""


def _inject_whatsapp(html: str, locale: str = "tr") -> str:
    """__NORYA_WHATSAPP_URL__ ve __NORYA_WHATSAPP_STYLE__ placeholder'larını doldurur. Locale'e göre mesaj dili değişir."""
    url, style = _whatsapp_url_and_style(locale)
    html = html.replace("__NORYA_WHATSAPP_URL__", url)
    html = html.replace("__NORYA_WHATSAPP_STYLE__", style)
    return html


def _inject_company(html: str) -> str:
    """Şirket bilgileri placeholder'larını config'den doldurur (footer, hakkımızda). Boşsa — gösterilir."""
    _fallback = "—"
    title = (settings.company_title or settings.invoice_company_title or "").strip() or _fallback
    tax_office = (settings.company_tax_office or settings.invoice_company_tax_office or "").strip() or _fallback
    tax_no = (settings.company_tax_number or settings.gib_earsiv_user or "").strip() or _fallback
    address = (settings.company_address or settings.invoice_company_address or "").strip() or _fallback
    phone = (settings.company_phone or "").strip() or _fallback
    if phone and phone != _fallback and phone.isdigit():
        phone = "+90 " + phone
    html = html.replace("__NORYA_COMPANY_TITLE__", title)
    html = html.replace("__NORYA_COMPANY_TAX_OFFICE__", tax_office)
    html = html.replace("__NORYA_COMPANY_TAX_NO__", tax_no)
    html = html.replace("__NORYA_COMPANY_ADDRESS__", address)
    html = html.replace("__NORYA_COMPANY_PHONE__", phone)
    return html


_GSC_VERIFICATION_PLACEHOLDER = "  <!-- NORYA_GSC_VERIFICATION -->"


def _inject_google_site_verification(html: str) -> str:
    """Search Console HTML etiketi: static/index.html içindeki placeholder'ı meta ile değiştirir."""
    from html import escape

    token = (getattr(settings, "google_site_verification", "") or "").strip()
    if not token:
        return html.replace(_GSC_VERIFICATION_PLACEHOLDER + "\n", "").replace(_GSC_VERIFICATION_PLACEHOLDER, "")
    meta = f'  <meta name="google-site-verification" content="{escape(token, quote=True)}" />'
    if _GSC_VERIFICATION_PLACEHOLDER in html:
        return html.replace(_GSC_VERIFICATION_PLACEHOLDER, meta, 1)
    return html


LEGAL_PAGES = {
    "mesafeli-satis-sozlesmesi",
    "gizlilik-politikasi",
    "iade-iptal-politikasi",
    "kvkk-gdpr",
    "kullanim-sartlari",
    "iletisim",
}


def _legal_lang_from_request(request: Request) -> str:
    """Yasal sayfa dili: ?lang=, norya_lang çerezi, yoksa Accept-Language."""
    lang_q = (request.query_params.get("lang") or "").strip().lower()[:2]
    if lang_q in LEGAL_LANGS:
        return lang_q
    cookie = (request.cookies.get("norya_lang") or "").strip().lower()[:2]
    if cookie in LEGAL_LANGS:
        return cookie
    return _parse_accept_language(request.headers.get("accept-language"))


PAYMENT_LANGS = ("tr", "en", "de", "fr", "it", "es", "he", "hi", "ar")


def _payment_lang_from_request(request: Request) -> str:
    """Ödeme sayfası dili: sitede seçilen dil (cookie) veya ?lang= veya tarayıcı dili."""
    lang_q = (request.query_params.get("lang") or "").strip().lower()[:2]
    if lang_q in PAYMENT_LANGS:
        return lang_q
    lang_cookie = (request.cookies.get("norya_lang") or "").strip().lower()[:2]
    if lang_cookie in PAYMENT_LANGS:
        return lang_cookie
    browser = _parse_accept_language(request.headers.get("accept-language"))
    # Bilinmeyen tarayıcı dili için TR yerine EN: HE/HI/AR vb. kullanıcılar yanlışlıkla Türkçe görmesin.
    return browser if browser in PAYMENT_LANGS else "en"


@app.get("/kvkk")
def redirect_kvkk():
    return RedirectResponse(url="/legal/kvkk-gdpr", status_code=302)


@app.get("/privacy-policy")
def redirect_privacy():
    return RedirectResponse(url="/legal/gizlilik-politikasi", status_code=302)


@app.get("/refund-policy")
def redirect_refund():
    return RedirectResponse(url="/iade-iptal", status_code=302)


@app.get("/distance-sales")
def redirect_distance_sales():
    return RedirectResponse(url="/legal/mesafeli-satis-sozlesmesi", status_code=302)


@app.get("/terms")
def redirect_terms():
    return RedirectResponse(url="/legal/kullanim-sartlari", status_code=302)


@app.get("/legal/{page}", response_class=HTMLResponse)
def legal_page(request: Request, page: str):
    """Yasal sayfalar: müşteri diline göre (?lang= veya Accept-Language) içerik sunulur."""
    if page not in LEGAL_PAGES:
        raise HTTPException(status_code=404, detail="Sayfa bulunamadı")
    lang = _legal_lang_from_request(request)
    ui = get_legal_ui(lang)
    content = get_legal_content(page, lang)
    if not content:
        raise HTTPException(status_code=404, detail="Sayfa bulunamadı")
    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/legal/{page}"
    hreflang_alternates = [{"lang": code, "url": f"{base_url}/legal/{page}?lang={code}"} for code in LEGAL_HREFLANG_LANGS]
    hreflang_alternates.append({"lang": "x-default", "url": f"{base_url}/legal/{page}?lang=en"})
    page_title = content.get("title", page) if content else page
    breadcrumb_items = [
        {"@type": "ListItem", "position": 1, "name": BRAND_NAME, "item": base_url},
        {"@type": "ListItem", "position": 2, "name": ui.get("nav_legal", "Legal"), "item": f"{base_url}/legal/{page}"},
        {"@type": "ListItem", "position": 3, "name": page_title, "item": canonical_url},
    ]
    breadcrumb_schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": breadcrumb_items}
    breadcrumb_schema_json = json.dumps(breadcrumb_schema, ensure_ascii=False, indent=2)
    ctx = {"request": request, "content": content, "canonical_url": canonical_url, "breadcrumb_schema_json": breadcrumb_schema_json, "hreflang_alternates": hreflang_alternates, **ui}
    if page == "iletisim":
        return templates.TemplateResponse("legal/legal_contact.html", ctx)
    return templates.TemplateResponse("legal/legal_article.html", ctx)


@app.get("/iade-iptal", response_class=HTMLResponse)
def iade_iptal_page(request: Request):
    """İade ve İptal Politikası — müşteri diline göre (?lang= veya Accept-Language)."""
    lang = _legal_lang_from_request(request)
    ui = get_legal_ui(lang)
    content = get_legal_content("iade-iptal-politikasi", lang)
    if not content:
        raise HTTPException(status_code=404, detail="Sayfa bulunamadı")
    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/iade-iptal"
    hreflang_alternates = [{"lang": code, "url": f"{base_url}/iade-iptal?lang={code}"} for code in LEGAL_HREFLANG_LANGS]
    hreflang_alternates.append({"lang": "x-default", "url": f"{base_url}/iade-iptal?lang=en"})
    breadcrumb_items = [
        {"@type": "ListItem", "position": 1, "name": BRAND_NAME, "item": base_url},
        {"@type": "ListItem", "position": 2, "name": ui.get("nav_legal", "Legal"), "item": base_url + "/iade-iptal"},
        {"@type": "ListItem", "position": 3, "name": content.title if content else "Refund", "item": canonical_url},
    ]
    breadcrumb_schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": breadcrumb_items}
    breadcrumb_schema_json = json.dumps(breadcrumb_schema, ensure_ascii=False, indent=2)
    return templates.TemplateResponse(
        "legal/legal_article.html",
        {"request": request, "content": content, "canonical_url": canonical_url, "breadcrumb_schema_json": breadcrumb_schema_json, "hreflang_alternates": hreflang_alternates, **ui},
    )


REFUND_LANGS = ("tr", "en", "de", "fr", "it", "es", "he", "hi", "ar")


def _refund_page_hreflang_alternates(base_url: str) -> list[dict]:
    u = f"{base_url.rstrip('/')}/iade-talebi"
    alts = [{"lang": code, "url": f"{u}?lang={code}"} for code in LEGAL_HREFLANG_LANGS]
    alts.append({"lang": "x-default", "url": f"{u}?lang=en"})
    return alts


def _refund_lang_from_request(request: Request) -> str:
    """İade talebi dili: ?lang=, norya_lang, yoksa Accept-Language."""
    lang_q = (request.query_params.get("lang") or "").strip().lower()[:2]
    if lang_q in REFUND_LANGS:
        return lang_q
    cookie = (request.cookies.get("norya_lang") or "").strip().lower()[:2]
    if cookie in REFUND_LANGS:
        return cookie
    browser = _parse_accept_language(request.headers.get("accept-language"))
    return browser if browser in REFUND_LANGS else "en"


@app.get("/iade-talebi", response_class=HTMLResponse)
def refund_request_page(
    request: Request,
    lang: str = Query(None, description="Language override; else from browser"),
    success: str | None = Query(None),
    error: str | None = Query(None),
):
    """İade talep formu: dil tarayıcıdan otomatik (?lang= ile override)."""
    lang = _refund_lang_from_request(request)
    t = get_pay_ui(lang)
    ui = get_legal_ui(lang)
    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/iade-talebi"
    hreflang_alternates = _refund_page_hreflang_alternates(base_url)
    return templates.TemplateResponse(
        "legal/refund_request.html",
        {
            "request": request,
            "t": t,
            "lang": lang,
            "success": success == "1",
            "error": error,
            "merchant_oid": None,
            "email": None,
            "reason": None,
            "canonical_url": canonical_url,
            "hreflang_alternates": hreflang_alternates,
            **ui,
        },
    )


@app.post("/iade-talebi", response_class=HTMLResponse)
def refund_request_submit(
    request: Request,
    merchant_oid: str = Form(""),
    email: str = Form(""),
    reason: str = Form(""),
    lang: str = Form("tr"),
    db: Session = Depends(get_db),
):
    """İade talebini kaydeder: sipariş admin_note'a eklenir, admin panelden PayTR iade yapılabilir."""
    lang = (lang or "tr").strip().lower()[:2]
    if lang not in REFUND_LANGS:
        lang = "tr"
    t = get_pay_ui(lang)
    ui = get_legal_ui(lang)

    merchant_oid = (merchant_oid or "").strip()
    email = (email or "").strip()
    reason = (reason or "").strip()[:500]

    base_url = str(request.base_url).rstrip("/")
    canonical = f"{base_url}/iade-talebi"
    href_alts = _refund_page_hreflang_alternates(base_url)
    if not merchant_oid or not email:
        return templates.TemplateResponse(
            "legal/refund_request.html",
            {
                "request": request,
                "t": t,
                "lang": lang,
                "success": False,
                "error": t.get("refund_request_error_invalid", "Sipariş numarası ve e-posta zorunludur."),
                "merchant_oid": merchant_oid or None,
                "email": email or None,
                "reason": reason or None,
                "canonical_url": canonical,
                "hreflang_alternates": href_alts,
                **ui,
            },
        )

    order = db.exec(select(PaymentOrder).where(PaymentOrder.merchant_oid == merchant_oid)).first()
    if not order or order.status != "completed":
        return templates.TemplateResponse(
            "legal/refund_request.html",
            {
                "request": request,
                "t": t,
                "lang": lang,
                "success": False,
                "error": t.get("refund_request_error_order_not_found", "Tamamlanmış sipariş bulunamadı."),
                "merchant_oid": merchant_oid,
                "email": email,
                "reason": reason or None,
                "canonical_url": canonical,
                "hreflang_alternates": href_alts,
                **ui,
            },
        )

    note_line = f"\n[İade talebi {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC] e-posta: {email}"
    if reason:
        note_line += f" | gerekçe: {reason[:200]}"
    order.admin_note = (order.admin_note or "") + note_line
    db.add(order)
    db.commit()

    return RedirectResponse(
        url=f"/iade-talebi?lang={lang}&success=1",
        status_code=302,
    )


def _enterprise_lang_from_request(request: Request) -> str:
    """Kurumsal sayfa dili: ?lang= veya Accept-Language."""
    lang_q = request.query_params.get("lang", "").strip().lower()
    if lang_q and lang_q in ENTERPRISE_LANGS:
        return lang_q
    parsed = _parse_accept_language(request.headers.get("accept-language"))
    return parsed if parsed in ENTERPRISE_LANGS else "tr"


@app.get("/kurumsal", response_class=HTMLResponse)
def kurumsal_page(request: Request):
    """Kurumsal landing: hastane/klinik demo talebi. Çok dilli."""
    lang = _enterprise_lang_from_request(request)
    if lang not in ENTERPRISE_LANGS:
        lang = "tr"
    t = get_enterprise_ui(lang)
    base_url = str(request.base_url).rstrip("/")
    return templates.TemplateResponse(
        "enterprise/kurumsal.html",
        {"request": request, "lang": lang, "t": t, "canonical_url": f"{base_url}/kurumsal"},
    )


@app.get("/hastaneler-icin", response_class=HTMLResponse)
def hastaneler_icin_page(request: Request):
    """Hastaneye özel kurumsal landing page (Türkçe)."""
    base_url = str(request.base_url).rstrip("/")
    return templates.TemplateResponse(
        "enterprise/hastaneler.html",
        {"request": request, "canonical_url": f"{base_url}/hastaneler-icin"},
    )


def _lang_label(code: str) -> str:
    mapping = {
        "tr": "Türkçe",
        "en": "English",
        "de": "Deutsch",
        "it": "Italiano",
        "es": "Español",
        "fr": "Français",
        "he": "עברית",
        "ar": "العربية",
        "hi": "हिन्दी",
        "el": "Ελληνικά",
        "cs": "Čeština",
        "sr": "Српски",
    }
    return mapping.get(code, code)


@app.get("/blog", response_class=HTMLResponse)
def blog_root(request: Request):
    """/blog -> varsayılan İngilizce /en/blog; kullanıcıyı zorla yönlendirme."""
    return RedirectResponse(url="/en/blog", status_code=302)


@app.get("/{lang}/blog", response_class=HTMLResponse)
def blog_index(request: Request, lang: str):
    """Blog ana sayfa: premium liste, sadece en/de/fr/it."""
    lang = (lang or "").lower()[:2]
    if lang not in BLOG_LANGS_PREMIUM:
        raise HTTPException(status_code=404, detail="Blog not available in this language.")
    request.state.locale = lang
    posts_raw = list_articles_for_lang(lang)
    base_url = str(request.base_url).rstrip("/")
    posts = []
    for p in posts_raw:
        posts.append(
            {
                **p,
                "url": f"/{lang}/blog/{p['slug']}",
            }
        )
    categories = list({p["category"] for p in posts if p.get("category")})
    categories.sort()
    canonical_url = f"{base_url}/{lang}/blog"
    # Fallback: ensure we always have a full UI dict (avoid KeyError in templates)
    ui = dict(BLOG_UI.get(lang, BLOG_UI[DEFAULT_BLOG_LANG]))
    seo_title = ui.get("seo_title", f"{BRAND_NAME} Blog")
    meta_description = ui.get("meta_description", "")
    og_image = base_url + "/static/images/blog/how-to-read-blood-test-results.png"
    hreflang_alternates = [{"lang": code, "url": f"{base_url}/{code}/blog"} for code in BLOG_LANGS_PREMIUM]
    og_locale_map = {"tr": "tr_TR", "en": "en_US", "de": "de_DE", "fr": "fr_FR", "it": "it_IT", "es": "es_ES", "he": "he_IL", "hi": "hi_IN", "ar": "ar_SA"}
    og_locale = og_locale_map.get(lang, "en_US")
    item_list = [
        {"@type": "ListItem", "position": i + 1, "url": f"{base_url}{p['url']}", "name": p.get("title", "")}
        for i, p in enumerate(posts[:20])
    ]
    item_list_schema_json = json.dumps(
        {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": item_list},
        ensure_ascii=False,
        indent=2,
    )
    # SEO: BreadcrumbList for blog index (Ana Sayfa > Blog)
    base_ui = get_base_ui(lang)
    blog_index_breadcrumb = [
        {"@type": "ListItem", "position": 1, "name": base_ui.get("home_link", BRAND_NAME), "item": f"{base_url}/{lang}"},
        {"@type": "ListItem", "position": 2, "name": ui.get("breadcrumb_blog", ui.get("back_to_blog", "Blog")), "item": f"{base_url}/{lang}/blog"},
    ]
    breadcrumb_schema_json = json.dumps(
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": blog_index_breadcrumb},
        ensure_ascii=False,
        indent=2,
    )
    return templates.TemplateResponse(
        "blog/index.html",
        {
            "request": request,
            "posts": posts,
            "categories": categories,
            "lang": lang,
            "blog_ui": ui,
            "base_ui": base_ui,
            "brand_name": BRAND_NAME,
            "seo_title": seo_title,
            "meta_description": meta_description,
            "canonical_url": canonical_url,
            "og_image": og_image,
            "og_locale": og_locale,
            "hreflang_alternates": hreflang_alternates,
            "item_list_schema_json": item_list_schema_json,
            "breadcrumb_schema_json": breadcrumb_schema_json,
            "premium_langs": BLOG_LANGS_PREMIUM,
        },
    )


@app.get("/{lang}/blog/{slug}", response_class=HTMLResponse)
def blog_detail(request: Request, lang: str, slug: str):
    """Blog detay: makale içeriği, CTA; sadece en/de/fr/it."""
    lang = (lang or "").lower()[:2]
    if lang not in BLOG_LANGS_PREMIUM:
        raise HTTPException(status_code=404, detail="Blog not available in this language.")
    art = get_article(lang, slug)
    if not art:
        raise HTTPException(status_code=404, detail="Article not found.")
    request.state.locale = lang

    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/{lang}/blog/{slug}"
    cover_absolute = art["cover_image"] if art["cover_image"].startswith("http") else f"{base_url}{art['cover_image']}"

    toc = []
    for sec in art["sections"]:
        toc.append({"id": sec.id, "level": sec.level, "label": sec.heading})

    # Dil seçimleri sabit sırada (BLOG_LANGS_PREMIUM): TR, EN, ES, DE, FR, IT, HE, HI, AR
    lang_alternates: dict[str, dict] = {}
    for code in BLOG_LANGS_PREMIUM:
        s = art["available_langs"].get(code)
        if s is not None:
            lang_alternates[code] = {"url": f"{base_url}/{code}/blog/{s}", "label": _lang_label(code)}

    hreflang_alternates = [{"lang": code, "url": f"{base_url}/{code}/blog/{art['available_langs'][code]}"} for code in BLOG_LANGS_PREMIUM if code in art["available_langs"]]

    published_iso = art["published_at"].isoformat()
    modified_iso = art.get("last_updated") and art["last_updated"].isoformat() or published_iso
    logo_url = f"{base_url}/static/logo.png"
    blog_posting_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": art["seo_title"] or art["title"],
        "description": art["seo_description"] or art["subtitle"],
        "image": cover_absolute,
        "articleSection": art["category"],
        "inLanguage": lang,
        "datePublished": published_iso,
        "dateModified": modified_iso,
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical_url},
        "url": canonical_url,
        "author": {"@type": "Organization", "name": BRAND_NAME},
        "publisher": {
            "@type": "Organization",
            "name": BRAND_NAME,
            "logo": {"@type": "ImageObject", "url": logo_url},
        },
    }
    article_schema_json = json.dumps(blog_posting_schema, ensure_ascii=False, indent=2)
    blog_ui = dict(BLOG_UI.get(lang, BLOG_UI[DEFAULT_BLOG_LANG]))
    breadcrumb_items = [
        {"@type": "ListItem", "position": 1, "name": BRAND_NAME, "item": base_url},
        {"@type": "ListItem", "position": 2, "name": blog_ui.get("breadcrumb_blog", blog_ui.get("back_to_blog", "Blog")), "item": f"{base_url}/{lang}/blog"},
        {"@type": "ListItem", "position": 3, "name": art["seo_title"] or art["title"], "item": canonical_url},
    ]
    breadcrumb_schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": breadcrumb_items}
    breadcrumb_schema_json = json.dumps(breadcrumb_schema, ensure_ascii=False, indent=2)
    faq_schema_json = None
    faq_qa = art.get("faq_schema_qa")
    if faq_qa and isinstance(faq_qa, list):
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": item.get("question", ""), "acceptedAnswer": {"@type": "Answer", "text": item.get("answer", "")}}
                for item in faq_qa
            ],
        }
        faq_schema_json = json.dumps(faq_schema, ensure_ascii=False, indent=2)
    base_ui = get_base_ui(lang)
    related_posts = get_related_articles(lang, art["id"], base_url, limit=4)
    og_locale_map = {"tr": "tr_TR", "en": "en_US", "de": "de_DE", "fr": "fr_FR", "it": "it_IT", "es": "es_ES", "he": "he_IL", "hi": "hi_IN", "ar": "ar_SA"}
    og_locale = og_locale_map.get(lang, "en_US")

    return templates.TemplateResponse(
        "blog/detail.html",
        {
            "request": request,
            "article": art,
            "canonical_url": canonical_url,
            "cover_absolute": cover_absolute,
            "og_locale": og_locale,
            "toc": toc,
            "current_lang": lang,
            "lang_alternates": lang_alternates,
            "hreflang_alternates": hreflang_alternates,
            "article_schema_json": article_schema_json,
            "breadcrumb_schema_json": breadcrumb_schema_json,
            "faq_schema_json": faq_schema_json,
            "blog_ui": blog_ui,
            "base_ui": base_ui,
            "brand_name": BRAND_NAME,
            "premium_langs": BLOG_LANGS_PREMIUM,
            "related_posts": related_posts,
        },
    )


@app.post("/api/enterprise-lead")
@limiter.limit("3/minute")
async def api_enterprise_lead(request: Request, db: Session = Depends(get_db)):
    """Kurumsal demo talep formu. Aynı IP ile dakikada en fazla 3 istek."""
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Geçersiz JSON.")
    if not isinstance(body, dict):
        raise HTTPException(status_code=400, detail="Geçersiz istek.")
    kurum_adi = (body.get("kurum_adi") or "").strip()
    yetkili_ad = (body.get("yetkili_ad") or "").strip()
    email = (body.get("email") or "").strip()
    kvkk = body.get("kvkk") is True
    if not kurum_adi or not yetkili_ad or not email:
        raise HTTPException(status_code=400, detail="Kurum adı, yetkili adı ve e-posta zorunludur.")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise HTTPException(status_code=400, detail="Geçerli bir e-posta adresi girin.")
    if not kvkk:
        raise HTTPException(status_code=400, detail="KVKK onayı gerekli.")
    telefon = (body.get("telefon") or "").strip() or None
    kurum_tipi = (body.get("kurum_tipi") or "").strip() or None
    aylik_rapor = (body.get("aylik_rapor") or "").strip() or None
    mesaj = (body.get("mesaj") or "").strip() or None
    ip = _client_ip(request)
    user_agent = (request.headers.get("user-agent") or "")[:500] or None
    try:
        db.add(
            EnterpriseLead(
                kurum_adi=kurum_adi,
                yetkili_ad=yetkili_ad,
                email=email,
                telefon=telefon,
                kurum_tipi=kurum_tipi,
                aylik_rapor=aylik_rapor,
                mesaj=mesaj,
                kvkk_accepted=True,
                ip=ip,
                user_agent=user_agent,
            )
        )
        db.commit()
    except Exception as e:
        log.warning("EnterpriseLead save failed: %s", e)
        raise HTTPException(status_code=500, detail="Kayıt alınamadı. Lütfen tekrar deneyin.")
    try:
        from app.services.email_sender import send_enterprise_lead_notification
        send_enterprise_lead_notification(
            kurum_adi=kurum_adi,
            yetkili_ad=yetkili_ad,
            email=email,
            telefon=telefon,
            kurum_tipi=kurum_tipi,
            aylik_rapor=aylik_rapor,
            mesaj=mesaj,
        )
    except Exception as e:
        log.warning("Enterprise lead notification email failed: %s", e)
    return JSONResponse(content={"ok": True})


VALID_LEAD_SOURCES = frozenset({"homepage", "blog", "sample-report", "pricing"})


@app.post("/api/lead/subscribe")
@limiter.limit("5/minute")
async def api_lead_subscribe(request: Request, db: Session = Depends(get_db)):
    """E-posta toplama: blog, homepage, sample report vb. kaynaklardan gelen lead'ler."""
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request.")
    if not isinstance(body, dict):
        raise HTTPException(status_code=400, detail="Invalid request.")

    email = (body.get("email") or "").strip().lower()
    if not email or "@" not in email or "." not in email.split("@")[-1]:
        return JSONResponse(status_code=422, content={"ok": False, "error": "invalid_email"})
    if len(email) > 255:
        return JSONResponse(status_code=422, content={"ok": False, "error": "invalid_email"})

    name = (body.get("name") or "").strip()[:255] or None
    source = (body.get("source") or "").strip().lower()
    if source not in VALID_LEAD_SOURCES:
        source = "homepage"
    locale = (body.get("locale") or "").strip().lower()[:16] or None

    from sqlmodel import select
    existing = db.exec(select(EmailLead).where(EmailLead.email == email)).first()
    if existing:
        return JSONResponse(content={"ok": True, "already": True})

    ip = _client_ip(request)
    user_agent = (request.headers.get("user-agent") or "")[:500] or None
    try:
        db.add(EmailLead(
            email=email,
            name=name,
            source=source,
            locale=locale,
            ip=ip,
            user_agent=user_agent,
        ))
        db.commit()
    except Exception as e:
        log.warning("EmailLead save failed: %s", e)
        return JSONResponse(status_code=500, content={"ok": False, "error": "server_error"})

    # Welcome email (background thread — non-blocking)
    base_url = str(request.base_url).rstrip("/")
    _lang = (locale or "en").split("-")[0].split("_")[0].strip().lower() or "en"

    def _send():
        try:
            from app.services.email_sender import send_welcome_email
            send_welcome_email(email, lang=_lang, base_url=base_url)
        except Exception as exc:
            log.warning("Welcome email failed for %s: %s", email, exc)

    threading.Thread(target=_send, daemon=True).start()

    return JSONResponse(content={"ok": True, "already": False})


def _inject_canonical(raw: str, canonical_url: str) -> str:
    """HTML içinde </head> öncesine canonical link ekler (SEO)."""
    tag = f'<link rel="canonical" href="{canonical_url}" />'
    if "</head>" in raw and tag not in raw:
        raw = raw.replace("</head>", tag + "\n  </head>", 1)
    return raw


def _landing_response(locale: str, request: Request):
    """Country-based landing: aynı index.html, locale'e göre title/meta/hreflang ve __LANDING_T__ enjekte edilir."""
    import re
    from html import escape

    index_file = STATIC_DIR / "index.html"
    if not index_file.is_file():
        index_file = Path.cwd() / "static" / "index.html"
    if not index_file.is_file():
        return JSONResponse(
            content={"durum": "hazır", "servis": "norya-api", "mesaj": "static/index.html bulunamadı."},
            status_code=404,
        )

    raw = index_file.read_text(encoding="utf-8")
    raw = _inject_ga(raw)
    raw = _inject_whatsapp(raw, locale)
    raw = _inject_company(raw)
    raw = _inject_google_site_verification(raw)

    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/{locale}"
    raw = _inject_canonical(raw, canonical_url)

    meta = get_landing_meta(locale)
    ui = get_landing_ui(locale)
    title = escape(meta.get("meta_title", BRAND_NAME))
    desc = escape(meta.get("meta_description", ""))
    og_locale = meta.get("og_locale", "en_US")

    raw = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", raw, count=1)
    raw = re.sub(
        r'<meta name="description" content="[^"]*" */?>',
        f'<meta name="description" content="{desc}" />',
        raw,
        count=1,
    )
    raw = re.sub(
        r'<meta property="og:title" content="[^"]*" */?>',
        f'<meta property="og:title" content="{title}" />',
        raw,
        count=1,
    )
    raw = re.sub(
        r'<meta property="og:description" content="[^"]*" */?>',
        f'<meta property="og:description" content="{desc}" />',
        raw,
        count=1,
    )
    raw = re.sub(
        r'<meta property="og:locale" content="[^"]*" */?>',
        f'<meta property="og:locale" content="{og_locale}" />',
        raw,
        count=1,
    )
    raw = re.sub(
        r'<meta name="twitter:title" content="[^"]*" */?>',
        f'<meta name="twitter:title" content="{title}" />',
        raw,
        count=1,
    )
    raw = re.sub(
        r'<meta name="twitter:description" content="[^"]*" */?>',
        f'<meta name="twitter:description" content="{desc}" />',
        raw,
        count=1,
    )
    raw = re.sub(
        r'<meta property="og:url" content="[^"]*" */?>',
        f'<meta property="og:url" content="{canonical_url}" />',
        raw,
        count=1,
    )
    raw = re.sub(
        r'<link rel="canonical" href="[^"]*" */?>',
        f'<link rel="canonical" href="{canonical_url}" />',
        raw,
        count=1,
    )

    def _hreflang_code(loc: str) -> str:
        # Google hreflang casing: en-CA (path: /en-ca)
        return "en-CA" if loc == "en-ca" else loc

    hreflang_lines = [
        f'  <link rel="alternate" hreflang="{_hreflang_code(loc)}" href="{base_url}/{loc}" />'
        for loc in LANDING_ROUTES
    ]
    hreflang_lines.append(f'  <link rel="alternate" hreflang="x-default" href="{base_url}/en" />')
    hreflang_block = "\n".join(hreflang_lines)
    raw = re.sub(
        r'  <link rel="alternate" hreflang="[^"]*" href="[^"]*" */?>\s*(?:  <link rel="alternate" hreflang="[^"]*" href="[^"]*" */?>\s*)*',
        hreflang_block + "\n  ",
        raw,
        count=1,
    )

    lang_attr = "en" if locale == "en-ca" else locale
    dir_attr = ' dir="rtl"' if locale in ("he", "ar") else ""
    raw = re.sub(
        r'<html lang="[^"]*" id="html-lang"',
        f'<html lang="{lang_attr}" id="html-lang"{dir_attr}',
        raw,
        count=1,
    )

    landing_script = (
        f'<script>window.__LANDING_LOCALE__="{escape(locale)}";'
        f"window.__LANDING_T__={json.dumps(ui, ensure_ascii=False)};</script>\n  "
    )
    faq_entities = []
    for i in range(1, 7):
        q = ui.get(f"faq_q{i}")
        a = ui.get(f"faq_a{i}")
        if q and a:
            faq_entities.append(
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            )
    if faq_entities:
        faq_schema = json.dumps(
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_entities},
            ensure_ascii=False,
        )
        landing_script += f'\n  <script type="application/ld+json">\n  {faq_schema}\n  </script>\n  '
    raw = raw.replace("</head>", landing_script + "</head>", 1)

    return HTMLResponse(
        raw,
        headers={"Cache-Control": "public, max-age=0, s-maxage=600, must-revalidate"},
    )


def _index_response(request: Request | None = None):
    """Ana sayfa içeriği: static/index.html veya fallback JSON. GET ve POST / için ortak. request verilirse canonical enjekte edilir."""
    index_file = STATIC_DIR / "index.html"
    if not index_file.is_file():
        index_file = Path.cwd() / "static" / "index.html"
    if index_file.is_file():
        _locale: str | None = None
        if request is not None:
            path = (request.url.path or "").strip()
            path_locale = None
            if path.startswith("/") and path != "/":
                segment = path[1:].split("/")[0].lower()
                if segment in LANDING_ROUTES or segment in ("fr", "es", "ar", "hi", "he", "el", "sr"):
                    path_locale = segment
            if path == "/":
                _locale = "en"
            elif path_locale:
                _locale = path_locale

        raw = index_file.read_text(encoding="utf-8")
        raw = _inject_ga(raw)  # Google Ads AW-18004536281 + isteğe bağlı GA4, tek yükleme
        raw = _inject_whatsapp(raw, _locale or "en")
        raw = _inject_company(raw)
        raw = _inject_google_site_verification(raw)
        if request is not None:
            import re
            from html import escape
            base_url = str(request.base_url).rstrip("/")
            canonical_url = base_url + request.url.path
            raw = re.sub(
                r'<link rel="canonical" href="[^"]*" */?>',
                f'<link rel="canonical" href="{canonical_url}" />',
                raw,
                count=1,
            )
            if '<link rel="canonical"' not in raw:
                raw = _inject_canonical(raw, canonical_url)
            raw = re.sub(
                r'<meta property="og:url" content="[^"]*" */?>',
                f'<meta property="og:url" content="{canonical_url}" />',
                raw,
                count=1,
            )
            if _locale is not None:
                meta = get_landing_meta(_locale) if _locale in LANDING_ROUTES else {"meta_title": BRAND_NAME, "meta_description": "", "og_locale": "en_US"}
                ui = get_landing_ui(_locale) if _locale in LANDING_ROUTES else {}
                _title = escape(meta.get("meta_title", BRAND_NAME))
                _desc = escape(meta.get("meta_description", ""))
                raw = re.sub(r"<title>[^<]*</title>", f"<title>{_title}</title>", raw, count=1)
                raw = re.sub(r'<meta name="description" content="[^"]*" */?>', f'<meta name="description" content="{_desc}" />', raw, count=1)
                raw = re.sub(r'<meta property="og:title" content="[^"]*" */?>', f'<meta property="og:title" content="{_title}" />', raw, count=1)
                raw = re.sub(r'<meta property="og:description" content="[^"]*" */?>', f'<meta property="og:description" content="{_desc}" />', raw, count=1)
                raw = re.sub(r'<meta name="twitter:title" content="[^"]*" */?>', f'<meta name="twitter:title" content="{_title}" />', raw, count=1)
                raw = re.sub(r'<meta name="twitter:description" content="[^"]*" */?>', f'<meta name="twitter:description" content="{_desc}" />', raw, count=1)
                _og_loc = meta.get("og_locale", "en_US")
                raw = re.sub(
                    r'<meta property="og:locale" content="[^"]*" */?>',
                    f'<meta property="og:locale" content="{_og_loc}" />',
                    raw,
                    count=1,
                )
                _html_lang = "en" if _locale == "en-ca" else _locale
                _html_dir = ' dir="rtl"' if _locale in ("he", "ar") else ""
                raw = re.sub(
                    r'<html lang="[^"]*" id="html-lang"',
                    f'<html lang="{_html_lang}" id="html-lang"{_html_dir}',
                    raw,
                    count=1,
                )

                def _hreflang_code(loc: str) -> str:
                    # Google hreflang casing: en-CA (path: /en-ca)
                    return "en-CA" if loc == "en-ca" else loc

                # SPA'nin statik index.html'i sadece kısmi hreflang içeriyor.
                # Burada tüm `LANDING_ROUTES` için hreflang bloğunu güncelliyoruz.
                hreflang_lines = [
                    f'  <link rel="alternate" hreflang="{_hreflang_code(loc)}" href="{base_url}/{loc}" />'
                    for loc in LANDING_ROUTES
                ]
                hreflang_lines.append(f'  <link rel="alternate" hreflang="x-default" href="{base_url}/en" />')
                hreflang_block = "\n".join(hreflang_lines)
                raw = re.sub(
                    r'  <link rel="alternate" hreflang="[^"]*" href="[^"]*" */?>\s*(?:  <link rel="alternate" hreflang="[^"]*" href="[^"]*" */?>\s*)*',
                    hreflang_block + "\n  ",
                    raw,
                    count=1,
                )

                landing_script = (
                    f'<script>window.__LANDING_LOCALE__="{escape(_locale)}";'
                    f"window.__LANDING_T__={json.dumps(ui, ensure_ascii=False)};</script>\n  "
                )
                raw = raw.replace("</head>", landing_script + "</head>", 1)
        return HTMLResponse(
            raw,
            headers={
                "Cache-Control": "public, max-age=0, s-maxage=600, must-revalidate",
            },
        )
    return {"durum": "hazır", "servis": "norya-api", "mesaj": "static/index.html bulunamadı. Proje kökünden çalıştırın: uvicorn app.main:app --reload"}


@app.get("/report")
def report_page(request: Request):
    """Rapor sayfası: /report?rid=... — aynı SPA, rid query ile rapor yüklenir."""
    index_file = STATIC_DIR / "index.html"
    if not index_file.is_file():
        index_file = Path.cwd() / "static" / "index.html"
    if index_file.is_file():
        _lang = (request.cookies.get("norya_lang") or "").strip().lower()[:2]
        if _lang not in WHATSAPP_GREETINGS:
            _lang = _parse_accept_language(request.headers.get("accept-language"))
        raw = index_file.read_text(encoding="utf-8")
        raw = _inject_ga(raw)  # Google Ads global site tag
        raw = _inject_whatsapp(raw, _lang)
        raw = _inject_company(raw)
        raw = _inject_google_site_verification(raw)
        base_url = str(request.base_url).rstrip("/")
        raw = _inject_canonical(raw, f"{base_url}/report")
        return HTMLResponse(
            raw,
            headers={"Cache-Control": "public, max-age=0, must-revalidate"},
        )
    return {"durum": "hazır", "servis": "norya-api", "mesaj": "static/index.html bulunamadı."}


@app.get("/analyze", response_class=HTMLResponse)
def analyze_landing(request: Request):
    """
    /analyze -> SPA içindeki analiz bölümüne yönlendir.
    Blog CTA'ları bu URL'yi kullanır.
    Öncelik: ?lang= ile gelen dil, yoksa referer'dan locale çıkarılırsa /{locale}#analyze.
    """
    lang_q = (request.query_params.get("lang") or "").strip().lower()[:2]
    locale = lang_q if lang_q in SUPPORTED_LOCALES else None
    if locale is None:
        referer = request.headers.get("referer") or ""
        for loc in SUPPORTED_LOCALES:
            if f"/{loc}/" in referer or referer.rstrip("/").endswith(f"/{loc}"):
                locale = loc
                break
    url = f"/{locale}#analyze" if locale else "/#analyze"
    return RedirectResponse(url=url, status_code=302)


def _how_it_works_lang_from_request(request: Request) -> str:
    """How-it-works dili: ?lang=, cookie norya_lang, sonra Accept-Language."""
    lang_q = request.query_params.get("lang", "").strip().lower()[:2]
    if lang_q and lang_q in HOW_IT_WORKS_LANGS:
        return lang_q
    lang_cookie = (request.cookies.get("norya_lang") or "").strip().lower()[:2]
    if lang_cookie and lang_cookie in HOW_IT_WORKS_LANGS:
        return lang_cookie
    parsed = _parse_accept_language(request.headers.get("accept-language"))
    return parsed if parsed in HOW_IT_WORKS_LANGS else DEFAULT_HOW_IT_WORKS_LANG


def _breadcrumb_json(base_url: str, items: list[tuple[str, str]]) -> str:
    """BreadcrumbList JSON-LD üret. items: [(name, url), ...]"""
    bc_items = []
    for i, (name, url) in enumerate(items, 1):
        bc_items.append({"@type": "ListItem", "position": i, "name": name, "item": url})
    return json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": bc_items}, ensure_ascii=False)


@app.get("/about", response_class=HTMLResponse)
def about_page(request: Request):
    """Hakkımızda / About sayfası – Stitch v21 tasarımı."""
    base_url = str(request.base_url).rstrip("/")
    breadcrumb_json = _breadcrumb_json(base_url, [("Home", base_url), ("About", f"{base_url}/about")])
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "canonical_url": f"{base_url}/about",
            "base_url": base_url,
            "og_image": f"{base_url}/static/images/og-default.png",
            "breadcrumb_json": breadcrumb_json,
        },
    )


@app.get("/science", response_class=HTMLResponse)
def science_page(request: Request):
    """Bilim & Teknoloji sayfası – Stitch v20 tasarımı."""
    base_url = str(request.base_url).rstrip("/")
    breadcrumb_json = _breadcrumb_json(base_url, [("Home", base_url), ("Science", f"{base_url}/science")])
    return templates.TemplateResponse(
        "science.html",
        {
            "request": request,
            "canonical_url": f"{base_url}/science",
            "base_url": base_url,
            "og_image": f"{base_url}/static/images/og-default.png",
            "breadcrumb_json": breadcrumb_json,
        },
    )


@app.get("/security", response_class=HTMLResponse)
def security_page(request: Request):
    """Güvenlik & Gizlilik sayfası – Stitch v25 tasarımı."""
    base_url = str(request.base_url).rstrip("/")
    breadcrumb_json = _breadcrumb_json(base_url, [("Home", base_url), ("Security", f"{base_url}/security")])
    return templates.TemplateResponse(
        "security.html",
        {
            "request": request,
            "canonical_url": f"{base_url}/security",
            "base_url": base_url,
            "og_image": f"{base_url}/static/images/og-default.png",
            "breadcrumb_json": breadcrumb_json,
        },
    )


@app.get("/technology", response_class=HTMLResponse)
def technology_page(request: Request):
    """Teknoloji sayfası – Stitch v22 tasarımı."""
    base_url = str(request.base_url).rstrip("/")
    breadcrumb_json = _breadcrumb_json(base_url, [("Home", base_url), ("Technology", f"{base_url}/technology")])
    return templates.TemplateResponse(
        "technology.html",
        {
            "request": request,
            "canonical_url": f"{base_url}/technology",
            "base_url": base_url,
            "og_image": f"{base_url}/static/images/og-default.png",
            "breadcrumb_json": breadcrumb_json,
        },
    )


@app.get("/how-it-works", response_class=HTMLResponse)
def how_it_works_page(request: Request):
    """
    /how-it-works -> Nasıl çalışır sayfası. Google Ads site bağlantısı için.
    Dil: ?lang=, norya_lang çerezi veya Accept-Language (tr, en, de, fr, it, es, he, hi, ar). SEO: canonical, hreflang.
    """
    lang = _how_it_works_lang_from_request(request)
    t = get_how_it_works_ui(lang)
    meta = get_how_it_works_meta(lang)
    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/how-it-works"
    hreflang_alternates = [
        {"lang": code, "url": f"{base_url}/how-it-works?lang={code}"}
        for code in HOW_IT_WORKS_LANGS
    ]
    hreflang_alternates.append({"lang": "x-default", "url": f"{base_url}/how-it-works?lang=en"})
    breadcrumb_json = _breadcrumb_json(base_url, [("Home", base_url), ("How it works", canonical_url)])
    return templates.TemplateResponse(
        "how_it_works.html",
        {
            "request": request,
            "lang": lang,
            "t": t,
            "meta": meta,
            "canonical_url": canonical_url,
            "hreflang_alternates": hreflang_alternates,
            "hiw_lang_codes": HOW_IT_WORKS_LANGS,
            "base_url": base_url,
            "breadcrumb_json": breadcrumb_json,
        },
    )


@app.get("/pricing", response_class=HTMLResponse)
def pricing_landing(
    request: Request,
    db: Session = Depends(get_db),
):
    """
    /pricing -> Karşılaştırmalı fiyatlandırma sayfası.
    Kullanıcı önce planları ve özelliklerini görür; ödeme için /payment'e yönlenir.
    """
    lang = _payment_lang_from_request(request)
    t = enrich_pricing_context(lang, get_pay_ui(lang))
    base_url = _paytr_canonical_base(request)
    hreflang_alternates = [{"lang": code, "url": f"{base_url}/{code}/pricing"} for code in PRICING_HREFLANG_LANGS]
    hreflang_alternates.append({"lang": "x-default", "url": f"{base_url}/en/pricing"})
    plan_map = get_plan_code_to_product_cents(db)

    def _plan(product_key: str) -> dict:
        for code, (product, cents) in plan_map.items():
            if product == product_key:
                return {"code": code, "product": product, "price_cents": cents}
        return {"code": "", "product": product_key, "price_cents": 0}

    plans = {
        "single": _plan("single"),
        "monthly": _plan("monthly"),
        "yearly": _plan("yearly"),
    }

    return templates.TemplateResponse(
        "pricing.html",
        {
            "request": request,
            "brand": BRAND_NAME,
            "lang": lang,
            "t": t,
            "base_url": base_url,
            "plans": plans,
            "hreflang_alternates": hreflang_alternates,
        },
    )


@app.get("/odeme", response_class=HTMLResponse)
def odeme_landing(request: Request):
    """
    /odeme -> SPA ödeme (checkout) sayfasına doğrudan yönlendir.
    Eksiklikleri görmek için ödeme sayfasını doğrudan açmak için kullanılır.
    """
    query = request.url.query
    target = "/?" + query + "#odeme" if query else "/#odeme"
    return RedirectResponse(url=target, status_code=302)


# Ücretsiz planda: ilk analiz ücretsiz, sonrası için ödeme gerekir (ayda 1 hak)
AYLIK_LIMIT_UCRETSIZ = 1
# Pro planı (50€ aylık / 99€ yıllık): ayda 10+3 = 13 analiz
AYLIK_LIMIT_PRO = 13


def _ayin_ilk_gunu() -> datetime:
    """Bu ayın ilk günü 00:00:00 UTC (naive; veritabanıyla uyumlu)."""
    now = datetime.now(timezone.utc)
    return now.replace(day=1, hour=0, minute=0, second=0, microsecond=0).replace(tzinfo=None)


def _aylik_analiz_sayisi(db: Session, user_id: int) -> int:
    """Kullanıcının bu ay yaptığı analiz sayısı."""
    baslangic = _ayin_ilk_gunu()
    stmt = (
        select(AnalysisRecord)
        .where(AnalysisRecord.user_id == user_id, AnalysisRecord.created_at >= baslangic)
    )
    return len(list(db.exec(stmt).all()))


def _total_analiz_sayisi(db: Session, user_id: int) -> int:
    """Kullanıcının toplam (tüm zamanlar) analiz sayısı. 0 ise ilk analiz ücretsiz."""
    stmt = select(AnalysisRecord).where(AnalysisRecord.user_id == user_id)
    return len(list(db.exec(stmt).all()))


def _aylik_limit(plan: str) -> int:
    """Plana göre aylık analiz limiti."""
    return AYLIK_LIMIT_PRO if (plan or "").strip().lower() == "pro" else AYLIK_LIMIT_UCRETSIZ


def _extra_credits(user: User) -> int:
    return getattr(user, "extra_credits", 0) or 0


def _can_analyze(limit: int, kullanilan: int, user: User) -> bool:
    """Aylık haktan veya ödenen ek haktan analiz yapabilir mi?"""
    if kullanilan < limit:
        return True
    return _extra_credits(user) > 0


def _ilk_analiz_ucretsiz(db: Session, user_id: int) -> bool:
    """Hesapta hiç analiz yoksa ilk analiz ücretsiz."""
    return _total_analiz_sayisi(db, user_id) == 0


def _use_analysis_credit(db: Session, user: User, limit: int, kullanilan: int) -> None:
    """Aylık limit doluysa bir ek hakkı düşür (önce öde sonra kullan)."""
    if kullanilan < limit:
        return
    u = db.get(User, user.id)
    if u and (getattr(u, "extra_credits", 0) or 0) > 0:
        u.extra_credits = (u.extra_credits or 0) - 1
        db.add(u)
        db.commit()


def _get_active_institution(db: Session, user_id: int):
    """Kullanıcının aktif kurumsal üyeliğini ve kurumunu döndür. Yoksa (None, None)."""
    from app.models.institution import Institution, InstitutionMembership
    membership = db.exec(
        select(InstitutionMembership).where(
            InstitutionMembership.user_id == user_id,
            InstitutionMembership.is_active == True,
        )
    ).first()
    if not membership:
        return None, None
    inst = db.get(Institution, membership.institution_id)
    if not inst or not inst.is_active:
        return None, None
    return inst, membership


def _institution_can_analyze(inst) -> bool:
    """Kurum kotası yeterli mi?"""
    if not inst:
        return False
    return inst.quota_used_this_month < inst.monthly_quota


def _use_institution_credit(db: Session, inst) -> None:
    """Kurum kotasından bir hak düşür."""
    if not inst:
        return
    inst.quota_used_this_month = (inst.quota_used_this_month or 0) + 1
    db.add(inst)
    db.commit()


def _client_ip(request: Request) -> str:
    """Müşteri IP'si; PayTR için proxy başlıkları öncelikli (Cloudflare, Render)."""
    cf = request.headers.get("cf-connecting-ip")
    if cf and cf.strip():
        return cf.strip()
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    xri = request.headers.get("x-real-ip")
    if xri and xri.strip():
        return xri.strip()
    return request.client.host if request.client else ""


# 30/hour per user for /analyze and /analyze/upload (in-memory; key = user_id)
_analyze_hourly: dict[str, list[float]] = {}
_analyze_hourly_lock = threading.Lock()
ANALYZE_HOURLY_LIMIT = 30
HOUR_SECONDS = 3600.0


def _check_analyze_hourly_limit(user_id: int) -> None:
    """Raises HTTPException 429 if this user has >= ANALYZE_HOURLY_LIMIT analyses in the last hour."""
    key = f"u_{user_id}"
    now = time.time()
    with _analyze_hourly_lock:
        if key not in _analyze_hourly:
            _analyze_hourly[key] = []
        times = _analyze_hourly[key]
        times[:] = [t for t in times if now - t < HOUR_SECONDS]
        if len(times) >= ANALYZE_HOURLY_LIMIT:
            raise HTTPException(
                status_code=429,
                detail="Too many analyses in the last hour. Please try again later.",
            )
        times.append(now)


def _audit(db: Session, event: str, user_id: int | None, ip: str | None, institution_id: int | None = None) -> None:
    try:
        country, city = get_geo_from_ip(ip) if ip else (None, None)
        db.add(AuditLog(event=event, user_id=user_id, ip=ip, country=country, city=city, institution_id=institution_id))
        db.commit()
    except Exception:
        pass


def _save_analysis(
    db: Session,
    user_id: int,
    input_text: str,
    result_text: str,
    source: str,
    doctor_notes: str | None = None,
    plan_type: str | None = None,
    institution_id: int | None = None,
) -> int:
    from app.core.plan_config import normalize_plan_type

    pt = normalize_plan_type(plan_type) if plan_type is not None else "single"
    rec = AnalysisRecord(
        user_id=user_id,
        input_text=input_text,
        result_text=result_text,
        source=source,
        doctor_notes=doctor_notes,
        plan_type=pt,
        institution_id=institution_id,
    )
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec.id or 0


def _get_trend_for_user(
    db: Session,
    user_id: int,
    exclude_analysis_id: int | None = None,
) -> dict | None:
    """Son 3 analizi (exclude_analysis_id hariç) çekip LDL/Glucose/CRP trend verisi döndürür."""
    stmt = (
        select(AnalysisRecord)
        .where(AnalysisRecord.user_id == user_id)
        .order_by(AnalysisRecord.id.desc())
        .limit(4)
    )
    rows = list(db.exec(stmt).all())
    entries: list[tuple[str, str]] = []
    for r in rows:
        if r.id == exclude_analysis_id:
            continue
        if len(entries) >= 3:
            break
        date_str = r.created_at.strftime("%d.%m.%Y") if getattr(r, "created_at", None) else ""
        entries.append((date_str, r.result_text or ""))
    return extract_trend_from_results(entries) if entries else None


def _attach_original_file(
    db: Session,
    analysis_id: int,
    content: bytes,
    filename: str,
    source: str,
) -> None:
    """Yüklenen orijinal dosyayı diske yazar ve kaydı günceller (admin: hastanın gönderdiği belge)."""
    if source not in ("pdf", "image"):
        return
    ext = "." + filename.lower().rsplit(".", 1)[-1] if "." in filename else (".jpg" if source == "image" else ".pdf")
    if ext not in ALLOWED_UPLOAD_EXTENSIONS:
        ext = ".pdf" if source == "pdf" else ".jpg"
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    stored_name = f"{analysis_id}{ext}"
    path = UPLOADS_DIR / stored_name
    try:
        path.write_bytes(content)
    except OSError as e:
        log.warning("Original file save failed for analysis %s: %s", analysis_id, e)
        return
    rec = db.get(AnalysisRecord, analysis_id)
    if rec:
        rec.original_filename = filename
        rec.original_stored_path = stored_name
        db.add(rec)
        db.commit()


def _is_test_mode(request: Request) -> bool:
    """Sınırsız test modu: canlıda kapalı; development'ta X-Test-Mode: 1 veya ?test=1 ile açılır."""
    if (getattr(settings, "environment", "") or "").strip().lower() == "production":
        return False
    return (
        request.headers.get("X-Test-Mode") == "1"
        or request.query_params.get("test") == "1"
    )


def _dev_override_plan(request: Request, user: User) -> str:
    """
    Development/test modunda plan önizleme:
    ?dev_plan=free|single|monthly|yearly ile analiz planını zorla.
    Production'da veya test_mode kapalıyken dev override çalışmaz.
    """
    env = (getattr(settings, "environment", "") or "").strip().lower()
    if env == "production":
        return (getattr(user, "plan", "free") or "free")
    if not _is_test_mode(request):
        return (getattr(user, "plan", "free") or "free")
    raw = (request.query_params.get("dev_plan") or "").strip().lower()
    if raw in {"free", "single", "monthly", "yearly"}:
        return raw
    return (getattr(user, "plan", "free") or "free")


@app.post("/analyze", response_model=AnalyzeResponse)
@limiter.limit("10/minute")
async def analyze(
    request: Request,
    user: User = Depends(get_current_user_or_dev_guest),
    db: Session = Depends(get_db),
):
    """Metin analizi. JSON body veya form (text, doctor_notes, lang) — PDF/görsel akışı ile aynı form gönderimi desteklenir."""
    test_mode = _is_test_mode(request)
    if not test_mode:
        _check_analyze_hourly_limit(user.id or 0)
    content_type = (request.headers.get("content-type") or "").lower()
    if "application/json" in content_type:
        try:
            body = await request.json()
        except Exception:
            raise HTTPException(status_code=400, detail="Geçersiz JSON.")
        text = (body.get("text") or "").strip()
        doctor_notes = body.get("doctor_notes")
        if doctor_notes is not None:
            doctor_notes = (doctor_notes or "").strip() or None
        lang = body.get("lang")
    else:
        form = await request.form()
        text = (form.get("text") or "").strip()
        doctor_notes = (form.get("doctor_notes") or "").strip() or None
        lang = form.get("lang") or None
    if not text:
        raise HTTPException(status_code=400, detail="Lütfen tahlil metnini girin veya PDF/görsel yükleyin.")
    plan = _dev_override_plan(request, user)
    _active_inst, _active_membership = (None, None)
    if not test_mode:
        _active_inst, _active_membership = _get_active_institution(db, user.id or 0)
        if _active_inst and _institution_can_analyze(_active_inst):
            _use_institution_credit(db, _active_inst)
        else:
            if _active_inst and not _institution_can_analyze(_active_inst):
                _active_inst = None
            limit = _aylik_limit(plan)
            kullanilan = _aylik_analiz_sayisi(db, user.id or 0)
            ilk_ucretsiz = _ilk_analiz_ucretsiz(db, user.id or 0)
            if not ilk_ucretsiz and not _can_analyze(limit, kullanilan, user):
                raise HTTPException(
                    status_code=402,
                    detail=f"Aylık analiz hakkınız doldu ({kullanilan}/{limit}). Önce 1 analiz satın alın veya Pro plana geçin.",
                )
            if not ilk_ucretsiz:
                _use_analysis_credit(db, user, limit, kullanilan)
    _inst_id_for_save = _active_inst.id if _active_inst else None
    log.info("/analyze payload: text_len=%s, has_doctor_notes=%s, lang=%s", len(text), bool(doctor_notes), lang)
    job = None
    if not test_mode:
        job = AnalysisJob(user_id=user.id or 0, status="processing")
        db.add(job)
        db.commit()
        db.refresh(job)
    t0 = time.perf_counter()
    try:
        report_lang = _report_lang_from_request(request, lang)
        # Cache key: normalize metin + dil + plan + model + doctor_notes + prompt_version (PII yok)
        labs_norm = {
            "t": " ".join(text.split()).strip(),
            "dn": (doctor_notes or "").strip() or None,
        }
        cache_key = make_cache_key(
            labs_norm=labs_norm,
            lang=report_lang,
            plan=plan,
            model=OPENAI_ANALYZE_MODEL,
            prompt_version=AI_CACHE_PROMPT_VERSION,
        )
        cached = cache_get(_cache_conn, cache_key)
        if cached is not None:
            log.info("CACHE HIT key=%s", cache_key[:16])
            result = cached["sonuc"]
            aid = _save_analysis(db, user.id or 0, text, result, "text", doctor_notes=doctor_notes, plan_type=plan, institution_id=_inst_id_for_save)
            if job:
                job.status = "done"
                job.analysis_record_id = aid
                job.duration_ms = int((time.perf_counter() - t0) * 1000)
                db.add(job)
                db.commit()
            _audit(db, "analyze", user.id, _client_ip(request), institution_id=_inst_id_for_save)
            return _build_analyze_response(
                result, aid, cached.get("risk_summary"), plan, user.id or 0, db, cached=True
            )
        log.info("CACHE MISS key=%s", cache_key[:16])
        report_payload, usage = analyze_blood_test(
            text,
            detailed=True,
            doctor_notes=doctor_notes,
            lang=report_lang,
            plan=plan,
            labs_norm=labs_norm,
        )
        result = report_payload["sonuc"]
        cache_set(
            _cache_conn,
            cache_key=cache_key,
            created_at=now_iso(),
            expires_at=expires_iso(AI_CACHE_TTL_DAYS),
            model=OPENAI_ANALYZE_MODEL,
            input_summary={"lang": report_lang, "plan": plan, "labs_count": len(labs_norm.get("t", ""))},
            response_obj={
                "sonuc": result,
                "usage": usage or {},
                "risk_summary": report_payload["risk_summary"],
                "explanation": report_payload["explanation"],
                "tables": report_payload["tables"],
                "meta": report_payload["meta"],
            },
        )
        aid = _save_analysis(db, user.id or 0, text, result, "text", doctor_notes=doctor_notes, plan_type=plan, institution_id=_inst_id_for_save)
        if job:
            job.status = "done"
            job.analysis_record_id = aid
            job.duration_ms = int((time.perf_counter() - t0) * 1000)
            if usage:
                job.prompt_tokens = usage.get("prompt_tokens")
                job.completion_tokens = usage.get("completion_tokens")
            db.add(job)
            db.commit()
        _audit(db, "analyze", user.id, _client_ip(request), institution_id=_inst_id_for_save)
        return _build_analyze_response(
            result, aid, report_payload.get("risk_summary"), plan, user.id or 0, db, cached=False
        )
    except ValueError as e:
        if job:
            job.status = "failed"
            job.error_message = str(e)[:500]
            db.add(job)
            db.commit()
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException:
        if job:
            job.status = "failed"
            job.error_message = "HTTPException"
            db.add(job)
            db.commit()
        raise
    except Exception as e:
        if job:
            job.status = "failed"
            job.error_message = str(e)[:500]
            db.add(job)
            db.commit()
        log.exception("Analyze error: %s", e)
        raise HTTPException(
            status_code=503,
            detail="Analiz şu an yapılamadı. Lütfen tekrar deneyin.",
        )


@app.post("/analyze/upload", response_model=AnalyzeResponse)
@limiter.limit("10/minute")
async def analyze_upload(
    request: Request,
    file: UploadFile = File(...),
    lang: str = Form("tr"),
    user: User = Depends(get_current_user_or_dev_guest),
    db: Session = Depends(get_db),
):
    """Dosya yükleme: multipart/form-data, alan adı 'file' (zorunlu), 'lang' (opsiyonel)."""
    try:
        return await _analyze_upload_impl(request, file, lang, user, db)
    except HTTPException:
        raise
    except Exception as e:
        log.exception("analyze/upload top-level error: %s", e)
        return JSONResponse(
            status_code=500,
            content={"error": "Analiz sırasında hata oluştu.", "detail": str(e)[:200]},
        )


async def _analyze_upload_impl(
    request: Request,
    file: UploadFile,
    lang: str,
    user: User,
    db: Session,
) -> AnalyzeResponse:
    """analyze_upload iç mantığı (try/except dışında)."""
    log.info("analyze/upload: filename=%s", getattr(file, "filename", ""))
    test_mode = _is_test_mode(request)
    plan = _dev_override_plan(request, user)
    _active_inst, _active_membership = (None, None)
    if not test_mode:
        _check_analyze_hourly_limit(user.id or 0)
        _active_inst, _active_membership = _get_active_institution(db, user.id or 0)
        if _active_inst and _institution_can_analyze(_active_inst):
            _use_institution_credit(db, _active_inst)
        else:
            if _active_inst and not _institution_can_analyze(_active_inst):
                _active_inst = None
            limit = _aylik_limit(plan)
            kullanilan = _aylik_analiz_sayisi(db, user.id or 0)
            ilk_ucretsiz = _ilk_analiz_ucretsiz(db, user.id or 0)
            if not ilk_ucretsiz and not _can_analyze(limit, kullanilan, user):
                raise HTTPException(
                    status_code=402,
                    detail=f"Aylık analiz hakkınız doldu ({kullanilan}/{limit}). Önce 1 analiz satın alın veya Pro plana geçin.",
                )
            if not ilk_ucretsiz:
                _use_analysis_credit(db, user, limit, kullanilan)
    _inst_id_for_save = _active_inst.id if _active_inst else None

    if not file.filename:
        raise HTTPException(status_code=400, detail="Dosya seçin.")
    ext = "." + file.filename.lower().rsplit(".", 1)[-1] if "." in file.filename else ""
    report_lang = _report_lang_from_request(request, lang)
    try:
        content = await file.read()
    except Exception as e:
        log.exception("analyze/upload file read error: %s", e)
        raise HTTPException(status_code=400, detail="Dosya okunamadı.")

    size_bytes = len(content)
    if size_bytes == 0:
        raise HTTPException(status_code=400, detail="Dosya boş.")

    max_bytes = _max_upload_bytes()
    if size_bytes > max_bytes:
        # Limit aşımı UploadLog
        try:
            ul = UploadLog(
                user_id=user.id or 0,
                filename=file.filename,
                file_size_bytes=size_bytes,
                status="failed",
                error_message=f"too_large: size={size_bytes}, limit={max_bytes}, mime={getattr(file, 'content_type', '')}",
            )
            db.add(ul)
            db.commit()
        except Exception as e:
            log.warning("UploadLog write failed for size limit: %s", e)
        mb_limit = max_bytes // (1024 * 1024)
        raise HTTPException(status_code=413, detail=f"Dosya en fazla {mb_limit} MB olabilir.")

    # MIME + magic bytes kontrolü
    reported_mime = getattr(file, "content_type", "") or ""
    magic_type = _detect_magic_type(content)
    magic_ext = None
    expected_mime = None
    if magic_type == "pdf":
        magic_ext = ".pdf"
        expected_mime = "application/pdf"
    elif magic_type == "jpeg":
        magic_ext = (".jpg", ".jpeg")  # JPEG ve JPG aynı format (image/jpeg)
        expected_mime = "image/jpeg"
    elif magic_type == "png":
        magic_ext = ".png"
        expected_mime = "image/png"

    # Mobil: bazen dosya adı uzantısız veya farklı gelir; içerik doğruysa uzantıyı magic'e göre kabul et
    if magic_type == "jpeg" and (ext not in ALLOWED_UPLOAD_EXTENSIONS or not ext):
        ext = ".jpg"
    elif magic_type == "png" and (ext not in ALLOWED_UPLOAD_EXTENSIONS or not ext):
        ext = ".png"
    elif magic_type == "pdf" and (ext not in ALLOWED_UPLOAD_EXTENSIONS or not ext):
        ext = ".pdf"

    ext_ok = (ext == magic_ext) if isinstance(magic_ext, str) else ((ext in magic_ext) if magic_ext is not None else False)
    if magic_type == "jpeg":
        mime_ok = reported_mime in ("image/jpeg", "image/jpg", "")
    else:
        mime_ok = reported_mime == expected_mime or (reported_mime == "" and magic_type is not None)
    # Uzantı .jpg/.jpeg ise (içerik PDF değilse) her zaman kabul — Mobil Safari/iOS
    jpeg_always_ok = ext in (".jpg", ".jpeg") and magic_type != "pdf"
    classic_ok = (
        magic_type is not None
        and ext_ok
        and (reported_mime in ALLOWED_UPLOAD_MIME_TYPES or reported_mime == "")
        and mime_ok
    )
    valid = ext in ALLOWED_UPLOAD_EXTENSIONS and (classic_ok or jpeg_always_ok)

    if not valid:
        log.warning(
            "analyze/upload reject: ext=%r, reported_mime=%r, magic_type=%r",
            ext, reported_mime, magic_type,
        )
        # Tip uyuşmazlığı UploadLog
        try:
            ul = UploadLog(
                user_id=user.id or 0,
                filename=file.filename,
                file_size_bytes=size_bytes,
                status="failed",
                error_message=(
                    f"invalid_type: ext={ext}, mime={reported_mime}, magic={magic_type}"
                ),
            )
            db.add(ul)
            db.commit()
        except Exception as e:
            log.warning("UploadLog write failed for invalid type: %s", e)
        raise HTTPException(
            status_code=400,
            detail="Sadece PDF, JPG/JPEG veya PNG dosyalarını yükleyebilirsiniz.",
        )
    try:
        return _process_uploaded_content(
            content, file.filename, report_lang, user.id or 0, db, request, save=True,
            plan=getattr(user, "plan", None) or "free",
            institution_id=_inst_id_for_save,
        )
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log.exception("analyze/upload process error: %s", e)
        raise HTTPException(status_code=400, detail=f"Dosya işlenemedi: {str(e)[:80]}")


def _build_analyze_response(
    result: str,
    aid: int | None,
    risk_summary: dict | None,
    plan: str,
    user_id: int,
    db: Session,
    cached: bool = False,
) -> AnalyzeResponse:
    """Ortak: premiumPdf = single|monthly|yearly|pro (gauge+score+PDF), premiumTrend = monthly|yearly|pro (trend açık). PREMIUM_VISIBLE_FOR_FREE=True ise free de görür. Tek analiz ve aylıkta rapor ekranında sadece önizleme + kapı (hepsini görmek için aylık/yıllık)."""
    from app.core.plan_config import normalize_plan_type

    premium_pdf = PREMIUM_VISIBLE_FOR_FREE or plan in ("single", "monthly", "yearly", "pro")
    premium_trend = PREMIUM_VISIBLE_FOR_FREE or plan in ("monthly", "yearly", "pro")
    # Tek analiz ve aylık: ekranda tam rapor gösterme; önizleme + "Hepsini görmek için aylık veya yıllık abonelik alın" kapısı. Yıllık/pro = tam rapor.
    report_limited_preview = plan in ("free", "single", "monthly")
    overall = (risk_summary or {}).get("overall") or {}
    health_score = HealthScoreSchema(score=overall.get("score", 0), level=overall.get("level", "mid")) if risk_summary else None
    trend = _get_trend_for_user(db, user_id, exclude_analysis_id=aid) if premium_trend and user_id else None
    plan_type = normalize_plan_type(plan)
    return AnalyzeResponse(
        sonuc=result,
        analiz_id=aid,
        cached=cached,
        premium=premium_pdf,
        risk_summary=risk_summary,
        health_score=health_score,
        trend=trend,
        ui_hints=UiHintsSchema(locked=not premium_pdf, report_limited_preview=report_limited_preview),
        pdf=PdfInfoSchema(template="premium" if premium_pdf else "basic", available=True),
        plan_type=plan_type,
    )


def _process_uploaded_content(
    content: bytes,
    filename: str,
    report_lang: str | None,
    user_id: int,
    db: Session,
    request: Request,
    save: bool = True,
    plan: str | None = None,
    institution_id: int | None = None,
) -> AnalyzeResponse:
    """Ortak: yüklenen dosya içeriğini analiz eder (görsel veya PDF). Her zaman kaydeder (PDF/rapor için analiz_id döner)."""
    ext = "." + filename.lower().rsplit(".", 1)[-1] if "." in filename else ""
    if ext not in ALLOWED_UPLOAD_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Sadece PDF, JPG/JPEG veya PNG yükleyebilirsiniz.")
    ul = None
    if save:
        ul = UploadLog(user_id=user_id, filename=filename, file_size_bytes=len(content), status="pending")
        db.add(ul)
        db.commit()
        db.refresh(ul)
    t0 = time.perf_counter()
    try:
        if ext in IMAGE_EXTENSIONS:
            mime = MIME_MAP.get(ext, "image/jpeg")
            job = AnalysisJob(user_id=user_id, status="processing") if save else None
            if job:
                db.add(job)
                db.commit()
                db.refresh(job)
            result, usage = analyze_blood_test_from_image(content, mime, lang=report_lang)
            input_preview = f"[Görsel: {filename}]"
            aid = _save_analysis(db, user_id, input_preview, result, "image", plan_type=plan, institution_id=institution_id)
            if job:
                job.status = "done"
                job.analysis_record_id = aid
                job.duration_ms = int((time.perf_counter() - t0) * 1000)
                if usage:
                    job.prompt_tokens = usage.get("prompt_tokens")
                    job.completion_tokens = usage.get("completion_tokens")
                db.add(job)
                db.commit()
            _attach_original_file(db, aid, content, filename, "image")
            if ul:
                ul.status = "success"
                ul.duration_ms = int((time.perf_counter() - t0) * 1000)
                db.add(ul)
                db.commit()
            _audit(db, "analyze", user_id, _client_ip(request), institution_id=institution_id)
            plan = plan or (getattr(db.get(User, user_id), "plan", None) or "free")
            return _build_analyze_response(result, aid, None, plan, user_id, db, cached=False)
        text = extract_text_from_pdf(content)
        if "çıkarılamadı" in text:
            raise HTTPException(status_code=400, detail="PDF'den metin okunamadı. Farklı bir dosya deneyin.")
        job = AnalysisJob(user_id=user_id, status="processing") if save else None
        if job:
            db.add(job)
            db.commit()
            db.refresh(job)
        labs_norm = {"t": " ".join(text.split()).strip(), "dn": None}
        report_payload, usage = analyze_blood_test(text, lang=report_lang, plan="free", labs_norm=labs_norm)
        result = report_payload["sonuc"]
        aid = _save_analysis(db, user_id, text[:2000], result, "pdf", plan_type=plan, institution_id=institution_id)
        if job:
            job.status = "done"
            job.analysis_record_id = aid
            job.duration_ms = int((time.perf_counter() - t0) * 1000)
            if usage:
                job.prompt_tokens = usage.get("prompt_tokens")
                job.completion_tokens = usage.get("completion_tokens")
            db.add(job)
            db.commit()
        _attach_original_file(db, aid, content, filename, "pdf")
        if ul:
            ul.status = "success"
            ul.duration_ms = int((time.perf_counter() - t0) * 1000)
            db.add(ul)
            db.commit()
        _audit(db, "analyze", user_id, _client_ip(request), institution_id=institution_id)
        plan = plan or (getattr(db.get(User, user_id), "plan", None) or "free")
        return _build_analyze_response(result, aid, report_payload.get("risk_summary"), plan, user_id, db, cached=False)
    except Exception as e:
        try:
            db.rollback()
        except Exception:
            pass
        if ul:
            try:
                ul.status = "failed"
                ul.error_message = str(e)[:500]
                ul.duration_ms = int((time.perf_counter() - t0) * 1000)
                db.add(ul)
                db.commit()
            except Exception:
                pass
        if save:
            try:
                last_job = db.exec(select(AnalysisJob).where(AnalysisJob.user_id == user_id).order_by(AnalysisJob.id.desc()).limit(1)).first()
                if last_job:
                    last_job.status = "failed"
                    last_job.error_message = str(e)[:500]
                    db.add(last_job)
                    db.commit()
            except Exception:
                pass
        raise


@app.post("/analyze/upload-json", response_model=AnalyzeResponse)
async def analyze_upload_json(
    request: Request,
    body: UploadJsonRequest,
    user: User = Depends(get_current_user_or_dev_guest),
    db: Session = Depends(get_db),
):
    """Dosyayı base64 JSON ile alır (UI dışı / yedek). file_base64, filename, lang."""
    test_mode = _is_test_mode(request)
    _active_inst, _active_membership = (None, None)
    if not test_mode:
        plan = getattr(user, "plan", "free") or "free"
        _active_inst, _active_membership = _get_active_institution(db, user.id or 0)
        if _active_inst and _institution_can_analyze(_active_inst):
            _use_institution_credit(db, _active_inst)
        else:
            if _active_inst and not _institution_can_analyze(_active_inst):
                _active_inst = None
            limit = _aylik_limit(plan)
            kullanilan = _aylik_analiz_sayisi(db, user.id or 0)
            ilk_ucretsiz = _ilk_analiz_ucretsiz(db, user.id or 0)
            if not ilk_ucretsiz and not _can_analyze(limit, kullanilan, user):
                raise HTTPException(
                    status_code=402,
                    detail=f"Aylık analiz hakkınız doldu ({kullanilan}/{limit}). Önce 1 analiz satın alın veya Pro plana geçin.",
                )
            if not ilk_ucretsiz:
                _use_analysis_credit(db, user, limit, kullanilan)
    if not (body.file_base64 and body.file_base64.strip()):
        raise HTTPException(status_code=400, detail="Dosya verisi gönderilmedi (file_base64 zorunlu).")
    try:
        content = base64.b64decode(body.file_base64.strip(), validate=True)
    except Exception as e:
        log.warning("upload-json b64 decode error: %s", e)
        raise HTTPException(status_code=400, detail="Dosya verisi geçersiz (base64).")
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Dosya en fazla 10 MB olabilir.")
    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Dosya boş.")
    report_lang = _report_lang_from_request(request, body.lang)
    _inst_id_for_save = _active_inst.id if _active_inst else None
    return _process_uploaded_content(
        content, body.filename or "upload", report_lang, user.id or 0, db, request, save=not test_mode,
        plan=getattr(user, "plan", None) or "free",
        institution_id=_inst_id_for_save,
    )


@app.get("/analyze/usage")
def analyze_usage(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Giriş yapmış kullanıcının bu ayki kullanım bilgisi (frontend için)."""
    plan = getattr(user, "plan", "free") or "free"
    limit = _aylik_limit(plan)
    kullanilan = _aylik_analiz_sayisi(db, user.id or 0)
    extra = _extra_credits(user)
    total_ever = _total_analiz_sayisi(db, user.id or 0)
    last_rec = (
        db.exec(
            select(AnalysisRecord)
            .where(AnalysisRecord.user_id == user.id)
            .order_by(AnalysisRecord.created_at.desc())
            .limit(1)
        ).first()
    )
    last_analysis_at = last_rec.created_at.isoformat() + "Z" if (last_rec and last_rec.created_at) else None
    return {
        "kullanilan": kullanilan,
        "limit": limit,
        "plan": plan,
        "extra_credits": extra,
        "first_analysis_free": total_ever == 0,
        "last_analysis_at": last_analysis_at,
    }


@app.get("/analyze/history", response_model=list[AnalysisHistoryItem])
def analyze_history(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = 50,
    source: str | None = Query(None, description="Filtre: text, pdf, image"),
    q: str | None = Query(None, description="Arama (giriş veya sonuç metninde)"),
    favorite_only: bool = Query(False, description="Sadece favoriler"),
):
    stmt = (
        select(AnalysisRecord)
        .where(AnalysisRecord.user_id == user.id)
        .order_by(AnalysisRecord.created_at.desc())
        .limit(limit)
    )
    if source and source.strip():
        stmt = stmt.where(AnalysisRecord.source == source.strip().lower())
    if getattr(AnalysisRecord, "is_favorite", None) is not None and favorite_only:
        stmt = stmt.where(AnalysisRecord.is_favorite == True)
    if q and q.strip():
        q = q.strip()
        stmt = stmt.where(
            or_(AnalysisRecord.input_text.contains(q), AnalysisRecord.result_text.contains(q))
        )
    rows = list(db.exec(stmt).all())
    return [
        AnalysisHistoryItem(
            id=r.id or 0,
            input_preview=(r.input_text[:120] + "…") if len(r.input_text) > 120 else r.input_text,
            result_preview=(r.result_text[:200] + "…") if len(r.result_text) > 200 else r.result_text,
            source=r.source,
            created_at=r.created_at.isoformat() if hasattr(r.created_at, "isoformat") else str(r.created_at),
            is_favorite=getattr(r, "is_favorite", False),
        )
        for r in rows
    ]


@app.get("/analyze/export")
def analyze_export(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Kullanıcının tüm analizlerini JSON olarak döner (KVKK/GDPR veri taşınabilirliği)."""
    stmt = (
        select(AnalysisRecord)
        .where(AnalysisRecord.user_id == user.id)
        .order_by(AnalysisRecord.created_at.desc())
    )
    rows = list(db.exec(stmt).all())
    data = {
        "exported_at": datetime.utcnow().isoformat() + "Z",
        "analyses": [
            {
                "id": r.id,
                "input_text": r.input_text,
                "result_text": r.result_text,
                "source": r.source,
                "created_at": r.created_at.isoformat() if hasattr(r.created_at, "isoformat") else str(r.created_at),
                "doctor_notes": getattr(r, "doctor_notes", None),
            }
            for r in rows
        ],
    }
    from fastapi.responses import JSONResponse
    return JSONResponse(
        content=data,
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=norya-verilerim.json"},
    )


@app.get("/analyze/history/{analysis_id}", response_model=AnalysisDetail)
def analyze_history_detail(
    analysis_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or rec.user_id != (user.id or 0):
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    return AnalysisDetail(
        id=rec.id or 0,
        input_text=rec.input_text,
        result_text=rec.result_text,
        source=rec.source,
        created_at=rec.created_at.isoformat() if hasattr(rec.created_at, "isoformat") else str(rec.created_at),
        doctor_notes=getattr(rec, "doctor_notes", None),
        is_favorite=getattr(rec, "is_favorite", False),
        plan_type=getattr(rec, "plan_type", None) or "single",
    )


@app.patch("/analyze/history/{analysis_id}")
def analyze_history_toggle_favorite(
    analysis_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Favori işaretini aç/kapa."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or rec.user_id != (user.id or 0):
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    rec.is_favorite = not getattr(rec, "is_favorite", False)
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return {"is_favorite": getattr(rec, "is_favorite", False)}


def _public_base_url_for_pdf_verify(request: Request) -> str:
    """
    PDF içindeki QR doğrulama linki için dışarıdan erişilebilir base URL.
    Nginx/gunicorn arkasında request.base_url genelde http://127.0.0.1:8000 olur; QR telefonda açılmaz.
    Öncelik: BACKEND_PUBLIC_URL > FRONTEND_URL (localhost değilse) > X-Forwarded-* > Host.
    """
    u = (getattr(settings, "backend_public_url", None) or "").strip().rstrip("/")
    if u:
        return u
    fu = (getattr(settings, "frontend_url", None) or "").strip().rstrip("/")
    if fu and "127.0.0.1" not in fu and "localhost" not in fu.lower():
        return fu
    proto = (request.headers.get("x-forwarded-proto") or "").split(",")[0].strip().lower()
    host = (request.headers.get("x-forwarded-host") or request.headers.get("host") or "").split(",")[0].strip()
    if host:
        if proto not in ("http", "https"):
            proto = "https" if (getattr(settings, "environment", "") or "").strip().lower() == "production" else "http"
        host = host.split("/")[0].strip()
        return f"{proto}://{host}"
    return str(request.base_url).rstrip("/")


def _get_pdf_requester_id(
    analysis_id: int,
    access_token: str | None = Query(None, description="Canlıda proxy Authorization keserse URL token (POST /pdf-token ile alınır)"),
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> int:
    """Bearer veya access_token ile PDF indirme yetkisi; canlıda proxy header kesebildiği için URL token desteklenir."""
    if access_token:
        decoded = decode_pdf_access_token(access_token)
        if decoded and decoded[0] == analysis_id:
            return decoded[1]
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    if not credentials:
        raise HTTPException(status_code=401, detail="Giriş yapın veya geçerli indirme linki kullanın.")
    payload = decode_access_token(credentials.credentials)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Geçersiz veya süresi dolmuş token.")
    return int(payload["sub"])


@app.post("/analyze/history/{analysis_id}/pdf-token")
def get_pdf_download_token(
    analysis_id: int,
    # Local development'da token olmayabilir; analiz endpoint'leri `get_current_user_or_dev_guest`
    # ile dev guest kullanıyor. PDF token üretimi için de aynı davranışı uygulayalım.
    user: User = Depends(get_current_user_or_dev_guest),
    db: Session = Depends(get_db),
) -> dict:
    """PDF indirme için 5 dakika geçerli tek kullanımlık token. Canlıda Raporu İndir bu token ile URL açar."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or rec.user_id != (user.id or 0):
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    token = create_pdf_access_token(analysis_id, user.id or 0)
    return {"access_token": token, "expires_in": 300}


@app.get("/analyze/history/{analysis_id}/pdf")
def download_analysis_pdf(
    request: Request,
    analysis_id: int,
    lang: str = Query("tr", description="Rapor dili: tr, en, de, fr, es, it, he, ar, hi, el, cs, sr"),
    disposition: str = Query("inline", description="inline = tarayıcıda aç (iOS uyumu), attachment = indir"),
    scope: str = Query(None, description="pro = Pro görünümü kapsamında PDF (risk, trend, tam içerik)"),
    user_id: int = Depends(_get_pdf_requester_id),
    db: Session = Depends(get_db),
):
    """İlgili analizin premium PDF raporu. Bearer veya ?access_token= ile yetki (canlıda proxy için token). scope=pro ile Pro kapsamlı PDF."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or rec.user_id != user_id:
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    report_date = None
    if getattr(rec, "created_at", None):
        dt = rec.created_at
        if hasattr(dt, "strftime"):
            report_date = dt.strftime("%d.%m.%Y %H:%M")
        else:
            report_date = str(dt)
    report_lang = (lang or "tr").strip().lower()[:5]
    user = db.get(User, user_id)
    plan = getattr(user, "plan", None) or "free"
    plan_for_pdf = getattr(rec, "plan_type", None) or plan
    use_pro_scope = (scope or "").strip().lower() == "pro"
    # SINGLE/STANDARD: premium PDF şablonunu kullanmaz; sadece monthly/yearly/pro veya scope=pro premium şablona geçer.
    premium_pdf = use_pro_scope or PREMIUM_VISIBLE_FOR_FREE or plan_for_pdf in ("monthly", "yearly", "pro")
    premium_trend = use_pro_scope or PREMIUM_VISIBLE_FOR_FREE or plan_for_pdf in ("monthly", "yearly", "pro")
    # PDF cache şema versiyonu: çıktı yapısı değiştiğinde eski PDF'ler yerine yenileri üretmek için anahtara eklenir.
    _PDF_SCHEMA_VERSION = 6  # Sağlık yaşı: dürüst etiket + feragatname (std/monthly/premium PDF)
    cache_key = (analysis_id, report_lang, "pro" if use_pro_scope else "std", plan_for_pdf or "free", _PDF_SCHEMA_VERSION)
    now_ts = time.time()
    with _pdf_cache_lock:
        if cache_key in _pdf_cache:
            cached_bytes, cached_at = _pdf_cache[cache_key]
            if now_ts - cached_at < _PDF_CACHE_TTL_SEC:
                filename = f"norya-rapor-{analysis_id}.pdf"
                disp = "attachment" if (disposition or "").strip().lower() == "attachment" else "inline"
                return Response(
                    content=cached_bytes,
                    media_type="application/pdf",
                    headers={"Content-Disposition": f'{disp}; filename="{filename}"'},
                )
            else:
                del _pdf_cache[cache_key]
    trend_data = _get_trend_for_user(db, user_id, exclude_analysis_id=analysis_id) if premium_trend else None
    verify_base_url = _public_base_url_for_pdf_verify(request)
    from app.core.plan_config import normalize_plan_type

    verification_package = normalize_plan_type(plan_for_pdf)
    verification_info = get_or_create_verification(
        db, analysis_id, user_id, verification_package, report_lang, verify_base_url
    )
    try:
        pdf_bytes = build_report_pdf(
            result_text=rec.result_text or "",
            report_date=report_date,
            lang=report_lang,
            report_id=analysis_id,
            user_identifier=user.email if user else None,
            patient_name=user.email if user else None,
            plan_name=plan_for_pdf if premium_pdf else (user.plan if user else None),
            source_type=rec.source if getattr(rec, "source", None) else None,
            trend_data=trend_data,
            verification_info=verification_info,
        )
    except Exception as e:
        log.exception("PDF build failed for analysis_id=%s: %s", analysis_id, e)
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    with _pdf_cache_lock:
        _pdf_cache[cache_key] = (pdf_bytes, time.time())
    filename = f"norya-rapor-{analysis_id}.pdf"
    disp = "attachment" if (disposition or "").strip().lower() == "attachment" else "inline"
    # MinIO açıksa yükle ve presigned URL ile yönlendir; frontend MinIO'dan indirir
    minio_url = upload_report_pdf(analysis_id, pdf_bytes, filename)
    if minio_url:
        return RedirectResponse(url=minio_url, status_code=302)
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'{disp}; filename="{filename}"'},
    )


@app.get("/analyze/history/{analysis_id}/pdf/doctor")
def download_doctor_pdf(
    request: Request,
    analysis_id: int,
    lang: str = Query("tr", description="Rapor dili: tr, en, de, fr, es, it, he, ar, hi, el, cs, sr"),
    disposition: str = Query("inline", description="inline = tarayıcıda aç, attachment = indir"),
    user_id: int = Depends(_get_pdf_requester_id),
    db: Session = Depends(get_db),
):
    """Doktoruma götür PDF: premiumPdf true ise premium klinik rapor, değilse hekime özel basit şablon."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or rec.user_id != user_id:
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    report_date = None
    if getattr(rec, "created_at", None):
        dt = rec.created_at
        if hasattr(dt, "strftime"):
            report_date = dt.strftime("%d.%m.%Y %H:%M")
        else:
            report_date = str(dt)
    report_lang = (lang or "tr").strip().lower()[:5]
    user = db.get(User, user_id)
    plan = getattr(user, "plan", None) or "free"
    plan_for_pdf = getattr(rec, "plan_type", None) or plan
    premium_pdf = PREMIUM_VISIBLE_FOR_FREE or plan_for_pdf in ("single", "monthly", "yearly", "pro")
    premium_trend = PREMIUM_VISIBLE_FOR_FREE or plan_for_pdf in ("monthly", "yearly", "pro")
    trend_data = _get_trend_for_user(db, user_id, exclude_analysis_id=analysis_id) if premium_trend else None
    verify_base_url = _public_base_url_for_pdf_verify(request)
    from app.core.plan_config import normalize_plan_type

    verification_package = normalize_plan_type(plan_for_pdf)
    verification_info = get_or_create_verification(
        db, analysis_id, user_id, verification_package, report_lang, verify_base_url
    )
    try:
        if premium_pdf:
            pdf_bytes = build_report_pdf(
                result_text=rec.result_text or "",
                report_date=report_date,
                lang=report_lang,
                report_id=analysis_id,
                user_identifier=user.email if user else None,
                patient_name=user.email if user else None,
                plan_name=plan_for_pdf if premium_pdf else (user.plan if user else None),
                source_type=rec.source if getattr(rec, "source", None) else None,
                trend_data=trend_data,
                verification_info=verification_info,
            )
        else:
            pdf_bytes = build_doctor_pdf(
                result_text=rec.result_text or "",
                report_date=report_date,
                lang=report_lang,
            )
    except Exception as e:
        log.exception("Doctor PDF build failed for analysis_id=%s: %s", analysis_id, e)
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    filename = f"norya-doctor-{analysis_id}.pdf"
    disp = "attachment" if (disposition or "").strip().lower() == "attachment" else "inline"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'{disp}; filename="{filename}"'},
    )


@app.post("/analyze/share/{analysis_id}")
def create_share_link(
    analysis_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or rec.user_id != (user.id or 0):
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    token_str = secrets.token_urlsafe(24)
    db.add(ShareToken(analysis_id=rec.id or 0, token=token_str))
    db.commit()
    return {"token": token_str}


@app.get("/share/{token}")
def get_shared_analysis(token: str, db: Session = Depends(get_db)):
    stmt = select(ShareToken).where(ShareToken.token == token)
    share = db.exec(stmt).first()
    if not share:
        raise HTTPException(status_code=404, detail="Paylaşım linki geçersiz veya kaldırılmış.")
    rec = db.get(AnalysisRecord, share.analysis_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Analiz bulunamadı.")
    return {
        "input_text": rec.input_text,
        "result_text": rec.result_text,
        "source": rec.source,
        "created_at": rec.created_at.isoformat() if hasattr(rec.created_at, "isoformat") else str(rec.created_at),
    }


# ---------- Ödeme: PayTR (Türkiye sanal pos), tam sayfa yönlendirme (iframe yok) ----------
def _paytr_enabled() -> bool:
    return bool(
        getattr(settings, "paytr_merchant_id", None)
        and getattr(settings, "paytr_merchant_key", None)
        and getattr(settings, "paytr_merchant_salt", None)
    )


def _paytr_canonical_base(request: Request) -> str:
    """PayTR success/fail/callback URL'leri için tek canonical domain (www/non-www uyumlu)."""
    base = (getattr(settings, "frontend_url", "") or "").strip().rstrip("/")
    if not base:
        base = str(request.base_url).rstrip("/")
    # Tek domain: www.noryaai.com ve noryaai.com -> https://noryaai.com
    try:
        from urllib.parse import urlparse
        p = urlparse(base)
        host = (p.netloc or "").lower()
        if host.startswith("www."):
            host = host[4:]
        if host in ("noryaai.com", "noryaai.com.tr"):
            base = f"{p.scheme or 'https'}://{host}"
        return base.rstrip("/")
    except Exception:
        return base.rstrip("/")


def _paytr_amount(product: str, db: Session) -> int:
    """Merkezi fiyat kaynağından plan tutarını (EUR cent) döner."""
    base = get_base_prices_cents(db)
    return base.get(product, 300)


def _paytr_amount_and_currency(amount_eur_cents: int) -> tuple[int, str]:
    """PayTR'ye gönderilecek tutar ve para birimi. EUR hesabı yoksa TL (kuruş) kullanır."""
    rate = float(getattr(settings, "paytr_eur_to_try_rate", 0) or 0)
    if rate > 0:
        # EUR → TL: amount_eur_cents/100 * rate = TL; kuruş = TL * 100
        amount_try_kurus = int(round((amount_eur_cents / 100.0) * rate * 100))
        return (max(1, amount_try_kurus), "TL")
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"
    return (amount_eur_cents, currency)


def _paytr_reason_to_detail(reason: str | None) -> str:
    """PayTR 'reason' metnini kullanıcıya gösterilecek Türkçe mesaja çevirir."""
    if not reason:
        return "PayTR token alınamadı. Lütfen sayfayı yenileyip tekrar deneyin; sorun sürerse destek@noryaai.com ile iletişime geçin."
    r = (reason or "").strip().lower()
    if "magaza" in r or "mağaza" in r or "mağaza aktif" in r or ("store" in r and "active" in r):
        return "Ödeme sistemi şu an kullanılamıyor. PayTR panelinde mağazanın aktif olduğunu ve entegrasyon bilgilerinin (Mağaza No, Parola, Gizli Anahtar) doğru girildiğini kontrol edin."
    if "paytr_token" in r or "gecersiz" in r and "token" in r or "hash" in r:
        return "Ödeme bağlantısı doğrulanamadı. Lütfen sayfayı yenileyip tekrar deneyin; sorun sürerse destek@noryaai.com ile iletişime geçin."
    if "user_ip" in r or "ip" in r and ("gecersiz" in r or "invalid" in r):
        return "Ödeme alınamadı (IP doğrulama). Lütfen VPN kullanmıyorsanız sayfayı yenileyip tekrar deneyin veya destek@noryaai.com ile iletişime geçin."
    return reason


def _plan_code_to_product_amount(plan_code: str, db: Session) -> tuple[str, int]:
    """plan_code -> (product, amount_cent). Merkezi pricing planından; geçersizse ValueError."""
    plan_map = get_plan_code_to_product_cents(db)
    t = plan_map.get((plan_code or "").strip().lower())
    if not t:
        raise ValueError("Geçersiz plan_code. Desteklenen: single_13eur, monthly_50eur, yearly_99eur")
    return t[0], t[1]


@app.post("/paytr/init")
def paytr_init(
    body: PaytrInitRequest,
    request: Request,
    current_user: User | None = Depends(get_current_user_optional),
    db: Session = Depends(get_db),
):
    """
    PayTR iFrame token üretir; sipariş açar. plan_code ile paket seçilir.
    Giriş yoksa email ile kullanıcı bulunur/oluşturulur. Dönüş: { status, token, merchant_oid }.
    """
    if not _paytr_enabled():
        raise HTTPException(status_code=503, detail="Ödeme şu an aktif değil. PayTR ayarlarını kontrol edin.")
    try:
        return _paytr_init_impl(body, request, current_user, db)
    except HTTPException:
        raise
    except Exception as e:
        err_type = type(e).__name__
        err_msg = (str(e) or "").strip()[:200]
        log.exception("PayTR init failed: %s: %s", err_type, err_msg)
        if not err_msg:
            err_msg = "Beklenmeyen sunucu hatası. Loglarda 'PayTR init failed' arayın."
        raise HTTPException(
            status_code=500,
            detail=f"Ödeme başlatılamadı: {err_msg}",
        )


def _paytr_init_impl(body: PaytrInitRequest, request: Request, current_user: User | None, db: Session):
    try:
        product, amount = _plan_code_to_product_amount(body.plan_code, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    quantity = max(1, min(int(getattr(body, "quantity", 1) or 1), 10))
    if product == "single":
        quantity = max(1, min(quantity, 10))
    elif product == "monthly":
        quantity = max(1, min(quantity, 6))
    else:
        quantity = max(1, min(quantity, 3))

    coupon_used: str | None = None
    if body.coupon_code and (code := (body.coupon_code or "").strip()):
        discount, err = validate_coupon(db, code, product, amount)
        if err:
            raise HTTPException(status_code=400, detail=err)
        amount = max(1, amount - discount)
        coupon_used = code

    total_amount = amount * quantity

    user: User | None = current_user
    if not user and (body.email or "").strip():
        email = (body.email or "").strip().lower()
        if "@" in email:
            stmt = select(User).where(User.email == email)
            user = db.exec(stmt).first()
            if not user:
                try:
                    user = User(
                        email=email,
                        hashed_password=hash_password("guest_" + secrets.token_hex(32)),
                        full_name=(body.name or "").strip()[:200] or "",
                    )
                    db.add(user)
                    db.commit()
                    db.refresh(user)
                except SQLIntegrityError:
                    db.rollback()
                    user = db.exec(select(User).where(User.email == email)).first()
                except Exception:
                    db.rollback()
                    raise
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Giriş yapın veya geçerli bir e-posta girin (email alanı zorunlu).",
        )

    user_id = user.id or 0
    merchant_oid = "norya" + uuid.uuid4().hex[:20]
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"

    customer_email_val = (user.email or "").strip().lower() if user else None
    coupon_used_trunc = (coupon_used or "")[:64] if coupon_used else None
    order = PaymentOrder(
        merchant_oid=merchant_oid,
        user_id=user_id,
        customer_email=customer_email_val or None,
        product=product,
        amount_kurus=total_amount,
        currency=currency,
        status="pending",
        coupon_code_used=coupon_used_trunc,
        quantity=quantity,
    )
    db.add(order)
    try:
        db.commit()
    except SQLIntegrityError as e:
        log.warning("PayTR init: order insert IntegrityError merchant_oid=%s: %s", merchant_oid, e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Sipariş oluşturulamadı (kayıt çakışması). Lütfen tekrar deneyin.")
    except Exception as e:
        log.exception("PayTR init: order insert failed: %s", e)
        db.rollback()
        err_msg = str(e).strip()[:120] if str(e) else ""
        if "no such column" in err_msg.lower() or "unknown column" in err_msg.lower():
            raise HTTPException(
                status_code=500,
                detail="Veritabanı şeması güncel değil. Sunucu yöneticisi init_db veya migration çalıştırmalı.",
            )
        raise HTTPException(status_code=500, detail="Sipariş oluşturulamadı.")

    paytr_amount, paytr_currency = _paytr_amount_and_currency(total_amount)
    user_ip = _client_ip(request)
    email = user.email or "customer@norya.ai"
    product_name = {"single": "1 Analiz", "monthly": "Pro Aylık", "yearly": "Pro Yıllık"}.get(product, product)
    log.info(
        "PAYTR_INIT: merchant_oid=%s plan_code=%s quantity=%s amount=%s currency=%s user_ip=%s",
        merchant_oid, body.plan_code, quantity, paytr_amount, paytr_currency, user_ip,
    )

    import base64
    import hmac
    import hashlib
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request as UrlRequest

    raw_mid = (settings.paytr_merchant_id or "").strip()
    merchant_id = raw_mid.replace("Value:", "").strip() if raw_mid else ""
    if not merchant_id:
        raise HTTPException(status_code=500, detail="PayTR merchant_id yapılandırılmadı. Ortam değişkeninde sadece mağaza numarası olmalı (örn. 677898).")
    raw_key = getattr(settings, "paytr_merchant_key", None)
    if not raw_key:
        raise HTTPException(status_code=500, detail="PayTR merchant_key (parola) yapılandırılmadı. .env dosyasında PAYTR_MERCHANT_KEY dolu olmalı.")
    if isinstance(raw_key, str):
        merchant_key = raw_key.strip().encode("utf-8")
    elif isinstance(raw_key, bytes):
        merchant_key = raw_key
    else:
        merchant_key = str(raw_key).strip().encode("utf-8")
    if not merchant_key:
        raise HTTPException(status_code=500, detail="PayTR merchant_key boş olamaz.")
    merchant_salt = (settings.paytr_merchant_salt or "").strip()
    if not merchant_salt:
        raise HTTPException(status_code=500, detail="PayTR merchant_salt (gizli anahtar) yapılandırılmadı.")
    basket_amount_str = f"{paytr_amount / 100:.2f}" if paytr_currency == "TL" else f"{total_amount / 100:.2f}"
    user_basket = base64.b64encode(
        json.dumps([[f"Norya Plan: {body.plan_code} x{quantity}", basket_amount_str, 1]]).encode()
    ).decode()
    no_installment = "0"
    max_installment = "0"
    # Canlıda test modu kapalı olmalı
    _env = (getattr(settings, "environment", "") or "").strip().lower()
    test_mode = "0" if _env == "production" else (getattr(settings, "paytr_test_mode", "0") or "0")
    debug_on = "1" if getattr(settings, "paytr_debug", False) else "0"
    paytr_amount_int = int(paytr_amount)
    hash_str = f"{merchant_id}{user_ip}{merchant_oid}{email}{paytr_amount_int}{user_basket}{no_installment}{max_installment}{paytr_currency}{test_mode}"
    paytr_token = base64.b64encode(
        hmac.new(merchant_key, (hash_str + merchant_salt).encode(), hashlib.sha256).digest()
    ).decode()

    # Dil: ödeme sayfasından gelen veya istekten; success/fail ve PayTR sayfası bu dilde
    _lang_raw = (getattr(body, "lang", None) or "").strip().lower()[:2]
    # PayTR yalnızca tr/en destekler; Kanada vb. uluslararası müşteriler için en kullan
    paytr_lang = _lang_raw if _lang_raw in ("tr", "en") else "en"
    return_lang = _lang_raw if _lang_raw in PAYMENT_LANGS else _payment_lang_from_request(request)

    # Tek canonical domain; success/fail URL'lerine merchant_oid ve lang ekle (dönüşte aynı dil)
    _base = _paytr_canonical_base(request)
    ok_url = (getattr(settings, "paytr_ok_url", "") or "").strip() or f"{_base}/payment/success"
    fail_url = (getattr(settings, "paytr_fail_url", "") or "").strip() or f"{_base}/payment/failed"
    sep_ok = "?" if "?" not in ok_url else "&"
    ok_url = f"{ok_url}{sep_ok}merchant_oid={merchant_oid}&lang={return_lang}"
    sep_fail = "?" if "?" not in fail_url else "&"
    fail_url = f"{fail_url}{sep_fail}merchant_oid={merchant_oid}&lang={return_lang}"

    log.info("PAYTR_INIT: merchant_ok_url=%s merchant_fail_url=%s lang=%s", ok_url[:80], fail_url[:80], return_lang)

    post_vals = {
        "merchant_id": merchant_id,
        "user_ip": user_ip,
        "merchant_oid": merchant_oid,
        "email": email,
        "payment_amount": paytr_amount_int,
        "paytr_token": paytr_token,
        "user_basket": user_basket,
        "debug_on": debug_on,
        "no_installment": no_installment,
        "max_installment": max_installment,
        "user_name": ((body.name or user.full_name or "").strip() or "Müşteri")[:60],
        "user_address": "Norya ödeme",
        "user_phone": (getattr(user, "phone", None) or "").strip() or "05551234567",
        "merchant_ok_url": ok_url,
        "merchant_fail_url": fail_url,
        "timeout_limit": "30",
        "currency": paytr_currency,
        "test_mode": test_mode,
        "lang": paytr_lang,
    }
    try:
        req = UrlRequest(
            "https://www.paytr.com/odeme/api/get-token",
            data=urlencode(post_vals).encode(),
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        with urlopen(req, timeout=20) as resp:
            result = json.loads(resp.read().decode())
    except Exception as e:
        order.status = "failed"
        order.admin_note = "init_failed"
        db.add(order)
        db.commit()
        log.warning("PAYTR_INIT: get-token request failed merchant_oid=%s err=%s", merchant_oid, str(e)[:100])
        raise HTTPException(status_code=502, detail=f"PayTR bağlantı hatası: {str(e)[:80]}")

    if result.get("status") != "success":
        reason = result.get("reason") or ""
        log.warning(
            "PAYTR_INIT: get-token failed merchant_oid=%s reason=%s full=%s",
            merchant_oid, reason, result,
        )
        order.status = "failed"
        order.admin_note = "init_failed"
        db.add(order)
        db.commit()
        detail = _paytr_reason_to_detail(reason)
        if not (detail or "").strip():
            detail = (
                "PayTR ödeme sayfası açılamadı. "
                "PayTR panelinde mağaza no, parola ve gizli anahtar doğru mu kontrol edin; "
                "sorun sürerse destek@noryaai.com ile iletişime geçin."
            )
        if reason and ("PayTR:" not in detail and "paytr" not in detail.lower()):
            detail = f"{detail.strip()} (PayTR yanıtı: {reason})"
        raise HTTPException(status_code=400, detail=detail.strip())

    token = result.get("token", "")
    redirect_url = f"https://www.paytr.com/odeme/guvenli/{token}"
    return {"status": "ok", "token": token, "redirect_url": redirect_url, "merchant_oid": merchant_oid}


def _validate_merchant_oid(merchant_oid: str) -> str:
    """Validate merchant_oid format; return stripped. Raises 400 if invalid.
    Beklenen format: alfanumerik, tire/alt çizgi/nokta olabilir; 6–128 karakter (örn. norya + 20 hex veya norya{user_id}{ts}{hex})."""
    oid = (merchant_oid or "").strip()
    if not oid or len(oid) < 6 or len(oid) > 128:
        raise HTTPException(status_code=400, detail="Geçersiz veya eksik merchant_oid.")
    if not all(c.isalnum() or c in "-_." for c in oid):
        raise HTTPException(status_code=400, detail="Geçersiz merchant_oid formatı.")
    return oid


@app.get("/api/orders/status")
def order_status(
    request: Request,
    merchant_oid: str = Query("", description="Sipariş merchant_oid (PayTR yönlendirmesinde query param)"),
    db: Session = Depends(get_db),
):
    """Ödeme durumu: pending, paid, failed. Premium kilit açma ve success sayfası polling için.
    Response: merchant_oid, status (pending|paid|failed), is_premium_active, plan_code?, total_amount_eur?.
    merchant_oid eksik/geçersizse 400 döner."""
    if not (merchant_oid and merchant_oid.strip()):
        raise HTTPException(status_code=400, detail="merchant_oid zorunludur.")
    oid = _validate_merchant_oid(merchant_oid)
    # Test OID: Google Ads / Tag Assistant testi için, veritabanına bakmadan hemen kontrollü yanıt döndür.
    # test123 veya test123_<suffix> (örn. test123_1, test123_1734567890) — benzersiz OID ile ilk açılışta her seferinde conversion fire edilir.
    if oid == "test123" or (oid.startswith("test123_") and len(oid) <= 64):
        resp = {
            "merchant_oid": oid,
            "status": "paid",
            "is_premium_active": True,
            "plan_code": "yearly",
            "total_amount_eur": 13.0,
            "currency": "EUR",
        }
        response = JSONResponse(content=resp)
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        return response
    stmt = select(PaymentOrder).where(PaymentOrder.merchant_oid == oid)
    order = db.exec(stmt).first()
    if not order:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı.")
    # Map backend "completed" -> "paid" for frontend contract
    status = order.status or "pending"
    status_out = "paid" if status == "completed" else status
    is_premium = status == "completed"
    plan_code = order.product if is_premium else None  # "single" | "monthly" | "yearly"
    total_eur = round((order.amount_kurus or 0) / 100.0, 2)
    resp = {
        "merchant_oid": order.merchant_oid,
        "status": status_out,
        "is_premium_active": is_premium,
        "plan_code": plan_code,
        "total_amount_eur": total_eur,
        "currency": getattr(order, "currency", None) or "EUR",
    }
    if getattr(order, "customer_email", None):
        resp["customer_email"] = order.customer_email
    # active_until not stored for now; optional for future subscription end
    response = JSONResponse(content=resp)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    return response


# Rapor doğrulama sayfası (QR ile açılır): /verify/{report_id}?token=...
VERIFY_LABELS: dict[str, dict[str, str]] = {
    "tr": {
        "title": "Rapor Doğrulama",
        "valid": "Geçerli",
        "invalid": "Geçersiz",
        "authentic_title": "Orijinal ve doğrulanmış rapor",
        "authentic_desc": "Bu rapor Norya tarafından üretilmiş orijinal rapordur. QR kod ile doğruluğu ve orijinalliği teyit edilmiştir.",
        "report_id": "Rapor No",
        "created_at": "Oluşturulma Tarihi",
        "language": "Dil",
        "package_type": "Paket Tipi",
        "verification_code": "Doğrulama Kodu",
        "disclaimer": "Bu sayfa rapor doğrulama amaçlıdır. Hassas sağlık verisi paylaşılmaz.",
        "summary_score": "Genel Skor",
        "critical_count": "Kritik Bulgu",
        "invalid_message": "Bu rapor doğrulanamadı. Linkin doğru olduğundan veya raporun hâlâ geçerli olduğundan emin olun.",
        "brand": "Norya",
        "brand_sub": "Kan Tahlili Analiz Raporu Doğrulama",
    },
    "en": {
        "title": "Report Verification",
        "valid": "Valid",
        "invalid": "Invalid",
        "authentic_title": "Authentic and verified report",
        "authentic_desc": "This report is an original Norya report. Its authenticity and originality have been confirmed via QR code verification.",
        "report_id": "Report ID",
        "created_at": "Created",
        "language": "Language",
        "package_type": "Package",
        "verification_code": "Verification Code",
        "disclaimer": "This page is for report verification only. No sensitive health data is shared.",
        "summary_score": "Overall Score",
        "critical_count": "Critical Findings",
        "invalid_message": "This report could not be verified. Please check that the link is correct and the report is still valid.",
        "brand": "Norya",
        "brand_sub": "Blood Test Report Verification",
    },
}


@app.get("/verify/{report_id}", response_class=HTMLResponse)
def verify_report_page(
    request: Request,
    report_id: str,
    token: str | None = Query(None, description="Signed verification token from QR"),
    db: Session = Depends(get_db),
):
    """QR ile açılan premium doğrulama sayfası. Geçerli/geçersiz durumu ve sınırlı özet gösterilir."""
    from app.services.report_pdf import parse_report_to_context

    lang = (request.query_params.get("lang") or request.headers.get("accept-language", "en")[:2] or "en").lower()
    if lang not in VERIFY_LABELS:
        lang = "en"
    labels = VERIFY_LABELS.get(lang, VERIFY_LABELS["en"])

    rec = db.exec(select(ReportVerification).where(ReportVerification.report_id == report_id)).first()
    valid = False
    created_at_str = ""
    package_type_display = ""
    verification_code = ""
    summary_score: int | None = None
    summary_critical_count: int | None = None

    if rec and rec.is_active and token:
        if verify_report_verification_token(rec.report_id, rec.verification_code, token):
            valid = True
            created_at_str = rec.created_at.strftime("%d.%m.%Y %H:%M") if hasattr(rec.created_at, "strftime") else str(rec.created_at)
            package_type_display = {"single": "Tek Analiz" if lang == "tr" else "Single Analysis", "monthly": "Aylık Abonelik" if lang == "tr" else "Monthly", "yearly": "Yıllık Abonelik" if lang == "tr" else "Yearly"}.get(rec.package_type, rec.package_type)
            verification_code = rec.verification_code or ""
            analysis_rec = db.get(AnalysisRecord, rec.analysis_id)
            if analysis_rec and getattr(analysis_rec, "result_text", None):
                try:
                    ctx = parse_report_to_context(analysis_rec.result_text or "", lang=rec.language or "tr")
                    summary_score = ctx.get("overall_score")
                    if summary_score is None:
                        summary_score = 100
                    findings = ctx.get("findings") or []
                    summary_critical_count = len([f for f in findings if f])
                except Exception:
                    pass

    base_url = str(request.base_url).rstrip("/")
    return templates.TemplateResponse(
        "verify.html",
        {
            "request": request,
            "valid": valid,
            "report_id": report_id,
            "created_at": created_at_str,
            "language": (rec.language if rec and valid else None) or lang,
            "package_type": package_type_display,
            "verification_code": verification_code,
            "labels": labels,
            "summary_score": summary_score,
            "summary_critical_count": summary_critical_count,
            "canonical_url": f"{base_url}/verify/{report_id}",
        },
    )


@app.get("/pay", response_class=HTMLResponse)
def pay_page(
    request: Request,
    plan: str = Query("single_13eur", description="Plan: single_13eur, monthly_50eur, yearly_99eur"),
    lang: str = Query("tr", description="Language: tr, en, de, fr, it, es"),
    db: Session = Depends(get_db),
):
    """Ödeme sayfası: plan seçili; /paytr/init ile token alınıp PayTR iFrame gösterilir. Tüm dillerde ve mobil uyumlu."""
    plan_code = (plan or "single_13eur").strip().lower()
    plan_map = get_plan_code_to_product_cents(db)
    if plan_code not in plan_map:
        plan_code = "single_13eur"
    lang = (lang or "tr").lower()[:2]
    if lang not in ("tr", "en", "de", "fr", "it", "es"):
        lang = "tr"
    t = get_pay_ui(lang)
    plan_display = get_plan_display_name(plan_code, lang)
    benefits = get_plan_benefits(plan_code, lang)
    base_url = str(request.base_url).rstrip("/")
    prices = {code: f"{cents / 100:.2f}" for code, (_, cents) in plan_map.items()}
    prices_cents = {code: cents for code, (_, cents) in plan_map.items()}
    benefits_monthly = get_plan_benefits("monthly_50eur", lang)
    benefits_yearly = get_plan_benefits("yearly_99eur", lang)
    # Bar’da kampanya görünsün: önce seçilen plan, yoksa herhangi bir planda aktif kampanya (featured)
    campaign_raw = None
    try:
        campaign_raw = get_active_campaign_for_checkout(db, plan_code, plan_code_to_amount=plan_map)
        if campaign_raw is None:
            for fallback_plan in ("yearly_99eur", "monthly_50eur", "single_13eur"):
                if fallback_plan == plan_code:
                    continue
                campaign_raw = get_active_campaign_for_checkout(db, fallback_plan, plan_code_to_amount=plan_map)
                if campaign_raw is not None:
                    break
    except Exception as e:
        log.warning("pay_page campaign fetch failed: %s", e)
    campaign_config = _payment_campaign_config(campaign_raw, t)
    resp = templates.TemplateResponse(
        "pay.html",
        {
            "request": request,
            "brand": BRAND_NAME,
            "plan_code": plan_code,
            "plan_code_js": json.dumps(plan_code),
            "lang": lang,
            "t": t,
            "t_js": json.dumps(t),
            "plan_display": plan_display,
            "base_url": base_url,
            "prices": prices,
            "prices_js": json.dumps(prices),
            "prices_cents_js": json.dumps(prices_cents),
            "benefits": benefits,
            "benefits_js": json.dumps(benefits),
            "benefits_monthly_js": json.dumps(benefits_monthly),
            "benefits_yearly_js": json.dumps(benefits_yearly),
            "campaign_config": campaign_config,
            "campaign_js": json.dumps(campaign_config),
        },
    )
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return resp


def _payment_campaign_config(campaign: dict | None, t: dict) -> dict:
    """Build frontend campaign config from admin campaign data. Extensible shape.
    discountValue her zaman int döner ki bar/ödeme sayfasında indirim oranı görünsün."""
    if not campaign:
        return {
            "campaignActive": False,
            "campaignTitle": "",
            "campaignMessage": "",
            "campaignBadge": "",
            "discountType": "",
            "discountValue": 0,
            "applicablePlans": "",
            "promoCode": "",
            "autoApply": False,
        }
    raw_value = campaign.get("discount_value")
    discount_value_int = int(raw_value) if raw_value is not None else 0
    display_label = (campaign.get("display_label") or "").strip()
    badge = (campaign.get("campaign_badge") or "").strip()
    return {
        "campaignActive": True,
        "campaignTitle": display_label or t.get("offer_annual_text", "Annual plan includes 15 extra analyses + 2 bonus months value."),
        "campaignMessage": (campaign.get("display_note") or "").strip() or t.get("offer_best_savings_pill", "Best savings"),
        "campaignBadge": badge or t.get("offer_limited_badge", "Limited Offer"),
        "discountType": campaign.get("discount_type") or "percent",
        "discountValue": discount_value_int,
        "applicablePlans": (campaign.get("products") or "").strip() or "",
        "promoCode": (campaign.get("code") or "").strip() or "",
        "autoApply": campaign.get("auto_apply", False),
    }


@app.get("/payment", response_class=HTMLResponse)
def payment_page_premium(
    request: Request,
    lang: str | None = Query(None, description="Dil override; yoksa tarayıcı diline göre otomatik"),
    current_user: User | None = Depends(get_current_user_optional),
    db: Session = Depends(get_db),
):
    """Premium Payment Page: 3 plan cards, PayTR iFrame embed. Kampanya admin’deki aktif kampanyaya bağlı."""
    lang = _payment_lang_from_request(request)
    t = get_pay_ui(lang)
    # Canonical domain (linkler, meta); API çağrıları için mevcut origin (localhost'ta CSP 'self' uyumu)
    base_url = _paytr_canonical_base(request)
    api_base = str(request.base_url).rstrip("/")
    plan_map = get_plan_code_to_product_cents(db)
    plans: list[dict] = []
    for code, (product, price_cents) in plan_map.items():
        plans.append(
            {
                "code": code,
                "price": f"{price_cents / 100:.2f}",
                "price_cents": price_cents,
                "label_key": f"plan_{product}",
                "product": product,
                "best_value": product == "yearly",
            }
        )
    _card_label_keys = {"single": "plan_card_single", "monthly": "plan_card_monthly", "yearly": "plan_card_yearly"}
    for p in plans:
        p["label"] = t.get(p["label_key"], p["code"])
        p["display_label"] = t.get(_card_label_keys.get(p["product"], p["label_key"]), p["label"])
        p["benefits"] = get_plan_benefits(p["product"], lang)
    user_logged_in = current_user is not None
    user_email = (current_user.email or "").strip() if current_user else ""
    user_name = (getattr(current_user, "full_name", None) or "").strip() if current_user else ""
    default_plan = next((p for p in plans if p.get("product") == "yearly"), plans[0] if plans else None)

    # Eski checkout şablonuyla uyum için: plan_code / prices / benefits_* değişkenleri
    prices = {code: f"{price_cents / 100:.2f}" for code, (product, price_cents) in plan_map.items()}
    prices_cents = {code: price_cents for code, (product, price_cents) in plan_map.items()}
    benefits_single = next((p["benefits"] for p in plans if p["product"] == "single"), [])
    benefits_monthly = next((p["benefits"] for p in plans if p["product"] == "monthly"), [])
    benefits_yearly = next((p["benefits"] for p in plans if p["product"] == "yearly"), [])
    plan_code = (default_plan or plans[0])["code"] if plans else "single_13eur"
    campaign_raw = None
    if default_plan:
        try:
            campaign_raw = get_active_campaign_for_checkout(db, default_plan["code"], plan_code_to_amount=plan_map)
        except Exception as e:
            log.warning("payment_page campaign fetch failed: %s", e)
    campaign_config = _payment_campaign_config(campaign_raw, t)
    resp = templates.TemplateResponse(
        "payment_page.html",
        {
            "request": request,
            "brand": BRAND_NAME,
            "lang": lang,
            "t": t,
            "t_js": json.dumps(t),
            "base_url": base_url,
            "plans": plans,
            "plans_js": json.dumps(plans),
            "base_url_js": json.dumps(api_base),
            "default_plan": default_plan,
            # Eski template alanları (plan_code + fiyat/benefit map'leri)
            "plan_code": plan_code,
            "plan_code_js": json.dumps(plan_code),
            "prices": prices,
            "prices_js": json.dumps(prices),
            "prices_cents_js": json.dumps(prices_cents),
            "benefits": benefits_single,
            "benefits_js": json.dumps(benefits_single),
            "benefits_monthly_js": json.dumps(benefits_monthly),
            "benefits_yearly_js": json.dumps(benefits_yearly),
            "campaign_config": campaign_config,
            "campaign_js": json.dumps(campaign_config),
            "user_logged_in": user_logged_in,
            "user_email": user_email,
            "user_name": user_name,
        },
    )
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return resp


@app.get("/api/coupon/validate")
def coupon_validate(
    code: str,
    product: str | None = None,
    plan_code: str | None = None,
    db: Session = Depends(get_db),
):
    """İndirim kodunu doğrular; geçerliyse indirim tutarı ve son fiyat döner. plan_code verilirse tutar merkezi fiyattan hesaplanır."""
    if plan_code:
        try:
            product, base = _plan_code_to_product_amount(plan_code, db)
        except ValueError:
            raise HTTPException(status_code=400, detail="Geçersiz plan_code.")
    elif product and product in ("single", "monthly", "yearly"):
        base = _paytr_amount(product, db)
    else:
        raise HTTPException(status_code=400, detail="product veya plan_code gerekli.")
    discount, err = validate_coupon(db, code, product, base)
    if err:
        return {"valid": False, "reason": err}
    discount_euro = discount / 100.0
    return {
        "valid": True,
        "discount_cents": discount,
        "discount": round(discount_euro, 2),
        "discount_formatted": f"-{discount_euro:.2f} €",
        "final_amount_cents": max(1, base - discount),
    }


# Kampanya API'leri: canlıda indirim güncellenince hemen görünsün diye önbelleklenmez
_CAMPAIGN_NO_CACHE_HEADERS = {
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "Pragma": "no-cache",
    "Expires": "0",
}


@app.get("/api/campaigns/active")
def campaigns_active(
    plan_code: str,
    lang: str = Query("tr", description="Language for campaign labels"),
    db: Session = Depends(get_db),
):
    """Seçilen plan için checkout’ta gösterilecek aktif kampanyayı döner. Aynı campaign_config yapısı."""
    try:
        campaign_raw = get_active_campaign_for_checkout(db, plan_code)
    except Exception as e:
        log.warning("campaigns/active failed for plan_code=%s: %s", plan_code, e)
        out = {"active": False, "campaign": _payment_campaign_config(None, get_pay_ui(lang or "tr"))}
        return JSONResponse(content=out, headers=_CAMPAIGN_NO_CACHE_HEADERS)
    t = get_pay_ui((lang or "tr").lower()[:2])
    campaign_config = _payment_campaign_config(campaign_raw, t)
    return JSONResponse(
        content={"active": campaign_config["campaignActive"], "campaign": campaign_config},
        headers=_CAMPAIGN_NO_CACHE_HEADERS,
    )


@app.get("/api/campaigns/featured")
def campaigns_featured(
    lang: str = Query("tr", description="Language for campaign labels"),
    db: Session = Depends(get_db),
):
    """Anasayfa / odeme linki icin tek bir aktif kampanya doner (yillik plan oncelikli). Merkezi fiyat kullanilir."""
    t = get_pay_ui((lang or "tr").lower()[:2])
    plan_map = get_plan_code_to_product_cents(db)
    for plan_code in ("yearly_99eur", "monthly_50eur", "single_13eur"):
        try:
            campaign_raw = get_active_campaign_for_checkout(db, plan_code, plan_code_to_amount=plan_map)
            if campaign_raw:
                cfg = _payment_campaign_config(campaign_raw, t)
                return JSONResponse(
                    content={"active": True, "campaign": cfg},
                    headers=_CAMPAIGN_NO_CACHE_HEADERS,
                )
        except Exception:
            continue
    return JSONResponse(
        content={"active": False, "campaign": _payment_campaign_config(None, t)},
        headers=_CAMPAIGN_NO_CACHE_HEADERS,
    )


@app.post("/payment/get-token")
def payment_get_token(
    body: CreateSessionRequest,
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """PayTR iFrame token döner; frontend bu token ile iframe açar. Ödeme sonrası bildirim URL'ye POST gelir."""
    if not _paytr_enabled():
        raise HTTPException(status_code=503, detail="Ödeme şu an aktif değil. PayTR ayarlarını kontrol edin.")
    if not (body.consent_mesafeli and body.consent_kvkk):
        raise HTTPException(
            status_code=400,
            detail="Mesafeli Satış Sözleşmesi ve Gizlilik/KVKK politikasını kabul etmeniz gerekiyor.",
        )
    if body.product not in ("single", "monthly", "yearly"):
        raise HTTPException(status_code=400, detail="Geçersiz ürün.")
    import base64
    import hmac
    import hashlib
    import json
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request as UrlRequest

    merchant_oid = f"norya{user.id}{int(datetime.now(timezone.utc).timestamp())}{secrets.token_hex(4)}"
    amount = _paytr_amount(body.product, db)
    coupon_used: str | None = None
    if body.coupon_code and (code := (body.coupon_code or "").strip()):
        discount, err = validate_coupon(db, code, body.product, amount)
        if err:
            raise HTTPException(status_code=400, detail=err)
        amount = max(1, amount - discount)
        coupon_used = code
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"
    order = PaymentOrder(
        merchant_oid=merchant_oid,
        user_id=user.id or 0,
        customer_email=(user.email or "").strip().lower() or None,
        product=body.product,
        amount_kurus=amount,
        currency=currency,
        coupon_code_used=coupon_used,
    )
    db.add(order)
    db.commit()
    _audit(db, "payment_consent", user.id, _client_ip(request))

    paytr_amount, paytr_currency = _paytr_amount_and_currency(amount)
    merchant_id = settings.paytr_merchant_id
    merchant_key = settings.paytr_merchant_key.encode() if isinstance(settings.paytr_merchant_key, str) else settings.paytr_merchant_key
    merchant_salt = settings.paytr_merchant_salt
    user_ip = _client_ip(request)
    email = user.email or ""
    product_name = {"single": "1 Analiz", "monthly": "Pro Aylık", "yearly": "Pro Yıllık"}[body.product]
    basket_amount_str = f"{paytr_amount / 100:.2f}" if paytr_currency == "TL" else f"{amount / 100:.2f}"
    user_basket = base64.b64encode(
        json.dumps([[product_name, basket_amount_str, 1]]).encode()
    ).decode()
    no_installment = "0"
    max_installment = "0"
    test_mode = getattr(settings, "paytr_test_mode", "0") or "0"

    hash_str = f"{merchant_id}{user_ip}{merchant_oid}{email}{paytr_amount}{user_basket}{no_installment}{max_installment}{paytr_currency}{test_mode}"
    paytr_token = base64.b64encode(
        hmac.new(merchant_key, (hash_str + merchant_salt).encode(), hashlib.sha256).digest()
    ).decode()

    base_url = _paytr_canonical_base(request)
    return_lang = _payment_lang_from_request(request) or "tr"
    ok_url = f"{base_url}/payment/success?merchant_oid={merchant_oid}&lang={return_lang}"
    fail_url = f"{base_url}/payment/failed?merchant_oid={merchant_oid}&lang={return_lang}"

    post_vals = {
        "merchant_id": merchant_id,
        "user_ip": user_ip,
        "merchant_oid": merchant_oid,
        "email": email,
        "payment_amount": paytr_amount,
        "paytr_token": paytr_token,
        "user_basket": user_basket,
        "debug_on": "0",
        "no_installment": no_installment,
        "max_installment": max_installment,
        "user_name": (user.full_name or "")[:60],
        "user_address": "Norya ödeme",
        "user_phone": (getattr(user, "phone", None) or "").strip() or "05551234567",
        "merchant_ok_url": ok_url,
        "merchant_fail_url": fail_url,
        "timeout_limit": "30",
        "currency": paytr_currency,
        "test_mode": test_mode,
    }
    try:
        req = UrlRequest(
            "https://www.paytr.com/odeme/api/get-token",
            data=urlencode(post_vals).encode(),
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        with urlopen(req, timeout=20) as resp:
            result = json.loads(resp.read().decode())
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"PayTR bağlantı hatası: {str(e)[:80]}")

    if result.get("status") != "success":
        raise HTTPException(status_code=400, detail=_paytr_reason_to_detail(result.get("reason")))
    token = result.get("token", "")
    return {"token": token, "iframe_url": f"https://www.paytr.com/odeme/guvenli/{token}", "merchant_oid": merchant_oid}


@app.post("/payment/get-token-guest")
def payment_get_token_guest(
    body: GuestSessionRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    """Kayıt olmadan sadece tek analiz ödemesi. E-posta ile kullanıcı oluşturulur veya mevcut kullanıcıya bağlanır; ödeme sonrası guest_token ile oturum açılır."""
    if not _paytr_enabled():
        raise HTTPException(status_code=503, detail="Ödeme şu an aktif değil. PayTR ayarlarını kontrol edin.")
    if not (body.consent_mesafeli and body.consent_kvkk):
        raise HTTPException(
            status_code=400,
            detail="Mesafeli Satış Sözleşmesi ve Gizlilik/KVKK politikasını kabul etmeniz gerekiyor.",
        )
    if body.product != "single":
        raise HTTPException(status_code=400, detail="Misafir ödeme sadece tek analiz için geçerlidir.")
    email = (body.email or "").strip().lower()
    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail="Geçerli bir e-posta adresi girin.")
    stmt = select(User).where(User.email == email)
    user = db.exec(stmt).first()
    if not user:
        user = User(
            email=email,
            hashed_password=hash_password("guest_" + secrets.token_hex(32)),
            full_name=(body.full_name or "").strip()[:200] or "",
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    user_id = user.id or 0
    merchant_oid = f"noryag{user_id}{int(datetime.now(timezone.utc).timestamp())}{secrets.token_hex(4)}"
    amount = _paytr_amount("single", db)
    coupon_used: str | None = None
    if body.coupon_code and (code := (body.coupon_code or "").strip()):
        discount, err = validate_coupon(db, code, "single", amount)
        if err:
            raise HTTPException(status_code=400, detail=err)
        amount = max(1, amount - discount)
        coupon_used = code
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"
    order = PaymentOrder(
        merchant_oid=merchant_oid,
        user_id=user_id,
        customer_email=email or None,
        product="single",
        amount_kurus=amount,
        currency=currency,
        coupon_code_used=coupon_used,
    )
    db.add(order)
    guest_token = secrets.token_hex(32)
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    guest_login = GuestLoginToken(token=guest_token, user_id=user_id, expires_at=expires_at)
    db.add(guest_login)
    db.commit()
    _audit(db, "payment_consent", user_id, _client_ip(request))

    paytr_amount, paytr_currency = _paytr_amount_and_currency(amount)
    import base64
    import hmac
    import hashlib
    import json
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request as UrlRequest

    merchant_id = settings.paytr_merchant_id
    merchant_key = settings.paytr_merchant_key.encode() if isinstance(settings.paytr_merchant_key, str) else settings.paytr_merchant_key
    merchant_salt = settings.paytr_merchant_salt
    user_ip = _client_ip(request)
    product_name = "1 Analiz"
    basket_amount_str = f"{paytr_amount / 100:.2f}" if paytr_currency == "TL" else f"{amount / 100:.2f}"
    user_basket = base64.b64encode(json.dumps([[product_name, basket_amount_str, 1]]).encode()).decode()
    no_installment = "0"
    max_installment = "0"
    test_mode = getattr(settings, "paytr_test_mode", "0") or "0"
    hash_str = f"{merchant_id}{user_ip}{merchant_oid}{email}{paytr_amount}{user_basket}{no_installment}{max_installment}{paytr_currency}{test_mode}"
    paytr_token = base64.b64encode(
        hmac.new(merchant_key, (hash_str + merchant_salt).encode(), hashlib.sha256).digest()
    ).decode()
    base_url = _paytr_canonical_base(request)
    return_lang = _payment_lang_from_request(request) or "tr"
    merchant_ok_url = f"{base_url}/payment/success?merchant_oid={merchant_oid}&lang={return_lang}&guest_token={guest_token}"
    merchant_fail_url = f"{base_url}/payment/failed?lang={return_lang}"
    post_vals = {
        "merchant_id": merchant_id,
        "user_ip": user_ip,
        "merchant_oid": merchant_oid,
        "email": email,
        "payment_amount": paytr_amount,
        "paytr_token": paytr_token,
        "user_basket": user_basket,
        "debug_on": "0",
        "no_installment": no_installment,
        "max_installment": max_installment,
        "user_name": ((body.full_name or "").strip() or "")[:60],
        "user_address": "Norya ödeme",
        "user_phone": "05551234567",
        "merchant_ok_url": merchant_ok_url,
        "merchant_fail_url": merchant_fail_url,
        "timeout_limit": "30",
        "currency": paytr_currency,
        "test_mode": test_mode,
    }
    try:
        req = UrlRequest(
            "https://www.paytr.com/odeme/api/get-token",
            data=urlencode(post_vals).encode(),
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        with urlopen(req, timeout=20) as resp:
            result = json.loads(resp.read().decode())
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"PayTR bağlantı hatası: {str(e)[:80]}")
    if result.get("status") != "success":
        raise HTTPException(status_code=400, detail=_paytr_reason_to_detail(result.get("reason")))
    token = result.get("token", "")
    return {"iframe_url": f"https://www.paytr.com/odeme/guvenli/{token}", "merchant_oid": merchant_oid}


async def _paytr_callback_handle(request: Request, db: Session):
    """PayTR bildirim işlemi. Her zaman 200 OK dönülür (PayTR tekrar denemesin)."""
    form = await request.form()
    post = {k: (form.get(k) or "") for k in form}
    merchant_oid = post.get("merchant_oid", "")
    status = post.get("status", "")
    total_amount = post.get("total_amount", "")
    payment_amount = post.get("payment_amount", "")
    paytr_hash = post.get("hash", "")
    transaction_id = post.get("payment_id") or post.get("transaction_id") or ""

    # Gözlemlenebilirlik: callback gelen tüm key'ler ve kritik alanlar loglanır
    log.info(
        "PAYTR_CALLBACK: merchant_oid=%s status=%s total_amount=%s payment_amount=%s keys=%s",
        merchant_oid, status, total_amount, payment_amount, list(post.keys()),
    )

    if not merchant_oid or not status or not total_amount or not paytr_hash:
        return PlainTextResponse("OK", status_code=200)

    merchant_key = (settings.paytr_merchant_key or "").strip()
    merchant_salt = (settings.paytr_merchant_salt or "").strip()
    hash_ok = False
    if merchant_key and merchant_salt:
        import base64
        import hmac
        import hashlib
        key_bytes = merchant_key.encode() if isinstance(merchant_key, str) else merchant_key
        hash_str = f"{merchant_oid}{merchant_salt}{status}{total_amount}"
        our_hash = base64.b64encode(
            hmac.new(key_bytes, hash_str.encode(), hashlib.sha256).digest()
        ).decode()
        hash_ok = our_hash == paytr_hash

    log.info("PAYTR_CALLBACK: merchant_oid=%s status=%s total_amount=%s payment_amount=%s hash_ok=%s", merchant_oid, status, total_amount, payment_amount, hash_ok)

    if not merchant_key or not merchant_salt:
        log.warning("PayTR callback: PAYTR_MERCHANT_KEY veya PAYTR_MERCHANT_SALT eksik.")
        try:
            db.add(
                SecurityLog(
                    event="paytr_invalid_hash",
                    ip=_client_ip(request),
                    endpoint="/paytr/callback",
                    detail="missing_merchant_key_or_salt",
                )
            )
            db.commit()
        except Exception as e:
            log.warning("SecurityLog write failed: %s", e)
        return PlainTextResponse("OK", status_code=200)

    if not hash_ok:
        try:
            db.add(
                SecurityLog(
                    event="paytr_invalid_hash",
                    ip=_client_ip(request),
                    endpoint="/paytr/callback",
                    detail=f"merchant_oid={merchant_oid} status={status} total_amount={total_amount}",
                )
            )
            db.commit()
        except Exception as e:
            log.warning("SecurityLog write failed: %s", e)
        return PlainTextResponse("OK", status_code=200)

    # Önce transaction_id (varsa), yoksa merchant_oid ile siparişi bul
    order = None
    if transaction_id:
        order = db.exec(
            select(PaymentOrder).where(PaymentOrder.paytr_transaction_id == transaction_id)
        ).first()
    if not order:
        order = db.exec(
            select(PaymentOrder).where(PaymentOrder.merchant_oid == merchant_oid)
        ).first()

    if not order:
        # Sipariş bulunamadıysa güvenlik loguna yaz, 200 dön (PayTR tekrar denemesin)
        try:
            db.add(
                SecurityLog(
                    event="suspicious",
                    user_id=None,
                    ip=_client_ip(request),
                    endpoint="/payment/callback",
                    detail=f"unknown_order: merchant_oid={merchant_oid} tx={transaction_id}",
                )
            )
            db.commit()
        except Exception as e:
            log.warning("SecurityLog write failed for missing order: %s", e)
        return PlainTextResponse("OK", status_code=200)

    # Idempotent: sipariş zaten işlendi ise hiçbir şey yapmadan OK dön
    if getattr(order, "is_processed", False):
        return PlainTextResponse("OK", status_code=200)

    try:
        raw_json = json.dumps({k: str(v) for k, v in post.items()})[:4000]
        if hasattr(order, "raw_callback_json"):
            order.raw_callback_json = raw_json
        if hasattr(order, "paytr_status"):
            order.paytr_status = status
        if hasattr(order, "paytr_payment_amount"):
            order.paytr_payment_amount = str(payment_amount) if payment_amount else None

        if (status or "").strip().lower() == "success":
            user = db.get(User, order.user_id)
            if user:
                qty = getattr(order, "quantity", 1) or 1
                if order.product == "single":
                    user.extra_credits = (getattr(user, "extra_credits", 0) or 0) + qty
                    db.add(user)
                elif order.product in ("monthly", "yearly"):
                    user.plan = "pro"
                    db.add(user)
                _audit(db, f"payment_{order.product}", order.user_id, None)
            order.status = "completed"
            order.is_processed = True
            order.processed_at = datetime.now(timezone.utc)
            if hasattr(order, "paid_at"):
                order.paid_at = datetime.now(timezone.utc)
            if transaction_id and not order.paytr_transaction_id:
                order.paytr_transaction_id = transaction_id
            db.add(order)
            if getattr(order, "coupon_code_used", None):
                apply_coupon_use(db, order.coupon_code_used)
        else:
            order.status = "failed"
            if transaction_id and not order.paytr_transaction_id:
                order.paytr_transaction_id = transaction_id
            db.add(order)
        db.commit()
    except Exception as e:
        log.error("PayTR callback failed: merchant_oid=%s, error=%s", merchant_oid, str(e))
        try:
            _audit(db, "payment_callback_error", None, str(merchant_oid)[:64])
        except Exception:
            pass
        return PlainTextResponse("OK", status_code=200)
    return PlainTextResponse("OK", status_code=200)


@app.get("/payment/success", response_class=HTMLResponse)
def payment_success_page(
    request: Request,
    lang: str = Query("tr", description="Language: tr, en, de, fr, it, es"),
    merchant_oid: str = Query("", description="Sipariş merchant_oid (PayTR yönlendirmesinde eklenir)"),
    guest_token: str = Query("", description="Misafir ödeme sonrası oturum için token"),
    verify_tag: str = Query("", description="1 ise sadece tag doğrulama; conversion tetiklenmez"),
):
    """Başarılı ödeme sonrası sayfa. merchant_oid varsa polling ile premium aktivasyonu beklenir.
    Global tag (AW-18004536281) her zaman yüklenir; conversion sadece API paid/premium_active + gerçek transaction_id ile."""
    base = _paytr_canonical_base(request)
    # API polling aynı origin'e gitsin (localhost'ta CSP engeli olmasın; production'da da same-origin)
    api_base = str(request.base_url).rstrip("/")
    lang = (lang or "tr").lower()[:2]
    if lang not in ("tr", "en", "de", "fr", "it", "es"):
        lang = "tr"
    t = get_pay_ui(lang)
    title = t["success_title"]
    msg = t["success_message"]
    btn_text = t["success_btn"]
    updating = t.get("success_updating", "Hesabınız güncelleniyor…")
    premium_active = t.get("success_premium_active", "Premium aktif")
    success_access_ready = t.get("success_access_ready", "Erişiminiz hazır.")
    success_linked_to_email = t.get("success_linked_to_email", "Rapor ve üyelik şu adrese bağlandı:")
    success_create_account_cta = t.get("success_create_account_cta", "İsterseniz şifre oluşturarak hesabınızı tamamlayabilirsiniz.")
    success_go_to_report = t.get("success_go_to_report", "Raporuma git")
    success_create_account = t.get("success_create_account", "Hesap oluştur")
    pending_bank = t.get("success_pending_bank", "İşlem bankanızdan onay bekliyor olabilir.")
    failed_short = t.get("success_payment_failed_short", "Ödeme tamamlanamadı.")
    btn_report = t.get("success_btn_report", "Rapor sayfasına git")
    check_done_btn = t.get("success_check_done_btn", "Ödeme tamamlandı mı?")
    retry_text = t.get("failed_retry", "Tekrar dene")
    invalid_oid_msg = t.get("success_invalid_oid", "Sipariş bilgisi alınamadı veya geçersiz. Rapor sayfasına gidebilirsiniz.")

    # Global tag her zaman aynı şekilde yüklensin (merchant_oid olsa da olmasa da)
    aw_id = (getattr(settings, "google_ads_conversion_id", "") or "").strip() or GOOGLE_ADS_GLOBAL_TAG_ID
    gtag_script = (
        f'<script async src="https://www.googletagmanager.com/gtag/js?id={aw_id}"></script>'
        f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{aw_id}");</script>'
    )
    is_verify_tag = (verify_tag or "").strip() == "1"
    data_verify_val = "1" if is_verify_tag else ""

    if not (merchant_oid and merchant_oid.strip()):
        # merchant_oid yok: yine de global tag yüklü; verify_tag=1 ise konsola gtag/dataLayer durumu yazılır
        verify_script = ""
        if is_verify_tag:
            verify_script = f"""  <script>
(function(){{
  try {{
    var gtagDefined = typeof window.gtag === "function";
    var dl = window.dataLayer || [];
    console.log("[Norya verify_tag] gtag defined:", gtagDefined, "dataLayer length:", dl.length, "AW id:", {json.dumps(aw_id)});
  }} catch(e) {{ console.warn("[Norya verify_tag]", e); }}
}})();
  </script>"""
        html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><meta name="theme-color" content="#0f172a">
{gtag_script}
<title>{title} – {BRAND_NAME}</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 0; padding: max(16px, env(safe-area-inset-top)); padding-bottom: max(24px, env(safe-area-inset-bottom)); background: linear-gradient(165deg, #0c1222 0%, #0f172a 50%); color: #e2e8f0; min-height: 100vh; min-height: 100dvh; display: flex; align-items: center; justify-content: center; -webkit-tap-highlight-color: transparent; }}
  .card {{ background: linear-gradient(180deg, rgba(30,41,59,0.95), rgba(15,23,42,0.98)); border: 1px solid rgba(14,165,164,0.2); border-radius: 20px; padding: clamp(24px, 5vw, 40px); max-width: 420px; width: 100%; margin: 0 16px; text-align: center; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.35); }}
  .ok {{ width: 56px; height: 56px; margin: 0 auto 20px; background: linear-gradient(135deg, #0EA5A4, #14b8a6); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; box-shadow: 0 0 30px rgba(14,165,164,0.35); }}
  h1 {{ color: #f1f5f9; font-size: clamp(1.25rem, 4vw, 1.5rem); margin-bottom: 10px; font-weight: 700; }}
  p {{ color: #94a3b8; margin-bottom: 28px; font-size: clamp(0.9rem, 2.5vw, 0.95rem); line-height: 1.5; }}
  a {{ display: inline-block; background: linear-gradient(135deg, #0EA5A4, #0d9488); color: #fff; padding: 14px 28px; min-height: 48px; line-height: 20px; border-radius: 12px; text-decoration: none; font-weight: 600; box-shadow: 0 4px 14px rgba(14,165,164,0.35); transition: transform 0.15s, box-shadow 0.15s; touch-action: manipulation; }}
  a:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(14,165,164,0.4); }}
</style>
</head>
<body data-gtag-conversion-page="payment-success" data-verify-tag="{data_verify_val}">
{verify_script}
  <div class="card">
    <div class="ok">✓</div>
    <h1>{title}</h1>
    <p>{msg}</p>
    <a href="{base}/#analyze">{btn_text}</a>
  </div>
</body>
</html>"""
        return HTMLResponse(html)

    oid = merchant_oid.strip()
    log.info(
        "PAYMENT_SUCCESS_PAGE: merchant_oid=%s guest_token=%s verify_tag=%s (conversion will fire client-side when order status=paid, unless verify_tag=1)",
        oid[:64],
        "yes" if (guest_token and guest_token.strip()) else "no",
        "1" if is_verify_tag else "0",
    )
    report_url = f"{base}/report"
    guest_token_js = json.dumps((guest_token or "").strip() or "")
    conv_label = (getattr(settings, "google_ads_conversion_label", "") or "").strip() or "RF4SCL78oIYcENnXnYlD"
    conversion_send_to = f"{aw_id}/{conv_label}"
    verify_tag_js = "true" if is_verify_tag else "false"
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><meta name="theme-color" content="#0f172a">
{gtag_script}
<title>{title} – {BRAND_NAME}</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 0; padding: max(16px, env(safe-area-inset-top)); padding-bottom: max(24px, env(safe-area-inset-bottom)); background: linear-gradient(165deg, #0c1222 0%, #0f172a 50%); color: #e2e8f0; min-height: 100vh; min-height: 100dvh; display: flex; align-items: center; justify-content: center; -webkit-tap-highlight-color: transparent; }}
  .card {{ background: linear-gradient(180deg, rgba(30,41,59,0.95), rgba(15,23,42,0.98)); border: 1px solid rgba(14,165,164,0.2); border-radius: 20px; padding: clamp(24px, 5vw, 40px); max-width: 420px; width: 100%; margin: 0 16px; text-align: center; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.35); }}
  .ok {{ width: 56px; height: 56px; margin: 0 auto 20px; background: linear-gradient(135deg, #0EA5A4, #14b8a6); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; box-shadow: 0 0 30px rgba(14,165,164,0.35); }}
  .spinner {{ width: 40px; height: 40px; margin: 0 auto 16px; border: 3px solid rgba(14,165,164,0.3); border-top-color: #0EA5A4; border-radius: 50%; animation: spin 0.8s linear infinite; }}
  @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  h1 {{ color: #f1f5f9; font-size: clamp(1.25rem, 4vw, 1.5rem); margin-bottom: 10px; font-weight: 700; }}
  #statusMsg {{ color: #94a3b8; margin-bottom: 28px; font-size: clamp(0.9rem, 2.5vw, 0.95rem); line-height: 1.5; }}
  .btns {{ display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; }}
  a, .btn {{ display: inline-block; background: linear-gradient(135deg, #0EA5A4, #0d9488); color: #fff; padding: 14px 28px; min-height: 48px; line-height: 20px; border-radius: 12px; text-decoration: none; font-weight: 600; box-shadow: 0 4px 14px rgba(14,165,164,0.35); transition: transform 0.15s; touch-action: manipulation; cursor: pointer; border: none; font-size: 1rem; }}
  a:hover, .btn:hover {{ transform: translateY(-2px); color: #fff; }}
  a.secondary {{ background: transparent; border: 2px solid #475569; color: #94a3b8; box-shadow: none; }}
  a.secondary:hover {{ border-color: #0EA5A4; color: #0EA5A4; }}
  .premium-done {{ color: #34d399; font-weight: 700; }}
</style>
</head>
<body data-gtag-conversion-page="payment-success" data-merchant-oid="{oid[:64]}">
  <!-- Conversion fires only when backend confirms paid via /api/orders/status (status=paid or is_premium_active). Not on page load. -->
  <div class="card">
    <div id="iconWrap" class="ok">✓</div>
    <div id="spinnerWrap" class="spinner" style="display:none;"></div>
    <h1 id="titleEl">{title}</h1>
    <p id="statusMsg">{updating}</p>
    <div id="btnWrap" class="btns" style="display:none;">
      <a id="btnReport" href="{report_url}">{success_go_to_report}</a>
      <a id="btnCreateAccount" href="{base}/?register=1" class="secondary" style="display:none;">{success_create_account}</a>
      <a id="btnRetry" class="secondary" href="{base}/payment?lang={lang}" style="display:none;">{retry_text}</a>
    </div>
    <p id="successLinkedEmail" style="display:none; margin-top:12px; font-size:0.875rem; color:#94a3b8;"></p>
    <p style="margin-top:16px;"><button type="button" class="btn secondary" id="checkDoneBtn" style="background:transparent;border:2px solid rgba(14,165,164,0.5);color:#94a3b8;">{check_done_btn}</button></p>
  </div>
  <script>
(function(){{
  // Sıra: (1) gtag head'de yüklü, (2) 500ms sonra polling, (3) API paid/premium_active gelince conversion (verify_tag=1 ise conversion atlanır)
  var apiBase = {json.dumps(api_base)};
  var oid = {json.dumps(oid)};
  var reportUrl = {json.dumps(report_url)};
  var guestToken = {guest_token_js};
  var baseUrl = {json.dumps(base)};
  var updating = {json.dumps(updating)};
  var premiumActive = {json.dumps(premium_active)};
  var successAccessReady = {json.dumps(success_access_ready)};
  var successLinkedToEmail = {json.dumps(success_linked_to_email)};
  var successCreateAccount = {json.dumps(success_create_account)};
  var pendingBank = {json.dumps(pending_bank)};
  var failedShort = {json.dumps(failed_short)};
  var invalidOidMsg = {json.dumps(invalid_oid_msg)};
  var conversionSendTo = {json.dumps(conversion_send_to)};
  var verifyTag = {verify_tag_js};
  var start = Date.now();
  var timeoutTotal = 90000;
  var intervalFast = 2000;
  var intervalSlow = 5000;
  var fastUntil = 30000;
  var pollTimer = null;
  var redirectTimer = null;
  var hasTimedOut = false;
  window.__noryaPaymentDebug = {{ orderId: oid, paymentStatus: null, callbackStatus: "polling", conversionTriggered: false, verifyTag: verifyTag, storageKey: "norya_conv_" + oid }};
  try {{ console.log("[Norya payment success] orderId=" + oid + ", guest_token=" + (guestToken ? "yes" : "no") + ", verify_tag=" + verifyTag); }} catch(e) {{}}
  if (oid === "test123" || (String(oid).indexOf("test123_") === 0)) {{
    try {{ console.log("[Norya] Test mode: use merchant_oid=test123_1 or test123_" + Date.now() + " for unique OID (fresh conversion fire every time, no sessionStorage). Or add ?conv_reset=1 to clear flag for " + oid); }} catch(e) {{}}
  }}
  if (typeof window.location !== "undefined" && window.location.search && window.location.search.indexOf("conv_reset=1") !== -1) {{
    try {{
      var resetKey = "norya_conv_" + oid;
      sessionStorage.removeItem(resetKey);
      window.__noryaPaymentDebug.convResetCleared = resetKey;
      console.log("[Norya] conv_reset=1: cleared sessionStorage key '" + resetKey + "'. Conversion will FIRE on this load if status=paid. (Remove ?conv_reset=1 for normal behaviour.)");
    }} catch(e) {{}}
  }}

  function showSpinner(show) {{
    document.getElementById("spinnerWrap").style.display = show ? "block" : "none";
    document.getElementById("iconWrap").style.display = show ? "none" : "flex";
  }}
  function setStatus(msg, isPremium) {{
    var el = document.getElementById("statusMsg");
    if (el) el.textContent = msg;
    if (isPremium) el && el.classList.add("premium-done");
  }}
  function showButtons(showReport, showRetry) {{
    var wrap = document.getElementById("btnWrap");
    var btnReport = document.getElementById("btnReport");
    var btnRetry = document.getElementById("btnRetry");
    if (wrap) wrap.style.display = "flex";
    if (btnReport) btnReport.style.display = showReport ? "inline-block" : "none";
    if (btnRetry) btnRetry.style.display = showRetry ? "inline-block" : "none";
  }}
  function stopPolling() {{
    if (pollTimer) {{ clearTimeout(pollTimer); pollTimer = null; }}
  }}
  function doPoll(isManual) {{
    var timeoutMsg = {json.dumps(t.get("success_timeout", "Zaman aşımı"))};
    var now = Date.now();
    var elapsed = now - start;
    if (elapsed > timeoutTotal && !isManual) {{
      if (!hasTimedOut) {{
        hasTimedOut = true;
        stopPolling();
        showSpinner(false);
        setStatus(updating + " (" + timeoutMsg + ")");
        showButtons(true, false);
        window.__noryaPaymentDebug.conversionNotFiredReason = "timeout";
        try {{ console.log("[Norya] Google Ads conversion NOT fired: timeout before paid (only paid orders trigger conversion)"); }} catch(e) {{}}
        try {{ console.log("[Norya payment success] payment status timeout (auto)"); }} catch(e) {{}}
      }}
      return;
    }}
    if (elapsed > timeoutTotal && isManual) {{
      try {{ console.log("[Norya payment success] manual recheck clicked (reset timeout window)"); }} catch(e) {{}}
      start = now;
      hasTimedOut = false;
    }}
    var statusUrl = apiBase + "/api/orders/status?merchant_oid=" + encodeURIComponent(oid);
    try {{ console.log("[Norya] orders status request sent", {{ url: statusUrl, orderId: oid }}); }} catch(e) {{}}
    try {{ console.log("[Norya] Network: look for GET request to url above (filter: 'orders/status' or 'merchant_oid')"); }} catch(e) {{}}
    fetch(statusUrl)
      .then(function(r) {{
        try {{ console.log("[Norya] orders status response received", {{ status: r.status, ok: r.ok, url: r.url }}); }} catch(e) {{}}
        if (r.status === 400 || r.status === 422) {{
          stopPolling();
          showSpinner(false);
          setStatus(invalidOidMsg);
          showButtons(true, false);
          return {{ __invalidOid: true }};
        }}
        return r.status === 404 ? null : r.json();
      }})
      .then(function(d) {{
        if (d && typeof d.status !== "undefined") {{
          try {{ console.log("[Norya] orders status response body", {{ status: d.status, merchant_oid: d.merchant_oid }}); }} catch(e) {{}}
        }}
        if (d && d.__invalidOid) {{
          window.__noryaPaymentDebug.conversionNotFiredReason = "invalid_merchant_oid";
          try {{ console.log("[Norya] Google Ads conversion NOT fired: invalid or missing merchant_oid"); }} catch(e) {{}}
          return;
        }}
        if (!d) {{ setStatus(updating); return; }}
        if (d.status === "paid" || d.is_premium_active) {{
          try {{ console.log("[Norya payment success] payment status=paid"); }} catch(e) {{}}
          stopPolling();
          showSpinner(false);
          setStatus(successAccessReady + " ✓", true);
          var linkedEl = document.getElementById("successLinkedEmail");
          var btnCreate = document.getElementById("btnCreateAccount");
          if (d.customer_email && linkedEl && btnCreate) {{
            linkedEl.textContent = successLinkedToEmail + " " + d.customer_email;
            linkedEl.style.display = "block";
            btnCreate.href = baseUrl + "/?register=1";
            btnCreate.textContent = successCreateAccount;
            btnCreate.style.display = "inline-block";
          }}
          showButtons(true, false);
          window.__noryaPaymentDebug.paymentStatus = d.status || "paid";
          var txId = (d.merchant_oid && String(d.merchant_oid).trim()) ? String(d.merchant_oid).trim() : oid;
          var val = (typeof d.total_amount_eur === "number") ? d.total_amount_eur : 0;
          var currency = (d.currency && typeof d.currency === "string") ? d.currency.trim() : "EUR";
          var storageKey = "norya_conv_" + txId;
          var alreadyFired = false;
          try {{ alreadyFired = sessionStorage.getItem(storageKey) === "1"; }} catch(e) {{}}
          window.__noryaPaymentDebug.send_to = conversionSendTo;
          window.__noryaPaymentDebug.condition = "status=paid_only";
          window.__noryaPaymentDebug.storageKey = storageKey;
          window.__noryaPaymentDebug.alreadyFiredFromSession = alreadyFired;
          if (verifyTag) {{
            try {{
              var gtagDefined = typeof window.gtag === "function";
              var dl = window.dataLayer || [];
              console.log("[Norya verify_tag] conversion NOT fired (verify_tag=1). gtag defined:", gtagDefined, "dataLayer length:", dl.length, "send_to:", conversionSendTo);
            }} catch(e) {{ console.warn("[Norya verify_tag]", e); }}
          }} else if (d.status === "paid" && !window.__noryaConversionFired && !alreadyFired) {{
            try {{ console.log("[Norya] conversion event dispatch start", {{ send_to: conversionSendTo, transaction_id: txId, value: val, currency: currency }}); }} catch(e) {{}}
            if (typeof gtag === "function") {{
              window.__noryaConversionFired = true;
              gtag("event", "conversion", {{ send_to: conversionSendTo, value: val, currency: currency, transaction_id: txId }});
              try {{ console.log("[Norya] conversion event dispatch attempted (gtag)", {{ send_to: conversionSendTo }}); }} catch(e) {{}}
              try {{ sessionStorage.setItem(storageKey, "1"); }} catch(e) {{}}
              try {{ console.log("[Norya] already_fired set to true", {{ storageKey: storageKey }}); }} catch(e) {{}}
              window.__noryaPaymentDebug.conversionTriggered = true;
              window.__noryaPaymentDebug.value = val;
              window.__noryaPaymentDebug.currency = currency;
              window.__noryaPaymentDebug.transaction_id = txId;
              try {{
                console.log("[Norya] Google Ads conversion FIRED — event sent to Google Ads.", {{ send_to: conversionSendTo, transaction_id: txId, value: val, currency: currency }});
                console.log("[Norya] Network: conversion request URL pattern — filter by 'googleadservices.com/pagead/conversion' or 'doubleclick.net/pagead/conversion' (GET, ~1-2s after this log).");
              }} catch(e) {{}}
            }} else {{
              window.dataLayer = window.dataLayer || [];
              window.dataLayer.push(["event", "conversion", {{ send_to: conversionSendTo, value: val, currency: currency, transaction_id: txId }}]);
              try {{ console.log("[Norya] conversion event dispatch attempted (dataLayer push, gtag not ready)"); }} catch(e) {{}}
              try {{ sessionStorage.setItem(storageKey, "1"); }} catch(e) {{}}
              try {{ console.log("[Norya] already_fired set to true", {{ storageKey: storageKey }}); }} catch(e) {{}}
              window.__noryaConversionFired = true;
              window.__noryaPaymentDebug.conversionTriggered = true;
              window.__noryaPaymentDebug.value = val;
              window.__noryaPaymentDebug.currency = currency;
              window.__noryaPaymentDebug.transaction_id = txId;
              try {{
                console.log("[Norya] Google Ads conversion QUEUED — event in dataLayer; gtag will send when loaded. Network: filter 'googleadservices.com/pagead/conversion' or 'doubleclick.net/pagead/conversion'.");
              }} catch(e) {{}}
            }}
            try {{
              window.dataLayer = window.dataLayer || [];
              window.dataLayer.push({{ event: "purchase", value: val, currency: currency, transaction_id: txId }});
            }} catch(e) {{}}
          }} else if (d.status !== "paid") {{
            window.__noryaPaymentDebug.conversionNotFiredReason = "status_not_paid";
            try {{ console.log("[Norya] Google Ads conversion NOT fired: status is not paid (purchase conversion only when status=paid)", {{ status: d.status }}); }} catch(e) {{}}
          }} else {{
            window.__noryaPaymentDebug.conversionSkippedReason = alreadyFired ? "already_sent_this_session" : "already_sent_this_page";
            if (alreadyFired) {{
              try {{
                console.log("[Norya] Google Ads conversion SKIPPED — already sent in this session for this order.", {{ storageKey: storageKey, reason: "sessionStorage set on a previous load" }});
                console.log("[Norya] To see FIRED again (e.g. for testing): add ?conv_reset=1 to the URL and reload, or use a new incognito/session.");
              }} catch(e) {{}}
            }} else {{
              try {{ console.log("[Norya] Google Ads conversion SKIPPED — already sent on this page load (duplicate prevention).", {{ send_to: conversionSendTo }}); }} catch(e) {{}}
            }}
          }}
          // Test akışı: test123 için otomatik yönlendirme yapma; kullanıcı success ekranında kalır.
          if (oid === "test123") {{
            try {{ console.log("[Norya payment success] test mode: skip auto-redirect for merchant_oid=test123"); }} catch(e) {{}}
            return;
          }}
          if (window.self !== window.top) {{ try {{ window.parent.postMessage("norya_payment_ok", "*"); }} catch(e) {{}} }}
          var redirectTo = guestToken ? (baseUrl + "/?guest_token=" + encodeURIComponent(guestToken) + "#analyze") : reportUrl;
          redirectTimer = setTimeout(function() {{ window.location.href = redirectTo; }}, 1500);
          return;
        }}
        if (d.status === "failed") {{
          stopPolling();
          showSpinner(false);
          setStatus(failedShort);
          showButtons(false, true);
          window.__noryaPaymentDebug.paymentStatus = "failed";
          window.__noryaPaymentDebug.conversionNotFiredReason = "status_failed";
          try {{ console.log("[Norya] Google Ads conversion NOT fired: payment status=failed (only paid orders trigger conversion)"); }} catch(e) {{}}
          return;
        }}
        try {{ console.log("[Norya payment success] payment status pending", d && d.status); }} catch(e) {{}}
        setStatus(pendingBank);
      }})
      .catch(function() {{
        try {{ console.log("[Norya payment success] polling error"); }} catch(e) {{}}
        setStatus(updating);
      }});
  }}
  function scheduleNext() {{
    if (hasTimedOut) return;
    if (Date.now() - start > timeoutTotal) return;
    var interval = (Date.now() - start) < fastUntil ? intervalFast : intervalSlow;
    pollTimer = setTimeout(function() {{ doPoll(false); scheduleNext(); }}, interval);
  }}
  document.getElementById("checkDoneBtn").addEventListener("click", function() {{
    doPoll(true);
    if (pollTimer) {{ clearTimeout(pollTimer); scheduleNext(); }}
  }});
  showSpinner(true);
  try {{ console.log("[Norya payment success] polling will start in 500ms (gtag load grace); send_to=" + conversionSendTo); }} catch(e) {{}}
  setTimeout(function() {{
    doPoll(false);
    scheduleNext();
  }}, 500);
}})();
  </script>
</body>
</html>"""
    return HTMLResponse(html)


@app.get("/payment/failed", response_class=HTMLResponse)
def payment_failed_page(
    request: Request,
    lang: str = Query("tr", description="Language: tr, en, de, fr, it, es"),
):
    """Ödeme tamamlanamadı sayfası. Tüm dillerde ve mobil uyumlu."""
    base = _paytr_canonical_base(request)
    lang = (lang or "tr").lower()[:2]
    if lang not in ("tr", "en", "de", "fr", "it", "es"):
        lang = "tr"
    t = get_pay_ui(lang)
    title = t["failed_title"]
    msg = t["failed_message"]
    retry_text = t["failed_retry"]
    pricing_text = t["failed_pricing"]
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><meta name="theme-color" content="#0f172a">
<title>{title} – {BRAND_NAME}</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 0; padding: max(16px, env(safe-area-inset-top)); padding-bottom: max(24px, env(safe-area-inset-bottom)); background: linear-gradient(165deg, #0c1222 0%, #0f172a 50%); color: #e2e8f0; min-height: 100vh; min-height: 100dvh; display: flex; align-items: center; justify-content: center; -webkit-tap-highlight-color: transparent; }}
  .card {{ background: linear-gradient(180deg, rgba(30,41,59,0.95), rgba(15,23,42,0.98)); border: 1px solid rgba(248,113,113,0.2); border-radius: 20px; padding: clamp(24px, 5vw, 40px); max-width: 420px; width: 100%; margin: 0 16px; text-align: center; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.35); }}
  h1 {{ color: #fca5a5; font-size: clamp(1.25rem, 4vw, 1.5rem); margin-bottom: 10px; font-weight: 700; }}
  p {{ color: #94a3b8; margin-bottom: 28px; font-size: clamp(0.9rem, 2.5vw, 0.95rem); line-height: 1.5; }}
  .btns {{ display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; }}
  a {{ display: inline-block; background: linear-gradient(135deg, #0EA5A4, #0d9488); color: #fff; padding: 14px 24px; min-height: 48px; line-height: 20px; border-radius: 12px; text-decoration: none; font-weight: 600; box-shadow: 0 4px 14px rgba(14,165,164,0.35); transition: transform 0.15s; touch-action: manipulation; }}
  a:hover {{ transform: translateY(-2px); }}
  a.secondary {{ background: transparent; border: 2px solid #475569; color: #94a3b8; box-shadow: none; }}
  a.secondary:hover {{ border-color: #0EA5A4; color: #0EA5A4; }}
</style>
</head>
<body>
  <div class="card">
    <h1>{title}</h1>
    <p>{msg}</p>
    <div class="btns">
      <a href="{base}/payment?lang={lang}">{retry_text}</a>
      <a href="{base}/#pricing" class="secondary">{pricing_text}</a>
    </div>
  </div>
</body>
</html>"""
    return HTMLResponse(html)


# --- PayTR callback (Bildirim URL): public, auth yok; POST ile PayTR sunucusu bildirim gönderir; başarıda plain text "OK" döner. ---
@app.get("/paytr/callback")
def paytr_callback_get():
    """Tarayıcıda GET ile açıldığında 404 vermemek için: Bu URL sadece PayTR'nin POST isteği içindir."""
    return PlainTextResponse(
        "PayTR bildirim URL'i. Bu adres yalnızca PayTR sunucusu tarafından POST ile kullanılır.",
        status_code=200,
    )


@app.post("/payment/callback")
async def payment_callback(request: Request, db: Session = Depends(get_db)):
    """PayTR bildirim URL: ödeme sonucu POST ile gelir. Public, auth yok. Başarılı işlemde plain text OK."""
    return await _paytr_callback_handle(request, db)


@app.post("/paytr/callback")
async def paytr_callback(request: Request, db: Session = Depends(get_db)):
    """PayTR bildirim URL (alias): panelde Bildirim URL https://noryaai.com/paytr/callback ise bu route kullanılır. Public, auth yok."""
    return await _paytr_callback_handle(request, db)


@app.post("/api/payment/callback")
async def api_payment_callback(request: Request, db: Session = Depends(get_db)):
    """PayTR bildirim URL (alias): /api/payment/callback kullanılıyorsa (örn. Render doc). Public, auth yok."""
    return await _paytr_callback_handle(request, db)


@app.post("/api/paytr/webhook")
async def paytr_webhook(request: Request, db: Session = Depends(get_db)):
    """PayTR webhook (alias): aynı işlem. Public, auth yok."""
    return await _paytr_callback_handle(request, db)


@app.post("/payment/grant")
def payment_grant(body: GrantPaymentRequest, db: Session = Depends(get_db)):
    """Destek: merchant_oid ile siparişi bulup kullanıcıya hak tanır (admin_secret gerekir)."""
    if not settings.admin_secret or body.admin_secret != settings.admin_secret:
        raise HTTPException(status_code=403, detail="Yetkisiz.")
    stmt = select(PaymentOrder).where(PaymentOrder.merchant_oid == body.merchant_oid)
    order = db.exec(stmt).first()
    if not order:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı.")
    if order.status == "completed":
        return {"ok": True, "message": "Sipariş zaten işlenmiş."}
    user = db.get(User, order.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    qty = getattr(order, "quantity", 1) or 1
    if order.product == "single":
        user.extra_credits = (getattr(user, "extra_credits", 0) or 0) + qty
        db.add(user)
    elif order.product in ("monthly", "yearly"):
        user.plan = "pro"
        db.add(user)
    else:
        raise HTTPException(status_code=400, detail="Geçersiz ürün.")
    order.status = "completed"
    db.add(order)
    _audit(db, f"payment_grant_{order.product}", order.user_id, body.merchant_oid[:64])
    db.commit()
    return {"ok": True, "message": "Hak tanındı."}


@app.post("/admin/cache/purge-expired")
def admin_cache_purge_expired(x_admin_secret: str | None = Header(None, alias="X-Admin-Secret")):
    """Süresi dolan ai_cache kayıtlarını siler. X-Admin-Secret header gerekir."""
    if not settings.admin_secret or x_admin_secret != settings.admin_secret:
        raise HTTPException(status_code=403, detail="Yetkisiz.")
    deleted = purge_ai_cache_expired(_cache_conn)
    return {"deleted": deleted}


# ——— SEO landing pages (high-intent queries). Must be registered before /{lang}/{path:path}. ———
def _render_seo_landing(request: Request, lang: str, slug: str) -> HTMLResponse:
    """Render SEO landing template for (lang, slug). Call only when (lang, slug) is a valid SEO route."""
    content = get_seo_landing_content(lang, slug)
    if not content:
        raise HTTPException(status_code=404, detail="Not Found")
    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/{lang}/{slug}"
    meta = get_seo_landing_meta(lang, slug)
    hreflang_alternates = get_seo_landing_hreflang(lang, slug, base_url)
    og_locale = SEO_OG_LOCALE_MAP.get(lang, "en_US")
    related_links = get_related_links(lang, base_url)
    return templates.TemplateResponse(
        "seo_landing.html",
        {
            "request": request,
            "lang": lang,
            "slug": slug,
            "t": content,
            "meta": meta,
            "canonical_url": canonical_url,
            "hreflang_alternates": hreflang_alternates,
            "og_locale": og_locale,
            "base_url": base_url,
            "related_links": related_links,
        },
    )


@app.get("/tr/kan-tahlili-sonucu", response_class=HTMLResponse)
def seo_landing_tr_kan_tahlili(request: Request):
    return _render_seo_landing(request, "tr", "kan-tahlili-sonucu")


@app.get("/tr/kan-degerleri-anlama", response_class=HTMLResponse)
def seo_landing_tr_kan_degerleri(request: Request):
    return _render_seo_landing(request, "tr", "kan-degerleri-anlama")


@app.get("/tr/hemogram-sonucu", response_class=HTMLResponse)
def seo_landing_tr_hemogram(request: Request):
    return _render_seo_landing(request, "tr", "hemogram-sonucu")


@app.get("/de/blutwerte-verstehen", response_class=HTMLResponse)
def seo_landing_de_blutwerte(request: Request):
    return _render_seo_landing(request, "de", "blutwerte-verstehen")


@app.get("/de/laborwerte-verstehen", response_class=HTMLResponse)
def seo_landing_de_laborwerte(request: Request):
    return _render_seo_landing(request, "de", "laborwerte-verstehen")


@app.get("/en/ai-blood-test-analyzer", response_class=HTMLResponse)
def seo_landing_en_ai_blood_test_analyzer(request: Request):
    return _render_seo_landing(request, "en", "ai-blood-test-analyzer")


@app.get("/en/compare/norya-vs-generic-ai", response_class=HTMLResponse)
def compare_en_norya_vs_generic_ai(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "NoryaAI vs Generic AI for Blood Tests — Honest Comparison | NoryaAI",
        "meta_description": "How does NoryaAI compare to ChatGPT or other AI chatbots for understanding blood test results? Side-by-side comparison of structured reports vs free-form chat answers.",
        "hero_title": "NoryaAI vs Generic AI Chatbots for Blood Tests",
        "hero_sub": "Both can work with lab data — but they approach it very differently. Here is an honest, side-by-side look at what each one offers when you need to understand your blood test results.",
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "See a sample report",
        "quick_answer_title": "The short version",
        "quick_answer": "Generic AI chatbots like ChatGPT can explain medical terms and answer health questions in conversation. NoryaAI is purpose-built for blood tests: it reads your lab report, maps every value to reference ranges, and produces a structured, doctor-ready summary with a health score — not a free-form paragraph. Both have a place, but they solve different problems.",
        "comparison_title": "Side-by-side comparison",
        "comparison_sub": "How the two approaches differ across the features that matter most when you are looking at blood test results.",
        "comparison_items": [
            {
                "label": "Report upload",
                "generic": "Copy-paste values into a chat prompt and hope the formatting holds",
                "norya": "Upload PDF, snap a photo, or paste text — values and ranges are parsed automatically",
            },
            {
                "label": "Reference ranges",
                "generic": "May guess ranges or omit them; no guarantee they match your lab's standards",
                "norya": "Reference ranges displayed for every value — normal, low, or high — clearly labeled",
            },
            {
                "label": "Units and lab formatting",
                "generic": "No built-in awareness of lab-specific units or result layouts",
                "norya": "Recognizes common lab units, panel structures, and result formats automatically",
            },
            {
                "label": "Output structure",
                "generic": "Free-form paragraph that varies with each prompt — no consistent format",
                "norya": "Structured health score, category breakdown, and flagged markers — consistent every time",
            },
            {
                "label": "Multilingual reports",
                "generic": "Can translate text, but medical nuance may be lost in general translation",
                "norya": "Full reports in 9+ languages with medical context preserved throughout",
            },
            {
                "label": "Doctor-ready summary",
                "generic": "No downloadable report — you would need to copy and format the chat yourself",
                "norya": "Doctor-ready PDF with QR verification — print it, save it, or share it",
            },
            {
                "label": "Privacy and data handling",
                "generic": "Conversations may be stored and used for model training",
                "norya": "GDPR/KVKK compliant — encrypted, never sold, never used for training",
            },
            {
                "label": "Blood-test specific workflow",
                "generic": "General-purpose chat interface designed for any topic",
                "norya": "Dedicated upload, analysis, and report pipeline built specifically for lab results",
            },
            {
                "label": "Workflow type",
                "generic": "Open-ended conversation — the quality depends on how you write your prompt",
                "norya": "Guided, structured analysis — upload once and get a complete report, no prompt needed",
            },
        ],
        "generic_helps_title": "When generic AI chatbots can still help",
        "generic_helps_sub": "This is not about one tool being bad and another being good. They serve different purposes.",
        "generic_helps_items": [
            {
                "icon": "📚",
                "title": "General health education",
                "desc": "Chatbots are great for learning what a biomarker means, how the immune system works, or what a specific condition involves — broad educational questions.",
            },
            {
                "icon": "💡",
                "title": "Brainstorming questions for your doctor",
                "desc": "Before an appointment, a chatbot can help you think through what to ask — even if it cannot read your actual lab report with precision.",
            },
            {
                "icon": "🔍",
                "title": "Understanding medical terminology",
                "desc": "If you encounter an unfamiliar term in your report, a general AI can explain it quickly in plain language.",
            },
        ],
        "why_norya_title": "Why people choose NoryaAI for blood tests",
        "why_norya_sub": "When accuracy, structure, and a clean next-step matter more than a general conversation.",
        "why_norya_items": [
            {
                "title": "Upload once, get a structured report",
                "desc": "No prompt engineering, no reformatting. Upload your lab results and receive a health score, category breakdown, and flagged markers — automatically.",
            },
            {
                "title": "Consistent format you can compare over time",
                "desc": "Every report follows the same structure, so you can track changes across multiple blood tests and spot trends at a glance.",
            },
            {
                "title": "Doctor-ready PDF you can actually bring",
                "desc": "A clean, professional summary with QR verification. Print it or share it digitally — designed to be useful at your next appointment.",
            },
            {
                "title": "Your language, your report",
                "desc": "Choose from 9+ languages and get your full report in the one that feels most natural to you — with medical context intact.",
            },
        ],
        "faqs": [
            {
                "q": "Can ChatGPT explain blood test results?",
                "a": "Yes, to a degree. ChatGPT can explain what individual values mean in general terms. However, it does not parse your actual lab report, may hallucinate reference ranges, and produces a different answer each time you ask. NoryaAI is built to read your report directly and output a consistent, structured summary.",
            },
            {
                "q": "Is NoryaAI a diagnosis tool?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions.",
            },
            {
                "q": "Why is a structured report better than a chat answer?",
                "a": "A structured report gives you a health score, category breakdown, and flagged markers in a consistent format. You can compare it with previous tests, print it for your doctor, and see at a glance which values need attention — something a free-form chat paragraph cannot reliably offer.",
            },
            {
                "q": "Can I upload a PDF instead of copying values manually?",
                "a": "Yes. NoryaAI accepts PDF uploads, photos of printed lab reports (JPG/PNG), and pasted text. It parses the values and reference ranges automatically — no manual data entry required.",
            },
            {
                "q": "Is NoryaAI better for multilingual lab reports?",
                "a": "NoryaAI generates full reports in 9+ languages with preserved medical context. While general chatbots can translate text, they may lose nuance in medical terminology. NoryaAI's multilingual output is designed specifically for lab result interpretation.",
            },
        ],
        "cta_title": "Ready to try a structured blood test report?",
        "cta_sub": "Upload your lab results and see the difference a purpose-built analyzer makes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing plans",
    }
    return templates.TemplateResponse("compare_page.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/compare/norya-vs-generic-ai",
    })


@app.get("/en/why-not-generic-ai-for-blood-test-results", response_class=HTMLResponse)
def editorial_en_why_not_generic_ai(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "Should You Use Generic AI for Blood Test Results? | NoryaAI",
        "meta_description": "Can ChatGPT or other AI chatbots safely explain your blood test results? Learn where general-purpose AI helps, where it falls short, and when a structured tool makes more sense.",
        "hero_title": "Should You Use Generic AI for Blood Test Results?",
        "hero_sub": "AI chatbots can do a lot \u2014 but understanding lab results takes more than a general conversation. Here is an honest look at what works, what does not, and when a purpose-built workflow makes the difference.",
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "See a sample report",
        "short_answer_title": "The short answer",
        "short_answer": "Generic AI chatbots are useful for explaining medical terms and exploring health topics. But when you need to upload a lab report and get structured output \u2014 with reference ranges, flagged markers, and a summary you can bring to your doctor \u2014 a tool built for that specific task tends to be more practical and reliable.",
        "generic_helps_title": "Where generic AI chatbots can genuinely help",
        "generic_helps_sub": "General-purpose AI is not the wrong choice for everything. Here is where it works well.",
        "generic_helps_items": [
            {
                "icon": "\U0001f4da",
                "title": "Learning about health topics",
                "desc": "Chatbots are excellent at exploring what a biomarker means, how certain conditions work, or what a specific lab panel measures \u2014 broad educational questions without needing your actual report.",
            },
            {
                "icon": "\U0001f4a1",
                "title": "Preparing questions for your doctor",
                "desc": "Before an appointment, a chatbot can help you brainstorm what to ask \u2014 even if it cannot reliably parse your lab report.",
            },
            {
                "icon": "\U0001f4dd",
                "title": "Summarizing general health articles",
                "desc": "If you find a medical article that is hard to follow, a chatbot can break it down into simpler language quickly.",
            },
        ],
        "falls_short_title": "Where generic AI falls short for lab reports",
        "falls_short_sub": "Lab results are not regular text. They contain structured data \u2014 values, units, reference ranges, panel groupings \u2014 that general-purpose chatbots were not designed to handle consistently.",
        "falls_short_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Uploading a lab report directly",
                "desc": "Most chatbots require you to copy and paste values manually. Formatting, tables, and panel structure are often lost \u2014 and with them, important context.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Reference ranges and units",
                "desc": "A chatbot may guess reference ranges or skip them entirely. It has no reliable way to know what your specific lab considers normal, low, or high.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Structured, consistent output",
                "desc": "Every chatbot response is different. There is no health score, no category breakdown, no flagged markers \u2014 just a paragraph that changes each time you ask.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "A doctor-ready summary",
                "desc": "Chatbot responses cannot be downloaded, printed, or verified. A dedicated tool produces a clean PDF you can share at your next appointment.",
            },
            {
                "icon": "\U0001f310",
                "title": "Multilingual medical context",
                "desc": "General translation can lose medical nuance. A purpose-built tool preserves clinical context when generating reports in different languages.",
            },
            {
                "icon": "\U0001f512",
                "title": "Privacy-first data handling",
                "desc": "Chat conversations may be stored and used for model training. A dedicated health tool can offer encrypted processing with no data reuse.",
            },
        ],
        "structured_title": "Why a structured workflow matters for blood tests",
        "structured_sub": "When you are looking at lab results, what you need is not a conversation \u2014 it is clarity.",
        "structured_items": [
            {
                "title": "Consistency you can track over time",
                "desc": "A structured report uses the same format every time, so you can compare your results across months and spot trends \u2014 not something a chat paragraph allows.",
            },
            {
                "title": "A format your doctor recognizes",
                "desc": "Doctors are used to structured summaries with ranges, flags, and categories. A well-organized report makes your appointment more productive.",
            },
            {
                "title": "No prompt engineering required",
                "desc": "Upload your report once and get a complete analysis. No need to figure out the right question or reformat your data.",
            },
            {
                "title": "Verified, downloadable output",
                "desc": "A PDF with a health score and QR verification is something you can save, print, and share \u2014 a chat window is not.",
            },
        ],
        "why_norya_title": "Why some users choose NoryaAI",
        "why_norya_sub": "NoryaAI is one option for people who want a structured, privacy-first approach to understanding their blood test results.",
        "why_norya_items": [
            {
                "title": "Upload once, get a structured report",
                "desc": "PDF, photo, or pasted text. NoryaAI reads your lab report and produces a health score, category breakdown, and flagged markers \u2014 automatically.",
            },
            {
                "title": "Doctor-ready PDF with QR verification",
                "desc": "A professional summary you can print, save, or share digitally. Designed to be useful at your next appointment.",
            },
            {
                "title": "Reports in 9+ languages",
                "desc": "English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, Arabic, and more \u2014 with medical context preserved.",
            },
            {
                "title": "Privacy-first \u2014 encrypted, never sold",
                "desc": "GDPR and KVKK compliant. Your data is encrypted, used only for your report, and never shared with third parties.",
            },
        ],
        "faqs": [
            {
                "q": "Should I use ChatGPT to understand my blood test results?",
                "a": "ChatGPT can explain what individual blood values mean in general terms. However, it cannot reliably parse your actual lab report, may generate inaccurate reference ranges, and produces inconsistent output. For structured analysis with reference ranges and a downloadable summary, a purpose-built tool is more practical.",
            },
            {
                "q": "Can generic AI tools read a lab report PDF?",
                "a": "Most general-purpose chatbots work with pasted text, not uploaded files. Even when file upload is available, they are not designed to parse lab-specific formatting \u2014 values, units, panel structures, and reference ranges may be misread or ignored.",
            },
            {
                "q": "Is NoryaAI a replacement for my doctor?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose, treat, or recommend medication. Always consult a qualified healthcare professional for medical decisions.",
            },
            {
                "q": "What makes a structured report different from a chatbot answer?",
                "a": "A structured report gives you a health score, category breakdown, and flagged markers in a consistent format that you can compare over time, print for your doctor, and verify. A chatbot gives you a paragraph that changes with every prompt.",
            },
            {
                "q": "Does NoryaAI support reports in different languages?",
                "a": "Yes. NoryaAI generates full reports in 9+ languages including English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic \u2014 with medical context preserved throughout.",
            },
            {
                "q": "Is my health data safe with NoryaAI?",
                "a": "All uploads are encrypted in transit and at rest. Your data is used only to generate your report and is never sold, shared with advertisers, or used for model training. NoryaAI is GDPR and KVKK compliant.",
            },
        ],
        "cta_title": "Ready to try a structured approach?",
        "cta_sub": "Upload your blood test and see what a purpose-built report looks like.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
    }
    return templates.TemplateResponse("editorial_landing.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/why-not-generic-ai-for-blood-test-results",
    })


@app.get("/en/upload-blood-test-results", response_class=HTMLResponse)
def landing_en_upload_blood_test(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "Upload Blood Test Results \u2014 AI-Powered Analysis | NoryaAI",
        "meta_description": "Upload your blood test PDF, photo, or lab report and get a structured, doctor-ready summary with reference ranges, health score, and flagged markers \u2014 in minutes.",
        "hero_title": "Upload Your Blood Test Results",
        "hero_sub": "Upload a PDF, snap a photo, or paste your lab values. NoryaAI turns your blood test into a structured, easy-to-read report with reference ranges, flagged markers, and a health score.",
        "hero_trust": "Encrypted upload \u00b7 GDPR & KVKK compliant \u00b7 No data sharing",
        "cta_hero_primary": "Start analysis",
        "cta_hero_secondary": "View sample report",
        "formats_title": "Supported upload formats",
        "formats_sub": "Choose whichever method is easiest for you \u2014 all three produce the same structured report.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "PDF lab reports",
                "desc": "Upload the PDF you received from your lab or hospital. NoryaAI reads tables, values, and reference ranges directly from the document.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "Photos & screenshots",
                "desc": "Take a photo of your printed report or screenshot your online lab portal. JPG and PNG files are supported.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "Pasted text",
                "desc": "No file? Copy and paste your lab values directly. NoryaAI will structure them into a complete report.",
            },
        ],
        "steps_title": "What happens after you upload",
        "steps_sub": "From upload to a structured report \u2014 the entire process takes just a few minutes.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Upload your report",
                "desc": "Choose a PDF, photo, or paste your lab values into the analysis form.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI reads your data",
                "desc": "Values, units, and reference ranges are extracted and structured automatically.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Structured summary",
                "desc": "Health score, category breakdown, and flagged markers \u2014 all in one clear view.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Download your report",
                "desc": "Get a doctor-ready PDF you can print, save, or share at your next appointment.",
            },
        ],
        "reasons_title": "Why people upload their results here",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "Before a doctor visit",
                "desc": "Arrive at your appointment with a clear, organized summary. It helps you ask better questions and makes the conversation more productive.",
            },
            {
                "icon": "\U0001f310",
                "title": "Reports in another language",
                "desc": "Got lab results in a language you do not fully understand? Upload them and get a structured explanation in your preferred language \u2014 9+ languages supported.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "To understand a complex report",
                "desc": "Pages of lab data can be overwhelming. NoryaAI turns them into a categorized, easy-to-read breakdown with reference ranges and clear explanations.",
            },
        ],
        "trust_title": "Your data stays yours",
        "trust_sub": "Privacy is not an afterthought. It is built into every step of the upload and analysis process.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "Encrypted in transit and at rest"},
            {"icon": "\U0001f6e1\ufe0f", "text": "GDPR & KVKK compliant"},
            {"icon": "\U0001f6ab", "text": "Never shared or sold"},
            {"icon": "\U0001f504", "text": "Not used for model training"},
        ],
        "preview_title": "What your report looks like",
        "preview_sub": "Here is a glimpse of the structured output you receive after uploading your blood test.",
        "preview_lines": [
            {"label": "Health Score", "value": "78 / 100 \u2014 Good overall, a few markers to watch"},
            {"label": "Hemoglobin", "value": "14.2 g/dL \u2014 Within normal range (13.5\u201317.5)"},
            {"label": "Glucose", "value": "108 mg/dL \u2014 Slightly elevated (normal: 70\u2013100)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Normal thyroid function (0.4\u20134.0)"},
            {"label": "Vitamin D", "value": "18 ng/mL \u2014 Below recommended level (30\u2013100)"},
        ],
        "preview_disclaimer": "Sample data for illustration only. Your actual report will reflect your personal lab values, units, and reference ranges.",
        "preview_link": "See a full sample report \u2192",
        "faqs": [
            {
                "q": "What file formats can I upload?",
                "a": "NoryaAI accepts PDF files, JPG/JPEG images, and PNG images. You can also paste your lab values as text if you do not have a file to upload.",
            },
            {
                "q": "How long does the analysis take?",
                "a": "Most reports are processed in under two minutes. Complex multi-page PDFs may take slightly longer, but you will see your structured summary shortly after uploading.",
            },
            {
                "q": "Is my uploaded report stored or shared?",
                "a": "Your uploaded file is used only to generate your report. All data is encrypted in transit and at rest, never shared with third parties, and never used for model training. NoryaAI is GDPR and KVKK compliant.",
            },
            {
                "q": "Can I upload reports in languages other than English?",
                "a": "Yes. NoryaAI can read lab reports in multiple languages and generate your structured summary in any of 9+ supported languages, including English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic.",
            },
            {
                "q": "Do I need to create an account to upload?",
                "a": "You can start an analysis without creating an account. An account lets you save your reports, track results over time, and access them from any device.",
            },
            {
                "q": "Is NoryaAI a replacement for my doctor?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values to help you understand your results better. It does not diagnose, treat, or prescribe. Always consult a qualified healthcare professional for medical decisions.",
            },
        ],
        "cta_title": "Ready to upload your blood test?",
        "cta_sub": "Get a structured, doctor-ready report in minutes. PDF, photo, or pasted text \u2014 your choice.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
    }
    return templates.TemplateResponse("upload_landing.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/upload-blood-test-results",
    })


@app.get("/en/blood-test-results-explained", response_class=HTMLResponse)
def landing_en_blood_test_explained(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "Blood Test Results Explained \u2014 What Your Report Actually Means | NoryaAI",
        "meta_description": "Not sure what your blood test results mean? Learn how to read abbreviations, reference ranges, and units \u2014 and how a structured AI report can make it clearer.",
        "hero_title": "Blood Test Results Explained",
        "hero_sub": "Lab reports are packed with abbreviations, numbers, and ranges that most people were never taught to read. This guide covers what makes them confusing, what to look for, and how a structured approach can help you understand your results before your next doctor visit.",
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "See a sample report",
        "confusing_title": "Why blood test reports can feel confusing",
        "confusing_sub": "You are not the only one who finds lab reports hard to read. Here are the most common reasons people struggle with them.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "Unfamiliar abbreviations",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 lab reports are full of shorthand that is rarely explained on the document itself.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Reference ranges that vary",
                "desc": "What counts as \u201cnormal\u201d can differ between labs, age groups, and even measurement methods. A value that is flagged at one lab may be fine at another.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "Different units, same test",
                "desc": "Hemoglobin in g/dL or g/L? Glucose in mg/dL or mmol/L? The same biomarker can appear in different units depending on the country or lab.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "Dense formatting, no explanation",
                "desc": "Most lab reports are designed for clinicians, not patients. You get rows of numbers but no context about what they mean for you.",
            },
        ],
        "clarify_title": "What NoryaAI helps clarify",
        "clarify_sub": "NoryaAI does not replace your doctor. It gives you a structured, readable version of your results so you can walk into your appointment better informed.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "Plain-language explanations",
                "desc": "Each biomarker comes with a clear, jargon-free explanation of what it measures and why it matters.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Reference ranges in context",
                "desc": "Your values are shown alongside reference ranges so you can see where you stand \u2014 high, low, or within normal limits.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "Flagged markers",
                "desc": "Values outside the expected range are highlighted so you can focus on what may need attention.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Structured categories",
                "desc": "Results are grouped by category \u2014 liver, kidney, thyroid, blood cells, and more \u2014 instead of a flat list of numbers.",
            },
            {
                "icon": "\U0001f310",
                "title": "Multilingual reports",
                "desc": "Get your report in 9+ languages with medical context preserved. Useful when your lab report is in a language you do not fully understand.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Doctor-ready summary",
                "desc": "A clean PDF with a health score and QR verification that you can print, save, or share at your next appointment.",
            },
        ],
        "common_title": "Common things people look for in their results",
        "common_sub": "These are some of the most frequently searched biomarkers and panels. NoryaAI covers all of them in its structured reports.",
        "common_items": [
            {"title": "Complete Blood Count (CBC)", "desc": "WBC, RBC, hemoglobin, hematocrit, platelets \u2014 the most common panel in routine checkups."},
            {"title": "Liver function (ALT, AST, ALP)", "desc": "Enzymes that indicate how well your liver is working. Often checked in routine bloodwork."},
            {"title": "Kidney function (BUN, creatinine)", "desc": "Markers that show how effectively your kidneys are filtering waste from your blood."},
            {"title": "Thyroid panel (TSH, T3, T4)", "desc": "Hormones that regulate metabolism, energy levels, and body temperature."},
            {"title": "Blood sugar (glucose, HbA1c)", "desc": "Fasting glucose and long-term average blood sugar. Key markers for metabolic health."},
            {"title": "Cholesterol & lipids (LDL, HDL, triglycerides)", "desc": "Lipid panel results that are commonly discussed in cardiovascular health assessments."},
            {"title": "Iron & ferritin", "desc": "Markers related to iron storage and transport. Relevant for fatigue, anemia, and general energy levels."},
            {"title": "Vitamin D & B12", "desc": "Common vitamin levels that many people have checked, especially in routine annual bloodwork."},
            {"title": "Inflammation markers (CRP, ESR)", "desc": "General indicators of inflammation in the body. Often used as a screening baseline."},
        ],
        "how_title": "How it works",
        "how_sub": "Three steps from a confusing lab report to a structured summary you can actually understand.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Upload your report",
                "desc": "PDF, photo, or pasted text. Choose whatever is easiest.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI structures your data",
                "desc": "Values, units, and ranges are extracted and organized into clear categories.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Get your explained report",
                "desc": "Health score, flagged markers, plain-language explanations, and a downloadable PDF.",
            },
        ],
        "preview_title": "What your explained report looks like",
        "preview_sub": "Here is a glimpse of how NoryaAI structures and explains your blood test results.",
        "preview_lines": [
            {"label": "Health Score", "value": "78 / 100 \u2014 Good overall, a few markers to review"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 Normal white blood cell count (4.5\u201311.0)"},
            {"label": "Hemoglobin", "value": "14.2 g/dL \u2014 Within reference range (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 Slightly elevated liver enzyme (normal: 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Normal thyroid function (0.4\u20134.0)"},
            {"label": "Vitamin D", "value": "18 ng/mL \u2014 Below recommended level (30\u2013100)"},
        ],
        "preview_disclaimer": "Sample data for illustration only. Your actual report will reflect your personal lab values, units, and reference ranges.",
        "faqs": [
            {
                "q": "What does \u201cblood test results explained\u201d actually mean?",
                "a": "It means turning the raw numbers, abbreviations, and reference ranges on your lab report into plain-language explanations you can understand \u2014 with context about what each value measures and whether it falls within normal limits.",
            },
            {
                "q": "Can NoryaAI explain any type of blood test?",
                "a": "NoryaAI supports most standard blood panels including CBC, metabolic panels, liver and kidney function, thyroid, lipids, vitamins, and inflammation markers. If your report contains values it can parse, they will be included in your structured summary.",
            },
            {
                "q": "Is this a medical diagnosis?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions, recommend treatments, or replace professional medical advice. Always consult a qualified healthcare professional.",
            },
            {
                "q": "Why do reference ranges differ between labs?",
                "a": "Labs use different equipment, methods, and population samples to establish their ranges. Age, sex, and even altitude can influence what a lab considers \u201cnormal.\u201d This is why the same value might be flagged at one lab but not another.",
            },
            {
                "q": "Can I get my results explained in another language?",
                "a": "Yes. NoryaAI generates reports in 9+ languages including English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic \u2014 with medical context preserved in translation.",
            },
            {
                "q": "How is this different from just Googling my results?",
                "a": "Googling individual values one by one gives you scattered, generic information. NoryaAI reads your entire report at once, compares each value against its reference range, and produces a single structured summary with a health score, flagged markers, and categories \u2014 all in one place.",
            },
        ],
        "cta_title": "Ready to understand your blood test?",
        "cta_sub": "Upload your lab report and get a clear, structured summary with plain-language explanations \u2014 in minutes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
    }
    return templates.TemplateResponse("explained_landing.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/blood-test-results-explained",
    })


@app.get("/en/guides/how-to-read-cbc", response_class=HTMLResponse)
def guide_en_how_to_read_cbc(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "How to Read a CBC \u2014 Complete Blood Count Explained | NoryaAI",
        "meta_description": "Learn how to read a CBC (complete blood count) report. Understand WBC, RBC, hemoglobin, hematocrit, platelets, and indices \u2014 with reference ranges explained in plain language.",
        "badge": "Lab Guide",
        "hero_title": "How to Read a CBC",
        "hero_sub": "A complete blood count is one of the most common blood tests ordered worldwide. This guide walks through each component \u2014 what it measures, what the abbreviations mean, and how to make sense of the numbers on your report.",
        "sections": [
            {
                "title": "What is a CBC?",
                "intro": "A complete blood count (CBC) measures the cells that make up your blood: red cells, white cells, and platelets. Doctors use it as a general screening tool to check for infections, anemia, clotting issues, and overall health. It is often part of a routine physical or a first step when investigating symptoms like fatigue, bruising, or recurring infections.",
                "paragraphs": [
                    "Your CBC report typically includes 10\u201320 individual values. Each one describes a different aspect of your blood \u2014 how many cells you have, how large they are, how much hemoglobin they carry, and how varied they are in size.",
                    "The sections below break these down into groups so they are easier to understand.",
                ],
            },
            {
                "title": "White blood cells (WBC)",
                "intro": "White blood cells are part of your immune system. A CBC measures their total count and sometimes breaks them into subtypes (a differential).",
                "markers": [
                    {
                        "name": "White blood cell count",
                        "abbr": "WBC",
                        "desc": "The total number of white blood cells in a given volume of blood. A high count may suggest infection or inflammation; a low count may indicate a weakened immune response. Many temporary factors \u2014 stress, exercise, medications \u2014 can shift this number.",
                        "range": "4,500\u201311,000 cells/\u00b5L",
                    },
                    {
                        "name": "Neutrophils",
                        "abbr": "NEUT",
                        "desc": "The most common type of white blood cell. Neutrophils are usually the first responders to bacterial infections. Their percentage and absolute count are reported separately.",
                        "range": "40\u201370% of WBC",
                    },
                    {
                        "name": "Lymphocytes",
                        "abbr": "LYMPH",
                        "desc": "Involved in viral defense and long-term immunity. A rise in lymphocytes can occur with viral infections; a decrease may appear in certain immune conditions.",
                        "range": "20\u201340% of WBC",
                    },
                ],
            },
            {
                "title": "Red blood cells, hemoglobin, and hematocrit",
                "intro": "Red blood cells carry oxygen from your lungs to the rest of your body. Several CBC values describe their count, their oxygen-carrying capacity, and their proportion in your blood.",
                "markers": [
                    {
                        "name": "Red blood cell count",
                        "abbr": "RBC",
                        "desc": "The total number of red blood cells per volume of blood. Values vary by sex and age. A low count is one sign that may be associated with anemia; a high count may be seen in dehydration or other conditions.",
                        "range": "4.5\u20135.5 million cells/\u00b5L (men) \u00b7 4.0\u20135.0 (women)",
                    },
                    {
                        "name": "Hemoglobin",
                        "abbr": "HGB / Hb",
                        "desc": "The protein inside red blood cells that binds oxygen. Hemoglobin is one of the most commonly checked values in a CBC. Low hemoglobin is a key marker associated with anemia.",
                        "range": "13.5\u201317.5 g/dL (men) \u00b7 12.0\u201316.0 g/dL (women)",
                    },
                    {
                        "name": "Hematocrit",
                        "abbr": "HCT",
                        "desc": "The percentage of your blood volume that is made up of red blood cells. It rises with dehydration and falls with blood loss or reduced red cell production.",
                        "range": "38.3\u201348.6% (men) \u00b7 35.5\u201344.9% (women)",
                    },
                ],
            },
            {
                "title": "Platelets",
                "intro": "Platelets are small cell fragments that help your blood clot. A CBC reports their count and sometimes their average size.",
                "markers": [
                    {
                        "name": "Platelet count",
                        "abbr": "PLT",
                        "desc": "The number of platelets per volume of blood. A low count (thrombocytopenia) can increase bleeding risk; a high count (thrombocytosis) may be reactive or, less commonly, related to a bone marrow condition.",
                        "range": "150,000\u2013400,000 /\u00b5L",
                    },
                    {
                        "name": "Mean platelet volume",
                        "abbr": "MPV",
                        "desc": "The average size of your platelets. Larger platelets are often younger and may indicate that your body is producing them faster to replace ones being used up.",
                        "range": "7.5\u201312.0 fL",
                    },
                ],
            },
            {
                "title": "Red cell indices",
                "intro": "Indices describe the size and hemoglobin content of your red blood cells. They help characterize the type of anemia if one is present.",
                "markers": [
                    {
                        "name": "Mean corpuscular volume",
                        "abbr": "MCV",
                        "desc": "The average size of a single red blood cell. A high MCV (macrocytic) can be associated with B12 or folate issues; a low MCV (microcytic) can be associated with iron-related conditions.",
                        "range": "80\u2013100 fL",
                    },
                    {
                        "name": "Mean corpuscular hemoglobin",
                        "abbr": "MCH",
                        "desc": "The average amount of hemoglobin in a single red blood cell. It usually tracks with MCV \u2014 small cells carry less hemoglobin, large cells carry more.",
                        "range": "27\u201333 pg",
                    },
                    {
                        "name": "Mean corpuscular hemoglobin concentration",
                        "abbr": "MCHC",
                        "desc": "The average concentration of hemoglobin within red blood cells. Low MCHC suggests the cells are paler than usual (hypochromic).",
                        "range": "32\u201336 g/dL",
                    },
                    {
                        "name": "Red cell distribution width",
                        "abbr": "RDW",
                        "desc": "Measures how much variation there is in the size of your red blood cells. A high RDW means your cells vary more in size, which can be an early sign that something is affecting red cell production.",
                        "range": "11.5\u201314.5%",
                    },
                ],
            },
            {
                "title": "What reference ranges actually mean",
                "intro": None,
                "paragraphs": [
                    "Reference ranges represent the middle 95% of results from a healthy population tested by that specific lab. They are not absolute cutoffs for health or disease. A value slightly outside the range does not automatically mean something is wrong, and a value inside the range does not guarantee everything is fine.",
                    "Ranges vary between labs because of differences in equipment, reagents, and the population samples used to establish them. Age, sex, altitude, hydration, and even the time of day can influence your results. This is why comparing your numbers against a single \u201cnormal\u201d value from the internet can be misleading.",
                    "The most useful way to interpret your CBC is in context: how do your values compare to your own previous results, and what does your doctor think given your symptoms and history?",
                ],
            },
            {
                "title": "Why one result alone is not the whole picture",
                "intro": None,
                "points": [
                    {
                        "title": "Values interact with each other",
                        "desc": "A low hemoglobin means more when MCV is also low (suggesting a possible iron-related cause) than when MCV is normal. Individual numbers gain meaning from the pattern they form together.",
                    },
                    {
                        "title": "Temporary factors matter",
                        "desc": "Dehydration, a recent meal, intense exercise, stress, or medication can shift your numbers for hours or days. One slightly out-of-range result is often repeated before any conclusion is drawn.",
                    },
                    {
                        "title": "Trends are more informative than snapshots",
                        "desc": "A hemoglobin of 12.0 g/dL means something different if your last three results were 14.5, 13.8, and 12.8 than if they have been stable around 12.0 for years.",
                    },
                    {
                        "title": "Clinical context is essential",
                        "desc": "Your doctor interprets your CBC alongside your symptoms, medical history, physical exam, and other tests. A lab report alone \u2014 without that context \u2014 can be misleading.",
                    },
                ],
            },
            {
                "title": "When people want a clearer summary",
                "intro": None,
                "paragraphs": [
                    "Many people receive a CBC report and feel lost. The abbreviations are unfamiliar, the reference ranges are hard to compare, and there is no plain-language explanation included.",
                    "Some look up individual values online, but that gives scattered, generic answers without showing how the numbers relate to each other. Others wait for their doctor appointment, which may be days or weeks away.",
                    "A structured tool like NoryaAI can help bridge that gap. It reads your report, organizes the values into categories, flags anything outside the reference range, and provides plain-language context \u2014 all in a single, downloadable summary you can review on your own time or bring to your next appointment.",
                    "It does not replace your doctor. But it can make the conversation more productive.",
                ],
            },
        ],
        "mid_cta_title": "Have a CBC report you want to understand?",
        "mid_cta_sub": "Upload it and get a structured summary with plain-language explanations, flagged markers, and a health score.",
        "mid_cta_primary": "Upload your report",
        "mid_cta_secondary": "See a sample report",
        "faqs": [
            {
                "q": "What does CBC stand for?",
                "a": "CBC stands for complete blood count. It is a routine blood test that measures the cells in your blood \u2014 red blood cells, white blood cells, and platelets \u2014 along with related values like hemoglobin, hematocrit, and cell indices.",
            },
            {
                "q": "How often should I get a CBC?",
                "a": "There is no universal schedule. Many doctors include a CBC in annual checkups. It may be ordered more frequently if you have symptoms, a chronic condition, or are taking medication that affects blood cell counts. Your doctor will recommend the right frequency for you.",
            },
            {
                "q": "What does it mean if one value is slightly out of range?",
                "a": "A single value slightly outside the reference range is common and not always a cause for concern. Temporary factors like hydration, exercise, or stress can shift your numbers. Doctors typically look at the overall pattern and may repeat the test before drawing conclusions.",
            },
            {
                "q": "Can NoryaAI interpret my CBC results?",
                "a": "NoryaAI can read your CBC report, organize each marker with its reference range, flag values outside normal limits, and provide plain-language explanations. It does not diagnose conditions \u2014 it structures your results so they are easier to understand.",
            },
            {
                "q": "Is this guide a substitute for medical advice?",
                "a": "No. This guide is educational and intended to help you understand the components of a CBC report. It does not diagnose or recommend treatment. Always consult a qualified healthcare professional for medical decisions about your results.",
            },
            {
                "q": "Why do reference ranges differ between labs?",
                "a": "Labs use different equipment, reagents, and population samples to establish their ranges. Factors like age, sex, and geographic location also influence what is considered \u201cnormal.\u201d This is why the same result may be flagged at one lab but considered within range at another.",
            },
        ],
        "cta_title": "Ready to make sense of your CBC?",
        "cta_sub": "Upload your report and get a structured, easy-to-read summary \u2014 in minutes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "AI Blood Test Analyzer", "path": "/en/ai-blood-test-analyzer"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "How it works", "path": "/how-it-works"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }
    return templates.TemplateResponse("guide_landing.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/guides/how-to-read-cbc",
    })


@app.get("/en/tools/unit-converter", response_class=HTMLResponse)
def tool_en_unit_converter(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "Blood Test Unit Converter \u2014 Free mg/dL to mmol/L Tool | NoryaAI",
        "meta_description": "Convert blood test values between mg/dL, mmol/L, g/dL, \u00b5mol/L, and more. Free online converter for glucose, cholesterol, hemoglobin, creatinine, and other common biomarkers.",
        "hero_title": "Blood Test Unit Converter",
        "hero_sub": "Different labs, different countries, different units. Use this free tool to convert your blood test values between common measurement systems \u2014 instantly, with no signup required.",
        "disclaimer": "This tool performs standard unit conversions using published conversion factors. It does not provide medical advice, diagnosis, or interpretation. Always verify values with your lab report and consult a healthcare professional.",
        "table_title": "Supported conversions",
        "table_sub": "All conversion factors below are standard values used in clinical laboratory practice.",
        "soft_cta_title": "Need more than a conversion?",
        "soft_cta_sub": "Upload your full blood test report and get a structured summary with reference ranges, flagged markers, and plain-language explanations.",
        "soft_cta_primary": "Upload your report",
        "soft_cta_secondary": "See a sample report",
        "faqs": [
            {
                "q": "Why do blood test units differ between countries?",
                "a": "The United States primarily uses conventional units (mg/dL, g/dL), while most other countries use SI units (mmol/L, \u00b5mol/L, g/L). Both systems are scientifically valid \u2014 the difference is historical, not medical. This can be confusing when comparing results from labs in different countries.",
            },
            {
                "q": "What is the conversion factor for glucose?",
                "a": "To convert glucose from mg/dL to mmol/L, multiply by 0.05551. For example, 100 mg/dL equals approximately 5.6 mmol/L. To go in the other direction, divide by 0.05551.",
            },
            {
                "q": "Is this converter accurate?",
                "a": "This converter uses the same standard conversion factors used in clinical laboratory practice. The math is straightforward multiplication or division. However, always verify converted values against your original lab report.",
            },
            {
                "q": "What is the difference between mg/dL and mmol/L?",
                "a": "mg/dL (milligrams per deciliter) measures the weight of a substance in a given volume of blood. mmol/L (millimoles per liter) measures the number of molecules. They express the same measurement in different ways, and the conversion factor depends on the molecular weight of the specific substance.",
            },
            {
                "q": "Can I convert HbA1c between % and mmol/mol?",
                "a": "Yes. This tool supports the NGSP (%) to IFCC (mmol/mol) conversion using the standard formula: mmol/mol = (% \u00d7 10.929) \u2212 23.5. For example, an HbA1c of 7.0% equals approximately 53 mmol/mol.",
            },
            {
                "q": "Does this tool store my data?",
                "a": "No. All conversions happen entirely in your browser. No values are sent to any server, stored, or logged.",
            },
        ],
        "cta_title": "Want your full report analyzed?",
        "cta_sub": "Upload your blood test and get a structured, doctor-ready summary with all units, ranges, and explanations included.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "AI Blood Test Analyzer", "path": "/en/ai-blood-test-analyzer"},
            {"label": "How to Read a CBC", "path": "/en/guides/how-to-read-cbc"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }
    return templates.TemplateResponse("tool_unit_converter.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/tools/unit-converter",
    })


@app.get("/en/sample-blood-test-reports", response_class=HTMLResponse)
def landing_en_sample_reports(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "Sample Blood Test Reports \u2014 See What NoryaAI Produces | NoryaAI",
        "meta_description": "Preview sample blood test reports generated by NoryaAI. See how your results are structured with a health score, reference ranges, flagged markers, and plain-language explanations.",
        "hero_title": "Sample Blood Test Reports",
        "hero_sub": "Wondering what a NoryaAI report looks like before you upload? Browse sample reports below to see the structure, level of detail, and format you can expect.",
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "View pricing",
        "overview_title": "What every report includes",
        "overview_sub": "Each NoryaAI report follows the same structured format, regardless of the lab or language your original results are in.",
        "overview_items": [
            {"icon": "\U0001f4ca", "label": "Health score (0\u2013100)"},
            {"icon": "\U0001f6a9", "label": "Flagged markers"},
            {"icon": "\U0001f4cb", "label": "Category breakdown"},
            {"icon": "\U0001f4cf", "label": "Reference ranges"},
            {"icon": "\U0001f4d6", "label": "Plain-language explanations"},
            {"icon": "\U0001fa7a", "label": "Doctor-ready PDF"},
            {"icon": "\U0001f310", "label": "9+ languages"},
            {"icon": "\U0001f512", "label": "QR verification"},
        ],
        "samples_title": "Sample report previews",
        "samples_sub": "These illustrative examples show how NoryaAI structures different types of blood test panels. All values below are fictional and for demonstration only.",
        "sample_cards": [
            {
                "title": "Routine checkup \u2014 CBC + metabolic panel",
                "panel": "Complete blood count, glucose, kidney, liver",
                "score": 82,
                "score_label": "Good",
                "score_class": "bg-green-100 text-green-700",
                "lines": [
                    {"name": "Hemoglobin", "value": "14.2 g/dL (ref: 13.5\u201317.5)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "Glucose (fasting)", "value": "108 mg/dL (ref: 70\u2013100)", "status": "Elevated", "status_class": "bg-amber-50 text-amber-600"},
                    {"name": "Creatinine", "value": "0.9 mg/dL (ref: 0.7\u20131.3)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "ALT", "value": "28 U/L (ref: 7\u201335)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L (ref: 4.5\u201311.0)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                ],
                "note": "Illustrative data only. A real report includes all parsed markers, full explanations, and a downloadable PDF.",
            },
            {
                "title": "Thyroid panel",
                "panel": "TSH, Free T3, Free T4",
                "score": 74,
                "score_label": "Moderate",
                "score_class": "bg-amber-100 text-amber-700",
                "lines": [
                    {"name": "TSH", "value": "5.8 mIU/L (ref: 0.4\u20134.0)", "status": "Elevated", "status_class": "bg-amber-50 text-amber-600"},
                    {"name": "Free T4", "value": "1.1 ng/dL (ref: 0.8\u20131.8)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "Free T3", "value": "2.9 pg/mL (ref: 2.3\u20134.2)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                ],
                "note": "Illustrative data only. Your report would include a plain-language explanation of each value and its clinical context.",
            },
            {
                "title": "Lipid panel",
                "panel": "Total cholesterol, LDL, HDL, triglycerides",
                "score": 68,
                "score_label": "Moderate",
                "score_class": "bg-amber-100 text-amber-700",
                "lines": [
                    {"name": "Total cholesterol", "value": "228 mg/dL (ref: <200)", "status": "Elevated", "status_class": "bg-amber-50 text-amber-600"},
                    {"name": "LDL", "value": "148 mg/dL (ref: <100)", "status": "High", "status_class": "bg-red-50 text-red-600"},
                    {"name": "HDL", "value": "52 mg/dL (ref: >40)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "Triglycerides", "value": "165 mg/dL (ref: <150)", "status": "Elevated", "status_class": "bg-amber-50 text-amber-600"},
                ],
                "note": "Illustrative data only. A full report groups lipid values under a cardiovascular health category with explanations.",
            },
            {
                "title": "Vitamin & mineral panel",
                "panel": "Vitamin D, B12, Iron, Ferritin",
                "score": 71,
                "score_label": "Moderate",
                "score_class": "bg-amber-100 text-amber-700",
                "lines": [
                    {"name": "Vitamin D", "value": "18 ng/mL (ref: 30\u2013100)", "status": "Low", "status_class": "bg-red-50 text-red-600"},
                    {"name": "Vitamin B12", "value": "380 pg/mL (ref: 200\u2013900)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "Iron", "value": "65 \u00b5g/dL (ref: 60\u2013170)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "Ferritin", "value": "22 ng/mL (ref: 30\u2013300)", "status": "Low", "status_class": "bg-red-50 text-red-600"},
                ],
                "note": "Illustrative data only. Low markers are flagged with context about what they mean and when to discuss them with your doctor.",
            },
            {
                "title": "Comprehensive panel \u2014 multilingual output",
                "panel": "CBC + metabolic + thyroid + vitamins \u00b7 Report in German",
                "score": 77,
                "score_label": "Good",
                "score_class": "bg-green-100 text-green-700",
                "lines": [
                    {"name": "H\u00e4moglobin", "value": "13.8 g/dL (Ref: 12.0\u201316.0)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "Glukose (n\u00fcchtern)", "value": "95 mg/dL (Ref: 70\u2013100)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "TSH", "value": "3.2 mIU/L (Ref: 0.4\u20134.0)", "status": "Normal", "status_class": "bg-green-50 text-green-600"},
                    {"name": "Vitamin D", "value": "24 ng/mL (Ref: 30\u2013100)", "status": "Niedrig", "status_class": "bg-amber-50 text-amber-600"},
                ],
                "note": "Illustrative data only. This shows how the same structured format works when the report is generated in German.",
            },
        ],
        "expect_title": "What you can expect from your report",
        "expect_sub": "Every NoryaAI report is built to be useful, clear, and ready to share.",
        "expect_items": [
            {
                "icon": "\U0001f3af",
                "title": "Structured, not scattered",
                "desc": "Your results are grouped by category \u2014 blood cells, liver, kidney, thyroid, vitamins \u2014 instead of a flat list of numbers.",
            },
            {
                "icon": "\U0001f4ac",
                "title": "Written for people, not clinicians",
                "desc": "Each marker comes with a plain-language explanation of what it measures and whether your value is within the expected range.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Downloadable and shareable",
                "desc": "Your report is a clean PDF with a health score and QR verification. Print it, save it, or share it with your doctor.",
            },
        ],
        "doctor_title": "Bring your report to your next appointment",
        "doctor_sub": "A NoryaAI report is designed to make your doctor visit more productive \u2014 not to replace it.",
        "doctor_items": [
            {"icon": "\U0001f4c4", "text": "Clean PDF format"},
            {"icon": "\u2705", "text": "QR-verified output"},
            {"icon": "\U0001f5e3\ufe0f", "text": "Better questions for your doctor"},
            {"icon": "\U0001f310", "text": "Same format, any language"},
        ],
        "faqs": [
            {
                "q": "Are these real patient reports?",
                "a": "No. All values shown on this page are fictional and created for illustration only. They demonstrate the structure and format of a NoryaAI report, not actual patient data.",
            },
            {
                "q": "What panels can NoryaAI analyze?",
                "a": "NoryaAI supports most standard blood test panels including CBC, metabolic panels, liver and kidney function, thyroid, lipids, vitamins, iron studies, inflammation markers, and more. If your report contains values it can parse, they will be included.",
            },
            {
                "q": "Can I download the report as a PDF?",
                "a": "Yes. Every analysis generates a downloadable, printable PDF report with a health score, category breakdown, flagged markers, explanations, and QR verification.",
            },
            {
                "q": "Is the report available in other languages?",
                "a": "Yes. NoryaAI generates reports in 9+ languages including English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic. You choose the language when you start your analysis.",
            },
            {
                "q": "How accurate is the health score?",
                "a": "The health score is an educational summary based on how many of your values fall within reference ranges. It is not a clinical diagnosis. It gives you a quick overview of your results and highlights areas that may need attention.",
            },
            {
                "q": "Is NoryaAI a replacement for my doctor?",
                "a": "No. NoryaAI structures and explains your lab values to help you understand them better. It does not diagnose, treat, or prescribe. Always consult a qualified healthcare professional for medical decisions.",
            },
        ],
        "cta_title": "Ready to see your own report?",
        "cta_sub": "Upload your blood test and get a structured, doctor-ready summary in minutes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Analyze", "path": "/analyze"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "AI Blood Test Analyzer", "path": "/en/ai-blood-test-analyzer"},
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "How it works", "path": "/how-it-works"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }
    return templates.TemplateResponse("sample_reports_landing.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/sample-blood-test-reports",
    })


@app.get("/en/understand-blood-test-results-in-your-language", response_class=HTMLResponse)
def landing_en_multilingual(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "Understand Blood Test Results in Your Language | NoryaAI",
        "meta_description": "Got lab results in a language you don\u2019t fully understand? Upload your blood test and get a structured, easy-to-read report in English, German, Turkish, French, and 6 more languages.",
        "hero_title": "Understand Your Blood Test Results \u2014 in Your Language",
        "hero_sub": "Living abroad or dealing with a lab report in an unfamiliar language? Upload your results and get a clear, structured explanation in the language you are most comfortable with.",
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "See sample reports",
        "barrier_title": "Why language makes lab reports harder to understand",
        "barrier_sub": "A blood test is already difficult to read. When the report is in a language that is not your first, the challenge multiplies.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Medical terms you cannot look up easily",
                "desc": "Lab reports are full of abbreviations and clinical terms. When those terms are in another language, even a dictionary does not always help \u2014 medical vocabulary is specialized.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Different naming conventions",
                "desc": "The same blood test may have a different name, abbreviation, or panel grouping depending on the country. A \u201cBlutbild\u201d in Germany is a CBC in the US, but the structure can differ.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Units and ranges vary by region",
                "desc": "Is your glucose in mg/dL or mmol/L? Reference ranges and measurement systems differ between countries, making it harder to compare values you may have seen before.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Generic translators miss medical nuance",
                "desc": "Running a lab report through a general translator can produce awkward or misleading results. Medical context requires more than word-for-word translation.",
            },
        ],
        "helps_title": "How NoryaAI bridges the language gap",
        "helps_sub": "NoryaAI does not just translate your report. It reads, structures, and explains your results in the language you choose.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Upload in any language",
                "desc": "Your lab report can be in German, Turkish, Italian, French, or any supported language. Upload the PDF, photo, or paste the text.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI structures your data",
                "desc": "Values, units, and reference ranges are extracted and organized into clear categories \u2014 regardless of the original language.",
            },
            {
                "icon": "\U0001f310",
                "title": "Get your report in your language",
                "desc": "Choose the output language. Your structured summary, explanations, and health score are generated in the language you are most comfortable reading.",
            },
        ],
        "langs_title": "Supported report languages",
        "langs_sub": "Upload your lab results in any of these languages and receive your structured report in whichever you prefer.",
        "langs": [
            {"flag": "\U0001f1ec\U0001f1e7", "name": "English"},
            {"flag": "\U0001f1e9\U0001f1ea", "name": "Deutsch"},
            {"flag": "\U0001f1f9\U0001f1f7", "name": "T\u00fcrk\u00e7e"},
            {"flag": "\U0001f1eb\U0001f1f7", "name": "Fran\u00e7ais"},
            {"flag": "\U0001f1ee\U0001f1f9", "name": "Italiano"},
            {"flag": "\U0001f1ea\U0001f1f8", "name": "Espa\u00f1ol"},
            {"flag": "\U0001f1ee\U0001f1f1", "name": "\u05e2\u05d1\u05e8\u05d9\u05ea"},
            {"flag": "\U0001f1ee\U0001f1f3", "name": "\u0939\u093f\u0928\u094d\u0926\u0940"},
            {"flag": "\U0001f1f8\U0001f1e6", "name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"},
            {"flag": "\U0001f30d", "name": "More coming"},
        ],
        "who_title": "Who this is for",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Expats and immigrants",
                "desc": "You moved to a new country and got bloodwork done. The report is in the local language, but you think and understand health topics in your mother tongue.",
            },
            {
                "icon": "\U0001f393",
                "title": "International students",
                "desc": "Required health screenings at university often produce reports in the local language. A structured explanation in your own language helps you follow up.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Families across borders",
                "desc": "Your parent or partner got lab results in another country. Upload their report and generate a summary in the language you both understand.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Medical tourists and travelers",
                "desc": "Had bloodwork done while traveling or during a medical trip abroad? Get a structured summary you can share with your doctor at home.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Bilingual doctor visits",
                "desc": "You understand your doctor in one language but received your lab report in another. A single structured PDF in your preferred language can make the appointment smoother.",
            },
            {
                "icon": "\U0001f310",
                "title": "Anyone comparing international results",
                "desc": "If you have had bloodwork done in different countries, a unified structured format in one language makes it easier to track your values over time.",
            },
        ],
        "mid_cta_title": "Your lab report, your language",
        "mid_cta_sub": "Upload your blood test in any supported language and choose how you want to read the results.",
        "faqs": [
            {
                "q": "Can I upload a lab report in one language and get the results in another?",
                "a": "Yes. You can upload a report in any supported language \u2014 German, Turkish, French, Italian, and more \u2014 and choose a different language for your structured output. The values and reference ranges stay the same; the explanations are generated in your preferred language.",
            },
            {
                "q": "Is this a medical translation service?",
                "a": "No. NoryaAI does not provide certified medical translations. It reads your lab report, structures the data, and generates an educational explanation in the language you choose. For official or legal purposes, consult a certified medical translator.",
            },
            {
                "q": "Does the language affect the accuracy of the analysis?",
                "a": "No. The underlying analysis works with the numerical values, units, and reference ranges in your report. The language of the original document does not affect how the values are parsed or structured.",
            },
            {
                "q": "Which languages are supported?",
                "a": "NoryaAI currently supports English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic. More languages are being added over time.",
            },
            {
                "q": "Can I share the report with a doctor who speaks a different language?",
                "a": "Yes. You can generate the same report in multiple languages if needed. The structured PDF format is designed to be clear and useful regardless of the reader\u2019s medical background.",
            },
            {
                "q": "Is NoryaAI a replacement for my doctor?",
                "a": "No. NoryaAI provides structured, educational explanations to help you understand your lab results. It does not diagnose, treat, or prescribe. Always consult a qualified healthcare professional for medical decisions.",
            },
        ],
        "cta_title": "Ready to understand your results?",
        "cta_sub": "Upload your blood test in any language and get a clear, structured report in the one you prefer.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Analyze", "path": "/analyze"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "AI Blood Test Analyzer", "path": "/en/ai-blood-test-analyzer"},
            {"label": "Sample Reports", "path": "/en/sample-blood-test-reports"},
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }
    return templates.TemplateResponse("multilingual_landing.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/understand-blood-test-results-in-your-language",
    })


@app.get("/en/blood-test-results-germany", response_class=HTMLResponse)
def landing_en_blood_test_germany(request: Request):
    base_url = str(request.base_url).rstrip("/")
    t = {
        "meta_title": "Understanding Blood Test Results from Germany | NoryaAI",
        "meta_description": "Got a Blutbild or Laborwerte report from a German lab? Learn how to read German blood test results, common abbreviations, and how to get a structured English summary.",
        "badge": "Country Guide \u00b7 Germany",
        "hero_title": "Understanding Blood Test Results from Germany",
        "hero_sub": "If you have received a Blutbild, gro\u00dfes Blutbild, or Laborwerte report from a German lab, this guide explains what the abbreviations mean, how German reference ranges work, and how to get a clear summary in English.",
        "sections": [
            {
                "title": "How blood tests work in Germany",
                "intro": None,
                "paragraphs": [
                    "In Germany, blood tests are typically ordered by your Hausarzt (family doctor) or a specialist and processed by certified labs (Labore). Results are usually returned as a printed or digital Laborbericht \u2014 a structured document listing each measured parameter, its value, the unit, and the reference range.",
                    "Most reports are written entirely in German, using abbreviations and terminology that can be difficult to navigate if German is not your first language. Even fluent speakers sometimes struggle with the medical vocabulary.",
                    "If you are an expat, international student, or someone who moved to Germany recently, understanding your Laborwerte can feel unnecessarily complicated \u2014 especially when you need to discuss the results with a doctor or share them with a physician in your home country.",
                ],
            },
            {
                "title": "Common German blood test abbreviations",
                "intro": "German lab reports use abbreviations that differ from the English-language conventions you may be used to. Here are the most frequently encountered ones.",
                "markers": [
                    {"name": "Kleines Blutbild", "abbr": "KBB", "desc": "The equivalent of a CBC (complete blood count). Includes red cells, white cells, hemoglobin, hematocrit, and platelets.", "range": None},
                    {"name": "Gro\u00dfes Blutbild", "abbr": "GBB", "desc": "An extended blood count that adds a white cell differential (neutrophils, lymphocytes, monocytes, eosinophils, basophils) to the kleines Blutbild.", "range": None},
                    {"name": "Erythrozyten", "abbr": "ERY", "desc": "Red blood cells (RBC). Measured in millions per microliter (Mio/\u00b5L or T/L).", "range": "4.1\u20135.9 Mio/\u00b5L (men) \u00b7 3.9\u20135.4 (women)"},
                    {"name": "Leukozyten", "abbr": "LEUK", "desc": "White blood cells (WBC). Reported in thousands per microliter (Tsd/\u00b5L or G/L).", "range": "4.0\u201310.0 Tsd/\u00b5L"},
                    {"name": "H\u00e4moglobin", "abbr": "HB / HGB", "desc": "The oxygen-carrying protein in red blood cells. German labs typically report in g/dL, the same unit used in the US.", "range": "13.5\u201317.5 g/dL (men) \u00b7 12.0\u201316.0 (women)"},
                    {"name": "H\u00e4matokrit", "abbr": "HKT / HCT", "desc": "The percentage of blood volume occupied by red blood cells.", "range": "40\u201354% (men) \u00b7 36\u201348% (women)"},
                    {"name": "Thrombozyten", "abbr": "THRO / PLT", "desc": "Platelets. Reported in thousands per microliter (Tsd/\u00b5L).", "range": "150\u2013400 Tsd/\u00b5L"},
                    {"name": "Blutzucker (n\u00fcchtern)", "abbr": "GLU", "desc": "Fasting blood glucose. German labs commonly use mg/dL, though some use mmol/L.", "range": "70\u2013100 mg/dL (fasting)"},
                    {"name": "Kreatinin", "abbr": "KREA", "desc": "Creatinine \u2014 a kidney function marker. Usually reported in mg/dL in Germany.", "range": "0.7\u20131.3 mg/dL (men) \u00b7 0.6\u20131.1 (women)"},
                    {"name": "Leberwerte", "abbr": "GOT / GPT / GGT", "desc": "Liver enzymes. GOT is AST, GPT is ALT, GGT is gamma-GT. These are the most commonly checked liver markers in German bloodwork.", "range": "GOT <50 U/L \u00b7 GPT <50 U/L \u00b7 GGT <60 U/L (men)"},
                ],
            },
            {
                "title": "Units and reference ranges in German labs",
                "intro": None,
                "paragraphs": [
                    "German labs generally use the same conventional units as US labs for most markers (mg/dL for glucose and creatinine, g/dL for hemoglobin). However, some labs report in SI units (mmol/L for glucose, \u00b5mol/L for creatinine), especially in academic hospital settings.",
                    "Reference ranges (Referenzbereiche or Normwerte) can differ slightly between German labs, just as they do worldwide. Your report will typically show the lab\u2019s own range next to each value. Values outside the range are often marked with an arrow (\u2191 for high, \u2193 for low) or printed in bold.",
                    "If you are comparing results from a German lab with previous results from another country, pay close attention to the units. NoryaAI\u2019s free unit converter can help you translate between measurement systems.",
                ],
            },
            {
                "title": "What makes German lab reports different",
                "intro": None,
                "points": [
                    {"title": "Language barrier", "desc": "All parameter names, explanations, and doctor comments are in German. Even common terms like Schilddr\u00fcse (thyroid), Nierenwerte (kidney values), or Blutfettwerte (blood lipids) can be hard to look up without medical context."},
                    {"title": "GOT/GPT instead of AST/ALT", "desc": "German labs traditionally use GOT (Glutamat-Oxalacetat-Transaminase) and GPT (Glutamat-Pyruvat-Transaminase) instead of the international AST/ALT nomenclature. Both refer to the same liver enzymes."},
                    {"title": "Structured Laborbericht format", "desc": "German lab reports are typically well-organized with clear columns for Messwert (measured value), Einheit (unit), and Referenzbereich (reference range). But the medical terminology can still be opaque."},
                    {"title": "Krankenkasse context", "desc": "In the German healthcare system, certain tests are covered by public insurance (gesetzliche Krankenversicherung) and others require private payment (IGeL). This affects which panels appear on your report and how results are communicated to you."},
                ],
            },
            {
                "title": "How to get your German results explained in English",
                "intro": None,
                "paragraphs": [
                    "If you have a Laborbericht from a German lab and want to understand it in English, you have a few options. You can ask your doctor to walk you through the results \u2014 but appointments are often short, and the explanation may still be in German.",
                    "You can try translating the report yourself, but general translators often miss medical nuance. \u201cErh\u00f6ht\u201d means elevated, not just \u201cincreased,\u201d and \u201cauff\u00e4llig\u201d means \u201cabnormal / notable,\u201d not just \u201cconspicuous.\u201d",
                    "NoryaAI offers a different approach: upload your German lab report (PDF or photo), and it extracts the values, matches them to reference ranges, and generates a structured summary in English (or any of 9+ languages). The output includes a health score, flagged markers, plain-language explanations, and a downloadable PDF you can bring to your next appointment \u2014 whether that is in Germany or your home country.",
                ],
            },
        ],
        "mid_cta_title": "Have a German lab report you want to understand?",
        "mid_cta_sub": "Upload your Blutbild or Laborwerte and get a structured English summary with reference ranges, flagged markers, and a health score.",
        "mid_cta_primary": "Upload your report",
        "mid_cta_secondary": "See a sample report",
        "faqs": [
            {
                "q": "Can I upload a lab report written in German?",
                "a": "Yes. NoryaAI can read lab reports in German (and other supported languages). It extracts the values, units, and reference ranges regardless of the document language and generates your structured summary in whichever language you choose.",
            },
            {
                "q": "What is the difference between a kleines and gro\u00dfes Blutbild?",
                "a": "A kleines Blutbild (small blood count) is equivalent to a standard CBC: red cells, white cells, hemoglobin, hematocrit, and platelets. A gro\u00dfes Blutbild (large blood count) adds a white cell differential, breaking WBC into neutrophils, lymphocytes, monocytes, eosinophils, and basophils.",
            },
            {
                "q": "Why does my German report say GOT/GPT instead of AST/ALT?",
                "a": "German labs traditionally use the older nomenclature: GOT (Glutamat-Oxalacetat-Transaminase) for AST and GPT (Glutamat-Pyruvat-Transaminase) for ALT. They measure the same liver enzymes. NoryaAI recognizes both naming conventions.",
            },
            {
                "q": "Do German labs use different units?",
                "a": "Most German labs use the same conventional units as US labs (mg/dL, g/dL, U/L). Some academic hospitals use SI units (mmol/L, \u00b5mol/L). Your report will show which units are used. NoryaAI handles both systems automatically.",
            },
            {
                "q": "Can I share my English report with my German doctor?",
                "a": "Yes. The NoryaAI report includes a structured PDF with reference ranges, flagged markers, and a health score. You can also generate the report in German if your doctor prefers. The format is designed to be useful in any clinical setting.",
            },
            {
                "q": "Is this a certified medical translation?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not provide certified medical translations. For official or legal purposes, consult a certified medical translator. Always discuss your results with a qualified healthcare professional.",
            },
        ],
        "cta_title": "Ready to understand your German lab report?",
        "cta_sub": "Upload your Blutbild or Laborwerte and get a clear, structured summary in English \u2014 in minutes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Understand Results in Your Language", "path": "/en/understand-blood-test-results-in-your-language"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "Unit Converter", "path": "/en/tools/unit-converter"},
            {"label": "Blutwerte verstehen (DE)", "path": "/de/blutwerte-verstehen"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }
    return templates.TemplateResponse("guide_landing.html", {
        "request": request,
        "lang": "en",
        "t": t,
        "base_url": base_url,
        "canonical_url": f"{base_url}/en/blood-test-results-germany",
    })


@app.get("/en/blood-test-results", response_class=HTMLResponse)
def seo_landing_en_blood_test(request: Request):
    return _render_seo_landing(request, "en", "blood-test-results")


@app.get("/en/understand-lab-results", response_class=HTMLResponse)
def seo_landing_en_understand_lab(request: Request):
    return _render_seo_landing(request, "en", "understand-lab-results")


# SEO: other languages "blood test results" & "understand lab results" intent
@app.get("/es/blood-test-results", response_class=HTMLResponse)
def seo_landing_es_blood_test(request: Request):
    return _render_seo_landing(request, "es", "blood-test-results")


@app.get("/es/understand-lab-results", response_class=HTMLResponse)
def seo_landing_es_understand_lab(request: Request):
    return _render_seo_landing(request, "es", "understand-lab-results")


@app.get("/fr/blood-test-results", response_class=HTMLResponse)
def seo_landing_fr_blood_test(request: Request):
    return _render_seo_landing(request, "fr", "blood-test-results")


@app.get("/fr/understand-lab-results", response_class=HTMLResponse)
def seo_landing_fr_understand_lab(request: Request):
    return _render_seo_landing(request, "fr", "understand-lab-results")


@app.get("/it/blood-test-results", response_class=HTMLResponse)
def seo_landing_it_blood_test(request: Request):
    return _render_seo_landing(request, "it", "blood-test-results")


@app.get("/it/understand-lab-results", response_class=HTMLResponse)
def seo_landing_it_understand_lab(request: Request):
    return _render_seo_landing(request, "it", "understand-lab-results")


@app.get("/he/blood-test-results", response_class=HTMLResponse)
def seo_landing_he_blood_test(request: Request):
    return _render_seo_landing(request, "he", "blood-test-results")


@app.get("/he/understand-lab-results", response_class=HTMLResponse)
def seo_landing_he_understand_lab(request: Request):
    return _render_seo_landing(request, "he", "understand-lab-results")


@app.get("/hi/blood-test-results", response_class=HTMLResponse)
def seo_landing_hi_blood_test(request: Request):
    return _render_seo_landing(request, "hi", "blood-test-results")


@app.get("/hi/understand-lab-results", response_class=HTMLResponse)
def seo_landing_hi_understand_lab(request: Request):
    return _render_seo_landing(request, "hi", "understand-lab-results")


@app.get("/ar/blood-test-results", response_class=HTMLResponse)
def seo_landing_ar_blood_test(request: Request):
    return _render_seo_landing(request, "ar", "blood-test-results")


@app.get("/ar/understand-lab-results", response_class=HTMLResponse)
def seo_landing_ar_understand_lab(request: Request):
    return _render_seo_landing(request, "ar", "understand-lab-results")


# SEO: robots.txt ve sitemap.xml — catch-all /{lang} rotasından ÖNCE tanımlanmalı (yoksa /sitemap.xml -> 404)
@app.get("/robots.txt", response_class=PlainTextResponse)
def robots_txt(request: Request):
    """SEO: Allow all; Disallow admin ve 401 dönen path'ler; sitemap canonical URL."""
    base_url = str(request.base_url).rstrip("/")
    return PlainTextResponse(
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        "Disallow: /analyze/history\n"
        "Disallow: /analyze/usage\n"
        "Disallow: /analyze/export\n"
        "Disallow: /enterprise/\n"
        "Disallow: /pay\n"
        "Disallow: /payment\n"
        "Disallow: /verify/\n"
        f"\nSitemap: {base_url}/sitemap.xml\n",
        media_type="text/plain",
    )


@app.get("/sitemap.xml", response_class=PlainTextResponse)
def sitemap_xml(request: Request):
    """
    XML sitemap: ana sayfa, kurumsal, yasal, blog listeleri ve tüm blog yazıları.
    - /en/blog, /de/blog, /it/blog, /fr/blog index sayfaları (ve BLOG_LANGS_PREMIUM) dahil.
    - Tüm blog post URL'leri (tüm diller) otomatik eklenir.
    - lastmod = makale updatedAt (last_updated), yoksa published_at.
    """
    base_url = str(request.base_url).rstrip("/")
    urls: list[str] = []

    def add(loc: str, priority: str = "0.8", changefreq: str = "weekly", lastmod: str | None = None):
        last = f"<lastmod>{lastmod}</lastmod>" if lastmod else ""
        urls.append(f"  <url><loc>{loc}</loc>{last}<changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>")

    from datetime import date
    today = date.today().isoformat()

    # Ana sayfa (root) ve dil bazlı landing sayfaları (SEO: /de, /tr, /en vb.)
    add(f"{base_url}/", priority="0.9", lastmod=today)
    for locale in LANDING_ROUTES:
        add(f"{base_url}/{locale}", priority="0.9", lastmod=today)
    add(f"{base_url}/pricing", priority="0.8", lastmod=today)
    add(f"{base_url}/how-it-works", priority="0.8", lastmod=today)
    add(f"{base_url}/about", priority="0.6", changefreq="monthly", lastmod=today)
    add(f"{base_url}/science", priority="0.6", changefreq="monthly", lastmod=today)
    add(f"{base_url}/security", priority="0.6", changefreq="monthly", lastmod=today)
    add(f"{base_url}/technology", priority="0.6", changefreq="monthly", lastmod=today)
    add(f"{base_url}/de/faq", priority="0.7", changefreq="monthly", lastmod=today)
    add(f"{base_url}/kurumsal", lastmod=today)
    for page in LEGAL_PAGES:
        add(f"{base_url}/legal/{page}", priority="0.5", lastmod=today)

    # SEO landing pages (high-intent): /tr/kan-tahlili-sonucu, /en/blood-test-results, vb.
    for loc_lang, loc_slug in iter_seo_landing_urls():
        add(f"{base_url}/{loc_lang}/{loc_slug}", priority="0.8", changefreq="monthly", lastmod=today)

    # Compare pages
    add(f"{base_url}/en/compare/norya-vs-generic-ai", priority="0.7", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/why-not-generic-ai-for-blood-test-results", priority="0.7", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/upload-blood-test-results", priority="0.8", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/blood-test-results-explained", priority="0.8", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/guides/how-to-read-cbc", priority="0.7", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/tools/unit-converter", priority="0.7", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/sample-blood-test-reports", priority="0.8", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/understand-blood-test-results-in-your-language", priority="0.8", changefreq="monthly", lastmod=today)
    add(f"{base_url}/en/blood-test-results-germany", priority="0.7", changefreq="monthly", lastmod=today)

    # Blog listeleri: /en/blog, /de/blog, /it/blog, /fr/blog dahil (BLOG_LANGS_PREMIUM)
    for lang in BLOG_LANGS_PREMIUM:
        add(f"{base_url}/{lang}/blog", priority="0.8", lastmod=today)
    # Blog yazıları (tüm diller): lastmod = updatedAt (last_updated) veya published_at
    for item in iter_all_article_paths():
        loc = f"{base_url}/{item['lang']}/blog/{item['slug']}"
        lastmod = (item.get("last_updated") or item["published_at"]).isoformat()
        add(loc, priority="0.7", lastmod=lastmod)

    body = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    body += "\n".join(urls)
    body += "\n</urlset>"
    return PlainTextResponse(content=body, media_type="application/xml")


# Path-based locale: /en, /tr, /en/pricing, /de/report — SPA index.html (dil dropdown navigate için)
SUPPORTED_LOCALES = frozenset({"en", "de", "it", "fr", "es", "tr", "ar", "hi", "he", "el", "sr"})


@app.get("/{lang}", response_class=HTMLResponse)
def index_with_locale(request: Request, lang: str):
    """Locale prefix tek segment: /en, /tr → SPA."""
    if lang.lower() in SUPPORTED_LOCALES:
        return _index_response(request)
    raise HTTPException(status_code=404, detail="Not Found")


_KNOWN_SPA_PATHS = frozenset({
    "upload", "report", "results", "history", "settings", "profile",
    "payment", "pay", "checkout", "success", "share",
})


@app.get("/{lang}/{path:path}", response_class=HTMLResponse)
def index_with_locale_path(request: Request, lang: str, path: str):
    """Locale prefix + path: /en/pricing, /de/report → SPA (blog hariç; /{lang}/blog ayrı route).

    Özel durumlar:
    - /{lang}/pricing       -> /pricing?lang={lang}
    - /{lang}/how-it-works  -> /how-it-works?lang={lang}
    - /{lang}/analyze       -> /analyze?lang={lang}
    - /{lang}/faq           -> /{lang}#faq

    SEO: Bilinmeyen path'lerde noindex enjekte edilir (duplicate content önleme).
    """
    lang_l = (lang or "").strip().lower()
    if lang_l in SUPPORTED_LOCALES:
        path_l = (path or "").strip().lower().strip("/")
        if path_l == "pricing":
            return RedirectResponse(url=f"/pricing?lang={lang_l}", status_code=301)
        if path_l == "how-it-works":
            return RedirectResponse(url=f"/how-it-works?lang={lang_l}", status_code=301)
        if path_l == "analyze":
            return RedirectResponse(url=f"/analyze?lang={lang_l}", status_code=301)
        if path_l == "faq":
            return RedirectResponse(url=f"/{lang_l}#faq", status_code=302)
        first_segment = path_l.split("/")[0] if path_l else ""
        if first_segment not in _KNOWN_SPA_PATHS:
            raise HTTPException(status_code=404, detail="Not Found")
        return _index_response(request)
    raise HTTPException(status_code=404, detail="Not Found")
