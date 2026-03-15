# -*- coding: utf-8 -*-
"""
Merkezi paket/plan konfigürasyonu: single, monthly, yearly.
Sonuç akışında paket tipine göre feature gating (modül görünürlüğü, açıklama derinliği, PDF, karşılaştırma, trend).
Bu aşamada sadece altyapı; UI değişikliği yapılmaz.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

# Ürün seviyeleri (pricing ile uyumlu)
PlanType = Literal["single", "monthly", "yearly"]

# Modül anahtarları (sonuç ekranı/PDF'de hangi bölümlerin gösterileceği)
MODULE_SUMMARY = "summary"
MODULE_BIOMARKERS = "biomarkers"
MODULE_RISK_INDICATORS = "risk_indicators"
MODULE_RECOMMENDATIONS = "recommendations"
MODULE_COMPARISON = "comparison"
MODULE_TREND = "trend"
MODULE_FOLLOW_UP = "follow_up"
# PDF seviyesi (hangi şablon/derinlik)
MODULE_PDF_BASIC = "pdf_basic"
MODULE_PDF_PREMIUM = "pdf_premium"

VISIBLE_MODULES_SINGLE = (
    MODULE_SUMMARY,
    MODULE_BIOMARKERS,
    MODULE_RISK_INDICATORS,
    MODULE_RECOMMENDATIONS,
    MODULE_PDF_BASIC,
)
VISIBLE_MODULES_MONTHLY = (
    *VISIBLE_MODULES_SINGLE,
    MODULE_COMPARISON,
    MODULE_PDF_PREMIUM,
)
VISIBLE_MODULES_YEARLY = (
    *VISIBLE_MODULES_MONTHLY,
    MODULE_TREND,
    MODULE_FOLLOW_UP,
)


@dataclass(frozen=True)
class PlanConfig:
    """Tek bir plan için özellik konfigürasyonu."""

    plan_name: str
    visible_modules: tuple[str, ...]
    explanation_depth: Literal["basic", "extended", "full"]
    pdf_depth: Literal["basic", "premium"]
    comparison_enabled: bool
    trend_enabled: bool

    def has_module(self, module: str) -> bool:
        return module in self.visible_modules


# Tablo: plan kodu → PlanConfig (tek kaynak)
PLAN_CONFIG_TABLE: dict[str, PlanConfig] = {
    "single": PlanConfig(
        plan_name="single",
        visible_modules=VISIBLE_MODULES_SINGLE,
        explanation_depth="basic",
        pdf_depth="basic",
        comparison_enabled=False,
        trend_enabled=False,
    ),
    "monthly": PlanConfig(
        plan_name="monthly",
        visible_modules=VISIBLE_MODULES_MONTHLY,
        explanation_depth="extended",
        pdf_depth="premium",
        comparison_enabled=True,
        trend_enabled=False,
    ),
    "yearly": PlanConfig(
        plan_name="yearly",
        visible_modules=VISIBLE_MODULES_YEARLY,
        explanation_depth="full",
        pdf_depth="premium",
        comparison_enabled=True,
        trend_enabled=True,
    ),
    # Pro (eski/mevcut): yıllık ile aynı özellikler
    "pro": PlanConfig(
        plan_name="yearly",
        visible_modules=VISIBLE_MODULES_YEARLY,
        explanation_depth="full",
        pdf_depth="premium",
        comparison_enabled=True,
        trend_enabled=True,
    ),
}


def normalize_plan_type(plan: str | None) -> PlanType:
    """
    Kullanıcı planını (user.plan) saklanacak/akışta kullanılacak plan tipine çevirir.
    Backward compatibility: free → single, pro → yearly, bilinmeyen → single.
    """
    if not plan or not (p := (plan or "").strip().lower()):
        return "single"
    if p in ("single", "monthly", "yearly"):
        return p  # type: ignore[return-value]
    if p == "pro":
        return "yearly"
    # free veya bilinmeyen
    return "single"


def get_plan_config(plan: str | None) -> PlanConfig:
    """
    Plan adına göre PlanConfig döner.
    Bilinmeyen/free için single config (güvenli varsayılan).
    """
    p = (plan or "").strip().lower()
    if p in PLAN_CONFIG_TABLE:
        return PLAN_CONFIG_TABLE[p]
    return PLAN_CONFIG_TABLE["single"]


def plan_allows(plan: str | None, feature: str) -> bool:
    """
    Bu plan için verilen özelliğin açık olup olmadığını döner.
    feature: "comparison_enabled" | "trend_enabled" | "module:<name>" (örn. "module:trend")
    """
    cfg = get_plan_config(plan)
    if feature == "comparison_enabled":
        return cfg.comparison_enabled
    if feature == "trend_enabled":
        return cfg.trend_enabled
    if feature.startswith("module:"):
        return cfg.has_module(feature[7:].strip())
    return False


def plan_pdf_premium(plan: str | None) -> bool:
    """Plan premium PDF şablonu kullanacak mı (mevcut davranışla uyumlu)."""
    cfg = get_plan_config(plan)
    return cfg.pdf_depth == "premium"


def plan_has_trend(plan: str | None) -> bool:
    """Plan trend verisi gösteriyor mu (monthly/yearly/pro)."""
    return plan_allows(plan, "trend_enabled")
