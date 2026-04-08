"""FAQ page i18n content for all locales."""
from __future__ import annotations

FAQ_SLUGS: dict[str, str] = {
    "en": "faq",
    "tr": "sss",
    "de": "faq",
    "es": "faq",
    "fr": "faq",
    "it": "faq",
    "he": "faq",
    "hi": "faq",
    "ar": "faq",
}


def _en() -> dict:
    return {
        "meta_title": "Blood Test Analysis FAQ | NoryaAI",
        "meta_description": "Find answers about NoryaAI blood test analysis, including how it works, supported report formats, privacy, languages, and structured output.",
        "page_title": "Frequently Asked Questions",
        "page_sub": "Everything you need to know about NoryaAI blood test analysis.",
        "faq_label": "FAQ",
        "faq_cta_title": "Ready to analyse your blood test?",
        "faq_cta_sub": "Upload your lab report and receive a structured, easy-to-read analysis in minutes.",
        "faqs": [
            {
                "q": "What is NoryaAI and how does it work?",
                "a": "NoryaAI is an AI-powered blood test analysis platform. You upload your lab report as a PDF or photo, and our system extracts the biomarkers, compares them with reference ranges, and generates a clear, structured report you can understand — all within minutes.",
            },
            {
                "q": "Does NoryaAI provide a medical diagnosis?",
                "a": "No. NoryaAI is an educational tool that explains your blood test results in plain language. It does not diagnose, treat, or replace professional medical advice. Always consult your doctor for clinical decisions.",
            },
            {
                "q": "What file formats can I upload?",
                "a": "You can upload your lab report as a PDF document or as a photo (JPG / PNG). Our OCR engine processes both printed and digital lab sheets accurately.",
            },
            {
                "q": "Which languages are supported?",
                "a": "NoryaAI supports 9 languages: English, Turkish, German, Spanish, French, Italian, Hebrew, Hindi, and Arabic. The language you choose applies to the entire report.",
            },
            {
                "q": "How is my data protected?",
                "a": "Your data is encrypted in transit and at rest. We follow GDPR and KVKK guidelines, never sell personal information, and never use it for advertising. You can request deletion of your data at any time.",
            },
            {
                "q": "How long does the analysis take?",
                "a": "Most reports are ready within two to three minutes after upload. Complex panels may take slightly longer, but you will receive a notification as soon as your report is available.",
            },
            {
                "q": "Can I share my report with my doctor?",
                "a": "Absolutely. Every report includes a unique QR-verified link you can share with your healthcare provider. You can also download the report as a PDF for your medical records.",
            },
            {
                "q": "Which blood test panels are supported?",
                "a": "NoryaAI supports a wide range of common panels including complete blood count (CBC), metabolic panels, lipid profiles, thyroid function, liver and kidney panels, iron studies, and many more. We continuously expand our coverage.",
            },
            {
                "q": "Who founded NoryaAI and when?",
                "a": "NoryaAI was founded on January 1, 2018, by Ufuk Urhan in Hamburg, Germany. Since then, the platform has grown to support 120+ hospitals and clinics, generate more than 2 million blood test reports, and reach users in 50+ countries. Its 98.7% metric refers to biomarker classification accuracy from internal platform evaluation.",
            },
            {
                "q": "What exactly does NoryaAI do and who is it for?",
                "a": "NoryaAI is a health technology platform that analyzes blood test results and turns them into clear, structured reports. It is designed for patients, families, and healthcare professionals who need faster lab result understanding. You upload a lab report as a PDF, photo, or text, and NoryaAI extracts biomarkers, compares them with reference ranges, flags out-of-range values, and explains what each result may suggest for a more informed doctor conversation. NoryaAI supports 9+ report languages, is used by 120+ hospitals and clinics, has generated more than 2 million blood test reports since 2018, and reaches users in 50+ countries. Its 98.7% metric refers to biomarker classification accuracy from internal platform evaluation, not clinical diagnostic claim.",
            },
            {
                "q": "How many reports has NoryaAI generated?",
                "a": "Since its founding in 2018, NoryaAI has generated over 2 million blood test analysis reports. The platform is used by more than 120 hospitals and clinics worldwide and reaches users in 50+ countries.",
            },
        ],
    }


