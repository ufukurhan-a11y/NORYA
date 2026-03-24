"""Blood Test Results Explained — landing page i18n content for all supported locales."""
from __future__ import annotations

EXPLAINED_SLUGS: dict[str, str] = {
    "en": "blood-test-results-explained",
    "tr": "kan-tahlili-sonuclari-aciklama",
    "de": "blutwerte-erklart",
    "es": "blood-test-results-explained",
    "fr": "blood-test-results-explained",
    "it": "blood-test-results-explained",
    "he": "blood-test-results-explained",
    "hi": "blood-test-results-explained",
    "ar": "blood-test-results-explained",
}


def _en() -> dict:
    return {
        "meta_title": "Blood Test Results Explained \u2014 What Your Report Actually Means | NoryaAI",
        "meta_description": "Not sure what your blood test results mean? Learn how to read abbreviations, reference ranges, and units \u2014 and how a structured AI report can make it clearer.",
        "hero_title": "Blood Test Results Explained",
        "hero_sub": "Lab reports are packed with abbreviations, numbers, and ranges that most people were never taught to read. This guide covers what makes them confusing, what to look for, and how a structured approach can help you understand your results before your next doctor visit.",
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "See a sample report",
        "confusing_title": "Why blood test reports can feel confusing",
        "confusing_sub": "You are not the only one who finds lab reports hard to read. Here are the most common reasons people struggle with them.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "Unfamiliar abbreviations",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 lab reports are full of shorthand that is rarely explained on the document itself.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Reference ranges that vary",
                "desc": "What counts as \u201cnormal\u201d can differ between labs, age groups, and even measurement methods. A value that is flagged at one lab may be fine at another.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "Different units, same test",
                "desc": "Hemoglobin in g/dL or g/L? Glucose in mg/dL or mmol/L? The same biomarker can appear in different units depending on the country or lab.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "Dense formatting, no explanation",
                "desc": "Most lab reports are designed for clinicians, not patients. You get rows of numbers but no context about what they mean for you.",
            },
        ],
        "clarify_title": "What NoryaAI helps clarify",
        "clarify_sub": "NoryaAI does not replace your doctor. It gives you a structured, readable version of your results so you can walk into your appointment better informed.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "Plain-language explanations",
                "desc": "Each biomarker comes with a clear, jargon-free explanation of what it measures and why it matters.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Reference ranges in context",
                "desc": "Your values are shown alongside reference ranges so you can see where you stand \u2014 high, low, or within normal limits.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "Flagged markers",
                "desc": "Values outside the expected range are highlighted so you can focus on what may need attention.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Structured categories",
                "desc": "Results are grouped by category \u2014 liver, kidney, thyroid, blood cells, and more \u2014 instead of a flat list of numbers.",
            },
            {
                "icon": "\U0001f310",
                "title": "Multilingual reports",
                "desc": "Get your report in 9+ languages with medical context preserved. Useful when your lab report is in a language you do not fully understand.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Doctor-ready summary",
                "desc": "A clean PDF with a health score and QR verification that you can print, save, or share at your next appointment.",
            },
        ],
        "common_title": "Common things people look for in their results",
        "common_sub": "These are some of the most frequently searched biomarkers and panels. NoryaAI covers all of them in its structured reports.",
        "common_items": [
            {"title": "Complete Blood Count (CBC)", "desc": "WBC, RBC, hemoglobin, hematocrit, platelets \u2014 the most common panel in routine checkups."},
            {"title": "Liver function (ALT, AST, ALP)", "desc": "Enzymes that indicate how well your liver is working. Often checked in routine bloodwork."},
            {"title": "Kidney function (BUN, creatinine)", "desc": "Markers that show how effectively your kidneys are filtering waste from your blood."},
            {"title": "Thyroid panel (TSH, T3, T4)", "desc": "Hormones that regulate metabolism, energy levels, and body temperature."},
            {"title": "Blood sugar (glucose, HbA1c)", "desc": "Fasting glucose and long-term average blood sugar. Key markers for metabolic health."},
            {"title": "Cholesterol & lipids (LDL, HDL, triglycerides)", "desc": "Lipid panel results that are commonly discussed in cardiovascular health assessments."},
            {"title": "Iron & ferritin", "desc": "Markers related to iron storage and transport. Relevant for fatigue, anemia, and general energy levels."},
            {"title": "Vitamin D & B12", "desc": "Common vitamin levels that many people have checked, especially in routine annual bloodwork."},
            {"title": "Inflammation markers (CRP, ESR)", "desc": "General indicators of inflammation in the body. Often used as a screening baseline."},
        ],
        "how_title": "How it works",
        "how_sub": "Three steps from a confusing lab report to a structured summary you can actually understand.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Upload your report",
                "desc": "PDF, photo, or pasted text. Choose whatever is easiest.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI structures your data",
                "desc": "Values, units, and ranges are extracted and organized into clear categories.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Get your explained report",
                "desc": "Health score, flagged markers, plain-language explanations, and a downloadable PDF.",
            },
        ],
        "preview_title": "What your explained report looks like",
        "preview_sub": "Here is a glimpse of how NoryaAI structures and explains your blood test results.",
        "preview_lines": [
            {"label": "Health Score", "value": "78 / 100 \u2014 Good overall, a few markers to review"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 Normal white blood cell count (4.5\u201311.0)"},
            {"label": "Hemoglobin", "value": "14.2 g/dL \u2014 Within reference range (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 Slightly elevated liver enzyme (normal: 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Normal thyroid function (0.4\u20134.0)"},
            {"label": "Vitamin D", "value": "18 ng/mL \u2014 Below recommended level (30\u2013100)"},
        ],
        "preview_disclaimer": "Sample data for illustration only. Your actual report will reflect your personal lab values, units, and reference ranges.",
        "faqs": [
            {
                "q": "What does \u201cblood test results explained\u201d actually mean?",
                "a": "It means turning the raw numbers, abbreviations, and reference ranges on your lab report into plain-language explanations you can understand \u2014 with context about what each value measures and whether it falls within normal limits.",
            },
            {
                "q": "Can NoryaAI explain any type of blood test?",
                "a": "NoryaAI supports most standard blood panels including CBC, metabolic panels, liver and kidney function, thyroid, lipids, vitamins, and inflammation markers. If your report contains values it can parse, they will be included in your structured summary.",
            },
            {
                "q": "Is this a medical diagnosis?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions, recommend treatments, or replace professional medical advice. Always consult a qualified healthcare professional.",
            },
            {
                "q": "Why do reference ranges differ between labs?",
                "a": "Labs use different equipment, methods, and population samples to establish their ranges. Age, sex, and even altitude can influence what a lab considers \u201cnormal.\u201d This is why the same value might be flagged at one lab but not another.",
            },
            {
                "q": "Can I get my results explained in another language?",
                "a": "Yes. NoryaAI generates reports in 9+ languages including English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic \u2014 with medical context preserved in translation.",
            },
            {
                "q": "How is this different from just Googling my results?",
                "a": "Googling individual values one by one gives you scattered, generic information. NoryaAI reads your entire report at once, compares each value against its reference range, and produces a single structured summary with a health score, flagged markers, and categories \u2014 all in one place.",
            },
        ],
        "cta_title": "Ready to understand your blood test?",
        "cta_sub": "Upload your lab report and get a clear, structured summary with plain-language explanations \u2014 in minutes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
    }


