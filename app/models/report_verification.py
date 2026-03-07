"""Rapor bazlı QR doğrulama: her rapor için benzersiz report_id, verification_code ve signed token."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class ReportVerification(SQLModel, table=True):
    """Her premium (aylık/yıllık) rapor için tek kayıt. QR ile doğrulama için kullanılır."""

    id: int | None = Field(default=None, primary_key=True)
    report_id: str = Field(unique=True, index=True)  # Public UUID; URL'de /verify/{report_id}
    analysis_id: int = Field(foreign_key="analysisrecord.id", unique=True, index=True)  # Bir analiz = bir doğrulama
    user_id: int = Field(foreign_key="user.id", index=True)
    package_type: str = Field(index=True)  # "monthly" | "yearly"
    language: str = Field(max_length=8, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    verification_code: str = Field(max_length=32, index=True)  # Kısa insan okunabilir kod (PDF/verify sayfasında)
    is_active: bool = Field(default=True, index=True)
    report_status: str = Field(default="completed", max_length=32)  # completed | draft | revoked
