"""Enterprise customer dashboard routes — full post-sale application layer."""
import hashlib
import hmac
import json
import logging
import os
import secrets
import shutil
import time
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, File, Form, Query, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from sqlmodel import Session, select, func

from app.core.database import get_db
from app.core.templating import Jinja2Templates
from app.enterprise.deps import require_enterprise_user
from app.models import AnalysisRecord, AuditLog, User
from app.models.enterprise_case import EnterpriseCase, EnterpriseReport
from app.models.enterprise_subscription import EnterpriseSubscription
from app.models.institution import Institution, InstitutionInvite, InstitutionMembership
from app.services.analyze import analyze_blood_test, analyze_blood_test_from_image
from app.services.pdf_extract import extract_text_from_pdf
from app.enterprise.i18n import get_t, is_rtl, detect_lang
from app.enterprise.email import send_invite_email
from app.enterprise.pdf_export import generate_report_pdf

log = logging.getLogger("norya.enterprise")
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

MAX_UPLOAD_SIZE = int(os.getenv("ENTERPRISE_MAX_UPLOAD_MB", "10")) * 1024 * 1024
_CSRF_SECRET = os.getenv("CSRF_SECRET", secrets.token_hex(32))


def _csrf_token(session_id: str) -> str:
    return hmac.new(_CSRF_SECRET.encode(), session_id.encode(), hashlib.sha256).hexdigest()[:32]


def _csrf_check(request: Request, form_token: str | None) -> bool:
    sid = request.cookies.get("access_token", "") or request.cookies.get("session", "")
    if not sid or not form_token:
        return False
    return hmac.compare_digest(_csrf_token(sid), form_token)


def _role_labels(t: dict) -> dict:
    return {"owner": t["role_owner"], "admin": t["role_admin"], "reviewer": t["role_reviewer"],
            "staff": t["role_staff"], "member": t["role_member"], "readonly": t["role_readonly"]}


def _status_labels(t: dict) -> dict:
    return {"new": t["status_new"], "processing": t["status_processing"], "needs_review": t["status_needs_review"],
            "approved": t["status_approved"], "rejected": t["status_rejected"], "archived": t["status_archived"]}


def _inst_status_labels(t: dict) -> dict:
    return {"pilot": t["inst_pilot"], "active": t["inst_active"], "suspended": t["inst_suspended"]}


def _type_labels(t: dict) -> dict:
    return {"hospital": t["type_hospital"], "clinic": t["type_clinic"],
            "lab": t["type_lab"], "network": t["type_network"]}


def _event_labels(t: dict) -> dict:
    return {
        "institution_join": t["ev_institution_join"], "analyze": t["ev_analyze"],
        "login": t["ev_login"], "register": t["ev_register"],
        "case_create": t["ev_case_create"], "case_approve": t["ev_case_approve"],
        "case_reject": t["ev_case_reject"], "case_status_change": t["ev_case_status_change"],
        "invite_send": t["ev_invite_send"], "role_change": t["ev_role_change"],
        "member_toggle": t["ev_member_toggle"], "onboarding_complete": t["ev_onboarding_complete"],
    }


def _billing_labels(t: dict) -> dict:
    return {"active": t["billing_active"], "past_due": t["billing_past_due"],
            "cancelled": t["billing_cancelled"], "trial": t["billing_trial"]}


def _base_ctx(request, user, membership, inst, active_page: str) -> dict:
    """Common template context with i18n and metadata."""
    lang = detect_lang(request, inst)
    t = get_t(lang)
    sid = request.cookies.get("access_token", "") or request.cookies.get("session", "")
    return {
        "request": request,
        "user": user,
        "membership": membership,
        "inst": inst,
        "t": t,
        "lang": lang,
        "is_rtl": is_rtl(lang),
        "is_admin": membership.role in ("admin", "owner"),
        "active_page": active_page,
        "inst_status_label": _inst_status_labels(t).get(inst.status, inst.status),
        "role_label": _role_labels(t).get(membership.role, membership.role),
        "csrf_token": _csrf_token(sid),
    }


# Keep backward-compat constants for any external code
ROLE_LABELS = {"owner": "Sahip", "admin": "Yönetici", "reviewer": "Gözlemci",
               "staff": "Personel", "member": "Üye", "readonly": "Salt Okunur"}
STATUS_LABELS = {"new": "Yeni", "processing": "İşleniyor", "needs_review": "İnceleme Bekliyor",
                 "approved": "Onaylandı", "rejected": "Reddedildi", "archived": "Arşivlendi"}
INST_STATUS_LABELS = {"pilot": "Pilot", "active": "Aktif", "suspended": "Askıda"}

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "enterprise_uploads")


def _ctx(ctx):
    """Unpack context dict or return the response object (redirect, error page, etc.)."""
    if isinstance(ctx, dict):
        return ctx["user"], ctx["membership"], ctx["institution"], None
    return None, None, None, ctx


def _enterprise_audit(db: Session, event: str, user_id: int, institution_id: int,
                       entity_type: str | None = None, entity_id: int | None = None,
                       meta: dict | None = None, ip: str | None = None):
    db.add(AuditLog(
        event=event,
        user_id=user_id,
        institution_id=institution_id,
        entity_type=entity_type,
        entity_id=entity_id,
        metadata_json=json.dumps(meta, ensure_ascii=False) if meta else None,
        ip=ip,
    ))


