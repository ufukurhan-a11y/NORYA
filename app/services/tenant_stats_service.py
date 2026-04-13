"""Tenant dashboard statistics service.

Provides daily/weekly/monthly analytics for tenant dashboards.
"""
import logging
from datetime import datetime, timedelta

from sqlmodel import Session, select, func

from app.models.enterprise_case import EnterpriseCase
from app.models.tenant_audit_log import TenantAuditLog
from app.models.tenant_wallet_transaction import TenantWalletTransaction
from app.models.user import User
from app.models.institution import InstitutionMembership

logger = logging.getLogger(__name__)


def get_tenant_stats(
    session: Session,
    institution_id: int,
    days: int = 30,
) -> dict:
    """Get comprehensive statistics for a tenant dashboard."""
    cutoff = datetime.utcnow() - timedelta(days=days)

    # Total cases
    total_cases = session.exec(
        select(func.count(EnterpriseCase.id)).where(
            EnterpriseCase.institution_id == institution_id
        )
    ).first() or 0

    # Cases by status
    status_counts = {}
    status_rows = session.exec(
        select(EnterpriseCase.status, func.count(EnterpriseCase.id))
        .where(EnterpriseCase.institution_id == institution_id)
        .group_by(EnterpriseCase.status)
    ).all()
    for status, count in status_rows:
        status_counts[status] = count

    # Cases in period
    cases_in_period = session.exec(
        select(func.count(EnterpriseCase.id)).where(
            EnterpriseCase.institution_id == institution_id,
            EnterpriseCase.created_at >= cutoff,
        )
    ).first() or 0

    # Active users (users who performed actions in period)
    active_users = session.exec(
        select(func.count(func.distinct(TenantAuditLog.user_id))).where(
            TenantAuditLog.institution_id == institution_id,
            TenantAuditLog.created_at >= cutoff,
            TenantAuditLog.user_id.isnot(None),
        )
    ).first() or 0

    # Total members
    total_members = session.exec(
        select(func.count(InstitutionMembership.id)).where(
            InstitutionMembership.institution_id == institution_id,
            InstitutionMembership.is_active == True,
        )
    ).first() or 0

    # Wallet stats
    wallet_spent = session.exec(
        select(func.sum(TenantWalletTransaction.amount_cents)).where(
            TenantWalletTransaction.institution_id == institution_id,
            TenantWalletTransaction.amount_cents < 0,
            TenantWalletTransaction.created_at >= cutoff,
        )
    ).first() or 0

    wallet_loaded = session.exec(
        select(func.sum(TenantWalletTransaction.amount_cents)).where(
            TenantWalletTransaction.institution_id == institution_id,
            TenantWalletTransaction.amount_cents > 0,
            TenantWalletTransaction.created_at >= cutoff,
        )
    ).first() or 0

    # Top users by activity
    top_users_stmt = (
        select(User.full_name, func.count(TenantAuditLog.id).label("action_count"))
        .join(TenantAuditLog, User.id == TenantAuditLog.user_id)
        .where(
            TenantAuditLog.institution_id == institution_id,
            TenantAuditLog.created_at >= cutoff,
        )
        .group_by(User.full_name)
        .order_by(func.count(TenantAuditLog.id).desc())
        .limit(10)
    )
    top_users = [
        {"name": name, "actions": count}
        for name, count in session.exec(top_users_stmt).all()
    ]

    # Daily breakdown (last 7 days)
    daily_breakdown = []
    for i in range(7):
        day_start = datetime.utcnow() - timedelta(days=6 - i)
        day_end = day_start + timedelta(days=1)
        day_cases = session.exec(
            select(func.count(EnterpriseCase.id)).where(
                EnterpriseCase.institution_id == institution_id,
                EnterpriseCase.created_at >= day_start,
                EnterpriseCase.created_at < day_end,
            )
        ).first() or 0
        daily_breakdown.append({
            "date": day_start.strftime("%Y-%m-%d"),
            "cases": day_cases,
        })

    return {
        "total_cases": total_cases,
        "cases_in_period": cases_in_period,
        "period_days": days,
        "status_counts": status_counts,
        "active_users": active_users,
        "total_members": total_members,
        "wallet_spent_cents": abs(wallet_spent),
        "wallet_spent_formatted": f"${abs(wallet_spent) / 100:.2f}",
        "wallet_loaded_cents": wallet_loaded,
        "wallet_loaded_formatted": f"${wallet_loaded / 100:.2f}",
        "top_users": top_users,
        "daily_breakdown": daily_breakdown,
    }
