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


def _internal_links(lang: str) -> list[dict[str, str]]:
    prefix = f"/{lang}"
    return [
        {"label": "Analyze", "path": "/analyze"},
        {"label": "Upload Results", "path": f"{prefix}/upload-blood-test-results"},
        {"label": "AI Blood Test Analyzer", "path": f"{prefix}/ai-blood-test-analyzer"},
        {"label": "Sample Reports", "path": f"{prefix}/sample-blood-test-reports"},
        {"label": "Blood Test Results Explained", "path": f"{prefix}/blood-test-results-explained"},
        {"label": "Pricing", "path": "/pricing"},
        {"label": "Blog", "path": f"{prefix}/blog"},
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
        "internal_links": _internal_links("en"),
    }


def _tr() -> dict:
    return {
        "meta_title": "Kan Tahlili Sonuçlarınızı Kendi Dilinizde Anlayın | NoryaAI",
        "meta_description": "Laboratuvar sonuçlarınız tam anlayamadığınız bir dilde mi? Kan tahlilinizi yükleyin ve Türkçe, İngilizce, Almanca, Fransızca ve 6 farklı dilde yapılandırılmış, kolay okunur bir rapor alın.",
        "hero_title": "Kan Tahlili Sonuçlarınızı Kendi Dilinizde Anlayın",
        "hero_sub": "Yurt dışında mı yaşıyorsunuz ya da tanımadığınız bir dilde laboratuvar raporu mu aldınız? Sonuçlarınızı yükleyin ve en rahat anladığınız dilde net, yapılandırılmış bir açıklama alın.",
        "cta_hero_primary": "Kan tahlilimi analiz et",
        "cta_hero_secondary": "Örnek raporları gör",
        "barrier_title": "Dil neden laboratuvar raporlarını anlamayı zorlaştırır",
        "barrier_sub": "Kan tahlili zaten okunması zor bir belgedir. Rapor ana dilinizde değilse bu zorluk katlanarak artar.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Kolayca araştırılamayan tıbbi terimler",
                "desc": "Laboratuvar raporları kısaltmalar ve klinik terimlerle doludur. Bu terimler başka bir dildeyse sözlük bile her zaman yardımcı olmaz — tıbbi terminoloji uzmanlık gerektirir.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Farklı adlandırma kuralları",
                "desc": "Aynı kan testi ülkeden ülkeye farklı isim, kısaltma veya panel gruplaması taşıyabilir. Almanya'daki \"Blutbild\" ABD'deki CBC'ye karşılık gelir, ancak yapısı farklılık gösterebilir.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Birimler ve referans aralıkları bölgeye göre değişir",
                "desc": "Glukozunuz mg/dL mi yoksa mmol/L mi? Referans aralıkları ve ölçüm sistemleri ülkeler arasında farklılık gösterir, bu da daha önce gördüğünüz değerlerle karşılaştırmayı zorlaştırır.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Genel çevirmenler tıbbi nüansları kaçırır",
                "desc": "Bir laboratuvar raporunu genel bir çeviri aracından geçirmek garip veya yanıltıcı sonuçlar üretebilir. Tıbbi bağlam, kelime kelime çeviriden fazlasını gerektirir.",
            },
        ],
        "helps_title": "NoryaAI dil bariyerini nasıl aşar",
        "helps_sub": "NoryaAI raporunuzu sadece çevirmez. Sonuçlarınızı okur, yapılandırır ve seçtiğiniz dilde açıklar.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Herhangi bir dilde yükleyin",
                "desc": "Laboratuvar raporunuz Almanca, İngilizce, İtalyanca, Fransızca veya desteklenen herhangi bir dilde olabilir. PDF, fotoğraf yükleyin veya metni yapıştırın.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "Yapay zekâ verilerinizi yapılandırır",
                "desc": "Değerler, birimler ve referans aralıkları orijinal dilden bağımsız olarak çıkarılır ve net kategorilere ayrılır.",
            },
            {
                "icon": "\U0001f310",
                "title": "Raporunuzu kendi dilinizde alın",
                "desc": "Çıktı dilini seçin. Yapılandırılmış özetiniz, açıklamalarınız ve sağlık puanınız en rahat okuduğunuz dilde oluşturulur.",
            },
        ],
        "langs_title": "Desteklenen rapor dilleri",
        "langs_sub": "Laboratuvar sonuçlarınızı bu dillerden herhangi birinde yükleyin ve yapılandırılmış raporunuzu tercih ettiğiniz dilde alın.",
        "langs": _LANGS_LIST,
        "who_title": "Bu kimler için",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Gurbetçiler ve göçmenler",
                "desc": "Yeni bir ülkeye taşındınız ve kan tahlili yaptırdınız. Rapor yerel dilde ama sağlık konularını ana dilinizde düşünüyor ve anlıyorsunuz.",
            },
            {
                "icon": "\U0001f393",
                "title": "Uluslararası öğrenciler",
                "desc": "Üniversitedeki zorunlu sağlık taramaları genellikle yerel dilde raporlar üretir. Kendi dilinizdeki yapılandırılmış bir açıklama takibinizi kolaylaştırır.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Sınır ötesi aileler",
                "desc": "Ebeveynleriniz veya eşiniz başka bir ülkede laboratuvar sonuçları aldı. Raporlarını yükleyin ve ikinizin de anladığı dilde bir özet oluşturun.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Sağlık turistleri ve gezginler",
                "desc": "Seyahat sırasında veya yurt dışında bir sağlık gezisinde kan tahlili mi yaptırdınız? Kendi ülkenizdeki doktorunuzla paylaşabileceğiniz yapılandırılmış bir özet alın.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "İki dilli doktor ziyaretleri",
                "desc": "Doktorunuzu bir dilde anlıyorsunuz ama laboratuvar raporunuzu başka bir dilde aldınız. Tercih ettiğiniz dildeki tek bir yapılandırılmış PDF randevunuzu kolaylaştırabilir.",
            },
            {
                "icon": "\U0001f310",
                "title": "Uluslararası sonuçları karşılaştıranlar",
                "desc": "Farklı ülkelerde kan tahlili yaptırdıysanız, tek bir dilde birleştirilmiş yapılandırılmış format değerlerinizi zaman içinde takip etmenizi kolaylaştırır.",
            },
        ],
        "mid_cta_title": "Laboratuvar raporunuz, kendi dilinizde",
        "mid_cta_sub": "Kan tahlilinizi desteklenen herhangi bir dilde yükleyin ve sonuçlarınızı nasıl okumak istediğinizi seçin.",
        "faqs": [
            {
                "q": "Bir dilde laboratuvar raporu yükleyip sonuçlarımı başka bir dilde alabilir miyim?",
                "a": "Evet. Raporunuzu desteklenen herhangi bir dilde — Almanca, İngilizce, Fransızca, İtalyanca ve daha fazlası — yükleyebilir ve yapılandırılmış çıktınız için farklı bir dil seçebilirsiniz. Değerler ve referans aralıkları aynı kalır; açıklamalar tercih ettiğiniz dilde oluşturulur.",
            },
            {
                "q": "Bu bir tıbbi çeviri hizmeti midir?",
                "a": "Hayır. NoryaAI sertifikalı tıbbi çeviri sağlamaz. Laboratuvar raporunuzu okur, verileri yapılandırır ve seçtiğiniz dilde eğitici bir açıklama oluşturur. Resmi veya yasal amaçlar için sertifikalı bir tıbbi çevirmene danışın.",
            },
            {
                "q": "Dil, analizin doğruluğunu etkiler mi?",
                "a": "Hayır. Temel analiz, raporunuzdaki sayısal değerler, birimler ve referans aralıklarıyla çalışır. Orijinal belgenin dili, değerlerin nasıl ayrıştırıldığını veya yapılandırıldığını etkilemez.",
            },
            {
                "q": "Hangi diller destekleniyor?",
                "a": "NoryaAI şu anda İngilizce, Almanca, Türkçe, Fransızca, İtalyanca, İspanyolca, İbranice, Hintçe ve Arapça desteklemektedir. Zamanla daha fazla dil eklenmektedir.",
            },
            {
                "q": "Raporu farklı bir dil konuşan bir doktorla paylaşabilir miyim?",
                "a": "Evet. Gerekirse aynı raporu birden fazla dilde oluşturabilirsiniz. Yapılandırılmış PDF formatı, okuyanın tıbbi geçmişinden bağımsız olarak net ve kullanışlı olacak şekilde tasarlanmıştır.",
            },
            {
                "q": "NoryaAI doktorumun yerini alır mı?",
                "a": "Hayır. NoryaAI, laboratuvar sonuçlarınızı anlamanıza yardımcı olmak için yapılandırılmış, eğitici açıklamalar sunar. Teşhis koymaz, tedavi uygulamaz veya reçete yazmaz. Tıbbi kararlar için her zaman nitelikli bir sağlık uzmanına danışın.",
            },
        ],
        "cta_title": "Sonuçlarınızı anlamaya hazır mısınız?",
        "cta_sub": "Kan tahlilinizi herhangi bir dilde yükleyin ve tercih ettiğiniz dilde net, yapılandırılmış bir rapor alın.",
        "cta_primary": "Yükle ve şimdi analiz et",
        "cta_secondary": "Fiyatlandırmayı gör",
        "internal_links": _internal_links("tr"),
    }


