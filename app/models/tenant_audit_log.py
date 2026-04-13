"""Tenant audit log: Her tenant içindeki tüm aktivitelerin detaylı kaydı (KVKK/GDPR uyumluluğu)."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class TenantAuditLog(SQLModel, table=True):
    __tablename__ = "tenant_audit_logs"
    id: int | None = Field(default=None, primary_key=True)
    institution_id: int = Field(foreign_key="institutions.id", index=True)
    user_id: int | None = Field(default=None, foreign_key="user.id", index=True)
    action: str = Field(max_length=64)  # login, logout, upload, analyze, download, export, settings_change, etc.
    entity_type: str | None = Field(default=None, max_length=64)  # case, report, user, settings
    entity_id: int | None = Field(default=None, index=True)
    ip_address: str | None = Field(default=None, max_length=64)
    user_agent: str | None = Field(default=None, max_length=512)
    detail: str | None = Field(default=None, max_length=1024)
    metadata_json: str | None = Field(default=None)  # Extra JSON data
    created_at: datetime = Field(default_factory=datetime.utcnow)