def _tr() -> dict:
    return {
        "meta_title": "Kan Tahlili Sonu\u00e7lar\u0131 A\u00e7\u0131klamas\u0131 \u2014 Raporunuz Ger\u00e7ekte Ne Anlat\u0131yor | NoryaAI",
        "meta_description": "Kan tahlili sonu\u00e7lar\u0131n\u0131z\u0131 anlamakta zorlan\u0131yor musunuz? K\u0131saltmalar\u0131, referans aral\u0131klar\u0131n\u0131 ve birimleri nas\u0131l okuyaca\u011f\u0131n\u0131z\u0131 \u00f6\u011frenin \u2014 yap\u0131land\u0131r\u0131lm\u0131\u015f bir AI raporu ile daha net anlay\u0131n.",
        "hero_title": "Kan Tahlili Sonu\u00e7lar\u0131 A\u00e7\u0131klamas\u0131",
        "hero_sub": "Laboratuvar raporlar\u0131 \u00e7o\u011fu insan\u0131n okumay\u0131 \u00f6\u011frenmedi\u011fi k\u0131saltmalar, say\u0131lar ve referans aral\u0131klar\u0131yla doludur. Bu rehber, raporlar\u0131n neden kafa kar\u0131\u015ft\u0131r\u0131c\u0131 oldu\u011funu, nelere dikkat etmeniz gerekti\u011fini ve yap\u0131land\u0131r\u0131lm\u0131\u015f bir yakla\u015f\u0131m\u0131n doktor ziyaretinizden \u00f6nce sonu\u00e7lar\u0131n\u0131z\u0131 anlaman\u0131za nas\u0131l yard\u0131mc\u0131 olabilece\u011fini a\u00e7\u0131klar.",
        "cta_hero_primary": "Kan tahlilimi analiz et",
        "cta_hero_secondary": "\u00d6rnek raporu g\u00f6r",
        "confusing_title": "Kan tahlili raporlar\u0131 neden kafa kar\u0131\u015ft\u0131r\u0131c\u0131 olabiliyor",
        "confusing_sub": "Laboratuvar raporlar\u0131n\u0131 anlamakta zorlanan tek ki\u015fi siz de\u011filsiniz. \u0130\u015fte insanlar\u0131n en \u00e7ok zorland\u0131\u011f\u0131 noktalar.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "Tan\u0131mad\u0131k k\u0131saltmalar",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 laboratuvar raporlar\u0131 belgenin \u00fczerinde nadiren a\u00e7\u0131klanan k\u0131saltmalarla doludur.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "De\u011fi\u015fken referans aral\u0131klar\u0131",
                "desc": "\u201cNormal\u201d kabul edilen de\u011ferler laboratuvarlar, ya\u015f gruplar\u0131 ve hatta \u00f6l\u00e7\u00fcm y\u00f6ntemleri aras\u0131nda farkl\u0131l\u0131k g\u00f6sterebilir. Bir laboratuvarda i\u015faretlenen de\u011fer ba\u015fka birinde normal olabilir.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "Farkl\u0131 birimler, ayn\u0131 test",
                "desc": "Hemoglobin g/dL mi yoksa g/L mi? Glikoz mg/dL mi yoksa mmol/L mi? Ayn\u0131 biyo belirte\u00e7 \u00fclkeye veya laboratuvara g\u00f6re farkl\u0131 birimlerde g\u00f6r\u00fcnebilir.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "Yo\u011fun format, a\u00e7\u0131klama yok",
                "desc": "\u00c7o\u011fu laboratuvar raporu hastalar i\u00e7in de\u011fil, klinisyenler i\u00e7in tasarlanm\u0131\u015ft\u0131r. Sat\u0131rlar dolusu say\u0131 g\u00f6r\u00fcrs\u00fcn\u00fcz ama sizin i\u00e7in ne anlama geldi\u011fine dair bir ba\u011flam yoktur.",
            },
        ],
        "clarify_title": "NoryaAI neleri a\u00e7\u0131kl\u0131yor",
        "clarify_sub": "NoryaAI doktorunuzun yerini almaz. Sonu\u00e7lar\u0131n\u0131z\u0131n yap\u0131land\u0131r\u0131lm\u0131\u015f, okunabilir bir versiyonunu sunar; b\u00f6ylece randevunuza daha bilgili gidersiniz.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "Sade dilde a\u00e7\u0131klamalar",
                "desc": "Her biyo belirte\u00e7, neyi \u00f6l\u00e7t\u00fc\u011f\u00fcn\u00fc ve neden \u00f6nemli oldu\u011funu anlatan net, jargondan ar\u0131nd\u0131r\u0131lm\u0131\u015f bir a\u00e7\u0131klama ile birlikte sunulur.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Ba\u011flam i\u00e7inde referans aral\u0131klar\u0131",
                "desc": "De\u011ferleriniz referans aral\u0131klar\u0131yla birlikte g\u00f6sterilir; b\u00f6ylece y\u00fcksek, d\u00fc\u015f\u00fck veya normal s\u0131n\u0131rlar i\u00e7inde olup olmad\u0131\u011f\u0131n\u0131z\u0131 g\u00f6rebilirsiniz.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "\u0130\u015faretlenmi\u015f de\u011ferler",
                "desc": "Beklenen aral\u0131\u011f\u0131n d\u0131\u015f\u0131ndaki de\u011ferler vurgulan\u0131r, b\u00f6ylece dikkat gerektiren noktalara odaklanabilirsiniz.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Yap\u0131land\u0131r\u0131lm\u0131\u015f kategoriler",
                "desc": "Sonu\u00e7lar d\u00fcz bir say\u0131 listesi yerine karaci\u011fer, b\u00f6brek, tiroid, kan h\u00fccreleri ve daha fazlas\u0131 olarak kategorilere ayr\u0131l\u0131r.",
            },
            {
                "icon": "\U0001f310",
                "title": "\u00c7ok dilli raporlar",
                "desc": "Raporunuzu t\u0131bbi ba\u011flam korunarak 9+ dilde al\u0131n. Laboratuvar raporunuz tam olarak anlamad\u0131\u011f\u0131n\u0131z bir dildeyse \u00f6zellikle faydal\u0131d\u0131r.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Doktora haz\u0131r \u00f6zet",
                "desc": "Sa\u011fl\u0131k skoru ve QR do\u011frulamas\u0131 i\u00e7eren temiz bir PDF; yazd\u0131rabilir, kaydedebilir veya bir sonraki randevunuzda payla\u015fabilirsiniz.",
            },
        ],
        "common_title": "Sonu\u00e7larda en \u00e7ok aranan de\u011ferler",
        "common_sub": "Bunlar en s\u0131k aranan biyo belirte\u00e7ler ve panellerdir. NoryaAI yap\u0131land\u0131r\u0131lm\u0131\u015f raporlar\u0131nda hepsini kapsar.",
        "common_items": [
            {"title": "Tam Kan Say\u0131m\u0131 (Hemogram)", "desc": "WBC, RBC, hemoglobin, hematokrit, trombositler \u2014 rutin kontrollerdeki en yayg\u0131n panel."},
            {"title": "Karaci\u011fer fonksiyonu (ALT, AST, ALP)", "desc": "Karaci\u011ferinizin ne kadar iyi \u00e7al\u0131\u015ft\u0131\u011f\u0131n\u0131 g\u00f6steren enzimler. Rutin kan tahlillerinde s\u0131kl\u0131kla kontrol edilir."},
            {"title": "B\u00f6brek fonksiyonu (BUN, kreatinin)", "desc": "B\u00f6breklerinizin kan\u0131n\u0131zdaki at\u0131k maddeleri ne kadar etkili filtreledi\u011fini g\u00f6steren belirte\u00e7ler."},
            {"title": "Tiroid paneli (TSH, T3, T4)", "desc": "Metabolizmay\u0131, enerji seviyelerini ve v\u00fccut \u0131s\u0131s\u0131n\u0131 d\u00fczenleyen hormonlar."},
            {"title": "Kan \u015fekeri (glikoz, HbA1c)", "desc": "A\u00e7l\u0131k glikozu ve uzun vadeli ortalama kan \u015fekeri. Metabolik sa\u011fl\u0131k i\u00e7in anahtar belirte\u00e7ler."},
            {"title": "Kolesterol ve lipitler (LDL, HDL, trigliseritler)", "desc": "Kardiyovask\u00fcler sa\u011fl\u0131k de\u011ferlendirmelerinde yayg\u0131n olarak tart\u0131\u015f\u0131lan lipit paneli sonu\u00e7lar\u0131."},
            {"title": "Demir ve ferritin", "desc": "Demir depolama ve ta\u015f\u0131nmas\u0131yla ilgili belirte\u00e7ler. Yorgunluk, anemi ve genel enerji seviyeleri i\u00e7in \u00f6nemlidir."},
            {"title": "D Vitamini ve B12", "desc": "\u00d6zellikle y\u0131ll\u0131k rutin kan tahlillerinde s\u0131kl\u0131kla kontrol edilen yayg\u0131n vitamin seviyeleri."},
            {"title": "\u0130nflamasyon belirte\u00e7leri (CRP, ESR)", "desc": "V\u00fccuttaki genel iltihap g\u00f6stergeleri. Genellikle tarama ba\u015flang\u0131c\u0131 olarak kullan\u0131l\u0131r."},
        ],
        "how_title": "Nas\u0131l \u00e7al\u0131\u015f\u0131r",
        "how_sub": "Kafa kar\u0131\u015ft\u0131r\u0131c\u0131 bir laboratuvar raporundan ger\u00e7ekten anlayabilece\u011finiz yap\u0131land\u0131r\u0131lm\u0131\u015f bir \u00f6zete \u00fc\u00e7 ad\u0131m.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Raporunuzu y\u00fckleyin",
                "desc": "PDF, foto\u011fraf veya yap\u0131\u015ft\u0131r\u0131lm\u0131\u015f metin. Hangisi kolaysa onu se\u00e7in.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI verilerinizi yap\u0131land\u0131r\u0131r",
                "desc": "De\u011ferler, birimler ve aral\u0131klar \u00e7\u0131kar\u0131l\u0131r ve net kategorilere ayr\u0131l\u0131r.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "A\u00e7\u0131klamal\u0131 raporunuzu al\u0131n",
                "desc": "Sa\u011fl\u0131k skoru, i\u015faretlenmi\u015f de\u011ferler, sade dilde a\u00e7\u0131klamalar ve indirilebilir PDF.",
            },
        ],
        "preview_title": "A\u00e7\u0131klamal\u0131 raporunuz neye benziyor",
        "preview_sub": "NoryaAI\u2019\u0131n kan tahlili sonu\u00e7lar\u0131n\u0131z\u0131 nas\u0131l yap\u0131land\u0131r\u0131p a\u00e7\u0131klad\u0131\u011f\u0131na dair bir \u00f6nizleme.",
        "preview_lines": [
            {"label": "Sa\u011fl\u0131k Skoru", "value": "78 / 100 \u2014 Genel olarak iyi, birka\u00e7 de\u011fer incelenmeli"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 Normal beyaz kan h\u00fccresi say\u0131s\u0131 (4.5\u201311.0)"},
            {"label": "Hemoglobin", "value": "14.2 g/dL \u2014 Referans aral\u0131\u011f\u0131nda (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 Hafif y\u00fcksek karaci\u011fer enzimi (normal: 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Normal tiroid fonksiyonu (0.4\u20134.0)"},
            {"label": "D Vitamini", "value": "18 ng/mL \u2014 \u00d6nerilen seviyenin alt\u0131nda (30\u2013100)"},
        ],
        "preview_disclaimer": "Yaln\u0131zca g\u00f6sterim ama\u00e7l\u0131 \u00f6rnek veriler. Ger\u00e7ek raporunuz ki\u015fisel laboratuvar de\u011ferlerinizi, birimlerinizi ve referans aral\u0131klar\u0131n\u0131z\u0131 yans\u0131tacakt\u0131r.",
        "faqs": [
            {
                "q": "\u201cKan tahlili sonu\u00e7lar\u0131 a\u00e7\u0131klamas\u0131\u201d tam olarak ne demek?",
                "a": "Laboratuvar raporunuzdaki ham say\u0131lar\u0131, k\u0131saltmalar\u0131 ve referans aral\u0131klar\u0131n\u0131, her de\u011ferin neyi \u00f6l\u00e7t\u00fc\u011f\u00fc ve normal s\u0131n\u0131rlar i\u00e7inde olup olmad\u0131\u011f\u0131 hakk\u0131nda ba\u011flam ile birlikte sade dilde a\u00e7\u0131klamalara d\u00f6n\u00fc\u015ft\u00fcrmek demektir.",
            },
            {
                "q": "NoryaAI her t\u00fcr kan tahlilini a\u00e7\u0131klayabilir mi?",
                "a": "NoryaAI; hemogram, metabolik paneller, karaci\u011fer ve b\u00f6brek fonksiyonlar\u0131, tiroid, lipitler, vitaminler ve inflamasyon belirte\u00e7leri dahil \u00e7o\u011fu standart kan panelini destekler. Raporunuz ayr\u0131\u015ft\u0131rabilece\u011fi de\u011ferler i\u00e7eriyorsa, bunlar yap\u0131land\u0131r\u0131lm\u0131\u015f \u00f6zetinize dahil edilecektir.",
            },
            {
                "q": "Bu t\u0131bbi bir te\u015fhis midir?",
                "a": "Hay\u0131r. NoryaAI laboratuvar de\u011ferlerinizin yap\u0131land\u0131r\u0131lm\u0131\u015f, e\u011fitici a\u00e7\u0131klamalar\u0131n\u0131 sunar. Hastal\u0131k te\u015fhisi koymaz, tedavi \u00f6nermez veya profesyonel t\u0131bbi tavsiyelerin yerini almaz. Her zaman yetkin bir sa\u011fl\u0131k uzman\u0131na dan\u0131\u015f\u0131n.",
            },
            {
                "q": "Referans aral\u0131klar\u0131 neden laboratuvarlar aras\u0131nda farkl\u0131l\u0131k g\u00f6steriyor?",
                "a": "Laboratuvarlar aral\u0131klar\u0131n\u0131 belirlemek i\u00e7in farkl\u0131 ekipman, y\u00f6ntem ve pop\u00fclasyon \u00f6rnekleri kullan\u0131r. Ya\u015f, cinsiyet ve hatta rak\u0131m bile bir laboratuvar\u0131n neyi \u201cnormal\u201d kabul etti\u011fini etkileyebilir. Bu nedenle ayn\u0131 de\u011fer bir laboratuvarda i\u015faretlenirken di\u011ferinde i\u015faretlenmeyebilir.",
            },
            {
                "q": "Sonu\u00e7lar\u0131m\u0131 ba\u015fka bir dilde a\u00e7\u0131klatabilir miyim?",
                "a": "Evet. NoryaAI; \u0130ngilizce, Almanca, T\u00fcrk\u00e7e, Frans\u0131zca, \u0130talyanca, \u0130spanyolca, \u0130branice, Hintce ve Arap\u00e7a dahil 9+ dilde t\u0131bbi ba\u011flam\u0131 koruyarak raporlar \u00fcretir.",
            },
            {
                "q": "Bu, sonu\u00e7lar\u0131m\u0131 Google\u2019da aramaktan ne fark\u0131 var?",
                "a": "Tek tek de\u011ferleri Google\u2019da aramak da\u011f\u0131n\u0131k, genel bilgiler verir. NoryaAI t\u00fcm raporunuzu ayn\u0131 anda okur, her de\u011feri referans aral\u0131\u011f\u0131yla kar\u015f\u0131la\u015ft\u0131r\u0131r ve sa\u011fl\u0131k skoru, i\u015faretlenmi\u015f de\u011ferler ve kategorilerle tek bir yap\u0131land\u0131r\u0131lm\u0131\u015f \u00f6zet \u00fcretir \u2014 hepsi tek bir yerde.",
            },
        ],
        "cta_title": "Kan tahlilinizi anlamaya haz\u0131r m\u0131s\u0131n\u0131z?",
        "cta_sub": "Laboratuvar raporunuzu y\u00fckleyin ve dakikalar i\u00e7inde sade dilde a\u00e7\u0131klamalarla net, yap\u0131land\u0131r\u0131lm\u0131\u015f bir \u00f6zet al\u0131n.",
        "cta_primary": "Y\u00fckle ve analiz et",
        "cta_secondary": "Fiyatland\u0131rmay\u0131 g\u00f6r",
    }


