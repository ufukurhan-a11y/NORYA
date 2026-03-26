# -*- coding: utf-8 -*-
"""Upload Blood Test Results — landing page i18n content for all supported locales."""
from __future__ import annotations

UPLOAD_SLUGS: dict[str, str] = {
    "en": "upload-blood-test-results",
    "tr": "kan-tahlili-yukle",
    "de": "bluttest-hochladen",
    "es": "upload-blood-test-results",
    "fr": "upload-blood-test-results",
    "it": "upload-blood-test-results",
    "he": "upload-blood-test-results",
    "hi": "upload-blood-test-results",
    "ar": "upload-blood-test-results",
}


def _en() -> dict:
    return {
        "meta_title": "Upload Blood Test Results | PDF, Photo, or Text | NoryaAI",
        "meta_description": "Upload blood test results from any lab as a PDF, photo, or pasted text and get a structured report with reference ranges, flagged markers, and a doctor-ready summary.",
        "hero_title": "Upload Blood Test Results and Get a Clear AI Report",
        "hero_sub": "Upload a blood test PDF, snap a photo of your lab report, or paste your values directly. NoryaAI turns raw lab data into a structured report with reference ranges, highlighted findings, and a doctor-ready summary.",
        "hero_trust": "Encrypted upload · GDPR & KVKK compliant · No data sharing",
        "cta_hero_primary": "Upload and analyze now",
        "cta_hero_secondary": "View sample report",
        "formats_title": "Supported upload formats",
        "formats_sub": "Choose the upload method that matches your lab report format. Every option leads to the same structured interpretation.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "PDF lab reports",
                "desc": "Upload the PDF you received from your lab or hospital. NoryaAI reads tables, values, and reference ranges directly from the document.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "Photos & screenshots",
                "desc": "Take a photo of your printed report or screenshot your online lab portal. JPG and PNG files are supported.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "Pasted text",
                "desc": "No file? Copy and paste your lab values directly. NoryaAI will structure them into a complete report.",
            },
        ],
        "steps_title": "What happens after you upload",
        "steps_sub": "From file upload to a structured blood test interpretation, the full flow usually takes only a few minutes.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Upload your report",
                "desc": "Choose a PDF, photo, or paste your lab values into the analysis form.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI reads your data",
                "desc": "Values, units, and reference ranges are extracted and structured automatically.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Structured summary",
                "desc": "Health score, category breakdown, and flagged markers — all in one clear view.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Download your report",
                "desc": "Get a doctor-ready PDF you can print, save, or share at your next appointment.",
            },
        ],
        "reasons_title": "Why people upload blood test results to NoryaAI",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "Before a doctor visit",
                "desc": "Arrive at your appointment with a clear, organized summary of your blood test. It helps you ask better questions and makes the conversation more productive.",
            },
            {
                "icon": "\U0001f310",
                "title": "Reports in another language",
                "desc": "Got lab results in a language you do not fully understand? Upload them and get a structured explanation in your preferred language — 9+ languages supported.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "To understand a complex report",
                "desc": "Pages of lab data can be overwhelming. NoryaAI turns them into a categorized, easy-to-read breakdown with reference ranges, flagged markers, and clear explanations.",
            },
        ],
        "trust_title": "Your data stays yours",
        "trust_sub": "Privacy is not an afterthought. It is built into every step of the upload and analysis process.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "Encrypted in transit and at rest"},
            {"icon": "\U0001f6e1\ufe0f", "text": "GDPR & KVKK compliant"},
            {"icon": "\U0001f6ab", "text": "Never shared or sold"},
            {"icon": "\U0001f504", "text": "Not used for model training"},
        ],
        "preview_title": "What your uploaded blood test report looks like",
        "preview_sub": "Here is a glimpse of the structured output you receive after uploading blood test results to NoryaAI.",
        "preview_lines": [
            {"label": "Health Score", "value": "78 / 100 — Good overall, a few markers to watch"},
            {"label": "Hemoglobin", "value": "14.2 g/dL — Within normal range (13.5–17.5)"},
            {"label": "Glucose", "value": "108 mg/dL — Slightly elevated (normal: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — Normal thyroid function (0.4–4.0)"},
            {"label": "Vitamin D", "value": "18 ng/mL — Below recommended level (30–100)"},
        ],
        "preview_disclaimer": "Sample data for illustration only. Your actual report will reflect your personal lab values, units, and reference ranges.",
        "preview_link": "See a full sample report →",
        "faqs": [
            {
                "q": "What file formats can I upload?",
                "a": "NoryaAI accepts PDF files, JPG/JPEG images, and PNG images. You can also paste your lab values as text if you do not have a file to upload.",
            },
            {
                "q": "Can I upload blood test results from any lab?",
                "a": "Yes. You can upload blood test results from hospitals, private labs, checkup providers, and international lab portals. NoryaAI works with PDFs, photos, screenshots, and pasted text from many report layouts.",
            },
            {
                "q": "How long does the analysis take?",
                "a": "Most reports are processed in under two minutes. Complex multi-page PDFs may take slightly longer, but you will see your structured summary shortly after uploading.",
            },
            {
                "q": "Is my uploaded report stored or shared?",
                "a": "Your uploaded file is used only to generate your report. All data is encrypted in transit and at rest, never shared with third parties, and never used for model training. NoryaAI is GDPR and KVKK compliant.",
            },
            {
                "q": "Do I need to create an account to upload?",
                "a": "You can start an analysis without creating an account. An account lets you save your reports, track results over time, and access them from any device.",
            },
            {
                "q": "Can I upload reports in languages other than English?",
                "a": "Yes. NoryaAI can read lab reports in multiple languages and generate your structured summary in any of 9+ supported languages, including English, German, Turkish, French, Italian, Spanish, Hebrew, Hindi, and Arabic.",
            },
            {
                "q": "Is NoryaAI a replacement for my doctor?",
                "a": "No. NoryaAI provides structured, educational explanations of your lab values to help you understand your results better. It does not diagnose, treat, or prescribe. Always consult a qualified healthcare professional for medical decisions.",
            },
        ],
        "cta_title": "Ready to upload your blood test?",
        "cta_sub": "Upload blood test results from any lab and get a structured, doctor-ready report in minutes. PDF, photo, or pasted text all work.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
    }


