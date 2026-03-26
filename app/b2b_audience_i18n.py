# pylint: disable=line-too-long
"""
B2B audience landing pages: shared copy for /for-doctors, /for-clinics, /for-hospitals,
/enterprise-security, /clinical-demo.
"""
from __future__ import annotations

import copy
from typing import Any, Dict

PAGE_PATHS = frozenset(
    {
        "for-doctors",
        "for-clinics",
        "for-hospitals",
        "enterprise-security",
        "clinical-demo",
    }
)


def _en_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "Book demo",
        "hero_cta_secondary": "Contact sales",
        "hero_cta_tertiary": "See sample workflow",
        "cta_book_demo": "Book demo",
        "cta_contact_sales": "Contact sales",
        "cta_sample_workflow": "Sample workflow",
    }


def _tr_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "Demo planla",
        "hero_cta_secondary": "Satış ile iletişim",
        "hero_cta_tertiary": "Örnek akışı gör",
        "cta_book_demo": "Demo planla",
        "cta_contact_sales": "Satış ile iletişim",
        "cta_sample_workflow": "Örnek akış",
    }


def _de_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "Demo buchen",
        "hero_cta_secondary": "Vertrieb kontaktieren",
        "hero_cta_tertiary": "Beispiel-Workflow ansehen",
        "cta_book_demo": "Demo buchen",
        "cta_contact_sales": "Vertrieb kontaktieren",
        "cta_sample_workflow": "Beispiel-Workflow",
    }


def _fr_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "Réserver une démo",
        "hero_cta_secondary": "Contacter les ventes",
        "hero_cta_tertiary": "Voir un exemple de flux",
        "cta_book_demo": "Réserver une démo",
        "cta_contact_sales": "Contacter les ventes",
        "cta_sample_workflow": "Exemple de flux",
    }


def _it_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "Prenota una demo",
        "hero_cta_secondary": "Contatta le vendite",
        "hero_cta_tertiary": "Vedi il flusso di esempio",
        "cta_book_demo": "Prenota una demo",
        "cta_contact_sales": "Contatta le vendite",
        "cta_sample_workflow": "Flusso di esempio",
    }


def _es_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "Reservar demo",
        "hero_cta_secondary": "Contactar ventas",
        "hero_cta_tertiary": "Ver flujo de ejemplo",
        "cta_book_demo": "Reservar demo",
        "cta_contact_sales": "Contactar ventas",
        "cta_sample_workflow": "Flujo de ejemplo",
    }


def _he_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "לקבוע הדגמה",
        "hero_cta_secondary": "ליצור קשר עם המכירות",
        "hero_cta_tertiary": "לצפות בתהליך לדוגמה",
        "cta_book_demo": "לקבוע הדגמה",
        "cta_contact_sales": "ליצור קשר עם המכירות",
        "cta_sample_workflow": "תהליך לדוגמה",
    }


def _hi_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "डेमो बुक करें",
        "hero_cta_secondary": "सेल्स से संपर्क",
        "hero_cta_tertiary": "नमूना वर्कफ़्लो देखें",
        "cta_book_demo": "डेमो बुक करें",
        "cta_contact_sales": "सेल्स से संपर्क",
        "cta_sample_workflow": "नमूना वर्कफ़्लो",
    }


def _ar_cta() -> Dict[str, str]:
    return {
        "hero_cta_primary": "احجز عرضاً توضيحياً",
        "hero_cta_secondary": "تواصل مع المبيعات",
        "hero_cta_tertiary": "شاهد مسار العمل النموذجي",
        "cta_book_demo": "احجز عرضاً توضيحياً",
        "cta_contact_sales": "تواصل مع المبيعات",
        "cta_sample_workflow": "مسار عمل نموذجي",
    }


CTA_BY_LANG: Dict[str, Dict[str, str]] = {
    "en": _en_cta(),
    "tr": _tr_cta(),
    "de": _de_cta(),
    "fr": _fr_cta(),
    "it": _it_cta(),
    "es": _es_cta(),
    "he": _he_cta(),
    "hi": _hi_cta(),
    "ar": _ar_cta(),
}


def _faq_common_en() -> list:
    return [
        {
            "q": "Is Norya a medical device or diagnostic?",
            "a": "No. Norya is assistive software for turning laboratory data into structured, multilingual patient explanations for clinicians to review.",
        },
        {
            "q": "How do you handle data protection?",
            "a": "We apply encryption in transit and tiered data handling policies. Enterprise controls (SSO, DPA, BAAs where applicable) are available for clinical teams.",
        },
        {
            "q": "Which regions do you support?",
            "a": "We serve teams in 50+ countries, with localization available across 9+ report languages.",
        },
        {
            "q": "Can you integrate with our LIMS or EMR?",
            "a": "Yes. We work with standard lab exports and enterprise integration patterns. Contact sales to align with your stack.",
        },
        {
            "q": "What accuracy do you claim?",
            "a": "Our internal platform evaluation reports 98.7% biomarker classification accuracy across structured lab inputs—not clinical diagnostic accuracy.",
        },
        {
            "q": "How do we start a pilot?",
            "a": "Book a demo through the corporate contact form. We will scope volume, languages, and governance with your team.",
        },
    ]


def _page_doctors_en() -> Dict[str, Any]:
    return {
        "meta_title": "Norya for Doctors | Lab clarity in minutes",
        "meta_description": "Assistive lab-to-language reports for busy physicians: structured markers, plain language, review-ready output in 9+ languages.",
        "hero_badge": "For clinicians",
        "hero_title": "Explain complex labs in patient-friendly language—without extra admin time.",
        "hero_desc": "Norya turns standard lab exports into bilingual-ready, plain-language summaries so you can counsel faster. Built for practices that see high lab volume across 4,000+ hospitals and clinics in our network footprint.",
        "who_title": "Who this is for",
        "who_desc": "Primary care physicians, specialists, and hospitalists who need rapid, consistent explanations across heterogeneous lab panels.",
        "who_primary": "High-throughput clinics and group practices",
        "who_secondary": "Multilingual patient populations",
        "who_points": [
            "Outpatient and inpatient workflows",
            "Teams that coordinate with external labs",
        ],
        "benefits_title": "What you get",
        "benefits": [
            {
                "title": "Faster counseling checkpoints",
                "desc": "Structured marker grouping highlights what matters first for the visit context.",
                "points": ["Triage-oriented layout", "Less dictation rework", "Consistent framing across visits"],
            },
            {
                "title": "Patient-ready language",
                "desc": "Plain-language explanations you can hand to patients or adapt into your own notes.",
                "points": ["9+ report languages", "Conservative phrasing", "Clinician review step built-in"],
            },
            {
                "title": "Operational reliability",
                "desc": "Built for teams that already generate 2M+ reports through the platform.",
                "points": ["Audit-friendly structure", "Enterprise security path", "Dedicated onboarding"],
            },
            {
                "title": "Trust and governance",
                "desc": "Designed as assistive documentation—not a diagnostic substitute.",
                "points": ["Human-in-the-loop review", "Clear limitations in copy", "Alignment with compliance discussions"],
            },
        ],
        "workflow_title": "From raw labs to review-ready patient language",
        "workflow_steps": [
            {"title": "Ingest", "desc": "Secure intake of CSV/PDF exports or API-connected feeds."},
            {"title": "Structure", "desc": "Marker normalization with 98.7% biomarker classification accuracy in internal platform evaluation."},
            {"title": "Explain", "desc": "Plain-language generation with clinical tone controls and multilingual output."},
            {"title": "Review", "desc": "Clinician sign-off before anything reaches the patient record or portal."},
        ],
        "faq_title": "Frequently asked questions",
        "faq": _faq_common_en(),
    }


