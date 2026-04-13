"""Tenant low balance email alert service.

Sends email notifications when a tenant's wallet balance falls below the threshold.
"""
import logging
from datetime import datetime, timedelta

from sqlmodel import Session, select

from app.models.institution import Institution
from app.core.config import settings

logger = logging.getLogger(__name__)


def check_and_send_low_balance_alerts(session: Session) -> list[dict]:
    """Check all active tenants for low balance and send email alerts.

    Returns list of alerts that were sent.
    """
    stmt = select(Institution).where(
        Institution.is_active == True,
        Institution.status == "active",
        Institution.billing_wallet_balance <= Institution.wallet_low_threshold,
        Institution.alert_email_enabled == True,
        Institution.contact_email.isnot(None),
    )
    institutions = session.exec(stmt).all()

    alerts_sent = []
    for inst in institutions:
        # Avoid spamming - only alert if last alert was > 24 hours ago
        if inst.wallet_last_alert:
            time_since_last = datetime.utcnow() - inst.wallet_last_alert
            if time_since_last < timedelta(hours=24):
                continue

        # Send email alert
        success = _send_low_balance_email(inst)
        if success:
            inst.wallet_last_alert = datetime.utcnow()
            session.add(inst)
            alerts_sent.append({
                "institution_id": inst.id,
                "name": inst.name,
                "tenant_slug": inst.tenant_slug,
                "contact_email": inst.contact_email,
                "balance": inst.billing_wallet_balance,
                "threshold": inst.wallet_low_threshold,
            })

    if alerts_sent:
        session.commit()

    return alerts_sent


def _send_low_balance_email(institution: Institution) -> bool:
    """Send low balance alert email to institution contact."""
    try:
        from app.services.email_service import send_email

        balance_formatted = f"${institution.billing_wallet_balance / 100:.2f}"
        threshold_formatted = f"${institution.wallet_low_threshold / 100:.2f}"

        subject = f"[NoryaAI] Düşük Bakiye Uyarısı - {institution.name}"
        body = f"""
Sayın {institution.name} Yetkilisi,

Hesabınızın bakiyesi düşük seviyeye ulaşmıştır.

Mevcut Bakiye: {balance_formatted}
Uyarı Eşiği: {threshold_formatted}
Analiz Başına Maliyet: ${institution.cost_per_analysis / 100:.2f}
Kalan Analiz Hakkı: {institution.billing_wallet_balance // institution.cost_per_analysis if institution.cost_per_analysis > 0 else 0}

Lütfen hesabınıza kredi yükleyerek analiz hizmetinizin kesintisiz devam etmesini sağlayın.

Portal: https://noryaai.com/hastane/{institution.tenant_slug}/billing

Bu bir otomatik mesajdır. Lütfen yanıtlamayın.

Saygılarımızla,
NoryaAI Ekibi
        """.strip()

        send_email(
            to_email=institution.contact_email,
            subject=subject,
            body=body,
        )

        logger.info(
            f"Low balance alert sent to {institution.contact_email} "
            f"for institution {institution.name} (balance: {balance_formatted})"
        )
        return True

    except ImportError:
        # email_service not available, log warning
        logger.warning(
            f"Low balance alert for {institution.name} - email service not configured. "
            f"Balance: ${institution.billing_wallet_balance / 100:.2f}"
        )
        return False
    except Exception as e:
        logger.error(f"Failed to send low balance alert to {institution.contact_email}: {e}")
        return False


def send_manual_low_balance_alert(
    session: Session,
    institution_id: int,
) -> bool:
    """Manually trigger a low balance alert for a specific institution."""
    stmt = select(Institution).where(Institution.id == institution_id)
    inst = session.exec(stmt).first()

    if not inst:
        return False

    return _send_low_balance_email(inst)
