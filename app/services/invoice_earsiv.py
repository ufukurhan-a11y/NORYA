"""GİB e-Arşiv fatura kesimi (eArsivPortal). Tutar EUR → TL config kuru ile dönüştürülür."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import NamedTuple

from app.core.config import settings


class EarsivResult(NamedTuple):
    ettn: str
    gib_no: str | None  # Onay sonrası alınır
    success: bool
    message: str


def _product_label(product: str) -> str:
    labels = {
        "single": "Norya - 1 Analiz",
        "monthly": "Norya Pro - Aylık Abonelik",
        "yearly": "Norya Pro - Yıllık Abonelik",
    }
    return labels.get(product, product)


def eur_to_try(eur_cents: int) -> float:
    """EUR cent → TL (config kuru)."""
    rate = getattr(settings, "invoice_eur_to_try_rate", None) or 35.0
    return round((eur_cents / 100) * float(rate), 2)


def create_earsiv_invoice(
    *,
    amount_eur_cents: int,
    product: str,
    customer_tckn: str,
    customer_ad: str,
    customer_soyad: str,
    customer_unvan: str = "",
    customer_vergi_dairesi: str = "",
    fatura_notu: str = "",
) -> EarsivResult:
    """
    GİB e-arşiv fatura oluşturur. Başarılıysa ETTN döner.
    SMS onayı portal tarafında gerekebilir; bu fonksiyon sadece faturayı oluşturur.
    """
    try:
        from eArsivPortal import eArsivPortal
    except ImportError:
        return EarsivResult(
            ettn="",
            gib_no=None,
            success=False,
            message="eArsivPortal kurulu değil. pip install eArsivPortal",
        )

    user = (getattr(settings, "gib_earsiv_user", None) or "").strip()
    password = (getattr(settings, "gib_earsiv_password", None) or "").strip()
    if not user or not password:
        return EarsivResult(
            ettn="",
            gib_no=None,
            success=False,
            message="GIB_EARSIV_USER ve GIB_EARSIV_PASSWORD .env'de tanımlı olmalı.",
        )

    test_mode = (getattr(settings, "gib_earsiv_test_mode", "1") or "1").strip() == "1"
    tckn = (customer_tckn or "").strip().replace(" ", "")
    if len(tckn) not in (10, 11):
        return EarsivResult(
            ettn="",
            gib_no=None,
            success=False,
            message="Alıcı TC Kimlik No 10 veya 11 haneli olmalı.",
        )

    ad = (customer_ad or "").strip()
    soyad = (customer_soyad or "").strip()
    if not ad and not soyad:
        return EarsivResult(
            ettn="",
            gib_no=None,
            success=False,
            message="Alıcı ad veya soyad gerekli.",
        )

    now = datetime.now(timezone.utc)
    tarih = now.strftime("%d/%m/%Y")
    saat = now.strftime("%H:%M:%S")
    urun_adi = _product_label(product)
    fiyat_tl = eur_to_try(amount_eur_cents)
    if fiyat_tl <= 0:
        return EarsivResult(
            ettn="",
            gib_no=None,
            success=False,
            message="Tutar TL'ye çevrildiğinde 0 veya negatif olamaz. INVOICE_EUR_TO_TRY_RATE kontrol edin.",
        )

    note = (fatura_notu or "").strip()
    if not note:
        note = f"Sipariş tutarı EUR karşılığı (1 EUR = {getattr(settings, 'invoice_eur_to_try_rate', 35)} TL)"

    portal = eArsivPortal(
        kullanici_kodu=user,
        sifre=password,
        test_modu=test_mode,
    )
    try:
        result = portal.fatura_olustur(
            tarih=tarih,
            saat=saat,
            vkn_veya_tckn=tckn,
            ad=ad or "-",
            soyad=soyad or "-",
            unvan=(customer_unvan or "").strip(),
            vergi_dairesi=(customer_vergi_dairesi or "").strip(),
            urun_adi=urun_adi,
            fiyat=fiyat_tl,
            fatura_notu=note,
        )
    except Exception as e:
        return EarsivResult(
            ettn="",
            gib_no=None,
            success=False,
            message=str(e),
        )
    finally:
        try:
            portal.cikis_yap()
        except Exception:
            pass

    ettn = getattr(result, "ettn", None) or ""
    if not ettn:
        return EarsivResult(
            ettn="",
            gib_no=None,
            success=False,
            message="GİB ETTN dönmedi. Portal/SMS onayı gerekebilir.",
        )
    return EarsivResult(
        ettn=ettn,
        gib_no=None,
        success=True,
        message="Fatura oluşturuldu. GİB portalında SMS ile onaylayabilirsiniz.",
    )
