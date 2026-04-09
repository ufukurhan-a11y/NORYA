# -*- coding: utf-8 -*-
"""Security page i18n: /security
9 languages: TR, EN, DE, FR, IT, ES, HE, HI, AR."""

from __future__ import annotations

SECURITY_LANGS = ("tr", "en", "de", "fr", "it", "es", "he", "hi", "ar")
DEFAULT_SECURITY_LANG = "en"

# ---------------------------------------------------------------------------
# ENGLISH
# ---------------------------------------------------------------------------

_SECURITY_EN = {
    # META
    "meta_title": "Security & Privacy | NoryaAI",
    "meta_description": "How NoryaAI protects your health data: encrypted transmission, controlled access, privacy-conscious architecture, and responsible product boundaries.",

    # HERO
    "hero_badge": "Security & Privacy",
    "hero_title_1": "Privacy-Conscious",
    "hero_title_2": "Infrastructure.",
    "hero_desc": "NoryaAI is built with privacy and security at its core. Your health data is handled with care — encrypted in transit, processed with access controls, and never sold to third parties.",
    "hero_cta_primary": "Start Analysis",
    "hero_cta_secondary": "Learn More",
    "hero_chip_encrypted": "Encrypted Transmission",
    "hero_chip_privacy": "Privacy-Focused",
    "hero_chip_responsible": "Responsible AI",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "Encryption Standard",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "Transit Encryption",
    "metric_3_value": "9+",
    "metric_3_label": "Supported Languages",
    "metric_4_value": "0",
    "metric_4_label": "Data Sold to Third Parties",

    # OVERVIEW SECTION
    "overview_badge": "Security Overview",
    "overview_title_1": "How We Protect",
    "overview_title_2": "Your Data",
    "overview_desc": "Multiple layers of security work together to protect your health information throughout its lifecycle.",

    # 6 OVERVIEW CARDS
    "card_1_title": "Encrypted Transmission",
    "card_1_desc": "All data is transmitted over TLS-encrypted connections. Uploaded files and generated reports are protected during transfer between your device and our servers.",
    "card_1_tag": "TLS Encrypted",

    "card_2_title": "Controlled Access",
    "card_2_desc": "Access to user data is restricted through authentication controls and role-based permissions. Administrative access follows least-privilege principles.",
    "card_2_tag": "Access Controls",

    "card_3_title": "Secure Payment Handling",
    "card_3_desc": "Payment processing is handled by PCI-compliant payment providers. Credit card details are never stored on NoryaAI servers.",
    "card_3_tag": "PCI Provider",

    "card_4_title": "Privacy-Conscious Architecture",
    "card_4_desc": "We follow data minimization principles — collecting only what is necessary to provide the service. Health data is not used for advertising or sold to third parties.",
    "card_4_tag": "Data Minimization",

    "card_5_title": "Multilingual Product",
    "card_5_desc": "Reports and analysis are delivered in 9+ languages with consistent quality controls, ensuring the same responsible presentation across all supported locales.",
    "card_5_tag": "9+ Languages",

    "card_6_title": "Responsible Product Boundaries",
    "card_6_desc": "NoryaAI is an educational health technology tool. It does not provide medical diagnoses, replace clinician judgment, or offer emergency guidance.",
    "card_6_tag": "Educational Tool",

    # DATA FLOW SECTION
    "data_badge": "Data Flow",
    "data_title_1": "How Your Data",
    "data_title_2": "Is Handled",
    "data_desc": "A high-level overview of how information flows through the NoryaAI platform — from upload to report delivery.",

    "step_1_title": "Upload",
    "step_1_desc": "Lab results uploaded over encrypted connections",
    "step_2_title": "Processing",
    "step_2_desc": "AI analysis with access controls and data isolation",
    "step_3_title": "Report",
    "step_3_desc": "Structured report created in your chosen language",
    "step_4_title": "Delivery",
    "step_4_desc": "Report delivered to authenticated users only",

    # DATA RIGHTS SECTION
    "rights_badge": "Your Data Rights",
    "rights_title_1": "Your Data,",
    "rights_title_2": "Your Control",
    "rights_desc": "We provide tools and processes to help you manage your personal data in line with applicable regulations.",

    "right_1_title": "Data Deletion",
    "right_1_desc": "You can request deletion of your account and associated data. Upon request, data is removed in accordance with applicable data protection regulations and any required legal retention periods.",
    "right_1_link": "Learn more",

    "right_2_title": "Access & Portability",
    "right_2_desc": "You have the right to access the personal data we hold about you and to request it in a portable format, subject to applicable regulations.",
    "right_2_link": "Privacy details",

    "right_3_title": "Purpose Limitation",
    "right_3_desc": "Your health data is used only to provide the analysis service you requested. It is not used for advertising, profiling, or sold to third parties.",
    "right_3_link": "Privacy policy",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "Operational Safeguards",
    "ops_title_1": "Access &",
    "ops_title_2": "Security Controls",

    "ops_1_title": "Access Management",
    "ops_1_desc": "Production systems use role-based access controls. Administrative access is limited to authorized personnel and follows least-privilege principles.",

    "ops_2_title": "Infrastructure Security",
    "ops_2_desc": "The platform uses Cloudflare for edge security and DDoS protection. Application infrastructure follows standard security hardening practices.",

    "ops_3_title": "Logging & Monitoring",
    "ops_3_desc": "System activity is logged for security and operational purposes. Monitoring helps detect and respond to potential issues.",

    "ops_4_title": "Payment Security",
    "ops_4_desc": "All payment processing is handled by PayTR, a PCI-compliant payment provider. NoryaAI does not store credit card details.",

    # REGULATORY APPROACH
    "reg_badge": "Regulatory Approach",
    "reg_title_1": "Our Approach to",
    "reg_title_2": "Data Protection",
    "reg_desc": "NoryaAI follows data protection principles aligned with applicable regulations in the regions we serve.",

    "reg_1_title": "GDPR Alignment",
    "reg_1_subtitle": "European Data Protection",
    "reg_1_desc": "We follow GDPR principles including data minimization, purpose limitation, and privacy by design. Users have rights to access, rectify, and request deletion of their personal data.",
    "reg_1_chip1": "Privacy by Design",
    "reg_1_chip2": "Data Rights",
    "reg_1_chip3": "Data Portability",

    "reg_2_title": "KVKK Alignment",
    "reg_2_subtitle": "Turkish Data Protection",
    "reg_2_desc": "As a company operating in Turkey, we follow the requirements of Turkey's Personal Data Protection Law (KVKK), including consent protocols and data controller obligations.",
    "reg_2_chip1": "Consent Protocols",
    "reg_2_chip2": "Data Controller",
    "reg_2_chip3": "Data Deletion",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "Responsible Use",
    "limits_title": "Important Limitations",
    "limits_desc": "NoryaAI is designed as an educational health technology tool. Understanding its boundaries is important for safe and responsible use.",

    "limit_1_title": "Not a Medical Diagnosis",
    "limit_1_desc": "NoryaAI provides educational explanations of lab values. It does not diagnose conditions, prescribe treatments, or replace professional medical evaluation.",

    "limit_2_title": "Not Emergency Guidance",
    "limit_2_desc": "This platform is not designed for urgent or emergency situations. If you have a medical emergency, contact your local emergency services immediately.",

    "limit_3_title": "Consult Your Healthcare Provider",
    "limit_3_desc": "Always discuss your lab results with a qualified healthcare professional before making health-related decisions.",

    # TRUST FRAMEWORK
    "trust_badge": "Trust Framework",
    "trust_title": "Explore Our Trust Framework",
    "trust_1_title": "Methodology",
    "trust_1_desc": "How we interpret blood test results",
    "trust_2_title": "Medical Review",
    "trust_2_desc": "Clinician oversight and safety",
    "trust_3_title": "Privacy Policy",
    "trust_3_desc": "How we handle your personal data",
    "trust_4_title": "Transparency",
    "trust_4_desc": "How we define and present claims",
    "trust_5_title": "Terms of Use",
    "trust_5_desc": "Service terms and responsibilities",
    "trust_6_title": "Trust Center",
    "trust_6_desc": "Our complete trust framework",

    # PROCUREMENT CTA
    "procurement_badge": "For Organizations",
    "procurement_title": "Evaluating NoryaAI for Your Organization?",
    "procurement_desc": "Learn more about our methodology, privacy practices, medical review process, and responsible use framework.",
    "procurement_cta_1": "Enterprise Information",
    "procurement_cta_2": "Contact Us",
    "procurement_cta_3": "View Methodology",

    # FAQ
    "faq_badge": "FAQ",
    "faq_title_1": "Security",
    "faq_title_2": "Questions",

    "faq_q1": "How is my health data protected?",
    "faq_a1": "All data is transmitted over TLS-encrypted connections. Uploaded lab results are processed with access controls in place, and reports are delivered only to authenticated users. We follow data minimization principles and do not sell health data to third parties.",

    "faq_q2": "Can NoryaAI staff see my lab results?",
    "faq_a2": "Access to user data is restricted through role-based controls. Our team accesses user data only when necessary for technical support or system maintenance, and only to the extent needed for that purpose.",

    "faq_q3": "How can I delete my data?",
    "faq_a3": "You can request deletion of your account and associated data at any time by contacting us. We process deletion requests in accordance with applicable data protection regulations, subject to any legally required retention periods.",

    "faq_q4": "Is my payment information secure?",
    "faq_a4": "We do not store credit card details. All payment processing is handled by PayTR, a PCI-compliant payment provider. Transaction data is tokenized and encrypted.",

    "faq_q5": "Does NoryaAI share data with third parties?",
    "faq_a5": "Your health data is not shared with third parties for advertising or marketing purposes. We work with service providers (hosting, payment) as necessary to deliver the service, as described in our Privacy Policy.",

    # BOTTOM CTA
    "cta_title_1": "Start Your Secure",
    "cta_title_2": "Health Journey",
    "cta_desc": "Upload your lab results and get clear, educational health insights — with privacy and security built in.",
    "cta_primary": "Get Started",
    "cta_secondary": "Contact Us",

    # NAV
    "nav_analysis": "Analysis",
    "nav_science": "Science",
    "nav_about": "About",
    "nav_security": "Security",
    "nav_pricing": "Pricing",
    "nav_get_started": "Get Started",
    "nav_menu": "Menu",

    # FOOTER
    "footer_platform": "Platform",
    "footer_biomarkers": "Biomarkers",
    "footer_science": "Science",
    "footer_reports": "Reports",
    "footer_trust_legal": "Trust & Legal",
    "footer_privacy_policy": "Privacy Policy",
    "footer_terms": "Terms of Use",
    "footer_security": "Security",
    "footer_gdpr_kvkk": "GDPR & KVKK",
    "footer_trust_center": "Trust Center",
    "footer_contact_heading": "Contact",
    "footer_support": "Support",
    "footer_security_inquiries": "Security Inquiries",
    "footer_enterprise": "Enterprise",
    "footer_copyright": "© 2025 NoryaAI. Responsible health technology.",
    "footer_tagline": "AI-powered blood test explanations in plain language. Not a substitute for medical advice.",

    # SEO INTERNAL LINKS
    "seo_explore": "Explore",
}

# ---------------------------------------------------------------------------
# TURKISH
# ---------------------------------------------------------------------------

