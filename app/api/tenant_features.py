"""Tenant feature APIs: audit logs, API keys, customization, stats, alerts."""
import hashlib
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from pydantic import BaseModel
from sqlmodel import Session, select

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.institution import Institution, InstitutionMembership
from app.models.tenant_audit_log import TenantAuditLog
from app.models.tenant_api_key import TenantApiKey
from app.services import (
    tenant_audit_service,
    tenant_api_key_service,
    tenant_alert_service,
    tenant_stats_service,
)
from app.tenants.isolation import require_tenant_active

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/tenant", tags=["tenant-features"])


# ==================== Audit Log APIs ====================

class AuditLogResponse(BaseModel):
    id: int
    action: str
    user_id: int | None
    entity_type: str | None
    entity_id: int | None
    detail: str | None
    ip_address: str | None
    created_at: str


@router.get("/audit-logs", response_model=list[AuditLogResponse])
async def get_audit_logs(
    action: str | None = Query(None),
    entity_type: str | None = Query(None),
    user_id: int | None = Query(None),
    limit: int = Query(100, le=500),
    offset: int = Query(0),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Get audit logs for current tenant."""
    logs = tenant_audit_service.get_tenant_audit_logs(
        db,
        tenant.id,
        limit=limit,
        offset=offset,
        action=action,
        entity_type=entity_type,
        user_id=user_id,
    )
    return [
        AuditLogResponse(
            id=log.id,
            action=log.action,
            user_id=log.user_id,
            entity_type=log.entity_type,
            entity_id=log.entity_id,
            detail=log.detail,
            ip_address=log.ip_address,
            created_at=log.created_at.isoformat() if log.created_at else None,
        )
        for log in logs
    ]


@router.get("/audit-stats")
async def get_audit_stats(
    days: int = Query(30, ge=1, le=365),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Get audit log statistics for current tenant."""
    return tenant_audit_service.get_tenant_audit_stats(db, tenant.id, days=days)


# ==================== API Key APIs ====================

class CreateApiKeyRequest(BaseModel):
    name: str
    expires_days: int | None = None


class CreateApiKeyResponse(BaseModel):
    success: bool
    raw_key: str  # Only shown once!
    key_id: int
    name: str
    key_prefix: str
    expires_at: str | None


class ApiKeyListItem(BaseModel):
    id: int
    name: str
    key_prefix: str
    is_active: bool
    last_used_at: str | None
    expires_at: str | None
    created_at: str


@router.post("/api-keys", response_model=CreateApiKeyResponse)
async def create_api_key(
    request: CreateApiKeyRequest,
    user: User = Depends(get_current_user),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Create a new API key for tenant integration."""
    # Check user has admin/owner role
    membership_stmt = select(InstitutionMembership).where(
        InstitutionMembership.institution_id == tenant.id,
        InstitutionMembership.user_id == user.id,
        InstitutionMembership.role.in_(["owner", "admin"]),
    )
    membership = db.exec(membership_stmt).first()
    if not membership:
        raise HTTPException(status_code=403, detail="Admin or owner role required")

    result = tenant_api_key_service.create_api_key(
        db,
        tenant.id,
        name=request.name,
        created_by_user_id=user.id,
        expires_days=request.expires_days,
    )

    # Log the action
    tenant_audit_service.log_tenant_action(
        db,
        institution_id=tenant.id,
        action="api_key_created",
        user_id=user.id,
        detail=f"API key '{request.name}' created",
    )

    return CreateApiKeyResponse(**result)


@router.get("/api-keys", response_model=list[ApiKeyListItem])
async def list_api_keys(
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """List all API keys for current tenant."""
    keys = tenant_api_key_service.get_api_keys(db, tenant.id)
    return [
        ApiKeyListItem(
            id=k.id,
            name=k.name,
            key_prefix=k.key_prefix,
            is_active=k.is_active,
            last_used_at=k.last_used_at.isoformat() if k.last_used_at else None,
            expires_at=k.expires_at.isoformat() if k.expires_at else None,
            created_at=k.created_at.isoformat() if k.created_at else None,
        )
        for k in keys
    ]


@router.post("/api-keys/{key_id}/revoke")
async def revoke_api_key(
    key_id: int,
    user: User = Depends(get_current_user),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Revoke an API key."""
    success = tenant_api_key_service.revoke_api_key(db, key_id, tenant.id)
    if not success:
        raise HTTPException(status_code=404, detail="API key not found")

    tenant_audit_service.log_tenant_action(
        db,
        institution_id=tenant.id,
        action="api_key_revoked",
        user_id=user.id,
        entity_type="api_key",
        entity_id=key_id,
        detail=f"API key {key_id} revoked",
    )

    return {"success": True, "message": "API key revoked"}


# ==================== Customization APIs ====================

class UpdateCustomizationRequest(BaseModel):
    logo_url: str | None = None
    primary_color: str | None = None
    secondary_color: str | None = None
    report_header_text: str | None = None
    report_footer_text: str | None = None
    custom_css: str | None = None


@router.get("/customization")
async def get_customization(
    tenant: Institution = Depends(require_tenant_active),
):
    """Get tenant customization settings."""
    return {
        "logo_url": tenant.logo_url,
        "primary_color": tenant.primary_color,
        "secondary_color": tenant.secondary_color,
        "report_header_text": tenant.report_header_text,
        "report_footer_text": tenant.report_footer_text,
        "custom_css": tenant.custom_css,
    }


@router.put("/customization")
async def update_customization(
    request: UpdateCustomizationRequest,
    user: User = Depends(get_current_user),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Update tenant customization settings."""
    # Check admin role
    membership_stmt = select(InstitutionMembership).where(
        InstitutionMembership.institution_id == tenant.id,
        InstitutionMembership.user_id == user.id,
        InstitutionMembership.role.in_(["owner", "admin"]),
    )
    membership = db.exec(membership_stmt).first()
    if not membership:
        raise HTTPException(status_code=403, detail="Admin or owner role required")

    if request.logo_url is not None:
        tenant.logo_url = request.logo_url
    if request.primary_color is not None:
        tenant.primary_color = request.primary_color
    if request.secondary_color is not None:
        tenant.secondary_color = request.secondary_color
    if request.report_header_text is not None:
        tenant.report_header_text = request.report_header_text
    if request.report_footer_text is not None:
        tenant.report_footer_text = request.report_footer_text
    if request.custom_css is not None:
        tenant.custom_css = request.custom_css

    tenant.updated_at = datetime.utcnow()
    db.add(tenant)
    db.commit()

    tenant_audit_service.log_tenant_action(
        db,
        institution_id=tenant.id,
        action="settings_change",
        user_id=user.id,
        entity_type="settings",
        detail="Customization settings updated",
    )

    return {"success": True, "message": "Customization updated"}


# ==================== Stats APIs ====================

@router.get("/stats")
async def get_tenant_stats(
    days: int = Query(30, ge=1, le=365),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Get comprehensive statistics for tenant dashboard."""
    return tenant_stats_service.get_tenant_stats(db, tenant.id, days=days)


# ==================== Alert APIs ====================

@router.get("/alerts/low-balance")
async def get_low_balance_status(
    tenant: Institution = Depends(require_tenant_active),
):
    """Get current low balance alert status."""
    return {
        "balance": tenant.billing_wallet_balance,
        "balance_formatted": f"${tenant.billing_wallet_balance / 100:.2f}",
        "threshold": tenant.wallet_low_threshold,
        "threshold_formatted": f"${tenant.wallet_low_threshold / 100:.2f}",
        "is_low": tenant.billing_wallet_balance <= tenant.wallet_low_threshold,
        "alert_email_enabled": tenant.alert_email_enabled,
        "alert_sms_enabled": tenant.alert_sms_enabled,
        "last_alert_at": tenant.wallet_last_alert.isoformat() if tenant.wallet_last_alert else None,
    }


@router.post("/alerts/test-low-balance")
async def test_low_balance_alert(
    user: User = Depends(get_current_user),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Send a test low balance alert email."""
    success = tenant_alert_service.send_manual_low_balance_alert(db, tenant.id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to send alert email")

    return {"success": True, "message": "Test alert email sent"}


@router.put("/alerts/settings")
async def update_alert_settings(
    alert_email_enabled: bool,
    alert_sms_enabled: bool | None = None,
    alert_phone: str | None = None,
    user: User = Depends(get_current_user),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Update alert settings for tenant."""
    membership_stmt = select(InstitutionMembership).where(
        InstitutionMembership.institution_id == tenant.id,
        InstitutionMembership.user_id == user.id,
        InstitutionMembership.role.in_(["owner", "admin"]),
    )
    membership = db.exec(membership_stmt).first()
    if not membership:
        raise HTTPException(status_code=403, detail="Admin or owner role required")

    tenant.alert_email_enabled = alert_email_enabled
    if alert_sms_enabled is not None:
        tenant.alert_sms_enabled = alert_sms_enabled
    if alert_phone is not None:
        tenant.alert_phone = alert_phone

    tenant.updated_at = datetime.utcnow()
    db.add(tenant)
    db.commit()

    return {"success": True, "message": "Alert settings updated"}