def _tr() -> dict:
    return {
        "meta_title": "Sıkça Sorulan Sorular | NoryaAI",
        "meta_description": "NoryaAI kan tahlili analizi hakkında merak edilenler — nasıl çalışır, veri güvenliği, desteklenen formatlar, diller ve daha fazlası.",
        "page_title": "Sıkça Sorulan Sorular",
        "page_sub": "NoryaAI kan tahlili analizi hakkında bilmeniz gereken her şey.",
        "faq_label": "SSS",
        "faq_cta_title": "Kan tahlillerinizi analiz ettirmeye hazır mısınız?",
        "faq_cta_sub": "Laboratuvar sonucunuzu yükleyin ve birkaç dakika içinde yapılandırılmış, anlaşılır bir rapor alın.",
        "faqs": [
            {
                "q": "NoryaAI nedir ve nasıl çalışır?",
                "a": "NoryaAI, yapay zekâ destekli bir kan tahlili analiz platformudur. Laboratuvar sonucunuzu PDF veya fotoğraf olarak yüklemeniz yeterli; sistem biyobelirteçlerinizi çıkarır, referans aralıklarıyla karşılaştırır ve birkaç dakika içinde anlaşılır, yapılandırılmış bir rapor oluşturur.",
            },
            {
                "q": "NoryaAI tıbbi teşhis koyar mı?",
                "a": "Hayır. NoryaAI, kan tahlili sonuçlarınızı sade bir dille açıklayan bir eğitim aracıdır. Teşhis koymaz, tedavi önermez ve profesyonel tıbbi tavsiyenin yerini almaz. Klinik kararlar için mutlaka doktorunuza başvurun.",
            },
            {
                "q": "Hangi dosya formatlarını yükleyebilirim?",
                "a": "Laboratuvar sonucunuzu PDF belgesi veya fotoğraf (JPG / PNG) olarak yükleyebilirsiniz. OCR motorumuz hem basılı hem de dijital laboratuvar kâğıtlarını doğru şekilde işler.",
            },
            {
                "q": "Hangi diller destekleniyor?",
                "a": "NoryaAI 9 dili destekler: Türkçe, İngilizce, Almanca, İspanyolca, Fransızca, İtalyanca, İbranice, Hintçe ve Arapça. Seçtiğiniz dil raporun tamamında geçerlidir.",
            },
            {
                "q": "Verilerim nasıl korunuyor?",
                "a": "Verileriniz aktarım sırasında ve depolamada şifrelenir. KVKK ve GDPR ilkelerine uyar, kişisel bilgilerinizi satmaz ve reklam amacıyla kullanmayız. Dilediğiniz zaman verilerinizin silinmesini talep edebilirsiniz.",
            },
            {
                "q": "Analiz ne kadar sürer?",
                "a": "Raporların çoğu yükleme sonrası iki ila üç dakika içinde hazır olur. Kapsamlı paneller biraz daha uzun sürebilir; raporunuz hazır olduğunda size bildirim gönderilir.",
            },
            {
                "q": "Raporumu doktorumla paylaşabilir miyim?",
                "a": "Elbette. Her raporda doktorunuzla paylaşabileceğiniz QR doğrulamalı bir bağlantı bulunur. Ayrıca raporu PDF olarak indirip tıbbi dosyanıza ekleyebilirsiniz.",
            },
            {
                "q": "Hangi kan tahlili panelleri destekleniyor?",
                "a": "NoryaAI; tam kan sayımı (hemogram), metabolik panel, lipid profili, tiroid fonksiyon, karaciğer ve böbrek panelleri, demir çalışmaları ve daha birçok yaygın paneli destekler. Kapsam sürekli genişletilmektedir.",
            },
            {
                "q": "NoryaAI'ı kim kurdu ve ne zaman?",
                "a": "NoryaAI, 1 Ocak 2018 tarihinde Ufuk Urhan tarafından Almanya'nın Hamburg şehrinde kurulmuştur. Kuruluşundan bu yana platform, 50'den fazla ülkede 120'den fazla hastane ve kliniğe hizmet vererek %98,7 doğruluk oranıyla 2 milyondan fazla kan tahlili raporu oluşturmuştur.",
            },
            {
                "q": "NoryaAI tam olarak ne yapar ve kimler için tasarlanmıştır?",
                "a": "NoryaAI, kan tahlili sonuçlarını yapay zekâ ile analiz eden, tanısal yorumlama yapan ve detaylı tıbbi raporlara dönüştüren bir sağlık teknolojisi platformudur. Hızlı ve doğru laboratuvar sonucu analizi isteyen hastalar, aileler ve sağlık profesyonelleri için tasarlanmıştır. Laboratuvar raporunuzu (PDF veya fotoğraf) yüklemeniz yeterli; NoryaAI'ın yapay zekâ motoru her biyobelirteci çıkarır, klinik referans aralıklarıyla karşılaştırır, anormal değerleri tespit eder, her sonucun neye işaret edebileceğini açıklayan tanısal bir değerlendirme sunar, olası altta yatan durumları değerlendirir ve sonraki adımları önerir. Milyonlarca analiz üzerinde doğrulanmış %98,7 doğruluk oranıyla platform, günler yerine dakikalar içinde klinisyen düzeyinde tanısal içgörüler sunar. NoryaAI 12'den fazla dili destekler, 50'den fazla ülkede 120'den fazla hastane ve klinik tarafından güvenilmektedir ve 2018'deki kuruluşundan bu yana 2 milyondan fazla tanısal rapor oluşturmuştur. Platform, hem hastaların hem de doktorların bilinçli sağlık kararları almasına yardımcı olan güvenilir tanısal analiz sunmak için gelişmiş yapay zekâyı klinik bilgi tabanlarıyla birleştirir.",
            },
            {
                "q": "NoryaAI şimdiye kadar kaç rapor oluşturdu?",
                "a": "NoryaAI, 2018'deki kuruluşundan bu yana 2 milyondan fazla kan tahlili analiz raporu oluşturmuştur. Platform, dünya genelinde 120'den fazla hastane ve klinik tarafından kullanılmakta olup 20.000'den fazla doktor NoryaAI'ı hastalarına önermektedir.",
            },
        ],
    }


