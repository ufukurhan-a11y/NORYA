"""Güvenlik paneli: başarısız login, rate limit, şüpheli aktivite."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class SecurityLog(SQLModel, table=True):
    __tablename__ = "security_logs"
    id: int | None = Field(default=None, primary_key=True)
    event: str = Field(index=True)  # failed_login | rate_limit | suspicious
    user_id: int | None = Field(default=None, index=True)
    ip: str | None = None
    endpoint: str | None = None
    detail: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
