"""PWA push bildirim abonelikleri (Web Push API)."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class PushSubscription(SQLModel, table=True):
    __tablename__ = "push_subscriptions"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    endpoint: str = Field(index=True)  # benzersiz; aynı endpoint tekrar kaydedilmez
    p256dh: str = ""  # client public key (base64url)
    auth: str = ""    # auth secret (base64url)
    created_at: datetime = Field(default_factory=datetime.utcnow)