def _tr() -> dict:
    return {
        "meta_title": "Kan Tahlili Yükle — Yapay Zekâ Destekli Analiz | NoryaAI",
        "meta_description": "Kan tahlili PDF'inizi, fotoğrafınızı veya laboratuvar raporunuzu yükleyin; referans aralıkları, sağlık puanı ve işaretlenmiş değerlerle yapılandırılmış, doktora hazır bir özet alın.",
        "hero_title": "Kan Tahlili Sonuçlarınızı Yükleyin",
        "hero_sub": "PDF yükleyin, fotoğraf çekin veya laboratuvar değerlerinizi yapıştırın. NoryaAI kan tahlilinizi referans aralıkları, işaretlenmiş değerler ve sağlık puanı içeren yapılandırılmış, kolay okunur bir rapora dönüştürür.",
        "hero_trust": "Şifreli yükleme · GDPR ve KVKK uyumlu · Veri paylaşımı yok",
        "cta_hero_primary": "Analize başla",
        "cta_hero_secondary": "Örnek raporu gör",
        "formats_title": "Desteklenen yükleme formatları",
        "formats_sub": "Sizin için en kolay yöntemi seçin — üçü de aynı yapılandırılmış raporu üretir.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "PDF laboratuvar raporları",
                "desc": "Laboratuvarınızdan veya hastanenizden aldığınız PDF'i yükleyin. NoryaAI tabloları, değerleri ve referans aralıklarını doğrudan belgeden okur.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "Fotoğraf ve ekran görüntüleri",
                "desc": "Basılı raporunuzun fotoğrafını çekin veya çevrimiçi laboratuvar portalınızın ekran görüntüsünü alın. JPG ve PNG dosyaları desteklenir.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "Yapıştırılmış metin",
                "desc": "Dosyanız yok mu? Laboratuvar değerlerinizi doğrudan kopyalayıp yapıştırın. NoryaAI bunları eksiksiz bir rapora dönüştürür.",
            },
        ],
        "steps_title": "Yükledikten sonra ne olur",
        "steps_sub": "Yüklemeden yapılandırılmış rapora — tüm süreç yalnızca birkaç dakika sürer.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Raporunuzu yükleyin",
                "desc": "Bir PDF, fotoğraf seçin veya laboratuvar değerlerinizi analiz formuna yapıştırın.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "Yapay zekâ verilerinizi okur",
                "desc": "Değerler, birimler ve referans aralıkları otomatik olarak çıkarılır ve yapılandırılır.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Yapılandırılmış özet",
                "desc": "Sağlık puanı, kategori dökümü ve işaretlenmiş değerler — hepsi tek bir görünümde.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Raporunuzu indirin",
                "desc": "Bir sonraki randevunuzda yazdırabileceğiniz, kaydedebileceğiniz veya paylaşabileceğiniz doktora hazır bir PDF alın.",
            },
        ],
        "reasons_title": "İnsanlar neden sonuçlarını buraya yüklüyor",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "Doktor ziyaretinden önce",
                "desc": "Randevunuza açık ve düzenli bir özetle gidin. Daha iyi sorular sormanıza yardımcı olur ve görüşmeyi daha verimli hale getirir.",
            },
            {
                "icon": "\U0001f310",
                "title": "Başka bir dildeki raporlar",
                "desc": "Tam olarak anlamadığınız bir dilde laboratuvar sonuçlarınız mı var? Yükleyin ve tercih ettiğiniz dilde yapılandırılmış bir açıklama alın — 9'dan fazla dil desteklenir.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "Karmaşık bir raporu anlamak için",
                "desc": "Sayfalarca laboratuvar verisi bunaltıcı olabilir. NoryaAI bunları referans aralıkları ve net açıklamalarla kategorize edilmiş, kolay okunur bir dökümüne dönüştürür.",
            },
        ],
        "trust_title": "Verileriniz sizin kalır",
        "trust_sub": "Gizlilik sonradan düşünülmüş bir şey değildir. Yükleme ve analiz sürecinin her adımına yerleştirilmiştir.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "İletim sırasında ve beklemede şifreli"},
            {"icon": "\U0001f6e1\ufe0f", "text": "GDPR ve KVKK uyumlu"},
            {"icon": "\U0001f6ab", "text": "Asla paylaşılmaz veya satılmaz"},
            {"icon": "\U0001f504", "text": "Model eğitimi için kullanılmaz"},
        ],
        "preview_title": "Raporunuz nasıl görünür",
        "preview_sub": "Kan tahlilinizi yükledikten sonra aldığınız yapılandırılmış çıktının bir önizlemesi.",
        "preview_lines": [
            {"label": "Sağlık Puanı", "value": "78 / 100 — Genel olarak iyi, izlenmesi gereken birkaç değer"},
            {"label": "Hemoglobin", "value": "14.2 g/dL — Normal aralıkta (13.5–17.5)"},
            {"label": "Glukoz", "value": "108 mg/dL — Hafif yüksek (normal: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — Normal tiroid fonksiyonu (0.4–4.0)"},
            {"label": "D Vitamini", "value": "18 ng/mL — Önerilen seviyenin altında (30–100)"},
        ],
        "preview_disclaimer": "Yalnızca gösterim amaçlı örnek verilerdir. Gerçek raporunuz kişisel laboratuvar değerlerinizi, birimlerinizi ve referans aralıklarınızı yansıtacaktır.",
        "preview_link": "Tam örnek raporu gör →",
        "faqs": [
            {
                "q": "Hangi dosya formatlarını yükleyebilirim?",
                "a": "NoryaAI; PDF dosyalarını, JPG/JPEG görsellerini ve PNG görsellerini kabul eder. Yükleyecek bir dosyanız yoksa laboratuvar değerlerinizi metin olarak da yapıştırabilirsiniz.",
            },
            {
                "q": "Analiz ne kadar sürer?",
                "a": "Çoğu rapor iki dakikadan kısa sürede işlenir. Karmaşık çok sayfalı PDF'ler biraz daha uzun sürebilir, ancak yükledikten kısa süre sonra yapılandırılmış özetinizi göreceksiniz.",
            },
            {
                "q": "Yüklenen raporum saklanıyor veya paylaşılıyor mu?",
                "a": "Yüklenen dosyanız yalnızca raporunuzu oluşturmak için kullanılır. Tüm veriler iletim sırasında ve beklemede şifrelenir, üçüncü taraflarla asla paylaşılmaz ve model eğitimi için kullanılmaz. NoryaAI, GDPR ve KVKK uyumludur.",
            },
            {
                "q": "İngilizce dışındaki dillerdeki raporları yükleyebilir miyim?",
                "a": "Evet. NoryaAI birden fazla dildeki laboratuvar raporlarını okuyabilir ve yapılandırılmış özetinizi İngilizce, Almanca, Türkçe, Fransızca, İtalyanca, İspanyolca, İbranice, Hintçe ve Arapça dahil 9'dan fazla desteklenen dilden herhangi birinde oluşturabilir.",
            },
            {
                "q": "Yüklemek için hesap oluşturmam gerekiyor mu?",
                "a": "Hesap oluşturmadan analiz başlatabilirsiniz. Hesap açmak raporlarınızı kaydetmenize, sonuçları zaman içinde takip etmenize ve herhangi bir cihazdan erişmenize olanak tanır.",
            },
            {
                "q": "NoryaAI doktorumun yerini alır mı?",
                "a": "Hayır. NoryaAI, sonuçlarınızı daha iyi anlamanıza yardımcı olmak için laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Teşhis koymaz, tedavi önermez veya ilaç yazmaz. Tıbbi kararlar için her zaman nitelikli bir sağlık uzmanına danışın.",
            },
        ],
        "cta_title": "Kan tahlilinizi yüklemeye hazır mısınız?",
        "cta_sub": "Dakikalar içinde yapılandırılmış, doktora hazır bir rapor alın. PDF, fotoğraf veya yapıştırılmış metin — tercih sizin.",
        "cta_primary": "Yükle ve analiz et",
        "cta_secondary": "Fiyatları gör",
    }