def _de() -> dict:
    return {
        "meta_title": "Blutwerte in Ihrer Sprache verstehen | NoryaAI",
        "meta_description": "Haben Sie Laborergebnisse in einer Sprache erhalten, die Sie nicht vollständig verstehen? Laden Sie Ihre Blutuntersuchung hoch und erhalten Sie einen strukturierten, leicht lesbaren Bericht auf Deutsch, Englisch, Türkisch, Französisch und in 6 weiteren Sprachen.",
        "hero_title": "Verstehen Sie Ihre Blutwerte \u2014 in Ihrer Sprache",
        "hero_sub": "Im Ausland leben oder einen Laborbericht in einer fremden Sprache erhalten? Laden Sie Ihre Ergebnisse hoch und erhalten Sie eine klare, strukturierte Erklärung in der Sprache, die Sie am besten verstehen.",
        "cta_hero_primary": "Meine Blutwerte analysieren",
        "cta_hero_secondary": "Beispielberichte ansehen",
        "barrier_title": "Warum Sprache Laborberichte schwerer verständlich macht",
        "barrier_sub": "Ein Blutbild ist bereits schwer zu lesen. Wenn der Bericht in einer Sprache ist, die nicht Ihre Muttersprache ist, vervielfacht sich die Herausforderung.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Medizinische Begriffe, die schwer nachzuschlagen sind",
                "desc": "Laborberichte sind voller Abkürzungen und klinischer Begriffe. Wenn diese in einer anderen Sprache sind, hilft selbst ein Wörterbuch nicht immer — medizinisches Vokabular ist hochspezialisiert.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Unterschiedliche Namenskonventionen",
                "desc": "Derselbe Bluttest kann je nach Land einen anderen Namen, eine andere Abk\u00fcrzung oder Panelgruppierung haben. Ein \u201eBlutbild\u201c in Deutschland ist ein CBC in den USA, aber die Struktur kann sich unterscheiden.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Einheiten und Referenzbereiche variieren je nach Region",
                "desc": "Ist Ihr Glukosewert in mg/dL oder mmol/L? Referenzbereiche und Messsysteme unterscheiden sich zwischen Ländern, was den Vergleich mit zuvor gesehenen Werten erschwert.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Allgemeine Übersetzer übersehen medizinische Nuancen",
                "desc": "Einen Laborbericht durch einen allgemeinen Übersetzer laufen zu lassen, kann ungenaue oder irreführende Ergebnisse liefern. Medizinischer Kontext erfordert mehr als eine wörtliche Übersetzung.",
            },
        ],
        "helps_title": "Wie NoryaAI die Sprachbarriere überbrückt",
        "helps_sub": "NoryaAI übersetzt Ihren Bericht nicht nur. Es liest, strukturiert und erklärt Ihre Ergebnisse in der von Ihnen gewählten Sprache.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "In jeder Sprache hochladen",
                "desc": "Ihr Laborbericht kann auf Englisch, Türkisch, Italienisch, Französisch oder einer anderen unterstützten Sprache sein. Laden Sie das PDF, ein Foto hoch oder fügen Sie den Text ein.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "KI strukturiert Ihre Daten",
                "desc": "Werte, Einheiten und Referenzbereiche werden unabhängig von der Originalsprache extrahiert und in klare Kategorien geordnet.",
            },
            {
                "icon": "\U0001f310",
                "title": "Bericht in Ihrer Sprache erhalten",
                "desc": "Wählen Sie die Ausgabesprache. Ihre strukturierte Zusammenfassung, Erklärungen und Ihr Gesundheitswert werden in der Sprache erstellt, die Sie am besten lesen.",
            },
        ],
        "langs_title": "Unterstützte Berichtssprachen",
        "langs_sub": "Laden Sie Ihre Laborergebnisse in einer dieser Sprachen hoch und erhalten Sie Ihren strukturierten Bericht in der Sprache Ihrer Wahl.",
        "langs": _LANGS_LIST,
        "who_title": "Für wen das gedacht ist",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Expats und Einwanderer",
                "desc": "Sie sind in ein neues Land gezogen und haben Blutuntersuchungen machen lassen. Der Bericht ist in der Landessprache, aber Sie denken und verstehen Gesundheitsthemen in Ihrer Muttersprache.",
            },
            {
                "icon": "\U0001f393",
                "title": "Internationale Studierende",
                "desc": "Pflichtuntersuchungen an der Universität liefern oft Berichte in der Landessprache. Eine strukturierte Erklärung in Ihrer eigenen Sprache hilft Ihnen bei der Nachsorge.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Familien über Grenzen hinweg",
                "desc": "Ihre Eltern oder Ihr Partner haben Laborergebnisse in einem anderen Land erhalten. Laden Sie den Bericht hoch und erstellen Sie eine Zusammenfassung in der Sprache, die Sie beide verstehen.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Medizintouristen und Reisende",
                "desc": "Blutuntersuchungen auf Reisen oder während eines Medizinaufenthalts im Ausland gemacht? Erhalten Sie eine strukturierte Zusammenfassung, die Sie Ihrem Arzt zu Hause zeigen können.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Zweisprachige Arztbesuche",
                "desc": "Sie verstehen Ihren Arzt in einer Sprache, aber haben Ihren Laborbericht in einer anderen erhalten. Ein einziges strukturiertes PDF in Ihrer bevorzugten Sprache kann den Termin erleichtern.",
            },
            {
                "icon": "\U0001f310",
                "title": "Internationale Ergebnisse vergleichen",
                "desc": "Wenn Sie in verschiedenen Ländern Blutuntersuchungen hatten, macht ein einheitliches strukturiertes Format in einer Sprache es einfacher, Ihre Werte über die Zeit zu verfolgen.",
            },
        ],
        "mid_cta_title": "Ihr Laborbericht, Ihre Sprache",
        "mid_cta_sub": "Laden Sie Ihre Blutuntersuchung in einer unterstützten Sprache hoch und wählen Sie, wie Sie die Ergebnisse lesen möchten.",
        "faqs": [
            {
                "q": "Kann ich einen Laborbericht in einer Sprache hochladen und die Ergebnisse in einer anderen erhalten?",
                "a": "Ja. Sie können einen Bericht in jeder unterstützten Sprache — Englisch, Türkisch, Französisch, Italienisch und mehr — hochladen und eine andere Sprache für Ihre strukturierte Ausgabe wählen. Die Werte und Referenzbereiche bleiben gleich; die Erklärungen werden in Ihrer bevorzugten Sprache erstellt.",
            },
            {
                "q": "Ist das ein medizinischer Übersetzungsdienst?",
                "a": "Nein. NoryaAI bietet keine zertifizierten medizinischen Übersetzungen. Es liest Ihren Laborbericht, strukturiert die Daten und erstellt eine lehrreiche Erklärung in der von Ihnen gewählten Sprache. Für offizielle oder rechtliche Zwecke wenden Sie sich an einen zertifizierten medizinischen Übersetzer.",
            },
            {
                "q": "Beeinflusst die Sprache die Genauigkeit der Analyse?",
                "a": "Nein. Die zugrunde liegende Analyse arbeitet mit den numerischen Werten, Einheiten und Referenzbereichen in Ihrem Bericht. Die Sprache des Originaldokuments beeinflusst nicht, wie die Werte geparst oder strukturiert werden.",
            },
            {
                "q": "Welche Sprachen werden unterstützt?",
                "a": "NoryaAI unterstützt derzeit Englisch, Deutsch, Türkisch, Französisch, Italienisch, Spanisch, Hebräisch, Hindi und Arabisch. Weitere Sprachen werden laufend hinzugefügt.",
            },
            {
                "q": "Kann ich den Bericht mit einem Arzt teilen, der eine andere Sprache spricht?",
                "a": "Ja. Sie können denselben Bericht bei Bedarf in mehreren Sprachen erstellen. Das strukturierte PDF-Format ist so gestaltet, dass es unabhängig vom medizinischen Hintergrund des Lesers klar und nützlich ist.",
            },
            {
                "q": "Ist NoryaAI ein Ersatz für meinen Arzt?",
                "a": "Nein. NoryaAI bietet strukturierte, lehrreiche Erklärungen, um Ihnen beim Verständnis Ihrer Laborergebnisse zu helfen. Es diagnostiziert nicht, behandelt nicht und verschreibt nichts. Konsultieren Sie bei medizinischen Entscheidungen immer einen qualifizierten Arzt.",
            },
        ],
        "cta_title": "Bereit, Ihre Ergebnisse zu verstehen?",
        "cta_sub": "Laden Sie Ihre Blutuntersuchung in jeder Sprache hoch und erhalten Sie einen klaren, strukturierten Bericht in der Sprache Ihrer Wahl.",
        "cta_primary": "Hochladen und jetzt analysieren",
        "cta_secondary": "Preise ansehen",
        "internal_links": _internal_links("de"),
    }


