"""Drip (zamanlı) e-posta kampanya motoru.

Lead subscribe olduktan sonra otomatik e-posta serisi:
  Step 0: Gün 0  - Welcome email (mevcut send_welcome_email ile gönderiliyor)
  Step 1: Gün 2  - Eğitim: "Kan tahlili nasıl okunur?"
  Step 2: Gün 5  - Sosyal kanıt + örnek rapor
  Step 3: Gün 8  - İndirim teklifi
  Step 4: Gün 14 - Son şans (urgency)
  Step 5: Gün 30 - Aylık sağlık bülteni

Scheduler: process_drip_emails() fonksiyonu cron/background task olarak çağrılır.
"""
import logging
from datetime import datetime, timedelta, timezone

from sqlmodel import Session, select

from app.core.config import settings
from app.core.database import engine
from app.models.drip_email import DripEmailLog
from app.models.email_lead import EmailLead
from app.services.email_sender import send_email

log = logging.getLogger("norya.drip")

DRIP_STEPS = {
    1: {"delay_days": 2, "builder": "build_drip_education"},
    2: {"delay_days": 5, "builder": "build_drip_social_proof"},
    3: {"delay_days": 8, "builder": "build_drip_discount"},
    4: {"delay_days": 14, "builder": "build_drip_urgency"},
    5: {"delay_days": 30, "builder": "build_drip_newsletter"},
}

_BASE_URL = None


def _get_base_url() -> str:
    global _BASE_URL
    if _BASE_URL:
        return _BASE_URL
    _BASE_URL = (getattr(settings, "frontend_url", None) or "https://noryaai.com").rstrip("/")
    return _BASE_URL


def _email_wrapper(lang: str, subject: str, body_html: str) -> str:
    base = _get_base_url()
    logo_url = f"{base}/static/norya_logo_transparent_trim.png"
    dir_attr = ' dir="rtl"' if lang in ("he", "ar") else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/><title>{subject}</title></head>
<body style="margin:0;padding:0;background-color:#f1f5f9;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background-color:#f1f5f9;">
<tr><td align="center" style="padding:32px 16px;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:520px;background:#ffffff;border-radius:16px;box-shadow:0 4px 24px rgba(10,25,41,0.08);overflow:hidden;">
<tr><td style="background:linear-gradient(135deg,#1a2d42 0%,#2d4a6f 50%,#0d9488 100%);padding:24px;text-align:center;">
<img src="{logo_url}" alt="Norya" style="height:48px;width:auto;max-width:180px;display:block;margin:0 auto 6px;object-fit:contain;" />
<div style="font-size:16px;font-weight:600;color:#ffffff;">NoryaAI</div>
</td></tr>
<tr><td style="padding:28px 24px;">
{body_html}
</td></tr>
<tr><td style="padding:16px 24px;border-top:1px solid #e2e8f0;font-size:12px;color:#94a3b8;text-align:center;">
&copy; NoryaAI &middot; <a href="{base}/api/lead/unsubscribe?email={{{{email}}}}" style="color:#94a3b8;text-decoration:underline;">Unsubscribe</a>
</td></tr>
</table>
</td></tr></table>
</body></html>"""


# -- Step 1: Education ---------------------------------------------------

_DRIP_EDU_SUBJECT = {
    "tr": "Kan tahlilini nasıl okumalısın?",
    "en": "How to read your blood test results",
    "de": "So lesen Sie Ihre Blutwerte richtig",
    "fr": "Comment lire vos résultats d'analyses sanguines",
    "es": "Cómo leer sus resultados de análisis de sangre",
    "it": "Come leggere le tue analisi del sangue",
}

_DRIP_EDU_BODY = {
    "tr": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Kan tahlilini okumak zor mu?</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">Çoğu kişi tahlil sonuçlarını aldığında ne anlama geldiğini anlamakta zorlanır. İşte bilmeniz gereken <strong>5 temel değer</strong>:</p>
<ul style="margin:0 0 20px;padding-left:20px;list-style:disc;">
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>Hemoglobin (Hb)</strong> — Kansızlık göstergesi</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>Glukoz</strong> — Kan şekeri seviyesi</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>TSH</strong> — Tiroid fonksiyonu</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>LDL Kolesterol</strong> — "Kötü" kolesterol</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>Vitamin D</strong> — Kemik ve bağışıklık sağlığı</li>
</ul>
<p style="margin:0 0 24px;font-size:15px;line-height:1.7;color:#334155;">NoryaAI, tahlilinizdeki <strong>tüm değerleri</strong> analiz edip size anlaşılır bir rapor sunar.</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/analyze" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">Tahlilimi analiz et</a>
</p>
""",
    "en": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Confused by your blood test results?</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">Most people struggle to understand their lab results. Here are <strong>5 key markers</strong> you should know:</p>
