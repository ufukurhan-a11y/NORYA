import secrets
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session, select

from app.core.database import get_db
from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from app.models import AuditLog, EmailVerifyToken, PasswordResetToken, User
from app.schemas import (
    ForgotPasswordRequest,
    ResetPasswordRequest,
    Token,
    UserCreate,
    UserLogin,
    UserResponse,
)

router = APIRouter(prefix="/auth", tags=["auth"])


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


def _send_verify_email_stub(email: str, token: str) -> None:
    # Gerçek ortamda: SMTP veya SendGrid ile e-posta gönder
    # Örnek link: {FRONTEND_URL}/verify-email?token={token}
    pass


def _send_reset_email_stub(email: str, token: str) -> None:
    # Gerçek ortamda: şifre sıfırlama linki gönder
    pass


@router.post("/register", response_model=UserResponse)
def register(
    body: UserCreate,
    request: Request,
    db: Session = Depends(get_db),
):
    try:
        stmt = select(User).where(User.email == body.email)
        if db.exec(stmt).first():
            raise HTTPException(status_code=400, detail="Bu e-posta adresi zaten kayıtlı.")
        user = User(
            email=body.email,
            hashed_password=hash_password(body.password),
            full_name=body.full_name or "",
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        token_str = secrets.token_urlsafe(32)
        verify = EmailVerifyToken(
            email=body.email,
            token=token_str,
            expires_at=datetime.utcnow() + timedelta(hours=24),
        )
        db.add(verify)
        db.commit()
        _send_verify_email_stub(body.email, token_str)
        _audit(db, "register", user.id, _client_ip(request))
        return UserResponse(id=user.id or 0, email=user.email, full_name=user.full_name)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Kayıt sırasında hata: {str(e)}. Veritabanı erişilebilir mi kontrol edin.",
        )


@router.post("/login", response_model=Token)
def login(
    body: UserLogin,
    request: Request,
    db: Session = Depends(get_db),
):
    stmt = select(User).where(User.email == body.email)
    user = db.exec(stmt).first()
    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="E-posta veya şifre hatalı.")
    token = create_access_token({"sub": str(user.id)})
    _audit(db, "login", user.id, _client_ip(request))
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
    db.add(
        PasswordResetToken(
            email=body.email,
            token=token_str,
            expires_at=datetime.utcnow() + timedelta(hours=1),
        )
    )
    db.commit()
    _send_reset_email_stub(body.email, token_str)
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
