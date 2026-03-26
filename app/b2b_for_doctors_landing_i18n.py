# -*- coding: utf-8 -*-
"""Premium locale-aware copy for /for-doctors landing (clinician positioning)."""
from __future__ import annotations

import copy
from typing import Any, Dict, List

from app.about_contact_i18n import ABOUT_CONTACT_LANGS

SUPPORTED_LANGS = frozenset(ABOUT_CONTACT_LANGS)


def _faq_en() -> List[Dict[str, str]]:
    return [
        {
            "q": "Is Norya a diagnostic tool?",
            "a": "No. Norya does not diagnose or treat. It organizes and explains laboratory results in structured, patient-friendly language for educational use and to support conversations with a clinician.",
        },
        {
            "q": "Can doctors use Norya to support patient communication?",
            "a": "Yes. Many teams use it as an assistive layer: clearer summaries, consistent reference-range presentation, and multilingual handoff materials that you still review and contextualize for the patient.",
        },
        {
            "q": "Does Norya replace physician judgment?",
            "a": "No. Clinical decisions stay with the licensed professional. Norya is designed to reduce repetitive explanation work and improve how information is presented—not to decide care.",
        },
        {
            "q": "Can reports be shared as PDFs?",
            "a": "Yes. Patients or teams can download a structured PDF suitable for review and sharing, subject to your workflow and policies.",
        },
        {
            "q": "Is multilingual output available?",
            "a": "Yes. Norya supports 9+ report languages so patients can read explanations in the language that fits them best.",
        },
        {
            "q": "Can doctors request demos for clinic use?",
            "a": "Yes. Use the demo request flow or contact our team to scope languages, volume, and onboarding for your setting.",
        },
        {
            "q": "Does Norya support trend or comparison workflows?",
            "a": "When prior analyses exist in supported product flows, comparison context can appear. It is informational only and must be interpreted by a clinician; not all plans include the same history features.",
        },
        {
            "q": "How should patients use the report?",
            "a": "As educational context before or after a visit—not as a substitute for medical advice. Encourage patients to bring questions to their clinician, especially for abnormal or changing values.",
        },
    ]


def _faq_tr() -> List[Dict[str, str]]:
    return [
        {
            "q": "Norya tanı aracı mı?",
            "a": "Hayır. Norya tanı koymaz veya tedavi önermez. Laboratuvar sonuçlarını eğitim amaçlı, yapılandırılmış ve hasta dostu dilde düzenler; klinisyenle görüşmeyi desteklemek içindir.",
        },
        {
            "q": "Doktorlar hasta iletişimini desteklemek için Norya kullanabilir mi?",
            "a": "Evet. Birçok ekip yardımcı katman olarak kullanır: daha net özetler, tutarlı referans aralığı sunumu ve sizin hasta için yorumlayıp bağlama ihtiyacınız olan çok dilli devir materyalleri.",
        },
        {
            "q": "Norya hekim kararının yerini alır mı?",
            "a": "Hayır. Klinik kararlar lisanslı hekimdedir. Norya, bilginin nasıl sunulduğunu iyileştirmek ve tekrarlayan açıklama yükünü hafifletmek için tasarlandı—tedaviyi seçmek için değil.",
        },
        {
            "q": "Raporlar PDF olarak paylaşılabilir mi?",
            "a": "Evet. Hastalar veya ekipler, inceleme ve paylaşıma uygun yapılandırılmış PDF indirebilir; bu, sizin iş akışınız ve politikalarınıza tabidir.",
        },
        {
            "q": "Çok dilli çıktı var mı?",
            "a": "Evet. Norya 9+ rapor dili sunar; hastalar açıklamayı kendilerine uygun dilde okuyabilir.",
        },
        {
            "q": "Doktorlar klinik kullanım için demo talep edebilir mi?",
            "a": "Evet. Demo talebi veya iletişim kanalımız üzerinden dil, hacim ve kurulum kapsamını birlikte netleştirebilirsiniz.",
        },
        {
            "q": "Norya trend veya karşılaştırma akışlarını destekliyor mu?",
            "a": "Desteklenen ürün akışlarında önceki analizler mevcut olduğunda karşılaştırma bağlamı görünebilir. Bu yalnızca bilgilendiricidir ve klinisyen yorumu gerektirir; tüm planlarda aynı geçmiş özellikleri bulunmayabilir.",
        },
        {
            "q": "Hastalar raporu nasıl kullanmalı?",
            "a": "Ziyaret öncesi veya sonrası eğitim bağlamı olarak—tıbbi tavsiye yerine geçmez. Özellikle anormal veya değişen değerlerde sorularını hekimlerine taşımalarını önerin.",
        },
    ]


def _content_en() -> Dict[str, Any]:
    return {
        "meta_title": "NoryaAI for doctors — Clearer lab communication & handoffs",
        "meta_description": "Assistive layer for laboratory results: structured summaries, reference-aware presentation, multilingual patient handoffs, and shareable PDFs. Not a diagnostic tool—designed to support clinical communication.",
        "hero_badge": "For clinicians",
        "hero_title": "Clearer conversations when labs come back.",
        "hero_desc": "NoryaAI is built for laboratory reporting—not open-ended chat. It helps turn routine blood work into structured, patient-friendly explanations, reference-range context, and doctor-ready PDFs you can use to reduce confusion after check-ups and prepare better follow-ups. It supports your judgment; it does not replace it.",
        "hero_cta_primary": "Request demo",
        "hero_cta_secondary": "View sample report",
        "how_title": "How clinicians use Norya",
        "how_cards": [
            {
                "title": "After-checkup explanation",
                "body": "When panels return dense numbers, a structured summary can help patients leave with a clearer mental model before your next message or visit.",
                "icon": "📋",
            },
            {
                "title": "Follow-up visit preparation",
                "body": "Highlight what changed, what stayed stable, and what merits discussion—so consultations start with shared context.",
                "icon": "📅",
            },
            {
                "title": "Complex markers in plain language",
                "body": "Translate common abbreviations and out-of-range flags into cautious, readable wording patients can revisit at home.",
                "icon": "💬",
            },
            {
                "title": "Multilingual patient handoff",
                "body": "Publish the same structured report in 9+ languages for international patients and family members who prefer another language.",
                "icon": "🌐",
            },
        ],
        "what_title": "What you get on the clinical side",
        "what_items": [
            {
                "title": "Structured report output",
                "body": "Sections for summary, values, and context—consistent formatting instead of a wall of unstructured text.",
            },
            {
                "title": "Key findings summary",
                "body": "Prioritized highlights that you can scan quickly before customizing advice for the patient.",
            },
            {
                "title": "Reference-range aware presentation",
                "body": "Values framed against typical ranges with conservative language suitable for patient education.",
            },
            {
                "title": "Shareable PDF",
                "body": "A clean file patients can print, save, or bring to an appointment—aligned with your communication workflow.",
            },
            {
                "title": "QR-verified report delivery",
                "body": "Optional authenticity check so recipients can trust the document came from Norya when you use that flow.",
            },
            {
                "title": "Trend comparison (when available)",
                "body": "When prior analyses exist in supported plans, the platform can surface change-over-time context. It is informational only and not a substitute for your interpretation.",
            },
            {
                "title": "Patient-friendly explanation layer",
                "body": "Plain-language scaffolding patients can read between visits; you remain the source of clinical decisions.",
            },
            {
                "title": "Multilingual output support",
                "body": "9+ report languages to align with your population and reduce translation friction.",
            },
        ],
        "why_title": "Why this helps day-to-day practice",
        "why_lead": "Most friction around labs is not the science—it is how little time there is to re-explain the same panel in patient terms.",
        "why_points": [
            "Clearer patient conversations with less duplicated explanation work.",
            "More professional handoffs when you share a structured PDF instead of ad-hoc printouts.",
            "Better baseline understanding before telehealth or short visits.",
            "Easier communication for travelers, expatriates, and multilingual households.",
            "Cleaner presentation of routine blood work without turning your EMR into a design project.",
        ],
        "limits_title": "What Norya does not replace",
        "limits_lead": "Transparency builds trust—especially in clinical settings.",
        "limits_items": [
            "It does not replace clinical judgment.",
            "It is not a diagnosis or treatment engine.",
            "It does not replace physician review of raw laboratory data.",
            "It is built to support understanding, preparation, and communication.",
        ],
        "preview_title": "Doctor-friendly output preview",
        "preview_desc": "Illustrative layout: structured sections, status cues, and language patients can digest—always reviewed in context of your care plan.",
        "preview_patient_block_title": "Patient-facing summary",
        "preview_patient_block_sample": "“Your values are mostly within typical ranges. A few markers deserve discussion at your next visit.”",
        "preview_clinical_block_title": "Structured values",
        "preview_clinical_block_sample": "Hb · Glucose · Lipids — each with range context and a short educational note.",
        "preview_sample_link": "Open sample report hub",
        "preview_disclaimer": "Sample layout for illustration; not a real patient record.",
        "preview_sheet_label": "Sample",
        "preview_range_cue": "Illustrative reference context",
        "insights_title": "Designed for clinical communication teams",
        "insights_intro": "These are practical design goals we hear from busy practices—not endorsements or claims about individual outcomes.",
        "insights": [
            {
                "label": "Less confusion after screening",
                "quote": "Patients often leave screening visits with numbers they cannot interpret. A concise, structured brief can reduce anxious messages before you have chart time.",
            },
            {
                "label": "Smoother multilingual handoffs",
                "quote": "When the report language matches the patient’s preference, fewer iterations are spent re-explaining the same panel.",
            },
            {
                "label": "More intentional follow-ups",
                "quote": "Highlighting what to monitor—or what improved—can make return visits feel collaborative instead of reactive.",
            },
        ],
        "nav_strip_title": "Also explore",
        "nav_strip_sample": "Sample reports",
        "nav_strip_trust": "Trust Center",
        "nav_strip_security": "Security",
        "nav_strip_methodology": "Methodology",
        "nav_strip_pricing": "Pricing",
        "nav_strip_compare": "Compare Norya",
        "nav_strip_clinics": "For clinics",
        "nav_strip_home": "Home",
        "faq_title": "Frequently asked questions",
        "faq": _faq_en(),
        "final_title": "Bring structure to how you explain labs.",
        "final_desc": "Request a demo, review a sample report, or talk with us about multilingual workflows and clinic onboarding—all grounded in a trust-first, assistive model.",
        "final_cta_demo": "Request demo",
        "final_cta_sample": "View sample report",
        "final_cta_clinic": "Contact for clinic use",
    }


