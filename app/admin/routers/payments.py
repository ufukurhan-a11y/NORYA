"""Satış & ödeme paneli: başarılı/hatalı/bekleyen, PayTR, detay, admin notu, e-arşiv fatura, iade."""
import logging
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from fastapi import APIRouter, Depends, Form, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import PaymentOrder, User
from app.services.invoice_earsiv import create_earsiv_invoice
from app.services.paytr_refund import paytr_refund

router = APIRouter()
# Mutlak yol: çalışma dizini nereden başlatılırsa başlatılsın şablonlar bulunur
_APP_DIR = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=str(_APP_DIR / "templates"))
log = logging.getLogger(__name__)


def _fmt_dt(val):
    """Format datetime/date or string for display; avoid AttributeError if DB returns str."""
    try:
        if val is None:
            return "-"
        if isinstance(val, datetime):
            return val.strftime("%d.%m.%Y %H:%M")
        if hasattr(val, "strftime"):
            return val.strftime("%d.%m.%Y %H:%M")
        if isinstance(val, str):
            return val[:16] if len(val) > 16 else val
    except Exception:
        pass
    return "-"


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def payments_list(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db), status_filter: str | None = None):
    stmt = select(PaymentOrder).order_by(PaymentOrder.id.desc()).limit(200)
    if status_filter and status_filter in ("completed", "failed", "pending"):
        stmt = stmt.where(PaymentOrder.status == status_filter)
    orders = list(db.exec(stmt).all())
    user_ids = [o.user_id for o in orders if getattr(o, "user_id", None) is not None]
    user_ids = list(dict.fromkeys(user_ids))  # unique, order preserved
    users_map = {}
    if user_ids:
        try:
            for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
                users_map[getattr(u, "id", None)] = getattr(u, "email", None) or ""
        except Exception as e:
            log.warning("payments_list: User lookup failed: %s", e)
    rows = []
    for o in orders:
        try:
            amount_cents = getattr(o, "amount_kurus", None) or 0
            rows.append({
                "id": getattr(o, "id", None),
                "merchant_oid": getattr(o, "merchant_oid", "") or "",
                "user_id": getattr(o, "user_id", None),
                "user_email": users_map.get(getattr(o, "user_id", None), ""),
                "product": getattr(o, "product", "") or "",
                "amount_cents": amount_cents,
                "amount_eur": amount_cents / 100.0,
                "currency": getattr(o, "currency", None) or "EUR",
                "status": getattr(o, "status", "") or "pending",
                "paytr_transaction_id": getattr(o, "paytr_transaction_id", None) or "-",
                "is_processed": getattr(o, "is_processed", False),
                "processed_at": _fmt_dt(getattr(o, "processed_at", None)),
                "created_at": _fmt_dt(getattr(o, "created_at", None)),
                "admin_note": getattr(o, "admin_note", None) or "",
                "invoice_ettn": getattr(o, "invoice_ettn", None) or "",
                "refunded_at": getattr(o, "refunded_at", None),
                "refund_amount_kurus": getattr(o, "refund_amount_kurus", None) or 0,
            })
        except Exception as e:
            log.exception("payments_list: row build failed for order id=%s: %s", getattr(o, "id", "?"), e)
            rows.append({
                "id": getattr(o, "id", None),
                "merchant_oid": getattr(o, "merchant_oid", "") or "?",
                "user_id": getattr(o, "user_id", None),
                "user_email": "",
                "product": "?",
                "amount_cents": 0,
                "amount_eur": 0.0,
                "currency": "EUR",
                "status": "?",
                "paytr_transaction_id": "-",
                "is_processed": False,
                "processed_at": "-",
                "created_at": "-",
                "admin_note": "",
                "invoice_ettn": "",
                "refunded_at": None,
                "refund_amount_kurus": 0,
            })
    # PayTR panelde girilmesi gereken bildirim URL (canonical domain)
    # request.base_url bir URL objesi döndürür; stringe çevirip son slash'ı kırp.
    base = str(request.base_url or "").rstrip("/")
    if "localhost" in base or "127.0.0.1" in base:
        paytr_callback_url = "https://noryaai.com/paytr/callback"
    else:
        paytr_callback_url = f"{base}/paytr/callback"
    return templates.TemplateResponse(
        "admin/payments_list.html",
        {"request": request, "payments": rows, "status_filter": status_filter or "", "paytr_callback_url": paytr_callback_url},
    )


