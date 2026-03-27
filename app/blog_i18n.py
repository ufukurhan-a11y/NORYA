from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional

from app.core.config import BRAND_NAME

# Blog'un desteklediği diller (mevcut sistemle uyumlu)
# SEO: Hero, seo_title, meta_description ve makale başlıkları tüm BLOG_LANGS_PREMIUM dillerinde
# tutarlı olmalı (aynı anahtar kelime mantığı, yerel dilde).
BLOG_LANGS = frozenset({"tr", "en", "de", "it", "es", "fr", "he", "ar", "hi", "el", "cs", "sr"})
# Premium blog: sadece bu dillerde route açılır; varsayılan İngilizce
BLOG_LANGS_PREMIUM = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")
DEFAULT_BLOG_LANG = "en"
BLOG_COVER_FALLBACK = "/static/images/blog/blog-hero.png"
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_STATIC_ROOT = _PROJECT_ROOT / "static"

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
        "featured_label": "Öne çıkan rehber",
        "filter_tags_label": "Konular",
        "filter_tags_title": "Konuya göre filtrele",
        "close_filter_drawer": "Filtreyi kapat",
        "breadcrumb_aria": "Sayfa konumu",
        "close_toc_drawer": "İçindekileri kapat",
        "breadcrumb_blog": "Blog",
        "trust_strip_1": "Gizlilik öncelikli",
        "trust_strip_2": "Güvenli işleme",
        "trust_strip_3": "Anlaşılır sunum",
        "cta_after_brand": " ile kan tahlili sonuçlarınızı yapılandırılmış, hekime hazır bir özet rapora dönüştürün.",
        "mid_cta_title": "Kendi sonuçlarınızı anlamak ister misiniz?",
        "mid_cta_desc": "Kan tahlili sonuçlarınızı yükleyin, yapay zeka destekli net bir açıklama alın.",
        "mid_cta_btn": "NoryaAI'yı dene",
        "article_edu_note": "Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez. Sonuçları mutlaka bir hekimle birlikte değerlendirin.",
        "related_intro": "Laboratuvar değerleri ve akıllı takip için seçilmiş okumalar.",
        "categories_aria": "Kategoriler",
        "articles_section_aria": "Makaleler",
        "lang_nav_aria": "Dil",
        "end_cta_nudge": "Yükleme sonrası birçok rapor dakikalar içinde hazır olur.",
        "lead_title": "Kan tahlili rehberleri ve yeni özellikler",
        "lead_desc": "Örnek raporlar, test yorumlama rehberleri ve doktora hazır özet güncellemelerini e-postana gönderelim.",
        "lead_placeholder_email": "E-posta adresiniz",
        "lead_placeholder_name": "Adınız (opsiyonel)",
        "lead_btn": "Beni bilgilendir",
        "lead_btn_loading": "Gönderiliyor…",
        "lead_success": "Kaydınız alındı — teşekkürler!",
        "lead_already": "Bu e-posta zaten kayıtlı.",
        "lead_error_email": "Lütfen geçerli bir e-posta girin.",
        "lead_error_generic": "Bir hata oluştu. Lütfen tekrar deneyin.",
        "lead_privacy": "Spam göndermeyiz. İstediğiniz zaman çıkabilirsiniz.",
        "lead_consent_text": "KVKK/GDPR kapsamında e-posta güncellemelerini almak için onay veriyorum.",
        "lead_error_consent": "KVKK/GDPR onayını kabul etmelisiniz.",
    },
    "en": {
        "hero_badge": "Health insights",
        "hero_title": "Blood Test Results Explained: CBC, Ferritin, HbA1c, Thyroid, and More",
        "hero_desc": "Plain-language guides on CBC, ferritin, HbA1c, thyroid, cholesterol, and more to help you understand lab results before your doctor visit. No diagnosis, just clear guidance.",
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
        "seo_title": f"{BRAND_NAME} Blog | Blood Test Results Explained, CBC & Biomarker Guides",
        "meta_description": "Blood test results explained with clear guides on CBC, ferritin, HbA1c, thyroid, cholesterol, CRP, and more. Educational lab report help for your next doctor visit.",
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
        "featured_label": "Featured guide",
        "filter_tags_label": "Topics",
        "filter_tags_title": "Filter by topic",
        "close_filter_drawer": "Close filter",
        "breadcrumb_aria": "Breadcrumb",
        "close_toc_drawer": "Close table of contents",
        "breadcrumb_blog": "Blog",
        "trust_strip_1": "Privacy-first",
        "trust_strip_2": "Secure processing",
        "trust_strip_3": "Built for clarity",
        "cta_after_brand": " — turn your lab results into a structured, clinician-ready summary.",
        "mid_cta_title": "Want to understand your own results?",
        "mid_cta_desc": "Upload your blood test and get a clear AI-powered explanation.",
        "mid_cta_btn": "Try NoryaAI",
        "article_edu_note": "Educational guide only — not medical advice. Always review results with a qualified clinician.",
        "related_intro": "Further reading on lab markers, trends, and sensible follow-up.",
        "categories_aria": "Categories",
        "articles_section_aria": "Articles",
        "lang_nav_aria": "Language",
        "end_cta_nudge": "Most reports are ready within minutes after upload.",
        "lead_title": "Blood test guides & new features",
        "lead_desc": "Get sample reports, lab result guides, and doctor-ready summary updates straight to your inbox.",
        "lead_placeholder_email": "Your email address",
        "lead_placeholder_name": "Your name (optional)",
        "lead_btn": "Keep me updated",
        "lead_btn_loading": "Sending…",
        "lead_success": "You're in — thank you!",
        "lead_already": "This email is already registered.",
        "lead_error_email": "Please enter a valid email.",
        "lead_error_generic": "Something went wrong. Please try again.",
        "lead_privacy": "No spam. Unsubscribe anytime.",
        "lead_consent_text": "I consent to receive email updates in accordance with KVKK/GDPR.",
        "lead_error_consent": "Please accept the KVKK/GDPR consent.",
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
        "featured_label": "Empfehlung",
        "filter_tags_label": "Themen",
        "filter_tags_title": "Nach Thema filtern",
        "close_filter_drawer": "Filter schließen",
        "breadcrumb_aria": "Brotkrümel",
        "close_toc_drawer": "Inhalt schließen",
        "breadcrumb_blog": "Blog",
        "trust_strip_1": "Datenschutz im Fokus",
        "trust_strip_2": "Sichere Verarbeitung",
        "trust_strip_3": "Klar strukturiert",
        "cta_after_brand": " — machen Sie aus Ihren Laborwerten eine strukturierte, arzttaugliche Zusammenfassung.",
        "mid_cta_title": "Möchten Sie Ihre eigenen Ergebnisse verstehen?",
        "mid_cta_desc": "Laden Sie Ihr Blutbild hoch und erhalten Sie eine klare KI-gestützte Erklärung.",
        "mid_cta_btn": "NoryaAI testen",
        "article_edu_note": "Dieser Ratgeber ersetzt keine ärztliche Beratung oder Diagnose. Besprechen Sie Befunde immer mit Ihrem Arzt oder Ihrer Ärztin.",
        "related_intro": "Weitere Artikel zu Biomarkern, Verlauf und sinnvollem Kontext.",
        "categories_aria": "Kategorien",
        "articles_section_aria": "Artikel",
        "lang_nav_aria": "Sprache",
        "end_cta_nudge": "Viele Berichte sind nach dem Upload in wenigen Minuten fertig.",
        "lead_title": "Bluttest-Leitfäden und neue Funktionen",
        "lead_desc": "Erhalten Sie Beispielberichte, Laborergebnis-Leitfäden und Updates zu arztfertigen Zusammenfassungen direkt in Ihr Postfach.",
        "lead_placeholder_email": "Ihre E-Mail-Adresse",
        "lead_placeholder_name": "Ihr Name (optional)",
        "lead_btn": "Auf dem Laufenden bleiben",
        "lead_btn_loading": "Wird gesendet…",
        "lead_success": "Anmeldung erfolgreich — danke!",
        "lead_already": "Diese E-Mail ist bereits registriert.",
        "lead_error_email": "Bitte geben Sie eine gültige E-Mail ein.",
        "lead_error_generic": "Ein Fehler ist aufgetreten. Bitte versuchen Sie es erneut.",
        "lead_privacy": "Kein Spam. Jederzeit abmeldbar.",
        "lead_consent_text": "Ich stimme zu, E-Mail-Updates gemäß KVKK/GDPR zu erhalten.",
        "lead_error_consent": "Bitte stimmen Sie der KVKK/GDPR Einwilligung zu.",
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
        "end_cta_title": "Importez vos résultats, obtenez un rapport clair",
        "end_cta_text": "Importez vos résultats en toute sécurité ; explications en langage clair et points clés en quelques minutes.",
        "end_cta_button": "Analyser le bilan sanguin",
        "related_label": "Articles similaires",
        "blog_back_to_landing": "Accueil",
        "how_it_works_link": "Comment ça marche",
        "pricing_link": "Tarifs",
        "featured_label": "À la une",
        "filter_tags_label": "Thèmes",
        "filter_tags_title": "Filtrer par thème",
        "close_filter_drawer": "Fermer le filtre",
        "breadcrumb_aria": "Fil d'Ariane",
        "close_toc_drawer": "Fermer le sommaire",
        "breadcrumb_blog": "Blog",
        "trust_strip_1": "Confidentialité avant tout",
        "trust_strip_2": "Traitement sécurisé",
        "trust_strip_3": "Lecture claire",
        "cta_after_brand": " — transformez vos résultats en synthèse structurée, prête à être partagée avec un soignant.",
        "mid_cta_title": "Envie de comprendre vos propres résultats ?",
        "mid_cta_desc": "Téléchargez votre bilan sanguin et obtenez une explication claire par IA.",
        "mid_cta_btn": "Essayer NoryaAI",
        "article_edu_note": "Ce guide est informatif ; il ne remplace ni un avis médical ni un diagnostic. Examinez toujours vos résultats avec un professionnel de santé.",
        "related_intro": "Pour aller plus loin : autres repères sur les biomarqueurs et le suivi.",
        "categories_aria": "Catégories",
        "articles_section_aria": "Articles",
        "lang_nav_aria": "Langue",
        "end_cta_nudge": "La plupart des rapports sont prêts en quelques minutes après l'import.",
        "lead_title": "Guides d'analyses sanguines et nouveautés",
        "lead_desc": "Recevez des rapports exemples, des guides de résultats de labo et des mises à jour sur les résumés prêts pour le médecin.",
        "lead_placeholder_email": "Votre adresse email",
        "lead_placeholder_name": "Votre nom (facultatif)",
        "lead_btn": "Me tenir informé",
        "lead_btn_loading": "Envoi en cours…",
        "lead_success": "Inscription réussie — merci !",
        "lead_already": "Cet email est déjà inscrit.",
        "lead_error_email": "Veuillez entrer un email valide.",
        "lead_error_generic": "Une erreur est survenue. Veuillez réessayer.",
        "lead_privacy": "Pas de spam. Désabonnement à tout moment.",
        "lead_consent_text": "J'accepte de recevoir des mises à jour par e-mail conformément à la politique KVKK/GDPR.",
        "lead_error_consent": "Veuillez accepter le consentement KVKK/GDPR.",
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
        "featured_label": "In evidenza",
        "filter_tags_label": "Argomenti",
        "filter_tags_title": "Filtra per argomento",
        "close_filter_drawer": "Chiudi filtro",
        "breadcrumb_aria": "Percorso di navigazione",
        "close_toc_drawer": "Chiudi indice",
        "breadcrumb_blog": "Blog",
        "trust_strip_1": "Privacy al centro",
        "trust_strip_2": "Elaborazione sicura",
        "trust_strip_3": "Chiarezza strutturata",
        "cta_after_brand": " — trasforma i risultati in un riepilogo chiaro e ordinato, utile al medico.",
        "mid_cta_title": "Vuoi capire i tuoi risultati?",
        "mid_cta_desc": "Carica le tue analisi del sangue e ottieni una spiegazione chiara con l'IA.",
        "mid_cta_btn": "Prova NoryaAI",
        "article_edu_note": "Questo contenuto è solo informativo; non sostituisce consulenza o diagnosi medica. Valuta sempre i risultati con un professionista.",
        "related_intro": "Altri approfondimenti sui biomarcatori e su un follow-up sensato.",
        "categories_aria": "Categorie",
        "articles_section_aria": "Articoli",
        "lang_nav_aria": "Lingua",
        "end_cta_nudge": "Molti report sono pronti in pochi minuti dopo il caricamento.",
        "lead_title": "Guide alle analisi del sangue e novità",
        "lead_desc": "Ricevi report di esempio, guide ai risultati di laboratorio e aggiornamenti sui riepiloghi per il medico nella tua casella.",
        "lead_placeholder_email": "Il tuo indirizzo email",
        "lead_placeholder_name": "Il tuo nome (facoltativo)",
        "lead_btn": "Tienimi aggiornato",
        "lead_btn_loading": "Invio in corso…",
        "lead_success": "Iscrizione avvenuta — grazie!",
        "lead_already": "Questa email è già registrata.",
        "lead_error_email": "Inserisci un'email valida.",
        "lead_error_generic": "Si è verificato un errore. Riprova.",
        "lead_privacy": "Niente spam. Cancella quando vuoi.",
        "lead_consent_text": "Acconsento a ricevere aggiornamenti via email in conformità con KVKK/GDPR.",
        "lead_error_consent": "Devi accettare il consenso KVKK/GDPR.",
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
        "meta_description": "Guías de interpretación y artículos sobre biomarcadores: ferritina, PCR, tiroides, colesterol. Claro y útil—para tu próxima consulta.",
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
        "featured_label": "Destacado",
        "filter_tags_label": "Temas",
        "filter_tags_title": "Filtrar por tema",
        "close_filter_drawer": "Cerrar filtro",
        "breadcrumb_aria": "Ruta de navegación",
        "close_toc_drawer": "Cerrar índice",
        "breadcrumb_blog": "Blog",
        "trust_strip_1": "Privacidad primero",
        "trust_strip_2": "Procesamiento seguro",
        "trust_strip_3": "Pensado para claridad",
        "cta_after_brand": " — convierta sus resultados en un informe estructurado y claro para compartir con su médico.",
        "mid_cta_title": "¿Quiere entender sus propios resultados?",
        "mid_cta_desc": "Suba su análisis de sangre y obtenga una explicación clara con IA.",
        "mid_cta_btn": "Probar NoryaAI",
        "article_edu_note": "Esta guía es informativa; no sustituye consejo ni diagnóstico médico. Revise siempre los resultados con un profesional.",
        "related_intro": "Más lecturas sobre biomarcadores, tendencias y seguimiento sensato.",
        "categories_aria": "Categorías",
        "articles_section_aria": "Artículos",
        "lang_nav_aria": "Idioma",
        "end_cta_nudge": "La mayoría de informes están listos en minutos tras subir el archivo.",
        "lead_title": "Guías de análisis de sangre y novedades",
        "lead_desc": "Recibe informes de ejemplo, guías de resultados de laboratorio y actualizaciones sobre resúmenes para el médico en tu correo.",
        "lead_placeholder_email": "Tu correo electrónico",
        "lead_placeholder_name": "Tu nombre (opcional)",
        "lead_btn": "Mantenme informado",
        "lead_btn_loading": "Enviando…",
        "lead_success": "¡Registro completado — gracias!",
        "lead_already": "Este correo ya está registrado.",
        "lead_error_email": "Introduce un correo válido.",
        "lead_error_generic": "Algo salió mal. Inténtalo de nuevo.",
        "lead_privacy": "Sin spam. Cancela cuando quieras.",
        "lead_consent_text": "Acepto recibir actualizaciones por correo según KVKK/GDPR.",
        "lead_error_consent": "Debe aceptar el consentimiento KVKK/GDPR.",
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
        "featured_label": "מאמר מומלץ",
        "filter_tags_label": "נושאים",
        "filter_tags_title": "סינון לפי נושא",
        "close_filter_drawer": "סגירת מסנן",
        "breadcrumb_aria": "שביל ניווט",
        "close_toc_drawer": "סגירת תוכן עניינים",
        "breadcrumb_blog": "בלוג",
        "trust_strip_1": "הפרטיות בראש",
        "trust_strip_2": "עיבוד מאובטח",
        "trust_strip_3": "בהיר ומסודר",
        "cta_after_brand": " — הפכו את תוצאות המעבדה לסיכום ברור ומובנה, מוכן לשיתוף עם הרופא.",
        "mid_cta_title": "רוצים להבין את התוצאות שלכם?",
        "mid_cta_desc": "העלו את בדיקת הדם וקבלו הסבר ברור באמצעות בינה מלאכותית.",
        "mid_cta_btn": "נסו את NoryaAI",
        "article_edu_note": "מדריך להעשרה בלבד; אינו מהווה ייעוץ רפואי או אבחון. יש להצליב תמיד עם רופא/ה.",
        "related_intro": "קראו עוד על מדדים, מגמות ומעקב נבון.",
        "categories_aria": "קטגוריות",
        "articles_section_aria": "מאמרים",
        "lang_nav_aria": "שפה",
        "end_cta_nudge": "רוב הדוחות מוכנים תוך דקות מהעלאת הקובץ.",
        "lead_title": "מדריכי בדיקות דם וחדשות",
        "lead_desc": "קבלו דוחות לדוגמה, מדריכי תוצאות מעבדה ועדכונים על סיכומים מוכנים לרופא ישירות למייל.",
        "lead_placeholder_email": "כתובת המייל שלך",
        "lead_placeholder_name": "השם שלך (אופציונלי)",
        "lead_btn": "עדכנו אותי",
        "lead_btn_loading": "שולח…",
        "lead_success": "נרשמת בהצלחה — תודה!",
        "lead_already": "מייל זה כבר רשום.",
        "lead_error_email": "נא להזין כתובת מייל תקינה.",
        "lead_error_generic": "אירעה שגיאה. נסה שוב.",
        "lead_privacy": "ללא ספאם. ביטול בכל עת.",
        "lead_consent_text": "אני מסכים לקבל עדכונים במייל בהתאם ל-KVKK/GDPR.",
        "lead_error_consent": "יש לאשר את הסכמת KVKK/GDPR.",
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
        "featured_label": "चुनिंदा लेख",
        "filter_tags_label": "विषय",
        "filter_tags_title": "विषय के अनुसार फ़िल्टर",
        "close_filter_drawer": "फ़िल्टर बंद करें",
        "breadcrumb_aria": "ब्रेडक्रंब",
        "close_toc_drawer": "विषय-सूची बंद करें",
        "breadcrumb_blog": "ब्लॉग",
        "trust_strip_1": "गोपनीयता पहले",
        "trust_strip_2": "सुरक्षित प्रसंस्करण",
        "trust_strip_3": "स्पष्ट प्रस्तुति",
        "cta_after_brand": " — अपने लैब रिज़ल्ट को संरचित, चिकित्सक-अनुकूल सारांश में बदलें।",
        "mid_cta_title": "अपने नतीजे समझना चाहते हैं?",
        "mid_cta_desc": "अपनी रक्त जाँच अपलोड करें और AI द्वारा स्पष्ट व्याख्या पाएँ।",
        "mid_cta_btn": "NoryaAI आज़माएँ",
        "article_edu_note": "यह मार्गदर्शन केवल जानकारी हेतु है; चिकित्सा सलाह या निदान नहीं। परिणाम हमेशा योग्य चिकित्सक के साथ साझा करें।",
        "related_intro": "बायोमार्कर और सही फ़ॉलो-अप पर और पढ़ें।",
        "categories_aria": "श्रेणियाँ",
        "articles_section_aria": "लेख",
        "lang_nav_aria": "भाषा",
        "end_cta_nudge": "अपलोड के बहुत से रिपोर्ट कुछ ही मिनटों में तैयार हो जाते हैं।",
        "lead_title": "रक्त परीक्षण गाइड और नई सुविधाएँ",
        "lead_desc": "नमूना रिपोर्ट, लैब परिणाम गाइड और डॉक्टर-रेडी सारांश अपडेट सीधे अपने इनबॉक्स में पाएँ।",
        "lead_placeholder_email": "आपका ईमेल पता",
        "lead_placeholder_name": "आपका नाम (वैकल्पिक)",
        "lead_btn": "मुझे अपडेट रखें",
        "lead_btn_loading": "भेजा जा रहा है…",
        "lead_success": "पंजीकरण सफल — धन्यवाद!",
        "lead_already": "यह ईमेल पहले से पंजीकृत है।",
        "lead_error_email": "कृपया एक मान्य ईमेल दर्ज करें।",
        "lead_error_generic": "कुछ गलत हो गया। कृपया पुनः प्रयास करें।",
        "lead_privacy": "कोई स्पैम नहीं। कभी भी अनसब्सक्राइब करें।",
        "lead_consent_text": "मैं KVKK/GDPR के अनुसार ईमेल अपडेट प्राप्त करने की सहमति देता/देती हूँ।",
        "lead_error_consent": "कृपया KVKK/GDPR सहमति स्वीकार करें।",
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
        "breadcrumb_blog": "المدونة",
        "trust_strip_1": "الخصوصية أولًا",
        "trust_strip_2": "معالجة آمنة",
        "trust_strip_3": "وضوح منظم",
        "cta_after_brand": " — حوّل نتائج المختبر إلى ملخص منظم وواضح يمكن مناقشته مع الطبيب.",
        "mid_cta_title": "هل تريد فهم نتائجك الخاصة؟",
        "mid_cta_desc": "ارفع تحليل الدم واحصل على شرح واضح بالذكاء الاصطناعي.",
        "mid_cta_btn": "جرّب NoryaAI",
        "article_edu_note": "هذا الدليل تثقيفي فقط؛ لا يغني عن استشارة طبية أو تشخيص. ناقش النتائج دائمًا مع مختص مؤهل.",
        "related_intro": "قراءات إضافية عن المؤشرات والاتجاهات والمتابعة المنطقية.",
        "categories_aria": "التصنيفات",
        "articles_section_aria": "المقالات",
        "lang_nav_aria": "اللغة",
        "end_cta_nudge": "كثير من التقارير تكون جاهزة خلال دقائق بعد الرفع.",
        "lead_title": "أدلة تحاليل الدم وآخر المستجدات",
        "lead_desc": "احصل على تقارير نموذجية، أدلة نتائج المختبر وتحديثات الملخصات الجاهزة للطبيب مباشرة في بريدك.",
        "lead_placeholder_email": "بريدك الإلكتروني",
        "lead_placeholder_name": "اسمك (اختياري)",
        "lead_btn": "أبقني على اطلاع",
        "lead_btn_loading": "جارٍ الإرسال…",
        "lead_success": "تم التسجيل — شكراً!",
        "lead_already": "هذا البريد مسجل بالفعل.",
        "lead_error_email": "يرجى إدخال بريد إلكتروني صحيح.",
        "lead_error_generic": "حدث خطأ. يرجى المحاولة مرة أخرى.",
        "lead_privacy": "لا رسائل مزعجة. إلغاء الاشتراك في أي وقت.",
        "lead_consent_text": "أوافق على تلقي تحديثات عبر البريد الإلكتروني وفقًا لـ KVKK/GDPR.",
        "lead_error_consent": "يرجى قبول موافقة KVKK/GDPR.",
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
    icon: Optional[str] = None  # optional icon path e.g. /static/images/blog/icons/slug.svg


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
            "hi": "एलडीएल (LDL) कोलेस्ट्रॉल कितना होना चाहिए और जोखिम कब बढ़ता है?",
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
<p>LDL ile birlikte sıklıkla konuşulan diğer lipid belirteçleri için ayrı rehberler: <a href="/tr/blog/apob-anlama-gelir">ApoB</a> · <a href="/tr/blog/lpa-anlama-gelir">Lp(a)</a>.</p>
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
<p>Clinicians sometimes also discuss <a href="/en/blog/apob-meaning">ApoB</a> (atherogenic particle load) and <a href="/en/blog/lpa-meaning">Lp(a)</a> (a genetically influenced lipoprotein) alongside LDL—these are separate markers and may not be on every basic panel.</p>
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
<p>Weitere Lipid‑Marker: <a href="/de/blog/apob-bedeutung">ApoB</a> · <a href="/de/blog/lpa-bedeutung">Lp(a)</a>.</p>
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
            "en": "Low Ferritin Meaning: What Low or High Ferritin Levels May Indicate",
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
            "en": "Low Ferritin Meaning, High Ferritin Causes, and Normal Ranges",
            "es": "Ferritina: niveles bajos y altos, rangos de referencia",
            "de": "Ferritin: Niedrige und hohe Werte, Referenzbereich, Ursachen",
            "fr": "Ferritine : taux bas ou élevé, fourchettes de référence et suites",
            "it": "Ferritina: valori bassi e alti, intervalli di riferimento e cosa fare",
            "he": "פריטין: ערכים נמוכים וגבוהים, טווחי נורמה",
            "hi": "फेरिटिन: कम और ज़्यादा स्तर, रेफरेंस रेंज",
            "ar": "الفيريتين: المستويات المنخفضة والمرتفعة ونطاقات المرجع",
        },
        seo_descriptions={
            "en": "Understand low ferritin meaning, high ferritin causes, normal ferritin ranges, and when to see a doctor. Clear guide to iron stores and follow-up tests.",
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
            "en": "High CRP Meaning: What Elevated CRP Levels Can Mean",
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
            "en": "High CRP Meaning, hs-CRP, and Causes of Elevated CRP Levels",
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
            "en": "Understand high CRP meaning, hs-CRP, common causes of elevated CRP levels, and when to follow up with a doctor. Educational guide only.",
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
            "en": "Low Vitamin D Meaning: How to Interpret 25(OH)D Results",
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
            "en": "Low Vitamin D Meaning, Normal Ranges, and 25(OH)D Interpretation",
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
            "en": "Understand low vitamin D meaning, 25(OH)D reference ranges, causes of low or high levels, and when to see a doctor. Informational only.",
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
            "en": "High or Low TSH Meaning: Thyroid Blood Test Explained",
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
            "en": "What TSH is, what high or low TSH means, how it relates to Free T4 and Free T3, and when to follow up with a clinician.",
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
            "en": "High or Low TSH Meaning: How to Interpret Thyroid Results | NoryaAI",
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
            "en": "Understand high or low TSH meaning, thyroid blood test patterns, Free T4 and Free T3, common causes, and when to see a clinician. Informational only.",
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
  <li><strong><a href="/en/blog/apob-meaning">ApoB</a></strong>: Reflects the number of atherogenic particles; sometimes used alongside or instead of LDL.</li>
  <li><strong><a href="/en/blog/lpa-meaning">Lp(a)</a></strong>: Genetically determined; high levels increase cardiovascular risk; one-time measurement often sufficient.</li>
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
            body_html="<p>Je nach Befund: <a href=\"/de/blog/apob-bedeutung\"><strong>ApoB</strong></a>, <a href=\"/de/blog/lpa-bedeutung\"><strong>Lp(a)</strong></a>, <strong>hs-CRP</strong>, <strong>HbA1c</strong>, <strong>TSH</strong>, Leber-/Nierenwerte, <strong>Risikorechner</strong>. Die Auswahl trifft der Arzt mit Ihnen.</p>"),
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
            body_html="<p>A seconda del quadro: <a href=\"/it/blog/significato-apob\"><strong>ApoB</strong></a>, <a href=\"/it/blog/significato-lpa\"><strong>Lp(a)</strong></a>, <strong>hs-CRP</strong>, <strong>HbA1c</strong>, <strong>TSH</strong>, funzione epatica/renale, <strong>calcolatori di rischio</strong>. La scelta è clinica.</p>"),
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
            body_html="<p>Selon le cas : <a href=\"/fr/blog/signification-apob\"><strong>ApoB</strong></a>, <a href=\"/fr/blog/signification-lpa\"><strong>Lp(a)</strong></a>, <strong>hs-CRP</strong>, <strong>HbA1c</strong>, <strong>TSH</strong>, fonction hépatique/rénale, <strong>calculateurs de risque</strong>. Le choix est clinique.</p>"),
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
            "en": "Understand creatinine and eGFR meaning, common kidney function categories, what can change results, and when doctors usually follow up.",
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
            "en": "Understand creatinine and eGFR meaning, common kidney function categories, what can affect results, and when doctors usually repeat or follow up these kidney markers.",
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
<p>If your kidney markers were part of a larger chemistry panel, see our <a href="/en/blog/metabolic-panel-results-explained">metabolic panel results explained</a> guide to understand how clinicians compare creatinine and eGFR with glucose, electrolytes, and liver-related markers. If you also had a urine test, our <a href="/en/blog/urine-acr-microalbumin-meaning">urine ACR / microalbumin guide</a> explains how albumin leakage adds another layer of kidney-risk context.</p>
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
        titles={"tr": "Demir eksikliği hangi kan değerlerinde görülür?", "en": "Iron Deficiency Blood Test Markers: Ferritin, Hemoglobin, and MCV", "de": "Eisenmangel im Blutbild erkennen", "fr": "Reconnaître une carence en fer dans les résultats", "it": "Come riconoscere la carenza di ferro negli esami", "es": "Cómo detectar la deficiencia de hierro en sangre", "he": "איך לזהות חוסר ברזל בתוצאות הדם?", "hi": "ब्लड रिज़ल्ट में आयरन की कमी कैसे पहचानें?", "ar": "كيف تتعرف على نقص الحديد في نتائج الدم؟"},
        subtitles={"tr": "Ferritin, hemoglobin, MCV ve diğer değerler demir eksikliğinde nasıl değişir? Kısa rehber.", "en": "Learn how ferritin, hemoglobin, MCV, and CBC patterns can help you spot iron deficiency in blood results.", "de": "Wie sich Ferritin, Hämoglobin, MCV bei Eisenmangel verändern. Kurzer Überblick.", "fr": "Comment la ferritine, l'hémoglobine et le VGM changent en cas de carence. Guide court.", "it": "Come cambiano ferritina, emoglobina e MCV in caso di carenza. Guida breve.", "es": "Cómo cambian ferritina, hemoglobina y VCM en la deficiencia de hierro. Guía breve.", "he": "איך פריטין, המוגלובין ו-MCV משתנים בחוסר ברזל. מדריך קצר.", "hi": "आयरन की कमी में फेरिटिन, हीमोग्लोबिन और MCV कैसे बदलते हैं। संक्षिप्त मार्गदर्शन।", "ar": "كيف تتغير الفيريتين والهيموغلوبين وMCV في نقص الحديد. دليل قصير."},
        excerpts={"tr": "Demir eksikliği tek bir değerle teşhis edilmez; ferritin ve tam kan sayımı birlikte değerlendirilir.", "en": "Iron deficiency is not diagnosed by one value; ferritin and full blood count are evaluated together.", "de": "Eisenmangel wird nicht durch einen Wert allein festgestellt; Ferritin und Blutbild zusammen.", "fr": "La carence en fer ne se diagnostique pas sur un seul chiffre ; ferritine et NFS ensemble.", "it": "La carenza di ferro non si diagnostica con un solo valore; ferritina ed emocromo insieme.", "es": "La deficiencia de hierro no se diagnostica con un solo valor; ferritina y hemograma juntos.", "he": "חוסר ברזל לא מאובחן לפי ערך אחד; פריטין וספירת דם מלאה ביחד.", "hi": "आयरन की कमी एक मान से निदान नहीं होती; फेरिटिन और पूर्ण रक्त गणना साथ में।", "ar": "نقص الحديد لا يُشخّص بقيمة واحدة؛ الفيريتين وعدّ الدم معاً."},
        seo_titles={"tr": "Demir Eksikliği Hangi Kan Değerlerinde Görülür? | Norya Blog", "en": "Iron Deficiency Blood Test Markers: Ferritin, Hemoglobin, and MCV | Norya Blog", "de": "Eisenmangel im Blutbild erkennen | Norya Blog", "fr": "Reconnaître une carence en fer dans les résultats | Norya Blog", "it": "Come riconoscere la carenza di ferro negli esami | Norya Blog", "es": "Cómo detectar la deficiencia de hierro en sangre | Norya Blog", "he": "איך לזהות חוסר ברזל בתוצאות הדם | Norya Blog", "hi": "ब्लड रिज़ल्ट में आयरन की कमी कैसे पहचानें | Norya Blog", "ar": "كيف تتعرف على نقص الحديد في نتائج الدم | Norya Blog"},
        seo_descriptions={"tr": "Ferritin, hemoglobin ve MCV ile demir eksikliği. Bilgilendirme amaçlı.", "en": "Learn how to spot iron deficiency in blood results using ferritin, hemoglobin, MCV, and CBC markers. Educational guide only.", "de": "Ferritin, Hämoglobin und MCV bei Eisenmangel. Nur zur Information.", "fr": "Ferritine, hémoglobine et VGM en cas de carence. À titre informatif.", "it": "Ferritina, emoglobina e MCV nella carenza di ferro. Solo informativo.", "es": "Ferritina, hemoglobina y VCM en la deficiencia de hierro. Solo informativo.", "he": "פריטין, המוגלובין ו-MCV בחוסר ברזל. למידע בלבד.", "hi": "आयरन की कमी में फेरिटिन, हीमोग्लोबिन और MCV. केवल सूचनार्थ।", "ar": "الفيريتين والهيموغلوبين وMCV في نقص الحديد. لأغراض إعلامية فقط."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Hangi kan değerleri?", body_html="<p><strong>Ferritin</strong> vücut demir depolarını yansıtır; düşük ferritin demir eksikliğini destekler. <strong>Hemoglobin</strong> (HGB) düşükse anemi olabilir. <strong>MCV</strong> (ortalama hücre hacmi) demir eksikliği anemisinde genellikle düşük veya normaldir. Tek başına bir değer teşhis koymaz; hekim tahlilleri birlikte yorumlar. Demir takviyesi hekim önerisiyle kullanılmalıdır.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> Sonuçlarınızı hekimle görüşün. <a href=\"/tr/hemogram-sonucu\">Hemogram sonucu</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="Which blood values?", body_html="<p><strong>Ferritin</strong> reflects body iron stores; low ferritin supports iron deficiency. <strong>Haemoglobin</strong> (HGB) may be low in anaemia. <strong>MCV</strong> (mean cell volume) is often low or normal in iron-deficiency anaemia. No single value makes a diagnosis; your doctor will interpret tests together. Iron supplements should be used on medical advice. You can also compare this pattern with our guides to <a href=\"/en/blog/ferritin-what-it-means\">ferritin</a> and <a href=\"/en/blog/hemoglobin-high-or-low-meaning\">hemoglobin</a>.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Discuss your results with a doctor. <a href=\"/en/blood-test-results\">Blood test results</a> · <a href=\"/en/upload-blood-test-results\">Upload blood test results</a> · <a href=\"/analyze\">Analyze</a></p>")],
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
    faq_qa = {
        "en": [
            {"question": "Can exercise raise ALT and AST?", "answer": "Yes. Intense exercise can temporarily raise AST and sometimes ALT, especially if muscles were heavily stressed. Your doctor may interpret the result together with symptoms, CK, and a repeat test if needed."},
            {"question": "Do high ALT and AST always mean liver disease?", "answer": "No. They often point toward liver-cell irritation or injury, but mild elevations can also be linked to alcohol, fatty liver, medications, viral illness, or heavy exercise. Interpretation depends on the full pattern and your history."},
            {"question": "When are high ALT and AST more urgent?", "answer": "Markedly abnormal results, jaundice, dark urine, severe abdominal pain, vomiting, confusion, or a rapidly worsening pattern need prompt medical review. Your clinician will decide whether urgent testing or referral is needed."},
        ]
    }
    return Article(
        id="alt-ast-yuksekligi-neyi-gosterir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        faq_schema_qa=faq_qa,
        cover_alt={"tr": "Karaciğer enzimleri ALT AST — Norya", "en": "Liver enzymes ALT AST — Norya", "de": "Leberenzyme ALT AST — Norya", "fr": "Enzymes hépatiques ALT AST — Norya", "it": "Enzimi epatici ALT AST — Norya", "es": "Enzimas hepáticas ALT AST — Norya", "he": "אנזימי כבד ALT AST — Norya", "hi": "लिवर एंजाइम ALT AST — Norya", "ar": "إنزيمات الكبد ALT AST — Norya"},
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "es": "Biomarcadores", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"},
        slugs={"tr": "alt-ve-ast-yuksekligi-neyi-gosterir", "en": "what-do-high-alt-and-ast-levels-mean", "de": "was-bedeuten-erhoehte-alt-und-ast-werte", "fr": "que-signifient-alt-ast-eleves", "it": "cosa-significano-alt-ast-alti", "es": "que-significan-alt-y-ast-altos", "he": "what-do-high-alt-and-ast-levels-mean", "hi": "high-alt-ast-levels-ka-matlab", "ar": "ma-dha-taani-mustawayat-alt-wa-ast-alalia"},
        titles={"tr": "ALT ve AST yüksekliği neyi gösterir?", "en": "High ALT and AST Meaning: Liver Enzymes Explained", "de": "Was bedeuten erhöhte ALT- und AST-Werte?", "fr": "Que signifient des ALT et AST élevés ?", "it": "Cosa significano ALT e AST alti?", "es": "¿Qué significan ALT y AST altos?", "he": "מה משמעות ערכי ALT ו-AST גבוהים?", "hi": "ALT और AST हाई लेवल का क्या मतलब है?", "ar": "ماذا تعني ارتفاع ALT وAST؟"},
        subtitles={"tr": "Karaciğer enzimleri yüksekliği nedenleri ve sonucunuzu nasıl değerlendireceğinize dair kısa rehber.", "en": "Understand common causes of high ALT and AST, what liver enzyme patterns may suggest, and when follow-up is usually needed.", "de": "Ursachen erhöhter Leberwerte und kurze Einordnung Ihres Befunds.", "fr": "Causes des enzymes hépatiques élevées et comment interpréter votre résultat.", "it": "Cause di enzimi epatici alti e come interpretare il risultato.", "es": "Causas de ALT y AST altos y cómo interpretar tu resultado.", "he": "סיבות לערכי כבד גבוהים ומדריך קצר לפרשנות.", "hi": "लिवर एंजाइम बढ़ने के कारण और अपने परिणाम की व्याख्या।", "ar": "أسباب ارتفاع إنزيمات الكبد وكيفية تفسير نتيجتك."},
        excerpts={"tr": "ALT ve AST yüksekliği tek başına teşhis değildir; hekim öykü ve gerekirse ek tetkiklerle değerlendirir.", "en": "Understand what high ALT and AST may mean, common liver enzyme causes, and why doctors often compare them with ALP, bilirubin, and GGT.", "de": "Erhöhte ALT/AST sind keine Diagnose; der Arzt beurteilt mit Anamnese und ggf. weiteren Tests.", "fr": "ALT et AST élevés seuls ne sont pas un diagnostic ; le médecin évalue avec l'histoire et examens.", "it": "ALT e AST alti da soli non sono una diagnosi; il medico valuta con anamnesi e eventuali esami.", "es": "ALT y AST altos por sí solos no son un diagnóstico; el médico valora con historia y pruebas.", "he": "ALT ו-AST גבוהים לבדם אינם אבחנה; הרופא יבדוק עם אנמנזה ובדיקות.", "hi": "ALT और AST अकेले निदान नहीं हैं; डॉक्टर इतिहास और टेस्ट से आंकलन करेंगे।", "ar": "ارتفاع ALT وAST وحدهما ليس تشخيصاً؛ الطبيب يقيّم مع التاريخ والفحوصات."},
        seo_titles={"tr": "ALT ve AST Yüksekliği Neyi Gösterir? | Norya Blog", "en": "High ALT and AST Meaning: Liver Enzymes Explained | Norya Blog", "de": "Was bedeuten erhöhte ALT- und AST-Werte? | Norya Blog", "fr": "Que signifient des ALT et AST élevés ? | Norya Blog", "it": "Cosa significano ALT e AST alti? | Norya Blog", "es": "¿Qué significan ALT y AST altos? | Norya Blog", "he": "מה משמעות ערכי ALT ו-AST גבוהים | Norya Blog", "hi": "ALT और AST हाई लेवल का क्या मतलब | Norya Blog", "ar": "ماذا تعني ارتفاع ALT وAST | Norya Blog"},
        seo_descriptions={"tr": "Karaciğer enzimleri ALT ve AST yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Understand high ALT and AST meaning, common liver enzyme causes, what patterns may suggest, and when doctors usually order more tests.", "de": "Ursachen für erhöhte Leberenzyme ALT und AST. Nur zur Information.", "fr": "Causes des ALT et AST élevés. À titre informatif.", "it": "Cause di ALT e AST alti. Solo informativo.", "es": "Causas de ALT y AST altos. Solo informativo.", "he": "סיבות ל-ALT ו-AST גבוהים. למידע בלבד.", "hi": "ALT और AST हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع ALT وAST. لأغراض إعلامية فقط."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="ALT ve AST yüksekliği neyi gösterir?", body_html="<p><strong>ALT</strong> ve <strong>AST</strong> karaciğer hücrelerinde bulunan enzimlerdir; hasar veya stres durumunda kanda yükselebilir. Hafif yükselmeler bazen ilaç, yağlanma veya enfeksiyonla ilişkili olabilir. Tek başına sayı teşhis koymaz; hekiminiz öykünüz, muayene ve gerekirse ek tetkiklerle değerlendirir. Belirgin veya sürekli yükseklikte mutlaka hekime danışın.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> Sonuçlarınızı hekimle görüşün. <a href=\"/analyze\">Analiz</a></p>")],
            "en": [
                Section(id="content", level=2, heading="What do high ALT and AST levels mean?", body_html="<p><strong>ALT</strong> and <strong>AST</strong> are enzymes found in liver cells; they can rise in blood with injury or stress. Mild rises may be linked to medication, fatty liver, alcohol, intense exercise, or infection. A number alone does not make a diagnosis; your doctor will assess with your history, examination, and further tests if needed. Doctors often compare ALT and AST with <a href=\"/en/blog/alp-high-meaning\">ALP</a>, bilirubin, or GGT to understand whether a pattern looks more liver-cell related or bile-duct related. Always see a doctor for marked or persistent elevation.</p>"),
                Section(id="quick-answer", level=2, heading="Quick answer", body_html="<div class=\"blog-definition\"><strong>Short answer:</strong> high ALT and AST usually mean liver cells are under stress, but the result does <em>not</em> tell the cause by itself. The next step is usually to compare the pattern with ALP, bilirubin, medications, alcohol exposure, fatty liver risk, and symptoms.</div>"),
                Section(id="pattern-guide", level=2, heading="Normal vs high: quick pattern guide", body_html="<div class=\"blog-example\"><strong>In range:</strong> usually means ALT and AST are within your lab's reference range, but symptoms and other markers can still matter.<br /><strong>Mildly high:</strong> often leads doctors to review alcohol, medicines, fatty liver risk, recent illness, and exercise.<br /><strong>Clearly high or rising:</strong> usually needs closer follow-up, especially if bilirubin, ALP, or symptoms are also abnormal.<br /><strong>Urgent pattern:</strong> jaundice, dark urine, severe abdominal pain, vomiting, confusion, or rapidly worsening values need prompt medical review.</div>"),
                Section(id="compare-pattern", level=2, heading="How doctors usually compare the pattern", body_html="<p>In simple terms, doctors often ask whether the pattern looks more <strong>liver-cell related</strong> or more <strong>bile-duct related</strong>. If ALT and AST are more prominent, the focus is often on liver-cell irritation. If <a href=\"/en/blog/alp-high-meaning\">ALP</a> and bilirubin are more prominent, attention may shift more toward bile flow or related pathways. This comparison does not diagnose the cause, but it helps decide what to check next.</p>"),
                Section(id="faq", level=2, heading="Frequently asked questions", body_html="<p><strong>Can exercise raise ALT and AST?</strong><br />Yes. Intense exercise can temporarily raise AST and sometimes ALT, especially if muscles were heavily stressed. Your doctor may interpret the result together with symptoms, CK, and a repeat test if needed.</p><p><strong>Do high ALT and AST always mean liver disease?</strong><br />No. They often point toward liver-cell irritation or injury, but mild elevations can also be linked to alcohol, fatty liver, medications, viral illness, or heavy exercise. Interpretation depends on the full pattern and your history.</p><p><strong>When are high ALT and AST more urgent?</strong><br />Markedly abnormal results, jaundice, dark urine, severe abdominal pain, vomiting, confusion, or a rapidly worsening pattern need prompt medical review. Your clinician will decide whether urgent testing or referral is needed.</p>"),
                Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Discuss your results with a doctor. Related guides: <a href=\"/en/blog/alp-high-meaning\">high ALP</a> · <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> · <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel</a>. If you want help with your own report, start with <a href=\"/en/blood-test-results-explained\">blood test results explained</a>, <a href=\"/en/upload-blood-test-results\">upload your blood test results</a>, or the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a>. <a href=\"/analyze\">Analyze</a></p>"),
            ],
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
    faq_qa = {
        "en": [
            {"question": "Can dehydration raise urea?", "answer": "Yes. Dehydration is one of the common reasons urea or BUN can rise, which is why doctors often compare it with creatinine, eGFR, and the clinical picture before drawing conclusions."},
            {"question": "Does a high urea result always mean kidney failure?", "answer": "No. High urea can be linked to dehydration, high protein intake, gastrointestinal bleeding, some medications, or reduced kidney function. The pattern needs to be interpreted with other kidney markers."},
            {"question": "Can a high-protein diet change my urea or BUN?", "answer": "Yes. Higher protein intake can increase urea production. Your clinician may consider diet, hydration, and other kidney markers when deciding whether the result is significant."},
        ]
    }
    return Article(
        id="ure-yuksekligi-ne-anlama-gelir",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        faq_schema_qa=faq_qa,
        cover_alt={"tr": "Üre kan tahlili — Norya", "en": "Urea blood test — Norya", "de": "Harnstoff Bluttest — Norya", "fr": "Urée sanguine — Norya", "it": "Urea nel sangue — Norya", "es": "Urea en sangre — Norya"},
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "es": "Biomarcadores"},
        slugs={"tr": "ure-yuksekligi-ne-anlama-gelir", "en": "what-does-a-high-urea-level-mean", "de": "was-bedeutet-ein-hoher-harnstoffwert", "fr": "que-signifie-uree-elevee", "it": "cosa-significa-urea-alta", "es": "que-significa-urea-alta"},
        titles={"tr": "Üre yüksekliği ne anlama gelir?", "en": "High Urea Meaning: BUN, Kidney Function, and Common Causes", "de": "Was bedeutet ein hoher Harnstoffwert?", "fr": "Que signifie un taux d'urée élevé ?", "it": "Cosa significa un valore di urea alto?", "es": "¿Qué significa un nivel de urea alto?"},
        subtitles={"tr": "Üre (BUN) referans aralıkları ve yüksek çıkmasının olası nedenleri. Kısa rehber.", "en": "Understand what a high urea or BUN result may mean, common causes, and how it is usually read with creatinine and eGFR.", "de": "Harnstoff (BUN): Referenzbereiche und mögliche Ursachen für einen hohen Wert.", "fr": "Urée (BUN) : fourchettes et causes possibles d'un taux élevé.", "it": "Urea (BUN): intervalli e possibili cause di un valore alto.", "es": "Urea (BUN): rangos y posibles causas de un nivel alto."},
        excerpts={"tr": "Üre yüksekliği tek başına teşhis değildir; böbrek fonksiyonu ve sıvı alımı hekimle değerlendirilir.", "en": "Understand high urea meaning, BUN causes, dehydration versus kidney-related patterns, and why doctors compare it with creatinine and eGFR.", "de": "Hoher Harnstoff allein ist keine Diagnose; Nierenfunktion und Flüssigkeit mit dem Arzt besprechen.", "fr": "Une urée élevée seule n'est pas un diagnostic ; fonction rénale et hydratation avec le médecin.", "it": "Urea alta da sola non è una diagnosi; funzione renale e idratazione con il medico.", "es": "Urea alta por sí sola no es un diagnóstico; función renal e hidratación con el médico."},
        seo_titles={"tr": "Üre Yüksekliği Ne Anlama Gelir? | Norya Blog", "en": "High Urea Meaning: BUN, Kidney Function, and Common Causes | Norya Blog", "de": "Was bedeutet ein hoher Harnstoffwert? | Norya Blog", "fr": "Que signifie un taux d'urée élevé ? | Norya Blog", "it": "Cosa significa urea alta? | Norya Blog", "es": "¿Qué significa urea alta? | Norya Blog"},
        seo_descriptions={"tr": "Üre (BUN) yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Understand high urea or BUN meaning, common causes like dehydration or kidney-related changes, and how doctors interpret it with creatinine and eGFR.", "de": "Ursachen für hohen Harnstoff (BUN). Nur zur Information.", "fr": "Causes d'une urée (BUN) élevée. À titre informatif.", "it": "Cause di urea (BUN) alta. Solo informativo.", "es": "Causas de urea (BUN) alta. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Üre yüksekliği ne anlama gelir?", body_html="<p><strong>Üre</strong> (bazen BUN) protein metabolizmasının bir ürünüdür; böbreklerden atılır. Yüksek çıkması böbrek fonksiyonunda azalma, susuzluk veya yüksek protein alımı gibi nedenlere bağlı olabilir. Tek başına teşhis koymaz; kreatinin ve eGFR ile birlikte hekim tarafından yorumlanır. Sonucunuzu hekimle görüşün.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [
                Section(id="content", level=2, heading="What does a high urea level mean?", body_html="<p><strong>Urea</strong> (sometimes BUN) is a product of protein metabolism and is cleared by the kidneys. A high level may be due to reduced kidney function, dehydration, gastrointestinal bleeding, or high protein intake. It does not make a diagnosis alone; doctors usually compare it with <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> to see whether the pattern looks more hydration-related, kidney-related, or temporary. Discuss your result with a doctor.</p>"),
                Section(id="quick-answer", level=2, heading="Quick answer", body_html="<div class=\"blog-definition\"><strong>Short answer:</strong> high urea or BUN often means the body is clearing more protein waste than usual or the kidneys are handling fluid and waste differently. By itself, it cannot tell whether the main issue is dehydration, diet, bleeding, medication effect, or reduced kidney function.</div>"),
                Section(id="pattern-guide", level=2, heading="Normal vs high: quick pattern guide", body_html="<div class=\"blog-example\"><strong>In range:</strong> often means protein waste handling looks typical for that lab, but kidney interpretation still depends on creatinine, eGFR, and context.<br /><strong>Mildly high:</strong> dehydration, higher protein intake, or temporary stressors may be considered first.<br /><strong>High together with other kidney markers:</strong> usually makes kidney-focused follow-up more important.<br /><strong>Urgent context:</strong> low urine output, confusion, vomiting, severe weakness, or rapidly changing kidney-related results need prompt medical review.</div>"),
                Section(id="compare-pattern", level=2, heading="How doctors compare urea with other kidney markers", body_html="<p>A common next step is to compare urea with <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a>. If urea is high but creatinine is relatively stable, dehydration, protein intake, or temporary factors may be considered. If several kidney markers move together, the result may deserve closer kidney-focused follow-up. This comparison guides the next questions, but it is not a diagnosis by itself.</p>"),
                Section(id="faq", level=2, heading="Frequently asked questions", body_html="<p><strong>Can dehydration raise urea?</strong><br />Yes. Dehydration is one of the common reasons urea or BUN can rise, which is why doctors often compare it with creatinine, eGFR, and the clinical picture before drawing conclusions.</p><p><strong>Does a high urea result always mean kidney failure?</strong><br />No. High urea can be linked to dehydration, high protein intake, gastrointestinal bleeding, some medications, or reduced kidney function. The pattern needs to be interpreted with other kidney markers.</p><p><strong>Can a high-protein diet change my urea or BUN?</strong><br />Yes. Higher protein intake can increase urea production. Your clinician may consider diet, hydration, and other kidney markers when deciding whether the result is significant.</p>"),
                Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> · <a href=\"/en/blog/sodium-low-meaning\">low sodium</a>. For your own lab report, see <a href=\"/en/blood-test-results-explained\">blood test results explained</a>, <a href=\"/en/upload-blood-test-results\">upload blood test results</a>, or the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a>. <a href=\"/analyze\">Analyze</a></p>"),
            ],
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
        titles={"tr": "Trombosit yüksekliği ve düşüklüğü ne demek?", "en": "Low or High Platelets Meaning: Platelet Count (PLT) Explained", "de": "Thrombozyten zu hoch oder zu niedrig?", "fr": "Plaquettes trop hautes ou trop basses : que signifie ?", "it": "Piastrine alte o basse: cosa significa?", "es": "¿Qué significan las plaquetas altas o bajas?"},
        subtitles={"tr": "Trombosit (PLT) referans aralıkları ve sapmaların olası nedenleri. Kısa rehber.", "en": "Understand platelet count (PLT), normal ranges, and common causes of low platelets or high platelets.", "de": "Thrombozyten (PLT): Referenzbereich und mögliche Ursachen für Abweichungen.", "fr": "Plaquettes (PLT) : fourchettes et causes possibles des écarts.", "it": "Piastrine (PLT): intervalli e possibili cause di valori alti o bassi.", "es": "Plaquetas (PLT): rangos y posibles causas de alteraciones."},
        excerpts={"tr": "Trombosit düşüklüğü veya yüksekliği tek başına teşhis değildir; hekim tüm tahlilleri birlikte yorumlar.", "en": "Low or high platelets alone are not a diagnosis; your doctor interprets all results together.", "de": "Thrombozyten zu niedrig oder zu hoch sind keine Diagnose; der Arzt wertet alle Befunde gemeinsam.", "fr": "Plaquettes basses ou hautes seules ne font pas un diagnostic ; le médecin interprète l'ensemble.", "it": "Piastrine basse o alte da sole non sono una diagnosi; il medico valuta tutti gli esami.", "es": "Plaquetas bajas o altas por sí solas no son un diagnóstico; el médico valora todos los resultados."},
        seo_titles={"tr": "Trombosit Yüksekliği ve Düşüklüğü Ne Demek? | Norya Blog", "en": "Low or High Platelets Meaning: Platelet Count (PLT) Explained | Norya Blog", "de": "Thrombozyten zu hoch oder zu niedrig? | Norya Blog", "fr": "Plaquettes trop hautes ou basses : que signifie ? | Norya Blog", "it": "Piastrine alte o basse: cosa significa? | Norya Blog", "es": "¿Qué significan plaquetas altas o bajas? | Norya Blog"},
        seo_descriptions={"tr": "Trombosit (PLT) yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "Understand low platelets or high platelets, platelet count ranges, common causes, and when to follow up. Educational guide only.", "de": "Ursachen für niedrige oder hohe Thrombozyten (PLT). Nur zur Information.", "fr": "Causes des plaquettes basses ou hautes (PLT). À titre informatif.", "it": "Cause di piastrine basse o alte (PLT). Solo informativo.", "es": "Causas de plaquetas bajas o altas (PLT). Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Trombosit yüksekliği ve düşüklüğü", body_html="<p><strong>Trombosit</strong> (PLT) kanın pıhtılaşmasında rol oynar. Referans aralığının altında veya üstünde çıkması çeşitli nedenlere bağlı olabilir; tek bir değer teşhis koymaz. Hekiminiz hemogram ve gerekirse ek tetkiklerle değerlendirir. Belirgin sapma veya kanama belirtisi varsa mutlaka hekime danışın.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/tr/hemogram-sonucu\">Hemogram</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What do low or high platelets mean?", body_html="<p><strong>Platelets</strong> (PLT) help blood to clot. A result below or above the reference range can have various causes; a single value does not make a diagnosis. Your doctor will assess with a full blood count and further tests if needed. If there is a marked change or signs of bleeding, see a doctor. For a wider CBC overview, see our guide to <a href=\"/en/blog/how-to-understand-wbc-rbc-hgb-and-hct\">WBC, RBC, HGB, and HCT</a>.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/en/blood-test-results\">Blood test results</a> · <a href=\"/en/upload-blood-test-results\">Upload blood test results</a> · <a href=\"/analyze\">Analyze</a></p>")],
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
        titles={"tr": "WBC, RBC, HGB, HCT nasıl okunur?", "en": "CBC Markers Explained: WBC, RBC, Hemoglobin, and Hematocrit", "de": "WBC, RBC, HGB und HCT verstehen", "fr": "Comprendre globules blancs, rouges, HGB et HCT", "it": "Come leggere WBC, RBC, HGB e HCT", "es": "Cómo entender WBC, RBC, HGB y HCT"},
        subtitles={"tr": "Tam kan sayımında beyaz küre, kırmızı küre, hemoglobin ve hematokrit ne anlama gelir? Kısa rehber.", "en": "Understand key CBC markers including WBC, RBC, hemoglobin, and hematocrit in one quick guide.", "de": "Was bedeuten weiße und rote Blutkörperchen, Hämoglobin und Hämatokrit im Blutbild? Kurzer Überblick.", "fr": "Que signifient globules blancs, rouges, hémoglobine et hématocrite dans la NFS ? Guide court.", "it": "Cosa significano globuli bianchi, rossi, emoglobina ed ematocrito nell'emocromo? Guida breve.", "es": "Qué significan glóbulos blancos, rojos, hemoglobina y hematocrito en el hemograma. Guía breve."},
        excerpts={"tr": "WBC, RBC, HGB ve HCT tam kan sayımının temel değerleridir; yorumu hekimle yapılır.", "en": "WBC, RBC, HGB and HCT are key values in a full blood count; interpretation is with a doctor.", "de": "WBC, RBC, HGB und HCT sind zentrale Werte im Blutbild; Einordnung durch den Arzt.", "fr": "Globules blancs/rouges, HGB et HCT sont des valeurs clés de la NFS ; interprétation avec le médecin.", "it": "WBC, RBC, HGB e HCT sono valori chiave dell'emocromo; interpretazione con il medico.", "es": "WBC, RBC, HGB y HCT son valores clave del hemograma; interpretación con el médico."},
        seo_titles={"tr": "WBC, RBC, HGB, HCT Nasıl Okunur? | Norya Blog", "en": "CBC Markers Explained: WBC, RBC, Hemoglobin, and Hematocrit | Norya Blog", "de": "WBC, RBC, HGB und HCT verstehen | Norya Blog", "fr": "Comprendre globules blancs, rouges, HGB et HCT | Norya Blog", "it": "Come leggere WBC, RBC, HGB e HCT | Norya Blog", "es": "Cómo entender WBC, RBC, HGB y HCT | Norya Blog"},
        seo_descriptions={"tr": "Tam kan sayımında WBC, RBC, hemoglobin ve hematokrit. Bilgilendirme amaçlı.", "en": "Understand CBC markers including WBC, RBC, hemoglobin, and hematocrit, plus what these blood count results may mean. Educational guide only.", "de": "WBC, RBC, Hämoglobin und Hämatokrit im Blutbild. Nur zur Information.", "fr": "Globules blancs/rouges, HGB et HCT dans la NFS. À titre informatif.", "it": "WBC, RBC, emoglobina ed ematocrito nell'emocromo. Solo informativo.", "es": "WBC, RBC, hemoglobina y hematocrito en el hemograma. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="WBC, RBC, HGB, HCT ne demek?", body_html="<p><strong>WBC</strong> (lökosit) beyaz kan hücreleri; enfeksiyon veya iltihap durumunda değişebilir. <strong>RBC</strong> (eritrosit) kırmızı kan hücreleri; <strong>HGB</strong> (hemoglobin) oksijen taşır; <strong>HCT</strong> (hematokrit) kırmızı hücrelerin kandaki oranıdır. Referans aralıkları laboratuvara göre değişir. Sonucunuzu raporunuzdaki aralıklarla ve hekiminizle değerlendirin.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/tr/hemogram-sonucu\">Hemogram</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What do WBC, RBC, HGB and HCT mean?", body_html="<p><strong>WBC</strong> (white blood cells) can change with infection or inflammation. <strong>RBC</strong> (red blood cells), <strong>HGB</strong> (haemoglobin) carries oxygen, and <strong>HCT</strong> (haematocrit) is the proportion of red cells in blood. Reference ranges vary by lab. Interpret your result using the ranges on your report and with your doctor. If one marker is abnormal, you may also want to compare with our focused guides to <a href=\"/en/blog/hemoglobin-high-or-low-meaning\">hemoglobin</a> and <a href=\"/en/blog/what-do-low-or-high-platelets-mean\">platelets</a>.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/en/understand-lab-results\">Lab results</a> · <a href=\"/en/upload-blood-test-results\">Upload blood test results</a> · <a href=\"/analyze\">Analyze</a></p>")],
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
        titles={"tr": "Açlık kan şekeri sonucu nasıl değerlendirilir?", "en": "High Fasting Blood Sugar Meaning: Normal, Prediabetes, and Diabetes Ranges", "de": "Nüchternblutzucker verstehen", "fr": "Comment lire la glycémie à jeun ?", "it": "Come leggere la glicemia a digiuno?", "es": "¿Cómo leer la glucosa en ayunas?"},
        subtitles={"tr": "Açlık glukozu referans aralıkları ve sonucunuzu nasıl yorumlayacağınıza dair kısa rehber.", "en": "Learn what fasting glucose measures, what high fasting blood sugar can mean, and how normal, prediabetes, and diabetes ranges are usually interpreted.", "de": "Referenzbereiche für Nüchternglukose und kurze Einordnung.", "fr": "Fourchettes de référence pour la glycémie à jeun et comment interpréter.", "it": "Intervalli di riferimento per la glicemia a digiuno e come interpretare.", "es": "Rangos de referencia para glucosa en ayunas y cómo interpretar."},
        excerpts={"tr": "Açlık kan şekeri tek başına teşhis değildir; diyabet veya prediyabet hekim tarafından değerlendirilir.", "en": "Understand what high fasting blood sugar means, where prediabetes starts, and why doctors often compare fasting glucose with HbA1c or OGTT.", "de": "Nüchternblutzucker allein ist keine Diagnose; Diabetes/Prädiabetes beurteilt der Arzt.", "fr": "La glycémie à jeun seule ne fait pas un diagnostic ; diabète ou prédiabète avec le médecin.", "it": "La glicemia a digiuno da sola non è una diagnosi; diabete o prediabete con il medico.", "es": "La glucosa en ayunas por sí sola no es un diagnóstico; diabetes o prediabetes con el médico."},
        seo_titles={"tr": "Açlık Kan Şekeri Sonucu Nasıl Değerlendirilir? | Norya Blog", "en": "High Fasting Blood Sugar Meaning: Normal, Prediabetes, and Diabetes Ranges | NoryaAI", "de": "Nüchternblutzucker verstehen | Norya Blog", "fr": "Comment lire la glycémie à jeun ? | Norya Blog", "it": "Come leggere la glicemia a digiuno? | Norya Blog", "es": "¿Cómo leer la glucosa en ayunas? | Norya Blog"},
        seo_descriptions={"tr": "Açlık kan şekeri referans aralıkları ve yorumlama. Bilgilendirme amaçlı.", "en": "What does high fasting blood sugar mean? See normal fasting glucose, prediabetes, and diabetes ranges, plus when HbA1c or OGTT may be used for follow-up.", "de": "Nüchternblutzucker: Referenzbereiche und Einordnung. Nur zur Information.", "fr": "Glycémie à jeun : fourchettes et interprétation. À titre informatif.", "it": "Glicemia a digiuno: intervalli e interpretazione. Solo informativo.", "es": "Glucosa en ayunas: rangos e interpretación. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Açlık kan şekeri nasıl değerlendirilir?", body_html="<p><strong>Açlık kan şekeri</strong> (glukoz) genellikle 8–12 saat açlık sonrası ölçülür. Referans aralıkları laboratuvara göre değişir; yüksek çıkması diyabet veya prediyabet açısından değerlendirilir. Tek bir ölçüm teşhis koymaz; hekiminiz HbA1c veya OGTT gibi ek testlerle karar verir. Sonucunuzu hekimle görüşün.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What high fasting blood sugar can mean", body_html="<p><strong>Fasting blood sugar</strong> (fasting glucose) is usually measured after 8-12 hours of fasting. In many labs, normal fasting glucose is below 100 mg/dL, <strong>prediabetes</strong> starts around 100-125 mg/dL, and <strong>diabetes</strong> may be considered at 126 mg/dL or above on repeat testing. Exact ranges can vary by lab and guideline.</p><p>A single high fasting glucose result does not diagnose diabetes on its own. Doctors often compare it with <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c</a>, and sometimes with an OGTT, to understand whether the pattern fits prediabetes, diabetes, or a temporary change. If you also want to understand early insulin resistance, see our <a href=\"/en/blog/what-is-homa-ir\">HOMA-IR guide</a>.</p><p>If the result comes from a chemistry panel, our <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel guide</a> shows how glucose is usually read alongside sodium, potassium, bicarbonate, and kidney markers.</p><p>Discuss your result with a clinician, especially if you have repeat high values, symptoms of high blood sugar, or a family history of diabetes.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c result meaning</a> · <a href=\"/en/blog/what-is-homa-ir\">HOMA-IR</a> · <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel</a> · <a href=\"/analyze\">Analyze</a></p>")],
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
        titles={"tr": "HbA1c sonucu ne anlama gelir?", "en": "What Does an HbA1c Result Mean? Normal, Prediabetes, and Diabetes Ranges", "de": "HbA1c verstehen: Was bedeutet der Wert?", "fr": "HbA1c : que signifie le résultat ?", "it": "HbA1c: cosa significa il valore?", "es": "¿Qué significa un resultado de HbA1c?"},
        subtitles={"tr": "HbA1c son 2–3 aydaki ortalama kan şekerini yansıtır. Referans aralıkları ve yorumlama.", "en": "HbA1c reflects average blood sugar over the last 2-3 months. Learn how normal, prediabetes, and diabetes ranges are usually interpreted.", "de": "HbA1c spiegelt den durchschnittlichen Blutzucker der letzten 2–3 Monate wider. Referenzbereiche und Einordnung.", "fr": "L'HbA1c reflète la glycémie moyenne sur 2–3 mois. Fourchettes et interprétation.", "it": "L'HbA1c riflette la glicemia media degli ultimi 2–3 mesi. Intervalli e interpretazione.", "es": "La HbA1c refleja el promedio de glucosa de los últimos 2–3 meses. Rangos e interpretación."},
        excerpts={"tr": "HbA1c diyabet taraması ve takipte kullanılır; yorumu hekimle yapılır.", "en": "See what an HbA1c result may mean, where prediabetes and diabetes ranges begin, and why fasting glucose is often checked alongside it.", "de": "HbA1c wird zur Diabetesscreening und -kontrolle genutzt; Einordnung durch den Arzt.", "fr": "L'HbA1c sert au dépistage et au suivi du diabète ; interprétation avec le médecin.", "it": "L'HbA1c si usa per screening e monitoraggio del diabete; interpretazione con il medico.", "es": "La HbA1c se usa para cribado y seguimiento de la diabetes; interpretación con el médico."},
        seo_titles={"tr": "HbA1c Sonucu Ne Anlama Gelir? | Norya Blog", "en": "What Does an HbA1c Result Mean? Normal, Prediabetes, and Diabetes Ranges | NoryaAI", "de": "HbA1c verstehen: Was bedeutet der Wert? | Norya Blog", "fr": "HbA1c : que signifie le résultat ? | Norya Blog", "it": "HbA1c: cosa significa il valore? | Norya Blog", "es": "¿Qué significa un resultado de HbA1c? | Norya Blog"},
        seo_descriptions={"tr": "HbA1c referans aralıkları ve ne anlama geldiği. Bilgilendirme amaçlı.", "en": "What does an HbA1c result mean? Understand normal, prediabetes, and diabetes ranges, plus how HbA1c compares with fasting glucose in blood sugar assessment.", "de": "HbA1c: Referenzbereiche und Bedeutung. Nur zur Information.", "fr": "HbA1c : fourchettes et signification. À titre informatif.", "it": "HbA1c: intervalli e significato. Solo informativo.", "es": "HbA1c: rangos y significado. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="HbA1c sonucu ne anlama gelir?", body_html="<p><strong>HbA1c</strong> son 2–3 aydaki ortalama kan şekerini tahmin etmek için kullanılır; diyabet tanısı ve takipte önemlidir. Referans aralıkları laboratuvara göre değişir; genelde yüzde (%) veya mmol/mol birimiyle raporlanır. Tek başına teşhis koymaz; hekiminiz açlık glukozu veya diğer testlerle birlikte değerlendirir.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What an HbA1c result may mean", body_html="<p><strong>HbA1c</strong> estimates your average blood sugar over the last 2-3 months and is widely used for diabetes screening and follow-up. In many guidelines, below 5.7% is considered normal, 5.7-6.4% falls in the <strong>prediabetes</strong> range, and 6.5% or above may support a diagnosis of <strong>diabetes</strong> when confirmed appropriately. Results may also be reported in mmol/mol.</p><p>HbA1c does not make a diagnosis on its own. Your doctor may compare it with <a href=\"/en/blog/how-to-read-fasting-blood-sugar-results\">fasting glucose</a>, symptoms, repeat testing, or other markers to understand the full picture. If you are trying to understand earlier metabolic changes, our <a href=\"/en/blog/what-is-homa-ir\">HOMA-IR guide</a> can also help.</p><p>If glucose was part of a CMP or BMP, see our <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel guide</a> for how clinicians place one blood sugar value into wider chemistry context.</p><p>Certain conditions such as anemia, hemoglobin variants, kidney disease, or recent blood loss can affect HbA1c interpretation, which is another reason to review the result with a clinician.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/how-to-read-fasting-blood-sugar-results\">Fasting glucose</a> · <a href=\"/en/blog/what-is-homa-ir\">HOMA-IR</a> · <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel</a> · <a href=\"/analyze\">Analyze</a></p>")],
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
        titles={"tr": "Kan tahlilinde kolesterol türleri nasıl anlaşılır?", "en": "Cholesterol Blood Test Explained: LDL, HDL, Triglycerides, and Total Cholesterol", "de": "Cholesterin im Bluttest richtig einordnen", "fr": "Comprendre les types de cholestérol dans le bilan sanguin", "it": "Come capire i tipi di colesterolo negli esami", "es": "Cómo entender los tipos de colesterol en el análisis"},
        subtitles={"tr": "Total kolesterol, LDL, HDL ve trigliserit ne anlama gelir? Kısa rehber.", "en": "Understand what total cholesterol, LDL, HDL, and triglycerides mean in a standard cholesterol blood test.", "de": "Was Gesamtcholesterin, LDL, HDL und Triglyceride bedeuten. Kurzer Überblick.", "fr": "Que signifient cholestérol total, LDL, HDL et triglycérides. Guide court.", "it": "Cosa significano colesterolo totale, LDL, HDL e trigliceridi. Guida breve.", "es": "Qué significan colesterol total, LDL, HDL y triglicéridos. Guía breve."},
        excerpts={"tr": "Kolesterol türleri tek başına risk göstermez; hekim tüm değerleri ve risk faktörlerini birlikte değerlendirir.", "en": "Cholesterol types alone do not define risk; your doctor assesses all values and risk factors together.", "de": "Cholesterinwerte allein definieren kein Risiko; der Arzt beurteilt alle Werte und Risikofaktoren.", "fr": "Les types de cholestérol seuls ne définissent pas le risque ; le médecin évalue l'ensemble.", "it": "I tipi di colesterolo da soli non definiscono il rischio; il medico valuta tutti i valori.", "es": "Los tipos de colesterol por sí solos no definen el riesgo; el médico valora todos los valores."},
        seo_titles={"tr": "Kan Tahlilinde Kolesterol Türleri Nasıl Anlaşılır? | Norya Blog", "en": "Cholesterol Blood Test Explained: LDL, HDL, Triglycerides, and Total Cholesterol | Norya Blog", "de": "Cholesterin im Bluttest richtig einordnen | Norya Blog", "fr": "Comprendre les types de cholestérol dans le bilan | Norya Blog", "it": "Come capire i tipi di colesterolo negli esami | Norya Blog", "es": "Cómo entender los tipos de colesterol en el análisis | Norya Blog"},
        seo_descriptions={"tr": "Total kolesterol, LDL, HDL, trigliserit. Bilgilendirme amaçlı.", "en": "Understand total cholesterol, LDL, HDL, and triglycerides, plus how a cholesterol blood test is usually interpreted. Educational guide only.", "de": "Gesamtcholesterin, LDL, HDL, Triglyceride. Nur zur Information.", "fr": "Cholestérol total, LDL, HDL, triglycérides. À titre informatif.", "it": "Colesterolo totale, LDL, HDL, trigliceridi. Solo informativo.", "es": "Colesterol total, LDL, HDL, triglicéridos. Solo informativo."},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Kolesterol türleri nasıl anlaşılır?", body_html="<p><strong>Total kolesterol</strong> tüm kolesterol türlerinin toplamıdır. <strong>LDL</strong> (\"kötü\" kolesterol) damar riskiyle ilişkilidir; <strong>HDL</strong> (\"iyi\" kolesterol) koruyucu kabul edilir. <strong>Trigliserit</strong> kan yağıdır. Referans aralıkları laboratuvara göre değişir; hedef değerler kardiyovasküler riskinize göre belirlenir. Sonucunuzu hekimle görüşün. Ek bağlam için: <a href=\"/tr/blog/apob-anlama-gelir\">ApoB</a> · <a href=\"/tr/blog/lpa-anlama-gelir\">Lp(a)</a>.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/tr/kan-degerleri-anlama\">Kan değerleri</a> · <a href=\"/pricing\">Fiyatlar</a> · <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="How to understand cholesterol types", body_html="<p><strong>Total cholesterol</strong> is the sum of all cholesterol types. <strong>LDL</strong> (\"bad\" cholesterol) is linked to vascular risk; <strong>HDL</strong> (\"good\" cholesterol) is considered protective. <strong>Triglycerides</strong> are blood fats. Reference ranges vary by lab; targets depend on your cardiovascular risk. Discuss your result with a doctor. For a deeper marker-by-marker view, compare with our <a href=\"/en/blog/ldl-cholesterol-level\">LDL cholesterol</a> and <a href=\"/en/blog/ldl-vs-hdl-what-it-means\">LDL vs HDL</a> guides, plus dedicated explainers for <a href=\"/en/blog/apob-meaning\">ApoB</a> and <a href=\"/en/blog/lpa-meaning\">Lp(a)</a>.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> <a href=\"/en/understand-lab-results\">Lab results</a> · <a href=\"/en/blood-test-results\">Blood test interpretation online</a> · <a href=\"/pricing\">Pricing</a> · <a href=\"/analyze\">Analyze</a></p>")],
            "de": [Section(id="content", level=2, heading="Cholesterin im Bluttest einordnen", body_html="<p><strong>Gesamtcholesterin</strong> ist die Summe aller Cholesterinanteile. <strong>LDL</strong> (\"schlechtes\" Cholesterin) ist mit Gefäßrisiko verbunden; <strong>HDL</strong> (\"gutes\" Cholesterin) gilt als schützend. <strong>Trigyceride</strong> sind Blutfette. Referenzbereiche sind laborabhängig; Ziele hängen vom kardiovaskulären Risiko ab. Befund mit dem Arzt besprechen. Vertiefung: <a href=\"/de/blog/apob-bedeutung\">ApoB</a> · <a href=\"/de/blog/lpa-bedeutung\">Lp(a)</a>.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/de/laborwerte-verstehen\">Laborwerte</a> · <a href=\"/pricing\">Preise</a> · <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Comprendre les types de cholestérol", body_html="<p>Le <strong>cholestérol total</strong> est la somme des fractions. Le <strong>LDL</strong> (\"mauvais\") est lié au risque vasculaire ; le <strong>HDL</strong> (\"bon\") est protecteur. Les <strong>triglycérides</strong> sont des graisses sanguines. Les fourchettes varient selon le laboratoire ; les cibles dépendent du risque cardiovasculaire. Discutez du résultat avec un médecin. Pour aller plus loin : <a href=\"/fr/blog/signification-apob\">ApoB</a> · <a href=\"/fr/blog/signification-lpa\">Lp(a)</a>.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/pricing\">Tarifs</a> · <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Come capire i tipi di colesterolo", body_html="<p>Il <strong>colesterolo totale</strong> è la somma delle frazioni. <strong>LDL</strong> (\"cattivo\") è legato al rischio vascolare; <strong>HDL</strong> (\"buono\") è protettivo. I <strong>trigliceridi</strong> sono grassi nel sangue. Gli intervalli variano da laboratorio; gli obiettivi dipendono dal rischio cardiovascolare. Discuti il risultato con il medico. Approfondimenti: <a href=\"/it/blog/significato-apob\">ApoB</a> · <a href=\"/it/blog/significato-lpa\">Lp(a)</a>.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/pricing\">Prezzi</a> · <a href=\"/analyze\">Analizza</a></p>")],
            "es": [Section(id="content", level=2, heading="Cómo entender los tipos de colesterol", body_html="<p>El <strong>colesterol total</strong> es la suma de las fracciones. <strong>LDL</strong> (\"malo\") se asocia a riesgo vascular; <strong>HDL</strong> (\"bueno\") es protector. Los <strong>triglicéridos</strong> son grasas en sangre. Los rangos varían por laboratorio; los objetivos dependen del riesgo cardiovascular. Comenta el resultado con un médico. Más contexto: <a href=\"/es/blog/significado-apob\">ApoB</a> · <a href=\"/es/blog/significado-lpa\">Lp(a)</a>.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/pricing\">Precios</a> · <a href=\"/analyze\">Analizar</a></p>")],
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


def _article_albumin_low() -> Article:
    """Albumin düşüklüğü / Low albumin — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/albumin-low-hero.png"
    slugs = {l: "albumin-low-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(
        id="albumin-low-meaning",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        icon="/static/images/blog/icons/albumin-low-meaning.svg",
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"},
        slugs=slugs,
        titles={"tr": "Albumin düşük çıkarsa ne olur?", "en": "Low Albumin Meaning: Common Causes and What It May Suggest", "es": "Albúmina baja: ¿qué implica?", "de": "Albumin zu niedrig: Was bedeutet der Wert?", "fr": "Albumine basse : qu'est-ce que ça indique ?", "it": "Albumina bassa: cosa significa?", "he": "מה המשמעות של אלבומין נמוך?", "hi": "ऐल्ब्यूमिन लो का क्या मतलब है?", "ar": "ماذا يعني انخفاض الألبومين؟"},
        subtitles={"tr": "Albumin karaciğer, böbrek ve beslenme ile ilişkili bir proteindir; düşüklüğü hekimle birlikte değerlendirilir.", "en": "Low albumin can be linked to liver, kidney, inflammation, or nutrition-related problems, but it is interpreted together with the rest of your blood work.", "es": "La albúmina es una proteína ligada a hígado, riñón y nutrición; un valor bajo se valora con el médico.", "de": "Albumin ist ein mit Leber, Niere und Ernährung zusammenhängendes Eiweiß; Niedrigwerte beurteilt der Arzt.", "fr": "L'albumine est une protéine liée au foie, au rein et à la nutrition ; un taux bas est évalué avec le médecin.", "it": "L'albumina è una proteina legata a fegato, rene e nutrizione; un valore basso si valuta con il medico.", "he": "אלבומין קשור לכבד, כליות ותזונה; ערך נמוך יבדוק עם הרופא.", "hi": "ऐल्ब्यूमिन लिवर, किडनी और पोषण से जुड़ा प्रोटीन है; लो लेवल डॉक्टर के साथ आंकलन।", "ar": "الألبومين بروتين مرتبط بالكبد والكلية والتغذية؛ انخفاضه يقيّم مع الطبيب."},
        excerpts={"tr": "Albumin kanda taşınan bir proteindir; düşüklüğü tek başına teşhis değildir—karaciğer, böbrek veya beslenme hekimle birlikte değerlendirilir.", "en": "See what low albumin may mean, common causes behind a low result, and why doctors often compare albumin with total protein and liver or kidney tests.", "es": "La albúmina es una proteína que circula en sangre. Un valor bajo por sí solo no es un diagnóstico; el médico valora hígado, riñón y nutrición.", "de": "Albumin ist ein im Blut vorkommendes Eiweiß. Ein niedriger Wert allein ist keine Diagnose—Leber, Niere und Ernährung beurteilt der Arzt gemeinsam.", "fr": "L'albumine est une protéine du sang. Un taux bas seul ne fait pas un diagnostic ; le médecin évalue foie, rein et nutrition.", "it": "L'albumina è una proteina del sangue. Un valore basso da solo non è una diagnosi; il medico valuta fegato, rene e nutrizione.", "he": "אלבומין הוא חלבון בדם. ערך נמוך לבדו אינו אבחנה—הרופא יבדוק כבד, כליות ותזונה.", "hi": "ऐल्ब्यूमिन खून में मौजूद प्रोटीन है। लो लेवल अकेले निदान नहीं—डॉक्टर लिवर, किडनी और पोषण साथ देखेंगे।", "ar": "الألبومين بروتين في الدم. انخفاضه وحده ليس تشخيصاً—الطبيب يقيّم الكبد والكلية والتغذية معاً."},
        seo_titles={"tr": "Albumin Düşüklüğü Ne Anlama Gelir? | Norya Blog", "en": "Low Albumin Meaning: Common Causes and What It May Suggest | NoryaAI", "es": "Albúmina baja: ¿qué implica? | Norya Blog", "de": "Albumin zu niedrig: Was bedeutet der Wert? | Norya Blog", "fr": "Albumine basse : qu'est-ce que ça indique ? | Norya Blog", "it": "Albumina bassa: cosa significa? | Norya Blog", "he": "מה המשמעות של אלבומין נמוך? | Norya Blog", "hi": "ऐल्ब्यूमिन लो का क्या मतलब है? | Norya Blog", "ar": "ماذا يعني انخفاض الألبومين؟ | Norya Blog"},
        seo_descriptions={"tr": "Albumin düşüklüğü nedenleri. Bilgilendirme amaçlı.", "en": "What does low albumin mean? Learn common causes of low albumin and how doctors interpret it with total protein, liver tests, kidney markers, and nutrition status.", "es": "Albúmina baja: causas. Solo informativo.", "de": "Ursachen für niedriges Albumin. Nur zur Information.", "fr": "Albumine basse : causes. À titre informatif.", "it": "Albumina bassa: cause. Solo informativo.", "he": "סיבות לאלבומין נמוך. למידע בלבד.", "hi": "ऐल्ब्यूमिन लो के कारण. केवल सूचनार्थ।", "ar": "أسباب انخفاض الألبومين. لأغراض إعلامية فقط."},
        cover_alt={"tr": "Albumin kan tahlili — Norya", "en": "Albumin blood test — Norya", "es": "Albúmina análisis — Norya", "de": "Albumin Bluttest — Norya", "fr": "Albumine sanguine — Norya", "it": "Albumina esami — Norya", "he": "בדיקת אלבומין — Norya", "hi": "ऐल्ब्यूमिन ब्लड टेस्ट — Norya", "ar": "تحليل الألبومين — Norya"},
        sections_by_lang={
            "tr": [
                Section(id="nedir", level=2, heading="Albumin nedir?", body_html="<p><strong>Albumin</strong> kanda taşınan başlıca proteinlerden biridir; karaciğerde üretilir. Sıvının damar içinde kalmasına yardımcı olur, hormon ve ilaç gibi maddelerin taşınmasında rol oynar. Rutin biyokimyada sıklıkla ölçülür; sonuç tek başına tanı koymaz.</p>"),
                Section(id="neden-dusuk", level=2, heading="Albumin neden düşük çıkar?", body_html="<p>Düşüklük karaciğer veya böbrek hastalığı, uzun süreli açlık veya yetersiz protein alımı, ciddi enfeksiyon veya iltihap, bağırsakta protein kaybı gibi durumlarla ilişkili olabilir. Hekiminiz öykü, muayene ve diğer tetkiklerle (total protein, karaciğer ve böbrek testleri) birlikte değerlendirir.</p>"),
                Section(id="ne-yapmali", level=2, heading="Sonuç nasıl yorumlanır?", body_html="<p>Referans aralığı laboratuvara göre değişir. Tek bir düşük değer her zaman ciddi bir hastalık anlamına gelmez; hafif düşüklük bazen geçici veya beslenmeyle ilgili olabilir. Yorum ve gerekirse ek tetkik kararı mutlaka hekim tarafından yapılmalıdır.</p>"),
                Section(id="cta", level=2, heading="Sonuçlarınızı netleştirin", body_html="<p>Kan tahlili sonuçlarınızı yapılandırılmış bir özet halinde görmek isterseniz <a href=\"/analyze\">analiz sayfamızdan</a> raporunuzu oluşturabilirsiniz. Teşhis ve tedavi için hekiminizle görüşün.</p>"),
                Section(id="uyari", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> Teşhis veya tedavi yerine geçmez. Sonuçlarınızı hekimle görüşün.</p>"),
            ],
            "en": [
                Section(id="what-is", level=2, heading="What is albumin?", body_html="<p><strong>Albumin</strong> is one of the main proteins in your blood; it is made in the liver. It helps keep fluid inside the blood vessels and plays a role in carrying hormones and some medicines. It is often measured in routine blood chemistry; a single result does not make a diagnosis.</p>"),
                Section(id="why-low", level=2, heading="Why might albumin be low?", body_html="<p>Low levels can be linked to liver or kidney disease, long-term poor intake or malnutrition, serious infection or inflammation, or protein loss from the gut. Your doctor will consider your history, examination, and other tests such as <a href=\"/en/blog/total-protein-high-or-low\">total protein</a>, liver markers, and kidney markers together.</p>"),
                Section(id="how-to-read", level=2, heading="How is the result interpreted?", body_html="<p>Reference ranges vary by lab. One low value does not always mean a serious condition; a mild drop can sometimes be temporary or diet-related. Interpretation and any follow-up tests should be done by your doctor. Looking at albumin next to <a href=\"/en/blog/total-protein-high-or-low\">total protein</a> and the <a href=\"/en/blog/globulin-high-or-low\">globulin</a> portion can help explain the pattern.</p>"),
                Section(id="cta", level=2, heading="Make sense of your results", body_html="<p>If you want to see your blood results in a clear, structured summary, you can <a href=\"/analyze\">run an analysis</a>. Related guides: <a href=\"/en/blog/total-protein-high-or-low\">high or low total protein</a> and <a href=\"/en/blog/globulin-high-or-low\">globulin results</a>. For diagnosis and treatment, always speak with your doctor.</p>"),
                Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Not a substitute for diagnosis or treatment. Discuss your results with a doctor.</p>"),
            ],
            "es": [
                Section(id="que-es", level=2, heading="¿Qué es la albúmina?", body_html="<p>La <strong>albúmina</strong> es una de las principales proteínas de la sangre; se produce en el hígado. Ayuda a mantener el líquido dentro de los vasos y participa en el transporte de hormonas y de algunos medicamentos. Se suele medir en la bioquímica rutinaria; un solo valor no da el diagnóstico.</p>"),
                Section(id="por-que-baja", level=2, heading="¿Por qué puede estar la albúmina baja?", body_html="<p>Un valor bajo puede relacionarse con enfermedad hepática o renal, mala nutrición o déficit de proteínas, infección o inflamación importante, o pérdida de proteínas por el intestino. El médico valorará tu historia, exploración y otras pruebas (proteínas totales, función hepática y renal) en conjunto.</p>"),
                Section(id="como-interpretar", level=2, heading="¿Cómo se interpreta el resultado?", body_html="<p>Los rangos de referencia varían según el laboratorio. Un valor bajo aislado no siempre indica enfermedad grave; una ligera bajada a veces puede ser transitoria o nutricional. La interpretación y las pruebas adicionales deben hacerlas tu médico.</p>"),
                Section(id="cta", level=2, heading="Aclara tus resultados", body_html="<p>Si quieres ver tus análisis en un resumen claro y ordenado, puedes <a href=\"/analyze\">realizar un análisis</a>. Para el diagnóstico y el tratamiento, consulta siempre con tu médico.</p>"),
                Section(id="aviso", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> No sustituye el diagnóstico ni el tratamiento. Comenta tus resultados con un médico.</p>"),
            ],
            "de": [
                Section(id="was-ist", level=2, heading="Was ist Albumin?", body_html="<p><strong>Albumin</strong> ist eines der Haupteiweiße im Blut; es wird in der Leber gebildet. Es hält Flüssigkeit in den Gefäßen und ist am Transport von Hormonen und manchen Medikamenten beteiligt. Es wird oft in der Routine-Blutchemie gemessen; ein einzelner Wert ergibt keine Diagnose.</p>"),
                Section(id="warum-niedrig", level=2, heading="Warum kann Albumin niedrig sein?", body_html="<p>Niedrige Werte können bei Leber- oder Nierenerkrankung, Mangelernährung, schwerer Infektion oder Entzündung oder Eiweißverlust über den Darm vorkommen. Ihr Arzt beurteilt Anamnese, Untersuchung und weitere Werte (Gesamteiweiß, Leber, Niere) gemeinsam.</p>"),
                Section(id="einordnung", level=2, heading="Wie wird der Befund eingeordnet?", body_html="<p>Referenzbereiche sind laborabhängig. Ein einzelner niedriger Wert bedeutet nicht zwangsläufig eine ernste Erkrankung; eine leichte Erniedrigung kann vorübergehend oder ernährungsbedingt sein. Einordnung und weitere Abklärung obliegen dem Arzt.</p>"),
                Section(id="cta", level=2, heading="Befund verständlich machen", body_html="<p>Wenn Sie Ihre Blutwerte als klare, strukturierte Zusammenfassung sehen möchten, können Sie <a href=\"/analyze\">eine Analyse starten</a>. Für Diagnose und Therapie sprechen Sie bitte mit Ihrem Arzt.</p>"),
                Section(id="hinweis", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> Ersetzt keine Diagnose oder Behandlung. Besprechen Sie Ihren Befund mit dem Arzt.</p>"),
            ],
            "fr": [
                Section(id="quest-ce-que", level=2, heading="Qu'est-ce que l'albumine ?", body_html="<p>L'<strong>albumine</strong> est l'une des principales protéines du sang ; elle est produite par le foie. Elle contribue à maintenir le liquide dans les vaisseaux et au transport d'hormones et de certains médicaments. Elle est souvent dosée en biochimie courante ; un seul chiffre ne fait pas un diagnostic.</p>"),
                Section(id="pourquoi-bas", level=2, heading="Pourquoi l'albumine peut-elle être basse ?", body_html="<p>Un taux bas peut être lié à une maladie du foie ou du rein, une malnutrition ou un déficit en protéines, une infection ou une inflammation importante, ou une perte de protéines par le tube digestif. Le médecin évalue l'histoire, l'examen et les autres examens (protéines totales, foie, rein) ensemble.</p>"),
                Section(id="comment-lire", level=2, heading="Comment interpréter le résultat ?", body_html="<p>Les fourchettes de référence varient selon le laboratoire. Un chiffre bas isolé ne signifie pas toujours une maladie grave ; une légère baisse peut être transitoire ou nutritionnelle. L'interprétation et d'éventuels examens complémentaires relèvent du médecin.</p>"),
                Section(id="cta", level=2, heading="Clarifiez vos résultats", body_html="<p>Pour voir vos résultats sous forme de résumé clair et structuré, vous pouvez <a href=\"/analyze\">lancer une analyse</a>. Pour le diagnostic et le traitement, consultez toujours un médecin.</p>"),
                Section(id="avertissement", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> Ne remplace pas le diagnostic ni le traitement. Discutez de vos résultats avec un médecin.</p>"),
            ],
            "it": [
                Section(id="cos-e", level=2, heading="Cos'è l'albumina?", body_html="<p>L'<strong>albumina</strong> è una delle principali proteine del sangue; è prodotta dal fegato. Contribuisce a mantenere i liquidi nei vasi e al trasporto di ormoni e di alcuni farmaci. Si misura spesso nella biochimica di routine; un solo valore non fa diagnosi.</p>"),
                Section(id="perche-bassa", level=2, heading="Perché l'albumina può essere bassa?", body_html="<p>Un valore basso può dipendere da malattia epatica o renale, malnutrizione o scarso apporto proteico, infezione o infiammazione importante, o perdita di proteine dall'intestino. Il medico valuta anamnesi, visita ed altri esami (proteine totali, fegato, rene) insieme.</p>"),
                Section(id="come-interpretare", level=2, heading="Come si interpreta il risultato?", body_html="<p>Gli intervalli di riferimento variano da laboratorio. Un valore basso da solo non significa sempre una patologia grave; un lieve calo a volte può essere transitorio o nutrizionale. Interpretazione ed eventuali approfondimenti spettano al medico.</p>"),
                Section(id="cta", level=2, heading="Chiariamo i tuoi risultati", body_html="<p>Se vuoi vedere i tuoi esami in un riepilogo chiaro e strutturato, puoi <a href=\"/analyze\">avviare un'analisi</a>. Per diagnosi e terapia consulta sempre il medico.</p>"),
                Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> Non sostituisce diagnosi o terapia. Discuti i risultati con il medico.</p>"),
            ],
            "he": [
                Section(id="ma-hu", level=2, heading="מהו אלבומין?", body_html="<p><strong>אלבומין</strong> הוא אחד החלבונים העיקריים בדם; הוא נוצר בכבד. הוא עוזר לשמור על נוזלים בכלי הדם ומשתתף בהובלת הורמונים ותרופות מסוימות. נמדד לעיתים קרובות בביוכימיה שגרתית; ערך בודד לא קובע אבחנה.</p>"),
                Section(id="lama-namuch", level=2, heading="למה אלבומין יכול להיות נמוך?", body_html="<p>ערך נמוך יכול לנבוע ממחלת כבד או כליות, תת־תזונה או חוסר חלבון, זיהום או דלקת משמעותיים, או אובדן חלבון מהמעי. הרופא יבדוק את האנמנזה, הבדיקה ובדיקות נוספות (חלבון כללי, כבד, כליות) ביחד.</p>"),
                Section(id="eich-lefaresh", level=2, heading="איך מפרשים את התוצאה?", body_html="<p>טווחי הנורמה משתנים בין מעבדות. ערך נמוך בודד לא תמיד מעיד על מחלה חמורה; ירידה קלה עשויה להיות זמנית או תזונתית. הפרשנות והמשך בירור הם באחריות הרופא.</p>"),
                Section(id="cta", level=2, heading="הבהר את התוצאות שלך", body_html="<p>אם תרצה לראות את תוצאות הבדיקה בסיכום ברור ומסודר, תוכל <a href=\"/analyze\">להפעיל ניתוח</a>. לאבחון ולטיפול יש לפנות לרופא.</p>"),
                Section(id="hodaa", level=2, heading="הודעה", body_html="<p><strong>למידע בלבד.</strong> אינו תחליף לאבחון או טיפול. יש לדון בתוצאות עם רופא.</p>"),
            ],
            "hi": [
                Section(id="kya-hai", level=2, heading="ऐल्ब्यूमिन क्या है?", body_html="<p><strong>ऐल्ब्यूमिन</strong> खून में मुख्य प्रोटीन में से एक है; यह लिवर में बनता है। यह रक्त वाहिकाओं में द्रव बनाए रखने और हार्मोन व कुछ दवाओं के परिवहन में भूमिका निभाता है। अक्सर रूटीन बायोकेमिस्ट्री में मापा जाता है; एक अकेला रिज़ल्ट निदान नहीं है।</p>"),
                Section(id="kyon-kam", level=2, heading="ऐल्ब्यूमिन कम क्यों हो सकता है?", body_html="<p>कम स्तर लिवर या किडनी रोग, कुपोषण या प्रोटीन की कमी, गंभीर संक्रमण या सूजन, या आंत से प्रोटीन नुकसान से जुड़ा हो सकता है। डॉक्टर इतिहास, जांच और अन्य टेस्ट (टोटल प्रोटीन, लिवर, किडनी) एक साथ देखेंगे।</p>"),
                Section(id="kaise-samjhe", level=2, heading="रिज़ल्ट कैसे समझें?", body_html="<p>रेफरेंस रेंज लैब के हिसाब से अलग होती है। एक कम वैल्यू हमेशा गंभीर बीमारी नहीं दर्शाती; हल्की कमी कभी अस्थायी या आहार से जुड़ी हो सकती है। व्याख्या और आगे की जांच डॉक्टर करेंगे।</p>"),
                Section(id="cta", level=2, heading="अपने रिज़ल्ट साफ करें", body_html="<p>अगर आप अपने ब्लड रिज़ल्ट को स्पष्ट, संरचित सारांश में देखना चाहते हैं तो <a href=\"/analyze\">विश्लेषण शुरू कर सकते हैं</a>। निदान और इलाज के लिए हमेशा डॉक्टर से बात करें।</p>"),
                Section(id="asvikaran", level=2, heading="अस्वीकरण", body_html="<p><strong>केवल सूचनार्थ।</strong> निदान या उपचार का विकल्प नहीं। परिणाम डॉक्टर से चर्चा करें।</p>"),
            ],
            "ar": [
                Section(id="ma-huwa", level=2, heading="ما هو الألبومين؟", body_html="<p><strong>الألبومين</strong> من البروتينات الرئيسية في الدم؛ يُنتج في الكبد. يساعد في الإبقاء على السوائل داخل الأوعية ويلعب دوراً في نقل الهرمونات وبعض الأدوية. يُقاس غالباً في كيمياء الدم الروتينية؛ رقم واحد لا يشخّص.</p>"),
                Section(id="limadha-low", level=2, heading="لماذا قد يكون الألبومين منخفضاً؟", body_html="<p>الانخفاض قد يكون بسبب مرض كبد أو كلية، سوء تغذية أو نقص بروتين، عدوى أو التهاب شديد، أو فقدان بروتين من الأمعاء. الطبيب يقيّم القصة والفحص والتحاليل الأخرى (البروتين الكلي، الكبد، الكلى) معاً.</p>"),
                Section(id="kayf-nufassir", level=2, heading="كيف نُفسّر النتيجة؟", body_html="<p>نطاقات المرجع تختلف حسب المختبر. قيمة منخفضة واحدة لا تعني دائماً مرضاً خطيراً؛ الانخفاض البسيط قد يكون مؤقتاً أو غذائياً. التفسير والمتابعة من اختصاص الطبيب.</p>"),
                Section(id="cta", level=2, heading="وضوح نتائجك", body_html="<p>إذا أردت رؤية نتائج تحاليلك في ملخص واضح ومنظم يمكنك <a href=\"/analyze\">تشغيل التحليل</a>. للتشخيص والعلاج راجع الطبيب دائماً.</p>"),
                Section(id="tanbeeh", level=2, heading="إخلاء المسؤولية", body_html="<p><strong>للمعلومات فقط.</strong> لا يغني عن التشخيص أو العلاج. ناقش نتائجك مع الطبيب.</p>"),
            ],
        },
    )


def _article_total_protein_high_low() -> Article:
    """Total protein yüksek/düşük — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/total-protein-hero.png"
    slugs = {l: "total-protein-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(
        id="total-protein-high-or-low",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"},
        slugs=slugs,
        titles={"tr": "Total protein yüksek veya düşük ne anlama gelir?", "en": "High or Low Total Protein Meaning: Albumin, Globulin, and Common Causes", "es": "Proteínas totales altas o bajas: ¿qué significan?", "de": "Gesamteiweiß zu hoch oder zu niedrig—was bedeutet das?", "fr": "Protéines totales hautes ou basses : que faut-il en déduire ?", "it": "Proteine totali alte o basse: cosa significano?", "he": "מה המשמעות של חלבון כללי גבוה או נמוך?", "hi": "टोटल प्रोटीन हाई या लो का क्या मतलब?", "ar": "ماذا يعني ارتفاع أو انخفاض البروتين الكلي؟"},
        subtitles={"tr": "Total protein albümin ve globulin toplamıdır; yüksek veya düşük hekim tarafından diğer tahlillerle birlikte yorumlanır.", "en": "Total protein is albumin plus globulins. High or low total protein is usually interpreted with albumin, globulin, liver tests, kidney markers, and hydration status.", "es": "Las proteínas totales son albúmina más globulinas; altas o bajas las interpreta el médico con el resto.", "de": "Gesamteiweiß ist Albumin plus Globuline; zu hoch oder zu niedrig wertet der Arzt mit anderen Befunden.", "fr": "Les protéines totales regroupent albumine et globulines ; haut ou bas, le médecin l'interprète avec le bilan.", "it": "Le proteine totali sono albumina più globuline; alto o basso il medico lo valuta con gli altri esami.", "he": "חלבון כללי הוא אלבומין וגלובולינים; גבוה או נמוך הרופא יפרש עם שאר התוצאות.", "hi": "टोटल प्रोटीन ऐल्ब्यूमिन और ग्लोब्युलिन का योग है; हाई या लो डॉक्टर बाकी रिज़ल्ट के साथ देखेंगे।", "ar": "البروتين الكلي هو الألبومين والغلوبولينات؛ ارتفاع أو انخفاض يفسره الطبيب مع بقية النتائج."},
        excerpts={"tr": "Total protein albümin ve globulinlerin toplamıdır; yüksek veya düşük tek başına teşhis değildir, hekim diğer tahlillerle birlikte yorumlar.", "en": "Understand what high or low total protein may mean and why doctors usually compare total protein with albumin, globulin, liver function, kidney markers, and inflammation.", "es": "Las proteínas totales son albúmina más globulinas. Altas o bajas por sí solas no son un diagnóstico; el médico las interpreta con el resto.", "de": "Gesamteiweiß setzt sich aus Albumin und Globulinen zusammen. Zu hoch oder zu niedrig allein ist keine Diagnose—der Arzt wertet mit anderen Befunden.", "fr": "Les protéines totales regroupent albumine et globulines. Un taux haut ou bas seul ne fait pas un diagnostic ; le médecin l'interprète avec le bilan.", "it": "Le proteine totali sono albumina più globuline. Alte o basse da sole non sono una diagnosi; il medico le valuta con gli altri esami.", "he": "חלבון כללי הוא אלבומין ועוד גלובולינים. גבוה או נמוך לבדו אינו אבחנה—הרופא יפרש עם שאר התוצאות.", "hi": "टोटल प्रोटीन ऐल्ब्यूमिन और ग्लोब्युलिन का योग है। हाई या लो अकेले निदान नहीं—डॉक्टर बाकी रिज़ल्ट के साथ व्याख्या करेंगे।", "ar": "البروتين الكلي هو الألبومين والغلوبولينات. ارتفاع أو انخفاض وحده ليس تشخيصاً—الطبيب يفسره مع بقية النتائج."},
        seo_titles={"tr": "Total Protein Yüksek veya Düşük Ne Anlama Gelir? | Norya Blog", "en": "High or Low Total Protein Meaning: Albumin, Globulin, and Common Causes | NoryaAI", "es": "Proteínas totales altas o bajas | Norya Blog", "de": "Gesamteiweiß zu hoch oder zu niedrig | Norya Blog", "fr": "Protéines totales hautes ou basses | Norya Blog", "it": "Proteine totali alte o basse | Norya Blog", "he": "חלבון כללי גבוה או נמוך | Norya Blog", "hi": "टोटल प्रोटीन हाई या लो | Norya Blog", "ar": "البروتين الكلي مرتفع أو منخفض | Norya Blog"},
        seo_descriptions={"tr": "Total protein yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What does high or low total protein mean? Learn common causes and how doctors interpret total protein with albumin, globulin, liver tests, kidney markers, and hydration.", "es": "Proteínas totales altas o bajas: causas. Solo informativo.", "de": "Ursachen für hohes oder niedriges Gesamteiweiß. Nur zur Information.", "fr": "Protéines totales hautes ou basses : causes. À titre informatif.", "it": "Proteine totali alte o basse: cause. Solo informativo.", "he": "חלבון כללי גבוה או נמוך. למידע בלבד.", "hi": "टोटल प्रोटीन हाई या लो. केवल सूचनार्थ।", "ar": "البروتين الكلي مرتفع أو منخفض. لأغراض إعلامية فقط."},
        cover_alt={"tr": "Total protein kan tahlili — Norya", "en": "Total protein blood test — Norya", "es": "Proteínas totales análisis — Norya", "de": "Gesamteiweiß Bluttest — Norya", "fr": "Protéines totales — Norya", "it": "Proteine totali esami — Norya", "he": "חלבון כללי — Norya", "hi": "टोटल प्रोटीन — Norya", "ar": "البروتين الكلي — Norya"},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="Total protein yüksek veya düşük ne anlama gelir?", body_html="<p><strong>Total protein</strong> albümin ile globulinlerin toplamıdır; karaciğer ve bağışıklıkla ilgilidir. Yüksek veya düşük çıkması iltihap, karaciğer veya böbrek hastalığı, beslenme gibi nedenlere bağlı olabilir. Tek başına teşhis koymaz; hekiminiz albümin, karaciğer ve böbrek testleriyle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [Section(id="content", level=2, heading="What high or low total protein may mean", body_html="<p><strong>Total protein</strong> is the sum of <strong>albumin</strong> and <strong>globulins</strong>. A higher or lower total protein result can be linked to dehydration, inflammation, liver disease, kidney conditions, immune-system activity, or nutrition-related problems. It does not make a diagnosis on its own.</p><p>Doctors usually interpret total protein next to <a href=\"/en/blog/albumin-low-meaning\">albumin</a>, the <a href=\"/en/blog/globulin-high-or-low\">globulin</a> fraction, and other blood tests such as liver or kidney markers. That broader pattern helps explain whether a result fits dehydration, protein loss, inflammation, or another cause.</p><p>Discuss your result with a clinician, especially if total protein is repeatedly outside the reference range or changes together with swelling, weight loss, infections, or abnormal liver and kidney tests.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/albumin-low-meaning\">Low albumin</a> · <a href=\"/en/blog/globulin-high-or-low\">Globulin</a> · <a href=\"/analyze\">Analyze</a></p>")],
            "es": [Section(id="content", level=2, heading="Proteínas totales altas o bajas", body_html="<p>Las <strong>proteínas totales</strong> son albúmina más globulinas; se relacionan con el hígado y la inmunidad. Un valor alto o bajo puede deberse a inflamación, enfermedad hepática o renal o nutrición. No da el diagnóstico por sí solo; el médico lo interpreta con albúmina y pruebas hepáticas o renales. Comenta el resultado con un médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>")],
            "de": [Section(id="content", level=2, heading="Gesamteiweiß zu hoch oder zu niedrig", body_html="<p><strong>Gesamteiweiß</strong> ist Albumin plus Globuline; es hängt mit Leber und Immunität zusammen. Erhöhung oder Erniedrigung kann bei Entzündung, Leber- oder Nierenerkrankung oder Ernährung vorkommen. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Albumin und Leber- bzw. Nierenwerten. Befund mit dem Arzt besprechen.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Protéines totales hautes ou basses", body_html="<p>Les <strong>protéines totales</strong> regroupent albumine et globulines ; elles sont liées au foie et à l'immunité. Un taux haut ou bas peut être lié à une inflammation, une maladie du foie ou du rein ou la nutrition. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec l'albumine et le bilan hépatique ou rénal. Discutez du résultat avec un médecin.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Proteine totali alte o basse", body_html="<p>Le <strong>proteine totali</strong> sono albumina più globuline; sono legate a fegato e immunità. Un valore alto o basso può dipendere da infiammazione, malattia epatica o renale o nutrizione. Un solo valore non fa diagnosi; il medico lo interpreta con albumina ed esami epatici o renali. Discuti il risultato con il medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>")],
            "he": [Section(id="content", level=2, heading="חלבון כללי גבוה או נמוך", body_html="<p><strong>חלבון כללי</strong> הוא אלבומין וגלובולינים; קשור לכבד ולמערכת החיסון. ערך גבוה או נמוך יכול לנבוע מדלקת, מחלת כבד או כליות או תזונה. ערך בודד לא קובע אבחנה; הרופא יפרש עם אלבומין ובדיקות כבד או כליות. יש לדון בתוצאה עם רופא.</p>"), Section(id="disclaimer", level=2, heading="הודעה", body_html="<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>")],
            "hi": [Section(id="content", level=2, heading="टोटल प्रोटीन हाई या लो", body_html="<p><strong>टोटल प्रोटीन</strong> ऐल्ब्यूमिन और ग्लोब्युलिन का योग है; लिवर और इम्युनिटी से जुड़ा है। हाई या लो इन्फ्लेमेशन, लिवर/किडनी रोग या पोषण से हो सकता है। अकेले निदान नहीं; डॉक्टर ऐल्ब्यूमिन और लिवर/किडनी टेस्ट के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>"), Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html="<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>")],
            "ar": [Section(id="content", level=2, heading="البروتين الكلي مرتفع أو منخفض", body_html="<p><strong>البروتين الكلي</strong> هو الألبومين والغلوبولينات؛ مرتبط بالكبد والمناعة. ارتفاع أو انخفاض قد يكون بسبب التهاب أو مرض كبد أو كلية أو التغذية. الرقم وحده لا يشخّص؛ الطبيب يفسره مع الألبومين وفحوص الكبد أو الكلى. ناقش نتيجتك مع الطبيب.</p>"), Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html="<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>")],
        },
        icon="/static/images/blog/icons/icon-total-protein.png",
    )


def _article_alp_high() -> Article:
    """ALP (alkalen fosfataz) yüksekliği — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/alp-high-hero.png"
    slugs = {l: "alp-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    faq_qa = {
        "en": [
            {"question": "Can pregnancy or growth raise ALP?", "answer": "Yes. ALP can rise normally in pregnancy and during growth because bone and placental sources can contribute. Your doctor will interpret the result in context."},
            {"question": "How do doctors tell whether ALP is from liver or bone?", "answer": "They often compare ALP with GGT, ALT, AST, bilirubin, and sometimes bone-related tests or calcium-related markers. The wider pattern helps suggest the likely source."},
            {"question": "Is a mildly high ALP always serious?", "answer": "Not necessarily. A mild isolated rise can be temporary or related to growth, pregnancy, healing bone, or other non-urgent causes. Persistent or clearly abnormal results still deserve medical follow-up."},
        ]
    }
    return Article(
        id="alp-high-meaning",
        published_at=published,
        read_minutes=4,
        cover_image=cover,
        icon="/static/images/blog/icons/alp-high-meaning.svg",
        faq_schema_qa=faq_qa,
        category={"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"},
        slugs=slugs,
        titles={"tr": "ALP (alkalen fosfataz) yüksek ne demek?", "en": "High ALP Meaning: Alkaline Phosphatase, Liver or Bone Causes", "es": "Fosfatasa alcalina alta: ¿qué significa?", "de": "Alkalische Phosphatase erhöht: Was bedeutet der Wert?", "fr": "Phosphatase alcaline élevée : que faut-il en penser ?", "it": "Fosfatasi alcaline alte: cosa significano?", "he": "מה המשמעות של ALP גבוה?", "hi": "ALP हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الفوسفاتاز القلوية؟"},
        subtitles={"tr": "ALP karaciğer, kemik ve safra yollarında bulunur; yüksekliği hekim tarafından kaynağa göre değerlendirilir.", "en": "Understand what high ALP may mean, whether the pattern looks more liver- or bone-related, and which follow-up tests are commonly used.", "es": "La ALP está en hígado, hueso y vías biliares; un valor alto el médico lo valora según el origen.", "de": "ALP kommt in Leber, Knochen und Gallenwegen vor; Erhöhung beurteilt der Arzt nach Herkunft.", "fr": "La phosphatase alcaline est dans le foie, l'os et les voies biliaires ; un taux élevé, le médecin l'évalue selon l'origine.", "it": "La ALP si trova in fegato, ossa e vie biliari; un valore alto il medico lo valuta in base all'origine.", "he": "ALP נמצא בכבד, בעצמות ובדרכי המרה; ערך גבוה הרופא יבדוק לפי המקור.", "hi": "ALP लिवर, हड्डी और पित्त नली में होता है; हाई लेवल डॉक्टर स्रोत के हिसाब से आंकलन करेंगे।", "ar": "الفوسفاتاز القلوية في الكبد والعظام والقنوات الصفراوية؛ ارتفاعها يقيّمها الطبيب حسب المصدر."},
        excerpts={"tr": "ALP karaciğer, kemik ve safra yollarında bulunur; yüksekliği tek başına teşhis değildir—hekim hangi kaynaktan geldiğini değerlendirir.", "en": "Understand high ALP meaning, common alkaline phosphatase causes, and why doctors compare it with ALT, AST, GGT, or bone-related tests.", "es": "La ALP está en hígado, hueso y vías biliares. Un valor alto por sí solo no es un diagnóstico; el médico valorará el origen.", "de": "ALP kommt in Leber, Knochen und Gallenwegen vor. Erhöhung allein ist keine Diagnose—der Arzt klärt die Herkunft.", "fr": "La phosphatase alcaline est présente dans le foie, l'os et les voies biliaires. Un taux élevé seul ne fait pas un diagnostic ; le médecin en cherche l'origine.", "it": "La ALP si trova in fegato, ossa e vie biliari. Un valore alto da solo non è una diagnosi; il medico ne valuta l'origine.", "he": "ALP נמצא בכבד, בעצמות ובדרכי המרה. ערך גבוה לבדו אינו אבחנה—הרופא יבדוק את המקור.", "hi": "ALP लिवर, हड्डी और पित्त नली में होता है। हाई लेवल अकेले निदान नहीं—डॉक्टर स्रोत पता करेंगे।", "ar": "الفوسفاتاز القلوية في الكبد والعظام والقنوات الصفراوية. ارتفاعها وحده ليس تشخيصاً—الطبيب يحدد المصدر."},
        seo_titles={"tr": "ALP Yüksekliği Ne Anlama Gelir? | Norya Blog", "en": "High ALP Meaning: Alkaline Phosphatase, Liver or Bone Causes | Norya Blog", "es": "Fosfatasa alcalina alta | Norya Blog", "de": "Alkalische Phosphatase erhöht | Norya Blog", "fr": "Phosphatase alcaline élevée | Norya Blog", "it": "Fosfatasi alcaline alte | Norya Blog", "he": "ALP גבוה | Norya Blog", "hi": "ALP हाई | Norya Blog", "ar": "ارتفاع الفوسفاتاز القلوية | Norya Blog"},
        seo_descriptions={"tr": "ALP (alkalen fosfataz) yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Understand high ALP meaning, common alkaline phosphatase causes, and how doctors interpret ALP with liver enzymes, GGT, and bone-related tests.", "es": "Fosfatasa alcalina alta: causas. Solo informativo.", "de": "Ursachen für erhöhte ALP. Nur zur Information.", "fr": "Phosphatase alcaline élevée : causes. À titre informatif.", "it": "Fosfatasi alcaline alte: cause. Solo informativo.", "he": "סיבות ל-ALP גבוה. למידע בלבד.", "hi": "ALP हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع الفوسفاتاز القلوية. لأغراض إعلامية فقط."},
        cover_alt={"tr": "ALP kan tahlili — Norya", "en": "ALP blood test — Norya", "es": "Fosfatasa alcalina — Norya", "de": "ALP Bluttest — Norya", "fr": "Phosphatase alcaline — Norya", "it": "Fosfatasi alcaline — Norya", "he": "ALP — Norya", "hi": "ALP ब्लड टेस्ट — Norya", "ar": "الفوسفاتاز القلوية — Norya"},
        sections_by_lang={
            "tr": [Section(id="content", level=2, heading="ALP yüksekliği ne anlama gelir?", body_html="<p><strong>ALP</strong> (alkalen fosfataz) karaciğer, kemik ve safra yollarında bulunan bir enzimdir. Yüksek çıkması bu dokulardan birinden kaynaklanabilir; bazen büyüme çağında veya gebelikte de fizyolojik olarak yükselir. Tek başına teşhis koymaz; hekiminiz GGT, ALT/AST veya kemik testleriyle kaynağı değerlendirir. Sonucunuzu hekimle görüşün.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html="<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>")],
            "en": [
                Section(id="content", level=2, heading="What does a high ALP level mean?", body_html="<p><strong>ALP</strong> (alkaline phosphatase) is an enzyme found in liver, bone, and bile ducts. A high level may come from any of these; it can also rise normally in growth or pregnancy. It does not make a diagnosis alone; your doctor will use GGT, <a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">ALT/AST</a>, or bone tests to work out the source. Discuss your result with a doctor.</p>"),
                Section(id="quick-answer", level=2, heading="Quick answer", body_html="<div class=\"blog-definition\"><strong>Short answer:</strong> a high ALP result usually tells doctors to ask where the enzyme is coming from first. The most common broad categories are liver or bile-duct sources, bone-related sources, and some normal physiologic states such as growth or pregnancy.</div>"),
                Section(id="pattern-guide", level=2, heading="In-range vs high: quick pattern guide", body_html="<div class=\"blog-example\"><strong>In range:</strong> usually means ALP is within the lab reference range for your age and situation.<br /><strong>Mildly high:</strong> can be seen with temporary or non-urgent causes, including growth, pregnancy, healing bone, or mild liver-related changes.<br /><strong>High with ALT/AST, GGT, or bilirubin:</strong> may look more liver- or bile-related.<br /><strong>High with calcium or bone-related issues:</strong> bone turnover may be considered more strongly.</div>"),
                Section(id="compare-pattern", level=2, heading="How doctors compare high ALP", body_html="<p>If ALP rises together with <a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">ALT/AST</a>, GGT, or bilirubin, the pattern may look more liver- or bile-related. If calcium, vitamin D, or bone-related tests are more relevant, bone turnover may be considered more strongly. This comparison helps guide follow-up rather than confirm a diagnosis.</p>"),
                Section(id="faq", level=2, heading="Frequently asked questions", body_html="<p><strong>Can pregnancy or growth raise ALP?</strong><br />Yes. ALP can rise normally in pregnancy and during growth because bone and placental sources can contribute. Your doctor will interpret the result in context.</p><p><strong>How do doctors tell whether ALP is from liver or bone?</strong><br />They often compare ALP with GGT, ALT, AST, bilirubin, and sometimes bone-related tests or calcium-related markers. The wider pattern helps suggest the likely source.</p><p><strong>Is a mildly high ALP always serious?</strong><br />Not necessarily. A mild isolated rise can be temporary or related to growth, pregnancy, healing bone, or other non-urgent causes. Persistent or clearly abnormal results still deserve medical follow-up.</p>"),
                Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">high ALT and AST</a> · <a href=\"/en/blog/calcium-high-meaning\">high calcium</a>. If you are checking your own report, go to <a href=\"/en/blood-test-results-explained\">blood test results explained</a>, <a href=\"/en/upload-blood-test-results\">upload blood test results</a>, or the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a>. <a href=\"/analyze\">Analyze</a></p>"),
            ],
            "es": [Section(id="content", level=2, heading="Fosfatasa alcalina alta", body_html="<p>La <strong>ALP</strong> (fosfatasa alcalina) es una enzima del hígado, hueso y vías biliares. Un valor alto puede proceder de cualquiera de ellos; también puede subir de forma fisiológica en crecimiento o embarazo. No da el diagnóstico por sí solo; el médico valorará el origen con GGT, ALT/AST o pruebas óseas. Comenta el resultado con un médico.</p>"), Section(id="disclaimer", level=2, heading="Aviso", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>")],
            "de": [Section(id="content", level=2, heading="ALP erhöht: Was bedeutet der Wert?", body_html="<p><strong>ALP</strong> (alkalische Phosphatase) ist ein Enzym in Leber, Knochen und Gallenwegen. Erhöhung kann von einem dieser Bereiche stammen; sie kann auch im Wachstum oder in der Schwangerschaft physiologisch ansteigen. Ein Wert allein ergibt keine Diagnose; der Arzt klärt die Herkunft mit GGT, ALT/AST oder Knochenwerten. Befund mit dem Arzt besprechen.</p>"), Section(id="disclaimer", level=2, heading="Hinweis", body_html="<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>")],
            "fr": [Section(id="content", level=2, heading="Phosphatase alcaline élevée", body_html="<p>La <strong>phosphatase alcaline</strong> est une enzyme du foie, de l'os et des voies biliaires. Un taux élevé peut venir de l'un de ces organes ; il peut aussi augmenter normalement en croissance ou grossesse. Un chiffre seul ne fait pas un diagnostic ; le médecin en cherche l'origine avec GGT, ALT/AST ou bilan osseux. Discutez du résultat avec un médecin.</p>"), Section(id="disclaimer", level=2, heading="Avertissement", body_html="<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>")],
            "it": [Section(id="content", level=2, heading="Fosfatasi alcaline alte", body_html="<p>Le <strong>fosfatasi alcaline</strong> (ALP) sono enzimi di fegato, ossa e vie biliari. Un valore alto può provenire da uno di questi; può anche aumentare fisiologicamente in crescita o gravidanza. Un solo valore non fa diagnosi; il medico ne valuta l'origine con GGT, ALT/AST o esami ossei. Discuti il risultato con il medico.</p>"), Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>")],
            "he": [Section(id="content", level=2, heading="מה המשמעות של ALP גבוה?", body_html="<p><strong>ALP</strong> (פוספטזה אלקלית) הוא אנזים בכבד, בעצמות ובדרכי המרה. ערך גבוה יכול לנבוע מאחד מהם; יכול גם לעלות פיזיולוגית בצמיחה או בהריון. ערך בודד לא קובע אבחנה; הרופא יבדוק את המקור עם GGT, ALT/AST או בדיקות עצם. יש לדון בתוצאה עם רופא.</p>"), Section(id="disclaimer", level=2, heading="הודעה", body_html="<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>")],
            "hi": [Section(id="content", level=2, heading="ALP हाई का क्या मतलब है?", body_html="<p><strong>ALP</strong> (ऐल्कलाइन फॉस्फेटेज़) लिवर, हड्डी और पित्त नली में मौजूद एंजाइम है। हाई लेवल इनमें से किसी से आ सकता है; बढ़ती उम्र या प्रेगनेंसी में सामान्य रूप से भी बढ़ सकता है। अकेले निदान नहीं; डॉक्टर GGT, ALT/AST या बोन टेस्ट से स्रोत पता करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>"), Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html="<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>")],
            "ar": [Section(id="content", level=2, heading="ماذا يعني ارتفاع الفوسفاتاز القلوية؟", body_html="<p><strong>الفوسفاتاز القلوية</strong> إنزيم في الكبد والعظام والقنوات الصفراوية. ارتفاعها قد يأتي من أي منها؛ وقد يرتفع أيضاً بشكل طبيعي في النمو أو الحمل. الرقم وحده لا يشخّص؛ الطبيب يحدد المصدر بـ GGT أو ALT/AST أو فحوص العظام. ناقش نتيجتك مع الطبيب.</p>"), Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html="<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>")],
        },
    )


_ARTICLE_ALBUMIN_LOW = _article_albumin_low()
_ARTICLE_TOTAL_PROTEIN = _article_total_protein_high_low()
_ARTICLE_ALP_HIGH = _article_alp_high()


def _article_sodium_low() -> Article:
    """Sodyum düşüklüğü / Low sodium — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/sodium-low-hero.png"
    slugs = {l: "sodium-low-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    faq_qa = {
        "en": [
            {"question": "Does low sodium always mean I need more salt?", "answer": "No. Low sodium often reflects a water-balance issue rather than simply too little salt. Doctors usually look at medications, fluid intake, kidney function, heart conditions, and hormone-related causes before recommending changes."},
            {"question": "Can drinking too much water lower sodium?", "answer": "Yes. Excess fluid intake can dilute blood sodium in some situations, especially if the body cannot balance water normally. Your clinician will interpret this in context."},
            {"question": "When is low sodium more urgent?", "answer": "Very low sodium or symptoms such as confusion, severe weakness, vomiting, seizures, or reduced consciousness need urgent medical attention. Your doctor will decide how quickly the result needs to be rechecked or treated."},
        ]
    }
    titles = {"tr": "Sodyum düşük çıkarsa ne olur?", "en": "Low Sodium Meaning: Hyponatremia, Common Causes, and Symptoms", "es": "Sodio bajo: ¿qué implica?", "de": "Natrium zu niedrig: Was bedeutet das?", "fr": "Sodium bas : qu'est-ce que ça signifie ?", "it": "Sodio basso: cosa significa?", "he": "מה אומר ערך נתרן נמוך?", "hi": "सोडियम लो का क्या मतलब है?", "ar": "ماذا يعني انخفاض الصوديوم؟"}
    excerpts = {"tr": "Sodyum kandaki başlıca elektrolitlerden biridir; düşüklüğü tek başına teşhis değildir, sıvı dengesi ve ilaçlar hekimle birlikte değerlendirilir.", "en": "Understand low sodium meaning, hyponatremia causes, symptoms, and why doctors compare sodium with fluid balance, potassium, and kidney markers.", "es": "El sodio es uno de los principales electrolitos en sangre. Un valor bajo por sí solo no es un diagnóstico; el médico valora equilibrio de líquidos y medicación.", "de": "Natrium ist einer der wichtigsten Blutelektrolyte. Ein niedriger Wert allein ist keine Diagnose—Flüssigkeitshaushalt und Medikamente beurteilt der Arzt.", "fr": "Le sodium est un des principaux électrolytes du sang. Un taux bas seul ne fait pas un diagnostic ; le médecin évalue l'équilibre hydrique et les médicaments.", "it": "Il sodio è uno dei principali elettroliti nel sangue. Un valore basso da solo non è una diagnosi; il medico valuta bilancio idrico e farmaci.", "he": "נתרן הוא אחד האלקטרוליטים העיקריים בדם. ערך נמוך לבדו אינו אבחנה—הרופא יבדוק איזון נוזלים ותרופות.", "hi": "सोडियम खून का एक मुख्य इलेक्ट्रोलाइट है। लो लेवल अकेले निदान नहीं—डॉक्टर फ्लूइड बैलेंस और दवाएं देखेंगे।", "ar": "الصوديوم أحد أهم كهارل الدم. انخفاضه وحده ليس تشخيصاً—الطبيب يقيّم توازن السوائل والأدوية."}
    disclaimer_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> Sonuçlarınızı hekimle görüşün. <a href=\"/analyze\">Analiz</a></p>"
    disclaimer_en = "<p><strong>For information only.</strong> Discuss your results with a doctor. Related guides: <a href=\"/en/blog/potassium-high-meaning\">high potassium</a> · <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> · <a href=\"/analyze\">Analyze</a></p>"
    content_tr = "<p><strong>Sodyum</strong> kandaki başlıca elektrolitlerden biridir; su dengesi ve sinir-kas iletimi için gereklidir. Düşük sodyum tek başına teşhis değildir; aşırı sıvı alımı, idrar söktürücüler, kalp veya böbrek durumları veya hormon dengesizlikleri hekim tarafından değerlendirilir. Belirgin düşüklük veya belirti varsa mutlaka hekime danışın.</p>"
    content_en = "<p><strong>Sodium</strong> is one of the main electrolytes in blood; it is needed for fluid balance and nerve and muscle function. Low sodium alone is not a diagnosis; excess fluid intake, diuretics, heart or kidney conditions, or hormone imbalances are assessed by your doctor. Doctors often compare sodium with <a href=\"/en/blog/potassium-high-meaning\">potassium</a> and <a href=\"/en/blog/creatinine-egfr-what-it-means\">kidney markers</a> to understand whether the result fits fluid imbalance, medication effect, or another cause. If you have a very low result or symptoms, see a doctor.</p>"
    subtitles = {"tr": "Sodyum kandaki başlıca elektrolittir; düşüklüğü sıvı dengesi, ilaç ve böbrek hekimle birlikte değerlendirilir.", "en": "Understand what low sodium may mean, common hyponatremia causes, symptoms, and how sodium is interpreted with fluid balance and kidney markers.", "es": "El sodio es un electrolito clave; un valor bajo se valora con el médico (líquidos, medicación, riñón).", "de": "Natrium ist ein zentraler Blutelektrolyt; zu niedrig beurteilt der Arzt (Flüssigkeit, Medikamente, Niere).", "fr": "Le sodium est un électrolyte clé ; un taux bas est évalué avec le médecin (équilibre hydrique, médicaments, rein).", "it": "Il sodio è un elettrolita chiave; un valore basso si valuta con il medico (liquidi, farmaci, rene).", "he": "נתרן הוא אלקטרוליט מרכזי; ערך נמוך יבדוק הרופא (נוזלים, תרופות, כליות).", "hi": "सोडियम खून में अहम इलेक्ट्रोलाइट है; लो सोडियम डॉक्टर फ्लूड, दवा, किडनी के साथ आंकलन करेंगे।", "ar": "الصوديوم إلكتروليت أساسي؛ انخفاضه يقيّمه الطبيب (التوازن المائي، الأدوية، الكلية)."}
    d_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>"
    d_en = "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>"
    d_es = "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>"
    d_de = "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>"
    d_fr = "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>"
    d_it = "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>"
    d_he = "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>"
    d_hi = "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>"
    d_ar = "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"
    c_es = "<p>El <strong>sodio</strong> es un electrolito clave en sangre; es necesario para el equilibrio de líquidos y la función nervio-músculo. Un valor bajo puede deberse a exceso de líquidos, enfermedad renal, ciertos medicamentos o causas hormonales. No da el diagnóstico por sí solo; el médico lo interpreta con potasio, creatinina e ingesta de líquidos. Comenta el resultado con un médico.</p>"
    c_de = "<p><strong>Natrium</strong> ist ein zentraler Blutelektrolyt; es wird für Flüssigkeitshaushalt und Nerv-Muskel-Funktion benötigt. Ein niedriger Wert kann bei Flüssigkeitsüberschuss, Nierenerkrankung, bestimmten Medikamenten oder hormonellen Ursachen vorkommen. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Kalium, Kreatinin und Flüssigkeitszufuhr. Befund mit dem Arzt besprechen.</p>"
    c_fr = "<p>Le <strong>sodium</strong> est un électrolyte clé du sang ; il est nécessaire à l'équilibre hydrique et à la fonction nerf-muscle. Un taux bas peut être lié à un excès de liquides, une maladie rénale, certains médicaments ou des causes hormonales. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec le potassium, la créatinine et les apports hydriques. Discutez du résultat avec un médecin.</p>"
    c_it = "<p>Il <strong>sodio</strong> è un elettrolita chiave nel sangue; serve per l'equilibrio idrico e la funzione nervo-muscolo. Un valore basso può dipendere da eccesso di liquidi, malattia renale, alcuni farmaci o cause ormonali. Un solo valore non fa diagnosi; il medico lo interpreta con potassio, creatinina e apporto di liquidi. Discuti il risultato con il medico.</p>"
    c_he = "<p><strong>נתרן</strong> הוא אלקטרוליט מרכזי בדם; נחוץ לאיזון נוזלים ולתפקוד עצב-שריר. ערך נמוך יכול לנבוע מעודף נוזלים, מחלת כליות, תרופות מסוימות או סיבות הורמונליות. ערך בודד לא קובע אבחנה; הרופא יפרש עם אשלגן, קראטינין וצריכת נוזלים. יש לדון בתוצאה עם רופא.</p>"
    c_hi = "<p><strong>सोडियम</strong> खून में एक अहम इलेक्ट्रोलाइट है; फ्लूड बैलेंस और नर्व-मसल फंक्शन के लिए जरूरी है। लो लेवल ज़्यादा फ्लूड, किडनी रोग, कुछ दवाएं या हार्मोनल कारणों से हो सकता है। अकेले निदान नहीं; डॉक्टर पोटैशियम, क्रिएटिनिन और फ्लूड इनटेक के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>"
    c_ar = "<p><strong>الصوديوم</strong> إلكتروليت أساسي في الدم؛ ضروري لتوازن السوائل ووظيفة الأعصاب والعضلات. انخفاضه قد يكون بسبب زيادة السوائل أو مرض كلية أو أدوية معينة أو أسباب هرمونية. الرقم وحده لا يشخّص؛ الطبيب يفسره مع البوتاسيوم والكرياتينين وتناول السوائل. ناقش نتيجتك مع الطبيب.</p>"
    sections_by_lang = {
        "tr": [Section(id="content", level=2, heading="Sodyum düşüklüğü ne anlama gelir?", body_html=content_tr), Section(id="disclaimer", level=2, heading="Uyarı", body_html=disclaimer_tr)],
        "en": [
            Section(id="content", level=2, heading="What does low sodium mean?", body_html=content_en),
            Section(id="quick-answer", level=2, heading="Quick answer", body_html="<div class=\"blog-definition\"><strong>Short answer:</strong> low sodium usually makes doctors think about <em>water balance</em>, medications, and the broader clinical picture before they think about low salt intake alone. The result is often interpreted with symptoms and other electrolytes rather than by itself.</div>"),
            Section(id="pattern-guide", level=2, heading="Normal vs low: quick pattern guide", body_html="<div class=\"blog-example\"><strong>In range:</strong> sodium is within your lab's reference range and fluid balance may be stable.<br /><strong>Mildly low:</strong> doctors often review fluid intake, medicines, glucose, and other electrolytes before drawing conclusions.<br /><strong>Clearly low:</strong> follow-up becomes more important, especially if symptoms or other abnormal results are present.<br /><strong>Urgent pattern:</strong> confusion, vomiting, seizures, severe weakness, or reduced consciousness need urgent medical attention.</div>"),
            Section(id="compare-pattern", level=2, heading="How doctors compare low sodium with other results", body_html="<p>Low sodium is often read together with <a href=\"/en/blog/potassium-high-meaning\">potassium</a>, glucose, and <a href=\"/en/blog/creatinine-egfr-what-it-means\">kidney markers</a>. This helps doctors decide whether the result fits fluid overload, dehydration, a medication effect, endocrine causes, or another pattern. If sodium came from a CMP or BMP, the <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel guide</a> shows how these chemistry markers are grouped together. The comparison helps narrow the next step, but it is not diagnostic by itself.</p>"),
            Section(id="faq", level=2, heading="Frequently asked questions", body_html="<p><strong>Does low sodium always mean I need more salt?</strong><br />No. Low sodium often reflects a water-balance issue rather than simply too little salt. Doctors usually look at medications, fluid intake, kidney function, heart conditions, and hormone-related causes before recommending changes.</p><p><strong>Can drinking too much water lower sodium?</strong><br />Yes. Excess fluid intake can dilute blood sodium in some situations, especially if the body cannot balance water normally. Your clinician will interpret this in context.</p><p><strong>When is low sodium more urgent?</strong><br />Very low sodium or symptoms such as confusion, severe weakness, vomiting, seizures, or reduced consciousness need urgent medical attention. Your doctor will decide how quickly the result needs to be rechecked or treated.</p>"),
            Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Discuss your results with a doctor. Related guides: <a href=\"/en/blog/potassium-high-meaning\">high potassium</a> · <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> · <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel</a>. For your own sodium result, see <a href=\"/en/blood-test-results-explained\">blood test results explained</a>, <a href=\"/en/upload-blood-test-results\">upload blood test results</a>, or the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a>. <a href=\"/analyze\">Analyze</a></p>"),
        ],
        "es": [Section(id="content", level=2, heading="Sodio bajo: ¿qué implica?", body_html=c_es), Section(id="disclaimer", level=2, heading="Aviso", body_html=d_es)],
        "de": [Section(id="content", level=2, heading="Natrium zu niedrig: Was bedeutet das?", body_html=c_de), Section(id="disclaimer", level=2, heading="Hinweis", body_html=d_de)],
        "fr": [Section(id="content", level=2, heading="Sodium bas : qu'est-ce que ça indique ?", body_html=c_fr), Section(id="disclaimer", level=2, heading="Avertissement", body_html=d_fr)],
        "it": [Section(id="content", level=2, heading="Sodio basso: cosa significa?", body_html=c_it), Section(id="disclaimer", level=2, heading="Disclaimer", body_html=d_it)],
        "he": [Section(id="content", level=2, heading="מה המשמעות של נתרן נמוך?", body_html=c_he), Section(id="disclaimer", level=2, heading="הודעה", body_html=d_he)],
        "hi": [Section(id="content", level=2, heading="सोडियम लो का क्या मतलब?", body_html=c_hi), Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html=d_hi)],
        "ar": [Section(id="content", level=2, heading="ماذا يعني انخفاض الصوديوم؟", body_html=c_ar), Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html=d_ar)],
    }
    return Article(id="sodium-low-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions={k: "Understand low sodium meaning, hyponatremia causes, symptoms, and how doctors interpret sodium with fluid balance, potassium, and kidney markers." if k == "en" else "Sodyum/elektrolit. Bilgilendirme amaçlı." if k == "tr" else "Solo informativo." for k in titles}, cover_alt={l: "Sodium / Natrium — Norya" for l in ("en", "de")} | {"tr": "Sodyum kan tahlili — Norya", "es": "Sodio análisis — Norya", "fr": "Sodium — Norya", "it": "Sodio — Norya", "he": "נתרן — Norya", "hi": "सोडियम — Norya", "ar": "الصوديوم — Norya"}, sections_by_lang=sections_by_lang, faq_schema_qa=faq_qa, icon="/static/images/blog/icons/sodium-low-meaning.svg")


def _article_potassium_high() -> Article:
    """Potasyum yüksekliği / High potassium — 9 dil."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/potassium-high-hero.png"
    slugs = {l: "potassium-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    faq_qa = {
        "en": [
            {"question": "Can high potassium be a lab error?", "answer": "Sometimes. Potassium can appear falsely high if red blood cells break during or after the blood draw. Your doctor may repeat the test if the result does not fit the clinical picture."},
            {"question": "Do blood pressure medicines affect potassium?", "answer": "Yes. Some blood pressure and kidney-related medicines can raise potassium. Your clinician will review your medication list before deciding what the result means."},
            {"question": "When is high potassium urgent?", "answer": "Markedly high potassium can be urgent because it may affect heart rhythm. Symptoms and ECG findings matter, but urgent action may be needed even without obvious symptoms depending on the level."},
        ]
    }
    titles = {"tr": "Potasyum yüksek çıkarsa ne anlama gelir?", "en": "High Potassium Meaning: Hyperkalemia Causes and What to Do", "es": "Potasio alto: ¿qué significa?", "de": "Kalium erhöht: Was bedeutet der Wert?", "fr": "Potassium élevé : que faut-il en déduire ?", "it": "Potassio alto: cosa significa?", "he": "מה המשמעות של אשלגן גבוה?", "hi": "पोटैशियम हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع البوتاسيوم؟"}
    subtitles = {"tr": "Potasyum kalp ve kas için önemli bir elektrolittir; yüksekliği böbrek ve ilaçlarla birlikte hekimce değerlendirilir.", "en": "Understand what high potassium may mean, common hyperkalemia causes, and why doctors usually review kidney function and medications first.", "es": "El potasio es importante para corazón y músculos; un valor alto lo valora el médico con función renal y medicación.", "de": "Kalium ist wichtig für Herz und Muskeln; Erhöhung beurteilt der Arzt mit Nierenfunktion und Medikamenten.", "fr": "Le potassium est important pour le cœur et les muscles ; un taux élevé est évalué par le médecin avec la fonction rénale et les médicaments.", "it": "Il potassio è importante per cuore e muscoli; un valore alto si valuta con il medico (funzione renale, farmaci).", "he": "אשלגן חשוב ללב ולשרירים; ערך גבוה יבדוק הרופא עם תפקוד כליות ותרופות.", "hi": "पोटैशियम दिल और मांसपेशियों के लिए जरूरी है; हाई लेवल डॉक्टर किडनी और दवाओं के साथ आंकलन करेंगे।", "ar": "البوتاسيوم مهم للقلب والعضلات؛ ارتفاعه يقيّمه الطبيب مع وظيفة الكلى والأدوية."}
    excerpts = {"tr": "Potasyum kalp ve kas fonksiyonu için önemli bir elektrolittir; yüksekliği tek başına teşhis değildir, böbrek ve ilaçlar hekimle birlikte yorumlanır.", "en": "Understand high potassium meaning, common hyperkalemia causes, medication and kidney-related patterns, and when urgent follow-up may be needed.", "es": "El potasio es importante para el corazón y los músculos. Un valor alto por sí solo no es un diagnóstico; el médico valora función renal y medicación.", "de": "Kalium ist wichtig für Herz und Muskeln. Ein erhöhter Wert allein ist keine Diagnose—der Arzt bezieht Nierenfunktion und Medikamente ein.", "fr": "Le potassium est important pour le cœur et les muscles. Un taux élevé seul ne fait pas un diagnostic ; le médecin tient compte de la fonction rénale et des médicaments.", "it": "Il potassio è importante per cuore e muscoli. Un valore alto da solo non è una diagnosi; il medico valuta funzione renale e farmaci.", "he": "אשלגן חשוב ללב ולשרירים. ערך גבוה לבדו אינו אבחנה—הרופא יבדוק תפקוד כליות ותרופות.", "hi": "पोटैशियम दिल और मांसपेशियों के लिए जरूरी है। हाई लेवल अकेले निदान नहीं—डॉक्टर किडनी फंक्शन और दवाएं देखेंगे।", "ar": "البوتاسيوم مهم للقلب والعضلات. ارتفاعه وحده ليس تشخيصاً—الطبيب يقيّم وظيفة الكلى والأدوية."}
    seo_descriptions = {"tr": "Potasyum yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Understand high potassium meaning, common hyperkalemia causes, kidney and medication-related patterns, and when doctors may act urgently.", "es": "Potasio alto: causas. Solo informativo.", "de": "Ursachen für erhöhtes Kalium. Nur zur Information.", "fr": "Potassium élevé : causes. À titre informatif.", "it": "Potassio alto: cause. Solo informativo.", "he": "סיבות לאשלגן גבוה. למידע בלבד.", "hi": "पोटैशियम हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع البوتاسيوم. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Potasyum kan tahlili — Norya", "en": "Potassium blood test — Norya", "de": "Kalium Bluttest — Norya", "es": "Potasio — Norya", "fr": "Potassium — Norya", "it": "Potassio — Norya", "he": "אשלגן — Norya", "hi": "पोटैशियम — Norya", "ar": "البوتاسيوم — Norya"}
    d = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    c_es = "<p>El <strong>potasio</strong> es un electrolito importante para el ritmo cardíaco y la función muscular y nerviosa. Un valor alto por sí solo no es un diagnóstico; el médico valora función renal, medicación (p. ej. algunos antihipertensivos), destrucción de glóbulos rojos o dieta. Una elevación importante puede requerir valoración urgente; comenta el resultado con un médico.</p>"
    c_de = "<p><strong>Kalium</strong> ist wichtig für Herzrhythmus und Nerv-Muskel-Funktion. Ein erhöhter Wert allein ist keine Diagnose; der Arzt bezieht Nierenfunktion, Medikamente (z. B. manche Blutdrucksenker), Hämolyse oder Ernährung ein. Starke Erhöhung kann dringend abgeklärt werden müssen; Befund mit dem Arzt besprechen.</p>"
    c_fr = "<p>Le <strong>potassium</strong> est un électrolyte important pour le rythme cardiaque et la fonction nerveuse et musculaire. Un taux élevé seul ne fait pas un diagnostic ; le médecin évalue la fonction rénale, les médicaments (ex. certains antihypertenseurs), l’hémolyse ou l’alimentation. Une élévation marquée peut nécessiter un bilan urgent ; discutez du résultat avec un médecin.</p>"
    c_it = "<p>Il <strong>potassio</strong> è un elettrolita importante per il ritmo cardiaco e la funzione nervosa e muscolare. Un valore alto da solo non è una diagnosi; il medico valuta funzione renale, farmaci (es. alcuni antipertensivi), emolisi o dieta. Un’elevazione marcata può richiedere accertamenti urgenti; discuti il risultato con il medico.</p>"
    c_he = "<p><strong>אשלגן</strong> חשוב לריתמוס הלב ולתפקוד עצב ושריר. ערך גבוה לבדו אינו אבחנה; הרופא יבדוק תפקוד כליות, תרופות (למשל חלק מנוגדי יתר לחץ דם), פירוק תאי דם אדומים או תזונה. עלייה משמעותית עשויה לדרוש בירור דחוף; יש לדון בתוצאה עם רופא.</p>"
    c_hi = "<p><strong>पोटैशियम</strong> हृदय रिद्म और मांसपेशी-नर्व फंक्शन के लिए जरूरी इलेक्ट्रोलाइट है। हाई पोटैशियम अकेले निदान नहीं; डॉक्टर किडनी फंक्शन, दवाएं (जैसे कुछ BP दवाएं), रेड सेल ब्रेकडाउन या डाइट देखेंगे। गंभीर बढ़ोतरी पर जरूरी जांच हो सकती है; परिणाम डॉक्टर से चर्चा करें।</p>"
    c_ar = "<p><strong>البوتاسيوم</strong> إلكتروليت مهم لانتظام القلب ووظيفة الأعصاب والعضلات. ارتفاعه وحده ليس تشخيصاً؛ الطبيب يقيّم وظيفة الكلى والأدوية (مثل بعض خافضات الضغط) أو انحلال الدم أو النظام الغذائي. الارتفاع الشديد قد يحتاج تقييماً عاجلاً؛ ناقش نتيجتك مع الطبيب.</p>"
    sections_by_lang = {
        "tr": [Section(id="content", level=2, heading="Potasyum yüksekliği ne anlama gelir?", body_html="<p><strong>Potasyum</strong> kalp ritmi ve kas-sinir fonksiyonu için önemli bir elektrolittir. Yüksek potasyum tek başına teşhis değildir; böbrek işlevi, ilaçlar (örn. bazı tansiyon ilaçları), kırmızı kan hücresi yıkımı veya diyet hekim tarafından göz önüne alınır. Ciddi yükseklik acil değerlendirme gerektirebilir; sonucunuzu hekimle yorumlayın.</p>"), Section(id="disclaimer", level=2, heading="Uyarı", body_html=d["tr"])],
        "en": [
            Section(id="content", level=2, heading="What does high potassium mean?", body_html="<p><strong>Potassium</strong> is an important electrolyte for heart rhythm and muscle and nerve function. High potassium alone is not a diagnosis; kidney function, medications (e.g. some blood pressure drugs), red cell breakdown, or diet are considered by your doctor. Doctors often compare potassium with <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> and may also look at sodium or acid-base markers to understand the pattern. Severe elevation may need urgent evaluation; discuss your result with a doctor.</p>"),
            Section(id="quick-answer", level=2, heading="Quick answer", body_html="<div class=\"blog-definition\"><strong>Short answer:</strong> high potassium makes doctors think first about kidney handling, medicines, and whether the blood sample itself may have affected the result. Because potassium can matter for heart rhythm, the urgency depends on both the level and the wider clinical picture.</div>"),
            Section(id="pattern-guide", level=2, heading="Normal vs high: quick pattern guide", body_html="<div class=\"blog-example\"><strong>In range:</strong> potassium is within your lab's reference range and usually does not suggest an immediate electrolyte issue by itself.<br /><strong>Mildly high:</strong> doctors may review medicines, kidney markers, and whether the sample hemolysed.<br /><strong>Clearly high:</strong> follow-up is usually faster because heart-rhythm risk becomes more relevant.<br /><strong>Urgent pattern:</strong> markedly high potassium, ECG changes, severe weakness, palpitations, or a strong kidney-related pattern may need urgent action.</div>"),
            Section(id="compare-pattern", level=2, heading="How doctors compare high potassium", body_html="<p>Doctors often compare potassium with <a href=\"/en/blog/sodium-low-meaning\">sodium</a>, bicarbonate or acid-base markers, and <a href=\"/en/blog/creatinine-egfr-what-it-means\">kidney function tests</a>. If the value came from a CMP or BMP, our <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel guide</a> shows why these markers are usually interpreted as a group. They may also ask whether the sample could have hemolysed, which can falsely increase potassium. This comparison helps decide whether the result is likely real and how urgent follow-up should be.</p>"),
            Section(id="faq", level=2, heading="Frequently asked questions", body_html="<p><strong>Can high potassium be a lab error?</strong><br />Sometimes. Potassium can appear falsely high if red blood cells break during or after the blood draw. Your doctor may repeat the test if the result does not fit the clinical picture.</p><p><strong>Do blood pressure medicines affect potassium?</strong><br />Yes. Some blood pressure and kidney-related medicines can raise potassium. Your clinician will review your medication list before deciding what the result means.</p><p><strong>When is high potassium urgent?</strong><br />Markedly high potassium can be urgent because it may affect heart rhythm. Symptoms and ECG findings matter, but urgent action may be needed even without obvious symptoms depending on the level.</p>"),
            Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/sodium-low-meaning\">low sodium</a> · <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> · <a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel</a>. If you want a clearer summary of your own report, start with <a href=\"/en/blood-test-results-explained\">blood test results explained</a>, <a href=\"/en/upload-blood-test-results\">upload blood test results</a>, or the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a>. <a href=\"/analyze\">Analyze</a></p>"),
        ],
        "es": [Section(id="content", level=2, heading="Potasio alto: ¿qué significa?", body_html=c_es), Section(id="disclaimer", level=2, heading="Aviso", body_html=d["es"])],
        "de": [Section(id="content", level=2, heading="Kalium erhöht: Was bedeutet der Wert?", body_html=c_de), Section(id="disclaimer", level=2, heading="Hinweis", body_html=d["de"])],
        "fr": [Section(id="content", level=2, heading="Potassium élevé : que faut-il en déduire ?", body_html=c_fr), Section(id="disclaimer", level=2, heading="Avertissement", body_html=d["fr"])],
        "it": [Section(id="content", level=2, heading="Potassio alto: cosa significa?", body_html=c_it), Section(id="disclaimer", level=2, heading="Disclaimer", body_html=d["it"])],
        "he": [Section(id="content", level=2, heading="מה המשמעות של אשלגן גבוה?", body_html=c_he), Section(id="disclaimer", level=2, heading="הודעה", body_html=d["he"])],
        "hi": [Section(id="content", level=2, heading="पोटैशियम हाई का क्या मतलब है?", body_html=c_hi), Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html=d["hi"])],
        "ar": [Section(id="content", level=2, heading="ماذا يعني ارتفاع البوتاسيوم؟", body_html=c_ar), Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html=d["ar"])],
    }
    return Article(id="potassium-high-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, faq_schema_qa=faq_qa, icon="/static/images/blog/icons/potassium-high-meaning.svg")


_ARTICLE_SODIUM_LOW = _article_sodium_low()
_ARTICLE_POTASSIUM_HIGH = _article_potassium_high()


def _article_calcium_high() -> Article:
    """Kalsiyum yüksekliği / High calcium — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/calcium-high-hero.png"
    slugs = {l: "calcium-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    faq_qa = {
        "en": [
            {"question": "Does high calcium always mean cancer?", "answer": "No. High calcium has many possible causes, including parathyroid-related causes, dehydration, medications, vitamin D-related factors, and others. The full context matters."},
            {"question": "Why does albumin matter when reading calcium?", "answer": "Part of blood calcium is bound to albumin. If albumin is abnormal, total calcium can look misleading, so doctors may correct it for albumin or measure ionized calcium depending on the situation."},
            {"question": "Can dehydration raise calcium?", "answer": "Yes, dehydration can sometimes make calcium appear higher. Your clinician may look at hydration status, kidney markers, albumin, and repeat testing if needed."},
        ]
    }
    titles = {"tr": "Kalsiyum yüksek ne demek?", "en": "High Calcium Meaning: Hypercalcemia Causes and What It May Suggest", "es": "Calcio alto: ¿qué implica?", "de": "Kalzium erhöht: Was bedeutet das?", "fr": "Calcium élevé : qu'est-ce que ça indique ?", "it": "Calcio alto: cosa significa?", "he": "מה אומר ערך סידן גבוה?", "hi": "कैल्शियम हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الكالسيوم؟"}
    excerpts = {"tr": "Kalsiyum kemik ve sinir-kas için önemlidir; yüksekliği tek başına teşhis değildir, paratiroid ve böbrek hekimle birlikte değerlendirilir.", "en": "Understand high calcium meaning, common hypercalcemia causes, and why doctors often compare calcium with vitamin D, kidney markers, and parathyroid-related tests.", "es": "El calcio es importante para huesos, nervios y músculos. Un valor alto por sí solo no es un diagnóstico; el médico valora paratiroides y riñón.", "de": "Kalzium ist wichtig für Knochen, Nerven und Muskeln. Erhöhung allein ist keine Diagnose—der Arzt bezieht Nebenschilddrüse und Niere ein.", "fr": "Le calcium est important pour les os, les nerfs et les muscles. Un taux élevé seul ne fait pas un diagnostic ; le médecin évalue parathyroïde et rein.", "it": "Il calcio è importante per ossa, nervi e muscoli. Un valore alto da solo non è una diagnosi; il medico valuta paratiroide e rene.", "he": "סידן חשוב לעצמות, לעצבים ולשרירים. ערך גבוה לבדו אינו אבחנה—הרופא יבדוק יותרת המגן וכליות.", "hi": "कैल्शियम हड्डियों, नसों और मांसपेशियों के लिए जरूरी है। हाई लेवल अकेले निदान नहीं—डॉक्टर पैराथायरॉइड और किडनी देखेंगे।", "ar": "الكالسيوم مهم للعظام والأعصاب والعضلات. ارتفاعه وحده ليس تشخيصاً—الطبيب يقيّم الغدة الجار درقية والكلى."}
    sub = {l: titles[l] for l in titles}
    c_tr = "<p><strong>Kalsiyum</strong> kemik, sinir ve kas fonksiyonu için gereklidir. Kanda yüksek kalsiyum tek başına teşhis değildir; paratiroid bezleri, böbrek, D vitamini veya bazı ilaçlar hekim tarafından değerlendirilir. Belirgin yükseklikte hekime danışın.</p>"
    c_en = "<p><strong>Calcium</strong> is needed for bone, nerve, and muscle function. High blood calcium alone is not a diagnosis; parathyroid glands, kidney, vitamin D, or certain medications are assessed by your doctor. Doctors often compare calcium with <a href=\"/en/blog/how-to-understand-vitamin-d-test-results\">vitamin D</a> and <a href=\"/en/blog/creatinine-egfr-what-it-means\">kidney markers</a> to understand the pattern. If your level is clearly high, see a doctor.</p>"
    d_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>"
    d_en = "<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/how-to-understand-vitamin-d-test-results\">vitamin D</a> · <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a> · <a href=\"/analyze\">Analyze</a></p>"
    sec = {
        "tr": [Section(id="content", level=2, heading="Kalsiyum yüksekliği ne anlama gelir?", body_html=c_tr), Section(id="disclaimer", level=2, heading="Uyarı", body_html=d_tr)],
        "en": [
            Section(id="content", level=2, heading="What does high calcium mean?", body_html=c_en),
            Section(id="quick-answer", level=2, heading="Quick answer", body_html="<div class=\"blog-definition\"><strong>Short answer:</strong> high calcium usually leads doctors to check whether the result is truly elevated and then compare it with albumin, parathyroid-related tests, vitamin D, and kidney markers. The number alone does not explain the cause.</div>"),
            Section(id="pattern-guide", level=2, heading="Normal vs high: quick pattern guide", body_html="<div class=\"blog-example\"><strong>In range:</strong> calcium is within the lab reference range, though albumin and symptoms can still affect interpretation.<br /><strong>Mildly high:</strong> doctors often recheck hydration, albumin, vitamin D, and medicines.<br /><strong>Repeatedly or clearly high:</strong> calcium is more often compared with parathyroid-related tests and kidney markers.<br /><strong>Urgent pattern:</strong> confusion, vomiting, dehydration, worsening weakness, or a strongly abnormal repeat result need prompt medical review.</div>"),
            Section(id="compare-pattern", level=2, heading="How doctors compare high calcium", body_html="<p>Doctors often look at calcium next to <a href=\"/en/blog/how-to-understand-vitamin-d-test-results\">vitamin D</a>, albumin, and <a href=\"/en/blog/creatinine-egfr-what-it-means\">kidney function markers</a>. They may also consider parathyroid-related tests if the pattern stays abnormal. This helps separate temporary shifts, dehydration-related changes, and other causes that need closer follow-up.</p>"),
            Section(id="faq", level=2, heading="Frequently asked questions", body_html="<p><strong>Does high calcium always mean cancer?</strong><br />No. High calcium has many possible causes, including parathyroid-related causes, dehydration, medications, vitamin D-related factors, and others. The full context matters.</p><p><strong>Why does albumin matter when reading calcium?</strong><br />Part of blood calcium is bound to albumin. If albumin is abnormal, total calcium can look misleading, so doctors may correct it for albumin or measure ionized calcium depending on the situation.</p><p><strong>Can dehydration raise calcium?</strong><br />Yes, dehydration can sometimes make calcium appear higher. Your clinician may look at hydration status, kidney markers, albumin, and repeat testing if needed.</p>"),
            Section(id="disclaimer", level=2, heading="Disclaimer", body_html="<p><strong>For information only.</strong> Related guides: <a href=\"/en/blog/how-to-understand-vitamin-d-test-results\">vitamin D</a> · <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a>. If you are trying to understand your own calcium result, see <a href=\"/en/blood-test-results-explained\">blood test results explained</a>, <a href=\"/en/upload-blood-test-results\">upload blood test results</a>, or the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a>. <a href=\"/analyze\">Analyze</a></p>"),
        ],
    }
    return Article(id="calcium-high-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=sub, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions={k: "Understand high calcium meaning, common hypercalcemia causes, and how doctors interpret calcium with vitamin D, kidney markers, and parathyroid-related tests." if k == "en" else "Kalsiyum. Bilgilendirme amaçlı." if k == "tr" else "Solo informativo." for k in titles}, cover_alt={l: "Calcium — Norya" for l in ("en", "de", "fr", "it")} | {"tr": "Kalsiyum kan tahlili — Norya", "es": "Calcio — Norya", "he": "סידן — Norya", "hi": "कैल्शियम — Norya", "ar": "الكالسيوم — Norya"}, sections_by_lang=sec, faq_schema_qa=faq_qa)


def _article_lymphocytes_high_low() -> Article:
    """Lenfosit yüksek veya düşük — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/lymphocytes-hero.png"
    slugs = {l: "lymphocytes-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "عد الدم"}
    titles = {"tr": "Lenfosit yüksek veya düşük çıkarsa ne olur?", "en": "What do high or low lymphocytes mean?", "es": "Linfocitos altos o bajos: ¿qué significan?", "de": "Lymphozyten zu hoch oder zu niedrig—was bedeutet das?", "fr": "Lymphocytes hauts ou bas : que signifient-ils ?", "it": "Linfociti alti o bassi: cosa significano?", "he": "מה המשמעות של לימפוציטים גבוהים או נמוכים?", "hi": "लिम्फोसाइट्स हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض اللمفاويات؟"}
    excerpts = {"tr": "Lenfositler bağışıklık hücrelerinin bir türüdür; yüksek veya düşük tek başına teşhis değildir, enfeksiyon ve diğer değerler hekimle birlikte yorumlanır.", "en": "Lymphocytes are a type of immune cell. High or low alone is not a diagnosis—your doctor will interpret them with infection and other blood counts.", "es": "Los linfocitos son un tipo de célula inmunitaria. Altos o bajos por sí solos no son un diagnóstico; el médico los interpreta con infección y hemograma.", "de": "Lymphozyten sind eine Art Immunzelle. Hoch oder niedrig allein ist keine Diagnose—der Arzt wertet sie mit Infektion und restlichem Blutbild aus.", "fr": "Les lymphocytes sont un type de cellule immunitaire. Hauts ou bas seuls ne font pas un diagnostic ; le médecin les interprète avec infection et NFS.", "it": "I linfociti sono un tipo di cellula immunitaria. Alti o bassi da soli non sono una diagnosi; il medico li valuta con infezione ed emocromo.", "he": "לימפוציטים הם סוג של תא חיסון. גבוה או נמוך לבדו אינו אבחנה—הרופא יפרש עם זיהום וספירת דם.", "hi": "लिम्फोसाइट्स एक तरह की इम्यून सेल हैं। हाई या लो अकेले निदान नहीं—डॉक्टर इन्फेक्शन और ब्लड काउंट के साथ व्याख्या करेंगे।", "ar": "اللمفاويات نوع من خلايا المناعة. ارتفاع أو انخفاض وحده ليس تشخيصاً—الطبيب يفسره مع العدوى وعدّ الدم."}
    sub = {l: titles[l] for l in titles}
    c_tr = "<p><strong>Lenfositler</strong> beyaz kan hücrelerinin bir türüdür; bağışıklık yanıtında rol oynar. Yüksek veya düşük sayı tek başına teşhis değildir; viral enfeksiyon, kronik iltihap, stres veya bazı ilaçlar sonucu etkileyebilir. Hemogramdaki diğer değerler ve klinik tablo hekimle birlikte yorumlanır.</p>"
    c_en = "<p><strong>Lymphocytes</strong> are a type of white blood cell involved in immune response. A high or low count alone is not a diagnosis; viral infection, chronic inflammation, stress, or certain medications can affect the result. Other blood count values and your clinical picture are interpreted together by your doctor.</p>"
    d_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>"
    d_en = "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>"
    sec = {"tr": [Section(id="content", level=2, heading="Lenfosit yüksek veya düşük ne demek?", body_html=c_tr), Section(id="disclaimer", level=2, heading="Uyarı", body_html=d_tr)], "en": [Section(id="content", level=2, heading="What do high or low lymphocytes mean?", body_html=c_en), Section(id="disclaimer", level=2, heading="Disclaimer", body_html=d_en)]}
    return Article(id="lymphocytes-high-or-low", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=sub, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions={k: "Lymphocytes/blood count. For information only." if k == "en" else "Lenfosit/hemogram. Bilgilendirme amaçlı." if k == "tr" else "Solo informativo." for k in titles}, cover_alt={"tr": "Lenfosit hemogram — Norya", "en": "Lymphocytes blood count — Norya", "es": "Linfocitos — Norya", "de": "Lymphozyten — Norya", "fr": "Lymphocytes — Norya", "it": "Linfociti — Norya", "he": "לימפוציטים — Norya", "hi": "लिम्फोसाइट्स — Norya", "ar": "اللمفاويات — Norya"}, sections_by_lang=sec)


def _article_monocytes_high() -> Article:
    """Monosit yüksekliği — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/monocytes-hero.png"
    slugs = {l: "monocytes-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "عد الدم"}
    titles = {"tr": "Monosit yüksek ne demek?", "en": "What does high monocytes mean?", "es": "Monocitos altos: ¿qué significan?", "de": "Monozyten erhöht: Was bedeutet der Wert?", "fr": "Monocytes élevés : que faut-il en conclure ?", "it": "Monociti alti: cosa significa?", "he": "מה המשמעות של מונוציטים גבוהים?", "hi": "मोनोसाइट्स हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الوحيدات؟"}
    excerpts = {"tr": "Monositler beyaz kürelerin bir türüdür; yüksekliği tek başına teşhis değildir, enfeksiyon veya iltihap durumunda hekim diğer tetkiklerle birlikte yorumlar.", "en": "Monocytes are a type of white blood cell. A high count alone is not a diagnosis—your doctor will interpret it with infection or inflammation and other tests.", "es": "Los monocitos son un tipo de glóbulos blancos. Un valor alto por sí solo no es un diagnóstico; el médico lo interpreta con infección o inflamación y otras pruebas.", "de": "Monozyten sind eine Art weißer Blutkörperchen. Erhöhung allein ist keine Diagnose—der Arzt wertet mit Infektion oder Entzündung und weiteren Befunden aus.", "fr": "Les monocytes sont un type de globules blancs. Un taux élevé seul ne fait pas un diagnostic ; le médecin l'interprète avec infection ou inflammation et autres examens.", "it": "I monociti sono un tipo di globuli bianchi. Un valore alto da solo non è una diagnosi; il medico lo valuta con infezione o infiammazione e altri esami.", "he": "מונוציטים הם סוג של תאי דם לבנים. ערך גבוה לבדו אינו אבחנה—הרופא יפרש עם זיהום או דלקת ובדיקות נוספות.", "hi": "मोनोसाइट्स एक तरह की वाइट ब्लड सेल हैं। हाई काउंट अकेले निदान नहीं—डॉक्टर इन्फेक्शन या इन्फ्लेमेशन और दूसरे टेस्ट के साथ व्याख्या करेंगे।", "ar": "الوحيدات نوع من كريات الدم البيضاء. ارتفاعها وحده ليس تشخيصاً—الطبيب يفسره مع العدوى أو الالتهاب وفحوص أخرى."}
    sub = {l: titles[l] for l in titles}
    c_tr = "<p><strong>Monositler</strong> beyaz kan hücrelerinin bir türüdür; enfeksiyon veya iltihap sonrası sayıları artabilir. Yüksek monosit tek başına teşhis değildir; hekiminiz bunu enfeksiyon, otoimmün veya diğer nedenlerle birlikte değerlendirir. Hemogram ve gerekirse ek tetkiklerle yorum yapılır.</p>"
    c_en = "<p><strong>Monocytes</strong> are a type of white blood cell; their count can rise after infection or inflammation. High monocytes alone are not a diagnosis; your doctor will consider infection, autoimmune, or other causes along with your full blood count and any further tests.</p>"
    d_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>"
    d_en = "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>"
    sec = {"tr": [Section(id="content", level=2, heading="Monosit yüksekliği ne anlama gelir?", body_html=c_tr), Section(id="disclaimer", level=2, heading="Uyarı", body_html=d_tr)], "en": [Section(id="content", level=2, heading="What does high monocytes mean?", body_html=c_en), Section(id="disclaimer", level=2, heading="Disclaimer", body_html=d_en)]}
    return Article(id="monocytes-high-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=sub, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions={k: "Monocytes/blood count. For information only." if k == "en" else "Monosit/hemogram. Bilgilendirme amaçlı." if k == "tr" else "Solo informativo." for k in titles}, cover_alt={"tr": "Monosit hemogram — Norya", "en": "Monocytes blood count — Norya", "es": "Monocitos — Norya", "de": "Monozyten — Norya", "fr": "Monocytes — Norya", "it": "Monociti — Norya", "he": "מונוציטים — Norya", "hi": "मोनोसाइट्स — Norya", "ar": "الوحيدات — Norya"}, sections_by_lang=sec)


def _article_mcv_high_low() -> Article:
    """MCV yüksek veya düşük — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/mcv-hero.png"
    slugs = {l: "mcv-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "عد الدم"}
    titles = {"tr": "MCV yüksek veya düşük ne anlama gelir?", "en": "What do high or low MCV mean?", "es": "VCM alto o bajo: ¿qué significan?", "de": "MCV zu hoch oder zu niedrig: Was bedeutet das?", "fr": "VGM haut ou bas : que signifient-ils ?", "it": "MCV alti o bassi: cosa significano?", "he": "מה המשמעות של MCV גבוה או נמוך?", "hi": "MCV हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض الحجم الكروي الوسطي؟"}
    excerpts = {"tr": "MCV kırmızı kan hücrelerinin ortalama büyüklüğünü gösterir; yüksek veya düşük tek başına teşhis değildir, B12, folat ve demir hekimle birlikte yorumlanır.", "en": "MCV shows the average size of red blood cells. High or low alone is not a diagnosis—your doctor will consider B12, folate, and iron together.", "es": "El VCM indica el tamaño medio de los glóbulos rojos. Alto o bajo por sí solo no es un diagnóstico; el médico valora B12, folato e hierro.", "de": "MCV zeigt die durchschnittliche Größe der roten Blutkörperchen. Hoch oder niedrig allein ist keine Diagnose—der Arzt bezieht B12, Folsäure und Eisen ein.", "fr": "Le VGM reflète la taille moyenne des globules rouges. Haut ou bas seul ne fait pas un diagnostic ; le médecin évalue B12, folates et fer.", "it": "L'MCV indica la dimensione media dei globuli rossi. Alto o basso da solo non è una diagnosi; il medico valuta B12, folati e ferro.", "he": "MCV מציג את גודל ממוצע של כדוריות הדם האדומות. גבוה או נמוך לבדו אינו אבחנה—הרופא יבדוק B12, חומצה פולית וברזל.", "hi": "MCV लाल रक्त कोशिकाओं का औसत आकार दिखाता है। हाई या लो अकेले निदान नहीं—डॉक्टर B12, फोलेट और आयरन एक साथ देखेंगे।", "ar": "الحجم الكروي الوسطي يعكس متوسط حجم كريات الدم الحمراء. ارتفاع أو انخفاض وحده ليس تشخيصاً—الطبيب يقيّم B12 والفولات والحديد."}
    sub = {l: titles[l] for l in titles}
    c_tr = "<p><strong>MCV</strong> (ortalama hücre hacmi) kırmızı kan hücrelerinin ortalama büyüklüğünü gösterir. Düşük MCV genellikle demir eksikliği veya kronik hastalık anemisiyle, yüksek MCV ise B12 veya folat eksikliğiyle ilişkili olabilir; tek başına teşhis değildir. Hemoglobin, ferritin, B12 ve folat hekimle birlikte yorumlanır.</p>"
    c_en = "<p><strong>MCV</strong> (mean cell volume) shows the average size of red blood cells. Low MCV often relates to iron deficiency or anaemia of chronic disease; high MCV may relate to B12 or folate deficiency—neither is a diagnosis on its own. Haemoglobin, ferritin, B12, and folate are interpreted together by your doctor.</p>"
    d_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>"
    d_en = "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>"
    sec = {"tr": [Section(id="content", level=2, heading="MCV yüksek veya düşük ne anlama gelir?", body_html=c_tr), Section(id="disclaimer", level=2, heading="Uyarı", body_html=d_tr)], "en": [Section(id="content", level=2, heading="What do high or low MCV mean?", body_html=c_en), Section(id="disclaimer", level=2, heading="Disclaimer", body_html=d_en)]}
    return Article(id="mcv-high-or-low", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=sub, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions={k: "MCV/blood count. For information only." if k == "en" else "MCV/hemogram. Bilgilendirme amaçlı." if k == "tr" else "Solo informativo." for k in titles}, cover_alt={"tr": "MCV hemogram — Norya", "en": "MCV blood count — Norya", "es": "VCM — Norya", "de": "MCV — Norya", "fr": "VGM — Norya", "it": "MCV — Norya", "he": "MCV — Norya", "hi": "MCV — Norya", "ar": "الحجم الكروي الوسطي — Norya"}, sections_by_lang=sec)


def _article_rdw_high() -> Article:
    """RDW yüksekliği — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/rdw-hero.png"
    slugs = {l: "rdw-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "عد الدم"}
    titles = {"tr": "RDW yüksek ne demek?", "en": "What does high RDW mean?", "es": "ADE alto: ¿qué significa?", "de": "RDW erhöht: Was bedeutet der Wert?", "fr": "RDW élevé : qu'est-ce que ça indique ?", "it": "RDW alto: cosa significa?", "he": "מה המשמעות של RDW גבוה?", "hi": "RDW हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع عرض توزيع كريات الدم الحمراء؟"}
    excerpts = {"tr": "RDW kırmızı kan hücrelerinin boyut dağılımını gösterir; yüksekliği tek başına teşhis değildir, MCV ve demir/B12 ile hekim yorumlar.", "en": "RDW reflects the spread of red blood cell sizes. A high value alone is not a diagnosis—your doctor will interpret it with MCV and iron or B12.", "es": "El ADE refleja la dispersión del tamaño de los glóbulos rojos. Un valor alto por sí solo no es un diagnóstico; el médico lo interpreta con VCM e hierro o B12.", "de": "RDW zeigt die Streuung der Größe der roten Blutkörperchen. Erhöhung allein ist keine Diagnose—der Arzt wertet mit MCV sowie Eisen oder B12 aus.", "fr": "Le RDW reflète la dispersion de la taille des globules rouges. Un taux élevé seul ne fait pas un diagnostic ; le médecin l'interprète avec VGM et fer ou B12.", "it": "L'RDW riflette la dispersione delle dimensioni dei globuli rossi. Un valore alto da solo non è una diagnosi; il medico lo valuta con MCV e ferro o B12.", "he": "RDW משקף את פיזור גודל כדוריות הדם האדומות. ערך גבוה לבדו אינו אבחנה—הרופא יפרש עם MCV וברזל או B12.", "hi": "RDW लाल रक्त कोशिकाओं के आकार के फैलाव को दिखाता है। हाई वैल्यू अकेले निदान नहीं—डॉक्टर MCV और आयरन या B12 के साथ व्याख्या करेंगे।", "ar": "عرض التوزيع يعكس توزّع أحجام كريات الدم الحمراء. ارتفاعه وحده ليس تشخيصاً—الطبيب يفسره مع الحجم الكروي والحديد أو B12."}
    sub = {l: titles[l] for l in titles}
    c_tr = "<p><strong>RDW</strong> (eritrosit dağılım genişliği) kırmızı kan hücrelerinin boyut dağılımını yansıtır. Yüksek RDW tek başına teşhis değildir; demir, B12 veya folat eksikliği, kronik hastalık veya kan kaybı gibi nedenler hekim tarafından MCV ve diğer değerlerle birlikte değerlendirilir. Sonucunuzu hekiminizle yorumlayın.</p>"
    c_en = "<p><strong>RDW</strong> (red cell distribution width) reflects the spread of red blood cell sizes. A high RDW alone is not a diagnosis; causes such as iron, B12, or folate deficiency, chronic disease, or blood loss are assessed by your doctor together with MCV and other values. Interpret your result with your doctor.</p>"
    d_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>"
    d_en = "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>"
    sec = {"tr": [Section(id="content", level=2, heading="RDW yüksekliği ne anlama gelir?", body_html=c_tr), Section(id="disclaimer", level=2, heading="Uyarı", body_html=d_tr)], "en": [Section(id="content", level=2, heading="What does high RDW mean?", body_html=c_en), Section(id="disclaimer", level=2, heading="Disclaimer", body_html=d_en)]}
    return Article(id="rdw-high-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=sub, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions={k: "RDW/blood count. For information only." if k == "en" else "RDW/hemogram. Bilgilendirme amaçlı." if k == "tr" else "Solo informativo." for k in titles}, cover_alt={"tr": "RDW hemogram — Norya", "en": "RDW blood count — Norya", "es": "ADE — Norya", "de": "RDW — Norya", "fr": "RDW — Norya", "it": "RDW — Norya", "he": "RDW — Norya", "hi": "RDW — Norya", "ar": "عرض التوزيع — Norya"}, sections_by_lang=sec)


def _article_ag_ratio_high_low() -> Article:
    """A/G oranı yüksek veya düşük — Plan 2."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/blog-hero.png"
    slugs = {l: "ag-ratio-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "A/G oranı yüksek veya düşük ne anlama gelir?", "en": "What do high or low A/G ratio mean?", "es": "Relación A/G alta o baja: ¿qué significan?", "de": "A/G-Quotient hoch oder niedrig: Was bedeutet das?", "fr": "Ratio A/G élevé ou bas : que signifient-ils ?", "it": "Rapporto A/G alto o basso: cosa significano?", "he": "מה המשמעות של יחס A/G גבוה או נמוך?", "hi": "A/G रेशियो हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض نسبة الألبومين إلى الغلوبيولين؟"}
    excerpts = {"tr": "A/G oranı albumin ve globulin dengesini gösterir; yüksek veya düşük tek başına teşhis değildir, karaciğer ve bağışıklık hekimle birlikte yorumlanır.", "en": "The A/G ratio reflects the balance of albumin and globulin. High or low alone is not a diagnosis—your doctor will interpret it with liver and immune context.", "es": "La relación A/G refleja el equilibrio entre albúmina y globulina. Alta o baja por sí sola no es un diagnóstico; el médico la interpreta con contexto hepático e inmunitario.", "de": "Der A/G-Quotient zeigt das Verhältnis von Albumin zu Globulin. Hoch oder niedrig allein ist keine Diagnose—der Arzt wertet mit Leber- und Immunbefunden aus.", "fr": "Le ratio A/G reflète l'équilibre albumine/globuline. Élevé ou bas seul ne fait pas un diagnostic ; le médecin l'interprète avec le contexte hépatique et immunitaire.", "it": "Il rapporto A/G riflette l'equilibrio albumina/globuline. Alto o basso da solo non è una diagnosi; il medico lo valuta con contesto epatico e immunitario.", "he": "יחס A/G משקף את האיזון בין אלבומין לגלובולין. גבוה או נמוך לבדו אינו אבחנה—הרופא יפרש עם כבד ומערכת חיסון.", "hi": "A/G रेशियो ऐल्ब्यूमिन और ग्लोब्युलिन का संतुलन दिखाता है। हाई या लो अकेले निदान नहीं—डॉक्टर लिवर और इम्यूनिटी संदर्भ में व्याख्या करेंगे।", "ar": "نسبة الألبومين إلى الغلوبيولين تعكس التوازن بينهما. ارتفاع أو انخفاض وحده ليس تشخيصاً—الطبيب يفسره في سياق الكبد والمناعة."}
    sub = {l: titles[l] for l in titles}
    c_tr = "<p><strong>A/G oranı</strong>, kandaki albumin ve globulin miktarlarının oranıdır. Düşük oran artmış globulin (örn. iltihap veya kronik hastalık) veya düşük albumin ile ilişkili olabilir; yüksek oran daha az yaygındır. Tek başına teşhis değildir; karaciğer paneli ve klinik tablo hekimle birlikte yorumlanır.</p>"
    c_en = "<p><strong>The A/G ratio</strong> is the ratio of albumin to globulin in the blood. A low ratio may be linked to increased globulin (e.g. inflammation or chronic disease) or low albumin; a high ratio is less common. It is not a diagnosis on its own; the liver panel and your clinical picture are interpreted together by your doctor.</p>"
    d_tr = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>"
    d_en = "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>"
    sec = {"tr": [Section(id="content", level=2, heading="A/G oranı yüksek veya düşük ne anlama gelir?", body_html=c_tr), Section(id="disclaimer", level=2, heading="Uyarı", body_html=d_tr)], "en": [Section(id="content", level=2, heading="What do high or low A/G ratio mean?", body_html=c_en), Section(id="disclaimer", level=2, heading="Disclaimer", body_html=d_en)]}
    return Article(id="ag-ratio-high-or-low", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=sub, excerpts=excerpts, seo_titles={k: v + " | Norya Blog" for k, v in titles.items()}, seo_descriptions={k: "A/G ratio/protein. For information only." if k == "en" else "A/G oranı/protein. Bilgilendirme amaçlı." if k == "tr" else "Solo informativo." for k in titles}, cover_alt={"tr": "A/G oranı protein — Norya", "en": "A/G ratio protein — Norya", "es": "Relación A/G — Norya", "de": "A/G-Quotient — Norya", "fr": "Ratio A/G — Norya", "it": "Rapporto A/G — Norya", "he": "יחס A/G — Norya", "hi": "A/G रेशियो — Norya", "ar": "نسبة الألبومين/الغلوبيولين — Norya"}, sections_by_lang=sec)


_ARTICLE_CALCIUM_HIGH = _article_calcium_high()
_ARTICLE_LYMPHOCYTES = _article_lymphocytes_high_low()
_ARTICLE_MONOCYTES = _article_monocytes_high()
_ARTICLE_MCV = _article_mcv_high_low()
_ARTICLE_RDW = _article_rdw_high()
_ARTICLE_AG_RATIO = _article_ag_ratio_high_low()


def _article_calcium_high() -> Article:
    """Kalsiyum yüksekliği / High calcium — 9 dil."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/calcium-high-hero.png"
    slugs = {l: "calcium-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "Kalsiyum yüksek çıkarsa ne anlama gelir?", "en": "What does high calcium mean?", "es": "Calcio alto: ¿qué significa?", "de": "Kalzium erhöht: Was bedeutet der Wert?", "fr": "Calcium élevé : qu'est-ce que ça indique ?", "it": "Calcio alto: cosa significa?", "he": "מה המשמעות של סידן גבוה?", "hi": "कैल्शियम हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الكالسيوم؟"}
    subtitles = {"tr": "Kalsiyum kemik ve sinir-kas için önemlidir; yüksekliği parathormon ve böbrek ile birlikte hekimce değerlendirilir.", "en": "Calcium is important for bones and nerve-muscle function; high levels are assessed by your doctor with PTH and kidney.", "es": "El calcio es importante para huesos y función nervio-músculo; un valor alto lo valora el médico con PTH y riñón.", "de": "Kalzium ist wichtig für Knochen und Nerv-Muskel; Erhöhung beurteilt der Arzt mit PTH und Niere.", "fr": "Le calcium est important pour les os et la fonction nerf-muscle ; un taux élevé est évalué par le médecin avec PTH et rein.", "it": "Il calcio è importante per ossa e funzione nervo-muscolo; un valore alto si valuta con il medico (PTH, rene).", "he": "סידן חשוב לעצמות ולתפקוד עצב-שריר; ערך גבוה יבדוק הרופא עם PTH וכליות.", "hi": "कैल्शियम हड्डियों और नर्व-मसल के लिए जरूरी है; हाई लेवल डॉक्टर PTH और किडनी के साथ देखेंगे।", "ar": "الكالسيوم مهم للعظام ووظيفة الأعصاب والعضلات؛ ارتفاعه يقيّمه الطبيب مع PTH والكلية."}
    excerpts = {"tr": "Kalsiyum yüksekliği tek başına teşhis değildir; parathormon, böbrek ve D vitamini hekimle birlikte yorumlanır.", "en": "High calcium alone is not a diagnosis; your doctor will consider PTH, kidney function, and vitamin D.", "es": "El calcio alto por sí solo no es un diagnóstico; el médico valora PTH, función renal y vitamina D.", "de": "Erhöhtes Kalzium allein ist keine Diagnose; der Arzt bezieht PTH, Nierenfunktion und Vitamin D ein.", "fr": "Un calcium élevé seul ne fait pas un diagnostic ; le médecin tient compte de la PTH, de la fonction rénale et de la vitamine D.", "it": "Calcio alto da solo non è una diagnosi; il medico valuta PTH, funzione renale e vitamina D.", "he": "סידן גבוה לבדו אינו אבחנה; הרופא יבדוק PTH, תפקוד כליות וויטמין D.", "hi": "कैल्शियम हाई अकेले निदान नहीं; डॉक्टर PTH, किडनी और विटामिन D देखेंगे।", "ar": "ارتفاع الكالسيوم وحده ليس تشخيصاً؛ الطبيب يقيّم PTH ووظيفة الكلى وفيتامين D."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Kalsiyum yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Causes of high calcium. For information only.", "es": "Calcio alto: causas. Solo informativo.", "de": "Ursachen für erhöhtes Kalzium. Nur zur Information.", "fr": "Calcium élevé : causes. À titre informatif.", "it": "Calcio alto: cause. Solo informativo.", "he": "סיבות לסידן גבוה. למידע בלבד.", "hi": "कैल्शियम हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع الكالسيوم. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Kalsiyum kan tahlili — Norya", "en": "Calcium blood test — Norya", "de": "Kalzium Bluttest — Norya", "es": "Calcio — Norya", "fr": "Calcium — Norya", "it": "Calcio — Norya", "he": "סידן — Norya", "hi": "कैल्शियम — Norya", "ar": "الكالسيوم — Norya"}
    content = {"tr": "<p><strong>Kalsiyum</strong> kemik sağlığı ve sinir-kas iletimi için gereklidir. Yüksek kalsiyum tek başına teşhis değildir; paratiroid hormonu (PTH), böbrek işlevi, D vitamini veya bazı ilaçlar hekim tarafından değerlendirilir. Belirgin yükseklikte mutlaka hekime danışın.</p>", "en": "<p><strong>Calcium</strong> is needed for bone health and nerve-muscle function. High calcium alone is not a diagnosis; parathyroid hormone (PTH), kidney function, vitamin D, or certain medications are considered by your doctor. Always discuss a marked elevation with a doctor.</p>", "es": "<p>El <strong>calcio</strong> es necesario para la salud ósea y la función nervio-músculo. Un valor alto por sí solo no es un diagnóstico; el médico valora hormona paratiroidea (PTH), función renal, vitamina D o ciertos medicamentos. Comenta siempre una elevación marcada con un médico.</p>", "de": "<p><strong>Kalzium</strong> wird für Knochengesundheit und Nerv-Muskel-Funktion benötigt. Erhöhung allein ist keine Diagnose; der Arzt beurteilt Parathormon (PTH), Nierenfunktion, Vitamin D oder bestimmte Medikamente. Deutliche Erhöhung mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>calcium</strong> est nécessaire à la santé osseuse et à la fonction nerf-muscle. Un taux élevé seul ne fait pas un diagnostic ; le médecin évalue la PTH, la fonction rénale, la vitamine D ou certains médicaments. Discutez toute élévation marquée avec un médecin.</p>", "it": "<p>Il <strong>calcio</strong> è necessario per la salute delle ossa e la funzione nervo-muscolo. Un valore alto da solo non è una diagnosi; il medico valuta PTH, funzione renale, vitamina D o alcuni farmaci. Discuti un'elevazione marcata con il medico.</p>", "he": "<p><strong>סידן</strong> נחוץ לבריאות העצם ולתפקוד עצב-שריר. ערך גבוה לבדו אינו אבחנה; הרופא יבדוק PTH, תפקוד כליות, ויטמין D או תרופות מסוימות. יש לדון בעלייה בולטת עם רופא.</p>", "hi": "<p><strong>कैल्शियम</strong> हड्डियों और नर्व-मसल फंक्शन के लिए जरूरी है। हाई कैल्शियम अकेले निदान नहीं; डॉक्टर PTH, किडनी, विटामिन D या कुछ दवाएं देखेंगे। ज़्यादा बढ़ोतरी डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>الكالسيوم</strong> ضروري لصحة العظام ووظيفة الأعصاب والعضلات. ارتفاعه وحده ليس تشخيصاً؛ الطبيب يقيّم PTH ووظيفة الكلى وفيتامين D أو أدوية معينة. ناقش أي ارتفاع واضح مع الطبيب.</p>"}
    body_d = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    d = {"tr": "Uyarı", "en": "Disclaimer", "es": "Aviso", "de": "Hinweis", "fr": "Avertissement", "it": "Disclaimer", "he": "הודעה", "hi": "अस्वीकरण", "ar": "إخلاء المسؤولية"}
    sections_by_lang = {lang: [Section(id="content", level=2, heading=titles[lang], body_html=content[lang]), Section(id="disclaimer", level=2, heading=d[lang], body_html=body_d[lang])] for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(id="calcium-high-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, icon="/static/images/blog/icons/calcium-high-meaning.svg")


_ARTICLE_SODIUM_LOW = _article_sodium_low()
_ARTICLE_POTASSIUM_HIGH = _article_potassium_high()
_ARTICLE_CALCIUM_HIGH = _article_calcium_high()


def _article_lymphocytes_high_low() -> Article:
    """Lenfosit yüksek veya düşük / Lymphocytes high or low — 9 dil."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/lymphocytes-high-or-low-hero.png"
    slugs = {l: "lymphocytes-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Lenfosit yüksek veya düşük ne anlama gelir?", "en": "What do high or low lymphocytes mean?", "es": "Linfocitos altos o bajos: ¿qué significan?", "de": "Lymphozyten zu hoch oder zu niedrig: Was bedeutet das?", "fr": "Lymphocytes élevés ou bas : que signifient-ils ?", "it": "Linfociti alti o bassi: cosa significano?", "he": "מה משמעות לימפוציטים גבוהים או נמוכים?", "hi": "लिम्फोसाइट्स हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض الخلايا اللمفاوية؟"}
    subtitles = {"tr": "Lenfosit beyaz kan hücresi türüdür; yüksek veya düşük çıkması enfeksiyon veya bağışıklıkla ilişkili olabilir, hekimce yorumlanır.", "en": "Lymphocytes are a type of white blood cell; high or low can be related to infection or immunity and is interpreted by your doctor.", "es": "Los linfocitos son un tipo de glóbulo blanco; altos o bajos pueden relacionarse con infección o inmunidad; el médico los interpreta.", "de": "Lymphozyten sind weiße Blutkörperchen; zu hoch oder zu niedrig kann mit Infektion oder Immunität zusammenhängen; der Arzt ordnet ein.", "fr": "Les lymphocytes sont des globules blancs ; élevés ou bas peuvent être liés à une infection ou l'immunité ; le médecin les interprète.", "it": "I linfociti sono globuli bianchi; alti o bassi possono dipendere da infezione o immunità; il medico li inquadra.", "he": "לימפוציטים הם סוג של תאי דם לבנים; גבוה או נמוך יכול להיות קשור לזיהום או חיסון; הרופא יפרש.", "hi": "लिम्फोसाइट्स एक तरह की वाइट ब्लड सेल हैं; हाई या लो इन्फेक्शन या इम्युनिटी से जुड़ा हो सकता है; डॉक्टर व्याख्या करेंगे।", "ar": "الخلايا اللمفاوية نوع من كريات الدم البيضاء؛ ارتفاع أو انخفاض قد يرتبط بالعدوى أو المناعة؛ الطبيب يفسر."}
    excerpts = {"tr": "Lenfosit yüksekliği veya düşüklüğü tek başına teşhis değildir; tam kan sayımı ve öykü hekimle birlikte değerlendirilir.", "en": "High or low lymphocytes alone are not a diagnosis; your doctor assesses them with the full blood count and your history.", "es": "Linfocitos altos o bajos por sí solos no son un diagnóstico; el médico los valora con el hemograma y tu historia.", "de": "Lymphozyten zu hoch oder zu niedrig allein sind keine Diagnose; der Arzt beurteilt mit Blutbild und Anamnese.", "fr": "Des lymphocytes élevés ou bas seuls ne font pas un diagnostic ; le médecin les évalue avec la NFS et l'histoire.", "it": "Linfociti alti o bassi da soli non sono una diagnosi; il medico li valuta con emocromo e anamnesi.", "he": "לימפוציטים גבוהים או נמוכים לבדם אינם אבחנה; הרופא יבדוק עם ספירת הדם ואנמנזה.", "hi": "लिम्फोसाइट्स हाई या लो अकेले निदान नहीं; डॉक्टर पूरे ब्लड काउंट और इतिहास के साथ आंकलन करेंगे।", "ar": "ارتفاع أو انخفاض الخلايا اللمفاوية وحده ليس تشخيصاً؛ الطبيب يقيّم مع تحليل الدم والتاريخ."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Lenfosit yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What high or low lymphocytes mean. For information only.", "es": "Linfocitos altos o bajos. Solo informativo.", "de": "Lymphozyten zu hoch oder zu niedrig. Nur zur Information.", "fr": "Lymphocytes élevés ou bas. À titre informatif.", "it": "Linfociti alti o bassi. Solo informativo.", "he": "לימפוציטים גבוהים או נמוכים. למידע בלבד.", "hi": "लिम्फोसाइट्स हाई या लो. केवल सूचनार्थ।", "ar": "الخلايا اللمفاوية مرتفعة أو منخفضة. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Lenfosit kan tahlili — Norya", "en": "Lymphocytes blood test — Norya", "de": "Lymphozyten Bluttest — Norya", "es": "Linfocitos — Norya", "fr": "Lymphocytes — Norya", "it": "Linfociti — Norya", "he": "לימפוציטים — Norya", "hi": "लिम्फोसाइट्स — Norya", "ar": "الخلايا اللمفاوية — Norya"}
    content = {"tr": "<p><strong>Lenfosit</strong> beyaz kan hücrelerinin bir türüdür; bağışıklık yanıtında rol oynar. Yüksek veya düşük çıkması enfeksiyon, viral hastalıklar veya bazı ilaçlarla ilişkili olabilir. Tek başına teşhis koymaz; hekiminiz tam kan sayımındaki diğer değerlerle (WBC, nötrofil vb.) birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>Lymphocytes</strong> are a type of white blood cell involved in immune response. High or low levels can be linked to infection, viral illness, or certain medications. A single result does not make a diagnosis; your doctor interprets them with other blood count values (WBC, neutrophils, etc.). Discuss your result with a doctor.</p>", "es": "<p>Los <strong>linfocitos</strong> son un tipo de glóbulo blanco que participa en la respuesta inmunitaria. Un valor alto o bajo puede relacionarse con infección, enfermedad viral o ciertos medicamentos. Un solo valor no da el diagnóstico; el médico lo interpreta con el resto del hemograma (WBC, neutrófilos, etc.). Comenta el resultado con un médico.</p>", "de": "<p><strong>Lymphozyten</strong> sind weiße Blutkörperchen und an der Immunantwort beteiligt. Erhöhung oder Erniedrigung kann bei Infektion, Viruserkrankung oder bestimmten Medikamenten vorkommen. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit den übrigen Blutbildwerten (Leukozyten, Neutrophile usw.). Befund mit dem Arzt besprechen.</p>", "fr": "<p>Les <strong>lymphocytes</strong> sont des globules blancs impliqués dans la réponse immunitaire. Un taux élevé ou bas peut être lié à une infection, une maladie virale ou certains médicaments. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec le reste de la NFS (globules blancs, neutrophiles, etc.). Discutez du résultat avec un médecin.</p>", "it": "<p>I <strong>linfociti</strong> sono globuli bianchi coinvolti nella risposta immunitaria. Un valore alto o basso può dipendere da infezione, malattia virale o alcuni farmaci. Un solo valore non fa diagnosi; il medico lo interpreta con gli altri valori dell'emocromo (globuli bianchi, neutrofili, ecc.). Discuti il risultato con il medico.</p>", "he": "<p><strong>לימפוציטים</strong> הם תאי דם לבנים המשתתפים בתגובה החיסונית. ערך גבוה או נמוך יכול להיות קשור לזיהום, מחלה נגיפית או תרופות מסוימות. ערך בודד לא קובע אבחנה; הרופא יפרש עם שאר ערכי ספירת הדם (WBC, נויטרופילים וכו'). יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>लिम्फोसाइट्स</strong> वाइट ब्लड सेल का एक प्रकार हैं; इम्यून रिस्पॉन्स में भूमिका होती है। हाई या लो इन्फेक्शन, वायरल बीमारी या कुछ दवाओं से जुड़ा हो सकता है। अकेला रिज़ल्ट निदान नहीं; डॉक्टर बाकी ब्लड काउंट (WBC, न्यूट्रोफिल आदि) के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>الخلايا اللمفاوية</strong> نوع من كريات الدم البيضاء تشارك في الاستجابة المناعية. ارتفاع أو انخفاض قد يرتبط بعدوى أو مرض فيروسي أو أدوية معينة. الرقم وحده لا يشخّص؛ الطبيب يفسره مع بقية تحليل الدم (WBC، العدلات، إلخ). ناقش نتيجتك مع الطبيب.</p>"}
    body_d = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    d = {"tr": "Uyarı", "en": "Disclaimer", "es": "Aviso", "de": "Hinweis", "fr": "Avertissement", "it": "Disclaimer", "he": "הודעה", "hi": "अस्वीकरण", "ar": "إخلاء المسؤولية"}
    sections_by_lang = {lang: [Section(id="content", level=2, heading=titles[lang], body_html=content[lang]), Section(id="disclaimer", level=2, heading=d[lang], body_html=body_d[lang])] for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(id="lymphocytes-high-or-low", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, icon="/static/images/blog/icons/lymphocytes-high-or-low.svg")


def _article_monocytes_high() -> Article:
    """Monosit yüksekliği / Monocytes high — 9 dil."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/monocytes-high-hero.png"
    slugs = {l: "monocytes-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Monosit yüksek ne anlama gelir?", "en": "What does high monocytes mean?", "es": "Monocitos altos: ¿qué significan?", "de": "Monozyten erhöht: Was bedeutet der Wert?", "fr": "Monocytes élevés : que signifient-ils ?", "it": "Monociti alti: cosa significano?", "he": "מה המשמעות של מונוציטים גבוהים?", "hi": "मोनोसाइट्स हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الوحيدات؟"}
    subtitles = {"tr": "Monosit beyaz kan hücresi türüdür; yüksekliği enfeksiyon veya iltihap ile ilişkili olabilir, hekimce yorumlanır.", "en": "Monocytes are a type of white blood cell; a high level can be related to infection or inflammation and is interpreted by your doctor.", "es": "Los monocitos son un tipo de glóbulo blanco; un valor alto puede relacionarse con infección o inflamación; el médico lo interpreta.", "de": "Monozyten sind weiße Blutkörperchen; Erhöhung kann mit Infektion oder Entzündung zusammenhängen; der Arzt ordnet ein.", "fr": "Les monocytes sont des globules blancs ; un taux élevé peut être lié à une infection ou une inflammation ; le médecin l'interprète.", "it": "I monociti sono globuli bianchi; un valore alto può dipendere da infezione o infiammazione; il medico lo inquadra.", "he": "מונוציטים הם תאי דם לבנים; ערך גבוה יכול להיות קשור לזיהום או דלקת; הרופא יפרש.", "hi": "मोनोसाइट्स वाइट ब्लड सेल हैं; हाई लेवल इन्फेक्शन या सूजन से जुड़ा हो सकता है; डॉक्टर व्याख्या करेंगे।", "ar": "الوحيدات نوع من كريات الدم البيضاء؛ ارتفاعها قد يرتبط بالعدوى أو الالتهاب؛ الطبيب يفسر."}
    excerpts = {"tr": "Monosit yüksekliği tek başına teşhis değildir; tam kan sayımı ve öykü hekimle birlikte değerlendirilir.", "en": "High monocytes alone are not a diagnosis; your doctor assesses them with the full blood count and your history.", "es": "Monocitos altos por sí solos no son un diagnóstico; el médico los valora con el hemograma y tu historia.", "de": "Erhöhte Monozyten allein sind keine Diagnose; der Arzt beurteilt mit Blutbild und Anamnese.", "fr": "Des monocytes élevés seuls ne font pas un diagnostic ; le médecin les évalue avec la NFS et l'histoire.", "it": "Monociti alti da soli non sono una diagnosi; il medico li valuta con emocromo e anamnesi.", "he": "מונוציטים גבוהים לבדם אינם אבחנה; הרופא יבדוק עם ספירת הדם ואנמנזה.", "hi": "मोनोसाइट्स हाई अकेले निदान नहीं; डॉक्टर पूरे ब्लड काउंट और इतिहास के साथ आंकलन करेंगे।", "ar": "ارتفاع الوحيدات وحده ليس تشخيصاً؛ الطبيب يقيّم مع تحليل الدم والتاريخ."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Monosit yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "What high monocytes mean. For information only.", "es": "Monocitos altos. Solo informativo.", "de": "Monozyten erhöht. Nur zur Information.", "fr": "Monocytes élevés. À titre informatif.", "it": "Monociti alti. Solo informativo.", "he": "מונוציטים גבוהים. למידע בלבד.", "hi": "मोनोसाइट्स हाई. केवल सूचनार्थ।", "ar": "ارتفاع الوحيدات. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Monosit kan tahlili — Norya", "en": "Monocytes blood test — Norya", "de": "Monozyten Bluttest — Norya", "es": "Monocitos — Norya", "fr": "Monocytes — Norya", "it": "Monociti — Norya", "he": "מונוציטים — Norya", "hi": "मोनोसाइट्स — Norya", "ar": "الوحيدات — Norya"}
    content = {"tr": "<p><strong>Monosit</strong> beyaz kan hücrelerinin bir türüdür; enfeksiyon ve iltihap yanıtında rol oynar. Yüksek çıkması geçirilen veya süren enfeksiyon, bazı kronik hastalıklar veya iyileşme dönemiyle ilişkili olabilir. Tek başına teşhis koymaz; hekiminiz tam kan sayımı ve öykünüzle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>Monocytes</strong> are a type of white blood cell involved in infection and inflammation response. A high level can be linked to past or current infection, some chronic conditions, or recovery. A single result does not make a diagnosis; your doctor interprets it with the full blood count and your history. Discuss your result with a doctor.</p>", "es": "<p>Los <strong>monocitos</strong> son un tipo de glóbulo blanco que participa en la respuesta a infección e inflamación. Un valor alto puede relacionarse con infección pasada o actual, algunas enfermedades crónicas o recuperación. Un solo valor no da el diagnóstico; el médico lo interpreta con el hemograma y tu historia. Comenta el resultado con un médico.</p>", "de": "<p><strong>Monozyten</strong> sind weiße Blutkörperchen und an der Abwehr von Infektionen und Entzündungen beteiligt. Erhöhung kann bei überstandener oder bestehender Infektion, chronischen Erkrankungen oder in der Erholungsphase vorkommen. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Blutbild und Anamnese. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Les <strong>monocytes</strong> sont des globules blancs impliqués dans la réponse à l'infection et à l'inflammation. Un taux élevé peut être lié à une infection passée ou en cours, à certaines maladies chroniques ou à la convalescence. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec la NFS et l'histoire. Discutez du résultat avec un médecin.</p>", "it": "<p>I <strong>monociti</strong> sono globuli bianchi coinvolti nella risposta a infezioni e infiammazioni. Un valore alto può dipendere da infezione passata o in corso, alcune patologie croniche o dalla fase di guarigione. Un solo valore non fa diagnosi; il medico lo interpreta con emocromo e anamnesi. Discuti il risultato con il medico.</p>", "he": "<p><strong>מונוציטים</strong> הם תאי דם לבנים המשתתפים בתגובה לזיהום ולדלקת. ערך גבוה יכול להיות קשור לזיהום בעבר או בהווה, מחלות כרוניות או החלמה. ערך בודד לא קובע אבחנה; הרופא יפרש עם ספירת הדם ואנמנזה. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>मोनोसाइट्स</strong> वाइट ब्लड सेल का एक प्रकार हैं; इन्फेक्शन और सूजन की प्रतिक्रिया में भूमिका। हाई लेवल पहले या चल रहे इन्फेक्शन, कुछ क्रॉनिक स्थितियों या रिकवरी से जुड़ा हो सकता है। अकेला रिज़ल्ट निदान नहीं; डॉक्टर पूरे ब्लड काउंट और इतिहास के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>الوحيدات</strong> نوع من كريات الدم البيضاء تشارك في الاستجابة للعدوى والالتهاب. ارتفاعها قد يرتبط بعدوى سابقة أو حالية أو أمراض مزمنة أو مرحلة النقاهة. الرقم وحده لا يشخّص؛ الطبيب يفسره مع تحليل الدم والتاريخ. ناقش نتيجتك مع الطبيب.</p>"}
    body_d = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    d = {"tr": "Uyarı", "en": "Disclaimer", "es": "Aviso", "de": "Hinweis", "fr": "Avertissement", "it": "Disclaimer", "he": "הודעה", "hi": "अस्वीकरण", "ar": "إخلاء المسؤولية"}
    sections_by_lang = {lang: [Section(id="content", level=2, heading=titles[lang], body_html=content[lang]), Section(id="disclaimer", level=2, heading=d[lang], body_html=body_d[lang])] for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(id="monocytes-high-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, icon="/static/images/blog/icons/monocytes-high-meaning.svg")


def _article_mcv_high_low() -> Article:
    """MCV yüksek veya düşük / MCV high or low — 9 dil."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/mcv-high-or-low-hero.png"
    slugs = {l: "mcv-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "MCV yüksek veya düşük ne anlama gelir?", "en": "What does high or low MCV mean?", "es": "VCM alto o bajo: ¿qué significa?", "de": "MCV zu hoch oder zu niedrig: Was bedeutet das?", "fr": "VGM élevé ou bas : que signifient-ils ?", "it": "MCV alto o basso: cosa significano?", "he": "מה המשמעות של MCV גבוה או נמוך?", "hi": "MCV हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض MCV؟"}
    subtitles = {"tr": "MCV kırmızı kan hücresi ortalama hacmini gösterir; yüksek veya düşük anemi tipi değerlendirmesinde kullanılır, hekimce yorumlanır.", "en": "MCV shows the average size of red blood cells; high or low is used in assessing anemia type and is interpreted by your doctor.", "es": "El VCM indica el tamaño medio de los glóbulos rojos; alto o bajo se usa para valorar el tipo de anemia; el médico lo interpreta.", "de": "MCV gibt die durchschnittliche Größe der roten Blutkörperchen an; zu hoch oder zu niedrig wird bei der Anämie-Einordnung verwendet.", "fr": "Le VGM indique la taille moyenne des globules rouges ; élevé ou bas sert à évaluer le type d'anémie ; le médecin l'interprète.", "it": "L'MCV indica la dimensione media dei globuli rossi; alto o basso si usa per valutare il tipo di anemia; il medico lo inquadra.", "he": "MCV מציג את הגודל הממוצע של כדוריות הדם האדומות; גבוה או נמוך משמש להערכת סוג אנמיה; הרופא יפרש.", "hi": "MCV लाल रक्त कोशिकाओं का औसत आकार दिखाता है; हाई या लो एनीमिया के प्रकार के आंकलन में इस्तेमाल होता है।", "ar": "MCV يعكس متوسط حجم كريات الدم الحمراء؛ ارتفاع أو انخفاض يُستخدم في تقييم نوع فقر الدم؛ الطبيب يفسر."}
    excerpts = {"tr": "MCV yüksek veya düşük tek başına teşhis değildir; hemoglobin, ferritin ve diğer değerler hekimle birlikte değerlendirilir.", "en": "High or low MCV alone is not a diagnosis; your doctor assesses it with hemoglobin, ferritin, and other values.", "es": "VCM alto o bajo por sí solo no es un diagnóstico; el médico lo valora con hemoglobina, ferritina y el resto.", "de": "MCV zu hoch oder zu niedrig allein ist keine Diagnose; der Arzt beurteilt mit Hämoglobin, Ferritin und weiteren Werten.", "fr": "Un VGM élevé ou bas seul ne fait pas un diagnostic ; le médecin l'évalue avec l'hémoglobine, la ferritine et le reste.", "it": "MCV alto o basso da solo non è una diagnosi; il medico lo valuta con emoglobina, ferritina e altri valori.", "he": "MCV גבוה או נמוך לבדו אינו אבחנה; הרופא יבדוק עם המוגלובין, פריטין ושאר הערכים.", "hi": "MCV हाई या लो अकेले निदान नहीं; डॉक्टर हीमोग्लोबिन, फेरिटिन और बाकी वैल्यू के साथ आंकलन करेंगे।", "ar": "ارتفاع أو انخفاض MCV وحده ليس تشخيصاً؛ الطبيب يقيّم مع الهيموغلوبين والحديد وباقي القيم."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "MCV yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What high or low MCV means. For information only.", "es": "VCM alto o bajo. Solo informativo.", "de": "MCV zu hoch oder zu niedrig. Nur zur Information.", "fr": "VGM élevé ou bas. À titre informatif.", "it": "MCV alto o basso. Solo informativo.", "he": "MCV גבוה או נמוך. למידע בלבד.", "hi": "MCV हाई या लो. केवल सूचनार्थ।", "ar": "ارتفاع أو انخفاض MCV. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "MCV kan tahlili — Norya", "en": "MCV blood test — Norya", "de": "MCV Bluttest — Norya", "es": "VCM — Norya", "fr": "VGM — Norya", "it": "MCV — Norya", "he": "MCV — Norya", "hi": "MCV — Norya", "ar": "MCV — Norya"}
    content = {"tr": "<p><strong>MCV</strong> (ortalama korpusküler hacim) kırmızı kan hücrelerinin ortalama büyüklüğünü gösterir. Düşük MCV genelde demir eksikliği veya talasemi taşıyıcılığıyla; yüksek MCV B12 veya folat eksikliği veya alkol kullanımıyla ilişkili olabilir. Tek başına teşhis koymaz; hekiminiz hemoglobin, ferritin ve diğer değerlerle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>MCV</strong> (mean corpuscular volume) reflects the average size of red blood cells. Low MCV is often linked to iron deficiency or thalassaemia trait; high MCV can be related to B12 or folate deficiency or alcohol use. A single value does not make a diagnosis; your doctor interprets it with hemoglobin, ferritin, and other results. Discuss your result with a doctor.</p>", "es": "<p>El <strong>VCM</strong> (volumen corpuscular medio) refleja el tamaño medio de los glóbulos rojos. Un VCM bajo suele relacionarse con déficit de hierro o rasgo talasémico; uno alto puede deberse a déficit de B12 o folato o consumo de alcohol. Un solo valor no da el diagnóstico; el médico lo interpreta con hemoglobina, ferritina y el resto. Comenta el resultado con un médico.</p>", "de": "<p><strong>MCV</strong> (mittleres korpuskuläres Volumen) gibt die durchschnittliche Größe der roten Blutkörperchen an. Niedriges MCV kann bei Eisenmangel oder Thalassämie-Trägerschaft vorkommen; hohes MCV bei B12- oder Folsäuremangel oder Alkohol. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Hämoglobin, Ferritin und weiteren Befunden. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>VGM</strong> (volume globulaire moyen) reflète la taille moyenne des globules rouges. Un VGM bas est souvent lié à une carence en fer ou un trait thalassémique ; un VGM élevé peut être lié à une carence en B12 ou folates ou à l'alcool. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec l'hémoglobine, la ferritine et le reste. Discutez du résultat avec un médecin.</p>", "it": "<p>L'<strong>MCV</strong> (volume corpuscolare medio) riflette la dimensione media dei globuli rossi. MCV basso può dipendere da carenza di ferro o tratto talassemico; MCV alto da carenza di B12 o folati o alcol. Un solo valore non fa diagnosi; il medico lo interpreta con emoglobina, ferritina e altri esami. Discuti il risultato con il medico.</p>", "he": "<p><strong>MCV</strong> (נפח כדורית ממוצע) משקף את הגודל הממוצע של כדוריות הדם האדומות. MCV נמוך קשור לעיתים לחוסר ברזל או נשאות תלסמיה; MCV גבוה ל-B12 או חומצה פולית או אלכוהול. ערך בודד לא קובע אבחנה; הרופא יפרש עם המוגלובין, פריטין ושאר התוצאות. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>MCV</strong> (मीन कॉर्पस्क्युलर वॉल्यूम) लाल रक्त कोशिकाओं का औसत आकार दिखाता है। लो MCV अक्सर आयरन की कमी या थैलेसीमिया ट्रेट से जुड़ा; हाई MCV B12 या फोलेट की कमी या शराब से हो सकता है। अकेला वैल्यू निदान नहीं; डॉक्टर हीमोग्लोबिन, फेरिटिन और बाकी रिज़ल्ट के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>MCV</strong> (متوسط حجم الكرية) يعكس متوسط حجم كريات الدم الحمراء. انخفاض MCV غالباً يرتبط بنقص الحديد أو سمة الثلاسيميا؛ ارتفاعه قد يكون بسبب نقص B12 أو الفولات أو الكحول. الرقم وحده لا يشخّص؛ الطبيب يفسره مع الهيموغلوبين والحديد وباقي النتائج. ناقش نتيجتك مع الطبيب.</p>"}
    body_d = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    d = {"tr": "Uyarı", "en": "Disclaimer", "es": "Aviso", "de": "Hinweis", "fr": "Avertissement", "it": "Disclaimer", "he": "הודעה", "hi": "अस्वीकरण", "ar": "إخلاء المسؤولية"}
    sections_by_lang = {lang: [Section(id="content", level=2, heading=titles[lang], body_html=content[lang]), Section(id="disclaimer", level=2, heading=d[lang], body_html=body_d[lang])] for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(id="mcv-high-or-low", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, icon="/static/images/blog/icons/mcv-high-or-low.svg")


def _article_rdw_high() -> Article:
    """RDW yüksekliği / RDW high — 9 dil."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/rdw-high-hero.png"
    slugs = {l: "rdw-high-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Hemogram", "en": "Blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "RDW yüksek ne anlama gelir?", "en": "What does high RDW mean?", "es": "RDW alto: ¿qué significa?", "de": "RDW erhöht: Was bedeutet der Wert?", "fr": "RDW élevé : que signifient-ils ?", "it": "RDW alto: cosa significa?", "he": "מה המשמעות של RDW גבוה?", "hi": "RDW हाई का क्या मतलब है?", "ar": "ماذا يعني ارتفاع RDW؟"}
    subtitles = {"tr": "RDW kırmızı kan hücresi boyut dağılımını gösterir; yüksekliği anemi veya beslenme ile ilişkili olabilir, hekimce yorumlanır.", "en": "RDW reflects the variation in red blood cell size; a high value can be related to anemia or nutrition and is interpreted by your doctor.", "es": "El RDW refleja la variación en el tamaño de los glóbulos rojos; un valor alto puede relacionarse con anemia o nutrición; el médico lo interpreta.", "de": "RDW gibt die Verteilung der Größe der roten Blutkörperchen an; Erhöhung kann bei Anämie oder Ernährung vorkommen; der Arzt ordnet ein.", "fr": "Le RDW reflète la variation de taille des globules rouges ; un taux élevé peut être lié à une anémie ou la nutrition ; le médecin l'interprète.", "it": "L'RDW riflette la variazione di dimensione dei globuli rossi; un valore alto può dipendere da anemia o nutrizione; il medico lo inquadra.", "he": "RDW משקף את השונות בגודל כדוריות הדם האדומות; ערך גבוה יכול להיות קשור לאנמיה או תזונה; הרופא יפרש.", "hi": "RDW लाल रक्त कोशिकाओं के आकार में विविधता दिखाता है; हाई वैल्यू एनीमिया या पोषण से जुड़ी हो सकती है; डॉक्टर व्याख्या करेंगे।", "ar": "RDW يعكس تباين حجم كريات الدم الحمراء؛ ارتفاعه قد يرتبط بفقر الدم أو التغذية؛ الطبيب يفسر."}
    excerpts = {"tr": "RDW yüksekliği tek başına teşhis değildir; hemoglobin, MCV ve ferritin hekimle birlikte değerlendirilir.", "en": "High RDW alone is not a diagnosis; your doctor assesses it with hemoglobin, MCV, and ferritin.", "es": "RDW alto por sí solo no es un diagnóstico; el médico lo valora con hemoglobina, VCM y ferritina.", "de": "Erhöhtes RDW allein ist keine Diagnose; der Arzt beurteilt mit Hämoglobin, MCV und Ferritin.", "fr": "Un RDW élevé seul ne fait pas un diagnostic ; le médecin l'évalue avec l'hémoglobine, le VGM et la ferritine.", "it": "RDW alto da solo non è una diagnosi; il medico lo valuta con emoglobina, MCV e ferritina.", "he": "RDW גבוה לבדו אינו אבחנה; הרופא יבדוק עם המוגלובין, MCV ופריטין.", "hi": "RDW हाई अकेले निदान नहीं; डॉक्टर हीमोग्लोबिन, MCV और फेरिटिन के साथ आंकलन करेंगे।", "ar": "ارتفاع RDW وحده ليس تشخيصاً؛ الطبيب يقيّم مع الهيموغلوبين وMCV والحديد."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "RDW yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "What high RDW means. For information only.", "es": "RDW alto. Solo informativo.", "de": "RDW erhöht. Nur zur Information.", "fr": "RDW élevé. À titre informatif.", "it": "RDW alto. Solo informativo.", "he": "RDW גבוה. למידע בלבד.", "hi": "RDW हाई. केवल सूचनार्थ।", "ar": "ارتفاع RDW. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "RDW kan tahlili — Norya", "en": "RDW blood test — Norya", "de": "RDW Bluttest — Norya", "es": "RDW — Norya", "fr": "RDW — Norya", "it": "RDW — Norya", "he": "RDW — Norya", "hi": "RDW — Norya", "ar": "RDW — Norya"}
    content = {"tr": "<p><strong>RDW</strong> (eritrosit dağılım genişliği) kırmızı kan hücrelerinin boyutlarındaki farklılığı gösterir. Yüksek RDW, hücre boyutlarında daha fazla dağılım olduğunu (anisositoz) ifade eder; demir, B12 veya folat eksikliği gibi anemi türlerinde sıklıkla görülür. Tek başına teşhis koymaz; hekiminiz hemoglobin, MCV ve ferritinle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>RDW</strong> (red cell distribution width) reflects how much the size of red blood cells varies. A high RDW means more variation in cell size (anisocytosis) and is often seen in anemias such as iron, B12, or folate deficiency. A single value does not make a diagnosis; your doctor interprets it with hemoglobin, MCV, and ferritin. Discuss your result with a doctor.</p>", "es": "<p>El <strong>RDW</strong> (amplitud de distribución eritrocitaria) refleja la variación en el tamaño de los glóbulos rojos. Un RDW alto indica más variación (anisocitosis) y suele verse en anemias por déficit de hierro, B12 o folato. Un solo valor no da el diagnóstico; el médico lo interpreta con hemoglobina, VCM y ferritina. Comenta el resultado con un médico.</p>", "de": "<p><strong>RDW</strong> (Verteilungsbreite der Erythrozyten) gibt die Streuung der Größe der roten Blutkörperchen an. Erhöhtes RDW bedeutet stärkere Streuung (Anisozytose) und kommt oft bei Anämien (Eisen-, B12- oder Folsäuremangel) vor. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Hämoglobin, MCV und Ferritin. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>RDW</strong> (largeur de distribution des globules rouges) reflète la variation de taille des globules rouges. Un RDW élevé signifie plus de variation (anisocytose) et s'observe souvent dans les anémies (carence en fer, B12 ou folates). Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec l'hémoglobine, le VGM et la ferritine. Discutez du résultat avec un médecin.</p>", "it": "<p>L'<strong>RDW</strong> (ampiezza di distribuzione dei globuli rossi) riflette la variazione di dimensione. RDW alto indica più variazione (anisocitosi) e si vede spesso nelle anemie da carenza di ferro, B12 o folati. Un solo valore non fa diagnosi; il medico lo interpreta con emoglobina, MCV e ferritina. Discuti il risultato con il medico.</p>", "he": "<p><strong>RDW</strong> (רוחב התפלגות כדוריות) משקף את השונות בגודל כדוריות הדם האדומות. RDW גבוה משמע יותר שונות (אניזוציטוזיס) ומופיע לעיתים באנמיה (חוסר ברזל, B12 או חומצה פולית). ערך בודד לא קובע אבחנה; הרופא יפרש עם המוגלובין, MCV ופריטין. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>RDW</strong> (रेड सेल डिस्ट्रिब्यूशन विड्थ) लाल रक्त कोशिकाओं के आकार में भिन्नता दिखाता है। हाई RDW का मतलब ज़्यादा भिन्नता (एनिसोसाइटोसिस); आयरन, B12 या फोलेट की कमी वाली एनीमिया में अक्सर दिखता है। अकेला वैल्यू निदान नहीं; डॉक्टर हीमोग्लोबिन, MCV और फेरिटिन के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>RDW</strong> (عرض توزيع كريات الدم الحمراء) يعكس تباين حجم الكريات. ارتفاع RDW يعني تبايناً أكبر (عدم تساوي الكريات) ويُشاهد غالباً في فقر الدم (نقص الحديد أو B12 أو الفولات). الرقم وحده لا يشخّص؛ الطبيب يفسره مع الهيموغلوبين وMCV والحديد. ناقش نتيجتك مع الطبيب.</p>"}
    body_d = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    d = {"tr": "Uyarı", "en": "Disclaimer", "es": "Aviso", "de": "Hinweis", "fr": "Avertissement", "it": "Disclaimer", "he": "הודעה", "hi": "अस्वीकरण", "ar": "إخلاء المسؤولية"}
    sections_by_lang = {lang: [Section(id="content", level=2, heading=titles[lang], body_html=content[lang]), Section(id="disclaimer", level=2, heading=d[lang], body_html=body_d[lang])] for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(id="rdw-high-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, icon="/static/images/blog/icons/rdw-high-meaning.svg")


def _article_ag_ratio_high_low() -> Article:
    """A/G oranı yüksek veya düşük / A/G ratio high or low — 9 dil."""
    published = date(2026, 3, 20)
    cover = "/static/images/blog/ag-ratio-high-or-low-hero.png"
    slugs = {l: "ag-ratio-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "A/G oranı yüksek veya düşük ne anlama gelir?", "en": "What does a high or low A/G ratio mean?", "es": "Relación A/G alta o baja: ¿qué significa?", "de": "A/G-Quotient zu hoch oder zu niedrig: Was bedeutet das?", "fr": "Rapport A/G élevé ou bas : que signifient-ils ?", "it": "Rapporto A/G alto o basso: cosa significano?", "he": "מה המשמעות של יחס A/G גבוה או נמוך?", "hi": "A/G रेशियो हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض نسبة A/G؟"}
    subtitles = {"tr": "A/G oranı albümin/globulin oranıdır; yüksek veya düşük karaciğer veya bağışıklıkla ilişkili olabilir, hekimce yorumlanır.", "en": "A/G ratio is albumin to globulin; high or low can be related to liver or immunity and is interpreted by your doctor.", "es": "La relación A/G es albúmina/globulina; alta o baja puede relacionarse con hígado o inmunidad; el médico la interpreta.", "de": "Der A/G-Quotient ist Albumin zu Globulin; zu hoch oder zu niedrig kann mit Leber oder Immunität zusammenhängen.", "fr": "Le rapport A/G est albumine/globulines ; élevé ou bas peut être lié au foie ou à l'immunité ; le médecin l'interprète.", "it": "Il rapporto A/G è albumina/globuline; alto o basso può dipendere da fegato o immunità; il medico lo inquadra.", "he": "יחס A/G הוא אלבומין לגלובולין; גבוה או נמוך יכול להיות קשור לכבד או חיסון; הרופא יפרש.", "hi": "A/G रेशियो ऐल्ब्यूमिन/ग्लोब्युलिन है; हाई या लो लिवर या इम्युनिटी से जुड़ा हो सकता है; डॉक्टर व्याख्या करेंगे।", "ar": "نسبة A/G هي الألبومين إلى الغلوبولين؛ ارتفاع أو انخفاض قد يرتبط بالكبد أو المناعة؛ الطبيب يفسر."}
    excerpts = {"tr": "A/G oranı yüksek veya düşük tek başına teşhis değildir; total protein, albümin ve karaciğer testleri hekimle birlikte değerlendirilir.", "en": "High or low A/G ratio alone is not a diagnosis; your doctor assesses it with total protein, albumin, and liver tests.", "es": "Relación A/G alta o baja por sí sola no es un diagnóstico; el médico la valora con proteínas totales, albúmina y pruebas hepáticas.", "de": "A/G-Quotient zu hoch oder zu niedrig allein ist keine Diagnose; der Arzt beurteilt mit Gesamteiweiß, Albumin und Leberwerten.", "fr": "Un rapport A/G élevé ou bas seul ne fait pas un diagnostic ; le médecin l'évalue avec les protéines totales, l'albumine et le bilan hépatique.", "it": "Rapporto A/G alto o basso da solo non è una diagnosi; il medico lo valuta con proteine totali, albumina ed esami epatici.", "he": "יחס A/G גבוה או נמוך לבדו אינו אבחנה; הרופא יבדוק עם חלבון כללי, אלבומין ובדיקות כבד.", "hi": "A/G रेशियो हाई या लो अकेले निदान नहीं; डॉक्टर टोटल प्रोटीन, ऐल्ब्यूमिन और लिवर टेस्ट के साथ आंकलन करेंगे।", "ar": "ارتفاع أو انخفاض نسبة A/G وحده ليس تشخيصاً؛ الطبيب يقيّم مع البروتين الكلي والألبومين وفحوص الكبد."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "A/G oranı yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What high or low A/G ratio means. For information only.", "es": "Relación A/G alta o baja. Solo informativo.", "de": "A/G-Quotient zu hoch oder zu niedrig. Nur zur Information.", "fr": "Rapport A/G élevé ou bas. À titre informatif.", "it": "Rapporto A/G alto o basso. Solo informativo.", "he": "יחס A/G גבוה או נמוך. למידע בלבד.", "hi": "A/G रेशियो हाई या लो. केवल सूचनार्थ।", "ar": "نسبة A/G مرتفعة أو منخفضة. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "A/G oranı kan tahlili — Norya", "en": "A/G ratio blood test — Norya", "de": "A/G-Quotient Bluttest — Norya", "es": "Relación A/G — Norya", "fr": "Rapport A/G — Norya", "it": "Rapporto A/G — Norya", "he": "יחס A/G — Norya", "hi": "A/G रेशियो — Norya", "ar": "نسبة A/G — Norya"}
    content = {"tr": "<p><strong>A/G oranı</strong> albüminin globulinlere oranıdır; total protein tahlilinden türetilir. Yüksek oran albüminin göreli artışı veya globulin düşüklüğü; düşük oran albümin düşüklüğü veya globulin artışı (örn. kronik iltihap) ile ilişkili olabilir. Tek başına teşhis koymaz; hekiminiz total protein, albümin ve karaciğer testleriyle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p>The <strong>A/G ratio</strong> is albumin divided by globulins; it is derived from total protein. A high ratio may reflect relatively more albumin or low globulins; a low ratio can be related to low albumin or raised globulins (e.g. chronic inflammation). A single value does not make a diagnosis; your doctor interprets it with total protein, albumin, and liver tests. Discuss your result with a doctor.</p>", "es": "<p>La <strong>relación A/G</strong> es albúmina entre globulinas; se obtiene de las proteínas totales. Una relación alta puede reflejar más albúmina o pocas globulinas; una baja puede deberse a albúmina baja o globulinas altas (p. ej. inflamación crónica). Un solo valor no da el diagnóstico; el médico lo interpreta con proteínas totales, albúmina y pruebas hepáticas. Comenta el resultado con un médico.</p>", "de": "<p>Der <strong>A/G-Quotient</strong> ist Albumin geteilt durch Globuline; er wird aus dem Gesamteiweiß abgeleitet. Ein hoher Quotient kann relativ mehr Albumin oder wenig Globuline bedeuten; ein niedriger bei wenig Albumin oder erhöhten Globulinen (z. B. chronische Entzündung). Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Gesamteiweiß, Albumin und Leberwerten. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>rapport A/G</strong> est albumine divisée par les globulines ; il est dérivé des protéines totales. Un rapport élevé peut refléter plus d'albumine ou peu de globulines ; un rapport bas peut être lié à une albumine basse ou des globulines élevées (ex. inflammation chronique). Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec les protéines totales, l'albumine et le bilan hépatique. Discutez du résultat avec un médecin.</p>", "it": "<p>Il <strong>rapporto A/G</strong> è albumina diviso globuline; si ricava dalle proteine totali. Un rapporto alto può riflettere più albumina o poche globuline; uno basso può dipendere da albumina bassa o globuline alte (es. infiammazione cronica). Un solo valore non fa diagnosi; il medico lo interpreta con proteine totali, albumina ed esami epatici. Discuti il risultato con il medico.</p>", "he": "<p><strong>יחס A/G</strong> הוא אלבומין חלקי גלובולינים; נגזר מחלבון כללי. יחס גבוה יכול לשקף יותר אלבומין או מעט גלובולינים; נמוך — אלבומין נמוך או גלובולינים מוגברים (למשל דלקת כרונית). ערך בודד לא קובע אבחנה; הרופא יפרש עם חלבון כללי, אלבומין ובדיקות כבד. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>A/G रेशियो</strong> ऐल्ब्यूमिन को ग्लोब्युलिन से भाग देने पर आता है; टोटल प्रोटीन से निकाला जाता है। हाई रेशियो ज़्यादा ऐल्ब्यूमिन या कम ग्लोब्युलिन; लो रेशियो ऐल्ब्यूमिन कम या ग्लोब्युलिन बढ़ा (जैसे क्रॉनिक इन्फ्लेमेशन) से जुड़ा हो सकता है। अकेला वैल्यू निदान नहीं; डॉक्टर टोटल प्रोटीन, ऐल्ब्यूमिन और लिवर टेस्ट के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>نسبة A/G</strong> هي الألبومين مقسوماً على الغلوبولينات؛ تُستمد من البروتين الكلي. نسبة عالية قد تعكس ألبوميناً أكثر أو غلوبولينات قليلة؛ منخفضة قد تكون بسبب ألبومين منخفض أو غلوبولينات مرتفعة (مثل التهاب مزمن). الرقم وحده لا يشخّص؛ الطبيب يفسره مع البروتين الكلي والألبومين وفحوص الكبد. ناقش نتيجتك مع الطبيب.</p>"}
    body_d = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    d = {"tr": "Uyarı", "en": "Disclaimer", "es": "Aviso", "de": "Hinweis", "fr": "Avertissement", "it": "Disclaimer", "he": "הודעה", "hi": "अस्वीकरण", "ar": "إخلاء المسؤولية"}
    sections_by_lang = {lang: [Section(id="content", level=2, heading=titles[lang], body_html=content[lang]), Section(id="disclaimer", level=2, heading=d[lang], body_html=body_d[lang])] for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(id="ag-ratio-high-or-low", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, icon="/static/images/blog/icons/ag-ratio-high-or-low.svg")


def _article_hematocrit_high_low() -> Article:
    """Hematocrit high or low — Yeni konu dalgası 1. konu (9 dil)."""
    published = date(2026, 3, 13)
    cover = "/static/images/blog/hematocrit-hero.png"
    slugs = {l: "hematocrit-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(
        id="hematocrit-high-or-low",
        published_at=published,
        read_minutes=5,
        cover_image=cover,
        category={"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"},
        slugs=slugs,
        titles={"tr": "Hematokrit yüksek veya düşük ne anlama gelir?", "en": "Hematocrit high or low: what it means", "es": "Hematocrito alto o bajo: qué significa", "de": "Hämatokrit zu hoch oder zu niedrig: Was bedeutet das?", "fr": "Hématocrite haut ou bas : qu'est-ce que ça indique ?", "it": "Ematocrito alto o basso: cosa significa?", "he": "המטוקריט גבוה או נמוך: מה המשמעות?", "hi": "हीमाटोक्रिट हाई या लो का क्या मतलब?", "ar": "الهيماتوكريت مرتفع أو منخفض: ماذا يعني؟"},
        subtitles={"tr": "Hematokrit, kırmızı kan hücrelerinin kandaki oranını gösterir; yüksek veya düşük çıkması tek başına teşhis değildir, hekimle yorumlanır.", "en": "Hematocrit reflects the proportion of red blood cells in your blood; high or low is not a diagnosis on its own—your doctor interprets it in context.", "es": "El hematocrito refleja la proporción de glóbulos rojos en sangre; alto o bajo no es un diagnóstico por sí solo—el médico lo interpreta en contexto.", "de": "Der Hämatokrit zeigt den Anteil der roten Blutkörperchen; zu hoch oder zu niedrig ist keine Diagnose für sich—der Arzt ordnet ihn ein.", "fr": "L'hématocrite reflète la proportion de globules rouges ; un taux haut ou bas seul ne fait pas un diagnostic—le médecin l'interprète.", "it": "L'ematocrito riflette la proporzione di globuli rossi; alto o basso da solo non è una diagnosi—il medico lo inquadra.", "he": "המטוקריט משקף את חלקם של כדוריות הדם האדומות; גבוה או נמוך לבדו אינו אבחנה—הרופא יפרש בהקשר.", "hi": "हीमाटोक्रिट लाल रक्त कोशिकाओं का अनुपात दिखाता है; हाई या लो अकेले निदान नहीं—डॉक्टर संदर्भ में देखेंगे।", "ar": "الهيماتوكريت يعكس نسبة كريات الدم الحمراء؛ ارتفاع أو انخفاض وحده ليس تشخيصاً—الطبيب يفسره في السياق."},
        excerpts={"tr": "Hematokrit CBC'de sık görülen bir değerdir; yüksek veya düşük nedenleri hekim tarafından diğer sonuçlarla birlikte değerlendirilir.", "en": "Hematocrit is a common CBC value; causes of high or low are assessed by your doctor together with other results.", "es": "El hematocrito es un valor habitual del hemograma; las causas de alto o bajo las valora el médico con el resto.", "de": "Hämatokrit ist ein üblicher Blutbildwert; Ursachen für hoch oder niedrig beurteilt der Arzt mit den übrigen Befunden.", "fr": "L'hématocrite est une valeur courante de la NFS ; les causes d'un taux haut ou bas sont évaluées par le médecin avec le bilan.", "it": "L'ematocrito è un valore comune dell'emocromo; le cause di alto o basso le valuta il medico con gli altri esami.", "he": "המטוקריט הוא ערך נפוץ בספירת הדם; סיבות לגבוה או נמוך יבדקו עם הרופא עם שאר התוצאות.", "hi": "हीमाटोक्रिट CBC का आम वैल्यू है; हाई या लो के कारण डॉक्टर बाकी रिज़ल्ट के साथ आंकलन करेंगे।", "ar": "الهيماتوكريت قيمة شائعة في تحليل الدم؛ أسباب الارتفاع أو الانخفاض يقيّمها الطبيب مع بقية النتائج."},
        seo_titles={"tr": "Hematokrit Yüksek veya Düşük Ne Anlama Gelir? | Norya Blog", "en": "Hematocrit High or Low: What It Means | Norya Blog", "es": "Hematocrito alto o bajo | Norya Blog", "de": "Hämatokrit zu hoch oder zu niedrig | Norya Blog", "fr": "Hématocrite haut ou bas | Norya Blog", "it": "Ematocrito alto o basso | Norya Blog", "he": "המטוקריט גבוה או נמוך | Norya Blog", "hi": "हीमाटोक्रिट हाई या लो | Norya Blog", "ar": "الهيماتوكريت مرتفع أو منخفض | Norya Blog"},
        seo_descriptions={"tr": "Hematokrit yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What hematocrit high or low means. For information only.", "es": "Hematocrito alto o bajo: causas. Solo informativo.", "de": "Hämatokrit zu hoch oder zu niedrig. Nur zur Information.", "fr": "Hématocrite haut ou bas. À titre informatif.", "it": "Ematocrito alto o basso. Solo informativo.", "he": "המטוקריט גבוה או נמוך. למידע בלבד.", "hi": "हीमाटोक्रिट हाई या लो. केवल सूचनार्थ।", "ar": "الهيماتوكريت مرتفع أو منخفض. لأغراض إعلامية فقط."},
        cover_alt={"tr": "Hematokrit kan tahlili — Norya", "en": "Hematocrit blood test — Norya", "es": "Hematocrito — Norya", "de": "Hämatokrit Bluttest — Norya", "fr": "Hématocrite — Norya", "it": "Ematocrito — Norya", "he": "המטוקריט — Norya", "hi": "हीमाटोक्रिट — Norya", "ar": "الهيماتوكريت — Norya"},
        sections_by_lang={
            "tr": [
                Section(
                    id="hematocrit-nedir",
                    level=2,
                    heading="Hematokrit nedir?",
                    body_html=(
                        "<p><strong>Hematokrit</strong>, kanınızın toplam hacmi içinde kırmızı kan hücrelerinin kapladığı yüzdedir. "
                        "Tam kan sayımında (CBC) en sık görülen parametrelerden biridir ve kanın ne kadar \"seyrek\" veya \"yoğun\" "
                        "olduğuna dair genel bir fikir verir. Bu değer tek başına bir hastalığı kanıtlamaz; sadece kan dolaşımınız "
                        "hakkında ek bir bilgi katmanı sunar.</p>"
                        "<p>Laboratuvar raporlarında hematokrit için yaşa, biyolojik cinsiyete ve kullanılan cihaza göre değişen "
                        "referans aralıkları bulunur. Bu yüzden rapordaki \"normal\" aralığı mutlaka dikkate almak gerekir. "
                        "Hekiminiz hematokriti; kırmızı hücre sayısı, oksijen taşıyan maddelerin düzeyi, kalp–damar ve solunum "
                        "sistemi ile ilgili öykünüz ve fizik muayene bulgularınızla birlikte yorumlar.</p>"
                    ),
                ),
                Section(
                    id="yuksek-dusuk",
                    level=2,
                    heading="Hematokrit yüksek veya düşük çıkarsa",
                    body_html=(
                        "<p><strong>Düşük hematokrit</strong>, kanda kırmızı hücre hacminin azaldığını gösterir ve yorgunluk, nefes "
                        "darlığı, çabuk yorulma gibi şikâyetlerle birlikte görülebilir. Uzun süren kan kaybı, bazı kronik hastalıklar "
                        "ve beslenme yetersizlikleri tabloya eşlik edebilir; ancak tek bir düşük değerle nedenin ne olduğu "
                        "söylenemez. Değerin hangi hızla düştüğü, diğer kan sayımı parametreleri ve hikâyeniz tanı sürecinde "
                        "kritik öneme sahiptir.</p>"
                        "<p><strong>Yüksek hematokrit</strong> ise kanın daha \"yoğun\" hale geldiği durumlarda görülebilir. "
                        "Sıvı kaybı (örneğin az su içmek, yoğun terleme, ishal), sigara kullanımı, uzun süre yüksek rakımda "
                        "yaşamak veya nadiren kemik iliğiyle ilişkili hastalıklar bu tabloya eşlik edebilir. Yüksek bir değer "
                        "damar içindeki akışkanlığı etkileyebileceği için hekimler genellikle eşlik eden şikâyetleri, tansiyon "
                        "ve nabız gibi yaşamsal bulguları, kalp–damar öyküsünü ve diğer testleri birlikte değerlendirir. "
                        "Sonucunuzu mutlaka hekiminizle görüşün; isterseniz randevu öncesi hazırlık için "
                        "<a href=\"/tr/blog/kan-tahlili-nasil-okunur\">kan tahlili sonuçlarını nasıl okuyacağınız</a> rehberimize de göz atabilirsiniz.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Uyarı",
                    body_html=(
                        "<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; kişisel tıbbi değerlendirme veya teşhis yerine "
                        "geçmez.</strong> Hematokritin tek başına düşük ya da yüksek çıkması, altta yatan nedenin kesin olarak "
                        "bilindiği anlamına gelmez. Sonuçlarınızı; şikâyetleriniz, kullandığınız ilaçlar ve önceki tahlillerinizle "
                        "birlikte hekiminiz değerlendirmelidir.</p>"
                        "<p>Raporunuzu daha yapılandırılmış biçimde gözden geçirmek isterseniz kan tahlili analiz aracımızı "
                        "kullanabilirsiniz: <a href=\"/analyze\">Analiz</a>. Ücretlendirme ve paketler için "
                        "<a href=\"/tr/pricing\">Fiyatlandırma</a> sayfasına göz atabilirsiniz.</p>"
                    ),
                ),
            ],
            "en": [
                Section(
                    id="what-is-hematocrit",
                    level=2,
                    heading="What is hematocrit?",
                    body_html=(
                        "<p><strong>Hematocrit</strong> is the percentage of your blood volume that is occupied by red blood cells. "
                        "You will usually see it reported on a complete blood count (CBC). Together with the oxygen‑carrying "
                        "components of red cells and the overall cell count, it helps your doctor understand how concentrated or "
                        "diluted your blood is.</p>"
                        "<p>Each laboratory uses its own reference ranges based on age, sex and equipment, so “normal” on one "
                        "report may look slightly different on another. Hematocrit on its own never proves or rules out a "
                        "condition. It is only one piece of the puzzle and is interpreted alongside your symptoms, examination, "
                        "other blood tests and, when needed, imaging or further investigations.</p>"
                    ),
                ),
                Section(
                    id="high-or-low",
                    level=2,
                    heading="When hematocrit is high or low",
                    body_html=(
                        "<p><strong>Low hematocrit</strong> means that red cells make up a smaller proportion of your blood volume. "
                        "People may notice tiredness, reduced exercise tolerance, shortness of breath on exertion or paleness, "
                        "but some have no symptoms at all, especially if the drop is slow. Long‑term blood loss, nutritional "
                        "issues or long‑standing illnesses can be associated, yet a single low reading cannot tell you the exact "
                        "cause. Trends over time, the rest of the CBC and your clinical story are all important.</p>"
                        "<p><strong>High hematocrit</strong> suggests that the blood is relatively more concentrated with red cells. "
                        "This can happen when you are short on fluids (for example with limited water intake, heavy sweating or "
                        "vomiting and diarrhoea), in people who live at high altitude, in smokers, or more rarely due to bone "
                        "marrow conditions. A higher value does not automatically mean there is a serious disease, but it prompts "
                        "your doctor to look at blood pressure, circulation, heart and lung health and any medicines you take. "
                        "Always discuss your result with a clinician; our <a href=\"/en/blog/how-to-read-blood-test-results\">guide "
                        "to understanding blood test results</a> can help you prepare questions for your appointment.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Disclaimer",
                    body_html=(
                        "<p><strong>This article is for information only and is not a diagnosis or treatment plan.</strong> "
                        "Hematocrit values must be interpreted in the context of your full medical history, examination and "
                        "other test results. Only a qualified health professional who knows you can make or exclude a diagnosis.</p>"
                        "<p>If you would like a structured, plain‑language overview of your lab report, you can use our "
                        "<a href=\"/analyze\">analysis</a> tool and review available options on the <a href=\"/en/pricing\">Pricing</a> "
                        "page. These services are designed to support, not replace, your conversation with your doctor.</p>"
                    ),
                ),
            ],
            "es": [
                Section(
                    id="que-es-hematocrito",
                    level=2,
                    heading="¿Qué es el hematocrito?",
                    body_html=(
                        "<p>El <strong>hematocrito</strong> indica qué porcentaje del volumen de sangre está formado por glóbulos rojos. "
                        "Es un valor básico del hemograma y ayuda a saber si la sangre está más concentrada o más diluida. No es una "
                        "medida aislada de salud, sino un dato adicional que el médico combina con el resto de parámetros.</p>"
                        "<p>Los rangos de referencia dependen del laboratorio, la edad y el sexo, por lo que conviene fijarse siempre "
                        "en los límites \"mínimo\" y \"máximo\" que aparecen en tu propio informe. Un hematocrito fuera de rango no "
                        "explica por sí solo cuál es el motivo; el médico tiene en cuenta síntomas, exploración física, otros "
                        "análisis y, si hace falta, pruebas complementarias.</p>"
                    ),
                ),
                Section(
                    id="alto-o-bajo",
                    level=2,
                    heading="Hematocrito alto o bajo",
                    body_html=(
                        "<p>Un <strong>hematocrito bajo</strong> significa que la proporción de glóbulos rojos es menor de lo esperado. "
                        "Puede acompañarse de cansancio, sensación de falta de aire con el esfuerzo, mareos o palidez, aunque muchas "
                        "personas no notan nada cuando el descenso es lento. Pérdidas de sangre, dificultades en la producción de "
                        "células rojas o enfermedades crónicas pueden influir, pero un solo dato no permite saber la causa exacta.</p>"
                        "<p>Un <strong>hematocrito alto</strong> sugiere que la sangre está más concentrada. La deshidratación, vivir "
                        "a gran altitud, fumar o determinadas situaciones médicas pueden elevar este valor. En algunos casos el médico "
                        "revisa la presión arterial, el estado de hidratación, el corazón, los pulmones y la medicación que tomas para "
                        "decidir si hacen falta más estudios. Comenta siempre tus resultados con el profesional que te sigue; nuestra "
                        "<a href=\"/es/blog/como-leer-analisis-sangre\">guía para entender el análisis de sangre</a> puede ayudarte a "
                        "preparar la consulta.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Aviso",
                    body_html=(
                        "<p><strong>Este contenido es solo informativo y no reemplaza una valoración médica individual.</strong> "
                        "El hematocrito debe interpretarse junto con el resto del hemograma, otros análisis y la historia clínica. "
                        "Solo un profesional que conoce tu caso puede confirmar o descartar diagnósticos.</p>"
                        "<p>Si quieres revisar tu informe de forma estructurada y en lenguaje sencillo, puedes usar nuestra página "
                        "de <a href=\"/analyze\">análisis</a> y consultar las opciones disponibles en <a href=\"/es/pricing\">Precios</a>. "
                        "Estas herramientas son un apoyo a la consulta médica, no un sustituto.</p>"
                    ),
                ),
            ],
            "de": [
                Section(
                    id="was-ist-haematokrit",
                    level=2,
                    heading="Was ist der Hämatokrit?",
                    body_html=(
                        "<p>Der <strong>Hämatokrit</strong> beschreibt, wie viel Prozent Ihres Blutvolumens aus roten Blutkörperchen "
                        "bestehen. Er ist ein Standardwert im Blutbild und hilft einzuordnen, ob das Blut eher verdünnt oder eher "
                        "eingedickt wirkt. Für sich allein sagt der Wert noch nichts über die eigentliche Ursache aus.</p>"
                        "<p>Referenzbereiche unterscheiden sich je nach Labor, Alter, biologischem Geschlecht und Messmethode. "
                        "Deshalb ist es wichtig, immer die Normspanne auf Ihrem eigenen Laborbericht heranzuziehen. Ärzte werten "
                        "den Hämatokrit nie isoliert, sondern gemeinsam mit anderen Blutwerten, Beschwerden, Vorerkrankungen und "
                        "gegebenenfalls weiteren Untersuchungen aus.</p>"
                    ),
                ),
                Section(
                    id="hoch-oder-niedrig",
                    level=2,
                    heading="Hämatokrit zu hoch oder zu niedrig",
                    body_html=(
                        "<p>Ein <strong>niedriger Hämatokrit</strong> bedeutet, dass der Anteil roter Blutkörperchen am Gesamtblut "
                        "verringert ist. Betroffene berichten unter Umständen über Müdigkeit, Belastungsdyspnoe oder Schwindel, "
                        "manchmal fehlen Beschwerden jedoch völlig – insbesondere, wenn der Wert langsam abgesunken ist. "
                        "Längerfristiger Blutverlust, Ernährungsprobleme oder chronische Erkrankungen kommen als Ursachen in Frage, "
                        "müssen aber im Einzelfall sorgfältig geprüft werden.</p>"
                        "<p>Ein <strong>erhöhter Hämatokrit</strong> deutet darauf hin, dass das Blut relativ konzentrierter ist. "
                        "Dies kann bei Flüssigkeitsmangel, Rauchen, Aufenthalt in großer Höhe oder – deutlich seltener – bei "
                        "Bestandserkrankungen des Knochenmarks vorkommen. Erhöhte Werte veranlassen Ärztinnen und Ärzte dazu, "
                        "Kreislauf, Herz‑ und Lungenfunktion, Trinkmenge und eingenommene Medikamente genauer anzuschauen. "
                        "Besprechen Sie Ihren Befund immer mit dem Arzt; unser <a href=\"/de/blog/blutwerte-lesen\">Ratgeber zum "
                        "Lesen von Blutwerten</a> kann Sie auf das Gespräch vorbereiten.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Hinweis",
                    body_html=(
                        "<p><strong>Die Informationen in diesem Artikel ersetzen keine ärztliche Diagnose oder Behandlung.</strong> "
                        "Ein einzelner Hämatokrit‑Wert – ob hoch oder niedrig – genügt nicht, um eine Erkrankung sicher zu "
                        "bestätigen oder auszuschließen. Die Einordnung erfolgt immer im Zusammenhang mit Ihrer Anamnese, "
                        "Untersuchung und weiteren Befunden.</p>"
                        "<p>Wenn Sie Ihre Laborwerte in klarer Sprache und strukturiert erläutert bekommen möchten, können Sie "
                        "unser <a href=\"/analyze\">Analyse</a>‑Angebot nutzen und sich auf der Seite <a href=\"/de/pricing\">Preise</a> "
                        "informieren. Dieses Angebot soll das Gespräch mit Ihrer behandelnden Ärztin oder Ihrem Arzt unterstützen, "
                        "nicht ersetzen.</p>"
                    ),
                ),
            ],
            "fr": [
                Section(
                    id="quest-ce-hematocrite",
                    level=2,
                    heading="Qu'est-ce que l'hématocrite ?",
                    body_html=(
                        "<p>L’<strong>hématocrite</strong> correspond à la proportion du volume sanguin occupée par les globules rouges. "
                        "C’est un paramètre de base de la numération formule sanguine (NFS) qui donne une idée du caractère plus "
                        "ou moins concentré du sang. Pris isolément, il ne permet pas de conclure sur une maladie précise.</p>"
                        "<p>Les valeurs de référence varient selon les laboratoires, l’âge, le sexe biologique et les méthodes de "
                        "mesure. Il est donc important de s’appuyer sur l’intervalle « normal » indiqué sur votre propre compte‑rendu. "
                        "Le médecin interprète l’hématocrite en même temps que les autres chiffres de la NFS, vos symptômes, vos "
                        "antécédents et, si besoin, d’autres examens.</p>"
                    ),
                ),
                Section(
                    id="haut-ou-bas",
                    level=2,
                    heading="Hématocrite haut ou bas",
                    body_html=(
                        "<p>Un <strong>hématocrite bas</strong> signifie que la part de globules rouges dans le sang est diminuée. "
                        "Cela peut s’accompagner de fatigue, d’essoufflement à l’effort, de vertiges ou de pâleur, mais certaines "
                        "personnes ne ressentent rien, notamment si la baisse est progressive. Des pertes de sang, des apports "
                        "insuffisants ou des maladies chroniques peuvent être en cause, mais un seul chiffre ne permet pas d’en "
                        "identifier la raison exacte.</p>"
                        "<p>Un <strong>hématocrite élevé</strong> traduit un sang plus concentré. La déshydratation, le tabagisme, "
                        "la vie en altitude ou, plus rarement, des atteintes de la moelle osseuse peuvent participer à cette "
                        "augmentation. Face à ce type de résultat, le médecin s’intéresse au contexte global : tension artérielle, "
                        "fonction cardiaque et respiratoire, traitements en cours, autres analyses… Discutez toujours de vos "
                        "résultats avec un professionnel ; notre <a href=\"/fr/blog/lire-resultats-prise-de-sang\">guide pour "
                        "comprendre la prise de sang</a> peut vous aider à préparer vos questions.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Avertissement",
                    body_html=(
                        "<p><strong>Ce texte est fourni à titre informatif et ne remplace pas une consultation médicale.</strong> "
                        "Un hématocrite haut ou bas doit toujours être interprété dans le contexte de votre histoire personnelle, "
                        "de votre examen clinique et des autres résultats biologiques. Seul un professionnel de santé peut poser "
                        "un diagnostic.</p>"
                        "<p>Pour obtenir un résumé structuré et en langage clair de vos examens, vous pouvez utiliser notre page "
                        "<a href=\"/analyze\">Analyser</a> et consulter les offres sur <a href=\"/fr/pricing\">Tarifs</a>. "
                        "Ces outils complètent, mais ne remplacent pas, l’échange avec votre médecin.</p>"
                    ),
                ),
            ],
            "it": [
                Section(
                    id="cos-e-emocrito",
                    level=2,
                    heading="Cos'è l'ematocrito?",
                    body_html=(
                        "<p>L’<strong>ematocrito</strong> indica la percentuale del volume di sangue occupata dai globuli rossi. "
                        "È uno dei valori base dell’emocromo e aiuta a capire se il sangue appare più concentrato o più diluito. "
                        "Da solo non basta per dire se c’è o meno una malattia precisa.</p>"
                        "<p>I range di riferimento variano in base al laboratorio, all’età, al sesso biologico e alla metodica di "
                        "misura. Per questo è importante guardare sempre l’intervallo «normale» riportato sul tuo referto. Il medico "
                        "interpreta l’ematocrito assieme agli altri parametri dell’emocromo, ai sintomi, alla visita e, se serve, "
                        "ad esami aggiuntivi.</p>"
                    ),
                ),
                Section(
                    id="alto-o-basso",
                    level=2,
                    heading="Ematocrito alto o basso",
                    body_html=(
                        "<p>Un <strong>ematocrito basso</strong> segnala che la quota di globuli rossi nel sangue è ridotta. "
                        "Questo può tradursi in stanchezza, fiato corto sotto sforzo, capogiri o pallore, ma quando la variazione "
                        "è lenta molte persone non avvertono disturbi evidenti. Perdite di sangue protratte, difficoltà nella "
                        "produzione delle cellule rosse o malattie croniche possono contribuire al quadro, ma un singolo numero "
                        "non permette di definire la causa.</p>"
                        "<p>Un <strong>ematocrito alto</strong> suggerisce invece un sangue relativamente più concentrato. "
                        "Può vedersi in caso di disidratazione, fumo, permanenza ad alta quota o, meno spesso, in presenza di "
                        "patologie del midollo osseo. In queste situazioni il medico valuta con attenzione la pressione, lo stato "
                        "di idratazione, la funzione di cuore e polmoni e le terapie in corso. Discuti sempre il risultato con il "
                        "tuo curante; la nostra <a href=\"/it/blog/come-leggere-esami-del-sangue\">guida per capire gli esami del "
                        "sangue</a> può aiutarti a preparare la visita.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Disclaimer",
                    body_html=(
                        "<p><strong>Queste informazioni hanno solo scopo informativo e non sostituiscono una valutazione medica "
                        "personale.</strong> Un ematocrito alto o basso va sempre interpretato nel contesto della tua storia "
                        "clinica, dell’esame obiettivo e degli altri esami di laboratorio. Solo il medico può confermare o escludere "
                        "una diagnosi.</p>"
                        "<p>Per rivedere il referto in modo strutturato e con un linguaggio semplice puoi utilizzare la pagina "
                        "<a href=\"/analyze\">Analisi</a> e consultare le opzioni su <a href=\"/it/pricing\">Prezzi</a>. "
                        "Si tratta di un supporto alla relazione con il tuo medico, non di un sostituto.</p>"
                    ),
                ),
            ],
            "he": [
                Section(
                    id="ma-hu-hematocrit",
                    level=2,
                    heading="מהו המטוקריט?",
                    body_html=(
                        "<p><strong>המטוקריט</strong> הוא האחוז מנפח הדם שמורכב מתאי דם אדומים. זהו אחד המדדים הבסיסיים "
                        "בספירת הדם המלאה (CBC) והוא נותן תמונה אם הדם נראה מרוכז יותר או מדולל יותר. מדד זה אינו אבחנה "
                        "בפני עצמו אלא נתון נוסף שהרופא משלב עם שאר הנתונים.</p>"
                        "<p>טווחי הייחוס משתנים בין מעבדות ותלויים בגיל, במין הביולוגי ובשיטת המדידה. לכן חשוב להסתכל תמיד "
                        "על הטווח שמודפס בדוח האישי שלך. הרופא מפרש את ערך ההמטוקריט יחד עם שאר מדדי ספירת הדם, הסימפטומים, "
                        "הבדיקה הגופנית ולעיתים גם בדיקות נוספות.</p>"
                    ),
                ),
                Section(
                    id="gavoha-o-namuch",
                    level=2,
                    heading="המטוקריט גבוה או נמוך",
                    body_html=(
                        "<p><strong>המטוקריט נמוך</strong> פירושו שחלקן של תאי הדם האדומים בנפח הדם קטן מהמצופה. "
                        "לעיתים זה מתבטא בעייפות, ירידה בסבולת המאמץ, קוצר נשימה במאמץ או סחרחורת, אך כאשר השינוי איטי "
                        "ייתכן שלא יופיעו תסמינים ברורים. מצבים של אובדן דם ממושך, תזונה לא מספקת או מחלות כרוניות יכולים "
                        "להשפיע, אבל ערך יחיד אינו מסביר לבדו מהי הסיבה.</p>"
                        "<p><strong>המטוקריט גבוה</strong> מצביע על דם מרוכז יותר. זה יכול להופיע במצבי התייבשות, אצל "
                        "מעשנים, במגורים בגובה רב או במקרים נדירים יותר במחלות של מח העצם. במצב כזה הרופא בודק גם לחץ דם, "
                        "מאזן נוזלים, מצב לב וריאות והתרופות הקבועות. יש לדון בתוצאה עם הרופא; ניתן להיעזר ב"
                        "<a href=\"/he/blog/how-to-read-blood-test\">מדריך להבנת תוצאות בדיקת הדם</a> כהכנה לפגישה.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="הודעה",
                    body_html=(
                        "<p><strong>המידע במאמר זה מיועד להסברה בלבד ואינו מחליף ייעוץ או אבחנה רפואית אישית.</strong> "
                        "ערכים גבוהים או נמוכים של המטוקריט דורשים פרשנות בהקשר של הסיפור הרפואי המלא, הבדיקה הגופנית "
                        "ושאר הבדיקות. רק איש מקצוע המכיר אותך יכול לקבוע אבחנה.</p>"
                        "<p>אם ברצונך לסקור את בדיקת הדם בשפה ברורה ובאופן מובנה, ניתן להשתמש בכלי ה‑"
                        "<a href=\"/analyze\">Analyse</a> של השירות ולבדוק אפשרויות בדף <a href=\"/he/pricing\">מחירים</a>. "
                        "הכלי נועד להוסיף בהירות לשיחה עם הרופא – לא להחליף אותה.</p>"
                    ),
                ),
            ],
            "hi": [
                Section(
                    id="hematocrit-kya-hai",
                    level=2,
                    heading="हीमाटोक्रिट क्या है?",
                    body_html=(
                        "<p><strong>हीमाटोक्रिट</strong> यह बताता है कि आपके खून के कुल वॉल्यूम का कितना हिस्सा लाल रक्त कोशिकाओं "
                        "से बना है। यह CBC (complete blood count) की बेसिक वैल्यू में से एक है और यह दिखाता है कि खून अपेक्षाकृत "
                        "गाढ़ा है या ज़्यादा पतला। अकेले हीमाटोक्रिट से किसी बीमारी का नाम तय नहीं किया जा सकता।</p>"
                        "<p>हर लैब का रेफरेंस रेंज थोड़ा अलग हो सकता है और उम्र, जैविक लिंग तथा मशीन पर निर्भर करता है। "
                        "इसलिए हमेशा अपने रिपोर्ट पर लिखे \"नॉर्मल\" रेंज को ही आधार मानें। डॉक्टर हीमाटोक्रिट को बाकी CBC "
                        "वैल्यू, आपकी कहानी, दवाओं और ज़रूरत पड़ने पर अन्य जांचों के साथ जोड़कर देखते हैं।</p>"
                    ),
                ),
                Section(
                    id="high-ya-low",
                    level=2,
                    heading="हीमाटोक्रिट हाई या लो होने पर",
                    body_html=(
                        "<p><strong>लो हीमाटोक्रिट</strong> का मतलब होता है कि खून में लाल कोशिकाओं की हिस्सेदारी कम है। "
                        "ऐसी स्थिति में थकान, सीढ़ियाँ चढ़ते समय सांस फूलना, चक्कर जैसा लगना या चेहरा फीका दिखना महसूस हो "
                        "सकता है, लेकिन अगर गिरावट धीरे‑धीरे हो तो कई लोगों को शुरुआती समय में कोई खास लक्षण नहीं होते। "
                        "लंबे समय से चल रही खून की कमी, कुछ पुरानी बीमारियाँ या पोषण संबंधी कारण पृष्ठभूमि में हो सकते हैं, "
                        "पर एक रिपोर्ट से कारण तय नहीं किया जा सकता।</p>"
                        "<p><strong>हाई हीमाटोक्रिट</strong> यह संकेत देता है कि खून अपेक्षाकृत ज़्यादा गाढ़ा है। कम पानी पीना, "
                        "ज़्यादा पसीना या उल्टी‑दस्त से फ्लूड लॉस, ऊँचाई वाली जगह पर रहना या धूम्रपान जैसे कारण इससे जुड़े "
                        "हो सकते हैं; कभी‑कभी बोन मैरो से संबंधित स्थितियाँ भी भूमिका निभाती हैं। ऐसे परिणाम में डॉक्टर "
                        "ब्लड प्रेशर, हार्ट और लंग फंक्शन, दवाओं और समग्र स्थिति को साथ में देखते हैं। विजिट से पहले "
                        "<a href=\"/hi/blog/blood-test-kaise-padhe\">ब्लड टेस्ट समझने की गाइड</a> पढ़ना आपके सवाल तैयार करने में "
                        "मदद कर सकता है।</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="अस्वीकरण",
                    body_html=(
                        "<p><strong>यह जानकारी केवल शिक्षा के उद्देश्य से है; यह व्यक्तिगत चिकित्सीय सलाह या निदान नहीं है।</strong> "
                        "हीमाटोक्रिट का हाई या लो होना अकेले किसी निष्कर्ष के लिए पर्याप्त नहीं होता। अंतिम निर्णय डॉक्टर "
                        "आपके लक्षण, जांच और मेडिकल इतिहास को जोड़कर लेते हैं।</p>"
                        "<p>अगर आप अपने लैब रिज़ल्ट को सरल भाषा में और ढाँचे के साथ देखना चाहें तो हमारा "
                        "<a href=\"/analyze\">विश्लेषण</a> टूल और <a href=\"/hi/pricing\">मूल्य निर्धारण</a> पेज देख सकते हैं। "
                        "ये टूल डॉक्टर से होने वाली बातचीत को सपोर्ट करते हैं, उसकी जगह नहीं लेते।</p>"
                    ),
                ),
            ],
            "ar": [
                Section(
                    id="ma-hu-al-haymatukrit",
                    level=2,
                    heading="ما هو الهيماتوكريت؟",
                    body_html=(
                        "<p><strong>الهيماتوكريت</strong> هو النسبة المئوية من حجم الدم التي تشغلها كريات الدم الحمراء. "
                        "يظهر هذا الرقم في تحليل الدم الشامل ويعطي انطباعاً أولياً عما إذا كان الدم أكثر تركيزاً أو أكثر "
                        "تمايعاً من المعتاد. هو مؤشر مساعد ولا يقدّم وحده تشخيصاً كاملاً.</p>"
                        "<p>تختلف القيم المرجعية بين المختبرات بحسب العمر والجنس وطريقة القياس، لذلك ينبغي دائماً الاعتماد "
                        "على المجال «الطبيعي» المدوّن في تقريرك الشخصي. يقوم الطبيب بتفسير الهيماتوكريت إلى جانب باقي قيم "
                        "التحليل، والأعراض، والفحص السريري، وأحياناً فحوصات إضافية عند الحاجة.</p>"
                    ),
                ),
                Section(
                    id="murtafi-aw-munkhafid",
                    level=2,
                    heading="الهيماتوكريت مرتفع أو منخفض",
                    body_html=(
                        "<p><strong>الهيماتوكريت المنخفض</strong> يعني أن حصة الكريات الحمراء من حجم الدم أقل من المتوقع. "
                        "قد يرافقه تعب، ضيق نفس مع الجهد، دوار أو شحوب، لكن في الحالات البطيئة التطور قد لا يلاحظ الشخص "
                        "أي أعراض واضحة في البداية. يمكن أن تتداخل عوامل مثل نقص الوارد الغذائي، فقدان الدم المزمن أو "
                        "أمراض طويلة الأمد، إلا أن قيمة واحدة لا تكفي لمعرفة السبب بدقة.</p>"
                        "<p><strong>الهيماتوكريت المرتفع</strong> يشير إلى دم أكثر تركيزاً. قد يُرى مع الجفاف، أو عند المدخنين، "
                        "أو لدى من يعيشون في المرتفعات، وأحياناً – بشكل أقل شيوعاً – في أمراض تصيب نخاع العظم. في مثل هذه "
                        "الحالات يقيّم الطبيب ضغط الدم، وحالة السوائل، ووظيفة القلب والرئتين، والأدوية المستخدمة قبل أن يقرر "
                        "إن كانت هناك حاجة إلى فحوص إضافية. ناقش نتيجتك دائماً مع الطبيب؛ ويمكنك استخدام "
                        "<a href=\"/ar/blog/how-to-read-blood-test\">دليل فهم تحليل الدم</a> للتحضير للزيارة.</p>"
                    ),
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="إخلاء المسؤولية",
                    body_html=(
                        "<p><strong>هذه المعلومات لأغراض التثقيف فقط ولا تغني عن استشارة طبية شخصية.</strong> "
                        "ارتفاع أو انخفاض الهيماتوكريت يجب أن يُفسر دوماً ضمن سياق التاريخ المرضي والفحص السريري وبقية "
                        "التحاليل. وحده الطبيب الذي يعرف حالتك يمكنه تأكيد أو نفي التشخيص.</p>"
                        "<p>للحصول على عرض منظم وبلغة مبسّطة لنتائجك يمكنك استخدام صفحة <a href=\"/analyze\">التحليل</a> "
                        "والاطلاع على الخيارات المتاحة في صفحة <a href=\"/ar/pricing\">الأسعار</a>. هذه الأدوات مكمّلة "
                        "للحوار مع طبيبك وليست بديلاً عنه.</p>"
                    ),
                ),
            ],
        },
        icon="/static/images/blog/icons/hematocrit-high-or-low.svg",
    )


_ARTICLE_HEMATOCRIT_HIGH_LOW = _article_hematocrit_high_low()


def _article_mch_high_low() -> Article:
    """MCH high or low — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/mch-high-or-low-hero.png"
    slugs = {l: "mch-high-or-low" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "MCH yüksek veya düşük ne anlama gelir?", "en": "MCH high or low: what it means", "es": "MCH alto o bajo: qué significa", "de": "MCH zu hoch oder zu niedrig", "fr": "MCH haut ou bas : qu'est-ce que ça indique ?", "it": "MCH alto o basso: cosa significa?", "he": "MCH גבוה או נמוך: מה המשמעות?", "hi": "MCH हाई या लो का क्या मतलब?", "ar": "MCH مرتفع أو منخفض: ماذا يعني؟"}
    subs = {"tr": "MCH, bir kırmızı kan hücresindeki ortalama hemoglobin miktarını gösterir; yüksek veya düşük çıkması anemi tiplerinin ayrımında ipucu verir ama tek başına teşhis değildir.", "en": "MCH is the average amount of hemoglobin per red blood cell; high or low is not a diagnosis on its own and needs to be read together with other CBC indices.", "es": "MCH es la cantidad media de hemoglobina por glóbulo rojo; un valor alto o bajo orienta sobre el tipo de anemia, pero por sí solo no da el diagnóstico.", "de": "MCH ist die durchschnittliche Hämoglobinmenge pro Erythrozyt; ein zu hoher oder zu niedriger Wert gibt Hinweise auf Anämieformen, ist aber für sich allein keine Diagnose.", "fr": "Le MCH est la quantité moyenne d'hémoglobine par globule rouge ; un taux haut ou bas oriente sur le type d'anémie mais ne suffit pas à poser un diagnostic.", "it": "L'MCH è la quantità media di emoglobina per globulo rosso; un valore alto o basso può orientare sul tipo di anemia ma da solo non basta per una diagnosi.", "he": "MCH הוא כמות ההמוגלובין הממוצעת בכל כדורית אדומה; ערך גבוה או נמוך נותן רמז לסוג האנמיה אך לבדו אינו אבחנה.", "hi": "MCH एक लाल रक्त कोशिका में औसत हीमोग्लोबिन मात्रा दिखाता है; हाई या लो मान एनीमिया tipine dair ipucu verir ama अकेले निदान नहीं करता।", "ar": "MCH هو متوسط كمية الهيموغلوبين في كل خلية دم حمراء؛ الارتفاع أو الانخفاض قد يعطي فكرة عن نوع فقر الدم لكنه وحده لا يكفي للتشخيص."}
    ex = {"tr": "MCH CBC'de yer alır; anemi tiplerinin ayrımında hekim diğer indekslerle birlikte yorumlar.", "en": "MCH appears on a CBC; your doctor interprets it with other indices when distinguishing types of anemia.", "es": "MCH aparece en el hemograma; el médico lo interpreta con otros índices al distinguir tipos de anemia.", "de": "MCH gehört zum Blutbild; der Arzt wertet es mit anderen Indizes bei Anämieformen aus.", "fr": "Le MCH figure sur la NFS ; le médecin l'interprète avec les autres indices pour distinguer les anémies.", "it": "L'MCH compare nell'emocromo; il medico lo valuta con altri indici per i tipi di anemia.", "he": "MCH מופיע בספירת הדם; הרופא יפרש עם מדדים אחרים להבחנת סוגי אנמיה.", "hi": "MCH CBC में आता है; डॉक्टर एनीमिया के प्रकार बताने के लिए दूसरे इंडेक्स के साथ देखेंगे।", "ar": "MCH يظهر في تحليل الدم؛ الطبيب يفسره مع مؤشرات أخرى لتمييز أنواع فقر الدم."}
    seo_t = {"tr": "MCH Yüksek veya Düşük Ne Anlama Gelir? | Norya Blog", "en": "MCH High or Low: What It Means | Norya Blog", "es": "MCH alto o bajo | Norya Blog", "de": "MCH zu hoch oder zu niedrig | Norya Blog", "fr": "MCH haut ou bas | Norya Blog", "it": "MCH alto o basso | Norya Blog", "he": "MCH גבוה או נמוך | Norya Blog", "hi": "MCH हाई या लो | Norya Blog", "ar": "MCH مرتفع أو منخفض | Norya Blog"}
    seo_d = {"tr": "MCH yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What MCH high or low means. For information only.", "es": "MCH alto o bajo: causas. Solo informativo.", "de": "MCH zu hoch oder zu niedrig. Nur zur Information.", "fr": "MCH haut ou bas. À titre informatif.", "it": "MCH alto o basso. Solo informativo.", "he": "MCH גבוה או נמוך. למידע בלבד.", "hi": "MCH हाई या लो. केवल सूचनार्थ।", "ar": "MCH مرتفع أو منخفض. لأغراض إعلامية فقط."}
    sec = {}
    for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar"):
        c = "<p><strong>MCH</strong> (mean corpuscular hemoglobin) bir kırmızı kan hücresinde ortalama hemoglobin miktarını gösterir; CBC'de hemoglobin ve MCV ile birlikte anemi tiplerinin değerlendirilmesinde kullanılır. Tek başına teşhis koymaz; hekiminiz diğer indekslerle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>" if lang == "tr" else "<p><strong>MCH</strong> (mean corpuscular hemoglobin) is the average amount of hemoglobin per red blood cell; it is used with hemoglobin and MCV on a CBC to assess types of anemia. A single value does not make a diagnosis; your doctor interprets it with other indices. Discuss your result with a doctor.</p>" if lang == "en" else "<p><strong>MCH</strong> indica la cantidad media de hemoglobina por glóbulo rojo; se usa con hemoglobina y VCM en el hemograma para valorar tipos de anemia. Un valor aislado no da el diagnóstico; el médico lo interpreta con otros índices. Comenta el resultado con un médico.</p>" if lang == "es" else "<p><strong>MCH</strong> (mittleres korpuskuläres Hämoglobin) ist die durchschnittliche Hämoglobinmenge pro Erythrozyt; es wird im Blutbild mit Hämoglobin und MCV bei Anämieformen beurteilt. Ein Wert allein ergibt keine Diagnose; Ihr Arzt ordnet ihn mit anderen Indizes ein. Befund mit dem Arzt besprechen.</p>" if lang == "de" else "<p>Le <strong>MCH</strong> (contenu corpusculaire moyen en hémoglobine) est la quantité moyenne d'hémoglobine par globule rouge ; il est utilisé avec l'hémoglobine et le VGM sur la NFS pour évaluer les anémies. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec les autres indices. Discutez du résultat avec un médecin.</p>" if lang == "fr" else "<p>L'<strong>MCH</strong> (contenuto emoglobinico corpuscolare medio) è la quantità media di emoglobina per globulo rosso; si usa con emoglobina e MCV nell'emocromo per valutare i tipi di anemia. Un solo valore non fa diagnosi; il medico lo inquadra con altri indici. Discuti il risultato con il medico.</p>" if lang == "it" else "<p><strong>MCH</strong> (ממוצע המוגלובין לכדורית) הוא כמות ההמוגלובין הממוצעת לכדורית אדומה; משמש עם המוגלובין ו-MCV בספירת הדם להערכת סוגי אנמיה. ערך בודד לא קובע אבחנה; הרופא יפרש עם מדדים אחרים. יש לדון בתוצאה עם רופא.</p>" if lang == "he" else "<p><strong>MCH</strong> एक लाल रक्त कोशिका में औसत हीमोग्लोबिन है; CBC में हीमोग्लोबिन और MCV के साथ एनीमिया के प्रकार देखने में इस्तेमाल होता है। अकेला वैल्यू निदान नहीं; डॉक्टर दूसरे इंडेक्स के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>" if lang == "hi" else "<p><strong>MCH</strong> هو متوسط كمية الهيموغلوبين في كرية حمراء؛ يُستخدم مع الهيموغلوبين وحجم الكرية الوسطي في تحليل الدم لتقييم أنواع فقر الدم. رقم واحد لا يشخّص؛ الطبيب يفسره مع مؤشرات أخرى. ناقش نتيجتك مع الطبيب.</p>"
        d = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>" if lang == "tr" else "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>" if lang == "en" else "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>" if lang == "es" else "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>" if lang == "de" else "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>" if lang == "fr" else "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>" if lang == "it" else "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>" if lang == "he" else "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>" if lang == "hi" else "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"
        sec[lang] = [Section(id="content", level=2, heading=titles[lang], body_html=c), Section(id="disclaimer", level=2, heading="Uyarı" if lang == "tr" else "Disclaimer" if lang == "en" else "Aviso" if lang == "es" else "Hinweis" if lang == "de" else "Avertissement" if lang == "fr" else "Disclaimer" if lang == "it" else "הודעה" if lang == "he" else "अस्वीकरण" if lang == "hi" else "إخلاء المسؤولية", body_html=d)]
    return Article(id="mch-high-or-low", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subs, excerpts=ex, seo_titles=seo_t, seo_descriptions=seo_d, sections_by_lang=sec, icon="/static/images/blog/icons/mch-high-or-low.svg")


def _article_mchc_low() -> Article:
    """MCHC low meaning — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/mchc-low-meaning-hero.png"
    slugs = {l: "mchc-low-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "MCHC düşük ne anlama gelir?", "en": "What does low MCHC mean?", "es": "MCHC bajo: ¿qué significa?", "de": "MCHC zu niedrig: Was bedeutet das?", "fr": "MCHC bas : qu'est-ce que ça indique ?", "it": "MCHC basso: cosa significa?", "he": "מה המשמעות של MCHC נמוך?", "hi": "MCHC लो का क्या मतलब है?", "ar": "ماذا يعني انخفاض MCHC؟"}
    subs = {"tr": "MCHC, kırmızı kan hücresindeki hemoglobin yoğunluğunu gösterir; düşük çıkması genelde anemi ve hidrasyon durumu hakkında ipucu verir ama tek başına teşhis anlamına gelmez.", "en": "MCHC reflects the concentration of hemoglobin inside red blood cells; a low result often relates to anemia or hydration status but is not a diagnosis on its own.", "es": "MCHC refleja la concentración de hemoglobina dentro de los glóbulos rojos; un valor bajo suele relacionarse con anemia o hidratación, pero por sí solo no equivale a un diagnóstico.", "de": "MCHC gibt die Hämoglobinkonzentration in den Erythrozyten an; ein erniedrigter Wert weist häufig auf Anämie oder Flüssigkeitshaushalt hin, ist jedoch allein keine Diagnose.", "fr": "Le MCHC reflète la concentration d'hémoglobine dans les globules rouges ; un taux bas évoque souvent une anémie ou un problème d'hydratation, sans suffire à poser un diagnostic.", "it": "L'MCHC riflette la concentrazione di emoglobina nei globuli rossi; un valore basso si associa spesso ad anemia o stato di idratazione, ma da solo non basta per una diagnosi.", "he": "MCHC משקף את ריכוז ההמוגלובין בתוך כדוריות הדם האדומות; ערך נמוך עשוי לרמוז על אנמיה או מצב נוזלים אך לבדו אינו אבחנה.", "hi": "MCHC लाल रक्त कोशिकाओं के अंदर हीमोग्लोबिन की सघनता दिखाता है; लो परिणाम अक्सर एनीमिया या हाइड्रेशन से जुड़ सकता है लेकिन अकेले निदान नहीं होता।", "ar": "MCHC يعكس تركيز الهيموغلوبين داخل كريات الدم الحمراء؛ انخفاضه يرتبط كثيراً بفقر الدم أو حالة السوائل لكنه وحده لا يضع تشخيصاً."}
    ex = {"tr": "MCHC düşüklüğü genelde anemi veya hidrasyonla ilişkilidir; hekim diğer CBC değerleriyle yorumlar.", "en": "Low MCHC is often related to anemia or hydration; your doctor interprets it with other CBC values.", "es": "MCHC bajo suele relacionarse con anemia o hidratación; el médico lo interpreta con el resto del hemograma.", "de": "Niedriges MCHC hängt oft mit Anämie oder Flüssigkeitshaushalt zusammen; der Arzt wertet mit dem übrigen Blutbild.", "fr": "Un MCHC bas est souvent lié à l'anémie ou à l'hydratation ; le médecin l'interprète avec le reste de la NFS.", "it": "MCHC basso è spesso legato ad anemia o idratazione; il medico lo valuta con il resto dell'emocromo.", "he": "MCHC נמוך קשור לעיתים לאנמיה או לאיזון נוזלים; הרופא יפרש עם שאר ספירת הדם.", "hi": "MCHC लो अक्सर एनीमिया या हाइड्रेशन से जुड़ा; डॉक्टर बाकी CBC के साथ व्याख्या करेंगे।", "ar": "انخفاض MCHC غالباً مرتبط بفقر الدم أو السوائل؛ الطبيب يفسره مع بقية تحليل الدم."}
    seo_t = {"tr": "MCHC Düşüklüğü Ne Anlama Gelir? | Norya Blog", "en": "What Does Low MCHC Mean? | Norya Blog", "es": "MCHC bajo | Norya Blog", "de": "MCHC zu niedrig | Norya Blog", "fr": "MCHC bas | Norya Blog", "it": "MCHC basso | Norya Blog", "he": "MCHC נמוך | Norya Blog", "hi": "MCHC लो | Norya Blog", "ar": "انخفاض MCHC | Norya Blog"}
    seo_d = {"tr": "MCHC düşüklüğü nedenleri. Bilgilendirme amaçlı.", "en": "Causes of low MCHC. For information only.", "es": "MCHC bajo: causas. Solo informativo.", "de": "Ursachen für niedriges MCHC. Nur zur Information.", "fr": "MCHC bas : causes. À titre informatif.", "it": "MCHC basso: cause. Solo informativo.", "he": "סיבות ל-MCHC נמוך. למידע בלבד.", "hi": "MCHC लो के कारण. केवल सूचनार्थ।", "ar": "أسباب انخفاض MCHC. لأغراض إعلامية فقط."}
    sec = {}
    for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar"):
        c = "<p><strong>MCHC</strong> (mean corpuscular hemoglobin concentration) bir kırmızı kan hücresindeki hemoglobin yoğunluğunu gösterir; düşük MCHC genelde demir eksikliği anemisi veya hidrasyonla ilişkili olabilir. Tek başına teşhis koymaz; hekiminiz hemoglobin, MCV ve MCH ile birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>" if lang == "tr" else "<p><strong>MCHC</strong> (mean corpuscular hemoglobin concentration) reflects how concentrated hemoglobin is inside red blood cells. Low MCHC is often seen with iron deficiency anemia or hydration issues. It does not make a diagnosis alone; your doctor interprets it with hemoglobin, MCV, and MCH. Discuss your result with a doctor.</p>" if lang == "en" else "<p><strong>MCHC</strong> refleja la concentración de hemoglobina en el glóbulo rojo. Un MCHC bajo suele verse en anemia ferropénica o en relación con la hidratación. No da el diagnóstico por sí solo; el médico lo interpreta con hemoglobina, VCM y MCH. Comenta el resultado con un médico.</p>" if lang == "es" else "<p><strong>MCHC</strong> gibt die Hämoglobinkonzentration in den Erythrozyten an. Niedriges MCHC tritt oft bei Eisenmangelanämie oder Flüssigkeitshaushalt auf. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Hämoglobin, MCV und MCH. Befund mit dem Arzt besprechen.</p>" if lang == "de" else "<p>Le <strong>MCHC</strong> reflète la concentration d'hémoglobine dans le globule rouge. Un MCHC bas s'observe souvent dans l'anémie ferriprive ou en lien avec l'hydratation. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec l'hémoglobine, le VGM et le MCH. Discutez du résultat avec un médecin.</p>" if lang == "fr" else "<p>L'<strong>MCHC</strong> riflette la concentrazione di emoglobina nel globulo rosso. Un MCHC basso si vede spesso nell'anemia sideropenica o in relazione all'idratazione. Un solo valore non fa diagnosi; il medico lo inquadra con emoglobina, MCV e MCH. Discuti il risultato con il medico.</p>" if lang == "it" else "<p><strong>MCHC</strong> משקף את ריכוז ההמוגלובין בכדורית האדומה. MCHC נמוך מופיע לעיתים באנמיה מחוסר ברזל או באיזון נוזלים. ערך בודד לא קובע אבחנה; הרופא יפרש עם המוגלובין, MCV ו-MCH. יש לדון בתוצאה עם רופא.</p>" if lang == "he" else "<p><strong>MCHC</strong> लाल रक्त कोशिका में हीमोग्लोबिन की सघनता दिखाता है। लो MCHC अक्सर आयरन की कमी वाली एनीमिया या हाइड्रेशन से जुड़ा होता है। अकेले निदान नहीं; डॉक्टर हीमोग्लोबिन, MCV और MCH के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>" if lang == "hi" else "<p><strong>MCHC</strong> يعكس تركيز الهيموغلوبين في الكرية الحمراء. انخفاض MCHC يُرى غالباً في فقر الدم بعوز الحديد أو مع السوائل. الرقم وحده لا يشخّص؛ الطبيب يفسره مع الهيموغلوبين وحجم الكرية الوسطي وMCH. ناقش نتيجتك مع الطبيب.</p>"
        d = "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>" if lang == "tr" else "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>" if lang == "en" else "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>" if lang == "es" else "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>" if lang == "de" else "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>" if lang == "fr" else "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>" if lang == "it" else "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>" if lang == "he" else "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>" if lang == "hi" else "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"
        sec[lang] = [Section(id="content", level=2, heading=titles[lang], body_html=c), Section(id="disclaimer", level=2, heading="Uyarı" if lang == "tr" else "Disclaimer" if lang == "en" else "Aviso" if lang == "es" else "Hinweis" if lang == "de" else "Avertissement" if lang == "fr" else "Disclaimer" if lang == "it" else "הודעה" if lang == "he" else "अस्वीकरण" if lang == "hi" else "إخلاء المسؤولية", body_html=d)]
    return Article(id="mchc-low-meaning", published_at=published, read_minutes=4, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subs, excerpts=ex, seo_titles=seo_t, seo_descriptions=seo_d, sections_by_lang=sec, icon="/static/images/blog/icons/mchc-low-meaning.svg")


def _make_short_article(article_id: str, slug_key: str, published: date, cover: str, read_min: int, cat: dict, titles: dict, subs: dict, ex: dict, seo_t: dict, seo_d: dict, content_by_lang: dict, icon: Optional[str] = None) -> Article:
    """Helper: 9 dilde 2 bölüm (içerik + disclaimer) ile kısa makale."""
    slugs = {l: slug_key for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    disclaimers = {"tr": "Uyarı", "en": "Disclaimer", "es": "Aviso", "de": "Hinweis", "fr": "Avertissement", "it": "Disclaimer", "he": "הודעה", "hi": "अस्वीकरण", "ar": "إخلاء المسؤولية"}
    d_html = {"tr": "<p><strong>Bilgilendirme amaçlıdır.</strong> <a href=\"/analyze\">Analiz</a></p>", "en": "<p><strong>For information only.</strong> <a href=\"/analyze\">Analyze</a></p>", "es": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizar</a></p>", "de": "<p><strong>Nur zur Information.</strong> <a href=\"/analyze\">Analyse</a></p>", "fr": "<p><strong>À titre informatif.</strong> <a href=\"/analyze\">Analyser</a></p>", "it": "<p><strong>Solo informativo.</strong> <a href=\"/analyze\">Analizza</a></p>", "he": "<p><strong>למידע בלבד.</strong> <a href=\"/analyze\">התחל ניתוח</a></p>", "hi": "<p><strong>केवल सूचनार्थ।</strong> <a href=\"/analyze\">विश्लेषण शुरू करें</a></p>", "ar": "<p><strong>للمعلومات فقط.</strong> <a href=\"/analyze\">بدء التحليل</a></p>"}
    sec = {lang: [Section(id="content", level=2, heading=titles[lang], body_html=content_by_lang[lang]), Section(id="disclaimer", level=2, heading=disclaimers[lang], body_html=d_html[lang])] for lang in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    return Article(id=article_id, published_at=published, read_minutes=read_min, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subs, excerpts=ex, seo_titles=seo_t, seo_descriptions=seo_d, sections_by_lang=sec, icon=icon)


def _article_eosinophils_high() -> Article:
    """Eosinophils high meaning — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/eosinophils-high-meaning-hero.png"
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Eozinofil yüksekliği ne anlama gelir?", "en": "What does high eosinophils mean?", "es": "Eosinófilos altos: ¿qué significa?", "de": "Eosinophile erhöht: Was bedeutet das?", "fr": "Éosinophiles élevés : qu'est-ce que ça indique ?", "it": "Eosinofili alti: cosa significa?", "he": "מה המשמעות של אאוזינופילים גבוהים?", "hi": "ईोसिनोफिल्स हाई का क्या मतलब?", "ar": "ماذا يعني ارتفاع الحمضات؟"}
    subs = {"tr": "Eozinofiller beyaz kan hücrelerinin bir türüdür; yüksekliği tek başına teşhis değildir, hekim diğer sonuçlarla yorumlar.", "en": "Eosinophils are a type of white blood cell; a high count alone is not a diagnosis—your doctor interprets it with other results.", "es": "Los eosinófilos son un tipo de glóbulo blanco; un valor alto por sí solo no es un diagnóstico.", "de": "Eosinophile sind eine Art weißer Blutkörperchen; Erhöhung allein ist keine Diagnose.", "fr": "Les éosinophiles sont un type de globules blancs ; un taux élevé seul ne fait pas un diagnostic.", "it": "Gli eosinofili sono un tipo di globuli bianchi; un valore alto da solo non è una diagnosi.", "he": "אאוזינופילים הם סוג של תאי דם לבנים; ערך גבוה לבדו אינו אבחנה.", "hi": "ईोसिनोफिल्स सफेद रक्त कोशिका का एक प्रकार हैं; हाई अकेले निदान नहीं।", "ar": "الحمضات نوع من خلايا الدم البيضاء؛ ارتفاعها وحده ليس تشخيصاً."}
    ex = {"tr": "Eozinofil yüksekliği alerji, parazit veya ilaçla ilişkili olabilir; hekim tam kan sayımı ve öyküyle değerlendirir.", "en": "High eosinophils can be related to allergy, parasites, or medication; your doctor assesses with full blood count and history.", "es": "Eosinófilos altos pueden relacionarse con alergia, parásitos o medicación; el médico valora con hemograma e historia.", "de": "Erhöhte Eosinophile können mit Allergie, Parasiten oder Medikamenten zusammenhängen; der Arzt beurteilt mit Blutbild und Anamnese.", "fr": "Des éosinophiles élevés peuvent être liés à l'allergie, aux parasites ou aux médicaments ; le médecin évalue avec la NFS et l'anamnèse.", "it": "Eosinofili alti possono essere legati ad allergia, parassiti o farmaci; il medico valuta con emocromo e anamnesi.", "he": "אאוזינופילים גבוהים יכולים להיות קשורים לאלרגיה, טפילים או תרופות; הרופא יבדוק עם ספירת דם מלאה וההיסטוריה.", "hi": "ईोसिनोफिल्स हाई एलर्जी, पैरासाइट या दवा से जुड़ सकते हैं; डॉक्टर पूर्ण रक्त और इतिहास से आंकलन करेंगे।", "ar": "ارتفاع الحمضات قد يرتبط بالحساسية أو الطفيليات أو الأدوية؛ الطبيب يقيّم مع تحليل الدم والتاريخ."}
    seo_t = {"tr": "Eozinofil Yüksekliği Ne Anlama Gelir? | Norya Blog", "en": "What Does High Eosinophils Mean? | Norya Blog", "es": "Eosinófilos altos | Norya Blog", "de": "Eosinophile erhöht | Norya Blog", "fr": "Éosinophiles élevés | Norya Blog", "it": "Eosinofili alti | Norya Blog", "he": "אאוזינופילים גבוהים | Norya Blog", "hi": "ईोसिनोफिल्स हाई | Norya Blog", "ar": "ارتفاع الحمضات | Norya Blog"}
    seo_d = {"tr": "Eozinofil yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Causes of high eosinophils. For information only.", "es": "Eosinófilos altos: causas. Solo informativo.", "de": "Ursachen für erhöhte Eosinophile. Nur zur Information.", "fr": "Éosinophiles élevés : causes. À titre informatif.", "it": "Eosinofili alti: cause. Solo informativo.", "he": "סיבות לאאוזינופילים גבוהים. למידע בלבד.", "hi": "ईोसिनोफिल्स हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع الحمضات. لأغراض إعلامية فقط."}
    c = {"tr": "<p><strong>Eozinofiller</strong> beyaz kan hücrelerinin bir türüdür; alerji, parazit enfeksiyonları veya bazı ilaçlar sayıyı yükseltebilir. Yüksek eozinofil tek başına teşhis koymaz; hekiminiz tam kan sayımı ve klinik öyküyle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>Eosinophils</strong> are a type of white blood cell; allergy, parasitic infections, or some medications can raise the count. High eosinophils alone do not make a diagnosis; your doctor interprets them with the full blood count and clinical history. Discuss your result with a doctor.</p>", "es": "<p>Los <strong>eosinófilos</strong> son un tipo de glóbulo blanco; la alergia, infecciones parasitarias o algunos medicamentos pueden elevar el valor. Eosinófilos altos por sí solos no dan el diagnóstico; el médico los interpreta con el hemograma y la historia clínica. Comenta el resultado con un médico.</p>", "de": "<p><strong>Eosinophile</strong> sind eine Art weißer Blutkörperchen; Allergie, Parasiten oder manche Medikamente können den Wert erhöhen. Erhöhte Eosinophile allein ergeben keine Diagnose; der Arzt wertet mit dem Blutbild und der Anamnese. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Les <strong>éosinophiles</strong> sont un type de globules blancs ; l'allergie, les parasitoses ou certains médicaments peuvent les élever. Un taux élevé seul ne fait pas un diagnostic ; le médecin l'interprète avec la NFS et l'anamnèse. Discutez du résultat avec un médecin.</p>", "it": "<p>Gli <strong>eosinofili</strong> sono un tipo di globuli bianchi; allergia, parassiti o alcuni farmaci possono alzare il valore. Eosinofili alti da soli non fanno diagnosi; il medico li valuta con l'emocromo e l'anamnesi. Discuti il risultato con il medico.</p>", "he": "<p><strong>אאוזינופילים</strong> הם סוג של תאי דם לבנים; אלרגיה, זיהומי טפילים או תרופות מסוימות יכולים להעלות את הערך. אאוזינופילים גבוהים לבדם אינם קובעים אבחנה; הרופא יפרש עם ספירת הדם וההיסטוריה. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>ईोसिनोफिल्स</strong> सफेद रक्त कोशिका का एक प्रकार हैं; एलर्जी, पैरासाइट संक्रमण या कुछ दवाएं काउंट बढ़ा सकती हैं। हाई ईोसिनोफिल्स अकेले निदान नहीं; डॉक्टर पूर्ण रक्त और क्लिनिकल इतिहास के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>الحمضات</strong> نوع من خلايا الدم البيضاء؛ الحساسية أو الطفيليات أو بعض الأدوية قد ترفع العدد. ارتفاع الحمضات وحده لا يشخّص؛ الطبيب يفسره مع تحليل الدم والتاريخ السريري. ناقش نتيجتك مع الطبيب.</p>"}
    return _make_short_article("eosinophils-high-meaning", "eosinophils-high-meaning", published, cover, 4, cat, titles, subs, ex, seo_t, seo_d, c, icon="/static/images/blog/icons/eosinophils-high-meaning.svg")


def _article_basophils_high() -> Article:
    """Basophils high meaning — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/basophils-high-meaning-hero.png"
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Bazofil yüksekliği ne anlama gelir?", "en": "What does high basophils mean?", "es": "Basófilos altos: ¿qué significa?", "de": "Basophile erhöht: Was bedeutet das?", "fr": "Basophiles élevés : qu'est-ce que ça indique ?", "it": "Basofili alti: cosa significa?", "he": "מה המשמעות של בזופילים גבוהים?", "hi": "बेसोफिल्स हाई का क्या मतलब?", "ar": "ماذا يعني ارتفاع الخلايا القاعدية؟"}
    subs = {"tr": "Bazofiller nadir görülen beyaz kan hücreleridir; yüksekliği tek başına teşhis değildir.", "en": "Basophils are a rare type of white blood cell; a high count alone is not a diagnosis.", "es": "Los basófilos son un tipo raro de glóbulo blanco; un valor alto por sí solo no es un diagnóstico.", "de": "Basophile sind eine seltene Art weißer Blutkörperchen; Erhöhung allein ist keine Diagnose.", "fr": "Les basophiles sont un type rare de globules blancs ; un taux élevé seul ne fait pas un diagnostic.", "it": "I basofili sono un tipo raro di globuli bianchi; un valore alto da solo non è una diagnosi.", "he": "בזופילים הם סוג נדיר של תאי דם לבנים; ערך גבוה לבדו אינו אבחנה.", "hi": "बेसोफिल्स दुर्लभ सफेद रक्त कोशिका हैं; हाई अकेले निदान नहीं।", "ar": "الخلايا القاعدية نوع نادر من خلايا الدم البيضاء؛ ارتفاعها وحده ليس تشخيصاً."}
    ex = {"tr": "Bazofil yüksekliği nadirdir; hekim tam kan sayımı ve klinikle birlikte yorumlar.", "en": "High basophils are uncommon; your doctor interprets the count with the full blood count and clinical context.", "es": "Basófilos altos son poco frecuentes; el médico interpreta el valor con el hemograma y el contexto clínico.", "de": "Erhöhte Basophile sind selten; der Arzt wertet mit dem Blutbild und dem klinischen Kontext.", "fr": "Des basophiles élevés sont peu fréquents ; le médecin interprète avec la NFS et le contexte clinique.", "it": "Basofili alti sono rari; il medico valuta con l'emocromo e il contesto clinico.", "he": "בזופילים גבוהים נדירים; הרופא יפרש עם ספירת הדם וההקשר הקליני.", "hi": "बेसोफिल्स हाई कम होते हैं; डॉक्टर पूर्ण रक्त और क्लिनिकल संदर्भ के साथ व्याख्या करेंगे।", "ar": "ارتفاع الخلايا القاعدية غير شائع؛ الطبيب يفسر العدد مع تحليل الدم والسياق السريري."}
    seo_t = {"tr": "Bazofil Yüksekliği Ne Anlama Gelir? | Norya Blog", "en": "What Does High Basophils Mean? | Norya Blog", "es": "Basófilos altos | Norya Blog", "de": "Basophile erhöht | Norya Blog", "fr": "Basophiles élevés | Norya Blog", "it": "Basofili alti | Norya Blog", "he": "בזופילים גבוהים | Norya Blog", "hi": "बेसोफिल्स हाई | Norya Blog", "ar": "ارتفاع الخلايا القاعدية | Norya Blog"}
    seo_d = {"tr": "Bazofil yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Causes of high basophils. For information only.", "es": "Basófilos altos: causas. Solo informativo.", "de": "Ursachen für erhöhte Basophile. Nur zur Information.", "fr": "Basophiles élevés : causes. À titre informatif.", "it": "Basofili alti: cause. Solo informativo.", "he": "סיבות לבזופילים גבוהים. למידע בלבד.", "hi": "बेसोफिल्स हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع الخلايا القاعدية. لأغراض إعلامية فقط."}
    c = {"tr": "<p><strong>Bazofiller</strong> beyaz kan hücrelerinin en az görülen türlerinden biridir. Yüksek bazofil nadirdir; bazen alerji veya kronik iltihapla ilişkili olabilir. Tek başına teşhis koymaz; hekiminiz tam kan sayımı ve klinikle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>Basophils</strong> are one of the rarest white blood cell types. High basophils are uncommon; they can sometimes be related to allergy or chronic inflammation. They do not make a diagnosis alone; your doctor interprets them with the full blood count and clinical context. Discuss your result with a doctor.</p>", "es": "<p>Los <strong>basófilos</strong> son uno de los tipos de glóbulos blancos más raros. Basófilos altos son poco frecuentes; a veces pueden relacionarse con alergia o inflamación crónica. No dan el diagnóstico por sí solos; el médico los interpreta con el hemograma y el contexto clínico. Comenta el resultado con un médico.</p>", "de": "<p><strong>Basophile</strong> gehören zu den seltensten weißen Blutkörperchen. Erhöhte Basophile sind ungewöhnlich; sie können gelegentlich mit Allergie oder chronischer Entzündung zusammenhängen. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit dem Blutbild und dem klinischen Kontext. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Les <strong>basophiles</strong> sont l'un des types de globules blancs les plus rares. Un taux élevé est peu fréquent ; il peut parfois être lié à l'allergie ou à une inflammation chronique. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec la NFS et le contexte clinique. Discutez du résultat avec un médecin.</p>", "it": "<p>I <strong>basofili</strong> sono uno dei tipi di globuli bianchi più rari. Basofili alti sono rari; a volte possono essere legati ad allergia o infiammazione cronica. Un solo valore non fa diagnosi; il medico lo valuta con l'emocromo e il contesto clinico. Discuti il risultato con il medico.</p>", "he": "<p><strong>בזופילים</strong> הם מהתאים הלבנים הנדירים ביותר. בזופילים גבוהים נדירים; לעיתים יכולים להיות קשורים לאלרגיה או דלקת כרונית. ערך בודד לא קובע אבחנה; הרופא יפרש עם ספירת הדם וההקשר הקליני. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>बेसोफिल्स</strong> सफेद रक्त कोशिकाओं के सबसे दुर्लभ प्रकारों में से एक हैं। बेसोफिल्स हाई कम होते हैं; कभी-कभी एलर्जी या क्रॉनिक सूजन से जुड़े हो सकते हैं। अकेले निदान नहीं; डॉक्टर पूर्ण रक्त और क्लिनिकल संदर्भ के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>الخلايا القاعدية</strong> من أندر أنواع خلايا الدم البيضاء. ارتفاعها غير شائع؛ قد يرتبط أحياناً بالحساسية أو الالتهاب المزمن. الرقم وحده لا يشخّص؛ الطبيب يفسره مع تحليل الدم والسياق السريري. ناقش نتيجتك مع الطبيب.</p>"}
    return _make_short_article("basophils-high-meaning", "basophils-high-meaning", published, cover, 4, cat, titles, subs, ex, seo_t, seo_d, c, icon="/static/images/blog/icons/basophils-high-meaning.svg")


def _article_chloride_high_low() -> Article:
    """Chloride high or low — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/chloride-high-or-low-hero.png"
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "Klor yüksek veya düşük ne anlama gelir?", "en": "Chloride high or low: what it means", "es": "Cloro alto o bajo: qué significa", "de": "Chlorid zu hoch oder zu niedrig", "fr": "Chlore haut ou bas : qu'est-ce que ça indique ?", "it": "Cloro alto o basso: cosa significa?", "he": "כלוריד גבוה או נמוך: מה המשמעות?", "hi": "क्लोराइड हाई या लो का क्या मतलब?", "ar": "الكلوريد مرتفع أو منخفض: ماذا يعني؟"}
    subs = {"tr": "Klor kandaki başlıca elektrolitlerden biridir; yüksek veya düşük tek başına teşhis değildir.", "en": "Chloride is one of the main electrolytes in blood; high or low is not a diagnosis on its own.", "es": "El cloro es uno de los principales electrolitos en sangre; alto o bajo no es un diagnóstico por sí solo.", "de": "Chlorid ist einer der wichtigsten Blutelektrolyte; zu hoch oder zu niedrig ist keine Diagnose für sich.", "fr": "Le chlore est un des principaux électrolytes du sang ; haut ou bas seul ne fait pas un diagnostic.", "it": "Il cloro è uno dei principali elettroliti nel sangue; alto o basso da solo non è una diagnosi.", "he": "כלוריד הוא אחד האלקטרוליטים העיקריים בדם; גבוה או נמוך לבדו אינו אבחנה.", "hi": "क्लोराइड खून का एक मुख्य इलेक्ट्रोलाइट है; हाई या लो अकेले निदान नहीं।", "ar": "الكلوريد أحد أهم كهارل الدم؛ ارتفاع أو انخفاض وحده ليس تشخيصاً."}
    ex = {"tr": "Klor sıvı dengesi ve asit-baz ile ilişkilidir; hekim elektrolit paneli ve klinikle yorumlar.", "en": "Chloride is linked to fluid balance and acid-base status; your doctor interprets it with the electrolyte panel and clinical context.", "es": "El cloro se relaciona con el equilibrio de líquidos y el estado ácido-base; el médico lo interpreta con el panel de electrolitos.", "de": "Chlorid hängt mit Flüssigkeitshaushalt und Säure-Basen-Status zusammen; der Arzt wertet mit dem Elektrolytpanel.", "fr": "Le chlore est lié à l'équilibre hydrique et au statut acido-basique ; le médecin l'interprète avec le bilan électrolytique.", "it": "Il cloro è legato all'equilibrio idrico e allo stato acido-base; il medico lo valuta con il panel elettroliti.", "he": "כלוריד קשור לאיזון נוזלים ולמצב חומצה-בסיס; הרופא יפרש עם פאנל האלקטרוליטים.", "hi": "क्लोराइड फ्लूइड बैलेंस और एसिड-बेस से जुड़ा है; डॉक्टर इलेक्ट्रोलाइट पैनल और क्लिनिकल संदर्भ के साथ व्याख्या करेंगे।", "ar": "الكلوريد مرتبط بتوازن السوائل وحالة الحمض-القاعدة؛ الطبيب يفسره مع لوحة الكهارل."}
    seo_t = {"tr": "Klor Yüksek veya Düşük Ne Anlama Gelir? | Norya Blog", "en": "Chloride High or Low: What It Means | Norya Blog", "es": "Cloro alto o bajo | Norya Blog", "de": "Chlorid zu hoch oder zu niedrig | Norya Blog", "fr": "Chlore haut ou bas | Norya Blog", "it": "Cloro alto o basso | Norya Blog", "he": "כלוריד גבוה או נמוך | Norya Blog", "hi": "क्लोराइड हाई या लो | Norya Blog", "ar": "الكلوريد مرتفع أو منخفض | Norya Blog"}
    seo_d = {"tr": "Klor yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What chloride high or low means. For information only.", "es": "Cloro alto o bajo: causas. Solo informativo.", "de": "Chlorid zu hoch oder zu niedrig. Nur zur Information.", "fr": "Chlore haut ou bas. À titre informatif.", "it": "Cloro alto o basso. Solo informativo.", "he": "כלוריד גבוה או נמוך. למידע בלבד.", "hi": "क्लोराइड हाई या लो. केवल सूचनार्थ।", "ar": "الكلوريد مرتفع أو منخفض. لأغراض إعلامية فقط."}
    c = {"tr": "<p><strong>Klor</strong> (klorür) kandaki ana elektrolitlerden biridir; sıvı dengesi ve asit-baz dengesiyle ilişkilidir. Yüksek veya düşük çıkması dehidratasyon, böbrek veya solunum durumlarıyla ilişkili olabilir. Tek başına teşhis koymaz; hekiminiz sodyum, CO2 ve diğer elektrolitlerle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>Chloride</strong> is one of the main electrolytes in blood; it is linked to fluid balance and acid-base balance. High or low can be related to dehydration, kidney or respiratory conditions. It does not make a diagnosis alone; your doctor interprets it with sodium, CO2, and other electrolytes. Discuss your result with a doctor.</p>", "es": "<p>El <strong>cloro</strong> es uno de los principales electrolitos en sangre; se relaciona con el equilibrio de líquidos y ácido-base. Alto o bajo puede deberse a deshidratación, riñón o situación respiratoria. No da el diagnóstico por sí solo; el médico lo interpreta con sodio, CO2 y otros electrolitos. Comenta el resultado con un médico.</p>", "de": "<p><strong>Chlorid</strong> ist einer der Hauptelektrolyte im Blut; es hängt mit Flüssigkeits- und Säure-Basen-Haushalt zusammen. Zu hoch oder zu niedrig kann bei Dehydratation, Niere oder Atemwegserkrankung vorkommen. Ein Wert allein ergibt keine Diagnose; der Arzt wertet mit Natrium, CO2 und anderen Elektrolyten. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>chlore</strong> est un des principaux électrolytes du sang ; il est lié à l'équilibre hydrique et acido-basique. Un taux haut ou bas peut être lié à la déshydratation, au rein ou à la situation respiratoire. Un chiffre seul ne fait pas un diagnostic ; le médecin l'interprète avec le sodium, le CO2 et les autres électrolytes. Discutez du résultat avec un médecin.</p>", "it": "<p>Il <strong>cloro</strong> è uno dei principali elettroliti nel sangue; è legato all'equilibrio idrico e acido-base. Alto o basso può dipendere da disidratazione, rene o situazione respiratoria. Un solo valore non fa diagnosi; il medico lo inquadra con sodio, CO2 e altri elettroliti. Discuti il risultato con il medico.</p>", "he": "<p><strong>כלוריד</strong> הוא אחד האלקטרוליטים העיקריים בדם; קשור לאיזון נוזלים וחומצה-בסיס. גבוה או נמוך יכול להיות קשור להתייבשות, כליות או מצב נשימתי. ערך בודד לא קובע אבחנה; הרופא יפרש עם נתרן, CO2 ואלקטרוליטים אחרים. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>क्लोराइड</strong> खून में मुख्य इलेक्ट्रोलाइट में से एक है; फ्लूइड बैलेंस और एसिड-बेस से जुड़ा है। हाई या लो डिहाइड्रेशन, किडनी या रेस्पिरेटरी स्थिति से जुड़ सकता है। अकेले निदान नहीं; डॉक्टर सोडियम, CO2 और दूसरे इलेक्ट्रोलाइट्स के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>الكلوريد</strong> أحد أهم كهارل الدم؛ مرتبط بتوازن السوائل والحمض-القاعدة. ارتفاع أو انخفاض قد يكون بسبب الجفاف أو الكلى أو الحالة التنفسية. الرقم وحده لا يشخّص؛ الطبيب يفسره مع الصوديوم وCO2 وكهارل أخرى. ناقش نتيجتك مع الطبيب.</p>"}
    return _make_short_article("chloride-high-or-low", "chloride-high-or-low", published, cover, 4, cat, titles, subs, ex, seo_t, seo_d, c, icon="/static/images/blog/icons/chloride-high-or-low.svg")


def _article_co2_blood_test() -> Article:
    """CO2 blood test high or low — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/co2-blood-test-high-or-low-hero.png"
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "CO2 (bikarbonat) kan testi yüksek veya düşük ne anlama gelir?", "en": "CO2 blood test high or low: what it means", "es": "CO2 en sangre alto o bajo: qué significa", "de": "CO2 im Blut zu hoch oder zu niedrig", "fr": "CO2 sanguin haut ou bas : qu'est-ce que ça indique ?", "it": "CO2 nel sangue alto o basso: cosa significa?", "he": "CO2 בדם גבוה או נמוך: מה המשמעות?", "hi": "CO2 ब्लड टेस्ट हाई या लो का क्या मतलब?", "ar": "تحليل CO2 في الدم مرتفع أو منخفض: ماذا يعني؟"}
    subs = {"tr": "Kan CO2/bikarbonat asit-baz dengesini yansıtır; yüksek veya düşük tek başına teşhis değildir.", "en": "Blood CO2/bicarbonate reflects acid-base balance; high or low is not a diagnosis on its own.", "es": "El CO2/bicarbonato en sangre refleja el equilibrio ácido-base; alto o bajo no es un diagnóstico por sí solo.", "de": "CO2/Bikarbonat im Blut spiegelt den Säure-Basen-Haushalt wider; zu hoch oder zu niedrig ist keine Diagnose für sich.", "fr": "Le CO2/bicarbonate sanguin reflète l'équilibre acido-basique ; haut ou bas seul ne fait pas un diagnostic.", "it": "La CO2/bicarbonato nel sangue riflette l'equilibrio acido-base; alto o basso da solo non è una diagnosi.", "he": "CO2/ביקרבונט בדם משקף את איזון החומצה-בסיס; גבוה או נמוך לבדו אינו אבחנה.", "hi": "खून में CO2/बाइकार्बोनेट एसिड-बेस बैलेंस दिखाता है; हाई या लो अकेले निदान नहीं।", "ar": "CO2/البيكربونات في الدم يعكس توازن الحمض-القاعدة؛ ارتفاع أو انخفاض وحده ليس تشخيصاً."}
    ex = {"tr": "CO2/bikarbonat böbrek ve solunumla ilişkilidir; hekim elektrolit ve kan gazıyla yorumlar.", "en": "CO2/bicarbonate is linked to kidney and breathing; your doctor interprets it with electrolytes and context.", "es": "CO2/bicarbonato se relaciona con riñón y respiración; el médico lo interpreta con electrolitos y contexto.", "de": "CO2/Bikarbonat hängt mit Niere und Atmung zusammen; der Arzt wertet mit Elektrolyten und Kontext.", "fr": "Le CO2/bicarbonate est lié au rein et à la respiration ; le médecin l'interprète avec les électrolytes et le contexte.", "it": "La CO2/bicarbonato è legata a rene e respirazione; il medico la valuta con elettroliti e contesto.", "he": "CO2/ביקרבונט קשור לכליות ולנשימה; הרופא יפרש עם אלקטרוליטים והקשר.", "hi": "CO2/बाइकार्बोनेट किडनी और सांस से जुड़ा है; डॉक्टर इलेक्ट्रोलाइट्स और संदर्भ के साथ व्याख्या करेंगे।", "ar": "CO2/البيكربونات مرتبط بالكلية والتنفس؛ الطبيب يفسره مع الكهارل والسياق."}
    seo_t = {"tr": "CO2 Kan Testi Yüksek veya Düşük Ne Anlama Gelir? | Norya Blog", "en": "CO2 Blood Test High or Low: What It Means | Norya Blog", "es": "CO2 en sangre alto o bajo | Norya Blog", "de": "CO2 im Blut zu hoch oder zu niedrig | Norya Blog", "fr": "CO2 sanguin haut ou bas | Norya Blog", "it": "CO2 nel sangue alto o basso | Norya Blog", "he": "CO2 בדם גבוה או נמוך | Norya Blog", "hi": "CO2 ब्लड टेस्ट हाई या लो | Norya Blog", "ar": "تحليل CO2 في الدم | Norya Blog"}
    seo_d = {"tr": "CO2/bikarbonat yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What CO2 blood test high or low means. For information only.", "es": "CO2 en sangre alto o bajo. Solo informativo.", "de": "CO2 im Blut zu hoch oder zu niedrig. Nur zur Information.", "fr": "CO2 sanguin haut ou bas. À titre informatif.", "it": "CO2 nel sangue alto o basso. Solo informativo.", "he": "CO2 בדם גבוה או נמוך. למידע בלבד.", "hi": "CO2 ब्लड टेस्ट हाई या लो. केवल सूचनार्थ।", "ar": "تحليل CO2 في الدم. لأغراض إعلامية فقط."}
    c = {"tr": "<p>Kan <strong>CO2</strong> (veya bikarbonat) asit-baz dengesini yansıtır; böbrek ve solunumla ilişkilidir. Yüksek veya düşük çıkması tek başına teşhis değildir; hekiminiz elektrolit paneli ve anion gap ile birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p>Blood <strong>CO2</strong> (or bicarbonate) reflects acid-base balance; it is linked to kidney and breathing. High or low does not make a diagnosis alone; your doctor interprets it with the electrolyte panel and anion gap. Discuss your result with a doctor.</p>", "es": "<p>El <strong>CO2</strong> (o bicarbonato) en sangre refleja el equilibrio ácido-base; se relaciona con riñón y respiración. Alto o bajo no da el diagnóstico por sí solo; el médico lo interpreta con el panel de electrolitos y el anion gap. Comenta el resultado con un médico.</p>", "de": "<p>CO2 (oder Bikarbonat) im Blut spiegelt den Säure-Basen-Haushalt wider; es hängt mit Niere und Atmung zusammen. Zu hoch oder zu niedrig ergibt allein keine Diagnose; der Arzt wertet mit dem Elektrolytpanel und der Anionenlücke. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>CO2</strong> (ou bicarbonate) sanguin reflète l'équilibre acido-basique ; il est lié au rein et à la respiration. Un taux haut ou bas seul ne fait pas un diagnostic ; le médecin l'interprète avec le bilan électrolytique et le trou anionique. Discutez du résultat avec un médecin.</p>", "it": "<p>La <strong>CO2</strong> (o bicarbonato) nel sangue riflette l'equilibrio acido-base; è legata a rene e respirazione. Alto o basso da solo non fa diagnosi; il medico la valuta con il panel elettroliti e l'anion gap. Discuti il risultato con il medico.</p>", "he": "<p>CO2 (או ביקרבונט) בדם משקף את איזון החומצה-בסיס; קשור לכליות ולנשימה. גבוה או נמוך לבדו לא קובע אבחנה; הרופא יפרש עם פאנל האלקטרוליטים ופער האניונים. יש לדון בתוצאה עם רופא.</p>", "hi": "<p>खून में <strong>CO2</strong> (या बाइकार्बोनेट) एसिड-बेस बैलेंस दिखाता है; किडनी और सांस से जुड़ा है। हाई या लो अकेले निदान नहीं; डॉक्टर इलेक्ट्रोलाइट पैनल और एनियन गैप के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p>CO2 (أو البيكربونات) في الدم يعكس توازن الحمض-القاعدة؛ مرتبط بالكلية والتنفس. ارتفاع أو انخفاض وحده لا يشخّص؛ الطبيب يفسره مع لوحة الكهارل وفجوة الأنيون. ناقش نتيجتك مع الطبيب.</p>"}
    return _make_short_article("co2-blood-test-high-or-low", "co2-blood-test-high-or-low", published, cover, 4, cat, titles, subs, ex, seo_t, seo_d, c)


def _article_anion_gap_high() -> Article:
    """Anion gap high meaning — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/anion-gap-high-meaning-hero.png"
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "Anion gap yüksek ne anlama gelir?", "en": "What does high anion gap mean?", "es": "Anión gap alto: ¿qué significa?", "de": "Anionenlücke erhöht: Was bedeutet das?", "fr": "Trou anionique élevé : qu'est-ce que ça indique ?", "it": "Anion gap alto: cosa significa?", "he": "מה המשמעות של פער אנטיונים גבוה?", "hi": "ऐनियन गैप हाई का क्या मतलब?", "ar": "ماذا يعني ارتفاع فجوة الأنيون؟"}
    subs = {"tr": "Anion gap elektrolit panelinde hesaplanan bir değerdir; yüksekliği tek başına teşhis değildir.", "en": "Anion gap is calculated from the electrolyte panel; a high value alone is not a diagnosis.", "es": "El anión gap se calcula en el panel de electrolitos; un valor alto por sí solo no es un diagnóstico.", "de": "Die Anionenlücke wird aus dem Elektrolytpanel berechnet; ein erhöhter Wert allein ist keine Diagnose.", "fr": "Le trou anionique est calculé à partir du bilan électrolytique ; une valeur élevée seule ne fait pas un diagnostic.", "it": "L'anion gap si calcola dal panel elettroliti; un valore alto da solo non è una diagnosi.", "he": "פער האניונים מחושב מפאנל האלקטרוליטים; ערך גבוה לבדו אינו אבחנה.", "hi": "ऐनियन गैप इलेक्ट्रोलाइट पैनल से निकाला जाता है; हाई अकेले निदान नहीं।", "ar": "فجوة الأنيون تُحسب من لوحة الكهارل؛ ارتفاعها وحده ليس تشخيصاً."}
    ex = {"tr": "Anion gap yüksekliği metabolik asidoz değerlendirmesinde kullanılır; hekim elektrolit ve klinikle yorumlar.", "en": "High anion gap is used in evaluating metabolic acidosis; your doctor interprets it with electrolytes and clinical context.", "es": "El anión gap alto se usa en la evaluación de la acidosis metabólica; el médico lo interpreta con electrolitos y contexto.", "de": "Erhöhte Anionenlücke wird bei der Beurteilung der metabolischen Azidose genutzt; der Arzt wertet mit Elektrolyten und Klinik.", "fr": "Un trou anionique élevé est utilisé dans l'évaluation de l'acidose métabolique ; le médecin l'interprète avec les électrolytes et le contexte.", "it": "L'anion gap alto si usa nella valutazione dell'acidosi metabolica; il medico lo valuta con elettroliti e contesto.", "he": "פער אנטיונים גבוה משמש בהערכת חמצת מטבולית; הרופא יפרש עם אלקטרוליטים והקשר קליני.", "hi": "ऐनियन गैप हाई मेटाबॉलिक एसिडोसिस की जांच में इस्तेमाल होता है; डॉक्टर इलेक्ट्रोलाइट्स और क्लिनिकल संदर्भ के साथ व्याख्या करेंगे।", "ar": "ارتفاع فجوة الأنيون يُستخدم في تقييم الحماض الاستقلابي؛ الطبيب يفسره مع الكهارل والسياق."}
    seo_t = {"tr": "Anion Gap Yüksekliği Ne Anlama Gelir? | Norya Blog", "en": "What Does High Anion Gap Mean? | Norya Blog", "es": "Anión gap alto | Norya Blog", "de": "Anionenlücke erhöht | Norya Blog", "fr": "Trou anionique élevé | Norya Blog", "it": "Anion gap alto | Norya Blog", "he": "פער אנטיונים גבוה | Norya Blog", "hi": "ऐनियन गैप हाई | Norya Blog", "ar": "ارتفاع فجوة الأنيون | Norya Blog"}
    seo_d = {"tr": "Anion gap yüksekliği nedenleri. Bilgilendirme amaçlı.", "en": "Causes of high anion gap. For information only.", "es": "Anión gap alto: causas. Solo informativo.", "de": "Ursachen für erhöhte Anionenlücke. Nur zur Information.", "fr": "Trou anionique élevé : causes. À titre informatif.", "it": "Anion gap alto: cause. Solo informativo.", "he": "סיבות לפער אנטיונים גבוה. למידע בלבד.", "hi": "ऐनियन गैप हाई के कारण. केवल सूचनार्थ।", "ar": "أسباب ارتفاع فجوة الأنيون. لأغراض إعلامية فقط."}
    c = {"tr": "<p><strong>Anion gap</strong> sodyum, klor ve bikarbonat değerlerinden hesaplanır; metabolik asidoz tiplerinin ayrımında kullanılır. Yüksek anion gap tek başına teşhis değildir; hekiminiz elektrolit paneli, CO2 ve klinikle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p>The <strong>anion gap</strong> is calculated from sodium, chloride, and bicarbonate; it is used to distinguish types of metabolic acidosis. A high anion gap alone is not a diagnosis; your doctor interprets it with the electrolyte panel, CO2, and clinical context. Discuss your result with a doctor.</p>", "es": "<p>El <strong>anión gap</strong> se calcula a partir de sodio, cloro y bicarbonato; se usa para distinguir tipos de acidosis metabólica. Un anion gap alto por sí solo no da el diagnóstico; el médico lo interpreta con el panel de electrolitos, CO2 y contexto clínico. Comenta el resultado con un médico.</p>", "de": "<p>Die <strong>Anionenlücke</strong> wird aus Natrium, Chlorid und Bikarbonat berechnet; sie dient zur Unterscheidung von Formen der metabolischen Azidose. Erhöhte Anionenlücke allein ergibt keine Diagnose; der Arzt wertet mit dem Elektrolytpanel, CO2 und Klinik. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>trou anionique</strong> est calculé à partir du sodium, du chlore et du bicarbonate ; il sert à distinguer les types d'acidose métabolique. Un trou élevé seul ne fait pas un diagnostic ; le médecin l'interprète avec le bilan électrolytique, le CO2 et le contexte clinique. Discutez du résultat avec un médecin.</p>", "it": "<p>L'<strong>anion gap</strong> si calcola da sodio, cloro e bicarbonato; si usa per distinguere i tipi di acidosi metabolica. Un anion gap alto da solo non fa diagnosi; il medico lo valuta con il panel elettroliti, CO2 e contesto clinico. Discuti il risultato con il medico.</p>", "he": "<p><strong>פער האניונים</strong> מחושב מנתרן, כלוריד וביקרבונט; משמש להבחנה בין סוגי חמצת מטבולית. פער גבוה לבדו אינו אבחנה; הרופא יפרש עם פאנל האלקטרוליטים, CO2 וההקשר הקליני. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>ऐनियन गैप</strong> सोडियम, क्लोराइड और बाइकार्बोनेट से निकाला जाता है; मेटाबॉलिक एसिडोसिस के प्रकार बताने में इस्तेमाल होता है। हाई ऐनियन गैप अकेले निदान नहीं; डॉक्टर इलेक्ट्रोलाइट पैनल, CO2 और क्लिनिकल संदर्भ के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>فجوة الأنيون</strong> تُحسب من الصوديوم والكلوريد والبيكربونات؛ تُستخدم لتمييز أنواع الحماض الاستقلابي. ارتفاع الفجوة وحده لا يشخّص؛ الطبيب يفسره مع لوحة الكهارل وCO2 والسياق السريري. ناقش نتيجتك مع الطبيب.</p>"}
    return _make_short_article("anion-gap-high-meaning", "anion-gap-high-meaning", published, cover, 4, cat, titles, subs, ex, seo_t, seo_d, c)


def _article_mpv_high_low() -> Article:
    """MPV high or low — 9 dil."""
    published = date(2026, 3, 25)
    cover = "/static/images/blog/mpv-high-or-low-hero.png"
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "MPV (trombosit hacmi) yüksek veya düşük ne anlama gelir?", "en": "MPV high or low: what it means", "es": "MPV alto o bajo: qué significa", "de": "MPV zu hoch oder zu niedrig", "fr": "MPV haut ou bas : qu'est-ce que ça indique ?", "it": "MPV alto o basso: cosa significa?", "he": "MPV גבוה או נמוך: מה המשמעות?", "hi": "MPV हाई या लो का क्या मतलब?", "ar": "MPV مرتفع أو منخفض: ماذا يعني؟"}
    subs = {"tr": "MPV trombositlerin ortalama hacmini gösterir; yüksek veya düşük tek başına teşhis değildir.", "en": "MPV reflects the average size of platelets; high or low is not a diagnosis on its own.", "es": "El MPV refleja el tamaño medio de las plaquetas; alto o bajo no es un diagnóstico por sí solo.", "de": "Der MPV gibt die durchschnittliche Thrombozytengröße an; zu hoch oder zu niedrig ist keine Diagnose für sich.", "fr": "Le MPV reflète la taille moyenne des plaquettes ; haut ou bas seul ne fait pas un diagnostic.", "it": "L'MPV riflette la dimensione media delle piastrine; alto o basso da solo non è una diagnosi.", "he": "MPV משקף את גודל הטסיות הממוצע; גבוה או נמוך לבדו אינו אבחנה.", "hi": "MPV प्लेटलेट्स का औसत आकार दिखाता है; हाई या लो अकेले निदान नहीं।", "ar": "MPV يعكس الحجم المتوسط للصفائح الدموية؛ ارتفاع أو انخفاض وحده ليس تشخيصاً."}
    ex = {"tr": "MPV trombosit sayısıyla birlikte hekim tarafından yorumlanır; tek başına teşhis koymaz.", "en": "MPV is interpreted by your doctor together with platelet count; it does not make a diagnosis alone.", "es": "El MPV lo interpreta el médico junto con el recuento de plaquetas; no da el diagnóstico por sí solo.", "de": "Der MPV wird vom Arzt zusammen mit der Thrombozytenzahl beurteilt; ein Wert allein ergibt keine Diagnose.", "fr": "Le MPV est interprété par le médecin avec le nombre de plaquettes ; un chiffre seul ne fait pas un diagnostic.", "it": "L'MPV viene valutato dal medico insieme alla piastrinemia; un solo valore non fa diagnosi.", "he": "MPV מפורש על ידי הרופא יחד עם ספירת הטסיות; ערך בודד לא קובע אבחנה.", "hi": "MPV डॉक्टर प्लेटलेट काउंट के साथ व्याख्या करेंगे; अकेले निदान नहीं।", "ar": "MPV يفسره الطبيب مع عدد الصفائح؛ الرقم وحده لا يشخّص."}
    seo_t = {"tr": "MPV Yüksek veya Düşük Ne Anlama Gelir? | Norya Blog", "en": "MPV High or Low: What It Means | Norya Blog", "es": "MPV alto o bajo | Norya Blog", "de": "MPV zu hoch oder zu niedrig | Norya Blog", "fr": "MPV haut ou bas | Norya Blog", "it": "MPV alto o basso | Norya Blog", "he": "MPV גבוה או נמוך | Norya Blog", "hi": "MPV हाई या लो | Norya Blog", "ar": "MPV مرتفع أو منخفض | Norya Blog"}
    seo_d = {"tr": "MPV yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What MPV high or low means. For information only.", "es": "MPV alto o bajo. Solo informativo.", "de": "MPV zu hoch oder zu niedrig. Nur zur Information.", "fr": "MPV haut ou bas. À titre informatif.", "it": "MPV alto o basso. Solo informativo.", "he": "MPV גבוה או נמוך. למידע בלבד.", "hi": "MPV हाई या लो. केवल सूचनार्थ।", "ar": "MPV مرتفع أو منخفض. لأغراض إعلامية فقط."}
    c = {"tr": "<p><strong>MPV</strong> (mean platelet volume) trombositlerin ortalama hacmini gösterir; CBC'de trombosit sayısıyla birlikte değerlendirilir. Yüksek veya düşük MPV tek başına teşhis değildir; hekiminiz trombosit sayısı ve klinikle birlikte yorumlar. Sonucunuzu hekimle görüşün.</p>", "en": "<p><strong>MPV</strong> (mean platelet volume) reflects the average size of platelets; it is assessed together with platelet count on a CBC. High or low MPV does not make a diagnosis alone; your doctor interprets it with platelet count and clinical context. Discuss your result with a doctor.</p>", "es": "<p>El <strong>MPV</strong> (volumen plaquetar medio) refleja el tamaño medio de las plaquetas; se valora junto con el recuento de plaquetas en el hemograma. MPV alto o bajo no da el diagnóstico por sí solo; el médico lo interpreta con el recuento de plaquetas y el contexto clínico. Comenta el resultado con un médico.</p>", "de": "<p>Der <strong>MPV</strong> (mittleres Thrombozytenvolumen) gibt die durchschnittliche Thrombozytengröße an; er wird im Blutbild zusammen mit der Thrombozytenzahl beurteilt. MPV zu hoch oder zu niedrig ergibt allein keine Diagnose; der Arzt wertet mit Thrombozytenzahl und Klinik. Befund mit dem Arzt besprechen.</p>", "fr": "<p>Le <strong>MPV</strong> (volume plaquettaire moyen) reflète la taille moyenne des plaquettes ; il est évalué avec le nombre de plaquettes sur la NFS. Un MPV haut ou bas seul ne fait pas un diagnostic ; le médecin l'interprète avec le nombre de plaquettes et le contexte clinique. Discutez du résultat avec un médecin.</p>", "it": "<p>L'<strong>MPV</strong> (volume piastrinico medio) riflette la dimensione media delle piastrine; si valuta insieme alla piastrinemia nell'emocromo. MPV alto o basso da solo non fa diagnosi; il medico lo inquadra con la piastrinemia e il contesto clinico. Discuti il risultato con il medico.</p>", "he": "<p><strong>MPV</strong> (נפח טסיות ממוצע) משקף את גודל הטסיות הממוצע; מוערך יחד עם ספירת הטסיות בספירת הדם. MPV גבוה או נמוך לבדו אינו אבחנה; הרופא יפרש עם ספירת הטסיות וההקשר הקליני. יש לדון בתוצאה עם רופא.</p>", "hi": "<p><strong>MPV</strong> (मीन प्लेटलेट वॉल्यूम) प्लेटलेट्स का औसत आकार दिखाता है; CBC में प्लेटलेट काउंट के साथ आंकलन होता है। MPV हाई या लो अकेले निदान नहीं; डॉक्टर प्लेटलेट काउंट और क्लिनिकल संदर्भ के साथ व्याख्या करेंगे। परिणाम डॉक्टर से चर्चा करें।</p>", "ar": "<p><strong>MPV</strong> (متوسط حجم الصفيحات) يعكس الحجم المتوسط للصفائح الدموية؛ يُقيّم مع عدد الصفائح في تحليل الدم. MPV مرتفع أو منخفض وحده لا يشخّص؛ الطبيب يفسره مع عدد الصفائح والسياق السريري. ناقش نتيجتك مع الطبيب.</p>"}
    return _make_short_article("mpv-high-or-low", "mpv-high-or-low", published, cover, 4, cat, titles, subs, ex, seo_t, seo_d, c, icon="/static/images/blog/icons/mpv-high-or-low.svg")


def _article_globulin_high_low() -> Article:
    """Globulin high or low meaning — 9 dil."""
    published = date(2026, 3, 13)
    # Hero: globulin-hero.png yoksa total-protein (protein paneli) fallback
    cover = "/static/images/blog/total-protein-hero.png"
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "Globulin yüksek veya düşük ne anlama gelir?", "en": "Globulin high or low: what it means", "es": "Globulina alta o baja: qué significa", "de": "Globulin zu hoch oder zu niedrig: Was bedeutet das?", "fr": "Globuline haute ou basse : qu'est-ce que ça indique ?", "it": "Globuline alte o basse: cosa significa?", "he": "גלובולין גבוה או נמוך: מה המשמעות?", "hi": "ग्लोब्युलिन हाई या लो का क्या मतलब?", "ar": "الغلوبولين مرتفع أو منخفض: ماذا يعني؟"}
    subs = {"tr": "Globulin, total proteinin albümin dışındaki kısmıdır; yüksek veya düşük tek başına teşhis değildir, hekimle yorumlanır.", "en": "Globulin is the non-albumin part of total protein; high or low is not a diagnosis on its own—your doctor interprets it with other results.", "es": "La globulina es la parte no albúmina de las proteínas totales; alto o bajo no es un diagnóstico por sí solo.", "de": "Globuline sind der Teil des Gesamteiweißes neben Albumin; zu hoch oder zu niedrig ist keine Diagnose für sich.", "fr": "Les globulines sont la partie des protéines totales autre que l'albumine ; un taux haut ou bas seul ne fait pas un diagnostic.", "it": "Le globuline sono la parte delle proteine totali diversa dall'albumina; alto o basso da solo non è una diagnosi.", "he": "גלובולין הוא החלק של חלבון כללי שאינו אלבומין; גבוה או נמוך לבדו אינו אבחנה.", "hi": "ग्लोब्युलिन टोटल प्रोटीन का वह हिस्सा है जो ऐल्ब्यूमिन नहीं है; हाई या लो अकेले निदान नहीं।", "ar": "الغلوبولين هو جزء البروتين الكلي غير الألبومين؛ ارتفاع أو انخفاض وحده ليس تشخيصاً."}
    ex = {"tr": "Globulin, total proteinde albümin dışında kalan proteinlerin toplamıdır; yüksek veya düşük nedenleri hekim tarafından albümin ve diğer tahlillerle değerlendirilir.", "en": "Globulin is the sum of proteins in blood other than albumin. Causes of high or low are assessed by your doctor together with albumin and other results.", "es": "La globulina es el conjunto de proteínas distintas de la albúmina; las causas de alto o bajo las valora el médico con albúmina y el resto.", "de": "Globuline sind die Summe der Eiweiße außer Albumin; Ursachen für hoch oder niedrig beurteilt der Arzt mit Albumin und übrigen Befunden.", "fr": "Les globulines regroupent les protéines autres que l'albumine ; les causes d'un taux haut ou bas sont évaluées par le médecin avec le bilan.", "it": "Le globuline sono l'insieme delle proteine diverse dall'albumina; le cause di alto o basso le valuta il medico con gli altri esami.", "he": "גלובולין הוא סך החלבונים מלבד אלבומין; סיבות לגבוה או נמוך יבדקו עם הרופא עם שאר התוצאות.", "hi": "ग्लोब्युलिन ऐल्ब्यूमिन के अलावा बाकी प्रोटीन का योग है; हाई या लो के कारण डॉक्टर ऐल्ब्यूमिन और बाकी रिज़ल्ट के साथ आंकलन करेंगे।", "ar": "الغلوبولين هو مجموع البروتينات عدا الألبومين؛ أسباب الارتفاع أو الانخفاض يقيّمها الطبيب مع بقية النتائج."}
    seo_t = {"tr": "Globulin Yüksek veya Düşük Ne Anlama Gelir? | Norya Blog", "en": "Globulin High or Low: What It Means | Norya Blog", "es": "Globulina alta o baja | Norya Blog", "de": "Globulin zu hoch oder zu niedrig | Norya Blog", "fr": "Globuline haute ou basse | Norya Blog", "it": "Globuline alte o basse | Norya Blog", "he": "גלובולין גבוה או נמוך | Norya Blog", "hi": "ग्लोब्युलिन हाई या लो | Norya Blog", "ar": "الغلوبولين مرتفع أو منخفض | Norya Blog"}
    seo_d = {"tr": "Globulin yüksek veya düşük nedenleri. Bilgilendirme amaçlı.", "en": "What globulin high or low means. For information only.", "es": "Globulina alta o baja: causas. Solo informativo.", "de": "Globulin zu hoch oder zu niedrig. Nur zur Information.", "fr": "Globuline haute ou basse. À titre informatif.", "it": "Globuline alte o basse. Solo informativo.", "he": "גלובולין גבוה או נמוך. למידע בלבד.", "hi": "ग्लोब्युलिन हाई या लो. केवल सूचनार्थ।", "ar": "الغلوبولين مرتفع أو منخفض. لأغراض إعلامية فقط."}
    c = {
        "tr": "<p><strong>Globulin</strong>, kanda ölçülen toplam protein miktarının albümin dışındaki kısmını temsil eder; antikorlar ve taşıma proteinleri gibi farklı protein türlerini içerir. Yüksek veya düşük globulin tek başına teşhis koydurmaz; karaciğer, böbrek ve beslenme ile ilgili başka verilerle birlikte anlam kazanır.</p><h3>Globulin yüksekse ne anlama gelebilir?</h3><p>Uzun süren iltihabi hastalıklar, bazı kronik enfeksiyonlar veya bağışıklık sistemiyle ilgili tablolar globulin düzeyini yükseltebilir. Karaciğer hastalıkları veya bazı kan hastalıklarında da globulin artışı görülebilir; bunun derecesi, birlikte değişen diğer kan değerleriyle beraber yorumlanmalıdır.</p><h3>Globulin düşükse ne anlama gelebilir?</h3><p>Düşük globulin, karaciğerin protein üretim kapasitesindeki azalma, yetersiz protein alımı veya bağırsak yoluyla protein kaybı gibi nedenlerle ilişkili olabilir. Bu durumun ciddiyetini anlamak için albümin, diğer protein ölçümleri ve klinik tablo birlikte değerlendirilir.</p><h3>Sonuçlar nasıl değerlendirilir?</h3><p>Referans aralıkları laboratuvarlar arasında değişebilir; bu nedenle raporda görülen aralık her zaman sizin için ideal değeri tam olarak yansıtmayabilir. Sonucunuzu hekiminizle görüşerek, gerekirse ayrıntılı değerlendirme veya ek testler planlamanız en güvenli yaklaşımdır. Bu yazı bilgilendirme amaçlıdır ve tıbbi muayenenin yerini tutmaz.</p>",
        "en": "<p><strong>Globulin</strong> represents the portion of proteins in your blood that is not albumin; it includes antibodies and various transport proteins. A high or low globulin value on its own does not give a diagnosis; it has to be interpreted together with liver, kidney and nutritional information.</p><h3>What can a high globulin level suggest?</h3><p>Chronic inflammatory conditions, some long‑lasting infections, or immune‑related disorders can be associated with elevated globulin. Liver disease and certain blood disorders may also raise this value; how significant the change is depends on other results that move in the same direction.</p><h3>What can a low globulin level suggest?</h3><p>A low globulin level can appear when the liver produces fewer proteins, when protein intake is insufficient, or when proteins are lost through the gut. To understand how serious this is, doctors usually look at albumin, other protein results and your clinical picture together.</p><h3>How is the result interpreted in practice?</h3><p>Reference ranges differ from one laboratory to another, so the interval printed on your report is only a guide. Your doctor will put globulin next to albumin, other protein‑related tests and your symptoms before deciding whether any follow‑up is needed. This article is for information only and is not a substitute for a medical consultation.</p>",
        "es": "<p>La <strong>globulina</strong> representa la fracción de proteínas en sangre que no es albúmina; incluye anticuerpos y proteínas de transporte. Un valor alto o bajo por sí solo no da el diagnóstico; debe interpretarse con la función hepática, el estado nutricional y el resto del análisis.</p><h3>¿Qué puede indicar una globulina alta?</h3><p>Procesos inflamatorios crónicos, algunas infecciones prolongadas y ciertas alteraciones inmunitarias pueden asociarse a globulina elevada. También en algunas enfermedades hepáticas o hematológicas el valor puede subir; la importancia real se valora junto con otros resultados.</p><h3>¿Y una globulina baja?</h3><p>Una globulina baja puede relacionarse con menor producción de proteínas en el hígado, ingesta insuficiente de proteínas o pérdida de proteínas por el intestino. Para entender el cuadro completo se revisan también la albúmina, otras proteínas y los síntomas.</p><h3>Cómo hablar de este resultado con el médico</h3><p>El rango de referencia del informe es orientativo y puede variar entre laboratorios. Comenta el resultado con tu médico, que decidirá si hacen falta controles adicionales o no. Este texto es informativo y no sustituye una valoración médica presencial.</p>",
        "de": "<p><strong>Globuline</strong> stehen für den Anteil der Bluteiweiße, der nicht aus Albumin besteht; dazu gehören Antikörper und Transportproteine. Ein erhöhter oder erniedrigter Globulinwert allein ergibt noch keine Diagnose, sondern muss zusammen mit Leber‑, Nieren‑ und Ernährungsparametern betrachtet werden.</p><h3>Was kann ein erhöhter Globulinwert bedeuten?</h3><p>Chronische Entzündungen, länger bestehende Infektionen oder immunologische Erkrankungen können mit erhöhten Globulinen einhergehen. Auch Lebererkrankungen und bestimmte Bluterkrankungen kommen als Ursache infrage; wie relevant der Befund ist, zeigt sich erst im Zusammenspiel mit anderen Werten.</p><h3>Was bedeutet ein erniedrigter Globulinwert?</h3><p>Niedrige Globuline können bei eingeschränkter Eiweißproduktion in der Leber, bei unzureichender Eiweißzufuhr oder bei Eiweißverlust über den Darm auftreten. Zur Einordnung werden Albumin, andere Eiweißwerte und Ihre Beschwerden gemeinsam beurteilt.</p><h3>Wie geht man mit dem Befund um?</h3><p>Referenzbereiche unterscheiden sich je nach Labor, daher ist die aufgedruckte Spanne nur ein Anhaltspunkt. Besprechen Sie das Ergebnis mit Ihrer Ärztin/Ihrem Arzt, der entscheiden kann, ob weitere Kontrollen nötig sind. Dieser Text ersetzt keine ärztliche Beratung.</p>",
        "fr": "<p>Les <strong>globulines</strong> correspondent à la part des protéines sanguines autre que l'albumine ; elles regroupent notamment les anticorps et certaines protéines de transport. Un taux de globulines élevé ou bas seul ne fait pas un diagnostic et doit être interprété avec le bilan hépatique, l'état nutritionnel et les autres résultats.</p><h3>Quand les globulines sont élevées</h3><p>Des globulines hautes peuvent s'observer en cas d'inflammation chronique, d'infections prolongées ou de troubles immunitaires. Certaines maladies du foie ou du sang peuvent également faire monter ce taux ; l'importance réelle se juge toujours en tenant compte du reste du bilan.</p><h3>Quand les globulines sont basses</h3><p>Un taux bas peut refléter une production moindre de protéines par le foie, une alimentation pauvre en protéines ou des pertes protéiques digestives. L'interprétation se fait avec l'albumine, les autres protéines et les symptômes.</p><h3>Parler de vos résultats avec un médecin</h3><p>Les fourchettes de référence varient d'un laboratoire à l'autre et restent indicatives. Discutez du résultat avec votre médecin, qui décidera si un contrôle ou des explorations complémentaires sont nécessaires. Ce texte est informatif et ne remplace pas une consultation médicale.</p>",
        "it": "<p>Le <strong>globuline</strong> rappresentano la quota di proteine del sangue diversa dall'albumina; comprendono anticorpi e proteine di trasporto. Un valore di globuline alto o basso da solo non pone una diagnosi e va sempre letto insieme alla funzione epatica, allo stato nutrizionale e ad altri esami.</p><h3>Quando le globuline sono alte</h3><p>Globuline aumentate si possono vedere in corso di infiammazioni croniche, infezioni prolungate o alcune malattie immunitarie. Anche alcune patologie epatiche o ematologiche possono far salire il valore; la reale importanza si valuta con il resto del laboratorio.</p><h3>Quando le globuline sono basse</h3><p>Globuline basse possono indicare minore produzione di proteine da parte del fegato, scarso apporto proteico o perdite proteiche intestinali. Per inquadrare la situazione si considerano anche albumina, altre proteine e i sintomi.</p><h3>Cosa chiedere al proprio medico</h3><p>L'intervallo di riferimento sul referto è solo indicativo e può cambiare tra laboratori. Parla del risultato con il tuo medico, che valuterà se servono controlli o approfondimenti. Questo contenuto è informativo e non sostituisce una visita.</p>",
        "he": "<p><strong>גלובולין</strong> הוא החלק של החלבון בדם שאינו אלבומין; הוא כולל נוגדנים וחלבוני הובלה שונים. ערך גלובולין גבוה או נמוך בפני עצמו אינו קובע אבחנה, אלא צריך להיבחן יחד עם תפקודי כבד, מצב תזונתי ושאר הבדיקות.</p><h3>מה עשוי להעיד גלובולין גבוה?</h3><p>דלקת כרונית, זיהומים ממושכים או מצבים הקשורים למערכת החיסון יכולים להיות מלווים בגלובולין מוגבר. גם מחלות כבד או מחלות דם מסוימות יכולות להשפיע על הערך; המשמעות נקבעת רק בהקשר של שאר התוצאות.</p><h3>ומה אם הגלובולין נמוך?</h3><p>גלובולין נמוך יכול להופיע כאשר ייצור החלבון בכבד פוחת, כאשר צריכת החלבון בתזונה נמוכה או כאשר יש איבוד חלבון דרך מערכת העיכול. לצורך ההערכה בודקים יחד גם אלבומין, בדיקות חלבון נוספות ותסמינים.</p><h3>איך להמשיך מכאן?</h3><p>טווחי הייחוס שונים בין מעבדות ולכן הם מדד כללי בלבד. חשוב לדון בתוצאה עם הרופא, שיחליט אם יש צורך בבדיקות נוספות או במעקב. המידע כאן הוא להסבר בלבד ואינו מחליף ייעוץ רפואי אישי.</p>",
        "hi": "<p><strong>ग्लोब्युलिन</strong> खून में मौजूद प्रोटीनों का वह हिस्सा है जो ऐल्ब्यूमिन से अलग होता है; इसमें एंटीबॉडी और ट्रांसपोर्ट प्रोटीन जैसी कई किस्में शामिल हैं। ग्लोब्युलिन हाई या लो अकेले निदान नहीं देता, इसे लिवर फंक्शन, किडनी और पोषण से जुड़ी बाकी जानकारी के साथ देखना पड़ता है।</p><h3>ग्लोब्युलिन हाई होने पर क्या सोचा जाता है?</h3><p>लंबे समय तक चलने वाली सूजन, कुछ क्रॉनिक इन्फेक्शन या इम्यून सिस्टम की बीमारियों में ग्लोब्युलिन बढ़ा हुआ मिल सकता है। कुछ लिवर या रक्त सम्बंधी रोगों में भी यह मान ऊपर जा सकता है; असली महत्व बाकी वैल्यूज़ और लक्षणों के साथ मिलाकर तय होता है।</p><h3>ग्लोब्युलिन लो होने पर क्या मतलब हो सकता है?</h3><p>लो ग्लोब्युलिन लिवर द्वारा प्रोटीन बनाने की क्षमता में कमी, कम प्रोटीन वाला आहार या आंत से प्रोटीन के नुकसान से जुड़ा हो सकता है। डॉक्टर आम तौर पर ऐल्ब्यूमिन, अन्य प्रोटीन परिणाम और आपकी स्थिति को साथ में देखकर अर्थ निकालते हैं।</p><h3>रिपोर्ट को कैसे आगे ले जाएं?</h3><p>रिपोर्ट पर छपा रेफरेंस रेंज लैब‑दर‑लैब बदल सकता है और केवल एक मार्गदर्शक है। सबसे güvenli yol, bu sonucu kendi doktorunuzla konuşmanız ve gerekirse ileri tetkiklerin onun yönlendirmesiyle yapılmasıdır. यह लेख केवल जानकारी के लिए है, इलाज या निदान का विकल्प नहीं।</p>",
        "ar": "<p><strong>الغلوبولين</strong> هو الجزء من بروتينات الدم الذي لا يكون ألبوميناً؛ يضم أجساماً مضادة وبروتينات نقل مختلفة. ارتفاع أو انخفاض الغلوبولين وحده لا يكفي لوضع تشخيص، بل يجب النظر إليه مع وظائف الكبد والكلى والحالة الغذائية وبقية التحاليل.</p><h3>ماذا قد يعني الغلوبولين المرتفع؟</h3><p>يمكن أن يرتفع في سياق التهابات مزمنة، أو بعض الإنتانات الطويلة، أو اضطرابات في الجهاز المناعي. بعض أمراض الكبد أو الدم قد ترفع هذا المؤشر أيضاً؛ وتُقيَّم أهميته الحقيقية فقط عند مقارنته بالتحاليل الأخرى.</p><h3>وماذا عن الغلوبولين المنخفض؟</h3><p>قد يرتبط الانخفاض بقلة تصنيع البروتين في الكبد، أو بقلة تناول البروتين في الغذاء، أو بفقدان البروتين عبر الأمعاء. عادة يُنظر أيضاً إلى الألبومين وبقية بروتينات الدم مع الأعراض السريرية.</p><h3>كيف تتعامل مع النتيجة؟</h3><p>نطاقات المرجع تختلف من مختبر لآخر، لذلك فهي دليل عام فقط. ناقش نتيجتك مع الطبيب، فهو من يقرر إن كانت هناك حاجة لمتابعة أو فحوص إضافية. هذه المعلومات للتثقيف فقط ولا تغني عن الاستشارة الطبية المباشرة.</p>",
    }
    return _make_short_article("globulin-high-or-low", "globulin-high-or-low", published, cover, 5, cat, titles, subs, ex, seo_t, seo_d, c, icon="/static/images/blog/icons/globulin-high-or-low.svg")


def _article_low_wbc() -> Article:
    """Low WBC: common causes explained — 9 dil, full body."""
    from app.blog_article_low_wbc_content import get_low_wbc_sections_by_lang, get_low_wbc_faq_schema_qa
    published = date(2026, 3, 14)
    cover = "/static/images/blog/lymphocytes-hero.png"
    slugs = {l: "low-wbc-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Düşük WBC: yaygın nedenler", "en": "Low WBC: common causes explained", "es": "WBC bajo: causas frecuentes", "de": "Leukozyten niedrig: häufige Ursachen", "fr": "Globules blancs bas : causes fréquentes", "it": "Globuli bianchi bassi: cause comuni", "he": "WBC נמוך: סיבות נפוצות", "hi": "लो WBC: आम कारण", "ar": "انخفاض كريات الدم البيضاء: الأسباب الشائعة"}
    subtitles = {"tr": "Düşük beyaz küre tek başına teşhis değildir; nedenler hekimle değerlendirilir.", "en": "A low white blood cell count alone is not a diagnosis; causes are evaluated by your doctor.", "es": "Un recuento bajo de glóbulos blancos por sí solo no es un diagnóstico; el médico evalúa las causas.", "de": "Ein niedriger Leukozytenwert allein ist keine Diagnose; die Ursachen beurteilt der Arzt.", "fr": "Un taux bas de globules blancs seul ne fait pas un diagnostic ; le médecin évalue les causes.", "it": "Un valore basso di globuli bianchi da solo non è una diagnosi; le cause le valuta il medico.", "he": "ספירת דם לבנים נמוכה לבדה אינה אבחנה; הסיבות יוערכו על ידי הרופא.", "hi": "लो WBC अकेले निदान नहीं; कारण डॉक्टर द्वारा मूल्यांकित किए जाते हैं।", "ar": "انخفاض عدد الكريات البيضاء وحده ليس تشخيصاً؛ الأسباب يقيّمها الطبيب."}
    excerpts = {"tr": "Düşük WBC birçok nedene bağlı olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "Low WBC can have many causes; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "El WBC bajo puede deberse a muchas causas; no es un diagnóstico por sí solo. El médico lo interpreta con el resto.", "de": "Niedriges WBC kann viele Ursachen haben; allein keine Diagnose. Der Arzt wertet es mit den übrigen Befunden.", "fr": "Un WBC bas peut avoir de nombreuses causes ; ce n'est pas un diagnostic en soi. Le médecin l'interprète avec le bilan.", "it": "Un WBC basso può avere molte cause; non è una diagnosi da solo. Il medico lo valuta con il resto.", "he": "WBC נמוך יכול לנבוע מסיבות רבות; אינו אבחנה לבדו. הרופא יפרש עם שאר התוצאות.", "hi": "लो WBC के कई कारण हो सकते हैं; अकेले निदान नहीं। डॉक्टर बाकी रिज़ल्ट के साथ व्याख्या करेंगे।", "ar": "انخفاض WBC قد يكون لأسباب كثيرة؛ ليس تشخيصاً بذاته. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Düşük WBC nedenleri: bilgilendirme amaçlı.", "en": "Low WBC causes explained. For information only.", "es": "WBC bajo: causas. Solo informativo.", "de": "Leukozyten niedrig: Ursachen. Nur zur Information.", "fr": "Globules blancs bas : causes. À titre informatif.", "it": "Globuli bianchi bassi: cause. Solo informativo.", "he": "WBC נמוך: סיבות. למידע בלבד.", "hi": "लो WBC के कारण. केवल सूचनार्थ।", "ar": "انخفاض كريات الدم البيضاء: الأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Düşük WBC beyaz küre — Norya", "en": "Low WBC white blood cells — Norya", "es": "WBC bajo glóbulos blancos — Norya", "de": "Leukozyten niedrig — Norya", "fr": "Globules blancs bas — Norya", "it": "Globuli bianchi bassi — Norya", "he": "WBC נמוך — Norya", "hi": "लो WBC — Norya", "ar": "انخفاض كريات الدم البيضاء — Norya"}
    sections_by_lang = get_low_wbc_sections_by_lang()
    faq_schema_qa = get_low_wbc_faq_schema_qa()
    return Article(
        id="low-wbc-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
        icon="/static/images/blog/icons/low-wbc-meaning.svg",
    )


def _article_high_wbc() -> Article:
    """High WBC: infection or inflammation? — 9 dil, full body."""
    from app.blog_article_high_wbc_content import get_high_wbc_sections_by_lang, get_high_wbc_faq_schema_qa
    published = date(2026, 3, 14)
    # Hero: high-wbc-hero.png eklenene kadar WBC ile uyumlu fallback
    cover = "/static/images/blog/lymphocytes-hero.png"
    slugs = {l: "high-wbc-meaning" for l in ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")}
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "WBC yüksek: enfeksiyon mu, iltihap mı?", "en": "High WBC: infection or inflammation?", "es": "Glóbulos blancos altos: ¿infección o inflamación?", "de": "Leukozyten erhöht: Infektion oder Entzündung?", "fr": "Globules blancs élevés : infection ou inflammation ?", "it": "Globuli bianchi alti: infezione o infiammazione?", "he": "לויקוציטים גבוהים: זיהום או דלקת?", "hi": "हाई WBC: इन्फेक्शन या इन्फ्लेमेशन?", "ar": "ارتفاع كريات الدم البيضاء: عدوى أم التهاب؟"}
    subtitles = {"tr": "Beyaz küre yüksekliği tek başına teşhis değildir; enfeksiyon ve iltihap ayrımı hekimle yapılır.", "en": "A high white blood cell count alone is not a diagnosis; infection vs inflammation is interpreted by your doctor.", "es": "Un recuento alto de glóbulos blancos por sí solo no es un diagnóstico; el médico interpreta infección vs inflamación.", "de": "Ein erhöhter Leukozytenwert allein ist keine Diagnose; Infektion vs. Entzündung beurteilt der Arzt.", "fr": "Un taux élevé de globules blancs seul ne fait pas un diagnostic ; le médecin interprète infection ou inflammation.", "it": "Un valore alto di globuli bianchi da solo non è una diagnosi; infezione vs infiammazione lo valuta il medico.", "he": "ספירת דם לבנים גבוהה לבדה אינה אבחנה; זיהום מול דלקת יפורש על ידי הרופא.", "hi": "हाई WBC अकेले निदान नहीं; इन्फेक्शन बनाम इन्फ्लेमेशन डॉक्टर समझाते हैं।", "ar": "ارتفاع عدد الكريات البيضاء وحده ليس تشخيصاً؛ الطبيب يفسر العدوى مقابل الالتهاب."}
    excerpts = {"tr": "WBC yüksekliği enfeksiyon veya iltihap gibi nedenlere bağlı olabilir; tek başına teşhis değildir, hekim diğer sonuçlarla yorumlar.", "en": "High WBC can be due to infection or inflammation; it is not a diagnosis on its own—your doctor interprets it with other results.", "es": "Un WBC alto puede deberse a infección o inflamación; no es un diagnóstico por sí solo; el médico lo interpreta con el resto.", "de": "Erhöhter WBC kann von Infektion oder Entzündung kommen; allein keine Diagnose—der Arzt wertet mit den übrigen Befunden.", "fr": "Un taux de GB élevé peut être dû à une infection ou une inflammation ; ce n'est pas un diagnostic en soi—le médecin l'interprète avec le bilan.", "it": "Un WBC alto può dipendere da infezione o infiammazione; non è una diagnosi da solo—il medico lo valuta con il resto.", "he": "WBC גבוה יכול לנבוע מזיהום או דלקת; אינו אבחנה לבדו—הרופא יפרש עם שאר התוצאות.", "hi": "हाई WBC इन्फेक्शन या इन्फ्लेमेशन की वजह से हो सकता है; अकेले निदान नहीं—डॉक्टर बाकी रिज़ल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع WBC قد يكون بسبب عدوى أو التهاب؛ ليس تشخيصاً بذاته—الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "WBC yüksekliği nedenleri: enfeksiyon veya iltihap. Bilgilendirme amaçlı.", "en": "High WBC causes: infection or inflammation. For information only.", "es": "Glóbulos blancos altos: causas. Solo informativo.", "de": "Leukozyten erhöht: Ursachen. Nur zur Information.", "fr": "Globules blancs élevés : causes. À titre informatif.", "it": "Globuli bianchi alti: cause. Solo informativo.", "he": "לויקוציטים גבוהים: סיבות. למידע בלבד.", "hi": "हाई WBC के कारण. केवल सूचनार्थ।", "ar": "ارتفاع كريات الدم البيضاء: الأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "WBC beyaz küre kan tahlili — Norya", "en": "High WBC white blood cells — Norya", "es": "Glóbulos blancos altos — Norya", "de": "Leukozyten erhöht — Norya", "fr": "Globules blancs élevés — Norya", "it": "Globuli bianchi alti — Norya", "he": "לויקוציטים גבוהים — Norya", "hi": "हाई WBC — Norya", "ar": "ارتفاع كريات الدم البيضاء — Norya"}
    sections_by_lang = get_high_wbc_sections_by_lang()
    faq_schema_qa = get_high_wbc_faq_schema_qa()
    return Article(
        id="high-wbc-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
        icon="/static/images/blog/icons/high-wbc-meaning.svg",
    )


_ARTICLE_MCH_HIGH_LOW = _article_mch_high_low()
_ARTICLE_MCHC_LOW = _article_mchc_low()
_ARTICLE_EOSINOPHILS_HIGH = _article_eosinophils_high()
_ARTICLE_BASOPHILS_HIGH = _article_basophils_high()
_ARTICLE_CHLORIDE_HIGH_LOW = _article_chloride_high_low()
_ARTICLE_CO2_BLOOD_TEST = _article_co2_blood_test()
_ARTICLE_ANION_GAP_HIGH = _article_anion_gap_high()
_ARTICLE_MPV_HIGH_LOW = _article_mpv_high_low()
_ARTICLE_GLOBULIN = _article_globulin_high_low()
_ARTICLE_HIGH_WBC = _article_high_wbc()
_ARTICLE_LOW_WBC = _article_low_wbc()


def _article_homa_ir() -> Article:
    """HOMA-IR nedir / What is HOMA-IR — 9 dil, full body."""
    from app.blog_article_homa_ir_content import get_homa_ir_sections_by_lang, get_homa_ir_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/hba1c-hero.png"
    slugs = {
        "tr": "homa-ir-nedir",
        "en": "what-is-homa-ir",
        "de": "homa-ir-was-bedeutet-das",
        "es": "que-es-homa-ir",
        "fr": "quest-ce-que-homa-ir",
        "it": "cos-e-homa-ir",
        "he": "\u05de\u05d4-\u05d6\u05d4-homa-ir",
        "hi": "homa-ir-kya-hai",
        "ar": "\u0645\u0627-\u0647\u0648-homa-ir",
    }
    cat = {"tr": "Kan \u015fekeri", "en": "Blood sugar", "es": "Glucosa", "de": "Blutzucker", "fr": "Glyc\u00e9mie", "it": "Glicemia", "he": "\u05e1\u05d5\u05db\u05e8 \u05d1\u05d3\u05dd", "hi": "\u092c\u094d\u0932\u0921 \u0936\u0941\u0917\u0930", "ar": "\u0633\u0643\u0631 \u0627\u0644\u062f\u0645"}
    titles = {
        "tr": "HOMA-IR nedir? \u0130ns\u00fclin direnci indeksini anlamak",
        "en": "What is HOMA-IR? Understanding the insulin resistance index",
        "de": "HOMA-IR: Was bedeutet der Insulinresistenz-Index?",
        "es": "\u00bfQu\u00e9 es el HOMA-IR? Entender el \u00edndice de resistencia a la insulina",
        "fr": "Qu\u2019est-ce que le HOMA-IR ? Comprendre l\u2019indice d\u2019insulinor\u00e9sistance",
        "it": "Cos\u2019\u00e8 l\u2019HOMA-IR? Capire l\u2019indice di resistenza insulinica",
        "he": "\u05de\u05d4\u05d5 HOMA-IR? \u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05de\u05d3\u05d3 \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df",
        "hi": "HOMA-IR \u0915\u094d\u092f\u093e \u0939\u0948? \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938 \u0907\u0902\u0921\u0947\u0915\u094d\u0938 \u0915\u094b \u0938\u092e\u091d\u0947\u0902",
        "ar": "\u0645\u0627 \u0647\u0648 HOMA-IR\u061f \u0641\u0647\u0645 \u0645\u0624\u0634\u0631 \u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646",
    }
    subtitles = {
        "tr": "HOMA-IR a\u00e7l\u0131k glukozu ve a\u00e7l\u0131k ins\u00fclini ile hesaplanan bir ins\u00fclin direnci g\u00f6stergesidir; tek ba\u015f\u0131na te\u015fhis arac\u0131 de\u011fildir.",
        "en": "HOMA-IR is an insulin resistance marker calculated from fasting glucose and fasting insulin; it is not a diagnostic tool on its own.",
        "de": "HOMA-IR ist ein aus N\u00fcchternglukose und N\u00fcchterninsulin berechneter Insulinresistenz-Marker; allein kein Diagnose-Instrument.",
        "es": "El HOMA-IR es un marcador de resistencia a la insulina calculado a partir de glucosa e insulina en ayunas; no es una herramienta diagn\u00f3stica por s\u00ed solo.",
        "fr": "Le HOMA-IR est un marqueur d\u2019insulinor\u00e9sistance calcul\u00e9 \u00e0 partir de la glyc\u00e9mie et de l\u2019insuline \u00e0 jeun ; ce n\u2019est pas un outil diagnostique en soi.",
        "it": "L\u2019HOMA-IR \u00e8 un marcatore di resistenza insulinica calcolato da glicemia e insulinemia a digiuno; da solo non \u00e8 uno strumento diagnostico.",
        "he": "HOMA-IR \u05d4\u05d5\u05d0 \u05de\u05d3\u05d3 \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d4\u05de\u05d7\u05d5\u05e9\u05d1 \u05de\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05d5\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd; \u05d0\u05d9\u05e0\u05d5 \u05db\u05dc\u05d9 \u05d0\u05d1\u05d7\u05d5\u05df \u05d1\u05e4\u05e0\u05d9 \u05e2\u05e6\u05de\u05d5.",
        "hi": "HOMA-IR \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0917\u094d\u0932\u0942\u0915\u094b\u091c\u093c \u0914\u0930 \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0938\u0947 \u0915\u0948\u0932\u0915\u0941\u0932\u0947\u091f \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u093e \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938 \u092e\u093e\u0930\u094d\u0915\u0930 \u0939\u0948; \u0905\u0915\u0947\u0932\u0947 \u092f\u0939 \u0921\u093e\u092f\u0917\u094d\u0928\u094b\u0938\u094d\u091f\u093f\u0915 \u091f\u0942\u0932 \u0928\u0939\u0940\u0902\u0964",
        "ar": "HOMA-IR \u0645\u0624\u0634\u0631 \u0644\u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u064a\u064f\u062d\u0633\u0628 \u0645\u0646 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0648\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u064a\u0646\u061b \u0644\u064a\u0633 \u0623\u062f\u0627\u0629 \u062a\u0634\u062e\u064a\u0635 \u0628\u0645\u0641\u0631\u062f\u0647.",
    }
    excerpts = {
        "tr": "HOMA-IR a\u00e7l\u0131k kan \u015fekeri ve a\u00e7l\u0131k ins\u00fclini ile hesaplanan bir tarama indeksidir. Tek ba\u015f\u0131na te\u015fhis koymaz; hekim di\u011fer de\u011ferlerle birlikte yorumlar.",
        "en": "HOMA-IR is a screening index calculated from fasting blood sugar and fasting insulin. It does not diagnose on its own; your doctor interprets it with other results.",
        "de": "Der HOMA-IR ist ein Screening-Index aus N\u00fcchternblutzucker und N\u00fcchterninsulin. Er stellt allein keine Diagnose; der Arzt wertet ihn mit weiteren Befunden.",
        "es": "El HOMA-IR es un \u00edndice de cribado calculado a partir de la glucosa y la insulina en ayunas. No diagnostica por s\u00ed solo; el m\u00e9dico lo interpreta con otros resultados.",
        "fr": "Le HOMA-IR est un indice de d\u00e9pistage calcul\u00e9 \u00e0 partir de la glyc\u00e9mie et de l\u2019insuline \u00e0 jeun. Il ne diagnostique pas seul ; le m\u00e9decin l\u2019interpr\u00e8te avec d\u2019autres r\u00e9sultats.",
        "it": "L\u2019HOMA-IR \u00e8 un indice di screening calcolato da glicemia e insulinemia a digiuno. Non diagnostica da solo; il medico lo interpreta con altri referti.",
        "he": "HOMA-IR \u05d4\u05d5\u05d0 \u05de\u05d3\u05d3 \u05e1\u05d9\u05e0\u05d5\u05df \u05d4\u05de\u05d7\u05d5\u05e9\u05d1 \u05de\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05d5\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd. \u05d0\u05d9\u05e0\u05d5 \u05de\u05d0\u05d1\u05d7\u05df \u05dc\u05d1\u05d3\u05d5; \u05d4\u05e8\u05d5\u05e4\u05d0 \u05de\u05e4\u05e8\u05e9 \u05e2\u05dd \u05e9\u05d0\u05e8 \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea.",
        "hi": "HOMA-IR \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0917\u094d\u0932\u0942\u0915\u094b\u091c\u093c \u0914\u0930 \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0938\u0947 \u0915\u0948\u0932\u0915\u0941\u0932\u0947\u091f \u0939\u094b\u0928\u0947 \u0935\u093e\u0932\u093e \u0938\u094d\u0915\u094d\u0930\u0940\u0928\u093f\u0902\u0917 \u0907\u0902\u0921\u0947\u0915\u094d\u0938 \u0939\u0948\u0964 \u0905\u0915\u0947\u0932\u0947 \u092f\u0939 \u0928\u093f\u0926\u093e\u0928 \u0928\u0939\u0940\u0902 \u0915\u0930\u0924\u093e; \u0921\u0949\u0915\u094d\u091f\u0930 \u0926\u0942\u0938\u0930\u0947 \u0930\u093f\u091c\u093c\u0932\u094d\u091f\u094d\u0938 \u0915\u0947 \u0938\u093e\u0925 \u092a\u0922\u093c\u0924\u0947 \u0939\u0948\u0902\u0964",
        "ar": "HOMA-IR \u0645\u0624\u0634\u0631 \u0641\u062d\u0635 \u064a\u064f\u062d\u0633\u0628 \u0645\u0646 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0648\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u064a\u0646. \u0644\u0627 \u064a\u064f\u0634\u062e\u0651\u0635 \u0628\u0645\u0641\u0631\u062f\u0647\u061b \u0627\u0644\u0637\u0628\u064a\u0628 \u064a\u064f\u0641\u0633\u0651\u0631\u0647 \u0645\u0639 \u0628\u0642\u064a\u0629 \u0627\u0644\u0646\u062a\u0627\u0626\u062c.",
    }
    seo_titles = {
        "tr": "HOMA-IR Nedir? \u0130ns\u00fclin Direnci \u0130ndeksi Rehberi | Norya Blog",
        "en": "What Is HOMA-IR? Insulin Resistance Index Guide | Norya Blog",
        "de": "HOMA-IR: Was bedeutet der Insulinresistenz-Index? | Norya Blog",
        "es": "\u00bfQu\u00e9 es el HOMA-IR? Gu\u00eda del \u00edndice de resistencia a la insulina | Norya Blog",
        "fr": "Qu\u2019est-ce que le HOMA-IR ? Guide de l\u2019insulinor\u00e9sistance | Norya Blog",
        "it": "Cos\u2019\u00e8 l\u2019HOMA-IR? Guida all\u2019indice di resistenza insulinica | Norya Blog",
        "he": "\u05de\u05d4\u05d5 HOMA-IR? \u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05de\u05d3\u05d3 \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df | Norya Blog",
        "hi": "HOMA-IR \u0915\u094d\u092f\u093e \u0939\u0948? \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938 \u0907\u0902\u0921\u0947\u0915\u094d\u0938 \u0917\u093e\u0907\u0921 | Norya Blog",
        "ar": "\u0645\u0627 \u0647\u0648 HOMA-IR\u061f \u062f\u0644\u064a\u0644 \u0645\u0624\u0634\u0631 \u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 | Norya Blog",
    }
    seo_descriptions = {
        "tr": "HOMA-IR nedir, nas\u0131l hesaplan\u0131r, a\u00e7l\u0131k glukozu ve ins\u00fclin ile ili\u015fkisi, ins\u00fclin direnci ba\u011flant\u0131s\u0131. E\u011fitim ama\u00e7l\u0131.",
        "en": "What is HOMA-IR, how it is calculated, its link to fasting glucose, fasting insulin, and insulin resistance. For information only.",
        "de": "Was ist der HOMA-IR, wie wird er berechnet, Zusammenhang mit N\u00fcchternglukose, N\u00fcchterninsulin und Insulinresistenz. Nur zur Information.",
        "es": "Qu\u00e9 es el HOMA-IR, c\u00f3mo se calcula, relaci\u00f3n con glucosa e insulina en ayunas y resistencia a la insulina. Solo informativo.",
        "fr": "Qu\u2019est-ce que le HOMA-IR, comment il est calcul\u00e9, lien avec la glyc\u00e9mie et l\u2019insuline \u00e0 jeun, insulinor\u00e9sistance. \u00c0 titre informatif.",
        "it": "Cos\u2019\u00e8 l\u2019HOMA-IR, come si calcola, rapporto con glicemia e insulinemia a digiuno, resistenza insulinica. Solo informativo.",
        "he": "\u05de\u05d4\u05d5 HOMA-IR, \u05d0\u05d9\u05da \u05de\u05d7\u05e9\u05d1\u05d9\u05dd, \u05e7\u05e9\u05e8 \u05dc\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05d5\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd, \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df. \u05dc\u05de\u05d9\u05d3\u05e2 \u05d1\u05dc\u05d1\u05d3.",
        "hi": "HOMA-IR \u0915\u094d\u092f\u093e \u0939\u0948, \u0915\u0948\u0938\u0947 \u0915\u0948\u0932\u0915\u0941\u0932\u0947\u091f \u0939\u094b\u0924\u093e \u0939\u0948, \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0917\u094d\u0932\u0942\u0915\u094b\u091c\u093c \u0914\u0930 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0938\u0947 \u0938\u0902\u092c\u0902\u0927, \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938\u0964 \u0915\u0947\u0935\u0932 \u0938\u0942\u091a\u0928\u093e\u0930\u094d\u0925\u0964",
        "ar": "\u0645\u0627 \u0647\u0648 HOMA-IR\u060c \u0643\u064a\u0641 \u064a\u064f\u062d\u0633\u0628\u060c \u0639\u0644\u0627\u0642\u062a\u0647 \u0628\u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0648\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u064a\u0646 \u0648\u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646. \u0644\u0623\u063a\u0631\u0627\u0636 \u0625\u0639\u0644\u0627\u0645\u064a\u0629 \u0641\u0642\u0637.",
    }
    cover_alt = {
        "tr": "HOMA-IR ins\u00fclin direnci kan tahlili \u2014 Norya",
        "en": "HOMA-IR insulin resistance blood test \u2014 Norya",
        "de": "HOMA-IR Insulinresistenz Bluttest \u2014 Norya",
        "es": "HOMA-IR resistencia a la insulina \u2014 Norya",
        "fr": "HOMA-IR insulinor\u00e9sistance \u2014 Norya",
        "it": "HOMA-IR resistenza insulinica \u2014 Norya",
        "he": "HOMA-IR \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u2014 Norya",
        "hi": "HOMA-IR \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938 \u2014 Norya",
        "ar": "HOMA-IR \u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u2014 Norya",
    }
    sections_by_lang = get_homa_ir_sections_by_lang()
    faq_schema_qa = get_homa_ir_faq_schema_qa()
    return Article(
        id="homa-ir-what-it-is",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


_ARTICLE_HOMA_IR = _article_homa_ir()


def _article_fasting_insulin_high() -> Article:
    """Açlık insülini yüksekse ne anlama gelir / High fasting insulin meaning — 9 dil, full body."""
    from app.blog_article_fasting_insulin_content import get_fasting_insulin_sections_by_lang, get_fasting_insulin_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/hba1c-hero.png"
    slugs = {
        "tr": "aclik-insulini-yuksekse-ne-anlama-gelir",
        "en": "high-fasting-insulin-meaning",
        "de": "nuechterninsulin-zu-hoch",
        "es": "insulina-en-ayunas-alta",
        "fr": "insuline-a-jeun-elevee",
        "it": "insulina-a-digiuno-alta",
        "he": "\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df-\u05d1\u05e6\u05d5\u05dd-\u05d2\u05d1\u05d5\u05d4",
        "hi": "fasting-insulin-high-meaning",
        "ar": "\u0627\u0631\u062a\u0641\u0627\u0639-\u0627\u0644\u0627\u0646\u0633\u0648\u0644\u064a\u0646-\u0627\u0644\u0635\u0627\u0626\u0645",
    }
    cat = {"tr": "Kan \u015fekeri", "en": "Blood sugar", "es": "Glucosa", "de": "Blutzucker", "fr": "Glyc\u00e9mie", "it": "Glicemia", "he": "\u05e1\u05d5\u05db\u05e8 \u05d1\u05d3\u05dd", "hi": "\u092c\u094d\u0932\u0921 \u0936\u0941\u0917\u0930", "ar": "\u0633\u0643\u0631 \u0627\u0644\u062f\u0645"}
    titles = {
        "tr": "A\u00e7l\u0131k ins\u00fclini y\u00fcksekse ne anlama gelir?",
        "en": "What does high fasting insulin mean?",
        "de": "N\u00fcchterninsulin zu hoch: Was bedeutet das?",
        "es": "\u00bfQu\u00e9 significa tener la insulina en ayunas alta?",
        "fr": "Insuline \u00e0 jeun \u00e9lev\u00e9e : que signifie ce r\u00e9sultat ?",
        "it": "Insulina a digiuno alta: cosa significa?",
        "he": "\u05de\u05d4 \u05de\u05e9\u05de\u05e2\u05d5\u05ea \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4?",
        "hi": "\u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0939\u093e\u0908 \u0939\u094b\u0928\u0947 \u0915\u093e \u0915\u094d\u092f\u093e \u092e\u0924\u0932\u092c \u0939\u0948?",
        "ar": "\u0645\u0627\u0630\u0627 \u064a\u0639\u0646\u064a \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u061f",
    }
    subtitles = {
        "tr": "A\u00e7l\u0131k ins\u00fclini y\u00fcksekli\u011fi ins\u00fclin direncinin erken i\u015fareti olabilir; tek ba\u015f\u0131na te\u015fhis arac\u0131 de\u011fildir.",
        "en": "Elevated fasting insulin may be an early sign of insulin resistance; it is not a diagnostic tool on its own.",
        "de": "Erh\u00f6htes N\u00fcchterninsulin kann ein Fr\u00fchzeichen f\u00fcr Insulinresistenz sein; allein kein Diagnoseinstrument.",
        "es": "La insulina en ayunas elevada puede ser una se\u00f1al temprana de resistencia a la insulina; no es una herramienta diagn\u00f3stica por s\u00ed sola.",
        "fr": "Une insuline \u00e0 jeun \u00e9lev\u00e9e peut \u00eatre un signe pr\u00e9coce d\u2019insulinor\u00e9sistance ; ce n\u2019est pas un outil diagnostique en soi.",
        "it": "Un\u2019insulina a digiuno elevata pu\u00f2 essere un segnale precoce di resistenza insulinica; da sola non \u00e8 uno strumento diagnostico.",
        "he": "\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4 \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d4\u05d9\u05d5\u05ea \u05e1\u05d9\u05de\u05df \u05de\u05d5\u05e7\u05d3\u05dd \u05dc\u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df; \u05d0\u05d9\u05e0\u05d5 \u05db\u05dc\u05d9 \u05d0\u05d1\u05d7\u05d5\u05df \u05d1\u05e4\u05e0\u05d9 \u05e2\u05e6\u05de\u05d5.",
        "hi": "\u0939\u093e\u0908 \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938 \u0915\u093e \u0905\u0930\u094d\u0932\u0940 \u0938\u0902\u0915\u0947\u0924 \u0939\u094b \u0938\u0915\u0924\u093e \u0939\u0948; \u0905\u0915\u0947\u0932\u0947 \u092f\u0939 \u0921\u093e\u092f\u0917\u094d\u0928\u094b\u0938\u094d\u091f\u093f\u0915 \u091f\u0942\u0932 \u0928\u0939\u0940\u0902\u0964",
        "ar": "\u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0642\u062f \u064a\u0643\u0648\u0646 \u0639\u0644\u0627\u0645\u0629 \u0645\u0628\u0643\u0631\u0629 \u0639\u0644\u0649 \u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646\u061b \u0644\u064a\u0633 \u0623\u062f\u0627\u0629 \u062a\u0634\u062e\u064a\u0635 \u0628\u0645\u0641\u0631\u062f\u0647.",
    }
    excerpts = {
        "tr": "A\u00e7l\u0131k ins\u00fclini y\u00fcksekli\u011fi ins\u00fclin direnci veya metabolik sendrom habercisi olabilir. Tek ba\u015f\u0131na te\u015fhis koymaz; hekim di\u011fer de\u011ferlerle yorumlar.",
        "en": "High fasting insulin can signal insulin resistance or metabolic syndrome risk. It is not a diagnosis alone; your doctor interprets it with other results.",
        "de": "Erh\u00f6htes N\u00fcchterninsulin kann auf Insulinresistenz oder metabolisches Syndrom hindeuten. Allein keine Diagnose; der Arzt wertet mit weiteren Befunden.",
        "es": "La insulina en ayunas alta puede indicar resistencia a la insulina o riesgo metab\u00f3lico. No diagnostica sola; el m\u00e9dico la interpreta con otros resultados.",
        "fr": "Une insuline \u00e0 jeun \u00e9lev\u00e9e peut signaler une insulinor\u00e9sistance. Elle ne diagnostique pas seule ; le m\u00e9decin l\u2019interpr\u00e8te avec d\u2019autres r\u00e9sultats.",
        "it": "Un\u2019insulina a digiuno elevata pu\u00f2 segnalare resistenza insulinica. Non diagnostica da sola; il medico la interpreta con altri referti.",
        "he": "\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4 \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d4\u05e6\u05d1\u05d9\u05e2 \u05e2\u05dc \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df. \u05d0\u05d9\u05e0\u05d5 \u05de\u05d0\u05d1\u05d7\u05df \u05dc\u05d1\u05d3\u05d5; \u05d4\u05e8\u05d5\u05e4\u05d0 \u05de\u05e4\u05e8\u05e9 \u05e2\u05dd \u05e9\u05d0\u05e8 \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea.",
        "hi": "\u0939\u093e\u0908 \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938 \u0915\u093e \u0938\u0902\u0915\u0947\u0924 \u0939\u094b \u0938\u0915\u0924\u093e \u0939\u0948\u0964 \u0905\u0915\u0947\u0932\u0947 \u092f\u0939 \u0928\u093f\u0926\u093e\u0928 \u0928\u0939\u0940\u0902 \u0915\u0930\u0924\u093e; \u0921\u0949\u0915\u094d\u091f\u0930 \u0926\u0942\u0938\u0930\u0947 \u0930\u093f\u091c\u093c\u0932\u094d\u091f\u094d\u0938 \u0915\u0947 \u0938\u093e\u0925 \u092a\u0922\u093c\u0924\u0947 \u0939\u0948\u0902\u0964",
        "ar": "\u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0642\u062f \u064a\u0634\u064a\u0631 \u0625\u0644\u0649 \u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646. \u0644\u0627 \u064a\u064f\u0634\u062e\u0651\u0635 \u0628\u0645\u0641\u0631\u062f\u0647\u061b \u0627\u0644\u0637\u0628\u064a\u0628 \u064a\u064f\u0641\u0633\u0651\u0631\u0647 \u0645\u0639 \u0628\u0642\u064a\u0629 \u0627\u0644\u0646\u062a\u0627\u0626\u062c.",
    }
    seo_titles = {
        "tr": "A\u00e7l\u0131k \u0130ns\u00fclini Y\u00fcksekse Ne Anlama Gelir? | Norya Blog",
        "en": "What Does High Fasting Insulin Mean? | Norya Blog",
        "de": "N\u00fcchterninsulin zu hoch: Was bedeutet das? | Norya Blog",
        "es": "\u00bfQu\u00e9 significa la insulina en ayunas alta? | Norya Blog",
        "fr": "Insuline \u00e0 jeun \u00e9lev\u00e9e : que signifie ce r\u00e9sultat ? | Norya Blog",
        "it": "Insulina a digiuno alta: cosa significa? | Norya Blog",
        "he": "\u05de\u05d4 \u05de\u05e9\u05de\u05e2\u05d5\u05ea \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4? | Norya Blog",
        "hi": "\u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0939\u093e\u0908 \u0915\u093e \u0915\u094d\u092f\u093e \u092e\u0924\u0932\u092c? | Norya Blog",
        "ar": "\u0645\u0627\u0630\u0627 \u064a\u0639\u0646\u064a \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u061f | Norya Blog",
    }
    seo_descriptions = {
        "tr": "A\u00e7l\u0131k ins\u00fclini y\u00fcksekli\u011fi, ins\u00fclin direnci, HOMA-IR ba\u011flant\u0131s\u0131 ve glukoz normal olsa bile neden ins\u00fclin y\u00fcksek olabilece\u011fi. E\u011fitim ama\u00e7l\u0131.",
        "en": "What high fasting insulin means, its link to insulin resistance and HOMA-IR, and why glucose can be normal while insulin is high. For information only.",
        "de": "Was erh\u00f6htes N\u00fcchterninsulin bedeutet, Zusammenhang mit Insulinresistenz und HOMA-IR, warum der Blutzucker normal sein kann. Nur zur Information.",
        "es": "Qu\u00e9 significa insulina en ayunas alta, relaci\u00f3n con resistencia a la insulina y HOMA-IR. Solo informativo.",
        "fr": "Insuline \u00e0 jeun \u00e9lev\u00e9e : signification, lien avec l\u2019insulinor\u00e9sistance et le HOMA-IR. \u00c0 titre informatif.",
        "it": "Insulina a digiuno alta: significato, legame con resistenza insulinica e HOMA-IR. Solo informativo.",
        "he": "\u05de\u05d4 \u05de\u05e9\u05de\u05e2\u05d5\u05ea \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4, \u05e7\u05e9\u05e8 \u05dc\u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d5-HOMA-IR. \u05dc\u05de\u05d9\u05d3\u05e2 \u05d1\u05dc\u05d1\u05d3.",
        "hi": "\u0939\u093e\u0908 \u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0915\u093e \u092e\u0924\u0932\u092c, \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u0930\u0947\u091c\u093c\u093f\u0938\u094d\u091f\u0947\u0902\u0938 \u0914\u0930 HOMA-IR \u0938\u0947 \u0938\u0902\u092c\u0902\u0927\u0964 \u0915\u0947\u0935\u0932 \u0938\u0942\u091a\u0928\u093e\u0930\u094d\u0925\u0964",
        "ar": "\u0645\u0627\u0630\u0627 \u064a\u0639\u0646\u064a \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u060c \u0639\u0644\u0627\u0642\u062a\u0647 \u0628\u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0648HOMA-IR. \u0644\u0623\u063a\u0631\u0627\u0636 \u0625\u0639\u0644\u0627\u0645\u064a\u0629 \u0641\u0642\u0637.",
    }
    cover_alt = {
        "tr": "A\u00e7l\u0131k ins\u00fclini kan tahlili \u2014 Norya",
        "en": "Fasting insulin blood test \u2014 Norya",
        "de": "N\u00fcchterninsulin Bluttest \u2014 Norya",
        "es": "Insulina en ayunas an\u00e1lisis \u2014 Norya",
        "fr": "Insuline \u00e0 jeun bilan sanguin \u2014 Norya",
        "it": "Insulina a digiuno esame \u2014 Norya",
        "he": "\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d1\u05d3\u05d9\u05e7\u05ea \u05d3\u05dd \u2014 Norya",
        "hi": "\u092b\u093c\u093e\u0938\u094d\u091f\u093f\u0902\u0917 \u0907\u0902\u0938\u0941\u0932\u093f\u0928 \u092c\u094d\u0932\u0921 \u091f\u0947\u0938\u094d\u091f \u2014 Norya",
        "ar": "\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u062a\u062d\u0644\u064a\u0644 \u062f\u0645 \u2014 Norya",
    }
    sections_by_lang = get_fasting_insulin_sections_by_lang()
    faq_schema_qa = get_fasting_insulin_faq_schema_qa()
    return Article(
        id="fasting-insulin-high-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


_ARTICLE_FASTING_INSULIN_HIGH = _article_fasting_insulin_high()


def _article_triglycerides() -> Article:
    from app.blog_article_triglycerides_content import get_triglycerides_sections_by_lang, get_triglycerides_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/triglycerides-high-hero.png"
    slugs = {"tr": "trigliserit-yuksekligi-ne-anlama-gelir", "en": "triglycerides-high-meaning", "es": "trigliceridos-altos-significado", "de": "triglyzeride-zu-hoch-bedeutung", "fr": "triglycerides-eleves-signification", "it": "trigliceridi-alti-significato", "he": "טריגליצרידים-גבוהים", "hi": "triglycerides-high-meaning-hindi", "ar": "ارتفاع-الدهون-الثلاثية"}
    cat = {"tr": "Kolesterol", "en": "Cholesterol", "es": "Colesterol", "de": "Cholesterin", "fr": "Cholestérol", "it": "Colesterolo", "he": "כולסטרול", "hi": "कोलेस्ट्रॉल", "ar": "الكوليسترول"}
    titles = {"tr": "Trigliserit yüksekliği ne anlama gelir?", "en": "What does high triglycerides mean?", "es": "¿Qué significan los triglicéridos altos?", "de": "Triglyzeride zu hoch: Was bedeutet das?", "fr": "Triglycérides élevés : que signifie ce résultat ?", "it": "Trigliceridi alti: cosa significa?", "he": "מה משמעות טריגליצרידים גבוהים?", "hi": "हाई ट्राइग्लिसराइड्स का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الدهون الثلاثية؟"}
    subtitles = {"tr": "Trigliserit yüksekliği kalp-damar riski açısından önemli; tek başına teşhis değildir.", "en": "High triglycerides can be a cardiovascular risk factor; they are not a diagnosis on their own.", "es": "Los triglicéridos altos pueden ser un factor de riesgo cardiovascular; no son un diagnóstico por sí solos.", "de": "Erhöhte Triglyzeride können ein kardiovaskulärer Risikofaktor sein; allein keine Diagnose.", "fr": "Des triglycérides élevés peuvent être un facteur de risque cardiovasculaire ; ce n'est pas un diagnostic en soi.", "it": "I trigliceridi alti possono essere un fattore di rischio cardiovascolare; non sono una diagnosi da soli.", "he": "טריגליצרידים גבוהים עשויים להוות גורם סיכון קרדיווסקולרי; אינם אבחנה בפני עצמם.", "hi": "हाई ट्राइग्लिसराइड्स हृदय रोग का जोखिम कारक हो सकते हैं; अकेले निदान नहीं।", "ar": "ارتفاع الدهون الثلاثية قد يكون عامل خطر قلبي وعائي؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Trigliserit yüksekliği kalp-damar hastalıkları riski ile ilişkilendirilebilir. Tek başına teşhis değildir; hekim diğer değerlerle yorumlar.", "en": "High triglycerides may be linked to cardiovascular disease risk. Not a diagnosis alone; your doctor interprets with other results.", "es": "Los triglicéridos altos pueden estar ligados al riesgo cardiovascular. No son diagnóstico; el médico interpreta con el resto.", "de": "Erhöhte Triglyzeride können mit kardiovaskulärem Risiko zusammenhängen. Keine Diagnose allein; der Arzt wertet mit anderen Werten.", "fr": "Des triglycérides élevés peuvent être liés au risque cardiovasculaire. Pas un diagnostic seul ; le médecin interprète avec le bilan.", "it": "I trigliceridi alti possono essere legati al rischio cardiovascolare. Non diagnosi da soli; il medico valuta con altri risultati.", "he": "טריגליצרידים גבוהים עשויים לקשור לסיכון קרדיווסקולרי. לא אבחנה לבד; הרופא מפרש עם שאר התוצאות.", "hi": "हाई ट्राइग्लिसराइड्स हृदय रोग जोखिम से जुड़े हो सकते हैं। अकेले निदान नहीं; डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع الدهون الثلاثية قد يرتبط بخطر أمراض القلب. ليس تشخيصاً وحده؛ الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Trigliserit yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high triglycerides mean, normal ranges, and causes. For information only.", "es": "Triglicéridos altos: significado y causas. Solo informativo.", "de": "Triglyzeride erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "Triglycérides élevés : signification et causes. À titre informatif.", "it": "Trigliceridi alti: significato e cause. Solo informativo.", "he": "טריגליצרידים גבוהים: משמעות וסיבות. למידע בלבד.", "hi": "हाई ट्राइग्लिसराइड्स: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع الدهون الثلاثية: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Trigliserit kan tahlili — Norya", "en": "Triglycerides blood test — Norya", "es": "Triglicéridos análisis — Norya", "de": "Triglyzeride Bluttest — Norya", "fr": "Triglycérides bilan sanguin — Norya", "it": "Trigliceridi esame del sangue — Norya", "he": "טריגליצרידים בדיקת דם — Norya", "hi": "ट्राइग्लिसराइड्स ब्लड टेस्ट — Norya", "ar": "الدهون الثلاثية تحليل دم — Norya"}
    sections_by_lang = get_triglycerides_sections_by_lang()
    faq_schema_qa = get_triglycerides_faq_schema_qa()
    return Article(
        id="triglycerides-high-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_ggt() -> Article:
    from app.blog_article_ggt_content import get_ggt_sections_by_lang, get_ggt_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/ggt-high-hero.png"
    slugs = {"tr": "ggt-yuksekligi-ne-anlama-gelir", "en": "ggt-high-meaning", "es": "ggt-alta-significado", "de": "ggt-gamma-gt-zu-hoch", "fr": "ggt-gamma-gt-elevee", "it": "ggt-gamma-gt-alta", "he": "ggt-גבוה", "hi": "ggt-high-meaning-hindi", "ar": "ارتفاع-ggt"}
    cat = {"tr": "Karaciğer", "en": "Liver", "es": "Hígado", "de": "Leber", "fr": "Foie", "it": "Fegato", "he": "כבד", "hi": "लिवर", "ar": "الكبد"}
    titles = {"tr": "GGT yüksekliği ne anlama gelir?", "en": "What does high GGT (Gamma-GT) mean?", "es": "¿Qué significa la GGT alta?", "de": "GGT (Gamma-GT) zu hoch: Was bedeutet das?", "fr": "GGT élevée : que signifie ce résultat ?", "it": "GGT alta: cosa significa?", "he": "מה משמעות GGT גבוה?", "hi": "हाई GGT (गामा-GT) का क्या मतलब है?", "ar": "ماذا يعني ارتفاع GGT؟"}
    subtitles = {"tr": "GGT karaciğer ve safra yolları hakkında ipucu verir; tek başına teşhis koymaz.", "en": "GGT gives clues about liver and bile duct health; it does not diagnose on its own.", "es": "La GGT da pistas sobre hígado y vías biliares; no diagnostica por sí sola.", "de": "GGT gibt Hinweise auf Leber und Gallenwege; allein keine Diagnose.", "fr": "La GGT donne des indices sur le foie et les voies biliaires ; elle ne diagnostique pas seule.", "it": "La GGT offre indizi su fegato e vie biliari; non diagnostica da sola.", "he": "GGT נותן רמזים על הכבד ודרכי המרה; אינו מאבחן לבד.", "hi": "GGT लिवर और पित्त नली के बारे में संकेत देता है; अकेले निदान नहीं करता।", "ar": "GGT يعطي مؤشرات عن الكبد والقنوات الصفراوية؛ لا يشخّص بمفرده."}
    excerpts = {"tr": "GGT yüksekliği karaciğer veya safra yolları sorunlarının işareti olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "High GGT may indicate liver or bile duct issues; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La GGT alta puede indicar problemas hepáticos o biliares; no es diagnóstico por sí sola. El médico interpreta con el resto.", "de": "Erhöhte GGT kann auf Leber- oder Gallenwegserkrankungen hinweisen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une GGT élevée peut indiquer des problèmes hépatiques ou biliaires ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "La GGT alta può indicare problemi epatici o biliari; non è diagnosi da sola. Il medico valuta con altri risultati.", "he": "GGT גבוה עשוי להצביע על בעיות בכבד או בדרכי המרה; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई GGT लिवर या पित्त नली की समस्या का संकेत हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع GGT قد يشير إلى مشاكل في الكبد أو القنوات الصفراوية؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "GGT yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high GGT means, normal ranges, and causes. For information only.", "es": "GGT alta: significado y causas. Solo informativo.", "de": "GGT erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "GGT élevée : signification et causes. À titre informatif.", "it": "GGT alta: significato e cause. Solo informativo.", "he": "GGT גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई GGT: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع GGT: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "GGT kan tahlili — Norya", "en": "GGT blood test — Norya", "es": "GGT análisis de sangre — Norya", "de": "GGT Bluttest — Norya", "fr": "GGT bilan sanguin — Norya", "it": "GGT esame del sangue — Norya", "he": "GGT בדיקת דם — Norya", "hi": "GGT ब्लड टेस्ट — Norya", "ar": "GGT تحليل دم — Norya"}
    sections_by_lang = get_ggt_sections_by_lang()
    faq_schema_qa = get_ggt_faq_schema_qa()
    return Article(
        id="ggt-high-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_uric_acid() -> Article:
    from app.blog_article_uric_acid_content import get_uric_acid_sections_by_lang, get_uric_acid_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/uric-acid-high-hero.png"
    slugs = {"tr": "urik-asit-yuksekligi-ne-anlama-gelir", "en": "uric-acid-high-meaning", "es": "acido-urico-alto-significado", "de": "harnsaeure-zu-hoch-bedeutung", "fr": "acide-urique-eleve-signification", "it": "acido-urico-alto-significato", "he": "חומצה-אורית-גבוהה", "hi": "uric-acid-high-meaning-hindi", "ar": "ارتفاع-حمض-اليوريك"}
    cat = {"tr": "Böbrek", "en": "Kidney", "es": "Riñón", "de": "Niere", "fr": "Rein", "it": "Rene", "he": "כליות", "hi": "किडनी", "ar": "الكلى"}
    titles = {"tr": "Ürik asit yüksekliği ne anlama gelir?", "en": "What does high uric acid mean?", "es": "¿Qué significa el ácido úrico alto?", "de": "Harnsäure zu hoch: Was bedeutet das?", "fr": "Acide urique élevé : que signifie ce résultat ?", "it": "Acido urico alto: cosa significa?", "he": "מה משמעות חומצה אורית גבוהה?", "hi": "हाई यूरिक एसिड का क्या मतलब है?", "ar": "ماذا يعني ارتفاع حمض اليوريك؟"}
    subtitles = {"tr": "Ürik asit yüksekliği gut veya böbrek sorunlarına işaret edebilir; tek başına teşhis değildir.", "en": "High uric acid may point to gout or kidney issues; it is not a diagnosis on its own.", "es": "El ácido úrico alto puede indicar gota o problemas renales; no es un diagnóstico por sí solo.", "de": "Erhöhte Harnsäure kann auf Gicht oder Nierenprobleme hinweisen; allein keine Diagnose.", "fr": "Un acide urique élevé peut indiquer la goutte ou des problèmes rénaux ; ce n'est pas un diagnostic en soi.", "it": "L'acido urico alto può indicare gotta o problemi renali; non è una diagnosi da solo.", "he": "חומצה אורית גבוהה עשויה להצביע על שגדון או בעיות כליות; אינה אבחנה בפני עצמה.", "hi": "हाई यूरिक एसिड गाउट या किडनी समस्या का संकेत हो सकता है; अकेले निदान नहीं।", "ar": "ارتفاع حمض اليوريك قد يشير إلى النقرس أو مشاكل كلوية؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Ürik asit yüksekliği gut veya böbrek sorunlarıyla ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "High uric acid may be associated with gout or kidney problems; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "El ácido úrico alto puede estar asociado a gota o problemas renales; no es diagnóstico solo. El médico interpreta con el resto.", "de": "Erhöhte Harnsäure kann mit Gicht oder Nierenproblemen zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Un acide urique élevé peut être lié à la goutte ou à des problèmes rénaux ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "L'acido urico alto può essere legato a gotta o problemi renali; non diagnosi da solo. Il medico valuta con altri risultati.", "he": "חומצה אורית גבוהה עשויה לקשור לשגדון או בעיות כליות; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई यूरिक एसिड गाउट या किडनी समस्या से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع حمض اليوريك قد يرتبط بالنقرس أو مشاكل الكلى؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Ürik asit yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high uric acid means, normal ranges, and causes. For information only.", "es": "Ácido úrico alto: significado y causas. Solo informativo.", "de": "Harnsäure erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "Acide urique élevé : signification et causes. À titre informatif.", "it": "Acido urico alto: significato e cause. Solo informativo.", "he": "חומצה אורית גבוהה: משמעות וסיבות. למידע בלבד.", "hi": "हाई यूरिक एसिड: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع حمض اليوريك: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Ürik asit kan tahlili — Norya", "en": "Uric acid blood test — Norya", "es": "Ácido úrico análisis — Norya", "de": "Harnsäure Bluttest — Norya", "fr": "Acide urique bilan sanguin — Norya", "it": "Acido urico esame del sangue — Norya", "he": "חומצה אורית בדיקת דם — Norya", "hi": "यूरिक एसिड ब्लड टेस्ट — Norya", "ar": "حمض اليوريك تحليل دم — Norya"}
    sections_by_lang = get_uric_acid_sections_by_lang()
    faq_schema_qa = get_uric_acid_faq_schema_qa()
    return Article(
        id="uric-acid-high-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_magnesium() -> Article:
    from app.blog_article_magnesium_content import get_magnesium_sections_by_lang, get_magnesium_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/magnesium-deficiency-hero.png"
    slugs = {"tr": "magnezyum-eksikligi-ne-anlama-gelir", "en": "magnesium-deficiency-meaning", "es": "deficiencia-magnesio-significado", "de": "magnesiummangel-bedeutung", "fr": "carence-magnesium-signification", "it": "carenza-magnesio-significato", "he": "מחסור-מגנזיום", "hi": "magnesium-deficiency-meaning-hindi", "ar": "نقص-المغنيسيوم"}
    cat = {"tr": "Mineraller", "en": "Minerals", "es": "Minerales", "de": "Mineralstoffe", "fr": "Minéraux", "it": "Minerali", "he": "מינרלים", "hi": "मिनरल्स", "ar": "المعادن"}
    titles = {"tr": "Magnezyum eksikliği ne anlama gelir?", "en": "What does magnesium deficiency mean?", "es": "¿Qué significa la deficiencia de magnesio?", "de": "Magnesiummangel: Was bedeutet das?", "fr": "Carence en magnésium : que signifie ce résultat ?", "it": "Carenza di magnesio: cosa significa?", "he": "מה משמעות מחסור במגנזיום?", "hi": "मैग्नीशियम की कमी का क्या मतलब है?", "ar": "ماذا يعني نقص المغنيسيوم؟"}
    subtitles = {"tr": "Magnezyum eksikliği kas, sinir ve kalp fonksiyonlarını etkileyebilir; tek başına teşhis değildir.", "en": "Magnesium deficiency can affect muscle, nerve, and heart function; it is not a diagnosis on its own.", "es": "La deficiencia de magnesio puede afectar músculos, nervios y corazón; no es un diagnóstico por sí sola.", "de": "Magnesiummangel kann Muskel-, Nerven- und Herzfunktion beeinflussen; allein keine Diagnose.", "fr": "Une carence en magnésium peut affecter muscles, nerfs et cœur ; ce n'est pas un diagnostic en soi.", "it": "La carenza di magnesio può influire su muscoli, nervi e cuore; non è una diagnosi da sola.", "he": "מחסור במגנזיום עשוי להשפיע על שרירים, עצבים ולב; אינו אבחנה בפני עצמו.", "hi": "मैग्नीशियम की कमी मांसपेशियों, नसों और हृदय को प्रभावित कर सकती है; अकेले निदान नहीं।", "ar": "نقص المغنيسيوم قد يؤثر على العضلات والأعصاب والقلب؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Magnezyum eksikliği kas krampları, yorgunluk ve kalp ritmi sorunlarıyla ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "Magnesium deficiency may be associated with muscle cramps, fatigue, and heart rhythm issues; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La deficiencia de magnesio puede asociarse a calambres, fatiga y arritmias; no es diagnóstico solo. El médico interpreta con el resto.", "de": "Magnesiummangel kann mit Muskelkrämpfen, Müdigkeit und Herzrhythmusstörungen zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une carence en magnésium peut être liée à des crampes, de la fatigue et des troubles du rythme ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "La carenza di magnesio può essere legata a crampi, stanchezza e aritmie; non diagnosi da sola. Il medico valuta con altri risultati.", "he": "מחסור במגנזיום עשוי לקשור להתכווצויות שרירים, עייפות ובעיות קצב לב; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "मैग्नीशियम की कमी मांसपेशियों में ऐंठन, थकान और हृदय ताल समस्या से जुड़ी हो सकती है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "نقص المغنيسيوم قد يرتبط بتشنجات عضلية وإرهاق واضطرابات نظم القلب؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Magnezyum eksikliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What magnesium deficiency means, normal ranges, and causes. For information only.", "es": "Deficiencia de magnesio: significado y causas. Solo informativo.", "de": "Magnesiummangel: Ursachen und Normalwerte. Nur zur Information.", "fr": "Carence en magnésium : signification et causes. À titre informatif.", "it": "Carenza di magnesio: significato e cause. Solo informativo.", "he": "מחסור במגנזיום: משמעות וסיבות. למידע בלבד.", "hi": "मैग्नीशियम की कमी: मतलब और कारण। केवल सूचनार्थ।", "ar": "نقص المغنيسيوم: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Magnezyum kan tahlili — Norya", "en": "Magnesium blood test — Norya", "es": "Magnesio análisis — Norya", "de": "Magnesium Bluttest — Norya", "fr": "Magnésium bilan sanguin — Norya", "it": "Magnesio esame del sangue — Norya", "he": "מגנזיום בדיקת דם — Norya", "hi": "मैग्नीशियम ब्लड टेस्ट — Norya", "ar": "المغنيسيوم تحليل دم — Norya"}
    sections_by_lang = get_magnesium_sections_by_lang()
    faq_schema_qa = get_magnesium_faq_schema_qa()
    return Article(
        id="magnesium-deficiency-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_bilirubin() -> Article:
    from app.blog_article_bilirubin_content import get_bilirubin_sections_by_lang, get_bilirubin_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/bilirubin-high-hero.png"
    slugs = {"tr": "bilirubin-yuksekligi-ne-anlama-gelir", "en": "bilirubin-high-meaning", "es": "bilirrubina-alta-significado", "de": "bilirubin-zu-hoch-bedeutung", "fr": "bilirubine-elevee-signification", "it": "bilirubina-alta-significato", "he": "בילירובין-גבוה", "hi": "bilirubin-high-meaning-hindi", "ar": "ارتفاع-البيليروبين"}
    cat = {"tr": "Karaciğer", "en": "Liver", "es": "Hígado", "de": "Leber", "fr": "Foie", "it": "Fegato", "he": "כבד", "hi": "लिवर", "ar": "الكبد"}
    titles = {"tr": "Bilirubin yüksekliği ne anlama gelir?", "en": "What does high bilirubin mean?", "es": "¿Qué significa la bilirrubina alta?", "de": "Bilirubin zu hoch: Was bedeutet das?", "fr": "Bilirubine élevée : que signifie ce résultat ?", "it": "Bilirubina alta: cosa significa?", "he": "מה משמעות בילירובין גבוה?", "hi": "हाई बिलीरुबिन का क्या मतलब है?", "ar": "ماذا يعني ارتفاع البيليروبين؟"}
    subtitles = {"tr": "Bilirubin yüksekliği karaciğer veya kan yıkımı sorunlarına işaret edebilir; tek başına teşhis değildir.", "en": "High bilirubin may indicate liver or red blood cell breakdown issues; it is not a diagnosis on its own.", "es": "La bilirrubina alta puede indicar problemas hepáticos o hemólisis; no es un diagnóstico por sí sola.", "de": "Erhöhtes Bilirubin kann auf Leber- oder Hämolyseprobleme hinweisen; allein keine Diagnose.", "fr": "Une bilirubine élevée peut indiquer des problèmes hépatiques ou d'hémolyse ; ce n'est pas un diagnostic en soi.", "it": "La bilirubina alta può indicare problemi epatici o emolisi; non è una diagnosi da sola.", "he": "בילירובין גבוה עשוי להצביע על בעיות בכבד או פירוק תאי דם; אינו אבחנה בפני עצמו.", "hi": "हाई बिलीरुबिन लिवर या लाल रक्त कोशिका विघटन समस्या का संकेत हो सकता है; अकेले निदान नहीं।", "ar": "ارتفاع البيليروبين قد يشير إلى مشاكل في الكبد أو تحلل كريات الدم الحمراء؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Bilirubin yüksekliği karaciğer hastalığı veya hemoliz ile ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "High bilirubin may be linked to liver disease or hemolysis; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La bilirrubina alta puede estar ligada a enfermedad hepática o hemólisis; no es diagnóstico sola. El médico interpreta con el resto.", "de": "Erhöhtes Bilirubin kann mit Lebererkrankung oder Hämolyse zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une bilirubine élevée peut être liée à une maladie hépatique ou une hémolyse ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "La bilirubina alta può essere legata a malattia epatica o emolisi; non diagnosi da sola. Il medico valuta con altri risultati.", "he": "בילירובין גבוה עשוי לקשור למחלת כבד או המוליזה; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई बिलीरुबिन लिवर रोग या हेमोलिसिस से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع البيليروبين قد يرتبط بمرض كبدي أو انحلال الدم؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Bilirubin yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high bilirubin means, normal ranges, and causes. For information only.", "es": "Bilirrubina alta: significado y causas. Solo informativo.", "de": "Bilirubin erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "Bilirubine élevée : signification et causes. À titre informatif.", "it": "Bilirubina alta: significato e cause. Solo informativo.", "he": "בילירובין גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई बिलीरुबिन: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع البيليروبين: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Bilirubin kan tahlili — Norya", "en": "Bilirubin blood test — Norya", "es": "Bilirrubina análisis — Norya", "de": "Bilirubin Bluttest — Norya", "fr": "Bilirubine bilan sanguin — Norya", "it": "Bilirubina esame del sangue — Norya", "he": "בילירובין בדיקת דם — Norya", "hi": "बिलीरुबिन ब्लड टेस्ट — Norya", "ar": "البيليروبين تحليل دم — Norya"}
    sections_by_lang = get_bilirubin_sections_by_lang()
    faq_schema_qa = get_bilirubin_faq_schema_qa()
    return Article(
        id="bilirubin-high-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_esr() -> Article:
    from app.blog_article_esr_content import get_esr_sections_by_lang, get_esr_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/esr-sedimentation-hero.png"
    slugs = {"tr": "sedimentasyon-yuksekligi-ne-anlama-gelir", "en": "esr-sedimentation-rate-meaning", "es": "vsg-sedimentacion-alta-significado", "de": "blutsenkung-bsg-erhoht-bedeutung", "fr": "vitesse-sedimentation-elevee-signification", "it": "ves-alta-significato", "he": "שקיעת-דם-גבוהה", "hi": "esr-sedimentation-rate-meaning-hindi", "ar": "ارتفاع-سرعة-الترسيب"}
    cat = {"tr": "İltihap", "en": "Inflammation", "es": "Inflamación", "de": "Entzündung", "fr": "Inflammation", "it": "Infiammazione", "he": "דלקת", "hi": "सूजन", "ar": "الالتهاب"}
    titles = {"tr": "Sedimentasyon (ESR) yüksekliği ne anlama gelir?", "en": "What does a high ESR (sedimentation rate) mean?", "es": "¿Qué significa la VSG alta?", "de": "Blutsenkung (BSG) erhöht: Was bedeutet das?", "fr": "Vitesse de sédimentation élevée : que signifie ce résultat ?", "it": "VES alta: cosa significa?", "he": "מה משמעות שקיעת דם (ESR) גבוהה?", "hi": "हाई ESR (सेडिमेंटेशन रेट) का क्या मतलब है?", "ar": "ماذا يعني ارتفاع سرعة الترسيب (ESR)؟"}
    subtitles = {"tr": "ESR yüksekliği iltihap veya enfeksiyon varlığına işaret edebilir; tek başına teşhis değildir.", "en": "A high ESR may indicate inflammation or infection; it is not a diagnosis on its own.", "es": "Una VSG alta puede indicar inflamación o infección; no es un diagnóstico por sí sola.", "de": "Eine erhöhte BSG kann auf Entzündung oder Infektion hinweisen; allein keine Diagnose.", "fr": "Une VS élevée peut indiquer une inflammation ou une infection ; ce n'est pas un diagnostic en soi.", "it": "Una VES alta può indicare infiammazione o infezione; non è una diagnosi da sola.", "he": "שקיעת דם גבוהה עשויה להצביע על דלקת או זיהום; אינה אבחנה בפני עצמה.", "hi": "हाई ESR सूजन या संक्रमण का संकेत हो सकता है; अकेले निदान नहीं।", "ar": "ارتفاع سرعة الترسيب قد يشير إلى التهاب أو عدوى؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "ESR yüksekliği iltihap veya enfeksiyon ile ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "A high ESR may be linked to inflammation or infection; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "Una VSG alta puede estar ligada a inflamación o infección; no es diagnóstico sola. El médico interpreta con el resto.", "de": "Erhöhte BSG kann mit Entzündung oder Infektion zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une VS élevée peut être liée à une inflammation ou une infection ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "Una VES alta può essere legata a infiammazione o infezione; non diagnosi da sola. Il medico valuta con altri risultati.", "he": "שקיעת דם גבוהה עשויה לקשור לדלקת או זיהום; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई ESR सूजन या संक्रमण से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع سرعة الترسيب قد يرتبط بالتهاب أو عدوى؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Sedimentasyon (ESR) yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What a high ESR means, normal ranges, and causes. For information only.", "es": "VSG alta: significado y causas. Solo informativo.", "de": "BSG erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "VS élevée : signification et causes. À titre informatif.", "it": "VES alta: significato e cause. Solo informativo.", "he": "שקיעת דם גבוהה: משמעות וסיבות. למידע בלבד.", "hi": "हाई ESR: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع سرعة الترسيب: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Sedimentasyon ESR kan tahlili — Norya", "en": "ESR sedimentation rate blood test — Norya", "es": "VSG análisis de sangre — Norya", "de": "BSG Blutsenkung Bluttest — Norya", "fr": "VS vitesse de sédimentation — Norya", "it": "VES esame del sangue — Norya", "he": "שקיעת דם בדיקת דם — Norya", "hi": "ESR सेडिमेंटेशन रेट ब्लड टेस्ट — Norya", "ar": "سرعة الترسيب تحليل دم — Norya"}
    sections_by_lang = get_esr_sections_by_lang()
    faq_schema_qa = get_esr_faq_schema_qa()
    return Article(
        id="esr-sedimentation-rate-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_cortisol() -> Article:
    from app.blog_article_cortisol_content import get_cortisol_sections_by_lang, get_cortisol_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/cortisol-levels-hero.png"
    slugs = {"tr": "kortizol-yuksekligi-ne-anlama-gelir", "en": "cortisol-levels-meaning", "es": "cortisol-alto-significado", "de": "cortisol-zu-hoch-bedeutung", "fr": "cortisol-eleve-signification", "it": "cortisolo-alto-significato", "he": "קורטיזול-גבוה", "hi": "cortisol-levels-meaning-hindi", "ar": "ارتفاع-الكورتيزول"}
    cat = {"tr": "Hormonlar", "en": "Hormones", "es": "Hormonas", "de": "Hormone", "fr": "Hormones", "it": "Ormoni", "he": "הורמונים", "hi": "हार्मोन", "ar": "الهرمونات"}
    titles = {"tr": "Kortizol yüksekliği ne anlama gelir?", "en": "What do high cortisol levels mean?", "es": "¿Qué significa el cortisol alto?", "de": "Cortisol zu hoch: Was bedeutet das?", "fr": "Cortisol élevé : que signifie ce résultat ?", "it": "Cortisolo alto: cosa significa?", "he": "מה משמעות רמת קורטיזול גבוהה?", "hi": "हाई कोर्टिसोल का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الكورتيزول؟"}
    subtitles = {"tr": "Kortizol stres hormonu olarak bilinir; yüksekliği tek başına teşhis değildir, hekim bağlamla değerlendirir.", "en": "Cortisol is known as the stress hormone; high levels alone are not a diagnosis — your doctor evaluates in context.", "es": "El cortisol es la hormona del estrés; su elevación sola no es diagnóstico — el médico evalúa en contexto.", "de": "Cortisol ist als Stresshormon bekannt; ein erhöhter Wert allein ist keine Diagnose — der Arzt beurteilt im Kontext.", "fr": "Le cortisol est l'hormone du stress ; un taux élevé seul n'est pas un diagnostic — le médecin évalue en contexte.", "it": "Il cortisolo è noto come ormone dello stress; un valore alto da solo non è una diagnosi — il medico valuta nel contesto.", "he": "קורטיזול ידוע כהורמון הלחץ; רמה גבוהה לבדה אינה אבחנה — הרופא מעריך בהקשר.", "hi": "कोर्टिसोल स्ट्रेस हार्मोन के रूप में जाना जाता है; अकेले उच्च स्तर निदान नहीं — डॉक्टर संदर्भ में मूल्यांकन करते हैं।", "ar": "الكورتيزول يُعرف بهرمون التوتر؛ ارتفاعه وحده ليس تشخيصاً — الطبيب يقيّم في السياق."}
    excerpts = {"tr": "Kortizol yüksekliği stres, ilaç kullanımı veya hormonal bozukluk ile ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "High cortisol may be related to stress, medication, or hormonal disorders; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "El cortisol alto puede estar relacionado con estrés, medicación o trastornos hormonales; no es diagnóstico solo. El médico interpreta con el resto.", "de": "Erhöhtes Cortisol kann mit Stress, Medikamenten oder Hormonstörungen zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Un cortisol élevé peut être lié au stress, à des médicaments ou à des troubles hormonaux ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "Il cortisolo alto può essere legato a stress, farmaci o disturbi ormonali; non diagnosi da solo. Il medico valuta con altri risultati.", "he": "קורטיזול גבוה עשוי לקשור ללחץ, תרופות או הפרעות הורמונליות; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई कोर्टिसोल तनाव, दवा या हार्मोनल विकार से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع الكورتيزول قد يرتبط بالتوتر أو الأدوية أو اضطرابات هرمونية؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Kortizol yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high cortisol levels mean, normal ranges, and causes. For information only.", "es": "Cortisol alto: significado y causas. Solo informativo.", "de": "Cortisol erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "Cortisol élevé : signification et causes. À titre informatif.", "it": "Cortisolo alto: significato e cause. Solo informativo.", "he": "קורטיזול גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई कोर्टिसोल: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع الكورتيزول: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Kortizol kan tahlili — Norya", "en": "Cortisol blood test — Norya", "es": "Cortisol análisis de sangre — Norya", "de": "Cortisol Bluttest — Norya", "fr": "Cortisol bilan sanguin — Norya", "it": "Cortisolo esame del sangue — Norya", "he": "קורטיזול בדיקת דם — Norya", "hi": "कोर्टिसोल ब्लड टेस्ट — Norya", "ar": "الكورتيزول تحليل دم — Norya"}
    sections_by_lang = get_cortisol_sections_by_lang()
    faq_schema_qa = get_cortisol_faq_schema_qa()
    return Article(
        id="cortisol-levels-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_testosterone() -> Article:
    from app.blog_article_testosterone_content import get_testosterone_sections_by_lang, get_testosterone_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/testosterone-levels-hero.png"
    slugs = {"tr": "testosteron-dusuklugu-ne-anlama-gelir", "en": "testosterone-levels-meaning", "es": "testosterona-baja-significado", "de": "testosteron-zu-niedrig-bedeutung", "fr": "testosterone-basse-signification", "it": "testosterone-basso-significato", "he": "טסטוסטרון-נמוך", "hi": "testosterone-levels-meaning-hindi", "ar": "انخفاض-التستوستيرون"}
    cat = {"tr": "Hormonlar", "en": "Hormones", "es": "Hormonas", "de": "Hormone", "fr": "Hormones", "it": "Ormoni", "he": "הורמונים", "hi": "हार्मोन", "ar": "الهرمونات"}
    titles = {"tr": "Testosteron düşüklüğü ne anlama gelir?", "en": "What do low testosterone levels mean?", "es": "¿Qué significa la testosterona baja?", "de": "Testosteron zu niedrig: Was bedeutet das?", "fr": "Testostérone basse : que signifie ce résultat ?", "it": "Testosterone basso: cosa significa?", "he": "מה משמעות טסטוסטרון נמוך?", "hi": "लो टेस्टोस्टेरोन का क्या मतलब है?", "ar": "ماذا يعني انخفاض التستوستيرون؟"}
    subtitles = {"tr": "Testosteron düşüklüğü hormonal dengesizliğe işaret edebilir; tek başına teşhis değildir, hekim bağlamla değerlendirir.", "en": "Low testosterone may indicate hormonal imbalance; it is not a diagnosis on its own — your doctor evaluates in context.", "es": "La testosterona baja puede indicar desequilibrio hormonal; no es diagnóstico por sí sola — el médico evalúa en contexto.", "de": "Niedriges Testosteron kann auf ein hormonelles Ungleichgewicht hinweisen; allein keine Diagnose — der Arzt beurteilt im Kontext.", "fr": "Une testostérone basse peut indiquer un déséquilibre hormonal ; ce n'est pas un diagnostic en soi — le médecin évalue en contexte.", "it": "Il testosterone basso può indicare uno squilibrio ormonale; non è una diagnosi da solo — il medico valuta nel contesto.", "he": "טסטוסטרון נמוך עשוי להצביע על חוסר איזון הורמונלי; אינו אבחנה בפני עצמו — הרופא מעריך בהקשר.", "hi": "लो टेस्टोस्टेरोन हार्मोनल असंतुलन का संकेत हो सकता है; अकेले निदान नहीं — डॉक्टर संदर्भ में मूल्यांकन करते हैं।", "ar": "انخفاض التستوستيرون قد يشير إلى خلل هرموني؛ ليس تشخيصاً بمفرده — الطبيب يقيّم في السياق."}
    excerpts = {"tr": "Testosteron düşüklüğü hormonal bozukluk, yaşlanma veya yaşam tarzı ile ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "Low testosterone may be related to hormonal disorders, aging, or lifestyle; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La testosterona baja puede estar relacionada con trastornos hormonales, envejecimiento o estilo de vida; no es diagnóstico solo. El médico interpreta con el resto.", "de": "Niedriges Testosteron kann mit Hormonstörungen, Alterung oder Lebensstil zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une testostérone basse peut être liée à des troubles hormonaux, au vieillissement ou au mode de vie ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "Il testosterone basso può essere legato a disturbi ormonali, invecchiamento o stile di vita; non diagnosi da solo. Il medico valuta con altri risultati.", "he": "טסטוסטרון נמוך עשוי לקשור להפרעות הורמונליות, הזדקנות או אורח חיים; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "लो टेस्टोस्टेरोन हार्मोनल विकार, उम्र बढ़ने या जीवनशैली से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "انخفاض التستوستيرون قد يرتبط باضطرابات هرمونية أو التقدم في العمر أو نمط الحياة؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Testosteron düşüklüğü nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What low testosterone levels mean, normal ranges, and causes. For information only.", "es": "Testosterona baja: significado y causas. Solo informativo.", "de": "Testosteron niedrig: Ursachen und Normalwerte. Nur zur Information.", "fr": "Testostérone basse : signification et causes. À titre informatif.", "it": "Testosterone basso: significato e cause. Solo informativo.", "he": "טסטוסטרון נמוך: משמעות וסיבות. למידע בלבד.", "hi": "लो टेस्टोस्टेरोन: मतलब और कारण। केवल सूचनार्थ।", "ar": "انخفاض التستوستيرون: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Testosteron kan tahlili — Norya", "en": "Testosterone blood test — Norya", "es": "Testosterona análisis de sangre — Norya", "de": "Testosteron Bluttest — Norya", "fr": "Testostérone bilan sanguin — Norya", "it": "Testosterone esame del sangue — Norya", "he": "טסטוסטרון בדיקת דם — Norya", "hi": "टेस्टोस्टेरोन ब्लड टेस्ट — Norya", "ar": "التستوستيرون تحليل دم — Norya"}
    sections_by_lang = get_testosterone_sections_by_lang()
    faq_schema_qa = get_testosterone_faq_schema_qa()
    return Article(
        id="testosterone-levels-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_folate() -> Article:
    from app.blog_article_folate_content import get_folate_sections_by_lang, get_folate_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/folate-deficiency-hero.png"
    slugs = {"tr": "folik-asit-eksikligi-ne-anlama-gelir", "en": "folate-deficiency-meaning", "es": "deficiencia-acido-folico-significado", "de": "folsaeuremangel-bedeutung", "fr": "carence-acide-folique-signification", "it": "carenza-acido-folico-significato", "he": "מחסור-חומצה-פולית", "hi": "folate-deficiency-meaning-hindi", "ar": "نقص-حمض-الفوليك"}
    cat = {"tr": "Vitaminler", "en": "Vitamins", "es": "Vitaminas", "de": "Vitamine", "fr": "Vitamines", "it": "Vitamine", "he": "ויטמינים", "hi": "विटामिन", "ar": "الفيتامينات"}
    titles = {"tr": "Folik asit eksikliği ne anlama gelir?", "en": "What does folate (folic acid) deficiency mean?", "es": "¿Qué significa la deficiencia de ácido fólico?", "de": "Folsäuremangel: Was bedeutet das?", "fr": "Carence en acide folique : que signifie ce résultat ?", "it": "Carenza di acido folico: cosa significa?", "he": "מה משמעות מחסור בחומצה פולית?", "hi": "फोलेट (फोलिक एसिड) की कमी का क्या मतलब है?", "ar": "ماذا يعني نقص حمض الفوليك؟"}
    subtitles = {"tr": "Folik asit eksikliği anemi ve sinir sistemi sorunlarına yol açabilir; tek başına teşhis değildir.", "en": "Folate deficiency can lead to anemia and nervous system issues; it is not a diagnosis on its own.", "es": "La deficiencia de ácido fólico puede causar anemia y problemas neurológicos; no es un diagnóstico por sí sola.", "de": "Folsäuremangel kann zu Anämie und Nervenproblemen führen; allein keine Diagnose.", "fr": "Une carence en acide folique peut entraîner anémie et troubles neurologiques ; ce n'est pas un diagnostic en soi.", "it": "La carenza di acido folico può causare anemia e problemi neurologici; non è una diagnosi da sola.", "he": "מחסור בחומצה פולית עשוי לגרום לאנמיה ובעיות מערכת עצבים; אינו אבחנה בפני עצמו.", "hi": "फोलेट की कमी एनीमिया और तंत्रिका तंत्र समस्या का कारण बन सकती है; अकेले निदान नहीं।", "ar": "نقص حمض الفوليك قد يؤدي إلى فقر الدم ومشاكل عصبية؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Folik asit eksikliği anemi ve sinir sistemi sorunlarıyla ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "Folate deficiency may be associated with anemia and nervous system problems; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La deficiencia de ácido fólico puede estar asociada a anemia y problemas neurológicos; no es diagnóstico sola. El médico interpreta con el resto.", "de": "Folsäuremangel kann mit Anämie und Nervenproblemen zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une carence en acide folique peut être liée à l'anémie et à des troubles neurologiques ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "La carenza di acido folico può essere legata ad anemia e problemi neurologici; non diagnosi da sola. Il medico valuta con altri risultati.", "he": "מחסור בחומצה פולית עשוי לקשור לאנמיה ובעיות מערכת עצבים; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "फोलेट की कमी एनीमिया और तंत्रिका तंत्र समस्या से जुड़ी हो सकती है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "نقص حمض الفوليك قد يرتبط بفقر الدم ومشاكل عصبية؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Folik asit eksikliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What folate deficiency means, normal ranges, and causes. For information only.", "es": "Deficiencia de ácido fólico: significado y causas. Solo informativo.", "de": "Folsäuremangel: Ursachen und Normalwerte. Nur zur Information.", "fr": "Carence en acide folique : signification et causes. À titre informatif.", "it": "Carenza di acido folico: significato e cause. Solo informativo.", "he": "מחסור בחומצה פולית: משמעות וסיבות. למידע בלבד.", "hi": "फोलेट की कमी: मतलब और कारण। केवल सूचनार्थ।", "ar": "نقص حمض الفوليك: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Folik asit kan tahlili — Norya", "en": "Folate blood test — Norya", "es": "Ácido fólico análisis — Norya", "de": "Folsäure Bluttest — Norya", "fr": "Acide folique bilan sanguin — Norya", "it": "Acido folico esame del sangue — Norya", "he": "חומצה פולית בדיקת דם — Norya", "hi": "फोलेट ब्लड टेस्ट — Norya", "ar": "حمض الفوليك تحليل دم — Norya"}
    sections_by_lang = get_folate_sections_by_lang()
    faq_schema_qa = get_folate_faq_schema_qa()
    return Article(
        id="folate-deficiency-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_phosphorus() -> Article:
    from app.blog_article_phosphorus_content import get_phosphorus_sections_by_lang, get_phosphorus_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/phosphorus-high-hero.png"
    slugs = {"tr": "fosfor-yuksekligi-ne-anlama-gelir", "en": "phosphorus-high-meaning", "es": "fosforo-alto-significado", "de": "phosphor-zu-hoch-bedeutung", "fr": "phosphore-eleve-signification", "it": "fosforo-alto-significato", "he": "זרחן-גבוה", "hi": "phosphorus-high-meaning-hindi", "ar": "ارتفاع-الفوسفور"}
    cat = {"tr": "Mineraller", "en": "Minerals", "es": "Minerales", "de": "Mineralstoffe", "fr": "Minéraux", "it": "Minerali", "he": "מינרלים", "hi": "मिनरल्स", "ar": "المعادن"}
    titles = {"tr": "Fosfor yüksekliği ne anlama gelir?", "en": "What does high phosphorus mean?", "es": "¿Qué significa el fósforo alto?", "de": "Phosphor zu hoch: Was bedeutet das?", "fr": "Phosphore élevé : que signifie ce résultat ?", "it": "Fosforo alto: cosa significa?", "he": "מה משמעות זרחן גבוה?", "hi": "हाई फॉस्फोरस का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الفوسفور؟"}
    subtitles = {"tr": "Fosfor yüksekliği böbrek fonksiyonu veya kalsiyum dengesiyle ilgili olabilir; tek başına teşhis değildir.", "en": "High phosphorus may relate to kidney function or calcium balance; it is not a diagnosis on its own.", "es": "El fósforo alto puede estar relacionado con función renal o equilibrio de calcio; no es un diagnóstico por sí solo.", "de": "Erhöhter Phosphor kann mit Nierenfunktion oder Kalziumgleichgewicht zusammenhängen; allein keine Diagnose.", "fr": "Un phosphore élevé peut être lié à la fonction rénale ou à l'équilibre calcique ; ce n'est pas un diagnostic en soi.", "it": "Il fosforo alto può essere legato alla funzione renale o all'equilibrio del calcio; non è una diagnosi da solo.", "he": "זרחן גבוה עשוי לקשור לתפקוד כליות או מאזן סידן; אינו אבחנה בפני עצמו.", "hi": "हाई फॉस्फोरस किडनी फंक्शन या कैल्शियम संतुलन से जुड़ा हो सकता है; अकेले निदान नहीं।", "ar": "ارتفاع الفوسفور قد يتعلق بوظائف الكلى أو توازن الكالسيوم؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Fosfor yüksekliği böbrek sorunları veya kalsiyum dengesizliğiyle ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "High phosphorus may be linked to kidney problems or calcium imbalance; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "El fósforo alto puede estar ligado a problemas renales o desequilibrio de calcio; no es diagnóstico solo. El médico interpreta con el resto.", "de": "Erhöhter Phosphor kann mit Nierenproblemen oder Kalziumungleichgewicht zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Un phosphore élevé peut être lié à des problèmes rénaux ou un déséquilibre calcique ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "Il fosforo alto può essere legato a problemi renali o squilibrio di calcio; non diagnosi da solo. Il medico valuta con altri risultati.", "he": "זרחן גבוה עשוי לקשור לבעיות כליות או חוסר איזון סידן; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई फॉस्फोरस किडनी समस्या या कैल्शियम असंतुलन से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع الفوسفور قد يرتبط بمشاكل كلوية أو خلل في توازن الكالسيوم؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Fosfor yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high phosphorus means, normal ranges, and causes. For information only.", "es": "Fósforo alto: significado y causas. Solo informativo.", "de": "Phosphor erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "Phosphore élevé : signification et causes. À titre informatif.", "it": "Fosforo alto: significato e cause. Solo informativo.", "he": "זרחן גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई फॉस्फोरस: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع الفوسفور: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Fosfor kan tahlili — Norya", "en": "Phosphorus blood test — Norya", "es": "Fósforo análisis — Norya", "de": "Phosphor Bluttest — Norya", "fr": "Phosphore bilan sanguin — Norya", "it": "Fosforo esame del sangue — Norya", "he": "זרחן בדיקת דם — Norya", "hi": "फॉस्फोरस ब्लड टेस्ट — Norya", "ar": "الفوسفور تحليل دم — Norya"}
    sections_by_lang = get_phosphorus_sections_by_lang()
    faq_schema_qa = get_phosphorus_faq_schema_qa()
    return Article(
        id="phosphorus-high-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_zinc() -> Article:
    from app.blog_article_zinc_content import get_zinc_sections_by_lang, get_zinc_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/zinc-deficiency-hero.png"
    slugs = {"tr": "cinko-eksikligi-ne-anlama-gelir", "en": "zinc-deficiency-meaning", "es": "deficiencia-zinc-significado", "de": "zinkmangel-bedeutung", "fr": "carence-zinc-signification", "it": "carenza-zinco-significato", "he": "מחסור-אבץ", "hi": "zinc-deficiency-meaning-hindi", "ar": "نقص-الزنك"}
    cat = {"tr": "Mineraller", "en": "Minerals", "es": "Minerales", "de": "Mineralstoffe", "fr": "Minéraux", "it": "Minerali", "he": "מינרלים", "hi": "मिनरल्स", "ar": "المعادن"}
    titles = {"tr": "Çinko eksikliği ne anlama gelir?", "en": "What does zinc deficiency mean?", "es": "¿Qué significa la deficiencia de zinc?", "de": "Zinkmangel: Was bedeutet das?", "fr": "Carence en zinc : que signifie ce résultat ?", "it": "Carenza di zinco: cosa significa?", "he": "מה משמעות מחסור באבץ?", "hi": "जिंक की कमी का क्या मतलब है?", "ar": "ماذا يعني نقص الزنك؟"}
    subtitles = {"tr": "Çinko eksikliği bağışıklık ve iyileşme süreçlerini etkileyebilir; tek başına teşhis değildir.", "en": "Zinc deficiency can affect immunity and healing; it is not a diagnosis on its own.", "es": "La deficiencia de zinc puede afectar la inmunidad y la cicatrización; no es un diagnóstico por sí sola.", "de": "Zinkmangel kann Immunität und Wundheilung beeinflussen; allein keine Diagnose.", "fr": "Une carence en zinc peut affecter l'immunité et la cicatrisation ; ce n'est pas un diagnostic en soi.", "it": "La carenza di zinco può influire sull'immunità e sulla guarigione; non è una diagnosi da sola.", "he": "מחסור באבץ עשוי להשפיע על חיסון וריפוי; אינו אבחנה בפני עצמו.", "hi": "जिंक की कमी इम्युनिटी और उपचार को प्रभावित कर सकती है; अकेले निदान नहीं।", "ar": "نقص الزنك قد يؤثر على المناعة والتئام الجروح؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Çinko eksikliği bağışıklık zayıflığı ve yara iyileşmesi sorunlarıyla ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "Zinc deficiency may be associated with weakened immunity and poor wound healing; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La deficiencia de zinc puede asociarse a inmunidad débil y cicatrización lenta; no es diagnóstico sola. El médico interpreta con el resto.", "de": "Zinkmangel kann mit geschwächter Immunität und schlechter Wundheilung zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une carence en zinc peut être liée à une immunité affaiblie et une cicatrisation lente ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "La carenza di zinco può essere legata a immunità debole e guarigione lenta; non diagnosi da sola. Il medico valuta con altri risultati.", "he": "מחסור באבץ עשוי לקשור לחיסון מוחלש וריפוי איטי; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "जिंक की कमी कमजोर इम्युनिटी और घाव भरने में समस्या से जुड़ी हो सकती है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "نقص الزنك قد يرتبط بضعف المناعة وبطء التئام الجروح؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Çinko eksikliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What zinc deficiency means, normal ranges, and causes. For information only.", "es": "Deficiencia de zinc: significado y causas. Solo informativo.", "de": "Zinkmangel: Ursachen und Normalwerte. Nur zur Information.", "fr": "Carence en zinc : signification et causes. À titre informatif.", "it": "Carenza di zinco: significato e cause. Solo informativo.", "he": "מחסור באבץ: משמעות וסיבות. למידע בלבד.", "hi": "जिंक की कमी: मतलब और कारण। केवल सूचनार्थ।", "ar": "نقص الزنك: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Çinko kan tahlili — Norya", "en": "Zinc blood test — Norya", "es": "Zinc análisis — Norya", "de": "Zink Bluttest — Norya", "fr": "Zinc bilan sanguin — Norya", "it": "Zinco esame del sangue — Norya", "he": "אבץ בדיקת דם — Norya", "hi": "जिंक ब्लड टेस्ट — Norya", "ar": "الزنك تحليل دم — Norya"}
    sections_by_lang = get_zinc_sections_by_lang()
    faq_schema_qa = get_zinc_faq_schema_qa()
    return Article(
        id="zinc-deficiency-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_inr() -> Article:
    from app.blog_article_inr_content import get_inr_sections_by_lang, get_inr_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/inr-prothrombin-hero.png"
    slugs = {"tr": "inr-protrombin-zamani-ne-anlama-gelir", "en": "inr-prothrombin-time-meaning", "es": "inr-tiempo-protrombina-significado", "de": "inr-prothrombinzeit-bedeutung", "fr": "inr-temps-prothrombine-signification", "it": "inr-tempo-protrombina-significato", "he": "inr-זמן-פרותרומבין", "hi": "inr-prothrombin-time-meaning-hindi", "ar": "inr-زمن-البروثرومبين"}
    cat = {"tr": "Pıhtılaşma", "en": "Coagulation", "es": "Coagulación", "de": "Gerinnung", "fr": "Coagulation", "it": "Coagulazione", "he": "קרישה", "hi": "कोगुलेशन", "ar": "التخثر"}
    titles = {"tr": "INR / Protrombin zamanı ne anlama gelir?", "en": "What does INR / prothrombin time mean?", "es": "¿Qué significan el INR y el tiempo de protrombina?", "de": "INR / Prothrombinzeit: Was bedeutet das?", "fr": "INR / temps de prothrombine : que signifie ce résultat ?", "it": "INR / tempo di protrombina: cosa significa?", "he": "מה משמעות INR / זמן פרותרומבין?", "hi": "INR / प्रोथ्रोम्बिन टाइम का क्या मतलब है?", "ar": "ماذا يعني INR / زمن البروثرومبين؟"}
    subtitles = {"tr": "INR pıhtılaşma hızını ölçer; tek başına teşhis değildir, hekim klinik bağlamla değerlendirir.", "en": "INR measures clotting speed; it is not a diagnosis on its own — your doctor evaluates in clinical context.", "es": "El INR mide la velocidad de coagulación; no es diagnóstico por sí solo — el médico evalúa en contexto clínico.", "de": "Der INR misst die Gerinnungsgeschwindigkeit; allein keine Diagnose — der Arzt beurteilt im klinischen Kontext.", "fr": "L'INR mesure la vitesse de coagulation ; ce n'est pas un diagnostic en soi — le médecin évalue en contexte clinique.", "it": "L'INR misura la velocità di coagulazione; non è una diagnosi da solo — il medico valuta nel contesto clinico.", "he": "INR מודד את מהירות הקרישה; אינו אבחנה בפני עצמו — הרופא מעריך בהקשר קליני.", "hi": "INR क्लॉटिंग स्पीड मापता है; अकेले निदान नहीं — डॉक्टर क्लिनिकल संदर्भ में मूल्यांकन करते हैं।", "ar": "INR يقيس سرعة التخثر؛ ليس تشخيصاً بمفرده — الطبيب يقيّم في السياق السريري."}
    excerpts = {"tr": "INR / protrombin zamanı kanın pıhtılaşma hızını gösterir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "INR / prothrombin time reflects how quickly blood clots; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "El INR / tiempo de protrombina refleja la velocidad de coagulación; no es diagnóstico solo. El médico interpreta con el resto.", "de": "INR / Prothrombinzeit zeigt die Gerinnungsgeschwindigkeit; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "L'INR / temps de prothrombine reflète la vitesse de coagulation ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "L'INR / tempo di protrombina riflette la velocità di coagulazione; non diagnosi da solo. Il medico valuta con altri risultati.", "he": "INR / זמן פרותרומבין משקף את מהירות קרישת הדם; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "INR / प्रोथ्रोम्बिन टाइम रक्त के थक्के बनने की गति दर्शाता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "INR / زمن البروثرومبين يعكس سرعة تخثر الدم؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "INR ve protrombin zamanı ne anlama gelir, normal aralıklar. Eğitim amaçlı.", "en": "What INR and prothrombin time mean, normal ranges. For information only.", "es": "INR y tiempo de protrombina: significado y causas. Solo informativo.", "de": "INR und Prothrombinzeit: Bedeutung und Normalwerte. Nur zur Information.", "fr": "INR et temps de prothrombine : signification et causes. À titre informatif.", "it": "INR e tempo di protrombina: significato e cause. Solo informativo.", "he": "INR וזמן פרותרומבין: משמעות וסיבות. למידע בלבד.", "hi": "INR और प्रोथ्रोम्बिन टाइम: मतलब और कारण। केवल सूचनार्थ।", "ar": "INR وزمن البروثرومبين: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "INR protrombin kan tahlili — Norya", "en": "INR prothrombin time blood test — Norya", "es": "INR tiempo de protrombina análisis — Norya", "de": "INR Prothrombinzeit Bluttest — Norya", "fr": "INR temps de prothrombine bilan sanguin — Norya", "it": "INR tempo di protrombina esame — Norya", "he": "INR זמן פרותרומבין בדיקת דם — Norya", "hi": "INR प्रोथ्रोम्बिन टाइम ब्लड टेस्ट — Norya", "ar": "INR زمن البروثرومبين تحليل دم — Norya"}
    sections_by_lang = get_inr_sections_by_lang()
    faq_schema_qa = get_inr_faq_schema_qa()
    return Article(
        id="inr-prothrombin-time-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_prolactin() -> Article:
    from app.blog_article_prolactin_content import get_prolactin_sections_by_lang, get_prolactin_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/prolactin-high-hero.png"
    slugs = {"tr": "prolaktin-yuksekligi-ne-anlama-gelir", "en": "prolactin-high-meaning", "es": "prolactina-alta-significado", "de": "prolaktin-zu-hoch-bedeutung", "fr": "prolactine-elevee-signification", "it": "prolattina-alta-significato", "he": "פרולקטין-גבוה", "hi": "prolactin-high-meaning-hindi", "ar": "ارتفاع-البرولاكتين"}
    cat = {"tr": "Hormonlar", "en": "Hormones", "es": "Hormonas", "de": "Hormone", "fr": "Hormones", "it": "Ormoni", "he": "הורמונים", "hi": "हार्मोन", "ar": "الهرمونات"}
    titles = {"tr": "Prolaktin yüksekliği ne anlama gelir?", "en": "What does high prolactin mean?", "es": "¿Qué significa la prolactina alta?", "de": "Prolaktin zu hoch: Was bedeutet das?", "fr": "Prolactine élevée : que signifie ce résultat ?", "it": "Prolattina alta: cosa significa?", "he": "מה משמעות פרולקטין גבוה?", "hi": "हाई प्रोलैक्टिन का क्या मतलब है?", "ar": "ماذا يعني ارتفاع البرولاكتين؟"}
    subtitles = {"tr": "Prolaktin yüksekliği hormonal bozukluk veya ilaç etkisine bağlı olabilir; tek başına teşhis değildir.", "en": "High prolactin may be due to hormonal disorders or medication; it is not a diagnosis on its own.", "es": "La prolactina alta puede deberse a trastornos hormonales o medicación; no es un diagnóstico por sí sola.", "de": "Erhöhtes Prolaktin kann durch Hormonstörungen oder Medikamente bedingt sein; allein keine Diagnose.", "fr": "Une prolactine élevée peut être due à des troubles hormonaux ou à des médicaments ; ce n'est pas un diagnostic en soi.", "it": "La prolattina alta può essere dovuta a disturbi ormonali o farmaci; non è una diagnosi da sola.", "he": "פרולקטין גבוה עשוי לנבוע מהפרעות הורמונליות או תרופות; אינו אבחנה בפני עצמו.", "hi": "हाई प्रोलैक्टिन हार्मोनल विकार या दवा के कारण हो सकता है; अकेले निदान नहीं।", "ar": "ارتفاع البرولاكتين قد يكون بسبب اضطرابات هرمونية أو أدوية؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Prolaktin yüksekliği hormonal bozukluk veya ilaç kullanımıyla ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "High prolactin may be related to hormonal disorders or medication; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La prolactina alta puede estar relacionada con trastornos hormonales o medicación; no es diagnóstico sola. El médico interpreta con el resto.", "de": "Erhöhtes Prolaktin kann mit Hormonstörungen oder Medikamenten zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une prolactine élevée peut être liée à des troubles hormonaux ou des médicaments ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "La prolattina alta può essere legata a disturbi ormonali o farmaci; non diagnosi da sola. Il medico valuta con altri risultati.", "he": "פרולקטין גבוה עשוי לקשור להפרעות הורמונליות או תרופות; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई प्रोलैक्टिन हार्मोनल विकार या दवा से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع البرولاكتين قد يرتبط باضطرابات هرمونية أو أدوية؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Prolaktin yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high prolactin means, normal ranges, and causes. For information only.", "es": "Prolactina alta: significado y causas. Solo informativo.", "de": "Prolaktin erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "Prolactine élevée : signification et causes. À titre informatif.", "it": "Prolattina alta: significato e cause. Solo informativo.", "he": "פרולקטין גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई प्रोलैक्टिन: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع البرولاكتين: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Prolaktin kan tahlili — Norya", "en": "Prolactin blood test — Norya", "es": "Prolactina análisis de sangre — Norya", "de": "Prolaktin Bluttest — Norya", "fr": "Prolactine bilan sanguin — Norya", "it": "Prolattina esame del sangue — Norya", "he": "פרולקטין בדיקת דם — Norya", "hi": "प्रोलैक्टिन ब्लड टेस्ट — Norya", "ar": "البرولاكتين تحليل دم — Norya"}
    sections_by_lang = get_prolactin_sections_by_lang()
    faq_schema_qa = get_prolactin_faq_schema_qa()
    return Article(
        id="prolactin-high-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_lipase() -> Article:
    from app.blog_article_lipase_content import get_lipase_sections_by_lang, get_lipase_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/lipase-high-hero.png"
    slugs = {"tr": "lipaz-yuksekligi-ne-anlama-gelir", "en": "lipase-high-meaning", "es": "lipasa-alta-significado", "de": "lipase-zu-hoch-bedeutung", "fr": "lipase-elevee-signification", "it": "lipasi-alta-significato", "he": "ליפאז-גבוה", "hi": "lipase-high-meaning-hindi", "ar": "ارتفاع-الليباز"}
    cat = {"tr": "Pankreas", "en": "Pancreas", "es": "Páncreas", "de": "Bauchspeicheldrüse", "fr": "Pancréas", "it": "Pancreas", "he": "לבלב", "hi": "पैंक्रियास", "ar": "البنكرياس"}
    titles = {"tr": "Lipaz yüksekliği ne anlama gelir?", "en": "What does high lipase mean?", "es": "¿Qué significa la lipasa alta?", "de": "Lipase zu hoch: Was bedeutet das?", "fr": "Lipase élevée : que signifie ce résultat ?", "it": "Lipasi alta: cosa significa?", "he": "מה משמעות ליפאז גבוה?", "hi": "हाई लाइपेज का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الليباز؟"}
    subtitles = {"tr": "Lipaz yüksekliği pankreas sorunlarına işaret edebilir; tek başına teşhis değildir.", "en": "High lipase may indicate pancreatic issues; it is not a diagnosis on its own.", "es": "La lipasa alta puede indicar problemas pancreáticos; no es un diagnóstico por sí sola.", "de": "Erhöhte Lipase kann auf Pankreasprobleme hinweisen; allein keine Diagnose.", "fr": "Une lipase élevée peut indiquer des problèmes pancréatiques ; ce n'est pas un diagnostic en soi.", "it": "La lipasi alta può indicare problemi pancreatici; non è una diagnosi da sola.", "he": "ליפאז גבוה עשוי להצביע על בעיות בלבלב; אינו אבחנה בפני עצמו.", "hi": "हाई लाइपेज पैंक्रियास समस्या का संकेत हो सकता है; अकेले निदान नहीं।", "ar": "ارتفاع الليباز قد يشير إلى مشاكل في البنكرياس؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Lipaz yüksekliği pankreatit veya diğer pankreas sorunlarıyla ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "High lipase may be linked to pancreatitis or other pancreatic issues; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "La lipasa alta puede estar ligada a pancreatitis u otros problemas pancreáticos; no es diagnóstico sola. El médico interpreta con el resto.", "de": "Erhöhte Lipase kann mit Pankreatitis oder anderen Pankreasproblemen zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Une lipase élevée peut être liée à une pancréatite ou d'autres problèmes pancréatiques ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "La lipasi alta può essere legata a pancreatite o altri problemi pancreatici; non diagnosi da sola. Il medico valuta con altri risultati.", "he": "ליפאז גבוה עשוי לקשור לדלקת לבלב או בעיות לבלב אחרות; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई लाइपेज पैंक्रिएटाइटिस या अन्य पैंक्रियास समस्या से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع الليباز قد يرتبط بالتهاب البنكرياس أو مشاكل بنكرياسية أخرى؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Lipaz yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What high lipase means, normal ranges, and causes. For information only.", "es": "Lipasa alta: significado y causas. Solo informativo.", "de": "Lipase erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "Lipase élevée : signification et causes. À titre informatif.", "it": "Lipasi alta: significato e cause. Solo informativo.", "he": "ליפאז גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई लाइपेज: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع الليباز: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Lipaz kan tahlili — Norya", "en": "Lipase blood test — Norya", "es": "Lipasa análisis de sangre — Norya", "de": "Lipase Bluttest — Norya", "fr": "Lipase bilan sanguin — Norya", "it": "Lipasi esame del sangue — Norya", "he": "ליפאז בדיקת דם — Norya", "hi": "लाइपेज ब्लड टेस्ट — Norya", "ar": "الليباز تحليل دم — Norya"}
    sections_by_lang = get_lipase_sections_by_lang()
    faq_schema_qa = get_lipase_faq_schema_qa()
    return Article(
        id="lipase-high-meaning",
        published_at=published,
        read_minutes=6,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


def _article_d_dimer() -> Article:
    from app.blog_article_d_dimer_content import get_d_dimer_sections_by_lang, get_d_dimer_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/d-dimer-high-hero.png"
    slugs = {"tr": "d-dimer-yuksekligi-ne-anlama-gelir", "en": "d-dimer-high-meaning", "es": "d-dimero-alto-significado", "de": "d-dimer-erhoht-bedeutung", "fr": "d-dimeres-eleves-signification", "it": "d-dimero-alto-significato", "he": "d-dimer-גבוה", "hi": "d-dimer-high-meaning-hindi", "ar": "ارتفاع-d-dimer"}
    cat = {"tr": "Pıhtılaşma", "en": "Coagulation", "es": "Coagulación", "de": "Gerinnung", "fr": "Coagulation", "it": "Coagulazione", "he": "קרישה", "hi": "कोगुलेशन", "ar": "التخثر"}
    titles = {"tr": "D-Dimer yüksekliği ne anlama gelir?", "en": "What does a high D-Dimer mean?", "es": "¿Qué significa el D-Dímero alto?", "de": "D-Dimer erhöht: Was bedeutet das?", "fr": "D-Dimères élevés : que signifie ce résultat ?", "it": "D-Dimero alto: cosa significa?", "he": "מה משמעות D-Dimer גבוה?", "hi": "हाई D-Dimer का क्या मतलब है?", "ar": "ماذا يعني ارتفاع D-Dimer؟"}
    subtitles = {"tr": "D-Dimer yüksekliği pıhtılaşma aktivitesine işaret edebilir; tek başına teşhis değildir.", "en": "A high D-Dimer may indicate clotting activity; it is not a diagnosis on its own.", "es": "El D-Dímero alto puede indicar actividad de coagulación; no es un diagnóstico por sí solo.", "de": "Ein erhöhter D-Dimer kann auf Gerinnungsaktivität hinweisen; allein keine Diagnose.", "fr": "Des D-Dimères élevés peuvent indiquer une activité de coagulation ; ce n'est pas un diagnostic en soi.", "it": "Un D-Dimero alto può indicare attività di coagulazione; non è una diagnosi da solo.", "he": "D-Dimer גבוה עשוי להצביע על פעילות קרישה; אינו אבחנה בפני עצמו.", "hi": "हाई D-Dimer क्लॉटिंग गतिविधि का संकेत हो सकता है; अकेले निदान नहीं।", "ar": "ارتفاع D-Dimer قد يشير إلى نشاط تخثري؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "D-Dimer yüksekliği pıhtı oluşumu veya çözülmesiyle ilişkili olabilir; tek başına teşhis değildir. Hekiminiz sonucu diğer değerlerle yorumlar.", "en": "A high D-Dimer may be linked to clot formation or breakdown; it is not a diagnosis on its own. Your doctor interprets it with other results.", "es": "El D-Dímero alto puede estar ligado a formación o degradación de coágulos; no es diagnóstico solo. El médico interpreta con el resto.", "de": "Ein erhöhter D-Dimer kann mit Gerinnselbildung oder -abbau zusammenhängen; allein keine Diagnose. Der Arzt wertet mit anderen Werten.", "fr": "Des D-Dimères élevés peuvent être liés à la formation ou dégradation de caillots ; pas un diagnostic seul. Le médecin interprète avec le bilan.", "it": "Un D-Dimero alto può essere legato a formazione o degradazione di coaguli; non diagnosi da solo. Il medico valuta con altri risultati.", "he": "D-Dimer גבוה עשוי לקשור ליצירת קרישים או פירוקם; לא אבחנה לבד. הרופא מפרש עם שאר התוצאות.", "hi": "हाई D-Dimer रक्त के थक्के बनने या टूटने से जुड़ा हो सकता है; अकेले निदान नहीं। डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "ارتفاع D-Dimer قد يرتبط بتكوّن الجلطات أو تحللها؛ ليس تشخيصاً وحده. الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "D-Dimer yüksekliği nedenleri ve normal aralıklar. Eğitim amaçlı.", "en": "What a high D-Dimer means, normal ranges, and causes. For information only.", "es": "D-Dímero alto: significado y causas. Solo informativo.", "de": "D-Dimer erhöht: Ursachen und Normalwerte. Nur zur Information.", "fr": "D-Dimères élevés : signification et causes. À titre informatif.", "it": "D-Dimero alto: significato e cause. Solo informativo.", "he": "D-Dimer גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई D-Dimer: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع D-Dimer: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "D-Dimer kan tahlili — Norya", "en": "D-Dimer blood test — Norya", "es": "D-Dímero análisis de sangre — Norya", "de": "D-Dimer Bluttest — Norya", "fr": "D-Dimères bilan sanguin — Norya", "it": "D-Dimero esame del sangue — Norya", "he": "D-Dimer בדיקת דם — Norya", "hi": "D-Dimer ब्लड टेस्ट — Norya", "ar": "D-Dimer تحليل دم — Norya"}
    sections_by_lang = get_d_dimer_sections_by_lang()
    faq_schema_qa = get_d_dimer_faq_schema_qa()
    return Article(
        id="d-dimer-high-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=sections_by_lang,
        faq_schema_qa=faq_schema_qa,
    )


_ARTICLE_TRIGLYCERIDES = _article_triglycerides()
_ARTICLE_GGT = _article_ggt()
_ARTICLE_URIC_ACID = _article_uric_acid()
_ARTICLE_MAGNESIUM = _article_magnesium()
_ARTICLE_BILIRUBIN = _article_bilirubin()
_ARTICLE_ESR = _article_esr()
_ARTICLE_CORTISOL = _article_cortisol()
_ARTICLE_TESTOSTERONE = _article_testosterone()
_ARTICLE_FOLATE = _article_folate()
_ARTICLE_PHOSPHORUS = _article_phosphorus()
_ARTICLE_ZINC = _article_zinc()
_ARTICLE_INR = _article_inr()
_ARTICLE_PROLACTIN = _article_prolactin()
_ARTICLE_LIPASE = _article_lipase()
_ARTICLE_D_DIMER = _article_d_dimer()

def _article_hemoglobin() -> Article:
    from app.blog_article_hemoglobin_content import get_hemoglobin_sections_by_lang, get_hemoglobin_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/hemoglobin-hero.jpg"
    slugs = {"tr": "hemoglobin-yuksekligi-dusuklugu-ne-anlama-gelir", "en": "hemoglobin-high-or-low-meaning", "es": "hemoglobina-alta-o-baja-significado", "de": "haemoglobin-zu-hoch-oder-niedrig", "fr": "hemoglobine-haute-ou-basse-signification", "it": "emoglobina-alta-o-bassa-significato", "he": "המוגלובין-גבוה-או-נמוך", "hi": "hemoglobin-high-or-low-meaning-hindi", "ar": "ارتفاع-او-انخفاض-الهيموجلوبين"}
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Hemoglobin yüksekliği veya düşüklüğü ne anlama gelir?", "en": "Low Hemoglobin Meaning: What High or Low Hemoglobin Means", "es": "¿Qué significa la hemoglobina alta o baja?", "de": "Hämoglobin zu hoch oder zu niedrig: Was bedeutet das?", "fr": "Hémoglobine haute ou basse : qu'est-ce que ça signifie ?", "it": "Emoglobina alta o bassa: cosa significa?", "he": "מה משמעות המוגלובין גבוה או נמוך?", "hi": "हीमोग्लोबिन हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض الهيموجلوبين؟"}
    subtitles = {"tr": "Hemoglobin kırmızı kan hücrelerinde oksijen taşıyan proteindir; yüksekliği veya düşüklüğü tek başına teşhis değildir.", "en": "Hemoglobin is the oxygen-carrying protein in red blood cells. This guide explains low hemoglobin meaning, high hemoglobin causes, normal ranges, and when to follow up.", "es": "La hemoglobina es la proteína que transporta oxígeno en los glóbulos rojos; un valor alto o bajo por sí solo no es un diagnóstico.", "de": "Hämoglobin ist das sauerstofftragende Protein in roten Blutkörperchen; erhöht oder erniedrigt allein ist keine Diagnose.", "fr": "L'hémoglobine est la protéine qui transporte l'oxygène dans les globules rouges ; un taux élevé ou bas seul ne constitue pas un diagnostic.", "it": "L'emoglobina è la proteina che trasporta ossigeno nei globuli rossi; un valore alto o basso da solo non è una diagnosi.", "he": "המוגלובין הוא החלבון הנושא חמצן בתאי דם אדומים; ערך גבוה או נמוך לבדו אינו אבחנה.", "hi": "हीमोग्लोबिन लाल रक्त कोशिकाओं में ऑक्सीजन ले जाने वाला प्रोटीन है; हाई या लो अकेले निदान नहीं।", "ar": "الهيموجلوبين هو البروتين الناقل للأكسجين في خلايا الدم الحمراء؛ ارتفاعه أو انخفاضه وحده ليس تشخيصاً."}
    excerpts = {"tr": "Hemoglobin düşüklüğü anemi, yüksekliği ise dehidrasyon veya polisitemi ile ilişkili olabilir. Tek başına teşhis değildir; hekim diğer değerlerle yorumlar.", "en": "Low hemoglobin may indicate anemia, while high hemoglobin can be related to dehydration or polycythemia. Not a diagnosis alone; your doctor interprets with other results.", "es": "La hemoglobina baja puede indicar anemia; alta puede relacionarse con deshidratación o policitemia. No es diagnóstico sola; el médico interpreta con el resto.", "de": "Niedriges Hämoglobin kann Anämie anzeigen; erhöhtes kann mit Dehydration oder Polyzythämie zusammenhängen. Keine Diagnose allein; der Arzt wertet mit anderen Werten.", "fr": "Une hémoglobine basse peut indiquer une anémie ; élevée peut être liée à la déshydratation ou la polyglobulie. Pas un diagnostic seul ; le médecin interprète avec le bilan.", "it": "Un'emoglobina bassa può indicare anemia; alta può essere legata a disidratazione o policitemia. Non diagnosi da sola; il medico valuta con altri risultati.", "he": "המוגלובין נמוך עשוי להצביע על אנמיה; גבוה עשוי לקשור להתייבשות או פוליציטמיה. לא אבחנה לבד; הרופא מפרש עם שאר התוצאות.", "hi": "लो हीमोग्लोबिन एनीमिया का संकेत हो सकता है; हाई डिहाइड्रेशन या पॉलीसिथीमिया से जुड़ सकता है। अकेले निदान नहीं; डॉक्टर अन्य रिजल्ट के साथ व्याख्या करेंगे।", "ar": "انخفاض الهيموجلوبين قد يشير إلى فقر الدم؛ ارتفاعه قد يرتبط بالجفاف أو كثرة الحمر. ليس تشخيصاً وحده؛ الطبيب يفسره مع بقية النتائج."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Hemoglobin yüksekliği ve düşüklüğü nedenleri, normal aralıklar ve belirtiler. Eğitim amaçlı.", "en": "Understand low hemoglobin meaning, high hemoglobin causes, symptoms, and normal ranges. Educational guide for interpreting hemoglobin blood test results.", "es": "Hemoglobina alta o baja: significado, rangos normales y causas. Solo informativo.", "de": "Hämoglobin erhöht oder erniedrigt: Ursachen, Normalwerte und Symptome. Nur zur Information.", "fr": "Hémoglobine haute ou basse : signification, valeurs normales et causes. À titre informatif.", "it": "Emoglobina alta o bassa: significato, range normali e cause. Solo informativo.", "he": "המוגלובין גבוה או נמוך: משמעות, טווחי נורמה וסיבות. למידע בלבד.", "hi": "हाई या लो हीमोग्लोबिन: मतलब, नॉर्मल रेंज और कारण। केवल सूचनार्थ।", "ar": "ارتفاع أو انخفاض الهيموجلوبين: المعنى والنطاقات الطبيعية والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Hemoglobin kan tahlili — Norya", "en": "Hemoglobin blood test — Norya", "es": "Hemoglobina análisis — Norya", "de": "Hämoglobin Bluttest — Norya", "fr": "Hémoglobine bilan sanguin — Norya", "it": "Emoglobina esame del sangue — Norya", "he": "המוגלובין בדיקת דם — Norya", "hi": "हीमोग्लोबिन ब्लड टेस्ट — Norya", "ar": "الهيموجلوبين تحليل دم — Norya"}
    sections_by_lang = get_hemoglobin_sections_by_lang()
    faq_schema_qa = get_hemoglobin_faq_schema_qa()
    return Article(id="hemoglobin-high-or-low", published_at=published, read_minutes=8, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, faq_schema_qa=faq_schema_qa)


def _article_neutrophils() -> Article:
    from app.blog_article_neutrophils_content import get_neutrophils_sections_by_lang, get_neutrophils_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/neutrophils-hero.jpg"
    slugs = {"tr": "notrofil-yuksekligi-dusuklugu-ne-anlama-gelir", "en": "neutrophils-high-or-low-meaning", "es": "neutrofilos-altos-o-bajos-significado", "de": "neutrophile-zu-hoch-oder-niedrig", "fr": "neutrophiles-hauts-ou-bas-signification", "it": "neutrofili-alti-o-bassi-significato", "he": "נויטרופילים-גבוהים-או-נמוכים", "hi": "neutrophils-high-or-low-meaning-hindi", "ar": "ارتفاع-او-انخفاض-النيوتروفيل"}
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Nötrofil yüksekliği veya düşüklüğü ne anlama gelir?", "en": "What does high or low neutrophils mean?", "es": "¿Qué significa tener neutrófilos altos o bajos?", "de": "Neutrophile zu hoch oder zu niedrig: Was bedeutet das?", "fr": "Neutrophiles hauts ou bas : qu'est-ce que ça signifie ?", "it": "Neutrofili alti o bassi: cosa significa?", "he": "מה משמעות נויטרופילים גבוהים או נמוכים?", "hi": "न्यूट्रोफिल्स हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض العدلات (النيوتروفيل)؟"}
    subtitles = {"tr": "Nötrofiller en yaygın beyaz kan hücreleridir; yüksekliği veya düşüklüğü tek başına teşhis değildir.", "en": "Neutrophils are the most common white blood cells; a high or low count alone is not a diagnosis.", "es": "Los neutrófilos son los glóbulos blancos más comunes; un valor alto o bajo por sí solo no es un diagnóstico.", "de": "Neutrophile sind die häufigsten weißen Blutkörperchen; erhöht oder erniedrigt allein ist keine Diagnose.", "fr": "Les neutrophiles sont les globules blancs les plus courants ; un taux élevé ou bas seul ne constitue pas un diagnostic.", "it": "I neutrofili sono i globuli bianchi più comuni; un valore alto o basso da solo non è una diagnosi.", "he": "נויטרופילים הם תאי הדם הלבנים הנפוצים ביותר; ערך גבוה או נמוך לבדו אינו אבחנה.", "hi": "न्यूट्रोफिल्स सबसे आम सफेद रक्त कोशिकाएं हैं; हाई या लो अकेले निदान नहीं।", "ar": "العدلات هي أكثر خلايا الدم البيضاء شيوعاً؛ ارتفاعها أو انخفاضها وحده ليس تشخيصاً."}
    excerpts = {"tr": "Nötrofil yüksekliği enfeksiyon veya iltihap, düşüklüğü ise bağışıklık zayıflığı ile ilişkili olabilir. Tek başına teşhis değildir; hekim tam kan sayımı ve klinikle yorumlar.", "en": "High neutrophils may indicate infection or inflammation; low neutrophils can signal immune suppression. Not a diagnosis alone; your doctor interprets with full blood count and clinical context.", "es": "Neutrófilos altos pueden indicar infección o inflamación; bajos pueden señalar inmunosupresión. No es diagnóstico solo; el médico interpreta con hemograma y contexto.", "de": "Erhöhte Neutrophile können auf Infektion oder Entzündung hinweisen; erniedrigte auf Immunschwäche. Keine Diagnose allein; der Arzt wertet mit dem Blutbild.", "fr": "Des neutrophiles élevés peuvent indiquer une infection ou une inflammation ; bas, une immunosuppression. Pas un diagnostic seul ; le médecin interprète avec la NFS.", "it": "Neutrofili alti possono indicare infezione o infiammazione; bassi possono segnalare immunosoppressione. Non diagnosi da soli; il medico valuta con emocromo.", "he": "נויטרופילים גבוהים עשויים להצביע על זיהום או דלקת; נמוכים עשויים להעיד על דיכוי חיסוני. לא אבחנה לבד; הרופא מפרש עם ספירת הדם.", "hi": "हाई न्यूट्रोफिल्स संक्रमण या सूजन का संकेत हो सकते हैं; लो इम्यून सप्रेशन का। अकेले निदान नहीं; डॉक्टर पूर्ण रक्त गणना के साथ व्याख्या करेंगे।", "ar": "ارتفاع العدلات قد يشير إلى عدوى أو التهاب؛ انخفاضها قد يشير إلى ضعف المناعة. ليس تشخيصاً وحده؛ الطبيب يفسره مع تحليل الدم."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Nötrofil yüksekliği ve düşüklüğü nedenleri, normal aralıklar. Eğitim amaçlı.", "en": "What high or low neutrophils mean, normal ranges, causes. For information only.", "es": "Neutrófilos altos o bajos: significado y causas. Solo informativo.", "de": "Neutrophile erhöht oder erniedrigt: Ursachen und Normalwerte. Nur zur Information.", "fr": "Neutrophiles hauts ou bas : signification et causes. À titre informatif.", "it": "Neutrofili alti o bassi: significato e cause. Solo informativo.", "he": "נויטרופילים גבוהים או נמוכים: משמעות וסיבות. למידע בלבד.", "hi": "हाई या लो न्यूट्रोफिल्स: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع أو انخفاض العدلات: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Nötrofil kan tahlili — Norya", "en": "Neutrophils blood test — Norya", "es": "Neutrófilos análisis — Norya", "de": "Neutrophile Bluttest — Norya", "fr": "Neutrophiles bilan sanguin — Norya", "it": "Neutrofili esame del sangue — Norya", "he": "נויטרופילים בדיקת דם — Norya", "hi": "न्यूट्रोफिल्स ब्लड टेस्ट — Norya", "ar": "العدلات تحليل دم — Norya"}
    sections_by_lang = get_neutrophils_sections_by_lang()
    faq_schema_qa = get_neutrophils_faq_schema_qa()
    return Article(id="neutrophils-high-or-low", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, faq_schema_qa=faq_schema_qa)


def _article_iron_levels() -> Article:
    from app.blog_article_iron_content import get_iron_sections_by_lang, get_iron_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/iron-hero.jpg"
    slugs = {"tr": "demir-dusuklugu-yuksekligi-ne-anlama-gelir", "en": "iron-low-or-high-meaning", "es": "hierro-bajo-o-alto-significado", "de": "eisen-zu-niedrig-oder-hoch", "fr": "fer-bas-ou-eleve-signification", "it": "ferro-basso-o-alto-significato", "he": "ברזל-נמוך-או-גבוה", "hi": "iron-low-or-high-meaning-hindi", "ar": "انخفاض-او-ارتفاع-الحديد"}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "Demir düşüklüğü veya yüksekliği ne anlama gelir?", "en": "What does low or high iron mean?", "es": "¿Qué significa tener el hierro bajo o alto?", "de": "Eisen zu niedrig oder zu hoch: Was bedeutet das?", "fr": "Fer bas ou élevé : qu'est-ce que ça signifie ?", "it": "Ferro basso o alto: cosa significa?", "he": "מה משמעות ברזל נמוך או גבוה?", "hi": "आयरन लो या हाई का क्या मतलब है?", "ar": "ماذا يعني انخفاض أو ارتفاع الحديد؟"}
    subtitles = {"tr": "Serum demiri vücuttaki demir durumunu gösterir; düşük veya yüksek tek başına teşhis değildir.", "en": "Serum iron reflects your body's iron status; low or high alone is not a diagnosis.", "es": "El hierro sérico refleja el estado de hierro corporal; bajo o alto por sí solo no es diagnóstico.", "de": "Serumeisen spiegelt den Eisenstatus wider; niedrig oder hoch allein ist keine Diagnose.", "fr": "Le fer sérique reflète le statut en fer ; bas ou élevé seul ne constitue pas un diagnostic.", "it": "Il ferro sierico riflette lo stato del ferro; basso o alto da solo non è una diagnosi.", "he": "ברזל בסרום משקף את מצב הברזל בגוף; גבוה או נמוך לבדו אינו אבחנה.", "hi": "सीरम आयरन शरीर में आयरन की स्थिति दर्शाता है; लो या हाई अकेले निदान नहीं।", "ar": "الحديد في المصل يعكس حالة الحديد في الجسم؛ منخفض أو مرتفع وحده ليس تشخيصاً."}
    excerpts = {"tr": "Demir düşüklüğü anemi, yüksekliği hemokromatoz ile ilişkili olabilir. Tek başına teşhis değildir; hekim ferritin ve TIBC ile birlikte yorumlar.", "en": "Low iron may indicate anemia; high iron can signal hemochromatosis. Not a diagnosis alone; your doctor interprets with ferritin and TIBC.", "es": "Hierro bajo puede indicar anemia; alto puede señalar hemocromatosis. No es diagnóstico solo; el médico interpreta con ferritina y TIBC.", "de": "Niedriges Eisen kann auf Anämie hinweisen; erhöhtes auf Hämochromatose. Keine Diagnose allein; der Arzt wertet mit Ferritin und TIBC.", "fr": "Un fer bas peut indiquer une anémie ; élevé peut signaler une hémochromatose. Pas un diagnostic seul ; le médecin interprète avec la ferritine et la TIBC.", "it": "Ferro basso può indicare anemia; alto può segnalare emocromatosi. Non diagnosi da solo; il medico valuta con ferritina e TIBC.", "he": "ברזל נמוך עשוי להצביע על אנמיה; גבוה עשוי להעיד על המוכרומטוזיס. לא אבחנה לבד; הרופא מפרש עם פריטין ו-TIBC.", "hi": "लो आयरन एनीमिया का संकेत हो सकता है; हाई हेमोक्रोमैटोसिस का। अकेले निदान नहीं; डॉक्टर फेरिटिन और TIBC के साथ व्याख्या करेंगे।", "ar": "انخفاض الحديد قد يشير إلى فقر الدم؛ ارتفاعه قد يشير إلى داء ترسب الأصبغة الدموية. ليس تشخيصاً وحده؛ الطبيب يفسره مع الفيريتين وTIBC."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Demir düşüklüğü ve yüksekliği nedenleri, ferritin-TIBC ilişkisi. Eğitim amaçlı.", "en": "What low or high iron means, ferritin and TIBC connection, normal ranges. For information only.", "es": "Hierro bajo o alto: significado, ferritina y TIBC. Solo informativo.", "de": "Eisen niedrig oder hoch: Ursachen, Ferritin- und TIBC-Zusammenhang. Nur zur Information.", "fr": "Fer bas ou élevé : signification, lien avec la ferritine et la TIBC. À titre informatif.", "it": "Ferro basso o alto: significato, legame con ferritina e TIBC. Solo informativo.", "he": "ברזל נמוך או גבוה: משמעות, קשר לפריטין ו-TIBC. למידע בלבד.", "hi": "लो या हाई आयरन: मतलब, फेरिटिन और TIBC संबंध। केवल सूचनार्थ।", "ar": "انخفاض أو ارتفاع الحديد: المعنى وعلاقته بالفيريتين وTIBC. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Demir kan tahlili — Norya", "en": "Iron blood test — Norya", "es": "Hierro análisis — Norya", "de": "Eisen Bluttest — Norya", "fr": "Fer bilan sanguin — Norya", "it": "Ferro esame del sangue — Norya", "he": "ברזל בדיקת דם — Norya", "hi": "आयरन ब्लड टेस्ट — Norya", "ar": "الحديد تحليل دم — Norya"}
    sections_by_lang = get_iron_sections_by_lang()
    faq_schema_qa = get_iron_faq_schema_qa()
    return Article(id="iron-low-or-high", published_at=published, read_minutes=8, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, faq_schema_qa=faq_schema_qa)


def _article_bun() -> Article:
    from app.blog_article_bun_content import get_bun_sections_by_lang, get_bun_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/bun-high-hero.jpg"
    slugs = {"tr": "bun-ure-azotu-yuksekligi-ne-anlama-gelir", "en": "bun-high-meaning", "es": "bun-nitrogeno-ureico-alto-significado", "de": "harnstoff-stickstoff-zu-hoch", "fr": "azote-ureique-eleve-signification", "it": "azoto-ureico-alto-significato", "he": "אוריאה-גבוהה", "hi": "bun-high-meaning-hindi", "ar": "ارتفاع-نيتروجين-اليوريا"}
    cat = {"tr": "Böbrek", "en": "Kidney", "es": "Riñón", "de": "Niere", "fr": "Rein", "it": "Rene", "he": "כליות", "hi": "किडनी", "ar": "الكلى"}
    titles = {"tr": "BUN (kan üre azotu) yüksekliği ne anlama gelir?", "en": "What does high BUN (blood urea nitrogen) mean?", "es": "¿Qué significa el BUN alto?", "de": "Harnstoff-Stickstoff (BUN) zu hoch: Was bedeutet das?", "fr": "Azote uréique (BUN) élevé : qu'est-ce que ça signifie ?", "it": "Azoto ureico (BUN) alto: cosa significa?", "he": "מה משמעות BUN (אוריאה בדם) גבוה?", "hi": "हाई BUN (ब्लड यूरिया नाइट्रोजन) का क्या मतलब है?", "ar": "ماذا يعني ارتفاع نيتروجين اليوريا في الدم (BUN)؟"}
    subtitles = {"tr": "BUN böbrek fonksiyonu ve protein metabolizması hakkında bilgi verir; tek başına teşhis değildir.", "en": "BUN provides information about kidney function and protein metabolism; it is not a diagnosis on its own.", "es": "El BUN da información sobre función renal y metabolismo proteico; no es un diagnóstico por sí solo.", "de": "BUN gibt Auskunft über Nierenfunktion und Proteinstoffwechsel; allein keine Diagnose.", "fr": "Le BUN renseigne sur la fonction rénale et le métabolisme protéique ; ce n'est pas un diagnostic en soi.", "it": "Il BUN fornisce informazioni sulla funzione renale e sul metabolismo proteico; non è una diagnosi da solo.", "he": "BUN מספק מידע על תפקוד הכליות ומטבוליזם חלבונים; אינו אבחנה בפני עצמו.", "hi": "BUN किडनी फंक्शन और प्रोटीन मेटाबॉलिज़्म के बारे में जानकारी देता है; अकेले निदान नहीं।", "ar": "BUN يوفر معلومات عن وظائف الكلى وأيض البروتين؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "BUN yüksekliği böbrek sorunları, dehidrasyon veya yüksek proteinli diyetle ilişkili olabilir. Hekim kreatinin ile birlikte yorumlar.", "en": "High BUN may be linked to kidney issues, dehydration, or high-protein diet. Your doctor interprets it with creatinine.", "es": "El BUN alto puede estar ligado a problemas renales, deshidratación o dieta hiperproteica. El médico interpreta con la creatinina.", "de": "Erhöhter BUN kann mit Nierenproblemen, Dehydration oder proteinreicher Ernährung zusammenhängen. Der Arzt wertet mit Kreatinin.", "fr": "Un BUN élevé peut être lié à des problèmes rénaux, à la déshydratation ou à un régime hyperprotéiné. Le médecin interprète avec la créatinine.", "it": "Un BUN alto può essere legato a problemi renali, disidratazione o dieta iperproteica. Il medico valuta con la creatinina.", "he": "BUN גבוה עשוי לקשור לבעיות כליות, התייבשות או תזונה עתירת חלבון. הרופא מפרש עם קראטינין.", "hi": "हाई BUN किडनी समस्या, डिहाइड्रेशन या उच्च प्रोटीन डाइट से जुड़ सकता है। डॉक्टर क्रिएटिनिन के साथ व्याख्या करेंगे।", "ar": "ارتفاع BUN قد يرتبط بمشاكل كلوية أو جفاف أو نظام غذائي عالي البروتين. الطبيب يفسره مع الكرياتينين."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "BUN yüksekliği nedenleri, BUN/kreatinin oranı. Eğitim amaçlı.", "en": "What high BUN means, BUN/creatinine ratio, normal ranges. For information only.", "es": "BUN alto: significado y relación con creatinina. Solo informativo.", "de": "BUN erhöht: Ursachen und BUN/Kreatinin-Verhältnis. Nur zur Information.", "fr": "BUN élevé : signification et rapport BUN/créatinine. À titre informatif.", "it": "BUN alto: significato e rapporto BUN/creatinina. Solo informativo.", "he": "BUN גבוה: משמעות ויחס BUN/קראטינין. למידע בלבד.", "hi": "हाई BUN: मतलब और BUN/क्रिएटिनिन अनुपात। केवल सूचनार्थ।", "ar": "ارتفاع BUN: المعنى ونسبة BUN/الكرياتينين. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "BUN kan tahlili — Norya", "en": "BUN blood test — Norya", "es": "BUN análisis — Norya", "de": "BUN Bluttest — Norya", "fr": "BUN bilan sanguin — Norya", "it": "BUN esame del sangue — Norya", "he": "BUN בדיקת דם — Norya", "hi": "BUN ब्लड टेस्ट — Norya", "ar": "BUN تحليل دم — Norya"}
    sections_by_lang = get_bun_sections_by_lang()
    faq_schema_qa = get_bun_faq_schema_qa()
    return Article(id="bun-high-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, faq_schema_qa=faq_schema_qa)


def _article_plt() -> Article:
    from app.blog_article_plt_content import get_plt_sections_by_lang, get_plt_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/platelets-hero.jpg"
    slugs = {"tr": "trombosit-plt-yuksekligi-dusuklugu", "en": "platelets-high-or-low-meaning", "es": "plaquetas-altas-o-bajas-significado", "de": "thrombozyten-zu-hoch-oder-niedrig", "fr": "plaquettes-hautes-ou-basses-signification", "it": "piastrine-alte-o-basse-significato", "he": "טסיות-גבוהות-או-נמוכות", "hi": "platelets-high-or-low-meaning-hindi", "ar": "ارتفاع-او-انخفاض-الصفائح-الدموية"}
    cat = {"tr": "Kan sayımı", "en": "Complete blood count", "es": "Hemograma", "de": "Blutbild", "fr": "Numération sanguine", "it": "Emocromo", "he": "ספירת דם", "hi": "ब्लड काउंट", "ar": "تحليل الدم"}
    titles = {"tr": "Trombosit (PLT) yüksekliği veya düşüklüğü ne anlama gelir?", "en": "What does high or low platelet count (PLT) mean?", "es": "¿Qué significa tener plaquetas altas o bajas?", "de": "Thrombozyten zu hoch oder zu niedrig: Was bedeutet das?", "fr": "Plaquettes hautes ou basses : qu'est-ce que ça signifie ?", "it": "Piastrine alte o basse: cosa significa?", "he": "מה משמעות ספירת טסיות גבוהה או נמוכה?", "hi": "प्लेटलेट काउंट (PLT) हाई या लो का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض عدد الصفائح الدموية؟"}
    subtitles = {"tr": "Trombositler pıhtılaşma için gereklidir; yüksekliği veya düşüklüğü tek başına teşhis değildir.", "en": "Platelets are essential for blood clotting; a high or low count alone is not a diagnosis.", "es": "Las plaquetas son esenciales para la coagulación; un valor alto o bajo por sí solo no es un diagnóstico.", "de": "Thrombozyten sind für die Blutgerinnung unerlässlich; erhöht oder erniedrigt allein ist keine Diagnose.", "fr": "Les plaquettes sont essentielles à la coagulation ; un taux élevé ou bas seul ne constitue pas un diagnostic.", "it": "Le piastrine sono essenziali per la coagulazione; un valore alto o basso da solo non è una diagnosi.", "he": "טסיות חיוניות לקרישת הדם; ספירה גבוהה או נמוכה לבדה אינה אבחנה.", "hi": "प्लेटलेट्स रक्त के थक्के बनने के लिए आवश्यक हैं; हाई या लो अकेले निदान नहीं।", "ar": "الصفائح الدموية ضرورية لتخثر الدم؛ ارتفاعها أو انخفاضها وحده ليس تشخيصاً."}
    excerpts = {"tr": "Trombosit yüksekliği enfeksiyon veya iltihap, düşüklüğü ise ITP veya ilaçlarla ilişkili olabilir. Hekim tam kan sayımıyla birlikte yorumlar.", "en": "High platelets may be linked to infection or inflammation; low platelets may signal ITP or medication effects. Your doctor interprets with full blood count.", "es": "Plaquetas altas pueden asociarse a infección o inflamación; bajas pueden señalar PTI o efectos de medicamentos. El médico interpreta con hemograma.", "de": "Erhöhte Thrombozyten können mit Infektion oder Entzündung zusammenhängen; erniedrigte mit ITP oder Medikamenten. Der Arzt wertet mit dem Blutbild.", "fr": "Des plaquettes élevées peuvent être liées à une infection ou une inflammation ; basses, à un PTI ou des médicaments. Le médecin interprète avec la NFS.", "it": "Piastrine alte possono essere legate a infezione o infiammazione; basse possono segnalare ITP o effetti farmacologici. Il medico valuta con emocromo.", "he": "טסיות גבוהות עשויות לקשור לזיהום או דלקת; נמוכות עשויות להעיד על ITP או השפעת תרופות. הרופא מפרש עם ספירת הדם.", "hi": "हाई प्लेटलेट्स संक्रमण या सूजन से जुड़ सकते हैं; लो ITP या दवा प्रभाव का संकेत हो सकता है। डॉक्टर पूर्ण रक्त गणना के साथ व्याख्या करेंगे।", "ar": "ارتفاع الصفائح قد يرتبط بعدوى أو التهاب؛ انخفاضها قد يشير إلى ITP أو تأثير أدوية. الطبيب يفسره مع تحليل الدم الكامل."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Trombosit yüksekliği ve düşüklüğü nedenleri, MPV ilişkisi. Eğitim amaçlı.", "en": "What high or low platelets mean, MPV connection, normal ranges. For information only.", "es": "Plaquetas altas o bajas: significado y conexión con VPM. Solo informativo.", "de": "Thrombozyten erhöht oder erniedrigt: Ursachen und MPV-Zusammenhang. Nur zur Information.", "fr": "Plaquettes hautes ou basses : signification et lien avec le VPM. À titre informatif.", "it": "Piastrine alte o basse: significato e legame con MPV. Solo informativo.", "he": "טסיות גבוהות או נמוכות: משמעות וקשר ל-MPV. למידע בלבד.", "hi": "हाई या लो प्लेटलेट्स: मतलब और MPV संबंध। केवल सूचनार्थ।", "ar": "ارتفاع أو انخفاض الصفائح: المعنى وعلاقته بـ MPV. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Trombosit PLT kan tahlili — Norya", "en": "Platelet PLT blood test — Norya", "es": "Plaquetas análisis — Norya", "de": "Thrombozyten Bluttest — Norya", "fr": "Plaquettes bilan sanguin — Norya", "it": "Piastrine esame del sangue — Norya", "he": "טסיות בדיקת דם — Norya", "hi": "प्लेटलेट PLT ब्लड टेस्ट — Norya", "ar": "الصفائح الدموية تحليل دم — Norya"}
    sections_by_lang = get_plt_sections_by_lang()
    faq_schema_qa = get_plt_faq_schema_qa()
    return Article(id="plt-high-or-low", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, faq_schema_qa=faq_schema_qa)


def _article_t3_t4() -> Article:
    from app.blog_article_t3_t4_content import get_t3_t4_sections_by_lang, get_t3_t4_faq_schema_qa
    published = date(2026, 3, 24)
    cover = "/static/images/blog/t3-t4-thyroid-hero.jpg"
    slugs = {"tr": "t3-t4-tiroid-hormonu-ne-anlama-gelir", "en": "t3-t4-thyroid-meaning", "es": "t3-t4-tiroides-significado", "de": "t3-t4-schilddruese-bedeutung", "fr": "t3-t4-thyroide-signification", "it": "t3-t4-tiroide-significato", "he": "t3-t4-בלוטת-התריס", "hi": "t3-t4-thyroid-meaning-hindi", "ar": "هرمونات-الغدة-الدرقية-t3-t4"}
    cat = {"tr": "Tiroid", "en": "Thyroid", "es": "Tiroides", "de": "Schilddrüse", "fr": "Thyroïde", "it": "Tiroide", "he": "בלוטת התריס", "hi": "थायरॉइड", "ar": "الغدة الدرقية"}
    titles = {"tr": "T3 ve T4 tiroid hormonları ne anlama gelir?", "en": "T3 and T4 Meaning: Thyroid Hormones Explained", "es": "¿Qué significan las hormonas tiroideas T3 y T4?", "de": "Was bedeuten die Schilddrüsenhormone T3 und T4?", "fr": "Que signifient les hormones thyroïdiennes T3 et T4 ?", "it": "Cosa significano gli ormoni tiroidei T3 e T4?", "he": "מה משמעות הורמוני בלוטת התריס T3 ו-T4?", "hi": "T3 और T4 थायरॉइड हार्मोन का क्या मतलब है?", "ar": "ماذا تعني هرمونات الغدة الدرقية T3 وT4؟"}
    subtitles = {"tr": "T3 ve T4 metabolizmayı düzenleyen tiroid hormonlarıdır; yüksekliği veya düşüklüğü tek başına teşhis değildir.", "en": "Understand what T3 and T4 mean, how they relate to TSH, and what abnormal thyroid hormone results may suggest.", "es": "T3 y T4 son hormonas tiroideas que regulan el metabolismo; altas o bajas por sí solas no son diagnóstico.", "de": "T3 und T4 sind Schilddrüsenhormone, die den Stoffwechsel regulieren; erhöht oder erniedrigt allein ist keine Diagnose.", "fr": "T3 et T4 sont des hormones thyroïdiennes régulant le métabolisme ; élevées ou basses seules ne constituent pas un diagnostic.", "it": "T3 e T4 sono ormoni tiroidei che regolano il metabolismo; alti o bassi da soli non sono una diagnosi.", "he": "T3 ו-T4 הם הורמוני תריס המווסתים את חילוף החומרים; גבוהים או נמוכים לבדם אינם אבחנה.", "hi": "T3 और T4 मेटाबॉलिज़्म को नियंत्रित करने वाले थायरॉइड हार्मोन हैं; हाई या लो अकेले निदान नहीं।", "ar": "T3 وT4 هرمونات الغدة الدرقية التي تنظم الأيض؛ ارتفاعها أو انخفاضها وحده ليس تشخيصاً."}
    excerpts = {"tr": "T3 ve T4 tiroid fonksiyonunu gösterir; TSH ile birlikte değerlendirilir. Yükseklik hipertiroidizm, düşüklük hipotiroidizm işareti olabilir.", "en": "T3 and T4 indicate thyroid function and are evaluated together with TSH. High levels may signal hyperthyroidism; low levels hypothyroidism.", "es": "T3 y T4 indican función tiroidea y se evalúan con TSH. Niveles altos pueden señalar hipertiroidismo; bajos, hipotiroidismo.", "de": "T3 und T4 zeigen die Schilddrüsenfunktion an und werden mit TSH bewertet. Erhöhte Werte können Hyperthyreose anzeigen; erniedrigte Hypothyreose.", "fr": "T3 et T4 indiquent la fonction thyroïdienne et sont évalués avec la TSH. Des taux élevés peuvent signaler une hyperthyroïdie ; bas, une hypothyroïdie.", "it": "T3 e T4 indicano la funzione tiroidea e si valutano con il TSH. Livelli alti possono segnalare ipertiroidismo; bassi ipotiroidismo.", "he": "T3 ו-T4 מעידים על תפקוד בלוטת התריס ומוערכים יחד עם TSH. רמות גבוהות עשויות להצביע על יתר פעילות; נמוכות על תת-פעילות.", "hi": "T3 और T4 थायरॉइड फंक्शन दर्शाते हैं और TSH के साथ मूल्यांकन होता है। हाई हाइपरथायरॉइडिज़्म; लो हाइपोथायरॉइडिज़्म का संकेत हो सकता है।", "ar": "T3 وT4 يشيران إلى وظائف الغدة الدرقية ويُقيَّمان مع TSH. مستويات مرتفعة قد تشير إلى فرط نشاط؛ منخفضة إلى قصور."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "T3 ve T4 tiroid hormonları, TSH ilişkisi, normal aralıklar. Eğitim amaçlı.", "en": "Understand T3 and T4 meaning, thyroid hormone patterns, TSH connection, and what high or low thyroid results may suggest. Educational guide only.", "es": "Hormonas tiroideas T3 y T4: significado y relación con TSH. Solo informativo.", "de": "T3 und T4 Schilddrüsenhormone: Bedeutung und TSH-Zusammenhang. Nur zur Information.", "fr": "Hormones thyroïdiennes T3 et T4 : signification et lien avec la TSH. À titre informatif.", "it": "Ormoni tiroidei T3 e T4: significato e connessione con TSH. Solo informativo.", "he": "הורמוני תריס T3 ו-T4: משמעות וקשר ל-TSH. למידע בלבד.", "hi": "T3 और T4 थायरॉइड हार्मोन: मतलब और TSH संबंध। केवल सूचनार्थ।", "ar": "هرمونات الغدة الدرقية T3 وT4: المعنى وعلاقتها بـ TSH. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "T3 T4 tiroid kan tahlili — Norya", "en": "T3 T4 thyroid blood test — Norya", "es": "T3 T4 tiroides análisis — Norya", "de": "T3 T4 Schilddrüse Bluttest — Norya", "fr": "T3 T4 thyroïde bilan sanguin — Norya", "it": "T3 T4 tiroide esame del sangue — Norya", "he": "T3 T4 בלוטת התריס בדיקת דם — Norya", "hi": "T3 T4 थायरॉइड ब्लड टेस्ट — Norya", "ar": "T3 T4 الغدة الدرقية تحليل دم — Norya"}
    sections_by_lang = get_t3_t4_sections_by_lang()
    faq_schema_qa = get_t3_t4_faq_schema_qa()
    return Article(id="t3-t4-thyroid-meaning", published_at=published, read_minutes=8, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=sections_by_lang, faq_schema_qa=faq_schema_qa)


_ARTICLE_HEMOGLOBIN = _article_hemoglobin()
_ARTICLE_NEUTROPHILS = _article_neutrophils()
_ARTICLE_IRON_LEVELS = _article_iron_levels()
_ARTICLE_BUN = _article_bun()
_ARTICLE_PLT = _article_plt()
_ARTICLE_T3_T4 = _article_t3_t4()


def _article_psa() -> Article:
    from app.blog_article_psa_content import get_psa_sections_by_lang, get_psa_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/psa-hero.jpg"
    slugs = {"tr": "psa-testi-ne-anlama-gelir", "en": "psa-test-meaning", "es": "prueba-psa-significado", "de": "psa-test-bedeutung", "fr": "test-psa-signification", "it": "test-psa-significato", "he": "בדיקת-psa-משמעות", "hi": "psa-test-meaning-hindi", "ar": "اختبار-psa-المعنى"}
    cat = {"tr": "Prostat", "en": "Prostate", "es": "Próstata", "de": "Prostata", "fr": "Prostate", "it": "Prostata", "he": "ערמונית", "hi": "प्रोस्टेट", "ar": "البروستاتا"}
    titles = {"tr": "PSA testi: yüksek PSA ne anlama gelir?", "en": "PSA test: what does a high PSA level mean?", "es": "Prueba de PSA: ¿qué significa un PSA alto?", "de": "PSA-Test: Was bedeutet ein erhöhter PSA-Wert?", "fr": "Test PSA : que signifie un taux de PSA élevé ?", "it": "Test del PSA: cosa significa un PSA alto?", "he": "בדיקת PSA: מה משמעות ערך PSA גבוה?", "hi": "PSA टेस्ट: हाई PSA का क्या मतलब है?", "ar": "اختبار PSA: ماذا يعني ارتفاع مستوى PSA؟"}
    subtitles = {"tr": "PSA prostat bezinden salgılanan bir proteindir; yüksekliği tek başına kanser anlamına gelmez.", "en": "PSA is a protein produced by the prostate gland; a high level alone does not mean cancer.", "es": "El PSA es una proteína producida por la próstata; un nivel alto por sí solo no significa cáncer.", "de": "PSA ist ein Protein der Prostata; ein erhöhter Wert allein bedeutet nicht Krebs.", "fr": "Le PSA est une protéine produite par la prostate ; un taux élevé seul ne signifie pas cancer.", "it": "Il PSA è una proteina prodotta dalla prostata; un valore alto da solo non significa cancro.", "he": "PSA הוא חלבון המיוצר על ידי הערמונית; ערך גבוה לבדו אינו אומר סרטן.", "hi": "PSA प्रोस्टेट ग्रंथि द्वारा उत्पादित प्रोटीन है; हाई लेवल अकेले कैंसर नहीं।", "ar": "PSA بروتين تفرزه غدة البروستاتا؛ ارتفاعه وحده لا يعني السرطان."}
    excerpts = {"tr": "PSA yüksekliği prostat büyümesi, enfeksiyon veya kanser dahil birçok nedene bağlı olabilir. Hekim PSA sonucunu klinik bağlamla yorumlar.", "en": "High PSA may be linked to prostate enlargement, infection, or cancer. Your doctor interprets PSA with clinical context.", "es": "El PSA alto puede deberse a agrandamiento prostático, infección o cáncer. El médico interpreta el PSA en contexto clínico.", "de": "Erhöhter PSA kann mit Prostatavergrößerung, Infektion oder Krebs zusammenhängen. Der Arzt interpretiert den PSA im klinischen Kontext.", "fr": "Un PSA élevé peut être lié à une hypertrophie prostatique, une infection ou un cancer. Le médecin interprète le PSA en contexte clinique.", "it": "Un PSA alto può essere legato a ingrossamento prostatico, infezione o cancro. Il medico interpreta il PSA nel contesto clinico.", "he": "PSA גבוה עשוי לקשור להגדלת ערמונית, זיהום או סרטן. הרופא מפרש את ה-PSA בהקשר קליני.", "hi": "हाई PSA प्रोस्टेट बढ़ने, संक्रमण या कैंसर से जुड़ सकता है। डॉक्टर PSA की क्लिनिकल संदर्भ में व्याख्या करेंगे।", "ar": "ارتفاع PSA قد يرتبط بتضخم البروستاتا أو العدوى أو السرطان. الطبيب يفسر PSA في السياق السريري."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "PSA testi ve yüksek PSA nedenleri, normal aralıklar. Eğitim amaçlı.", "en": "PSA test meaning, high PSA causes, normal ranges. For information only.", "es": "Prueba de PSA: significado y causas de PSA alto. Solo informativo.", "de": "PSA-Test: Bedeutung und Ursachen für erhöhten PSA. Nur zur Information.", "fr": "Test PSA : signification et causes d'un PSA élevé. À titre informatif.", "it": "Test del PSA: significato e cause di PSA alto. Solo informativo.", "he": "בדיקת PSA: משמעות וסיבות ל-PSA גבוה. למידע בלבד.", "hi": "PSA टेस्ट: मतलब और हाई PSA के कारण। केवल सूचनार्थ।", "ar": "اختبار PSA: المعنى وأسباب ارتفاعه. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "PSA prostat kan tahlili — Norya", "en": "PSA prostate blood test — Norya", "es": "PSA análisis de próstata — Norya", "de": "PSA Prostata Bluttest — Norya", "fr": "PSA bilan prostate — Norya", "it": "PSA esame prostata — Norya", "he": "PSA בדיקת ערמונית — Norya", "hi": "PSA प्रोस्टेट ब्लड टेस्ट — Norya", "ar": "PSA تحليل البروستاتا — Norya"}
    return Article(id="psa-test-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_psa_sections_by_lang(), faq_schema_qa=get_psa_faq_schema_qa())


def _article_estradiol() -> Article:
    from app.blog_article_estradiol_content import get_estradiol_sections_by_lang, get_estradiol_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/estradiol-hero.jpg"
    slugs = {"tr": "estradiol-ostrojen-testi-ne-anlama-gelir", "en": "estradiol-estrogen-test-meaning", "es": "estradiol-estrogeno-significado", "de": "oestradiol-oestrogen-test-bedeutung", "fr": "oestradiol-oestrogene-signification", "it": "estradiolo-estrogeni-significato", "he": "אסטרדיול-אסטרוגן-משמעות", "hi": "estradiol-estrogen-test-hindi", "ar": "اختبار-الاستراديول-الاستروجين"}
    cat = {"tr": "Hormonlar", "en": "Hormones", "es": "Hormonas", "de": "Hormone", "fr": "Hormones", "it": "Ormoni", "he": "הורמונים", "hi": "हार्मोन", "ar": "الهرمونات"}
    titles = {"tr": "Estradiol (östrojen) testi: düşük veya yüksek östrojen ne anlama gelir?", "en": "Estradiol (estrogen) test: what do low or high estrogen levels mean?", "es": "Prueba de estradiol: ¿qué significan niveles altos o bajos de estrógeno?", "de": "Östradiol-Test: Was bedeuten niedrige oder hohe Östrogenspiegel?", "fr": "Test d'œstradiol : que signifient des niveaux d'œstrogène bas ou élevés ?", "it": "Test dell'estradiolo: cosa significano livelli alti o bassi di estrogeni?", "he": "בדיקת אסטרדיול: מה משמעות רמות אסטרוגן גבוהות או נמוכות?", "hi": "एस्ट्राडियोल टेस्ट: लो या हाई एस्ट्रोजन का क्या मतलब है?", "ar": "اختبار الاستراديول: ماذا يعني ارتفاع أو انخفاض الإستروجين؟"}
    subtitles = {"tr": "Estradiol (E2) kadınlarda üreme sağlığı ve menopoz için kritik bir hormondur; tek başına teşhis değildir.", "en": "Estradiol (E2) is a critical hormone for reproductive health and menopause; it is not a diagnosis on its own.", "es": "El estradiol (E2) es una hormona crítica para la salud reproductiva y la menopausia; no es un diagnóstico por sí solo.", "de": "Östradiol (E2) ist ein wichtiges Hormon für reproduktive Gesundheit und Menopause; allein keine Diagnose.", "fr": "L'œstradiol (E2) est une hormone clé pour la santé reproductive et la ménopause ; ce n'est pas un diagnostic en soi.", "it": "L'estradiolo (E2) è un ormone fondamentale per la salute riproduttiva e la menopausa; non è una diagnosi da solo.", "he": "אסטרדיול (E2) הוא הורמון קריטי לבריאות הפוריות ולגיל המעבר; אינו אבחנה בפני עצמו.", "hi": "एस्ट्राडियोल (E2) प्रजनन स्वास्थ्य और मेनोपॉज़ के लिए महत्वपूर्ण हार्मोन है; अकेले निदान नहीं।", "ar": "الاستراديول (E2) هرمون حاسم للصحة الإنجابية وانقطاع الطمث؛ ليس تشخيصاً بمفرده."}
    excerpts = {"tr": "Düşük östrojen menopoz, yüksek östrojen PCOS veya obezite ile ilişkili olabilir. Hekim sonucu klinikle yorumlar.", "en": "Low estrogen may relate to menopause; high estrogen to PCOS or obesity. Your doctor interprets with clinical context.", "es": "Estrógeno bajo puede relacionarse con menopausia; alto con SOP u obesidad. El médico interpreta con el contexto.", "de": "Niedriger Östrogenspiegel kann mit Menopause zusammenhängen; hoher mit PCOS oder Übergewicht. Der Arzt interpretiert im klinischen Kontext.", "fr": "Un œstrogène bas peut être lié à la ménopause ; élevé au SOPK ou à l'obésité. Le médecin interprète en contexte.", "it": "Estrogeni bassi possono essere legati alla menopausa; alti a PCOS o obesità. Il medico valuta nel contesto clinico.", "he": "אסטרוגן נמוך עשוי לקשור לגיל המעבר; גבוה ל-PCOS או השמנה. הרופא מפרש בהקשר קליני.", "hi": "लो एस्ट्रोजन मेनोपॉज़ से; हाई PCOS या मोटापे से जुड़ सकता है। डॉक्टर क्लिनिकल संदर्भ में व्याख्या करेंगे।", "ar": "انخفاض الإستروجين قد يرتبط بانقطاع الطمث؛ ارتفاعه بمتلازمة تكيس المبايض أو السمنة. الطبيب يفسره في السياق السريري."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Estradiol testi, östrojen düşüklüğü ve yüksekliği nedenleri. Eğitim amaçlı.", "en": "Estradiol test meaning, low and high estrogen causes, normal ranges. For information only.", "es": "Prueba de estradiol: significado y causas. Solo informativo.", "de": "Östradiol-Test: Bedeutung und Ursachen. Nur zur Information.", "fr": "Test d'œstradiol : signification et causes. À titre informatif.", "it": "Test dell'estradiolo: significato e cause. Solo informativo.", "he": "בדיקת אסטרדיול: משמעות וסיבות. למידע בלבד.", "hi": "एस्ट्राडियोल टेस्ट: मतलब और कारण। केवल सूचनार्थ।", "ar": "اختبار الاستراديول: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Estradiol östrojen kan tahlili — Norya", "en": "Estradiol estrogen blood test — Norya", "es": "Estradiol estrógeno análisis — Norya", "de": "Östradiol Östrogen Bluttest — Norya", "fr": "Œstradiol œstrogène bilan sanguin — Norya", "it": "Estradiolo estrogeni esame — Norya", "he": "אסטרדיול אסטרוגן בדיקת דם — Norya", "hi": "एस्ट्राडियोल एस्ट्रोजन ब्लड टेस्ट — Norya", "ar": "الاستراديول الإستروجين تحليل دم — Norya"}
    return Article(id="estradiol-estrogen-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_estradiol_sections_by_lang(), faq_schema_qa=get_estradiol_faq_schema_qa())


def _article_progesterone() -> Article:
    from app.blog_article_progesterone_content import get_progesterone_sections_by_lang, get_progesterone_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/progesterone-hero.jpg"
    slugs = {"tr": "progesteron-testi-ne-anlama-gelir", "en": "progesterone-test-meaning", "es": "prueba-progesterona-significado", "de": "progesteron-test-bedeutung", "fr": "test-progesterone-signification", "it": "test-progesterone-significato", "he": "בדיקת-פרוגסטרון-משמעות", "hi": "progesterone-test-meaning-hindi", "ar": "اختبار-البروجسترون-المعنى"}
    cat = {"tr": "Hormonlar", "en": "Hormones", "es": "Hormonas", "de": "Hormone", "fr": "Hormones", "it": "Ormoni", "he": "הורמונים", "hi": "हार्मोन", "ar": "الهرمونات"}
    titles = {"tr": "Progesteron testi: düşük progesteron ne anlama gelir?", "en": "Progesterone test: what does low progesterone mean?", "es": "Prueba de progesterona: ¿qué significa la progesterona baja?", "de": "Progesteron-Test: Was bedeutet ein niedriger Progesteronspiegel?", "fr": "Test de progestérone : que signifie une progestérone basse ?", "it": "Test del progesterone: cosa significa il progesterone basso?", "he": "בדיקת פרוגסטרון: מה משמעות פרוגסטרון נמוך?", "hi": "प्रोजेस्टेरोन टेस्ट: लो प्रोजेस्टेरोन का क्या मतलब है?", "ar": "اختبار البروجسترون: ماذا يعني انخفاض البروجسترون؟"}
    subtitles = {"tr": "Progesteron hamilelik ve menstrüel döngü için kritik bir hormondur; düşüklüğü veya yüksekliği tek başına teşhis değildir.", "en": "Progesterone is a critical hormone for pregnancy and the menstrual cycle; low or high alone is not a diagnosis.", "es": "La progesterona es una hormona esencial para el embarazo y el ciclo menstrual; baja o alta por sí sola no es diagnóstico.", "de": "Progesteron ist ein Schlüsselhormon für Schwangerschaft und Menstruationszyklus; niedrig oder hoch allein ist keine Diagnose.", "fr": "La progestérone est une hormone clé pour la grossesse et le cycle menstruel ; basse ou élevée seule ne constitue pas un diagnostic.", "it": "Il progesterone è un ormone fondamentale per gravidanza e ciclo mestruale; basso o alto da solo non è una diagnosi.", "he": "פרוגסטרון הוא הורמון קריטי להריון ולמחזור החודשי; ערך גבוה או נמוך לבדו אינו אבחנה.", "hi": "प्रोजेस्टेरोन गर्भावस्था और मासिक धर्म चक्र के लिए महत्वपूर्ण हार्मोन है; लो या हाई अकेले निदान नहीं।", "ar": "البروجسترون هرمون حاسم للحمل والدورة الشهرية؛ انخفاضه أو ارتفاعه وحده ليس تشخيصاً."}
    excerpts = {"tr": "Düşük progesteron düşük riski veya anovülasyon ile ilişkili olabilir. Hekim sonucu HCG ve ultrason ile birlikte yorumlar.", "en": "Low progesterone may indicate miscarriage risk or anovulation. Your doctor interprets with HCG and ultrasound.", "es": "Progesterona baja puede indicar riesgo de aborto o anovulación. El médico interpreta con HCG y ecografía.", "de": "Niedriger Progesteronspiegel kann auf Fehlgeburtsrisiko oder Anovulation hinweisen. Der Arzt wertet mit HCG und Ultraschall.", "fr": "Une progestérone basse peut indiquer un risque de fausse couche ou d'anovulation. Le médecin interprète avec HCG et échographie.", "it": "Progesterone basso può indicare rischio di aborto o anovulazione. Il medico valuta con HCG ed ecografia.", "he": "פרוגסטרון נמוך עשוי להצביע על סיכון להפלה או אנובולציה. הרופא מפרש עם HCG ואולטרסאונד.", "hi": "लो प्रोजेस्टेरोन गर्भपात जोखिम या एनोव्यूलेशन का संकेत हो सकता है। डॉक्टर HCG और अल्ट्रासाउंड के साथ व्याख्या करेंगे।", "ar": "انخفاض البروجسترون قد يشير إلى خطر الإجهاض أو عدم الإباضة. الطبيب يفسره مع HCG والموجات فوق الصوتية."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Progesteron testi, düşük progesteron nedenleri, hamilelikte progesteron. Eğitim amaçlı.", "en": "Progesterone test meaning, low progesterone causes, pregnancy. For information only.", "es": "Prueba de progesterona: significado y causas. Solo informativo.", "de": "Progesteron-Test: Bedeutung und Ursachen. Nur zur Information.", "fr": "Test de progestérone : signification et causes. À titre informatif.", "it": "Test del progesterone: significato e cause. Solo informativo.", "he": "בדיקת פרוגסטרון: משמעות וסיבות. למידע בלבד.", "hi": "प्रोजेस्टेरोन टेस्ट: मतलब और कारण। केवल सूचनार्थ।", "ar": "اختبار البروجسترون: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Progesteron kan tahlili — Norya", "en": "Progesterone blood test — Norya", "es": "Progesterona análisis — Norya", "de": "Progesteron Bluttest — Norya", "fr": "Progestérone bilan sanguin — Norya", "it": "Progesterone esame — Norya", "he": "פרוגסטרון בדיקת דם — Norya", "hi": "प्रोजेस्टेरोन ब्लड टेस्ट — Norya", "ar": "البروجسترون تحليل دم — Norya"}
    return Article(id="progesterone-test-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_progesterone_sections_by_lang(), faq_schema_qa=get_progesterone_faq_schema_qa())


def _article_beta_hcg() -> Article:
    from app.blog_article_beta_hcg_content import get_beta_hcg_sections_by_lang, get_beta_hcg_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/beta-hcg-hero.jpg"
    slugs = {"tr": "beta-hcg-testi-ne-anlama-gelir", "en": "beta-hcg-test-meaning", "es": "beta-hcg-prueba-significado", "de": "beta-hcg-test-bedeutung", "fr": "beta-hcg-test-signification", "it": "beta-hcg-test-significato", "he": "בדיקת-בטא-hcg-משמעות", "hi": "beta-hcg-test-meaning-hindi", "ar": "اختبار-بيتا-hcg-المعنى"}
    cat = {"tr": "Hamilelik", "en": "Pregnancy", "es": "Embarazo", "de": "Schwangerschaft", "fr": "Grossesse", "it": "Gravidanza", "he": "הריון", "hi": "गर्भावस्था", "ar": "الحمل"}
    titles = {"tr": "Beta-HCG testi: hamilelik kan testi ne anlama gelir?", "en": "Beta-HCG test: what does the pregnancy blood test mean?", "es": "Prueba de beta-HCG: ¿qué significa el análisis de sangre de embarazo?", "de": "Beta-HCG-Test: Was bedeutet der Schwangerschaftsbluttest?", "fr": "Test bêta-HCG : que signifie la prise de sang de grossesse ?", "it": "Test beta-HCG: cosa significa l'esame del sangue per la gravidanza?", "he": "בדיקת בטא HCG: מה משמעות בדיקת הדם להריון?", "hi": "बीटा HCG टेस्ट: प्रेगनेंसी ब्लड टेस्ट का क्या मतलब है?", "ar": "اختبار بيتا HCG: ماذا يعني تحليل دم الحمل؟"}
    subtitles = {"tr": "Beta-HCG hamileliğin en erken biyokimyasal belirtecidir; haftalara göre yükselen değerler gebelik takibinde kullanılır.", "en": "Beta-HCG is the earliest biochemical marker of pregnancy; rising levels by week are used to monitor gestation.", "es": "La beta-HCG es el marcador bioquímico más temprano del embarazo; los niveles ascendentes por semana se usan para monitorear la gestación.", "de": "Beta-HCG ist der früheste biochemische Marker einer Schwangerschaft; steigende Werte pro Woche dienen der Schwangerschaftsüberwachung.", "fr": "La bêta-HCG est le marqueur biochimique le plus précoce de la grossesse ; les taux croissants par semaine servent au suivi.", "it": "La beta-HCG è il primo marcatore biochimico della gravidanza; i livelli crescenti per settimana servono al monitoraggio.", "he": "בטא HCG הוא הסמן הביוכימי המוקדם ביותר להריון; רמות עולות לפי שבוע משמשות למעקב.", "hi": "बीटा HCG गर्भावस्था का सबसे प्रारंभिक बायोकेमिकल मार्कर है; हफ्ते के हिसाब से बढ़ते लेवल मॉनिटरिंग के लिए उपयोग होते हैं।", "ar": "بيتا HCG هو أول مؤشر بيوكيميائي للحمل؛ المستويات المتصاعدة أسبوعياً تُستخدم لمتابعة الحمل."}
    excerpts = {"tr": "Beta-HCG hamilelik teyidi ve takibinde kullanılır. Düşük HCG dış gebelik veya düşük riski, yüksek HCG çoğul gebelik işareti olabilir.", "en": "Beta-HCG confirms and monitors pregnancy. Low HCG may signal ectopic pregnancy; high HCG may indicate multiples.", "es": "La beta-HCG confirma y monitorea el embarazo. HCG baja puede señalar embarazo ectópico; alta puede indicar embarazo múltiple.", "de": "Beta-HCG bestätigt und überwacht die Schwangerschaft. Niedriger HCG kann ektope Schwangerschaft anzeigen; hoher HCG Mehrlingsschwangerschaft.", "fr": "La bêta-HCG confirme et surveille la grossesse. Un HCG bas peut signaler une grossesse extra-utérine ; élevé, une grossesse multiple.", "it": "La beta-HCG conferma e monitora la gravidanza. HCG basso può segnalare gravidanza ectopica; alto gravidanza multipla.", "he": "בטא HCG מאשר ועוקב אחר הריון. HCG נמוך עשוי להצביע על הריון חוץ-רחמי; גבוה על הריון מרובה עוברים.", "hi": "बीटा HCG प्रेगनेंसी की पुष्टि और मॉनिटरिंग करता है। लो HCG एक्टोपिक प्रेगनेंसी; हाई HCG मल्टीपल प्रेगनेंसी का संकेत हो सकता है।", "ar": "بيتا HCG يؤكد ويراقب الحمل. HCG منخفض قد يشير إلى حمل خارج الرحم؛ مرتفع إلى حمل متعدد."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Beta-HCG testi, haftalara göre HCG değerleri, hamilelik kan testi. Eğitim amaçlı.", "en": "Beta-HCG test, HCG levels by week, pregnancy blood test. For information only.", "es": "Beta-HCG: niveles por semana y prueba de embarazo en sangre. Solo informativo.", "de": "Beta-HCG-Test: HCG-Werte nach Woche, Schwangerschaftsbluttest. Nur zur Information.", "fr": "Test bêta-HCG : taux par semaine, prise de sang grossesse. À titre informatif.", "it": "Test beta-HCG: livelli per settimana, esame gravidanza. Solo informativo.", "he": "בדיקת בטא HCG: רמות לפי שבוע, בדיקת דם להריון. למידע בלבד.", "hi": "बीटा HCG टेस्ट: हफ्ते के हिसाब से लेवल। केवल सूचनार्थ।", "ar": "اختبار بيتا HCG: المستويات حسب الأسبوع. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Beta-HCG hamilelik kan tahlili — Norya", "en": "Beta-HCG pregnancy blood test — Norya", "es": "Beta-HCG análisis embarazo — Norya", "de": "Beta-HCG Schwangerschaft Bluttest — Norya", "fr": "Bêta-HCG bilan grossesse — Norya", "it": "Beta-HCG esame gravidanza — Norya", "he": "בטא HCG בדיקת דם הריון — Norya", "hi": "बीटा HCG प्रेगनेंसी ब्लड टेस्ट — Norya", "ar": "بيتا HCG تحليل دم الحمل — Norya"}
    return Article(id="beta-hcg-test-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_beta_hcg_sections_by_lang(), faq_schema_qa=get_beta_hcg_faq_schema_qa())


def _article_troponin() -> Article:
    from app.blog_article_troponin_content import get_troponin_sections_by_lang, get_troponin_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/troponin-hero.jpg"
    slugs = {"tr": "troponin-testi-ne-anlama-gelir", "en": "troponin-test-meaning", "es": "troponina-significado", "de": "troponin-test-bedeutung", "fr": "troponine-signification", "it": "troponina-significato", "he": "טרופונין-משמעות", "hi": "troponin-test-meaning-hindi", "ar": "اختبار-التروبونين-المعنى"}
    cat = {"tr": "Kalp", "en": "Heart", "es": "Corazón", "de": "Herz", "fr": "Cœur", "it": "Cuore", "he": "לב", "hi": "हृदय", "ar": "القلب"}
    titles = {"tr": "Troponin testi: yüksek troponin ne anlama gelir?", "en": "Troponin test: what does high troponin mean?", "es": "Troponina: ¿qué significa la troponina alta?", "de": "Troponin-Test: Was bedeutet ein erhöhter Troponinwert?", "fr": "Test de troponine : que signifie une troponine élevée ?", "it": "Troponina: cosa significa la troponina alta?", "he": "בדיקת טרופונין: מה משמעות טרופונין גבוה?", "hi": "ट्रोपोनिन टेस्ट: हाई ट्रोपोनिन का क्या मतलब है?", "ar": "اختبار التروبونين: ماذا يعني ارتفاع التروبونين؟"}
    subtitles = {"tr": "Troponin kalp kası hasarının en hassas belirtecidir; yüksekliği tek başına kalp krizi anlamına gelmez.", "en": "Troponin is the most sensitive marker of heart muscle damage; a high level alone does not mean a heart attack.", "es": "La troponina es el marcador más sensible de daño al músculo cardíaco; alta por sí sola no significa infarto.", "de": "Troponin ist der empfindlichste Marker für Herzmuskelschäden; erhöht allein bedeutet nicht Herzinfarkt.", "fr": "La troponine est le marqueur le plus sensible de lésion du muscle cardiaque ; élevée seule ne signifie pas infarctus.", "it": "La troponina è il marcatore più sensibile di danno al muscolo cardiaco; alta da sola non significa infarto.", "he": "טרופונין הוא הסמן הרגיש ביותר לנזק לשריר הלב; ערך גבוה לבדו אינו אומר אוטם.", "hi": "ट्रोपोनिन हृदय की मांसपेशी क्षति का सबसे संवेदनशील मार्कर है; हाई अकेले हार्ट अटैक नहीं।", "ar": "التروبونين هو أكثر المؤشرات حساسية لتلف عضلة القلب؛ ارتفاعه وحده لا يعني نوبة قلبية."}
    excerpts = {"tr": "Troponin yüksekliği kalp krizi, miyokardit veya pulmoner emboli ile ilişkili olabilir. Acil değerlendirme gerektirir.", "en": "High troponin may indicate heart attack, myocarditis, or pulmonary embolism. Requires emergency evaluation.", "es": "Troponina alta puede indicar infarto, miocarditis o embolia pulmonar. Requiere evaluación de emergencia.", "de": "Erhöhtes Troponin kann auf Herzinfarkt, Myokarditis oder Lungenembolie hinweisen. Erfordert Notfallbeurteilung.", "fr": "Une troponine élevée peut indiquer un infarctus, une myocardite ou une embolie pulmonaire. Nécessite une évaluation d'urgence.", "it": "Troponina alta può indicare infarto, miocardite o embolia polmonare. Richiede valutazione d'emergenza.", "he": "טרופונין גבוה עשוי להצביע על אוטם, מיוקרדיטיס או תסחיף ריאתי. דורש הערכה דחופה.", "hi": "हाई ट्रोपोनिन हार्ट अटैक, मायोकार्डिटिस या पल्मोनरी एम्बोलिज़्म का संकेत हो सकता है। आपातकालीन मूल्यांकन आवश्यक।", "ar": "ارتفاع التروبونين قد يشير إلى نوبة قلبية أو التهاب عضلة القلب أو انسداد رئوي. يتطلب تقييماً طارئاً."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Troponin testi, yüksek troponin nedenleri, kalp krizi belirteci. Eğitim amaçlı.", "en": "Troponin test meaning, high troponin causes, heart attack marker. For information only.", "es": "Troponina: significado y causas de troponina alta. Solo informativo.", "de": "Troponin-Test: Bedeutung und Ursachen. Nur zur Information.", "fr": "Test de troponine : signification et causes. À titre informatif.", "it": "Troponina: significato e cause. Solo informativo.", "he": "בדיקת טרופונין: משמעות וסיבות. למידע בלבד.", "hi": "ट्रोपोनिन टेस्ट: मतलब और कारण। केवल सूचनार्थ।", "ar": "اختبار التروبونين: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Troponin kalp kan tahlili — Norya", "en": "Troponin heart blood test — Norya", "es": "Troponina análisis cardíaco — Norya", "de": "Troponin Herz Bluttest — Norya", "fr": "Troponine bilan cardiaque — Norya", "it": "Troponina esame cardiaco — Norya", "he": "טרופונין בדיקת דם לב — Norya", "hi": "ट्रोपोनिन हार्ट ब्लड टेस्ट — Norya", "ar": "التروبونين تحليل دم القلب — Norya"}
    return Article(id="troponin-test-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_troponin_sections_by_lang(), faq_schema_qa=get_troponin_faq_schema_qa())


def _article_amh() -> Article:
    from app.blog_article_amh_content import get_amh_sections_by_lang, get_amh_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/amh-hero.jpg"
    slugs = {"tr": "amh-testi-yumurtalik-rezervi", "en": "amh-test-ovarian-reserve", "es": "prueba-amh-reserva-ovarica", "de": "amh-test-ovarielle-reserve", "fr": "test-amh-reserve-ovarienne", "it": "test-amh-riserva-ovarica", "he": "בדיקת-amh-רזרבה-שחלתית", "hi": "amh-test-ovarian-reserve-hindi", "ar": "اختبار-amh-احتياطي-المبيض"}
    cat = {"tr": "Fertilite", "en": "Fertility", "es": "Fertilidad", "de": "Fruchtbarkeit", "fr": "Fertilité", "it": "Fertilità", "he": "פוריות", "hi": "फर्टिलिटी", "ar": "الخصوبة"}
    titles = {"tr": "AMH testi: yumurtalık rezerviniz hakkında ne söylüyor?", "en": "AMH test: what does it tell you about ovarian reserve?", "es": "Prueba de AMH: ¿qué dice sobre tu reserva ovárica?", "de": "AMH-Test: Was sagt er über Ihre ovarielle Reserve?", "fr": "Test AMH : que révèle-t-il sur votre réserve ovarienne ?", "it": "Test AMH: cosa dice sulla riserva ovarica?", "he": "בדיקת AMH: מה היא אומרת על הרזרבה השחלתית?", "hi": "AMH टेस्ट: ओवेरियन रिज़र्व के बारे में क्या बताता है?", "ar": "اختبار AMH: ماذا يقول عن احتياطي المبيض؟"}
    subtitles = {"tr": "AMH yumurtalık rezervini gösteren bir hormondur; düşük AMH doğurganlığın azaldığı anlamına gelebilir.", "en": "AMH is a hormone reflecting ovarian reserve; low AMH may mean declining fertility.", "es": "La AMH es una hormona que refleja la reserva ovárica; AMH baja puede significar fertilidad en descenso.", "de": "AMH ist ein Hormon, das die ovarielle Reserve widerspiegelt; niedriger AMH kann abnehmende Fruchtbarkeit bedeuten.", "fr": "L'AMH est une hormone reflétant la réserve ovarienne ; un AMH bas peut signifier une fertilité en déclin.", "it": "L'AMH è un ormone che riflette la riserva ovarica; AMH basso può significare fertilità in calo.", "he": "AMH הוא הורמון המשקף את הרזרבה השחלתית; AMH נמוך עשוי להעיד על ירידה בפוריות.", "hi": "AMH ओवेरियन रिज़र्व दर्शाने वाला हार्मोन है; लो AMH फर्टिलिटी कम होने का संकेत हो सकता है।", "ar": "AMH هرمون يعكس احتياطي المبيض؛ AMH منخفض قد يعني تراجع الخصوبة."}
    excerpts = {"tr": "AMH testi yumurtalık rezervini değerlendirir. Düşük AMH IVF planlamasında, yüksek AMH PCOS'ta önemlidir. Hekim yaş ve klinikle yorumlar.", "en": "AMH test evaluates ovarian reserve. Low AMH matters in IVF planning; high AMH may suggest PCOS. Doctor interprets with age and clinical context.", "es": "La prueba de AMH evalúa la reserva ovárica. AMH baja es clave para FIV; alta puede sugerir SOP. El médico interpreta con edad y contexto.", "de": "Der AMH-Test bewertet die ovarielle Reserve. Niedriger AMH ist für IVF-Planung wichtig; hoher für PCOS. Der Arzt interpretiert mit Alter und Klinik.", "fr": "Le test AMH évalue la réserve ovarienne. Un AMH bas est clé pour la FIV ; élevé peut suggérer un SOPK. Le médecin interprète avec l'âge.", "it": "Il test AMH valuta la riserva ovarica. AMH basso è chiave per la FIV; alto può suggerire PCOS. Il medico interpreta con età e contesto.", "he": "בדיקת AMH מעריכה את הרזרבה השחלתית. AMH נמוך חשוב לתכנון IVF; גבוה עשוי להצביע על PCOS. הרופא מפרש עם גיל והקשר.", "hi": "AMH टेस्ट ओवेरियन रिज़र्व का मूल्यांकन करता है। लो AMH IVF प्लानिंग में; हाई AMH PCOS में महत्वपूर्ण। डॉक्टर उम्र के साथ व्याख्या करेंगे।", "ar": "اختبار AMH يقيّم احتياطي المبيض. AMH منخفض مهم لتخطيط IVF؛ مرتفع قد يشير إلى PCOS. الطبيب يفسره مع العمر والسياق."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "AMH testi, yumurtalık rezervi, yaşa göre AMH değerleri. Eğitim amaçlı.", "en": "AMH test meaning, ovarian reserve, AMH levels by age. For information only.", "es": "Prueba de AMH: reserva ovárica y niveles por edad. Solo informativo.", "de": "AMH-Test: ovarielle Reserve und Werte nach Alter. Nur zur Information.", "fr": "Test AMH : réserve ovarienne et taux par âge. À titre informatif.", "it": "Test AMH: riserva ovarica e livelli per età. Solo informativo.", "he": "בדיקת AMH: רזרבה שחלתית ורמות לפי גיל. למידע בלבד.", "hi": "AMH टेस्ट: ओवेरियन रिज़र्व और उम्र के हिसाब से लेवल। केवल सूचनार्थ।", "ar": "اختبار AMH: احتياطي المبيض ومستويات حسب العمر. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "AMH fertilite kan tahlili — Norya", "en": "AMH fertility blood test — Norya", "es": "AMH análisis fertilidad — Norya", "de": "AMH Fruchtbarkeit Bluttest — Norya", "fr": "AMH bilan fertilité — Norya", "it": "AMH esame fertilità — Norya", "he": "AMH בדיקת פוריות — Norya", "hi": "AMH फर्टिलिटी ब्लड टेस्ट — Norya", "ar": "AMH تحليل الخصوبة — Norya"}
    return Article(id="amh-ovarian-reserve", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_amh_sections_by_lang(), faq_schema_qa=get_amh_faq_schema_qa())


def _article_ck() -> Article:
    from app.blog_article_ck_content import get_ck_sections_by_lang, get_ck_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/ck-hero.jpg"
    slugs = {"tr": "ck-cpk-kreatin-kinaz-yuksekligi", "en": "ck-cpk-creatine-kinase-meaning", "es": "ck-cpk-creatina-quinasa-significado", "de": "ck-cpk-kreatinkinase-bedeutung", "fr": "ck-cpk-creatine-kinase-signification", "it": "ck-cpk-creatina-chinasi-significato", "he": "ck-cpk-קראטין-קינאז", "hi": "ck-cpk-creatine-kinase-hindi", "ar": "اختبار-ck-cpk-كرياتين-كيناز"}
    cat = {"tr": "Kas & Kalp", "en": "Muscle & Heart", "es": "Músculo y corazón", "de": "Muskel & Herz", "fr": "Muscle et cœur", "it": "Muscolo e cuore", "he": "שריר ולב", "hi": "मांसपेशी और हृदय", "ar": "العضلات والقلب"}
    titles = {"tr": "CK (kreatin kinaz) yüksekliği ne anlama gelir?", "en": "What does high CK (creatine kinase) mean?", "es": "¿Qué significa la CK (creatina quinasa) alta?", "de": "CK (Kreatinkinase) erhöht: Was bedeutet das?", "fr": "CK (créatine kinase) élevée : que signifie ce résultat ?", "it": "CK (creatina chinasi) alta: cosa significa?", "he": "מה משמעות CK (קראטין קינאז) גבוה?", "hi": "हाई CK (क्रिएटिन काइनेज) का क्या मतलब है?", "ar": "ماذا يعني ارتفاع CK (كرياتين كيناز)؟"}
    subtitles = {"tr": "CK kas ve kalp hasarının önemli bir belirtecidir; yüksekliği tek başına teşhis değildir.", "en": "CK is an important marker of muscle and heart damage; a high level alone is not a diagnosis.", "es": "La CK es un marcador importante de daño muscular y cardíaco; alta por sí sola no es diagnóstico.", "de": "CK ist ein wichtiger Marker für Muskel- und Herzschäden; erhöht allein ist keine Diagnose.", "fr": "La CK est un marqueur important de lésion musculaire et cardiaque ; élevée seule ne constitue pas un diagnostic.", "it": "La CK è un marcatore importante di danno muscolare e cardiaco; alta da sola non è una diagnosi.", "he": "CK הוא סמן חשוב לנזק בשרירים ובלב; ערך גבוה לבדו אינו אבחנה.", "hi": "CK मांसपेशी और हृदय क्षति का महत्वपूर्ण मार्कर है; हाई अकेले निदान नहीं।", "ar": "CK مؤشر مهم لتلف العضلات والقلب؛ ارتفاعه وحده ليس تشخيصاً."}
    excerpts = {"tr": "CK yüksekliği yoğun egzersiz, rabdomiyoliz, kalp krizi veya statin yan etkisi ile ilişkili olabilir. Hekim CK-MB ve klinikle yorumlar.", "en": "High CK may be linked to intense exercise, rhabdomyolysis, heart attack, or statin side effects. Your doctor interprets with CK-MB and clinical context.", "es": "CK alta puede deberse a ejercicio intenso, rabdomiólisis, infarto o efectos de estatinas. El médico interpreta con CK-MB y contexto.", "de": "Erhöhte CK kann mit intensivem Training, Rhabdomyolyse, Herzinfarkt oder Statinnebenwirkungen zusammenhängen. Der Arzt wertet mit CK-MB.", "fr": "Une CK élevée peut être liée à un exercice intense, une rhabdomyolyse, un infarctus ou des statines. Le médecin interprète avec CK-MB.", "it": "CK alta può essere legata a esercizio intenso, rabdomiolisi, infarto o effetti delle statine. Il medico valuta con CK-MB.", "he": "CK גבוה עשוי לקשור לאימון אינטנסיבי, רבדומיוליזיס, אוטם או תופעות לוואי של סטטינים. הרופא מפרש עם CK-MB.", "hi": "हाई CK तीव्र व्यायाम, रैब्डोमायोलिसिस, हार्ट अटैक या स्टैटिन साइड इफेक्ट से जुड़ सकता है। डॉक्टर CK-MB के साथ व्याख्या करेंगे।", "ar": "ارتفاع CK قد يرتبط بتمارين مكثفة أو انحلال الربيدات أو نوبة قلبية أو آثار الستاتين. الطبيب يفسره مع CK-MB."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "CK kreatin kinaz yüksekliği nedenleri, CK-MB, rabdomiyoliz. Eğitim amaçlı.", "en": "CK creatine kinase meaning, high CK causes, CK-MB. For information only.", "es": "CK creatina quinasa: significado y causas. Solo informativo.", "de": "CK Kreatinkinase: Bedeutung und Ursachen. Nur zur Information.", "fr": "CK créatine kinase : signification et causes. À titre informatif.", "it": "CK creatina chinasi: significato e cause. Solo informativo.", "he": "CK קראטין קינאז: משמעות וסיבות. למידע בלבד.", "hi": "CK क्रिएटिन काइनेज: मतलब और कारण। केवल सूचनार्थ।", "ar": "CK كرياتين كيناز: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "CK kreatin kinaz kan tahlili — Norya", "en": "CK creatine kinase blood test — Norya", "es": "CK creatina quinasa análisis — Norya", "de": "CK Kreatinkinase Bluttest — Norya", "fr": "CK créatine kinase bilan — Norya", "it": "CK creatina chinasi esame — Norya", "he": "CK קראטין קינאז בדיקת דם — Norya", "hi": "CK क्रिएटिन काइनेज ब्लड टेस्ट — Norya", "ar": "CK كرياتين كيناز تحليل دم — Norya"}
    return Article(id="ck-cpk-high-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_ck_sections_by_lang(), faq_schema_qa=get_ck_faq_schema_qa())


def _article_ldh() -> Article:
    from app.blog_article_ldh_content import get_ldh_sections_by_lang, get_ldh_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/ldh-hero.jpg"
    slugs = {"tr": "ldh-laktat-dehidrojenaz-yuksekligi", "en": "ldh-lactate-dehydrogenase-meaning", "es": "ldh-lactato-deshidrogenasa-significado", "de": "ldh-laktatdehydrogenase-bedeutung", "fr": "ldh-lactate-deshydrogenase-signification", "it": "ldh-lattato-deidrogenasi-significato", "he": "ldh-לקטט-דהידרוגנאז", "hi": "ldh-lactate-dehydrogenase-hindi", "ar": "اختبار-ldh-نازعة-هيدروجين-اللاكتات"}
    cat = {"tr": "Biyobelirteçler", "en": "Biomarkers", "es": "Biomarcadores", "de": "Biomarker", "fr": "Biomarqueurs", "it": "Biomarcatori", "he": "ביומרקרים", "hi": "बायोमार्कर", "ar": "المؤشرات الحيوية"}
    titles = {"tr": "LDH (laktat dehidrojenaz) yüksekliği ne anlama gelir?", "en": "What does high LDH (lactate dehydrogenase) mean?", "es": "¿Qué significa la LDH alta?", "de": "LDH (Laktatdehydrogenase) erhöht: Was bedeutet das?", "fr": "LDH élevée : que signifie ce résultat ?", "it": "LDH alta: cosa significa?", "he": "מה משמעות LDH גבוה?", "hi": "हाई LDH (लैक्टेट डिहाइड्रोजिनेज) का क्या मतलब है?", "ar": "ماذا يعني ارتفاع LDH؟"}
    subtitles = {"tr": "LDH doku hasarının genel bir belirtecidir; yüksekliği tek başına teşhis değildir.", "en": "LDH is a general marker of tissue damage; a high level alone is not a diagnosis.", "es": "La LDH es un marcador general de daño tisular; alta por sí sola no es diagnóstico.", "de": "LDH ist ein allgemeiner Marker für Gewebeschäden; erhöht allein ist keine Diagnose.", "fr": "La LDH est un marqueur général de lésion tissulaire ; élevée seule ne constitue pas un diagnostic.", "it": "L'LDH è un marcatore generale di danno tissutale; alta da sola non è una diagnosi.", "he": "LDH הוא סמן כללי לנזק רקמתי; ערך גבוה לבדו אינו אבחנה.", "hi": "LDH ऊतक क्षति का सामान्य मार्कर है; हाई अकेले निदान नहीं।", "ar": "LDH مؤشر عام لتلف الأنسجة؛ ارتفاعه وحده ليس تشخيصاً."}
    excerpts = {"tr": "LDH yüksekliği kanser, hemolitik anemi, karaciğer hastalığı veya kalp krizi ile ilişkili olabilir. Hekim izoenzimlerle yorumlar.", "en": "High LDH may be linked to cancer, hemolytic anemia, liver disease, or heart attack. Your doctor interprets with isoenzymes.", "es": "LDH alta puede asociarse a cáncer, anemia hemolítica, enfermedad hepática o infarto. El médico interpreta con isoenzimas.", "de": "Erhöhte LDH kann mit Krebs, hämolytischer Anämie, Lebererkrankung oder Herzinfarkt zusammenhängen. Der Arzt wertet mit Isoenzymen.", "fr": "Une LDH élevée peut être liée au cancer, à l'anémie hémolytique, à une maladie hépatique ou un infarctus. Le médecin interprète avec les isoenzymes.", "it": "LDH alta può essere legata a cancro, anemia emolitica, malattia epatica o infarto. Il medico valuta con gli isoenzimi.", "he": "LDH גבוה עשוי לקשור לסרטן, אנמיה המוליטית, מחלת כבד או אוטם. הרופא מפרש עם איזואנזימים.", "hi": "हाई LDH कैंसर, हेमोलिटिक एनीमिया, लिवर रोग या हार्ट अटैक से जुड़ सकता है। डॉक्टर आइसोएंजाइम के साथ व्याख्या करेंगे।", "ar": "ارتفاع LDH قد يرتبط بالسرطان أو فقر الدم الانحلالي أو أمراض الكبد أو نوبة قلبية. الطبيب يفسره مع الإنزيمات المتماثلة."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "LDH yüksekliği nedenleri, izoenzimler, kanser belirteci. Eğitim amaçlı.", "en": "LDH meaning, high LDH causes, isoenzymes, cancer marker. For information only.", "es": "LDH alta: significado y causas. Solo informativo.", "de": "LDH erhöht: Bedeutung und Ursachen. Nur zur Information.", "fr": "LDH élevée : signification et causes. À titre informatif.", "it": "LDH alta: significato e cause. Solo informativo.", "he": "LDH גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई LDH: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع LDH: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "LDH kan tahlili — Norya", "en": "LDH blood test — Norya", "es": "LDH análisis — Norya", "de": "LDH Bluttest — Norya", "fr": "LDH bilan sanguin — Norya", "it": "LDH esame del sangue — Norya", "he": "LDH בדיקת דם — Norya", "hi": "LDH ब्लड टेस्ट — Norya", "ar": "LDH تحليل دم — Norya"}
    return Article(id="ldh-high-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_ldh_sections_by_lang(), faq_schema_qa=get_ldh_faq_schema_qa())


def _article_amylase() -> Article:
    from app.blog_article_amylase_content import get_amylase_sections_by_lang, get_amylase_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/amylase-hero.jpg"
    slugs = {"tr": "amilaz-yuksekligi-ne-anlama-gelir", "en": "amylase-high-meaning", "es": "amilasa-alta-significado", "de": "amylase-erhoht-bedeutung", "fr": "amylase-elevee-signification", "it": "amilasi-alta-significato", "he": "עמילאז-גבוה-משמעות", "hi": "amylase-high-meaning-hindi", "ar": "ارتفاع-الأميلاز-المعنى"}
    cat = {"tr": "Pankreas", "en": "Pancreas", "es": "Páncreas", "de": "Pankreas", "fr": "Pancréas", "it": "Pancreas", "he": "לבלב", "hi": "अग्न्याशय", "ar": "البنكرياس"}
    titles = {"tr": "Amilaz yüksekliği ne anlama gelir?", "en": "What does high amylase mean?", "es": "¿Qué significa la amilasa alta?", "de": "Amylase erhöht: Was bedeutet das?", "fr": "Amylase élevée : que signifie ce résultat ?", "it": "Amilasi alta: cosa significa?", "he": "מה משמעות עמילאז גבוה?", "hi": "हाई एमाइलेज़ का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الأميلاز؟"}
    subtitles = {"tr": "Amilaz pankreas ve tükürük bezlerinden salgılanan bir sindirim enzimidir; yüksekliği tek başına teşhis değildir.", "en": "Amylase is a digestive enzyme from the pancreas and salivary glands; a high level alone is not a diagnosis.", "es": "La amilasa es una enzima digestiva del páncreas y las glándulas salivales; alta por sí sola no es diagnóstico.", "de": "Amylase ist ein Verdauungsenzym der Bauchspeicheldrüse und Speicheldrüsen; erhöht allein ist keine Diagnose.", "fr": "L'amylase est une enzyme digestive du pancréas et des glandes salivaires ; élevée seule ne constitue pas un diagnostic.", "it": "L'amilasi è un enzima digestivo del pancreas e delle ghiandole salivari; alta da sola non è una diagnosi.", "he": "עמילאז הוא אנזים עיכול מהלבלב ובלוטות הרוק; ערך גבוה לבדו אינו אבחנה.", "hi": "एमाइलेज़ अग्न्याशय और लार ग्रंथियों का पाचन एंजाइम है; हाई अकेले निदान नहीं।", "ar": "الأميلاز إنزيم هضمي من البنكرياس والغدد اللعابية؛ ارتفاعه وحده ليس تشخيصاً."}
    excerpts = {"tr": "Amilaz yüksekliği pankreatit, tükürük bezi hastalığı veya bağırsak tıkanıklığı ile ilişkili olabilir. Hekim lipaz ile birlikte yorumlar.", "en": "High amylase may be linked to pancreatitis, salivary gland disease, or bowel obstruction. Your doctor interprets with lipase.", "es": "Amilasa alta puede asociarse a pancreatitis, enfermedad de glándulas salivales u obstrucción intestinal. El médico interpreta con lipasa.", "de": "Erhöhte Amylase kann mit Pankreatitis, Speicheldrüsenerkrankung oder Darmverschluss zusammenhängen. Der Arzt wertet mit Lipase.", "fr": "Une amylase élevée peut être liée à une pancréatite, une maladie salivaire ou une occlusion intestinale. Le médecin interprète avec la lipase.", "it": "Amilasi alta può essere legata a pancreatite, malattia delle ghiandole salivari o occlusione intestinale. Il medico valuta con la lipasi.", "he": "עמילאז גבוה עשוי לקשור לדלקת לבלב, מחלת בלוטות רוק או חסימת מעי. הרופא מפרש עם ליפאז.", "hi": "हाई एमाइलेज़ पैंक्रिएटाइटिस, लार ग्रंथि रोग या आंत्र रुकावट से जुड़ सकता है। डॉक्टर लाइपेज के साथ व्याख्या करेंगे।", "ar": "ارتفاع الأميلاز قد يرتبط بالتهاب البنكرياس أو أمراض الغدد اللعابية أو انسداد الأمعاء. الطبيب يفسره مع الليباز."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Amilaz yüksekliği nedenleri, pankreatit, normal aralıklar. Eğitim amaçlı.", "en": "High amylase meaning, pancreatitis, normal ranges. For information only.", "es": "Amilasa alta: significado y causas. Solo informativo.", "de": "Amylase erhöht: Bedeutung und Ursachen. Nur zur Information.", "fr": "Amylase élevée : signification et causes. À titre informatif.", "it": "Amilasi alta: significato e cause. Solo informativo.", "he": "עמילאז גבוה: משמעות וסיבות. למידע בלבד.", "hi": "हाई एमाइलेज़: मतलब और कारण। केवल सूचनार्थ।", "ar": "ارتفاع الأميلاز: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Amilaz pankreas kan tahlili — Norya", "en": "Amylase pancreas blood test — Norya", "es": "Amilasa análisis páncreas — Norya", "de": "Amylase Pankreas Bluttest — Norya", "fr": "Amylase bilan pancréas — Norya", "it": "Amilasi esame pancreas — Norya", "he": "עמילאז בדיקת לבלב — Norya", "hi": "एमाइलेज़ पैंक्रियास ब्लड टेस्ट — Norya", "ar": "الأميلاز تحليل البنكرياس — Norya"}
    return Article(id="amylase-high-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_amylase_sections_by_lang(), faq_schema_qa=get_amylase_faq_schema_qa())


def _article_ana() -> Article:
    from app.blog_article_ana_content import get_ana_sections_by_lang, get_ana_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/ana-hero.jpg"
    slugs = {"tr": "ana-antinukleer-antikor-testi", "en": "ana-antinuclear-antibody-test", "es": "ana-anticuerpo-antinuclear-significado", "de": "ana-antinukleare-antikorper-test", "fr": "ana-anticorps-antinucleaires-signification", "it": "ana-anticorpi-antinucleo-significato", "he": "בדיקת-ana-נוגדנים-אנטי-גרעיניים", "hi": "ana-antinuclear-antibody-test-hindi", "ar": "اختبار-ana-الأجسام-المضادة"}
    cat = {"tr": "Otoimmün", "en": "Autoimmune", "es": "Autoinmune", "de": "Autoimmun", "fr": "Auto-immun", "it": "Autoimmune", "he": "אוטואימוני", "hi": "ऑटोइम्यून", "ar": "المناعة الذاتية"}
    titles = {"tr": "ANA (antinükleer antikor) testi: pozitif ANA ne anlama gelir?", "en": "ANA test: what does a positive antinuclear antibody mean?", "es": "Prueba ANA: ¿qué significa un anticuerpo antinuclear positivo?", "de": "ANA-Test: Was bedeutet ein positiver antinukleärer Antikörper?", "fr": "Test ANA : que signifie un anticorps antinucléaire positif ?", "it": "Test ANA: cosa significa un anticorpo antinucleo positivo?", "he": "בדיקת ANA: מה משמעות נוגדן אנטי-גרעיני חיובי?", "hi": "ANA टेस्ट: पॉज़िटिव एंटीन्यूक्लियर एंटीबॉडी का क्या मतलब है?", "ar": "اختبار ANA: ماذا يعني الجسم المضاد للنواة الإيجابي؟"}
    subtitles = {"tr": "ANA testi otoimmün hastalıkların taranmasında kullanılır; pozitif sonuç tek başına hastalık anlamına gelmez.", "en": "The ANA test screens for autoimmune diseases; a positive result alone does not mean disease.", "es": "La prueba ANA detecta enfermedades autoinmunes; un resultado positivo por sí solo no significa enfermedad.", "de": "Der ANA-Test screent auf Autoimmunerkrankungen; positiv allein bedeutet nicht Krankheit.", "fr": "Le test ANA dépiste les maladies auto-immunes ; un résultat positif seul ne signifie pas maladie.", "it": "Il test ANA cerca malattie autoimmuni; un risultato positivo da solo non significa malattia.", "he": "בדיקת ANA סורקת מחלות אוטואימוניות; תוצאה חיובית לבדה אינה אומרת מחלה.", "hi": "ANA टेस्ट ऑटोइम्यून बीमारियों की जांच करता है; पॉज़िटिव अकेले बीमारी नहीं।", "ar": "اختبار ANA يكشف عن أمراض المناعة الذاتية؛ نتيجة إيجابية وحدها لا تعني مرضاً."}
    excerpts = {"tr": "ANA pozitifliği lupus, Sjögren veya skleroderma ile ilişkili olabilir; ancak sağlıklı bireylerin %15-20'sinde de görülebilir.", "en": "Positive ANA may be linked to lupus, Sjögren's, or scleroderma; but 15-20% of healthy people can also test positive.", "es": "ANA positivo puede relacionarse con lupus, Sjögren o esclerodermia; pero el 15-20% de personas sanas también pueden dar positivo.", "de": "Positiver ANA kann mit Lupus, Sjögren oder Sklerodermie zusammenhängen; aber 15-20% gesunder Menschen können auch positiv sein.", "fr": "Un ANA positif peut être lié au lupus, Sjögren ou sclérodermie ; mais 15-20% des personnes saines peuvent aussi être positives.", "it": "ANA positivo può essere legato a lupus, Sjögren o sclerodermia; ma il 15-20% dei sani può risultare positivo.", "he": "ANA חיובי עשוי לקשור ללופוס, סיוגרן או סקלרודרמה; אך 15-20% מהבריאים יכולים להיות חיוביים.", "hi": "पॉज़िटिव ANA ल्यूपस, स्जोग्रेन या स्क्लेरोडर्मा से जुड़ सकता है; लेकिन 15-20% स्वस्थ लोगों में भी पॉज़िटिव हो सकता है।", "ar": "ANA إيجابي قد يرتبط بالذئبة أو سيوغرن أو تصلب الجلد؛ لكن 15-20% من الأصحاء قد يكونون إيجابيين."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "ANA testi, pozitif ANA nedenleri, otoimmün hastalık taraması. Eğitim amaçlı.", "en": "ANA test meaning, positive ANA causes, autoimmune screening. For information only.", "es": "Prueba ANA: significado y causas. Solo informativo.", "de": "ANA-Test: Bedeutung und Ursachen. Nur zur Information.", "fr": "Test ANA : signification et causes. À titre informatif.", "it": "Test ANA: significato e cause. Solo informativo.", "he": "בדיקת ANA: משמעות וסיבות. למידע בלבד.", "hi": "ANA टेस्ट: मतलब और कारण। केवल सूचनार्थ।", "ar": "اختبار ANA: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "ANA antinükleer antikor kan tahlili — Norya", "en": "ANA antinuclear antibody blood test — Norya", "es": "ANA anticuerpo antinuclear análisis — Norya", "de": "ANA antinukleärer Antikörper Bluttest — Norya", "fr": "ANA anticorps antinucléaires bilan — Norya", "it": "ANA anticorpi antinucleo esame — Norya", "he": "ANA נוגדנים אנטי-גרעיניים בדיקת דם — Norya", "hi": "ANA एंटीन्यूक्लियर एंटीबॉडी ब्लड टेस्ट — Norya", "ar": "ANA الأجسام المضادة للنواة تحليل دم — Norya"}
    return Article(id="ana-test-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_ana_sections_by_lang(), faq_schema_qa=get_ana_faq_schema_qa())


def _article_homocysteine() -> Article:
    from app.blog_article_homocysteine_content import get_homocysteine_sections_by_lang, get_homocysteine_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/homocysteine-hero.jpg"
    slugs = {"tr": "homosistein-yuksekligi-ne-anlama-gelir", "en": "homocysteine-high-meaning", "es": "homocisteina-alta-significado", "de": "homocystein-erhoht-bedeutung", "fr": "homocysteine-elevee-signification", "it": "omocisteina-alta-significato", "he": "הומוציסטאין-גבוה-משמעות", "hi": "homocysteine-high-meaning-hindi", "ar": "ارتفاع-الهوموسيستين-المعنى"}
    cat = {"tr": "Kalp & Damar", "en": "Cardiovascular", "es": "Cardiovascular", "de": "Herz-Kreislauf", "fr": "Cardiovasculaire", "it": "Cardiovascolare", "he": "לב וכלי דם", "hi": "कार्डियोवैस्कुलर", "ar": "القلب والأوعية"}
    titles = {"tr": "Homosistein yüksekliği ne anlama gelir?", "en": "What does high homocysteine mean?", "es": "¿Qué significa la homocisteína alta?", "de": "Homocystein erhöht: Was bedeutet das?", "fr": "Homocystéine élevée : que signifie ce résultat ?", "it": "Omocisteina alta: cosa significa?", "he": "מה משמעות הומוציסטאין גבוה?", "hi": "हाई होमोसिस्टीन का क्या मतलब है?", "ar": "ماذا يعني ارتفاع الهوموسيستين؟"}
    subtitles = {"tr": "Homosistein kardiyovasküler risk faktörüdür; B12, folat ve B6 eksikliği ile ilişkilidir.", "en": "Homocysteine is a cardiovascular risk factor; linked to B12, folate, and B6 deficiency.", "es": "La homocisteína es un factor de riesgo cardiovascular; ligada a deficiencia de B12, folato y B6.", "de": "Homocystein ist ein kardiovaskulärer Risikofaktor; verbunden mit B12-, Folat- und B6-Mangel.", "fr": "L'homocystéine est un facteur de risque cardiovasculaire ; liée aux carences en B12, folates et B6.", "it": "L'omocisteina è un fattore di rischio cardiovascolare; legata a carenza di B12, folati e B6.", "he": "הומוציסטאין הוא גורם סיכון קרדיווסקולרי; קשור לחסר B12, חומצה פולית ו-B6.", "hi": "होमोसिस्टीन कार्डियोवैस्कुलर जोखिम कारक है; B12, फोलेट और B6 की कमी से जुड़ा।", "ar": "الهوموسيستين عامل خطر قلبي وعائي؛ مرتبط بنقص B12 والفولات وB6."}
    excerpts = {"tr": "Yüksek homosistein kalp hastalığı, inme ve DVT riski ile ilişkilidir. B12, folat ve MTHFR mutasyonu değerlendirilir.", "en": "High homocysteine is linked to heart disease, stroke, and DVT risk. B12, folate, and MTHFR mutation are evaluated.", "es": "Homocisteína alta se asocia a riesgo de enfermedad cardíaca, ictus y TVP. Se evalúan B12, folato y mutación MTHFR.", "de": "Erhöhtes Homocystein ist mit Herzerkrankung, Schlaganfall und TVT-Risiko verbunden. B12, Folat und MTHFR werden geprüft.", "fr": "Une homocystéine élevée est liée au risque cardiovasculaire, AVC et TVP. B12, folates et mutation MTHFR sont évalués.", "it": "Omocisteina alta è associata a rischio cardiovascolare, ictus e TVP. Si valutano B12, folati e mutazione MTHFR.", "he": "הומוציסטאין גבוה קשור לסיכון למחלת לב, שבץ ו-DVT. נבדקים B12, חומצה פולית ומוטציית MTHFR.", "hi": "हाई होमोसिस्टीन हृदय रोग, स्ट्रोक और DVT जोखिम से जुड़ा है। B12, फोलेट और MTHFR म्यूटेशन का मूल्यांकन होता है।", "ar": "ارتفاع الهوموسيستين مرتبط بخطر أمراض القلب والسكتة والتخثر الوريدي. يُقيَّم B12 والفولات وطفرة MTHFR."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Homosistein yüksekliği nedenleri, MTHFR, B12 bağlantısı. Eğitim amaçlı.", "en": "High homocysteine meaning, MTHFR mutation, B12 connection. For information only.", "es": "Homocisteína alta: significado y MTHFR. Solo informativo.", "de": "Homocystein erhöht: Bedeutung und MTHFR. Nur zur Information.", "fr": "Homocystéine élevée : signification et MTHFR. À titre informatif.", "it": "Omocisteina alta: significato e MTHFR. Solo informativo.", "he": "הומוציסטאין גבוה: משמעות ו-MTHFR. למידע בלבד.", "hi": "हाई होमोसिस्टीन: मतलब और MTHFR। केवल सूचनार्थ।", "ar": "ارتفاع الهوموسيستين: المعنى وMTHFR. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Homosistein kan tahlili — Norya", "en": "Homocysteine blood test — Norya", "es": "Homocisteína análisis — Norya", "de": "Homocystein Bluttest — Norya", "fr": "Homocystéine bilan sanguin — Norya", "it": "Omocisteina esame — Norya", "he": "הומוציסטאין בדיקת דם — Norya", "hi": "होमोसिस्टीन ब्लड टेस्ट — Norya", "ar": "الهوموسيستين تحليل دم — Norya"}
    return Article(id="homocysteine-high-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_homocysteine_sections_by_lang(), faq_schema_qa=get_homocysteine_faq_schema_qa())


def _article_fibrinogen() -> Article:
    from app.blog_article_fibrinogen_content import get_fibrinogen_sections_by_lang, get_fibrinogen_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/fibrinogen-hero.jpg"
    slugs = {"tr": "fibrinojen-yuksekligi-dusuklugu", "en": "fibrinogen-high-or-low-meaning", "es": "fibrinogeno-alto-o-bajo-significado", "de": "fibrinogen-erhoht-oder-niedrig", "fr": "fibrinogene-eleve-ou-bas-signification", "it": "fibrinogeno-alto-o-basso-significato", "he": "פיברינוגן-גבוה-או-נמוך", "hi": "fibrinogen-high-or-low-hindi", "ar": "ارتفاع-او-انخفاض-الفيبرينوجين"}
    cat = {"tr": "Pıhtılaşma", "en": "Coagulation", "es": "Coagulación", "de": "Gerinnung", "fr": "Coagulation", "it": "Coagulazione", "he": "קרישה", "hi": "कोगुलेशन", "ar": "التخثر"}
    titles = {"tr": "Fibrinojen yüksekliği veya düşüklüğü ne anlama gelir?", "en": "What does high or low fibrinogen mean?", "es": "¿Qué significa el fibrinógeno alto o bajo?", "de": "Fibrinogen erhöht oder erniedrigt: Was bedeutet das?", "fr": "Fibrinogène élevé ou bas : que signifie ce résultat ?", "it": "Fibrinogeno alto o basso: cosa significa?", "he": "מה משמעות פיברינוגן גבוה או נמוך?", "hi": "हाई या लो फाइब्रिनोजेन का क्या मतलब है?", "ar": "ماذا يعني ارتفاع أو انخفاض الفيبرينوجين؟"}
    subtitles = {"tr": "Fibrinojen pıhtılaşma ve akut faz proteinidir; yüksekliği veya düşüklüğü tek başına teşhis değildir.", "en": "Fibrinogen is a clotting and acute phase protein; high or low alone is not a diagnosis.", "es": "El fibrinógeno es una proteína de coagulación y fase aguda; alto o bajo por sí solo no es diagnóstico.", "de": "Fibrinogen ist ein Gerinnungs- und Akute-Phase-Protein; erhöht oder erniedrigt allein ist keine Diagnose.", "fr": "Le fibrinogène est une protéine de coagulation et de phase aiguë ; élevé ou bas seul ne constitue pas un diagnostic.", "it": "Il fibrinogeno è una proteina della coagulazione e di fase acuta; alto o basso da solo non è una diagnosi.", "he": "פיברינוגן הוא חלבון קרישה ושלב חריף; גבוה או נמוך לבדו אינו אבחנה.", "hi": "फाइब्रिनोजेन क्लॉटिंग और एक्यूट फेज़ प्रोटीन है; हाई या लो अकेले निदान नहीं।", "ar": "الفيبرينوجين بروتين تخثر ومرحلة حادة؛ ارتفاعه أو انخفاضه وحده ليس تشخيصاً."}
    excerpts = {"tr": "Yüksek fibrinojen enfeksiyon, iltihap veya kanser ile ilişkili; düşük fibrinojen DIC veya karaciğer hastalığı işareti olabilir.", "en": "High fibrinogen may relate to infection, inflammation, or cancer; low fibrinogen may signal DIC or liver disease.", "es": "Fibrinógeno alto puede relacionarse con infección o inflamación; bajo puede señalar CID o enfermedad hepática.", "de": "Erhöhtes Fibrinogen kann mit Infektion oder Entzündung zusammenhängen; niedriges mit DIC oder Lebererkrankung.", "fr": "Un fibrinogène élevé peut être lié à l'infection ou l'inflammation ; bas à la CIVD ou une maladie hépatique.", "it": "Fibrinogeno alto può essere legato a infezione o infiammazione; basso a CID o malattia epatica.", "he": "פיברינוגן גבוה עשוי לקשור לזיהום או דלקת; נמוך ל-DIC או מחלת כבד.", "hi": "हाई फाइब्रिनोजेन संक्रमण या सूजन से; लो DIC या लिवर रोग से जुड़ सकता है।", "ar": "ارتفاع الفيبرينوجين قد يرتبط بعدوى أو التهاب؛ انخفاضه بالتخثر المنتشر أو أمراض الكبد."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Fibrinojen yüksekliği ve düşüklüğü nedenleri. Eğitim amaçlı.", "en": "Fibrinogen high or low meaning, causes, DIC. For information only.", "es": "Fibrinógeno alto o bajo: significado. Solo informativo.", "de": "Fibrinogen erhöht oder erniedrigt: Bedeutung. Nur zur Information.", "fr": "Fibrinogène élevé ou bas : signification. À titre informatif.", "it": "Fibrinogeno alto o basso: significato. Solo informativo.", "he": "פיברינוגן גבוה או נמוך: משמעות. למידע בלבד.", "hi": "हाई या लो फाइब्रिनोजेन: मतलब। केवल सूचनार्थ।", "ar": "ارتفاع أو انخفاض الفيبرينوجين: المعنى. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Fibrinojen kan tahlili — Norya", "en": "Fibrinogen blood test — Norya", "es": "Fibrinógeno análisis — Norya", "de": "Fibrinogen Bluttest — Norya", "fr": "Fibrinogène bilan sanguin — Norya", "it": "Fibrinogeno esame — Norya", "he": "פיברינוגן בדיקת דם — Norya", "hi": "फाइब्रिनोजेन ब्लड टेस्ट — Norya", "ar": "الفيبرينوجين تحليل دم — Norya"}
    return Article(id="fibrinogen-high-or-low", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_fibrinogen_sections_by_lang(), faq_schema_qa=get_fibrinogen_faq_schema_qa())


def _article_rf() -> Article:
    from app.blog_article_rf_content import get_rf_sections_by_lang, get_rf_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/rf-hero.jpg"
    slugs = {"tr": "romatoid-faktor-rf-testi", "en": "rheumatoid-factor-rf-test", "es": "factor-reumatoide-rf-significado", "de": "rheumafaktor-rf-test-bedeutung", "fr": "facteur-rhumatoide-rf-signification", "it": "fattore-reumatoide-rf-significato", "he": "גורם-שגרוני-rf-משמעות", "hi": "rheumatoid-factor-rf-test-hindi", "ar": "اختبار-العامل-الروماتويدي-rf"}
    cat = {"tr": "Otoimmün", "en": "Autoimmune", "es": "Autoinmune", "de": "Autoimmun", "fr": "Auto-immun", "it": "Autoimmune", "he": "אוטואימוני", "hi": "ऑटोइम्यून", "ar": "المناعة الذاتية"}
    titles = {"tr": "Romatoid faktör (RF) testi: pozitif RF ne anlama gelir?", "en": "Rheumatoid factor (RF) test: what does positive RF mean?", "es": "Factor reumatoide (FR): ¿qué significa un FR positivo?", "de": "Rheumafaktor (RF): Was bedeutet ein positiver RF?", "fr": "Facteur rhumatoïde (FR) : que signifie un FR positif ?", "it": "Fattore reumatoide (FR): cosa significa un FR positivo?", "he": "גורם שגרוני (RF): מה משמעות RF חיובי?", "hi": "रूमेटॉइड फैक्टर (RF) टेस्ट: पॉज़िटिव RF का क्या मतलब है?", "ar": "العامل الروماتويدي (RF): ماذا يعني RF إيجابي؟"}
    subtitles = {"tr": "RF romatoid artrit gibi otoimmün hastalıkların taranmasında kullanılır; pozitifliği tek başına hastalık anlamına gelmez.", "en": "RF is used to screen for autoimmune diseases like rheumatoid arthritis; positivity alone does not mean disease.", "es": "El FR se usa para detectar enfermedades autoinmunes como la artritis reumatoide; positivo solo no significa enfermedad.", "de": "RF wird zur Screening auf Autoimmunerkrankungen wie rheumatoide Arthritis verwendet; positiv allein bedeutet nicht Krankheit.", "fr": "Le FR est utilisé pour dépister des maladies auto-immunes comme la polyarthrite rhumatoïde ; positif seul ne signifie pas maladie.", "it": "Il FR è usato per lo screening di malattie autoimmuni come l'artrite reumatoide; positivo da solo non significa malattia.", "he": "RF משמש לסקירת מחלות אוטואימוניות כמו דלקת מפרקים שגרונית; חיוביות לבדה אינה מחלה.", "hi": "RF रूमेटॉइड आर्थराइटिस जैसी ऑटोइम्यून बीमारियों की जांच के लिए है; पॉज़िटिव अकेले बीमारी नहीं।", "ar": "RF يُستخدم لفحص أمراض المناعة الذاتية كالتهاب المفاصل الروماتويدي؛ إيجابيته وحدها لا تعني مرضاً."}
    excerpts = {"tr": "RF pozitifliği romatoid artrit, Sjögren veya kronik enfeksiyonlarla ilişkili olabilir. Anti-CCP ile birlikte değerlendirilir.", "en": "Positive RF may be linked to rheumatoid arthritis, Sjögren's, or chronic infections. Evaluated with anti-CCP.", "es": "FR positivo puede asociarse a artritis reumatoide, Sjögren o infecciones crónicas. Se evalúa con anti-CCP.", "de": "Positiver RF kann mit rheumatoider Arthritis, Sjögren oder chronischen Infektionen zusammenhängen. Mit Anti-CCP bewertet.", "fr": "Un FR positif peut être lié à la polyarthrite rhumatoïde, Sjögren ou des infections chroniques. Évalué avec anti-CCP.", "it": "FR positivo può essere legato a artrite reumatoide, Sjögren o infezioni croniche. Valutato con anti-CCP.", "he": "RF חיובי עשוי לקשור לדלקת מפרקים שגרונית, סיוגרן או זיהומים כרוניים. מוערך עם anti-CCP.", "hi": "पॉज़िटिव RF रूमेटॉइड आर्थराइटिस, स्जोग्रेन या क्रोनिक इंफेक्शन से जुड़ सकता है। एंटी-CCP के साथ मूल्यांकन।", "ar": "RF إيجابي قد يرتبط بالتهاب المفاصل الروماتويدي أو سيوغرن أو عدوى مزمنة. يُقيَّم مع anti-CCP."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "RF testi, pozitif RF nedenleri, romatoid artrit. Eğitim amaçlı.", "en": "RF test meaning, positive RF causes, rheumatoid arthritis. For information only.", "es": "Factor reumatoide: significado y causas. Solo informativo.", "de": "Rheumafaktor: Bedeutung und Ursachen. Nur zur Information.", "fr": "Facteur rhumatoïde : signification et causes. À titre informatif.", "it": "Fattore reumatoide: significato e cause. Solo informativo.", "he": "גורם שגרוני: משמעות וסיבות. למידע בלבד.", "hi": "RF टेस्ट: मतलब और कारण। केवल सूचनार्थ।", "ar": "العامل الروماتويدي: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "RF romatoid faktör kan tahlili — Norya", "en": "Rheumatoid factor blood test — Norya", "es": "Factor reumatoide análisis — Norya", "de": "Rheumafaktor Bluttest — Norya", "fr": "Facteur rhumatoïde bilan — Norya", "it": "Fattore reumatoide esame — Norya", "he": "גורם שגרוני בדיקת דם — Norya", "hi": "रूमेटॉइड फैक्टर ब्लड टेस्ट — Norya", "ar": "العامل الروماتويدي تحليل دم — Norya"}
    return Article(id="rf-rheumatoid-factor", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_rf_sections_by_lang(), faq_schema_qa=get_rf_faq_schema_qa())


def _article_dheas() -> Article:
    from app.blog_article_dheas_content import get_dheas_sections_by_lang, get_dheas_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/dheas-hero.jpg"
    slugs = {"tr": "dhea-s-testi-ne-anlama-gelir", "en": "dhea-s-test-meaning", "es": "dhea-s-prueba-significado", "de": "dhea-s-test-bedeutung", "fr": "dhea-s-test-signification", "it": "dhea-s-test-significato", "he": "בדיקת-dhea-s-משמעות", "hi": "dhea-s-test-meaning-hindi", "ar": "اختبار-dhea-s-المعنى"}
    cat = {"tr": "Hormonlar", "en": "Hormones", "es": "Hormonas", "de": "Hormone", "fr": "Hormones", "it": "Ormoni", "he": "הורמונים", "hi": "हार्मोन", "ar": "الهرمونات"}
    titles = {"tr": "DHEA-S testi: yüksek veya düşük DHEA sülfat ne anlama gelir?", "en": "DHEA-S test: what does high or low DHEA sulfate mean?", "es": "Prueba de DHEA-S: ¿qué significa DHEA sulfato alto o bajo?", "de": "DHEA-S-Test: Was bedeutet ein hoher oder niedriger DHEA-Sulfat-Wert?", "fr": "Test DHEA-S : que signifie un taux de DHEA sulfate élevé ou bas ?", "it": "Test DHEA-S: cosa significa DHEA solfato alto o basso?", "he": "בדיקת DHEA-S: מה משמעות DHEA סולפט גבוה או נמוך?", "hi": "DHEA-S टेस्ट: हाई या लो DHEA सल्फेट का क्या मतलब है?", "ar": "اختبار DHEA-S: ماذا يعني ارتفاع أو انخفاض كبريتات DHEA؟"}
    subtitles = {"tr": "DHEA-S adrenal bezlerden salgılanan bir hormondur; yüksekliği veya düşüklüğü tek başına teşhis değildir.", "en": "DHEA-S is a hormone produced by the adrenal glands; high or low alone is not a diagnosis.", "es": "La DHEA-S es una hormona producida por las glándulas suprarrenales; alta o baja por sí sola no es diagnóstico.", "de": "DHEA-S ist ein Hormon der Nebennieren; erhöht oder erniedrigt allein ist keine Diagnose.", "fr": "La DHEA-S est une hormone produite par les glandes surrénales ; élevée ou basse seule ne constitue pas un diagnostic.", "it": "Il DHEA-S è un ormone prodotto dalle ghiandole surrenali; alto o basso da solo non è una diagnosi.", "he": "DHEA-S הוא הורמון המיוצר בבלוטות האדרנל; ערך גבוה או נמוך לבדו אינו אבחנה.", "hi": "DHEA-S अधिवृक्क ग्रंथियों द्वारा उत्पादित हार्मोन है; हाई या लो अकेले निदान नहीं।", "ar": "DHEA-S هرمون تفرزه الغدد الكظرية؛ ارتفاعه أو انخفاضه وحده ليس تشخيصاً."}
    excerpts = {"tr": "Yüksek DHEA-S PCOS, adrenal tümör veya CAH ile ilişkili; düşüklüğü adrenal yetmezlik işareti olabilir.", "en": "High DHEA-S may relate to PCOS, adrenal tumor, or CAH; low may signal adrenal insufficiency.", "es": "DHEA-S alta puede relacionarse con SOP, tumor adrenal o HAC; baja puede señalar insuficiencia adrenal.", "de": "Hoher DHEA-S kann mit PCOS, Nebennierentumor oder AGS zusammenhängen; niedriger mit Nebenniereninsuffizienz.", "fr": "Un DHEA-S élevé peut être lié au SOPK, tumeur surrénalienne ou HAC ; bas à l'insuffisance surrénalienne.", "it": "DHEA-S alto può essere legato a PCOS, tumore surrenale o IAC; basso a insufficienza surrenale.", "he": "DHEA-S גבוה עשוי לקשור ל-PCOS, גידול אדרנל או CAH; נמוך לאי-ספיקת אדרנל.", "hi": "हाई DHEA-S PCOS, एड्रेनल ट्यूमर या CAH से; लो एड्रेनल इनसफिशिएंसी से जुड़ सकता है।", "ar": "ارتفاع DHEA-S قد يرتبط بتكيس المبايض أو ورم كظري أو CAH؛ انخفاضه بقصور الغدة الكظرية."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "DHEA-S testi, adrenal hormon, PCOS bağlantısı. Eğitim amaçlı.", "en": "DHEA-S test meaning, adrenal hormone, PCOS connection. For information only.", "es": "DHEA-S: significado y conexión con SOP. Solo informativo.", "de": "DHEA-S-Test: Bedeutung und PCOS-Zusammenhang. Nur zur Information.", "fr": "Test DHEA-S : signification et lien SOPK. À titre informatif.", "it": "Test DHEA-S: significato e connessione PCOS. Solo informativo.", "he": "בדיקת DHEA-S: משמעות וקשר ל-PCOS. למידע בלבד.", "hi": "DHEA-S टेस्ट: मतलब और PCOS संबंध। केवल सूचनार्थ।", "ar": "اختبار DHEA-S: المعنى وعلاقته بتكيس المبايض. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "DHEA-S adrenal hormon kan tahlili — Norya", "en": "DHEA-S adrenal hormone blood test — Norya", "es": "DHEA-S hormona adrenal análisis — Norya", "de": "DHEA-S Nebennierenhormon Bluttest — Norya", "fr": "DHEA-S hormone surrénalienne bilan — Norya", "it": "DHEA-S ormone surrenale esame — Norya", "he": "DHEA-S הורמון אדרנל בדיקת דם — Norya", "hi": "DHEA-S एड्रेनल हार्मोन ब्लड टेस्ट — Norya", "ar": "DHEA-S هرمون الغدة الكظرية تحليل دم — Norya"}
    return Article(id="dheas-test-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_dheas_sections_by_lang(), faq_schema_qa=get_dheas_faq_schema_qa())


def _article_procalcitonin() -> Article:
    from app.blog_article_procalcitonin_content import get_procalcitonin_sections_by_lang, get_procalcitonin_faq_schema_qa
    published = date(2026, 3, 25)
    cover = "/static/images/blog/procalcitonin-hero.jpg"
    slugs = {"tr": "prokalsitonin-pct-testi-ne-anlama-gelir", "en": "procalcitonin-pct-test-meaning", "es": "procalcitonina-pct-significado", "de": "procalcitonin-pct-test-bedeutung", "fr": "procalcitonine-pct-signification", "it": "procalcitonina-pct-significato", "he": "פרוקלציטונין-pct-משמעות", "hi": "procalcitonin-pct-test-hindi", "ar": "اختبار-البروكالسيتونين-pct"}
    cat = {"tr": "Enfeksiyon", "en": "Infection", "es": "Infección", "de": "Infektion", "fr": "Infection", "it": "Infezione", "he": "זיהום", "hi": "संक्रमण", "ar": "العدوى"}
    titles = {"tr": "Prokalsitonin (PCT) testi: yüksek prokalsitonin ne anlama gelir?", "en": "Procalcitonin (PCT) test: what does high procalcitonin mean?", "es": "Procalcitonina (PCT): ¿qué significa la procalcitonina alta?", "de": "Procalcitonin (PCT): Was bedeutet ein erhöhter Procalcitoninwert?", "fr": "Procalcitonine (PCT) : que signifie une procalcitonine élevée ?", "it": "Procalcitonina (PCT): cosa significa la procalcitonina alta?", "he": "פרוקלציטונין (PCT): מה משמעות PCT גבוה?", "hi": "प्रोकैल्सीटोनिन (PCT) टेस्ट: हाई PCT का क्या मतलब है?", "ar": "البروكالسيتونين (PCT): ماذا يعني ارتفاع PCT؟"}
    subtitles = {"tr": "Prokalsitonin bakteriyel enfeksiyonlar ile viral enfeksiyonları ayırt etmede kullanılan önemli bir belirteçtir.", "en": "Procalcitonin is an important marker used to differentiate bacterial from viral infections.", "es": "La procalcitonina es un marcador importante para diferenciar infecciones bacterianas de virales.", "de": "Procalcitonin ist ein wichtiger Marker zur Unterscheidung bakterieller von viralen Infektionen.", "fr": "La procalcitonine est un marqueur important pour différencier les infections bactériennes des virales.", "it": "La procalcitonina è un marcatore importante per differenziare le infezioni batteriche dalle virali.", "he": "פרוקלציטונין הוא סמן חשוב להבחנה בין זיהומים חיידקיים לנגיפיים.", "hi": "प्रोकैल्सीटोनिन बैक्टीरियल और वायरल संक्रमण में अंतर करने के लिए महत्वपूर्ण मार्कर है।", "ar": "البروكالسيتونين مؤشر مهم للتمييز بين العدوى البكتيرية والفيروسية."}
    excerpts = {"tr": "Yüksek prokalsitonin bakteriyel sepsis, pnömoni veya menenjit ile ilişkili olabilir. Antibiyotik yönetiminde kullanılır.", "en": "High procalcitonin may be linked to bacterial sepsis, pneumonia, or meningitis. Used in antibiotic stewardship.", "es": "Procalcitonina alta puede asociarse a sepsis bacteriana, neumonía o meningitis. Se usa en gestión de antibióticos.", "de": "Erhöhtes Procalcitonin kann mit bakterieller Sepsis, Pneumonie oder Meningitis zusammenhängen. Zur Antibiotika-Steuerung.", "fr": "Une procalcitonine élevée peut être liée à une septicémie, pneumonie ou méningite. Utilisée pour la gestion des antibiotiques.", "it": "Procalcitonina alta può essere legata a sepsi batterica, polmonite o meningite. Usata nella gestione antibiotica.", "he": "PCT גבוה עשוי לקשור לאלח דם חיידקי, דלקת ריאות או מנינגיטיס. משמש בניהול אנטיביוטיקה.", "hi": "हाई PCT बैक्टीरियल सेप्सिस, निमोनिया या मेनिंजाइटिस से जुड़ सकता है। एंटीबायोटिक स्टीवर्डशिप में उपयोग।", "ar": "ارتفاع PCT قد يرتبط بإنتان جرثومي أو ذات الرئة أو التهاب السحايا. يُستخدم في إدارة المضادات الحيوية."}
    seo_titles = {k: v + " | Norya Blog" for k, v in titles.items()}
    seo_descriptions = {"tr": "Prokalsitonin testi, yüksek PCT nedenleri, sepsis belirteci. Eğitim amaçlı.", "en": "Procalcitonin test meaning, high PCT causes, sepsis marker. For information only.", "es": "Procalcitonina: significado y causas. Solo informativo.", "de": "Procalcitonin: Bedeutung und Ursachen. Nur zur Information.", "fr": "Procalcitonine : signification et causes. À titre informatif.", "it": "Procalcitonina: significato e cause. Solo informativo.", "he": "פרוקלציטונין: משמעות וסיבות. למידע בלבד.", "hi": "PCT टेस्ट: मतलब और कारण। केवल सूचनार्थ।", "ar": "البروكالسيتونين: المعنى والأسباب. لأغراض إعلامية فقط."}
    cover_alt = {"tr": "Prokalsitonin PCT kan tahlili — Norya", "en": "Procalcitonin PCT blood test — Norya", "es": "Procalcitonina PCT análisis — Norya", "de": "Procalcitonin PCT Bluttest — Norya", "fr": "Procalcitonine PCT bilan — Norya", "it": "Procalcitonina PCT esame — Norya", "he": "פרוקלציטונין PCT בדיקת דם — Norya", "hi": "प्रोकैल्सीटोनिन PCT ब्लड टेस्ट — Norya", "ar": "البروكالسيتونين PCT تحليل دم — Norya"}
    return Article(id="procalcitonin-pct-meaning", published_at=published, read_minutes=7, cover_image=cover, category=cat, slugs=slugs, titles=titles, subtitles=subtitles, excerpts=excerpts, seo_titles=seo_titles, seo_descriptions=seo_descriptions, cover_alt=cover_alt, sections_by_lang=get_procalcitonin_sections_by_lang(), faq_schema_qa=get_procalcitonin_faq_schema_qa())


_ARTICLE_PSA = _article_psa()
_ARTICLE_ESTRADIOL = _article_estradiol()
_ARTICLE_PROGESTERONE = _article_progesterone()
_ARTICLE_BETA_HCG = _article_beta_hcg()
_ARTICLE_TROPONIN = _article_troponin()
_ARTICLE_AMH = _article_amh()
_ARTICLE_CK = _article_ck()
_ARTICLE_LDH = _article_ldh()
_ARTICLE_AMYLASE = _article_amylase()
_ARTICLE_ANA = _article_ana()
_ARTICLE_HOMOCYSTEINE = _article_homocysteine()
_ARTICLE_FIBRINOGEN = _article_fibrinogen()
_ARTICLE_RF = _article_rf()
_ARTICLE_DHEAS = _article_dheas()
_ARTICLE_PROCALCITONIN = _article_procalcitonin()

# Pillar articles (imported from dedicated content modules)
from app.blog_article_cbc_guide_content import build_cbc_article
from app.blog_article_thyroid_panel_content import build_thyroid_article
from app.blog_article_liver_panel_content import build_liver_panel_article
from app.blog_article_annual_tests_content import build_annual_tests_article
from app.blog_article_metabolic_panel_content import build_metabolic_panel_article
from app.blog_article_urine_acr_content import build_urine_acr_article
from app.blog_article_apob_content import build_apob_article
from app.blog_article_lpa_content import build_lpa_article
from app.blog_article_blood_sugar_guide_content import build_blood_sugar_article
from app.blog_article_noryaai_story_content import build_noryaai_story_article
_ARTICLE_CBC_GUIDE = build_cbc_article()
_ARTICLE_THYROID_GUIDE = build_thyroid_article()
_ARTICLE_LIVER_PANEL = build_liver_panel_article()
_ARTICLE_ANNUAL_TESTS = build_annual_tests_article()
_ARTICLE_METABOLIC_PANEL = build_metabolic_panel_article()
_ARTICLE_URINE_ACR = build_urine_acr_article()
_ARTICLE_APOB = build_apob_article()
_ARTICLE_LPA = build_lpa_article()
_ARTICLE_BLOOD_SUGAR_GUIDE = build_blood_sugar_article()
_ARTICLE_NORYAAI_STORY = build_noryaai_story_article()

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
    _ARTICLE_ALBUMIN_LOW,
    _ARTICLE_TOTAL_PROTEIN,
    _ARTICLE_ALP_HIGH,
    _ARTICLE_SODIUM_LOW,
    _ARTICLE_POTASSIUM_HIGH,
    _ARTICLE_CALCIUM_HIGH,
    _ARTICLE_LYMPHOCYTES,
    _ARTICLE_MONOCYTES,
    _ARTICLE_MCV,
    _ARTICLE_RDW,
    _ARTICLE_AG_RATIO,
    _ARTICLE_HEMATOCRIT_HIGH_LOW,
    _ARTICLE_MCH_HIGH_LOW,
    _ARTICLE_MCHC_LOW,
    _ARTICLE_EOSINOPHILS_HIGH,
    _ARTICLE_BASOPHILS_HIGH,
    _ARTICLE_CHLORIDE_HIGH_LOW,
    _ARTICLE_CO2_BLOOD_TEST,
    _ARTICLE_ANION_GAP_HIGH,
    _ARTICLE_MPV_HIGH_LOW,
    _ARTICLE_GLOBULIN,
    _ARTICLE_HIGH_WBC,
    _ARTICLE_LOW_WBC,
    _ARTICLE_HOMA_IR,
    _ARTICLE_FASTING_INSULIN_HIGH,
    _ARTICLE_CBC_GUIDE,
    _ARTICLE_THYROID_GUIDE,
    _ARTICLE_TRIGLYCERIDES,
    _ARTICLE_GGT,
    _ARTICLE_URIC_ACID,
    _ARTICLE_MAGNESIUM,
    _ARTICLE_BILIRUBIN,
    _ARTICLE_ESR,
    _ARTICLE_CORTISOL,
    _ARTICLE_TESTOSTERONE,
    _ARTICLE_FOLATE,
    _ARTICLE_PHOSPHORUS,
    _ARTICLE_ZINC,
    _ARTICLE_INR,
    _ARTICLE_PROLACTIN,
    _ARTICLE_LIPASE,
    _ARTICLE_D_DIMER,
    _ARTICLE_HEMOGLOBIN,
    _ARTICLE_NEUTROPHILS,
    _ARTICLE_IRON_LEVELS,
    _ARTICLE_BUN,
    _ARTICLE_PLT,
    _ARTICLE_T3_T4,
    _ARTICLE_PSA,
    _ARTICLE_ESTRADIOL,
    _ARTICLE_PROGESTERONE,
    _ARTICLE_BETA_HCG,
    _ARTICLE_TROPONIN,
    _ARTICLE_AMH,
    _ARTICLE_CK,
    _ARTICLE_LDH,
    _ARTICLE_AMYLASE,
    _ARTICLE_ANA,
    _ARTICLE_HOMOCYSTEINE,
    _ARTICLE_FIBRINOGEN,
    _ARTICLE_RF,
    _ARTICLE_DHEAS,
    _ARTICLE_PROCALCITONIN,
    _ARTICLE_LIVER_PANEL,
    _ARTICLE_ANNUAL_TESTS,
    _ARTICLE_METABOLIC_PANEL,
    _ARTICLE_URINE_ACR,
    _ARTICLE_APOB,
    _ARTICLE_LPA,
    _ARTICLE_BLOOD_SUGAR_GUIDE,
    _ARTICLE_NORYAAI_STORY,
]

_ARTICLE_BY_ID: Dict[str, Article] = {a.id: a for a in ARTICLES}

# Blog index "Quick definitions" — stable order; entries missing in a locale are skipped.
BLOG_INDEX_DEFINITION_ARTICLE_IDS: tuple[str, ...] = (
    "aclik-kan-sekeri-sonucu-nasil-degerlendirilir",
    "hba1c-sonucu-ne-anlama-gelir",
    "homa-ir-what-it-is",
    "trombosit-yuksekligi-dusuklugu",
    "wbc-rbc-hgb-hct-nasil-okunur",
    "creatinine-egfr-what-it-means",
    "sodium-low-meaning",
    "potassium-high-meaning",
    "alt-ast-yuksekligi-neyi-gosterir",
    "albumin-low-meaning",
    "total-protein-high-or-low",
    "ferritin-what-it-means",
    "tsh-what-it-means",
    "metabolic-panel-results-explained",
    "alp-high-meaning",
    "ure-yuksekligi-ne-anlama-gelir",
    "urine-acr-microalbumin-meaning",
    "triglycerides-high-meaning",
    "apob-meaning",
    "lpa-meaning",
    "ggt-high-meaning",
    "low-wbc-meaning",
    "high-wbc-meaning",
)

_BLOG_TOPIC_CLUSTER_CBC_GUIDE_LANGS = frozenset({"en", "he", "hi", "ar"})

_CBC_GUIDE_LINK_LABELS: Dict[str, str] = {
    "en": "How to read CBC results",
    "tr": "Hemogram sonuçları nasıl okunur?",
    "es": "Cómo leer un hemograma",
    "de": "Blutbild richtig lesen",
    "fr": "Comment lire une numération sanguine",
    "it": "Come leggere l'emocromo",
    "he": "איך לקרוא ספירת דם מלאה",
    "hi": "CBC रिज़ल्ट कैसे पढ़ें",
    "ar": "كيف تقرأ تحليل الدم الشامل",
}

# (title_by_lang, desc_by_lang, link_specs) — link_specs: ("cbc_guide",) or ("article", article_id)
_BLOG_TOPIC_CLUSTER_SPECS: List[tuple[Dict[str, str], Dict[str, str], List[tuple]]] = [
    (
        {
            "en": "CBC and blood counts",
            "tr": "Hemogram ve kan sayımları",
            "es": "Hemograma y recuento sanguíneo",
            "de": "Blutbild und Blutzellwerte",
            "fr": "Numération sanguine et hémogramme",
            "it": "Emocromo e formula leucocitaria",
            "he": "ספירת דם מלאה ותאי דם",
            "hi": "CBC और ब्लड काउंट",
            "ar": "صورة دم كاملة وتعداد الخلايا",
        },
        {
            "en": "Start with core cell counts, then move into differentials and red-cell indices.",
            "tr": "Önce temel hücre sayılarına bakın; ardından diferansiyel ve eritrosit indekslerine geçin.",
            "es": "Empieza por los recuentos básicos y luego mira el diferencial y los índices eritrocitarios.",
            "de": "Beginnen Sie mit den Basiswerten des Blutbilds, dann Differenzialblutbild und rote‑Zell‑Indizes.",
            "fr": "Commencez par les numérations de base, puis le différentiel et les indices érythrocytaires.",
            "it": "Parti dai conteggi principali, poi differenziale e indici dei globuli rossi.",
            "he": "התחילו מספירות התאים הבסיסיות, ואז דיפרנציאל ומדדי תאי דם אדומים.",
            "hi": "पहले मुख्य सेल काउंट, फिर डिफरेंशियल और लाल कोशिका इंडेक्स।",
            "ar": "ابدأ بعدّ الخلايا الأساسية، ثم الفرقيات ومؤشرات كريات الدم الحمراء.",
        },
        [("cbc_guide",), ("article", "wbc-rbc-hgb-hct-nasil-okunur"), ("article", "trombosit-yuksekligi-dusuklugu")],
    ),
    (
        {
            "en": "Glucose and metabolic health",
            "tr": "Glikoz ve metabolik sağlık",
            "es": "Glucosa y salud metabólica",
            "de": "Glukose und Stoffwechselgesundheit",
            "fr": "Glycémie et santé métabolique",
            "it": "Glicemia e salute metabolica",
            "he": "גלוקוז ובריאות מטבולית",
            "hi": "ग्लूकोज और मेटाबोलिक हेल्थ",
            "ar": "الجلوكوز والصحة الأيضية",
        },
        {
            "en": "Understand fasting glucose, HbA1c, insulin resistance, and the wider chemistry panel.",
            "tr": "Açlık glukozu, HbA1c, insülin direnci ve geniş kimya panelini anlayın.",
            "es": "Entiende glucosa en ayunas, HbA1c, resistencia a la insulina y el panel metabólico.",
            "de": "Nüchternglukose, HbA1c, Insulinresistenz und das erweiterte Chemiepanel verstehen.",
            "fr": "Comprenez la glycémie à jeun, l'HbA1c, l'insulinorésistance et le bilan métabolique.",
            "it": "Capisci glicemia a digiuno, HbA1c, resistenza insulinica e il pannello metabolico.",
            "he": "הבנת גלוקוז בצום, HbA1c, עמידות לאינסולין והפאנל המטבולי.",
            "hi": "फास्टिंग ग्लूकोज, HbA1c, इंसुलिन रेज़िस्टेंस और मेटाबोलिक पैनल समझें।",
            "ar": "افهم الجلوكوز الصائم، الـHbA1c، مقاومة الأنسولين ولوحة الأيض.",
        },
        [
            ("article", "aclik-kan-sekeri-sonucu-nasil-degerlendirilir"),
            ("article", "hba1c-sonucu-ne-anlama-gelir"),
            ("article", "metabolic-panel-results-explained"),
        ],
    ),
    (
        {
            "en": "Kidney and electrolytes",
            "tr": "Böbrek ve elektrolitler",
            "es": "Riñón y electrolitos",
            "de": "Nieren und Elektrolyte",
            "fr": "Reins et électrolytes",
            "it": "Reni ed elettroliti",
            "he": "כליות ואלקטרוליטים",
            "hi": "किडनी और इलेक्ट्रोलाइट",
            "ar": "الكلى والكهارل",
        },
        {
            "en": "Move from creatinine and eGFR into sodium, potassium, calcium, and hydration-related patterns.",
            "tr": "Kreatinin ve eGFR'den başlayıp sodyum, potasyum ve sıvı dengesi örüntülerine geçin.",
            "es": "Desde creatinina y FG hasta sodio, potasio y patrones de hidratación.",
            "de": "Von Kreatinin und eGFR zu Natrium, Kalzium, Kalium und Flüssigkeitsmustern.",
            "fr": "De la créatinine et du DFG au sodium, potassium et contexte d'hydratation.",
            "it": "Da creatinina ed eGFR a sodio, potassio e idratazione.",
            "he": "מקראטינין ו-eGFR לנתרן, אשלגן ודפוסי נוזלים.",
            "hi": "क्रिएटिनिन और eGFR से सोडियम, पोटैशियम और हाइड्रेशन पैटर्न तक।",
            "ar": "من الكرياتينين ومعدل الترشيح إلى الصوديوم والبوتاسيوم وأنماط السوائل.",
        },
        [
            ("article", "creatinine-egfr-what-it-means"),
            ("article", "sodium-low-meaning"),
            ("article", "potassium-high-meaning"),
            ("article", "urine-acr-microalbumin-meaning"),
        ],
    ),
    (
        {
            "en": "Liver and proteins",
            "tr": "Karaciğer ve proteinler",
            "es": "Hígado y proteínas",
            "de": "Leber und Proteine",
            "fr": "Foie et protéines",
            "it": "Fegato e proteine",
            "he": "כבד וחלבונים",
            "hi": "लिवर और प्रोटीन",
            "ar": "الكبد والبروتينات",
        },
        {
            "en": "Review liver enzymes, protein markers, and the chemistry patterns doctors usually compare together.",
            "tr": "Karaciğer enzimleri, protein belirteçleri ve birlikte yorumlanan kimya örüntüleri.",
            "es": "Enzimas hepáticas, proteínas y patrones bioquímicos que suelen leerse juntos.",
            "de": "Leberenzyme, Eiweißmarker und Chemie‑Muster, die zusammen gelesen werden.",
            "fr": "Enzymes hépatiques, protéines et schémas de biochimie souvent comparés ensemble.",
            "it": "Enzimi epatici, proteine e schemi di chimica letti insieme.",
            "he": "אנזימי כבד, חלבונים ודפוסי כימיה שנקראים יחד.",
            "hi": "लिवर एंजाइम, प्रोटीन मार्कर और साथ पढ़े जाने वाले पैटर्न।",
            "ar": "إنزيمات الكبد والبروتينات وأنماط الكيمياء التي تُقارن معاً.",
        },
        [
            ("article", "alt-ast-yuksekligi-neyi-gosterir"),
            ("article", "alp-high-meaning"),
            ("article", "albumin-low-meaning"),
        ],
    ),
    (
        {
            "en": "Thyroid and hormones",
            "tr": "Tiroid ve hormonlar",
            "es": "Tiroides y hormonas",
            "de": "Schilddrüse und Hormone",
            "fr": "Thyroïde et hormones",
            "it": "Tiroide e ormoni",
            "he": "בלוטת התריס והורמונים",
            "hi": "थायरॉयड और हार्मोन",
            "ar": "الغدة الدرقية والهرمونات",
        },
        {
            "en": "Use a panel-first view, then go deeper into single markers or symptom-driven follow-up.",
            "tr": "Önce panel bakışı; ardından tek belirteçlere veya semptoma göre takibe geçin.",
            "es": "Primero el panel; luego marcadores puntuales o seguimiento según síntomas.",
            "de": "Zuerst das Panel, dann Einzelmarker oder symptomgeleitete Nachsorge.",
            "fr": "D'abord le panel, puis marqueurs ciblés ou suivi selon les symptômes.",
            "it": "Prima il pannello, poi marker singoli o follow-up sui sintomi.",
            "he": "קודם תמונת הפאנל, ואז סמנים בודדים או מעקב לפי תסמינים.",
            "hi": "पहले पैनल दृष्टिकोण, फिर एकल मार्कर या लक्षणों पर फॉलो-अप।",
            "ar": "ابدأ بلوحة الفحوصات، ثم مؤشرات منفصلة أو متابعة حسب الأعراض.",
        },
        [
            ("article", "tsh-what-it-means"),
            ("article", "thyroid-panel-guide"),
            ("article", "d-vitamini-sonucu-nasil-yorumlanir"),
        ],
    ),
    (
        {
            "en": "Lipids and cardiovascular risk",
            "tr": "Lipitler ve kardiyovasküler risk",
            "es": "Lípidos y riesgo cardiovascular",
            "de": "Lipide und kardiovaskuläres Risiko",
            "fr": "Lipides et risque cardiovasculaire",
            "it": "Lipidi e rischio cardiovascolare",
            "he": "ליפידים וסיכון לבבי־כלי",
            "hi": "लिपिड्स और हृदय जोखिम",
            "ar": "الدهون والخطر القلبي الوعائي",
        },
        {
            "en": "Cover LDL, HDL, triglycerides, inflammatory context, and advanced lipid follow-up questions.",
            "tr": "LDL, HDL, trigliserit, inflamatuvar bağlam ve ileri lipid soruları.",
            "es": "LDL, HDL, triglicéridos, inflamación y preguntas de seguimiento lipídico.",
            "de": "LDL, HDL, Triglyzeride, Entzündungskontext und weiterführende Lipidfragen.",
            "fr": "LDL, HDL, triglycérides, inflammation et questions de suivi lipidique.",
            "it": "LDL, HDL, trigliceridi, contesto infiammatorio e follow-up lipidico.",
            "he": "LDL, HDL, טריגליצרידים, הקשר דלקתי ושאלות המשך.",
            "hi": "LDL, HDL, ट्राइग्लिसराइड्स, सूजन संदर्भ और आगे के सवाल।",
            "ar": "LDL وHDL والدهون الثلاثية والسياق الالتهابي ومتابعة الدهون.",
        },
        [
            ("article", "ldl-vs-hdl-what-it-means"),
            ("article", "apob-meaning"),
            ("article", "lpa-meaning"),
            ("article", "triglycerides-high-meaning"),
            ("article", "crp-what-it-means"),
        ],
    ),
]


def _blog_index_card_for_article(lang: str, article_id: str) -> dict | None:
    """Return label/path/desc for blog index widgets, or None if the article is unavailable in `lang`."""
    lang = _normalize_lang(lang)
    art = _ARTICLE_BY_ID.get(article_id)
    if not art or lang not in art.slugs:
        return None
    return {
        "label": art.titles.get(lang) or art.titles.get(DEFAULT_BLOG_LANG, ""),
        "path": f"/{lang}/blog/{art.slugs[lang]}",
        "desc": art.excerpts.get(lang) or art.excerpts.get(DEFAULT_BLOG_LANG, ""),
    }


def build_blog_index_definition_links(lang: str) -> List[dict]:
    """Localized quick-definition cards for /{lang}/blog (skips articles missing in that locale)."""
    lang = _normalize_lang(lang)
    out: List[dict] = []
    for aid in BLOG_INDEX_DEFINITION_ARTICLE_IDS:
        row = _blog_index_card_for_article(lang, aid)
        if row:
            out.append(row)
    return out


def build_blog_index_topic_clusters(lang: str) -> List[dict]:
    """Topic cluster cards for /{lang}/blog; links resolve per locale; empty clusters are omitted."""
    lang = _normalize_lang(lang)
    clusters: List[dict] = []
    for titles, descs, specs in _BLOG_TOPIC_CLUSTER_SPECS:
        title = titles.get(lang) or titles.get("en", "")
        desc = descs.get(lang) or descs.get("en", "")
        links: List[dict] = []
        for spec in specs:
            if spec[0] == "cbc_guide":
                if lang in _BLOG_TOPIC_CLUSTER_CBC_GUIDE_LANGS:
                    lab = _CBC_GUIDE_LINK_LABELS.get(lang) or _CBC_GUIDE_LINK_LABELS["en"]
                    links.append({"label": lab, "path": f"/{lang}/guides/how-to-read-cbc"})
            elif spec[0] == "article":
                card = _blog_index_card_for_article(lang, spec[1])
                if card:
                    links.append({"label": card["label"], "path": card["path"]})
        if links:
            clusters.append({"title": title, "desc": desc, "links": links})
    return clusters


def get_blog_icon_paths() -> List[str]:
    """Blog makalelerinde referans verilen tüm ikon dosya yollarını döner (/static/ sonrası, static köküne göre).
    Örnek: 'images/blog/icons/albumin-low-meaning.svg'
    Eksik dosyaların başlangıçta tespiti için kullanılır."""
    paths: List[str] = []
    for art in ARTICLES:
        icon = getattr(art, "icon", None)
        if not icon or not isinstance(icon, str):
            continue
        if icon.startswith("/static/"):
            paths.append(icon[len("/static/"):].lstrip("/"))
        elif icon.startswith("static/"):
            paths.append(icon[len("static/"):].lstrip("/"))
    return paths


def _normalize_lang(lang: str | None) -> str:
    if not lang:
        return DEFAULT_BLOG_LANG
    lang = lang.lower()[:5]
    if lang in BLOG_LANGS:
        return lang
    short = lang.split("-")[0]
    return short if short in BLOG_LANGS else DEFAULT_BLOG_LANG


@lru_cache(maxsize=512)
def _resolve_cover_image(cover_image: str | None) -> str:
    """Return a valid cover image path or a safe fallback if file is missing.
    Prefers compressed .jpg over .png when both exist."""
    if not cover_image or not isinstance(cover_image, str):
        return BLOG_COVER_FALLBACK
    path = cover_image.strip()
    if not path:
        return BLOG_COVER_FALLBACK

    def _prefer_jpg(static_rel: str, url_prefix: str) -> str | None:
        """If a .png is requested and .jpg exists, prefer .jpg for smaller file size."""
        if static_rel.lower().endswith(".png"):
            jpg_rel = static_rel[:-4] + ".jpg"
            if (_STATIC_ROOT / jpg_rel).is_file():
                return url_prefix + jpg_rel
        if (_STATIC_ROOT / static_rel).is_file():
            return url_prefix + static_rel
        return None

    if path.startswith("/static/"):
        rel = path[len("/static/"):].lstrip("/")
        result = _prefer_jpg(rel, "/static/")
        return result if result else BLOG_COVER_FALLBACK
    if path.startswith("static/"):
        rel = path[len("static/"):].lstrip("/")
        result = _prefer_jpg(rel, "/static/")
        return result if result else BLOG_COVER_FALLBACK
    if path.startswith("http://") or path.startswith("https://"):
        return path
    return BLOG_COVER_FALLBACK


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
                "cover_image": _resolve_cover_image(art.cover_image),
                "cover_alt": cover_alt,
                "read_minutes": art.read_minutes,
                "published_at": art.published_at,
                "icon": getattr(art, "icon", None),
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
                "cover_image": _resolve_cover_image(art.cover_image),
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
                "icon": getattr(art, "icon", None),
            }
    return None


def iter_all_article_paths():
    """Sitemap için tüm dil+slug kombinasyonlarını döner (last_updated = updatedAt).

    Yalnızca BLOG_LANGS_PREMIUM: /{lang}/blog/{slug} rotası bu dillerde 200 verir;
    el/cs/sr vb. çeviriler veri içinde olsa bile canlı blog URL'si yok — sitemap'e eklenmez.
    """
    for art in ARTICLES:
        last_updated = getattr(art, "last_updated", None) or art.published_at
        for lang, slug in art.slugs.items():
            if lang not in BLOG_LANGS_PREMIUM:
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