def _content_tr() -> Dict[str, Any]:
    return {
        "meta_title": "NoryaAI doktorlar için — Daha net laboratuvar iletişimi",
        "meta_description": "Laboratuvar sonuçları için yardımcı katman: yapılandırılmış özetler, referans bilinci, çok dilli hasta devirleri ve paylaşılabilir PDF’ler. Tanı aracı değildir—klinik iletişimi desteklemek için tasarlandı.",
        "hero_badge": "Klinisyenler için",
        "hero_title": "Tahlil sonuçları geldiğinde daha net konuşmalar.",
        "hero_desc": "NoryaAI açık uçlu sohbet için değil; laboratuvar raporlama için üretildi. Rutin kan tahlillerini yapılandırılmış, hasta dostu açıklamalara, referans aralığı bağlamına ve doktora hazır PDF’lere dönüştürerek kontrol sonrası kafa karışıklığını azaltmanıza ve takip ziyaretlerine daha iyi hazırlanmanıza yardımcı olur. Klinik kararınızı destekler; yerinizi almaz.",
        "hero_cta_primary": "Demo talep et",
        "hero_cta_secondary": "Örnek raporu gör",
        "how_title": "Klinisyenler Norya’yı nasıl kullanır",
        "how_cards": [
            {
                "title": "Kontrol sonrası açıklama",
                "body": "Panel yoğun rakamlarla döndüğünde, yapılandırılmış bir özet hastanın bir sonraki mesajınızdan veya ziyaretinden önce daha net bir çerçeve edinmesine yardımcı olabilir.",
                "icon": "📋",
            },
            {
                "title": "Kontrol ziyareti hazırlığı",
                "body": "Ne değişti, ne stabil kaldı ve ne konuşmayı hak ediyor—görüşmeler ortak bağlamla başlasın.",
                "icon": "📅",
            },
            {
                "title": "Karmaşık göstergeleri sade dilde",
                "body": "Yaygın kısaltmaları ve sınır dışı işaretleri hasta evde tekrar okuyabileceği temkinli, anlaşılır ifadelere çevirir.",
                "icon": "💬",
            },
            {
                "title": "Çok dilli hasta devri",
                "body": "Aynı yapılandırılmış raporu 9+ dilde sunarak yurtdışı hastalar ve farklı dil tercih eden aileler için iletişimi kolaylaştırır.",
                "icon": "🌐",
            },
        ],
        "what_title": "Klinik tarafta ne elde edersiniz",
        "what_items": [
            {
                "title": "Yapılandırılmış rapor çıktısı",
                "body": "Özet, değerler ve bağlam için bölümler—düzensiz metin duvarı yerine tutarlı biçim.",
            },
            {
                "title": "Önemli bulgular özeti",
                "body": "Hasta için tavsiyenizi kişiselleştirmeden önce hızlıca tarayabileceğiniz öncelikli vurgular.",
            },
            {
                "title": "Referans aralığı bilincine sahip sunum",
                "body": "Değerler, hasta eğitimine uygun muhafazakâr dil ile tipik aralıklar çerçevesinde.",
            },
            {
                "title": "Paylaşılabilir PDF",
                "body": "Hastaların yazdırabileceği, saklayabileceği veya randevuya getirebileceği sade bir dosya—iletişim akışınıza uyumlu.",
            },
            {
                "title": "QR ile doğrulanabilir rapor teslimi",
                "body": "Bu akışı kullandığınızda, alıcıların belgenin Norya’dan geldiğine güvenmesi için isteğe bağlı özgünlük kontrolü.",
            },
            {
                "title": "Trend karşılaştırması (uygun olduğunda)",
                "body": "Desteklenen planlarda önceki analizler mevcut olduğunda platform zaman içi değişim bağlamı gösterebilir. Bu yalnızca bilgilendiricidir ve yorumunuzun yerini tutmaz.",
            },
            {
                "title": "Hasta dostu açıklama katmanı",
                "body": "Ziyaretler arasında okunabilen sade dil iskelesi; klinik kararların kaynağı sizsiniz.",
            },
            {
                "title": "Çok dilli çıktı desteği",
                "body": "Nüfusunuza uyum ve çeviri sürtünmesini azaltmak için 9+ rapor dili.",
            },
        ],
        "why_title": "Günlük pratiğe neden yardımcı olur",
        "why_lead": "Laboratuvarlar etrafındaki sürtünme çoğu zaman bilim değil—aynı paneli hasta dilinde yeniden anlatmak için ayırılan süredir.",
        "why_points": [
            "Tekrarlayan açıklama yükünü azaltarak daha net hasta görüşmeleri.",
            "Geçici çıktılar yerine yapılandırılmış PDF paylaştığınızda daha profesyonel devir.",
            "Tele-sağlık veya kısa ziyaretlerden önce daha iyi temel anlayış.",
            "Seyahat edenler, yurtdışında yaşayanlar ve çok dilli haneler için daha kolay iletişim.",
            "EMR’nizi tasarım projesine çevirmeden rutin kan tahlillerinin daha düzenli sunumu.",
        ],
        "limits_title": "Norya neyin yerini almaz",
        "limits_lead": "Şeffaflık güveni güçlendirir—özellikle klinik ortamda.",
        "limits_items": [
            "Klinik muhakemenin yerini tutmaz.",
            "Tanı veya tedavi motoru değildir.",
            "Ham laboratuvar verilerinin hekim incelemesinin yerini almaz.",
            "Anlama, hazırlık ve iletişimi desteklemek için üretildi.",
        ],
        "preview_title": "Doktora uygun çıktı önizlemesi",
        "preview_desc": "Örnek düzen: yapılandırılmış bölümler, durum ipuçları ve hastaların sindirebileceği dil—her zaman bakım planınızın bağlamında incelenmelidir.",
        "preview_patient_block_title": "Hastaya dönük özet",
        "preview_patient_block_sample": "“Değerleriniz çoğunlukla tipik aralıklarda. Birkaç gösterge bir sonraki ziyaretinizde konuşmayı hak ediyor.”",
        "preview_clinical_block_title": "Yapılandırılmış değerler",
        "preview_clinical_block_sample": "Hb · Glukoz · Lipidler — her biri aralık bağlamı ve kısa eğitim notu ile.",
        "preview_sample_link": "Örnek rapor merkezini aç",
        "preview_disclaimer": "Gösterim amaçlı örnek düzen; gerçek hasta kaydı değildir.",
        "preview_sheet_label": "Örnek",
        "preview_range_cue": "Örnek referans bağlamı",
        "insights_title": "Klinik iletişim ekipleri için tasarlandı",
        "insights_intro": "Bunlar yoğun pratiklerden duyduğumuz tasarım hedefleri—bireysel sonuç iddiası veya onay değildir.",
        "insights": [
            {
                "label": "Tarama sonrası daha az kafa karışıklığı",
                "quote": "Hastalar tarama ziyaretlerinden yorumlayamadıkları rakamlarla çıkabiliyor. Kısa, yapılandırılmış bir özet grafik zamanınız olmadan endişeli mesajları azaltabilir.",
            },
            {
                "label": "Daha akıcı çok dilli devir",
                "quote": "Rapor dili hastanın tercihiyle uyduğunda aynı panelin tekrar açıklanmasında daha az tur harcanır.",
            },
            {
                "label": "Daha bilinçli takip",
                "quote": "İzlenecek veya iyileşen şeyleri vurgulamak dönüş ziyaretlerini daha iş birlikçi hissettirebilir.",
            },
        ],
        "nav_strip_title": "Keşfet",
        "nav_strip_sample": "Örnek raporlar",
        "nav_strip_trust": "Güven Merkezi",
        "nav_strip_security": "Güvenlik",
        "nav_strip_methodology": "Metodoloji",
        "nav_strip_pricing": "Fiyatlandırma",
        "nav_strip_compare": "Norya karşılaştırması",
        "nav_strip_clinics": "Klinikler için",
        "nav_strip_home": "Ana sayfa",
        "faq_title": "Sık sorulan sorular",
        "faq": _faq_tr(),
        "final_title": "Laboratuvarları nasıl açıkladığınıza düzen getirin.",
        "final_desc": "Demo talep edin, örnek raporu inceleyin veya çok dilli akışlar ve klinik kurulum hakkında konuşun—hepsi güven öncelikli yardımcı modele dayanır.",
        "final_cta_demo": "Demo talep et",
        "final_cta_sample": "Örnek raporu gör",
        "final_cta_clinic": "Klinik kullanım için iletişim",
    }


