"""Tenant-scoped portal routes.

Routes under /hastane/{tenant_slug}/ for hospital staff to access their isolated environment.
"""
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session, select

from app.core.database import get_db
from app.core.templating import templates
from app.models.institution import Institution, InstitutionMembership
from app.models.enterprise_case import EnterpriseCase
from app.models.tenant_wallet_transaction import TenantWalletTransaction
from app.models.tenant_audit_log import TenantAuditLog
from app.models.tenant_api_key import TenantApiKey
from app.api.deps import get_current_user
from app.models.user import User
from app.services import tenant_stats_service, tenant_audit_service, tenant_api_key_service
from .context import get_current_tenant
from .isolation import require_tenant_active, get_current_institution_id

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/hastane/{tenant_slug}", tags=["tenant-portal"])


def _require_admin(tenant: Institution, user: User, db: Session) -> bool:
    """Check if user has admin/owner role in tenant."""
    membership_stmt = select(InstitutionMembership).where(
        InstitutionMembership.institution_id == tenant.id,
        InstitutionMembership.user_id == user.id,
        InstitutionMembership.role.in_(["owner", "admin"]),
    )
    return db.exec(membership_stmt).first() is not None


@router.get("/dashboard")
async def tenant_dashboard(
    request: Request,
    tenant: Institution = Depends(require_tenant_active),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Hospital dashboard showing overview stats."""
    institution_id = tenant.id

    # Get comprehensive stats
    stats = tenant_stats_service.get_tenant_stats(db, institution_id, days=30)

    # Get wallet balance
    wallet_balance = tenant.billing_wallet_balance
    cost_per_analysis = tenant.cost_per_analysis
    remaining_analyses = wallet_balance // cost_per_analysis if cost_per_analysis > 0 else 0
    is_low_balance = wallet_balance <= tenant.wallet_low_threshold

    return templates.TemplateResponse(
        "tenant/dashboard.html",
        {
            "request": request,
            "tenant": tenant,
            "tenant_slug": tenant.tenant_slug,
            "user": user,
            "stats": stats,
            "total_cases": stats["total_cases"],
            "status_counts": stats["status_counts"],
            "wallet_balance": wallet_balance,
            "wallet_balance_formatted": f"${wallet_balance / 100:.2f}",
            "cost_per_analysis": cost_per_analysis,
            "cost_per_analysis_formatted": f"${cost_per_analysis / 100:.2f}",
            "remaining_analyses": remaining_analyses,
            "is_low_balance": is_low_balance,
            "daily_breakdown": stats["daily_breakdown"],
            "top_users": stats["top_users"],
        },
    )


@router.get("/cases")
async def tenant_cases(
    request: Request,
    tenant: Institution = Depends(require_tenant_active),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List all cases for this tenant."""
    institution_id = tenant.id

    cases = db.exec(
        select(EnterpriseCase)
        .where(EnterpriseCase.institution_id == institution_id)
        .order_by(EnterpriseCase.created_at.desc())
    ).all()

    return templates.TemplateResponse(
        "tenant/cases.html",
        {
            "request": request,
            "tenant": tenant,
            "tenant_slug": tenant.tenant_slug,
            "user": user,
            "cases": cases,
        },
    )


@router.get("/billing")
async def tenant_billing(
    request: Request,
    tenant: Institution = Depends(require_tenant_active),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Wallet balance and transaction history."""
    institution_id = tenant.id

    # Get recent transactions
    transactions = db.exec(
        select(TenantWalletTransaction)
        .where(TenantWalletTransaction.institution_id == institution_id)
        .order_by(TenantWalletTransaction.created_at.desc())
        .limit(50)
    ).all()

    wallet_balance = tenant.billing_wallet_balance
    cost_per_analysis = tenant.cost_per_analysis
    remaining_analyses = wallet_balance // cost_per_analysis if cost_per_analysis > 0 else 0
    is_low_balance = wallet_balance <= tenant.wallet_low_threshold

    return templates.TemplateResponse(
        "tenant/billing.html",
        {
            "request": request,
            "tenant": tenant,
            "tenant_slug": tenant.tenant_slug,
            "user": user,
            "wallet_balance": wallet_balance,
            "wallet_balance_formatted": f"${wallet_balance / 100:.2f}",
            "cost_per_analysis": cost_per_analysis,
            "cost_per_analysis_formatted": f"${cost_per_analysis / 100:.2f}",
            "remaining_analyses": remaining_analyses,
            "is_low_balance": is_low_balance,
            "transactions": transactions,
        },
    )


@router.get("/settings")
async def tenant_settings(
    request: Request,
    tenant: Institution = Depends(require_tenant_active),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Tenant settings page (customization, alerts, rate limits)."""
    is_admin = _require_admin(tenant, user, db)

    return templates.TemplateResponse(
        "tenant/settings.html",
        {
            "request": request,
            "tenant": tenant,
            "tenant_slug": tenant.tenant_slug,
            "user": user,
            "is_admin": is_admin,
        },
    )


@router.get("/audit-log")
async def tenant_audit_log_page(
    request: Request,
    tenant: Institution = Depends(require_tenant_active),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Tenant audit log viewer."""
    logs = tenant_audit_service.get_tenant_audit_logs(db, tenant.id, limit=100)

    return templates.TemplateResponse(
        "tenant/audit_log.html",
        {
            "request": request,
            "tenant": tenant,
            "tenant_slug": tenant.tenant_slug,
            "user": user,
            "logs": logs,
        },
    )


@router.get("/api-keys")
async def tenant_api_keys_page(
    request: Request,
    tenant: Institution = Depends(require_tenant_active),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Tenant API key management page."""
    is_admin = _require_admin(tenant, user, db)
    keys = tenant_api_key_service.get_api_keys(db, tenant.id)

    return templates.TemplateResponse(
        "tenant/api_keys.html",
        {
            "request": request,
            "tenant": tenant,
            "tenant_slug": tenant.tenant_slug,
            "user": user,
            "is_admin": is_admin,
            "api_keys": keys,
        },
    )


@router.get("/users")
async def tenant_users_page(
    request: Request,
    tenant: Institution = Depends(require_tenant_active),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Tenant user management page (hospital admin panel)."""
    is_admin = _require_admin(tenant, user, db)

    return templates.TemplateResponse(
        "tenant/users.html",
        {
            "request": request,
            "tenant": tenant,
            "tenant_slug": tenant.tenant_slug,
            "user": user,
            "is_admin": is_admin,
        },
    )
