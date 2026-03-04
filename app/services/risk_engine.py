"""
Risk Engine: Lab değerlerinden risk özeti hesaplar. OpenAI kullanmaz.
Çıktı: risk_summary JSON (overall, domains, highlights).
"""
from typing import Any

# Referans aralıkları (yaygın yetişkin değerleri; lab kendi ref'ini verirse o kullanılır)
REF_RANGES: dict[str, tuple[float | None, float | None]] = {
    "LDL": (None, 100),
    "HDL": (40, None),
    "Triglycerides": (None, 150),
    "Total cholesterol": (None, 200),
    "Glucose": (70, 100),
    "HbA1c": (None, 5.7),
    "CRP": (None, 3),
    "Homocysteine": (None, 15),
    "ALT": (None, 40),
    "AST": (None, 40),
    "GGT": (None, 60),
    "Creatinine": (None, 1.2),
    "eGFR": (90, None),
    "Vitamin D": (30, None),
    "B12": (200, None),
    "Folate": (3, None),
    "Ferritin": (30, None),
    "Iron": (60, None),
    "Hb": (12, 16),
    "TSH": (0.4, 4.0),
}

# Domain -> parametreler
DOMAIN_PARAMS: dict[str, tuple[str, ...]] = {
    "cardio": ("LDL", "HDL", "Triglycerides", "Total cholesterol", "Glucose", "HbA1c", "CRP", "Homocysteine"),
    "metabolic": ("Glucose", "HbA1c", "ALT", "AST", "GGT", "Creatinine", "eGFR"),
    "inflammation": ("CRP", "Homocysteine"),
    "vitamin": ("Vitamin D", "B12", "Folate", "Ferritin", "Iron", "Hb"),
}

# Parametre -> kısa flag (highlights.flags için)
PARAM_FLAGS: dict[str, str] = {
    "LDL": "LDL", "HDL": "HDL", "Triglycerides": "TG", "Total cholesterol": "CHOL",
    "Glucose": "GLU", "HbA1c": "HbA1c", "CRP": "CRP", "Homocysteine": "Hcy",
    "ALT": "ALT", "AST": "AST", "GGT": "GGT", "Creatinine": "Krea", "eGFR": "eGFR",
    "Vitamin D": "VITD", "B12": "B12", "Folate": "FOL", "Ferritin": "Ferritin", "Iron": "Fe", "Hb": "Hb",
}

# "low" -> 0-33, "mid" -> 34-66, "high" -> 67-100
LEVEL_SCORES: dict[str, int] = {"low": 18, "mid": 50, "high": 78}


def _get_ref(lab: dict[str, Any], param: str) -> tuple[float | None, float | None]:
    rl, rh = lab.get("ref_low"), lab.get("ref_high")
    if rl is not None or rh is not None:
        return (rl, rh)
    return REF_RANGES.get(param, (None, None))


def _status(value: float, ref_low: float | None, ref_high: float | None) -> str:
    if ref_low is not None and value < ref_low:
        return "low"
    if ref_high is not None and value > ref_high:
        return "high"
    return "normal"


def _domain_level_from_risks(risks: list[str]) -> str:
    if not risks:
        return "low"
    if "high" in risks:
        return "high"
    return "mid"


def _level_to_score(level: str) -> int:
    return LEVEL_SCORES.get(level, 50)


def _reason_text(param: str, status: str, lang: str = "tr") -> str:
    """Tek parametre için neden cümlesi (Türkçe)."""
    if status == "high":
        if param in ("LDL", "Triglycerides", "Total cholesterol", "Glucose", "HbA1c", "CRP", "Homocysteine", "ALT", "AST", "GGT", "Creatinine"):
            return f"{param} yüksek"
        return f"{param} yüksek"
    if status == "low":
        if param in ("HDL", "eGFR"):
            return f"{param} düşük"
        if param in ("Vitamin D", "B12", "Folate", "Ferritin", "Iron", "Hb"):
            return f"{param} düşük"
        return f"{param} düşük"
    return ""


