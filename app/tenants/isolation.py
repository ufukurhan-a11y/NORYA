"""Tenant isolation enforcement.

Provides dependencies and utilities to ensure tenant-scoped operations
cannot access data from other tenants.
"""
import logging
from typing import Optional

from fastapi import Depends, HTTPException, Request
from sqlmodel import Session, select

from app.core.database import get_db
from app.models.institution import Institution
from .context import get_current_tenant, TenantContext

logger = logging.getLogger(__name__)


def require_tenant_active(
    request: Request,
    db: Session = Depends(get_db),
) -> Institution:
    """FastAPI dependency that ensures the current tenant is active.

    Returns the Institution object for the current tenant.
    Raises 404 if no tenant context, 403 if tenant is not active.
    """
    tenant_ctx = get_current_tenant()

    if not tenant_ctx:
        raise HTTPException(status_code=404, detail="Tenant context not found")

    stmt = select(Institution).where(
        Institution.id == tenant_ctx.institution_id,
        Institution.is_active == True,
    )
    institution = db.exec(stmt).first()

    if not institution:
        raise HTTPException(status_code=404, detail="Tenant not found")

    if institution.status not in ("active", "trial"):
        raise HTTPException(
            status_code=403,
            detail=f"Tenant is not active (status: {institution.status})",
        )

    return institution


def enforce_tenant_boundary(
    query,
    institution_id: Optional[int] = None,
    tenant_ctx: Optional[TenantContext] = None,
):
    """Enforce tenant boundary on a SQLModel query.

    Appends WHERE institution_id = {current_tenant_id} to the query.

    Usage:
        stmt = select(EnterpriseCase)
        stmt = enforce_tenant_boundary(stmt)
        cases = db.exec(stmt).all()
    """
    if tenant_ctx is None:
        tenant_ctx = get_current_tenant()

    if tenant_ctx:
        inst_id = tenant_ctx.institution_id
    elif institution_id:
        inst_id = institution_id
    else:
        # No tenant context - this is a B2C request, no filtering needed
        return query

    return query.where(getattr(query._raw_columns[0].entity.class_, "institution_id", None) == inst_id) if query._raw_columns else query


def get_current_institution_id() -> Optional[int]:
    """Get the current tenant's institution_id from context."""
    tenant_ctx = get_current_tenant()
    if tenant_ctx:
        return tenant_ctx.institution_id
    return None


def require_tenant_context() -> TenantContext:
    """FastAPI dependency that requires a tenant context to be present."""
    tenant_ctx = get_current_tenant()
    if not tenant_ctx:
        raise HTTPException(status_code=404, detail="Tenant context not found")
    return tenant_ctx
