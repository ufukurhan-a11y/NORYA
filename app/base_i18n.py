# -*- coding: utf-8 -*-
"""Global UI strings for base template: navbar, footer, CTA. Single source for locale-aware text."""

from __future__ import annotations

from app.core.config import BRAND_NAME

BASE_UI_LANGS = ("en", "de", "fr", "it", "tr")
DEFAULT_BASE_LANG = "en"

BASE_UI = {
    "en": {
        "nav_how": "How it works",
        "nav_security": "Security",
        "nav_analyze": "Analyze",
        "nav_menu": "Menu",
        "nav_close": "Close",
        "footer_tagline": "Lab results explained in plain language. Not a substitute for medical advice.",
        "footer_privacy": "Privacy Policy",
        "footer_terms": "Terms of Use",
        "footer_contact": "Contact",
        "cta_analyze": "Analyze",
        "title_suffix": "— Reliable AI blood test analysis",
        "home_link": BRAND_NAME,
    },
    "de": {
        "nav_how": "So funktioniert's",
        "nav_security": "Sicherheit",
        "nav_analyze": "Analysieren",
        "nav_menu": "Menü",
        "nav_close": "Schließen",
        "footer_tagline": "Laborergebnisse verständlich erklärt. Kein Ersatz für medizinischen Rat.",
        "footer_privacy": "Datenschutz",
        "footer_terms": "Nutzungsbedingungen",
        "footer_contact": "Kontakt",
        "cta_analyze": "Analysieren",
        "title_suffix": "— Zuverlässige KI-Blutanalyse",
        "home_link": BRAND_NAME,
    },
    "fr": {
        "nav_how": "Comment ça marche",
        "nav_security": "Sécurité",
        "nav_analyze": "Analyser",
        "nav_menu": "Menu",
        "nav_close": "Fermer",
        "footer_tagline": "Résultats d'analyses expliqués simplement. Ne remplace pas un avis médical.",
        "footer_privacy": "Politique de confidentialité",
        "footer_terms": "Conditions d'utilisation",
        "footer_contact": "Contact",
        "cta_analyze": "Analyser",
        "title_suffix": "— Analyse sanguine par IA fiable",
        "home_link": BRAND_NAME,
    },
    "it": {
        "nav_how": "Come funziona",
        "nav_security": "Sicurezza",
        "nav_analyze": "Analizza",
        "nav_menu": "Menu",
        "nav_close": "Chiudi",
        "footer_tagline": "Risultati di laboratorio in linguaggio chiaro. Non sostituiscono il parere medico.",
        "footer_privacy": "Privacy",
        "footer_terms": "Termini d'uso",
        "footer_contact": "Contatti",
        "cta_analyze": "Analizza",
        "title_suffix": "— Analisi del sangue con IA affidabile",
        "home_link": BRAND_NAME,
    },
    "tr": {
        "nav_how": "Nasıl Çalışır",
        "nav_security": "Güvenlik",
        "nav_analyze": "Analiz Yap",
        "nav_menu": "Menü",
        "nav_close": "Kapat",
        "footer_tagline": "Laboratuvar sonuçlarınızı anlaşılır dilde açıklayan bilgilendirme hizmeti. Teşhis yerine geçmez.",
        "footer_privacy": "Gizlilik Politikası",
        "footer_terms": "Kullanım Şartları",
        "footer_contact": "İletişim",
        "cta_analyze": "Analiz Yap",
        "title_suffix": "— Güvenilir Yapay Zeka Kan Tahlili Analizi",
        "home_link": BRAND_NAME,
    },
}


def get_base_ui(lang: str | None) -> dict:
    """Return BASE_UI for the given locale. Fallback: en (never TR for /en routes)."""
    if not lang:
        return BASE_UI[DEFAULT_BASE_LANG]
    lang = (lang or "").lower()[:2]
    return BASE_UI.get(lang, BASE_UI[DEFAULT_BASE_LANG])