_SECURITY_TR = {
    # META
    "meta_title": "Güvenlik ve Gizlilik | NoryaAI",
    "meta_description": "NoryaAI sağlık verilerinizi nasıl korur: şifreli iletim, kontrollü erişim, gizlilik odaklı mimari ve sorumlu ürün sınırları.",

    # HERO
    "hero_badge": "Güvenlik ve Gizlilik",
    "hero_title_1": "Gizlilik Odaklı",
    "hero_title_2": "Altyapı.",
    "hero_desc": "NoryaAI, gizlilik ve güvenliği temel ilke olarak benimser. Sağlık verileriniz özenle işlenir — iletim sırasında şifrelenir, erişim kontrolleriyle işlenir ve asla üçüncü taraflara satılmaz.",
    "hero_cta_primary": "Analize Başla",
    "hero_cta_secondary": "Daha Fazla Bilgi",
    "hero_chip_encrypted": "Şifreli İletim",
    "hero_chip_privacy": "Gizlilik Odaklı",
    "hero_chip_responsible": "Sorumlu Yapay Zekâ",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "Şifreleme Standardı",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "İletim Şifrelemesi",
    "metric_3_value": "9+",
    "metric_3_label": "Desteklenen Dil",
    "metric_4_value": "0",
    "metric_4_label": "Üçüncü Taraflara Satılan Veri",

    # OVERVIEW SECTION
    "overview_badge": "Güvenlik Genel Bakışı",
    "overview_title_1": "Verilerinizi Nasıl",
    "overview_title_2": "Koruyoruz",
    "overview_desc": "Birden fazla güvenlik katmanı, sağlık bilgilerinizi yaşam döngüsü boyunca korumak için birlikte çalışır.",

    # 6 OVERVIEW CARDS
    "card_1_title": "Şifreli İletim",
    "card_1_desc": "Tüm veriler TLS şifreli bağlantılar üzerinden iletilir. Yüklenen dosyalar ve oluşturulan raporlar, cihazınız ile sunucularımız arasındaki aktarım sırasında korunur.",
    "card_1_tag": "TLS Şifreli",

    "card_2_title": "Kontrollü Erişim",
    "card_2_desc": "Kullanıcı verilerine erişim, kimlik doğrulama kontrolleri ve rol tabanlı izinlerle kısıtlanmıştır. Yönetici erişimi en az ayrıcalık ilkesine uyar.",
    "card_2_tag": "Erişim Kontrolleri",

    "card_3_title": "Güvenli Ödeme İşleme",
    "card_3_desc": "Ödeme işlemleri PCI uyumlu ödeme sağlayıcıları tarafından gerçekleştirilir. Kredi kartı bilgileri NoryaAI sunucularında asla saklanmaz.",
    "card_3_tag": "PCI Sağlayıcı",

    "card_4_title": "Gizlilik Odaklı Mimari",
    "card_4_desc": "Veri minimizasyonu ilkelerini takip ediyoruz — yalnızca hizmeti sunmak için gerekli olanı topluyoruz. Sağlık verileri reklam amacıyla kullanılmaz veya üçüncü taraflara satılmaz.",
    "card_4_tag": "Veri Minimizasyonu",

    "card_5_title": "Çok Dilli Ürün",
    "card_5_desc": "Raporlar ve analizler, tutarlı kalite kontrolleriyle 9'dan fazla dilde sunulur ve desteklenen tüm bölgelerde aynı sorumlu sunum sağlanır.",
    "card_5_tag": "9+ Dil",

    "card_6_title": "Sorumlu Ürün Sınırları",
    "card_6_desc": "NoryaAI eğitim amaçlı bir sağlık teknolojisi aracıdır. Tıbbi teşhis koymaz, klinisyen kararının yerini almaz veya acil durum rehberliği sunmaz.",
    "card_6_tag": "Eğitim Aracı",

    # DATA FLOW SECTION
    "data_badge": "Veri Akışı",
    "data_title_1": "Verileriniz Nasıl",
    "data_title_2": "İşlenir",
    "data_desc": "NoryaAI platformu üzerinden bilginin nasıl aktığına dair üst düzey bir genel bakış — yüklemeden rapor teslimatına kadar.",

    "step_1_title": "Yükleme",
    "step_1_desc": "Laboratuvar sonuçları şifreli bağlantılar üzerinden yüklenir",
    "step_2_title": "İşleme",
    "step_2_desc": "Erişim kontrolleri ve veri izolasyonu ile akıllı analiz",
    "step_3_title": "Rapor",
    "step_3_desc": "Seçtiğiniz dilde yapılandırılmış rapor oluşturulur",
    "step_4_title": "Teslimat",
    "step_4_desc": "Rapor yalnızca kimliği doğrulanmış kullanıcılara teslim edilir",

    # DATA RIGHTS SECTION
    "rights_badge": "Veri Haklarınız",
    "rights_title_1": "Verileriniz,",
    "rights_title_2": "Sizin Kontrolünüzde",
    "rights_desc": "Kişisel verilerinizi geçerli düzenlemelere uygun şekilde yönetmenize yardımcı olacak araçlar ve süreçler sunuyoruz.",

    "right_1_title": "Veri Silme",
    "right_1_desc": "Hesabınızın ve ilişkili verilerinizin silinmesini talep edebilirsiniz. Talep üzerine veriler, geçerli veri koruma düzenlemeleri ve yasal saklama süreleri doğrultusunda kaldırılır.",
    "right_1_link": "Daha fazla bilgi",

    "right_2_title": "Erişim ve Taşınabilirlik",
    "right_2_desc": "Hakkınızda tuttuğumuz kişisel verilere erişme ve bunları taşınabilir bir biçimde talep etme hakkına sahipsiniz.",
    "right_2_link": "Gizlilik detayları",

    "right_3_title": "Amaç Sınırlaması",
    "right_3_desc": "Sağlık verileriniz yalnızca talep ettiğiniz analiz hizmetini sunmak için kullanılır. Reklam, profil oluşturma amacıyla kullanılmaz veya üçüncü taraflara satılmaz.",
    "right_3_link": "Gizlilik politikası",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "Operasyonel Güvenceler",
    "ops_title_1": "Erişim ve",
    "ops_title_2": "Güvenlik Kontrolleri",

    "ops_1_title": "Erişim Yönetimi",
    "ops_1_desc": "Üretim sistemleri rol tabanlı erişim kontrolleri kullanır. Yönetici erişimi yetkili personelle sınırlıdır ve en az ayrıcalık ilkesine uyar.",

    "ops_2_title": "Altyapı Güvenliği",
    "ops_2_desc": "Platform, uç güvenlik ve DDoS koruması için Cloudflare kullanır. Uygulama altyapısı standart güvenlik sıkılaştırma uygulamalarını takip eder.",

    "ops_3_title": "Günlükleme ve İzleme",
    "ops_3_desc": "Sistem etkinliği güvenlik ve operasyonel amaçlarla günlüğe kaydedilir. İzleme, olası sorunların tespit edilmesine ve müdahale edilmesine yardımcı olur.",

    "ops_4_title": "Ödeme Güvenliği",
    "ops_4_desc": "Tüm ödeme işlemleri, PCI uyumlu bir ödeme sağlayıcısı olan PayTR tarafından gerçekleştirilir. NoryaAI kredi kartı bilgilerini saklamaz.",

    # REGULATORY APPROACH
    "reg_badge": "Düzenleyici Yaklaşım",
    "reg_title_1": "Veri Korumaya",
    "reg_title_2": "Yaklaşımımız",
    "reg_desc": "NoryaAI, hizmet verdiğimiz bölgelerdeki geçerli düzenlemelerle uyumlu veri koruma ilkelerini takip eder.",

    "reg_1_title": "GDPR Uyumu",
    "reg_1_subtitle": "Avrupa Veri Koruma",
    "reg_1_desc": "Veri minimizasyonu, amaç sınırlaması ve tasarımdan gizlilik dahil GDPR ilkelerini takip ediyoruz. Kullanıcılar kişisel verilerine erişme, düzeltme ve silme talebinde bulunma haklarına sahiptir.",
    "reg_1_chip1": "Tasarımdan Gizlilik",
    "reg_1_chip2": "Veri Hakları",
    "reg_1_chip3": "Veri Taşınabilirliği",

    "reg_2_title": "KVKK Uyumu",
    "reg_2_subtitle": "Türkiye Veri Koruma",
    "reg_2_desc": "Türkiye'de faaliyet gösteren bir şirket olarak, Kişisel Verilerin Korunması Kanunu'nun (KVKK) gerekliliklerini, rıza protokolleri ve veri sorumlusu yükümlülükleri dahil olmak üzere takip ediyoruz.",
    "reg_2_chip1": "Rıza Protokolleri",
    "reg_2_chip2": "Veri Sorumlusu",
    "reg_2_chip3": "Veri Silme",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "Sorumlu Kullanım",
    "limits_title": "Önemli Sınırlamalar",
    "limits_desc": "NoryaAI eğitim amaçlı bir sağlık teknolojisi aracı olarak tasarlanmıştır. Güvenli ve sorumlu kullanım için sınırlarını anlamak önemlidir.",

    "limit_1_title": "Tıbbi Teşhis Değildir",
    "limit_1_desc": "NoryaAI, laboratuvar değerlerinin eğitim amaçlı açıklamalarını sunar. Hastalık teşhisi koymaz, tedavi reçete etmez veya profesyonel tıbbi değerlendirmenin yerini almaz.",

    "limit_2_title": "Acil Durum Rehberliği Değildir",
    "limit_2_desc": "Bu platform acil veya ivedi durumlar için tasarlanmamıştır. Tıbbi bir acil durumunuz varsa derhal yerel acil servislerinize başvurun.",

    "limit_3_title": "Sağlık Uzmanınıza Danışın",
    "limit_3_desc": "Sağlıkla ilgili kararlar almadan önce laboratuvar sonuçlarınızı her zaman nitelikli bir sağlık uzmanıyla görüşün.",

    # TRUST FRAMEWORK
    "trust_badge": "Güven Çerçevesi",
    "trust_title": "Güven Çerçevemizi Keşfedin",
    "trust_1_title": "Metodoloji",
    "trust_1_desc": "Kan testi sonuçlarını nasıl yorumluyoruz",
    "trust_2_title": "Tıbbi İnceleme",
    "trust_2_desc": "Klinisyen gözetimi ve güvenlik",
    "trust_3_title": "Gizlilik Politikası",
    "trust_3_desc": "Kişisel verilerinizi nasıl işliyoruz",
    "trust_4_title": "Şeffaflık",
    "trust_4_desc": "İddiaları nasıl tanımlıyor ve sunuyoruz",
    "trust_5_title": "Kullanım Koşulları",
    "trust_5_desc": "Hizmet şartları ve sorumluluklar",
    "trust_6_title": "Güven Merkezi",
    "trust_6_desc": "Eksiksiz güven çerçevemiz",

    # PROCUREMENT CTA
    "procurement_badge": "Kurumlar İçin",
    "procurement_title": "Kurumunuz İçin NoryaAI'ı Değerlendiriyor musunuz?",
    "procurement_desc": "Metodolojimiz, gizlilik uygulamalarımız, tıbbi inceleme sürecimiz ve sorumlu kullanım çerçevemiz hakkında daha fazla bilgi edinin.",
    "procurement_cta_1": "Kurumsal Bilgi",
    "procurement_cta_2": "Bize Ulaşın",
    "procurement_cta_3": "Metodolojiyi İncele",

    # FAQ
    "faq_badge": "SSS",
    "faq_title_1": "Güvenlik",
    "faq_title_2": "Soruları",

    "faq_q1": "Sağlık verilerim nasıl korunuyor?",
    "faq_a1": "Tüm veriler TLS şifreli bağlantılar üzerinden iletilir. Yüklenen laboratuvar sonuçları erişim kontrolleri ile işlenir ve raporlar yalnızca kimliği doğrulanmış kullanıcılara teslim edilir. Veri minimizasyonu ilkelerini takip ediyoruz ve sağlık verilerini üçüncü taraflara satmıyoruz.",

    "faq_q2": "NoryaAI çalışanları laboratuvar sonuçlarımı görebilir mi?",
    "faq_a2": "Kullanıcı verilerine erişim rol tabanlı kontrollerle kısıtlanmıştır. Ekibimiz kullanıcı verilerine yalnızca teknik destek veya sistem bakımı için gerekli olduğunda ve yalnızca gereken ölçüde erişir.",

    "faq_q3": "Verilerimi nasıl silebilirim?",
    "faq_a3": "Hesabınızın ve ilişkili verilerinizin silinmesini istediğiniz zaman bizimle iletişime geçerek talep edebilirsiniz. Silme taleplerini geçerli veri koruma düzenlemelerine ve yasal saklama sürelerine uygun şekilde işliyoruz.",

    "faq_q4": "Ödeme bilgilerim güvende mi?",
    "faq_a4": "Kredi kartı bilgilerini saklamıyoruz. Tüm ödeme işlemleri PCI uyumlu bir ödeme sağlayıcısı olan PayTR tarafından gerçekleştirilir. İşlem verileri tokenize edilir ve şifrelenir.",

    "faq_q5": "NoryaAI verileri üçüncü taraflarla paylaşıyor mu?",
    "faq_a5": "Sağlık verileriniz reklam veya pazarlama amacıyla üçüncü taraflarla paylaşılmaz. Gizlilik Politikamızda açıklandığı şekilde hizmeti sunmak için gerekli servis sağlayıcılarıyla (barındırma, ödeme) çalışıyoruz.",

    # BOTTOM CTA
    "cta_title_1": "Güvenli Sağlık",
    "cta_title_2": "Yolculuğunuza Başlayın",
    "cta_desc": "Laboratuvar sonuçlarınızı yükleyin ve gizlilik ile güvenlik yerleşik olarak sunulan net, eğitim amaçlı sağlık içgörüleri elde edin.",
    "cta_primary": "Başlayın",
    "cta_secondary": "Bize Ulaşın",

    # NAV
    "nav_analysis": "Analiz",
    "nav_science": "Bilim",
    "nav_about": "Hakkımızda",
    "nav_security": "Güvenlik",
    "nav_pricing": "Fiyatlandırma",
    "nav_get_started": "Başlayın",
    "nav_menu": "Menü",

    # FOOTER
    "footer_platform": "Platform",
    "footer_biomarkers": "Biyobelirteçler",
    "footer_science": "Bilim",
    "footer_reports": "Raporlar",
    "footer_trust_legal": "Güven ve Hukuki",
    "footer_privacy_policy": "Gizlilik Politikası",
    "footer_terms": "Kullanım Koşulları",
    "footer_security": "Güvenlik",
    "footer_gdpr_kvkk": "GDPR ve KVKK",
    "footer_trust_center": "Güven Merkezi",
    "footer_contact_heading": "İletişim",
    "footer_support": "Destek",
    "footer_security_inquiries": "Güvenlik Soruları",
    "footer_enterprise": "Kurumsal",
    "footer_copyright": "© 2025 NoryaAI. Sorumlu sağlık teknolojisi.",
    "footer_tagline": "Yapay zekâ destekli kan testi açıklamaları, anlaşılır bir dilde. Tıbbi tavsiye yerine geçmez.",

    # SEO INTERNAL LINKS
    "seo_explore": "Keşfet",
}

# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------