def _page_clinics_en() -> Dict[str, Any]:
    return {
        "meta_title": "Norya for Clinics | Operational lab communication",
        "meta_description": "Standardize patient-facing lab explanations across providers, languages, and shifts—without adding headcount.",
        "hero_badge": "For clinics",
        "hero_title": "One operating rhythm for lab communication across every room in the clinic.",
        "hero_desc": "Norya gives clinic operators a single pipeline for turning labs into review-ready, multilingual collateral. Scale the same quality whether you run one site or a regional footprint across 50+ countries.",
        "who_title": "Built for clinical operators",
        "who_desc": "Medical directors, operations leads, and care teams modernizing how labs are explained after every draw.",
        "who_primary": "Multi-provider ambulatory networks",
        "who_secondary": "High-volume phlebotomy and rapid follow-up models",
        "who_points": ["CCM / care coordination programs", "Employer and occupational health panels"],
        "benefits_title": "Outcomes your administrators track",
        "benefits": [
            {
                "title": "Throughput without burnout",
                "desc": "Automate the first draft of patient education tied to each result pattern.",
                "points": ["Templated escalations", "Shift-friendly handoffs", "Fewer manual edits"],
            },
            {
                "title": "Brand-safe patient voice",
                "desc": "Lock tone, disclaimers, and glossary terms centrally.",
                "points": ["9+ languages out of the box", "Versioned snippets", "Legal review checkpoints"],
            },
            {
                "title": "Visibility for leadership",
                "desc": "Dashboard-ready metrics on turnaround and language coverage.",
                "points": ["Volume telemetry", "SLA alignment", "Export for QI initiatives"],
            },
            {
                "title": "Enterprise-ready controls",
                "desc": "Security reviews map to hospital compliance expectations.",
                "points": ["SSO roadmap", "DPA templates", "Dedicated success partner"],
            },
        ],
        "workflow_title": "Clinic-scale workflow",
        "workflow_steps": [
            {"title": "Intake", "desc": "Route orders from LIMS or batched uploads with clinic metadata."},
            {"title": "Normalize", "desc": "Canonicalize analytes and units across mixed lab feeds."},
            {"title": "Generate", "desc": "Produce multilingual drafts plus internal clinician notes."},
            {"title": "Publish", "desc": "Release to portals, print-at-check-in, or secure messaging once reviewed."},
        ],
        "faq_title": "Clinic FAQs",
        "faq": _faq_common_en(),
    }


def _page_hospitals_en() -> Dict[str, Any]:
    return {
        "meta_title": "Norya for Hospitals | Enterprise lab language layer",
        "meta_description": "Deploy an enterprise lab communication layer across inpatient, outpatient, and affiliate networks with governance built in.",
        "hero_badge": "For hospital systems",
        "hero_title": "A single governance model for every lab result leaving your IDN.",
        "hero_desc": "Hospital informatics and clinical leadership get a unified assistive layer: consistent terminology, localized variants, and SOC2-minded operations that match IDN procurement standards.",
        "who_title": "Who we partner with",
        "who_desc": "CMIOs, CNIOs, pathology informatics, and revenue-cycle leaders aligning quality with throughput.",
        "who_primary": "Integrated delivery networks",
        "who_secondary": "Teaching hospitals and specialty institutes",
        "who_points": ["Laboratory services with outreach programs", "Hybrid on-prem / cloud strategies"],
        "benefits_title": "Health-system value",
        "benefits": [
            {
                "title": "Risk-aware automation",
                "desc": "Guard-railed generation with explicit assistive positioning.",
                "points": ["Policy overlays", "Escalation to subspecialists", "Immutable audit logs"],
            },
            {
                "title": "Cross-campus consistency",
                "desc": "Synchronize languages, reading levels, and escalation language across sites.",
                "points": ["Central glossary", "Regional overrides", "Epic/Cerner adjacency projects"],
            },
            {
                "title": "Measured excellence",
                "desc": "Leverage the same internal platform evaluation showing 98.7% biomarker classification accuracy.",
                "points": ["Before/after QA studies", "Biomarker coverage reporting", "Patient comprehension pilots"],
            },
            {
                "title": "Procurement-ready diligence",
                "desc": "Enterprise security documentation and clinical workflows are packaged for your committee process.",
                "points": ["BAA readiness", "Pen-test summaries", "Implementation playbook"],
            },
        ],
        "workflow_title": "Enterprise rollout",
        "workflow_steps": [
            {"title": "Align", "desc": "Joint design session covering service lines, languages, and data routing."},
            {"title": "Integrate", "desc": "Stand up connectors to lab middleware and identity providers."},
            {"title": "Validate", "desc": "Parallel run with quality indicators and clinician sampling."},
            {"title": "Scale", "desc": "Progressive activation by campus, affiliate, or franchise partner."},
        ],
        "faq_title": "Hospital FAQs",
        "faq": _faq_common_en(),
    }


def _page_security_en() -> Dict[str, Any]:
    return {
        "meta_title": "Enterprise security | Norya",
        "meta_description": "Encryption, access controls, and procurement documentation for teams adopting Norya's assistive lab intelligence layer.",
        "hero_badge": "Security & compliance",
        "hero_title": "Security architecture that stands up to healthcare procurement.",
        "hero_desc": "Norya is built for regulated environments: tiered data handling, least-privilege access, and audit trails suitable for hospital ISO/SOC review cycles.",
        "who_title": "Stakeholders we support",
        "who_desc": "CISOs, diagnostic security officers, and contracting teams who must document every subsystem.",
        "who_primary": "Healthcare enterprises",
        "who_secondary": "Diagnostic service organizations",
        "who_points": ["Cloud-forward and hybrid footprints", "Multinational privacy counsel reviews"],
        "benefits_title": "Control areas",
        "benefits": [
            {
                "title": "Data protection",
                "desc": "Encryption in transit, scoped retention, and regional processing options reviewed with your counsel.",
                "points": ["TLS 1.2+", "Key management guidance", "Configurable purge windows"],
            },
            {
                "title": "Access governance",
                "desc": "Enterprise SSO, granular roles, and session policies.",
                "points": ["SAML / OIDC roadmap", "JIT provisioning patterns", "Break-glass procedures"],
            },
            {
                "title": "Assurance artifacts",
                "desc": "Security packet includes architecture diagrams, pen-test summaries, and subprocessors.",
                "points": ["SOC2 program alignment", "DPA templates", "Incident response runbooks"],
            },
            {
                "title": "Clinical alignment",
                "desc": "Articulate how assistive outputs remain clinician-in-the-loop.",
                "points": ["Risk analysis memos", "Clinical safety narratives", "FAQ for legal review"],
            },
        ],
        "workflow_title": "How reviews proceed",
        "workflow_steps": [
            {"title": "NDA & scoping", "desc": "Exchange standard paperwork and align on deployment topology."},
            {"title": "Architecture review", "desc": "Walk through data flows, encryption, and subprocessors together."},
            {"title": "Pilot", "desc": "Limited production with logging and monitoring dashboards."},
            {"title": "Scale decision", "desc": "Finalize BAAs/DPAs and regional configurations for broad rollout."},
        ],
        "faq_title": "Security FAQs",
        "faq": _faq_common_en(),
    }


