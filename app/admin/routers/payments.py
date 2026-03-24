"""Satış & ödeme paneli: başarılı/hatalı/bekleyen, PayTR, detay, admin notu, e-arşiv fatura, iade, arama, CSV, toplu fatura, audit."""
import csv
import io
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from fastapi import APIRouter, Depends, Form, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from app.core.templating import Jinja2Templates
from sqlalchemy import or_
from sqlmodel import Session, select, func

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import AuditLog, PaymentOrder, User
from app.services.invoice_earsiv import create_earsiv_invoice
from app.services.paytr_refund import paytr_refund

router = APIRouter()
_APP_DIR = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=str(_APP_DIR / "templates"))
log = logging.getLogger(__name__)


def _audit(db: Session, event: str, *, order_id: int | None = None, detail: str | None = None):
    """Ödeme admin aksiyonlarını audit log'a yaz."""
    try:
        meta = {}
        if order_id:
            meta["order_id"] = order_id
        if detail:
            meta["detail"] = detail
        db.add(AuditLog(
            event=event,
            entity_type="payment",
            entity_id=order_id,
            metadata_json=json.dumps(meta, ensure_ascii=False) if meta else None,
        ))
    except Exception as exc:
        log.warning("payment audit log failed: %s", exc)


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


def _build_payment_query(
    db: Session,
    *,
    status_filter: str | None = None,
    want_invoice_pending: bool = False,
    q: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    list_limit: int = 500,
):
    """Ortak sorgu mantığı: payments_list ve CSV export ikisi de kullanır."""
    stmt = select(PaymentOrder)

    if want_invoice_pending:
        stmt = stmt.where(PaymentOrder.status == "completed").where(
            or_(PaymentOrder.invoice_ettn.is_(None), PaymentOrder.invoice_ettn == "")
        )
    elif status_filter and status_filter in ("completed", "failed", "pending"):
        stmt = stmt.where(PaymentOrder.status == status_filter)

    if q and q.strip():
        term = q.strip()
        try:
            uid = int(term)
            stmt = stmt.where(
                or_(
                    PaymentOrder.user_id == uid,
                    PaymentOrder.merchant_oid.contains(term),
                    PaymentOrder.customer_email.contains(term),
                )
            )
        except ValueError:
            stmt = stmt.where(
                or_(
                    PaymentOrder.merchant_oid.contains(term),
                    PaymentOrder.customer_email.contains(term),
                )
            )

    if date_from and date_from.strip():
        try:
            dt = datetime.fromisoformat(date_from.strip())
            stmt = stmt.where(PaymentOrder.created_at >= dt)
        except ValueError:
            pass
    if date_to and date_to.strip():
        try:
            dt = datetime.fromisoformat(date_to.strip())
            dt = dt.replace(hour=23, minute=59, second=59)
            stmt = stmt.where(PaymentOrder.created_at <= dt)
        except ValueError:
            pass

    stmt = stmt.order_by(PaymentOrder.id.desc()).limit(list_limit)
    return list(db.exec(stmt).all())