_SECURITY_DE = {
    # META
    "meta_title": "Sicherheit & Datenschutz | NoryaAI",
    "meta_description": "Wie NoryaAI Ihre Gesundheitsdaten schützt: verschlüsselte Übertragung, kontrollierter Zugriff, datenschutzbewusste Architektur und verantwortungsvolle Produktgrenzen.",

    # HERO
    "hero_badge": "Sicherheit & Datenschutz",
    "hero_title_1": "Datenschutzbewusste",
    "hero_title_2": "Infrastruktur.",
    "hero_desc": "NoryaAI basiert auf den Grundprinzipien Datenschutz und Sicherheit. Ihre Gesundheitsdaten werden sorgfältig behandelt — während der Übertragung verschlüsselt, mit Zugriffskontrollen verarbeitet und niemals an Dritte verkauft.",
    "hero_cta_primary": "Analyse starten",
    "hero_cta_secondary": "Mehr erfahren",
    "hero_chip_encrypted": "Verschlüsselte Übertragung",
    "hero_chip_privacy": "Datenschutzorientiert",
    "hero_chip_responsible": "Verantwortungsvolle KI",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "Verschlüsselungsstandard",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "Transportverschlüsselung",
    "metric_3_value": "9+",
    "metric_3_label": "Unterstützte Sprachen",
    "metric_4_value": "0",
    "metric_4_label": "An Dritte verkaufte Daten",

    # OVERVIEW SECTION
    "overview_badge": "Sicherheitsübersicht",
    "overview_title_1": "Wie wir Ihre",
    "overview_title_2": "Daten schützen",
    "overview_desc": "Mehrere Sicherheitsebenen arbeiten zusammen, um Ihre Gesundheitsinformationen während ihres gesamten Lebenszyklus zu schützen.",

    # 6 OVERVIEW CARDS
    "card_1_title": "Verschlüsselte Übertragung",
    "card_1_desc": "Alle Daten werden über TLS-verschlüsselte Verbindungen übertragen. Hochgeladene Dateien und erstellte Berichte sind während der Übertragung zwischen Ihrem Gerät und unseren Servern geschützt.",
    "card_1_tag": "TLS-verschlüsselt",

    "card_2_title": "Kontrollierter Zugriff",
    "card_2_desc": "Der Zugriff auf Benutzerdaten ist durch Authentifizierungskontrollen und rollenbasierte Berechtigungen eingeschränkt. Administrativer Zugriff folgt dem Prinzip der geringsten Berechtigung.",
    "card_2_tag": "Zugriffskontrollen",

    "card_3_title": "Sichere Zahlungsabwicklung",
    "card_3_desc": "Die Zahlungsabwicklung erfolgt durch PCI-konforme Zahlungsanbieter. Kreditkartendaten werden niemals auf NoryaAI-Servern gespeichert.",
    "card_3_tag": "PCI-Anbieter",

    "card_4_title": "Datenschutzbewusste Architektur",
    "card_4_desc": "Wir folgen dem Grundsatz der Datenminimierung — es werden nur die Daten erhoben, die zur Erbringung des Dienstes erforderlich sind. Gesundheitsdaten werden nicht für Werbung verwendet oder an Dritte verkauft.",
    "card_4_tag": "Datenminimierung",

    "card_5_title": "Mehrsprachiges Produkt",
    "card_5_desc": "Berichte und Analysen werden in über 9 Sprachen mit einheitlichen Qualitätskontrollen bereitgestellt, um in allen unterstützten Regionen dieselbe verantwortungsvolle Darstellung zu gewährleisten.",
    "card_5_tag": "9+ Sprachen",

    "card_6_title": "Verantwortungsvolle Produktgrenzen",
    "card_6_desc": "NoryaAI ist ein Bildungsinstrument im Bereich Gesundheitstechnologie. Es stellt keine medizinischen Diagnosen, ersetzt nicht das klinische Urteil und bietet keine Notfallberatung.",
    "card_6_tag": "Bildungsinstrument",

    # DATA FLOW SECTION
    "data_badge": "Datenfluss",
    "data_title_1": "Wie Ihre Daten",
    "data_title_2": "verarbeitet werden",
    "data_desc": "Ein Überblick darüber, wie Informationen durch die NoryaAI-Plattform fließen — vom Upload bis zur Berichtsübermittlung.",

    "step_1_title": "Upload",
    "step_1_desc": "Laborergebnisse werden über verschlüsselte Verbindungen hochgeladen",
    "step_2_title": "Verarbeitung",
    "step_2_desc": "KI-Analyse mit Zugriffskontrollen und Datenisolierung",
    "step_3_title": "Bericht",
    "step_3_desc": "Strukturierter Bericht in Ihrer gewählten Sprache erstellt",
    "step_4_title": "Zustellung",
    "step_4_desc": "Bericht wird nur an authentifizierte Benutzer übermittelt",

    # DATA RIGHTS SECTION
    "rights_badge": "Ihre Datenrechte",
    "rights_title_1": "Ihre Daten,",
    "rights_title_2": "Ihre Kontrolle",
    "rights_desc": "Wir stellen Werkzeuge und Verfahren bereit, die Ihnen helfen, Ihre personenbezogenen Daten im Einklang mit geltenden Vorschriften zu verwalten.",

    "right_1_title": "Datenlöschung",
    "right_1_desc": "Sie können die Löschung Ihres Kontos und der zugehörigen Daten beantragen. Auf Anfrage werden Daten gemäß den geltenden Datenschutzbestimmungen und gesetzlichen Aufbewahrungsfristen entfernt.",
    "right_1_link": "Mehr erfahren",

    "right_2_title": "Zugang & Übertragbarkeit",
    "right_2_desc": "Sie haben das Recht, auf die von uns über Sie gespeicherten personenbezogenen Daten zuzugreifen und diese in einem übertragbaren Format anzufordern.",
    "right_2_link": "Datenschutzdetails",

    "right_3_title": "Zweckbindung",
    "right_3_desc": "Ihre Gesundheitsdaten werden ausschließlich zur Bereitstellung des von Ihnen angeforderten Analysedienstes verwendet. Sie werden nicht für Werbung, Profiling oder den Verkauf an Dritte genutzt.",
    "right_3_link": "Datenschutzrichtlinie",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "Betriebliche Sicherungsmaßnahmen",
    "ops_title_1": "Zugriffs- &",
    "ops_title_2": "Sicherheitskontrollen",

    "ops_1_title": "Zugriffsverwaltung",
    "ops_1_desc": "Produktionssysteme verwenden rollenbasierte Zugriffskontrollen. Administrativer Zugriff ist auf autorisiertes Personal beschränkt und folgt dem Prinzip der geringsten Berechtigung.",

    "ops_2_title": "Infrastruktursicherheit",
    "ops_2_desc": "Die Plattform nutzt Cloudflare für Edge-Sicherheit und DDoS-Schutz. Die Anwendungsinfrastruktur folgt bewährten Sicherheitshärtungspraktiken.",

    "ops_3_title": "Protokollierung & Überwachung",
    "ops_3_desc": "Systemaktivitäten werden zu Sicherheits- und Betriebszwecken protokolliert. Überwachung hilft bei der Erkennung und Reaktion auf potenzielle Probleme.",

    "ops_4_title": "Zahlungssicherheit",
    "ops_4_desc": "Die gesamte Zahlungsabwicklung erfolgt über PayTR, einen PCI-konformen Zahlungsanbieter. NoryaAI speichert keine Kreditkartendaten.",

    # REGULATORY APPROACH
    "reg_badge": "Regulatorischer Ansatz",
    "reg_title_1": "Unser Ansatz zum",
    "reg_title_2": "Datenschutz",
    "reg_desc": "NoryaAI folgt Datenschutzprinzipien, die auf die geltenden Vorschriften in den von uns bedienten Regionen abgestimmt sind.",

    "reg_1_title": "DSGVO-Ausrichtung",
    "reg_1_subtitle": "Europäischer Datenschutz",
    "reg_1_desc": "Wir folgen DSGVO-Grundsätzen einschließlich Datenminimierung, Zweckbindung und Datenschutz durch Technikgestaltung. Nutzer haben das Recht auf Zugang, Berichtigung und Löschung ihrer personenbezogenen Daten.",
    "reg_1_chip1": "Privacy by Design",
    "reg_1_chip2": "Datenrechte",
    "reg_1_chip3": "Datenübertragbarkeit",

    "reg_2_title": "KVKK-Ausrichtung",
    "reg_2_subtitle": "Türkischer Datenschutz",
    "reg_2_desc": "Als in der Türkei tätiges Unternehmen erfüllen wir die Anforderungen des türkischen Datenschutzgesetzes (KVKK), einschließlich Einwilligungsprotokolle und Pflichten des Datenverantwortlichen.",
    "reg_2_chip1": "Einwilligungsprotokolle",
    "reg_2_chip2": "Datenverantwortlicher",
    "reg_2_chip3": "Datenlöschung",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "Verantwortungsvoller Gebrauch",
    "limits_title": "Wichtige Einschränkungen",
    "limits_desc": "NoryaAI ist als Bildungsinstrument im Bereich Gesundheitstechnologie konzipiert. Das Verständnis seiner Grenzen ist für eine sichere und verantwortungsvolle Nutzung wichtig.",

    "limit_1_title": "Keine medizinische Diagnose",
    "limit_1_desc": "NoryaAI bietet bildungsbezogene Erläuterungen zu Laborwerten. Es diagnostiziert keine Erkrankungen, verschreibt keine Behandlungen und ersetzt keine professionelle medizinische Beurteilung.",

    "limit_2_title": "Keine Notfallberatung",
    "limit_2_desc": "Diese Plattform ist nicht für dringende oder notfallmedizinische Situationen konzipiert. Kontaktieren Sie im Notfall umgehend Ihren örtlichen Rettungsdienst.",

    "limit_3_title": "Konsultieren Sie Ihren Arzt",
    "limit_3_desc": "Besprechen Sie Ihre Laborergebnisse immer mit einem qualifizierten Arzt, bevor Sie gesundheitsbezogene Entscheidungen treffen.",

    # TRUST FRAMEWORK
    "trust_badge": "Vertrauensrahmen",
    "trust_title": "Entdecken Sie unseren Vertrauensrahmen",
    "trust_1_title": "Methodik",
    "trust_1_desc": "Wie wir Bluttestergebnisse interpretieren",
    "trust_2_title": "Medizinische Überprüfung",
    "trust_2_desc": "Klinische Aufsicht und Sicherheit",
    "trust_3_title": "Datenschutzrichtlinie",
    "trust_3_desc": "Wie wir mit Ihren personenbezogenen Daten umgehen",
    "trust_4_title": "Transparenz",
    "trust_4_desc": "Wie wir Aussagen definieren und präsentieren",
    "trust_5_title": "Nutzungsbedingungen",
    "trust_5_desc": "Servicebedingungen und Verantwortlichkeiten",
    "trust_6_title": "Vertrauenszentrum",
    "trust_6_desc": "Unser vollständiger Vertrauensrahmen",

    # PROCUREMENT CTA
    "procurement_badge": "Für Organisationen",
    "procurement_title": "Evaluieren Sie NoryaAI für Ihre Organisation?",
    "procurement_desc": "Erfahren Sie mehr über unsere Methodik, Datenschutzpraktiken, medizinische Überprüfungsverfahren und den Rahmen für verantwortungsvolle Nutzung.",
    "procurement_cta_1": "Unternehmensinformationen",
    "procurement_cta_2": "Kontaktieren Sie uns",
    "procurement_cta_3": "Methodik ansehen",

    # FAQ
    "faq_badge": "FAQ",
    "faq_title_1": "Sicherheits-",
    "faq_title_2": "fragen",

    "faq_q1": "Wie werden meine Gesundheitsdaten geschützt?",
    "faq_a1": "Alle Daten werden über TLS-verschlüsselte Verbindungen übertragen. Hochgeladene Laborergebnisse werden mit vorhandenen Zugriffskontrollen verarbeitet und Berichte nur an authentifizierte Benutzer übermittelt. Wir folgen dem Grundsatz der Datenminimierung und verkaufen Gesundheitsdaten nicht an Dritte.",

    "faq_q2": "Können NoryaAI-Mitarbeiter meine Laborergebnisse sehen?",
    "faq_a2": "Der Zugriff auf Benutzerdaten ist durch rollenbasierte Kontrollen eingeschränkt. Unser Team greift nur bei Bedarf für technischen Support oder Systemwartung auf Benutzerdaten zu, und nur im erforderlichen Umfang.",

    "faq_q3": "Wie kann ich meine Daten löschen?",
    "faq_a3": "Sie können jederzeit die Löschung Ihres Kontos und der zugehörigen Daten beantragen, indem Sie uns kontaktieren. Wir bearbeiten Löschanfragen gemäß den geltenden Datenschutzbestimmungen und unter Berücksichtigung gesetzlicher Aufbewahrungsfristen.",

    "faq_q4": "Sind meine Zahlungsinformationen sicher?",
    "faq_a4": "Wir speichern keine Kreditkartendaten. Die gesamte Zahlungsabwicklung erfolgt über PayTR, einen PCI-konformen Zahlungsanbieter. Transaktionsdaten werden tokenisiert und verschlüsselt.",

    "faq_q5": "Teilt NoryaAI Daten mit Dritten?",
    "faq_a5": "Ihre Gesundheitsdaten werden nicht für Werbe- oder Marketingzwecke an Dritte weitergegeben. Wir arbeiten mit Dienstleistern (Hosting, Zahlungen) zusammen, soweit dies zur Erbringung des Dienstes erforderlich ist, wie in unserer Datenschutzrichtlinie beschrieben.",

    # BOTTOM CTA
    "cta_title_1": "Starten Sie Ihre sichere",
    "cta_title_2": "Gesundheitsreise",
    "cta_desc": "Laden Sie Ihre Laborergebnisse hoch und erhalten Sie klare, bildungsbezogene Gesundheitseinblicke — mit integriertem Datenschutz und Sicherheit.",
    "cta_primary": "Jetzt starten",
    "cta_secondary": "Kontaktieren Sie uns",

    # NAV
    "nav_analysis": "Analyse",
    "nav_science": "Wissenschaft",
    "nav_about": "Über uns",
    "nav_security": "Sicherheit",
    "nav_pricing": "Preise",
    "nav_get_started": "Jetzt starten",
    "nav_menu": "Menü",

    # FOOTER
    "footer_platform": "Plattform",
    "footer_biomarkers": "Biomarker",
    "footer_science": "Wissenschaft",
    "footer_reports": "Berichte",
    "footer_trust_legal": "Vertrauen & Recht",
    "footer_privacy_policy": "Datenschutzrichtlinie",
    "footer_terms": "Nutzungsbedingungen",
    "footer_security": "Sicherheit",
    "footer_gdpr_kvkk": "DSGVO & KVKK",
    "footer_trust_center": "Vertrauenszentrum",
    "footer_contact_heading": "Kontakt",
    "footer_support": "Support",
    "footer_security_inquiries": "Sicherheitsanfragen",
    "footer_enterprise": "Unternehmen",
    "footer_copyright": "© 2025 NoryaAI. Verantwortungsvolle Gesundheitstechnologie.",
    "footer_tagline": "KI-gestützte Bluttest-Erklärungen in verständlicher Sprache. Kein Ersatz für ärztlichen Rat.",

    # SEO INTERNAL LINKS
    "seo_explore": "Entdecken",
}

# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------

_SECURITY_FR = {
    # META
    "meta_title": "Sécurité & Confidentialité | NoryaAI",
    "meta_description": "Comment NoryaAI protège vos données de santé : transmission chiffrée, accès contrôlé, architecture respectueuse de la vie privée et limites responsables du produit.",

    # HERO
    "hero_badge": "Sécurité & Confidentialité",
    "hero_title_1": "Infrastructure",
    "hero_title_2": "respectueuse de la vie privée.",
    "hero_desc": "NoryaAI est conçu avec la confidentialité et la sécurité au cœur de son architecture. Vos données de santé sont traitées avec soin — chiffrées en transit, traitées avec des contrôles d'accès et jamais vendues à des tiers.",
    "hero_cta_primary": "Démarrer l'analyse",
    "hero_cta_secondary": "En savoir plus",
    "hero_chip_encrypted": "Transmission chiffrée",
    "hero_chip_privacy": "Respect de la vie privée",
    "hero_chip_responsible": "IA responsable",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "Standard de chiffrement",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "Chiffrement en transit",
    "metric_3_value": "9+",
    "metric_3_label": "Langues prises en charge",
    "metric_4_value": "0",
    "metric_4_label": "Données vendues à des tiers",

    # OVERVIEW SECTION
    "overview_badge": "Aperçu de la sécurité",
    "overview_title_1": "Comment nous protégeons",
    "overview_title_2": "vos données",
    "overview_desc": "Plusieurs couches de sécurité fonctionnent ensemble pour protéger vos informations de santé tout au long de leur cycle de vie.",

    # 6 OVERVIEW CARDS
    "card_1_title": "Transmission chiffrée",
    "card_1_desc": "Toutes les données sont transmises via des connexions chiffrées TLS. Les fichiers téléchargés et les rapports générés sont protégés pendant le transfert entre votre appareil et nos serveurs.",
    "card_1_tag": "Chiffrement TLS",

    "card_2_title": "Accès contrôlé",
    "card_2_desc": "L'accès aux données utilisateur est restreint par des contrôles d'authentification et des permissions basées sur les rôles. L'accès administratif suit le principe du moindre privilège.",
    "card_2_tag": "Contrôles d'accès",

    "card_3_title": "Paiement sécurisé",
    "card_3_desc": "Le traitement des paiements est assuré par des prestataires conformes PCI. Les données de carte bancaire ne sont jamais stockées sur les serveurs NoryaAI.",
    "card_3_tag": "Prestataire PCI",

    "card_4_title": "Architecture respectueuse de la vie privée",
    "card_4_desc": "Nous suivons les principes de minimisation des données — ne collectant que ce qui est nécessaire à la fourniture du service. Les données de santé ne sont pas utilisées à des fins publicitaires ni vendues à des tiers.",
    "card_4_tag": "Minimisation des données",

    "card_5_title": "Produit multilingue",
    "card_5_desc": "Les rapports et analyses sont disponibles dans plus de 9 langues avec des contrôles de qualité uniformes, garantissant la même présentation responsable dans toutes les régions prises en charge.",
    "card_5_tag": "9+ langues",

    "card_6_title": "Limites responsables du produit",
    "card_6_desc": "NoryaAI est un outil éducatif de technologie de santé. Il ne fournit pas de diagnostics médicaux, ne remplace pas le jugement clinique et ne propose pas de conseils d'urgence.",
    "card_6_tag": "Outil éducatif",

    # DATA FLOW SECTION
    "data_badge": "Flux de données",
    "data_title_1": "Comment vos données",
    "data_title_2": "sont traitées",
    "data_desc": "Un aperçu de la circulation des informations à travers la plateforme NoryaAI — du téléchargement à la livraison du rapport.",

    "step_1_title": "Téléchargement",
    "step_1_desc": "Résultats de laboratoire téléchargés via des connexions chiffrées",
    "step_2_title": "Traitement",
    "step_2_desc": "Analyse IA avec contrôles d'accès et isolation des données",
    "step_3_title": "Rapport",
    "step_3_desc": "Rapport structuré créé dans la langue de votre choix",
    "step_4_title": "Livraison",
    "step_4_desc": "Rapport délivré uniquement aux utilisateurs authentifiés",

    # DATA RIGHTS SECTION
    "rights_badge": "Vos droits sur les données",
    "rights_title_1": "Vos données,",
    "rights_title_2": "votre contrôle",
    "rights_desc": "Nous fournissons des outils et des processus pour vous aider à gérer vos données personnelles conformément aux réglementations applicables.",

    "right_1_title": "Suppression des données",
    "right_1_desc": "Vous pouvez demander la suppression de votre compte et des données associées. Sur demande, les données sont supprimées conformément aux réglementations applicables en matière de protection des données et aux délais de conservation légaux.",
    "right_1_link": "En savoir plus",

    "right_2_title": "Accès & Portabilité",
    "right_2_desc": "Vous avez le droit d'accéder aux données personnelles que nous détenons à votre sujet et de les demander dans un format portable, conformément aux réglementations applicables.",
    "right_2_link": "Détails de confidentialité",

    "right_3_title": "Limitation de la finalité",
    "right_3_desc": "Vos données de santé sont utilisées uniquement pour fournir le service d'analyse que vous avez demandé. Elles ne sont pas utilisées à des fins publicitaires, de profilage, ni vendues à des tiers.",
    "right_3_link": "Politique de confidentialité",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "Garanties opérationnelles",
    "ops_title_1": "Contrôles d'accès",
    "ops_title_2": "et de sécurité",

    "ops_1_title": "Gestion des accès",
    "ops_1_desc": "Les systèmes de production utilisent des contrôles d'accès basés sur les rôles. L'accès administratif est limité au personnel autorisé et suit le principe du moindre privilège.",

    "ops_2_title": "Sécurité de l'infrastructure",
    "ops_2_desc": "La plateforme utilise Cloudflare pour la sécurité en périphérie et la protection DDoS. L'infrastructure applicative suit les pratiques standard de durcissement de la sécurité.",

    "ops_3_title": "Journalisation & Surveillance",
    "ops_3_desc": "L'activité du système est journalisée à des fins de sécurité et opérationnelles. La surveillance aide à détecter et répondre aux problèmes potentiels.",

    "ops_4_title": "Sécurité des paiements",
    "ops_4_desc": "Tout le traitement des paiements est assuré par PayTR, un prestataire de paiement conforme PCI. NoryaAI ne stocke pas les données de carte bancaire.",

    # REGULATORY APPROACH
    "reg_badge": "Approche réglementaire",
    "reg_title_1": "Notre approche de la",
    "reg_title_2": "protection des données",
    "reg_desc": "NoryaAI suit des principes de protection des données conformes aux réglementations applicables dans les régions que nous desservons.",

    "reg_1_title": "Conformité RGPD",
    "reg_1_subtitle": "Protection des données européenne",
    "reg_1_desc": "Nous suivons les principes du RGPD, notamment la minimisation des données, la limitation de la finalité et la protection de la vie privée dès la conception. Les utilisateurs ont le droit d'accéder à leurs données personnelles, de les rectifier et d'en demander la suppression.",
    "reg_1_chip1": "Privacy by Design",
    "reg_1_chip2": "Droits sur les données",
    "reg_1_chip3": "Portabilité des données",

    "reg_2_title": "Conformité KVKK",
    "reg_2_subtitle": "Protection des données turque",
    "reg_2_desc": "En tant qu'entreprise opérant en Turquie, nous respectons les exigences de la loi turque sur la protection des données personnelles (KVKK), y compris les protocoles de consentement et les obligations du responsable du traitement.",
    "reg_2_chip1": "Protocoles de consentement",
    "reg_2_chip2": "Responsable du traitement",
    "reg_2_chip3": "Suppression des données",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "Utilisation responsable",
    "limits_title": "Limitations importantes",
    "limits_desc": "NoryaAI est conçu comme un outil éducatif de technologie de santé. Comprendre ses limites est essentiel pour une utilisation sûre et responsable.",

    "limit_1_title": "Pas un diagnostic médical",
    "limit_1_desc": "NoryaAI fournit des explications éducatives sur les valeurs de laboratoire. Il ne diagnostique pas de pathologies, ne prescrit pas de traitements et ne remplace pas une évaluation médicale professionnelle.",

    "limit_2_title": "Pas de conseils d'urgence",
    "limit_2_desc": "Cette plateforme n'est pas conçue pour les situations urgentes ou d'urgence. En cas d'urgence médicale, contactez immédiatement vos services d'urgence locaux.",

    "limit_3_title": "Consultez votre professionnel de santé",
    "limit_3_desc": "Discutez toujours de vos résultats de laboratoire avec un professionnel de santé qualifié avant de prendre des décisions liées à votre santé.",

    # TRUST FRAMEWORK
    "trust_badge": "Cadre de confiance",
    "trust_title": "Découvrez notre cadre de confiance",
    "trust_1_title": "Méthodologie",
    "trust_1_desc": "Comment nous interprétons les résultats d'analyses sanguines",
    "trust_2_title": "Revue médicale",
    "trust_2_desc": "Supervision clinique et sécurité",
    "trust_3_title": "Politique de confidentialité",
    "trust_3_desc": "Comment nous traitons vos données personnelles",
    "trust_4_title": "Transparence",
    "trust_4_desc": "Comment nous définissons et présentons nos affirmations",
    "trust_5_title": "Conditions d'utilisation",
    "trust_5_desc": "Conditions de service et responsabilités",
    "trust_6_title": "Centre de confiance",
    "trust_6_desc": "Notre cadre de confiance complet",

    # PROCUREMENT CTA
    "procurement_badge": "Pour les organisations",
    "procurement_title": "Vous évaluez NoryaAI pour votre organisation ?",
    "procurement_desc": "Découvrez notre méthodologie, nos pratiques de confidentialité, notre processus de revue médicale et notre cadre d'utilisation responsable.",
    "procurement_cta_1": "Informations entreprise",
    "procurement_cta_2": "Contactez-nous",
    "procurement_cta_3": "Voir la méthodologie",

    # FAQ
    "faq_badge": "FAQ",
    "faq_title_1": "Questions de",
    "faq_title_2": "sécurité",

    "faq_q1": "Comment mes données de santé sont-elles protégées ?",
    "faq_a1": "Toutes les données sont transmises via des connexions chiffrées TLS. Les résultats de laboratoire téléchargés sont traités avec des contrôles d'accès en place, et les rapports ne sont délivrés qu'aux utilisateurs authentifiés. Nous suivons les principes de minimisation des données et ne vendons pas les données de santé à des tiers.",

    "faq_q2": "Le personnel de NoryaAI peut-il voir mes résultats de laboratoire ?",
    "faq_a2": "L'accès aux données utilisateur est restreint par des contrôles basés sur les rôles. Notre équipe n'accède aux données utilisateur que lorsque cela est nécessaire pour le support technique ou la maintenance du système, et uniquement dans la mesure requise.",

    "faq_q3": "Comment puis-je supprimer mes données ?",
    "faq_a3": "Vous pouvez demander la suppression de votre compte et des données associées à tout moment en nous contactant. Nous traitons les demandes de suppression conformément aux réglementations applicables en matière de protection des données, sous réserve des délais de conservation légaux.",

    "faq_q4": "Mes informations de paiement sont-elles sécurisées ?",
    "faq_a4": "Nous ne stockons pas les données de carte bancaire. Tout le traitement des paiements est assuré par PayTR, un prestataire conforme PCI. Les données de transaction sont tokenisées et chiffrées.",

    "faq_q5": "NoryaAI partage-t-il des données avec des tiers ?",
    "faq_a5": "Vos données de santé ne sont pas partagées avec des tiers à des fins publicitaires ou marketing. Nous travaillons avec des prestataires de services (hébergement, paiement) dans la mesure nécessaire à la fourniture du service, comme décrit dans notre politique de confidentialité.",

    # BOTTOM CTA
    "cta_title_1": "Commencez votre parcours",
    "cta_title_2": "santé sécurisé",
    "cta_desc": "Téléchargez vos résultats de laboratoire et obtenez des informations de santé claires et éducatives — avec confidentialité et sécurité intégrées.",
    "cta_primary": "Commencer",
    "cta_secondary": "Contactez-nous",

    # NAV
    "nav_analysis": "Analyse",
    "nav_science": "Science",
    "nav_about": "À propos",
    "nav_security": "Sécurité",
    "nav_pricing": "Tarifs",
    "nav_get_started": "Commencer",
    "nav_menu": "Menu",

    # FOOTER
    "footer_platform": "Plateforme",
    "footer_biomarkers": "Biomarqueurs",
    "footer_science": "Science",
    "footer_reports": "Rapports",
    "footer_trust_legal": "Confiance & Juridique",
    "footer_privacy_policy": "Politique de confidentialité",
    "footer_terms": "Conditions d'utilisation",
    "footer_security": "Sécurité",
    "footer_gdpr_kvkk": "RGPD & KVKK",
    "footer_trust_center": "Centre de confiance",
    "footer_contact_heading": "Contact",
    "footer_support": "Support",
    "footer_security_inquiries": "Questions de sécurité",
    "footer_enterprise": "Entreprise",
    "footer_copyright": "© 2025 NoryaAI. Technologie de santé responsable.",
    "footer_tagline": "Explications de bilans sanguins par IA dans un langage clair. Ne se substitue pas à un avis médical.",

    # SEO INTERNAL LINKS
    "seo_explore": "Explorer",
}

