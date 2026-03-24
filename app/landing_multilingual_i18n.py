# -*- coding: utf-8 -*-
"""Multilingual Blood Test — landing page i18n content for all supported locales."""
from __future__ import annotations

MULTILINGUAL_SLUGS: dict[str, str] = {
    "en": "understand-blood-test-results-in-your-language",
    "tr": "kan-tahlili-kendi-dilinde",
    "de": "blutwerte-in-deiner-sprache",
    "es": "understand-blood-test-results-in-your-language",
    "fr": "understand-blood-test-results-in-your-language",
    "it": "understand-blood-test-results-in-your-language",
    "he": "understand-blood-test-results-in-your-language",
    "hi": "understand-blood-test-results-in-your-language",
    "ar": "understand-blood-test-results-in-your-language",
}

_LANGS_LIST = [
    {"flag": "\U0001f1ec\U0001f1e7", "name": "English"},
    {"flag": "\U0001f1e9\U0001f1ea", "name": "Deutsch"},
    {"flag": "\U0001f1f9\U0001f1f7", "name": "Türkçe"},
    {"flag": "\U0001f1eb\U0001f1f7", "name": "Français"},
    {"flag": "\U0001f1ee\U0001f1f9", "name": "Italiano"},
    {"flag": "\U0001f1ea\U0001f1f8", "name": "Español"},
    {"flag": "\U0001f1ee\U0001f1f1", "name": "עברית"},
    {"flag": "\U0001f1ee\U0001f1f3", "name": "हिन्दी"},
    {"flag": "\U0001f1f8\U0001f1e6", "name": "العربية"},
    {"flag": "\U0001f30d", "name": "More coming"},
]


def _en() -> dict:
    return {
        "meta_title": "Understand Blood Test Results in Your Language | NoryaAI",
        "meta_description": "Got lab results in a language you don\u2019t fully understand? Upload your blood test and get a structured, easy-to-read report in English, German, Turkish, French, and 6 more languages.",
        "hero_title": "Understand Your Blood Test Results \u2014 in Your Language",
        "hero_sub": "Living abroad or dealing with a lab report in an unfamiliar language? Upload your results and get a clear, structured explanation in the language you are most comfortable with.",
        "cta_hero_primary": "Analyze my blood test",
        "cta_hero_secondary": "See sample reports",
        "barrier_title": "Why language makes lab reports harder to understand",
        "barrier_sub": "A blood test is already difficult to read. When the report is in a language that is not your first, the challenge multiplies.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Medical terms you cannot look up easily",
                "desc": "Lab reports are full of abbreviations and clinical terms. When those terms are in another language, even a dictionary does not always help \u2014 medical vocabulary is specialized.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Different naming conventions",
                "desc": "The same blood test may have a different name, abbreviation, or panel grouping depending on the country. A \u201cBlutbild\u201d in Germany is a CBC in the US, but the structure can differ.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Units and ranges vary by region",
                "desc": "Is your glucose in mg/dL or mmol/L? Reference ranges and measurement systems differ between countries, making it harder to compare values you may have seen before.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Generic translators miss medical nuance",
                "desc": "Running a lab report through a general translator can produce awkward or misleading results. Medical context requires more than word-for-word translation.",
            },
        ],
        "helps_title": "How NoryaAI bridges the language gap",
        "helps_sub": "NoryaAI does not just translate your report. It reads, structures, and explains your results in the language you choose.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Upload in any language",
                "desc": "Your lab report can be in German, Turkish, Italian, French, or any supported language. Upload the PDF, photo, or paste the text.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI structures your data",
                "desc": "Values, units, and reference ranges are extracted and organized into clear categories \u2014 regardless of the original language.",
            },
            {
                "icon": "\U0001f310",
                "title": "Get your report in your language",
                "desc": "Choose the output language. Your structured summary, explanations, and health score are generated in the language you are most comfortable reading.",
            },
        ],
        "langs_title": "Supported report languages",
        "langs_sub": "Upload your lab results in any of these languages and receive your structured report in whichever you prefer.",
        "langs": _LANGS_LIST,
        "who_title": "Who this is for",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Expats and immigrants",
                "desc": "You moved to a new country and got bloodwork done. The report is in the local language, but you think and understand health topics in your mother tongue.",
            },
            {
                "icon": "\U0001f393",
                "title": "International students",
                "desc": "Required health screenings at university often produce reports in the local language. A structured explanation in your own language helps you follow up.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Families across borders",
                "desc": "Your parent or partner got lab results in another country. Upload their report and generate a summary in the language you both understand.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Medical tourists and travelers",
                "desc": "Had bloodwork done while traveling or during a medical trip abroad? Get a structured summary you can share with your doctor at home.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Bilingual doctor visits",
                "desc": "You understand your doctor in one language but received your lab report in another. A single structured PDF in your preferred language can make the appointment smoother.",
            },
            {
                "icon": "\U0001f310",
                "title": "Anyone comparing international results",
                "desc": "If you have had bloodwork done in different countries, a unified structured format in one language makes it easier to track your values over time.",
            },
        ],
        "mid_cta_title": "Your lab report, your language",
        "mid_cta_sub": "Upload your blood test in any supported language and choose how you want to read the results.",
        "faqs": [
            {
                "q": "Can I upload a lab report in one language and get the results in another?",
                "a": "Yes. You can upload a report in any supported language \u2014 German, Turkish, French, Italian, and more \u2014 and choose a different language for your structured output. The values and reference ranges stay the same; the explanations are generated in your preferred language.",
            },
            {
                "q": "Is this a medical translation service?",
                "a": "No. NoryaAI does not provide certified medical translations. It reads your lab report, structures the data, and generates an educational explanation in the language you choose. For official or legal purposes, consult a certified medical translator.",
            },
            {
                "q": "Does the language affect the accuracy of the analysis?",
                "a": "No. The underlying analysis works with the numerical values, units, and reference ranges in your report. The language of the original document does not affect how the values are parsed or structured.",
            },
            {
                "q": "Which languages are supported?",
                "a": "NoryaAI currently supports English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic. More languages are being added over time.",
            },
            {
                "q": "Can I share the report with a doctor who speaks a different language?",
                "a": "Yes. You can generate the same report in multiple languages if needed. The structured PDF format is designed to be clear and useful regardless of the reader\u2019s medical background.",
            },
            {
                "q": "Is NoryaAI a replacement for my doctor?",
                "a": "No. NoryaAI provides structured, educational explanations to help you understand your lab results. It does not diagnose, treat, or prescribe. Always consult a qualified healthcare professional for medical decisions.",
            },
        ],
        "cta_title": "Ready to understand your results?",
        "cta_sub": "Upload your blood test in any language and get a clear, structured report in the one you prefer.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Analyze", "path": "/analyze"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "AI Blood Test Analyzer", "path": "/en/ai-blood-test-analyzer"},
            {"label": "Sample Reports", "path": "/en/sample-blood-test-reports"},
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }


