# -*- coding: utf-8 -*-
"""
Compare pages i18n: multilingual competitor comparison system.

Central config for /{lang}/compare/ (hub) and /{lang}/compare/{slug} (detail)
across 9 locales and 5 competitors.

Architecture:
- Shared locale data (nav, CTA, why-norya, breadcrumbs) defined once per locale
- Comparison table labels and Norya column defined once per locale
- Competitor column defined per (locale, slug)
- Hub content defined per locale
- Detail content (meta, hero, verdict, helps, faqs) defined per (locale, slug)
- Builder functions compose shared + competitor-specific content at request time
"""
from __future__ import annotations

# ── Constants ──────────────────────────────────────────────────────────────

COMPARE_LANGS = ("en", "tr", "de", "fr", "it", "es", "he", "hi", "ar")

COMPETITOR_SLUGS = (
    "norya-vs-chatgpt-for-blood-tests",
    "norya-vs-kantesti",
    "norya-vs-siphox-health",
    "norya-vs-wizey",
    "norya-vs-generic-ai",
)

COMPETITOR_DISPLAY_NAMES: dict[str, str] = {
    "norya-vs-chatgpt-for-blood-tests": "ChatGPT",
    "norya-vs-kantesti": "Kantesti",
    "norya-vs-siphox-health": "SiPhox Health",
    "norya-vs-wizey": "Wizey",
    "norya-vs-generic-ai": "Generic AI",
}

OG_LOCALE_MAP: dict[str, str] = {
    "en": "en_US", "tr": "tr_TR", "de": "de_DE", "fr": "fr_FR",
    "it": "it_IT", "es": "es_ES", "he": "he_IL", "hi": "hi_IN", "ar": "ar_SA",
}

# ── Shared locale data ────────────────────────────────────────────────────
# Navigation labels, CTA copy, "Why Norya" section, breadcrumbs, footer
# shared across all compare pages in the same locale.

_SHARED: dict[str, dict] = {
    "en": {
        "nav_home": "Home",
        "nav_how": "How it works",
        "nav_pricing": "Pricing",
        "nav_blog": "Blog",
        "nav_analyze": "Analyze",
        "badge": "Honest comparison · NoryaAI",
        "comparison_title": "Side-by-side comparison",
        "why_norya_title": "Why people choose NoryaAI for blood tests",
        "why_norya_sub": "When accuracy, structure, and a clean next-step matter more than a general conversation.",
        "why_norya_items": [
            {"title": "Upload once, get a structured report", "desc": "No prompt engineering, no reformatting. Upload your lab results and receive a health score, category breakdown, and flagged markers — automatically."},
            {"title": "Consistent format you can compare over time", "desc": "Every report follows the same structure, so you can track changes across multiple blood tests and spot trends at a glance."},
            {"title": "Doctor-ready PDF you can actually bring", "desc": "A clean, professional summary with QR verification. Print it or share it digitally — designed to be useful at your next appointment."},
            {"title": "Your language, your report", "desc": "Choose from 9+ languages and get your full report in the one that feels most natural to you — with medical context intact."},
        ],
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "See a sample report",
        "cta_title": "Ready to try a structured blood test report?",
        "cta_sub": "Upload your lab results and see the difference a purpose-built analyzer makes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing plans",
        "faq_section_title": "Frequently Asked Questions",
        "footer_disclaimer": "NoryaAI does not provide medical diagnoses. All content is for educational and informational purposes only.",
        "breadcrumb_home": "Home",
        "breadcrumb_compare": "Compare",
        "related_title": "Related Comparisons",
    },
    "tr": {
        "nav_home": "Ana Sayfa",
        "nav_how": "Nasıl Çalışır",
        "nav_pricing": "Fiyatlar",
        "nav_blog": "Blog",
        "nav_analyze": "Analiz",
        "badge": "Dürüst karşılaştırma · NoryaAI",
        "comparison_title": "Yan yana karşılaştırma",
        "why_norya_title": "İnsanlar kan testi için neden NoryaAI'ı tercih ediyor",
        "why_norya_sub": "Doğruluk, yapı ve net bir sonraki adım genel bir sohbetten daha önemli olduğunda.",
        "why_norya_items": [
            {"title": "Bir kez yükle, yapılandırılmış rapor al", "desc": "Prompt mühendisliği yok, yeniden biçimlendirme yok. Laboratuvar sonuçlarınızı yükleyin; sağlık skoru, kategori dökümü ve işaretlenmiş belirteçler otomatik olarak gelsin."},
            {"title": "Zaman içinde karşılaştırabileceğiniz tutarlı format", "desc": "Her rapor aynı yapıyı takip eder, böylece birden fazla kan testindeki değişiklikleri takip edebilir ve eğilimleri bir bakışta görebilirsiniz."},
            {"title": "Gerçekten götürebileceğiniz doktora hazır PDF", "desc": "QR doğrulamalı temiz, profesyonel bir özet. Yazdırın veya dijital olarak paylaşın — bir sonraki randevunuzda kullanışlı olacak şekilde tasarlandı."},
            {"title": "Sizin diliniz, sizin raporunuz", "desc": "9+ dil arasından seçim yapın ve tam raporunuzu size en doğal gelen dilde alın — tıbbi bağlam korunarak."},
        ],
        "cta_hero_primary": "Kan tahlilimi analiz et",
        "cta_hero_secondary": "Örnek raporu gör",
        "cta_title": "Yapılandırılmış bir kan testi raporu denemeye hazır mısınız?",
        "cta_sub": "Laboratuvar sonuçlarınızı yükleyin ve amaca yönelik bir analizörün farkını görün.",
        "cta_primary": "Yükle ve analiz et",
        "cta_secondary": "Fiyatları görüntüle",
        "faq_section_title": "Sıkça Sorulan Sorular",
        "footer_disclaimer": "NoryaAI tıbbi teşhis sağlamaz. Tüm içerik yalnızca eğitim ve bilgilendirme amaçlıdır.",
        "breadcrumb_home": "Ana Sayfa",
        "breadcrumb_compare": "Karşılaştır",
        "related_title": "İlgili Karşılaştırmalar",
    },
    "de": {
        "nav_home": "Startseite",
        "nav_how": "So funktioniert's",
        "nav_pricing": "Preise",
        "nav_blog": "Blog",
        "nav_analyze": "Analysieren",
        "badge": "Ehrlicher Vergleich · NoryaAI",
        "comparison_title": "Direktvergleich",
        "why_norya_title": "Warum sich Menschen für NoryaAI entscheiden",
        "why_norya_sub": "Wenn Genauigkeit, Struktur und ein klarer nächster Schritt wichtiger sind als ein allgemeines Gespräch.",
        "why_norya_items": [
            {"title": "Einmal hochladen, strukturierten Bericht erhalten", "desc": "Kein Prompt-Engineering, keine Umformatierung. Laden Sie Ihre Laborergebnisse hoch und erhalten Sie automatisch einen Gesundheitsscore, eine Kategorieübersicht und markierte Marker."},
            {"title": "Konsistentes Format zum Vergleichen über die Zeit", "desc": "Jeder Bericht folgt derselben Struktur, sodass Sie Änderungen über mehrere Bluttests hinweg verfolgen und Trends auf einen Blick erkennen können."},
            {"title": "Arzt-taugliches PDF zum Mitnehmen", "desc": "Eine saubere, professionelle Zusammenfassung mit QR-Verifizierung. Drucken oder digital teilen — für Ihren nächsten Termin konzipiert."},
            {"title": "Ihre Sprache, Ihr Bericht", "desc": "Wählen Sie aus 9+ Sprachen und erhalten Sie Ihren vollständigen Bericht in der Sprache, die sich für Sie am natürlichsten anfühlt — mit erhaltenem medizinischem Kontext."},
        ],
        "cta_hero_primary": "Mein Blutbild analysieren",
        "cta_hero_secondary": "Beispielbericht ansehen",
        "cta_title": "Bereit für einen strukturierten Bluttest-Bericht?",
        "cta_sub": "Laden Sie Ihre Laborergebnisse hoch und erleben Sie den Unterschied.",
        "cta_primary": "Hochladen und analysieren",
        "cta_secondary": "Preise ansehen",
        "faq_section_title": "Häufig gestellte Fragen",
        "footer_disclaimer": "NoryaAI stellt keine medizinischen Diagnosen. Alle Inhalte dienen ausschließlich Bildungs- und Informationszwecken.",
        "breadcrumb_home": "Startseite",
        "breadcrumb_compare": "Vergleich",
        "related_title": "Weitere Vergleiche",
    },
    "fr": {
        "nav_home": "Accueil",
        "nav_how": "Comment ça marche",
        "nav_pricing": "Tarifs",
        "nav_blog": "Blog",
        "nav_analyze": "Analyser",
        "badge": "Comparaison honnête · NoryaAI",
        "comparison_title": "Comparaison côte à côte",
        "why_norya_title": "Pourquoi les gens choisissent NoryaAI pour les analyses de sang",
        "why_norya_sub": "Quand la précision, la structure et une prochaine étape claire comptent plus qu'une conversation générale.",
        "why_norya_items": [
            {"title": "Téléchargez une fois, obtenez un rapport structuré", "desc": "Pas de prompt engineering, pas de reformatage. Téléchargez vos résultats et recevez automatiquement un score de santé, une répartition par catégorie et des marqueurs signalés."},
            {"title": "Format cohérent pour comparer dans le temps", "desc": "Chaque rapport suit la même structure, vous permettant de suivre les changements et de repérer les tendances d'un coup d'œil."},
            {"title": "PDF prêt pour le médecin", "desc": "Un résumé propre et professionnel avec vérification QR. Imprimez-le ou partagez-le — conçu pour votre prochain rendez-vous."},
            {"title": "Votre langue, votre rapport", "desc": "Choisissez parmi 9+ langues et obtenez votre rapport complet dans celle qui vous est la plus naturelle — avec le contexte médical préservé."},
        ],
        "cta_hero_primary": "Analyser mon bilan sanguin",
        "cta_hero_secondary": "Voir un exemple de rapport",
        "cta_title": "Prêt à essayer un rapport d'analyse structuré ?",
        "cta_sub": "Téléchargez vos résultats et découvrez la différence d'un analyseur dédié.",
        "cta_primary": "Télécharger et analyser",
        "cta_secondary": "Voir les tarifs",
        "faq_section_title": "Questions fréquemment posées",
        "footer_disclaimer": "NoryaAI ne fournit pas de diagnostics médicaux. Tout le contenu est à des fins éducatives et informatives uniquement.",
        "breadcrumb_home": "Accueil",
        "breadcrumb_compare": "Comparer",
        "related_title": "Comparaisons associées",
    },
    "it": {
        "nav_home": "Home",
        "nav_how": "Come funziona",
        "nav_pricing": "Prezzi",
        "nav_blog": "Blog",
        "nav_analyze": "Analizza",
        "badge": "Confronto onesto · NoryaAI",
        "comparison_title": "Confronto diretto",
        "why_norya_title": "Perché le persone scelgono NoryaAI per le analisi del sangue",
        "why_norya_sub": "Quando precisione, struttura e un chiaro passo successivo contano più di una conversazione generica.",
        "why_norya_items": [
            {"title": "Carica una volta, ottieni un referto strutturato", "desc": "Nessun prompt engineering, nessuna riformattazione. Carica i tuoi risultati e ricevi automaticamente un punteggio di salute, una suddivisione per categoria e marcatori segnalati."},
            {"title": "Formato coerente per confronti nel tempo", "desc": "Ogni referto segue la stessa struttura, così puoi monitorare i cambiamenti e individuare le tendenze a colpo d'occhio."},
            {"title": "PDF pronto per il medico", "desc": "Un riepilogo pulito e professionale con verifica QR. Stampalo o condividilo — progettato per il tuo prossimo appuntamento."},
            {"title": "La tua lingua, il tuo referto", "desc": "Scegli tra 9+ lingue e ottieni il tuo referto completo nella lingua più naturale per te — con il contesto medico preservato."},
        ],
        "cta_hero_primary": "Analizza le mie analisi",
        "cta_hero_secondary": "Vedi un referto esempio",
        "cta_title": "Pronto a provare un referto strutturato?",
        "cta_sub": "Carica i tuoi risultati e scopri la differenza di un analizzatore dedicato.",
        "cta_primary": "Carica e analizza",
        "cta_secondary": "Vedi i prezzi",
        "faq_section_title": "Domande frequenti",
        "footer_disclaimer": "NoryaAI non fornisce diagnosi mediche. Tutti i contenuti sono solo a scopo educativo e informativo.",
        "breadcrumb_home": "Home",
        "breadcrumb_compare": "Confronto",
        "related_title": "Confronti correlati",
    },
    "es": {
        "nav_home": "Inicio",
        "nav_how": "Cómo funciona",
        "nav_pricing": "Precios",
        "nav_blog": "Blog",
        "nav_analyze": "Analizar",
        "badge": "Comparación honesta · NoryaAI",
        "comparison_title": "Comparación lado a lado",
        "why_norya_title": "Por qué la gente elige NoryaAI para análisis de sangre",
        "why_norya_sub": "Cuando la precisión, la estructura y un siguiente paso claro importan más que una conversación general.",
        "why_norya_items": [
            {"title": "Sube una vez, obtén un informe estructurado", "desc": "Sin ingeniería de prompts, sin reformateo. Sube tus resultados y recibe automáticamente una puntuación de salud, desglose por categoría y marcadores señalados."},
            {"title": "Formato consistente para comparar a lo largo del tiempo", "desc": "Cada informe sigue la misma estructura, para que puedas rastrear cambios y detectar tendencias de un vistazo."},
            {"title": "PDF listo para el médico", "desc": "Un resumen limpio y profesional con verificación QR. Imprímelo o compártelo — diseñado para tu próxima cita."},
            {"title": "Tu idioma, tu informe", "desc": "Elige entre 9+ idiomas y obtén tu informe completo en el que te resulte más natural — con el contexto médico preservado."},
        ],
        "cta_hero_primary": "Analizar mi análisis de sangre",
        "cta_hero_secondary": "Ver informe de ejemplo",
        "cta_title": "¿Listo para probar un informe estructurado?",
        "cta_sub": "Sube tus resultados y descubre la diferencia de un analizador dedicado.",
        "cta_primary": "Subir y analizar",
        "cta_secondary": "Ver precios",
        "faq_section_title": "Preguntas frecuentes",
        "footer_disclaimer": "NoryaAI no proporciona diagnósticos médicos. Todo el contenido es solo con fines educativos e informativos.",
        "breadcrumb_home": "Inicio",
        "breadcrumb_compare": "Comparar",
        "related_title": "Comparaciones relacionadas",
    },
    "he": {
        "nav_home": "דף הבית",
        "nav_how": "איך זה עובד",
        "nav_pricing": "מחירים",
        "nav_blog": "בלוג",
        "nav_analyze": "ניתוח",
        "badge": "השוואה כנה · NoryaAI",
        "comparison_title": "השוואה זה מול זה",
        "why_norya_title": "למה אנשים בוחרים ב-NoryaAI לבדיקות דם",
        "why_norya_sub": "כשדיוק, מבנה וצעד הבא ברור חשובים יותר משיחה כללית.",
        "why_norya_items": [
            {"title": "העלו פעם אחת, קבלו דוח מובנה", "desc": "ללא הנדסת פרומפטים, ללא עיצוב מחדש. העלו את תוצאות המעבדה וקבלו אוטומטית ציון בריאות, פירוט לפי קטגוריה וסמנים מסומנים."},
            {"title": "פורמט עקבי להשוואה לאורך זמן", "desc": "כל דוח עוקב אחר אותו מבנה, כך שתוכלו לעקוב אחר שינויים ולזהות מגמות במבט אחד."},
            {"title": "PDF מוכן לרופא", "desc": "סיכום נקי ומקצועי עם אימות QR. הדפיסו או שתפו דיגיטלית — מעוצב לתור הבא שלכם."},
            {"title": "השפה שלכם, הדוח שלכם", "desc": "בחרו מבין 9+ שפות וקבלו את הדוח המלא בשפה הטבעית ביותר עבורכם — עם שימור ההקשר הרפואי."},
        ],
        "cta_hero_primary": "נתחו את בדיקת הדם שלי",
        "cta_hero_secondary": "ראו דוח לדוגמה",
        "cta_title": "מוכנים לנסות דוח בדיקת דם מובנה?",
        "cta_sub": "העלו את תוצאות המעבדה וגלו את ההבדל של מנתח ייעודי.",
        "cta_primary": "העלו ונתחו עכשיו",
        "cta_secondary": "צפו במחירים",
        "faq_section_title": "שאלות נפוצות",
        "footer_disclaimer": "NoryaAI אינו מספק אבחנות רפואיות. כל התוכן הוא למטרות חינוכיות ומידעיות בלבד.",
        "breadcrumb_home": "דף הבית",
        "breadcrumb_compare": "השוואה",
        "related_title": "השוואות נוספות",
    },
    "hi": {
        "nav_home": "होम",
        "nav_how": "यह कैसे काम करता है",
        "nav_pricing": "कीमतें",
        "nav_blog": "ब्लॉग",
        "nav_analyze": "विश्लेषण",
        "badge": "ईमानदार तुलना · NoryaAI",
        "comparison_title": "आमने-सामने की तुलना",
        "why_norya_title": "लोग रक्त परीक्षण के लिए NoryaAI क्यों चुनते हैं",
        "why_norya_sub": "जब सटीकता, संरचना और एक स्पष्ट अगला कदम सामान्य बातचीत से ज़्यादा मायने रखते हैं।",
        "why_norya_items": [
            {"title": "एक बार अपलोड करें, संरचित रिपोर्ट पाएं", "desc": "कोई प्रॉम्प्ट इंजीनियरिंग नहीं, कोई रीफॉर्मेटिंग नहीं। अपने लैब परिणाम अपलोड करें और स्वचालित रूप से स्वास्थ्य स्कोर, श्रेणी विभाजन और चिह्नित मार्कर प्राप्त करें।"},
            {"title": "समय के साथ तुलना के लिए सुसंगत प्रारूप", "desc": "हर रिपोर्ट एक ही संरचना का पालन करती है, ताकि आप कई रक्त परीक्षणों में बदलावों को ट्रैक कर सकें और एक नज़र में रुझान देख सकें।"},
            {"title": "डॉक्टर-रेडी PDF जो आप वास्तव में ले जा सकते हैं", "desc": "QR सत्यापन के साथ एक साफ, पेशेवर सारांश। इसे प्रिंट करें या डिजिटल रूप से साझा करें — आपकी अगली अपॉइंटमेंट के लिए डिज़ाइन किया गया।"},
            {"title": "आपकी भाषा, आपकी रिपोर्ट", "desc": "9+ भाषाओं में से चुनें और अपनी पूरी रिपोर्ट उस भाषा में प्राप्त करें जो आपके लिए सबसे स्वाभाविक हो — चिकित्सा संदर्भ बरकरार।"},
        ],
        "cta_hero_primary": "मेरा रक्त परीक्षण विश्लेषण करें",
        "cta_hero_secondary": "नमूना रिपोर्ट देखें",
        "cta_title": "एक संरचित रक्त परीक्षण रिपोर्ट आज़माने के लिए तैयार हैं?",
        "cta_sub": "अपने लैब परिणाम अपलोड करें और एक समर्पित विश्लेषक का अंतर देखें।",
        "cta_primary": "अपलोड करें और विश्लेषण करें",
        "cta_secondary": "कीमतें देखें",
        "faq_section_title": "अक्सर पूछे जाने वाले प्रश्न",
        "footer_disclaimer": "NoryaAI चिकित्सा निदान प्रदान नहीं करता। सभी सामग्री केवल शैक्षिक और सूचनात्मक उद्देश्यों के लिए है।",
        "breadcrumb_home": "होम",
        "breadcrumb_compare": "तुलना",
        "related_title": "संबंधित तुलनाएँ",
    },
    "ar": {
        "nav_home": "الرئيسية",
        "nav_how": "كيف يعمل",
        "nav_pricing": "الأسعار",
        "nav_blog": "المدوّنة",
        "nav_analyze": "تحليل",
        "badge": "مقارنة صادقة · NoryaAI",
        "comparison_title": "مقارنة جنبًا إلى جنب",
        "why_norya_title": "لماذا يختار الناس NoryaAI لفحوصات الدم",
        "why_norya_sub": "عندما تكون الدقة والبنية والخطوة التالية الواضحة أهم من محادثة عامة.",
        "why_norya_items": [
            {"title": "حمّل مرة واحدة واحصل على تقرير منظم", "desc": "بدون هندسة برومبت، بدون إعادة تنسيق. حمّل نتائج مختبرك واحصل تلقائيًا على نقاط صحية وتصنيف حسب الفئة وعلامات محددة."},
            {"title": "تنسيق متسق للمقارنة عبر الزمن", "desc": "كل تقرير يتبع نفس الهيكل، حتى تتمكن من تتبع التغييرات واكتشاف الاتجاهات بنظرة واحدة."},
            {"title": "PDF جاهز للطبيب يمكنك إحضاره فعلاً", "desc": "ملخص نظيف واحترافي مع التحقق بـ QR. اطبعه أو شاركه رقميًا — مصمم لموعدك القادم."},
            {"title": "لغتك، تقريرك", "desc": "اختر من بين 9+ لغات واحصل على تقريرك الكامل باللغة الأكثر طبيعية لك — مع الحفاظ على السياق الطبي."},
        ],
        "cta_hero_primary": "حلّل فحص دمي",
        "cta_hero_secondary": "شاهد تقريرًا نموذجيًا",
        "cta_title": "مستعد لتجربة تقرير فحص دم منظم؟",
        "cta_sub": "حمّل نتائج مختبرك واكتشف الفرق الذي يحدثه محلل مخصص.",
        "cta_primary": "حمّل وحلّل الآن",
        "cta_secondary": "عرض الأسعار",
        "faq_section_title": "الأسئلة الشائعة",
        "footer_disclaimer": "NoryaAI لا يقدم تشخيصات طبية. جميع المحتويات لأغراض تعليمية ومعلوماتية فقط.",
        "breadcrumb_home": "الرئيسية",
        "breadcrumb_compare": "مقارنة",
        "related_title": "مقارنات ذات صلة",
    },
}

