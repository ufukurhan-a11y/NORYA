"""Satış & ödeme paneli: başarılı/hatalı/bekleyen, PayTR."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import PaymentOrder, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def payments_list(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db), status_filter: str | None = None):
    stmt = select(PaymentOrder).order_by(PaymentOrder.id.desc()).limit(200)
    if status_filter and status_filter in ("completed", "failed", "pending"):
        stmt = stmt.where(PaymentOrder.status == status_filter)
    orders = list(db.exec(stmt).all())
    user_ids = {o.user_id for o in orders}
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email or ""
    rows = [
        {
            "id": o.id,
            "merchant_oid": o.merchant_oid,
            "user_id": o.user_id,
            "user_email": users_map.get(o.user_id, ""),
            "product": o.product,
            "amount_cents": o.amount_kurus,
            "amount_eur": (o.amount_kurus or 0) / 100,
            "currency": getattr(o, "currency", None) or "EUR",
            "status": o.status,
            "paytr_transaction_id": getattr(o, "paytr_transaction_id", None) or "-",
            "created_at": (o.created_at.strftime("%d.%m.%Y %H:%M") if o.created_at else "-"),
        }
        for o in orders
    ]
    return templates.TemplateResponse(
        "admin/payments_list.html",
        {"request": request, "payments": rows, "status_filter": status_filter or ""},
    )
