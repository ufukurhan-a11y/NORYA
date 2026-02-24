import secrets
import time
from collections import defaultdict
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

from fastapi import Depends, FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select

# Basit rate limit: IP başına dakikada max istek
_RATE_LIMIT: dict[str, list[float]] = defaultdict(list)
_RATE_LIMIT_WINDOW = 60.0  # saniye
_RATE_LIMIT_MAX = 30  # /analyze ve /auth için dakikada max


def _rate_limit_key(request: Request) -> str:
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    return request.client.host if request.client else ""


def _check_rate_limit(request: Request) -> None:
    key = _rate_limit_key(request)
    now = time.monotonic()
    lst = _RATE_LIMIT[key]
    lst.append(now)
    while lst and lst[0] < now - _RATE_LIMIT_WINDOW:
        lst.pop(0)
    if len(lst) > _RATE_LIMIT_MAX:
        raise HTTPException(status_code=429, detail="Çok fazla istek. Lütfen bir dakika bekleyin.")

from app.api.auth import router as auth_router
from app.api.deps import get_current_user
from app.core.database import get_db, init_db
from app.models import AnalysisRecord, AuditLog, EmailVerifyToken, PasswordResetToken, ShareToken, User  # noqa: F401
from app.schemas.analyze import (
    AnalysisDetail,
    AnalysisHistoryItem,
    AnalyzeRequest,
    AnalyzeResponse,
)
from app.services.analyze import analyze_blood_test, analyze_blood_test_from_image
from app.services.pdf_extract import extract_text_from_pdf

ALLOWED_UPLOAD_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MIME_MAP = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}

# Proje kökü: app/main.py -> app/ -> norya/
_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = _ROOT / "static"
# Çalışma dizininden de dene (uvicorn farklı yerden çalıştırılırsa)
if not STATIC_DIR.is_dir():
    STATIC_DIR = Path.cwd() / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Norya API",
    description="Kan tahlili açıklama SaaS API",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

if STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/health")
def health():
    return {"durum": "hazır", "servis": "norya-api"}


# Ülke kodu -> dil kodu. Global: tr, en, de, ar, he, hi, it, es, fr
COUNTRY_TO_LANG = {
    "TR": "tr",
    "US": "en", "GB": "en", "AU": "en", "CA": "en", "IE": "en", "NZ": "en",
    "DE": "de", "AT": "de", "CH": "de",
    "IL": "he",
    "SA": "ar", "EG": "ar", "AE": "ar", "QA": "ar", "JO": "ar", "LB": "ar", "SY": "ar", "IQ": "ar", "KW": "ar", "BH": "ar", "OM": "ar", "YE": "ar", "PS": "ar", "MA": "ar", "DZ": "ar", "TN": "ar",
    "IN": "hi",
    "FR": "fr", "ES": "es", "IT": "it", "NL": "nl", "PL": "pl", "RU": "ru",
}
DEFAULT_LANG = "en"

