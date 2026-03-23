# -*- coding: utf-8 -*-
"""Yasal sayfalar için çok dilli içerik. Müşteri diline göre sayfa sunulur."""

# Desteklenen diller: sitedeki dil seçenekleri. Bilinmeyen dil için "en" kullanılır.
from app.core.config import settings

LEGAL_LANGS = frozenset({"tr", "en", "de", "fr", "es", "it", "he", "ar", "hi", "el", "cs", "sr"})
# Tam hukuki gövde sağlanan diller (legal_bodies + tr/en temel metin)
LEGAL_CONTENT_LANGS = frozenset({"tr", "en", "de", "fr", "es", "it", "he", "hi", "ar"})
# hreflang / alternate link sırası (pricing ile uyumlu)
LEGAL_HREFLANG_LANGS = ("tr", "en", "de", "fr", "it", "es", "he", "hi", "ar")
DEFAULT_LEGAL_LANG = "tr"
FALLBACK_CONTENT_LANG = "en"  # LEGAL_CONTENT_LANGS dışı dil kodunda içerik dili

# UI: başlık, geri linki, footer nav etiketleri, footer metinleri
UI = {
    "tr": {
        "back_to_home": "← Ana sayfa",
        "nav_mesafeli": "Mesafeli Satış Sözleşmesi",
        "nav_privacy": "Gizlilik Politikası",
        "nav_refund": "İade ve İptal Politikası",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Kullanım Şartları",
        "nav_contact": "İletişim",
        "footer_desc": "Kan tahlili sonuçlarını anlaşılır dilde açıklayan araç.",
        "footer_disclaimer": "Bu araç eğitim amaçlıdır. Tıbbi kararlar için mutlaka bir sağlık uzmanına danışın.",
        "nav_legal": "Yasal",
        "footer_company_info_title": "İletişim ve şirket bilgileri",
        "footer_tax_office_label": "Vergi dairesi",
        "footer_tax_no_label": "Vergi no",
    },
    "en": {
        "back_to_home": "← Home",
        "nav_mesafeli": "Distance Selling Agreement",
        "nav_privacy": "Privacy Policy",
        "nav_refund": "Refund and Cancellation Policy",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Terms of Use",
        "nav_contact": "Contact",
        "footer_desc": "Tool that explains blood test results in plain language.",
        "footer_disclaimer": "This tool is for educational purposes. Always consult a healthcare professional for medical decisions.",
        "nav_legal": "Legal",
        "footer_company_info_title": "Contact & company information",
        "footer_tax_office_label": "Tax office",
        "footer_tax_no_label": "Tax number",
    },
    "de": {
        "back_to_home": "← Start",
        "nav_mesafeli": "Fernabsatzvereinbarung",
        "nav_privacy": "Datenschutz",
        "nav_refund": "Rückgabe und Stornierung",
        "nav_kvkk": "Datenschutz (DSGVO)",
        "nav_terms": "Nutzungsbedingungen",
        "nav_contact": "Kontakt",
        "footer_desc": "Laborergebnisse verständlich erklärt. Zur Orientierung — keine Diagnose.",
        "footer_disclaimer": "Nur zur Information. Medizinische Entscheidungen bitte mit dem Arzt besprechen.",
        "nav_legal": "Rechtliches",
        "footer_company_info_title": "Kontakt & Unternehmensangaben",
        "footer_tax_office_label": "Finanzamt",
        "footer_tax_no_label": "Steuernummer",
    },
    "fr": {
        "back_to_home": "← Accueil",
        "nav_mesafeli": "Contrat de vente à distance",
        "nav_privacy": "Politique de confidentialité",
        "nav_refund": "Remboursement et annulation",
        "nav_kvkk": "RGPD / Données personnelles",
        "nav_terms": "Conditions d'utilisation",
        "nav_contact": "Contact",
        "footer_desc": "Résultats d'analyses expliqués en langage clair. À titre informatif uniquement — pas un diagnostic.",
        "footer_disclaimer": "Contenu à but informatif. Pour toute décision médicale, consultez un professionnel de santé.",
        "nav_legal": "Mentions légales",
        "footer_company_info_title": "Coordonnées et informations société",
        "footer_tax_office_label": "Service des impôts",
        "footer_tax_no_label": "Numéro fiscal",
    },
    "es": {
        "back_to_home": "← Inicio",
        "nav_mesafeli": "Contrato de venta a distancia",
        "nav_privacy": "Política de privacidad",
        "nav_refund": "Reembolso y cancelación",
        "nav_kvkk": "RGPD / Protección de datos",
        "nav_terms": "Términos de uso",
        "nav_contact": "Contacto",
        "footer_desc": "Resultados de análisis explicados en lenguaje claro. Solo información — no sustituye el diagnóstico médico.",
        "footer_disclaimer": "Contenido informativo. Para decisiones médicas, consulte siempre a un profesional de la salud.",
        "nav_legal": "Legal",
        "footer_company_info_title": "Contacto e información de la empresa",
        "footer_tax_office_label": "Oficina tributaria",
        "footer_tax_no_label": "Número fiscal",
    },
    "it": {
        "back_to_home": "← Home",
        "nav_mesafeli": "Contratto di vendita a distanza",
        "nav_privacy": "Informativa sulla privacy",
        "nav_refund": "Rimborso e cancellazione",
        "nav_kvkk": "GDPR / Privacy",
        "nav_terms": "Termini di utilizzo",
        "nav_contact": "Contatti",
        "footer_desc": "Referti di laboratorio in linguaggio chiaro. Solo informativi — non sostituiscono il parere medico.",
        "footer_disclaimer": "Contenuto a scopo informativo. Per decisioni mediche consultare sempre un medico.",
        "nav_legal": "Note legali",
        "footer_company_info_title": "Contatti e dati aziendali",
        "footer_tax_office_label": "Ufficio imposte",
        "footer_tax_no_label": "Partita IVA / codice fiscale",
    },
    "he": {
        "back_to_home": "← דף הבית",
        "nav_mesafeli": "הסכם מכירה מרחוק",
        "nav_privacy": "מדיניות פרטיות",
        "nav_refund": "החזרה וביטול",
        "nav_kvkk": "GDPR / הגנת מידע",
        "nav_terms": "תנאי שימוש",
        "nav_contact": "צור קשר",
        "footer_desc": "תוצאות בדיקות דם מוסברות בשפה ברורה. למטרות מידע בלבד — לא תחליף לאבחון.",
        "footer_disclaimer": "תוכן אינפורמטיבי. להחלטות רפואיות יש להתייעץ עם רופא.",
        "nav_legal": "מסמכים משפטיים",
        "footer_company_info_title": "פרטי קשר וחברה",
        "footer_tax_office_label": "רשות המס",
        "footer_tax_no_label": "מספר עוסק / מס",
    },
    "ar": {
        "back_to_home": "← الرئيسية",
        "nav_mesafeli": "اتفاقية البيع عن بُعد",
        "nav_privacy": "سياسة الخصوصية",
        "nav_refund": "الاسترداد والإلغاء",
        "nav_kvkk": "GDPR / حماية البيانات",
        "nav_terms": "شروط الاستخدام",
        "nav_contact": "اتصل بنا",
        "footer_desc": "نتائج التحاليل مفسرة بلغة واضحة. للمعلومات فقط — لا تغني عن التشخيص الطبي.",
        "footer_disclaimer": "محتوى إعلامي. للقرارات الطبية استشر دائماً مختصاً.",
        "nav_legal": "الوثائق القانونية",
        "footer_company_info_title": "بيانات التواصل والشركة",
        "footer_tax_office_label": "مأمورية الضرائب",
        "footer_tax_no_label": "الرقم الضريبي",
    },
    "hi": {
        "back_to_home": "← होम",
        "nav_mesafeli": "दूरबिक्री समझौता",
        "nav_privacy": "गोपनीयता नीति",
        "nav_refund": "रिफंड और रद्दीकरण",
        "nav_kvkk": "GDPR / डेटा संरक्षण",
        "nav_terms": "उपयोग की शर्तें",
        "nav_contact": "संपर्क",
        "footer_desc": "लैब परिणाम सरल भाषा में समझाए गए। सिर्फ जानकारी—निदान का विकल्प नहीं।",
        "footer_disclaimer": "जानकारी के लिए। चिकित्सा निर्णय के लिए डॉक्टर से सलाह लें।",
        "nav_legal": "कानूनी जानकारी",
        "footer_company_info_title": "संपर्क व कंपनी विवरण",
        "footer_tax_office_label": "कर कार्यालय",
        "footer_tax_no_label": "कर संख्या",
    },
    "el": {
        "back_to_home": "← Αρχική",
        "nav_mesafeli": "Σύμβαση τηλεπώλησης",
        "nav_privacy": "Πολιτική απορρήτου",
        "nav_refund": "Επιστροφή και ακύρωση",
        "nav_kvkk": "GDPR / Προστασία δεδομένων",
        "nav_terms": "Όροι χρήσης",
        "nav_contact": "Επικοινωνία",
        "footer_desc": "Αποτελέσματα αναλύσεων σε απλή γλώσσα. Μόνο ενημέρωση—όχι διάγνωση.",
        "footer_disclaimer": "Ενημερωτικό περιεχόμενο. Για ιατρικές αποφάσεις συμβουλευτείτε γιατρό.",
        "nav_legal": "Legal",
        "footer_company_info_title": "Contact & company information",
        "footer_tax_office_label": "Tax office",
        "footer_tax_no_label": "Tax number",
    },
    "cs": {
        "back_to_home": "← Domů",
        "nav_mesafeli": "Smlouva o dálkovém prodeji",
        "nav_privacy": "Zásady ochrany osobních údajů",
        "nav_refund": "Vrácení a zrušení",
        "nav_kvkk": "GDPR / Ochrana údajů",
        "nav_terms": "Podmínky použití",
        "nav_contact": "Kontakt",
        "footer_desc": "Výsledky rozborů vysvětlené srozumitelně. Pouze informace—nenahrazuje diagnózu.",
        "footer_disclaimer": "Informační obsah. Pro lékařská rozhodnutí se poraďte s lékařem.",
        "nav_legal": "Legal",
        "footer_company_info_title": "Contact & company information",
        "footer_tax_office_label": "Tax office",
        "footer_tax_no_label": "Tax number",
    },
    "sr": {
        "back_to_home": "← Почетна",
        "nav_mesafeli": "Уговор о даљинској продаји",
        "nav_privacy": "Политика приватности",
        "nav_refund": "Реституција и отказивање",
        "nav_kvkk": "GDPR / Заштита података",
        "nav_terms": "Услови коришћења",
        "nav_contact": "Контакт",
        "footer_desc": "Резултати анализе објашњени јасно. Само информација—не замењује дијагнозу.",
        "footer_disclaimer": "Информативни садржај. За медицинске одлуке консултујте лекара.",
        "nav_legal": "Legal",
        "footer_company_info_title": "Contact & company information",
        "footer_tax_office_label": "Tax office",
        "footer_tax_no_label": "Tax number",
    },
}