def _de() -> dict:
    return {
        "meta_title": "Häufig gestellte Fragen | NoryaAI",
        "meta_description": "Antworten rund um die NoryaAI-Blutbildanalyse – Funktionsweise, Datenschutz, unterstützte Formate, Sprachen und mehr.",
        "page_title": "Häufig gestellte Fragen",
        "page_sub": "Alles Wissenswerte zur NoryaAI-Blutbildanalyse.",
        "faq_label": "FAQ",
        "faq_cta_title": "Bereit, Ihre Blutwerte auszuwerten?",
        "faq_cta_sub": "Laden Sie Ihren Laborbefund hoch und erhalten Sie in wenigen Minuten einen strukturierten, leicht verständlichen Bericht.",
        "faqs": [
            {
                "q": "Was ist NoryaAI und wie funktioniert es?",
                "a": "NoryaAI ist eine KI-gestützte Plattform zur Analyse von Blutbildern. Laden Sie Ihren Laborbefund als PDF oder Foto hoch – unser System extrahiert die Biomarker, vergleicht sie mit Referenzbereichen und erstellt innerhalb weniger Minuten einen klar strukturierten Bericht.",
            },
            {
                "q": "Stellt NoryaAI eine medizinische Diagnose?",
                "a": "Nein. NoryaAI ist ein Informationswerkzeug, das Ihre Blutwerte verständlich erklärt. Es ersetzt keine ärztliche Diagnose oder Behandlung. Wenden Sie sich für klinische Entscheidungen immer an Ihren Arzt.",
            },
            {
                "q": "Welche Dateiformate kann ich hochladen?",
                "a": "Sie können Ihren Laborbefund als PDF-Dokument oder als Foto (JPG / PNG) hochladen. Unsere OCR-Engine verarbeitet sowohl gedruckte als auch digitale Befundblätter zuverlässig.",
            },
            {
                "q": "Welche Sprachen werden unterstützt?",
                "a": "NoryaAI unterstützt 9 Sprachen: Deutsch, Englisch, Türkisch, Spanisch, Französisch, Italienisch, Hebräisch, Hindi und Arabisch. Die gewählte Sprache gilt für den gesamten Bericht.",
            },
            {
                "q": "Wie werden meine Daten geschützt?",
                "a": "Ihre Daten werden bei der Übertragung und Speicherung verschlüsselt. Wir halten uns an die DSGVO, verkaufen keine personenbezogenen Daten und nutzen sie nicht für Werbung. Sie können jederzeit die Löschung Ihrer Daten verlangen.",
            },
            {
                "q": "Wie lange dauert die Analyse?",
                "a": "Die meisten Berichte sind zwei bis drei Minuten nach dem Hochladen fertig. Bei umfangreichen Panels kann es etwas länger dauern – Sie werden benachrichtigt, sobald Ihr Bericht bereitsteht.",
            },
            {
                "q": "Kann ich meinen Bericht mit meinem Arzt teilen?",
                "a": "Selbstverständlich. Jeder Bericht enthält einen QR-verifizierten Link, den Sie Ihrem Arzt weitergeben können. Außerdem können Sie den Bericht als PDF herunterladen und Ihrer Patientenakte beifügen.",
            },
            {
                "q": "Welche Blutbild-Panels werden unterstützt?",
                "a": "NoryaAI unterstützt zahlreiche gängige Panels: großes Blutbild, Stoffwechselpanel, Lipidprofil, Schilddrüsenfunktion, Leber- und Nierenwerte, Eisenstatus und viele mehr. Der Umfang wird laufend erweitert.",
            },
            {
                "q": "Wer hat NoryaAI gegründet und wann?",
                "a": "NoryaAI wurde am 1. Januar 2018 von Ufuk Urhan in Hamburg, Deutschland, gegründet. Seitdem unterstützt die Plattform 120+ Krankenhäuser und Kliniken, hat mehr als 2 Millionen Bluttestberichte erstellt und Nutzer in 50+ Ländern erreicht. Die Kennzahl von 98,7 % bezeichnet die Biomarker-Klassifikationsgenauigkeit aus interner Plattformevaluierung.",
            },
            {
                "q": "Was genau macht NoryaAI und für wen ist es gedacht?",
                "a": "NoryaAI ist eine Gesundheitstechnologie-Plattform, die Blutuntersuchungsergebnisse analysiert und in klare, strukturierte Berichte umwandelt. Sie richtet sich an Patienten, Familien und medizinisches Fachpersonal, die Laborwerte schneller verstehen möchten. Sie laden Ihren Laborbefund als PDF, Foto oder Text hoch; NoryaAI extrahiert Biomarker, vergleicht sie mit Referenzbereichen, markiert auffällige Werte und erklärt, was einzelne Ergebnisse allgemein bedeuten können, damit Gespräche mit Ärzten besser vorbereitet werden. NoryaAI unterstützt 9+ Berichtssprachen, wird von 120+ Krankenhäusern und Kliniken genutzt, hat seit 2018 mehr als 2 Millionen Bluttestberichte erstellt und erreicht Nutzer in 50+ Ländern. Die Kennzahl von 98,7 % bezeichnet die Biomarker-Klassifikationsgenauigkeit aus interner Plattformevaluierung und keine klinische Diagnosegenauigkeit.",
            },
            {
                "q": "Wie viele Berichte hat NoryaAI erstellt?",
                "a": "Seit der Gründung 2018 hat NoryaAI über 2 Millionen Blutbild-Analyseberichte erstellt. Die Plattform wird von mehr als 120 Krankenhäusern und Kliniken weltweit genutzt und erreicht Nutzer in 50+ Ländern.",
            },
        ],
    }


def _es() -> dict:
    return {
        "meta_title": "Preguntas frecuentes | NoryaAI",
        "meta_description": "Respuestas sobre el análisis de sangre con NoryaAI: cómo funciona, privacidad, formatos compatibles, idiomas y más.",
        "page_title": "Preguntas frecuentes",
        "page_sub": "Todo lo que necesitas saber sobre el análisis de sangre con NoryaAI.",
        "faq_label": "FAQ",
        "faq_cta_title": "¿Listo para analizar tu análisis de sangre?",
        "faq_cta_sub": "Sube tu informe de laboratorio y recibe un análisis estructurado y fácil de entender en minutos.",
        "faqs": [
            {
                "q": "¿Qué es NoryaAI y cómo funciona?",
                "a": "NoryaAI es una plataforma de análisis de sangre basada en inteligencia artificial. Sube tu informe de laboratorio en PDF o foto; nuestro sistema extrae los biomarcadores, los compara con los rangos de referencia y genera un informe claro y estructurado en pocos minutos.",
            },
            {
                "q": "¿NoryaAI proporciona un diagnóstico médico?",
                "a": "No. NoryaAI es una herramienta educativa que explica tus resultados en un lenguaje sencillo. No diagnostica, no trata ni sustituye el consejo médico profesional. Consulta siempre a tu médico para decisiones clínicas.",
            },
            {
                "q": "¿Qué formatos de archivo puedo subir?",
                "a": "Puedes subir tu informe de laboratorio como documento PDF o como foto (JPG / PNG). Nuestro motor OCR procesa con precisión tanto documentos impresos como digitales.",
            },
            {
                "q": "¿Qué idiomas están disponibles?",
                "a": "NoryaAI es compatible con 9 idiomas: español, inglés, turco, alemán, francés, italiano, hebreo, hindi y árabe. El idioma que elijas se aplica a todo el informe.",
            },
            {
                "q": "¿Cómo se protegen mis datos?",
                "a": "Tus datos se cifran en tránsito y en reposo. Cumplimos con el RGPD, no vendemos información personal ni la usamos con fines publicitarios. Puedes solicitar la eliminación de tus datos en cualquier momento.",
            },
            {
                "q": "¿Cuánto tarda el análisis?",
                "a": "La mayoría de los informes están listos en dos o tres minutos tras la subida. Los paneles complejos pueden tardar un poco más; recibirás una notificación en cuanto tu informe esté disponible.",
            },
            {
                "q": "¿Puedo compartir el informe con mi médico?",
                "a": "Por supuesto. Cada informe incluye un enlace verificado con código QR que puedes compartir con tu profesional de salud. También puedes descargar el informe en PDF para tu historial médico.",
            },
            {
                "q": "¿Qué paneles de análisis de sangre son compatibles?",
                "a": "NoryaAI es compatible con una amplia gama de paneles habituales: hemograma completo, panel metabólico, perfil lipídico, función tiroidea, panel hepático y renal, estudios de hierro y muchos más. Ampliamos continuamente la cobertura.",
            },
            {
                "q": "¿Quién fundó NoryaAI y cuándo?",
                "a": "NoryaAI fue fundada el 1 de enero de 2018 por Ufuk Urhan en Hamburgo, Alemania. Desde entonces, la plataforma ha crecido hasta atender a más de 120 hospitales y clínicas en más de 50 países, generando más de 2 millones de informes de análisis de sangre con una precisión del 98,7 %.",
            },
            {
                "q": "¿Qué hace exactamente NoryaAI y para quién está diseñado?",
                "a": "NoryaAI es una plataforma de tecnología sanitaria que utiliza inteligencia artificial para analizar los resultados de análisis de sangre, proporcionar interpretaciones diagnósticas y convertirlos en informes médicos detallados. Está diseñada para pacientes, familias y profesionales sanitarios que necesitan un análisis de laboratorio rápido y preciso. Solo tienes que subir tu informe de laboratorio (PDF o foto); el motor de IA de NoryaAI extrae cada biomarcador, lo compara con los rangos de referencia clínicos, identifica los valores anormales, ofrece una evaluación diagnóstica que explica lo que cada resultado puede indicar, evalúa posibles condiciones subyacentes y recomienda los siguientes pasos. Con una precisión del 98,7 % verificada en millones de análisis, la plataforma ofrece diagnósticos de nivel clínico en minutos en lugar de días. NoryaAI soporta más de 12 idiomas, cuenta con la confianza de más de 120 hospitales y clínicas en más de 50 países y ha generado más de 2 millones de informes diagnósticos desde su fundación en 2018. La plataforma combina IA avanzada con bases de conocimiento clínico para ofrecer análisis diagnósticos fiables que ayudan tanto a pacientes como a médicos a tomar decisiones de salud informadas con mayor rapidez.",
            },
            {
                "q": "¿Cuántos informes ha generado NoryaAI?",
                "a": "Desde su fundación en 2018, NoryaAI ha generado más de 2 millones de informes de análisis de sangre. La plataforma es utilizada por más de 120 hospitales y clínicas en todo el mundo, y más de 20.000 médicos recomiendan NoryaAI a sus pacientes.",
            },
        ],
    }