# ---------------------------------------------------------------------------
# SPANISH
# ---------------------------------------------------------------------------

_SECURITY_ES = {
    # META
    "meta_title": "Seguridad y Privacidad | NoryaAI",
    "meta_description": "Cómo NoryaAI protege sus datos de salud: transmisión cifrada, acceso controlado, arquitectura consciente de la privacidad y límites responsables del producto.",

    # HERO
    "hero_badge": "Seguridad y Privacidad",
    "hero_title_1": "Infraestructura",
    "hero_title_2": "consciente de la privacidad.",
    "hero_desc": "NoryaAI está construido con la privacidad y la seguridad como principios fundamentales. Sus datos de salud se manejan con cuidado — cifrados en tránsito, procesados con controles de acceso y nunca vendidos a terceros.",
    "hero_cta_primary": "Iniciar análisis",
    "hero_cta_secondary": "Más información",
    "hero_chip_encrypted": "Transmisión cifrada",
    "hero_chip_privacy": "Enfoque en privacidad",
    "hero_chip_responsible": "IA responsable",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "Estándar de cifrado",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "Cifrado en tránsito",
    "metric_3_value": "9+",
    "metric_3_label": "Idiomas admitidos",
    "metric_4_value": "0",
    "metric_4_label": "Datos vendidos a terceros",

    # OVERVIEW SECTION
    "overview_badge": "Resumen de seguridad",
    "overview_title_1": "Cómo protegemos",
    "overview_title_2": "sus datos",
    "overview_desc": "Múltiples capas de seguridad trabajan juntas para proteger su información de salud durante todo su ciclo de vida.",

    # 6 OVERVIEW CARDS
    "card_1_title": "Transmisión cifrada",
    "card_1_desc": "Todos los datos se transmiten a través de conexiones cifradas con TLS. Los archivos subidos y los informes generados están protegidos durante la transferencia entre su dispositivo y nuestros servidores.",
    "card_1_tag": "Cifrado TLS",

    "card_2_title": "Acceso controlado",
    "card_2_desc": "El acceso a los datos del usuario está restringido mediante controles de autenticación y permisos basados en roles. El acceso administrativo sigue el principio de mínimo privilegio.",
    "card_2_tag": "Controles de acceso",

    "card_3_title": "Procesamiento seguro de pagos",
    "card_3_desc": "El procesamiento de pagos es gestionado por proveedores de pago conformes con PCI. Los datos de tarjetas de crédito nunca se almacenan en los servidores de NoryaAI.",
    "card_3_tag": "Proveedor PCI",

    "card_4_title": "Arquitectura consciente de la privacidad",
    "card_4_desc": "Seguimos principios de minimización de datos — recopilando solo lo necesario para prestar el servicio. Los datos de salud no se utilizan con fines publicitarios ni se venden a terceros.",
    "card_4_tag": "Minimización de datos",

    "card_5_title": "Producto multilingüe",
    "card_5_desc": "Los informes y análisis se entregan en más de 9 idiomas con controles de calidad uniformes, asegurando la misma presentación responsable en todas las regiones admitidas.",
    "card_5_tag": "9+ idiomas",

    "card_6_title": "Límites responsables del producto",
    "card_6_desc": "NoryaAI es una herramienta educativa de tecnología sanitaria. No proporciona diagnósticos médicos, no reemplaza el juicio clínico ni ofrece orientación de emergencia.",
    "card_6_tag": "Herramienta educativa",

    # DATA FLOW SECTION
    "data_badge": "Flujo de datos",
    "data_title_1": "Cómo se gestionan",
    "data_title_2": "sus datos",
    "data_desc": "Una visión general de cómo fluye la información a través de la plataforma NoryaAI — desde la subida hasta la entrega del informe.",

    "step_1_title": "Subida",
    "step_1_desc": "Resultados de laboratorio subidos mediante conexiones cifradas",
    "step_2_title": "Procesamiento",
    "step_2_desc": "Análisis de IA con controles de acceso y aislamiento de datos",
    "step_3_title": "Informe",
    "step_3_desc": "Informe estructurado creado en el idioma elegido",
    "step_4_title": "Entrega",
    "step_4_desc": "Informe entregado solo a usuarios autenticados",

    # DATA RIGHTS SECTION
    "rights_badge": "Sus derechos sobre los datos",
    "rights_title_1": "Sus datos,",
    "rights_title_2": "su control",
    "rights_desc": "Proporcionamos herramientas y procesos para ayudarle a gestionar sus datos personales de acuerdo con las normativas aplicables.",

    "right_1_title": "Eliminación de datos",
    "right_1_desc": "Puede solicitar la eliminación de su cuenta y los datos asociados. A petición, los datos se eliminan de acuerdo con las normativas de protección de datos aplicables y los períodos de retención legales requeridos.",
    "right_1_link": "Más información",

    "right_2_title": "Acceso y portabilidad",
    "right_2_desc": "Tiene derecho a acceder a los datos personales que poseemos sobre usted y a solicitarlos en un formato portátil, sujeto a las normativas aplicables.",
    "right_2_link": "Detalles de privacidad",

    "right_3_title": "Limitación de finalidad",
    "right_3_desc": "Sus datos de salud se utilizan únicamente para proporcionar el servicio de análisis que solicitó. No se utilizan con fines publicitarios, de perfilado, ni se venden a terceros.",
    "right_3_link": "Política de privacidad",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "Medidas operativas",
    "ops_title_1": "Controles de acceso",
    "ops_title_2": "y seguridad",

    "ops_1_title": "Gestión de accesos",
    "ops_1_desc": "Los sistemas de producción utilizan controles de acceso basados en roles. El acceso administrativo está limitado al personal autorizado y sigue el principio de mínimo privilegio.",

    "ops_2_title": "Seguridad de la infraestructura",
    "ops_2_desc": "La plataforma utiliza Cloudflare para la seguridad perimetral y la protección DDoS. La infraestructura de la aplicación sigue prácticas estándar de endurecimiento de seguridad.",

    "ops_3_title": "Registro y monitorización",
    "ops_3_desc": "La actividad del sistema se registra con fines de seguridad y operativos. La monitorización ayuda a detectar y responder ante posibles incidencias.",

    "ops_4_title": "Seguridad de pagos",
    "ops_4_desc": "Todo el procesamiento de pagos es gestionado por PayTR, un proveedor de pago conforme con PCI. NoryaAI no almacena datos de tarjetas de crédito.",

    # REGULATORY APPROACH
    "reg_badge": "Enfoque regulatorio",
    "reg_title_1": "Nuestro enfoque sobre la",
    "reg_title_2": "protección de datos",
    "reg_desc": "NoryaAI sigue principios de protección de datos alineados con las normativas aplicables en las regiones donde operamos.",

    "reg_1_title": "Alineación con el RGPD",
    "reg_1_subtitle": "Protección de datos europea",
    "reg_1_desc": "Seguimos los principios del RGPD, incluyendo la minimización de datos, la limitación de finalidad y la privacidad desde el diseño. Los usuarios tienen derecho a acceder, rectificar y solicitar la eliminación de sus datos personales.",
    "reg_1_chip1": "Privacidad desde el diseño",
    "reg_1_chip2": "Derechos sobre los datos",
    "reg_1_chip3": "Portabilidad de datos",

    "reg_2_title": "Alineación con KVKK",
    "reg_2_subtitle": "Protección de datos turca",
    "reg_2_desc": "Como empresa que opera en Turquía, cumplimos con los requisitos de la Ley de Protección de Datos Personales de Turquía (KVKK), incluyendo protocolos de consentimiento y obligaciones del responsable del tratamiento.",
    "reg_2_chip1": "Protocolos de consentimiento",
    "reg_2_chip2": "Responsable del tratamiento",
    "reg_2_chip3": "Eliminación de datos",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "Uso responsable",
    "limits_title": "Limitaciones importantes",
    "limits_desc": "NoryaAI está diseñado como una herramienta educativa de tecnología sanitaria. Comprender sus límites es importante para un uso seguro y responsable.",

    "limit_1_title": "No es un diagnóstico médico",
    "limit_1_desc": "NoryaAI proporciona explicaciones educativas sobre valores de laboratorio. No diagnostica enfermedades, no prescribe tratamientos ni sustituye una evaluación médica profesional.",

    "limit_2_title": "No es orientación de emergencia",
    "limit_2_desc": "Esta plataforma no está diseñada para situaciones urgentes o de emergencia. En caso de emergencia médica, contacte inmediatamente con los servicios de emergencia locales.",

    "limit_3_title": "Consulte a su profesional sanitario",
    "limit_3_desc": "Siempre consulte sus resultados de laboratorio con un profesional sanitario cualificado antes de tomar decisiones relacionadas con su salud.",

    # TRUST FRAMEWORK
    "trust_badge": "Marco de confianza",
    "trust_title": "Explore nuestro marco de confianza",
    "trust_1_title": "Metodología",
    "trust_1_desc": "Cómo interpretamos los resultados de análisis de sangre",
    "trust_2_title": "Revisión médica",
    "trust_2_desc": "Supervisión clínica y seguridad",
    "trust_3_title": "Política de privacidad",
    "trust_3_desc": "Cómo gestionamos sus datos personales",
    "trust_4_title": "Transparencia",
    "trust_4_desc": "Cómo definimos y presentamos nuestras afirmaciones",
    "trust_5_title": "Condiciones de uso",
    "trust_5_desc": "Términos del servicio y responsabilidades",
    "trust_6_title": "Centro de confianza",
    "trust_6_desc": "Nuestro marco de confianza completo",

    # PROCUREMENT CTA
    "procurement_badge": "Para organizaciones",
    "procurement_title": "¿Evaluando NoryaAI para su organización?",
    "procurement_desc": "Conozca más sobre nuestra metodología, prácticas de privacidad, proceso de revisión médica y marco de uso responsable.",
    "procurement_cta_1": "Información empresarial",
    "procurement_cta_2": "Contáctenos",
    "procurement_cta_3": "Ver metodología",

    # FAQ
    "faq_badge": "FAQ",
    "faq_title_1": "Preguntas de",
    "faq_title_2": "seguridad",

    "faq_q1": "¿Cómo se protegen mis datos de salud?",
    "faq_a1": "Todos los datos se transmiten a través de conexiones cifradas con TLS. Los resultados de laboratorio subidos se procesan con controles de acceso y los informes se entregan solo a usuarios autenticados. Seguimos principios de minimización de datos y no vendemos datos de salud a terceros.",

    "faq_q2": "¿Puede el personal de NoryaAI ver mis resultados de laboratorio?",
    "faq_a2": "El acceso a los datos de usuario está restringido mediante controles basados en roles. Nuestro equipo accede a los datos de usuario solo cuando es necesario para soporte técnico o mantenimiento del sistema, y solo en la medida necesaria.",

    "faq_q3": "¿Cómo puedo eliminar mis datos?",
    "faq_a3": "Puede solicitar la eliminación de su cuenta y los datos asociados en cualquier momento contactándonos. Procesamos las solicitudes de eliminación de acuerdo con las normativas de protección de datos aplicables, sujeto a los períodos de retención legalmente requeridos.",

    "faq_q4": "¿Está segura mi información de pago?",
    "faq_a4": "No almacenamos datos de tarjetas de crédito. Todo el procesamiento de pagos es gestionado por PayTR, un proveedor de pago conforme con PCI. Los datos de transacción se tokenizan y cifran.",

    "faq_q5": "¿NoryaAI comparte datos con terceros?",
    "faq_a5": "Sus datos de salud no se comparten con terceros con fines publicitarios o de marketing. Trabajamos con proveedores de servicios (alojamiento, pagos) según sea necesario para prestar el servicio, como se describe en nuestra Política de Privacidad.",

    # BOTTOM CTA
    "cta_title_1": "Comience su recorrido",
    "cta_title_2": "de salud seguro",
    "cta_desc": "Suba sus resultados de laboratorio y obtenga información de salud clara y educativa — con privacidad y seguridad integradas.",
    "cta_primary": "Comenzar",
    "cta_secondary": "Contáctenos",

    # NAV
    "nav_analysis": "Análisis",
    "nav_science": "Ciencia",
    "nav_about": "Acerca de",
    "nav_security": "Seguridad",
    "nav_pricing": "Precios",
    "nav_get_started": "Comenzar",
    "nav_menu": "Menú",

    # FOOTER
    "footer_platform": "Plataforma",
    "footer_biomarkers": "Biomarcadores",
    "footer_science": "Ciencia",
    "footer_reports": "Informes",
    "footer_trust_legal": "Confianza y Legal",
    "footer_privacy_policy": "Política de privacidad",
    "footer_terms": "Condiciones de uso",
    "footer_security": "Seguridad",
    "footer_gdpr_kvkk": "RGPD y KVKK",
    "footer_trust_center": "Centro de confianza",
    "footer_contact_heading": "Contacto",
    "footer_support": "Soporte",
    "footer_security_inquiries": "Consultas de seguridad",
    "footer_enterprise": "Empresarial",
    "footer_copyright": "© 2025 NoryaAI. Tecnología sanitaria responsable.",
    "footer_tagline": "Explicaciones de análisis de sangre con IA en lenguaje claro. No sustituye el consejo médico.",

    # SEO INTERNAL LINKS
    "seo_explore": "Explorar",
}

# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------

_SECURITY_IT = {
    # META
    "meta_title": "Sicurezza e Privacy | NoryaAI",
    "meta_description": "Come NoryaAI protegge i tuoi dati sanitari: trasmissione crittografata, accesso controllato, architettura attenta alla privacy e limiti responsabili del prodotto.",

    # HERO
    "hero_badge": "Sicurezza e Privacy",
    "hero_title_1": "Infrastruttura attenta",
    "hero_title_2": "alla privacy.",
    "hero_desc": "NoryaAI è costruito con privacy e sicurezza al centro. I tuoi dati sanitari sono gestiti con cura — crittografati in transito, elaborati con controlli di accesso e mai venduti a terzi.",
    "hero_cta_primary": "Avvia l'analisi",
    "hero_cta_secondary": "Scopri di più",
    "hero_chip_encrypted": "Trasmissione crittografata",
    "hero_chip_privacy": "Focus sulla privacy",
    "hero_chip_responsible": "IA responsabile",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "Standard di crittografia",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "Crittografia in transito",
    "metric_3_value": "9+",
    "metric_3_label": "Lingue supportate",
    "metric_4_value": "0",
    "metric_4_label": "Dati venduti a terzi",

    # OVERVIEW SECTION
    "overview_badge": "Panoramica sulla sicurezza",
    "overview_title_1": "Come proteggiamo",
    "overview_title_2": "i tuoi dati",
    "overview_desc": "Più livelli di sicurezza lavorano insieme per proteggere le tue informazioni sanitarie durante tutto il loro ciclo di vita.",

    # 6 OVERVIEW CARDS
    "card_1_title": "Trasmissione crittografata",
    "card_1_desc": "Tutti i dati vengono trasmessi tramite connessioni crittografate TLS. I file caricati e i report generati sono protetti durante il trasferimento tra il tuo dispositivo e i nostri server.",
    "card_1_tag": "Crittografia TLS",

    "card_2_title": "Accesso controllato",
    "card_2_desc": "L'accesso ai dati degli utenti è limitato tramite controlli di autenticazione e permessi basati sui ruoli. L'accesso amministrativo segue il principio del minimo privilegio.",
    "card_2_tag": "Controlli di accesso",

    "card_3_title": "Gestione sicura dei pagamenti",
    "card_3_desc": "L'elaborazione dei pagamenti è gestita da fornitori conformi PCI. I dati delle carte di credito non vengono mai memorizzati sui server NoryaAI.",
    "card_3_tag": "Fornitore PCI",

    "card_4_title": "Architettura attenta alla privacy",
    "card_4_desc": "Seguiamo i principi di minimizzazione dei dati — raccogliendo solo ciò che è necessario per fornire il servizio. I dati sanitari non vengono utilizzati per scopi pubblicitari né venduti a terzi.",
    "card_4_tag": "Minimizzazione dei dati",

    "card_5_title": "Prodotto multilingue",
    "card_5_desc": "Report e analisi sono disponibili in oltre 9 lingue con controlli di qualità uniformi, garantendo la stessa presentazione responsabile in tutte le aree supportate.",
    "card_5_tag": "9+ lingue",

    "card_6_title": "Limiti responsabili del prodotto",
    "card_6_desc": "NoryaAI è uno strumento educativo di tecnologia sanitaria. Non fornisce diagnosi mediche, non sostituisce il giudizio clinico e non offre indicazioni di emergenza.",
    "card_6_tag": "Strumento educativo",

    # DATA FLOW SECTION
    "data_badge": "Flusso dei dati",
    "data_title_1": "Come vengono gestiti",
    "data_title_2": "i tuoi dati",
    "data_desc": "Una panoramica di come le informazioni fluiscono attraverso la piattaforma NoryaAI — dal caricamento alla consegna del report.",

    "step_1_title": "Caricamento",
    "step_1_desc": "Risultati di laboratorio caricati tramite connessioni crittografate",
    "step_2_title": "Elaborazione",
    "step_2_desc": "Analisi IA con controlli di accesso e isolamento dei dati",
    "step_3_title": "Report",
    "step_3_desc": "Report strutturato creato nella lingua scelta",
    "step_4_title": "Consegna",
    "step_4_desc": "Report consegnato solo agli utenti autenticati",

    # DATA RIGHTS SECTION
    "rights_badge": "I tuoi diritti sui dati",
    "rights_title_1": "I tuoi dati,",
    "rights_title_2": "il tuo controllo",
    "rights_desc": "Forniamo strumenti e processi per aiutarti a gestire i tuoi dati personali in conformità con le normative applicabili.",

    "right_1_title": "Cancellazione dei dati",
    "right_1_desc": "Puoi richiedere la cancellazione del tuo account e dei dati associati. Su richiesta, i dati vengono rimossi in conformità con le normative sulla protezione dei dati applicabili e i periodi di conservazione legalmente previsti.",
    "right_1_link": "Scopri di più",

    "right_2_title": "Accesso e portabilità",
    "right_2_desc": "Hai il diritto di accedere ai dati personali che conserviamo su di te e di richiederli in un formato portabile, nel rispetto delle normative applicabili.",
    "right_2_link": "Dettagli sulla privacy",

    "right_3_title": "Limitazione delle finalità",
    "right_3_desc": "I tuoi dati sanitari vengono utilizzati esclusivamente per fornire il servizio di analisi richiesto. Non vengono utilizzati per pubblicità, profilazione né venduti a terzi.",
    "right_3_link": "Informativa sulla privacy",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "Garanzie operative",
    "ops_title_1": "Controlli di accesso",
    "ops_title_2": "e sicurezza",

    "ops_1_title": "Gestione degli accessi",
    "ops_1_desc": "I sistemi di produzione utilizzano controlli di accesso basati sui ruoli. L'accesso amministrativo è limitato al personale autorizzato e segue il principio del minimo privilegio.",

    "ops_2_title": "Sicurezza dell'infrastruttura",
    "ops_2_desc": "La piattaforma utilizza Cloudflare per la sicurezza perimetrale e la protezione DDoS. L'infrastruttura applicativa segue pratiche standard di hardening della sicurezza.",

    "ops_3_title": "Registrazione e monitoraggio",
    "ops_3_desc": "Le attività del sistema vengono registrate per finalità di sicurezza e operative. Il monitoraggio aiuta a rilevare e rispondere a potenziali problemi.",

    "ops_4_title": "Sicurezza dei pagamenti",
    "ops_4_desc": "Tutta l'elaborazione dei pagamenti è gestita da PayTR, un fornitore di pagamento conforme PCI. NoryaAI non memorizza i dati delle carte di credito.",

    # REGULATORY APPROACH
    "reg_badge": "Approccio normativo",
    "reg_title_1": "Il nostro approccio alla",
    "reg_title_2": "protezione dei dati",
    "reg_desc": "NoryaAI segue principi di protezione dei dati allineati alle normative applicabili nelle regioni in cui operiamo.",

    "reg_1_title": "Allineamento GDPR",
    "reg_1_subtitle": "Protezione dei dati europea",
    "reg_1_desc": "Seguiamo i principi del GDPR, inclusa la minimizzazione dei dati, la limitazione delle finalità e la privacy by design. Gli utenti hanno il diritto di accedere, rettificare e richiedere la cancellazione dei propri dati personali.",
    "reg_1_chip1": "Privacy by Design",
    "reg_1_chip2": "Diritti sui dati",
    "reg_1_chip3": "Portabilità dei dati",

    "reg_2_title": "Allineamento KVKK",
    "reg_2_subtitle": "Protezione dei dati turca",
    "reg_2_desc": "In qualità di azienda operante in Turchia, rispettiamo i requisiti della Legge turca sulla protezione dei dati personali (KVKK), inclusi i protocolli di consenso e gli obblighi del titolare del trattamento.",
    "reg_2_chip1": "Protocolli di consenso",
    "reg_2_chip2": "Titolare del trattamento",
    "reg_2_chip3": "Cancellazione dei dati",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "Uso responsabile",
    "limits_title": "Limitazioni importanti",
    "limits_desc": "NoryaAI è progettato come strumento educativo di tecnologia sanitaria. Comprendere i suoi limiti è importante per un uso sicuro e responsabile.",

    "limit_1_title": "Non è una diagnosi medica",
    "limit_1_desc": "NoryaAI fornisce spiegazioni educative sui valori di laboratorio. Non diagnostica patologie, non prescrive trattamenti e non sostituisce una valutazione medica professionale.",

    "limit_2_title": "Non è una guida di emergenza",
    "limit_2_desc": "Questa piattaforma non è progettata per situazioni urgenti o di emergenza. In caso di emergenza medica, contatta immediatamente i servizi di emergenza locali.",

    "limit_3_title": "Consulta il tuo medico",
    "limit_3_desc": "Discuti sempre i tuoi risultati di laboratorio con un professionista sanitario qualificato prima di prendere decisioni relative alla salute.",

    # TRUST FRAMEWORK
    "trust_badge": "Quadro di fiducia",
    "trust_title": "Esplora il nostro quadro di fiducia",
    "trust_1_title": "Metodologia",
    "trust_1_desc": "Come interpretiamo i risultati delle analisi del sangue",
    "trust_2_title": "Revisione medica",
    "trust_2_desc": "Supervisione clinica e sicurezza",
    "trust_3_title": "Informativa sulla privacy",
    "trust_3_desc": "Come gestiamo i tuoi dati personali",
    "trust_4_title": "Trasparenza",
    "trust_4_desc": "Come definiamo e presentiamo le nostre affermazioni",
    "trust_5_title": "Condizioni d'uso",
    "trust_5_desc": "Termini del servizio e responsabilità",
    "trust_6_title": "Centro di fiducia",
    "trust_6_desc": "Il nostro quadro di fiducia completo",

    # PROCUREMENT CTA
    "procurement_badge": "Per le organizzazioni",
    "procurement_title": "Stai valutando NoryaAI per la tua organizzazione?",
    "procurement_desc": "Scopri di più sulla nostra metodologia, pratiche di privacy, processo di revisione medica e quadro di utilizzo responsabile.",
    "procurement_cta_1": "Informazioni aziendali",
    "procurement_cta_2": "Contattaci",
    "procurement_cta_3": "Vedi metodologia",

    # FAQ
    "faq_badge": "FAQ",
    "faq_title_1": "Domande sulla",
    "faq_title_2": "sicurezza",

    "faq_q1": "Come vengono protetti i miei dati sanitari?",
    "faq_a1": "Tutti i dati vengono trasmessi tramite connessioni crittografate TLS. I risultati di laboratorio caricati vengono elaborati con controlli di accesso e i report vengono consegnati solo agli utenti autenticati. Seguiamo i principi di minimizzazione dei dati e non vendiamo dati sanitari a terzi.",

    "faq_q2": "Il personale di NoryaAI può vedere i miei risultati di laboratorio?",
    "faq_a2": "L'accesso ai dati degli utenti è limitato tramite controlli basati sui ruoli. Il nostro team accede ai dati degli utenti solo quando necessario per il supporto tecnico o la manutenzione del sistema, e solo nella misura strettamente necessaria.",

    "faq_q3": "Come posso cancellare i miei dati?",
    "faq_a3": "Puoi richiedere la cancellazione del tuo account e dei dati associati in qualsiasi momento contattandoci. Elaboriamo le richieste di cancellazione in conformità con le normative sulla protezione dei dati applicabili, nel rispetto dei periodi di conservazione legalmente previsti.",

    "faq_q4": "Le mie informazioni di pagamento sono sicure?",
    "faq_a4": "Non memorizziamo i dati delle carte di credito. Tutta l'elaborazione dei pagamenti è gestita da PayTR, un fornitore di pagamento conforme PCI. I dati delle transazioni vengono tokenizzati e crittografati.",

    "faq_q5": "NoryaAI condivide dati con terzi?",
    "faq_a5": "I tuoi dati sanitari non vengono condivisi con terzi per scopi pubblicitari o di marketing. Collaboriamo con fornitori di servizi (hosting, pagamenti) nella misura necessaria per erogare il servizio, come descritto nella nostra Informativa sulla privacy.",

    # BOTTOM CTA
    "cta_title_1": "Inizia il tuo percorso",
    "cta_title_2": "salute sicuro",
    "cta_desc": "Carica i tuoi risultati di laboratorio e ottieni informazioni sanitarie chiare ed educative — con privacy e sicurezza integrate.",
    "cta_primary": "Inizia ora",
    "cta_secondary": "Contattaci",

    # NAV
    "nav_analysis": "Analisi",
    "nav_science": "Scienza",
    "nav_about": "Chi siamo",
    "nav_security": "Sicurezza",
    "nav_pricing": "Prezzi",
    "nav_get_started": "Inizia ora",
    "nav_menu": "Menu",

    # FOOTER
    "footer_platform": "Piattaforma",
    "footer_biomarkers": "Biomarcatori",
    "footer_science": "Scienza",
    "footer_reports": "Report",
    "footer_trust_legal": "Fiducia e Legale",
    "footer_privacy_policy": "Informativa sulla privacy",
    "footer_terms": "Condizioni d'uso",
    "footer_security": "Sicurezza",
    "footer_gdpr_kvkk": "GDPR e KVKK",
    "footer_trust_center": "Centro di fiducia",
    "footer_contact_heading": "Contatti",
    "footer_support": "Supporto",
    "footer_security_inquiries": "Richieste di sicurezza",
    "footer_enterprise": "Aziendale",
    "footer_copyright": "© 2025 NoryaAI. Tecnologia sanitaria responsabile.",
    "footer_tagline": "Spiegazioni delle analisi del sangue con IA in linguaggio chiaro. Non sostituisce il parere medico.",

    # SEO INTERNAL LINKS
    "seo_explore": "Esplora",
}

# ---------------------------------------------------------------------------
# HEBREW (RTL)
# ---------------------------------------------------------------------------

