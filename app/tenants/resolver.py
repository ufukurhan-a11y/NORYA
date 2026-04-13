"""Tenant resolution middleware.

Intercepts requests to /hastane/{tenant_slug}/* paths, resolves the tenant,
validates access, and sets up the tenant context for the request lifecycle.
"""
import logging
import re
from datetime import datetime

from fastapi import Request, Response
from sqlmodel import Session, select

from app.core.database import engine, DATABASE_URL
from app.models.institution import Institution, InstitutionMembership
from app.models.security_log import SecurityLog
from .context import TenantContext, set_current_tenant, clear_current_tenant
from .schema_manager import set_tenant_search_path

logger = logging.getLogger(__name__)

# Pattern to match tenant paths: /hastane/{slug}/...
TENANT_PATH_PATTERN = re.compile(r"^/hastane/([^/]+)/")


async def tenant_resolver_middleware(request: Request, call_next) -> Response:
    """FastAPI middleware that resolves tenant from URL path.

    Only activates for /hastane/{tenant_slug}/* paths.
    """
    path = request.url.path

    match = TENANT_PATH_PATTERN.match(path)
    if not match:
        # Not a tenant path, continue normally
        return await call_next(request)

    tenant_slug = match.group(1)

    # Look up the institution by tenant_slug
    with Session(engine) as session:
        stmt = select(Institution).where(Institution.tenant_slug == tenant_slug)
        institution = session.exec(stmt).first()

        if not institution:
            # Tenant not found - 404
            logger.warning(f"Tenant not found: {tenant_slug}")
            return Response(
                content="Tenant not found",
                status_code=404,
                media_type="text/plain",
            )

        # Check if tenant is active
        if not institution.is_active or institution.status not in ("active", "trial"):
            logger.warning(f"Tenant is not active: {tenant_slug} (status={institution.status})")
            return Response(
                content="This tenant is currently unavailable",
                status_code=403,
                media_type="text/plain",
            )

        # Get user from request (if authenticated)
        user_id = _get_user_id_from_request(request)

        # Check user membership if user is authenticated
        user_role = None
        if user_id:
            membership_stmt = select(InstitutionMembership).where(
                InstitutionMembership.institution_id == institution.id,
                InstitutionMembership.user_id == user_id,
                InstitutionMembership.is_active == True,
            )
            membership = session.exec(membership_stmt).first()

            if membership:
                user_role = membership.role
            else:
                # User is authenticated but not a member of this tenant
                _log_security_event(
                    session=session,
                    event_type="cross_tenant_access_attempt",
                    user_id=user_id,
                    institution_id=institution.id,
                    detail=f"User {user_id} attempted to access tenant {tenant_slug} without membership",
                )
                return Response(
                    content="Access denied: you are not a member of this organization",
                    status_code=403,
                    media_type="text/plain",
                )

        # Set tenant context
        tenant_ctx = TenantContext(
            tenant_slug=tenant_slug,
            institution_id=institution.id,
            is_active=True,
            user_membership_role=user_role,
        )
        set_current_tenant(tenant_ctx)

        # For PostgreSQL, set search_path to tenant schema
        set_tenant_search_path(session, tenant_slug, DATABASE_URL)

    try:
        response = await call_next(request)
        return response
    finally:
        # Clean up tenant context after request
        clear_current_tenant()


def _get_user_id_from_request(request: Request) -> int | None:
    """Extract user_id from request state (set by auth middleware)."""
    # The auth middleware in main.py sets request.state.user
    user = getattr(request.state, "user", None)
    if user and hasattr(user, "id"):
        return user.id
    return None


def _log_security_event(
    session: Session,
    event_type: str,
    user_id: int,
    institution_id: int,
    detail: str,
) -> None:
    """Log a security event to the SecurityLog table."""
    try:
        log_entry = SecurityLog(
            user_id=user_id,
            event_type=event_type,
            ip_address="",
            user_agent="",
            detail=detail,
            severity="high",
            institution_id=institution_id,
            created_at=datetime.utcnow(),
        )
        session.add(log_entry)
        session.commit()
    except Exception as e:
        logger.error(f"Failed to log security event: {e}")
        session.rollback()