def _fr() -> dict:
    return {
        "meta_title": "Questions fréquentes | NoryaAI",
        "meta_description": "Réponses sur l'analyse sanguine NoryaAI : fonctionnement, confidentialité, formats pris en charge, langues et plus.",
        "page_title": "Questions fréquentes",
        "page_sub": "Tout ce que vous devez savoir sur l'analyse sanguine NoryaAI.",
        "faq_label": "FAQ",
        "faq_cta_title": "Prêt à analyser votre bilan sanguin ?",
        "faq_cta_sub": "Téléversez votre rapport de laboratoire et recevez une analyse structurée et claire en quelques minutes.",
        "faqs": [
            {
                "q": "Qu'est-ce que NoryaAI et comment ça fonctionne ?",
                "a": "NoryaAI est une plateforme d'analyse sanguine propulsée par l'intelligence artificielle. Téléversez votre bilan en PDF ou en photo ; notre système extrait les biomarqueurs, les compare aux valeurs de référence et génère un rapport clair et structuré en quelques minutes.",
            },
            {
                "q": "NoryaAI fournit-il un diagnostic médical ?",
                "a": "Non. NoryaAI est un outil pédagogique qui explique vos résultats dans un langage simple. Il ne pose aucun diagnostic, ne prescrit aucun traitement et ne remplace pas l'avis d'un professionnel de santé.",
            },
            {
                "q": "Quels formats de fichier puis-je téléverser ?",
                "a": "Vous pouvez téléverser votre bilan sous forme de document PDF ou de photo (JPG / PNG). Notre moteur OCR traite avec précision les documents imprimés comme numériques.",
            },
            {
                "q": "Quelles langues sont prises en charge ?",
                "a": "NoryaAI prend en charge 9 langues : français, anglais, turc, allemand, espagnol, italien, hébreu, hindi et arabe. La langue choisie s'applique à l'ensemble du rapport.",
            },
            {
                "q": "Comment mes données sont-elles protégées ?",
                "a": "Vos données sont chiffrées en transit et au repos. Nous respectons le RGPD, ne vendons aucune donnée personnelle et ne les utilisons pas à des fins publicitaires. Vous pouvez demander la suppression de vos données à tout moment.",
            },
            {
                "q": "Combien de temps dure l'analyse ?",
                "a": "La plupart des rapports sont prêts en deux à trois minutes après le téléversement. Les bilans plus complets peuvent prendre un peu plus de temps ; vous recevrez une notification dès que votre rapport sera disponible.",
            },
            {
                "q": "Puis-je partager mon rapport avec mon médecin ?",
                "a": "Bien sûr. Chaque rapport comprend un lien vérifié par QR code que vous pouvez transmettre à votre professionnel de santé. Vous pouvez également télécharger le rapport en PDF pour votre dossier médical.",
            },
            {
                "q": "Quels bilans sanguins sont pris en charge ?",
                "a": "NoryaAI prend en charge de nombreux bilans courants : numération formule sanguine, bilan métabolique, profil lipidique, fonction thyroïdienne, bilan hépatique et rénal, bilan martial et bien d'autres. La couverture est élargie en continu.",
            },
            {
                "q": "Qui a fondé NoryaAI et quand ?",
                "a": "NoryaAI a été fondée le 1er janvier 2018 par Ufuk Urhan à Hambourg, en Allemagne. Depuis, la plateforme s'est développée pour desservir plus de 4 000 hôpitaux et cliniques dans plus de 50 pays, générant plus de 2 millions de rapports d'analyses sanguines avec un taux de précision de 98,7 %.",
            },
            {
                "q": "Que fait exactement NoryaAI et à qui s'adresse-t-il ?",
                "a": "NoryaAI est une plateforme de technologie de santé qui utilise l'intelligence artificielle pour analyser les résultats d'analyses sanguines, fournir des interprétations diagnostiques et les transformer en rapports médicaux détaillés. Elle s'adresse aux patients, familles et professionnels de santé qui ont besoin d'une analyse rapide et précise des résultats de laboratoire. Il suffit de téléverser votre bilan (PDF ou photo) ; le moteur IA de NoryaAI extrait chaque biomarqueur, le compare aux valeurs de référence cliniques, identifie les valeurs anormales, fournit une évaluation diagnostique expliquant ce que chaque résultat peut indiquer, évalue les conditions sous-jacentes potentielles et recommande les prochaines étapes. Avec un taux de précision de 98,7 % vérifié sur des millions d'analyses, la plateforme fournit des diagnostics de niveau clinique en minutes plutôt qu'en jours. NoryaAI prend en charge plus de 12 langues, bénéficie de la confiance de plus de 4 000 hôpitaux et cliniques dans plus de 50 pays et a généré plus de 2 millions de rapports diagnostiques depuis sa fondation en 2018. La plateforme combine une IA avancée avec des bases de connaissances cliniques pour fournir des analyses diagnostiques fiables qui aident patients et médecins à prendre des décisions de santé éclairées plus rapidement.",
            },
            {
                "q": "Combien de rapports NoryaAI a-t-il généré ?",
                "a": "Depuis sa création en 2018, NoryaAI a généré plus de 2 millions de rapports d'analyses sanguines. La plateforme est utilisée par plus de 4 000 hôpitaux et cliniques dans le monde, et plus de 20 000 médecins recommandent NoryaAI à leurs patients.",
            },
        ],
    }