def _de() -> dict:
    return {
        "meta_title": "Bluttest hochladen — KI-gestützte Analyse | NoryaAI",
        "meta_description": "Laden Sie Ihr Blutbild als PDF, Foto oder Laborbericht hoch und erhalten Sie eine strukturierte, arztfertige Zusammenfassung mit Referenzbereichen, Gesundheitsscore und markierten Werten.",
        "hero_title": "Laden Sie Ihre Blutwerte hoch",
        "hero_sub": "Laden Sie ein PDF hoch, machen Sie ein Foto oder fügen Sie Ihre Laborwerte ein. NoryaAI verwandelt Ihr Blutbild in einen strukturierten, leicht lesbaren Bericht mit Referenzbereichen, markierten Werten und einem Gesundheitsscore.",
        "hero_trust": "Verschlüsselter Upload · DSGVO- und KVKK-konform · Keine Datenweitergabe",
        "cta_hero_primary": "Analyse starten",
        "cta_hero_secondary": "Beispielbericht ansehen",
        "formats_title": "Unterstützte Upload-Formate",
        "formats_sub": "Wählen Sie die Methode, die für Sie am einfachsten ist — alle drei erzeugen denselben strukturierten Bericht.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "PDF-Laborberichte",
                "desc": "Laden Sie das PDF hoch, das Sie von Ihrem Labor oder Krankenhaus erhalten haben. NoryaAI liest Tabellen, Werte und Referenzbereiche direkt aus dem Dokument.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "Fotos und Screenshots",
                "desc": "Fotografieren Sie Ihren gedruckten Befund oder machen Sie einen Screenshot Ihres Online-Laborportals. JPG- und PNG-Dateien werden unterstützt.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "Eingefügter Text",
                "desc": "Keine Datei? Kopieren Sie Ihre Laborwerte und fügen Sie sie direkt ein. NoryaAI strukturiert sie zu einem vollständigen Bericht.",
            },
        ],
        "steps_title": "Was nach dem Hochladen passiert",
        "steps_sub": "Vom Upload zum strukturierten Bericht — der gesamte Vorgang dauert nur wenige Minuten.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Bericht hochladen",
                "desc": "Wählen Sie ein PDF, ein Foto oder fügen Sie Ihre Laborwerte in das Analyseformular ein.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "KI liest Ihre Daten",
                "desc": "Werte, Einheiten und Referenzbereiche werden automatisch extrahiert und strukturiert.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Strukturierte Zusammenfassung",
                "desc": "Gesundheitsscore, Kategorieübersicht und markierte Werte — alles auf einen Blick.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Bericht herunterladen",
                "desc": "Erhalten Sie ein arztfertiges PDF, das Sie ausdrucken, speichern oder bei Ihrem nächsten Termin teilen können.",
            },
        ],
        "reasons_title": "Warum Menschen ihre Ergebnisse hier hochladen",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "Vor einem Arztbesuch",
                "desc": "Kommen Sie mit einer klaren, übersichtlichen Zusammenfassung zu Ihrem Termin. Das hilft Ihnen, bessere Fragen zu stellen und das Gespräch produktiver zu gestalten.",
            },
            {
                "icon": "\U0001f310",
                "title": "Berichte in einer anderen Sprache",
                "desc": "Haben Sie Laborergebnisse in einer Sprache, die Sie nicht vollständig verstehen? Laden Sie sie hoch und erhalten Sie eine strukturierte Erklärung in Ihrer bevorzugten Sprache — über 9 Sprachen werden unterstützt.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "Einen komplexen Befund verstehen",
                "desc": "Seitenweise Labordaten können überwältigend sein. NoryaAI verwandelt sie in eine kategorisierte, leicht lesbare Aufschlüsselung mit Referenzbereichen und klaren Erklärungen.",
            },
        ],
        "trust_title": "Ihre Daten bleiben Ihre",
        "trust_sub": "Datenschutz ist kein nachträglicher Gedanke. Er ist in jeden Schritt des Upload- und Analyseprozesses integriert.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "Verschlüsselt bei Übertragung und Speicherung"},
            {"icon": "\U0001f6e1\ufe0f", "text": "DSGVO- und KVKK-konform"},
            {"icon": "\U0001f6ab", "text": "Wird niemals geteilt oder verkauft"},
            {"icon": "\U0001f504", "text": "Wird nicht für Modelltraining verwendet"},
        ],
        "preview_title": "So sieht Ihr Bericht aus",
        "preview_sub": "Hier ein Einblick in die strukturierte Ausgabe, die Sie nach dem Hochladen Ihres Bluttests erhalten.",
        "preview_lines": [
            {"label": "Gesundheitsscore", "value": "78 / 100 — Insgesamt gut, einige Werte im Blick behalten"},
            {"label": "Hämoglobin", "value": "14.2 g/dL — Im Normalbereich (13.5–17.5)"},
            {"label": "Glukose", "value": "108 mg/dL — Leicht erhöht (normal: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — Normale Schilddrüsenfunktion (0.4–4.0)"},
            {"label": "Vitamin D", "value": "18 ng/mL — Unter dem empfohlenen Wert (30–100)"},
        ],
        "preview_disclaimer": "Beispieldaten nur zur Veranschaulichung. Ihr tatsächlicher Bericht spiegelt Ihre persönlichen Laborwerte, Einheiten und Referenzbereiche wider.",
        "preview_link": "Vollständigen Beispielbericht ansehen →",
        "faqs": [
            {
                "q": "Welche Dateiformate kann ich hochladen?",
                "a": "NoryaAI akzeptiert PDF-Dateien, JPG/JPEG-Bilder und PNG-Bilder. Sie können Ihre Laborwerte auch als Text einfügen, wenn Sie keine Datei zum Hochladen haben.",
            },
            {
                "q": "Wie lange dauert die Analyse?",
                "a": "Die meisten Berichte werden in weniger als zwei Minuten verarbeitet. Komplexe mehrseitige PDFs können etwas länger dauern, aber Sie sehen Ihre strukturierte Zusammenfassung kurz nach dem Hochladen.",
            },
            {
                "q": "Wird mein hochgeladener Bericht gespeichert oder weitergegeben?",
                "a": "Ihre hochgeladene Datei wird ausschließlich zur Erstellung Ihres Berichts verwendet. Alle Daten werden bei Übertragung und Speicherung verschlüsselt, niemals an Dritte weitergegeben und nicht für Modelltraining verwendet. NoryaAI ist DSGVO- und KVKK-konform.",
            },
            {
                "q": "Kann ich Berichte in anderen Sprachen als Englisch hochladen?",
                "a": "Ja. NoryaAI kann Laborberichte in mehreren Sprachen lesen und Ihre strukturierte Zusammenfassung in jeder der über 9 unterstützten Sprachen erstellen, darunter Englisch, Deutsch, Türkisch, Französisch, Italienisch, Spanisch, Hebräisch, Hindi und Arabisch.",
            },
            {
                "q": "Muss ich ein Konto erstellen, um hochzuladen?",
                "a": "Sie können eine Analyse starten, ohne ein Konto zu erstellen. Ein Konto ermöglicht es Ihnen, Berichte zu speichern, Ergebnisse über die Zeit zu verfolgen und von jedem Gerät darauf zuzugreifen.",
            },
            {
                "q": "Ist NoryaAI ein Ersatz für meinen Arzt?",
                "a": "Nein. NoryaAI bietet strukturierte, lehrreiche Erklärungen Ihrer Laborwerte, um Ihnen zu helfen, Ihre Ergebnisse besser zu verstehen. Es diagnostiziert nicht, behandelt nicht und verschreibt nichts. Konsultieren Sie für medizinische Entscheidungen immer einen qualifizierten Arzt.",
            },
        ],
        "cta_title": "Bereit, Ihren Bluttest hochzuladen?",
        "cta_sub": "Erhalten Sie in wenigen Minuten einen strukturierten, arztfertigen Bericht. PDF, Foto oder eingefügter Text — Sie entscheiden.",
        "cta_primary": "Hochladen und analysieren",
        "cta_secondary": "Preise ansehen",
    }


def _es() -> dict:
    return {
        "meta_title": "Subir análisis de sangre — Análisis con IA | NoryaAI",
        "meta_description": "Suba su análisis de sangre en PDF, foto o informe de laboratorio y obtenga un resumen estructurado con rangos de referencia, puntuación de salud y marcadores señalados.",
        "hero_title": "Suba sus resultados de análisis de sangre",
        "hero_sub": "Suba un PDF, tome una foto o pegue sus valores de laboratorio. NoryaAI convierte su análisis de sangre en un informe estructurado y fácil de leer con rangos de referencia, marcadores señalados y una puntuación de salud.",
        "hero_trust": "Carga cifrada · Cumple con RGPD y KVKK · Sin compartir datos",
        "cta_hero_primary": "Iniciar análisis",
        "cta_hero_secondary": "Ver informe de ejemplo",
        "formats_title": "Formatos de carga admitidos",
        "formats_sub": "Elija el método más cómodo para usted — los tres producen el mismo informe estructurado.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "Informes de laboratorio en PDF",
                "desc": "Suba el PDF que recibió de su laboratorio u hospital. NoryaAI lee tablas, valores y rangos de referencia directamente del documento.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "Fotos y capturas de pantalla",
                "desc": "Tome una foto de su informe impreso o una captura de pantalla de su portal de laboratorio en línea. Se admiten archivos JPG y PNG.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "Texto pegado",
                "desc": "¿No tiene archivo? Copie y pegue sus valores de laboratorio directamente. NoryaAI los estructurará en un informe completo.",
            },
        ],
        "steps_title": "Qué ocurre después de subir su archivo",
        "steps_sub": "Desde la carga hasta el informe estructurado — todo el proceso lleva solo unos minutos.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Suba su informe",
                "desc": "Elija un PDF, una foto o pegue sus valores de laboratorio en el formulario de análisis.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "La IA lee sus datos",
                "desc": "Los valores, unidades y rangos de referencia se extraen y estructuran automáticamente.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Resumen estructurado",
                "desc": "Puntuación de salud, desglose por categorías y marcadores señalados — todo en una vista clara.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Descargue su informe",
                "desc": "Obtenga un PDF listo para su médico que puede imprimir, guardar o compartir en su próxima cita.",
            },
        ],
        "reasons_title": "Por qué las personas suben sus resultados aquí",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "Antes de una visita médica",
                "desc": "Llegue a su cita con un resumen claro y organizado. Le ayuda a hacer mejores preguntas y hace que la conversación sea más productiva.",
            },
            {
                "icon": "\U0001f310",
                "title": "Informes en otro idioma",
                "desc": "¿Tiene resultados de laboratorio en un idioma que no comprende del todo? Súbalos y obtenga una explicación estructurada en su idioma preferido — más de 9 idiomas disponibles.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "Para entender un informe complejo",
                "desc": "Páginas de datos de laboratorio pueden ser abrumadoras. NoryaAI las convierte en un desglose categorizado y fácil de leer con rangos de referencia y explicaciones claras.",
            },
        ],
        "trust_title": "Sus datos son suyos",
        "trust_sub": "La privacidad no es una idea de último momento. Está integrada en cada paso del proceso de carga y análisis.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "Cifrado en tránsito y en reposo"},
            {"icon": "\U0001f6e1\ufe0f", "text": "Cumple con RGPD y KVKK"},
            {"icon": "\U0001f6ab", "text": "Nunca se comparte ni se vende"},
            {"icon": "\U0001f504", "text": "No se utiliza para entrenamiento de modelos"},
        ],
        "preview_title": "Así se ve su informe",
        "preview_sub": "Un vistazo a la salida estructurada que recibe tras subir su análisis de sangre.",
        "preview_lines": [
            {"label": "Puntuación de salud", "value": "78 / 100 — Bueno en general, algunos marcadores a vigilar"},
            {"label": "Hemoglobina", "value": "14.2 g/dL — Dentro del rango normal (13.5–17.5)"},
            {"label": "Glucosa", "value": "108 mg/dL — Ligeramente elevada (normal: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — Función tiroidea normal (0.4–4.0)"},
            {"label": "Vitamina D", "value": "18 ng/mL — Por debajo del nivel recomendado (30–100)"},
        ],
        "preview_disclaimer": "Datos de ejemplo solo con fines ilustrativos. Su informe real reflejará sus valores de laboratorio, unidades y rangos de referencia personales.",
        "preview_link": "Ver un informe de ejemplo completo →",
        "faqs": [
            {
                "q": "¿Qué formatos de archivo puedo subir?",
                "a": "NoryaAI acepta archivos PDF, imágenes JPG/JPEG e imágenes PNG. También puede pegar sus valores de laboratorio como texto si no tiene un archivo para subir.",
            },
            {
                "q": "¿Cuánto tarda el análisis?",
                "a": "La mayoría de los informes se procesan en menos de dos minutos. Los PDF complejos de varias páginas pueden tardar un poco más, pero verá su resumen estructurado poco después de la carga.",
            },
            {
                "q": "¿Se almacena o comparte mi informe subido?",
                "a": "Su archivo subido se utiliza únicamente para generar su informe. Todos los datos se cifran en tránsito y en reposo, nunca se comparten con terceros y no se utilizan para entrenamiento de modelos. NoryaAI cumple con RGPD y KVKK.",
            },
            {
                "q": "¿Puedo subir informes en idiomas distintos al inglés?",
                "a": "Sí. NoryaAI puede leer informes de laboratorio en varios idiomas y generar su resumen estructurado en cualquiera de los más de 9 idiomas compatibles, incluyendo inglés, alemán, turco, francés, italiano, español, hebreo, hindi y árabe.",
            },
            {
                "q": "¿Necesito crear una cuenta para subir?",
                "a": "Puede iniciar un análisis sin crear una cuenta. Una cuenta le permite guardar sus informes, hacer seguimiento de los resultados con el tiempo y acceder a ellos desde cualquier dispositivo.",
            },
            {
                "q": "¿Es NoryaAI un sustituto de mi médico?",
                "a": "No. NoryaAI proporciona explicaciones estructuradas y educativas de sus valores de laboratorio para ayudarle a comprender mejor sus resultados. No diagnostica, no trata ni prescribe. Consulte siempre a un profesional sanitario cualificado para tomar decisiones médicas.",
            },
        ],
        "cta_title": "¿Listo para subir su análisis de sangre?",
        "cta_sub": "Obtenga un informe estructurado y listo para su médico en minutos. PDF, foto o texto pegado — usted elige.",
        "cta_primary": "Subir y analizar ahora",
        "cta_secondary": "Ver precios",
    }


