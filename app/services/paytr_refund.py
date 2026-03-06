"""PayTR İade API: sipariş için tam veya kısmi iade isteği."""
from __future__ import annotations

import base64
import hashlib
import hmac
import logging
from typing import NamedTuple
from urllib.parse import urlencode

from app.core.config import settings

log = logging.getLogger(__name__)

PAYTR_REFUND_URL = "https://www.paytr.com/odeme/iade"


class RefundResult(NamedTuple):
    success: bool
    message: str
    """Hata veya başarı mesajı."""
    reference_no: str | None
    """PayTR'den dönen reference_no (varsa)."""


def _return_amount_str(amount_eur_cents: int, currency: str) -> str:
    """İade tutarını PayTR'nin beklediği formata çevirir (nokta ayraçlı string)."""
    if currency == "TL":
        rate = float(getattr(settings, "paytr_eur_to_try_rate", 0) or 0)
        if rate <= 0:
            rate = 35.0
        tl = (amount_eur_cents / 100) * rate
        return f"{tl:.2f}"
    # EUR
    return f"{amount_eur_cents / 100:.2f}"


def paytr_refund(
    merchant_oid: str,
    return_amount_eur_cents: int,
    currency: str = "EUR",
    reference_no: str | None = None,
) -> RefundResult:
    """
    PayTR İade API'ye istek atar. Tam veya kısmi iade.
    return_amount_eur_cents: iade edilecek tutar (EUR cent). Sipariş tutarından fazla olamaz.
    """
    merchant_id = (getattr(settings, "paytr_merchant_id", None) or "").strip()
    merchant_key = (getattr(settings, "paytr_merchant_key", None) or "").strip()
    merchant_salt = (getattr(settings, "paytr_merchant_salt", None) or "").strip()

    if not merchant_id or not merchant_key or not merchant_salt:
        return RefundResult(
            success=False,
            message="PayTR iade için merchant_id / merchant_key / merchant_salt tanımlı değil.",
            reference_no=None,
        )

    return_amount = _return_amount_str(return_amount_eur_cents, currency)
    key_bytes = merchant_key.encode() if isinstance(merchant_key, str) else merchant_key
    hash_str = f"{merchant_id}{merchant_oid}{return_amount}{merchant_salt}"
    paytr_token = base64.b64encode(
        hmac.new(key_bytes, hash_str.encode(), hashlib.sha256).digest()
    ).decode()

    post_vals = {
        "merchant_id": merchant_id,
        "merchant_oid": merchant_oid,
        "return_amount": return_amount,
        "paytr_token": paytr_token,
    }
    if reference_no and len(reference_no) <= 64:
        post_vals["reference_no"] = reference_no

    try:
        from urllib.request import Request, urlopen
        from urllib.error import URLError

        req = Request(
            PAYTR_REFUND_URL,
            data=urlencode(post_vals).encode(),
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        with urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        log.warning("PayTR iade API bağlantı hatası: %s", e)
        return RefundResult(
            success=False,
            message=f"PayTR bağlantı hatası: {getattr(e, 'reason', str(e))}",
            reference_no=None,
        )
    except Exception as e:
        log.warning("PayTR iade API hata: %s", e)
        return RefundResult(success=False, message=str(e)[:200], reference_no=None)

    try:
        import json
        res = json.loads(body)
    except Exception as e:
        return RefundResult(
            success=False,
            message=f"PayTR yanıtı okunamadı: {e}",
            reference_no=None,
        )

    status = (res.get("status") or "").strip().lower()
    if status == "success":
        return RefundResult(
            success=True,
            message="İade talebi PayTR tarafından kabul edildi.",
            reference_no=res.get("reference_no") or None,
        )
    err_msg = res.get("err_msg") or res.get("err_no") or body
    return RefundResult(
        success=False,
        message=f"PayTR iade reddi: {err_msg}"[:300],
        reference_no=None,
    )