def _action_hint(param: str, level: str, lang: str = "tr") -> str:
    if level == "high":
        if param in ("LDL", "Triglycerides", "Total cholesterol"):
            return "Beslenme/aktivite"
        if param in ("Vitamin D", "B12", "Folate", "Ferritin", "Iron", "Hb"):
            return "Doktorla görüş"
        if param in ("Glucose", "HbA1c"):
            return "Beslenme/diyet; doktor takibi"
        return "Doktorla görüş"
    if level == "mid":
        return "Beslenme/aktivite"
    return ""


def _why_text(status: str, lang: str = "tr") -> str:
    if status == "high":
        return "Referans üzeri"
    if status == "low":
        return "Düşük"
    return "Normal"


def compute_risk(lab_values: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Lab değerlerinden risk_summary üretir (kural tabanlı).
    Çıktı:
      overall: { level: "low"|"mid"|"high", score: 0-100 }
      domains: { cardio, metabolic, inflammation, vitamin }: { level, score, reasons[], flags[] }
      highlights: [ { test, level, why, action }, ... ]
    """
    by_name: dict[str, dict[str, Any]] = {}
    for lab in lab_values:
        name = lab.get("name")
        if not name:
            continue
        if name not in by_name:
            by_name[name] = lab

    def param_risk_level(status: str, param: str) -> str:
        if status == "normal":
            return "low"
        if status == "high":
            if param in ("HDL", "eGFR", "Vitamin D", "B12", "Folate", "Ferritin", "Iron", "Hb"):
                return "low"
            return "high"
        if param in ("LDL", "HDL", "Triglycerides", "Total cholesterol", "Glucose", "HbA1c",
                     "CRP", "Homocysteine", "ALT", "AST", "GGT", "Creatinine", "eGFR",
                     "Vitamin D", "B12", "Folate", "Ferritin", "Iron", "Hb", "TSH"):
            return "high"
        return "mid"

    domains_out: dict[str, Any] = {}
    all_highlights: list[dict[str, Any]] = []

    for domain_key, params in DOMAIN_PARAMS.items():
        reasons: list[str] = []
        flags: list[str] = []
        levels: list[str] = []
        for p in params:
            lab = by_name.get(p)
            if not lab:
                continue
            ref_low, ref_high = _get_ref(lab, p)
            st = _status(lab["value"], ref_low, ref_high)
            lev = param_risk_level(st, p)
            if lev != "low":
                levels.append(lev)
                reason = _reason_text(p, st)
                if reason:
                    reasons.append(reason)
                flags.append(PARAM_FLAGS.get(p, p))
                all_highlights.append({
                    "test": p,
                    "level": lev,
                    "why": _why_text(st),
                    "action": _action_hint(p, lev),
                })
        domain_level = _domain_level_from_risks(levels)
        domains_out[domain_key] = {
            "level": domain_level,
            "score": _level_to_score(domain_level),
            "reasons": reasons,
            "flags": flags,
        }

    # Ağırlıklı ortalama: cardio 0.35, metabolic 0.30, inflammation 0.15, vitamin 0.20
    weights = {"cardio": 0.35, "metabolic": 0.30, "inflammation": 0.15, "vitamin": 0.20}
    overall_score = 0.0
    for dk, w in weights.items():
        if dk in domains_out:
            overall_score += domains_out[dk]["score"] * w
    overall_score = max(0, min(100, round(overall_score)))
    # Level: 0-33 low, 34-66 mid, 67-100 high
    if overall_score <= 33:
        overall_level = "low"
    elif overall_score <= 66:
        overall_level = "mid"
    else:
        overall_level = "high"

    return {
        "overall": {"level": overall_level, "score": overall_score},
        "domains": domains_out,
        "highlights": all_highlights,
    }