def _faq_de() -> List[Dict[str, str]]:
    return [
        {
            "q": "Ist Norya ein Diagnosetool?",
            "a": "Nein. Norya stellt keine Diagnosen und empfiehlt keine Therapien. Es ordnet Laborergebnisse strukturiert und patientenverständlich für Bildungszwecke und zur Unterstützung des Arzt-Patienten-Gesprächs auf.",
        },
        {
            "q": "Können Ärztinnen und Ärzte Norya zur Patientenkommunikation nutzen?",
            "a": "Ja. Viele Teams nutzen es als assistive Ebene: klarere Zusammenfassungen, einheitliche Referenzdarstellung und mehrsprachige Übergaben, die Sie weiterhin prüfen und für den Patienten einordnen.",
        },
        {
            "q": "Ersetzt Norya das ärztliche Urteil?",
            "a": "Nein. Klinische Entscheidungen liegen bei der zugelassenen Fachkraft. Norya soll wiederholte Erklärungsarbeit erleichtern und die Darstellung verbessern—nicht die Behandlung festlegen.",
        },
        {
            "q": "Lassen sich Berichte als PDF teilen?",
            "a": "Ja. Patientinnen oder Teams können ein strukturiertes PDF herunterladen—vorbehaltlich Ihrer Abläufe und Richtlinien.",
        },
        {
            "q": "Gibt es mehrsprachige Ausgabe?",
            "a": "Ja. Norya unterstützt 9+ Berichtssprachen, damit Erklärungen zur bevorzugten Sprache passen.",
        },
        {
            "q": "Können Kliniken Demos anfragen?",
            "a": "Ja. Nutzen Sie den Demo-Workflow oder kontaktieren Sie uns für Sprachen, Volumen und Onboarding.",
        },
        {
            "q": "Gibt es Trend- oder Vergleichsfunktionen?",
            "a": "Wenn frühere Analysen in unterstützten Produktpfaden vorliegen, kann Vergleichskontext erscheinen. Das ist nur informativ und ersetzt nicht die ärztliche Interpretation; nicht alle Pläne bieten dieselben Verlaufsfunktionen.",
        },
        {
            "q": "Wie sollen Patientinnen den Bericht nutzen?",
            "a": "Als Bildungskontext vor oder nach einem Termin—nicht als Ersatz für medizinische Beratung. Besonders bei auffälligen oder wechselnden Werten Fragen an die behandelnde Person richten.",
        },
    ]


# Non-EN/TR: full structure from English; professional translations for visible strings.
def _content_de() -> Dict[str, Any]:
    t = copy.deepcopy(_content_en())
    t.update(
        {
            "meta_title": "NoryaAI für Ärztinnen und Ärzte — Klarere Laborkommunikation",
            "meta_description": "Assistive Ebene für Laborergebnisse: strukturierte Zusammenfassungen, referenzbewusste Darstellung, mehrsprachige Übergaben und teilbare PDFs. Kein Diagnosetool—für die klinische Kommunikation konzipiert.",
            "hero_badge": "Für Kliniker",
            "hero_title": "Klarere Gespräche, wenn Laborwerte zurückkommen.",
            "hero_desc": "NoryaAI ist für Laborberichte gedacht—nicht für allgemeinen Chat. Es hilft, routinemäßige Blutwerte in strukturierte, patientenfreundliche Erklärungen, Referenzkontext und arztfertige PDFs zu verwandeln, um Verwirrung nach Check-ups zu reduzieren und Follow-ups vorzubereiten. Es unterstützt Ihr Urteil; es ersetzt es nicht.",
            "hero_cta_primary": "Demo anfragen",
            "hero_cta_secondary": "Beispielbericht ansehen",
            "how_title": "So nutzen Kliniker Norya",
            "what_title": "Was Sie klinisch gewinnen",
            "why_title": "Warum das den Praxisalltag entlastet",
            "why_lead": "Reibung entsteht oft weniger durch die Medizin selbst—sondern durch die knappe Zeit, dieselben Kennwerte verständlich zu erklären.",
            "limits_title": "Was Norya nicht ersetzt",
            "limits_lead": "Transparenz schafft Vertrauen—besonders im klinischen Umfeld.",
            "preview_title": "Vorschau ärztetauglicher Ausgabe",
            "preview_desc": "Illustratives Layout: strukturierte Abschnitte, Statushinweise und verständliche Sprache—immer im Kontext Ihres Behandlungsplans zu prüfen.",
            "preview_patient_block_title": "Patientenorientierte Zusammenfassung",
            "preview_patient_block_sample": "„Ihre Werte liegen größtenteils im typischen Bereich. Einzelne Marker sollten beim nächsten Termin besprochen werden.“",
            "preview_clinical_block_title": "Strukturierte Werte",
            "preview_clinical_block_sample": "Hb · Glukose · Lipide—jeweils mit Referenz und kurzem Bildungshinweis.",
            "preview_sample_link": "Beispielberichte öffnen",
            "preview_disclaimer": "Beispiellayout zur Veranschaulichung; keine echten Patientendaten.",
            "preview_sheet_label": "Beispiel",
            "preview_range_cue": "Illustrativer Referenzkontext",
            "insights_title": "Für Kommunikationsteams in der Praxis",
            "insights_intro": "Praktische Designziele aus vielbeschäftigten Teams—keine Ergebnisversprechen.",
            "nav_strip_title": "Mehr entdecken",
            "nav_strip_sample": "Beispielberichte",
            "nav_strip_trust": "Trust Center",
            "nav_strip_security": "Sicherheit",
            "nav_strip_methodology": "Methodik",
            "nav_strip_pricing": "Preise",
            "nav_strip_compare": "Norya vergleichen",
            "nav_strip_clinics": "Für Kliniken",
            "nav_strip_home": "Startseite",
            "faq_title": "Häufige Fragen",
            "faq": _faq_de(),
            "final_title": "Strukturieren Sie, wie Sie Laborwerte erklären.",
            "final_desc": "Demo anfragen, Beispielbericht prüfen oder mit uns über mehrsprachige Workflows sprechen—auf Basis eines assistiven, vertrauensorientierten Modells.",
            "final_cta_demo": "Demo anfragen",
            "final_cta_sample": "Beispielbericht ansehen",
            "final_cta_clinic": "Kontakt für Kliniken",
        }
    )
    t["how_cards"] = [
        {"title": "Erklärung nach dem Check-up", "body": "Wenn Panels dicht sind, kann eine strukturierte Zusammenfassung helfen, bevor die nächste Nachricht oder der Termin kommt.", "icon": "📋"},
        {"title": "Vorbereitung auf Folgetermine", "body": "Was sich geändert hat, was stabil blieb—damit Gespräche mit gemeinsamem Kontext starten.", "icon": "📅"},
        {"title": "Komplexe Marker in einfacher Sprache", "body": "Abkürzungen und Grenzwerte vorsichtig formulieren, damit Patientinnen und Patienten zu Hause nachlesen können.", "icon": "💬"},
        {"title": "Mehrsprachige Übergabe", "body": "Denselben Bericht in 9+ Sprachen—für internationale Patientinnen und Familien.", "icon": "🌐"},
    ]
    t["what_items"] = [
        {
            "title": "Strukturierter Bericht",
            "body": "Abschnitte für Zusammenfassung, Werte und Kontext—statt unstrukturierter Textwände.",
        },
        {
            "title": "Kernaussagen",
            "body": "Priorisierte Highlights, die Sie schnell sichten, bevor Sie die Beratung individualisieren.",
        },
        {
            "title": "Referenzbewusste Darstellung",
            "body": "Werte mit typischem Referenzrahmen und vorsichtiger Bildungssprache.",
        },
        {
            "title": "Teilbares PDF",
            "body": "Eine saubere Datei zum Ausdrucken, Speichern oder Mitbringen zum Termin.",
        },
        {
            "title": "QR-verifizierbare Zustellung",
            "body": "Optional: Prüfung der Echtheit, wenn Sie diesen Ablauf nutzen.",
        },
        {
            "title": "Trendvergleich (wenn verfügbar)",
            "body": "Bei früheren Analysen in unterstützten Plänen kann Verlaufskontext erscheinen—nur informativ, kein Ersatz Ihrer Interpretation.",
        },
        {
            "title": "Patientenfreundliche Erklärebene",
            "body": "Alltagstaugliche Formulierungen zwischen Terminen; klinische Entscheidungen bleiben bei Ihnen.",
        },
        {
            "title": "Mehrsprachige Ausgabe",
            "body": "9+ Berichtssprachen für Ihre Population und weniger Übersetzungsreibung.",
        },
    ]
    t["why_points"] = [
        "Klarere Gespräche mit weniger wiederholter Erklärungsarbeit.",
        "Professionellere Übergaben mit strukturierten PDFs.",
        "Besseres Verständnis vor Kurzkontakten oder Videosprechstunden.",
        "Einfachere Kommunikation für Reisende und mehrsprachige Haushalte.",
        "Ordentlichere Darstellung routinemäßiger Blutwerte.",
    ]
    t["limits_items"] = [
        "Ersetzt nicht das klinische Urteil.",
        "Ist keine Diagnose- oder Therapie-Engine.",
        "Ersetzt nicht die ärztliche Prüfung der Rohdaten.",
        "Unterstützt Verständnis, Vorbereitung und Kommunikation.",
    ]
    t["insights"] = [
        {
            "label": "Weniger Verwirrung nach Screening",
            "quote": "Patienten verlassen mit Zahlen, die sie nicht einordnen. Ein kurzer Brief kann Anfragen reduzieren, bevor Sie Chart-Zeit haben.",
        },
        {
            "label": "Flüssigere mehrsprachige Übergaben",
            "quote": "Passt die Sprache zum Patienten, sinkt oft die Zahl der Nachfragen.",
        },
        {
            "label": "Bewusstere Nachsorge",
            "quote": "Was zu beobachten oder was sich verbessert hat—macht Rücktermine kooperativer.",
        },
    ]
    return t


