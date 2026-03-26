# -*- coding: utf-8 -*-
"""Shared FAQ blocks for B2B audience pages (same Q&A across slugs per locale)."""

from __future__ import annotations

from typing import Any

_FAQ: dict[str, list[dict[str, Any]]] = {
    "de": [
        {
            "q": "Ist Norya ein Medizinprodukt oder ein Diagnostiksystem?",
            "a": "Nein. Norya ist assistierende Software, die Labordaten in strukturierte, mehrsprachige Patientenerklärungen für die ärztliche Durchsicht verwandelt.",
        },
        {
            "q": "Wie wird Datenschutz gehandhabt?",
            "a": "Wir nutzen Verschlüsselung während der Übertragung und gestufte Datenverarbeitungsrichtlinien. Unternehmensfunktionen (SSO, AVV/DPAs und wo zutreffend BAA) sind für klinische Teams verfügbar.",
        },
        {
            "q": "Welche Regionen werden unterstützt?",
            "a": "Wir betreuen Teams in über 50 Ländern, mit Lokalisierung für mehr als 9 Berichtssprachen.",
        },
        {
            "q": "Können Sie unsere LIMS- oder EMR-Lösung anbinden?",
            "a": "Ja. Wir arbeiten mit Standard-Laborexporten und üblichen Integrationsmustern. Kontaktieren Sie den Vertrieb, um die Anbindung an Ihre Umgebung abzustimmen.",
        },
        {
            "q": "Welche Genauigkeit geben Sie an?",
            "a": "In unserer internen Plattformbewertung liegt die Biomarker-Klassifikationsgenauigkeit bei strukturierten Laboreingaben bei 98,7 %—nicht die klinische diagnostische Genauigkeit.",
        },
        {
            "q": "Wie starten wir einen Pilot?",
            "a": "Buchen Sie eine Demo über das Unternehmensformular. Wir klären mit Ihrem Team Volumen, Sprachen und Governance.",
        },
    ],
    "fr": [
        {
            "q": "Norya est-il un dispositif médical ou un outil de diagnostic ?",
            "a": "Non. Norya est un logiciel d’aide qui transforme les données de laboratoire en explications patient structurées et multilingues pour reprise par les cliniciens.",
        },
        {
            "q": "Comment la protection des données est-elle assurée ?",
            "a": "Nous appliquons le chiffrement en transit et des politiques de traitement à plusieurs niveaux. Les contrôles entreprise (SSO, DPA et BAA lorsque applicable) sont disponibles pour les équipes cliniques.",
        },
        {
            "q": "Quelles régions sont prises en charge ?",
            "a": "Nous accompagnons des équipes dans plus de 50 pays, avec localisation sur plus de 9 langues de rapport.",
        },
        {
            "q": "Pouvez-vous vous intégrer à notre LIMS ou EMR ?",
            "a": "Oui. Nous utilisons les exports labo standards et des schémas d’intégration habituels. Contactez les ventes pour l’alignement avec votre stack.",
        },
        {
            "q": "Quelle précision revendiquez-vous ?",
            "a": "Notre évaluation interne sur plateforme fait état de 98,7 % de précision de classification des biomarqueurs sur entrées structurées—pas de précision diagnostique clinique.",
        },
        {
            "q": "Comment démarrer un pilote ?",
            "a": "Réservez une démo via le formulaire entreprise. Nous cadrons volume, langues et gouvernance avec votre équipe.",
        },
    ],
    "it": [
        {
            "q": "Norya è un dispositivo medico o uno strumento diagnostico?",
            "a": "No. Norya è software assistivo che trasforma i dati di laboratorio in spiegazioni per il paziente strutturate e multilingue, da revisionare dai clinici.",
        },
        {
            "q": "Come gestite la protezione dei dati?",
            "a": "Applichiamo crittografia in transito e policy di trattamento a livelli. Controlli enterprise (SSO, DPA e BAA dove applicabile) sono disponibili per i team clinici.",
        },
        {
            "q": "Quali regioni supportate?",
            "a": "Serviamo team in oltre 50 paesi, con localizzazione in più di 9 lingue di report.",
        },
        {
            "q": "Potete integrarvi con LIMS o EMR?",
            "a": "Sì. Lavoriamo con export di laboratorio standard e pattern di integrazione enterprise. Contattate le vendite per allinearvi allo stack.",
        },
        {
            "q": "Quale accuratezza dichiarate?",
            "a": "La nostra valutazione interna riporta il 98,7% di accuratezza di classificazione dei biomarcatori su input strutturati—non accuratezza diagnostica clinica.",
        },
        {
            "q": "Come iniziamo un pilota?",
            "a": "Prenotate una demo dal modulo corporate. Definiamo volumi, lingue e governance con il vostro team.",
        },
    ],
    "es": [
        {
            "q": "¿Es Norya un dispositivo médico o de diagnóstico?",
            "a": "No. Norya es software asistencial que convierte datos de laboratorio en explicaciones estructuradas y multilingües para revisión clínica.",
        },
        {
            "q": "¿Cómo cuidan la protección de datos?",
            "a": "Aplicamos cifrado en tránsito y políticas de tratamiento por niveles. Los controles empresariales (SSO, DPA y BAA cuando aplique) están disponibles para equipos clínicos.",
        },
        {
            "q": "¿Qué regiones cubren?",
            "a": "Atendemos equipos en más de 50 países, con localización en más de 9 idiomas de informe.",
        },
        {
            "q": "¿Se integran con nuestro LIMS o EMR?",
            "a": "Sí. Trabajamos con exportaciones estándar y patrones de integración habituales. Contacte a ventas para alinearlo a su stack.",
        },
        {
            "q": "¿Qué precisión declaran?",
            "a": "Nuestra evaluación interna informa un 98,7 % de precisión en clasificación de biomarcadores con entradas estructuradas—no precisión diagnóstica clínica.",
        },
        {
            "q": "¿Cómo iniciamos un piloto?",
            "a": "Reserve una demo por el formulario corporativo. Afinamos volumen, idiomas y gobernanza con su equipo.",
        },
    ],
    "he": [
        {
            "q": "האם נוריאה מכשיר רפואי או כלי אבחון?",
            "a": "לא. נוריאה היא תוכנה מסייעת המהפכת נתוני מעבדה להסברים מובנים ורבי־לשון לבדיקה קלינית.",
        },
        {
            "q": "איך מטפלים בהגנת מידע?",
            "a": "אנו מפעילים הצפנה במעבר ומדיניות טיפול בשכבות. בקרות ארגוניות (SSO, DPA ו־BAA כשחל) זמינות לצוותים קליניים.",
        },
        {
            "q": "אילו אזורים נתמכים?",
            "a": "אנו משרתים צוותים ב־50+ מדינות, עם לוקליזציה ב־9+ שפות דו״ח.",
        },
        {
            "q": "האם ניתן לשלב עם LIMS או EMR?",
            "a": "כן. אנו עובדים עם ייצואי מעבדה סטנדרטיים ודפוסי אינטגרציה. פנו למכירות להתאמה לסביבה שלכם.",
        },
        {
            "q": "מהי רמת הדיוק שאתם מציגים?",
            "a": "בהערכת הפלטפורמה הפנימית: 98.7% דיוק סיווג ביומרקרים על קלטים מובנים—לא דיוק אבחון קליני.",
        },
        {
            "q": "איך מתחילים פיילוט?",
            "a": "קבעו הדגמה דרך טופס ארגוני. נגדיר יחד נפח, שפות וממשל.",
        },
    ],
    "hi": [
        {
            "q": "क्या Norya चिकित्सा उपकरण या निदान उपकरण है?",
            "a": "नहीं। Norya सहायक सॉफ़्टवेयर है जो लैब डेटा को संरचित, बहुभाषी रोगी स्पष्टीकरण में बदलता है—क्लिनिशियन समीक्षा के लिए।",
        },
        {
            "q": "डेटा सुरक्षा कैसे?",
            "a": "हम ट्रांजिट में एन्क्रिप्शन और स्तरीय हैंडलिंग नीति लागू करते हैं। एंटरप्राइज़ नियंत्रण (SSO, DPA, जहाँ लागू BAA) क्लिनिकल टीमों के लिए उपलब्ध हैं।",
        },
        {
            "q": "किन क्षेत्रों में सहायता?",
            "a": "हम 50+ देशों की टीमों को सेवा देते हैं; 9+ रिपोर्ट भाषाओं में लोकलाइज़ेशन।",
        },
        {
            "q": "क्या LIMS या EMR से इंटिग्रेशन?",
            "a": "हाँ। हम मानक लैब निर्यात और एंटरप्राइज़ इंटिग्रेशन पैटर्न के साथ काम करते हैं। अपने स्टैक के लिए सेल्स से संपर्क करें।",
        },
        {
            "q": "कौन सी सटीकता बताते हैं?",
            "a": "हमारे आंतरिक मूल्यांकन में संरचित लैब इनपुट पर 98.7% बायोमार्कर वर्गीकरण सटीकता—क्लिनिकल निदान सटीकता नहीं।",
        },
        {
            "q": "पायलट कैसे शुरू करें?",
            "a": "कॉर्पोरेट फॉर्म से डेमो बुक करें। हम आपकी टीम के साथ वॉल्यूम, भाषाएँ और गवर्नेंस तय करते हैं।",
        },
    ],
    "ar": [
        {
            "q": "هل نوريا جهاز طبي أو أداة تشخيص؟",
            "a": "لا. نوريا برنامج مساعد يحوّل بيانات المختبر إلى شروحات مريض منظمة ومتعددة اللغات لمراجعة الطاقم السريري.",
        },
        {
            "q": "كيف تُدار حماية البيانات؟",
            "a": "نطبّق التشفير أثناء النقل وسياسات معالجة بيانات متدرجة. تتوفر ضوابط مؤسسات (SSO وDPA وBAA حيث ينطبق) للفرق السريرية.",
        },
        {
            "q": "ما المناطق المدعومة؟",
            "a": "ندعم فرقًا في أكثر من 50 دولة، مع توطين بأكثر من 9 لغات تقرير.",
        },
        {
            "q": "هل يمكن التكامل مع LIMS أو EMR؟",
            "a": "نعم. نعمل مع صيغ تصدير معيارية وأنماط تكامل مؤسسية. تواصل مع المبيعات لملاءمة بيئتكم.",
        },
        {
            "q": "ما الدقة التي تعلنونها؟",
            "a": "تقييمنا الداخلي يبلغ عن 98٫7٪ دقة تصنيف للمؤشرات الحيوية على مدخلات منظّمة—وليس دقة تشخيص سريري.",
        },
        {
            "q": "كيف نبدأ تجربة؟",
            "a": "احجزوا عرضًا عبر نموذج المؤسسات. نحدد مع فريقكم الحجم واللغات والحوكمة.",
        },
    ],
}


def faq_for(lang: str) -> list[dict[str, Any]]:
    return [dict(x) for x in _FAQ.get(lang, _FAQ["de"])]