def _tr() -> dict:
    return {
        "meta_title": "Kan Tahlili Sonuçlarını Kendi Dilinde Anla | NoryaAI",
        "meta_description": "Laboratuvar sonuçların anlamadığın bir dilde mi? Kan tahlilini yükle, Türkçe, Almanca, İngilizce ve 6 dilde daha yapılandırılmış, kolay okunur rapor al.",
        "hero_title": "Kan Tahlili Sonuçlarını Kendi Dilinde Anla",
        "hero_sub": "Yurt dışında mı yaşıyorsun veya tanımadığın bir dilde laboratuvar raporu mu aldın? Sonuçlarını yükle, en rahat anladığın dilde açık ve yapılandırılmış bir açıklama al.",
        "cta_hero_primary": "Kan tahlilimi analiz et",
        "cta_hero_secondary": "Örnek raporları gör",
        "barrier_title": "Dil neden laboratuvar raporlarını anlamayı zorlaştırır",
        "barrier_sub": "Kan tahlili zaten okunması zor bir belge. Rapor ana dilin olmayan bir dilde olduğunda zorluk katlanır.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Kolayca araştıramadığın tıbbi terimler",
                "desc": "Laboratuvar raporları kısaltmalar ve klinik terimlerle doludur. Bu terimler başka bir dilde olduğunda sözlük bile her zaman yardımcı olmaz — tıbbi terminoloji çok özeldir.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Farklı adlandırma kuralları",
                "desc": "Aynı kan testi ülkeye göre farklı bir isim, kısaltma veya panel gruplamasına sahip olabilir. Almanya'da 'Blutbild', ABD'de CBC'dir ama yapı farklılık gösterebilir.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Birimler ve aralıklar bölgeye göre değişir",
                "desc": "Glukozun mg/dL mi yoksa mmol/L mi? Referans aralıkları ve ölçüm sistemleri ülkeler arasında farklılık gösterir, daha önce gördüğün değerlerle karşılaştırmayı zorlaştırır.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Genel çevirmenler tıbbi nüansı kaçırır",
                "desc": "Bir laboratuvar raporunu genel bir çeviri aracından geçirmek tuhaf veya yanıltıcı sonuçlar üretebilir. Tıbbi bağlam, kelime kelime çeviriden daha fazlasını gerektirir.",
            },
        ],
        "helps_title": "NoryaAI dil engelini nasıl aşar",
        "helps_sub": "NoryaAI raporunu sadece çevirmez. Sonuçlarını okur, yapılandırır ve seçtiğin dilde açıklar.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Herhangi bir dilde yükle",
                "desc": "Laboratuvar raporun Almanca, İngilizce, İtalyanca, Fransızca veya desteklenen başka bir dilde olabilir. PDF, fotoğraf yükle veya metni yapıştır.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "Yapay zekâ verilerini yapılandırır",
                "desc": "Değerler, birimler ve referans aralıkları orijinal dil ne olursa olsun çıkarılır ve net kategorilere düzenlenir.",
            },
            {
                "icon": "\U0001f310",
                "title": "Raporunu kendi dilinde al",
                "desc": "Çıktı dilini seç. Yapılandırılmış özet, açıklamalar ve sağlık puanın en rahat okuduğun dilde oluşturulur.",
            },
        ],
        "langs_title": "Desteklenen rapor dilleri",
        "langs_sub": "Laboratuvar sonuçlarını bu dillerden herhangi birinde yükle ve yapılandırılmış raporunu tercih ettiğin dilde al.",
        "langs": _LANGS_LIST,
        "who_title": "Bu kimler için",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Gurbetçiler ve göçmenler",
                "desc": "Yeni bir ülkeye taşındın ve kan testi yaptırdın. Rapor yerel dilde ama sağlık konularını ana dilinde düşünüyor ve anlıyorsun.",
            },
            {
                "icon": "\U0001f393",
                "title": "Uluslararası öğrenciler",
                "desc": "Üniversitedeki zorunlu sağlık taramaları genellikle yerel dilde raporlar üretir. Kendi dilinde yapılandırılmış bir açıklama takip etmeni kolaylaştırır.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Sınır ötesi aileler",
                "desc": "Annen veya eşin başka bir ülkede laboratuvar sonuçları aldı. Raporlarını yükle ve ikinizin de anladığı dilde bir özet oluştur.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Sağlık turizmi ve gezginler",
                "desc": "Seyahat ederken veya yurt dışında bir sağlık gezisi sırasında kan testi mi yaptırdın? Evdeki doktorunla paylaşabileceğin yapılandırılmış bir özet al.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "İki dilli doktor ziyaretleri",
                "desc": "Doktorunu bir dilde anlıyorsun ama laboratuvar raporunu başka bir dilde aldın. Tercih ettiğin dilde tek bir yapılandırılmış PDF randevuyu kolaylaştırabilir.",
            },
            {
                "icon": "\U0001f310",
                "title": "Uluslararası sonuçları karşılaştıranlar",
                "desc": "Farklı ülkelerde kan testi yaptırdıysan, tek bir dilde birleşik yapılandırılmış format değerlerini zaman içinde takip etmeyi kolaylaştırır.",
            },
        ],
        "mid_cta_title": "Laboratuvar raporun, senin dilin",
        "mid_cta_sub": "Kan tahlilini desteklenen herhangi bir dilde yükle ve sonuçları nasıl okumak istediğini seç.",
        "faqs": [
            {
                "q": "Bir dilde laboratuvar raporu yükleyip sonuçları başka bir dilde alabilir miyim?",
                "a": "Evet. Raporu desteklenen herhangi bir dilde — Almanca, İngilizce, Fransızca, İtalyanca ve daha fazlası — yükleyebilir ve yapılandırılmış çıktın için farklı bir dil seçebilirsin. Değerler ve referans aralıkları aynı kalır; açıklamalar tercih ettiğin dilde oluşturulur.",
            },
            {
                "q": "Bu bir tıbbi çeviri hizmeti mi?",
                "a": "Hayır. NoryaAI sertifikalı tıbbi çeviri sağlamaz. Laboratuvar raporunu okur, verileri yapılandırır ve seçtiğin dilde eğitici bir açıklama oluşturur. Resmi veya yasal amaçlar için sertifikalı bir tıbbi çevirmene başvur.",
            },
            {
                "q": "Dil analizin doğruluğunu etkiler mi?",
                "a": "Hayır. Temel analiz raporundaki sayısal değerler, birimler ve referans aralıklarıyla çalışır. Orijinal belgenin dili değerlerin nasıl ayrıştırıldığını veya yapılandırıldığını etkilemez.",
            },
            {
                "q": "Hangi diller destekleniyor?",
                "a": "NoryaAI şu anda İngilizce, Almanca, Türkçe, Fransızca, İtalyanca, İspanyolca, İbranice, Hintçe ve Arapça desteklemektedir. Zaman içinde daha fazla dil eklenmektedir.",
            },
            {
                "q": "Raporu farklı bir dil konuşan bir doktorla paylaşabilir miyim?",
                "a": "Evet. Gerekirse aynı raporu birden fazla dilde oluşturabilirsin. Yapılandırılmış PDF formatı, okuyucunun tıbbi geçmişi ne olursa olsun açık ve kullanışlı olacak şekilde tasarlanmıştır.",
            },
            {
                "q": "NoryaAI doktorumun yerini tutar mı?",
                "a": "Hayır. NoryaAI laboratuvar sonuçlarını anlamanıza yardımcı olmak için yapılandırılmış, eğitici açıklamalar sunar. Teşhis koymaz, tedavi uygulamaz veya reçete yazmaz. Tıbbi kararlar için her zaman nitelikli bir sağlık uzmanına başvurun.",
            },
        ],
        "cta_title": "Sonuçlarını anlamaya hazır mısın?",
        "cta_sub": "Kan tahlilini herhangi bir dilde yükle ve tercih ettiğin dilde açık, yapılandırılmış bir rapor al.",
        "cta_primary": "Yükle ve analiz et",
        "cta_secondary": "Fiyatları gör",
        "internal_links": [
            {"label": "Analiz", "path": "/analyze"},
            {"label": "Sonuç Yükle", "path": "/tr/kan-tahlili-yukle"},
            {"label": "Yapay Zekâ Kan Analizi", "path": "/tr/yapay-zeka-kan-tahlili-analizi"},
            {"label": "Örnek Raporlar", "path": "/tr/ornek-kan-tahlili-raporlari"},
            {"label": "Kan Tahlili Açıklaması", "path": "/tr/kan-tahlili-sonuclari-aciklama"},
            {"label": "Fiyatlar", "path": "/pricing"},
            {"label": "Blog", "path": "/tr/blog"},
        ],
    }