def _apply_locale_patch(base: Dict[str, Any], patch: Dict[str, Any]) -> Dict[str, Any]:
    t = copy.deepcopy(base)
    for k, v in patch.items():
        t[k] = v
    return t


def _content_fr() -> Dict[str, Any]:
    return _apply_locale_patch(
        _content_en(),
        {
            "meta_title": "NoryaAI pour les médecins — Communication biologique plus claire",
            "meta_description": "Couche d’aide pour les résultats de laboratoire : synthèses structurées, présentation avec plages de référence, transmissions multilingues et PDF partageables. Pas un outil de diagnostic—conçu pour soutenir la communication clinique.",
            "hero_badge": "Pour les cliniciens",
            "hero_title": "Des échanges plus clairs lorsque les résultats arrivent.",
            "hero_desc": "NoryaAI sert à la restitution de bilans—pas à la conversation libre. Il aide à transformer les analyses routinières en explications structurées et accessibles, avec contexte des plages de référence et PDF prêts pour le clinicien, pour réduire la confusion après une visite et mieux préparer le suivi. Il soutient votre jugement ; il ne le remplace pas.",
            "hero_cta_primary": "Demander une démo",
            "hero_cta_secondary": "Voir un rapport d’exemple",
            "how_title": "Comment les cliniciens utilisent Norya",
            "what_title": "Ce que vous obtenez côté pratique",
            "why_title": "Pourquoi cela aide au quotidien",
            "why_lead": "La friction autour des bilans vient souvent du peu de temps pour réexpliquer le même panel en langage patient.",
            "limits_title": "Ce que Norya ne remplace pas",
            "limits_lead": "La transparence renforce la confiance—surtout en milieu clinique.",
            "preview_title": "Aperçu du rendu adapté aux médecins",
            "preview_desc": "Mise en page illustrative : sections structurées et formulations lisibles—à toujours valider dans le cadre de votre prise en charge.",
            "preview_patient_block_title": "Synthèse orientée patient",
            "preview_patient_block_sample": "« Vos valeurs sont globalement dans les plages habituelles. Quelques marqueurs méritent d’être abordés à la prochaine consultation. »",
            "preview_clinical_block_title": "Valeurs structurées",
            "preview_clinical_block_sample": "Hb · Glucose · Lipides — chacun avec contexte de plage et courte note pédagogique.",
            "preview_sample_link": "Ouvrir la galerie d’exemples",
            "preview_disclaimer": "Exemple à titre illustratif ; pas de dossier patient réel.",
            "preview_sheet_label": "Exemple",
            "preview_range_cue": "Contexte de référence illustratif",
            "insights_title": "Conçu pour les équipes de communication clinique",
            "insights_intro": "Objectifs pratiques entendus auprès d’équipes chargées—pas des promesses de résultats individuels.",
            "nav_strip_title": "Explorer aussi",
            "nav_strip_sample": "Rapports d’exemple",
            "nav_strip_trust": "Centre de confiance",
            "nav_strip_security": "Sécurité",
            "nav_strip_methodology": "Méthodologie",
            "nav_strip_pricing": "Tarifs",
            "nav_strip_compare": "Comparer Norya",
            "nav_strip_clinics": "Pour les cliniques",
            "nav_strip_home": "Accueil",
            "faq_title": "Questions fréquentes",
            "final_title": "Structurez la façon dont vous expliquez les bilans.",
            "final_desc": "Demandez une démo, consultez un exemple ou parlez-nous de flux multilingues et d’onboarding clinique—dans un modèle assistif et orienté confiance.",
            "final_cta_demo": "Demander une démo",
            "final_cta_sample": "Voir un rapport d’exemple",
            "final_cta_clinic": "Contact usage en clinique",
            "how_cards": [
                {"title": "Après la visite de contrôle", "body": "Quand le panel est dense, une synthèse structurée aide avant le prochain message ou rendez-vous.", "icon": "📋"},
                {"title": "Préparation du suivi", "body": "Ce qui a changé, ce qui est stable—pour démarrer la consultation avec un contexte partagé.", "icon": "📅"},
                {"title": "Marqueurs complexes, langage simple", "body": "Formuler prudemment abréviations et écarts pour une relecture à domicile.", "icon": "💬"},
                {"title": "Transmission multilingue", "body": "Le même rapport structuré en 9+ langues pour les patients internationaux et les familles.", "icon": "🌐"},
            ],
            "what_items": [
                {"title": "Rapport structuré", "body": "Sections résumé, valeurs et contexte—format cohérent plutôt qu’un bloc de texte."},
                {"title": "Synthèse des éléments clés", "body": "Faits saillants priorisés à parcourir avant de personnaliser vos conseils."},
                {"title": "Présentation avec plages de référence", "body": "Valeurs cadrées avec un langage prudent pour l’éducation thérapeutique."},
                {"title": "PDF partageable", "body": "Un document propre à imprimer, archiver ou apporter au rendez-vous."},
                {"title": "Livraison vérifiable par QR", "body": "Contrôle d’authenticité optionnel lorsque vous utilisez ce flux."},
                {"title": "Comparaison d’évolution (si disponible)", "body": "Lorsque des analyses antérieures existent sur des offres prises en charge, un contexte d’évolution peut apparaître—à titre informatif seulement."},
                {"title": "Couche d’explication patient", "body": "Formulations accessibles entre les visites ; vos décisions cliniques restent la référence."},
                {"title": "Sortie multilingue", "body": "9+ langues de rapport pour coller à votre population."},
            ],
            "why_points": [
                "Échanges plus clairs avec moins d’explications répétées.",
                "Remises plus professionnelles avec des PDF structurés.",
                "Meilleure compréhension de base avant téléconsultation ou rendez-vous court.",
                "Communication facilitée pour les voyageurs et foyers multilingues.",
                "Présentation plus nette des bilans de routine sans retravailler l’interface du DPI.",
            ],
            "limits_items": [
                "Ne remplace pas le jugement clinique.",
                "N’est pas un moteur de diagnostic ou de traitement.",
                "Ne remplace pas la relecture médicale des données brutes.",
                "Conçu pour la compréhension, la préparation et la communication.",
            ],
            "insights": [
                {"label": "Moins de confusion après dépistage", "quote": "Les patients repartent souvent avec des chiffres qu’ils n’interprètent pas. Un bref structuré peut réduire les messages anxieux avant que vous ayez le dossier."},
                {"label": "Remises multilingues plus fluides", "quote": "Quand la langue du rapport suit la préférence du patient, il y a souvent moins de va-et-vient."},
                {"label": "Suivis plus intentionnels", "quote": "Mettre en avant ce qu’il faut surveiller ou ce qui s’améliore rend les retours plus collaboratifs."},
            ],
        },
    )


