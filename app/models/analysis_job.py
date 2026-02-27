"""AI analiz kuyruğu: pending → processing → done | failed."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class AnalysisJob(SQLModel, table=True):
    __tablename__ = "analysis_jobs"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    analysis_record_id: int | None = Field(default=None, index=True)  # AnalysisRecord.id ile ilişki
    status: str = "pending"  # pending | processing | done | failed
    duration_ms: int | None = None
    error_message: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = Field(default_factory=datetime.utcnow)