def _ui(lang: str) -> dict:
    if lang in UI:
        return UI[lang]
    if lang in ("tr", "en"):
        return UI[lang]
    return UI["en"]


def _nav_links(lang: str) -> list[dict]:
    u = _ui(lang)
    return [
        {"url": "/legal/mesafeli-satis-sozlesmesi", "label": u["nav_mesafeli"]},
        {"url": "/legal/gizlilik-politikasi", "label": u["nav_privacy"]},
        {"url": "/iade-iptal", "label": u["nav_refund"]},
        {"url": "/legal/kvkk-gdpr", "label": u["nav_kvkk"]},
        {"url": "/legal/kullanim-sartlari", "label": u["nav_terms"]},
        {"url": "/legal/iletisim", "label": u["nav_contact"]},
    ]


# --- Gizlilik Politikası ---
# DRAFT: Taslak hukuki içerik — nihai şirket bilgileri ve hukuk danışmanı onayı sonrası güncellenecektir.
PRIVACY = {
    "tr": {
        "title": "Gizlilik Politikası",
        "meta_description": "NoryaAI gizlilik politikası: hangi kişisel veriler işlenir, kullanım amaçları, veri paylaşımı, güvenlik yaklaşımı, KVKK/GDPR kapsamındaki haklarınız ve iletişim bilgileri.",
        "last_updated": "Son güncelleme: Mart 2026",
                        "intro": "<p>Bu Gizlilik Politikas\u0131, NoryaAI platformunu kullanan ziyaret\u00e7i ve kullan\u0131c\u0131lar\u0131n ki\u015fisel verilerinin hangi kapsamda i\u015flendi\u011fini, korundu\u011funu ve hangi ama\u00e7larla kullan\u0131ld\u0131\u011f\u0131n\u0131 a\u00e7\u0131klamak amac\u0131yla haz\u0131rlanm\u0131\u015ft\u0131r.</p><p>NoryaAI, kullan\u0131c\u0131lar\u0131n y\u00fckledi\u011fi laboratuvar ve tahlil sonu\u00e7lar\u0131n\u0131 daha anla\u015f\u0131l\u0131r ve yap\u0131land\u0131r\u0131lm\u0131\u015f \u015fekilde sunmay\u0131 ama\u00e7layan dijital bir sa\u011fl\u0131k teknolojisi platformudur. Platform \u00fczerinden sunulan i\u00e7erikler yaln\u0131zca bilgilendirme ve kullan\u0131c\u0131 deneyimini destekleme amac\u0131 ta\u015f\u0131r; t\u0131bbi te\u015fhis, tedavi veya doktor de\u011ferlendirmesinin yerine ge\u00e7mez.</p>",
        "sections": [
            {"title": "1. Veri Sorumlusu / \u0130\u015fletmeci Bilgileri", "body": "<p><strong>Ticari Unvan:</strong> NoryaAI</p><p><strong>E-posta:</strong> <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a></p><p><strong>Adres:</strong> 31 A\u011fustos Mahallesi, Tomurcuk Aysa\u015f M\u00fchendislik No:2 \u0130\u00e7 Kap\u0131 No:4, Banaz/U\u015fak, T\u00fcrkiye</p><p><strong>Telefon:</strong> <a href=\"tel:+905071703564\" class=\"text-norya-brand hover:underline\">+90 507 170 35 64</a></p>"},
            {"title": "2. Hangi Verileri \u0130\u015fleyebiliriz", "body": "<p>A\u015fa\u011f\u0131daki veri t\u00fcrleri i\u015flenebilir:</p><ul><li>Ad soyad, e-posta adresi, kurum bilgisi gibi ileti\u015fim verileri</li><li>Hesap, oturum ve kullan\u0131m bilgileri</li><li>Y\u00fcklenen tahlil, laboratuvar sonucu ve ilgili kullan\u0131c\u0131 girdileri</li><li>\u00d6deme, sipari\u015f ve abonelik bilgileri</li><li>IP adresi, cihaz bilgisi, taray\u0131c\u0131 bilgisi ve teknik log verileri</li></ul>"},
            {"title": "3. Verileri Hangi Ama\u00e7larla Kullan\u0131r\u0131z", "body": "<ul><li>Hizmetin sunulmas\u0131 ve \u00e7al\u0131\u015ft\u0131r\u0131lmas\u0131</li><li>Y\u00fcklenen sonu\u00e7lar\u0131n analiz edilmesi ve raporlanmas\u0131</li><li>Kullan\u0131c\u0131 deneyiminin geli\u015ftirilmesi</li><li>Teknik destek sa\u011flanmas\u0131</li><li>Hesap ve abonelik s\u00fcre\u00e7lerinin y\u00f6netilmesi</li><li>G\u00fcvenlik, loglama ve hata tespiti</li><li>Yasal y\u00fck\u00fcml\u00fcl\u00fcklerin yerine getirilmesi</li></ul>"},
            {"title": "4. Sa\u011fl\u0131k Verileri ve Hassas Veriler Hakk\u0131nda", "body": "<p>NoryaAI \u00fczerinden y\u00fcklenen baz\u0131 i\u00e7erikler sa\u011fl\u0131k verisi niteli\u011fi ta\u015f\u0131yabilir. Bu t\u00fcr veriler, yaln\u0131zca kullan\u0131c\u0131n\u0131n a\u00e7\u0131k iradesiyle platforma y\u00fcklenmesi veya girilmesi halinde i\u015flenir.</p><p>Platform \u00e7\u0131kt\u0131lar\u0131 doktor de\u011ferlendirmesi yerine ge\u00e7mez. Kullan\u0131c\u0131, sa\u011fl\u0131kla ilgili kararlar\u0131n\u0131 yaln\u0131zca platform \u00e7\u0131kt\u0131s\u0131na dayanarak vermemeli ve gerekti\u011finde yetkili sa\u011fl\u0131k profesyoneline ba\u015fvurmal\u0131d\u0131r.</p>"},
            {"title": "5. Verilerin Payla\u015f\u0131lmas\u0131", "body": "<p>Veriler, gerekli oldu\u011fu \u00f6l\u00e7\u00fcde a\u015fa\u011f\u0131daki taraflarla payla\u015f\u0131labilir:</p><ul><li>Bar\u0131nd\u0131rma ve altyap\u0131 sa\u011flay\u0131c\u0131lar\u0131</li><li>Bulut hizmet sa\u011flay\u0131c\u0131lar\u0131</li><li>\u00d6deme hizmet sa\u011flay\u0131c\u0131lar\u0131</li><li>E-posta, ileti\u015fim ve analitik servisleri</li><li>Yasal zorunluluk halinde yetkili kurumlar</li></ul>"},
            {"title": "6. \u00c7erezler ve Teknik Veriler", "body": "<p>NoryaAI, hizmetin d\u00fczg\u00fcn \u00e7al\u0131\u015fmas\u0131, g\u00fcvenli\u011fin sa\u011flanmas\u0131, tercihlerin hat\u0131rlanmas\u0131 ve performans \u00f6l\u00e7\u00fcm\u00fc amac\u0131yla \u00e7erezler ve benzeri teknolojiler kullanabilir.</p>"},
            {"title": "7. Veri G\u00fcvenli\u011fi", "body": "<p>NoryaAI, i\u015flenen verilerin gizlili\u011fini ve b\u00fct\u00fcnl\u00fc\u011f\u00fcn\u00fc korumak amac\u0131yla makul teknik ve idari tedbirler uygulamay\u0131 hedefler. Bu kapsamda eri\u015fim kontrolleri, yetkilendirme, loglama, g\u00fcvenli ba\u011flant\u0131lar ve veri minimizasyonu yakla\u015f\u0131m\u0131 benimsenebilir.</p>"},
            {"title": "8. Veri Saklama S\u00fcresi", "body": "<p>Veriler, i\u015fleme amac\u0131n\u0131n gerektirdi\u011fi s\u00fcre boyunca veya ilgili mevzuat\u0131n \u00f6ng\u00f6rd\u00fc\u011f\u00fc yasal saklama s\u00fcreleri kadar muhafaza edilebilir. S\u00fcre sonunda veriler silinebilir, anonim hale getirilebilir veya mevzuata uygun \u015fekilde imha edilebilir.</p>"},
            {"title": "9. Kullan\u0131c\u0131n\u0131n Haklar\u0131", "body": "<p>Uygulanabilir mevzuat kapsam\u0131nda kullan\u0131c\u0131lar a\u015fa\u011f\u0131daki haklara sahip olabilir:</p><ul><li>Verilerinin i\u015flenip i\u015flenmedi\u011fini \u00f6\u011frenme</li><li>\u0130\u015flenmi\u015fse buna ili\u015fkin bilgi talep etme</li><li>Eksik veya yanl\u0131\u015f verilerin d\u00fczeltilmesini isteme</li><li>Belirli \u015fartlarda silme veya yok etme talep etme</li><li>\u0130\u015fleme faaliyetlerine itiraz etme</li></ul>"},
            {"title": "10. \u00dc\u00e7\u00fcnc\u00fc Taraf Ba\u011flant\u0131lar", "body": "<p>Platform \u00fczerinde \u00fc\u00e7\u00fcnc\u00fc taraf internet sitelerine veya hizmetlerine y\u00f6nlendiren ba\u011flant\u0131lar bulunabilir. Bu \u00fc\u00e7\u00fcnc\u00fc taraflar\u0131n gizlilik uygulamalar\u0131ndan NoryaAI sorumlu de\u011fildir.</p>"},
            {"title": "11. \u00c7ocuklar\u0131n Kullan\u0131m\u0131", "body": "<p>NoryaAI hizmetleri, do\u011frudan \u00e7ocuklara y\u00f6nelik olarak tasarlanmam\u0131\u015ft\u0131r. Uygulanabilir mevzuat uyar\u0131nca gerekli ya\u015f\u0131n alt\u0131ndaki bireylerin kullan\u0131m\u0131 i\u00e7in ebeveyn veya yasal temsilci onay\u0131 gerekebilir.</p>"},
            {"title": "12. Politika De\u011fi\u015fiklikleri", "body": "<p>Bu Gizlilik Politikas\u0131 zaman zaman g\u00fcncellenebilir. G\u00fcncel s\u00fcr\u00fcm, yay\u0131mland\u0131\u011f\u0131 tarih itibar\u0131yla ge\u00e7erli olur.</p><p><strong>Son g\u00fcncelleme tarihi:</strong> Mart 2026</p>"},
            {"title": "13. \u0130leti\u015fim", "body": "<p>Gizlilik politikas\u0131 veya ki\u015fisel verilerinizle ilgili talepleriniz i\u00e7in bizimle ileti\u015fime ge\u00e7ebilirsiniz.</p><p><strong>\u015eirket:</strong> NoryaAI</p><p><strong>E-posta:</strong> <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a></p><p><strong>Adres:</strong> 31 A\u011fustos Mahallesi, Tomurcuk Aysa\u015f M\u00fchendislik No:2 \u0130\u00e7 Kap\u0131 No:4, Banaz/U\u015fak, T\u00fcrkiye</p><p><strong>Telefon:</strong> <a href=\"tel:+905071703564\" class=\"text-norya-brand hover:underline\">+90 507 170 35 64</a></p>"},
        ],
        "footer_note": "NoryaAI \u2014 Dijital sa\u011fl\u0131k teknolojisi platformu. T\u0131bbi te\u015fhis veya tedavi yerine ge\u00e7mez.",
    },
    "en": {
        "title": "Privacy Policy",
        "meta_description": "Norya privacy policy: what we collect, how we use data, PayTR, your KVKK/GDPR rights and how to contact us.",
        "last_updated": "Last updated: March 2025",
        "intro": "At Norya (“we”, “us”), we respect your personal data. This Privacy Policy explains what data we collect when you use the Norya website and blood test analysis service, how we use it, who we may share it with, and your rights. We comply with Turkey's Law on Protection of Personal Data (KVKK), the EU General Data Protection Regulation (GDPR), and related legislation.",
        "sections": [
            {"title": "1. Data Controller", "body": "The data controller for the service and your personal data is Norya. Contact: <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a>. You can also send requests via our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page."},
            {"title": "2. Data We Collect", "body": "<strong>Identity and contact:</strong> Name, email, (optional) phone and country.<br><strong>Account:</strong> Your password is stored hashed; we do not store plain-text passwords.<br><strong>Test and report data:</strong> Lab result text you paste or upload, and the generated analysis report. This is processed to provide the service; reports may be stored in association with your account.<br><strong>Payment:</strong> Payments are processed via PayTR. Card numbers are not stored on Norya servers; only order ID, amount and payment status are recorded.<br><strong>Technical:</strong> IP address, session duration, error logs (for security and quality), browser type. Cookies are described below."},
            {"title": "3. Purposes of Use", "body": "Collected data is used to provide the service (account creation, login, report generation, payment confirmation, granting credits), security (preventing unauthorized access and abuse), legal obligations, password reset and email verification. Your data is not sold or shared for advertising targeting."},
            {"title": "4. Cookies and Similar Technologies", "body": "The site uses necessary cookies for session management and security. If we use optional tools such as Google Analytics (anonymous/measurement), this is disclosed on the site. You can restrict cookies in your browser settings; this may affect some features."},
            {"title": "5. Sharing of Data", "body": "Your data is shared only (i) with subcontractors necessary to provide the service (hosting, payment provider PayTR, email delivery), (ii) where required by law (court order, authority request), or (iii) with your explicit consent. Payments are processed by PayTR; PayTR's own privacy policy applies."},
            {"title": "6. Retention", "body": "Your data is retained while your account is active. On account deletion request, we delete or anonymise your data except where legal retention (e.g. tax, business records) applies. Only necessary information may be kept until legal periods expire."},
            {"title": "7. Security", "body": "Your data is transmitted over TLS/SSL. Passwords are hashed using secure methods; sensitive health-related data is processed only as necessary to provide the service, for the minimum period and scope required."},
            {"title": "8. Your Rights (KVKK / GDPR)", "body": "Under KVKK and GDPR you have rights of access, rectification, erasure, restriction of processing, data portability and objection. If you are in the EU you may lodge a complaint with a supervisory authority. Send requests via our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page or support@noryaai.com; we will respond within legal timeframes."},
            {"title": "9. Children", "body": "Our service is not directed at persons under 18. We do not knowingly collect personal data from under-18s. If we identify such data we will delete it."},
            {"title": "10. Policy Changes", "body": "When this policy is updated it will be published on the site; material changes may be announced by email or site notice. Continued use constitutes acceptance of the current policy."},
        ],
        "footer_note": "Norya — Service that explains blood test results in plain language. Not a substitute for medical diagnosis.",
    },
}

