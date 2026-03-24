"""Drip (zamanlı) e-posta kampanya takibi: hangi lead'e hangi adım gönderildi."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class DripEmailLog(SQLModel, table=True):
    __tablename__ = "drip_email_logs"
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(max_length=255, index=True)
    step: int = Field(index=True)  # 0=welcome, 1=education, 2=sample, 3=discount, 4=urgency, 5=newsletter
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    opened: bool = Field(default=False)
    clicked: bool = Field(default=False)
