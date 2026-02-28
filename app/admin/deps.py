"""Admin auth: X-Admin-Secret (API) veya cookie (panel sayfaları)."""
import base64
import hashlib
import hmac
from fastapi import Header, HTTPException, Query, Request
from fastapi.responses import RedirectResponse

from app.core.config import settings

ADMIN_COOKIE = "norya_admin"

# Lockout: aynı IP için 5 başarısız deneme -> 15 dk
ADMIN_LOGIN_MAX_FAILURES = 5
ADMIN_LOCKOUT_MINUTES = 15


def get_client_ip(request: Request) -> str:
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip() or ""
    return request.client.host if request.client else ""


def _admin_secret_constant_time_compare(provided: str | None, expected: str | None) -> bool:
    """Timing-safe karşılaştırma; detay sızdırmaz."""
    p = (provided or "").encode("utf-8")
    e = (expected or "").encode("utf-8")
    if len(p) != len(e):
        # Sabit süre için aynı uzunlukta karşılaştır (dummy ile)
        dummy = b"\x00" * max(len(p), len(e))
        hmac.compare_digest(p if len(p) >= len(e) else dummy[: len(p)], e if len(e) >= len(p) else dummy[: len(e)])
        return False
    return hmac.compare_digest(p, e)


def _admin_cookie_value() -> str:
    raw = hmac.new(
        (settings.secret_key or "norya").encode(),
        (settings.admin_secret or "").encode(),
        hashlib.sha256,
    ).digest()
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def verify_admin_cookie(cookie_value: str | None) -> bool:
    if not cookie_value or not (settings.admin_secret or "").strip():
        return False
    return hmac.compare_digest(cookie_value, _admin_cookie_value())  # zaten constant-time


def require_admin(
    x_admin_secret: str | None = Header(None, alias="X-Admin-Secret"),
    admin_secret: str | None = Query(None, description="Admin şifresi"),
) -> None:
    """API için: header veya query ile secret kontrolü (constant-time compare)."""
    expected = (settings.admin_secret or "").strip()
    if not expected:
        raise HTTPException(status_code=503, detail="Admin paneli yapılandırılmamış (ADMIN_SECRET yok).")
    secret = (x_admin_secret or admin_secret) or ""
    if not _admin_secret_constant_time_compare(secret, settings.admin_secret):
        raise HTTPException(status_code=403, detail="Yetkisiz.")


def require_admin_cookie(request: Request):
    """Panel sayfaları için: cookie ile kontrol; yoksa /admin/login'e yönlendir."""
    if not (settings.admin_secret or "").strip():
        return RedirectResponse(url="/admin/login?err=config", status_code=302)
    c = request.cookies.get(ADMIN_COOKIE)
    if not verify_admin_cookie(c):
        return RedirectResponse(url="/admin/login", status_code=302)
    return None


def require_admin_secret_or_cookie(
    request: Request,
    x_admin_secret: str | None = Header(None, alias="X-Admin-Secret"),
    admin_secret: str | None = Query(None),
):
    """PDF/orijinal belge için: cookie (yeni panel) veya X-Admin-Secret (eski API) ile yetki."""
    if not (settings.admin_secret or "").strip():
        raise HTTPException(status_code=503, detail="Admin paneli yapılandırılmamış.")
    if verify_admin_cookie(request.cookies.get(ADMIN_COOKIE)):
        return None
    secret = (x_admin_secret or admin_secret) or ""
    if _admin_secret_constant_time_compare(secret, settings.admin_secret):
        return None
    raise HTTPException(status_code=403, detail="Yetkisiz.")
