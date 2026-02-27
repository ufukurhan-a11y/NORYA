from datetime import datetime

from sqlmodel import Field, SQLModel


class AuditLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event: str = Field(index=True)  # login, register, analyze, forgot_password, etc.
    user_id: int | None = Field(default=None, index=True)
    ip: str | None = None
    country: str | None = None  # IP'den çözülen ülke kodu (TR, US vb.)
    created_at: datetime = Field(default_factory=datetime.utcnow)
