#!/usr/bin/env python3
"""ApoB makalesini 9 dilde veritabanına ekler.
Kullanim: python scripts/apob_insert.py
"""
import sqlite3, json
from datetime import datetime, timezone

DB = "/Users/ufukurhan/norya/norya.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def sec(i, h, b, l=2):
    return {"id":i, "level":l, "heading":h, "body_html":b}

TS = 'class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"'
THL = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
THR = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;"'
TD = 'style="border:1px solid #cbd5e1;padding:8px 12px;"'

def tbl(hs, rows, rtl=False):
    th = THR if rtl else THL
    h = "<thead><tr>" + "".join(f"<th {th}>{x}</th>" for x in hs) + "</tr></thead>"
    b = "<tbody>" + "".join("<tr>" + "".join(f"<td {TD}>{x}</td>" for x in r) + "</tr>" for r in rows) + "</tbody>"
    return f'<table {TS}>{h}{b}</table>'

DISCLAIMER = "<p><em>Bu icerik bilgilendirme amacli olup tbbi tavsiye yerine gecmez. Sonuclarinizi hekiminizle gorusun.</em></p>"

COVER = "/static/images/blog/apob-cholesterol-hero.jpg"
AUTHOR = "Norya Editorial Team"

posts = []

# ========================== EN ========================================
en_sections = json.dumps([
    sec("intro","What Is ApoB and Why Does It Matter for Heart Health?",
        "<p><strong>Apolipoprotein B (ApoB)</strong> is a structural protein found on the surface of every atherogenic lipoprotein particle in your bloodstream — including LDL (low-density lipoprotein), VLDL (very-low-density lipoprotein), IDL (intermediate-density lipoprotein), and even Lp(a) (lipoprotein(a)). Because each of these particles carries <strong>exactly one ApoB molecule</strong>, measuring the concentration of ApoB in your blood provides a direct estimate of the <strong>total number of atherogenic particles</strong> circulating in your bloodstream.</p>"
        "<p>This is fundamentally different from the traditional lipid panel measurement of LDL cholesterol (LDL-C). LDL-C measures the <em>amount of cholesterol</em> contained within LDL particles, but two people with identical LDL-C values can have very different numbers of LDL particles. The person with more particles (higher ApoB) is at greater cardiovascular risk, even though their LDL-C looks &quot;normal.&quot;</p>"
        "<p>Large observational studies show that ApoB is a <strong>superior predictor of cardiovascular events</strong> compared to LDL-C and non-HDL-C. Major cardiology guidelines have begun incorporating ApoB as a preferred risk marker, particularly in patients with metabolic syndrome, diabetes, or discordant LDL-C/ApoB patterns (&ldquo;discordance,&rdquo; affecting 25–30% of the population). Understanding your ApoB level is a critical step in accurate cardiovascular risk assessment and personalized prevention.</p>"),
    sec("what-is-apob","Understanding ApoB: The Science Behind the Particle Count",
        "<p>To understand why ApoB matters, consider how cholesterol is transported in the blood. Cholesterol is hydrophobic — it cannot dissolve in blood plasma. Instead, it is packaged into lipoprotein particles, each surrounded by a shell of phospholipids and proteins. ApoB is the primary structural protein of this shell for atherogenic particles.</p>"
        "<p>There are two main forms of ApoB:</p>"
        "<ul>"
        "<li><strong>ApoB-100</strong> — synthesized by the liver, found on LDL, VLDL, IDL, and Lp(a) particles. This is the form measured in the standard ApoB blood test.</li>"
        "<li><strong>ApoB-48</strong> — produced by the intestine, found on chylomicrons (dietary fat transport particles). Not included in the standard test.</li>"
        "</ul>"
        "<p>Because each atherogenic particle contains exactly one ApoB-100 molecule, the ApoB blood test effectively acts as a <strong>particle counter</strong>. This is more informative than measuring the cholesterol cargo inside particles, which can vary dramatically between individuals. For example, in insulin-resistant states (obesity, metabolic syndrome, type 2 diabetes), the liver produces many small, cholesterol-poor LDL particles. These patients have normal LDL-C but elevated ApoB — a dangerous combination often missed by standard lipid panels.</p>"
        "<p>Current evidence-based guidelines from the Canadian Cardiology Society, the European Atherosclerosis Society, and a growing number of American lipidologists now recommend ApoB as the <strong>preferred primary lipid marker for cardiovascular risk assessment</strong>.</p>"),
    sec("normal-ranges","ApoB Reference Ranges and Target Levels",
        tbl(["Category","ApoB Level","Interpretation"],
        [("Optimal","&lt; 65 mg/dL","Recommended for very high-risk patients"),
         ("Near optimal","65–79 mg/dL","Goal for high-risk patients"),
         ("Borderline","80–99 mg/dL","Approaching elevated risk"),
         ("Elevated","100–129 mg/dL","Increased cardiovascular risk"),
         ("High","130–159 mg/dL","Substantially increased risk"),
         ("Very high","\u2265 160 mg/dL","Urgent clinical evaluation recommended")],
        rtl=False),
        "<p><strong>Key target:</strong> For patients with established cardiovascular disease, diabetes with target organ damage, or familial hypercholesterolemia, the European Atherosclerosis Society recommends ApoB <strong>&lt; 65 mg/dL</strong> (corresponding roughly to LDL-C &lt; 55 mg/dL). For high-risk patients without established disease, the target is <strong>&lt; 80 mg/dL</strong>.</p>"
        "<p>Reference ranges may vary slightly between laboratories and testing methods. Always interpret your results in the context of your overall cardiovascular risk profile, age, sex, family history, blood pressure, glucose control, and other lipid markers. If your ApoB is elevated, discuss a personalized treatment plan with your physician.</p>"),
    sec("high-apob","What Causes Elevated ApoB Levels?",
        "<p>Elevated ApoB (hyperapobipoproteinemia) can result from multiple factors, often acting in combination:</p>"
        "<ul>"
        "<li><strong>Genetic factors</strong> — Familial hypercholesterolemia (FH) and familial combined hyperlipidemia (FCHL) are inherited conditions that cause significantly elevated ApoB. FCHL is the most common inherited lipid disorder, affecting approximately 1 in 200 people.</li>"
        "<li><strong>Insulin resistance and metabolic syndrome</strong> — These conditions drive the liver to overproduce VLDL particles, which are converted to small, dense LDL particles with high ApoB counts but relatively normal cholesterol content.</li>"
        "<li><strong>Dietary factors</strong> — High intake of saturated fatty acids (particularly palmitic and myristic acids found in red meat, butter, and full-fat dairy) and trans fatty acids increases ApoB production and impairs particle clearance.</li>"
        "<li><strong>Obesity</strong> — Visceral adipose tissue increases free fatty acid flux to the liver, stimulating VLDL overproduction and raising ApoB levels.</li>"
        "<li><strong>Hypothyroidism</strong> — Thyroid hormone regulates LDL receptor expression. Low thyroid function reduces LDL receptor activity, slowing particle clearance from blood.</li>"
        "<li><strong>Chronic kidney disease</strong> — Impaired kidney function alters lipoprotein metabolism and reduces clearance of atherogenic particles.</li>"
        "<li><strong>Physical inactivity</strong> — Sedentary behavior reduces LPL (lipoprotein lipase) activity, impairing triglyceride clearance and elevating ApoB.</li>"
        "<li><strong>Age</strong> — ApoB levels tend to increase with age, particularly after menopause in women, due to hormonal changes affecting lipid metabolism.</li>"
        "</ul>"),
    sec("cardiovascular-risk","Why ApoB Matters More Than LDL Cholesterol",
        "<p>The concept of <strong>discordance</strong> explains why ApoB provides superior risk prediction. Discordance occurs when LDL-C and ApoB give different risk signals. Studies show that in approximately 25% of patients, ApoB is higher than expected for a given LDL-C level — meaning their true risk is underestimated by LDL-C.</p>"
        "<p>When ApoB and LDL-C are discordant, <strong>ApoB consistently outperforms LDL-C</strong> as a predictor of cardiovascular events, including heart attack, stroke, and cardiovascular mortality. This finding has been replicated in large cohorts including the AMORIS study (776,000 patients), the INTERHEART study, and the Framingham Offspring Study.</p>"
        "<p>High ApoB is also associated with increased risk of <strong>aortic valve stenosis</strong>, <strong>peripheral artery disease</strong>, and may predict <strong>vascular dementia</strong>. Emerging evidence also links elevated ApoB to certain cancers through inflammatory pathways.</p>"
        "<p>Because ApoB can be elevated even when traditional cholesterol levels appear normal, it identifies at-risk patients who would otherwise be missed by standard screening. This is particularly important in younger individuals and those with metabolic syndrome.</p>"),
    sec("treatment","Evidence-Based Strategies to Lower ApoB",
        "<p>Lowering ApoB reduces cardiovascular event rates in a dose-dependent manner. The following strategies are supported by clinical evidence:</p>"
        "<h3 style=\"font-size:1.1rem;margin:1.5rem 0 0.75rem;font-weight:600;\">Pharmacological interventions</h3>"
        "<ul>"
        "<li><strong>High-intensity statins</strong> (atorvastatin 40–80 mg, rosuvastatin 20–40 mg) — First-line therapy, reduce ApoB by 35–50%. Statins lower ApoB by upregulating hepatic LDL receptors, which clear ApoB-carrying particles from circulation.</li>"
        "<li><strong>Ezetimibe</strong> (10 mg daily) — Added to statins when targets are not met, provides additional 15–20% ApoB reduction by blocking intestinal cholesterol absorption.</li>"
        "<li><strong>PCSK9 inhibitors</strong> (evolocumab, alirocumab; subcutaneous injection every 2–4 weeks) — Can reduce ApoB by an additional 50–60% on top of statin therapy. Reserved for very high-risk patients, including those with established cardiovascular disease, familial hypercholesterolemia, or statin intolerance.</li>"
        "<li><strong>Bempedoic acid</strong> — A newer oral agent that inhibits ACL (ATP citrate lyase); reduces ApoB by approximately 15%. Useful for statin-intolerant patients.</li>"
        "<li><strong>Inclisiran</strong> — A siRNA therapy administered twice yearly that silences the PCSK9 gene; reduces ApoB by approximately 50%.</li>"
        "</ul>"
        "<h3 style=\"font-size:1.1rem;margin:1.5rem 0 0.75rem;font-weight:600;\">Lifestyle modifications</h3>"
        "<ul>"
        "<li><strong>Dietary changes</strong> — Replace saturated fats with unsaturated fats (olive oil, nuts, fatty fish). Increase soluble fiber intake (oats, psyllium, legumes, fruit) by 5–10 g/day to bind bile acids and increase ApoB clearance. Plant sterols/stanols (2 g/day) block intestinal cholesterol absorption.</li>"
        "<li><strong>Regular exercise</strong> — At least 150 minutes/week of moderate aerobic activity or 75 minutes/week of vigorous activity. Exercise upregulates LPL and improves lipoprotein profile.</li>"
        "<li><strong>Weight management</strong> — A 5–10% reduction in body weight can reduce ApoB by 10–15%, primarily through reduced visceral fat and improved insulin sensitivity.</li>"
        "<li><strong>Smoking cessation</strong> — Smoking oxidizes LDL particles, making them more atherogenic. Quitting improves the entire lipoprotein profile.</li>"
        "</ul>"),
    sec("when-to-test","Who Should Be Tested for ApoB?",
        "<p>We recommend discussing ApoB testing with your healthcare provider in the following situations:</p>"
        "<ul>"
        "<li>Routine cardiovascular risk assessment (as an alternative or complement to non-HDL-C)</li>"
        "<li>Family history of premature cardiovascular disease (men &lt; 55 years, women &lt; 65 years at first event)</li>"
        "<li>Personal history of heart attack, stroke, or peripheral artery disease</li>"
        "<li>Metabolic syndrome or type 2 diabetes</li>"
        "<li>Known or suspected familial hypercholesterolemia</li>"
        "<li>Discordant lipid profile (normal LDL-C but elevated triglycerides or low HDL-C)</li>"
        "<li>Monitoring response to lipid-lowering therapy</li>"
        "<li>Chronic kidney disease stages 3–5</li>"
        "<li>Autoimmune or inflammatory conditions associated with increased cardiovascular risk</li>"
        "</ul>"
        "<p><strong>How Norya can help:</strong> Upload your blood test results to Norya and our AI-powered engine will analyze your full lipid panel, including ApoB and related biomarkers. You'll receive personalized insights, risk interpretation, and evidence-based recommendations — all in your preferred language.</p>"
        f'<div style="background:#f0fdfa;border:1px solid #99f6e4;border-radius:12px;padding:1.25rem;margin-top:1rem;">'
        f'<p style="margin:0;"><strong>Quick tip:</strong> ApoB testing is typically included in advanced lipid panels or can be ordered as a standalone test. It does not require fasting. Ask your doctor to include ApoB in your next blood work.</p></div>'
        f"<p>{DISCLAIMER}</p>")
])

posts.append(("en","en-apob-cholesterol-meaning","ApoB Explained: What Your Apolipoprotein B Blood Test Results Mean","ApoB Blood Test Explained — How to Interpret Your Results | Norya","Comprehensive guide to apolipoprotein B: what it measures, optimal ranges, causes of elevation, evidence-based treatment strategies, and why ApoB is superior to LDL cholesterol for cardiovascular risk prediction.",COVERAGE_NOTE,8))
