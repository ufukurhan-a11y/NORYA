# -*- coding: utf-8 -*-
"""Country-based landing page i18n. Routes: /tr, /en, /en-ca, /de, /it. Header, hero, CTA, FAQ, pricing from locale."""

from __future__ import annotations

LANDING_ROUTES = ("tr", "en", "en-ca", "de", "it")
DEFAULT_LANDING_LOCALE = "en"

# Meta and hreflang: title, description, og:locale per route
LANDING_META = {
    "tr": {
        "meta_title": "Norya — Kan Tahlili Sonuçlarınızı Dakikalar İçinde Anlayın | Laboratuvar Raporu Açıklaması",
        "meta_description": "Laboratuvar sonuçlarınızı yükleyin; referans aralıkları ve önerilerle net rapor alın. KVKK uyumlu, teşhis yok—yalnızca bilgilendirme. 9 dil.",
        "og_locale": "tr_TR",
    },
    "en": {
        "meta_title": "Norya — Understand Your Blood Test Results in Minutes | Lab Report Explained",
        "meta_description": "Upload your lab results and get a clear report with reference ranges and recommendations. GDPR compliant, no diagnosis—educational only. 9 languages.",
        "og_locale": "en_US",
    },
    "en-ca": {
        "meta_title": "Norya — Reliable AI Blood Test Analysis (Canada)",
        "meta_description": "Understand your lab results in plain language. Upload PDF or photo, get a clear report. Privacy-first, for Canadian users.",
        "og_locale": "en_CA",
    },
    "de": {
        "meta_title": "Norya — Blutwerte & Laborergebnisse verstehen | Auswertung in Minuten",
        "meta_description": "Blutwerte oder Laborergebnisse verstehen: Befund hochladen, in Minuten klaren Bericht mit Referenzbereichen und Empfehlungen. DSGVO-konform, keine Diagnose.",
        "og_locale": "de_DE",
    },
    "it": {
        "meta_title": "Norya — Capire le analisi del sangue in pochi minuti | Referto spiegato",
        "meta_description": "Carica i risultati di laboratorio e ricevi un report chiaro con intervalli di riferimento e indicazioni. GDPR, nessuna diagnosi—solo informazione. 9 lingue.",
        "og_locale": "it_IT",
    },
}


def _tr_ui() -> dict:
    """Turkish landing UI (header, hero, CTA, FAQ, pricing) — DE kalitesinde."""
    return {
        "nav_home": "Ana Sayfa",
        "nav_about": "Hakkımızda",
        "nav_how": "Nasıl Çalışır",
        "nav_reviews": "Yorumlar",
        "nav_pricing": "Fiyatlandırma",
        "nav_corporate": "Kurumsal",
        "nav_blog": "Blog",
        "nav_faq": "SSS",
        "nav_contact": "Bize Ulaşın",
        "nav_login": "Giriş",
        "nav_register": "Ücretsiz Başla",
        "nav_profile": "Profil",
        "nav_analyze": "Analiz Yap",
        "nav_logout": "Çıkış",
        "nav_menu": "Menü",
        "nav_languages": "Diller",
        "hero_sub": "Laboratuvar sonuçları anlaşılır dilde açıklanır. Teşhis değil—sadece hekim görüşmenize hazırlık.",
        "hero_title": "Kan Tahlilinizi Dakikalar İçinde Anlayın",
        "hero_desc": "Sonuçlarınızı yükleyin; referans aralıkları, sade açıklamalar ve önerilerle net rapor alın. Hekim randevunuza hazırlanmak için ideal.",
        "hero_cta": "Analizi Başlat",
        "hero_see_sample": "Örnek Raporu Gör",
        "trust_badge_ssl": "SSL şifreli",
        "trust_badge_kvkk_gdpr": "KVKK uyumlu",
        "trust_badge_paytr": "Güvenli ödeme (PayTR)",
        "trust_badge_qr": "QR ile rapor doğrulama",
        "cta_features_heading": "Birkaç dakikada rapor?",
        "cta_features_sub": "Sonuçlarınızı yükleyin—net önerilerle yapılandırılmış rapor.",
        "cta_start_analysis": "Analizi başlat",
        "faq_title": "Sıkça Sorulan Sorular",
        "faq_subtitle": "Önemli sorulara kısa cevaplar.",
        "faq_q1": "Norya teşhis koyar mı?",
        "faq_a1": "Hayır. Norya yalnızca eğitim amaçlı, anlaşılır açıklama sunar. Teşhis ve tedavi hekime bırakılmalıdır.",
        "faq_q2": "Verilerim güvende mi?",
        "faq_a2": "Evet. Verileriniz şifreli saklanır; satılmaz, reklam amaçlı kullanılmaz.",
        "faq_q3": "PDF veya fotoğraf yükleyebilir miyim?",
        "faq_a3": "Evet. PDF veya sonuç kağıdının fotoğrafını (JPG/PNG) yükleyebilirsiniz.",
        "faq_q4": "Raporu hangi dillerde alabilirim?",
        "faq_a4": "Türkçe, İngilizce, Almanca, İtalyanca, İspanyolca, Fransızca, İbranice, Arapça ve Hintçe. Seçtiğiniz dil tüm rapor için geçerlidir.",
        "faq_q5": "Ücretsiz deneme var mı?",
        "faq_a5": "Evet. Kayıt sonrası sınırlı sayıda ücretsiz analiz sunulur.",
        "faq_q6": "Laboratuvar sonuçlarımı Norya'da analiz ettirebilir miyim?",
        "faq_a6": "Evet. Sonuçlarınızı yükleyerek yapılandırılmış rapor ve anlaşılır açıklama alırsınız. Yalnızca bilgilendirme amaçlı, teşhis değil.",
        "pricing_title": "Fiyatlandırma",
        "pricing_hero_sub": "Kan tahlili analizi: tek rapor veya abonelik.",
        "pricing_eur": "Fiyatlar kendi para biriminizde, şeffaf ve gizli ücret yok.",
        "drawer_trust_meta": "KVKK uyumlu · SSL şifreli · Güvenli ödeme (PayTR)",
        "aria_select_language": "Dil seçin",
    }


