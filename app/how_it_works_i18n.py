# -*- coding: utf-8 -*-
"""How it works page i18n. Supports DE, EN, TR, IT, FR, ES for /how-it-works. Used in Google Ads site links."""

from __future__ import annotations

HOW_IT_WORKS_LANGS = ("de", "en", "tr", "it", "fr", "es")
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
        "meta_description": "Upload your lab results and get a clear report. No diagnosis—educational explanations only. GDPR compliant, 9 languages.",
        "nav_home": "Home",
        "nav_how": "How it works",
        "nav_pricing": "Pricing",
        "nav_analyze": "Start analysis",
        "hero_title": "How Norya Works",
        "hero_sub": "Your lab results explained in minutes. No diagnosis—clear, educational summaries to prepare for your doctor visit.",
        "cta_primary": "Start analysis",
        "cta_secondary": "View pricing",
        "section_how_title": "How it works — 3 steps",
        "step1_title": "Create an account",
        "step1_desc": "Free sign-up. No credit card required to get started.",
        "step2_title": "Upload results or enter values",
        "step2_desc": "PDF, photo, or paste text of your lab results—Norya reads values and reference ranges.",
        "step3_title": "Get your explained report",
        "step3_desc": "Structured report with reference ranges, plain-language explanations and highlights. Ideal to prepare for your doctor appointment.",
        "section_report_title": "What you see in your Norya report",
        "report_ref": "Reference ranges for each value (normal / low / high).",
        "report_plain": "Plain-language explanations you can understand.",
        "report_highlights": "Key takeaways and recommendations at a glance.",
        "report_doctor_prep": "Preparation for your doctor visit—come with better questions.",
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
        "hero_sub": "Laboratuvar sonuçlarınız dakikalar içinde anlaşılır hale gelir. Teşhis koymuyoruz—hekim görüşmenize hazırlanmanız için net, eğitim amaçlı özetler.",
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


def _it() -> dict:
    return {
        "meta_title": "Come funziona Norya — Capire le analisi del sangue in 3 passi",
        "meta_description": "Carica i risultati di laboratorio e ricevi un report chiaro. Nessuna diagnosi—solo informazione. Conforme GDPR, 9 lingue.",
        "nav_home": "Home",
        "nav_how": "Come funziona",
        "nav_pricing": "Prezzi",
        "nav_analyze": "Avvia analisi",
        "hero_title": "Come funziona Norya",
        "hero_sub": "I tuoi referti spiegati in pochi minuti. Nessuna diagnosi—riassunti chiari per prepararti alla visita.",
        "cta_primary": "Avvia analisi",
        "cta_secondary": "Vedi prezzi",
        "section_how_title": "Come funziona — 3 passi",
        "step1_title": "Crea un account",
        "step1_desc": "Registrazione gratuita. Nessuna carta richiesta per iniziare.",
        "step2_title": "Carica i risultati o inserisci i valori",
        "step2_desc": "PDF, foto o testo incollato dei referti—Norya legge valori e intervalli di riferimento.",
        "step3_title": "Ricevi il report spiegato",
        "step3_desc": "Report strutturato con intervalli di riferimento, spiegazioni in linguaggio chiaro e punti salienti. Ideale per prepararti alla visita.",
        "section_report_title": "Cosa trovi nel report Norya",
        "report_ref": "Intervalli di riferimento per ogni valore (normale / basso / alto).",
        "report_plain": "Spiegazioni in linguaggio chiaro.",
        "report_highlights": "Punti chiave e indicazioni a colpo d'occhio.",
        "report_doctor_prep": "Preparazione alla visita—vieni con domande più mirate.",
        "section_trust_title": "Sicurezza e trasparenza",
        "trust_dsgvo": "Conforme GDPR e KVKK. Dati crittografati, non venduti a terzi. Pagamento sicuro (PayTR), SSL.",
        "trust_disclaimer": "Norya non fornisce diagnosi. Tutto il contenuto è solo informativo. Consulta sempre un medico per sintomi o decisioni di cura.",
        "section_who_title": "A chi è rivolto Norya?",
        "who_1": "Vuoi capire meglio i tuoi risultati di laboratorio.",
        "who_2": "Vuoi prepararti alla visita e fare domande più mirate.",
        "who_3": "Ti serve il report in un'altra lingua (italiano, inglese, tedesco, turco…).",
        "section_cta_title": "Pronto per il tuo primo report?",
        "cta_primary2": "Avvia analisi",
        "cta_secondary2": "Vedi prezzi",
        "footer_legal": "Legale",
        "footer_privacy": "Privacy",
        "footer_terms": "Termini d'uso",
    }


