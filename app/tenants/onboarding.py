"""Tenant onboarding flow.

Handles the creation and setup of new tenant environments.
"""
import logging
from datetime import datetime

from sqlmodel import Session, select

from app.core.database import DATABASE_URL
from app.models.institution import Institution
from .schema_manager import ensure_tenant_schema

logger = logging.getLogger(__name__)


def create_tenant(
    session: Session,
    name: str,
    institution_type: str = "hospital",
    contact_email: str | None = None,
    contact_phone: str | None = None,
    initial_credits_cents: int = 0,
    cost_per_analysis: int = 100,
    wallet_low_threshold: int = 20000,
    notes: str | None = None,
) -> Institution:
    """Create a new tenant institution.

    1. Generate unique tenant_slug from name
    2. Create Institution record with status="inactive"
    3. (PostgreSQL only) Create dedicated schema
    4. Set initial wallet balance if provided
    """
    # Generate slug
    base_slug = Institution(name=name).generate_slug()

    # Ensure slug uniqueness
    slug = base_slug
    counter = 1
    while True:
        existing = session.exec(
            select(Institution).where(Institution.tenant_slug == slug)
        ).first()
        if not existing:
            break
        slug = f"{base_slug}-{counter}"
        counter += 1

    # Create institution
    institution = Institution(
        name=name,
        type=institution_type,
        status="inactive",
        is_active=False,
        tenant_slug=slug,
        billing_wallet_balance=initial_credits_cents,
        cost_per_analysis=cost_per_analysis,
        wallet_low_threshold=wallet_low_threshold,
        contact_email=contact_email,
        contact_phone=contact_phone,
        notes=notes,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(institution)
    session.commit()
    session.refresh(institution)

    # Create tenant schema (PostgreSQL only)
    try:
        ensure_tenant_schema(session, slug, DATABASE_URL)
    except Exception as e:
        logger.error(f"Failed to create tenant schema for '{slug}': {e}")
        # Don't fail institution creation if schema creation fails
        # Admin can retry manually

    logger.info(
        f"Created tenant '{name}' with slug '{slug}', "
        f"initial credits: {initial_credits_cents} cents"
    )
    return institution


def activate_tenant(session: Session, institution_id: int) -> Institution | None:
    """Activate a tenant institution.

    Sets status="active" and is_active=True.
    """
    stmt = select(Institution).where(Institution.id == institution_id)
    institution = session.exec(stmt).first()

    if not institution:
        return None

    institution.status = "active"
    institution.is_active = True
    institution.updated_at = datetime.utcnow()

    session.add(institution)
    session.commit()
    session.refresh(institution)

    logger.info(f"Activated tenant '{institution.name}' (slug: {institution.tenant_slug})")
    return institution


def suspend_tenant(session: Session, institution_id: int) -> Institution | None:
    """Suspend a tenant institution."""
    stmt = select(Institution).where(Institution.id == institution_id)
    institution = session.exec(stmt).first()

    if not institution:
        return None

    institution.status = "suspended"
    institution.is_active = False
    institution.updated_at = datetime.utcnow()

    session.add(institution)
    session.commit()
    session.refresh(institution)

    logger.info(f"Suspended tenant '{institution.name}' (slug: {institution.tenant_slug})")
    return institution


def deactivate_tenant(session: Session, institution_id: int) -> Institution | None:
    """Deactivate a tenant institution."""
    stmt = select(Institution).where(Institution.id == institution_id)
    institution = session.exec(stmt).first()

    if not institution:
        return None

    institution.status = "inactive"
    institution.is_active = False
    institution.updated_at = datetime.utcnow()

    session.add(institution)
    session.commit()
    session.refresh(institution)

    logger.info(f"Deactivated tenant '{institution.name}' (slug: {institution.tenant_slug})")
    return institution
