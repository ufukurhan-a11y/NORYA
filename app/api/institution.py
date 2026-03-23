"""Kurum API: davet kabul, üye listeleme, üye çıkarma, kurum bilgileri."""
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlmodel import Session, select, func

from app.api.deps import get_current_user
from app.core.database import get_db
from app.core.templating import Jinja2Templates
from app.models import AnalysisRecord, AuditLog, User
from app.models.institution import Institution, InstitutionInvite, InstitutionMembership

log = logging.getLogger("norya.institution")
router = APIRouter(prefix="/api/institution", tags=["institution"])
templates = Jinja2Templates(directory="app/templates")


def _get_membership(db: Session, user_id: int, institution_id: int) -> InstitutionMembership | None:
    return db.exec(
        select(InstitutionMembership).where(
            InstitutionMembership.user_id == user_id,
            InstitutionMembership.institution_id == institution_id,
            InstitutionMembership.is_active == True,
        )
    ).first()


def _require_institution_admin(db: Session, user_id: int, institution_id: int) -> InstitutionMembership:
    m = _get_membership(db, user_id, institution_id)
    if not m or m.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Bu kurum için yönetici yetkisine sahip değilsiniz.")
    return m


class InviteRequest(BaseModel):
    email: str
    role: str = "member"


class RemoveMemberRequest(BaseModel):
    user_id: int


# --- Enterprise admin APIs ---

