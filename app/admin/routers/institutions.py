"""Kurum yönetimi: listeleme, oluşturma, düzenleme, üye yönetimi, davet."""
from datetime import datetime, timedelta
import secrets

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select, func

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.core.templating import Jinja2Templates
from app.models import (
    AnalysisRecord,
    AuditLog,
    User,
)
from app.models.institution import Institution, InstitutionInvite, InstitutionMembership
from app.models.enterprise_subscription import EnterpriseSubscription

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

INSTITUTION_TYPES = [
    ("hospital", "Hastane"),
    ("clinic", "Klinik"),
    ("lab", "Laboratuvar"),
    ("network", "Sağlayıcı Ağı"),
]

INSTITUTION_STATUSES = [
    ("pilot", "Pilot"),
    ("active", "Aktif"),
    ("suspended", "Askıda"),
]

INSTITUTION_PLANS = [
    ("enterprise", "Enterprise"),
    ("pro", "Pro Hastane"),
    ("custom", "Özel"),
]

MEMBER_ROLES = [
    ("admin", "Yönetici"),
    ("reviewer", "Gözlemci"),
    ("member", "Üye"),
]


def _sync_enterprise_subscription(db: Session, inst: Institution) -> None:
    """Kurum oluşturulduğunda veya düzenlendiğinde EnterpriseSubscription kaydını senkronize et."""
    sub = db.exec(
        select(EnterpriseSubscription)
        .where(EnterpriseSubscription.institution_id == inst.id)
        .order_by(EnterpriseSubscription.created_at.desc())
    ).first()

    billing_status = "active" if inst.is_active and inst.status != "suspended" else "cancelled"
    if inst.status == "pilot":
        billing_status = "trial"

    if sub:
        sub.plan_name = inst.plan
        sub.billing_status = billing_status
        sub.quota_limit = inst.monthly_quota
        sub.seat_limit = inst.seat_limit
        sub.start_date = inst.contract_start
        sub.end_date = inst.contract_end
        db.add(sub)
    else:
        sub = EnterpriseSubscription(
            institution_id=inst.id,
            plan_name=inst.plan,
            billing_status=billing_status,
            start_date=inst.contract_start,
            end_date=inst.contract_end,
            quota_limit=inst.monthly_quota,
            seat_limit=inst.seat_limit,
        )
        db.add(sub)


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def institutions_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    q: str | None = None,
):
    stmt = select(Institution).order_by(Institution.id.desc())
    if q and q.strip():
        stmt = stmt.where(Institution.name.contains(q.strip()))
    institutions = list(db.exec(stmt).all())

    inst_ids = [i.id for i in institutions]
    member_counts: dict[int, int] = {}
    usage_counts: dict[int, int] = {}
    if inst_ids:
        for row in db.exec(
            select(InstitutionMembership.institution_id, func.count(InstitutionMembership.id))
            .where(InstitutionMembership.institution_id.in_(inst_ids), InstitutionMembership.is_active == True)
            .group_by(InstitutionMembership.institution_id)
        ).all():
            member_counts[row[0]] = row[1]
        for row in db.exec(
            select(AnalysisRecord.institution_id, func.count(AnalysisRecord.id))
            .where(AnalysisRecord.institution_id.in_(inst_ids))
            .group_by(AnalysisRecord.institution_id)
        ).all():
            usage_counts[row[0]] = row[1]

    type_labels = dict(INSTITUTION_TYPES)
    status_labels = dict(INSTITUTION_STATUSES)
    plan_labels = dict(INSTITUTION_PLANS)
    rows = [
        {
            "id": i.id,
            "name": i.name,
            "type": i.type,
            "type_label": type_labels.get(i.type, i.type),
            "status": i.status,
            "status_label": status_labels.get(i.status, i.status),
            "plan": i.plan,
            "plan_label": plan_labels.get(i.plan, i.plan),
            "seat_limit": i.seat_limit,
            "monthly_quota": i.monthly_quota,
            "quota_used": i.quota_used_this_month,
            "is_active": i.is_active,
            "members": member_counts.get(i.id, 0),
            "total_analyses": usage_counts.get(i.id, 0),
            "contract_end": i.contract_end.strftime("%d.%m.%Y") if i.contract_end else "—",
            "created_at": i.created_at.strftime("%d.%m.%Y") if i.created_at else "—",
        }
        for i in institutions
    ]
    return templates.TemplateResponse("admin/institutions_list.html", {
        "request": request,
        "institutions": rows,
        "q": q or "",
        "total": len(rows),
    })


