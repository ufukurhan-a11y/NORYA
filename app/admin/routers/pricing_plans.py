"""Merkezi fiyat planları: admin'den baz fiyat (EUR cent) güncelleme. Tüm landing/ödeme buradan beslenir."""
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from app.core.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import PricingPlan

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def pricing_plans_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """Fiyat planları listesi (single, monthly, yearly). Tek sayfada düzenleme."""
    rows = list(db.exec(select(PricingPlan).order_by(PricingPlan.display_order)).all())
    items = [
        {
            "id": r.id,
            "code": r.code,
            "product": r.product,
            "price_cents": r.price_cents,
            "price_eur": round(r.price_cents / 100.0, 2),
            "display_order": r.display_order,
        }
        for r in rows
    ]
    resp = templates.TemplateResponse(
        "admin/pricing_plans_list.html",
        {"request": request, "plans": items},
    )
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return resp


@router.post("/{plan_id:int}")
def pricing_plan_update(
    request: Request,
    plan_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    price_cents: int = Form(...),
):
    """Tek planın fiyatını (EUR cent) günceller."""
    plan = db.get(PricingPlan, plan_id)
    if not plan:
        return RedirectResponse(url="/admin/pricing-plans", status_code=302)
    if price_cents < 0:
        return RedirectResponse(url="/admin/pricing-plans", status_code=302)
    plan.price_cents = price_cents
    db.add(plan)
    db.commit()
    return RedirectResponse(url="/admin/pricing-plans", status_code=302)