# ──────────────────────────────────────────────
# DASHBOARD — Overview
# ──────────────────────────────────────────────

@router.get("/dashboard", response_class=HTMLResponse)
def enterprise_dashboard(request: Request, ctx=Depends(require_enterprise_user), db: Session = Depends(get_db)):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir

    if not inst.onboarding_completed:
        return RedirectResponse(url="/enterprise/onboarding", status_code=303)

    member_count = db.exec(
        select(func.count(InstitutionMembership.id)).where(
            InstitutionMembership.institution_id == inst.id,
            InstitutionMembership.is_active == True,
        )
    ).one()

    total_analyses = db.exec(
        select(func.count(AnalysisRecord.id)).where(AnalysisRecord.institution_id == inst.id)
    ).one()

    pending_review = db.exec(
        select(func.count(EnterpriseCase.id)).where(
            EnterpriseCase.institution_id == inst.id,
            EnterpriseCase.status == "needs_review",
        )
    ).one()

    total_cases = db.exec(
        select(func.count(EnterpriseCase.id)).where(EnterpriseCase.institution_id == inst.id)
    ).one()

    recent_analyses = list(db.exec(
        select(AnalysisRecord).where(AnalysisRecord.institution_id == inst.id)
        .order_by(AnalysisRecord.created_at.desc()).limit(10)
    ).all())
    ra_users = {}
    if recent_analyses:
        for u in db.exec(select(User).where(User.id.in_(list({a.user_id for a in recent_analyses})))).all():
            ra_users[u.id] = u

    recent = [
        {
            "id": a.id,
            "user_email": ra_users[a.user_id].email if a.user_id in ra_users else "—",
            "source": a.source,
            "created_at": a.created_at.strftime("%d.%m.%Y %H:%M") if a.created_at else "—",
        }
        for a in recent_analyses
    ]

    recent_activity = list(db.exec(
        select(AuditLog).where(AuditLog.institution_id == inst.id)
        .order_by(AuditLog.created_at.desc()).limit(8)
    ).all())
    act_users = {}
    if recent_activity:
        uids = list({a.user_id for a in recent_activity if a.user_id})
        if uids:
            for u in db.exec(select(User).where(User.id.in_(uids))).all():
                act_users[u.id] = u

    activity = [
        {
            "event": a.event,
            "user_email": act_users[a.user_id].email if a.user_id and a.user_id in act_users else "—",
            "created_at": a.created_at.strftime("%d.%m.%Y %H:%M") if a.created_at else "—",
            "entity_type": a.entity_type or "",
        }
        for a in recent_activity
    ]

    pct = (inst.quota_used_this_month / inst.monthly_quota * 100) if inst.monthly_quota > 0 else 0

    sub = db.exec(
        select(EnterpriseSubscription).where(EnterpriseSubscription.institution_id == inst.id)
        .order_by(EnterpriseSubscription.created_at.desc())
    ).first()

    ctx = _base_ctx(request, user, membership, inst, "dashboard")
    t = ctx["t"]
    ctx.update({
        "member_count": member_count,
        "total_analyses": total_analyses,
        "total_cases": total_cases,
        "pending_review": pending_review,
        "recent_analyses": recent,
        "recent_activity": activity,
        "quota_pct": min(pct, 100),
        "subscription": sub,
        "role_labels": _role_labels(t),
        "billing_labels": _billing_labels(t),
        "event_labels": _event_labels(t),
    })
    return templates.TemplateResponse("enterprise/dashboard.html", ctx)


# ──────────────────────────────────────────────
# ONBOARDING — Post-sale wizard
# ──────────────────────────────────────────────

@router.get("/onboarding", response_class=HTMLResponse)
def enterprise_onboarding(request: Request, ctx=Depends(require_enterprise_user), db: Session = Depends(get_db)):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if inst.onboarding_completed:
        return RedirectResponse(url="/enterprise/dashboard", status_code=303)
    ctx = _base_ctx(request, user, membership, inst, "onboarding")
    ctx["type_labels"] = _type_labels(ctx["t"])
    ctx["role_labels"] = _role_labels(ctx["t"])
    return templates.TemplateResponse("enterprise/onboarding.html", ctx)