@router.get("/my")
def get_my_institutions(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    memberships = list(db.exec(
        select(InstitutionMembership).where(
            InstitutionMembership.user_id == user.id,
            InstitutionMembership.is_active == True,
        )
    ).all())
    if not memberships:
        return {"institutions": []}
    inst_ids = [m.institution_id for m in memberships]
    institutions = list(db.exec(select(Institution).where(Institution.id.in_(inst_ids))).all())
    inst_map = {i.id: i for i in institutions}
    role_map = {m.institution_id: m.role for m in memberships}
    return {
        "institutions": [
            {
                "id": i.id,
                "name": i.name,
                "type": i.type,
                "role": role_map.get(i.id, "member"),
                "monthly_quota": i.monthly_quota,
                "quota_used": i.quota_used_this_month,
                "is_active": i.is_active,
            }
            for i in institutions if inst_map.get(i.id)
        ]
    }


@router.get("/{institution_id}/members")
def list_members(
    institution_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_institution_admin(db, user.id, institution_id)
    memberships = list(db.exec(
        select(InstitutionMembership).where(InstitutionMembership.institution_id == institution_id)
    ).all())
    user_ids = [m.user_id for m in memberships]
    users = {u.id: u for u in db.exec(select(User).where(User.id.in_(user_ids))).all()} if user_ids else {}
    return {
        "members": [
            {
                "membership_id": m.id,
                "user_id": m.user_id,
                "email": users[m.user_id].email if m.user_id in users else "",
                "full_name": (users[m.user_id].full_name if m.user_id in users else "") or "",
                "role": m.role,
                "is_active": m.is_active,
                "accepted_at": m.accepted_at.isoformat() if m.accepted_at else None,
            }
            for m in memberships
        ]
    }


@router.post("/{institution_id}/invite")
def invite_member(
    institution_id: int,
    body: InviteRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    import secrets
    from datetime import timedelta
    _require_institution_admin(db, user.id, institution_id)
    inst = db.get(Institution, institution_id)
    if not inst or not inst.is_active:
        raise HTTPException(status_code=404, detail="Kurum bulunamadı veya pasif.")
    email = body.email.strip().lower()
    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail="Geçerli bir e-posta girin.")
    role = body.role if body.role in ("admin", "reviewer", "member") else "member"
    token = secrets.token_urlsafe(48)
    invite = InstitutionInvite(
        institution_id=institution_id,
        email=email,
        role=role,
        token=token,
        invited_by=user.id,
        expires_at=datetime.utcnow() + timedelta(days=30),
    )
    db.add(invite)
    db.commit()
    db.refresh(invite)
    return {
        "ok": True,
        "invite_token": token,
        "join_url": f"/institution/join/{token}",
    }


@router.delete("/{institution_id}/members/{target_user_id}")
def remove_member(
    institution_id: int,
    target_user_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_institution_admin(db, user.id, institution_id)
    if target_user_id == user.id:
        raise HTTPException(status_code=400, detail="Kendinizi kurumdan çıkaramazsınız.")
    m = db.exec(
        select(InstitutionMembership).where(
            InstitutionMembership.institution_id == institution_id,
            InstitutionMembership.user_id == target_user_id,
        )
    ).first()
    if not m:
        raise HTTPException(status_code=404, detail="Üyelik bulunamadı.")
    m.is_active = False
    db.add(m)
    db.commit()
    return {"ok": True}


@router.get("/{institution_id}/usage")
def get_usage(
    institution_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    membership = _get_membership(db, user.id, institution_id)
    if not membership:
        raise HTTPException(status_code=403, detail="Bu kuruma erişiminiz yok.")
    inst = db.get(Institution, institution_id)
    if not inst:
        raise HTTPException(status_code=404)
    total_analyses = db.exec(
        select(func.count(AnalysisRecord.id)).where(AnalysisRecord.institution_id == institution_id)
    ).one()
    member_count = db.exec(
        select(func.count(InstitutionMembership.id)).where(
            InstitutionMembership.institution_id == institution_id,
            InstitutionMembership.is_active == True,
        )
    ).one()
    return {
        "institution_id": institution_id,
        "name": inst.name,
        "monthly_quota": inst.monthly_quota,
        "quota_used": inst.quota_used_this_month,
        "quota_remaining": max(0, inst.monthly_quota - inst.quota_used_this_month),
        "total_analyses": total_analyses,
        "member_count": member_count,
    }


# --- Join page (HTML) ---

page_router = APIRouter(tags=["institution-pages"])


@page_router.get("/institution/join/{token}", response_class=HTMLResponse)
def institution_join_page(
    request: Request,
    token: str,
    db: Session = Depends(get_db),
):
    invite = db.exec(
        select(InstitutionInvite).where(InstitutionInvite.token == token)
    ).first()
    if not invite:
        return templates.TemplateResponse("enterprise/join_invalid.html", {
            "request": request,
            "error": "Bu davet bağlantısı geçersiz veya süresi dolmuş.",
        })
    if invite.accepted_at:
        return templates.TemplateResponse("enterprise/join_invalid.html", {
            "request": request,
            "error": "Bu davet daha önce kabul edilmiş.",
        })
    if invite.expires_at and invite.expires_at < datetime.utcnow():
        return templates.TemplateResponse("enterprise/join_invalid.html", {
            "request": request,
            "error": "Bu davetin süresi dolmuş. Lütfen kurum yöneticinizden yeni bir davet isteyin.",
        })
    inst = db.get(Institution, invite.institution_id)
    return templates.TemplateResponse("enterprise/join.html", {
        "request": request,
        "invite": invite,
        "institution": inst,
    })


@page_router.post("/institution/join/{token}")
def institution_join_accept(
    request: Request,
    token: str,
    db: Session = Depends(get_db),
):
    from fastapi.responses import RedirectResponse
    invite = db.exec(
        select(InstitutionInvite).where(InstitutionInvite.token == token)
    ).first()
    if not invite or invite.accepted_at:
        return templates.TemplateResponse("enterprise/join_invalid.html", {
            "request": request,
            "error": "Bu davet bağlantısı geçersiz veya daha önce kullanılmış.",
        })
    if invite.expires_at and invite.expires_at < datetime.utcnow():
        return templates.TemplateResponse("enterprise/join_invalid.html", {
            "request": request,
            "error": "Bu davetin süresi dolmuş.",
        })

    user = db.exec(select(User).where(User.email == invite.email)).first()
    if not user:
        return templates.TemplateResponse("enterprise/join.html", {
            "request": request,
            "invite": invite,
            "institution": db.get(Institution, invite.institution_id),
            "needs_registration": True,
            "message": "Bu e-posta ile kayıtlı bir hesap bulunamadı. Önce hesap oluşturun, ardından tekrar bu bağlantıyı kullanın.",
        })

    existing = db.exec(
        select(InstitutionMembership).where(
            InstitutionMembership.institution_id == invite.institution_id,
            InstitutionMembership.user_id == user.id,
        )
    ).first()
    if existing:
        existing.is_active = True
        existing.role = invite.role
        existing.accepted_at = datetime.utcnow()
        db.add(existing)
    else:
        membership = InstitutionMembership(
            institution_id=invite.institution_id,
            user_id=user.id,
            role=invite.role,
            invited_by=invite.invited_by,
            invited_at=invite.created_at,
            accepted_at=datetime.utcnow(),
            is_active=True,
        )
        db.add(membership)

    invite.accepted_at = datetime.utcnow()
    db.add(invite)

    db.add(AuditLog(
        event="institution_join",
        user_id=user.id,
        institution_id=invite.institution_id,
    ))
    db.commit()

    return templates.TemplateResponse("enterprise/join_success.html", {
        "request": request,
        "institution": db.get(Institution, invite.institution_id),
    })
