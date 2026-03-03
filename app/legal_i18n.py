# -*- coding: utf-8 -*-
"""Yasal sayfalar için çok dilli içerik. Müşteri diline göre sayfa sunulur."""

# Desteklenen diller: sitedeki dil seçenekleri. Bilinmeyen dil için "en" kullanılır.
from app.core.config import settings

LEGAL_LANGS = frozenset({"tr", "en", "de", "fr", "es", "it", "he", "ar", "hi", "el", "cs", "sr"})
DEFAULT_LEGAL_LANG = "tr"
FALLBACK_CONTENT_LANG = "en"  # İçerik çevirisi yoksa (sadece TR/EN var) EN kullan

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
    },
    "de": {
        "back_to_home": "← Startseite",
        "nav_mesafeli": "Fernabsatzvereinbarung",
        "nav_privacy": "Datenschutz",
        "nav_refund": "Rückgabe und Stornierung",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Nutzungsbedingungen",
        "nav_contact": "Kontakt",
        "footer_desc": "Tool zur verständlichen Erklärung von Blutwerten.",
        "footer_disclaimer": "Dieses Tool dient der Information. Konsultieren Sie für medizinische Entscheidungen einen Arzt.",
    },
    "fr": {
        "back_to_home": "← Accueil",
        "nav_mesafeli": "Contrat de vente à distance",
        "nav_privacy": "Politique de confidentialité",
        "nav_refund": "Remboursement et annulation",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Conditions d'utilisation",
        "nav_contact": "Contact",
        "footer_desc": "Outil d'explication des résultats d'analyses sanguines.",
        "footer_disclaimer": "Cet outil est à but informatif. Consultez un professionnel de santé pour toute décision médicale.",
    },
    "es": {
        "back_to_home": "← Inicio",
        "nav_mesafeli": "Contrato de venta a distancia",
        "nav_privacy": "Política de privacidad",
        "nav_refund": "Reembolso y cancelación",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Términos de uso",
        "nav_contact": "Contacto",
        "footer_desc": "Herramienta que explica los resultados de análisis de sangre.",
        "footer_disclaimer": "Esta herramienta es informativa. Consulte a un profesional de la salud para decisiones médicas.",
    },
    "it": {
        "back_to_home": "← Home",
        "nav_mesafeli": "Contratto di vendita a distanza",
        "nav_privacy": "Informativa sulla privacy",
        "nav_refund": "Rimborso e cancellazione",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Termini di utilizzo",
        "nav_contact": "Contatti",
        "footer_desc": "Strumento che spiega i risultati delle analisi del sangue.",
        "footer_disclaimer": "Questo strumento è informativo. Consultare un medico per decisioni mediche.",
    },
    "he": {
        "back_to_home": "← דף הבית",
        "nav_mesafeli": "הסכם מכירה מרחוק",
        "nav_privacy": "מדיניות פרטיות",
        "nav_refund": "החזרה וביטול",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "תנאי שימוש",
        "nav_contact": "צור קשר",
        "footer_desc": "כלי להסבר תוצאות בדיקות דם.",
        "footer_disclaimer": "כלי זה למטרות מידע. התייעץ עם רופא להחלטות רפואיות.",
    },
    "ar": {
        "back_to_home": "← الرئيسية",
        "nav_mesafeli": "اتفاقية البيع عن بُعد",
        "nav_privacy": "سياسة الخصوصية",
        "nav_refund": "الاسترداد والإلغاء",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "شروط الاستخدام",
        "nav_contact": "اتصل بنا",
        "footer_desc": "أداة لشرح نتائج تحاليل الدم.",
        "footer_disclaimer": "هذه الأداة للمعلومات. استشر طبيباً للقرارات الطبية.",
    },
    "hi": {
        "back_to_home": "← होम",
        "nav_mesafeli": "दूरबिक्री समझौता",
        "nav_privacy": "गोपनीयता नीति",
        "nav_refund": "रिफंड और रद्दीकरण",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "उपयोग की शर्तें",
        "nav_contact": "संपर्क",
        "footer_desc": "रक्त परीक्षण परिणामों को समझाने वाला टूल।",
        "footer_disclaimer": "यह टूल शैक्षिक है। चिकित्सा निर्णय के लिए डॉक्टर से सलाह लें।",
    },
    "el": {
        "back_to_home": "← Αρχική",
        "nav_mesafeli": "Σύμβαση τηλεπώλησης",
        "nav_privacy": "Πολιτική απορρήτου",
        "nav_refund": "Επιστροφή και ακύρωση",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Όροι χρήσης",
        "nav_contact": "Επικοινωνία",
        "footer_desc": "Εργαλείο εξήγησης αποτελεσμάτων αίματος.",
        "footer_disclaimer": "Αυτό το εργαλείο είναι ενημερωτικό. Συμβουλευτείτε γιατρό για ιατρικές αποφάσεις.",
    },
    "cs": {
        "back_to_home": "← Domů",
        "nav_mesafeli": "Smlouva o dálkovém prodeji",
        "nav_privacy": "Zásady ochrany osobních údajů",
        "nav_refund": "Vrácení a zrušení",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Podmínky použití",
        "nav_contact": "Kontakt",
        "footer_desc": "Nástroj pro vysvětlení výsledků krevních testů.",
        "footer_disclaimer": "Tento nástroj je informační. Pro lékařská rozhodnutí se poraďte s lékařem.",
    },
    "sr": {
        "back_to_home": "← Почетна",
        "nav_mesafeli": "Уговор о даљинској продаји",
        "nav_privacy": "Политика приватности",
        "nav_refund": "Реституција и отказивање",
        "nav_kvkk": "KVKK / GDPR",
        "nav_terms": "Услови коришћења",
        "nav_contact": "Контакт",
        "footer_desc": "Алатка за објашњење резултата крви.",
        "footer_disclaimer": "Ова алатка је информативна. Консултујте лекара за медицинске одлуке.",
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
PRIVACY = {
    "tr": {
        "title": "Gizlilik Politikası",
        "last_updated": "Son güncelleme: Mart 2025",
        "intro": "Norya (“biz”, “bizim”) olarak kişisel verilerinize saygı duyuyoruz. Bu Gizlilik Politikası, Norya web sitesi ve kan tahlili analiz hizmetimizi kullanırken hangi verilerin toplandığını, nasıl kullanıldığını, kiminle paylaşılabileceğini ve haklarınızı açıklar. Türkiye'de 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK), Avrupa Birliği Genel Veri Koruma Tüzüğü (GDPR) ve ilgili mevzuata uygun hareket ediyoruz.",
        "sections": [
            {"title": "1. Veri Sorumlusu", "body": "Hizmeti sunan ve kişisel verilerinizi işleyen taraf Norya'dır. İletişim: <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a>. Taleplerinizi <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> sayfasından da iletebilirsiniz."},
            {"title": "2. Toplanan Veriler", "body": "<strong>Kimlik ve iletişim bilgileri:</strong> Ad soyad, e-posta adresi, (kayıt sırasında verdiğiniz) telefon numarası ve ülke bilgisi.<br><strong>Hesap bilgileri:</strong> Şifreniz şifrelenmiş (hash) olarak saklanır; düz metin şifre tutulmaz.<br><strong>Tahlil ve rapor verileri:</strong> Yapıştırdığınız veya yüklediğiniz laboratuvar sonuç metni, üretilen analiz raporu. Bu veriler hizmetin sunulması için işlenir; raporlar hesabınızla ilişkili olarak saklanabilir.<br><strong>Ödeme bilgileri:</strong> Ödemeler PayTR altyapısı ile alınır. Kredi kartı numarası vb. kart bilgileri Norya sunucularında tutulmaz; yalnızca sipariş kimliği, tutar ve ödeme durumu kaydedilir.<br><strong>Teknik veriler:</strong> IP adresi, oturum süresi, hata logları (güvenlik ve hizmet kalitesi için), tarayıcı türü. Çerezler aşağıda açıklanmaktadır."},
            {"title": "3. Verilerin Kullanım Amaçları", "body": "Toplanan veriler; hizmetin sunulması (hesap oluşturma, giriş, rapor üretimi, ödeme onayı ve hak tanıma), güvenlik (yetkisiz erişim ve kötüye kullanımın önlenmesi), yasal yükümlülüklerin yerine getirilmesi, şifre sıfırlama ve e-posta doğrulama gibi işlemler için kullanılır. Verileriniz üçüncü taraflara satılmaz veya reklam hedeflenmesi amacıyla paylaşılmaz."},
            {"title": "4. Çerezler ve Benzeri Teknolojiler", "body": "Site, oturum yönetimi ve güvenlik için gerekli çerezleri kullanır. İsteğe bağlı olarak Google Analytics (anonim/ölçüm) kullanılıyorsa, bu kullanım sitede belirtilir. Tarayıcı ayarlarınızdan çerezleri kısıtlayabilirsiniz; ancak bazı özelliklerin çalışmamasına neden olabilir."},
            {"title": "5. Verilerin Paylaşımı", "body": "Verileriniz yalnızca (i) hizmetin sunulması için gerekli alt yükleniciler (barındırma, ödeme sağlayıcısı PayTR, e-posta gönderimi), (ii) yasal zorunluluk (mahkeme kararı, yetkili kurum talebi) veya (iii) açık rızanız ile paylaşılır. Ödeme işlemleri PayTR üzerinden gerçekleşir; PayTR'nin kendi gizlilik politikası geçerlidir."},
            {"title": "6. Saklama Süresi", "body": "Hesabınız açık kaldığı sürece verileriniz saklanır. Hesap silme talebinizde, yasal saklama süreleri (ör. vergi, ticari kayıt) dışında verileriniz silinir veya anonimleştirilir. Yasal süreler dolana kadar sadece zorunlu bilgiler tutulabilir."},
            {"title": "7. Güvenlik", "body": "Verileriniz TLS/SSL ile şifrelenmiş bağlantılar üzerinden iletilir. Şifreler güvenli yöntemlerle hash'lenir; hassas sağlık verileri hizmetin sunulması için gerekli minimum süre ve kapsamda işlenir."},
            {"title": "8. Haklarınız (KVKK / GDPR)", "body": "KVKK ve GDPR kapsamında verilerinize erişim, düzeltme, silme, işlemenin kısıtlanması, veri taşınabilirliği ve itiraz haklarınız bulunmaktadır. AB'de ikamet ediyorsanız bir veri koruma denetim otoritesine şikayette bulunma hakkınız vardır. Taleplerinizi <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> veya support@noryaai.com üzerinden iletebilirsiniz; yasal süreler içinde yanıtlanacaktır."},
            {"title": "9. Çocuklar", "body": "Hizmetimiz 18 yaş altındaki kişilere yönelik değildir. Bilerek 18 yaş altı bireylerden kişisel veri toplamıyoruz. Böyle bir veri tespit edilirse silinir."},
            {"title": "10. Politika Değişiklikleri", "body": "Bu metin güncellendiğinde sitede yayımlanır; önemli değişiklikler e-posta veya site bildirimi ile duyurulabilir. Kullanıma devam etmeniz güncel politikayı kabul ettiğiniz anlamına gelir."},
        ],
        "footer_note": "Norya — Kan tahlili sonuçlarını anlaşılır dilde açıklayan hizmet. Tıbbi tanı yerine geçmez.",
    },
    "en": {
        "title": "Privacy Policy",
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
TERMS = {
    "tr": {
        "title": "Kullanım Şartları",
        "last_updated": "Son güncelleme: Mart 2025",
        "intro": "Norya hizmetini (“Site”, “Hizmet”) kullanarak aşağıdaki koşulları kabul etmiş sayılırsınız. Koşullarda değişiklik yapıldığında güncel metin sitede yayımlanır; önemli değişiklikler e-posta veya site bildirimi ile duyurulabilir.",
        "sections": [
            {"title": "1. Hizmetin Kapsamı", "body": "Norya, kan tahlili ve benzeri laboratuvar sonuçlarınızı anlaşılır bir dille özetleyen bilgilendirme aracı sunar. Bu araç tıbbi teşhis veya tedavi önerisi değildir; yalnızca eğitim ve bilgilendirme amaçlıdır. Sağlıkla ilgili kararlarınızı mutlaka bir hekim veya sağlık kuruluşu ile görüşerek almanız gerekir."},
            {"title": "2. Hesap ve Kullanım", "body": "Kayıt sırasında verdiğiniz bilgilerin doğru ve güncel olması sizin sorumluluğunuzdadır. Hesabınızı başkasıyla paylaşmamanız ve şifrenizi gizli tutmanız gerekir. Hizmeti yalnızca yasal ve kişisel kullanımınız için kullanabilirsiniz; toplu, ticari veya otomatik istekler (bot, scraping) yasaktır."},
            {"title": "3. Yasak Kullanım", "body": "Hizmeti kötüye kullanmak, başkalarının verilerini izinsiz girmek, sistemi aşırı yüklemek, güvenlik açıklarını denemek veya yasalara aykırı amaçlarla kullanmak yasaktır. İhlal tespit edildiğinde hesap askıya alınabilir veya sonlandırılır."},
            {"title": "4. Fikri Mülkiyet", "body": "Sitedeki metinler, tasarım, logo ve yazılım Norya'ya aittir. İzinsiz kopyalama, dağıtım veya ticari kullanım yasaktır. Kullanıcı tarafından yüklenen içeriklerin hakları size aittir; rapor üretimi için gerekli lisansı bize verdiğiniz kabul edilir."},
            {"title": "5. Sorumluluk Sınırı", "body": "Hizmet “olduğu gibi” sunulur. Norya, raporların doğruluğu veya eksiksizliği, kesintisiz erişim veya dolaylı zararlar konusunda garanti vermez. Mücbir sebep, bakım veya güvenlik güncellemeleri nedeniyle kısa süreli kesintiler olabilir; makul sürede bilgilendirme yapılır."},
            {"title": "6. Fesih", "body": "Hesabınızı istediğiniz zaman kapatabilirsiniz. Norya, bu şartları ihlal eden veya kötüye kullanım tespit edilen hesapları askıya alma veya sonlandırma hakkını saklı tutar."},
            {"title": "7. Uygulanacak Hukuk ve Uyuşmazlık", "body": "Bu şartlar Türkiye Cumhuriyeti kanunlarına tabidir. Uyuşmazlıklarda Türkiye mahkemeleri ve icra daireleri yetkilidir. Tüketici olarak Tüketici Hakem Heyetleri ve Tüketici Mahkemelerine başvuru haklarınız saklıdır."},
            {"title": "8. İletişim", "body": "Sorularınız için <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> sayfamızı veya support@noryaai.com adresini kullanabilirsiniz."},
        ],
        "footer_note": "Norya — Kan tahlili sonuçlarını anlaşılır dilde açıklayan hizmet.",
    },
    "en": {
        "title": "Terms of Use",
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
        "last_updated": "Son güncelleme: Mart 2025",
        "intro": "Norya üzerinden satın alınan hizmetler dijital hizmet niteliğindedir. Ödemeler PayTR sanal pos altyapısı ile alınır; kart bilgileriniz Norya sunucularında tutulmaz.",
        "sections": [
            {"title": "a) Dijital hizmet niteliği", "body": "Norya, kan tahlili sonuçlarını anlaşılır dilde açıklayan bir dijital analiz hizmeti sunar. Satın alınan ürün (tek analiz hakkı veya aylık/yıllık abonelik paketi) 6502 sayılı Tüketicinin Korunması Hakkında Kanun ve Mesafeli Sözleşmeler Yönetmeliği kapsamında \"anında ifa edilen dijital içerik\" niteliğindedir. Kullanıcı ödeme öncesi bu niteliği kabul etmiş sayılır."},
            {"title": "b) Tek seferlik analiz (anında dijital hizmet) ve iade", "body": "Tek analiz satın alındığında hesabınıza bir analiz hakkı tanınır. Rapor üretildiği anda hizmet ifa edilmiş olur; bu nedenle rapor oluşturulduktan sonra cayma hakkı kullanılamaz. <strong>Hiç analiz yapılmamış</strong> ve ödeme tarihinden itibaren 14 gün içinde iletilen iade talepleri değerlendirmeye alınır. Teknik hata nedeniyle rapor oluşturulamadıysa veya ödeme alınmış ancak hesaba hak tanınmamışsa iade/manuel hak tanıma yapılır."},
            {"title": "c) Abonelik iptali", "body": "Aylık veya yıllık paketlerde otomatik yenileme yoktur; süre bitince paket kendiliğinden sona erer. İptal etmek isterseniz bir sonraki dönem için yeniden ödeme yapmamanız yeterlidir. Kullanıcı panelinden aboneliğinizi görüntüleyebilirsiniz. İptal sonrası mevcut paket süreniz dolana kadar analiz hakkınız kullanılabilir; süre bittiğinde erişim sona erer."},
            {"title": "d) Ücret iadesi süreci", "body": "Uygun bulunan iadeler, talebin onaylandığı tarihten itibaren <strong>en geç 14 iş günü</strong> içinde, ödeme yapılan yönteme (kredi kartı / banka kartı) iade edilir. İade, kartınıza veya aynı ödeme kanalına yansır; banka işlem süresi ek 1–5 iş günü sürebilir. Kısmen kullanılmış paketlerde oransal iade uygulanmaz. Kötüye kullanım tespit edilen durumlarda Norya iade talebini reddetme hakkını saklı tutar."},
            {"title": "e) İletişim", "body": "İade ve iptal taleplerinizi sipariş numaranız (merchant_oid) ile <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a> adresine veya <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">İletişim</a> sayfasından iletebilirsiniz. En geç 1 iş günü içinde dönüş yapıyoruz."},
        ],
        "footer_note": "Norya — Kan tahlili sonuçlarını anlaşılır dilde açıklayan hizmet.",
    },
    "en": {
        "title": "Refund and Cancellation Policy",
        "last_updated": "Last updated: March 2025",
        "intro": "Services purchased via Norya are digital services. Payments are taken via PayTR's payment infrastructure; your card details are not stored on Norya servers.",
        "sections": [
            {"title": "a) Nature of the digital service", "body": "Norya provides a digital analysis service that explains blood test results in plain language. The product purchased (single analysis credit or monthly/yearly subscription package) qualifies as \"digital content supplied immediately\" under Turkish consumer law and the Distance Contracts Regulation. The user is deemed to have accepted this nature before payment."},
            {"title": "b) Single analysis (instant digital service) and refund", "body": "When you buy a single analysis, one analysis credit is added to your account. Once the report is generated, the service is deemed performed; therefore the right of withdrawal cannot be exercised after the report has been created. Refund requests received within 14 days of the payment date with <strong>no analysis having been performed</strong> will be considered. If the report could not be generated due to a technical error, or payment was received but the account was not credited, a refund or manual credit will be applied."},
            {"title": "c) Subscription cancellation", "body": "Monthly or yearly packages do not auto-renew; the package ends when the period ends. To cancel, simply do not pay for the next period. You can view your subscription in the user panel. After cancellation, your analysis credits remain available until the current package period ends; access then ceases."},
            {"title": "d) Refund process", "body": "Approved refunds are processed to the original payment method (credit/debit card) within <strong>14 business days</strong> of approval. The refund will appear on your card or the same payment channel; bank processing may take an additional 1–5 business days. Proportional refunds are not applied for partially used packages. Norya reserves the right to refuse refund requests where abuse is detected."},
            {"title": "e) Contact", "body": "Send refund and cancellation requests with your order number (merchant_oid) to <a href=\"mailto:support@noryaai.com\" class=\"text-norya-brand hover:underline\">support@noryaai.com</a> or via our <a href=\"/legal/iletisim\" class=\"text-norya-brand hover:underline\">Contact</a> page. We aim to respond within 1 business day."},
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
    },
}


def _content_lang(lang: str) -> str:
    """İçerik için kullanılacak dil: sadece tr ve en tam metin var."""
    if lang == "tr":
        return "tr"
    return FALLBACK_CONTENT_LANG


def get_legal_ui(lang: str) -> dict:
    """Seçilen dil için UI metinleri ve nav linkleri."""
    use_lang = lang if lang in LEGAL_LANGS else "en"
    u = _ui(use_lang)
    # Şirket bilgileri: ENV'den okunur, boşsa PLACEHOLDER veya fatura alanları kullanılır
    company_title = (settings.company_title or settings.invoice_company_title or "PLACEHOLDER_UNVAN").strip()
    company_tax_office = (settings.company_tax_office or settings.invoice_company_tax_office or "PLACEHOLDER_VD").strip()
    company_tax_number = (settings.company_tax_number or settings.gib_earsiv_user or "PLACEHOLDER_VNO").strip()
    company_address = (settings.company_address or settings.invoice_company_address or "PLACEHOLDER_ADRES").strip()
    company_phone = (settings.company_phone or "PLACEHOLDER_TELEFON").strip()
    if not company_phone.startswith("+") and company_phone.isdigit():
        company_phone = "+90 " + company_phone
    return {
        "lang": use_lang,
        "back_to_home": u["back_to_home"],
        "nav_links": _nav_links(use_lang),
        "footer_desc": u["footer_desc"],
        "footer_disclaimer": u["footer_disclaimer"],
        "company_title": company_title,
        "company_tax_office": company_tax_office,
        "company_tax_number": company_tax_number,
        "company_address": company_address,
        "company_phone": company_phone,
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