# ── Comparison table: labels and Norya column (shared across competitors) ──

_COMPARISON_LABELS: dict[str, list[str]] = {
    "en": ["Report upload", "Reference ranges", "Units and lab formatting", "Output structure", "Multilingual reports", "Doctor-ready summary", "Privacy and data handling", "Blood-test specific workflow", "Workflow type"],
    "tr": ["Rapor yükleme", "Referans aralıkları", "Birim ve laboratuvar formatı", "Çıktı yapısı", "Çok dilli raporlar", "Doktora hazır özet", "Gizlilik ve veri yönetimi", "Kan testine özel iş akışı", "İş akışı türü"],
    "de": ["Bericht-Upload", "Referenzbereiche", "Einheiten und Laborformat", "Ausgabestruktur", "Mehrsprachige Berichte", "Arzt-taugliche Zusammenfassung", "Datenschutz und Datenverarbeitung", "Bluttest-spezifischer Workflow", "Workflow-Typ"],
    "fr": ["Téléchargement du rapport", "Plages de référence", "Unités et format de laboratoire", "Structure de sortie", "Rapports multilingues", "Résumé prêt pour le médecin", "Confidentialité et traitement des données", "Flux spécifique analyses de sang", "Type de flux de travail"],
    "it": ["Caricamento referto", "Intervalli di riferimento", "Unità e formato del laboratorio", "Struttura dell'output", "Referti multilingue", "Riepilogo pronto per il medico", "Privacy e gestione dei dati", "Flusso specifico analisi del sangue", "Tipo di flusso di lavoro"],
    "es": ["Carga de informe", "Rangos de referencia", "Unidades y formato de laboratorio", "Estructura de salida", "Informes multilingües", "Resumen listo para el médico", "Privacidad y manejo de datos", "Flujo específico para análisis de sangre", "Tipo de flujo de trabajo"],
    "he": ["העלאת דוח", "טווחי ייחוס", "יחידות ופורמט מעבדה", "מבנה הפלט", "דוחות רב-לשוניים", "סיכום מוכן לרופא", "פרטיות וטיפול בנתונים", "תהליך ייעודי לבדיקות דם", "סוג תהליך העבודה"],
    "hi": ["रिपोर्ट अपलोड", "संदर्भ श्रेणियाँ", "इकाइयाँ और लैब फॉर्मेट", "आउटपुट संरचना", "बहुभाषी रिपोर्ट", "डॉक्टर-रेडी सारांश", "गोपनीयता और डेटा प्रबंधन", "रक्त परीक्षण विशिष्ट वर्कफ़्लो", "वर्कफ़्लो का प्रकार"],
    "ar": ["تحميل التقرير", "النطاقات المرجعية", "الوحدات وتنسيق المختبر", "بنية المخرجات", "تقارير متعددة اللغات", "ملخص جاهز للطبيب", "الخصوصية ومعالجة البيانات", "سير عمل مخصص لفحوصات الدم", "نوع سير العمل"],
}

