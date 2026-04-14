"""PayTR Recurring Payment (Kayıtlı Kart Tekrarlayan Ödeme) servisi.

PayTR Direkt API üzerinden kayıtlı kart ile otomatik kredi yenileme.
Docs: https://dev.paytr.com/direkt-api/kart-saklama-api/kayitli-kart-tekrarlayan-odeme
"""

import base64
import hashlib
import hmac
import json
import logging
from datetime import datetime, timezone

import httpx
from sqlmodel import Session, select

from app.core.config import settings
from app.models.institution import Institution

log = logging.getLogger(__name__)

PAYTR_RECURRING_URL = "https://www.paytr.com/odeme"


def _build_paytr_token(merchant_id: str, merchant_key: str, merchant_salt: str, data: dict) -> str:
    """PayTR token oluşturur (HMAC-SHA256)."""
    raw = (
        f"merchant_id:{merchant_id}"
        f"user_ip:{data.get('user_ip', '')}"
        f"merchant_oid:{data.get('merchant_oid', '')}"
        f"email:{data.get('email', '')}"
        f"payment_amount:{data.get('payment_amount', '')}"
        f"user_basket:{data.get('user_basket', '')}"
        f"no_installment:{data.get('no_installment', '')}"
        f"max_installment:{data.get('max_installment', '')}"
        f"currency:{data.get('currency', '')}"
        f"test_mode:{data.get('test_mode', '')}"
        f"payment_type:{data.get('payment_type', '')}"
        f"non_3d:{data.get('non_3d', '')}"
        f"order_id:{data.get('order_id', '')}"
        f"installment_count:{data.get('installment_count', '')}"
        f"merchant_salt:{merchant_salt}"
    )
    token = hmac.new(
        merchant_key.encode("utf-8"),
        raw.encode("utf-8"),
        hashlib.sha256,
    ).digest()
    return base64.b64encode(token).decode("utf-8")