def _de() -> dict:
    return {
        "meta_title": "Blutwerte erkl\u00e4rt \u2014 Was Ihr Laborbericht wirklich bedeutet | NoryaAI",
        "meta_description": "Sie verstehen Ihre Blutwerte nicht? Erfahren Sie, wie Sie Abk\u00fcrzungen, Referenzbereiche und Einheiten lesen \u2014 und wie ein strukturierter KI-Bericht f\u00fcr Klarheit sorgt.",
        "hero_title": "Blutwerte erkl\u00e4rt",
        "hero_sub": "Laborberichte sind voller Abk\u00fcrzungen, Zahlen und Referenzbereiche, die die meisten Menschen nie gelernt haben zu lesen. Dieser Leitfaden erkl\u00e4rt, warum sie verwirrend sind, worauf Sie achten sollten und wie ein strukturierter Ansatz Ihnen helfen kann, Ihre Ergebnisse vor dem n\u00e4chsten Arztbesuch zu verstehen.",
        "cta_hero_primary": "Meine Blutwerte analysieren",
        "cta_hero_secondary": "Beispielbericht ansehen",
        "confusing_title": "Warum Laborberichte verwirrend sein k\u00f6nnen",
        "confusing_sub": "Sie sind nicht die einzige Person, die Laborberichte schwer lesbar findet. Hier sind die h\u00e4ufigsten Gr\u00fcnde.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "Unbekannte Abk\u00fcrzungen",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 Laborberichte sind voller K\u00fcrzel, die auf dem Dokument selbst selten erkl\u00e4rt werden.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Variierende Referenzbereiche",
                "desc": "Was als \u201enormal\u201c gilt, kann je nach Labor, Altersgruppe und sogar Messmethode variieren. Ein Wert, der in einem Labor auff\u00e4llig ist, kann in einem anderen v\u00f6llig in Ordnung sein.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "Verschiedene Einheiten, gleicher Test",
                "desc": "H\u00e4moglobin in g/dL oder g/L? Glukose in mg/dL oder mmol/L? Derselbe Biomarker kann je nach Land oder Labor in verschiedenen Einheiten erscheinen.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "Dichtes Format, keine Erkl\u00e4rung",
                "desc": "Die meisten Laborberichte sind f\u00fcr \u00c4rzte konzipiert, nicht f\u00fcr Patienten. Sie sehen Zahlenreihen, aber keinen Kontext dar\u00fcber, was sie f\u00fcr Sie bedeuten.",
            },
        ],
        "clarify_title": "Was NoryaAI verdeutlicht",
        "clarify_sub": "NoryaAI ersetzt nicht Ihren Arzt. Es gibt Ihnen eine strukturierte, lesbare Version Ihrer Ergebnisse, damit Sie besser informiert zu Ihrem Termin gehen.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "Verst\u00e4ndliche Erkl\u00e4rungen",
                "desc": "Jeder Biomarker wird mit einer klaren, jargonfreien Erkl\u00e4rung versehen, was er misst und warum er wichtig ist.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Referenzbereiche im Kontext",
                "desc": "Ihre Werte werden neben den Referenzbereichen angezeigt, damit Sie sehen k\u00f6nnen, wo Sie stehen \u2014 hoch, niedrig oder im Normalbereich.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "Markierte Werte",
                "desc": "Werte au\u00dferhalb des erwarteten Bereichs werden hervorgehoben, damit Sie sich auf das konzentrieren k\u00f6nnen, was m\u00f6glicherweise Aufmerksamkeit erfordert.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Strukturierte Kategorien",
                "desc": "Ergebnisse werden nach Kategorie gruppiert \u2014 Leber, Niere, Schilddr\u00fcse, Blutzellen und mehr \u2014 statt als flache Zahlenliste.",
            },
            {
                "icon": "\U0001f310",
                "title": "Mehrsprachige Berichte",
                "desc": "Erhalten Sie Ihren Bericht in 9+ Sprachen mit erhaltener medizinischer Bedeutung. N\u00fctzlich, wenn Ihr Laborbericht in einer Sprache ist, die Sie nicht vollst\u00e4ndig verstehen.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Arztfertige Zusammenfassung",
                "desc": "Ein sauberes PDF mit Gesundheitsscore und QR-Verifizierung, das Sie ausdrucken, speichern oder bei Ihrem n\u00e4chsten Termin teilen k\u00f6nnen.",
            },
        ],
        "common_title": "H\u00e4ufig gesuchte Werte in Laborberichten",
        "common_sub": "Dies sind einige der am h\u00e4ufigsten gesuchten Biomarker und Panels. NoryaAI deckt sie alle in seinen strukturierten Berichten ab.",
        "common_items": [
            {"title": "Gro\u00dfes Blutbild (CBC)", "desc": "WBC, RBC, H\u00e4moglobin, H\u00e4matokrit, Thrombozyten \u2014 das h\u00e4ufigste Panel bei Routineuntersuchungen."},
            {"title": "Leberfunktion (ALT, AST, ALP)", "desc": "Enzyme, die anzeigen, wie gut Ihre Leber arbeitet. Werden h\u00e4ufig bei Routine-Blutuntersuchungen kontrolliert."},
            {"title": "Nierenfunktion (BUN, Kreatinin)", "desc": "Marker, die zeigen, wie effektiv Ihre Nieren Abfallstoffe aus Ihrem Blut filtern."},
            {"title": "Schilddr\u00fcsenpanel (TSH, T3, T4)", "desc": "Hormone, die Stoffwechsel, Energieniveau und K\u00f6rpertemperatur regulieren."},
            {"title": "Blutzucker (Glukose, HbA1c)", "desc": "N\u00fcchternglukose und langfristiger Blutzuckerdurchschnitt. Schl\u00fcsselmarker f\u00fcr die metabolische Gesundheit."},
            {"title": "Cholesterin & Lipide (LDL, HDL, Triglyceride)", "desc": "Lipidpanel-Ergebnisse, die h\u00e4ufig bei kardiovaskul\u00e4ren Gesundheitsbewertungen besprochen werden."},
            {"title": "Eisen & Ferritin", "desc": "Marker f\u00fcr Eisenspeicherung und -transport. Relevant bei M\u00fcdigkeit, An\u00e4mie und allgemeinem Energieniveau."},
            {"title": "Vitamin D & B12", "desc": "H\u00e4ufig kontrollierte Vitaminspiegel, besonders bei j\u00e4hrlichen Routine-Blutuntersuchungen."},
            {"title": "Entz\u00fcndungsmarker (CRP, BSG)", "desc": "Allgemeine Indikatoren f\u00fcr Entz\u00fcndungen im K\u00f6rper. Werden h\u00e4ufig als Screening-Ausgangswert verwendet."},
        ],
        "how_title": "So funktioniert es",
        "how_sub": "Drei Schritte von einem verwirrenden Laborbericht zu einer strukturierten Zusammenfassung, die Sie tats\u00e4chlich verstehen.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Bericht hochladen",
                "desc": "PDF, Foto oder eingef\u00fcgter Text. W\u00e4hlen Sie, was am einfachsten ist.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "KI strukturiert Ihre Daten",
                "desc": "Werte, Einheiten und Bereiche werden extrahiert und in \u00fcbersichtliche Kategorien geordnet.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Erkl\u00e4rten Bericht erhalten",
                "desc": "Gesundheitsscore, markierte Werte, verst\u00e4ndliche Erkl\u00e4rungen und ein herunterladbares PDF.",
            },
        ],
        "preview_title": "So sieht Ihr erkl\u00e4rter Bericht aus",
        "preview_sub": "Hier sehen Sie, wie NoryaAI Ihre Blutwerte strukturiert und erkl\u00e4rt.",
        "preview_lines": [
            {"label": "Gesundheitsscore", "value": "78 / 100 \u2014 Insgesamt gut, einige Werte zur \u00dcberpr\u00fcfung"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 Normale Leukozytenzahl (4.5\u201311.0)"},
            {"label": "H\u00e4moglobin", "value": "14.2 g/dL \u2014 Im Referenzbereich (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 Leicht erh\u00f6htes Leberenzym (normal: 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Normale Schilddr\u00fcsenfunktion (0.4\u20134.0)"},
            {"label": "Vitamin D", "value": "18 ng/mL \u2014 Unter dem empfohlenen Wert (30\u2013100)"},
        ],
        "preview_disclaimer": "Beispieldaten nur zur Veranschaulichung. Ihr tats\u00e4chlicher Bericht spiegelt Ihre pers\u00f6nlichen Laborwerte, Einheiten und Referenzbereiche wider.",
        "faqs": [
            {
                "q": "Was bedeutet \u201eBlutwerte erkl\u00e4rt\u201c genau?",
                "a": "Es bedeutet, die Rohzahlen, Abk\u00fcrzungen und Referenzbereiche in Ihrem Laborbericht in verst\u00e4ndliche Erkl\u00e4rungen umzuwandeln \u2014 mit Kontext dar\u00fcber, was jeder Wert misst und ob er im Normalbereich liegt.",
            },
            {
                "q": "Kann NoryaAI jede Art von Bluttest erkl\u00e4ren?",
                "a": "NoryaAI unterst\u00fctzt die meisten Standard-Blutpanels einschlie\u00dflich gro\u00dfes Blutbild, Stoffwechselpanels, Leber- und Nierenfunktion, Schilddr\u00fcse, Lipide, Vitamine und Entz\u00fcndungsmarker. Wenn Ihr Bericht Werte enth\u00e4lt, die analysiert werden k\u00f6nnen, werden sie in Ihre strukturierte Zusammenfassung aufgenommen.",
            },
            {
                "q": "Ist das eine medizinische Diagnose?",
                "a": "Nein. NoryaAI bietet strukturierte, informative Erkl\u00e4rungen Ihrer Laborwerte. Es stellt keine Diagnosen, empfiehlt keine Behandlungen und ersetzt keine professionelle medizinische Beratung. Konsultieren Sie immer einen qualifizierten Arzt.",
            },
            {
                "q": "Warum unterscheiden sich Referenzbereiche zwischen Laboren?",
                "a": "Labore verwenden unterschiedliche Ger\u00e4te, Methoden und Populationsstichproben, um ihre Bereiche festzulegen. Alter, Geschlecht und sogar die H\u00f6henlage k\u00f6nnen beeinflussen, was ein Labor als \u201enormal\u201c betrachtet. Deshalb kann derselbe Wert in einem Labor auff\u00e4llig sein, in einem anderen jedoch nicht.",
            },
            {
                "q": "Kann ich meine Ergebnisse in einer anderen Sprache erkl\u00e4ren lassen?",
                "a": "Ja. NoryaAI erstellt Berichte in 9+ Sprachen, darunter Englisch, Deutsch, T\u00fcrkisch, Franz\u00f6sisch, Italienisch, Spanisch, Hebr\u00e4isch, Hindi und Arabisch \u2014 mit erhaltenem medizinischem Kontext.",
            },
            {
                "q": "Wie unterscheidet sich das vom einfachen Googeln meiner Werte?",
                "a": "Wenn Sie einzelne Werte nacheinander googeln, erhalten Sie verstreute, allgemeine Informationen. NoryaAI liest Ihren gesamten Bericht auf einmal, vergleicht jeden Wert mit seinem Referenzbereich und erstellt eine einzige strukturierte Zusammenfassung mit Gesundheitsscore, markierten Werten und Kategorien \u2014 alles an einem Ort.",
            },
        ],
        "cta_title": "Bereit, Ihre Blutwerte zu verstehen?",
        "cta_sub": "Laden Sie Ihren Laborbericht hoch und erhalten Sie in Minuten eine klare, strukturierte Zusammenfassung mit verst\u00e4ndlichen Erkl\u00e4rungen.",
        "cta_primary": "Hochladen und analysieren",
        "cta_secondary": "Preise ansehen",
    }


def _es() -> dict:
    return {
        "meta_title": "Resultados de an\u00e1lisis de sangre explicados \u2014 Qu\u00e9 significa realmente tu informe | NoryaAI",
        "meta_description": "\u00bfNo entiendes tus resultados de an\u00e1lisis de sangre? Aprende a leer abreviaturas, rangos de referencia y unidades \u2014 y c\u00f3mo un informe de IA estructurado puede hacerlo m\u00e1s claro.",
        "hero_title": "Resultados de an\u00e1lisis de sangre explicados",
        "hero_sub": "Los informes de laboratorio est\u00e1n llenos de abreviaturas, n\u00fameros y rangos que la mayor\u00eda de las personas nunca aprendi\u00f3 a leer. Esta gu\u00eda explica por qu\u00e9 son confusos, qu\u00e9 buscar y c\u00f3mo un enfoque estructurado puede ayudarte a entender tus resultados antes de tu pr\u00f3xima cita m\u00e9dica.",
        "cta_hero_primary": "Analizar mi an\u00e1lisis de sangre",
        "cta_hero_secondary": "Ver informe de ejemplo",
        "confusing_title": "Por qu\u00e9 los informes de an\u00e1lisis de sangre pueden ser confusos",
        "confusing_sub": "No eres la \u00fanica persona que encuentra dif\u00edciles de leer los informes de laboratorio. Estas son las razones m\u00e1s comunes.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "Abreviaturas desconocidas",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 los informes de laboratorio est\u00e1n llenos de siglas que rara vez se explican en el propio documento.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Rangos de referencia variables",
                "desc": "Lo que se considera \u201cnormal\u201d puede variar entre laboratorios, grupos de edad e incluso m\u00e9todos de medici\u00f3n. Un valor marcado en un laboratorio puede ser normal en otro.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "Diferentes unidades, misma prueba",
                "desc": "\u00bfHemoglobina en g/dL o g/L? \u00bfGlucosa en mg/dL o mmol/L? El mismo biomarcador puede aparecer en diferentes unidades seg\u00fan el pa\u00eds o laboratorio.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "Formato denso, sin explicaci\u00f3n",
                "desc": "La mayor\u00eda de los informes de laboratorio est\u00e1n dise\u00f1ados para m\u00e9dicos, no para pacientes. Ves filas de n\u00fameros pero sin contexto sobre lo que significan para ti.",
            },
        ],
        "clarify_title": "Qu\u00e9 aclara NoryaAI",
        "clarify_sub": "NoryaAI no reemplaza a tu m\u00e9dico. Te ofrece una versi\u00f3n estructurada y legible de tus resultados para que vayas a tu cita mejor informado.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "Explicaciones en lenguaje sencillo",
                "desc": "Cada biomarcador incluye una explicaci\u00f3n clara y sin jerga sobre qu\u00e9 mide y por qu\u00e9 es importante.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Rangos de referencia en contexto",
                "desc": "Tus valores se muestran junto con los rangos de referencia para que puedas ver d\u00f3nde te encuentras \u2014 alto, bajo o dentro de los l\u00edmites normales.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "Marcadores se\u00f1alados",
                "desc": "Los valores fuera del rango esperado se resaltan para que puedas centrarte en lo que puede necesitar atenci\u00f3n.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Categor\u00edas estructuradas",
                "desc": "Los resultados se agrupan por categor\u00eda \u2014 h\u00edgado, ri\u00f1\u00f3n, tiroides, c\u00e9lulas sangu\u00edneas y m\u00e1s \u2014 en lugar de una lista plana de n\u00fameros.",
            },
            {
                "icon": "\U0001f310",
                "title": "Informes multiling\u00fces",
                "desc": "Obt\u00e9n tu informe en 9+ idiomas con el contexto m\u00e9dico preservado. \u00datil cuando tu informe de laboratorio est\u00e1 en un idioma que no comprendes completamente.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Resumen listo para el m\u00e9dico",
                "desc": "Un PDF limpio con puntuaci\u00f3n de salud y verificaci\u00f3n QR que puedes imprimir, guardar o compartir en tu pr\u00f3xima cita.",
            },
        ],
        "common_title": "Lo que la gente busca com\u00fanmente en sus resultados",
        "common_sub": "Estos son algunos de los biomarcadores y paneles m\u00e1s buscados. NoryaAI los cubre todos en sus informes estructurados.",
        "common_items": [
            {"title": "Hemograma completo (CBC)", "desc": "WBC, RBC, hemoglobina, hematocrito, plaquetas \u2014 el panel m\u00e1s com\u00fan en chequeos de rutina."},
            {"title": "Funci\u00f3n hep\u00e1tica (ALT, AST, ALP)", "desc": "Enzimas que indican c\u00f3mo est\u00e1 funcionando tu h\u00edgado. Se verifican frecuentemente en an\u00e1lisis de rutina."},
            {"title": "Funci\u00f3n renal (BUN, creatinina)", "desc": "Marcadores que muestran cu\u00e1n eficazmente tus ri\u00f1ones filtran los desechos de tu sangre."},
            {"title": "Panel tiroideo (TSH, T3, T4)", "desc": "Hormonas que regulan el metabolismo, los niveles de energ\u00eda y la temperatura corporal."},
            {"title": "Az\u00facar en sangre (glucosa, HbA1c)", "desc": "Glucosa en ayunas y promedio de az\u00facar en sangre a largo plazo. Marcadores clave para la salud metab\u00f3lica."},
            {"title": "Colesterol y l\u00edpidos (LDL, HDL, triglic\u00e9ridos)", "desc": "Resultados del panel lip\u00eddico que se discuten com\u00fanmente en evaluaciones de salud cardiovascular."},
            {"title": "Hierro y ferritina", "desc": "Marcadores relacionados con el almacenamiento y transporte de hierro. Relevantes para fatiga, anemia y niveles generales de energ\u00eda."},
            {"title": "Vitamina D y B12", "desc": "Niveles comunes de vitaminas que muchas personas verifican, especialmente en an\u00e1lisis de sangre anuales de rutina."},
            {"title": "Marcadores de inflamaci\u00f3n (PCR, VSG)", "desc": "Indicadores generales de inflamaci\u00f3n en el cuerpo. Se usan frecuentemente como l\u00ednea base de detecci\u00f3n."},
        ],
        "how_title": "C\u00f3mo funciona",
        "how_sub": "Tres pasos desde un informe de laboratorio confuso hasta un resumen estructurado que realmente puedes entender.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Sube tu informe",
                "desc": "PDF, foto o texto pegado. Elige lo que sea m\u00e1s f\u00e1cil.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "La IA estructura tus datos",
                "desc": "Los valores, unidades y rangos se extraen y organizan en categor\u00edas claras.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Recibe tu informe explicado",
                "desc": "Puntuaci\u00f3n de salud, marcadores se\u00f1alados, explicaciones en lenguaje sencillo y un PDF descargable.",
            },
        ],
        "preview_title": "C\u00f3mo se ve tu informe explicado",
        "preview_sub": "Aqu\u00ed tienes un vistazo de c\u00f3mo NoryaAI estructura y explica tus resultados de an\u00e1lisis de sangre.",
        "preview_lines": [
            {"label": "Puntuaci\u00f3n de salud", "value": "78 / 100 \u2014 Bien en general, algunos marcadores para revisar"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 Recuento normal de gl\u00f3bulos blancos (4.5\u201311.0)"},
            {"label": "Hemoglobina", "value": "14.2 g/dL \u2014 Dentro del rango de referencia (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 Enzima hep\u00e1tica ligeramente elevada (normal: 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Funci\u00f3n tiroidea normal (0.4\u20134.0)"},
            {"label": "Vitamina D", "value": "18 ng/mL \u2014 Por debajo del nivel recomendado (30\u2013100)"},
        ],
        "preview_disclaimer": "Datos de ejemplo solo con fines ilustrativos. Tu informe real reflejar\u00e1 tus valores de laboratorio personales, unidades y rangos de referencia.",
        "faqs": [
            {
                "q": "\u00bfQu\u00e9 significa realmente \u201cresultados de an\u00e1lisis de sangre explicados\u201d?",
                "a": "Significa convertir los n\u00fameros, abreviaturas y rangos de referencia de tu informe de laboratorio en explicaciones en lenguaje sencillo que puedas entender \u2014 con contexto sobre qu\u00e9 mide cada valor y si est\u00e1 dentro de los l\u00edmites normales.",
            },
            {
                "q": "\u00bfPuede NoryaAI explicar cualquier tipo de an\u00e1lisis de sangre?",
                "a": "NoryaAI admite la mayor\u00eda de los paneles de sangre est\u00e1ndar, incluidos hemograma, paneles metab\u00f3licos, funci\u00f3n hep\u00e1tica y renal, tiroides, l\u00edpidos, vitaminas y marcadores de inflamaci\u00f3n. Si tu informe contiene valores que puede analizar, se incluir\u00e1n en tu resumen estructurado.",
            },
            {
                "q": "\u00bfEsto es un diagn\u00f3stico m\u00e9dico?",
                "a": "No. NoryaAI proporciona explicaciones estructuradas y educativas de tus valores de laboratorio. No diagnostica enfermedades, no recomienda tratamientos ni reemplaza el consejo m\u00e9dico profesional. Siempre consulta a un profesional de salud calificado.",
            },
            {
                "q": "\u00bfPor qu\u00e9 los rangos de referencia var\u00edan entre laboratorios?",
                "a": "Los laboratorios usan diferentes equipos, m\u00e9todos y muestras de poblaci\u00f3n para establecer sus rangos. La edad, el sexo e incluso la altitud pueden influir en lo que un laboratorio considera \u201cnormal\u201d. Por eso el mismo valor puede estar marcado en un laboratorio pero no en otro.",
            },
            {
                "q": "\u00bfPuedo obtener mis resultados explicados en otro idioma?",
                "a": "S\u00ed. NoryaAI genera informes en 9+ idiomas, incluidos ingl\u00e9s, alem\u00e1n, turco, franc\u00e9s, italiano, espa\u00f1ol, hebreo, hindi y \u00e1rabe \u2014 con el contexto m\u00e9dico preservado en la traducci\u00f3n.",
            },
            {
                "q": "\u00bfEn qu\u00e9 se diferencia esto de simplemente buscar mis resultados en Google?",
                "a": "Buscar valores individuales uno por uno en Google te da informaci\u00f3n dispersa y gen\u00e9rica. NoryaAI lee tu informe completo de una vez, compara cada valor con su rango de referencia y produce un \u00fanico resumen estructurado con puntuaci\u00f3n de salud, marcadores se\u00f1alados y categor\u00edas \u2014 todo en un solo lugar.",
            },
        ],
        "cta_title": "\u00bfListo para entender tu an\u00e1lisis de sangre?",
        "cta_sub": "Sube tu informe de laboratorio y obt\u00e9n un resumen claro y estructurado con explicaciones en lenguaje sencillo \u2014 en minutos.",
        "cta_primary": "Subir y analizar ahora",
        "cta_secondary": "Ver precios",
    }


