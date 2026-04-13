"""Tenant context management using contextvars for request-scoped tenant state."""
from contextvars import ContextVar
from dataclasses import dataclass
from typing import Optional


@dataclass
class TenantContext:
    """Request-scoped tenant context."""
    tenant_slug: str
    institution_id: int
    is_active: bool
    user_membership_role: Optional[str] = None


# Context variable for current tenant
_current_tenant: ContextVar[Optional[TenantContext]] = ContextVar("current_tenant", default=None)


def get_current_tenant() -> Optional[TenantContext]:
    """Get the current tenant context for this request."""
    return _current_tenant.get()


def set_current_tenant(ctx: TenantContext) -> None:
    """Set the current tenant context for this request."""
    _current_tenant.set(ctx)


def clear_current_tenant() -> None:
    """Clear the current tenant context."""
    _current_tenant.set(None)
