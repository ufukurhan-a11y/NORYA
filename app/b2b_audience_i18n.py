# pylint: disable=line-too-long
"""
B2B audience landing pages: shared copy for /for-doctors, /for-clinics, /for-hospitals,
/enterprise-security, /clinical-demo.
"""
from __future__ import annotations

import copy
from typing import Any, Dict

from app.b2b_locales import LOCALE_BUILDERS, get_full_locale_pages

FULL_LOCALE_LANGS = frozenset(LOCALE_BUILDERS.keys())
_FULL_LOCALE_CACHE: Dict[str, Dict[str, Dict[str, Any]]] = {}

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


def _for_clinics_faq_extras_en() -> list:
    return [
        {
            "q": "Will Norya replace our nurses or patient educators?",
            "a": "No. Norya produces assistive first drafts of lab explanations for clinicians to review and release. Education staffing stays focused on complex counseling; routing stays under your policies.",
        },
        {
            "q": "Can we centralize tone, disclaimers, and glossary terms?",
            "a": "Yes. Enterprise clinic programs lock language snippets, legal disclaimers, and biomarker glossaries so every room uses the same guardrails. Sales can map this to your governance model.",
        },
    ]


def _for_clinics_faq_extras_tr() -> list:
    return [
        {
            "q": "Norya hemşireleri veya hasta eğitimcilerimizin yerini alır mı?",
            "a": "Hayır. Norya, klinisyenlerin inceleyip yayınlayacağı laboratuvar açıklamaları için yardımcı ilk taslaklar üretir. Eğitim kadrosu karmaşık danışmanlıkta kalır; yönlendirme sizin politikalarınızda kalır.",
        },
        {
            "q": "Ton, feragatnameler ve sözlük terimlerini merkezileştirebilir miyiz?",
            "a": "Evet. Kurumsal klinik programları dil parçalarını, hukuki feragatları ve biyomarker sözlüklerini kilitleyerek her odanın aynı güvenlik bariyerlerini kullanmasını sağlar. Satış bunu yönetişim modelinize haritalar.",
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
                        "points": ["9+ report languages", "Versioned snippets", "Legal review checkpoints"],
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
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "Enterprise diagram of clinic locations connected to a unified lab explanation workflow",
            "caption": "Illustrative visual: one operating rhythm across rooms, providers, and languages—clinicians stay in the review path.",
        },
        "stats_strip": [
            {"value": "2M+", "label": "reports generated"},
            {"value": "4,000+", "label": "hospitals and clinics"},
            {"value": "50+", "label": "countries reached"},
            {"value": "9+", "label": "report languages"},
            {"value": "98.7%", "label": "biomarker classification accuracy"},
        ],
        "stats_disclaimer": "98.7% is biomarker classification accuracy from internal platform evaluation—not clinical diagnostic accuracy.",
        "modules_eyebrow": "Operational depth",
        "modules_title": "Modules operators run every week",
        "modules_desc": "Assistive drafting with clinician review at every step—designed to scale from a single clinic to regional groups without duplicating manual work.",
        "modules": [
            {
                "title": "Intake & orchestration",
                "desc": "Queue batched CSV/PDF exports, connector-ready feeds, and site metadata without rewriting your LIMS rhythm.",
            },
            {
                "title": "Language & policy layer",
                "desc": "Central glossary, disclaimers, and locale packs so every shift speaks with the same clinical and legal guardrails.",
            },
            {
                "title": "Ops telemetry",
                "desc": "Throughput, language coverage, and QA signals formatted for leadership dashboards and improvement cycles.",
            },
            {
                "title": "Security & procurement path",
                "desc": "Encryption in transit, enterprise SSO roadmap, and diligence packets aligned with hospital-grade reviews.",
            },
        ],
        "resources_eyebrow": "Continue the evaluation",
        "resources_title": "Pair this overview with diligence assets",
        "resources_desc": "Move from narrative to proof: security artifacts, a guided storyline, and corporate contracting in one place.",
        "resources": [
            {
                "title": "Clinical demo storyline",
                "desc": "Walk ingest, structuring, multilingual drafts, and clinician review with your multidisciplinary team.",
                "path": "/clinical-demo",
                "cta": "Open demo page",
            },
            {
                "title": "Enterprise security",
                "desc": "Architecture narratives, access models, and procurement-ready documentation for IT and legal reviewers.",
                "path": "/enterprise-security",
                "cta": "Review security",
            },
            {
                "title": "Trust center",
                "desc": "Methodology, transparency, and medical-review context that procurement teams expect alongside Norya.",
                "path": "/trust",
                "cta": "Visit Trust Center",
            },
            {
                "title": "Corporate programs",
                "desc": "Rollout planning, onboarding playbooks, and contracting paths for multi-site clinic groups.",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "Contact corporate",
            },
        ],
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
            "a": "50 ülkedeki ekiplere hizmet veriyoruz; 9+ rapor dilinde lokalizasyon sunulur.",
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
                    "points": ["9+ rapor dili", "Sürümlü parçalar", "Hukuk inceleme kontrol noktaları"],
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
            "hero_image": {
                "src": "/static/images/clinic-enterprise-visual.png",
                "alt": "Klinik lokasyonlarını birleşik laboratuvar açıklama akışına bağlayan kurumsal diyagram",
                "caption": "Örnek görsel: odalar, sağlayıcılar ve diller arasında tek ritim—inceleme yolu klinisyenlerde kalır.",
            },
            "stats_strip": [
                {"value": "2M+", "label": "üretilen rapor"},
                {"value": "4.000+", "label": "hastane ve klinik"},
                {"value": "50+", "label": "ulaşılan ülke"},
                {"value": "9+", "label": "rapor dili"},
                {"value": "%98,7", "label": "biyomarker sınıflandırma doğruluğu"},
            ],
            "stats_disclaimer": "%98,7 değeri iç platform değerlendirmesindeki biyomarker sınıflandırma doğruluğudur; klinik tanı doğruluğu değildir.",
            "modules_eyebrow": "Operasyonel derinlik",
            "modules_title": "Operatörlerin her hafta kullandığı modüller",
            "modules_desc": "Her adımda klinisyen incelemesi olan yardımcı taslaklar—tek merkezden bölgesel gruplara ölçeklenir, manuel iş yükünü çoğaltmaz.",
            "modules": [
                {
                    "title": "Alım ve orkestrasyon",
                    "desc": "LIMS ritminizi yeniden yazmadan toplu CSV/PDF dışa aktarımları, bağlayıcıya hazır beslemeler ve site meta verisini kuyruğa alın.",
                },
                {
                    "title": "Dil ve politika katmanı",
                    "desc": "Merkezi sözlük, feragatlar ve yerel paketlerle her vardiyanın aynı klinik ve hukuki bariyerlerle konuşmasını sağlayın.",
                },
                {
                    "title": "Operasyon telemetrisi",
                    "desc": "Liderlik panoları ve iyileştirme döngüleri için hacim, dil kapsamı ve QA sinyalleri.",
                },
                {
                    "title": "Güvenlik ve satın alma yolu",
                    "desc": "Aktarımda şifreleme, kurumsal SSO yol haritası ve hastane düzeyi incelemelerle uyumlu özen paketleri.",
                },
            ],
            "resources_eyebrow": "Değerlendirmeye devam",
            "resources_title": "Bu özeti özen varlıklarıyla eşleştirin",
            "resources_desc": "Anlatıdan kanıta: güvenlik eserleri, rehberli bir hikâye ve kurumsal sözleşme tek yerde.",
            "resources": [
                {
                    "title": "Klinik demo hikâyesi",
                    "desc": "Alım, yapılandırma, çok dilli taslaklar ve klinisyen incelemesini disiplinler arası ekibinizle adım adım ilerletin.",
                    "path": "/clinical-demo",
                    "cta": "Demo sayfasını aç",
                },
                {
                    "title": "Kurumsal güvenlik",
                    "desc": "BT ve hukuk inceleyicileri için mimari anlatılar, erişim modelleri ve satın almaya hazır dokümantasyon.",
                    "path": "/enterprise-security",
                    "cta": "Güvenliği incele",
                },
                {
                    "title": "Güven Merkezi",
                    "desc": "Yöntembilim, şeffaflık ve tıbbi inceleme bağlamı; satın alma ekiplerinin Norya ile beklediği içerik.",
                    "path": "/trust",
                    "cta": "Güven Merkezi",
                },
                {
                    "title": "Kurumsal programlar",
                    "desc": "Çok merkezli klinik grupları için yayılım planı, onboarding playbook ve sözleşme yolları.",
                    "path": "/kurumsal",
                    "fragment": "contact",
                    "cta": "Kurumsal iletişim",
                },
            ],
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

def _get_cached_full_locale_pages(lang: str) -> Dict[str, Dict[str, Any]]:
    if lang not in FULL_LOCALE_LANGS:
        return {}
    cached = _FULL_LOCALE_CACHE.get(lang)
    if cached is not None:
        return cached
    built = get_full_locale_pages(lang, PAGES_EN)
    _FULL_LOCALE_CACHE[lang] = built
    return built


_FOR_CLINICS_FAQ_EXTRAS: Dict[str, list] = {
    "en": _for_clinics_faq_extras_en(),
    "tr": _for_clinics_faq_extras_tr(),
    "de": [
        {
            "q": "Ersetzt Norya unsere Pflegekräfte oder Patientenedukator:innen?",
            "a": "Nein. Norya erstellt assistierende Erstentwürfe von Laborderklärungen zur ärztlichen Durchsicht und Freigabe. Die Edukationsbesetzung konzentriert sich weiter auf komplexe Beratung; Routing bleibt in Ihren Richtlinien.",
        },
        {
            "q": "Können wir Tonalität, Disclaimer und Glossar zentral steuern?",
            "a": "Ja. Enterprise-Klinikprogramme verankern Textbausteine, Disclaimer und Biomarker-Glossare, sodass jede Station dieselben Leitplanken nutzt. Der Vertrieb ordnet dies Ihrem Governance-Modell zu.",
        },
    ],
    "fr": [
        {
            "q": "Norya remplace-t-il nos infirmières ou éducateurs patients ?",
            "a": "Non. Norya produit des premiers jets assistés d’explications d’analyses à relire et publier par les cliniciens. L’équipe d’éducation reste sur le conseil complexe ; le routage suit vos politiques.",
        },
        {
            "q": "Pouvons-nous centraliser le ton, les clauses et le glossaire ?",
            "a": "Oui. Les programmes cliniques entreprise verrouillent extraits, clauses légales et glossaires biomarqueurs pour une même ligne de garde-fous. Les ventes peuvent l’aligner sur votre gouvernance.",
        },
    ],
    "es": [
        {
            "q": "¿Norya sustituye a nuestras enfermeras o educadoras de pacientes?",
            "a": "No. Norya genera borradores asistidos de explicaciones de laboratorio para revisión y publicación clínica. El equipo educativo sigue en consejería compleja; el enrutamiento queda bajo sus políticas.",
        },
        {
            "q": "¿Podemos centralizar tono, descargos de responsabilidad y glosario?",
            "a": "Sí. Los programas clínicos enterprise fijan fragmentos, descargos y glosarios de biomarcadores para que cada sala use las mismas barreras. Ventas puede alinearlo con su modelo de gobernanza.",
        },
    ],
    "it": [
        {
            "q": "Norya sostituisce infermieri o educatori dei pazienti?",
            "a": "No. Norya produce bozze assistite di spiegazioni di laboratorio per revisione e rilascio clinico. Il personale educativo resta sul counseling complesso; il percorso resta nelle vostre policy.",
        },
        {
            "q": "Possiamo centralizzare tono, disclaimer e glossario?",
            "a": "Sì. I programmi clinici enterprise bloccano snippet, disclaimer e glossari dei biomarcatori così ogni stanza usa gli stessi guardrail. Le vendite possono mapparlo sul vostro modello di governance.",
        },
    ],
    "he": [
        {
            "q": "האם Norya מחליף את האחיות או את צוות חינוך המטופלים שלנו?",
            "a": "לא. Norya מפיק טיוטות עזר להסברי מעבדה לבדיקה ופרסום קליני. צוות החינוך נשאר במיקוד בייעוץ מורכב; הניתוב נשאר במדיניות שלכם.",
        },
        {
            "q": "האם נוכל למרכז טון, כתבי ויתור ומונחי מילון?",
            "a": "כן. תוכניות קליניות ארגוניות נועלות קטעי שפה, כתבי ויתור ומילוני ביומרקרים כך שכל חדר משתמש באותן מגבלות. המכירות יכולות למפות זאת למודל הממשל שלכם.",
        },
    ],
    "hi": [
        {
            "q": "क्या Norya हमारी नर्सों या रोगी शिक्षकों की जगह लेगी?",
            "a": "नहीं। Norya प्रयोगशाला स्पष्टीकरण के लिए सहायक प्रारूप तैयार करता है जिनकी क्लिनिशियन समीक्षा करके जारी करते हैं। शिक्षा स्टाफ जटिल परामर्श पर केंद्रित रहता है; रूटिंग आपकी नीतियों के अंतर्गत रहती है।",
        },
        {
            "q": "क्या हम टोन, अस्वीकरण और शब्दावली को केंद्रीकृत कर सकते हैं?",
            "a": "हाँ। एंटरप्राइज क्लिनिक कार्यक्रम भाषा खंड, कानूनी अस्वीकरण और बायोमार्कर शब्दकोश लॉक करते हैं ताकि हर कक्ष समान सुरक्षा-रेल का उपयोग करे। सेल्स इसे आपके शासन मॉडल से मैप कर सकता है।",
        },
    ],
    "ar": [
        {
            "q": "هل تحلّ Norya محلّ ممرّضاتنا أو مُربّي المرضى؟",
            "a": "لا. تُنشئ Norya مسودات مساعدة لشرح نتائج المختبر لمراجعتها وإصدارها من قبل الطاقم السريري. يبقى فريق التثقيف مركزاً على الاستشارات المعقّدة؛ يبقى التوجيه وفق سياساتكم.",
        },
        {
            "q": "هل يمكننا توحيد النبرة وإخلاء المسؤولية والمصطلحات المعجمية؟",
            "a": "نعم. تثبّت برامج العيادات المؤسسية مقاطع النص وإخلاء المسؤولية القانونية ومسارد المؤشرات الحيوية ليستخدم كل غرفة نفس الحواجز. يمكن للمبيعات ربط ذلك بنموذج الحوكمة لديكم.",
        },
    ],
}

_FOR_CLINICS_LANG_PATCH: Dict[str, Dict[str, Any]] = {
    "de": {
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "Unternehmensdiagramm vernetzter Kliniken mit einem einheitlichen Laborkommunikations-Workflow",
            "caption": "Illustration: ein Betriebsrhythmus über Räume, Anbieter und Sprachen—ärztliche Prüfung bleibt Pflicht.",
        },
        "stats_strip": [
            {"value": "2M+", "label": "generierte Berichte"},
            {"value": "4.000+", "label": "Krankenhäuser und Kliniken"},
            {"value": "50+", "label": "erreichte Länder"},
            {"value": "9+", "label": "Berichtssprachen"},
            {"value": "98,7 %", "label": "Biomarker-Klassifikationsgenauigkeit"},
        ],
        "stats_disclaimer": "98,7 % bezieht sich auf die Biomarker-Klassifikation in der internen Plattformbewertung—nicht auf klinische diagnostische Genauigkeit.",
        "modules_eyebrow": "Operative Tiefe",
        "modules_title": "Module, die Betriebsteams wöchentlich nutzen",
        "modules_desc": "Assistierende Entwürfe mit ärztlicher Prüfung in jedem Schritt—skalierbar vom Einzelstandort bis zu regionalen Gruppen.",
        "modules": [
            {
                "title": "Aufnahme & Orchestrierung",
                "desc": "Stapel-CSV/PDF, connector-fähige Feeds und Standort-Metadaten ohne Umbau Ihres LIMS takten.",
            },
            {
                "title": "Sprach- und Policy-Schicht",
                "desc": "Zentrales Glossar, Disclaimer und Lokalisierungspakete für einheitliche klinische und rechtliche Leitplanken.",
            },
            {
                "title": "Ops-Telemetrie",
                "desc": "Durchsatz, Sprachabdeckung und QA-Signale für Führungs-Dashboards und Verbesserungszyklen.",
            },
            {
                "title": "Security- und Beschaffungspfad",
                "desc": "Verschlüsselung bei Übertragung, Enterprise-SSO-Roadmap und Diligence-Pakete auf Krankenhausniveau.",
            },
        ],
        "resources_eyebrow": "Nächste Schritte",
        "resources_title": "Vertiefung mit Prüfunterlagen",
        "resources_desc": "Vom Narrativ zum Nachweis: Security-Artefakte, geführter Ablauf und Enterprise-Vertragspfad an einem Ort.",
        "resources": [
            {
                "title": "Klinische Demo-Storyline",
                "desc": "Import, Strukturierung, mehrsprachige Entwürfe und ärztliche Prüfung mit Ihrem Team.",
                "path": "/clinical-demo",
                "cta": "Demo-Seite öffnen",
            },
            {
                "title": "Enterprise-Sicherheit",
                "desc": "Architektur, Zugriffsmodelle und beschaffungsreife Dokumentation für IT und Recht.",
                "path": "/enterprise-security",
                "cta": "Security prüfen",
            },
            {
                "title": "Trust Center",
                "desc": "Methodik, Transparenz und medizinischer Review-Kontext für Beschaffungsteams.",
                "path": "/trust",
                "cta": "Trust Center",
            },
            {
                "title": "Unternehmensprogramme",
                "desc": "Rollout, Onboarding-Playbooks und Vertragswege für multistandörtige Klinikgruppen.",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "Corporate kontaktieren",
            },
        ],
    },
    "fr": {
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "Schéma d’exploitation reliant des sites cliniques à un flux commun d’explications laboratoire",
            "caption": "Visuel illustratif : un rythme unique salles, praticiens et langues—la reprise clinicien reste obligatoire.",
        },
        "stats_strip": [
            {"value": "2M+", "label": "rapports générés"},
            {"value": "4 000+", "label": "hôpitaux et cliniques"},
            {"value": "50+", "label": "pays couverts"},
            {"value": "9+", "label": "langues de rapport"},
            {"value": "98,7 %", "label": "précision classification biomarqueurs"},
        ],
        "stats_disclaimer": "98,7 % = précision de classification des biomarqueurs dans notre évaluation interne—pas de précision diagnostique clinique.",
        "modules_eyebrow": "Profondeur opérationnelle",
        "modules_title": "Modules utilisés chaque semaine",
        "modules_desc": "Rédaction assistée avec relecture clinicien à chaque étape—du site unique au réseau régional.",
        "modules": [
            {
                "title": "Entrée & orchestration",
                "desc": "Files de CSV/PDF groupés, flux prêts connecteurs et métadonnées sans refonte LIMS.",
            },
            {
                "title": "Couche langue & politique",
                "desc": "Glossaire central, clauses et packs locaux pour les mêmes garde-fous cliniques et juridiques.",
            },
            {
                "title": "Télémétrie ops",
                "desc": "Débit, couverture linguistique et signaux QA pour tableaux de pilotage et cycles d’amélioration.",
            },
            {
                "title": "Sécurité & achats",
                "desc": "Chiffrement en transit, feuille de route SSO entreprise et dossiers alignés diligence hôpital.",
            },
        ],
        "resources_eyebrow": "Poursuivre l’évaluation",
        "resources_title": "Compléter avec les livrables diligence",
        "resources_desc": "Du récit à la preuve : sécurité, parcours guidé et voie contractuelle enterprise.",
        "resources": [
            {
                "title": "Démo clinique",
                "desc": "Parcourir ingestion, structuration, brouillons multilingues et relecture avec votre équipe.",
                "path": "/clinical-demo",
                "cta": "Ouvrir la démo",
            },
            {
                "title": "Sécurité entreprise",
                "desc": "Récits d’architecture, accès et documentation achat pour IT et juridique.",
                "path": "/enterprise-security",
                "cta": "Voir la sécurité",
            },
            {
                "title": "Trust Center",
                "desc": "Méthodologie, transparence et contexte revue médicale attendus en achat.",
                "path": "/trust",
                "cta": "Trust Center",
            },
            {
                "title": "Programmes corporate",
                "desc": "Déploiement, playbooks d’onboarding et contrats pour groupes multi-sites.",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "Contacter corporate",
            },
        ],
    },
    "es": {
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "Diagrama de clínicas conectadas a un flujo unificado de explicaciones de laboratorio",
            "caption": "Visual ilustrativa: un ritmo operativo en salas, proveedores e idiomas—la revisión clínica sigue siendo obligatoria.",
        },
        "stats_strip": [
            {"value": "2M+", "label": "informes generados"},
            {"value": "4.000+", "label": "hospitales y clínicas"},
            {"value": "50+", "label": "países alcanzados"},
            {"value": "9+", "label": "idiomas de informe"},
            {"value": "98,7%", "label": "precisión clasificación biomarcadores"},
        ],
        "stats_disclaimer": "98,7% es precisión de clasificación de biomarcadores en evaluación interna de plataforma—no precisión diagnóstica clínica.",
        "modules_eyebrow": "Profundidad operativa",
        "modules_title": "Módulos que operaciones usa cada semana",
        "modules_desc": "Borradores asistidos con revisión clínica en cada paso—de un centro a grupos regionales.",
        "modules": [
            {
                "title": "Ingesta y orquestación",
                "desc": "Colas de CSV/PDF por lotes, feeds listos para conectores y metadatos sin reescribir el LIMS.",
            },
            {
                "title": "Capa de idioma y política",
                "desc": "Glosario central, descargos y paquetes locales para las mismas barreras clínicas y legales.",
            },
            {
                "title": "Telemetría de ops",
                "desc": "Rendimiento, cobertura de idiomas y señales QA para cuadros de mando y ciclos de mejora.",
            },
            {
                "title": "Seguridad y compras",
                "desc": "Cifrado en tránsito, hoja de ruta SSO enterprise y paquetes de diligencia tipo hospital.",
            },
        ],
        "resources_eyebrow": "Siguiente fase",
        "resources_title": "Complementar con activos de diligencia",
        "resources_desc": "De la narrativa a la prueba: seguridad, historia guiada y vía contractual corporativa.",
        "resources": [
            {
                "title": "Historia de demo clínica",
                "desc": "Recorrer ingesta, estructura, borradores multilingües y revisión con su equipo.",
                "path": "/clinical-demo",
                "cta": "Abrir demo",
            },
            {
                "title": "Seguridad enterprise",
                "desc": "Narrativas de arquitectura y documentación para TI y legal.",
                "path": "/enterprise-security",
                "cta": "Ver seguridad",
            },
            {
                "title": "Trust Center",
                "desc": "Metodología, transparencia y contexto de revisión médica para compras.",
                "path": "/trust",
                "cta": "Trust Center",
            },
            {
                "title": "Programas corporativos",
                "desc": "Despliegue, playbooks de incorporación y contratación multi-sede.",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "Contactar corporate",
            },
        ],
    },
    "it": {
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "Diagramma di siti clinici collegati a un workflow unico di spiegazioni di laboratorio",
            "caption": "Immagine illustrativa: un ritmo operativo tra stanze, provider e lingue—la revisione clinica resta obbligatoria.",
        },
        "stats_strip": [
            {"value": "2M+", "label": "report generati"},
            {"value": "4.000+", "label": "ospedali e cliniche"},
            {"value": "50+", "label": "paesi raggiunti"},
            {"value": "9+", "label": "lingue di report"},
            {"value": "98,7%", "label": "accuratezza classificazione biomarcatori"},
        ],
        "stats_disclaimer": "98,7% è accuratezza di classificazione biomarcatori in valutazione interna della piattaforma—non accuratezza diagnostica clinica.",
        "modules_eyebrow": "Profondità operativa",
        "modules_title": "Moduli usati ogni settimana dagli operatori",
        "modules_desc": "Bozze assistite con revisione clinica ad ogni passo—da sito singolo a gruppi regionali.",
        "modules": [
            {
                "title": "Ingresso e orchestrazione",
                "desc": "Code di CSV/PDF batch, feed pronti per connettori e metadati senza riscrivere il LIMS.",
            },
            {
                "title": "Strato lingua e policy",
                "desc": "Glossario centrale, disclaimer e pacchetti locali per gli stessi guardrail clinici e legali.",
            },
            {
                "title": "Telemetria ops",
                "desc": "Throughput, copertura linguistica e segnali QA per dashboard direzionali e cicli di miglioramento.",
            },
            {
                "title": "Percorso sicurezza e acquisti",
                "desc": "Crittografia in transito, roadmap SSO enterprise e pacchetti di diligence da contesto ospedaliero.",
            },
        ],
        "resources_eyebrow": "Proseguire la valutazione",
        "resources_title": "Abbinare a materiali di diligence",
        "resources_desc": "Dal racconto alla prova: sicurezza, percorso guidato e contrattazione corporate.",
        "resources": [
            {
                "title": "Demo clinica",
                "desc": "Mostrare ingest, struttura, bozze multilingue e revisione con il team multidisciplinare.",
                "path": "/clinical-demo",
                "cta": "Apri demo",
            },
            {
                "title": "Sicurezza enterprise",
                "desc": "Narrazioni architetturali e documentazione procurement per IT e legal.",
                "path": "/enterprise-security",
                "cta": "Vedi sicurezza",
            },
            {
                "title": "Trust Center",
                "desc": "Metodologia, trasparenza e contesto di medical review per gli acquisti.",
                "path": "/trust",
                "cta": "Trust Center",
            },
            {
                "title": "Programmi corporate",
                "desc": "Rollout, playbook di onboarding e percorsi contrattuali per gruppi multi-sede.",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "Contatta corporate",
            },
        ],
    },
    "he": {
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "תרשים ארגוני של מרכזים קליניים המחוברים למסלול הסברי מעבדה אחיד",
            "caption": "איור להמחשה: קצב תפעול אחד בין חדרים, ספקים ושפות—הבדיקה הקלינית נשארת חובה.",
        },
        "stats_strip": [
            {"value": "2M+", "label": "דוחות שיוצרו בפלטפורמה"},
            {"value": "4,000+", "label": "בתי חולים ומרפאות"},
            {"value": "50+", "label": "מדינות נחתו"},
            {"value": "9+", "label": "שפות דו״ח"},
            {"value": "98.7%", "label": "דיוק סיווג ביומרקרים"},
        ],
        "stats_disclaimer": "98.7% מתייחס לדיוק סיווג ביומרקרים בהערכת פלטפורמה פנימית—לא לדיוק אבחנה קלינית.",
        "modules_eyebrow": "עומק תפעולי",
        "modules_title": "מודולים שהמפעילים משתמשים בהם מדי שבוע",
        "modules_desc": "טיוטות עזר עם בדיקה קלינית בכל שלב—מבנה שניתן להרחבה ממרפאה בודדת לקבוצות אזוריות.",
        "modules": [
            {
                "title": "קליטה ותזמור",
                "desc": "תורים של ייצוא CSV/PDF בקבוצות, הזנות מוכנות למחברים ומטא-נתוני אתר בלי לשכתב את תהליך ה-LIMS.",
            },
            {
                "title": "שכבת שפה ומדיניות",
                "desc": "מונחון מרכזי, כתבי ויתור וחבילות לוקליזציה כדי שכל משמרת תעבוד עם אותן מגבלות קליניות ומשפטיות.",
            },
            {
                "title": "טלמטריית תפעול",
                "desc": "תפוקה, כיסוי שפות ואותות QA מעוצבים ללוחות בקרה להנהלה ולמחזורי שיפור.",
            },
            {
                "title": "מסלול אבטחה ורכש",
                "desc": "הצפנה במעבר, מפת דרכים ל-SSO ארגוני וחבילות בדיקת נאותות ברמת בית חולים.",
            },
        ],
        "resources_eyebrow": "שלבים הבאים",
        "resources_title": "העמקה עם חומרי בדיקת נאותות",
        "resources_desc": "מסיפור לראיה: אבטחה, מסלול מודרך וחוזה ארגוני במקום אחד.",
        "resources": [
            {
                "title": "סיפור דמו קליני",
                "desc": "קליטה, מבנה, טיוטות רב-לשוניות ובדיקה קלינית עם הצוות הרב-תחומי שלכם.",
                "path": "/clinical-demo",
                "cta": "לפתיחת עמוד הדמו",
            },
            {
                "title": "אבטחה ארגונית",
                "desc": "תיאורי ארכיטקטורה, מודלי גישה ותיעוד מוכן לרכש עבור IT ומשפטים.",
                "path": "/enterprise-security",
                "cta": "סקירת אבטחה",
            },
            {
                "title": "מרכז האמון",
                "desc": "מתודולוגיה, שקיפות והקשר לבדיקה רפואית שצוותי רכש מצפים לו לצד Norya.",
                "path": "/trust",
                "cta": "מרכז האמון",
            },
            {
                "title": "תוכניות ארגוניות",
                "desc": "הרצה, ספריי קליטה ומסלולי חוזים לקבוצות קליניות רב-אתריות.",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "צרו קשר ארגוני",
            },
        ],
    },
    "hi": {
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "क्लिनिक स्थानों को एकीकृत लैब व्याख्या वर्कफ़्लो से जोड़ता उद्यम आरेख",
            "caption": "चित्रात्मक: कमरों, प्रदाताओं और भाषाओं में एक संचालन लय—क्लिनिशियन समीक्षा अनिवार्य रहती है।",
        },
        "stats_strip": [
            {"value": "2M+", "label": "जेनरेट किए गए रिपोर्ट"},
            {"value": "4,000+", "label": "अस्पताल और क्लिनिक"},
            {"value": "50+", "label": "देशों तक पहुँच"},
            {"value": "9+", "label": "रिपोर्ट भाषाएँ"},
            {"value": "98.7%", "label": "बायोमार्कर वर्गीकरण सटीकता"},
        ],
        "stats_disclaimer": "98.7% आंतरिक प्लेटफ़ॉर्म मूल्यांकन में बायोमार्कर वर्गीकरण सटीकता है—क्लिनिक निदान सटीकता नहीं।",
        "modules_eyebrow": "संचालन गहराई",
        "modules_title": "मॉड्यूल जो ऑपरेटर हर सप्ताह चलाते हैं",
        "modules_desc": "हर चरण पर क्लिनिशियन समीक्षा के साथ सहायक ड्राफ़्ट—एक साइट से क्षेत्रीय समूहों तक स्केल करने के लिए।",
        "modules": [
            {
                "title": "इनटेक और ऑर्केस्ट्रेशन",
                "desc": "बैच CSV/PDF निर्यात, कनेक्टर-तैयार फीड और साइट मेटाडेटा—LIMS वर्कफ़्लो फिर से लिखे बिना।",
            },
            {
                "title": "भाषा और नीति परत",
                "desc": "केंद्रीय शब्दकोश, अस्वीकरण और लोकेल पैक ताकि हर शिफ्ट वही क्लिनिकल और कानूनी गार्डरेल उपयोग करे।",
            },
            {
                "title": "ऑप्स टेलीमेटरी",
                "desc": "थ्रूपुट, भाषा कवरेज और QA संकेत—नेतृत्व डैशबोर्ड और सुधार चक्रों के लिए।",
            },
            {
                "title": "सुरक्षा और खरीद पथ",
                "desc": "ट्रांज़िट में एन्क्रिप्शन, एंटरप्राइज SSO रोडमैप और अस्पताल-स्तर की ड्यू डिलिजेंस पैकेज।",
            },
        ],
        "resources_eyebrow": "आगे का मूल्यांकन",
        "resources_title": "ड्यू डिलिजेंस सामग्री के साथ जोड़ें",
        "resources_desc": "कथा से प्रमाण: सुरक्षा, मार्गदर्शित कहानी और कॉर्पोटेट अनुबंध एक ही जगह।",
        "resources": [
            {
                "title": "क्लिनिकल डेमो कहानी",
                "desc": "अंतःविषय टीम के साथ इनजेस्ट, संरचना, बहुभाषी ड्राफ़्ट और क्लिनिशियन समीक्षा।",
                "path": "/clinical-demo",
                "cta": "डेमो पेज खोलें",
            },
            {
                "title": "एंटरप्राइज सुरक्षा",
                "desc": "आर्किटेक्चर कथन, एक्सेस मॉडल और IT/कानूनी समीक्षकों के लिए खरीद-तैयार दस्तावेज़।",
                "path": "/enterprise-security",
                "cta": "सुरक्षा देखें",
            },
            {
                "title": "ट्रस्ट सेंटर",
                "desc": "कार्यप्रणाली, पारदर्शिता और मेडिकल-रिव्यू संदर्भ जो क्रय टीमें Norya के साथ अपेक्षा करती हैं।",
                "path": "/trust",
                "cta": "ट्रस्ट सेंटर",
            },
            {
                "title": "कॉर्पोरेट कार्यक्रम",
                "desc": "मल्टी-साइट क्लिनिक समूहों के लिए रोलआउट, ऑनबोर्डिंग प्लेबुक और अनुबंध पथ।",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "कॉर्पोरेट संपर्क",
            },
        ],
    },
    "ar": {
        "hero_image": {
            "src": "/static/images/clinic-enterprise-visual.png",
            "alt": "مخطط مؤسسي يربط مواقع العيادات بمسار موحّد لشرح نتائج المختبر",
            "caption": "صورة توضيحية: إيقاع تشغيلي واحد عبر الغرف والمزوّدين واللغات—تبقى المراجعة السريرية إلزامية.",
        },
        "stats_strip": [
            {"value": "2M+", "label": "تقارير مُنشأة"},
            {"value": "4,000+", "label": "مستشفيات وعيادات"},
            {"value": "50+", "label": "دول تم الوصول إليها"},
            {"value": "9+", "label": "لغات التقرير"},
            {"value": "98.7%", "label": "دقة تصنيف المؤشرات الحيوية"},
        ],
        "stats_disclaimer": "98.7% هي دقة تصنيف المؤشرات الحيوية في تقييم المنصة الداخلي—وليست دقة تشخيصية سريرية.",
        "modules_eyebrow": "عمق تشغيلي",
        "modules_title": "وحدات يستخدمها المشغّلون أسبوعياً",
        "modules_desc": "مسودات مساعدة مع مراجعة سريرية في كل خطوة—قابلة للتوسع من موقع واحد إلى مجموعات إقليمية.",
        "modules": [
            {
                "title": "الاستقبال والتنسيق",
                "desc": "طوابير تصدير CSV/PDF المجمّعة، وتغذيات جاهزة للموصلات وبيانات وصفية للموقع دون إعادة كتابة سير عمل LIMS.",
            },
            {
                "title": "طبقة اللغة والسياسة",
                "desc": "معجم مركزي وإخلاء مسؤولية وحزم توطين بحيث يستخدم كل نوبة نفس الحواجز السريرية والقانونية.",
            },
            {
                "title": "قياسات التشغيل",
                "desc": "معدلات الإنتاج وتغطية اللغة وإشارات ضبط الجودة منسّقة للوحات القيادة ودورات التحسين.",
            },
            {
                "title": "مسار الأمن والمشتريات",
                "desc": "تشفير أثناء النقل وخارطة طريق SSO مؤسسية وحزم عناية واجبة بمستوى المستشفى.",
            },
        ],
        "resources_eyebrow": "مواصلة التقييم",
        "resources_title": "أكمل مع أصول العناية الواجبة",
        "resources_desc": "من السرد إلى الدليل: الأمن، مسار موجّه وعقد مؤسسي في مكان واحد.",
        "resources": [
            {
                "title": "سردية العرض السريري",
                "desc": "استقبل البيانات، البنية، المسودات متعددة اللغات والمراجعة السريرية مع فريقكم متعدد التخصصات.",
                "path": "/clinical-demo",
                "cta": "فتح صفحة العرض",
            },
            {
                "title": "الأمن المؤسسي",
                "desc": "سرديات البنية ونماذج الوصول وتوثيق جاهز للمشتريات لفرق تقنية المعلومات والقانون.",
                "path": "/enterprise-security",
                "cta": "مراجعة الأمن",
            },
            {
                "title": "مركز الثقة",
                "desc": "المنهجية والشفافية وسياق المراجعة الطبية التي تتوقعها فرق المشتريات إلى جانب Norya.",
                "path": "/trust",
                "cta": "مركز الثقة",
            },
            {
                "title": "البرامج المؤسسية",
                "desc": "خطة الإطلاق وأدلة الإدماج ومسارات التعاقد لمجموعات عيادات متعددة المواقع.",
                "path": "/kurumsal",
                "fragment": "contact",
                "cta": "تواصل مؤسسي",
            },
        ],
    },
}