def _de() -> dict:
    return {
        "meta_title": "Blutwerte in deiner Sprache verstehen | NoryaAI",
        "meta_description": "Laborergebnisse in einer Sprache erhalten, die du nicht vollständig verstehst? Lade deinen Bluttest hoch und erhalte einen strukturierten, leicht verständlichen Bericht auf Deutsch, Englisch, Türkisch und in 6 weiteren Sprachen.",
        "hero_title": "Verstehe deine Blutwerte \u2014 in deiner Sprache",
        "hero_sub": "Im Ausland lebend oder mit einem Laborbericht in einer fremden Sprache? Lade deine Ergebnisse hoch und erhalte eine klare, strukturierte Erklärung in der Sprache, die dir am vertrautesten ist.",
        "cta_hero_primary": "Mein Blutbild analysieren",
        "cta_hero_secondary": "Beispielberichte ansehen",
        "barrier_title": "Warum Sprache Laborberichte schwerer verständlich macht",
        "barrier_sub": "Ein Bluttest ist bereits schwer zu lesen. Wenn der Bericht in einer Sprache ist, die nicht deine Muttersprache ist, vervielfacht sich die Herausforderung.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Medizinische Begriffe, die schwer nachzuschlagen sind",
                "desc": "Laborberichte sind voller Abkürzungen und klinischer Begriffe. Wenn diese in einer anderen Sprache sind, hilft selbst ein Wörterbuch nicht immer — medizinisches Vokabular ist hochspezialisiert.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Unterschiedliche Bezeichnungen",
                "desc": "Derselbe Bluttest kann je nach Land einen anderen Namen, eine andere Abk\u00fcrzung oder Panelgruppierung haben. Ein \u201eBlutbild\u201c in Deutschland ist ein CBC in den USA, aber die Struktur kann sich unterscheiden.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Einheiten und Referenzbereiche variieren nach Region",
                "desc": "Ist dein Glukosewert in mg/dL oder mmol/L? Referenzbereiche und Messsysteme unterscheiden sich zwischen Ländern, was den Vergleich mit früheren Werten erschwert.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Allgemeine Übersetzer verfehlen medizinische Nuancen",
                "desc": "Einen Laborbericht durch einen allgemeinen Übersetzer zu jagen kann unpassende oder irreführende Ergebnisse liefern. Medizinischer Kontext erfordert mehr als wörtliche Übersetzung.",
            },
        ],
        "helps_title": "Wie NoryaAI die Sprachbarriere überbrückt",
        "helps_sub": "NoryaAI übersetzt deinen Bericht nicht nur. Es liest, strukturiert und erklärt deine Ergebnisse in der Sprache deiner Wahl.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "In jeder Sprache hochladen",
                "desc": "Dein Laborbericht kann auf Englisch, Türkisch, Italienisch, Französisch oder in jeder unterstützten Sprache sein. Lade das PDF, Foto hoch oder füge den Text ein.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "KI strukturiert deine Daten",
                "desc": "Werte, Einheiten und Referenzbereiche werden extrahiert und unabhängig von der Originalsprache in klare Kategorien eingeordnet.",
            },
            {
                "icon": "\U0001f310",
                "title": "Erhalte deinen Bericht in deiner Sprache",
                "desc": "Wähle die Ausgabesprache. Deine strukturierte Zusammenfassung, Erklärungen und dein Gesundheitsscore werden in der Sprache erstellt, die du am liebsten liest.",
            },
        ],
        "langs_title": "Unterstützte Berichtssprachen",
        "langs_sub": "Lade deine Laborergebnisse in einer dieser Sprachen hoch und erhalte deinen strukturierten Bericht in der Sprache deiner Wahl.",
        "langs": _LANGS_LIST,
        "who_title": "Für wen das gedacht ist",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Expats und Einwanderer",
                "desc": "Du bist in ein neues Land gezogen und hast Blut abnehmen lassen. Der Bericht ist in der Landessprache, aber du denkst und verstehst Gesundheitsthemen in deiner Muttersprache.",
            },
            {
                "icon": "\U0001f393",
                "title": "Internationale Studierende",
                "desc": "Pflichtuntersuchungen an der Universität liefern oft Berichte in der Landessprache. Eine strukturierte Erklärung in deiner eigenen Sprache hilft dir, die Ergebnisse nachzuverfolgen.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Familien über Grenzen hinweg",
                "desc": "Dein Elternteil oder Partner hat Laborergebnisse in einem anderen Land erhalten. Lade den Bericht hoch und erstelle eine Zusammenfassung in der Sprache, die ihr beide versteht.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Medizintouristen und Reisende",
                "desc": "Auf Reisen oder während eines Medizinaufenthalts im Ausland Blut abnehmen lassen? Erhalte eine strukturierte Zusammenfassung, die du mit deinem Arzt zu Hause teilen kannst.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Zweisprachige Arztbesuche",
                "desc": "Du verstehst deinen Arzt in einer Sprache, aber dein Laborbericht ist in einer anderen. Ein einziges strukturiertes PDF in deiner bevorzugten Sprache kann den Termin reibungsloser gestalten.",
            },
            {
                "icon": "\U0001f310",
                "title": "Internationale Ergebnisse vergleichen",
                "desc": "Wenn du in verschiedenen Ländern Blut abnehmen lassen hast, macht ein einheitliches strukturiertes Format in einer Sprache es einfacher, deine Werte im Zeitverlauf zu verfolgen.",
            },
        ],
        "mid_cta_title": "Dein Laborbericht, deine Sprache",
        "mid_cta_sub": "Lade deinen Bluttest in jeder unterstützten Sprache hoch und wähle, wie du die Ergebnisse lesen möchtest.",
        "faqs": [
            {
                "q": "Kann ich einen Laborbericht in einer Sprache hochladen und die Ergebnisse in einer anderen erhalten?",
                "a": "Ja. Du kannst einen Bericht in jeder unterstützten Sprache hochladen — Englisch, Türkisch, Französisch, Italienisch und mehr — und eine andere Sprache für deine strukturierte Ausgabe wählen. Die Werte und Referenzbereiche bleiben gleich; die Erklärungen werden in deiner bevorzugten Sprache erstellt.",
            },
            {
                "q": "Ist das ein medizinischer Übersetzungsdienst?",
                "a": "Nein. NoryaAI bietet keine zertifizierten medizinischen Übersetzungen. Es liest deinen Laborbericht, strukturiert die Daten und erstellt eine edukative Erklärung in der Sprache deiner Wahl. Für offizielle oder rechtliche Zwecke wende dich an einen zertifizierten medizinischen Übersetzer.",
            },
            {
                "q": "Beeinflusst die Sprache die Genauigkeit der Analyse?",
                "a": "Nein. Die zugrunde liegende Analyse arbeitet mit den numerischen Werten, Einheiten und Referenzbereichen in deinem Bericht. Die Sprache des Originaldokuments beeinflusst nicht, wie die Werte geparst oder strukturiert werden.",
            },
            {
                "q": "Welche Sprachen werden unterstützt?",
                "a": "NoryaAI unterstützt derzeit Englisch, Deutsch, Türkisch, Französisch, Italienisch, Spanisch, Hebräisch, Hindi und Arabisch. Weitere Sprachen werden laufend hinzugefügt.",
            },
            {
                "q": "Kann ich den Bericht mit einem Arzt teilen, der eine andere Sprache spricht?",
                "a": "Ja. Du kannst denselben Bericht bei Bedarf in mehreren Sprachen erstellen. Das strukturierte PDF-Format ist so gestaltet, dass es unabhängig vom medizinischen Hintergrund des Lesers klar und nützlich ist.",
            },
            {
                "q": "Ist NoryaAI ein Ersatz für meinen Arzt?",
                "a": "Nein. NoryaAI bietet strukturierte, edukative Erklärungen, um dir beim Verständnis deiner Laborwerte zu helfen. Es diagnostiziert, behandelt oder verschreibt nicht. Konsultiere immer einen qualifizierten Gesundheitsexperten für medizinische Entscheidungen.",
            },
        ],
        "cta_title": "Bereit, deine Ergebnisse zu verstehen?",
        "cta_sub": "Lade deinen Bluttest in jeder Sprache hoch und erhalte einen klaren, strukturierten Bericht in der Sprache deiner Wahl.",
        "cta_primary": "Hochladen und analysieren",
        "cta_secondary": "Preise ansehen",
        "internal_links": [
            {"label": "Analysieren", "path": "/analyze"},
            {"label": "Ergebnisse hochladen", "path": "/de/bluttest-hochladen"},
            {"label": "KI-Bluttest-Analyse", "path": "/de/ki-bluttest-analyse"},
            {"label": "Beispielberichte", "path": "/de/beispiel-bluttest-berichte"},
            {"label": "Blutwerte erklärt", "path": "/de/bluttest-ergebnisse-erklaert"},
            {"label": "Preise", "path": "/pricing"},
            {"label": "Blog", "path": "/de/blog"},
        ],
    }


def _es() -> dict:
    return {
        "meta_title": "Entiende los resultados de tu análisis de sangre en tu idioma | NoryaAI",
        "meta_description": "¿Recibiste resultados de laboratorio en un idioma que no comprendes del todo? Sube tu análisis de sangre y obtén un informe estructurado y fácil de leer en español, inglés, alemán, francés y 5 idiomas más.",
        "hero_title": "Entiende tus resultados de análisis de sangre \u2014 en tu idioma",
        "hero_sub": "¿Vives en el extranjero o tienes un informe de laboratorio en un idioma desconocido? Sube tus resultados y obtén una explicación clara y estructurada en el idioma con el que te sientas más cómodo.",
        "cta_hero_primary": "Analizar mi análisis de sangre",
        "cta_hero_secondary": "Ver informes de ejemplo",
        "barrier_title": "Por qué el idioma dificulta la comprensión de los informes de laboratorio",
        "barrier_sub": "Un análisis de sangre ya es difícil de leer. Cuando el informe está en un idioma que no es el tuyo, el desafío se multiplica.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Términos médicos difíciles de buscar",
                "desc": "Los informes de laboratorio están llenos de abreviaturas y términos clínicos. Cuando esos términos están en otro idioma, ni siquiera un diccionario ayuda siempre — el vocabulario médico es muy especializado.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Diferentes convenciones de nombres",
                "desc": "El mismo análisis de sangre puede tener un nombre, abreviatura o agrupación de panel diferente según el país. Un «Blutbild» en Alemania es un hemograma en España, pero la estructura puede variar.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Las unidades y rangos varían según la región",
                "desc": "¿Tu glucosa está en mg/dL o mmol/L? Los rangos de referencia y sistemas de medición difieren entre países, lo que dificulta comparar valores que hayas visto antes.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Los traductores genéricos pierden matices médicos",
                "desc": "Pasar un informe de laboratorio por un traductor general puede producir resultados confusos o engañosos. El contexto médico requiere más que una traducción palabra por palabra.",
            },
        ],
        "helps_title": "Cómo NoryaAI elimina la barrera del idioma",
        "helps_sub": "NoryaAI no solo traduce tu informe. Lee, estructura y explica tus resultados en el idioma que elijas.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Sube en cualquier idioma",
                "desc": "Tu informe de laboratorio puede estar en alemán, turco, italiano, francés o cualquier idioma compatible. Sube el PDF, una foto o pega el texto.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "La IA estructura tus datos",
                "desc": "Los valores, unidades y rangos de referencia se extraen y organizan en categorías claras, independientemente del idioma original.",
            },
            {
                "icon": "\U0001f310",
                "title": "Recibe tu informe en tu idioma",
                "desc": "Elige el idioma de salida. Tu resumen estructurado, explicaciones y puntuación de salud se generan en el idioma que prefieras leer.",
            },
        ],
        "langs_title": "Idiomas de informe compatibles",
        "langs_sub": "Sube tus resultados de laboratorio en cualquiera de estos idiomas y recibe tu informe estructurado en el que prefieras.",
        "langs": _LANGS_LIST,
        "who_title": "Para quién es esto",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Expatriados e inmigrantes",
                "desc": "Te mudaste a un nuevo país y te hiciste un análisis de sangre. El informe está en el idioma local, pero piensas y entiendes los temas de salud en tu lengua materna.",
            },
            {
                "icon": "\U0001f393",
                "title": "Estudiantes internacionales",
                "desc": "Los exámenes de salud obligatorios en la universidad suelen generar informes en el idioma local. Una explicación estructurada en tu propio idioma te ayuda a hacer seguimiento.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Familias más allá de las fronteras",
                "desc": "Tu padre o pareja recibió resultados de laboratorio en otro país. Sube su informe y genera un resumen en el idioma que ambos entiendan.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Turistas médicos y viajeros",
                "desc": "¿Te hiciste un análisis de sangre mientras viajabas o durante un viaje médico al extranjero? Obtén un resumen estructurado que puedas compartir con tu médico en casa.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Consultas médicas bilingües",
                "desc": "Entiendes a tu médico en un idioma pero recibiste tu informe de laboratorio en otro. Un solo PDF estructurado en tu idioma preferido puede facilitar la consulta.",
            },
            {
                "icon": "\U0001f310",
                "title": "Comparar resultados internacionales",
                "desc": "Si te has hecho análisis de sangre en diferentes países, un formato estructurado unificado en un solo idioma facilita el seguimiento de tus valores a lo largo del tiempo.",
            },
        ],
        "mid_cta_title": "Tu informe de laboratorio, tu idioma",
        "mid_cta_sub": "Sube tu análisis de sangre en cualquier idioma compatible y elige cómo quieres leer los resultados.",
        "faqs": [
            {
                "q": "¿Puedo subir un informe de laboratorio en un idioma y obtener los resultados en otro?",
                "a": "Sí. Puedes subir un informe en cualquier idioma compatible — alemán, turco, francés, italiano y más — y elegir un idioma diferente para tu salida estructurada. Los valores y rangos de referencia permanecen iguales; las explicaciones se generan en tu idioma preferido.",
            },
            {
                "q": "¿Es esto un servicio de traducción médica?",
                "a": "No. NoryaAI no proporciona traducciones médicas certificadas. Lee tu informe de laboratorio, estructura los datos y genera una explicación educativa en el idioma que elijas. Para fines oficiales o legales, consulta a un traductor médico certificado.",
            },
            {
                "q": "¿El idioma afecta la precisión del análisis?",
                "a": "No. El análisis subyacente trabaja con los valores numéricos, unidades y rangos de referencia de tu informe. El idioma del documento original no afecta cómo se analizan o estructuran los valores.",
            },
            {
                "q": "¿Qué idiomas son compatibles?",
                "a": "NoryaAI actualmente es compatible con inglés, alemán, turco, francés, italiano, español, hebreo, hindi y árabe. Se están añadiendo más idiomas con el tiempo.",
            },
            {
                "q": "¿Puedo compartir el informe con un médico que habla otro idioma?",
                "a": "Sí. Puedes generar el mismo informe en varios idiomas si es necesario. El formato PDF estructurado está diseñado para ser claro y útil independientemente de la formación médica del lector.",
            },
            {
                "q": "¿NoryaAI reemplaza a mi médico?",
                "a": "No. NoryaAI proporciona explicaciones estructuradas y educativas para ayudarte a entender tus resultados de laboratorio. No diagnostica, trata ni prescribe. Siempre consulta a un profesional de la salud cualificado para decisiones médicas.",
            },
        ],
        "cta_title": "¿Listo para entender tus resultados?",
        "cta_sub": "Sube tu análisis de sangre en cualquier idioma y obtén un informe claro y estructurado en el que prefieras.",
        "cta_primary": "Subir y analizar ahora",
        "cta_secondary": "Ver precios",
        "internal_links": [
            {"label": "Analizar", "path": "/analyze"},
            {"label": "Subir resultados", "path": "/es/upload-blood-test-results"},
            {"label": "Analizador de sangre IA", "path": "/es/ai-blood-test-analyzer"},
            {"label": "Informes de ejemplo", "path": "/es/sample-blood-test-reports"},
            {"label": "Resultados explicados", "path": "/es/blood-test-results-explained"},
            {"label": "Precios", "path": "/pricing"},
            {"label": "Blog", "path": "/es/blog"},
        ],
    }