_NORYA_SIDE: dict[str, list[str]] = {
    "en": [
        "Upload PDF, snap a photo, or paste text — values and ranges are parsed automatically",
        "Reference ranges displayed for every value — normal, low, or high — clearly labeled",
        "Recognizes common lab units, panel structures, and result formats automatically",
        "Structured health score, category breakdown, and flagged markers — consistent every time",
        "Full reports in 9+ languages with medical context preserved throughout",
        "Doctor-ready PDF with QR verification — print it, save it, or share it",
        "GDPR/KVKK compliant — encrypted, never sold, never used for training",
        "Dedicated upload, analysis, and report pipeline built specifically for lab results",
        "Guided, structured analysis — upload once and get a complete report, no prompt needed",
    ],
    "tr": [
        "PDF yükleyin, fotoğraf çekin veya metin yapıştırın — değerler ve aralıklar otomatik olarak ayrıştırılır",
        "Her değer için referans aralıkları gösterilir — normal, düşük veya yüksek — açıkça etiketlenir",
        "Yaygın laboratuvar birimlerini, panel yapılarını ve sonuç formatlarını otomatik olarak tanır",
        "Yapılandırılmış sağlık skoru, kategori dökümü ve işaretlenmiş belirteçler — her seferinde tutarlı",
        "Tıbbi bağlam korunarak 9+ dilde tam raporlar",
        "QR doğrulamalı doktora hazır PDF — yazdırın, kaydedin veya paylaşın",
        "GDPR/KVKK uyumlu — şifreli, satılmaz, eğitim için kullanılmaz",
        "Özellikle laboratuvar sonuçları için tasarlanmış yükleme, analiz ve rapor hattı",
        "Yönlendirilmiş, yapılandırılmış analiz — bir kez yükleyin, eksiksiz rapor alın, prompt gerekmez",
    ],
    "de": [
        "PDF hochladen, Foto aufnehmen oder Text einfügen — Werte und Bereiche werden automatisch erfasst",
        "Referenzbereiche für jeden Wert angezeigt — normal, niedrig oder hoch — klar gekennzeichnet",
        "Erkennt gängige Laboreinheiten, Panelstrukturen und Ergebnisformate automatisch",
        "Strukturierter Gesundheitsscore, Kategorieübersicht und markierte Marker — jedes Mal konsistent",
        "Vollständige Berichte in 9+ Sprachen mit erhaltenem medizinischem Kontext",
        "Arzt-taugliches PDF mit QR-Verifizierung — drucken, speichern oder teilen",
        "DSGVO/KVKK-konform — verschlüsselt, niemals verkauft, niemals für Training verwendet",
        "Dedizierte Upload-, Analyse- und Berichtspipeline speziell für Laborergebnisse",
        "Geführte, strukturierte Analyse — einmal hochladen, vollständigen Bericht erhalten, kein Prompt nötig",
    ],
    "fr": [
        "Téléchargez un PDF, prenez une photo ou collez du texte — les valeurs et plages sont analysées automatiquement",
        "Plages de référence affichées pour chaque valeur — normal, bas ou élevé — clairement indiquées",
        "Reconnaît automatiquement les unités courantes, les structures de panels et les formats de résultats",
        "Score de santé structuré, répartition par catégorie et marqueurs signalés — cohérent à chaque fois",
        "Rapports complets en 9+ langues avec contexte médical préservé",
        "PDF prêt pour le médecin avec vérification QR — imprimez, enregistrez ou partagez",
        "Conforme RGPD/KVKK — chiffré, jamais vendu, jamais utilisé pour l'entraînement",
        "Pipeline dédiée de téléchargement, d'analyse et de rapport pour les résultats de laboratoire",
        "Analyse guidée et structurée — téléchargez une fois, obtenez un rapport complet, sans prompt",
    ],
    "it": [
        "Carica un PDF, scatta una foto o incolla il testo — valori e intervalli vengono analizzati automaticamente",
        "Intervalli di riferimento visualizzati per ogni valore — normale, basso o alto — chiaramente etichettati",
        "Riconosce automaticamente unità di laboratorio comuni, strutture dei pannelli e formati dei risultati",
        "Punteggio di salute strutturato, suddivisione per categoria e marcatori segnalati — coerente ogni volta",
        "Referti completi in 9+ lingue con contesto medico preservato",
        "PDF pronto per il medico con verifica QR — stampa, salva o condividi",
        "Conforme GDPR/KVKK — crittografato, mai venduto, mai usato per l'addestramento",
        "Pipeline dedicata di caricamento, analisi e report per i risultati di laboratorio",
        "Analisi guidata e strutturata — carica una volta, ottieni un report completo, senza prompt",
    ],
    "es": [
        "Sube un PDF, toma una foto o pega texto — los valores y rangos se analizan automáticamente",
        "Rangos de referencia mostrados para cada valor — normal, bajo o alto — claramente etiquetados",
        "Reconoce automáticamente unidades de laboratorio comunes, estructuras de paneles y formatos de resultados",
        "Puntuación de salud estructurada, desglose por categoría y marcadores señalados — consistente cada vez",
        "Informes completos en 9+ idiomas con contexto médico preservado",
        "PDF listo para el médico con verificación QR — imprímelo, guárdalo o compártelo",
        "Cumple con RGPD/KVKK — cifrado, nunca vendido, nunca utilizado para entrenamiento",
        "Pipeline dedicada de carga, análisis e informes para resultados de laboratorio",
        "Análisis guiado y estructurado — sube una vez, obtén un informe completo, sin necesidad de prompt",
    ],
    "he": [
        "העלו PDF, צלמו תמונה או הדביקו טקסט — ערכים וטווחים מנותחים אוטומטית",
        "טווחי ייחוס מוצגים לכל ערך — תקין, נמוך או גבוה — מסומנים בבירור",
        "מזהה אוטומטית יחידות מעבדה נפוצות, מבני פאנלים ופורמטים של תוצאות",
        "ציון בריאות מובנה, פירוט לפי קטגוריה וסמנים מסומנים — עקבי בכל פעם",
        "דוחות מלאים ב-9+ שפות עם שימור הקשר רפואי",
        "PDF מוכן לרופא עם אימות QR — הדפיסו, שמרו או שתפו",
        "תואם GDPR/KVKK — מוצפן, לעולם לא נמכר, לעולם לא משמש לאימון",
        "צנרת ייעודית להעלאה, ניתוח ודוח שנבנתה במיוחד לתוצאות מעבדה",
        "ניתוח מונחה ומובנה — העלו פעם אחת וקבלו דוח מלא, ללא צורך בפרומפט",
    ],
    "hi": [
        "PDF अपलोड करें, फ़ोटो लें या टेक्स्ट पेस्ट करें — मान और श्रेणियाँ स्वचालित रूप से पार्स होती हैं",
        "प्रत्येक मान के लिए संदर्भ श्रेणियाँ प्रदर्शित — सामान्य, कम या उच्च — स्पष्ट रूप से लेबल",
        "सामान्य लैब इकाइयों, पैनल संरचनाओं और परिणाम प्रारूपों को स्वचालित रूप से पहचानता है",
        "संरचित स्वास्थ्य स्कोर, श्रेणी विभाजन और चिह्नित मार्कर — हर बार सुसंगत",
        "चिकित्सा संदर्भ के साथ 9+ भाषाओं में पूर्ण रिपोर्ट",
        "QR सत्यापन के साथ डॉक्टर-रेडी PDF — प्रिंट करें, सेव करें या साझा करें",
        "GDPR/KVKK अनुपालन — एन्क्रिप्टेड, कभी बेचा नहीं, प्रशिक्षण के लिए कभी उपयोग नहीं",
        "विशेष रूप से लैब परिणामों के लिए निर्मित समर्पित अपलोड, विश्लेषण और रिपोर्ट पाइपलाइन",
        "मार्गदर्शित, संरचित विश्लेषण — एक बार अपलोड करें, पूरी रिपोर्ट प्राप्त करें, कोई प्रॉम्प्ट नहीं",
    ],
    "ar": [
        "حمّل ملف PDF أو التقط صورة أو الصق نصًا — يتم تحليل القيم والنطاقات تلقائيًا",
        "نطاقات مرجعية معروضة لكل قيمة — طبيعي أو منخفض أو مرتفع — بعلامات واضحة",
        "يتعرف تلقائيًا على وحدات المختبر الشائعة وهياكل اللوحات وتنسيقات النتائج",
        "نقاط صحية منظمة وتصنيف حسب الفئة وعلامات محددة — متسق في كل مرة",
        "تقارير كاملة بأكثر من 9 لغات مع الحفاظ على السياق الطبي",
        "ملف PDF جاهز للطبيب مع التحقق بـ QR — اطبعه أو احفظه أو شاركه",
        "متوافق مع GDPR/KVKK — مشفر، لا يُباع أبدًا، لا يُستخدم للتدريب أبدًا",
        "خط أنابيب مخصص للتحميل والتحليل والتقارير مصمم خصيصًا لنتائج المختبر",
        "تحليل موجه ومنظم — حمّل مرة واحدة واحصل على تقرير كامل، بدون حاجة لبرومبت",
    ],
}