def _fr() -> dict:
    return {
        "meta_title": "Télécharger ses résultats d'analyses sanguines — Analyse par IA | NoryaAI",
        "meta_description": "Téléchargez votre bilan sanguin en PDF, photo ou rapport de laboratoire et obtenez un résumé structuré avec valeurs de référence, score de santé et marqueurs signalés.",
        "hero_title": "Téléchargez vos résultats d'analyses sanguines",
        "hero_sub": "Téléchargez un PDF, prenez une photo ou collez vos valeurs de laboratoire. NoryaAI transforme votre bilan sanguin en un rapport structuré et facile à lire avec valeurs de référence, marqueurs signalés et score de santé.",
        "hero_trust": "Téléchargement chiffré · Conforme au RGPD et au KVKK · Aucun partage de données",
        "cta_hero_primary": "Lancer l'analyse",
        "cta_hero_secondary": "Voir un exemple de rapport",
        "formats_title": "Formats de téléchargement acceptés",
        "formats_sub": "Choisissez la méthode la plus simple pour vous — les trois produisent le même rapport structuré.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "Rapports de laboratoire en PDF",
                "desc": "Téléchargez le PDF reçu de votre laboratoire ou hôpital. NoryaAI lit les tableaux, valeurs et plages de référence directement depuis le document.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "Photos et captures d'écran",
                "desc": "Prenez une photo de votre rapport imprimé ou faites une capture d'écran de votre portail de laboratoire en ligne. Les fichiers JPG et PNG sont acceptés.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "Texte collé",
                "desc": "Pas de fichier ? Copiez-collez vos valeurs de laboratoire directement. NoryaAI les structurera en un rapport complet.",
            },
        ],
        "steps_title": "Ce qui se passe après le téléchargement",
        "steps_sub": "Du téléchargement au rapport structuré — l'ensemble du processus ne prend que quelques minutes.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Téléchargez votre rapport",
                "desc": "Choisissez un PDF, une photo ou collez vos valeurs de laboratoire dans le formulaire d'analyse.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "L'IA lit vos données",
                "desc": "Les valeurs, unités et plages de référence sont extraites et structurées automatiquement.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Résumé structuré",
                "desc": "Score de santé, répartition par catégorie et marqueurs signalés — le tout dans une vue claire.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Téléchargez votre rapport",
                "desc": "Obtenez un PDF prêt pour votre médecin que vous pouvez imprimer, sauvegarder ou partager lors de votre prochain rendez-vous.",
            },
        ],
        "reasons_title": "Pourquoi les gens téléchargent leurs résultats ici",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "Avant une visite chez le médecin",
                "desc": "Arrivez à votre rendez-vous avec un résumé clair et organisé. Cela vous aide à poser de meilleures questions et rend la conversation plus productive.",
            },
            {
                "icon": "\U0001f310",
                "title": "Rapports dans une autre langue",
                "desc": "Vous avez des résultats de laboratoire dans une langue que vous ne comprenez pas entièrement ? Téléchargez-les et obtenez une explication structurée dans votre langue préférée — plus de 9 langues prises en charge.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "Pour comprendre un rapport complexe",
                "desc": "Des pages de données de laboratoire peuvent être accablantes. NoryaAI les transforme en une synthèse catégorisée et facile à lire avec des plages de référence et des explications claires.",
            },
        ],
        "trust_title": "Vos données restent les vôtres",
        "trust_sub": "La confidentialité n'est pas une considération secondaire. Elle est intégrée à chaque étape du processus de téléchargement et d'analyse.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "Chiffré en transit et au repos"},
            {"icon": "\U0001f6e1\ufe0f", "text": "Conforme au RGPD et au KVKK"},
            {"icon": "\U0001f6ab", "text": "Jamais partagé ni vendu"},
            {"icon": "\U0001f504", "text": "Non utilisé pour l'entraînement de modèles"},
        ],
        "preview_title": "À quoi ressemble votre rapport",
        "preview_sub": "Voici un aperçu de la sortie structurée que vous recevez après avoir téléchargé votre bilan sanguin.",
        "preview_lines": [
            {"label": "Score de santé", "value": "78 / 100 — Bon dans l'ensemble, quelques marqueurs à surveiller"},
            {"label": "Hémoglobine", "value": "14.2 g/dL — Dans la plage normale (13.5–17.5)"},
            {"label": "Glucose", "value": "108 mg/dL — Légèrement élevé (normal : 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — Fonction thyroïdienne normale (0.4–4.0)"},
            {"label": "Vitamine D", "value": "18 ng/mL — En dessous du niveau recommandé (30–100)"},
        ],
        "preview_disclaimer": "Données d'exemple à titre d'illustration uniquement. Votre rapport réel reflétera vos valeurs de laboratoire, unités et plages de référence personnelles.",
        "preview_link": "Voir un exemple de rapport complet →",
        "faqs": [
            {
                "q": "Quels formats de fichier puis-je télécharger ?",
                "a": "NoryaAI accepte les fichiers PDF, les images JPG/JPEG et les images PNG. Vous pouvez également coller vos valeurs de laboratoire sous forme de texte si vous n'avez pas de fichier à télécharger.",
            },
            {
                "q": "Combien de temps dure l'analyse ?",
                "a": "La plupart des rapports sont traités en moins de deux minutes. Les PDF complexes de plusieurs pages peuvent prendre un peu plus de temps, mais vous verrez votre résumé structuré peu après le téléchargement.",
            },
            {
                "q": "Mon rapport téléchargé est-il stocké ou partagé ?",
                "a": "Votre fichier téléchargé est utilisé uniquement pour générer votre rapport. Toutes les données sont chiffrées en transit et au repos, jamais partagées avec des tiers et jamais utilisées pour l'entraînement de modèles. NoryaAI est conforme au RGPD et au KVKK.",
            },
            {
                "q": "Puis-je télécharger des rapports dans des langues autres que l'anglais ?",
                "a": "Oui. NoryaAI peut lire des rapports de laboratoire en plusieurs langues et générer votre résumé structuré dans n'importe laquelle des plus de 9 langues prises en charge, dont l'anglais, l'allemand, le turc, le français, l'italien, l'espagnol, l'hébreu, l'hindi et l'arabe.",
            },
            {
                "q": "Dois-je créer un compte pour télécharger ?",
                "a": "Vous pouvez commencer une analyse sans créer de compte. Un compte vous permet de sauvegarder vos rapports, de suivre les résultats dans le temps et d'y accéder depuis n'importe quel appareil.",
            },
            {
                "q": "NoryaAI remplace-t-il mon médecin ?",
                "a": "Non. NoryaAI fournit des explications structurées et pédagogiques de vos valeurs de laboratoire pour vous aider à mieux comprendre vos résultats. Il ne diagnostique pas, ne traite pas et ne prescrit pas. Consultez toujours un professionnel de santé qualifié pour les décisions médicales.",
            },
        ],
        "cta_title": "Prêt à télécharger votre bilan sanguin ?",
        "cta_sub": "Obtenez un rapport structuré, prêt pour votre médecin, en quelques minutes. PDF, photo ou texte collé — à vous de choisir.",
        "cta_primary": "Télécharger et analyser",
        "cta_secondary": "Voir les tarifs",
    }


