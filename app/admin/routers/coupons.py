"""İndirim kodu yönetimi: admin panelinde CRUD."""
from datetime import date

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import DiscountCode

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def coupons_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    rows = list(db.exec(select(DiscountCode).order_by(DiscountCode.id.desc())).all())
    items = [
        {
            "id": r.id,
            "code": r.code,
            "discount_type": r.discount_type,
            "discount_value": r.discount_value,
            "valid_from": r.valid_from.strftime("%Y-%m-%d") if r.valid_from else "",
            "valid_until": r.valid_until.strftime("%Y-%m-%d") if r.valid_until else "",
            "valid_days_of_month": r.valid_days_of_month or "",
            "max_uses": r.max_uses,
            "use_count": r.use_count or 0,
            "products": r.products or "",
            "created_at": r.created_at.strftime("%d.%m.%Y %H:%M") if r.created_at else "-",
        }
        for r in rows
    ]
    return templates.TemplateResponse(
        "admin/coupons_list.html",
        {"request": request, "coupons": items},
    )


@router.get("/new", response_class=HTMLResponse)
def coupon_new_form(request: Request, _=Depends(require_admin_cookie)):
    return templates.TemplateResponse(
        "admin/coupon_form.html",
        {"request": request, "coupon": None, "is_edit": False},
    )


@router.post("/new")
def coupon_create(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    code: str = Form(""),
    discount_type: str = Form("percent"),
    discount_value: int = Form(0),
    valid_from: str | None = Form(None),
    valid_until: str | None = Form(None),
    valid_days_of_month: str | None = Form(None),
    max_uses: int | None = Form(None),
    products: str | None = Form(None),
):
    code_clean = (code or "").strip().upper()
    if not code_clean:
        return templates.TemplateResponse(
            "admin/coupon_form.html",
            {"request": request, "coupon": None, "is_edit": False, "error": "Kod boş olamaz."},
        )
    existing = db.exec(select(DiscountCode).where(DiscountCode.code == code_clean)).first()
    if existing:
        return templates.TemplateResponse(
            "admin/coupon_form.html",
            {"request": request, "coupon": None, "is_edit": False, "error": "Bu kod zaten var."},
        )
    valid_from_d = None
    if valid_from and valid_from.strip():
        try:
            valid_from_d = date.fromisoformat(valid_from.strip())
        except ValueError:
            pass
    valid_until_d = None
    if valid_until and valid_until.strip():
        try:
            valid_until_d = date.fromisoformat(valid_until.strip())
        except ValueError:
            pass
    coupon = DiscountCode(
        code=code_clean,
        discount_type=discount_type or "percent",
        discount_value=discount_value or 0,
        valid_from=valid_from_d,
        valid_until=valid_until_d,
        valid_days_of_month=(valid_days_of_month or "").strip() or None,
        max_uses=max_uses if max_uses is not None and max_uses > 0 else None,
        products=(products or "").strip() or None,
    )
    db.add(coupon)
    db.commit()
    return RedirectResponse(url="/admin/coupons", status_code=302)


@router.get("/{coupon_id:int}/edit", response_class=HTMLResponse)
def coupon_edit_form(
    request: Request,
    coupon_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    coupon = db.get(DiscountCode, coupon_id)
    if not coupon:
        return RedirectResponse(url="/admin/coupons", status_code=302)
    return templates.TemplateResponse(
        "admin/coupon_form.html",
        {
            "request": request,
            "coupon": coupon,
            "is_edit": True,
        },
    )


@router.post("/{coupon_id:int}/edit")
def coupon_update(
    request: Request,
    coupon_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    code: str = Form(""),
    discount_type: str = Form("percent"),
    discount_value: int = Form(0),
    valid_from: str | None = Form(None),
    valid_until: str | None = Form(None),
    valid_days_of_month: str | None = Form(None),
    max_uses: int | None = Form(None),
    products: str | None = Form(None),
):
    coupon = db.get(DiscountCode, coupon_id)
    if not coupon:
        return RedirectResponse(url="/admin/coupons", status_code=302)
    code_clean = (code or "").strip().upper()
    if not code_clean:
        return templates.TemplateResponse(
            "admin/coupon_form.html",
            {"request": request, "coupon": coupon, "is_edit": True, "error": "Kod boş olamaz."},
        )
    existing = db.exec(select(DiscountCode).where(DiscountCode.code == code_clean, DiscountCode.id != coupon_id)).first()
    if existing:
        return templates.TemplateResponse(
            "admin/coupon_form.html",
            {"request": request, "coupon": coupon, "is_edit": True, "error": "Bu kod başka bir kuponda kullanılıyor."},
        )
    valid_from_d = None
    if valid_from and valid_from.strip():
        try:
            valid_from_d = date.fromisoformat(valid_from.strip())
        except ValueError:
            pass
    valid_until_d = None
    if valid_until and valid_until.strip():
        try:
            valid_until_d = date.fromisoformat(valid_until.strip())
        except ValueError:
            pass
    coupon.code = code_clean
    coupon.discount_type = discount_type or "percent"
    coupon.discount_value = discount_value or 0
    coupon.valid_from = valid_from_d
    coupon.valid_until = valid_until_d
    coupon.valid_days_of_month = (valid_days_of_month or "").strip() or None
    coupon.max_uses = max_uses if max_uses is not None and max_uses > 0 else None
    coupon.products = (products or "").strip() or None
    db.add(coupon)
    db.commit()
    return RedirectResponse(url="/admin/coupons", status_code=302)


@router.post("/{coupon_id:int}/delete")
def coupon_delete(
    coupon_id: int,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    coupon = db.get(DiscountCode, coupon_id)
    if coupon:
        db.delete(coupon)
        db.commit()
    return RedirectResponse(url="/admin/coupons", status_code=302)
