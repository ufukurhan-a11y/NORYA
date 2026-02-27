import secrets
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session, select

from app.core.config import settings
from app.core.database import get_db
from app.core.geo import get_country_from_ip
from app.core.rate_limit import limiter
from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from app.api.deps import get_current_user
from app.models import AuditLog, EmailVerifyToken, GuestLoginToken, PasswordResetToken, Presence, SecurityLog, User
from app.schemas import (
    ChangePasswordRequest,
    DeleteAccountRequest,
    ForgotPasswordRequest,
    GuestLoginRequest,
    ResetPasswordRequest,
    Token,
    UserCreate,
    UserLogin,
    UserResponse,
    UserUpdate,
)

router = APIRouter(prefix="/auth", tags=["auth"])
_AUTH_RATE_LIMIT = f"{settings.rate_limit_per_minute}/minute"
_REGISTER_LIMIT = f"{getattr(settings, 'rate_limit_register_per_minute', 3)}/minute;100/hour"


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


def _send_verify_email(email: str, token: str, country: str | None = None) -> None:
    """E-posta doğrulama linki gönderir (frontend_url + token, dil ülkeye göre)."""
    from app.services.email_sender import country_to_lang, send_verify_email

    frontend_url = (getattr(settings, "frontend_url", None) or "").strip().rstrip("/") or "http://127.0.0.1:8000"
    verify_link = f"{frontend_url}/?verify-email={token}"
    lang = country_to_lang(country)
    send_verify_email(email, verify_link, lang)


def _send_reset_email(email: str, token: str, lang: str, expiry_hours: int = 1) -> None:
    """Şifre sıfırlama linki e-postası (ülkeye göre dil, kurumsal şablon)."""
    from app.core.config import settings
    from app.services.email_sender import send_password_reset_email

    frontend_url = (getattr(settings, "frontend_url", None) or "").strip().rstrip("/") or "http://127.0.0.1:8000"
    reset_link = f"{frontend_url}/?reset={token}"
    send_password_reset_email(email, reset_link, lang, expiry_hours)


