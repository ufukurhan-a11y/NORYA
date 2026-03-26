# -*- coding: utf-8 -*-
"""
Triglycerides blog article — full body content for all 9 languages.
Used by blog_i18n._article_triglycerides().
Sections: intro, what-are-triglycerides, normal-ranges, high-triglycerides-causes,
triglycerides-vs-cholesterol, cardiovascular-risk, lifestyle-and-diet, medications,
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
            heading="High triglycerides: what your blood test result means",
            body_html=(
                "<p><strong>Triglycerides</strong> are the most common type of fat (lipid) in your body. When you eat, your body converts "
                "any calories it doesn't need to use right away into triglycerides, which are stored in fat cells and later released for energy "
                "between meals. A routine blood test called a <em>lipid panel</em> measures triglycerides along with total cholesterol, "
                "LDL cholesterol, and HDL cholesterol to assess your cardiovascular risk profile.</p>"
                "<p>While some level of triglycerides is necessary for normal body function, elevated triglycerides&mdash;a condition called "
                "<strong>hypertriglyceridemia</strong>&mdash;can significantly increase the risk of heart disease, stroke, and pancreatitis. "
                "Studies consistently show that high triglyceride levels are an independent risk factor for atherosclerotic cardiovascular disease, "
                "even after adjusting for other lipid markers. Understanding your triglyceride level is therefore a crucial part of managing "
                "your overall metabolic health.</p>"
                "<p>This guide explains what triglycerides are, how to interpret your results, what causes elevated levels, and what lifestyle "
                "changes and treatments are available. It is educational and does not replace medical advice. Always discuss your lipid panel "
                "results with your doctor.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="What are triglycerides?",
            body_html=(
                "<p>Triglycerides are molecules composed of three fatty acid chains attached to a glycerol backbone. They are the primary form "
                "in which the body stores fat. After you eat a meal, your intestines absorb dietary fats and package them into lipoproteins called "
                "<strong>chylomicrons</strong>, which transport triglycerides through the bloodstream to tissues that need energy or store fat. "
                "The liver also produces triglycerides from excess carbohydrates and packages them into <strong>very-low-density lipoproteins (VLDL)</strong>.</p>"
                "<p>An enzyme called <strong>lipoprotein lipase</strong>, located on the surface of blood vessel walls, breaks down triglycerides in "
                "circulating lipoproteins so that fatty acids can enter muscle cells (for energy) or adipose tissue (for storage). When caloric intake "
                "consistently exceeds expenditure&mdash;especially from sugars, refined carbohydrates, and alcohol&mdash;the liver ramps up VLDL "
                "production, and triglyceride levels in the blood rise.</p>"
                "<p>Because triglyceride levels are heavily influenced by recent food intake, your doctor will typically ask you to fast for "
                "9&ndash;12 hours before having a lipid panel drawn. Non-fasting triglyceride levels may be 20&ndash;30% higher than fasting values, "
                "though recent guidelines accept non-fasting samples for initial screening.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Triglyceride reference ranges",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Category</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fasting level (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fasting level (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Borderline high</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">High</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.3 &ndash; 5.6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Very high</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5.6</td></tr>'
                "</tbody></table>"
                "<p>These categories are based on the <strong>National Cholesterol Education Program (NCEP) Adult Treatment Panel III</strong> guidelines "
                "and are widely adopted worldwide. An optimal triglyceride level is below 100&nbsp;mg/dL, which is associated with the lowest "
                "cardiovascular risk. Borderline-high levels signal the need for lifestyle modifications, while high and very-high levels often "
                "require a combination of lifestyle changes and medication.</p>"
                "<p>It is important to note that triglyceride levels can fluctuate significantly from day to day&mdash;by as much as 20&ndash;30%&mdash;"
                "based on diet, exercise, alcohol intake, and illness. A single measurement should be confirmed with a repeat test before making "
                "treatment decisions. Very high levels (&ge;500&nbsp;mg/dL) require urgent attention due to the risk of acute pancreatitis.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Causes of high triglycerides",
            body_html=(
                "<p>Elevated triglycerides can result from lifestyle factors, underlying medical conditions, medications, or genetic predisposition. "
                "Understanding the root cause is essential for choosing the right treatment approach:</p>"
                "<p><strong>Lifestyle and dietary factors:</strong></p>"
                "<ul>"
                "<li><strong>Excessive caloric intake</strong> &ndash; consuming more calories than the body can burn leads to increased VLDL production by the liver.</li>"
                "<li><strong>High intake of refined carbohydrates and sugars</strong> &ndash; white bread, pastries, sweetened beverages, and fruit juices "
                "stimulate hepatic de-novo lipogenesis, converting excess glucose into triglycerides.</li>"
                "<li><strong>Excess alcohol consumption</strong> &ndash; alcohol is metabolized by the liver and promotes triglyceride synthesis. Even moderate "
                "drinking can raise levels in susceptible individuals.</li>"
                "<li><strong>Sedentary lifestyle</strong> &ndash; physical inactivity reduces lipoprotein lipase activity, slowing triglyceride clearance from the blood.</li>"
                "<li><strong>Obesity</strong> &ndash; particularly visceral (abdominal) adiposity is strongly correlated with hypertriglyceridemia and insulin resistance.</li>"
                "</ul>"
                "<p><strong>Medical conditions:</strong></p>"
                "<ul>"
                "<li><strong>Type 2 diabetes and insulin resistance</strong> &ndash; insulin normally suppresses hepatic VLDL production; when tissues become resistant to insulin, "
                "the liver overproduces triglyceride-rich particles.</li>"
                "<li><strong>Hypothyroidism</strong> &ndash; thyroid hormones regulate lipoprotein lipase activity; low thyroid function slows triglyceride clearance.</li>"
                "<li><strong>Chronic kidney disease and nephrotic syndrome</strong> &ndash; altered lipoprotein metabolism and increased hepatic lipid synthesis.</li>"
                "<li><strong>Genetic factors</strong> &ndash; familial hypertriglyceridemia and familial combined hyperlipidemia are inherited conditions that cause "
                "persistently elevated triglycerides regardless of diet.</li>"
                "</ul>"
                "<p><strong>Medications:</strong> Beta-blockers, thiazide diuretics, corticosteroids, oral estrogens, tamoxifen, retinoids, and some antiretroviral drugs "
                "can raise triglyceride levels as a side effect. If your triglycerides rose after starting a new medication, discuss alternatives with your doctor.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglycerides vs. cholesterol: understanding the difference",
            body_html=(
                "<p>Although both triglycerides and cholesterol are lipids carried in the blood, they serve fundamentally different purposes. "
                "<strong>Triglycerides</strong> are used for energy storage and release; they are the body's primary fuel reserve. "
                "<strong>Cholesterol</strong>, on the other hand, is a structural component of cell membranes and a precursor for hormones "
                "(estrogen, testosterone, cortisol), bile acids, and vitamin D.</p>"
                "<p>On a standard lipid panel, you will see several cholesterol-related measurements: <strong>total cholesterol</strong>, "
                "<strong>LDL (low-density lipoprotein)</strong> cholesterol&mdash;often called &ldquo;bad&rdquo; cholesterol because elevated levels "
                "promote plaque formation in arteries&mdash;and <strong>HDL (high-density lipoprotein)</strong> cholesterol, known as &ldquo;good&rdquo; "
                "cholesterol because it helps remove cholesterol from artery walls. Triglycerides are measured separately but are closely interrelated "
                "with these cholesterol fractions. For more on LDL and HDL, see our guides on "
                '<a href="/en/blog/ldl-cholesterol-level">LDL cholesterol</a> and '
                '<a href="/en/blog/ldl-vs-hdl-what-it-means">LDL vs HDL</a>. '
                "Clinicians often also interpret <a href=\"/en/blog/apob-meaning\">ApoB</a> and "
                "<a href=\"/en/blog/lpa-meaning\">Lp(a)</a> alongside triglycerides when assessing atherogenic particle load and inherited risk context.</p>"
                "<p>High triglycerides frequently coexist with <em>low HDL</em> and the presence of <em>small, dense LDL particles</em>&mdash;a combination "
                "sometimes called the <strong>atherogenic lipid triad</strong> or <strong>lipid triad of metabolic syndrome</strong>. This pattern is "
                "particularly dangerous because small dense LDL particles penetrate artery walls more easily, accelerating atherosclerosis. Thus, even if "
                "your LDL number looks acceptable, high triglycerides may signal that your LDL particles are of the more harmful subtype.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Triglycerides and cardiovascular risk",
            body_html=(
                "<p>For decades, the link between triglycerides and heart disease was debated. While LDL cholesterol has long been established as "
                "a causal factor in atherosclerosis, the role of triglycerides was less clear because high triglycerides often coexist with other "
                "metabolic abnormalities. However, large-scale genetic studies (<em>Mendelian randomization</em>) have now confirmed that "
                "<strong>triglyceride-rich lipoproteins are independently causal for atherosclerotic cardiovascular disease</strong>.</p>"
                "<p>Elevated triglycerides contribute to cardiovascular risk through several mechanisms. Remnant particles&mdash;the partially "
                "metabolized remains of VLDL and chylomicrons&mdash;can penetrate the artery wall and trigger inflammation, similar to LDL. "
                "High triglycerides also promote a pro-thrombotic state by increasing levels of plasminogen activator inhibitor-1 (PAI-1) and "
                "fibrinogen, making blood clots more likely. Additionally, very high triglyceride levels (&ge;500&nbsp;mg/dL) carry the serious risk of "
                "<strong>acute pancreatitis</strong>&mdash;inflammation of the pancreas that can be life-threatening.</p>"
                "<p>The combination of high triglycerides with other elements of <strong>metabolic syndrome</strong>&mdash;central obesity, high blood pressure, "
                "elevated fasting glucose, and low HDL cholesterol&mdash;creates a synergistic increase in cardiovascular risk that is greater than the sum "
                "of individual risk factors. Addressing triglycerides is therefore an important part of comprehensive cardiovascular risk management.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Lifestyle and dietary changes to lower triglycerides",
            body_html=(
                "<p>Lifestyle modification is the cornerstone of triglyceride management and can reduce levels by 20&ndash;50% or more. "
                "The most effective strategies include:</p>"
                "<ul>"
                "<li><strong>Reduce refined carbohydrates and added sugars</strong> &ndash; limit white bread, pasta, rice, sweets, "
                "and especially sugar-sweetened beverages. Fructose is particularly potent at raising triglycerides because it is metabolized "
                "directly by the liver.</li>"
                "<li><strong>Limit or eliminate alcohol</strong> &ndash; even small amounts of alcohol can significantly raise triglycerides in "
                "sensitive individuals. Complete abstinence may be necessary for people with very high levels.</li>"
                "<li><strong>Increase omega-3 fatty acid intake</strong> &ndash; fatty fish (salmon, mackerel, sardines, herring) provide EPA and DHA, "
                "which reduce hepatic VLDL production. The American Heart Association recommends eating fish at least twice per week.</li>"
                "<li><strong>Choose healthy fats</strong> &ndash; replace saturated fats with monounsaturated fats (olive oil, avocados, nuts) "
                "and polyunsaturated fats (flaxseed, walnuts).</li>"
                "<li><strong>Exercise regularly</strong> &ndash; aim for at least 150 minutes per week of moderate-intensity aerobic activity. "
                "Exercise increases lipoprotein lipase activity, accelerating triglyceride clearance from the blood.</li>"
                "<li><strong>Lose excess weight</strong> &ndash; even a 5&ndash;10% weight loss can lower triglycerides by 20% or more.</li>"
                "<li><strong>Increase fiber intake</strong> &ndash; soluble fiber from oats, beans, lentils, and vegetables slows carbohydrate absorption.</li>"
                "</ul>"
                "<p>A Mediterranean-style diet that emphasizes vegetables, fruits, whole grains, legumes, fish, and olive oil while minimizing "
                "processed foods and sweets has been shown to effectively reduce triglycerides and improve overall cardiovascular health. "
                "Combining dietary changes with regular physical activity produces the most significant and sustainable results.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medications for high triglycerides",
            body_html=(
                "<p>When lifestyle changes alone are insufficient&mdash;particularly when triglycerides remain above 200&nbsp;mg/dL despite diet and "
                "exercise&mdash;your doctor may consider medications:</p>"
                "<ul>"
                "<li><strong>Fibrates (fenofibrate, gemfibrozil)</strong> &ndash; these drugs activate PPAR-alpha receptors, increasing lipoprotein lipase "
                "activity and reducing hepatic VLDL production. They can lower triglycerides by 30&ndash;50%. Fibrates are often the first-line drug "
                "specifically for hypertriglyceridemia.</li>"
                "<li><strong>Omega-3 fatty acid prescriptions (icosapent ethyl / Vascepa)</strong> &ndash; prescription-strength EPA has been shown "
                "to reduce cardiovascular events in the REDUCE-IT trial. Doses of 2&ndash;4&nbsp;g/day can lower triglycerides by 20&ndash;45%.</li>"
                "<li><strong>Statins</strong> &ndash; while primarily used for LDL cholesterol reduction, statins also modestly lower triglycerides "
                "by 10&ndash;20%. They are often prescribed when both LDL and triglycerides are elevated.</li>"
                "<li><strong>Niacin (nicotinic acid)</strong> &ndash; niacin can lower triglycerides by 20&ndash;35% and raise HDL, but its use has "
                "declined due to side effects (flushing, liver toxicity) and lack of proven cardiovascular benefit in recent trials.</li>"
                "</ul>"
                "<p>For patients with very high triglycerides (&ge;500&nbsp;mg/dL), treatment is urgent to prevent acute pancreatitis. "
                "In these cases, fibrates or high-dose omega-3s are typically initiated alongside strict dietary modification. "
                "Combination therapy may be necessary for patients with severely elevated levels resistant to single agents. "
                "All medications should be used under medical supervision with regular monitoring of liver function and muscle enzymes.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>You should consult your doctor about your triglyceride levels in the following situations:</p>"
                "<ul>"
                "<li>Your fasting triglycerides are <strong>above 150&nbsp;mg/dL</strong> on two or more occasions.</li>"
                "<li>Your triglycerides are <strong>200&ndash;499&nbsp;mg/dL</strong>&mdash;this range requires active management with lifestyle changes "
                "and possibly medication, especially if you have other cardiovascular risk factors.</li>"
                "<li>Your triglycerides are <strong>&ge;500&nbsp;mg/dL</strong>&mdash;this is a medical urgency due to pancreatitis risk and "
                "requires prompt treatment.</li>"
                "<li>You have signs of <strong>metabolic syndrome</strong>: large waist circumference, high blood pressure, elevated fasting glucose, "
                "low HDL cholesterol, along with high triglycerides.</li>"
                "<li>You experience <strong>severe abdominal pain</strong> with very high triglycerides, which could indicate pancreatitis.</li>"
                "<li>You have a family history of premature heart disease or familial hypertriglyceridemia.</li>"
                "</ul>"
                "<p>Adults should have a lipid panel checked at least every 4&ndash;6 years starting at age 20, and more frequently if they have "
                "risk factors such as obesity, diabetes, or a family history of dyslipidemia. Early detection and management of high triglycerides "
                "can significantly reduce the long-term risk of cardiovascular events.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your triglyceride results",
            body_html=(
                "<p>Understanding a lipid panel with multiple numbers can be confusing. <strong>Norya</strong> simplifies this process: "
                "upload your blood test results and receive a structured, easy-to-understand health summary within minutes. "
                "Norya analyzes your triglycerides alongside your cholesterol fractions, glucose, and other markers to give you a "
                "comprehensive view of your metabolic health.</p>"
                "<p>The report highlights which values fall outside the normal range, explains what they mean in plain language, "
                "and helps you prepare informed questions for your next doctor visit. Whether your triglycerides are borderline or very high, "
                "Norya ensures you walk into your appointment with clarity. <a href=\"/analyze\">Start your free analysis with Norya</a>.</p>"
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
            heading="Yüksek trigliserid: kan testi sonucunuz ne anlama geliyor?",
            body_html=(
                "<p><strong>Trigliseridler</strong>, vücuttaki en yaygın yağ (lipit) türüdür. Yemek yediğinizde, vücudunuz hemen kullanmadığı "
                "kalorileri trigliseritlere dönüştürür; bunlar yağ hücrelerinde depolanır ve öğünler arasında enerji için serbest bırakılır. "
                "<em>Lipit paneli</em> adı verilen rutin kan testi, kardiyovasküler risk profilinizi değerlendirmek için trigliseritleri total kolesterol, "
                "LDL kolesterol ve HDL kolesterol ile birlikte ölçer.</p>"
                "<p>Belirli bir düzeyde trigliserit normal vücut fonksiyonları için gerekli olsa da yüksek trigliseridler&mdash;"
                "<strong>hipertrigliseridemi</strong>&mdash;kalp hastalığı, inme ve pankreatit riskini önemli ölçüde artırabilir. "
                "Araştırmalar, yüksek trigliserit düzeylerinin diğer lipit belirteçlerine göre düzeltme yapıldığında bile aterosklerotik "
                "kardiyovasküler hastalık için bağımsız bir risk faktörü olduğunu tutarlı bir şekilde göstermektedir.</p>"
                "<p>Bu rehber trigliseritlerin ne olduğunu, sonuçlarınızı nasıl yorumlayacağınızı, yüksek düzeylerin nedenlerini ve mevcut "
                "yaşam tarzı değişiklikleri ile tedavileri açıklamaktadır. Eğitim amaçlıdır, tıbbi tavsiye yerine geçmez.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Trigliserid nedir?",
            body_html=(
                "<p>Trigliseridler, bir gliserol iskeletine bağlı üç yağ asidi zincirinden oluşan moleküllerdir. Vücudun yağ depolamasının "
                "birincil formudur. Yemek yedikten sonra bağırsaklarınız besin yağlarını emer ve bunları <strong>şilomikronlar</strong> adı verilen "
                "lipoproteinlere paketler; bu lipoproteinler trigliseritleri kan dolaşımı yoluyla enerji gerektiren veya yağ depolayan dokulara taşır. "
                "Karaciğer de fazla karbonhidratlardan trigliserit üretir ve bunları <strong>çok düşük yoğunluklu lipoproteinler (VLDL)</strong> "
                "içinde paketler.</p>"
                "<p>Kan damarı duvarlarının yüzeyinde bulunan <strong>lipoprotein lipaz</strong> enzimi, dolaşımdaki lipoproteinlerdeki trigliseritleri parçalar "
                "ve yağ asitlerinin kas hücrelerine (enerji için) veya yağ dokusuna (depolama için) girmesini sağlar. Kalori alımı sürekli olarak harcamayı aştığında "
                "&mdash;özellikle şekerler, rafine karbonhidratlar ve alkolden&mdash;karaciğer VLDL üretimini artırır ve kandaki trigliserit düzeyleri yükselir.</p>"
                "<p>Trigliserit düzeyleri yakın zamandaki besin alımından büyük ölçüde etkilendiğinden, doktorunuz genellikle lipit paneli çekilmeden önce "
                "9&ndash;12 saat açlık isteyecektir. Tokluk trigliserit düzeyleri açlık değerlerinden %20&ndash;30 daha yüksek olabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Trigliserit referans aralıkları",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Kategori</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Açlık düzeyi (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Açlık düzeyi (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Sınırda yüksek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yüksek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,3 &ndash; 5,6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Çok yüksek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5,6</td></tr>'
                "</tbody></table>"
                "<p>Bu kategoriler <strong>NCEP ATP III</strong> kılavuzlarına dayanmaktadır. Optimal trigliserit düzeyi 100&nbsp;mg/dL'nin "
                "altındadır ve en düşük kardiyovasküler riskle ilişkilidir. Sınırda yüksek düzeyler yaşam tarzı değişiklikleri gerektiğinin sinyalini verirken, "
                "yüksek ve çok yüksek düzeyler genellikle yaşam tarzı değişiklikleri ve ilaç kombinasyonu gerektirir.</p>"
                "<p>Trigliserit düzeylerinin günden güne %20&ndash;30 kadar dalgalanabileceğini unutmamak önemlidir. Tek bir ölçüm, tedavi kararları "
                "alınmadan önce tekrar testle doğrulanmalıdır. Çok yüksek düzeyler (&ge;500&nbsp;mg/dL) akut pankreatit riski nedeniyle acil dikkat gerektirir.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Yüksek trigliserit nedenleri",
            body_html=(
                "<p>Yüksek trigliseridler yaşam tarzı faktörlerinden, altta yatan tıbbi durumlardan, ilaçlardan veya genetik yatkınlıktan kaynaklanabilir:</p>"
                "<p><strong>Yaşam tarzı ve diyet faktörleri:</strong></p>"
                "<ul>"
                "<li><strong>Aşırı kalori alımı</strong> &ndash; vücudun yakabileceğinden fazla kalori tüketmek karaciğerin VLDL üretimini artırır.</li>"
                "<li><strong>Rafine karbonhidrat ve şeker tüketimi</strong> &ndash; beyaz ekmek, hamur işleri, şekerli içecekler karaciğerde de-novo lipogenezi uyarır.</li>"
                "<li><strong>Aşırı alkol tüketimi</strong> &ndash; alkol karaciğerde metabolize edilir ve trigliserit sentezini teşvik eder.</li>"
                "<li><strong>Hareketsiz yaşam tarzı</strong> &ndash; fiziksel hareketsizlik lipoprotein lipaz aktivitesini azaltır.</li>"
                "<li><strong>Obezite</strong> &ndash; özellikle viseral yağlanma hipertrigliseridemi ve insülin direnci ile güçlü bir şekilde ilişkilidir.</li>"
                "</ul>"
                "<p><strong>Tıbbi durumlar:</strong></p>"
                "<ul>"
                "<li><strong>Tip 2 diyabet ve insülin direnci</strong> &ndash; insülin normalde karaciğerin VLDL üretimini baskılar; insülin direncinde karaciğer aşırı üretim yapar.</li>"
                "<li><strong>Hipotiroidizm</strong> &ndash; tiroid hormonları lipoprotein lipaz aktivitesini düzenler; düşük tiroid fonksiyonu trigliserit klerensini yavaşlatır.</li>"
                "<li><strong>Kronik böbrek hastalığı</strong> &ndash; değişmiş lipoprotein metabolizması ve artmış hepatik lipit sentezi.</li>"
                "<li><strong>Genetik faktörler</strong> &ndash; ailesel hipertrigliseridemi ve ailesel kombine hiperlipidemi kalıtsal durumlardır.</li>"
                "</ul>"
                "<p><strong>İlaçlar:</strong> Beta-blokerler, tiazid diüretikler, kortikosteroidler, oral östrojenler, tamoksifen ve bazı antiretroviral ilaçlar yan etki olarak trigliserit düzeylerini yükseltebilir.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Trigliserid ve kolesterol: farkı anlamak",
            body_html=(
                "<p>Hem trigliseridler hem de kolesterol kanda taşınan lipitler olmasına rağmen temelde farklı amaçlara hizmet ederler. "
                "<strong>Trigliseridler</strong> enerji depolama ve salınımı için kullanılır. <strong>Kolesterol</strong> ise hücre zarlarının yapısal bileşeni ve "
                "hormonlar (östrojen, testosteron, kortizol), safra asitleri ve D vitamini için öncüdür.</p>"
                "<p>Standart bir lipit panelinde birkaç kolesterolle ilgili ölçüm göreceksiniz: <strong>total kolesterol</strong>, "
                "<strong>LDL kolesterol</strong>&mdash;atardamarlarda plak oluşumunu teşvik ettiği için &ldquo;kötü&rdquo; kolesterol olarak adlandırılır&mdash;"
                "ve <strong>HDL kolesterol</strong>&mdash;atardamar duvarlarından kolesterolün uzaklaştırılmasına yardımcı olduğu için &ldquo;iyi&rdquo; kolesterol olarak bilinir. "
                "Daha fazla bilgi için <a href=\"/tr/blog/ldl-kolesterol-kac-olmali\">LDL kolesterol</a> ve "
                "<a href=\"/tr/blog/ldl-vs-hdl-what-it-means\">LDL ve HDL</a> rehberlerimize bakabilirsiniz. "
                "Aterojenik partikül yükü ve kalıtsal risk bağlamında klinisyenler trigliseritlere ek olarak sıklıkla "
                "<a href=\"/tr/blog/apob-anlama-gelir\">ApoB</a> ve <a href=\"/tr/blog/lpa-anlama-gelir\">Lp(a)</a> sonuçlarını da yorumlar.</p>"
                "<p>Yüksek trigliseridler sıklıkla <em>düşük HDL</em> ve <em>küçük, yoğun LDL partikülleri</em> ile birlikte görülür&mdash;"
                "bazen <strong>aterojenik lipit triadı</strong> olarak adlandırılan bu kombinasyon. Bu küçük yoğun LDL partikülleri atardamar duvarlarını "
                "daha kolay penetre eder ve aterosklerozu hızlandırır.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Trigliseridler ve kardiyovasküler risk",
            body_html=(
                "<p>On yıllar boyunca trigliseridler ile kalp hastalığı arasındaki bağlantı tartışıldı. LDL kolesterol aterosklerozdaki nedensel rolü "
                "uzun süredir kanıtlanmış olsa da trigliseritlerin rolü daha az netti. Ancak büyük ölçekli genetik çalışmalar (<em>Mendelian randomizasyon</em>) "
                "<strong>trigliseritten zengin lipoproteinlerin aterosklerotik kardiyovasküler hastalık için bağımsız olarak nedensel olduğunu</strong> "
                "doğrulamıştır.</p>"
                "<p>Yüksek trigliseridler kardiyovasküler riske birkaç mekanizma aracılığıyla katkıda bulunur. Artık partiküller&mdash;VLDL ve şilomikronların "
                "kısmen metabolize edilmiş kalıntıları&mdash;atardamar duvarına nüfuz edebilir ve LDL'ye benzer şekilde iltihaplanmayı tetikleyebilir. "
                "Ayrıca çok yüksek trigliserit düzeyleri (&ge;500&nbsp;mg/dL) <strong>akut pankreatit</strong> riskini taşır.</p>"
                "<p><strong>Metabolik sendrom</strong> unsurlarıyla&mdash;merkezi obezite, yüksek tansiyon, yüksek açlık glukozu ve düşük HDL kolesterol&mdash;"
                "yüksek trigliseritlerin kombinasyonu, bireysel risk faktörlerinin toplamından daha büyük bir sinerjik kardiyovasküler risk artışı yaratır.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Trigliseritleri düşürmek için yaşam tarzı ve diyet değişiklikleri",
            body_html=(
                "<p>Yaşam tarzı değişikliği trigliserit yönetiminin temel taşıdır ve düzeyleri %20&ndash;50 veya daha fazla azaltabilir:</p>"
                "<ul>"
                "<li><strong>Rafine karbonhidratları ve eklenen şekerleri azaltın</strong> &ndash; beyaz ekmek, makarna, pirinç, tatlılar ve özellikle şekerli içecekleri sınırlayın.</li>"
                "<li><strong>Alkolü sınırlayın veya bırakın</strong> &ndash; duyarlı bireylerde az miktarda alkol bile trigliseritleri önemli ölçüde yükseltebilir.</li>"
                "<li><strong>Omega-3 yağ asidi alımını artırın</strong> &ndash; yağlı balıklar (somon, uskumru, sardalya) EPA ve DHA sağlar.</li>"
                "<li><strong>Sağlıklı yağları tercih edin</strong> &ndash; doymuş yağları tekli doymamış yağlarla (zeytinyağı, avokado) değiştirin.</li>"
                "<li><strong>Düzenli egzersiz yapın</strong> &ndash; haftada en az 150 dakika orta yoğunlukta aerobik aktivite hedefleyin.</li>"
                "<li><strong>Fazla kiloları verin</strong> &ndash; %5&ndash;10 kilo kaybı bile trigliseritleri %20 veya daha fazla düşürebilir.</li>"
                "<li><strong>Lif alımını artırın</strong> &ndash; yulaf, fasulye, mercimek ve sebzelerden çözünür lif karbonhidrat emilimini yavaşlatır.</li>"
                "</ul>"
                "<p>Sebzeler, meyveler, tam tahıllar, baklagiller, balık ve zeytinyağını ön plana çıkaran Akdeniz tarzı diyet, trigliseritleri etkili bir şekilde "
                "düşürdüğü ve genel kardiyovasküler sağlığı iyileştirdiği gösterilmiştir.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Yüksek trigliserid tedavisinde ilaçlar",
            body_html=(
                "<p>Yaşam tarzı değişiklikleri tek başına yeterli olmadığında&mdash;özellikle diyet ve egzersize rağmen trigliseridler 200&nbsp;mg/dL'nin "
                "üzerinde kaldığında&mdash;doktorunuz ilaç tedavisi düşünebilir:</p>"
                "<ul>"
                "<li><strong>Fibratlar (fenofibrat, gemfibrozil)</strong> &ndash; PPAR-alfa reseptörlerini aktive ederek lipoprotein lipaz aktivitesini artırır "
                "ve hepatik VLDL üretimini azaltır. Trigliseritleri %30&ndash;50 düşürebilir.</li>"
                "<li><strong>Reçeteli omega-3 yağ asitleri (ikosapent etil / Vascepa)</strong> &ndash; reçete dozunda EPA'nın REDUCE-IT çalışmasında "
                "kardiyovasküler olayları azalttığı gösterilmiştir.</li>"
                "<li><strong>Statinler</strong> &ndash; öncelikle LDL kolesterol düşürmek için kullanılsa da statinler trigliseritleri de %10&ndash;20 düşürür.</li>"
                "<li><strong>Niasin (nikotinik asit)</strong> &ndash; trigliseritleri %20&ndash;35 düşürebilir ancak yan etkiler nedeniyle kullanımı azalmıştır.</li>"
                "</ul>"
                "<p>Çok yüksek trigliserit (&ge;500&nbsp;mg/dL) olan hastalarda akut pankreatiti önlemek için tedavi acildir. Bu durumlarda sıkı diyet "
                "değişikliğiyle birlikte fibratlar veya yüksek doz omega-3'ler başlanır. Tüm ilaçlar karaciğer fonksiyonlarının düzenli izlenmesiyle birlikte "
                "tıbbi gözetim altında kullanılmalıdır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda trigliserit düzeyleriniz hakkında doktorunuza danışmalısınız:</p>"
                "<ul>"
                "<li>Açlık trigliseridleriniz iki veya daha fazla ölçümde <strong>150&nbsp;mg/dL'nin üzerinde</strong>.</li>"
                "<li>Trigliseridleriniz <strong>200&ndash;499&nbsp;mg/dL</strong>&mdash;bu aralık yaşam tarzı değişiklikleri ve muhtemelen ilaç tedavisi gerektirir.</li>"
                "<li>Trigliseridleriniz <strong>&ge;500&nbsp;mg/dL</strong>&mdash;pankreatit riski nedeniyle acil tedavi gerektirir.</li>"
                "<li><strong>Metabolik sendrom</strong> belirtileriniz var: geniş bel çevresi, yüksek tansiyon, yüksek açlık şekeri, düşük HDL kolesterol.</li>"
                "<li>Çok yüksek trigliseridlerle birlikte <strong>şiddetli karın ağrısı</strong> yaşıyorsanız&mdash;bu pankreatite işaret edebilir.</li>"
                "<li>Ailede erken kalp hastalığı veya ailesel hipertrigliseridemi öyküsü var.</li>"
                "</ul>"
                "<p>Yetişkinler 20 yaşından itibaren en az her 4&ndash;6 yılda bir lipit paneli yaptırmalı ve obezite, diyabet veya aile öyküsü gibi "
                "risk faktörleri varsa daha sık kontrol edilmelidir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya trigliserit sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Birden fazla sayı içeren bir lipit panelini anlamak kafa karıştırıcı olabilir. <strong>Norya</strong> bu süreci basitleştirir: "
                "kan testi sonuçlarınızı yükleyin ve dakikalar içinde yapılandırılmış, anlaşılması kolay bir sağlık özeti raporu alın. "
                "Norya, trigliseridlerinizi kolesterol fraksiyonlarınız, glikoz ve diğer belirteçlerle birlikte analiz ederek metabolik sağlığınızın "
                "kapsamlı bir görünümünü sunar.</p>"
                "<p>Rapor, hangi değerlerin normal aralığın dışında kaldığını vurgular, bunların ne anlama geldiğini sade bir dille açıklar ve "
                "bir sonraki doktor ziyaretiniz için bilinçli sorular hazırlamanıza yardımcı olur. "
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
        Section(
            id="intro", level=2,
            heading="Triglicéridos altos: qué significa su resultado de análisis de sangre",
            body_html=(
                "<p>Los <strong>triglicéridos</strong> son el tipo de grasa (lípido) más común en el cuerpo. Cuando come, el organismo convierte "
                "las calorías que no necesita de inmediato en triglicéridos, que se almacenan en las células adiposas y se liberan para obtener "
                "energía entre comidas. Un análisis de sangre rutinario llamado <em>perfil lipídico</em> mide los triglicéridos junto con el "
                "colesterol total, LDL y HDL para evaluar su riesgo cardiovascular.</p>"
                "<p>Si bien cierto nivel de triglicéridos es necesario para el funcionamiento normal del cuerpo, los triglicéridos elevados "
                "&mdash;una condición llamada <strong>hipertrigliceridemia</strong>&mdash; pueden aumentar significativamente el riesgo de "
                "enfermedad cardíaca, accidente cerebrovascular y pancreatitis. Los estudios demuestran que los triglicéridos altos son un "
                "factor de riesgo independiente para la enfermedad cardiovascular aterosclerótica.</p>"
                "<p>Esta guía explica qué son los triglicéridos, cómo interpretar sus resultados, las causas de niveles elevados y los "
                "cambios de estilo de vida y tratamientos disponibles. Es educativa y no sustituye el consejo médico.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="¿Qué son los triglicéridos?",
            body_html=(
                "<p>Los triglicéridos son moléculas compuestas por tres cadenas de ácidos grasos unidas a un esqueleto de glicerol. Son la forma "
                "principal en la que el cuerpo almacena grasa. Después de comer, los intestinos absorben las grasas de la dieta y las empaquetan en "
                "lipoproteínas llamadas <strong>quilomicrones</strong>, que transportan los triglicéridos por el torrente sanguíneo. El hígado también "
                "produce triglicéridos a partir del exceso de carbohidratos y los empaqueta en <strong>lipoproteínas de muy baja densidad (VLDL)</strong>.</p>"
                "<p>La enzima <strong>lipoproteína lipasa</strong>, ubicada en las paredes de los vasos sanguíneos, descompone los triglicéridos para que "
                "los ácidos grasos puedan entrar en las células musculares (para energía) o en el tejido adiposo (para almacenamiento). Cuando la ingesta "
                "calórica supera consistentemente el gasto, el hígado aumenta la producción de VLDL y los niveles de triglicéridos se elevan.</p>"
                "<p>Dado que los niveles de triglicéridos son muy sensibles a la ingesta reciente de alimentos, su médico generalmente solicitará un ayuno "
                "de 9&ndash;12 horas antes de la extracción. Los valores en no-ayuno pueden ser un 20&ndash;30% más altos que los valores en ayuno.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos de referencia de triglicéridos",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Categoría</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Nivel en ayunas (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Nivel en ayunas (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Límite alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,3 &ndash; 5,6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Muy alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5,6</td></tr>'
                "</tbody></table>"
                "<p>Estas categorías se basan en las guías del <strong>NCEP ATP III</strong>. Un nivel óptimo de triglicéridos es inferior a "
                "100&nbsp;mg/dL, asociado con el menor riesgo cardiovascular. Los niveles limítrofes señalan la necesidad de modificaciones del "
                "estilo de vida, mientras que niveles altos y muy altos a menudo requieren una combinación de cambios de estilo de vida y medicación.</p>"
                "<p>Los niveles de triglicéridos pueden fluctuar significativamente de un día a otro&mdash;hasta un 20&ndash;30%&mdash;según la dieta, "
                "el ejercicio, el consumo de alcohol y las enfermedades. Una sola medición debe confirmarse con una prueba repetida. Los niveles muy altos "
                "(&ge;500&nbsp;mg/dL) requieren atención urgente debido al riesgo de pancreatitis aguda.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Causas de triglicéridos altos",
            body_html=(
                "<p>Los triglicéridos elevados pueden deberse a factores del estilo de vida, condiciones médicas subyacentes, medicamentos o predisposición genética:</p>"
                "<p><strong>Factores de estilo de vida y dieta:</strong></p>"
                "<ul>"
                "<li><strong>Ingesta calórica excesiva</strong> &ndash; consumir más calorías de las que el cuerpo quema aumenta la producción hepática de VLDL.</li>"
                "<li><strong>Alto consumo de carbohidratos refinados y azúcares</strong> &ndash; pan blanco, bollería, bebidas azucaradas estimulan la lipogénesis hepática.</li>"
                "<li><strong>Exceso de alcohol</strong> &ndash; el alcohol es metabolizado por el hígado y promueve la síntesis de triglicéridos.</li>"
                "<li><strong>Sedentarismo</strong> &ndash; la inactividad física reduce la actividad de la lipoproteína lipasa.</li>"
                "<li><strong>Obesidad</strong> &ndash; especialmente la adiposidad visceral está fuertemente correlacionada con la hipertrigliceridemia.</li>"
                "</ul>"
                "<p><strong>Condiciones médicas:</strong> diabetes tipo 2, hipotiroidismo, enfermedad renal crónica, síndrome nefrótico "
                "y factores genéticos (hipertrigliceridemia familiar). <strong>Medicamentos:</strong> betabloqueantes, diuréticos tiazídicos, "
                "corticosteroides, estrógenos orales y algunos antirretrovirales pueden elevar los triglicéridos.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglicéridos vs. colesterol: entendiendo la diferencia",
            body_html=(
                "<p>Aunque tanto los triglicéridos como el colesterol son lípidos transportados en la sangre, cumplen funciones fundamentalmente "
                "diferentes. Los <strong>triglicéridos</strong> se utilizan para el almacenamiento y liberación de energía. El <strong>colesterol</strong> "
                "es un componente estructural de las membranas celulares y precursor de hormonas, ácidos biliares y vitamina D.</p>"
                "<p>En un perfil lipídico estándar verá: <strong>colesterol total</strong>, <strong>colesterol LDL</strong> (&ldquo;malo&rdquo;) y "
                "<strong>colesterol HDL</strong> (&ldquo;bueno&rdquo;). Para más información, consulte nuestras guías sobre "
                '<a href="/es/blog/niveles-colesterol-ldl">colesterol LDL</a> y '
                '<a href="/es/blog/ldl-vs-hdl-what-it-means">LDL frente a HDL</a>. '
                "Los profesionales suelen valorar también <a href=\"/es/blog/significado-apob\">ApoB</a> y "
                "<a href=\"/es/blog/significado-lpa\">Lp(a)</a> junto a los triglicéridos al evaluar la carga de partículas aterogénicas y el contexto de riesgo heredado.</p>"
                "<p>Los triglicéridos altos frecuentemente coexisten con <em>HDL bajo</em> y <em>partículas LDL pequeñas y densas</em>&mdash;"
                "una combinación llamada <strong>tríada lipídica aterogénica</strong>. Este patrón es particularmente peligroso porque las "
                "partículas LDL pequeñas y densas penetran más fácilmente en las paredes arteriales, acelerando la aterosclerosis.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Triglicéridos y riesgo cardiovascular",
            body_html=(
                "<p>Grandes estudios genéticos (randomización mendeliana) han confirmado que las <strong>lipoproteínas ricas en triglicéridos son "
                "causalmente independientes de la enfermedad cardiovascular aterosclerótica</strong>. Las partículas remanentes pueden penetrar "
                "la pared arterial y desencadenar inflamación, de forma similar al LDL.</p>"
                "<p>Los triglicéridos elevados también promueven un estado protrombótico al aumentar los niveles de PAI-1 y fibrinógeno. "
                "Niveles muy altos (&ge;500&nbsp;mg/dL) conllevan el riesgo grave de <strong>pancreatitis aguda</strong>, una inflamación del "
                "páncreas potencialmente mortal.</p>"
                "<p>La combinación de triglicéridos altos con otros elementos del <strong>síndrome metabólico</strong>&mdash;obesidad central, "
                "hipertensión, glucosa en ayunas elevada y colesterol HDL bajo&mdash;crea un aumento sinérgico del riesgo cardiovascular "
                "mayor que la suma de los factores de riesgo individuales.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Cambios de estilo de vida y dieta para reducir los triglicéridos",
            body_html=(
                "<p>La modificación del estilo de vida es la piedra angular del manejo de triglicéridos y puede reducir los niveles un 20&ndash;50%:</p>"
                "<ul>"
                "<li><strong>Reduzca los carbohidratos refinados y azúcares añadidos</strong> &ndash; limite pan blanco, pasta, arroz, dulces y bebidas azucaradas.</li>"
                "<li><strong>Limite o elimine el alcohol</strong> &ndash; incluso pequeñas cantidades pueden elevar significativamente los triglicéridos.</li>"
                "<li><strong>Aumente la ingesta de omega-3</strong> &ndash; pescados grasos (salmón, caballa, sardinas) aportan EPA y DHA.</li>"
                "<li><strong>Elija grasas saludables</strong> &ndash; sustituya grasas saturadas por monoinsaturadas (aceite de oliva, aguacate).</li>"
                "<li><strong>Haga ejercicio regularmente</strong> &ndash; al menos 150 minutos semanales de actividad aeróbica moderada.</li>"
                "<li><strong>Pierda el exceso de peso</strong> &ndash; incluso un 5&ndash;10% de pérdida de peso puede reducir los triglicéridos un 20% o más.</li>"
                "</ul>"
                "<p>Una dieta de estilo mediterráneo que enfatice verduras, frutas, cereales integrales, legumbres, pescado y aceite de oliva ha demostrado "
                "reducir eficazmente los triglicéridos y mejorar la salud cardiovascular general.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medicamentos para triglicéridos altos",
            body_html=(
                "<p>Cuando los cambios de estilo de vida no son suficientes, su médico puede considerar medicamentos:</p>"
                "<ul>"
                "<li><strong>Fibratos (fenofibrato, gemfibrozilo)</strong> &ndash; pueden reducir los triglicéridos un 30&ndash;50%.</li>"
                "<li><strong>Omega-3 con receta (icosapent etil)</strong> &ndash; el estudio REDUCE-IT demostró reducción de eventos cardiovasculares.</li>"
                "<li><strong>Estatinas</strong> &ndash; reducen modestamente los triglicéridos un 10&ndash;20%.</li>"
                "<li><strong>Niacina</strong> &ndash; puede reducir triglicéridos un 20&ndash;35%, pero su uso ha disminuido por efectos secundarios.</li>"
                "</ul>"
                "<p>Para pacientes con triglicéridos muy altos (&ge;500&nbsp;mg/dL), el tratamiento es urgente para prevenir la pancreatitis aguda. "
                "Todos los medicamentos deben usarse bajo supervisión médica con monitorización regular de la función hepática.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Consulte a su médico sobre sus triglicéridos en las siguientes situaciones:</p>"
                "<ul>"
                "<li>Triglicéridos en ayunas <strong>superiores a 150&nbsp;mg/dL</strong> en dos o más ocasiones.</li>"
                "<li>Triglicéridos entre <strong>200&ndash;499&nbsp;mg/dL</strong> que requieren manejo activo.</li>"
                "<li>Triglicéridos <strong>&ge;500&nbsp;mg/dL</strong>&mdash;urgencia médica por riesgo de pancreatitis.</li>"
                "<li>Signos de <strong>síndrome metabólico</strong>.</li>"
                "<li><strong>Dolor abdominal intenso</strong> con triglicéridos muy altos.</li>"
                "<li>Antecedentes familiares de enfermedad cardíaca prematura o hipertrigliceridemia familiar.</li>"
                "</ul>"
                "<p>Los adultos deben realizarse un perfil lipídico al menos cada 4&ndash;6 años a partir de los 20 años, y con mayor frecuencia si "
                "tienen factores de riesgo como obesidad, diabetes o antecedentes familiares de dislipidemia.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya le ayuda a entender sus resultados de triglicéridos",
            body_html=(
                "<p>Entender un perfil lipídico con múltiples cifras puede ser confuso. <strong>Norya</strong> simplifica este proceso: suba sus "
                "resultados de análisis de sangre y reciba un resumen de salud estructurado y fácil de entender en minutos. Norya analiza sus "
                "triglicéridos junto con sus fracciones de colesterol, glucosa y otros marcadores.</p>"
                "<p>El informe destaca qué valores están fuera del rango normal, explica su significado en un lenguaje claro y le ayuda a preparar "
                "preguntas informadas para su próxima cita médica. <a href=\"/analyze\">Inicie su análisis gratuito con Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> '
                'Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Hohe Triglyceride: Was Ihr Blutergebnis bedeutet",
            body_html=(
                "<p><strong>Triglyceride</strong> sind die häufigste Fettart (Lipid) im Körper. Wenn Sie essen, wandelt der Körper nicht "
                "sofort benötigte Kalorien in Triglyceride um, die in Fettzellen gespeichert und zwischen den Mahlzeiten als Energie "
                "freigesetzt werden. Ein routinemäßiger Bluttest namens <em>Lipidprofil</em> misst Triglyceride zusammen mit Gesamtcholesterin, "
                "LDL- und HDL-Cholesterin, um Ihr kardiovaskuläres Risikoprofil zu bewerten.</p>"
                "<p>Während ein gewisser Triglyceridspiegel für die normale Körperfunktion notwendig ist, können erhöhte Triglyceride&mdash;"
                "ein Zustand namens <strong>Hypertriglyceridämie</strong>&mdash;das Risiko für Herzkrankheiten, Schlaganfall und Pankreatitis "
                "erheblich erhöhen. Studien zeigen, dass hohe Triglyceridspiegel ein unabhängiger Risikofaktor für atherosklerotische "
                "Herz-Kreislauf-Erkrankungen sind.</p>"
                "<p>Dieser Leitfaden erklärt, was Triglyceride sind, wie Sie Ihre Ergebnisse interpretieren, was erhöhte Werte verursacht "
                "und welche Lebensstiländerungen und Behandlungen verfügbar sind. Er dient der Aufklärung und ersetzt keine ärztliche Beratung.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Was sind Triglyceride?",
            body_html=(
                "<p>Triglyceride sind Moleküle aus drei Fettsäureketten, die an ein Glycerolgerüst gebunden sind. Sie sind die primäre Form "
                "der Fettspeicherung im Körper. Nach dem Essen absorbiert der Darm Nahrungsfette und verpackt sie in Lipoproteine namens "
                "<strong>Chylomikronen</strong>. Die Leber produziert ebenfalls Triglyceride aus überschüssigen Kohlenhydraten und verpackt "
                "sie in <strong>Very-Low-Density-Lipoproteine (VLDL)</strong>.</p>"
                "<p>Das Enzym <strong>Lipoproteinlipase</strong> an den Blutgefäßwänden spaltet Triglyceride auf, damit Fettsäuren in Muskelzellen "
                "(zur Energiegewinnung) oder Fettgewebe (zur Speicherung) gelangen können. Wenn die Kalorienaufnahme den Verbrauch übersteigt "
                "&mdash;insbesondere durch Zucker, raffinierte Kohlenhydrate und Alkohol&mdash;steigert die Leber die VLDL-Produktion und die "
                "Triglyceridspiegel im Blut steigen.</p>"
                "<p>Da Triglyceridspiegel stark von der kürzlichen Nahrungsaufnahme beeinflusst werden, wird Ihr Arzt in der Regel eine "
                "9&ndash;12-stündige Nüchternperiode vor der Blutentnahme verlangen.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Triglycerid-Referenzbereiche",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Kategorie</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Nüchternwert (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Nüchternwert (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Grenzwertig hoch</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hoch</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,3 &ndash; 5,6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Sehr hoch</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5,6</td></tr>'
                "</tbody></table>"
                "<p>Ein optimaler Triglyceridspiegel liegt unter 100&nbsp;mg/dL. Grenzwertig hohe Werte signalisieren die Notwendigkeit "
                "von Lebensstiländerungen, während hohe und sehr hohe Werte oft eine Kombination aus Lebensstiländerungen und Medikamenten erfordern.</p>"
                "<p>Triglyceridspiegel können täglich um 20&ndash;30% schwanken. Sehr hohe Werte (&ge;500&nbsp;mg/dL) erfordern dringende "
                "Aufmerksamkeit wegen des Risikos einer akuten Pankreatitis.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Ursachen hoher Triglyceride",
            body_html=(
                "<p>Erhöhte Triglyceride können durch Lebensstilfaktoren, zugrundeliegende Erkrankungen, Medikamente oder genetische Veranlagung verursacht werden:</p>"
                "<p><strong>Lebensstil- und Ernährungsfaktoren:</strong></p>"
                "<ul>"
                "<li><strong>Übermäßige Kalorienzufuhr</strong> &ndash; steigert die hepatische VLDL-Produktion.</li>"
                "<li><strong>Hoher Konsum raffinierter Kohlenhydrate und Zucker</strong> &ndash; stimuliert die hepatische De-novo-Lipogenese.</li>"
                "<li><strong>Übermäßiger Alkoholkonsum</strong> &ndash; fördert die Triglyceridsynthese in der Leber.</li>"
                "<li><strong>Bewegungsmangel</strong> &ndash; vermindert die Lipoproteinlipase-Aktivität.</li>"
                "<li><strong>Adipositas</strong> &ndash; insbesondere viszerale Fettleibigkeit korreliert stark mit Hypertriglyceridämie.</li>"
                "</ul>"
                "<p><strong>Medizinische Ursachen:</strong> Typ-2-Diabetes und Insulinresistenz, Hypothyreose, chronische Nierenerkrankung, "
                "nephrotisches Syndrom und genetische Faktoren (familiäre Hypertriglyceridämie). <strong>Medikamente:</strong> Betablocker, "
                "Thiaziddiuretika, Kortikosteroide, orale Östrogene, Tamoxifen und einige antiretrovirale Medikamente.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglyceride vs. Cholesterin: den Unterschied verstehen",
            body_html=(
                "<p><strong>Triglyceride</strong> dienen der Energiespeicherung und -freisetzung. <strong>Cholesterin</strong> ist ein Strukturbestandteil "
                "der Zellmembranen und Vorläufer von Hormonen (Östrogen, Testosteron, Cortisol), Gallensäuren und Vitamin D.</p>"
                "<p>Im Lipidprofil finden Sie: <strong>Gesamtcholesterin</strong>, <strong>LDL-Cholesterin</strong> (&bdquo;schlecht&ldquo;) und "
                "<strong>HDL-Cholesterin</strong> (&bdquo;gut&ldquo;). Weitere Informationen in unseren Leitfäden zu "
                '<a href="/de/blog/ldl-cholesterin">LDL-Cholesterin</a> und '
                '<a href="/de/blog/ldl-vs-hdl-what-it-means">LDL vs. HDL</a>. '
                "Im klinischen Kontext werden oft auch <a href=\"/de/blog/apob-bedeutung\">ApoB</a> und "
                "<a href=\"/de/blog/lpa-bedeutung\">Lp(a)</a> neben Triglyceriden betrachtet, um ätherogene Partikelzahl und erbliches Risiko einzuordnen.</p>"
                "<p>Hohe Triglyceride treten häufig zusammen mit <em>niedrigem HDL</em> und <em>kleinen, dichten LDL-Partikeln</em> auf&mdash;"
                "die sogenannte <strong>atherogene Lipidtriade</strong>. Dieses Muster ist besonders gefährlich, da kleine dichte LDL-Partikel "
                "leichter in Arterienwände eindringen und die Atherosklerose beschleunigen.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Triglyceride und kardiovaskuläres Risiko",
            body_html=(
                "<p>Große genetische Studien (Mendelsche Randomisierung) haben bestätigt, dass <strong>triglyceridreiche Lipoproteine unabhängig "
                "kausal für atherosklerotische Herz-Kreislauf-Erkrankungen</strong> sind. Remnant-Partikel können die Arterienwand durchdringen "
                "und Entzündungen auslösen.</p>"
                "<p>Erhöhte Triglyceride fördern außerdem einen prothrombotischen Zustand. Sehr hohe Werte (&ge;500&nbsp;mg/dL) bergen das "
                "ernste Risiko einer <strong>akuten Pankreatitis</strong>.</p>"
                "<p>Die Kombination hoher Triglyceride mit den Elementen des <strong>metabolischen Syndroms</strong>&mdash;zentrale Adipositas, "
                "Bluthochdruck, erhöhte Nüchternglukose und niedriges HDL-Cholesterin&mdash;erzeugt eine synergistische Erhöhung des "
                "kardiovaskulären Risikos.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Lebensstil- und Ernährungsänderungen zur Senkung der Triglyceride",
            body_html=(
                "<p>Lebensstiländerungen sind der Grundpfeiler der Triglyceridbehandlung und können die Werte um 20&ndash;50% senken:</p>"
                "<ul>"
                "<li><strong>Raffinierte Kohlenhydrate und Zuckerzusatz reduzieren</strong> &ndash; Weißbrot, Nudeln, Süßigkeiten und gesüßte Getränke einschränken.</li>"
                "<li><strong>Alkohol einschränken oder weglassen</strong> &ndash; schon geringe Mengen können Triglyceride deutlich erhöhen.</li>"
                "<li><strong>Omega-3-Fettsäuren erhöhen</strong> &ndash; fettreicher Fisch (Lachs, Makrele, Sardinen) liefert EPA und DHA.</li>"
                "<li><strong>Gesunde Fette wählen</strong> &ndash; gesättigte Fette durch einfach ungesättigte Fette (Olivenöl, Avocado) ersetzen.</li>"
                "<li><strong>Regelmäßig Sport treiben</strong> &ndash; mindestens 150 Minuten pro Woche moderate aerobe Aktivität.</li>"
                "<li><strong>Übergewicht abbauen</strong> &ndash; schon 5&ndash;10% Gewichtsverlust können Triglyceride um 20% oder mehr senken.</li>"
                "</ul>"
                "<p>Eine mediterrane Ernährung mit Gemüse, Obst, Vollkornprodukten, Hülsenfrüchten, Fisch und Olivenöl hat sich als wirksam "
                "zur Senkung der Triglyceride und Verbesserung der kardiovaskulären Gesundheit erwiesen.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medikamente bei hohen Triglyceriden",
            body_html=(
                "<p>Wenn Lebensstiländerungen allein nicht ausreichen, kann Ihr Arzt Medikamente in Betracht ziehen:</p>"
                "<ul>"
                "<li><strong>Fibrate (Fenofibrat, Gemfibrozil)</strong> &ndash; senken Triglyceride um 30&ndash;50%.</li>"
                "<li><strong>Verschreibungspflichtige Omega-3-Fettsäuren (Icosapentethyl)</strong> &ndash; die REDUCE-IT-Studie zeigte eine Reduktion kardiovaskulärer Ereignisse.</li>"
                "<li><strong>Statine</strong> &ndash; senken Triglyceride moderat um 10&ndash;20%.</li>"
                "<li><strong>Niacin</strong> &ndash; senkt Triglyceride um 20&ndash;35%, wird aber wegen Nebenwirkungen seltener eingesetzt.</li>"
                "</ul>"
                "<p>Bei sehr hohen Triglyceriden (&ge;500&nbsp;mg/dL) ist die Behandlung dringend zur Prävention einer akuten Pankreatitis. "
                "Alle Medikamente sollten unter ärztlicher Aufsicht mit regelmäßiger Kontrolle der Leberfunktion angewendet werden.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann Sie einen Arzt aufsuchen sollten",
            body_html=(
                "<p>Konsultieren Sie Ihren Arzt in folgenden Situationen:</p>"
                "<ul>"
                "<li>Nüchterntriglyceride <strong>über 150&nbsp;mg/dL</strong> bei zwei oder mehr Messungen.</li>"
                "<li>Triglyceride zwischen <strong>200&ndash;499&nbsp;mg/dL</strong>.</li>"
                "<li>Triglyceride <strong>&ge;500&nbsp;mg/dL</strong>&mdash;dringend wegen Pankreatitisrisiko.</li>"
                "<li>Anzeichen eines <strong>metabolischen Syndroms</strong>.</li>"
                "<li><strong>Starke Bauchschmerzen</strong> bei sehr hohen Triglyceriden.</li>"
                "<li>Familiengeschichte mit vorzeitiger Herzerkrankung oder familiärer Hypertriglyceridämie.</li>"
                "</ul>"
                "<p>Erwachsene sollten ab dem 20. Lebensjahr mindestens alle 4&ndash;6 Jahre ein Lipidprofil erstellen lassen und bei Risikofaktoren häufiger.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihre Triglycerid-Ergebnisse zu verstehen",
            body_html=(
                "<p>Ein Lipidprofil mit mehreren Zahlen zu verstehen kann verwirrend sein. <strong>Norya</strong> vereinfacht diesen Prozess: "
                "Laden Sie Ihre Blutergebnisse hoch und erhalten Sie innerhalb von Minuten einen strukturierten, leicht verständlichen "
                "Gesundheitsbericht. Norya analysiert Ihre Triglyceride zusammen mit Cholesterinfraktionen, Glukose und anderen Markern.</p>"
                "<p>Der Bericht hebt hervor, welche Werte außerhalb des Normalbereichs liegen, erklärt ihre Bedeutung in einfacher Sprache "
                "und hilft Ihnen, informierte Fragen für Ihren nächsten Arztbesuch vorzubereiten. "
                "<a href=\"/analyze\">Starten Sie Ihre kostenlose Analyse mit Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> '
                'Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Triglycérides élevés : que signifie votre résultat d'analyse de sang ?",
            body_html=(
                "<p>Les <strong>triglycérides</strong> sont le type de graisse (lipide) le plus courant dans l'organisme. Lorsque vous mangez, "
                "le corps convertit les calories dont il n'a pas immédiatement besoin en triglycérides, stockés dans les cellules adipeuses "
                "et libérés comme source d'énergie entre les repas. Un bilan sanguin de routine appelé <em>bilan lipidique</em> mesure les "
                "triglycérides ainsi que le cholestérol total, LDL et HDL.</p>"
                "<p>Si un certain niveau de triglycérides est nécessaire au fonctionnement normal du corps, des triglycérides élevés "
                "&mdash;une condition appelée <strong>hypertriglycéridémie</strong>&mdash; peuvent augmenter significativement le risque "
                "de maladie cardiaque, d'AVC et de pancréatite.</p>"
                "<p>Ce guide est éducatif et ne remplace pas un avis médical. Discutez toujours de vos résultats avec votre médecin.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Que sont les triglycérides ?",
            body_html=(
                "<p>Les triglycérides sont des molécules composées de trois chaînes d'acides gras liées à un squelette de glycérol. Après un repas, "
                "les intestins absorbent les graisses alimentaires et les conditionnent en lipoprotéines appelées <strong>chylomicrons</strong>. "
                "Le foie produit également des triglycérides à partir de l'excès de glucides et les conditionne en <strong>lipoprotéines de très "
                "basse densité (VLDL)</strong>.</p>"
                "<p>L'enzyme <strong>lipoprotéine lipase</strong> sur les parois des vaisseaux sanguins décompose les triglycérides pour que les "
                "acides gras puissent entrer dans les cellules musculaires ou le tissu adipeux. Lorsque l'apport calorique dépasse constamment "
                "les dépenses, le foie augmente la production de VLDL et les triglycérides sanguins augmentent.</p>"
                "<p>Les niveaux de triglycérides étant fortement influencés par l'alimentation récente, votre médecin vous demandera généralement "
                "de jeûner 9&ndash;12 heures avant le prélèvement.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs de référence des triglycérides",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Catégorie</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">À jeun (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">À jeun (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Limite haute</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Élevé</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,3 &ndash; 5,6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Très élevé</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5,6</td></tr>'
                "</tbody></table>"
                "<p>Un taux optimal de triglycérides est inférieur à 100&nbsp;mg/dL. Les niveaux limites nécessitent des modifications du mode de vie. "
                "Les niveaux très élevés (&ge;500&nbsp;mg/dL) nécessitent une attention urgente en raison du risque de pancréatite aiguë.</p>"
                "<p>Les triglycérides peuvent fluctuer de 20&ndash;30% d'un jour à l'autre. Une mesure unique doit être confirmée par un test de contrôle.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Causes des triglycérides élevés",
            body_html=(
                "<p>Les triglycérides élevés peuvent résulter de facteurs liés au mode de vie, de conditions médicales, de médicaments ou d'une prédisposition génétique :</p>"
                "<p><strong>Facteurs liés au mode de vie :</strong></p>"
                "<ul>"
                "<li><strong>Apport calorique excessif</strong> &ndash; augmente la production hépatique de VLDL.</li>"
                "<li><strong>Glucides raffinés et sucres ajoutés</strong> &ndash; stimulent la lipogenèse de novo hépatique.</li>"
                "<li><strong>Excès d'alcool</strong> &ndash; favorise la synthèse hépatique des triglycérides.</li>"
                "<li><strong>Sédentarité</strong> &ndash; réduit l'activité de la lipoprotéine lipase.</li>"
                "<li><strong>Obésité</strong> &ndash; l'adiposité viscérale est fortement corrélée à l'hypertriglycéridémie.</li>"
                "</ul>"
                "<p><strong>Conditions médicales :</strong> diabète de type 2, hypothyroïdie, insuffisance rénale chronique, syndrome néphrotique "
                "et facteurs génétiques. <strong>Médicaments :</strong> bêta-bloquants, diurétiques thiazidiques, corticostéroïdes, œstrogènes oraux.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglycérides vs. cholestérol : comprendre la différence",
            body_html=(
                "<p>Les <strong>triglycérides</strong> servent au stockage et à la libération d'énergie. Le <strong>cholestérol</strong> est un composant "
                "structurel des membranes cellulaires et un précurseur d'hormones, d'acides biliaires et de vitamine D.</p>"
                "<p>Le bilan lipidique comprend : <strong>cholestérol total</strong>, <strong>LDL</strong> (&laquo; mauvais &raquo;) et "
                "<strong>HDL</strong> (&laquo; bon &raquo;). Pour en savoir plus, consultez nos guides sur "
                '<a href="/fr/blog/taux-de-ldl-cholesterol">le LDL</a> et '
                '<a href="/fr/blog/ldl-vs-hdl-what-it-means">LDL vs HDL</a>. '
                "Dans une approche clinique, on interprète souvent aussi <a href=\"/fr/blog/signification-apob\">l&rsquo;ApoB</a> et "
                "<a href=\"/fr/blog/signification-lpa\">le Lp(a)</a> avec les triglycérides pour estimer la charge en particules athérogènes et le risque héréditaire.</p>"
                "<p>Les triglycérides élevés coexistent fréquemment avec un <em>HDL bas</em> et des <em>particules LDL petites et denses</em>&mdash;"
                "la <strong>triade lipidique athérogène</strong>. Ce profil est particulièrement dangereux car les petites particules LDL denses "
                "pénètrent plus facilement dans les parois artérielles, accélérant l'athérosclérose.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Triglycérides et risque cardiovasculaire",
            body_html=(
                "<p>De vastes études génétiques (randomisation mendélienne) ont confirmé que les <strong>lipoprotéines riches en triglycérides "
                "sont un facteur causal indépendant des maladies cardiovasculaires athérosclérotiques</strong>.</p>"
                "<p>Les triglycérides élevés favorisent un état prothrombotique. Des niveaux très élevés (&ge;500&nbsp;mg/dL) comportent le risque "
                "grave de <strong>pancréatite aiguë</strong>.</p>"
                "<p>La combinaison de triglycérides élevés avec les éléments du <strong>syndrome métabolique</strong>&mdash;obésité abdominale, "
                "hypertension, glycémie à jeun élevée et HDL bas&mdash;crée une augmentation synergique du risque cardiovasculaire.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Modifications du mode de vie et de l'alimentation pour réduire les triglycérides",
            body_html=(
                "<p>Les modifications du mode de vie sont la pierre angulaire de la gestion des triglycérides et peuvent réduire les niveaux de 20&ndash;50% :</p>"
                "<ul>"
                "<li><strong>Réduire les glucides raffinés et les sucres ajoutés</strong> &ndash; limiter le pain blanc, les pâtes, les sucreries et les boissons sucrées.</li>"
                "<li><strong>Limiter ou supprimer l'alcool</strong> &ndash; même de petites quantités peuvent élever les triglycérides.</li>"
                "<li><strong>Augmenter les apports en oméga-3</strong> &ndash; poissons gras (saumon, maquereau, sardines).</li>"
                "<li><strong>Choisir des graisses saines</strong> &ndash; remplacer les graisses saturées par des graisses mono-insaturées (huile d'olive, avocat).</li>"
                "<li><strong>Faire de l'exercice régulièrement</strong> &ndash; au moins 150 minutes par semaine d'activité aérobie modérée.</li>"
                "<li><strong>Perdre le poids excédentaire</strong> &ndash; une perte de 5&ndash;10% peut réduire les triglycérides de 20% ou plus.</li>"
                "</ul>"
                "<p>Un régime méditerranéen riche en légumes, fruits, céréales complètes, légumineuses, poisson et huile d'olive s'est avéré "
                "efficace pour réduire les triglycérides et améliorer la santé cardiovasculaire.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Médicaments pour les triglycérides élevés",
            body_html=(
                "<p>Lorsque les modifications du mode de vie ne suffisent pas, votre médecin peut envisager des médicaments :</p>"
                "<ul>"
                "<li><strong>Fibrates (fénofibrate, gemfibrozil)</strong> &ndash; réduisent les triglycérides de 30&ndash;50%.</li>"
                "<li><strong>Oméga-3 sur ordonnance (icosapent éthyl)</strong> &ndash; l'étude REDUCE-IT a montré une réduction des événements cardiovasculaires.</li>"
                "<li><strong>Statines</strong> &ndash; réduisent modestement les triglycérides de 10&ndash;20%.</li>"
                "<li><strong>Niacine</strong> &ndash; réduit les triglycérides de 20&ndash;35%, mais moins utilisée en raison d'effets secondaires.</li>"
                "</ul>"
                "<p>Pour les patients avec des triglycérides très élevés (&ge;500&nbsp;mg/dL), le traitement est urgent pour prévenir la pancréatite aiguë.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin",
            body_html=(
                "<p>Consultez votre médecin dans les situations suivantes :</p>"
                "<ul>"
                "<li>Triglycérides à jeun <strong>supérieurs à 150&nbsp;mg/dL</strong> à deux reprises ou plus.</li>"
                "<li>Triglycérides entre <strong>200&ndash;499&nbsp;mg/dL</strong>.</li>"
                "<li>Triglycérides <strong>&ge;500&nbsp;mg/dL</strong>&mdash;urgence médicale.</li>"
                "<li>Signes de <strong>syndrome métabolique</strong>.</li>"
                "<li><strong>Douleurs abdominales sévères</strong> avec triglycérides très élevés.</li>"
                "</ul>"
                "<p>Les adultes devraient faire un bilan lipidique au moins tous les 4&ndash;6 ans à partir de 20 ans, et plus fréquemment en présence de facteurs de risque.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre vos résultats de triglycérides",
            body_html=(
                "<p>Comprendre un bilan lipidique avec de multiples chiffres peut être déroutant. <strong>Norya</strong> simplifie le processus : "
                "téléchargez vos résultats d'analyses sanguines et recevez en quelques minutes un rapport de santé structuré et facile à comprendre.</p>"
                "<p>Le rapport met en évidence les valeurs en dehors des normes, explique leur signification en langage clair et vous aide à préparer "
                "des questions éclairées pour votre prochaine consultation. "
                "<a href=\"/analyze\">Commencez votre analyse gratuite avec Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> '
                'Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Trigliceridi alti: cosa significa il risultato delle analisi del sangue",
            body_html=(
                "<p>I <strong>trigliceridi</strong> sono il tipo di grasso (lipide) più comune nell'organismo. Quando si mangia, il corpo converte "
                "le calorie non immediatamente necessarie in trigliceridi, che vengono immagazzinati nelle cellule adipose e rilasciati come "
                "energia tra i pasti. Un esame del sangue di routine chiamato <em>profilo lipidico</em> misura i trigliceridi insieme a colesterolo "
                "totale, LDL e HDL per valutare il rischio cardiovascolare.</p>"
                "<p>Sebbene un certo livello di trigliceridi sia necessario per il normale funzionamento corporeo, i trigliceridi elevati&mdash;"
                "una condizione chiamata <strong>ipertrigliceridemia</strong>&mdash;possono aumentare significativamente il rischio di malattie "
                "cardiache, ictus e pancreatite.</p>"
                "<p>Questa guida è educativa e non sostituisce il parere medico. Discutete sempre i risultati con il vostro medico.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Cosa sono i trigliceridi?",
            body_html=(
                "<p>I trigliceridi sono molecole composte da tre catene di acidi grassi legate a uno scheletro di glicerolo. Dopo un pasto, "
                "l'intestino assorbe i grassi alimentari e li confeziona in lipoproteine chiamate <strong>chilomicroni</strong>. Il fegato produce "
                "anche trigliceridi dai carboidrati in eccesso e li confeziona in <strong>lipoproteine a bassissima densità (VLDL)</strong>.</p>"
                "<p>L'enzima <strong>lipoproteina lipasi</strong> sulle pareti dei vasi sanguigni scompone i trigliceridi affinché gli acidi grassi "
                "possano entrare nelle cellule muscolari (per energia) o nel tessuto adiposo (per immagazzinamento). Quando l'apporto calorico "
                "supera costantemente il dispendio, il fegato aumenta la produzione di VLDL e i trigliceridi nel sangue aumentano.</p>"
                "<p>Poiché i livelli di trigliceridi sono fortemente influenzati dall'assunzione recente di cibo, il medico chiederà "
                "generalmente un digiuno di 9&ndash;12 ore prima del prelievo.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Intervalli di riferimento dei trigliceridi",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Categoria</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">A digiuno (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">A digiuno (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normale</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Limite alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7 &ndash; 2,2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,3 &ndash; 5,6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Molto alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5,6</td></tr>'
                "</tbody></table>"
                "<p>Un livello ottimale di trigliceridi è inferiore a 100&nbsp;mg/dL. I livelli molto alti (&ge;500&nbsp;mg/dL) richiedono "
                "attenzione urgente per il rischio di pancreatite acuta.</p>"
                "<p>I trigliceridi possono fluttuare del 20&ndash;30% da un giorno all'altro. Un singolo valore deve essere confermato con un test di controllo.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Cause dei trigliceridi alti",
            body_html=(
                "<p>I trigliceridi elevati possono derivare da fattori legati allo stile di vita, condizioni mediche, farmaci o predisposizione genetica:</p>"
                "<p><strong>Fattori legati allo stile di vita:</strong></p>"
                "<ul>"
                "<li><strong>Apporto calorico eccessivo</strong> &ndash; aumenta la produzione epatica di VLDL.</li>"
                "<li><strong>Carboidrati raffinati e zuccheri aggiunti</strong> &ndash; stimolano la lipogenesi de novo epatica.</li>"
                "<li><strong>Eccesso di alcol</strong> &ndash; promuove la sintesi epatica di trigliceridi.</li>"
                "<li><strong>Sedentarietà</strong> &ndash; riduce l'attività della lipoproteina lipasi.</li>"
                "<li><strong>Obesità</strong> &ndash; l'adiposità viscerale è fortemente correlata all'ipertrigliceridemia.</li>"
                "</ul>"
                "<p><strong>Condizioni mediche:</strong> diabete di tipo 2, ipotiroidismo, insufficienza renale cronica, sindrome nefrosica "
                "e fattori genetici. <strong>Farmaci:</strong> beta-bloccanti, diuretici tiazidici, corticosteroidi, estrogeni orali.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Trigliceridi vs. colesterolo: capire la differenza",
            body_html=(
                "<p>I <strong>trigliceridi</strong> servono per lo stoccaggio e il rilascio di energia. Il <strong>colesterolo</strong> è un componente "
                "strutturale delle membrane cellulari e precursore di ormoni, acidi biliari e vitamina D.</p>"
                "<p>Nel profilo lipidico si trovano: <strong>colesterolo totale</strong>, <strong>LDL</strong> (&ldquo;cattivo&rdquo;) e "
                "<strong>HDL</strong> (&ldquo;buono&rdquo;). Per approfondire, consultate le nostre guide su "
                '<a href="/it/blog/valori-ldl-colesterolo">LDL</a> e '
                '<a href="/it/blog/ldl-vs-hdl-what-it-means">LDL vs HDL</a>. '
                "In ambito clinico si considerano spesso anche <a href=\"/it/blog/significato-apob\">ApoB</a> e "
                "<a href=\"/it/blog/significato-lpa\">Lp(a)</a> insieme ai trigliceridi per valutare il carico di particelle aterogene e il contesto di rischio ereditario.</p>"
                "<p>I trigliceridi alti coesistono frequentemente con <em>HDL basso</em> e <em>particelle LDL piccole e dense</em>&mdash;"
                "la <strong>triade lipidica aterogenica</strong>. Questo profilo è particolarmente pericoloso.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Trigliceridi e rischio cardiovascolare",
            body_html=(
                "<p>Ampi studi genetici (randomizzazione mendeliana) hanno confermato che le <strong>lipoproteine ricche di trigliceridi sono "
                "un fattore causale indipendente per le malattie cardiovascolari aterosclerotiche</strong>.</p>"
                "<p>I trigliceridi elevati favoriscono uno stato protrombotico. Livelli molto alti (&ge;500&nbsp;mg/dL) comportano il rischio "
                "grave di <strong>pancreatite acuta</strong>.</p>"
                "<p>La combinazione di trigliceridi alti con gli elementi della <strong>sindrome metabolica</strong>&mdash;obesità addominale, "
                "ipertensione, glicemia a digiuno elevata e HDL basso&mdash;crea un aumento sinergico del rischio cardiovascolare.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Modifiche dello stile di vita e della dieta per ridurre i trigliceridi",
            body_html=(
                "<p>Le modifiche dello stile di vita sono il pilastro della gestione dei trigliceridi e possono ridurre i livelli del 20&ndash;50%:</p>"
                "<ul>"
                "<li><strong>Ridurre i carboidrati raffinati e gli zuccheri aggiunti</strong> &ndash; limitare pane bianco, pasta, dolci e bevande zuccherate.</li>"
                "<li><strong>Limitare o eliminare l'alcol</strong> &ndash; anche piccole quantità possono innalzare significativamente i trigliceridi.</li>"
                "<li><strong>Aumentare l'assunzione di omega-3</strong> &ndash; pesci grassi (salmone, sgombro, sardine).</li>"
                "<li><strong>Scegliere grassi sani</strong> &ndash; sostituire i grassi saturi con monoinsaturi (olio d'oliva, avocado).</li>"
                "<li><strong>Fare esercizio regolarmente</strong> &ndash; almeno 150 minuti a settimana di attività aerobica moderata.</li>"
                "<li><strong>Perdere il peso in eccesso</strong> &ndash; anche un calo del 5&ndash;10% può ridurre i trigliceridi del 20% o più.</li>"
                "</ul>"
                "<p>Una dieta mediterranea ricca di verdure, frutta, cereali integrali, legumi, pesce e olio d'oliva si è dimostrata efficace "
                "nel ridurre i trigliceridi e migliorare la salute cardiovascolare.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Farmaci per i trigliceridi alti",
            body_html=(
                "<p>Quando le modifiche dello stile di vita non bastano, il medico può considerare farmaci:</p>"
                "<ul>"
                "<li><strong>Fibrati (fenofibrato, gemfibrozil)</strong> &ndash; riducono i trigliceridi del 30&ndash;50%.</li>"
                "<li><strong>Omega-3 su prescrizione (icosapent etile)</strong> &ndash; lo studio REDUCE-IT ha dimostrato una riduzione degli eventi cardiovascolari.</li>"
                "<li><strong>Statine</strong> &ndash; riducono moderatamente i trigliceridi del 10&ndash;20%.</li>"
                "<li><strong>Niacina</strong> &ndash; riduce i trigliceridi del 20&ndash;35%, ma meno utilizzata per gli effetti collaterali.</li>"
                "</ul>"
                "<p>Per pazienti con trigliceridi molto alti (&ge;500&nbsp;mg/dL), il trattamento è urgente per prevenire la pancreatite acuta.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico",
            body_html=(
                "<p>Consultate il vostro medico nelle seguenti situazioni:</p>"
                "<ul>"
                "<li>Trigliceridi a digiuno <strong>superiori a 150&nbsp;mg/dL</strong> in due o più occasioni.</li>"
                "<li>Trigliceridi tra <strong>200&ndash;499&nbsp;mg/dL</strong>.</li>"
                "<li>Trigliceridi <strong>&ge;500&nbsp;mg/dL</strong>&mdash;urgenza medica.</li>"
                "<li>Segni di <strong>sindrome metabolica</strong>.</li>"
                "<li><strong>Forte dolore addominale</strong> con trigliceridi molto alti.</li>"
                "</ul>"
                "<p>Gli adulti dovrebbero effettuare un profilo lipidico almeno ogni 4&ndash;6 anni a partire dai 20 anni.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a capire i risultati dei trigliceridi",
            body_html=(
                "<p>Capire un profilo lipidico con più numeri può essere confuso. <strong>Norya</strong> semplifica il processo: caricate i vostri "
                "risultati delle analisi del sangue e ricevete in pochi minuti un report sanitario strutturato e facile da comprendere.</p>"
                "<p>Il report evidenzia i valori fuori norma, spiega il loro significato in un linguaggio chiaro e vi aiuta a preparare domande "
                "informate per la prossima visita. <a href=\"/analyze\">Iniziate l'analisi gratuita con Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> '
                'Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="טריגליצרידים גבוהים: מה המשמעות של תוצאת בדיקת הדם שלך",
            body_html=(
                "<p><strong>טריגליצרידים</strong> הם סוג השומן (ליפיד) הנפוץ ביותר בגוף. כאשר אתם אוכלים, הגוף ממיר קלוריות שאינן נחוצות "
                "באופן מיידי לטריגליצרידים, המאוחסנים בתאי שומן ומשתחררים כאנרגיה בין הארוחות. בדיקת דם שגרתית הנקראת <em>פרופיל שומנים</em> "
                "מודדת טריגליצרידים יחד עם כולסטרול כללי, LDL ו-HDL כדי להעריך את פרופיל הסיכון הקרדיווסקולרי שלכם.</p>"
                "<p>בעוד שרמה מסוימת של טריגליצרידים נחוצה לתפקוד תקין של הגוף, טריגליצרידים גבוהים&mdash;מצב הנקרא "
                "<strong>היפרטריגליצרידמיה</strong>&mdash;עלולים להגביר משמעותית את הסיכון למחלות לב, שבץ מוחי ודלקת הלבלב.</p>"
                "<p>מדריך זה הוא חינוכי ואינו מחליף ייעוץ רפואי. דונו תמיד בתוצאות עם הרופא שלכם.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="מהם טריגליצרידים?",
            body_html=(
                "<p>טריגליצרידים הם מולקולות המורכבות משלוש שרשראות חומצות שומן המחוברות לשלד גליצרול. לאחר ארוחה, המעיים סופגים "
                "שומנים מהמזון ואורזים אותם בליפופרוטאינים הנקראים <strong>כילומיקרונים</strong>. הכבד גם מייצר טריגליצרידים "
                "מעודף פחמימות ואורז אותם ב-<strong>VLDL</strong>.</p>"
                "<p>האנזים <strong>ליפופרוטאין ליפאז</strong> על דפנות כלי הדם מפרק טריגליצרידים כדי שחומצות שומן יוכלו להיכנס "
                "לתאי שריר (לאנרגיה) או לרקמת שומן (לאחסון). כאשר צריכת הקלוריות עולה באופן עקבי על ההוצאה, הכבד מגביר את ייצור "
                "ה-VLDL ורמות הטריגליצרידים בדם עולות.</p>"
                "<p>מכיוון שרמות טריגליצרידים מושפעות מאוד ממזון שנצרך לאחרונה, הרופא ידרוש בדרך כלל צום של 9&ndash;12 שעות לפני "
                "נטילת הדגימה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ייחוס לטריגליצרידים",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קטגוריה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">בצום (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">בצום (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">תקין</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גבולי-גבוה</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גבוה</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.3 &ndash; 5.6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גבוה מאוד</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5.6</td></tr>'
                "</tbody></table>"
                "<p>רמה אופטימלית של טריגליצרידים היא מתחת ל-100 mg/dL. רמות גבוהות מאוד (&ge;500 mg/dL) דורשות טיפול דחוף "
                "בגלל סיכון לדלקת לבלב חריפה.</p>"
                "<p>טריגליצרידים יכולים להשתנות ב-20&ndash;30% מיום ליום. מדידה בודדת צריכה להיות מאושרת בבדיקה חוזרת.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="גורמים לטריגליצרידים גבוהים",
            body_html=(
                "<p>טריגליצרידים גבוהים יכולים לנבוע מגורמי אורח חיים, מצבים רפואיים, תרופות או נטייה גנטית:</p>"
                "<p><strong>גורמי אורח חיים:</strong></p>"
                "<ul>"
                "<li><strong>צריכת קלוריות מופרזת</strong> &ndash; מגבירה ייצור VLDL בכבד.</li>"
                "<li><strong>צריכת פחמימות מזוקקות וסוכרים</strong> &ndash; מעוררת ליפוגנזה דה-נובו בכבד.</li>"
                "<li><strong>צריכת אלכוהול מופרזת</strong> &ndash; מקדמת סינתזת טריגליצרידים.</li>"
                "<li><strong>חוסר פעילות גופנית</strong> &ndash; מפחית פעילות ליפופרוטאין ליפאז.</li>"
                "<li><strong>השמנה</strong> &ndash; במיוחד שומן ויסצרלי קשור מאוד להיפרטריגליצרידמיה.</li>"
                "</ul>"
                "<p><strong>מצבים רפואיים:</strong> סוכרת סוג 2, תת-פעילות בלוטת התריס, מחלת כליות כרונית, תסמונת נפרוטית "
                "וגורמים גנטיים. <strong>תרופות:</strong> חוסמי בטא, משתני תיאזיד, קורטיקוסטרואידים, אסטרוגנים.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="טריגליצרידים לעומת כולסטרול: הבנת ההבדל",
            body_html=(
                "<p><strong>טריגליצרידים</strong> משמשים לאגירה ושחרור אנרגיה. <strong>כולסטרול</strong> הוא מרכיב מבני של ממברנות "
                "תאים ומקדים להורמונים, חומצות מרה וויטמין D.</p>"
                "<p>בפרופיל שומנים תמצאו: <strong>כולסטרול כללי</strong>, <strong>LDL</strong> (&ldquo;רע&rdquo;) ו-<strong>HDL</strong> "
                "(&ldquo;טוב&rdquo;). למידע נוסף, ראו את המדריכים שלנו בנושא "
                '<a href="/he/blog/ldl-cholesterol-target">כולסטרול LDL</a> ו-'
                '<a href="/he/blog/ldl-vs-hdl-what-it-means">LDL מול HDL</a>. '
                "בהקשר קליני משקללים לעתים קרובות גם "
                '<a href="/he/blog/פירוש-apob">ApoB</a> ו-'
                '<a href="/he/blog/פירוש-lpa">Lp(a)</a> יחד עם טריגליצרידים בעומס חלקיקים אתרוגניים והקשר סיכון תורשתי.</p>'
                "<p>טריגליצרידים גבוהים מתקיימים לעתים קרובות יחד עם <em>HDL נמוך</em> ו-<em>חלקיקי LDL קטנים וצפופים</em>&mdash;"
                "<strong>השלישיה הליפידית האתרוגנית</strong>. דפוס זה מסוכן במיוחד.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="טריגליצרידים וסיכון קרדיווסקולרי",
            body_html=(
                "<p>מחקרים גנטיים גדולים (רנדומיזציה מנדליאנית) אישרו ש<strong>ליפופרוטאינים עשירים בטריגליצרידים הם גורם סיבתי "
                "עצמאי למחלות קרדיווסקולריות טרשתיות</strong>.</p>"
                "<p>טריגליצרידים גבוהים מקדמים מצב פרותרומבוטי. רמות גבוהות מאוד (&ge;500 mg/dL) נושאות סיכון חמור "
                "ל<strong>דלקת לבלב חריפה</strong>.</p>"
                "<p>השילוב של טריגליצרידים גבוהים עם מרכיבי <strong>התסמונת המטבולית</strong>&mdash;השמנה מרכזית, לחץ דם גבוה, "
                "גלוקוז בצום מוגבר ו-HDL נמוך&mdash;יוצר עלייה סינרגטית בסיכון הקרדיווסקולרי.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="שינויים באורח חיים ובתזונה להורדת טריגליצרידים",
            body_html=(
                "<p>שינוי אורח חיים הוא אבן הפינה בניהול טריגליצרידים ויכול להפחית רמות ב-20&ndash;50%:</p>"
                "<ul>"
                "<li><strong>הפחתת פחמימות מזוקקות וסוכרים מוספים</strong></li>"
                "<li><strong>הגבלה או הימנעות מאלכוהול</strong></li>"
                "<li><strong>הגדלת צריכת אומגה-3</strong> &ndash; דגים שומניים (סלמון, מקרל, סרדינים).</li>"
                "<li><strong>בחירת שומנים בריאים</strong> &ndash; שמן זית, אבוקדו, אגוזים.</li>"
                "<li><strong>פעילות גופנית סדירה</strong> &ndash; 150 דקות בשבוע לפחות.</li>"
                "<li><strong>ירידה במשקל</strong> &ndash; אפילו 5&ndash;10% עשויים להוריד טריגליצרידים ב-20% ומעלה.</li>"
                "</ul>"
                "<p>דיאטה ים-תיכונית הדגישה ירקות, פירות, דגנים מלאים, קטניות, דגים ושמן זית הוכחה כיעילה "
                "בהורדת טריגליצרידים ובשיפור בריאות הלב.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="תרופות לטריגליצרידים גבוהים",
            body_html=(
                "<p>כאשר שינויי אורח חיים לבדם אינם מספיקים, הרופא עשוי לשקול תרופות:</p>"
                "<ul>"
                "<li><strong>פיבראטים (פנופיבראט, גמפיברוזיל)</strong> &ndash; מורידים טריגליצרידים ב-30&ndash;50%.</li>"
                "<li><strong>אומגה-3 במרשם (איקוספנט אתיל)</strong> &ndash; מחקר REDUCE-IT הראה הפחתה באירועים קרדיווסקולריים.</li>"
                "<li><strong>סטטינים</strong> &ndash; מורידים טריגליצרידים באופן מתון ב-10&ndash;20%.</li>"
                "<li><strong>ניאצין</strong> &ndash; מוריד טריגליצרידים ב-20&ndash;35% אך פחות בשימוש בשל תופעות לוואי.</li>"
                "</ul>"
                "<p>למטופלים עם טריגליצרידים גבוהים מאוד (&ge;500 mg/dL), הטיפול דחוף למניעת דלקת לבלב חריפה.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא",
            body_html=(
                "<p>פנו לרופא במצבים הבאים:</p>"
                "<ul>"
                "<li>טריגליצרידים בצום <strong>מעל 150 mg/dL</strong> בשתי בדיקות או יותר.</li>"
                "<li>טריגליצרידים <strong>200&ndash;499 mg/dL</strong>.</li>"
                "<li>טריגליצרידים <strong>&ge;500 mg/dL</strong>&mdash;דחיפות רפואית.</li>"
                "<li>סימנים של <strong>תסמונת מטבולית</strong>.</li>"
                "<li><strong>כאבי בטן חזקים</strong> עם טריגליצרידים גבוהים מאוד.</li>"
                "</ul>"
                "<p>מבוגרים צריכים לבצע פרופיל שומנים לפחות כל 4&ndash;6 שנים מגיל 20, ולעתים קרובות יותר אם יש גורמי סיכון.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד Norya עוזרת לך להבין את תוצאות הטריגליצרידים",
            body_html=(
                "<p>הבנת פרופיל שומנים עם מספרים רבים עלולה להיות מבלבלת. <strong>Norya</strong> מפשטת את התהליך: העלו את תוצאות "
                "בדיקת הדם שלכם וקבלו תוך דקות דוח בריאות מובנה וקל להבנה.</p>"
                "<p>הדוח מדגיש אילו ערכים חורגים מהנורמה, מסביר את משמעותם בשפה פשוטה ועוזר לכם להכין שאלות מושכלות "
                "לביקור הבא אצל הרופא. <a href=\"/analyze\">התחילו ניתוח חינמי עם Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הודעה",
            body_html=(
                '<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> '
                'דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="उच्च ट्राइग्लिसराइड्स: आपकी रक्त जांच के परिणाम का क्या अर्थ है",
            body_html=(
                "<p><strong>ट्राइग्लिसराइड्स</strong> शरीर में सबसे आम प्रकार की वसा (लिपिड) हैं। जब आप खाना खाते हैं, तो शरीर उन कैलोरी को "
                "जिनकी तुरंत आवश्यकता नहीं होती, ट्राइग्लिसराइड्स में बदल देता है जो वसा कोशिकाओं में संग्रहित होती हैं और भोजन के बीच ऊर्जा "
                "के लिए मुक्त की जाती हैं। <em>लिपिड पैनल</em> नामक नियमित रक्त परीक्षण ट्राइग्लिसराइड्स को कुल कोलेस्ट्रॉल, LDL और HDL "
                "के साथ मापता है।</p>"
                "<p>जबकि ट्राइग्लिसराइड्स का एक निश्चित स्तर सामान्य शारीरिक कार्य के लिए आवश्यक है, उच्च ट्राइग्लिसराइड्स&mdash;"
                "<strong>हाइपरट्राइग्लिसराइडिमिया</strong>&mdash;हृदय रोग, स्ट्रोक और अग्नाशयशोथ के जोखिम को काफी बढ़ा सकते हैं।</p>"
                "<p>यह मार्गदर्शिका शैक्षिक है और चिकित्सा सलाह का विकल्प नहीं है। हमेशा अपने परिणामों पर डॉक्टर से चर्चा करें।</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="ट्राइग्लिसराइड्स क्या हैं?",
            body_html=(
                "<p>ट्राइग्लिसराइड्स तीन फैटी एसिड श्रृंखलाओं से बने अणु हैं जो ग्लिसरॉल रीढ़ से जुड़े होते हैं। भोजन के बाद, आंतें "
                "आहार वसा को अवशोषित करती हैं और उन्हें <strong>काइलोमाइक्रॉन</strong> नामक लिपोप्रोटीन में पैक करती हैं। यकृत भी "
                "अतिरिक्त कार्बोहाइड्रेट से ट्राइग्लिसराइड्स बनाता है और उन्हें <strong>VLDL</strong> में पैक करता है।</p>"
                "<p>रक्त वाहिका की दीवारों पर मौजूद <strong>लिपोप्रोटीन लाइपेज</strong> एंजाइम ट्राइग्लिसराइड्स को तोड़ता है ताकि "
                "फैटी एसिड मांसपेशी कोशिकाओं (ऊर्जा के लिए) या वसा ऊतक (भंडारण के लिए) में प्रवेश कर सकें। जब कैलोरी की खपत "
                "लगातार खर्च से अधिक होती है, तो यकृत VLDL उत्पादन बढ़ाता है।</p>"
                "<p>चूंकि ट्राइग्लिसराइड स्तर हाल के भोजन से बहुत प्रभावित होता है, इसलिए डॉक्टर आमतौर पर लिपिड पैनल से पहले "
                "9&ndash;12 घंटे का उपवास कराते हैं।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ट्राइग्लिसराइड संदर्भ सीमाएँ",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">श्रेणी</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">उपवास स्तर (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">उपवास स्तर (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">सामान्य</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">सीमावर्ती उच्च</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">उच्च</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.3 &ndash; 5.6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">बहुत उच्च</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5.6</td></tr>'
                "</tbody></table>"
                "<p>ट्राइग्लिसराइड्स का इष्टतम स्तर 100 mg/dL से कम है। बहुत उच्च स्तर (&ge;500 mg/dL) को तीव्र अग्नाशयशोथ "
                "के जोखिम के कारण तत्काल ध्यान देने की आवश्यकता होती है।</p>"
                "<p>ट्राइग्लिसराइड स्तर दिन-प्रतिदिन 20&ndash;30% तक उतार-चढ़ाव कर सकते हैं। एक माप की पुष्टि दोहराव परीक्षण से की जानी चाहिए।</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="उच्च ट्राइग्लिसराइड्स के कारण",
            body_html=(
                "<p>उच्च ट्राइग्लिसराइड्स जीवनशैली कारकों, अंतर्निहित चिकित्सा स्थितियों, दवाओं या आनुवंशिक प्रवृत्ति से हो सकते हैं:</p>"
                "<p><strong>जीवनशैली और आहार कारक:</strong></p>"
                "<ul>"
                "<li><strong>अत्यधिक कैलोरी सेवन</strong> &ndash; यकृत द्वारा VLDL उत्पादन बढ़ाता है।</li>"
                "<li><strong>परिष्कृत कार्बोहाइड्रेट और चीनी</strong> &ndash; यकृत में डी-नोवो लिपोजेनेसिस को उत्तेजित करते हैं।</li>"
                "<li><strong>अत्यधिक शराब का सेवन</strong> &ndash; ट्राइग्लिसराइड संश्लेषण को बढ़ावा देता है।</li>"
                "<li><strong>गतिहीन जीवनशैली</strong> &ndash; लिपोप्रोटीन लाइपेज गतिविधि कम करता है।</li>"
                "<li><strong>मोटापा</strong> &ndash; विशेष रूप से आंत की वसा हाइपरट्राइग्लिसराइडिमिया से जुड़ी है।</li>"
                "</ul>"
                "<p><strong>चिकित्सा स्थितियाँ:</strong> टाइप 2 मधुमेह, हाइपोथायरायडिज्म, क्रोनिक किडनी रोग, नेफ्रोटिक सिंड्रोम "
                "और आनुवंशिक कारक। <strong>दवाएँ:</strong> बीटा-ब्लॉकर्स, थियाजाइड मूत्रवर्धक, कॉर्टिकोस्टेरॉइड्स, मौखिक एस्ट्रोजन।</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="ट्राइग्लिसराइड्स बनाम कोलेस्ट्रॉल: अंतर समझना",
            body_html=(
                "<p><strong>ट्राइग्लिसराइड्स</strong> ऊर्जा भंडारण और विमोचन के लिए उपयोग किए जाते हैं। <strong>कोलेस्ट्रॉल</strong> "
                "कोशिका झिल्ली का संरचनात्मक घटक है और हार्मोन, पित्त अम्ल और विटामिन D का अग्रदूत है।</p>"
                "<p>लिपिड पैनल में आपको मिलेगा: <strong>कुल कोलेस्ट्रॉल</strong>, <strong>LDL</strong> (&ldquo;खराब&rdquo;) और "
                "<strong>HDL</strong> (&ldquo;अच्छा&rdquo;)। अधिक जानकारी के लिए "
                '<a href="/hi/blog/ldl-cholesterol-kitna-hona-chahiye">LDL कोलेस्ट्रॉल</a> और '
                '<a href="/hi/blog/ldl-vs-hdl-what-it-means">LDL बनाम HDL</a> पर हमारी मार्गदर्शिका देखें। '
                "क्लिनिशियन अक्सर ट्राइग्लिसराइड्स के साथ <a href=\"/hi/blog/apob-का-मतलब\">ApoB</a> और "
                "<a href=\"/hi/blog/lpa-का-मतलब\">Lp(a)</a> को भी देखते हैं—एथेरोजेनिक कण बोझ और वंशागत जोखिम संदर्भ में।</p>"
                "<p>उच्च ट्राइग्लिसराइड्स अक्सर <em>कम HDL</em> और <em>छोटे, घने LDL कणों</em> के साथ सह-अस्तित्व में होते हैं&mdash;"
                "<strong>एथेरोजेनिक लिपिड ट्रायड</strong>। यह पैटर्न विशेष रूप से खतरनाक है।</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="ट्राइग्लिसराइड्स और हृदय संबंधी जोखिम",
            body_html=(
                "<p>बड़े पैमाने पर आनुवंशिक अध्ययनों (मेंडेलियन रैंडमाइजेशन) ने पुष्टि की है कि <strong>ट्राइग्लिसराइड-समृद्ध लिपोप्रोटीन "
                "एथेरोस्क्लेरोटिक हृदय रोग के लिए स्वतंत्र रूप से कारक हैं</strong>।</p>"
                "<p>उच्च ट्राइग्लिसराइड्स एक प्रोथ्रोम्बोटिक स्थिति को बढ़ावा देते हैं। बहुत उच्च स्तर (&ge;500 mg/dL) "
                "<strong>तीव्र अग्नाशयशोथ</strong> का गंभीर जोखिम रखते हैं।</p>"
                "<p>उच्च ट्राइग्लिसराइड्स का <strong>मेटाबोलिक सिंड्रोम</strong> के तत्वों&mdash;केंद्रीय मोटापा, उच्च रक्तचाप, "
                "उच्च उपवास ग्लूकोज और कम HDL&mdash;के साथ संयोजन हृदय जोखिम में सहक्रियात्मक वृद्धि पैदा करता है।</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="ट्राइग्लिसराइड्स कम करने के लिए जीवनशैली और आहार में बदलाव",
            body_html=(
                "<p>जीवनशैली में बदलाव ट्राइग्लिसराइड प्रबंधन की आधारशिला है और स्तरों को 20&ndash;50% तक कम कर सकता है:</p>"
                "<ul>"
                "<li><strong>परिष्कृत कार्बोहाइड्रेट और अतिरिक्त चीनी कम करें</strong></li>"
                "<li><strong>शराब सीमित या बंद करें</strong></li>"
                "<li><strong>ओमेगा-3 फैटी एसिड का सेवन बढ़ाएँ</strong> &ndash; वसायुक्त मछली (सैल्मन, मैकेरल, सार्डिन)।</li>"
                "<li><strong>स्वस्थ वसा चुनें</strong> &ndash; जैतून का तेल, एवोकाडो, मेवे।</li>"
                "<li><strong>नियमित व्यायाम करें</strong> &ndash; प्रति सप्ताह कम से कम 150 मिनट मध्यम-तीव्रता वाली एरोबिक गतिविधि।</li>"
                "<li><strong>अतिरिक्त वजन कम करें</strong> &ndash; 5&ndash;10% वजन घटाने से भी ट्राइग्लिसराइड्स 20% या अधिक कम हो सकते हैं।</li>"
                "</ul>"
                "<p>भूमध्यसागरीय शैली का आहार जो सब्जियों, फलों, साबुत अनाज, फलियों, मछली और जैतून के तेल पर जोर देता है, "
                "ट्राइग्लिसराइड्स को प्रभावी ढंग से कम करता है।</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="उच्च ट्राइग्लिसराइड्स के लिए दवाएँ",
            body_html=(
                "<p>जब जीवनशैली में बदलाव अकेले पर्याप्त नहीं होते, तो डॉक्टर दवाओं पर विचार कर सकते हैं:</p>"
                "<ul>"
                "<li><strong>फाइब्रेट्स (फेनोफाइब्रेट, जेमफाइब्रोज़िल)</strong> &ndash; ट्राइग्लिसराइड्स को 30&ndash;50% कम करते हैं।</li>"
                "<li><strong>प्रिस्क्रिप्शन ओमेगा-3 (इकोसापेंट एथिल)</strong> &ndash; REDUCE-IT अध्ययन ने हृदय संबंधी घटनाओं में कमी दिखाई।</li>"
                "<li><strong>स्टैटिन</strong> &ndash; ट्राइग्लिसराइड्स को मामूली रूप से 10&ndash;20% कम करते हैं।</li>"
                "<li><strong>नियासिन</strong> &ndash; 20&ndash;35% कमी लेकिन दुष्प्रभावों के कारण कम उपयोग।</li>"
                "</ul>"
                "<p>बहुत उच्च ट्राइग्लिसराइड्स (&ge;500 mg/dL) वाले रोगियों में तीव्र अग्नाशयशोथ की रोकथाम के लिए उपचार तत्काल है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर को कब दिखाएँ",
            body_html=(
                "<p>निम्नलिखित स्थितियों में अपने ट्राइग्लिसराइड स्तरों के बारे में डॉक्टर से परामर्श करें:</p>"
                "<ul>"
                "<li>उपवास ट्राइग्लिसराइड्स दो या अधिक बार <strong>150 mg/dL से ऊपर</strong>।</li>"
                "<li>ट्राइग्लिसराइड्स <strong>200&ndash;499 mg/dL</strong>।</li>"
                "<li>ट्राइग्लिसराइड्स <strong>&ge;500 mg/dL</strong>&mdash;चिकित्सा आपातकाल।</li>"
                "<li><strong>मेटाबोलिक सिंड्रोम</strong> के संकेत।</li>"
                "<li>बहुत उच्च ट्राइग्लिसराइड्स के साथ <strong>गंभीर पेट दर्द</strong>।</li>"
                "</ul>"
                "<p>वयस्कों को 20 वर्ष की आयु से कम से कम हर 4&ndash;6 वर्षों में लिपिड पैनल करवाना चाहिए।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके ट्राइग्लिसराइड परिणामों को समझने में कैसे मदद करता है",
            body_html=(
                "<p>कई संख्याओं वाले लिपिड पैनल को समझना भ्रमित करने वाला हो सकता है। <strong>Norya</strong> इस प्रक्रिया को सरल बनाता है: "
                "अपनी रक्त जांच के परिणाम अपलोड करें और मिनटों में एक संरचित, समझने में आसान स्वास्थ्य सारांश रिपोर्ट प्राप्त करें।</p>"
                "<p>रिपोर्ट बताती है कि कौन से मान सामान्य सीमा से बाहर हैं, सरल भाषा में उनका अर्थ बताती है और आपकी अगली "
                "डॉक्टर यात्रा की तैयारी में मदद करती है। <a href=\"/analyze\">Norya के साथ मुफ्त विश्लेषण शुरू करें</a>।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> '
                'अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="الدهون الثلاثية المرتفعة: ماذا تعني نتيجة تحليل الدم",
            body_html=(
                "<p><strong>الدهون الثلاثية (الترايجليسرايد)</strong> هي أكثر أنواع الدهون شيوعاً في الجسم. عندما تأكل، يحوّل الجسم "
                "السعرات الحرارية التي لا يحتاجها فوراً إلى دهون ثلاثية تُخزَّن في الخلايا الدهنية وتُطلَق كطاقة بين الوجبات. "
                "تحليل دم روتيني يُسمى <em>صورة الدهون</em> يقيس الدهون الثلاثية مع الكوليسترول الكلي وLDL وHDL لتقييم خطر الإصابة "
                "بأمراض القلب والأوعية الدموية.</p>"
                "<p>في حين أن مستوى معيناً من الدهون الثلاثية ضروري لوظائف الجسم الطبيعية، فإن الدهون الثلاثية المرتفعة&mdash;حالة تُسمى "
                "<strong>فرط ثلاثي غليسيريد الدم</strong>&mdash;يمكن أن تزيد بشكل كبير من خطر أمراض القلب والسكتة الدماغية والتهاب البنكرياس.</p>"
                "<p>هذا الدليل تعليمي ولا يحل محل المشورة الطبية. ناقش دائماً نتائجك مع طبيبك.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="ما هي الدهون الثلاثية؟",
            body_html=(
                "<p>الدهون الثلاثية هي جزيئات تتكون من ثلاث سلاسل أحماض دهنية مرتبطة بهيكل غليسرول. بعد الأكل، تمتص الأمعاء "
                "الدهون الغذائية وتعبئها في بروتينات دهنية تُسمى <strong>الكيلومكرونات</strong>. يُنتج الكبد أيضاً دهوناً ثلاثية من "
                "الكربوهيدرات الزائدة ويعبئها في <strong>بروتينات دهنية منخفضة الكثافة جداً (VLDL)</strong>.</p>"
                "<p>يقوم إنزيم <strong>ليبوبروتين ليباز</strong> على جدران الأوعية الدموية بتكسير الدهون الثلاثية حتى تتمكن "
                "الأحماض الدهنية من الدخول إلى خلايا العضلات (للطاقة) أو الأنسجة الدهنية (للتخزين). عندما يتجاوز استهلاك "
                "السعرات الحرارية الإنفاق باستمرار، يزيد الكبد إنتاج VLDL وترتفع مستويات الدهون الثلاثية في الدم.</p>"
                "<p>نظراً لأن مستويات الدهون الثلاثية تتأثر بشدة بتناول الطعام الأخير، سيطلب طبيبك عادةً صيام 9&ndash;12 ساعة قبل سحب الدم.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="النطاقات المرجعية للدهون الثلاثية",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الفئة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">صائم (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">صائم (mmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">طبيعي</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 1.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">حدّي مرتفع</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 &ndash; 199</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7 &ndash; 2.2</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">مرتفع</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 499</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.3 &ndash; 5.6</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">مرتفع جداً</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 5.6</td></tr>'
                "</tbody></table>"
                "<p>المستوى الأمثل للدهون الثلاثية أقل من 100 mg/dL. المستويات المرتفعة جداً (&ge;500 mg/dL) تتطلب اهتماماً عاجلاً "
                "بسبب خطر التهاب البنكرياس الحاد.</p>"
                "<p>يمكن أن تتقلب الدهون الثلاثية بنسبة 20&ndash;30% من يوم لآخر. يجب تأكيد القياس الواحد بفحص متكرر.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="أسباب ارتفاع الدهون الثلاثية",
            body_html=(
                "<p>يمكن أن تنتج الدهون الثلاثية المرتفعة عن عوامل نمط الحياة أو حالات طبية أو أدوية أو استعداد وراثي:</p>"
                "<p><strong>عوامل نمط الحياة والنظام الغذائي:</strong></p>"
                "<ul>"
                "<li><strong>استهلاك مفرط للسعرات الحرارية</strong> &ndash; يزيد إنتاج الكبد لـ VLDL.</li>"
                "<li><strong>الكربوهيدرات المكررة والسكريات</strong> &ndash; تحفز تكوين الدهون الكبدي.</li>"
                "<li><strong>الإفراط في الكحول</strong> &ndash; يعزز تصنيع الدهون الثلاثية.</li>"
                "<li><strong>نمط الحياة الخامل</strong> &ndash; يقلل نشاط ليبوبروتين ليباز.</li>"
                "<li><strong>السمنة</strong> &ndash; خاصة الدهون الحشوية ترتبط بفرط الدهون الثلاثية.</li>"
                "</ul>"
                "<p><strong>حالات طبية:</strong> السكري من النوع 2، قصور الغدة الدرقية، أمراض الكلى المزمنة، المتلازمة الكلوية "
                "والعوامل الوراثية. <strong>الأدوية:</strong> حاصرات بيتا، مدرات البول الثيازيدية، الكورتيكوستيرويدات، الإستروجينات الفموية.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="الدهون الثلاثية مقابل الكوليسترول: فهم الفرق",
            body_html=(
                "<p><strong>الدهون الثلاثية</strong> تُستخدم لتخزين الطاقة وإطلاقها. <strong>الكوليسترول</strong> مكون بنيوي لأغشية الخلايا "
                "وسلف للهرمونات والأحماض الصفراوية وفيتامين D.</p>"
                "<p>في صورة الدهون ستجد: <strong>الكوليسترول الكلي</strong>، <strong>LDL</strong> (&laquo;السيئ&raquo;) و<strong>HDL</strong> "
                "(&laquo;الجيد&raquo;). لمزيد من المعلومات، راجع أدلتنا حول "
                '<a href="/ar/blog/ldl-cholesterol-normal-range">كوليسترول LDL</a> و'
                '<a href="/ar/blog/ldl-vs-hdl-what-it-means">LDL مقابل HDL</a>. '
                "في السياق السريري يُفسَّر غالباً أيضاً "
                '<a href="/ar/blog/معنى-apob">ApoB</a> و'
                '<a href="/ar/blog/معنى-lpa">Lp(a)</a> مع الدهون الثلاثية عند تقييم عبء الجزيئات المُسَبِّبة للتصلب والخطر الوراثي.</p>'
                "<p>الدهون الثلاثية المرتفعة تتواجد في كثير من الأحيان مع <em>HDL منخفض</em> و<em>جزيئات LDL الصغيرة والكثيفة</em>&mdash;"
                "<strong>الثالوث الدهني المسبب لتصلب الشرايين</strong>. هذا النمط خطير بشكل خاص.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="الدهون الثلاثية ومخاطر القلب والأوعية الدموية",
            body_html=(
                "<p>أكدت الدراسات الجينية الكبيرة (العشوائية المندلية) أن <strong>البروتينات الدهنية الغنية بالدهون الثلاثية هي عامل "
                "سببي مستقل لأمراض القلب والأوعية الدموية التصلبية</strong>.</p>"
                "<p>ارتفاع الدهون الثلاثية يعزز حالة تجلطية. المستويات المرتفعة جداً (&ge;500 mg/dL) تحمل خطر "
                "<strong>التهاب البنكرياس الحاد</strong> الذي قد يهدد الحياة.</p>"
                "<p>الجمع بين الدهون الثلاثية المرتفعة وعناصر <strong>المتلازمة الأيضية</strong>&mdash;السمنة المركزية وارتفاع ضغط الدم "
                "وارتفاع سكر الصيام وانخفاض HDL&mdash;يخلق زيادة تآزرية في مخاطر القلب والأوعية الدموية.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="تغييرات نمط الحياة والنظام الغذائي لخفض الدهون الثلاثية",
            body_html=(
                "<p>تعديل نمط الحياة هو حجر الزاوية في إدارة الدهون الثلاثية ويمكن أن يخفض المستويات بنسبة 20&ndash;50%:</p>"
                "<ul>"
                "<li><strong>تقليل الكربوهيدرات المكررة والسكريات المضافة</strong></li>"
                "<li><strong>تقليل أو إيقاف الكحول</strong></li>"
                "<li><strong>زيادة تناول أوميغا-3</strong> &ndash; الأسماك الدهنية (السلمون، الماكريل، السردين).</li>"
                "<li><strong>اختيار الدهون الصحية</strong> &ndash; زيت الزيتون، الأفوكادو، المكسرات.</li>"
                "<li><strong>ممارسة الرياضة بانتظام</strong> &ndash; 150 دقيقة أسبوعياً على الأقل من النشاط الهوائي المعتدل.</li>"
                "<li><strong>فقدان الوزن الزائد</strong> &ndash; حتى خسارة 5&ndash;10% قد تخفض الدهون الثلاثية بنسبة 20% أو أكثر.</li>"
                "</ul>"
                "<p>نظام البحر الأبيض المتوسط الغذائي الذي يركز على الخضروات والفواكه والحبوب الكاملة والبقوليات والأسماك وزيت الزيتون "
                "أثبت فعاليته في خفض الدهون الثلاثية وتحسين صحة القلب.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="أدوية لارتفاع الدهون الثلاثية",
            body_html=(
                "<p>عندما لا تكفي تغييرات نمط الحياة وحدها، قد يفكر طبيبك في الأدوية:</p>"
                "<ul>"
                "<li><strong>الفيبرات (فينوفيبرات، جمفيبروزيل)</strong> &ndash; تخفض الدهون الثلاثية بنسبة 30&ndash;50%.</li>"
                "<li><strong>أوميغا-3 بوصفة طبية (إيكوسابنت إيثيل)</strong> &ndash; أظهرت دراسة REDUCE-IT تقليل أحداث القلب والأوعية الدموية.</li>"
                "<li><strong>الستاتينات</strong> &ndash; تخفض الدهون الثلاثية بشكل متواضع بنسبة 10&ndash;20%.</li>"
                "<li><strong>النياسين</strong> &ndash; يخفض الدهون الثلاثية بنسبة 20&ndash;35% لكن استخدامه تراجع بسبب الآثار الجانبية.</li>"
                "</ul>"
                "<p>للمرضى الذين لديهم دهون ثلاثية مرتفعة جداً (&ge;500 mg/dL)، العلاج عاجل لمنع التهاب البنكرياس الحاد.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب",
            body_html=(
                "<p>استشر طبيبك في الحالات التالية:</p>"
                "<ul>"
                "<li>الدهون الثلاثية الصائمة <strong>أعلى من 150 mg/dL</strong> في مناسبتين أو أكثر.</li>"
                "<li>الدهون الثلاثية بين <strong>200&ndash;499 mg/dL</strong>.</li>"
                "<li>الدهون الثلاثية <strong>&ge;500 mg/dL</strong>&mdash;حالة طبية طارئة.</li>"
                "<li>علامات <strong>المتلازمة الأيضية</strong>.</li>"
                "<li><strong>ألم شديد في البطن</strong> مع دهون ثلاثية مرتفعة جداً.</li>"
                "</ul>"
                "<p>يجب على البالغين إجراء صورة دهون كل 4&ndash;6 سنوات على الأقل بدءاً من سن 20، وبشكل أكثر تكراراً مع وجود عوامل خطر.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم نتائج الدهون الثلاثية",
            body_html=(
                "<p>فهم صورة الدهون بأرقامها المتعددة قد يكون محيراً. <strong>Norya</strong> تبسّط العملية: ارفع نتائج تحليل الدم "
                "واحصل خلال دقائق على تقرير صحي منظم وسهل الفهم.</p>"
                "<p>يبرز التقرير القيم خارج النطاق الطبيعي ويشرح معناها بلغة واضحة ويساعدك على تحضير أسئلة مستنيرة لزيارتك "
                "القادمة للطبيب. <a href=\"/analyze\">ابدأ تحليلك المجاني مع Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> '
                'ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# PUBLIC GETTERS
# ---------------------------------------------------------------------------
def get_triglycerides_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_triglycerides_faq_schema_qa() -> dict:
    return {
        "en": [
            {"question": "What is a normal triglyceride level?",
             "answer": "A normal fasting triglyceride level is below 150 mg/dL (1.7 mmol/L). An optimal level is below 100 mg/dL. Levels of 150-199 mg/dL are borderline high, 200-499 mg/dL are high, and 500 mg/dL or above are very high."},
            {"question": "What causes high triglycerides?",
             "answer": "High triglycerides can be caused by a diet rich in refined carbohydrates and sugars, excess alcohol, sedentary lifestyle, obesity, type 2 diabetes, hypothyroidism, kidney disease, genetic factors, and certain medications like beta-blockers and corticosteroids."},
            {"question": "What is the difference between triglycerides and cholesterol?",
             "answer": "Triglycerides store and release energy, while cholesterol is a structural component of cell membranes and a precursor for hormones and bile acids. Both are lipids but serve different functions."},
            {"question": "Can high triglycerides cause pancreatitis?",
             "answer": "Yes. Very high triglycerides (500 mg/dL or above) significantly increase the risk of acute pancreatitis, a potentially life-threatening inflammation of the pancreas."},
            {"question": "How can I lower my triglycerides naturally?",
             "answer": "Reduce refined carbohydrates and sugars, limit alcohol, eat omega-3-rich fish, exercise regularly (150 minutes per week), lose excess weight, and follow a Mediterranean-style diet."},
        ],
        "tr": [
            {"question": "Normal trigliserit düzeyi nedir?",
             "answer": "Normal açlık trigliserit düzeyi 150 mg/dL'nin (1,7 mmol/L) altındadır. Optimal düzey 100 mg/dL'nin altındadır. 150-199 mg/dL sınırda yüksek, 200-499 mg/dL yüksek ve 500 mg/dL veya üzeri çok yüksek kabul edilir."},
            {"question": "Yüksek trigliseride ne sebep olur?",
             "answer": "Rafine karbonhidrat ve şekerden zengin diyet, aşırı alkol, hareketsiz yaşam tarzı, obezite, tip 2 diyabet, hipotiroidizm, böbrek hastalığı, genetik faktörler ve beta-bloker, kortikosteroid gibi ilaçlar yüksek trigliseride neden olabilir."},
            {"question": "Trigliserid ile kolesterol arasındaki fark nedir?",
             "answer": "Trigliseridler enerji depolar ve serbest bırakırken, kolesterol hücre zarlarının yapısal bileşeni ve hormonlar ile safra asitleri için öncüdür. İkisi de lipit olmakla birlikte farklı işlevlere sahiptir."},
            {"question": "Yüksek trigliserid pankreatite neden olabilir mi?",
             "answer": "Evet. Çok yüksek trigliseridler (500 mg/dL veya üzeri) akut pankreatit riskini önemli ölçüde artırır."},
        ],
        "es": [
            {"question": "¿Cuál es un nivel normal de triglicéridos?",
             "answer": "Un nivel normal de triglicéridos en ayunas es inferior a 150 mg/dL (1,7 mmol/L). El nivel óptimo es inferior a 100 mg/dL."},
            {"question": "¿Qué causa los triglicéridos altos?",
             "answer": "Dieta rica en carbohidratos refinados y azúcares, exceso de alcohol, sedentarismo, obesidad, diabetes tipo 2, hipotiroidismo, enfermedad renal y factores genéticos."},
            {"question": "¿Cuál es la diferencia entre triglicéridos y colesterol?",
             "answer": "Los triglicéridos almacenan y liberan energía, mientras que el colesterol es un componente estructural de las membranas celulares y precursor de hormonas."},
            {"question": "¿Cómo puedo bajar mis triglicéridos de forma natural?",
             "answer": "Reduzca carbohidratos refinados, limite el alcohol, consuma pescados ricos en omega-3, haga ejercicio regularmente, pierda peso y siga una dieta mediterránea."},
        ],
        "de": [
            {"question": "Was ist ein normaler Triglyceridwert?",
             "answer": "Ein normaler Nüchtern-Triglyceridwert liegt unter 150 mg/dL (1,7 mmol/L). Optimal ist unter 100 mg/dL."},
            {"question": "Was verursacht hohe Triglyceride?",
             "answer": "Ernährung reich an raffinierten Kohlenhydraten, übermäßiger Alkoholkonsum, Bewegungsmangel, Adipositas, Typ-2-Diabetes, Hypothyreose, Nierenerkrankungen und genetische Faktoren."},
            {"question": "Können hohe Triglyceride eine Pankreatitis verursachen?",
             "answer": "Ja. Sehr hohe Triglyceride (ab 500 mg/dL) erhöhen das Risiko einer akuten Pankreatitis erheblich."},
            {"question": "Wie kann ich Triglyceride natürlich senken?",
             "answer": "Raffinierte Kohlenhydrate reduzieren, Alkohol einschränken, Omega-3-reichen Fisch essen, regelmäßig Sport treiben, Übergewicht abbauen und eine mediterrane Ernährung befolgen."},
        ],
        "fr": [
            {"question": "Quel est un taux normal de triglycérides ?",
             "answer": "Un taux normal de triglycérides à jeun est inférieur à 150 mg/dL (1,7 mmol/L). Le taux optimal est inférieur à 100 mg/dL."},
            {"question": "Quelles sont les causes des triglycérides élevés ?",
             "answer": "Alimentation riche en glucides raffinés, excès d'alcool, sédentarité, obésité, diabète de type 2, hypothyroïdie, maladie rénale et facteurs génétiques."},
            {"question": "Quelle est la différence entre triglycérides et cholestérol ?",
             "answer": "Les triglycérides stockent et libèrent de l'énergie, tandis que le cholestérol est un composant structurel des membranes cellulaires et un précurseur d'hormones."},
            {"question": "Comment réduire les triglycérides naturellement ?",
             "answer": "Réduire les glucides raffinés, limiter l'alcool, manger des poissons riches en oméga-3, faire de l'exercice régulièrement, perdre du poids et suivre un régime méditerranéen."},
        ],
        "it": [
            {"question": "Qual è un livello normale di trigliceridi?",
             "answer": "Un livello normale di trigliceridi a digiuno è inferiore a 150 mg/dL (1,7 mmol/L). Il livello ottimale è inferiore a 100 mg/dL."},
            {"question": "Cosa causa i trigliceridi alti?",
             "answer": "Dieta ricca di carboidrati raffinati, eccesso di alcol, sedentarietà, obesità, diabete di tipo 2, ipotiroidismo, nefropatia e fattori genetici."},
            {"question": "Qual è la differenza tra trigliceridi e colesterolo?",
             "answer": "I trigliceridi immagazzinano e rilasciano energia, mentre il colesterolo è un componente strutturale delle membrane cellulari e precursore di ormoni."},
            {"question": "Come posso abbassare i trigliceridi naturalmente?",
             "answer": "Ridurre i carboidrati raffinati, limitare l'alcol, mangiare pesce ricco di omega-3, fare esercizio regolarmente, perdere peso e seguire una dieta mediterranea."},
        ],
        "he": [
            {"question": "מהי רמת טריגליצרידים תקינה?",
             "answer": "רמת טריגליצרידים תקינה בצום היא מתחת ל-150 mg/dL (1.7 mmol/L). הרמה האופטימלית היא מתחת ל-100 mg/dL."},
            {"question": "מה גורם לטריגליצרידים גבוהים?",
             "answer": "תזונה עשירה בפחמימות מזוקקות, אלכוהול מופרז, חוסר פעילות, השמנה, סוכרת סוג 2, תת-פעילות בלוטת התריס, מחלת כליות וגורמים גנטיים."},
            {"question": "מה ההבדל בין טריגליצרידים לכולסטרול?",
             "answer": "טריגליצרידים מאחסנים ומשחררים אנרגיה, בעוד כולסטרול הוא מרכיב מבני של ממברנות תאים ומקדים להורמונים."},
            {"question": "כיצד ניתן להוריד טריגליצרידים באופן טבעי?",
             "answer": "להפחית פחמימות מזוקקות, להגביל אלכוהול, לאכול דגים עשירים באומגה-3, להתאמן באופן סדיר, להוריד במשקל ולאמץ תזונה ים-תיכונית."},
        ],
        "hi": [
            {"question": "सामान्य ट्राइग्लिसराइड स्तर क्या है?",
             "answer": "सामान्य उपवास ट्राइग्लिसराइड स्तर 150 mg/dL (1.7 mmol/L) से कम है। इष्टतम स्तर 100 mg/dL से कम है।"},
            {"question": "उच्च ट्राइग्लिसराइड्स का क्या कारण है?",
             "answer": "परिष्कृत कार्बोहाइड्रेट और चीनी से भरपूर आहार, अत्यधिक शराब, गतिहीन जीवनशैली, मोटापा, टाइप 2 मधुमेह, हाइपोथायरायडिज्म, गुर्दे की बीमारी और आनुवंशिक कारक।"},
            {"question": "ट्राइग्लिसराइड्स और कोलेस्ट्रॉल में क्या अंतर है?",
             "answer": "ट्राइग्लिसराइड्स ऊर्जा भंडारण और विमोचन करते हैं, जबकि कोलेस्ट्रॉल कोशिका झिल्ली का संरचनात्मक घटक और हार्मोन का अग्रदूत है।"},
            {"question": "ट्राइग्लिसराइड्स को प्राकृतिक रूप से कैसे कम करें?",
             "answer": "परिष्कृत कार्बोहाइड्रेट कम करें, शराब सीमित करें, ओमेगा-3 समृद्ध मछली खाएँ, नियमित व्यायाम करें, वजन कम करें और भूमध्यसागरीय आहार अपनाएँ।"},
        ],
        "ar": [
            {"question": "ما هو مستوى الدهون الثلاثية الطبيعي؟",
             "answer": "مستوى الدهون الثلاثية الطبيعي صائماً أقل من 150 mg/dL (1.7 mmol/L). المستوى الأمثل أقل من 100 mg/dL."},
            {"question": "ما أسباب ارتفاع الدهون الثلاثية؟",
             "answer": "نظام غذائي غني بالكربوهيدرات المكررة والسكريات، الإفراط في الكحول، الخمول، السمنة، السكري من النوع 2، قصور الغدة الدرقية، أمراض الكلى والعوامل الوراثية."},
            {"question": "ما الفرق بين الدهون الثلاثية والكوليسترول؟",
             "answer": "الدهون الثلاثية تخزن وتطلق الطاقة، بينما الكوليسترول مكون بنيوي لأغشية الخلايا وسلف للهرمونات."},
            {"question": "كيف يمكنني خفض الدهون الثلاثية طبيعياً؟",
             "answer": "تقليل الكربوهيدرات المكررة، الحد من الكحول، تناول الأسماك الغنية بأوميغا-3، ممارسة الرياضة بانتظام، فقدان الوزن الزائد واتباع نظام البحر المتوسط الغذائي."},
        ],
    }
