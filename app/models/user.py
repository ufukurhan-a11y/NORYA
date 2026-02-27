from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    full_name: str = ""
    email_verified_at: datetime | None = None
    plan: str = "free"  # "free" | "pro" — ücretsiz aylık limit, pro sınırsız
    extra_credits: int = 0  # Ödeme ile alınan tek analiz hakları (önce öde, sonra kullan)
    phone: str | None = None
    country: str | None = None  # IP'den veya kullanıcıdan (örn. TR, US)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
    is_banned: bool = False
    last_login_at: datetime | None = None
