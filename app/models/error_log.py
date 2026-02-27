"""Hata log merkezi: global exception handler ile doldurulur."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class ErrorLog(SQLModel, table=True):
    __tablename__ = "error_logs"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, index=True)
    endpoint: str | None = None
    method: str | None = None
    error_message: str | None = None
    stack_trace: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
