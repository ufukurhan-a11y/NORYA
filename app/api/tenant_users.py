"""Tenant user management API endpoints.

Hospital admins can manage their internal users (doctors, staff).
"""

import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlmodel import Session

from app.core.database import get_db
from app.tenants.isolation import require_tenant_active
from app.models.institution import Institution
from app.services import tenant_user_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/tenant/users", tags=["tenant-users"])


class CreateUserRequest(BaseModel):
    email: str
    full_name: str
    role: str = "member"  # admin | doctor | member
    phone: str | None = None


class UpdateUserRequest(BaseModel):
    full_name: str | None = None
    role: str | None = None
    phone: str | None = None
    tenant_is_active: bool | None = None


@router.get("/")
async def list_tenant_users(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """List all users for current tenant."""
    users = tenant_user_service.get_tenant_users(db, tenant.id, limit=limit, offset=offset)
    return [
        {
            "id": u.id,
            "email": u.email,
            "full_name": u.full_name,
            "role": u.tenant_role,
            "phone": u.phone,
            "is_active": u.tenant_is_active,
            "created_at": u.created_at.isoformat() if u.created_at else None,
            "last_login_at": u.last_login_at.isoformat() if u.last_login_at else None,
        }
        for u in users
    ]


@router.get("/stats")
async def get_tenant_user_stats(
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Get user statistics for current tenant."""
    return tenant_user_service.get_tenant_user_stats(db, tenant.id)


@router.post("/")
async def create_tenant_user(
    request: CreateUserRequest,
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Create a new user for current tenant."""
    if request.role not in ("admin", "doctor", "member"):
        raise HTTPException(status_code=400, detail="Geçersiz rol. admin, doctor veya member olmalı.")

    result = tenant_user_service.create_tenant_user(
        db,
        tenant.id,
        email=request.email,
        full_name=request.full_name,
        role=request.role,
        phone=request.phone,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])

    return {
        "success": True,
        "user": {
            "id": result["user"].id,
            "email": result["user"].email,
            "full_name": result["user"].full_name,
            "role": result["user"].tenant_role,
        },
        "temp_password": result["temp_password"],
        "message": "Kullanıcı oluşturuldu. Geçici şifreyi kullanıcı ile paylaşın.",
    }


@router.put("/{user_id}")
async def update_tenant_user(
    user_id: int,
    request: UpdateUserRequest,
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Update a tenant user's details."""
    if request.role and request.role not in ("admin", "doctor", "member"):
        raise HTTPException(status_code=400, detail="Geçersiz rol.")

    result = tenant_user_service.update_tenant_user(
        db,
        tenant.id,
        user_id,
        full_name=request.full_name,
        role=request.role,
        phone=request.phone,
        tenant_is_active=request.tenant_is_active,
    )

    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["error"])

    return {
        "success": True,
        "user": {
            "id": result["user"].id,
            "email": result["user"].email,
            "full_name": result["user"].full_name,
            "role": result["user"].tenant_role,
            "is_active": result["user"].tenant_is_active,
        },
    }


@router.post("/{user_id}/reset-password")
async def reset_user_password(
    user_id: int,
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Reset a tenant user's password."""
    result = tenant_user_service.reset_tenant_user_password(db, tenant.id, user_id)

    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["error"])

    return {
        "success": True,
        "temp_password": result["temp_password"],
        "message": "Şifre sıfırlandı. Geçici şifreyi kullanıcı ile paylaşın.",
    }


@router.delete("/{user_id}")
async def delete_tenant_user(
    user_id: int,
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Deactivate a tenant user."""
    result = tenant_user_service.delete_tenant_user(db, tenant.id, user_id)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])

    return {"success": True, "message": "Kullanıcı devre dışı bırakıldı."}