@router.post("/onboarding", response_class=HTMLResponse)
def enterprise_onboarding_save(
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    institution_name: str = Form(""),
    institution_type: str = Form("hospital"),
    active_languages: str = Form("tr,en"),
    status_choice: str = Form("pilot"),
    csrf_token: str = Form(""),
    invite_emails: str = Form(""),
    invite_role: str = Form("member"),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner"):
        return HTMLResponse("Yetkiniz yok.", status_code=403)

    if institution_name.strip():
        inst.name = institution_name.strip()
    inst.type = institution_type if institution_type in ("hospital", "clinic", "lab", "network") else inst.type
    inst.active_languages = active_languages.strip() or "tr,en"
    inst.status = status_choice if status_choice in ("pilot", "active") else "pilot"
    inst.onboarding_completed = True
    inst.updated_at = datetime.utcnow()
    db.add(inst)

    if invite_emails.strip():
        for email_raw in invite_emails.split(","):
            email = email_raw.strip().lower()
            if not email or "@" not in email:
                continue
            token = secrets.token_urlsafe(48)
            db.add(InstitutionInvite(
                institution_id=inst.id,
                email=email,
                role=invite_role if invite_role in ("admin", "reviewer", "staff", "member", "readonly") else "member",
                token=token,
                invited_by=user.id,
                expires_at=datetime.utcnow() + timedelta(days=30),
            ))

    _enterprise_audit(db, "onboarding_complete", user.id, inst.id, "institution", inst.id)
    db.commit()
    return RedirectResponse(url="/enterprise/dashboard", status_code=303)


# ──────────────────────────────────────────────
# TEAM — Members & invitations
# ──────────────────────────────────────────────

@router.get("/team", response_class=HTMLResponse)
def enterprise_team(request: Request, ctx=Depends(require_enterprise_user), db: Session = Depends(get_db)):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir

    memberships = list(db.exec(
        select(InstitutionMembership).where(InstitutionMembership.institution_id == inst.id)
        .order_by(InstitutionMembership.id.desc())
    ).all())
    user_ids = [m.user_id for m in memberships]
    users_map = {}
    analysis_counts = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u
        for row in db.exec(
            select(AnalysisRecord.user_id, func.count(AnalysisRecord.id))
            .where(AnalysisRecord.institution_id == inst.id, AnalysisRecord.user_id.in_(user_ids))
            .group_by(AnalysisRecord.user_id)
        ).all():
            analysis_counts[row[0]] = row[1]

    members = [
        {
            "id": m.id,
            "user_id": m.user_id,
            "email": users_map[m.user_id].email if m.user_id in users_map else "—",
            "full_name": (users_map[m.user_id].full_name if m.user_id in users_map else "") or "—",
            "role": m.role,
            "role_label": ROLE_LABELS.get(m.role, m.role),
            "is_active": m.is_active,
            "analyses": analysis_counts.get(m.user_id, 0),
            "accepted_at": m.accepted_at.strftime("%d.%m.%Y") if m.accepted_at else "Bekliyor",
        }
        for m in memberships
    ]

    pending_invites = list(db.exec(
        select(InstitutionInvite).where(
            InstitutionInvite.institution_id == inst.id,
            InstitutionInvite.accepted_at == None,
        ).order_by(InstitutionInvite.created_at.desc())
    ).all())

    ctx = _base_ctx(request, user, membership, inst, "team")
    ctx.update({
        "members": members,
        "pending_invites": pending_invites,
        "role_labels": _role_labels(ctx["t"]),
        "seat_limit": inst.seat_limit,
        "seat_used": len([m for m in members if m["is_active"]]),
    })
    return templates.TemplateResponse("enterprise/team.html", ctx)


@router.post("/team/invite")
def enterprise_team_invite(
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    email: str = Form(...),
    role: str = Form("member"),
    csrf_token: str = Form(""),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner"):
        return HTMLResponse("Yetkiniz yok.", status_code=403)

    active_count = db.exec(
        select(func.count(InstitutionMembership.id)).where(
            InstitutionMembership.institution_id == inst.id,
            InstitutionMembership.is_active == True,
        )
    ).one()
    if active_count >= inst.seat_limit:
        return RedirectResponse(url="/enterprise/team?error=seat_limit", status_code=303)

    email_clean = email.strip().lower()
    valid_roles = ("admin", "reviewer", "staff", "member", "readonly")
    assigned_role = role if role in valid_roles else "member"
    token = secrets.token_urlsafe(48)
    db.add(InstitutionInvite(
        institution_id=inst.id,
        email=email_clean,
        role=assigned_role,
        token=token,
        invited_by=user.id,
        expires_at=datetime.utcnow() + timedelta(days=30),
    ))
    _enterprise_audit(db, "invite_send", user.id, inst.id, "invite", None, {"email": email_clean, "role": assigned_role})
    db.commit()

    lang = detect_lang(request, inst)
    t = get_t(lang)
    role_label = _role_labels(t).get(assigned_role, assigned_role)
    inviter_name = user.full_name or user.email.split("@")[0]
    send_invite_email(
        to_email=email_clean,
        institution_name=inst.name,
        inviter_name=inviter_name,
        role=role_label,
        token=token,
        lang=lang,
    )
    return RedirectResponse(url="/enterprise/team", status_code=303)


@router.post("/team/members/{membership_id}/role")
def enterprise_team_role(
    membership_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    new_role: str = Form(...),
    csrf_token: str = Form(""),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner"):
        return HTMLResponse("Yetkiniz yok.", status_code=403)
    m = db.get(InstitutionMembership, membership_id)
    if not m or m.institution_id != inst.id:
        return HTMLResponse("Üyelik bulunamadı.", status_code=404)
    valid_roles = ("admin", "reviewer", "staff", "member", "readonly")
    if new_role in valid_roles:
        old_role = m.role
        m.role = new_role
        db.add(m)
        _enterprise_audit(db, "role_change", user.id, inst.id, "membership", m.id,
                          {"old_role": old_role, "new_role": new_role, "target_user_id": m.user_id})
        db.commit()
    return RedirectResponse(url="/enterprise/team", status_code=303)


@router.post("/team/members/{membership_id}/toggle")
def enterprise_team_toggle(
    membership_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    csrf_token: str = Form(""),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner"):
        return HTMLResponse("Yetkiniz yok.", status_code=403)
    m = db.get(InstitutionMembership, membership_id)
    if not m or m.institution_id != inst.id:
        return HTMLResponse("Üyelik bulunamadı.", status_code=404)
    if m.user_id == user.id:
        return RedirectResponse(url="/enterprise/team?error=self", status_code=303)
    m.is_active = not m.is_active
    db.add(m)
    _enterprise_audit(db, "member_toggle", user.id, inst.id, "membership", m.id,
                      {"target_user_id": m.user_id, "new_status": m.is_active})
    db.commit()
    return RedirectResponse(url="/enterprise/team", status_code=303)


# ──────────────────────────────────────────────
# UPLOADS — Enterprise case upload center
# ──────────────────────────────────────────────

@router.get("/uploads", response_class=HTMLResponse)
def enterprise_uploads(
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    page: int = 1,
    status_filter: str = "",
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir

    per_page = 30
    offset = (max(page, 1) - 1) * per_page

    q = select(EnterpriseCase).where(EnterpriseCase.institution_id == inst.id)
    q_count = select(func.count(EnterpriseCase.id)).where(EnterpriseCase.institution_id == inst.id)
    if status_filter and status_filter in STATUS_LABELS:
        q = q.where(EnterpriseCase.status == status_filter)
        q_count = q_count.where(EnterpriseCase.status == status_filter)

    total = db.exec(q_count).one()
    cases = list(db.exec(q.order_by(EnterpriseCase.created_at.desc()).offset(offset).limit(per_page)).all())

    case_user_ids = list({c.uploaded_by_user_id for c in cases})
    reviewer_ids = list({c.reviewed_by_user_id for c in cases if c.reviewed_by_user_id})
    all_uids = list(set(case_user_ids + reviewer_ids))
    u_map = {}
    if all_uids:
        for u in db.exec(select(User).where(User.id.in_(all_uids))).all():
            u_map[u.id] = u

    rows = [
        {
            "id": c.id,
            "filename": c.source_filename or "—",
            "source_type": c.source_type,
            "status": c.status,
            "status_label": STATUS_LABELS.get(c.status, c.status),
            "uploader_email": u_map[c.uploaded_by_user_id].email if c.uploaded_by_user_id in u_map else "—",
            "reviewer_email": u_map[c.reviewed_by_user_id].email if c.reviewed_by_user_id and c.reviewed_by_user_id in u_map else "",
            "created_at": c.created_at.strftime("%d.%m.%Y %H:%M") if c.created_at else "—",
            "reviewed_at": c.reviewed_at.strftime("%d.%m.%Y %H:%M") if c.reviewed_at else "",
        }
        for c in cases
    ]

    status_counts = {}
    for s_key in STATUS_LABELS:
        cnt = db.exec(
            select(func.count(EnterpriseCase.id)).where(
                EnterpriseCase.institution_id == inst.id, EnterpriseCase.status == s_key
            )
        ).one()
        if cnt > 0:
            status_counts[s_key] = cnt

    ctx = _base_ctx(request, user, membership, inst, "uploads")
    ctx.update({
        "cases": rows,
        "total": total,
        "page": page,
        "per_page": per_page,
        "has_next": offset + per_page < total,
        "has_prev": page > 1,
        "status_filter": status_filter,
        "status_labels": _status_labels(ctx["t"]),
        "status_counts": status_counts,
        "can_upload": membership.role in ("admin", "owner", "staff", "member"),
    })
    return templates.TemplateResponse("enterprise/uploads.html", ctx)


ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".webp"}
MIME_MAP = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


@router.post("/uploads")
async def enterprise_upload_file(
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    file: UploadFile = File(...),
    lang: str = Form("tr"),
    csrf_token: str = Form(""),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner", "staff", "member"):
        t = get_t(detect_lang(request, inst))
        return HTMLResponse(t.get("err_upload_no_perm", "No permission."), status_code=403)

    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return RedirectResponse(url="/enterprise/uploads?error=format", status_code=303)

    if inst.quota_used_this_month >= inst.monthly_quota:
        return RedirectResponse(url="/enterprise/uploads?error=quota", status_code=303)

    content = await file.read()
    if not content:
        return RedirectResponse(url="/enterprise/uploads?error=empty", status_code=303)

    if len(content) > MAX_UPLOAD_SIZE:
        return RedirectResponse(url="/enterprise/uploads?error=size", status_code=303)

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    safe_name = f"{inst.id}_{user.id}_{int(datetime.utcnow().timestamp())}_{secrets.token_hex(4)}"
    stored_name = safe_name + ext
    stored_path = os.path.join(UPLOAD_DIR, stored_name)
    with open(stored_path, "wb") as f:
        f.write(content)

    source_type = "pdf" if ext == ".pdf" else ("image" if ext in IMAGE_EXTENSIONS else "text")

    case = EnterpriseCase(
        institution_id=inst.id,
        uploaded_by_user_id=user.id,
        source_filename=file.filename,
        source_type=source_type,
        stored_path=stored_name,
        status="processing",
    )
    db.add(case)
    db.flush()
    _enterprise_audit(db, "case_create", user.id, inst.id, "case", case.id,
                      {"filename": file.filename, "source_type": source_type})
    db.commit()
    db.refresh(case)

    analysis_text = None
    analysis_error = None
    try:
        if source_type == "image":
            mime = MIME_MAP.get(ext, "image/jpeg")
            result_text, _usage = analyze_blood_test_from_image(content, mime, lang=lang)
            input_preview = f"[Görsel: {file.filename}]"
            analysis_text = result_text
        else:
            extracted = extract_text_from_pdf(content)
            if "çıkarılamadı" in extracted:
                analysis_error = "PDF'den metin okunamadı."
            else:
                labs_norm = {"t": " ".join(extracted.split()).strip(), "dn": None}
                report_payload, _usage = analyze_blood_test(extracted, lang=lang, plan="enterprise", labs_norm=labs_norm)
                result_text = report_payload["sonuc"]
                input_preview = extracted[:2000]
                analysis_text = result_text
    except Exception as exc:
        log.exception("Enterprise upload analysis failed for case %s: %s", case.id, exc)
        analysis_error = str(exc)[:500]

    if analysis_text and not analysis_error:
        rec = AnalysisRecord(
            user_id=user.id,
            input_text=input_preview,
            result_text=analysis_text,
            source=source_type,
            plan_type="enterprise",
            institution_id=inst.id,
            original_filename=file.filename,
            original_stored_path=stored_name,
        )
        db.add(rec)
        db.flush()

        case.analysis_record_id = rec.id
        case.status = "needs_review"
        case.updated_at = datetime.utcnow()

        report = EnterpriseReport(
            case_id=case.id,
            language=lang or "tr",
            report_text=analysis_text,
            approval_status="pending",
        )
        db.add(report)

        inst.quota_used_this_month = (inst.quota_used_this_month or 0) + 1
        inst.updated_at = datetime.utcnow()
        db.add(inst)
        db.add(case)

        _enterprise_audit(db, "analyze", user.id, inst.id, "case", case.id,
                          {"analysis_record_id": rec.id, "language": lang})
        db.commit()
    else:
        case.status = "new"
        case.review_notes = analysis_error or "Analiz işlenemedi."
        case.updated_at = datetime.utcnow()
        db.add(case)
        db.commit()

    return RedirectResponse(url="/enterprise/uploads", status_code=303)


# ──────────────────────────────────────────────
# CASE DETAIL — View analysis result
# ──────────────────────────────────────────────

@router.get("/case/{case_id}", response_class=HTMLResponse)
def enterprise_case_detail(
    case_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir

    case = db.get(EnterpriseCase, case_id)
    if not case or case.institution_id != inst.id:
        return HTMLResponse("Vaka bulunamadı.", status_code=404)

    uploader = db.get(User, case.uploaded_by_user_id)
    reviewer = db.get(User, case.reviewed_by_user_id) if case.reviewed_by_user_id else None

    analysis = db.get(AnalysisRecord, case.analysis_record_id) if case.analysis_record_id else None

    reports = list(db.exec(
        select(EnterpriseReport).where(EnterpriseReport.case_id == case.id)
        .order_by(EnterpriseReport.created_at.desc())
    ).all())

    can_review = membership.role in ("admin", "owner", "reviewer")

    ctx = _base_ctx(request, user, membership, inst, "uploads")
    t = ctx["t"]
    ctx.update({
        "case": case,
        "uploader": uploader,
        "reviewer": reviewer,
        "analysis": analysis,
        "reports": reports,
        "status_label": _status_labels(t).get(case.status, case.status),
        "status_labels": _status_labels(t),
        "can_review": can_review,
    })
    active_langs = (inst.active_languages or "tr,en").replace(" ", "").split(",")
    ctx["active_languages"] = active_langs
    return templates.TemplateResponse("enterprise/case_detail.html", ctx)


@router.post("/case/{case_id}/regenerate")
def enterprise_case_regenerate(
    case_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    target_lang: str = Form("tr"),
    csrf_token: str = Form(""),
):
    """Re-generate a report for the given case in a specific language."""
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner", "staff", "reviewer"):
        t = get_t(detect_lang(request, inst))
        return HTMLResponse(t.get("err_no_permission", "No permission."), status_code=403)

    case = db.get(EnterpriseCase, case_id)
    if not case or case.institution_id != inst.id:
        return RedirectResponse(url="/enterprise/uploads", status_code=303)

    analysis = db.get(AnalysisRecord, case.analysis_record_id) if case.analysis_record_id else None
    if not analysis or not analysis.input_text:
        return RedirectResponse(url=f"/enterprise/case/{case_id}", status_code=303)

    regen_text = None
    try:
        input_src = analysis.input_text
        if case.source_type == "image" and case.stored_path:
            fpath = os.path.join(UPLOAD_DIR, case.stored_path)
            if os.path.isfile(fpath):
                with open(fpath, "rb") as fh:
                    img_data = fh.read()
                ext = os.path.splitext(case.stored_path)[1].lower()
                mime = MIME_MAP.get(ext, "image/jpeg")
                regen_text, _ = analyze_blood_test_from_image(img_data, mime, lang=target_lang)
        if not regen_text:
            labs_norm = {"t": " ".join(input_src.split()).strip(), "dn": None}
            payload, _ = analyze_blood_test(input_src, lang=target_lang, plan="enterprise", labs_norm=labs_norm)
            regen_text = payload["sonuc"]
    except Exception as exc:
        log.exception("Regenerate failed for case %s lang=%s: %s", case_id, target_lang, exc)
        return RedirectResponse(url=f"/enterprise/case/{case_id}", status_code=303)

    if regen_text:
        report = EnterpriseReport(
            case_id=case.id,
            language=target_lang,
            report_text=regen_text,
            approval_status="pending",
        )
        db.add(report)
        _enterprise_audit(db, "case_status_change", user.id, inst.id, "case", case.id,
                          {"action": "regenerate", "language": target_lang})
        db.commit()

    return RedirectResponse(url=f"/enterprise/case/{case_id}", status_code=303)


@router.get("/case/{case_id}/export-pdf")
def enterprise_case_export_pdf(
    case_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    report_id: int = Query(None),
):
    """Download a PDF export of an approved report."""
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir

    case = db.get(EnterpriseCase, case_id)
    if not case or case.institution_id != inst.id:
        return HTMLResponse("Not found", status_code=404)

    if report_id:
        report = db.get(EnterpriseReport, report_id)
        if not report or report.case_id != case.id:
            return HTMLResponse("Report not found", status_code=404)
    else:
        reports = list(db.exec(
            select(EnterpriseReport).where(
                EnterpriseReport.case_id == case.id,
                EnterpriseReport.approval_status == "approved",
            ).order_by(EnterpriseReport.created_at.desc())
        ).all())
        report = reports[0] if reports else None

    if not report or not report.report_text:
        return RedirectResponse(url=f"/enterprise/case/{case_id}", status_code=303)

    try:
        pdf_bytes = generate_report_pdf(
            report_text=report.report_text,
            case_filename=case.source_filename,
            institution_name=inst.name,
            language=report.language or "tr",
            case_id=case.id,
            report_date=report.created_at,
        )
    except Exception as exc:
        log.exception("PDF export failed for case %s: %s", case_id, exc)
        return RedirectResponse(url=f"/enterprise/case/{case_id}", status_code=303)

    safe_name = (case.source_filename or f"case_{case_id}").rsplit(".", 1)[0]
    filename = f"NoryaAI_{safe_name}_{report.language}.pdf"

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


# ──────────────────────────────────────────────
# REVIEW — Case review queue
# ──────────────────────────────────────────────

@router.get("/review", response_class=HTMLResponse)
def enterprise_review(
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    page: int = 1,
    show: str = "pending",
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner", "reviewer"):
        return HTMLResponse("İnceleme yetkiniz yok.", status_code=403)

    per_page = 20
    offset = (max(page, 1) - 1) * per_page

    if show == "all":
        q = select(EnterpriseCase).where(EnterpriseCase.institution_id == inst.id)
        q_count = select(func.count(EnterpriseCase.id)).where(EnterpriseCase.institution_id == inst.id)
    else:
        q = select(EnterpriseCase).where(
            EnterpriseCase.institution_id == inst.id,
            EnterpriseCase.status.in_(["new", "needs_review", "processing"]),
        )
        q_count = select(func.count(EnterpriseCase.id)).where(
            EnterpriseCase.institution_id == inst.id,
            EnterpriseCase.status.in_(["new", "needs_review", "processing"]),
        )

    total = db.exec(q_count).one()
    pending_count = db.exec(
        select(func.count(EnterpriseCase.id)).where(
            EnterpriseCase.institution_id == inst.id,
            EnterpriseCase.status.in_(["new", "needs_review", "processing"]),
        )
    ).one()
    cases = list(db.exec(q.order_by(EnterpriseCase.created_at.desc()).offset(offset).limit(per_page)).all())

    all_uids = list({c.uploaded_by_user_id for c in cases} | {c.reviewed_by_user_id for c in cases if c.reviewed_by_user_id})
    u_map = {}
    if all_uids:
        for u in db.exec(select(User).where(User.id.in_(all_uids))).all():
            u_map[u.id] = u

    report_case_ids = [c.id for c in cases]
    reports_map = {}
    if report_case_ids:
        for r in db.exec(select(EnterpriseReport).where(EnterpriseReport.case_id.in_(report_case_ids))).all():
            reports_map.setdefault(r.case_id, []).append(r)

    rows = [
        {
            "id": c.id,
            "filename": c.source_filename or "—",
            "source_type": c.source_type,
            "status": c.status,
            "status_label": STATUS_LABELS.get(c.status, c.status),
            "uploader_email": u_map[c.uploaded_by_user_id].email if c.uploaded_by_user_id in u_map else "—",
            "reviewer_email": u_map[c.reviewed_by_user_id].email if c.reviewed_by_user_id and c.reviewed_by_user_id in u_map else "",
            "created_at": c.created_at.strftime("%d.%m.%Y %H:%M") if c.created_at else "—",
            "reviewed_at": c.reviewed_at.strftime("%d.%m.%Y %H:%M") if c.reviewed_at else "",
            "review_notes": c.review_notes or "",
            "reports": [
                {"id": r.id, "language": r.language, "approval_status": r.approval_status}
                for r in reports_map.get(c.id, [])
            ],
        }
        for c in cases
    ]

    ctx = _base_ctx(request, user, membership, inst, "review")
    ctx.update({
        "cases": rows,
        "total": total,
        "page": page,
        "per_page": per_page,
        "has_next": offset + per_page < total,
        "has_prev": page > 1,
        "show": show,
        "pending_count": pending_count,
        "status_labels": _status_labels(ctx["t"]),
    })
    return templates.TemplateResponse("enterprise/review.html", ctx)


@router.post("/review/{case_id}/approve")
def enterprise_review_approve(
    case_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    notes: str = Form(""),
    csrf_token: str = Form(""),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner", "reviewer"):
        return HTMLResponse("Yetkiniz yok.", status_code=403)
    case = db.get(EnterpriseCase, case_id)
    if not case or case.institution_id != inst.id:
        return HTMLResponse("Vaka bulunamadı.", status_code=404)
    case.status = "approved"
    case.reviewed_by_user_id = user.id
    case.reviewed_at = datetime.utcnow()
    case.review_notes = notes.strip() or None
    case.updated_at = datetime.utcnow()
    db.add(case)
    _enterprise_audit(db, "case_approve", user.id, inst.id, "case", case.id)
    db.commit()
    return RedirectResponse(url="/enterprise/review", status_code=303)


@router.post("/review/{case_id}/reject")
def enterprise_review_reject(
    case_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    notes: str = Form(""),
    csrf_token: str = Form(""),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner", "reviewer"):
        return HTMLResponse("Yetkiniz yok.", status_code=403)
    case = db.get(EnterpriseCase, case_id)
    if not case or case.institution_id != inst.id:
        return HTMLResponse("Vaka bulunamadı.", status_code=404)
    case.status = "rejected"
    case.reviewed_by_user_id = user.id
    case.reviewed_at = datetime.utcnow()
    case.review_notes = notes.strip() or case.review_notes
    case.updated_at = datetime.utcnow()
    db.add(case)
    _enterprise_audit(db, "case_reject", user.id, inst.id, "case", case.id)
    db.commit()
    return RedirectResponse(url="/enterprise/review", status_code=303)


@router.post("/review/{case_id}/status")
def enterprise_review_set_status(
    case_id: int,
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    new_status: str = Form(...),
    csrf_token: str = Form(""),
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner", "reviewer"):
        return HTMLResponse("Yetkiniz yok.", status_code=403)
    case = db.get(EnterpriseCase, case_id)
    if not case or case.institution_id != inst.id:
        return HTMLResponse("Vaka bulunamadı.", status_code=404)
    if new_status in STATUS_LABELS:
        old = case.status
        case.status = new_status
        case.updated_at = datetime.utcnow()
        if new_status in ("approved", "rejected"):
            case.reviewed_by_user_id = user.id
            case.reviewed_at = datetime.utcnow()
        db.add(case)
        _enterprise_audit(db, "case_status_change", user.id, inst.id, "case", case.id,
                          {"old_status": old, "new_status": new_status})
        db.commit()
    return RedirectResponse(url="/enterprise/review", status_code=303)


# ──────────────────────────────────────────────
# BILLING — Plan, quota, contract
# ──────────────────────────────────────────────

@router.get("/billing", response_class=HTMLResponse)
def enterprise_billing(request: Request, ctx=Depends(require_enterprise_user), db: Session = Depends(get_db)):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir

    sub = db.exec(
        select(EnterpriseSubscription).where(EnterpriseSubscription.institution_id == inst.id)
        .order_by(EnterpriseSubscription.created_at.desc())
    ).first()

    pct = (inst.quota_used_this_month / inst.monthly_quota * 100) if inst.monthly_quota > 0 else 0

    member_count = db.exec(
        select(func.count(InstitutionMembership.id)).where(
            InstitutionMembership.institution_id == inst.id,
            InstitutionMembership.is_active == True,
        )
    ).one()

    ctx = _base_ctx(request, user, membership, inst, "billing")
    ctx.update({
        "subscription": sub,
        "quota_pct": min(pct, 100),
        "member_count": member_count,
        "billing_labels": _billing_labels(ctx["t"]),
    })
    return templates.TemplateResponse("enterprise/billing.html", ctx)


# ──────────────────────────────────────────────
# AUDIT — Activity trail
# ──────────────────────────────────────────────

@router.get("/audit", response_class=HTMLResponse)
def enterprise_audit(
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    page: int = 1,
    event_filter: str = "",
):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    if membership.role not in ("admin", "owner", "reviewer"):
        return HTMLResponse("Bu sayfaya erişim yetkiniz yok.", status_code=403)

    per_page = 50
    offset = (max(page, 1) - 1) * per_page

    q = select(AuditLog).where(AuditLog.institution_id == inst.id)
    q_count = select(func.count(AuditLog.id)).where(AuditLog.institution_id == inst.id)
    if event_filter:
        q = q.where(AuditLog.event == event_filter)
        q_count = q_count.where(AuditLog.event == event_filter)

    total = db.exec(q_count).one()
    logs = list(db.exec(q.order_by(AuditLog.created_at.desc()).offset(offset).limit(per_page)).all())

    log_user_ids = list({l.user_id for l in logs if l.user_id})
    log_users = {}
    if log_user_ids:
        for u in db.exec(select(User).where(User.id.in_(log_user_ids))).all():
            log_users[u.id] = u

    audit_ev_labels = _event_labels(get_t(detect_lang(request)))

    distinct_events = list({l.event for l in logs})

    rows = [
        {
            "id": l.id,
            "event": l.event,
            "event_label": audit_ev_labels.get(l.event, l.event),
            "user_email": log_users[l.user_id].email if l.user_id and l.user_id in log_users else "—",
            "entity_type": l.entity_type or "",
            "entity_id": l.entity_id or "",
            "created_at": l.created_at.strftime("%d.%m.%Y %H:%M") if l.created_at else "—",
            "ip": l.ip or "—",
        }
        for l in logs
    ]

    ctx = _base_ctx(request, user, membership, inst, "audit")
    ctx.update({
        "logs": rows,
        "total": total,
        "page": page,
        "per_page": per_page,
        "has_next": offset + per_page < total,
        "has_prev": page > 1,
        "event_filter": event_filter,
        "event_labels": _event_labels(ctx["t"]),
        "distinct_events": distinct_events,
    })
    return templates.TemplateResponse("enterprise/audit.html", ctx)


# ──────────────────────────────────────────────
# SUPPORT — Documentation & contact
# ──────────────────────────────────────────────

@router.get("/support", response_class=HTMLResponse)
def enterprise_support(request: Request, ctx=Depends(require_enterprise_user), db: Session = Depends(get_db)):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    ctx = _base_ctx(request, user, membership, inst, "support")
    tl = _type_labels(ctx["t"])
    ctx["type_labels"] = tl
    ctx["type_label"] = tl.get(inst.type, inst.type)
    return templates.TemplateResponse("enterprise/support.html", ctx)


# ──────────────────────────────────────────────
# SETTINGS (existing, enhanced)
# ──────────────────────────────────────────────

@router.get("/settings", response_class=HTMLResponse)
def enterprise_settings(request: Request, ctx=Depends(require_enterprise_user), db: Session = Depends(get_db)):
    user, membership, inst, redir = _ctx(ctx)
    if redir:
        return redir
    ctx = _base_ctx(request, user, membership, inst, "settings")
    tl = _type_labels(ctx["t"])
    ctx["type_label"] = tl.get(inst.type, inst.type)
    return templates.TemplateResponse("enterprise/settings.html", ctx)


# ──────────────────────────────────────────────
# ANALYTICS API (JSON)
# ──────────────────────────────────────────────

@router.get("/analytics")
def enterprise_analytics_api(
    request: Request,
    ctx=Depends(require_enterprise_user),
    db: Session = Depends(get_db),
    days: int = 30,
):
    if not isinstance(ctx, dict):
        return JSONResponse({"error": "auth"}, status_code=401)
    user, membership, inst = ctx["user"], ctx["membership"], ctx["institution"]
    if membership.role not in ("admin", "owner", "reviewer"):
        return JSONResponse({"error": "forbidden"}, status_code=403)

    days = min(max(days, 7), 90)
    since = datetime.utcnow() - timedelta(days=days)

    analyses = list(db.exec(
        select(AnalysisRecord)
        .where(AnalysisRecord.institution_id == inst.id, AnalysisRecord.created_at >= since)
        .order_by(AnalysisRecord.created_at.asc())
    ).all())

    daily: dict[str, int] = {}
    per_member: dict[int, int] = {}
    for a in analyses:
        day_key = a.created_at.strftime("%Y-%m-%d") if a.created_at else "unknown"
        daily[day_key] = daily.get(day_key, 0) + 1
        per_member[a.user_id] = per_member.get(a.user_id, 0) + 1

    member_emails = {}
    if per_member:
        for u in db.exec(select(User).where(User.id.in_(list(per_member.keys())))).all():
            member_emails[u.id] = u.email

    return JSONResponse({
        "institution_id": inst.id,
        "days": days,
        "total": len(analyses),
        "daily": daily,
        "per_member": [
            {"user_id": uid, "email": member_emails.get(uid, "—"), "count": cnt}
            for uid, cnt in sorted(per_member.items(), key=lambda x: -x[1])
        ],
    })


# ──────────────────────────────────────────────
# BACKWARD-COMPAT REDIRECTS from old /dashboard/* paths
# ──────────────────────────────────────────────

@router.get("/dashboard/members", response_class=HTMLResponse)
def _compat_members(request: Request):
    return RedirectResponse(url="/enterprise/team", status_code=301)


@router.get("/dashboard/reports", response_class=HTMLResponse)
def _compat_reports(request: Request):
    return RedirectResponse(url="/enterprise/uploads", status_code=301)


@router.get("/dashboard/audit", response_class=HTMLResponse)
def _compat_audit(request: Request):
    return RedirectResponse(url="/enterprise/audit", status_code=301)


@router.get("/dashboard/settings", response_class=HTMLResponse)
def _compat_settings(request: Request):
    return RedirectResponse(url="/enterprise/settings", status_code=301)
