from datetime import datetime

from sqlmodel import Field, SQLModel


class AnalysisRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    input_text: str
    result_text: str
    source: str = "text"  # "text" | "pdf" | "image"
    doctor_notes: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
