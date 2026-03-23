"""Kurumsal iş akışı: vaka (case) ve rapor modelleri."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class EnterpriseCase(SQLModel, table=True):
    __tablename__ = "enterprise_cases"
    id: int | None = Field(default=None, primary_key=True)
    institution_id: int = Field(foreign_key="institutions.id", index=True)
    uploaded_by_user_id: int = Field(foreign_key="user.id", index=True)
    source_filename: str | None = Field(default=None, max_length=512)
    source_type: str = Field(default="pdf", max_length=32)  # pdf | image | text
    stored_path: str | None = Field(default=None, max_length=512)
    input_text: str | None = None
    status: str = Field(default="new", max_length=32, index=True)  # new | processing | needs_review | approved | rejected | archived
    reviewed_by_user_id: int | None = Field(default=None, foreign_key="user.id")
    reviewed_at: datetime | None = None
    review_notes: str | None = None
    analysis_record_id: int | None = Field(default=None, foreign_key="analysisrecord.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class EnterpriseReport(SQLModel, table=True):
    __tablename__ = "enterprise_reports"
    id: int | None = Field(default=None, primary_key=True)
    case_id: int = Field(foreign_key="enterprise_cases.id", index=True)
    language: str = Field(default="tr", max_length=8)
    report_text: str | None = None
    approval_status: str = Field(default="pending", max_length=32)  # pending | approved | rejected
    export_status: str = Field(default="none", max_length=32)  # none | pdf_ready | exported
    created_at: datetime = Field(default_factory=datetime.utcnow)