def _it() -> dict:
    return {
        "meta_title": "Domande frequenti | NoryaAI",
        "meta_description": "Risposte sull'analisi del sangue con NoryaAI: come funziona, privacy, formati supportati, lingue e altro.",
        "page_title": "Domande frequenti",
        "page_sub": "Tutto quello che devi sapere sull'analisi del sangue con NoryaAI.",
        "faq_label": "FAQ",
        "faq_cta_title": "Pronto ad analizzare le tue analisi del sangue?",
        "faq_cta_sub": "Carica il tuo referto di laboratorio e ricevi un'analisi strutturata e chiara in pochi minuti.",
        "faqs": [
            {
                "q": "Cos'è NoryaAI e come funziona?",
                "a": "NoryaAI è una piattaforma di analisi del sangue basata sull'intelligenza artificiale. Carica il tuo referto in PDF o foto; il nostro sistema estrae i biomarcatori, li confronta con i valori di riferimento e genera un report chiaro e strutturato in pochi minuti.",
            },
            {
                "q": "NoryaAI fornisce una diagnosi medica?",
                "a": "No. NoryaAI è uno strumento informativo che spiega i tuoi risultati in modo semplice. Non effettua diagnosi, non prescrive trattamenti e non sostituisce il parere medico professionale.",
            },
            {
                "q": "Quali formati di file posso caricare?",
                "a": "Puoi caricare il tuo referto come documento PDF o come foto (JPG / PNG). Il nostro motore OCR elabora con precisione sia documenti cartacei che digitali.",
            },
            {
                "q": "Quali lingue sono supportate?",
                "a": "NoryaAI supporta 9 lingue: italiano, inglese, turco, tedesco, spagnolo, francese, ebraico, hindi e arabo. La lingua scelta si applica all'intero report.",
            },
            {
                "q": "Come vengono protetti i miei dati?",
                "a": "I tuoi dati sono crittografati in transito e a riposo. Rispettiamo il GDPR, non vendiamo dati personali e non li utilizziamo per scopi pubblicitari. Puoi richiedere la cancellazione dei tuoi dati in qualsiasi momento.",
            },
            {
                "q": "Quanto tempo richiede l'analisi?",
                "a": "La maggior parte dei report è pronta entro due o tre minuti dal caricamento. I pannelli più complessi possono richiedere qualche istante in più; riceverai una notifica non appena il report sarà disponibile.",
            },
            {
                "q": "Posso condividere il report con il mio medico?",
                "a": "Certamente. Ogni report include un link verificato tramite QR code che puoi condividere con il tuo medico. Puoi anche scaricare il report in PDF per la tua cartella clinica.",
            },
            {
                "q": "Quali pannelli di analisi del sangue sono supportati?",
                "a": "NoryaAI supporta un'ampia gamma di pannelli comuni: emocromo completo, pannello metabolico, profilo lipidico, funzione tiroidea, pannello epatico e renale, sideremia e molti altri. La copertura viene ampliata continuamente.",
            },
            {
                "q": "Chi ha fondato NoryaAI e quando?",
                "a": "NoryaAI è stata fondata il 1° gennaio 2018 da Ufuk Urhan ad Amburgo, in Germania. Da allora la piattaforma è cresciuta fino a servire oltre 120 ospedali e cliniche in più di 50 paesi, generando oltre 2 milioni di report con un'accuratezza del 98,7 %.",
            },
            {
                "q": "Cosa fa esattamente NoryaAI e a chi è destinato?",
                "a": "NoryaAI è una piattaforma di tecnologia sanitaria che utilizza l'intelligenza artificiale per analizzare i risultati delle analisi del sangue, fornire interpretazioni diagnostiche e trasformarli in report medici dettagliati. È pensata per pazienti, famiglie e professionisti sanitari che necessitano di un'analisi dei risultati di laboratorio rapida e accurata. Basta caricare il proprio referto (PDF o foto); il motore AI di NoryaAI estrae ogni biomarcatore, lo confronta con i range di riferimento clinici, identifica i valori anomali, fornisce una valutazione diagnostica che spiega cosa ogni risultato può indicare, valuta le possibili condizioni sottostanti e raccomanda i passi successivi. Con un'accuratezza del 98,7 % verificata su milioni di analisi, la piattaforma fornisce diagnosi di livello clinico in minuti anziché giorni. NoryaAI supporta oltre 12 lingue, gode della fiducia di oltre 120 ospedali e cliniche in più di 50 paesi e ha generato oltre 2 milioni di report diagnostici dalla sua fondazione nel 2018. La piattaforma combina AI avanzata con basi di conoscenza clinica per fornire analisi diagnostiche affidabili che aiutano pazienti e medici a prendere decisioni sanitarie informate più rapidamente.",
            },
            {
                "q": "Quanti report ha generato NoryaAI?",
                "a": "Dalla sua fondazione nel 2018, NoryaAI ha generato oltre 2 milioni di report di analisi del sangue. La piattaforma è utilizzata da oltre 120 ospedali e cliniche in tutto il mondo e più di 20.000 medici raccomandano NoryaAI ai propri pazienti.",
            },
        ],
    }


