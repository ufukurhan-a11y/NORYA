"""Kurumsal müşteri modelleri: hastane, klinik, laboratuvar, sağlayıcı ağı."""
import re
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


def _slugify(text: str) -> str:
    """URL-safe slug generation from text."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


class Institution(SQLModel, table=True):
    __tablename__ = "institutions"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, index=True)
    type: str = Field(default="hospital", max_length=64)  # hospital | clinic | lab | network
    status: str = Field(default="pilot", max_length=32)  # pilot | active | suspended | inactive | trial
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

    # --- Multi-tenant fields ---
    tenant_slug: str | None = Field(default=None, max_length=128, unique=True, index=True)
    billing_wallet_balance: int = Field(default=0)  # Prepaid wallet in cents (e.g. $1000 = 100000)
    cost_per_analysis: int = Field(default=100)  # Credit cost per analysis in cents (default $1)
    subdomain: str | None = Field(default=None, max_length=255)  # Optional custom domain
    wallet_low_threshold: int = Field(default=20000)  # Alert threshold in cents (default $200)
    wallet_last_alert: datetime | None = None

    # --- Customization fields (white-label) ---
    logo_url: str | None = Field(default=None, max_length=512)  # Hospital logo URL
    primary_color: str | None = Field(default=None, max_length=16)  # Brand color (hex, e.g. #1a56db)
    secondary_color: str | None = Field(default=None, max_length=16)
    report_header_text: str | None = Field(default=None, max_length=256)  # Custom text on reports
    report_footer_text: str | None = Field(default=None, max_length=256)
    custom_css: str | None = Field(default=None)  # Custom CSS for tenant portal

    # --- Rate limiting ---
    daily_analysis_limit: int | None = Field(default=None)  # Max analyses per day (None = unlimited)
    hourly_analysis_limit: int | None = Field(default=None)  # Max analyses per hour

    # --- Low balance alerts ---
    alert_email_enabled: bool = Field(default=True)  # Enable email alerts for low balance
    alert_sms_enabled: bool = Field(default=False)  # Enable SMS alerts (future)
    alert_phone: str | None = Field(default=None, max_length=64)  # Phone for SMS alerts

    # --- Recurring payment (auto-renew) ---
    auto_renew_enabled: bool = Field(default=False)  # Enable automatic credit renewal
    auto_renew_amount_cents: int = Field(default=100000)  # Auto-renew amount in cents (default $1000)
    auto_renew_threshold_cents: int = Field(default=20000)  # Trigger auto-renew when balance below this
    auto_renew_interval_days: int = Field(default=30)  # Renew every N days
    auto_renew_last_at: datetime | None = None  # Last auto-renew timestamp
    paytr_utoken: str | None = Field(default=None, max_length=256)  # PayTR user token for recurring payments
    paytr_ctoken: str | None = Field(default=None, max_length=256)  # PayTR card token for recurring payments

    def generate_slug(self) -> str:
        """Generate and set tenant_slug from name."""
        if not self.tenant_slug:
            self.tenant_slug = _slugify(self.name)
        return self.tenant_slug


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
