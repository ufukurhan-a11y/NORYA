import base64
import json
import logging
import secrets
import time
import uuid
from datetime import datetime, timedelta, timezone
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

from dotenv import load_dotenv

# Uvicorn nereden çalışırsa çalışsın .env proje kökünden yüklensin (norya/)
_PROJ_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJ_ROOT / ".env")

from fastapi import Depends, FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles
from slowapi.errors import RateLimitExceeded
from sqlmodel import Session, select

from app.admin import admin_router as new_admin_router
from app.api.admin import get_admin_html, router as admin_router
from app.api.auth import router as auth_router
from app.api.deps import get_current_user
from app.core.config import settings
from app.core.database import engine, get_db, init_db
from app.core.rate_limit import limiter
from app.core.geo import get_country_from_ip
from app.core.security import hash_password
from app.models import (  # noqa: F401
    AnalysisJob,
    AnalysisRecord,
    AuditLog,
    ErrorLog,
    PaymentOrder,
    Presence,
    SecurityLog,
    UploadLog,
    EmailVerifyToken,
    GuestLoginToken,
    PasswordResetToken,
    ShareToken,
    User,
)
from app.services.report_pdf import build_report_pdf
from app.schemas.analyze import (
    AnalysisDetail,
    AnalysisHistoryItem,
    AnalyzeResponse,
    UploadJsonRequest,
)
from app.schemas.payment import CreateSessionRequest, GrantPaymentRequest, GuestSessionRequest
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

# Proje kökü: app/main.py -> app/ -> norya/
_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = _ROOT / "static"
UPLOADS_DIR = _ROOT / "data" / "uploads"  # Yüklenen orijinal belgeler (admin: hastanın gönderdiği)
# Çalışma dizininden de dene (uvicorn farklı yerden çalıştırılırsa)
if not STATIC_DIR.is_dir():
    STATIC_DIR = Path.cwd() / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    key_ok = bool((settings.openai_api_key or "").strip())
    log.info("OPENAI_API_KEY loaded: %s", "yes" if key_ok else "NO (.env dosyasına OPENAI_API_KEY=sk-... ekleyin)")
    yield


app = FastAPI(
    title="Norya API",
    description="Kan tahlili açıklama SaaS API",
    lifespan=lifespan,
)
app.state.limiter = limiter


def _error_response(request: Request, status_code: int, detail: str) -> JSONResponse:
    rid = getattr(request.state, "request_id", None)
    body = {"error": detail, "status_code": status_code}
    if rid:
        body["request_id"] = rid
    return JSONResponse(status_code=status_code, content=body)


def _rate_limit_handler(request: Request, exc: RateLimitExceeded) -> JSONResponse:
    try:
        ip = (request.headers.get("x-forwarded-for") or "").split(",")[0].strip() or (request.client.host if request.client else "")
        with Session(engine) as db:
            db.add(SecurityLog(event="rate_limit", ip=ip or None, endpoint=request.url.path, detail="Rate limit exceeded"))
            db.commit()
    except Exception as e:
        log.warning("SecurityLog rate_limit write failed: %s", e)
    return _error_response(request, 429, "Çok fazla istek. Lütfen bir dakika bekleyin.")


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


app.add_exception_handler(RateLimitExceeded, _rate_limit_handler)


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
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
app.include_router(auth_router)
app.include_router(new_admin_router)  # Yeni modüler admin (Jinja2); /admin/ -> dashboard
# GET /admin (slash yok) yeni panele yönlendir; eski admin'den önce kayıt edilmeli
@app.get("/admin")
def admin_redirect():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/admin/dashboard", status_code=302)

app.include_router(admin_router)  # Eski API paneli: /admin/stats, /admin/analyses, vb.


@app.get("/yonetim", response_class=HTMLResponse)
@app.get("/yonetim/", response_class=HTMLResponse)
def admin_yonetim():
    """Eski URL: /yonetim -> /admin yönlendir."""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/admin", status_code=302)


if STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/health")
def health():
    openai_configured = bool((getattr(settings, "openai_api_key", None) or "").strip())
    return {"status": "ok", "openai_configured": openai_configured}


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
EUR_BASE = {"single": 13, "monthly": 50, "yearly": 99}
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


def _pricing_response(currency: str, rate: float) -> dict:
    """Tek bir para birimi ve kur için fiyat yanıtı üretir."""
    symbol = CURRENCY_SYMBOLS.get(currency, currency + " ")
    decimals = 0 if currency in ("JPY", "KRW") else 2
    return {
        "currency": currency,
        "symbol": symbol,
        "single": round(EUR_BASE["single"] * rate, decimals),
        "monthly": round(EUR_BASE["monthly"] * rate, decimals),
        "yearly": round(EUR_BASE["yearly"] * rate, decimals),
        "note": "pricing_note_" + currency.lower(),
    }


@app.get("/api/pricing")
def get_pricing(request: Request, country: str | None = None):
    """
    Ziyaretçinin ülkesine göre fiyatları anlık kura göre yerel para biriminde döner.
    Kurlar Frankfurter API ile güncellenir (6 saat cache). Hata durumunda EUR fallback.
    ?country=TR ile TRY, country=US ile USD vb. override edilebilir.
    """
    try:
        country = (country or _get_country_from_request(request) or "DE").upper()[:2]
        currency = COUNTRY_TO_CURRENCY.get(country, "EUR")
        rates = _fetch_eur_rates_live()
        rate = float(rates.get(currency, EUR_RATES_FALLBACK.get(currency, 1.0)))
        return _pricing_response(currency, rate)
    except Exception:
        return _pricing_response("EUR", 1.0)


@app.get("/api-check")
def api_check():
    """OpenAI anahtarı yüklü mü kontrol et (anahtar gösterilmez)."""
    from app.core.config import settings
    key_ok = bool(settings.openai_api_key and settings.openai_api_key.startswith("sk-"))
    return {"openai_ayarli": key_ok, "mesaj": "Anahtar tanımlı." if key_ok else "OPENAI_API_KEY .env'de eksik veya geçersiz."}


@app.get("/")
def index():
    index_file = STATIC_DIR / "index.html"
    if not index_file.is_file():
        index_file = Path.cwd() / "static" / "index.html"
    if index_file.is_file():
        return FileResponse(str(index_file), media_type="text/html; charset=utf-8")
    return {"durum": "hazır", "servis": "norya-api", "mesaj": "static/index.html bulunamadı. Proje kökünden çalıştırın: uvicorn app.main:app --reload"}


# Ücretsiz planda: ilk analiz ücretsiz, sonrası için ödeme gerekir (ayda 1 hak)
AYLIK_LIMIT_UCRETSIZ = 1
# Pro planında limit yok (büyük sayı)
AYLIK_LIMIT_PRO = 999_999


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
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    return request.client.host if request.client else ""


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
    """Sınırsız test modu: X-Test-Mode: 1 header'ı veya ?test=1 query."""
    return (
        request.headers.get("X-Test-Mode") == "1"
        or request.query_params.get("test") == "1"
    )


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Metin analizi. JSON body veya form (text, doctor_notes, lang) — PDF/görsel akışı ile aynı form gönderimi desteklenir."""
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
        result = analyze_blood_test(text, detailed=True, doctor_notes=doctor_notes, lang=report_lang)
        if test_mode:
            return AnalyzeResponse(sonuc=result, analiz_id=None)
        aid = _save_analysis(db, user.id or 0, text, result, "text", doctor_notes=doctor_notes)
        if job:
            job.status = "done"
            job.analysis_record_id = aid
            job.duration_ms = int((time.perf_counter() - t0) * 1000)
            db.add(job)
            db.commit()
        _audit(db, "analyze", user.id, _client_ip(request))
        return AnalyzeResponse(sonuc=result, analiz_id=aid)
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
async def analyze_upload(
    request: Request,
    file: UploadFile = File(...),
    lang: str = Form("tr"),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Dosya yükleme: multipart/form-data, alan adı 'file' (zorunlu), 'lang' (opsiyonel)."""
    log.info("analyze/upload: filename=%s", getattr(file, "filename", ""))
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

    if not file.filename:
        raise HTTPException(status_code=400, detail="Dosya seçin.")
    ext = "." + file.filename.lower().rsplit(".", 1)[-1] if "." in file.filename else ""
    if ext not in ALLOWED_UPLOAD_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Sadece PDF, JPG veya PNG yükleyebilirsiniz.",
        )
    report_lang = _report_lang_from_request(request, lang)
    try:
        content = await file.read()
    except Exception as e:
        log.exception("analyze/upload file read error: %s", e)
        raise HTTPException(status_code=400, detail="Dosya okunamadı.")
    MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="Dosya en fazla 10 MB olabilir.")
    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Dosya boş.")
    try:
        return _process_uploaded_content(
            content, file.filename, report_lang, user.id or 0, db, request, save=not test_mode
        )
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log.exception("analyze/upload process error: %s", e)
        raise HTTPException(status_code=400, detail=f"Dosya işlenemedi: {str(e)[:80]}")


