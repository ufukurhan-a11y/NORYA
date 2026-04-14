"""Tenant wallet transaction audit trail."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class TenantWalletTransaction(SQLModel, table=True):
    __tablename__ = "tenant_wallet_transactions"
    id: int | None = Field(default=None, primary_key=True)
    institution_id: int = Field(foreign_key="institutions.id", index=True)
    amount_cents: int  # Positive=load, negative=spend
    transaction_type: str = Field(max_length=32)  # load | spend | refund | admin_adjust | auto_renew
    description: str | None = Field(default=None, max_length=512)
    created_at: datetime = Field(default_factory=datetime.utcnow)