def _fr() -> dict:
    return {
        "meta_title": "Comprendre vos résultats d'analyses sanguines dans votre langue | NoryaAI",
        "meta_description": "Vous avez reçu des résultats de laboratoire dans une langue que vous ne comprenez pas entièrement ? Téléchargez votre analyse de sang et obtenez un rapport structuré et facile à lire en français, anglais, allemand, turc et 5 autres langues.",
        "hero_title": "Comprenez vos résultats d'analyses sanguines \u2014 dans votre langue",
        "hero_sub": "Vous vivez à l'étranger ou avez reçu un rapport de laboratoire dans une langue inconnue ? Téléchargez vos résultats et obtenez une explication claire et structurée dans la langue qui vous convient le mieux.",
        "cta_hero_primary": "Analyser mon bilan sanguin",
        "cta_hero_secondary": "Voir les rapports d'exemple",
        "barrier_title": "Pourquoi la langue rend les rapports de laboratoire plus difficiles à comprendre",
        "barrier_sub": "Une analyse de sang est déjà difficile à lire. Quand le rapport est dans une langue qui n'est pas la vôtre, le défi se multiplie.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Des termes médicaux difficiles à rechercher",
                "desc": "Les rapports de laboratoire sont remplis d'abréviations et de termes cliniques. Quand ces termes sont dans une autre langue, même un dictionnaire n'aide pas toujours — le vocabulaire médical est très spécialisé.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Des conventions de nommage différentes",
                "desc": "Le même test sanguin peut avoir un nom, une abréviation ou un regroupement de panel différent selon le pays. Un « Blutbild » en Allemagne est un hémogramme en France, mais la structure peut varier.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Les unités et plages varient selon la région",
                "desc": "Votre glucose est-elle en mg/dL ou mmol/L ? Les plages de référence et les systèmes de mesure diffèrent entre les pays, ce qui rend plus difficile la comparaison avec des valeurs vues précédemment.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Les traducteurs génériques manquent les nuances médicales",
                "desc": "Passer un rapport de laboratoire dans un traducteur général peut produire des résultats maladroits ou trompeurs. Le contexte médical nécessite plus qu'une traduction mot à mot.",
            },
        ],
        "helps_title": "Comment NoryaAI élimine la barrière linguistique",
        "helps_sub": "NoryaAI ne se contente pas de traduire votre rapport. Il lit, structure et explique vos résultats dans la langue de votre choix.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Téléchargez dans n'importe quelle langue",
                "desc": "Votre rapport de laboratoire peut être en allemand, turc, italien, anglais ou toute autre langue prise en charge. Téléchargez le PDF, une photo ou collez le texte.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "L'IA structure vos données",
                "desc": "Les valeurs, unités et plages de référence sont extraites et organisées en catégories claires — quelle que soit la langue d'origine.",
            },
            {
                "icon": "\U0001f310",
                "title": "Recevez votre rapport dans votre langue",
                "desc": "Choisissez la langue de sortie. Votre résumé structuré, vos explications et votre score de santé sont générés dans la langue que vous préférez lire.",
            },
        ],
        "langs_title": "Langues de rapport prises en charge",
        "langs_sub": "Téléchargez vos résultats de laboratoire dans l'une de ces langues et recevez votre rapport structuré dans celle de votre choix.",
        "langs": _LANGS_LIST,
        "who_title": "À qui cela s'adresse",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Expatriés et immigrants",
                "desc": "Vous avez déménagé dans un nouveau pays et fait une prise de sang. Le rapport est dans la langue locale, mais vous pensez et comprenez les sujets de santé dans votre langue maternelle.",
            },
            {
                "icon": "\U0001f393",
                "title": "Étudiants internationaux",
                "desc": "Les examens de santé obligatoires à l'université produisent souvent des rapports dans la langue locale. Une explication structurée dans votre propre langue vous aide à assurer le suivi.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Familles au-delà des frontières",
                "desc": "Votre parent ou partenaire a reçu des résultats de laboratoire dans un autre pays. Téléchargez leur rapport et générez un résumé dans la langue que vous comprenez tous les deux.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Touristes médicaux et voyageurs",
                "desc": "Vous avez fait une prise de sang en voyage ou lors d'un séjour médical à l'étranger ? Obtenez un résumé structuré à partager avec votre médecin traitant.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Consultations médicales bilingues",
                "desc": "Vous comprenez votre médecin dans une langue mais avez reçu votre rapport de laboratoire dans une autre. Un seul PDF structuré dans votre langue préférée peut faciliter le rendez-vous.",
            },
            {
                "icon": "\U0001f310",
                "title": "Comparer des résultats internationaux",
                "desc": "Si vous avez fait des analyses de sang dans différents pays, un format structuré unifié dans une seule langue facilite le suivi de vos valeurs dans le temps.",
            },
        ],
        "mid_cta_title": "Votre rapport de laboratoire, votre langue",
        "mid_cta_sub": "Téléchargez votre analyse de sang dans n'importe quelle langue prise en charge et choisissez comment vous voulez lire les résultats.",
        "faqs": [
            {
                "q": "Puis-je télécharger un rapport de laboratoire dans une langue et obtenir les résultats dans une autre ?",
                "a": "Oui. Vous pouvez télécharger un rapport dans n'importe quelle langue prise en charge — allemand, turc, anglais, italien et plus — et choisir une langue différente pour votre sortie structurée. Les valeurs et plages de référence restent les mêmes ; les explications sont générées dans votre langue préférée.",
            },
            {
                "q": "Est-ce un service de traduction médicale ?",
                "a": "Non. NoryaAI ne fournit pas de traductions médicales certifiées. Il lit votre rapport de laboratoire, structure les données et génère une explication éducative dans la langue de votre choix. Pour des fins officielles ou légales, consultez un traducteur médical certifié.",
            },
            {
                "q": "La langue affecte-t-elle la précision de l'analyse ?",
                "a": "Non. L'analyse sous-jacente travaille avec les valeurs numériques, les unités et les plages de référence de votre rapport. La langue du document original n'affecte pas la façon dont les valeurs sont analysées ou structurées.",
            },
            {
                "q": "Quelles langues sont prises en charge ?",
                "a": "NoryaAI prend actuellement en charge l'anglais, l'allemand, le turc, le français, l'italien, l'espagnol, l'hébreu, le hindi et l'arabe. D'autres langues sont ajoutées au fil du temps.",
            },
            {
                "q": "Puis-je partager le rapport avec un médecin qui parle une autre langue ?",
                "a": "Oui. Vous pouvez générer le même rapport dans plusieurs langues si nécessaire. Le format PDF structuré est conçu pour être clair et utile, quel que soit le bagage médical du lecteur.",
            },
            {
                "q": "NoryaAI remplace-t-il mon médecin ?",
                "a": "Non. NoryaAI fournit des explications structurées et éducatives pour vous aider à comprendre vos résultats de laboratoire. Il ne diagnostique pas, ne traite pas et ne prescrit pas. Consultez toujours un professionnel de santé qualifié pour les décisions médicales.",
            },
        ],
        "cta_title": "Prêt à comprendre vos résultats ?",
        "cta_sub": "Téléchargez votre analyse de sang dans n'importe quelle langue et obtenez un rapport clair et structuré dans celle que vous préférez.",
        "cta_primary": "Télécharger et analyser",
        "cta_secondary": "Voir les tarifs",
        "internal_links": [
            {"label": "Analyser", "path": "/analyze"},
            {"label": "Télécharger les résultats", "path": "/fr/upload-blood-test-results"},
            {"label": "Analyseur sanguin IA", "path": "/fr/ai-blood-test-analyzer"},
            {"label": "Rapports d'exemple", "path": "/fr/sample-blood-test-reports"},
            {"label": "Résultats expliqués", "path": "/fr/blood-test-results-explained"},
            {"label": "Tarifs", "path": "/pricing"},
            {"label": "Blog", "path": "/fr/blog"},
        ],
    }