def _content_it() -> Dict[str, Any]:
    return _apply_locale_patch(
        _content_en(),
        {
            "meta_title": "NoryaAI per medici — Comunicazione sugli esami più chiara",
            "meta_description": "Strato assistivo per i risultati di laboratorio: sintesi strutturate, presentazione con range di riferimento, passaggi multilingue e PDF condivisibili. Non è uno strumento diagnostico—progettato per supportare la comunicazione clinica.",
            "hero_badge": "Per i clinici",
            "hero_title": "Conversazioni più chiare quando tornano gli esami.",
            "hero_desc": "NoryaAI è pensato per la rendicontazione di laboratorio, non per chat libera. Aiuta a trasformare i profili ematici di routine in spiegazioni strutturate e comprensibili, con contesto dei range e PDF pronti per il medico, riducendo la confusione dopo i controlli e preparando meglio i follow-up. Supporta il suo giudizio; non lo sostituisce.",
            "hero_cta_primary": "Richiedi demo",
            "hero_cta_secondary": "Vedi rapporto di esempio",
            "how_title": "Come i clinici usano Norya",
            "what_title": "Cosa ottieni sul piano clinico",
            "why_title": "Perché aiuta nella pratica quotidiana",
            "why_lead": "Spesso il problema non è la medicina, ma il poco tempo per rispiegare lo stesso pannello in linguaggio paziente.",
            "limits_title": "Cosa Norya non sostituisce",
            "limits_lead": "La trasparenza costruisce fiducia—in particolare in ambito clinico.",
            "preview_title": "Anteprima output favorevole al medico",
            "preview_desc": "Layout illustrativo: sezioni strutturate e linguaggio leggibile—sempre da inquadrare nel piano di cura.",
            "preview_patient_block_title": "Sintesi per il paziente",
            "preview_patient_block_sample": "«I suoi valori sono per lo più nei range abituali. Alcuni marcatori meritano discussione alla prossima visita.»",
            "preview_clinical_block_title": "Valori strutturati",
            "preview_clinical_block_sample": "Emoglobina · Glucidi · Lipidi — ciascuno con contesto di range e breve nota educativa.",
            "preview_sample_link": "Apri hub rapporti di esempio",
            "preview_disclaimer": "Layout di esempio; non è una cartella clinica reale.",
            "preview_sheet_label": "Esempio",
            "preview_range_cue": "Contesto di riferimento illustrativo",
            "insights_title": "Pensato per i team di comunicazione clinica",
            "insights_intro": "Obiettivi pratici che emergono da team carichi di lavoro—non promesse su esiti individuali.",
            "nav_strip_title": "Scopri anche",
            "nav_strip_sample": "Rapporti di esempio",
            "nav_strip_trust": "Trust Center",
            "nav_strip_security": "Sicurezza",
            "nav_strip_methodology": "Metodologia",
            "nav_strip_pricing": "Prezzi",
            "nav_strip_compare": "Confronta Norya",
            "nav_strip_clinics": "Per le cliniche",
            "nav_strip_home": "Home",
            "faq_title": "Domande frequenti",
            "final_title": "Dai struttura a come spieghi gli esami.",
            "final_desc": "Richiedi una demo, consulta un esempio o parla con noi di flussi multilingue e onboarding in clinica—con un modello assistivo e orientato alla fiducia.",
            "final_cta_demo": "Richiedi demo",
            "final_cta_sample": "Vedi rapporto di esempio",
            "final_cta_clinic": "Contatto per uso in clinica",
            "how_cards": [
                {"title": "Dopo il controllo", "body": "Quando il pannello è denso, una sintesi strutturata aiuta prima del prossimo messaggio o appuntamento.", "icon": "📋"},
                {"title": "Preparazione al follow-up", "body": "Cosa è cambiato e cosa è stabile—così la visita inizia con contesto condiviso.", "icon": "📅"},
                {"title": "Marcatori complessi in parole semplici", "body": "Abbreviazioni e valori fuori range formulati con prudenza per una rilettura a casa.", "icon": "💬"},
                {"title": "Passaggio multilingue", "body": "Lo stesso rapporto strutturato in oltre 9 lingue per pazienti internazionali e famiglie.", "icon": "🌐"},
            ],
            "what_items": [
                {"title": "Output strutturato", "body": "Sezioni per sintesi, valori e contesto—formattazione uniforme."},
                {"title": "Sintesi dei punti chiave", "body": "Evidenziazioni prioritarie da scansionare prima di personalizzare i consigli."},
                {"title": "Presentazione con range di riferimento", "body": "Valori inquadrati con linguaggio prudente per l’educazione sanitaria."},
                {"title": "PDF condivisibile", "body": "File pulito da stampare, salvare o portare in visita."},
                {"title": "Consegna con verifica QR", "body": "Controllo di autenticità opzionale quando usi quel flusso."},
                {"title": "Confronto trend (se disponibile)", "body": "Con analisi precedenti nei piani supportati può comparire contesto temporale—informativo, non sostitutivo della tua interpretazione."},
                {"title": "Livello esplicativo per il paziente", "body": "Impalcatura in linguaggio semplice tra una visita e l’altra; le decisioni cliniche restano tue."},
                {"title": "Output multilingue", "body": "Oltre 9 lingue di report per adattarti al tuo bacino utenti."},
            ],
            "why_points": [
                "Dialoghi più chiari con meno ripetizione delle spiegazioni.",
                "Passaggi di mano più professionali con PDF strutturati.",
                "Comprensione di base migliore prima di tele-visite o visite brevi.",
                "Comunicazione più semplice per viaggiatori e nuclei multilingue.",
                "Presentazione ordinata degli esami di routine senza ridisegnare il referto nel CED.",
            ],
            "limits_items": [
                "Non sostituisce il giudizio clinico.",
                "Non è un motore di diagnosi o terapia.",
                "Non sostituisce la revisione medica dei dati grezzi.",
                "Progettato per comprensione, preparazione e comunicazione.",
            ],
            "insights": [
                {"label": "Meno confusione dopo lo screening", "quote": "I pazienti escono con numeri che non sanno leggere. Un riepilogo sintetico può ridurre messaggi ansiosi prima che tu abbia tempo per la cartella."},
                {"label": "Passaggi multilingue più fluidi", "quote": "Quando la lingua del referto coincide con la preferenza del paziente, spesso calano i round di rispiegazione."},
                {"label": "Follow-up più intenzionali", "quote": "Evidenziare cosa monitorare o cosa è migliorato rende i ritorni più collaborativi."},
            ],
        },
    )


