"""
Premium tıbbi PDF raporu: result_text (AI çıktısı) → parse → Jinja2 → WeasyPrint → PDF bytes.
"""
import re
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from app.charts import range_bar_svg_base64

# Şablon dizini: app/templates (package içinden çalışırken app/templates)
_TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
_ENV = Environment(loader=FileSystemLoader(str(_TEMPLATES_DIR)), autoescape=True)


# Bölüm başlıkları (Türkçe / İngilizce / yaygın varyantlar)
SECTION_PATTERNS = [
    (r"\*\*Summary\*\*", "summary"),
    (r"\*\*Özet\*\*", "summary"),
    (r"\*\*Risk indicators?\*\*", "risk_indicators"),
    (r"\*\*Dikkat edilmesi gerekenler\*\*", "risk_indicators"),
    (r"\*\*Values?\*\*", "values"),
    (r"\*\*Değerler\*\*", "values"),
    (r"\*\*Parametreler\*\*", "values"),
    (r"\*\*Possible causes?\*\*", "possible_causes"),
    (r"\*\*Olası nedenler\*\*", "possible_causes"),
    (r"\*\*Recommendations?\*\*", "recommendations"),
    (r"\*\*Öneriler\*\*", "recommendations"),
]

# Values bloğundaki satır: **Parametre adı:** değer birim. Reference: ... Normal/Low/High (sonunda nokta olabilir)
# Not: Markdown bazen **name*:** veya **name**: şeklinde olabiliyor; *? ile kabul ediyoruz.
BIOMARKER_LINE = re.compile(
    r"\*\*([^*]+)\*?\s*:\s*([^\n]+?)\s*\.\s*"
    r"(?:Reference:\s*([^\n]+?)\s*\.\s*)?"
    r"(Normal|Low|High|Borderline|Düşük|Yüksek|Sınırda|Sınır)\s*\.?\s*$",
    re.IGNORECASE,
)


def _is_section_header(line: str) -> bool:
    """Satır sadece bölüm başlığı mı (Summary, Risk, Values, ...) kontrol et."""
    if not line or not line.strip().startswith("**"):
        return False
    # İçerik kısmı (**: sonrası) boş veya çok kısa ise bölüm başlığıdır
    stripped = line.strip()
    match = re.match(r"^\*\*([^*]+)\*\*\s*:?\s*(.*)$", stripped)
    if not match:
        return False
    title, rest = match.group(1).strip(), (match.group(2) or "").strip()
    # Bilinen bölüm başlıkları (veya benzeri)
    known = (
        "summary", "özet", "risk indicators", "risk indicator", "dikkat edilmesi gerekenler",
        "values", "value", "değerler", "parametreler", "possible causes", "possible cause",
        "olası nedenler", "recommendations", "recommendation", "öneriler", "recommendations",
    )
    if title.lower() in known:
        return True
    if any(k in title.lower() for k in ("summary", "özet", "risk", "dikkat", "value", "değer", "parametre", "cause", "neden", "recommendation", "öneri")):
        return len(rest) < 80  # Uzun devamı varsa muhtemelen parametre satırı değil başlık
    return False


def _split_sections(text: str) -> list[tuple[str, str]]:
    """Metni **Bölüm başlığı** bloklarına göre böl; (başlık, içerik) listesi döndür."""
    if not (text or text.strip()):
        return []
    lines = text.split("\n")
    result: list[tuple[str, str]] = []
    current_title: str | None = None
    current_body: list[str] = []
    for line in lines:
        if _is_section_header(line):
            if current_title is not None:
                result.append((current_title, "\n".join(current_body).strip()))
            match = re.match(r"^\s*\*\*([^*]+)\*\*\s*:?\s*(.*)$", line.strip())
            if match:
                current_title = match.group(1).strip()
                rest = (match.group(2) or "").strip()
                current_body = [rest] if rest else []
            else:
                current_title = re.sub(r"^\*\*|\*\*\s*:?\s*$", "", line.strip()).strip()
                current_body = []
        else:
            if current_title is not None:
                current_body.append(line)
    if current_title is not None:
        result.append((current_title, "\n".join(current_body).strip()))
    return result