def _page_demo_en() -> Dict[str, Any]:
    return {
        "meta_title": "Clinical demo | Norya workflow",
        "meta_description": "See how labs move from structured data to multilingual, review-ready patient explanations in one workflow.",
        "hero_badge": "Guided evaluation",
        "hero_title": "Walk a real clinical workflow—from lab file to signed patient copy.",
        "hero_desc": "In 30 minutes we map your lab feeds, languages, and review model to the Norya pipeline used across 50+ countries and 4,000+ hospitals and clinics.",
        "who_title": "Ideal evaluation teams",
        "who_desc": "Clinical innovation leads, lab directors, and digital health sponsors validating assistive tooling.",
        "who_primary": "Multidisciplinary steering committees",
        "who_secondary": "Quality and patient-education owners",
        "who_points": ["Innovation budgets for FY planning", "Need for multilingual proof points"],
        "benefits_title": "What you will validate",
        "benefits": [
            {
                "title": "Hands-on pipeline",
                "desc": "Load sanitized samples and watch structure, explanation, and review steps.",
                "points": ["Marker grouping fidelity", "Language quality", "Clinician review UX"],
            },
            {
                "title": "Metric transparency",
                "desc": "We contextualize 98.7% biomarker classification accuracy from internal platform evaluation—not diagnostic claims.",
                "points": ["Biomarker-level QA", "Edge-case discussion", "Roadmap for your analytes"],
            },
            {
                "title": "Stakeholder kits",
                "desc": "Leave with security FAQ, clinical positioning, and procurement paths.",
                "points": ["Slide outline", "DPA checklist", "Integration prerequisites"],
            },
            {
                "title": "Next steps",
                "desc": "Pilot scoping, licensing, and success metrics in one working session.",
                "points": ["Volume assumptions", "Localization plan", "Training approach"],
            },
        ],
        "workflow_title": "Demo storyline",
        "workflow_steps": [
            {"title": "Scenario", "desc": "Pick a representative panel and patient context."},
            {"title": "Ingest & normalize", "desc": "Show mapping from your typical export format."},
            {"title": "Generate", "desc": "Produce multilingual drafts with review annotations."},
            {"title": "Q&A", "desc": "Open discussion for medical, IT, and legal stakeholders."},
        ],
        "faq_title": "Demo FAQs",
        "faq": _faq_common_en(),
    }


PAGES_EN: Dict[str, Dict[str, Any]] = {
    "for-doctors": _page_doctors_en(),
    "for-clinics": _page_clinics_en(),
    "for-hospitals": _page_hospitals_en(),
    "enterprise-security": _page_security_en(),
    "clinical-demo": _page_demo_en(),
}


def _faq_common_tr() -> list:
    return [
        {
            "q": "Norya tıbbi cihaz veya tanı aracı mı?",
            "a": "Hayır. Norya, klinisyenlerin gözden geçirmesi için laboratuvar verilerini yapılandırılmış, çok dilli hasta açıklamalarına dönüştüren yardımcı yazılımdır.",
        },
        {
            "q": "Veri koruma nasıl ele alınıyor?",
            "a": "Aktarımda şifreleme ve katmanlı veri işleme politikaları uygularız. SSO, DPA ve gerekli yerlerde BAA gibi kurumsal kontroller klinik ekipler için mevcuttur.",
        },
        {
            "q": "Hangi bölgeler destekleniyor?",
            "a": "50 ülkedeki ekiplere hizmet veriyoruz; 9 rapor dilinde lokalizasyon sunulur.",
        },
        {
            "q": "LIMS veya EMR ile entegre olabilir misiniz?",
            "a": "Evet. Standart laboratuvar dışa aktarımları ve kurumsal entegrasyon desenleriyle çalışırız. Yığınınıza uydurmak için satış ile iletişime geçin.",
        },
        {
            "q": "Hangi doğruluğu iddia ediyorsunuz?",
            "a": "İç platform değerlendirmemizde yapılandırılmış laboratuvar girdilerinde %98,7 biyomarker sınıflandırma doğruluğu görülür; bu klinik tanı doğruluğu değildir.",
        },
        {
            "q": "Pilotu nasıl başlatırız?",
            "a": "Kurumsal iletişim formundan demo planlayın. Hacim, diller ve yönetişimi birlikte kapsamlarız.",
        },
    ]


def _page_doctors_tr() -> Dict[str, Any]:
    t = copy.deepcopy(_page_doctors_en())
    t.update(
        {
            "meta_title": "Hekimler için Norya | Laboratuvar netliği dakikalar içinde",
            "meta_description": "Yoğun hekimler için yardımcı laboratuvar raporları: yapılandırılmış gösterge, sade dil, 9+ dilde incelemeye hazır çıktı.",
            "hero_badge": "Klinisyenler için",
            "hero_title": "Karmaşık laboratuvarları hasta dostu dile çevirin—ekstra idari yükle olmadan.",
            "hero_desc": "Norya standart laboratuvar dışa aktarımlarını çift dil hazır, sade özetlere dönüştürür; böylece danışmanlığı hızlandırırsınız. Ağımızdaki 4.000 hastane ve klinikte yüksek laboratuvar hacmini gören uygulamalar için tasarlandı.",
            "who_title": "Kimler için",
            "who_desc": "Birincil bakım hekimleri, uzmanlar ve heterojen paneller arasında tutarlı açıklama isteyen hastane hekimleri.",
            "who_primary": "Yüksek hacimli klinikler ve grup pratiği",
            "who_secondary": "Çok dilli hasta popülasyonları",
            "who_points": ["Ayaktan ve yatan hasta akışları", "Harici laboratuvarlarla koordinasyon"],
            "benefits_title": "Kazanımlar",
            "benefits": [
                {
                    "title": "Daha hızlı danışmanlık",
                    "desc": "Yapılandırılmış gruplama ziyaret bağlamında önce neyin önemli olduğunu öne çıkarır.",
                    "points": ["Triage odaklı düzen", "Daha az dikte düzeltmesi", "Ziyaretler arası tutarlı çerçeve"],
                },
                {
                    "title": "Hazır hasta dili",
                    "desc": "Hastalara verebileceğiniz veya notlarınıza uyarlayabileceğiniz sade açıklamalar.",
                    "points": ["9+ rapor dili", "Muhafazakar ifadeler", "Klinisyen incelemesi dahil"],
                },
                {
                    "title": "Operasyonel güvenilirlik",
                    "desc": "Platform üzerinden 2M+ rapor üreten ekipler için tasarlandı.",
                    "points": ["Denetime uygun yapı", "Kurumsal güvenlik yolu", "Özel onboarding"],
                },
                {
                    "title": "Güven ve yönetişim",
                    "desc": "Tanı yerine geçmeyen yardımcı dokümantasyon olarak konumlanır.",
                    "points": ["İnsan döngüsünde inceleme", "Metinde net sınırlar", "Uyum görüşmeleriyle uyum"],
                },
            ],
            "workflow_title": "Ham laboratuvardan incelemeye hazır dile",
            "workflow_steps": [
                {"title": "Alım", "desc": "CSV/PDF dışa aktarım veya API beslemelerinin güvenli alımı."},
                {"title": "Yapılandırma", "desc": "İç platform değerlendirmesinde %98,7 biyomarker sınıflandırma doğruluğu ile gösterge normalizasyonu."},
                {"title": "Açıklama", "desc": "Klinik ton kontrolleri ve çok dilli çıktı ile sade dil üretimi."},
                {"title": "İnceleme", "desc": "Hasta kaydına veya portala geçmeden önce klinisyen onayı."},
            ],
            "faq_title": "Sık sorulan sorular",
            "faq": _faq_common_tr(),
        }
    )
    return t


