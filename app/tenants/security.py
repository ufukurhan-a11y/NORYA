"""Cross-tenant access prevention and security enforcement.

Multi-layered security:
1. Query-level enforcement
2. Middleware-level validation
3. API-level verification
4. Audit logging
"""
import logging
from datetime import datetime

from sqlmodel import Session, select

from app.models.institution import InstitutionMembership
from app.models.security_log import SecurityLog

logger = logging.getLogger(__name__)


def log_cross_tenant_attempt(
    session: Session,
    user_id: int,
    target_institution_id: int,
    detail: str,
    ip_address: str = "",
    user_agent: str = "",
) -> None:
    """Log a cross-tenant access attempt to SecurityLog."""
    try:
        log_entry = SecurityLog(
            user_id=user_id,
            event_type="cross_tenant_access_attempt",
            ip_address=ip_address,
            user_agent=user_agent,
            detail=detail,
            severity="high",
            institution_id=target_institution_id,
            created_at=datetime.utcnow(),
        )
        session.add(log_entry)
        session.commit()
        logger.warning(
            f"Cross-tenant access attempt: user={user_id}, "
            f"target_institution={target_institution_id}, detail={detail}"
        )
    except Exception as e:
        logger.error(f"Failed to log cross-tenant access attempt: {e}")
        session.rollback()


def enforce_user_tenant_membership(
    session: Session,
    user_id: int,
    institution_id: int,
    required_role: str | None = None,
) -> InstitutionMembership | None:
    """Verify that a user belongs to the specified institution.

    Returns the InstitutionMembership if valid, None otherwise.
    Logs a security event if membership is not found.
    """
    stmt = select(InstitutionMembership).where(
        InstitutionMembership.user_id == user_id,
        InstitutionMembership.institution_id == institution_id,
        InstitutionMembership.is_active == True,
    )
    membership = session.exec(stmt).first()

    if not membership:
        log_cross_tenant_attempt(
            session=session,
            user_id=user_id,
            target_institution_id=institution_id,
            detail=f"User {user_id} attempted to access institution {institution_id} without membership",
        )
        return None

    if required_role and membership.role != required_role:
        log_cross_tenant_attempt(
            session=session,
            user_id=user_id,
            target_institution_id=institution_id,
            detail=f"User {user_id} has role '{membership.role}', required '{required_role}'",
        )
        return None

    return membership


def validate_institution_access(
    session: Session,
    user_id: int,
    institution_id: int,
    raise_on_fail: bool = True,
) -> bool:
    """Validate that a user can access the given institution.

    Returns True if access is valid, False otherwise.
    Raises HTTPException if raise_on_fail is True and access is denied.
    """
    from fastapi import HTTPException

    membership = enforce_user_tenant_membership(session, user_id, institution_id)

    if not membership:
        if raise_on_fail:
            raise HTTPException(
                status_code=403,
                detail="Access denied: you do not have access to this organization",
            )
        return False

    return True
