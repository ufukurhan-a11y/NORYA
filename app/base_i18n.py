# -*- coding: utf-8 -*-
"""Global UI strings for base template: navbar, footer, CTA. Single source for locale-aware text."""

from __future__ import annotations

from app.core.config import BRAND_NAME

BASE_UI_LANGS = ("en", "de", "fr", "it", "tr", "es", "he", "hi", "ar")
DEFAULT_BASE_LANG = "en"

BASE_UI = {
    "en": {
        "nav_how": "How it works",
        "nav_security": "Security",
        "nav_analyze": "Analyze",
        "nav_menu": "Menu",
        "nav_close": "Close",
        "footer_tagline": "NoryaAI is a multilingual AI-powered platform designed to help users understand blood test results more clearly.",
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
        "footer_tagline": "NoryaAI ist eine mehrsprachige KI-Plattform, die Blutwerte klarer verstaendlich macht.",
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
        "footer_tagline": "NoryaAI est une plateforme IA multilingue conçue pour expliquer les analyses sanguines de façon claire.",
        "footer_privacy": "Politique de confidentialité",
        "footer_terms": "Conditions d'utilisation",
        "footer_contact": "Contact",
        "cta_analyze": "Analyser",
        "title_suffix": "— Comprendre vos analyses sanguines",
        "home_link": BRAND_NAME,
    },
    "it": {
        "nav_how": "Come funziona",
        "nav_security": "Sicurezza",
        "nav_analyze": "Analizza",
        "nav_menu": "Menu",
        "nav_close": "Chiudi",
        "footer_tagline": "NoryaAI e una piattaforma IA multilingue pensata per spiegare gli esami del sangue in modo piu chiaro.",
        "footer_privacy": "Privacy",
        "footer_terms": "Termini d'uso",
        "footer_contact": "Contatti",
        "cta_analyze": "Analizza",
        "title_suffix": "— Capire le analisi del sangue",
        "home_link": BRAND_NAME,
    },
    "tr": {
        "nav_how": "Nasıl Çalışır",
        "nav_security": "Güvenlik",
        "nav_analyze": "Analiz Yap",
        "nav_menu": "Menü",
        "nav_close": "Kapat",
        "footer_tagline": "NoryaAI, kan tahlili sonuclarini daha net anlamaniz icin tasarlanmis cok dilli bir AI platformudur.",
        "footer_privacy": "Gizlilik Politikası",
        "footer_terms": "Kullanım Şartları",
        "footer_contact": "İletişim",
        "cta_analyze": "Analiz Yap",
        "title_suffix": "— Kan tahlili sonuçlarını anlaşılır kılan analiz",
        "home_link": BRAND_NAME,
    },
    "es": {
        "nav_how": "Cómo funciona",
        "nav_security": "Seguridad",
        "nav_analyze": "Analizar",
        "nav_menu": "Menú",
        "nav_close": "Cerrar",
        "footer_tagline": "NoryaAI es una plataforma multilingue con IA disenada para explicar analisis de sangre con mas claridad.",
        "footer_privacy": "Política de privacidad",
        "footer_terms": "Términos de uso",
        "footer_contact": "Contacto",
        "cta_analyze": "Analizar",
        "title_suffix": "— Análisis de resultados de sangre en lenguaje claro",
        "home_link": BRAND_NAME,
    },
    "he": {
        "nav_how": "איך זה עובד",
        "nav_security": "אבטחה",
        "nav_analyze": "נתחו",
        "nav_menu": "תפריט",
        "nav_close": "סגור",
        "footer_tagline": "NoryaAI היא פלטפורמת AI רב-לשונית שנועדה לעזור להבין תוצאות בדיקות דם בצורה ברורה יותר.",
        "footer_privacy": "מדיניות פרטיות",
        "footer_terms": "תנאי שימוש",
        "footer_contact": "יצירת קשר",
        "cta_analyze": "נתחו",
        "title_suffix": "— ניתוח ברור של בדיקות דם",
        "home_link": BRAND_NAME,
    },
    "hi": {
        "nav_how": "Kaise kaam karta hai",
        "nav_security": "Suraksha",
        "nav_analyze": "Analyze karein",
        "nav_menu": "Menu",
        "nav_close": "Band karein",
        "footer_tagline": "NoryaAI ek multilingual AI platform hai jo blood test results ko aur zyada clearly samajhne mein madad karta hai.",
        "footer_privacy": "Privacy Policy",
        "footer_terms": "Terms of Use",
        "footer_contact": "Contact",
        "cta_analyze": "Analyze karein",
        "title_suffix": "— AI blood test analysis",
        "home_link": BRAND_NAME,
    },
    "ar": {
        "nav_how": "كيف يعمل",
        "nav_security": "الامان",
        "nav_analyze": "ابدأ التحليل",
        "nav_menu": "القائمة",
        "nav_close": "اغلاق",
        "footer_tagline": "NoryaAI منصة ذكاء اصطناعي متعددة اللغات تساعد المستخدمين على فهم نتائج فحوصات الدم بوضوح اكبر.",
        "footer_privacy": "سياسة الخصوصية",
        "footer_terms": "شروط الاستخدام",
        "footer_contact": "اتصل بنا",
        "cta_analyze": "ابدأ التحليل",
        "title_suffix": "— تحليل واضح لفحوصات الدم",
        "home_link": BRAND_NAME,
    },
}


def get_base_ui(lang: str | None) -> dict:
    """Return BASE_UI for the given locale. Fallback: en (never TR for /en routes)."""
    if not lang:
        return BASE_UI[DEFAULT_BASE_LANG]
    lang = (lang or "").lower()[:2]
    return BASE_UI.get(lang, BASE_UI[DEFAULT_BASE_LANG])
