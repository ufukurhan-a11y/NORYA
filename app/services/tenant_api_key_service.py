"""Tenant API Key management service.

Handles creation, validation, and rotation of API keys for hospital integrations.
"""
import hashlib
import logging
import secrets
from datetime import datetime

from sqlmodel import Session, select

from app.models.tenant_api_key import TenantApiKey

logger = logging.getLogger(__name__)

# API key prefix for identification
API_KEY_PREFIX = "norya_tk_"


def generate_api_key() -> tuple[str, str]:
    """Generate a new API key.

    Returns:
        Tuple of (raw_key, key_hash)
        raw_key: The full key to show to the user (only shown once)
        key_hash: SHA-256 hash to store in DB
    """
    raw_key = API_KEY_PREFIX + secrets.token_urlsafe(32)
    key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
    key_prefix = raw_key[:16]  # First 16 chars for display
    return raw_key, key_hash, key_prefix


def create_api_key(
    session: Session,
    institution_id: int,
    name: str,
    created_by_user_id: int | None = None,
    expires_days: int | None = None,
) -> dict:
    """Create a new API key for a tenant.

    Args:
        session: Database session
        institution_id: Institution ID
        name: Key name/description
        created_by_user_id: User who created the key
        expires_days: Key expires in N days (None = never)

    Returns:
        dict with raw_key (shown once) and key metadata
    """
    raw_key, key_hash, key_prefix = generate_api_key()

    expires_at = None
    if expires_days:
        from datetime import timedelta
        expires_at = datetime.utcnow() + timedelta(days=expires_days)

    api_key = TenantApiKey(
        institution_id=institution_id,
        name=name,
        key_hash=key_hash,
        key_prefix=key_prefix,
        is_active=True,
        expires_at=expires_at,
        created_by_user_id=created_by_user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(api_key)
    session.commit()
    session.refresh(api_key)

    logger.info(f"Created API key '{name}' for institution {institution_id}")

    return {
        "success": True,
        "raw_key": raw_key,  # Only shown once!
        "key_id": api_key.id,
        "name": api_key.name,
        "key_prefix": api_key.key_prefix,
        "expires_at": api_key.expires_at.isoformat() if api_key.expires_at else None,
    }


def validate_api_key(session: Session, raw_key: str) -> TenantApiKey | None:
    """Validate an API key and return the associated record.

    Updates last_used_at on successful validation.

    Args:
        session: Database session
        raw_key: The raw API key from the request

    Returns:
        TenantApiKey if valid, None otherwise
    """
    key_hash = hashlib.sha256(raw_key.encode()).hexdigest()

    stmt = select(TenantApiKey).where(
        TenantApiKey.key_hash == key_hash,
        TenantApiKey.is_active == True,
    )
    api_key = session.exec(stmt).first()

    if not api_key:
        return None

    # Check expiration
    if api_key.expires_at and api_key.expires_at < datetime.utcnow():
        return None

    # Update last used
    api_key.last_used_at = datetime.utcnow()
    session.add(api_key)
    session.commit()

    return api_key


def revoke_api_key(session: Session, key_id: int, institution_id: int) -> bool:
    """Revoke (deactivate) an API key."""
    stmt = select(TenantApiKey).where(
        TenantApiKey.id == key_id,
        TenantApiKey.institution_id == institution_id,
    )
    api_key = session.exec(stmt).first()

    if not api_key:
        return False

    api_key.is_active = False
    api_key.updated_at = datetime.utcnow()
    session.add(api_key)
    session.commit()

    logger.info(f"Revoked API key {key_id} for institution {institution_id}")
    return True


def get_api_keys(
    session: Session,
    institution_id: int,
) -> list[TenantApiKey]:
    """Get all API keys for a tenant."""
    stmt = (
        select(TenantApiKey)
        .where(TenantApiKey.institution_id == institution_id)
        .order_by(TenantApiKey.created_at.desc())
    )
    return list(session.exec(stmt).all())