<ul style="margin:0 0 20px;padding-left:20px;list-style:disc;">
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>Hemoglobin (Hb)</strong> — Anemia indicator</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>Glucose</strong> — Blood sugar level</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>TSH</strong> — Thyroid function</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>LDL Cholesterol</strong> — "Bad" cholesterol</li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><strong>Vitamin D</strong> — Bone &amp; immune health</li>
</ul>
<p style="margin:0 0 24px;font-size:15px;line-height:1.7;color:#334155;">NoryaAI analyzes <strong>every marker</strong> in your report and explains them in plain language.</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/analyze" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">Analyze my blood test</a>
</p>
""",
}

# -- Step 2: Social proof ------------------------------------------------

_DRIP_SOCIAL_SUBJECT = {
    "tr": "Binlerce kişi tahlilini NoryaAI ile analiz etti",
    "en": "Thousands of people trust NoryaAI with their lab results",
    "de": "Tausende vertrauen NoryaAI ihre Blutwerte an",
    "fr": "Des milliers de personnes font confiance à NoryaAI",
    "es": "Miles de personas confían en NoryaAI",
    "it": "Migliaia di persone si affidano a NoryaAI",
}

_DRIP_SOCIAL_BODY = {
    "tr": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Neden NoryaAI?</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">Binlerce kullanıcı tahlillerini NoryaAI ile analiz etti. İşte bazı sonuçlar:</p>
<div style="margin:0 0 20px;padding:16px;background:#f0fdfa;border-radius:12px;border:1px solid #99f6e4;">
<p style="margin:0 0 10px;font-size:14px;color:#134e4a;"><strong>"Doktora gitmeden önce neyi sormam gerektiğini anladım."</strong></p>
<p style="margin:0 0 12px;font-size:14px;color:#134e4a;"><strong>"Yıllardır düşük olan B12'mi fark etmemişim."</strong></p>
<p style="margin:0;font-size:14px;color:#134e4a;"><strong>"Rapor çok net ve anlaşılır."</strong></p>
</div>
<p style="margin:0 0 8px;text-align:center;">
<a href="{base_url}/en/sample-blood-test-reports" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">Örnek raporu incele</a>
</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/analyze" style="color:#0d9488;text-decoration:underline;font-size:14px;">veya tahlilini şimdi analiz et →</a>
</p>
""",
    "en": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Why NoryaAI?</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">Thousands of users have analyzed their lab results with NoryaAI. Here's what they say:</p>
<div style="margin:0 0 20px;padding:16px;background:#f0fdfa;border-radius:12px;border:1px solid #99f6e4;">
<p style="margin:0 0 10px;font-size:14px;color:#134e4a;"><strong>"I finally understood what to ask my doctor."</strong></p>
<p style="margin:0 0 12px;font-size:14px;color:#134e4a;"><strong>"I didn't realize my B12 had been low for years."</strong></p>
<p style="margin:0;font-size:14px;color:#134e4a;"><strong>"The report is incredibly clear and actionable."</strong></p>
</div>
<p style="margin:0 0 8px;text-align:center;">
<a href="{base_url}/en/sample-blood-test-reports" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">See a sample report</a>
</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/analyze" style="color:#0d9488;text-decoration:underline;font-size:14px;">or analyze your blood test now →</a>
</p>
""",
}

# -- Step 3: Discount -----------------------------------------------------

_DRIP_DISCOUNT_SUBJECT = {
    "tr": "Sana özel %20 indirim — ilk analizin için",
    "en": "Your exclusive 20% off — for your first analysis",
    "de": "Ihr exklusiver 20 % Rabatt — für Ihre erste Analyse",
    "fr": "Votre réduction exclusive de 20 % — pour votre première analyse",
    "es": "Su descuento exclusivo del 20 % — para su primer análisis",
    "it": "Il tuo sconto esclusivo del 20% — per la tua prima analisi",
}

_DRIP_DISCOUNT_BODY = {
    "tr": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Sana özel teklif!</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">İlk kan tahlili analizin için <strong>%20 indirim</strong> kazandın. Aşağıdaki kodu ödeme sayfasında kullan:</p>
<div style="margin:0 0 20px;text-align:center;">
<div style="display:inline-block;padding:16px 32px;background:#0f172a;border-radius:12px;">
<span style="font-size:24px;font-weight:800;color:#5eead4;letter-spacing:0.1em;">INDIRIM20</span>
</div>
</div>
<p style="margin:0 0 20px;font-size:14px;color:#64748b;text-align:center;">Tek kullanımlık · Tüm planlar için geçerli</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/pricing" style="display:inline-block;padding:14px 28px;background:#e07a5f;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">İndirimli fiyatları gör</a>
</p>
""",
    "en": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Your exclusive offer!</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">You've earned <strong>20% off</strong> your first blood test analysis. Use the code below at checkout:</p>