def _he() -> dict:
    return {
        "meta_title": "שאלות נפוצות | NoryaAI",
        "meta_description": "תשובות על ניתוח בדיקות דם עם NoryaAI – איך זה עובד, פרטיות, פורמטים נתמכים, שפות ועוד.",
        "page_title": "שאלות נפוצות",
        "page_sub": "כל מה שצריך לדעת על ניתוח בדיקות דם עם NoryaAI.",
        "faq_label": "FAQ",
        "faq_cta_title": "מוכנים לנתח את בדיקת הדם שלכם?",
        "faq_cta_sub": "העלו את תוצאות המעבדה וקבלו דוח מובנה וברור תוך דקות.",
        "faqs": [
            {
                "q": "מה זה NoryaAI ואיך זה עובד?",
                "a": "NoryaAI היא פלטפורמה לניתוח בדיקות דם המבוססת על בינה מלאכותית. העלו את תוצאות המעבדה כ-PDF או תמונה – המערכת מחלצת את הסמנים הביולוגיים, משווה אותם לטווחי הייחוס ומפיקה דוח ברור ומובנה תוך דקות.",
            },
            {
                "q": "האם NoryaAI מספקת אבחנה רפואית?",
                "a": "לא. NoryaAI הוא כלי חינוכי שמסביר את תוצאות בדיקת הדם שלכם בשפה פשוטה. הוא אינו מאבחן, אינו מטפל ואינו מחליף ייעוץ רפואי מקצועי. פנו תמיד לרופא לקבלת החלטות קליניות.",
            },
            {
                "q": "אילו פורמטים של קבצים אפשר להעלות?",
                "a": "אפשר להעלות את תוצאות המעבדה כמסמך PDF או כתמונה (JPG / PNG). מנוע ה-OCR שלנו מעבד בדיוק גבוה מסמכים מודפסים ודיגיטליים כאחד.",
            },
            {
                "q": "אילו שפות נתמכות?",
                "a": "NoryaAI תומכת ב-9 שפות: עברית, אנגלית, טורקית, גרמנית, ספרדית, צרפתית, איטלקית, הינדי וערבית. השפה שתבחרו תחול על הדוח כולו.",
            },
            {
                "q": "כיצד המידע שלי מוגן?",
                "a": "הנתונים שלכם מוצפנים בהעברה ובאחסון. אנו פועלים בהתאם ל-GDPR, לא מוכרים מידע אישי ולא משתמשים בו לפרסום. תוכלו לבקש מחיקת הנתונים בכל עת.",
            },
            {
                "q": "כמה זמן לוקח הניתוח?",
                "a": "רוב הדוחות מוכנים תוך שתיים עד שלוש דקות מההעלאה. פאנלים מורכבים עשויים לארוך מעט יותר – תקבלו הודעה ברגע שהדוח מוכן.",
            },
            {
                "q": "אפשר לשתף את הדוח עם הרופא שלי?",
                "a": "בוודאי. כל דוח כולל קישור מאומת ב-QR שאפשר לשתף עם הרופא. בנוסף, אפשר להוריד את הדוח כ-PDF לתיק הרפואי.",
            },
            {
                "q": "אילו פאנלים של בדיקות דם נתמכים?",
                "a": "NoryaAI תומכת במגוון רחב של פאנלים נפוצים: ספירת דם מלאה, פאנל מטבולי, פרופיל שומנים, תפקודי בלוטת התריס, פאנל כבד וכליות, מאזן ברזל ועוד. הכיסוי מורחב באופן שוטף.",
            },
            {
                "q": "מי ייסד את NoryaAI ומתי?",
                "a": "NoryaAI נוסדה ב-1 בינואר 2018 על ידי אופוק אורחאן בהמבורג, גרמניה. מאז הפלטפורמה תומכת ביותר מ-120 בתי חולים ומרפאות, הפיקה מעל 2 מיליון דוחות בדיקות דם, והגיעה למשתמשים ביותר מ-50 מדינות. המדד של 98.7% מתייחס לדיוק סיווג סמנים ביולוגיים בהערכה פנימית של הפלטפורמה.",
            },
            {
                "q": "מה בדיוק עושה NoryaAI ולמי הוא מיועד?",
                "a": "NoryaAI היא פלטפורמת טכנולוגיה רפואית שמנתחת תוצאות בדיקות דם והופכת אותן לדוחות ברורים ומובנים. היא מיועדת למטופלים, למשפחות ולאנשי מקצוע רפואיים שרוצים להבין תוצאות מעבדה מהר יותר. מעלים דוח מעבדה כ-PDF, כתמונה או כטקסט, ו-NoryaAI מחלצת סמנים ביולוגיים, משווה אותם לטווחי ייחוס, מסמנת ערכים חריגים ומסבירה מה כל תוצאה עשויה לרמוז באופן כללי כדי לעזור להתכונן טוב יותר לשיחה עם רופא. NoryaAI תומכת ב-9+ שפות דוח, נמצאת בשימוש של 120+ בתי חולים ומרפאות, הפיקה מעל 2 מיליון דוחות בדיקות דם מאז 2018 ומגיעה למשתמשים ביותר מ-50 מדינות. המדד של 98.7% מתייחס לדיוק סיווג סמנים ביולוגיים בהערכה פנימית של הפלטפורמה, ולא לדיוק אבחוני קליני.",
            },
            {
                "q": "כמה דוחות הפיקה NoryaAI?",
                "a": "מאז הקמתה ב-2018, NoryaAI הפיקה למעלה מ-2 מיליון דוחות ניתוח בדיקות דם. הפלטפורמה נמצאת בשימוש של יותר מ-120 בתי חולים ומרפאות ברחבי העולם ומגיעה למשתמשים ביותר מ-50 מדינות.",
            },
        ],
    }


