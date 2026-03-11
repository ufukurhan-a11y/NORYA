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
from fastapi.templating import Jinja2Templates
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from sqlalchemy import or_, text
from sqlmodel import Session, select

from app.admin import admin_router as new_admin_router
from app.api.admin import get_admin_html, router as admin_router
from app.api.auth import router as auth_router
from app.api.deps import get_current_user, get_current_user_optional, security
from app.cache_db import cache_get, cache_set, get_conn as get_cache_conn, init_cache as init_ai_cache, purge_expired as purge_ai_cache_expired
from app.cache_utils import expires_iso, make_cache_key, now_iso
from app.core.config import is_openai_configured, settings
from app.core.database import engine, get_db, init_db
from app.core.rate_limit import limiter
from app.core.geo import get_country_from_ip
from app.legal_i18n import get_legal_content, get_legal_ui
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
from app.base_i18n import get_base_ui
from app.landing_i18n import (
    LANDING_ROUTES,
    get_landing_meta,
    get_landing_ui,
)
from app.pay_i18n import get_pay_ui, get_plan_display_name, get_plan_benefits
from app.blog_i18n import BLOG_LANGS, BLOG_LANGS_PREMIUM, BLOG_UI, DEFAULT_BLOG_LANG, get_article, get_related_articles, iter_all_article_paths, list_articles_for_lang
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    _seed_pricing_plan()
    _seed_default_coupon()
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
    yield


app = FastAPI(
    title="Norya API",
    description="Kan tahlili açıklama SaaS API",
    lifespan=lifespan,
)

# Statik dosyalar: proje kökünde /static klasöründen servis edilir
app.mount("/static", StaticFiles(directory="static"), name="static")
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


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    if exc.status_code == 429:
        detail = exc.detail if isinstance(exc.detail, str) else "Rate limit exceeded. Please try again later."
        return JSONResponse(
            status_code=429,
            content={"error": "Too many requests", "detail": detail},
        )
    return _error_response(request, exc.status_code, exc.detail if isinstance(exc.detail, str) else str(exc.detail))


@app.exception_handler(Exception)
def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
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
    return JSONResponse(status_code=500, content={"error": user_msg})


@app.middleware("http")
async def security_headers(request: Request, call_next):
    """Production güvenlik başlıkları: CSP, X-Content-Type-Options, X-Frame-Options, HSTS (HTTPS)."""
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    if getattr(settings, "environment", "development") == "production":
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
        # API + form + inline script + cdn + Google Analytics (gtag) için CSP
        _csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.tailwindcss.com https://www.googletagmanager.com; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data: blob: https:; "
            "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com; frame-ancestors 'self';"
        )
        response.headers["Content-Security-Policy"] = _csp
    return response


@app.middleware("http")
async def inject_tracking_ids(request: Request, call_next):
    """Şablonlarda kullanılmak üzere GA ve Google Ads kimliklerini request.state'e yazar."""
    request.state.ga_measurement_id = (getattr(settings, "ga_measurement_id", "") or "").strip()
    request.state.google_ads_conversion_id = (getattr(settings, "google_ads_conversion_id", "") or "").strip()
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


def _inject_ga(html: str) -> str:
    """GA_MEASUREMENT_ID ve/veya GOOGLE_ADS_CONVERSION_ID doluysa gtag script'ini <!-- GA_INJECT --> yerine koyar; ikisi de boşsa siler."""
    ga_id = (getattr(settings, "ga_measurement_id", "") or "").strip()
    aw_id = (getattr(settings, "google_ads_conversion_id", "") or "").strip()
    if not ga_id and not aw_id:
        inject = ""
    else:
        first_id = ga_id or aw_id
        configs = []
        if ga_id:
            configs.append(f'gtag("config","{ga_id}");')
        if aw_id:
            configs.append(f'gtag("config","{aw_id}");')
        inject = (
            f'<script async src="https://www.googletagmanager.com/gtag/js?id={first_id}"></script>\n'
            f'  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());{" ".join(configs)}</script>\n  '
        )
    return html.replace("<!-- GA_INJECT: .env GA_MEASUREMENT_ID=G-XXX ile GA4 eklenir -->", inject)


