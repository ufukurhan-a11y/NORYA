"""Blood Test Results from Germany — guide page i18n."""
from __future__ import annotations

GERMANY_GUIDE_SLUGS = {
    "en": "blood-test-results-germany",
    "de": "blutwerte-aus-deutschland",
    "tr": "almanya-kan-tahlili-sonuclari",
}


def _en() -> dict:
    return {
        "meta_title": "Understanding Blood Test Results from Germany | NoryaAI",
        "meta_description": "Got a Blutbild or Laborwerte report from a German lab? Learn how to read German blood test results, common abbreviations, and how to get a structured English summary.",
        "badge": "Country Guide · Germany",
        "hero_title": "Understanding Blood Test Results from Germany",
        "hero_sub": "If you have received a Blutbild, großes Blutbild, or Laborwerte report from a German lab, this guide explains what the abbreviations mean, how German reference ranges work, and how to get a clear summary in English.",
        "sections": [
            {
                "title": "How blood tests work in Germany",
                "intro": None,
                "paragraphs": [
                    "In Germany, blood tests are typically ordered by your Hausarzt (family doctor) or a specialist and processed by certified labs (Labore). Results are usually returned as a printed or digital Laborbericht — a structured document listing each measured parameter, its value, the unit, and the reference range.",
                    "Most reports are written entirely in German, using abbreviations and terminology that can be difficult to navigate if German is not your first language. Even fluent speakers sometimes struggle with the medical vocabulary.",
                    "If you are an expat, international student, or someone who moved to Germany recently, understanding your Laborwerte can feel unnecessarily complicated — especially when you need to discuss the results with a doctor or share them with a physician in your home country.",
                ],
            },
            {
                "title": "Common German blood test abbreviations",
                "intro": "German lab reports use abbreviations that differ from the English-language conventions you may be used to. Here are the most frequently encountered ones.",
                "markers": [
                    {"name": "Kleines Blutbild", "abbr": "KBB", "desc": "The equivalent of a CBC (complete blood count). Includes red cells, white cells, hemoglobin, hematocrit, and platelets.", "range": None},
                    {"name": "Großes Blutbild", "abbr": "GBB", "desc": "An extended blood count that adds a white cell differential (neutrophils, lymphocytes, monocytes, eosinophils, basophils) to the kleines Blutbild.", "range": None},
                    {"name": "Erythrozyten", "abbr": "ERY", "desc": "Red blood cells (RBC). Measured in millions per microliter (Mio/µL or T/L).", "range": "4.1–5.9 Mio/µL (men) · 3.9–5.4 (women)"},
                    {"name": "Leukozyten", "abbr": "LEUK", "desc": "White blood cells (WBC). Reported in thousands per microliter (Tsd/µL or G/L).", "range": "4.0–10.0 Tsd/µL"},
                    {"name": "Hämoglobin", "abbr": "HB / HGB", "desc": "The oxygen-carrying protein in red blood cells. German labs typically report in g/dL, the same unit used in the US.", "range": "13.5–17.5 g/dL (men) · 12.0–16.0 (women)"},
                    {"name": "Hämatokrit", "abbr": "HKT / HCT", "desc": "The percentage of blood volume occupied by red blood cells.", "range": "40–54% (men) · 36–48% (women)"},
                    {"name": "Thrombozyten", "abbr": "THRO / PLT", "desc": "Platelets. Reported in thousands per microliter (Tsd/µL).", "range": "150–400 Tsd/µL"},
                    {"name": "Blutzucker (nüchtern)", "abbr": "GLU", "desc": "Fasting blood glucose. German labs commonly use mg/dL, though some use mmol/L.", "range": "70–100 mg/dL (fasting)"},
                    {"name": "Kreatinin", "abbr": "KREA", "desc": "Creatinine — a kidney function marker. Usually reported in mg/dL in Germany.", "range": "0.7–1.3 mg/dL (men) · 0.6–1.1 (women)"},
                    {"name": "Leberwerte", "abbr": "GOT / GPT / GGT", "desc": "Liver enzymes. GOT is AST, GPT is ALT, GGT is gamma-GT. These are the most commonly checked liver markers in German bloodwork.", "range": "GOT <50 U/L · GPT <50 U/L · GGT <60 U/L (men)"},
                ],
            },
            {
                "title": "Units and reference ranges in German labs",
                "intro": None,
                "paragraphs": [
                    "German labs generally use the same conventional units as US labs for most markers (mg/dL for glucose and creatinine, g/dL for hemoglobin). However, some labs report in SI units (mmol/L for glucose, µmol/L for creatinine), especially in academic hospital settings.",
                    "Reference ranges (Referenzbereiche or Normwerte) can differ slightly between German labs, just as they do worldwide. Your report will typically show the lab\u2019s own range next to each value. Values outside the range are often marked with an arrow (\u2191 for high, \u2193 for low) or printed in bold.",
                    "If you are comparing results from a German lab with previous results from another country, pay close attention to the units. NoryaAI\u2019s free unit converter can help you translate between measurement systems.",
                ],
            },
            {
                "title": "What makes German lab reports different",
                "intro": None,
                "points": [
                    {"title": "Language barrier", "desc": "All parameter names, explanations, and doctor comments are in German. Even common terms like Schilddrüse (thyroid), Nierenwerte (kidney values), or Blutfettwerte (blood lipids) can be hard to look up without medical context."},
                    {"title": "GOT/GPT instead of AST/ALT", "desc": "German labs traditionally use GOT (Glutamat-Oxalacetat-Transaminase) and GPT (Glutamat-Pyruvat-Transaminase) instead of the international AST/ALT nomenclature. Both refer to the same liver enzymes."},
                    {"title": "Structured Laborbericht format", "desc": "German lab reports are typically well-organized with clear columns for Messwert (measured value), Einheit (unit), and Referenzbereich (reference range). But the medical terminology can still be opaque."},
                    {"title": "Krankenkasse context", "desc": "In the German healthcare system, certain tests are covered by public insurance (gesetzliche Krankenversicherung) and others require private payment (IGeL). This affects which panels appear on your report and how results are communicated to you."},
                ],
            },
            {
                "title": "How to get your German results explained in English",
                "intro": None,
                "paragraphs": [
                    "If you have a Laborbericht from a German lab and want to understand it in English, you have a few options. You can ask your doctor to walk you through the results — but appointments are often short, and the explanation may still be in German.",
                    "You can try translating the report yourself, but general translators often miss medical nuance. \u201cErhöht\u201d means elevated, not just \u201cincreased,\u201d and \u201cauffällig\u201d means \u201cabnormal / notable,\u201d not just \u201cconspicuous.\u201d",
                    "NoryaAI offers a different approach: upload your German lab report (PDF or photo), and it extracts the values, matches them to reference ranges, and generates a structured summary in English (or any of 9+ languages). The output includes a health score, flagged markers, plain-language explanations, and a downloadable PDF you can bring to your next appointment — whether that is in Germany or your home country.",
                ],
            },
        ],
        "mid_cta_title": "Have a German lab report you want to understand?",
        "mid_cta_sub": "Upload your Blutbild or Laborwerte and get a structured English summary with reference ranges, flagged markers, and a health score.",
        "mid_cta_primary": "Upload your report",
        "mid_cta_secondary": "See a sample report",
        "faqs": [
            {
                "q": "Can I upload a lab report written in German?",
                "a": "Yes. NoryaAI can read lab reports in German (and other supported languages). It extracts the values, units, and reference ranges regardless of the document language and generates your structured summary in whichever language you choose.",
            },
            {
                "q": "What is the difference between a kleines and großes Blutbild?",
                "a": "A kleines Blutbild (small blood count) is equivalent to a standard CBC: red cells, white cells, hemoglobin, hematocrit, and platelets. A großes Blutbild (large blood count) adds a white cell differential, breaking WBC into neutrophils, lymphocytes, monocytes, eosinophils, and basophils.",
            },
            {
                "q": "Why does my German report say GOT/GPT instead of AST/ALT?",
                "a": "German labs traditionally use the older nomenclature: GOT (Glutamat-Oxalacetat-Transaminase) for AST and GPT (Glutamat-Pyruvat-Transaminase) for ALT. They measure the same liver enzymes. NoryaAI recognizes both naming conventions.",
            },
            {
                "q": "Do German labs use different units?",
                "a": "Most German labs use the same conventional units as US labs (mg/dL, g/dL, U/L). Some academic hospitals use SI units (mmol/L, µmol/L). Your report will show which units are used. NoryaAI handles both systems automatically.",
            },
            {
                "q": "Can I share my English report with my German doctor?",
                "a": "Yes. The NoryaAI report includes a structured PDF with reference ranges, flagged markers, and a health score. You can also generate the report in German if your doctor prefers. The format is designed to be useful in any clinical setting.",
            },
            {
                "q": "Is this a certified medical translation?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not provide certified medical translations. For official or legal purposes, consult a certified medical translator. Always discuss your results with a qualified healthcare professional.",
            },
        ],
        "cta_title": "Ready to understand your German lab report?",
        "cta_sub": "Upload your Blutbild or Laborwerte and get a clear, structured summary in English — in minutes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Understand Results in Your Language", "path": "/en/understand-blood-test-results-in-your-language"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "Unit Converter", "path": "/en/tools/unit-converter"},
            {"label": "Blutwerte verstehen (DE)", "path": "/de/blutwerte-verstehen"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }


def _de() -> dict:
    return {
        "meta_title": "Blutwerte aus Deutschland verstehen | NoryaAI",
        "meta_description": "Sie haben ein Blutbild oder einen Laborbericht aus einem deutschen Labor erhalten? Erfahren Sie, was die Abkürzungen bedeuten, wie Referenzbereiche funktionieren und wie Sie eine strukturierte Zusammenfassung erhalten.",
        "badge": "Länder-Ratgeber · Deutschland",
        "hero_title": "Blutwerte aus Deutschland verstehen",
        "hero_sub": "Sie haben ein Blutbild, großes Blutbild oder einen Laborbericht erhalten? Dieser Ratgeber erklärt die gängigen Abkürzungen, Referenzbereiche deutscher Labore und wie Sie eine klare, strukturierte Zusammenfassung Ihrer Werte erhalten.",
        "sections": [
            {
                "title": "Wie Blutuntersuchungen in Deutschland funktionieren",
                "intro": None,
                "paragraphs": [
                    "In Deutschland werden Blutuntersuchungen in der Regel vom Hausarzt oder einem Facharzt angeordnet und von akkreditierten Laboren (z.\u202fB. Synlab, Limbach, Labor Berlin) ausgewertet. Die Ergebnisse werden als gedruckter oder digitaler Laborbericht zurückgegeben — ein strukturiertes Dokument mit jedem gemessenen Parameter, seinem Wert, der Einheit und dem Referenzbereich.",
                    "Die meisten Berichte sind vollständig auf Deutsch verfasst und verwenden medizinische Abkürzungen und Fachbegriffe. Selbst Muttersprachler haben manchmal Schwierigkeiten mit der medizinischen Terminologie — besonders wenn es um die Interpretation der Ergebnisse geht.",
                    "Für viele Patienten — ob Expats, internationale Studierende oder Menschen, die erst kürzlich nach Deutschland gezogen sind — kann das Verstehen der eigenen Laborwerte unnötig kompliziert wirken, vor allem wenn die Ergebnisse mit einem Arzt im Heimatland besprochen werden sollen.",
                ],
            },
            {
                "title": "Häufige Abkürzungen im deutschen Blutbild",
                "intro": "Deutsche Laborberichte verwenden Abkürzungen, die sich von den englischsprachigen Konventionen unterscheiden. Hier sind die am häufigsten vorkommenden.",
                "markers": [
                    {"name": "Kleines Blutbild", "abbr": "KBB", "desc": "Entspricht dem CBC (Complete Blood Count): Erythrozyten, Leukozyten, Hämoglobin, Hämatokrit und Thrombozyten.", "range": None},
                    {"name": "Großes Blutbild", "abbr": "GBB", "desc": "Erweitertes Blutbild mit Differentialblutbild (Neutrophile, Lymphozyten, Monozyten, Eosinophile, Basophile) zusätzlich zum kleinen Blutbild.", "range": None},
                    {"name": "Erythrozyten", "abbr": "ERY", "desc": "Rote Blutkörperchen (RBC). Gemessen in Millionen pro Mikroliter (Mio/µL oder T/L).", "range": "4,1–5,9 Mio/µL (Männer) · 3,9–5,4 (Frauen)"},
                    {"name": "Leukozyten", "abbr": "LEUK", "desc": "Weiße Blutkörperchen (WBC). Angegeben in Tausend pro Mikroliter (Tsd/µL oder G/L).", "range": "4,0–10,0 Tsd/µL"},
                    {"name": "Hämoglobin", "abbr": "HB / HGB", "desc": "Das sauerstofftragende Protein in roten Blutkörperchen. Deutsche Labore geben den Wert in g/dL an.", "range": "13,5–17,5 g/dL (Männer) · 12,0–16,0 (Frauen)"},
                    {"name": "Hämatokrit", "abbr": "HKT / HCT", "desc": "Der Anteil der roten Blutkörperchen am Gesamtblutvolumen in Prozent.", "range": "40–54 % (Männer) · 36–48 % (Frauen)"},
                    {"name": "Thrombozyten", "abbr": "THRO / PLT", "desc": "Blutplättchen. Angegeben in Tausend pro Mikroliter (Tsd/µL).", "range": "150–400 Tsd/µL"},
                    {"name": "Blutzucker (nüchtern)", "abbr": "GLU", "desc": "Nüchternblutzucker. Deutsche Labore verwenden häufig mg/dL, manche auch mmol/L.", "range": "70–100 mg/dL (nüchtern)"},
                    {"name": "Kreatinin", "abbr": "KREA", "desc": "Kreatinin — ein Marker für die Nierenfunktion. In Deutschland meist in mg/dL angegeben.", "range": "0,7–1,3 mg/dL (Männer) · 0,6–1,1 (Frauen)"},
                    {"name": "Leberwerte", "abbr": "GOT / GPT / GGT", "desc": "Leberenzyme. GOT entspricht AST, GPT entspricht ALT, GGT ist Gamma-GT. Dies sind die am häufigsten überprüften Lebermarker.", "range": "GOT <50 U/L · GPT <50 U/L · GGT <60 U/L (Männer)"},
                ],
            },
            {
                "title": "Einheiten und Referenzbereiche deutscher Labore",
                "intro": None,
                "paragraphs": [
                    "Deutsche Labore verwenden für die meisten Marker die gleichen konventionellen Einheiten wie US-Labore (mg/dL für Glukose und Kreatinin, g/dL für Hämoglobin). Einige Labore — insbesondere an Universitätskliniken — berichten jedoch in SI-Einheiten (mmol/L für Glukose, µmol/L für Kreatinin).",
                    "Referenzbereiche (Normwerte) können zwischen verschiedenen deutschen Laboren leicht variieren, genau wie weltweit. Ihr Laborbericht zeigt in der Regel den laboreigenen Referenzbereich neben jedem Wert. Werte außerhalb des Bereichs werden oft mit einem Pfeil (↑ für hoch, ↓ für niedrig) oder fett markiert.",
                    "Wenn Sie Ergebnisse aus einem deutschen Labor mit früheren Ergebnissen aus einem anderen Land vergleichen, achten Sie genau auf die Einheiten. Der kostenlose Einheitenumrechner von NoryaAI kann Ihnen bei der Umrechnung helfen.",
                ],
            },
            {
                "title": "Was deutsche Laborberichte besonders macht",
                "intro": None,
                "points": [
                    {"title": "Sprachbarriere", "desc": "Alle Parameternamen, Erklärungen und ärztlichen Kommentare sind auf Deutsch. Selbst gängige Begriffe wie Schilddrüse, Nierenwerte oder Blutfettwerte können ohne medizinischen Kontext schwer zu verstehen sein."},
                    {"title": "GOT/GPT statt AST/ALT", "desc": "Deutsche Labore verwenden traditionell GOT (Glutamat-Oxalacetat-Transaminase) und GPT (Glutamat-Pyruvat-Transaminase) statt der internationalen AST/ALT-Nomenklatur. Beide bezeichnen die gleichen Leberenzyme."},
                    {"title": "Strukturiertes Laborbericht-Format", "desc": "Deutsche Laborberichte sind in der Regel gut strukturiert mit klaren Spalten für Messwert, Einheit und Referenzbereich. Die medizinische Terminologie kann dennoch schwer verständlich sein."},
                    {"title": "Krankenkasse und Kostenübernahme", "desc": "Im deutschen Gesundheitssystem werden bestimmte Untersuchungen von der gesetzlichen Krankenversicherung übernommen, andere sind individuelle Gesundheitsleistungen (IGeL) und müssen privat bezahlt werden. Dies beeinflusst, welche Parameter auf Ihrem Bericht erscheinen."},
                ],
            },
            {
                "title": "Wie Sie Ihre Blutwerte verständlich erklärt bekommen",
                "intro": None,
                "paragraphs": [
                    "Wenn Sie einen Laborbericht haben und Ihre Werte besser verstehen möchten, gibt es verschiedene Möglichkeiten. Sie können Ihren Arzt um eine Erklärung bitten — aber Termine sind oft kurz, und nicht alle Fragen lassen sich in wenigen Minuten klären.",
                    "Sie können versuchen, den Bericht selbst zu recherchieren, aber allgemeine Quellen erfassen oft nicht die medizinischen Nuancen. \u201eErhöht\u201c bedeutet nicht einfach \u201ehöher\u201c — es weist auf eine klinisch relevante Abweichung hin. \u201eAuffällig\u201c bedeutet \u201eaußerhalb des Normbereichs\u201c, nicht nur \u201emerkenswert\u201c.",
                    "NoryaAI bietet einen anderen Ansatz: Laden Sie Ihren Laborbericht (PDF oder Foto) hoch, und die KI extrahiert die Werte, vergleicht sie mit Referenzbereichen und erstellt eine strukturierte Zusammenfassung auf Deutsch (oder in 9+ weiteren Sprachen). Die Auswertung umfasst einen Gesundheitsscore, auffällige Marker, verständliche Erklärungen und ein herunterladbares PDF für Ihren nächsten Arzttermin.",
                ],
            },
        ],
        "mid_cta_title": "Haben Sie einen Laborbericht, den Sie verstehen möchten?",
        "mid_cta_sub": "Laden Sie Ihr Blutbild oder Ihre Laborwerte hoch und erhalten Sie eine strukturierte Zusammenfassung mit Referenzbereichen, auffälligen Markern und einem Gesundheitsscore.",
        "mid_cta_primary": "Bericht hochladen",
        "mid_cta_secondary": "Beispielbericht ansehen",
        "faqs": [
            {
                "q": "Kann ich einen Laborbericht auf Deutsch hochladen?",
                "a": "Ja. NoryaAI kann Laborberichte auf Deutsch (und in anderen unterstützten Sprachen) lesen. Es extrahiert die Werte, Einheiten und Referenzbereiche unabhängig von der Dokumentsprache und erstellt Ihre strukturierte Zusammenfassung in der Sprache Ihrer Wahl.",
            },
            {
                "q": "Was ist der Unterschied zwischen kleinem und großem Blutbild?",
                "a": "Ein kleines Blutbild entspricht einem Standard-CBC: Erythrozyten, Leukozyten, Hämoglobin, Hämatokrit und Thrombozyten. Ein großes Blutbild ergänzt dies um ein Differentialblutbild mit Neutrophilen, Lymphozyten, Monozyten, Eosinophilen und Basophilen.",
            },
            {
                "q": "Warum steht auf meinem Bericht GOT/GPT statt AST/ALT?",
                "a": "Deutsche Labore verwenden traditionell die ältere Nomenklatur: GOT (Glutamat-Oxalacetat-Transaminase) für AST und GPT (Glutamat-Pyruvat-Transaminase) für ALT. Es handelt sich um dieselben Leberenzyme. NoryaAI erkennt beide Benennungskonventionen.",
            },
            {
                "q": "Verwenden deutsche Labore andere Einheiten?",
                "a": "Die meisten deutschen Labore verwenden die gleichen konventionellen Einheiten wie US-Labore (mg/dL, g/dL, U/L). Einige Universitätskliniken nutzen SI-Einheiten (mmol/L, µmol/L). Ihr Bericht zeigt an, welche Einheiten verwendet werden. NoryaAI verarbeitet beide Systeme automatisch.",
            },
            {
                "q": "Kann ich meinen Bericht auch auf Englisch erhalten?",
                "a": "Ja. NoryaAI erstellt eine strukturierte Auswertung als PDF mit Referenzbereichen, auffälligen Markern und einem Gesundheitsscore. Sie können die Ausgabesprache frei wählen — ideal, wenn Sie den Bericht mit einem Arzt im Ausland teilen möchten.",
            },
            {
                "q": "Ist das eine zertifizierte medizinische Übersetzung?",
                "a": "Nein. NoryaAI bietet strukturierte, verständliche Erklärungen Ihrer Laborwerte. Es ersetzt keine zertifizierte medizinische Übersetzung. Für amtliche oder rechtliche Zwecke wenden Sie sich an einen zertifizierten Übersetzer. Besprechen Sie Ihre Ergebnisse immer mit einem qualifizierten Arzt.",
            },
        ],
        "cta_title": "Bereit, Ihren Laborbericht zu verstehen?",
        "cta_sub": "Laden Sie Ihr Blutbild oder Ihre Laborwerte hoch und erhalten Sie eine klare, strukturierte Zusammenfassung — in wenigen Minuten.",
        "cta_primary": "Jetzt hochladen und analysieren",
        "cta_secondary": "Preise ansehen",
        "internal_links": [
            {"label": "Blutwerte verstehen", "path": "/de/blutwerte-verstehen"},
            {"label": "Ergebnisse in deiner Sprache", "path": "/de/blutwerte-in-deiner-sprache"},
            {"label": "Blood Test Results Explained (EN)", "path": "/en/blood-test-results-explained"},
            {"label": "Einheitenumrechner", "path": "/en/tools/unit-converter"},
            {"label": "Preise", "path": "/pricing"},
            {"label": "Blog", "path": "/de/blog"},
        ],
    }