# --- Kullanım Şartları ---
# DRAFT: Taslak hukuki içerik — nihai şirket bilgileri ve hukuk danışmanı onayı sonrası güncellenecektir.
TERMS = {
    "tr": {
        "title": "Kullanım Şartları",
        "meta_description": "NoryaAI kullanım şartları: hizmet kapsamı, tıbbi sorumluluk reddi, kullanıcı sorumlulukları, fikri mülkiyet, ücretlendirme ve uygulanacak hukuk.",
        "last_updated": "Son güncelleme: Mart 2026",
                        "intro": "<p>Bu Kullan\u0131m \u015eartlar\u0131, NoryaAI platformuna eri\u015fen ve hizmetlerden yararlanan t\u00fcm kullan\u0131c\u0131lar i\u00e7in ge\u00e7erlidir. Platformu kullanarak a\u015fa\u011f\u0131daki \u015fartlar\u0131 okudu\u011funuzu, anlad\u0131\u011f\u0131n\u0131z\u0131 ve kabul etti\u011finizi beyan etmi\u015f olursunuz.</p><p>NoryaAI, laboratuvar ve kan tahlili sonu\u00e7lar\u0131n\u0131n daha anla\u015f\u0131l\u0131r, yap\u0131land\u0131r\u0131lm\u0131\u015f ve kullan\u0131c\u0131 dostu bi\u00e7imde sunulmas\u0131na yard\u0131mc\u0131 olan dijital bir platformdur.</p>",
        "sections": [
            {"title": "1. Hizmetin Kapsam\u0131", "body": "<p>NoryaAI hizmetleri \u00f6rnek olarak \u015funlar\u0131 i\u00e7erebilir:</p><ul><li>Laboratuvar sonu\u00e7lar\u0131n\u0131n y\u00fcklenmesi</li><li>Yapay zek\u00e2 destekli \u00f6n de\u011ferlendirme ve \u00f6n analiz deste\u011fi</li><li>\u00d6zet rapor ve a\u00e7\u0131klama \u00fcretimi</li><li>\u00c7ok dilli \u00e7\u0131kt\u0131 sunulmas\u0131</li><li>Kullan\u0131c\u0131ya daha anla\u015f\u0131l\u0131r sa\u011fl\u0131k ileti\u015fimi deste\u011fi</li></ul>"},
            {"title": "2. T\u0131bbi Sorumluluk Reddi", "body": "<p>NoryaAI taraf\u0131ndan sunulan t\u00fcm i\u00e7erikler yaln\u0131zca bilgilendirme ve destekleyici kullan\u0131m ama\u00e7l\u0131d\u0131r.</p><p>Platform; doktor muayenesi yerine ge\u00e7mez, t\u0131bbi te\u015fhis koymaz, tedavi \u00f6nerisi yerine ge\u00e7mez ve kritik klinik kararlar\u0131n tek dayana\u011f\u0131 olamaz.</p><p>Kullan\u0131c\u0131, sa\u011fl\u0131kla ilgili t\u00fcm \u00f6nemli kararlar\u0131n\u0131 yetkili sa\u011fl\u0131k profesyonelleriyle birlikte de\u011ferlendirmelidir.</p>"},
            {"title": "3. Kullan\u0131c\u0131n\u0131n Sorumluluklar\u0131", "body": "<ul><li>Do\u011fru ve hukuka uygun bilgi y\u00fcklemek</li><li>Hesap g\u00fcvenli\u011fini korumak</li><li>Mevzuata uygun hareket etmek</li><li>\u00dc\u00e7\u00fcnc\u00fc ki\u015filere ait verileri yetkisiz \u015fekilde y\u00fcklememek</li><li>Hizmeti k\u00f6t\u00fcye kullanmamak</li></ul>"},
            {"title": "4. Hesap ve Eri\u015fim", "body": "<p>Baz\u0131 hizmetlere eri\u015fim i\u00e7in kullan\u0131c\u0131 hesab\u0131 olu\u015fturulmas\u0131 gerekebilir. Kullan\u0131c\u0131, hesap bilgilerini do\u011fru ve g\u00fcncel tutmakla y\u00fck\u00fcml\u00fcd\u00fcr.</p><p>NoryaAI; g\u00fcvenlik, k\u00f6t\u00fcye kullan\u0131m, yasal zorunluluk veya s\u00f6zle\u015fmeye ayk\u0131r\u0131l\u0131k gibi durumlarda hesab\u0131 ask\u0131ya alma veya sonland\u0131rma hakk\u0131n\u0131 sakl\u0131 tutar.</p>"},
            {"title": "5. \u00dccretlendirme ve \u00d6deme", "body": "<p>Platform \u00fczerindeki baz\u0131 hizmetler \u00fccretli olabilir. \u00dccretlendirme abonelik, tek seferlik sat\u0131n alma veya farkl\u0131 ticari modeller \u00fczerinden sunulabilir.</p><p>\u00d6deme s\u00fcre\u00e7leri \u00fc\u00e7\u00fcnc\u00fc taraf \u00f6deme sa\u011flay\u0131c\u0131lar\u0131 \u00fczerinden y\u00fcr\u00fct\u00fclebilir.</p>"},
            {"title": "6. Kabul Edilemez Kullan\u0131m", "body": "<ul><li>Hizmeti yasa d\u0131\u015f\u0131 ama\u00e7larla kullanmak</li><li>Sistemlere yetkisiz eri\u015fim sa\u011flamaya \u00e7al\u0131\u015fmak</li><li>Platformun \u00e7al\u0131\u015fmas\u0131n\u0131 bozmak</li><li>Zararl\u0131 yaz\u0131l\u0131m veya k\u00f6t\u00fc niyetli i\u00e7erik y\u00fcklemek</li><li>Ba\u015fkalar\u0131n\u0131n verilerini izinsiz i\u015flemek veya payla\u015fmak</li><li>Platform \u00e7\u0131kt\u0131s\u0131n\u0131 yan\u0131lt\u0131c\u0131 veya zararl\u0131 \u015fekilde kullanmak</li></ul>"},
            {"title": "7. Fikri M\u00fclkiyet", "body": "<p>NoryaAI platformuna ait tasar\u0131m, yaz\u0131l\u0131m, marka, logo, metin, aray\u00fcz, rapor yap\u0131s\u0131 ve di\u011fer t\u00fcm i\u00e7eriklerin fikri m\u00fclkiyet haklar\u0131, aksi belirtilmedik\u00e7e NoryaAI veya ilgili hak sahiplerine aittir.</p>"},
            {"title": "8. Hizmetin S\u00fcreklili\u011fi", "body": "<p>NoryaAI, hizmeti s\u00fcrekli ve kesintisiz sunmak i\u00e7in makul \u00e7aba g\u00f6stermeyi hedefler. Ancak bak\u0131m, teknik hata, altyap\u0131 sorunu, g\u00fcvenlik gereksinimi veya \u00fc\u00e7\u00fcnc\u00fc taraf servis kesintileri nedeniyle hizmette zaman zaman aksama ya\u015fanabilir.</p>"},
            {"title": "9. Sorumlulu\u011fun S\u0131n\u0131rland\u0131r\u0131lmas\u0131", "body": "<p>Mevzuat\u0131n izin verdi\u011fi \u00f6l\u00e7\u00fcde, NoryaAI; platform kullan\u0131m\u0131ndan do\u011fan dolayl\u0131 zararlar, veri kayb\u0131, ticari kay\u0131p, karar verme hatalar\u0131 veya \u00fc\u00e7\u00fcnc\u00fc taraf hizmetlerinden kaynakl\u0131 aksakl\u0131klar bak\u0131m\u0131ndan s\u0131n\u0131rl\u0131 sorumluluk esas\u0131na tabi olabilir.</p><p>Kullan\u0131c\u0131, platform \u00e7\u0131kt\u0131lar\u0131n\u0131n profesyonel t\u0131bbi de\u011ferlendirme yerine kullan\u0131lmamas\u0131 gerekti\u011fini kabul eder.</p>"},
            {"title": "10. \u00dc\u00e7\u00fcnc\u00fc Taraf Hizmetleri", "body": "<p>NoryaAI, baz\u0131 hizmetleri sunarken \u00fc\u00e7\u00fcnc\u00fc taraf altyap\u0131, \u00f6deme, analiz, ileti\u015fim veya bar\u0131nd\u0131rma ara\u00e7lar\u0131ndan yararlanabilir.</p>"},
            {"title": "11. De\u011fi\u015fiklikler", "body": "<p>NoryaAI, bu Kullan\u0131m \u015eartlar\u0131\u2019n\u0131 zaman zaman g\u00fcncelleyebilir. G\u00fcncellenmi\u015f s\u00fcr\u00fcm, yay\u0131mland\u0131\u011f\u0131 tarihten itibaren ge\u00e7erli say\u0131l\u0131r.</p><p><strong>Son g\u00fcncelleme tarihi:</strong> Mart 2026</p>"},
            {"title": "12. Uygulanacak Hukuk ve Yetki", "body": "<p>Bu \u015fartlar, aksi zorunlu olarak \u00f6ng\u00f6r\u00fclmedik\u00e7e T\u00fcrkiye Cumhuriyeti hukuku kapsam\u0131nda yorumlan\u0131r. Uyu\u015fmazl\u0131klarda U\u015fak Mahkemeleri ve \u0130cra Daireleri yetkili olabilir.</p>"},
            {"title": "13. \u0130leti\u015fim", "body": "<p><strong>\u015eirket:</strong> NoryaAI</p><p><strong>E-posta:</strong> <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a></p><p><strong>Adres:</strong> 31 A\u011fustos Mahallesi, Tomurcuk Aysa\u015f M\u00fchendislik No:2 \u0130\u00e7 Kap\u0131 No:4, Banaz/U\u015fak, T\u00fcrkiye</p><p><strong>Telefon:</strong> <a href=\"tel:+905071703564\" class=\"text-norya-brand hover:underline\">+90 507 170 35 64</a></p>"},
        ],
        "footer_note": "NoryaAI \u2014 Dijital sa\u011fl\u0131k teknolojisi platformu. T\u0131bbi te\u015fhis veya tedavi yerine ge\u00e7mez.",
    },
    "en": {
        "title": "Terms of Use",
        "meta_description": "Norya terms of use: service scope, account rules, prohibited use, liability and governing law.",
        "last_updated": "Last updated: March 2025",
        "intro": "By using the Norya service (“Site”, “Service”) you are deemed to accept the following terms. When terms are updated, the current text will be published on the site; material changes may be announced by email or site notice.",
        "sections": [
            {"title": "1. Scope of Service", "body": "Norya provides an informational tool that summarises your blood test and similar lab results in plain language. This tool is not medical diagnosis or treatment advice; it is for education and information only. You must consult a doctor or healthcare provider for health-related decisions."},
            {"title": "2. Account and Use", "body": "You are responsible for the accuracy of the information you provide when registering. You must not share your account or disclose your password. You may use the service only for lawful, personal use; bulk, commercial or automated requests (bots, scraping) are prohibited."},
            {"title": "3. Prohibited Use", "body": "You must not misuse the service, access others' data without permission, overload the system, probe for security vulnerabilities or use it for illegal purposes. We may suspend or terminate accounts in case of violation."},
            {"title": "4. Intellectual Property", "body": "Texts, design, logo and software on the site belong to Norya. Unauthorised copying, distribution or commercial use is prohibited. You retain rights in content you upload; you are deemed to grant us the licence necessary to generate reports."},
            {"title": "5. Limitation of Liability", "body": "The service is provided “as is”. Norya does not warrant the accuracy or completeness of reports, uninterrupted access or absence of indirect damage. Short interruptions may occur for force majeure, maintenance or security updates; we will inform you where reasonable."},
            {"title": "6. Termination", "body": "You may close your account at any time. Norya reserves the right to suspend or terminate accounts that breach these terms or are used abusively."},
            {"title": "7. Governing Law and Disputes", "body": "These terms are governed by the laws of the Republic of Turkey. Turkish courts and enforcement offices have jurisdiction. Your rights as a consumer to refer to consumer arbitration boards and consumer courts are reserved."},
            {"title": "8. Contact", "body": "For questions use our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page or support@noryaai.com."},
        ],
        "footer_note": "Norya — Service that explains blood test results in plain language.",
    },
}