def _es() -> dict:
    return {
        "meta_title": "Entiende tus resultados de análisis de sangre en tu idioma | NoryaAI",
        "meta_description": "¿Tienes resultados de laboratorio en un idioma que no comprendes del todo? Sube tu análisis de sangre y obtén un informe estructurado y fácil de leer en español, inglés, alemán, francés y 6 idiomas más.",
        "hero_title": "Entiende tus resultados de análisis de sangre \u2014 en tu idioma",
        "hero_sub": "¿Vives en el extranjero o tienes un informe de laboratorio en un idioma desconocido? Sube tus resultados y obtén una explicación clara y estructurada en el idioma que mejor entiendas.",
        "cta_hero_primary": "Analizar mi análisis de sangre",
        "cta_hero_secondary": "Ver informes de ejemplo",
        "barrier_title": "Por qué el idioma dificulta la comprensión de los informes de laboratorio",
        "barrier_sub": "Un análisis de sangre ya es difícil de leer. Cuando el informe está en un idioma que no es el tuyo, el desafío se multiplica.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Términos médicos difíciles de buscar",
                "desc": "Los informes de laboratorio están llenos de abreviaturas y términos clínicos. Cuando están en otro idioma, ni siquiera un diccionario ayuda siempre — el vocabulario médico es especializado.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Convenciones de nombres diferentes",
                "desc": "La misma prueba de sangre puede tener un nombre, abreviatura o agrupación de panel diferente según el país. Un \"Blutbild\" en Alemania es un hemograma en España, pero la estructura puede variar.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Las unidades y rangos varían según la región",
                "desc": "¿Tu glucosa está en mg/dL o mmol/L? Los rangos de referencia y los sistemas de medición difieren entre países, lo que dificulta comparar valores que hayas visto antes.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Los traductores genéricos pierden matices médicos",
                "desc": "Pasar un informe de laboratorio por un traductor general puede producir resultados incómodos o engañosos. El contexto médico requiere más que una traducción palabra por palabra.",
            },
        ],
        "helps_title": "Cómo NoryaAI supera la barrera del idioma",
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
                "title": "Familias en distintos países",
                "desc": "Tu padre o pareja recibió resultados de laboratorio en otro país. Sube su informe y genera un resumen en el idioma que ambos entiendan.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Turistas médicos y viajeros",
                "desc": "¿Te hiciste un análisis de sangre mientras viajabas o durante un viaje médico al extranjero? Obtén un resumen estructurado que puedas compartir con tu médico en casa.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Visitas médicas bilingües",
                "desc": "Entiendes a tu médico en un idioma pero recibiste tu informe de laboratorio en otro. Un único PDF estructurado en tu idioma preferido puede facilitar la consulta.",
            },
            {
                "icon": "\U0001f310",
                "title": "Comparación de resultados internacionales",
                "desc": "Si te has hecho análisis de sangre en diferentes países, un formato estructurado unificado en un solo idioma facilita el seguimiento de tus valores a lo largo del tiempo.",
            },
        ],
        "mid_cta_title": "Tu informe de laboratorio, en tu idioma",
        "mid_cta_sub": "Sube tu análisis de sangre en cualquier idioma compatible y elige cómo quieres leer los resultados.",
        "faqs": [
            {
                "q": "¿Puedo subir un informe de laboratorio en un idioma y obtener los resultados en otro?",
                "a": "Sí. Puedes subir un informe en cualquier idioma compatible — alemán, turco, francés, italiano y más — y elegir un idioma diferente para tu salida estructurada. Los valores y rangos de referencia se mantienen iguales; las explicaciones se generan en tu idioma preferido.",
            },
            {
                "q": "¿Es esto un servicio de traducción médica?",
                "a": "No. NoryaAI no ofrece traducciones médicas certificadas. Lee tu informe de laboratorio, estructura los datos y genera una explicación educativa en el idioma que elijas. Para fines oficiales o legales, consulta a un traductor médico certificado.",
            },
            {
                "q": "¿El idioma afecta la precisión del análisis?",
                "a": "No. El análisis subyacente trabaja con los valores numéricos, unidades y rangos de referencia de tu informe. El idioma del documento original no afecta cómo se analizan o estructuran los valores.",
            },
            {
                "q": "¿Qué idiomas son compatibles?",
                "a": "NoryaAI actualmente soporta inglés, alemán, turco, francés, italiano, español, hebreo, hindi y árabe. Se están añadiendo más idiomas con el tiempo.",
            },
            {
                "q": "¿Puedo compartir el informe con un médico que hable otro idioma?",
                "a": "Sí. Puedes generar el mismo informe en varios idiomas si es necesario. El formato PDF estructurado está diseñado para ser claro y útil independientemente de la formación médica del lector.",
            },
            {
                "q": "¿NoryaAI reemplaza a mi médico?",
                "a": "No. NoryaAI ofrece explicaciones estructuradas y educativas para ayudarte a entender tus resultados de laboratorio. No diagnostica, trata ni prescribe. Consulta siempre a un profesional de la salud cualificado para decisiones médicas.",
            },
        ],
        "cta_title": "¿Listo para entender tus resultados?",
        "cta_sub": "Sube tu análisis de sangre en cualquier idioma y obtén un informe claro y estructurado en el que prefieras.",
        "cta_primary": "Subir y analizar ahora",
        "cta_secondary": "Ver precios",
        "internal_links": _internal_links("es"),
    }