def _it() -> dict:
    return {
        "meta_title": "Carica le analisi del sangue — Analisi con IA | NoryaAI",
        "meta_description": "Carica il PDF delle tue analisi del sangue, una foto o il referto di laboratorio e ottieni un riepilogo strutturato con intervalli di riferimento, punteggio di salute e valori segnalati.",
        "hero_title": "Carica i risultati delle tue analisi del sangue",
        "hero_sub": "Carica un PDF, scatta una foto o incolla i tuoi valori di laboratorio. NoryaAI trasforma le tue analisi del sangue in un report strutturato e facile da leggere con intervalli di riferimento, valori segnalati e un punteggio di salute.",
        "hero_trust": "Caricamento crittografato · Conforme al GDPR e al KVKK · Nessuna condivisione dati",
        "cta_hero_primary": "Avvia l'analisi",
        "cta_hero_secondary": "Vedi un report di esempio",
        "formats_title": "Formati di caricamento supportati",
        "formats_sub": "Scegli il metodo più comodo per te — tutti e tre producono lo stesso report strutturato.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "Referti di laboratorio in PDF",
                "desc": "Carica il PDF ricevuto dal tuo laboratorio o ospedale. NoryaAI legge tabelle, valori e intervalli di riferimento direttamente dal documento.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "Foto e screenshot",
                "desc": "Scatta una foto del tuo referto stampato o fai uno screenshot del tuo portale di laboratorio online. Sono supportati file JPG e PNG.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "Testo incollato",
                "desc": "Non hai un file? Copia e incolla i tuoi valori di laboratorio direttamente. NoryaAI li strutturerà in un report completo.",
            },
        ],
        "steps_title": "Cosa succede dopo il caricamento",
        "steps_sub": "Dal caricamento al report strutturato — l'intero processo richiede solo pochi minuti.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "Carica il tuo referto",
                "desc": "Scegli un PDF, una foto o incolla i tuoi valori di laboratorio nel modulo di analisi.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "L'IA legge i tuoi dati",
                "desc": "Valori, unità e intervalli di riferimento vengono estratti e strutturati automaticamente.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "Riepilogo strutturato",
                "desc": "Punteggio di salute, suddivisione per categorie e valori segnalati — tutto in un'unica vista chiara.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "Scarica il tuo report",
                "desc": "Ottieni un PDF pronto per il medico che puoi stampare, salvare o condividere al prossimo appuntamento.",
            },
        ],
        "reasons_title": "Perché le persone caricano i loro risultati qui",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "Prima di una visita medica",
                "desc": "Presenta al tuo appuntamento un riepilogo chiaro e organizzato. Ti aiuta a fare domande migliori e rende la conversazione più produttiva.",
            },
            {
                "icon": "\U0001f310",
                "title": "Referti in un'altra lingua",
                "desc": "Hai risultati di laboratorio in una lingua che non comprendi completamente? Caricali e ottieni una spiegazione strutturata nella tua lingua preferita — oltre 9 lingue supportate.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "Per capire un referto complesso",
                "desc": "Pagine di dati di laboratorio possono essere travolgenti. NoryaAI li trasforma in una suddivisione categorizzata e facile da leggere con intervalli di riferimento e spiegazioni chiare.",
            },
        ],
        "trust_title": "I tuoi dati restano tuoi",
        "trust_sub": "La privacy non è un ripensamento. È integrata in ogni fase del processo di caricamento e analisi.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "Crittografato in transito e a riposo"},
            {"icon": "\U0001f6e1\ufe0f", "text": "Conforme al GDPR e al KVKK"},
            {"icon": "\U0001f6ab", "text": "Mai condiviso né venduto"},
            {"icon": "\U0001f504", "text": "Non utilizzato per l'addestramento di modelli"},
        ],
        "preview_title": "Come appare il tuo report",
        "preview_sub": "Ecco un'anteprima dell'output strutturato che ricevi dopo aver caricato le tue analisi del sangue.",
        "preview_lines": [
            {"label": "Punteggio di salute", "value": "78 / 100 — Buono nel complesso, alcuni valori da monitorare"},
            {"label": "Emoglobina", "value": "14.2 g/dL — Nell'intervallo normale (13.5–17.5)"},
            {"label": "Glucosio", "value": "108 mg/dL — Leggermente elevato (normale: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — Funzione tiroidea normale (0.4–4.0)"},
            {"label": "Vitamina D", "value": "18 ng/mL — Al di sotto del livello raccomandato (30–100)"},
        ],
        "preview_disclaimer": "Dati di esempio solo a scopo illustrativo. Il tuo report reale rifletterà i tuoi valori di laboratorio, unità e intervalli di riferimento personali.",
        "preview_link": "Vedi un report di esempio completo →",
        "faqs": [
            {
                "q": "Quali formati di file posso caricare?",
                "a": "NoryaAI accetta file PDF, immagini JPG/JPEG e immagini PNG. Puoi anche incollare i tuoi valori di laboratorio come testo se non hai un file da caricare.",
            },
            {
                "q": "Quanto tempo richiede l'analisi?",
                "a": "La maggior parte dei referti viene elaborata in meno di due minuti. I PDF complessi con più pagine possono richiedere un po' più tempo, ma vedrai il tuo riepilogo strutturato poco dopo il caricamento.",
            },
            {
                "q": "Il mio referto caricato viene archiviato o condiviso?",
                "a": "Il tuo file caricato viene utilizzato esclusivamente per generare il tuo report. Tutti i dati sono crittografati in transito e a riposo, mai condivisi con terze parti e mai utilizzati per l'addestramento di modelli. NoryaAI è conforme al GDPR e al KVKK.",
            },
            {
                "q": "Posso caricare referti in lingue diverse dall'inglese?",
                "a": "Sì. NoryaAI può leggere referti di laboratorio in più lingue e generare il tuo riepilogo strutturato in una qualsiasi delle oltre 9 lingue supportate, tra cui inglese, tedesco, turco, francese, italiano, spagnolo, ebraico, hindi e arabo.",
            },
            {
                "q": "Devo creare un account per caricare?",
                "a": "Puoi avviare un'analisi senza creare un account. Un account ti consente di salvare i tuoi report, monitorare i risultati nel tempo e accedervi da qualsiasi dispositivo.",
            },
            {
                "q": "NoryaAI sostituisce il mio medico?",
                "a": "No. NoryaAI fornisce spiegazioni strutturate e didattiche dei tuoi valori di laboratorio per aiutarti a comprendere meglio i tuoi risultati. Non diagnostica, non cura e non prescrive. Consulta sempre un professionista sanitario qualificato per le decisioni mediche.",
            },
        ],
        "cta_title": "Pronto a caricare le tue analisi del sangue?",
        "cta_sub": "Ottieni un report strutturato e pronto per il medico in pochi minuti. PDF, foto o testo incollato — la scelta è tua.",
        "cta_primary": "Carica e analizza ora",
        "cta_secondary": "Vedi i prezzi",
    }