# --- KVKK / GDPR ---
KVKK_GDPR = {
    "tr": {
        "title": "KVKK, GDPR ve HIPAA Aydınlatma Metni",
        "meta_description": "KVKK, GDPR ve sağlık verisi güvenliği hakkında kısa aydınlatma; veri kategorileri, hukuki sebepler ve başvuru yolları.",
        "last_updated": "Son güncelleme: Mart 2025",
        "intro": "Norya olarak kişisel ve sağlıkla ilgili verilerinizi Türkiye'de KVKK, AB'de GDPR ve ABD'de sağlık verisi güvenliği ilkeleri (HIPAA-aligned güvenlik yaklaşımı) çerçevesinde işliyoruz. Bu sayfa, her bir çerçeveye ilişkin kısa aydınlatmayı içerir.",
        "sections": [
            {"title": "1. Veri Sorumlusu", "body": "Hizmeti sunan ve verilerinizi işleyen taraf Norya'dır. İletişim: <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a>. Taleplerinizi <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> sayfasından iletebilirsiniz."},
            {"title": "2. KVKK (Türkiye)", "body": "6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında veri sorumlusu Norya'dır. İşlenen veriler: kimlik ve iletişim bilgileri (ad, e-posta, telefon, ülke), hesap bilgileri (şifre hash'i, giriş kayıtları), tahlil metinleri ve üretilen raporlar (hizmetin ifası için), ödeme işlem kayıtları (kart numarası saklanmaz; PayTR kullanılır). Hukuki sebepler: sözleşmenin ifası, hukuki yükümlülük, meşru menfaat ve açık rıza. Verilerinize erişim, düzeltme, silme, işlemenin kısıtlanması ve itiraz haklarınız vardır; taleplerinizi yazılı veya e-posta ile iletebilirsiniz. Kişisel Verileri Koruma Kuruluna şikaret hakkınız saklıdır."},
            {"title": "3. GDPR (Avrupa Birliği)", "body": "AB Genel Veri Koruma Tüzüğü (GDPR) kapsamında işleme faaliyetleri yukarıdaki veri kategorileri ve amaçlarla uyumludur. Yasal dayanak: sözleşme (madde 6/1/b), yasal zorunluluk (6/1/c), meşru menfaat (6/1/f) ve gerektiğinde açık rıza (6/1/a). Verileriniz AB dışına (ör. sunucu konumu) aktarılıyorsa uygun güvenceler (standart sözleşme hükümleri vb.) uygulanır. Erişim, düzeltme, silme, kısıtlama, taşınabilirlik ve itiraz haklarınız vardır; ayrıca AB üye devletindeki bir denetim otoritesine şikayette bulunabilirsiniz. Taleplerinizi <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> veya support@noryaai.com üzerinden iletebilirsiniz."},
            {"title": "4. HIPAA ve Sağlık Verisi Güvenliği (ABD)", "body": "Norya, ABD'de \"covered entity\" (sağlık kurumu) veya \"business associate\" olarak HIPAA kapsamında kayıtlı değildir. Hizmet, kullanıcıların kendi laboratuvar sonuçlarını yükleyip anlaşılır rapor alması için sunulur; teşhis veya tedavi hizmeti değildir. Buna rağmen sağlıkla ilgili verileri ciddiye alıyoruz: tahlil metinleri ve raporlar yalnızca hizmetin sunulması amacıyla işlenir, TLS/SSL ile şifrelenir, yetkisiz erişime karşı korunur ve üçüncü taraflarla reklam veya ticari amaçla paylaşılmaz. Verilerinizi minimum gerekli süre ve kapsamda tutuyoruz; hesap silme talebinde yasal saklama süreleri dışında silinir veya anonimleştirilir. ABD'deki kullanıcılar için bu uygulama, sağlık verisi güvenliği ve gizlilik beklentileriyle uyumlu bir yaklaşım sunar."},
            {"title": "5. Ortak İlkeler", "body": "Tüm bölgelerde: veri minimizasyonu (yalnızca gerekli veriler), şifreleme ve güvenli altyapı, erişim kısıtlaması, hesap silme ve talep üzerine veri düzeltme/silme. Detaylı bilgi için <a href=\"/legal/gizlilik-politikasi\" class=\"text-norya-brand hover:underline\">Gizlilik Politikası</a> sayfamızı inceleyebilirsiniz."},
        ],
        "footer_note": "Norya — Kan tahlili sonuçlarını anlaşılır dilde açıklayan hizmet.",
    },
    "en": {
        "title": "KVKK, GDPR and HIPAA Notice",
        "meta_description": "Short notice on KVKK (Turkey), GDPR (EU) and our approach to health-related data security (HIPAA-aligned, non-covered entity).",
        "last_updated": "Last updated: March 2025",
        "intro": "At Norya we process your personal and health-related data in line with Turkey's KVKK, the EU GDPR and US health data security principles (HIPAA-aligned approach). This page provides a short notice for each framework.",
        "sections": [
            {"title": "1. Data Controller", "body": "The controller for the service and your data is Norya. Contact: <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a>. You can send requests via our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page."},
            {"title": "2. KVKK (Turkey)", "body": "Under Law No. 6698 on Protection of Personal Data, the data controller is Norya. Data processed: identity and contact (name, email, phone, country), account data (password hash, login records), test texts and generated reports (for performance of the service), payment records (card numbers are not stored; PayTR is used). Legal bases: contract performance, legal obligation, legitimate interest and, where applicable, consent. You have rights of access, rectification, erasure, restriction and objection; you may send requests in writing or by email. You may complain to the Turkish Personal Data Protection Board."},
            {"title": "3. GDPR (European Union)", "body": "Processing under the EU General Data Protection Regulation (GDPR) is consistent with the data categories and purposes above. Legal bases: contract (Art. 6(1)(b)), legal obligation (6(1)(c)), legitimate interest (6(1)(f)) and consent where applicable (6(1)(a)). If your data is transferred outside the EU (e.g. server location), appropriate safeguards (e.g. standard contractual clauses) apply. You have rights of access, rectification, erasure, restriction, portability and objection, and may lodge a complaint with a supervisory authority in an EU member state. Send requests via our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page or support@noryaai.com."},
            {"title": "4. HIPAA and Health Data Security (USA)", "body": "Norya is not registered as a HIPAA “covered entity” or “business associate” in the US. The service is offered for users to upload their own lab results and receive plain-language reports; it is not a diagnosis or treatment service. We nevertheless take health-related data seriously: test texts and reports are processed only to provide the service, transmitted over TLS/SSL, protected against unauthorised access and not shared with third parties for advertising or commercial purposes. We retain your data for the minimum necessary period; on account deletion, data is deleted or anonymised except where legal retention applies. For US users this approach is consistent with health data security and privacy expectations."},
            {"title": "5. Common Principles", "body": "Across all regions: data minimisation (only necessary data), encryption and secure infrastructure, access controls, account deletion and data rectification/erasure on request. See our <a href=\"/legal/gizlilik-politikasi\" class=\"text-norya-brand hover:underline\">Privacy Policy</a> for details."},
        ],
        "footer_note": "Norya — Service that explains blood test results in plain language.",
    },
}

