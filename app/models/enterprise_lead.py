"""Kurumsal demo talep formu: hastane/klinik başvuruları."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class EnterpriseLead(SQLModel, table=True):
    __tablename__ = "enterprise_leads"
    id: int | None = Field(default=None, primary_key=True)
    kurum_adi: str = Field(max_length=255)
    yetkili_ad: str = Field(max_length=255)
    email: str = Field(max_length=255, index=True)
    telefon: str | None = Field(default=None, max_length=64)
    kurum_tipi: str | None = Field(default=None, max_length=64)
    aylik_rapor: str | None = Field(default=None, max_length=64)
    mesaj: str | None = Field(default=None)
    kvkk_accepted: bool = Field(default=False)
    ip: str | None = Field(default=None, max_length=64)
    user_agent: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