def _it() -> dict:
    return {
        "meta_title": "Comprendi i risultati delle analisi del sangue nella tua lingua | NoryaAI",
        "meta_description": "Hai ricevuto risultati di laboratorio in una lingua che non comprendi del tutto? Carica le tue analisi del sangue e ottieni un rapporto strutturato e facile da leggere in italiano, inglese, tedesco, turco e 5 altre lingue.",
        "hero_title": "Comprendi i risultati delle tue analisi del sangue \u2014 nella tua lingua",
        "hero_sub": "Vivi all'estero o hai ricevuto un referto di laboratorio in una lingua sconosciuta? Carica i tuoi risultati e ottieni una spiegazione chiara e strutturata nella lingua con cui ti senti più a tuo agio.",
        "cta_hero_primary": "Analizza le mie analisi del sangue",
        "cta_hero_secondary": "Vedi rapporti di esempio",
        "barrier_title": "Perché la lingua rende i referti di laboratorio più difficili da capire",
        "barrier_sub": "Un'analisi del sangue è già difficile da leggere. Quando il referto è in una lingua che non è la tua, la sfida si moltiplica.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Termini medici difficili da cercare",
                "desc": "I referti di laboratorio sono pieni di abbreviazioni e termini clinici. Quando quei termini sono in un'altra lingua, anche un dizionario non aiuta sempre — il vocabolario medico è molto specializzato.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Convenzioni di denominazione diverse",
                "desc": "Lo stesso esame del sangue può avere un nome, un'abbreviazione o un raggruppamento di pannello diverso a seconda del paese. Un «Blutbild» in Germania è un emocromo in Italia, ma la struttura può variare.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Unità e intervalli variano per regione",
                "desc": "La tua glicemia è in mg/dL o mmol/L? Gli intervalli di riferimento e i sistemi di misura differiscono tra i paesi, rendendo più difficile confrontare i valori visti in precedenza.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "I traduttori generici perdono le sfumature mediche",
                "desc": "Passare un referto di laboratorio attraverso un traduttore generico può produrre risultati inadeguati o fuorvianti. Il contesto medico richiede più di una traduzione parola per parola.",
            },
        ],
        "helps_title": "Come NoryaAI supera la barriera linguistica",
        "helps_sub": "NoryaAI non si limita a tradurre il tuo referto. Legge, struttura e spiega i tuoi risultati nella lingua che scegli.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Carica in qualsiasi lingua",
                "desc": "Il tuo referto di laboratorio può essere in tedesco, turco, francese, inglese o qualsiasi lingua supportata. Carica il PDF, una foto o incolla il testo.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "L'IA struttura i tuoi dati",
                "desc": "Valori, unità e intervalli di riferimento vengono estratti e organizzati in categorie chiare — indipendentemente dalla lingua originale.",
            },
            {
                "icon": "\U0001f310",
                "title": "Ricevi il rapporto nella tua lingua",
                "desc": "Scegli la lingua di output. Il tuo riepilogo strutturato, le spiegazioni e il punteggio di salute vengono generati nella lingua che preferisci leggere.",
            },
        ],
        "langs_title": "Lingue supportate per i rapporti",
        "langs_sub": "Carica i tuoi risultati di laboratorio in una di queste lingue e ricevi il tuo rapporto strutturato in quella che preferisci.",
        "langs": _LANGS_LIST,
        "who_title": "A chi è destinato",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Espatriati e immigrati",
                "desc": "Ti sei trasferito in un nuovo paese e hai fatto le analisi del sangue. Il referto è nella lingua locale, ma pensi e comprendi i temi di salute nella tua lingua madre.",
            },
            {
                "icon": "\U0001f393",
                "title": "Studenti internazionali",
                "desc": "Gli screening sanitari obbligatori all'università producono spesso referti nella lingua locale. Una spiegazione strutturata nella tua lingua ti aiuta a seguire i risultati.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Famiglie oltre i confini",
                "desc": "Il tuo genitore o partner ha ricevuto risultati di laboratorio in un altro paese. Carica il loro referto e genera un riepilogo nella lingua che entrambi capite.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Turisti medici e viaggiatori",
                "desc": "Hai fatto le analisi del sangue durante un viaggio o un soggiorno medico all'estero? Ottieni un riepilogo strutturato da condividere con il tuo medico a casa.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Visite mediche bilingui",
                "desc": "Comprendi il tuo medico in una lingua ma hai ricevuto il referto in un'altra. Un unico PDF strutturato nella tua lingua preferita può rendere l'appuntamento più fluido.",
            },
            {
                "icon": "\U0001f310",
                "title": "Confrontare risultati internazionali",
                "desc": "Se hai fatto analisi del sangue in diversi paesi, un formato strutturato unificato in una sola lingua facilita il monitoraggio dei tuoi valori nel tempo.",
            },
        ],
        "mid_cta_title": "Il tuo referto, la tua lingua",
        "mid_cta_sub": "Carica le tue analisi del sangue in qualsiasi lingua supportata e scegli come vuoi leggere i risultati.",
        "faqs": [
            {
                "q": "Posso caricare un referto di laboratorio in una lingua e ottenere i risultati in un'altra?",
                "a": "Sì. Puoi caricare un referto in qualsiasi lingua supportata — tedesco, turco, francese, inglese e altre — e scegliere una lingua diversa per il tuo output strutturato. I valori e gli intervalli di riferimento rimangono gli stessi; le spiegazioni vengono generate nella tua lingua preferita.",
            },
            {
                "q": "È un servizio di traduzione medica?",
                "a": "No. NoryaAI non fornisce traduzioni mediche certificate. Legge il tuo referto di laboratorio, struttura i dati e genera una spiegazione educativa nella lingua che scegli. Per scopi ufficiali o legali, consulta un traduttore medico certificato.",
            },
            {
                "q": "La lingua influisce sulla precisione dell'analisi?",
                "a": "No. L'analisi sottostante lavora con i valori numerici, le unità e gli intervalli di riferimento del tuo referto. La lingua del documento originale non influisce su come i valori vengono analizzati o strutturati.",
            },
            {
                "q": "Quali lingue sono supportate?",
                "a": "NoryaAI attualmente supporta inglese, tedesco, turco, francese, italiano, spagnolo, ebraico, hindi e arabo. Altre lingue vengono aggiunte nel tempo.",
            },
            {
                "q": "Posso condividere il rapporto con un medico che parla un'altra lingua?",
                "a": "Sì. Puoi generare lo stesso rapporto in più lingue se necessario. Il formato PDF strutturato è progettato per essere chiaro e utile indipendentemente dal background medico del lettore.",
            },
            {
                "q": "NoryaAI sostituisce il mio medico?",
                "a": "No. NoryaAI fornisce spiegazioni strutturate ed educative per aiutarti a comprendere i tuoi risultati di laboratorio. Non diagnostica, non tratta e non prescrive. Consulta sempre un professionista sanitario qualificato per le decisioni mediche.",
            },
        ],
        "cta_title": "Pronto a capire i tuoi risultati?",
        "cta_sub": "Carica le tue analisi del sangue in qualsiasi lingua e ottieni un rapporto chiaro e strutturato nella lingua che preferisci.",
        "cta_primary": "Carica e analizza ora",
        "cta_secondary": "Vedi i prezzi",
        "internal_links": [
            {"label": "Analizza", "path": "/analyze"},
            {"label": "Carica risultati", "path": "/it/upload-blood-test-results"},
            {"label": "Analizzatore sangue IA", "path": "/it/ai-blood-test-analyzer"},
            {"label": "Rapporti di esempio", "path": "/it/sample-blood-test-reports"},
            {"label": "Risultati spiegati", "path": "/it/blood-test-results-explained"},
            {"label": "Prezzi", "path": "/pricing"},
            {"label": "Blog", "path": "/it/blog"},
        ],
    }