def _orders_to_rows(orders: list, users_map: dict) -> list[dict]:
    rows = []
    for o in orders:
        try:
            amount_cents = getattr(o, "amount_kurus", None) or 0
            rows.append({
                "id": getattr(o, "id", None),
                "merchant_oid": getattr(o, "merchant_oid", "") or "",
                "user_id": getattr(o, "user_id", None),
                "user_email": users_map.get(getattr(o, "user_id", None), "")
                or (getattr(o, "customer_email", None) or "").strip()
                or "",
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
            log.exception("payments row build failed for order id=%s: %s", getattr(o, "id", "?"), e)
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
    return rows


def _build_users_map(db: Session, orders: list) -> dict:
    user_ids = list(dict.fromkeys(o.user_id for o in orders if getattr(o, "user_id", None) is not None))
    users_map: dict = {}
    if user_ids:
        try:
            for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
                users_map[getattr(u, "id", None)] = getattr(u, "email", None) or ""
        except Exception as e:
            log.warning("payments: User lookup failed: %s", e)
    return users_map


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def payments_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    status_filter: str | None = None,
    invoice_pending: str | None = Query(None),
    q: str | None = Query(None, description="Arama: e-posta, merchant_oid veya user_id"),
    date_from: str | None = Query(None, description="Başlangıç tarihi YYYY-MM-DD"),
    date_to: str | None = Query(None, description="Bitiş tarihi YYYY-MM-DD"),
):
    list_limit = 500
    want_invoice_pending = (invoice_pending or "").strip().lower() in ("1", "true", "yes", "on")

    orders = _build_payment_query(
        db,
        status_filter=status_filter,
        want_invoice_pending=want_invoice_pending,
        q=q,
        date_from=date_from,
        date_to=date_to,
        list_limit=list_limit,
    )
    users_map = _build_users_map(db, orders)
    rows = _orders_to_rows(orders, users_map)

    total_eur = sum(r["amount_eur"] for r in rows if r["status"] == "completed")

    base = str(request.base_url or "").rstrip("/")
    if "localhost" in base or "127.0.0.1" in base:
        paytr_callback_url = "https://noryaai.com/paytr/callback"
    else:
        paytr_callback_url = f"{base}/paytr/callback"
    return templates.TemplateResponse(
        "admin/payments_list.html",
        {
            "request": request,
            "payments": rows,
            "status_filter": status_filter or "",
            "invoice_pending": want_invoice_pending,
            "payments_list_limit": list_limit,
            "paytr_callback_url": paytr_callback_url,
            "q": q or "",
            "date_from": date_from or "",
            "date_to": date_to or "",
            "total_eur": total_eur,
        },
    )


# ── CSV Export ────────────────────────────────────────────────────────────────
@router.get("/export-csv")
def payments_export_csv(
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    status_filter: str | None = None,
    invoice_pending: str | None = Query(None),
    q: str | None = Query(None),
    date_from: str | None = Query(None),
    date_to: str | None = Query(None),
):
    """Filtrelenen ödemeleri CSV olarak indir."""
    want_invoice_pending = (invoice_pending or "").strip().lower() in ("1", "true", "yes", "on")
    orders = _build_payment_query(
        db,
        status_filter=status_filter,
        want_invoice_pending=want_invoice_pending,
        q=q,
        date_from=date_from,
        date_to=date_to,
        list_limit=10_000,
    )
    users_map = _build_users_map(db, orders)
    rows = _orders_to_rows(orders, users_map)

    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow([
        "ID", "merchant_oid", "Kullanıcı E-posta", "Kullanıcı ID",
        "Ürün", "Tutar (EUR)", "Para Birimi", "Durum",
        "PayTR TX", "İşlendi", "İşlenme Tarihi", "Oluşturma Tarihi",
        "Fatura ETTN", "İade Tutarı (EUR)", "Admin Notu",
    ])
    for r in rows:
        writer.writerow([
            r["id"], r["merchant_oid"], r["user_email"], r["user_id"],
            r["product"], f'{r["amount_eur"]:.2f}', r["currency"], r["status"],
            r["paytr_transaction_id"], "Evet" if r["is_processed"] else "Hayır",
            r["processed_at"], r["created_at"],
            r["invoice_ettn"], f'{r["refund_amount_kurus"] / 100:.2f}' if r["refund_amount_kurus"] else "0.00",
            r["admin_note"],
        ])

    buf.seek(0)
    now_str = datetime.utcnow().strftime("%Y%m%d_%H%M")
    filename = f"norya_payments_{now_str}.csv"
    return StreamingResponse(
        iter([buf.getvalue()]),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


# ── Toplu e-arşiv fatura kesme ────────────────────────────────────────────────
@router.post("/batch-invoice")
async def payment_batch_invoice(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """Seçili siparişler için toplu e-arşiv fatura kes (sadece completed ve faturasız)."""
    form = await request.form()
    order_ids = form.getlist("order_ids")
    customer_tckn = (form.get("batch_tckn") or "").strip()
    customer_ad = (form.get("batch_ad") or "").strip()
    customer_soyad = (form.get("batch_soyad") or "").strip()
    customer_unvan = (form.get("batch_unvan") or "").strip()
    customer_vergi_dairesi = (form.get("batch_vergi_dairesi") or "").strip()
    fatura_notu = (form.get("batch_fatura_notu") or "").strip()

    if not customer_tckn or len(customer_tckn) < 10:
        return RedirectResponse(
            url="/admin/payments?invoice_pending=1&batch_err=" + quote("TC Kimlik No gerekli (10-11 hane)."),
            status_code=302,
        )

    success_count = 0
    fail_count = 0
    errors: list[str] = []

    for oid_str in order_ids:
        try:
            oid = int(oid_str)
        except (ValueError, TypeError):
            continue
        order = db.get(PaymentOrder, oid)
        if not order or order.status != "completed" or getattr(order, "invoice_ettn", None):
            continue
        result = create_earsiv_invoice(
            amount_eur_cents=order.amount_kurus or 0,
            product=order.product,
            customer_tckn=customer_tckn,
            customer_ad=customer_ad,
            customer_soyad=customer_soyad,
            customer_unvan=customer_unvan,
            customer_vergi_dairesi=customer_vergi_dairesi,
            fatura_notu=fatura_notu,
        )
        if result.success:
            order.invoice_ettn = result.ettn
            order.invoice_gib_no = result.gib_no
            db.add(order)
            _audit(db, "payment_batch_invoice", order_id=oid, detail=f"ettn={result.ettn}")
            success_count += 1
        else:
            fail_count += 1
            errors.append(f"#{oid}: {(result.message or 'Hata')[:80]}")

    db.commit()
    msg = f"{success_count} fatura kesildi"
    if fail_count:
        msg += f", {fail_count} başarısız"
    if errors:
        msg += " — " + "; ".join(errors[:5])
    return RedirectResponse(
        url="/admin/payments?invoice_pending=1&batch_ok=" + quote(msg),
        status_code=302,
    )


@router.get("/{order_id}", response_class=HTMLResponse)
def payment_detail(
    request: Request,
    order_id: int,
    invoice_ok: str | None = Query(None),
    invoice_err: str | None = Query(None),
    refund_ok: str | None = Query(None),
    refund_err: str | None = Query(None),
    status_ok: str | None = Query(None),
    status_err: str | None = Query(None),
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

    audit_logs = list(db.exec(
        select(AuditLog)
        .where(AuditLog.entity_type == "payment", AuditLog.entity_id == order_id)
        .order_by(AuditLog.created_at.desc())
        .limit(50)
    ).all())

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
            "status_ok": status_ok,
            "status_err": status_err,
            "refunded_at": getattr(order, "refunded_at", None),
            "refund_amount_kurus": refunded_kurus,
            "refundable_kurus": max(0, amount_kurus - refunded_kurus),
            "audit_logs": audit_logs,
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
    old_note = order.admin_note
    order.admin_note = (admin_note or "").strip() or None
    db.add(order)
    _audit(db, "payment_note_updated", order_id=order_id, detail=f"old={old_note!r} new={order.admin_note!r}")
    db.commit()
    return RedirectResponse(url=f"/admin/payments/{order_id}", status_code=302)


# ── Manuel durum güncelleme ───────────────────────────────────────────────────
@router.post("/{order_id}/status")
def payment_update_status(
    order_id: int,
    new_status: str = Form(...),
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """Admin panelden ödeme durumunu manuel değiştir (callback gelmezse vb.)."""
    from fastapi import HTTPException
    order = db.get(PaymentOrder, order_id)
    if not order:
        raise HTTPException(404, "Ödeme bulunamadı.")
    allowed = ("pending", "completed", "failed")
    if new_status not in allowed:
        return RedirectResponse(
            url=f"/admin/payments/{order_id}?status_err=" + quote("Geçersiz durum."),
            status_code=302,
        )
    old_status = order.status
    if old_status == new_status:
        return RedirectResponse(url=f"/admin/payments/{order_id}", status_code=302)
    order.status = new_status
    if new_status == "completed" and not order.is_processed:
        order.is_processed = True
        order.processed_at = datetime.now(timezone.utc)
    db.add(order)
    _audit(db, "payment_status_changed", order_id=order_id, detail=f"{old_status} -> {new_status}")
    db.commit()
    return RedirectResponse(
        url=f"/admin/payments/{order_id}?status_ok=" + quote(f"Durum {old_status} → {new_status} olarak güncellendi."),
        status_code=302,
    )


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
    _audit(db, "payment_invoice_created", order_id=order_id, detail=f"ettn={result.ettn}")
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
    _audit(db, "payment_refund", order_id=order_id, detail=f"{return_amount_cents/100:.2f} {currency}")
    db.commit()
    return RedirectResponse(
        url=f"/admin/payments/{order_id}?refund_ok=1",
        status_code=302,
    )
