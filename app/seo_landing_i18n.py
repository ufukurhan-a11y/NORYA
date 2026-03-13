# -*- coding: utf-8 -*-
"""
SEO landing pages: high-intent queries per locale.
Routes: /tr/kan-tahlili-sonucu, /tr/kan-degerleri-anlama, /tr/hemogram-sonucu,
        /de/blutwerte-verstehen, /de/laborwerte-verstehen,
        /en/blood-test-results, /en/understand-lab-results.
Content is native per language; no diagnosis claims; informational only.
"""

from __future__ import annotations

# (lang, path_slug) -> page key for routing; used to know which content to load
SEO_LANDING_ROUTES = {
    ("tr", "kan-tahlili-sonucu"),
    ("tr", "kan-degerleri-anlama"),
    ("tr", "hemogram-sonucu"),
    ("de", "blutwerte-verstehen"),
    ("de", "laborwerte-verstehen"),
    ("en", "blood-test-results"),
    ("en", "understand-lab-results"),
}

# Hreflang: (lang, slug) -> list of (lang_alt, slug_alt) for alternate URLs
SEO_LANDING_HREFLANG = {
    ("tr", "kan-tahlili-sonucu"): [("en", "blood-test-results")],
    ("en", "blood-test-results"): [("tr", "kan-tahlili-sonucu")],
    ("tr", "kan-degerleri-anlama"): [],
    ("tr", "hemogram-sonucu"): [],
    ("de", "blutwerte-verstehen"): [],
    ("de", "laborwerte-verstehen"): [],
    ("en", "understand-lab-results"): [],
}

OG_LOCALE_MAP = {"tr": "tr_TR", "de": "de_DE", "en": "en_US"}


def _tr_kan_tahlili() -> dict:
    return {
        "meta_title": "Kan Tahlili Sonucu Anlama ve Yorumlama | Norya",
        "meta_description": "Kan tahlili sonucunuzu anlamak için laboratuvar raporunuzu yükleyin; referans aralıkları ve sade açıklamalarla özet rapor alırsınız. Teşhis değil, yalnızca bilgilendirme.",
        "hero_title": "Kan Tahlili Sonucunu Anlama ve Yorumlama",
        "hero_sub": "Laboratuvar sonuçlarınızı yükleyin; referans aralıkları ve anlaşılır açıklamalarla yapılandırılmış rapor alın. Hekim randevunuza hazırlanmak için kullanabilirsiniz.",
        "cta_primary": "Analizi Başlat",
        "cta_secondary": "Fiyatları Gör",
        "section_how_title": "Nasıl çalışır — 3 adım",
        "step1_title": "Hesap oluşturun",
        "step1_desc": "Ücretsiz kayıt. Başlamak için kredi kartı gerekmez.",
        "step2_title": "Sonuçları yükleyin",
        "step2_desc": "Tahlil PDF'inizi veya sonuç kağıdının fotoğrafını yükleyin — Norya değerleri ve referans aralıklarını okur.",
        "step3_title": "Açıklamalı raporunuzu alın",
        "step3_desc": "Referans aralıkları, sade açıklamalar ve önemli noktalarla yapılandırılmış rapor. Hekim randevunuza hazırlanmak için ideal.",
        "section_report_title": "Raporda neler görürsünüz?",
        "report_ref": "Her değer için referans aralıkları (normal / düşük / yüksek).",
        "report_plain": "Anlaşılır, sade dilde açıklamalar.",
        "report_highlights": "Önemli çıkarımlar ve öneriler tek bakışta.",
        "report_doctor_prep": "Hekim görüşmesine hazırlık — daha iyi sorularla gidin.",
        "section_who_title": "Kimler için uygun?",
        "who_1": "Tahlil sonuçlarınızı kendi başınıza daha iyi anlamak isteyenler.",
        "who_2": "Hekim randevusu öncesi hazırlanıp daha bilinçli sorular sormak isteyenler.",
        "who_3": "Raporunuzu farklı bir dilde (Türkçe, İngilizce, Almanca vb.) almak isteyenler.",
        "section_trust_title": "Güven ve şeffaflık",
        "trust_dsgvo": "KVKK ve GDPR uyumlu. Verileriniz şifreli saklanır; üçüncü taraflara satılmaz. Güvenli ödeme (PayTR), SSL.",
        "trust_disclaimer": "Norya teşhis koymaz. Tüm içerik yalnızca bilgilendirme ve eğitim amaçlıdır. Belirti veya tedavi kararları için mutlaka bir hekime danışın.",
        "faq_title": "Sıkça Sorulan Sorular",
        "faq_q1": "Kan tahlili sonucu nasıl yorumlanır?",
        "faq_a1": "Norya, laboratuvar değerlerinizi referans aralıklarıyla karşılaştırıp sade dilde açıklar. Bu bir teşhis değildir; hekim görüşmesine hazırlık için bilgilendirme sunar.",
        "faq_q2": "PDF veya fotoğraf yükleyebilir miyim?",
        "faq_a2": "Evet. Tahlil sonucunuzun PDF'i veya fotoğrafını (JPG/PNG) yükleyebilirsiniz.",
        "faq_q3": "Norya teşhis koyar mı?",
        "faq_a3": "Hayır. Norya yalnızca eğitim amaçlı açıklama sunar. Teşhis ve tedavi hekime bırakılmalıdır.",
        "section_cta_title": "İlk raporunuz için hazır mısınız?",
        "cta_primary2": "Analizi Başlat",
        "cta_secondary2": "Fiyatları Gör",
        "related_title": "İlgili içerikler",
        "related_1_label": "Kan değerleri anlama",
        "related_1_path": "/tr/kan-degerleri-anlama",
        "related_2_label": "Nasıl çalışır",
        "related_2_path": "/how-it-works",
        "nav_home": "Ana Sayfa",
        "nav_how": "Nasıl Çalışır",
        "nav_pricing": "Fiyatlandırma",
        "nav_analyze": "Analiz Yap",
        "nav_blog": "Blog",
        "footer_privacy": "Gizlilik",
        "footer_terms": "Kullanım Koşulları",
    }