def _fr() -> dict:
    return {
        "meta_title": "Comprendre vos résultats d'analyses sanguines dans votre langue | NoryaAI",
        "meta_description": "Vous avez reçu des résultats de laboratoire dans une langue que vous ne maîtrisez pas entièrement ? Téléchargez votre bilan sanguin et obtenez un rapport structuré et facile à lire en français, anglais, allemand, turc et 6 autres langues.",
        "hero_title": "Comprenez vos résultats d'analyses sanguines \u2014 dans votre langue",
        "hero_sub": "Vous vivez à l'étranger ou avez reçu un rapport de laboratoire dans une langue inconnue ? Téléchargez vos résultats et obtenez une explication claire et structurée dans la langue qui vous convient le mieux.",
        "cta_hero_primary": "Analyser mon bilan sanguin",
        "cta_hero_secondary": "Voir des rapports exemples",
        "barrier_title": "Pourquoi la langue rend les rapports de laboratoire plus difficiles à comprendre",
        "barrier_sub": "Un bilan sanguin est déjà difficile à lire. Lorsque le rapport est dans une langue qui n'est pas la vôtre, la difficulté se multiplie.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Des termes médicaux difficiles à rechercher",
                "desc": "Les rapports de laboratoire regorgent d'abréviations et de termes cliniques. Lorsqu'ils sont dans une autre langue, même un dictionnaire ne suffit pas toujours — le vocabulaire médical est spécialisé.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Des conventions de nommage différentes",
                "desc": "La même analyse sanguine peut porter un nom, une abréviation ou un regroupement de panel différent selon le pays. Un « Blutbild » en Allemagne correspond à un NFS en France, mais la structure peut varier.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Les unités et les plages de référence varient selon la région",
                "desc": "Votre glycémie est-elle en mg/dL ou en mmol/L ? Les plages de référence et les systèmes de mesure diffèrent d'un pays à l'autre, ce qui rend la comparaison des valeurs plus difficile.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "Les traducteurs génériques manquent les nuances médicales",
                "desc": "Passer un rapport de laboratoire dans un traducteur générique peut produire des résultats maladroits ou trompeurs. Le contexte médical nécessite bien plus qu'une traduction mot à mot.",
            },
        ],
        "helps_title": "Comment NoryaAI comble la barrière linguistique",
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
                "desc": "Les valeurs, unités et plages de référence sont extraites et organisées en catégories claires, quelle que soit la langue d'origine.",
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
                "desc": "Vous avez déménagé dans un nouveau pays et fait une analyse de sang. Le rapport est dans la langue locale, mais vous pensez et comprenez les sujets de santé dans votre langue maternelle.",
            },
            {
                "icon": "\U0001f393",
                "title": "Étudiants internationaux",
                "desc": "Les examens de santé obligatoires à l'université produisent souvent des rapports dans la langue locale. Une explication structurée dans votre propre langue vous aide à assurer le suivi.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Familles séparées par les frontières",
                "desc": "Votre parent ou partenaire a reçu des résultats de laboratoire dans un autre pays. Téléchargez leur rapport et générez un résumé dans la langue que vous comprenez tous les deux.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Touristes médicaux et voyageurs",
                "desc": "Vous avez fait une analyse de sang en voyage ou lors d'un séjour médical à l'étranger ? Obtenez un résumé structuré à partager avec votre médecin à domicile.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Consultations médicales bilingues",
                "desc": "Vous comprenez votre médecin dans une langue mais avez reçu votre rapport de laboratoire dans une autre. Un seul PDF structuré dans votre langue préférée peut faciliter le rendez-vous.",
            },
            {
                "icon": "\U0001f310",
                "title": "Comparer des résultats internationaux",
                "desc": "Si vous avez fait des analyses de sang dans différents pays, un format structuré unifié dans une seule langue facilite le suivi de vos valeurs au fil du temps.",
            },
        ],
        "mid_cta_title": "Votre rapport de laboratoire, dans votre langue",
        "mid_cta_sub": "Téléchargez votre bilan sanguin dans n'importe quelle langue prise en charge et choisissez comment vous souhaitez lire les résultats.",
        "faqs": [
            {
                "q": "Puis-je télécharger un rapport de laboratoire dans une langue et obtenir les résultats dans une autre ?",
                "a": "Oui. Vous pouvez télécharger un rapport dans n'importe quelle langue prise en charge — allemand, turc, anglais, italien et plus — et choisir une langue différente pour votre sortie structurée. Les valeurs et plages de référence restent identiques ; les explications sont générées dans votre langue préférée.",
            },
            {
                "q": "Est-ce un service de traduction médicale ?",
                "a": "Non. NoryaAI ne fournit pas de traductions médicales certifiées. Il lit votre rapport de laboratoire, structure les données et génère une explication éducative dans la langue de votre choix. Pour des besoins officiels ou juridiques, consultez un traducteur médical certifié.",
            },
            {
                "q": "La langue affecte-t-elle la précision de l'analyse ?",
                "a": "Non. L'analyse sous-jacente fonctionne avec les valeurs numériques, les unités et les plages de référence de votre rapport. La langue du document original n'affecte pas la façon dont les valeurs sont analysées ou structurées.",
            },
            {
                "q": "Quelles langues sont prises en charge ?",
                "a": "NoryaAI prend actuellement en charge l'anglais, l'allemand, le turc, le français, l'italien, l'espagnol, l'hébreu, l'hindi et l'arabe. D'autres langues sont ajoutées au fil du temps.",
            },
            {
                "q": "Puis-je partager le rapport avec un médecin qui parle une autre langue ?",
                "a": "Oui. Vous pouvez générer le même rapport dans plusieurs langues si nécessaire. Le format PDF structuré est conçu pour être clair et utile quel que soit le parcours médical du lecteur.",
            },
            {
                "q": "NoryaAI remplace-t-il mon médecin ?",
                "a": "Non. NoryaAI fournit des explications structurées et éducatives pour vous aider à comprendre vos résultats de laboratoire. Il ne diagnostique pas, ne traite pas et ne prescrit pas. Consultez toujours un professionnel de santé qualifié pour les décisions médicales.",
            },
        ],
        "cta_title": "Prêt à comprendre vos résultats ?",
        "cta_sub": "Téléchargez votre bilan sanguin dans n'importe quelle langue et obtenez un rapport clair et structuré dans celle que vous préférez.",
        "cta_primary": "Télécharger et analyser maintenant",
        "cta_secondary": "Voir les tarifs",
        "internal_links": _internal_links("fr"),
    }