def _map_section_key(title: str) -> str | None:
    """Bölüm başlığını summary/risk_indicators/values/possible_causes/recommendations ile eşle."""
    title_lower = title.strip().lower()
    for pattern, key in SECTION_PATTERNS:
        if re.search(pattern, title, re.IGNORECASE):
            return key
    if "summary" in title_lower or "özet" in title_lower:
        return "summary"
    if "risk" in title_lower or "dikkat" in title_lower:
        return "risk_indicators"
    if "value" in title_lower or "değer" in title_lower or "parametre" in title_lower:
        return "values"
    if "cause" in title_lower or "neden" in title_lower:
        return "possible_causes"
    if "recommendation" in title_lower or "öneri" in title_lower:
        return "recommendations"
    return None


def _normalize_status(s: str) -> str:
    """Normal/Low/High/Borderline → normal, low, high, border."""
    if not s:
        return "normal"
    s = s.strip().lower()
    if s in ("normal", "normale"):
        return "normal"
    if s in ("low", "düşük", "basso", "baja"):
        return "low"
    if s in ("high", "yüksek", "alto", "alta"):
        return "high"
    if "border" in s or "sınır" in s:
        return "border"
    return "normal"


def _status_label(status: str) -> str:
    tr = {"normal": "Normal", "low": "Düşük", "high": "Yüksek", "border": "Sınırda"}
    return tr.get(status, status)


def _split_value_unit(raw: str) -> tuple[str, str | None]:
    """Örn. '14.2 g/dL' -> ('14.2', 'g/dL'); '120' -> ('120', None)."""
    raw = (raw or "").strip()
    if not raw:
        return ("—", None)
    parts = raw.split(None, 1)
    value = parts[0] if parts else "—"
    unit = parts[1] if len(parts) > 1 else None
    return (value, unit)


# Referans metninden min-max sayıları: "12-16 g/dL", "0.27-4.2 mIU/L" -> (12, 16) veya (0.27, 4.2)
_REF_NUMBERS = re.compile(r"(\d+(?:[.,]\d+)?)")


def _parse_reference_range(reference: str | None) -> tuple[float, float] | None:
    """Referans aralığı string'inden (ref_min, ref_max) döndürür."""
    if not reference or not reference.strip():
        return None
    numbers = _REF_NUMBERS.findall(reference.strip().replace(",", "."))
    if len(numbers) < 2:
        return None
    try:
        low = float(numbers[0])
        high = float(numbers[1])
        if low > high:
            low, high = high, low
        return (low, high)
    except ValueError:
        return None


def _value_to_float(value_str: str) -> float | None:
    """Gösterim değerini sayıya çevirir: '14.2', '<5', '>20' -> float veya None."""
    if not value_str or value_str == "—":
        return None
    s = (value_str.strip().replace(",", ".").replace(" ", "")
         .lstrip("<>≤≥"))
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _enrich_biomarker_chart(row: dict) -> None:
    """Biomarker satırına chart_svg_base64, display_min, display_max ekler (referans ve değer parse edilebiliyorsa)."""
    ref = _parse_reference_range(row.get("reference"))
    value_float = _value_to_float(row.get("value") or "")
    if ref is None or value_float is None:
        row["chart_svg_base64"] = None
        row["display_min"] = None
        row["display_max"] = None
        return
    ref_min, ref_max = ref
    if ref_max <= ref_min:
        row["chart_svg_base64"] = None
        row["display_min"] = None
        row["display_max"] = None
        return
    span = ref_max - ref_min
    padding = max(span * 0.3, span * 0.1) if span > 0 else 1.0
    display_min = min(ref_min, value_float) - padding
    display_max = max(ref_max, value_float) + padding
    b64 = range_bar_svg_base64(
        name=row["name"],
        value=value_float,
        unit=row.get("unit") or "",
        ref_min=ref_min,
        ref_max=ref_max,
        status=row.get("status") or "normal",
        display_min=display_min,
        display_max=display_max,
    )
    row["chart_svg_base64"] = b64
    row["display_min"] = display_min
    row["display_max"] = display_max