def _whatsapp_url_and_style() -> tuple[str, str]:
    """WhatsApp iletişim: (href, style). Numara yoksa varsayılan kullanılır, yine de gizlenmez."""
    num = (getattr(settings, "whatsapp_contact", None) or "905071703564").strip().replace("+", "").replace(" ", "")
    if not num or len(num) < 10:
        num = "905071703564"
    text = quote("Merhaba, Norya hakkında soru sormak istiyorum.")
    return f"https://wa.me/{num}?text={text}", ""


def _inject_whatsapp(html: str) -> str:
    """__NORYA_WHATSAPP_URL__ ve __NORYA_WHATSAPP_STYLE__ placeholder'larını doldurur."""
    url, style = _whatsapp_url_and_style()
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


LEGAL_PAGES = {
    "mesafeli-satis-sozlesmesi",
    "gizlilik-politikasi",
    "iade-iptal-politikasi",
    "kvkk-gdpr",
    "kullanim-sartlari",
    "iletisim",
}


def _legal_lang_from_request(request: Request) -> str:
    """Yasal sayfa dili: önce ?lang=, yoksa Accept-Language."""
    lang_q = request.query_params.get("lang", "").strip().lower()
    if lang_q:
        return lang_q[:5]
    return _parse_accept_language(request.headers.get("accept-language"))


PAYMENT_LANGS = ("tr", "en", "de", "fr", "it", "es")


def _payment_lang_from_request(request: Request) -> str:
    """Ödeme sayfası dili: sitede seçilen dil (cookie) veya ?lang= veya tarayıcı dili."""
    lang_q = (request.query_params.get("lang") or "").strip().lower()[:2]
    if lang_q in PAYMENT_LANGS:
        return lang_q
    lang_cookie = (request.cookies.get("norya_lang") or "").strip().lower()[:2]
    if lang_cookie in PAYMENT_LANGS:
        return lang_cookie
    browser = _parse_accept_language(request.headers.get("accept-language"))
    return browser if browser in PAYMENT_LANGS else "tr"


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
    if page == "iletisim":
        return templates.TemplateResponse(
            "legal/legal_contact.html",
            {"request": request, "content": content, "canonical_url": canonical_url, **ui},
        )
    return templates.TemplateResponse(
        "legal/legal_article.html",
        {"request": request, "content": content, "canonical_url": canonical_url, **ui},
    )


@app.get("/iade-iptal", response_class=HTMLResponse)
def iade_iptal_page(request: Request):
    """İade ve İptal Politikası — müşteri diline göre (?lang= veya Accept-Language)."""
    lang = _legal_lang_from_request(request)
    ui = get_legal_ui(lang)
    content = get_legal_content("iade-iptal-politikasi", lang)
    if not content:
        raise HTTPException(status_code=404, detail="Sayfa bulunamadı")
    base_url = str(request.base_url).rstrip("/")
    return templates.TemplateResponse(
        "legal/legal_article.html",
        {"request": request, "content": content, "canonical_url": f"{base_url}/iade-iptal", **ui},
    )


REFUND_LANGS = ("tr", "en", "de", "fr", "it", "es")