def _he() -> dict:
    return {
        "meta_title": "הבן את תוצאות בדיקות הדם שלך בשפה שלך | NoryaAI",
        "meta_description": "קיבלת תוצאות מעבדה בשפה שאתה לא מבין לגמרי? העלה את בדיקת הדם שלך וקבל דוח מובנה וקל לקריאה בעברית, אנגלית, גרמנית, טורקית ו-5 שפות נוספות.",
        "hero_title": "הבן את תוצאות בדיקת הדם שלך — בשפה שלך",
        "hero_sub": "גר בחו״ל או קיבלת דוח מעבדה בשפה לא מוכרת? העלה את התוצאות שלך וקבל הסבר ברור ומובנה בשפה שהכי נוחה לך.",
        "cta_hero_primary": "נתח את בדיקת הדם שלי",
        "cta_hero_secondary": "צפה בדוחות לדוגמה",
        "barrier_title": "למה שפה מקשה על הבנת דוחות מעבדה",
        "barrier_sub": "בדיקת דם כבר קשה לקריאה. כשהדוח בשפה שאינה שפת האם שלך, האתגר מתרבה.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "מונחים רפואיים שקשה לחפש",
                "desc": "דוחות מעבדה מלאים בקיצורים ומונחים קליניים. כשהמונחים האלה בשפה אחרת, גם מילון לא תמיד עוזר — אוצר המילים הרפואי מאוד מתמחה.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "מוסכמות שמות שונות",
                "desc": "אותה בדיקת דם עשויה לשאת שם, קיצור או קיבוץ פאנל שונה בהתאם למדינה. ״Blutbild״ בגרמניה הוא ספירת דם בישראל, אבל המבנה יכול להיות שונה.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "יחידות וטווחים משתנים לפי אזור",
                "desc": "הגלוקוז שלך ב-mg/dL או mmol/L? טווחי ייחוס ומערכות מדידה שונים בין מדינות, מה שמקשה על השוואה לערכים שראית בעבר.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "מתרגמים כלליים מפספסים ניואנסים רפואיים",
                "desc": "להעביר דוח מעבדה דרך מתרגם כללי יכול לייצר תוצאות מביכות או מטעות. הקשר רפואי דורש יותר מתרגום מילה במילה.",
            },
        ],
        "helps_title": "איך NoryaAI מגשר על פער השפה",
        "helps_sub": "NoryaAI לא רק מתרגם את הדוח שלך. הוא קורא, מארגן ומסביר את התוצאות בשפה שתבחר.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "העלה בכל שפה",
                "desc": "דוח המעבדה שלך יכול להיות בגרמנית, טורקית, איטלקית, צרפתית או כל שפה נתמכת. העלה PDF, תמונה או הדבק את הטקסט.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "הבינה המלאכותית מארגנת את הנתונים",
                "desc": "ערכים, יחידות וטווחי ייחוס מופקים ומאורגנים בקטגוריות ברורות — ללא קשר לשפת המקור.",
            },
            {
                "icon": "\U0001f310",
                "title": "קבל את הדוח שלך בשפה שלך",
                "desc": "בחר את שפת הפלט. הסיכום המובנה, ההסברים וציון הבריאות נוצרים בשפה שהכי נוח לך לקרוא.",
            },
        ],
        "langs_title": "שפות דוח נתמכות",
        "langs_sub": "העלה את תוצאות המעבדה שלך באחת מהשפות הבאות וקבל את הדוח המובנה בשפה שתעדיף.",
        "langs": _LANGS_LIST,
        "who_title": "למי זה מיועד",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "עולים ומהגרים",
                "desc": "עברת למדינה חדשה ועשית בדיקת דם. הדוח בשפה המקומית, אבל אתה חושב ומבין נושאי בריאות בשפת האם שלך.",
            },
            {
                "icon": "\U0001f393",
                "title": "סטודנטים בינלאומיים",
                "desc": "בדיקות בריאות חובה באוניברסיטה מייצרות לעיתים קרובות דוחות בשפה המקומית. הסבר מובנה בשפה שלך עוזר לך לעקוב.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "משפחות מעבר לגבולות",
                "desc": "ההורה או בן/בת הזוג שלך קיבלו תוצאות מעבדה במדינה אחרת. העלה את הדוח וצור סיכום בשפה ששניכם מבינים.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "תיירים רפואיים ומטיילים",
                "desc": "עשית בדיקת דם בזמן טיול או נסיעה רפואית לחו״ל? קבל סיכום מובנה שאפשר לשתף עם הרופא שלך בבית.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "ביקורי רופא דו-לשוניים",
                "desc": "אתה מבין את הרופא בשפה אחת אבל קיבלת את דוח המעבדה בשפה אחרת. PDF מובנה אחד בשפה המועדפת עליך יכול להפוך את הפגישה לחלקה יותר.",
            },
            {
                "icon": "\U0001f310",
                "title": "השוואת תוצאות בינלאומיות",
                "desc": "אם עשית בדיקות דם במדינות שונות, פורמט מובנה אחיד בשפה אחת מקל על מעקב אחר הערכים שלך לאורך זמן.",
            },
        ],
        "mid_cta_title": "הדוח שלך, השפה שלך",
        "mid_cta_sub": "העלה את בדיקת הדם שלך בכל שפה נתמכת ובחר איך אתה רוצה לקרוא את התוצאות.",
        "faqs": [
            {
                "q": "אפשר להעלות דוח מעבדה בשפה אחת ולקבל תוצאות בשפה אחרת?",
                "a": "כן. אפשר להעלות דוח בכל שפה נתמכת — גרמנית, טורקית, צרפתית, איטלקית ועוד — ולבחור שפה אחרת לפלט המובנה. הערכים וטווחי הייחוס נשארים זהים; ההסברים נוצרים בשפה המועדפת עליך.",
            },
            {
                "q": "זה שירות תרגום רפואי?",
                "a": "לא. NoryaAI לא מספק תרגומים רפואיים מוסמכים. הוא קורא את דוח המעבדה, מארגן את הנתונים ומייצר הסבר לימודי בשפה שתבחר. לצרכים רשמיים או משפטיים, פנה למתרגם רפואי מוסמך.",
            },
            {
                "q": "האם השפה משפיעה על דיוק הניתוח?",
                "a": "לא. הניתוח הבסיסי עובד עם הערכים המספריים, היחידות וטווחי הייחוס בדוח שלך. שפת המסמך המקורי לא משפיעה על אופן הניתוח או המבנה של הערכים.",
            },
            {
                "q": "אילו שפות נתמכות?",
                "a": "NoryaAI תומך כרגע באנגלית, גרמנית, טורקית, צרפתית, איטלקית, ספרדית, עברית, הינדי וערבית. שפות נוספות מתווספות עם הזמן.",
            },
            {
                "q": "אפשר לשתף את הדוח עם רופא שמדבר שפה אחרת?",
                "a": "כן. אפשר ליצור את אותו דוח במספר שפות לפי הצורך. פורמט ה-PDF המובנה מתוכנן להיות ברור ושימושי ללא קשר לרקע הרפואי של הקורא.",
            },
            {
                "q": "האם NoryaAI מחליף את הרופא שלי?",
                "a": "לא. NoryaAI מספק הסברים מובנים ולימודיים כדי לעזור לך להבין את תוצאות המעבדה. הוא לא מאבחן, לא מטפל ולא רושם תרופות. תמיד התייעץ עם איש מקצוע רפואי מוסמך לגבי החלטות רפואיות.",
            },
        ],
        "cta_title": "מוכן להבין את התוצאות שלך?",
        "cta_sub": "העלה את בדיקת הדם שלך בכל שפה וקבל דוח ברור ומובנה בשפה שאתה מעדיף.",
        "cta_primary": "העלה ונתח עכשיו",
        "cta_secondary": "צפה במחירים",
        "internal_links": [
            {"label": "ניתוח", "path": "/analyze"},
            {"label": "העלאת תוצאות", "path": "/he/upload-blood-test-results"},
            {"label": "מנתח בדיקות דם AI", "path": "/he/ai-blood-test-analyzer"},
            {"label": "דוחות לדוגמה", "path": "/he/sample-blood-test-reports"},
            {"label": "תוצאות בדיקות דם מוסברות", "path": "/he/blood-test-results-explained"},
            {"label": "מחירים", "path": "/pricing"},
            {"label": "בלוג", "path": "/he/blog"},
        ],
    }