# Competitor-side comparison rows per (lang, slug)
_COMPETITOR_SIDE: dict[tuple[str, str], list[str]] = {
    # ── ChatGPT ──
    ("en", "norya-vs-chatgpt-for-blood-tests"): [
        "Copy-paste values into a chat prompt and hope the formatting holds",
        "May guess ranges or omit them; no guarantee they match your lab's standards",
        "No built-in awareness of lab-specific units or result layouts",
        "Free-form paragraph that varies with each prompt — no consistent format",
        "Can translate text, but medical nuance may be lost in general translation",
        "No downloadable report — you would need to copy and format the chat yourself",
        "Conversations may be stored and used for model training",
        "General-purpose chat interface designed for any topic",
        "Open-ended conversation — the quality depends on how you write your prompt",
    ],
    ("tr", "norya-vs-chatgpt-for-blood-tests"): [
        "Değerleri bir sohbet istemine kopyalayıp yapıştırın ve formatın korunmasını umun",
        "Aralıkları tahmin edebilir veya atlayabilir; laboratuvarınızın standartlarıyla eşleşme garantisi yok",
        "Laboratuvara özgü birimler veya sonuç düzenleri konusunda yerleşik bir farkındalığı yok",
        "Her istemde değişen serbest biçimli paragraf — tutarlı bir format yok",
        "Metni çevirebilir, ancak genel çeviride tıbbi nüans kaybolabilir",
        "İndirilebilir rapor yok — sohbeti kendiniz kopyalayıp biçimlendirmeniz gerekir",
        "Konuşmalar model eğitimi için saklanabilir ve kullanılabilir",
        "Her konu için tasarlanmış genel amaçlı sohbet arayüzü",
        "Açık uçlu sohbet — kalite, isteminizi nasıl yazdığınıza bağlıdır",
    ],
    # ── Kantesti ──
    ("en", "norya-vs-kantesti"): [
        "Web-based form entry for test values — manual input required",
        "Basic reference range display for common blood markers",
        "Standard Turkish lab units supported; international format support not clearly disclosed",
        "Basic interpretation of individual values — limited structured output",
        "Primarily Turkish language interface; multilingual support not clearly disclosed",
        "On-screen results — downloadable doctor-ready PDF not clearly disclosed",
        "Data handling practices not clearly disclosed on public-facing pages",
        "Focused on lab test interpretation with a web-based interface",
        "Manual value entry with basic explanations — no automated parsing from lab reports",
    ],
    ("tr", "norya-vs-kantesti"): [
        "Test değerleri için web tabanlı form girişi — manuel giriş gerekli",
        "Yaygın kan belirteçleri için temel referans aralığı gösterimi",
        "Standart Türk laboratuvar birimleri desteklenir; uluslararası format desteği açıkça belirtilmemiş",
        "Bireysel değerlerin temel yorumlanması — sınırlı yapılandırılmış çıktı",
        "Öncelikle Türkçe dil arayüzü; çok dilli destek açıkça belirtilmemiş",
        "Ekran üzerinde sonuçlar — indirilebilir doktora hazır PDF açıkça belirtilmemiş",
        "Veri işleme uygulamaları kamuya açık sayfalarda açıkça belirtilmemiş",
        "Web tabanlı arayüz ile laboratuvar testi yorumlamaya odaklı",
        "Temel açıklamalarla manuel değer girişi — laboratuvar raporlarından otomatik ayrıştırma yok",
    ],
    # ── SiPhox Health ──
    ("en", "norya-vs-siphox-health"): [
        "Results delivered through the SiPhox app after using their fingerprick test kit",
        "Reference ranges provided for SiPhox-specific test panels",
        "Standardized units within the SiPhox ecosystem",
        "Results displayed in the SiPhox app with basic interpretation",
        "Primarily English interface; multilingual report output not clearly disclosed",
        "Results accessible in-app — exportable doctor-ready PDF format not clearly disclosed",
        "Health data stored within SiPhox platform; detailed retention policies on their site",
        "At-home blood testing service — requires purchasing their specific test kit",
        "Order kit → collect sample → mail back → receive results — multi-day turnaround",
    ],
    ("tr", "norya-vs-siphox-health"): [
        "Parmaktan kan alma kiti kullandıktan sonra SiPhox uygulaması üzerinden sonuçlar iletilir",
        "SiPhox'a özgü test panelleri için referans aralıkları sağlanır",
        "SiPhox ekosistemi içinde standartlaştırılmış birimler",
        "Sonuçlar temel yorumlamayla SiPhox uygulamasında görüntülenir",
        "Öncelikle İngilizce arayüz; çok dilli rapor çıktısı açıkça belirtilmemiş",
        "Sonuçlara uygulama içinden erişilebilir — indirilebilir doktora hazır PDF formatı açıkça belirtilmemiş",
        "Sağlık verileri SiPhox platformunda saklanır; ayrıntılı saklama politikaları sitelerinde",
        "Evde kan testi hizmeti — kendi test kitlerinin satın alınmasını gerektirir",
        "Kit sipariş et → numune topla → geri gönder → sonuçları al — birkaç günlük süreç",
    ],
    # ── Wizey ──
    ("en", "norya-vs-wizey"): [
        "Upload or connect health data from various sources",
        "Reference range handling not clearly disclosed in public materials",
        "Unit handling and format recognition not clearly disclosed",
        "AI-generated health insights based on uploaded data",
        "Multilingual report output not clearly disclosed",
        "Downloadable report format not clearly disclosed",
        "Data handling and privacy practices described on their platform",
        "General health data interpretation — not exclusively focused on blood tests",
        "Data-upload approach with AI interpretation — specific workflow varies by data type",
    ],
    ("tr", "norya-vs-wizey"): [
        "Çeşitli kaynaklardan sağlık verilerini yükleyin veya bağlayın",
        "Referans aralığı yönetimi kamuya açık materyallerde açıkça belirtilmemiş",
        "Birim yönetimi ve format tanıma açıkça belirtilmemiş",
        "Yüklenen verilere dayalı yapay zeka destekli sağlık içgörüleri",
        "Çok dilli rapor çıktısı açıkça belirtilmemiş",
        "İndirilebilir rapor formatı açıkça belirtilmemiş",
        "Veri işleme ve gizlilik uygulamaları platformlarında açıklanmıştır",
        "Genel sağlık verisi yorumlama — yalnızca kan testlerine odaklanmış değil",
        "Yapay zeka yorumlamalı veri yükleme yaklaşımı — iş akışı veri türüne göre değişir",
    ],
    # ── Generic AI ──
    ("en", "norya-vs-generic-ai"): [
        "Copy-paste values into a chat prompt and hope the formatting holds",
        "May guess ranges or omit them; no guarantee they match your lab's standards",
        "No built-in awareness of lab-specific units or result layouts",
        "Free-form paragraph that varies with each prompt — no consistent format",
        "Can translate text, but medical nuance may be lost in general translation",
        "No downloadable report — you would need to copy and format the chat yourself",
        "Conversations may be stored and used for model training",
        "General-purpose chat interface designed for any topic",
        "Open-ended conversation — the quality depends on how you write your prompt",
    ],
    ("tr", "norya-vs-generic-ai"): [
        "Değerleri bir sohbet istemine kopyalayıp yapıştırın ve formatın korunmasını umun",
        "Aralıkları tahmin edebilir veya atlayabilir; laboratuvarınızın standartlarıyla eşleşme garantisi yok",
        "Laboratuvara özgü birimler veya sonuç düzenleri konusunda yerleşik bir farkındalığı yok",
        "Her istemde değişen serbest biçimli paragraf — tutarlı bir format yok",
        "Metni çevirebilir, ancak genel çeviride tıbbi nüans kaybolabilir",
        "İndirilebilir rapor yok — sohbeti kendiniz kopyalayıp biçimlendirmeniz gerekir",
        "Konuşmalar model eğitimi için saklanabilir ve kullanılabilir",
        "Her konu için tasarlanmış genel amaçlı sohbet arayüzü",
        "Açık uçlu sohbet — kalite, isteminizi nasıl yazdığınıza bağlıdır",
    ],
}

# ── Hub page content per locale ────────────────────────────────────────────