def _en_ui() -> dict:
    """English landing UI."""
    return {
        "nav_home": "Home",
        "nav_about": "About",
        "nav_how": "How it works",
        "nav_reviews": "Reviews",
        "nav_pricing": "Pricing",
        "nav_corporate": "Enterprise",
        "nav_blog": "Blog",
        "nav_faq": "FAQ",
        "nav_contact": "Contact",
        "nav_login": "Log in",
        "nav_register": "Get started free",
        "nav_profile": "Profile",
        "nav_analyze": "Analyze",
        "nav_logout": "Log out",
        "nav_menu": "Menu",
        "nav_languages": "Languages",
        "hero_sub": "Lab results explained in plain language. Not a diagnosis—just clear guidance for your next doctor visit.",
        "hero_title": "Understand Your Blood Test in Minutes",
        "hero_desc": "Upload your lab results and get a clear report with reference ranges, plain-language explanations and recommendations. Ideal to prepare for your appointment.",
        "hero_cta": "Start analysis",
        "hero_see_sample": "See sample report",
        "trust_badge_ssl": "SSL encrypted",
        "trust_badge_kvkk_gdpr": "GDPR compliant",
        "trust_badge_paytr": "Secure payment (PayTR)",
        "trust_badge_qr": "QR report verification",
        "cta_features_heading": "Report in a few minutes?",
        "cta_features_sub": "Upload your results—structured report with clear recommendations.",
        "cta_start_analysis": "Start analysis",
        "faq_title": "Frequently Asked Questions",
        "faq_subtitle": "Short answers to the essentials.",
        "faq_q1": "Does Norya give a diagnosis?",
        "faq_a1": "No. Norya only provides educational, easy-to-understand explanations. Diagnosis and treatment are for your doctor.",
        "faq_q2": "Is my data secure?",
        "faq_a2": "Yes. Your data is stored encrypted; not sold or used for advertising.",
        "faq_q3": "Can I upload PDF or photo?",
        "faq_a3": "Yes. You can upload a PDF or a photo (JPG/PNG) of your result sheet.",
        "faq_q4": "In which languages can I get the report?",
        "faq_a4": "English, German, Turkish, Italian, Spanish, French, Hebrew, Arabic and Hindi. The language you choose applies to the full report.",
        "faq_q5": "Is there a free trial?",
        "faq_a5": "Yes. After signing up, you get a limited number of free analyses.",
        "faq_q6": "Can I have my lab results analysed on Norya?",
        "faq_a6": "Yes. Upload your results to get a structured report and plain-language explanations. For information only, not diagnosis.",
        "pricing_title": "Pricing",
        "pricing_hero_sub": "Blood test analysis: single report or subscription.",
        "pricing_eur": "Prices in your currency, transparent and no hidden fees.",
        "drawer_trust_meta": "GDPR compliant · SSL encrypted · Secure payment (PayTR)",
        "aria_select_language": "Select language",
    }