# --- Mesafeli Satış ---
MESAFELI = {
    "tr": {
        "title": "Mesafeli Satış Sözleşmesi",
        "meta_description": "Mesafeli satış sözleşmesi: dijital hizmet, PayTR ödeme, cayma ve iade koşulları, şikayet yolları.",
        "last_updated": "Son güncelleme: Mart 2025",
        "intro": "Bu sözleşme, 6502 sayılı Tüketicinin Korunması Hakkında Kanun ve Mesafeli Sözleşmeler Yönetmeliği hükümlerine uygun olarak Norya hizmeti üzerinden elektronik ortamda gerçekleştirilen satışlara ilişkindir.",
        "sections": [
            {"title": "1. Taraflar", "body": "<strong>Satıcı:</strong> Norya hizmetini sunan taraf (veri sorumlusu ile aynı). <strong>Alıcı:</strong> Sitede kayıt olup hizmeti (tek analiz veya aylık/yıllık abonelik paketi) satın alan gerçek veya tüzel kişi (tüketici)."},
            {"title": "2. Sözleşme Konusu", "body": "Konu, alıcının Norya sitesinde sipariş ettiği dijital hizmetin (kan tahlili analizi hakkı veya abonelik) mesafeli satış yöntemiyle sunulmasıdır. Tek analiz satın alındığında hesaba bir analiz hakkı eklenir; aylık veya yıllık Pro pakette ayda belirlenen analiz hakkı, seçilen süre boyunca kullanılabilir. Hizmet, ödeme onayı (PayTR bildirimi) sonrası anında veya paket süresi boyunca ifa edilir."},
            {"title": "3. Ödeme ve Fiyat", "body": "Ödemeler PayTR sanal pos altyapısı ile güvenli şekilde alınır. Kredi kartı bilgileri Norya sunucularında saklanmaz. Fiyatlar sipariş ekranında net olarak gösterilir; vergiler dahildir. İndirim kodu kullanıldığında son tutar ödeme ekranında görünür."},
            {"title": "4. Cayma Hakkı ve İade", "body": "Mesafeli sözleşmelerde tüketicinin 14 gün içinde herhangi bir gerekçe göstermeksizin cayma hakkı vardır. Ancak tüketicinin onayı ile anında ifa edilen dijital içerik (analiz hakkının kullanılması) 6502 sayılı Kanun ve Yönetmelik uyarınca cayma hakkı istisnasına tabi olabilir. <strong>Hiç analiz yapılmamış</strong> ve ödeme tarihinden itibaren 14 gün içinde cayma talebi iletilirse iade değerlendirmeye alınır. Cayma talebi <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> veya support@noryaai.com üzerinden sipariş numarası ile iletilmelidir. Detaylar <a href=\"/iade-iptal\" class=\"text-norya-brand hover:underline\">İade ve İptal Politikası</a> sayfasında yer alır."},
            {"title": "5. Şikâyet ve Uyuşmazlık", "body": "Türk hukuku uygulanır. Tüketici olarak Tüketici Hakem Heyetleri ve Tüketici Mahkemelerine başvuru haklarınız saklıdır. Satıcı iletişim bilgileri: <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> sayfası ve support@noryaai.com."},
        ],
        "footer_note": "Norya — Kan tahlili sonuçlarını anlaşılır dilde açıklayan hizmet.",
    },
    "en": {
        "title": "Distance Selling Agreement",
        "meta_description": "Distance selling agreement for Norya digital services under Turkish consumer law, PayTR and withdrawal.",
        "last_updated": "Last updated: March 2025",
        "intro": "This agreement relates to sales made electronically via the Norya service in accordance with Turkish consumer protection law and the Distance Contracts Regulation.",
        "sections": [
            {"title": "1. Parties", "body": "<strong>Seller:</strong> The party providing the Norya service (same as data controller). <strong>Buyer:</strong> The natural or legal person (consumer) who registers on the site and purchases the service (single analysis or monthly/yearly subscription package)."},
            {"title": "2. Subject of the Agreement", "body": "The subject is the supply of the digital service (blood test analysis right or subscription) ordered by the buyer on the Norya site by means of distance selling. A single purchase adds one analysis credit to the account; in a monthly or yearly Pro package, the monthly analysis allowance is available for the chosen period. The service is performed upon payment confirmation (PayTR notification) or over the package period."},
            {"title": "3. Payment and Price", "body": "Payments are taken securely via PayTR's payment infrastructure. Card details are not stored on Norya servers. Prices are shown clearly on the order screen; tax is included. If a discount code is used, the final amount is shown on the payment screen."},
            {"title": "4. Right of Withdrawal and Refund", "body": "In distance contracts the consumer has a 14-day right of withdrawal without giving a reason. However, digital content performed immediately with the consumer's consent (use of the analysis right) may be exempt from the right of withdrawal under the Law and Regulation. If <strong>no analysis has been performed</strong> and a withdrawal request is sent within 14 days of the payment date, a refund will be considered. Send withdrawal requests with your order number via our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page or support@noryaai.com. Details are on our <a href=\"/iade-iptal\" class=\"text-norya-brand hover:underline\">Refund and Cancellation Policy</a> page."},
            {"title": "5. Complaints and Disputes", "body": "Turkish law applies. Your rights as a consumer to refer to consumer arbitration boards and consumer courts are reserved. Seller contact: <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page and support@noryaai.com."},
        ],
        "footer_note": "Norya — Service that explains blood test results in plain language.",
    },
}