def _fr() -> dict:
    return {
        "meta_title": "R\u00e9sultats d\u2019analyses sanguines expliqu\u00e9s \u2014 Ce que votre rapport signifie vraiment | NoryaAI",
        "meta_description": "Vous ne comprenez pas vos r\u00e9sultats d\u2019analyses sanguines ? Apprenez \u00e0 lire les abr\u00e9viations, les plages de r\u00e9f\u00e9rence et les unit\u00e9s \u2014 et comment un rapport IA structur\u00e9 peut clarifier les choses.",
        "hero_title": "R\u00e9sultats d\u2019analyses sanguines expliqu\u00e9s",
        "hero_sub": "Les rapports de laboratoire sont remplis d\u2019abr\u00e9viations, de chiffres et de plages que la plupart des gens n\u2019ont jamais appris \u00e0 lire. Ce guide explique pourquoi ils pr\u00eatent \u00e0 confusion, ce qu\u2019il faut rechercher et comment une approche structur\u00e9e peut vous aider \u00e0 comprendre vos r\u00e9sultats avant votre prochain rendez-vous m\u00e9dical.",
        "cta_hero_primary": "Analyser mon bilan sanguin",
        "cta_hero_secondary": "Voir un exemple de rapport",
        "confusing_title": "Pourquoi les rapports d\u2019analyses sanguines peuvent \u00eatre d\u00e9routants",
        "confusing_sub": "Vous n\u2019\u00eates pas la seule personne \u00e0 trouver les rapports de laboratoire difficiles \u00e0 lire. Voici les raisons les plus courantes.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "Abr\u00e9viations inconnues",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 les rapports de laboratoire regorgent de sigles rarement expliqu\u00e9s sur le document lui-m\u00eame.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Plages de r\u00e9f\u00e9rence variables",
                "desc": "Ce qui est consid\u00e9r\u00e9 comme \u00ab normal \u00bb peut varier selon les laboratoires, les groupes d\u2019\u00e2ge et m\u00eame les m\u00e9thodes de mesure. Une valeur signal\u00e9e dans un laboratoire peut \u00eatre normale dans un autre.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "Unit\u00e9s diff\u00e9rentes, m\u00eame test",
                "desc": "H\u00e9moglobine en g/dL ou g/L ? Glucose en mg/dL ou mmol/L ? Le m\u00eame biomarqueur peut appara\u00eetre dans des unit\u00e9s diff\u00e9rentes selon le pays ou le laboratoire.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "Format dense, aucune explication",
                "desc": "La plupart des rapports de laboratoire sont con\u00e7us pour les cliniciens, pas pour les patients. Vous voyez des rang\u00e9es de chiffres mais aucun contexte sur ce qu\u2019ils signifient pour vous.",
            },
        ],
        "clarify_title": "Ce que NoryaAI clarifie",
        "clarify_sub": "NoryaAI ne remplace pas votre m\u00e9decin. Il vous donne une version structur\u00e9e et lisible de vos r\u00e9sultats pour que vous arriviez \u00e0 votre rendez-vous mieux inform\u00e9.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "Explications en langage clair",
                "desc": "Chaque biomarqueur est accompagn\u00e9 d\u2019une explication claire et sans jargon sur ce qu\u2019il mesure et pourquoi c\u2019est important.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Plages de r\u00e9f\u00e9rence en contexte",
                "desc": "Vos valeurs sont affich\u00e9es \u00e0 c\u00f4t\u00e9 des plages de r\u00e9f\u00e9rence pour que vous puissiez voir o\u00f9 vous en \u00eates \u2014 \u00e9lev\u00e9, bas ou dans les limites normales.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "Marqueurs signal\u00e9s",
                "desc": "Les valeurs hors de la plage attendue sont mises en \u00e9vidence pour que vous puissiez vous concentrer sur ce qui peut n\u00e9cessiter une attention.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Cat\u00e9gories structur\u00e9es",
                "desc": "Les r\u00e9sultats sont regroup\u00e9s par cat\u00e9gorie \u2014 foie, reins, thyro\u00efde, cellules sanguines et plus \u2014 au lieu d\u2019une simple liste de chiffres.",
            },
            {
                "icon": "\U0001f310",
                "title": "Rapports multilingues",
                "desc": "Obtenez votre rapport dans 9+ langues avec le contexte m\u00e9dical pr\u00e9serv\u00e9. Utile quand votre rapport de laboratoire est dans une langue que vous ne ma\u00eetrisez pas compl\u00e8tement.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "R\u00e9sum\u00e9 pr\u00eat pour le m\u00e9decin",
                "desc": "Un PDF propre avec un score de sant\u00e9 et une v\u00e9rification QR que vous pouvez imprimer, sauvegarder ou partager lors de votre prochain rendez-vous.",
            },
        ],
        "common_title": "\u00c9l\u00e9ments couramment recherch\u00e9s dans les r\u00e9sultats",
        "common_sub": "Voici quelques-uns des biomarqueurs et panels les plus fr\u00e9quemment recherch\u00e9s. NoryaAI les couvre tous dans ses rapports structur\u00e9s.",
        "common_items": [
            {"title": "H\u00e9mogramme complet (NFS)", "desc": "WBC, RBC, h\u00e9moglobine, h\u00e9matocrite, plaquettes \u2014 le panel le plus courant lors des bilans de routine."},
            {"title": "Fonction h\u00e9patique (ALT, AST, ALP)", "desc": "Enzymes qui indiquent le bon fonctionnement de votre foie. Souvent v\u00e9rifi\u00e9es lors des bilans sanguins de routine."},
            {"title": "Fonction r\u00e9nale (ur\u00e9e, cr\u00e9atinine)", "desc": "Marqueurs montrant l\u2019efficacit\u00e9 de vos reins \u00e0 filtrer les d\u00e9chets de votre sang."},
            {"title": "Bilan thyro\u00efdien (TSH, T3, T4)", "desc": "Hormones qui r\u00e9gulent le m\u00e9tabolisme, les niveaux d\u2019\u00e9nergie et la temp\u00e9rature corporelle."},
            {"title": "Glyc\u00e9mie (glucose, HbA1c)", "desc": "Glucose \u00e0 jeun et moyenne glyc\u00e9mique \u00e0 long terme. Marqueurs cl\u00e9s pour la sant\u00e9 m\u00e9tabolique."},
            {"title": "Cholest\u00e9rol et lipides (LDL, HDL, triglyc\u00e9rides)", "desc": "R\u00e9sultats du bilan lipidique couramment discut\u00e9s dans les \u00e9valuations de sant\u00e9 cardiovasculaire."},
            {"title": "Fer et ferritine", "desc": "Marqueurs li\u00e9s au stockage et au transport du fer. Pertinents pour la fatigue, l\u2019an\u00e9mie et les niveaux d\u2019\u00e9nergie g\u00e9n\u00e9raux."},
            {"title": "Vitamine D et B12", "desc": "Niveaux vitaminiques courants que beaucoup de gens v\u00e9rifient, surtout lors des bilans sanguins annuels de routine."},
            {"title": "Marqueurs inflammatoires (CRP, VS)", "desc": "Indicateurs g\u00e9n\u00e9raux d\u2019inflammation dans le corps. Souvent utilis\u00e9s comme r\u00e9f\u00e9rence de d\u00e9pistage."},
        ],
        "how_title": "Comment \u00e7a marche",
        "how_sub": "Trois \u00e9tapes pour passer d\u2019un rapport de laboratoire confus \u00e0 un r\u00e9sum\u00e9 structur\u00e9 que vous pouvez r\u00e9ellement comprendre.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "T\u00e9l\u00e9chargez votre rapport",
                "desc": "PDF, photo ou texte coll\u00e9. Choisissez ce qui est le plus facile.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "L\u2019IA structure vos donn\u00e9es",
                "desc": "Les valeurs, unit\u00e9s et plages sont extraites et organis\u00e9es en cat\u00e9gories claires.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Recevez votre rapport expliqu\u00e9",
                "desc": "Score de sant\u00e9, marqueurs signal\u00e9s, explications en langage clair et un PDF t\u00e9l\u00e9chargeable.",
            },
        ],
        "preview_title": "\u00c0 quoi ressemble votre rapport expliqu\u00e9",
        "preview_sub": "Voici un aper\u00e7u de la fa\u00e7on dont NoryaAI structure et explique vos r\u00e9sultats d\u2019analyses sanguines.",
        "preview_lines": [
            {"label": "Score de sant\u00e9", "value": "78 / 100 \u2014 Bon dans l\u2019ensemble, quelques marqueurs \u00e0 v\u00e9rifier"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 Nombre normal de globules blancs (4.5\u201311.0)"},
            {"label": "H\u00e9moglobine", "value": "14.2 g/dL \u2014 Dans la plage de r\u00e9f\u00e9rence (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 Enzyme h\u00e9patique l\u00e9g\u00e8rement \u00e9lev\u00e9e (normal : 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Fonction thyro\u00efdienne normale (0.4\u20134.0)"},
            {"label": "Vitamine D", "value": "18 ng/mL \u2014 En dessous du niveau recommand\u00e9 (30\u2013100)"},
        ],
        "preview_disclaimer": "Donn\u00e9es d\u2019exemple \u00e0 titre illustratif uniquement. Votre rapport r\u00e9el refl\u00e9tera vos valeurs de laboratoire personnelles, unit\u00e9s et plages de r\u00e9f\u00e9rence.",
        "faqs": [
            {
                "q": "Que signifie r\u00e9ellement \u00ab r\u00e9sultats d\u2019analyses sanguines expliqu\u00e9s \u00bb ?",
                "a": "Cela signifie transformer les chiffres bruts, les abr\u00e9viations et les plages de r\u00e9f\u00e9rence de votre rapport de laboratoire en explications en langage clair que vous pouvez comprendre \u2014 avec le contexte sur ce que chaque valeur mesure et si elle se situe dans les limites normales.",
            },
            {
                "q": "NoryaAI peut-il expliquer tout type d\u2019analyse sanguine ?",
                "a": "NoryaAI prend en charge la plupart des panels sanguins standard, y compris l\u2019h\u00e9mogramme, les panels m\u00e9taboliques, les fonctions h\u00e9patique et r\u00e9nale, la thyro\u00efde, les lipides, les vitamines et les marqueurs inflammatoires. Si votre rapport contient des valeurs analysables, elles seront incluses dans votre r\u00e9sum\u00e9 structur\u00e9.",
            },
            {
                "q": "Est-ce un diagnostic m\u00e9dical ?",
                "a": "Non. NoryaAI fournit des explications structur\u00e9es et \u00e9ducatives de vos valeurs de laboratoire. Il ne diagnostique pas de maladies, ne recommande pas de traitements et ne remplace pas les conseils m\u00e9dicaux professionnels. Consultez toujours un professionnel de sant\u00e9 qualifi\u00e9.",
            },
            {
                "q": "Pourquoi les plages de r\u00e9f\u00e9rence diff\u00e8rent-elles entre les laboratoires ?",
                "a": "Les laboratoires utilisent des \u00e9quipements, des m\u00e9thodes et des \u00e9chantillons de population diff\u00e9rents pour \u00e9tablir leurs plages. L\u2019\u00e2ge, le sexe et m\u00eame l\u2019altitude peuvent influencer ce qu\u2019un laboratoire consid\u00e8re comme \u00ab normal \u00bb. C\u2019est pourquoi la m\u00eame valeur peut \u00eatre signal\u00e9e dans un laboratoire mais pas dans un autre.",
            },
            {
                "q": "Puis-je obtenir mes r\u00e9sultats expliqu\u00e9s dans une autre langue ?",
                "a": "Oui. NoryaAI g\u00e9n\u00e8re des rapports dans 9+ langues, dont l\u2019anglais, l\u2019allemand, le turc, le fran\u00e7ais, l\u2019italien, l\u2019espagnol, l\u2019h\u00e9breu, l\u2019hindi et l\u2019arabe \u2014 avec le contexte m\u00e9dical pr\u00e9serv\u00e9 dans la traduction.",
            },
            {
                "q": "En quoi est-ce diff\u00e9rent de simplement chercher mes r\u00e9sultats sur Google ?",
                "a": "Chercher des valeurs individuelles une par une sur Google donne des informations dispers\u00e9es et g\u00e9n\u00e9riques. NoryaAI lit l\u2019ensemble de votre rapport en une fois, compare chaque valeur \u00e0 sa plage de r\u00e9f\u00e9rence et produit un r\u00e9sum\u00e9 structur\u00e9 unique avec un score de sant\u00e9, des marqueurs signal\u00e9s et des cat\u00e9gories \u2014 le tout en un seul endroit.",
            },
        ],
        "cta_title": "Pr\u00eat \u00e0 comprendre votre bilan sanguin ?",
        "cta_sub": "T\u00e9l\u00e9chargez votre rapport de laboratoire et obtenez un r\u00e9sum\u00e9 clair et structur\u00e9 avec des explications en langage simple \u2014 en quelques minutes.",
        "cta_primary": "T\u00e9l\u00e9charger et analyser",
        "cta_secondary": "Voir les tarifs",
    }