def _hi() -> dict:
    return {
        "meta_title": "अपनी भाषा में रक्त परीक्षण के परिणाम समझें | NoryaAI",
        "meta_description": "क्या आपको ऐसी भाषा में लैब रिपोर्ट मिली जो आप पूरी तरह नहीं समझते? अपना रक्त परीक्षण अपलोड करें और हिंदी, अंग्रेज़ी, जर्मन, तुर्की और 5 अन्य भाषाओं में एक संरचित, पढ़ने में आसान रिपोर्ट प्राप्त करें।",
        "hero_title": "अपने रक्त परीक्षण के परिणाम समझें — अपनी भाषा में",
        "hero_sub": "विदेश में रह रहे हैं या अपरिचित भाषा में लैब रिपोर्ट मिली? अपने परिणाम अपलोड करें और सबसे सहज भाषा में स्पष्ट, संरचित व्याख्या प्राप्त करें।",
        "cta_hero_primary": "मेरा रक्त परीक्षण विश्लेषित करें",
        "cta_hero_secondary": "नमूना रिपोर्ट देखें",
        "barrier_title": "भाषा क्यों लैब रिपोर्ट को समझना कठिन बनाती है",
        "barrier_sub": "रक्त परीक्षण पहले से ही पढ़ना कठिन है। जब रिपोर्ट आपकी मातृभाषा में नहीं होती, तो चुनौती कई गुना बढ़ जाती है।",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "चिकित्सा शब्द जो आसानी से नहीं खोजे जा सकते",
                "desc": "लैब रिपोर्ट संक्षिप्ताक्षरों और नैदानिक शब्दों से भरी होती हैं। जब ये शब्द दूसरी भाषा में हों, तो शब्दकोश भी हमेशा मदद नहीं करता — चिकित्सा शब्दावली बहुत विशिष्ट होती है।",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "अलग-अलग नामकरण प्रथाएँ",
                "desc": "एक ही रक्त परीक्षण का देश के अनुसार अलग नाम, संक्षिप्ताक्षर या पैनल समूह हो सकता है। जर्मनी में 'Blutbild' अमेरिका में CBC है, लेकिन संरचना भिन्न हो सकती है।",
            },
            {
                "icon": "\U0001f4cf",
                "title": "इकाइयाँ और रेंज क्षेत्र के अनुसार बदलती हैं",
                "desc": "आपका ग्लूकोज mg/dL में है या mmol/L में? संदर्भ रेंज और माप प्रणालियाँ देशों के बीच भिन्न होती हैं, जिससे पहले देखे गए मूल्यों से तुलना करना कठिन हो जाता है।",
            },
            {
                "icon": "\U0001f6ab",
                "title": "सामान्य अनुवादक चिकित्सा सूक्ष्मता चूक जाते हैं",
                "desc": "लैब रिपोर्ट को सामान्य अनुवादक से गुज़ारने पर अटपटे या भ्रामक परिणाम मिल सकते हैं। चिकित्सा संदर्भ में शब्द-दर-शब्द अनुवाद से अधिक की आवश्यकता होती है।",
            },
        ],
        "helps_title": "NoryaAI भाषा की बाधा कैसे दूर करता है",
        "helps_sub": "NoryaAI सिर्फ आपकी रिपोर्ट का अनुवाद नहीं करता। यह आपके परिणामों को पढ़ता है, संरचित करता है और आपकी चुनी हुई भाषा में समझाता है।",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "किसी भी भाषा में अपलोड करें",
                "desc": "आपकी लैब रिपोर्ट जर्मन, तुर्की, इतालवी, फ्रेंच या किसी भी समर्थित भाषा में हो सकती है। PDF, फोटो अपलोड करें या टेक्स्ट पेस्ट करें।",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI आपके डेटा को संरचित करता है",
                "desc": "मूल्य, इकाइयाँ और संदर्भ रेंज निकाले जाते हैं और मूल भाषा की परवाह किए बिना स्पष्ट श्रेणियों में व्यवस्थित किए जाते हैं।",
            },
            {
                "icon": "\U0001f310",
                "title": "अपनी भाषा में रिपोर्ट प्राप्त करें",
                "desc": "आउटपुट भाषा चुनें। आपका संरचित सारांश, व्याख्याएँ और स्वास्थ्य स्कोर उस भाषा में तैयार किए जाते हैं जो आप सबसे सहजता से पढ़ते हैं।",
            },
        ],
        "langs_title": "समर्थित रिपोर्ट भाषाएँ",
        "langs_sub": "इनमें से किसी भी भाषा में अपने लैब परिणाम अपलोड करें और अपनी पसंदीदा भाषा में संरचित रिपोर्ट प्राप्त करें।",
        "langs": _LANGS_LIST,
        "who_title": "यह किसके लिए है",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "प्रवासी और आप्रवासी",
                "desc": "आप नए देश में आए और रक्त परीक्षण कराया। रिपोर्ट स्थानीय भाषा में है, लेकिन आप स्वास्थ्य विषयों को अपनी मातृभाषा में सोचते और समझते हैं।",
            },
            {
                "icon": "\U0001f393",
                "title": "अंतर्राष्ट्रीय छात्र",
                "desc": "विश्वविद्यालय में अनिवार्य स्वास्थ्य जांच अक्सर स्थानीय भाषा में रिपोर्ट तैयार करती है। अपनी भाषा में संरचित व्याख्या आपको फॉलो-अप में मदद करती है।",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "सीमा पार परिवार",
                "desc": "आपके माता-पिता या साथी को दूसरे देश में लैब परिणाम मिले। उनकी रिपोर्ट अपलोड करें और दोनों की समझ में आने वाली भाषा में सारांश तैयार करें।",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "मेडिकल टूरिस्ट और यात्री",
                "desc": "यात्रा के दौरान या विदेश में मेडिकल ट्रिप पर रक्त परीक्षण कराया? घर पर अपने डॉक्टर के साथ साझा करने के लिए संरचित सारांश प्राप्त करें।",
            },
            {
                "icon": "\U0001fa7a",
                "title": "द्विभाषी डॉक्टर विज़िट",
                "desc": "आप डॉक्टर को एक भाषा में समझते हैं लेकिन लैब रिपोर्ट दूसरी भाषा में मिली। आपकी पसंदीदा भाषा में एक संरचित PDF अपॉइंटमेंट को आसान बना सकता है।",
            },
            {
                "icon": "\U0001f310",
                "title": "अंतर्राष्ट्रीय परिणामों की तुलना",
                "desc": "यदि आपने विभिन्न देशों में रक्त परीक्षण कराया है, तो एक भाषा में एकीकृत संरचित प्रारूप समय के साथ आपके मूल्यों को ट्रैक करना आसान बनाता है।",
            },
        ],
        "mid_cta_title": "आपकी लैब रिपोर्ट, आपकी भाषा",
        "mid_cta_sub": "अपना रक्त परीक्षण किसी भी समर्थित भाषा में अपलोड करें और चुनें कि आप परिणाम कैसे पढ़ना चाहते हैं।",
        "faqs": [
            {
                "q": "क्या मैं एक भाषा में लैब रिपोर्ट अपलोड करके दूसरी भाषा में परिणाम प्राप्त कर सकता हूँ?",
                "a": "हाँ। आप किसी भी समर्थित भाषा में रिपोर्ट अपलोड कर सकते हैं — जर्मन, तुर्की, फ्रेंच, इतालवी और अन्य — और अपने संरचित आउटपुट के लिए अलग भाषा चुन सकते हैं। मूल्य और संदर्भ रेंज समान रहते हैं; व्याख्याएँ आपकी पसंदीदा भाषा में तैयार की जाती हैं।",
            },
            {
                "q": "क्या यह चिकित्सा अनुवाद सेवा है?",
                "a": "नहीं। NoryaAI प्रमाणित चिकित्सा अनुवाद प्रदान नहीं करता। यह आपकी लैब रिपोर्ट पढ़ता है, डेटा को संरचित करता है और आपकी चुनी हुई भाषा में शैक्षिक व्याख्या तैयार करता है। आधिकारिक या कानूनी उद्देश्यों के लिए, प्रमाणित चिकित्सा अनुवादक से परामर्श करें।",
            },
            {
                "q": "क्या भाषा विश्लेषण की सटीकता को प्रभावित करती है?",
                "a": "नहीं। अंतर्निहित विश्लेषण आपकी रिपोर्ट में संख्यात्मक मूल्यों, इकाइयों और संदर्भ रेंज के साथ काम करता है। मूल दस्तावेज़ की भाषा मूल्यों के विश्लेषण या संरचना को प्रभावित नहीं करती।",
            },
            {
                "q": "कौन सी भाषाएँ समर्थित हैं?",
                "a": "NoryaAI वर्तमान में अंग्रेज़ी, जर्मन, तुर्की, फ्रेंच, इतालवी, स्पेनिश, हिब्रू, हिंदी और अरबी का समर्थन करता है। समय के साथ और भाषाएँ जोड़ी जा रही हैं।",
            },
            {
                "q": "क्या मैं अलग भाषा बोलने वाले डॉक्टर के साथ रिपोर्ट साझा कर सकता हूँ?",
                "a": "हाँ। ज़रूरत पड़ने पर आप एक ही रिपोर्ट कई भाषाओं में तैयार कर सकते हैं। संरचित PDF प्रारूप पाठक की चिकित्सा पृष्ठभूमि की परवाह किए बिना स्पष्ट और उपयोगी होने के लिए डिज़ाइन किया गया है।",
            },
            {
                "q": "क्या NoryaAI मेरे डॉक्टर का विकल्प है?",
                "a": "नहीं। NoryaAI आपके लैब परिणामों को समझने में मदद के लिए संरचित, शैक्षिक व्याख्याएँ प्रदान करता है। यह निदान, उपचार या नुस्खे नहीं देता। चिकित्सा निर्णयों के लिए हमेशा योग्य स्वास्थ्य पेशेवर से परामर्श करें।",
            },
        ],
        "cta_title": "अपने परिणाम समझने के लिए तैयार हैं?",
        "cta_sub": "किसी भी भाषा में अपना रक्त परीक्षण अपलोड करें और अपनी पसंदीदा भाषा में स्पष्ट, संरचित रिपोर्ट प्राप्त करें।",
        "cta_primary": "अपलोड करें और विश्लेषित करें",
        "cta_secondary": "मूल्य देखें",
        "internal_links": [
            {"label": "विश्लेषण", "path": "/analyze"},
            {"label": "परिणाम अपलोड करें", "path": "/hi/upload-blood-test-results"},
            {"label": "AI रक्त परीक्षण विश्लेषक", "path": "/hi/ai-blood-test-analyzer"},
            {"label": "नमूना रिपोर्ट", "path": "/hi/sample-blood-test-reports"},
            {"label": "रक्त परीक्षण परिणाम व्याख्या", "path": "/hi/blood-test-results-explained"},
            {"label": "मूल्य", "path": "/pricing"},
            {"label": "ब्लॉग", "path": "/hi/blog"},
        ],
    }


