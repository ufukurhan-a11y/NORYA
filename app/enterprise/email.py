# -*- coding: utf-8 -*-
"""Enterprise email delivery — SMTP-based invitation emails with token fallback."""
from __future__ import annotations

import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log = logging.getLogger("norya.enterprise.email")

SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_FROM = os.getenv("SMTP_FROM", "noreply@norya.ai")
SMTP_TLS = os.getenv("SMTP_TLS", "1") == "1"
BASE_URL = os.getenv("BASE_URL", "https://app.norya.ai")


def is_smtp_configured() -> bool:
    return bool(SMTP_HOST and SMTP_USER and SMTP_PASS)


def send_invite_email(
    to_email: str,
    institution_name: str,
    inviter_name: str,
    role: str,
    token: str,
    lang: str = "tr",
) -> bool:
    """Send invitation email. Returns True on success, False on failure (token fallback applies)."""
    if not is_smtp_configured():
        log.info("SMTP not configured — skipping email for %s (token: %s)", to_email, token[:8])
        return False

    join_url = f"{BASE_URL}/institution/join/{token}"

    subject, body_html = _build_invite_content(
        institution_name=institution_name,
        inviter_name=inviter_name,
        role=role,
        join_url=join_url,
        lang=lang,
    )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_FROM
    msg["To"] = to_email
    msg.attach(MIMEText(f"{subject}\n\n{join_url}", "plain", "utf-8"))
    msg.attach(MIMEText(body_html, "html", "utf-8"))

    try:
        if SMTP_TLS:
            server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=15)
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15)
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_FROM, [to_email], msg.as_string())
        server.quit()
        log.info("Invite email sent to %s for institution %s", to_email, institution_name)
        return True
    except Exception:
        log.exception("Failed to send invite email to %s", to_email)
        return False


def _build_invite_content(
    institution_name: str,
    inviter_name: str,
    role: str,
    join_url: str,
    lang: str,
) -> tuple[str, str]:
    """Return (subject, html_body) for the invitation."""
    subjects = {
        "tr": f"NoryaAI — {institution_name} kurumuna davet",
        "en": f"NoryaAI — Invitation to join {institution_name}",
        "de": f"NoryaAI — Einladung zu {institution_name}",
        "es": f"NoryaAI — Invitación a {institution_name}",
        "fr": f"NoryaAI — Invitation à rejoindre {institution_name}",
        "it": f"NoryaAI — Invito a {institution_name}",
        "he": f"NoryaAI — הזמנה להצטרף ל-{institution_name}",
        "hi": f"NoryaAI — {institution_name} में शामिल होने का निमंत्रण",
        "ar": f"NoryaAI — دعوة للانضمام إلى {institution_name}",
    }
    subject = subjects.get(lang, subjects["en"])

    cta_labels = {
        "tr": "Daveti Kabul Et",
        "en": "Accept Invitation",
        "de": "Einladung annehmen",
        "es": "Aceptar invitación",
        "fr": "Accepter l'invitation",
        "it": "Accetta invito",
        "he": "קבל הזמנה",
        "hi": "निमंत्रण स्वीकार करें",
        "ar": "قبول الدعوة",
    }
    cta = cta_labels.get(lang, cta_labels["en"])

    body_lines = {
        "tr": (
            f"{inviter_name} sizi <strong>{institution_name}</strong> kurumuna "
            f"<strong>{role}</strong> rolüyle davet etti.",
            "Aşağıdaki bağlantıya tıklayarak kuruma katılabilirsiniz.",
        ),
        "en": (
            f"{inviter_name} has invited you to join <strong>{institution_name}</strong> "
            f"as <strong>{role}</strong>.",
            "Click the link below to accept the invitation.",
        ),
    }
    intro, action = body_lines.get(lang, body_lines["en"])

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="utf-8"></head>
<body style="margin:0;padding:0;background:#f4f5f7;font-family:Inter,system-ui,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f5f7;padding:40px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
        <tr><td style="background:linear-gradient(135deg,#006a69,#0ea5a4);padding:28px 32px;">
          <h1 style="margin:0;color:#fff;font-size:20px;font-weight:700;">NoryaAI</h1>
        </td></tr>
        <tr><td style="padding:32px;">
          <p style="margin:0 0 16px;font-size:15px;line-height:1.6;color:#1a1c1e;">{intro}</p>
          <p style="margin:0 0 24px;font-size:14px;line-height:1.6;color:#44474e;">{action}</p>
          <a href="{join_url}" style="display:inline-block;background:#006a69;color:#fff;padding:12px 28px;border-radius:10px;text-decoration:none;font-weight:600;font-size:14px;">{cta}</a>
          <p style="margin:24px 0 0;font-size:12px;color:#74777f;word-break:break-all;">{join_url}</p>
        </td></tr>
        <tr><td style="padding:16px 32px;background:#f8f9fa;border-top:1px solid #e8eaed;">
          <p style="margin:0;font-size:11px;color:#74777f;">NoryaAI Enterprise · {institution_name}</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""
    return subject, html
