from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Dict, List, Optional

from app.core.config import BRAND_NAME

# Blog'un desteklediği diller (mevcut sistemle uyumlu)
# SEO: Hero, seo_title, meta_description ve makale başlıkları tüm BLOG_LANGS_PREMIUM dillerinde
# tutarlı olmalı (aynı anahtar kelime mantığı, yerel dilde).
BLOG_LANGS = frozenset({"tr", "en", "de", "it", "es", "fr", "he", "ar", "hi", "el", "cs", "sr"})
# Premium blog: sadece bu dillerde route açılır; varsayılan İngilizce
BLOG_LANGS_PREMIUM = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")
DEFAULT_BLOG_LANG = "en"

# Blog arayüzü çevirileri (liste sayfası, detay CTA, vb.)
BLOG_UI = {
    "tr": {
        "hero_badge": "Sağlık rehberi",
        "hero_title": "Kan Tahlili Sonuçları Açıklaması: Biyobelirteç Rehberleri ve Net Yorumlar",
        "hero_desc": "Ferritin, CRP, tiroid, kolesterol ve daha fazlası hakkında sade dilde makaleler—hekim görüşmenize hazırlanmanız için. Teşhis değil, net rehberlik.",
        "search_placeholder": "Makale ara…",
        "category_all": "Tümü",
        "read_article": "Makaleyi oku",
        "read_min": "dk okuma",
        "cta_title": "Kan tahlilinizi dakikalar içinde anlayın",
        "cta_text": f"{BRAND_NAME} ile sonuçlarınızı net, yapılandırılmış bir sağlık özetine dönüştürün.",
        "cta_button": "Analizi başlat",
        "toc_title": "Bu sayfada",
        "other_languages": "Diğer diller",
        "back_to_blog": "Bloga dön",
        "home_link": BRAND_NAME,
        "seo_title": f"{BRAND_NAME} Blog | Kan Tahlili Sonuçları Açıklaması ve Laboratuvar Rehberleri",
        "meta_description": "Kan tahlili yorumlama rehberleri ve biyobelirteç makaleleri: ferritin, CRP, tiroid, kolesterol. Net ve eğitim amaçlı—hekim randevunuza hazırlık.",
        "no_results": "Aramanızla eşleşen makale bulunamadı.",
        "last_updated": "Son güncelleme",
        "hero_cta_primary": "Kan tahlilinizi analiz edin",
        "hero_cta_caption": "KVKK uyumlu. Dakikalar içinde net raporlar.",
        "end_cta_title": "Sonuçlarınızı yükleyin, net rapor alın",
        "end_cta_text": "Laboratuvar sonuçlarınızı güvenle yükleyin; sade dilde açıklamalar ve önemli noktalar dakikalar içinde.",
        "end_cta_button": "Kan tahlili analizi",
        "related_label": "İlgili makaleler",
        "blog_back_to_landing": "Ana Sayfa",
        "how_it_works_link": "Nasıl çalışır",
        "pricing_link": "Fiyatlandırma",
    },
    "en": {
        "hero_badge": "Health insights",
        "hero_title": "Blood Test Results Explained: Biomarker Guides and Clear Lab Interpretations",
        "hero_desc": "Plain-language articles on ferritin, CRP, thyroid, cholesterol and more—to help you prepare for your doctor visit. No diagnosis, just clear guidance.",
        "search_placeholder": "Search articles…",
        "category_all": "All",
        "read_article": "Read article",
        "read_min": "min read",
        "cta_title": "Understand your blood test in minutes",
        "cta_text": f"Use {BRAND_NAME} to turn your results into a clear, structured health summary.",
        "cta_button": "Start analysis",
        "toc_title": "On this page",
        "other_languages": "Other languages",
        "back_to_blog": "Back to blog",
        "home_link": BRAND_NAME,
        "seo_title": f"{BRAND_NAME} Blog | Blood Test Results Explained & Lab Report Guides",
        "meta_description": "Blood test interpretation guides and biomarker articles: ferritin, CRP, thyroid, cholesterol. Clear, educational—for your next doctor visit.",
        "no_results": "No articles match your search.",
        "last_updated": "Last updated",
        "hero_cta_primary": "Analyze your blood test",
        "hero_cta_caption": "GDPR compliant. Clear reports in minutes.",
        "end_cta_title": "Upload your results, get a clear report",
        "end_cta_text": "Upload your lab results securely; get plain-language explanations and key points in minutes.",
        "end_cta_button": "Analyze blood test",
        "related_label": "Related articles",
        "blog_back_to_landing": "Home",
        "how_it_works_link": "How it works",
        "pricing_link": "Pricing",
    },
    "de": {
        "hero_badge": "Gesundheitswissen",
        "hero_title": "Blutwerte verstehen: Ratgeber zu Biomarkern und Laborergebnissen",
        "hero_desc": "Verständliche Artikel zu Ferritin, CRP, Schilddrüse, Cholesterin und mehr — für Ihre Orientierung vor dem Arztgespräch.",
        "search_placeholder": "Artikel suchen…",
        "category_all": "Alle",
        "read_article": "Artikel lesen",
        "read_min": "Min. Lesezeit",
        "cta_title": "Blutwerte in Minuten verstehen",
        "cta_text": f"Mit {BRAND_NAME} aus Ihren Werten eine klare, strukturierte Gesundheitszusammenfassung erstellen.",
        "cta_button": "Analyse starten",
        "toc_title": "Auf dieser Seite",
        "other_languages": "Andere Sprachen",
        "back_to_blog": "Zurück zum Blog",
        "home_link": BRAND_NAME,
        "seo_title": f"{BRAND_NAME} Blog | Blutwerte & Laborergebnisse verstehen — Ratgeber",
        "meta_description": "Blutwerte und Laborergebnisse verständlich erklärt: Ferritin, CRP, Schilddrüse, Cholesterin. Für die Orientierung vor dem Arztbesuch.",
        "no_results": "Keine Artikel entsprechen Ihrer Suche.",
        "last_updated": "Zuletzt aktualisiert",
        "hero_cta_primary": "Blutwerte analysieren",
        "hero_cta_caption": "DSGVO-konform. Klare Berichte in Minuten.",
        "end_cta_title": "Befund hochladen — klaren Bericht bekommen",
        "end_cta_text": "Laborergebnisse sicher hochladen. Verständliche Erklärungen — das Wichtigste in Minuten erfassen.",
        "end_cta_button": "Analyse starten",
        "related_label": "Das könnte Sie auch interessieren",
        "blog_back_to_landing": "Startseite",
        "how_it_works_link": "So funktioniert's",
        "pricing_link": "Preise",
    },
    "fr": {
        "hero_badge": "Santé & analyses",
        "hero_title": "Résultats d'analyses expliqués : guides biomarqueurs et interprétations claires",
        "hero_desc": "Articles en langage clair sur la ferritine, CRP, thyroïde, cholestérol et plus—pour préparer votre consultation. Pas de diagnostic, juste des repères clairs.",
        "search_placeholder": "Rechercher un article…",
        "category_all": "Tout",
        "read_article": "Lire l'article",
        "read_min": "min de lecture",
        "cta_title": "Comprenez votre bilan sanguin en quelques minutes",
        "cta_text": f"Avec {BRAND_NAME}, transformez vos résultats en un résumé de santé clair et structuré.",
        "cta_button": "Lancer l'analyse",
        "toc_title": "Sur cette page",
        "other_languages": "Autres langues",
        "back_to_blog": "Retour au blog",
        "home_link": BRAND_NAME,
        "seo_title": f"Blog {BRAND_NAME} | Résultats d'analyses expliqués et guides bilan sanguin",
        "meta_description": "Guides d'interprétation et articles biomarqueurs : ferritine, CRP, thyroïde, cholestérol. Clair et informatif—pour votre prochaine consultation.",
        "no_results": "Aucun article ne correspond à votre recherche.",
        "last_updated": "Dernière mise à jour",
        "hero_cta_primary": "Analyser votre bilan sanguin",
        "hero_cta_caption": "Conforme RGPD. Rapports clairs en quelques minutes.",
        "end_cta_title": "Uploadez vos résultats, obtenez un rapport clair",
        "end_cta_text": "Uploadez vos résultats en toute sécurité ; explications en langage clair et points clés en quelques minutes.",
        "end_cta_button": "Analyser le bilan sanguin",
        "related_label": "Articles similaires",
        "blog_back_to_landing": "Accueil",
        "how_it_works_link": "Comment ça marche",
        "pricing_link": "Tarifs",
    },
    "it": {
        "hero_badge": "Salute e analisi",
        "hero_title": "Risultati delle analisi spiegati: guide biomarcatori e interpretazioni chiare",
        "hero_desc": "Articoli in linguaggio chiaro su ferritina, PCR, tiroide, colesterolo e altro—per prepararti alla visita. Nessuna diagnosi, solo orientamento chiaro.",
        "search_placeholder": "Cerca articoli…",
        "category_all": "Tutti",
        "read_article": "Leggi l'articolo",
        "read_min": "min di lettura",
        "cta_title": "Comprendi le tue analisi in pochi minuti",
        "cta_text": f"Con {BRAND_NAME} trasformi i risultati in un riepilogo di salute chiaro e strutturato.",
        "cta_button": "Avvia analisi",
        "toc_title": "In questa pagina",
        "other_languages": "Altre lingue",
        "back_to_blog": "Torna al blog",
        "home_link": BRAND_NAME,
        "seo_title": f"Blog {BRAND_NAME} | Risultati analisi spiegati e guide referti",
        "meta_description": "Guide interpretazione analisi e articoli biomarcatori: ferritina, PCR, tiroide, colesterolo. Chiaro e informativo—per la prossima visita.",
        "no_results": "Nessun articolo corrisponde alla ricerca.",
        "last_updated": "Ultimo aggiornamento",
        "hero_cta_primary": "Analizza le tue analisi",
        "hero_cta_caption": "Conforme GDPR. Report chiari in pochi minuti.",
        "end_cta_title": "Carica i risultati, ottieni un report chiaro",
        "end_cta_text": "Carica i referti in modo sicuro; spiegazioni in linguaggio semplice e punti chiave in pochi minuti.",
        "end_cta_button": "Analizza le analisi",
        "related_label": "Articoli correlati",
        "blog_back_to_landing": "Home",
        "how_it_works_link": "Come funziona",
        "pricing_link": "Prezzi",
    },
    "es": {
        "hero_badge": "Salud y análisis",
        "hero_title": "Resultados de análisis explicados: guías de biomarcadores e interpretaciones claras",
        "hero_desc": "Artículos en lenguaje claro sobre ferritina, PCR, tiroides, colesterol y más—para preparar tu consulta. No es diagnóstico, solo orientación clara.",
        "search_placeholder": "Buscar artículos…",
        "category_all": "Todos",
        "read_article": "Leer artículo",
        "read_min": "min de lectura",
        "cta_title": "Comprende tu análisis en minutos",
        "cta_text": f"Con {BRAND_NAME} convierte tus resultados en un resumen de salud claro y estructurado.",
        "cta_button": "Iniciar análisis",
        "toc_title": "En esta página",
        "other_languages": "Otros idiomas",
        "back_to_blog": "Volver al blog",
        "home_link": BRAND_NAME,
        "seo_title": f"Blog {BRAND_NAME} | Resultados de análisis explicados y guías",
        "meta_description": "Guías de interpretación y artículos biomarcadores: ferritina, PCR, tiroides, colesterol. Claro e informativo—para tu próxima consulta.",
        "no_results": "Ningún artículo coincide con tu búsqueda.",
        "last_updated": "Última actualización",
        "hero_cta_primary": "Analiza tu análisis",
        "hero_cta_caption": "Cumple GDPR. Informes claros en minutos.",
        "end_cta_title": "Sube tus resultados, obtén un informe claro",
        "end_cta_text": "Sube tus resultados de forma segura; explicaciones en lenguaje claro y puntos clave en minutos.",
        "end_cta_button": "Analizar análisis",
        "related_label": "Artículos relacionados",
        "blog_back_to_landing": "Inicio",
        "how_it_works_link": "Cómo funciona",
        "pricing_link": "Precios",
    },
    "he": {
        "hero_badge": "תובנות בריאות",
        "hero_title": "תוצאות בדיקות דם מוסברות: מדריכי ביומרקרים ופרשנויות ברורות",
        "hero_desc": "מאמרים בשפה פשוטה על פריטין, CRP, תירואיד, כולסטרול ועוד—להכנה לפני הפגישה עם הרופא. לא אבחון, רק הכוונה ברורה.",
        "search_placeholder": "חיפוש מאמרים…",
        "category_all": "הכל",
        "read_article": "קרא את המאמר",
        "read_min": "דק׳ קריאה",
        "cta_title": "הבן את בדיקת הדם שלך תוך דקות",
        "cta_text": f"השתמש ב-{BRAND_NAME} להפוך את התוצאות לסיכום בריאות ברור ומסודר.",
        "cta_button": "התחל ניתוח",
        "toc_title": "בעמוד זה",
        "other_languages": "שפות אחרות",
        "back_to_blog": "חזרה לבלוג",
        "home_link": BRAND_NAME,
        "seo_title": f"בלוג {BRAND_NAME} | תוצאות בדיקות דם מוסברות ומדריכים",
        "meta_description": "מדריכי פרשנות בדיקות דם ומאמרי ביומרקרים: פריטין, CRP, תירואיד, כולסטרול. ברור ואינפורמטיבי—לפני הפגישה עם הרופא.",
        "no_results": "לא נמצאו מאמרים התואמים לחיפוש.",
        "last_updated": "עדכון אחרון",
        "hero_cta_primary": "נתח את בדיקת הדם שלך",
        "hero_cta_caption": "תואם GDPR. דוחות ברורים תוך דקות.",
        "end_cta_title": "העלה את התוצאות, קבל דוח ברור",
        "end_cta_text": "העלה את התוצאות בצורה מאובטחת; הסברים בשפה פשוטה ונקודות עיקריות תוך דקות.",
        "end_cta_button": "ניתוח בדיקת דם",
        "related_label": "מאמרים קשורים",
        "blog_back_to_landing": "בית",
        "how_it_works_link": "איך זה עובד",
        "pricing_link": "מחירים",
    },
    "hi": {
        "hero_badge": "स्वास्थ्य जानकारी",
        "hero_title": "ब्लड टेस्ट रिज़ल्ट समझाए गए: बायोमार्कर गाइड और स्पष्ट व्याख्या",
        "hero_desc": "फेरिटिन, CRP, थायरॉइड, कोलेस्ट्रॉल आदि पर सरल लेख—डॉक्टर से मिलने की तैयारी के लिए। निदान नहीं, बस स्पष्ट मार्गदर्शन।",
        "search_placeholder": "लेख खोजें…",
        "category_all": "सभी",
        "read_article": "लेख पढ़ें",
        "read_min": "मिनट पढ़ने",
        "cta_title": "अपना ब्लड टेस्ट मिनटों में समझें",
        "cta_text": f"{BRAND_NAME} से अपने रिज़ल्ट को स्पष्ट, संरचित स्वास्थ्य सारांश में बदलें।",
        "cta_button": "विश्लेषण शुरू करें",
        "toc_title": "इस पृष्ठ पर",
        "other_languages": "अन्य भाषाएं",
        "back_to_blog": "ब्लॉग पर वापस",
        "home_link": BRAND_NAME,
        "seo_title": f"{BRAND_NAME} ब्लॉग | ब्लड टेस्ट रिज़ल्ट समझाए गए और गाइड",
        "meta_description": "ब्लड टेस्ट व्याख्या गाइड और बायोमार्कर लेख: फेरिटिन, CRP, थायरॉइड, कोलेस्ट्रॉल। स्पष्ट और शैक्षिक—अपनी अगली विजिट के लिए।",
        "no_results": "आपकी खोज से मेल खाता कोई लेख नहीं मिला।",
        "last_updated": "अंतिम अपडेट",
        "hero_cta_primary": "अपना ब्लड टेस्ट विश्लेषण करें",
        "hero_cta_caption": "GDPR अनुरूप। मिनटों में स्पष्ट रिपोर्ट।",
        "end_cta_title": "अपने परिणाम अपलोड करें, स्पष्ट रिपोर्ट पाएं",
        "end_cta_text": "अपनी लैब रिपोर्ट सुरक्षित अपलोड करें; सरल भाषा में व्याख्या और मुख्य बिंदु मिनटों में।",
        "end_cta_button": "ब्लड टेस्ट विश्लेषण",
        "related_label": "संबंधित लेख",
        "blog_back_to_landing": "होम",
        "how_it_works_link": "यह कैसे काम करता है",
        "pricing_link": "मूल्य निर्धारण",
    },
    "ar": {
        "hero_badge": "صحة وتحاليل",
        "hero_title": "شرح نتائج تحاليل الدم: أدلة المؤشرات الحيوية وتفسيرات واضحة",
        "hero_desc": "مقالات بلغة بسيطة عن الفيريتين، CRP، الغدة الدرقية، الكوليسترول والمزيد—للاستعداد لزيارة الطبيب. ليست تشخيصاً، بل توجيه واضح.",
        "search_placeholder": "البحث في المقالات…",
        "category_all": "الكل",
        "read_article": "قراءة المقال",
        "read_min": "دقائق قراءة",
        "cta_title": "افهم تحليل دمك في دقائق",
        "cta_text": f"استخدم {BRAND_NAME} لتحويل نتائجك إلى ملخص صحي واضح ومنظم.",
        "cta_button": "بدء التحليل",
        "toc_title": "في هذه الصفحة",
        "other_languages": "لغات أخرى",
        "back_to_blog": "العودة للمدونة",
        "home_link": BRAND_NAME,
        "seo_title": f"مدونة {BRAND_NAME} | شرح نتائج التحاليل وأدلة التقارير",
        "meta_description": "أدلة تفسير التحاليل ومقالات المؤشرات الحيوية: الفيريتين، CRP، الغدة الدرقية، الكوليسترول. واضحة وتعليمية—قبل زيارة الطبيب.",
        "no_results": "لا توجد مقالات تطابق بحثك.",
        "last_updated": "آخر تحديث",
        "hero_cta_primary": "تحليل تحاليلك",
        "hero_cta_caption": "متوافق مع حماية البيانات. تقارير واضحة في دقائق.",
        "end_cta_title": "ارفع نتائجك واحصل على تقرير واضح",
        "end_cta_text": "ارفع نتائج المختبر بأمان؛ احصل على شرح بلغة بسيطة والنقاط الأساسية في دقائق.",
        "end_cta_button": "تحليل التحاليل",
        "related_label": "مقالات ذات صلة",
        "blog_back_to_landing": "الرئيسية",
        "featured_label": "مقال مميز",
        "filter_tags_label": "تصفية",
        "filter_tags_title": "تصفية حسب الموضوع",
        "close_filter_drawer": "إغلاق",
        "breadcrumb_aria": "مسار التنقل",
        "close_toc_drawer": "إغلاق المحتويات",
        "how_it_works_link": "كيف يعمل",
        "pricing_link": "الأسعار",
    },
}


@dataclass(frozen=True)
class Section:
    id: str
    level: int  # 2 = H2, 3 = H3
    heading: str
    body_html: str  # Güvenli, önceden yazılmış HTML


@dataclass(frozen=True)
class Article:
    id: str
    published_at: date
    read_minutes: int
    cover_image: str
    category: Dict[str, str]  # lang -> kategori adı
    slugs: Dict[str, str]  # lang -> slug
    titles: Dict[str, str]  # lang -> H1
    subtitles: Dict[str, str]  # lang -> alt açıklama
    excerpts: Dict[str, str]  # lang -> liste kartı kısa açıklama
    seo_titles: Dict[str, str]
    seo_descriptions: Dict[str, str]
    sections_by_lang: Dict[str, List[Section]]  # lang -> bölümler
    cover_alt: Optional[Dict[str, str]] = None  # lang -> alt text for cover image
    last_updated: Optional[date] = None  # display "Last updated"; if None, use published_at
    faq_schema_qa: Optional[Dict[str, List[Dict[str, str]]]] = None  # lang -> [{"question", "answer"}] for FAQ schema


def _article_ldl() -> Article:
    """LDL kolesterol yazısı — tüm dillerde çeviri içeren örnek makale."""
    published = date(2025, 1, 5)
    cover = "/static/images/blog/ldl-hdl-hero.png"

    return Article(
        id="ldl-target-values",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category={
            "tr": "Kolesterol",
            "en": "Cholesterol",
            "de": "Cholesterin",
            "it": "Colesterolo",
            "es": "Colesterol",
            "fr": "Cholestérol",
            "he": "כולסטרול",
            "ar": "الكوليسترول",
            "hi": "कोलेस्ट्रॉल",
            "el": "Χοληστερόλη",
            "cs": "Cholesterol",
            "sr": "Холестерол",
        },
        slugs={
            "tr": "ldl-kolesterol-kac-olmali",
            "en": "ldl-cholesterol-level",
            "de": "ldl-cholesterin",
            "it": "valori-ldl-colesterolo",
            "es": "niveles-colesterol-ldl",
            "fr": "taux-de-ldl-cholesterol",
            "he": "ldl-cholesterol-target",
            "ar": "ldl-cholesterol-normal-range",
            "hi": "ldl-cholesterol-kitna-hona-chahiye",
            "el": "ldl-cholesterol-target-values",
            "cs": "hodnoty-ldl-cholesterolu",
            "sr": "ciljne-vrednosti-ldl-holesterola",
        },
        titles={
            "tr": "LDL kolesterol kaç olmalı? Hangi seviye riskli?",
            "en": "What should your LDL cholesterol level be?",
            "de": "Wie hoch sollte Ihr LDL‑Cholesterin sein?",
            "it": "Quanto dovrebbe essere il colesterolo LDL?",
            "es": "¿Cuál debería ser tu nivel de colesterol LDL?",
            "fr": "Quel devrait être votre taux de LDL‑cholestérol ?",
            "he": "מהו ערך LDL כולסטרול תקין ולמי יש סיכון?",
            "ar": "كم يجب أن يكون مستوى كوليسترول LDL وما الذي يعتبر خطيراً؟",
            "hi": "एलडीएल (LDL) कोलेस्ट्रॉल कितना होना चाहिए और कब जोखिम artar?",
            "el": "Ποια πρέπει να είναι τα επίπεδα LDL χοληστερόλης σας;",
            "cs": "Jaké by měly být hodnoty LDL cholesterolu?",
            "sr": "Колико треба да буде LDL холестерол и када постаје ризичан?",
        },
        subtitles={
            "tr": "LDL kolesterol için hedef aralıkları, risk gruplarına göre hedefler ve tetkik sonucunuzda gördüğünüz değerleri adım adım açıklıyoruz.",
            "en": "Understand target LDL ranges, how risk factors change your goal values, and what your lab report number really means.",
            "de": "Zielbereiche für LDL, Einfluss von Risikofaktoren und was der Wert in Ihrem Laborbefund praktisch bedeutet.",
            "it": "Scopri i valori obiettivo di LDL, come cambiano con i fattori di rischio e come leggere correttamente il tuo referto.",
            "es": "Conoce los rangos objetivo de LDL, cómo cambian según tus factores de riesgo y cómo interpretar tu informe de laboratorio.",
            "fr": "Comprenez les valeurs cibles de LDL, l’impact de vos facteurs de risque et comment interpréter votre résultat de laboratoire.",
            "he": "הסבר פשוט על טווחי היעד של LDL, איך גורמי סיכון משפיעים עליהם ומה אומר המספר שמופיע בבדיקת הדם.",
            "ar": "شرح مبسط لقيم الهدف من LDL، وكيف تؤثر عوامل الخطر على هذه القيم، وكيف تفهم الرقم في نتيجة التحليل.",
            "hi": "LDL के सामान्य लक्ष्य रेंज, जोखिम कारक होने पर लक्ष्य कैसे बदलते हैं और आपकी रिपोर्ट में दिखने वाला नंबर क्या बताता है।",
            "el": "Στόχοι για LDL, πώς τους αλλάζουν οι παράγοντες κινδύνου και πώς να διαβάζετε σωστά το αποτέλεσμα στο χαρτί εξετάσεων.",
            "cs": "Cílové hodnoty LDL, vliv rizikových faktorů a návod, jak číst váš laboratorní výsledek.",
            "sr": "Циљне вредности LDL‑а, утицај фактора ризика и како да правилно тумачите број у лабораторијском извештају.",
        },
        excerpts={
            "tr": "LDL kolesterol için 'normal' tek bir sayı yoktur. Kardiyovasküler riskinize göre hedef değerler değişir.",
            "en": "There is no single “normal” LDL value. Targets depend on your overall cardiovascular risk.",
            "de": "Es gibt keinen einen „normalen“ LDL‑Wert – Zielbereiche hängen von Ihrem kardiovaskulären Risiko ab.",
            "it": "Non esiste un unico valore “normale” di LDL: il target dipende dal tuo rischio cardiovascolare.",
            "es": "No hay un único valor “normal” de LDL: el objetivo depende de tu riesgo cardiovascular global.",
            "fr": "Il n’existe pas une seule valeur « normale » de LDL ; la cible dépend de votre risque cardiovasculaire.",
            "he": "אין מספר אחד ״נורמלי״ ל‑LDL – ערך היעד נקבע לפי רמת הסיכון הלבבי הכוללת.",
            "ar": "لا يوجد رقم واحد «طبيعي» لـ LDL، فالقيمة المستهدفة تختلف حسب مستوى خطر أمراض القلب لديك.",
            "hi": "LDL के लिए एक ही ‘नॉर्मल’ वैल्यू नहीं होती, आपका समग्र हार्ट‑रिस्क तय करता है कि लक्ष्य कितना होना चाहिए।",
            "el": "Δεν υπάρχει μία «φυσιολογική» τιμή LDL – ο στόχος εξαρτάται από το συνολικό καρδιαγγειακό σας κίνδυνο.",
            "cs": "Neexistuje jedno univerzální „normální“ číslo LDL – cíle se určují podle vašeho kardiovaskulárního rizika.",
            "sr": "Не постоји једна „нормална“ вредност LDL‑а – циљ зависи од укупног кардиоваскуларног ризика.",
        },
        seo_titles={
            "tr": "LDL Kolesterol Kaç Olmalı? Normal ve Yüksek Değerler",
            "en": "LDL Cholesterol: Normal, High and Target Levels Explained",
            "de": "LDL‑Cholesterin: Normwerte, Zielbereiche und hohes Risiko",
            "it": "LDL Colesterolo: Valori Normali, Alti e Obiettivo",
            "es": "Colesterol LDL: Valores Normales, Altos y Objetivo",
            "fr": "LDL‑cholestérol : valeurs normales, élevées et objectifs",
            "he": "ערכי LDL כולסטרול: תקין, גבוה וערכי יעד",
            "ar": "كوليسترول LDL: القيم الطبيعية، المرتفعة وقيم الهدف",
            "hi": "LDL कोलेस्ट्रॉल: सामान्य, बढ़ा हुआ और लक्ष्य स्तर",
            "el": "LDL χοληστερόλη: φυσιολογικές, υψηλές και στόχοι",
            "cs": "LDL cholesterol: normální, zvýšené a cílové hodnoty",
            "sr": "LDL холестерол: нормалне, повишене и циљне вредности",
        },
        seo_descriptions={
            "tr": "LDL kolesterol için yaşa göre değil risk düzeyine göre hedefler kullanılır. Kendi raporunuzdaki değeri bu rehberle daha iyi anlayın.",
            "en": "LDL targets are set by cardiovascular risk, not age alone. Learn how to interpret your LDL value with practical examples.",
            "de": "LDL‑Zielwerte richten sich nach Ihrem kardiovaskulären Risiko. Erfahren Sie, wie Sie Ihren Laborwert richtig einordnen.",
            "it": "I target di LDL si definiscono in base al rischio cardiovascolare. Scopri come interpretare il valore riportato nel tuo referto.",
            "es": "Los objetivos de LDL se fijan según el riesgo cardiovascular. Aprende a interpretar tu valor de LDL con ejemplos claros.",
            "fr": "Les objectifs de LDL dépendent de votre risque cardiovasculaire. Découvrez comment lire et comprendre votre résultat.",
            "he": "ערכי היעד של LDL נקבעים לפי רמת הסיכון הלבבי. מדריך קצר שיעזור לך להבין טוב יותר את התוצאה בבדיקת הדם.",
            "ar": "قيم الهدف لـ LDL تُحدد حسب خطر أمراض القلب لديك. دليل مبسط لفهم نتيجتك في تحليل الدم.",
            "hi": "LDL का लक्ष्य सिर्फ उम्र से नहीं बल्कि हार्ट‑रिस्क से तय होता है. उदाहरणों के साथ अपनी रिपोर्ट को समझें।",
            "el": "Οι στόχοι για LDL ορίζονται με βάση τον καρδιαγγειακό κίνδυνο. Δείτε πώς να ερμηνεύσετε τη δική σας τιμή.",
            "cs": "Cílové hodnoty LDL vycházejí z vašeho kardiovaskulárního rizika. Podívejte se, jak si správně vyložit svůj výsledek.",
            "sr": "Циљне вредности LDL‑а одређују се према кардиоваскуларном ризику. Сазнајте како да протумачите свој резултат.",
        },
        sections_by_lang={
            "tr": [
                Section(
                    id="ldl-nedir",
                    level=2,
                    heading="LDL kolesterol nedir?",
                    body_html="""
<p>Kolesterol, vücudunuzun hormon üretimi ve hücre zarı yapımı için ihtiyaç duyduğu yağ benzeri bir maddedir. Kanda taşınırken
“lipoprotein” adı verilen paketler içinde dolaşır. LDL (low density lipoprotein), kolesterolü damar duvarına taşıyan partiküldür
ve bu yüzden genellikle “kötü kolesterol” olarak anılır.</p>
<p>LDL seviyesi uzun süre yüksek kaldığında, damar duvarında yağ birikimi (ateroskleroz) artar. Bu süreç kalp krizi ve inme gibi
kardiyovasküler olayların temel nedenlerinden biridir.</p>
""",
                ),
                Section(
                    id="ldl-hedef-degerler",
                    level=2,
                    heading="LDL için hedef değerler nelerdir?",
                    body_html="""
<p>Güncel kılavuzlarda LDL için <strong>tek bir “normal” değer yerine risk düzeyine göre hedef aralıklar</strong> kullanılır.
Basitleştirerek özetlersek:</p>
<ul>
  <li><strong>Düşük / orta riskli bireyler</strong>: LDL genellikle <strong>130 mg/dL&apos;nin altında</strong> tutulur.</li>
  <li><strong>Yüksek riskli bireyler</strong> (hipertansiyon, diyabet, sigara, ailede erken kalp hastalığı vb.): Hedef çoğunlukla
      <strong>100 mg/dL&apos;nin altı</strong>dır.</li>
  <li><strong>Çok yüksek riskli bireyler</strong> (geçirilmiş kalp krizi, stent, inme vb.): Hedef <strong>70 mg/dL, hatta 55 mg/dL</strong>
      altına çekilebilir.</li>
</ul>
<p>Sonuç kâğıdınızda gördüğünüz “referans aralığı” genellikle herkese ortak bir aralığı gösterir. Oysa sizin için uygun hedef,
kişisel risk profilinize göre daha düşük olabilir. Bu nedenle LDL yorumunun mutlaka hekiminizle birlikte yapılması gerekir.</p>
""",
                ),
                Section(
                    id="ldl-yuksekse-ne-olur",
                    level=2,
                    heading="LDL yüksekse ne anlama gelir?",
                    body_html="""
<p>LDL sonucunuz, yaşınıza ve cinsiyetinize bakılmaksızın, <strong>diğer risk faktörlerinizle birlikte</strong> değerlendirilir.
Örneğin 140 mg/dL LDL değeri:</p>
<ul>
  <li>Hiçbir ek risk faktörü olmayan genç bir bireyde <strong>sınırlı risk artışı</strong> anlamına gelebilir.</li>
  <li>Hipertansiyon, diyabet ve sigara öyküsü olan bir kişide ise <strong>agresif tedavi gerektiren belirgin bir risk</strong> göstergesi olabilir.</li>
</ul>
<p>Bu yüzden, sadece “yüksek” veya “düşük” etiketine değil, <strong>toplam kardiyovasküler riskinize</strong> odaklanmak önemlidir.</p>
""",
                ),
                Section(
                    id="ldl-nasil-dusurulur",
                    level=2,
                    heading="LDL kolesterol nasıl düşürülür?",
                    body_html="""
<p>Hedef LDL düzeyine ulaşmak için genellikle üç eksen birlikte kullanılır:</p>
<ol>
  <li><strong>Beslenme düzeni</strong>: Doymuş yağ (işlenmiş et ürünleri, tereyağı, bazı paketli gıdalar) ve trans yağları azaltmak,
      sebze, tam tahıl ve zeytinyağı ağırlıklı Akdeniz tipi beslenmeyi öne çıkarmak.</li>
  <li><strong>Hareket</strong>: Haftada en az 150 dakika orta tempolu egzersiz (hızlı yürüyüş gibi) hem LDL&apos;yi düşürmeye
      hem de HDL&apos;yi (iyi kolesterol) desteklemeye yardımcı olabilir.</li>
  <li><strong>Gerektiğinde ilaç tedavisi</strong>: Statinler ve hekiminizin seçeceği diğer ilaçlar, özellikle yüksek ve çok yüksek
      riskli gruplarda LDL hedeflerine ulaşmada kritik rol oynar.</li>
</ol>
<p>Herhangi bir ilaç veya takviye başlamadan önce mutlaka doktorunuza danışın. Bu yazı, tıbbi değerlendirme ve tedavinin yerini
almak için değil, raporunuzu <strong>daha bilinçli şekilde</strong> okumanız için hazırlanmıştır.</p>
""",
                ),
            ],
            # Diğer diller için içerikler, Türkçe metnin anlamını koruyacak şekilde kısaltılmış ve sadeleştirilmiş versiyonlardır.
            "en": [
                Section(
                    id="ldl-what",
                    level=2,
                    heading="What is LDL cholesterol?",
                    body_html="""
<p>Cholesterol is a fat‑like substance your body uses to build cell membranes and hormones. In the bloodstream it travels inside
lipoprotein particles. LDL (low‑density lipoprotein) delivers cholesterol towards the artery wall and is therefore often called
the “bad cholesterol”.</p>
<p>When LDL stays high for many years it accelerates atherosclerosis – fatty build‑up in the arteries – which increases the risk of
heart attack and stroke.</p>
""",
                ),
                Section(
                    id="ldl-targets",
                    level=2,
                    heading="Target LDL levels by risk group",
                    body_html="""
<p>Modern guidelines do not use a single “normal” LDL value. Instead they define <strong>target ranges based on overall cardiovascular risk</strong>:</p>
<ul>
  <li><strong>Low / moderate risk</strong>: often aim for LDL <strong>below 130 mg/dL</strong>.</li>
  <li><strong>High risk</strong> (diabetes, hypertension, smoking, strong family history): usually aim for
      <strong>below 100 mg/dL</strong>.</li>
  <li><strong>Very high risk</strong> (previous heart attack, stent, stroke): targets may be <strong>below 70 mg/dL or even 55 mg/dL</strong>.</li>
</ul>
<p>The reference range printed on your report is usually a generic interval. Your personal goal can be lower than that, which is
why LDL must always be interpreted together with your doctor.</p>
""",
                ),
                Section(
                    id="ldl-high",
                    level=2,
                    heading="What if your LDL is high?",
                    body_html="""
<p>An LDL value is never interpreted in isolation. The same number – for example <strong>140 mg/dL</strong> – can mean different things:</p>
<ul>
  <li>In a young person with no other risk factors it may represent a <strong>modest risk</strong>.</li>
  <li>In someone with diabetes, high blood pressure and smoking it may signal a <strong>clearly increased risk requiring aggressive treatment</strong>.</li>
</ul>
<p>Rather than focusing only on “high” or “low”, discuss your <strong>global cardiovascular risk</strong> and target range with your clinician.</p>
""",
                ),
                Section(
                    id="ldl-lower",
                    level=2,
                    heading="How to lower LDL cholesterol",
                    body_html="""
<p>Reaching your LDL target usually involves three pillars:</p>
<ol>
  <li><strong>Nutrition</strong>: reduce saturated and trans fats, favour vegetables, whole grains and olive‑oil‑based meals (Mediterranean pattern).</li>
  <li><strong>Physical activity</strong>: at least 150 minutes of moderate exercise per week can help lower LDL and support HDL (“good” cholesterol).</li>
  <li><strong>Medication when needed</strong>: statins and other drugs chosen by your doctor are essential in high and very‑high‑risk groups.</li>
</ol>
<p>This article is for information only and <strong>does not replace medical advice</strong>. Always consult your doctor before
starting or changing any treatment.</p>
""",
                ),
            ],
            # Diğer diller için daha kısa ama anlamdaş içerikler
            "de": [
                Section(
                    id="ldl-was",
                    level=2,
                    heading="Was ist LDL‑Cholesterin?",
                    body_html="""
<p>LDL transportiert Cholesterin in Richtung Gefäßwand und wird deshalb oft als „schlechtes Cholesterin“ bezeichnet.
Bleibt der Wert über Jahre erhöht, fördert dies Ablagerungen in den Arterien und steigert das Risiko für Herzinfarkt und Schlaganfall.</p>
""",
                ),
                Section(
                    id="ldl-zielwerte",
                    level=2,
                    heading="Typische Zielwerte nach Risikogruppe",
                    body_html="""
<ul>
  <li><strong>Niedriges / mittleres Risiko</strong>: häufig Ziel <strong>&lt; 130 mg/dL</strong></li>
  <li><strong>Hohes Risiko</strong>: meist Ziel <strong>&lt; 100 mg/dL</strong></li>
  <li><strong>Sehr hohes Risiko</strong>: Ziel <strong>&lt; 70 mg/dL</strong>, teils sogar <strong>&lt; 55 mg/dL</strong></li>
</ul>
<p>Ihr persönliches Ziel hängt von Begleiterkrankungen und Vorerkrankungen ab und sollte mit der behandelnden Ärztin / dem Arzt besprochen werden.</p>
""",
                ),
            ],
            # Kalan diller için EN içeriğini sadeleştirilmiş şekilde kullanıyoruz
        },
    )


_LDL_ARTICLE = _article_ldl()


def _article_kan_tahlili_nasil_okunur() -> Article:
    """Kan tahlili nasıl okunur — ultra premium: tanım kutuları, örnekler, stealth tarzı."""
    published = date(2025, 3, 4)
    cover = "/static/images/blog/how-to-read-blood-test-results.png"

    return Article(
        id="kan-tahlili-nasil-okunur",
        published_at=published,
        read_minutes=8,
        cover_image=cover,
        category={
            "tr": "Rehber",
            "en": "Guide",
            "de": "Leitfaden",
            "it": "Guida",
            "es": "Guía",
            "fr": "Guide",
            "he": "מדריך",
            "ar": "دليل",
            "hi": "गाइड",
            "el": "Οδηγός",
            "cs": "Průvodce",
            "sr": "Водич",
        },
        slugs={
            "tr": "kan-tahlili-nasil-okunur",
            "en": "how-to-read-blood-test-results",
            "de": "blutwerte-lesen",
            "it": "come-leggere-esami-del-sangue",
            "es": "como-leer-analisis-sangre",
            "fr": "lire-resultats-prise-de-sang",
            "he": "how-to-read-blood-test",
            "ar": "how-to-read-blood-test",
            "hi": "blood-test-kaise-padhe",
            "el": "how-to-read-blood-test",
            "cs": "jak-cist-vysledky-krve",
            "sr": "kako-citati-krvnu-analizu",
        },
        titles={
            "tr": "Kan Tahlili Sonuçları Açıklaması: Sonuçları Nasıl Anlarsınız",
            "en": "Blood Test Results Explained: How to Understand Blood Test Results",
            "de": "Blutwerte erklärt: So verstehen Sie Ihre Laborergebnisse",
            "it": "Risultati delle analisi del sangue spiegati: come capirli",
            "es": "Resultados del análisis de sangre explicados: cómo entenderlos",
            "fr": "Résultats d'analyses sanguines expliqués : comment les comprendre",
            "he": "תוצאות בדיקת דם מוסברות: איך להבין את התוצאות",
            "ar": "كيف تقرأ تحليل الدم",
            "hi": "ब्लड टेस्ट रिज़ल्ट समझाए गए: कैसे समझें",
            "el": "Πώς να διαβάσετε τα αποτελέσματα αίματος",
            "cs": "Jak číst výsledky krevního testu",
            "sr": "Како читати крвну анализу",
        },
        subtitles={
            "tr": "Tahlil sonucu kâğıdındaki terimleri, referans aralıklarını ve değerlerin ne anlama geldiğini sade bir dille açıklıyoruz.",
            "en": "A step-by-step guide to understanding values, units, and reference ranges.",
            "de": "Verständliche Erklärung von Begriffen, Referenzbereichen und Werten im Laborbefund.",
            "it": "Guida chiara a termini, intervalli di riferimento e valori sul referto.",
            "es": "Guía clara de términos, rangos de referencia y valores en el informe.",
            "fr": "Guide clair des termes, fourchettes de référence et valeurs sur le résultat.",
            "he": "הסבר ברור על המונחים, טווחי הנורמה והמספרים בתוצאות הבדיקה.",
            "ar": "دليل واضح للمصطلحات ونطاقات المرجع والقيم في التقرير.",
            "hi": "रिपोर्ट में दिखने वाले शब्दों, रेफरेंस रेंज और संख्याओं की सरल व्याख्या।",
            "el": "Ξεκάθαρος οδηγός για τους όρους, τα διαστήματα αναφοράς και τις τιμές στην ανακοίνωση.",
            "cs": "Přehled pojmů, referenčních rozmezí a hodnot na laboratorním protokolu.",
            "sr": "Јасан водич кроз појмове, референтне вредности и бројеве на извештају.",
        },
        excerpts={
            "tr": "Referans aralığı, birimler ve sonuç kâğıdındaki sütunlar: tahlilinizi doğru yorumlamak için bilmeniz gerekenler.",
            "en": "A clear guide to blood test interpretation: reference ranges, units, high/low flags, and how to understand your results step by step.",
            "de": "Referenzbereiche, Einheiten und Spalten im Befund – das Wichtigste für die Einordnung Ihrer Werte.",
            "it": "Intervalli di riferimento, unità e colonne del referto: cosa serve per leggere bene le analisi.",
            "es": "Rangos de referencia, unidades y columnas del informe: lo esencial para interpretar tu análisis.",
            "fr": "Fourchettes de référence, unités et colonnes du résultat : l’essentiel pour interpréter votre bilan.",
            "he": "טווחי נורמה, יחידות ועמודות בדף התוצאות – מה שצריך כדי להבין את הבדיקה.",
            "ar": "نطاقات المرجع والوحدات والأعمدة في التقرير: ما تحتاج معرفته لفهم التحليل.",
            "hi": "रेफरेंस रेंज, यूनिट और रिपोर्ट के कॉलम: ब्लड टेस्ट समझने के लिए जरूरी बातें।",
            "el": "Διαστήματα αναφοράς, μονάδες και στήλες στην ανακοίνωση: ό,τι χρειάζεστε για να ερμηνεύσετε τη διαζήτηση.",
            "cs": "Referenční rozmezí, jednotky a sloupce na protokolu: co potřebujete k interpretaci výsledků.",
            "sr": "Референтни опсези, јединице и колоне у извештају: све што треба да протумачите анализу.",
        },
        seo_titles={
            "tr": "Kan Tahlili Nasıl Okunur? Referans Aralığı ve Değerler Rehberi",
            "en": "How to Read Blood Test Results (Step-by-Step) | NoryaAI",
            "de": "Blutbefund lesen: Referenzbereich und Werte verstehen",
            "it": "Come leggere gli esami del sangue | Guida valori e riferimenti",
            "es": "Cómo leer un análisis de sangre | Guía de valores y referencia",
            "fr": "Comment lire une prise de sang | Guide des valeurs et références",
            "he": "איך לקרוא תוצאות בדיקת דם | מדריך טווחי נורמה",
            "ar": "كيف تقرأ تحليل الدم | دليل القيم ونطاق المرجع",
            "hi": "ब्लड टेस्ट रिपोर्ट कैसे पढ़ें | रेफरेंस रेंज गाइड",
            "el": "Πώς να διαβάσετε τα εξεταστικά αίματος | Οδηγός τιμών",
            "cs": "Jak číst krevní výsledky | Referenční rozmezí a hodnoty",
            "sr": "Како читати крвну анализу | Водич референтних вредности",
        },
        seo_descriptions={
            "tr": "Kan tahlili sonucu kâğıdında referans aralığı, birimler ve değerlerin anlamı. Adım adım, sade dilde rehber.",
            "en": "Learn how to read a blood test report: values, units, reference ranges, high/low flags, and common panels like CBC and lipids. A clear, step-by-step guide.",
            "de": "Referenzbereich, Einheiten und Werte im Blutbefund verstehen. Laborwerte einordnen — Schritt für Schritt, verständlich.",
            "it": "Cosa significano intervallo di riferimento, unità e valori sul referto. Guida passo passo in linguaggio semplice.",
            "es": "Qué significan rango de referencia, unidades y valores en el análisis. Guía paso a paso en lenguaje claro.",
            "fr": "Fourchette de référence, unités et valeurs sur la prise de sang : explications. Guide pas à pas en langage simple.",
            "he": "מה משמעות טווח הנורמה, היחידות והערכים בתוצאות הבדיקה. מדריך שלב-אחר-שלב בשפה פשוטה.",
            "ar": "معنى نطاق المرجع والوحدات والقيم في تحليل الدم. دليل خطوة بخطوة بلغة واضحة.",
            "hi": "ब्लड टेस्ट रिपोर्ट में रेफरेंस रेंज, यूनिट और वैल्यू का मतलब। सरल भाषा में स्टेप-बाय-स्टेप गाइड।",
            "el": "Τι σημαίνουν το διάστημα αναφοράς, οι μονάδες και οι τιμές στο αποτέλεσμα. Οδηγός βήμα-βήμα με απλή γλώσσα.",
            "cs": "Co znamená referenční rozmezí, jednotky a hodnoty na protokolu. Přehledný krok-za-krokem průvodce.",
            "sr": "Шта значи референтни опсег, јединице и вредности на анализи. Водич корак-по-корак јасним језиком.",
        },
        sections_by_lang={
            "tr": [
                Section(
                    id="tahlil-sonucu-nedir",
                    level=2,
                    heading="Kan tahlili sonucu nedir?",
                    body_html="""
<p>Kan tahlili (laboratuvar testi), kandaki belirli maddelerin miktarını veya varlığını ölçer. Sonuç kâğıdında her parametre için
bir <strong>sayı</strong>, çoğu zaman bir <strong>birim</strong> (ör. mg/dL, mmol/L) ve sıklıkla bir <strong>referans aralığı</strong> yer alır.</p>
<div class="blog-definition">
  <p><strong>Kan tahlili:</strong> Alınan kan örneğinin laboratuvarda incelenmesiyle elde edilen; şeker, kolesterol, vitamin, mineral,
  enzim veya hormon gibi değerlerin sayısal sonuçlarını gösteren rapor. Teşhis koymak için tek başına yeterli değildir;
  hekimin klinik değerlendirmesiyle birlikte yorumlanır.</p>
</div>
<p>Bu yazıda, sonuç kâğıdını okurken karşınıza çıkan terimleri ve sayıları nasıl anlayacağınızı adım adım ele alıyoruz.</p>
""",
                ),
                Section(
                    id="referans-araligi",
                    level=2,
                    heading="Referans aralığı ne anlama gelir?",
                    body_html="""
<p>Referans aralığı (normal aralık), sağlıklı bir popülasyonda o parametre için kabul edilen alt ve üst sınırlardır. Sonuç bu
aralığın <strong>içindeyse</strong> çoğu kılavuzda “normal sınırlarda” kabul edilir; <strong>dışındaysa</strong> düşük veya yüksek olarak işaretlenebilir.</p>
<div class="blog-definition">
  <p><strong>Referans aralığı:</strong> Laboratuvarın veya kılavuzların, “sağlıklı” kabul edilen bir grupta yapılan ölçümlere dayanarak
  belirlediği alt ve üst sınırlar. Örneğin “LDL 70–130 mg/dL” yazıyorsa, bu aralık o laboratuvar için kullanılan referans değerleridir.</p>
</div>
<div class="blog-example">
  <p><strong>Örnek:</strong> Sonuç kâğıdında <strong>Hemoglobin: 14,2 g/dL</strong> ve yanında <strong>Referans: 12–16 g/dL</strong> görüyorsanız,
  14,2 bu aralığın içinde olduğu için değer “normal sınırlarda” kabul edilir. 10 g/dL yazsaydı, referansın altında kalırdı ve
  “düşük” olarak yorumlanırdı.</p>
</div>
<p>Referans aralıkları laboratuvardan laboratuvara, cinsiyet ve yaş gruplarına göre hafifçe değişebilir. Bu yüzden her zaman
kâğıtta yazan aralığa göre yorum yapılır.</p>
""",
                ),
                Section(
                    id="sonuc-kagidinda-neler-var",
                    level=2,
                    heading="Sonuç kâğıdında neler bulunur?",
                    body_html="""
<p>Tipik bir kan tahlili sonuç sayfasında şu sütunlar yer alır:</p>
<ul>
  <li><strong>Parametre adı</strong>: Ölçülen değerin adı (örn. LDL kolesterol, Açlık glukozu, Hemoglobin).</li>
  <li><strong>Sonuç / Değer</strong>: Sizin ölçümünüz (sayı + birim).</li>
  <li><strong>Referans aralığı</strong>: O laboratuvar için kullanılan normal alt–üst sınırlar.</li>
  <li><strong>Birim</strong>: mg/dL, mmol/L, g/dL, U/L vb. Değeri doğru yorumlamak için birime bakmak gerekir.</li>
</ul>
<p>Bazı laboratuvarlar “Normal / Düşük / Yüksek” gibi bir etiket de ekler. Bu etiket, sonucun referans aralığına göre otomatik
üretilir; ancak sizin için “hedef” değer risk faktörlerinize göre farklı olabileceği için, nihai yorumu hekiminizle yapmanız önemlidir.</p>
""",
                ),
                Section(
                    id="yuksek-dusuk-deger",
                    level=2,
                    heading="Değer yüksek veya düşük çıkarsa",
                    body_html="""
<p>Bir değer referans aralığının <strong>dışında</strong> çıktığında, bu mutlaka “hastalık” anlamına gelmez. Geçici enfeksiyon, açlık süresi,
kullanılan ilaçlar veya laboratuvar tekniği gibi faktörler sonucu etkileyebilir. Hekiminiz, sizin öykünüz ve diğer tetkiklerle birlikte
bu sonucun anlamını değerlendirir; gerekirse tekrar test veya ek inceleme önerebilir.</p>
<p>Bu rehber, tahlil kâğıdındaki terimleri ve sayıları <strong>daha iyi anlamanız</strong> için hazırlanmıştır. Teşhis veya tedavi kararı yerine
geçmez; tüm sağlık kararlarında hekiminize danışınız.</p>
""",
                ),
            ],
            "en": [
                Section(
                    id="safety-note",
                    level=2,
                    heading="Before you start: safety note",
                    body_html="""
<section>
  <p><strong>Important:</strong> This guide is educational and does not replace medical advice. If you have severe symptoms, very abnormal values, or concerns, contact a clinician.</p>
</section>
""",
                ),
                Section(
                    id="what-is-report",
                    level=2,
                    heading="What is a blood test report?",
                    body_html="""
<section>
  <p>A blood test report (lab report) lists measurements from your blood sample. Each line usually includes: a <strong>test name</strong>, your <strong>value</strong>, the <strong>unit</strong>, and a <strong>reference range</strong> (sometimes called “normal range”).</p>
  <p>Different labs may use different methods and ranges, so always interpret results <strong>with the lab’s own reference range</strong>.</p>
</section>
""",
                ),
                Section(
                    id="step-1-context",
                    level=2,
                    heading="Step 1 — Start with the context",
                    body_html="""
<section>
  <ul>
    <li><strong>Why was the test ordered?</strong> Screening, symptoms, follow-up, medication monitoring?</li>
    <li><strong>Were you fasting?</strong> Lipids and glucose-related tests may be affected.</li>
    <li><strong>Recent illness, exercise, alcohol, supplements?</strong> These can shift values.</li>
    <li><strong>Timing matters:</strong> A single result is a snapshot—trends are often more meaningful.</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="step-2-four-things",
                    level=2,
                    heading="Step 2 — Understand the four things on each line",
                    body_html="""
<section>
  <ol>
    <li><strong>Test name:</strong> what was measured (e.g., Hemoglobin, ALT, Ferritin).</li>
    <li><strong>Your value:</strong> the number reported.</li>
    <li><strong>Unit:</strong> how it’s measured (e.g., mg/dL, mmol/L, U/L).</li>
    <li><strong>Reference range:</strong> expected range for a population under lab conditions.</li>
  </ol>
  <blockquote>
    <p><strong>Pro tip:</strong> Being slightly outside the range doesn’t automatically mean disease. It can reflect hydration, recent activity, timing, or lab variation.</p>
  </blockquote>
</section>
""",
                ),
                Section(
                    id="step-3-reference-range",
                    level=2,
                    heading="Step 3 — What does “reference range” actually mean?",
                    body_html="""
<section>
  <p>A reference range is often built so that most healthy people fall inside it (commonly around 95%). That means some healthy people will naturally fall slightly below or above.</p>
  <p>Reference ranges also vary by <strong>age</strong>, <strong>sex</strong>, pregnancy status, altitude, and lab method.</p>
</section>
""",
                ),
                Section(
                    id="step-4-flags",
                    level=2,
                    heading="Step 4 — High / Low flags: when to pay attention",
                    body_html="""
<section>
  <p>Reports may show flags like <strong>H</strong> (high) or <strong>L</strong> (low). Use these flags as a signal to look closer, not a diagnosis.</p>
  <ul>
    <li><strong>Mild:</strong> close to the range — often re-check or consider context.</li>
    <li><strong>Moderate:</strong> clearly out of range — consider repeat plus clinical correlation.</li>
    <li><strong>Severe:</strong> far out of range — follow lab or clinician instructions promptly.</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="step-5-panels",
                    level=2,
                    heading="Step 5 — Learn the common panels first",
                    body_html="""
<section>
  <h3>Complete Blood Count (CBC)</h3>
  <p>CBC describes blood cells and oxygen-carrying capacity. Common items include:</p>
  <ul>
    <li><strong>WBC:</strong> white blood cells (immune response)</li>
    <li><strong>RBC / HGB / HCT:</strong> red cells and oxygen transport</li>
    <li><strong>PLT:</strong> platelets (clotting)</li>
    <li><strong>MCV / MCH / MCHC / RDW:</strong> red cell size and hemoglobin patterns</li>
  </ul>

  <h3>Basic metabolic / chemistry</h3>
  <ul>
    <li><strong>Glucose:</strong> blood sugar</li>
    <li><strong>Creatinine / eGFR:</strong> kidney function indicators</li>
    <li><strong>Sodium / Potassium:</strong> electrolytes</li>
  </ul>

  <h3>Liver enzymes</h3>
  <ul>
    <li><strong>ALT / AST:</strong> liver cell stress or injury markers (non-specific)</li>
    <li><strong>ALP / GGT / Bilirubin:</strong> bile flow and related pathways</li>
  </ul>

  <h3>Lipids</h3>
  <ul>
    <li><strong>Total Cholesterol, LDL, HDL, Triglycerides</strong></li>
    <li>Interpret in the context of risk factors and fasting status.</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="step-6-units",
                    level=2,
                    heading="Step 6 — Units and conversions",
                    body_html="""
<section>
  <p>Some results appear in different units depending on the country or lab (for example, glucose in mg/dL versus mmol/L). If you compare results between reports, confirm units match before assuming there is a change.</p>
</section>
""",
                ),
                Section(
                    id="step-7-trends",
                    level=2,
                    heading="Step 7 — Trends beat single numbers",
                    body_html="""
<section>
  <p>If you have multiple tests over time, look for:</p>
  <ul>
    <li><strong>Direction:</strong> improving, stable, or worsening</li>
    <li><strong>Speed:</strong> sudden shifts usually matter more</li>
    <li><strong>Consistency:</strong> repeat abnormal results are more significant than a one-off outlier</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="when-to-seek-help",
                    level=2,
                    heading="When to seek medical advice urgently",
                    body_html="""
<section>
  <p>Seek urgent care if you have severe symptoms such as chest pain, fainting, shortness of breath, or confusion, or if your lab result is marked as critical and the lab or clinic advises immediate action.</p>
</section>
""",
                ),
                Section(
                    id="try-clearer-report",
                    level=2,
                    heading="Try a clearer report view",
                    body_html="""
<section>
  <p>If you want a more structured overview, you can upload your lab PDF and get a clean, readable summary with key terms and reference ranges.</p>
  <p><a href="/analyze">Analyze your blood test →</a></p>
</section>
""",
                ),
            ],
        },
    )


_KAN_TAHLILI_ARTICLE = _article_kan_tahlili_nasil_okunur()


def _article_ferritin() -> Article:
    """Ferritin: low/high meaning, reference ranges, when to see a doctor."""
    published = date(2026, 3, 5)
    updated = date(2026, 3, 5)
    cover = "/static/images/blog/ferritin-hero.png"
    return Article(
        id="ferritin-what-it-means",
        published_at=published,
        read_minutes=10,
        cover_image=cover,
        category={
            "tr": "Demir ve Anemi",
            "en": "Iron & Anemia",
            "es": "Hierro y anemia",
            "de": "Eisen & Anämie",
            "fr": "Fer et anémie",
            "it": "Ferro e anemia",
            "he": "ברזל ואנמיה",
            "hi": "आयरन और एनीमिया",
            "ar": "الحديد وفقر الدم",
        },
        slugs={
            "tr": "ferritin-dusuk-yuksek-ne-anlama-gelir",
            "en": "ferritin-what-it-means",
            "es": "ferritina-baja-alta-significado",
            "de": "ferritin-what-it-means",
            "fr": "ferritin-what-it-means",
            "it": "ferritin-what-it-means",
            "he": "ferritin-what-it-means",
            "hi": "ferritin-kya-hai-low-high",
            "ar": "ferritin-what-it-means",
        },
        titles={
            "tr": "Ferritin Düşük Ne Anlama Gelir: Düşük veya Yüksek Ferritin Ne Gösterebilir",
            "en": "Ferritin Low Meaning: What Low or High Ferritin Levels May Indicate",
            "es": "Ferritina baja: qué pueden indicar niveles bajos o altos",
            "de": "Ferritin niedrig: Was niedrige oder hohe Werte bedeuten können",
            "fr": "Ferritine basse : ce que des taux bas ou élevés peuvent indiquer",
            "it": "Ferritina bassa: cosa possono indicare valori bassi o alti",
            "he": "פריטין נמוך: מה ערכים נמוכים או גבוהים עלולים להצביע",
            "hi": "फेरिटिन कम: कम या ज़्यादा स्तर क्या संकेत दे सकते हैं",
            "ar": "الفيريتين منخفض أو مرتفع: ماذا قد تعني النتائج",
        },
        subtitles={
            "tr": "Ferritin, demir depoları, referans aralıkları, düşük/yüksek nedenleri ve ne zaman doktora gidilmeli rehberi.",
            "en": "A clear guide to ferritin, iron stores, reference ranges, common causes of low or high results, and when to see a doctor.",
            "es": "Guía sobre ferritina, reservas de hierro, rangos de referencia y cuándo consultar al médico.",
            "de": "Ein Überblick über Ferritin, Eisenspeicher, Referenzbereiche, häufige Ursachen für niedrige oder hohe Werte und wann Sie zum Arzt sollten.",
            "fr": "Guide clair sur la ferritine, les réserves en fer, les fourchettes de référence, les causes fréquentes de taux bas ou élevés et quand consulter.",
            "it": "Guida chiara su ferritina, riserve di ferro, intervalli di riferimento, cause comuni di valori bassi o alti e quando rivolgersi al medico.",
            "he": "מדריך על פריטין, מאגרי ברזל, טווחי נורמה ומתי לפנות לרופא.",
            "hi": "फेरिटिन, आयरन स्टोर, रेफरेंस रेंज और डॉक्टर से कब मिलें — सरल गाइड।",
            "ar": "دليل واضح عن الفيريتين ومخزون الحديد ونطاقات المرجع ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "Ferritin reflects your body’s iron stores. Low or high levels can have many causes; interpretation should be done with a clinician and other tests.",
            "de": "Ferritin spiegelt die Eisenspeicher wider. Niedrige oder hohe Werte können viele Ursachen haben; die Einordnung erfolgt mit dem Arzt und weiteren Tests.",
            "it": "La ferritina riflette le riserve di ferro. Valori bassi o alti possono avere molte cause; l’interpretazione va fatta con il medico e altri esami.",
            "fr": "La ferritine reflète les réserves en fer. Un taux bas ou élevé peut avoir de nombreuses causes ; l’interprétation se fait avec un médecin et d’autres examens.",
            "ar": "الفيريتين يعكس مخزون الحديد في الجسم. المستوى المنخفض أو المرتفع قد يكون لأسباب كثيرة؛ التفسير يكون مع الطبيب.",
        },
        seo_titles={
            "tr": "Ferritin: Düşük ve Yüksek Değerler, Referans Aralığı",
            "en": "Ferritin Explained: Low vs High Levels, Reference Ranges & Next Steps",
            "es": "Ferritina: niveles bajos y altos, rangos de referencia",
            "de": "Ferritin: Niedrige und hohe Werte, Referenzbereich, Ursachen",
            "fr": "Ferritine : taux bas ou élevé, fourchettes de référence et suites",
            "it": "Ferritina: valori bassi e alti, intervalli di riferimento e cosa fare",
            "he": "פריטין: ערכים נמוכים וגבוהים, טווחי נורמה",
            "hi": "फेरिटिन: कम और ज़्यादा स्तर, रेफरेंस रेंज",
            "ar": "الفيريتين: المستويات المنخفضة والمرتفعة ونطاقات المرجع",
        },
        seo_descriptions={
            "en": "Understand ferritin and iron stores. What low or high ferritin means, common causes, reference ranges, when to see a doctor, and what to do next. Informational.",
            "de": "Ferritin und Eisenspeicher verstehen. Bedeutung niedriger/hoher Werte, Ursachen, Referenzbereich, wann zum Arzt und was Sie tun können. Nur zur Information.",
            "it": "Capire ferritina e riserve di ferro. Cosa significano valori bassi o alti, cause comuni, intervalli di riferimento, quando rivolgersi al medico. Solo informativo.",
            "fr": "Comprendre la ferritine et les réserves en fer. Taux bas ou élevé, causes fréquentes, fourchettes de référence, quand consulter et quoi faire. À titre informatif.",
            "tr": "Ferritin ve demir depoları. Düşük/yüksek ferritin ne anlama gelir, referans aralığı, ne zaman doktora gidilmeli. Bilgilendirme amaçlıdır.",
            "es": "Entiende la ferritina y las reservas de hierro. Niveles bajos o altos, causas, rangos y cuándo consultar. Solo informativo.",
            "he": "הבן פריטין ומאגרי ברזל. ערכים נמוכים/גבוהים, סיבות, טווחי נורמה ומתי לרופא. למידע בלבד.",
            "hi": "फेरिटिन और आयरन स्टोर समझें। कम/ज़्यादा मतलब, कारण, रेंज और डॉक्टर से कब मिलें। सूचनात्मक।",
            "ar": "افهم الفيريتين ومخزون الحديد. ماذا تعني القيمة المنخفضة أو المرتفعة ومتى ترى الطبيب. للمعلومات فقط.",
        },
        sections_by_lang={
            "en": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="What is ferritin?",
                    body_html="""
<p>Ferritin is a protein that stores iron and releases it in a controlled way when the body needs it. Measured in blood, ferritin is the most practical indicator of your body’s <strong>iron stores</strong>. It is not the same as “serum iron” (the iron circulating in the blood at the moment of the test), which can vary with meals and time of day.</p>
<p>Low ferritin usually suggests depleted iron stores and may point to iron deficiency if other causes are ruled out. High ferritin can reflect excess iron storage, but it is also an <strong>acute-phase reactant</strong>: it often rises with inflammation, infection, or liver conditions, so a high value does not automatically mean too much iron. Interpretation should always be done together with your doctor and, when needed, additional tests.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritin vs iron vs transferrin vs TSAT",
                    body_html="""
<p>These tests are often ordered together to assess iron status. A short overview:</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Test</th><th class="border border-slate-300 px-3 py-2 text-left">What it reflects</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritin</strong></td><td class="border border-slate-300 px-3 py-2">Iron stores (storage form). Best single marker for deficiency.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Serum iron</strong></td><td class="border border-slate-300 px-3 py-2">Iron in circulation at time of draw. Varies with diet and time of day.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrin / TIBC</strong></td><td class="border border-slate-300 px-3 py-2">Iron-carrying capacity. Often high when stores are low.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>TSAT</strong></td><td class="border border-slate-300 px-3 py-2">Transferrin saturation. Low in deficiency; very high may suggest overload.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Low ferritin: causes and symptoms",
                    body_html="""
<p><strong>Common causes</strong> of low ferritin include: blood loss (heavy periods, digestive bleeding, surgery), low dietary intake or poor absorption (e.g. coeliac disease, gastric surgery), increased needs (pregnancy, growth, intense training), and chronic inflammation affecting absorption. More than one factor can apply at once.</p>
<p><strong>Common symptoms</strong> that may be associated with low iron stores include fatigue, weakness, pale skin, shortness of breath on exertion, dizziness, cold hands and feet, brittle nails, and hair loss. These are non-specific: they can have many other causes. <strong>Symptoms alone do not establish a diagnosis</strong>; they must be interpreted together with blood tests and clinical history by a doctor.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="High ferritin: causes and acute-phase reaction",
                    body_html="""
<p><strong>Common causes</strong> of elevated ferritin include: inflammation or infection (ferritin is an acute-phase reactant and often rises even when iron stores are normal), fatty liver disease, alcohol use, metabolic syndrome, obesity, and in some cases hereditary haemochromatosis or other iron overload conditions. Liver damage or chronic disease can also raise ferritin.</p>
<p>Because <strong>ferritin is an acute-phase reactant</strong>, it often increases during illness, infection, or inflammation. A high result does not necessarily mean excess iron; your doctor will consider CRP, serum iron, TIBC, TSAT, and sometimes imaging or genetic testing to clarify.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="What ranges are “normal”?",
                    body_html="""
<p>Reference ranges for ferritin <strong>differ by laboratory</strong> (method and population). Always use the range printed on your own report. As a rough guide only: in many labs, approximate ranges are around <strong>12–150 ng/mL for adult women</strong> and <strong>30–300 ng/mL (or higher) for adult men</strong>. Values may be lower in menstruating women and higher in older adults. These figures are illustrative; your lab’s reference is the one that applies to your result.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="When to see a doctor",
                    body_html="""
<p>See a doctor if: ferritin is very low or very high; you have low haemoglobin (anaemia) or symptoms such as unexplained fatigue, shortness of breath, or dizziness; you have fever, weight loss, or signs of liver disease; or other blood tests (e.g. liver enzymes) are abnormal. Early discussion with a clinician allows proper work-up (e.g. CBC, CRP, serum iron, TIBC, TSAT, B12, folate) and, if needed, treatment or referral.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="What might happen next",
                    body_html="""
<p>Depending on your result and history, your doctor may order further tests: full blood count (CBC), CRP, serum iron, TIBC, TSAT, vitamin B12, folate, and sometimes tests for coeliac disease or digestive bleeding. <strong>Lifestyle and diet</strong>: if deficiency is confirmed, iron-rich foods and, if prescribed, supplements can help; avoid self-dosing high amounts. For high ferritin, the cause must be clarified first (inflammation, liver, metabolic, or genetic); diet and lifestyle advice will depend on that. Always follow your doctor’s recommendations.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Frequently asked questions",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">What is a “normal” ferritin level?</h3>
<p>“Normal” depends on your lab’s reference range, age, and sex. Use the range on your report; your doctor can say whether your value is appropriate for you.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can low ferritin cause hair loss?</h3>
<p>Low iron stores are sometimes associated with hair thinning or loss, but many other factors (hormones, stress, diet) also play a role. Correcting deficiency may help in some people; a doctor can advise.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What raises ferritin besides iron?</h3>
<p>Inflammation, infection, liver disease, alcohol, metabolic syndrome, and certain medications can raise ferritin without true iron overload. That’s why high ferritin is interpreted together with other tests.</p>
<h3 class="text-base font-semibold mt-4 mb-1">How long until supplements affect ferritin?</h3>
<p>If you are prescribed iron for deficiency, ferritin may start to rise over several weeks; full repletion can take months. Follow your doctor’s dosing and repeat-test schedule.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is ferritin tested fasting?</h3>
<p>Ferritin is usually not strongly affected by a recent meal, but your lab may request fasting for a panel that includes glucose or lipids. Follow the instructions given for your blood draw.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can I interpret ferritin alone?</h3>
<p>Ferritin is best interpreted with clinical context and often with serum iron, TIBC, TSAT, and sometimes CRP or other tests. Your doctor can give a proper interpretation.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Disclaimer",
                    body_html="""
<p><strong>This content is for information only and does not constitute medical advice.</strong> Always discuss your results and symptoms with a doctor. Do not start or change supplements or treatment based solely on this article.</p>
""",
                ),
            ],
            "de": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="Was ist Ferritin?",
                    body_html="""
<p>Ferritin ist ein Speichereiweiß für Eisen, das bei Bedarf kontrolliert abgegeben wird. Im Blut gemessen, ist Ferritin der praktischste Indikator für Ihre <strong>Eisenspeicher</strong>. Es ist nicht dasselbe wie „Serumeisen“ (das zum Zeitpunkt der Abnahme zirkulierende Eisen), das mit Mahlzeiten und Tageszeit schwanken kann.</p>
<p>Niedriges Ferritin spricht oft für leere Eisenspeicher und kann auf einen Eisenmangel hindeuten, wenn andere Ursachen ausgeschlossen sind. Hohes Ferritin kann auf zu viel gespeichertes Eisen hindeuten, ist aber auch ein <strong>Akute-Phase-Protein</strong>: Es steigt oft bei Entzündung, Infektion oder Lebererkrankung – ein hoher Wert bedeutet also nicht automatisch Eisenüberladung. Die Einordnung erfolgt immer gemeinsam mit dem Arzt und gegebenenfalls weiteren Tests.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritin vs. Eisen vs. Transferrin vs. TSAT",
                    body_html="""
<p>Diese Werte werden oft gemeinsam bestimmt. Kurzüberblick:</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Parameter</th><th class="border border-slate-300 px-3 py-2 text-left">Bedeutung</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritin</strong></td><td class="border border-slate-300 px-3 py-2">Eisenspeicher. Bester Einzelmarker bei Mangel.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Serumeisen</strong></td><td class="border border-slate-300 px-3 py-2">Zirkulierendes Eisen zum Abnahmezeitpunkt. Variiert mit Ernährung und Tageszeit.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrin / TIBC</strong></td><td class="border border-slate-300 px-3 py-2">Eisentransportkapazität. Oft erhöht bei niedrigen Speichern.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>TSAT</strong></td><td class="border border-slate-300 px-3 py-2">Transferrinsättigung. Niedrig bei Mangel; sehr hoch kann auf Überladung hindeuten.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Niedriges Ferritin: Ursachen und Symptome",
                    body_html="""
<p><strong>Häufige Ursachen</strong> sind: Blutverlust (starke Regelblutung, Magen-Darm-Blutungen, OP), geringe Aufnahme oder schlechte Resorption (z. B. Zöliakie, Magen-OP), erhöhter Bedarf (Schwangerschaft, Wachstum, intensiver Sport), chronische Entzündung. Mehrere Faktoren können zusammenspielen.</p>
<p><strong>Mögliche Symptome</strong> bei niedrigen Eisenspeichern: Müdigkeit, Schwäche, blasse Haut, Atemnot bei Belastung, Schwindel, kalte Hände/Füße, brüchige Nägel, Haarausfall. Diese sind unspezifisch und können viele andere Ursachen haben. <strong>Symptome allein stellen keine Diagnose</strong>; die Bewertung erfolgt durch den Arzt anhand von Blutwerten und Anamnese.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="Hohes Ferritin: Ursachen und Akute-Phase-Reaktion",
                    body_html="""
<p><strong>Häufige Ursachen</strong> erhöhten Ferritins: Entzündung oder Infektion (Ferritin ist ein Akute-Phase-Protein und steigt oft auch bei normalen Speichern), Fettleber, Alkohol, metabolisches Syndrom, Adipositas, in Einzelfällen hereditäre Hämochromatose oder andere Eisenüberladung. Auch Leberschaden oder chronische Erkrankung können Ferritin anheben.</p>
<p>Da <strong>Ferritin ein Akute-Phase-Protein ist</strong>, steigt es bei Krankheit, Infekt oder Entzündung oft an. Ein hoher Wert bedeutet nicht zwingend Eisenüberschuss; der Arzt zieht CRP, Serumeisen, TIBC, TSAT und ggf. Bildgebung oder Genetik zur Klärung heran.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="Welche Bereiche gelten als „normal“?",
                    body_html="""
<p>Referenzbereiche für Ferritin <strong>unterscheiden sich je nach Labor</strong> (Methode und Population). Orientieren Sie sich immer am Bereich auf Ihrem Befund. Nur zur groben Einordnung: In vielen Laboren liegen die Bereiche etwa bei <strong>12–150 ng/mL für erwachsene Frauen</strong> und <strong>30–300 ng/mL (oder höher) für Männer</strong>. Bei menstruierenden Frauen oft niedriger, bei Älteren teils höher. Diese Angaben sind nur Richtwerte; maßgeblich ist der Referenzbereich Ihres Labors.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Wann zum Arzt?",
                    body_html="""
<p>Gehen Sie zum Arzt, wenn: Ferritin stark erniedrigt oder stark erhöht ist; Sie niedrigen Hämoglobinwert (Anämie) oder Symptome wie unklare Müdigkeit, Atemnot oder Schwindel haben; Fieber, Gewichtsverlust oder Hinweise auf Lebererkrankung bestehen; oder andere Blutwerte (z. B. Leberenzyme) auffällig sind. Eine zeitige Abklärung (z. B. Blutbild, CRP, Serumeisen, TIBC, TSAT, B12, Folsäure) ermöglicht bei Bedarf gezielte Therapie oder Überweisung.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="Was kann als Nächstes passieren?",
                    body_html="""
<p>Je nach Befund und Vorgeschichte kann der Arzt weitere Tests veranlassen: großes Blutbild, CRP, Serumeisen, TIBC, TSAT, Vitamin B12, Folsäure, ggf. Zöliakie- oder Blutungsabklärung. <strong>Lebensstil und Ernährung:</strong> Bei bestätigtem Mangel können eisenreiche Ernährung und ggf. vom Arzt verordnete Präparate helfen; hohe Dosen nicht auf eigene Faust. Bei hohem Ferritin muss zuerst die Ursache geklärt werden (Entzündung, Leber, Stoffwechsel, Genetik); darauf basieren dann Empfehlungen. Bitte folgen Sie den Anweisungen Ihres Arztes.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Häufige Fragen",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Was ist ein „normaler“ Ferritin-Wert?</h3>
<p>„Normal“ hängt vom Referenzbereich des Labors, Alter und Geschlecht ab. Verwenden Sie den Bereich auf Ihrem Befund; Ihr Arzt kann einschätzen, ob Ihr Wert für Sie passend ist.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann niedriges Ferritin Haarausfall verursachen?</h3>
<p>Niedrige Eisenspeicher werden manchmal mit dünner werdendem oder ausfallendem Haar in Verbindung gebracht, aber auch Hormone, Stress und Ernährung spielen eine Rolle. Die Korrektur eines Mangels kann bei einigen helfen; der Arzt berät.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Was erhöht Ferritin außer Eisen?</h3>
<p>Entzündung, Infektion, Lebererkrankung, Alkohol, metabolisches Syndrom und bestimmte Medikamente können Ferritin anheben, ohne echte Eisenüberladung. Daher wird hohes Ferritin immer mit anderen Werten zusammen beurteilt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wie lange dauert es, bis Eisenpräparate wirken?</h3>
<p>Bei verordneter Eisensubstitution kann Ferritin über einige Wochen ansteigen; die Auffüllung der Speicher kann Monate dauern. Halten Sie Dosis und Kontrolltermine ein.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wird Ferritin nüchtern gemessen?</h3>
<p>Ferritin wird durch eine Mahlzeit meist wenig beeinflusst; das Labor kann aber Nüchternheit für ein Profil mit Glukose/Lipiden verlangen. Bitte die Anweisungen zur Blutabnahme beachten.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann ich Ferritin allein interpretieren?</h3>
<p>Ferritin wird am besten im klinischen Kontext und oft zusammen mit Serumeisen, TIBC, TSAT und ggf. CRP beurteilt. Ihr Arzt kann es fachgerecht einordnen.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Hinweis",
                    body_html="""
<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung.</strong> Besprechen Sie Ihre Ergebnisse und Beschwerden immer mit einem Arzt. Setzen Sie keine Präparate ein oder ändern Sie die Therapie nicht nur aufgrund dieses Artikels.</p>
""",
                ),
            ],
            "it": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="Cos’è la ferritina?",
                    body_html="""
<p>La ferritina è una proteina che immagazzina il ferro e lo rilascia in modo controllato quando l’organismo ne ha bisogno. Misurata nel sangue, è l’indicatore più utile delle <strong>riserve di ferro</strong>. Non va confusa con il “ferro sierico” (il ferro in circolo al momento del prelievo), che può variare con i pasti e l’ora del giorno.</p>
<p>Una ferritina bassa suggerisce spesso riserve ridotte e può indicare carenza di ferro se altre cause sono escluse. Una ferritina alta può riflettere un eccesso di ferro accumulato, ma è anche un <strong>reattante di fase acuta</strong>: aumenta spesso con infiammazione, infezione o patologie epatiche, quindi un valore alto non significa automaticamente sovraccarico. L’interpretazione va sempre fatta con il medico e, se necessario, con altri esami.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritina vs ferro vs transferrina vs TSAT",
                    body_html="""
<p>Questi esami sono spesso richiesti insieme per valutare il ferro. In sintesi:</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Esame</th><th class="border border-slate-300 px-3 py-2 text-left">Cosa riflette</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritina</strong></td><td class="border border-slate-300 px-3 py-2">Riserve di ferro. Miglior marcatore singolo in caso di carenza.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferro sierico</strong></td><td class="border border-slate-300 px-3 py-2">Ferro in circolo al prelievo. Varia con dieta e orario.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrina / TIBC</strong></td><td class="border border-slate-300 px-3 py-2">Capacità di trasporto del ferro. Spesso alta quando le riserve sono basse.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>TSAT</strong></td><td class="border border-slate-300 px-3 py-2">Saturazione della transferrina. Bassa in carenza; molto alta può far sospettare sovraccarico.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Ferritina bassa: cause e sintomi",
                    body_html="""
<p><strong>Cause comuni</strong> di ferritina bassa: perdite di sangue (mestruazioni abbondanti, sanguinamento digestivo, interventi), scarso apporto o malassorbimento (es. celiachia, chirurgia gastrica), aumentato fabbisogno (gravidanza, crescita, sport intenso), infiammazione cronica. Più fattori possono coesistere.</p>
<p><strong>Sintomi comuni</strong> associati a riserve basse: stanchezza, debolezza, pallore, fiato corto sotto sforzo, capogiri, mani e piedi freddi, unghie fragili, caduta dei capelli. Sono aspecifici e possono dipendere da molte altre cause. <strong>I sintomi da soli non consentono la diagnosi</strong>; vanno interpretati dal medico insieme agli esami e alla storia clinica.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="Ferritina alta: cause e reattante di fase acuta",
                    body_html="""
<p><strong>Cause comuni</strong> di ferritina elevata: infiammazione o infezione (la ferritina è un reattante di fase acuta e sale spesso anche con riserve normali), steatosi epatica, alcol, sindrome metabolica, obesità, in alcuni casi emocromatosi ereditaria o altro sovraccarico. Anche danno epatico o malattia cronica possono alzare la ferritina.</p>
<p>Poiché <strong>la ferritina è un reattante di fase acuta</strong>, aumenta spesso in corso di malattia, infezione o infiammazione. Un valore alto non significa necessariamente eccesso di ferro; il medico valuterà CRP, ferro sierico, TIBC, TSAT e eventualmente imaging o genetica per chiarire.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="Quali intervalli sono “normali”?",
                    body_html="""
<p>Gli intervalli di riferimento per la ferritina <strong>variano da laboratorio a laboratorio</strong>. Usate sempre quello indicato sul vostro referto. Solo a titolo orientativo: in molti laboratori si usano intervalli approssimativi di circa <strong>12–150 ng/mL per le donne adulte</strong> e <strong>30–300 ng/mL (o più) per gli uomini</strong>. I valori possono essere più bassi nelle donne in età fertile e più alti negli anziani. Queste cifre sono indicative; fa fede l’intervallo del vostro laboratorio.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quando rivolgersi al medico",
                    body_html="""
<p>Consultate il medico se: la ferritina è molto bassa o molto alta; avete emoglobina bassa (anemia) o sintomi come stanchezza inspiegabile, fiato corto o capogiri; avete febbre, perdita di peso o segni di malattia epatica; oppure altri esami (es. enzimi epatici) sono alterati. Una valutazione tempestiva (es. emocromo, CRP, ferro sierico, TIBC, TSAT, B12, folati) permette eventuale terapia o invio allo specialista.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="Cosa può succedere dopo",
                    body_html="""
<p>In base al risultato e alla storia, il medico può prescrivere altri esami: emocromo, CRP, ferro sierico, TIBC, TSAT, vitamina B12, folati, e a volte test per celiachia o sanguinamento digestivo. <strong>Stile di vita e dieta:</strong> in caso di carenza accertata, alimenti ricchi di ferro e, se prescritti, integratori possono aiutare; evitate dosi elevate fai-da-te. Per ferritina alta va prima chiarita la causa (infiammazione, fegato, metabolismo, genetica); le indicazioni dipendono da quella. Seguite sempre le indicazioni del medico.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Domande frequenti",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Qual è un livello “normale” di ferritina?</h3>
<p>“Normale” dipende dall’intervallo del laboratorio, dall’età e dal sesso. Usate l’intervallo sul referto; il medico può dirvi se il valore è adeguato per voi.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritina bassa può causare caduta dei capelli?</h3>
<p>Riserve di ferro basse sono a volte associate a diradamento o caduta; anche ormoni, stress e dieta contano. Correggere la carenza può aiutare in alcuni casi; il medico può consigliare.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Cosa alza la ferritina oltre al ferro?</h3>
<p>Infiammazione, infezione, malattia epatica, alcol, sindrome metabolica e alcuni farmaci possono alzare la ferritina senza vero sovraccarico. Per questo la ferritina alta si interpreta con altri esami.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Quanto tempo prima che gli integratori influenzino la ferritina?</h3>
<p>Se vi viene prescritto ferro per carenza, la ferritina può iniziare a salire in alcune settimane; il ripristino completo può richiedere mesi. Rispettate dosi e controlli indicati dal medico.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritina si misura a digiuno?</h3>
<p>La ferritina di solito non è influenzata dal pasto; il laboratorio può richiedere il digiuno per un pannello che include glucosio o lipidi. Seguite le istruzioni per il prelievo.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Posso interpretare la ferritina da solo?</h3>
<p>La ferritina si interpreta meglio con il contesto clinico e spesso con ferro sierico, TIBC, TSAT e a volte CRP. Il medico può dare un’interpretazione corretta.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Nota",
                    body_html="""
<p><strong>Questo contenuto è solo informativo e non costituisce consulenza medica.</strong> Discutete sempre risultati e sintomi con un medico. Non iniziare o modificare integratori o cure solo in base a questo articolo.</p>
""",
                ),
            ],
            "fr": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="Qu’est-ce que la ferritine ?",
                    body_html="""
<p>La ferritine est une protéine qui stocke le fer et le libère de façon contrôlée lorsque l’organisme en a besoin. Dosée dans le sang, elle est le meilleur indicateur pratique de vos <strong>réserves en fer</strong>. Elle ne doit pas être confondue avec le « fer sérique » (fer circulant au moment du prélèvement), qui varie avec les repas et l’heure.</p>
<p>Une ferritine basse suggère souvent des réserves diminuées et peut indiquer une carence en fer si les autres causes sont écartées. Une ferritine élevée peut refléter un excès de stockage, mais c’est aussi un <strong>réactant de phase aiguë</strong> : elle augmente souvent avec l’inflammation, l’infection ou une atteinte hépatique, donc un taux élevé ne signifie pas automatiquement surcharge en fer. L’interprétation doit toujours se faire avec un médecin et, si besoin, d’autres examens.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritine vs fer vs transferrine vs CST",
                    body_html="""
<p>Ces paramètres sont souvent demandés ensemble pour évaluer le statut martial. En bref :</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Paramètre</th><th class="border border-slate-300 px-3 py-2 text-left">Signification</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritine</strong></td><td class="border border-slate-300 px-3 py-2">Réserves en fer. Meilleur marqueur isolé en cas de carence.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Fer sérique</strong></td><td class="border border-slate-300 px-3 py-2">Fer en circulation au moment du prélèvement. Varie avec l’alimentation et l’heure.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrine / CCT</strong></td><td class="border border-slate-300 px-3 py-2">Capacité de transport du fer. Souvent élevée quand les réserves sont basses.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>CST</strong></td><td class="border border-slate-300 px-3 py-2">Saturation de la transferrine. Basse en carence ; très élevée peut évoquer une surcharge.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Ferritine basse : causes et symptômes",
                    body_html="""
<p><strong>Causes fréquentes</strong> : pertes de sang (règles abondantes, saignements digestifs, chirurgie), faible apport ou mauvaise absorption (maladie cœliaque, chirurgie gastrique), besoins accrus (grossesse, croissance, sport intense), inflammation chronique. Plusieurs facteurs peuvent s’associer.</p>
<p><strong>Symptômes fréquents</strong> possibles en cas de réserves basses : fatigue, faiblesse, pâleur, essoufflement à l’effort, vertiges, mains et pieds froids, ongles fragiles, chute de cheveux. Ils sont non spécifiques et peuvent avoir bien d’autres causes. <strong>Les symptômes seuls ne permettent pas de poser un diagnostic</strong> ; ils doivent être interprétés par un médecin avec les examens et l’histoire clinique.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="Ferritine élevée : causes et réaction de phase aiguë",
                    body_html="""
<p><strong>Causes fréquentes</strong> de ferritine élevée : inflammation ou infection (la ferritine est un réactant de phase aiguë et monte souvent même avec des réserves normales), stéatose hépatique, alcool, syndrome métabolique, obésité, et parfois hémochromatose héréditaire ou autre surcharge. Une atteinte hépatique ou une maladie chronique peut aussi élever la ferritine.</p>
<p>Comme <strong>la ferritine est un réactant de phase aiguë</strong>, elle augmente souvent en cas de maladie, d’infection ou d’inflammation. Un taux élevé ne signifie pas forcément excès de fer ; le médecin s’appuiera sur la CRP, le fer sérique, la CCT, la CST et éventuellement l’imagerie ou la génétique pour préciser.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="Quelles fourchettes sont « normales » ?",
                    body_html="""
<p>Les fourchettes de référence pour la ferritine <strong>varient selon le laboratoire</strong>. Utilisez toujours celle indiquée sur votre résultat. À titre indicatif seulement : dans beaucoup de laboratoires, les fourchettes sont environ <strong>12–150 ng/mL pour les femmes adultes</strong> et <strong>30–300 ng/mL (ou plus) pour les hommes</strong>. Les valeurs peuvent être plus basses chez les femmes réglées et plus hautes chez les personnes âgées. Ces chiffres sont indicatifs ; c’est la fourchette de votre laboratoire qui s’applique.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quand consulter un médecin",
                    body_html="""
<p>Consultez si : la ferritine est très basse ou très élevée ; vous avez une hémoglobine basse (anémie) ou des symptômes comme une fatigue inexpliquée, un essoufflement ou des vertiges ; vous avez de la fièvre, une perte de poids ou des signes d’atteinte hépatique ; ou d’autres examens (ex. enzymes hépatiques) sont anormaux. Un avis médical précoce permet un bilan adapté (NFS, CRP, fer sérique, CCT, CST, B12, folates) et, si besoin, un traitement ou une orientation.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="Que peut-il se passer ensuite ?",
                    body_html="""
<p>Selon le résultat et l’histoire, le médecin peut prescrire d’autres examens : NFS, CRP, fer sérique, CCT, CST, vitamine B12, folates, et parfois dépistage de maladie cœliaque ou de saignement digestif. <strong>Hygiène de vie et alimentation :</strong> en cas de carence confirmée, aliments riches en fer et, si prescrits, compléments peuvent aider ; évitez les fortes doses en automédication. Pour une ferritine élevée, la cause doit d’abord être précisée (inflammation, foie, métabolisme, génétique) ; les conseils en dépendent. Suivez toujours les recommandations de votre médecin.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Questions fréquentes",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Quel est un taux « normal » de ferritine ?</h3>
<p>« Normal » dépend du laboratoire, de l’âge et du sexe. Utilisez la fourchette sur votre résultat ; votre médecin peut dire si la valeur vous convient.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritine basse peut-elle causer une chute de cheveux ?</h3>
<p>Des réserves basses sont parfois associées à une chute ou une perte de cheveux, mais d’autres facteurs (hormones, stress, alimentation) jouent aussi. Corriger la carence peut aider dans certains cas ; le médecin peut conseiller.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Qu’est-ce qui élève la ferritine en dehors du fer ?</h3>
<p>L’inflammation, l’infection, une maladie du foie, l’alcool, le syndrome métabolique et certains médicaments peuvent élever la ferritine sans vraie surcharge. C’est pourquoi un taux élevé est interprété avec d’autres examens.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Combien de temps avant que les compléments n’agissent sur la ferritine ?</h3>
<p>Si du fer vous est prescrit pour une carence, la ferritine peut commencer à remonter en quelques semaines ; le remplissage complet peut prendre des mois. Respectez la posologie et les contrôles prescrits.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritine se dose-t-elle à jeun ?</h3>
<p>La ferritine est en général peu influencée par un repas récent, mais le laboratoire peut demander le jeûne pour un bilan incluant glucose ou lipides. Suivez les consignes du prélèvement.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Puis-je interpréter la ferritine seul ?</h3>
<p>La ferritine s’interprète au mieux dans le contexte clinique et souvent avec le fer sérique, la CCT, la CST et parfois la CRP. Votre médecin peut en donner une interprétation adaptée.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Avertissement",
                    body_html="""
<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis médical.</strong> Discutez toujours de vos résultats et symptômes avec un médecin. Ne commencez ni ne modifiez un complément ou un traitement sur la seule base de cet article.</p>
""",
                ),
            ],
        },
        cover_alt={
            "en": "Ferritin blood test and lab dashboard — NoryaAI",
            "de": "Ferritin-Bluttest und Labor-Überblick — NoryaAI",
            "it": "Ferritin blood test and lab dashboard — NoryaAI",
            "fr": "Ferritin blood test and lab dashboard — NoryaAI",
        },
        last_updated=updated,
    )


_FERRITIN_ARTICLE = _article_ferritin()


def _article_crp() -> Article:
    """CRP: what it is, hs-CRP difference, when high, when to see a doctor. en, de, it, fr."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/crp-hero.png"
    cover_alt_text = {
        "en": "CRP blood test and inflammation dashboard — NoryaAI",
        "de": "CRP-Bluttest und Entzündungs-Dashboard — NoryaAI",
        "it": "Esame CRP e dashboard infiammazione — NoryaAI",
        "fr": "Dosage CRP et tableau de bord inflammation — NoryaAI",
        "ar": "تحليل CRP ولوحة الالتهاب — NoryaAI",
        "tr": "CRP kan testi ve inflamasyon paneli — NoryaAI",
        "es": "Análisis CRP y panel de inflamación — NoryaAI",
        "he": "בדיקת CRP ולוח דלקת — NoryaAI",
        "hi": "CRP ब्लड टेस्ट और इन्फ्लेमेशन डैशबोर्ड — NoryaAI",
    }
    return Article(
        id="crp-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=11,
        cover_image=cover,
        cover_alt=cover_alt_text,
        category={
            "tr": "İnflamasyon / Biyobelirteçler",
            "en": "Inflammation / Biomarkers",
            "es": "Inflamación / Biomarcadores",
            "de": "Entzündung / Biomarker",
            "fr": "Inflammation / Biomarqueurs",
            "it": "Infiammazione / Biomarcatori",
            "he": "דלקת / ביו-מרקרים",
            "hi": "सूजन / बायोमार्कर",
            "ar": "الالتهاب / المؤشرات الحيوية",
        },
        slugs={
            "tr": "crp-yuksek-ne-anlama-gelir",
            "en": "crp-what-it-means",
            "es": "crp-elevado-significado",
            "de": "crp-what-it-means",
            "fr": "crp-what-it-means",
            "it": "crp-what-it-means",
            "he": "crp-what-it-means",
            "hi": "crp-high-kya-matlab",
            "ar": "crp-what-it-means",
        },
        titles={
            "tr": "CRP Yüksek Ne Anlama Gelir: Yüksek CRP Ne Gösterebilir",
            "en": "CRP High Meaning: What Elevated CRP Levels Can Mean",
            "es": "PCR alta: qué pueden significar los niveles elevados",
            "de": "CRP erhöht: Was erhöhte CRP-Werte bedeuten können",
            "fr": "CRP élevé : ce qu'un taux élevé peut signifier",
            "it": "PCR alta: cosa possono significare valori elevati",
            "he": "CRP גבוה: מה ערכים גבוהים יכולים להצביע",
            "hi": "CRP बढ़ा हुआ: ऊंचे स्तर क्या मतलब रख सकते हैं",
            "ar": "CRP مرتفع: ماذا قد تعني المستويات المرتفعة",
        },
        subtitles={
            "en": "A clear guide to C-reactive protein, hs-CRP, infection vs inflammation, reference ranges, and when to see a doctor.",
            "de": "Überblick über C-reaktives Protein, hs-CRP, Infektion vs. Entzündung, Referenzbereiche und wann Sie zum Arzt sollten.",
            "it": "Guida chiara su proteina C-reattiva, hs-CRP, infezione vs infiammazione, intervalli di riferimento e quando rivolgersi al medico.",
            "fr": "Guide clair sur la CRP, hs-CRP, infection vs inflammation, fourchettes de référence et quand consulter.",
            "ar": "دليل واضح عن بروتين C التفاعلي وhs-CRP ونطاقات المرجع ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "CRP is a marker of inflammation produced by the liver. High levels can point to infection or chronic inflammation; interpretation should be done with a clinician.",
            "de": "CRP ist ein Entzündungsmarker, der in der Leber gebildet wird. Erhöhte Werte können auf Infektion oder chronische Entzündung hindeuten.",
            "it": "La CRP è un marcatore dell’infiammazione prodotto dal fegato. Valori alti possono indicare infezione o infiammazione cronica.",
            "fr": "La CRP est un marqueur d’inflammation produit par le foie. Un taux élevé peut indiquer une infection ou une inflammation chronique.",
        },
        seo_titles={
            "en": "CRP Explained: What Elevated Levels Can Mean (and When to Follow Up)",
            "de": "CRP verstehen: Was erhöhte Werte bedeuten",
            "it": "CRP: cosa significa se è alto",
            "fr": "CRP : que signifie un taux élevé",
            "ar": "CRP: ماذا تعني المستويات المرتفعة ومتى المتابعة",
            "tr": "CRP Yüksek Ne Anlama Gelir: Ne Zaman Doktora Gidilmeli",
            "es": "CRP: qué significan los niveles elevados",
            "he": "CRP: מה משמעות ערכים גבוהים",
            "hi": "CRP: ऊंचे स्तर क्या मतलब रखते हैं",
        },
        seo_descriptions={
            "en": "Understand CRP and hs-CRP: what they measure, why levels rise, when values are high, and when to see a doctor. Informational guide only.",
            "de": "CRP und hs-CRP verstehen: Bedeutung, Ursachen erhöhter Werte, Referenzbereiche und wann Sie zum Arzt sollten.",
            "it": "Capire CRP e hs-CRP: cosa misurano, perché aumentano, quando i valori sono alti e quando rivolgersi al medico.",
            "fr": "Comprendre la CRP et la hs-CRP : ce qu’elles mesurent, pourquoi le taux monte, quand consulter. Guide informatif uniquement.",
            "ar": "افهم CRP وhs-CRP: ماذا يقيسان ولماذا ترتفع القيم ومتى ترى الطبيب. للمعلومات فقط.",
            "tr": "CRP ve hs-CRP: ne anlama gelir, ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "Entiende CRP y hs-CRP: qué miden, cuándo suben y cuándo consultar. Solo informativo.",
            "he": "הבן CRP ו-hs-CRP: מתי הערכים עולים ומתי לרופא. למידע בלבד.",
            "hi": "CRP और hs-CRP समझें: कब स्तर ऊंचे होते हैं और डॉक्टर से कब मिलें। सूचनात्मक।",
        },
        sections_by_lang={
            "en": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="What is CRP?",
                    body_html="""
<p>C-reactive protein (CRP) is a protein produced by the liver in response to inflammation anywhere in the body. It is one of the best-known <strong>acute-phase reactants</strong>: its level in the blood rises when tissue is damaged or when the immune system is activated by infection, injury, or chronic inflammatory conditions. CRP does not tell you <em>where</em> the inflammation is or <em>what</em> caused it; it only indicates that some inflammatory process is active. For that reason, it is always interpreted together with your symptoms, other tests, and a doctor’s assessment.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs hs-CRP",
                    body_html="""
<p><strong>Standard CRP</strong> is typically used to monitor infection or acute inflammation (e.g. after surgery, in sepsis, or in autoimmune flares). It is reported in mg/L and can rise into the tens or hundreds in serious infection.</p>
<p><strong>High-sensitivity CRP (hs-CRP)</strong> uses a more sensitive assay and is mainly used to assess <strong>cardiovascular risk</strong> in otherwise stable adults. It measures the same protein but at lower levels (often under 10 mg/L). Guidelines use hs-CRP ranges such as &lt;1 mg/L (low risk), 1–3 mg/L (moderate risk), and &gt;3 mg/L (higher risk) when evaluating heart disease risk—always in combination with other factors and under a doctor’s guidance.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Why does CRP rise?",
                    body_html="""
<p>Common causes of elevated CRP include:</p>
<ul>
  <li><strong>Infections</strong> (bacterial or viral): colds, flu, urinary tract infections, pneumonia, and more serious infections can raise CRP, often sharply in bacterial cases.</li>
  <li><strong>Chronic inflammation</strong>: conditions such as rheumatoid arthritis, inflammatory bowel disease, or chronic kidney disease.</li>
  <li><strong>Autoimmune disease</strong>: flares in lupus, vasculitis, or other autoimmune disorders.</li>
  <li><strong>Injury, surgery, or trauma</strong>: tissue damage triggers an acute-phase response.</li>
  <li><strong>Lifestyle factors</strong>: smoking, obesity, and a sedentary lifestyle can keep CRP mildly elevated over time.</li>
</ul>
<p>CRP is non-specific: a high value does not diagnose a condition. Your doctor will use it together with your history, examination, and other tests to narrow down the cause.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="What counts as “high”?",
                    body_html="""
<p>Reference ranges <strong>vary by laboratory</strong> and by assay. Always use the range printed on your own report. The following are rough, illustrative ranges in mg/L (not a substitute for your lab’s reference):</p>
<ul>
  <li><strong>Standard CRP</strong>: &lt;5 often considered normal; 5–10 mild elevation; 10–40 moderate; &gt;40 marked elevation; &gt;100 often seen in serious bacterial infection. These figures are approximate and method-dependent.</li>
  <li><strong>hs-CRP</strong> (for cardiovascular risk context): &lt;1 mg/L low risk; 1–3 mg/L moderate risk; &gt;3 mg/L higher risk. Again, this is used together with other risk factors and only under clinical guidance.</li>
</ul>
<p>Do not self-diagnose from these numbers. Interpretation must be done by a doctor who can consider your full picture.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="What can you do to lower CRP?",
                    body_html="""
<p>There is no single “treatment for high CRP”—the goal is to address the underlying cause. In general, healthy lifestyle measures can support lower background inflammation:</p>
<ul>
  <li>Quality sleep, weight management if needed, avoiding smoking, a balanced anti-inflammatory-style diet (e.g. Mediterranean), and regular moderate exercise.</li>
</ul>
<p>If your CRP is elevated because of an infection, autoimmune condition, or other illness, your doctor will recommend specific treatments or referrals. Do not start or change supplements or medication based on CRP alone; always follow your doctor’s evaluation and advice.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="When should you see a doctor?",
                    body_html="""
<p>See a doctor if you have:</p>
<ul>
  <li>High CRP together with <strong>fever</strong>, severe pain, shortness of breath, or feeling very unwell.</li>
  <li>Unexplained <strong>weight loss</strong> or fatigue with elevated CRP.</li>
  <li>CRP that stays <strong>elevated for a long time</strong> without a clear explanation.</li>
  <li>Other blood tests or symptoms that suggest infection, inflammation, or an autoimmune condition.</li>
</ul>
<p>Seek urgent care for severe symptoms (e.g. difficulty breathing, chest pain, confusion, or if your lab or doctor has advised immediate follow-up).</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="What tests might come next?",
                    body_html="""
<p>Depending on your result and history, your doctor may order further tests to find the cause of inflammation or to assess risk. These can include:</p>
<ul>
  <li><strong>Full blood count (CBC)</strong>, <strong>ESR</strong> (erythrocyte sedimentation rate), <strong>ferritin</strong>.</li>
  <li><strong>Procalcitonin</strong> (often used to help distinguish bacterial infection from other causes).</li>
  <li><strong>Liver function tests (LFT)</strong>, <strong>urinalysis</strong>, or imaging (e.g. X-ray, ultrasound) when appropriate.</li>
</ul>
<p>Which tests are needed is a clinical decision made by your doctor; this list is for information only.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Frequently asked questions",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">If CRP is high, do I need antibiotics?</h3>
<p>Not necessarily. CRP can rise with viral infections (e.g. colds, flu), where antibiotics are not indicated. Only your doctor can decide whether an infection is bacterial and whether antibiotics are appropriate.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Does a cold raise CRP?</h3>
<p>Yes. Viral upper respiratory infections, including the common cold, can cause a mild to moderate rise in CRP. This does not mean you have a bacterial infection.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can exercise raise CRP?</h3>
<p>Intense or unaccustomed exercise can cause a temporary, small rise in CRP due to muscle micro-injury. Regular moderate exercise is generally associated with lower background inflammation over time.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is CRP tested fasting?</h3>
<p>CRP is usually not strongly affected by a recent meal. Your lab may still ask for fasting if the sample is used for a panel that includes glucose or lipids; follow the instructions you are given.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What is the difference between CRP and ESR?</h3>
<p>Both are markers of inflammation. CRP often rises and falls more quickly; ESR can stay elevated longer. Doctors sometimes use them together to get a fuller picture.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can stress raise CRP?</h3>
<p>Chronic stress may be associated with slightly higher CRP in some people. Stress alone does not explain very high CRP; other causes (infection, inflammation) are usually considered first.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Disclaimer",
                    body_html="""
<p><strong>This content is for information only and does not constitute medical advice or diagnosis.</strong> Always discuss your results and symptoms with a doctor. Do not start or change treatment or supplements based solely on this article. If you have concerns about your health, seek professional medical care.</p>
""",
                ),
            ],
            "de": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="Was ist CRP?",
                    body_html="""
<p>C-reaktives Protein (CRP) wird in der Leber als Reaktion auf Entzündungen im Körper gebildet. Es zählt zu den bekanntesten <strong>Akute-Phase-Proteinen</strong>: Der Spiegel im Blut steigt bei Gewebeschäden oder bei Aktivierung des Immunsystems durch Infektion, Verletzung oder chronische Entzündung. CRP sagt nicht, <em>wo</em> die Entzündung sitzt oder <em>was</em> sie verursacht hat; es zeigt nur an, dass ein entzündlicher Prozess aktiv ist. Die Einordnung erfolgt daher immer gemeinsam mit Beschwerden, weiteren Befunden und der ärztlichen Beurteilung.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs. hs-CRP",
                    body_html="""
<p><strong>Standard-CRP</strong> dient typischerweise der Verlaufskontrolle bei Infektion oder akuter Entzündung (z. B. nach OP, bei Sepsis oder Schüben autoimmuner Erkrankungen). Es wird in mg/L angegeben und kann bei schweren Infektionen stark ansteigen.</p>
<p><strong>High-sensitivity CRP (hs-CRP)</strong> wird mit einer empfindlicheren Methode gemessen und vor allem zur Einschätzung des <strong>kardiovaskulären Risikos</strong> bei stabilen Erwachsenen genutzt. Es misst dasselbe Protein in niedrigeren Bereichen (oft unter 10 mg/L). In Leitlinien werden z. B. &lt;1 mg/L (niedriges Risiko), 1–3 mg/L (mittleres Risiko) und &gt;3 mg/L (höheres Risiko) verwendet – stets zusammen mit anderen Faktoren und in ärztlicher Absprache.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Warum steigt CRP?",
                    body_html="""
<p>Häufige Ursachen erhöhten CRP sind:</p>
<ul>
  <li><strong>Infektionen</strong> (bakteriell oder viral): Erkältung, Grippe, Harnwegsinfekte, Lungenentzündung oder schwerere Infektionen können CRP anheben, bei bakteriellen oft stark.</li>
  <li><strong>Chronische Entzündung</strong>: z. B. rheumatoide Arthritis, chronisch-entzündliche Darmerkrankungen, Nierenerkrankung.</li>
  <li><strong>Autoimmunerkrankungen</strong>: Schübe bei Lupus, Vaskulitis oder anderen Erkrankungen.</li>
  <li><strong>Verletzung, Operation, Trauma</strong>: Gewebeschaden löst eine Akute-Phase-Reaktion aus.</li>
  <li><strong>Lebensstil</strong>: Rauchen, Übergewicht, Bewegungsmangel können CRP leicht erhöht halten.</li>
</ul>
<p>CRP ist unspezifisch: Ein hoher Wert stellt keine Diagnose. Der Arzt ordnet ihn gemeinsam mit Anamnese, Untersuchung und weiteren Tests ein.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="Wann gilt CRP als „erhöht“?",
                    body_html="""
<p>Referenzbereiche <strong>unterscheiden sich je nach Labor und Methode</strong>. Orientieren Sie sich am Bereich auf Ihrem Befund. Zur groben Einordnung (in mg/L, nur Richtwerte):</p>
<ul>
  <li><strong>Standard-CRP</strong>: &lt;5 oft als normal; 5–10 leicht erhöht; 10–40 mäßig; &gt;40 deutlich erhöht; &gt;100 oft bei schwerer bakterieller Infektion. Die Werte sind methodenabhängig.</li>
  <li><strong>hs-CRP</strong> (im kardiovaskulären Kontext): &lt;1 mg/L niedriges Risiko; 1–3 mg/L mittleres; &gt;3 mg/L höheres Risiko. Auch hier nur in Verbindung mit anderen Faktoren und nach ärztlicher Bewertung.</li>
</ul>
<p>Bitte keine Selbstdiagnose. Die Einordnung muss durch einen Arzt erfolgen.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="Was kann man tun, um CRP zu senken?",
                    body_html="""
<p>Es gibt keine einzelne „Therapie gegen hohes CRP“ – Ziel ist die Behandlung der Ursache. Allgemein können gesunder Schlaf, Gewichtsnormalisierung, Nichtrauchen, ausgewogene Ernährung (z. B. mediterran) und regelmäßige moderate Bewegung die Entzündungsaktivität günstig beeinflussen.</p>
<p>Bei Infektion, Autoimmunerkrankung oder anderer Ursache wird der Arzt gezielte Maßnahmen oder Überweisungen empfehlen. Setzen Sie keine Präparate oder Medikamente allein wegen CRP ein; folgen Sie der ärztlichen Einschätzung.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Wann zum Arzt?",
                    body_html="""
<p>Gehen Sie zum Arzt, wenn Sie hohes CRP haben und z. B. Fieber, starke Schmerzen, Atemnot oder starkes Unwohlsein; ungewollten Gewichtsverlust oder anhaltende Müdigkeit; oder wenn CRP über längere Zeit ohne klare Erklärung erhöht bleibt. Auch bei anderen auffälligen Werten oder Symptomen, die auf Infektion oder Entzündung hindeuten, ist eine Abklärung nötig. Bei schweren Symptomen (z. B. Atemnot, Brustschmerz, Verwirrtheit) oder wenn Labor/Arzt sofortige Kontrolle angeraten haben, suchen Sie zeitnah ärztliche Hilfe.</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="Welche Tests können folgen?",
                    body_html="""
<p>Je nach Befund und Vorgeschichte kann der Arzt weitere Tests veranlassen: z. B. großes Blutbild (CBC), Blutkörperchensenkung (ESR), Ferritin, Procalcitonin (zur Abgrenzung bakterieller Infektion), Leberwerte, Urinuntersuchung oder Bildgebung. Welche Tests nötig sind, entscheidet der Arzt; diese Auflistung dient nur der Information.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Häufige Fragen",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Brauche ich bei hohem CRP Antibiotika?</h3>
<p>Nicht zwingend. CRP kann auch bei viralen Infekten (z. B. Erkältung, Grippe) ansteigen, bei denen keine Antibiotika angezeigt sind. Ob eine bakterielle Infektion vorliegt und ob Antibiotika sinnvoll sind, entscheidet der Arzt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Erhöht eine Erkältung das CRP?</h3>
<p>Ja. Virusbedingte Atemwegsinfekte können CRP leicht bis mäßig anheben. Das bedeutet nicht, dass eine bakterielle Infektion vorliegt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann Sport CRP erhöhen?</h3>
<p>Intensive oder ungewohnte Belastung kann durch Mikroverletzungen der Muskulatur kurzfristig leicht CRP anheben. Regelmäßige moderate Bewegung geht langfristig oft mit niedrigerer Entzündungsaktivität einher.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wird CRP nüchtern gemessen?</h3>
<p>CRP wird durch eine Mahlzeit meist wenig beeinflusst. Das Labor kann trotzdem Nüchternheit verlangen, wenn das Blut für ein Profil mit Glukose/Lipiden verwendet wird; bitte die Anweisungen beachten.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Was ist der Unterschied zwischen CRP und BKS (ESR)?</h3>
<p>Beide sind Entzündungsmarker. CRP steigt und fällt oft rascher; die BKS kann länger erhöht bleiben. Sie werden teils gemeinsam beurteilt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann Stress CRP erhöhen?</h3>
<p>Dauerhafter Stress kann bei manchen Menschen mit leicht erhöhtem CRP einhergehen. Sehr hohes CRP erklärt sich dadurch nicht; andere Ursachen (Infektion, Entzündung) werden zuerst geprüft.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Hinweis",
                    body_html="""
<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse und Beschwerden immer mit einem Arzt. Setzen Sie keine Behandlung oder Präparate nur aufgrund dieses Artikels ein. Bei gesundheitlichen Sorgen wenden Sie sich an Fachpersonal.</p>
""",
                ),
            ],
            "it": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="Cos’è la CRP?",
                    body_html="""
<p>La proteina C-reattiva (CRP) è prodotta dal fegato in risposta a un’infiammazione in qualsiasi parte del corpo. È uno dei più noti <strong>reattanti di fase acuta</strong>: il suo livello nel sangue aumenta quando i tessuti sono danneggiati o quando il sistema immunitario è attivato da infezione, trauma o condizioni infiammatorie croniche. La CRP non indica <em>dove</em> sia l’infiammazione né <em>cosa</em> l’abbia causata; indica solo che è in corso un processo infiammatorio. Va quindi sempre interpretata insieme a sintomi, altri esami e al giudizio del medico.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs hs-CRP",
                    body_html="""
<p>La <strong>CRP standard</strong> si usa tipicamente per monitorare infezioni o infiammazione acuta (es. dopo intervento, sepsi, riacutizzazioni autoimmuni). Si esprime in mg/L e può salire molto in caso di infezione grave.</p>
<p>La <strong>CRP ad alta sensibilità (hs-CRP)</strong> usa un test più sensibile ed è usata soprattutto per valutare il <strong>rischio cardiovascolare</strong> in adulti stabili. Misura la stessa proteina a livelli più bassi (spesso sotto 10 mg/L). Nelle linee guida si usano intervalli come &lt;1 mg/L (rischio basso), 1–3 mg/L (moderato), &gt;3 mg/L (più alto), sempre insieme ad altri fattori e sotto guida medica.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Perché la CRP aumenta?",
                    body_html="""
<p>Cause comuni di CRP elevata: <strong>infezioni</strong> (batteriche o virali), <strong>infiammazione cronica</strong> (es. artrite reumatoide, malattie intestinali croniche), <strong>malattie autoimmuni</strong>, <strong>trauma, intervento chirurgico</strong>, <strong>fumo, obesità, sedentarietà</strong>. La CRP è aspecifica: un valore alto non fa diagnosi; il medico la valuta con anamnesi, visita e altri esami.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="Quando si considera “alta”?",
                    body_html="""
<p>I range di riferimento <strong>variano da laboratorio a laboratorio</strong>. Usate sempre quello sul vostro referto. Solo a titolo orientativo (mg/L): CRP standard: &lt;5 spesso normale; 5–10 lieve; 10–40 moderata; &gt;40 marcata; &gt;100 spesso in infezione batterica seria. hs-CRP (contesto cardiovascolare): &lt;1 rischio basso; 1–3 moderato; &gt;3 più alto. L’interpretazione spetta al medico.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="Cosa si può fare per abbassarla?",
                    body_html="""
<p>Non esiste un unico “trattamento per la CRP alta”; l’obiettivo è agire sulla causa. In generale, sonno adeguato, peso nella norma, niente fumo, dieta equilibrata (es. mediterranea) e attività fisica moderata regolare possono aiutare a ridurre l’infiammazione di base. Per infezione o altra causa il medico indicherà cure o invii. Non iniziare o modificare integratori/terapie solo in base alla CRP; seguire sempre il medico.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quando rivolgersi al medico?",
                    body_html="""
<p>Consultate il medico se avete CRP alta con febbre, dolore forte, mancanza di respiro o malessere intenso; perdita di peso inspiegabile o stanchezza con CRP elevata; CRP che resta alta a lungo senza spiegazione; altri esami o sintomi che suggeriscono infezione o infiammazione. In caso di sintomi gravi (difficoltà respiratoria, dolore al petto, confusione) o se il laboratorio/medico consigliano controllo urgente, recatevi subito a un medico.</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="Quali esami possono seguire?",
                    body_html="""
<p>In base al risultato e alla storia, il medico può prescrivere altri esami: emocromo, VES, ferritina, procalcitonina, esami epatici, urinocoltura o imaging. La scelta spetta al medico; questo elenco è solo informativo.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Domande frequenti",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Con CRP alta servono antibiotici?</h3>
<p>Non necessariamente. La CRP può salire anche con infezioni virali (raffreddore, influenza), per cui gli antibiotici non sono indicati. Solo il medico può stabilire se c’è un’infezione batterica e se servono antibiotici.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Il raffreddore fa salire la CRP?</h3>
<p>Sì. Le infezioni virali delle vie respiratorie possono far aumentare lievemente o moderatamente la CRP. Non significa che ci sia un’infezione batterica.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Lo sport può alzare la CRP?</h3>
<p>L’esercizio intenso o non abituale può causare un piccolo aumento temporaneo per microlesioni muscolari. L’attività moderata regolare è in genere associata a minore infiammazione di base.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La CRP si misura a digiuno?</h3>
<p>La CRP di solito non è influenzata dal pasto. Il laboratorio può comunque richiedere il digiuno se il prelievo è per un pannello con glucosio o lipidi; seguite le istruzioni.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Qual è la differenza tra CRP e VES?</h3>
<p>Entrambi sono marker di infiammazione. La CRP spesso sale e scende più rapidamente; la VES può restare elevata più a lungo. A volte si usano insieme.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Lo stress può alzare la CRP?</h3>
<p>Lo stress cronico può essere associato a CRP leggermente più alta in alcune persone. Lo stress da solo non spiega valori molto alti; si considerano prima altre cause (infezione, infiammazione).</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Nota",
                    body_html="""
<p><strong>Questo contenuto è solo informativo e non costituisce consulenza o diagnosi medica.</strong> Discutete sempre risultati e sintomi con un medico. Non iniziare o modificare cure o integratori solo in base a questo articolo. In caso di dubbi sulla salute, rivolgetevi a un professionista.</p>
""",
                ),
            ],
            "fr": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="Qu’est-ce que la CRP ?",
                    body_html="""
<p>La protéine C-réactive (CRP) est produite par le foie en réponse à une inflammation n’importe où dans l’organisme. C’est l’un des <strong>réactants de phase aiguë</strong> les plus connus : son taux sanguin augmente en cas de lésion tissulaire ou d’activation du système immunitaire (infection, traumatisme, maladie inflammatoire chronique). La CRP ne indique pas <em>où</em> est l’inflammation ni <em>quelle</em> en est la cause ; elle signale seulement qu’un processus inflammatoire est actif. Elle est donc toujours interprétée avec les symptômes, les autres examens et l’avis du médecin.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs hs-CRP",
                    body_html="""
<p>La <strong>CRP standard</strong> sert typiquement à surveiller une infection ou une inflammation aiguë (après chirurgie, sepsis, poussée autoimmune). Elle est exprimée en mg/L et peut monter beaucoup en cas d’infection grave.</p>
<p>La <strong>CRP ultra-sensible (hs-CRP)</strong> utilise une technique plus sensible et sert surtout à évaluer le <strong>risque cardiovasculaire</strong> chez l’adulte stable. Elle mesure la même protéine à des niveaux plus bas (souvent &lt;10 mg/L). Les recommandations utilisent des fourchettes comme &lt;1 mg/L (risque faible), 1–3 mg/L (modéré), &gt;3 mg/L (plus élevé), toujours avec d’autres facteurs et sous suivi médical.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Pourquoi la CRP monte-t-elle ?",
                    body_html="""
<p>Causes fréquentes d’élévation : <strong>infections</strong> (bactériennes ou virales), <strong>inflammation chronique</strong> (polyarthrite, maladie inflammatoire intestinale, etc.), <strong>maladies auto-immunes</strong>, <strong>traumatisme ou chirurgie</strong>, <strong>tabac, obésité, sédentarité</strong>. La CRP est non spécifique : un taux élevé ne fait pas à lui seul un diagnostic ; le médecin l’interprète avec l’histoire, l’examen et d’autres examens.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="À partir de quand c’est « élevé » ?",
                    body_html="""
<p>Les fourchettes de référence <strong>varient selon le laboratoire</strong>. Utilisez toujours celle indiquée sur votre résultat. À titre indicatif (mg/L) : CRP standard : &lt;5 souvent normal ; 5–10 légère ; 10–40 modérée ; &gt;40 marquée ; &gt;100 souvent en cas d’infection bactérienne sévère. hs-CRP (contexte cardiovasculaire) : &lt;1 risque faible ; 1–3 modéré ; &gt;3 plus élevé. L’interprétation relève du médecin.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="Que faire pour faire baisser la CRP ?",
                    body_html="""
<p>Il n’y a pas de « traitement du taux de CRP » unique ; l’objectif est de traiter la cause. En général, un bon sommeil, un poids correct, l’arrêt du tabac, une alimentation équilibrée (type méditerranéen) et une activité physique modérée régulière peuvent aider à limiter l’inflammation de fond. En cas d’infection ou d’autre cause, le médecin proposera un traitement ou une orientation. Ne pas modifier seul son traitement ou ses compléments à cause de la CRP ; suivre l’avis du médecin.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quand consulter un médecin ?",
                    body_html="""
<p>Consultez si vous avez un taux de CRP élevé avec fièvre, douleur intense, essoufflement ou malaise important ; perte de poids inexpliquée ou fatigue avec CRP élevée ; CRP qui reste élevée longtemps sans explication ; ou d’autres examens/symptômes évocateurs d’infection ou d’inflammation. En cas de symptômes graves (difficulté à respirer, douleur thoracique, confusion) ou si le laboratoire ou le médecin a conseillé un suivi urgent, consultez sans tarder.</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="Quels examens peuvent suivre ?",
                    body_html="""
<p>Selon le résultat et l’histoire, le médecin peut prescrire d’autres examens : NFS, VS, ferritine, procalcitonine, bilan hépatique, examen urinaire ou imagerie. Le choix des examens est médical ; cette liste est informative.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Questions fréquentes",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">En cas de CRP élevée, faut-il des antibiotiques ?</h3>
<p>Pas forcément. La CRP peut monter lors d’infections virales (rhume, grippe), pour lesquelles les antibiotiques ne sont pas indiqués. Seul le médecin peut juger si une infection bactérienne est présente et si des antibiotiques sont nécessaires.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Un rhume fait-il monter la CRP ?</h3>
<p>Oui. Les infections virales des voies respiratoires peuvent faire monter un peu la CRP. Cela ne signifie pas une infection bactérienne.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Le sport peut-il faire monter la CRP ?</h3>
<p>Un effort intense ou inhabituel peut entraîner une légère hausse temporaire (micro-lésions musculaires). Une activité modérée régulière est en général associée à une inflammation de fond plus basse.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La CRP se dose-t-elle à jeun ?</h3>
<p>La CRP est en général peu influencée par le repas. Le laboratoire peut quand même demander le jeûne pour un bilan incluant glucose ou lipides ; suivez les consignes.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Quelle est la différence entre CRP et VS ?</h3>
<p>Les deux sont des marqueurs d’inflammation. La CRP monte et descend souvent plus vite ; la VS peut rester élevée plus longtemps. Ils sont parfois utilisés ensemble.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Le stress peut-il faire monter la CRP ?</h3>
<p>Le stress chronique peut être associé à une CRP un peu plus élevée chez certaines personnes. Le stress seul n’explique pas une CRP très élevée ; d’autres causes (infection, inflammation) sont d’abord envisagées.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Avertissement",
                    body_html="""
<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis médical ni un diagnostic.</strong> Discutez toujours de vos résultats et symptômes avec un médecin. Ne commencez ni ne modifiez un traitement ou des compléments sur la seule base de cet article. En cas de doute sur votre santé, consultez un professionnel.</p>
""",
                ),
            ],
        },
    )


_CRP_ARTICLE = _article_crp()


def _article_vitamin_d() -> Article:
    """Vitamin D (25(OH)D): low/high meaning, ranges, causes, when to see a doctor, safe supplementation. en, de, it, fr."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/vitamin-d-hero.png"
    cover_alt_text = {
        "en": "Vitamin D blood test and status dashboard — NoryaAI",
        "de": "Vitamin-D-Bluttest und Status-Dashboard — NoryaAI",
        "it": "Esame vitamina D e dashboard stato — NoryaAI",
        "fr": "Dosage vitamine D et tableau de bord statut — NoryaAI",
    }
    return Article(
        id="vitamin-d-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=12,
        cover_image=cover,
        cover_alt=cover_alt_text,
        category={
            "en": "Vitamins & Minerals",
            "de": "Vitamine & Mineralstoffe",
            "it": "Vitamine e minerali",
            "fr": "Vitamines et minéraux",
            "tr": "Vitaminlar ve Mineraller",
            "es": "Vitaminas y minerales",
            "he": "ויטמינים ומינרלים",
            "hi": "विटामिन और मिनरल",
            "ar": "الفيتامينات والمعادن",
        },
        slugs={
            "en": "vitamin-d-what-it-means",
            "de": "vitamin-d-what-it-means",
            "it": "vitamin-d-what-it-means",
            "fr": "vitamin-d-what-it-means",
            "tr": "vitamin-d-what-it-means",
            "es": "vitamina-d-what-it-means",
            "he": "vitamin-d-what-it-means",
            "hi": "vitamin-d-what-it-means",
            "ar": "vitamin-d-what-it-means",
        },
        titles={
            "en": "Vitamin D Explained: Interpreting Low and High 25(OH)D Results",
            "de": "Vitamin D verstehen: Niedrige und hohe 25(OH)D-Werte",
            "it": "Vitamina D: come interpretare valori bassi o alti di 25(OH)D",
            "fr": "Vitamine D : interpréter un taux bas ou élevé de 25(OH)D",
            "tr": "D Vitamini: Düşük ve Yüksek 25(OH)D Sonuçları Nasıl Yorumlanır",
            "es": "Vitamina D: cómo interpretar niveles bajos o altos de 25(OH)D",
            "he": "ויטמין D: איך לפרש ערכים נמוכים או גבוהים של 25(OH)D",
            "hi": "विटामिन D: कम या ज़्यादा 25(OH)D रिज़ल्ट कैसे समझें",
            "ar": "فيتامين D: كيف تُفسَّر المستويات المنخفضة أو المرتفعة لـ 25(OH)D",
        },
        subtitles={
            "en": "A clear guide to vitamin D, 25(OH)D ranges, causes of low or high levels, when to see a doctor, and safe supplementation principles.",
            "de": "Überblick über Vitamin D, 25(OH)D-Referenzbereiche, Ursachen für niedrige oder hohe Werte und wann Sie zum Arzt sollten.",
            "it": "Guida chiara su vitamina D, intervalli 25(OH)D, cause di valori bassi o alti e quando rivolgersi al medico.",
            "fr": "Guide clair sur la vitamine D, fourchettes 25(OH)D, causes de taux bas ou élevés et quand consulter.",
            "tr": "D vitamini, 25(OH)D aralıkları, düşük/yüksek nedenleri ve ne zaman doktora gidilmeli rehberi.",
            "es": "Guía sobre vitamina D, rangos 25(OH)D, causas de niveles bajos o altos y cuándo consultar.",
            "he": "מדריך על ויטמין D, טווחי 25(OH)D ומתי לפנות לרופא.",
            "hi": "विटामिन D, 25(OH)D रेंज और डॉक्टर से कब मिलें — गाइड।",
            "ar": "دليل واضح عن فيتامين D ونطاقات 25(OH)D ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "Vitamin D status is usually assessed by 25(OH)D. Low or high results have many possible causes; interpretation should be done with a clinician.",
            "de": "Der Vitamin-D-Status wird meist über 25(OH)D beurteilt. Niedrige oder hohe Werte können viele Ursachen haben; die Einordnung erfolgt mit dem Arzt.",
            "it": "Lo stato della vitamina D si valuta con il 25(OH)D. Valori bassi o alti possono avere molte cause; l’interpretazione va fatta con il medico.",
            "fr": "Le statut en vitamine D est évalué par le 25(OH)D. Un taux bas ou élevé peut avoir de nombreuses causes ; l’interprétation se fait avec un médecin.",
            "tr": "D vitamini durumu genelde 25(OH)D ile değerlendirilir. Düşük veya yüksek sonuçların birçok nedeni olabilir; yorum hekimle yapılmalıdır.",
            "es": "El estado de vitamina D se valora con 25(OH)D. Niveles bajos o altos pueden deberse a muchas causas; la interpretación debe hacerla el médico.",
            "he": "מצב ויטמין D נבדק בדרך כלל עם 25(OH)D. ערכים נמוכים או גבוהים יכולים לנבוע מסיבות רבות; יש לפרש עם הרופא.",
            "hi": "विटामिन D स्टेटस आमतौर पर 25(OH)D से आंका जाता है। कम या ज़्यादा रिज़ल्ट के कई कारण हो सकते हैं; व्याख्या डॉक्टर के साथ करें।",
            "ar": "حالة فيتامين D تُقيّم عادة بـ 25(OH)D. المستوى المنخفض أو المرتفع قد يكون لأسباب كثيرة؛ التفسير يكون مع الطبيب.",
        },
        seo_titles={
            "en": "Vitamin D Explained: Interpreting Low and High 25(OH)D Results",
            "de": "Vitamin D verstehen: Niedrige und hohe 25(OH)D-Werte",
            "it": "Vitamina D: come interpretare valori bassi o alti di 25(OH)D",
            "fr": "Vitamine D : interpréter un taux bas ou élevé de 25(OH)D",
            "tr": "D Vitamini: Düşük ve Yüksek 25(OH)D Nasıl Yorumlanır",
            "es": "Vitamina D: niveles bajos y altos de 25(OH)D",
            "he": "ויטמין D: ערכים נמוכים וגבוהים של 25(OH)D",
            "hi": "विटामिन D: कम और ज़्यादा 25(OH)D रिज़ल्ट",
            "ar": "فيتامين D: المستويات المنخفضة والمرتفعة لـ 25(OH)D",
        },
        seo_descriptions={
            "en": "Understand vitamin D and 25(OH)D: typical ranges, causes of low or high levels, when to see a doctor, and safe supplement use. Informational only.",
            "de": "Vitamin D und 25(OH)D verstehen: Referenzbereiche, Ursachen für niedrige/hohe Werte, wann zum Arzt. Nur zur Information.",
            "it": "Capire vitamina D e 25(OH)D: intervalli tipici, cause di valori bassi o alti, quando rivolgersi al medico. Solo informativo.",
            "fr": "Comprendre la vitamine D et le 25(OH)D : fourchettes, causes de taux bas ou élevés, quand consulter. À titre informatif uniquement.",
            "tr": "D vitamini ve 25(OH)D: referans aralıkları, düşük/yüksek nedenleri, ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "Entiende vitamina D y 25(OH)D: rangos, causas de niveles bajos o altos, cuándo consultar. Solo informativo.",
            "he": "הבן ויטמין D ו-25(OH)D: טווחים, מתי לרופא. למידע בלבד.",
            "hi": "विटामिन D और 25(OH)D समझें: रेंज, कब डॉक्टर से मिलें। सूचनात्मक।",
            "ar": "افهم فيتامين D و25(OH)D: النطاقات ومتى ترى الطبيب. للمعلومات فقط.",
        },
        sections_by_lang={
            "en": [
                Section(
                    id="what-is-vitamin-d",
                    level=2,
                    heading="What is vitamin D?",
                    body_html="""
<p>Vitamin D is a fat-soluble vitamin that helps regulate calcium and phosphate and supports bone health, muscle function, and immune modulation. It comes in two main forms: <strong>D2</strong> (ergocalciferol, from plants/fungi) and <strong>D3</strong> (cholecalciferol, from sunlight on skin and from animal sources or supplements). Both can be measured indirectly; the form that best reflects your body’s supply is <strong>25-hydroxyvitamin D, or 25(OH)D</strong>. Laboratories typically report total 25(OH)D (D2 + D3), which is why lab results refer to “25(OH)D” or “vitamin D level”—this is the standard marker used to assess deficiency, sufficiency, or excess.</p>
""",
                ),
                Section(
                    id="typical-ranges",
                    level=2,
                    heading="Typical ranges",
                    body_html="""
<p>Reference ranges <strong>vary by laboratory and method</strong>. Always use the range on your own report. The following are approximate, for context only (in ng/mL; multiply by 2.5 for nmol/L):</p>
<ul>
  <li><strong>Deficiency</strong>: often &lt;20 ng/mL (≈50 nmol/L).</li>
  <li><strong>Insufficiency</strong>: often 20–29 ng/mL.</li>
  <li><strong>Sufficient</strong>: commonly ~30–50 ng/mL for the general population.</li>
  <li><strong>Potentially high</strong>: &gt;50–60 ng/mL depending on context; not always harmful but worth discussing with a doctor.</li>
  <li><strong>Toxicity concern</strong>: often cited above ~100 ng/mL (hypercalcemia risk); assessment and any intervention are for a clinician to decide.</li>
</ul>
<p>Your doctor will interpret your result in light of your age, health conditions, and any supplements or medications.</p>
""",
                ),
                Section(
                    id="causes-low",
                    level=2,
                    heading="Causes of low vitamin D",
                    body_html="""
<p>Common reasons for low 25(OH)D include: <strong>low sun exposure</strong> (latitude, season, clothing, sunscreen, indoor lifestyle); <strong>darker skin pigmentation</strong> (more melanin reduces vitamin D synthesis in skin); <strong>winter months</strong> in higher latitudes; <strong>obesity</strong> (vitamin D can be sequestered in adipose tissue); <strong>malabsorption</strong> (e.g. coeliac disease, Crohn’s, gastric surgery); <strong>liver or kidney disease</strong> (altered metabolism of vitamin D); and <strong>certain medications</strong> that affect absorption or metabolism. More than one factor can apply. A clinician can help identify the most relevant causes for you.</p>
""",
                ),
                Section(
                    id="symptoms-signs",
                    level=2,
                    heading="Symptoms and signs",
                    body_html="""
<p>Signs that are sometimes associated with low vitamin D include fatigue, bone or muscle pain, weakness, frequent infections, and low mood. These are <strong>non-specific</strong>—they can have many other causes. <strong>Symptoms alone do not establish a diagnosis</strong>; they must be interpreted together with blood tests and clinical history by a doctor. Do not self-diagnose deficiency based only on how you feel.</p>
""",
                ),
                Section(
                    id="when-high",
                    level=2,
                    heading="When vitamin D is high",
                    body_html="""
<p>Elevated 25(OH)D is often due to <strong>supplement overuse or dosing errors</strong>. Very high levels increase the risk of <strong>hypercalcemia</strong> (high blood calcium), which can affect the heart, kidneys, and nerves. Red flags that warrant prompt medical attention include: nausea, excessive thirst, frequent urination, confusion, or kidney stones. If your level is high or you take high-dose vitamin D, discuss with a clinician; do not stop or change supplements without medical advice.</p>
""",
                ),
                Section(
                    id="next-labs",
                    level=2,
                    heading="Next labs a clinician may check",
                    body_html="""
<p>Depending on your result and history, your doctor may order additional tests to clarify status or rule out complications. These can include: <strong>calcium</strong> (total and/or ionized), <strong>parathyroid hormone (PTH)</strong>, <strong>phosphate</strong>, <strong>magnesium</strong>, <strong>alkaline phosphatase (ALP)</strong>, and <strong>kidney function</strong> (e.g. creatinine, eGFR). Which tests are needed is a clinical decision made by your doctor.</p>
""",
                ),
                Section(
                    id="practical-guidance",
                    level=2,
                    heading="Practical guidance",
                    body_html="""
<p><strong>Sunlight</strong>: sensible, limited exposure (without burning) can help the body make vitamin D; duration and safety depend on skin type, location, and season—your doctor can advise. <strong>Diet</strong>: fatty fish, fortified dairy or plant milks, egg yolk, and some fortified foods provide vitamin D but often not enough to correct deficiency alone. <strong>Supplements</strong>: if your doctor recommends supplementation, use the dose they suggest. Avoid mega-doses without clinical supervision. Rechecking 25(OH)D after 8–12 weeks is often used to see if the level has improved; your doctor will advise on timing and target. Do not self-prescribe high doses; excess can be harmful.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Frequently asked questions",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">How fast does vitamin D increase?</h3>
<p>With appropriate supplementation or improved sun exposure, 25(OH)D can begin to rise within several weeks; meaningful change often takes 8–12 weeks. Your doctor can suggest when to recheck.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can I take vitamin D3 daily?</h3>
<p>Many people take a daily maintenance dose recommended by their doctor. The right dose depends on your baseline level, diet, sun exposure, and health; do not exceed amounts advised by a clinician.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Does vitamin D help immunity?</h3>
<p>Vitamin D is involved in immune regulation. Adequate levels may support normal immune function, but supplementation is not a substitute for a balanced diet, sleep, or medical care when you are ill. Evidence is nuanced; your doctor can advise for your situation.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What about magnesium or vitamin K2?</h3>
<p>Magnesium is involved in vitamin D metabolism; some people have low magnesium. Vitamin K2 is sometimes discussed in relation to bone and cardiovascular health. Neither is a universal “must take” with vitamin D; balance and individual needs matter. Discuss with your doctor before adding supplements.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is 25(OH)D tested fasting?</h3>
<p>Fasting is usually not required for 25(OH)D alone, but your lab may request it if the sample is used for a panel that includes glucose or lipids. Follow the instructions given for your blood draw.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can I interpret my result myself?</h3>
<p>Your result should be interpreted in context (age, health, medications, diet). Your doctor can say whether your level is appropriate for you and whether you need treatment or further tests.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Disclaimer",
                    body_html="""
<p><strong>This content is for information only and does not constitute medical advice or diagnosis.</strong> Always discuss your results and symptoms with a doctor. Do not start or change supplements or treatment based solely on this article. If you have concerns about your health, seek professional medical care.</p>
""",
                ),
            ],
            "de": [
                Section(
                    id="what-is-vitamin-d",
                    level=2,
                    heading="Was ist Vitamin D?",
                    body_html="""
<p>Vitamin D ist ein fettlösliches Vitamin, das bei der Regulation von Kalzium und Phosphat sowie bei Knochen- und Muskelfunktion und Immunmodulation eine Rolle spielt. Es kommt vor allem als <strong>D2</strong> (Ergocalciferol, pflanzlich) und <strong>D3</strong> (Cholecalciferol, durch Sonne und tierische Quellen/Supplemente) vor. Der beste Indikator für die Versorgung ist <strong>25-Hydroxyvitamin D, 25(OH)D</strong>. Labore messen in der Regel Gesamt-25(OH)D (D2 + D3) – das ist der übliche Marker für Mangel, ausreichende Versorgung oder Überschuss.</p>
""",
                ),
                Section(
                    id="typical-ranges",
                    level=2,
                    heading="Typische Referenzbereiche",
                    body_html="""
<p>Referenzbereiche <strong>unterscheiden sich je nach Labor und Methode</strong>. Orientieren Sie sich am Befund. Zur groben Einordnung (ng/mL; ×2,5 für nmol/L): <strong>Mangel</strong> oft &lt;20; <strong>Insuffizienz</strong> 20–29; <strong>ausreichend</strong> oft ~30–50; <strong>erhöht</strong> &gt;50–60 (kontextabhängig); <strong>Toxizitätsrisiko</strong> oft ab ~100 ng/mL. Die Bewertung übernimmt Ihr Arzt.</p>
""",
                ),
                Section(
                    id="causes-low",
                    level=2,
                    heading="Ursachen für niedriges Vitamin D",
                    body_html="""
<p>Häufige Ursachen: wenig Sonnenexposition, dunklere Hautpigmentierung, Winter in nördlichen Breiten, Adipositas, Malabsorption (z. B. Zöliakie, Morbus Crohn), Leber- oder Nierenerkrankung, bestimmte Medikamente. Mehrere Faktoren können zusammenspielen. Der Arzt hilft bei der Einordnung.</p>
""",
                ),
                Section(
                    id="symptoms-signs",
                    level=2,
                    heading="Symptome und Zeichen",
                    body_html="""
<p>Mögliche Zeichen bei niedrigem Vitamin D: Müdigkeit, Knochen- oder Muskelschmerzen, Infektanfälligkeit, gedrückte Stimmung. Diese sind <strong>unspezifisch</strong> und allein keine Diagnose. Die Bewertung erfolgt durch den Arzt anhand von Labor und Anamnese.</p>
""",
                ),
                Section(
                    id="when-high",
                    level=2,
                    heading="Wenn Vitamin D erhöht ist",
                    body_html="""
<p>Hohe Werte entstehen oft durch <strong>übermäßige oder falsche Supplementation</strong>. Sehr hohe Spiegel erhöhen das Risiko für <strong>Hyperkalzämie</strong>. Warnzeichen: Übelkeit, starker Durst, häufiges Wasserlassen, Verwirrtheit, Nierensteine. Bei hohem Spiegel oder hochdosierter Einnahme den Arzt konsultieren.</p>
""",
                ),
                Section(
                    id="next-labs",
                    level=2,
                    heading="Weitere Laborwerte",
                    body_html="""
<p>Der Arzt kann je nach Befund u. a. Kalzium, Parathormon (PTH), Phosphat, Magnesium, alkalische Phosphatase (AP) und Nierenfunktion veranlassen. Die Auswahl ist eine klinische Entscheidung.</p>
""",
                ),
                Section(
                    id="practical-guidance",
                    level=2,
                    heading="Praktische Hinweise",
                    body_html="""
<p><strong>Sonne</strong>: maßvolle, kurze Exposition (ohne Sonnenbrand) kann die Bildung von Vitamin D fördern. <strong>Ernährung</strong>: fettreicher Fisch, angereicherte Milch, Eigelb. <strong>Supplemente</strong>: nur in der vom Arzt empfohlenen Dosis; keine Mega-Dosen ohne Aufsicht. Kontrolle von 25(OH)D nach 8–12 Wochen ist üblich. Bitte nicht in Eigenregie hochdosieren.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Häufige Fragen",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Wie schnell steigt Vitamin D?</h3>
<p>Bei angepasster Supplementation oder mehr Sonne kann 25(OH)D innerhalb von Wochen ansteigen; oft sind 8–12 Wochen nötig. Der Arzt legt den Kontrollzeitpunkt fest.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann ich D3 täglich einnehmen?</h3>
<p>Viele nehmen eine vom Arzt empfohlene Erhaltungsdosis. Die Dosis hängt von Ausgangswert, Ernährung und Gesundheit ab.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Stärkt Vitamin D die Abwehr?</h3>
<p>Vitamin D ist an der Immunregulation beteiligt. Ausreichende Spiegel können die normale Abwehr unterstützen; Supplemente ersetzen keine ausgewogene Ernährung oder ärztliche Behandlung.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Was ist mit Magnesium oder Vitamin K2?</h3>
<p>Magnesium ist am Vitamin-D-Stoffwechsel beteiligt; K2 wird teils im Zusammenhang mit Knochen/Kreislauf diskutiert. Beides ist nicht pauschal „Pflicht“; Besprechen Sie mit dem Arzt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wird 25(OH)D nüchtern gemessen?</h3>
<p>Für 25(OH)D allein meist nicht nötig; das Labor kann Nüchternheit für ein Gesamtprofil verlangen.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann ich meinen Wert selbst einordnen?</h3>
<p>Die Einordnung erfolgt im Kontext (Alter, Gesundheit, Medikamente). Ihr Arzt kann beurteilen, ob Ihr Wert für Sie passend ist.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Hinweis",
                    body_html="""
<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung oder Diagnose.</strong> Besprechen Sie Ergebnisse und Beschwerden immer mit einem Arzt. Setzen Sie keine Präparate oder Therapie nur aufgrund dieses Artikels ein.</p>
""",
                ),
            ],
            "it": [
                Section(
                    id="what-is-vitamin-d",
                    level=2,
                    heading="Cos’è la vitamina D?",
                    body_html="""
<p>La vitamina D è una vitamina liposolubile che aiuta a regolare calcio e fosfato e sostiene ossa, muscoli e sistema immunitario. Esiste come <strong>D2</strong> (ergocalciferolo, da fonti vegetali) e <strong>D3</strong> (colecalciferolo, da sole e fonti animali/integratori). Il marker che riflette meglio la disponibilità nell’organismo è il <strong>25-idrossivitamina D, 25(OH)D</strong>. I laboratori riportano in genere il 25(OH)D totale (D2 + D3), usato per valutare carenza, sufficienza o eccesso.</p>
""",
                ),
                Section(
                    id="typical-ranges",
                    level=2,
                    heading="Intervalli tipici",
                    body_html="""
<p>Gli intervalli di riferimento <strong>variano da laboratorio a laboratorio</strong>. Usate sempre quello sul referto. In modo orientativo (ng/mL; ×2,5 per nmol/L): <strong>carenza</strong> spesso &lt;20; <strong>insufficienza</strong> 20–29; <strong>sufficiente</strong> ~30–50; <strong>potenzialmente alto</strong> &gt;50–60; <strong>rischio tossicità</strong> spesso sopra ~100 ng/mL. L’interpretazione spetta al medico.</p>
""",
                ),
                Section(
                    id="causes-low",
                    level=2,
                    heading="Cause di vitamina D bassa",
                    body_html="""
<p>Cause comuni: poca esposizione al sole, pelle scura, stagione invernale, obesità, malassorbimento (celiachia, Crohn, chirurgia gastrica), malattie epatiche o renali, alcuni farmaci. Il medico aiuta a individuare le cause rilevanti.</p>
""",
                ),
                Section(
                    id="symptoms-signs",
                    level=2,
                    heading="Sintomi e segni",
                    body_html="""
<p>Sintomi a volte associati a carenza: stanchezza, dolori ossei o muscolari, infezioni frequenti, umore basso. Sono <strong>aspecifici</strong>; da soli non consentono la diagnosi. Vanno interpretati dal medico con gli esami e la storia clinica.</p>
""",
                ),
                Section(
                    id="when-high",
                    level=2,
                    heading="Quando la vitamina D è alta",
                    body_html="""
<p>Valori elevati spesso da <strong>eccesso di integratori o dosaggi errati</strong>. Livelli molto alti aumentano il rischio di <strong>ipercalcemia</strong>. Segnali d’allarme: nausea, sete eccessiva, minzione frequente, confusione, calcoli renali. In caso di valori alti o assunzione di dosi elevate, consultare il medico.</p>
""",
                ),
                Section(
                    id="next-labs",
                    level=2,
                    heading="Altri esami che il medico può richiedere",
                    body_html="""
<p>In base al risultato e alla storia, il medico può prescrivere calcio, PTH, fosfato, magnesio, fosfatasi alcalina, funzionalità renale. La scelta è clinica.</p>
""",
                ),
                Section(
                    id="practical-guidance",
                    level=2,
                    heading="Consigli pratici",
                    body_html="""
<p><strong>Sole</strong>: un’esposizione sensata e limitata (senza scottature) può favorire la produzione di vitamina D. <strong>Dieta</strong>: pesce grasso, latticini fortificati, tuorlo. <strong>Integratori</strong>: solo nella dose consigliata dal medico; evitare megadosi senza supervisione. Il controllo del 25(OH)D dopo 8–12 settimane è comune. Non assumere dosi elevate di iniziativa propria.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Domande frequenti",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Quanto velocemente aumenta la vitamina D?</h3>
<p>Con integrazione adeguata o più sole, il 25(OH)D può iniziare a salire in alcune settimane; spesso servono 8–12 settimane. Il medico indica quando ripetere l’esame.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Posso prendere la D3 ogni giorno?</h3>
<p>Molte persone assumono una dose di mantenimento consigliata dal medico. La dose giusta dipende dal livello basale e dalla salute; non superare le quantità indicate.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La vitamina D aiuta le difese immunitarie?</h3>
<p>La vitamina D è coinvolta nella regolazione immunitaria. Livelli adeguati possono sostenere la funzione immunitaria; gli integratori non sostituiscono dieta equilibrata o cure mediche.</p>
<h3 class="text-base font-semibold mt-4 mb-1">E il magnesio o la vitamina K2?</h3>
<p>Il magnesio partecipa al metabolismo della vitamina D; la K2 è a volte discussa per ossa e salute cardiovascolare. Nessuno è obbligatorio in modo universale; parlatene con il medico.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Il 25(OH)D si misura a digiuno?</h3>
<p>Per il solo 25(OH)D di solito non è necessario; il laboratorio può richiedere il digiuno per un pannello più ampio.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Posso interpretare il risultato da solo?</h3>
<p>Il risultato va interpretato nel contesto (età, salute, farmaci). Il medico può dire se il livello è adeguato per voi.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Nota",
                    body_html="""
<p><strong>Questo contenuto è solo informativo e non costituisce consulenza o diagnosi medica.</strong> Discutete sempre risultati e sintomi con un medico. Non iniziare o modificare integratori o cure solo in base a questo articolo.</p>
""",
                ),
            ],
            "fr": [
                Section(
                    id="what-is-vitamin-d",
                    level=2,
                    heading="Qu’est-ce que la vitamine D ?",
                    body_html="""
<p>La vitamine D est une vitamine liposoluble qui aide à réguler le calcium et le phosphate et soutient les os, les muscles et l’immunité. Elle existe sous forme <strong>D2</strong> (ergocalciférol, végétale) et <strong>D3</strong> (cholécalciférol, soleil et sources animales/compléments). Le meilleur reflet des réserves est le <strong>25-hydroxyvitamine D, 25(OH)D</strong>. Les laboratoires dosent en général le 25(OH)D total (D2 + D3), utilisé pour évaluer carence, suffisance ou excès.</p>
""",
                ),
                Section(
                    id="typical-ranges",
                    level=2,
                    heading="Fourchettes typiques",
                    body_html="""
<p>Les fourchettes de référence <strong>varient selon le laboratoire</strong>. Utilisez toujours celle de votre résultat. À titre indicatif (ng/mL ; ×2,5 pour nmol/L) : <strong>carence</strong> souvent &lt;20 ; <strong>insuffisance</strong> 20–29 ; <strong>suffisant</strong> ~30–50 ; <strong>potentiellement élevé</strong> &gt;50–60 ; <strong>risque de toxicité</strong> souvent au-dessus de ~100 ng/mL. L’interprétation relève du médecin.</p>
""",
                ),
                Section(
                    id="causes-low",
                    level=2,
                    heading="Causes d’un taux bas",
                    body_html="""
<p>Causes fréquentes : peu d’exposition au soleil, peau foncée, hiver sous nos latitudes, obésité, malabsorption (maladie cœliaque, Crohn, chirurgie gastrique), atteinte hépatique ou rénale, certains médicaments. Le médecin aide à identifier les causes pertinentes.</p>
""",
                ),
                Section(
                    id="symptoms-signs",
                    level=2,
                    heading="Symptômes et signes",
                    body_html="""
<p>Signes parfois associés à un taux bas : fatigue, douleurs osseuses ou musculaires, infections fréquentes, moral bas. Ils sont <strong>non spécifiques</strong> ; à eux seuls ils ne permettent pas le diagnostic. Ils doivent être interprétés par un médecin avec les examens et l’histoire clinique.</p>
""",
                ),
                Section(
                    id="when-high",
                    level=2,
                    heading="Quand la vitamine D est élevée",
                    body_html="""
<p>Un taux élevé vient souvent d’un <strong>surdosage ou d’erreurs de prise</strong>. Des niveaux très élevés augmentent le risque d’<strong>hypercalcémie</strong>. Signes d’alerte : nausées, soif excessive, urines fréquentes, confusion, calculs rénaux. En cas de taux élevé ou de prise à forte dose, consulter un médecin.</p>
""",
                ),
                Section(
                    id="next-labs",
                    level=2,
                    heading="Autres examens possibles",
                    body_html="""
<p>Selon le résultat et l’histoire, le médecin peut prescrire calcium, PTH, phosphate, magnésium, phosphatases alcalines, fonction rénale. Le choix est médical.</p>
""",
                ),
                Section(
                    id="practical-guidance",
                    level=2,
                    heading="Conseils pratiques",
                    body_html="""
<p><strong>Soleil</strong> : une exposition raisonnable et limitée (sans coup de soleil) peut aider à fabriquer de la vitamine D. <strong>Alimentation</strong> : poissons gras, laitages enrichis, jaune d’œuf. <strong>Compléments</strong> : uniquement à la dose conseillée par le médecin ; éviter les mégadoses sans suivi. Contrôler le 25(OH)D après 8–12 semaines est courant. Ne pas prendre de fortes doses en automédication.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Questions fréquentes",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">À quelle vitesse la vitamine D augmente-t-elle ?</h3>
<p>Avec une supplémentation adaptée ou plus de soleil, le 25(OH)D peut commencer à monter en quelques semaines ; un changement net prend souvent 8–12 semaines. Le médecin indiquera quand contrôler.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Puis-je prendre de la D3 tous les jours ?</h3>
<p>Beaucoup de personnes prennent une dose d’entretien conseillée par le médecin. La dose dépend du taux de départ et de l’état de santé.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La vitamine D aide-t-elle l’immunité ?</h3>
<p>La vitamine D est impliquée dans la régulation immunitaire. Un taux suffisant peut soutenir la fonction immunitaire ; les compléments ne remplacent pas une alimentation équilibrée ni un avis médical.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Et le magnésium ou la vitamine K2 ?</h3>
<p>Le magnésium intervient dans le métabolisme de la vitamine D ; la K2 est parfois évoquée pour les os et le cœur. Ni l’un ni l’autre n’est systématiquement « obligatoire » ; en parler au médecin.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Le 25(OH)D se dose-t-il à jeun ?</h3>
<p>Pour le 25(OH)D seul, le jeûne n’est en général pas requis ; le laboratoire peut le demander pour un bilan plus large.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Puis-je interpréter mon résultat moi-même ?</h3>
<p>Le résultat doit être interprété dans le contexte (âge, santé, médicaments). Votre médecin peut dire si le taux vous convient.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Avertissement",
                    body_html="""
<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis médical ni un diagnostic.</strong> Discutez toujours de vos résultats et symptômes avec un médecin. Ne commencez ni ne modifiez un complément ou un traitement sur la seule base de cet article.</p>
""",
                ),
            ],
        },
    )


_VITAMIN_D_ARTICLE = _article_vitamin_d()


def _article_vitamin_b12() -> Article:
    """Vitamin B12: low levels, symptoms, causes, next steps. en, de, it, fr. Clinical/corporate tone; no diagnosis; inform + direct to doctor."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/vitamin-b12-hero.png"
    cover_alt_text = {
        "en": "Vitamin B12 blood test and status dashboard — NoryaAI",
        "de": "Vitamin-B12-Bluttest und Status-Dashboard — NoryaAI",
        "it": "Esame vitamina B12 e dashboard stato — NoryaAI",
        "fr": "Dosage vitamine B12 et tableau de bord statut — NoryaAI",
    }
    return Article(
        id="vitamin-b12-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=11,
        cover_image=cover,
        cover_alt=cover_alt_text,
        category={
            "en": "Vitamins & Minerals",
            "de": "Vitamine & Mineralstoffe",
            "it": "Vitamine e minerali",
            "fr": "Vitamines et minéraux",
            "tr": "Vitaminlar ve Mineraller",
            "es": "Vitaminas y minerales",
            "he": "ויטמינים ומינרלים",
            "hi": "विटामिन और मिनरल",
            "ar": "الفيتامينات والمعادن",
        },
        slugs={
            "en": "vitamin-b12-what-it-means",
            "de": "vitamin-b12-what-it-means",
            "it": "vitamin-b12-what-it-means",
            "fr": "vitamin-b12-what-it-means",
            "tr": "vitamin-b12-what-it-means",
            "es": "vitamina-b12-what-it-means",
            "he": "vitamin-b12-what-it-means",
            "hi": "vitamin-b12-what-it-means",
            "ar": "vitamin-b12-what-it-means",
        },
        titles={
            "en": "Vitamin B12 Explained: Low Levels, Symptoms, Causes, and Next Steps",
            "de": "Vitamin B12 verstehen: Niedrige Werte, Symptome und nächste Schritte",
            "it": "Vitamina B12: valori bassi, sintomi, cause e cosa fare",
            "fr": "Vitamine B12 : taux bas, symptômes, causes et étapes suivantes",
            "tr": "B12 Vitamini: Düşük Seviye, Belirtiler, Nedenler ve Sonraki Adımlar",
            "es": "Vitamina B12: niveles bajos, síntomas, causas y qué hacer",
            "he": "ויטמין B12: ערכים נמוכים, תסמינים ושלבים הבאים",
            "hi": "विटामिन B12: कम स्तर, लक्षण, कारण और आगे क्या करें",
            "ar": "فيتامين B12: المستويات المنخفضة، الأعراض والأسباب والخطوات التالية",
        },
        subtitles={
            "en": "A clear guide to vitamin B12: what it does, typical ranges, common causes of low levels, symptoms and when to see a doctor, and how it is managed.",
            "de": "Überblick über Vitamin B12: Funktion, Referenzbereiche, Ursachen für niedrige Werte, Symptome und wann Sie zum Arzt sollten.",
            "it": "Guida chiara sulla vitamina B12: a cosa serve, intervalli tipici, cause di valori bassi, sintomi e quando rivolgersi al medico.",
            "fr": "Guide clair sur la vitamine B12 : rôle, fourchettes typiques, causes de taux bas, symptômes et quand consulter.",
            "tr": "B12 vitamini rehberi: ne işe yarar, referans aralıkları, düşük nedenleri ve ne zaman doktora gidilmeli.",
            "es": "Guía sobre vitamina B12: para qué sirve, rangos típicos, causas de niveles bajos y cuándo consultar.",
            "he": "מדריך על ויטמין B12: תפקיד, טווחים ומתי לרופא.",
            "hi": "विटामिन B12 गाइड: क्या करता है, रेंज और डॉक्टर से कब मिलें।",
            "ar": "دليل واضح عن فيتامين B12: الوظيفة، النطاقات ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "Vitamin B12 supports nerves, red blood cells and DNA. Low levels can have many causes; interpretation and next steps are for a clinician.",
            "de": "Vitamin B12 ist wichtig für Nerven, rote Blutkörperchen und DNA. Niedrige Werte können viele Ursachen haben; die Einordnung übernimmt der Arzt.",
            "it": "La vitamina B12 sostiene nervi, globuli rossi e DNA. Valori bassi possono avere molte cause; l’interpretazione spetta al medico.",
            "fr": "La vitamine B12 soutient les nerfs, les globules rouges et l’ADN. Un taux bas peut avoir plusieurs causes ; l’interprétation relève du médecin.",
        },
        seo_titles={
            "en": "Vitamin B12 Explained: Low Levels, Symptoms, Causes, and Next Steps",
            "de": "Vitamin B12 verstehen: Niedrige Werte, Symptome und nächste Schritte",
            "it": "Vitamina B12: valori bassi, sintomi, cause e cosa fare",
            "fr": "Vitamine B12 : taux bas, symptômes, causes et étapes suivantes",
        },
        seo_descriptions={
            "en": "Understand vitamin B12: what it does, typical ranges, causes of low B12, symptoms and when to see a doctor. Informational only — not medical advice.",
            "de": "Vitamin B12 verstehen: Funktion, Referenzbereiche, Ursachen für niedrige Werte, wann zum Arzt. Nur zur Information.",
            "it": "Capire la vitamina B12: a cosa serve, intervalli tipici, cause di carenza, quando rivolgersi al medico. Solo informativo.",
            "fr": "Comprendre la vitamine B12 : rôle, fourchettes, causes de taux bas, quand consulter. À titre informatif uniquement.",
            "tr": "B12 vitamini: ne işe yarar, referans aralıkları, düşük nedenleri ve ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "Entiende la vitamina B12: función, rangos, causas de niveles bajos y cuándo consultar. Solo informativo.",
            "he": "הבן ויטמין B12: תפקיד, טווחים ומתי לרופא. למידע בלבד.",
            "hi": "विटामिन B12 समझें: कार्य, रेंज और डॉक्टर से कब मिलें। सूचनात्मक।",
            "ar": "افهم فيتامين B12: الوظيفة، النطاقات ومتى ترى الطبيب. للمعلومات فقط.",
        },
        sections_by_lang={
            "en": _b12_sections_en(),
            "de": _b12_sections_de(),
            "it": _b12_sections_it(),
            "fr": _b12_sections_fr(),
        },
    )


def _b12_sections_en() -> List[Section]:
    return [
        Section(
            id="what-b12-does",
            level=2,
            heading="What Vitamin B12 does",
            body_html="""
<p>Vitamin B12 (cobalamin) is essential for <strong>nerve function</strong>, <strong>red blood cell formation</strong>, and <strong>DNA synthesis</strong>. The body cannot make it; it must come from diet or, in some cases, supplements or injections prescribed by a clinician. Low B12 can lead to anaemia and, if prolonged, to neurological symptoms. This article is for information only and does not replace a medical assessment.</p>
""",
        ),
        Section(
            id="typical-ranges",
            level=2,
            heading="Typical ranges and “borderline”",
            body_html="""
<p>Reference ranges <strong>vary by laboratory and method</strong>. Always use the range on your own report. Many labs use approximate ranges in the hundreds of pg/mL (or pmol/L in some countries); values below the lab’s lower limit may be reported as low or deficient, while values just above it are sometimes called “borderline”. There is no single universal cut-off; interpretation depends on your history, other tests, and your doctor’s judgment. Do not self-diagnose based on a number alone.</p>
""",
        ),
        Section(
            id="causes-low",
            level=2,
            heading="Common causes of low B12",
            body_html="""
<p><strong>Diet</strong>: Strict vegan or vegetarian diets without fortified foods or B12 supplements can lead to low intake. <strong>Absorption</strong>: Pernicious anaemia (autoimmune condition affecting intrinsic factor), coeliac disease, Crohn’s disease, or surgery that removes or bypasses part of the stomach or small intestine can reduce absorption. <strong>Medications</strong>: Long-term use of metformin or proton-pump inhibitors (PPIs) may contribute to low B12 in some people. <strong>Age</strong>: Absorption can decrease with age. More than one factor may apply. A clinician can help identify the most relevant causes for you.</p>
""",
        ),
        Section(
            id="symptoms",
            level=2,
            heading="Symptoms and when to see a clinician",
            body_html="""
<p>Signs that are sometimes associated with low B12 include fatigue, weakness, pale skin, and breathlessness. These are <strong>non-specific</strong>—they can have many other causes. <strong>Neurological red flags</strong> that warrant prompt medical attention include: numbness or tingling in hands or feet, balance or walking problems, memory or concentration difficulties, and mood changes. <strong>Symptoms alone do not establish a diagnosis</strong>; they must be interpreted together with blood tests and clinical history by a doctor. If you have such symptoms or a low or borderline B12 result, see a clinician for proper evaluation.</p>
""",
        ),
        Section(
            id="related-tests",
            level=2,
            heading="Related and confirmatory tests",
            body_html="""
<p>Your doctor may order additional tests to clarify B12 status or rule out other causes of symptoms. These can include: <strong>full blood count (CBC)</strong> and <strong>MCV</strong> (mean cell volume—often elevated in B12 deficiency); <strong>folate</strong> (low folate can mimic or coexist with B12 deficiency); <strong>methylmalonic acid (MMA)</strong> and <strong>homocysteine</strong> (often elevated when B12 is functionally low). Which tests are needed is a clinical decision made by your doctor.</p>
""",
        ),
        Section(
            id="treatment-overview",
            level=2,
            heading="Treatment overview",
            body_html="""
<p>Management is determined by your doctor based on cause and severity. <strong>Dietary sources</strong> of B12 include meat, fish, eggs, dairy, and fortified plant-based foods. For deficiency, clinicians often recommend <strong>oral B12 or B12 injections</strong>; the choice and dose depend on absorption, severity, and clinical guidelines. <strong>Recheck timing</strong> is often around 8–12 weeks after starting treatment, but your doctor will advise on the right interval and target for you. Do not self-prescribe high-dose B12 without medical guidance.</p>
""",
        ),
        Section(
            id="practical-tips",
            level=2,
            heading="Practical tips",
            body_html="""
<p>If your doctor recommends more B12 from diet, include reliable sources (animal products or fortified foods) as appropriate for your diet. If supplements or injections are prescribed, take them as directed and attend follow-up tests so your doctor can confirm that levels are improving. Adherence to the agreed plan helps ensure a reliable response.</p>
""",
        ),
        Section(
            id="faq",
            level=2,
            heading="Frequently asked questions",
            body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Can B12 be low with normal haemoglobin?</h3>
<p>Yes. B12 deficiency can develop before anaemia appears. Some people have low or borderline B12 with a normal full blood count; others have anaemia (often with raised MCV). Your doctor will interpret your results in context.</p>
<h3 class="text-base font-semibold mt-4 mb-1">How fast do symptoms improve?</h3>
<p>Improvement depends on cause, severity, and treatment. Some people notice more energy within weeks; neurological symptoms may take longer to improve and in some cases may not fully resolve. Follow your doctor’s plan and report any ongoing symptoms.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is high B12 a problem?</h3>
<p>Very high B12 levels are uncommon from diet alone and can sometimes be linked to certain conditions or supplements. Interpretation of high B12 is for your doctor, who can consider your history and other tests.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Do I need to stop metformin or PPIs?</h3>
<p>Do not stop prescribed medications on your own. If you take metformin or PPIs long-term, your doctor may check B12 periodically or recommend supplementation. Any change in medication should be decided by your clinician.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can I get enough B12 on a vegan diet?</h3>
<p>Yes, with fortified foods (e.g. plant milks, breakfast cereals) or a B12 supplement. Many vegans take a reliable B12 supplement as recommended by a doctor or dietitian to avoid deficiency.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is B12 tested fasting?</h3>
<p>Fasting is usually not required for B12 alone, but your lab may request it if the sample is used for other tests. Follow the instructions given for your blood draw.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can I interpret my result myself?</h3>
<p>Your result should be interpreted in context (diet, medications, symptoms, other tests). Your doctor can say whether your level is appropriate for you and whether you need treatment or further tests.</p>
""",
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Medical disclaimer",
            body_html="""
<p><strong>This content is for information only and does not constitute medical advice or diagnosis.</strong> Always discuss your results and symptoms with a doctor. Do not start or change supplements or treatment based solely on this article. If you have concerns about your health, seek professional medical care.</p>
""",
        ),
    ]


def _b12_sections_de() -> List[Section]:
    return [
        Section(id="what-b12-does", level=2, heading="Was Vitamin B12 bewirkt",
            body_html="""<p>Vitamin B12 (Cobalamin) ist wichtig für <strong>Nervenfunktion</strong>, <strong>Bildung roter Blutkörperchen</strong> und <strong>DNA-Synthese</strong>. Der Körper kann es nicht selbst herstellen; es muss über die Ernährung oder ggf. vom Arzt verordnete Präparate/Spritzen zugeführt werden. Ein Mangel kann zu Anämie und bei längerer Dauer zu neurologischen Beschwerden führen. Dieser Artikel dient nur der Information und ersetzt keine ärztliche Abklärung.</p>"""),
        Section(id="typical-ranges", level=2, heading="Typische Referenzbereiche und „Grenzbereich“",
            body_html="""<p>Referenzbereiche <strong>unterscheiden sich je nach Labor und Methode</strong>. Orientieren Sie sich am Befund. Viele Labore nutzen Bereiche im Bereich von hunderten pg/mL (bzw. pmol/L); Werte unterhalb des Referenzbereichs gelten als niedrig oder mangelhaft, Werte knapp darüber oft als „Grenzbereich“. Die Bewertung hängt von Anamnese, weiteren Werten und der Einschätzung des Arztes ab. Bitte nicht selbst diagnostizieren.</p>"""),
        Section(id="causes-low", level=2, heading="Häufige Ursachen für niedriges B12",
            body_html="""<p><strong>Ernährung</strong>: Strenge vegane/vegetarische Kost ohne angereicherte Lebensmittel oder B12-Supplemente kann zu geringer Zufuhr führen. <strong>Resorption</strong>: Perniziöse Anämie, Zöliakie, Morbus Crohn oder Magen-Darm-Operationen können die Aufnahme mindern. <strong>Medikamente</strong>: Langzeitanwendung von Metformin oder Protonenpumpenhemmern (PPI) kann bei manchen Personen zu niedrigem B12 beitragen. <strong>Alter</strong>: Die Resorption kann im Alter abnehmen. Die Einordnung übernimmt der Arzt.</p>"""),
        Section(id="symptoms", level=2, heading="Symptome und wann zum Arzt",
            body_html="""<p>Mögliche Zeichen bei niedrigem B12: Müdigkeit, Schwäche, blasse Haut, Atemnot – alles <strong>unspezifisch</strong>. <strong>Neurologische Warnzeichen</strong>, die zeitnah abgeklärt werden sollten: Kribbeln oder Taubheit in Händen/Füßen, Gang- oder Gleichgewichtsstörungen, Gedächtnis- oder Konzentrationsprobleme, Stimmungsschwankungen. Die Bewertung erfolgt durch den Arzt anhand von Labor und Anamnese. Bei solchen Beschwerden oder niedrigem/grenzwertigem B12-Befund bitte zum Arzt.</p>"""),
        Section(id="related-tests", level=2, heading="Ergänzende und Bestätigungstests",
            body_html="""<p>Der Arzt kann u. a. veranlassen: <strong>Blutbild (CBC)</strong> und <strong>MCV</strong> (oft bei B12-Mangel erhöht), <strong>Folsäure</strong>, <strong>Methylmalonsäure (MMA)</strong> und <strong>Homocystein</strong>. Welche Tests nötig sind, entscheidet der Arzt.</p>"""),
        Section(id="treatment-overview", level=2, heading="Behandlung – Überblick",
            body_html="""<p>Die Therapie legt der Arzt anhand von Ursache und Schwere fest. <strong>Ernährung</strong>: Fleisch, Fisch, Eier, Milch, angereicherte Lebensmittel. Bei Mangel oft <strong>orales B12 oder B12-Spritzen</strong>; Dosis und Form nach Leitlinie und Resorption. <strong>Kontrolle</strong> oft nach etwa 8–12 Wochen – der Arzt gibt den genauen Zeitpunkt vor. Bitte keine hochdosierte Selbstmedikation.</p>"""),
        Section(id="practical-tips", level=2, heading="Praktische Hinweise",
            body_html="""<p>Bei Empfehlung zu mehr B12 über die Ernährung: zuverlässige Quellen einplanen. Bei verordneten Präparaten oder Spritzen: Einnahme wie verordnet und Kontrolltermine einhalten, damit der Arzt den Verlauf prüfen kann.</p>"""),
        Section(id="faq", level=2, heading="Häufige Fragen",
            body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Kann B12 niedrig sein bei normalem Hb?</h3>
<p>Ja. Ein B12-Mangel kann entstehen, bevor eine Anämie sichtbar wird. Die Einordnung erfolgt durch den Arzt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wie schnell bessern sich die Symptome?</h3>
<p>Das hängt von Ursache, Schwere und Therapie ab. Manche merken binnen Wochen mehr Energie; neurologische Beschwerden können länger brauchen. Dem Therapieplan folgen und anhaltende Symptome melden.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Ist hohes B12 ein Problem?</h3>
<p>Sehr hohe B12-Werte sind durch Ernährung allein selten und können mit bestimmten Erkrankungen oder Präparaten zusammenhängen. Die Bewertung übernimmt der Arzt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Muss ich Metformin oder PPI absetzen?</h3>
<p>Verordnete Medikamente nicht eigenmächtig absetzen. Bei längerer Einnahme kann der Arzt B12 kontrollieren oder Supplementation empfehlen.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Reicht B12 bei veganer Ernährung?</h3>
<p>Mit angereicherten Lebensmitteln oder einem B12-Präparat ja. Viele Veganer nehmen ein zuverlässiges B12-Supplement nach Empfehlung von Arzt oder Ernährungsberatung.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wird B12 nüchtern gemessen?</h3>
<p>Für B12 allein meist nicht nötig; das Labor kann Nüchternheit für ein Gesamtprofil verlangen.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann ich meinen Wert selbst einordnen?</h3>
<p>Die Einordnung erfolgt im Kontext (Ernährung, Medikamente, Symptome). Ihr Arzt kann beurteilen, ob Ihr Wert für Sie passend ist.</p>
"""),
        Section(id="disclaimer", level=2, heading="Hinweis",
            body_html="""<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung oder Diagnose.</strong> Besprechen Sie Ergebnisse und Beschwerden immer mit einem Arzt.</p>"""),
    ]


def _b12_sections_it() -> List[Section]:
    return [
        Section(id="what-b12-does", level=2, heading="A cosa serve la vitamina B12",
            body_html="""<p>La vitamina B12 (cobalamina) è essenziale per <strong>la funzione nervosa</strong>, <strong>la formazione dei globuli rossi</strong> e <strong>la sintesi del DNA</strong>. L’organismo non la produce; deve assumerla con la dieta o, se indicato, con integratori o iniezioni prescritti dal medico. Una carenza può portare ad anemia e, se prolungata, a sintomi neurologici. Questo articolo è solo informativo e non sostituisce una valutazione medica.</p>"""),
        Section(id="typical-ranges", level=2, heading="Intervalli tipici e „borderline“",
            body_html="""<p>Gli intervalli di riferimento <strong>variano da laboratorio a laboratorio</strong>. Usate sempre quello sul referto. Molti laboratori usano intervalli approssimativi (centinaia di pg/mL o pmol/L); valori sotto il limite possono essere indicati come bassi o carenti, valori appena sopra come „borderline“. L’interpretazione dipende dalla storia clinica, da altri esami e dal medico. Non autodiagnosticare in base al solo numero.</p>"""),
        Section(id="causes-low", level=2, heading="Cause comuni di B12 bassa",
            body_html="""<p><strong>Dieta</strong>: Diete vegane/vegetariane strette senza alimenti fortificati o integratori B12 possono portare a bassa assunzione. <strong>Assorbimento</strong>: Anemia perniciosa, celiachia, morbo di Crohn o chirurgia gastrica/intestinale possono ridurre l’assorbimento. <strong>Farmaci</strong>: Uso prolungato di metformina o inibitori della pompa protonica (PPI) può contribuire a B12 bassa in alcuni. <strong>Età</strong>: L’assorbimento può ridursi con l’età. Il medico aiuta a individuare le cause rilevanti.</p>"""),
        Section(id="symptoms", level=2, heading="Sintomi e quando rivolgersi al medico",
            body_html="""<p>Sintomi a volte associati a B12 bassa: stanchezza, debolezza, pallore, fiato corto – tutti <strong>aspecifici</strong>. <strong>Segnali neurologici</strong> da far valutare subito: formicolio o intorpidimento a mani/piedi, problemi di equilibrio o deambulazione, memoria o concentrazione, umore. La diagnosi non si fa solo con i sintomi; servono esami e anamnesi. In caso di tali sintomi o risultato basso/borderline, rivolgersi al medico.</p>"""),
        Section(id="related-tests", level=2, heading="Esami correlati e di conferma",
            body_html="""<p>Il medico può prescrivere: <strong>emocromo (CBC)</strong> e <strong>MCV</strong> (spesso elevato in carenza di B12), <strong>folati</strong>, <strong>acido metilmalonico (MMA)</strong> e <strong>omocisteina</strong>. Quali esami servono è una decisione clinica.</p>"""),
        Section(id="treatment-overview", level=2, heading="Trattamento – panoramica",
            body_html="""<p>La gestione è decisa dal medico in base a causa e gravità. <strong>Fonti alimentari</strong>: carne, pesce, uova, latticini, alimenti fortificati. In carenza spesso <strong>B12 orale o iniettabile</strong>; dose e via secondo linee guida e assorbimento. <strong>Controllo</strong> spesso dopo 8–12 settimane – il medico indicherà tempi e obiettivi. Non assumere alte dosi di B12 senza indicazione medica.</p>"""),
        Section(id="practical-tips", level=2, heading="Consigli pratici",
            body_html="""<p>Se il medico consiglia più B12 dalla dieta: includere fonti affidabili. Se sono prescritti integratori o iniezioni: assumerli come indicato e rispettare i controlli per verificare il miglioramento.</p>"""),
        Section(id="faq", level=2, heading="Domande frequenti",
            body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">La B12 può essere bassa con emoglobina normale?</h3>
<p>Sì. La carenza di B12 può precedere l’anemia. L’interpretazione spetta al medico.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Quanto velocemente migliorano i sintomi?</h3>
<p>Dipende da causa, gravità e terapia. Qualcuno nota più energia in settimane; i sintomi neurologici possono richiedere più tempo. Seguire il piano del medico e segnalare sintomi persistenti.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La B12 alta è un problema?</h3>
<p>Valori molto alti sono rari con la sola dieta e possono essere legati ad alcune condizioni o integratori. La valutazione spetta al medico.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Devo sospendere metformina o PPI?</h3>
<p>Non sospendere i farmaci prescritti di propria iniziativa. In caso di uso prolungato il medico può controllare la B12 o consigliare integrazione.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Si può avere abbastanza B12 con dieta vegana?</h3>
<p>Sì, con alimenti fortificati o un integratore B12. Molti vegani assumono un integratore B12 affidabile su consiglio del medico o del dietista.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La B12 si misura a digiuno?</h3>
<p>Per la sola B12 di solito no; il laboratorio può richiedere il digiuno per un pannello più ampio.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Posso interpretare il risultato da solo?</h3>
<p>Il risultato va interpretato nel contesto (dieta, farmaci, sintomi). Il medico può dire se il livello è adeguato per voi.</p>
"""),
        Section(id="disclaimer", level=2, heading="Nota",
            body_html="""<p><strong>Questo contenuto è solo informativo e non costituisce consulenza o diagnosi medica.</strong> Discutete sempre risultati e sintomi con un medico.</p>"""),
    ]


def _b12_sections_fr() -> List[Section]:
    return [
        Section(id="what-b12-does", level=2, heading="À quoi sert la vitamine B12",
            body_html="""<p>La vitamine B12 (cobalamine) est essentielle pour <strong>le fonctionnement des nerfs</strong>, <strong>la formation des globules rouges</strong> et <strong>la synthèse de l’ADN</strong>. L’organisme ne la produit pas ; elle doit venir de l’alimentation ou, si besoin, de compléments ou injections prescrits par un médecin. Une carence peut entraîner une anémie et, si elle dure, des symptômes neurologiques. Cet article est à titre informatif uniquement et ne remplace pas un avis médical.</p>"""),
        Section(id="typical-ranges", level=2, heading="Fourchettes typiques et « limite »",
            body_html="""<p>Les fourchettes de référence <strong>varient selon le laboratoire et la méthode</strong>. Utilisez toujours celle de votre résultat. Beaucoup de laboratoires utilisent des fourchettes approximatives (centaines de pg/mL ou pmol/L) ; les valeurs en dessous peuvent être qualifiées de basses ou carence, juste au-dessus de « limite ». L’interprétation dépend de votre histoire, d’autres examens et du médecin. Ne pas s’autodiagnostiquer sur un seul chiffre.</p>"""),
        Section(id="causes-low", level=2, heading="Causes fréquentes d’un taux bas de B12",
            body_html="""<p><strong>Alimentation</strong> : Régimes vegan/végétarien stricts sans aliments enrichis ou compléments B12 peuvent entraîner une faible ingestion. <strong>Absorption</strong> : Anémie de Biermer, maladie cœliaque, Crohn ou chirurgie gastrique/intestinale peuvent réduire l’absorption. <strong>Médicaments</strong> : Prise prolongée de metformine ou inhibiteurs de la pompe à protons (IPP) peut contribuer à un taux bas chez certains. <strong>Âge</strong> : L’absorption peut diminuer avec l’âge. Le médecin aide à identifier les causes pertinentes.</p>"""),
        Section(id="symptoms", level=2, heading="Symptômes et quand consulter",
            body_html="""<p>Signes parfois associés à un taux bas : fatigue, faiblesse, pâleur, essoufflement – <strong>non spécifiques</strong>. <strong>Signaux neurologiques</strong> à faire évaluer rapidement : fourmillements ou engourdissement mains/pieds, problèmes d’équilibre ou de marche, mémoire ou concentration, humeur. Les symptômes seuls ne permettent pas le diagnostic ; ils doivent être interprétés avec les examens et l’histoire par un médecin. En cas de tels symptômes ou résultat bas/limite, consulter un médecin.</p>"""),
        Section(id="related-tests", level=2, heading="Examens complémentaires et de confirmation",
            body_html="""<p>Le médecin peut prescrire : <strong>numération (CBC)</strong> et <strong>VGM</strong> (souvent élevé en carence B12), <strong>folates</strong>, <strong>acide méthylmalonique (MMA)</strong> et <strong>homocystéine</strong>. Le choix des examens est une décision médicale.</p>"""),
        Section(id="treatment-overview", level=2, heading="Traitement – aperçu",
            body_html="""<p>La prise en charge est décidée par le médecin selon la cause et la sévérité. <strong>Sources alimentaires</strong> : viande, poisson, œufs, laitages, aliments enrichis. En carence, souvent <strong>B12 orale ou en injection</strong> ; dose et voie selon recommandations et absorption. <strong>Contrôle</strong> souvent vers 8–12 semaines – le médecin indiquera le moment et l’objectif. Ne pas prendre de fortes doses de B12 sans avis médical.</p>"""),
        Section(id="practical-tips", level=2, heading="Conseils pratiques",
            body_html="""<p>Si le médecin recommande plus de B12 par l’alimentation : inclure des sources fiables. Si des compléments ou injections sont prescrits : les prendre comme indiqué et respecter les contrôles pour vérifier l’évolution.</p>"""),
        Section(id="faq", level=2, heading="Questions fréquentes",
            body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">La B12 peut-elle être basse avec une hémoglobine normale ?</h3>
<p>Oui. La carence en B12 peut précéder l’anémie. L’interprétation relève du médecin.</p>
<h3 class="text-base font-semibold mt-4 mb-1">À quelle vitesse les symptômes s’améliorent-ils ?</h3>
<p>Cela dépend de la cause, de la sévérité et du traitement. Certains sentent plus d’énergie en quelques semaines ; les symptômes neurologiques peuvent mettre plus de temps. Suivre le plan du médecin et signaler les symptômes persistants.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Un taux élevé de B12 est-il un problème ?</h3>
<p>Des taux très élevés sont rares avec la seule alimentation et peuvent être liés à certaines pathologies ou compléments. L’interprétation relève du médecin.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Faut-il arrêter la metformine ou les IPP ?</h3>
<p>Ne pas arrêter les médicaments prescrits de sa propre initiative. En cas de prise prolongée, le médecin peut contrôler la B12 ou recommander une supplémentation.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Peut-on avoir assez de B12 en vegan ?</h3>
<p>Oui, avec des aliments enrichis ou un complément B12. Beaucoup de vegans prennent un complément B12 fiable sur conseil du médecin ou du diététicien.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La B12 se dose-t-elle à jeun ?</h3>
<p>Pour la B12 seule, en général non ; le laboratoire peut demander le jeûne pour un bilan plus large.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Puis-je interpréter mon résultat moi-même ?</h3>
<p>Le résultat doit être interprété dans le contexte (alimentation, médicaments, symptômes). Votre médecin peut dire si le taux vous convient.</p>
"""),
        Section(id="disclaimer", level=2, heading="Avertissement",
            body_html="""<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis médical ni un diagnostic.</strong> Discutez toujours de vos résultats et symptômes avec un médecin.</p>"""),
    ]


_VITAMIN_B12_ARTICLE = _article_vitamin_b12()


def _article_hba1c() -> Article:
    """HbA1c: what it measures, prediabetes/diabetes ranges, eAG, confounders, when to see a doctor. en, de, it, fr."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/hba1c-hero.png"
    cover_alt_text = {
        "en": "HbA1c test and diabetes monitoring dashboard — NoryaAI",
        "de": "HbA1c-Test und Diabetes-Überwachung — NoryaAI",
        "it": "HbA1c test and diabetes monitoring dashboard — NoryaAI",
        "fr": "HbA1c test and diabetes monitoring dashboard — NoryaAI",
    }
    faq_qa = {
        "en": [
            {"question": "How fast can HbA1c change?", "answer": "HbA1c reflects average glucose over about 2–3 months. Meaningful change usually takes at least several weeks of sustained difference in blood sugar. Your clinician can advise when to repeat the test."},
            {"question": "Is an HbA1c of 5.8% bad?", "answer": "5.8% falls in the prediabetes range (5.7–6.4%). It does not mean you have diabetes, but it suggests higher risk and that lifestyle measures and possibly repeat testing or further assessment may be recommended. Interpretation is for your doctor."},
            {"question": "Why might my HbA1c be high but fasting glucose normal?", "answer": "HbA1c reflects 2–3 months of glucose; fasting glucose is a single snapshot. Post-meal or overnight glucose can be elevated while fasting stays normal. Certain conditions (e.g. anemia, hemoglobin variants) can also affect HbA1c. Your doctor can help explain your pattern."},
            {"question": "What about anemia and HbA1c?", "answer": "Iron deficiency, B12 or folate deficiency, and other causes of anemia can skew HbA1c (often lowering it). Hemoglobin variants can also affect results. If you have known or suspected anemia, your clinician will take this into account when interpreting HbA1c."},
            {"question": "Do I need to fast for HbA1c?", "answer": "HbA1c can usually be measured non-fasting. If the same blood draw is used for fasting glucose or lipids, your lab will ask you to fast; follow the instructions given for your test."},
            {"question": "What is a normal HbA1c?", "answer": "In general guidelines, below 5.7% is often considered in the normal (non-diabetic) range. Exact cut-offs and reference ranges vary by lab and guideline; your clinician interprets your result in context."},
        ],
        "de": [
            {"question": "Wie schnell kann sich der HbA1c ändern?", "answer": "Der HbA1c spiegelt den durchschnittlichen Glukosewert über etwa 2–3 Monate wider. Eine merkliche Änderung dauert in der Regel mindestens mehrere Wochen. Ihr Arzt legt den Zeitpunkt der Kontrolle fest."},
            {"question": "Ist ein HbA1c von 5,8 % schlecht?", "answer": "5,8 % liegt im Prädiabetes-Bereich (5,7–6,4 %). Das bedeutet nicht zwingend Diabetes, weist aber auf ein höheres Risiko hin; Lebensstilmaßnahmen und ggf. Kontrollen können sinnvoll sein. Die Einordnung übernimmt Ihr Arzt."},
            {"question": "Warum ist mein HbA1c hoch, der Nüchternzucker aber normal?", "answer": "HbA1c erfasst 2–3 Monate Glukose; Nüchternzucker ist eine Momentaufnahme. Nach dem Essen oder nachts kann der Zucker erhöht sein. Auch Anämie oder Hämoglobinvarianten können den HbA1c beeinflussen. Ihr Arzt kann Ihr Muster erklären."},
            {"question": "Was ist mit Anämie und HbA1c?", "answer": "Eisenmangel, B12- oder Folsäuremangel und andere Ursachen einer Anämie können den HbA1c verfälschen (oft nach unten). Hämoglobinvarianten ebenfalls. Bei bekannter oder vermuteter Anämie berücksichtigt Ihr Arzt dies bei der Bewertung."},
            {"question": "Muss ich für HbA1c nüchtern sein?", "answer": "HbA1c kann in der Regel ohne Nüchternheit gemessen werden. Wird dasselbe Blut für Nüchternglukose oder Fette verwendet, verlangt das Labor Nüchternheit; folgen Sie den Anweisungen."},
            {"question": "Was ist ein normaler HbA1c?", "answer": "Nach gängigen Leitlinien gilt oft unter 5,7 % als Normalbereich. Grenzwerte und Referenzbereiche variieren je nach Labor und Leitlinie; Ihr Arzt interpretiert Ihren Wert im Kontext."},
        ],
        "it": [
            {"question": "Quanto velocemente può cambiare l'HbA1c?", "answer": "L'HbA1c riflette la glicemia media in circa 2–3 mesi. Un cambiamento significativo richiede di solito almeno diverse settimane. Il medico consiglierà quando ripetere l'esame."},
            {"question": "Un HbA1c del 5,8% è preoccupante?", "answer": "Il 5,8% rientra nell'intervallo del prediabete (5,7–6,4%). Non significa diabete, ma indica un rischio maggiore; stile di vita e eventuali controlli possono essere consigliati. L'interpretazione spetta al medico."},
            {"question": "Perché l'HbA1c è alto ma la glicemia a digiuno normale?", "answer": "L'HbA1c riflette 2–3 mesi di glucosio; la glicemia a digiuno è un singolo valore. Il glucosio dopo i pasti o notturno può essere alto. Anemia o varianti dell'emoglobina possono alterare l'HbA1c. Il medico può spiegare il quadro."},
            {"question": "E l'anemia e l'HbA1c?", "answer": "Carenza di ferro, B12 o folati e altre cause di anemia possono alterare l'HbA1c (spesso abbassandolo). Anche varianti dell'emoglobina. In caso di anemia nota o sospetta, il medico ne terrà conto nell'interpretazione."},
            {"question": "Devo essere a digiuno per l'HbA1c?", "answer": "L'HbA1c di solito si può misurare non a digiuno. Se il prelievo è usato anche per glicemia a digiuno o lipidi, il laboratorio richiederà il digiuno; seguite le istruzioni."},
            {"question": "Qual è un HbA1c normale?", "answer": "In linee guida generali, sotto 5,7% è spesso considerato nella norma. I limiti variano per laboratorio e linee guida; il medico interpreta il risultato nel contesto."},
        ],
        "fr": [
            {"question": "À quelle vitesse l'HbA1c peut-il changer ?", "answer": "L'HbA1c reflète la glycémie moyenne sur environ 2–3 mois. Un changement significatif prend généralement au moins plusieurs semaines. Votre médecin indiquera quand répéter le dosage."},
            {"question": "Un HbA1c à 5,8 % est-il mauvais ?", "answer": "5,8 % se situe dans la zone prédiabète (5,7–6,4 %). Ce n'est pas un diabète, mais cela suggère un risque accru ; mesures hygiéno-diététiques et éventuellement contrôles peuvent être recommandés. L'interprétation relève du médecin."},
            {"question": "Pourquoi mon HbA1c est élevé mais ma glycémie à jeun normale ?", "answer": "L'HbA1c reflète 2–3 mois de glucose ; la glycémie à jeun est un instantané. La glycémie post-prandiale ou nocturne peut être élevée. Anémie ou variants d'hémoglobine peuvent aussi fausser l'HbA1c. Votre médecin peut expliquer votre profil."},
            {"question": "Et l'anémie et l'HbA1c ?", "answer": "Carence en fer, B12 ou folates et autres causes d'anémie peuvent fausser l'HbA1c (souvent à la baisse). Les variants d'hémoglobine aussi. En cas d'anémie connue ou suspectée, le médecin en tiendra compte."},
            {"question": "Faut-il être à jeun pour l'HbA1c ?", "answer": "L'HbA1c peut en général être dosé sans être à jeun. Si le prélèvement sert aussi à la glycémie à jeun ou aux lipides, le laboratoire demandera le jeûne ; suivez les consignes."},
            {"question": "Quel est un HbA1c normal ?", "answer": "En général, en dessous de 5,7 % est souvent considéré comme normal. Les seuils varient selon le laboratoire et les recommandations ; votre médecin interprète le résultat dans le contexte."},
        ],
    }
    return Article(
        id="hba1c-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=11,
        cover_image=cover,
        cover_alt=cover_alt_text,
        faq_schema_qa=faq_qa,
        category={
            "en": "Diabetes & Metabolic Health",
            "de": "Diabetes & Stoffwechselgesundheit",
            "it": "Diabete e salute metabolica",
            "fr": "Diabète et santé métabolique",
            "tr": "Diyabet ve Metabolik Sağlık",
            "es": "Diabetes y salud metabólica",
            "he": "סוכרת ובריאות מטבולית",
            "hi": "मधुमेह और मेटाबॉलिक स्वास्थ्य",
            "ar": "السكري والصحة الأيضية",
        },
        slugs={
            "en": "hba1c-what-it-means",
            "de": "hba1c-what-it-means",
            "it": "hba1c-what-it-means",
            "fr": "hba1c-what-it-means",
            "tr": "hba1c-what-it-means",
            "es": "hba1c-what-it-means",
            "he": "hba1c-what-it-means",
            "hi": "hba1c-what-it-means",
            "ar": "hba1c-what-it-means",
        },
        titles={
            "en": "HbA1c Explained: How to Interpret Prediabetes and Diabetes Ranges",
            "de": "HbA1c verstehen: Prädiabetes- und Diabetes-Bereiche richtig deuten",
            "it": "HbA1c: come interpretare prediabete e diabete",
            "fr": "HbA1c : interpréter les seuils de prédiabète et de diabète",
            "tr": "HbA1c: Prediyabet ve Diyabet Aralıkları Nasıl Yorumlanır",
            "es": "HbA1c: cómo interpretar prediabetes y diabetes",
            "he": "HbA1c: איך לפרש טרום-סוכרת וסוכרת",
            "hi": "HbA1c: प्रीडायबिटीज और डायबिटीज रेंज कैसे समझें",
            "ar": "HbA1c: كيف تُفسَّر مرحلة ما قبل السكري والسكري",
        },
        subtitles={
            "en": "What HbA1c measures, typical diagnostic ranges, eAG, factors that can skew results, and when to follow up with a clinician.",
            "de": "Was HbA1c misst, typische Grenzbereiche, eAG, störende Faktoren und wann Sie zum Arzt sollten.",
            "it": "Cosa misura l'HbA1c, intervalli diagnostici tipici, eAG, fattori che possono alterare il risultato e quando rivolgersi al medico.",
            "fr": "Ce que mesure l'HbA1c, seuils diagnostiques typiques, eAG, facteurs pouvant fausser le résultat et quand consulter.",
            "tr": "HbA1c ne ölçer, tipik tanı aralıkları ve ne zaman doktora gidilmeli.",
            "es": "Qué mide el HbA1c, rangos típicos y cuándo consultar.",
            "he": "מה HbA1c מודד, טווחים אופייניים ומתי לרופא.",
            "hi": "HbA1c क्या मापता है, रेंज और डॉक्टर से कब मिलें।",
            "ar": "ماذا يقيس HbA1c والنطاقات ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "HbA1c reflects average blood glucose over about 2–3 months. Understanding typical ranges and confounders helps you discuss results with your doctor.",
            "de": "HbA1c spiegelt den durchschnittlichen Blutzucker über etwa 2–3 Monate wider. Typische Bereiche und Störfaktoren helfen beim Arztgespräch.",
            "it": "L'HbA1c riflette la glicemia media in circa 2–3 mesi. Conoscere gli intervalli tipici e i fattori confondenti aiuta a parlarne con il medico.",
            "fr": "L'HbA1c reflète la glycémie moyenne sur environ 2–3 mois. Comprendre les seuils typiques et les facteurs de confusion aide à en parler avec le médecin.",
            "tr": "HbA1c yaklaşık 2–3 aylık ortalama kan şekerini yansıtır. Tipik aralıklar ve karıştırıcı faktörler doktorla sonuçları tartışmanıza yardımcı olur.",
            "es": "El HbA1c refleja la glucosa media en unos 2–3 meses. Entender los rangos típicos ayuda a hablar con el médico.",
            "he": "HbA1c משקף את רמת הגלוקוז הממוצעת בכ־2–3 חודשים. הבנת הטווחים עוזרת לשיחה עם הרופא.",
            "hi": "HbA1c लगभग 2–3 महीने का औसत ब्लड ग्लूकोज दर्शाता है। रेंज समझकर डॉक्टर से बात करें।",
            "ar": "HbA1c يعكس متوسط جلوكوز الدم خلال نحو 2–3 أشهر. فهم النطاقات يساعد في مناقشة النتائج مع الطبيب.",
        },
        seo_titles={
            "en": "HbA1c Explained: How to Interpret Prediabetes and Diabetes Ranges | NoryaAI",
            "de": "HbA1c verstehen: Prädiabetes- und Diabetes-Bereiche | NoryaAI",
            "it": "HbA1c: come interpretare prediabete e diabete | NoryaAI",
            "fr": "HbA1c : interpréter les seuils de prédiabète et de diabète | NoryaAI",
            "tr": "HbA1c: Prediyabet ve Diyabet Aralıkları | NoryaAI",
            "es": "HbA1c: prediabetes y diabetes | NoryaAI",
            "he": "HbA1c: טרום-סוכרת וסוכרת | NoryaAI",
            "hi": "HbA1c: प्रीडायबिटीज और डायबिटीज | NoryaAI",
            "ar": "HbA1c: مرحلة ما قبل السكري والسكري | NoryaAI",
        },
        seo_descriptions={
            "en": "Understand HbA1c: what it measures, typical prediabetes and diabetes ranges, eAG, what can skew results, and when to see a clinician. Informational only.",
            "de": "HbA1c verstehen: was er misst, typische Grenzbereiche, eAG, Störfaktoren und wann zum Arzt. Nur zur Information.",
            "it": "Capire l'HbA1c: cosa misura, intervalli tipici, eAG, fattori confondenti e quando rivolgersi al medico. Solo informativo.",
            "fr": "Comprendre l'HbA1c : ce qu'il mesure, seuils typiques, eAG, facteurs de confusion et quand consulter. À titre informatif uniquement.",
            "tr": "HbA1c: ne ölçer, prediyabet ve diyabet aralıkları, ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "Entiende HbA1c: qué mide, rangos típicos y cuándo consultar. Solo informativo.",
            "he": "הבן HbA1c: מה הוא מודד, טווחים ומתי לרופא. למידע בלבד.",
            "hi": "HbA1c समझें: क्या मापता है, रेंज और डॉक्टर से कब मिलें। सूचनात्मक।",
            "ar": "افهم HbA1c: ماذا يقيس والنطاقات ومتى ترى الطبيب. للمعلومات فقط.",
        },
        sections_by_lang={
            "en": _hba1c_sections_en(),
            "de": _hba1c_sections_de(),
            "it": _hba1c_sections_it(),
            "fr": _hba1c_sections_fr(),
        },
    )


def _hba1c_sections_en() -> List[Section]:
    return [
        Section(
            id="what-hba1c-measures",
            level=2,
            heading="What HbA1c measures",
            body_html="""
<p>HbA1c (glycated haemoglobin A1c) is a form of haemoglobin that has glucose attached to it. It reflects your <strong>average blood glucose over roughly 2–3 months</strong>, because red blood cells live about that long. The more glucose in your blood over that period, the higher the proportion of haemoglobin that becomes glycated. Laboratories report HbA1c as a percentage (e.g. 5.6%) or in mmol/mol in some countries. This test is widely used to screen for and monitor diabetes and prediabetes, and to guide treatment. It does not replace a clinical diagnosis; interpretation and any treatment decisions are made by your doctor.</p>
""",
        ),
        Section(
            id="typical-diagnostic-ranges",
            level=2,
            heading="Typical diagnostic ranges",
            body_html="""
<p>Reference and diagnostic cut-offs <strong>vary by laboratory and guideline</strong>. The following are commonly used for context only; your lab and clinician use the criteria that apply to your situation. In many guidelines:</p>
<ul>
  <li><strong>Normal</strong>: below 5.7% (often &lt;5.7%).</li>
  <li><strong>Prediabetes</strong>: 5.7–6.4%.</li>
  <li><strong>Diabetes</strong>: 6.5% or above (≥6.5%).</li>
</ul>
<p>These ranges are for general information. The final classification (normal, prediabetes, or diabetes) is a <strong>clinical and laboratory decision</strong> made by your doctor using your result, your history, and sometimes repeat or additional tests. Do not self-diagnose; discuss your result with a clinician.</p>
""",
        ),
        Section(
            id="hba1c-vs-fasting-vs-ogtt",
            level=2,
            heading="HbA1c vs fasting glucose vs OGTT",
            body_html="""
<p>Different tests give different information:</p>
<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">
  <thead><tr class="bg-slate-50"><th class="border border-slate-200 px-3 py-2 text-left">Test</th><th class="border border-slate-200 px-3 py-2 text-left">What it reflects</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>HbA1c</strong></td><td class="border border-slate-200 px-3 py-2">Average glucose over ~2–3 months; no fasting needed for HbA1c itself.</td></tr>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>Fasting glucose</strong></td><td class="border border-slate-200 px-3 py-2">Blood sugar at a single time after fasting (often 8+ hours).</td></tr>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>OGTT (oral glucose tolerance)</strong></td><td class="border border-slate-200 px-3 py-2">Glucose before and after a standard glucose drink; used in some diagnostic and pregnancy protocols.</td></tr>
  </tbody>
</table>
<p>Your doctor may use one or more of these, depending on the clinical situation and local guidelines.</p>
""",
        ),
        Section(
            id="estimated-average-glucose",
            level=2,
            heading="Estimated Average Glucose (eAG)",
            body_html="""
<p>Some labs or reports show an <strong>Estimated Average Glucose (eAG)</strong> next to your HbA1c. This is a calculated estimate of what your average blood glucose might have been (e.g. in mg/dL or mmol/L) over the period that HbA1c reflects. It is <strong>not a precise measurement</strong> and is meant only to help you relate the percentage to everyday glucose units. Do not use it as the sole basis for treatment; your clinician will interpret your actual HbA1c and other results in context.</p>
""",
        ),
        Section(
            id="what-can-skew-hba1c",
            level=2,
            heading="What can skew HbA1c",
            body_html="""
<p>Several conditions can make HbA1c less reliable or harder to interpret:</p>
<ul>
  <li><strong>Anaemia / iron deficiency</strong>: Can alter red cell turnover and haemoglobin, affecting HbA1c.</li>
  <li><strong>Haemoglobin variants</strong>: Some genetic variants (e.g. sickle cell trait, thalassaemia) can interfere with certain HbA1c methods.</li>
  <li><strong>Pregnancy</strong>: Guidelines may prefer other tests (e.g. fasting glucose, OGTT) for screening or diagnosis in pregnancy.</li>
  <li><strong>Kidney disease</strong>: Can affect red cell life span and haemoglobin; interpretation may need adjustment.</li>
  <li><strong>Recent blood loss or transfusion</strong>: Can change the mix of red cells and thus HbA1c.</li>
  <li><strong>Other</strong>: Severe liver disease, some medications, or recent major illness can sometimes influence results.</li>
</ul>
<p>If any of these apply to you, your clinician will take them into account when interpreting your HbA1c.</p>
""",
        ),
        Section(
            id="when-to-follow-up",
            level=2,
            heading="When to follow up with a clinician",
            body_html="""
<p>You should see a doctor or nurse for interpretation and next steps if:</p>
<ul>
  <li>Your <strong>HbA1c is 6.5% or above</strong> (or in a range your lab flags as diabetes).</li>
  <li>Your HbA1c has <strong>risen quickly</strong> or is in the prediabetes range and you have risk factors or symptoms.</li>
  <li>You have <strong>symptoms</strong> such as unusual thirst, frequent urination, unexplained weight loss, fatigue, or blurred vision.</li>
  <li>You are <strong>pregnant</strong> or planning pregnancy and have questions about glucose or diabetes screening.</li>
  <li>You have conditions that can skew HbA1c (e.g. anaemia, haemoglobin variant) and need guidance on which tests to use.</li>
</ul>
<p>This article is for information only; it does not replace a clinical assessment. Always discuss your results and symptoms with a healthcare provider.</p>
""",
        ),
        Section(
            id="next-steps-clinician",
            level=2,
            heading="Next steps a clinician may consider",
            body_html="""
<p>Depending on your result and history, your doctor may:</p>
<ul>
  <li>Repeat the HbA1c or order <strong>fasting glucose</strong> or an <strong>OGTT</strong> to confirm or clarify.</li>
  <li>Check <strong>lipids</strong>, <strong>kidney function</strong> (e.g. creatinine, eGFR), and <strong>urine albumin</strong> as part of cardiovascular and kidney risk assessment.</li>
  <li>Monitor <strong>blood pressure</strong> and advise on lifestyle (diet, activity, weight, sleep) and, if needed, medication.</li>
</ul>
<p>Which tests and treatments are chosen is a clinical decision made with you by your doctor.</p>
""",
        ),
        Section(
            id="practical-lifestyle",
            level=2,
            heading="Practical lifestyle overview",
            body_html="""
<p>General principles that often support metabolic health (and are not a substitute for medical advice):</p>
<ul>
  <li><strong>Diet</strong>: Balanced meals, plenty of vegetables and fibre, limited added sugars and highly processed foods; portion awareness. No specific “diabetes diet” is required for everyone—your doctor or dietitian can tailor advice.</li>
  <li><strong>Activity</strong>: Regular physical activity (e.g. 150 minutes per week of moderate exercise, or as advised for you) can help improve glucose and overall health.</li>
  <li><strong>Sleep</strong>: Adequate, regular sleep supports metabolism and well-being.</li>
  <li><strong>Weight</strong>: If your doctor has recommended weight management, gradual, sustained changes are usually more effective than short-term diets. This is general guidance only; no medication or supplement is recommended here—your clinician will advise on any treatment.</li>
</ul>
""",
        ),
        Section(
            id="faq",
            level=2,
            heading="Frequently asked questions",
            body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">How fast can HbA1c change?</h3>
<p>HbA1c reflects average glucose over about 2–3 months. Meaningful change usually takes at least several weeks of sustained difference in blood sugar. Your clinician can advise when to repeat the test.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is an HbA1c of 5.8% bad?</h3>
<p>5.8% falls in the prediabetes range (5.7–6.4%). It does not mean you have diabetes, but it suggests higher risk and that lifestyle measures and possibly repeat testing or further assessment may be recommended. Interpretation is for your doctor.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Why might my HbA1c be high but fasting glucose normal?</h3>
<p>HbA1c reflects 2–3 months of glucose; fasting glucose is a single snapshot. Post-meal or overnight glucose can be elevated while fasting stays normal. Certain conditions (e.g. anemia, hemoglobin variants) can also affect HbA1c. Your doctor can help explain your pattern.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What about anemia and HbA1c?</h3>
<p>Iron deficiency, B12 or folate deficiency, and other causes of anemia can skew HbA1c (often lowering it). Hemoglobin variants can also affect results. If you have known or suspected anemia, your clinician will take this into account when interpreting HbA1c.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Do I need to fast for HbA1c?</h3>
<p>HbA1c can usually be measured non-fasting. If the same blood draw is used for fasting glucose or lipids, your lab will ask you to fast; follow the instructions given for your test.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What is a normal HbA1c?</h3>
<p>In general guidelines, below 5.7% is often considered in the normal (non-diabetic) range. Exact cut-offs and reference ranges vary by lab and guideline; your clinician interprets your result in context.</p>
""",
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Medical disclaimer",
            body_html="""
<p><strong>This content is for information only and does not constitute medical advice, diagnosis, or treatment.</strong> Always discuss your results and any symptoms with a qualified healthcare provider. Do not start or change diet, exercise, or medication based solely on this article. If you have concerns about your health, seek professional medical care.</p>
""",
        ),
    ]


def _hba1c_sections_de() -> List[Section]:
    return [
        Section(id="what-hba1c-measures", level=2, heading="Was HbA1c misst",
            body_html="<p>HbA1c (glykiertes Hämoglobin A1c) ist Hämoglobin mit gebundenem Glukose. Es spiegelt Ihren <strong>durchschnittlichen Blutzucker über etwa 2–3 Monate</strong> wider. Je mehr Glukose in dieser Zeit im Blut, desto höher der Anteil glykierter Hämoglobine. Labore geben HbA1c oft in % (z. B. 5,6 %) oder in mmol/mol an. Der Test dient u. a. zum Screening und zur Verlaufskontrolle bei Diabetes und Prädiabetes. Die Bewertung und Therapieentscheidung obliegt dem Arzt.</p>"),
        Section(id="typical-diagnostic-ranges", level=2, heading="Typische Grenzbereiche",
            body_html="<p>Referenz- und Grenzwerte <strong>variieren je nach Labor und Leitlinie</strong>. Zur groben Orientierung (nur Kontext): <strong>Normal</strong> oft &lt;5,7 %; <strong>Prädiabetes</strong> 5,7–6,4 %; <strong>Diabetes</strong> ≥6,5 %. Die Einordnung (Normal, Prädiabetes, Diabetes) ist eine <strong>klinisch-labormedizinische Entscheidung</strong> durch Ihren Arzt. Bitte nicht selbst diagnostizieren.</p>"),
        Section(id="hba1c-vs-fasting-vs-ogtt", level=2, heading="HbA1c vs. Nüchternglukose vs. oGTT",
            body_html="<p><strong>HbA1c</strong>: Durchschnitt über ~2–3 Monate; für den HbA1c selbst meist kein Nüchtern nötig. <strong>Nüchternglukose</strong>: Einzelwert nach Fasten (z. B. 8+ Stunden). <strong>oGTT</strong>: Glukose vor und nach Trinklösung; u. a. in Diagnostik und Schwangerschaft. Welche Tests der Arzt anordnet, hängt von der Situation und den Leitlinien ab.</p>"),
        Section(id="estimated-average-glucose", level=2, heading="Geschätzte durchschnittliche Glukose (eAG)",
            body_html="<p>Manche Berichte zeigen einen <strong>eAG</strong> (geschätzte durchschnittliche Glukose) neben dem HbA1c. Das ist eine <strong>Schätzung</strong>, kein exakter Wert, und dient nur der Veranschaulichung (z. B. in mg/dL). Die Interpretation von HbA1c und weiteren Werten übernimmt Ihr Arzt.</p>"),
        Section(id="what-can-skew-hba1c", level=2, heading="Was den HbA1c verfälschen kann",
            body_html="<p>U. a.: <strong>Anämie/Eisenmangel</strong>, <strong>Hämoglobinvarianten</strong>, <strong>Schwangerschaft</strong> (oft andere Tests bevorzugt), <strong>Nierenerkrankung</strong>, <strong>kürzlicher Blutverlust oder Transfusion</strong>, schwere Lebererkrankung oder bestimmte Medikamente. Bei Zutreffen berücksichtigt Ihr Arzt dies bei der Bewertung.</p>"),
        Section(id="when-to-follow-up", level=2, heading="Wann Sie zum Arzt sollten",
            body_html="<p>Bitte zum Arzt, wenn: HbA1c <strong>≥6,5 %</strong> (oder als Diabetes eingestuft), <strong>schneller Anstieg</strong> oder Prädiabetes mit Risikofaktoren/Symptomen, <strong>Symptome</strong> wie starker Durst, häufiges Wasserlassen, Gewichtsverlust, Müdigkeit, Sehstörungen, <strong>Schwangerschaft</strong> oder geplante Schwangerschaft, oder bekannte Störfaktoren (z. B. Anämie). Dieser Artikel ersetzt keine ärztliche Bewertung.</p>"),
        Section(id="next-steps-clinician", level=2, heading="Mögliche nächste Schritte",
            body_html="<p>Der Arzt kann z. B. HbA1c wiederholen, <strong>Nüchternglukose</strong> oder <strong>oGTT</strong> veranlassen, <strong>Lipide</strong>, <strong>Nierenfunktion</strong> (z. B. Kreatinin, eGFR), <strong>Urin-Albumin</strong> und <strong>Blutdruck</strong> prüfen sowie zu Lebensstil (Ernährung, Bewegung, Gewicht, Schlaf) und ggf. Medikation beraten. Die Auswahl trifft der Arzt mit Ihnen.</p>"),
        Section(id="practical-lifestyle", level=2, heading="Praktischer Lebensstil-Überblick",
            body_html="<p>Allgemeine Prinzipien (kein Ersatz für ärztlichen Rat): <strong>Ernährung</strong>: ausgewogen, viel Gemüse und Ballaststoffe, wenig zugesetzter Zucker und stark verarbeitete Lebensmittel. <strong>Bewegung</strong>: z. B. 150 Min./Woche moderate Aktivität. <strong>Schlaf</strong>: ausreichend und regelmäßig. <strong>Gewicht</strong>: falls vom Arzt empfohlen, eher langfristige, stetige Änderungen. Keine Medikamenten- oder Supplementempfehlung hier—Ihr Arzt berät.</p>"),
        Section(id="faq", level=2, heading="Häufige Fragen",
            body_html="<p>Siehe Abschnitt „Häufige Fragen“ oben; die Bewertung Ihres Wertes erfolgt durch den Arzt.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
            body_html="<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung, Diagnose oder Behandlung.</strong> Besprechen Sie Ergebnisse und Beschwerden immer mit einem Arzt. Keine Änderung von Ernährung, Bewegung oder Medikation nur aufgrund dieses Artikels.</p>"),
    ]


def _hba1c_sections_it() -> List[Section]:
    return [
        Section(id="what-hba1c-measures", level=2, heading="Cosa misura l'HbA1c",
            body_html="<p>L'HbA1c (emoglobina glicata A1c) riflette la <strong>glicemia media in circa 2–3 mesi</strong>. Più glucosio nel sangue in quel periodo, più emoglobina glicata. I laboratori riportano l'HbA1c in % o in mmol/mol. Si usa per screening e monitoraggio di diabete e prediabete. L'interpretazione e le decisioni terapeutiche spettano al medico.</p>"),
        Section(id="typical-diagnostic-ranges", level=2, heading="Intervalli diagnostici tipici",
            body_html="<p>I limiti <strong>variano per laboratorio e linee guida</strong>. In generale: <strong>Normale</strong> &lt;5,7%; <strong>Prediabete</strong> 5,7–6,4%; <strong>Diabete</strong> ≥6,5%. La classificazione è una <strong>decisione clinica e di laboratorio</strong> del medico. Non autodiagnosticarsi.</p>"),
        Section(id="hba1c-vs-fasting-vs-ogtt", level=2, heading="HbA1c vs glicemia a digiuno vs OGTT",
            body_html="<p><strong>HbA1c</strong>: media su ~2–3 mesi; di solito non serve digiuno. <strong>Glicemia a digiuno</strong>: valore singolo dopo digiuno. <strong>OGTT</strong>: glucosio prima e dopo bevanda standard; usato in gravidanza e in alcuni protocolli. Il medico sceglie i test in base alla situazione.</p>"),
        Section(id="estimated-average-glucose", level=2, heading="Glucosio medio stimato (eAG)",
            body_html="<p>Alcuni referti mostrano l'<strong>eAG</strong> (glucosio medio stimato) accanto all'HbA1c. È una <strong>stima</strong>, non una misura precisa, per orientarsi (es. in mg/dL). L'interpretazione spetta al medico.</p>"),
        Section(id="what-can-skew-hba1c", level=2, heading="Cosa può alterare l'HbA1c",
            body_html="<p>Anemia/carenza di ferro, varianti dell'emoglobina, gravidanza (spesso si preferiscono altri test), malattia renale, recente perdita di sangue o trasfusione, grave malattia epatica o alcuni farmaci. Il medico ne terrà conto.</p>"),
        Section(id="when-to-follow-up", level=2, heading="Quando rivolgersi al medico",
            body_html="<p>Consultare il medico se: HbA1c <strong>≥6,5%</strong>, <strong>aumento rapido</strong> o prediabete con fattori di rischio/sintomi, <strong>sintomi</strong> (sete, minzione frequente, perdita di peso, affaticamento, vista offuscata), <strong>gravidanza</strong> o condizioni che alterano l'HbA1c. Questo articolo non sostituisce la valutazione clinica.</p>"),
        Section(id="next-steps-clinician", level=2, heading="Prossimi passi che il medico può considerare",
            body_html="<p>Il medico può ripetere l'HbA1c, richiedere <strong>glicemia a digiuno</strong> o <strong>OGTT</strong>, controllare <strong>lipidi</strong>, <strong>funzione renale</strong>, <strong>albumina urinaria</strong> e <strong>pressione</strong>, e consigliare stile di vita (dieta, attività, sonno, peso) e eventuale terapia. La scelta è clinica.</p>"),
        Section(id="practical-lifestyle", level=2, heading="Stile di vita in pratica",
            body_html="<p>Principi generali (non sostituiscono il parere medico): <strong>Dieta</strong>: equilibrata, verdure e fibre, poco zucchero aggiunto. <strong>Attività</strong>: es. 150 min/settimana di attività moderata. <strong>Sonno</strong>: adeguato. <strong>Peso</strong>: se consigliato dal medico, modifiche graduali. Nessun farmaco o integratore consigliato qui—il medico indicherà eventuali cure.</p>"),
        Section(id="faq", level=2, heading="Domande frequenti",
            body_html="<p>Vedi sezione Domande frequenti sopra; l'interpretazione del valore spetta al medico.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer medico",
            body_html="<p><strong>Questo contenuto è solo informativo e non costituisce consulenza, diagnosi o trattamento medico.</strong> Discutere sempre risultati e sintomi con un operatore sanitario. Non modificare dieta, esercizio o farmaci solo in base a questo articolo.</p>"),
    ]


def _hba1c_sections_fr() -> List[Section]:
    return [
        Section(id="what-hba1c-measures", level=2, heading="Ce que mesure l'HbA1c",
            body_html="<p>L'HbA1c (hémoglobine glyquée A1c) reflète la <strong>glycémie moyenne sur environ 2–3 mois</strong>. Plus de glucose dans le sang sur cette période, plus la proportion d'hémoglobine glyquée. Les laboratoires rapportent l'HbA1c en % ou en mmol/mol. Utilisé pour le dépistage et le suivi du diabète et du prédiabète. L'interprétation et les décisions thérapeutiques relèvent du médecin.</p>"),
        Section(id="typical-diagnostic-ranges", level=2, heading="Seuils diagnostiques typiques",
            body_html="<p>Les seuils <strong>varient selon le laboratoire et les recommandations</strong>. En général : <strong>Normal</strong> &lt;5,7 % ; <strong>Prédiabète</strong> 5,7–6,4 % ; <strong>Diabète</strong> ≥6,5 %. La classification est une <strong>décision clinique et biologique</strong> du médecin. Ne pas s'auto-diagnostiquer.</p>"),
        Section(id="hba1c-vs-fasting-vs-ogtt", level=2, heading="HbA1c vs glycémie à jeun vs HGPO",
            body_html="<p><strong>HbA1c</strong> : moyenne sur ~2–3 mois ; en général pas besoin d'être à jeun pour l'HbA1c seul. <strong>Glycémie à jeun</strong> : valeur unique après jeûne. <strong>HGPO</strong> : glucose avant et après boisson standard ; utilisé en grossesse et dans certains protocoles. Le médecin choisit les examens selon la situation.</p>"),
        Section(id="estimated-average-glucose", level=2, heading="Glycémie moyenne estimée (eAG)",
            body_html="<p>Certains comptes-rendus affichent l'<strong>eAG</strong> (glycémie moyenne estimée) à côté de l'HbA1c. C'est une <strong>estimation</strong>, pas une mesure précise, pour illustrer (ex. en mg/dL). L'interprétation relève du médecin.</p>"),
        Section(id="what-can-skew-hba1c", level=2, heading="Ce qui peut fausser l'HbA1c",
            body_html="<p>Anémie/carence en fer, variants d'hémoglobine, grossesse (souvent d'autres tests préférés), maladie rénale, perte de sang ou transfusion récente, maladie hépatique sévère ou certains médicaments. Le médecin en tiendra compte.</p>"),
        Section(id="when-to-follow-up", level=2, heading="Quand consulter",
            body_html="<p>Consulter si : HbA1c <strong>≥6,5 %</strong>, <strong>augmentation rapide</strong> ou prédiabète avec facteurs de risque/symptômes, <strong>symptômes</strong> (soif, urines fréquentes, perte de poids, fatigue, vue floue), <strong>grossesse</strong> ou facteurs pouvant fausser l'HbA1c. Cet article ne remplace pas une évaluation clinique.</p>"),
        Section(id="next-steps-clinician", level=2, heading="Prochaines étapes possibles",
            body_html="<p>Le médecin peut répéter l'HbA1c, prescrire <strong>glycémie à jeun</strong> ou <strong>HGPO</strong>, contrôler <strong>lipides</strong>, <strong>fonction rénale</strong>, <strong>albumine urinaire</strong> et <strong>tension</strong>, et conseiller le mode de vie (alimentation, activité, sommeil, poids) et éventuellement un traitement. Le choix est clinique.</p>"),
        Section(id="practical-lifestyle", level=2, heading="Mode de vie en pratique",
            body_html="<p>Principes généraux (ne remplacent pas l'avis médical) : <strong>Alimentation</strong> : équilibrée, légumes et fibres, peu de sucres ajoutés. <strong>Activité</strong> : ex. 150 min/semaine d'activité modérée. <strong>Sommeil</strong> : suffisant. <strong>Poids</strong> : si le médecin le recommande, changements progressifs. Aucun médicament ou complément recommandé ici—le médecin indiquera les traitements.</p>"),
        Section(id="faq", level=2, heading="Questions fréquentes",
            body_html="<p>Voir section Questions fréquentes ci-dessus ; l'interprétation du résultat relève du médecin.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement médical",
            body_html="<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis, diagnostic ou traitement médical.</strong> Toujours discuter des résultats et symptômes avec un professionnel de santé. Ne pas modifier alimentation, exercice ou médicaments uniquement sur la base de cet article.</p>"),
    ]


_HBA1C_ARTICLE = _article_hba1c()


def _article_tsh() -> Article:
    """TSH (thyroid): what it is, high/low meaning, Free T4/T3, Hashimoto/Graves, when to see a doctor. en, de, it, fr."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/tsh-hero.png"
    cover_alt_text = {
        "en": "TSH thyroid test and monitoring dashboard — NoryaAI",
        "de": "TSH-Schilddrüsen-Test und Überwachung — NoryaAI",
        "it": "TSH thyroid test and monitoring dashboard — NoryaAI",
        "fr": "TSH thyroid test and monitoring dashboard — NoryaAI",
    }
    faq_qa = {
        "en": [
            {"question": "Why might my TSH be high with normal Free T4?", "answer": "This pattern can suggest subclinical hypothyroidism—the pituitary is raising TSH to keep thyroid hormone in range. It may be monitored or treated depending on your age, symptoms, and antibody status. Your clinician will interpret and advise."},
            {"question": "Can stress affect TSH?", "answer": "Acute illness, stress, or fasting can sometimes temporarily alter TSH. Results are best interpreted in context; your doctor may suggest repeating the test when you are stable if the result was borderline."},
            {"question": "Do I need to fast for a TSH test?", "answer": "Fasting is usually not required for TSH alone. If the same sample is used for other tests (e.g. lipids, glucose), your lab may ask you to fast. Follow the instructions given for your blood draw."},
            {"question": "How often should TSH be rechecked?", "answer": "Frequency depends on your situation—new diagnosis, medication adjustment, or stable treatment. Your doctor will recommend when to recheck (e.g. every 6–12 weeks after a change, or less often when stable)."},
            {"question": "What about TSH in pregnancy?", "answer": "Pregnancy-specific reference ranges for TSH are often used; targets can be stricter in the first trimester. If you are pregnant or planning pregnancy, your obstetrician or endocrinologist will guide testing and targets."},
            {"question": "Does biotin interfere with TSH results?", "answer": "High-dose biotin can interfere with some immunoassay methods and falsely lower TSH (or affect Free T4/Free T3). If you take biotin, tell your doctor and consider stopping it several days before thyroid blood tests, as advised by your lab or clinician."},
            {"question": "What is subclinical hypothyroidism or hyperthyroidism?", "answer": "Subclinical hypothyroidism usually means high TSH with Free T4 still in the normal range. Subclinical hyperthyroidism means low TSH with Free T4/Free T3 in the normal range. Whether to treat is a clinical decision based on your levels, symptoms, and risk factors."},
            {"question": "Can iodine supplements help?", "answer": "Iodine is needed for thyroid hormone production, but excess can worsen some thyroid conditions (e.g. trigger or worsen hyperthyroidism). Do not take iodine supplements without medical advice; your clinician can advise based on your diet and thyroid status."},
        ],
        "de": [
            {"question": "Warum ist mein TSH hoch bei normalem freiem T4?", "answer": "Das kann auf eine subklinische Hypothyreose hindeuten—die Hypophyse erhöht das TSH, um die Schilddrüsenhormone im Normbereich zu halten. Je nach Alter, Symptomen und Antikörperstatus wird überwacht oder behandelt. Ihr Arzt interpretiert und berät."},
            {"question": "Kann Stress das TSH beeinflussen?", "answer": "Akute Erkrankung, Stress oder Fasten können TSH vorübergehend verändern. Die Bewertung erfolgt im Kontext; bei Grenzwerten kann der Arzt eine Wiederholung in stabiler Phase empfehlen."},
            {"question": "Muss ich für TSH nüchtern sein?", "answer": "Für TSH allein ist Nüchternheit meist nicht nötig. Wird dasselbe Blut für andere Tests (z. B. Fette, Glukose) verwendet, kann das Labor Nüchternheit verlangen. Folgen Sie den Anweisungen."},
            {"question": "Wie oft soll TSH kontrolliert werden?", "answer": "Abhängig von Situation—Neudiagnose, Medikamentenanpassung oder stabile Therapie. Ihr Arzt empfiehlt den Kontrollzeitpunkt (z. B. alle 6–12 Wochen nach Änderung oder seltener bei Stabilität)."},
            {"question": "TSH in der Schwangerschaft?", "answer": "In der Schwangerschaft gelten oft eigene Referenzbereiche; die Ziele können im ersten Trimenon strenger sein. Bei bestehender oder geplanter Schwangerschaft berät Sie Ihr Gynäkologe oder Endokrinologe."},
            {"question": "Stört Biotin die TSH-Werte?", "answer": "Hochdosiertes Biotin kann manche Immunassays stören und TSH (oder fT4/fT3) fälschlich senken. Bei Biotin-Einnahme den Arzt informieren und ggf. einige Tage vor der Blutentnahme absetzen, wie Labor oder Arzt empfehlen."},
            {"question": "Was ist subklinische Hypo- oder Hyperthyreose?", "answer": "Subklinische Hypothyreose: TSH erhöht, fT4 noch normal. Subklinische Hyperthyreose: TSH erniedrigt, fT4/fT3 normal. Ob behandelt wird, entscheidet der Arzt anhand von Werten, Symptomen und Risiken."},
            {"question": "Helfen Jodpräparate?", "answer": "Jod wird für die Schilddrüsenhormonbildung benötigt; Überschuss kann manche Schilddrüsenerkrankungen verschlechtern. Jod nicht ohne ärztlichen Rat einnehmen—Ihr Arzt berät je nach Ernährung und Befund."},
        ],
        "it": [
            {"question": "Perché il TSH è alto con FT4 normale?", "answer": "Può indicare ipotiroidismo subclinico: l'ipofisi aumenta il TSH per mantenere gli ormoni tiroidei nella norma. Si può monitorare o trattare in base a età, sintomi e anticorpi. Il medico interpreta e consiglia."},
            {"question": "Lo stress può influire sul TSH?", "answer": "Malattia acuta, stress o digiuno a volte alterano temporaneamente il TSH. I risultati vanno interpretati nel contesto; il medico può suggerire di ripetere il test in condizioni stabili se il valore è borderline."},
            {"question": "Devo essere a digiuno per il TSH?", "answer": "Per il TSH da solo di solito non serve il digiuno. Se il prelievo è usato anche per altri esami (lipidi, glucosio), il laboratorio può richiedere il digiuno. Seguire le istruzioni."},
            {"question": "Quanto spesso ripetere il TSH?", "answer": "Dipende dalla situazione: nuova diagnosi, modifica della terapia o trattamento stabile. Il medico indicherà quando ripetere (es. ogni 6–12 settimane dopo una modifica, o meno spesso se stabile)."},
            {"question": "TSH in gravidanza?", "answer": "In gravidanza si usano spesso intervalli di riferimento specifici; i target possono essere più stringenti nel primo trimestre. In gravidanza o programmazione, ginecologo o endocrinologo guideranno i controlli."},
            {"question": "La biotina interferisce con il TSH?", "answer": "Alte dosi di biotina possono interferire con alcuni metodi e abbassare falsamente il TSH (o alterare fT4/fT3). Se assumi biotina, dillo al medico e valuta di sospenderla alcuni giorni prima del prelievo, come consigliato."},
            {"question": "Cos'è l'ipotiroidismo o ipertiroidismo subclinico?", "answer": "Ipotiroidismo subclinico: TSH alto con fT4 ancora nella norma. Ipertiroidismo subclinico: TSH basso con fT4/fT3 nella norma. Se trattare è una decisione clinica in base a livelli, sintomi e fattori di rischio."},
            {"question": "Gli integratori di iodio aiutano?", "answer": "Lo iodio serve per la produzione ormonale tiroidea, ma l'eccesso può peggiorare alcune patologie (es. scatenare o peggiorare ipertiroidismo). Non assumere iodio senza parere medico."},
        ],
        "fr": [
            {"question": "Pourquoi mon TSH est élevé avec une T4 libre normale ?", "answer": "Cela peut évoquer une hypothyroïdie fruste : l'hypophyse augmente le TSH pour maintenir les hormones dans la norme. Surveillance ou traitement selon âge, symptômes et anticorps. Votre médecin interprète et conseille."},
            {"question": "Le stress peut-il affecter le TSH ?", "answer": "Une maladie aiguë, le stress ou le jeûne peuvent parfois modifier temporairement le TSH. Les résultats sont interprétés en contexte ; le médecin peut proposer de répéter le dosage en période stable si le résultat est limite."},
            {"question": "Faut-il être à jeun pour le TSH ?", "answer": "Le jeûne n'est en général pas requis pour le TSH seul. Si le prélèvement sert aussi à d'autres dosages (lipides, glucose), le laboratoire peut demander le jeûne. Suivre les consignes."},
            {"question": "À quelle fréquence refaire le TSH ?", "answer": "Cela dépend de la situation : nouveau diagnostic, adaptation du traitement ou traitement stable. Votre médecin indiquera quand refaire le dosage (ex. toutes les 6–12 semaines après un changement, ou moins souvent si stable)."},
            {"question": "Et le TSH en grossesse ?", "answer": "En grossesse, des fourchettes de référence spécifiques sont souvent utilisées ; les cibles peuvent être plus strictes au premier trimestre. En cas de grossesse ou projet, votre gynécologue ou endocrinologue guidera les dosages."},
            {"question": "La biotine interfère-t-elle avec le TSH ?", "answer": "Les fortes doses de biotine peuvent fausser certains dosages immunologiques et abaisser à tort le TSH (ou modifier T4/T3 libres). Si vous prenez de la biotine, prévenez votre médecin et envisagez de l'arrêter quelques jours avant le prélèvement, selon les conseils du laboratoire ou du médecin."},
            {"question": "Qu'est-ce que l'hypo- ou l'hyperthyroïdie fruste ?", "answer": "Hypothyroïdie fruste : TSH élevé avec T4 libre encore normale. Hyperthyroïdie fruste : TSH bas avec T4/T3 libres normales. La décision de traiter est clinique, selon les valeurs, symptômes et facteurs de risque."},
            {"question": "Les compléments d'iode peuvent-ils aider ?", "answer": "L'iode est nécessaire à la production d'hormones thyroïdiennes, mais l'excès peut aggraver certaines affections (ex. déclencher ou aggraver une hyperthyroïdie). Ne pas prendre d'iode sans avis médical."},
        ],
    }
    return Article(
        id="tsh-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=12,
        cover_image=cover,
        cover_alt=cover_alt_text,
        faq_schema_qa=faq_qa,
        category={
            "en": "Thyroid & Hormones",
            "de": "Schilddrüse & Hormone",
            "it": "Tiroide e ormoni",
            "fr": "Thyroïde et hormones",
            "tr": "Tiroid ve Hormonlar",
            "es": "Tiroides y hormonas",
            "he": "תירואיד והורמונים",
            "hi": "थायरॉइड और हार्मोन",
            "ar": "الغدة الدرقية والهرمونات",
        },
        slugs={"en": "tsh-what-it-means", "de": "tsh-what-it-means", "it": "tsh-what-it-means", "fr": "tsh-what-it-means", "tr": "tsh-what-it-means", "es": "tsh-what-it-means", "he": "tsh-what-it-means", "hi": "tsh-what-it-means", "ar": "tsh-what-it-means"},
        titles={
            "en": "Thyroid Blood Test Explained: TSH, T3, T4 and What They Mean",
            "de": "Schilddrüsen-Bluttest erklärt: TSH, T3, T4 und was sie bedeuten",
            "it": "Esami della tiroide spiegati: TSH, T3, T4 e cosa significano",
            "fr": "Bilan thyroïdien expliqué : TSH, T3, T4 et ce qu'ils signifient",
            "tr": "Tiroid Kan Testi: TSH, T3, T4 Ne Anlama Gelir",
            "es": "Análisis tiroideo: TSH, T3, T4 y qué significan",
            "he": "בדיקת תירואיד: TSH, T3, T4 ומה הם אומרים",
            "hi": "थायरॉइड ब्लड टेस्ट: TSH, T3, T4 क्या मतलब",
            "ar": "تحليل الغدة الدرقية: TSH وT3 وT4 وماذا تعني",
        },
        subtitles={
            "en": "What TSH is, how it relates to Free T4 and Free T3, typical patterns, symptoms, causes, and when to follow up with a clinician.",
            "de": "Was TSH ist, Zusammenhang mit freiem T4 und T3, typische Muster, Symptome, Ursachen und wann Sie zum Arzt sollten.",
            "it": "Cosa è il TSH, rapporto con FT4 e FT3, pattern tipici, sintomi, cause e quando rivolgersi al medico.",
            "fr": "Ce qu'est le TSH, lien avec T4 et T3 libres, schémas typiques, symptômes, causes et quand consulter.",
            "tr": "TSH nedir, Serbest T4 ve T3 ile ilişkisi, tipik paternler ve ne zaman doktora gidilmeli.",
            "es": "Qué es el TSH, relación con T4 y T3 libre, patrones típicos y cuándo consultar.",
            "he": "מהו TSH, קשר ל-T4 ו-T3 חופשי ומתי לרופא.",
            "hi": "TSH क्या है, Free T4/T3 से संबंध और डॉक्टर से कब मिलें।",
            "ar": "ما هو TSH وعلاقته بـ T4 وT3 الحر ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "TSH reflects the pituitary signal to the thyroid. High or low TSH, together with Free T4 and Free T3, helps clinicians assess thyroid function. Interpretation and next steps are for your doctor.",
            "de": "TSH spiegelt das Hypophysen-Signal an die Schilddrüse. Hohes oder niedriges TSH zusammen mit fT4/fT3 hilft bei der Beurteilung. Die Einordnung übernimmt Ihr Arzt.",
            "it": "Il TSH riflette il segnale ipofisario alla tiroide. TSH alto o basso con FT4/FT3 aiuta a valutare la funzione tiroidea. L'interpretazione spetta al medico.",
            "fr": "Le TSH reflète le signal hypophysaire vers la thyroïde. Un TSH élevé ou bas avec T4/T3 libres aide à évaluer la fonction thyroïdienne. L'interprétation relève du médecin.",
            "tr": "TSH hipofizin tiroid sinyalini yansıtır. Yüksek veya düşük TSH, Serbest T4 ve T3 ile birlikte tiroid işlevini değerlendirmeye yardımcı olur. Yorum hekiminizindir.",
            "es": "El TSH refleja la señal hipofisaria a la tiroides. TSH alto o bajo con T4/T3 libre ayuda a valorar la función tiroidea. La interpretación la hace el médico.",
            "he": "TSH משקף את האות מההיפופיזה לתירואיד. TSH גבוה או נמוך עם T4/T3 חופשי עוזר להעריך את תפקוד התירואיד. הפרשנות אצל הרופא.",
            "hi": "TSH पिट्यूटरी से थायरॉइड सिग्नल दर्शाता है। ऊंचा या नीचा TSH, Free T4/T3 के साथ थायरॉइड फंक्शन समझने में मदद करता है। व्याख्या डॉक्टर करते हैं।",
            "ar": "TSH يعكس إشارة الغدة النخامية للدرقية. TSH مرتفع أو منخفض مع T4/T3 الحر يساعد في تقييم وظيفة الدرقية. التفسير يكون مع الطبيب.",
        },
        seo_titles={
            "en": "TSH Explained: How to Interpret High vs Low Thyroid Results | NoryaAI",
            "de": "TSH verstehen: Hohe vs. niedrige Werte richtig deuten | NoryaAI",
            "it": "TSH: come interpretare valori alti o bassi | NoryaAI",
            "fr": "TSH : interpréter un taux élevé ou bas | NoryaAI",
            "tr": "TSH: Yüksek ve Düşük Tiroid Sonuçları | NoryaAI",
            "es": "TSH: cómo interpretar resultados tiroideos | NoryaAI",
            "he": "TSH: איך לפרש תוצאות תירואיד | NoryaAI",
            "hi": "TSH: थायरॉइड रिज़ल्ट कैसे समझें | NoryaAI",
            "ar": "TSH: كيف تُفسَّر نتائج الغدة الدرقية | NoryaAI",
        },
        seo_descriptions={
            "en": "Understand TSH: what it is, link to Free T4 and Free T3, typical ranges, symptoms, Hashimoto/Graves, and when to see a clinician. Informational only.",
            "de": "TSH verstehen: Bedeutung, Zusammenhang mit fT4/fT3, typische Bereiche, Symptome und wann zum Arzt. Nur zur Information.",
            "it": "Capire il TSH: cos'è, rapporto con FT4/FT3, intervalli tipici, sintomi e quando rivolgersi al medico. Solo informativo.",
            "fr": "Comprendre le TSH : ce qu'il mesure, lien avec T4/T3 libres, seuils typiques, symptômes et quand consulter. À titre informatif.",
            "tr": "TSH: ne ölçer, Serbest T4/T3 ile ilişkisi, tipik aralıklar ve ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "Entiende TSH: qué mide, relación con T4/T3 libre y cuándo consultar. Solo informativo.",
            "he": "הבן TSH: מה מודד, קשר ל-T4/T3 חופשי ומתי לרופא. למידע בלבד.",
            "hi": "TSH समझें: क्या मापता है और डॉक्टर से कब मिलें। सूचनात्मक।",
            "ar": "افهم TSH: ماذا يقيس ومتى ترى الطبيب. للمعلومات فقط.",
        },
        sections_by_lang={
            "en": _tsh_sections_en(),
            "de": _tsh_sections_de(),
            "it": _tsh_sections_it(),
            "fr": _tsh_sections_fr(),
        },
    )


def _tsh_sections_en() -> List[Section]:
    return [
        Section(id="what-tsh-is", level=2, heading="What TSH is",
            body_html="<p>TSH (thyroid-stimulating hormone) is produced by the <strong>pituitary gland</strong> and acts as the main \"signal\" to the thyroid to make and release thyroid hormones (T4 and T3). When thyroid hormone levels are low, the pituitary releases more TSH; when high, TSH falls. <strong>TSH reflects the brain's attempt to keep thyroid hormone in the right range</strong>. It is one of the most common blood tests for thyroid function. Interpretation and diagnosis are for your clinician.</p>"),
        Section(id="tsh-free-t4-free-t3", level=2, heading="TSH + Free T4 + Free T3 together",
            body_html="<p>TSH is usually interpreted with <strong>Free T4 (FT4)</strong> and often <strong>Free T3 (FT3)</strong>. Typical patterns: <strong>High TSH + low FT4</strong> → primary hypothyroidism. <strong>Low TSH + high FT4/FT3</strong> → hyperthyroidism. <strong>High TSH, FT4 normal</strong> → subclinical hypothyroidism; <strong>Low TSH, FT4/FT3 normal</strong> → subclinical hyperthyroidism or non-thyroid illness. Borderline results should be discussed with your doctor.</p>"),
        Section(id="typical-ranges", level=2, heading="Typical reference ranges",
            body_html="<p>Reference ranges <strong>vary by laboratory and method</strong>. Many labs use TSH around 0.4–4.0 mU/L. <strong>In pregnancy</strong>, different (often stricter) TSH targets are used—your obstetrician or endocrinologist will advise. Do not self-interpret.</p>"),
        Section(id="symptoms", level=2, heading="Symptoms (non-specific)",
            body_html="<p>Possible <strong>hypothyroid</strong> symptoms: fatigue, weight gain, cold intolerance, constipation, dry skin. Possible <strong>hyperthyroid</strong> symptoms: palpitations, weight loss, heat intolerance, tremor, anxiety. All non-specific; discuss with your doctor.</p>"),
        Section(id="common-causes", level=2, heading="Common causes",
            body_html="<p>Common causes: <strong>Hashimoto's</strong> (autoimmune hypothyroidism), <strong>Graves'</strong> (autoimmune hyperthyroidism), <strong>thyroiditis</strong>, iodine deficiency or excess, <strong>medications</strong> (e.g. amiodarone, lithium), recent severe illness. Your doctor will consider history, antibodies (TPOAb, TgAb, TRAb), and sometimes imaging.</p>"),
        Section(id="when-to-contact", level=2, heading="When to contact a clinician",
            body_html="<p>See a doctor if: <strong>TSH very abnormal</strong> or changing quickly; <strong>pregnancy</strong> with thyroid concerns; <strong>heart symptoms</strong>; severe fatigue; <strong>rapid weight change</strong> or neck swelling (goiter); or known thyroid disease with changed symptoms. This article does not replace clinical assessment.</p>"),
        Section(id="next-tests", level=2, heading="Next tests a clinician may consider",
            body_html="<p>Your doctor may order: <strong>TPOAb, TgAb</strong> (Hashimoto's), <strong>TRAb</strong> (Graves'), <strong>thyroid ultrasound</strong>, repeat TSH/FT4/FT3, or ferritin/B12/vitamin D if relevant. Which tests are needed is a clinical decision.</p>"),
        Section(id="practical-tips", level=2, heading="Practical tips",
            body_html="<p><strong>Medication timing</strong>: If you take thyroid hormone (e.g. levothyroxine), take it as prescribed. Blood draws are often before the morning dose. <strong>Do not</strong> change or stop your dose on your own—any adjustment should be clinician-directed.</p>"),
        Section(id="faq", level=2, heading="Frequently asked questions",
            body_html="<p>See FAQ above; interpretation is for your clinician.</p>"),
        Section(id="disclaimer", level=2, heading="Medical disclaimer",
            body_html="<p><strong>This content is for information only and does not constitute medical advice, diagnosis, or treatment.</strong> Always discuss your results and symptoms with a qualified healthcare provider.</p>"),
    ]


def _tsh_sections_de() -> List[Section]:
    return [
        Section(id="what-tsh-is", level=2, heading="Was ist TSH?",
            body_html="<p>TSH wird von der <strong>Hypophyse</strong> gebildet und ist das zentrale „Signal“ an die Schilddrüse. Bei niedrigen Schilddrüsenhormonen steigt das TSH, bei hohen sinkt es. Die Einordnung obliegt dem Arzt.</p>"),
        Section(id="tsh-free-t4-free-t3", level=2, heading="TSH + freies T4 + freies T3",
            body_html="<p>Typische Muster: <strong>Hohes TSH + niedriges fT4</strong> → primäre Hypothyreose. <strong>Niedriges TSH + hohes fT4/fT3</strong> → Hyperthyreose. Grenzwerte mit dem Arzt besprechen.</p>"),
        Section(id="typical-ranges", level=2, heading="Typische Referenzbereiche",
            body_html="<p>Referenzbereiche variieren je nach Labor. In der Schwangerschaft gelten oft strengere Ziele. Immer mit dem Arzt besprechen.</p>"),
        Section(id="symptoms", level=2, heading="Symptome (unspezifisch)",
            body_html="<p>Unterfunktion: Müdigkeit, Gewichtszunahme, Kälteempfinden. Überfunktion: Herzrasen, Gewichtsverlust, Hitzeintoleranz, Zittern. Alle unspezifisch.</p>"),
        Section(id="common-causes", level=2, heading="Häufige Ursachen",
            body_html="<p>Hashimoto, Morbus Basedow/Graves, Thyreoiditis, Jod, Medikamente (Amiodaron, Lithium), schwere Erkrankung. Der Arzt berücksichtigt Antikörper und ggf. Bildgebung.</p>"),
        Section(id="when-to-contact", level=2, heading="Wann zum Arzt",
            body_html="<p>Bei stark abweichendem TSH, Schwangerschaft, Herzbeschwerden, starker Müdigkeit, schneller Gewichtsänderung oder Schwellung am Hals.</p>"),
        Section(id="next-tests", level=2, heading="Mögliche weitere Tests",
            body_html="<p>TPOAb, TgAb, TRAb, Schilddrüsen-Sonografie, Kontrolle TSH/fT4/fT3, ggf. Ferritin/B12/Vitamin D. Klinische Entscheidung.</p>"),
        Section(id="practical-tips", level=2, heading="Praktische Hinweise",
            body_html="<p>Schilddrüsenhormon wie verordnet einnehmen; Dosis nicht eigenmächtig ändern.</p>"),
        Section(id="faq", level=2, heading="Häufige Fragen",
            body_html="<p>Siehe FAQ oben.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
            body_html="<p><strong>Nur zur Information; ersetzt keine medizinische Beratung.</strong> Immer mit dem Arzt besprechen.</p>"),
    ]


def _tsh_sections_it() -> List[Section]:
    return [
        Section(id="what-tsh-is", level=2, heading="Cos'è il TSH",
            body_html="<p>Il TSH è prodotto dall'ipofisi e rappresenta il principale „segnale“ alla tiroide. L'interpretazione spetta al medico.</p>"),
        Section(id="tsh-free-t4-free-t3", level=2, heading="TSH + FT4 + FT3 insieme",
            body_html="<p>TSH alto + FT4 basso → ipotiroidismo primario. TSH basso + FT4/FT3 alti → ipertiroidismo. Valori borderline da discutere con il medico.</p>"),
        Section(id="typical-ranges", level=2, heading="Intervalli tipici",
            body_html="<p>I range variano per laboratorio. In gravidanza target più stringenti. Interpretazione con il medico.</p>"),
        Section(id="symptoms", level=2, heading="Sintomi (aspecifici)",
            body_html="<p>Ipo: affaticamento, aumento di peso, freddo. Iper: palpitazioni, dimagrimento, tremore, ansia. Tutti aspecifici.</p>"),
        Section(id="common-causes", level=2, heading="Cause comuni",
            body_html="<p>Hashimoto, Graves, tiroidite, iodio, farmaci (amiodarone, litio). Il medico considera anticorpi e imaging.</p>"),
        Section(id="when-to-contact", level=2, heading="Quando rivolgersi al medico",
            body_html="<p>TSH molto alterato, gravidanza, sintomi cardiaci, forte affaticamento, rapido cambio di peso o gonfiore al collo.</p>"),
        Section(id="next-tests", level=2, heading="Possibili esami",
            body_html="<p>TPOAb, TgAb, TRAb, ecografia tiroidea, ripetizione TSH/FT4/FT3. Scelta clinica.</p>"),
        Section(id="practical-tips", level=2, heading="Consigli pratici",
            body_html="<p>Ormone tiroideo come prescritto; non modificare la dose da soli.</p>"),
        Section(id="faq", level=2, heading="Domande frequenti",
            body_html="<p>Vedi FAQ sopra.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer medico",
            body_html="<p><strong>Solo informativo; non costituisce consulenza medica.</strong> Discutere con il medico.</p>"),
    ]


def _tsh_sections_fr() -> List[Section]:
    return [
        Section(id="what-tsh-is", level=2, heading="Ce qu'est le TSH",
            body_html="<p>La TSH est sécrétée par l'hypophyse et constitue le principal « signal » vers la thyroïde. L'interprétation relève du médecin.</p>"),
        Section(id="tsh-free-t4-free-t3", level=2, heading="TSH + T4 libre + T3 libre",
            body_html="<p>TSH élevée + T4 libre basse → hypothyroïdie primaire. TSH basse + T4/T3 libres élevées → hyperthyroïdie. Valeurs limites à discuter avec le médecin.</p>"),
        Section(id="typical-ranges", level=2, heading="Fourchettes typiques",
            body_html="<p>Les fourchettes varient selon le laboratoire. En grossesse, cibles plus strictes. Interprétation avec le médecin.</p>"),
        Section(id="symptoms", level=2, heading="Symptômes (non spécifiques)",
            body_html="<p>Hypo : fatigue, prise de poids, frilosité. Hyper : palpitations, perte de poids, tremblements, anxiété. Tous non spécifiques.</p>"),
        Section(id="common-causes", level=2, heading="Causes fréquentes",
            body_html="<p>Hashimoto, Basedow/Graves, thyroïdite, iode, médicaments (amiodarone, lithium). Le médecin considère anticorps et imagerie.</p>"),
        Section(id="when-to-contact", level=2, heading="Quand consulter",
            body_html="<p>TSH très anormale, grossesse, symptômes cardiaques, forte fatigue, changement de poids rapide ou gonflement du cou.</p>"),
        Section(id="next-tests", level=2, heading="Examens possibles",
            body_html="<p>TPOAb, TgAb, TRAb, échographie thyroïdienne, répétition TSH/T4/T3 libres. Choix clinique.</p>"),
        Section(id="practical-tips", level=2, heading="Conseils pratiques",
            body_html="<p>Hormone thyroïdienne comme prescrit ; ne pas modifier la dose soi-même.</p>"),
        Section(id="faq", level=2, heading="Questions fréquentes",
            body_html="<p>Voir FAQ ci-dessus.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement médical",
            body_html="<p><strong>À titre informatif uniquement ; ne constitue pas un avis médical.</strong> Toujours discuter avec le médecin.</p>"),
    ]


_TSH_ARTICLE = _article_tsh()


def _ldl_hdl_sections_en() -> List[Section]:
    return [
        Section(
            id="what-ldl-hdl-are",
            level=2,
            heading="What LDL and HDL are",
            body_html="""
<p>LDL (low-density lipoprotein) and HDL (high-density lipoprotein) are lipoproteins that carry cholesterol in the blood. <strong>LDL</strong> delivers cholesterol to tissues; in excess it can contribute to plaque in artery walls. <strong>HDL</strong> helps remove cholesterol from tissues and carries it back to the liver. In routine lipid panels, LDL is often labelled “bad” and HDL “good” cholesterol—useful shorthand, but interpretation depends on your full profile and risk factors. This overview is for information only; it does not replace a clinical assessment.</p>
""",
        ),
        Section(
            id="full-lipid-panel",
            level=2,
            heading="The full lipid panel: Total, LDL, HDL, Triglycerides",
            body_html="""
<p>A standard lipid panel usually includes:</p>
<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">
  <thead><tr class="bg-slate-50"><th class="border border-slate-200 px-3 py-2 text-left">Marker</th><th class="border border-slate-200 px-3 py-2 text-left">What it reflects</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>Total cholesterol</strong></td><td class="border border-slate-200 px-3 py-2">Sum of cholesterol in all lipoproteins (LDL + HDL + VLDL and other fractions).</td></tr>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>LDL cholesterol</strong></td><td class="border border-slate-200 px-3 py-2">Main carrier of cholesterol into tissues; primary target for risk reduction in many guidelines.</td></tr>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>HDL cholesterol</strong></td><td class="border border-slate-200 px-3 py-2">Carries cholesterol from tissues to the liver; higher levels are generally associated with lower cardiovascular risk.</td></tr>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>Triglycerides (TG)</strong></td><td class="border border-slate-200 px-3 py-2">Fats in the blood; high levels can increase cardiovascular and pancreatitis risk; often measured fasting.</td></tr>
  </tbody>
</table>
<p>LDL may be reported as calculated (e.g. Friedewald) or directly measured. Your clinician interprets these values in context.</p>
""",
        ),
        Section(
            id="non-hdl-cholesterol",
            level=2,
            heading="Non-HDL cholesterol explained",
            body_html="""
<p><strong>Non-HDL cholesterol</strong> is total cholesterol minus HDL (Non-HDL = Total − HDL). It includes LDL and all other atherogenic lipoproteins (e.g. VLDL, remnant particles). Guidelines often use it as a secondary or alternative target because it captures risk from non-LDL particles and does not depend on fasting. Your doctor may use either LDL or non-HDL (or both) to guide decisions; targets depend on your risk profile.</p>
""",
        ),
        Section(
            id="typical-targets",
            level=2,
            heading="Typical targets and reference ranges",
            body_html="""
<p>Targets and reference ranges <strong>vary by lab and guideline</strong> and depend on your cardiovascular risk (age, sex, smoking, blood pressure, diabetes, family history, etc.). The following are for general context only; your clinician sets your individual goals.</p>
<ul>
  <li><strong>HDL</strong>: Higher is generally better. Sex-specific cut-offs may apply (e.g. &gt;40 mg/dL men, &gt;50 mg/dL women in some guidelines). Very high HDL can sometimes be genetic and does not always mean lower risk.</li>
  <li><strong>LDL</strong>: Lower targets for higher-risk patients (e.g. &lt;100, &lt;70, or &lt;55 mg/dL depending on risk). No single “normal” applies to everyone.</li>
  <li><strong>Triglycerides</strong>: Fasting &lt;150 mg/dL is often used as “normal”; higher tiers (e.g. 150–199, 200–499, ≥500 mg/dL) may prompt lifestyle or medical follow-up. Non-fasting cut-offs differ; follow your lab’s and doctor’s guidance.</li>
</ul>
""",
        ),
        Section(
            id="what-raises-ldl-tg",
            level=2,
            heading="What can raise LDL or triglycerides or lower HDL",
            body_html="""
<p>Many factors influence lipid levels:</p>
<ul>
  <li><strong>Diet</strong>: Saturated and trans fats can raise LDL; excess calories and refined carbs can raise TG; very low fat may lower HDL.</li>
  <li><strong>Genetics</strong>: Familial hypercholesterolaemia and other inherited patterns can raise LDL or TG regardless of diet.</li>
  <li><strong>Medical conditions</strong>: Hypothyroidism, diabetes, kidney disease, obesity, and liver disease can affect lipids.</li>
  <li><strong>Alcohol</strong>: Moderate intake may raise HDL; excess can raise TG.</li>
  <li><strong>Medications</strong>: Some drugs (e.g. steroids, certain blood pressure or HIV drugs) can raise LDL or TG or lower HDL.</li>
  <li><strong>Inactivity</strong>: Sedentary lifestyle can lower HDL and contribute to higher TG.</li>
</ul>
<p>Your doctor can help identify relevant factors and next steps.</p>
""",
        ),
        Section(
            id="when-to-follow-up",
            level=2,
            heading="When to follow up with a clinician",
            body_html="""
<p>See a doctor or nurse for interpretation and next steps if:</p>
<ul>
  <li>Your <strong>LDL is very high</strong> or above the target suggested for your risk.</li>
  <li><strong>Triglycerides are very high</strong> (e.g. ≥500 mg/dL), which can increase pancreatitis risk.</li>
  <li>You have a <strong>family history of early heart disease</strong> or very high cholesterol.</li>
  <li>You have <strong>symptoms</strong> that could relate to heart or vascular disease (e.g. chest pain, shortness of breath).</li>
  <li>You have <strong>diabetes</strong>, <strong>high blood pressure</strong>, or other cardiovascular risk factors and need a lipid management plan.</li>
</ul>
<p>This article is for information only; it does not replace a clinical assessment.</p>
""",
        ),
        Section(
            id="next-tests-clinician",
            level=2,
            heading="Next tests a clinician may consider",
            body_html="""
<p>Depending on your results and risk, your doctor may consider:</p>
<ul>
  <li><strong>ApoB</strong>: Reflects the number of atherogenic particles; sometimes used alongside or instead of LDL.</li>
  <li><strong>Lp(a)</strong>: Genetically determined; high levels increase cardiovascular risk; one-time measurement often sufficient.</li>
  <li><strong>hs-CRP</strong>: Marker of inflammation; may be used in risk assessment.</li>
  <li><strong>HbA1c</strong>: To screen for or monitor diabetes.</li>
  <li><strong>TSH</strong>: To check thyroid function if lipids are abnormal.</li>
  <li><strong>Liver and kidney function</strong>: If medication or secondary causes are being considered.</li>
  <li><strong>Risk calculators</strong>: To estimate 10-year cardiovascular risk and guide targets.</li>
</ul>
<p>Which tests are ordered is a clinical decision made with you by your doctor.</p>
""",
        ),
        Section(
            id="practical-lifestyle",
            level=2,
            heading="Practical lifestyle overview",
            body_html="""
<p>General measures that often support healthy lipid levels (not a substitute for medical advice; no “cure” claims):</p>
<ul>
  <li><strong>Fibre</strong>: Adequate fibre from vegetables, fruits, and whole grains.</li>
  <li><strong>Unsaturated fats</strong>: Prefer sources such as olive oil, nuts, and oily fish; limit saturated and trans fats.</li>
  <li><strong>Activity</strong>: Regular physical activity can help raise HDL and lower TG; follow your doctor’s recommendations.</li>
  <li><strong>Weight</strong>: If your doctor has recommended weight management, gradual changes are usually more sustainable.</li>
  <li><strong>Smoking cessation</strong>: Improves HDL and overall cardiovascular risk.</li>
  <li><strong>Sleep</strong>: Adequate sleep supports general metabolic health.</li>
</ul>
""",
        ),
        Section(
            id="faq",
            level=2,
            heading="Frequently asked questions",
            body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Is high HDL always good?</h3>
<p>Generally higher HDL is associated with lower cardiovascular risk, but very high HDL can be genetic and not always protective. Some drugs that raise HDL have not been shown to reduce events. Your clinician interprets your level in context.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Why is my LDL high even with a good diet?</h3>
<p>Genetics (e.g. familial hypercholesterolaemia), hypothyroidism, diabetes, kidney disease, or certain medications can raise LDL despite a healthy diet. Your doctor can help identify causes and options.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Do I need to fast for a lipid panel?</h3>
<p>For LDL and total cholesterol, fasting (often 9–12 hours) is traditionally used; non-fasting panels are accepted in some guidelines. Triglycerides are most comparable when fasting. Follow your lab’s instructions.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What is non-HDL cholesterol?</h3>
<p>Non-HDL is total cholesterol minus HDL. It includes LDL and other atherogenic particles and is often used as an alternative or additional target in guidelines.</p>
<h3 class="text-base font-semibold mt-4 mb-1">How fast can lipids change?</h3>
<p>Lifestyle changes can shift lipids within weeks to months; medication effects vary. Your doctor will advise on when to recheck.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Triglycerides vs LDL—what’s the difference?</h3>
<p>LDL is the main cholesterol-carrying particle targeted for cardiovascular risk; triglycerides are a different type of blood fat. Both can be elevated and both matter for risk; management may address both.</p>
<h3 class="text-base font-semibold mt-4 mb-1">ApoB vs LDL—which matters?</h3>
<p>ApoB reflects the number of atherogenic particles; LDL cholesterol reflects the cholesterol in those particles. Guidelines may use one or both; your clinician can explain how they apply to you.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Should I get Lp(a) tested?</h3>
<p>Lp(a) is a genetically determined risk factor. Testing can be useful in people with family history of early heart disease or unclear risk. Your doctor can recommend whether and when to test.</p>
""",
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Medical disclaimer",
            body_html="""
<p><strong>This content is for information only and does not constitute medical advice, diagnosis, or treatment.</strong> Always discuss your results and any symptoms with a qualified healthcare provider. Do not start or change diet, exercise, or medication based solely on this article. If you have concerns about your health, seek professional medical care.</p>
""",
        ),
    ]


def _ldl_hdl_sections_de() -> List[Section]:
    return [
        Section(id="what-ldl-hdl-are", level=2, heading="Was LDL und HDL sind",
            body_html="<p>LDL (Low-Density Lipoprotein) und HDL (High-Density Lipoprotein) transportieren Cholesterin im Blut. <strong>LDL</strong> bringt Cholesterin in die Gewebe; im Übermaß kann es zur Ablagerung in Gefäßwänden beitragen. <strong>HDL</strong> transportiert Cholesterin aus den Geweben zurück zur Leber. Im Laborbericht wird LDL oft als „schlechtes“, HDL als „gutes“ Cholesterin bezeichnet—die Bewertung hängt vom Gesamtprofil und Ihren Risikofaktoren ab. Dieser Überblick dient nur der Information; er ersetzt keine ärztliche Beurteilung.</p>"),
        Section(id="full-lipid-panel", level=2, heading="Das vollständige Lipidprofil: Gesamt-, LDL-, HDL-Cholesterin, Triglyceride",
            body_html="<p>Ein Standard-Lipidprofil umfasst in der Regel: <strong>Gesamtcholesterin</strong> (Summe aus allen Lipoproteinen), <strong>LDL-Cholesterin</strong> (Hauptzielwert in vielen Leitlinien), <strong>HDL-Cholesterin</strong> (höhere Werte oft mit geringerem kardiovaskulärem Risiko verbunden), <strong>Triglyceride</strong> (Blutfette; hohe Werte können Risiko erhöhen; oft nüchtern gemessen). LDL kann berechnet (z. B. Friedewald) oder direkt gemessen werden. Die Bewertung übernimmt Ihr Arzt.</p>"),
        Section(id="non-hdl-cholesterol", level=2, heading="Non-HDL-Cholesterin erklärt",
            body_html="<p><strong>Non-HDL-Cholesterin</strong> = Gesamtcholesterin minus HDL. Es umfasst LDL und andere atherogene Lipoproteine (z. B. VLDL). In Leitlinien wird es oft als alternatives Ziel verwendet, da es unabhängig von der Nüchternheit ist. Ihr Arzt kann LDL und/oder Non-HDL zur Steuerung nutzen.</p>"),
        Section(id="typical-targets", level=2, heading="Typische Zielwerte und Referenzbereiche",
            body_html="<p>Zielwerte <strong>variieren je nach Labor und Leitlinie</strong> und hängen von Ihrem kardiovaskulären Risiko ab. <strong>HDL</strong>: Höher ist in der Regel besser (geschlechtsspezifische Grenzen möglich). <strong>LDL</strong>: Niedrigere Ziele bei höherem Risiko (z. B. &lt;100, &lt;70 oder &lt;55 mg/dL). <strong>Triglyceride</strong>: Nüchtern oft &lt;150 mg/dL als Orientierung; höhere Stufen können Nachsorge erfordern. Ihr Arzt legt Ihre individuellen Ziele fest.</p>"),
        Section(id="what-raises-ldl-tg", level=2, heading="Was LDL/Triglyceride erhöhen oder HDL senken kann",
            body_html="<p>Ernährung (gesättigte/Transfette, Überschuss an Kalorien/Kohlenhydraten), <strong>Genetik</strong> (z. B. familiäre Hypercholesterinämie), <strong>Erkrankungen</strong> (Schilddrüsenunterfunktion, Diabetes, Nieren- oder Lebererkrankung), <strong>Alkohol</strong>, <strong>Medikamente</strong>, <strong>Bewegungsmangel</strong>. Ihr Arzt kann relevante Faktoren einordnen.</p>"),
        Section(id="when-to-follow-up", level=2, heading="Wann Sie zum Arzt sollten",
            body_html="<p>Bitte zum Arzt, wenn: LDL deutlich erhöht oder über Ihrem Zielwert, <strong>Triglyceride sehr hoch</strong> (z. B. ≥500 mg/dL), <strong>familiäre Belastung</strong> mit früher Herzerkrankung, <strong>Symptome</strong> (z. B. Brustschmerzen, Atemnot), <strong>Diabetes</strong>, <strong>Bluthochdruck</strong> oder andere Risikofaktoren. Dieser Artikel ersetzt keine klinische Beurteilung.</p>"),
        Section(id="next-tests-clinician", level=2, heading="Weitere Tests, die der Arzt erwägen kann",
            body_html="<p>Je nach Befund: <strong>ApoB</strong>, <strong>Lp(a)</strong>, <strong>hs-CRP</strong>, <strong>HbA1c</strong>, <strong>TSH</strong>, Leber-/Nierenwerte, <strong>Risikorechner</strong>. Die Auswahl trifft der Arzt mit Ihnen.</p>"),
        Section(id="practical-lifestyle", level=2, heading="Praktischer Lebensstil-Überblick",
            body_html="<p>Allgemeine Maßnahmen (kein Ersatz für ärztlichen Rat): Ballaststoffe, ungesättigte Fette (Olivenöl, Nüsse, Fisch), <strong>Bewegung</strong>, ggf. Gewichtsmanagement, <strong>Raucherentwöhnung</strong>, ausreichend Schlaf.</p>"),
        Section(id="faq", level=2, heading="Häufige Fragen",
            body_html="<p>Siehe Abschnitt FAQ; die Bewertung Ihrer Werte erfolgt durch den Arzt.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
            body_html="<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung, Diagnose oder Behandlung.</strong> Besprechen Sie Ergebnisse und Beschwerden immer mit einem Arzt.</p>"),
    ]


def _ldl_hdl_sections_it() -> List[Section]:
    return [
        Section(id="what-ldl-hdl-are", level=2, heading="Cosa sono LDL e HDL",
            body_html="<p>LDL (lipoproteina a bassa densità) e HDL (lipoproteina ad alta densità) trasportano il colesterolo nel sangue. <strong>LDL</strong> porta il colesterolo ai tessuti; in eccesso può contribuire alla placca nelle arterie. <strong>HDL</strong> aiuta a rimuovere il colesterolo dai tessuti. Nel referto LDL è spesso definito colesterolo „cattivo“ e HDL „buono“—la valutazione dipende dal profilo completo e dai fattori di rischio. Solo a scopo informativo; non sostituisce la valutazione clinica.</p>"),
        Section(id="full-lipid-panel", level=2, heading="Il profilo lipidico completo: Totale, LDL, HDL, Trigliceridi",
            body_html="<p>Un profilo lipidico standard include: <strong>Colesterolo totale</strong>, <strong>LDL</strong> (obiettivo principale in molte linee guida), <strong>HDL</strong> (valori più alti spesso associati a minor rischio cardiovascolare), <strong>Trigliceridi</strong> (grassi nel sangue; alti valori possono aumentare il rischio; spesso a digiuno). L'interpretazione spetta al medico.</p>"),
        Section(id="non-hdl-cholesterol", level=2, heading="Colesterolo non-HDL spiegato",
            body_html="<p><strong>Non-HDL</strong> = colesterolo totale meno HDL. Include LDL e altre lipoproteine aterogene. Usato in alcune linee guida come obiettivo alternativo. Il medico può usare LDL e/o non-HDL.</p>"),
        Section(id="typical-targets", level=2, heading="Obiettivi e intervalli di riferimento tipici",
            body_html="<p>Gli obiettivi <strong>variano per laboratorio e linee guida</strong> e dipendono dal rischio cardiovascolare. <strong>HDL</strong>: più alto in genere meglio. <strong>LDL</strong>: target più bassi per pazienti a rischio più alto. <strong>Trigliceridi</strong>: a digiuno spesso &lt;150 mg/dL come riferimento. Il medico definisce i vostri obiettivi.</p>"),
        Section(id="what-raises-ldl-tg", level=2, heading="Cosa può aumentare LDL/TG o abbassare HDL",
            body_html="<p>Dieta (grassi saturi/trans, eccesso di calorie/carboidrati), <strong>genetica</strong>, <strong>ipotiroidismo</strong>, <strong>diabete</strong>, <strong>alcol</strong>, <strong>farmaci</strong>, <strong>sedentarietà</strong>. Il medico può identificare i fattori rilevanti.</p>"),
        Section(id="when-to-follow-up", level=2, heading="Quando rivolgersi al medico",
            body_html="<p>Consultare il medico se: LDL molto alto o sopra il target, <strong>trigliceridi molto alti</strong> (es. ≥500 mg/dL), <strong>storia familiare</strong> di malattia cardiaca precoce, <strong>sintomi</strong>, <strong>diabete</strong> o <strong>ipertensione</strong>. Questo articolo non sostituisce la valutazione clinica.</p>"),
        Section(id="next-tests-clinician", level=2, heading="Altri esami che il medico può considerare",
            body_html="<p>A seconda del quadro: <strong>ApoB</strong>, <strong>Lp(a)</strong>, <strong>hs-CRP</strong>, <strong>HbA1c</strong>, <strong>TSH</strong>, funzione epatica/renale, <strong>calcolatori di rischio</strong>. La scelta è clinica.</p>"),
        Section(id="practical-lifestyle", level=2, heading="Stile di vita in pratica",
            body_html="<p>Fibre, grassi insaturi, attività fisica, eventuale gestione del peso, <strong>smettere di fumare</strong>, sonno adeguato. Nessun consiglio al posto del medico.</p>"),
        Section(id="faq", level=2, heading="Domande frequenti",
            body_html="<p>Vedi sezione FAQ; l'interpretazione spetta al medico.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer medico",
            body_html="<p><strong>Questo contenuto è solo informativo e non costituisce consulenza, diagnosi o trattamento medico.</strong> Discutere sempre i risultati con un operatore sanitario.</p>"),
    ]


def _ldl_hdl_sections_fr() -> List[Section]:
    return [
        Section(id="what-ldl-hdl-are", level=2, heading="Ce que sont le LDL et le HDL",
            body_html="<p>Le LDL (lipoproteine de basse densité) et le HDL (lipoproteines de haute densité) transportent le cholestérol dans le sang. Le <strong>LDL</strong> apporte le cholestérol aux tissus ; en excès il peut contribuer à la plaque dans les artères. Le <strong>HDL</strong> aide à ramener le cholestérol vers le foie. Sur le bilan, le LDL est souvent qualifié de « mauvais » et le HDL de « bon » cholestérol—l’interprétation dépend du profil complet et des facteurs de risque. À titre informatif uniquement ; ne remplace pas une évaluation clinique.</p>"),
        Section(id="full-lipid-panel", level=2, heading="Le bilan lipidique complet : Total, LDL, HDL, Triglycérides",
            body_html="<p>Un bilan lipidique standard inclut : <strong>Cholestérol total</strong>, <strong>LDL</strong> (cible principale dans nombre de recommandations), <strong>HDL</strong> (niveaux plus élevés souvent associés à un risque cardiovasculaire moindre), <strong>Triglycérides</strong> (graisses sanguines ; des niveaux élevés peuvent augmenter le risque ; souvent à jeun). L’interprétation relève du médecin.</p>"),
        Section(id="non-hdl-cholesterol", level=2, heading="Le cholestérol non-HDL expliqué",
            body_html="<p>Le <strong>non-HDL</strong> = cholestérol total moins HDL. Il inclut le LDL et les autres lipoproteines athérogènes. Utilisé dans certaines recommandations comme cible alternative. Le médecin peut utiliser le LDL et/ou le non-HDL.</p>"),
        Section(id="typical-targets", level=2, heading="Objectifs et valeurs de référence typiques",
            body_html="<p>Les objectifs <strong>varient selon le laboratoire et les recommandations</strong> et dépendent du risque cardiovasculaire. <strong>HDL</strong> : plus élevé en général mieux. <strong>LDL</strong> : objectifs plus bas pour les patients à plus haut risque. <strong>Triglycérides</strong> : à jeun souvent &lt;150 mg/dL comme référence. Le médecin fixe vos objectifs.</p>"),
        Section(id="what-raises-ldl-tg", level=2, heading="Ce qui peut augmenter LDL/TG ou baisser le HDL",
            body_html="<p>Alimentation (graisses saturées/trans, excès de calories/glucides), <strong>génétique</strong>, <strong>hypothyroïdie</strong>, <strong>diabète</strong>, <strong>alcool</strong>, <strong>médicaments</strong>, <strong>sédentarité</strong>. Le médecin peut identifier les facteurs en cause.</p>"),
        Section(id="when-to-follow-up", level=2, heading="Quand consulter",
            body_html="<p>Consulter si : LDL très élevé ou au-dessus de la cible, <strong>triglycérides très élevés</strong> (ex. ≥500 mg/dL), <strong>antécédents familiaux</strong> de maladie cardiaque précoce, <strong>symptômes</strong>, <strong>diabète</strong> ou <strong>hypertension</strong>. Cet article ne remplace pas une évaluation clinique.</p>"),
        Section(id="next-tests-clinician", level=2, heading="Autres examens que le médecin peut envisager",
            body_html="<p>Selon le cas : <strong>ApoB</strong>, <strong>Lp(a)</strong>, <strong>hs-CRP</strong>, <strong>HbA1c</strong>, <strong>TSH</strong>, fonction hépatique/rénale, <strong>calculateurs de risque</strong>. Le choix est clinique.</p>"),
        Section(id="practical-lifestyle", level=2, heading="Mode de vie en pratique",
            body_html="<p>Fibres, graisses insaturées, activité physique, gestion du poids si indiquée, <strong>arrêt du tabac</strong>, sommeil suffisant. À titre informatif ; pas en remplacement de l’avis médical.</p>"),
        Section(id="faq", level=2, heading="Questions fréquentes",
            body_html="<p>Voir section FAQ ; l’interprétation relève du médecin.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement médical",
            body_html="<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis, diagnostic ou traitement médical.</strong> Toujours discuter des résultats avec un professionnel de santé.</p>"),
    ]


def _article_ldl_vs_hdl() -> Article:
    """LDL vs HDL: lipid panel interpretation. en, de, it, fr. Premium; no TR."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/ldl-hdl-hero.png"
    cover_alt_text = {
        "en": "LDL vs HDL cholesterol testing and lipid dashboard — NoryaAI",
        "de": "LDL- und HDL-Cholesterin: Lipidprofil und Überblick — NoryaAI",
        "it": "LDL vs HDL cholesterol testing and lipid dashboard — NoryaAI",
        "fr": "LDL vs HDL cholesterol testing and lipid dashboard — NoryaAI",
    }
    faq_qa = {
        "en": [
            {"question": "Is high HDL always good?", "answer": "Generally higher HDL is associated with lower cardiovascular risk, but very high HDL can be genetic and not always protective. Your clinician interprets your level in context."},
            {"question": "Why is my LDL high even with a good diet?", "answer": "Genetics (e.g. familial hypercholesterolaemia), hypothyroidism, diabetes, kidney disease, or certain medications can raise LDL despite a healthy diet. Your doctor can help identify causes and options."},
            {"question": "Do I need to fast for a lipid panel?", "answer": "For LDL and total cholesterol, fasting (often 9–12 hours) is traditionally used; non-fasting panels are accepted in some guidelines. Triglycerides are most comparable when fasting. Follow your lab's instructions."},
            {"question": "What is non-HDL cholesterol?", "answer": "Non-HDL is total cholesterol minus HDL. It includes LDL and other atherogenic particles and is often used as an alternative or additional target in guidelines."},
            {"question": "How fast can lipids change?", "answer": "Lifestyle changes can shift lipids within weeks to months; medication effects vary. Your doctor will advise on when to recheck."},
            {"question": "Triglycerides vs LDL—what's the difference?", "answer": "LDL is the main cholesterol-carrying particle targeted for cardiovascular risk; triglycerides are a different type of blood fat. Both can be elevated and both matter for risk; management may address both."},
            {"question": "ApoB vs LDL—which matters?", "answer": "ApoB reflects the number of atherogenic particles; LDL cholesterol reflects the cholesterol in those particles. Guidelines may use one or both; your clinician can explain how they apply to you."},
            {"question": "Should I get Lp(a) tested?", "answer": "Lp(a) is a genetically determined risk factor. Testing can be useful in people with family history of early heart disease or unclear risk. Your doctor can recommend whether and when to test."},
        ],
        "de": [
            {"question": "Ist hohes HDL immer gut?", "answer": "Höheres HDL ist oft mit geringerem kardiovaskulärem Risiko verbunden; sehr hohes HDL kann genetisch bedingt sein und nicht immer schützend. Die Einordnung übernimmt Ihr Arzt."},
            {"question": "Warum ist mein LDL trotz guter Ernährung hoch?", "answer": "Genetik (z. B. familiäre Hypercholesterinämie), Schilddrüsenunterfunktion, Diabetes, Nierenerkrankung oder bestimmte Medikamente können LDL erhöhen. Ihr Arzt kann Ursachen und Optionen klären."},
            {"question": "Muss ich für das Lipidprofil nüchtern sein?", "answer": "Für LDL und Gesamtcholesterin wird traditionell nüchtern (oft 9–12 h) gemessen; manche Leitlinien erlauben Nicht-Nüchtern-Profil. Triglyceride sind nüchtern am besten vergleichbar. Folgen Sie den Laboranweisungen."},
            {"question": "Was ist Non-HDL-Cholesterin?", "answer": "Non-HDL = Gesamtcholesterin minus HDL. Es umfasst LDL und andere atherogene Partikel und wird in Leitlinien oft als alternatives Ziel verwendet."},
            {"question": "Wie schnell können sich die Lipide ändern?", "answer": "Lebensstiländerungen können Lipide innerhalb von Wochen bis Monaten beeinflussen; Medikamenteneffekte variieren. Ihr Arzt empfiehlt, wann kontrolliert werden soll."},
            {"question": "Triglyceride vs. LDL—was ist der Unterschied?", "answer": "LDL ist die Hauptzielgröße für das kardiovaskuläre Risiko; Triglyceride sind eine andere Art von Blutfett. Beide können erhöht sein und beide sind für das Risiko relevant."},
            {"question": "ApoB vs. LDL—was zählt?", "answer": "ApoB spiegelt die Anzahl atherogener Partikel wider, LDL-Cholesterin den Cholesteringehalt. Leitlinien können eines oder beides nutzen; Ihr Arzt erläutert die Bedeutung für Sie."},
            {"question": "Soll ich Lp(a) testen lassen?", "answer": "Lp(a) ist ein genetisch bedingter Risikofaktor. Ein Test kann bei familiärer Belastung oder unklarem Risiko sinnvoll sein. Ihr Arzt empfiehlt, ob und wann getestet werden soll."},
        ],
        "it": [
            {"question": "L'HDL alto è sempre buono?", "answer": "In genere un HDL più alto è associato a minor rischio cardiovascolare; un HDL molto alto può essere genetico e non sempre protettivo. L'interpretazione spetta al medico."},
            {"question": "Perché ho l'LDL alto nonostante una buona dieta?", "answer": "Genetica (es. ipercolesterolemia familiare), ipotiroidismo, diabete, malattia renale o alcuni farmaci possono aumentare l'LDL. Il medico può aiutare a identificare cause e opzioni."},
            {"question": "Devo essere a digiuno per il profilo lipidico?", "answer": "Per LDL e colesterolo totale si usa tradizionalmente il digiuno (9–12 ore); alcune linee guida accettano il prelievo non a digiuno. I trigliceridi sono più confrontabili a digiuno. Seguire le istruzioni del laboratorio."},
            {"question": "Cos'è il colesterolo non-HDL?", "answer": "Il non-HDL è il colesterolo totale meno l'HDL. Include LDL e altre particelle aterogene ed è spesso usato come obiettivo alternativo nelle linee guida."},
            {"question": "Quanto velocemente possono cambiare i lipidi?", "answer": "Le modifiche dello stile di vita possono influire sui lipidi in settimane o mesi; l'effetto dei farmaci varia. Il medico consiglierà quando ripetere gli esami."},
            {"question": "Trigliceridi vs LDL—qual è la differenza?", "answer": "LDL è la principale particella portatrice di colesterolo target per il rischio cardiovascolare; i trigliceridi sono un altro tipo di grasso nel sangue. Entrambi possono essere elevati e contano per il rischio."},
            {"question": "ApoB vs LDL—cosa conta?", "answer": "L'ApoB riflette il numero di particelle aterogene; il colesterolo LDL riflette il colesterolo in quelle particelle. Le linee guida possono usare uno o entrambi; il medico può spiegare come si applicano a voi."},
            {"question": "Dovrei fare il test per Lp(a)?", "answer": "Lp(a) è un fattore di rischio genetico. Il test può essere utile in caso di familiarità per malattia cardiaca precoce o rischio non chiaro. Il medico può raccomandare se e quando testare."},
        ],
        "fr": [
            {"question": "Un HDL élevé est-il toujours bon ?", "answer": "En général un HDL plus élevé est associé à un risque cardiovasculaire moindre ; un HDL très élevé peut être génétique et pas toujours protecteur. L'interprétation relève du médecin."},
            {"question": "Pourquoi mon LDL est-il élevé malgré une bonne alimentation ?", "answer": "La génétique (ex. hypercholestérolémie familiale), l'hypothyroïdie, le diabète, une maladie rénale ou certains médicaments peuvent augmenter le LDL. Votre médecin peut aider à identifier les causes et options."},
            {"question": "Faut-il être à jeun pour le bilan lipidique ?", "answer": "Pour le LDL et le cholestérol total, le jeûne (souvent 9–12 h) est traditionnellement utilisé ; certains protocoles acceptent le prélèvement non à jeun. Les triglycérides sont plus comparables à jeun. Suivez les consignes du laboratoire."},
            {"question": "Qu'est-ce que le cholestérol non-HDL ?", "answer": "Le non-HDL = cholestérol total moins HDL. Il inclut le LDL et les autres particules athérogènes et est souvent utilisé comme objectif alternatif dans les recommandations."},
            {"question": "À quelle vitesse les lipides peuvent-ils changer ?", "answer": "Les changements d'hygiène de vie peuvent modifier les lipides en quelques semaines à mois ; l'effet des médicaments varie. Votre médecin indiquera quand refaire un contrôle."},
            {"question": "Triglycérides vs LDL—quelle différence ?", "answer": "Le LDL est la principale cible pour le risque cardiovasculaire ; les triglycérides sont un autre type de graisse sanguine. Les deux peuvent être élevés et comptent pour le risque."},
            {"question": "ApoB vs LDL—lequel compte ?", "answer": "L'ApoB reflète le nombre de particules athérogènes ; le cholestérol LDL reflète le cholestérol dans ces particules. Les recommandations peuvent utiliser l'un ou les deux ; votre médecin peut expliquer comment ils s'appliquent à vous."},
            {"question": "Faut-il faire doser le Lp(a) ?", "answer": "Le Lp(a) est un facteur de risque génétique. Le dosage peut être utile en cas d'antécédents familiaux de maladie cardiaque précoce ou de risque peu clair. Votre médecin peut recommander si et quand doser."},
        ],
    }
    return Article(
        id="ldl-vs-hdl-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=10,
        cover_image=cover,
        cover_alt=cover_alt_text,
        faq_schema_qa=faq_qa,
        category={
            "en": "Heart Health & Lipids",
            "de": "Herzgesundheit & Lipide",
            "it": "Salute cardiaca e lipidi",
            "fr": "Santé cardiaque et lipides",
            "tr": "Kalp Sağlığı ve Lipitler",
            "es": "Salud cardíaca y lípidos",
            "he": "בריאות לב וליפידים",
            "hi": "हृदय स्वास्थ्य और लिपिड",
            "ar": "صحة القلب والدهون",
        },
        slugs={
            "en": "ldl-vs-hdl-what-it-means",
            "de": "ldl-vs-hdl-what-it-means",
            "it": "ldl-vs-hdl-what-it-means",
            "fr": "ldl-vs-hdl-what-it-means",
            "tr": "ldl-vs-hdl-what-it-means",
            "es": "ldl-vs-hdl-what-it-means",
            "he": "ldl-vs-hdl-what-it-means",
            "hi": "ldl-vs-hdl-what-it-means",
            "ar": "ldl-vs-hdl-what-it-means",
        },
        titles={
            "en": "Cholesterol Blood Test Explained: How to Read Your Lipid Panel",
            "de": "Cholesterin-Bluttest erklärt: So lesen Sie Ihr Lipidprofil",
            "it": "Esami del colesterolo spiegati: come leggere il profilo lipidico",
            "fr": "Bilan cholestérol expliqué : comment lire votre bilan lipidique",
            "tr": "Kolesterol Kan Testi: Lipid Paneli Nasıl Okunur",
            "es": "Análisis de colesterol: cómo leer tu perfil lipídico",
            "he": "בדיקת כולסטרול: איך לקרוא את פרופיל השומנים",
            "hi": "कोलेस्ट्रॉल ब्लड टेस्ट: लिपिड पैनल कैसे पढ़ें",
            "ar": "تحليل الكوليسترول: كيف تقرأ لوحة الدهون",
        },
        subtitles={
            "en": "What LDL and HDL mean, how to interpret your lipid panel, non-HDL and targets, and when to follow up with a clinician.",
            "de": "Was LDL und HDL bedeuten, wie Sie Ihr Lipidprofil einordnen, Non-HDL und Zielwerte, wann Sie zum Arzt sollten.",
            "it": "Cosa significano LDL e HDL, come interpretare il profilo lipidico, non-HDL e obiettivi, quando rivolgersi al medico.",
            "fr": "Ce que signifient LDL et HDL, comment interpréter votre bilan lipidique, non-HDL et objectifs, quand consulter.",
            "tr": "LDL ve HDL ne anlama gelir, lipid paneli nasıl yorumlanır ve ne zaman doktora gidilmeli.",
            "es": "Qué significan LDL y HDL, cómo interpretar tu perfil lipídico y cuándo consultar.",
            "he": "מה אומרים LDL ו-HDL, איך לקרוא את פרופיל השומנים ומתי לרופא.",
            "hi": "LDL और HDL क्या मतलब, लिपिड पैनल कैसे समझें और डॉक्टर से कब मिलें।",
            "ar": "ماذا يعني LDL وHDL وكيف تقرأ لوحة الدهون ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "Understand LDL vs HDL, the full lipid panel, non-HDL cholesterol, typical targets, and when to see a doctor. Informational only.",
            "de": "LDL vs. HDL verstehen, vollständiges Lipidprofil, Non-HDL, typische Ziele und wann zum Arzt. Nur zur Information.",
            "it": "Capire LDL vs HDL, profilo lipidico completo, colesterolo non-HDL, obiettivi tipici e quando rivolgersi al medico. Solo informativo.",
            "fr": "Comprendre LDL vs HDL, bilan lipidique complet, cholestérol non-HDL, objectifs typiques et quand consulter. À titre informatif uniquement.",
            "tr": "LDL ve HDL, lipid paneli ve non-HDL hedeflerini anlayın; ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "Entiende LDL vs HDL, perfil lipídico y cuándo consultar. Solo informativo.",
            "he": "הבן LDL vs HDL, פרופיל שומנים ומתי לרופא. למידע בלבד.",
            "hi": "LDL vs HDL, लिपिड पैनल समझें और डॉक्टर से कब मिलें। सूचनात्मक।",
            "ar": "افهم LDL وHDL ولوحة الدهون ومتى ترى الطبيب. للمعلومات فقط.",
        },
        seo_titles={
            "en": "LDL vs HDL Cholesterol: How to Read Your Lipid Panel | NoryaAI",
            "de": "LDL vs HDL: Lipidprofil richtig verstehen | NoryaAI",
            "it": "LDL e HDL: come leggere il profilo lipidico | NoryaAI",
            "fr": "LDL et HDL : comprendre votre bilan lipidique | NoryaAI",
            "tr": "LDL ve HDL: Lipid Paneli Nasıl Okunur | NoryaAI",
            "es": "LDL vs HDL: cómo leer tu perfil lipídico | NoryaAI",
            "he": "LDL vs HDL: איך לקרוא את פרופיל השומנים | NoryaAI",
            "hi": "LDL vs HDL: लिपिड पैनल कैसे पढ़ें | NoryaAI",
            "ar": "LDL وHDL: كيف تقرأ لوحة الدهون | NoryaAI",
        },
        seo_descriptions={
            "en": "LDL vs HDL explained: how to read your lipid panel, what non-HDL means, typical targets, and when to follow up with a clinician. Informational only.",
            "de": "LDL vs. HDL: Lipidprofil verstehen, Non-HDL-Cholesterin, typische Zielwerte und wann Sie zum Arzt sollten. Nur zur Information, keine Diagnose.",
            "it": "LDL e HDL: come leggere il profilo lipidico, colesterolo non-HDL, obiettivi tipici e quando rivolgersi al medico. Solo informativo.",
            "fr": "LDL et HDL : comment lire votre bilan lipidique, cholestérol non-HDL, objectifs typiques et quand consulter. À titre informatif uniquement.",
            "tr": "LDL ve HDL: lipid paneli nasıl okunur, non-HDL ne demek ve ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "LDL vs HDL: cómo leer tu perfil lipídico, qué es el no-HDL y cuándo consultar. Solo informativo.",
            "he": "LDL vs HDL: איך לקרוא את פרופיל השומנים ומתי לרופא. למידע בלבד.",
            "hi": "LDL vs HDL: लिपिड पैनल कैसे पढ़ें और डॉक्टर से कब मिलें। सूचनात्मक।",
            "ar": "LDL وHDL: كيف تقرأ لوحة الدهون ومتى ترى الطبيب. للمعلومات فقط.",
        },
        sections_by_lang={
            "en": _ldl_hdl_sections_en(),
            "de": _ldl_hdl_sections_de(),
            "it": _ldl_hdl_sections_it(),
            "fr": _ldl_hdl_sections_fr(),
        },
    )


_LDL_HDL_ARTICLE = _article_ldl_vs_hdl()


def _article_creatinine_egfr() -> Article:
    """Creatinine & eGFR: kidney function results, categories, confounders, when to follow up. en, de, it, fr."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/creatinine-egfr-hero.png"
    cover_alt_text = {
        "en": "Creatinine test and eGFR kidney function dashboard — NoryaAI",
        "de": "Kreatinin und eGFR: Nierenfunktion im Überblick — NoryaAI",
        "it": "Creatinine test and eGFR kidney function dashboard — NoryaAI",
        "fr": "Creatinine test and eGFR kidney function dashboard — NoryaAI",
    }
    faq_qa = {
        "en": [
            {"question": "Can eGFR improve?", "answer": "eGFR can sometimes improve with treatment of reversible causes (e.g. dehydration, certain medications), good blood pressure and diabetes control, and lifestyle measures. How much it can improve depends on the cause and your situation. Your clinician will interpret your results and advise on follow-up."},
            {"question": "Do I need fasting for creatinine or eGFR?", "answer": "Fasting is usually not required for creatinine or eGFR. If the same blood draw is used for glucose or lipids, your lab may ask you to fast. Follow the instructions given for your test."},
            {"question": "Why is my creatinine high after a workout?", "answer": "Intense or prolonged exercise can temporarily raise creatinine because it is a byproduct of muscle metabolism. Dehydration can also raise it. If your level is only slightly high and you were dehydrated or had recent heavy exercise, your doctor may suggest repeating the test after rest and adequate hydration."},
            {"question": "What is urine ACR?", "answer": "Urine ACR (albumin-to-creatinine ratio) measures albumin in a urine sample relative to creatinine. It is used to detect kidney damage (e.g. diabetic kidney disease) and is often part of kidney and cardiovascular risk assessment. Your clinician can explain whether this test is appropriate for you."},
            {"question": "Does creatine supplement affect my labs?", "answer": "Creatine supplements can increase blood creatinine levels because creatine is converted to creatinine in the body. This may not reflect true kidney dysfunction. If you take creatine, tell your doctor so they can interpret your results in context; they may suggest temporarily stopping the supplement before a repeat test."},
            {"question": "What eGFR level is concerning?", "answer": "Guidelines often flag eGFR below 60 as potentially indicating reduced kidney function; below 30 is moderate to severe, and below 15 is in the kidney failure range and needs urgent medical care. Exact interpretation depends on your age, other markers, and clinical context. Your doctor will explain what your result means for you."},
            {"question": "How often should kidney function be rechecked?", "answer": "Frequency depends on your situation—e.g. known kidney disease, diabetes, hypertension, or medication that affects the kidneys. Your doctor will recommend how often to recheck (e.g. every 3–12 months or more often if adjusting treatment)."},
            {"question": "What about age and eGFR?", "answer": "eGFR formulas often include age; older adults may have lower eGFR that is still considered acceptable in the absence of other kidney damage. A single number must be interpreted with your age, other tests (e.g. urine ACR), and clinical picture. Your clinician will explain what is appropriate for you."},
        ],
        "de": [
            {"question": "Kann sich der eGFR verbessern?", "answer": "Der eGFR kann sich bei behandelbaren Ursachen (z. B. Dehydratation, bestimmte Medikamente), gut eingestelltem Blutdruck und Diabetes sowie Lebensstilmaßnahmen manchmal verbessern. Das Ausmaß hängt von der Ursache ab. Ihr Arzt interpretiert die Werte und empfiehlt die Kontrolle."},
            {"question": "Muss ich für Kreatinin/eGFR nüchtern sein?", "answer": "Für Kreatinin und eGFR ist in der Regel kein Nüchtern nötig. Wird dasselbe Blut für Glukose oder Fette verwendet, kann das Labor Nüchternheit verlangen. Folgen Sie den Anweisungen."},
            {"question": "Warum ist mein Kreatinin nach dem Training hoch?", "answer": "Intensiver oder längerer Sport kann Kreatinin vorübergehend erhöhen (Stoffwechselprodukt der Muskeln). Auch Dehydratation kann den Wert anheben. Bei nur leicht erhöhtem Wert und kürzlicher Anstrengung/Flüssigkeitsmangel kann der Arzt eine Wiederholung nach Erholung und ausreichend Trinken empfehlen."},
            {"question": "Was ist der Urin-ACR?", "answer": "Der Urin-ACR (Albumin-Kreatinin-Quotient) misst Albumin im Urin relativ zu Kreatinin. Er dient zur Erkennung von Nierenschäden (z. B. diabetische Nephropathie) und ist oft Teil der Nieren- und kardiovaskulären Risikobewertung. Ihr Arzt kann sagen, ob der Test für Sie sinnvoll ist."},
            {"question": "Beeinflusst Kreatin-Supplement meine Werte?", "answer": "Kreatin-Supplemente können das Blutkreatinin erhöhen, da Kreatin im Körper zu Kreatinin umgebaut wird. Das muss keine echte Nierenfunktionsstörung bedeuten. Wenn Sie Kreatin einnehmen, sagen Sie es dem Arzt; ggf. wird eine Wiederholung nach Absetzen empfohlen."},
            {"question": "Ab welchem eGFR-Wert wird es bedenklich?", "answer": "Leitlinien sehen oft eGFR unter 60 als Hinweis auf eingeschränkte Nierenfunktion; unter 30 als mittel bis schwer, unter 15 im Bereich Nierenversagen mit dringender ärztlicher Betreuung. Die Einordnung hängt von Alter, weiteren Befunden und Kontext ab. Ihr Arzt erklärt Ihre Werte."},
            {"question": "Wie oft soll die Nierenfunktion kontrolliert werden?", "answer": "Die Häufigkeit hängt von Ihrer Situation ab (z. B. bekannte Nierenerkrankung, Diabetes, Bluthochdruck, nierenschädliche Medikamente). Ihr Arzt empfiehlt den Kontrollrhythmus (z. B. alle 3–12 Monate)."},
            {"question": "Was bedeutet das Alter für den eGFR?", "answer": "eGFR-Formeln berücksichtigen oft das Alter; bei Älteren kann ein niedrigerer eGFR noch akzeptabel sein, wenn keine anderen Nierenschäden vorliegen. Die Bewertung erfolgt mit Alter, weiteren Tests (z. B. Urin-ACR) und Klinik. Ihr Arzt erläutert das für Sie."},
        ],
        "it": [
            {"question": "L'eGFR può migliorare?", "answer": "L'eGFR a volte può migliorare con il trattamento di cause reversibili (es. disidratazione, alcuni farmaci), buon controllo di pressione e diabete e stile di vita. Quanto migliora dipende dalla causa. Il medico interpreterà i risultati e consiglierà i controlli."},
            {"question": "Devo essere a digiuno per creatinina o eGFR?", "answer": "Per creatinina ed eGFR di solito non serve il digiuno. Se il prelievo è usato anche per glicemia o lipidi, il laboratorio può richiedere il digiuno. Seguite le istruzioni del laboratorio."},
            {"question": "Perché la creatinina è alta dopo l'allenamento?", "answer": "Esercizio intenso o prolungato può aumentare temporaneamente la creatinina (è un prodotto del metabolismo muscolare). Anche la disidratazione può alzarla. Se il valore è solo lievemente alto e eri disidratato o hai fatto sforzo recente, il medico può consigliare di ripetere il test dopo riposo e idratazione."},
            {"question": "Cos'è l'ACR urinario?", "answer": "L'ACR urinario (rapporto albumina/creatinina) misura l'albumina nelle urine rispetto alla creatinina. Si usa per rilevare danno renale (es. nefropatia diabetica) ed è spesso parte della valutazione del rischio renale e cardiovascolare. Il medico può spiegare se il test è indicato per voi."},
            {"question": "Gli integratori di creatina influenzano gli esami?", "answer": "Gli integratori di creatina possono aumentare la creatinina nel sangue perché la creatina viene convertita in creatinina nell'organismo. Questo può non riflettere una vera disfunzione renale. Se assumete creatina, ditelo al medico; potrebbe suggerire di sospenderla prima di un controllo."},
            {"question": "Quale valore di eGFR è preoccupante?", "answer": "Le linee guida spesso considerano eGFR sotto 60 come possibile riduzione della funzione renale; sotto 30 da moderata a severa, sotto 15 in ambito di insufficienza renale con necessità di cure urgenti. L'interpretazione dipende da età, altri marker e contesto. Il medico spiegherà il vostro risultato."},
            {"question": "Con quale frequenza controllare la funzione renale?", "answer": "La frequenza dipende dalla situazione (es. malattia renale nota, diabete, ipertensione, farmaci che influenzano i reni). Il medico consiglierà quando ripetere gli esami (es. ogni 3–12 mesi)."},
            {"question": "Che ruolo ha l'età nell'eGFR?", "answer": "Le formule eGFR spesso includono l'età; negli anziani un eGFR più basso può essere ancora accettabile in assenza di altri danni renali. Il singolo valore va interpretato con età, altri esami (es. ACR urinario) e quadro clinico. Il medico spiegherà cosa è appropriato per voi."},
        ],
        "fr": [
            {"question": "L'eGFR peut-il s'améliorer ?", "answer": "L'eGFR peut parfois s'améliorer avec le traitement de causes réversibles (déshydratation, certains médicaments), un bon contrôle tensionnel et du diabète, et des mesures d'hygiène de vie. L'ampleur dépend de la cause. Votre médecin interprétera les résultats et conseillera le suivi."},
            {"question": "Faut-il être à jeun pour la créatinine ou l'eGFR ?", "answer": "Le jeûne n'est en général pas nécessaire pour la créatinine ou l'eGFR. Si le prélèvement sert aussi à la glycémie ou aux lipides, le laboratoire peut demander le jeûne. Suivez les consignes du laboratoire."},
            {"question": "Pourquoi ma créatinine est-elle élevée après l'entraînement ?", "answer": "Un exercice intense ou prolongé peut augmenter temporairement la créatinine (produit du métabolisme musculaire). La déshydratation aussi. Si le taux est légèrement élevé et que vous étiez déshydraté ou avez beaucoup sollicité vos muscles, le médecin peut proposer de répéter le dosage après repos et réhydratation."},
            {"question": "Qu'est-ce que l'ACR urinaire ?", "answer": "L'ACR urinaire (rapport albumine/créatinine) mesure l'albumine dans les urines par rapport à la créatinine. Il sert à détecter un atteinte rénale (ex. néphropathie diabétique) et fait souvent partie du bilan rénal et cardiovasculaire. Votre médecin peut indiquer si ce dosage est pertinent pour vous."},
            {"question": "La créatine en complément affecte-t-elle mes analyses ?", "answer": "Les compléments de créatine peuvent augmenter la créatinine sanguine car la créatine est convertie en créatinine dans l'organisme. Cela ne reflète pas forcément une vraie atteinte rénale. Si vous prenez de la créatine, indiquez-le à votre médecin ; il pourra proposer d'arrêter temporairement avant un nouveau dosage."},
            {"question": "À partir de quel eGFR faut-il s'inquiéter ?", "answer": "Les recommandations considèrent souvent un eGFR inférieur à 60 comme possible réduction de la fonction rénale ; en dessous de 30 comme modérée à sévère, en dessous de 15 comme insuffisance rénale nécessitant une prise en charge urgente. L'interprétation dépend de l'âge, d'autres marqueurs et du contexte. Votre médecin vous expliquera votre résultat."},
            {"question": "À quelle fréquence contrôler la fonction rénale ?", "answer": "La fréquence dépend de votre situation (maladie rénale connue, diabète, hypertension, médicaments néphrotoxiques). Votre médecin recommandera la fréquence des contrôles (ex. tous les 3–12 mois)."},
            {"question": "Qu'en est-il de l'âge et de l'eGFR ?", "answer": "Les formules d'eGFR incluent souvent l'âge ; chez les personnes âgées, un eGFR plus bas peut rester acceptable en l'absence d'autres atteintes rénales. Le chiffre doit être interprété avec l'âge, d'autres examens (ex. ACR urinaire) et le tableau clinique. Votre médecin vous expliquera ce qui est adapté à votre cas."},
        ],
    }
    return Article(
        id="creatinine-egfr-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=10,
        cover_image=cover,
        cover_alt=cover_alt_text,
        faq_schema_qa=faq_qa,
        category={
            "en": "Kidney & Metabolic Health",
            "de": "Nieren- & Stoffwechselgesundheit",
            "it": "Reni e salute metabolica",
            "fr": "Reins et santé métabolique",
            "tr": "Böbrek ve Metabolik Sağlık",
            "es": "Riñón y salud metabólica",
            "he": "כליות ובריאות מטבולית",
            "hi": "किडनी और मेटाबॉलिक स्वास्थ्य",
            "ar": "الكلى والصحة الأيضية",
        },
        slugs={
            "en": "creatinine-egfr-what-it-means",
            "de": "creatinine-egfr-what-it-means",
            "it": "creatinine-egfr-what-it-means",
            "fr": "creatinine-egfr-what-it-means",
            "tr": "creatinine-egfr-what-it-means",
            "es": "creatinine-egfr-what-it-means",
            "he": "creatinine-egfr-what-it-means",
            "hi": "creatinine-egfr-what-it-means",
            "ar": "creatinine-egfr-what-it-means",
        },
        titles={
            "en": "Creatinine & eGFR Explained: Reading Kidney Function Results",
            "de": "Kreatinin & eGFR verstehen: Nierenwerte richtig deuten",
            "it": "Creatinina ed eGFR: come interpretare la funzione renale",
            "fr": "Créatinine et eGFR : comprendre la fonction rénale",
            "tr": "Kreatinin ve eGFR: Böbrek Fonksiyonu Sonuçları Nasıl Okunur",
            "es": "Creatinina y eGFR: cómo leer la función renal",
            "he": "קריאטינין ו-eGFR: איך לקרוא תוצאות תפקוד כליות",
            "hi": "क्रिएटिनिन और eGFR: किडनी फंक्शन रिज़ल्ट कैसे पढ़ें",
            "ar": "الكرياتينين وeGFR: كيف تقرأ نتائج وظيفة الكلى",
        },
        subtitles={
            "en": "What creatinine and eGFR mean, typical categories, what can affect results without kidney disease, and when to follow up with a clinician.",
            "de": "Was Kreatinin und eGFR bedeuten, typische Kategorien, Störfaktoren und wann Sie zum Arzt sollten.",
            "it": "Cosa significano creatinina ed eGFR, categorie tipiche, fattori confondenti e quando rivolgersi al medico.",
            "fr": "Ce que signifient créatinine et eGFR, catégories typiques, facteurs de confusion et quand consulter.",
            "tr": "Kreatinin ve eGFR ne anlama gelir, tipik kategoriler ve ne zaman doktora gidilmeli.",
            "es": "Qué significan creatinina y eGFR, categorías típicas y cuándo consultar.",
            "he": "מה אומרים קריאטינין ו-eGFR, קטגוריות ומתי לרופא.",
            "hi": "क्रिएटिनिन और eGFR क्या मतलब, श्रेणियां और डॉक्टर से कब मिलें।",
            "ar": "ماذا يعني الكرياتينين وeGFR والفئات ومتى ترى الطبيب.",
        },
        excerpts={
            "en": "Creatinine and eGFR reflect kidney function. Understanding typical ranges and what can affect results helps you discuss them with your doctor.",
            "de": "Kreatinin und eGFR spiegeln die Nierenfunktion wider. Typische Bereiche und Störfaktoren helfen beim Arztgespräch.",
            "it": "Creatinina ed eGFR riflettono la funzione renale. Conoscere gli intervalli tipici e i fattori confondenti aiuta a parlarne con il medico.",
            "fr": "Créatinine et eGFR reflètent la fonction rénale. Comprendre les seuils typiques et les facteurs de confusion aide à en parler avec le médecin.",
            "tr": "Kreatinin ve eGFR böbrek işlevini yansıtır. Tipik aralıklar ve sonucu etkileyen faktörler doktorla tartışmanıza yardımcı olur.",
            "es": "La creatinina y el eGFR reflejan la función renal. Entender los rangos típicos ayuda a hablar con el médico.",
            "he": "קריאטינין ו-eGFR משקפים את תפקוד הכליות. הבנת הטווחים עוזרת לשיחה עם הרופא.",
            "hi": "क्रिएटिनिन और eGFR किडनी फंक्शन दर्शाते हैं। रेंज समझकर डॉक्टर से बात करें।",
            "ar": "الكرياتينين وeGFR يعكسان وظيفة الكلى. فهم النطاقات يساعد في مناقشة النتائج مع الطبيب.",
        },
        seo_titles={
            "en": "Creatinine & eGFR Explained: Reading Kidney Function Results | NoryaAI",
            "de": "Kreatinin & eGFR verstehen: Nierenwerte richtig deuten | NoryaAI",
            "it": "Creatinina ed eGFR: come interpretare la funzione renale | NoryaAI",
            "fr": "Créatinine et eGFR : comprendre la fonction rénale | NoryaAI",
            "tr": "Kreatinin ve eGFR: Böbrek Fonksiyonu Sonuçları | NoryaAI",
            "es": "Creatinina y eGFR: función renal | NoryaAI",
            "he": "קריאטינין ו-eGFR: תוצאות תפקוד כליות | NoryaAI",
            "hi": "क्रिएटिनिन और eGFR: किडनी फंक्शन | NoryaAI",
            "ar": "الكرياتينين وeGFR: نتائج وظيفة الكلى | NoryaAI",
        },
        seo_descriptions={
            "en": "Understand creatinine and eGFR: what they mean, typical kidney function categories, what can affect results, and when to follow up. Informational only.",
            "de": "Kreatinin und eGFR verstehen: Bedeutung, typische Kategorien, Störfaktoren und wann zum Arzt. Nur zur Information.",
            "it": "Capire creatinina ed eGFR: significato, categorie tipiche, fattori confondenti e quando rivolgersi al medico. Solo informativo.",
            "fr": "Comprendre créatinine et eGFR : signification, catégories typiques, facteurs de confusion et quand consulter. À titre informatif uniquement.",
            "tr": "Kreatinin ve eGFR: ne anlama gelir, böbrek fonksiyonu kategorileri ve ne zaman doktora gidilmeli. Sadece bilgilendirme.",
            "es": "Entiende creatinina y eGFR: qué significan, categorías y cuándo consultar. Solo informativo.",
            "he": "הבן קריאטינין ו-eGFR: משמעות, קטגוריות ומתי לרופא. למידע בלבד.",
            "hi": "क्रिएटिनिन और eGFR समझें: मतलब, श्रेणियां और डॉक्टर से कब मिलें। सूचनात्मक।",
            "ar": "افهم الكرياتينين وeGFR: المعنى والفئات ومتى ترى الطبيب. للمعلومات فقط.",
        },
        sections_by_lang={
            "en": _creatinine_egfr_sections_en(),
            "de": _creatinine_egfr_sections_de(),
            "it": _creatinine_egfr_sections_it(),
            "fr": _creatinine_egfr_sections_fr(),
        },
    )


def _creatinine_egfr_sections_en() -> List[Section]:
    return [
        Section(
            id="what-creatinine-is",
            level=2,
            heading="What creatinine is and why it’s measured",
            body_html="""
<p>Creatinine is a waste product produced by your <strong>muscles</strong> as part of normal metabolism. It is released into the blood and filtered out by the kidneys. When kidney function is reduced, creatinine tends to rise in the blood because it is cleared less efficiently. Laboratories measure blood creatinine to help assess kidney function. The result is often reported in mg/dL or µmol/L. Creatinine alone does not tell the full story—body size, muscle mass, age, and sex can affect the level. That is why clinicians often use <strong>eGFR</strong> (estimated glomerular filtration rate), which adjusts for these factors.</p>
""",
        ),
        Section(
            id="what-egfr-means",
            level=2,
            heading="What eGFR means and why it can be more informative",
            body_html="""
<p><strong>eGFR</strong> (estimated glomerular filtration rate) is a calculated value that estimates how well your kidneys are filtering blood. It is usually derived from your creatinine level, age, and sex (and sometimes race, depending on the formula used). eGFR is often reported in mL/min/1.73 m². Because it accounts for age and body factors, it can be <strong>more informative than creatinine alone</strong> when assessing kidney function. A falling eGFR over time may suggest worsening kidney function and often prompts further tests. eGFR is an <strong>estimate</strong>; your clinician will interpret it together with other results (e.g. urine tests, imaging) and your medical history.</p>
""",
        ),
        Section(
            id="creatinine-vs-egfr-vs-bun",
            level=2,
            heading="Creatinine vs eGFR vs BUN",
            body_html="""
<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">
  <thead><tr class="bg-slate-50"><th class="border border-slate-200 px-3 py-2 text-left">Marker</th><th class="border border-slate-200 px-3 py-2 text-left">What it reflects</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>Creatinine</strong></td><td class="border border-slate-200 px-3 py-2">Waste product from muscle metabolism; cleared by kidneys. High level can indicate reduced kidney clearance.</td></tr>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>eGFR</strong></td><td class="border border-slate-200 px-3 py-2">Estimated filtration rate (often from creatinine, age, sex). Lower value = less kidney filtering capacity.</td></tr>
    <tr><td class="border border-slate-200 px-3 py-2"><strong>BUN</strong></td><td class="border border-slate-200 px-3 py-2">Blood urea nitrogen; influenced by protein intake, hydration, and kidney function. Often used together with creatinine.</td></tr>
  </tbody>
</table>
<p>Your doctor interprets these together in the context of your health and other tests.</p>
""",
        ),
        Section(
            id="egfr-categories",
            level=2,
            heading="Typical eGFR categories",
            body_html="""
<p>Reference ranges and categories <strong>vary by laboratory and guideline</strong>. The following is a rough guide for context only; your clinician will interpret your result in your situation. In many guidelines:</p>
<ul>
  <li><strong>≥90</strong>: Normal or near-normal (if no other markers of kidney damage).</li>
  <li><strong>60–89</strong>: Mildly decreased; context matters (e.g. age, other tests).</li>
  <li><strong>45–59</strong>: Mild to moderate decrease.</li>
  <li><strong>30–44</strong>: Moderate decrease.</li>
  <li><strong>15–29</strong>: Severe decrease.</li>
  <li><strong>&lt;15</strong>: Kidney failure range; urgent medical care is needed.</li>
</ul>
<p>These categories are for general information. The meaning of your result depends on your age, other kidney markers (e.g. urine albumin), and clinical context. Do not self-diagnose; discuss your results with a clinician.</p>
""",
        ),
        Section(
            id="what-can-change-without-kidney-disease",
            level=2,
            heading="What can change creatinine or eGFR without “true” kidney disease",
            body_html="""
<p>Several factors can raise creatinine or lower eGFR temporarily or without indicating lasting kidney damage:</p>
<ul>
  <li><strong>Dehydration</strong>: Less fluid can concentrate blood and raise creatinine.</li>
  <li><strong>High muscle mass</strong>: More muscle can produce more creatinine.</li>
  <li><strong>Intense or prolonged exercise</strong>: Can temporarily raise creatinine.</li>
  <li><strong>High-protein diet or creatine supplements</strong>: Can increase creatinine levels.</li>
  <li><strong>Certain medications</strong>: Some drugs affect kidney function or creatinine; your doctor will consider these.</li>
  <li><strong>Lab variation</strong>: Slight differences between labs or between draws can occur.</li>
</ul>
<p>If your result is borderline or only slightly outside the reference range, your clinician may suggest repeating the test (e.g. after rest and hydration) or ordering additional tests to clarify.</p>
""",
        ),
        Section(
            id="signs-need-medical-attention",
            level=2,
            heading="Signs that need prompt medical attention",
            body_html="""
<p>Seek medical care promptly if you have:</p>
<ul>
  <li><strong>Swelling</strong> (especially of legs, feet, or face).</li>
  <li><strong>Shortness of breath</strong> or difficulty breathing.</li>
  <li><strong>Very low urine output</strong> or no urination.</li>
  <li><strong>Confusion</strong> or severe drowsiness.</li>
  <li><strong>Persistent vomiting</strong> or inability to keep fluids down.</li>
  <li><strong>Severe weakness</strong> or fatigue.</li>
  <li><strong>Chest pain</strong> or pressure.</li>
</ul>
<p>These can be signs of serious kidney or other medical problems. This list is not complete; if you are worried, contact a healthcare provider.</p>
""",
        ),
        Section(
            id="next-tests-clinicians-use",
            level=2,
            heading="Next tests clinicians often use to confirm kidney status",
            body_html="""
<p>Depending on your result and history, your doctor may order:</p>
<ul>
  <li><strong>Urine ACR</strong> (albumin-to-creatinine ratio) to look for kidney damage.</li>
  <li><strong>Urinalysis</strong> for blood, protein, or other abnormalities.</li>
  <li><strong>Repeat creatinine and eGFR</strong> to see if the result is stable.</li>
  <li><strong>Electrolytes</strong> (e.g. potassium, sodium) if kidney function is a concern.</li>
  <li><strong>Blood pressure</strong> measurement and monitoring.</li>
  <li><strong>Glucose or HbA1c</strong> if diabetes is relevant.</li>
  <li><strong>Ultrasound or other imaging</strong> of the kidneys when indicated.</li>
</ul>
<p>Which tests are chosen is a clinical decision made with you by your doctor.</p>
""",
        ),
        Section(
            id="practical-kidney-friendly-habits",
            level=2,
            heading="Practical kidney-friendly habits",
            body_html="""
<p>General measures that often support kidney health (and are not a substitute for medical advice or treatment):</p>
<ul>
  <li><strong>Hydration</strong>: Adequate fluid intake, unless your doctor has restricted it for a medical reason.</li>
  <li><strong>Blood pressure and diabetes control</strong>: Important for long-term kidney health; follow your doctor’s plan.</li>
  <li><strong>Avoid NSAID overuse</strong>: Non-steroidal anti-inflammatory drugs can affect the kidneys; use only as directed and discuss with your doctor if you have kidney concerns.</li>
  <li><strong>Salt moderation</strong>: In line with general heart and kidney health advice; your clinician can advise on your target.</li>
  <li><strong>Protein intake</strong>: If you have known kidney disease, your doctor or dietitian may give specific guidance on protein; do not change diet solely based on this article.</li>
</ul>
""",
        ),
        Section(
            id="faq",
            level=2,
            heading="Frequently asked questions",
            body_html="""
<p>See the FAQ entries in this article; your clinician will interpret your individual results and advise on follow-up.</p>
""",
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Medical disclaimer",
            body_html="""
<p><strong>This content is for information only and does not constitute medical advice, diagnosis, or treatment.</strong> Always discuss your results and any symptoms with a qualified healthcare provider. Do not start or change diet, exercise, or medication based solely on this article. If you have concerns about your health, seek professional medical care.</p>
""",
        ),
    ]


def _creatinine_egfr_sections_de() -> List[Section]:
    return [
        Section(id="what-creatinine-is", level=2, heading="Was Kreatinin ist und warum es gemessen wird",
            body_html="<p>Kreatinin ist ein <strong>Abbauprodukt der Muskeln</strong> und wird über die Nieren ausgeschieden. Bei eingeschränkter Nierenfunktion steigt der Kreatininwert im Blut. Labore messen das Blutkreatinin zur Beurteilung der Nierenfunktion (oft in mg/dL oder µmol/L). Kreatinin allein reicht nicht—Körpergröße, Muskelmasse, Alter und Geschlecht beeinflussen den Wert. Daher nutzen Ärzte oft den <strong>eGFR</strong> (geschätzter glomerulärer Filtrationswert), der diese Faktoren berücksichtigt.</p>"),
        Section(id="what-egfr-means", level=2, heading="Was der eGFR bedeutet und warum er aussagekräftiger sein kann",
            body_html="<p>Der <strong>eGFR</strong> (geschätzter glomerulärer Filtrationswert) schätzt, wie gut die Nieren das Blut filtern. Er wird meist aus Kreatinin, Alter und Geschlecht berechnet (Formel abhängig). Der eGFR wird oft in mL/min/1,73 m² angegeben. Da er Alter und Körperfaktoren einbezieht, ist er oft <strong>aussagekräftiger als Kreatinin allein</strong>. Ein sinkender eGFR kann auf eine Verschlechterung hindeuten. Der eGFR ist eine <strong>Schätzung</strong>; Ihr Arzt interpretiert ihn zusammen mit anderen Befunden (z. B. Urin, Bildgebung) und Ihrer Anamnese.</p>"),
        Section(id="creatinine-vs-egfr-vs-bun", level=2, heading="Kreatinin vs. eGFR vs. BUN",
            body_html="<p><strong>Kreatinin</strong>: Abbauprodukt der Muskeln; wird von den Nieren ausgeschieden. Erhöhung kann auf verminderte Nierenfunktion hinweisen. <strong>eGFR</strong>: Geschätzte Filtrationsrate (meist aus Kreatinin, Alter, Geschlecht). Niedrigerer Wert = geringere Filtrationsleistung. <strong>BUN</strong> (Harnstoff-Stickstoff): Von Eiweißzufuhr, Flüssigkeit und Nierenfunktion beeinflusst; wird oft zusammen mit Kreatinin beurteilt. Ihr Arzt wertet die Werte im Kontext aus.</p>"),
        Section(id="egfr-categories", level=2, heading="Typische eGFR-Kategorien",
            body_html="<p>Referenzbereiche <strong>variieren je nach Labor und Leitlinie</strong>. Grobe Orientierung: <strong>≥90</strong> oft normal/nah-normal; <strong>60–89</strong> leicht vermindert (Kontext wichtig); <strong>45–59</strong> leicht bis mäßig; <strong>30–44</strong> mäßig; <strong>15–29</strong> stark vermindert; <strong>&lt;15</strong> Nierenversagen—dringend ärztliche Betreuung. Die Einordnung Ihres Wertes erfolgt durch den Arzt unter Berücksichtigung von Alter, weiteren Nierenmarkern (z. B. Urin-Albumin) und Klinik.</p>"),
        Section(id="what-can-change-without-kidney-disease", level=2, heading="Was Kreatinin/eGFR ohne „echte“ Nierenerkrankung verändern kann",
            body_html="<p>U. a.: <strong>Dehydratation</strong>, <strong>hohe Muskelmasse</strong>, <strong>intensiver Sport</strong>, <strong>viel Eiweiß/Kreatin-Supplemente</strong>, <strong>bestimmte Medikamente</strong>, <strong>Laborabweichungen</strong>. Bei Grenzwerten kann der Arzt eine Wiederholung (z. B. nach Erholung und Trinken) oder weitere Tests empfehlen.</p>"),
        Section(id="signs-need-medical-attention", level=2, heading="Zeichen, die rasche ärztliche Abklärung erfordern",
            body_html="<p>Bitte zeitnah zum Arzt bei: <strong>Ödemen</strong> (Beine, Füße, Gesicht), <strong>Kurzatmigkeit</strong>, <strong>sehr wenig Urin</strong>, <strong>Verwirrtheit</strong> oder starke Müdigkeit, <strong>anhaltendem Erbrechen</strong>, <strong>starker Schwäche</strong>, <strong>Brustschmerzen</strong>. Diese Liste ist nicht vollständig; bei Sorgen einen Arzt kontaktieren.</p>"),
        Section(id="next-tests-clinicians-use", level=2, heading="Weitere Tests, die der Arzt oft veranlasst",
            body_html="<p>Je nach Befund: <strong>Urin-ACR</strong> (Albumin-Kreatinin-Quotient), <strong>Urinanalyse</strong>, <strong>Wiederholung Kreatinin/eGFR</strong>, <strong>Elektrolyte</strong> (K, Na), <strong>Blutdruck</strong>, <strong>Glukose/HbA1c</strong>, <strong>Sonographie</strong> der Nieren. Die Auswahl trifft der Arzt mit Ihnen.</p>"),
        Section(id="practical-kidney-friendly-habits", level=2, heading="Praktische nierenfreundliche Gewohnheiten",
            body_html="<p>Allgemeine Hinweise (kein Ersatz für ärztlichen Rat): <strong>Flüssigkeit</strong> ausreichend, sofern nicht vom Arzt eingeschränkt. <strong>Blutdruck und Diabetes</strong> gut einstellen. <strong>NSAR</strong> nicht übermäßig; bei Nierenfragen mit dem Arzt besprechen. <strong>Salz</strong> in Maßen. <strong>Eiweiß</strong>: Bei bekannter Nierenerkrankung kann der Arzt/die Diätberatung gezielte Empfehlungen geben.</p>"),
        Section(id="faq", level=2, heading="Häufige Fragen",
            body_html="<p>Siehe FAQ in diesem Artikel; die Bewertung Ihrer Werte erfolgt durch den Arzt.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
            body_html="<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung, Diagnose oder Behandlung.</strong> Besprechen Sie Ergebnisse und Beschwerden immer mit einem Arzt. Keine Änderung von Ernährung, Bewegung oder Medikation nur aufgrund dieses Artikels.</p>"),
    ]


def _creatinine_egfr_sections_it() -> List[Section]:
    return [
        Section(id="what-creatinine-is", level=2, heading="Cos'è la creatinina e perché si misura",
            body_html="<p>La creatinina è un <strong>prodotto di scarto del metabolismo muscolare</strong>, eliminata dai reni. Se la funzione renale è ridotta, la creatinina nel sangue tende ad aumentare. I laboratori la misurano per valutare la funzione renale (spesso in mg/dL o µmol/L). La creatinina da sola non basta—corporatura, massa muscolare, età e sesso la influenzano. Per questo si usa spesso l'<strong>eGFR</strong> (filtrato glomerulare stimato), che tiene conto di questi fattori.</p>"),
        Section(id="what-egfr-means", level=2, heading="Cosa significa l'eGFR e perché può essere più informativo",
            body_html="<p>L'<strong>eGFR</strong> (filtrato glomerulare stimato) stima quanto bene i reni filtrano il sangue. Si calcola di solito da creatinina, età e sesso. Si esprime spesso in mL/min/1,73 m². Considerando età e fattori corporei, può essere <strong>più informativo della sola creatinina</strong>. Un eGFR in calo può indicare peggioramento. L'eGFR è una <strong>stima</strong>; il medico lo interpreta con altri esami (es. urina, imaging) e la storia clinica.</p>"),
        Section(id="creatinine-vs-egfr-vs-bun", level=2, heading="Creatinina vs eGFR vs BUN",
            body_html="<p><strong>Creatinina</strong>: prodotto di scarto muscolare; eliminata dai reni. Valore alto può indicare ridotta clearance renale. <strong>eGFR</strong>: velocità di filtrazione stimata; valore più basso = minore capacità filtrante. <strong>BUN</strong> (azoto ureico): influenzato da proteine, idratazione e funzione renale; spesso valutato con la creatinina. Il medico interpreta il tutto nel contesto.</p>"),
        Section(id="egfr-categories", level=2, heading="Categorie eGFR tipiche",
            body_html="<p>Gli intervalli <strong>variano per laboratorio e linee guida</strong>. Orientativamente: <strong>≥90</strong> normale o quasi; <strong>60–89</strong> lieve riduzione (conto il contesto); <strong>45–59</strong> lieve-moderata; <strong>30–44</strong> moderata; <strong>15–29</strong> severa; <strong>&lt;15</strong> insufficienza renale—cure urgenti. L'interpretazione del vostro valore spetta al medico (età, altri marker, quadro clinico).</p>"),
        Section(id="what-can-change-without-kidney-disease", level=2, heading="Cosa può alterare creatinina/eGFR senza malattia renale “vera”",
            body_html="<p>Es.: <strong>disidratazione</strong>, <strong>massa muscolare alta</strong>, <strong>esercizio intenso</strong>, <strong>dieta iperproteica o integratori di creatina</strong>, <strong>alcuni farmaci</strong>, <strong>variazione di laboratorio</strong>. In caso di valori al limite il medico può consigliare ripetizione (es. dopo riposo e idratazione) o altri esami.</p>"),
        Section(id="signs-need-medical-attention", level=2, heading="Segni che richiedono attenzione medica tempestiva",
            body_html="<p>Rivolgersi al medico in caso di: <strong>gonfiore</strong> (gambe, piedi, viso), <strong>mancanza di respiro</strong>, <strong>scarsa emissione di urina</strong>, <strong>confusione</strong> o sonnolenza marcata, <strong>vomito persistente</strong>, <strong>debolezza grave</strong>, <strong>dolore al petto</strong>. Lista non esaustiva; in caso di dubbi contattare il medico.</p>"),
        Section(id="next-tests-clinicians-use", level=2, heading="Altri esami che il medico può richiedere",
            body_html="<p>A seconda del risultato: <strong>ACR urinario</strong>, <strong>esame delle urine</strong>, <strong>ripetizione creatinina/eGFR</strong>, <strong>elettroliti</strong> (K, Na), <strong>pressione</strong>, <strong>glicemia/HbA1c</strong>, <strong>ecografia</strong> renale. La scelta è clinica.</p>"),
        Section(id="practical-kidney-friendly-habits", level=2, heading="Abitudini pratiche a sostegno dei reni",
            body_html="<p>Indicazioni generali (non sostituiscono il parere medico): <strong>idratazione</strong> adeguata salvo diversa indicazione. <strong>Controllo pressione e diabete</strong>. <strong>Evitare abuso di FANS</strong>; in caso di problemi renali parlarne con il medico. <strong>Sale</strong> con moderazione. <strong>Proteine</strong>: in caso di malattia renale nota, il medico/dietista può dare indicazioni specifiche.</p>"),
        Section(id="faq", level=2, heading="Domande frequenti",
            body_html="<p>Vedi le FAQ in questo articolo; l'interpretazione dei vostri valori spetta al medico.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer medico",
            body_html="<p><strong>Questo contenuto è solo informativo e non costituisce consulenza, diagnosi o trattamento medico.</strong> Discutere sempre risultati e sintomi con un operatore sanitario. Non modificare dieta, esercizio o farmaci solo in base a questo articolo.</p>"),
    ]


def _creatinine_egfr_sections_fr() -> List[Section]:
    return [
        Section(id="what-creatinine-is", level=2, heading="Ce qu'est la créatinine et pourquoi on la dose",
            body_html="<p>La créatinine est un <strong>produit de dégradation du métabolisme musculaire</strong>, éliminée par les reins. Quand la fonction rénale baisse, la créatinine sanguine tend à augmenter. Les laboratoires la dosent pour évaluer la fonction rénale (souvent en mg/dL ou µmol/L). La créatinine seule ne suffit pas—taille, masse musculaire, âge et sexe l'influencent. C'est pourquoi on utilise souvent l'<strong>eGFR</strong> (débit de filtration glomérulaire estimé), qui tient compte de ces facteurs.</p>"),
        Section(id="what-egfr-means", level=2, heading="Ce que signifie l'eGFR et pourquoi il peut être plus informatif",
            body_html="<p>L'<strong>eGFR</strong> (débit de filtration glomérulaire estimé) estime la capacité des reins à filtrer le sang. Il est calculé à partir de la créatinine, de l'âge et du sexe. Il est souvent exprimé en mL/min/1,73 m². En tenant compte de l'âge et du corps, il peut être <strong>plus informatif que la créatinine seule</strong>. Une baisse de l'eGFR peut suggérer une aggravation. L'eGFR est une <strong>estimation</strong> ; le médecin l'interprète avec les autres résultats (urines, imagerie) et l'histoire clinique.</p>"),
        Section(id="creatinine-vs-egfr-vs-bun", level=2, heading="Créatinine vs eGFR vs BUN",
            body_html="<p><strong>Créatinine</strong> : déchet du métabolisme musculaire ; éliminée par les reins. Un taux élevé peut indiquer une baisse de la fonction rénale. <strong>eGFR</strong> : débit de filtration estimé ; valeur basse = moins de capacité de filtration. <strong>BUN</strong> (urée sanguine) : influencé par les protéines, l'hydratation et la fonction rénale ; souvent interprété avec la créatinine. Le médecin fait la synthèse dans votre contexte.</p>"),
        Section(id="egfr-categories", level=2, heading="Catégories d'eGFR typiques",
            body_html="<p>Les seuils <strong>varient selon le laboratoire et les recommandations</strong>. À titre indicatif : <strong>≥90</strong> normal ou proche ; <strong>60–89</strong> légèrement diminué (contexte important) ; <strong>45–59</strong> légère à modérée ; <strong>30–44</strong> modérée ; <strong>15–29</strong> sévère ; <strong>&lt;15</strong> insuffisance rénale—prise en charge urgente. L'interprétation de votre résultat relève du médecin (âge, autres marqueurs, tableau clinique).</p>"),
        Section(id="what-can-change-without-kidney-disease", level=2, heading="Ce qui peut modifier créatinine ou eGFR sans « vraie » maladie rénale",
            body_html="<p>Ex. : <strong>déshydratation</strong>, <strong>forte masse musculaire</strong>, <strong>exercice intense</strong>, <strong>régime hyperprotéiné ou compléments de créatine</strong>, <strong>certains médicaments</strong>, <strong>variation entre laboratoires</strong>. En cas de valeur limite, le médecin peut proposer de répéter le dosage (après repos et réhydratation) ou d'autres examens.</p>"),
        Section(id="signs-need-medical-attention", level=2, heading="Signes qui nécessitent une consultation rapide",
            body_html="<p>Consulter en cas de : <strong>œdèmes</strong> (jambes, pieds, visage), <strong>essoufflement</strong>, <strong>très peu d'urines</strong>, <strong>confusion</strong> ou somnolence importante, <strong>vomissements persistants</strong>, <strong>faiblesse sévère</strong>, <strong>douleur thoracique</strong>. Liste non exhaustive ; en cas d'inquiétude, contacter un professionnel de santé.</p>"),
        Section(id="next-tests-clinicians-use", level=2, heading="Examens que le médecin peut prescrire",
            body_html="<p>Selon le résultat : <strong>ACR urinaire</strong>, <strong>analyse d'urines</strong>, <strong>répétition créatinine/eGFR</strong>, <strong>électrolytes</strong> (K, Na), <strong>tension</strong>, <strong>glycémie/HbA1c</strong>, <strong>échographie</strong> rénale. Le choix est clinique.</p>"),
        Section(id="practical-kidney-friendly-habits", level=2, heading="Habitudes pratiques pour les reins",
            body_html="<p>Recommandations générales (ne remplacent pas l'avis médical) : <strong>hydratation</strong> suffisante sauf contre-indication. <strong>Contrôle tension et diabète</strong>. <strong>Éviter l'abus d'AINS</strong> ; en cas de souci rénal en parler au médecin. <strong>Sel</strong> avec modération. <strong>Protéines</strong> : en cas de maladie rénale connue, le médecin/diététicien peut donner des conseils ciblés.</p>"),
        Section(id="faq", level=2, heading="Questions fréquentes",
            body_html="<p>Voir les FAQ dans cet article ; l'interprétation de vos résultats relève du médecin.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement médical",
            body_html="<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis, diagnostic ou traitement médical.</strong> Toujours discuter des résultats et symptômes avec un professionnel de santé. Ne pas modifier alimentation, exercice ou médicaments uniquement sur la base de cet article.</p>"),
    ]


_CREATININE_EGFR_ARTICLE = _article_creatinine_egfr()


def _article_blutwerte_online_analysieren() -> Article:
    """Blutwerte online analysieren — DE/EN/TR rehber (SEO: Blutwerte online analysieren)."""
    published = date(2025, 3, 12)
    cover = "/static/images/blog/how-to-read-blood-test-results.png"
    return Article(
        id="blutwerte-online-analysieren",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        category={
            "tr": "Rehber",
            "en": "Guide",
            "de": "Ratgeber",
            "it": "Guida",
            "es": "Guía",
            "fr": "Guide",
            "he": "מדריך",
            "hi": "गाइड",
            "ar": "دليل",
        },
        slugs={
            "tr": "kan-tahlili-online-analiz",
            "en": "blood-test-online-analysis",
            "de": "blutwerte-online-analysieren-so-gehts",
            "it": "analisi-online-esami-sangue",
            "es": "analisis-online-analisis-sangre",
            "fr": "analyse-en-ligne-bilan-sanguin",
            "he": "blood-test-online-analysis",
            "hi": "blood-test-online-analysis",
            "ar": "blood-test-online-analysis",
        },
        titles={
            "tr": "Kan tahlilini online nasıl analiz ettirirsiniz?",
            "en": "How to analyse your blood test online",
            "de": "Blutwerte online analysieren: So geht's",
            "it": "Come analizzare online gli esami del sangue",
            "es": "Cómo analizar tu análisis de sangre online",
            "fr": "Comment analyser votre bilan sanguin en ligne",
            "he": "איך לנתח את בדיקת הדם שלך אונליין",
            "hi": "ब्लड टेस्ट ऑनलाइन कैसे विश्लेषण करें",
            "ar": "كيف تحلل تحاليلك الدموية عبر الإنترنت",
        },
        subtitles={
            "tr": "Laboratuvar sonuçlarınızı yükleyin, dakikalar içinde anlaşılır bir rapor alın. Üç adımda rehber.",
            "en": "Upload your lab results and get a clear report in minutes. A short guide in three steps.",
            "de": "Befund hochladen, in wenigen Minuten einen verständlichen Bericht erhalten. Kurz erklärt in drei Schritten.",
            "it": "Carica i referti e ottieni un report chiaro in pochi minuti. Guida in tre passi.",
            "es": "Sube tus resultados y obtén un informe claro en minutos. Guía en tres pasos.",
            "fr": "Uploadez vos résultats et obtenez un rapport clair en quelques minutes. Guide en trois étapes.",
            "he": "העלה את התוצאות וקבל דוח ברור תוך דקות. מדריך קצר בשלושה שלבים.",
            "hi": "अपने रिज़ल्ट अपलोड करें, मिनटों में स्पष्ट रिपोर्ट पाएं। तीन चरणों में गाइड।",
            "ar": "ارفع نتائجك واحصل على تقرير واضح في دقائق. دليل من ثلاث خطوات.",
        },
        excerpts={
            "tr": "Kan tahlili sonuçlarınızı online analiz ettirmek için Norya ile üç adım: yükle, raporu al, doktorunla paylaş.",
            "en": "Three steps to analyse your blood test online with Norya: upload, get the report, share with your doctor.",
            "de": "Blutwerte online analysieren mit Norya in drei Schritten: hochladen, Bericht erhalten, mit dem Arzt teilen.",
            "it": "Tre passi per analizzare gli esami del sangue online con Norya: carica, ottieni il report, condividi con il medico.",
            "es": "Tres pasos para analizar tu análisis online con Norya: subir, obtener el informe, compartir con el médico.",
            "fr": "Trois étapes pour analyser votre bilan en ligne avec Norya : uploader, obtenir le rapport, partager avec le médecin.",
            "he": "שלושה שלבים לניתוח בדיקת הדם אונליין עם Norya: העלאה, קבלת דוח, שיתוף עם הרופא.",
            "hi": "Norya के साथ ब्लड टेस्ट ऑनलाइन विश्लेषण के तीन चरण: अपलोड करें, रिपोर्ट पाएं, डॉक्टर के साथ साझा करें।",
            "ar": "ثلاث خطوات لتحليل التحاليل عبر Norya: ارفع، احصل على التقرير، شارك مع الطبيب.",
        },
        seo_titles={
            "tr": "Kan Tahlili Online Analiz | Laboratuvar Sonuçları Yorumlama",
            "en": "Blood Test Online Analysis: How It Works | NoryaAI",
            "de": "Blutwerte online analysieren: So geht's | NoryaAI",
            "it": "Analisi esami del sangue online: come funziona | NoryaAI",
            "es": "Análisis de sangre online: cómo funciona | NoryaAI",
            "fr": "Analyse bilan sanguin en ligne : comment ça marche | NoryaAI",
            "he": "ניתוח בדיקת דם אונליין: איך זה עובד | NoryaAI",
            "hi": "ब्लड टेस्ट ऑनलाइन विश्लेषण: कैसे काम करता है | NoryaAI",
            "ar": "تحليل التحاليل الدموية عبر الإنترنت: كيف يعمل | NoryaAI",
        },
        seo_descriptions={
            "tr": "Kan tahlili sonuçlarınızı online analiz ettirin. PDF veya fotoğraf yükleyin, anlaşılır rapor alın. Teşhis yerine bilgilendirme.",
            "en": "Analyse your blood test results online. Upload PDF or photo, get a clear report. For information only, not diagnosis.",
            "de": "Blutwerte online analysieren: Befund hochladen, klaren Bericht erhalten. Nur zur Information, keine Diagnose.",
            "it": "Analizza i tuoi esami del sangue online. Carica PDF o foto, ottieni un report chiaro. Solo informativo.",
            "es": "Analiza tus resultados de análisis online. Sube PDF o foto, obtén un informe claro. Solo informativo.",
            "fr": "Analysez vos résultats en ligne. Uploadez PDF ou photo, obtenez un rapport clair. À titre informatif uniquement.",
            "he": "נתח את תוצאות בדיקת הדם אונליין. העלה PDF או תמונה, קבל דוח ברור. למידע בלבד.",
            "hi": "अपने ब्लड टेस्ट रिज़ल्ट ऑनलाइन विश्लेषण करें। PDF या फोटो अपलोड करें, स्पष्ट रिपोर्ट पाएं। सूचनात्मक।",
            "ar": "حلل نتائج تحاليلك عبر الإنترنت. ارفع PDF أو صورة، احصل على تقرير واضح. للمعلومات فقط.",
        },
        sections_by_lang={
            "tr": _blutwerte_online_sections_tr(),
            "en": _blutwerte_online_sections_en(),
            "de": _blutwerte_online_sections_de(),
            "it": _blutwerte_online_sections_it(),
            "fr": _blutwerte_online_sections_fr(),
            "es": _blutwerte_online_sections_es(),
            "he": _blutwerte_online_sections_he(),
            "hi": _blutwerte_online_sections_hi(),
            "ar": _blutwerte_online_sections_ar(),
        },
    )


def _blutwerte_online_sections_de() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="Warum Blutwerte online auswerten?",
            body_html="<p>Viele Menschen erhalten nach dem Arztbesuch oder dem Labor einen Befund mit Abkürzungen und Zahlen. <strong>Blutwerte online analysieren</strong> hilft dabei, diese Werte einzuordnen—bevor Sie zum nächsten Termin gehen oder Fragen an Ihren Arzt haben. Mit Norya laden Sie Ihren Befund hoch und erhalten einen verständlichen Bericht mit Referenzbereichen und kurzen Empfehlungen. Das ersetzt keine Diagnose, unterstützt aber Ihre Vorbereitung auf das Arztgespräch.</p>"),
        Section(id="steps", level=2, heading="Blutwerte online analysieren in drei Schritten",
            body_html="<p><strong>Schritt 1:</strong> Auf Norya gehen und anmelden bzw. kostenlos starten. <strong>Schritt 2:</strong> Ihren Laborbefund hochladen—als PDF, Foto (JPG/PNG) oder durch Einfügen des Textes. <strong>Schritt 3:</strong> Den Bericht lesen und bei Bedarf als PDF herunterladen oder mit Ihrem Arzt teilen. Die Auswertung erfolgt automatisch; Sie erhalten eine strukturierte Übersicht und Einordnung Ihrer Werte.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
            body_html="<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung, Diagnose oder Behandlung.</strong> Die Auswertung bei Norya ist bildend und orientierend. Besprechen Sie Ihre Ergebnisse und Beschwerden immer mit einem Arzt. <a href=\"/de/upload\">Blutwerte bei Norya auswerten</a> — Jetzt starten.</p>"),
    ]


def _blutwerte_online_sections_en() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="Why analyse blood test results online?",
            body_html="<p>Many people receive a lab report full of abbreviations and numbers. <strong>Analysing your blood test online</strong> helps you understand these values—before your next appointment or when you have questions for your doctor. With Norya you upload your result and get a clear report with reference ranges and short recommendations. This is not a diagnosis, but it helps you prepare for the conversation with your doctor.</p>"),
        Section(id="steps", level=2, heading="How to analyse your blood test online in three steps",
            body_html="<p><strong>Step 1:</strong> Go to Norya and sign up or start for free. <strong>Step 2:</strong> Upload your lab result—as PDF, photo (JPG/PNG), or by pasting the text. <strong>Step 3:</strong> Read the report and, if needed, download it as PDF or share it with your doctor. The analysis is automatic; you get a structured overview and interpretation of your values.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
            body_html="<p><strong>This content is for information only and does not constitute medical advice, diagnosis, or treatment.</strong> Norya's analysis is educational and for orientation. Always discuss your results and any symptoms with a doctor. <a href=\"/en/upload\">Analyse your blood test with Norya</a> — Get started.</p>"),
    ]


def _blutwerte_online_sections_tr() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="Kan tahlilini neden online analiz ettirmelisiniz?",
            body_html="<p>Birçok kişi laboratuvar veya doktor sonrası kısaltmalar ve sayılarla dolu bir sonuç kağıdı alıyor. <strong>Kan tahlilini online analiz ettirmek</strong>, bir sonraki randevudan veya doktorunuza sormak istediğiniz sorulardan önce bu değerleri anlamanıza yardımcı olur. Norya ile sonucunuzu yüklersiniz ve referans aralıkları ile kısa öneriler içeren anlaşılır bir rapor alırsınız. Bu bir teşhis değildir; ancak doktor görüşmenize hazırlanmanıza yardımcı olur.</p>"),
        Section(id="steps", level=2, heading="Kan tahlilini online analiz ettirmenin üç adımı",
            body_html="<p><strong>Adım 1:</strong> Norya'ya gidin ve ücretsiz başlayın. <strong>Adım 2:</strong> Laboratuvar sonucunuzu yükleyin—PDF, fotoğraf (JPG/PNG) veya metni yapıştırarak. <strong>Adım 3:</strong> Raporu okuyun ve gerekiyorsa PDF indirin veya doktorunuzla paylaşın. Analiz otomatik yapılır; değerlerinizin yapılandırılmış bir özeti ve yorumunu alırsınız.</p>"),
        Section(id="disclaimer", level=2, heading="Uyarı",
            body_html="<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye, teşhis veya tedavinin yerine geçmez.</strong> Norya analizi eğitim ve yönlendirme içindir. Sonuçlarınızı ve şikayetlerinizi her zaman bir hekimle görüşün. <a href=\"/tr/upload\">Norya ile kan tahlili analizi</a> — Hemen başlayın.</p>"),
    ]


def _blutwerte_online_sections_it() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="Perché analizzare gli esami del sangue online?",
            body_html="<p>Molte persone ricevono un referto pieno di sigle e numeri. <strong>Analizzare gli esami del sangue online</strong> aiuta a capire questi valori prima del prossimo controllo o quando avete domande per il medico. Con Norya caricate il risultato e ottenete un report chiaro con intervalli di riferimento e brevi raccomandazioni. Non è una diagnosi, ma aiuta a prepararsi al colloquio con il medico.</p>"),
        Section(id="steps", level=2, heading="Come analizzare gli esami del sangue online in tre passi",
            body_html="<p><strong>Passo 1:</strong> Andate su Norya e registratevi o iniziate gratuitamente. <strong>Passo 2:</strong> Caricate il referto—in PDF, foto (JPG/PNG) o incollando il testo. <strong>Passo 3:</strong> Leggete il report e, se serve, scaricatelo in PDF o condividetelo con il medico. L'analisi è automatica; ottenete una panoramica strutturata e un'interpretazione dei vostri valori.</p>"),
        Section(id="disclaimer", level=2, heading="Nota",
            body_html="<p><strong>Questo contenuto è solo informativo e non costituisce consulenza medica, diagnosi o trattamento.</strong> L'analisi Norya è a scopo educativo. Discutete sempre i risultati e i sintomi con un medico. <a href=\"/it/upload\">Analizza gli esami con Norya</a> — Inizia ora.</p>"),
    ]


def _blutwerte_online_sections_fr() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="Pourquoi analyser votre bilan sanguin en ligne ?",
            body_html="<p>Beaucoup de personnes reçoivent un résultat d'analyses avec des abréviations et des chiffres. <strong>Analyser votre bilan sanguin en ligne</strong> vous aide à comprendre ces valeurs avant votre prochain rendez-vous ou quand vous avez des questions pour votre médecin. Avec Norya vous uploadez votre résultat et obtenez un rapport clair avec les fourchettes de référence et de courtes recommandations. Ce n'est pas un diagnostic, mais cela vous aide à préparer l'échange avec votre médecin.</p>"),
        Section(id="steps", level=2, heading="Comment analyser votre bilan en ligne en trois étapes",
            body_html="<p><strong>Étape 1 :</strong> Allez sur Norya et inscrivez-vous ou commencez gratuitement. <strong>Étape 2 :</strong> Uploadez votre résultat—en PDF, photo (JPG/PNG) ou en collant le texte. <strong>Étape 3 :</strong> Lisez le rapport et, si besoin, téléchargez-le en PDF ou partagez-le avec votre médecin. L'analyse est automatique ; vous obtenez une vue structurée et une interprétation de vos valeurs.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
            body_html="<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis médical, un diagnostic ou un traitement.</strong> L'analyse Norya est à but éducatif. Discutez toujours de vos résultats et symptômes avec un médecin. <a href=\"/fr/upload\">Analyser votre bilan avec Norya</a> — Commencer.</p>"),
    ]


def _blutwerte_online_sections_es() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="¿Por qué analizar tu análisis de sangre online?",
            body_html="<p>Muchas personas reciben un informe con abreviaturas y números. <strong>Analizar tu análisis de sangre online</strong> te ayuda a entender estos valores antes de tu próxima cita o cuando tengas preguntas para tu médico. Con Norya subes tu resultado y obtienes un informe claro con rangos de referencia y recomendaciones breves. No es un diagnóstico, pero te ayuda a preparar la conversación con tu médico.</p>"),
        Section(id="steps", level=2, heading="Cómo analizar tu análisis online en tres pasos",
            body_html="<p><strong>Paso 1:</strong> Entra en Norya y regístrate o empieza gratis. <strong>Paso 2:</strong> Sube tu resultado—en PDF, foto (JPG/PNG) o pegando el texto. <strong>Paso 3:</strong> Lee el informe y, si hace falta, descárgalo en PDF o compártelo con tu médico. El análisis es automático; obtienes una visión estructurada e interpretación de tus valores.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
            body_html="<p><strong>Este contenido es solo informativo y no sustituye el consejo médico, el diagnóstico o el tratamiento.</strong> El análisis de Norya es educativo. Comenta siempre tus resultados y síntomas con un médico. <a href=\"/es/upload\">Analiza tu análisis con Norya</a> — Empieza ahora.</p>"),
    ]


def _blutwerte_online_sections_he() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="למה לנתח את בדיקת הדם אונליין?",
            body_html="<p>רבים מקבלים דף תוצאות מלא בקיצורים ומספרים. <strong>ניתוח בדיקת הדם אונליין</strong> עוזר להבין את הערכים לפני הפגישה הבאה או כשיש שאלות לרופא. עם Norya מעלים את התוצאה ומקבלים דוח ברור עם טווחי נורמה והמלצות קצרות. זה לא אבחנה, אבל עוזר להתכונן לשיחה עם הרופא.</p>"),
        Section(id="steps", level=2, heading="איך לנתח את בדיקת הדם אונליין בשלושה שלבים",
            body_html="<p><strong>שלב 1:</strong> היכנסו ל-Norya והרשמו או התחילו בחינם. <strong>שלב 2:</strong> העלו את התוצאה—כ-PDF, תמונה (JPG/PNG) או בהדבקת הטקסט. <strong>שלב 3:</strong> קראו את הדוח ובהתאם הורידו PDF או שתפו עם הרופא. הניתוח אוטומטי; מקבלים סקירה מסודרת ופרשנות לערכים.</p>"),
        Section(id="disclaimer", level=2, heading="הערה",
            body_html="<p><strong>התוכן למידע בלבד ואינו ייעוץ רפואי, אבחנה או טיפול.</strong> ניתוח Norya הוא חינוכי. תמיד דונו בתוצאות ובתסמינים עם רופא. <a href=\"/he/upload\">נתח את הבדיקה עם Norya</a> — התחל עכשיו.</p>"),
    ]


def _blutwerte_online_sections_hi() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="ब्लड टेस्ट ऑनलाइन क्यों विश्लेषण करें?",
            body_html="<p>कई लोगों को संक्षिप्त नाम और संख्याओं वाली रिपोर्ट मिलती है। <strong>ब्लड टेस्ट ऑनलाइन विश्लेषण</strong> अगली अपॉइंटमेंट से पहले या डॉक्टर से सवाल पूछने से पहले इन मानों को समझने में मदद करता है। Norya से आप रिज़ल्ट अपलोड करते हैं और रेफरेंस रेंज और संक्षिप्त सुझावों वाली स्पष्ट रिपोर्ट पाते हैं। यह डायग्नोसिस नहीं है; डॉक्टर से बातचीत की तैयारी में मदद मिलती है।</p>"),
        Section(id="steps", level=2, heading="तीन चरणों में ब्लड टेस्ट ऑनलाइन कैसे विश्लेषण करें",
            body_html="<p><strong>चरण 1:</strong> Norya पर जाएं और साइन अप करें या मुफ्त शुरू करें। <strong>चरण 2:</strong> अपना रिज़ल्ट अपलोड करें—PDF, फोटो (JPG/PNG) या टेक्स्ट पेस्ट करके। <strong>चरण 3:</strong> रिपोर्ट पढ़ें और जरूरत हो तो PDF डाउनलोड करें या डॉक्टर के साथ शेयर करें। विश्लेषण ऑटोमैटिक है; आपको संरचित सारांश और अपने मानों की व्याख्या मिलती है।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
            body_html="<p><strong>यह सामग्री केवल सूचनार्थ है और चिकित्सा सलाह, निदान या उपचार नहीं है।</strong> Norya विश्लेषण शैक्षिक है। हमेशा अपने रिज़ल्ट और लक्षण डॉक्टर से चर्चा करें। <a href=\"/hi/upload\">Norya के साथ ब्लड टेस्ट विश्लेषण</a> — अभी शुरू करें।</p>"),
    ]


def _blutwerte_online_sections_ar() -> List[Section]:
    return [
        Section(id="intro", level=2, heading="لماذا تحلل تحاليلك الدموية عبر الإنترنت؟",
            body_html="<p>كثيرون يستلمون تقريراً مليئاً بالاختصارات والأرقام. <strong>تحليل التحاليل الدموية عبر الإنترنت</strong> يساعدك على فهم هذه القيم قبل الموعد التالي أو عندما يكون لديك أسئلة لطبيبك. مع Norya ترفع نتيجتك وتحصل على تقرير واضح مع نطاقات مرجعية وتوصيات مختصرة. هذا ليس تشخيصاً؛ بل يساعدك على الاستعداد لمحادثة الطبيب.</p>"),
        Section(id="steps", level=2, heading="كيف تحلل تحاليلك عبر الإنترنت في ثلاث خطوات",
            body_html="<p><strong>الخطوة 1:</strong> ادخل إلى Norya وسجّل أو ابدأ مجاناً. <strong>الخطوة 2:</strong> ارفع نتيجتك—كـ PDF أو صورة (JPG/PNG) أو بلصق النص. <strong>الخطوة 3:</strong> اقرأ التقرير وحمّله PDF إن لزم أو شاركه مع طبيبك. التحليل آلي؛ تحصل على نظرة منظمة وتفسير لقيمك.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء مسؤولية",
            body_html="<p><strong>هذا المحتوى للمعلومات فقط ولا يغني عن الاستشارة الطبية أو التشخيص أو العلاج.</strong> تحليل Norya تعليمي. ناقش دائماً نتائجك وأعراضك مع الطبيب. <a href=\"/ar/upload\">حلل تحاليلك مع Norya</a> — ابدأ الآن.</p>"),
    ]


_BLUTWERTE_ONLINE_ARTICLE = _article_blutwerte_online_analysieren()


# ——— Second-wave blog articles (long-tail, TR/DE/EN/FR/IT/ES). Cover images reused; Norya badge in template. ———
def _article_b12_low() -> Article:
    """B12 düşüklüğü ne anlama gelir? / What does low B12 mean? — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/vitamin-b12-hero.png"
    return Article(
        id="b12-dusuklugu-ne-anlama-gelir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={
            "tr": "B12 vitamini kan tahlili — Norya",
            "en": "Vitamin B12 blood test — Norya",
            "de": "Vitamin-B12-Bluttest — Norya",
            "fr": "Dosage vitamine B12 — Norya",
            "it": "Esame vitamina B12 — Norya",
            "es": "Análisis vitamina B12 — Norya",
            "he": "בדיקת ויטמין B12 — Norya",
            "hi": "विटामिन B12 ब्लड टेस्ट — Norya",
            "ar": "تحليل فيتامين B12 — Norya",
        },
        category={"tr": "Vitaminlar", "en": "Vitamins", "de": "Vitamine", "fr": "Vitamines", "it": "Vitamine", "es": "Vitaminas", "he": "ויטמינים", "hi": "विटामिन", "ar": "الفيتامينات"},
        slugs={
            "tr": "b12-dusuklugu-ne-anlama-gelir",
            "en": "what-does-low-vitamin-b12-mean",
            "de": "was-bedeutet-niedriger-vitamin-b12-wert",
            "fr": "que-signifie-un-taux-faible-de-vitamine-b12",
            "it": "cosa-significa-valore-basso-vitamina-b12",
            "es": "que-significa-nivel-bajo-vitamina-b12",
            "he": "what-does-low-vitamin-b12-mean",
            "hi": "low-vitamin-b12-level-kya-matlab",
            "ar": "ماذا-يعني-انخفاض-فيتامين-b12",
        },
        titles={
            "tr": "B12 düşüklüğü ne anlama gelir?",
            "en": "What does a low vitamin B12 level mean?",
            "de": "Was bedeutet ein niedriger Vitamin-B12-Wert?",
            "fr": "Que signifie un taux faible de vitamine B12 ?",
            "it": "Cosa significa un valore basso di vitamina B12?",
            "es": "¿Qué significa un nivel bajo de vitamina B12?",
            "he": "מה המשמעות של ערך ויטמין B12 נמוך?",
            "hi": "विटामिन B12 का निम्न स्तर क्या मतलब है?",
            "ar": "ماذا يعني انخفاض مستوى فيتامين B12؟",
        },
        subtitles={
            "tr": "B12 sonucunuz düşük veya sınırda çıktıysa ne yapmalısınız? Referans aralıkları ve sonraki adımlar hakkında kısa rehber.",
            "en": "What to do if your B12 result is low or borderline? A short guide on reference ranges and next steps.",
            "de": "Was tun, wenn Ihr B12-Wert niedrig oder grenzwertig ist? Kurzer Überblick zu Referenzbereichen und nächsten Schritten.",
            "fr": "Que faire si votre B12 est basse ou limite ? Un guide court sur les fourchettes et les prochaines étapes.",
            "it": "Cosa fare se la B12 è bassa o al limite? Breve guida su intervalli di riferimento e passi successivi.",
            "es": "¿Qué hacer si tu B12 está baja o en el límite? Guía breve sobre rangos y próximos pasos.",
            "he": "מה לעשות אם תוצאת B12 נמוכה או בגבול? מדריך קצר על טווחים והמשך.",
            "hi": "B12 निम्न या सीमा पर हो तो क्या करें? संदर्भ सीमा और अगले कदमों पर संक्षिप्त मार्गदर्शन।",
            "ar": "ماذا تفعل إذا كانت نتيجة B12 منخفضة أو على الحد؟ دليل قصير عن النطاقات والخطوات التالية.",
        },
        excerpts={
            "tr": "B12 düşüklüğü tek başına teşhis değildir; nedenleri ve yorumu hekimle görüşülmelidir.",
            "en": "Low B12 alone is not a diagnosis; causes and interpretation should be discussed with a doctor.",
            "de": "Niedriges B12 ist keine Diagnose; Ursachen und Einordnung besprechen Sie mit dem Arzt.",
            "fr": "Un B12 bas seul n'est pas un diagnostic ; causes et interprétation avec le médecin.",
            "it": "B12 bassa da sola non è una diagnosi; cause e interpretazione vanno discusse con il medico.",
            "es": "B12 baja por sí sola no es un diagnóstico; causas e interpretación con el médico.",
            "he": "B12 נמוך לבדו אינו אבחנה; יש לדון בסיבות ובפרשנות עם רופא.",
            "hi": "कम B12 अकेले निदान नहीं है; कारण और व्याख्या डॉक्टर से चर्चा करें।",
            "ar": "انخفاض B12 وحده ليس تشخيصاً؛ ناقش الأسباب والتفسير مع الطبيب.",
        },
        seo_titles={
            "tr": "B12 Düşüklüğü Ne Anlama Gelir? | Norya Blog",
            "en": "What Does a Low Vitamin B12 Level Mean? | Norya Blog",
            "de": "Was bedeutet ein niedriger Vitamin-B12-Wert? | Norya Blog",
            "fr": "Que signifie un taux faible de vitamine B12 ? | Norya Blog",
            "it": "Cosa significa un valore basso di vitamina B12? | Norya Blog",
            "es": "¿Qué significa un nivel bajo de vitamina B12? | Norya Blog",
            "he": "מה המשמעות של ערך B12 נמוך? | Norya Blog",
            "hi": "विटामिन B12 का निम्न स्तर क्या मतलब है? | Norya Blog",
            "ar": "ماذا يعني انخفاض فيتامين B12؟ | Norya Blog",
        },
        seo_descriptions={
            "tr": "B12 düşüklüğü nedenleri, referans aralıkları ve ne zaman doktora gidilmeli. Sadece bilgilendirme amaçlı.",
            "en": "Causes of low B12, reference ranges, and when to see a doctor. For information only.",
            "de": "Ursachen für niedriges B12, Referenzbereiche und wann zum Arzt. Nur zur Information.",
            "fr": "Causes d'un B12 bas, fourchettes de référence et quand consulter. À titre informatif uniquement.",
            "it": "Cause di B12 bassa, intervalli di riferimento e quando rivolgersi al medico. Solo informativo.",
            "es": "Causas de B12 baja, rangos de referencia y cuándo consultar. Solo informativo.",
            "he": "סיבות ל-B12 נמוך, טווחי ייחוס ומתי לפנות לרופא. לצורכי מידע בלבד.",
            "hi": "कम B12 के कारण, संदर्भ सीमा और डॉक्टर से कब मिलें. केवल सूचनार्थ।",
            "ar": "أسباب انخفاض B12 والنطاقات المرجعية ومتى ترى الطبيب. لأغراض إعلامية فقط.",
        },
        sections_by_lang={
            "tr": [
                Section(id="content", level=2, heading="B12 düşüklüğü ne anlama gelir?",
                    body_html="<p>B12 (kobalamin) sinir fonksiyonu, kırmızı kan hücresi yapımı ve DNA sentezi için gereklidir. Tahlilde <strong>referans aralığının altında</strong> veya sınırda bir değer çıkması, beslenme yetersizliği, emilim bozukluğu veya bazı ilaçlar gibi nedenlerle ilişkili olabilir. Tek bir sayı teşhis koymaz; sonucunuzu hekiminiz sizin öykünüz ve gerekirse ek tetkiklerle değerlendirir. Düşük veya sınırda B12 sonucu aldıysanız bir hekime danışın.</p>"),
                Section(id="disclaimer", level=2, heading="Uyarı",
                    body_html="<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> Sonuçlarınızı ve şikayetlerinizi her zaman bir hekimle görüşün. <a href=\"/tr/kan-tahlili-sonucu\">Kan tahlili sonucu anlama</a> · <a href=\"/analyze\">Analiz başlat</a></p>"),
            ],
            "en": [
                Section(id="content", level=2, heading="What does a low vitamin B12 level mean?",
                    body_html="<p>Vitamin B12 (cobalamin) is needed for nerve function, red blood cell formation, and DNA synthesis. A result <strong>below or at the lower end</strong> of the reference range can be linked to diet, absorption issues, or certain medications. A single number does not make a diagnosis; your doctor will interpret your result with your history and any follow-up tests. If you have a low or borderline B12 result, see a doctor.</p>"),
                Section(id="disclaimer", level=2, heading="Disclaimer",
                    body_html="<p><strong>This content is for information only and does not replace medical advice or diagnosis.</strong> Always discuss your results and symptoms with a doctor. <a href=\"/en/blood-test-results\">Understand blood test results</a> · <a href=\"/analyze\">Start analysis</a></p>"),
            ],
            "de": [
                Section(id="content", level=2, heading="Was bedeutet ein niedriger Vitamin-B12-Wert?",
                    body_html="<p>Vitamin B12 (Cobalamin) ist wichtig für Nerven, rote Blutkörperchen und DNA. Ein Wert <strong>unterhalb oder am unteren Rand</strong> des Referenzbereichs kann an Ernährung, Aufnahme oder Medikamenten liegen. Ein einzelner Wert ist keine Diagnose; Ihr Arzt ordnet das Ergebnis mit Anamnese und ggf. weiteren Tests ein. Bei niedrigem oder grenzwertigem B12 bitte zum Arzt.</p>"),
                Section(id="disclaimer", level=2, heading="Hinweis",
                    body_html="<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung oder Diagnose.</strong> Besprechen Sie Ergebnisse und Beschwerden immer mit einem Arzt. <a href=\"/de/blutwerte-verstehen\">Blutwerte verstehen</a> · <a href=\"/analyze\">Analyse starten</a></p>"),
            ],
            "fr": [
                Section(id="content", level=2, heading="Que signifie un taux faible de vitamine B12 ?",
                    body_html="<p>La vitamine B12 (cobalamine) est nécessaire aux nerfs, aux globules rouges et à l’ADN. Un résultat <strong>sous ou en bas</strong> de la fourchette de référence peut être lié à l’alimentation, à l’absorption ou à certains médicaments. Un chiffre seul ne fait pas un diagnostic ; votre médecin interprétera le résultat avec votre histoire et d’éventuels examens. En cas de B12 basse ou limite, consultez un médecin.</p>"),
                Section(id="disclaimer", level=2, heading="Avertissement",
                    body_html="<p><strong>Ce contenu est à titre informatif uniquement et ne remplace pas un avis ou diagnostic médical.</strong> Discutez toujours de vos résultats et symptômes avec un médecin. <a href=\"/analyze\">Lancer l'analyse</a></p>"),
            ],
            "it": [
                Section(id="content", level=2, heading="Cosa significa un valore basso di vitamina B12?",
                    body_html="<p>La vitamina B12 (cobalamina) serve per nervi, globuli rossi e DNA. Un valore <strong>sotto o al limite inferiore</strong> dell’intervallo di riferimento può dipendere da dieta, assorbimento o farmaci. Un solo numero non fa diagnosi; il medico valuterà il risultato con la tua storia e eventuali controlli. In caso di B12 bassa o limite, rivolgiti al medico.</p>"),
                Section(id="disclaimer", level=2, heading="Disclaimer",
                    body_html="<p><strong>Questo contenuto è solo informativo e non sostituisce parere o diagnosi medica.</strong> Discuti sempre risultati e sintomi con un medico. <a href=\"/analyze\">Avvia analisi</a></p>"),
            ],
            "es": [
                Section(id="content", level=2, heading="¿Qué significa un nivel bajo de vitamina B12?",
                    body_html="<p>La vitamina B12 (cobalamina) es necesaria para nervios, glóbulos rojos y ADN. Un resultado <strong>por debajo o en el límite</strong> del rango de referencia puede deberse a dieta, absorción o medicación. Un solo valor no es un diagnóstico; tu médico interpretará el resultado con tu historia y pruebas. Si tienes B12 baja o en el límite, consulta al médico.</p>"),
                Section(id="disclaimer", level=2, heading="Aviso",
                    body_html="<p><strong>Este contenido es solo informativo y no sustituye consejo ni diagnóstico médico.</strong> Siempre comenta resultados y síntomas con un médico. <a href=\"/analyze\">Iniciar análisis</a></p>"),
            ],
            "he": [
                Section(id="content", level=2, heading="מה המשמעות של ערך ויטמין B12 נמוך?",
                    body_html="<p>ויטמין B12 (קובלמין) נחוץ לתפקוד עצבים, יצירת תאי דם אדומים ו-DNA. תוצאה <strong>מתחת או בגבול התחתון</strong> של טווח הייחוס יכולה להיות קשורה לתזונה, ספיגה או תרופות. מספר בודד אינו אבחנה; הרופא יפרש את התוצאה עם ההיסטוריה והמעקב. אם יש לך B12 נמוך או בגבול — פנה לרופא.</p>"),
                Section(id="disclaimer", level=2, heading="הודעה",
                    body_html="<p><strong>תוכן זה למידע בלבד ואינו מחליף ייעוץ או אבחנה רפואית.</strong> תמיד לדון בתוצאות ובתסמינים עם רופא. <a href=\"/he/blog\">בלוג</a> · <a href=\"/analyze\">התחל ניתוח</a></p>"),
            ],
            "hi": [
                Section(id="content", level=2, heading="विटामिन B12 का निम्न स्तर क्या मतलब है?",
                    body_html="<p>विटामिन B12 (कोबालामिन) नसों, लाल रक्त कोशिकाओं और DNA के लिए जरूरी है। संदर्भ सीमा के <strong>नीचे या सीमा पर</strong> परिणाम आहार, अवशोषण या दवाओं से जुड़ा हो सकता है। एक अकेला नंबर निदान नहीं है; डॉक्टर आपके इतिहास और फॉलो-अप टेस्ट से परिणाम की व्याख्या करेंगे। कम या सीमा पर B12 हो तो डॉक्टर से मिलें।</p>"),
                Section(id="disclaimer", level=2, heading="अस्वीकरण",
                    body_html="<p><strong>यह सामग्री केवल जानकारी के लिए है और चिकित्सा सलाह या निदान का विकल्प नहीं।</strong> हमेशा परिणाम और लक्षण डॉक्टर से चर्चा करें। <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>"),
            ],
            "ar": [
                Section(id="content", level=2, heading="ماذا يعني انخفاض مستوى فيتامين B12؟",
                    body_html="<p>فيتامين B12 (كوبالامين) ضروري للأعصاب وخلايا الدم الحمراء والحمض النووي. نتيجة <strong>أقل أو عند الحد الأدنى</strong> من النطاق المرجعي قد ترتبط بالنظام الغذائي أو الامتصاص أو أدوية معينة. الرقم وحده لا يشخّص؛ الطبيب يفسر نتيجتك مع تاريخك وأي فحوصات متابعة. إن كانت B12 منخفضة أو على الحد، راجع الطبيب.</p>"),
                Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                    body_html="<p><strong>هذا المحتوى للمعلومات فقط ولا يغني عن الاستشارة أو التشخيص الطبي.</strong> ناقش دائماً نتائجك وأعراضك مع الطبيب. <a href=\"/analyze\">بدء التحليل</a></p>"),
            ],
        },
    )


_ARTICLE_B12_LOW = _article_b12_low()


def _article_vitamin_d_interpret() -> Article:
    """D vitamini sonucu nasıl yorumlanır? / Vitamin D test results — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/vitamin-d-hero.png"
    return Article(
        id="d-vitamini-sonucu-nasil-yorumlanir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={"tr": "D vitamini kan tahlili — Norya", "en": "Vitamin D blood test — Norya", "de": "Vitamin-D-Bluttest — Norya", "fr": "Dosage vitamine D — Norya", "it": "Esame vitamina D — Norya", "es": "Análisis vitamina D — Norya", "he": "בדיקת ויטמין D — Norya", "hi": "विटामिन D ब्लड टेस्ट — Norya", "ar": "تحليل فيتامين D — Norya"},
        category={"tr": "Vitaminlar", "en": "Vitamins", "de": "Vitamine", "fr": "Vitamines", "it": "Vitamine", "es": "Vitaminas", "he": "ויטמינים", "hi": "विटामिन", "ar": "الفيتامينات"},
        slugs={"tr": "d-vitamini-sonucu-nasil-yorumlanir", "en": "how-to-understand-vitamin-d-test-results", "de": "vitamin-d-verstehen-was-sagen-die-werte-aus", "fr": "vitamine-d-comprendre-les-resultats", "it": "come-interpretare-risultato-vitamina-d", "es": "como-interpretar-resultado-vitamina-d", "he": "how-to-understand-vitamin-d-test-results", "hi": "vitamin-d-result-kaise-samjhe", "ar": "kayf-tafham-natijat-fitamin-d"},
        titles={"tr": "D vitamini sonucu nasıl yorumlanır?", "en": "How to understand vitamin D test results", "de": "Vitamin D verstehen: Was sagen die Werte aus?", "fr": "Comprendre les résultats de la vitamine D", "it": "Come interpretare il risultato della vitamina D?", "es": "¿Cómo interpretar el resultado de vitamina D?", "he": "איך להבין תוצאות בדיקת ויטמין D?", "hi": "विटामिन D टेस्ट रिज़ल्ट कैसे समझें?", "ar": "كيف تفهم نتائج تحليل فيتامين D؟"},
        subtitles={"tr": "D vitamini (25-OH) referans aralıkları ve sonucunuzu nasıl değerlendireceğinize dair kısa rehber.", "en": "Vitamin D (25-OH) reference ranges and a short guide to interpreting your result.", "de": "Vitamin D (25-OH): Referenzbereiche und kurze Einordnung Ihres Befunds.", "fr": "Vitamine D (25-OH) : fourchettes de référence et comment interpréter votre résultat.", "it": "Vitamina D (25-OH): intervalli di riferimento e come interpretare il risultato.", "es": "Vitamina D (25-OH): rangos de referencia y cómo interpretar tu resultado.", "he": "טווחי ייחוס לוויטמין D (25-OH) ומדריך קצר לפרשנות התוצאה.", "hi": "विटामिन D (25-OH) संदर्भ सीमा और अपने परिणाम की व्याख्या के लिए संक्षिप्त मार्गदर्शन।", "ar": "نطاقات فيتامين D (25-OH) المرجعية ودليل قصير لتفسير نتيجتك."},
        excerpts={"tr": "D vitamini sonucu laboratuvara göre değişir; yorumu hekimle yapılmalıdır.", "en": "Vitamin D results vary by lab; interpretation should be done with a doctor.", "de": "Vitamin-D-Werte sind laborabhängig; die Einordnung erfolgt mit dem Arzt.", "fr": "Les résultats vitamine D varient selon le laboratoire ; interprétation avec le médecin.", "it": "I risultati della vitamina D variano da laboratorio; interpretazione con il medico.", "es": "Los resultados de vitamina D varían por laboratorio; interpretación con el médico.", "he": "תוצאות ויטמין D משתנות לפי מעבדה; הפרשנות עם רופא.", "hi": "विटामिन D परिणाम लैब के अनुसार भिन्न होते हैं; व्याख्या डॉक्टर से करवाएं।", "ar": "نتائج فيتامين D تختلف حسب المختبر؛ التفسير مع الطبيب."},
        seo_titles={"tr": "D Vitamini Sonucu Nasıl Yorumlanır? | Norya Blog", "en": "How to Understand Vitamin D Test Results | Norya Blog", "de": "Vitamin D verstehen: Was sagen die Werte aus? | Norya Blog", "fr": "Comprendre les résultats vitamine D | Norya Blog", "it": "Come interpretare il risultato della vitamina D | Norya Blog", "es": "Cómo interpretar el resultado de vitamina D | Norya Blog", "he": "איך להבין תוצאות בדיקת ויטמין D | Norya Blog", "hi": "विटामिन D टेस्ट रिज़ल्ट कैसे समझें | Norya Blog", "ar": "كيف تفهم نتائج تحليل فيتامين D | Norya Blog"},
        seo_descriptions={"tr": "D vitamini (25-OH) referans aralıkları ve yorumlama. Bilgilendirme amaçlı.", "en": "Vitamin D (25-OH) reference ranges and interpretation. For information only.", "de": "Vitamin D (25-OH): Referenzbereiche und Einordnung. Nur zur Information.", "fr": "Vitamine D (25-OH) : fourchettes et interprétation. À titre informatif.", "it": "Vitamina D (25-OH): intervalli e interpretazione. Solo informativo.", "es": "Vitamina D (25-OH): rangos e interpretación. Solo informativo.", "he": "טווחי ויטמין D (25-OH) ופרשנות. למידע בלבד.", "hi": "विटामिन D (25-OH) संदर्भ सीमा और व्याख्या. केवल सूचनार्थ।", "ar": "نطاقات فيتامين D (25-OH) وتفسيرها. لأغراض إعلامية فقط."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="D vitamini sonucu nasıl yorumlanır?", body_html="<p>Kandaki <strong>25-OH D vitamini</strong> (kalsidiol) en sık ölçülen göstergedir. Referans aralıkları laboratuvara göre değişir; birçok laboratuvar \"yetersiz\" veya \"eksik\" için alt sınır kullanır. Sonucunuzu raporunuzdaki referans aralığıyla birlikte değerlendirin. D vitamini düşüklüğü kemik sağlığı ve bağışıklıkla ilişkili olabilir; takviye ve doz hekim tarafından belirlenmelidir.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır.</strong> Sonuçlarınızı hekimle görüşün. <a href=\"/tr/kan-degerleri-anlama\">Kan değerleri anlama</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="How to understand vitamin D test results", body_html="<p><strong>25-OH vitamin D</strong> (calcidiol) in blood is the most common measure. Reference ranges vary by lab; many labs define \"insufficient\" or \"deficient\" with a lower cutoff. Interpret your result using the range on your report. Low vitamin D may relate to bone health and immunity; supplementation and dose should be decided by a doctor.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>This content is for information only.</strong> Discuss your results with a doctor. <a href=\"/en/understand-lab-results\">Understand lab results</a> · <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Vitamin D verstehen: Was sagen die Werte aus?", body_html="<p><strong>25-OH-Vitamin D</strong> (Calcidiol) im Blut wird am häufigsten gemessen. Referenzbereiche sind laborabhängig; viele Labore geben Untergrenzen für \"insuffizient\" oder \"Mangel\" an. Ordnen Sie Ihren Wert anhand des Referenzbereichs auf dem Befund ein. Niedriges Vitamin D kann mit Knochen und Immunität zusammenhängen; Einnahme und Dosis legt der Arzt fest.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> Besprechen Sie Ihren Befund mit dem Arzt. <a href=\"/de/laborwerte-verstehen\">Laborwerte verstehen</a> · <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Comprendre les résultats de la vitamine D", body_html="<p>La <strong>25-OH vitamine D</strong> (calcidiol) dans le sang est le dosage le plus courant. Les fourchettes varient selon le laboratoire. Interprétez votre résultat avec la fourchette indiquée sur le compte-rendu. Un taux bas peut concerner les os et l’immunité ; supplémentation et dose à voir avec le médecin.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif uniquement.</strong> Discutez de vos résultats avec un médecin. <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Come interpretare il risultato della vitamina D", body_html="<p>La <strong>25-OH vitamina D</strong> (calcidiolo) nel sangue è il dosaggio più usato. Gli intervalli di riferimento variano da laboratorio. Interpreta il risultato con l’intervallo sul referto. Valori bassi possono riguardare ossa e immunità; integrazione e dose vanno decise dal medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> Discuti i risultati con il medico. <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="Cómo interpretar el resultado de vitamina D", body_html="<p>La <strong>25-OH vitamina D</strong> (calcidiol) en sangre es la medida más habitual. Los rangos de referencia varían por laboratorio. Interpreta tu resultado con el rango de tu informe. Un nivel bajo puede relacionarse con huesos e inmunidad; suplementación y dosis deben determinarlas el médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> Comenta tus resultados con un médico. <a href=\"/analyze\">Analizar</a></p>")],
            "he": [Section(id="content", level=2, heading="איך להבין תוצאות בדיקת ויטמין D", body_html="<p><strong>25-OH ויטמין D</strong> (קלצידיול) בדם הוא המדד הנפוץ ביותר. טווחי ייחוס משתנים לפי מעבדה. פרש את התוצאה לפי הטווח בדו\"ח. ויטמין D נמוך יכול להיות קשור לעצמות ולמערכת החיסון; מינון ותוספים ייקבעו על ידי רופא.</p>"), Section(id="disclaimer", level=2, heading="הודעה", body_html="<p><strong>למידע בלבד.</strong> יש לדון בתוצאות עם רופא. <a href=\"/analyze\">התחל ניתוח</a></p>")],
            "hi": [Section(id="content", level=2, heading="विटामिन D टेस्ट रिज़ल्ट कैसे समझें", body_html="<p>खून में <strong>25-OH विटामिन D</strong> (कैल्सिडिओल) सबसे आम माप है। संदर्भ सीमाएं लैब के अनुसार अलग होती हैं। अपनी रिपोर्ट की सीमा से अपना परिणाम समझें। कम विटामिन D हड्डी और इम्युनिटी से जुड़ा हो सकता है; सप्लीमेंट और खुराक डॉक्टर तय करें।</p>"), Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html="<p><strong>केवल सूचनार्थ।</strong> परिणाम डॉक्टर से चर्चा करें। <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>")],
            "ar": [Section(id="content", level=2, heading="كيف تفهم نتائج تحليل فيتامين D", body_html="<p><strong>25-OH فيتامين D</strong> (كالسيديول) في الدم هو القياس الأكثر شيوعاً. النطاقات المرجعية تختلف حسب المختبر. فسّر نتيجتك باستخدام النطاق في تقريرك. انخفاض فيتامين D قد يرتبط بالعظام والمناعة؛ المكملات والجرعة يحددها الطبيب.</p>"), Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html="<p><strong>للمعلومات فقط.</strong> ناقش نتائجك مع الطبيب. <a href=\"/analyze\">بدء التحليل</a></p>")],
        },
    )


_ARTICLE_VITAMIN_D_INTERPRET = _article_vitamin_d_interpret()


def _article_iron_deficiency_blood() -> Article:
    """Demir eksikliği hangi kan değerlerinde görülür? / How to spot iron deficiency — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/ferritin-hero.png"
    return Article(
        id="demir-eksikligi-hangi-kan-degerlerinde",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={"tr": "Demir ve ferritin kan tahlili — Norya", "en": "Iron and ferritin blood test — Norya", "de": "Eisen und Ferritin Bluttest — Norya", "fr": "Fer et ferritine — Norya", "it": "Ferro e ferritina — Norya", "es": "Hierro y ferritina — Norya", "he": "בדיקת ברזל ופריטין — Norya", "hi": "आयरन और फेरिटिन ब्लड टेस्ट — Norya", "ar": "تحليل الحديد والفرتين — Norya"},
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "es": "Biomarcadores", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"},
        slugs={"tr": "demir-eksikligi-hangi-kan-degerlerinde-gorulur", "en": "how-to-spot-iron-deficiency-in-blood-results", "de": "eisenmangel-im-blutbild-erkennen", "fr": "reconnaitre-carence-fer-resultats-sang", "it": "come-riconoscere-carenza-ferro-esami", "es": "como-detectar-deficiencia-hierro-sangre", "he": "how-to-spot-iron-deficiency-in-blood-results", "hi": "blood-results-mein-iron-deficiency-kaise-pehchane", "ar": "kayf-tatashaeh-naqs-alhadid-fi-nataij-aldam"},
        titles={"tr": "Demir eksikliği hangi kan değerlerinde görülür?", "en": "How to spot iron deficiency in blood results", "de": "Eisenmangel im Blutbild erkennen", "fr": "Reconnaître une carence en fer dans les résultats", "it": "Come riconoscere la carenza di ferro negli esami", "es": "Cómo detectar la deficiencia de hierro en sangre", "he": "איך לזהות חוסר ברזל בתוצאות הדם?", "hi": "ब्लड रिज़ल्ट में आयरन की कमी कैसे पहचानें?", "ar": "كيف تتعرف على نقص الحديد في نتائج الدم؟"},
        subtitles={"tr": "Ferritin, hemoglobin, MCV ve diğer değerler demir eksikliğinde nasıl değişir? Kısa rehber.", "en": "How ferritin, haemoglobin, MCV and other values change in iron deficiency. A short guide.", "de": "Wie sich Ferritin, Hämoglobin, MCV bei Eisenmangel verändern. Kurzer Überblick.", "fr": "Comment la ferritine, l'hémoglobine et le VGM changent en cas de carence. Guide court.", "it": "Come cambiano ferritina, emoglobina e MCV in caso di carenza. Guida breve.", "es": "Cómo cambian ferritina, hemoglobina y VCM en la deficiencia de hierro. Guía breve.", "he": "איך פריטין, המוגלובין ו-MCV משתנים בחוסר ברזל. מדריך קצר.", "hi": "आयरन की कमी में फेरिटिन, हीमोग्लोबिन और MCV कैसे बदलते हैं। संक्षिप्त मार्गदर्शन।", "ar": "كيف تتغير الفيريتين والهيموغلوبين وMCV في نقص الحديد. دليل قصير."},
        excerpts={"tr": "Demir eksikliği tek bir değerle teşhis edilmez; ferritin ve tam kan sayımı birlikte değerlendirilir.", "en": "Iron deficiency is not diagnosed by one value; ferritin and full blood count are evaluated together.", "de": "Eisenmangel wird nicht durch einen Wert allein festgestellt; Ferritin und Blutbild zusammen.", "fr": "La carence en fer ne se diagnostique pas sur un seul chiffre ; ferritine et NFS ensemble.", "it": "La carenza di ferro non si diagnostica con un solo valore; ferritina ed emocromo insieme.", "es": "La deficiencia de hierro no se diagnostica con un solo valor; ferritina y hemograma juntos.", "he": "חוסר ברזל לא מאובחן לפי ערך אחד; פריטין וספירת דם מלאה ביחד.", "hi": "आयरन की कमी एक मान से निदान नहीं होती; फेरिटिन और पूर्ण रक्त गणना साथ में।", "ar": "نقص الحديد لا يُشخّص بقيمة واحدة؛ الفيريتين وعدّ الدم معاً."},
        seo_titles={"tr": "Demir Eksikliği Hangi Kan Değerlerinde Görülür? | Norya Blog", "en": "How to Spot Iron Deficiency in Blood Results | Norya Blog", "de": "Eisenmangel im Blutbild erkennen | Norya Blog", "fr": "Reconnaître une carence en fer dans les résultats | Norya Blog", "it": "Come riconoscere la carenza di ferro negli esami | Norya Blog", "es": "Cómo detectar la deficiencia de hierro en sangre | Norya Blog", "he": "איך לזהות חוסר ברזל בתוצאות הדם | Norya Blog", "hi": "ब्लड रिज़ल्ट में आयरन की कमी कैसे पहचानें | Norya Blog", "ar": "كيف تتعرف على نقص الحديد في نتائج الدم | Norya Blog"},
        seo_descriptions={"tr": "Ferritin, hemoglobin ve MCV ile demir eksikliği. Bilgilendirme amaçlı.", "en": "Ferritin, haemoglobin and MCV in iron deficiency. For information only.", "de": "Ferritin, Hämoglobin und MCV bei Eisenmangel. Nur zur Information.", "fr": "Ferritine, hémoglobine et VGM en cas de carence. À titre informatif.", "it": "Ferritina, emoglobina e MCV nella carenza di ferro. Solo informativo.", "es": "Ferritina, hemoglobina y VCM en la deficiencia de hierro. Solo informativo.", "he": "פריטין, המוגלובין ו-MCV בחוסר ברזל. למידע בלבד.", "hi": "आयरन की कमी में फेरिटिन, हीमोग्लोबिन और MCV. केवल सूचनार्थ।", "ar": "الفيريتين والهيموغلوبين وMCV في نقص الحديد. لأغراض إعلامية فقط."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Hangi kan değerleri?", body_html="<p><strong>Ferritin</strong> vücut demir depolarını yansıtır; düşük ferritin demir eksikliğini destekler. <strong>Hemoglobin</strong> (HGB) düşükse anemi olabilir. <strong>MCV</strong> (ortalama hücre hacmi) demir eksikliği anemisinde genellikle düşük veya normaldir. Tek başına bir değer teşhis koymaz; hekim tahlilleri birlikte yorumlar. Demir takviyesi hekim önerisiyle kullanılmalıdır.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> Sonuçlarınızı hekimle görüşün. <a href=\"/tr/hemogram-sonucu\">Hemogram sonucu</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="Which blood values?", body_html="<p><strong>Ferritin</strong> reflects body iron stores; low ferritin supports iron deficiency. <strong>Haemoglobin</strong> (HGB) may be low in anaemia. <strong>MCV</strong> (mean cell volume) is often low or normal in iron-deficiency anaemia. No single value makes a diagnosis; your doctor will interpret tests together. Iron supplements should be used on medical advice.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Discuss your results with a doctor. <a href=\"/en/blood-test-results\">Blood test results</a> · <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Welche Blutwerte?", body_html="<p><strong>Ferritin</strong> spiegelt die Eisenspeicher wider; niedriges Ferritin spricht für Eisenmangel. <strong>Hämoglobin</strong> (HGB) kann bei Anämie erniedrigt sein. <strong>MCV</strong> ist bei Eisenmangelanämie oft niedrig oder normal. Ein Wert allein ergibt keine Diagnose; der Arzt wertet die Befunde gemeinsam aus. Eisenpräparate nur nach ärztlicher Rücksprache.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> Befund mit dem Arzt besprechen. <a href=\"/de/blutwerte-verstehen\">Blutwerte</a> · <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Quelles valeurs sanguines?", body_html="<p>La <strong>ferritine</strong> reflète les réserves en fer ; une ferritine basse oriente vers une carence. L’<strong>hémoglobine</strong> (HGB) peut être basse en cas d’anémie. Le <strong>VGM</strong> est souvent bas ou normal en cas d’anémie ferriprive. Un seul chiffre ne fait pas le diagnostic ; le médecin interprète l’ensemble. Supplémentation en fer sur avis médical.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> Discutez de vos résultats avec un médecin. <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Quali valori del sangue?", body_html="<p>La <strong>ferritina</strong> riflette le riserve di ferro; ferritina bassa suggerisce carenza. L’<strong>emoglobina</strong> (HGB) può essere bassa in caso di anemia. L’<strong>MCV</strong> è spesso basso o normale nell’anemia da carenza di ferro. Un solo valore non fa diagnosi; il medico valuta gli esami insieme. Integratori di ferro su consiglio medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> Discuti i risultati con il medico. <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="¿Qué valores en sangre?", body_html="<p>La <strong>ferritina</strong> refleja los depósitos de hierro; ferritina baja apoya deficiencia. La <strong>hemoglobina</strong> (HGB) puede estar baja en anemia. El <strong>VCM</strong> suele ser bajo o normal en la anemia ferropénica. Un solo valor no da el diagnóstico; el médico interpreta las pruebas juntas. Suplementos de hierro bajo indicación médica.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> Comenta tus resultados con un médico. <a href=\"/analyze\">Analizar</a></p>")],
            "he": [Section(id="content", level=2, heading="אילו ערכי דם?", body_html="<p><strong>פריטין</strong> משקף מאגרי ברזל; פריטין נמוך תומך בחוסר ברזל. <strong>המוגלובין</strong> (HGB) יכול להיות נמוך באנמיה. <strong>MCV</strong> לרוב נמוך או תקין באנמיה מחוסר ברזל. ערך בודד לא קובע אבחנה; הרופא יפרש את הבדיקות יחד. תוספי ברזל בהמלצת רופא.</p>"), Section(id="disclaimer", level=2, heading="הודעה", body_html="<p><strong>למידע בלבד.</strong> יש לדון בתוצאות עם רופא. <a href=\"/analyze\">התחל ניתוח</a></p>")],
            "hi": [Section(id="content", level=2, heading="कौन से ब्लड वैल्यू?", body_html="<p><strong>फेरिटिन</strong> शरीर में आयरन स्टोर दर्शाता है; कम फेरिटिन आयरन की कमी का संकेत। <strong>हीमोग्लोबिन</strong> (HGB) एनीमिया में कम हो सकता है। <strong>MCV</strong> आयरन की कमी वाली एनीमिया में अक्सर कम या सामान्य। एक अकेला मान निदान नहीं है; डॉक्टर सभी टेस्ट एक साथ देखेंगे। आयरन सप्लीमेंट डॉक्टर की सलाह से।</p>"), Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html="<p><strong>केवल सूचनार्थ।</strong> परिणाम डॉक्टर से चर्चा करें। <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>")],
            "ar": [Section(id="content", level=2, heading="أي قيم الدم؟", body_html="<p><strong>الفيريتين</strong> يعكس مخزون الحديد؛ انخفاضه يدعم نقص الحديد. <strong>الهيموغلوبين</strong> (HGB) قد يكون منخفضاً في فقر الدم. <strong>MCV</strong> غالباً منخفض أو طبيعي في فقر الدم بعوز الحديد. قيمة واحدة لا تشخّص؛ الطبيب يفسر التحاليل معاً. مكملات الحديد بوصفة الطبيب.</p>"), Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html="<p><strong>للمعلومات فقط.</strong> ناقش نتائجك مع الطبيب. <a href=\"/analyze\">بدء التحليل</a></p>")],
        },
    )


def _article_alt_ast_high() -> Article:
    """ALT ve AST yüksekliği / High ALT and AST — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/crp-hero.png"
    return Article(
        id="alt-ast-yuksekligi-neyi-gosterir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={"tr": "Karaciğer enzimleri ALT AST — Norya", "en": "Liver enzymes ALT AST — Norya", "de": "Leberenzyme ALT AST — Norya", "fr": "Enzymes hépatiques ALT AST — Norya", "it": "Enzimi epatici ALT AST — Norya", "es": "Enzimas hepáticas ALT AST — Norya", "he": "אנזימי כבד ALT AST — Norya", "hi": "लिवर एंजाइम ALT AST — Norya", "ar": "إنزيمات الكبد ALT AST — Norya"},
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "es": "Biomarcadores", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"},
        slugs={"tr": "alt-ve-ast-yuksekligi-neyi-gosterir", "en": "what-do-high-alt-and-ast-levels-mean", "de": "was-bedeuten-erhoehte-alt-und-ast-werte", "fr": "que-signifient-alt-ast-eleves", "it": "cosa-significano-alt-ast-alti", "es": "que-significan-alt-y-ast-altos", "he": "what-do-high-alt-and-ast-levels-mean", "hi": "high-alt-ast-levels-ka-matlab", "ar": "ma-dha-taani-mustawayat-alt-wa-ast-alalia"},
        titles={"tr": "ALT ve AST yüksekliği neyi gösterir?", "en": "What do high ALT and AST levels mean?", "de": "Was bedeuten erhöhte ALT- und AST-Werte?", "fr": "Que signifient des ALT et AST élevés ?", "it": "Cosa significano ALT e AST alti?", "es": "¿Qué significan ALT y AST altos?", "he": "מה משמעות ערכי ALT ו-AST גבוהים?", "hi": "ALT और AST हाई लेवल का क्या मतलब है?", "ar": "ماذا تعني ارتفاع ALT وAST؟"},
        subtitles={"tr": "Karaciğer enzimleri yüksekliği nedenleri ve sonucunuzu nasıl değerlendireceğinize dair kısa rehber.", "en": "Causes of raised liver enzymes and a short guide to interpreting your result.", "de": "Ursachen erhöhter Leberwerte und kurze Einordnung Ihres Befunds.", "fr": "Causes des enzymes hépatiques élevées et comment interpréter votre résultat.", "it": "Cause di enzimi epatici alti e come interpretare il risultato.", "es": "Causas de ALT y AST altos y cómo interpretar tu resultado.", "he": "סיבות לערכי כבד גבוהים ומדריך קצר לפרשנות.", "hi": "लिवर एंजाइम बढ़ने के कारण और अपने परिणाम की व्याख्या।", "ar": "أسباب ارتفاع إنزيمات الكبد وكيفية تفسير نتيجتك."},
        excerpts={"tr": "ALT ve AST yüksekliği tek başına teşhis değildir; hekim öykü ve gerekirse ek tetkiklerle değerlendirir.", "en": "High ALT and AST alone are not a diagnosis; your doctor will assess with history and further tests if needed.", "de": "Erhöhte ALT/AST sind keine Diagnose; der Arzt beurteilt mit Anamnese und ggf. weiteren Tests.", "fr": "ALT et AST élevés seuls ne sont pas un diagnostic ; le médecin évalue avec l'histoire et examens.", "it": "ALT e AST alti da soli non sono una diagnosi; il medico valuta con anamnesi e eventuali esami.", "es": "ALT y AST altos por sí solos no son un diagnóstico; el médico valora con historia y pruebas.", "he": "ALT ו-AST גבוהים לבדם אינם אבחנה; הרופא יבדוק עם אנמנזה ובדיקות.", "hi": "ALT और AST अकेले निदान नहीं हैं; डॉक्टर इतिहास और टेस्ट से आंकलन करेंगे।", "ar": "ارتفاع ALT وAST وحدهما ليس تشخيصاً؛ الطبيب يقيّم مع التاريخ والفحوصات."},
        seo_titles={"tr": "ALT ve AST Yüksekliği Neyi Gösterir? | Norya Blog", "en": "What Do High ALT and AST Levels Mean? | Norya Blog", "de": "Was bedeuten erhöhte ALT- und AST-Werte? | Norya Blog", "fr": "Que signifient des ALT et AST élevés ? | Norya Blog", "it": "Cosa significano ALT e AST alti? | Norya Blog", "es": "¿Qué significan ALT y AST altos? | Norya Blog", "he": "מה משמעות ערכי ALT ו-AST גבוהים | Norya Blog", "hi": "ALT और AST हाई लेवल का क्या मतलब | Norya Blog", "ar": "ماذا تعني ارتفاع ALT وAST | Norya Blog"},
        seo_descriptions={"tr": "Karaciğer enzimleri ALT ve AST yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Causes of high ALT and AST liver enzymes. For information only.", "de": "Ursachen für erhöhte Leberenzyme ALT und AST. Nur zur Information.", "fr": "Causes des ALT et AST élevés. À titre informatif.", "it": "Cause di ALT e AST alti. Solo informativo.", "es": "Causas de ALT y AST altos. Solo informativo.", "he": "סיבות ל-ALT ו-AST גבוהים. למידע בלבד.", "hi": "ALT और AST हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع ALT وAST. لأغراض إعلامية فقط."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="ALT ve AST yüksekliği neyi gösterir?", body_html="<p><strong>ALT</strong> ve <strong>AST</strong> karaciğer hücrelerinde bulunan enzimlerdir; hasar veya stres durumunda kanda yükselebilir. Hafif yükselmeler bazen ilaç, yağlanma veya enfeksiyonla ilişkili olabilir. Tek başına sayı teşhis koymaz; hekiminiz öykünüz, muayene ve gerekirse ek tetkiklerle değerlendirir. Belirgin veya sürekli yükseklikte mutlaka hekime danışın.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> Sonuçlarınızı hekimle görüşün. <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What do high ALT and AST levels mean?", body_html="<p><strong>ALT</strong> and <strong>AST</strong> are enzymes found in liver cells; they can rise in blood with injury or stress. Mild rises may be linked to medication, fatty liver, or infection. A number alone does not make a diagnosis; your doctor will assess with your history, examination, and further tests if needed. Always see a doctor for marked or persistent elevation.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Discuss your results with a doctor. <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Was bedeuten erhöhte ALT- und AST-Werte?", body_html="<p><strong>ALT</strong> und <strong>AST</strong> sind Enzyme in Leberzellen; bei Schädigung oder Belastung können sie im Blut ansteigen. Leichte Erhöhungen können z. B. durch Medikamente, Fettleber oder Infektionen bedingt sein. Ein Wert allein ist keine Diagnose; Ihr Arzt beurteilt mit Anamnese, Untersuchung und ggf. weiteren Tests. Bei deutlicher oder anhaltender Erhöhung zum Arzt.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> Befund mit dem Arzt besprechen. <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Que signifient des ALT et AST élevés ?", body_html="<p>Les <strong>ALT</strong> et <strong>AST</strong> sont des enzymes hépatiques ; elles peuvent augmenter dans le sang en cas de souffrance ou de stress du foie. Une légère élévation peut être liée à un médicament, une stéatose ou une infection. Un chiffre seul ne fait pas un diagnostic ; le médecin évalue avec l’histoire, l’examen et d’éventuels examens. En cas d’élévation marquée ou persistante, consultez.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> Discutez de vos résultats avec un médecin. <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Cosa significano ALT e AST alti?", body_html="<p><strong>ALT</strong> e <strong>AST</strong> sono enzimi presenti nelle cellule del fegato; possono aumentare nel sangue in caso di danno o stress. Lievi aumenti possono dipendere da farmaci, steatosi o infezioni. Un solo valore non fa diagnosi; il medico valuta con anamnesi, visita ed eventuali esami. In caso di aumento marcato o persistente, rivolgersi al medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> Discuti i risultati con il medico. <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="¿Qué significan ALT y AST altos?", body_html="<p><strong>ALT</strong> y <strong>AST</strong> son enzimas del hígado; pueden subir en sangre con daño o estrés hepático. Elevaciones leves pueden relacionarse con medicación, hígado graso o infección. Un solo valor no es un diagnóstico; el médico valora con tu historia, exploración y pruebas si hace falta. Ante elevación marcada o persistente, consulta al médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> Comenta tus resultados con un médico. <a href=\"/analyze\">Analizar</a></p>")],
            "he": [Section(id="content", level=2, heading="מה משמעות ערכי ALT ו-AST גבוהים?", body_html="<p><strong>ALT</strong> ו-<strong>AST</strong> הם אנזימים בתאי הכבד; הם יכולים לעלות בדם בעקבות נזק או עקה. עלייה קלה יכולה להיות קשורה לתרופות, שומן בכבד או זיהום. ערך בודד לא קובע אבחנה; הרופא יבדוק עם אנמנזה, בדיקה ובדיקות נוספות. בעלייה בולטת או מתמשכת — לפנות לרופא.</p>"), Section(id="disclaimer", level=2, heading="הודעה", body_html="<p><strong>למידע בלבד.</strong> יש לדון בתוצאות עם רופא. <a href=\"/analyze\">התחל ניתוח</a></p>")],
            "hi": [Section(id="content", level=2, heading="ALT और AST हाई लेवल का क्या मतलब?", body_html="<p><strong>ALT</strong> और <strong>AST</strong> लिवर सेल में एंजाइम हैं; चोट या स्ट्रेस में खून में बढ़ सकते हैं। हल्की बढ़ोतरी दवा, फैटी लिवर या इन्फेक्शन से जुड़ी हो सकती है। एक अकेला नंबर निदान नहीं है; डॉक्टर इतिहास, जांच और जरूरत में और टेस्ट से आंकलन करेंगे। ज़्यादा या लगातार बढ़ोतरी पर डॉक्टर से मिलें।</p>"), Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html="<p><strong>केवल सूचनार्थ।</strong> परिणाम डॉक्टर से चर्चा करें। <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>")],
            "ar": [Section(id="content", level=2, heading="ماذا تعني ارتفاع ALT وAST؟", body_html="<p><strong>ALT</strong> و<strong>AST</strong> إنزيمات في خلايا الكبد؛ قد ترتفع في الدم مع الإصابة أو الإجهاد. الارتفاع البسيط قد يرتبط بدواء أو كبد دهني أو عدوى. الرقم وحده لا يشخّص؛ الطبيب يقيّم مع التاريخ والفحص والتحاليل. عند ارتفاع واضح أو مستمر راجع الطبيب.</p>"), Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html="<p><strong>للمعلومات فقط.</strong> ناقش نتائجك مع الطبيب. <a href=\"/analyze\">بدء التحليل</a></p>")],
        },
    )


def _article_urea_high() -> Article:
    """Üre yüksekliği / High urea — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/creatinine-egfr-hero.png"
    return Article(
        id="ure-yuksekligi-ne-anlama-gelir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={"tr": "Üre kan tahlili — Norya", "en": "Urea blood test — Norya", "de": "Harnstoff Bluttest — Norya", "fr": "Urée sanguine — Norya", "it": "Urea nel sangue — Norya", "es": "Urea en sangre — Norya"},
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "es": "Biomarcadores"},
        slugs={"tr": "ure-yuksekligi-ne-anlama-gelir", "en": "what-does-a-high-urea-level-mean", "de": "was-bedeutet-ein-hoher-harnstoffwert", "fr": "que-signifie-uree-elevee", "it": "cosa-significa-urea-alta", "es": "que-significa-urea-alta"},
        titles={"tr": "Üre yüksekliği ne anlama gelir?", "en": "What does a high urea level mean?", "de": "Was bedeutet ein hoher Harnstoffwert?", "fr": "Que signifie un taux d'urée élevé ?", "it": "Cosa significa un valore di urea alto?", "es": "¿Qué significa un nivel de urea alto?"},
        subtitles={"tr": "Üre (BUN) referans aralıkları ve yüksek çıkmasının olası nedenleri. Kısa rehber.", "en": "Urea (BUN) reference ranges and possible causes of a high result. Short guide.", "de": "Harnstoff (BUN): Referenzbereiche und mögliche Ursachen für einen hohen Wert.", "fr": "Urée (BUN) : fourchettes et causes possibles d'un taux élevé.", "it": "Urea (BUN): intervalli e possibili cause di un valore alto.", "es": "Urea (BUN): rangos y posibles causas de un nivel alto."},
        excerpts={"tr": "Üre yüksekliği tek başına teşhis değildir; böbrek fonksiyonu ve sıvı alımı hekimle değerlendirilir.", "en": "High urea alone is not a diagnosis; kidney function and fluid intake are assessed with a doctor.", "de": "Hoher Harnstoff allein ist keine Diagnose; Nierenfunktion und Flüssigkeit mit dem Arzt besprechen.", "fr": "Une urée élevée seule n'est pas un diagnostic ; fonction rénale et hydratation avec le médecin.", "it": "Urea alta da sola non è una diagnosi; funzione renale e idratazione con il medico.", "es": "Urea alta por sí sola no es un diagnóstico; función renal e hidratación con el médico."},
        seo_titles={"tr": "Üre Yüksekliği Ne Anlama Gelir? | Norya Blog", "en": "What Does a High Urea Level Mean? | Norya Blog", "de": "Was bedeutet ein hoher Harnstoffwert? | Norya Blog", "fr": "Que signifie un taux d'urée élevé ? | Norya Blog", "it": "Cosa significa urea alta? | Norya Blog", "es": "¿Qué significa urea alta? | Norya Blog"},
        seo_descriptions={"tr": "Üre (BUN) yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Causes of high urea (BUN). For information only.", "de": "Ursachen für hohen Harnstoff (BUN). Nur zur Information.", "fr": "Causes d'une urée (BUN) élevée. À titre informatif.", "it": "Cause di urea (BUN) alta. Solo informativo.", "es": "Causas de urea (BUN) alta. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Üre yüksekliği ne anlama gelir?", body_html="<p><strong>Üre</strong> (bazen BUN) protein metabolizmasının bir ürünüdür; böbreklerden atılır. Yüksek çıkması böbrek fonksiyonunda azalma, susuzluk veya yüksek protein alımı gibi nedenlere bağlı olabilir. Tek başına teşhis koymaz; kreatinin ve eGFR ile birlikte hekim tarafından yorumlanır. Sonucunuzu hekimle görüşün.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What does a high urea level mean?", body_html="<p><strong>Urea</strong> (sometimes BUN) is a product of protein metabolism and is cleared by the kidneys. A high level may be due to reduced kidney function, dehydration, or high protein intake. It does not make a diagnosis alone; it is interpreted by your doctor together with creatinine and eGFR. Discuss your result with a doctor.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Was bedeutet ein hoher Harnstoffwert?", body_html="<p><strong>Harnstoff</strong> (oft BUN) entsteht beim Eiweißstoffwechsel und wird über die Nieren ausgeschieden. Erhöhung kann z. B. bei eingeschränkter Nierenfunktion, Flüssigkeitsmangel oder hoher Eiweißzufuhr vorkommen. Ein Wert allein ergibt keine Diagnose; der Arzt beurteilt zusammen mit Kreatinin und eGFR. Befund mit dem Arzt besprechen.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Que signifie un taux d'urée élevé ?", body_html="<p>L’<strong>urée</strong> (parfois BUN) est un produit du métabolisme des protéines, éliminée par les reins. Une élévation peut être liée à une baisse de la fonction rénale, une déshydratation ou un apport protéique élevé. Un chiffre seul ne fait pas le diagnostic ; le médecin interprète avec la créatinine et le DFG. Discutez du résultat avec un médecin.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Cosa significa un valore di urea alto?", body_html="<p>L’<strong>urea</strong> (a volte BUN) è un prodotto del metabolismo delle proteine, eliminata dai reni. Un valore alto può dipendere da ridotta funzione renale, disidratazione o elevato apporto proteico. Un solo valore non fa diagnosi; il medico interpreta con creatinina e eGFR. Discuti il risultato con il medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="¿Qué significa un nivel de urea alto?", body_html="<p>La <strong>urea</strong> (a veces BUN) es un producto del metabolismo de las proteínas, eliminada por los riñones. Un nivel alto puede deberse a menor función renal, deshidratación o alto consumo de proteínas. Un solo valor no da el diagnóstico; el médico interpreta con creatinina y FG. Comenta el resultado con un médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>")],
        },
    )


def _article_platelets_high_low() -> Article:
    """Trombosit yüksekliği ve düşüklüğü / Platelets high or low — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/vitamin-b12-hero.png"
    return Article(
        id="trombosit-yuksekligi-dusuklugu",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={"tr": "Trombosit kan tahlili — Norya", "en": "Platelets blood test — Norya", "de": "Thrombozyten Bluttest — Norya", "fr": "Plaquettes sanguines — Norya", "it": "Piastrine esami — Norya", "es": "Plaquetas análisis — Norya"},
        category={"tr": "Hemogram", "en": "Blood count", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "es": "Hemograma"},
        slugs={"tr": "trombosit-yuksekligi-ve-dusuklugu-ne-demek", "en": "what-do-low-or-high-platelets-mean", "de": "thrombozyten-zu-hoch-oder-zu-niedrig", "fr": "plaquettes-trop-hautes-ou-basses", "it": "piastrine-alte-o-basse-cosa-significa", "es": "plaquetas-altas-o-bajas-que-significa"},
        titles={"tr": "Trombosit yüksekliği ve düşüklüğü ne demek?", "en": "What do low or high platelets mean?", "de": "Thrombozyten zu hoch oder zu niedrig?", "fr": "Plaquettes trop hautes ou trop basses : que signifie ?", "it": "Piastrine alte o basse: cosa significa?", "es": "¿Qué significan las plaquetas altas o bajas?"},
        subtitles={"tr": "Trombosit (PLT) referans aralıkları ve sapmaların olası nedenleri. Kısa rehber.", "en": "Platelet (PLT) reference ranges and possible causes of high or low. Short guide.", "de": "Thrombozyten (PLT): Referenzbereich und mögliche Ursachen für Abweichungen.", "fr": "Plaquettes (PLT) : fourchettes et causes possibles des écarts.", "it": "Piastrine (PLT): intervalli e possibili cause di valori alti o bassi.", "es": "Plaquetas (PLT): rangos y posibles causas de alteraciones."},
        excerpts={"tr": "Trombosit düşüklüğü veya yüksekliği tek başına teşhis değildir; hekim tüm tahlilleri birlikte yorumlar.", "en": "Low or high platelets alone are not a diagnosis; your doctor interprets all results together.", "de": "Thrombozyten zu niedrig oder zu hoch sind keine Diagnose; der Arzt wertet alle Befunde gemeinsam.", "fr": "Plaquettes basses ou hautes seules ne font pas un diagnostic ; le médecin interprète l'ensemble.", "it": "Piastrine basse o alte da sole non sono una diagnosi; il medico valuta tutti gli esami.", "es": "Plaquetas bajas o altas por sí solas no son un diagnóstico; el médico valora todos los resultados."},
        seo_titles={"tr": "Trombosit Yüksekliği ve Düşüklüğü Ne Demek? | Norya Blog", "en": "What Do Low or High Platelets Mean? | Norya Blog", "de": "Thrombozyten zu hoch oder zu niedrig? | Norya Blog", "fr": "Plaquettes trop hautes ou basses : que signifie ? | Norya Blog", "it": "Piastrine alte o basse: cosa significa? | Norya Blog", "es": "¿Qué significan plaquetas altas o bajas? | Norya Blog"},
        seo_descriptions={"tr": "Trombosit (PLT) yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "Causes of low or high platelets (PLT). For information only.", "de": "Ursachen für niedrige oder hohe Thrombozyten (PLT). Nur zur Information.", "fr": "Causes des plaquettes basses ou hautes (PLT). À titre informatif.", "it": "Cause di piastrine basse o alte (PLT). Solo informativo.", "es": "Causas de plaquetas bajas o altas (PLT). Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Trombosit yüksekliği ve düşüklüğü", body_html="<p><strong>Trombosit</strong> (PLT) kanın pıhtılaşmasında rol oynar. Referans aralığının altında veya üstünde çıkması çeşitli nedenlere bağlı olabilir; tek bir değer teşhis koymaz. Hekiminiz hemogram ve gerekirse ek tetkiklerle değerlendirir. Belirgin sapma veya kanama belirtisi varsa mutlaka hekime danışın.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/tr/hemogram-sonucu\">Hemogram</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What do low or high platelets mean?", body_html="<p><strong>Platelets</strong> (PLT) help blood to clot. A result below or above the reference range can have various causes; a single value does not make a diagnosis. Your doctor will assess with a full blood count and further tests if needed. If there is a marked change or signs of bleeding, see a doctor.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/en/blood-test-results\">Blood test</a> · <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Thrombozyten zu hoch oder zu niedrig?", body_html="<p><strong>Thrombozyten</strong> (PLT) sind an der Blutgerinnung beteiligt. Abweichungen nach unten oder oben können verschiedene Ursachen haben; ein Wert allein ergibt keine Diagnose. Ihr Arzt beurteilt mit Blutbild und ggf. weiteren Tests. Bei deutlicher Abweichung oder Blutungszeichen zum Arzt.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/de/blutwerte-verstehen\">Blutwerte</a> · <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Plaquettes trop hautes ou trop basses", body_html="<p>Les <strong>plaquettes</strong> (PLT) participent à la coagulation. Un écart à la fourchette peut avoir plusieurs causes ; un chiffre seul ne fait pas un diagnostic. Le médecin évalue avec la NFS et d’éventuels examens. En cas d’écart marqué ou de signes de saignement, consultez.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Piastrine alte o basse", body_html="<p>Le <strong>piastrine</strong> (PLT) partecipano alla coagulazione. Un valore fuori intervallo può dipendere da varie cause; un solo valore non fa diagnosi. Il medico valuta con emocromo ed eventuali esami. In caso di scostamento marcato o segni di sanguinamento, rivolgersi al medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="Plaquetas altas o bajas", body_html="<p>Las <strong>plaquetas</strong> (PLT) intervienen en la coagulación. Un valor fuera de rango puede deberse a varias causas; un solo valor no da el diagnóstico. El médico valora con hemograma y pruebas si hace falta. Ante alteración marcada o signos de sangrado, consulta al médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>")],
        },
    )


def _article_wbc_rbc_hgb_hct() -> Article:
    """WBC, RBC, HGB, HCT nasıl okunur? — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/how-to-read-blood-test-results.png"
    return Article(
        id="wbc-rbc-hgb-hct-nasil-okunur",
        published_at=published,
        read_minutes=5,
        cover_image=cover,
        cover_alt={"tr": "Tam kan sayımı WBC RBC HGB HCT — Norya", "en": "Complete blood count WBC RBC HGB HCT — Norya", "de": "Blutbild WBC RBC HGB HCT — Norya", "fr": "NFS globules blancs rouges HGB HCT — Norya", "it": "Emocromo globuli bianchi rossi HGB HCT — Norya", "es": "Hemograma WBC RBC HGB HCT — Norya"},
        category={"tr": "Hemogram", "en": "Blood count", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "es": "Hemograma"},
        slugs={"tr": "wbc-rbc-hgb-hct-nasil-okunur", "en": "how-to-understand-wbc-rbc-hgb-and-hct", "de": "wbc-rbc-hgb-und-hct-verstehen", "fr": "comprendre-globules-blancs-rouges-hgb-hct", "it": "come-leggere-wbc-rbc-hgb-hct", "es": "como-entender-wbc-rbc-hgb-y-hct"},
        titles={"tr": "WBC, RBC, HGB, HCT nasıl okunur?", "en": "How to understand WBC, RBC, HGB and HCT", "de": "WBC, RBC, HGB und HCT verstehen", "fr": "Comprendre globules blancs, rouges, HGB et HCT", "it": "Come leggere WBC, RBC, HGB e HCT", "es": "Cómo entender WBC, RBC, HGB y HCT"},
        subtitles={"tr": "Tam kan sayımında beyaz küre, kırmızı küre, hemoglobin ve hematokrit ne anlama gelir? Kısa rehber.", "en": "What white cells, red cells, haemoglobin and haematocrit mean in a full blood count. Short guide.", "de": "Was bedeuten weiße und rote Blutkörperchen, Hämoglobin und Hämatokrit im Blutbild? Kurzer Überblick.", "fr": "Que signifient globules blancs, rouges, hémoglobine et hématocrite dans la NFS ? Guide court.", "it": "Cosa significano globuli bianchi, rossi, emoglobina ed ematocrito nell'emocromo? Guida breve.", "es": "Qué significan glóbulos blancos, rojos, hemoglobina y hematocrito en el hemograma. Guía breve."},
        excerpts={"tr": "WBC, RBC, HGB ve HCT tam kan sayımının temel değerleridir; yorumu hekimle yapılır.", "en": "WBC, RBC, HGB and HCT are key values in a full blood count; interpretation is with a doctor.", "de": "WBC, RBC, HGB und HCT sind zentrale Werte im Blutbild; Einordnung durch den Arzt.", "fr": "Globules blancs/rouges, HGB et HCT sont des valeurs clés de la NFS ; interprétation avec le médecin.", "it": "WBC, RBC, HGB e HCT sono valori chiave dell'emocromo; interpretazione con il medico.", "es": "WBC, RBC, HGB y HCT son valores clave del hemograma; interpretación con el médico."},
        seo_titles={"tr": "WBC, RBC, HGB, HCT Nasıl Okunur? | Norya Blog", "en": "How to Understand WBC, RBC, HGB and HCT | Norya Blog", "de": "WBC, RBC, HGB und HCT verstehen | Norya Blog", "fr": "Comprendre globules blancs, rouges, HGB et HCT | Norya Blog", "it": "Come leggere WBC, RBC, HGB e HCT | Norya Blog", "es": "Cómo entender WBC, RBC, HGB y HCT | Norya Blog"},
        seo_descriptions={"tr": "Tam kan sayımında WBC, RBC, hemoglobin ve hematokrit. Bilgilendirme amaçlı.", "en": "WBC, RBC, haemoglobin and haematocrit in a full blood count. For information only.", "de": "WBC, RBC, Hämoglobin und Hämatokrit im Blutbild. Nur zur Information.", "fr": "Globules blancs/rouges, HGB et HCT dans la NFS. À titre informatif.", "it": "WBC, RBC, emoglobina ed ematocrito nell'emocromo. Solo informativo.", "es": "WBC, RBC, hemoglobina y hematocrito en el hemograma. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="WBC, RBC, HGB, HCT ne demek?", body_html="<p><strong>WBC</strong> (lökosit) beyaz kan hücreleri; enfeksiyon veya iltihap durumunda değişebilir. <strong>RBC</strong> (eritrosit) kırmızı kan hücreleri; <strong>HGB</strong> (hemoglobin) oksijen taşır; <strong>HCT</strong> (hematokrit) kırmızı hücrelerin kandaki oranıdır. Referans aralıkları laboratuvara göre değişir. Sonucunuzu raporunuzdaki aralıklarla ve hekiminizle değerlendirin.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/tr/hemogram-sonucu\">Hemogram</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What do WBC, RBC, HGB and HCT mean?", body_html="<p><strong>WBC</strong> (white blood cells) can change with infection or inflammation. <strong>RBC</strong> (red blood cells), <strong>HGB</strong> (haemoglobin) carries oxygen, and <strong>HCT</strong> (haematocrit) is the proportion of red cells in blood. Reference ranges vary by lab. Interpret your result using the ranges on your report and with your doctor.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/en/understand-lab-results\">Lab results</a> · <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Was bedeuten WBC, RBC, HGB und HCT?", body_html="<p><strong>WBC</strong> (Leukozyten) können bei Infektion oder Entzündung verändert sein. <strong>RBC</strong> (Erythrozyten), <strong>HGB</strong> (Hämoglobin) und <strong>HCT</strong> (Hämatokrit) beschreiben die roten Blutkörperchen. Referenzbereiche sind laborabhängig. Ordnen Sie Ihren Befund anhand der Angaben auf dem Laborbericht und mit dem Arzt ein.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/de/laborwerte-verstehen\">Laborwerte</a> · <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Que signifient globules blancs, rouges, HGB et HCT?", body_html="<p>Les <strong>globules blancs</strong> (GB) peuvent varier en cas d’infection ou d’inflammation. Les <strong>globules rouges</strong> (GR), l’<strong>hémoglobine</strong> (HGB) et l’<strong>hématocrite</strong> (HCT) décrivent les cellules rouges. Les fourchettes varient selon le laboratoire. Interprétez votre résultat avec la fourchette du compte-rendu et avec le médecin.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Cosa significano WBC, RBC, HGB e HCT?", body_html="<p>I <strong>globuli bianchi</strong> (WBC) possono variare in caso di infezione o infiammazione. <strong>Globuli rossi</strong> (RBC), <strong>emoglobina</strong> (HGB) e <strong>ematocrito</strong> (HCT) descrivono le cellule rosse. Gli intervalli di riferimento variano da laboratorio. Interpreta il risultato con l’intervallo sul referto e con il medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="¿Qué significan WBC, RBC, HGB y HCT?", body_html="<p>Los <strong>glóbulos blancos</strong> (WBC) pueden cambiar con infección o inflamación. <strong>Glóbulos rojos</strong> (RBC), <strong>hemoglobina</strong> (HGB) y <strong>hematocrito</strong> (HCT) describen las células rojas. Los rangos de referencia varían por laboratorio. Interpreta tu resultado con el rango del informe y con el médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>")],
        },
    )


def _article_fasting_blood_sugar() -> Article:
    """Açlık kan şekeri sonucu / Fasting blood sugar — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/hba1c-hero.png"
    return Article(
        id="aclik-kan-sekeri-sonucu-nasil-degerlendirilir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={"tr": "Açlık kan şekeri — Norya", "en": "Fasting blood sugar — Norya", "de": "Nüchternblutzucker — Norya", "fr": "Glycémie à jeun — Norya", "it": "Glicemia a digiuno — Norya", "es": "Glucosa en ayunas — Norya"},
        category={"tr": "Kan şekeri", "en": "Blood sugar", "de": "Blutzucker", "fr": "Glycémie", "it": "Glicemia", "es": "Glucosa"},
        slugs={"tr": "aclik-kan-sekeri-sonucu-nasil-degerlendirilir", "en": "how-to-read-fasting-blood-sugar-results", "de": "nuechternblutzucker-verstehen", "fr": "comment-lire-glycemie-a-jeun", "it": "come-leggere-glicemia-a-digiuno", "es": "como-leer-glucosa-en-ayunas"},
        titles={"tr": "Açlık kan şekeri sonucu nasıl değerlendirilir?", "en": "How to read fasting blood sugar results", "de": "Nüchternblutzucker verstehen", "fr": "Comment lire la glycémie à jeun ?", "it": "Come leggere la glicemia a digiuno?", "es": "¿Cómo leer la glucosa en ayunas?"},
        subtitles={"tr": "Açlık glukozu referans aralıkları ve sonucunuzu nasıl yorumlayacağınıza dair kısa rehber.", "en": "Fasting glucose reference ranges and a short guide to interpreting your result.", "de": "Referenzbereiche für Nüchternglukose und kurze Einordnung.", "fr": "Fourchettes de référence pour la glycémie à jeun et comment interpréter.", "it": "Intervalli di riferimento per la glicemia a digiuno e come interpretare.", "es": "Rangos de referencia para glucosa en ayunas y cómo interpretar."},
        excerpts={"tr": "Açlık kan şekeri tek başına teşhis değildir; diyabet veya prediyabet hekim tarafından değerlendirilir.", "en": "Fasting blood sugar alone is not a diagnosis; diabetes or prediabetes is assessed by a doctor.", "de": "Nüchternblutzucker allein ist keine Diagnose; Diabetes/Prädiabetes beurteilt der Arzt.", "fr": "La glycémie à jeun seule ne fait pas un diagnostic ; diabète ou prédiabète avec le médecin.", "it": "La glicemia a digiuno da sola non è una diagnosi; diabete o prediabete con il medico.", "es": "La glucosa en ayunas por sí sola no es un diagnóstico; diabetes o prediabetes con el médico."},
        seo_titles={"tr": "Açlık Kan Şekeri Sonucu Nasıl Değerlendirilir? | Norya Blog", "en": "How to Read Fasting Blood Sugar Results | Norya Blog", "de": "Nüchternblutzucker verstehen | Norya Blog", "fr": "Comment lire la glycémie à jeun ? | Norya Blog", "it": "Come leggere la glicemia a digiuno? | Norya Blog", "es": "¿Cómo leer la glucosa en ayunas? | Norya Blog"},
        seo_descriptions={"tr": "Açlık kan şekeri referans aralıkları ve yorumlama. Bilgilendirme amaçlı.", "en": "Fasting blood sugar reference ranges and interpretation. For information only.", "de": "Nüchternblutzucker: Referenzbereiche und Einordnung. Nur zur Information.", "fr": "Glycémie à jeun : fourchettes et interprétation. À titre informatif.", "it": "Glicemia a digiuno: intervalli e interpretazione. Solo informativo.", "es": "Glucosa en ayunas: rangos e interpretación. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Açlık kan şekeri nasıl değerlendirilir?", body_html="<p><strong>Açlık kan şekeri</strong> (glukoz) genellikle 8–12 saat açlık sonrası ölçülür. Referans aralıkları laboratuvara göre değişir; yüksek çıkması diyabet veya prediyabet açısından değerlendirilir. Tek bir ölçüm teşhis koymaz; hekiminiz HbA1c veya OGTT gibi ek testlerle karar verir. Sonucunuzu hekimle görüşün.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="How to read fasting blood sugar results", body_html="<p><strong>Fasting blood sugar</strong> (glucose) is usually measured after 8–12 hours of fasting. Reference ranges vary by lab; a high result may be assessed for diabetes or prediabetes. A single reading does not make a diagnosis; your doctor may use HbA1c or OGTT. Discuss your result with a doctor.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Nüchternblutzucker verstehen", body_html="<p><strong>Nüchternblutzucker</strong> (Glukose) wird meist nach 8–12 Stunden Nüchternheit gemessen. Referenzbereiche sind laborabhängig; Erhöhung kann auf Diabetes oder Prädiabetes hinweisen. Ein einzelner Wert ergibt keine Diagnose; der Arzt kann HbA1c oder oGTT anordnen. Befund mit dem Arzt besprechen.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Comment lire la glycémie à jeun ?", body_html="<p>La <strong>glycémie à jeun</strong> (glucose) est mesurée après 8–12 h de jeûne. Les fourchettes varient selon le laboratoire ; une élévation peut orienter vers diabète ou prédiabète. Un seul chiffre ne fait pas le diagnostic ; le médecin peut prescrire HbA1c ou HGPO. Discutez du résultat avec un médecin.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Come leggere la glicemia a digiuno?", body_html="<p>La <strong>glicemia a digiuno</strong> (glucosio) si misura dopo 8–12 ore di digiuno. Gli intervalli variano da laboratorio; un valore alto può essere valutato per diabete o prediabete. Un solo valore non fa diagnosi; il medico può richiedere HbA1c o OGTT. Discuti il risultato con il medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="Cómo leer la glucosa en ayunas", body_html="<p>La <strong>glucosa en ayunas</strong> se mide tras 8–12 h de ayuno. Los rangos varían por laboratorio; un nivel alto puede valorarse para diabetes o prediabetes. Un solo valor no da el diagnóstico; el médico puede solicitar HbA1c o SOG. Comenta el resultado con un médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>")],
        },
    )


def _article_hba1c_meaning() -> Article:
    """HbA1c sonucu ne anlama gelir? / What does HbA1c result mean? — Second wave (focused)."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/hba1c-hero.png"
    return Article(
        id="hba1c-sonucu-ne-anlama-gelir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        cover_alt={"tr": "HbA1c kan tahlili — Norya", "en": "HbA1c blood test — Norya", "de": "HbA1c Bluttest — Norya", "fr": "HbA1c sanguine — Norya", "it": "HbA1c esami — Norya", "es": "HbA1c análisis — Norya"},
        category={"tr": "Kan şekeri", "en": "Blood sugar", "de": "Blutzucker", "fr": "Glycémie", "it": "Glicemia", "es": "Glucosa"},
        slugs={"tr": "hba1c-sonucu-ne-anlama-gelir", "en": "what-does-an-hba1c-result-mean", "de": "hba1c-verstehen-was-bedeutet-der-wert", "fr": "hba1c-comprendre-resultat", "it": "hba1c-cosa-significa-il-valore", "es": "hba1c-que-significa-el-resultado"},
        titles={"tr": "HbA1c sonucu ne anlama gelir?", "en": "What does an HbA1c result mean?", "de": "HbA1c verstehen: Was bedeutet der Wert?", "fr": "HbA1c : que signifie le résultat ?", "it": "HbA1c: cosa significa il valore?", "es": "¿Qué significa un resultado de HbA1c?"},
        subtitles={"tr": "HbA1c son 2–3 aydaki ortalama kan şekerini yansıtır. Referans aralıkları ve yorumlama.", "en": "HbA1c reflects average blood sugar over the last 2–3 months. Reference ranges and interpretation.", "de": "HbA1c spiegelt den durchschnittlichen Blutzucker der letzten 2–3 Monate wider. Referenzbereiche und Einordnung.", "fr": "L'HbA1c reflète la glycémie moyenne sur 2–3 mois. Fourchettes et interprétation.", "it": "L'HbA1c riflette la glicemia media degli ultimi 2–3 mesi. Intervalli e interpretazione.", "es": "La HbA1c refleja el promedio de glucosa de los últimos 2–3 meses. Rangos e interpretación."},
        excerpts={"tr": "HbA1c diyabet taraması ve takipte kullanılır; yorumu hekimle yapılır.", "en": "HbA1c is used for diabetes screening and monitoring; interpretation is with a doctor.", "de": "HbA1c wird zur Diabetesscreening und -kontrolle genutzt; Einordnung durch den Arzt.", "fr": "L'HbA1c sert au dépistage et au suivi du diabète ; interprétation avec le médecin.", "it": "L'HbA1c si usa per screening e monitoraggio del diabete; interpretazione con il medico.", "es": "La HbA1c se usa para cribado y seguimiento de la diabetes; interpretación con el médico."},
        seo_titles={"tr": "HbA1c Sonucu Ne Anlama Gelir? | Norya Blog", "en": "What Does an HbA1c Result Mean? | Norya Blog", "de": "HbA1c verstehen: Was bedeutet der Wert? | Norya Blog", "fr": "HbA1c : que signifie le résultat ? | Norya Blog", "it": "HbA1c: cosa significa il valore? | Norya Blog", "es": "¿Qué significa un resultado de HbA1c? | Norya Blog"},
        seo_descriptions={"tr": "HbA1c referans aralıkları ve ne anlama geldiği. Bilgilendirme amaçlı.", "en": "HbA1c reference ranges and what they mean. For information only.", "de": "HbA1c: Referenzbereiche und Bedeutung. Nur zur Information.", "fr": "HbA1c : fourchettes et signification. À titre informatif.", "it": "HbA1c: intervalli e significato. Solo informativo.", "es": "HbA1c: rangos y significado. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="HbA1c sonucu ne anlama gelir?", body_html="<p><strong>HbA1c</strong> son 2–3 aydaki ortalama kan şekerini tahmin etmek için kullanılır; diyabet tanısı ve takipte önemlidir. Referans aralıkları laboratuvara göre değişir; genelde yüzde (%) veya mmol/mol birimiyle raporlanır. Tek başına teşhis koymaz; hekiminiz açlık glukozu veya diğer testlerle birlikte değerlendirir.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What does an HbA1c result mean?", body_html="<p><strong>HbA1c</strong> is used to estimate average blood sugar over the last 2–3 months and is important in diabetes diagnosis and monitoring. Reference ranges vary by lab; results are often reported as % or mmol/mol. It does not make a diagnosis alone; your doctor will assess it with fasting glucose or other tests.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="HbA1c verstehen: Was bedeutet der Wert?", body_html="<p><strong>HbA1c</strong> schätzt den durchschnittlichen Blutzucker der letzten 2–3 Monate und ist bei Diabetes-Diagnostik und -Kontrolle wichtig. Referenzbereiche sind laborabhängig; Angabe oft in % oder mmol/mol. Ein Wert allein ergibt keine Diagnose; der Arzt beurteilt mit Nüchternzucker und ggf. weiteren Tests.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="HbA1c : que signifie le résultat ?", body_html="<p>L’<strong>HbA1c</strong> reflète la glycémie moyenne sur 2–3 mois et est utilisée pour le diagnostic et le suivi du diabète. Les fourchettes varient selon le laboratoire ; résultat souvent en % ou mmol/mol. Un chiffre seul ne fait pas le diagnostic ; le médecin évalue avec la glycémie à jeun et d’éventuels autres examens.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="HbA1c: cosa significa il valore?", body_html="<p>L’<strong>HbA1c</strong> riflette la glicemia media degli ultimi 2–3 mesi ed è usata per diagnosi e monitoraggio del diabete. Gli intervalli variano da laboratorio; risultato spesso in % o mmol/mol. Un solo valore non fa diagnosi; il medico valuta con glicemia a digiuno ed eventuali altri esami.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="¿Qué significa un resultado de HbA1c?", body_html="<p>La <strong>HbA1c</strong> refleja el promedio de glucosa de los últimos 2–3 meses y se usa para diagnóstico y seguimiento de la diabetes. Los rangos varían por laboratorio; resultado a menudo en % o mmol/mol. Un solo valor no da el diagnóstico; el médico valora con glucosa en ayunas y otras pruebas.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>")],
        },
    )


def _article_cholesterol_types() -> Article:
    """Kan tahlilinde kolesterol türleri / Cholesterol types in blood work — Second wave."""
    published = date(2026, 3, 15)
    cover = "/static/images/blog/ldl-hdl-hero.png"
    return Article(
        id="kan-tahlilinde-kolesterol-turleri",
        published_at=published,
        read_minutes=5,
        cover_image=cover,
        cover_alt={"tr": "Kolesterol türleri kan tahlili — Norya", "en": "Cholesterol types blood test — Norya", "de": "Cholesterinarten Bluttest — Norya", "fr": "Types de cholestérol — Norya", "it": "Tipi di colesterolo — Norya", "es": "Tipos de colesterol — Norya"},
        category={"tr": "Kolesterol", "en": "Cholesterol", "de": "Cholesterin", "fr": "Cholestérol", "it": "Colesterolo", "es": "Colesterol"},
        slugs={"tr": "kan-tahlilinde-kolesterol-turleri-nasil-anlasilir", "en": "how-to-understand-cholesterol-types-in-blood-work", "de": "cholesterin-im-bluttest-richtig-einordnen", "fr": "comprendre-types-cholesterol-bilan-sanguin", "it": "come-capire-tipi-colesterolo-esami", "es": "como-entender-tipos-colesterol-analisis"},
        titles={"tr": "Kan tahlilinde kolesterol türleri nasıl anlaşılır?", "en": "How to understand cholesterol types in blood work", "de": "Cholesterin im Bluttest richtig einordnen", "fr": "Comprendre les types de cholestérol dans le bilan sanguin", "it": "Come capire i tipi di colesterolo negli esami", "es": "Cómo entender los tipos de colesterol en el análisis"},
        subtitles={"tr": "Total kolesterol, LDL, HDL ve trigliserit ne anlama gelir? Kısa rehber.", "en": "What total cholesterol, LDL, HDL and triglycerides mean. Short guide.", "de": "Was Gesamtcholesterin, LDL, HDL und Triglyceride bedeuten. Kurzer Überblick.", "fr": "Que signifient cholestérol total, LDL, HDL et triglycérides. Guide court.", "it": "Cosa significano colesterolo totale, LDL, HDL e trigliceridi. Guida breve.", "es": "Qué significan colesterol total, LDL, HDL y triglicéridos. Guía breve."},
        excerpts={"tr": "Kolesterol türleri tek başına risk göstermez; hekim tüm değerleri ve risk faktörlerini birlikte değerlendirir.", "en": "Cholesterol types alone do not define risk; your doctor assesses all values and risk factors together.", "de": "Cholesterinwerte allein definieren kein Risiko; der Arzt beurteilt alle Werte und Risikofaktoren.", "fr": "Les types de cholestérol seuls ne définissent pas le risque ; le médecin évalue l'ensemble.", "it": "I tipi di colesterolo da soli non definiscono il rischio; il medico valuta tutti i valori.", "es": "Los tipos de colesterol por sí solos no definen el riesgo; el médico valora todos los valores."},
        seo_titles={"tr": "Kan Tahlilinde Kolesterol Türleri Nasıl Anlaşılır? | Norya Blog", "en": "How to Understand Cholesterol Types in Blood Work | Norya Blog", "de": "Cholesterin im Bluttest richtig einordnen | Norya Blog", "fr": "Comprendre les types de cholestérol dans le bilan | Norya Blog", "it": "Come capire i tipi di colesterolo negli esami | Norya Blog", "es": "Cómo entender los tipos de colesterol en el análisis | Norya Blog"},
        seo_descriptions={"tr": "Total kolesterol, LDL, HDL, trigliserit. Bilgilendirme amaçlı.", "en": "Total cholesterol, LDL, HDL, triglycerides. For information only.", "de": "Gesamtcholesterin, LDL, HDL, Triglyceride. Nur zur Information.", "fr": "Cholestérol total, LDL, HDL, triglycérides. À titre informatif.", "it": "Colesterolo totale, LDL, HDL, trigliceridi. Solo informativo.", "es": "Colesterol total, LDL, HDL, triglicéridos. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Kolesterol türleri nasıl anlaşılır?", body_html="<p><strong>Total kolesterol</strong> tüm kolesterol türlerinin toplamıdır. <strong>LDL</strong> (\"kötü\" kolesterol) damar riskiyle ilişkilidir; <strong>HDL</strong> (\"iyi\" kolesterol) koruyucu kabul edilir. <strong>Trigliserit</strong> kan yağıdır. Referans aralıkları laboratuvara göre değişir; hedef değerler kardiyovasküler riskinize göre belirlenir. Sonucunuzu hekimle görüşün.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/tr/kan-degerleri-anlama\">Kan değerleri</a> · <a href=\"/pricing\">Fiyatlar</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="How to understand cholesterol types", body_html="<p><strong>Total cholesterol</strong> is the sum of all cholesterol types. <strong>LDL</strong> (\"bad\" cholesterol) is linked to vascular risk; <strong>HDL</strong> (\"good\" cholesterol) is considered protective. <strong>Triglycerides</strong> are blood fats. Reference ranges vary by lab; targets depend on your cardiovascular risk. Discuss your result with a doctor.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/en/understand-lab-results\">Lab results</a> · <a href=\"/pricing\">Pricing</a> · <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Cholesterin im Bluttest einordnen", body_html="<p><strong>Gesamtcholesterin</strong> ist die Summe aller Cholesterinanteile. <strong>LDL</strong> (\"schlechtes\" Cholesterin) ist mit Gefäßrisiko verbunden; <strong>HDL</strong> (\"gutes\" Cholesterin) gilt als schützend. <strong>Trigyceride</strong> sind Blutfette. Referenzbereiche sind laborabhängig; Ziele hängen vom kardiovaskulären Risiko ab. Befund mit dem Arzt besprechen.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/de/laborwerte-verstehen\">Laborwerte</a> · <a href=\"/pricing\">Preise</a> · <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Comprendre les types de cholestérol", body_html="<p>Le <strong>cholestérol total</strong> est la somme des fractions. Le <strong>LDL</strong> (\"mauvais\") est lié au risque vasculaire ; le <strong>HDL</strong> (\"bon\") est protecteur. Les <strong>triglycérides</strong> sont des graisses sanguines. Les fourchettes varient selon le laboratoire ; les cibles dépendent du risque cardiovasculaire. Discutez du résultat avec un médecin.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/pricing\">Tarifs</a> · <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Come capire i tipi di colesterolo", body_html="<p>Il <strong>colesterolo totale</strong> è la somma delle frazioni. <strong>LDL</strong> (\"cattivo\") è legato al rischio vascolare; <strong>HDL</strong> (\"buono\") è protettivo. I <strong>trigliceridi</strong> sono grassi nel sangue. Gli intervalli variano da laboratorio; gli obiettivi dipendono dal rischio cardiovascolare. Discuti il risultato con il medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/pricing\">Prezzi</a> · <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="Cómo entender los tipos de colesterol", body_html="<p>El <strong>colesterol total</strong> es la suma de las fracciones. <strong>LDL</strong> (\"malo\") se asocia a riesgo vascular; <strong>HDL</strong> (\"bueno\") es protector. Los <strong>triglicéridos</strong> son grasas en sangre. Los rangos varían por laboratorio; los objetivos dependen del riesgo cardiovascular. Comenta el resultado con un médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/pricing\">Precios</a> · <a href=\"/analyze\">Analizar</a></p>")],
        },
    )


_ARTICLE_IRON_DEFICIENCY = _article_iron_deficiency_blood()
_ARTICLE_ALT_AST = _article_alt_ast_high()
_ARTICLE_UREA = _article_urea_high()
_ARTICLE_PLATELETS = _article_platelets_high_low()
_ARTICLE_WBC_RBC = _article_wbc_rbc_hgb_hct()
_ARTICLE_FASTING_GLUCOSE = _article_fasting_blood_sugar()
_ARTICLE_HBA1C_MEANING = _article_hba1c_meaning()
_ARTICLE_CHOLESTEROL_TYPES = _article_cholesterol_types()


# TODO: create dedicated blog posts for "complete blood count explained" and "liver enzyme test explained"
ARTICLES: List[Article] = [
    _LDL_ARTICLE,
    _LDL_HDL_ARTICLE,
    _KAN_TAHLILI_ARTICLE,
    _FERRITIN_ARTICLE,
    _CRP_ARTICLE,
    _VITAMIN_D_ARTICLE,
    _VITAMIN_B12_ARTICLE,
    _HBA1C_ARTICLE,
    _TSH_ARTICLE,
    _CREATININE_EGFR_ARTICLE,
    _BLUTWERTE_ONLINE_ARTICLE,
    _ARTICLE_B12_LOW,
    _ARTICLE_VITAMIN_D_INTERPRET,
    _ARTICLE_IRON_DEFICIENCY,
    _ARTICLE_ALT_AST,
    _ARTICLE_UREA,
    _ARTICLE_PLATELETS,
    _ARTICLE_WBC_RBC,
    _ARTICLE_FASTING_GLUCOSE,
    _ARTICLE_HBA1C_MEANING,
    _ARTICLE_CHOLESTEROL_TYPES,
]


def _normalize_lang(lang: str | None) -> str:
    if not lang:
        return DEFAULT_BLOG_LANG
    lang = lang.lower()[:5]
    if lang in BLOG_LANGS:
        return lang
    short = lang.split("-")[0]
    return short if short in BLOG_LANGS else DEFAULT_BLOG_LANG


def list_articles_for_lang(lang: str) -> List[dict]:
    """Belirli bir dil için blog listesinde kullanılacak kart verilerini döner."""
    lang = _normalize_lang(lang)
    items: List[dict] = []
    for art in ARTICLES:
        if lang not in art.slugs:
            continue
        cover_alt = None
        if getattr(art, "cover_alt", None) and isinstance(art.cover_alt, dict):
            cover_alt = art.cover_alt.get(lang) or art.cover_alt.get(DEFAULT_BLOG_LANG)
        items.append(
            {
                "id": art.id,
                "slug": art.slugs[lang],
                "title": art.titles.get(lang, art.titles.get(DEFAULT_BLOG_LANG)),
                "excerpt": art.excerpts.get(lang, art.excerpts.get(DEFAULT_BLOG_LANG, "")),
                "category": art.category.get(lang, art.category.get(DEFAULT_BLOG_LANG, "")),
                "cover_image": art.cover_image,
                "cover_alt": cover_alt,
                "read_minutes": art.read_minutes,
                "published_at": art.published_at,
            }
        )
    # Yayın tarihine göre yeni -> eski
    items.sort(key=lambda x: x["published_at"], reverse=True)
    return items


def get_article(lang: str, slug: str) -> dict | None:
    """Dil + slug ile makale ve seçili dil içeriğini döner."""
    lang = _normalize_lang(lang)
    for art in ARTICLES:
        if art.slugs.get(lang) == slug:
            sections = art.sections_by_lang.get(lang) or art.sections_by_lang.get(DEFAULT_BLOG_LANG) or []
            cover_alt = None
            if getattr(art, "cover_alt", None) and isinstance(art.cover_alt, dict):
                cover_alt = art.cover_alt.get(lang) or art.cover_alt.get(DEFAULT_BLOG_LANG)
            last_updated = getattr(art, "last_updated", None) or art.published_at
            faq_schema_qa = None
            if getattr(art, "faq_schema_qa", None) and isinstance(art.faq_schema_qa, dict):
                faq_schema_qa = art.faq_schema_qa.get(lang) or art.faq_schema_qa.get(DEFAULT_BLOG_LANG)
            return {
                "id": art.id,
                "lang": lang,
                "slug": slug,
                "title": art.titles.get(lang, art.titles.get(DEFAULT_BLOG_LANG)),
                "subtitle": art.subtitles.get(lang, art.subtitles.get(DEFAULT_BLOG_LANG, "")),
                "excerpt": art.excerpts.get(lang, art.excerpts.get(DEFAULT_BLOG_LANG, "")),
                "seo_title": art.seo_titles.get(lang, art.seo_titles.get(DEFAULT_BLOG_LANG)),
                "seo_description": art.seo_descriptions.get(lang, art.seo_descriptions.get(DEFAULT_BLOG_LANG, "")),
                "cover_image": art.cover_image,
                "cover_alt": cover_alt,
                "category": art.category.get(lang, art.category.get(DEFAULT_BLOG_LANG, "")),
                "read_minutes": art.read_minutes,
                "published_at": art.published_at,
                "last_updated": last_updated,
                "sections": sections,
                "available_langs": {
                    l: art.slugs[l] for l in art.slugs.keys() if l in BLOG_LANGS
                },
                "faq_schema_qa": faq_schema_qa,
            }
    return None


def iter_all_article_paths():
    """Sitemap için tüm dil+slug kombinasyonlarını döner (last_updated = updatedAt)."""
    for art in ARTICLES:
        last_updated = getattr(art, "last_updated", None) or art.published_at
        for lang, slug in art.slugs.items():
            if lang not in BLOG_LANGS:
                continue
            yield {
                "lang": lang,
                "slug": slug,
                "published_at": art.published_at,
                "last_updated": last_updated,
            }


def get_related_articles(lang: str, current_article_id: str, base_url: str, limit: int = 4) -> List[dict]:
    """Aynı dilde, aynı kategori öncelikli en fazla `limit` makale döner (mevcut hariç). İç linkleme için."""
    lang = _normalize_lang(lang)
    if lang not in BLOG_LANGS_PREMIUM:
        return []
    posts = list_articles_for_lang(lang)
    current = next((p for p in posts if p["id"] == current_article_id), None)
    if not current:
        return []
    cat = current.get("category") or ""
    same_cat = [p for p in posts if p["id"] != current_article_id and (p.get("category") or "") == cat]
    other = [p for p in posts if p["id"] != current_article_id and (p.get("category") or "") != cat]
    chosen = (same_cat + other)[:limit]
    base_url = base_url.rstrip("/")
    result = []
    for p in chosen:
        cover = p.get("cover_image") or ""
        cover_abs = cover if cover.startswith("http") else f"{base_url}{cover}"
        result.append({
            "url": f"{base_url}/{lang}/blog/{p['slug']}",
            "title": p.get("title") or "",
            "cover_image": cover_abs,
            "cover_alt": p.get("cover_alt") or p.get("title") or "",
            "category": p.get("category") or "",
        })
    return result