def _he() -> dict:
    return {
        "meta_title": "העלאת תוצאות בדיקת דם — ניתוח מבוסס בינה מלאכותית | NoryaAI",
        "meta_description": "העלו את תוצאות בדיקת הדם שלכם כ-PDF, צילום או דוח מעבדה וקבלו סיכום מובנה עם טווחי ייחוס, ציון בריאות וסמנים מסומנים — תוך דקות.",
        "hero_title": "העלו את תוצאות בדיקת הדם שלכם",
        "hero_sub": "העלו PDF, צלמו תמונה או הדביקו את ערכי המעבדה שלכם. NoryaAI הופך את בדיקת הדם שלכם לדוח מובנה וקל לקריאה עם טווחי ייחוס, סמנים מסומנים וציון בריאות.",
        "hero_trust": "העלאה מוצפנת · עמידה ב-GDPR ו-KVKK · ללא שיתוף נתונים",
        "cta_hero_primary": "התחילו ניתוח",
        "cta_hero_secondary": "צפו בדוח לדוגמה",
        "formats_title": "פורמטי העלאה נתמכים",
        "formats_sub": "בחרו את השיטה הנוחה לכם ביותר — שלושתן מפיקות את אותו דוח מובנה.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "דוחות מעבדה ב-PDF",
                "desc": "העלו את ה-PDF שקיבלתם מהמעבדה או מבית החולים. NoryaAI קורא טבלאות, ערכים וטווחי ייחוס ישירות מהמסמך.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "צילומים וצילומי מסך",
                "desc": "צלמו את הדוח המודפס שלכם או את צילום המסך מפורטל המעבדה המקוון. קבצי JPG ו-PNG נתמכים.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "טקסט מודבק",
                "desc": "אין קובץ? העתיקו והדביקו את ערכי המעבדה שלכם ישירות. NoryaAI יבנה אותם לדוח מלא.",
            },
        ],
        "steps_title": "מה קורה אחרי ההעלאה",
        "steps_sub": "מהעלאה ועד דוח מובנה — כל התהליך לוקח מספר דקות בלבד.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "העלו את הדוח שלכם",
                "desc": "בחרו PDF, צילום או הדביקו את ערכי המעבדה שלכם בטופס הניתוח.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "הבינה המלאכותית קוראת את הנתונים",
                "desc": "ערכים, יחידות וטווחי ייחוס מחולצים ומובנים באופן אוטומטי.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "סיכום מובנה",
                "desc": "ציון בריאות, פירוט לפי קטגוריות וסמנים מסומנים — הכול בתצוגה אחת ברורה.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "הורידו את הדוח שלכם",
                "desc": "קבלו PDF מוכן לרופא שניתן להדפיס, לשמור או לשתף בפגישה הבאה.",
            },
        ],
        "reasons_title": "למה אנשים מעלים את התוצאות שלהם לכאן",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "לפני ביקור אצל הרופא",
                "desc": "הגיעו לפגישה עם סיכום ברור ומאורגן. זה עוזר לכם לשאול שאלות טובות יותר והופך את השיחה לפרודוקטיבית יותר.",
            },
            {
                "icon": "\U0001f310",
                "title": "דוחות בשפה אחרת",
                "desc": "קיבלתם תוצאות מעבדה בשפה שאתם לא מבינים לגמרי? העלו אותן וקבלו הסבר מובנה בשפה המועדפת עליכם — יותר מ-9 שפות נתמכות.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "כדי להבין דוח מורכב",
                "desc": "עמודים של נתוני מעבדה יכולים להציף. NoryaAI הופך אותם לפירוט מסווג וקל לקריאה עם טווחי ייחוס והסברים ברורים.",
            },
        ],
        "trust_title": "הנתונים שלכם נשארים שלכם",
        "trust_sub": "הפרטיות אינה מחשבה שלאחר מעשה. היא מוטמעת בכל שלב של תהליך ההעלאה והניתוח.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "מוצפן בהעברה ובאחסון"},
            {"icon": "\U0001f6e1\ufe0f", "text": "עמידה ב-GDPR ו-KVKK"},
            {"icon": "\U0001f6ab", "text": "לעולם לא משותף או נמכר"},
            {"icon": "\U0001f504", "text": "לא משמש לאימון מודלים"},
        ],
        "preview_title": "כך נראה הדוח שלכם",
        "preview_sub": "הנה הצצה לפלט המובנה שתקבלו לאחר העלאת בדיקת הדם.",
        "preview_lines": [
            {"label": "ציון בריאות", "value": "78 / 100 — טוב בסך הכול, כמה סמנים לעקוב אחריהם"},
            {"label": "המוגלובין", "value": "14.2 g/dL — בטווח התקין (13.5–17.5)"},
            {"label": "גלוקוז", "value": "108 mg/dL — מעט מוגבה (תקין: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — תפקוד תקין של בלוטת התריס (0.4–4.0)"},
            {"label": "ויטמין D", "value": "18 ng/mL — מתחת לרמה המומלצת (30–100)"},
        ],
        "preview_disclaimer": "נתוני דוגמה למטרות המחשה בלבד. הדוח בפועל ישקף את ערכי המעבדה, היחידות וטווחי הייחוס האישיים שלכם.",
        "preview_link": "צפו בדוח לדוגמה מלא →",
        "faqs": [
            {
                "q": "אילו פורמטי קבצים ניתן להעלות?",
                "a": "NoryaAI מקבל קבצי PDF, תמונות JPG/JPEG ותמונות PNG. ניתן גם להדביק את ערכי המעבדה כטקסט אם אין לכם קובץ להעלאה.",
            },
            {
                "q": "כמה זמן לוקח הניתוח?",
                "a": "רוב הדוחות מעובדים תוך פחות משתי דקות. קבצי PDF מורכבים עם מספר עמודים עשויים לקחת קצת יותר זמן, אך תראו את הסיכום המובנה שלכם זמן קצר לאחר ההעלאה.",
            },
            {
                "q": "האם הדוח שהועלה נשמר או משותף?",
                "a": "הקובץ שהעליתם משמש אך ורק ליצירת הדוח שלכם. כל הנתונים מוצפנים בהעברה ובאחסון, לעולם לא משותפים עם צדדים שלישיים ולא משמשים לאימון מודלים. NoryaAI עומד בדרישות ה-GDPR וה-KVKK.",
            },
            {
                "q": "האם ניתן להעלות דוחות בשפות אחרות מלבד אנגלית?",
                "a": "כן. NoryaAI יכול לקרוא דוחות מעבדה בשפות מרובות ולהפיק את הסיכום המובנה שלכם בכל אחת מיותר מ-9 שפות נתמכות, כולל אנגלית, גרמנית, טורקית, צרפתית, איטלקית, ספרדית, עברית, הינדית וערבית.",
            },
            {
                "q": "האם צריך ליצור חשבון כדי להעלות?",
                "a": "ניתן להתחיל ניתוח ללא יצירת חשבון. חשבון מאפשר לכם לשמור דוחות, לעקוב אחר תוצאות לאורך זמן ולגשת אליהן מכל מכשיר.",
            },
            {
                "q": "האם NoryaAI מחליף את הרופא שלי?",
                "a": "לא. NoryaAI מספק הסברים מובנים וחינוכיים של ערכי המעבדה שלכם כדי לעזור לכם להבין את התוצאות טוב יותר. הוא אינו מאבחן, אינו מטפל ואינו רושם תרופות. התייעצו תמיד עם איש מקצוע רפואי מוסמך לקבלת החלטות רפואיות.",
            },
        ],
        "cta_title": "מוכנים להעלות את בדיקת הדם שלכם?",
        "cta_sub": "קבלו דוח מובנה ומוכן לרופא תוך דקות. PDF, צילום או טקסט מודבק — הבחירה שלכם.",
        "cta_primary": "העלו ונתחו עכשיו",
        "cta_secondary": "צפו במחירים",
    }