def _tr_kan_degerleri() -> dict:
    return {
        "meta_title": "Kan Değerleri Anlama Rehberi | Norya",
        "meta_description": "Kan değerlerinizi nasıl okuyacağınızı öğrenin. Raporunuzu yükleyin; referans aralıkları ve sade açıklamalarla değerleri anlayın. Yalnızca bilgilendirme amaçlı.",
        "hero_title": "Kan Değerlerini Anlama",
        "hero_sub": "Laboratuvar raporunuzdaki değerlerin anlamı nedir? Raporunuzu yükleyerek referans aralıkları ve sade açıklamalarla özet alabilirsiniz.",
        "cta_primary": "Analizi Başlat",
        "cta_secondary": "Fiyatları Gör",
        "section_how_title": "Nasıl çalışır — 3 adım",
        "step1_title": "Hesap oluşturun",
        "step1_desc": "Ücretsiz kayıt. Başlamak için kredi kartı gerekmez.",
        "step2_title": "Sonuçları yükleyin",
        "step2_desc": "Raporunuzun PDF'i veya fotoğrafını yükleyin — Norya kan değerlerini ve referans aralıklarını okur.",
        "step3_title": "Açıklamalı raporunuzu alın",
        "step3_desc": "Her değer için referans aralığı, sade açıklama ve öneriler. Hekim randevunuza hazırlık için ideal.",
        "section_report_title": "Raporda neler görürsünüz?",
        "report_ref": "Her kan değeri için referans aralıkları (normal / düşük / yüksek).",
        "report_plain": "Tıbbi terimler sade dilde açıklanır.",
        "report_highlights": "Önemli noktalar ve öneriler tek bakışta.",
        "report_doctor_prep": "Hekim görüşmesine hazırlık — daha iyi sorularla gidin.",
        "section_who_title": "Kimler için uygun?",
        "who_1": "Kan değerlerinizi kendi başınıza anlamak isteyenler.",
        "who_2": "Hekim öncesi hazırlanıp doğru soruları sormak isteyenler.",
        "who_3": "Raporu farklı dilde almak isteyenler.",
        "section_trust_title": "Güven ve şeffaflık",
        "trust_dsgvo": "KVKK ve GDPR uyumlu. Verileriniz şifreli; satılmaz. Güvenli ödeme (PayTR), SSL.",
        "trust_disclaimer": "Norya teşhis koymaz. Tüm içerik yalnızca bilgilendirme amaçlıdır. Tedavi kararları için hekime danışın.",
        "faq_title": "Sıkça Sorulan Sorular",
        "faq_q1": "Kan değerleri nasıl yorumlanır?",
        "faq_a1": "Norya, değerlerinizi referans aralıklarıyla karşılaştırıp sade dilde açıklar. Teşhis değildir; bilgilendirme amaçlıdır.",
        "faq_q2": "Hangi belgeleri yükleyebilirim?",
        "faq_a2": "Laboratuvar raporunuzun PDF'i veya fotoğrafını (JPG/PNG) yükleyebilirsiniz.",
        "faq_q3": "Norya teşhis koyar mı?",
        "faq_a3": "Hayır. Yalnızca eğitim amaçlı açıklama sunar. Teşhis hekime bırakılmalıdır.",
        "section_cta_title": "Kan değerlerinizi anlamaya başlayın",
        "cta_primary2": "Analizi Başlat",
        "cta_secondary2": "Fiyatları Gör",
        "related_title": "İlgili içerikler",
        "related_1_label": "Kan tahlili sonucu anlama",
        "related_1_path": "/tr/kan-tahlili-sonucu",
        "related_2_label": "Hemogram sonucu",
        "related_2_path": "/tr/hemogram-sonucu",
        "nav_home": "Ana Sayfa",
        "nav_how": "Nasıl Çalışır",
        "nav_pricing": "Fiyatlandırma",
        "nav_analyze": "Analiz Yap",
        "nav_blog": "Blog",
        "footer_privacy": "Gizlilik",
        "footer_terms": "Kullanım Koşulları",
    }


