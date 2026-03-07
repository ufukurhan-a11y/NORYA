"""Rapor bazlı QR doğrulama: get_or_create verification, signed token, QR PNG base64."""
import base64
import io
import secrets
from typing import Any

from sqlmodel import Session, select

from app.core.security import create_report_verification_token
from app.models.report_verification import ReportVerification


def _generate_report_id() -> str:
    """Tahmin edilemez public rapor ID (32 hex karakter)."""
    return secrets.token_hex(16)


def _generate_verification_code() -> str:
    """İnsan okunabilir kısa kod (8 karakter, büyük harf + rakam)."""
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "".join(secrets.choice(alphabet) for _ in range(8))


def _qr_png_base64(url: str, size_px: int = 120) -> str:
    """URL için QR kod PNG üretir; base64 string döner. WeasyPrint embed için."""
    try:
        import qrcode
        buf = io.BytesIO()
        qr = qrcode.QRCode(version=1, box_size=4, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#0F172A", back_color="white")
        img = img.resize((size_px, size_px))
        img.save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode("ascii")
    except Exception:
        return ""


def get_or_create_verification(
    db: Session,
    analysis_id: int,
    user_id: int,
    plan: str,
    language: str,
    base_url: str,
) -> dict[str, Any] | None:
    """
    Tek analiz, aylık veya yıllık paket için bu analize ait doğrulama kaydını getirir veya oluşturur.
    Müşteri PDF'deki QR ile raporun doğruluğunu ve orijinalliğini doğrulayabilir.
    base_url: örn. https://norya.com (verify sayfası için; /verify/... burada üretilir).
    Dönen dict: report_id, verification_code, verification_url, signed_token, qr_image_base64.
    plan single/monthly/yearly değilse None döner.
    """
    plan = (plan or "").strip().lower()
    if plan not in ("single", "monthly", "yearly"):
        return None
    base_url = (base_url or "").strip().rstrip("/")
    if not base_url:
        return None

    existing = db.exec(
        select(ReportVerification).where(ReportVerification.analysis_id == analysis_id)
    ).first()
    if existing and existing.is_active:
        report_id = existing.report_id
        verification_code = existing.verification_code
    else:
        report_id = _generate_report_id()
        verification_code = _generate_verification_code()
        if existing:
            existing.report_id = report_id
            existing.verification_code = verification_code
            existing.is_active = True
            existing.report_status = "completed"
            existing.package_type = plan
            existing.language = language
            db.add(existing)
        else:
            rv = ReportVerification(
                report_id=report_id,
                analysis_id=analysis_id,
                user_id=user_id,
                package_type=plan,
                language=language,
                verification_code=verification_code,
                is_active=True,
                report_status="completed",
            )
            db.add(rv)
        db.commit()

    signed_token = create_report_verification_token(report_id, verification_code)
    verification_url = f"{base_url}/verify/{report_id}?token={signed_token}"
    qr_image_base64 = _qr_png_base64(verification_url)

    return {
        "report_id": report_id,
        "verification_code": verification_code,
        "verification_url": verification_url,
        "signed_token": signed_token,
        "qr_image_base64": qr_image_base64,
    }