def _hi() -> dict:
    return {
        "meta_title": "रक्त परीक्षण रिपोर्ट अपलोड करें — AI-संचालित विश्लेषण | NoryaAI",
        "meta_description": "अपनी रक्त परीक्षण PDF, फ़ोटो या लैब रिपोर्ट अपलोड करें और संदर्भ श्रेणियों, स्वास्थ्य स्कोर और चिह्नित मार्करों के साथ एक संरचित, डॉक्टर-तैयार सारांश प्राप्त करें।",
        "hero_title": "अपनी रक्त परीक्षण रिपोर्ट अपलोड करें",
        "hero_sub": "PDF अपलोड करें, फ़ोटो लें या अपने लैब मान पेस्ट करें। NoryaAI आपके रक्त परीक्षण को संदर्भ श्रेणियों, चिह्नित मार्करों और स्वास्थ्य स्कोर के साथ एक संरचित, आसानी से पढ़ने योग्य रिपोर्ट में बदल देता है।",
        "hero_trust": "एन्क्रिप्टेड अपलोड · GDPR और KVKK अनुपालन · कोई डेटा साझाकरण नहीं",
        "cta_hero_primary": "विश्लेषण शुरू करें",
        "cta_hero_secondary": "नमूना रिपोर्ट देखें",
        "formats_title": "समर्थित अपलोड प्रारूप",
        "formats_sub": "जो भी तरीका आपके लिए सबसे आसान हो वह चुनें — तीनों एक ही संरचित रिपोर्ट तैयार करते हैं।",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "PDF लैब रिपोर्ट",
                "desc": "अपनी लैब या अस्पताल से प्राप्त PDF अपलोड करें। NoryaAI दस्तावेज़ से सीधे तालिकाओं, मानों और संदर्भ श्रेणियों को पढ़ता है।",
            },
            {
                "icon": "\U0001f4f7",
                "title": "फ़ोटो और स्क्रीनशॉट",
                "desc": "अपनी मुद्रित रिपोर्ट की फ़ोटो लें या अपने ऑनलाइन लैब पोर्टल का स्क्रीनशॉट लें। JPG और PNG फ़ाइलें समर्थित हैं।",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "पेस्ट किया गया टेक्स्ट",
                "desc": "कोई फ़ाइल नहीं? अपने लैब मान सीधे कॉपी और पेस्ट करें। NoryaAI उन्हें एक पूर्ण रिपोर्ट में संरचित करेगा।",
            },
        ],
        "steps_title": "अपलोड के बाद क्या होता है",
        "steps_sub": "अपलोड से संरचित रिपोर्ट तक — पूरी प्रक्रिया में बस कुछ मिनट लगते हैं।",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "अपनी रिपोर्ट अपलोड करें",
                "desc": "PDF, फ़ोटो चुनें या विश्लेषण फ़ॉर्म में अपने लैब मान पेस्ट करें।",
            },
            {
                "icon": "\U0001f9e0",
                "title": "AI आपका डेटा पढ़ता है",
                "desc": "मान, इकाइयाँ और संदर्भ श्रेणियाँ स्वचालित रूप से निकाली और संरचित की जाती हैं।",
            },
            {
                "icon": "\U0001f4cb",
                "title": "संरचित सारांश",
                "desc": "स्वास्थ्य स्कोर, श्रेणी विश्लेषण और चिह्नित मार्कर — सब एक स्पष्ट दृश्य में।",
            },
            {
                "icon": "\U0001f4e5",
                "title": "अपनी रिपोर्ट डाउनलोड करें",
                "desc": "डॉक्टर-तैयार PDF प्राप्त करें जिसे आप प्रिंट, सेव या अपनी अगली अपॉइंटमेंट में साझा कर सकते हैं।",
            },
        ],
        "reasons_title": "लोग अपनी रिपोर्ट यहाँ क्यों अपलोड करते हैं",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "डॉक्टर से मिलने से पहले",
                "desc": "एक स्पष्ट, व्यवस्थित सारांश के साथ अपनी अपॉइंटमेंट पर जाएँ। यह आपको बेहतर प्रश्न पूछने में मदद करता है और बातचीत को अधिक उत्पादक बनाता है।",
            },
            {
                "icon": "\U0001f310",
                "title": "दूसरी भाषा में रिपोर्ट",
                "desc": "क्या आपको ऐसी भाषा में लैब परिणाम मिले हैं जो आप पूरी तरह नहीं समझते? उन्हें अपलोड करें और अपनी पसंदीदा भाषा में संरचित व्याख्या प्राप्त करें — 9 से अधिक भाषाएँ समर्थित हैं।",
            },
            {
                "icon": "\U0001f4d6",
                "title": "एक जटिल रिपोर्ट को समझने के लिए",
                "desc": "पृष्ठों भर लैब डेटा भारी हो सकता है। NoryaAI उन्हें संदर्भ श्रेणियों और स्पष्ट व्याख्याओं के साथ वर्गीकृत, आसानी से पढ़ने योग्य विश्लेषण में बदल देता है।",
            },
        ],
        "trust_title": "आपका डेटा आपका रहता है",
        "trust_sub": "गोपनीयता बाद का विचार नहीं है। यह अपलोड और विश्लेषण प्रक्रिया के हर चरण में अंतर्निहित है।",
        "trust_items": [
            {"icon": "\U0001f512", "text": "ट्रांज़िट और स्टोरेज में एन्क्रिप्टेड"},
            {"icon": "\U0001f6e1\ufe0f", "text": "GDPR और KVKK अनुपालन"},
            {"icon": "\U0001f6ab", "text": "कभी साझा या बेचा नहीं जाता"},
            {"icon": "\U0001f504", "text": "मॉडल प्रशिक्षण के लिए उपयोग नहीं किया जाता"},
        ],
        "preview_title": "आपकी रिपोर्ट कैसी दिखती है",
        "preview_sub": "आपकी रक्त परीक्षण रिपोर्ट अपलोड करने के बाद आपको मिलने वाले संरचित आउटपुट की एक झलक।",
        "preview_lines": [
            {"label": "स्वास्थ्य स्कोर", "value": "78 / 100 — कुल मिलाकर अच्छा, कुछ मार्करों पर नज़र रखें"},
            {"label": "हीमोग्लोबिन", "value": "14.2 g/dL — सामान्य सीमा में (13.5–17.5)"},
            {"label": "ग्लूकोज़", "value": "108 mg/dL — थोड़ा बढ़ा हुआ (सामान्य: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — सामान्य थायरॉइड कार्य (0.4–4.0)"},
            {"label": "विटामिन D", "value": "18 ng/mL — अनुशंसित स्तर से नीचे (30–100)"},
        ],
        "preview_disclaimer": "केवल उदाहरण के लिए नमूना डेटा। आपकी वास्तविक रिपोर्ट आपके व्यक्तिगत लैब मान, इकाइयों और संदर्भ श्रेणियों को दर्शाएगी।",
        "preview_link": "पूर्ण नमूना रिपोर्ट देखें →",
        "faqs": [
            {
                "q": "मैं कौन से फ़ाइल प्रारूप अपलोड कर सकता हूँ?",
                "a": "NoryaAI PDF फ़ाइलें, JPG/JPEG छवियाँ और PNG छवियाँ स्वीकार करता है। यदि आपके पास अपलोड करने के लिए कोई फ़ाइल नहीं है तो आप अपने लैब मान टेक्स्ट के रूप में भी पेस्ट कर सकते हैं।",
            },
            {
                "q": "विश्लेषण में कितना समय लगता है?",
                "a": "अधिकांश रिपोर्ट दो मिनट से कम में संसाधित हो जाती हैं। जटिल बहु-पृष्ठ PDF में थोड़ा अधिक समय लग सकता है, लेकिन आप अपलोड के कुछ ही समय बाद अपना संरचित सारांश देखेंगे।",
            },
            {
                "q": "क्या मेरी अपलोड की गई रिपोर्ट संग्रहीत या साझा की जाती है?",
                "a": "आपकी अपलोड की गई फ़ाइल का उपयोग केवल आपकी रिपोर्ट बनाने के लिए किया जाता है। सभी डेटा ट्रांज़िट और स्टोरेज में एन्क्रिप्टेड होता है, कभी तीसरे पक्ष के साथ साझा नहीं किया जाता और मॉडल प्रशिक्षण के लिए उपयोग नहीं किया जाता। NoryaAI GDPR और KVKK अनुपालन करता है।",
            },
            {
                "q": "क्या मैं अंग्रेज़ी के अलावा अन्य भाषाओं में रिपोर्ट अपलोड कर सकता हूँ?",
                "a": "हाँ। NoryaAI कई भाषाओं में लैब रिपोर्ट पढ़ सकता है और आपका संरचित सारांश 9 से अधिक समर्थित भाषाओं में से किसी में भी तैयार कर सकता है, जिसमें अंग्रेज़ी, जर्मन, तुर्की, फ़्रेंच, इतालवी, स्पेनिश, हिब्रू, हिंदी और अरबी शामिल हैं।",
            },
            {
                "q": "क्या अपलोड करने के लिए मुझे खाता बनाना होगा?",
                "a": "आप बिना खाता बनाए विश्लेषण शुरू कर सकते हैं। खाता आपको रिपोर्ट सहेजने, समय के साथ परिणामों को ट्रैक करने और किसी भी डिवाइस से एक्सेस करने की सुविधा देता है।",
            },
            {
                "q": "क्या NoryaAI मेरे डॉक्टर का विकल्प है?",
                "a": "नहीं। NoryaAI आपके परिणामों को बेहतर ढंग से समझने में मदद करने के लिए आपके लैब मानों की संरचित, शैक्षिक व्याख्या प्रदान करता है। यह निदान, उपचार या दवा नहीं लिखता। चिकित्सा निर्णयों के लिए हमेशा किसी योग्य स्वास्थ्य पेशेवर से परामर्श करें।",
            },
        ],
        "cta_title": "अपनी रक्त परीक्षण रिपोर्ट अपलोड करने के लिए तैयार हैं?",
        "cta_sub": "मिनटों में एक संरचित, डॉक्टर-तैयार रिपोर्ट प्राप्त करें। PDF, फ़ोटो या पेस्ट किया गया टेक्स्ट — आपकी पसंद।",
        "cta_primary": "अपलोड करें और अभी विश्लेषण करें",
        "cta_secondary": "मूल्य देखें",
    }