def _page_clinics_tr() -> Dict[str, Any]:
    t = copy.deepcopy(_page_clinics_en())
    t.update(
        {
            "meta_title": "Klinikler için Norya | Operasyonel laboratuvar iletişimi",
            "meta_description": "Sağlayıcı, dil ve vardiya genelinde hasta odaklı laboratuvar açıklamalarını standartlaştırın—ek personel eklemeden.",
            "hero_badge": "Klinikler için",
            "hero_title": "Klinikteki her oda için tek operasyon ritmi.",
            "hero_desc": "Norya operatörlere laboratuvarları çok dilli, incelemeye hazır materyale dönüştürmek için tek bir boru hattı verir. Tek merkez veya 50 ülkedeki bölgesel ağınız olsun aynı kaliteyi ölçeklersiniz.",
            "who_title": "Klinik operatörler için",
            "who_desc": "Her çekimden sonra laboratuvarların nasıl açıklanacağını modernleştiren tıbbi direktörler ve operasyon liderleri.",
            "who_primary": "Çok sağlayıcılı ayak tedavi ağları",
            "who_secondary": "Yüksek hacimli flebotomi ve hızlı takip modelleri",
            "who_points": ["CCM / bakım koordinasyonu", "İşveren ve iş sağlığı panelleri"],
            "benefits_title": "Yöneticilerin takip ettiği sonuçlar",
            "benefits": [
                {
                    "title": "Tükenmişlik olmadan hız",
                    "desc": "Her sonuç modeline bağlı hasta eğitiminin ilk taslağını otomatikleştirin.",
                    "points": ["Şablonlu eskalasyonlar", "Vardiya dostu devir", "Daha az manuel düzenleme"],
                },
                {
                    "title": "Marka güvenli ses",
                    "desc": "Ton, feragat ve sözlük terimlerini merkezi olarak kilitleyin.",
                    "points": ["9+ dil", "Sürümlü parçalar", "Hukuk inceleme kontrol noktaları"],
                },
                {
                    "title": "Liderlik için görünürlük",
                    "desc": "Döngü ve dil kapsamı için pano metrikleri.",
                    "points": ["Hacim telemetrisi", "SLA uyumu", "QI ihracı"],
                },
                {
                    "title": "Kurumsal kontroller",
                    "desc": "Güvenlik incelemeleri hastane uyum beklentilerine haritalanır.",
                    "points": ["SSO yol haritası", "DPA şablonları", "Özel başarı ortağı"],
                },
            ],
            "workflow_title": "Klinik ölçeği",
            "workflow_steps": [
                {"title": "Alım", "desc": "LIMS veya batched yüklemelerden klinik meta veri ile yönlendirme."},
                {"title": "Normalize et", "desc": "Karışık beslemeler arasında analit ve birimleri tekilleştir."},
                {"title": "Üret", "desc": "Çok dilli taslaklar ve dahili klinisyen notları oluştur."},
                {"title": "Yayınla", "desc": "İnceleme sonrası portallar, yazdırmalar veya güvenli mesajlaşma."},
            ],
            "faq_title": "SSS — klinik",
            "faq": _faq_common_tr(),
        }
    )
    return t


def _page_hospitals_tr() -> Dict[str, Any]:
    t = copy.deepcopy(_page_hospitals_en())
    t.update(
        {
            "meta_title": "Hastaneler için Norya | Kurumsal laboratuvar dil katmanı",
            "meta_description": "Yönetişimle birlikte yatan, ayak ve bağlı ağlara kurumsal laboratuvar iletişim katmanı dağıtın.",
            "hero_badge": "Hastane sistemleri",
            "hero_title": "IDN'nizi terk eden her laboratuvar sonucu için tek model.",
            "hero_desc": "Hastane informatik ve klinik liderlik birleşik bir yardımcı katman elde eder: tutarlı terminoloji, yerelleştirilmiş varyantlar ve IDN satın alma standartlarına uygun SOC2 odaklı operasyon.",
            "who_title": "Ortaklarımız",
            "who_desc": "Kalite ile hızı hizalayan CMIO, CNIO, patoloji informatik ve gelir döngüsü liderleri.",
            "who_primary": "Entegre sunum ağları",
            "who_secondary": "Eğitim hastaneleri ve enstitüler",
            "who_points": ["Ulaşım programlı laboratuvar hizmetleri", "Hibrit on-prem / bulut stratejileri"],
            "benefits_title": "Sistem değeri",
            "benefits": [
                {
                    "title": "Risk bilincinde otomasyon",
                    "desc": "Açık yardımcı konumlandırması ile kısıtlanmış üretim.",
                    "points": ["Politika katmanları", "Yan dal uzman eskalasyonu", "Değişmez denetim günlükleri"],
                },
                {
                    "title": "Kampüsler arası tutarlılık",
                    "desc": "Dil, okuma seviyesi ve eskalasyon dilini senkronize edin.",
                    "points": ["Merkezi sözlük", "Bölgesel geçersiz kılmalar", "Epic/Cerner yakınlığı"],
                },
                {
                    "title": "Ölçülmüş mükemmellik",
                    "desc": "%98,7 biyomarker sınıflandırma doğruluğunu gösteren aynı iç platform değerlendirmesinden yararlanın.",
                    "points": ["Önce/sonra QA çalışmaları", "Biyomarker kapsam raporlama", "Hasta anlama pilotları"],
                },
                {
                    "title": "Satın almaya hazır özen",
                    "desc": "Kurumsal güvenlik dokümantasyonu ve klinik akışlar komite süreciniz için paketlenir.",
                    "points": ["BAA hazırlığı", "Pen-test özetleri", "Uygulama rehberi"],
                },
            ],
            "workflow_title": "Kurumsal yayılım",
            "workflow_steps": [
                {"title": "Hizala", "desc": "Servis hatları, diller ve veri yönlendirmesini kapsayan ortak tasarım oturumu."},
                {"title": "Entegre et", "desc": "Laboratuvar ara katmanı ve kimlik sağlayıcılara bağlantılar kurun."},
                {"title": "Doğrula", "desc": "Gösterge ve klinisyen örnekleme ile paralel çalıştırma."},
                {"title": "Ölçekle", "desc": "Kampüs, bağlı veya franchaise ortağına göre artımlı aktivasyon."},
            ],
            "faq_title": "SSS — hastane",
            "faq": _faq_common_tr(),
        }
    )
    return t


