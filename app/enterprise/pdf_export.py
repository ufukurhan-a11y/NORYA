# -*- coding: utf-8 -*-
"""Enterprise PDF export — WeasyPrint-based report PDF generation."""
from __future__ import annotations

import io
import logging
from datetime import datetime

log = logging.getLogger("norya.enterprise.pdf")

_RTL_LANGS = frozenset({"he", "ar"})


def generate_report_pdf(
    report_text: str,
    case_filename: str | None,
    institution_name: str,
    language: str = "tr",
    case_id: int | None = None,
    report_date: datetime | None = None,
) -> bytes:
    """Generate a styled PDF from a report text. Returns PDF bytes."""
    try:
        from weasyprint import HTML
    except ImportError:
        log.error("weasyprint not installed — cannot generate PDF")
        raise RuntimeError("PDF generation unavailable")

    direction = "rtl" if language in _RTL_LANGS else "ltr"
    date_str = (report_date or datetime.utcnow()).strftime("%d.%m.%Y %H:%M")
    case_ref = f"#{case_id}" if case_id else ""

    report_html = _escape(report_text).replace("\n", "<br>")

    html_content = f"""<!DOCTYPE html>
<html lang="{language}" dir="{direction}">
<head>
<meta charset="utf-8">
<style>
  @page {{ size: A4; margin: 2cm; }}
  body {{ font-family: Inter, 'Noto Sans', system-ui, sans-serif; font-size: 11pt;
         line-height: 1.65; color: #1a1c1e; direction: {direction}; }}
  .header {{ border-bottom: 2px solid #006a69; padding-bottom: 12px; margin-bottom: 20px; }}
  .header h1 {{ font-size: 18pt; font-weight: 700; color: #006a69; margin: 0 0 4px; }}
  .header .meta {{ font-size: 9pt; color: #74777f; }}
  .header .meta span {{ margin-{("left" if direction == "ltr" else "right")}: 12px; }}
  .report {{ white-space: pre-wrap; font-size: 10.5pt; line-height: 1.7; }}
  .footer {{ margin-top: 32px; padding-top: 12px; border-top: 1px solid #dde1e6;
             font-size: 8pt; color: #74777f; }}
  .disclaimer {{ margin-top: 16px; padding: 10px 14px; background: #f8f9fa;
                 border-radius: 6px; font-size: 8.5pt; color: #44474e; line-height: 1.5; }}
</style>
</head>
<body>
  <div class="header">
    <h1>NoryaAI — {_escape(institution_name)}</h1>
    <div class="meta">
      <span>{date_str}</span>
      <span>{case_ref}</span>
      <span>{_escape(case_filename or "")}</span>
      <span>{language.upper()}</span>
    </div>
  </div>
  <div class="report">{report_html}</div>
  <div class="disclaimer">
    {_disclaimer(language)}
  </div>
  <div class="footer">
    NoryaAI Enterprise · {_escape(institution_name)} · {date_str}
  </div>
</body>
</html>"""

    pdf_bytes = HTML(string=html_content).write_pdf()
    return pdf_bytes


def _escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _disclaimer(lang: str) -> str:
    texts = {
        "tr": "Bu rapor yalnızca bilgilendirme amaçlıdır. Tıbbi teşhis veya tedavi yerine geçmez. Klinik kararlar için yetkili sağlık profesyoneline başvurunuz.",
        "en": "This report is for informational purposes only. It does not replace medical diagnosis or treatment. Consult a qualified healthcare professional for clinical decisions.",
        "de": "Dieser Bericht dient nur zu Informationszwecken. Er ersetzt keine medizinische Diagnose oder Behandlung. Wenden Sie sich für klinische Entscheidungen an einen qualifizierten Gesundheitsfachmann.",
        "es": "Este informe es solo para fines informativos. No reemplaza el diagnóstico o tratamiento médico. Consulte a un profesional de salud calificado para decisiones clínicas.",
        "fr": "Ce rapport est fourni à titre informatif uniquement. Il ne remplace pas un diagnostic ou un traitement médical. Consultez un professionnel de santé qualifié pour les décisions cliniques.",
        "it": "Questo rapporto è solo a scopo informativo. Non sostituisce la diagnosi o il trattamento medico. Consultare un professionista sanitario qualificato per decisioni cliniche.",
        "he": "דוח זה הוא למטרות מידע בלבד. הוא אינו מחליף אבחון או טיפול רפואי. פנו לאיש מקצוע רפואי מוסמך להחלטות קליניות.",
        "hi": "यह रिपोर्ट केवल सूचनात्मक उद्देश्यों के लिए है। यह चिकित्सा निदान या उपचार का विकल्प नहीं है। नैदानिक निर्णयों के लिए योग्य स्वास्थ्य पेशेवर से परामर्श करें।",
        "ar": "هذا التقرير لأغراض إعلامية فقط. لا يحل محل التشخيص أو العلاج الطبي. استشر أخصائي رعاية صحية مؤهل للقرارات السريرية.",
    }
    return texts.get(lang, texts["en"])