@router.get("/create", response_class=HTMLResponse)
def institution_create_form(request: Request, _=Depends(require_admin_cookie)):
    return templates.TemplateResponse("admin/institution_form.html", {
        "request": request,
        "institution": None,
        "types": INSTITUTION_TYPES,
        "statuses": INSTITUTION_STATUSES,
        "plans": INSTITUTION_PLANS,
        "mode": "create",
    })


@router.post("/create")
def institution_create(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    name: str = Form(...),
    type: str = Form("hospital"),
    status: str = Form("pilot"),
    plan: str = Form("enterprise"),
    seat_limit: int = Form(25),
    monthly_quota: int = Form(100),
    quota_reset_day: int = Form(1),
    contact_email: str = Form(""),
    contact_phone: str = Form(""),
    notes: str = Form(""),
    contract_start: str = Form(""),
    contract_end: str = Form(""),
):
    inst = Institution(
        name=name.strip(),
        type=type,
        status=status if status in ("pilot", "active", "suspended") else "pilot",
        plan=plan if plan in ("enterprise", "pro", "custom") else "enterprise",
        seat_limit=max(seat_limit, 1),
        monthly_quota=monthly_quota,
        quota_reset_day=min(max(quota_reset_day, 1), 28),
        contact_email=contact_email.strip() or None,
        contact_phone=contact_phone.strip() or None,
        notes=notes.strip() or None,
    )
    if contract_start:
        try:
            inst.contract_start = datetime.strptime(contract_start, "%Y-%m-%d")
        except ValueError:
            pass
    if contract_end:
        try:
            inst.contract_end = datetime.strptime(contract_end, "%Y-%m-%d")
        except ValueError:
            pass
    db.add(inst)
    db.flush()
    _sync_enterprise_subscription(db, inst)
    db.commit()
    db.refresh(inst)
    return RedirectResponse(url=f"/admin/institutions/{inst.id}", status_code=303)