def _content_es() -> Dict[str, Any]:
    return _apply_locale_patch(
        _content_en(),
        {
            "meta_title": "NoryaAI para médicos — Comunicación de laboratorio más clara",
            "meta_description": "Capa de apoyo para resultados de laboratorio: resúmenes estructurados, presentación con rangos de referencia, entregas multilingües y PDF compartibles. No es una herramienta de diagnóstico—diseñada para apoyar la comunicación clínica.",
            "hero_badge": "Para clínicos",
            "hero_title": "Conversaciones más claras cuando vuelven los resultados.",
            "hero_desc": "NoryaAI está pensado para informes de laboratorio, no para chat abierto. Ayuda a convertir analíticas rutinarias en explicaciones estructuradas y comprensibles, con contexto de rangos y PDF listos para el médico, reduciendo la confusión tras revisiones y preparando mejor el seguimiento. Apoya su criterio; no lo sustituye.",
            "hero_cta_primary": "Solicitar demo",
            "hero_cta_secondary": "Ver informe de muestra",
            "how_title": "Cómo usan Norya los clínicos",
            "what_title": "Qué obtiene el lado clínico",
            "why_title": "Por qué ayuda en el día a día",
            "why_lead": "La fricción suele ser el poco tiempo para volver a explicar el mismo panel en lenguaje paciente, no la ciencia en sí.",
            "limits_title": "Lo que Norya no sustituye",
            "limits_lead": "La transparencia genera confianza—especialmente en entornos clínicos.",
            "preview_title": "Vista previa del resultado apto para médicos",
            "preview_desc": "Diseño ilustrativo: secciones estructuradas y lenguaje legible—confirmar siempre en el contexto del plan asistencial.",
            "preview_patient_block_title": "Resumen orientado al paciente",
            "preview_patient_block_sample": "«Sus valores se mantienen en gran parte en rangos habituales. Algunos marcadores merecen comentarse en la próxima visita.»",
            "preview_clinical_block_title": "Valores estructurados",
            "preview_clinical_block_sample": "Hb · Glucosa · Lípidos — cada uno con contexto de rango y nota educativa breve.",
            "preview_sample_link": "Abrir centro de informes de muestra",
            "preview_disclaimer": "Ejemplo ilustrativo; no es un historial real.",
            "preview_sheet_label": "Ejemplo",
            "preview_range_cue": "Contexto de referencia ilustrativo",
            "insights_title": "Diseñado para equipos de comunicación clínica",
            "insights_intro": "Objetivos prácticos que escuchamos en consultas ocupadas—no promesas sobre resultados individuales.",
            "nav_strip_title": "Explorar también",
            "nav_strip_sample": "Informes de muestra",
            "nav_strip_trust": "Centro de confianza",
            "nav_strip_security": "Seguridad",
            "nav_strip_methodology": "Metodología",
            "nav_strip_pricing": "Precios",
            "nav_strip_compare": "Comparar Norya",
            "nav_strip_clinics": "Para clínicas",
            "nav_strip_home": "Inicio",
            "faq_title": "Preguntas frecuentes",
            "final_title": "Estructure cómo explica los análisis.",
            "final_desc": "Solicite una demo, revise un ejemplo o hable con nosotros sobre flujos multilingües e incorporación en clínicas—con un modelo asistivo y centrado en la confianza.",
            "final_cta_demo": "Solicitar demo",
            "final_cta_sample": "Ver informe de muestra",
            "final_cta_clinic": "Contacto para uso en clínica",
            "how_cards": [
                {"title": "Tras la revisión", "body": "Cuando el panel es denso, un resumen estructurado ayuda antes del siguiente mensaje o cita.", "icon": "📋"},
                {"title": "Preparación del seguimiento", "body": "Qué cambió y qué se mantuvo estable—para empezar con contexto compartido.", "icon": "📅"},
                {"title": "Marcadores complejos en lenguaje llano", "body": "Abreviaturas y desviaciones formuladas con cautela para releer en casa.", "icon": "💬"},
                {"title": "Entrega multilingüe", "body": "El mismo informe estructurado en más de 9 idiomas para pacientes internacionales y familias.", "icon": "🌐"},
            ],
            "what_items": [
                {"title": "Informe estructurado", "body": "Secciones de resumen, valores y contexto—formato coherente."},
                {"title": "Resumen de hallazgos clave", "body": "Destacados priorizados para revisar antes de personalizar consejos."},
                {"title": "Presentación con rangos de referencia", "body": "Valores enmarcados con lenguaje prudente para educación sanitaria."},
                {"title": "PDF compartible", "body": "Archivo limpio para imprimir, guardar o llevar a la cita."},
                {"title": "Entrega verificable por QR", "body": "Comprobación de autenticidad opcional cuando use ese flujo."},
                {"title": "Comparación de tendencias (cuando aplique)", "body": "Con análisis previos en planes admitidos puede mostrarse contexto evolutivo—informativo únicamente."},
                {"title": "Capa explicativa para pacientes", "body": "Andamiaje en lenguaje sencillo entre visitas; usted sigue siendo la fuente de decisiones clínicas."},
                {"title": "Salida multilingüe", "body": "Más de 9 idiomas de informe para su población."},
            ],
            "why_points": [
                "Conversaciones más claras con menos repetición explicativa.",
                "Entregas más profesionales al compartir PDF estructurados.",
                "Mejor comprensión básica antes de teleconsultas o visitas cortas.",
                "Comunicación más sencilla para viajeros y hogares multilingües.",
                "Presentación ordenada de analíticas rutinarias sin rediseñar el informe en la historia clínica.",
            ],
            "limits_items": [
                "No sustituye el juicio clínico.",
                "No es un motor de diagnóstico ni tratamiento.",
                "No sustituye la revisión médica de los datos en bruto.",
                "Está pensado para comprensión, preparación y comunicación.",
            ],
            "insights": [
                {"label": "Menos confusión tras cribados", "quote": "Los pacientes se van con cifras que no saben interpretar. Un resumen breve puede reducir mensajes ansiosos antes de que tenga tiempo de revisar la historia."},
                {"label": "Traspasos multilingües más fluidos", "quote": "Cuando el idioma del informe coincide con la preferencia del paciente, a menudo hay menos idas y vueltas."},
                {"label": "Seguimientos más deliberados", "quote": "Resaltar qué vigilar o qué mejoró hace que las visitas de control se sientan más colaborativas."},
            ],
        },
    )


def _content_he() -> Dict[str, Any]:
    return _apply_locale_patch(
        _content_en(),
        {
            "meta_title": "NoryaAI לרופאים — תקשורת ברורה יותר סביב תוצאות מעבדה",
            "meta_description": "שכבת עזר להצגת תוצאות מעבדה: סיכומים מובנים, הקשר לטווחי ערכים, מסירה רב־לשונית וקובץ PDF לשיתוף. לא כלי אבחון—תוכנן לתמוך בתקשורת קלינית.",
            "hero_badge": "לקלינאים",
            "hero_title": "שיחות ברורות יותר כשחוזרות תוצאות.",
            "hero_desc": "NoryaAI מיועד לדיווח בדיקות מעבדה—לא לצ'אט כללי. הוא עוזר להפוך בדיקות דם שגרתיות להסברים מובנים וידידותיים למטופל, עם הקשר לטווחי ערכים ו־PDF שמוכן לרופא, כדי להפחית בלבול אחרי בדיקות ולשפר הכנה למעקב. הוא תומך בשיקול הדעת שלכם; הוא לא מחליף אותו.",
            "hero_cta_primary": "בקשו הדגמה",
            "hero_cta_secondary": "צפו בדו״ח לדוגמה",
            "how_title": "איך קלינאים משתמשים ב־Norya",
            "what_title": "מה מקבלים בצד הקליני",
            "why_title": "למה זה עוזר ביום־יום",
            "why_lead": "החיכוך סביב בדיקות מעבדה לעתים קרובות נובע ממחסור בזמן להסביר שוב את אותו פאנל בשפה מטופלית.",
            "limits_title": "מה Norya לא מחליף",
            "limits_lead": "שקיפות בונה אמון—במיוחד בסביבה קלינית.",
            "preview_title": "תצוגה מקדימה של פלט ידידותי לרופא",
            "preview_desc": "פריסה להמחשה: מקטעים מובנים ושפה קריאה—תמיד לבחון בהקשר תוכנית הטיפול.",
            "preview_patient_block_title": "סיכום למטופל",
            "preview_patient_block_sample": "«הערכים שלכם ברובם בטווח המקובל. יש מדדים שכדאי לדון בהם בביקור הבא.»",
            "preview_clinical_block_title": "ערכים מובנים",
            "preview_clinical_block_sample": "המוגלובין · גלוקוז · שומנים — כל אחד עם הקשר לטווח והערת מידע קצרה.",
            "preview_sample_link": "פתיחת דף דוחות לדוגמה",
            "preview_disclaimer": "דוגמה להמחשה בלבד; לא רישום מטופל אמיתי.",
            "preview_sheet_label": "דוגמה",
            "preview_range_cue": "הקשר התייחסות להמחשה בלבד",
            "insights_title": "תוכנן עבור צוותי תקשורת קלינית",
            "insights_intro": "יעדי עיצוב מעשיים שמצטברים ממרפאות עמוסות—לא הסמכות או הבטחות לתוצאות אישיות.",
            "nav_strip_title": "גם לגלות",
            "nav_strip_sample": "דוחות לדוגמה",
            "nav_strip_trust": "מרכז אמון",
            "nav_strip_security": "אבטחה",
            "nav_strip_methodology": "מתודולוגיה",
            "nav_strip_pricing": "מחירים",
            "nav_strip_compare": "השוואת Norya",
            "nav_strip_clinics": "למרפאות",
            "nav_strip_home": "דף הבית",
            "faq_title": "שאלות נפוצות",
            "final_title": "תנו מבנה לאופן שבו אתם מסבירים בדיקות.",
            "final_desc": "בקשו הדגמה, עיינו בדוגמה או דברו איתנו על תהליכים רב־לשוניים וקליטה במרפאות—במודל מסייע ובגישת אמון תחילה.",
            "final_cta_demo": "בקשו הדגמה",
            "final_cta_sample": "צפו בדו״ח לדוגמה",
            "final_cta_clinic": "יצירת קשר לשימוש במרפאה",
            "how_cards": [
                {"title": "אחרי בדיקה", "body": "כשהפאנל צפוף, סיכום מובנה עוזר לפני ההודעה או הביקור הבא.", "icon": "📋"},
                {"title": "הכנה למעקב", "body": "מה השתנה ומה יציב—כדי לפתוח ביקור בהקשר משותף.", "icon": "📅"},
                {"title": "מדדים מורכבים בשפה פשוטה", "body": "קיצורים וחריגות ניסוח זהירים לקריאה בבית.", "icon": "💬"},
                {"title": "מסירה רב־לשונית", "body": "אותו דוח מובנה ב־9+ שפות למטופלים בינלאומיים ולמשפחות.", "icon": "🌐"},
            ],
            "what_items": [
                {"title": "דוח מובנה", "body": "מקטעים לסיכום, ערכים והקשר—פורמט עקבי במקום טקסט ארוך."},
                {"title": "סיכום ממצאים עיקריים", "body": "הדגשות מסודרות לסריקה מהירה לפני התאמת הדרכה."},
                {"title": "הצגה מודעת לטווחי ערכים", "body": "ערכים ממוסגרים בשפה זהירה המתאימה להסברה."},
                {"title": "PDF לשיתוף", "body": "קובץ נקי להדפסה, שמירה או הבאה לביקור."},
                {"title": "מסירה עם אימות QR", "body": "בדיקת מקור אופציונלית כאשר משתמשים בתהליך הזה."},
                {"title": "השוואת מגמה (כשזמין)", "body": "כשבדיקות קודמות קיימות בתוכניות נתמכות, עשוי להופיע הקשר שינוי לאור זמן—למידע בלבד."},
                {"title": "שכבת הסבר ידידותית למטופל", "body": "מסגרת בשפה פשוטה בין ביקורים; ההחלטות הקליניות נשארות אצלכם."},
                {"title": "פלט רב־לשוני", "body": "יותר מ־9 שפות דיווח כדי להתאים לאוכלוסייה."},
            ],
            "why_points": [
                "שיחות ברורות יותר עם פחות חזרה על אותן הסברים.",
                "מסירה מקצועית יותר עם PDF מובנה.",
                "הבנה בסיסית טובה יותר לפני וידאו־ביקור או ביקור קצר.",
                "תקשורת קלה יותר למטיילים ולבתים רב־לשוניים.",
                "הצגה נקייה של בדיקות שגרה בלי לעצב מחדש את דוח ה־EMR.",
            ],
            "limits_items": [
                "לא מחליף שיקול דעת קליני.",
                "לא מנוע אבחון או טיפול.",
                "לא מחליף עיון רופא בנתוני מעבדה גולמיים.",
                "נועד לתמוך בהבנה, בהכנה ובתקשורת.",
            ],
            "insights": [
                {"label": "פחות בלבול אחרי סקר", "quote": "מטופלים יוצאים עם מספרים שלא יודעים לפרש. תקציר תמציתי יכול להפחית הודעות חרדה לפני שיש זמן לתיק."},
                {"label": "מסירות רב־לשוניות חלקות יותר", "quote": "כששפת הדוח מתאימה להעדפת המטופל, לרוב יש פחות סבבי הסבר."},
                {"label": "מעקב מכוון יותר", "quote": "להדגיש מה לעקוב או מה השתפר יכול להפוך ביקורי המשך לשיתופיים יותר."},
            ],
        },
    )


