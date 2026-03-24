# -*- coding: utf-8 -*-
"""
Magnesium blog article — full body content for all 9 languages.
Used by blog_i18n._article_magnesium().
Sections: intro, what-is-magnesium, role-in-body, normal-ranges,
low-magnesium-causes, high-magnesium-causes, symptoms, dietary-sources,
when-to-see-doctor, how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# ENGLISH
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Magnesium blood test: what low or high levels mean",
            body_html=(
                "<p><strong>Magnesium</strong> is the fourth most abundant mineral in the body and an essential cofactor in more than "
                "<strong>300 enzymatic reactions</strong>. It plays critical roles in energy production, protein synthesis, muscle and nerve "
                "function, blood glucose regulation, and blood pressure control. Despite its importance, magnesium deficiency is remarkably "
                "common&mdash;studies suggest that up to 50% of people in Western countries have inadequate magnesium intake.</p>"
                "<p>A serum magnesium test measures the concentration of magnesium in your blood. However, because only about <strong>1% of "
                "total body magnesium</strong> is in the blood (the rest is in bones, muscles, and soft tissues), serum levels can appear "
                "normal even when body stores are significantly depleted. This makes clinical context and symptom recognition essential when "
                "interpreting results.</p>"
                "<p>This guide explains what magnesium does, how to interpret your levels, causes and symptoms of deficiency and excess, "
                "and dietary strategies to optimize your magnesium status. It is educational and does not replace medical advice.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="What is magnesium?",
            body_html=(
                "<p>Magnesium (Mg<sup>2+</sup>) is a divalent cation and the second most abundant intracellular cation after potassium. "
                "The adult body contains approximately 25 grams of magnesium, distributed as follows: about <strong>60% in bone</strong> "
                "(serving as a reservoir), <strong>20% in skeletal muscle</strong>, <strong>19% in other soft tissues</strong>, and only "
                "<strong>1% in extracellular fluids</strong> including blood.</p>"
                "<p>Dietary magnesium is absorbed primarily in the small intestine via both passive paracellular transport (when dietary "
                "intake is high) and active transcellular transport mediated by the <strong>TRPM6</strong> channel (when intake is low). "
                "Absorption efficiency ranges from 30&ndash;50% and is influenced by the form of magnesium, other dietary components, "
                "and gut health.</p>"
                "<p>The kidneys are the primary regulators of magnesium balance. They filter about 2,400 mg of magnesium per day but "
                "reabsorb 95&ndash;99% of it, primarily in the thick ascending limb of the loop of Henle and the distal convoluted tubule. "
                "When serum levels drop, renal reabsorption increases; when levels are high, excess is excreted in urine. Hormones such "
                "as PTH, aldosterone, and insulin also modulate renal magnesium handling.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="The role of magnesium in the body",
            body_html=(
                "<p>Magnesium's involvement in over 300 enzyme systems makes it one of the most versatile minerals in human physiology:</p>"
                "<ul>"
                "<li><strong>Energy production</strong> &ndash; magnesium is required for ATP (adenosine triphosphate) to be biologically active. "
                "ATP must be bound to magnesium to function, making Mg essential for every energy-dependent process in the body.</li>"
                "<li><strong>Muscle function</strong> &ndash; magnesium acts as a natural calcium channel blocker in muscle cells. It promotes "
                "muscle relaxation by counteracting calcium's role in muscle contraction. Deficiency can lead to cramps, spasms, and tremors.</li>"
                "<li><strong>Nerve function</strong> &ndash; magnesium regulates neurotransmitter release and acts as a gatekeeper for the "
                "NMDA receptor, modulating excitatory signaling. Low magnesium can increase neuronal excitability, contributing to anxiety, "
                "irritability, and seizures in severe cases.</li>"
                "<li><strong>Heart rhythm</strong> &ndash; magnesium stabilizes cardiac cell membranes and is critical for normal heart rhythm. "
                "Deficiency is a recognized cause of cardiac arrhythmias, including torsades de pointes. For related markers, see our guides on "
                '<a href="/blog/calcium-blood-test-meaning">calcium</a> and <a href="/blog/potassium-blood-test-meaning">potassium</a>.</li>'
                "<li><strong>Bone health</strong> &ndash; about 60% of body magnesium resides in bone. Magnesium influences both bone mineral "
                "density and calcium metabolism; deficiency is associated with increased osteoporosis risk.</li>"
                "<li><strong>Blood sugar regulation</strong> &ndash; magnesium plays a role in insulin signaling. Low magnesium is linked to "
                "insulin resistance and type 2 diabetes.</li>"
                "<li><strong>Blood pressure</strong> &ndash; magnesium promotes vasodilation. Meta-analyses show that magnesium supplementation "
                "modestly reduces blood pressure.</li>"
                "</ul>"
                "<p>Given these wide-ranging roles, even mild magnesium deficiency can have significant health consequences across multiple "
                "organ systems.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal magnesium ranges",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marker</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serum magnesium (adults)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2 mg/dL (0.70 &ndash; 0.91 mmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hypomagnesemia (low)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1.7 mg/dL (&lt; 0.70 mmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hypermagnesemia (high)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 2.2 mg/dL (&gt; 0.91 mmol/L)</td></tr>'
                "</tbody></table>"
                "<p>It is important to understand that serum magnesium reflects only <strong>1% of total body magnesium</strong>. A patient can "
                "have significant intracellular magnesium depletion while serum levels remain within the normal range&mdash;a concept called "
                "<strong>&ldquo;chronic latent magnesium deficiency.&rdquo;</strong> Some experts argue that the optimal serum magnesium level "
                "is above 2.0&nbsp;mg/dL, and that the traditional lower limit of 1.7 may miss clinically significant deficiency.</p>"
                "<p>RBC (red blood cell) magnesium and 24-hour urine magnesium can provide additional information about magnesium status "
                "but are not routinely ordered. In clinical practice, the serum level combined with symptoms and risk factors guides management.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Causes of low magnesium (hypomagnesemia)",
            body_html=(
                "<p>Magnesium deficiency is far more common than excess. Causes can be grouped into reduced intake, increased losses, and redistribution:</p>"
                "<p><strong>Inadequate dietary intake:</strong></p>"
                "<ul>"
                "<li>Diets low in green leafy vegetables, nuts, seeds, legumes, and whole grains.</li>"
                "<li>Highly processed food diets&mdash;food processing removes up to 80% of magnesium from grains.</li>"
                "<li>Soil depletion has reduced the magnesium content of crops over recent decades.</li>"
                "</ul>"
                "<p><strong>Gastrointestinal losses and malabsorption:</strong></p>"
                "<ul>"
                "<li>Chronic diarrhea, celiac disease, Crohn's disease, and short bowel syndrome.</li>"
                "<li>Chronic alcoholism&mdash;alcohol increases renal magnesium excretion and often accompanies poor diet.</li>"
                "<li>Bariatric surgery, particularly gastric bypass, significantly reduces magnesium absorption.</li>"
                "</ul>"
                "<p><strong>Renal losses (increased urinary excretion):</strong></p>"
                "<ul>"
                "<li><strong>Medications</strong> &ndash; loop and thiazide diuretics, proton pump inhibitors (PPIs, when used long-term), "
                "aminoglycoside antibiotics, cisplatin, calcineurin inhibitors (cyclosporine, tacrolimus), and amphotericin B.</li>"
                "<li><strong>Diabetes</strong> &ndash; glycosuria causes osmotic diuresis with magnesium wasting.</li>"
                "<li><strong>Genetic disorders</strong> &ndash; Gitelman syndrome and Bartter syndrome involve renal magnesium wasting.</li>"
                "</ul>"
                "<p><strong>Other:</strong> Hungry bone syndrome after parathyroidectomy, acute pancreatitis, and refeeding syndrome.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Causes of high magnesium (hypermagnesemia)",
            body_html=(
                "<p>Hypermagnesemia is uncommon in people with normal kidney function because the kidneys efficiently excrete excess magnesium. "
                "When it does occur, causes include:</p>"
                "<ul>"
                "<li><strong>Kidney failure</strong> &ndash; the most common cause. When glomerular filtration rate (GFR) drops below "
                "30&nbsp;mL/min, the kidneys lose their ability to excrete magnesium adequately, and even normal dietary intake can lead to "
                "accumulation. Advanced chronic kidney disease and dialysis patients are at greatest risk.</li>"
                "<li><strong>Excessive supplementation</strong> &ndash; high-dose magnesium supplements, particularly in patients with impaired "
                "kidney function, can cause dangerously high levels. Magnesium-containing antacids and laxatives (magnesium hydroxide, "
                "magnesium citrate) are common culprits in the elderly.</li>"
                "<li><strong>Medications</strong> &ndash; magnesium-containing antacids, laxatives, and intravenous magnesium sulfate "
                "(used for eclampsia treatment and tocolysis) can cause hypermagnesemia.</li>"
                "<li><strong>Other</strong> &ndash; adrenal insufficiency, hypothyroidism, lithium therapy, and familial hypocalciuric "
                "hypercalcemia can mildly elevate magnesium.</li>"
                "</ul>"
                "<p>Mild hypermagnesemia (2.2&ndash;4.0&nbsp;mg/dL) is often asymptomatic. Severe hypermagnesemia (&gt;4.0&nbsp;mg/dL) is a "
                "medical emergency that can cause loss of deep tendon reflexes, respiratory depression, cardiac arrest, and death.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of magnesium deficiency and excess",
            body_html=(
                "<p><strong>Hypomagnesemia symptoms</strong> (low magnesium) affect multiple systems:</p>"
                "<ul>"
                "<li><strong>Neuromuscular</strong> &ndash; muscle cramps, spasms, twitching (fasciculations), tremor, and tetany. "
                "Trousseau sign and Chvostek sign may be positive (similar to hypocalcemia).</li>"
                "<li><strong>Cardiovascular</strong> &ndash; cardiac arrhythmias (premature beats, atrial fibrillation, ventricular tachycardia, "
                "torsades de pointes), hypertension, and coronary artery spasm.</li>"
                "<li><strong>Neuropsychiatric</strong> &ndash; fatigue, weakness, irritability, anxiety, depression, insomnia, and in severe "
                "cases, seizures and altered consciousness.</li>"
                "<li><strong>Metabolic</strong> &ndash; hypomagnesemia frequently causes <strong>refractory hypokalemia</strong> (low potassium "
                "that does not respond to potassium supplementation until magnesium is corrected) and <strong>hypocalcemia</strong> (by impairing "
                "PTH secretion and action).</li>"
                "</ul>"
                "<p><strong>Hypermagnesemia symptoms</strong> (high magnesium) progress with rising levels:</p>"
                "<ul>"
                "<li>Mild (2.2&ndash;4.0 mg/dL): nausea, flushing, headache.</li>"
                "<li>Moderate (4.0&ndash;7.0 mg/dL): loss of deep tendon reflexes, drowsiness, hypotension.</li>"
                "<li>Severe (&gt;7.0 mg/dL): respiratory depression, complete heart block, cardiac arrest.</li>"
                "</ul>"
                "<p>The association of magnesium deficiency with refractory hypokalemia and hypocalcemia is clinically critical&mdash;if a "
                "patient's potassium or calcium won't normalize despite supplementation, always check magnesium.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Dietary sources of magnesium",
            body_html=(
                "<p>The recommended daily intake of magnesium is <strong>400&ndash;420&nbsp;mg for adult men</strong> and "
                "<strong>310&ndash;320&nbsp;mg for adult women</strong>. Excellent food sources include:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Food</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Serving size</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Magnesium (mg)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Pumpkin seeds</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">28 g (1 oz)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">156</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Almonds</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">28 g (1 oz)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">80</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Spinach (cooked)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">½ cup</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">78</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Dark chocolate (70%+)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">28 g (1 oz)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">65</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Black beans (cooked)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">½ cup</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">60</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Avocado</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1 medium</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">58</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Brown rice (cooked)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">½ cup</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">42</td></tr>'
                "</tbody></table>"
                "<p>Other good sources include cashews, peanuts, edamame, bananas, salmon, and yogurt. Mineral water can also contribute "
                "meaningfully to magnesium intake. When dietary intake is insufficient, supplementation with magnesium citrate, glycinate, "
                "or taurate is generally well absorbed. Magnesium oxide is commonly sold but has lower bioavailability.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult your doctor about your magnesium levels in the following situations:</p>"
                "<ul>"
                "<li>Your serum magnesium is <strong>below 1.7&nbsp;mg/dL</strong> or you have symptoms suggestive of deficiency: persistent "
                "muscle cramps, tremors, fatigue, or heart palpitations.</li>"
                "<li>You have <strong>refractory hypokalemia or hypocalcemia</strong>&mdash;low potassium or calcium that doesn't respond to "
                "supplementation, which may indicate underlying magnesium depletion.</li>"
                "<li>You are taking medications that deplete magnesium: <strong>diuretics, PPIs, or aminoglycosides</strong>.</li>"
                "<li>You have <strong>chronic kidney disease</strong>&mdash;both deficiency and excess can occur depending on the stage.</li>"
                "<li>You have <strong>cardiac arrhythmias</strong>, especially if unexplained or associated with electrolyte abnormalities.</li>"
                "<li>You are experiencing <strong>severe symptoms of hypermagnesemia</strong>: loss of reflexes, extreme drowsiness, "
                "difficulty breathing&mdash;this is a medical emergency.</li>"
                "</ul>"
                "<p>Magnesium is often overlooked in routine blood panels. If you have risk factors for deficiency, request that your doctor "
                "include magnesium in your next blood work.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your magnesium results",
            body_html=(
                "<p>Understanding your magnesium result in the context of calcium, potassium, and other electrolytes is important for seeing the "
                "full picture. <strong>Norya</strong> makes this easy: upload your blood test results and receive a structured, easy-to-understand "
                "health summary within minutes. Norya evaluates your magnesium alongside related markers to identify potential deficiencies "
                "and electrolyte imbalances.</p>"
                "<p>The report highlights abnormal values, explains what they mean in plain language, and prepares you for a productive "
                "conversation with your doctor. <a href=\"/analyze\">Start your free analysis with Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace medical advice or diagnosis.</strong> '
                'Always discuss your results with a healthcare professional. <a href="/analyze">Start analysis with Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# TURKISH
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Magnezyum kan testi: düşük veya yüksek düzeyler ne anlama gelir?",
            body_html=(
                "<p><strong>Magnezyum</strong>, vücuttaki dördüncü en bol mineral ve <strong>300'den fazla enzimatik reaksiyonda</strong> "
                "temel bir kofaktördür. Enerji üretimi, protein sentezi, kas ve sinir fonksiyonu, kan şekeri düzenlemesi ve kan basıncı "
                "kontrolünde kritik roller oynar. Önemine rağmen magnezyum eksikliği oldukça yaygındır&mdash;araştırmalar Batı ülkelerindeki "
                "insanların %50'ye kadarının yetersiz magnezyum alımına sahip olduğunu göstermektedir.</p>"
                "<p>Serum magnezyum testi kanınızdaki magnezyum konsantrasyonunu ölçer. Ancak <strong>toplam vücut magnezyumunun yalnızca %1'i</strong> "
                "kanda olduğundan (geri kalanı kemikler, kaslar ve yumuşak dokulardadır), vücut depoları önemli ölçüde tükenmiş olsa bile serum "
                "düzeyleri normal görünebilir.</p>"
                "<p>Bu rehber magnezyumun ne yaptığını, düzeylerinizi nasıl yorumlayacağınızı, eksiklik ve fazlalık nedenlerini ve diyet "
                "stratejilerini açıklar. Eğitim amaçlıdır, tıbbi tavsiye yerine geçmez.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="Magnezyum nedir?",
            body_html=(
                "<p>Magnezyum (Mg<sup>2+</sup>) iki değerlikli bir katyon ve potasyumdan sonra en bol hücre içi katyondur. Yetişkin vücudunda "
                "yaklaşık 25 gram magnezyum bulunur: <strong>%60 kemikte</strong>, <strong>%20 iskelet kasında</strong>, <strong>%19 diğer "
                "yumuşak dokularda</strong> ve yalnızca <strong>%1 kan dahil hücre dışı sıvılarda</strong>.</p>"
                "<p>Besinlerden alınan magnezyum ağırlıklı olarak ince bağırsakta emilir. Emilim verimliliği %30&ndash;50 arasındadır. "
                "Böbrekler günde yaklaşık 2.400 mg magnezyumu filtreler ancak %95&ndash;99'unu geri emer.</p>"
                "<p>PTH, aldosteron ve insülin gibi hormonlar renal magnezyum işlemesini modüle eder.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="Magnezyumun vücuttaki rolü",
            body_html=(
                "<p>Magnezyumun 300'den fazla enzim sistemine katılması onu insan fizyolojisindeki en çok yönlü minerallerden biri yapar:</p>"
                "<ul>"
                "<li><strong>Enerji üretimi</strong> &ndash; ATP'nin biyolojik olarak aktif olması için magnezyum gereklidir.</li>"
                "<li><strong>Kas fonksiyonu</strong> &ndash; magnezyum doğal bir kalsiyum kanal blokeri olarak kas gevşemesini destekler. Eksiklik kramplara, spazmolara ve tremorona yol açabilir.</li>"
                "<li><strong>Sinir fonksiyonu</strong> &ndash; nörotransmitter salınımını düzenler ve NMDA reseptörünün kapı bekçisi olarak görev yapar.</li>"
                "<li><strong>Kalp ritmi</strong> &ndash; kardiyak hücre zarlarını stabilize eder; eksiklik aritmilere neden olabilir. "
                "İlgili belirteçler için <a href=\"/blog/calcium-blood-test-meaning\">kalsiyum</a> ve "
                "<a href=\"/blog/potassium-blood-test-meaning\">potasyum</a> rehberlerimize bakın.</li>"
                "<li><strong>Kemik sağlığı</strong> &ndash; vücut magnezyumunun %60'ı kemikte bulunur.</li>"
                "<li><strong>Kan şekeri düzenlemesi</strong> &ndash; insülin sinyal yolunda rol oynar; düşük magnezyum insülin direnciyle ilişkilidir.</li>"
                "<li><strong>Kan basıncı</strong> &ndash; vazodilatasyonu destekler.</li>"
                "</ul>"
                "<p>Bu geniş kapsamlı roller göz önüne alındığında, hafif magnezyum eksikliği bile birden fazla organ sisteminde önemli sağlık sonuçlarına yol açabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal magnezyum aralıkları",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Belirteç</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serum magnezyum (yetişkin)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2 mg/dL (0,70 &ndash; 0,91 mmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hipomagnezemi (düşük)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1,7 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hipermagnezemi (yüksek)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 2,2 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Serum magnezyumunun toplam vücut magnezyumunun yalnızca <strong>%1'ini</strong> yansıttığını anlamak önemlidir. "
                "Serum düzeyleri normal aralıkta olsa bile hücre içi magnezyum tükenmesi olabilir&mdash;<strong>&ldquo;kronik latent magnezyum "
                "eksikliği&rdquo;</strong> olarak adlandırılan bir kavram.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Düşük magnezyum (hipomagnezemi) nedenleri",
            body_html=(
                "<p>Magnezyum eksikliği fazlalıktan çok daha yaygındır:</p>"
                "<p><strong>Yetersiz diyet alımı:</strong> yeşil yapraklı sebzeler, kuruyemişler, tohumlar, baklagiller ve tam tahıllardan "
                "fakir diyetler. İşlenmiş gıda diyetleri&mdash;gıda işleme tahıllardan magnezyumun %80'ine kadarını uzaklaştırır.</p>"
                "<p><strong>Gastrointestinal kayıplar:</strong> kronik ishal, çölyak hastalığı, Crohn hastalığı, alkolizm ve bariyatrik cerrahi.</p>"
                "<p><strong>Renal kayıplar:</strong></p>"
                "<ul>"
                "<li><strong>İlaçlar</strong> &ndash; loop ve tiazid diüretikler, proton pompa inhibitörleri (PPI, uzun süreli kullanımda), "
                "aminoglikozid antibiyotikler, sisplatin.</li>"
                "<li><strong>Diyabet</strong> &ndash; glikozüri ozmotik diüreze neden olarak magnezyum kaybına yol açar.</li>"
                "<li><strong>Genetik bozukluklar</strong> &ndash; Gitelman sendromu ve Bartter sendromu.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Yüksek magnezyum (hipermagnezemi) nedenleri",
            body_html=(
                "<p>Hipermagnezemi normal böbrek fonksiyonu olan kişilerde nadirdir:</p>"
                "<ul>"
                "<li><strong>Böbrek yetmezliği</strong> &ndash; en yaygın neden. GFR 30&nbsp;mL/dk'nın altına düştüğünde böbrekler magnezyumu yeterince atamaz.</li>"
                "<li><strong>Aşırı takviye</strong> &ndash; yüksek doz magnezyum takviyeleri, özellikle böbrek fonksiyon bozukluğu olan hastalarda. "
                "Magnezyum içeren antiasitler ve laksatifler yaşlılarda yaygın nedenlerdir.</li>"
                "<li><strong>İlaçlar</strong> &ndash; magnezyum içeren antiasitler, laksatifler ve intravenöz magnezyum sülfat.</li>"
                "<li><strong>Diğer</strong> &ndash; adrenal yetmezlik, hipotiroidizm, lityum tedavisi.</li>"
                "</ul>"
                "<p>Hafif hipermagnezemi genellikle asemptomatiktir. Ciddi hipermagnezemi (&gt;4,0&nbsp;mg/dL) derin tendon refleksi kaybı, "
                "solunum depresyonu, kardiyak arrest ve ölüme neden olabilen tıbbi bir acildir.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Magnezyum eksikliği ve fazlalığının belirtileri",
            body_html=(
                "<p><strong>Hipomagnezemi belirtileri:</strong></p>"
                "<ul>"
                "<li><strong>Nöromüsküler</strong> &ndash; kas krampları, spazmlar, seğirmeler, tremor ve tetani.</li>"
                "<li><strong>Kardiyovasküler</strong> &ndash; kardiyak aritmiler, hipertansiyon, koroner arter spazmı.</li>"
                "<li><strong>Nöropsikiyatrik</strong> &ndash; yorgunluk, halsizlik, sinirlilik, anksiyete, depresyon, uykusuzluk.</li>"
                "<li><strong>Metabolik</strong> &ndash; <strong>dirençli hipokalemi</strong> (magnezyum düzeltilene kadar potasyum takviyesine yanıt vermeyen düşük potasyum) "
                "ve <strong>hipokalsemi</strong>.</li>"
                "</ul>"
                "<p><strong>Hipermagnezemi belirtileri:</strong></p>"
                "<ul>"
                "<li>Hafif (2,2&ndash;4,0 mg/dL): bulantı, yüz kızarması, baş ağrısı.</li>"
                "<li>Orta (4,0&ndash;7,0 mg/dL): derin tendon refleksi kaybı, uyuşukluk, hipotansiyon.</li>"
                "<li>Ciddi (&gt;7,0 mg/dL): solunum depresyonu, tam kalp bloğu, kardiyak arrest.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Magnezyumun besin kaynakları",
            body_html=(
                "<p>Önerilen günlük magnezyum alımı yetişkin erkekler için <strong>400&ndash;420&nbsp;mg</strong>, yetişkin kadınlar için "
                "<strong>310&ndash;320&nbsp;mg</strong>'dır. Mükemmel besin kaynakları:</p>"
                "<ul>"
                "<li><strong>Kabak çekirdeği</strong> (28g: 156 mg), <strong>badem</strong> (28g: 80 mg), <strong>ıspanak (pişmiş)</strong> "
                "(½ bardak: 78 mg), <strong>bitter çikolata</strong> (28g: 65 mg), <strong>siyah fasulye</strong> (½ bardak: 60 mg), "
                "<strong>avokado</strong> (1 orta: 58 mg), <strong>esmer pirinç</strong> (½ bardak: 42 mg).</li>"
                "</ul>"
                "<p>Diğer iyi kaynaklar: kaju, yer fıstığı, edamame, muz, somon ve yoğurt. Diyet alımı yetersiz olduğunda magnezyum sitrat, "
                "glisin veya tauratla takviye genellikle iyi emilir. Magnezyum oksit yaygındır ancak daha düşük biyoyararlanıma sahiptir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda magnezyum düzeyleriniz hakkında doktorunuza danışın:</p>"
                "<ul>"
                "<li>Serum magnezyumunuz <strong>1,7&nbsp;mg/dL'nin altında</strong> veya eksiklik düşündüren belirtileriniz var.</li>"
                "<li><strong>Dirençli hipokalemi veya hipokalsemi</strong>&mdash;takviyeye yanıt vermeyen düşük potasyum veya kalsiyum.</li>"
                "<li>Magnezyum tüketen ilaçlar kullanıyorsunuz: <strong>diüretikler, PPI'ler veya aminoglikozidler</strong>.</li>"
                "<li><strong>Kronik böbrek hastalığınız</strong> var.</li>"
                "<li>Açıklanamayan <strong>kardiyak aritmileriniz</strong> var.</li>"
                "<li><strong>Ciddi hipermagnezemi belirtileri</strong> yaşıyorsanız&mdash;refleks kaybı, aşırı uyuşukluk, nefes güçlüğü&mdash;bu tıbbi bir acildir.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya magnezyum sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Magnezyum sonucunuzu kalsiyum, potasyum ve diğer elektrolitler bağlamında anlamak önemlidir. <strong>Norya</strong> bunu "
                "kolaylaştırır: kan testi sonuçlarınızı yükleyin ve dakikalar içinde yapılandırılmış bir sağlık özeti alın.</p>"
                "<p>Rapor anormal değerleri vurgular, anlaşılır dilde açıklar ve doktorunuzla verimli bir görüşmeye hazırlar. "
                "<a href=\"/analyze\">Norya ile ücretsiz analizinizi başlatın</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                'Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. <a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# SPANISH
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Análisis de magnesio: qué significan los niveles bajos o altos",
                body_html="<p>El <strong>magnesio</strong> es el cuarto mineral más abundante en el cuerpo y un cofactor esencial en más de <strong>300 reacciones enzimáticas</strong>. A pesar de su importancia, la deficiencia es notablemente común.</p><p>El test de magnesio sérico mide la concentración en sangre, pero solo el <strong>1% del magnesio total</strong> se encuentra en la sangre. Esta guía es educativa y no sustituye el consejo médico.</p>"),
        Section(id="what-is-magnesium", level=2, heading="¿Qué es el magnesio?",
                body_html="<p>El magnesio (Mg<sup>2+</sup>) es el segundo catión intracelular más abundante. El cuerpo adulto contiene unos 25 g: <strong>60% en hueso</strong>, <strong>20% en músculo</strong>, <strong>19% en tejidos blandos</strong> y <strong>1% en líquidos extracelulares</strong>.</p><p>La absorción intestinal oscila entre el 30&ndash;50%. Los riñones filtran unos 2.400 mg diarios pero reabsorben el 95&ndash;99%.</p>"),
        Section(id="role-in-body", level=2, heading="El papel del magnesio en el cuerpo",
                body_html="<p>El magnesio participa en más de 300 sistemas enzimáticos: producción de energía (ATP), función muscular (relajación), función nerviosa (regulación del receptor NMDA), ritmo cardíaco, salud ósea, regulación de glucemia y presión arterial. Para marcadores relacionados, consulte nuestras guías de <a href=\"/blog/calcium-blood-test-meaning\">calcio</a> y <a href=\"/blog/potassium-blood-test-meaning\">potasio</a>.</p>"),
        Section(id="normal-ranges", level=2, heading="Rangos normales de magnesio",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marcador</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Magnesio sérico</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2 mg/dL (0,70 &ndash; 0,91 mmol/L)</td></tr></tbody></table><p>El magnesio sérico refleja solo el <strong>1% del magnesio corporal total</strong>. Puede existir deficiencia intracelular significativa con niveles séricos normales.</p>'),
        Section(id="low-magnesium-causes", level=2, heading="Causas de magnesio bajo",
                body_html="<p><strong>Dieta inadecuada:</strong> pobre en vegetales verdes, frutos secos, semillas y cereales integrales. <strong>Pérdidas GI:</strong> diarrea crónica, celiaquía, alcoholismo, cirugía bariátrica. <strong>Pérdidas renales:</strong> diuréticos, IBP (uso prolongado), aminoglucósidos, diabetes (diuresis osmótica), síndromes de Gitelman/Bartter.</p>"),
        Section(id="high-magnesium-causes", level=2, heading="Causas de magnesio alto",
                body_html="<p><strong>Insuficiencia renal</strong> (causa más frecuente), <strong>suplementación excesiva</strong>, antiácidos y laxantes con magnesio, sulfato de magnesio IV. La hipermagnesemia grave (&gt;4,0 mg/dL) es una emergencia médica.</p>"),
        Section(id="symptoms", level=2, heading="Síntomas de deficiencia y exceso de magnesio",
                body_html="<p><strong>Hipomagnesemia:</strong> calambres, espasmos, temblor, arritmias, fatiga, irritabilidad, hipopotasemia refractaria e hipocalcemia. <strong>Hipermagnesemia:</strong> leve (náuseas), moderada (pérdida de reflejos), grave (depresión respiratoria, paro cardíaco).</p>"),
        Section(id="dietary-sources", level=2, heading="Fuentes alimentarias de magnesio",
                body_html="<p>Ingesta recomendada: hombres 400-420 mg/día, mujeres 310-320 mg/día. Fuentes: semillas de calabaza (156 mg/28g), almendras, espinacas, chocolate negro, frijoles negros, aguacate, arroz integral. Para suplementación: citrato, glicinato o taurato de magnesio tienen buena absorción.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Cuándo consultar al médico",
                body_html="<p>Consulte si: magnesio sérico &lt;1,7 mg/dL; hipopotasemia o hipocalcemia refractarias; toma de diuréticos/IBP; enfermedad renal crónica; arritmias cardíacas; o síntomas graves de hipermagnesemia.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo Norya le ayuda a entender sus resultados de magnesio",
                body_html="<p><strong>Norya</strong> simplifica la interpretación: suba sus resultados y reciba un resumen de salud claro en minutos. <a href=\"/analyze\">Inicie su análisis con Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Magnesium-Bluttest: Was niedrige oder hohe Werte bedeuten",
                body_html="<p><strong>Magnesium</strong> ist das vierthäufigste Mineral im Körper und ein essentieller Kofaktor in über <strong>300 enzymatischen Reaktionen</strong>. Magnesiummangel ist überraschend häufig. Dieser Leitfaden ist informativ und ersetzt keine ärztliche Beratung.</p>"),
        Section(id="what-is-magnesium", level=2, heading="Was ist Magnesium?",
                body_html="<p>Magnesium (Mg<sup>2+</sup>) ist das zweithäufigste intrazelluläre Kation. Der Körper enthält ca. 25 g: <strong>60% im Knochen</strong>, <strong>20% im Skelettmuskel</strong>, <strong>19% in Weichgewebe</strong> und nur <strong>1% in extrazellulären Flüssigkeiten</strong>.</p>"),
        Section(id="role-in-body", level=2, heading="Die Rolle von Magnesium im Körper",
                body_html="<p>Magnesium ist an über 300 Enzymsystemen beteiligt: Energieproduktion (ATP), Muskelfunktion, Nervenfunktion, Herzrhythmus, Knochengesundheit, Blutzuckerregulation und Blutdruck. Siehe auch unsere Leitfäden zu <a href=\"/blog/calcium-blood-test-meaning\">Kalzium</a> und <a href=\"/blog/potassium-blood-test-meaning\">Kalium</a>.</p>"),
        Section(id="normal-ranges", level=2, heading="Normale Magnesiumwerte",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marker</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serummagnesium</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2 mg/dL (0,70 &ndash; 0,91 mmol/L)</td></tr></tbody></table><p>Serummagnesium spiegelt nur <strong>1% des Gesamtkörpermagnesiums</strong> wider.</p>'),
        Section(id="low-magnesium-causes", level=2, heading="Ursachen von niedrigem Magnesium",
                body_html="<p><strong>Ernährung:</strong> arm an grünem Blattgemüse, Nüssen, Samen. <strong>GI-Verluste:</strong> Durchfall, Zöliakie, Alkoholismus, Adipositaschirurgie. <strong>Renale Verluste:</strong> Diuretika, PPI, Aminoglykoside, Diabetes, Gitelman-/Bartter-Syndrom.</p>"),
        Section(id="high-magnesium-causes", level=2, heading="Ursachen von hohem Magnesium",
                body_html="<p><strong>Nierenversagen</strong> (häufigste Ursache), <strong>übermäßige Supplementierung</strong>, magnesiumhaltige Antazida/Laxantien. Schwere Hypermagnesiämie (&gt;4,0 mg/dL) ist ein medizinischer Notfall.</p>"),
        Section(id="symptoms", level=2, heading="Symptome von Magnesiummangel und -überschuss",
                body_html="<p><strong>Hypomagnesiämie:</strong> Muskelkrämpfe, Tremor, Arrhythmien, Müdigkeit, refraktäre Hypokaliämie und Hypokalzämie. <strong>Hypermagnesiämie:</strong> leicht (Übelkeit), mäßig (Reflexverlust), schwer (Atemdepression, Herzstillstand).</p>"),
        Section(id="dietary-sources", level=2, heading="Nahrungsquellen für Magnesium",
                body_html="<p>Empfohlene Zufuhr: Männer 400-420 mg/Tag, Frauen 310-320 mg/Tag. Quellen: Kürbiskerne, Mandeln, Spinat, Zartbitterschokolade, schwarze Bohnen, Avocado, Naturreis.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann Sie einen Arzt aufsuchen sollten",
                body_html="<p>Konsultieren Sie Ihren Arzt bei: Serummagnesium &lt;1,7 mg/dL; refraktärer Hypokaliämie oder Hypokalzämie; Einnahme von Diuretika/PPI; chronischer Nierenerkrankung; Herzrhythmusstörungen; oder schweren Hypermagnesiämie-Symptomen.</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie Norya Ihnen hilft, Ihre Magnesium-Ergebnisse zu verstehen",
                body_html="<p><strong>Norya</strong> vereinfacht die Interpretation: Laden Sie Ihre Ergebnisse hoch und erhalten Sie einen klaren Gesundheitsbericht. <a href=\"/analyze\">Starten Sie Ihre Analyse mit Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Analyse du magnésium : que signifient des niveaux bas ou élevés ?",
                body_html="<p>Le <strong>magnésium</strong> est le quatrième minéral le plus abondant et un cofacteur dans plus de <strong>300 réactions enzymatiques</strong>. La carence est étonnamment fréquente. Ce guide est éducatif et ne remplace pas un avis médical.</p>"),
        Section(id="what-is-magnesium", level=2, heading="Qu'est-ce que le magnésium ?",
                body_html="<p>Le magnésium (Mg<sup>2+</sup>) est le deuxième cation intracellulaire. Le corps contient environ 25 g : <strong>60% dans l'os</strong>, <strong>20% dans le muscle</strong>, <strong>19% dans les tissus mous</strong> et <strong>1% dans les liquides extracellulaires</strong>.</p>"),
        Section(id="role-in-body", level=2, heading="Le rôle du magnésium dans le corps",
                body_html="<p>Le magnésium intervient dans plus de 300 systèmes enzymatiques : production d'énergie (ATP), fonction musculaire et nerveuse, rythme cardiaque, santé osseuse, glycémie et pression artérielle. Voir nos guides sur <a href=\"/blog/calcium-blood-test-meaning\">le calcium</a> et <a href=\"/blog/potassium-blood-test-meaning\">le potassium</a>.</p>"),
        Section(id="normal-ranges", level=2, heading="Valeurs normales de magnésium",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marqueur</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valeur normale</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Magnésium sérique</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2 mg/dL (0,70 &ndash; 0,91 mmol/L)</td></tr></tbody></table><p>Le magnésium sérique ne reflète que <strong>1% du magnésium corporel total</strong>.</p>'),
        Section(id="low-magnesium-causes", level=2, heading="Causes d'un magnésium bas",
                body_html="<p><strong>Apport insuffisant :</strong> régime pauvre en légumes verts, noix, graines. <strong>Pertes GI :</strong> diarrhée, maladie cœliaque, alcoolisme, chirurgie bariatrique. <strong>Pertes rénales :</strong> diurétiques, IPP, aminosides, diabète, syndromes de Gitelman/Bartter.</p>"),
        Section(id="high-magnesium-causes", level=2, heading="Causes d'un magnésium élevé",
                body_html="<p><strong>Insuffisance rénale</strong> (cause la plus fréquente), <strong>supplémentation excessive</strong>, antiacides et laxatifs contenant du magnésium. L'hypermagnésémie sévère (&gt;4,0 mg/dL) est une urgence médicale.</p>"),
        Section(id="symptoms", level=2, heading="Symptômes de carence et d'excès de magnésium",
                body_html="<p><strong>Hypomagnésémie :</strong> crampes, tremblements, arythmies, fatigue, hypokaliémie et hypocalcémie réfractaires. <strong>Hypermagnésémie :</strong> légère (nausées), modérée (perte de réflexes), sévère (dépression respiratoire, arrêt cardiaque).</p>"),
        Section(id="dietary-sources", level=2, heading="Sources alimentaires de magnésium",
                body_html="<p>Apport recommandé : hommes 400-420 mg/j, femmes 310-320 mg/j. Sources : graines de courge, amandes, épinards, chocolat noir, haricots noirs, avocat, riz complet. En supplémentation : citrate, glycinate ou taurate de magnésium sont bien absorbés.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter un médecin",
                body_html="<p>Consultez si : magnésium &lt;1,7 mg/dL ; hypokaliémie ou hypocalcémie réfractaires ; prise de diurétiques/IPP ; insuffisance rénale ; arythmies cardiaques ; ou symptômes graves d'hypermagnésémie.</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment Norya vous aide à comprendre vos résultats de magnésium",
                body_html="<p><strong>Norya</strong> simplifie l'interprétation : téléchargez vos résultats et recevez un rapport clair en minutes. <a href=\"/analyze\">Commencez votre analyse avec Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Analisi del magnesio: cosa significano livelli bassi o alti",
                body_html="<p>Il <strong>magnesio</strong> è il quarto minerale più abbondante e cofattore essenziale in oltre <strong>300 reazioni enzimatiche</strong>. La carenza è sorprendentemente comune. Questa guida è educativa e non sostituisce il parere medico.</p>"),
        Section(id="what-is-magnesium", level=2, heading="Cos'è il magnesio?",
                body_html="<p>Il magnesio (Mg<sup>2+</sup>) è il secondo catione intracellulare. Il corpo contiene circa 25 g: <strong>60% nelle ossa</strong>, <strong>20% nei muscoli</strong>, <strong>19% nei tessuti molli</strong> e <strong>1% nei liquidi extracellulari</strong>.</p>"),
        Section(id="role-in-body", level=2, heading="Il ruolo del magnesio nel corpo",
                body_html="<p>Il magnesio partecipa a oltre 300 sistemi enzimatici: produzione di energia (ATP), funzione muscolare e nervosa, ritmo cardiaco, salute ossea, glicemia e pressione arteriosa. Consultate le nostre guide su <a href=\"/blog/calcium-blood-test-meaning\">calcio</a> e <a href=\"/blog/potassium-blood-test-meaning\">potassio</a>.</p>"),
        Section(id="normal-ranges", level=2, heading="Valori normali del magnesio",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marcatore</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normale</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Magnesio sierico</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2 mg/dL (0,70 &ndash; 0,91 mmol/L)</td></tr></tbody></table><p>Il magnesio sierico riflette solo l\'<strong>1% del magnesio corporeo totale</strong>.</p>'),
        Section(id="low-magnesium-causes", level=2, heading="Cause del magnesio basso",
                body_html="<p><strong>Apporto inadeguato:</strong> dieta povera di verdure verdi, frutta secca, semi. <strong>Perdite GI:</strong> diarrea cronica, celiachia, alcolismo, chirurgia bariatrica. <strong>Perdite renali:</strong> diuretici, IPP, aminoglicosidi, diabete, sindromi di Gitelman/Bartter.</p>"),
        Section(id="high-magnesium-causes", level=2, heading="Cause del magnesio alto",
                body_html="<p><strong>Insufficienza renale</strong> (causa più comune), <strong>supplementazione eccessiva</strong>, antiacidi e lassativi con magnesio. L'ipermagnesemia grave (&gt;4,0 mg/dL) è un'emergenza medica.</p>"),
        Section(id="symptoms", level=2, heading="Sintomi di carenza ed eccesso di magnesio",
                body_html="<p><strong>Ipomagnesemia:</strong> crampi, tremori, aritmie, affaticamento, ipokaliemia e ipocalcemia refrattarie. <strong>Ipermagnesemia:</strong> lieve (nausea), moderata (perdita di riflessi), grave (depressione respiratoria, arresto cardiaco).</p>"),
        Section(id="dietary-sources", level=2, heading="Fonti alimentari di magnesio",
                body_html="<p>Apporto raccomandato: uomini 400-420 mg/die, donne 310-320 mg/die. Fonti: semi di zucca, mandorle, spinaci, cioccolato fondente, fagioli neri, avocado, riso integrale.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico",
                body_html="<p>Consultate il medico se: magnesio &lt;1,7 mg/dL; ipokaliemia o ipocalcemia refrattarie; assunzione di diuretici/IPP; nefropatia cronica; aritmie cardiache; o sintomi gravi di ipermagnesemia.</p>"),
        Section(id="how-norya-helps", level=2, heading="Come Norya ti aiuta a capire i risultati del magnesio",
                body_html="<p><strong>Norya</strong> semplifica l'interpretazione: caricate i risultati e ricevete un report chiaro in minuti. <a href=\"/analyze\">Iniziate l'analisi con Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="בדיקת מגנזיום בדם: מה המשמעות של רמות נמוכות או גבוהות",
                body_html="<p><strong>מגנזיום</strong> הוא המינרל הרביעי בשכיחותו בגוף וקופקטור חיוני ביותר מ-<strong>300 תגובות אנזימטיות</strong>. חוסר מגנזיום נפוץ להפליא. מדריך זה חינוכי ואינו מחליף ייעוץ רפואי.</p>"),
        Section(id="what-is-magnesium", level=2, heading="מהו מגנזיום?",
                body_html="<p>מגנזיום (Mg<sup>2+</sup>) הוא הקטיון התוך-תאי השני בשכיחותו. הגוף מכיל כ-25 גרם: <strong>60% בעצמות</strong>, <strong>20% בשריר</strong>, <strong>19% ברקמות רכות</strong> ורק <strong>1% בנוזלים חוץ-תאיים</strong>.</p>"),
        Section(id="role-in-body", level=2, heading="תפקיד המגנזיום בגוף",
                body_html="<p>מגנזיום מעורב ביותר מ-300 מערכות אנזימטיות: ייצור אנרגיה (ATP), תפקוד שרירים ועצבים, קצב לב, בריאות עצמות, ויסות סוכר בדם ולחץ דם. ראו גם <a href=\"/blog/calcium-blood-test-meaning\">סידן</a> ו-<a href=\"/blog/potassium-blood-test-meaning\">אשלגן</a>.</p>"),
        Section(id="normal-ranges", level=2, heading="טווחים תקינים של מגנזיום",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">סמן</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח תקין</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">מגנזיום בסרום</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2 mg/dL (0.70 &ndash; 0.91 mmol/L)</td></tr></tbody></table><p>מגנזיום בסרום משקף רק <strong>1% מהמגנזיום הכולל בגוף</strong>.</p>'),
        Section(id="low-magnesium-causes", level=2, heading="גורמים למגנזיום נמוך",
                body_html="<p><strong>צריכה לא מספקת:</strong> ירקות ירוקים, אגוזים, זרעים. <strong>איבודים GI:</strong> שלשול כרוני, צליאק, אלכוהוליזם. <strong>איבודים כלייתיים:</strong> משתנים, PPI, אמינוגליקוזידים, סוכרת, תסמונות גיטלמן/ברטר.</p>"),
        Section(id="high-magnesium-causes", level=2, heading="גורמים למגנזיום גבוה",
                body_html="<p><strong>אי-ספיקת כליות</strong> (הגורם השכיח ביותר), <strong>תוספת מופרזת</strong>, אנטאצידים ומשלשלים המכילים מגנזיום. היפרמגנזמיה חמורה (&gt;4.0 mg/dL) היא מצב חירום רפואי.</p>"),
        Section(id="symptoms", level=2, heading="תסמינים של חוסר ועודף מגנזיום",
                body_html="<p><strong>היפומגנזמיה:</strong> התכווצויות, רעד, הפרעות קצב, עייפות, היפוקלמיה והיפוקלצמיה עמידות. <strong>היפרמגנזמיה:</strong> קלה (בחילה), בינונית (איבוד רפלקסים), חמורה (דיכוי נשימתי, דום לב).</p>"),
        Section(id="dietary-sources", level=2, heading="מקורות תזונתיים של מגנזיום",
                body_html="<p>צריכה מומלצת: גברים 400-420 מ\"ג/יום, נשים 310-320 מ\"ג/יום. מקורות: זרעי דלעת, שקדים, תרד, שוקולד מריר, שעועית שחורה, אבוקדו, אורז חום.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא",
                body_html="<p>פנו לרופא אם: מגנזיום מתחת ל-1.7 mg/dL; היפוקלמיה או היפוקלצמיה עמידות; נטילת משתנים/PPI; מחלת כליות כרונית; הפרעות קצב; או תסמינים חמורים של היפרמגנזמיה.</p>"),
        Section(id="how-norya-helps", level=2, heading="כיצד Norya עוזרת לך להבין את תוצאות המגנזיום",
                body_html="<p><strong>Norya</strong> מפשטת את הפרשנות: העלו תוצאות וקבלו דוח בריאות ברור תוך דקות. <a href=\"/analyze\">התחילו ניתוח עם Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="मैग्नीशियम रक्त परीक्षण: कम या अधिक स्तर का क्या अर्थ है",
                body_html="<p><strong>मैग्नीशियम</strong> शरीर में चौथा सबसे प्रचुर खनिज है और <strong>300 से अधिक एंजाइमी प्रतिक्रियाओं</strong> में एक आवश्यक सहकारक है। इसके महत्व के बावजूद, मैग्नीशियम की कमी उल्लेखनीय रूप से आम है।</p><p>यह मार्गदर्शिका शैक्षिक है और चिकित्सा सलाह का विकल्प नहीं है।</p>"),
        Section(id="what-is-magnesium", level=2, heading="मैग्नीशियम क्या है?",
                body_html="<p>मैग्नीशियम (Mg<sup>2+</sup>) दूसरा सबसे प्रचुर अंतःकोशिकीय धनायन है। शरीर में लगभग 25 ग्राम होता है: <strong>60% हड्डियों में</strong>, <strong>20% मांसपेशियों में</strong>, <strong>19% अन्य ऊतकों में</strong> और केवल <strong>1% बाह्यकोशिकीय तरल पदार्थों में</strong>।</p>"),
        Section(id="role-in-body", level=2, heading="शरीर में मैग्नीशियम की भूमिका",
                body_html="<p>मैग्नीशियम 300 से अधिक एंजाइम प्रणालियों में शामिल है: ऊर्जा उत्पादन (ATP), मांसपेशी और तंत्रिका कार्य, हृदय गति, हड्डी स्वास्थ्य, रक्त शर्करा और रक्तचाप। <a href=\"/blog/calcium-blood-test-meaning\">कैल्शियम</a> और <a href=\"/blog/potassium-blood-test-meaning\">पोटैशियम</a> गाइड भी देखें।</p>"),
        Section(id="normal-ranges", level=2, heading="सामान्य मैग्नीशियम सीमाएँ",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">मार्कर</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य सीमा</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">सीरम मैग्नीशियम</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2 mg/dL (0.70 &ndash; 0.91 mmol/L)</td></tr></tbody></table><p>सीरम मैग्नीशियम कुल शारीरिक मैग्नीशियम का केवल <strong>1%</strong> दर्शाता है।</p>'),
        Section(id="low-magnesium-causes", level=2, heading="कम मैग्नीशियम के कारण",
                body_html="<p><strong>अपर्याप्त आहार:</strong> हरी पत्तेदार सब्जियों, मेवों, बीजों की कमी। <strong>GI हानि:</strong> पुरानी दस्त, सीलिएक, शराब की लत। <strong>गुर्दे से हानि:</strong> मूत्रवर्धक, PPI, अमीनोग्लाइकोसाइड, मधुमेह, गिटेलमैन/बार्टर सिंड्रोम।</p>"),
        Section(id="high-magnesium-causes", level=2, heading="उच्च मैग्नीशियम के कारण",
                body_html="<p><strong>गुर्दे की विफलता</strong> (सबसे आम कारण), <strong>अत्यधिक पूरकता</strong>, मैग्नीशियम युक्त एंटासिड और रेचक। गंभीर हाइपरमैग्नेसीमिया (&gt;4.0 mg/dL) एक चिकित्सा आपातकाल है।</p>"),
        Section(id="symptoms", level=2, heading="मैग्नीशियम की कमी और अधिकता के लक्षण",
                body_html="<p><strong>हाइपोमैग्नेसीमिया:</strong> मांसपेशियों में ऐंठन, कंपन, अतालता, थकान, प्रतिरोधी हाइपोकैलेमिया और हाइपोकैल्सीमिया। <strong>हाइपरमैग्नेसीमिया:</strong> हल्का (मतली), मध्यम (रिफ्लेक्स हानि), गंभीर (श्वसन अवसाद, कार्डियक अरेस्ट)।</p>"),
        Section(id="dietary-sources", level=2, heading="मैग्नीशियम के आहार स्रोत",
                body_html="<p>अनुशंसित दैनिक सेवन: पुरुष 400-420 mg, महिलाएँ 310-320 mg। स्रोत: कद्दू के बीज, बादाम, पालक, डार्क चॉकलेट, काली फलियाँ, एवोकाडो, ब्राउन राइस।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर को कब दिखाएँ",
                body_html="<p>डॉक्टर से परामर्श करें यदि: मैग्नीशियम &lt;1.7 mg/dL; प्रतिरोधी हाइपोकैलेमिया/हाइपोकैल्सीमिया; मूत्रवर्धक/PPI लेना; क्रोनिक किडनी रोग; हृदय अतालता; या गंभीर हाइपरमैग्नेसीमिया लक्षण।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya मैग्नीशियम परिणामों को समझने में कैसे मदद करता है",
                body_html="<p><strong>Norya</strong> व्याख्या को सरल बनाता है: रक्त जांच के परिणाम अपलोड करें और मिनटों में स्पष्ट स्वास्थ्य रिपोर्ट प्राप्त करें। <a href=\"/analyze\">Norya के साथ विश्लेषण शुरू करें</a>।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="تحليل المغنيسيوم في الدم: ماذا تعني المستويات المنخفضة أو المرتفعة",
                body_html="<p><strong>المغنيسيوم</strong> هو رابع أكثر المعادن وفرة في الجسم وعامل مساعد أساسي في أكثر من <strong>300 تفاعل إنزيمي</strong>. نقص المغنيسيوم شائع بشكل ملحوظ. هذا الدليل تعليمي ولا يحل محل المشورة الطبية.</p>"),
        Section(id="what-is-magnesium", level=2, heading="ما هو المغنيسيوم؟",
                body_html="<p>المغنيسيوم (Mg<sup>2+</sup>) هو ثاني أكثر الكاتيونات داخل الخلوية وفرة. يحتوي الجسم على حوالي 25 غرام: <strong>60% في العظام</strong>، <strong>20% في العضلات</strong>، <strong>19% في الأنسجة الرخوة</strong> و<strong>1% فقط في السوائل خارج الخلوية</strong>.</p>"),
        Section(id="role-in-body", level=2, heading="دور المغنيسيوم في الجسم",
                body_html="<p>المغنيسيوم يشارك في أكثر من 300 نظام إنزيمي: إنتاج الطاقة (ATP)، وظيفة العضلات والأعصاب، نظم القلب، صحة العظام، تنظيم سكر الدم وضغط الدم. انظر أدلتنا حول <a href=\"/blog/calcium-blood-test-meaning\">الكالسيوم</a> و<a href=\"/blog/potassium-blood-test-meaning\">البوتاسيوم</a>.</p>"),
        Section(id="normal-ranges", level=2, heading="النطاقات الطبيعية للمغنيسيوم",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المؤشر</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق الطبيعي</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">مغنيسيوم المصل</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2 mg/dL (0.70 &ndash; 0.91 mmol/L)</td></tr></tbody></table><p>مغنيسيوم المصل يعكس فقط <strong>1% من إجمالي مغنيسيوم الجسم</strong>.</p>'),
        Section(id="low-magnesium-causes", level=2, heading="أسباب انخفاض المغنيسيوم",
                body_html="<p><strong>نقص التغذية:</strong> قلة الخضروات الورقية والمكسرات والبذور. <strong>فقدان معدي معوي:</strong> إسهال مزمن، داء بطني، إدمان كحول. <strong>فقدان كلوي:</strong> مدرات البول، مثبطات مضخة البروتون، أمينوغليكوزيدات، السكري، متلازمات جيتلمان/بارتر.</p>"),
        Section(id="high-magnesium-causes", level=2, heading="أسباب ارتفاع المغنيسيوم",
                body_html="<p><strong>الفشل الكلوي</strong> (السبب الأكثر شيوعاً)، <strong>الإفراط في المكملات</strong>، مضادات الحموضة والملينات المحتوية على المغنيسيوم. فرط المغنيسيوم الحاد (&gt;4.0 mg/dL) حالة طوارئ طبية.</p>"),
        Section(id="symptoms", level=2, heading="أعراض نقص وفرط المغنيسيوم",
                body_html="<p><strong>نقص المغنيسيوم:</strong> تشنجات عضلية، رعشة، اضطرابات نظم القلب، إرهاق، نقص بوتاسيوم ونقص كالسيوم مقاومين للعلاج. <strong>فرط المغنيسيوم:</strong> خفيف (غثيان)، متوسط (فقدان منعكسات)، شديد (تثبيط تنفسي، سكتة قلبية).</p>"),
        Section(id="dietary-sources", level=2, heading="المصادر الغذائية للمغنيسيوم",
                body_html="<p>الكمية الموصى بها: رجال 400-420 مغ/يوم، نساء 310-320 مغ/يوم. المصادر: بذور اليقطين، اللوز، السبانخ، الشوكولاتة الداكنة، الفاصوليا السوداء، الأفوكادو، الأرز البني.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى يجب مراجعة الطبيب",
                body_html="<p>استشر طبيبك إذا: مغنيسيوم أقل من 1.7 mg/dL؛ نقص بوتاسيوم أو كالسيوم مقاوم للعلاج؛ تناول مدرات بول/PPI؛ مرض كلوي مزمن؛ اضطرابات نظم القلب؛ أو أعراض شديدة لفرط المغنيسيوم.</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف تساعدك Norya في فهم نتائج المغنيسيوم",
                body_html="<p><strong>Norya</strong> تبسّط التفسير: ارفع نتائج تحليل الدم واحصل على تقرير صحي واضح خلال دقائق. <a href=\"/analyze\">ابدأ التحليل مع Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# PUBLIC GETTERS
# ---------------------------------------------------------------------------
def get_magnesium_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_magnesium_faq_schema_qa() -> dict:
    return {
        "en": [
            {"question": "What is a normal magnesium level?",
             "answer": "Normal serum magnesium is 1.7-2.2 mg/dL (0.70-0.91 mmol/L). However, serum levels reflect only 1% of total body magnesium, so deficiency can exist even with normal blood levels."},
            {"question": "What causes low magnesium?",
             "answer": "Common causes include poor dietary intake, malabsorption (celiac, Crohn's), alcoholism, medications (diuretics, PPIs), diabetes, and bariatric surgery."},
            {"question": "What are the symptoms of magnesium deficiency?",
             "answer": "Muscle cramps, spasms, tremors, fatigue, irritability, heart palpitations, and in severe cases seizures. Magnesium deficiency also causes refractory hypokalemia and hypocalcemia."},
            {"question": "What foods are high in magnesium?",
             "answer": "Pumpkin seeds (156 mg per ounce), almonds, spinach, dark chocolate, black beans, avocado, and brown rice are excellent sources."},
            {"question": "Can too much magnesium be dangerous?",
             "answer": "Yes. Hypermagnesemia is rare with normal kidneys but dangerous in kidney failure. Severe levels (above 4.0 mg/dL) can cause respiratory depression, heart block, and cardiac arrest."},
        ],
        "tr": [
            {"question": "Normal magnezyum düzeyi nedir?",
             "answer": "Normal serum magnezyum 1,7-2,2 mg/dL'dir. Ancak serum düzeyleri toplam vücut magnezyumunun yalnızca %1'ini yansıtır."},
            {"question": "Düşük magnezyumun nedenleri nelerdir?",
             "answer": "Yetersiz diyet alımı, emilim bozuklukları, alkolizm, diüretik ve PPI gibi ilaçlar, diyabet ve bariyatrik cerrahi."},
            {"question": "Magnezyum eksikliğinin belirtileri nelerdir?",
             "answer": "Kas krampları, spazmlar, tremor, yorgunluk, çarpıntı ve ağır vakalarda nöbet. Dirençli hipokalemi ve hipokalsemiye de neden olur."},
            {"question": "Hangi besinler magnezyum açısından zengindir?",
             "answer": "Kabak çekirdeği, badem, ıspanak, bitter çikolata, siyah fasulye, avokado ve esmer pirinç."},
        ],
        "es": [
            {"question": "¿Cuál es un nivel normal de magnesio?",
             "answer": "El magnesio sérico normal es 1,7-2,2 mg/dL. Solo refleja el 1% del magnesio corporal total."},
            {"question": "¿Qué causa el magnesio bajo?",
             "answer": "Dieta insuficiente, malabsorción, alcoholismo, medicamentos (diuréticos, IBP), diabetes y cirugía bariátrica."},
            {"question": "¿Cuáles son los síntomas de la deficiencia de magnesio?",
             "answer": "Calambres, espasmos, temblor, fatiga, palpitaciones y en casos graves convulsiones. También causa hipopotasemia e hipocalcemia refractarias."},
        ],
        "de": [
            {"question": "Was ist ein normaler Magnesiumwert?",
             "answer": "Normales Serummagnesium: 1,7-2,2 mg/dL. Spiegelt nur 1% des Gesamtkörpermagnesiums wider."},
            {"question": "Was verursacht niedrige Magnesiumwerte?",
             "answer": "Unzureichende Ernährung, Malabsorption, Alkoholismus, Medikamente (Diuretika, PPI), Diabetes und bariatrische Chirurgie."},
            {"question": "Welche Symptome hat Magnesiummangel?",
             "answer": "Muskelkrämpfe, Tremor, Arrhythmien, Müdigkeit, Reizbarkeit und in schweren Fällen Krampfanfälle. Verursacht auch refraktäre Hypokaliämie und Hypokalzämie."},
        ],
        "fr": [
            {"question": "Quel est un taux normal de magnésium ?",
             "answer": "Le magnésium sérique normal est de 1,7-2,2 mg/dL. Il ne reflète que 1% du magnésium corporel total."},
            {"question": "Quelles sont les causes d'un magnésium bas ?",
             "answer": "Apport alimentaire insuffisant, malabsorption, alcoolisme, médicaments (diurétiques, IPP), diabète et chirurgie bariatrique."},
            {"question": "Quels sont les symptômes de la carence en magnésium ?",
             "answer": "Crampes, tremblements, arythmies, fatigue, irritabilité et convulsions dans les cas graves. Cause aussi une hypokaliémie et hypocalcémie réfractaires."},
        ],
        "it": [
            {"question": "Qual è un livello normale di magnesio?",
             "answer": "Il magnesio sierico normale è 1,7-2,2 mg/dL. Riflette solo l'1% del magnesio corporeo totale."},
            {"question": "Cosa causa il magnesio basso?",
             "answer": "Apporto alimentare inadeguato, malassorbimento, alcolismo, farmaci (diuretici, IPP), diabete e chirurgia bariatrica."},
            {"question": "Quali sono i sintomi della carenza di magnesio?",
             "answer": "Crampi, tremori, aritmie, affaticamento e in casi gravi convulsioni. Causa anche ipokaliemia e ipocalcemia refrattarie."},
        ],
        "he": [
            {"question": "מהי רמת מגנזיום תקינה?",
             "answer": "מגנזיום תקין בסרום: 1.7-2.2 mg/dL. משקף רק 1% מהמגנזיום הכולל בגוף."},
            {"question": "מה גורם למגנזיום נמוך?",
             "answer": "צריכה לא מספקת, תת-ספיגה, אלכוהוליזם, תרופות (משתנים, PPI), סוכרת וניתוח בריאטרי."},
            {"question": "מהם תסמיני חסר מגנזיום?",
             "answer": "התכווצויות, רעד, הפרעות קצב, עייפות ובמקרים חמורים פרכוסים. גורם גם להיפוקלמיה והיפוקלצמיה עמידות."},
        ],
        "hi": [
            {"question": "सामान्य मैग्नीशियम स्तर क्या है?",
             "answer": "सामान्य सीरम मैग्नीशियम 1.7-2.2 mg/dL है। यह कुल शारीरिक मैग्नीशियम का केवल 1% दर्शाता है।"},
            {"question": "कम मैग्नीशियम का क्या कारण है?",
             "answer": "अपर्याप्त आहार, कुअवशोषण, शराब की लत, दवाएँ (मूत्रवर्धक, PPI), मधुमेह और बेरियाट्रिक सर्जरी।"},
            {"question": "मैग्नीशियम की कमी के लक्षण क्या हैं?",
             "answer": "मांसपेशियों में ऐंठन, कंपन, अतालता, थकान और गंभीर मामलों में दौरे। प्रतिरोधी हाइपोकैलेमिया और हाइपोकैल्सीमिया भी कारण बनता है।"},
        ],
        "ar": [
            {"question": "ما هو المستوى الطبيعي للمغنيسيوم؟",
             "answer": "المغنيسيوم المصلي الطبيعي: 1.7-2.2 mg/dL. يعكس فقط 1% من إجمالي مغنيسيوم الجسم."},
            {"question": "ما أسباب انخفاض المغنيسيوم؟",
             "answer": "نقص التغذية، سوء الامتصاص، إدمان الكحول، أدوية (مدرات البول، مثبطات مضخة البروتون)، السكري وجراحة السمنة."},
            {"question": "ما أعراض نقص المغنيسيوم؟",
             "answer": "تشنجات عضلية، رعشة، اضطرابات نظم القلب، إرهاق وفي الحالات الشديدة نوبات صرع. يسبب أيضاً نقص بوتاسيوم ونقص كالسيوم مقاومين للعلاج."},
        ],
    }
