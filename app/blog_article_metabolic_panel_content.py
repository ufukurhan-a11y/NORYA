"""Dedicated English blog article for metabolic panel / CMP / BMP intent."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what a metabolic panel tells you",
            body_html=(
                "<p>A <strong>metabolic panel</strong> is a blood test that groups together "
                "markers related to blood sugar, electrolytes, kidney function, and in the "
                "case of a <strong>Comprehensive Metabolic Panel (CMP)</strong>, liver and "
                "protein markers as well. A <strong>Basic Metabolic Panel (BMP)</strong> is "
                "shorter and usually focuses on glucose, sodium, potassium, chloride, "
                "bicarbonate/CO<sub>2</sub>, calcium, BUN, and creatinine.</p>"
                "<p>Doctors do not interpret the panel as a single score. They compare each "
                "marker with the others to decide whether the pattern looks more related to "
                "hydration, kidney function, glucose control, acid-base balance, liver "
                "stress, or a temporary lab variation.</p>"
            ),
        ),
        Section(
            id="cmp-vs-bmp",
            level=2,
            heading="CMP vs BMP: what is the difference?",
            body_html=(
                "<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\">"
                "<thead><tr class=\"bg-slate-50\">"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Panel</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">What it usually includes</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Typical use</th>"
                "</tr></thead><tbody>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>BMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Glucose, electrolytes, calcium, BUN, creatinine, CO<sub>2</sub>/bicarbonate</td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Hydration, kidney function, electrolyte or acid-base checks</td></tr>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>CMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Everything in a BMP plus albumin, total protein, ALP, ALT, AST, and bilirubin</td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Broader metabolic overview including liver and protein markers</td></tr>"
                "</tbody></table>"
                "<p>If your report says <strong>CMP</strong>, you are usually getting a broader "
                "chemistry overview than a BMP. The exact panel can still vary by lab, so the "
                "best reference is the list of markers shown on your own report.</p>"
            ),
        ),
        Section(
            id="how-doctors-read-it",
            level=2,
            heading="How doctors read a metabolic panel in real life",
            body_html=(
                "<p>Most of the value comes from the <strong>pattern</strong>, not one isolated number. "
                "Examples:</p>"
                "<ul>"
                "<li><strong>Glucose</strong> is often compared with <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c</a> and sometimes fasting insulin or <a href=\"/en/blog/what-is-homa-ir\">HOMA-IR</a>.</li>"
                "<li><strong>BUN, creatinine, and eGFR</strong> are reviewed together to understand kidney function and hydration. See <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR explained</a>.</li>"
                "<li><strong>Sodium, potassium, chloride, and bicarbonate</strong> help doctors think about fluid balance, medications, and acid-base patterns. Related guides: <a href=\"/en/blog/sodium-low-meaning\">low sodium</a> and <a href=\"/en/blog/potassium-high-meaning\">high potassium</a>.</li>"
                "<li><strong>ALT, AST, ALP, bilirubin, albumin, and total protein</strong> give liver and protein context. Start with <a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">high ALT/AST</a>, <a href=\"/en/blog/albumin-low-meaning\">low albumin</a>, and <a href=\"/en/blog/total-protein-high-or-low\">total protein</a>.</li>"
                "</ul>"
                "<p>This is why a metabolic panel is often one of the most useful first-step blood "
                "tests: it connects several systems at once rather than looking at only one biomarker.</p>"
            ),
        ),
        Section(
            id="normal-high-low",
            level=2,
            heading="Normal, mildly abnormal, and clearly abnormal patterns",
            body_html=(
                "<div class=\"blog-example\"><strong>Mostly in range:</strong> Often reassuring, but doctors still compare with symptoms, trend, and why the test was ordered.</div>"
                "<div class=\"blog-example\"><strong>One mild out-of-range result:</strong> Can reflect dehydration, fasting status, medication effect, or lab variation. Repeat testing is common before drawing conclusions.</div>"
                "<div class=\"blog-example\"><strong>Several related markers move together:</strong> More likely to prompt a focused kidney, glucose, liver, or electrolyte work-up.</div>"
                "<div class=\"blog-example\"><strong>Clearly abnormal or symptomatic pattern:</strong> Needs faster review, especially with high potassium, very low sodium, markedly high glucose, or worsening kidney markers.</div>"
            ),
        ),
        Section(
            id="fasting-prep",
            level=2,
            heading="Do you need to fast before a metabolic panel?",
            body_html=(
                "<p>For many labs, a metabolic panel itself does <strong>not always require fasting</strong>, "
                "but fasting may be recommended if the same blood draw also includes glucose-focused or lipid testing. "
                "If your clinician wants fasting glucose, lipid values, or insulin resistance markers interpreted "
                "together, following the lab instructions matters.</p>"
                "<p>Also tell your clinician about supplements, creatine, diuretics, blood pressure medicines, "
                "or recent vomiting, diarrhea, intense exercise, or dehydration, because these can influence results.</p>"
            ),
        ),
        Section(
            id="follow-up",
            level=2,
            heading="What follow-up is common after an abnormal metabolic panel?",
            body_html=(
                "<p>Common next steps depend on which part of the panel is abnormal:</p>"
                "<ul>"
                "<li>Repeat the same chemistry panel if the result may be temporary or affected by hydration.</li>"
                "<li>Add kidney follow-up such as <a href=\"/en/tools/egfr-calculator\">eGFR calculation</a>, <a href=\"/en/blog/urine-acr-microalbumin-meaning\">urine ACR</a>, or blood pressure review.</li>"
                "<li>Add glucose follow-up such as <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c</a>, fasting glucose review, or insulin resistance context.</li>"
                "<li>Add liver or protein-focused follow-up if ALT, AST, ALP, bilirubin, albumin, or total protein are off.</li>"
                "</ul>"
                "<p>An abnormal panel is a signal to interpret in context, not a diagnosis by itself.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="How to use this with your own report",
            body_html=(
                "<p>If your lab report includes a BMP or CMP and you want the full picture, "
                "start with <a href=\"/en/blood-test-results-explained\">blood test results explained</a> "
                "or <a href=\"/en/upload-blood-test-results\">upload your blood test results</a> for a "
                "structured summary. If you are comparing general-purpose AI tools, see the "
                "<a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a> page for how NoryaAI "
                "is tailored to lab reports rather than generic prompting.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This guide is for educational purposes only.</strong> A metabolic panel "
                "cannot diagnose a condition on its own. Always review abnormal results with a "
                "qualified clinician, especially if you have symptoms, repeat abnormalities, or "
                "multiple markers moving together.</p>"
            ),
        ),
    ]


def build_metabolic_panel_article():
    """Build a dedicated English metabolic panel article."""
    from app.blog_i18n import Article

    return Article(
        id="metabolic-panel-results-explained",
        published_at=date(2026, 3, 26),
        last_updated=date(2026, 3, 26),
        read_minutes=8,
        cover_image="/static/images/blog/how-to-read-blood-test-results.png",
        category={"en": "Metabolic Panel"},
        slugs={"en": "metabolic-panel-results-explained"},
        titles={"en": "Metabolic Panel Results Explained: CMP vs BMP, Normal, High, and Low Patterns"},
        subtitles={"en": "Understand what a metabolic panel includes, how doctors read CMP and BMP results, and which combinations of markers usually drive follow-up."},
        excerpts={"en": "Clear guide to metabolic panel results, including CMP vs BMP, common markers, normal vs abnormal patterns, and what doctors usually compare next."},
        seo_titles={"en": "Metabolic Panel Results Explained: CMP vs BMP, Normal, High, Low | NoryaAI"},
        seo_descriptions={"en": "Learn how to read metabolic panel results, including CMP vs BMP, glucose, electrolytes, kidney markers, liver markers, and common follow-up patterns."},
        sections_by_lang={"en": _sections_en()},
        cover_alt={"en": "Blood test report overview for metabolic panel interpretation"},
        faq_schema_qa={
            "en": [
                {
                    "question": "What is the difference between a CMP and a BMP?",
                    "answer": "A BMP usually covers glucose, electrolytes, calcium, BUN, creatinine, and bicarbonate/CO2. A CMP includes those plus albumin, total protein, ALT, AST, ALP, and bilirubin for a broader chemistry overview.",
                },
                {
                    "question": "Does one abnormal metabolic panel result mean disease?",
                    "answer": "Not necessarily. A single mild abnormality can reflect hydration, fasting status, medication effect, or temporary variation. Doctors usually interpret the result together with symptoms, trend, and the rest of the panel.",
                },
                {
                    "question": "Do I need to fast before a metabolic panel?",
                    "answer": "Not always. Some labs allow non-fasting metabolic panels, but fasting may still be advised if glucose-focused tests, lipids, or insulin-related markers are being checked in the same blood draw.",
                },
                {
                    "question": "What do doctors compare with a metabolic panel?",
                    "answer": "Common comparisons include HbA1c for glucose context, creatinine and eGFR for kidney function, sodium and potassium for fluid balance, and ALT/AST, ALP, albumin, or total protein for liver and protein patterns.",
                },
            ]
        },
    )
