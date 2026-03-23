"""Kurumsal müşteri modelleri: hastane, klinik, laboratuvar, sağlayıcı ağı."""
from datetime import datetime

from sqlmodel import Field, SQLModel


class Institution(SQLModel, table=True):
    __tablename__ = "institutions"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, index=True)
    type: str = Field(default="hospital", max_length=64)  # hospital | clinic | lab | network
    status: str = Field(default="pilot", max_length=32)  # pilot | active | suspended
    plan: str = Field(default="enterprise", max_length=32)
    seat_limit: int = Field(default=25)
    monthly_quota: int = Field(default=100)
    quota_used_this_month: int = Field(default=0)
    quota_reset_day: int = Field(default=1)
    active_languages: str = Field(default="tr,en", max_length=255)  # comma-separated
    is_active: bool = Field(default=True)
    contract_start: datetime | None = None
    contract_end: datetime | None = None
    contact_email: str | None = Field(default=None, max_length=255)
    contact_phone: str | None = Field(default=None, max_length=64)
    notes: str | None = None
    onboarding_completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class InstitutionMembership(SQLModel, table=True):
    __tablename__ = "institution_memberships"
    id: int | None = Field(default=None, primary_key=True)
    institution_id: int = Field(foreign_key="institutions.id", index=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    role: str = Field(default="member", max_length=32)  # owner | admin | reviewer | staff | member | readonly
    invited_by: int | None = Field(default=None)  # user_id of the person who invited
    invited_at: datetime | None = None
    accepted_at: datetime | None = None
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class InstitutionInvite(SQLModel, table=True):
    __tablename__ = "institution_invites"
    id: int | None = Field(default=None, primary_key=True)
    institution_id: int = Field(foreign_key="institutions.id", index=True)
    email: str = Field(max_length=255, index=True)
    role: str = Field(default="member", max_length=32)
    token: str = Field(unique=True, index=True, max_length=128)
    invited_by: int | None = Field(default=None)  # user_id
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime | None = None
    accepted_at: datetime | None = None