def _tr_hemogram() -> dict:
    return {
        "meta_title": "Hemogram Sonucu Anlama ve Yorumlama | Norya",
        "meta_description": "Hemogram (tam kan sayımı) sonucunuzu anlamak için raporunuzu yükleyin; WBC, RBC, hemoglobin ve trombosit değerleri referans aralıklarıyla sade dilde açıklanır. Bilgilendirme amaçlı.",
        "hero_title": "Hemogram Sonucu Anlama ve Yorumlama",
        "hero_sub": "Tam kan sayımı raporunuzu yükleyin; WBC, RBC, hemoglobin ve trombosit gibi değerler referans aralıklarıyla birlikte sade dilde açıklanır.",
        "cta_primary": "Analizi Başlat",
        "cta_secondary": "Fiyatları Gör",
        "section_how_title": "Nasıl çalışır — 3 adım",
        "step1_title": "Hesap oluşturun",
        "step1_desc": "Ücretsiz kayıt. Başlamak için kredi kartı gerekmez.",
        "step2_title": "Hemogram sonucunu yükleyin",
        "step2_desc": "Tam kan sayımı raporunuzun PDF'i veya fotoğrafını yükleyin — Norya değerleri okur.",
        "step3_title": "Açıklamalı raporunuzu alın",
        "step3_desc": "Her parametre için referans aralığı ve sade açıklama. Hekim randevunuza hazırlık için ideal.",
        "section_report_title": "Raporda neler görürsünüz?",
        "report_ref": "WBC, RBC, hemoglobin, trombosit vb. için referans aralıkları.",
        "report_plain": "Tıbbi terimler sade dilde açıklanır.",
        "report_highlights": "Önemli noktalar ve öneriler tek bakışta.",
        "report_doctor_prep": "Hekim görüşmesine hazırlık — daha iyi sorularla gidin.",
        "section_who_title": "Kimler için uygun?",
        "who_1": "Hemogram sonucunu kendi başınıza anlamak isteyenler.",
        "who_2": "Tam kan sayımı değerlerini hekim öncesi gözden geçirmek isteyenler.",
        "who_3": "Raporu farklı dilde almak isteyenler.",
        "section_trust_title": "Güven ve şeffaflık",
        "trust_dsgvo": "KVKK ve GDPR uyumlu. Verileriniz şifreli; satılmaz. Güvenli ödeme (PayTR), SSL.",
        "trust_disclaimer": "Norya teşhis koymaz. Tüm içerik yalnızca bilgilendirme amaçlıdır. Tedavi kararları için hekime danışın.",
        "faq_title": "Sıkça Sorulan Sorular",
        "faq_q1": "Hemogram sonucu nasıl yorumlanır?",
        "faq_a1": "Norya, tam kan sayımı değerlerinizi referans aralıklarıyla karşılaştırıp sade dilde açıklar. Teşhis değildir; bilgilendirme amaçlıdır.",
        "faq_q2": "Hangi değerler açıklanır?",
        "faq_a2": "WBC, RBC, hemoglobin, hematokrit, trombosit ve diğer hemogram parametreleri referans aralıklarıyla birlikte açıklanır.",
        "faq_q3": "Norya teşhis koyar mı?",
        "faq_a3": "Hayır. Yalnızca eğitim amaçlı açıklama sunar. Teşhis hekime bırakılmalıdır.",
        "section_cta_title": "Hemogram raporunuzu anlamaya başlayın",
        "cta_primary2": "Analizi Başlat",
        "cta_secondary2": "Fiyatları Gör",
        "related_title": "İlgili içerikler",
        "related_1_label": "Kan tahlili sonucu anlama",
        "related_1_path": "/tr/kan-tahlili-sonucu",
        "related_2_label": "Kan değerleri anlama",
        "related_2_path": "/tr/kan-degerleri-anlama",
        "nav_home": "Ana Sayfa",
        "nav_how": "Nasıl Çalışır",
        "nav_pricing": "Fiyatlandırma",
        "nav_analyze": "Analiz Yap",
        "nav_blog": "Blog",
        "footer_privacy": "Gizlilik",
        "footer_terms": "Kullanım Koşulları",
    }