@router.get("/{order_id}", response_class=HTMLResponse)
def payment_detail(
    request: Request,
    order_id: int,
    invoice_ok: str | None = Query(None),
    invoice_err: str | None = Query(None),
    refund_ok: str | None = Query(None),
    refund_err: str | None = Query(None),
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    order = db.get(PaymentOrder, order_id)
    if not order:
        from fastapi import HTTPException
        raise HTTPException(404, "Ödeme bulunamadı.")
    user = db.get(User, order.user_id)
    user_email = user.email if user else ""
    amount_kurus = order.amount_kurus or 0
    refunded_kurus = getattr(order, "refund_amount_kurus", None) or 0
    return templates.TemplateResponse(
        "admin/payment_detail.html",
        {
            "request": request,
            "order": order,
            "user_email": user_email,
            "amount_eur": amount_kurus / 100,
            "admin_note": getattr(order, "admin_note", None) or "",
            "invoice_ettn": getattr(order, "invoice_ettn", None) or "",
            "invoice_gib_no": getattr(order, "invoice_gib_no", None) or "",
            "invoice_ok": invoice_ok,
            "invoice_err": invoice_err,
            "refund_ok": refund_ok,
            "refund_err": refund_err,
            "refunded_at": getattr(order, "refunded_at", None),
            "refund_amount_kurus": refunded_kurus,
            "refundable_kurus": max(0, amount_kurus - refunded_kurus),
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


@router.post("/{order_id}/refund")
def payment_refund(
    order_id: int,
    full_refund: str | None = Form(None),
    amount_eur: str | None = Form(None),
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """PayTR İade API ile tam veya kısmi iade. Sipariş completed olmalı."""
    from fastapi import HTTPException
    from datetime import datetime, timezone

    order = db.get(PaymentOrder, order_id)
    if not order:
        raise HTTPException(404, "Ödeme bulunamadı.")
    if order.status != "completed":
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?refund_err=" + quote("Sadece tamamlanmış siparişler iade edilebilir."),
            status_code=302,
        )
    amount_kurus = order.amount_kurus or 0
    refunded_kurus = getattr(order, "refund_amount_kurus", None) or 0
    refundable = max(0, amount_kurus - refunded_kurus)
    if refundable <= 0:
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?refund_err=" + quote("Bu sipariş için iade limiti doldu."),
            status_code=302,
        )

    if full_refund and str(full_refund).strip().lower() in ("1", "true", "on", "yes"):
        return_amount_cents = refundable
    elif amount_eur and str(amount_eur).strip():
        try:
            eur_val = float(str(amount_eur).strip().replace(",", "."))
            if eur_val <= 0:
                raise ValueError("Tutar pozitif olmalı")
            return_amount_cents = int(round(eur_val * 100))
        except ValueError as e:
            return RedirectResponse(
                url=f"/admin/payments/{order_id}?refund_err=" + quote(f"Geçersiz tutar: {e}"),
                status_code=302,
            )
        if return_amount_cents > refundable:
            return RedirectResponse(
                url=f"/admin/payments/{order_id}?refund_err=" + quote(f"Kalan iade edilebilir tutar {refundable/100:.2f} EUR."),
                status_code=302,
            )
    else:
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?refund_err=" + quote("Tam iade veya kısmi iade tutarı girin."),
            status_code=302,
        )

    currency = getattr(order, "currency", None) or "EUR"
    result = paytr_refund(
        merchant_oid=order.merchant_oid,
        return_amount_eur_cents=return_amount_cents,
        currency=currency,
    )
    if not result.success:
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?refund_err=" + quote((result.message or "İade başarısız.")[:150]),
            status_code=302,
        )
    order.refund_amount_kurus = refunded_kurus + return_amount_cents
    if not getattr(order, "refunded_at", None):
        order.refunded_at = datetime.now(timezone.utc)
    db.add(order)
    db.commit()
    return RedirectResponse(
        url=f"/admin/payments/{order_id}?refund_ok=1",
        status_code=302,
    )