def _it() -> dict:
    return {
        "meta_title": "Risultati degli esami del sangue spiegati \u2014 Cosa significa davvero il tuo referto | NoryaAI",
        "meta_description": "Non capisci i risultati dei tuoi esami del sangue? Scopri come leggere abbreviazioni, intervalli di riferimento e unit\u00e0 \u2014 e come un report IA strutturato pu\u00f2 renderli pi\u00f9 chiari.",
        "hero_title": "Risultati degli esami del sangue spiegati",
        "hero_sub": "I referti di laboratorio sono pieni di abbreviazioni, numeri e intervalli che la maggior parte delle persone non ha mai imparato a leggere. Questa guida spiega perch\u00e9 sono confusi, cosa cercare e come un approccio strutturato pu\u00f2 aiutarti a capire i tuoi risultati prima della prossima visita medica.",
        "cta_hero_primary": "Analizza il mio esame del sangue",
        "cta_hero_secondary": "Vedi un report di esempio",
        "confusing_title": "Perch\u00e9 i referti degli esami del sangue possono sembrare confusi",
        "confusing_sub": "Non sei l\u2019unica persona che trova difficili da leggere i referti di laboratorio. Ecco i motivi pi\u00f9 comuni.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "Abbreviazioni sconosciute",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 i referti di laboratorio sono pieni di sigle che raramente vengono spiegate nel documento stesso.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Intervalli di riferimento variabili",
                "desc": "Ci\u00f2 che \u00e8 considerato \u201cnormale\u201d pu\u00f2 variare tra laboratori, fasce d\u2019et\u00e0 e persino metodi di misurazione. Un valore segnalato in un laboratorio pu\u00f2 essere normale in un altro.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "Unit\u00e0 diverse, stesso test",
                "desc": "Emoglobina in g/dL o g/L? Glucosio in mg/dL o mmol/L? Lo stesso biomarcatore pu\u00f2 apparire in unit\u00e0 diverse a seconda del paese o del laboratorio.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "Formato denso, nessuna spiegazione",
                "desc": "La maggior parte dei referti di laboratorio \u00e8 progettata per i medici, non per i pazienti. Vedi righe di numeri ma nessun contesto su cosa significano per te.",
            },
        ],
        "clarify_title": "Cosa chiarisce NoryaAI",
        "clarify_sub": "NoryaAI non sostituisce il tuo medico. Ti fornisce una versione strutturata e leggibile dei tuoi risultati in modo che tu possa presentarti al tuo appuntamento meglio informato.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "Spiegazioni in linguaggio semplice",
                "desc": "Ogni biomarcatore \u00e8 accompagnato da una spiegazione chiara e priva di gergo su cosa misura e perch\u00e9 \u00e8 importante.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "Intervalli di riferimento contestualizzati",
                "desc": "I tuoi valori vengono mostrati accanto agli intervalli di riferimento in modo che tu possa vedere dove ti trovi \u2014 alto, basso o entro i limiti normali.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "Marcatori segnalati",
                "desc": "I valori al di fuori dell\u2019intervallo atteso vengono evidenziati per consentirti di concentrarti su ci\u00f2 che potrebbe richiedere attenzione.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Categorie strutturate",
                "desc": "I risultati sono raggruppati per categoria \u2014 fegato, reni, tiroide, cellule del sangue e altro \u2014 invece di un semplice elenco di numeri.",
            },
            {
                "icon": "\U0001f310",
                "title": "Report multilingue",
                "desc": "Ricevi il tuo report in 9+ lingue con il contesto medico preservato. Utile quando il tuo referto di laboratorio \u00e8 in una lingua che non comprendi completamente.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Riepilogo pronto per il medico",
                "desc": "Un PDF pulito con punteggio di salute e verifica QR che puoi stampare, salvare o condividere al tuo prossimo appuntamento.",
            },
        ],
        "common_title": "Cosa cercano comunemente le persone nei loro risultati",
        "common_sub": "Questi sono alcuni dei biomarcatori e pannelli pi\u00f9 cercati. NoryaAI li copre tutti nei suoi report strutturati.",
        "common_items": [
            {"title": "Emocromo completo (CBC)", "desc": "WBC, RBC, emoglobina, ematocrito, piastrine \u2014 il pannello pi\u00f9 comune nei controlli di routine."},
            {"title": "Funzionalit\u00e0 epatica (ALT, AST, ALP)", "desc": "Enzimi che indicano quanto bene funziona il tuo fegato. Spesso controllati negli esami del sangue di routine."},
            {"title": "Funzionalit\u00e0 renale (BUN, creatinina)", "desc": "Marcatori che mostrano quanto efficacemente i tuoi reni filtrano le scorie dal sangue."},
            {"title": "Pannello tiroideo (TSH, T3, T4)", "desc": "Ormoni che regolano il metabolismo, i livelli di energia e la temperatura corporea."},
            {"title": "Glicemia (glucosio, HbA1c)", "desc": "Glucosio a digiuno e media glicemica a lungo termine. Marcatori chiave per la salute metabolica."},
            {"title": "Colesterolo e lipidi (LDL, HDL, trigliceridi)", "desc": "Risultati del pannello lipidico comunemente discussi nelle valutazioni di salute cardiovascolare."},
            {"title": "Ferro e ferritina", "desc": "Marcatori legati allo stoccaggio e al trasporto del ferro. Rilevanti per stanchezza, anemia e livelli di energia generali."},
            {"title": "Vitamina D e B12", "desc": "Livelli vitaminici comuni che molte persone controllano, specialmente negli esami del sangue annuali di routine."},
            {"title": "Marcatori infiammatori (PCR, VES)", "desc": "Indicatori generali di infiammazione nel corpo. Spesso usati come riferimento di base per lo screening."},
        ],
        "how_title": "Come funziona",
        "how_sub": "Tre passaggi da un referto di laboratorio confuso a un riepilogo strutturato che puoi davvero capire.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Carica il tuo referto",
                "desc": "PDF, foto o testo incollato. Scegli quello che \u00e8 pi\u00f9 facile.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "L\u2019IA struttura i tuoi dati",
                "desc": "Valori, unit\u00e0 e intervalli vengono estratti e organizzati in categorie chiare.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Ricevi il tuo report spiegato",
                "desc": "Punteggio di salute, marcatori segnalati, spiegazioni in linguaggio semplice e un PDF scaricabile.",
            },
        ],
        "preview_title": "Come appare il tuo report spiegato",
        "preview_sub": "Ecco un\u2019anteprima di come NoryaAI struttura e spiega i risultati dei tuoi esami del sangue.",
        "preview_lines": [
            {"label": "Punteggio di salute", "value": "78 / 100 \u2014 Buono nel complesso, alcuni marcatori da verificare"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 Conta normale dei globuli bianchi (4.5\u201311.0)"},
            {"label": "Emoglobina", "value": "14.2 g/dL \u2014 Nell\u2019intervallo di riferimento (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 Enzima epatico leggermente elevato (normale: 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 Funzione tiroidea normale (0.4\u20134.0)"},
            {"label": "Vitamina D", "value": "18 ng/mL \u2014 Al di sotto del livello raccomandato (30\u2013100)"},
        ],
        "preview_disclaimer": "Dati di esempio solo a scopo illustrativo. Il tuo report reale riflettar\u00e0 i tuoi valori di laboratorio personali, unit\u00e0 e intervalli di riferimento.",
        "faqs": [
            {
                "q": "Cosa significa realmente \u201crisultati degli esami del sangue spiegati\u201d?",
                "a": "Significa trasformare i numeri grezzi, le abbreviazioni e gli intervalli di riferimento del tuo referto di laboratorio in spiegazioni in linguaggio semplice che puoi capire \u2014 con contesto su cosa misura ogni valore e se rientra nei limiti normali.",
            },
            {
                "q": "NoryaAI pu\u00f2 spiegare qualsiasi tipo di esame del sangue?",
                "a": "NoryaAI supporta la maggior parte dei pannelli ematici standard inclusi emocromo, pannelli metabolici, funzionalit\u00e0 epatica e renale, tiroide, lipidi, vitamine e marcatori infiammatori. Se il tuo referto contiene valori analizzabili, verranno inclusi nel tuo riepilogo strutturato.",
            },
            {
                "q": "\u00c8 una diagnosi medica?",
                "a": "No. NoryaAI fornisce spiegazioni strutturate ed educative dei tuoi valori di laboratorio. Non diagnostica condizioni, non raccomanda trattamenti e non sostituisce il parere medico professionale. Consulta sempre un professionista sanitario qualificato.",
            },
            {
                "q": "Perch\u00e9 gli intervalli di riferimento differiscono tra i laboratori?",
                "a": "I laboratori utilizzano attrezzature, metodi e campioni di popolazione diversi per stabilire i loro intervalli. Et\u00e0, sesso e persino l\u2019altitudine possono influenzare ci\u00f2 che un laboratorio considera \u201cnormale\u201d. Ecco perch\u00e9 lo stesso valore pu\u00f2 essere segnalato in un laboratorio ma non in un altro.",
            },
            {
                "q": "Posso ottenere i miei risultati spiegati in un\u2019altra lingua?",
                "a": "S\u00ec. NoryaAI genera report in 9+ lingue tra cui inglese, tedesco, turco, francese, italiano, spagnolo, ebraico, hindi e arabo \u2014 con il contesto medico preservato nella traduzione.",
            },
            {
                "q": "In cosa \u00e8 diverso dal cercare semplicemente i miei risultati su Google?",
                "a": "Cercare singoli valori uno per uno su Google ti d\u00e0 informazioni sparse e generiche. NoryaAI legge l\u2019intero referto in una volta, confronta ogni valore con il suo intervallo di riferimento e produce un unico riepilogo strutturato con punteggio di salute, marcatori segnalati e categorie \u2014 tutto in un unico posto.",
            },
        ],
        "cta_title": "Pronto a capire i tuoi esami del sangue?",
        "cta_sub": "Carica il tuo referto di laboratorio e ottieni un riepilogo chiaro e strutturato con spiegazioni in linguaggio semplice \u2014 in pochi minuti.",
        "cta_primary": "Carica e analizza ora",
        "cta_secondary": "Vedi i prezzi",
    }


