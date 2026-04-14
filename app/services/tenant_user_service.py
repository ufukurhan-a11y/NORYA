"""Hospital tenant user management service.

Allows hospital admins to manage their internal users (doctors, staff).
"""

import logging
import secrets
from datetime import datetime

from sqlmodel import Session, select

from app.core.security import hash_password
from app.models.user import User
from app.models.institution import Institution

log = logging.getLogger(__name__)


class TenantUserCreateRequest:
    email: str
    full_name: str
    role: str  # admin | doctor | member
    phone: str | None = None


def create_tenant_user(
    db: Session,
    institution_id: int,
    email: str,
    full_name: str,
    role: str = "member",
    phone: str | None = None,
    created_by_user_id: int | None = None,
) -> dict:
    """Create a new user associated with a hospital tenant.

    Returns dict with success status and user or error message.
    """
    # Check if email already exists
    existing = db.exec(select(User).where(User.email == email.lower())).first()
    if existing:
        if existing.institution_id == institution_id:
            return {"success": False, "error": "Bu e-posta zaten bu hastanede kayıtlı."}
        else:
            return {"success": False, "error": "Bu e-posta başka bir hesap tarafından kullanılıyor."}

    # Generate temporary password
    temp_password = secrets.token_urlsafe(12)

    user = User(
        email=email.lower(),
        hashed_password=hash_password(temp_password),
        full_name=full_name,
        institution_id=institution_id,
        tenant_role=role,
        tenant_is_active=True,
        phone=phone,
        plan="free",  # Tenant users don't need pro plan
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    log.info(
        "TENANT_USER_CREATED: user_id=%s email=%s institution_id=%s role=%s by_user_id=%s",
        user.id,
        email,
        institution_id,
        role,
        created_by_user_id,
    )

    return {
        "success": True,
        "user": user,
        "temp_password": temp_password,  # Return for admin to share with user
    }


def get_tenant_users(
    db: Session,
    institution_id: int,
    limit: int = 50,
    offset: int = 0,
) -> list[User]:
    """Get all users associated with a hospital tenant."""
    stmt = (
        select(User)
        .where(User.institution_id == institution_id)
        .order_by(User.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    return list(db.exec(stmt).all())


def get_tenant_user(db: Session, institution_id: int, user_id: int) -> User | None:
    """Get a specific user from a hospital tenant."""
    stmt = select(User).where(
        User.id == user_id,
        User.institution_id == institution_id,
    )
    return db.exec(stmt).first()


def update_tenant_user(
    db: Session,
    institution_id: int,
    user_id: int,
    full_name: str | None = None,
    role: str | None = None,
    phone: str | None = None,
    tenant_is_active: bool | None = None,
) -> dict:
    """Update a tenant user's details."""
    user = get_tenant_user(db, institution_id, user_id)
    if not user:
        return {"success": False, "error": "Kullanıcı bulunamadı."}

    if full_name is not None:
        user.full_name = full_name
    if role is not None and role in ("admin", "doctor", "member"):
        user.tenant_role = role
    if phone is not None:
        user.phone = phone
    if tenant_is_active is not None:
        user.tenant_is_active = tenant_is_active

    db.add(user)
    db.commit()
    db.refresh(user)

    log.info("TENANT_USER_UPDATED: user_id=%s institution_id=%s", user_id, institution_id)
    return {"success": True, "user": user}


def reset_tenant_user_password(
    db: Session,
    institution_id: int,
    user_id: int,
) -> dict:
    """Reset a tenant user's password and return temporary password."""
    user = get_tenant_user(db, institution_id, user_id)
    if not user:
        return {"success": False, "error": "Kullanıcı bulunamadı."}

    temp_password = secrets.token_urlsafe(12)
    user.hashed_password = hash_password(temp_password)
    db.add(user)
    db.commit()

    log.info("TENANT_USER_PASSWORD_RESET: user_id=%s institution_id=%s", user_id, institution_id)
    return {"success": True, "temp_password": temp_password}


def delete_tenant_user(
    db: Session,
    institution_id: int,
    user_id: int,
) -> dict:
    """Soft-delete (deactivate) a tenant user."""
    user = get_tenant_user(db, institution_id, user_id)
    if not user:
        return {"success": False, "error": "Kullanıcı bulunamadı."}

    # Don't allow deleting the last admin
    if user.tenant_role == "admin":
        admin_count = db.exec(
            select(User).where(
                User.institution_id == institution_id,
                User.tenant_role == "admin",
                User.tenant_is_active == True,
            )
        ).all()
        if len(admin_count) <= 1:
            return {"success": False, "error": "Son yönetici silinemez."}

    user.tenant_is_active = False
    db.add(user)
    db.commit()

    log.info("TENANT_USER_DELETED: user_id=%s institution_id=%s", user_id, institution_id)
    return {"success": True}


def get_tenant_user_stats(db: Session, institution_id: int) -> dict:
    """Get user statistics for a hospital tenant."""
    total = db.exec(
        select(User).where(User.institution_id == institution_id)
    ).all()

    active = [u for u in total if u.tenant_is_active]
    admins = [u for u in total if u.tenant_role == "admin" and u.tenant_is_active]
    doctors = [u for u in total if u.tenant_role == "doctor" and u.tenant_is_active]
    members = [u for u in total if u.tenant_role == "member" and u.tenant_is_active]

    return {
        "total_users": len(total),
        "active_users": len(active),
        "admin_count": len(admins),
        "doctor_count": len(doctors),
        "member_count": len(members),
    }
