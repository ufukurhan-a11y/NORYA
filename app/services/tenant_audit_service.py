"""Tenant audit logging service.

Records all tenant-scoped activities for KVKK/GDPR compliance and internal auditing.
"""
import json
import logging
from datetime import datetime

from sqlmodel import Session, select

from app.models.tenant_audit_log import TenantAuditLog

logger = logging.getLogger(__name__)


def log_tenant_action(
    session: Session,
    institution_id: int,
    action: str,
    user_id: int | None = None,
    entity_type: str | None = None,
    entity_id: int | None = None,
    ip_address: str | None = None,
    user_agent: str | None = None,
    detail: str | None = None,
    metadata: dict | None = None,
) -> TenantAuditLog:
    """Log a tenant-scoped action.

    Args:
        session: Database session
        institution_id: Institution ID
        action: Action type (login, logout, upload, analyze, download, export, settings_change, etc.)
        user_id: User who performed the action
        entity_type: Type of entity affected (case, report, user, settings)
        entity_id: ID of the affected entity
        ip_address: Client IP
        user_agent: Client user agent
        detail: Human-readable description
        metadata: Extra JSON-serializable data

    Returns:
        Created TenantAuditLog record
    """
    log_entry = TenantAuditLog(
        institution_id=institution_id,
        user_id=user_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        ip_address=ip_address,
        user_agent=user_agent,
        detail=detail,
        metadata_json=json.dumps(metadata) if metadata else None,
        created_at=datetime.utcnow(),
    )
    session.add(log_entry)
    session.commit()
    session.refresh(log_entry)
    return log_entry


def get_tenant_audit_logs(
    session: Session,
    institution_id: int,
    limit: int = 100,
    offset: int = 0,
    action: str | None = None,
    user_id: int | None = None,
    entity_type: str | None = None,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
) -> list[TenantAuditLog]:
    """Get audit logs for a tenant with optional filters."""
    stmt = select(TenantAuditLog).where(
        TenantAuditLog.institution_id == institution_id
    )

    if action:
        stmt = stmt.where(TenantAuditLog.action == action)
    if user_id:
        stmt = stmt.where(TenantAuditLog.user_id == user_id)
    if entity_type:
        stmt = stmt.where(TenantAuditLog.entity_type == entity_type)
    if date_from:
        stmt = stmt.where(TenantAuditLog.created_at >= date_from)
    if date_to:
        stmt = stmt.where(TenantAuditLog.created_at <= date_to)

    stmt = stmt.order_by(TenantAuditLog.created_at.desc()).offset(offset).limit(limit)
    return list(session.exec(stmt).all())


def get_tenant_audit_stats(
    session: Session,
    institution_id: int,
    days: int = 30,
) -> dict:
    """Get audit log statistics for a tenant."""
    from datetime import timedelta

    cutoff = datetime.utcnow() - timedelta(days=days)

    stmt = select(TenantAuditLog).where(
        TenantAuditLog.institution_id == institution_id,
        TenantAuditLog.created_at >= cutoff,
    )
    logs = session.exec(stmt).all()

    action_counts = {}
    user_counts = {}
    for log in logs:
        action_counts[log.action] = action_counts.get(log.action, 0) + 1
        if log.user_id:
            user_counts[log.user_id] = user_counts.get(log.user_id, 0) + 1

    return {
        "total_actions": len(logs),
        "action_counts": action_counts,
        "unique_users": len(user_counts),
        "user_counts": user_counts,
        "period_days": days,
    }
