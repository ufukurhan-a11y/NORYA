"""Dosya upload logları: kullanıcı, dosya adı, boyut, durum, süre."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class UploadLog(SQLModel, table=True):
    __tablename__ = "upload_logs"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, index=True)
    filename: str | None = None
    file_size_bytes: int | None = None
    status: str = "pending"  # pending | success | failed
    error_message: str | None = None
    duration_ms: int | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
