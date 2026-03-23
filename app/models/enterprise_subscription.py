"""Kurumsal sözleşme / abonelik modeli."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class EnterpriseSubscription(SQLModel, table=True):
    __tablename__ = "enterprise_subscriptions"
    id: int | None = Field(default=None, primary_key=True)
    institution_id: int = Field(foreign_key="institutions.id", index=True)
    plan_name: str = Field(default="enterprise", max_length=64)
    billing_status: str = Field(default="active", max_length=32)  # active | past_due | cancelled | trial
    start_date: datetime | None = None
    end_date: datetime | None = None
    quota_limit: int = Field(default=100)
    seat_limit: int = Field(default=25)
    notes: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