def _content_hi() -> Dict[str, Any]:
    return _apply_locale_patch(
        _content_en(),
        {
            "meta_title": "डॉक्टरों के लिए NoryaAI — स्पष्ट लैब संवाद",
            "meta_description": "लैब परिणामों के लिए सहायक परत: संरचित सार, संदर्भ सीमा-जागरूक प्रस्तुति, बहुभाषी हैंडऑफ और साझा करने योग्य PDF. निदान उपकरण नहीं—क्लिनिकल संचार का समर्थन।",
            "hero_badge": "क्लिनिशियनों के लिए",
            "hero_title": "जब रिपोर्ट लौटे, तब स्पष्ट बातचीत।",
            "hero_desc": "NoryaAI सामान्य चैट नहीं, प्रयोगशाला रिपोर्टिंग के लिए बना है। यह रूटीन ब्लड वर्क को संरचित, मरीज-मित्र व्याख्या, संदर्भ रेंज और डॉक्टर-तैयार PDF में बदलने में मदद करता है ताकि जाँच के बाद भ्रम कम हो और फॉलो-अप बेहतर तैयार हो। यह आपके निर्णय का समर्थन करता है; इसकी जगह नहीं लेता।",
            "hero_cta_primary": "डेमो का अनुरोध करें",
            "hero_cta_secondary": "नमूना रिपोर्ट देखें",
            "how_title": "क्लिनिशियन Norya का उपयोग कैसे करते हैं",
            "what_title": "क्लिनिकल पक्ष पर आपको क्या मिलता है",
            "why_title": "दैनिक अभ्यास में यह क्यों मददगार है",
            "why_lead": "अक्सर समस्या विज्ञान नहीं, बल्कि मरीज की भाषा में उसी पैनल को दोहराने का कम समय है।",
            "limits_title": "Norya क्या नहीं करता",
            "limits_lead": "पारदर्शिता भरोसा बनाती है—विशेषकर क्लिनिकल सेटिंग में।",
            "preview_title": "डॉक्टर-अनुकूल आउटपुट पूर्वावलोकन",
            "preview_desc": "नमूना लेआउट: संरचित खंड और पढ़ने योग्य भाषा—हमेशा आपकी देखभाल योजना के संदर्भ में समीक्षित करें.",
            "preview_patient_block_title": "मरीज-उन्मुख सारांश",
            "preview_patient_block_sample": "«आपके मान अधिकतर सामान्य सीमा में हैं। कुछ मार्कर अगली विजिट पर चर्चा के योग्य हैं।»",
            "preview_clinical_block_title": "संरचित मान",
            "preview_clinical_block_sample": "Hb · ग्लूकोज · लिपिड — प्रत्येक में सीमा संदर्भ और संक्षिप्त शैक्षिक नोट।",
            "preview_sample_link": "नमूना रिपोर्ट हब खोलें",
            "preview_disclaimer": "चित्रण के लिए नमूना; वास्तविक रोगी रिकॉर्ड नहीं।",
            "preview_sheet_label": "नमूना",
            "preview_range_cue": "चित्रण हेतु संदर्भ सीमा",
            "insights_title": "क्लिनिकल संचार टीमों के लिए डिज़ाइन",
            "insights_intro": "व्यस्त प्रैक्टिस से प्राप्त व्यावहारिक डिज़ाइन लक्ष्य—व्यक्तिगत परिणाम का दावा नहीं।",
            "nav_strip_title": "यह भी देखें",
            "nav_strip_sample": "नमूना रिपोर्ट",
            "nav_strip_trust": "ट्रस्ट सेंटर",
            "nav_strip_security": "सुरक्षा",
            "nav_strip_methodology": "कार्यप्रणाली",
            "nav_strip_pricing": "मूल्य निर्धारण",
            "nav_strip_compare": "Norya की तुलना",
            "nav_strip_clinics": "क्लिनिक के लिए",
            "nav_strip_home": "होम",
            "faq_title": "अक्सर पूछे जाने वाले प्रश्न",
            "final_title": "लैब समझाने के तरीके को संरचित करें।",
            "final_desc": "डेमो माँगें, नमूना देखें, या बहुभाषी वर्कफ़्लो और क्लिनिक ऑनबोर्डिंग पर बात करें—विश्वास-प्रथम सहायक मॉडल पर।",
            "final_cta_demo": "डेमो का अनुरोध करें",
            "final_cta_sample": "नमूना रिपोर्ट देखें",
            "final_cta_clinic": "क्लिनिक उपयोग के लिए संपर्क",
            "how_cards": [
                {"title": "जाँच के बाद स्पष्टीकरण", "body": "जब पैनल घना हो, संरचित सार अगले संदेश या विजिट से पहले मदद करता है।", "icon": "📋"},
                {"title": "फॉलो-अप की तैयारी", "body": "क्या बदला, क्या स्थिर रहा—साझा संदर्भ से परामर्श शुरू करें।", "icon": "📅"},
                {"title": "जटिल मार्कर साधारण भाषा में", "body": "संक्षिप्ताक्षर और असामान्य मानों को सावधानीपूर्ण शब्दों में।", "icon": "💬"},
                {"title": "बहुभाषी हैंडऑफ", "body": "9+ भाषाओं में वही संरचित रिपोर्ट—अंतर्राष्ट्रीय मरीजों और परिवारों के लिए।", "icon": "🌐"},
            ],
            "what_items": [
                {"title": "संरचित रिपोर्ट आउटपुट", "body": "सार, मान और संदर्भ के खंड—सुसंगत फ़ॉर्मेटिंग।"},
                {"title": "मुख्य निष्कर्ष सारांश", "body": "सलाह व्यक्तिगत करने से पहले त्वरित स्कैन के लिए प्राथमिकता।"},
                {"title": "संदर्भ-सीमा जागरूक प्रस्तुति", "body": "मरीज शिक्षा के लिए संतुलित भाषा में मान।"},
                {"title": "साझा योग्य PDF", "body": "साफ़ फ़ाइल छापने, सहेजने या अपॉइंटमेंट पर लाने के लिए।"},
                {"title": "QR-सत्यापित वितरण", "body": "जब आप उस प्रवाह का उपयोग करें तो वैकल्पिक प्रामाणिकता जाँच।"},
                {"title": "ट्रेंड तुलना (जब आसान हो)", "body": "समर्थित योजनाओं में पूर्व विश्लेषण होने पर समय के साथ परिवर्तन संदर्भ दिख सकता है—केवल सूचनात्मक।"},
                {"title": "मरीज-मित्र व्याख्या परत", "body": "विजिट के बीच सरल भाषा की संरचना; नैदानिक निर्णय आपके पास।"},
                {"title": "बहुभाषी आउटपुट", "body": "आपकी आबादी के अनुरूप 9+ रिपोर्ट भाषाएँ।"},
            ],
            "why_points": [
                "कम दोहराए गए स्पष्टीकरण के साथ स्पष्ट संवाद।",
                "संरचित PDF साझा करते समय अधिक व्यावसायिक हैंडऑफ।",
                "टेलीहेल्थ या छोटी विजिट से पहले बेहतर आधारभूत समझ।",
                "यात्रियों और बहुभाषी परिवारों के लिए आसान संचार।",
                "EMR को डिज़ाइन प्रोजेक्ट बनाए बिना रूटीन ब्लड वर्क की साफ़ प्रस्तुति।",
            ],
            "limits_items": [
                "नैदानिक निर्णय का स्थान नहीं लेता।",
                "निदान या उपचार इंजन नहीं है।",
                "कच्चे लैब डेटा की चिकित्सक समीक्षा का स्थान नहीं लेता।",
                "समझ, तैयारी और संचार का समर्थन करने के लिए बना है।",
            ],
            "insights": [
                {"label": "स्क्रीनिंग के बाद कम भ्रम", "quote": "मरीज अक्सर ऐसे नंबर लेकर जाते हैं जिन्हें वे नहीं समझते। संक्षिप्त संरचित सार चार्ट समय से पहले चिंतित संदेश कम कर सकता है।"},
                {"label": "अधिक सहज बहुभाषी हैंडऑफ", "quote": "जब रिपोर्ट की भाषा मरीज की पसंद से मेल खाती है, अक्सर कम दौर लगते हैं।"},
                {"label": "अधिक जानबूझकर फॉलो-अप", "quote": "निगरानी या सुधार पर प्रकाश डालने से लौटने वाली विज़िट अधिक सहयोगी लग सकती हैं।"},
            ],
        },
    )