def _it() -> dict:
    return {
        "meta_title": "Comprendi i risultati delle analisi del sangue nella tua lingua | NoryaAI",
        "meta_description": "Hai ricevuto referti di laboratorio in una lingua che non comprendi del tutto? Carica le tue analisi del sangue e ottieni un report strutturato e facile da leggere in italiano, inglese, tedesco, francese e altre 6 lingue.",
        "hero_title": "Comprendi i risultati delle analisi del sangue \u2014 nella tua lingua",
        "hero_sub": "Vivi all'estero o hai ricevuto un referto di laboratorio in una lingua sconosciuta? Carica i tuoi risultati e ottieni una spiegazione chiara e strutturata nella lingua che preferisci.",
        "cta_hero_primary": "Analizza le mie analisi del sangue",
        "cta_hero_secondary": "Vedi report di esempio",
        "barrier_title": "Perché la lingua rende i referti di laboratorio più difficili da capire",
        "barrier_sub": "Un'analisi del sangue è già difficile da leggere. Quando il referto è in una lingua che non è la tua, la sfida si moltiplica.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "Termini medici difficili da cercare",
                "desc": "I referti di laboratorio sono pieni di abbreviazioni e termini clinici. Quando sono in un'altra lingua, neanche un dizionario aiuta sempre — il vocabolario medico è specializzato.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "Convenzioni di denominazione diverse",
                "desc": "Lo stesso esame del sangue può avere un nome, un'abbreviazione o un raggruppamento di pannello diverso a seconda del Paese. Un \"Blutbild\" in Germania è un emocromo in Italia, ma la struttura può variare.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "Unità e intervalli di riferimento variano per regione",
                "desc": "La tua glicemia è in mg/dL o mmol/L? Gli intervalli di riferimento e i sistemi di misurazione differiscono tra i Paesi, rendendo più difficile confrontare i valori visti in precedenza.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "I traduttori generici perdono le sfumature mediche",
                "desc": "Passare un referto di laboratorio in un traduttore generico può produrre risultati imprecisi o fuorvianti. Il contesto medico richiede più di una traduzione parola per parola.",
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
                "desc": "I valori, le unità e gli intervalli di riferimento vengono estratti e organizzati in categorie chiare, indipendentemente dalla lingua originale.",
            },
            {
                "icon": "\U0001f310",
                "title": "Ricevi il tuo report nella tua lingua",
                "desc": "Scegli la lingua di output. Il tuo riepilogo strutturato, le spiegazioni e il punteggio di salute vengono generati nella lingua che preferisci leggere.",
            },
        ],
        "langs_title": "Lingue dei report supportate",
        "langs_sub": "Carica i tuoi risultati di laboratorio in una qualsiasi di queste lingue e ricevi il tuo report strutturato in quella che preferisci.",
        "langs": _LANGS_LIST,
        "who_title": "A chi è rivolto",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "Espatriati e immigrati",
                "desc": "Ti sei trasferito in un nuovo Paese e hai fatto le analisi del sangue. Il referto è nella lingua locale, ma pensi e comprendi i temi di salute nella tua lingua madre.",
            },
            {
                "icon": "\U0001f393",
                "title": "Studenti internazionali",
                "desc": "Gli screening sanitari obbligatori all'università spesso producono referti nella lingua locale. Una spiegazione strutturata nella tua lingua ti aiuta nel follow-up.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "Famiglie oltre i confini",
                "desc": "Il tuo genitore o partner ha ricevuto risultati di laboratorio in un altro Paese. Carica il loro referto e genera un riepilogo nella lingua che entrambi comprendete.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "Turisti medici e viaggiatori",
                "desc": "Hai fatto le analisi del sangue in viaggio o durante un soggiorno medico all'estero? Ottieni un riepilogo strutturato da condividere con il tuo medico a casa.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "Visite mediche bilingui",
                "desc": "Capisci il tuo medico in una lingua ma hai ricevuto il referto in un'altra. Un unico PDF strutturato nella tua lingua preferita può rendere l'appuntamento più semplice.",
            },
            {
                "icon": "\U0001f310",
                "title": "Confronto di risultati internazionali",
                "desc": "Se hai fatto analisi del sangue in diversi Paesi, un formato strutturato unificato in una sola lingua rende più facile monitorare i tuoi valori nel tempo.",
            },
        ],
        "mid_cta_title": "Il tuo referto, nella tua lingua",
        "mid_cta_sub": "Carica le tue analisi del sangue in qualsiasi lingua supportata e scegli come vuoi leggere i risultati.",
        "faqs": [
            {
                "q": "Posso caricare un referto di laboratorio in una lingua e ottenere i risultati in un'altra?",
                "a": "Sì. Puoi caricare un referto in qualsiasi lingua supportata — tedesco, turco, francese, inglese e altro — e scegliere una lingua diversa per il tuo output strutturato. I valori e gli intervalli di riferimento restano gli stessi; le spiegazioni vengono generate nella tua lingua preferita.",
            },
            {
                "q": "Questo è un servizio di traduzione medica?",
                "a": "No. NoryaAI non fornisce traduzioni mediche certificate. Legge il tuo referto di laboratorio, struttura i dati e genera una spiegazione educativa nella lingua che scegli. Per scopi ufficiali o legali, consulta un traduttore medico certificato.",
            },
            {
                "q": "La lingua influisce sulla precisione dell'analisi?",
                "a": "No. L'analisi sottostante lavora con i valori numerici, le unità e gli intervalli di riferimento del tuo referto. La lingua del documento originale non influenza il modo in cui i valori vengono analizzati o strutturati.",
            },
            {
                "q": "Quali lingue sono supportate?",
                "a": "NoryaAI attualmente supporta inglese, tedesco, turco, francese, italiano, spagnolo, ebraico, hindi e arabo. Altre lingue vengono aggiunte nel tempo.",
            },
            {
                "q": "Posso condividere il report con un medico che parla un'altra lingua?",
                "a": "Sì. Puoi generare lo stesso report in più lingue se necessario. Il formato PDF strutturato è progettato per essere chiaro e utile indipendentemente dal background medico del lettore.",
            },
            {
                "q": "NoryaAI sostituisce il mio medico?",
                "a": "No. NoryaAI fornisce spiegazioni strutturate ed educative per aiutarti a comprendere i tuoi risultati di laboratorio. Non diagnostica, non cura e non prescrive. Consulta sempre un professionista sanitario qualificato per decisioni mediche.",
            },
        ],
        "cta_title": "Pronto a capire i tuoi risultati?",
        "cta_sub": "Carica le tue analisi del sangue in qualsiasi lingua e ottieni un report chiaro e strutturato in quella che preferisci.",
        "cta_primary": "Carica e analizza ora",
        "cta_secondary": "Vedi i prezzi",
        "internal_links": _internal_links("it"),
    }