@router.post("/register", response_model=UserResponse)
@limiter.limit(_REGISTER_LIMIT)
async def register(
    request: Request,
    db: Session = Depends(get_db),
):
    form = await request.form()
    email = (form.get("email") or "").strip()
    password = (form.get("password") or "")
    full_name = (form.get("full_name") or "").strip()
    phone_raw = form.get("phone")
    phone = (phone_raw or "").strip() if phone_raw else ""
    country = (form.get("country") or "").strip().upper()[:2] if form.get("country") else ""
    if not full_name:
        raise HTTPException(status_code=422, detail="Ad soyad girin.")
    if not email:
        raise HTTPException(status_code=422, detail="E-posta girin.")
    if not password or len(password) < 6:
        raise HTTPException(status_code=422, detail="Şifre en az 6 karakter olmalı.")
    if not phone or len(phone) < 5:
        raise HTTPException(status_code=422, detail="Geçerli bir telefon numarası girin (ülke kodu ile, örn. +905551234567).")
    if not country or len(country) != 2:
        raise HTTPException(status_code=422, detail="Ülke seçin.")
    try:
        stmt = select(User).where(User.email == email)
        if db.exec(stmt).first():
            raise HTTPException(status_code=400, detail="Bu e-posta adresi zaten kayıtlı.")
        user = User(
            email=email,
            hashed_password=hash_password(password),
            full_name=full_name,
            phone=phone or None,
            country=country or None,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        ip = _client_ip(request)
        token_str = secrets.token_urlsafe(32)
        db.add(
            EmailVerifyToken(
                email=email,
                token=token_str,
                expires_at=datetime.utcnow() + timedelta(hours=24),
            )
        )
        db.commit()
        _send_verify_email(email, token_str, country or (get_country_from_ip(ip) if ip else None))
        _audit(db, "register", user.id, ip)
        country = get_country_from_ip(ip)
        if country and not getattr(user, "country", None):
            user.country = country
            db.add(user)
            db.commit()
            db.refresh(user)
        return UserResponse(
            id=user.id or 0,
            email=user.email,
            full_name=user.full_name,
            phone=getattr(user, "phone", None),
            country=getattr(user, "country", None),
            email_verified=bool(getattr(user, "email_verified_at", None)),
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Kayıt sırasında hata: {str(e)}. Veritabanı erişilebilir mi kontrol edin.",
        )


@router.post("/login", response_model=Token)
@limiter.limit("5/minute;20/hour")
async def login(
    request: Request,
    db: Session = Depends(get_db),
):
    form = await request.form()
    email = (form.get("email") or "").strip()
    password = (form.get("password") or "")
    if not email:
        raise HTTPException(status_code=422, detail="E-posta girin.")
    if not password:
        raise HTTPException(status_code=422, detail="Şifre girin.")
    stmt = select(User).where(User.email == email)
    user = db.exec(stmt).first()
    ip = _client_ip(request)
    if not user or not verify_password(password, user.hashed_password):
        try:
            db.add(SecurityLog(event="failed_login", ip=ip, endpoint="/auth/login", detail=email or "no_email"))
            db.commit()
        except Exception:
            pass
        raise HTTPException(status_code=401, detail="E-posta veya şifre hatalı.")
    if getattr(user, "is_banned", False):
        try:
            db.add(SecurityLog(event="failed_login", user_id=user.id, ip=ip, endpoint="/auth/login", detail="banned"))
            db.commit()
        except Exception:
            pass
        raise HTTPException(status_code=403, detail="Hesabınız kısıtlandı.")
    token = create_access_token({"sub": str(user.id)})
    _audit(db, "login", user.id, ip)
    try:
        user.last_login_at = datetime.utcnow()
        db.add(user)
        db.commit()
    except Exception:
        pass
    if not getattr(user, "country", None):
        country = get_country_from_ip(ip)
        if country:
            user.country = country
            db.add(user)
            db.commit()
    return Token(access_token=token)


@router.get("/me", response_model=UserResponse)
def me(user: User = Depends(get_current_user)):
    """Giriş yapmış kullanıcının ad, e-posta, telefon, ülke, e-posta doğrulama bilgisi."""
    return UserResponse(
        id=user.id or 0,
        email=user.email,
        full_name=user.full_name or "",
        phone=getattr(user, "phone", None),
        country=getattr(user, "country", None),
        email_verified=bool(getattr(user, "email_verified_at", None)),
    )


@router.patch("/me", response_model=UserResponse)
def update_me(
    body: UserUpdate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Profil güncelleme: ad, telefon, ülke."""
    if body.full_name is not None:
        user.full_name = (body.full_name or "").strip() or user.full_name
    if body.phone is not None:
        user.phone = (body.phone or "").strip() or None
    if body.country is not None:
        user.country = (body.country or "").strip().upper()[:2] or None
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserResponse(
        id=user.id or 0,
        email=user.email,
        full_name=user.full_name or "",
        phone=getattr(user, "phone", None),
        country=getattr(user, "country", None),
        email_verified=bool(getattr(user, "email_verified_at", None)),
    )


@router.post("/change-password")
def change_password(
    body: ChangePasswordRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Giriş yapmış kullanıcı şifre değiştirir (mevcut şifre + yeni şifre)."""
    if not verify_password(body.current_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Mevcut şifre hatalı.")
    user.hashed_password = hash_password(body.new_password)
    db.add(user)
    db.commit()
    return {"message": "Şifre güncellendi."}


@router.post("/delete-account")
def delete_account(
    body: DeleteAccountRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Hesabı siler (şifre ile onay). Kullanıcı ve ilişkili veriler silinir."""
    if not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Şifre hatalı.")
    from app.models import AnalysisRecord, AuditLog, EmailVerifyToken, GuestLoginToken, PasswordResetToken, Presence, ShareToken

    uid = user.id
    user_email = user.email
    try:
        analysis_ids = [r.id for r in db.exec(select(AnalysisRecord.id).where(AnalysisRecord.user_id == uid)).all() if r.id]
        for aid in analysis_ids:
            for st in db.exec(select(ShareToken).where(ShareToken.analysis_id == aid)).all():
                db.delete(st)
        for rec in db.exec(select(AnalysisRecord).where(AnalysisRecord.user_id == uid)).all():
            db.delete(rec)
        for rec in db.exec(select(AuditLog).where(AuditLog.user_id == uid)).all():
            db.delete(rec)
        for rec in db.exec(select(Presence).where(Presence.user_id == uid)).all():
            db.delete(rec)
        for rec in db.exec(select(EmailVerifyToken).where(EmailVerifyToken.email == user_email)).all():
            db.delete(rec)
        for rec in db.exec(select(PasswordResetToken).where(PasswordResetToken.email == user_email)).all():
            db.delete(rec)
        for rec in db.exec(select(GuestLoginToken).where(GuestLoginToken.user_id == uid)).all():
            db.delete(rec)
        db.delete(user)
        db.commit()
    except Exception:
        raise HTTPException(status_code=500, detail="Hesap silinirken hata oluştu.")
    return {"message": "Hesabınız silindi."}


@router.post("/guest-login", response_model=Token)
def guest_login(
    body: GuestLoginRequest,
    request: Request,
    db: Session = Depends(get_db),
    _: None = Depends(limiter.limit(_AUTH_RATE_LIMIT)),
):
    """Ödeme sonrası misafir: guest_token ile tek seferlik giriş (sadece tek analiz satın alanlar)."""
    token_str = (body.guest_token or "").strip()
    if not token_str:
        raise HTTPException(status_code=400, detail="Geçersiz misafir kodu.")
    stmt = select(GuestLoginToken).where(GuestLoginToken.token == token_str)
    row = db.exec(stmt).first()
    if not row:
        raise HTTPException(status_code=400, detail="Geçersiz veya kullanılmış misafir kodu.")
    if row.used:
        raise HTTPException(status_code=400, detail="Bu kod zaten kullanıldı.")
    if row.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Misafir kodu süresi dolmuş.")
    row.used = True
    db.add(row)
    db.commit()
    token = create_access_token({"sub": str(row.user_id)})
    _audit(db, "guest_login", row.user_id, _client_ip(request))
    return Token(access_token=token)


@router.post("/forgot-password")
def forgot_password(
    body: ForgotPasswordRequest,
    db: Session = Depends(get_db),
):
    stmt = select(User).where(User.email == body.email)
    user = db.exec(stmt).first()
    if not user:
        return {"message": "Bu e-posta kayıtlıysa şifre sıfırlama linki gönderildi."}
    token_str = secrets.token_urlsafe(32)
    expiry_hours = 1
    db.add(
        PasswordResetToken(
            email=body.email,
            token=token_str,
            expires_at=datetime.utcnow() + timedelta(hours=expiry_hours),
        )
    )
    db.commit()
    from app.services.email_sender import country_to_lang

    lang = country_to_lang(getattr(user, "country", None))
    _send_reset_email(body.email, token_str, lang, expiry_hours)
    return {"message": "E-posta adresinize şifre sıfırlama linki gönderildi."}


@router.get("/verify-email")
def verify_email(token: str, db: Session = Depends(get_db)):
    stmt = select(EmailVerifyToken).where(EmailVerifyToken.token == token)
    row = db.exec(stmt).first()
    if not row or row.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Geçersiz veya süresi dolmuş link.")
    stmt = select(User).where(User.email == row.email)
    user = db.exec(stmt).first()
    if user:
        user.email_verified_at = datetime.utcnow()
        db.add(user)
    db.delete(row)
    db.commit()
    return {"message": "E-posta adresiniz doğrulandı."}


@router.post("/reset-password")
def reset_password(body: ResetPasswordRequest, db: Session = Depends(get_db)):
    stmt = select(PasswordResetToken).where(PasswordResetToken.token == body.token)
    row = db.exec(stmt).first()
    if not row or row.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Geçersiz veya süresi dolmuş link.")
    stmt = select(User).where(User.email == row.email)
    user = db.exec(stmt).first()
    if not user:
        raise HTTPException(status_code=400, detail="Kullanıcı bulunamadı.")
    user.hashed_password = hash_password(body.new_password)
    db.add(user)
    db.delete(row)
    db.commit()
    return {"message": "Şifre güncellendi. Giriş yapabilirsiniz."}


@router.post("/heartbeat")
def heartbeat(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    page: str | None = None,
):
    """Giriş yapmış kullanıcı 'şu an sitede' sayılır. Frontend her ~60 sn çağırabilir. Opsiyonel: ?page=/path ile sayfa bilgisi (canlı takip)."""
    uid = user.id
    if not uid:
        return {"ok": True}
    now = datetime.utcnow()
    ip = _client_ip(request)
    country = get_country_from_ip(ip) if ip else None
    current_page = (page or "").strip() or None
    existing = db.exec(select(Presence).where(Presence.user_id == uid)).first()
    if existing:
        existing.last_seen_at = now
        existing.ip = ip
        existing.country = country
        existing.current_page = current_page or existing.current_page
        db.add(existing)
    else:
        db.add(Presence(user_id=uid, last_seen_at=now, ip=ip, country=country, current_page=current_page))
    db.commit()
    return {"ok": True}