def _content_ar() -> Dict[str, Any]:
    return _apply_locale_patch(
        _content_en(),
        {
            "meta_title": "NoryaAI للأطباء — تواصل أوضح حول نتائج المختبر",
            "meta_description": "طبقة مساعدة لنتائج المختبر: ملخصات منظمة، عرض يراعي مراجع القيم، تسليم متعدد اللغات وملف PDF قابل للمشاركة. ليس أداة تشخيص—صُمم لدعم التواصل السريري.",
            "hero_badge": "لمقدمي الرعاية السريرية",
            "hero_title": "حوارات أوضح عند عودة التحاليل.",
            "hero_desc": "صُمم NoryaAI لتقارير المختبر—وليس للمحادثة العامة. يساعد على تحويل تحاليل الدم الروتينية إلى شروح منظمة ولغة يفهمها المريض، مع سياق النطاقات المرجعية وملفات PDF جاهزة لك لتقليل الارتباك بعد الفحوصات والاستعداد للمتابعة بشكل أفضل. يدعم حكمك السريري؛ ولا يحل محله.",
            "hero_cta_primary": "طلب عرض توضيحي",
            "hero_cta_secondary": "عرض تقرير نموذجي",
            "how_title": "كيف يستخدم المُرْقِّمُون Norya",
            "what_title": "ما الذي تحصل عليه في الجانب السريري",
            "why_title": "لماذا يساعد ذلك يومياً",
            "why_lead": "الاحتكاك غالباً ليس حول العلم—بل حول الوقت القليل لإعادة شرح نفس اللوحة بلغة المريض.",
            "limits_title": "ما لا يحلّه Norya محلّه",
            "limits_lead": "الشفافية تبني الثقة—خصوصاً في البيئة السريرية.",
            "preview_title": "معاينة مخرجات مناسبة للأطباء",
            "preview_desc": "تخطيط توضيحي: أقسام منظمة ولغة مقروءة—يُراجع دائماً في سياق خطة الرعاية.",
            "preview_patient_block_title": "ملخص موجّه للمريض",
            "preview_patient_block_sample": "«قيمك غالباً ضمن النطاقات المعتادة. هناك مؤشرات يستحق مناقشتها في الزيارة القادمة.»",
            "preview_clinical_block_title": "قيم منظمة",
            "preview_clinical_block_sample": "الهيموغلوبين · الجلوكوز · الدهونيات — لكل منها سياق نطاق وملاحظة تعليمية قصيرة.",
            "preview_sample_link": "فتح مركز تقارير نموذجية",
            "preview_disclaimer": "مثال للتوضيح؛ ليس سجلاً حقيقياً.",
            "preview_sheet_label": "عيّنة",
            "preview_range_cue": "سياق مرجعي توضيحي",
            "insights_title": "صُمم لفرق التواصل السريري",
            "insights_intro": "أهداف تصميم عملية نسمعها من عيادات مشغولة—وليست شهادات أو وعوداً بنتائج فردية.",
            "nav_strip_title": "استكشف أيضاً",
            "nav_strip_sample": "تقارير نموذجية",
            "nav_strip_trust": "مركز الثقة",
            "nav_strip_security": "الأمن",
            "nav_strip_methodology": "المنهجية",
            "nav_strip_pricing": "التسعير",
            "nav_strip_compare": "مقارنة Norya",
            "nav_strip_clinics": "للعيادات",
            "nav_strip_home": "الرئيسية",
            "faq_title": "الأسئلة الشائعة",
            "final_title": "نظّم الطريقة التي تشرح بها التحاليل.",
            "final_desc": "اطلب عرضاً، راجع نموذجاً، أو تحدث معنا عن تدفقات متعددة اللغات واستقرار العيادات—ضمن نموذج مساعد يضع الثقة أولاً.",
            "final_cta_demo": "طلب عرض توضيحي",
            "final_cta_sample": "عرض تقرير نموذجي",
            "final_cta_clinic": "تواصل لاستخدام العيادة",
            "how_cards": [
                {"title": "بعد الفحص", "body": "عندما يعود اللوح كثيف الأرقام، يساعد ملخص منظم قبل الرسالة أو الموعد التالي.", "icon": "📋"},
                {"title": "تحضير المتابعة", "body": "ما الذي تغيّر وما بقي مستقراً—لتبدأ الاستشارة بسياق مشترك.", "icon": "📅"},
                {"title": "مؤشرات معقدة بلغة بسيطة", "body": "اختصارات وقيم خارج النطاق بصياغة حذرة لقراءة المنزل.", "icon": "💬"},
                {"title": "تسليم متعدد اللغات", "body": "نفس التقرير المنظّم بأكثر من 9 لغات للمرضى الدوليين والعائلات.", "icon": "🌐"},
            ],
            "what_items": [
                {"title": "مخرجات تقرير منظمة", "body": "أقسام للملخص والقيم والسياق—تنسيق متسق بدلاً من نص غير منظم."},
                {"title": "ملخص للنتائج الرئيسية", "body": "نقاط رئيسية مرتبة للمسح السريع قبل تخصيص النصائح."},
                {"title": "عرض يراعي نطاق المرجع", "body": "قيم ضمن إطار لغوي حذر مناسب للتثقيف."},
                {"title": "PDF قابل للمشاركة", "body": "ملف نظيف للطباعة أو الحفظ أو إحضاره للموعد."},
                {"title": "تسليم يُتحقق منه عبر QR", "body": "تحقق اختياري من الأصالة عند استخدام ذلك المسار."},
                {"title": "مقارنة مسار (عند توفرها)", "body": "عند وجود تحاليل سابقة في خطط مدعومة قد يظهر سياق التغير الزمني—للمعلومية فقط."},
                {"title": "طبقة شرح مناسبة للمريض", "body": "هيكل بلغة مبسطة بين الزيارات؛ القرار السريري يبقى لديك."},
                {"title": "دعم مخرجات متعددة اللغات", "body": "أكثر من 9 لغات تقارير لتناسب مجتمعك."},
            ],
            "why_points": [
                "حوارات أوضح مع عبء أقل من تكرار الشرح.",
                "تسليم أكثر احترافية عند مشاركة PDF منظم.",
                "فهم أفضل قبل الاستشارة عن بُعد أو الزيارات القصيرة.",
                "تواصل أسهل للمسافرين والأسر متعددة اللغات.",
                "عرض أنظف لتحاليل الدم الروتينية دون تحويل EMR إلى مشروع تصميم.",
            ],
            "limits_items": [
                "لا يحل محل الحكم السريري.",
                "ليس محرك تشخيص أو علاج.",
                "لا يحل محل مراجعة الطبيب للبيانات الخام.",
                "مُصمم لدعم الفهم والتحضير والتواصل.",
            ],
            "insights": [
                {"label": "ارتباك أقل بعد الفحص", "quote": "غالباً يغادر المرضى بأرقام لا يفسرونها. ملخص موجز منظم يقلل الرسائل القلقة قبل وقت السجل."},
                {"label": "تسليمات متعددة اللغات أنعم", "quote": "عندما تطابق لغة التقرير تفضيل المريض، غالباً تقل جولات إعادة الشرح."},
                {"label": "متابعات أكثر قصدية", "quote": "إبراز ما يُراقب أو ما تحسّن يجعل زيارات العودة أكثر تعاونية."},
            ],
        },
    )


def get_for_doctors_landing_ui(lang_code: str) -> Dict[str, Any]:
    lc = (lang_code or "en").strip().lower()
    if lc not in SUPPORTED_LANGS:
        lc = "en"
    builders = {
        "en": _content_en,
        "tr": _content_tr,
        "de": _content_de,
        "fr": _content_fr,
        "it": _content_it,
        "es": _content_es,
        "he": _content_he,
        "hi": _content_hi,
        "ar": _content_ar,
    }
    return builders[lc]()