def _page_security_tr() -> Dict[str, Any]:
    t = copy.deepcopy(_page_security_en())
    t.update(
        {
            "meta_title": "Kurumsal güvenlik | Norya",
            "meta_description": "Norya yardımcı laboratuvar zekâ katmanını benimseyen ekipler için şifreleme, erişim kontrolleri ve satın alma dokümantasyonu.",
            "hero_badge": "Güvenlik ve uyum",
            "hero_title": "Sağlık satın almasına dayanan güvenlik mimarisi.",
            "hero_desc": "Norya düzenlenmiş ortamlar için geliştirildi: katmanlı veri işleme, en az ayrıcalık erişimi ve hastane ISO/SOC inceleme döngülerine uygun denetim izleri.",
            "who_title": "Desteklenen paydaşlar",
            "who_desc": "Her alt sistemi belgelemek zorunda olan CISO, tanı güvenliği ve sözleşme ekipleri.",
            "who_primary": "Sağlık kurumları",
            "who_secondary": "Tanı hizmet organizasyonları",
            "who_points": ["Bulut öncelikli ve hibrit ayak izleri", "Çok uluslu gizlilik danışmanlığı incelemeleri"],
            "benefits_title": "Kontrol alanları",
            "benefits": [
                {
                    "title": "Veri koruma",
                    "desc": "Aktarımda şifreme, kapsamlı saklama ve bölgesel işleme seçenekleri danışmanınızla incelenir.",
                    "points": ["TLS 1.2+", "Anahtar yönetimi rehberliği", "Yapılandırılabilir silme pencereleri"],
                },
                {
                    "title": "Erişim yönetişimi",
                    "desc": "Kurumsal SSO, ayrıntılı roller ve oturum politikaları.",
                    "points": ["SAML / OIDC yol haritası", "JIT kaynak desenleri", "Acil erişim prosedürleri"],
                },
                {
                    "title": "Güvence eserleri",
                    "desc": "Güvenlik paketi mimari diyagramlar, pen-test özetleri ve alt işlemcileri içerir.",
                    "points": ["SOC2 program uyumu", "DPA şablonları", "Olay müdahale runbookları"],
                },
                {
                    "title": "Klinik hizalama",
                    "desc": "Yardımcı çıktıların klinisyen döngüsünde kaldığını ifade edin.",
                    "points": ["Risk analiz notları", "Klinik güvenlik anlatıları", "Hukuk SSS"],
                },
            ],
            "workflow_title": "İnceleme nasıl ilerler",
            "workflow_steps": [
                {"title": "NDA ve kapsam", "desc": "Standart evrak alışverişi ve dağıtım topolojisi hizalaması."},
                {"title": "Mimari inceleme", "desc": "Veri akışları, şifreleme ve alt işlemciler üzerinden birlikte geçiş."},
                {"title": "Pilot", "desc": "Günlük ve izleme panoları ile sınırlı üretim."},
                {"title": "Ölçek kararı", "desc": "BAA/DPA ve yaygın yayılım için bölgesel yapılandırmaları kesinleştirin."},
            ],
            "faq_title": "Güvenlik SSS",
            "faq": _faq_common_tr(),
        }
    )
    return t


def _page_demo_tr() -> Dict[str, Any]:
    t = copy.deepcopy(_page_demo_en())
    t.update(
        {
            "meta_title": "Klinik demo | Norya akışı",
            "meta_description": "Laboratuvarların tek akışta yapılandırılmış veriden çok dilli incelemeye hazır açıklamalara nasıl aktığını görün.",
            "hero_badge": "Rehberli değerlendirme",
            "hero_title": "Gerçek klinik akış—laboratuvar dosyasından imzalı hasta kopyasına.",
            "hero_desc": "30 dakikada laboratuvar beslemelerinizi, dillerinizi ve inceleme modelinizi 50 ülke ve 4.000 hastane/klinikte kullanılan Norya boru hattına haritalıyoruz.",
            "who_title": "İdeal değerlendirme ekipleri",
            "who_desc": "Yardımcı araçları doğrulayan klinik inovasyon, laboratuvar direktörü ve dijital sağlık sponsorları.",
            "who_primary": "Disiplinler arası yönlendirme",
            "who_secondary": "Kalite ve hasta eğitimi sahipleri",
            "who_points": ["FY planlama için inovasyon bütçesi", "Çok dilli kanıt ihtiyacı"],
            "benefits_title": "Doğrulayacaklarınız",
            "benefits": [
                {
                    "title": "Uygulamalı boru hattı",
                    "desc": "Anonim örnekleri yükleyin; yapılandırma, açıklama ve inceleme adımlarını izleyin.",
                    "points": ["Gruplama doğruluğu", "Dil kalitesi", "Klinisyen UX"],
                },
                {
                    "title": "Metrik şeffaflığı",
                    "desc": "%98,7 biyomarker sınıflandırma doğruluğunu iç platform değerlendirmesi bağlamında açıklarız—tanı iddiası değildir.",
                    "points": ["Biyomarker QA", "Uç vaka tartışması", "Analitler için yol haritası"],
                },
                {
                    "title": "Paydaş setleri",
                    "desc": "Güvenlik SSS, klinik konumlandırma ve satın alma yolları ile ayrılın.",
                    "points": ["Slayt taslağı", "DPA kontrol listesi", "Entegrasyon önkoşulları"],
                },
                {
                    "title": "Sonraki adımlar",
                    "desc": "Pilot kapsamı, lisans ve başarı metrikleri tek oturumda.",
                    "points": ["Hacim varsayımları", "Lokalizasyon planı", "Eğitim yaklaşımı"],
                },
            ],
            "workflow_title": "Demo hikâyesi",
            "workflow_steps": [
                {"title": "Senaryo", "desc": "Temsil bir panel ve hasta bağlamı seçin."},
                {"title": "Al ve normalize et", "desc": "Tipik dışa aktarma biçiminizden eşleme gösterin."},
                {"title": "Üret", "desc": "İnceleme notlarıyla çok dilli taslaklar oluşturun."},
                {"title": "Soru-cevap", "desc": "Tıbbi, BT ve hukuk paydaşları için açık tartışma."},
            ],
            "faq_title": "Demo SSS",
            "faq": _faq_common_tr(),
        }
    )
    return t