def _fr() -> dict:
    return {
        "meta_title": "Comment fonctionne Norya — Comprendre vos analyses en 3 étapes",
        "meta_description": "Uploadez vos résultats de laboratoire et recevez un rapport clair. Pas de diagnostic—information uniquement. Conforme RGPD, 9 langues.",
        "nav_home": "Accueil",
        "nav_how": "Comment ça marche",
        "nav_pricing": "Tarifs",
        "nav_analyze": "Lancer l'analyse",
        "hero_title": "Comment fonctionne Norya",
        "hero_sub": "Vos résultats d'analyses expliqués en quelques minutes. Pas de diagnostic—des résumés clairs pour préparer votre consultation.",
        "cta_primary": "Lancer l'analyse",
        "cta_secondary": "Voir les tarifs",
        "section_how_title": "Comment ça marche — 3 étapes",
        "step1_title": "Créer un compte",
        "step1_desc": "Inscription gratuite. Aucune carte bancaire requise pour commencer.",
        "step2_title": "Uploadez les résultats ou saisissez les valeurs",
        "step2_desc": "PDF, photo ou texte collé de vos analyses—Norya lit les valeurs et les fourchettes de référence.",
        "step3_title": "Recevez votre rapport expliqué",
        "step3_desc": "Rapport structuré avec fourchettes de référence, explications en langage clair et points clés. Idéal pour préparer la consultation.",
        "section_report_title": "Ce que vous voyez dans votre rapport Norya",
        "report_ref": "Fourchettes de référence pour chaque valeur (normal / bas / haut).",
        "report_plain": "Explications en langage clair.",
        "report_highlights": "Points clés et recommandations en un coup d'œil.",
        "report_doctor_prep": "Préparation à la consultation—posez les bonnes questions.",
        "section_trust_title": "Sécurité et transparence",
        "trust_dsgvo": "Conforme RGPD et KVKK. Données chiffrées, non vendues à des tiers. Paiement sécurisé (PayTR), SSL.",
        "trust_disclaimer": "Norya ne pose pas de diagnostic. Tout le contenu est à titre informatif. Consultez toujours un médecin pour symptômes ou décisions de traitement.",
        "section_who_title": "À qui s'adresse Norya ?",
        "who_1": "Vous voulez mieux comprendre vos propres résultats.",
        "who_2": "Vous voulez vous préparer avant la consultation et poser de meilleures questions.",
        "who_3": "Vous avez besoin du rapport dans une autre langue (français, anglais, allemand, turc…).",
        "section_cta_title": "Prêt pour votre premier rapport ?",
        "cta_primary2": "Lancer l'analyse",
        "cta_secondary2": "Voir les tarifs",
        "footer_legal": "Mentions légales",
        "footer_privacy": "Confidentialité",
        "footer_terms": "Conditions d'utilisation",
    }


def _es() -> dict:
    return {
        "meta_title": "Cómo funciona Norya — Entender tus análisis en 3 pasos",
        "meta_description": "Sube tus resultados de laboratorio y recibe un informe claro. No es un diagnóstico—solo información. Cumple GDPR, 9 idiomas.",
        "nav_home": "Inicio",
        "nav_how": "Cómo funciona",
        "nav_pricing": "Precios",
        "nav_analyze": "Iniciar análisis",
        "hero_title": "Cómo funciona Norya",
        "hero_sub": "Tus resultados explicados en minutos. No hacemos diagnóstico—resúmenes claros para preparar tu visita al médico.",
        "cta_primary": "Iniciar análisis",
        "cta_secondary": "Ver precios",
        "section_how_title": "Cómo funciona — 3 pasos",
        "step1_title": "Crear una cuenta",
        "step1_desc": "Registro gratuito. No hace falta tarjeta para empezar.",
        "step2_title": "Sube resultados o introduce valores",
        "step2_desc": "PDF, foto o texto pegado de tus análisis—Norya lee valores e intervalos de referencia.",
        "step3_title": "Recibe tu informe explicado",
        "step3_desc": "Informe estructurado con intervalos de referencia, explicaciones en lenguaje claro y puntos clave. Ideal para preparar la consulta.",
        "section_report_title": "Qué verás en tu informe Norya",
        "report_ref": "Intervalos de referencia para cada valor (normal / bajo / alto).",
        "report_plain": "Explicaciones en lenguaje claro.",
        "report_highlights": "Puntos clave y recomendaciones de un vistazo.",
        "report_doctor_prep": "Preparación para la consulta—lleva mejores preguntas.",
        "section_trust_title": "Seguridad y transparencia",
        "trust_dsgvo": "Cumplimiento GDPR y KVKK. Datos cifrados, no vendidos a terceros. Pago seguro (PayTR), SSL.",
        "trust_disclaimer": "Norya no da diagnóstico. Todo el contenido es solo informativo. Consulte siempre a un médico para síntomas o decisiones de tratamiento.",
        "section_who_title": "¿Para quién es Norya?",
        "who_1": "Quieres entender mejor tus propios resultados.",
        "who_2": "Quieres prepararte antes de la consulta y hacer mejores preguntas.",
        "who_3": "Necesitas el informe en otro idioma (español, inglés, alemán, turco…).",
        "section_cta_title": "¿Listo para tu primer informe?",
        "cta_primary2": "Iniciar análisis",
        "cta_secondary2": "Ver precios",
        "footer_legal": "Legal",
        "footer_privacy": "Privacidad",
        "footer_terms": "Términos de uso",
    }


_HOW_IT_WORKS_UI = {
    "de": _de(),
    "en": _en(),
    "tr": _tr(),
    "it": _it(),
    "fr": _fr(),
    "es": _es(),
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