@router.get("/{inst_id}", response_class=HTMLResponse)
def institution_detail(
    request: Request,
    inst_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    inst = db.get(Institution, inst_id)
    if not inst:
        return HTMLResponse("Kurum bulunamadı", status_code=404)

    memberships = list(db.exec(
        select(InstitutionMembership).where(InstitutionMembership.institution_id == inst_id).order_by(InstitutionMembership.id.desc())
    ).all())
    user_ids = [m.user_id for m in memberships]
    users_map: dict[int, User] = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u

    members = [
        {
            "id": m.id,
            "user_id": m.user_id,
            "email": users_map[m.user_id].email if m.user_id in users_map else "—",
            "full_name": (users_map[m.user_id].full_name if m.user_id in users_map else "") or "—",
            "role": m.role,
            "is_active": m.is_active,
            "accepted_at": m.accepted_at.strftime("%d.%m.%Y") if m.accepted_at else "Bekliyor",
        }
        for m in memberships
    ]

    pending_invites = list(db.exec(
        select(InstitutionInvite)
        .where(InstitutionInvite.institution_id == inst_id, InstitutionInvite.accepted_at == None)
        .order_by(InstitutionInvite.created_at.desc())
    ).all())

    recent_analyses = list(db.exec(
        select(AnalysisRecord)
        .where(AnalysisRecord.institution_id == inst_id)
        .order_by(AnalysisRecord.created_at.desc())
        .limit(20)
    ).all())
    analysis_user_ids = list({a.user_id for a in recent_analyses})
    analysis_users: dict[int, User] = {}
    if analysis_user_ids:
        for u in db.exec(select(User).where(User.id.in_(analysis_user_ids))).all():
            analysis_users[u.id] = u

    recent = [
        {
            "id": a.id,
            "user_email": analysis_users[a.user_id].email if a.user_id in analysis_users else "—",
            "source": a.source,
            "created_at": a.created_at.strftime("%d.%m.%Y %H:%M") if a.created_at else "—",
        }
        for a in recent_analyses
    ]

    type_labels = dict(INSTITUTION_TYPES)

    status_labels = dict(INSTITUTION_STATUSES)
    plan_labels = dict(INSTITUTION_PLANS)

    return templates.TemplateResponse("admin/institution_detail.html", {
        "request": request,
        "inst": inst,
        "type_label": type_labels.get(inst.type, inst.type),
        "status_label": status_labels.get(inst.status, inst.status),
        "plan_label": plan_labels.get(inst.plan, inst.plan),
        "members": members,
        "pending_invites": pending_invites,
        "recent_analyses": recent,
        "roles": MEMBER_ROLES,
        "types": INSTITUTION_TYPES,
        "statuses": INSTITUTION_STATUSES,
        "plans": INSTITUTION_PLANS,
    })


@router.post("/{inst_id}/edit")
def institution_edit(
    request: Request,
    inst_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    name: str = Form(...),
    type: str = Form("hospital"),
    status: str = Form("pilot"),
    plan: str = Form("enterprise"),
    seat_limit: int = Form(25),
    monthly_quota: int = Form(100),
    quota_reset_day: int = Form(1),
    is_active: bool = Form(False),
    contact_email: str = Form(""),
    contact_phone: str = Form(""),
    notes: str = Form(""),
    contract_start: str = Form(""),
    contract_end: str = Form(""),
):
    inst = db.get(Institution, inst_id)
    if not inst:
        return HTMLResponse("Kurum bulunamadı", status_code=404)
    inst.name = name.strip()
    inst.type = type
    inst.status = status if status in ("pilot", "active", "suspended") else inst.status
    inst.plan = plan if plan in ("enterprise", "pro", "custom") else inst.plan
    inst.seat_limit = max(seat_limit, 1)
    inst.monthly_quota = monthly_quota
    inst.quota_reset_day = min(max(quota_reset_day, 1), 28)
    inst.is_active = is_active
    inst.contact_email = contact_email.strip() or None
    inst.contact_phone = contact_phone.strip() or None
    inst.notes = notes.strip() or None
    if contract_start:
        try:
            inst.contract_start = datetime.strptime(contract_start, "%Y-%m-%d")
        except ValueError:
            pass
    if contract_end:
        try:
            inst.contract_end = datetime.strptime(contract_end, "%Y-%m-%d")
        except ValueError:
            pass
    inst.updated_at = datetime.utcnow()
    db.add(inst)
    _sync_enterprise_subscription(db, inst)
    db.commit()
    return RedirectResponse(url=f"/admin/institutions/{inst_id}", status_code=303)


@router.post("/{inst_id}/invite")
def institution_invite_member(
    request: Request,
    inst_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    email: str = Form(...),
    role: str = Form("member"),
):
    inst = db.get(Institution, inst_id)
    if not inst:
        return HTMLResponse("Kurum bulunamadı", status_code=404)
    token = secrets.token_urlsafe(48)
    invite = InstitutionInvite(
        institution_id=inst_id,
        email=email.strip().lower(),
        role=role if role in ("admin", "reviewer", "member") else "member",
        token=token,
        expires_at=datetime.utcnow() + timedelta(days=30),
    )
    db.add(invite)
    db.commit()
    return RedirectResponse(url=f"/admin/institutions/{inst_id}", status_code=303)


@router.post("/{inst_id}/add-member")
def institution_add_member(
    request: Request,
    inst_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    user_email: str = Form(...),
    role: str = Form("member"),
):
    inst = db.get(Institution, inst_id)
    if not inst:
        return HTMLResponse("Kurum bulunamadı", status_code=404)
    user = db.exec(select(User).where(User.email == user_email.strip().lower())).first()
    if not user:
        return RedirectResponse(url=f"/admin/institutions/{inst_id}?error=user_not_found", status_code=303)
    existing = db.exec(
        select(InstitutionMembership).where(
            InstitutionMembership.institution_id == inst_id,
            InstitutionMembership.user_id == user.id,
        )
    ).first()
    if existing:
        existing.is_active = True
        existing.role = role
        db.add(existing)
    else:
        membership = InstitutionMembership(
            institution_id=inst_id,
            user_id=user.id,
            role=role if role in ("admin", "reviewer", "member") else "member",
            accepted_at=datetime.utcnow(),
            is_active=True,
        )
        db.add(membership)
    db.commit()
    return RedirectResponse(url=f"/admin/institutions/{inst_id}", status_code=303)


@router.post("/{inst_id}/members/{membership_id}/toggle")
def institution_toggle_member(
    inst_id: int,
    membership_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    m = db.get(InstitutionMembership, membership_id)
    if m and m.institution_id == inst_id:
        m.is_active = not m.is_active
        db.add(m)
        db.commit()
    return RedirectResponse(url=f"/admin/institutions/{inst_id}", status_code=303)


@router.post("/{inst_id}/quota-reset")
def institution_quota_reset(
    inst_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    inst = db.get(Institution, inst_id)
    if inst:
        inst.quota_used_this_month = 0
        db.add(inst)
        db.commit()
    return RedirectResponse(url=f"/admin/institutions/{inst_id}", status_code=303)