_HUB: dict[str, dict] = {
    "en": {
        "meta_title": "Compare NoryaAI — Blood Test Analyzer vs Alternatives | NoryaAI",
        "meta_description": "Honest, side-by-side comparisons of NoryaAI with ChatGPT, Kantesti, SiPhox Health, Wizey, and other AI tools for blood test analysis.",
        "hero_title": "How NoryaAI Compares to Other Blood Test Tools",
        "hero_sub": "We believe in transparency. These pages offer honest, side-by-side comparisons so you can decide which tool fits your needs.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "General-purpose AI chatbot. Great for explaining medical terms — but not built for structured blood test reports."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Turkish lab test interpretation platform. Focused on the local market with basic test value explanations."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "At-home blood testing service with their own test kits. Norya analyzes the results you already have."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "AI-powered health data interpretation tool. Handles various data types with a different analysis approach."},
            {"slug": "norya-vs-generic-ai", "name": "Generic AI Chatbots", "summary": "ChatGPT, Claude, Gemini and others. How conversational AI compares to a dedicated blood test analyzer."},
        ],
        "cards_cta": "Read full comparison",
        "hub_faqs": [
            {"q": "Which tool is best for understanding blood test results?", "a": "It depends on your needs. If you want a structured, consistent report with health scores, flagged markers, and a doctor-ready PDF, NoryaAI is purpose-built for that. If you need general medical information or have questions beyond lab results, a general AI chatbot may complement your workflow."},
            {"q": "Can AI chatbots replace a dedicated blood test analyzer?", "a": "General AI chatbots can explain medical terms and answer health questions, but they do not parse lab reports, map values to reference ranges, or produce consistent structured reports. A dedicated tool like NoryaAI is designed specifically for this workflow."},
            {"q": "Is NoryaAI free to use?", "a": "NoryaAI offers a free analysis so you can see how it works. Additional analyses are available through affordable pricing plans. Visit the pricing page for details."},
        ],
    },
    "tr": {
        "meta_title": "NoryaAI Karşılaştırma — Kan Tahlili Analiz Araçları | NoryaAI",
        "meta_description": "NoryaAI ile ChatGPT, Kantesti, SiPhox Health, Wizey ve diğer yapay zeka araçlarının kan tahlili analizi için dürüst, yan yana karşılaştırmaları.",
        "hero_title": "NoryaAI Diğer Kan Tahlili Araçlarıyla Nasıl Karşılaştırılır?",
        "hero_sub": "Şeffaflığa inanıyoruz. Bu sayfalar, ihtiyaçlarınıza en uygun aracı seçmeniz için dürüst, yan yana karşılaştırmalar sunar.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Genel amaçlı yapay zeka sohbet robotu. Tıbbi terimleri açıklamak için harika — ancak yapılandırılmış kan testi raporları için tasarlanmamış."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Türk laboratuvar testi yorumlama platformu. Temel test değeri açıklamalarıyla yerel pazara odaklı."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Kendi test kitleriyle evde kan testi hizmeti. Norya ise zaten elinizdeki sonuçları analiz eder."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "Yapay zeka destekli sağlık verisi yorumlama aracı. Farklı bir analiz yaklaşımıyla çeşitli veri türlerini işler."},
            {"slug": "norya-vs-generic-ai", "name": "Genel Yapay Zeka", "summary": "ChatGPT, Claude, Gemini ve diğerleri. Sohbet yapay zekasının özel bir kan tahlili analizörüyle karşılaştırması."},
        ],
        "cards_cta": "Tam karşılaştırmayı oku",
        "hub_faqs": [
            {"q": "Kan tahlili sonuçlarını anlamak için en iyi araç hangisi?", "a": "İhtiyaçlarınıza bağlıdır. Sağlık skoru, işaretlenmiş belirteçler ve doktora hazır PDF ile yapılandırılmış, tutarlı bir rapor istiyorsanız, NoryaAI tam olarak bunun için tasarlanmıştır. Laboratuvar sonuçlarının ötesinde genel tıbbi bilgi veya sorularınız varsa, genel bir yapay zeka sohbet robotu iş akışınızı tamamlayabilir."},
            {"q": "Yapay zeka sohbet robotları özel bir kan tahlili analizörünün yerini alabilir mi?", "a": "Genel yapay zeka sohbet robotları tıbbi terimleri açıklayabilir ve sağlık sorularını yanıtlayabilir, ancak laboratuvar raporlarını ayrıştırmaz, değerleri referans aralıklarıyla eşleştirmez veya tutarlı yapılandırılmış raporlar üretmez. NoryaAI gibi özel bir araç bu iş akışı için özellikle tasarlanmıştır."},
            {"q": "NoryaAI ücretsiz mi?", "a": "NoryaAI, nasıl çalıştığını görebilmeniz için ücretsiz bir analiz sunar. Ek analizler uygun fiyatlı planlarla kullanılabilir. Ayrıntılar için fiyatlandırma sayfasını ziyaret edin."},
        ],
    },
    "de": {
        "meta_title": "NoryaAI Vergleich — Bluttest-Analysator vs. Alternativen | NoryaAI",
        "meta_description": "Ehrliche Vergleiche von NoryaAI mit ChatGPT, Kantesti, SiPhox Health, Wizey und anderen KI-Tools für die Bluttest-Analyse.",
        "hero_title": "Wie sich NoryaAI von anderen Bluttest-Tools unterscheidet",
        "hero_sub": "Wir setzen auf Transparenz. Diese Seiten bieten ehrliche Vergleiche, damit Sie das richtige Tool für Ihre Bedürfnisse finden.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Allzweck-KI-Chatbot. Gut für medizinische Begriffe — aber nicht für strukturierte Bluttest-Berichte gebaut."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Türkische Labortesterklärung. Auf den lokalen Markt mit grundlegenden Testwert-Erklärungen ausgerichtet."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Bluttest-Service für zu Hause mit eigenen Testkits. Norya analysiert Ergebnisse, die Sie bereits haben."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "KI-gestütztes Gesundheitsdaten-Tool. Verarbeitet verschiedene Datentypen mit einem anderen Ansatz."},
            {"slug": "norya-vs-generic-ai", "name": "Allgemeine KI-Chatbots", "summary": "ChatGPT, Claude, Gemini u.a. Wie sich KI-Chat mit einem dedizierten Bluttest-Analysator vergleicht."},
        ],
        "cards_cta": "Vollständigen Vergleich lesen",
        "hub_faqs": [
            {"q": "Welches Tool ist am besten für Bluttest-Ergebnisse?", "a": "Das hängt von Ihren Bedürfnissen ab. Wenn Sie einen strukturierten Bericht mit Gesundheitsscore, markierten Markern und arzt-tauglichem PDF möchten, ist NoryaAI genau dafür gebaut. Für allgemeine medizinische Informationen kann ein KI-Chatbot ergänzend nützlich sein."},
            {"q": "Können KI-Chatbots einen Bluttest-Analysator ersetzen?", "a": "Allgemeine KI-Chatbots können medizinische Begriffe erklären, aber sie parsen keine Laborberichte, ordnen Werte keinen Referenzbereichen zu und erstellen keine konsistenten strukturierten Berichte."},
            {"q": "Ist NoryaAI kostenlos?", "a": "NoryaAI bietet eine kostenlose Analyse, damit Sie sehen können, wie es funktioniert. Weitere Analysen sind über günstige Preispläne verfügbar."},
        ],
    },
    "fr": {
        "meta_title": "Comparer NoryaAI — Analyseur de bilan sanguin vs alternatives | NoryaAI",
        "meta_description": "Comparaisons honnêtes de NoryaAI avec ChatGPT, Kantesti, SiPhox Health, Wizey et d'autres outils d'IA pour l'analyse de sang.",
        "hero_title": "Comment NoryaAI se compare aux autres outils d'analyse sanguine",
        "hero_sub": "Nous croyons en la transparence. Ces pages offrent des comparaisons honnêtes pour vous aider à choisir l'outil adapté.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Chatbot IA polyvalent. Bon pour expliquer les termes médicaux — mais pas conçu pour des rapports d'analyses structurés."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Plateforme turque d'interprétation de tests. Orientée vers le marché local avec des explications de base."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Service de test sanguin à domicile avec kits. Norya analyse les résultats que vous avez déjà."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "Outil d'interprétation de données de santé par IA. Gère différents types de données avec une approche différente."},
            {"slug": "norya-vs-generic-ai", "name": "IA générique", "summary": "ChatGPT, Claude, Gemini et autres. Comment l'IA conversationnelle se compare à un analyseur dédié."},
        ],
        "cards_cta": "Lire la comparaison complète",
        "hub_faqs": [
            {"q": "Quel outil est le meilleur pour comprendre les résultats d'analyses ?", "a": "Cela dépend de vos besoins. Pour un rapport structuré avec score de santé et PDF médical, NoryaAI est conçu pour cela. Pour des informations médicales générales, un chatbot IA peut compléter votre démarche."},
            {"q": "Les chatbots IA peuvent-ils remplacer un analyseur dédié ?", "a": "Les chatbots IA généraux peuvent expliquer des termes médicaux mais ne parsent pas les rapports de laboratoire et ne produisent pas de rapports structurés cohérents."},
            {"q": "NoryaAI est-il gratuit ?", "a": "NoryaAI offre une analyse gratuite pour découvrir le service. Des analyses supplémentaires sont disponibles via des forfaits abordables."},
        ],
    },
    "it": {
        "meta_title": "Confronta NoryaAI — Analizzatore analisi del sangue vs alternative | NoryaAI",
        "meta_description": "Confronti onesti di NoryaAI con ChatGPT, Kantesti, SiPhox Health, Wizey e altri strumenti IA per l'analisi del sangue.",
        "hero_title": "Come NoryaAI si confronta con altri strumenti per le analisi del sangue",
        "hero_sub": "Crediamo nella trasparenza. Queste pagine offrono confronti onesti per aiutarti a scegliere lo strumento più adatto.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Chatbot IA generico. Ottimo per spiegare termini medici — ma non progettato per referti strutturati."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Piattaforma turca per interpretazione test. Orientata al mercato locale con spiegazioni di base."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Servizio di test ematici a domicilio con kit propri. Norya analizza i risultati che hai già."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "Strumento IA per interpretazione dati sanitari. Gestisce vari tipi di dati con un approccio diverso."},
            {"slug": "norya-vs-generic-ai", "name": "IA generica", "summary": "ChatGPT, Claude, Gemini e altri. Come l'IA conversazionale si confronta con un analizzatore dedicato."},
        ],
        "cards_cta": "Leggi il confronto completo",
        "hub_faqs": [
            {"q": "Qual è lo strumento migliore per capire le analisi del sangue?", "a": "Dipende dalle tue esigenze. Per un referto strutturato con punteggio di salute e PDF medico, NoryaAI è progettato appositamente. Per informazioni mediche generali, un chatbot IA può essere complementare."},
            {"q": "I chatbot IA possono sostituire un analizzatore dedicato?", "a": "I chatbot IA generici possono spiegare termini medici ma non analizzano referti di laboratorio né producono report strutturati e coerenti."},
            {"q": "NoryaAI è gratuito?", "a": "NoryaAI offre un'analisi gratuita per provare il servizio. Analisi aggiuntive sono disponibili tramite piani convenienti."},
        ],
    },
    "es": {
        "meta_title": "Comparar NoryaAI — Analizador de sangre vs alternativas | NoryaAI",
        "meta_description": "Comparaciones honestas de NoryaAI con ChatGPT, Kantesti, SiPhox Health, Wizey y otras herramientas de IA para análisis de sangre.",
        "hero_title": "Cómo se compara NoryaAI con otras herramientas de análisis de sangre",
        "hero_sub": "Creemos en la transparencia. Estas páginas ofrecen comparaciones honestas para ayudarte a elegir la herramienta adecuada.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Chatbot de IA de propósito general. Bueno para explicar términos médicos — pero no diseñado para informes estructurados."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Plataforma turca de interpretación de pruebas. Enfocada al mercado local con explicaciones básicas."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Servicio de análisis de sangre en casa con kits propios. Norya analiza los resultados que ya tienes."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "Herramienta de IA para interpretación de datos de salud. Maneja varios tipos de datos con un enfoque diferente."},
            {"slug": "norya-vs-generic-ai", "name": "IA genérica", "summary": "ChatGPT, Claude, Gemini y otros. Cómo la IA conversacional se compara con un analizador dedicado."},
        ],
        "cards_cta": "Leer comparación completa",
        "hub_faqs": [
            {"q": "¿Cuál es la mejor herramienta para entender análisis de sangre?", "a": "Depende de tus necesidades. Para un informe estructurado con puntuación de salud y PDF médico, NoryaAI está diseñado para eso. Para información médica general, un chatbot de IA puede complementar tu flujo."},
            {"q": "¿Pueden los chatbots de IA reemplazar un analizador dedicado?", "a": "Los chatbots de IA generales pueden explicar términos médicos pero no analizan informes de laboratorio ni producen reportes estructurados consistentes."},
            {"q": "¿NoryaAI es gratis?", "a": "NoryaAI ofrece un análisis gratuito para probar el servicio. Análisis adicionales están disponibles a través de planes asequibles."},
        ],
    },
    "he": {
        "meta_title": "השוואת NoryaAI — מנתח בדיקות דם מול חלופות | NoryaAI",
        "meta_description": "השוואות כנות של NoryaAI עם ChatGPT, Kantesti, SiPhox Health, Wizey וכלי AI נוספים לניתוח בדיקות דם.",
        "hero_title": "איך NoryaAI משתווה לכלים אחרים לבדיקות דם",
        "hero_sub": "אנחנו מאמינים בשקיפות. דפים אלה מציעים השוואות כנות כדי לעזור לכם לבחור את הכלי המתאים.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "צ'אטבוט AI כללי. מצוין להסברת מונחים רפואיים — אך לא בנוי לדוחות בדיקות דם מובנים."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "פלטפורמה טורקית לפירוש בדיקות מעבדה. מתמקדת בשוק המקומי עם הסברים בסיסיים."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "שירות בדיקות דם ביתי עם ערכות בדיקה. Norya מנתח תוצאות שכבר יש לכם."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "כלי AI לפירוש נתוני בריאות. מטפל בסוגי נתונים שונים בגישה שונה."},
            {"slug": "norya-vs-generic-ai", "name": "צ'אטבוטים כלליים", "summary": "ChatGPT, Claude, Gemini ואחרים. איך AI שיחתי משתווה למנתח בדיקות דם ייעודי."},
        ],
        "cards_cta": "קראו את ההשוואה המלאה",
        "hub_faqs": [
            {"q": "איזה כלי הכי טוב להבנת תוצאות בדיקות דם?", "a": "תלוי בצרכים שלכם. לדוח מובנה עם ציון בריאות ו-PDF רפואי, NoryaAI תוכנן במיוחד לכך. למידע רפואי כללי, צ'אטבוט AI יכול להשלים."},
            {"q": "האם צ'אטבוטים יכולים להחליף מנתח ייעודי?", "a": "צ'אטבוטים כלליים יכולים להסביר מונחים רפואיים אך אינם מנתחים דוחות מעבדה ואינם מפיקים דוחות מובנים ועקביים."},
            {"q": "האם NoryaAI חינמי?", "a": "NoryaAI מציע ניתוח חינמי כדי שתוכלו לראות איך זה עובד. ניתוחים נוספים זמינים דרך תוכניות במחירים נוחים."},
        ],
    },
    "hi": {
        "meta_title": "NoryaAI तुलना — रक्त परीक्षण विश्लेषक बनाम विकल्प | NoryaAI",
        "meta_description": "रक्त परीक्षण विश्लेषण के लिए ChatGPT, Kantesti, SiPhox Health, Wizey और अन्य AI उपकरणों के साथ NoryaAI की ईमानदार तुलना।",
        "hero_title": "NoryaAI अन्य रक्त परीक्षण उपकरणों से कैसे तुलना करता है",
        "hero_sub": "हम पारदर्शिता में विश्वास करते हैं। ये पृष्ठ ईमानदार तुलना प्रदान करते हैं ताकि आप अपनी ज़रूरतों के लिए सही उपकरण चुन सकें।",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "सामान्य-उद्देश्य AI चैटबॉट। चिकित्सा शब्दों की व्याख्या के लिए अच्छा — लेकिन संरचित रक्त परीक्षण रिपोर्ट के लिए नहीं बनाया गया।"},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "तुर्की लैब परीक्षण व्याख्या मंच। बुनियादी परीक्षण मान स्पष्टीकरण के साथ स्थानीय बाज़ार पर केंद्रित।"},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "अपनी टेस्ट किट के साथ घर पर रक्त परीक्षण सेवा। Norya आपके मौजूदा परिणामों का विश्लेषण करता है।"},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "AI-संचालित स्वास्थ्य डेटा व्याख्या उपकरण। विभिन्न डेटा प्रकारों को अलग दृष्टिकोण से संभालता है।"},
            {"slug": "norya-vs-generic-ai", "name": "सामान्य AI चैटबॉट", "summary": "ChatGPT, Claude, Gemini और अन्य। बातचीत AI एक समर्पित रक्त परीक्षण विश्लेषक से कैसे तुलना करता है।"},
        ],
        "cards_cta": "पूरी तुलना पढ़ें",
        "hub_faqs": [
            {"q": "रक्त परीक्षण परिणाम समझने के लिए सबसे अच्छा उपकरण कौन सा है?", "a": "यह आपकी ज़रूरतों पर निर्भर करता है। स्वास्थ्य स्कोर और मेडिकल PDF के साथ संरचित रिपोर्ट के लिए, NoryaAI विशेष रूप से इसके लिए बनाया गया है।"},
            {"q": "क्या AI चैटबॉट एक समर्पित विश्लेषक की जगह ले सकते हैं?", "a": "सामान्य AI चैटबॉट चिकित्सा शब्दों की व्याख्या कर सकते हैं लेकिन लैब रिपोर्ट पार्स नहीं करते और सुसंगत संरचित रिपोर्ट नहीं बनाते।"},
            {"q": "क्या NoryaAI मुफ़्त है?", "a": "NoryaAI एक मुफ़्त विश्लेषण प्रदान करता है। अतिरिक्त विश्लेषण किफ़ायती योजनाओं के माध्यम से उपलब्ध हैं।"},
        ],
    },
    "ar": {
        "meta_title": "مقارنة NoryaAI — محلل فحوصات الدم مقابل البدائل | NoryaAI",
        "meta_description": "مقارنات صادقة بين NoryaAI وChatGPT وKantesti وSiPhox Health وWizey وأدوات الذكاء الاصطناعي الأخرى لتحليل فحوصات الدم.",
        "hero_title": "كيف يقارن NoryaAI بأدوات فحص الدم الأخرى",
        "hero_sub": "نؤمن بالشفافية. تقدم هذه الصفحات مقارنات صادقة لمساعدتك في اختيار الأداة المناسبة.",
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "روبوت دردشة ذكاء اصطناعي للأغراض العامة. جيد لشرح المصطلحات الطبية — لكنه غير مصمم لتقارير فحص الدم المنظمة."},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "منصة تركية لتفسير الاختبارات المعملية. تركز على السوق المحلي مع شروحات أساسية."},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "خدمة فحص دم منزلية بأدوات فحص خاصة. Norya يحلل النتائج التي لديك بالفعل."},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "أداة ذكاء اصطناعي لتفسير البيانات الصحية. تتعامل مع أنواع بيانات مختلفة بنهج مختلف."},
            {"slug": "norya-vs-generic-ai", "name": "روبوتات الدردشة العامة", "summary": "ChatGPT وClaude وGemini وغيرها. كيف يقارن الذكاء الاصطناعي المحادثاتي بمحلل فحوصات دم مخصص."},
        ],
        "cards_cta": "اقرأ المقارنة الكاملة",
        "hub_faqs": [
            {"q": "ما أفضل أداة لفهم نتائج فحوصات الدم؟", "a": "يعتمد على احتياجاتك. لتقرير منظم مع نقاط صحية وPDF طبي، NoryaAI مصمم خصيصًا لذلك. للمعلومات الطبية العامة، يمكن لروبوت الدردشة أن يكمل سير عملك."},
            {"q": "هل يمكن لروبوتات الدردشة أن تحل محل محلل مخصص؟", "a": "روبوتات الدردشة العامة يمكنها شرح المصطلحات الطبية لكنها لا تحلل تقارير المختبر ولا تنتج تقارير منظمة متسقة."},
            {"q": "هل NoryaAI مجاني؟", "a": "يقدم NoryaAI تحليلاً مجانيًا لتجربة الخدمة. تحليلات إضافية متاحة عبر خطط بأسعار معقولة."},
        ],
    },
}