def parse_biomarkers(values_block: str) -> list[dict]:
    """Values bölümünden parametre satırlarını parse et."""
    rows: list[dict] = []
    for line in (values_block or "").splitlines():
        line = line.strip()
        if not line or not line.startswith("**"):
            continue
        m = BIOMARKER_LINE.search(line)
        if m:
            name = m.group(1).strip()
            value_str = (m.group(2) or "").strip()
            # AI bazen değeri **value** bold yazar; baştaki ** ve boşluğu kaldır
            if value_str.startswith("**"):
                value_str = value_str.lstrip("*").strip()
            reference = (m.group(3) or "").strip() or None
            status = _normalize_status(m.group(4) or "")
            value, unit = _split_value_unit(value_str)
            rows.append({
                "name": name,
                "value": value,
                "unit": unit,
                "reference": reference,
                "status": status,
                "status_label": _status_label(status),
            })
        else:
            simple = re.match(r"\*\*([^*]+)\*\*\s*:\s*(.+)", line)
            if simple:
                value, unit = _split_value_unit(simple.group(2))
                rows.append({
                    "name": simple.group(1).strip(),
                    "value": value,
                    "unit": unit,
                    "reference": None,
                    "status": "normal",
                    "status_label": "—",
                })
    return rows


def parse_report_to_context(
    result_text: str,
    report_date: str | None = None,
    lang: str = "tr",
) -> dict:
    """
    AI result_text'i bölümlere ayırıp PDF şablonu için context sözlüğü üretir.
    """
    report_date = report_date or datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M")
    sections_list = _split_sections(result_text or "")
    data: dict = {
        "summary": "",
        "risk_indicators": "",
        "values": "",
        "possible_causes": "",
        "recommendations": "",
        "raw_sections": [],
    }
    for title, body in sections_list:
        key = _map_section_key(title)
        if key and key in data and isinstance(data[key], str):
            data[key] = body
        elif key is None:
            data["raw_sections"].append({"title": title, "body": body})

    biomarkers = parse_biomarkers(data["values"])
    for row in biomarkers:
        _enrich_biomarker_chart(row)
    risk_level = "none"
    risk_message = ""
    if data["risk_indicators"]:
        risk_message = data["risk_indicators"].strip()
        risk_lower = risk_message.lower()
        if any(
            x in risk_lower
            for x in ("yüksek risk", "acil", "doktora", "hemen", "high risk", "urgent")
        ):
            risk_level = "high"
        elif any(
            x in risk_lower
            for x in ("dikkat", "attention", "sınır", "borderline", "kontrol")
        ) or any(b.get("status") in ("low", "high", "border") for b in biomarkers):
            risk_level = "attention"
        else:
            risk_level = "normal"

    if not risk_message and biomarkers:
        has_abnormal = any(b.get("status") in ("low", "high", "border") for b in biomarkers)
        risk_message = (
            "Bazı parametreler referans dışında. Öneriler bölümünü okuyun."
            if has_abnormal
            else "Tüm değerler referans aralığında."
        )

    return {
        "title": "Norya Analiz Raporu",
        "lang": lang,
        "report_date": report_date,
        "summary": data["summary"],
        "risk_level": risk_level,
        "risk_message": risk_message,
        "biomarkers": biomarkers,
        "possible_causes": data["possible_causes"],
        "recommendations": data["recommendations"],
        "raw_sections": data["raw_sections"],
    }


def render_pdf(context: dict) -> bytes:
    """Jinja2 şablonunu render edip WeasyPrint ile PDF üretir (lazy import: WeasyPrint sistem kütüphaneleri sunucu başlarken gerekmez)."""
    from weasyprint import HTML
    template = _ENV.get_template("report_pdf.html")
    html_str = template.render(**context)
    html_doc = HTML(string=html_str, base_url=str(_TEMPLATES_DIR))
    pdf_bytes = html_doc.write_pdf()
    return pdf_bytes


def build_report_pdf(
    result_text: str,
    report_date: str | None = None,
    lang: str = "tr",
) -> bytes:
    """result_text'ten premium PDF raporu üretir."""
    context = parse_report_to_context(result_text, report_date=report_date, lang=lang)
    return render_pdf(context)
