from datetime import datetime

from sqlmodel import Field, SQLModel


class UserRegistration(SQLModel, table=True):
    """Kayıt ve e-posta doğrulama takip tablosu. Admin panelinde görüntüleme amaçlıdır."""
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    full_name: str = ""
    # status: pending | verified | failed
    status: str = Field(default="pending", index=True)
    # User tablosundaki kullanıcı ID'si (verified olduğunda set edilir)
    user_id: int | None = Field(default=None, index=True)
    verification_mail_sent_at: datetime | None = None
    mail_send_error: str | None = None
    source: str | None = None  # "signup" | "guest_claim" | "admin_manual" | "resend"
    ip_address: str | None = None  # Backend IP (sunucu tarafı)
    frontend_ip_address: str | None = None  # Frontend IP (tarayıcı tarafı, cookie'den)
    user_agent: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    verified_at: datetime | None = None