# --- İade ve İptal (PayTR uyumlu: dijital hizmet, tek analiz, abonelik iptali, iade süreci, iletişim) ---
REFUND = {
    "tr": {
        "title": "İade ve İptal Politikası",
        "meta_description": "İade ve iptal politikası: dijital hizmet, PayTR, kullanılmamış analiz için 14 gün, abonelik ve iade süreci.",
        "last_updated": "Son güncelleme: Mart 2025",
        "intro": "Norya üzerinden satın alınan hizmetler dijital hizmet niteliğindedir. Ödemeler PayTR sanal pos altyapısı ile alınır; kart bilgileriniz Norya sunucularında tutulmaz.",
        "sections": [
            {"title": "a) Dijital hizmet niteliği", "body": "Norya, kan tahlili sonuçlarını anlaşılır dilde açıklayan bir dijital analiz hizmeti sunar. Satın alınan ürün (tek analiz hakkı veya aylık/yıllık abonelik paketi) 6502 sayılı Tüketicinin Korunması Hakkında Kanun ve Mesafeli Sözleşmeler Yönetmeliği kapsamında \"anında ifa edilen dijital içerik\" niteliğindedir. Kullanıcı ödeme öncesi bu niteliği kabul etmiş sayılır."},
            {"title": "b) Tek seferlik analiz (anında dijital hizmet) ve iade", "body": "Tek analiz satın alındığında hesabınıza bir analiz hakkı tanınır. Rapor üretildiği anda hizmet ifa edilmiş olur; bu nedenle rapor oluşturulduktan sonra cayma hakkı kullanılamaz. <strong>Hiç analiz yapılmamış</strong> ve ödeme tarihinden itibaren 14 gün içinde iletilen iade talepleri değerlendirmeye alınır. Teknik hata nedeniyle rapor oluşturulamadıysa veya ödeme alınmış ancak hesaba hak tanınmamışsa iade/manuel hak tanıma yapılır."},
            {"title": "c) Abonelik iptali", "body": "Aylık veya yıllık paketlerde otomatik yenileme yoktur; süre bitince paket kendiliğinden sona erer. İptal etmek isterseniz bir sonraki dönem için yeniden ödeme yapmamanız yeterlidir. Kullanıcı panelinden aboneliğinizi görüntüleyebilirsiniz. İptal sonrası mevcut paket süreniz dolana kadar analiz hakkınız kullanılabilir; süre bittiğinde erişim sona erer."},
            {"title": "d) Ücret iadesi süreci", "body": "Uygun bulunan iadeler, talebin onaylandığı tarihten itibaren <strong>en geç 14 iş günü</strong> içinde, ödeme yapılan yönteme (kredi kartı / banka kartı) iade edilir. İade, kartınıza veya aynı ödeme kanalına yansır; banka işlem süresi ek 1–5 iş günü sürebilir. Kısmen kullanılmış paketlerde oransal iade uygulanmaz. Kötüye kullanım tespit edilen durumlarda Norya iade talebini reddetme hakkını saklı tutar."},
            {"title": "e) İletişim", "body": "İade ve iptal taleplerinizi sipariş numaranız (merchant_oid) ile <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a> adresine, <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> sayfasından veya <a href=\"/iade-talebi\" class=\"text-norya-brand hover:underline\">İade talebi formu</a> üzerinden iletebilirsiniz. En geç 1 iş günü içinde dönüş yapıyoruz."},
        ],
        "footer_note": "Norya — Kan tahlili sonuçlarını anlaşılır dilde açıklayan hizmet.",
    },
    "en": {
        "title": "Refund and Cancellation Policy",
        "meta_description": "Refund and cancellation policy: digital service, PayTR, 14 days if unused, subscription end and processing times.",
        "last_updated": "Last updated: March 2025",
        "intro": "Services purchased via Norya are digital services. Payments are taken via PayTR's payment infrastructure; your card details are not stored on Norya servers.",
        "sections": [
            {"title": "a) Nature of the digital service", "body": "Norya provides a digital analysis service that explains blood test results in plain language. The product purchased (single analysis credit or monthly/yearly subscription package) qualifies as \"digital content supplied immediately\" under Turkish consumer law and the Distance Contracts Regulation. The user is deemed to have accepted this nature before payment."},
            {"title": "b) Single analysis (instant digital service) and refund", "body": "When you buy a single analysis, one analysis credit is added to your account. Once the report is generated, the service is deemed performed; therefore the right of withdrawal cannot be exercised after the report has been created. Refund requests received within 14 days of the payment date with <strong>no analysis having been performed</strong> will be considered. If the report could not be generated due to a technical error, or payment was received but the account was not credited, a refund or manual credit will be applied."},
            {"title": "c) Subscription cancellation", "body": "Monthly or yearly packages do not auto-renew; the package ends when the period ends. To cancel, simply do not pay for the next period. You can view your subscription in the user panel. After cancellation, your analysis credits remain available until the current package period ends; access then ceases."},
            {"title": "d) Refund process", "body": "Approved refunds are processed to the original payment method (credit/debit card) within <strong>14 business days</strong> of approval. The refund will appear on your card or the same payment channel; bank processing may take an additional 1–5 business days. Proportional refunds are not applied for partially used packages. Norya reserves the right to refuse refund requests where abuse is detected."},
            {"title": "e) Contact", "body": "Send refund and cancellation requests with your order number (merchant_oid) to <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a>, via our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page, or using the <a href=\"/iade-talebi\">refund request form</a>. We aim to respond within 1 business day."},
        ],
        "footer_note": "Norya — Service that explains blood test results in plain language.",
    },
}