def _de_blutwerte() -> dict:
    return {
        "meta_title": "Blutwerte verstehen — Befund einordnen mit Norya",
        "meta_description": "Blutwerte verstehen: Befund hochladen, klaren Bericht mit Referenzbereichen und Einordnung erhalten. Keine Diagnose — nur Aufklärung. DSGVO-konform.",
        "hero_title": "Blutwerte verstehen — Befund einordnen",
        "hero_sub": "Laden Sie Ihren Laborbefund hoch und erhalten Sie einen strukturierten Bericht mit Referenzbereichen und verständlichen Erklärungen. Zur Orientierung vor dem Arztgespräch.",
        "cta_primary": "Analyse starten",
        "cta_secondary": "Preise ansehen",
        "section_how_title": "So funktioniert's — 3 Schritte",
        "step1_title": "Konto erstellen",
        "step1_desc": "Kostenlos registrieren. Keine Kreditkarte für den Einstieg nötig.",
        "step2_title": "Befund hochladen",
        "step2_desc": "PDF oder Foto Ihres Laborbefunds — Norya erkennt Werte und Referenzbereiche.",
        "step3_title": "Bericht mit Erklärungen erhalten",
        "step3_desc": "Strukturierter Bericht mit Referenzbereichen und verständlichen Erklärungen. Ideal zur Vorbereitung auf das Arztgespräch.",
        "section_report_title": "Was Sie im Bericht sehen",
        "report_ref": "Referenzbereiche zu jedem Wert (Normal / niedrig / hoch).",
        "report_plain": "Verständliche Erklärungen in einfacher Sprache.",
        "report_highlights": "Wichtige Punkte und Hinweise auf einen Blick.",
        "report_doctor_prep": "Vorbereitung für das Arztgespräch — Sie kommen mit besseren Fragen.",
        "section_who_title": "Für wen geeignet?",
        "who_1": "Sie möchten Ihre Blutwerte selbst besser einordnen.",
        "who_2": "Sie wollen sich vor dem Arzttermin vorbereiten.",
        "who_3": "Sie benötigen Ihren Bericht in einer anderen Sprache (z. B. Deutsch, Englisch, Türkisch).",
        "section_trust_title": "Sicherheit und Transparenz",
        "trust_dsgvo": "DSGVO-konform. Daten verschlüsselt, nicht an Dritte verkauft. Sichere Zahlung (PayTR), SSL.",
        "trust_disclaimer": "Norya stellt keine Diagnose. Alle Inhalte dienen ausschließlich der Information und Bildung. Bei Beschwerden oder Behandlungsentscheidungen bitte immer einen Arzt konsultieren.",
        "faq_title": "Häufig gestellte Fragen",
        "faq_q1": "Wie werden Blutwerte eingeordnet?",
        "faq_a1": "Norya vergleicht Ihre Werte mit Referenzbereichen und erklärt sie in verständlicher Sprache. Das ist keine Diagnose, sondern Orientierung für das Arztgespräch.",
        "faq_q2": "Kann ich PDF oder Foto hochladen?",
        "faq_a2": "Ja. Sie können eine PDF oder ein Foto (JPG/PNG) Ihres Befunds hochladen.",
        "faq_q3": "Stellt Norya eine Diagnose?",
        "faq_a3": "Nein. Norya liefert nur bildende Erklärungen. Diagnose und Behandlung obliegen dem Arzt.",
        "section_cta_title": "Bereit für Ihren ersten Bericht?",
        "cta_primary2": "Analyse starten",
        "cta_secondary2": "Preise ansehen",
        "related_title": "Das könnte Sie auch interessieren",
        "related_1_label": "Laborwerte verstehen",
        "related_1_path": "/de/laborwerte-verstehen",
        "related_2_label": "So funktioniert's",
        "related_2_path": "/how-it-works",
        "nav_home": "Startseite",
        "nav_how": "So funktioniert's",
        "nav_pricing": "Preise",
        "nav_analyze": "Analysieren",
        "nav_blog": "Blog",
        "footer_privacy": "Datenschutz",
        "footer_terms": "Nutzungsbedingungen",
    }


