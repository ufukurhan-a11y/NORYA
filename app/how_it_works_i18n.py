# -*- coding: utf-8 -*-
"""How it works page i18n. Supports DE, EN, TR for /how-it-works. Used in Google Ads site links."""

from __future__ import annotations

HOW_IT_WORKS_LANGS = ("de", "en", "tr")
DEFAULT_HOW_IT_WORKS_LANG = "en"


def _de() -> dict:
    return {
        "meta_title": "So funktioniert Norya — Blutwerte verstehen in 3 Schritten",
        "meta_description": "Laborergebnisse hochladen, verständlichen Bericht erhalten. Keine Diagnose — nur Aufklärung. DSGVO-konform, in 9 Sprachen.",
        "nav_home": "Startseite",
        "nav_how": "So funktioniert's",
        "nav_pricing": "Preise",
        "nav_analyze": "Analyse starten",
        "hero_title": "So funktioniert Norya",
        "hero_sub": "Ihre Laborwerte in wenigen Minuten verständlich aufbereitet. Keine Diagnose — klare, bildungsorientierte Erklärungen für Ihre nächste Arztbesprechung.",
        "cta_primary": "Analyse starten",
        "cta_secondary": "Preise ansehen",
        "section_how_title": "So funktioniert's — 3 Schritte",
        "step1_title": "Konto erstellen",
        "step1_desc": "Kostenlos registrieren. Keine Kreditkarte für den Einstieg nötig.",
        "step2_title": "Ergebnisse hochladen oder Werte eingeben",
        "step2_desc": "PDF, Foto oder Text Ihrer Laborergebnisse — Norya erkennt die Werte und Referenzbereiche.",
        "step3_title": "Bericht mit Erklärungen erhalten",
        "step3_desc": "Strukturierter Bericht mit Referenzbereichen, verständlichen Erklärungen und Hinweisen. Ideal zur Vorbereitung auf das Arztgespräch.",
        "section_report_title": "Was Sie im Norya-Bericht sehen",
        "report_ref": "Referenzbereiche zu jedem Wert (Normal / niedrig / hoch).",
        "report_plain": "Verständliche Erklärungen in einfacher Sprache.",
        "report_highlights": "Wichtige Punkte und Empfehlungen auf einen Blick.",
        "report_doctor_prep": "Vorbereitung für das Arztgespräch — Sie kommen mit besseren Fragen.",
        "section_trust_title": "Sicherheit und Transparenz",
        "trust_dsgvo": "DSGVO- und KVKK-konform. Daten verschlüsselt, nicht an Dritte verkauft. Sichere Zahlung (z. B. PayTR), SSL.",
        "trust_disclaimer": "Norya stellt keine Diagnose. Alle Inhalte dienen ausschließlich der Information und Bildung. Bei Beschwerden oder Behandlungsentscheidungen bitte immer einen Arzt konsultieren.",
        "section_who_title": "Für wen ist Norya geeignet?",
        "who_1": "Sie möchten Ihre Laborergebnisse selbst besser verstehen.",
        "who_2": "Sie wollen sich vor dem Arzttermin vorbereiten und gezieltere Fragen stellen.",
        "who_3": "Sie benötigen Ihren Bericht in einer anderen Sprache (z. B. Deutsch, Englisch, Türkisch).",
        "section_cta_title": "Bereit für Ihren ersten Bericht?",
        "cta_primary2": "Analyse starten",
        "cta_secondary2": "Preise ansehen",
        "footer_legal": "Rechtliches",
        "footer_privacy": "Datenschutz",
        "footer_terms": "Nutzungsbedingungen",
    }


def _en() -> dict:
    return {
        "meta_title": "How Norya Works — Understand Your Lab Results in 3 Steps",
        "meta_description": "Upload lab results, get a clear report. Not a diagnosis — educational explanations only. GDPR compliant, 9 languages.",
        "nav_home": "Home",
        "nav_how": "How it works",
        "nav_pricing": "Pricing",
        "nav_analyze": "Start analysis",
        "hero_title": "How Norya Works",
        "hero_sub": "Your lab results explained in minutes. No diagnosis — clear, educational summaries to help you prepare for your doctor visit.",
        "cta_primary": "Start analysis",
        "cta_secondary": "View pricing",
        "section_how_title": "How it works — 3 steps",
        "step1_title": "Create an account",
        "step1_desc": "Free sign-up. No credit card required to get started.",
        "step2_title": "Upload results or enter values",
        "step2_desc": "PDF, photo, or paste text of your lab results — Norya reads values and reference ranges.",
        "step3_title": "Get your explained report",
        "step3_desc": "Structured report with reference ranges, plain-language explanations, and highlights. Ideal to prepare for your doctor appointment.",
        "section_report_title": "What you see in your Norya report",
        "report_ref": "Reference ranges for each value (normal / low / high).",
        "report_plain": "Plain-language explanations you can understand.",
        "report_highlights": "Key takeaways and recommendations at a glance.",
        "report_doctor_prep": "Preparation for your doctor visit — come with better questions.",
        "section_trust_title": "Security and transparency",
        "trust_dsgvo": "GDPR and KVKK compliant. Data encrypted, not sold to third parties. Secure payment (e.g. PayTR), SSL.",
        "trust_disclaimer": "Norya does not provide a diagnosis. All content is for information and education only. Always consult a doctor for symptoms or treatment decisions.",
        "section_who_title": "Who is Norya for?",
        "who_1": "You want to understand your own lab results better.",
        "who_2": "You want to prepare before your doctor appointment and ask better questions.",
        "who_3": "You need your report in another language (e.g. English, German, Turkish).",
        "section_cta_title": "Ready for your first report?",
        "cta_primary2": "Start analysis",
        "cta_secondary2": "View pricing",
        "footer_legal": "Legal",
        "footer_privacy": "Privacy",
        "footer_terms": "Terms of use",
    }