<div style="margin:0 0 20px;text-align:center;">
<div style="display:inline-block;padding:16px 32px;background:#0f172a;border-radius:12px;">
<span style="font-size:24px;font-weight:800;color:#5eead4;letter-spacing:0.1em;">INDIRIM20</span>
</div>
</div>
<p style="margin:0 0 20px;font-size:14px;color:#64748b;text-align:center;">One-time use · Valid for all plans</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/pricing" style="display:inline-block;padding:14px 28px;background:#e07a5f;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">See discounted prices</a>
</p>
""",
}

# -- Step 4: Urgency ------------------------------------------------------

_DRIP_URGENCY_SUBJECT = {
    "tr": "İndirim kodun yakında sona eriyor",
    "en": "Your discount code is expiring soon",
    "de": "Ihr Rabattcode läuft bald ab",
    "fr": "Votre code de réduction expire bientôt",
    "es": "Su código de descuento está por vencer",
    "it": "Il tuo codice sconto sta per scadere",
}

_DRIP_URGENCY_BODY = {
    "tr": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Son şans!</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">Sana özel <strong>%20 indirim kodun</strong> birkaç gün içinde geçerliliğini yitiriyor. Tahlilini henüz analiz etmediysen şimdi tam zamanı.</p>
<div style="margin:0 0 20px;text-align:center;">
<div style="display:inline-block;padding:12px 24px;background:#fef2f2;border:2px solid #fca5a5;border-radius:12px;">
<span style="font-size:20px;font-weight:800;color:#dc2626;">INDIRIM20</span>
<span style="font-size:13px;color:#991b1b;display:block;margin-top:4px;">Süresi doluyor!</span>
</div>
</div>
<p style="margin:0;text-align:center;">
<a href="{base_url}/analyze" style="display:inline-block;padding:14px 28px;background:#dc2626;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">Şimdi analiz et</a>
</p>
""",
    "en": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Last chance!</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">Your exclusive <strong>20% discount code</strong> is expiring in a few days. If you haven't analyzed your blood test yet, now is the time.</p>
<div style="margin:0 0 20px;text-align:center;">
<div style="display:inline-block;padding:12px 24px;background:#fef2f2;border:2px solid #fca5a5;border-radius:12px;">
<span style="font-size:20px;font-weight:800;color:#dc2626;">INDIRIM20</span>
<span style="font-size:13px;color:#991b1b;display:block;margin-top:4px;">Expiring soon!</span>
</div>
</div>
<p style="margin:0;text-align:center;">
<a href="{base_url}/analyze" style="display:inline-block;padding:14px 28px;background:#dc2626;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">Analyze now</a>
</p>
""",
}

# -- Step 5: Newsletter ---------------------------------------------------

_DRIP_NEWSLETTER_SUBJECT = {
    "tr": "Aylık sağlık rehberiniz — NoryaAI",
    "en": "Your monthly health guide — NoryaAI",
    "de": "Ihr monatlicher Gesundheitsratgeber — NoryaAI",
    "fr": "Votre guide santé mensuel — NoryaAI",
    "es": "Su guía de salud mensual — NoryaAI",
    "it": "La tua guida alla salute mensile — NoryaAI",
}

_DRIP_NEWSLETTER_BODY = {
    "tr": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">Bu ay blogumuzdan</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">En çok okunan sağlık rehberlerimizi sizin için derledik:</p>
<ul style="margin:0 0 20px;padding-left:20px;list-style:disc;">
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><a href="{base_url}/tr/blog/demir-eksikligi-ferritin" style="color:#0d9488;text-decoration:underline;">Demir Eksikliği ve Ferritin</a></li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><a href="{base_url}/tr/blog/vitamin-d-eksikligi" style="color:#0d9488;text-decoration:underline;">Vitamin D Eksikliği</a></li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><a href="{base_url}/tr/blog/tiroid-tsh" style="color:#0d9488;text-decoration:underline;">TSH ve Tiroid Fonksiyonu</a></li>
</ul>
<p style="margin:0 0 20px;font-size:15px;line-height:1.7;color:#334155;">Daha fazlası için blogumuzu ziyaret edin.</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/tr/blog" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">Blog'a git</a>
</p>
""",
    "en": """
<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">This month on our blog</p>
<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:#334155;">We've curated our most-read health guides for you:</p>
<ul style="margin:0 0 20px;padding-left:20px;list-style:disc;">
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><a href="{base_url}/en/blog/iron-deficiency-ferritin" style="color:#0d9488;text-decoration:underline;">Iron Deficiency &amp; Ferritin</a></li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><a href="{base_url}/en/blog/vitamin-d-deficiency" style="color:#0d9488;text-decoration:underline;">Vitamin D Deficiency</a></li>
<li style="margin-bottom:8px;font-size:15px;color:#334155;"><a href="{base_url}/en/blog/thyroid-tsh" style="color:#0d9488;text-decoration:underline;">TSH &amp; Thyroid Function</a></li>
</ul>
<p style="margin:0 0 20px;font-size:15px;line-height:1.7;color:#334155;">Visit our blog for more health insights.</p>
<p style="margin:0;text-align:center;">
<a href="{base_url}/en/blog" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">Read the blog</a>
</p>
""",
}