def _he() -> dict:
    return {
        "meta_title": "הבינו את תוצאות בדיקות הדם שלכם בשפה שלכם | NoryaAI",
        "meta_description": "קיבלתם תוצאות מעבדה בשפה שאתם לא מבינים לגמרי? העלו את בדיקת הדם שלכם וקבלו דוח מובנה וקל לקריאה בעברית, אנגלית, גרמנית, צרפתית ו-6 שפות נוספות.",
        "hero_title": "הבינו את תוצאות בדיקות הדם שלכם — בשפה שלכם",
        "hero_sub": "גרים בחו\"ל או קיבלתם דוח מעבדה בשפה לא מוכרת? העלו את התוצאות שלכם וקבלו הסבר ברור ומובנה בשפה הנוחה לכם ביותר.",
        "cta_hero_primary": "נתחו את בדיקת הדם שלי",
        "cta_hero_secondary": "צפו בדוחות לדוגמה",
        "barrier_title": "למה שפה מקשה על הבנת דוחות מעבדה",
        "barrier_sub": "בדיקת דם כבר קשה לקריאה. כשהדוח בשפה שאינה שפת האם שלכם, האתגר מוכפל.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "מונחים רפואיים שקשה לחפש",
                "desc": "דוחות מעבדה מלאים בקיצורים ומונחים קליניים. כשהם בשפה אחרת, גם מילון לא תמיד עוזר — אוצר המילים הרפואי מתמחה.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "מוסכמות שמות שונות",
                "desc": "לאותה בדיקת דם יכולים להיות שם, קיצור או קיבוץ פאנל שונה בהתאם למדינה. \"Blutbild\" בגרמניה הוא ספירת דם בישראל, אבל המבנה עשוי להיות שונה.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "יחידות וטווחים משתנים לפי אזור",
                "desc": "הגלוקוז שלכם ב-mg/dL או mmol/L? טווחי הייחוס ומערכות המדידה שונים בין מדינות, מה שמקשה על השוואת ערכים שאולי ראיתם בעבר.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "מתרגמים כלליים מפספסים ניואנסים רפואיים",
                "desc": "העברת דוח מעבדה דרך מתרגם כללי עלולה לייצר תוצאות מביכות או מטעות. הקשר רפואי דורש יותר מתרגום מילה במילה.",
            },
        ],
        "helps_title": "איך NoryaAI מגשר על פער השפה",
        "helps_sub": "NoryaAI לא רק מתרגם את הדוח שלכם. הוא קורא, מבנה ומסביר את התוצאות שלכם בשפה שבחרתם.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "העלו בכל שפה",
                "desc": "דוח המעבדה שלכם יכול להיות בגרמנית, טורקית, איטלקית, צרפתית או כל שפה נתמכת. העלו PDF, תמונה או הדביקו את הטקסט.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "בינה מלאכותית מבנה את הנתונים",
                "desc": "ערכים, יחידות וטווחי ייחוס מופקים ומאורגנים בקטגוריות ברורות — ללא תלות בשפת המקור.",
            },
            {
                "icon": "\U0001f310",
                "title": "קבלו את הדוח בשפה שלכם",
                "desc": "בחרו את שפת הפלט. הסיכום המובנה, ההסברים וציון הבריאות שלכם נוצרים בשפה הנוחה לכם ביותר לקריאה.",
            },
        ],
        "langs_title": "שפות דוח נתמכות",
        "langs_sub": "העלו את תוצאות המעבדה שלכם בכל אחת מהשפות הללו וקבלו את הדוח המובנה שלכם בשפה שתבחרו.",
        "langs": _LANGS_LIST,
        "who_title": "למי זה מיועד",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "עולים ומהגרים",
                "desc": "עברתם למדינה חדשה ועשיתם בדיקות דם. הדוח בשפה המקומית, אבל אתם חושבים ומבינים נושאי בריאות בשפת האם שלכם.",
            },
            {
                "icon": "\U0001f393",
                "title": "סטודנטים בינלאומיים",
                "desc": "בדיקות בריאות חובה באוניברסיטה מייצרות לעתים קרובות דוחות בשפה המקומית. הסבר מובנה בשפה שלכם עוזר לכם במעקב.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "משפחות מעבר לגבולות",
                "desc": "ההורה או בן/בת הזוג שלכם קיבלו תוצאות מעבדה במדינה אחרת. העלו את הדוח שלהם וצרו סיכום בשפה שאתם שניכם מבינים.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "תיירים רפואיים ומטיילים",
                "desc": "עשיתם בדיקות דם בנסיעה או במהלך טיול רפואי בחו\"ל? קבלו סיכום מובנה שתוכלו לשתף עם הרופא שלכם בבית.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "ביקורים רפואיים דו-לשוניים",
                "desc": "אתם מבינים את הרופא שלכם בשפה אחת אבל קיבלתם את דוח המעבדה בשפה אחרת. PDF מובנה יחיד בשפה המועדפת עליכם יכול להקל על התור.",
            },
            {
                "icon": "\U0001f310",
                "title": "השוואת תוצאות בינלאומיות",
                "desc": "אם עשיתם בדיקות דם במדינות שונות, פורמט מובנה אחיד בשפה אחת מקל על מעקב אחר הערכים שלכם לאורך זמן.",
            },
        ],
        "mid_cta_title": "דוח המעבדה שלכם, בשפה שלכם",
        "mid_cta_sub": "העלו את בדיקת הדם שלכם בכל שפה נתמכת ובחרו איך אתם רוצים לקרוא את התוצאות.",
        "faqs": [
            {
                "q": "האם אפשר להעלות דוח מעבדה בשפה אחת ולקבל את התוצאות בשפה אחרת?",
                "a": "כן. אתם יכולים להעלות דוח בכל שפה נתמכת — גרמנית, טורקית, צרפתית, איטלקית ועוד — ולבחור שפה אחרת לפלט המובנה שלכם. הערכים וטווחי הייחוס נשארים זהים; ההסברים נוצרים בשפה המועדפת עליכם.",
            },
            {
                "q": "האם זה שירות תרגום רפואי?",
                "a": "לא. NoryaAI אינו מספק תרגומים רפואיים מוסמכים. הוא קורא את דוח המעבדה שלכם, מבנה את הנתונים ומייצר הסבר חינוכי בשפה שבחרתם. לצרכים רשמיים או משפטיים, פנו למתרגם רפואי מוסמך.",
            },
            {
                "q": "האם השפה משפיעה על דיוק הניתוח?",
                "a": "לא. הניתוח הבסיסי עובד עם הערכים המספריים, היחידות וטווחי הייחוס בדוח שלכם. שפת המסמך המקורי אינה משפיעה על אופן הניתוח או המבנה של הערכים.",
            },
            {
                "q": "אילו שפות נתמכות?",
                "a": "NoryaAI תומך כרגע באנגלית, גרמנית, טורקית, צרפתית, איטלקית, ספרדית, עברית, הינדי וערבית. שפות נוספות מתווספות עם הזמן.",
            },
            {
                "q": "האם אפשר לשתף את הדוח עם רופא שמדבר שפה אחרת?",
                "a": "כן. אתם יכולים ליצור את אותו הדוח במספר שפות אם צריך. פורמט ה-PDF המובנה מתוכנן להיות ברור ושימושי ללא קשר לרקע הרפואי של הקורא.",
            },
            {
                "q": "האם NoryaAI מחליף את הרופא שלי?",
                "a": "לא. NoryaAI מספק הסברים מובנים וחינוכיים כדי לעזור לכם להבין את תוצאות המעבדה שלכם. הוא אינו מאבחן, מטפל או רושם תרופות. התייעצו תמיד עם איש מקצוע רפואי מוסמך בעניין החלטות רפואיות.",
            },
        ],
        "cta_title": "מוכנים להבין את התוצאות שלכם?",
        "cta_sub": "העלו את בדיקת הדם שלכם בכל שפה וקבלו דוח ברור ומובנה בשפה שאתם מעדיפים.",
        "cta_primary": "העלו ונתחו עכשיו",
        "cta_secondary": "צפו בתמחור",
        "internal_links": _internal_links("he"),
    }