_SECURITY_HE = {
    # META
    "meta_title": "אבטחה ופרטיות | NoryaAI",
    "meta_description": "כיצד NoryaAI מגן על נתוני הבריאות שלך: העברה מוצפנת, גישה מבוקרת, ארכיטקטורה מודעת לפרטיות וגבולות מוצר אחראיים.",

    # HERO
    "hero_badge": "אבטחה ופרטיות",
    "hero_title_1": "תשתית מודעת",
    "hero_title_2": "לפרטיות.",
    "hero_desc": "NoryaAI נבנה עם פרטיות ואבטחה כעקרונות יסוד. נתוני הבריאות שלך מטופלים בקפידה — מוצפנים בהעברה, מעובדים עם בקרות גישה ולעולם אינם נמכרים לצדדים שלישיים.",
    "hero_cta_primary": "התחל ניתוח",
    "hero_cta_secondary": "למד עוד",
    "hero_chip_encrypted": "העברה מוצפנת",
    "hero_chip_privacy": "מוכוון פרטיות",
    "hero_chip_responsible": "בינה מלאכותית אחראית",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "תקן הצפנה",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "הצפנת העברה",
    "metric_3_value": "9+",
    "metric_3_label": "שפות נתמכות",
    "metric_4_value": "0",
    "metric_4_label": "נתונים שנמכרו לצדדים שלישיים",

    # OVERVIEW SECTION
    "overview_badge": "סקירת אבטחה",
    "overview_title_1": "כיצד אנו מגנים",
    "overview_title_2": "על הנתונים שלך",
    "overview_desc": "שכבות אבטחה מרובות פועלות יחד כדי להגן על המידע הבריאותי שלך לאורך כל מחזור החיים שלו.",

    # 6 OVERVIEW CARDS
    "card_1_title": "העברה מוצפנת",
    "card_1_desc": "כל הנתונים מועברים דרך חיבורים מוצפנים ב-TLS. קבצים שהועלו ודוחות שנוצרו מוגנים במהלך ההעברה בין המכשיר שלך לשרתים שלנו.",
    "card_1_tag": "הצפנת TLS",

    "card_2_title": "גישה מבוקרת",
    "card_2_desc": "הגישה לנתוני המשתמשים מוגבלת באמצעות בקרות אימות והרשאות מבוססות תפקידים. גישה ניהולית פועלת לפי עקרון ההרשאה המינימלית.",
    "card_2_tag": "בקרות גישה",

    "card_3_title": "עיבוד תשלומים מאובטח",
    "card_3_desc": "עיבוד התשלומים מבוצע על ידי ספקי תשלום התואמים ל-PCI. פרטי כרטיסי אשראי אינם נשמרים לעולם על שרתי NoryaAI.",
    "card_3_tag": "ספק PCI",

    "card_4_title": "ארכיטקטורה מודעת לפרטיות",
    "card_4_desc": "אנו פועלים לפי עקרונות מזעור נתונים — אוספים רק את הנדרש לצורך מתן השירות. נתוני בריאות אינם משמשים לפרסום ואינם נמכרים לצדדים שלישיים.",
    "card_4_tag": "מזעור נתונים",

    "card_5_title": "מוצר רב-לשוני",
    "card_5_desc": "דוחות וניתוחים זמינים ביותר מ-9 שפות עם בקרות איכות עקביות, להבטחת אותה הצגה אחראית בכל האזורים הנתמכים.",
    "card_5_tag": "9+ שפות",

    "card_6_title": "גבולות מוצר אחראיים",
    "card_6_desc": "NoryaAI הוא כלי חינוכי בתחום טכנולוגיית הבריאות. הוא אינו מספק אבחנות רפואיות, אינו מחליף שיקול דעת קליני ואינו מציע הנחיות חירום.",
    "card_6_tag": "כלי חינוכי",

    # DATA FLOW SECTION
    "data_badge": "זרימת נתונים",
    "data_title_1": "כיצד הנתונים שלך",
    "data_title_2": "מטופלים",
    "data_desc": "סקירה כללית של אופן זרימת המידע דרך פלטפורמת NoryaAI — מההעלאה ועד מסירת הדוח.",

    "step_1_title": "העלאה",
    "step_1_desc": "תוצאות מעבדה מועלות דרך חיבורים מוצפנים",
    "step_2_title": "עיבוד",
    "step_2_desc": "ניתוח בינה מלאכותית עם בקרות גישה ובידוד נתונים",
    "step_3_title": "דוח",
    "step_3_desc": "דוח מובנה נוצר בשפה שבחרת",
    "step_4_title": "מסירה",
    "step_4_desc": "הדוח מועבר למשתמשים מאומתים בלבד",

    # DATA RIGHTS SECTION
    "rights_badge": "הזכויות שלך על הנתונים",
    "rights_title_1": "הנתונים שלך,",
    "rights_title_2": "השליטה שלך",
    "rights_desc": "אנו מספקים כלים ותהליכים שיעזרו לך לנהל את הנתונים האישיים שלך בהתאם לתקנות החלות.",

    "right_1_title": "מחיקת נתונים",
    "right_1_desc": "ניתן לבקש מחיקת החשבון והנתונים המשויכים אליו. על פי בקשה, הנתונים מוסרים בהתאם לתקנות הגנת הנתונים החלות ותקופות השמירה החוקיות.",
    "right_1_link": "למד עוד",

    "right_2_title": "גישה וניידות",
    "right_2_desc": "יש לך זכות לגשת לנתונים האישיים שאנו מחזיקים עליך ולבקש אותם בפורמט נייד, בכפוף לתקנות החלות.",
    "right_2_link": "פרטי פרטיות",

    "right_3_title": "הגבלת מטרה",
    "right_3_desc": "נתוני הבריאות שלך משמשים אך ורק לצורך מתן שירות הניתוח שביקשת. הם אינם משמשים לפרסום, ליצירת פרופיל או למכירה לצדדים שלישיים.",
    "right_3_link": "מדיניות פרטיות",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "אמצעי הגנה תפעוליים",
    "ops_title_1": "בקרות גישה",
    "ops_title_2": "ואבטחה",

    "ops_1_title": "ניהול גישה",
    "ops_1_desc": "מערכות הייצור משתמשות בבקרות גישה מבוססות תפקידים. גישה ניהולית מוגבלת לצוות מורשה ופועלת לפי עקרון ההרשאה המינימלית.",

    "ops_2_title": "אבטחת תשתית",
    "ops_2_desc": "הפלטפורמה משתמשת ב-Cloudflare לאבטחת קצה והגנה מפני DDoS. תשתית האפליקציה פועלת בהתאם לנהלי חיזוק אבטחה סטנדרטיים.",

    "ops_3_title": "רישום ומעקב",
    "ops_3_desc": "פעילות המערכת נרשמת למטרות אבטחה ותפעול. המעקב מסייע באיתור מוקדם ובתגובה לבעיות פוטנציאליות.",

    "ops_4_title": "אבטחת תשלומים",
    "ops_4_desc": "כל עיבוד התשלומים מבוצע על ידי PayTR, ספק תשלום התואם ל-PCI. NoryaAI אינו שומר פרטי כרטיסי אשראי.",

    # REGULATORY APPROACH
    "reg_badge": "גישה רגולטורית",
    "reg_title_1": "הגישה שלנו להגנת",
    "reg_title_2": "נתונים",
    "reg_desc": "NoryaAI פועל לפי עקרונות הגנת נתונים המתואמים עם התקנות החלות באזורים שבהם אנו פועלים.",

    "reg_1_title": "התאמה ל-GDPR",
    "reg_1_subtitle": "הגנת נתונים אירופית",
    "reg_1_desc": "אנו פועלים לפי עקרונות ה-GDPR הכוללים מזעור נתונים, הגבלת מטרה ופרטיות מובנית בתכנון. למשתמשים יש זכות לגשת לנתונים האישיים שלהם, לתקנם ולבקש את מחיקתם.",
    "reg_1_chip1": "פרטיות מובנית בתכנון",
    "reg_1_chip2": "זכויות נתונים",
    "reg_1_chip3": "ניידות נתונים",

    "reg_2_title": "התאמה ל-KVKK",
    "reg_2_subtitle": "הגנת נתונים טורקית",
    "reg_2_desc": "כחברה הפועלת בטורקיה, אנו מקפידים על דרישות חוק הגנת הנתונים האישיים של טורקיה (KVKK), לרבות פרוטוקולי הסכמה וחובות בקר הנתונים.",
    "reg_2_chip1": "פרוטוקולי הסכמה",
    "reg_2_chip2": "בקר נתונים",
    "reg_2_chip3": "מחיקת נתונים",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "שימוש אחראי",
    "limits_title": "מגבלות חשובות",
    "limits_desc": "NoryaAI תוכנן ככלי חינוכי בתחום טכנולוגיית הבריאות. הבנת גבולותיו חשובה לשימוש בטוח ואחראי.",

    "limit_1_title": "אינו אבחנה רפואית",
    "limit_1_desc": "NoryaAI מספק הסברים חינוכיים על ערכי מעבדה. הוא אינו מאבחן מצבים רפואיים, אינו רושם טיפולים ואינו מחליף הערכה רפואית מקצועית.",

    "limit_2_title": "אינו הנחיית חירום",
    "limit_2_desc": "פלטפורמה זו אינה מיועדת למצבי חירום או דחיפות. במקרה של חירום רפואי, פנה מיד לשירותי החירום המקומיים.",

    "limit_3_title": "התייעץ עם הרופא שלך",
    "limit_3_desc": "תמיד דון בתוצאות המעבדה שלך עם איש מקצוע רפואי מוסמך לפני קבלת החלטות הקשורות לבריאות.",

    # TRUST FRAMEWORK
    "trust_badge": "מסגרת אמון",
    "trust_title": "גלה את מסגרת האמון שלנו",
    "trust_1_title": "מתודולוגיה",
    "trust_1_desc": "כיצד אנו מפרשים תוצאות בדיקות דם",
    "trust_2_title": "בדיקה רפואית",
    "trust_2_desc": "פיקוח קליני ובטיחות",
    "trust_3_title": "מדיניות פרטיות",
    "trust_3_desc": "כיצד אנו מטפלים בנתונים האישיים שלך",
    "trust_4_title": "שקיפות",
    "trust_4_desc": "כיצד אנו מגדירים ומציגים טענות",
    "trust_5_title": "תנאי שימוש",
    "trust_5_desc": "תנאי השירות והאחריות",
    "trust_6_title": "מרכז אמון",
    "trust_6_desc": "מסגרת האמון המלאה שלנו",

    # PROCUREMENT CTA
    "procurement_badge": "לארגונים",
    "procurement_title": "מעריכים את NoryaAI עבור הארגון שלכם?",
    "procurement_desc": "למדו עוד על המתודולוגיה, נהלי הפרטיות, תהליך הבדיקה הרפואית ומסגרת השימוש האחראי שלנו.",
    "procurement_cta_1": "מידע לארגונים",
    "procurement_cta_2": "צרו קשר",
    "procurement_cta_3": "צפה במתודולוגיה",

    # FAQ
    "faq_badge": "שאלות נפוצות",
    "faq_title_1": "שאלות",
    "faq_title_2": "אבטחה",

    "faq_q1": "כיצד מוגנים נתוני הבריאות שלי?",
    "faq_a1": "כל הנתונים מועברים דרך חיבורים מוצפנים ב-TLS. תוצאות מעבדה שהועלו מעובדות עם בקרות גישה, ודוחות מועברים רק למשתמשים מאומתים. אנו פועלים לפי עקרונות מזעור נתונים ואיננו מוכרים נתוני בריאות לצדדים שלישיים.",

    "faq_q2": "האם צוות NoryaAI יכול לראות את תוצאות המעבדה שלי?",
    "faq_a2": "הגישה לנתוני משתמשים מוגבלת באמצעות בקרות מבוססות תפקידים. הצוות שלנו ניגש לנתוני משתמשים רק כאשר הדבר נחוץ לתמיכה טכנית או תחזוקת מערכת, ורק במידה הנדרשת לצורך כך.",

    "faq_q3": "כיצד אוכל למחוק את הנתונים שלי?",
    "faq_a3": "ניתן לבקש מחיקת החשבון והנתונים המשויכים בכל עת על ידי פנייה אלינו. אנו מעבדים בקשות מחיקה בהתאם לתקנות הגנת הנתונים החלות, בכפוף לתקופות שמירה הנדרשות בחוק.",

    "faq_q4": "האם פרטי התשלום שלי מאובטחים?",
    "faq_a4": "איננו שומרים פרטי כרטיסי אשראי. כל עיבוד התשלומים מבוצע על ידי PayTR, ספק תשלום התואם ל-PCI. נתוני העסקאות עוברים טוקניזציה והצפנה.",

    "faq_q5": "האם NoryaAI משתף נתונים עם צדדים שלישיים?",
    "faq_a5": "נתוני הבריאות שלך אינם משותפים עם צדדים שלישיים למטרות פרסום או שיווק. אנו עובדים עם ספקי שירות (אירוח, תשלומים) לפי הצורך לצורך מתן השירות, כמתואר במדיניות הפרטיות שלנו.",

    # BOTTOM CTA
    "cta_title_1": "התחל את מסע",
    "cta_title_2": "הבריאות המאובטח שלך",
    "cta_desc": "העלה את תוצאות המעבדה שלך וקבל תובנות בריאותיות ברורות וחינוכיות — עם פרטיות ואבטחה מובנות.",
    "cta_primary": "התחל עכשיו",
    "cta_secondary": "צור קשר",

    # NAV
    "nav_analysis": "ניתוח",
    "nav_science": "מדע",
    "nav_about": "אודות",
    "nav_security": "אבטחה",
    "nav_pricing": "תמחור",
    "nav_get_started": "התחל עכשיו",
    "nav_menu": "תפריט",

    # FOOTER
    "footer_platform": "פלטפורמה",
    "footer_biomarkers": "סמנים ביולוגיים",
    "footer_science": "מדע",
    "footer_reports": "דוחות",
    "footer_trust_legal": "אמון ומשפט",
    "footer_privacy_policy": "מדיניות פרטיות",
    "footer_terms": "תנאי שימוש",
    "footer_security": "אבטחה",
    "footer_gdpr_kvkk": "GDPR ו-KVKK",
    "footer_trust_center": "מרכז אמון",
    "footer_contact_heading": "יצירת קשר",
    "footer_support": "תמיכה",
    "footer_security_inquiries": "פניות אבטחה",
    "footer_enterprise": "ארגוני",
    "footer_copyright": "© 2025 NoryaAI. טכנולוגיית בריאות אחראית.",
    "footer_tagline": "הסברי בדיקות דם מונעי בינה מלאכותית בשפה פשוטה. אינו תחליף לייעוץ רפואי.",

    # SEO INTERNAL LINKS
    "seo_explore": "גלה",
}

# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------