# Ülke kodu -> para birimi (sizin tahsilat EUR; ziyaretçiye kendi para biriminde gösterilir)
COUNTRY_TO_CURRENCY = {
    "TR": "TRY", "US": "USD", "GB": "GBP", "AU": "AUD", "CA": "CAD", "SA": "SAR", "AE": "AED",
    "QA": "QAR", "KW": "KWD", "BH": "BHD", "OM": "OMR", "EG": "EGP", "JO": "JOD", "IL": "ILS",
    "IN": "INR", "RU": "RUB", "CH": "CHF", "PL": "PLN", "MA": "MAD", "DZ": "DZD", "TN": "TND",
}
EUR_BASE = {"single": 13, "monthly": 50, "yearly": 99}
# Varsayılan kurlar (API yanıt vermezse kullanılır)
EUR_RATES_FALLBACK = {
    "EUR": 1.0, "USD": 1.08, "GBP": 0.85, "TRY": 34.5, "SAR": 4.05, "AED": 3.97, "QAR": 3.94,
    "KWD": 0.33, "BHD": 0.41, "OMR": 0.42, "EGP": 33.0, "JOD": 0.77, "ILS": 4.0, "INR": 90.0,
    "RUB": 100.0, "CHF": 0.95, "AUD": 1.65, "CAD": 1.47, "PLN": 4.3, "MAD": 10.8, "DZD": 145.0, "TND": 3.35,
}
CURRENCY_SYMBOLS = {
    "EUR": "€", "USD": "$", "GBP": "£", "TRY": "₺", "SAR": "ر.س", "AED": "د.إ", "QAR": "ر.ق",
    "KWD": "د.ك", "BHD": "د.ب", "OMR": "ر.ع", "EGP": "E£", "JOD": "د.أ", "ILS": "₪", "INR": "₹",
    "RUB": "₽", "CHF": "CHF", "AUD": "A$", "CAD": "C$", "PLN": "zł", "MAD": "DH", "DZD": "DA", "TND": "DT",
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


FREE_ANALYSIS_LIMIT = 1  # Ücretsiz kullanıcı başına analiz hakkı (sonra yükseltme istenir)


def _analysis_count(db: Session, user_id: int) -> int:
    stmt = select(AnalysisRecord).where(AnalysisRecord.user_id == user_id)
    return len(list(db.exec(stmt).all()))


def _client_ip(request: Request) -> str:
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    return request.client.host if request.client else ""


def _audit(db: Session, event: str, user_id: int | None, ip: str | None) -> None:
    try:
        db.add(AuditLog(event=event, user_id=user_id, ip=ip))
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


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(
    req: AnalyzeRequest,
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _check_rate_limit(request)
    if _analysis_count(db, user.id or 0) >= FREE_ANALYSIS_LIMIT:
        raise HTTPException(
            status_code=402,
            detail="Ücretsiz analiz hakkınızı kullandınız. Daha fazla analiz için abonelik planlarına göz atın.",
        )
    try:
        result = analyze_blood_test(req.text, detailed=True, doctor_notes=req.doctor_notes, lang=req.lang)
        aid = _save_analysis(db, user.id or 0, req.text, result, "text", doctor_notes=req.doctor_notes)
        _audit(db, "analyze", user.id, _client_ip(request))
        return AnalyzeResponse(sonuc=result, analiz_id=aid)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        msg = str(e).lower()
        if "api_key" in msg or "authentication" in msg or "invalid" in msg:
            raise HTTPException(
                status_code=503,
                detail="OpenAI anahtarı geçersiz veya eksik. .env içinde OPENAI_API_KEY kontrol edin.",
            )
        raise HTTPException(
            status_code=503,
            detail=f"Analiz şu an yapılamadı. ({str(e)[:100]})",
        )


@app.post("/analyze/upload", response_model=AnalyzeResponse)
def analyze_upload(
    request: Request,
    file: UploadFile = File(...),
    lang: str | None = Form(None),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _check_rate_limit(request)
    if _analysis_count(db, user.id or 0) >= FREE_ANALYSIS_LIMIT:
        raise HTTPException(
            status_code=402,
            detail="Ücretsiz analiz hakkınızı kullandınız. Daha fazla analiz için abonelik planlarına göz atın.",
        )
    if not file.filename:
        raise HTTPException(status_code=400, detail="Dosya seçin.")
    ext = "." + file.filename.lower().rsplit(".", 1)[-1] if "." in file.filename else ""
    if ext not in ALLOWED_UPLOAD_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Sadece PDF, JPG veya PNG yükleyebilirsiniz.",
        )
    try:
        content = file.file.read()
        if len(content) > 10 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="Dosya en fazla 10 MB olabilir.")
        if ext in IMAGE_EXTENSIONS:
            mime = MIME_MAP.get(ext, "image/jpeg")
            result = analyze_blood_test_from_image(content, mime, lang=lang)
            input_preview = f"[Görsel: {file.filename}]"
            aid = _save_analysis(db, user.id or 0, input_preview, result, "image")
            _audit(db, "analyze", user.id, _client_ip(request))
            return AnalyzeResponse(sonuc=result, analiz_id=aid)
        # PDF
        text = extract_text_from_pdf(content)
        if "çıkarılamadı" in text:
            raise HTTPException(status_code=400, detail="PDF'den metin okunamadı. Farklı bir dosya deneyin.")
        result = analyze_blood_test(text, lang=lang)
        aid = _save_analysis(db, user.id or 0, text[:2000], result, "pdf")
        _audit(db, "analyze", user.id, _client_ip(request))
        return AnalyzeResponse(sonuc=result, analiz_id=aid)
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Dosya işlenemedi: {str(e)[:80]}")


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
