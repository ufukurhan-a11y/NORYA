"""
Ham tahlil metninden yapısal lab değerleri çıkarır.
Risk engine ve AI aşaması için kullanılır.
"""
import re
import logging
from typing import Any

logger = logging.getLogger(__name__)

# Parametre adı eşleştirmesi (Türkçe/İngilizce -> canonical)
PARAM_ALIASES: dict[str, str] = {
    "hb": "Hb", "hemoglobin": "Hb", "hemoglobine": "Hb",
    "glukoz": "Glucose", "glucose": "Glucose", "glikoz": "Glucose", "açlık glukoz": "Glucose",
    "hba1c": "HbA1c", "a1c": "HbA1c", "glycated": "HbA1c",
    "ldl": "LDL", "ldl kolesterol": "LDL",
    "hdl": "HDL", "hdl kolesterol": "HDL",
    "trigliserid": "Triglycerides", "triglycerides": "Triglycerides", "tg": "Triglycerides",
    "kolesterol": "Total cholesterol", "total cholesterol": "Total cholesterol", "cholesterol": "Total cholesterol",
    "alt": "ALT", "sgpt": "ALT", "alanine": "ALT",
    "ast": "AST", "sgot": "AST", "aspartate": "AST",
    "ggt": "GGT", "gama gt": "GGT", "gamma gt": "GGT",
    "kreatinin": "Creatinine", "creatinine": "Creatinine", "krea": "Creatinine",
    "egfr": "eGFR", "gfr": "eGFR",
    "crp": "CRP", "c-reactive": "CRP", "hs-crp": "CRP",
    "homosistein": "Homocysteine", "homocysteine": "Homocysteine",
    "vitamin d": "Vitamin D", "vit d": "Vitamin D", "d vitamini": "Vitamin D", "25-oh": "Vitamin D",
    "b12": "B12", "vitamin b12": "B12", "kobalamin": "B12", "cobalamin": "B12",
    "folat": "Folate", "folate": "Folate", "folik asit": "Folate", "folic": "Folate",
    "ferritin": "Ferritin", "serum ferritin": "Ferritin",
    "demir": "Iron", "iron": "Iron", "serum demir": "Iron", "serum iron": "Iron",
    "tsh": "TSH", "tiroid": "TSH",
    "wbc": "WBC", "lökosit": "WBC", "leukocyte": "WBC",
    "rbc": "RBC", "eritrosit": "RBC", "erythrocyte": "RBC",
    "plt": "Platelets", "trombosit": "Platelets", "platelets": "Platelets",
}


def _normalize_param_name(raw: str) -> str:
    """Ham parametre adını canonical forma getirir."""
    key = re.sub(r"\s+", " ", raw).strip().lower()
    key = re.sub(r"[^\w\s]", "", key)
    for alias, canonical in PARAM_ALIASES.items():
        if alias in key or key in alias:
            return canonical
    # Bilinmeyen: ilk kelime veya kısaltma (büyük harf)
    cleaned = raw.strip()
    if len(cleaned) <= 4 and cleaned.isalpha():
        return cleaned.upper()
    return cleaned[:40].strip()


def _extract_ref_range(s: str) -> tuple[float | None, float | None]:
    """Metinden ref aralığı çıkarır: 12-16, 12 – 16, (70-100), <100, >4."""
    s = s.replace(",", ".")
    # min-max
    m = re.search(r"(?:ref\.?|referans|reference|ref:)?\s*\(?\s*(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)", s, re.I)
    if m:
        return float(m.group(1)), float(m.group(2))
    # < max
    m = re.search(r"<\s*(\d+(?:\.\d+)?)", s, re.I)
    if m:
        return None, float(m.group(1))
    # > min
    m = re.search(r">\s*(\d+(?:\.\d+)?)", s, re.I)
    if m:
        return float(m.group(1)), None
    return None, None


def parse_lab_text(text: str) -> list[dict[str, Any]]:
    """
    Ham tahlil metninden lab değerleri listesi döner.
    Her öğe: {"name": str, "value": float, "unit": str | None, "ref_low": float | None, "ref_high": float | None}
    """
    if not text or not text.strip():
        return []
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, float]] = set()  # (name, value) tekrarları atla
    lines = re.split(r"[\n\r]+", text)
    # Sayı (ondalık, virgül/nokta); ardından opsiyonel unit ve ref
    value_ref_re = re.compile(
        r"([A-Za-z\u00C0-\u024F\u0400-\u04FF\s\-/]+?)\s*[:\.]?\s*(\d+(?:[.,]\d+)?)\s*([a-zA-Z/%]*)\s*(.*)",
        re.U,
    )
    simple_re = re.compile(r"([A-Za-z\u00C0-\u024F\u0400-\u04FF0-9\s\-/]+?)\s+(\d+(?:[.,]\d+)?)\s*([a-zA-Z/%]*)")
    for raw_line in lines:
        line = raw_line.strip()
        if not line or len(line) < 3:
            continue
        ref_low, ref_high = _extract_ref_range(line)
        m = value_ref_re.match(line)
        if m:
            name_part = m.group(1).strip()
            value_s = m.group(2).replace(",", ".")
            unit = (m.group(3) or "").strip() or None
            rest = (m.group(4) or "").strip()
            if not ref_low and not ref_high:
                rl, rh = _extract_ref_range(rest)
                if rl is not None or rh is not None:
                    ref_low, ref_high = rl, rh
        else:
            # Daha basit: "Parametre 14.2 g/dL"
            m2 = simple_re.search(line)
            if not m2:
                continue
            name_part = m2.group(1).strip()
            value_s = m2.group(2).replace(",", ".")
            unit = (m2.group(3) or "").strip() or None
        try:
            value = float(value_s)
        except ValueError:
            continue
        if not name_part or len(name_part) > 80:
            continue
        name = _normalize_param_name(name_part)
        if (name, value) in seen:
            continue
        seen.add((name, value))
        out.append({
            "name": name,
            "value": value,
            "unit": unit or None,
            "ref_low": ref_low,
            "ref_high": ref_high,
        })
    return out