_SECURITY_HI = {
    # META
    "meta_title": "सुरक्षा और गोपनीयता | NoryaAI",
    "meta_description": "NoryaAI आपके स्वास्थ्य डेटा की सुरक्षा कैसे करता है: एन्क्रिप्टेड ट्रांसमिशन, नियंत्रित एक्सेस, गोपनीयता-सचेत आर्किटेक्चर और जिम्मेदार उत्पाद सीमाएँ।",

    # HERO
    "hero_badge": "सुरक्षा और गोपनीयता",
    "hero_title_1": "गोपनीयता-सचेत",
    "hero_title_2": "इन्फ्रास्ट्रक्चर।",
    "hero_desc": "NoryaAI गोपनीयता और सुरक्षा को अपने मूल में रखकर बनाया गया है। आपका स्वास्थ्य डेटा सावधानी से संभाला जाता है — ट्रांज़िट में एन्क्रिप्टेड, एक्सेस नियंत्रणों के साथ प्रोसेस किया जाता है और कभी भी तृतीय पक्षों को नहीं बेचा जाता।",
    "hero_cta_primary": "विश्लेषण शुरू करें",
    "hero_cta_secondary": "और जानें",
    "hero_chip_encrypted": "एन्क्रिप्टेड ट्रांसमिशन",
    "hero_chip_privacy": "गोपनीयता-केंद्रित",
    "hero_chip_responsible": "जिम्मेदार AI",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "एन्क्रिप्शन मानक",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "ट्रांज़िट एन्क्रिप्शन",
    "metric_3_value": "9+",
    "metric_3_label": "समर्थित भाषाएँ",
    "metric_4_value": "0",
    "metric_4_label": "तृतीय पक्षों को बेचा गया डेटा",

    # OVERVIEW SECTION
    "overview_badge": "सुरक्षा अवलोकन",
    "overview_title_1": "हम आपके डेटा की",
    "overview_title_2": "सुरक्षा कैसे करते हैं",
    "overview_desc": "सुरक्षा की कई परतें आपकी स्वास्थ्य जानकारी को उसके पूरे जीवनचक्र में सुरक्षित रखने के लिए मिलकर काम करती हैं।",

    # 6 OVERVIEW CARDS
    "card_1_title": "एन्क्रिप्टेड ट्रांसमिशन",
    "card_1_desc": "सभी डेटा TLS-एन्क्रिप्टेड कनेक्शन के माध्यम से प्रेषित किया जाता है। अपलोड की गई फ़ाइलें और जनरेट की गई रिपोर्ट आपके डिवाइस और हमारे सर्वर के बीच ट्रांसफर के दौरान सुरक्षित रहती हैं।",
    "card_1_tag": "TLS एन्क्रिप्टेड",

    "card_2_title": "नियंत्रित एक्सेस",
    "card_2_desc": "उपयोगकर्ता डेटा तक पहुँच प्रमाणीकरण नियंत्रणों और भूमिका-आधारित अनुमतियों द्वारा प्रतिबंधित है। प्रशासनिक एक्सेस न्यूनतम विशेषाधिकार सिद्धांतों का पालन करता है।",
    "card_2_tag": "एक्सेस नियंत्रण",

    "card_3_title": "सुरक्षित भुगतान प्रबंधन",
    "card_3_desc": "भुगतान प्रोसेसिंग PCI-अनुपालक भुगतान प्रदाताओं द्वारा की जाती है। क्रेडिट कार्ड विवरण NoryaAI सर्वर पर कभी संग्रहीत नहीं किए जाते।",
    "card_3_tag": "PCI प्रदाता",

    "card_4_title": "गोपनीयता-सचेत आर्किटेक्चर",
    "card_4_desc": "हम डेटा न्यूनीकरण सिद्धांतों का पालन करते हैं — केवल सेवा प्रदान करने के लिए आवश्यक डेटा एकत्र करते हैं। स्वास्थ्य डेटा विज्ञापन के लिए उपयोग नहीं किया जाता या तृतीय पक्षों को नहीं बेचा जाता।",
    "card_4_tag": "डेटा न्यूनीकरण",

    "card_5_title": "बहुभाषी उत्पाद",
    "card_5_desc": "रिपोर्ट और विश्लेषण सुसंगत गुणवत्ता नियंत्रणों के साथ 9 से अधिक भाषाओं में उपलब्ध हैं, जो सभी समर्थित क्षेत्रों में समान जिम्मेदार प्रस्तुति सुनिश्चित करते हैं।",
    "card_5_tag": "9+ भाषाएँ",

    "card_6_title": "जिम्मेदार उत्पाद सीमाएँ",
    "card_6_desc": "NoryaAI एक शैक्षिक स्वास्थ्य प्रौद्योगिकी उपकरण है। यह चिकित्सा निदान प्रदान नहीं करता, चिकित्सक के निर्णय का स्थान नहीं लेता, या आपातकालीन मार्गदर्शन नहीं देता।",
    "card_6_tag": "शैक्षिक उपकरण",

    # DATA FLOW SECTION
    "data_badge": "डेटा प्रवाह",
    "data_title_1": "आपका डेटा कैसे",
    "data_title_2": "संभाला जाता है",
    "data_desc": "NoryaAI प्लेटफ़ॉर्म के माध्यम से जानकारी कैसे प्रवाहित होती है, इसका उच्च-स्तरीय अवलोकन — अपलोड से लेकर रिपोर्ट डिलीवरी तक।",

    "step_1_title": "अपलोड",
    "step_1_desc": "लैब परिणाम एन्क्रिप्टेड कनेक्शन के माध्यम से अपलोड किए जाते हैं",
    "step_2_title": "प्रोसेसिंग",
    "step_2_desc": "एक्सेस नियंत्रण और डेटा अलगाव के साथ AI विश्लेषण",
    "step_3_title": "रिपोर्ट",
    "step_3_desc": "आपकी चुनी हुई भाषा में संरचित रिपोर्ट बनाई जाती है",
    "step_4_title": "डिलीवरी",
    "step_4_desc": "रिपोर्ट केवल प्रमाणित उपयोगकर्ताओं को डिलीवर की जाती है",

    # DATA RIGHTS SECTION
    "rights_badge": "आपके डेटा अधिकार",
    "rights_title_1": "आपका डेटा,",
    "rights_title_2": "आपका नियंत्रण",
    "rights_desc": "हम आपको लागू नियमों के अनुसार अपने व्यक्तिगत डेटा को प्रबंधित करने में मदद करने के लिए उपकरण और प्रक्रियाएँ प्रदान करते हैं।",

    "right_1_title": "डेटा विलोपन",
    "right_1_desc": "आप अपने खाते और संबंधित डेटा के विलोपन का अनुरोध कर सकते हैं। अनुरोध पर, डेटा लागू डेटा सुरक्षा नियमों और किसी भी आवश्यक कानूनी प्रतिधारण अवधि के अनुसार हटा दिया जाता है।",
    "right_1_link": "और जानें",

    "right_2_title": "एक्सेस और पोर्टेबिलिटी",
    "right_2_desc": "आपको हमारे पास रखे आपके व्यक्तिगत डेटा तक पहुँचने और उसे पोर्टेबल प्रारूप में अनुरोध करने का अधिकार है, जो लागू नियमों के अधीन है।",
    "right_2_link": "गोपनीयता विवरण",

    "right_3_title": "उद्देश्य सीमा",
    "right_3_desc": "आपका स्वास्थ्य डेटा केवल आपके द्वारा अनुरोधित विश्लेषण सेवा प्रदान करने के लिए उपयोग किया जाता है। इसका उपयोग विज्ञापन, प्रोफाइलिंग के लिए नहीं किया जाता या तृतीय पक्षों को नहीं बेचा जाता।",
    "right_3_link": "गोपनीयता नीति",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "परिचालन सुरक्षा उपाय",
    "ops_title_1": "एक्सेस और",
    "ops_title_2": "सुरक्षा नियंत्रण",

    "ops_1_title": "एक्सेस प्रबंधन",
    "ops_1_desc": "प्रोडक्शन सिस्टम भूमिका-आधारित एक्सेस नियंत्रण का उपयोग करते हैं। प्रशासनिक एक्सेस अधिकृत कर्मियों तक सीमित है और न्यूनतम विशेषाधिकार सिद्धांतों का पालन करता है।",

    "ops_2_title": "इन्फ्रास्ट्रक्चर सुरक्षा",
    "ops_2_desc": "प्लेटफ़ॉर्म एज सुरक्षा और DDoS सुरक्षा के लिए Cloudflare का उपयोग करता है। एप्लिकेशन इन्फ्रास्ट्रक्चर मानक सुरक्षा हार्डनिंग प्रथाओं का पालन करता है।",

    "ops_3_title": "लॉगिंग और मॉनिटरिंग",
    "ops_3_desc": "सिस्टम गतिविधि सुरक्षा और परिचालन उद्देश्यों के लिए लॉग की जाती है। मॉनिटरिंग संभावित समस्याओं का पता लगाने और उनका जवाब देने में मदद करती है।",

    "ops_4_title": "भुगतान सुरक्षा",
    "ops_4_desc": "सभी भुगतान प्रोसेसिंग PayTR द्वारा की जाती है, जो एक PCI-अनुपालक भुगतान प्रदाता है। NoryaAI क्रेडिट कार्ड विवरण संग्रहीत नहीं करता।",

    # REGULATORY APPROACH
    "reg_badge": "नियामक दृष्टिकोण",
    "reg_title_1": "डेटा सुरक्षा के प्रति",
    "reg_title_2": "हमारा दृष्टिकोण",
    "reg_desc": "NoryaAI हमारे सेवा क्षेत्रों में लागू नियमों के अनुरूप डेटा सुरक्षा सिद्धांतों का पालन करता है।",

    "reg_1_title": "GDPR संरेखण",
    "reg_1_subtitle": "यूरोपीय डेटा सुरक्षा",
    "reg_1_desc": "हम डेटा न्यूनीकरण, उद्देश्य सीमा और डिज़ाइन द्वारा गोपनीयता सहित GDPR सिद्धांतों का पालन करते हैं। उपयोगकर्ताओं को अपने व्यक्तिगत डेटा तक पहुँचने, उसे सही करने और विलोपन का अनुरोध करने का अधिकार है।",
    "reg_1_chip1": "डिज़ाइन द्वारा गोपनीयता",
    "reg_1_chip2": "डेटा अधिकार",
    "reg_1_chip3": "डेटा पोर्टेबिलिटी",

    "reg_2_title": "KVKK संरेखण",
    "reg_2_subtitle": "तुर्की डेटा सुरक्षा",
    "reg_2_desc": "तुर्की में संचालित कंपनी के रूप में, हम तुर्की के व्यक्तिगत डेटा सुरक्षा कानून (KVKK) की आवश्यकताओं का पालन करते हैं, जिसमें सहमति प्रोटोकॉल और डेटा नियंत्रक दायित्व शामिल हैं।",
    "reg_2_chip1": "सहमति प्रोटोकॉल",
    "reg_2_chip2": "डेटा नियंत्रक",
    "reg_2_chip3": "डेटा विलोपन",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "जिम्मेदार उपयोग",
    "limits_title": "महत्वपूर्ण सीमाएँ",
    "limits_desc": "NoryaAI एक शैक्षिक स्वास्थ्य प्रौद्योगिकी उपकरण के रूप में डिज़ाइन किया गया है। इसकी सीमाओं को समझना सुरक्षित और जिम्मेदार उपयोग के लिए महत्वपूर्ण है।",

    "limit_1_title": "चिकित्सा निदान नहीं",
    "limit_1_desc": "NoryaAI लैब मूल्यों की शैक्षिक व्याख्या प्रदान करता है। यह स्थितियों का निदान नहीं करता, उपचार निर्धारित नहीं करता, या पेशेवर चिकित्सा मूल्यांकन का स्थान नहीं लेता।",

    "limit_2_title": "आपातकालीन मार्गदर्शन नहीं",
    "limit_2_desc": "यह प्लेटफ़ॉर्म तत्काल या आपातकालीन स्थितियों के लिए डिज़ाइन नहीं किया गया है। चिकित्सा आपातकाल की स्थिति में, तुरंत अपनी स्थानीय आपातकालीन सेवाओं से संपर्क करें।",

    "limit_3_title": "अपने स्वास्थ्य सेवा प्रदाता से परामर्श करें",
    "limit_3_desc": "स्वास्थ्य संबंधी निर्णय लेने से पहले हमेशा अपने लैब परिणामों पर किसी योग्य स्वास्थ्य पेशेवर से चर्चा करें।",

    # TRUST FRAMEWORK
    "trust_badge": "विश्वास ढाँचा",
    "trust_title": "हमारा विश्वास ढाँचा जानें",
    "trust_1_title": "कार्यप्रणाली",
    "trust_1_desc": "हम रक्त परीक्षण परिणामों की व्याख्या कैसे करते हैं",
    "trust_2_title": "चिकित्सा समीक्षा",
    "trust_2_desc": "चिकित्सक निगरानी और सुरक्षा",
    "trust_3_title": "गोपनीयता नीति",
    "trust_3_desc": "हम आपके व्यक्तिगत डेटा को कैसे संभालते हैं",
    "trust_4_title": "पारदर्शिता",
    "trust_4_desc": "हम दावों को कैसे परिभाषित और प्रस्तुत करते हैं",
    "trust_5_title": "उपयोग की शर्तें",
    "trust_5_desc": "सेवा शर्तें और जिम्मेदारियाँ",
    "trust_6_title": "विश्वास केंद्र",
    "trust_6_desc": "हमारा संपूर्ण विश्वास ढाँचा",

    # PROCUREMENT CTA
    "procurement_badge": "संगठनों के लिए",
    "procurement_title": "अपने संगठन के लिए NoryaAI का मूल्यांकन कर रहे हैं?",
    "procurement_desc": "हमारी कार्यप्रणाली, गोपनीयता प्रथाओं, चिकित्सा समीक्षा प्रक्रिया और जिम्मेदार उपयोग ढाँचे के बारे में अधिक जानें।",
    "procurement_cta_1": "एंटरप्राइज़ जानकारी",
    "procurement_cta_2": "हमसे संपर्क करें",
    "procurement_cta_3": "कार्यप्रणाली देखें",

    # FAQ
    "faq_badge": "अक्सर पूछे जाने वाले प्रश्न",
    "faq_title_1": "सुरक्षा",
    "faq_title_2": "प्रश्न",

    "faq_q1": "मेरे स्वास्थ्य डेटा की सुरक्षा कैसे की जाती है?",
    "faq_a1": "सभी डेटा TLS-एन्क्रिप्टेड कनेक्शन के माध्यम से प्रेषित किया जाता है। अपलोड किए गए लैब परिणाम एक्सेस नियंत्रणों के साथ प्रोसेस किए जाते हैं, और रिपोर्ट केवल प्रमाणित उपयोगकर्ताओं को डिलीवर की जाती हैं। हम डेटा न्यूनीकरण सिद्धांतों का पालन करते हैं और स्वास्थ्य डेटा तृतीय पक्षों को नहीं बेचते।",

    "faq_q2": "क्या NoryaAI कर्मचारी मेरे लैब परिणाम देख सकते हैं?",
    "faq_a2": "उपयोगकर्ता डेटा तक पहुँच भूमिका-आधारित नियंत्रणों द्वारा प्रतिबंधित है। हमारी टीम उपयोगकर्ता डेटा तक केवल तकनीकी सहायता या सिस्टम रखरखाव के लिए आवश्यक होने पर और केवल उतनी ही सीमा तक पहुँचती है।",

    "faq_q3": "मैं अपना डेटा कैसे हटा सकता हूँ?",
    "faq_a3": "आप किसी भी समय हमसे संपर्क करके अपने खाते और संबंधित डेटा के विलोपन का अनुरोध कर सकते हैं। हम लागू डेटा सुरक्षा नियमों के अनुसार विलोपन अनुरोधों को प्रोसेस करते हैं, जो किसी भी कानूनी रूप से आवश्यक प्रतिधारण अवधि के अधीन है।",

    "faq_q4": "क्या मेरी भुगतान जानकारी सुरक्षित है?",
    "faq_a4": "हम क्रेडिट कार्ड विवरण संग्रहीत नहीं करते। सभी भुगतान प्रोसेसिंग PayTR द्वारा की जाती है, जो एक PCI-अनुपालक भुगतान प्रदाता है। लेनदेन डेटा टोकनाइज़ और एन्क्रिप्ट किया जाता है।",

    "faq_q5": "क्या NoryaAI तृतीय पक्षों के साथ डेटा साझा करता है?",
    "faq_a5": "आपका स्वास्थ्य डेटा विज्ञापन या मार्केटिंग उद्देश्यों के लिए तृतीय पक्षों के साथ साझा नहीं किया जाता। हम सेवा प्रदान करने के लिए आवश्यकतानुसार सेवा प्रदाताओं (होस्टिंग, भुगतान) के साथ काम करते हैं, जैसा कि हमारी गोपनीयता नीति में वर्णित है।",

    # BOTTOM CTA
    "cta_title_1": "अपनी सुरक्षित स्वास्थ्य",
    "cta_title_2": "यात्रा शुरू करें",
    "cta_desc": "अपने लैब परिणाम अपलोड करें और गोपनीयता और सुरक्षा के साथ स्पष्ट, शैक्षिक स्वास्थ्य जानकारी प्राप्त करें।",
    "cta_primary": "शुरू करें",
    "cta_secondary": "हमसे संपर्क करें",

    # NAV
    "nav_analysis": "विश्लेषण",
    "nav_science": "विज्ञान",
    "nav_about": "हमारे बारे में",
    "nav_security": "सुरक्षा",
    "nav_pricing": "मूल्य निर्धारण",
    "nav_get_started": "शुरू करें",
    "nav_menu": "मेनू",

    # FOOTER
    "footer_platform": "प्लेटफ़ॉर्म",
    "footer_biomarkers": "बायोमार्कर",
    "footer_science": "विज्ञान",
    "footer_reports": "रिपोर्ट",
    "footer_trust_legal": "विश्वास और कानूनी",
    "footer_privacy_policy": "गोपनीयता नीति",
    "footer_terms": "उपयोग की शर्तें",
    "footer_security": "सुरक्षा",
    "footer_gdpr_kvkk": "GDPR और KVKK",
    "footer_trust_center": "विश्वास केंद्र",
    "footer_contact_heading": "संपर्क",
    "footer_support": "सहायता",
    "footer_security_inquiries": "सुरक्षा पूछताछ",
    "footer_enterprise": "एंटरप्राइज़",
    "footer_copyright": "© 2025 NoryaAI. जिम्मेदार स्वास्थ्य प्रौद्योगिकी।",
    "footer_tagline": "AI-संचालित रक्त परीक्षण व्याख्या सरल भाषा में। चिकित्सा सलाह का विकल्प नहीं।",

    # SEO INTERNAL LINKS
    "seo_explore": "खोजें",
}

