"""Kullanıcı 'şu an sitede' takibi: heartbeat ile güncellenir."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class Presence(SQLModel, table=True):
    """Kullanıcı başına son görülme. Heartbeat endpoint'i günceller; canlı kullanıcı takibi."""
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(unique=True, index=True)
    last_seen_at: datetime = Field(default_factory=datetime.utcnow)
    ip: str | None = None
    country: str | None = None
    current_page: str | None = None