def _get_step_content(step: int, lang: str) -> tuple[str, str] | None:
    """Returns (subject, body_html) for a drip step, or None if not available."""
    base_url = _get_base_url()
    lang_key = lang if lang in ("tr", "en", "de", "fr", "es", "it") else "en"

    if step == 1:
        subj = _DRIP_EDU_SUBJECT.get(lang_key, _DRIP_EDU_SUBJECT["en"])
        body = _DRIP_EDU_BODY.get(lang_key, _DRIP_EDU_BODY["en"])
    elif step == 2:
        subj = _DRIP_SOCIAL_SUBJECT.get(lang_key, _DRIP_SOCIAL_SUBJECT["en"])
        body = _DRIP_SOCIAL_BODY.get(lang_key, _DRIP_SOCIAL_BODY["en"])
    elif step == 3:
        subj = _DRIP_DISCOUNT_SUBJECT.get(lang_key, _DRIP_DISCOUNT_SUBJECT["en"])
        body = _DRIP_DISCOUNT_BODY.get(lang_key, _DRIP_DISCOUNT_BODY["en"])
    elif step == 4:
        subj = _DRIP_URGENCY_SUBJECT.get(lang_key, _DRIP_URGENCY_SUBJECT["en"])
        body = _DRIP_URGENCY_BODY.get(lang_key, _DRIP_URGENCY_BODY["en"])
    elif step == 5:
        subj = _DRIP_NEWSLETTER_SUBJECT.get(lang_key, _DRIP_NEWSLETTER_SUBJECT["en"])
        body = _DRIP_NEWSLETTER_BODY.get(lang_key, _DRIP_NEWSLETTER_BODY["en"])
    else:
        return None

    body = body.replace("{base_url}", base_url)
    full_html = _email_wrapper(lang_key, subj, body).replace("{{email}}", "{email}")
    return subj, full_html


def process_drip_emails(batch_size: int = 50) -> int:
    """Process pending drip emails. Returns number of emails sent.

    Should be called periodically (e.g. every hour via cron or background task).
    """
    now = datetime.now(timezone.utc)
    sent_count = 0

    with Session(engine) as db:
        leads = db.exec(
            select(EmailLead)
            .where(EmailLead.unsubscribed == False)  # noqa: E712
            .where(EmailLead.drip_step < 5)
            .order_by(EmailLead.created_at)
            .limit(batch_size)
        ).all()

        for lead in leads:
            next_step = lead.drip_step + 1
            step_config = DRIP_STEPS.get(next_step)
            if not step_config:
                continue

            created = lead.created_at.replace(tzinfo=timezone.utc) if lead.created_at.tzinfo is None else lead.created_at
            send_after = created + timedelta(days=step_config["delay_days"])
            if now < send_after:
                continue

            lang = (lead.locale or "en").split("-")[0].split("_")[0].strip().lower() or "en"
            content = _get_step_content(next_step, lang)
            if not content:
                continue

            subject, html = content
            html = html.replace("{email}", lead.email)

            already_sent = db.exec(
                select(DripEmailLog)
                .where(DripEmailLog.email == lead.email)
                .where(DripEmailLog.step == next_step)
            ).first()
            if already_sent:
                lead.drip_step = next_step
                db.add(lead)
                db.commit()
                continue

            ok = send_email(lead.email, subject, html)
            if ok:
                db.add(DripEmailLog(email=lead.email, step=next_step))
                lead.drip_step = next_step
                lead.drip_last_sent_at = now
                db.add(lead)
                db.commit()
                sent_count += 1
                log.info("Drip step %d sent to %s", next_step, lead.email)
            else:
                log.warning("Drip step %d failed for %s", next_step, lead.email)

    return sent_count