def _clinic_seo_resource_cards(lang: str) -> list[dict[str, Any]]:
    """Locale-aware patient/education tiles appended to /for-clinics resources (SEO paths)."""
    code = (lang or "en").strip().lower()
    if code not in CTA_BY_LANG:
        code = "en"
    rows = _CLINIC_SEO_RESOURCES.get(code) or _CLINIC_SEO_RESOURCES["en"]
    return [dict(x) for x in rows]


# Extra resource tiles: hrefs resolved via localized_b2b_resource_url (locale-prefixed paths).
_CLINIC_SEO_RESOURCES: Dict[str, list[dict[str, Any]]] = {
    "en": [
        {
            "seo_link": "hub",
            "title": "Blood test results hub",
            "desc": "Reference ranges, units, and how to read high/low patterns—useful collateral for front-desk and portal copy.",
            "cta": "Open hub",
        },
        {
            "seo_link": "explained",
            "title": "Blood test results explained",
            "desc": "Plain-language context for panels and flagged values your teams can mirror in discharge education.",
            "cta": "Open explainer",
        },
        {
            "seo_link": "upload",
            "title": "Upload blood test results",
            "desc": "Show patients the structured intake flow behind multilingual drafts and clinician review.",
            "cta": "See upload",
        },
        {
            "seo_link": "analyzer",
            "title": "AI blood test analyzer",
            "desc": "Product-shaped workflow for lab reports—not generic chat—when you brief clinical IT.",
            "cta": "View analyzer",
        },
        {
            "seo_link": "cbc",
            "title": "How to read CBC results",
            "desc": "Pillar guide on WBC, RBC, hemoglobin, hematocrit, and platelets for standardized patient education.",
            "cta": "Open CBC guide",
        },
        {
            "seo_link": "faq",
            "title": "Blood test analysis FAQ",
            "desc": "Methodology boundaries, languages, and what the platform does not replace in care delivery.",
            "cta": "Read FAQ",
        },
    ],
    "tr": [
        {
            "seo_link": "hub",
            "title": "Kan tahlili sonuçları merkezi",
            "desc": "Referans aralıkları, birimler ve yüksek/düşük yorumlar—önbüro ve portal metinleri için referans.",
            "cta": "Merkeze git",
        },
        {
            "seo_link": "explained",
            "title": "Kan tahlili sonuçları açıklandı",
            "desc": "Paneller ve işaretli değerler için sade dil bağlamı; taburcu eğitiminde aynı çerçeveyi kullanın.",
            "cta": "Açıklamayı aç",
        },
        {
            "seo_link": "upload",
            "title": "Kan tahlili sonuçlarını yükle",
            "desc": "Çok dilli taslaklar ve klinisyen incelemesi arkasındaki yapılandırılmış alım akışını gösterin.",
            "cta": "Yükleme sayfası",
        },
        {
            "seo_link": "analyzer",
            "title": "Yapay zekâ kan tahlili analizi",
            "desc": "Klinik BT brifingleri için sohbet değil, laboratuvar raporuna uygun ürün akışı.",
            "cta": "Analizörü gör",
        },
        {
            "seo_link": "cbc",
            "title": "Tam kan sayımı nasıl okunur",
            "desc": "WBC, RBC, hemoglobin, hematokrit ve trombosit için standart hasta eğitimi rehberi.",
            "cta": "TİT rehberi",
        },
        {
            "seo_link": "faq",
            "title": "Kan tahlili analizi SSS",
            "desc": "Yöntembilim sınırları, diller ve platformun bakımda yerini almadığı alanlar.",
            "cta": "SSS’yi oku",
        },
    ],
    "de": [
        {
            "seo_link": "hub",
            "title": "Blutwerte-Hub",
            "desc": "Referenzbereiche, Einheiten und Hoch/Tief-Muster—Referenz für Empfang und Portaltexte.",
            "cta": "Hub öffnen",
        },
        {
            "seo_link": "explained",
            "title": "Blutwerte erklärt",
            "desc": "Klartext-Kontext für Profile und auffällige Werte, den Sie in Aufklärung übernehmen können.",
            "cta": "Erklärung öffnen",
        },
        {
            "seo_link": "upload",
            "title": "Blutwerte hochladen",
            "desc": "Zeigen Sie Patientinnen den strukturierten Import hinter mehrsprachigen Entwürfen und ärztlicher Prüfung.",
            "cta": "Upload ansehen",
        },
        {
            "seo_link": "analyzer",
            "title": "KI-Blutanalyse",
            "desc": "Produktorientierter Ablauf für Laborberichte—für IT- und Klinik-Briefings.",
            "cta": "Analyzer ansehen",
        },
        {
            "seo_link": "cbc",
            "title": "CBC-Befunde lesen",
            "desc": "Leitfaden zu Leukozyten, Erythrozyten, Hämoglobin, Hämatokrit und Thrombozyten.",
            "cta": "CBC-Guide",
        },
        {
            "seo_link": "faq",
            "title": "FAQ zur Blutanalyse",
            "desc": "Methodik-Grenzen, Sprachen und was die Plattform in der Versorgung nicht ersetzt.",
            "cta": "FAQ lesen",
        },
    ],
    "fr": [
        {
            "seo_link": "hub",
            "title": "Pilier résultats analyses",
            "desc": "Valeurs de référence, unités et lectures haut/bas—support pour accueil et portail.",
            "cta": "Voir le pilier",
        },
        {
            "seo_link": "explained",
            "title": "Résultats d’analyses expliqués",
            "desc": "Contexte accessible pour bilans et valeurs signalées, aligné avec l’éducation patient.",
            "cta": "Voir l’explicateur",
        },
        {
            "seo_link": "upload",
            "title": "Téléverser ses analyses",
            "desc": "Le parcours d’import structuré derrière brouillons multilingues et reprise clinique.",
            "cta": "Voir l’upload",
        },
        {
            "seo_link": "analyzer",
            "title": "Analyseur IA des analyses",
            "desc": "Parcours produit pour rapports de labo—pas un chat générique—pour brief IT/clinique.",
            "cta": "Voir l’outil",
        },
        {
            "seo_link": "cbc",
            "title": "Lire une numération",
            "desc": "GB, GR, hémoglobine, hématocrite, plaquettes—guide pédagogique unifié.",
            "cta": "Guide NFS",
        },
        {
            "seo_link": "faq",
            "title": "FAQ analyses sanguines",
            "desc": "Limites méthodologiques, langues et ce que la plateforme ne remplace pas.",
            "cta": "Lire la FAQ",
        },
    ],
    "es": [
        {
            "seo_link": "hub",
            "title": "Centro resultados de análisis",
            "desc": "Rangos de referencia, unidades y patrones alto/bajo—material para recepción y portal.",
            "cta": "Abrir centro",
        },
        {
            "seo_link": "explained",
            "title": "Resultados de análisis explicados",
            "desc": "Contexto claro para paneles y valores marcados, alineado con educación al alta.",
            "cta": "Ver explicador",
        },
        {
            "seo_link": "upload",
            "title": "Subir resultados de análisis",
            "desc": "El flujo de ingesta estructurada detrás de borradores multilingües y revisión clínica.",
            "cta": "Ver carga",
        },
        {
            "seo_link": "analyzer",
            "title": "Analizador IA de análisis",
            "desc": "Flujo de producto para informes de laboratorio—no chat genérico—para IT clínico.",
            "cta": "Ver analizador",
        },
        {
            "seo_link": "cbc",
            "title": "Cómo leer el hemograma",
            "desc": "Leucocitos, eritrocitos, hemoglobina, hematocrito y plaquetas—guía unificada.",
            "cta": "Guía CBC",
        },
        {
            "seo_link": "faq",
            "title": "Preguntas frecuentes análisis",
            "desc": "Límites metodológicos, idiomas y qué no sustituye la plataforma en la atención.",
            "cta": "Leer FAQ",
        },
    ],
    "it": [
        {
            "seo_link": "hub",
            "title": "Hub risultati esami del sangue",
            "desc": "Range di riferimento, unità e interpretazione alto/basso—supporto per accettazione e portale.",
            "cta": "Apri hub",
        },
        {
            "seo_link": "explained",
            "title": "Risultati spiegati",
            "desc": "Contesto in linguaggio semplice per pannelli e valori evidenziati, allineato all’educazione.",
            "cta": "Apri spiegazione",
        },
        {
            "seo_link": "upload",
            "title": "Carica referti",
            "desc": "Il flusso di ingestione strutturata dietro bozze multilingue e revisione clinica.",
            "cta": "Vedi upload",
        },
        {
            "seo_link": "analyzer",
            "title": "Analizzatore IA",
            "desc": "Percorso prodotto per referti di laboratorio—non chat generica—per briefing clinico/IT.",
            "cta": "Vedi analizzatore",
        },
        {
            "seo_link": "cbc",
            "title": "Leggere l’emocromo",
            "desc": "WBC, RBC, emoglobina, ematocrito, piastrine—guida unificata.",
            "cta": "Guida CBC",
        },
        {
            "seo_link": "faq",
            "title": "FAQ analisi del sangue",
            "desc": "Limiti metodologici, lingue e cosa la piattaforma non sostituisce nella cura.",
            "cta": "Leggi FAQ",
        },
    ],
    "he": [
        {
            "seo_link": "hub",
            "title": "מרכז תוצאות בדיקות דם",
            "desc": "טווחי ערכי התייחסות, יחידות ודפוסי גבוה/נמוך—חומר לקבלה ולפורטל.",
            "cta": "למרכז",
        },
        {
            "seo_link": "explained",
            "title": "תוצאות בדיקות דם מוסברות",
            "desc": "הקשר בשפה פשוטה לפאנלים ולערכים מסומנים—מתאים להנחיות שחרור.",
            "cta": "למספר המסביר",
        },
        {
            "seo_link": "upload",
            "title": "העלאת תוצאות בדיקות דם",
            "desc": "תהליך הקליטה המובנה מאחורי טיוטות רב־לשוניות ובדיקה קלינית.",
            "cta": "לעמוד העלאה",
        },
        {
            "seo_link": "analyzer",
            "title": "מנתח בדיקות דם מבוסס בינה מלאכותית",
            "desc": "זרימת מוצר לדוחות מעבדה—לא צ׳אט כללי—לתיאום עם מערכות מידע.",
            "cta": "למנתח",
        },
        {
            "seo_link": "cbc",
            "title": "איך לקרוא ספירת דם מלאה",
            "desc": "תאי דם לבנים ואדומים, המוגלובין, המטוקריט וטסיות—מדריך אחיד.",
            "cta": "מדריך CBC",
        },
        {
            "seo_link": "faq",
            "title": "שאלות נפוצות — ניתוח בדיקות דם",
            "desc": "גבולות מתודולוגיה, שפות ומה שהפלטפורמה אינה מחליפה בטיפול.",
            "cta": "לשאלות נפוצות",
        },
    ],
    "hi": [
        {
            "seo_link": "hub",
            "title": "ब्लड टेस्ट परिणाम केंद्र",
            "desc": "संदर्भ सीमाएँ, इकाइयाँ और उच्च/निम्न पैटर्न—रिसेप्शन और पोर्टल के लिए संदर्भ.",
            "cta": "केंद्र खोलें",
        },
        {
            "seo_link": "explained",
            "title": "ब्लड टेस्ट परिणाम समझाया गया",
            "desc": "पैनल और चिह्नित मानों के लिए साधारण भाषा संदर्भ—डिस्चार्ज शिक्षा के अनुरूप.",
            "cta": "व्याख्या खोलें",
        },
        {
            "seo_link": "upload",
            "title": "ब्लड टेस्ट परिणाम अपलोड करें",
            "desc": "बहुभाषी ड्राफ़्ट और क्लिनिशियन समीक्षा के पीछे संरचित इनटेक प्रवाह.",
            "cta": "अपलोड देखें",
        },
        {
            "seo_link": "analyzer",
            "title": "AI ब्लड टेस्ट विश्लेषक",
            "desc": "लैब रिपोर्ट के लिए उत्पाद-शीर्ष वर्कफ़्लो—सामान्य चैट नहीं—IT ब्रीफ़िंग के लिए.",
            "cta": "विश्लेषक देखें",
        },
        {
            "seo_link": "cbc",
            "title": "CBC परिणाम कैसे पढ़ें",
            "desc": "WBC, RBC, हीमोग्लोबिन, हेमैटोक्रिट, प्लेटलेट्स—एकीकृत मरीज़ शिक्षा गाइड.",
            "cta": "CBC गाइड",
        },
        {
            "seo_link": "faq",
            "title": "ब्लड टेस्ट विश्लेषण FAQ",
            "desc": "कार्यप्रणाली सीमाएँ, भाषाएँ और मंच देखभाल में क्या नहीं बदलता.",
            "cta": "FAQ पढ़ें",
        },
    ],
    "ar": [
        {
            "seo_link": "hub",
            "title": "مركز نتائج تحاليل الدم",
            "desc": "المرجعيات والوحدات وأنماط الارتفاع/الانخفاض—مرجع للاستقبال والبوابة.",
            "cta": "افتح المركز",
        },
        {
            "seo_link": "explained",
            "title": "شرح نتائج تحاليل الدم",
            "desc": "سياق مبسّط لللوحات والقيم المُعلّمة، متوافق مع توعية المرضى عند الخروج.",
            "cta": "افتح الشرح",
        },
        {
            "seo_link": "upload",
            "title": "رفع نتائج تحاليل الدم",
            "desc": "تدفق الاستقبال المهيكل وراء المسودات متعددة اللغات والمراجعة السريرية.",
            "cta": "صفحة الرفع",
        },
        {
            "seo_link": "analyzer",
            "title": "محلّل تحاليل الدم بالذكاء الاصطناعي",
            "desc": "مسار منتج لتقارير المختبر—ليست دردشة عامة—لإحاطة تقنية المعلومات السريرية.",
            "cta": "المحلّل",
        },
        {
            "seo_link": "cbc",
            "title": "كيف تقرأ نتائج تعداد الدم الكامل",
            "desc": "كريات بيضاء وحمراء، الهيموغلوبين، الهيماتوكريت والصفائح—دليل تثقيف موحّد.",
            "cta": "دليل CBC",
        },
        {
            "seo_link": "faq",
            "title": "الأسئلة الشائعة حول تحليل الدم",
            "desc": "حدود المنهجية واللغات وما لا تستبدله المنصّة في الرعاية.",
            "cta": "اقرأ الأسئلة الشائعة",
        },
    ],
}


def get_b2b_audience_ui(slug: str, lang_code: str) -> Dict[str, Any]:
    lang = (lang_code or "en").strip().lower()
    if lang not in CTA_BY_LANG:
        lang = "en"
    if slug not in PAGE_PATHS:
        return {}
    if lang == "tr":
        out = copy.deepcopy(PAGES_TR[slug])
    elif lang in FULL_LOCALE_LANGS:
        pages = _get_cached_full_locale_pages(lang)
        page = pages.get(slug)
        out = copy.deepcopy(page) if page else copy.deepcopy(PAGES_EN[slug])
    else:
        out = copy.deepcopy(PAGES_EN[slug])
    out.update(CTA_BY_LANG[lang])
    if slug == "for-clinics":
        patch = _FOR_CLINICS_LANG_PATCH.get(lang)
        if patch:
            out.update(patch)
        extras = _FOR_CLINICS_FAQ_EXTRAS.get(lang, _FOR_CLINICS_FAQ_EXTRAS["en"])
        out["faq"] = list(out["faq"]) + list(extras)
        base_res = list(out.get("resources") or [])
        out["resources"] = base_res + _clinic_seo_resource_cards(lang)
    return out