def _de_laborwerte() -> dict:
    return {
        "meta_title": "Laborwerte verstehen — Befund auswerten mit Norya",
        "meta_description": "Laborwerte verstehen: Befund hochladen, klaren Bericht mit Referenzbereichen und Einordnung erhalten. Keine Diagnose — nur Aufklärung. DSGVO-konform.",
        "hero_title": "Laborwerte verstehen — Befund einordnen",
        "hero_sub": "Laden Sie Ihren Laborbefund hoch und erhalten Sie einen klaren Bericht mit Referenzbereichen und verständlichen Erklärungen. Zur Orientierung vor dem Arztbesuch.",
        "cta_primary": "Analyse starten",
        "cta_secondary": "Preise ansehen",
        "section_how_title": "So funktioniert's — 3 Schritte",
        "step1_title": "Konto erstellen",
        "step1_desc": "Kostenlos registrieren. Keine Kreditkarte für den Einstieg nötig.",
        "step2_title": "Befund hochladen",
        "step2_desc": "PDF oder Foto Ihres Laborbefunds — Norya erkennt Laborwerte und Referenzbereiche.",
        "step3_title": "Bericht mit Erklärungen erhalten",
        "step3_desc": "Strukturierter Bericht mit Referenzbereichen und Einordnung. Ideal zur Vorbereitung auf das Arztgespräch.",
        "section_report_title": "Was Sie im Bericht sehen",
        "report_ref": "Referenzbereiche zu jedem Laborwert (Normal / niedrig / hoch).",
        "report_plain": "Verständliche Erklärungen in einfacher Sprache.",
        "report_highlights": "Wichtige Punkte und Hinweise auf einen Blick.",
        "report_doctor_prep": "Vorbereitung für das Arztgespräch — Sie kommen mit besseren Fragen.",
        "section_who_title": "Für wen geeignet?",
        "who_1": "Sie möchten Ihre Laborwerte selbst besser verstehen.",
        "who_2": "Sie wollen sich vor dem Arzttermin vorbereiten.",
        "who_3": "Sie benötigen Ihren Bericht in einer anderen Sprache.",
        "section_trust_title": "Sicherheit und Transparenz",
        "trust_dsgvo": "DSGVO-konform. Daten verschlüsselt, nicht an Dritte verkauft. Sichere Zahlung (PayTR), SSL.",
        "trust_disclaimer": "Norya stellt keine Diagnose. Alle Inhalte dienen ausschließlich der Information und Bildung. Immer einen Arzt konsultieren.",
        "faq_title": "Häufig gestellte Fragen",
        "faq_q1": "Wie werden Laborwerte erklärt?",
        "faq_a1": "Norya ordnet Ihre Werte Referenzbereichen zu und erklärt sie verständlich. Keine Diagnose — nur Orientierung.",
        "faq_q2": "Kann ich PDF oder Foto hochladen?",
        "faq_a2": "Ja. PDF oder Foto (JPG/PNG) Ihres Befunds hochladen.",
        "faq_q3": "Stellt Norya eine Diagnose?",
        "faq_a3": "Nein. Nur bildende Erklärungen. Diagnose obliegt dem Arzt.",
        "section_cta_title": "Bereit für Ihren ersten Bericht?",
        "cta_primary2": "Analyse starten",
        "cta_secondary2": "Preise ansehen",
        "related_title": "Das könnte Sie auch interessieren",
        "related_1_label": "Blutwerte verstehen",
        "related_1_path": "/de/blutwerte-verstehen",
        "related_2_label": "So funktioniert's",
        "related_2_path": "/how-it-works",
        "nav_home": "Startseite",
        "nav_how": "So funktioniert's",
        "nav_pricing": "Preise",
        "nav_analyze": "Analysieren",
        "nav_blog": "Blog",
        "footer_privacy": "Datenschutz",
        "footer_terms": "Nutzungsbedingungen",
    }