# ── Detail page content (competitor-specific) ─────────────────────────────
# Keys: meta_title, meta_description, hero_title, hero_sub,
#       quick_answer_title, quick_answer,
#       comparison_sub, competitor_name,
#       competitor_helps_title, competitor_helps_sub, competitor_helps_items,
#       faqs

_DETAIL: dict[tuple[str, str], dict] = {}

# ── EN detail pages ──

_DETAIL[("en", "norya-vs-chatgpt-for-blood-tests")] = {
    "competitor_name": "ChatGPT",
    "meta_title": "NoryaAI vs ChatGPT for Blood Tests — Honest Comparison | NoryaAI",
    "meta_description": "How does NoryaAI compare to ChatGPT for understanding blood test results? Side-by-side comparison of structured reports vs free-form chat answers.",
    "hero_title": "NoryaAI vs ChatGPT for Blood Tests",
    "hero_sub": "ChatGPT is a powerful general-purpose AI — but analyzing blood tests requires a different kind of tool. Here is an honest look at how they compare.",
    "quick_answer_title": "The short version",
    "quick_answer": "ChatGPT can explain medical terms and answer health questions in conversation. NoryaAI is purpose-built for blood tests: it reads your lab report, maps every value to reference ranges, and produces a structured, doctor-ready summary with a health score. Both have a place, but they solve different problems.",
    "comparison_sub": "How NoryaAI and ChatGPT differ across the features that matter most when you need to understand blood test results.",
    "competitor_helps_title": "When ChatGPT can still help",
    "competitor_helps_sub": "This is not about one tool being bad and another being good. They serve different purposes.",
    "competitor_helps_items": [
        {"icon": "📚", "title": "General health education", "desc": "ChatGPT is great for learning what a biomarker means, how the immune system works, or what a specific condition involves."},
        {"icon": "💡", "title": "Brainstorming questions for your doctor", "desc": "Before an appointment, ChatGPT can help you think through what to ask — even if it cannot read your actual lab report with precision."},
        {"icon": "🔍", "title": "Understanding medical terminology", "desc": "If you encounter an unfamiliar term in your report, ChatGPT can explain it quickly in plain language."},
    ],
    "faqs": [
        {"q": "Can ChatGPT explain blood test results?", "a": "Yes, to a degree. ChatGPT can explain what individual values mean in general terms. However, it does not parse your actual lab report, may hallucinate reference ranges, and produces a different answer each time. NoryaAI reads your report directly and outputs a consistent, structured summary."},
        {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions."},
        {"q": "Why is a structured report better than a chat answer?", "a": "A structured report gives you a health score, category breakdown, and flagged markers in a consistent format. You can compare it with previous tests, print it for your doctor, and see at a glance which values need attention."},
        {"q": "Can I upload a PDF to ChatGPT for blood test analysis?", "a": "ChatGPT Plus can process PDFs, but it treats them as general documents without blood-test-specific parsing. NoryaAI is designed to extract values, match reference ranges, and produce a medical-context report."},
        {"q": "Is NoryaAI better for multilingual lab reports?", "a": "NoryaAI generates full reports in 9+ languages with preserved medical context. While ChatGPT can translate, it may lose nuance in medical terminology."},
    ],
}

_DETAIL[("en", "norya-vs-kantesti")] = {
    "competitor_name": "Kantesti",
    "meta_title": "NoryaAI vs Kantesti for Blood Tests — Honest Comparison | NoryaAI",
    "meta_description": "Comparing NoryaAI and Kantesti for blood test interpretation. See how structured AI analysis compares to web-based value lookups.",
    "hero_title": "NoryaAI vs Kantesti for Blood Tests",
    "hero_sub": "Kantesti is a Turkish lab test platform focused on value lookups. NoryaAI takes a different approach with full report parsing and structured analysis. Here is how they compare.",
    "quick_answer_title": "The short version",
    "quick_answer": "Kantesti offers a web-based interface for looking up individual blood test values with basic explanations, primarily serving the Turkish market. NoryaAI parses your entire lab report automatically, maps values to reference ranges, and delivers a structured summary with health scores in 9+ languages.",
    "comparison_sub": "How NoryaAI and Kantesti differ across the features that matter most for understanding blood test results.",
    "competitor_helps_title": "When Kantesti can still help",
    "competitor_helps_sub": "Different tools serve different needs. Here is where Kantesti may be useful.",
    "competitor_helps_items": [
        {"icon": "🇹🇷", "title": "Quick Turkish-language explanations", "desc": "For Turkish users who want a fast lookup of what a specific blood value means, Kantesti provides a convenient local-language reference."},
        {"icon": "🔢", "title": "Common blood marker reference", "desc": "Kantesti can be helpful for checking individual test values one at a time when you already know which marker to look up."},
        {"icon": "🏥", "title": "Turkish healthcare context", "desc": "Explanations are framed within the Turkish medical system, which may be useful for patients interacting with Turkish healthcare providers."},
    ],
    "faqs": [
        {"q": "What is Kantesti?", "a": "Kantesti is a Turkish web platform where users can look up blood test values and read basic explanations of what each marker means."},
        {"q": "Does Kantesti provide structured reports?", "a": "Kantesti primarily offers individual value lookups with explanations. A comprehensive, structured report format with health scores is not clearly disclosed in their public offering."},
        {"q": "Is NoryaAI available in Turkish?", "a": "Yes. NoryaAI supports full Turkish-language reports with the same structured format, health scores, and doctor-ready PDF available in all supported languages."},
        {"q": "Can I upload my lab report to Kantesti?", "a": "Kantesti primarily uses manual value entry. NoryaAI accepts PDF uploads, photos, and pasted text with automatic parsing."},
        {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor."},
    ],
}

_DETAIL[("en", "norya-vs-siphox-health")] = {
    "competitor_name": "SiPhox Health",
    "meta_title": "NoryaAI vs SiPhox Health — Blood Test Analysis Comparison | NoryaAI",
    "meta_description": "Comparing NoryaAI with SiPhox Health for blood test analysis. At-home test kits vs structured AI analysis of your existing lab results.",
    "hero_title": "NoryaAI vs SiPhox Health",
    "hero_sub": "SiPhox Health sells at-home blood test kits. NoryaAI analyzes lab results you already have. They approach blood testing from different angles — here is an honest comparison.",
    "quick_answer_title": "The short version",
    "quick_answer": "SiPhox Health is an at-home blood testing service: you order a kit, collect a fingerprick sample, mail it back, and receive results through their app. NoryaAI works differently — you upload any existing lab report (PDF, photo, or text) and get a structured analysis instantly. They solve different parts of the blood test journey.",
    "comparison_sub": "How NoryaAI and SiPhox Health differ in their approach to blood test analysis.",
    "competitor_helps_title": "When SiPhox Health can still help",
    "competitor_helps_sub": "Different tools serve different needs. Here is where SiPhox Health may be a good fit.",
    "competitor_helps_items": [
        {"icon": "🏠", "title": "At-home testing convenience", "desc": "If you want to test from home without visiting a lab, SiPhox provides fingerprick kits you can use at your convenience."},
        {"icon": "📊", "title": "Longitudinal tracking", "desc": "With their subscription model, you can take repeat tests over time and track trends within the SiPhox ecosystem."},
        {"icon": "🎯", "title": "Curated biomarker panels", "desc": "SiPhox offers pre-selected panels designed for specific health goals, which can simplify the decision of what to test."},
    ],
    "faqs": [
        {"q": "What is SiPhox Health?", "a": "SiPhox Health is an at-home blood testing service that ships fingerprick test kits to your door. You collect a small blood sample and mail it back for analysis."},
        {"q": "Can I use NoryaAI with SiPhox test results?", "a": "Yes. If you have your SiPhox results as a PDF or digital report, you can upload them to NoryaAI for a structured analysis with health scores and doctor-ready formatting."},
        {"q": "Do I need to buy a test kit to use NoryaAI?", "a": "No. NoryaAI works with any existing lab report — from hospitals, clinics, or any laboratory. Just upload your results and get your analysis."},
        {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor."},
        {"q": "Which is better: at-home testing or analyzing existing results?", "a": "They complement each other. SiPhox is useful when you need a new test without visiting a lab. NoryaAI is useful when you already have results and want a clear, structured understanding of them."},
    ],
}

_DETAIL[("en", "norya-vs-wizey")] = {
    "competitor_name": "Wizey",
    "meta_title": "NoryaAI vs Wizey — Blood Test Analysis Comparison | NoryaAI",
    "meta_description": "Comparing NoryaAI and Wizey for health data interpretation. See how a blood-test-specific analyzer compares to a general health data tool.",
    "hero_title": "NoryaAI vs Wizey",
    "hero_sub": "Wizey interprets various health data types using AI. NoryaAI is focused specifically on blood test analysis. Here is how they compare for lab result interpretation.",
    "quick_answer_title": "The short version",
    "quick_answer": "Wizey is an AI-powered health data interpretation platform that can work with various types of health information. NoryaAI is purpose-built exclusively for blood test analysis: it parses lab reports, maps values to reference ranges, and produces structured, doctor-ready reports. If your primary need is understanding blood test results, NoryaAI offers a more specialized workflow.",
    "comparison_sub": "How NoryaAI and Wizey differ across the features that matter most for blood test analysis.",
    "competitor_helps_title": "When Wizey can still help",
    "competitor_helps_sub": "Different tools serve different needs. Here is where Wizey may be useful.",
    "competitor_helps_items": [
        {"icon": "📱", "title": "Broad health data integration", "desc": "Wizey can work with various types of health data beyond blood tests, which may be useful if you want a broader health overview."},
        {"icon": "⌚", "title": "Wearable data connection", "desc": "Wizey may integrate with fitness trackers and wearable devices, providing insights that go beyond lab results."},
        {"icon": "🌐", "title": "General wellness insights", "desc": "For users who want AI-powered analysis across multiple health data sources, Wizey offers a broader scope."},
    ],
    "faqs": [
        {"q": "What is Wizey?", "a": "Wizey is an AI-powered health data interpretation platform that can analyze various types of health information to provide insights and recommendations."},
        {"q": "Does Wizey focus specifically on blood tests?", "a": "Wizey handles various health data types. NoryaAI is built exclusively for blood test analysis with specialized parsing, reference range mapping, and structured report generation."},
        {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor."},
        {"q": "Can I use both Wizey and NoryaAI?", "a": "Yes. They serve complementary purposes. You might use Wizey for broader health tracking and NoryaAI specifically when you need a detailed, structured blood test report."},
        {"q": "Which tool is better for blood test analysis specifically?", "a": "NoryaAI is purpose-built for blood tests with specialized lab report parsing, value-to-range mapping, health scoring, and doctor-ready PDF generation. Its entire workflow is designed around this specific use case."},
    ],
}

_DETAIL[("en", "norya-vs-generic-ai")] = {
    "competitor_name": "Generic AI",
    "meta_title": "NoryaAI vs Generic AI for Blood Tests — Honest Comparison | NoryaAI",
    "meta_description": "How does NoryaAI compare to ChatGPT or other AI chatbots for understanding blood test results? Side-by-side comparison of structured reports vs free-form chat answers.",
    "hero_title": "NoryaAI vs Generic AI Chatbots for Blood Tests",
    "hero_sub": "Both can work with lab data — but they approach it very differently. Here is an honest, side-by-side look at what each one offers when you need to understand your blood test results.",
    "quick_answer_title": "The short version",
    "quick_answer": "Generic AI chatbots like ChatGPT can explain medical terms and answer health questions in conversation. NoryaAI is purpose-built for blood tests: it reads your lab report, maps every value to reference ranges, and produces a structured, doctor-ready summary with a health score — not a free-form paragraph. Both have a place, but they solve different problems.",
    "comparison_sub": "How the two approaches differ across the features that matter most when you are looking at blood test results.",
    "competitor_helps_title": "When generic AI chatbots can still help",
    "competitor_helps_sub": "This is not about one tool being bad and another being good. They serve different purposes.",
    "competitor_helps_items": [
        {"icon": "📚", "title": "General health education", "desc": "Chatbots are great for learning what a biomarker means, how the immune system works, or what a specific condition involves — broad educational questions."},
        {"icon": "💡", "title": "Brainstorming questions for your doctor", "desc": "Before an appointment, a chatbot can help you think through what to ask — even if it cannot read your actual lab report with precision."},
        {"icon": "🔍", "title": "Understanding medical terminology", "desc": "If you encounter an unfamiliar term in your report, a general AI can explain it quickly in plain language."},
    ],
    "faqs": [
        {"q": "Can ChatGPT explain blood test results?", "a": "Yes, to a degree. ChatGPT can explain what individual values mean in general terms. However, it does not parse your actual lab report, may hallucinate reference ranges, and produces a different answer each time you ask. NoryaAI is built to read your report directly and output a consistent, structured summary."},
        {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions."},
        {"q": "Why is a structured report better than a chat answer?", "a": "A structured report gives you a health score, category breakdown, and flagged markers in a consistent format. You can compare it with previous tests, print it for your doctor, and see at a glance which values need attention — something a free-form chat paragraph cannot reliably offer."},
        {"q": "Can I upload a PDF instead of copying values manually?", "a": "Yes. NoryaAI accepts PDF uploads, photos of printed lab reports (JPG/PNG), and pasted text. It parses the values and reference ranges automatically — no manual data entry required."},
        {"q": "Is NoryaAI better for multilingual lab reports?", "a": "NoryaAI generates full reports in 9+ languages with preserved medical context. While general chatbots can translate text, they may lose nuance in medical terminology. NoryaAI's multilingual output is designed specifically for lab result interpretation."},
    ],
}

# ── TR detail pages ──

_DETAIL[("tr", "norya-vs-chatgpt-for-blood-tests")] = {
    "competitor_name": "ChatGPT",
    "meta_title": "NoryaAI vs ChatGPT Kan Tahlili İçin — Dürüst Karşılaştırma | NoryaAI",
    "meta_description": "NoryaAI, kan tahlili sonuçlarını anlamak için ChatGPT ile nasıl karşılaştırılır? Yapılandırılmış raporlar ile serbest sohbet yanıtlarının yan yana karşılaştırması.",
    "hero_title": "NoryaAI vs ChatGPT — Kan Tahlili İçin",
    "hero_sub": "ChatGPT güçlü bir genel amaçlı yapay zekadır — ancak kan tahlili analizi farklı türde bir araç gerektirir. İşte dürüst bir karşılaştırma.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "ChatGPT tıbbi terimleri açıklayabilir ve sağlık sorularını sohbet formatında yanıtlayabilir. NoryaAI ise kan testleri için özel olarak tasarlanmıştır: laboratuvar raporunuzu okur, her değeri referans aralıklarıyla eşleştirir ve sağlık skoruyla yapılandırılmış, doktora hazır bir özet üretir. Her ikisinin de yeri var, ancak farklı sorunları çözerler.",
    "comparison_sub": "NoryaAI ve ChatGPT'nin kan tahlili sonuçlarını anlamak için en önemli özellikler açısından farkları.",
    "competitor_helps_title": "ChatGPT ne zaman yardımcı olabilir",
    "competitor_helps_sub": "Bu, bir aracın kötü, diğerinin iyi olmasıyla ilgili değil. Farklı amaçlara hizmet ederler.",
    "competitor_helps_items": [
        {"icon": "📚", "title": "Genel sağlık eğitimi", "desc": "ChatGPT, bir biyobelirtecin ne anlama geldiğini, bağışıklık sisteminin nasıl çalıştığını veya belirli bir durumun ne içerdiğini öğrenmek için mükemmeldir."},
        {"icon": "💡", "title": "Doktorunuza sorular hazırlama", "desc": "Bir randevu öncesinde, ChatGPT ne soracağınızı düşünmenize yardımcı olabilir — laboratuvar raporunuzu doğrudan okuyamasa bile."},
        {"icon": "🔍", "title": "Tıbbi terminolojiyi anlama", "desc": "Raporunuzda bilmediğiniz bir terimle karşılaşırsanız, ChatGPT bunu sade bir dille hızlıca açıklayabilir."},
    ],
    "faqs": [
        {"q": "ChatGPT kan tahlili sonuçlarını açıklayabilir mi?", "a": "Evet, bir dereceye kadar. ChatGPT bireysel değerlerin genel olarak ne anlama geldiğini açıklayabilir. Ancak gerçek laboratuvar raporunuzu ayrıştırmaz, referans aralıklarını halüsinasyon olarak üretebilir ve her seferinde farklı bir yanıt verir. NoryaAI raporunuzu doğrudan okuyarak tutarlı, yapılandırılmış bir özet çıkarır."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önermez. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
        {"q": "Yapılandırılmış rapor neden sohbet yanıtından daha iyidir?", "a": "Yapılandırılmış rapor, tutarlı bir formatta sağlık skoru, kategori dökümü ve işaretlenmiş belirteçler sunar. Önceki testlerle karşılaştırabilir, doktorunuz için yazdırabilir ve hangi değerlerin dikkat gerektirdiğini bir bakışta görebilirsiniz."},
        {"q": "ChatGPT'ye kan tahlili için PDF yükleyebilir miyim?", "a": "ChatGPT Plus PDF'leri işleyebilir, ancak bunları kan testine özgü ayrıştırma olmadan genel belgeler olarak ele alır. NoryaAI değerleri çıkarmak, referans aralıklarını eşleştirmek ve tıbbi bağlam raporu üretmek için tasarlanmıştır."},
        {"q": "NoryaAI çok dilli laboratuvar raporları için daha mı iyi?", "a": "NoryaAI, korunmuş tıbbi bağlamla 9+ dilde tam raporlar üretir. ChatGPT çevirebilir, ancak tıbbi terminolojide nüans kaybolabilir."},
    ],
}

_DETAIL[("tr", "norya-vs-kantesti")] = {
    "competitor_name": "Kantesti",
    "meta_title": "NoryaAI vs Kantesti Kan Tahlili İçin — Dürüst Karşılaştırma | NoryaAI",
    "meta_description": "Kan tahlili yorumlama için NoryaAI ve Kantesti karşılaştırması. Yapılandırılmış AI analizi ile web tabanlı değer aramanın farkları.",
    "hero_title": "NoryaAI vs Kantesti — Kan Tahlili İçin",
    "hero_sub": "Kantesti, Türk pazarına odaklı bir laboratuvar testi platformudur. NoryaAI ise tam rapor ayrıştırma ve yapılandırılmış analiz ile farklı bir yaklaşım sunar.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "Kantesti, ağırlıklı olarak Türk pazarına hizmet veren, bireysel kan testi değerlerini temel açıklamalarla aramak için web tabanlı bir arayüz sunar. NoryaAI ise tüm laboratuvar raporunuzu otomatik olarak ayrıştırır, değerleri referans aralıklarıyla eşleştirir ve 9+ dilde sağlık skorlarıyla yapılandırılmış bir özet sunar.",
    "comparison_sub": "NoryaAI ve Kantesti'nin kan tahlili sonuçlarını anlamak için en önemli özellikler açısından farkları.",
    "competitor_helps_title": "Kantesti ne zaman yardımcı olabilir",
    "competitor_helps_sub": "Farklı araçlar farklı ihtiyaçlara hizmet eder. İşte Kantesti'nin faydalı olabileceği durumlar.",
    "competitor_helps_items": [
        {"icon": "🇹🇷", "title": "Hızlı Türkçe açıklamalar", "desc": "Belirli bir kan değerinin ne anlama geldiğini hızlıca öğrenmek isteyen Türk kullanıcılar için Kantesti uygun bir yerel referans sağlar."},
        {"icon": "🔢", "title": "Yaygın kan belirteçleri referansı", "desc": "Hangi belirteci arayacağınızı zaten biliyorsanız, bireysel test değerlerini tek tek kontrol etmek için faydalı olabilir."},
        {"icon": "🏥", "title": "Türk sağlık sistemi bağlamı", "desc": "Açıklamalar Türk tıp sistemi çerçevesinde sunulur, bu da Türk sağlık hizmet sağlayıcılarıyla etkileşimde olan hastalar için faydalı olabilir."},
    ],
    "faqs": [
        {"q": "Kantesti nedir?", "a": "Kantesti, kullanıcıların kan testi değerlerini arayabildiği ve her belirtecin ne anlama geldiğine dair temel açıklamalar okuyabildiği bir Türk web platformudur."},
        {"q": "Kantesti yapılandırılmış raporlar sağlıyor mu?", "a": "Kantesti öncelikle açıklamalarla bireysel değer aramaları sunar. Sağlık skorlarıyla kapsamlı, yapılandırılmış bir rapor formatı kamuya açık tekliflerinde açıkça belirtilmemiştir."},
        {"q": "NoryaAI Türkçe kullanılabilir mi?", "a": "Evet. NoryaAI, desteklenen tüm dillerde aynı yapılandırılmış format, sağlık skorları ve doktora hazır PDF ile tam Türkçe raporları destekler."},
        {"q": "Laboratuvar raporumu Kantesti'ye yükleyebilir miyim?", "a": "Kantesti öncelikle manuel değer girişi kullanır. NoryaAI ise otomatik ayrıştırmayla PDF yüklemeleri, fotoğraflar ve yapıştırılmış metni kabul eder."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önermez."},
    ],
}

_DETAIL[("tr", "norya-vs-siphox-health")] = {
    "competitor_name": "SiPhox Health",
    "meta_title": "NoryaAI vs SiPhox Health — Kan Tahlili Analiz Karşılaştırması | NoryaAI",
    "meta_description": "Kan tahlili analizi için NoryaAI ile SiPhox Health karşılaştırması. Evde test kitleri ile mevcut lab sonuçlarınızın yapılandırılmış AI analizi.",
    "hero_title": "NoryaAI vs SiPhox Health",
    "hero_sub": "SiPhox Health evde kan testi kitleri satar. NoryaAI ise zaten elinizdeki laboratuvar sonuçlarını analiz eder. Kan testine farklı açılardan yaklaşırlar.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "SiPhox Health bir evde kan testi hizmetidir: kit sipariş edersiniz, parmaktan numune alırsınız, geri gönderirsiniz ve sonuçları uygulamalarından alırsınız. NoryaAI farklı çalışır — mevcut herhangi bir laboratuvar raporunu (PDF, fotoğraf veya metin) yüklersiniz ve anında yapılandırılmış analiz alırsınız. Kan testi sürecinin farklı bölümlerini çözerler.",
    "comparison_sub": "NoryaAI ve SiPhox Health'in kan tahlili analizine yaklaşımlarındaki farklar.",
    "competitor_helps_title": "SiPhox Health ne zaman yardımcı olabilir",
    "competitor_helps_sub": "Farklı araçlar farklı ihtiyaçlara hizmet eder.",
    "competitor_helps_items": [
        {"icon": "🏠", "title": "Evde test kolaylığı", "desc": "Laboratuvara gitmeden evden test yapmak istiyorsanız, SiPhox kolaylığınız için parmaktan kan alma kitleri sağlar."},
        {"icon": "📊", "title": "Uzun vadeli takip", "desc": "Abonelik modelleriyle zaman içinde tekrarlanan testler yapabilir ve SiPhox ekosistemi içinde trendleri takip edebilirsiniz."},
        {"icon": "🎯", "title": "Seçilmiş biyobelirteç panelleri", "desc": "SiPhox, belirli sağlık hedeflerine yönelik önceden seçilmiş paneller sunar, neyi test edeceğinize karar vermeyi basitleştirir."},
    ],
    "faqs": [
        {"q": "SiPhox Health nedir?", "a": "SiPhox Health, kapınıza parmaktan kan alma test kitleri gönderen bir evde kan testi hizmetidir. Küçük bir kan numunesi alır ve analiz için geri gönderirsiniz."},
        {"q": "SiPhox test sonuçlarımla NoryaAI kullanabilir miyim?", "a": "Evet. SiPhox sonuçlarınız PDF veya dijital rapor olarak varsa, sağlık skorları ve doktora hazır formatla yapılandırılmış bir analiz için NoryaAI'ya yükleyebilirsiniz."},
        {"q": "NoryaAI kullanmak için test kiti satın almam gerekir mi?", "a": "Hayır. NoryaAI hastanelerden, kliniklerden veya herhangi bir laboratuvardan alınmış mevcut herhangi bir laboratuvar raporu ile çalışır. Sadece sonuçlarınızı yükleyin."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önermez."},
        {"q": "Evde test mi yoksa mevcut sonuçları analiz etmek mi daha iyi?", "a": "Birbirlerini tamamlarlar. SiPhox, laboratuvara gitmeden yeni bir teste ihtiyaç duyduğunuzda faydalıdır. NoryaAI ise zaten sonuçlarınız olduğunda ve bunların net, yapılandırılmış bir anlayışını istediğinizde faydalıdır."},
    ],
}

_DETAIL[("tr", "norya-vs-wizey")] = {
    "competitor_name": "Wizey",
    "meta_title": "NoryaAI vs Wizey — Kan Tahlili Analiz Karşılaştırması | NoryaAI",
    "meta_description": "Sağlık verisi yorumlama için NoryaAI ve Wizey karşılaştırması. Kan testine özel analizör ile genel sağlık verisi aracının farkları.",
    "hero_title": "NoryaAI vs Wizey",
    "hero_sub": "Wizey, yapay zeka kullanarak çeşitli sağlık verilerini yorumlar. NoryaAI ise özellikle kan tahlili analizine odaklanır. İşte laboratuvar sonuçları yorumlaması için karşılaştırma.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "Wizey, çeşitli sağlık bilgileriyle çalışabilen yapay zeka destekli bir sağlık verisi yorumlama platformudur. NoryaAI ise yalnızca kan tahlili analizi için özel olarak tasarlanmıştır: laboratuvar raporlarını ayrıştırır, değerleri referans aralıklarıyla eşleştirir ve yapılandırılmış, doktora hazır raporlar üretir.",
    "comparison_sub": "NoryaAI ve Wizey'in kan tahlili analizi için en önemli özellikler açısından farkları.",
    "competitor_helps_title": "Wizey ne zaman yardımcı olabilir",
    "competitor_helps_sub": "Farklı araçlar farklı ihtiyaçlara hizmet eder.",
    "competitor_helps_items": [
        {"icon": "📱", "title": "Geniş sağlık verisi entegrasyonu", "desc": "Wizey kan testlerinin ötesinde çeşitli sağlık verileriyle çalışabilir, daha geniş bir sağlık genel bakışı istiyorsanız faydalı olabilir."},
        {"icon": "⌚", "title": "Giyilebilir cihaz bağlantısı", "desc": "Wizey, fitness takip cihazları ve giyilebilir cihazlarla entegre olabilir, laboratuvar sonuçlarının ötesinde içgörüler sağlayabilir."},
        {"icon": "🌐", "title": "Genel sağlık içgörüleri", "desc": "Birden fazla sağlık verisi kaynağında yapay zeka destekli analiz isteyen kullanıcılar için Wizey daha geniş bir kapsam sunar."},
    ],
    "faqs": [
        {"q": "Wizey nedir?", "a": "Wizey, içgörüler ve öneriler sağlamak için çeşitli sağlık bilgilerini analiz edebilen yapay zeka destekli bir sağlık verisi yorumlama platformudur."},
        {"q": "Wizey özellikle kan testlerine mi odaklanır?", "a": "Wizey çeşitli sağlık verisi türlerini işler. NoryaAI ise özelleştirilmiş ayrıştırma, referans aralığı eşleme ve yapılandırılmış rapor üretimiyle yalnızca kan tahlili analizi için tasarlanmıştır."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önermez."},
        {"q": "Hem Wizey hem de NoryaAI kullanabilir miyim?", "a": "Evet. Tamamlayıcı amaçlara hizmet ederler. Daha geniş sağlık takibi için Wizey'i, ayrıntılı ve yapılandırılmış bir kan tahlili raporu gerektiğinde ise NoryaAI'ı kullanabilirsiniz."},
        {"q": "Kan tahlili analizi için özellikle hangi araç daha iyi?", "a": "NoryaAI, özelleştirilmiş laboratuvar raporu ayrıştırma, değer-aralık eşleme, sağlık skorlama ve doktora hazır PDF üretimi ile kan testleri için özel olarak tasarlanmıştır."},
    ],
}

_DETAIL[("tr", "norya-vs-generic-ai")] = {
    "competitor_name": "Genel Yapay Zeka",
    "meta_title": "NoryaAI vs Genel Yapay Zeka Kan Tahlili İçin — Dürüst Karşılaştırma | NoryaAI",
    "meta_description": "NoryaAI, kan tahlili sonuçlarını anlamak için ChatGPT veya diğer yapay zeka sohbet robotlarıyla nasıl karşılaştırılır? Yapılandırılmış raporlar ile serbest sohbet yanıtlarının karşılaştırması.",
    "hero_title": "NoryaAI vs Genel Yapay Zeka Sohbet Robotları — Kan Tahlili İçin",
    "hero_sub": "Her ikisi de laboratuvar verileriyle çalışabilir — ancak çok farklı yaklaşırlar. İşte kan tahlili sonuçlarınızı anlamanız gerektiğinde her birinin sunduklarının dürüst, yan yana karşılaştırması.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "ChatGPT gibi genel yapay zeka sohbet robotları tıbbi terimleri açıklayabilir ve sağlık sorularını sohbet formatında yanıtlayabilir. NoryaAI ise kan testleri için özel olarak tasarlanmıştır: laboratuvar raporunuzu okur, her değeri referans aralıklarıyla eşleştirir ve sağlık skoruyla yapılandırılmış, doktora hazır bir özet üretir — serbest biçimli bir paragraf değil.",
    "comparison_sub": "İki yaklaşımın kan tahlili sonuçlarına baktığınızda en çok önem taşıyan özellikler açısından farkları.",
    "competitor_helps_title": "Genel yapay zeka sohbet robotları ne zaman yardımcı olabilir",
    "competitor_helps_sub": "Bu, bir aracın kötü, diğerinin iyi olmasıyla ilgili değil. Farklı amaçlara hizmet ederler.",
    "competitor_helps_items": [
        {"icon": "📚", "title": "Genel sağlık eğitimi", "desc": "Sohbet robotları, bir biyobelirtecin ne anlama geldiğini, bağışıklık sisteminin nasıl çalıştığını veya belirli bir durumun ne içerdiğini öğrenmek için mükemmeldir."},
        {"icon": "💡", "title": "Doktorunuza sorular hazırlama", "desc": "Bir randevu öncesinde, bir sohbet robotu ne soracağınızı düşünmenize yardımcı olabilir — laboratuvar raporunuzu doğrudan okuyamasa bile."},
        {"icon": "🔍", "title": "Tıbbi terminolojiyi anlama", "desc": "Raporunuzda bilmediğiniz bir terimle karşılaşırsanız, genel bir yapay zeka bunu sade bir dille hızlıca açıklayabilir."},
    ],
    "faqs": [
        {"q": "ChatGPT kan tahlili sonuçlarını açıklayabilir mi?", "a": "Evet, bir dereceye kadar. ChatGPT bireysel değerlerin genel olarak ne anlama geldiğini açıklayabilir. Ancak gerçek laboratuvar raporunuzu ayrıştırmaz, referans aralıklarını halüsinasyon olarak üretebilir ve her seferinde farklı bir yanıt verir."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önermez. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
        {"q": "Yapılandırılmış rapor neden sohbet yanıtından daha iyidir?", "a": "Yapılandırılmış rapor, tutarlı bir formatta sağlık skoru, kategori dökümü ve işaretlenmiş belirteçler sunar. Önceki testlerle karşılaştırabilir, doktorunuz için yazdırabilir ve hangi değerlerin dikkat gerektirdiğini bir bakışta görebilirsiniz."},
        {"q": "Değerleri manuel olarak kopyalamak yerine PDF yükleyebilir miyim?", "a": "Evet. NoryaAI, PDF yüklemelerini, basılı laboratuvar raporlarının fotoğraflarını (JPG/PNG) ve yapıştırılmış metni kabul eder. Değerleri ve referans aralıklarını otomatik olarak ayrıştırır — manuel veri girişi gerekmez."},
        {"q": "NoryaAI çok dilli laboratuvar raporları için daha mı iyi?", "a": "NoryaAI, korunmuş tıbbi bağlamla 9+ dilde tam raporlar üretir. Genel sohbet robotları metni çevirebilir, ancak tıbbi terminolojide nüans kaybolabilir."},
    ],
}


# ── Import extra locale content ────────────────────────────────────────────
# DE, FR, IT, ES, HE, HI, AR detail & competitor-side content
from app.compare_pages_extra_locales import (
    EXTRA_DETAIL as _EXTRA_DETAIL,
    EXTRA_COMPETITOR_SIDE as _EXTRA_COMPETITOR_SIDE,
)

_DETAIL.update(_EXTRA_DETAIL)
_COMPETITOR_SIDE.update(_EXTRA_COMPETITOR_SIDE)


# ── Builder functions ──────────────────────────────────────────────────────

def _build_comparison_items(lang: str, slug: str) -> list[dict]:
    """Compose comparison table rows from labels + norya side + competitor side."""
    labels = _COMPARISON_LABELS.get(lang, _COMPARISON_LABELS["en"])
    norya = _NORYA_SIDE.get(lang, _NORYA_SIDE["en"])
    competitor = _COMPETITOR_SIDE.get((lang, slug))
    if not competitor:
        competitor = _COMPETITOR_SIDE.get(("en", slug), [""] * 9)
    return [
        {"label": l, "competitor": c, "norya": n}
        for l, c, n in zip(labels, competitor, norya)
    ]


# ── Public API ─────────────────────────────────────────────────────────────

def get_compare_hub_content(lang: str) -> dict | None:
    """Return merged hub page content for locale."""
    lang = lang.strip().lower()
    shared = _SHARED.get(lang)
    hub = _HUB.get(lang)
    if not shared or not hub:
        return None
    return {**shared, **hub}


def get_compare_detail_content(lang: str, slug: str) -> dict | None:
    """Return merged detail page content for (locale, competitor slug)."""
    lang = lang.strip().lower()
    slug = slug.strip().lower()
    shared = _SHARED.get(lang)
    detail = _DETAIL.get((lang, slug))
    if not shared or not detail:
        return None
    items = _build_comparison_items(lang, slug)
    return {**shared, **detail, "comparison_items": items}


def get_compare_hreflang_hub(lang: str, base_url: str) -> list[dict]:
    """Return hreflang alternates for a compare hub page."""
    out = [{"lang": lg, "url": f"{base_url}/{lg}/compare/"} for lg in COMPARE_LANGS]
    out.append({"lang": "x-default", "url": f"{base_url}/en/compare/"})
    return out


def get_compare_hreflang_detail(lang: str, slug: str, base_url: str) -> list[dict]:
    """Return hreflang alternates for a compare detail page."""
    out = [{"lang": lg, "url": f"{base_url}/{lg}/compare/{slug}"} for lg in COMPARE_LANGS]
    out.append({"lang": "x-default", "url": f"{base_url}/en/compare/{slug}"})
    return out


def iter_compare_urls() -> list[tuple[str, str]]:
    """Return [(type, lang, slug_or_empty), ...] for sitemap.

    type is 'hub' or 'detail'.
    """
    urls: list[tuple[str, str, str]] = []
    for lang in COMPARE_LANGS:
        urls.append(("hub", lang, ""))
    for lang in COMPARE_LANGS:
        for slug in COMPETITOR_SLUGS:
            urls.append(("detail", lang, slug))
    return urls


def get_other_competitors(slug: str, lang: str) -> list[dict]:
    """Return list of {name, slug, url_suffix} for related-comparisons block."""
    result = []
    for s in COMPETITOR_SLUGS:
        if s == slug:
            continue
        detail = _DETAIL.get((lang, s)) or _DETAIL.get(("en", s))
        name = COMPETITOR_DISPLAY_NAMES.get(s, s)
        if detail:
            name = detail.get("competitor_name", name)
        result.append({"name": name, "slug": s})
    return result