def _ar() -> dict:
    return {
        "meta_title": "رفع نتائج تحليل الدم — تحليل بالذكاء الاصطناعي | NoryaAI",
        "meta_description": "ارفع تحليل الدم الخاص بك كملف PDF أو صورة أو تقرير مختبر واحصل على ملخص منظم وجاهز للطبيب مع النطاقات المرجعية ودرجة الصحة والمؤشرات المميزة.",
        "hero_title": "ارفع نتائج تحليل الدم الخاصة بك",
        "hero_sub": "ارفع ملف PDF أو التقط صورة أو الصق قيم المختبر الخاصة بك. يحوّل NoryaAI تحليل الدم الخاص بك إلى تقرير منظم وسهل القراءة مع نطاقات مرجعية ومؤشرات مميزة ودرجة صحة.",
        "hero_trust": "رفع مشفّر · متوافق مع GDPR وKVKK · بدون مشاركة بيانات",
        "cta_hero_primary": "ابدأ التحليل",
        "cta_hero_secondary": "عرض تقرير نموذجي",
        "formats_title": "صيغ الرفع المدعومة",
        "formats_sub": "اختر الطريقة الأسهل بالنسبة لك — الطرق الثلاث تنتج نفس التقرير المنظم.",
        "formats": [
            {
                "icon": "\U0001f4c4",
                "title": "تقارير المختبر بصيغة PDF",
                "desc": "ارفع ملف PDF الذي استلمته من المختبر أو المستشفى. يقرأ NoryaAI الجداول والقيم والنطاقات المرجعية مباشرة من المستند.",
            },
            {
                "icon": "\U0001f4f7",
                "title": "صور ولقطات شاشة",
                "desc": "التقط صورة لتقريرك المطبوع أو لقطة شاشة من بوابة المختبر الإلكترونية. الملفات بصيغة JPG وPNG مدعومة.",
            },
            {
                "icon": "\u2328\ufe0f",
                "title": "نص ملصق",
                "desc": "ليس لديك ملف؟ انسخ والصق قيم المختبر الخاصة بك مباشرة. سيقوم NoryaAI ببنائها في تقرير كامل.",
            },
        ],
        "steps_title": "ماذا يحدث بعد الرفع",
        "steps_sub": "من الرفع إلى التقرير المنظم — العملية بأكملها تستغرق بضع دقائق فقط.",
        "steps": [
            {
                "icon": "\U0001f4e4",
                "title": "ارفع تقريرك",
                "desc": "اختر ملف PDF أو صورة أو الصق قيم المختبر في نموذج التحليل.",
            },
            {
                "icon": "\U0001f9e0",
                "title": "الذكاء الاصطناعي يقرأ بياناتك",
                "desc": "يتم استخراج القيم والوحدات والنطاقات المرجعية وتنظيمها تلقائيًا.",
            },
            {
                "icon": "\U0001f4cb",
                "title": "ملخص منظم",
                "desc": "درجة الصحة وتفصيل الفئات والمؤشرات المميزة — الكل في عرض واحد واضح.",
            },
            {
                "icon": "\U0001f4e5",
                "title": "حمّل تقريرك",
                "desc": "احصل على ملف PDF جاهز للطبيب يمكنك طباعته أو حفظه أو مشاركته في موعدك القادم.",
            },
        ],
        "reasons_title": "لماذا يرفع الناس نتائجهم هنا",
        "reasons": [
            {
                "icon": "\U0001fa7a",
                "title": "قبل زيارة الطبيب",
                "desc": "اذهب إلى موعدك مع ملخص واضح ومنظم. يساعدك على طرح أسئلة أفضل ويجعل المحادثة أكثر إنتاجية.",
            },
            {
                "icon": "\U0001f310",
                "title": "تقارير بلغة أخرى",
                "desc": "هل حصلت على نتائج مختبر بلغة لا تفهمها بالكامل؟ ارفعها واحصل على شرح منظم بلغتك المفضلة — أكثر من 9 لغات مدعومة.",
            },
            {
                "icon": "\U0001f4d6",
                "title": "لفهم تقرير معقد",
                "desc": "صفحات من بيانات المختبر قد تكون مربكة. يحوّلها NoryaAI إلى تفصيل مصنّف وسهل القراءة مع نطاقات مرجعية وشروحات واضحة.",
            },
        ],
        "trust_title": "بياناتك تبقى ملكك",
        "trust_sub": "الخصوصية ليست فكرة لاحقة. إنها مدمجة في كل خطوة من عملية الرفع والتحليل.",
        "trust_items": [
            {"icon": "\U0001f512", "text": "مشفّر أثناء النقل والتخزين"},
            {"icon": "\U0001f6e1\ufe0f", "text": "متوافق مع GDPR وKVKK"},
            {"icon": "\U0001f6ab", "text": "لا يُشارَك أو يُباع أبدًا"},
            {"icon": "\U0001f504", "text": "لا يُستخدم لتدريب النماذج"},
        ],
        "preview_title": "كيف يبدو تقريرك",
        "preview_sub": "إليك لمحة عن المخرجات المنظمة التي تحصل عليها بعد رفع تحليل الدم الخاص بك.",
        "preview_lines": [
            {"label": "درجة الصحة", "value": "78 / 100 — جيد بشكل عام، بعض المؤشرات تستحق المتابعة"},
            {"label": "الهيموغلوبين", "value": "14.2 g/dL — ضمن النطاق الطبيعي (13.5–17.5)"},
            {"label": "الغلوكوز", "value": "108 mg/dL — مرتفع قليلاً (طبيعي: 70–100)"},
            {"label": "TSH", "value": "2.1 mIU/L — وظيفة الغدة الدرقية طبيعية (0.4–4.0)"},
            {"label": "فيتامين D", "value": "18 ng/mL — أقل من المستوى الموصى به (30–100)"},
        ],
        "preview_disclaimer": "بيانات نموذجية لأغراض التوضيح فقط. سيعكس تقريرك الفعلي قيم المختبر والوحدات والنطاقات المرجعية الخاصة بك.",
        "preview_link": "عرض تقرير نموذجي كامل →",
        "faqs": [
            {
                "q": "ما صيغ الملفات التي يمكنني رفعها؟",
                "a": "يقبل NoryaAI ملفات PDF وصور JPG/JPEG وصور PNG. يمكنك أيضًا لصق قيم المختبر كنص إذا لم يكن لديك ملف للرفع.",
            },
            {
                "q": "كم يستغرق التحليل؟",
                "a": "تتم معالجة معظم التقارير في أقل من دقيقتين. قد تستغرق ملفات PDF المعقدة متعددة الصفحات وقتًا أطول قليلاً، لكنك سترى ملخصك المنظم بعد وقت قصير من الرفع.",
            },
            {
                "q": "هل يتم تخزين تقريري المرفوع أو مشاركته؟",
                "a": "يُستخدم ملفك المرفوع فقط لإنشاء تقريرك. جميع البيانات مشفرة أثناء النقل والتخزين، ولا تُشارَك مع أطراف ثالثة أبدًا، ولا تُستخدم لتدريب النماذج. NoryaAI متوافق مع GDPR وKVKK.",
            },
            {
                "q": "هل يمكنني رفع تقارير بلغات أخرى غير الإنجليزية؟",
                "a": "نعم. يستطيع NoryaAI قراءة تقارير المختبر بعدة لغات وإنشاء ملخصك المنظم بأي لغة من أكثر من 9 لغات مدعومة، بما في ذلك الإنجليزية والألمانية والتركية والفرنسية والإيطالية والإسبانية والعبرية والهندية والعربية.",
            },
            {
                "q": "هل أحتاج إلى إنشاء حساب للرفع؟",
                "a": "يمكنك بدء التحليل بدون إنشاء حساب. يتيح لك الحساب حفظ تقاريرك وتتبع النتائج بمرور الوقت والوصول إليها من أي جهاز.",
            },
            {
                "q": "هل NoryaAI بديل عن طبيبي؟",
                "a": "لا. يقدم NoryaAI شروحات منظمة وتثقيفية لقيم المختبر الخاصة بك لمساعدتك على فهم نتائجك بشكل أفضل. لا يُشخّص ولا يُعالج ولا يصف أدوية. استشر دائمًا متخصصًا صحيًا مؤهلاً لاتخاذ القرارات الطبية.",
            },
        ],
        "cta_title": "مستعد لرفع تحليل الدم الخاص بك؟",
        "cta_sub": "احصل على تقرير منظم وجاهز للطبيب في دقائق. PDF أو صورة أو نص ملصق — اختيارك.",
        "cta_primary": "ارفع وحلّل الآن",
        "cta_secondary": "عرض الأسعار",
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


def get_upload_landing_content(lang: str) -> dict:
    return _CONTENT.get(lang, _CONTENT["en"])


def get_upload_landing_slug(lang: str) -> str:
    return UPLOAD_SLUGS.get(lang, UPLOAD_SLUGS["en"])