def _en_blood_test_results() -> dict:
    return {
        "meta_title": "Understand Your Blood Test Results | Norya",
        "meta_description": "Upload your blood test results and get a clear report with reference ranges and plain-language explanations. Educational only, no diagnosis. GDPR compliant.",
        "hero_title": "Understand Your Blood Test Results",
        "hero_sub": "Upload your lab results and get a structured report with reference ranges and plain-language explanations. For orientation before your doctor visit.",
        "cta_primary": "Start analysis",
        "cta_secondary": "View pricing",
        "section_how_title": "How it works — 3 steps",
        "step1_title": "Create an account",
        "step1_desc": "Free sign-up. No credit card required to get started.",
        "step2_title": "Upload your results",
        "step2_desc": "PDF or photo of your lab report — Norya reads values and reference ranges.",
        "step3_title": "Get your explained report",
        "step3_desc": "Structured report with reference ranges and plain-language explanations. Ideal to prepare for your doctor appointment.",
        "section_report_title": "What you see in your report",
        "report_ref": "Reference ranges for each value (normal / low / high).",
        "report_plain": "Plain-language explanations you can understand.",
        "report_highlights": "Key takeaways and points to discuss with your doctor.",
        "report_doctor_prep": "Preparation for your doctor visit — come with better questions.",
        "section_who_title": "Who is it for?",
        "who_1": "You want to understand your own blood test results better.",
        "who_2": "You want to prepare before your doctor appointment and ask better questions.",
        "who_3": "You need your report in another language (e.g. English, German, Turkish).",
        "section_trust_title": "Security and transparency",
        "trust_dsgvo": "GDPR compliant. Data encrypted, not sold to third parties. Secure payment (PayTR), SSL.",
        "trust_disclaimer": "Norya does not provide a diagnosis. All content is for information and education only. Always consult a doctor for symptoms or treatment decisions.",
        "faq_title": "Frequently Asked Questions",
        "faq_q1": "How are blood test results explained?",
        "faq_a1": "Norya compares your values to reference ranges and explains them in plain language. This is not a diagnosis—it's guidance to prepare for your doctor visit.",
        "faq_q2": "Can I upload PDF or photo?",
        "faq_a2": "Yes. You can upload a PDF or a photo (JPG/PNG) of your lab result.",
        "faq_q3": "Does Norya give a diagnosis?",
        "faq_a3": "No. Norya only provides educational explanations. Diagnosis and treatment are for your doctor.",
        "section_cta_title": "Ready for your first report?",
        "cta_primary2": "Start analysis",
        "cta_secondary2": "View pricing",
        "related_title": "Related content",
        "related_1_label": "Understand lab results",
        "related_1_path": "/en/understand-lab-results",
        "related_2_label": "How it works",
        "related_2_path": "/how-it-works",
        "nav_home": "Home",
        "nav_how": "How it works",
        "nav_pricing": "Pricing",
        "nav_analyze": "Analyze",
        "nav_blog": "Blog",
        "footer_privacy": "Privacy",
        "footer_terms": "Terms of use",
    }