def _hi() -> dict:
    return {
        "meta_title": "अपनी रक्त परीक्षण रिपोर्ट अपनी भाषा में समझें | NoryaAI",
        "meta_description": "क्या आपको ऐसी भाषा में लैब रिपोर्ट मिली है जो आप पूरी तरह नहीं समझते? अपना रक्त परीक्षण अपलोड करें और हिन्दी, अंग्रेज़ी, जर्मन, फ़्रेंच और 6 अन्य भाषाओं में एक संरचित, पढ़ने में आसान रिपोर्ट प्राप्त करें।",
        "hero_title": "अपने रक्त परीक्षण के परिणाम समझें — अपनी भाषा में",
        "hero_sub": "विदेश में रह रहे हैं या किसी अपरिचित भाषा में लैब रिपोर्ट मिली है? अपने परिणाम अपलोड करें और जिस भाषा में आप सबसे सहज हैं, उसमें एक स्पष्ट, संरचित स्पष्टीकरण प्राप्त करें।",
        "cta_hero_primary": "मेरा रक्त परीक्षण विश्लेषित करें",
        "cta_hero_secondary": "नमूना रिपोर्ट देखें",
        "barrier_title": "भाषा लैब रिपोर्ट को समझना क्यों कठिन बनाती है",
        "barrier_sub": "रक्त परीक्षण पहले से ही पढ़ना मुश्किल होता है। जब रिपोर्ट ऐसी भाषा में हो जो आपकी मातृभाषा नहीं है, तो चुनौती कई गुना बढ़ जाती है।",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "चिकित्सा शब्द जो आसानी से खोजे नहीं जा सकते",
                "desc": "लैब रिपोर्ट संक्षिप्ताक्षरों और नैदानिक शब्दों से भरी होती हैं। जब ये किसी अन्य भाषा में हों, तो शब्दकोश भी हमेशा मदद नहीं करता — चिकित्सा शब्दावली विशेषज्ञ होती है।",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "अलग-अलग नामकरण परंपराएँ",
                "desc": "एक ही रक्त परीक्षण का देश के अनुसार अलग नाम, संक्षिप्त रूप या पैनल ग्रुपिंग हो सकती है। जर्मनी में \"Blutbild\" अमेरिका में CBC है, लेकिन संरचना भिन्न हो सकती है।",
            },
            {
                "icon": "\U0001f4cf",
                "title": "इकाइयाँ और संदर्भ सीमाएँ क्षेत्र के अनुसार भिन्न होती हैं",
                "desc": "आपका ग्लूकोज़ mg/dL में है या mmol/L में? संदर्भ सीमाएँ और मापन प्रणालियाँ देशों के बीच भिन्न होती हैं, जिससे पहले देखे गए मूल्यों से तुलना करना कठिन हो जाता है।",
            },
            {
                "icon": "\U0001f6ab",
                "title": "सामान्य अनुवादक चिकित्सा सूक्ष्मताएँ चूक जाते हैं",
                "desc": "लैब रिपोर्ट को सामान्य अनुवादक से गुज़ारने पर अजीब या भ्रामक परिणाम आ सकते हैं। चिकित्सा संदर्भ के लिए शब्द-दर-शब्द अनुवाद से अधिक की आवश्यकता होती है।",
            },
        ],
        "helps_title": "NoryaAI भाषा की खाई कैसे पाटता है",
        "helps_sub": "NoryaAI सिर्फ़ आपकी रिपोर्ट का अनुवाद नहीं करता। यह आपके परिणामों को पढ़ता है, संरचित करता है और आपकी चुनी हुई भाषा में समझाता है।",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "किसी भी भाषा में अपलोड करें",
                "desc": "आपकी लैब रिपोर्ट जर्मन, तुर्की, इतालवी, फ़्रेंच या किसी भी समर्थित भाषा में हो सकती है। PDF, फ़ोटो अपलोड करें या टेक्स्ट पेस्ट करें।",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI आपके डेटा को संरचित करता है",
                "desc": "मूल भाषा से स्वतंत्र रूप से मूल्यों, इकाइयों और संदर्भ सीमाओं को निकालकर स्पष्ट श्रेणियों में व्यवस्थित किया जाता है।",
            },
            {
                "icon": "\U0001f310",
                "title": "अपनी भाषा में रिपोर्ट प्राप्त करें",
                "desc": "आउटपुट भाषा चुनें। आपका संरचित सारांश, स्पष्टीकरण और स्वास्थ्य स्कोर उस भाषा में तैयार किए जाते हैं जिसमें आप सबसे आरामदायक हैं।",
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
                "desc": "आप एक नए देश में चले गए और रक्त परीक्षण करवाया। रिपोर्ट स्थानीय भाषा में है, लेकिन आप स्वास्थ्य विषयों को अपनी मातृभाषा में सोचते और समझते हैं।",
            },
            {
                "icon": "\U0001f393",
                "title": "अंतरराष्ट्रीय छात्र",
                "desc": "विश्वविद्यालय में अनिवार्य स्वास्थ्य जाँच अक्सर स्थानीय भाषा में रिपोर्ट तैयार करती है। अपनी भाषा में एक संरचित स्पष्टीकरण आपको फ़ॉलो-अप में मदद करता है।",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "सीमाओं के पार परिवार",
                "desc": "आपके माता-पिता या साथी को दूसरे देश में लैब परिणाम मिले। उनकी रिपोर्ट अपलोड करें और दोनों की समझ में आने वाली भाषा में सारांश बनाएँ।",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "चिकित्सा पर्यटक और यात्री",
                "desc": "यात्रा के दौरान या विदेश में चिकित्सा यात्रा के दौरान रक्त परीक्षण करवाया? एक संरचित सारांश प्राप्त करें जिसे आप अपने घर के डॉक्टर के साथ साझा कर सकें।",
            },
            {
                "icon": "\U0001fa7a",
                "title": "द्विभाषी डॉक्टर विज़िट",
                "desc": "आप अपने डॉक्टर को एक भाषा में समझते हैं लेकिन लैब रिपोर्ट दूसरी भाषा में मिली। आपकी पसंदीदा भाषा में एक संरचित PDF अपॉइंटमेंट को आसान बना सकता है।",
            },
            {
                "icon": "\U0001f310",
                "title": "अंतरराष्ट्रीय परिणामों की तुलना करने वाले",
                "desc": "अगर आपने विभिन्न देशों में रक्त परीक्षण करवाए हैं, तो एक भाषा में एकीकृत संरचित प्रारूप समय के साथ आपके मूल्यों को ट्रैक करना आसान बनाता है।",
            },
        ],
        "mid_cta_title": "आपकी लैब रिपोर्ट, आपकी भाषा",
        "mid_cta_sub": "अपना रक्त परीक्षण किसी भी समर्थित भाषा में अपलोड करें और चुनें कि आप परिणाम कैसे पढ़ना चाहते हैं।",
        "faqs": [
            {
                "q": "क्या मैं एक भाषा में लैब रिपोर्ट अपलोड करके दूसरी भाषा में परिणाम प्राप्त कर सकता/सकती हूँ?",
                "a": "हाँ। आप किसी भी समर्थित भाषा — जर्मन, तुर्की, फ़्रेंच, इतालवी और अधिक — में रिपोर्ट अपलोड कर सकते हैं और अपने संरचित आउटपुट के लिए अलग भाषा चुन सकते हैं। मूल्य और संदर्भ सीमाएँ वही रहती हैं; स्पष्टीकरण आपकी पसंदीदा भाषा में तैयार किए जाते हैं।",
            },
            {
                "q": "क्या यह चिकित्सा अनुवाद सेवा है?",
                "a": "नहीं। NoryaAI प्रमाणित चिकित्सा अनुवाद प्रदान नहीं करता। यह आपकी लैब रिपोर्ट पढ़ता है, डेटा को संरचित करता है और आपकी चुनी हुई भाषा में शैक्षिक स्पष्टीकरण तैयार करता है। आधिकारिक या कानूनी उद्देश्यों के लिए, प्रमाणित चिकित्सा अनुवादक से परामर्श करें।",
            },
            {
                "q": "क्या भाषा विश्लेषण की सटीकता को प्रभावित करती है?",
                "a": "नहीं। अंतर्निहित विश्लेषण आपकी रिपोर्ट में संख्यात्मक मूल्यों, इकाइयों और संदर्भ सीमाओं के साथ काम करता है। मूल दस्तावेज़ की भाषा मूल्यों के विश्लेषण या संरचना को प्रभावित नहीं करती।",
            },
            {
                "q": "कौन सी भाषाएँ समर्थित हैं?",
                "a": "NoryaAI वर्तमान में अंग्रेज़ी, जर्मन, तुर्की, फ़्रेंच, इतालवी, स्पेनिश, हिब्रू, हिन्दी और अरबी का समर्थन करता है। समय के साथ और भाषाएँ जोड़ी जा रही हैं।",
            },
            {
                "q": "क्या मैं रिपोर्ट को किसी ऐसे डॉक्टर के साथ साझा कर सकता/सकती हूँ जो दूसरी भाषा बोलता है?",
                "a": "हाँ। ज़रूरत पड़ने पर आप वही रिपोर्ट कई भाषाओं में तैयार कर सकते हैं। संरचित PDF प्रारूप पाठक की चिकित्सा पृष्ठभूमि की परवाह किए बिना स्पष्ट और उपयोगी होने के लिए डिज़ाइन किया गया है।",
            },
            {
                "q": "क्या NoryaAI मेरे डॉक्टर का विकल्प है?",
                "a": "नहीं। NoryaAI आपकी लैब रिपोर्ट को समझने में मदद करने के लिए संरचित, शैक्षिक स्पष्टीकरण प्रदान करता है। यह न तो निदान करता है, न उपचार करता है, न दवाई लिखता है। चिकित्सा निर्णयों के लिए हमेशा किसी योग्य स्वास्थ्य पेशेवर से परामर्श करें।",
            },
        ],
        "cta_title": "अपने परिणाम समझने के लिए तैयार हैं?",
        "cta_sub": "अपना रक्त परीक्षण किसी भी भाषा में अपलोड करें और अपनी पसंदीदा भाषा में एक स्पष्ट, संरचित रिपोर्ट प्राप्त करें।",
        "cta_primary": "अपलोड करें और अभी विश्लेषण करें",
        "cta_secondary": "मूल्य देखें",
        "internal_links": _internal_links("hi"),
    }