def _process_uploaded_content(
    content: bytes,
    filename: str,
    report_lang: str | None,
    user_id: int,
    db: Session,
    request: Request,
    save: bool = True,
) -> AnalyzeResponse:
    """Ortak: yüklenen dosya içeriğini analiz eder (görsel veya PDF). save=False ise kaydetmez (test modu)."""
    ext = "." + filename.lower().rsplit(".", 1)[-1] if "." in filename else ""
    if ext not in ALLOWED_UPLOAD_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Sadece PDF, JPG veya PNG yükleyebilirsiniz.")
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
            result = analyze_blood_test_from_image(content, mime, lang=report_lang)
            if not save:
                return AnalyzeResponse(sonuc=result, analiz_id=None)
            input_preview = f"[Görsel: {filename}]"
            aid = _save_analysis(db, user_id, input_preview, result, "image")
            if job:
                job.status = "done"
                job.analysis_record_id = aid
                job.duration_ms = int((time.perf_counter() - t0) * 1000)
                db.add(job)
                db.commit()
            _attach_original_file(db, aid, content, filename, "image")
            if ul:
                ul.status = "success"
                ul.duration_ms = int((time.perf_counter() - t0) * 1000)
                db.add(ul)
                db.commit()
            _audit(db, "analyze", user_id, _client_ip(request))
            return AnalyzeResponse(sonuc=result, analiz_id=aid)
        text = extract_text_from_pdf(content)
        if "çıkarılamadı" in text:
            raise HTTPException(status_code=400, detail="PDF'den metin okunamadı. Farklı bir dosya deneyin.")
        job = AnalysisJob(user_id=user_id, status="processing") if save else None
        if job:
            db.add(job)
            db.commit()
            db.refresh(job)
        result = analyze_blood_test(text, lang=report_lang)
        if not save:
            return AnalyzeResponse(sonuc=result, analiz_id=None)
        aid = _save_analysis(db, user_id, text[:2000], result, "pdf")
        if job:
            job.status = "done"
            job.analysis_record_id = aid
            job.duration_ms = int((time.perf_counter() - t0) * 1000)
            db.add(job)
            db.commit()
        _attach_original_file(db, aid, content, filename, "pdf")
        if ul:
            ul.status = "success"
            ul.duration_ms = int((time.perf_counter() - t0) * 1000)
            db.add(ul)
            db.commit()
        _audit(db, "analyze", user_id, _client_ip(request))
        return AnalyzeResponse(sonuc=result, analiz_id=aid)
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
        content, body.filename or "upload", report_lang, user.id or 0, db, request, save=not test_mode
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
):
    stmt = (
        select(AnalysisRecord)
        .where(AnalysisRecord.user_id == user.id)
        .order_by(AnalysisRecord.created_at.desc())
        .limit(limit)
    )
    rows = list(db.exec(stmt).all())
    return [
        AnalysisHistoryItem(
            id=r.id or 0,
            input_preview=(r.input_text[:120] + "…") if len(r.input_text) > 120 else r.input_text,
            result_preview=(r.result_text[:200] + "…") if len(r.result_text) > 200 else r.result_text,
            source=r.source,
            created_at=r.created_at.isoformat() if hasattr(r.created_at, "isoformat") else str(r.created_at),
        )
        for r in rows
    ]


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
    )


