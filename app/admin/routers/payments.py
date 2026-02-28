"""Satış & ödeme paneli: başarılı/hatalı/bekleyen, PayTR, detay, admin notu, e-arşiv fatura."""
from urllib.parse import quote

from fastapi import APIRouter, Depends, Form, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import PaymentOrder, User
from app.services.invoice_earsiv import create_earsiv_invoice

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
            "is_processed": getattr(o, "is_processed", False),
            "processed_at": (o.processed_at.strftime("%d.%m.%Y %H:%M") if getattr(o, "processed_at", None) else "-"),
            "created_at": (o.created_at.strftime("%d.%m.%Y %H:%M") if o.created_at else "-"),
            "admin_note": getattr(o, "admin_note", None) or "",
            "invoice_ettn": getattr(o, "invoice_ettn", None) or "",
        }
        for o in orders
    ]
    return templates.TemplateResponse(
        "admin/payments_list.html",
        {"request": request, "payments": rows, "status_filter": status_filter or ""},
    )


@router.get("/{order_id}", response_class=HTMLResponse)
def payment_detail(
    request: Request,
    order_id: int,
    invoice_ok: str | None = Query(None),
    invoice_err: str | None = Query(None),
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    order = db.get(PaymentOrder, order_id)
    if not order:
        from fastapi import HTTPException
        raise HTTPException(404, "Ödeme bulunamadı.")
    user = db.get(User, order.user_id)
    user_email = user.email if user else ""
    return templates.TemplateResponse(
        "admin/payment_detail.html",
        {
            "request": request,
            "order": order,
            "user_email": user_email,
            "amount_eur": (order.amount_kurus or 0) / 100,
            "admin_note": getattr(order, "admin_note", None) or "",
            "invoice_ettn": getattr(order, "invoice_ettn", None) or "",
            "invoice_gib_no": getattr(order, "invoice_gib_no", None) or "",
            "invoice_ok": invoice_ok,
            "invoice_err": invoice_err,
        },
    )


@router.post("/{order_id}/note")
def payment_save_note(
    order_id: int,
    admin_note: str | None = Form(None),
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    order = db.get(PaymentOrder, order_id)
    if not order:
        from fastapi import HTTPException
        raise HTTPException(404, "Ödeme bulunamadı.")
    order.admin_note = (admin_note or "").strip() or None
    db.add(order)
    db.commit()
    return RedirectResponse(url=f"/admin/payments/{order_id}", status_code=302)


@router.post("/{order_id}/invoice")
def payment_create_invoice(
    request: Request,
    order_id: int,
    customer_tckn: str = Form(..., min_length=10, max_length=11),
    customer_ad: str = Form(""),
    customer_soyad: str = Form(""),
    customer_unvan: str = Form(""),
    customer_vergi_dairesi: str = Form(""),
    fatura_notu: str = Form(""),
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """E-arşiv fatura keser; sipariş tamamlanmış ve daha önce kesilmemiş olmalı."""
    from fastapi import HTTPException

    order = db.get(PaymentOrder, order_id)
    if not order:
        raise HTTPException(404, "Ödeme bulunamadı.")
    if order.status != "completed":
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?invoice_err=" + quote("Sipariş tamamlanmış olmalı"),
            status_code=302,
        )
    if getattr(order, "invoice_ettn", None):
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?invoice_err=" + quote("Bu sipariş için zaten fatura kesildi"),
            status_code=302,
        )
    result = create_earsiv_invoice(
        amount_eur_cents=order.amount_kurus or 0,
        product=order.product,
        customer_tckn=customer_tckn.strip(),
        customer_ad=customer_ad.strip(),
        customer_soyad=customer_soyad.strip(),
        customer_unvan=customer_unvan.strip(),
        customer_vergi_dairesi=customer_vergi_dairesi.strip(),
        fatura_notu=fatura_notu.strip(),
    )
    if not result.success:
        err = (result.message or "Bilinmeyen hata")[:200]
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?invoice_err=" + quote(err),
            status_code=302,
        )
    order.invoice_ettn = result.ettn
    order.invoice_gib_no = result.gib_no
    db.add(order)
    db.commit()
    return RedirectResponse(
        url=f"/admin/payments/{order_id}?invoice_ok=1",
        status_code=302,
    )