def _ar() -> dict:
    return {
        "meta_title": "افهم نتائج تحليل الدم بلغتك | NoryaAI",
        "meta_description": "حصلت على نتائج مختبر بلغة لا تفهمها تمامًا؟ ارفع تحليل الدم واحصل على تقرير منظّم وسهل القراءة بالعربية والإنجليزية والألمانية والتركية و5 لغات أخرى.",
        "hero_title": "افهم نتائج تحليل الدم — بلغتك",
        "hero_sub": "تعيش في الخارج أو حصلت على تقرير مختبر بلغة غير مألوفة؟ ارفع نتائجك واحصل على شرح واضح ومنظّم باللغة الأكثر راحة لك.",
        "cta_hero_primary": "حلّل تحليل الدم الخاص بي",
        "cta_hero_secondary": "شاهد تقارير نموذجية",
        "barrier_title": "لماذا تجعل اللغة تقارير المختبر أصعب في الفهم",
        "barrier_sub": "تحليل الدم صعب القراءة بالفعل. عندما يكون التقرير بلغة ليست لغتك الأم، يتضاعف التحدي.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "مصطلحات طبية يصعب البحث عنها",
                "desc": "تقارير المختبر مليئة بالاختصارات والمصطلحات السريرية. عندما تكون هذه المصطلحات بلغة أخرى، حتى القاموس لا يساعد دائمًا — المفردات الطبية متخصصة للغاية.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "اصطلاحات تسمية مختلفة",
                "desc": "نفس تحليل الدم قد يحمل اسمًا أو اختصارًا أو تجميع لوحة مختلفًا حسب البلد. «Blutbild» في ألمانيا هو صورة دم كاملة في بلدان أخرى، لكن البنية قد تختلف.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "الوحدات والنطاقات تختلف حسب المنطقة",
                "desc": "هل الجلوكوز بوحدة mg/dL أم mmol/L؟ النطاقات المرجعية وأنظمة القياس تختلف بين الدول، مما يصعّب مقارنة القيم التي رأيتها سابقًا.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "المترجمات العامة تفتقد الدقة الطبية",
                "desc": "تمرير تقرير مختبر عبر مترجم عام قد ينتج نتائج غريبة أو مضللة. السياق الطبي يتطلب أكثر من ترجمة حرفية.",
            },
        ],
        "helps_title": "كيف يتجاوز NoryaAI حاجز اللغة",
        "helps_sub": "NoryaAI لا يترجم تقريرك فحسب. بل يقرأ نتائجك وينظّمها ويشرحها باللغة التي تختارها.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "ارفع بأي لغة",
                "desc": "تقرير المختبر يمكن أن يكون بالألمانية أو التركية أو الإيطالية أو الفرنسية أو أي لغة مدعومة. ارفع ملف PDF أو صورة أو الصق النص.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "الذكاء الاصطناعي ينظّم بياناتك",
                "desc": "يتم استخراج القيم والوحدات والنطاقات المرجعية وتنظيمها في فئات واضحة — بغض النظر عن اللغة الأصلية.",
            },
            {
                "icon": "\U0001f310",
                "title": "احصل على تقريرك بلغتك",
                "desc": "اختر لغة الإخراج. ملخصك المنظّم والشروحات ونقاط الصحة تُنشأ باللغة الأكثر راحة لك في القراءة.",
            },
        ],
        "langs_title": "لغات التقارير المدعومة",
        "langs_sub": "ارفع نتائج المختبر بأي من هذه اللغات واحصل على تقريرك المنظّم باللغة التي تفضلها.",
        "langs": _LANGS_LIST,
        "who_title": "لمن هذا",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "المغتربون والمهاجرون",
                "desc": "انتقلت إلى بلد جديد وأجريت تحليل دم. التقرير باللغة المحلية، لكنك تفكر وتفهم المواضيع الصحية بلغتك الأم.",
            },
            {
                "icon": "\U0001f393",
                "title": "الطلاب الدوليون",
                "desc": "الفحوصات الصحية الإلزامية في الجامعة غالبًا تنتج تقارير باللغة المحلية. شرح منظّم بلغتك يساعدك على المتابعة.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "عائلات عبر الحدود",
                "desc": "أحد والديك أو شريكك حصل على نتائج مختبر في بلد آخر. ارفع تقريرهم وأنشئ ملخصًا باللغة التي يفهمها كلاكما.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "السياح الطبيون والمسافرون",
                "desc": "أجريت تحليل دم أثناء السفر أو رحلة طبية للخارج؟ احصل على ملخص منظّم يمكنك مشاركته مع طبيبك في بلدك.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "زيارات طبية ثنائية اللغة",
                "desc": "تفهم طبيبك بلغة لكن تقرير المختبر جاء بلغة أخرى. ملف PDF منظّم واحد بلغتك المفضلة يمكن أن يجعل الموعد أكثر سلاسة.",
            },
            {
                "icon": "\U0001f310",
                "title": "مقارنة نتائج دولية",
                "desc": "إذا أجريت تحاليل دم في بلدان مختلفة، فإن تنسيقًا منظّمًا موحّدًا بلغة واحدة يسهّل تتبع قيمك عبر الوقت.",
            },
        ],
        "mid_cta_title": "تقريرك، لغتك",
        "mid_cta_sub": "ارفع تحليل الدم بأي لغة مدعومة واختر كيف تريد قراءة النتائج.",
        "faqs": [
            {
                "q": "هل يمكنني رفع تقرير مختبر بلغة والحصول على النتائج بلغة أخرى؟",
                "a": "نعم. يمكنك رفع تقرير بأي لغة مدعومة — الألمانية والتركية والفرنسية والإيطالية وغيرها — واختيار لغة مختلفة لمخرجاتك المنظّمة. القيم والنطاقات المرجعية تبقى كما هي؛ الشروحات تُنشأ بلغتك المفضلة.",
            },
            {
                "q": "هل هذه خدمة ترجمة طبية؟",
                "a": "لا. NoryaAI لا يقدم ترجمات طبية معتمدة. يقرأ تقرير المختبر وينظّم البيانات ويُنشئ شرحًا تعليميًا باللغة التي تختارها. للأغراض الرسمية أو القانونية، استشر مترجمًا طبيًا معتمدًا.",
            },
            {
                "q": "هل تؤثر اللغة على دقة التحليل؟",
                "a": "لا. التحليل الأساسي يعمل مع القيم الرقمية والوحدات والنطاقات المرجعية في تقريرك. لغة المستند الأصلي لا تؤثر على كيفية تحليل القيم أو تنظيمها.",
            },
            {
                "q": "ما اللغات المدعومة؟",
                "a": "NoryaAI يدعم حاليًا الإنجليزية والألمانية والتركية والفرنسية والإيطالية والإسبانية والعبرية والهندية والعربية. يتم إضافة المزيد من اللغات مع الوقت.",
            },
            {
                "q": "هل يمكنني مشاركة التقرير مع طبيب يتحدث لغة أخرى؟",
                "a": "نعم. يمكنك إنشاء نفس التقرير بعدة لغات عند الحاجة. تنسيق PDF المنظّم مصمم ليكون واضحًا ومفيدًا بغض النظر عن الخلفية الطبية للقارئ.",
            },
            {
                "q": "هل NoryaAI بديل عن طبيبي؟",
                "a": "لا. NoryaAI يقدم شروحات منظّمة وتعليمية لمساعدتك على فهم نتائج المختبر. لا يشخّص ولا يعالج ولا يصف أدوية. استشر دائمًا متخصصًا صحيًا مؤهلًا للقرارات الطبية.",
            },
        ],
        "cta_title": "مستعد لفهم نتائجك؟",
        "cta_sub": "ارفع تحليل الدم بأي لغة واحصل على تقرير واضح ومنظّم باللغة التي تفضلها.",
        "cta_primary": "ارفع وحلّل الآن",
        "cta_secondary": "عرض الأسعار",
        "internal_links": [
            {"label": "تحليل", "path": "/analyze"},
            {"label": "رفع النتائج", "path": "/ar/upload-blood-test-results"},
            {"label": "محلل فحص الدم بالذكاء الاصطناعي", "path": "/ar/ai-blood-test-analyzer"},
            {"label": "تقارير نموذجية", "path": "/ar/sample-blood-test-reports"},
            {"label": "شرح نتائج تحليل الدم", "path": "/ar/blood-test-results-explained"},
            {"label": "الأسعار", "path": "/pricing"},
            {"label": "المدونة", "path": "/ar/blog"},
        ],
    }


_CONTENT: dict[str, dict] = {
    "en": _en(),
    "tr": _tr(),
    "de": _de(),
    "es": _es(),
    "fr": _fr(),
    "it": _it(),
    "he": _he(),
    "hi": _hi(),
    "ar": _ar(),
}


def get_multilingual_landing_content(lang: str) -> dict:
    return _CONTENT.get(lang, _CONTENT["en"])


def get_multilingual_landing_slug(lang: str) -> str:
    return MULTILINGUAL_SLUGS.get(lang, MULTILINGUAL_SLUGS["en"])
