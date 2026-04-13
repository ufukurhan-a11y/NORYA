"""Tenant API Key: Hastane entegrasyonu için API key yönetimi."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class TenantApiKey(SQLModel, table=True):
    __tablename__ = "tenant_api_keys"
    id: int | None = Field(default=None, primary_key=True)
    institution_id: int = Field(foreign_key="institutions.id", index=True)
    name: str = Field(max_length=128)  # Key adı (örn: "LIS Entegrasyonu")
    key_hash: str = Field(unique=True, index=True, max_length=128)  # Hash'lenmiş key
    key_prefix: str = Field(max_length=16)  # İlk 8 karakter (gösterim için)
    is_active: bool = Field(default=True)
    last_used_at: datetime | None = None
    expires_at: datetime | None = None
    created_by_user_id: int | None = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