def _tr() -> dict:
    return {
        "meta_title": "Norya Nasıl Çalışır — 3 Adımda Laboratuvar Sonuçlarınızı Anlayın",
        "meta_description": "Laboratuvar sonuçlarınızı yükleyin, anlaşılır rapor alın. Teşhis değil — yalnızca bilgilendirme. KVKK uyumlu, 9 dil.",
        "nav_home": "Ana Sayfa",
        "nav_how": "Nasıl Çalışır",
        "nav_pricing": "Fiyatlandırma",
        "nav_analyze": "Analizi Başlat",
        "hero_title": "Norya Nasıl Çalışır",
        "hero_sub": "Laboratuvar sonuçlarınız dakikalar içinde anlaşılır hale gelir. Teşhis koymuyoruz — hekim görüşmenize hazırlanmanız için net, eğitim amaçlı özetler sunuyoruz.",
        "cta_primary": "Analizi Başlat",
        "cta_secondary": "Fiyatları Gör",
        "section_how_title": "Nasıl çalışır — 3 adım",
        "step1_title": "Hesap oluşturun",
        "step1_desc": "Ücretsiz kayıt. Başlamak için kredi kartı gerekmez.",
        "step2_title": "Sonuçları yükleyin veya değerleri girin",
        "step2_desc": "Laboratuvar sonuçlarınızın PDF’i, fotoğrafı veya metnini yapıştırın — Norya değerleri ve referans aralıklarını okur.",
        "step3_title": "Açıklamalı raporunuzu alın",
        "step3_desc": "Referans aralıkları, sade açıklamalar ve önemli noktalarla yapılandırılmış rapor. Hekim randevunuza hazırlanmak için ideal.",
        "section_report_title": "Norya raporunda neler görürsünüz?",
        "report_ref": "Her değer için referans aralıkları (normal / düşük / yüksek).",
        "report_plain": "Anlaşılır, sade dilde açıklamalar.",
        "report_highlights": "Önemli çıkarımlar ve öneriler tek bakışta.",
        "report_doctor_prep": "Hekim görüşmesine hazırlık — daha iyi sorularla gidin.",
        "section_trust_title": "Güvenlik ve şeffaflık",
        "trust_dsgvo": "KVKK ve GDPR uyumlu. Veriler şifreli, üçüncü taraflara satılmaz. Güvenli ödeme (PayTR), SSL.",
        "trust_disclaimer": "Norya teşhis koymaz. Tüm içerik yalnızca bilgilendirme ve eğitim amaçlıdır. Belirti veya tedavi kararları için mutlaka bir hekime danışın.",
        "section_who_title": "Norya kimler için uygun?",
        "who_1": "Kendi laboratuvar sonuçlarınızı daha iyi anlamak istiyorsanız.",
        "who_2": "Hekim randevusu öncesi hazırlanıp daha iyi sorular sormak istiyorsanız.",
        "who_3": "Raporunuzu farklı bir dilde (Türkçe, İngilizce, Almanca vb.) istiyorsanız.",
        "section_cta_title": "İlk raporunuz için hazır mısınız?",
        "cta_primary2": "Analizi Başlat",
        "cta_secondary2": "Fiyatları Gör",
        "footer_legal": "Yasal",
        "footer_privacy": "Gizlilik",
        "footer_terms": "Kullanım Koşulları",
    }


_HOW_IT_WORKS_UI = {
    "de": _de(),
    "en": _en(),
    "tr": _tr(),
}


def get_how_it_works_ui(lang: str) -> dict:
    """Return UI strings for the How it works page. Fallback: en."""
    lang = (lang or "").strip().lower()[:2]
    if lang not in _HOW_IT_WORKS_UI:
        lang = DEFAULT_HOW_IT_WORKS_LANG
    return dict(_HOW_IT_WORKS_UI[lang])


def get_how_it_works_meta(lang: str) -> dict:
    """Return meta_title, meta_description for SEO/OG. Uses get_how_it_works_ui."""
    ui = get_how_it_works_ui(lang)
    return {
        "meta_title": ui.get("meta_title", "How it works — Norya"),
        "meta_description": ui.get("meta_description", ""),
    }