def _refund_lang_from_request(request: Request) -> str:
    """İade talebi dili: önce ?lang=, yoksa tarayıcı Accept-Language."""
    lang_q = request.query_params.get("lang", "").strip().lower()[:2]
    if lang_q and lang_q in REFUND_LANGS:
        return lang_q
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
            "canonical_url": f"{base_url}/iade-talebi",
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
    if lang not in ("tr", "en", "de", "fr", "it", "es"):
        lang = "tr"
    t = get_pay_ui(lang)
    ui = get_legal_ui(lang)

    merchant_oid = (merchant_oid or "").strip()
    email = (email or "").strip()
    reason = (reason or "").strip()[:500]

    base_url = str(request.base_url).rstrip("/")
    canonical = f"{base_url}/iade-talebi"
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
    ui = BLOG_UI.get(lang, BLOG_UI["en"])
    seo_title = ui.get("seo_title", f"{BRAND_NAME} Blog")
    meta_description = ui.get("meta_description", "")
    og_image = base_url + "/static/images/blog/how-to-read-blood-test-results.png"
    hreflang_alternates = [{"lang": code, "url": f"{base_url}/{code}/blog"} for code in BLOG_LANGS_PREMIUM]
    base_ui = get_base_ui(lang)
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
            "hreflang_alternates": hreflang_alternates,
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

    lang_alternates: dict[str, dict] = {}
    for code, s in art["available_langs"].items():
        if code in BLOG_LANGS_PREMIUM:
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

    blog_ui = BLOG_UI.get(lang, BLOG_UI["en"])
    base_ui = get_base_ui(lang)
    related_posts = get_related_articles(lang, art["id"], base_url, limit=4)

    return templates.TemplateResponse(
        "blog/detail.html",
        {
            "request": request,
            "article": art,
            "canonical_url": canonical_url,
            "cover_absolute": cover_absolute,
            "toc": toc,
            "current_lang": lang,
            "lang_alternates": lang_alternates,
            "hreflang_alternates": hreflang_alternates,
            "article_schema_json": article_schema_json,
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
    return JSONResponse(content={"ok": True})


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
    if getattr(settings, "ga_measurement_id", "") or getattr(settings, "google_ads_conversion_id", ""):
        raw = _inject_ga(raw)
    raw = _inject_whatsapp(raw)
    raw = _inject_company(raw)

    base_url = str(request.base_url).rstrip("/")
    canonical_url = f"{base_url}/{locale}"
    raw = _inject_canonical(raw, canonical_url)

    meta = get_landing_meta(locale)
    ui = get_landing_ui(locale)
    title = escape(meta.get("meta_title", "Norya"))
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

    hreflang_lines = [
        f'  <link rel="alternate" hreflang="tr" href="{base_url}/tr" />',
        f'  <link rel="alternate" hreflang="en" href="{base_url}/en" />',
        f'  <link rel="alternate" hreflang="en-CA" href="{base_url}/en-ca" />',
        f'  <link rel="alternate" hreflang="de" href="{base_url}/de" />',
        f'  <link rel="alternate" hreflang="it" href="{base_url}/it" />',
        f'  <link rel="alternate" hreflang="x-default" href="{base_url}/en" />',
    ]
    hreflang_block = "\n".join(hreflang_lines)
    raw = re.sub(
        r'  <link rel="alternate" hreflang="[^"]*" href="[^"]*" */?>\s*(?:  <link rel="alternate" hreflang="[^"]*" href="[^"]*" */?>\s*)*',
        hreflang_block + "\n  ",
        raw,
        count=1,
    )

    lang_attr = "en" if locale == "en-ca" else locale
    raw = re.sub(r'<html lang="[^"]*"', f'<html lang="{lang_attr}"', raw, count=1)

    landing_script = (
        f'<script>window.__LANDING_LOCALE__="{escape(locale)}";'
        f"window.__LANDING_T__={json.dumps(ui, ensure_ascii=False)};</script>\n  "
    )
    raw = raw.replace("</head>", landing_script + "</head>", 1)

    return HTMLResponse(
        raw,
        headers={"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache"},
    )


def _index_response(request: Request | None = None):
    """Ana sayfa içeriği: static/index.html veya fallback JSON. GET ve POST / için ortak. request verilirse canonical enjekte edilir."""
    index_file = STATIC_DIR / "index.html"
    if not index_file.is_file():
        index_file = Path.cwd() / "static" / "index.html"
    if index_file.is_file():
        raw = index_file.read_text(encoding="utf-8")
        if getattr(settings, "ga_measurement_id", "") or getattr(settings, "google_ads_conversion_id", ""):
            raw = _inject_ga(raw)
        raw = _inject_whatsapp(raw)
        raw = _inject_company(raw)
        if request is not None:
            base_url = str(request.base_url).rstrip("/")
            canonical_url = base_url + request.url.path
            raw = _inject_canonical(raw, canonical_url)
        return HTMLResponse(
            raw,
            headers={"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache"},
        )
    return {"durum": "hazır", "servis": "norya-api", "mesaj": "static/index.html bulunamadı. Proje kökünden çalıştırın: uvicorn app.main:app --reload"}


@app.get("/report")
def report_page(request: Request):
    """Rapor sayfası: /report?rid=... — aynı SPA, rid query ile rapor yüklenir."""
    index_file = STATIC_DIR / "index.html"
    if not index_file.is_file():
        index_file = Path.cwd() / "static" / "index.html"
    if index_file.is_file():
        raw = index_file.read_text(encoding="utf-8")
        if getattr(settings, "ga_measurement_id", "") or getattr(settings, "google_ads_conversion_id", ""):
            raw = _inject_ga(raw)
        raw = _inject_whatsapp(raw)
        raw = _inject_company(raw)
        base_url = str(request.base_url).rstrip("/")
        raw = _inject_canonical(raw, f"{base_url}/report")
        return HTMLResponse(
            raw,
            headers={"Cache-Control": "public, max-age=0, must-revalidate"},
        )
    return {"durum": "hazır", "servis": "norya-api", "mesaj": "static/index.html bulunamadı."}


@app.get("/analyze", response_class=HTMLResponse)
def analyze_landing():
    """
    /analyze -> SPA içindeki analiz bölümüne yönlendir.
    Blog CTA&apos;ları bu URL&apos;yi kullanır.
    """
    return RedirectResponse(url="/#analyze", status_code=302)


@app.get("/pricing", response_class=HTMLResponse)
def pricing_landing(request: Request):
    """
    /pricing -> Premium ödeme sayfasına (/payment) yönlendir.
    Plan seçimi ve PayTR iFrame /payment sayfasında yapılır.
    """
    query = request.url.query
    target = "/payment" + ("?" + query if query else "")
    return RedirectResponse(url=target, status_code=302)


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


def _audit(db: Session, event: str, user_id: int | None, ip: str | None) -> None:
    try:
        country = get_country_from_ip(ip) if ip else None
        db.add(AuditLog(event=event, user_id=user_id, ip=ip, country=country))
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
) -> int:
    rec = AnalysisRecord(
        user_id=user_id,
        input_text=input_text,
        result_text=result_text,
        source=source,
        doctor_notes=doctor_notes,
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


@app.post("/analyze", response_model=AnalyzeResponse)
@limiter.limit("10/minute")
async def analyze(
    request: Request,
    user: User = Depends(get_current_user),
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
    plan = getattr(user, "plan", "free") or "free"
    if not test_mode:
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
            aid = _save_analysis(db, user.id or 0, text, result, "text", doctor_notes=doctor_notes)
            if job:
                job.status = "done"
                job.analysis_record_id = aid
                job.duration_ms = int((time.perf_counter() - t0) * 1000)
                db.add(job)
                db.commit()
            _audit(db, "analyze", user.id, _client_ip(request))
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
        aid = _save_analysis(db, user.id or 0, text, result, "text", doctor_notes=doctor_notes)
        if job:
            job.status = "done"
            job.analysis_record_id = aid
            job.duration_ms = int((time.perf_counter() - t0) * 1000)
            if usage:
                job.prompt_tokens = usage.get("prompt_tokens")
                job.completion_tokens = usage.get("completion_tokens")
            db.add(job)
            db.commit()
        _audit(db, "analyze", user.id, _client_ip(request))
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
    user: User = Depends(get_current_user),
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
    if not test_mode:
        _check_analyze_hourly_limit(user.id or 0)
        plan = getattr(user, "plan", "free") or "free"
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
    premium_pdf = PREMIUM_VISIBLE_FOR_FREE or plan in ("single", "monthly", "yearly", "pro")
    premium_trend = PREMIUM_VISIBLE_FOR_FREE or plan in ("monthly", "yearly", "pro")
    # Tek analiz ve aylık: ekranda tam rapor gösterme; önizleme + "Hepsini görmek için aylık veya yıllık abonelik alın" kapısı. Yıllık/pro = tam rapor.
    report_limited_preview = plan in ("free", "single", "monthly")
    overall = (risk_summary or {}).get("overall") or {}
    health_score = HealthScoreSchema(score=overall.get("score", 0), level=overall.get("level", "mid")) if risk_summary else None
    trend = _get_trend_for_user(db, user_id, exclude_analysis_id=aid) if premium_trend and user_id else None
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
            aid = _save_analysis(db, user_id, input_preview, result, "image")
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
            _audit(db, "analyze", user_id, _client_ip(request))
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
        aid = _save_analysis(db, user_id, text[:2000], result, "pdf")
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
        _audit(db, "analyze", user_id, _client_ip(request))
        plan = plan or (getattr(db.get(User, user_id), "plan", None) or "free")
        return _build_analyze_response(result, aid, report_payload.get("risk_summary"), plan, user_id, db, cached=False)
    except Exception as e:
        if ul:
            ul.status = "failed"
            ul.error_message = str(e)[:500]
            ul.duration_ms = int((time.perf_counter() - t0) * 1000)
            db.add(ul)
            db.commit()
        if save:
            last_job = db.exec(select(AnalysisJob).where(AnalysisJob.user_id == user_id).order_by(AnalysisJob.id.desc()).limit(1)).first()
            if last_job:
                last_job.status = "failed"
                last_job.error_message = str(e)[:500]
                db.add(last_job)
                db.commit()
        raise


@app.post("/analyze/upload-json", response_model=AnalyzeResponse)
async def analyze_upload_json(
    request: Request,
    body: UploadJsonRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Dosyayı base64 JSON ile alır (UI dışı / yedek). file_base64, filename, lang."""
    test_mode = _is_test_mode(request)
    if not test_mode:
        plan = getattr(user, "plan", "free") or "free"
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
    return _process_uploaded_content(
        content, body.filename or "upload", report_lang, user.id or 0, db, request, save=not test_mode,
        plan=getattr(user, "plan", None) or "free",
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
    return {
        "kullanilan": kullanilan,
        "limit": limit,
        "plan": plan,
        "extra_credits": extra,
        "first_analysis_free": total_ever == 0,
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
    user: User = Depends(get_current_user),
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
    use_pro_scope = (scope or "").strip().lower() == "pro"
    premium_pdf = use_pro_scope or PREMIUM_VISIBLE_FOR_FREE or plan in ("single", "monthly", "yearly", "pro")
    premium_trend = use_pro_scope or PREMIUM_VISIBLE_FOR_FREE or plan in ("monthly", "yearly", "pro")
    cache_key = (analysis_id, report_lang, "pro" if use_pro_scope else "std", plan or "free")
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
    verify_base_url = (getattr(settings, "backend_public_url", None) or "").strip().rstrip("/") or str(request.base_url).rstrip("/")
    verification_info = None
    if plan in ("single", "monthly", "yearly"):
        verification_info = get_or_create_verification(db, analysis_id, user_id, plan, report_lang, verify_base_url)
    try:
        pdf_bytes = build_report_pdf(
            result_text=rec.result_text or "",
            report_date=report_date,
            lang=report_lang,
            report_id=analysis_id,
            user_identifier=user.email if user else None,
            patient_name=user.full_name if user else None,
            plan_name="premium" if premium_pdf else (user.plan if user else None),
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
    premium_pdf = PREMIUM_VISIBLE_FOR_FREE or plan in ("single", "monthly", "yearly", "pro")
    premium_trend = PREMIUM_VISIBLE_FOR_FREE or plan in ("monthly", "yearly", "pro")
    trend_data = _get_trend_for_user(db, user_id, exclude_analysis_id=analysis_id) if premium_trend else None
    verify_base_url = (getattr(settings, "backend_public_url", None) or "").strip().rstrip("/") or str(request.base_url).rstrip("/")
    verification_info = get_or_create_verification(db, analysis_id, user_id, plan, report_lang, verify_base_url) if plan in ("single", "monthly", "yearly") else None
    try:
        if premium_pdf:
            pdf_bytes = build_report_pdf(
                result_text=rec.result_text or "",
                report_date=report_date,
                lang=report_lang,
                report_id=analysis_id,
                user_identifier=user.email if user else None,
                patient_name=user.full_name if user else None,
                plan_name="premium" if premium_pdf else (user.plan if user else None),
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
        log.exception("PayTR init failed")
        msg = (str(e) or "").strip()[:200]
        if not msg:
            msg = "Beklenmeyen sunucu hatası. Terminal veya Render loglarında 'PayTR init failed' arayın."
        raise HTTPException(
            status_code=500,
            detail=f"Ödeme başlatılamadı: {msg} (.env içinde PAYTR_MERCHANT_ID, PAYTR_MERCHANT_KEY, PAYTR_MERCHANT_SALT dolu mu kontrol edin.)",
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
                user = User(
                    email=email,
                    hashed_password=hash_password("guest_" + secrets.token_hex(32)),
                    full_name=(body.name or "").strip()[:200] or "",
                )
                db.add(user)
                db.commit()
                db.refresh(user)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Giriş yapın veya geçerli bir e-posta girin (email alanı zorunlu).",
        )

    user_id = user.id or 0
    merchant_oid = "norya" + uuid.uuid4().hex[:20]
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"

    order = PaymentOrder(
        merchant_oid=merchant_oid,
        user_id=user_id,
        product=product,
        amount_kurus=total_amount,
        currency=currency,
        status="pending",
        coupon_code_used=coupon_used,
        quantity=quantity,
    )
    db.add(order)
    try:
        db.commit()
    except Exception as e:
        log.exception("PayTR init: order insert failed")
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
    """Validate merchant_oid format; return stripped. Raises 400 if invalid."""
    oid = (merchant_oid or "").strip()
    if not oid or len(oid) < 10 or len(oid) > 128:
        raise HTTPException(status_code=400, detail="Geçersiz merchant_oid.")
    if not all(c.isalnum() or c in "-_" for c in oid):
        raise HTTPException(status_code=400, detail="Geçersiz merchant_oid formatı.")
    return oid


@app.get("/api/orders/status")
def order_status(
    request: Request,
    merchant_oid: str = Query(..., description="Sipariş merchant_oid"),
    db: Session = Depends(get_db),
):
    """Ödeme durumu: pending, paid, failed. Premium kilit açma ve success sayfası polling için.
    Response: merchant_oid, status (pending|paid|failed), is_premium_active, active_until?, plan_code?."""
    oid = _validate_merchant_oid(merchant_oid)
    stmt = select(PaymentOrder).where(PaymentOrder.merchant_oid == oid)
    order = db.exec(stmt).first()
    if not order:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı.")
    # Map backend "completed" -> "paid" for frontend contract
    status = order.status or "pending"
    status_out = "paid" if status == "completed" else status
    is_premium = status == "completed"
    plan_code = order.product if is_premium else None  # "single" | "monthly" | "yearly"
    resp = {
        "merchant_oid": order.merchant_oid,
        "status": status_out,
        "is_premium_active": is_premium,
        "plan_code": plan_code,
    }
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
    # Tek canonical domain (statik ve API istekleri)
    base_url = _paytr_canonical_base(request)
    plan_map = get_plan_code_to_product_cents(db)
    plans = []
    for code, (product, price_cents) in plan_map.items():
        plans.append({
            "code": code,
            "price": f"{price_cents / 100:.2f}",
            "price_cents": price_cents,
            "label_key": f"plan_{product}",
            "product": product,
            "best_value": product == "yearly",
        })
    _card_label_keys = {"single": "plan_card_single", "monthly": "plan_card_monthly", "yearly": "plan_card_yearly"}
    for p in plans:
        p["label"] = t.get(p["label_key"], p["code"])
        p["display_label"] = t.get(_card_label_keys.get(p["product"], p["label_key"]), p["label"])
        p["benefits"] = get_plan_benefits(p["product"], lang)
    user_logged_in = current_user is not None
    user_email = (current_user.email or "").strip() if current_user else ""
    user_name = (getattr(current_user, "full_name", None) or "").strip() if current_user else ""
    default_plan = next((p for p in plans if p.get("product") == "yearly"), plans[0] if plans else None)
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
            "base_url_js": json.dumps(base_url),
            "default_plan": default_plan,
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

    ok_url = (body.success_url or "").strip() or getattr(settings, "paytr_ok_url", "") or "/#analyze"
    fail_url = (body.cancel_url or "").strip() or getattr(settings, "paytr_fail_url", "") or "/#pricing"

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
    base_url = (str(request.base_url).rstrip("/") + "/").rstrip("/")
    if body.success_url:
        parts = body.success_url.split("#", 1)
        success_base = parts[0].rstrip("/") or base_url
        hash_part = (parts[1] if len(parts) > 1 else "") or "payment-ok"
    else:
        success_base = base_url
        hash_part = "payment-ok"
    merchant_ok_url = f"{success_base}#{hash_part}&guest_token={guest_token}"
    merchant_fail_url = (body.cancel_url or "").strip() or (base_url + "#pricing")
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

        if status == "success":
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
):
    """Başarılı ödeme sonrası sayfa. merchant_oid varsa polling ile premium aktivasyonu beklenir."""
    base = _paytr_canonical_base(request)
    api_base = base
    lang = (lang or "tr").lower()[:2]
    if lang not in ("tr", "en", "de", "fr", "it", "es"):
        lang = "tr"
    t = get_pay_ui(lang)
    title = t["success_title"]
    msg = t["success_message"]
    btn_text = t["success_btn"]
    updating = t.get("success_updating", "Hesabınız güncelleniyor…")
    premium_active = t.get("success_premium_active", "Premium aktif")
    pending_bank = t.get("success_pending_bank", "İşlem bankanızdan onay bekliyor olabilir.")
    failed_short = t.get("success_payment_failed_short", "Ödeme tamamlanamadı.")
    btn_report = t.get("success_btn_report", "Rapor sayfasına git")
    check_done_btn = t.get("success_check_done_btn", "Ödeme tamamlandı mı?")
    retry_text = t.get("failed_retry", "Tekrar dene")

    if not (merchant_oid and merchant_oid.strip()):
        html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><meta name="theme-color" content="#0f172a">
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
<body>
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
    report_url = f"{base}/report"
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><meta name="theme-color" content="#0f172a">
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
<body>
  <div class="card">
    <div id="iconWrap" class="ok">✓</div>
    <div id="spinnerWrap" class="spinner" style="display:none;"></div>
    <h1 id="titleEl">{title}</h1>
    <p id="statusMsg">{updating}</p>
    <div id="btnWrap" class="btns" style="display:none;">
      <a id="btnReport" href="{report_url}">{btn_report}</a>
      <a id="btnRetry" class="secondary" href="{base}/payment?lang={lang}" style="display:none;">{retry_text}</a>
    </div>
    <p style="margin-top:16px;"><button type="button" class="btn secondary" id="checkDoneBtn" style="background:transparent;border:2px solid rgba(14,165,164,0.5);color:#94a3b8;">{check_done_btn}</button></p>
  </div>
  <script>
(function(){{
  var apiBase = {json.dumps(api_base)};
  var oid = {json.dumps(oid)};
  var reportUrl = {json.dumps(report_url)};
  var updating = {json.dumps(updating)};
  var premiumActive = {json.dumps(premium_active)};
  var pendingBank = {json.dumps(pending_bank)};
  var failedShort = {json.dumps(failed_short)};
  var start = Date.now();
  var timeoutTotal = 90000;
  var intervalFast = 2000;
  var intervalSlow = 5000;
  var fastUntil = 30000;
  var pollTimer = null;
  var redirectTimer = null;

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
  function doPoll() {{
    var timeoutMsg = {json.dumps(t.get("success_timeout", "Zaman aşımı"))};
    if (Date.now() - start > timeoutTotal) {{ showSpinner(false); setStatus(updating + " (" + timeoutMsg + ")"); showButtons(true, false); return; }}
    fetch(apiBase + "/api/orders/status?merchant_oid=" + encodeURIComponent(oid))
      .then(function(r) {{ return r.status === 404 ? null : r.json(); }})
      .then(function(d) {{
        if (!d) {{ setStatus(updating); return; }}
        if (d.status === "paid" || d.is_premium_active) {{
          stopPolling();
          showSpinner(false);
          setStatus(premiumActive + " ✓", true);
          showButtons(true, false);
          redirectTimer = setTimeout(function() {{ window.location.href = reportUrl; }}, 1000);
          return;
        }}
        if (d.status === "failed") {{
          stopPolling();
          showSpinner(false);
          setStatus(failedShort);
          showButtons(false, true);
          return;
        }}
        setStatus(pendingBank);
      }})
      .catch(function() {{ setStatus(updating); }});
  }}
  function scheduleNext() {{
    if (Date.now() - start > timeoutTotal) return;
    var interval = (Date.now() - start) < fastUntil ? intervalFast : intervalSlow;
    pollTimer = setTimeout(function() {{ doPoll(); scheduleNext(); }}, interval);
  }}
  document.getElementById("checkDoneBtn").addEventListener("click", function() {{
    doPoll();
    if (pollTimer) {{ clearTimeout(pollTimer); scheduleNext(); }}
  }});
  showSpinner(true);
  doPoll();
  scheduleNext();
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


# Path-based locale: /en, /tr, /en/pricing, /de/report — SPA index.html (dil dropdown navigate için)
SUPPORTED_LOCALES = frozenset({"en", "de", "it", "fr", "es", "tr", "ar", "hi", "he", "el", "sr"})


@app.get("/{lang}", response_class=HTMLResponse)
def index_with_locale(request: Request, lang: str):
    """Locale prefix tek segment: /en, /tr → SPA."""
    if lang.lower() in SUPPORTED_LOCALES:
        return _index_response(request)
    raise HTTPException(status_code=404, detail="Not Found")


@app.get("/{lang}/{path:path}", response_class=HTMLResponse)
def index_with_locale_path(request: Request, lang: str, path: str):
    """Locale prefix + path: /en/pricing, /de/report → SPA (blog hariç; /{lang}/blog ayrı route)."""
    if lang.lower() in SUPPORTED_LOCALES:
        return _index_response(request)
    raise HTTPException(status_code=404, detail="Not Found")


@app.get("/robots.txt", response_class=PlainTextResponse)
def robots_txt():
    """SEO: Allow all; Disallow admin ve 401 dönen path'ler; sitemap canonical URL."""
    return PlainTextResponse(
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        "Disallow: /analyze/history\n"
        "Disallow: /analyze/usage\n"
        "Disallow: /analyze/export\n"
        "\nSitemap: https://noryaai.com/sitemap.xml\n",
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

    # Ana sayfa
    add(f"{base_url}/", priority="0.9", lastmod=today)
    add(f"{base_url}/kurumsal", lastmod=today)
    for page in LEGAL_PAGES:
        add(f"{base_url}/legal/{page}", priority="0.5", lastmod=today)

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