# --- İletişim (Contact): yapı biraz farklı, kartlar ve SSS ---
CONTACT = {
    "tr": {
        "title": "Bize Ulaşın",
        "meta_description": "Sorularınız, teknik destek veya iade talepleriniz için Norya iletişim. Türkiye merkezli destek.",
        "hero_title": "Bize Ulaşın",
        "hero_sub": "İstediğiniz zaman sorunlarınızı çözelim. Sorularınız, teknik destek veya iade talepleriniz için buradayız.",
        "email_title": "E-posta ile yazın",
        "email_desc": "Sorularınız, iade talepleriniz veya \"ödeme alındı ama analiz hakkı gelmedi\" gibi teknik konular için bize ulaşabilirsiniz.",
        "email_note": "Mümkünse hesap e-posta adresinizi ve konuyla ilgili kısa açıklamayı (sipariş no, tarih vb.) yazın. En geç 1 iş günü içinde dönüş yapıyoruz.",
        "support_title": "Türkiye — Destek",
        "support_desc": "Norya, Türkiye'den hizmet veriyor. Tüm sorularınızı Türkçe veya İngilizce iletebilirsiniz.",
        "support_email": "E-posta:",
        "support_whatsapp": "WhatsApp:",
        "support_time": "Yanıt süresi:",
        "support_time_val": "En geç 1 iş günü",
        "support_topics": "Konular:",
        "support_topics_val": "Teknik destek, iade/iptal, ödeme sorunları, genel sorular",
        "closing": "Sorularınızı yanıtlamaktan mutluluk duyarız. Kan tahlili sonuçlarınızı anlaşılır dilde açıklayan Norya ekibi olarak yanınızdayız.",
        "faq_title": "Sık sorulan sorular",
        "faq1_q": "Ödeme yaptım ama analiz hakkı gelmedi.",
        "faq1_a": "Banka veya ödeme sağlayıcısı onayı bazen gecikebilir. E-posta ile sipariş veya ödeme bilginizi yazın; en geç 1 iş günü içinde kontrol edip düzeltiyoruz.",
        "faq2_q": "İade nasıl yapılır?",
        "faq2_a": "İade ve iptal koşulları <a href=\"/iade-iptal\" class=\"text-primary-600 hover:underline\">İade ve İptal Politikası</a> sayfamızda. Talebinizi support@noryaai.com veya norya.destek@gmail.com adresine iletebilirsiniz.",
        "label_authorized": "Yetkili Kişi",
        "label_trade_name": "Ticari Ünvan",
        "label_tax": "Vergi Bilgileri",
        "label_tax_office": "Vergi dairesi",
        "label_tax_number": "Vergi no",
        "label_phone_section": "Telefon / WhatsApp",
        "label_support_email": "Destek e-postası",
        "label_contact_email": "İletişim e-postası",
        "label_address": "Adres",
        "label_country": "Ülke",
        "wa_button": "WhatsApp ile yazın",
    },
    "en": {
        "title": "Contact Us",
        "meta_description": "Contact Norya for questions, technical support or refund requests. Turkey-based support.",
        "hero_title": "Contact Us",
        "hero_sub": "We're here to help. For questions, technical support or refund requests, we're just a message away.",
        "email_title": "Email us",
        "email_desc": "For questions, refund requests or technical issues such as \"payment received but analysis credit not granted\", you can reach us below.",
        "email_note": "Please include your account email and a short description (order number, date, etc.). We aim to reply within 1 business day.",
        "support_title": "Turkey — Support",
        "support_desc": "Norya operates from Turkey. You can contact us in Turkish or English.",
        "support_email": "Email:",
        "support_whatsapp": "WhatsApp:",
        "support_time": "Response time:",
        "support_time_val": "Within 1 business day",
        "support_topics": "Topics:",
        "support_topics_val": "Technical support, refunds/cancellation, payment issues, general enquiries",
        "closing": "We're happy to answer your questions. The Norya team is here to explain your blood test results in plain language.",
        "faq_title": "Frequently asked questions",
        "faq1_q": "I paid but didn't receive my analysis credit.",
        "faq1_a": "Bank or payment provider approval can sometimes be delayed. Email us with your order or payment details; we'll check and fix within 1 business day.",
        "faq2_q": "How do I request a refund?",
        "faq2_a": "Refund and cancellation conditions are on our <a href=\"/iade-iptal\" class=\"text-primary-600 hover:underline\">Refund and Cancellation Policy</a> page. You can send your request to support@noryaai.com or norya.destek@gmail.com.",
        "label_authorized": "Authorized person",
        "label_trade_name": "Trade name",
        "label_tax": "Tax information",
        "label_tax_office": "Tax office",
        "label_tax_number": "Tax number",
        "label_phone_section": "Phone / WhatsApp",
        "label_support_email": "Support email",
        "label_contact_email": "General contact email",
        "label_address": "Address",
        "label_country": "Country",
        "wa_button": "Message us on WhatsApp",
    },
}