def _he() -> dict:
    return {
        "meta_title": "\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d3\u05dd \u05de\u05d5\u05e1\u05d1\u05e8\u05d5\u05ea \u2014 \u05de\u05d4 \u05d4\u05d3\u05d5\u05d7 \u05e9\u05dc\u05da \u05d1\u05d0\u05de\u05ea \u05d0\u05d5\u05de\u05e8 | NoryaAI",
        "meta_description": "\u05dc\u05d0 \u05d1\u05d8\u05d5\u05d7 \u05de\u05d4 \u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d4\u05d3\u05dd \u05e9\u05dc\u05da \u05d0\u05d5\u05de\u05e8\u05d5\u05ea? \u05dc\u05de\u05d3 \u05dc\u05e7\u05e8\u05d5\u05d0 \u05e7\u05d9\u05e6\u05d5\u05e8\u05d9\u05dd, \u05d8\u05d5\u05d5\u05d7\u05d9 \u05d9\u05d9\u05d7\u05d5\u05e1 \u05d5\u05d9\u05d7\u05d9\u05d3\u05d5\u05ea \u2014 \u05d5\u05d0\u05d9\u05da \u05d3\u05d5\u05d7 AI \u05de\u05d1\u05e0\u05d4 \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05d1\u05d4\u05d9\u05e8 \u05d0\u05ea \u05d4\u05d3\u05d1\u05e8\u05d9\u05dd.",
        "hero_title": "\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d3\u05dd \u05de\u05d5\u05e1\u05d1\u05e8\u05d5\u05ea",
        "hero_sub": "\u05d3\u05d5\u05d7\u05d5\u05ea \u05de\u05e2\u05d1\u05d3\u05d4 \u05de\u05dc\u05d0\u05d9\u05dd \u05d1\u05e7\u05d9\u05e6\u05d5\u05e8\u05d9\u05dd, \u05de\u05e1\u05e4\u05e8\u05d9\u05dd \u05d5\u05d8\u05d5\u05d5\u05d7\u05d9\u05dd \u05e9\u05e8\u05d5\u05d1 \u05d4\u05d0\u05e0\u05e9\u05d9\u05dd \u05de\u05e2\u05d5\u05dc\u05dd \u05dc\u05d0 \u05dc\u05de\u05d3\u05d5 \u05dc\u05e7\u05e8\u05d5\u05d0. \u05de\u05d3\u05e8\u05d9\u05da \u05d6\u05d4 \u05de\u05e1\u05d1\u05d9\u05e8 \u05de\u05d4 \u05d4\u05d5\u05e4\u05da \u05d0\u05d5\u05ea\u05dd \u05dc\u05de\u05d1\u05dc\u05d1\u05dc\u05d9\u05dd, \u05e2\u05dc \u05de\u05d4 \u05dc\u05e9\u05d9\u05dd \u05dc\u05d1, \u05d5\u05d0\u05d9\u05da \u05d2\u05d9\u05e9\u05d4 \u05de\u05d1\u05e0\u05d9\u05ea \u05d9\u05db\u05d5\u05dc\u05d4 \u05dc\u05e2\u05d6\u05d5\u05e8 \u05dc\u05da \u05dc\u05d4\u05d1\u05d9\u05df \u05d0\u05ea \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05dc\u05e4\u05e0\u05d9 \u05d4\u05d1\u05d9\u05e7\u05d5\u05e8 \u05d4\u05d1\u05d0 \u05d0\u05e6\u05dc \u05d4\u05e8\u05d5\u05e4\u05d0.",
        "cta_hero_primary": "\u05e0\u05ea\u05d7 \u05d0\u05ea \u05d1\u05d3\u05d9\u05e7\u05ea \u05d4\u05d3\u05dd \u05e9\u05dc\u05d9",
        "cta_hero_secondary": "\u05e6\u05e4\u05d4 \u05d1\u05d3\u05d5\u05d7 \u05dc\u05d3\u05d5\u05d2\u05de\u05d4",
        "confusing_title": "\u05dc\u05de\u05d4 \u05d3\u05d5\u05d7\u05d5\u05ea \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d3\u05dd \u05d9\u05db\u05d5\u05dc\u05d9\u05dd \u05dc\u05d4\u05e8\u05d2\u05d9\u05e9 \u05de\u05d1\u05dc\u05d1\u05dc\u05d9\u05dd",
        "confusing_sub": "\u05d0\u05ea\u05d4 \u05dc\u05d0 \u05dc\u05d1\u05d3 \u05e9\u05de\u05d5\u05e6\u05d0 \u05e9\u05e7\u05e9\u05d4 \u05dc\u05e7\u05e8\u05d5\u05d0 \u05d3\u05d5\u05d7\u05d5\u05ea \u05de\u05e2\u05d1\u05d3\u05d4. \u05d4\u05e0\u05d4 \u05d4\u05e1\u05d9\u05d1\u05d5\u05ea \u05d4\u05e0\u05e4\u05d5\u05e6\u05d5\u05ea \u05d1\u05d9\u05d5\u05ea\u05e8.",
        "confusing_items": [
            {
                "icon": "\U0001f524",
                "title": "\u05e7\u05d9\u05e6\u05d5\u05e8\u05d9\u05dd \u05dc\u05d0 \u05de\u05d5\u05db\u05e8\u05d9\u05dd",
                "desc": "WBC, RBC, ALT, TSH, HbA1c \u2014 \u05d3\u05d5\u05d7\u05d5\u05ea \u05de\u05e2\u05d1\u05d3\u05d4 \u05de\u05dc\u05d0\u05d9\u05dd \u05d1\u05e8\u05d0\u05e9\u05d9 \u05ea\u05d9\u05d1\u05d5\u05ea \u05e9\u05dc\u05e2\u05d9\u05ea\u05d9\u05dd \u05e8\u05d7\u05d5\u05e7\u05d5\u05ea \u05de\u05d5\u05e1\u05d1\u05e8\u05d9\u05dd \u05d1\u05de\u05e1\u05de\u05da \u05e2\u05e6\u05de\u05d5.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "\u05d8\u05d5\u05d5\u05d7\u05d9 \u05d9\u05d9\u05d7\u05d5\u05e1 \u05de\u05e9\u05ea\u05e0\u05d9\u05dd",
                "desc": "\u05de\u05d4 \u05e9\u05e0\u05d7\u05e9\u05d1 \u201c\u05ea\u05e7\u05d9\u05df\u201d \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05e9\u05ea\u05e0\u05d5\u05ea \u05d1\u05d9\u05df \u05de\u05e2\u05d1\u05d3\u05d5\u05ea, \u05e7\u05d1\u05d5\u05e6\u05d5\u05ea \u05d2\u05d9\u05dc \u05d5\u05d0\u05e4\u05d9\u05dc\u05d5 \u05e9\u05d9\u05d8\u05d5\u05ea \u05de\u05d3\u05d9\u05d3\u05d4. \u05e2\u05e8\u05da \u05e9\u05de\u05e1\u05d5\u05de\u05df \u05d1\u05de\u05e2\u05d1\u05d3\u05d4 \u05d0\u05d7\u05ea \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d4\u05d9\u05d5\u05ea \u05ea\u05e7\u05d9\u05df \u05d1\u05d0\u05d7\u05e8\u05ea.",
            },
            {
                "icon": "\u2696\ufe0f",
                "title": "\u05d9\u05d7\u05d9\u05d3\u05d5\u05ea \u05e9\u05d5\u05e0\u05d5\u05ea, \u05d0\u05d5\u05ea\u05d4 \u05d1\u05d3\u05d9\u05e7\u05d4",
                "desc": "\u05d4\u05de\u05d5\u05d2\u05dc\u05d5\u05d1\u05d9\u05df \u05d1-g/dL \u05d0\u05d5 g/L? \u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05d1-mg/dL \u05d0\u05d5 mmol/L? \u05d0\u05d5\u05ea\u05d5 \u05e1\u05de\u05df \u05d1\u05d9\u05d5\u05dc\u05d5\u05d2\u05d9 \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05d5\u05e4\u05d9\u05e2 \u05d1\u05d9\u05d7\u05d9\u05d3\u05d5\u05ea \u05e9\u05d5\u05e0\u05d5\u05ea \u05d1\u05d4\u05ea\u05d0\u05dd \u05dc\u05de\u05d3\u05d9\u05e0\u05d4 \u05d0\u05d5 \u05dc\u05de\u05e2\u05d1\u05d3\u05d4.",
            },
            {
                "icon": "\U0001f4c4",
                "title": "\u05e4\u05d5\u05e8\u05de\u05d8 \u05e6\u05e4\u05d5\u05e3, \u05d1\u05dc\u05d9 \u05d4\u05e1\u05d1\u05e8",
                "desc": "\u05e8\u05d5\u05d1 \u05d3\u05d5\u05d7\u05d5\u05ea \u05d4\u05de\u05e2\u05d1\u05d3\u05d4 \u05de\u05ea\u05d5\u05db\u05e0\u05e0\u05d9\u05dd \u05dc\u05e8\u05d5\u05e4\u05d0\u05d9\u05dd, \u05dc\u05d0 \u05dc\u05de\u05d8\u05d5\u05e4\u05dc\u05d9\u05dd. \u05d0\u05ea\u05d4 \u05e8\u05d5\u05d0\u05d4 \u05e9\u05d5\u05e8\u05d5\u05ea \u05e9\u05dc \u05de\u05e1\u05e4\u05e8\u05d9\u05dd \u05d0\u05d1\u05dc \u05d1\u05dc\u05d9 \u05d4\u05e7\u05e9\u05e8 \u05dc\u05de\u05d4 \u05d4\u05dd \u05d0\u05d5\u05de\u05e8\u05d9\u05dd \u05e2\u05d1\u05d5\u05e8\u05da.",
            },
        ],
        "clarify_title": "\u05de\u05d4 NoryaAI \u05de\u05d1\u05d4\u05d9\u05e8",
        "clarify_sub": "NoryaAI \u05dc\u05d0 \u05de\u05d7\u05dc\u05d9\u05e3 \u05d0\u05ea \u05d4\u05e8\u05d5\u05e4\u05d0 \u05e9\u05dc\u05da. \u05d4\u05d5\u05d0 \u05e0\u05d5\u05ea\u05df \u05dc\u05da \u05d2\u05e8\u05e1\u05d4 \u05de\u05d1\u05e0\u05d9\u05ea \u05d5\u05e7\u05e8\u05d9\u05d0\u05d4 \u05e9\u05dc \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05e9\u05dc\u05da \u05db\u05d3\u05d9 \u05e9\u05ea\u05d2\u05d9\u05e2 \u05dc\u05ea\u05d5\u05e8 \u05e9\u05dc\u05da \u05de\u05d9\u05d5\u05d3\u05e2 \u05d9\u05d5\u05ea\u05e8.",
        "clarify_items": [
            {
                "icon": "\U0001f4d6",
                "title": "\u05d4\u05e1\u05d1\u05e8\u05d9\u05dd \u05d1\u05e9\u05e4\u05d4 \u05e4\u05e9\u05d5\u05d8\u05d4",
                "desc": "\u05db\u05dc \u05e1\u05de\u05df \u05d1\u05d9\u05d5\u05dc\u05d5\u05d2\u05d9 \u05de\u05dc\u05d5\u05d5\u05d4 \u05d1\u05d4\u05e1\u05d1\u05e8 \u05d1\u05e8\u05d5\u05e8, \u05dc\u05dc\u05d0 \u05d6\u05e8\u05d2\u05d5\u05df \u05de\u05e7\u05e6\u05d5\u05e2\u05d9, \u05e2\u05dc \u05de\u05d4 \u05d4\u05d5\u05d0 \u05de\u05d5\u05d3\u05d3 \u05d5\u05dc\u05de\u05d4 \u05d6\u05d4 \u05d7\u05e9\u05d5\u05d1.",
            },
            {
                "icon": "\U0001f4ca",
                "title": "\u05d8\u05d5\u05d5\u05d7\u05d9 \u05d9\u05d9\u05d7\u05d5\u05e1 \u05d1\u05d4\u05e7\u05e9\u05e8",
                "desc": "\u05d4\u05e2\u05e8\u05db\u05d9\u05dd \u05e9\u05dc\u05da \u05de\u05d5\u05e6\u05d2\u05d9\u05dd \u05dc\u05e6\u05d3 \u05d8\u05d5\u05d5\u05d7\u05d9 \u05d4\u05d9\u05d9\u05d7\u05d5\u05e1 \u05db\u05d3\u05d9 \u05e9\u05ea\u05d5\u05db\u05dc \u05dc\u05e8\u05d0\u05d5\u05ea \u05d0\u05d9\u05e4\u05d4 \u05d0\u05ea\u05d4 \u05e0\u05de\u05e6\u05d0 \u2014 \u05d2\u05d1\u05d5\u05d4, \u05e0\u05de\u05d5\u05da \u05d0\u05d5 \u05d1\u05d2\u05d1\u05d5\u05dc\u05d5\u05ea \u05d4\u05ea\u05e7\u05df.",
            },
            {
                "icon": "\U0001f3f7\ufe0f",
                "title": "\u05e1\u05de\u05e0\u05d9\u05dd \u05de\u05e1\u05d5\u05de\u05e0\u05d9\u05dd",
                "desc": "\u05e2\u05e8\u05db\u05d9\u05dd \u05de\u05d7\u05d5\u05e5 \u05dc\u05d8\u05d5\u05d5\u05d7 \u05d4\u05e6\u05e4\u05d5\u05d9 \u05de\u05d5\u05d3\u05d2\u05e9\u05d9\u05dd \u05db\u05d3\u05d9 \u05e9\u05ea\u05d5\u05db\u05dc \u05dc\u05d4\u05ea\u05de\u05e7\u05d3 \u05d1\u05de\u05d4 \u05e9\u05e2\u05e9\u05d5\u05d9 \u05dc\u05d3\u05e8\u05d5\u05e9 \u05ea\u05e9\u05d5\u05de\u05ea \u05dc\u05d1.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "\u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d5\u05ea \u05de\u05d1\u05e0\u05d9\u05d5\u05ea",
                "desc": "\u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05de\u05e7\u05d5\u05d1\u05e6\u05d5\u05ea \u05dc\u05e4\u05d9 \u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4 \u2014 \u05db\u05d1\u05d3, \u05db\u05dc\u05d9\u05d5\u05ea, \u05ea\u05e8\u05d9\u05e1, \u05ea\u05d0\u05d9 \u05d3\u05dd \u05d5\u05e2\u05d5\u05d3 \u2014 \u05d1\u05de\u05e7\u05d5\u05dd \u05e8\u05e9\u05d9\u05de\u05d4 \u05e9\u05d8\u05d5\u05d7\u05d4 \u05e9\u05dc \u05de\u05e1\u05e4\u05e8\u05d9\u05dd.",
            },
            {
                "icon": "\U0001f310",
                "title": "\u05d3\u05d5\u05d7\u05d5\u05ea \u05e8\u05d1-\u05dc\u05e9\u05d5\u05e0\u05d9\u05d9\u05dd",
                "desc": "\u05e7\u05d1\u05dc \u05d0\u05ea \u05d4\u05d3\u05d5\u05d7 \u05e9\u05dc\u05da \u05d1-9+ \u05e9\u05e4\u05d5\u05ea \u05e2\u05dd \u05e9\u05d9\u05de\u05d5\u05e8 \u05d4\u05d4\u05e7\u05e9\u05e8 \u05d4\u05e8\u05e4\u05d5\u05d0\u05d9. \u05e9\u05d9\u05de\u05d5\u05e9\u05d9 \u05db\u05e9\u05d3\u05d5\u05d7 \u05d4\u05de\u05e2\u05d1\u05d3\u05d4 \u05e9\u05dc\u05da \u05d1\u05e9\u05e4\u05d4 \u05e9\u05d0\u05ea\u05d4 \u05dc\u05d0 \u05de\u05d1\u05d9\u05df \u05d1\u05de\u05dc\u05d5\u05d0\u05d4.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "\u05e1\u05d9\u05db\u05d5\u05dd \u05de\u05d5\u05db\u05df \u05dc\u05e8\u05d5\u05e4\u05d0",
                "desc": "PDF \u05e0\u05e7\u05d9 \u05e2\u05dd \u05e6\u05d9\u05d5\u05df \u05d1\u05e8\u05d9\u05d0\u05d5\u05ea \u05d5\u05d0\u05d9\u05de\u05d5\u05ea QR \u05e9\u05d0\u05e4\u05e9\u05e8 \u05dc\u05d4\u05d3\u05e4\u05d9\u05e1, \u05dc\u05e9\u05de\u05d5\u05e8 \u05d0\u05d5 \u05dc\u05e9\u05ea\u05e3 \u05d1\u05ea\u05d5\u05e8 \u05d4\u05d1\u05d0.",
            },
        ],
        "common_title": "\u05de\u05d4 \u05d0\u05e0\u05e9\u05d9\u05dd \u05d7\u05d5\u05e4\u05e9\u05d9\u05dd \u05d1\u05d3\u05e8\u05da \u05db\u05dc\u05dc \u05d1\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea",
        "common_sub": "\u05d0\u05dc\u05d4 \u05d7\u05dc\u05e7 \u05de\u05d4\u05e1\u05de\u05e0\u05d9\u05dd \u05d4\u05d1\u05d9\u05d5\u05dc\u05d5\u05d2\u05d9\u05d9\u05dd \u05d5\u05d4\u05e4\u05d0\u05e0\u05dc\u05d9\u05dd \u05d4\u05e0\u05e4\u05d5\u05e6\u05d9\u05dd \u05d1\u05d9\u05d5\u05ea\u05e8. NoryaAI \u05de\u05db\u05e1\u05d4 \u05d0\u05ea \u05db\u05d5\u05dc\u05dd \u05d1\u05d3\u05d5\u05d7\u05d5\u05ea \u05d4\u05de\u05d1\u05e0\u05d9\u05d9\u05dd \u05e9\u05dc\u05d5.",
        "common_items": [
            {"title": "\u05e1\u05e4\u05d9\u05e8\u05ea \u05d3\u05dd \u05de\u05dc\u05d0\u05d4 (CBC)", "desc": "WBC, RBC, \u05d4\u05de\u05d5\u05d2\u05dc\u05d5\u05d1\u05d9\u05df, \u05d4\u05de\u05d8\u05d5\u05e7\u05e8\u05d9\u05d8, \u05d8\u05e1\u05d9\u05d5\u05ea \u2014 \u05d4\u05e4\u05d0\u05e0\u05dc \u05d4\u05e0\u05e4\u05d5\u05e5 \u05d1\u05d9\u05d5\u05ea\u05e8 \u05d1\u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05e9\u05d2\u05e8\u05ea\u05d9\u05d5\u05ea."},
            {"title": "\u05ea\u05e4\u05e7\u05d5\u05d3 \u05db\u05d1\u05d3 (ALT, AST, ALP)", "desc": "\u05d0\u05e0\u05d6\u05d9\u05de\u05d9\u05dd \u05e9\u05de\u05e6\u05d9\u05d9\u05e0\u05d9\u05dd \u05e2\u05d3 \u05db\u05de\u05d4 \u05d4\u05db\u05d1\u05d3 \u05e9\u05dc\u05da \u05e4\u05d5\u05e2\u05dc \u05d4\u05d9\u05d8\u05d1. \u05e0\u05d1\u05d3\u05e7\u05d9\u05dd \u05dc\u05e2\u05d9\u05ea\u05d9\u05dd \u05e7\u05e8\u05d5\u05d1\u05d5\u05ea \u05d1\u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d3\u05dd \u05e9\u05d2\u05e8\u05ea\u05d9\u05d5\u05ea."},
            {"title": "\u05ea\u05e4\u05e7\u05d5\u05d3 \u05db\u05dc\u05d9\u05d5\u05ea (BUN, \u05e7\u05e8\u05d0\u05d8\u05d9\u05e0\u05d9\u05df)", "desc": "\u05e1\u05de\u05e0\u05d9\u05dd \u05e9\u05de\u05e8\u05d0\u05d9\u05dd \u05e2\u05d3 \u05db\u05de\u05d4 \u05d4\u05db\u05dc\u05d9\u05d5\u05ea \u05e9\u05dc\u05da \u05de\u05e1\u05e0\u05e0\u05d5\u05ea \u05e4\u05e1\u05d5\u05dc\u05ea \u05de\u05d4\u05d3\u05dd \u05d1\u05d9\u05e2\u05d9\u05dc\u05d5\u05ea."},
            {"title": "\u05e4\u05d0\u05e0\u05dc \u05ea\u05e8\u05d9\u05e1 (TSH, T3, T4)", "desc": "\u05d4\u05d5\u05e8\u05de\u05d5\u05e0\u05d9\u05dd \u05d4\u05de\u05d5\u05d5\u05e1\u05ea\u05d9\u05dd \u05de\u05d8\u05d1\u05d5\u05dc\u05d9\u05d6\u05dd, \u05e8\u05de\u05d5\u05ea \u05d0\u05e0\u05e8\u05d2\u05d9\u05d4 \u05d5\u05d8\u05de\u05e4\u05e8\u05d8\u05d5\u05e8\u05ea \u05d2\u05d5\u05e3."},
            {"title": "\u05e1\u05d5\u05db\u05e8 \u05d1\u05d3\u05dd (\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6, HbA1c)", "desc": "\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05d1\u05e6\u05d5\u05dd \u05d5\u05de\u05de\u05d5\u05e6\u05e2 \u05e1\u05d5\u05db\u05e8 \u05d3\u05dd \u05dc\u05d8\u05d5\u05d5\u05d7 \u05d0\u05e8\u05d5\u05da. \u05e1\u05de\u05e0\u05d9\u05dd \u05de\u05e4\u05ea\u05d7 \u05dc\u05d1\u05e8\u05d9\u05d0\u05d5\u05ea \u05de\u05d8\u05d1\u05d5\u05dc\u05d9\u05ea."},
            {"title": "\u05db\u05d5\u05dc\u05e1\u05d8\u05e8\u05d5\u05dc \u05d5\u05e9\u05d5\u05de\u05e0\u05d9\u05dd (LDL, HDL, \u05d8\u05e8\u05d9\u05d2\u05dc\u05d9\u05e6\u05e8\u05d9\u05d3\u05d9\u05dd)", "desc": "\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05e4\u05d0\u05e0\u05dc \u05e9\u05d5\u05de\u05e0\u05d9\u05dd \u05e9\u05e0\u05d3\u05d5\u05e0\u05d5\u05ea \u05dc\u05e2\u05d9\u05ea\u05d9\u05dd \u05e7\u05e8\u05d5\u05d1\u05d5\u05ea \u05d1\u05d4\u05e2\u05e8\u05db\u05d5\u05ea \u05d1\u05e8\u05d9\u05d0\u05d5\u05ea \u05e7\u05e8\u05d3\u05d9\u05d5\u05d5\u05e1\u05e7\u05d5\u05dc\u05e8\u05d9\u05ea."},
            {"title": "\u05d1\u05e8\u05d6\u05dc \u05d5\u05e4\u05e8\u05d9\u05d8\u05d9\u05df", "desc": "\u05e1\u05de\u05e0\u05d9\u05dd \u05d4\u05e7\u05e9\u05d5\u05e8\u05d9\u05dd \u05dc\u05d0\u05d7\u05e1\u05d5\u05df \u05d5\u05d4\u05e2\u05d1\u05e8\u05ea \u05d1\u05e8\u05d6\u05dc. \u05e8\u05dc\u05d5\u05d5\u05e0\u05d8\u05d9\u05d9\u05dd \u05dc\u05e2\u05d9\u05d9\u05e4\u05d5\u05ea, \u05d0\u05e0\u05de\u05d9\u05d4 \u05d5\u05e8\u05de\u05d5\u05ea \u05d0\u05e0\u05e8\u05d2\u05d9\u05d4 \u05db\u05dc\u05dc\u05d9\u05d5\u05ea."},
            {"title": "\u05d5\u05d9\u05d8\u05de\u05d9\u05df D \u05d5-B12", "desc": "\u05e8\u05de\u05d5\u05ea \u05d5\u05d9\u05d8\u05de\u05d9\u05e0\u05d9\u05dd \u05e0\u05e4\u05d5\u05e6\u05d5\u05ea \u05e9\u05d0\u05e0\u05e9\u05d9\u05dd \u05e8\u05d1\u05d9\u05dd \u05d1\u05d5\u05d3\u05e7\u05d9\u05dd, \u05d1\u05de\u05d9\u05d5\u05d7\u05d3 \u05d1\u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d3\u05dd \u05e9\u05e0\u05ea\u05d9\u05d5\u05ea \u05e9\u05d2\u05e8\u05ea\u05d9\u05d5\u05ea."},
            {"title": "\u05e1\u05de\u05e0\u05d9 \u05d3\u05dc\u05e7\u05ea (CRP, ESR)", "desc": "\u05de\u05d3\u05d3\u05d9\u05dd \u05db\u05dc\u05dc\u05d9\u05d9\u05dd \u05dc\u05d3\u05dc\u05e7\u05ea \u05d1\u05d2\u05d5\u05e3. \u05de\u05e9\u05de\u05e9\u05d9\u05dd \u05dc\u05e2\u05d9\u05ea\u05d9\u05dd \u05e7\u05e8\u05d5\u05d1\u05d5\u05ea \u05db\u05e7\u05d5 \u05d1\u05e1\u05d9\u05e1 \u05dc\u05e1\u05e8\u05d9\u05e7\u05d4."},
        ],
        "how_title": "\u05d0\u05d9\u05da \u05d6\u05d4 \u05e2\u05d5\u05d1\u05d3",
        "how_sub": "\u05e9\u05dc\u05d5\u05e9\u05d4 \u05e6\u05e2\u05d3\u05d9\u05dd \u05de\u05d3\u05d5\u05d7 \u05de\u05e2\u05d1\u05d3\u05d4 \u05de\u05d1\u05dc\u05d1\u05dc \u05dc\u05e1\u05d9\u05db\u05d5\u05dd \u05de\u05d1\u05e0\u05d9 \u05e9\u05d0\u05e4\u05e9\u05e8 \u05dc\u05d4\u05d1\u05d9\u05df \u05d1\u05d0\u05de\u05ea.",
        "how_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "\u05d4\u05e2\u05dc\u05d4 \u05d0\u05ea \u05d4\u05d3\u05d5\u05d7 \u05e9\u05dc\u05da",
                "desc": "PDF, \u05ea\u05de\u05d5\u05e0\u05d4 \u05d0\u05d5 \u05d8\u05e7\u05e1\u05d8 \u05de\u05d5\u05d3\u05d1\u05e7. \u05d1\u05d7\u05e8 \u05de\u05d4 \u05e9\u05d4\u05db\u05d9 \u05e0\u05d5\u05d7.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "\u05d4-AI \u05de\u05d1\u05e0\u05d4 \u05d0\u05ea \u05d4\u05e0\u05ea\u05d5\u05e0\u05d9\u05dd \u05e9\u05dc\u05da",
                "desc": "\u05e2\u05e8\u05db\u05d9\u05dd, \u05d9\u05d7\u05d9\u05d3\u05d5\u05ea \u05d5\u05d8\u05d5\u05d5\u05d7\u05d9\u05dd \u05de\u05d7\u05d5\u05dc\u05e6\u05d9\u05dd \u05d5\u05de\u05d0\u05d5\u05e8\u05d2\u05e0\u05d9\u05dd \u05d1\u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d5\u05ea \u05d1\u05e8\u05d5\u05e8\u05d5\u05ea.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "\u05e7\u05d1\u05dc \u05d0\u05ea \u05d4\u05d3\u05d5\u05d7 \u05d4\u05de\u05d5\u05e1\u05d1\u05e8 \u05e9\u05dc\u05da",
                "desc": "\u05e6\u05d9\u05d5\u05df \u05d1\u05e8\u05d9\u05d0\u05d5\u05ea, \u05e1\u05de\u05e0\u05d9\u05dd \u05de\u05e1\u05d5\u05de\u05e0\u05d9\u05dd, \u05d4\u05e1\u05d1\u05e8\u05d9\u05dd \u05d1\u05e9\u05e4\u05d4 \u05e4\u05e9\u05d5\u05d8\u05d4 \u05d5-PDF \u05dc\u05d4\u05d5\u05e8\u05d3\u05d4.",
            },
        ],
        "preview_title": "\u05d0\u05d9\u05da \u05e0\u05e8\u05d0\u05d4 \u05d4\u05d3\u05d5\u05d7 \u05d4\u05de\u05d5\u05e1\u05d1\u05e8 \u05e9\u05dc\u05da",
        "preview_sub": "\u05d4\u05e0\u05d4 \u05d4\u05e6\u05e6\u05d4 \u05e9\u05dc \u05d0\u05d9\u05da NoryaAI \u05de\u05d1\u05e0\u05d4 \u05d5\u05de\u05e1\u05d1\u05d9\u05e8 \u05d0\u05ea \u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d4\u05d3\u05dd \u05e9\u05dc\u05da.",
        "preview_lines": [
            {"label": "\u05e6\u05d9\u05d5\u05df \u05d1\u05e8\u05d9\u05d0\u05d5\u05ea", "value": "78 / 100 \u2014 \u05d8\u05d5\u05d1 \u05d1\u05d0\u05d5\u05e4\u05df \u05db\u05dc\u05dc\u05d9, \u05db\u05de\u05d4 \u05e1\u05de\u05e0\u05d9\u05dd \u05dc\u05d1\u05d3\u05d9\u05e7\u05d4"},
            {"label": "WBC", "value": "6.8 \u00d710\u00b3/\u00b5L \u2014 \u05e1\u05e4\u05d9\u05e8\u05ea \u05ea\u05d0\u05d9 \u05d3\u05dd \u05dc\u05d1\u05e0\u05d9\u05dd \u05ea\u05e7\u05d9\u05e0\u05d4 (4.5\u201311.0)"},
            {"label": "\u05d4\u05de\u05d5\u05d2\u05dc\u05d5\u05d1\u05d9\u05df", "value": "14.2 g/dL \u2014 \u05d1\u05d8\u05d5\u05d5\u05d7 \u05d4\u05d9\u05d9\u05d7\u05d5\u05e1 (13.5\u201317.5)"},
            {"label": "ALT", "value": "42 U/L \u2014 \u05d0\u05e0\u05d6\u05d9\u05dd \u05db\u05d1\u05d3 \u05de\u05d5\u05d2\u05d1\u05d4 \u05de\u05e2\u05d8 (normal: 7\u201335)"},
            {"label": "TSH", "value": "2.1 mIU/L \u2014 \u05ea\u05e4\u05e7\u05d5\u05d3 \u05ea\u05e8\u05d9\u05e1 \u05ea\u05e7\u05d9\u05df (0.4\u20134.0)"},
            {"label": "\u05d5\u05d9\u05d8\u05de\u05d9\u05df D", "value": "18 ng/mL \u2014 \u05de\u05ea\u05d7\u05ea \u05dc\u05e8\u05de\u05d4 \u05d4\u05de\u05d5\u05de\u05dc\u05e6\u05ea (30\u2013100)"},
        ],
        "preview_disclaimer": "\u05e0\u05ea\u05d5\u05e0\u05d9\u05dd \u05dc\u05d3\u05d5\u05d2\u05de\u05d4 \u05d1\u05dc\u05d1\u05d3. \u05d4\u05d3\u05d5\u05d7 \u05d4\u05d0\u05de\u05d9\u05ea\u05d9 \u05e9\u05dc\u05da \u05d9\u05e9\u05e7\u05e3 \u05d0\u05ea \u05e2\u05e8\u05db\u05d9 \u05d4\u05de\u05e2\u05d1\u05d3\u05d4 \u05d4\u05d0\u05d9\u05e9\u05d9\u05d9\u05dd \u05e9\u05dc\u05da, \u05d4\u05d9\u05d7\u05d9\u05d3\u05d5\u05ea \u05d5\u05d8\u05d5\u05d5\u05d7\u05d9 \u05d4\u05d9\u05d9\u05d7\u05d5\u05e1.",
        "faqs": [
            {
                "q": "\u05de\u05d4 \u05d6\u05d4 \u05d0\u05d5\u05de\u05e8 \u201c\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d3\u05dd \u05de\u05d5\u05e1\u05d1\u05e8\u05d5\u05ea\u201d?",
                "a": "\u05d6\u05d4 \u05d0\u05d5\u05de\u05e8 \u05dc\u05d4\u05e4\u05d5\u05da \u05d0\u05ea \u05d4\u05de\u05e1\u05e4\u05e8\u05d9\u05dd \u05d4\u05d2\u05d5\u05dc\u05de\u05d9\u05d9\u05dd, \u05d4\u05e7\u05d9\u05e6\u05d5\u05e8\u05d9\u05dd \u05d5\u05d8\u05d5\u05d5\u05d7\u05d9 \u05d4\u05d9\u05d9\u05d7\u05d5\u05e1 \u05d1\u05d3\u05d5\u05d7 \u05d4\u05de\u05e2\u05d1\u05d3\u05d4 \u05e9\u05dc\u05da \u05dc\u05d4\u05e1\u05d1\u05e8\u05d9\u05dd \u05d1\u05e9\u05e4\u05d4 \u05e4\u05e9\u05d5\u05d8\u05d4 \u05e9\u05d0\u05e4\u05e9\u05e8 \u05dc\u05d4\u05d1\u05d9\u05df \u2014 \u05e2\u05dd \u05d4\u05e7\u05e9\u05e8 \u05dc\u05d2\u05d1\u05d9 \u05de\u05d4 \u05db\u05dc \u05e2\u05e8\u05da \u05de\u05d5\u05d3\u05d3 \u05d5\u05d4\u05d0\u05dd \u05d4\u05d5\u05d0 \u05d1\u05d2\u05d1\u05d5\u05dc\u05d5\u05ea \u05d4\u05ea\u05e7\u05df.",
            },
            {
                "q": "\u05d4\u05d0\u05dd NoryaAI \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05e1\u05d1\u05d9\u05e8 \u05db\u05dc \u05e1\u05d5\u05d2 \u05e9\u05dc \u05d1\u05d3\u05d9\u05e7\u05ea \u05d3\u05dd?",
                "a": "NoryaAI \u05ea\u05d5\u05de\u05da \u05d1\u05e8\u05d5\u05d1 \u05e4\u05d0\u05e0\u05dc\u05d9 \u05d4\u05d3\u05dd \u05d4\u05e1\u05d8\u05e0\u05d3\u05e8\u05d8\u05d9\u05d9\u05dd \u05db\u05d5\u05dc\u05dc \u05e1\u05e4\u05d9\u05e8\u05ea \u05d3\u05dd, \u05e4\u05d0\u05e0\u05dc\u05d9\u05dd \u05de\u05d8\u05d1\u05d5\u05dc\u05d9\u05d9\u05dd, \u05ea\u05e4\u05e7\u05d5\u05d3 \u05db\u05d1\u05d3 \u05d5\u05db\u05dc\u05d9\u05d5\u05ea, \u05ea\u05e8\u05d9\u05e1, \u05e9\u05d5\u05de\u05e0\u05d9\u05dd, \u05d5\u05d9\u05d8\u05de\u05d9\u05e0\u05d9\u05dd \u05d5\u05e1\u05de\u05e0\u05d9 \u05d3\u05dc\u05e7\u05ea. \u05d0\u05dd \u05d4\u05d3\u05d5\u05d7 \u05e9\u05dc\u05da \u05de\u05db\u05d9\u05dc \u05e2\u05e8\u05db\u05d9\u05dd \u05e9\u05e0\u05d9\u05ea\u05df \u05dc\u05e0\u05ea\u05d7, \u05d4\u05dd \u05d9\u05d9\u05db\u05dc\u05dc\u05d5 \u05d1\u05e1\u05d9\u05db\u05d5\u05dd \u05d4\u05de\u05d1\u05e0\u05d9 \u05e9\u05dc\u05da.",
            },
            {
                "q": "\u05d4\u05d0\u05dd \u05d6\u05d5 \u05d0\u05d1\u05d7\u05e0\u05d4 \u05e8\u05e4\u05d5\u05d0\u05d9\u05ea?",
                "a": "\u05dc\u05d0. NoryaAI \u05de\u05e1\u05e4\u05e7 \u05d4\u05e1\u05d1\u05e8\u05d9\u05dd \u05de\u05d1\u05e0\u05d9\u05d9\u05dd \u05d5\u05d7\u05d9\u05e0\u05d5\u05db\u05d9\u05d9\u05dd \u05e9\u05dc \u05e2\u05e8\u05db\u05d9 \u05d4\u05de\u05e2\u05d1\u05d3\u05d4 \u05e9\u05dc\u05da. \u05d4\u05d5\u05d0 \u05dc\u05d0 \u05de\u05d0\u05d1\u05d7\u05df \u05de\u05e6\u05d1\u05d9\u05dd, \u05dc\u05d0 \u05de\u05de\u05dc\u05d9\u05e5 \u05e2\u05dc \u05d8\u05d9\u05e4\u05d5\u05dc\u05d9\u05dd \u05d5\u05dc\u05d0 \u05de\u05d7\u05dc\u05d9\u05e3 \u05d9\u05d9\u05e2\u05d5\u05e5 \u05e8\u05e4\u05d5\u05d0\u05d9 \u05de\u05e7\u05e6\u05d5\u05e2\u05d9. \u05d4\u05ea\u05d9\u05d9\u05e2\u05e5 \u05ea\u05de\u05d9\u05d3 \u05e2\u05dd \u05d0\u05d9\u05e9 \u05de\u05e7\u05e6\u05d5\u05e2 \u05d1\u05ea\u05d7\u05d5\u05dd \u05d4\u05d1\u05e8\u05d9\u05d0\u05d5\u05ea.",
            },
            {
                "q": "\u05dc\u05de\u05d4 \u05d8\u05d5\u05d5\u05d7\u05d9 \u05d4\u05d9\u05d9\u05d7\u05d5\u05e1 \u05e9\u05d5\u05e0\u05d9\u05dd \u05d1\u05d9\u05df \u05de\u05e2\u05d1\u05d3\u05d5\u05ea?",
                "a": "\u05de\u05e2\u05d1\u05d3\u05d5\u05ea \u05de\u05e9\u05ea\u05de\u05e9\u05d5\u05ea \u05d1\u05e6\u05d9\u05d5\u05d3, \u05e9\u05d9\u05d8\u05d5\u05ea \u05d5\u05d3\u05d2\u05d9\u05de\u05d5\u05ea \u05d0\u05d5\u05db\u05dc\u05d5\u05e1\u05d9\u05d4 \u05e9\u05d5\u05e0\u05d9\u05dd \u05db\u05d3\u05d9 \u05dc\u05e7\u05d1\u05d5\u05e2 \u05d0\u05ea \u05d4\u05d8\u05d5\u05d5\u05d7\u05d9\u05dd \u05e9\u05dc\u05d4\u05dd. \u05d2\u05d9\u05dc, \u05de\u05d9\u05df \u05d5\u05d0\u05e4\u05d9\u05dc\u05d5 \u05d2\u05d5\u05d1\u05d4 \u05d9\u05db\u05d5\u05dc\u05d9\u05dd \u05dc\u05d4\u05e9\u05e4\u05d9\u05e2 \u05e2\u05dc \u05de\u05d4 \u05e9\u05de\u05e2\u05d1\u05d3\u05d4 \u05de\u05d7\u05e9\u05d9\u05d1\u05d4 \u201c\u05ea\u05e7\u05d9\u05df\u201d. \u05dc\u05db\u05df \u05d0\u05d5\u05ea\u05d5 \u05e2\u05e8\u05da \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d4\u05d9\u05d5\u05ea \u05de\u05e1\u05d5\u05de\u05df \u05d1\u05de\u05e2\u05d1\u05d3\u05d4 \u05d0\u05d7\u05ea \u05d0\u05da \u05dc\u05d0 \u05d1\u05d0\u05d7\u05e8\u05ea.",
            },
            {
                "q": "\u05d0\u05e4\u05e9\u05e8 \u05dc\u05e7\u05d1\u05dc \u05d0\u05ea \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05de\u05d5\u05e1\u05d1\u05e8\u05d5\u05ea \u05d1\u05e9\u05e4\u05d4 \u05d0\u05d7\u05e8\u05ea?",
                "a": "\u05db\u05df. NoryaAI \u05de\u05e4\u05d9\u05e7 \u05d3\u05d5\u05d7\u05d5\u05ea \u05d1-9+ \u05e9\u05e4\u05d5\u05ea \u05db\u05d5\u05dc\u05dc \u05d0\u05e0\u05d2\u05dc\u05d9\u05ea, \u05d2\u05e8\u05de\u05e0\u05d9\u05ea, \u05d8\u05d5\u05e8\u05e7\u05d9\u05ea, \u05e6\u05e8\u05e4\u05ea\u05d9\u05ea, \u05d0\u05d9\u05d8\u05dc\u05e7\u05d9\u05ea, \u05e1\u05e4\u05e8\u05d3\u05d9\u05ea, \u05e2\u05d1\u05e8\u05d9\u05ea, \u05d4\u05d9\u05e0\u05d3\u05d9\u05ea \u05d5\u05e2\u05e8\u05d1\u05d9\u05ea \u2014 \u05e2\u05dd \u05e9\u05d9\u05de\u05d5\u05e8 \u05d4\u05d4\u05e7\u05e9\u05e8 \u05d4\u05e8\u05e4\u05d5\u05d0\u05d9 \u05d1\u05ea\u05e8\u05d2\u05d5\u05dd.",
            },
            {
                "q": "\u05d1\u05de\u05d4 \u05d6\u05d4 \u05e9\u05d5\u05e0\u05d4 \u05de\u05e4\u05e9\u05d5\u05d8 \u05dc\u05d7\u05e4\u05e9 \u05d0\u05ea \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d1\u05d2\u05d5\u05d2\u05dc?",
                "a": "\u05d7\u05d9\u05e4\u05d5\u05e9 \u05e2\u05e8\u05db\u05d9\u05dd \u05d1\u05d5\u05d3\u05d3\u05d9\u05dd \u05d0\u05d7\u05d3 \u05d0\u05d7\u05d3 \u05d1\u05d2\u05d5\u05d2\u05dc \u05e0\u05d5\u05ea\u05df \u05de\u05d9\u05d3\u05e2 \u05de\u05e4\u05d5\u05d6\u05e8 \u05d5\u05db\u05dc\u05dc\u05d9. NoryaAI \u05e7\u05d5\u05e8\u05d0 \u05d0\u05ea \u05db\u05dc \u05d4\u05d3\u05d5\u05d7 \u05e9\u05dc\u05da \u05d1\u05d1\u05ea \u05d0\u05d7\u05ea, \u05de\u05e9\u05d5\u05d5\u05d4 \u05db\u05dc \u05e2\u05e8\u05da \u05dc\u05d8\u05d5\u05d5\u05d7 \u05d4\u05d9\u05d9\u05d7\u05d5\u05e1 \u05e9\u05dc\u05d5 \u05d5\u05de\u05e4\u05d9\u05e7 \u05e1\u05d9\u05db\u05d5\u05dd \u05de\u05d1\u05e0\u05d9 \u05d0\u05d7\u05d3 \u05e2\u05dd \u05e6\u05d9\u05d5\u05df \u05d1\u05e8\u05d9\u05d0\u05d5\u05ea, \u05e1\u05de\u05e0\u05d9\u05dd \u05de\u05e1\u05d5\u05de\u05e0\u05d9\u05dd \u05d5\u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d5\u05ea \u2014 \u05d4\u05db\u05dc \u05d1\u05de\u05e7\u05d5\u05dd \u05d0\u05d7\u05d3.",
            },
        ],
        "cta_title": "\u05de\u05d5\u05db\u05df \u05dc\u05d4\u05d1\u05d9\u05df \u05d0\u05ea \u05d1\u05d3\u05d9\u05e7\u05ea \u05d4\u05d3\u05dd \u05e9\u05dc\u05da?",
        "cta_sub": "\u05d4\u05e2\u05dc\u05d4 \u05d0\u05ea \u05d3\u05d5\u05d7 \u05d4\u05de\u05e2\u05d1\u05d3\u05d4 \u05e9\u05dc\u05da \u05d5\u05e7\u05d1\u05dc \u05e1\u05d9\u05db\u05d5\u05dd \u05d1\u05e8\u05d5\u05e8 \u05d5\u05de\u05d1\u05e0\u05d4 \u05e2\u05dd \u05d4\u05e1\u05d1\u05e8\u05d9\u05dd \u05d1\u05e9\u05e4\u05d4 \u05e4\u05e9\u05d5\u05d8\u05d4 \u2014 \u05ea\u05d5\u05da \u05d3\u05e7\u05d5\u05ea.",
        "cta_primary": "\u05d4\u05e2\u05dc\u05d4 \u05d5\u05e0\u05ea\u05d7 \u05e2\u05db\u05e9\u05d9\u05d5",
        "cta_secondary": "\u05e6\u05e4\u05d4 \u05d1\u05de\u05d7\u05d9\u05e8\u05d9\u05dd",
    }
