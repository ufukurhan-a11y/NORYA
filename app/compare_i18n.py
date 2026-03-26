# -*- coding: utf-8 -*-
"""Competitor comparison pages — i18n content and configuration.

Data-driven system: all comparison content lives here.
Templates consume the dicts returned by the public API functions.
"""
from __future__ import annotations

# ── Configuration ────────────────────────────────────────────────
COMPARE_LANGS = ("en", "tr", "de", "fr", "es", "it", "he", "hi", "ar")
RTL_LANGS = frozenset({"he", "ar"})

COMPARE_SLUGS = (
    "norya-vs-chatgpt-for-blood-tests",
    "norya-vs-bloodgpt",
    "norya-vs-kantesti",
    "norya-vs-siphox-health",
    "norya-vs-wizey",
    "norya-vs-generic-ai",
)

_ROW_KEYS = (
    "report_upload", "reference_ranges", "units_formatting",
    "output_structure", "multilingual", "doctor_summary",
    "privacy", "workflow", "guided_flow",
)

_OG: dict[str, str] = {
    "en": "en_US", "tr": "tr_TR", "de": "de_DE", "fr": "fr_FR",
    "es": "es_ES", "it": "it_IT", "he": "he_IL", "hi": "hi_IN", "ar": "ar_SA",
}

_COMPARE_VISUALS: dict[str, dict] = {
    "norya-vs-chatgpt-for-blood-tests": {
        "image": "/static/images/og-blood-test-explained.png",
        "accent": "#10b981",
        "glow": "rgba(16,185,129,0.34)",
        "mark": "GPT",
    },
    "norya-vs-bloodgpt": {
        "image": "/static/images/og-cbc-guide.png",
        "accent": "#ef4444",
        "glow": "rgba(239,68,68,0.30)",
        "mark": "BGT",
    },
    "norya-vs-kantesti": {
        "image": "/static/images/og-upload-blood-test.png",
        "accent": "#f97316",
        "glow": "rgba(249,115,22,0.32)",
        "mark": "TR",
    },
    "norya-vs-siphox-health": {
        "image": "/static/images/clinic-enterprise-visual.png",
        "accent": "#6366f1",
        "glow": "rgba(99,102,241,0.32)",
        "mark": "LAB",
    },
    "norya-vs-wizey": {
        "image": "/static/images/og-sample-reports.png",
        "accent": "#8b5cf6",
        "glow": "rgba(139,92,246,0.32)",
        "mark": "WZ",
    },
    "norya-vs-generic-ai": {
        "image": "/static/images/hero-globe.png",
        "accent": "#0f172a",
        "glow": "rgba(15,23,42,0.28)",
        "mark": "AI",
    },
}

# ── Accuracy badge (detail pages) ─────────────────────────────────
_ACCURACY_BADGE: dict[str, dict] = {
    "en": {"value": "98.7%", "label": "Result accuracy", "sub": "Verified with laboratory data"},
    "tr": {"value": "%98,7", "label": "Sonuç doğruluğu", "sub": "Laboratuvar verileriyle doğrulanmış"},
    "de": {"value": "98,7%", "label": "Ergebnisgenauigkeit", "sub": "Mit Labordaten verifiziert"},
    "fr": {"value": "98,7%", "label": "Précision des résultats", "sub": "Vérifiée avec des données de laboratoire"},
    "es": {"value": "98,7%", "label": "Precisión de resultados", "sub": "Verificada con datos de laboratorio"},
    "it": {"value": "98,7%", "label": "Accuratezza dei risultati", "sub": "Verificata con dati di laboratorio"},
    "he": {"value": "98.7%", "label": "דיוק תוצאות", "sub": "אומת עם נתוני מעבדה"},
    "hi": {"value": "98.7%", "label": "परिणाम सटीकता", "sub": "प्रयोगशाला डेटा से सत्यापित"},
    "ar": {"value": "98.7%", "label": "دقة النتائج", "sub": "تم التحقق منها بواسطة بيانات مخبرية"},
}

# ── UI strings (nav, breadcrumbs, footer, section labels) ────────
_UI: dict[str, dict] = {
    "en": {
        "home": "Home", "compare": "Compare", "how_it_works": "How it works",
        "pricing": "Pricing", "blog": "Blog", "analyze": "Analyze",
        "faq_heading": "Frequently Asked Questions",
        "related_heading": "Related Comparisons",
        "badge": "Honest comparison · NoryaAI",
        "comparison_title": "Side-by-side comparison",
        "comparison_sub": "How the two approaches differ across the features that matter most when you are looking at blood test results.",
        "disclaimer": "NoryaAI does not provide medical diagnoses. All content is for educational and informational purposes only.",
        "privacy": "Privacy", "terms": "Terms of use",
    },
}

# ── Comparison row labels (same structure for every competitor) ───
_LABELS: dict[str, dict] = {
    "en": {
        "report_upload": "Report upload",
        "reference_ranges": "Reference ranges",
        "units_formatting": "Units and lab formatting",
        "output_structure": "Output structure",
        "multilingual": "Multilingual reports",
        "doctor_summary": "Doctor-ready summary",
        "privacy": "Privacy and data handling",
        "workflow": "Blood-test specific workflow",
        "guided_flow": "Workflow type",
    },
}

# ── Norya comparison cells (same for ALL competitors) ────────────
_NORYA: dict[str, dict] = {
    "en": {
        "report_upload": "Upload PDF, snap a photo, or paste text — values and ranges are parsed automatically",
        "reference_ranges": "Reference ranges displayed for every value — normal, low, or high — clearly labeled",
        "units_formatting": "Recognizes common lab units, panel structures, and result formats automatically",
        "output_structure": "Structured health score, category breakdown, and flagged markers — consistent every time",
        "multilingual": "Full reports in 9+ languages with medical context preserved throughout",
        "doctor_summary": "Doctor-ready PDF with QR verification — print it, save it, or share it",
        "privacy": "GDPR/KVKK compliant — encrypted, never sold, never used for training",
        "workflow": "Dedicated upload, analysis, and report pipeline built specifically for lab results",
        "guided_flow": "Guided, structured analysis — upload once and get a complete report, no prompt needed",
    },
}

# ── Shared "Why Norya" (reused across all competitor pages) ──────
_WHY: dict[str, dict] = {
    "en": {
        "title": "Why people choose NoryaAI for blood tests",
        "sub": "When accuracy, structure, and a clean next-step matter more than a general conversation.",
        "items": [
            {"title": "Upload once, get a structured report", "desc": "No prompt engineering, no reformatting. Upload your lab results and receive a health score, category breakdown, and flagged markers — automatically."},
            {"title": "Consistent format you can compare over time", "desc": "Every report follows the same structure, so you can track changes across multiple blood tests and spot trends at a glance."},
            {"title": "Doctor-ready PDF you can actually bring", "desc": "A clean, professional summary with QR verification. Print it or share it digitally — designed to be useful at your next appointment."},
            {"title": "Your language, your report", "desc": "Choose from 9+ languages and get your full report in the one that feels most natural to you — with medical context intact."},
        ],
    },
}

# ── Shared CTA (reused across all competitor pages) ──────────────
_CTA: dict[str, dict] = {
    "en": {
        "title": "Ready to try a structured blood test report?",
        "sub": "Upload your lab results and see the difference a purpose-built analyzer makes.",
        "primary": "Upload and analyze now",
        "secondary": "View pricing plans",
        "hero_primary": "Analyze my blood test",
        "hero_secondary": "See a sample report",
    },
}