# ---------------------------------------------------------------------------
# ARABIC (RTL)
# ---------------------------------------------------------------------------

_SECURITY_AR = {
    # META
    "meta_title": "الأمان والخصوصية | NoryaAI",
    "meta_description": "كيف يحمي NoryaAI بياناتك الصحية: نقل مشفّر، وصول مُتحكَّم به، بنية واعية بالخصوصية، وحدود منتج مسؤولة.",

    # HERO
    "hero_badge": "الأمان والخصوصية",
    "hero_title_1": "بنية تحتية",
    "hero_title_2": "واعية بالخصوصية.",
    "hero_desc": "بُني NoryaAI مع وضع الخصوصية والأمان في صميمه. تُعالج بياناتك الصحية بعناية — مشفّرة أثناء النقل، ومعالجة بضوابط وصول، ولا تُباع أبدًا لأطراف ثالثة.",
    "hero_cta_primary": "ابدأ التحليل",
    "hero_cta_secondary": "اعرف المزيد",
    "hero_chip_encrypted": "نقل مشفّر",
    "hero_chip_privacy": "التركيز على الخصوصية",
    "hero_chip_responsible": "ذكاء اصطناعي مسؤول",

    # METRICS BAR
    "metric_1_value": "AES-256",
    "metric_1_label": "معيار التشفير",
    "metric_2_value": "TLS 1.3",
    "metric_2_label": "تشفير النقل",
    "metric_3_value": "9+",
    "metric_3_label": "اللغات المدعومة",
    "metric_4_value": "0",
    "metric_4_label": "بيانات مبيعة لأطراف ثالثة",

    # OVERVIEW SECTION
    "overview_badge": "نظرة عامة على الأمان",
    "overview_title_1": "كيف نحمي",
    "overview_title_2": "بياناتك",
    "overview_desc": "تعمل طبقات أمان متعددة معًا لحماية معلوماتك الصحية طوال دورة حياتها.",

    # 6 OVERVIEW CARDS
    "card_1_title": "نقل مشفّر",
    "card_1_desc": "يتم نقل جميع البيانات عبر اتصالات مشفّرة بـ TLS. تُحمى الملفات المرفوعة والتقارير المُنشأة أثناء النقل بين جهازك وخوادمنا.",
    "card_1_tag": "تشفير TLS",

    "card_2_title": "وصول مُتحكَّم به",
    "card_2_desc": "يُقيَّد الوصول إلى بيانات المستخدمين من خلال ضوابط المصادقة والأذونات القائمة على الأدوار. يتبع الوصول الإداري مبدأ الحد الأدنى من الامتيازات.",
    "card_2_tag": "ضوابط الوصول",

    "card_3_title": "معالجة دفع آمنة",
    "card_3_desc": "تتم معالجة المدفوعات من قبل مزودي دفع متوافقين مع PCI. لا تُخزَّن بيانات بطاقات الائتمان أبدًا على خوادم NoryaAI.",
    "card_3_tag": "مزوّد PCI",

    "card_4_title": "بنية واعية بالخصوصية",
    "card_4_desc": "نتبع مبادئ تقليل البيانات — نجمع فقط ما هو ضروري لتقديم الخدمة. لا تُستخدم البيانات الصحية للإعلانات ولا تُباع لأطراف ثالثة.",
    "card_4_tag": "تقليل البيانات",

    "card_5_title": "منتج متعدد اللغات",
    "card_5_desc": "تُقدَّم التقارير والتحليلات بأكثر من 9 لغات مع ضوابط جودة متسقة، مما يضمن نفس العرض المسؤول في جميع المناطق المدعومة.",
    "card_5_tag": "9+ لغة",

    "card_6_title": "حدود منتج مسؤولة",
    "card_6_desc": "NoryaAI هو أداة تعليمية في مجال التكنولوجيا الصحية. لا يقدم تشخيصات طبية، ولا يحل محل الحكم السريري، ولا يقدم إرشادات طوارئ.",
    "card_6_tag": "أداة تعليمية",

    # DATA FLOW SECTION
    "data_badge": "تدفق البيانات",
    "data_title_1": "كيف تُعالج",
    "data_title_2": "بياناتك",
    "data_desc": "نظرة عامة رفيعة المستوى حول كيفية تدفق المعلومات عبر منصة NoryaAI — من الرفع إلى تسليم التقرير.",

    "step_1_title": "الرفع",
    "step_1_desc": "تُرفع نتائج المختبر عبر اتصالات مشفّرة",
    "step_2_title": "المعالجة",
    "step_2_desc": "تحليل بالذكاء الاصطناعي مع ضوابط وصول وعزل البيانات",
    "step_3_title": "التقرير",
    "step_3_desc": "يُنشأ تقرير منظم باللغة التي اخترتها",
    "step_4_title": "التسليم",
    "step_4_desc": "يُسلَّم التقرير فقط للمستخدمين الموثّقين",

    # DATA RIGHTS SECTION
    "rights_badge": "حقوقك في البيانات",
    "rights_title_1": "بياناتك،",
    "rights_title_2": "تحكّمك",
    "rights_desc": "نوفر أدوات وعمليات لمساعدتك في إدارة بياناتك الشخصية وفقًا للوائح المعمول بها.",

    "right_1_title": "حذف البيانات",
    "right_1_desc": "يمكنك طلب حذف حسابك والبيانات المرتبطة به. عند الطلب، تُزال البيانات وفقًا للوائح حماية البيانات المعمول بها وأي فترات احتفاظ قانونية مطلوبة.",
    "right_1_link": "اعرف المزيد",

    "right_2_title": "الوصول والنقل",
    "right_2_desc": "لديك الحق في الوصول إلى البيانات الشخصية التي نحتفظ بها عنك وطلبها بتنسيق قابل للنقل، وفقًا للوائح المعمول بها.",
    "right_2_link": "تفاصيل الخصوصية",

    "right_3_title": "تقييد الغرض",
    "right_3_desc": "تُستخدم بياناتك الصحية فقط لتقديم خدمة التحليل التي طلبتها. لا تُستخدم للإعلانات أو التنميط أو تُباع لأطراف ثالثة.",
    "right_3_link": "سياسة الخصوصية",

    # OPERATIONAL SAFEGUARDS
    "ops_badge": "ضمانات تشغيلية",
    "ops_title_1": "ضوابط الوصول",
    "ops_title_2": "والأمان",

    "ops_1_title": "إدارة الوصول",
    "ops_1_desc": "تستخدم أنظمة الإنتاج ضوابط وصول قائمة على الأدوار. يُقيَّد الوصول الإداري بالموظفين المصرح لهم ويتبع مبدأ الحد الأدنى من الامتيازات.",

    "ops_2_title": "أمان البنية التحتية",
    "ops_2_desc": "تستخدم المنصة Cloudflare لأمان الحافة والحماية من هجمات DDoS. تتبع البنية التحتية للتطبيق ممارسات تقوية الأمان القياسية.",

    "ops_3_title": "التسجيل والمراقبة",
    "ops_3_desc": "تُسجَّل نشاطات النظام لأغراض أمنية وتشغيلية. تساعد المراقبة في اكتشاف المشكلات المحتملة والاستجابة لها.",

    "ops_4_title": "أمان المدفوعات",
    "ops_4_desc": "تتم جميع عمليات معالجة المدفوعات عبر PayTR، وهو مزوّد دفع متوافق مع PCI. لا يخزّن NoryaAI بيانات بطاقات الائتمان.",

    # REGULATORY APPROACH
    "reg_badge": "النهج التنظيمي",
    "reg_title_1": "نهجنا في",
    "reg_title_2": "حماية البيانات",
    "reg_desc": "يتبع NoryaAI مبادئ حماية البيانات المتوافقة مع اللوائح المعمول بها في المناطق التي نخدمها.",

    "reg_1_title": "التوافق مع GDPR",
    "reg_1_subtitle": "حماية البيانات الأوروبية",
    "reg_1_desc": "نتبع مبادئ GDPR بما في ذلك تقليل البيانات، وتقييد الغرض، والخصوصية المدمجة في التصميم. للمستخدمين حق الوصول إلى بياناتهم الشخصية وتصحيحها وطلب حذفها.",
    "reg_1_chip1": "الخصوصية بالتصميم",
    "reg_1_chip2": "حقوق البيانات",
    "reg_1_chip3": "نقل البيانات",

    "reg_2_title": "التوافق مع KVKK",
    "reg_2_subtitle": "حماية البيانات التركية",
    "reg_2_desc": "بصفتنا شركة تعمل في تركيا، نلتزم بمتطلبات قانون حماية البيانات الشخصية التركي (KVKK)، بما في ذلك بروتوكولات الموافقة والتزامات مراقب البيانات.",
    "reg_2_chip1": "بروتوكولات الموافقة",
    "reg_2_chip2": "مراقب البيانات",
    "reg_2_chip3": "حذف البيانات",

    # LIMITS & RESPONSIBLE USE
    "limits_badge": "الاستخدام المسؤول",
    "limits_title": "قيود مهمة",
    "limits_desc": "صُمّم NoryaAI كأداة تعليمية في مجال التكنولوجيا الصحية. فهم حدوده أمر مهم للاستخدام الآمن والمسؤول.",

    "limit_1_title": "ليس تشخيصًا طبيًا",
    "limit_1_desc": "يقدم NoryaAI شروحات تعليمية لقيم المختبر. لا يشخّص حالات مرضية، ولا يصف علاجات، ولا يحل محل التقييم الطبي المهني.",

    "limit_2_title": "ليس إرشادات طوارئ",
    "limit_2_desc": "هذه المنصة غير مصممة للحالات العاجلة أو الطارئة. إذا كانت لديك حالة طبية طارئة، اتصل بخدمات الطوارئ المحلية فورًا.",

    "limit_3_title": "استشر مقدم الرعاية الصحية",
    "limit_3_desc": "ناقش دائمًا نتائج مختبرك مع أخصائي رعاية صحية مؤهل قبل اتخاذ قرارات متعلقة بالصحة.",

    # TRUST FRAMEWORK
    "trust_badge": "إطار الثقة",
    "trust_title": "استكشف إطار الثقة لدينا",
    "trust_1_title": "المنهجية",
    "trust_1_desc": "كيف نفسّر نتائج تحاليل الدم",
    "trust_2_title": "المراجعة الطبية",
    "trust_2_desc": "الإشراف السريري والسلامة",
    "trust_3_title": "سياسة الخصوصية",
    "trust_3_desc": "كيف نتعامل مع بياناتك الشخصية",
    "trust_4_title": "الشفافية",
    "trust_4_desc": "كيف نحدد ونقدم ادعاءاتنا",
    "trust_5_title": "شروط الاستخدام",
    "trust_5_desc": "شروط الخدمة والمسؤوليات",
    "trust_6_title": "مركز الثقة",
    "trust_6_desc": "إطار الثقة الكامل لدينا",

    # PROCUREMENT CTA
    "procurement_badge": "للمؤسسات",
    "procurement_title": "هل تقيّمون NoryaAI لمؤسستكم؟",
    "procurement_desc": "تعرّفوا على منهجيتنا وممارسات الخصوصية وعملية المراجعة الطبية وإطار الاستخدام المسؤول.",
    "procurement_cta_1": "معلومات المؤسسات",
    "procurement_cta_2": "اتصل بنا",
    "procurement_cta_3": "عرض المنهجية",

    # FAQ
    "faq_badge": "الأسئلة الشائعة",
    "faq_title_1": "أسئلة",
    "faq_title_2": "الأمان",

    "faq_q1": "كيف تُحمى بياناتي الصحية؟",
    "faq_a1": "تُنقل جميع البيانات عبر اتصالات مشفّرة بـ TLS. تُعالج نتائج المختبر المرفوعة مع وجود ضوابط وصول، وتُسلَّم التقارير فقط للمستخدمين الموثّقين. نتبع مبادئ تقليل البيانات ولا نبيع البيانات الصحية لأطراف ثالثة.",

    "faq_q2": "هل يمكن لموظفي NoryaAI رؤية نتائج مختبري؟",
    "faq_a2": "يُقيَّد الوصول إلى بيانات المستخدمين من خلال ضوابط قائمة على الأدوار. يصل فريقنا إلى بيانات المستخدمين فقط عند الضرورة للدعم الفني أو صيانة النظام، وفقط بالقدر اللازم لذلك الغرض.",

    "faq_q3": "كيف يمكنني حذف بياناتي؟",
    "faq_a3": "يمكنك طلب حذف حسابك والبيانات المرتبطة به في أي وقت عن طريق الاتصال بنا. نعالج طلبات الحذف وفقًا للوائح حماية البيانات المعمول بها، مع مراعاة أي فترات احتفاظ مطلوبة قانونيًا.",

    "faq_q4": "هل معلومات الدفع الخاصة بي آمنة؟",
    "faq_a4": "لا نخزّن بيانات بطاقات الائتمان. تتم جميع عمليات معالجة المدفوعات عبر PayTR، وهو مزوّد دفع متوافق مع PCI. تُرمَّز بيانات المعاملات وتُشفَّر.",

    "faq_q5": "هل يشارك NoryaAI البيانات مع أطراف ثالثة؟",
    "faq_a5": "لا تُشارَك بياناتك الصحية مع أطراف ثالثة لأغراض إعلانية أو تسويقية. نعمل مع مزودي خدمات (استضافة، دفع) حسب الحاجة لتقديم الخدمة، كما هو موضح في سياسة الخصوصية الخاصة بنا.",

    # BOTTOM CTA
    "cta_title_1": "ابدأ رحلتك",
    "cta_title_2": "الصحية الآمنة",
    "cta_desc": "ارفع نتائج مختبرك واحصل على رؤى صحية واضحة وتعليمية — مع خصوصية وأمان مدمجين.",
    "cta_primary": "ابدأ الآن",
    "cta_secondary": "اتصل بنا",

    # NAV
    "nav_analysis": "التحليل",
    "nav_science": "العلوم",
    "nav_about": "حول",
    "nav_security": "الأمان",
    "nav_pricing": "الأسعار",
    "nav_get_started": "ابدأ الآن",
    "nav_menu": "القائمة",

    # FOOTER
    "footer_platform": "المنصة",
    "footer_biomarkers": "المؤشرات الحيوية",
    "footer_science": "العلوم",
    "footer_reports": "التقارير",
    "footer_trust_legal": "الثقة والقانون",
    "footer_privacy_policy": "سياسة الخصوصية",
    "footer_terms": "شروط الاستخدام",
    "footer_security": "الأمان",
    "footer_gdpr_kvkk": "GDPR و KVKK",
    "footer_trust_center": "مركز الثقة",
    "footer_contact_heading": "التواصل",
    "footer_support": "الدعم",
    "footer_security_inquiries": "استفسارات الأمان",
    "footer_enterprise": "المؤسسات",
    "footer_copyright": "© 2025 NoryaAI. تكنولوجيا صحية مسؤولة.",
    "footer_tagline": "شروحات تحاليل الدم بالذكاء الاصطناعي بلغة واضحة. ليس بديلاً عن الاستشارة الطبية.",

    # SEO INTERNAL LINKS
    "seo_explore": "استكشف",
}

# ---------------------------------------------------------------------------
# Aggregation & helpers
# ---------------------------------------------------------------------------

_SECURITY_ALL = {
    "en": _SECURITY_EN,
    "tr": _SECURITY_TR,
    "de": _SECURITY_DE,
    "fr": _SECURITY_FR,
    "es": _SECURITY_ES,
    "it": _SECURITY_IT,
    "he": _SECURITY_HE,
    "hi": _SECURITY_HI,
    "ar": _SECURITY_AR,
}


def get_security_ui(lang: str | None) -> dict:
    """Return security page UI strings for the given locale."""
    lang = ((lang or "").lower()[:2]) or DEFAULT_SECURITY_LANG
    return dict(_SECURITY_ALL.get(lang, _SECURITY_ALL[DEFAULT_SECURITY_LANG]))


def get_security_meta(lang: str | None) -> dict:
    """Return meta_title and meta_description for the security page."""
    t = get_security_ui(lang)
    return {"meta_title": t["meta_title"], "meta_description": t["meta_description"]}