def _ar() -> dict:
    return {
        "meta_title": "افهم نتائج فحص الدم بلغتك | NoryaAI",
        "meta_description": "هل حصلت على نتائج مختبرية بلغة لا تفهمها بالكامل؟ ارفع فحص الدم الخاص بك واحصل على تقرير منظّم وسهل القراءة بالعربية والإنجليزية والألمانية والفرنسية و6 لغات أخرى.",
        "hero_title": "افهم نتائج فحص الدم \u2014 بلغتك",
        "hero_sub": "تعيش في الخارج أو حصلت على تقرير مختبري بلغة غير مألوفة؟ ارفع نتائجك واحصل على شرح واضح ومنظّم باللغة التي تفهمها بشكل أفضل.",
        "cta_hero_primary": "حلّل فحص الدم الخاص بي",
        "cta_hero_secondary": "اعرض تقارير نموذجية",
        "barrier_title": "لماذا تجعل اللغة تقارير المختبر أصعب في الفهم",
        "barrier_sub": "فحص الدم صعب القراءة بالفعل. عندما يكون التقرير بلغة ليست لغتك الأم، يتضاعف التحدي.",
        "barrier_items": [
            {
                "icon": "\U0001f4c4",
                "title": "مصطلحات طبية يصعب البحث عنها",
                "desc": "تقارير المختبر مليئة بالاختصارات والمصطلحات السريرية. عندما تكون بلغة أخرى، حتى القاموس لا يساعد دائمًا — المفردات الطبية متخصصة.",
            },
            {
                "icon": "\U0001f5fa\ufe0f",
                "title": "اختلافات في التسمية",
                "desc": "قد يحمل نفس فحص الدم اسمًا أو اختصارًا أو تصنيفًا مختلفًا حسب البلد. \"Blutbild\" في ألمانيا هو تعداد دم كامل (CBC) في أمريكا، لكن البنية قد تختلف.",
            },
            {
                "icon": "\U0001f4cf",
                "title": "الوحدات والنطاقات تختلف حسب المنطقة",
                "desc": "هل مستوى السكر لديك بـ mg/dL أم mmol/L؟ نطاقات المرجعية وأنظمة القياس تختلف بين البلدان، مما يصعّب مقارنة القيم التي ربما رأيتها سابقًا.",
            },
            {
                "icon": "\U0001f6ab",
                "title": "المترجمات العامة تفوّت الدقة الطبية",
                "desc": "تمرير تقرير مختبري عبر مترجم عام قد ينتج نتائج محرجة أو مضللة. السياق الطبي يتطلب أكثر من ترجمة كلمة بكلمة.",
            },
        ],
        "helps_title": "كيف يسدّ NoryaAI فجوة اللغة",
        "helps_sub": "NoryaAI لا يترجم تقريرك فحسب. يقرأ نتائجك ويُنظّمها ويشرحها باللغة التي تختارها.",
        "helps_steps": [
            {
                "icon": "\U0001f4e4",
                "title": "ارفع بأي لغة",
                "desc": "يمكن أن يكون تقريرك المختبري بالألمانية أو التركية أو الإيطالية أو الفرنسية أو أي لغة مدعومة. ارفع ملف PDF أو صورة أو الصق النص.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "الذكاء الاصطناعي يُنظّم بياناتك",
                "desc": "يتم استخراج القيم والوحدات والنطاقات المرجعية وتنظيمها في فئات واضحة — بغض النظر عن اللغة الأصلية.",
            },
            {
                "icon": "\U0001f310",
                "title": "احصل على تقريرك بلغتك",
                "desc": "اختر لغة الإخراج. ملخصك المنظّم وشروحاتك ونقاط صحتك يتم إنشاؤها باللغة التي تفضل قراءتها.",
            },
        ],
        "langs_title": "لغات التقارير المدعومة",
        "langs_sub": "ارفع نتائج مختبرك بأي من هذه اللغات واستلم تقريرك المنظّم باللغة التي تفضلها.",
        "langs": _LANGS_LIST,
        "who_title": "لمن هذا مخصص",
        "who_items": [
            {
                "icon": "\u2708\ufe0f",
                "title": "المغتربون والمهاجرون",
                "desc": "انتقلت إلى بلد جديد وأجريت فحص دم. التقرير باللغة المحلية، لكنك تفكر وتفهم المواضيع الصحية بلغتك الأم.",
            },
            {
                "icon": "\U0001f393",
                "title": "الطلاب الدوليون",
                "desc": "الفحوصات الصحية الإلزامية في الجامعة غالبًا ما تنتج تقارير باللغة المحلية. شرح منظّم بلغتك يساعدك في المتابعة.",
            },
            {
                "icon": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
                "title": "عائلات عبر الحدود",
                "desc": "والدك أو شريكك حصل على نتائج مختبرية في بلد آخر. ارفع تقريرهم وأنشئ ملخصًا باللغة التي تفهمونها معًا.",
            },
            {
                "icon": "\U0001f3d6\ufe0f",
                "title": "السياح الطبيون والمسافرون",
                "desc": "أجريت فحص دم أثناء السفر أو في رحلة طبية للخارج؟ احصل على ملخص منظّم يمكنك مشاركته مع طبيبك في بلدك.",
            },
            {
                "icon": "\U0001fa7a",
                "title": "زيارات طبية ثنائية اللغة",
                "desc": "تفهم طبيبك بلغة لكنك تلقيت تقرير المختبر بلغة أخرى. ملف PDF منظّم واحد بلغتك المفضلة يمكن أن يسهّل الموعد.",
            },
            {
                "icon": "\U0001f310",
                "title": "مقارنة النتائج الدولية",
                "desc": "إذا أجريت فحوصات دم في بلدان مختلفة، فإن تنسيقًا منظّمًا موحّدًا بلغة واحدة يسهّل تتبع قيمك عبر الزمن.",
            },
        ],
        "mid_cta_title": "تقريرك المختبري، بلغتك",
        "mid_cta_sub": "ارفع فحص الدم الخاص بك بأي لغة مدعومة واختر كيف تريد قراءة النتائج.",
        "faqs": [
            {
                "q": "هل يمكنني رفع تقرير مختبري بلغة والحصول على النتائج بلغة أخرى؟",
                "a": "نعم. يمكنك رفع تقرير بأي لغة مدعومة — الألمانية والتركية والفرنسية والإيطالية والمزيد — واختيار لغة مختلفة لمخرجاتك المنظّمة. القيم والنطاقات المرجعية تبقى كما هي؛ الشروحات تُولَّد بلغتك المفضلة.",
            },
            {
                "q": "هل هذه خدمة ترجمة طبية؟",
                "a": "لا. NoryaAI لا يقدم ترجمات طبية معتمدة. يقرأ تقريرك المختبري ويُنظّم البيانات ويُنشئ شرحًا تعليميًا باللغة التي تختارها. للأغراض الرسمية أو القانونية، استشر مترجمًا طبيًا معتمدًا.",
            },
            {
                "q": "هل تؤثر اللغة على دقة التحليل؟",
                "a": "لا. التحليل الأساسي يعمل مع القيم الرقمية والوحدات والنطاقات المرجعية في تقريرك. لغة المستند الأصلي لا تؤثر على كيفية تحليل القيم أو تنظيمها.",
            },
            {
                "q": "ما اللغات المدعومة؟",
                "a": "يدعم NoryaAI حاليًا الإنجليزية والألمانية والتركية والفرنسية والإيطالية والإسبانية والعبرية والهندية والعربية. يتم إضافة المزيد من اللغات مع مرور الوقت.",
            },
            {
                "q": "هل يمكنني مشاركة التقرير مع طبيب يتحدث لغة مختلفة؟",
                "a": "نعم. يمكنك إنشاء نفس التقرير بعدة لغات إذا لزم الأمر. تنسيق PDF المنظّم مصمم ليكون واضحًا ومفيدًا بغض النظر عن الخلفية الطبية للقارئ.",
            },
            {
                "q": "هل NoryaAI بديل عن طبيبي؟",
                "a": "لا. NoryaAI يقدم شروحات منظّمة وتعليمية لمساعدتك في فهم نتائج مختبرك. لا يُشخّص ولا يُعالج ولا يصف أدوية. استشر دائمًا متخصصًا صحيًا مؤهلًا لاتخاذ القرارات الطبية.",
            },
        ],
        "cta_title": "مستعد لفهم نتائجك؟",
        "cta_sub": "ارفع فحص الدم الخاص بك بأي لغة واحصل على تقرير واضح ومنظّم باللغة التي تفضلها.",
        "cta_primary": "ارفع وحلّل الآن",
        "cta_secondary": "اعرض الأسعار",
        "internal_links": _internal_links("ar"),
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