# ── Hub page content ─────────────────────────────────────────────
_HUB: dict[str, dict] = {
    "en": {
        "meta_title": "Best AI for Blood Test Results? Compare NoryaAI, ChatGPT, and Alternatives | NoryaAI",
        "meta_description": "Compare NoryaAI with ChatGPT, BloodGPT, Kantesti, SiPhox Health, Wizey, and other AI tools for blood test interpretation. Honest side-by-side comparisons for structured reports, privacy, and reference-range-aware analysis.",
        "hero_title": "Compare AI Tools for Blood Test Results",
        "hero_sub": "Trying to decide which AI tool is best for blood test interpretation? Compare NoryaAI with ChatGPT and other alternatives to see which workflow, output format, and privacy approach fit your needs.",
        "trust_stats": [
            {"value": "98.7%", "label": "Result accuracy", "sub": "Verified with laboratory data"},
            {"value": "9+", "label": "Languages", "sub": "Full reports with medical context"},
            {"value": "QR", "label": "Verified PDF", "sub": "Doctor-ready shareable summary"},
        ],
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Compare ChatGPT vs NoryaAI for blood test interpretation, lab report upload support, and structured report output.", "link_text": "Read full comparison"},
            {"slug": "norya-vs-bloodgpt", "name": "BloodGPT", "summary": "A blood-test-focused AI chat workflow compared with NoryaAI's structured reports, multilingual output, and doctor-ready summaries.", "link_text": "Read full comparison"},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Two blood test analysis platforms compared — multilingual structured reports vs a Turkish-focused service.", "link_text": "Read full comparison"},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "At-home biomarker test kits vs structured analysis of your existing lab results — two different approaches.", "link_text": "Read full comparison"},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "How NoryaAI's structured report workflow compares to Wizey's approach to blood test analysis.", "link_text": "Read full comparison"},
            {"slug": "norya-vs-generic-ai", "name": "Generic AI", "summary": "See how a purpose-built blood test analyzer compares with generic AI chatbots for blood test results and lab report questions.", "link_text": "Read full comparison"},
        ],
        "hub_faqs": [
            {"q": "Which tool is best for understanding blood test results?", "a": "It depends on what you need. For structured, consistent reports with health scores and doctor-ready summaries, NoryaAI is purpose-built. General AI chatbots are better for broad health education, while platforms like SiPhox Health focus on at-home testing."},
            {"q": "Are these comparisons fair and honest?", "a": "We aim for transparency. Where a competitor's features are not clearly disclosed, we say so rather than guessing. We encourage you to try different tools and decide based on your own experience."},
            {"q": "Can I use NoryaAI together with other tools?", "a": "Yes. NoryaAI is designed to complement your health workflow. You can use it alongside other platforms, and you should always consult a qualified doctor for medical decisions."},
        ],
        "matrix_title": "Blood test AI comparison table",
        "matrix_sub": "A quick side-by-side view of which tool is better for blood test interpretation, report uploads, structured output, and privacy.",
        "matrix_row_labels": [
            "Best use case",
            "Blood-test-specific workflow",
            "File upload flow",
            "Reference-range-aware structure",
            "Structured output",
            "Multilingual result support",
            "Doctor-ready / shareable summary",
            "Privacy / educational framing",
            "Suitable for preparing for a clinician visit",
            "Result accuracy",
        ],
        "matrix_columns": [
            {"key": "norya", "name": "NoryaAI", "slug": None},
            {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"},
            {"key": "bloodgpt", "name": "BloodGPT", "slug": "norya-vs-bloodgpt"},
            {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"},
            {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"},
            {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"},
            {"key": "generic", "name": "Generic AI", "slug": "norya-vs-generic-ai"},
        ],
        "matrix_rows": [
            {"norya": "Structured blood test analysis", "chatgpt": "General health Q&A", "bloodgpt": "Blood-test-focused chat Q&A", "kantesti": "Blood test interpretation", "siphox": "At-home biomarker testing", "wizey": "Blood test analysis", "generic": "General health Q&A"},
            {"norya": "Strong", "chatgpt": "Limited", "bloodgpt": "Available", "kantesti": "Available", "siphox": "Partial", "wizey": "Available", "generic": "Limited"},
            {"norya": "PDF, photo, or text", "chatgpt": "Copy-paste into prompt", "bloodgpt": "Not clearly disclosed", "kantesti": "Available", "siphox": "Own test kits only", "wizey": "Not clearly disclosed", "generic": "Copy-paste into prompt"},
            {"norya": "Strong", "chatgpt": "Limited", "bloodgpt": "Partial", "kantesti": "Partial", "siphox": "Own panels only", "wizey": "Not clearly disclosed", "generic": "Limited"},
            {"norya": "Health score + categories", "chatgpt": "Free-form text", "bloodgpt": "Chat-style answer", "kantesti": "Not clearly disclosed", "siphox": "Dashboard view", "wizey": "Not clearly disclosed", "generic": "Free-form text"},
            {"norya": "9+ languages", "chatgpt": "Partial", "bloodgpt": "Not clearly disclosed", "kantesti": "Primarily Turkish", "siphox": "Primarily English", "wizey": "Not clearly disclosed", "generic": "Partial"},
            {"norya": "PDF with QR verification", "chatgpt": "Not available", "bloodgpt": "Not clearly disclosed", "kantesti": "Not clearly disclosed", "siphox": "Not clearly disclosed", "wizey": "Not clearly disclosed", "generic": "Not available"},
            {"norya": "GDPR/KVKK · educational only", "chatgpt": "May store for training", "bloodgpt": "See their policy", "kantesti": "See their policy", "siphox": "See their policy", "wizey": "See their policy", "generic": "May store for training"},
            {"norya": "Strong", "chatgpt": "Partial", "bloodgpt": "Partial", "kantesti": "Available", "siphox": "Limited", "wizey": "Not clearly disclosed", "generic": "Partial"},
            {"norya": "98.7% · lab-verified", "chatgpt": "Not disclosed", "bloodgpt": "Not disclosed", "kantesti": "Not disclosed", "siphox": "Not disclosed", "wizey": "Not disclosed", "generic": "Not disclosed"},
        ],
        "suits_title": "Which tool suits whom?",
        "suits_items": [
            {"label": "Structured blood test analysis", "text": "If you want a consistent health score, flagged markers, and a doctor-ready PDF from your existing lab results, NoryaAI is purpose-built for that.", "link_slug": None},
            {"label": "General health Q&A", "text": "If you want to ask open-ended health questions, learn about medical terms, or brainstorm questions for your doctor, a general AI chatbot like ChatGPT is a strong choice.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
            {"label": "Comparing lab-report-focused tools", "text": "If you are evaluating platforms that specifically analyze blood test reports, compare NoryaAI with Kantesti and Wizey to see which workflow, language support, and output format fits your needs.", "link_slug": "norya-vs-kantesti"},
        ],
    },
}

# ── Competitor-specific content ──────────────────────────────────
_COMP: dict[str, dict] = {
    "norya-vs-chatgpt-for-blood-tests": {
        "name": "ChatGPT",
        "en": {
            "meta_title": "NoryaAI vs ChatGPT for Blood Test Interpretation | NoryaAI",
            "meta_description": "Compare NoryaAI vs ChatGPT for blood test interpretation. See which tool is better for lab report uploads, reference ranges, structured summaries, privacy, and doctor-ready output.",
            "hero_title": "NoryaAI vs ChatGPT for Blood Test Interpretation",
            "hero_sub": "ChatGPT is useful for general health questions, but NoryaAI is built specifically for blood test results. This comparison shows which tool is better when you need lab-report parsing, structured summaries, and reference-range-aware output.",
            "quick_answer_title": "The short version",
            "quick_answer": "If you want general explanations, ChatGPT can help. If you want blood test interpretation from an actual lab report, NoryaAI is the stronger fit: it reads the report directly, maps values to reference ranges, and generates a structured, doctor-ready summary instead of a free-form chat reply.",
            "cells": {
                "report_upload": "Requires copy-pasting values into a chat prompt; no native lab report parsing pipeline",
                "reference_ranges": "May cite general ranges or hallucinate values; no guarantee they match your lab",
                "units_formatting": "No built-in awareness of lab-specific units or regional result layouts",
                "output_structure": "Free-form text that varies each time — no consistent format for tracking changes",
                "multilingual": "Can translate text on request, but medical nuance may be lost in general translation",
                "doctor_summary": "No downloadable report — you would need to format the conversation yourself",
                "privacy": "Conversations may be stored and used for model training by OpenAI",
                "workflow": "General-purpose chat interface not designed for lab report analysis",
                "guided_flow": "Open-ended conversation — quality depends on how well you write your prompt",
            },
            "helps_title": "When ChatGPT can still help",
            "helps_sub": "ChatGPT is excellent for many tasks. Here is where it genuinely shines.",
            "helps_items": [
                {"icon": "📚", "title": "General health education", "desc": "ChatGPT is great for learning what a biomarker means, how the immune system works, or exploring broad medical concepts."},
                {"icon": "💡", "title": "Brainstorming doctor questions", "desc": "Before a medical appointment, ChatGPT can help you organize your thoughts and prepare questions for your physician."},
                {"icon": "🔍", "title": "Quick medical term lookups", "desc": "If you encounter an unfamiliar term in your report, ChatGPT can explain it instantly in plain language."},
            ],
            "faqs": [
                {"q": "Can ChatGPT analyze my blood test results?", "a": "ChatGPT can discuss blood test values if you type them in, but it does not parse lab reports, cannot verify reference ranges for your specific lab, and may hallucinate medical details. NoryaAI is built specifically to read lab reports and produce consistent, structured analysis."},
                {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions."},
                {"q": "Why not just ask ChatGPT about my lab values?", "a": "You can, but ChatGPT gives a different answer every time, does not track reference ranges, and cannot produce a printable report. NoryaAI generates a consistent health score, flagged markers, and a doctor-ready PDF — every time."},
                {"q": "Can I upload a PDF to ChatGPT for blood test analysis?", "a": "ChatGPT can read PDFs with the Plus plan, but it was not designed to parse lab report structures. NoryaAI is specifically built to extract values, reference ranges, and units from lab reports automatically."},
                {"q": "Is my data safe with ChatGPT vs NoryaAI?", "a": "OpenAI may store and use conversations for model training unless you opt out. NoryaAI is GDPR/KVKK compliant — your data is encrypted, never sold, and never used for training."},
            ],
        },
    },
    "norya-vs-bloodgpt": {
        "name": "BloodGPT",
        "en": {
            "meta_title": "NoryaAI vs BloodGPT for Blood Tests — Honest Comparison | NoryaAI",
            "meta_description": "Compare NoryaAI and BloodGPT for blood test analysis. Structured reports, multilingual output, and doctor-ready PDFs versus a chat-first workflow.",
            "hero_title": "NoryaAI vs BloodGPT for Blood Test Analysis",
            "hero_sub": "BloodGPT is positioned as a blood-test-focused AI experience. NoryaAI is built around structured reports, reference-range-aware analysis, and doctor-ready output. Here is how the two approaches differ.",
            "quick_answer_title": "The short version",
            "quick_answer": "BloodGPT is a chat-first approach built around discussing blood test results in conversation. NoryaAI is a structured upload-and-report workflow: it reads your lab report, maps each marker to reference ranges, and returns a multilingual summary with a health score and doctor-ready PDF. One is conversational; the other is designed for repeatable reporting.",
            "cells": {
                "report_upload": "Chat-first workflow; native report upload support is not clearly disclosed",
                "reference_ranges": "Can discuss ranges in conversation, but lab-specific matching and structure are not clearly disclosed",
                "units_formatting": "May interpret values in chat, but support for different lab layouts and unit formats is not clearly disclosed",
                "output_structure": "Conversation-style answers rather than a fixed report structure",
                "multilingual": "Language coverage is not clearly disclosed",
                "doctor_summary": "Doctor-ready PDF or verified export format is not clearly disclosed",
                "privacy": "Check their policy for storage, retention, and model usage details",
                "workflow": "Blood-test-focused AI chat experience",
                "guided_flow": "Conversational Q&A about blood test results",
            },
            "helps_title": "When BloodGPT may still help",
            "helps_sub": "A chat-first blood test tool may suit users who prefer back-and-forth exploration over a fixed report.",
            "helps_items": [
                {"icon": "💬", "title": "Conversation-first experience", "desc": "If you prefer asking follow-up questions in a chat interface, a blood-test-focused chatbot can feel more natural than a fixed report."},
                {"icon": "🧪", "title": "Blood-test-specific prompts", "desc": "A focused chatbot may offer a narrower context than a generic AI assistant when you want to discuss biomarkers in conversation."},
                {"icon": "⚡", "title": "Quick exploratory answers", "desc": "For rapid back-and-forth brainstorming around lab markers, a conversational interface can be useful before you want a formal summary."},
            ],
            "faqs": [
                {"q": "What is the difference between BloodGPT and NoryaAI?", "a": "BloodGPT appears to focus on blood test interpretation in a chat-style workflow. NoryaAI focuses on structured blood test reports with reference-range-aware analysis, health scores, multilingual output, and doctor-ready PDFs."},
                {"q": "Is a chat interface enough for blood test review?", "a": "It depends on your goal. Chat can be useful for discussion, but if you want a consistent format you can revisit, compare over time, or share with a clinician, a structured report is usually more practical."},
                {"q": "Does NoryaAI diagnose medical conditions?", "a": "No. NoryaAI provides structured, educational explanations of lab values. It does not diagnose conditions or recommend treatment. Always consult a qualified doctor for medical decisions."},
                {"q": "Can I upload a lab report directly to NoryaAI?", "a": "Yes. NoryaAI accepts PDF uploads, photos, and pasted text, then extracts values, units, and reference ranges automatically."},
            ],
        },
    },
    "norya-vs-kantesti": {
        "name": "Kantesti",
        "en": {
            "meta_title": "NoryaAI vs Kantesti — Blood Test Comparison | NoryaAI",
            "meta_description": "How does NoryaAI compare to Kantesti for blood test analysis? Feature comparison of two platforms — upload workflow, report structure, and multilingual support.",
            "hero_title": "NoryaAI vs Kantesti for Blood Test Analysis",
            "hero_sub": "Both NoryaAI and Kantesti help users understand blood test results. Here is an honest comparison of what each platform offers.",
            "quick_answer_title": "The short version",
            "quick_answer": "Kantesti is a blood test analysis service primarily serving Turkish-speaking users. NoryaAI offers a structured, multilingual blood test analysis workflow with health scores, doctor-ready PDFs, and support for 9+ languages. Both aim to make lab results easier to understand.",
            "cells": {
                "report_upload": "Supports lab result input for analysis",
                "reference_ranges": "Provides reference range information for analyzed values",
                "units_formatting": "Handles Turkish lab report formats",
                "output_structure": "Provides analysis results in its own format",
                "multilingual": "Primarily available in Turkish",
                "doctor_summary": "Report format and sharing options not clearly disclosed",
                "privacy": "Data handling policies available on their platform",
                "workflow": "Focused on blood test result interpretation",
                "guided_flow": "Offers its own analysis workflow",
            },
            "helps_title": "When Kantesti may still help",
            "helps_sub": "Different tools work better for different people. Here is where Kantesti may be a good fit.",
            "helps_items": [
                {"icon": "🇹🇷", "title": "Turkish-first experience", "desc": "If you want a platform built primarily for Turkish-speaking users, Kantesti offers a native Turkish interface."},
                {"icon": "🏥", "title": "Local lab familiarity", "desc": "Kantesti may be familiar with specific Turkish laboratory formats and conventions."},
                {"icon": "📋", "title": "Straightforward analysis", "desc": "For straightforward blood test interpretation without multilingual needs, Kantesti may serve well."},
            ],
            "faqs": [
                {"q": "What is Kantesti?", "a": "Kantesti is a blood test analysis platform focused on helping users understand their lab results. It primarily serves Turkish-speaking users."},
                {"q": "How is NoryaAI different from Kantesti?", "a": "NoryaAI offers structured health scores, doctor-ready PDFs with QR verification, multilingual reports in 9+ languages, and supports multiple lab report formats from around the world. Your specific needs determine which platform fits better."},
                {"q": "Is NoryaAI available in Turkish?", "a": "Yes. NoryaAI offers full blood test analysis and reports in Turkish, along with 9+ other languages."},
                {"q": "Does NoryaAI work with Turkish lab reports?", "a": "Yes. NoryaAI recognizes Turkish lab report formats, units, and panel structures, and can generate reports in Turkish or any supported language."},
                {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions."},
            ],
        },
    },
    "norya-vs-siphox-health": {
        "name": "SiPhox Health",
        "en": {
            "meta_title": "NoryaAI vs SiPhox Health — Blood Test Analysis Comparison | NoryaAI",
            "meta_description": "NoryaAI vs SiPhox Health: at-home testing kits vs structured lab report analysis. Compare approaches to understanding your blood test results.",
            "hero_title": "NoryaAI vs SiPhox Health",
            "hero_sub": "SiPhox Health offers at-home biomarker testing kits. NoryaAI analyzes your existing lab results and turns them into structured, actionable reports. Here is how they compare.",
            "quick_answer_title": "The short version",
            "quick_answer": "SiPhox Health and NoryaAI serve different stages of health testing. SiPhox provides at-home test kits to collect biomarker samples, while NoryaAI analyzes lab results you already have — from any lab, any format — and produces a structured health report. They can complement each other.",
            "cells": {
                "report_upload": "Provides results from their own at-home test kits — not designed for external lab reports",
                "reference_ranges": "Shows ranges for their specific biomarker panels",
                "units_formatting": "Standardized to their own test kit format",
                "output_structure": "Dashboard and results within their platform",
                "multilingual": "Primarily available in English",
                "doctor_summary": "Results viewable within their platform; export options not clearly disclosed",
                "privacy": "Data handling policies available on their website",
                "workflow": "End-to-end testing: order kit, collect sample, receive results",
                "guided_flow": "Guided at-home testing workflow tied to their proprietary kits",
            },
            "helps_title": "When SiPhox Health may be a better fit",
            "helps_sub": "SiPhox Health and NoryaAI serve different needs. Here is where SiPhox shines.",
            "helps_items": [
                {"icon": "🏠", "title": "At-home convenience", "desc": "If you want to test without visiting a lab, SiPhox Health sends a kit to your door."},
                {"icon": "📊", "title": "Recurring monitoring", "desc": "SiPhox offers subscription-based testing for regular biomarker tracking over time."},
                {"icon": "🔬", "title": "Curated panels", "desc": "Their test panels are designed around specific health goals like longevity or metabolic health."},
            ],
            "faqs": [
                {"q": "What is SiPhox Health?", "a": "SiPhox Health offers at-home biomarker testing kits. You order a kit, collect a sample at home, and receive results through their platform."},
                {"q": "Can NoryaAI analyze SiPhox Health results?", "a": "If you receive lab results from SiPhox or any other provider, you can upload them to NoryaAI for a structured analysis with health scores and a doctor-ready PDF."},
                {"q": "Do I need a test kit to use NoryaAI?", "a": "No. NoryaAI works with lab results you already have — from any lab, any country. Upload a PDF, photo, or paste text, and you get a structured report."},
                {"q": "Can I use both SiPhox Health and NoryaAI?", "a": "Yes. You can use SiPhox to collect your samples and then upload the results to NoryaAI for an additional structured analysis with health scores and a shareable PDF."},
                {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions."},
            ],
        },
    },
    "norya-vs-wizey": {
        "name": "Wizey",
        "en": {
            "meta_title": "NoryaAI vs Wizey — Blood Test Analysis Comparison | NoryaAI",
            "meta_description": "How does NoryaAI compare to Wizey for blood test analysis? Side-by-side comparison of structured report features, multilingual support, and workflow.",
            "hero_title": "NoryaAI vs Wizey for Blood Test Analysis",
            "hero_sub": "Both NoryaAI and Wizey help users understand blood test results. Here is an honest, side-by-side comparison of what each platform offers.",
            "quick_answer_title": "The short version",
            "quick_answer": "Wizey offers blood test analysis tools for health insights. NoryaAI provides a structured, upload-based workflow that produces health scores, doctor-ready PDFs, and multilingual reports from any lab format. Different approaches to the same goal.",
            "cells": {
                "report_upload": "Accepts lab results for analysis",
                "reference_ranges": "Provides reference range information",
                "units_formatting": "Lab format support not clearly disclosed",
                "output_structure": "Delivers analysis in its own format",
                "multilingual": "Language support not clearly disclosed",
                "doctor_summary": "Report sharing options not clearly disclosed",
                "privacy": "Data handling policies available on their platform",
                "workflow": "Offers blood test interpretation workflow",
                "guided_flow": "Provides its own analysis process",
            },
            "helps_title": "When Wizey may still help",
            "helps_sub": "Different tools suit different preferences. Here is where Wizey may fit.",
            "helps_items": [
                {"icon": "📱", "title": "Their specific approach", "desc": "Wizey may offer features or interface choices that suit your particular preferences and workflow."},
                {"icon": "🔄", "title": "Alternative perspective", "desc": "Getting a second interpretation from a different tool can provide additional context for your health data."},
                {"icon": "💭", "title": "Personal preference", "desc": "The right tool depends on your workflow, language needs, and what kind of output you find most useful."},
            ],
            "faqs": [
                {"q": "What is Wizey?", "a": "Wizey is a blood test analysis platform that helps users understand their lab results. For specific feature details, we recommend checking their website directly."},
                {"q": "How is NoryaAI different from Wizey?", "a": "NoryaAI offers structured health scores, doctor-ready PDFs with QR verification, multilingual reports in 9+ languages, and accepts lab reports from any laboratory worldwide — PDF, photo, or pasted text."},
                {"q": "Which one should I choose?", "a": "It depends on your needs. If you value structured reports, multilingual support, and doctor-ready PDFs from any lab format, NoryaAI is purpose-built for that. We recommend trying both and deciding based on your experience."},
                {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions."},
            ],
        },
    },
    "norya-vs-generic-ai": {
        "name": "Generic AI",
        "en": {
            "meta_title": "NoryaAI vs Generic AI Chatbots for Blood Test Results | NoryaAI",
            "meta_description": "Compare NoryaAI with generic AI chatbots for blood test results. See the difference between structured lab report analysis and free-form AI answers for blood test interpretation.",
            "hero_title": "NoryaAI vs Generic AI for Blood Test Results",
            "hero_sub": "Generic AI chatbots can discuss blood test questions, but they are not built as blood test analyzers. Here is a side-by-side comparison for people choosing between a structured lab-report workflow and open-ended AI chat.",
            "quick_answer_title": "The short version",
            "quick_answer": "Generic AI tools are better for broad medical Q&A. NoryaAI is better for blood test interpretation from real lab reports: it reads the report, maps every value to reference ranges, and produces a structured summary with flagged markers and a doctor-ready PDF instead of a one-off chat answer.",
            "cells": {
                "report_upload": "Copy-paste values into a chat prompt and hope the formatting holds",
                "reference_ranges": "May guess ranges or omit them; no guarantee they match your lab's standards",
                "units_formatting": "No built-in awareness of lab-specific units or result layouts",
                "output_structure": "Free-form paragraph that varies with each prompt — no consistent format",
                "multilingual": "Can translate text, but medical nuance may be lost in general translation",
                "doctor_summary": "No downloadable report — you would need to copy and format the chat yourself",
                "privacy": "Conversations may be stored and used for model training",
                "workflow": "General-purpose chat interface designed for any topic",
                "guided_flow": "Open-ended conversation — the quality depends on how you write your prompt",
            },
            "helps_title": "When generic AI chatbots can still help",
            "helps_sub": "This is not about one tool being bad and another being good. They serve different purposes.",
            "helps_items": [
                {"icon": "📚", "title": "General health education", "desc": "Chatbots are great for learning what a biomarker means, how the immune system works, or what a specific condition involves — broad educational questions."},
                {"icon": "💡", "title": "Brainstorming questions for your doctor", "desc": "Before an appointment, a chatbot can help you think through what to ask — even if it cannot read your actual lab report with precision."},
                {"icon": "🔍", "title": "Understanding medical terminology", "desc": "If you encounter an unfamiliar term in your report, a general AI can explain it quickly in plain language."},
            ],
            "faqs": [
                {"q": "Can ChatGPT explain blood test results?", "a": "Yes, to a degree. ChatGPT can explain what individual values mean in general terms. However, it does not parse your actual lab report, may hallucinate reference ranges, and produces a different answer each time you ask. NoryaAI is built to read your report directly and output a consistent, structured summary."},
                {"q": "Is NoryaAI a diagnosis tool?", "a": "No. NoryaAI provides structured, educational explanations of your lab values. It does not diagnose conditions or recommend treatments. Always consult a qualified doctor for medical decisions."},
                {"q": "Why is a structured report better than a chat answer?", "a": "A structured report gives you a health score, category breakdown, and flagged markers in a consistent format. You can compare it with previous tests, print it for your doctor, and see at a glance which values need attention — something a free-form chat paragraph cannot reliably offer."},
                {"q": "Can I upload a PDF instead of copying values manually?", "a": "Yes. NoryaAI accepts PDF uploads, photos of printed lab reports (JPG/PNG), and pasted text. It parses the values and reference ranges automatically — no manual data entry required."},
                {"q": "Is NoryaAI better for multilingual lab reports?", "a": "NoryaAI generates full reports in 9+ languages with preserved medical context. While general chatbots can translate text, they may lose nuance in medical terminology. NoryaAI's multilingual output is designed specifically for lab result interpretation."},
            ],
        },
    },
}


# ══════════════════════════════════════════════════════════════════
# TRANSLATIONS — Turkish
# ══════════════════════════════════════════════════════════════════
_UI["tr"] = {
    "home": "Ana Sayfa", "compare": "Karşılaştır", "how_it_works": "Nasıl çalışır",
    "pricing": "Fiyatlandırma", "blog": "Blog", "analyze": "Analiz Et",
    "faq_heading": "Sık Sorulan Sorular",
    "related_heading": "İlgili Karşılaştırmalar",
    "badge": "Dürüst karşılaştırma · NoryaAI",
    "comparison_title": "Yan yana karşılaştırma",
    "comparison_sub": "Kan tahlili sonuçlarına baktığınızda en önemli özellikler açısından iki yaklaşım arasındaki farklar.",
    "disclaimer": "NoryaAI tıbbi teşhis sağlamaz. Tüm içerikler yalnızca eğitim ve bilgilendirme amaçlıdır.",
    "privacy": "Gizlilik", "terms": "Kullanım şartları",
}
_LABELS["tr"] = {
    "report_upload": "Rapor yükleme", "reference_ranges": "Referans aralıkları",
    "units_formatting": "Birimler ve laboratuvar formatı", "output_structure": "Çıktı yapısı",
    "multilingual": "Çok dilli raporlar", "doctor_summary": "Doktora hazır özet",
    "privacy": "Gizlilik ve veri yönetimi", "workflow": "Kan tahlili odaklı iş akışı",
    "guided_flow": "İş akışı türü",
}
_NORYA["tr"] = {
    "report_upload": "PDF yükleyin, fotoğraf çekin veya metin yapıştırın — değerler ve aralıklar otomatik ayrıştırılır",
    "reference_ranges": "Her değer için referans aralıkları gösterilir — normal, düşük veya yüksek — net etiketlenmiş",
    "units_formatting": "Yaygın laboratuvar birimlerini, panel yapılarını ve sonuç formatlarını otomatik tanır",
    "output_structure": "Yapılandırılmış sağlık puanı, kategori dökümü ve işaretlenmiş belirteçler — her seferinde tutarlı",
    "multilingual": "9+ dilde tam raporlar, tıbbi bağlam korunarak",
    "doctor_summary": "QR doğrulamalı doktora hazır PDF — yazdırın, kaydedin veya paylaşın",
    "privacy": "GDPR/KVKK uyumlu — şifrelenmiş, satılmaz, eğitim için kullanılmaz",
    "workflow": "Laboratuvar sonuçları için özel olarak tasarlanmış yükleme, analiz ve rapor hattı",
    "guided_flow": "Yönlendirilmiş, yapılandırılmış analiz — bir kez yükleyin, eksiksiz rapor alın, istem gerekmez",
}
_WHY["tr"] = {
    "title": "İnsanlar kan tahlili için neden NoryaAI'ı tercih ediyor",
    "sub": "Doğruluk, yapı ve net bir sonraki adım genel bir sohbetten daha önemli olduğunda.",
    "items": [
        {"title": "Bir kez yükleyin, yapılandırılmış rapor alın", "desc": "İstem mühendisliği yok, yeniden biçimlendirme yok. Laboratuvar sonuçlarınızı yükleyin; sağlık puanı, kategori dökümü ve işaretlenmiş belirteçleri otomatik alın."},
        {"title": "Zaman içinde karşılaştırabileceğiniz tutarlı format", "desc": "Her rapor aynı yapıyı izler, böylece birden fazla kan tahlilindeki değişiklikleri takip edebilir ve eğilimleri bir bakışta görebilirsiniz."},
        {"title": "Gerçekten götürebileceğiniz doktora hazır PDF", "desc": "QR doğrulamalı temiz, profesyonel bir özet. Yazdırın veya dijital paylaşın — bir sonraki randevunuzda faydalı olması için tasarlandı."},
        {"title": "Sizin diliniz, sizin raporunuz", "desc": "9+ dil arasından seçin ve raporunuzu size en doğal gelen dilde alın — tıbbi bağlam bozulmadan."},
    ],
}
_CTA["tr"] = {
    "title": "Yapılandırılmış bir kan tahlili raporu denemek ister misiniz?",
    "sub": "Laboratuvar sonuçlarınızı yükleyin ve amaca yönelik bir analizörün farkını görün.",
    "primary": "Yükle ve analiz et",
    "secondary": "Fiyatları görüntüle",
    "hero_primary": "Kan tahlilimi analiz et",
    "hero_secondary": "Örnek rapor gör",
}
_HUB["tr"] = {
    "meta_title": "NoryaAI Karşılaştırma — Kan Tahlili Analiz Alternatifleri | NoryaAI",
    "meta_description": "NoryaAI'ı ChatGPT, BloodGPT, Kantesti, SiPhox Health, Wizey ve genel yapay zeka sohbet botlarıyla karşılaştırın. Dürüst, yan yana karşılaştırmalar.",
    "hero_title": "NoryaAI'ı Kan Tahlili Analiz Araçlarıyla Karşılaştırın",
    "hero_sub": "Kan tahlili sonuçlarınızı anlamak için doğru aracı mı arıyorsunuz? Popüler alternatiflerle dürüst, yan yana karşılaştırmalar hazırladık.",
    "trust_stats": [
        {"value": "%98,7", "label": "Sonuç doğruluğu", "sub": "Laboratuvar verileriyle doğrulanmış"},
        {"value": "9+", "label": "Dil desteği", "sub": "Tıbbi bağlam korunarak tam raporlar"},
        {"value": "QR", "label": "Doğrulanmış PDF", "sub": "Doktora hazır paylaşılabilir özet"},
    ],
    "cards": [
        {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Amaca yönelik bir kan tahlili analizörü ile dünyanın en popüler yapay zeka sohbet botunun karşılaştırması.", "link_text": "Tam karşılaştırmayı oku"},
        {"slug": "norya-vs-bloodgpt", "name": "BloodGPT", "summary": "Kan tahliline odaklı sohbet tabanlı bir yapay zeka deneyimini NoryaAI'ın yapılandırılmış raporları ve doktora hazır çıktılarıyla karşılaştırın.", "link_text": "Tam karşılaştırmayı oku"},
        {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "İki kan tahlili analiz platformu karşılaştırması — çok dilli yapılandırılmış raporlar ve Türkçe odaklı hizmet.", "link_text": "Tam karşılaştırmayı oku"},
        {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Evde biyobelirteç test kitleri ile mevcut laboratuvar sonuçlarınızın yapılandırılmış analizi — iki farklı yaklaşım.", "link_text": "Tam karşılaştırmayı oku"},
        {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "NoryaAI'ın yapılandırılmış rapor iş akışının Wizey'in kan tahlili analiz yaklaşımıyla karşılaştırması.", "link_text": "Tam karşılaştırmayı oku"},
        {"slug": "norya-vs-generic-ai", "name": "Genel Yapay Zeka", "summary": "Amaca yönelik bir kan tahlili analizörünün genel yapay zeka sohbet botlarına kıyasla sunduklarını keşfedin.", "link_text": "Tam karşılaştırmayı oku"},
    ],
    "hub_faqs": [
        {"q": "Kan tahlili sonuçlarını anlamak için en iyi araç hangisi?", "a": "İhtiyaçlarınıza bağlı. Sağlık puanları ve doktora hazır özetlerle yapılandırılmış, tutarlı raporlar istiyorsanız NoryaAI bunun için tasarlandı. Genel yapay zeka sohbet botları geniş sağlık eğitimi için daha uygundur."},
        {"q": "Bu karşılaştırmalar adil ve dürüst mü?", "a": "Şeffaflığı hedefliyoruz. Bir rakibin özellikleri net olarak açıklanmadığında, tahmin etmek yerine bunu belirtiyoruz. Farklı araçları denemenizi ve kendi deneyiminize göre karar vermenizi teşvik ediyoruz."},
        {"q": "NoryaAI'ı diğer araçlarla birlikte kullanabilir miyim?", "a": "Evet. NoryaAI sağlık iş akışınızı tamamlamak için tasarlanmıştır. Diğer platformlarla birlikte kullanabilirsiniz ve tıbbi kararlar için her zaman nitelikli bir doktora danışmalısınız."},
    ],
    "matrix_title": "Araçları yan yana karşılaştırın",
    "matrix_sub": "Her aracın kan tahlili analizine nasıl yaklaştığına hızlı bir genel bakış.",
    "matrix_row_labels": [
        "En iyi kullanım alanı",
        "Kan tahlili odaklı iş akışı",
        "Dosya yükleme akışı",
        "Referans aralığı farkındalığı",
        "Yapılandırılmış çıktı",
        "Çok dilli sonuç desteği",
        "Doktora hazır / paylaşılabilir özet",
        "Gizlilik / eğitici çerçeve",
        "Klinisyen ziyaretine hazırlık için uygunluk",
        "Sonuç doğruluğu",
    ],
    "matrix_columns": [
        {"key": "norya", "name": "NoryaAI", "slug": None},
        {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"},
        {"key": "bloodgpt", "name": "BloodGPT", "slug": "norya-vs-bloodgpt"},
        {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"},
        {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"},
        {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"},
        {"key": "generic", "name": "Genel YZ", "slug": "norya-vs-generic-ai"},
    ],
    "matrix_rows": [
        {"norya": "Yapılandırılmış kan tahlili analizi", "chatgpt": "Genel sağlık soru-cevap", "bloodgpt": "Kan tahlili odaklı sohbet", "kantesti": "Kan tahlili yorumlama", "siphox": "Evde biyobelirteç testi", "wizey": "Kan tahlili analizi", "generic": "Genel sağlık soru-cevap"},
        {"norya": "Güçlü", "chatgpt": "Sınırlı", "bloodgpt": "Mevcut", "kantesti": "Mevcut", "siphox": "Kısmi", "wizey": "Mevcut", "generic": "Sınırlı"},
        {"norya": "PDF, fotoğraf veya metin", "chatgpt": "İsteme kopyala-yapıştır", "bloodgpt": "Net olarak açıklanmamış", "kantesti": "Mevcut", "siphox": "Yalnızca kendi test kitleri", "wizey": "Net olarak açıklanmamış", "generic": "İsteme kopyala-yapıştır"},
        {"norya": "Güçlü", "chatgpt": "Sınırlı", "bloodgpt": "Kısmi", "kantesti": "Kısmi", "siphox": "Yalnızca kendi panelleri", "wizey": "Net olarak açıklanmamış", "generic": "Sınırlı"},
        {"norya": "Sağlık puanı + kategoriler", "chatgpt": "Serbest biçimli metin", "bloodgpt": "Sohbet tarzı yanıt", "kantesti": "Net olarak açıklanmamış", "siphox": "Panel görünümü", "wizey": "Net olarak açıklanmamış", "generic": "Serbest biçimli metin"},
        {"norya": "9+ dil", "chatgpt": "Kısmi", "bloodgpt": "Net olarak açıklanmamış", "kantesti": "Ağırlıklı Türkçe", "siphox": "Ağırlıklı İngilizce", "wizey": "Net olarak açıklanmamış", "generic": "Kısmi"},
        {"norya": "QR doğrulamalı PDF", "chatgpt": "Mevcut değil", "bloodgpt": "Net olarak açıklanmamış", "kantesti": "Net olarak açıklanmamış", "siphox": "Net olarak açıklanmamış", "wizey": "Net olarak açıklanmamış", "generic": "Mevcut değil"},
        {"norya": "GDPR/KVKK · yalnızca eğitici", "chatgpt": "Eğitim için saklanabilir", "bloodgpt": "Gizlilik politikasına bakınız", "kantesti": "Gizlilik politikasına bakınız", "siphox": "Gizlilik politikasına bakınız", "wizey": "Gizlilik politikasına bakınız", "generic": "Eğitim için saklanabilir"},
        {"norya": "Güçlü", "chatgpt": "Kısmi", "bloodgpt": "Kısmi", "kantesti": "Mevcut", "siphox": "Sınırlı", "wizey": "Net olarak açıklanmamış", "generic": "Kısmi"},
        {"norya": "%98,7 · laboratuvar doğrulamalı", "chatgpt": "Açıklanmamış", "bloodgpt": "Açıklanmamış", "kantesti": "Açıklanmamış", "siphox": "Açıklanmamış", "wizey": "Açıklanmamış", "generic": "Açıklanmamış"},
    ],
    "suits_title": "Hangi araç kime daha uygun?",
    "suits_items": [
        {"label": "Yapılandırılmış kan tahlili analizi", "text": "Mevcut laboratuvar sonuçlarınızdan tutarlı sağlık puanı, işaretlenmiş belirteçler ve doktora hazır PDF istiyorsanız NoryaAI bunun için özel olarak tasarlanmıştır.", "link_slug": None},
        {"label": "Genel sağlık soru-cevap", "text": "Açık uçlu sağlık soruları sormak, tıbbi terimler hakkında bilgi edinmek veya doktorunuz için sorular hazırlamak istiyorsanız ChatGPT gibi genel bir yapay zeka sohbet botu güçlü bir seçenektir.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
        {"label": "Laboratuvar raporu odaklı araçları karşılaştırma", "text": "Özellikle kan tahlili raporlarını analiz eden platformları değerlendiriyorsanız, hangi iş akışı, dil desteği ve çıktı formatının ihtiyaçlarınıza uyduğunu görmek için NoryaAI'ı Kantesti ve Wizey ile karşılaştırın.", "link_slug": "norya-vs-kantesti"},
    ],
}
_COMP["norya-vs-chatgpt-for-blood-tests"]["tr"] = {
    "meta_title": "NoryaAI vs ChatGPT — Kan Tahlili Karşılaştırması | NoryaAI",
    "meta_description": "NoryaAI ile ChatGPT'yi kan tahlili analizi için karşılaştırın. Yapılandırılmış rapor ile genel amaçlı sohbet botu — yan yana dürüst karşılaştırma.",
    "hero_title": "Kan Tahlili Analizi için NoryaAI vs ChatGPT",
    "hero_sub": "ChatGPT güçlü, genel amaçlı bir yapay zeka asistanıdır. NoryaAI ise kan tahlili analizi için özel olarak tasarlanmıştır. İşte her birinin en iyi yaptığına dürüst bir bakış.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "ChatGPT tıbbi terimleri açıklayabilir ve sohbet halinde sağlık sorularını yanıtlayabilir, ancak laboratuvar raporlarını ayrıştırmak için tasarlanmamıştır. NoryaAI kan tahlili sonuçlarınızı doğrudan okur, değerleri referans aralıklarıyla eşleştirir ve yapılandırılmış, doktora hazır bir özet üretir. Farklı sorunları çözerler.",
    "cells": {
        "report_upload": "Değerleri sohbet istemine kopyalayıp yapıştırmak gerekir; yerel laboratuvar raporu ayrıştırma hattı yoktur",
        "reference_ranges": "Genel aralıklar verebilir veya değerleri uydurabilir; laboratuvarınızla eşleşme garantisi yoktur",
        "units_formatting": "Laboratuvara özgü birimler veya bölgesel sonuç düzenleri konusunda yerleşik farkındalık yoktur",
        "output_structure": "Her seferinde değişen serbest biçimli metin — değişiklikleri takip etmek için tutarlı format yoktur",
        "multilingual": "İstek üzerine metin çevirebilir, ancak genel çeviride tıbbi nüans kaybolabilir",
        "doctor_summary": "İndirilebilir rapor yoktur — sohbeti kendiniz biçimlendirmeniz gerekir",
        "privacy": "Sohbetler OpenAI tarafından model eğitimi için saklanabilir ve kullanılabilir",
        "workflow": "Laboratuvar raporu analizi için tasarlanmamış genel amaçlı sohbet arayüzü",
        "guided_flow": "Açık uçlu sohbet — kalite isteminizi ne kadar iyi yazdığınıza bağlıdır",
    },
    "helps_title": "ChatGPT ne zaman yine de yardımcı olabilir",
    "helps_sub": "ChatGPT birçok görev için mükemmeldir. İşte gerçekten parladığı alanlar.",
    "helps_items": [
        {"icon": "📚", "title": "Genel sağlık eğitimi", "desc": "ChatGPT bir biyobelirtecin ne anlama geldiğini, bağışıklık sisteminin nasıl çalıştığını veya geniş tıbbi kavramları öğrenmek için harikadır."},
        {"icon": "💡", "title": "Doktor soruları hazırlama", "desc": "Tıbbi randevudan önce ChatGPT düşüncelerinizi düzenlemenize ve hekiminize sorular hazırlamanıza yardımcı olabilir."},
        {"icon": "🔍", "title": "Hızlı tıbbi terim arama", "desc": "Raporunuzda bilmediğiniz bir terimle karşılaşırsanız ChatGPT anında sade bir dilde açıklayabilir."},
    ],
    "faqs": [
        {"q": "ChatGPT kan tahlili sonuçlarımı analiz edebilir mi?", "a": "ChatGPT kan tahlili değerlerini yazarsanız tartışabilir, ancak laboratuvar raporlarını ayrıştırmaz, referans aralıklarını doğrulayamaz ve tıbbi detayları uydurabilir. NoryaAI laboratuvar raporlarını okumak ve tutarlı, yapılandırılmış analiz üretmek için özel olarak tasarlanmıştır."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önerisi yapmaz. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
        {"q": "Laboratuvar değerlerimi neden ChatGPT'ye sormayayım?", "a": "Sorabilirsiniz, ancak ChatGPT her seferinde farklı bir cevap verir, referans aralıklarını takip etmez ve yazdırılabilir rapor üretemez. NoryaAI her seferinde tutarlı sağlık puanı, işaretlenmiş belirteçler ve doktora hazır PDF üretir."},
        {"q": "ChatGPT'ye kan tahlili analizi için PDF yükleyebilir miyim?", "a": "ChatGPT Plus planı ile PDF okuyabilir, ancak laboratuvar raporu yapılarını ayrıştırmak için tasarlanmamıştır. NoryaAI değerleri, referans aralıklarını ve birimleri otomatik olarak çıkarmak için özel olarak tasarlanmıştır."},
        {"q": "ChatGPT ile NoryaAI arasında verilerim güvende mi?", "a": "OpenAI, devre dışı bırakmadığınız sürece sohbetleri model eğitimi için saklayabilir ve kullanabilir. NoryaAI GDPR/KVKK uyumludur — verileriniz şifrelenir, satılmaz ve eğitim için kullanılmaz."},
    ],
}
_COMP["norya-vs-bloodgpt"]["tr"] = {
    "meta_title": "NoryaAI vs BloodGPT — Kan Tahlili Karşılaştırması | NoryaAI",
    "meta_description": "NoryaAI ile BloodGPT'yi kan tahlili analizi için karşılaştırın. Yapılandırılmış raporlar, çok dilli çıktı ve doktora hazır PDF'ler ile sohbet odaklı iş akışı yan yana.",
    "hero_title": "Kan Tahlili Analizi için NoryaAI vs BloodGPT",
    "hero_sub": "BloodGPT kan tahlili odaklı bir yapay zeka sohbet deneyimi olarak konumlanır. NoryaAI ise yapılandırılmış raporlar, referans aralığı farkındalığı ve doktora hazır çıktılar etrafında inşa edilmiştir. İşte iki yaklaşımın farkı.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "BloodGPT kan tahlili sonuçlarını sohbet içinde tartışmaya odaklanan bir yaklaşımdır. NoryaAI ise yapılandırılmış yükleme ve raporlama iş akışıdır: laboratuvar raporunuzu okur, her belirteci referans aralıklarıyla eşleştirir ve sağlık puanı ile doktora hazır PDF içeren çok dilli bir özet döndürür. Biri sohbet odaklıdır, diğeri tekrar kullanılabilir raporlama için tasarlanmıştır.",
    "cells": {
        "report_upload": "Sohbet öncelikli iş akışı; yerel rapor yükleme desteği net olarak açıklanmamıştır",
        "reference_ranges": "Sohbet içinde aralıkları tartışabilir, ancak laboratuvara özel eşleştirme ve yapı net olarak açıklanmamıştır",
        "units_formatting": "Değerleri sohbette yorumlayabilir, ancak farklı laboratuvar düzenleri ve birim formatları desteği net olarak açıklanmamıştır",
        "output_structure": "Sabit rapor yapısından çok sohbet tarzı yanıtlar",
        "multilingual": "Dil kapsamı net olarak açıklanmamıştır",
        "doctor_summary": "Doktora hazır PDF veya doğrulanmış dışa aktarma formatı net olarak açıklanmamıştır",
        "privacy": "Saklama, tutma süresi ve model kullanımı ayrıntıları için gizlilik politikasına bakın",
        "workflow": "Kan tahlili odaklı yapay zeka sohbet deneyimi",
        "guided_flow": "Kan tahlili sonuçları hakkında soru-cevap odaklı sohbet",
    },
    "helps_title": "BloodGPT ne zaman yine de yardımcı olabilir",
    "helps_sub": "Sohbet odaklı bir kan tahlili aracı, sabit rapor yerine karşılıklı soru-cevap tercih eden kullanıcılara uygun olabilir.",
    "helps_items": [
        {"icon": "💬", "title": "Sohbet öncelikli deneyim", "desc": "Takip sorularını sohbet arayüzünde sormayı tercih ediyorsanız, kan tahlili odaklı bir chatbot sabit rapordan daha doğal gelebilir."},
        {"icon": "🧪", "title": "Kan tahliline odaklı istemler", "desc": "Odaklı bir chatbot, biyobelirteçleri sohbet içinde tartışmak istediğinizde genel amaçlı yapay zekaya göre daha dar bağlam sunabilir."},
        {"icon": "⚡", "title": "Hızlı keşif amaçlı cevaplar", "desc": "Belirteçler hakkında hızlı ileri-geri düşünme için, resmi bir özet istemeden önce konuşma tabanlı arayüz faydalı olabilir."},
    ],
    "faqs": [
        {"q": "BloodGPT ile NoryaAI arasındaki temel fark nedir?", "a": "BloodGPT daha çok sohbet tarzı kan tahlili yorumlamasına odaklanıyor gibi görünür. NoryaAI ise referans aralığı farkındalığı, sağlık puanları, çok dilli çıktı ve doktora hazır PDF'lerle yapılandırılmış kan tahlili raporlarına odaklanır."},
        {"q": "Kan tahlili incelemesi için sohbet arayüzü yeterli mi?", "a": "Hedefinize bağlıdır. Sohbet tartışma için faydalı olabilir; ancak zaman içinde karşılaştırabileceğiniz, yeniden açabileceğiniz veya klinisyenle paylaşabileceğiniz tutarlı bir format istiyorsanız yapılandırılmış rapor genellikle daha pratiktir."},
        {"q": "NoryaAI tıbbi teşhis koyar mı?", "a": "Hayır. NoryaAI laboratuvar değerlerinin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz ve tedavi önermez. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
    ],
}
_COMP["norya-vs-kantesti"]["tr"] = {
    "meta_title": "NoryaAI vs Kantesti — Kan Tahlili Karşılaştırması | NoryaAI",
    "meta_description": "NoryaAI ile Kantesti'yi kan tahlili analizi için karşılaştırın. İki platformun özellikleri — yükleme iş akışı, rapor yapısı ve çok dilli destek.",
    "hero_title": "Kan Tahlili Analizi için NoryaAI vs Kantesti",
    "hero_sub": "Hem NoryaAI hem de Kantesti kullanıcıların kan tahlili sonuçlarını anlamasına yardımcı olur. İşte her platformun sunduklarının dürüst bir karşılaştırması.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "Kantesti ağırlıklı olarak Türkçe konuşan kullanıcılara hizmet veren bir kan tahlili analiz hizmetidir. NoryaAI sağlık puanları, doktora hazır PDF'ler ve 9+ dil desteğiyle yapılandırılmış, çok dilli bir kan tahlili analiz iş akışı sunar. Her ikisi de laboratuvar sonuçlarını anlamayı kolaylaştırmayı amaçlar.",
    "cells": {
        "report_upload": "Analiz için laboratuvar sonucu girişini destekler",
        "reference_ranges": "Analiz edilen değerler için referans aralığı bilgisi sağlar",
        "units_formatting": "Türk laboratuvar rapor formatlarını işler",
        "output_structure": "Analiz sonuçlarını kendi formatında sunar",
        "multilingual": "Ağırlıklı olarak Türkçe'de mevcuttur",
        "doctor_summary": "Rapor formatı ve paylaşım seçenekleri net olarak açıklanmamıştır",
        "privacy": "Veri işleme politikaları platformlarında mevcuttur",
        "workflow": "Kan tahlili sonucu yorumlamaya odaklıdır",
        "guided_flow": "Kendi analiz iş akışını sunar",
    },
    "helps_title": "Kantesti ne zaman daha uygun olabilir",
    "helps_sub": "Farklı araçlar farklı kişiler için daha iyi çalışır. İşte Kantesti'nin uygun olabileceği durumlar.",
    "helps_items": [
        {"icon": "🇹🇷", "title": "Türkçe öncelikli deneyim", "desc": "Öncelikle Türkçe konuşan kullanıcılar için tasarlanmış bir platform istiyorsanız Kantesti yerel Türkçe arayüz sunar."},
        {"icon": "🏥", "title": "Yerel laboratuvar aşinalığı", "desc": "Kantesti belirli Türk laboratuvar formatları ve geleneklerine aşina olabilir."},
        {"icon": "📋", "title": "Basit analiz", "desc": "Çok dilli ihtiyaç olmadan doğrudan kan tahlili yorumlama için Kantesti iyi hizmet verebilir."},
    ],
    "faqs": [
        {"q": "Kantesti nedir?", "a": "Kantesti, kullanıcıların laboratuvar sonuçlarını anlamalarına yardımcı olan bir kan tahlili analiz platformudur. Ağırlıklı olarak Türkçe konuşan kullanıcılara hizmet verir."},
        {"q": "NoryaAI Kantesti'den nasıl farklıdır?", "a": "NoryaAI yapılandırılmış sağlık puanları, QR doğrulamalı doktora hazır PDF'ler, 9+ dilde çok dilli raporlar sunar ve dünya çapında birden fazla laboratuvar rapor formatını destekler. Hangi platformun daha uygun olduğunu ihtiyaçlarınız belirler."},
        {"q": "NoryaAI Türkçe'de mevcut mu?", "a": "Evet. NoryaAI, Türkçe dahil 9+ dilde tam kan tahlili analizi ve raporlar sunar."},
        {"q": "NoryaAI Türk laboratuvar raporlarıyla çalışır mı?", "a": "Evet. NoryaAI Türk laboratuvar rapor formatlarını, birimlerini ve panel yapılarını tanır ve Türkçe veya desteklenen herhangi bir dilde rapor üretebilir."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önerisi yapmaz. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
    ],
}
_COMP["norya-vs-siphox-health"]["tr"] = {
    "meta_title": "NoryaAI vs SiPhox Health — Kan Tahlili Karşılaştırması | NoryaAI",
    "meta_description": "NoryaAI ile SiPhox Health'i karşılaştırın: evde test kitleri ve yapılandırılmış laboratuvar raporu analizi. Kan tahlili sonuçlarınızı anlamak için iki farklı yaklaşım.",
    "hero_title": "NoryaAI vs SiPhox Health",
    "hero_sub": "SiPhox Health evde biyobelirteç test kitleri sunar. NoryaAI mevcut laboratuvar sonuçlarınızı analiz eder ve yapılandırılmış, uygulanabilir raporlara dönüştürür. İşte nasıl karşılaştırıldıkları.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "SiPhox Health ve NoryaAI sağlık testinin farklı aşamalarına hizmet eder. SiPhox biyobelirteç örnekleri toplamak için evde test kitleri sağlarken, NoryaAI zaten sahip olduğunuz laboratuvar sonuçlarını analiz eder — herhangi bir laboratuvardan, herhangi bir formatta — ve yapılandırılmış bir sağlık raporu üretir. Birbirlerini tamamlayabilirler.",
    "cells": {
        "report_upload": "Kendi evde test kitlerinden sonuçlar sağlar — harici laboratuvar raporları için tasarlanmamıştır",
        "reference_ranges": "Kendi biyobelirteç panelleri için aralıklar gösterir",
        "units_formatting": "Kendi test kiti formatına göre standartlaştırılmıştır",
        "output_structure": "Platformları içinde gösterge paneli ve sonuçlar",
        "multilingual": "Ağırlıklı olarak İngilizce'de mevcuttur",
        "doctor_summary": "Sonuçlar platformlarında görüntülenebilir; dışa aktarma seçenekleri net olarak açıklanmamıştır",
        "privacy": "Veri işleme politikaları web sitelerinde mevcuttur",
        "workflow": "Uçtan uca test: kit siparişi, örnek toplama, sonuç alma",
        "guided_flow": "Tescilli kitlerine bağlı yönlendirilmiş evde test iş akışı",
    },
    "helps_title": "SiPhox Health ne zaman daha uygun olabilir",
    "helps_sub": "SiPhox Health ve NoryaAI farklı ihtiyaçlara hizmet eder. İşte SiPhox'un parladığı alanlar.",
    "helps_items": [
        {"icon": "🏠", "title": "Evde kolaylık", "desc": "Laboratuvara gitmeden test yapmak istiyorsanız SiPhox Health kapınıza kit gönderir."},
        {"icon": "📊", "title": "Düzenli izleme", "desc": "SiPhox zaman içinde düzenli biyobelirteç takibi için abonelik tabanlı test sunar."},
        {"icon": "🔬", "title": "Seçilmiş paneller", "desc": "Test panelleri uzun ömür veya metabolik sağlık gibi belirli sağlık hedefleri etrafında tasarlanmıştır."},
    ],
    "faqs": [
        {"q": "SiPhox Health nedir?", "a": "SiPhox Health evde biyobelirteç test kitleri sunar. Bir kit sipariş eder, evde örnek toplarsınız ve sonuçları platformları aracılığıyla alırsınız."},
        {"q": "NoryaAI SiPhox Health sonuçlarını analiz edebilir mi?", "a": "SiPhox veya başka bir sağlayıcıdan laboratuvar sonuçları alırsanız, sağlık puanları ve doktora hazır PDF ile yapılandırılmış analiz için NoryaAI'a yükleyebilirsiniz."},
        {"q": "NoryaAI kullanmak için test kitine ihtiyacım var mı?", "a": "Hayır. NoryaAI zaten sahip olduğunuz laboratuvar sonuçlarıyla çalışır — herhangi bir laboratuvardan, herhangi bir ülkeden. PDF, fotoğraf yükleyin veya metin yapıştırın ve yapılandırılmış rapor alın."},
        {"q": "Hem SiPhox Health hem de NoryaAI kullanabilir miyim?", "a": "Evet. Örneklerinizi toplamak için SiPhox'u kullanabilir, ardından sağlık puanları ve paylaşılabilir PDF ile ek yapılandırılmış analiz için sonuçları NoryaAI'a yükleyebilirsiniz."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önerisi yapmaz. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
    ],
}
_COMP["norya-vs-wizey"]["tr"] = {
    "meta_title": "NoryaAI vs Wizey — Kan Tahlili Karşılaştırması | NoryaAI",
    "meta_description": "NoryaAI ile Wizey'i kan tahlili analizi için karşılaştırın. Yapılandırılmış rapor özellikleri, çok dilli destek ve iş akışı — yan yana karşılaştırma.",
    "hero_title": "Kan Tahlili Analizi için NoryaAI vs Wizey",
    "hero_sub": "Hem NoryaAI hem de Wizey kullanıcıların kan tahlili sonuçlarını anlamasına yardımcı olur. İşte her platformun sunduklarının dürüst, yan yana karşılaştırması.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "Wizey sağlık bilgileri için kan tahlili analiz araçları sunar. NoryaAI herhangi bir laboratuvar formatından sağlık puanları, doktora hazır PDF'ler ve çok dilli raporlar üreten yapılandırılmış, yükleme tabanlı bir iş akışı sunar. Aynı hedefe farklı yaklaşımlar.",
    "cells": {
        "report_upload": "Analiz için laboratuvar sonuçlarını kabul eder",
        "reference_ranges": "Referans aralığı bilgisi sağlar",
        "units_formatting": "Laboratuvar format desteği net olarak açıklanmamıştır",
        "output_structure": "Analizi kendi formatında sunar",
        "multilingual": "Dil desteği net olarak açıklanmamıştır",
        "doctor_summary": "Rapor paylaşım seçenekleri net olarak açıklanmamıştır",
        "privacy": "Veri işleme politikaları platformlarında mevcuttur",
        "workflow": "Kan tahlili yorumlama iş akışı sunar",
        "guided_flow": "Kendi analiz sürecini sağlar",
    },
    "helps_title": "Wizey ne zaman yine de yardımcı olabilir",
    "helps_sub": "Farklı araçlar farklı tercihlere uygundur. İşte Wizey'in uygun olabileceği durumlar.",
    "helps_items": [
        {"icon": "📱", "title": "Kendine özgü yaklaşımı", "desc": "Wizey, belirli tercihlerinize ve iş akışınıza uygun platform özellikleri sunabilir."},
        {"icon": "🔄", "title": "Alternatif bakış açısı", "desc": "Farklı bir araçtan ikinci bir yorum almak, sağlık verileriniz için ek bağlam sağlayabilir."},
        {"icon": "💭", "title": "Kişisel tercih", "desc": "Doğru araç iş akışınıza, dil ihtiyaçlarınıza ve en faydalı bulduğunuz çıktı türüne bağlıdır."},
    ],
    "faqs": [
        {"q": "Wizey nedir?", "a": "Wizey, kullanıcıların laboratuvar sonuçlarını anlamalarına yardımcı olan bir kan tahlili analiz platformudur. Belirli özellik detayları için doğrudan web sitelerini kontrol etmenizi öneririz."},
        {"q": "NoryaAI Wizey'den nasıl farklıdır?", "a": "NoryaAI yapılandırılmış sağlık puanları, QR doğrulamalı doktora hazır PDF'ler, 9+ dilde çok dilli raporlar sunar ve dünya çapında herhangi bir laboratuvardan laboratuvar raporlarını kabul eder — PDF, fotoğraf veya yapıştırılmış metin."},
        {"q": "Hangisini seçmeliyim?", "a": "İhtiyaçlarınıza bağlı. Yapılandırılmış raporlar, çok dilli destek ve herhangi bir laboratuvar formatından doktora hazır PDF'ler değerliyse NoryaAI bunun için özel olarak tasarlanmıştır. Her ikisini de denemenizi ve deneyiminize göre karar vermenizi öneririz."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önerisi yapmaz. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
    ],
}
_COMP["norya-vs-generic-ai"]["tr"] = {
    "meta_title": "NoryaAI vs Genel Yapay Zeka — Kan Tahlili Karşılaştırması | NoryaAI",
    "meta_description": "NoryaAI ile ChatGPT veya diğer yapay zeka sohbet botlarını kan tahlili sonuçları için karşılaştırın. Yapılandırılmış raporlar ile serbest biçimli sohbet cevapları — yan yana karşılaştırma.",
    "hero_title": "Kan Tahlilleri için NoryaAI vs Genel Yapay Zeka Sohbet Botları",
    "hero_sub": "Her ikisi de laboratuvar verileriyle çalışabilir — ancak çok farklı yaklaşırlar. İşte kan tahlili sonuçlarınızı anlamanız gerektiğinde her birinin sunduklarına dürüst, yan yana bir bakış.",
    "quick_answer_title": "Kısa özet",
    "quick_answer": "ChatGPT gibi genel yapay zeka sohbet botları tıbbi terimleri açıklayabilir ve sohbet halinde sağlık sorularını yanıtlayabilir. NoryaAI kan tahlilleri için özel olarak tasarlanmıştır: laboratuvar raporunuzu okur, her değeri referans aralıklarıyla eşleştirir ve sağlık puanlı, yapılandırılmış, doktora hazır bir özet üretir — serbest biçimli bir paragraf değil. Her ikisinin de yeri var, ancak farklı sorunları çözerler.",
    "cells": {
        "report_upload": "Değerleri sohbet istemine kopyalayıp yapıştırın ve biçimlendirmenin tutmasını umun",
        "reference_ranges": "Aralıkları tahmin edebilir veya atlayabilir; laboratuvarınızın standartlarıyla eşleşme garantisi yoktur",
        "units_formatting": "Laboratuvara özgü birimler veya sonuç düzenleri konusunda yerleşik farkındalık yoktur",
        "output_structure": "Her istemde değişen serbest biçimli paragraf — tutarlı format yoktur",
        "multilingual": "Metin çevirebilir, ancak genel çeviride tıbbi nüans kaybolabilir",
        "doctor_summary": "İndirilebilir rapor yok — sohbeti kendiniz kopyalayıp biçimlendirmeniz gerekir",
        "privacy": "Sohbetler model eğitimi için saklanabilir ve kullanılabilir",
        "workflow": "Herhangi bir konu için tasarlanmış genel amaçlı sohbet arayüzü",
        "guided_flow": "Açık uçlu sohbet — kalite isteminizi nasıl yazdığınıza bağlıdır",
    },
    "helps_title": "Genel yapay zeka sohbet botları ne zaman yine de yardımcı olabilir",
    "helps_sub": "Bu bir aracın kötü, diğerinin iyi olmasıyla ilgili değil. Farklı amaçlara hizmet ederler.",
    "helps_items": [
        {"icon": "📚", "title": "Genel sağlık eğitimi", "desc": "Sohbet botları bir biyobelirtecin ne anlama geldiğini, bağışıklık sisteminin nasıl çalıştığını veya belirli bir durumun ne içerdiğini öğrenmek için harikadır — geniş eğitici sorular."},
        {"icon": "💡", "title": "Doktorunuza sorular hazırlama", "desc": "Randevudan önce bir sohbet botu ne soracağınızı düşünmenize yardımcı olabilir — gerçek laboratuvar raporunuzu hassasiyetle okuyamasa bile."},
        {"icon": "🔍", "title": "Tıbbi terminolojiyi anlama", "desc": "Raporunuzda bilmediğiniz bir terimle karşılaşırsanız genel bir yapay zeka sade bir dille hızla açıklayabilir."},
    ],
    "faqs": [
        {"q": "ChatGPT kan tahlili sonuçlarını açıklayabilir mi?", "a": "Evet, bir dereceye kadar. ChatGPT bireysel değerlerin genel olarak ne anlama geldiğini açıklayabilir. Ancak gerçek laboratuvar raporunuzu ayrıştırmaz, referans aralıklarını uydurabilir ve her sorduğunuzda farklı cevap verir. NoryaAI raporunuzu doğrudan okumak ve tutarlı, yapılandırılmış bir özet çıkarmak için tasarlanmıştır."},
        {"q": "NoryaAI bir teşhis aracı mıdır?", "a": "Hayır. NoryaAI laboratuvar değerlerinizin yapılandırılmış, eğitici açıklamalarını sunar. Hastalık teşhisi koymaz veya tedavi önerisi yapmaz. Tıbbi kararlar için her zaman nitelikli bir doktora danışın."},
        {"q": "Yapılandırılmış rapor sohbet cevabından neden daha iyidir?", "a": "Yapılandırılmış rapor tutarlı formatta sağlık puanı, kategori dökümü ve işaretlenmiş belirteçler verir. Önceki testlerle karşılaştırabilir, doktorunuz için yazdırabilir ve hangi değerlerin dikkat gerektirdiğini bir bakışta görebilirsiniz — serbest biçimli bir sohbet paragrafının güvenilir şekilde sunamayacağı bir şey."},
        {"q": "Değerleri elle kopyalamak yerine PDF yükleyebilir miyim?", "a": "Evet. NoryaAI PDF yüklemelerini, basılı laboratuvar raporlarının fotoğraflarını (JPG/PNG) ve yapıştırılmış metni kabul eder. Değerleri ve referans aralıklarını otomatik ayrıştırır — elle veri girişi gerekmez."},
        {"q": "NoryaAI çok dilli laboratuvar raporları için daha mı iyidir?", "a": "NoryaAI 9+ dilde korunmuş tıbbi bağlamla tam raporlar üretir. Genel sohbet botları metni çevirebilirken tıbbi terminolojide nüans kaybedebilirler. NoryaAI'ın çok dilli çıktısı özellikle laboratuvar sonucu yorumlama için tasarlanmıştır."},
    ],
}


# ══════════════════════════════════════════════════════════════════
# TRANSLATIONS — German
# ══════════════════════════════════════════════════════════════════
_UI["de"] = {
    "home": "Startseite", "compare": "Vergleich", "how_it_works": "So funktioniert's",
    "pricing": "Preise", "blog": "Blog", "analyze": "Analysieren",
    "faq_heading": "Häufig gestellte Fragen",
    "related_heading": "Weitere Vergleiche",
    "badge": "Ehrlicher Vergleich · NoryaAI",
    "comparison_title": "Vergleich Seite an Seite",
    "comparison_sub": "Wie sich die beiden Ansätze bei den wichtigsten Funktionen für Bluttestergebnisse unterscheiden.",
    "disclaimer": "NoryaAI stellt keine medizinischen Diagnosen. Alle Inhalte dienen ausschließlich Bildungs- und Informationszwecken.",
    "privacy": "Datenschutz", "terms": "Nutzungsbedingungen",
}
_LABELS["de"] = {
    "report_upload": "Bericht-Upload", "reference_ranges": "Referenzbereiche",
    "units_formatting": "Einheiten und Laborformat", "output_structure": "Ausgabestruktur",
    "multilingual": "Mehrsprachige Berichte", "doctor_summary": "Arztfertiger Bericht",
    "privacy": "Datenschutz und Datenverarbeitung", "workflow": "Bluttest-spezifischer Workflow",
    "guided_flow": "Workflow-Typ",
}
_NORYA["de"] = {
    "report_upload": "PDF hochladen, Foto machen oder Text einfügen — Werte und Bereiche werden automatisch erkannt",
    "reference_ranges": "Referenzbereiche für jeden Wert angezeigt — normal, niedrig oder hoch — klar gekennzeichnet",
    "units_formatting": "Erkennt gängige Laboreinheiten, Panelstrukturen und Ergebnisformate automatisch",
    "output_structure": "Strukturierter Gesundheitsscore, Kategorieaufschlüsselung und markierte Marker — jedes Mal konsistent",
    "multilingual": "Vollständige Berichte in 9+ Sprachen mit bewahrtem medizinischem Kontext",
    "doctor_summary": "Arztfertiges PDF mit QR-Verifizierung — ausdrucken, speichern oder teilen",
    "privacy": "DSGVO/KVKK-konform — verschlüsselt, nie verkauft, nie für Training verwendet",
    "workflow": "Speziell für Laborergebnisse entwickelte Upload-, Analyse- und Berichtspipeline",
    "guided_flow": "Geführte, strukturierte Analyse — einmal hochladen und vollständigen Bericht erhalten, keine Eingabeaufforderung nötig",
}
_WHY["de"] = {
    "title": "Warum Menschen NoryaAI für Bluttests wählen",
    "sub": "Wenn Genauigkeit, Struktur und ein klarer nächster Schritt wichtiger sind als ein allgemeines Gespräch.",
    "items": [
        {"title": "Einmal hochladen, strukturierten Bericht erhalten", "desc": "Kein Prompt-Engineering, keine Neuformatierung. Laden Sie Ihre Laborergebnisse hoch und erhalten Sie automatisch einen Gesundheitsscore, Kategorieaufschlüsselung und markierte Marker."},
        {"title": "Konsistentes Format zum Vergleichen über die Zeit", "desc": "Jeder Bericht folgt der gleichen Struktur, sodass Sie Veränderungen über mehrere Bluttests verfolgen und Trends auf einen Blick erkennen können."},
        {"title": "Arztfertiges PDF, das Sie tatsächlich mitnehmen können", "desc": "Eine saubere, professionelle Zusammenfassung mit QR-Verifizierung. Drucken oder digital teilen — für Ihren nächsten Termin konzipiert."},
        {"title": "Ihre Sprache, Ihr Bericht", "desc": "Wählen Sie aus 9+ Sprachen und erhalten Sie Ihren Bericht in der Sprache, die sich am natürlichsten anfühlt — mit intaktem medizinischem Kontext."},
    ],
}
_CTA["de"] = {
    "title": "Bereit für einen strukturierten Bluttest-Bericht?",
    "sub": "Laden Sie Ihre Laborergebnisse hoch und erleben Sie den Unterschied eines spezialisierten Analysators.",
    "primary": "Hochladen und analysieren",
    "secondary": "Preise ansehen",
    "hero_primary": "Meinen Bluttest analysieren",
    "hero_secondary": "Beispielbericht ansehen",
}
_HUB["de"] = {
    "meta_title": "NoryaAI Vergleich — Bluttest-Analyse-Alternativen | NoryaAI",
    "meta_description": "Vergleichen Sie NoryaAI mit ChatGPT, BloodGPT, Kantesti, SiPhox Health, Wizey und allgemeinen KI-Chatbots für die Bluttestanalyse. Ehrliche Vergleiche.",
    "hero_title": "NoryaAI mit Bluttest-Analyse-Tools vergleichen",
    "hero_sub": "Suchen Sie das richtige Tool zum Verstehen Ihrer Bluttestergebnisse? Wir haben ehrliche Vergleiche mit mehreren beliebten Alternativen vorbereitet.",
    "trust_stats": [
        {"value": "98,7%", "label": "Ergebnisgenauigkeit", "sub": "Mit Labordaten verifiziert"},
        {"value": "9+", "label": "Sprachen", "sub": "Vollständige Berichte mit medizinischem Kontext"},
        {"value": "QR", "label": "Verifiziertes PDF", "sub": "Arztfertiger teilbarer Bericht"},
    ],
    "cards": [
        {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Wie ein spezialisierter Bluttest-Analysator im Vergleich zum weltweit beliebtesten KI-Chatbot abschneidet.", "link_text": "Vollständigen Vergleich lesen"},
        {"slug": "norya-vs-bloodgpt", "name": "BloodGPT", "summary": "Ein bluttestfokussierter KI-Chat-Workflow im Vergleich zu NoryaAIs strukturierten Berichten und arztfertigen Zusammenfassungen.", "link_text": "Vollständigen Vergleich lesen"},
        {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Zwei Bluttest-Analyseplattformen im Vergleich — mehrsprachige strukturierte Berichte vs. ein türkischsprachiger Dienst.", "link_text": "Vollständigen Vergleich lesen"},
        {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Heim-Biomarker-Testkits vs. strukturierte Analyse Ihrer vorhandenen Laborergebnisse — zwei verschiedene Ansätze.", "link_text": "Vollständigen Vergleich lesen"},
        {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "NoryaAIs strukturierter Berichts-Workflow im Vergleich zu Wizeys Ansatz zur Bluttestanalyse.", "link_text": "Vollständigen Vergleich lesen"},
        {"slug": "norya-vs-generic-ai", "name": "Allgemeine KI", "summary": "Was ein spezialisierter Bluttest-Analysator im Vergleich zu allgemeinen KI-Chatbots bietet.", "link_text": "Vollständigen Vergleich lesen"},
    ],
    "hub_faqs": [
        {"q": "Welches Tool ist am besten zum Verstehen von Bluttestergebnissen?", "a": "Es hängt von Ihren Bedürfnissen ab. Für strukturierte, konsistente Berichte mit Gesundheitsscores und arztfertigen Zusammenfassungen ist NoryaAI speziell entwickelt. Allgemeine KI-Chatbots eignen sich besser für allgemeine Gesundheitsbildung."},
        {"q": "Sind diese Vergleiche fair und ehrlich?", "a": "Wir streben Transparenz an. Wo die Funktionen eines Mitbewerbers nicht klar offengelegt sind, sagen wir das, anstatt zu raten. Wir ermutigen Sie, verschiedene Tools auszuprobieren und aufgrund Ihrer eigenen Erfahrung zu entscheiden."},
        {"q": "Kann ich NoryaAI zusammen mit anderen Tools nutzen?", "a": "Ja. NoryaAI ergänzt Ihren Gesundheits-Workflow. Sie können es neben anderen Plattformen nutzen und sollten für medizinische Entscheidungen immer einen qualifizierten Arzt konsultieren."},
    ],
    "matrix_title": "Tools im direkten Vergleich",
    "matrix_sub": "Ein schneller Überblick, wie jedes Tool die Bluttestanalyse angeht.",
    "matrix_row_labels": [
        "Bester Anwendungsfall",
        "Bluttest-spezifischer Workflow",
        "Datei-Upload-Ablauf",
        "Referenzbereich-Erkennung",
        "Strukturierte Ausgabe",
        "Mehrsprachige Ergebnisunterstützung",
        "Arztfertiger / teilbarer Bericht",
        "Datenschutz / Bildungsrahmen",
        "Geeignet zur Vorbereitung auf einen Arztbesuch",
        "Ergebnisgenauigkeit",
    ],
    "matrix_columns": [
        {"key": "norya", "name": "NoryaAI", "slug": None},
        {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"},
        {"key": "bloodgpt", "name": "BloodGPT", "slug": "norya-vs-bloodgpt"},
        {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"},
        {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"},
        {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"},
        {"key": "generic", "name": "Allgemeine KI", "slug": "norya-vs-generic-ai"},
    ],
    "matrix_rows": [
        {"norya": "Strukturierte Bluttestanalyse", "chatgpt": "Allgemeine Gesundheitsfragen", "bloodgpt": "Bluttestfokussierter Chat", "kantesti": "Bluttest-Interpretation", "siphox": "Heim-Biomarker-Tests", "wizey": "Bluttestanalyse", "generic": "Allgemeine Gesundheitsfragen"},
        {"norya": "Stark", "chatgpt": "Begrenzt", "bloodgpt": "Verfügbar", "kantesti": "Verfügbar", "siphox": "Teilweise", "wizey": "Verfügbar", "generic": "Begrenzt"},
        {"norya": "PDF, Foto oder Text", "chatgpt": "Kopieren-Einfügen", "bloodgpt": "Nicht klar offengelegt", "kantesti": "Verfügbar", "siphox": "Nur eigene Testkits", "wizey": "Nicht klar offengelegt", "generic": "Kopieren-Einfügen"},
        {"norya": "Stark", "chatgpt": "Begrenzt", "bloodgpt": "Teilweise", "kantesti": "Teilweise", "siphox": "Nur eigene Panels", "wizey": "Nicht klar offengelegt", "generic": "Begrenzt"},
        {"norya": "Gesundheitsscore + Kategorien", "chatgpt": "Freitext", "bloodgpt": "Chat-Antwort", "kantesti": "Nicht klar offengelegt", "siphox": "Dashboard-Ansicht", "wizey": "Nicht klar offengelegt", "generic": "Freitext"},
        {"norya": "9+ Sprachen", "chatgpt": "Teilweise", "bloodgpt": "Nicht klar offengelegt", "kantesti": "Hauptsächlich Türkisch", "siphox": "Hauptsächlich Englisch", "wizey": "Nicht klar offengelegt", "generic": "Teilweise"},
        {"norya": "PDF mit QR-Verifizierung", "chatgpt": "Nicht verfügbar", "bloodgpt": "Nicht klar offengelegt", "kantesti": "Nicht klar offengelegt", "siphox": "Nicht klar offengelegt", "wizey": "Nicht klar offengelegt", "generic": "Nicht verfügbar"},
        {"norya": "DSGVO · nur bildungsbezogen", "chatgpt": "Kann für Training gespeichert werden", "bloodgpt": "Siehe Datenschutzrichtlinie", "kantesti": "Siehe Datenschutzrichtlinie", "siphox": "Siehe Datenschutzrichtlinie", "wizey": "Siehe Datenschutzrichtlinie", "generic": "Kann für Training gespeichert werden"},
        {"norya": "Stark", "chatgpt": "Teilweise", "bloodgpt": "Teilweise", "kantesti": "Verfügbar", "siphox": "Begrenzt", "wizey": "Nicht klar offengelegt", "generic": "Teilweise"},
        {"norya": "98,7% · laborverifiziert", "chatgpt": "Nicht offengelegt", "bloodgpt": "Nicht offengelegt", "kantesti": "Nicht offengelegt", "siphox": "Nicht offengelegt", "wizey": "Nicht offengelegt", "generic": "Nicht offengelegt"},
    ],
    "suits_title": "Welches Tool passt zu wem?",
    "suits_items": [
        {"label": "Strukturierte Bluttestanalyse", "text": "Wenn Sie aus Ihren vorhandenen Laborergebnissen einen konsistenten Gesundheitsscore, markierte Marker und ein arztfertiges PDF möchten, ist NoryaAI dafür speziell entwickelt.", "link_slug": None},
        {"label": "Allgemeine Gesundheitsfragen", "text": "Wenn Sie offene Gesundheitsfragen stellen, medizinische Begriffe lernen oder Fragen für Ihren Arzt vorbereiten möchten, ist ein allgemeiner KI-Chatbot wie ChatGPT eine starke Wahl.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
        {"label": "Laborbericht-fokussierte Tools vergleichen", "text": "Wenn Sie Plattformen bewerten, die speziell Bluttestberichte analysieren, vergleichen Sie NoryaAI mit Kantesti und Wizey, um zu sehen, welcher Workflow und welches Ausgabeformat zu Ihnen passt.", "link_slug": "norya-vs-kantesti"},
    ],
}
# DE competitor content — using concise keys
for _slug in COMPARE_SLUGS:
    if "de" not in _COMP[_slug]:
        _COMP[_slug]["de"] = {}
_COMP["norya-vs-chatgpt-for-blood-tests"]["de"] = {
    "meta_title": "NoryaAI vs ChatGPT für Bluttests — Ehrlicher Vergleich | NoryaAI",
    "meta_description": "NoryaAI vs ChatGPT für Bluttestanalyse. Strukturierter Bluttest-Analysator vs allgemeiner KI-Chatbot — Seite an Seite.",
    "hero_title": "NoryaAI vs ChatGPT für die Bluttestanalyse",
    "hero_sub": "ChatGPT ist ein leistungsstarker allgemeiner KI-Assistent. NoryaAI ist speziell für die Bluttestanalyse entwickelt. Hier ein ehrlicher Blick auf die Stärken beider.",
    "quick_answer_title": "Kurzfassung",
    "quick_answer": "ChatGPT kann medizinische Begriffe erklären und Gesundheitsfragen beantworten, ist aber nicht für die Analyse von Laborberichten konzipiert. NoryaAI liest Ihre Bluttestergebnisse direkt, ordnet Werte Referenzbereichen zu und erstellt eine strukturierte, arztfertige Zusammenfassung. Beide lösen unterschiedliche Probleme.",
    "cells": {
        "report_upload": "Werte müssen in einen Chat-Prompt kopiert werden; keine native Laborberichts-Analyse",
        "reference_ranges": "Kann allgemeine Bereiche nennen oder Werte halluzinieren; keine Garantie für Übereinstimmung mit Ihrem Labor",
        "units_formatting": "Kein eingebautes Bewusstsein für laborspezifische Einheiten oder regionale Ergebnislayouts",
        "output_structure": "Freitext, der jedes Mal variiert — kein konsistentes Format zur Nachverfolgung von Veränderungen",
        "multilingual": "Kann Text auf Anfrage übersetzen, medizinische Nuancen können bei allgemeiner Übersetzung verloren gehen",
        "doctor_summary": "Kein herunterladbarer Bericht — Sie müssten die Konversation selbst formatieren",
        "privacy": "Gespräche können von OpenAI für Modelltraining gespeichert und verwendet werden",
        "workflow": "Allgemeine Chat-Oberfläche, nicht für Laborberichtsanalyse konzipiert",
        "guided_flow": "Offenes Gespräch — Qualität hängt davon ab, wie gut Sie Ihren Prompt formulieren",
    },
    "helps_title": "Wann ChatGPT dennoch helfen kann",
    "helps_sub": "ChatGPT ist für viele Aufgaben hervorragend. Hier glänzt es wirklich.",
    "helps_items": [
        {"icon": "📚", "title": "Allgemeine Gesundheitsbildung", "desc": "ChatGPT eignet sich hervorragend, um zu lernen, was ein Biomarker bedeutet oder wie das Immunsystem funktioniert."},
        {"icon": "💡", "title": "Arztfragen vorbereiten", "desc": "Vor einem Arzttermin kann ChatGPT Ihnen helfen, Ihre Gedanken zu ordnen und Fragen vorzubereiten."},
        {"icon": "🔍", "title": "Schnelle medizinische Begriffssuche", "desc": "Wenn Sie einen unbekannten Begriff in Ihrem Bericht finden, kann ChatGPT ihn sofort in einfacher Sprache erklären."},
    ],
    "faqs": [
        {"q": "Kann ChatGPT meine Bluttestergebnisse analysieren?", "a": "ChatGPT kann Blutwerte besprechen, wenn Sie sie eintippen, analysiert aber keine Laborberichte, kann Referenzbereiche nicht verifizieren und kann medizinische Details halluzinieren. NoryaAI ist speziell für konsistente, strukturierte Analyse gebaut."},
        {"q": "Ist NoryaAI ein Diagnosetool?", "a": "Nein. NoryaAI bietet strukturierte, informative Erklärungen Ihrer Laborwerte. Es stellt keine Diagnosen und gibt keine Behandlungsempfehlungen. Konsultieren Sie immer einen qualifizierten Arzt."},
        {"q": "Warum nicht einfach ChatGPT nach meinen Laborwerten fragen?", "a": "Sie können, aber ChatGPT gibt jedes Mal eine andere Antwort, verfolgt keine Referenzbereiche und kann keinen druckbaren Bericht erstellen. NoryaAI erzeugt jedes Mal einen konsistenten Gesundheitsscore und ein arztfertiges PDF."},
        {"q": "Sind meine Daten bei ChatGPT vs NoryaAI sicher?", "a": "OpenAI kann Gespräche für Modelltraining speichern. NoryaAI ist DSGVO/KVKK-konform — Ihre Daten sind verschlüsselt, werden nie verkauft und nie für Training verwendet."},
    ],
}
_COMP["norya-vs-bloodgpt"]["de"] = {
    "meta_title": "NoryaAI vs BloodGPT für Bluttests — Ehrlicher Vergleich | NoryaAI",
    "meta_description": "Vergleichen Sie NoryaAI und BloodGPT für Bluttestanalyse. Strukturierte Berichte, mehrsprachige Ausgabe und arztfertige PDFs versus ein chatbasierter Workflow.",
    "hero_title": "NoryaAI vs BloodGPT für die Bluttestanalyse",
    "hero_sub": "BloodGPT wirkt wie eine bluttestfokussierte KI-Chat-Erfahrung. NoryaAI ist rund um strukturierte Berichte, referenzbereichsbewusste Analyse und arztfertige Ausgabe aufgebaut. So unterscheiden sich die Ansätze.",
    "quick_answer_title": "Kurzfassung",
    "quick_answer": "BloodGPT verfolgt einen chatbasierten Ansatz für Gespräche über Bluttestergebnisse. NoryaAI ist ein strukturierter Upload-und-Bericht-Workflow: Ihr Laborbericht wird gelesen, Marker werden Referenzbereichen zugeordnet und eine mehrsprachige Zusammenfassung mit Gesundheitsscore und arztfertigem PDF erstellt. Das eine ist konversationell, das andere auf wiederholbare Berichte ausgelegt.",
    "cells": {
        "report_upload": "Chat-first-Workflow; native Upload-Unterstützung für Laborberichte ist nicht klar offengelegt",
        "reference_ranges": "Kann Bereiche im Gespräch besprechen, aber labspezifische Zuordnung und Struktur sind nicht klar offengelegt",
        "units_formatting": "Kann Werte im Chat interpretieren, aber Unterstützung für verschiedene Laborlayouts und Einheiten ist nicht klar offengelegt",
        "output_structure": "Konversationsartige Antworten statt fester Berichtsstruktur",
        "multilingual": "Sprachabdeckung ist nicht klar offengelegt",
        "doctor_summary": "Arztfertiges PDF oder verifiziertes Exportformat ist nicht klar offengelegt",
        "privacy": "Siehe Richtlinie für Speicherung, Aufbewahrung und Modellnutzung",
        "workflow": "Bluttestfokussierte KI-Chat-Erfahrung",
        "guided_flow": "Konversationelles Q&A über Bluttestergebnisse",
    },
    "helps_title": "Wann BloodGPT dennoch helfen kann",
    "helps_sub": "Ein chatbasierter Bluttestdienst kann zu Nutzern passen, die Rückfragen lieber im Gespräch als in einem festen Bericht klären.",
    "helps_items": [
        {"icon": "💬", "title": "Gesprächsorientierte Erfahrung", "desc": "Wenn Sie Anschlussfragen lieber in einer Chat-Oberfläche stellen, kann ein bluttestfokussierter Chatbot natürlicher wirken als ein fixer Bericht."},
        {"icon": "🧪", "title": "Bluttestfokussierte Prompts", "desc": "Ein fokussierter Chatbot kann einen engeren Kontext als eine allgemeine KI bieten, wenn Sie Biomarker im Gespräch diskutieren möchten."},
        {"icon": "⚡", "title": "Schnelle explorative Antworten", "desc": "Für schnelles Hin-und-Her-Denken zu Laborwerten kann eine konversationelle Oberfläche hilfreich sein, bevor Sie eine formale Zusammenfassung brauchen."},
    ],
    "faqs": [
        {"q": "Was ist der Unterschied zwischen BloodGPT und NoryaAI?", "a": "BloodGPT scheint sich auf Bluttest-Interpretation im Chatstil zu konzentrieren. NoryaAI konzentriert sich auf strukturierte Bluttestberichte mit Referenzbereichslogik, Gesundheitsscores, mehrsprachiger Ausgabe und arztfertigen PDFs."},
        {"q": "Reicht eine Chat-Oberfläche für die Bluttestbewertung aus?", "a": "Das hängt vom Ziel ab. Chat kann für Diskussionen nützlich sein. Wenn Sie jedoch ein konsistentes Format möchten, das Sie erneut öffnen, über die Zeit vergleichen oder mit einem Arzt teilen können, ist ein strukturierter Bericht meist praktischer."},
        {"q": "Ist NoryaAI ein Diagnosetool?", "a": "Nein. NoryaAI liefert strukturierte, informative Erklärungen von Laborwerten. Es stellt keine Diagnosen und empfiehlt keine Behandlung. Konsultieren Sie für medizinische Entscheidungen immer einen qualifizierten Arzt."},
    ],
}
_COMP["norya-vs-kantesti"]["de"] = {
    "meta_title": "NoryaAI vs Kantesti — Bluttest-Vergleich | NoryaAI",
    "meta_description": "NoryaAI vs Kantesti für Bluttestanalyse. Funktionsvergleich zweier Plattformen — Upload-Workflow, Berichtsstruktur und mehrsprachiger Support.",
    "hero_title": "NoryaAI vs Kantesti für die Bluttestanalyse",
    "hero_sub": "Sowohl NoryaAI als auch Kantesti helfen Nutzern, Bluttestergebnisse zu verstehen. Hier ein ehrlicher Vergleich.",
    "quick_answer_title": "Kurzfassung",
    "quick_answer": "Kantesti ist ein Bluttest-Analysedienst hauptsächlich für türkischsprachige Nutzer. NoryaAI bietet einen strukturierten, mehrsprachigen Workflow mit Gesundheitsscores, arztfertigen PDFs und Unterstützung für 9+ Sprachen.",
    "cells": {
        "report_upload": "Unterstützt Laboreingabe zur Analyse", "reference_ranges": "Bietet Referenzbereichsinformationen",
        "units_formatting": "Verarbeitet türkische Laborberichtsformate", "output_structure": "Liefert Analyseergebnisse im eigenen Format",
        "multilingual": "Hauptsächlich auf Türkisch verfügbar", "doctor_summary": "Berichtsformat und Freigabeoptionen nicht klar offengelegt",
        "privacy": "Datenverarbeitungsrichtlinien auf ihrer Plattform verfügbar", "workflow": "Fokussiert auf Bluttestergebnis-Interpretation",
        "guided_flow": "Bietet eigenen Analyse-Workflow",
    },
    "helps_title": "Wann Kantesti besser passen kann", "helps_sub": "Verschiedene Tools passen besser für verschiedene Menschen.",
    "helps_items": [
        {"icon": "🇹🇷", "title": "Türkisch-erste Erfahrung", "desc": "Für eine Plattform, die primär für türkischsprachige Nutzer gebaut ist, bietet Kantesti eine native türkische Oberfläche."},
        {"icon": "🏥", "title": "Lokale Laborkenntnisse", "desc": "Kantesti ist möglicherweise mit spezifischen türkischen Laborformaten und Konventionen vertraut."},
        {"icon": "📋", "title": "Einfache Analyse", "desc": "Für eine unkomplizierte Bluttest-Interpretation ohne mehrsprachige Anforderungen kann Kantesti gut geeignet sein."},
    ],
    "faqs": [
        {"q": "Was ist Kantesti?", "a": "Kantesti ist eine Bluttest-Analyseplattform, die hauptsächlich türkischsprachige Nutzer bedient."},
        {"q": "Wie unterscheidet sich NoryaAI von Kantesti?", "a": "NoryaAI bietet strukturierte Gesundheitsscores, arztfertige PDFs, mehrsprachige Berichte in 9+ Sprachen und unterstützt Laborformate weltweit."},
        {"q": "Ist NoryaAI ein Diagnosetool?", "a": "Nein. NoryaAI bietet strukturierte, informative Erklärungen. Konsultieren Sie immer einen qualifizierten Arzt für medizinische Entscheidungen."},
    ],
}
_COMP["norya-vs-siphox-health"]["de"] = {
    "meta_title": "NoryaAI vs SiPhox Health — Bluttest-Vergleich | NoryaAI",
    "meta_description": "NoryaAI vs SiPhox Health: Heim-Testkits vs strukturierte Laborberichtsanalyse. Vergleichen Sie Ansätze zum Verstehen Ihrer Bluttestergebnisse.",
    "hero_title": "NoryaAI vs SiPhox Health",
    "hero_sub": "SiPhox Health bietet Heim-Biomarker-Testkits an. NoryaAI analysiert Ihre vorhandenen Laborergebnisse und erstellt strukturierte Berichte. Hier der Vergleich.",
    "quick_answer_title": "Kurzfassung",
    "quick_answer": "SiPhox Health und NoryaAI bedienen verschiedene Phasen der Gesundheitstests. SiPhox bietet Heim-Testkits, NoryaAI analysiert vorhandene Laborergebnisse aus jedem Labor und Format. Sie können sich ergänzen.",
    "cells": {
        "report_upload": "Ergebnisse aus eigenen Heim-Testkits — nicht für externe Laborberichte", "reference_ranges": "Zeigt Bereiche für eigene Biomarker-Panels",
        "units_formatting": "Standardisiert auf eigenes Testkit-Format", "output_structure": "Dashboard und Ergebnisse innerhalb ihrer Plattform",
        "multilingual": "Hauptsächlich auf Englisch verfügbar", "doctor_summary": "Ergebnisse in ihrer Plattform einsehbar; Exportoptionen nicht klar offengelegt",
        "privacy": "Datenverarbeitungsrichtlinien auf ihrer Website", "workflow": "End-to-End-Tests: Kit bestellen, Probe sammeln, Ergebnisse erhalten",
        "guided_flow": "Geführter Heim-Test-Workflow an eigene Kits gebunden",
    },
    "helps_title": "Wann SiPhox Health besser passen kann", "helps_sub": "SiPhox Health und NoryaAI bedienen verschiedene Bedürfnisse.",
    "helps_items": [
        {"icon": "🏠", "title": "Bequemlichkeit zu Hause", "desc": "Testen ohne Laborbesuch — SiPhox Health sendet ein Kit zu Ihnen."},
        {"icon": "📊", "title": "Regelmäßiges Monitoring", "desc": "SiPhox bietet abonnementbasierte Tests für regelmäßige Biomarker-Nachverfolgung."},
        {"icon": "🔬", "title": "Kuratierte Panels", "desc": "Testpanels sind auf Gesundheitsziele wie Langlebigkeit oder metabolische Gesundheit ausgerichtet."},
    ],
    "faqs": [
        {"q": "Was ist SiPhox Health?", "a": "SiPhox Health bietet Heim-Biomarker-Testkits. Kit bestellen, Probe zu Hause sammeln, Ergebnisse über deren Plattform erhalten."},
        {"q": "Brauche ich ein Testkit für NoryaAI?", "a": "Nein. NoryaAI arbeitet mit vorhandenen Laborergebnissen — aus jedem Labor, jedem Land. PDF oder Foto hochladen, Text einfügen."},
        {"q": "Ist NoryaAI ein Diagnosetool?", "a": "Nein. NoryaAI bietet strukturierte, informative Erklärungen. Konsultieren Sie immer einen qualifizierten Arzt."},
    ],
}
_COMP["norya-vs-wizey"]["de"] = {
    "meta_title": "NoryaAI vs Wizey — Bluttest-Vergleich | NoryaAI",
    "meta_description": "NoryaAI vs Wizey für Bluttestanalyse. Strukturierte Berichtsfunktionen, mehrsprachiger Support und Workflow im Vergleich.",
    "hero_title": "NoryaAI vs Wizey für die Bluttestanalyse",
    "hero_sub": "Sowohl NoryaAI als auch Wizey helfen Nutzern, Bluttestergebnisse zu verstehen. Hier ein ehrlicher Vergleich.",
    "quick_answer_title": "Kurzfassung",
    "quick_answer": "Wizey bietet Bluttest-Analysetools. NoryaAI liefert einen strukturierten, uploadbasierten Workflow mit Gesundheitsscores, arztfertigen PDFs und mehrsprachigen Berichten aus jedem Laborformat.",
    "cells": {
        "report_upload": "Akzeptiert Laborergebnisse zur Analyse", "reference_ranges": "Bietet Referenzbereichsinformationen",
        "units_formatting": "Laborformat-Unterstützung nicht klar offengelegt", "output_structure": "Liefert Analyse im eigenen Format",
        "multilingual": "Sprachunterstützung nicht klar offengelegt", "doctor_summary": "Berichtsfreigabeoptionen nicht klar offengelegt",
        "privacy": "Datenverarbeitungsrichtlinien auf ihrer Plattform", "workflow": "Bietet Bluttest-Interpretations-Workflow",
        "guided_flow": "Bietet eigenen Analyseprozess",
    },
    "helps_title": "Wann Wizey dennoch helfen kann", "helps_sub": "Verschiedene Tools passen zu verschiedenen Vorlieben.",
    "helps_items": [
        {"icon": "📱", "title": "Eigener Ansatz", "desc": "Wizey bietet möglicherweise Funktionen, die zu Ihren spezifischen Vorlieben passen."},
        {"icon": "🔄", "title": "Alternative Perspektive", "desc": "Eine zweite Interpretation von einem anderen Tool kann zusätzlichen Kontext bieten."},
        {"icon": "💭", "title": "Persönliche Präferenz", "desc": "Das richtige Tool hängt von Ihrem Workflow, Sprachbedürfnissen und bevorzugter Ausgabe ab."},
    ],
    "faqs": [
        {"q": "Was ist Wizey?", "a": "Wizey ist eine Bluttest-Analyseplattform. Für Details empfehlen wir, deren Website direkt zu besuchen."},
        {"q": "Wie unterscheidet sich NoryaAI von Wizey?", "a": "NoryaAI bietet strukturierte Gesundheitsscores, arztfertige PDFs, mehrsprachige Berichte in 9+ Sprachen und akzeptiert Laborberichte weltweit."},
        {"q": "Ist NoryaAI ein Diagnosetool?", "a": "Nein. NoryaAI bietet strukturierte, informative Erklärungen. Konsultieren Sie immer einen qualifizierten Arzt."},
    ],
}
_COMP["norya-vs-generic-ai"]["de"] = {
    "meta_title": "NoryaAI vs Allgemeine KI für Bluttests — Ehrlicher Vergleich | NoryaAI",
    "meta_description": "NoryaAI vs ChatGPT oder andere KI-Chatbots für Bluttestergebnisse. Strukturierte Berichte vs Freitext-Chat-Antworten im Vergleich.",
    "hero_title": "NoryaAI vs Allgemeine KI-Chatbots für Bluttests",
    "hero_sub": "Beide können mit Labordaten arbeiten — aber auf sehr unterschiedliche Weise. Ein ehrlicher Vergleich dessen, was jeder bietet.",
    "quick_answer_title": "Kurzfassung",
    "quick_answer": "Allgemeine KI-Chatbots können medizinische Begriffe erklären. NoryaAI ist speziell für Bluttests gebaut: Es liest Ihren Laborbericht, ordnet Werte Referenzbereichen zu und erstellt eine strukturierte, arztfertige Zusammenfassung mit Gesundheitsscore. Beide haben ihren Platz, lösen aber unterschiedliche Probleme.",
    "cells": {
        "report_upload": "Werte in einen Chat-Prompt kopieren und auf korrekte Formatierung hoffen",
        "reference_ranges": "Kann Bereiche raten oder weglassen; keine Garantie für Übereinstimmung mit Ihrem Labor",
        "units_formatting": "Kein Bewusstsein für laborspezifische Einheiten oder Ergebnislayouts",
        "output_structure": "Freitext-Absatz, der bei jedem Prompt variiert — kein konsistentes Format",
        "multilingual": "Kann Text übersetzen, medizinische Nuancen können bei allgemeiner Übersetzung verloren gehen",
        "doctor_summary": "Kein herunterladbarer Bericht — Sie müssten den Chat selbst kopieren und formatieren",
        "privacy": "Gespräche können für Modelltraining gespeichert werden",
        "workflow": "Allgemeine Chat-Oberfläche für beliebige Themen",
        "guided_flow": "Offenes Gespräch — Qualität hängt von der Formulierung Ihres Prompts ab",
    },
    "helps_title": "Wann allgemeine KI-Chatbots dennoch helfen können",
    "helps_sub": "Es geht nicht darum, dass ein Tool schlecht und ein anderes gut ist. Sie dienen verschiedenen Zwecken.",
    "helps_items": [
        {"icon": "📚", "title": "Allgemeine Gesundheitsbildung", "desc": "Chatbots eignen sich hervorragend zum Lernen über Biomarker, Immunsystem oder medizinische Konzepte."},
        {"icon": "💡", "title": "Fragen für den Arzt vorbereiten", "desc": "Vor einem Termin kann ein Chatbot helfen, Ihre Fragen zu strukturieren."},
        {"icon": "🔍", "title": "Medizinische Terminologie verstehen", "desc": "Unbekannte Begriffe in Ihrem Bericht kann eine allgemeine KI schnell in einfacher Sprache erklären."},
    ],
    "faqs": [
        {"q": "Kann ChatGPT Bluttestergebnisse erklären?", "a": "Ja, teilweise. ChatGPT kann erklären, was einzelne Werte allgemein bedeuten. Es analysiert aber nicht Ihren tatsächlichen Laborbericht, kann Referenzbereiche halluzinieren und gibt jedes Mal eine andere Antwort. NoryaAI liest Ihren Bericht direkt und gibt eine konsistente, strukturierte Zusammenfassung aus."},
        {"q": "Ist NoryaAI ein Diagnosetool?", "a": "Nein. NoryaAI bietet strukturierte, informative Erklärungen Ihrer Laborwerte. Es diagnostiziert keine Erkrankungen und empfiehlt keine Behandlungen. Konsultieren Sie immer einen qualifizierten Arzt."},
        {"q": "Warum ist ein strukturierter Bericht besser als eine Chat-Antwort?", "a": "Ein strukturierter Bericht liefert Gesundheitsscore, Kategorieaufschlüsselung und markierte Marker in konsistentem Format. Sie können mit früheren Tests vergleichen und auf einen Blick sehen, welche Werte Aufmerksamkeit brauchen."},
        {"q": "Kann ich statt manueller Eingabe ein PDF hochladen?", "a": "Ja. NoryaAI akzeptiert PDF-Uploads, Fotos gedruckter Laborberichte und eingefügten Text. Werte und Referenzbereiche werden automatisch erkannt."},
    ],
}


# ══════════════════════════════════════════════════════════════════
# TRANSLATIONS — remaining languages (FR, ES, IT, HE, HI, AR)
# are loaded from the companion module to keep this file navigable.
# ══════════════════════════════════════════════════════════════════
from app.compare_translations import apply_translations as _apply_translations  # noqa: E402
_apply_translations(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP)

_BLOODGPT_HUB_I18N: dict[str, dict] = {
    "fr": {
        "summary": "Comparez un workflow d'IA conversationnelle centré sur les analyses sanguines avec les rapports structurés, multilingues et prêts pour le médecin de NoryaAI.",
        "best_use": "Chat axé sur les analyses sanguines",
        "workflow": "Disponible",
        "upload": "Non clairement divulgué",
        "ranges": "Partiel",
        "output": "Réponse de type chat",
        "languages": "Non clairement divulgué",
        "doctor_summary": "Non clairement divulgué",
        "privacy": "Voir leur politique",
        "clinician": "Partiel",
        "accuracy": "Non divulgué",
    },
    "es": {
        "summary": "Compare un flujo conversacional de IA centrado en análisis de sangre con los informes estructurados, multilingues y listos para el médico de NoryaAI.",
        "best_use": "Chat centrado en análisis de sangre",
        "workflow": "Disponible",
        "upload": "No claramente divulgado",
        "ranges": "Parcial",
        "output": "Respuesta tipo chat",
        "languages": "No claramente divulgado",
        "doctor_summary": "No claramente divulgado",
        "privacy": "Consulte su política",
        "clinician": "Parcial",
        "accuracy": "No divulgado",
    },
    "it": {
        "summary": "Confronta un flusso conversazionale di IA focalizzato sugli esami del sangue con i report strutturati, multilingue e pronti per il medico di NoryaAI.",
        "best_use": "Chat focalizzata sugli esami del sangue",
        "workflow": "Disponibile",
        "upload": "Non chiaramente divulgato",
        "ranges": "Parziale",
        "output": "Risposta in stile chat",
        "languages": "Non chiaramente divulgato",
        "doctor_summary": "Non chiaramente divulgato",
        "privacy": "Vedi la loro policy",
        "clinician": "Parziale",
        "accuracy": "Non divulgato",
    },
    "he": {
        "summary": "השוו חוויית AI שיחתית ממוקדת בדיקות דם לדוחות המובנים, הרב-לשוניים והמוכנים לרופא של NoryaAI.",
        "best_use": "צ'אט ממוקד בדיקות דם",
        "workflow": "זמין",
        "upload": "לא נחשף בבירור",
        "ranges": "חלקי",
        "output": "תשובה בסגנון צ'אט",
        "languages": "לא נחשף בבירור",
        "doctor_summary": "לא נחשף בבירור",
        "privacy": "ראו את המדיניות שלהם",
        "clinician": "חלקי",
        "accuracy": "לא נחשף",
    },
    "hi": {
        "summary": "ब्लड टेस्ट पर केंद्रित AI चैट वर्कफ़्लो की तुलना NoryaAI की संरचित, बहुभाषी और डॉक्टर-तैयार रिपोर्टों से करें।",
        "best_use": "ब्लड टेस्ट केंद्रित चैट",
        "workflow": "उपलब्ध",
        "upload": "स्पष्ट रूप से सार्वजनिक नहीं",
        "ranges": "आंशिक",
        "output": "चैट शैली उत्तर",
        "languages": "स्पष्ट रूप से सार्वजनिक नहीं",
        "doctor_summary": "स्पष्ट रूप से सार्वजनिक नहीं",
        "privacy": "उनकी नीति देखें",
        "clinician": "आंशिक",
        "accuracy": "प्रकट नहीं",
    },
    "ar": {
        "summary": "قارن بين تجربة ذكاء اصطناعي محادثية مركزة على تحاليل الدم وبين التقارير المنظمة ومتعددة اللغات والجاهزة للطبيب من NoryaAI.",
        "best_use": "دردشة مركزة على تحاليل الدم",
        "workflow": "متاح",
        "upload": "غير مُفصح عنه بوضوح",
        "ranges": "جزئي",
        "output": "إجابة بأسلوب الدردشة",
        "languages": "غير مُفصح عنه بوضوح",
        "doctor_summary": "غير مُفصح عنه بوضوح",
        "privacy": "راجع سياستهم",
        "clinician": "جزئي",
        "accuracy": "غير مُفصح عنه",
    },
}


def _inject_bloodgpt_hub_content() -> None:
    localized = {
        "en": {
            "summary": "A blood-test-focused AI chat workflow compared with NoryaAI's structured reports, multilingual output, and doctor-ready summaries.",
            "best_use": "Blood-test-focused chat Q&A",
            "workflow": "Available",
            "upload": "Not clearly disclosed",
            "ranges": "Partial",
            "output": "Chat-style answer",
            "languages": "Not clearly disclosed",
            "doctor_summary": "Not clearly disclosed",
            "privacy": "See their policy",
            "clinician": "Partial",
            "accuracy": "Not disclosed",
        },
        "tr": {
            "summary": "Kan tahliline odaklı sohbet tabanlı bir yapay zeka deneyimini NoryaAI'ın yapılandırılmış raporları ve doktora hazır çıktılarıyla karşılaştırın.",
            "best_use": "Kan tahlili odaklı sohbet",
            "workflow": "Mevcut",
            "upload": "Net olarak açıklanmamış",
            "ranges": "Kısmi",
            "output": "Sohbet tarzı yanıt",
            "languages": "Net olarak açıklanmamış",
            "doctor_summary": "Net olarak açıklanmamış",
            "privacy": "Gizlilik politikasına bakınız",
            "clinician": "Kısmi",
            "accuracy": "Açıklanmamış",
        },
        "de": {
            "summary": "Ein bluttestfokussierter KI-Chat-Workflow im Vergleich zu NoryaAIs strukturierten Berichten und arztfertigen Zusammenfassungen.",
            "best_use": "Bluttestfokussierter Chat",
            "workflow": "Verfügbar",
            "upload": "Nicht klar offengelegt",
            "ranges": "Teilweise",
            "output": "Chat-Antwort",
            "languages": "Nicht klar offengelegt",
            "doctor_summary": "Nicht klar offengelegt",
            "privacy": "Siehe Datenschutzrichtlinie",
            "clinician": "Teilweise",
            "accuracy": "Nicht offengelegt",
        },
        **_BLOODGPT_HUB_I18N,
    }
    for lang, hub in _HUB.items():
        loc = localized.get(lang, localized["en"])
        cards = hub.setdefault("cards", [])
        if not any(card.get("slug") == "norya-vs-bloodgpt" for card in cards):
            link_text = cards[0]["link_text"] if cards else "Read full comparison"
            insert_at = next((i + 1 for i, card in enumerate(cards) if card.get("slug") == "norya-vs-chatgpt-for-blood-tests"), len(cards))
            cards.insert(insert_at, {
                "slug": "norya-vs-bloodgpt",
                "name": "BloodGPT",
                "summary": loc["summary"],
                "link_text": link_text,
            })
        cols = hub.setdefault("matrix_columns", [])
        if not any(col.get("key") == "bloodgpt" for col in cols):
            insert_at = next((i + 1 for i, col in enumerate(cols) if col.get("key") == "chatgpt"), len(cols))
            cols.insert(insert_at, {"key": "bloodgpt", "name": "BloodGPT", "slug": "norya-vs-bloodgpt"})
        rows = hub.setdefault("matrix_rows", [])
        bloodgpt_values = [
            loc["best_use"],
            loc["workflow"],
            loc["upload"],
            loc["ranges"],
            loc["output"],
            loc["languages"],
            loc["doctor_summary"],
            loc["privacy"],
            loc["clinician"],
            loc["accuracy"],
        ]
        for idx, val in enumerate(bloodgpt_values):
            if idx < len(rows) and "bloodgpt" not in rows[idx]:
                rows[idx]["bloodgpt"] = val


_inject_bloodgpt_hub_content()


# ══════════════════════════════════════════════════════════════════
# PUBLIC API
# ══════════════════════════════════════════════════════════════════

def _build_comparison_items(lang: str, slug: str) -> list[dict]:
    labels = _LABELS.get(lang, _LABELS["en"])
    norya = _NORYA.get(lang, _NORYA["en"])
    comp_data = _COMP.get(slug, {}).get(lang) or _COMP.get(slug, {}).get("en")
    if not comp_data:
        return []
    cells = comp_data.get("cells", {})
    return [
        {"label": labels[k], "competitor": cells.get(k, ""), "norya": norya[k]}
        for k in _ROW_KEYS
    ]


def _get_compare_visual(slug: str) -> dict:
    visual = _COMPARE_VISUALS.get(slug, {})
    return {
        "image": visual.get("image", "/static/images/og-default.png"),
        "accent": visual.get("accent", "#0EA5A4"),
        "glow": visual.get("glow", "rgba(14,165,164,0.28)"),
        "mark": visual.get("mark", "AI"),
    }


def _enrich_compare_card(card: dict) -> dict:
    out = dict(card)
    out["visual"] = _get_compare_visual(card["slug"])
    return out


def get_compare_detail(lang: str, slug: str) -> dict | None:
    """Full template context for a comparison detail page."""
    if slug not in _COMP or lang not in COMPARE_LANGS:
        return None
    comp = _COMP[slug]
    c = comp.get(lang) or comp.get("en")
    if not c:
        return None
    ui = _UI.get(lang, _UI["en"])
    why = _WHY.get(lang, _WHY["en"])
    cta = _CTA.get(lang, _CTA["en"])
    hub = _HUB.get(lang, _HUB["en"])
    return {
        "meta_title": c["meta_title"],
        "meta_description": c["meta_description"],
        "hero_title": c["hero_title"],
        "hero_sub": c["hero_sub"],
        "hero_visual": _get_compare_visual(slug),
        "hero_highlights": hub.get("trust_stats", _HUB["en"]["trust_stats"]),
        "cta_hero_primary": cta["hero_primary"],
        "cta_hero_secondary": cta["hero_secondary"],
        "quick_answer_title": c["quick_answer_title"],
        "quick_answer": c["quick_answer"],
        "comparison_title": ui.get("comparison_title", _UI["en"].get("comparison_title", "")),
        "comparison_sub": ui.get("comparison_sub", _UI["en"].get("comparison_sub", "")),
        "comparison_items": _build_comparison_items(lang, slug),
        "competitor_name": comp["name"],
        "helps_title": c["helps_title"],
        "helps_sub": c["helps_sub"],
        "helps_items": c["helps_items"],
        "why_norya_title": why["title"],
        "why_norya_sub": why["sub"],
        "why_norya_items": why["items"],
        "faqs": c["faqs"],
        "accuracy_badge": _ACCURACY_BADGE.get(lang, _ACCURACY_BADGE["en"]),
        "cta_title": cta["title"],
        "cta_sub": cta["sub"],
        "cta_primary": cta["primary"],
        "cta_secondary": cta["secondary"],
        # UI
        **{f"ui_{k}": v for k, v in ui.items()},
    }


def get_compare_hub(lang: str) -> dict | None:
    """Full template context for the comparison hub page."""
    if lang not in COMPARE_LANGS:
        return None
    hub = _HUB.get(lang)
    if not hub:
        return None
    ui = _UI.get(lang, _UI["en"])
    cta = _CTA.get(lang, _CTA["en"])
    en_hub = _HUB["en"]
    return {
        "meta_title": hub["meta_title"],
        "meta_description": hub["meta_description"],
        "hero_title": hub["hero_title"],
        "hero_sub": hub["hero_sub"],
        "trust_stats": hub.get("trust_stats", en_hub["trust_stats"]),
        "cards": [_enrich_compare_card(card) for card in hub["cards"]],
        "hub_faqs": hub["hub_faqs"],
        "matrix_title": hub.get("matrix_title", en_hub["matrix_title"]),
        "matrix_sub": hub.get("matrix_sub", en_hub["matrix_sub"]),
        "matrix_row_labels": hub.get("matrix_row_labels", en_hub["matrix_row_labels"]),
        "matrix_columns": hub.get("matrix_columns", en_hub["matrix_columns"]),
        "matrix_rows": hub.get("matrix_rows", en_hub["matrix_rows"]),
        "suits_title": hub.get("suits_title", en_hub["suits_title"]),
        "suits_items": hub.get("suits_items", en_hub["suits_items"]),
        "cta_title": cta["title"],
        "cta_sub": cta["sub"],
        "cta_primary": cta["primary"],
        "cta_secondary": cta["secondary"],
        **{f"ui_{k}": v for k, v in ui.items()},
    }


def get_compare_hreflang_detail(lang: str, slug: str, base_url: str) -> list[dict]:
    """Hreflang alternates for a comparison detail page (all locales + x-default)."""
    alts = []
    for loc in COMPARE_LANGS:
        if loc in (_COMP.get(slug, {})):
            alts.append({"hreflang": loc, "href": f"{base_url}/{loc}/compare/{slug}"})
    alts.append({"hreflang": "x-default", "href": f"{base_url}/en/compare/{slug}"})
    return alts


def get_compare_hreflang_hub(lang: str, base_url: str) -> list[dict]:
    """Hreflang alternates for the comparison hub page."""
    alts = []
    for loc in COMPARE_LANGS:
        if loc in _HUB:
            alts.append({"hreflang": loc, "href": f"{base_url}/{loc}/compare/"})
    alts.append({"hreflang": "x-default", "href": f"{base_url}/en/compare/"})
    return alts


def get_compare_og_locale(lang: str) -> str:
    return _OG.get(lang, "en_US")


def get_compare_related(lang: str, current_slug: str) -> list[dict]:
    """Other competitor pages for the 'Related comparisons' block."""
    out = []
    for slug in COMPARE_SLUGS:
        if slug == current_slug:
            continue
        comp = _COMP.get(slug, {})
        if lang not in comp and "en" not in comp:
            continue
        out.append({
            "slug": slug,
            "name": comp["name"],
            "url": f"/{lang}/compare/{slug}",
            "visual": _get_compare_visual(slug),
        })
    return out


def get_compare_breadcrumbs(lang: str, base_url: str, slug: str | None = None, competitor_name: str | None = None) -> list[dict]:
    """Breadcrumb items for JSON-LD and visible trail."""
    ui = _UI.get(lang, _UI["en"])
    items = [
        {"name": ui["home"], "url": f"{base_url}/{lang}"},
        {"name": ui["compare"], "url": f"{base_url}/{lang}/compare/"},
    ]
    if slug and competitor_name:
        items.append({"name": f"NoryaAI vs {competitor_name}", "url": f"{base_url}/{lang}/compare/{slug}"})
    return items


def iter_compare_sitemap_urls():
    """Yield (lang, path) tuples for all compare pages (hub + detail)."""
    for lang in COMPARE_LANGS:
        if lang in _HUB:
            yield (lang, f"{lang}/compare/")
        for slug in COMPARE_SLUGS:
            if lang in _COMP.get(slug, {}):
                yield (lang, f"{lang}/compare/{slug}")