def _de_ui() -> dict:
    """German landing UI."""
    return {
        "nav_home": "Startseite",
        "nav_about": "Über uns",
        "nav_how": "So funktioniert's",
        "nav_reviews": "Bewertungen",
        "nav_pricing": "Preise",
        "nav_corporate": "Unternehmen",
        "nav_blog": "Blog",
        "nav_faq": "FAQ",
        "nav_contact": "Kontakt",
        "nav_login": "Anmelden",
        "nav_register": "Kostenlos starten",
        "nav_profile": "Profil",
        "nav_analyze": "Analysieren",
        "nav_logout": "Abmelden",
        "nav_menu": "Menü",
        "nav_languages": "Sprachen",
        "hero_sub": "Laborergebnisse verständlich erklärt — keine Diagnose, nur Orientierung.",
        "hero_title": "Blutwerte in Minuten verstehen",
        "hero_desc": "Befund hochladen, klaren Bericht bekommen: Referenzbereiche, Einordnung und Empfehlungen. Ideal vor dem Arztbesuch.",
        "hero_cta": "Analyse starten",
        "hero_see_sample": "Beispielbericht ansehen",
        "trust_badge_ssl": "SSL-verschlüsselt",
        "trust_badge_kvkk_gdpr": "DSGVO-konform",
        "trust_badge_paytr": "Sichere Zahlung (PayTR)",
        "trust_badge_qr": "QR-Berichtsprüfung",
        "cta_features_heading": "Bericht in wenigen Minuten?",
        "cta_features_sub": "Befund hochladen — strukturierter Bericht mit klaren Empfehlungen.",
        "cta_start_analysis": "Analyse starten",
        "faq_title": "Häufig gestellte Fragen",
        "faq_subtitle": "Kurze Antworten auf das Wichtigste.",
        "faq_q1": "Stellt Norya eine Diagnose?",
        "faq_a1": "Nein. Norya liefert nur bildende, verständliche Erklärungen. Diagnose und Behandlung obliegen dem Arzt.",
        "faq_q2": "Sind meine Daten sicher?",
        "faq_a2": "Ja. Ihre Daten werden verschlüsselt gespeichert; nicht verkauft oder für Werbung genutzt.",
        "faq_q3": "Kann ich PDF oder Foto hochladen?",
        "faq_a3": "Ja. Sie können eine PDF oder ein Foto (JPG/PNG) des Ergebnisbogens hochladen.",
        "faq_q4": "In welchen Sprachen gibt es den Bericht?",
        "faq_a4": "Deutsch, Englisch, Türkisch, Italienisch, Spanisch, Französisch, Hebräisch, Arabisch und Hindi. Die gewählte Sprache gilt für den gesamten Bericht.",
        "faq_q5": "Gibt es eine kostenlose Testversion?",
        "faq_a5": "Ja. Nach der Registrierung erhalten Sie eine begrenzte Anzahl kostenloser Analysen.",
        "faq_q6": "Kann ich meine Laborwerte bei Norya auswerten lassen?",
        "faq_a6": "Ja. Laden Sie Ihren Befund hoch und erhalten Sie einen strukturierten Bericht und verständliche Erklärungen. Nur zur Information, keine Diagnose.",
        "pricing_title": "Preise",
        "pricing_hero_sub": "Blutwerte auswerten: Einzelbericht oder Abo.",
        "pricing_eur": "Preise in Ihrer Währung, transparent und ohne versteckte Kosten.",
        "drawer_trust_meta": "DSGVO-konform · SSL-verschlüsselt · Sichere Zahlung (PayTR)",
        "aria_select_language": "Sprache wählen",
    }


