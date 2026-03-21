"""E-posta toplama: blog, homepage, sample report vb. kaynaklardan gelen lead'ler."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class EmailLead(SQLModel, table=True):
    __tablename__ = "email_leads"
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(max_length=255, index=True)
    name: str | None = Field(default=None, max_length=255)
    source: str | None = Field(default=None, max_length=64)
    locale: str | None = Field(default=None, max_length=16)
    ip: str | None = Field(default=None, max_length=64)
    user_agent: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
