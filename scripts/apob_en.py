#!/usr/bin/env python3
"""ApoB makalesi - English veritabanina ekle"""
import sqlite3, json
from datetime import datetime

DB = "/Users/ufukurhan/norya/norya.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def s(i,h,b,l=2):
    return {"id":i,"level":l,"heading":h,"body_html":b}

TS='class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"'
TH='style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
TD='style="border:1px solid #cbd5e1;padding:8px 12px;"'
def tbl(hs,rows):
    h="<thead><tr>"+"".join(f'<th {TH}>{x}</th>' for x in hs)+"</tr></thead>"
    b="<tbody>"+"".join("<tr>"+"".join(f'<td {TD}>{x}</td>' for x in r)+"</tr>" for r in rows)+"</tbody>"
    return f'<table {TS}>{h}{b}</table>'

DIS="<p><em>This content is educational and does not substitute for professional medical advice. Discuss your results with a qualified healthcare provider.</em></p>"

secs = [
    s("intro","What Is ApoB and Why Does It Matter?",
        "<p><strong>Apolipoprotein B (ApoB)</strong> is a structural protein found on the surface of every atherogenic lipoprotein particle in your bloodstream — including LDL (low-density lipoprotein), VLDL (very-low-density lipoprotein), IDL (intermediate-density lipoprotein), and Lp(a) (lipoprotein(a)). Because each atherogenic particle carries <strong>exactly one ApoB molecule</strong>, measuring ApoB in your blood provides a direct count of the total number of particles capable of depositing cholesterol in your artery walls and causing atherosclerosis.</p>"
        "<p>This is fundamentally different from the traditional lipid panel measurement of LDL cholesterol (LDL-C). LDL-C measures the cholesterol <em>content</em> within LDL particles, but two people with identical LDL-C values can have very different numbers of LDL particles. The person with more particles (higher ApoB) is at greater cardiovascular risk, even if their LDL-C appears normal.</p>"
        "<p>Large clinical studies consistently show that ApoB is a <strong>superior predictor of cardiovascular events</strong> compared to LDL-C and non-HDL-C. Major cardiology organizations have begun incorporating ApoB into clinical guidelines as a preferred risk marker, particularly in patients with metabolic syndrome, diabetes, or discordant LDL-C/ApoB patterns. Understanding your ApoB level is a critical step in accurate cardiovascular risk assessment and personalized prevention.</p>"),
    s("what-is-apob","Understanding ApoB: The Science Behind the Particle Count",
        "<p>Cholesterol cannot dissolve in blood — it must be transported inside lipoprotein particles. ApoB is the primary structural protein of the atherogenic particles, forming the scaffold that holds the particle together. There are two forms:</p>"
        "<ul>"
        "<li><strong>ApoB-100</strong> — produced by the liver, found on LDL, VLDL, IDL, and Lp(a). This is the form measured in the standard ApoB blood test.</li>"
        "<li><strong>ApoB-48</strong> — produced by the intestine, found on chylomicrons. Not measured in the standard test.</li>"
        "</ul>"
        "<p>Because each atherogenic particle contains exactly one ApoB-100 molecule, the ApoB blood test acts as a <strong>particle counter</strong>. In insulin-resistant states (obesity, metabolic syndrome, type 2 diabetes), the liver overproduces many small, cholesterol-poor LDL particles. These patients often have normal LDL-C but elevated ApoB — a dangerous combination frequently missed by standard lipid screening. This phenomenon, called <strong>discordance</strong>, affects approximately 25-30% of the population and is particularly common in people with metabolic syndrome.</p>"),
    s("normal-ranges","ApoB Reference Ranges and Target Levels",
        tbl(["Risk Category","ApoB Level (mg/dL)","Clinical Interpretation"],
        [("Optimal","< 65","Recommended for very high-risk patients"),
         ("Near optimal","65-79","Goal for high-risk patients"),
         ("Borderline","80-99","Approaching elevated risk"),
         ("Elevated","100-129","Increased cardiovascular risk"),
         ("High","130-159","Substantially increased risk"),
         ("Very high","\u2265 160","Urgent clinical evaluation recommended")]),
        "<p><strong>Key treatment target:</strong> For patients with established cardiovascular disease, diabetes with target organ damage, or familial hypercholesterolemia, the European Atherosclerosis Society recommends ApoB <strong>&lt; 65 mg/dL</strong> (corresponding roughly to LDL-C &lt; 55 mg/dL). For high-risk patients without established disease, the target is <strong>&lt; 80 mg/dL</strong>. For moderate-risk individuals, <strong>&lt; 100 mg/dL</strong> is generally recommended.</p>"
        "<p>Reference ranges may vary slightly between laboratories and testing methods. Always interpret results in the context of your overall cardiovascular risk profile, including age, sex, family history, blood pressure, glucose control, and other lipid markers. If your ApoB is elevated, your physician can recommend a personalized treatment plan based on your individual risk level.</p>"),
    s("high-apob","What Causes Elevated ApoB Levels?",
        "<p>Elevated ApoB can result from multiple factors, often acting in combination:</p>"
        "<ul>"
        "<li><strong>Genetic factors</strong> — Familial hypercholesterolemia (FH) affects approximately 1 in 250 people and causes markedly elevated ApoB from birth. Familial combined hyperlipidemia (FCHL) affects about 1 in 200 and is the most common inherited cause of high ApoB.</li>"
        "<li><strong>Insulin resistance and metabolic syndrome</strong> — These conditions drive the liver to overproduce VLDL particles, raising ApoB even with normal LDL cholesterol.</li>"
        "<li><strong>Unhealthy diet</strong> — High intake of saturated fats (palmitic and myristic acids from red meat, butter, full-fat dairy) and industrial trans fats increase ApoB production and impair clearance.</li>"
        "<li><strong>Obesity</strong> — Visceral adipose tissue increases free fatty acid delivery to the liver, stimulating VLDL overproduction. A 5-10% weight reduction can lower ApoB by 10-15%.</li>"
        "<li><strong>Hypothyroidism</strong> — Thyroid hormone regulates LDL receptor expression; low thyroid function reduces LDL receptor activity, slowing ApoB particle clearance from blood.</li>"
        "<li><strong>Chronic kidney disease</strong> — Impaired kidney function alters lipoprotein metabolism and reduces clearance of atherogenic particles by up to 50%.</li>"
        "<li><strong>Physical inactivity</strong> — Sedentary lifestyle reduces lipoprotein lipase activity and impairs triglyceride clearance, elevated