@app.get("/analyze/history/{analysis_id}/pdf")
def download_analysis_pdf(
    analysis_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """İlgili analizin premium PDF raporunu indirir (WeasyPrint + Jinja2)."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or rec.user_id != (user.id or 0):
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    report_date = None
    if getattr(rec, "created_at", None):
        dt = rec.created_at
        if hasattr(dt, "strftime"):
            report_date = dt.strftime("%d.%m.%Y %H:%M")
        else:
            report_date = str(dt)
    try:
        pdf_bytes = build_report_pdf(
            result_text=rec.result_text or "",
            report_date=report_date,
            lang="tr",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    filename = f"norya-rapor-{analysis_id}.pdf"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
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


# ---------- Ödeme: PayTR (Türkiye sanal pos), önce öde sonra analiz ----------
def _paytr_enabled() -> bool:
    return bool(
        getattr(settings, "paytr_merchant_id", None)
        and getattr(settings, "paytr_merchant_key", None)
        and getattr(settings, "paytr_merchant_salt", None)
    )


def _paytr_amount(product: str) -> int:
    if product == "single":
        return int(getattr(settings, "paytr_amount_single", 300) or 300)
    if product == "monthly":
        return int(getattr(settings, "paytr_amount_monthly", 5000) or 5000)
    if product == "yearly":
        return int(getattr(settings, "paytr_amount_yearly", 9900) or 9900)
    return 300


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
    if body.product not in ("single", "monthly", "yearly"):
        raise HTTPException(status_code=400, detail="Geçersiz ürün.")
    import base64
    import hmac
    import hashlib
    import json
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request as UrlRequest

    merchant_oid = f"norya_{user.id}_{int(datetime.now(timezone.utc).timestamp())}_{secrets.token_hex(4)}"
    amount = _paytr_amount(body.product)
    order = PaymentOrder(merchant_oid=merchant_oid, user_id=user.id or 0, product=body.product, amount_kurus=amount, currency=currency)
    db.add(order)
    db.commit()

    merchant_id = settings.paytr_merchant_id
    merchant_key = settings.paytr_merchant_key.encode() if isinstance(settings.paytr_merchant_key, str) else settings.paytr_merchant_key
    merchant_salt = settings.paytr_merchant_salt
    user_ip = _client_ip(request)
    email = user.email or ""
    product_name = {"single": "1 Analiz", "monthly": "Pro Aylık", "yearly": "Pro Yıllık"}[body.product]
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"
    user_basket = base64.b64encode(
        json.dumps([[product_name, f"{amount / 100:.2f}", 1]]).encode()
    ).decode()
    no_installment = "0"
    max_installment = "0"
    test_mode = getattr(settings, "paytr_test_mode", "0") or "0"

    hash_str = f"{merchant_id}{user_ip}{merchant_oid}{email}{amount}{user_basket}{no_installment}{max_installment}{currency}{test_mode}"
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
        "payment_amount": amount,
        "paytr_token": paytr_token,
        "user_basket": user_basket,
        "debug_on": "0",
        "no_installment": no_installment,
        "max_installment": max_installment,
        "user_name": (user.full_name or "")[:60],
        "user_address": "Norya ödeme",
        "user_phone": "",
        "merchant_ok_url": ok_url,
        "merchant_fail_url": fail_url,
        "timeout_limit": "30",
        "currency": currency,
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
        raise HTTPException(status_code=400, detail=result.get("reason", "PayTR token alınamadı."))
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
    merchant_oid = f"norya_guest_{user_id}_{int(datetime.now(timezone.utc).timestamp())}_{secrets.token_hex(4)}"
    amount = _paytr_amount("single")
    order = PaymentOrder(merchant_oid=merchant_oid, user_id=user_id, product="single", amount_kurus=amount, currency=currency)
    db.add(order)
    guest_token = secrets.token_hex(32)
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    guest_login = GuestLoginToken(token=guest_token, user_id=user_id, expires_at=expires_at)
    db.add(guest_login)
    db.commit()

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
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"
    user_basket = base64.b64encode(json.dumps([[product_name, f"{amount / 100:.2f}", 1]]).encode()).decode()
    no_installment = "0"
    max_installment = "0"
    test_mode = getattr(settings, "paytr_test_mode", "0") or "0"
    hash_str = f"{merchant_id}{user_ip}{merchant_oid}{email}{amount}{user_basket}{no_installment}{max_installment}{currency}{test_mode}"
    paytr_token = base64.b64encode(
        hmac.new(merchant_key, (hash_str + merchant_salt).encode(), hashlib.sha256).digest()
    ).decode()
    base_url = (request.base_url.rstrip("/") + "/").rstrip("/")
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
        "payment_amount": amount,
        "paytr_token": paytr_token,
        "user_basket": user_basket,
        "debug_on": "0",
        "no_installment": no_installment,
        "max_installment": max_installment,
        "user_name": ((body.full_name or "").strip() or "")[:60],
        "user_address": "Norya ödeme",
        "user_phone": "",
        "merchant_ok_url": merchant_ok_url,
        "merchant_fail_url": merchant_fail_url,
        "timeout_limit": "30",
        "currency": currency,
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
        raise HTTPException(status_code=400, detail=result.get("reason", "PayTR token alınamadı."))
    token = result.get("token", "")
    return {"iframe_url": f"https://www.paytr.com/odeme/guvenli/{token}", "merchant_oid": merchant_oid}


async def _paytr_callback_handle(request: Request, db: Session):
    """PayTR bildirim işlemi. /payment/callback ve /api/paytr/webhook tarafından kullanılır."""
    form = await request.form()
    post = {k: (form.get(k) or "") for k in form}
    merchant_oid = post.get("merchant_oid", "")
    status = post.get("status", "")
    total_amount = post.get("total_amount", "")
    paytr_hash = post.get("hash", "")

    if not merchant_oid or not status or not total_amount or not paytr_hash:
        return PlainTextResponse("OK", status_code=200)

    merchant_key = settings.paytr_merchant_key.encode() if isinstance(settings.paytr_merchant_key, str) else settings.paytr_merchant_key
    merchant_salt = settings.paytr_merchant_salt
    import base64
    import hmac
    import hashlib
    hash_str = f"{merchant_oid}{merchant_salt}{status}{total_amount}"
    our_hash = base64.b64encode(
        hmac.new(merchant_key, hash_str.encode(), hashlib.sha256).digest()
    ).decode()
    if our_hash != paytr_hash:
        return PlainTextResponse("PAYTR notification failed: bad hash", status_code=400)

    stmt = select(PaymentOrder).where(PaymentOrder.merchant_oid == merchant_oid)
    order = db.exec(stmt).first()
    if not order:
        return PlainTextResponse("OK", status_code=200)
    if order.status == "completed":
        return PlainTextResponse("OK", status_code=200)

    try:
        if status == "success":
            user = db.get(User, order.user_id)
            if user:
                if order.product == "single":
                    user.extra_credits = (getattr(user, "extra_credits", 0) or 0) + 1
                    db.add(user)
                elif order.product in ("monthly", "yearly"):
                    user.plan = "pro"
                    db.add(user)
                _audit(db, f"payment_{order.product}", order.user_id, None)
            order.status = "completed"
            db.add(order)
        else:
            order.status = "failed"
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


@app.post("/payment/callback")
async def payment_callback(request: Request, db: Session = Depends(get_db)):
    """PayTR bildirim URL: ödeme sonucu POST ile gelir."""
    return await _paytr_callback_handle(request, db)


@app.post("/api/paytr/webhook")
async def paytr_webhook(request: Request, db: Session = Depends(get_db)):
    """PayTR webhook (alias): aynı işlem, PayTR panelinde bu URL de kullanılabilir."""
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
    if order.product == "single":
        user.extra_credits = (getattr(user, "extra_credits", 0) or 0) + 1
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
