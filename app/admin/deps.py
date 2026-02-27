"""Admin auth: X-Admin-Secret (API) veya cookie (panel sayfaları)."""
import base64
import hashlib
import hmac
from fastapi import Header, HTTPException, Query, Request
from fastapi.responses import RedirectResponse

from app.core.config import settings

ADMIN_COOKIE = "norya_admin"


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
    return hmac.compare_digest(cookie_value, _admin_cookie_value())


def require_admin(
    x_admin_secret: str | None = Header(None, alias="X-Admin-Secret"),
    admin_secret: str | None = Query(None, description="Admin şifresi"),
) -> None:
    """API için: header veya query ile secret kontrolü."""
    if not (settings.admin_secret or "").strip():
        raise HTTPException(status_code=503, detail="Admin paneli yapılandırılmamış (ADMIN_SECRET yok).")
    secret = x_admin_secret or admin_secret
    if not secret or secret != settings.admin_secret:
        raise HTTPException(status_code=403, detail="Yetkisiz.")


def require_admin_cookie(request: Request):
    """Panel sayfaları için: cookie ile kontrol; yoksa /admin/login'e yönlendir."""
    if not (settings.admin_secret or "").strip():
        return RedirectResponse(url="/admin/login?err=config", status_code=302)
    c = request.cookies.get(ADMIN_COOKIE)
    if not verify_admin_cookie(c):
        return RedirectResponse(url="/admin/login", status_code=302)
    return None