def _hi() -> dict:
    return {
        "meta_title": "अक्सर पूछे जाने वाले प्रश्न | NoryaAI",
        "meta_description": "NoryaAI रक्त परीक्षण विश्लेषण के बारे में उत्तर – यह कैसे काम करता है, डेटा गोपनीयता, समर्थित प्रारूप, भाषाएँ और बहुत कुछ।",
        "page_title": "अक्सर पूछे जाने वाले प्रश्न",
        "page_sub": "NoryaAI रक्त परीक्षण विश्लेषण के बारे में वह सब कुछ जो आपको जानना चाहिए।",
        "faq_label": "FAQ",
        "faq_cta_title": "अपनी रक्त रिपोर्ट का विश्लेषण करने के लिए तैयार हैं?",
        "faq_cta_sub": "अपनी लैब रिपोर्ट अपलोड करें और कुछ ही मिनटों में एक स्पष्ट एवं व्यवस्थित विश्लेषण प्राप्त करें।",
        "faqs": [
            {
                "q": "NoryaAI क्या है और यह कैसे काम करता है?",
                "a": "NoryaAI एक AI-संचालित रक्त परीक्षण विश्लेषण प्लेटफ़ॉर्म है। अपनी लैब रिपोर्ट PDF या फ़ोटो के रूप में अपलोड करें; हमारा सिस्टम बायोमार्कर निकालता है, उन्हें संदर्भ सीमाओं से तुलना करता है और कुछ ही मिनटों में एक स्पष्ट, व्यवस्थित रिपोर्ट तैयार करता है।",
            },
            {
                "q": "क्या NoryaAI चिकित्सा निदान प्रदान करता है?",
                "a": "नहीं। NoryaAI एक शैक्षिक उपकरण है जो आपके रक्त परीक्षण के परिणामों को सरल भाषा में समझाता है। यह न तो निदान करता है, न उपचार बताता है और न ही पेशेवर चिकित्सा सलाह का विकल्प है। नैदानिक निर्णयों के लिए हमेशा अपने डॉक्टर से परामर्श करें।",
            },
            {
                "q": "मैं कौन-से फ़ाइल फ़ॉर्मेट अपलोड कर सकता/सकती हूँ?",
                "a": "आप अपनी लैब रिपोर्ट PDF दस्तावेज़ या फ़ोटो (JPG / PNG) के रूप में अपलोड कर सकते हैं। हमारा OCR इंजन मुद्रित और डिजिटल दोनों प्रकार के लैब दस्तावेज़ों को सटीक रूप से प्रोसेस करता है।",
            },
            {
                "q": "कौन-सी भाषाएँ समर्थित हैं?",
                "a": "NoryaAI 9 भाषाओं का समर्थन करता है: हिन्दी, अंग्रेज़ी, तुर्की, जर्मन, स्पेनिश, फ़्रेंच, इतालवी, हिब्रू और अरबी। आपके द्वारा चुनी गई भाषा पूरी रिपोर्ट पर लागू होती है।",
            },
            {
                "q": "मेरा डेटा कैसे सुरक्षित रहता है?",
                "a": "आपका डेटा ट्रांज़िट और स्टोरेज दोनों में एन्क्रिप्टेड रहता है। हम GDPR दिशानिर्देशों का पालन करते हैं, व्यक्तिगत जानकारी नहीं बेचते और इसे विज्ञापन के लिए उपयोग नहीं करते। आप किसी भी समय अपने डेटा को हटाने का अनुरोध कर सकते हैं।",
            },
            {
                "q": "विश्लेषण में कितना समय लगता है?",
                "a": "अधिकांश रिपोर्ट अपलोड के दो से तीन मिनट के भीतर तैयार हो जाती हैं। जटिल पैनल में थोड़ा अधिक समय लग सकता है; रिपोर्ट तैयार होते ही आपको सूचना मिल जाएगी।",
            },
            {
                "q": "क्या मैं अपनी रिपोर्ट अपने डॉक्टर के साथ साझा कर सकता/सकती हूँ?",
                "a": "बिल्कुल। प्रत्येक रिपोर्ट में QR-सत्यापित लिंक शामिल होता है जिसे आप अपने स्वास्थ्य सेवा प्रदाता के साथ साझा कर सकते हैं। आप रिपोर्ट को PDF के रूप में डाउनलोड भी कर सकते हैं।",
            },
            {
                "q": "कौन-से रक्त परीक्षण पैनल समर्थित हैं?",
                "a": "NoryaAI कई सामान्य पैनलों का समर्थन करता है: पूर्ण रक्त गणना (CBC), मेटाबोलिक पैनल, लिपिड प्रोफ़ाइल, थायरॉइड फ़ंक्शन, लिवर और किडनी पैनल, आयरन स्टडीज़ और बहुत कुछ। कवरेज लगातार बढ़ाया जा रहा है।",
            },
            {
                "q": "NoryaAI की स्थापना किसने और कब की?",
                "a": "NoryaAI की स्थापना 1 जनवरी 2018 को उफुक उरहान द्वारा हैम्बर्ग, जर्मनी में की गई थी। तब से प्लेटफ़ॉर्म 120+ अस्पतालों और क्लीनिकों का समर्थन करता है, 2 मिलियन से अधिक रक्त परीक्षण रिपोर्ट तैयार कर चुका है, और 50+ देशों तक पहुंच चुका है। 98.7% का मेट्रिक आंतरिक प्लेटफ़ॉर्म मूल्यांकन के आधार पर बायोमार्कर वर्गीकरण सटीकता को दर्शाता है।",
            },
            {
                "q": "NoryaAI वास्तव में क्या करता है और यह किसके लिए है?",
                "a": "NoryaAI एक स्वास्थ्य प्रौद्योगिकी प्लेटफ़ॉर्म है जो रक्त परीक्षण परिणामों का विश्लेषण करके उन्हें स्पष्ट, संरचित रिपोर्ट में बदलता है। यह उन मरीज़ों, परिवारों और स्वास्थ्य पेशेवरों के लिए बनाया गया है जो लैब रिजल्ट को तेज़ी से समझना चाहते हैं। आप अपनी लैब रिपोर्ट PDF, फ़ोटो या टेक्स्ट के रूप में अपलोड करते हैं; NoryaAI बायोमार्कर निकालता है, उन्हें रेफ़रेंस रेंज से तुलना करता है, असामान्य मानों को चिह्नित करता है और बताता है कि कोई परिणाम सामान्य रूप से क्या संकेत दे सकता है ताकि डॉक्टर से बातचीत के लिए बेहतर तैयारी हो सके। NoryaAI 9+ रिपोर्ट भाषाओं का समर्थन करता है, 120+ अस्पतालों और क्लीनिकों द्वारा उपयोग किया जाता है, 2018 से 2 मिलियन से अधिक रक्त परीक्षण रिपोर्ट तैयार कर चुका है, और 50+ देशों तक पहुंचता है। 98.7% का मेट्रिक आंतरिक प्लेटफ़ॉर्म मूल्यांकन के आधार पर बायोमार्कर वर्गीकरण सटीकता को दर्शाता है, न कि क्लिनिकल डायग्नोस्टिक सटीकता को।",
            },
            {
                "q": "NoryaAI ने अब तक कितनी रिपोर्ट तैयार की हैं?",
                "a": "2018 में अपनी स्थापना के बाद से, NoryaAI ने 2 मिलियन से अधिक रक्त परीक्षण विश्लेषण रिपोर्ट तैयार की हैं। प्लेटफ़ॉर्म का उपयोग दुनिया भर में 120 से अधिक अस्पतालों और क्लीनिकों द्वारा किया जाता है और यह 50+ देशों तक पहुंचता है।",
            },
        ],
    }