def execute_recurring_payment(
    institution: Institution,
    amount_cents: int,
    user_ip: str = "127.0.0.1",
) -> dict:
    """PayTR üzerinden kayıtlı kart ile tekrarlayan ödeme yapar.

    Returns:
        dict: {"status": "success"|"failed", "merchant_oid": str, "reason": str, "reference_no": str}
    """
    merchant_id = (getattr(settings, "paytr_merchant_id", None) or "").strip()
    merchant_key = (getattr(settings, "paytr_merchant_key", None) or "").strip()
    merchant_salt = (getattr(settings, "paytr_merchant_salt", None) or "").strip()

    if not all([merchant_id, merchant_key, merchant_salt]):
        return {
            "status": "failed",
            "merchant_oid": "",
            "reason": "PayTR merchant bilgileri eksik",
            "reference_no": "",
        }

    if not institution.paytr_utoken or not institution.paytr_ctoken:
        return {
            "status": "failed",
            "merchant_oid": "",
            "reason": "Kurum için kayıtlı kart bilgisi (utoken/ctoken) bulunamadı",
            "reference_no": "",
        }

    # Para birimi kontrolü
    currency = getattr(settings, "paytr_currency", "EUR") or "EUR"
    payment_amount_str = f"{amount_cents / 100:.2f}"

    if currency == "TRY":
        # TRY ise kuruş cinsinden gönder
        payment_amount_str = f"{amount_cents / 100:.2f}"
    else:
        # EUR/USD için aynı format
        payment_amount_str = f"{amount_cents / 100:.2f}"

    merchant_oid = f"autorenew_{institution.id}_{int(datetime.now(timezone.utc).timestamp())}"

    user_basket = json.dumps([
        [
            f"Otomatik Kredi Yenileme - {institution.name}",
            payment_amount_str,
            1,
        ]
    ])

    paytr_token = _build_paytr_token(
        merchant_id=merchant_id,
        merchant_key=merchant_key,
        merchant_salt=merchant_salt,
        data={
            "user_ip": user_ip,
            "merchant_oid": merchant_oid,
            "email": (institution.email or "billing@noryaai.com").strip(),
            "payment_amount": payment_amount_str,
            "user_basket": user_basket,
            "no_installment": "0",
            "max_installment": "0",
            "currency": currency,
            "test_mode": "0",
            "payment_type": "card",
            "non_3d": "1",
            "order_id": "",
            "installment_count": "0",
        },
    )

    payload = {
        "merchant_id": merchant_id,
        "paytr_token": paytr_token,
        "user_ip": user_ip,
        "merchant_oid": merchant_oid,
        "email": (institution.email or "billing@noryaai.com").strip(),
        "payment_amount": payment_amount_str,
        "user_basket": user_basket,
        "no_installment": "0",
        "max_installment": "0",
        "currency": currency,
        "test_mode": "0",
        "payment_type": "card",
        "non_3d": "1",
        "order_id": "",
        "installment_count": "0",
        # Kayıtlı kart bilgileri
        "utoken": institution.paytr_utoken,
        "ctoken": institution.paytr_ctoken,
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.post(PAYTR_RECURRING_URL, data=payload)
            resp.raise_for_status()
            result = resp.json()

        status = result.get("status", "failed")
        reason = result.get("reason", "Bilinmeyen hata")
        reference_no = result.get("reference_no", "")

        if status == "success":
            log.info(
                "PAYTR_RECURRING: success institution_id=%s merchant_oid=%s reference_no=%s",
                institution.id,
                merchant_oid,
                reference_no,
            )
            return {
                "status": "success",
                "merchant_oid": merchant_oid,
                "reason": "",
                "reference_no": reference_no,
            }
        else:
            log.warning(
                "PAYTR_RECURRING: failed institution_id=%s merchant_oid=%s reason=%s",
                institution.id,
                merchant_oid,
                reason,
            )
            return {
                "status": "failed",
                "merchant_oid": merchant_oid,
                "reason": reason,
                "reference_no": "",
            }

    except httpx.HTTPStatusError as e:
        log.error("PAYTR_RECURRING HTTP error: %s", e)
        return {
            "status": "failed",
            "merchant_oid": merchant_oid,
            "reason": f"HTTP hatası: {e.response.status_code}",
            "reference_no": "",
        }
    except httpx.RequestError as e:
        log.error("PAYTR_RECURRING connection error: %s", e)
        return {
            "status": "failed",
            "merchant_oid": merchant_oid,
            "reason": f"Bağlantı hatası: {e}",
            "reference_no": "",
        }
    except Exception as e:
        log.exception("PAYTR_RECURRING unexpected error: %s", e)
        return {
            "status": "failed",
            "merchant_oid": merchant_oid,
            "reason": f"Beklenmeyen hata: {e}",
            "reference_no": "",
        }


def process_auto_renew_for_institution(
    db: Session,
    institution_id: int,
    user_ip: str = "127.0.0.1",
) -> dict:
    """Tek bir kurum için otomatik yenileme işlemini gerçekleştirir.

    Returns:
        dict: {"status": "success"|"failed"|"skipped", "message": str}
    """
    inst = db.get(Institution, institution_id)
    if not inst:
        return {"status": "failed", "message": "Kurum bulunamadı"}

    if not inst.auto_renew_enabled:
        return {"status": "skipped", "message": "Otomatik yenileme devre dışı"}

    if inst.billing_wallet_balance >= inst.auto_renew_threshold_cents:
        return {"status": "skipped", "message": "Bakiye eşik değerin üzerinde"}

    # Son yenileme tarihini kontrol et (çok sık yenilemeyi önle)
    if inst.auto_renew_last_at:
        from datetime import timedelta
        days_since = (datetime.utcnow() - inst.auto_renew_last_at).days
        if days_since < inst.auto_renew_interval_days:
            return {
                "status": "skipped",
                "message": f"Son yenilemeden {days_since} gün geçti, {inst.auto_renew_interval_days} gün beklenmeli",
            }

    # Ödeme yap
    result = execute_recurring_payment(
        institution=inst,
        amount_cents=inst.auto_renew_amount_cents,
        user_ip=user_ip,
    )

    if result["status"] == "success":
        # Cüzdana kredi ekle
        inst.billing_wallet_balance += inst.auto_renew_amount_cents
        inst.auto_renew_last_at = datetime.utcnow()
        db.add(inst)

        # Transaction kaydı
        from app.models.tenant_wallet_transaction import TenantWalletTransaction
        txn = TenantWalletTransaction(
            institution_id=inst.id,
            amount_cents=inst.auto_renew_amount_cents,
            transaction_type="auto_renew",
            description=f"Otomatik kredi yenileme (PayTR) - merchant_oid: {result['merchant_oid']}",
        )
        db.add(txn)
        db.commit()

        log.info(
            "AUTO_RENEW: success institution_id=%s amount=%d new_balance=%d",
            inst.id,
            inst.auto_renew_amount_cents,
            inst.billing_wallet_balance,
        )
        return {
            "status": "success",
            "message": f"Otomatik yenileme başarılı. {inst.auto_renew_amount_cents / 100:.2f} kredi eklendi.",
        }
    else:
        log.warning(
            "AUTO_RENEW: failed institution_id=%s reason=%s",
            inst.id,
            result.get("reason", ""),
        )
        return {
            "status": "failed",
            "message": f"Otomatik yenileme başarısız: {result.get('reason', '')}",
        }


def process_all_auto_renewals(db: Session, user_ip: str = "127.0.0.1") -> list[dict]:
    """Tüm kurumlar için otomatik yenileme kontrolü yapar.

    Returns:
        list[dict]: Her kurum için işlem sonucu
    """
    stmt = select(Institution).where(Institution.auto_renew_enabled == True)
    institutions = db.exec(stmt).all()

    results = []
    for inst in institutions:
        result = process_auto_renew_for_institution(db, inst.id, user_ip)
        results.append({
            "institution_id": inst.id,
            "institution_name": inst.name,
            **result,
        })

    return results
