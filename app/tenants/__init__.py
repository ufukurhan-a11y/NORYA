"""Multi-tenant module for hospital-specific isolated environments."""
from .context import TenantContext, get_current_tenant, set_current_tenant
from .resolver import tenant_resolver_middleware
from .isolation import require_tenant_active, enforce_tenant_boundary
from .security import log_cross_tenant_attempt, enforce_user_tenant_membership

__all__ = [
    "TenantContext",
    "get_current_tenant",
    "set_current_tenant",
    "tenant_resolver_middleware",
    "require_tenant_active",
    "enforce_tenant_boundary",
    "log_cross_tenant_attempt",
    "enforce_user_tenant_membership",
]
