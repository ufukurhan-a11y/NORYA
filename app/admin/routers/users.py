"""Kullanıcı yönetimi: listeleme, arama, detay, ban/unban."""
from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select, func

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import AnalysisRecord, AuditLog, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def users_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    q: str | None = None,
    limit: int = 100,
):
    stmt = select(User).order_by(User.id.desc()).limit(limit)
    if q and q.strip():
        q = q.strip()
        stmt = stmt.where(User.email.contains(q))
    users = list(db.exec(stmt).all())
    # Analiz sayısı ve son giriş (AuditLog login)
    user_ids = [u.id for u in users]
    analysis_count = {}
    if user_ids:
        for row in db.exec(
            select(AnalysisRecord.user_id, func.count(AnalysisRecord.id)).where(AnalysisRecord.user_id.in_(user_ids)).group_by(AnalysisRecord.user_id)
        ).all():
            analysis_count[row[0]] = row[1]
    last_login = {}
    if user_ids:
        subq = select(AuditLog.user_id, func.max(AuditLog.created_at)).where(AuditLog.event == "login").where(AuditLog.user_id.in_(user_ids)).group_by(AuditLog.user_id)
        for row in db.exec(subq).all():
            last_login[row[0]] = row[1].strftime("%d.%m.%Y %H:%M") if row[1] else "-"
    rows = [
        {
            "id": u.id,
            "email": u.email,
            "full_name": getattr(u, "full_name", "") or "",
            "plan": getattr(u, "plan", "free") or "free",
            "extra_credits": getattr(u, "extra_credits", 0) or 0,
            "is_banned": getattr(u, "is_banned", False),
            "email_verified": bool(getattr(u, "email_verified_at", None)),
            "created_at": (u.created_at.strftime("%d.%m.%Y %H:%M") if getattr(u, "created_at", None) else "-"),
            "analysis_count": analysis_count.get(u.id, 0),
            "last_login": last_login.get(u.id, "-"),
        }
        for u in users
    ]
    return templates.TemplateResponse(
        "admin/users_list.html",
        {"request": request, "users": rows, "q": q or ""},
    )


@router.post("/bulk-ban")
async def users_bulk_ban(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    from fastapi.responses import RedirectResponse
    try:
        form = await request.form()
    except Exception:
        return RedirectResponse(url="/admin/users", status_code=302)
    ids = form.getlist("user_id")
    for uid_str in ids:
        try:
            uid = int(uid_str)
            user = db.get(User, uid)
            if user:
                user.is_banned = True
                db.add(user)
        except ValueError:
            continue
    db.commit()
    return RedirectResponse(url="/admin/users", status_code=302)


@router.post("/bulk-unban")
async def users_bulk_unban(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    from fastapi.responses import RedirectResponse
    try:
        form = await request.form()
    except Exception:
        return RedirectResponse(url="/admin/users", status_code=302)
    ids = form.getlist("user_id")
    for uid_str in ids:
        try:
            uid = int(uid_str)
            user = db.get(User, uid)
            if user:
                user.is_banned = False
                db.add(user)
        except ValueError:
            continue
    db.commit()
    return RedirectResponse(url="/admin/users", status_code=302)


@router.get("/{user_id}", response_class=HTMLResponse)
def user_detail(
    request: Request,
    user_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)
    if not user:
        from fastapi import HTTPException
        raise HTTPException(404, "Kullanıcı bulunamadı.")
    analysis_count = db.exec(select(func.count(AnalysisRecord.id)).where(AnalysisRecord.user_id == user_id)).one() or 0
    last_login_log = db.exec(
        select(AuditLog).where(AuditLog.user_id == user_id).where(AuditLog.event == "login").order_by(AuditLog.created_at.desc()).limit(1)
    ).first()
    last_login = (last_login_log.created_at.strftime("%d.%m.%Y %H:%M") if last_login_log and last_login_log.created_at else "-")
    analyses = list(
        db.exec(
            select(AnalysisRecord)
            .where(AnalysisRecord.user_id == user_id)
            .order_by(AnalysisRecord.created_at.desc())
            .limit(50)
        ).all()
    )
    audit_logs = list(
        db.exec(
            select(AuditLog)
            .where(AuditLog.user_id == user_id)
            .order_by(AuditLog.created_at.desc())
            .limit(100)
        ).all()
    )
    return templates.TemplateResponse(
        "admin/user_detail.html",
        {
            "request": request,
            "user": user,
            "analysis_count": analysis_count,
            "last_login": last_login,
            "analyses": analyses,
            "audit_logs": audit_logs,
        },
    )


@router.post("/{user_id}/grant")
async def user_grant(
    request: Request,
    user_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    from fastapi.responses import RedirectResponse
    from fastapi import HTTPException
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "Kullanıcı bulunamadı.")
    try:
        form = await request.form()
        extra = form.get("extra_credits")
        plan = form.get("plan")
        if extra is not None:
            try:
                user.extra_credits = int(extra)
            except ValueError:
                pass
        if plan in ("free", "pro"):
            user.plan = plan
        db.add(user)
        db.commit()
    except Exception:
        pass
    return RedirectResponse(url=f"/admin/users/{user_id}", status_code=302)


@router.post("/{user_id}/ban")
def user_ban(user_id: int, _=Depends(require_admin_cookie), db: Session = Depends(get_db)):
    from fastapi.responses import RedirectResponse
    from fastapi import HTTPException
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "Kullanıcı bulunamadı.")
    user.is_banned = True
    db.add(user)
    db.commit()
    return RedirectResponse(url=f"/admin/users/{user_id}", status_code=302)


@router.post("/{user_id}/unban")
def user_unban(user_id: int, _=Depends(require_admin_cookie), db: Session = Depends(get_db)):
    from fastapi.responses import RedirectResponse
    from fastapi import HTTPException
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "Kullanıcı bulunamadı.")
    user.is_banned = False
    db.add(user)
    db.commit()
    return RedirectResponse(url=f"/admin/users/{user_id}", status_code=302)