def _en_understand_lab_results() -> dict:
    return {
        "meta_title": "Understand Lab Results — Clear Report | Norya",
        "meta_description": "Understand your lab results: upload your report and get reference ranges and plain-language explanations. Educational only, no diagnosis. GDPR compliant.",
        "hero_title": "Understand Your Lab Results",
        "hero_sub": "Upload your lab report and get a clear summary with reference ranges and plain-language explanations. For orientation before your doctor appointment.",
        "cta_primary": "Start analysis",
        "cta_secondary": "View pricing",
        "section_how_title": "How it works — 3 steps",
        "step1_title": "Create an account",
        "step1_desc": "Free sign-up. No credit card required to get started.",
        "step2_title": "Upload your lab report",
        "step2_desc": "PDF or photo of your lab results — Norya reads values and reference ranges.",
        "step3_title": "Get your explained report",
        "step3_desc": "Structured report with reference ranges and clear explanations. Ideal to prepare for your doctor visit.",
        "section_report_title": "What you see in your report",
        "report_ref": "Reference ranges for each value (normal / low / high).",
        "report_plain": "Plain-language explanations you can understand.",
        "report_highlights": "Key takeaways and points to discuss with your doctor.",
        "report_doctor_prep": "Preparation for your doctor visit — come with better questions.",
        "section_who_title": "Who is it for?",
        "who_1": "You want to understand your lab values better.",
        "who_2": "You want to prepare before your doctor appointment.",
        "who_3": "You need your report in another language.",
        "section_trust_title": "Security and transparency",
        "trust_dsgvo": "GDPR compliant. Data encrypted, not sold to third parties. Secure payment (PayTR), SSL.",
        "trust_disclaimer": "Norya does not provide a diagnosis. All content is for information and education only. Always consult a doctor for symptoms or treatment decisions.",
        "faq_title": "Frequently Asked Questions",
        "faq_q1": "How are lab results interpreted?",
        "faq_a1": "Norya compares your values to reference ranges and explains them in plain language. This is not a diagnosis—it's educational guidance.",
        "faq_q2": "Can I upload PDF or photo?",
        "faq_a2": "Yes. You can upload a PDF or a photo (JPG/PNG) of your lab report.",
        "faq_q3": "Does Norya give a diagnosis?",
        "faq_a3": "No. Norya only provides educational explanations. Diagnosis and treatment are for your doctor.",
        "section_cta_title": "Ready for your first report?",
        "cta_primary2": "Start analysis",
        "cta_secondary2": "View pricing",
        "related_title": "Related content",
        "related_1_label": "Blood test results",
        "related_1_path": "/en/blood-test-results",
        "related_2_label": "How it works",
        "related_2_path": "/how-it-works",
        "nav_home": "Home",
        "nav_how": "How it works",
        "nav_pricing": "Pricing",
        "nav_analyze": "Analyze",
        "nav_blog": "Blog",
        "footer_privacy": "Privacy",
        "footer_terms": "Terms of use",
    }