def _inject_extended_legal_bodies() -> None:
    """de/fr/es/it/he/hi/ar tam hukuki gövdeleri legal_bodies paketinden yükler."""
    from app.legal_bodies import ar as ar_body
    from app.legal_bodies import de, es, fr, he, hi, it

    for code, pack in (
        ("de", de),
        ("fr", fr),
        ("es", es),
        ("it", it),
        ("he", he),
        ("hi", hi),
        ("ar", ar_body),
    ):
        PRIVACY[code] = pack.PRIVACY
        TERMS[code] = pack.TERMS
        KVKK_GDPR[code] = pack.KVKK_GDPR
        MESAFELI[code] = pack.MESAFELI
        REFUND[code] = pack.REFUND
        CONTACT[code] = pack.CONTACT


_inject_extended_legal_bodies()


def _content_lang(lang: str) -> str:
    """Tam hukuki gövde dilini seçer; desteklenmeyen kodlarda İngilizce."""
    code = (lang or "").strip().lower()[:2]
    if code in LEGAL_CONTENT_LANGS:
        return code
    return FALLBACK_CONTENT_LANG


def get_legal_ui(lang: str) -> dict:
    """Seçilen dil için UI metinleri ve nav linkleri."""
    use_lang = lang if lang in LEGAL_LANGS else "en"
    u = _ui(use_lang)
    uen = UI["en"]
    # Şirket bilgileri: ENV'den okunur, boşsa config varsayılanları veya — kullanılır
    _f = "—"
    company_title = (settings.company_title or settings.invoice_company_title or "").strip() or _f
    company_authorized_person = (settings.company_authorized_person or "").strip() or _f
    company_tax_office = (settings.company_tax_office or settings.invoice_company_tax_office or "").strip() or _f
    company_tax_number = (settings.company_tax_number or settings.gib_earsiv_user or "").strip() or _f
    company_address = (settings.company_address or settings.invoice_company_address or "").strip() or _f
    company_phone = (settings.company_phone or "").strip() or _f
    if company_phone != _f and not company_phone.startswith("+") and company_phone.replace(" ", "").replace("-", "").isdigit():
        company_phone = "+90 " + company_phone.lstrip("0")
    company_support_email = (settings.company_support_email or "").strip() or "support@noryaai.com"
    company_contact_email = (settings.company_contact_email or "").strip() or "info@noryaai.com"
    company_country = (settings.company_country or "").strip() or "Türkiye"
    # WhatsApp link için sadece rakamlar (örn. 905071703564)
    _phone_digits = "".join(c for c in (company_phone or "") if c.isdigit())
    company_phone_wa = _phone_digits if len(_phone_digits) >= 10 else "905071703564"
    return {
        "lang": use_lang,
        "back_to_home": u["back_to_home"],
        "nav_links": _nav_links(use_lang),
        "nav_legal": u.get("nav_legal", uen["nav_legal"]),
        "footer_company_info_title": u.get("footer_company_info_title", uen["footer_company_info_title"]),
        "footer_tax_office_label": u.get("footer_tax_office_label", uen["footer_tax_office_label"]),
        "footer_tax_no_label": u.get("footer_tax_no_label", uen["footer_tax_no_label"]),
        "footer_desc": u["footer_desc"],
        "footer_disclaimer": u["footer_disclaimer"],
        "company_title": company_title,
        "company_authorized_person": company_authorized_person,
        "company_tax_office": company_tax_office,
        "company_tax_number": company_tax_number,
        "company_address": company_address,
        "company_phone": company_phone,
        "company_support_email": company_support_email,
        "company_contact_email": company_contact_email,
        "company_country": company_country,
        "company_phone_wa": company_phone_wa,
    }


def get_legal_content(page: str, lang: str) -> dict | None:
    """Sayfa adı ve dil için içerik döner. Desteklenen sayfa yoksa None."""
    content_lang = _content_lang(lang)
    pages = {
        "gizlilik-politikasi": PRIVACY,
        "kullanim-sartlari": TERMS,
        "kvkk-gdpr": KVKK_GDPR,
        "mesafeli-satis-sozlesmesi": MESAFELI,
        "iade-iptal-politikasi": REFUND,
        "iletisim": CONTACT,
    }
    data = pages.get(page)
    if not data:
        return None
    return data.get(content_lang) or data.get(FALLBACK_CONTENT_LANG)