PAGES_TR: Dict[str, Dict[str, Any]] = {
    "for-doctors": _page_doctors_tr(),
    "for-clinics": _page_clinics_tr(),
    "for-hospitals": _page_hospitals_tr(),
    "enterprise-security": _page_security_tr(),
    "clinical-demo": _page_demo_tr(),
}


# Hero + meta overlays for DE FR IT ES HE HI AR (rest inherits EN structure, FAQ stays EN unless tr)
_LANG_OVERLAY = {
    "for-doctors": {
        "de": {
            "meta_title": "Norya für Ärzt:innen | Laborklarheit in Minuten",
            "meta_description": "Assistierende Labor-zu-Sprache-Berichte: strukturierte Marker, einfache Sprache, prüfbereite Ausgaben in 9+ Sprachen.",
            "hero_badge": "Für Kliniker:innen",
            "hero_title": "Komplexe Labore patientenverständlich erklären—ohne Mehraufwand in der Verwaltung.",
            "hero_desc": "Norya verwandelt Standard-Laborexporte in zweisprachig vorbereitete, einfache Zusammenfassungen. Für Praxen mit hohem Laboraufkommen im Umfeld von 4.000+ Krankenhäusern und Kliniken.",
        },
        "fr": {
            "meta_title": "Norya pour les médecins | Clarité des analyses",
            "meta_description": "Rapports assistés laboratoire-langage : marqueurs structurés, langage simple, sortie prête à examen en 9+ langues.",
            "hero_badge": "Pour les cliniciens",
            "hero_title": "Expliquez des analyses complexes en langage patient—sans charge administrative supplémentaire.",
            "hero_desc": "Norya transforme les exports labo standard en résumés clairs, prêts pour le bilinguisme. Pour les pratiques à fort volume au sein de 4 000+ établissements.",
        },
        "it": {
            "meta_title": "Norya per medici | Chiarezza di laboratorio",
            "meta_description": "Report assistiti laboratorio-linguaggio: marker strutturati, linguaggio semplice, output pronto alla revisione in 9+ lingue.",
            "hero_badge": "Per clinici",
            "hero_title": "Spiegare laboratori complessi in linguaggio per il paziente—senza tempo amministrativo extra.",
            "hero_desc": "Norya trasforma gli export di laboratorio in riassunti chiari e pronti per il multilingue. Per studi ad alto volume nella rete di 4.000+ strutture.",
        },
        "es": {
            "meta_title": "Norya para médicos | Claridad de laboratorio",
            "meta_description": "Informes asistidos de laboratorio a lenguaje: marcadores estructurados, lenguaje sencillo, listo para revisión en 9+ idiomas.",
            "hero_badge": "Para clínicos",
            "hero_title": "Explique análisis complejos en lenguaje comprensible—sin carga administrativa extra.",
            "hero_desc": "Norya convierte exportaciones estándar en resúmenes claros y multilingües. Para prácticas de alto volumen en la red de 4.000+ hospitales y clínicas.",
        },
        "he": {
            "meta_title": "נוריאה לרופאים | בהירות במעבדה תוך דקות",
            "meta_description": "דוחות סיעוד ממעבדה לשפה: סמנים מובנים, שפה פשוטה, פלט מוכן לבדיקה ב־9+ שפות.",
            "hero_badge": "לקלינאים",
            "hero_title": "להסביר מעבדות מורכבות בשפה מותאמת למטופל—בלי עומס ניהולי נוסף.",
            "hero_desc": "נוריאה הופכת ייצוא מעבדה סטנדרטי לתקצירים ברורים, רבי־לשון. לקליניקות בעומס גבוה ברשת של 4,000+ בתי חולים ומרפאות.",
        },
        "hi": {
            "meta_title": "डॉक्टरों के लिए Norya | लैब स्पष्टता कुछ ही मिनटों में",
            "meta_description": "सहायक लैब-से-भाषा रिपोर्ट: संरचित मार्कर, साधारण भाषा, 9+ भाषाओं में समीक्षा-तैयार आउटपुट।",
            "hero_badge": "क्लिनिशियनों के लिए",
            "hero_title": "जटिल लैब को मरीज़-अनुकूल भाषा में समझाएँ—बिना अतिरिक्त प्रशासनिक बोझ के।",
            "hero_desc": "Norya मानक लैब निर्यात को द्विभाषा-तैयार सरल सार में बदलता है। 4,000+ अस्पतालों व क्लिनिक नेटवर्क में उच्च लैब वॉल्यूम वाले अभ्यासों के लिए।",
        },
        "ar": {
            "meta_title": "نوريا للأطباء | وضوح المختبر في دقائق",
            "meta_description": "تقارير مساعدة من المختبر إلى لغة المريض: مؤشرات منظّمة، لغة بسيطة، مخرجات جاهزة للمراجعة بأكثر من 9 لغات.",
            "hero_badge": "للكلينيين",
            "hero_title": "شرح تحاليل معقّدة بلغة يفهمها المريض—بدون زيادة عبء إداري.",
            "hero_desc": "تحوّل نوريا مخرجات المختبر القياسية إلى ملخصات واضحة ومتعددة اللغات. لعيادات ذات حجم كبير ضمن شبكة تضم أكثر من 4000 مستشفى وعيادة.",
        },
    },
    "for-clinics": {
        "de": {
            "meta_title": "Norya für Kliniken | Operative Laborkommunikation",
            "meta_description": "Patientennahe Laborerklärungen über Anbieter, Sprachen und Schichten standardisieren—ohne zusätzliches Personal.",
            "hero_badge": "Für Kliniken",
            "hero_title": "Ein Betriebsrhythmus für die Laborkommunikation in jeder Sprechstunde.",
            "hero_desc": "Eine Pipeline von Labs zu geprüften, mehrsprachigen Materialien. Skalieren Sie Qualität über 50+ Länder.",
        },
        "fr": {
            "meta_title": "Norya pour les cliniques | Communication labo",
            "meta_description": "Standardisez les explications des analyses pour les patients—sans embaucher davantage.",
            "hero_badge": "Pour les cliniques",
            "hero_title": "Un rythme opérationnel unique pour chaque salle de la clinique.",
            "hero_desc": "Une pipeline pour transformer les labs en supports multilingues prêts à examen. Même qualité dans 50+ pays.",
        },
        "it": {
            "meta_title": "Norya per le cliniche | Comunicazione di laboratorio",
            "meta_description": "Standardizzate le spiegazioni degli esami ai pazienti tra provider, lingue e turni senza aumentare il personale.",
            "hero_badge": "Per le cliniche",
            "hero_title": "Un solo ritmo operativo per la comunicazione di laboratorio in ogni stanza.",
            "hero_desc": "Un'unica pipeline verso materiali multilingue pronti alla revisione. Scalate la qualità in 50+ paesi.",
        },
        "es": {
            "meta_title": "Norya para clínicas | Comunicación de laboratorio",
            "meta_description": "Estandarice explicaciones de laboratorio al paciente entre proveedores, idiomas y turnos sin más personal.",
            "hero_badge": "Para clínicas",
            "hero_title": "Un solo ritmo operativo para la comunicación de laboratorio en toda la clínica.",
            "hero_desc": "Una tubería hacia material multilingue listo para revisión. La misma calidad en 50+ países.",
        },
        "he": {
            "meta_title": "נוריאה למרפאות | תקשורת מעבדה תפעולית",
            "meta_description": "סטנדרטיזציה של הסברי מעבדה למטופלים בין ספקים, שפות ומשמרות—בלי להגדיל כוח אדם.",
            "hero_badge": "למרפאות",
            "hero_title": "קצב תפעול אחד לתקשורת מעבדה בכל חדר במרפאה.",
            "hero_desc": "צינור אחד ממעבדה לחומר רב־לשוני מוכן לביקורת. אותה איכות ב־50+ מדינות.",
        },
        "hi": {
            "meta_title": "क्लिनिक के लिए Norya | परिचालन लैब संचार",
            "meta_description": "प्रदाता, भाषाओं और शिफ्टों में रोगी-उन्मुख लैब स्पष्टीकरण को मानकीकृत करें—बिना अतिरिक्त स्टाफ।",
            "hero_badge": "क्लिनिकों के लिए",
            "hero_title": "क्लिनिक की हर क्षेत्र में लैब संचार के लिए एक संचालन लय।",
            "hero_desc": "लैब से समीक्षा-तैय्यार बहुभाषी सामग्री तक एक पाइपलाइन। 50+ देशों में समान गुणवत्ता।",
        },
        "ar": {
            "meta_title": "نوريا للعيادات | تواصل المختبر التشغيلي",
            "meta_description": "توحيد شروحات المختبر للمرضى عبر مقدمي الخدمة واللغات والورديات—دون زيادة الموظفين.",
            "hero_badge": "للعيادات",
            "hero_title": "إيقاع تشغيلي واحد لتواصل المختبر في كل غرفة بالعيادة.",
            "hero_desc": "مسار واحد من نتائج المختبر إلى مواد متعددة اللغات جاهزة للمراجعة. نفس الجودة في أكثر من 50 دولة.",
        },
    },
    "for-hospitals": {
        "de": {
            "meta_title": "Norya für Krankenhäuser | Enterprise-Laborsprache",
            "meta_description": "Ein governance-fähiger Kommunikationslayer für stationäre, ambulante und verbundene Netzwerke.",
            "hero_badge": "Krankenhausverbünde",
            "hero_title": "Ein Governance-Modell für jede Laborergebnis-Linie Ihrer IDN.",
            "hero_desc": "Einheitliche Terminologie, lokalisierungen und SOC2-orientierter Betrieb für IDN-Beschaffung.",
        },
        "fr": {
            "meta_title": "Norya pour hôpitaux | Couche labo d'entreprise",
            "meta_description": "Déployez une couche de communication laboratoire avec gouvernance sur tous les réseaux.",
            "hero_badge": "Systèmes hospitaliers",
            "hero_title": "Un seul modèle de gouvernance pour chaque résultat quittant votre IDN.",
            "hero_desc": "Couche assistive unifiée : terminologie cohérente et exploitation alignée SOC2.",
        },
        "it": {
            "meta_title": "Norya per ospedali | Layer linguistico enterprise",
            "meta_description": "Distribuite comunicazione di laboratorio con governance su interni, esterni e reti affiliate.",
            "hero_badge": "Sistemi ospedalieri",
            "hero_title": "Un unico modello di governance per ogni risultato che lascia la vostra rete.",
            "hero_desc": "Terminologia coerente, varianti localizzate e operazioni orientate SOC2.",
        },
        "es": {
            "meta_title": "Norya para hospitales | Capa de lenguaje empresarial",
            "meta_description": "Despliegue comunicación de laboratorio con gobernanza en redes hospitalarias y afiliadas.",
            "hero_badge": "Sistemas hospitalarios",
            "hero_title": "Un solo modelo de gobernanza para cada resultado que sale de su IDN.",
            "hero_desc": "Capa asistiva unificada con terminología consistente y operación alineada a SOC2.",
        },
        "he": {
            "meta_title": "נוריאה לבתי חולים | שכבת שפה ארגונית",
            "meta_description": "פריסת שכבת תקשורת מעבדה עם ממשל על פני חולים פנימיים, חיצוניים ורשתות שותפות.",
            "hero_badge": "מערכות בתי חולים",
            "hero_title": "מודל ממשל אחיד לכל תוצאת מעבדה שיוצאת מה־IDN שלכם.",
            "hero_desc": "שכבה עוזרת מאוחדת: מונחים עקביים והפעלה בהתאם ל־SOC2.",
        },
        "hi": {
            "meta_title": "अस्पतालों के लिए Norya | एंटरप्राइज़ लैब भाषा परत",
            "meta_description": "भर्ती, बाह्य रोगी और सहयोगी नेटवर्क में गवर्नेंस सहित लैब संचार परत तैनात करें।",
            "hero_badge": "अस्पताल प्रणाली",
            "hero_title": "आपके IDN से निकलने वाले प्रत्येक लैब परिणाम के लिए एक गवर्नेंस मॉडल।",
            "hero_desc": "एकीकृत सहायक परत: सुसंगत शब्दावली, स्थानीयकृत संस्करण और SOC2-उन्मुख संचालन।",
        },
        "ar": {
            "meta_title": "نوريا للمستشفيات | طبقة لغة مؤسسية",
            "meta_description": "نشر طبقة تواصل مختبر مع حوكمة عبر المنومين والعيادات والشبكات التابعة.",
            "hero_badge": "أنظمة مستشفيات",
            "hero_title": "نموذج حوكمة واحد لكل نتيجة مختبر تغادر شبكتكم المتكاملة.",
            "hero_desc": "طبقة مساعدة موحّدة: مصطلحات ثابتة وعمليات بمواءمة SOC2.",
        },
    },
    "enterprise-security": {
        "de": {
            "meta_title": "Enterprise-Sicherheit | Norya",
            "meta_description": "Verschlüsselung, Zugriffskontrolle und Beschaffungsunterlagen für das assistierende Norya-Layer.",
            "hero_badge": "Sicherheit",
            "hero_title": "Sicherheitsarchitektur für Healthcare-Procurement.",
            "hero_desc": "Gestufte Datenverarbeitung, least privilege und Prüfpfade für ISO/SOC-Zyklen.",
        },
        "fr": {
            "meta_title": "Sécurité entreprise | Norya",
            "meta_description": "Chiffrement, contrôles d'accès et dossiers d'achat pour l'offre assistive Norya.",
            "hero_badge": "Sécurité",
            "hero_title": "Architecture de sécurité validée par les achats santé.",
            "hero_desc": "Traitement des données par niveaux, moindre privilège et pistes d'audit adaptées.",
        },
        "it": {
            "meta_title": "Sicurezza enterprise | Norya",
            "meta_description": "Crittografia, controlli di accesso e documentazione per l'adozione del layer assistito Norya.",
            "hero_badge": "Sicurezza",
            "hero_title": "Architettura di sicurezza per gli acquisti sanitari.",
            "hero_desc": "Gestione dei dati a livelli, privilegi minimi e audit per cicli ISO/SOC.",
        },
        "es": {
            "meta_title": "Seguridad empresarial | Norya",
            "meta_description": "Cifrado, controles de acceso y documentación de compras para la capa asistida de Norya.",
            "hero_badge": "Seguridad",
            "hero_title": "Arquitectura de seguridad apta para compras en salud.",
            "hero_desc": "Datos por capas, mínimo privilegio y huellas de auditoría para revisiones ISO/SOC.",
        },
        "he": {
            "meta_title": "אבטחה ארגונית | נוריאה",
            "meta_description": "הצפנה, בקרות גישה ותיעוד רכש לצוותים שמאמצים את שכבת נוריאה המסייעת.",
            "hero_badge": "אבטחה",
            "hero_title": "ארכיטקטורת אבטחה שעומדת ברכישה בבריאות.",
            "hero_desc": "טיפול רב-שכבתי בנתונים, הרשאות מינימליות ושבילי ביקורת ל־ISO/SOC.",
        },
        "hi": {
            "meta_title": "एंटरप्राइज़ सुरक्षा | Norya",
            "meta_description": "एन्क्रिप्शन, एक्सेस नियंत्रण और खरीद दस्तावेज़ — Norya सहायक परत अपनाने वाली टीमों के लिए।",
            "hero_badge": "सुरक्षा",
            "hero_title": "स्वास्थ्य खरीद को झेलने वाली सुरक्षा संरचना।",
            "hero_desc": "स्तरीय डेटा हैंडलिंग, न्यूनतम विशेषाधिकार और ISO/SOC समीक्षा चक्रों के लिए ऑडिट पथ।",
        },
        "ar": {
            "meta_title": "أمن المؤسسات | نوريا",
            "meta_description": "تشفير وضوابط وصول ووثائق توريد للفرق التي تعتمد طبقة نوريا المساعدة.",
            "hero_badge": "الأمن",
            "hero_title": "هندسة أمنية تلائم مشتريات الرعاية الصحية.",
            "hero_desc": "معالجة بيانات متدرجة وأقل امتيازًا ومسارات تدقيق لدورات ISO/SOC.",
        },
    },
    "clinical-demo": {
        "de": {
            "meta_title": "Klinische Demo | Norya-Workflow",
            "meta_description": "Vom strukturierten Labordatensatz zu mehrsprachigen, prüfbereiten Patientenerklärungen.",
            "hero_badge": "Evaluation",
            "hero_title": "Ein echter klinischer Workflow—Von der Labordatei bis zur unterzeichneten Patientenkopie.",
            "hero_desc": "In 30 Minuten mappen wir Feeds, Sprachen und Review-Modell auf die Norya-Pipeline in 50+ Ländern.",
        },
        "fr": {
            "meta_title": "Démo clinique | Flux Norya",
            "meta_description": "Des données structurées aux explications patient multilingues prêtes à examen.",
            "hero_badge": "Évaluation",
            "hero_title": "Un parcours clinique réel—du fichier labo à la copie patient signée.",
            "hero_desc": "En 30 minutes nous alignons flux, langues et revalidation sur le pipeline utilisé dans 50+ pays.",
        },
        "it": {
            "meta_title": "Demo clinica | Workflow Norya",
            "meta_description": "Da dati strutturati a spiegazioni per il paziente multilingue pronte alla revisione.",
            "hero_badge": "Valutazione guidata",
            "hero_title": "Un workflow clinico reale—dal file di laboratorio alla copia firmata.",
            "hero_desc": "In 30 minuti mappiamo feed, lingue e modello di review sulla pipeline in 50+ paesi.",
        },
        "es": {
            "meta_title": "Demo clínica | Flujo Norya",
            "meta_description": "De datos estructurados a explicaciones multilingües listas para revisión.",
            "hero_badge": "Evaluación guiada",
            "hero_title": "Flujo clínico real—desde el archivo de laboratorio hasta la copia firmada.",
            "hero_desc": "En 30 minutos alineamos feeds, idiomas y revisión con el pipeline en 50+ países.",
        },
        "he": {
            "meta_title": "הדגמה קלינית | זרימת נוריאה",
            "meta_description": "מנתונים מובנים להסברים רבי־לשון מוכנים לבדיקה.",
            "hero_badge": "הערכה מודרכת",
            "hero_title": "זרימה קלינית אמיתית—מקובץ מעבדה עד עותק חתום למטופל.",
            "hero_desc": "תוך 30 דקות מתאימים הזנות, שפות ומודל בדיקה לצינור בשימוש ב־50+ מדינות.",
        },
        "hi": {
            "meta_title": "क्लिनिकल डेमो | Norya वर्कफ़्लो",
            "meta_description": "संरचित डेटा से बहुभाषी, समीक्षा-तैय्यार मरीज़ स्पष्टीकरण तक एक वर्कफ़्लो।",
            "hero_badge": "मार्गदर्शित मूल्यांकन",
            "hero_title": "वास्तविक क्लिनिकल वर्कफ़्लो—लैब फ़ाइल से हस्ताक्षरित मरीज़ प्रति तक।",
            "hero_desc": "30 मिनट में हम आपके फ़ीड, भाषाओं और समीक्षा मॉडल को 50+ देशों में उपयोग होने वाली पाइपलाइन पर मैप करते हैं।",
        },
        "ar": {
            "meta_title": "عرض سريري | مسار نوريا",
            "meta_description": "من بيانات منظّمة إلى شروحات للمرضى بعدة لغات جاهزة للمراجعة.",
            "hero_badge": "تقييم موجّه",
            "hero_title": "مسار سريري حقيقي—من ملف المختبر إلى نسخة المريض الموقّعة.",
            "hero_desc": "خلال 30 دقيقة نربط مغذياتك ولغاتك ونموذج المراجعة بمسار العمل المستخدم في أكثر من 50 دولة.",
        },
    },
}


def get_b2b_audience_ui(slug: str, lang_code: str) -> Dict[str, Any]:
    lang = (lang_code or "en").strip().lower()
    if lang not in CTA_BY_LANG:
        lang = "en"
    if slug not in PAGE_PATHS:
        return {}
    if lang == "tr":
        out = copy.deepcopy(PAGES_TR[slug])
    else:
        out = copy.deepcopy(PAGES_EN[slug])
        if lang != "en":
            overlay = _LANG_OVERLAY.get(slug, {}).get(lang)
            if overlay:
                out.update(overlay)
    out.update(CTA_BY_LANG[lang])
    return out