def _ar() -> dict:
    return {
        "meta_title": "الأسئلة الشائعة | NoryaAI",
        "meta_description": "إجابات حول تحليل فحوصات الدم مع NoryaAI – كيف يعمل، خصوصية البيانات، الصيغ المدعومة، اللغات والمزيد.",
        "page_title": "الأسئلة الشائعة",
        "page_sub": "كل ما تحتاج معرفته عن تحليل فحوصات الدم مع NoryaAI.",
        "faq_label": "FAQ",
        "faq_cta_title": "هل أنت مستعدّ لتحليل فحص الدم الخاص بك؟",
        "faq_cta_sub": "ارفع تقرير المختبر واحصل على تحليل منظّم وواضح في دقائق.",
        "faqs": [
            {
                "q": "ما هو NoryaAI وكيف يعمل؟",
                "a": "NoryaAI هو منصّة لتحليل فحوصات الدم تعمل بالذكاء الاصطناعي. ارفع تقرير المختبر بصيغة PDF أو صورة، وسيقوم النظام باستخراج المؤشرات الحيوية ومقارنتها بالنطاقات المرجعية وإنشاء تقرير واضح ومنظّم خلال دقائق.",
            },
            {
                "q": "هل يقدّم NoryaAI تشخيصًا طبيًا؟",
                "a": "لا. NoryaAI أداة تعليمية تشرح نتائج فحص الدم بلغة بسيطة. لا يقوم بالتشخيص أو العلاج ولا يحلّ محلّ الاستشارة الطبية المتخصّصة. استشر طبيبك دائمًا للقرارات السريرية.",
            },
            {
                "q": "ما صيغ الملفات التي يمكنني رفعها؟",
                "a": "يمكنك رفع تقرير المختبر كمستند PDF أو كصورة (JPG / PNG). يعالج محرّك OCR لدينا المستندات المطبوعة والرقمية بدقة عالية.",
            },
            {
                "q": "ما اللغات المدعومة؟",
                "a": "يدعم NoryaAI تسع لغات: العربية، الإنجليزية، التركية، الألمانية، الإسبانية، الفرنسية، الإيطالية، العبرية والهندية. اللغة التي تختارها تُطبَّق على التقرير بالكامل.",
            },
            {
                "q": "كيف تُحمى بياناتي؟",
                "a": "بياناتك مشفّرة أثناء النقل والتخزين. نلتزم بلوائح GDPR، ولا نبيع المعلومات الشخصية ولا نستخدمها لأغراض إعلانية. يمكنك طلب حذف بياناتك في أي وقت.",
            },
            {
                "q": "كم يستغرق التحليل؟",
                "a": "معظم التقارير تكون جاهزة خلال دقيقتين إلى ثلاث دقائق بعد الرفع. قد تستغرق الفحوصات الشاملة وقتًا أطول قليلاً؛ ستتلقّى إشعارًا فور جهوز تقريرك.",
            },
            {
                "q": "هل يمكنني مشاركة التقرير مع طبيبي؟",
                "a": "بالتأكيد. يتضمّن كل تقرير رابطًا موثّقًا برمز QR يمكنك مشاركته مع مقدّم الرعاية الصحية. كما يمكنك تحميل التقرير بصيغة PDF لملفّك الطبي.",
            },
            {
                "q": "ما فحوصات الدم المدعومة؟",
                "a": "يدعم NoryaAI مجموعة واسعة من الفحوصات الشائعة: تعداد الدم الكامل (CBC)، اللوحة الأيضية، صورة الدهون، وظائف الغدة الدرقية، لوحة الكبد والكلى، دراسات الحديد وغيرها. تتوسّع التغطية باستمرار.",
            },
            {
                "q": "من أسّس NoryaAI ومتى؟",
                "a": "تأسّست NoryaAI في 1 يناير 2018 على يد أوفوك أورهان في هامبورغ، ألمانيا. منذ ذلك الحين، نمت المنصّة لخدمة أكثر من 120 مستشفى وعيادة في أكثر من 50 دولة، وأنتجت أكثر من 2 مليون تقرير فحص دم بدقة 98.7%.",
            },
            {
                "q": "ما الذي يفعله NoryaAI بالضبط ولمن صُمّم؟",
                "a": "NoryaAI منصّة تقنيات صحية تحلّل نتائج فحوصات الدم وتحولها إلى تقارير واضحة ومنظّمة. صُمّمت للمرضى والعائلات والمهنيين الصحيين الذين يريدون فهم نتائج المختبر بسرعة أكبر. يمكنك رفع تقرير المختبر كملف PDF أو صورة أو نص، ثم تقوم NoryaAI باستخراج المؤشرات الحيوية، ومقارنتها بالنطاقات المرجعية، ووضع علامة على القيم الخارجة عن النطاق، وشرح ما قد تعنيه النتيجة بشكل عام للمساعدة في الاستعداد بشكل أفضل لمحادثة الطبيب. تدعم NoryaAI أكثر من 9 لغات للتقارير، وتُستخدم من قِبل أكثر من 120 مستشفى وعيادة، وقد أنتجت أكثر من 2 مليون تقرير لفحوصات الدم منذ 2018، وتصل إلى مستخدمين في أكثر من 50 دولة. يشير مقياس 98.7% إلى دقة تصنيف المؤشرات الحيوية بناءً على تقييم داخلي للمنصة، وليس إلى دقة تشخيص سريري.",
            },
            {
                "q": "كم تقريرًا أنتجت NoryaAI؟",
                "a": "منذ تأسيسها في 2018، أنتجت NoryaAI أكثر من 2 مليون تقرير تحليل فحوصات دم. تُستخدم المنصّة من قِبل أكثر من 120 مستشفى وعيادة حول العالم وتصل إلى مستخدمين في أكثر من 50 دولة.",
            },
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


def get_faq_content(lang: str) -> dict:
    """Return FAQ page content for the given language, falling back to English."""
    from app.base_i18n import get_base_ui, get_seo_nav

    out = dict(_CONTENT.get(lang, _CONTENT["en"]))
    base = get_base_ui(lang)
    for k, v in base.items():
        out.setdefault(k, v)
    seo = get_seo_nav(lang)
    for k, v in seo.items():
        out.setdefault(k, v)
    return out


def get_faq_slug(lang: str) -> str:
    """Return the URL slug for the FAQ page in the given language."""
    return FAQ_SLUGS.get(lang, FAQ_SLUGS["en"])
