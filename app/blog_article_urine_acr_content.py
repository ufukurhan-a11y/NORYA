"""Dedicated English blog article for urine ACR / microalbumin intent."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what urine ACR measures",
            body_html=(
                "<p><strong>Urine ACR</strong> stands for <strong>albumin-to-creatinine ratio</strong>. "
                "It measures how much albumin is leaking into the urine compared with creatinine, "
                "which helps adjust for how concentrated or diluted the urine sample is. It is "
                "often used to look for <strong>early kidney damage</strong>, especially in people "
                "with diabetes, high blood pressure, or chronic kidney disease risk.</p>"
            ),
        ),
        Section(
            id="microalbumin-vs-acr",
            level=2,
            heading="Is urine ACR the same as a microalbumin test?",
            body_html=(
                "<p>People often use the terms <strong>microalbumin</strong> and <strong>urine ACR</strong> "
                "interchangeably. In practice, a urine ACR is the more useful report format because it "
                "relates albumin to creatinine, which makes the result easier to compare between samples. "
                "This is why many labs now report an albumin-to-creatinine ratio rather than albumin alone.</p>"
            ),
        ),
        Section(
            id="what-high-acr-means",
            level=2,
            heading="What a high urine ACR may mean",
            body_html=(
                "<p>A higher urine ACR can mean the kidneys are allowing more albumin to pass into the urine "
                "than expected. Doctors often think about <strong>diabetes, blood pressure, kidney disease risk, "
                "and cardiovascular risk</strong> when they see this pattern. The result still needs context: "
                "exercise, fever, infection, menstruation, dehydration, and temporary illness can also affect "
                "a urine sample.</p>"
                "<p>Because of that, one abnormal ACR usually leads to <strong>repeat testing</strong> or wider "
                "kidney review rather than an immediate diagnosis.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-it",
            level=2,
            heading="How doctors compare urine ACR with blood tests",
            body_html=(
                "<p>Urine ACR is often interpreted together with:</p>"
                "<ul>"
                "<li><a href=\"/en/blog/creatinine-egfr-what-it-means\">Creatinine and eGFR</a> to understand overall kidney filtration.</li>"
                "<li><a href=\"/en/blog/how-to-read-fasting-blood-sugar-results\">Fasting glucose</a> and <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c</a> when diabetes or prediabetes is relevant.</li>"
                "<li>Blood pressure history, swelling, and medication review.</li>"
                "<li><a href=\"/en/blog/metabolic-panel-results-explained\">Metabolic panel markers</a> when the kidney pattern sits inside a wider chemistry panel.</li>"
                "</ul>"
                "<p>That combined view helps separate a temporary urine finding from a pattern that deserves closer kidney follow-up.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevated: quick pattern guide",
            body_html=(
                "<div class=\"blog-example\"><strong>In range:</strong> usually reassuring, especially if creatinine, eGFR, and blood pressure are also stable.</div>"
                "<div class=\"blog-example\"><strong>Mildly elevated:</strong> often leads to repeat urine ACR and a review of glucose, blood pressure, exercise, and temporary causes.</div>"
                "<div class=\"blog-example\"><strong>Persistently elevated:</strong> makes doctors think more seriously about early kidney damage and long-term kidney or cardiovascular risk reduction.</div>"
                "<div class=\"blog-example\"><strong>Elevated plus worsening creatinine/eGFR:</strong> usually needs a more focused kidney work-up.</div>"
            ),
        ),
        Section(
            id="when-repeat-testing-happens",
            level=2,
            heading="Why repeat testing is common",
            body_html=(
                "<p>A urine ACR can change from day to day. Clinicians often repeat it because a single "
                "sample can be affected by recent exercise, illness, hydration changes, or collection factors. "
                "Persistent elevation across repeated samples matters more than one isolated abnormal result.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="How to use this with your own report",
            body_html=(
                "<p>If your blood work and urine tests are spread across multiple pages, start with "
                "<a href=\"/en/blood-test-results-explained\">blood test results explained</a> or "
                "<a href=\"/en/upload-blood-test-results\">upload your blood test results</a> to turn "
                "the numbers into a single structured summary. That makes it easier to compare urine ACR "
                "with creatinine, eGFR, glucose, and blood pressure-related context before your appointment.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This guide is educational only.</strong> Urine ACR does not diagnose kidney disease "
                "on its own. A clinician should interpret it with repeat testing, symptoms, blood pressure, blood "
                "tests, and your overall medical history.</p>"
            ),
        ),
    ]


def build_urine_acr_article():
    """Build a dedicated English urine ACR / microalbumin article."""
    from app.blog_i18n import Article

    return Article(
        id="urine-acr-microalbumin-meaning",
        published_at=date(2026, 3, 26),
        last_updated=date(2026, 3, 26),
        read_minutes=7,
        cover_image="/static/images/blog/how-to-read-blood-test-results.png",
        category={"en": "Kidney & Metabolic Health"},
        slugs={"en": "urine-acr-microalbumin-meaning"},
        titles={"en": "Urine ACR / Microalbumin Meaning: What a High Albumin-Creatinine Ratio Can Suggest"},
        subtitles={"en": "Understand what urine ACR measures, how it differs from a simple microalbumin result, and why doctors compare it with creatinine, eGFR, glucose, and blood pressure."},
        excerpts={"en": "Plain-language guide to urine ACR and microalbumin, including what high results may suggest, when repeat testing is common, and how doctors connect the result to kidney risk."},
        seo_titles={"en": "Urine ACR / Microalbumin Meaning: High Albumin-Creatinine Ratio | NoryaAI"},
        seo_descriptions={"en": "Learn what urine ACR or microalbumin means, why doctors use albumin-creatinine ratio, and how high results are compared with creatinine, eGFR, and glucose."},
        sections_by_lang={"en": _sections_en()},
        cover_alt={"en": "Kidney-focused blood and urine test interpretation overview"},
        faq_schema_qa={
            "en": [
                {
                    "question": "What is urine ACR?",
                    "answer": "Urine ACR is the albumin-to-creatinine ratio in a urine sample. It is used to detect albumin leakage from the kidneys and helps adjust for how concentrated the urine is.",
                },
                {
                    "question": "Is urine ACR the same as microalbumin?",
                    "answer": "They are closely related. Many people say microalbumin test, but urine ACR is the more informative report format because it compares albumin with creatinine in the same sample.",
                },
                {
                    "question": "Does a high urine ACR always mean kidney disease?",
                    "answer": "Not always. Temporary illness, exercise, infection, dehydration, and collection factors can affect the result. Doctors usually confirm with repeat testing and compare it with blood tests and blood pressure history.",
                },
                {
                    "question": "What is compared with urine ACR?",
                    "answer": "Doctors often compare urine ACR with creatinine, eGFR, fasting glucose, HbA1c, blood pressure, and sometimes other chemistry markers to understand whether the pattern suggests early kidney damage or a temporary finding.",
                },
            ]
        },
    )