def _tr() -> dict:
    return {
        "meta_title": "Almanya'dan Kan Tahlili Sonuçlarını Anlama | NoryaAI",
        "meta_description": "Almanya'daki bir laboratuvardan Blutbild veya Laborwerte raporu mu aldınız? Alman kan tahlili sonuçlarını nasıl okuyacağınızı, yaygın kısaltmaları ve yapılandırılmış Türkçe özet almayı öğrenin.",
        "badge": "Ülke Rehberi · Almanya",
        "hero_title": "Almanya'dan Kan Tahlili Sonuçlarını Anlama",
        "hero_sub": "Bir Alman laboratuvarından Blutbild, großes Blutbild veya Laborwerte raporu aldıysanız, bu rehber kısaltmaların ne anlama geldiğini, Alman referans aralıklarının nasıl çalıştığını ve sonuçlarınızın Türkçe özetini nasıl alabileceğinizi açıklar.",
        "sections": [
            {
                "title": "Almanya'da kan tahlilleri nasıl çalışır?",
                "intro": None,
                "paragraphs": [
                    "Almanya'da kan tahlilleri genellikle Hausarzt (aile hekimi) veya bir uzman doktor tarafından istenir ve akredite laboratuvarlarda (Labore) değerlendirilir. Sonuçlar basılı veya dijital bir Laborbericht olarak iletilir — her ölçülen parametreyi, değerini, birimini ve referans aralığını listeleyen yapılandırılmış bir belge.",
                    "Raporların çoğu tamamen Almanca yazılmıştır ve Almanca ana diliniz değilse zor olabilecek kısaltmalar ve tıbbi terimler kullanır. Ana dili Almanca olanlar bile bazen tıbbi terminolojiyle zorlanabilir.",
                    "Almanya'ya yeni taşınan biri, uluslararası öğrenci veya gurbetçiyseniz, Laborwerte'nizi anlamak gereksiz yere karmaşık hissedebilir — özellikle sonuçları bir doktorla tartışmanız veya kendi ülkenizdeki bir hekimle paylaşmanız gerektiğinde.",
                ],
            },
            {
                "title": "Yaygın Alman kan tahlili kısaltmaları",
                "intro": "Alman laboratuvar raporları, alışık olabileceğiniz İngilizce dilindeki konvansiyonlardan farklı kısaltmalar kullanır. İşte en sık karşılaşılanlar.",
                "markers": [
                    {"name": "Kleines Blutbild", "abbr": "KBB", "desc": "CBC'nin (tam kan sayımı) karşılığı. Kırmızı hücreler, beyaz hücreler, hemoglobin, hematokrit ve trombositler dahildir.", "range": None},
                    {"name": "Großes Blutbild", "abbr": "GBB", "desc": "Kleines Blutbild'e beyaz hücre diferansiyeli (nötrofiller, lenfositler, monositler, eozinofiller, bazofiller) ekleyen genişletilmiş kan sayımı.", "range": None},
                    {"name": "Erythrozyten", "abbr": "ERY", "desc": "Kırmızı kan hücreleri (RBC). Mikrolitrede milyon olarak ölçülür (Mio/µL veya T/L).", "range": "4,1–5,9 Mio/µL (erkek) · 3,9–5,4 (kadın)"},
                    {"name": "Leukozyten", "abbr": "LEUK", "desc": "Beyaz kan hücreleri (WBC). Mikrolitrede bin olarak rapor edilir (Tsd/µL veya G/L).", "range": "4,0–10,0 Tsd/µL"},
                    {"name": "Hämoglobin", "abbr": "HB / HGB", "desc": "Kırmızı kan hücrelerindeki oksijen taşıyıcı protein. Alman laboratuvarları genellikle g/dL biriminde rapor eder.", "range": "13,5–17,5 g/dL (erkek) · 12,0–16,0 (kadın)"},
                    {"name": "Hämatokrit", "abbr": "HKT / HCT", "desc": "Kırmızı kan hücrelerinin toplam kan hacmindeki yüzdesi.", "range": "%40–54 (erkek) · %36–48 (kadın)"},
                    {"name": "Thrombozyten", "abbr": "THRO / PLT", "desc": "Trombositler (kan pulcukları). Mikrolitrede bin olarak rapor edilir (Tsd/µL).", "range": "150–400 Tsd/µL"},
                    {"name": "Blutzucker (nüchtern)", "abbr": "GLU", "desc": "Açlık kan şekeri. Alman laboratuvarları genellikle mg/dL kullanır, bazıları mmol/L kullanır.", "range": "70–100 mg/dL (açlık)"},
                    {"name": "Kreatinin", "abbr": "KREA", "desc": "Kreatinin — böbrek fonksiyonu belirteci. Almanya'da genellikle mg/dL olarak rapor edilir.", "range": "0,7–1,3 mg/dL (erkek) · 0,6–1,1 (kadın)"},
                    {"name": "Leberwerte", "abbr": "GOT / GPT / GGT", "desc": "Karaciğer enzimleri. GOT = AST, GPT = ALT, GGT = gamma-GT. Alman kan tahlillerinde en sık kontrol edilen karaciğer belirteçleridir.", "range": "GOT <50 U/L · GPT <50 U/L · GGT <60 U/L (erkek)"},
                ],
            },
            {
                "title": "Alman laboratuvarlarında birimler ve referans aralıkları",
                "intro": None,
                "paragraphs": [
                    "Alman laboratuvarları çoğu belirteç için ABD laboratuvarlarıyla aynı geleneksel birimleri kullanır (glukoz ve kreatinin için mg/dL, hemoglobin için g/dL). Ancak bazı laboratuvarlar — özellikle üniversite hastanelerinde — SI birimlerini kullanır (glukoz için mmol/L, kreatinin için µmol/L).",
                    "Referans aralıkları (Referenzbereiche veya Normwerte) Alman laboratuvarları arasında hafif farklılık gösterebilir, tıpkı dünya genelinde olduğu gibi. Raporunuz genellikle her değerin yanında laboratuvarın kendi aralığını gösterir. Aralık dışındaki değerler genellikle bir okla (↑ yüksek, ↓ düşük) veya kalın yazıyla işaretlenir.",
                    "Bir Alman laboratuvarındaki sonuçları başka bir ülkedeki önceki sonuçlarla karşılaştırıyorsanız birimlere dikkat edin. NoryaAI'nin ücretsiz birim dönüştürücüsü ölçüm sistemleri arasında çeviri yapmanıza yardımcı olabilir.",
                ],
            },
            {
                "title": "Alman laboratuvar raporlarını farklı kılan nedir?",
                "intro": None,
                "points": [
                    {"title": "Dil bariyeri", "desc": "Tüm parametre adları, açıklamalar ve doktor yorumları Almancadır. Schilddrüse (tiroid), Nierenwerte (böbrek değerleri) veya Blutfettwerte (kan yağları) gibi yaygın terimler bile tıbbi bağlam olmadan anlaşılması zor olabilir."},
                    {"title": "AST/ALT yerine GOT/GPT", "desc": "Alman laboratuvarları geleneksel olarak uluslararası AST/ALT nomenklatürü yerine GOT (Glutamat-Oxalacetat-Transaminase) ve GPT (Glutamat-Pyruvat-Transaminase) kullanır. Her ikisi de aynı karaciğer enzimlerini ifade eder."},
                    {"title": "Yapılandırılmış Laborbericht formatı", "desc": "Alman laboratuvar raporları genellikle Messwert (ölçülen değer), Einheit (birim) ve Referenzbereich (referans aralığı) için net sütunlarla iyi organize edilmiştir. Ancak tıbbi terminoloji yine de anlaşılması zor olabilir."},
                    {"title": "Krankenkasse bağlamı", "desc": "Alman sağlık sisteminde bazı testler kamu sigortası (gesetzliche Krankenversicherung) kapsamında karşılanırken diğerleri özel ödeme (IGeL) gerektirir. Bu, raporunuzda hangi panellerin göründüğünü ve sonuçların size nasıl iletildiğini etkiler."},
                ],
            },
            {
                "title": "Alman tahlil sonuçlarınızı Türkçe nasıl anlayabilirsiniz?",
                "intro": None,
                "paragraphs": [
                    "Bir Alman laboratuvarından Laborbericht'iniz varsa ve Türkçe olarak anlamak istiyorsanız birkaç seçeneğiniz var. Doktorunuzdan sonuçları açıklamasını isteyebilirsiniz — ancak randevular genellikle kısa sürer ve açıklama Almanca olabilir.",
                    "Raporu kendiniz çevirmeyi deneyebilirsiniz, ancak genel çevirmenler genellikle tıbbi nüansları kaçırır. \u201eErhöht\u201c sadece \u201eartmış\u201c değil, \u201eyükselmiş\u201c anlamına gelir; \u201eauffällig\u201c sadece \u201edikkat çekici\u201c değil, \u201eanormal / dikkate değer\u201c anlamına gelir.",
                    "NoryaAI farklı bir yaklaşım sunar: Alman laboratuvar raporunuzu (PDF veya fotoğraf) yükleyin, değerler otomatik olarak çıkarılır, referans aralıklarıyla eşleştirilir ve Türkçe (veya 9+ dilde) yapılandırılmış bir özet oluşturulur. Çıktı, sağlık skoru, işaretlenmiş belirteçler, anlaşılır açıklamalar ve bir sonraki randevunuza götürebileceğiniz indirilebilir bir PDF içerir.",
                ],
            },
        ],
        "mid_cta_title": "Anlamak istediğiniz bir Alman laboratuvar raporunuz mu var?",
        "mid_cta_sub": "Blutbild veya Laborwerte raporunuzu yükleyin, referans aralıkları, işaretlenmiş belirteçler ve sağlık skoru içeren yapılandırılmış bir Türkçe özet alın.",
        "mid_cta_primary": "Raporunuzu yükleyin",
        "mid_cta_secondary": "Örnek rapor görün",
        "faqs": [
            {
                "q": "Almanca yazılmış bir laboratuvar raporu yükleyebilir miyim?",
                "a": "Evet. NoryaAI, Almanca (ve diğer desteklenen dillerde) yazılmış laboratuvar raporlarını okuyabilir. Belge dilinden bağımsız olarak değerleri, birimleri ve referans aralıklarını çıkarır ve yapılandırılmış özetinizi seçtiğiniz dilde oluşturur.",
            },
            {
                "q": "Kleines ve großes Blutbild arasındaki fark nedir?",
                "a": "Kleines Blutbild (küçük kan sayımı) standart bir CBC'ye karşılık gelir: kırmızı hücreler, beyaz hücreler, hemoglobin, hematokrit ve trombositler. Großes Blutbild (büyük kan sayımı) buna beyaz hücre diferansiyeli ekler: nötrofiller, lenfositler, monositler, eozinofiller ve bazofiller.",
            },
            {
                "q": "Alman raporumda neden AST/ALT yerine GOT/GPT yazıyor?",
                "a": "Alman laboratuvarları geleneksel olarak eski isimlendirmeyi kullanır: AST için GOT (Glutamat-Oxalacetat-Transaminase) ve ALT için GPT (Glutamat-Pyruvat-Transaminase). Aynı karaciğer enzimlerini ölçerler. NoryaAI her iki isimlendirme kuralını da tanır.",
            },
            {
                "q": "Alman laboratuvarları farklı birimler mi kullanır?",
                "a": "Çoğu Alman laboratuvarı ABD laboratuvarlarıyla aynı geleneksel birimleri kullanır (mg/dL, g/dL, U/L). Bazı üniversite hastaneleri SI birimleri kullanır (mmol/L, µmol/L). Raporunuz hangi birimlerin kullanıldığını gösterir. NoryaAI her iki sistemi de otomatik olarak işler.",
            },
            {
                "q": "Türkçe raporumu Almanya'daki doktorumla paylaşabilir miyim?",
                "a": "Evet. NoryaAI raporu referans aralıkları, işaretlenmiş belirteçler ve sağlık skoru içeren yapılandırılmış bir PDF içerir. Doktorunuz tercih ederse raporu Almanca da oluşturabilirsiniz. Format herhangi bir klinik ortamda kullanılabilecek şekilde tasarlanmıştır.",
            },
            {
                "q": "Bu sertifikalı bir tıbbi çeviri mi?",
                "a": "Hayır. NoryaAI, laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Sertifikalı tıbbi çeviri sağlamaz. Resmi veya yasal amaçlar için sertifikalı bir tıbbi çevirmene başvurun. Sonuçlarınızı her zaman nitelikli bir sağlık uzmanıyla görüşün.",
            },
        ],
        "cta_title": "Alman laboratuvar raporunuzu anlamaya hazır mısınız?",
        "cta_sub": "Blutbild veya Laborwerte raporunuzu yükleyin ve dakikalar içinde net, yapılandırılmış bir Türkçe özet alın.",
        "cta_primary": "Şimdi yükle ve analiz et",
        "cta_secondary": "Fiyatları gör",
        "internal_links": [
            {"label": "Kan Tahlili Sonuçları", "path": "/tr/kan-tahlili-sonucu"},
            {"label": "Kendi Dilinde Anla", "path": "/tr/kan-tahlili-kendi-dilinde"},
            {"label": "Tahlil Yükle", "path": "/tr/kan-tahlili-yukle"},
            {"label": "Birim Dönüştürücü", "path": "/en/tools/unit-converter"},
            {"label": "Fiyatlar", "path": "/pricing"},
            {"label": "Blog", "path": "/tr/blog"},
        ],
    }


_CONTENT = {"en": _en(), "de": _de(), "tr": _tr()}


def get_germany_guide_content(lang: str) -> dict:
    return _CONTENT.get(lang, _CONTENT["en"])


def get_germany_guide_slug(lang: str) -> str:
    return GERMANY_GUIDE_SLUGS.get(lang, GERMANY_GUIDE_SLUGS["en"])