# (lang, slug) -> content dict
_SEO_LANDING_CONTENT = {
    ("tr", "kan-tahlili-sonucu"): _tr_kan_tahlili(),
    ("tr", "kan-degerleri-anlama"): _tr_kan_degerleri(),
    ("tr", "hemogram-sonucu"): _tr_hemogram(),
    ("de", "blutwerte-verstehen"): _de_blutwerte(),
    ("de", "laborwerte-verstehen"): _de_laborwerte(),
    ("en", "blood-test-results"): _en_blood_test_results(),
    ("en", "understand-lab-results"): _en_understand_lab_results(),
}


def is_seo_landing_route(lang: str, slug: str) -> bool:
    """True if (lang, slug) is a registered SEO landing page."""
    return (lang.strip().lower(), slug.strip().lower()) in SEO_LANDING_ROUTES


def get_seo_landing_content(lang: str, slug: str) -> dict | None:
    """Return full UI content for the SEO landing page (lang, slug). None if not a valid route."""
    key = (lang.strip().lower(), slug.strip().lower())
    return _SEO_LANDING_CONTENT.get(key)


def get_seo_landing_meta(lang: str, slug: str) -> dict:
    """Return meta_title, meta_description for the page. Uses get_seo_landing_content."""
    content = get_seo_landing_content(lang, slug)
    if not content:
        return {"meta_title": "Norya", "meta_description": ""}
    return {
        "meta_title": content.get("meta_title", "Norya"),
        "meta_description": content.get("meta_description", ""),
    }


def get_seo_landing_hreflang(lang: str, slug: str, base_url: str) -> list[dict]:
    """Return list of {lang, url} for hreflang alternates (including self and x-default)."""
    key = (lang.strip().lower(), slug.strip().lower())
    alternates = list(SEO_LANDING_HREFLANG.get(key, []))
    # Self
    self_url = f"{base_url}/{lang}/{slug}"
    out = [{"lang": lang, "url": self_url}]
    for lang_alt, slug_alt in alternates:
        out.append({"lang": lang_alt, "url": f"{base_url}/{lang_alt}/{slug_alt}"})
    # x-default: prefer en if available, else self
    default_slug = slug
    default_lang = lang
    for lang_alt, slug_alt in alternates:
        if lang_alt == "en":
            default_lang, default_slug = "en", slug_alt
            break
    out.append({"lang": "x-default", "url": f"{base_url}/{default_lang}/{default_slug}"})
    return out


def iter_seo_landing_urls() -> list[tuple[str, str]]:
    """Return [(lang, slug), ...] for all SEO landing pages (for sitemap)."""
    return sorted(SEO_LANDING_ROUTES)


def get_related_links(lang: str, base_url: str) -> list[dict]:
    """Return crawlable internal links: analyze, pricing, how-it-works, blog (for template)."""
    lang = lang.strip().lower()
    prefix = f"{base_url}/{lang}" if lang else base_url
    if lang == "tr":
        return [
            {"label": "Analiz Yap", "url": f"{base_url}/analyze"},
            {"label": "Fiyatlandırma", "url": f"{base_url}/pricing"},
            {"label": "Nasıl Çalışır", "url": f"{base_url}/how-it-works"},
            {"label": "Blog", "url": f"{prefix}/blog"},
        ]
    if lang == "de":
        return [
            {"label": "Analysieren", "url": f"{base_url}/analyze"},
            {"label": "Preise", "url": f"{base_url}/pricing"},
            {"label": "So funktioniert's", "url": f"{base_url}/how-it-works"},
            {"label": "Blog", "url": f"{prefix}/blog"},
        ]
    return [
        {"label": "Analyze", "url": f"{base_url}/analyze"},
        {"label": "Pricing", "url": f"{base_url}/pricing"},
        {"label": "How it works", "url": f"{base_url}/how-it-works"},
        {"label": "Blog", "url": f"{prefix}/blog"},
    ]
