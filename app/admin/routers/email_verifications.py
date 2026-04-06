"""E-posta doğrulama kayıtları admin paneli."""
import logging
import secrets
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.config import settings
from app.core.database import get_db
from app.core.geo import get_geo_from_ip
from app.core.templating import Jinja2Templates
from app.models import EmailVerifyToken, User, UserRegistration

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
log = logging.getLogger(__name__)


def _client_ip(request: Request) -> str:
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    return request.client.host if request.client else ""


def _send_verify_email(email: str, token_str: str, country: str | None = None) -> None:
    from app.services.email_sender import country_to_lang, send_verify_email

    frontend_url = (getattr(settings, "frontend_url", None) or "").strip().rstrip("/") or "http://127.0.0.1:8000"
    verify_link = f"{frontend_url}/?verify-email={token_str}"
    lang = country_to_lang(country)
    send_verify_email(email, verify_link, lang)


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def email_verifications_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    status_filter: str | None = None,
    q: str | None = None,
    sort: str | None = "newest",
):
    query = select(UserRegistration)

    # Status filter
    valid_statuses = {"pending", "verified", "failed"}
    if status_filter and status_filter in valid_statuses:
        query = query.where(UserRegistration.status == status_filter)

    # Search by email
    if q and q.strip():
        q = q.strip()
        query = query.where(UserRegistration.email.contains(q))

    # Sort
    if sort == "oldest":
        query = query.order_by(UserRegistration.id.asc())
    else:
        query = query.order_by(UserRegistration.id.desc())

    records = list(db.exec(query.limit(500)).all())

    # Zenginleştir: ilgili kullanıcıyı bul
    user_map = {}
    for rec in records:
        if rec.user_id and rec.user_id not in user_map:
            usr = db.get(User, rec.user_id)
            user_map[rec.user_id] = usr

    rows = []
    for rec in records:
        usr = user_map.get(rec.user_id)
        rows.append({
            "id": rec.id,
            "email": rec.email,
            "full_name": rec.full_name or "",
            "status": rec.status or "pending",
            "source": rec.source or "unknown",
            "ip_address": rec.ip_address or "",
            "user_agent": (rec.user_agent or "")[:120],
            "created_at": (rec.created_at.strftime("%d.%m.%Y %H:%M:%S") if getattr(rec, "created_at", None) else "-"),
            "verified_at": (rec.verified_at.strftime("%d.%m.%Y %H:%M:%S") if getattr(rec, "verified_at", None) else "-"),
            "verification_mail_sent_at": (rec.verification_mail_sent_at.strftime("%d.%m.%Y %H:%M:%S") if getattr(rec, "verification_mail_sent_at", None) else "-"),
            "mail_send_error": rec.mail_send_error or "",
            "user_id": rec.user_id,
            "user_exists": bool(usr),
        })

    return templates.TemplateResponse(
        "admin/email_verifications.html",
        {
            "request": request,
            "records": rows,
            "status_filter": status_filter or "all",
            "q": q or "",
            "sort": sort or "newest",
        },
    )


@router.post("/{reg_id}/resend-verification")
async def resend_verification(
    request: Request,
    reg_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    rec = db.get(UserRegistration, reg_id)
    if not rec:
        return RedirectResponse(url="/admin/email-verifications", status_code=302)

    # Eski token'ları temizle
    old_tokens = list(db.exec(select(EmailVerifyToken).where(EmailVerifyToken.email == rec.email)).all())
    for old in old_tokens:
        db.delete(old)

    # Yeni token oluştur
    token_str = secrets.token_urlsafe(32)
    db.add(
        EmailVerifyToken(
            email=rec.email,
            token=token_str,
            expires_at=datetime.utcnow() + timedelta(hours=24),
        )
    )
    db.commit()

    # E-posta göndermeyi dene
    from app.services.email_sender import is_mail_configured

    mail_sent = False
    mail_error = None
    if is_mail_configured():
        try:
            country = None
            if rec.ip_address:
                country = get_geo_from_ip(rec.ip_address)[0]
            _send_verify_email(rec.email, token_str, country)
            mail_sent = True
        except Exception as e:
            mail_error = str(e)
            log.warning("Resend verification failed for %s: %s", rec.email, e)

    # Kaydı güncelle
    if mail_sent:
        rec.status = "pending"
        rec.verification_mail_sent_at = datetime.utcnow()
        rec.mail_send_error = mail_error
        rec.source = "resend"
        db.add(rec)
    elif mail_error:
        rec.status = "failed"
        rec.mail_send_error = mail_error
        db.add(rec)
    db.commit()

    return RedirectResponse(url="/admin/email-verifications?status_filter=" + rec.status, status_code=302)
