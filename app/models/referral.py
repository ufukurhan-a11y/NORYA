"""Referral (davet) sistemi: kullanıcılar arkadaşlarını davet eder, indirim kazanır."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class ReferralCode(SQLModel, table=True):
    __tablename__ = "referral_codes"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    code: str = Field(unique=True, index=True, max_length=32)
    uses: int = Field(default=0)
    max_uses: int | None = Field(default=None)
    discount_percent: int = Field(default=15)  # davet eden + edilen kişiye verilecek indirim yüzdesi
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)


class ReferralUsage(SQLModel, table=True):
    __tablename__ = "referral_usages"
    id: int | None = Field(default=None, primary_key=True)
    referral_code_id: int = Field(foreign_key="referral_codes.id", index=True)
    referred_user_id: int = Field(foreign_key="user.id", index=True)
    referrer_user_id: int = Field(foreign_key="user.id", index=True)
    reward_granted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