def _it_ui() -> dict:
    """Italian landing UI."""
    return {
        "nav_home": "Home",
        "nav_about": "Chi siamo",
        "nav_how": "Come funziona",
        "nav_reviews": "Recensioni",
        "nav_pricing": "Prezzi",
        "nav_corporate": "Enterprise",
        "nav_blog": "Blog",
        "nav_faq": "FAQ",
        "nav_contact": "Contatti",
        "nav_login": "Accedi",
        "nav_register": "Inizia gratis",
        "nav_profile": "Profilo",
        "nav_analyze": "Analizza",
        "nav_logout": "Esci",
        "nav_menu": "Menu",
        "nav_languages": "Lingue",
        "hero_sub": "Referti di laboratorio spiegati in linguaggio chiaro. Nessuna diagnosi—solo orientamento per la prossima visita.",
        "hero_title": "Comprendi le tue analisi del sangue in pochi minuti",
        "hero_desc": "Carica i risultati di laboratorio e ricevi un report chiaro con intervalli di riferimento, spiegazioni in linguaggio semplice e indicazioni. Ideale per prepararti alla visita.",
        "hero_cta": "Avvia analisi",
        "hero_see_sample": "Vedi report di esempio",
        "trust_badge_ssl": "Connessione SSL",
        "trust_badge_kvkk_gdpr": "Conforme GDPR",
        "trust_badge_paytr": "Pagamento sicuro (PayTR)",
        "trust_badge_qr": "Verifica report con QR",
        "cta_features_heading": "Report in pochi minuti?",
        "cta_features_sub": "Carica i risultati—report strutturato con indicazioni chiare.",
        "cta_start_analysis": "Avvia analisi",
        "faq_title": "Domande frequenti",
        "faq_subtitle": "Risposte brevi sull'essenziale.",
        "faq_q1": "Norya fa diagnosi?",
        "faq_a1": "No. Norya fornisce solo spiegazioni a scopo informativo. Diagnosi e trattamento spettano al medico.",
        "faq_q2": "I miei dati sono al sicuro?",
        "faq_a2": "Sì. I dati sono memorizzati crittografati; non venduti né usati per pubblicità.",
        "faq_q3": "Posso caricare PDF o foto?",
        "faq_a3": "Sì. Puoi caricare un PDF o una foto (JPG/PNG) del referto.",
        "faq_q4": "In quali lingue è disponibile il report?",
        "faq_a4": "Italiano, inglese, tedesco, turco, spagnolo, francese, ebraico, arabo e hindi. La lingua scelta vale per l'intero report.",
        "faq_q5": "C'è una prova gratuita?",
        "faq_a5": "Sì. Dopo la registrazione hai diritto a un numero limitato di analisi gratuite.",
        "faq_q6": "Posso far analizzare i miei risultati di laboratorio su Norya?",
        "faq_a6": "Sì. Carica i risultati per ottenere un report strutturato e spiegazioni chiare. Solo a scopo informativo, non diagnosi.",
        "pricing_title": "Prezzi",
        "pricing_hero_sub": "Analisi del sangue: report singolo o abbonamento.",
        "pricing_eur": "Prezzi nella tua valuta, trasparenti e senza costi nascosti.",
        "drawer_trust_meta": "Conforme GDPR · Connessione SSL · Pagamento sicuro (PayTR)",
        "aria_select_language": "Seleziona lingua",
    }


# Per-locale UI; en-ca uses English
LANDING_UI = {
    "tr": _tr_ui(),
    "en": _en_ui(),
    "en-ca": _en_ui(),  # placeholder: same as en
    "de": _de_ui(),
    "it": _it_ui(),
}


def get_landing_meta(locale: str) -> dict:
    """Return meta_title, meta_description, og_locale for the given locale."""
    locale = (locale or "").strip().lower()
    if locale not in LANDING_META:
        locale = DEFAULT_LANDING_LOCALE
    return dict(LANDING_META.get(locale, LANDING_META[DEFAULT_LANDING_LOCALE]))


def get_landing_ui(locale: str) -> dict:
    """Return full landing UI strings (header, hero, CTA, FAQ, pricing) for the given locale."""
    locale = (locale or "").strip().lower()
    if locale not in LANDING_UI:
        locale = DEFAULT_LANDING_LOCALE
    return dict(LANDING_UI.get(locale, LANDING_UI[DEFAULT_LANDING_LOCALE]))
