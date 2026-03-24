# -*- coding: utf-8 -*-
"""
Folate / Folic Acid blog article — full body content for all 9 languages.
Used by blog_i18n._article_folate().
Sections: intro, what-is, normal-ranges, causes, symptoms,
related-tests, when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="Folate blood test: what your result means",
            body_html=(
                "<p>Folate&mdash;also known as <strong>vitamin B9</strong>&mdash;is an essential water-soluble vitamin "
                "that plays a critical role in DNA synthesis, red blood cell formation, and cell division. "
                "When your blood test reports a folate level, it reflects how much of this vitamin is circulating "
                "in your serum or stored inside your red blood cells.</p>"
                "<p>A low folate result can point to nutritional deficiency, malabsorption, or increased demand "
                "(such as during pregnancy), while elevated levels are uncommon and usually harmless. "
                "Understanding what the number means&mdash;and what to do next&mdash;is the goal of this guide.</p>"
                "<p>This article is educational and does not replace medical advice. Always discuss your lab results "
                "with a qualified healthcare professional who knows your full clinical picture.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is folate and why does it matter?",
            body_html=(
                "<p><strong>Folate</strong> is the naturally occurring form of vitamin B9 found in foods such as dark leafy greens, "
                "legumes, and citrus fruits. <strong>Folic acid</strong> is the synthetic form used in supplements and fortified foods. "
                "Both are converted in the body to tetrahydrofolate (THF), the biologically active coenzyme that participates "
                "in one-carbon metabolism&mdash;a pathway essential for nucleotide synthesis and methylation reactions.</p>"
                "<p>Folate is required for the production of healthy red blood cells. When folate is insufficient, the bone marrow "
                "produces abnormally large, immature red cells called <em>megaloblasts</em>, leading to <strong>megaloblastic anemia</strong>. "
                "This is the same type of anemia seen in <a href=\"/en/blog/vitamin-b12-deficiency-or-excess\">vitamin B12 deficiency</a>, "
                "which is why doctors often test both markers together.</p>"
                "<p>In pregnancy, folate is crucial for the closure of the fetal neural tube during the first 28 days of gestation. "
                "Adequate folate intake before conception and in early pregnancy dramatically reduces the risk of neural tube defects "
                "such as spina bifida and anencephaly. This is why folic acid supplementation is universally recommended for women of "
                "childbearing age.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal folate ranges",
            body_html=(
                "<p>Folate can be measured as <strong>serum folate</strong> (reflects recent intake) or <strong>RBC folate</strong> "
                "(reflects long-term stores over the preceding 2&ndash;3 months). Your lab report will specify which was tested.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marker</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serum folate</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">RBC folate</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL (317&ndash;1422 nmol/L)</td></tr>'
                "</tbody></table>"
                "<p>A serum folate below 3&nbsp;ng/mL is generally considered deficient. Values between 3 and 5&nbsp;ng/mL may be "
                "borderline and warrant further evaluation&mdash;especially if the patient has symptoms or an elevated homocysteine level. "
                "RBC folate is a more reliable indicator of tissue stores because serum folate fluctuates with recent dietary intake.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of low and high folate",
            body_html=(
                "<p><strong>Low folate</strong> (deficiency) is most often caused by:</p>"
                "<ul>"
                "<li><strong>Inadequate dietary intake</strong> &ndash; diets low in fresh vegetables, legumes, and fortified grains.</li>"
                "<li><strong>Malabsorption</strong> &ndash; conditions such as <em>celiac disease</em>, <em>Crohn&rsquo;s disease</em>, "
                "and inflammatory bowel disease impair folate absorption in the small intestine.</li>"
                "<li><strong>Alcoholism</strong> &ndash; chronic alcohol use both reduces intake and directly impairs folate absorption and metabolism.</li>"
                "<li><strong>Increased demand</strong> &ndash; pregnancy, lactation, and periods of rapid cell growth (e.g.&nbsp;hemolytic anemia) "
                "increase the body&rsquo;s requirement for folate.</li>"
                "<li><strong>Medications</strong> &ndash; methotrexate (a folate antagonist), phenytoin, sulfasalazine, and trimethoprim "
                "can interfere with folate metabolism or absorption.</li>"
                "</ul>"
                "<p><strong>Elevated folate</strong> levels are rarely clinically significant. They typically result from high-dose supplementation "
                "or a diet very rich in fortified foods. Excess folic acid is generally excreted in the urine. However, very high folic acid "
                "intake can mask a concurrent <a href=\"/en/blog/vitamin-b12-deficiency-or-excess\">vitamin B12 deficiency</a> by partially "
                "correcting the anemia while neurological damage continues unchecked&mdash;a reason to check B12 alongside folate.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of folate deficiency",
            body_html=(
                "<p>Folate deficiency develops gradually and may be subtle at first. As the deficiency worsens, symptoms become more apparent:</p>"
                "<ul>"
                "<li><strong>Fatigue and weakness</strong> &ndash; due to megaloblastic anemia, which reduces the blood&rsquo;s oxygen-carrying capacity.</li>"
                "<li><strong>Pallor and shortness of breath</strong> &ndash; classic signs of anemia.</li>"
                "<li><strong>Mouth sores and glossitis</strong> &ndash; a smooth, swollen, red tongue is characteristic of folate (and B12) deficiency.</li>"
                "<li><strong>Irritability and difficulty concentrating</strong> &ndash; low folate can affect mood and cognitive function.</li>"
                "<li><strong>Elevated homocysteine</strong> &ndash; folate is needed to convert homocysteine to methionine; deficiency causes homocysteine to rise, "
                "which is associated with cardiovascular risk.</li>"
                "</ul>"
                "<p>In pregnant women, the most serious consequence of folate deficiency is the risk of <strong>neural tube defects</strong> in the developing "
                "fetus, including spina bifida and anencephaly. This risk is highest in the first trimester, often before a woman knows she is pregnant, "
                "which is why preconception supplementation is strongly advised.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>Folate is rarely interpreted in isolation. Your doctor may order the following tests alongside it:</p>"
                "<ul>"
                "<li><strong>Vitamin B12</strong> &ndash; folate and B12 deficiency produce similar blood findings (megaloblastic anemia, high MCV). "
                "Distinguishing between them is essential because the treatments differ and B12 deficiency can cause irreversible neurological damage. "
                "See our <a href=\"/en/blog/vitamin-b12-deficiency-or-excess\">vitamin B12 guide</a>.</li>"
                "<li><strong>Homocysteine</strong> &ndash; elevated in both folate and B12 deficiency; useful for detecting early or borderline deficiency.</li>"
                "<li><strong>MCV (Mean Corpuscular Volume)</strong> &ndash; a high MCV (&gt;100&nbsp;fL) suggests macrocytic anemia, which prompts testing "
                "for folate and B12.</li>"
                "<li><strong>Complete Blood Count (CBC)</strong> &ndash; evaluates red cell count, hemoglobin, hematocrit, and white blood cell morphology, "
                "all of which can be affected by folate deficiency.</li>"
                "<li><strong>Methylmalonic acid (MMA)</strong> &ndash; elevated specifically in B12 deficiency but not folate deficiency; "
                "helps differentiate the two when both are borderline.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>You should discuss your folate result with a healthcare provider if:</p>"
                "<ul>"
                "<li>Your serum folate is below 3&nbsp;ng/mL or your RBC folate is below the reference range.</li>"
                "<li>You have symptoms of anemia: unexplained fatigue, pallor, shortness of breath, or a sore tongue.</li>"
                "<li>You are pregnant or planning to become pregnant&mdash;adequate folate is critical for fetal development.</li>"
                "<li>You have a condition that impairs absorption (celiac disease, Crohn&rsquo;s disease, chronic alcohol use).</li>"
                "<li>You take medications that interfere with folate (methotrexate, phenytoin, sulfasalazine).</li>"
                "</ul>"
                "<p>Your doctor can determine whether supplementation is needed, identify the underlying cause of deficiency, "
                "and monitor your response to treatment. Do not self-treat with high-dose folic acid without medical guidance, "
                "as it may mask a B12 deficiency.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How NoryaAI helps you understand your folate results",
            body_html=(
                "<p>NoryaAI makes it easy to understand your folate and other blood test results. Simply "
                "<a href=\"/analyze\">upload your lab report</a>&mdash;whether it is a PDF, photo, or scan&mdash;and our AI engine will:</p>"
                "<ul>"
                "<li>Extract your folate value along with all other biomarkers on the report.</li>"
                "<li>Compare each result against age- and sex-specific reference ranges.</li>"
                "<li>Flag abnormal values with clear, plain-language explanations.</li>"
                "<li>Highlight connections between related markers (e.g.&nbsp;folate + B12 + homocysteine + MCV).</li>"
                "<li>Generate a structured, doctor-ready summary you can share at your next appointment.</li>"
                "</ul>"
                "<p>Explore our <a href=\"/pricing\">pricing plans</a> to see which option fits your needs. "
                "NoryaAI is designed to help you prepare for&mdash;not replace&mdash;a conversation with your doctor.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Medical disclaimer",
            body_html=(
                "<p><strong>This article is for informational and educational purposes only. It does not constitute medical advice, "
                "diagnosis, or treatment. Always consult a qualified healthcare professional before making any decisions based on "
                "your lab results. NoryaAI provides automated analysis to help you understand your reports, but it is not a substitute "
                "for professional medical judgment.</strong></p>"
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
            heading="Folat (folik asit) kan testi: sonucunuz ne anlama geliyor?",
            body_html=(
                "<p>Folat&mdash;diğer adıyla <strong>vitamin B9</strong>&mdash;DNA sentezi, kırmızı kan hücresi üretimi "
                "ve hücre bölünmesi için vazgeçilmez olan suda çözünür bir vitamindir. Kan tahlilinizdeki folat değeri, "
                "serumunuzda dolaşan veya kırmızı kan hücrelerinizde depolanan bu vitaminin miktarını yansıtır.</p>"
                "<p>Düşük folat sonucu beslenme yetersizliğine, emilim bozukluğuna veya artan ihtiyaca (örneğin gebelik) "
                "işaret edebilir. Yüksek folat ise genellikle zararsızdır ve nadiren klinik öneme sahiptir. "
                "Bu rehber, sonuçlarınızı anlamanıza yardımcı olmayı amaçlamaktadır.</p>"
                "<p>Bu makale eğitim amaçlıdır ve tıbbi tavsiye yerine geçmez. Sonuçlarınızı mutlaka bir hekimle değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Folat nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Folat</strong>, koyu yeşil yapraklı sebzeler, baklagiller ve narenciye gibi gıdalarda doğal olarak "
                "bulunan B9 vitaminidir. <strong>Folik asit</strong> ise takviyelerde ve zenginleştirilmiş gıdalarda kullanılan "
                "sentetik formudur. Her ikisi de vücutta tetrahidrofolata (THF) dönüştürülerek nükleotid sentezi ve metilasyon "
                "reaksiyonlarında görev alır.</p>"
                "<p>Folat, sağlıklı kırmızı kan hücresi üretimi için gereklidir. Yetersiz olduğunda kemik iliği anormal derecede büyük "
                "ve olgunlaşmamış hücreler&mdash;<em>megaloblastlar</em>&mdash;üretir; bu durum <strong>megaloblastik anemi</strong>ye yol açar. "
                "Aynı tablo <a href=\"/tr/blog/vitamin-b12-eksikligi-veya-fazlaligi\">vitamin B12 eksikliği</a>nde de görüldüğünden "
                "doktorlar genellikle her iki belirteci birlikte ister.</p>"
                "<p>Gebelikte folat, ilk 28 günde fetal nöral tüpün kapanması için kritik öneme sahiptir. Gebe kalmadan önce ve erken "
                "gebelikte yeterli folat alımı, spina bifida ve anensefali gibi nöral tüp defektlerinin riskini büyük ölçüde azaltır. "
                "Bu nedenle doğurganlık çağındaki tüm kadınlara folik asit takviyesi önerilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal folat aralıkları",
            body_html=(
                "<p>Folat <strong>serum folatı</strong> (son alımı yansıtır) veya <strong>eritrosit (RBC) folatı</strong> "
                "(son 2&ndash;3 aylık depoları yansıtır) olarak ölçülebilir.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Belirteç</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serum folat</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">RBC folat</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Serum folatı 3&nbsp;ng/mL&rsquo;nin altında ise genellikle eksiklik kabul edilir. 3&ndash;5&nbsp;ng/mL arası "
                "sınırda değerlendirilebilir ve özellikle semptomlar veya yüksek homosistein varsa ileri inceleme gerektirir. "
                "RBC folatı, doku depolarının daha güvenilir bir göstergesidir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Düşük ve yüksek folat nedenleri",
            body_html=(
                "<p><strong>Düşük folat</strong> (eksiklik) en sık şu nedenlerle ortaya çıkar:</p>"
                "<ul>"
                "<li><strong>Yetersiz beslenme</strong> &ndash; taze sebze, baklagil ve zenginleştirilmiş tahıl açısından fakir diyetler.</li>"
                "<li><strong>Emilim bozukluğu</strong> &ndash; çölyak hastalığı, Crohn hastalığı ve inflamatuar bağırsak hastalıkları.</li>"
                "<li><strong>Alkolizm</strong> &ndash; kronik alkol kullanımı hem alımı azaltır hem de folatın emilim ve metabolizmasını bozar.</li>"
                "<li><strong>Artan ihtiyaç</strong> &ndash; gebelik, emzirme ve hızlı hücre büyüme dönemleri.</li>"
                "<li><strong>İlaçlar</strong> &ndash; metotreksat, fenitoin, sülfasalazin ve trimetoprim folat metabolizmasını olumsuz etkiler.</li>"
                "</ul>"
                "<p><strong>Yüksek folat</strong> nadiren klinik önem taşır ve genellikle yüksek doz takviye kullanımından kaynaklanır. "
                "Ancak fazla folik asit, eşzamanlı bir <a href=\"/tr/blog/vitamin-b12-eksikligi-veya-fazlaligi\">B12 eksikliğini</a> "
                "maskeleyerek anemiyi düzeltirken nörolojik hasarın devam etmesine neden olabilir.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Folat eksikliği belirtileri",
            body_html=(
                "<p>Folat eksikliği yavaş gelişir ve başlangıçta fark edilmeyebilir. Eksiklik ilerledikçe belirtiler belirginleşir:</p>"
                "<ul>"
                "<li><strong>Yorgunluk ve halsizlik</strong> &ndash; megaloblastik anemiye bağlı olarak kanın oksijen taşıma kapasitesi azalır.</li>"
                "<li><strong>Soluk cilt ve nefes darlığı</strong> &ndash; aneminin klasik işaretleri.</li>"
                "<li><strong>Ağız yaraları ve glossit</strong> &ndash; pürüzsüz, şiş ve kırmızı bir dil, folat eksikliğine özgüdür.</li>"
                "<li><strong>Huzursuzluk ve konsantrasyon güçlüğü</strong> &ndash; düşük folat ruh hali ve bilişsel işlevi etkileyebilir.</li>"
                "<li><strong>Yüksek homosistein</strong> &ndash; folat eksikliği homosisteininin yükselmesine neden olur ve kardiyovasküler risk artırır.</li>"
                "</ul>"
                "<p>Gebelerde en ciddi sonuç, <strong>nöral tüp defektleri</strong> riskidir. Bu risk özellikle birinci trimesterde "
                "yüksektir ve kadın genellikle henüz hamile olduğunu bilmez; bu yüzden gebe kalmadan önce takviye başlanması önerilir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlişkili testler",
            body_html=(
                "<p>Folat genellikle tek başına değerlendirilmez. Doktorunuz şu testleri de isteyebilir:</p>"
                "<ul>"
                "<li><strong>Vitamin B12</strong> &ndash; folat ve B12 eksikliği benzer kan bulguları üretir; ayrım tedavi açısından kritiktir. "
                "<a href=\"/tr/blog/vitamin-b12-eksikligi-veya-fazlaligi\">B12 rehberimize</a> bakın.</li>"
                "<li><strong>Homosistein</strong> &ndash; hem folat hem B12 eksikliğinde yükselir; erken eksiklik tespitinde faydalıdır.</li>"
                "<li><strong>MCV (Ortalama Eritrosit Hacmi)</strong> &ndash; yüksek MCV makrositik anemiye işaret eder.</li>"
                "<li><strong>Tam Kan Sayımı (CBC)</strong> &ndash; kırmızı hücre sayısı, hemoglobin ve beyaz hücre morfolojisini değerlendirir.</li>"
                "<li><strong>Metilmalonik asit (MMA)</strong> &ndash; yalnızca B12 eksikliğinde yükselir; iki eksikliği ayırt etmeye yardımcı olur.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda folat sonucunuzu bir hekimle görüşmelisiniz:</p>"
                "<ul>"
                "<li>Serum folatınız 3&nbsp;ng/mL&rsquo;nin altında veya RBC folatınız referans aralığının dışında.</li>"
                "<li>Anemi belirtileriniz var: açıklanamayan yorgunluk, soluk cilt, nefes darlığı veya ağrılı dil.</li>"
                "<li>Hamilesiniz veya hamile kalmayı planlıyorsunuz.</li>"
                "<li>Emilimi bozan bir hastalığınız var (çölyak, Crohn, kronik alkol kullanımı).</li>"
                "<li>Folat metabolizmasını etkileyen ilaçlar kullanıyorsunuz (metotreksat, fenitoin).</li>"
                "</ul>"
                "<p>Doktorunuz takviye gerekip gerekmediğini belirleyebilir, altta yatan nedeni saptayabilir ve tedavi yanıtınızı "
                "izleyebilir. Tıbbi rehberlik olmadan yüksek doz folik asit kullanmaktan kaçının.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI folat sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>NoryaAI, folat ve diğer kan testi sonuçlarınızı kolayca anlamanızı sağlar. "
                "<a href=\"/analyze\">Laboratuvar raporunuzu yükleyin</a>&mdash;PDF, fotoğraf veya tarama olabilir&mdash;yapay zeka motorumuz:</p>"
                "<ul>"
                "<li>Rapordaki folat değerini ve diğer tüm biyobelirteçleri otomatik olarak çıkarır.</li>"
                "<li>Her sonucu yaş ve cinsiyete özel referans aralıklarıyla karşılaştırır.</li>"
                "<li>Anormal değerleri sade ve anlaşılır açıklamalarla işaretler.</li>"
                "<li>İlişkili belirteçler arasındaki bağlantıları vurgular (örn. folat + B12 + homosistein + MCV).</li>"
                "<li>Doktorunuza götürebileceğiniz yapılandırılmış bir özet rapor oluşturur.</li>"
                "</ul>"
                "<p><a href=\"/pricing\">Fiyatlandırma planlarımızı</a> inceleyerek ihtiyacınıza uygun seçeneği bulun. "
                "NoryaAI, doktorunuzla görüşmenize hazırlanmanıza yardımcı olur; onun yerini almaz.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Tıbbi sorumluluk reddi",
            body_html=(
                "<p><strong>Bu makale yalnızca bilgilendirme ve eğitim amaçlıdır. Tıbbi tavsiye, teşhis veya tedavi niteliği taşımaz. "
                "Laboratuvar sonuçlarınıza dayalı herhangi bir karar vermeden önce mutlaka nitelikli bir sağlık uzmanına danışın. "
                "NoryaAI, raporlarınızı anlamanıza yardımcı olmak için otomatik analiz sunar ancak profesyonel tıbbi değerlendirmenin "
                "yerini tutmaz.</strong></p>"
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
            heading="Análisis de folato en sangre: qué significa tu resultado",
            body_html=(
                "<p>El folato&mdash;también conocido como <strong>vitamina B9</strong>&mdash;es una vitamina hidrosoluble esencial "
                "para la síntesis de ADN, la formación de glóbulos rojos y la división celular. El valor de folato en tu análisis "
                "refleja la cantidad de esta vitamina que circula en tu suero o se almacena dentro de tus eritrocitos.</p>"
                "<p>Un resultado bajo puede indicar deficiencia nutricional, malabsorción o aumento de la demanda (como durante el embarazo). "
                "Los niveles elevados son infrecuentes y generalmente inofensivos. Esta guía te ayudará a entender tu resultado.</p>"
                "<p>Este artículo es educativo y no sustituye el consejo médico. Siempre comenta tus resultados con un profesional de salud.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es el folato y por qué es importante?",
            body_html=(
                "<p><strong>El folato</strong> es la forma natural de la vitamina B9 que se encuentra en alimentos como verduras de hoja oscura, "
                "legumbres y cítricos. <strong>El ácido fólico</strong> es la forma sintética utilizada en suplementos y alimentos fortificados. "
                "Ambos se convierten en tetrahidrofolato (THF), la coenzima activa que participa en la síntesis de nucleótidos y reacciones de metilación.</p>"
                "<p>El folato es necesario para la producción de glóbulos rojos sanos. Cuando es insuficiente, la médula ósea produce células "
                "anormalmente grandes e inmaduras llamadas <em>megaloblastos</em>, lo que conduce a la <strong>anemia megaloblástica</strong>. "
                "Este mismo tipo de anemia se observa en la <a href=\"/es/blog/deficiencia-vitamina-b12\">deficiencia de vitamina B12</a>.</p>"
                "<p>Durante el embarazo, el folato es crucial para el cierre del tubo neural fetal durante los primeros 28 días de gestación. "
                "Una ingesta adecuada reduce drásticamente el riesgo de defectos del tubo neural como espina bífida y anencefalia.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos normales de folato",
            body_html=(
                "<p>El folato puede medirse como <strong>folato sérico</strong> (refleja la ingesta reciente) o <strong>folato eritrocitario (RBC)</strong> "
                "(refleja las reservas a largo plazo de los últimos 2&ndash;3 meses).</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marcador</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Folato sérico</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Folato RBC</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Un folato sérico por debajo de 3&nbsp;ng/mL se considera deficiente. Valores entre 3 y 5&nbsp;ng/mL pueden ser límite "
                "y requieren evaluación adicional, especialmente si hay síntomas o la homocisteína está elevada.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de folato bajo y alto",
            body_html=(
                "<p><strong>Folato bajo</strong> (deficiencia) suele deberse a:</p>"
                "<ul>"
                "<li><strong>Ingesta dietética inadecuada</strong> &ndash; dietas pobres en verduras frescas, legumbres y cereales fortificados.</li>"
                "<li><strong>Malabsorción</strong> &ndash; enfermedad celíaca, enfermedad de Crohn y enfermedad inflamatoria intestinal.</li>"
                "<li><strong>Alcoholismo</strong> &ndash; reduce la ingesta y altera la absorción y el metabolismo del folato.</li>"
                "<li><strong>Demanda aumentada</strong> &ndash; embarazo, lactancia y periodos de crecimiento celular rápido.</li>"
                "<li><strong>Medicamentos</strong> &ndash; metotrexato, fenitoína, sulfasalazina y trimetoprima.</li>"
                "</ul>"
                "<p>El <strong>folato elevado</strong> rara vez es clínicamente significativo. Sin embargo, dosis altas de ácido fólico pueden "
                "enmascarar una <a href=\"/es/blog/deficiencia-vitamina-b12\">deficiencia de B12</a> simultánea.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de la deficiencia de folato",
            body_html=(
                "<p>La deficiencia de folato se desarrolla gradualmente. A medida que empeora, los síntomas se hacen evidentes:</p>"
                "<ul>"
                "<li><strong>Fatiga y debilidad</strong> &ndash; por anemia megaloblástica que reduce la capacidad de transporte de oxígeno.</li>"
                "<li><strong>Palidez y dificultad respiratoria</strong> &ndash; signos clásicos de anemia.</li>"
                "<li><strong>Úlceras bucales y glositis</strong> &ndash; lengua lisa, hinchada y enrojecida.</li>"
                "<li><strong>Irritabilidad y dificultad de concentración</strong> &ndash; el folato bajo afecta el ánimo y la cognición.</li>"
                "<li><strong>Homocisteína elevada</strong> &ndash; asociada con mayor riesgo cardiovascular.</li>"
                "</ul>"
                "<p>En mujeres embarazadas, la consecuencia más grave son los <strong>defectos del tubo neural</strong> en el feto, "
                "incluyendo espina bífida y anencefalia.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p>El folato rara vez se interpreta de forma aislada. Tu médico puede solicitar:</p>"
                "<ul>"
                "<li><strong>Vitamina B12</strong> &ndash; la deficiencia de folato y B12 producen hallazgos similares. "
                "Consulta nuestra <a href=\"/es/blog/deficiencia-vitamina-b12\">guía de B12</a>.</li>"
                "<li><strong>Homocisteína</strong> &ndash; elevada en ambas deficiencias.</li>"
                "<li><strong>VCM (Volumen Corpuscular Medio)</strong> &ndash; un VCM alto sugiere anemia macrocítica.</li>"
                "<li><strong>Hemograma completo (CBC)</strong> &ndash; evalúa glóbulos rojos, hemoglobina y morfología leucocitaria.</li>"
                "<li><strong>Ácido metilmalónico (MMA)</strong> &ndash; elevado solo en deficiencia de B12, no de folato.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Consulta con tu médico si:</p>"
                "<ul>"
                "<li>Tu folato sérico está por debajo de 3&nbsp;ng/mL o el folato RBC está fuera del rango.</li>"
                "<li>Tienes síntomas de anemia: fatiga inexplicable, palidez, dificultad para respirar o lengua dolorosa.</li>"
                "<li>Estás embarazada o planeas un embarazo.</li>"
                "<li>Tienes una enfermedad que afecta la absorción (celíaca, Crohn, consumo crónico de alcohol).</li>"
                "<li>Tomas medicamentos que interfieren con el folato (metotrexato, fenitoína).</li>"
                "</ul>"
                "<p>Tu médico determinará si necesitas suplementación, identificará la causa y monitoreará tu respuesta al tratamiento.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo NoryaAI te ayuda a entender tu folato",
            body_html=(
                "<p>NoryaAI facilita la comprensión de tu folato y otros análisis de sangre. "
                "<a href=\"/analyze\">Sube tu informe de laboratorio</a>&mdash;PDF, foto o escaneo&mdash;y nuestro motor de IA:</p>"
                "<ul>"
                "<li>Extrae tu folato y todos los demás biomarcadores del informe.</li>"
                "<li>Compara cada resultado con rangos de referencia específicos por edad y sexo.</li>"
                "<li>Señala valores anormales con explicaciones claras en lenguaje sencillo.</li>"
                "<li>Destaca conexiones entre marcadores relacionados (ej. folato + B12 + homocisteína).</li>"
                "<li>Genera un resumen estructurado listo para tu médico.</li>"
                "</ul>"
                "<p>Explora nuestros <a href=\"/pricing\">planes de precios</a> y encuentra la opción que mejor se adapte a ti.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso médico",
            body_html=(
                "<p><strong>Este artículo es solo informativo y educativo. No constituye consejo médico, diagnóstico ni tratamiento. "
                "Consulta siempre a un profesional de salud cualificado antes de tomar decisiones basadas en tus resultados de laboratorio. "
                "NoryaAI ofrece análisis automatizado para ayudarte a comprender tus informes, pero no sustituye el criterio médico profesional.</strong></p>"
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
            heading="Folat-Bluttest: Was Ihr Ergebnis bedeutet",
            body_html=(
                "<p>Folat&mdash;auch bekannt als <strong>Vitamin B9</strong>&mdash;ist ein essentielles wasserlösliches Vitamin, "
                "das eine zentrale Rolle bei der DNA-Synthese, der Bildung roter Blutkörperchen und der Zellteilung spielt. "
                "Der Folatwert in Ihrer Blutuntersuchung zeigt, wie viel von diesem Vitamin in Ihrem Serum zirkuliert oder in Ihren "
                "roten Blutkörperchen gespeichert ist.</p>"
                "<p>Ein niedriger Folatwert kann auf Ernährungsmangel, Malabsorption oder erhöhten Bedarf (z.&nbsp;B. in der Schwangerschaft) "
                "hinweisen. Erhöhte Werte sind selten und in der Regel harmlos. Dieser Ratgeber hilft Ihnen, Ihr Ergebnis zu verstehen.</p>"
                "<p>Dieser Artikel dient der Aufklärung und ersetzt keine ärztliche Beratung. Besprechen Sie Ihre Laborergebnisse stets mit Ihrem Arzt.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist Folat und warum ist es wichtig?",
            body_html=(
                "<p><strong>Folat</strong> ist die natürlich vorkommende Form von Vitamin B9 in Lebensmitteln wie dunkelgrünem Blattgemüse, "
                "Hülsenfrüchten und Zitrusfrüchten. <strong>Folsäure</strong> ist die synthetische Form in Nahrungsergänzungsmitteln und "
                "angereicherten Lebensmitteln. Beide werden im Körper zu Tetrahydrofolat (THF) umgewandelt, dem biologisch aktiven Coenzym "
                "für Nukleotidsynthese und Methylierungsreaktionen.</p>"
                "<p>Folat wird für die Produktion gesunder roter Blutkörperchen benötigt. Bei Mangel produziert das Knochenmark abnorm große, "
                "unreife Zellen (<em>Megaloblasten</em>), was zu einer <strong>megaloblastären Anämie</strong> führt&mdash;derselbe Anämietyp "
                "wie bei <a href=\"/de/blog/vitamin-b12-mangel-oder-ueberschuss\">Vitamin-B12-Mangel</a>.</p>"
                "<p>In der Schwangerschaft ist Folat entscheidend für den Verschluss des fetalen Neuralrohrs in den ersten 28 Tagen. "
                "Eine ausreichende Zufuhr vor der Empfängnis und in der Frühschwangerschaft reduziert das Risiko von Neuralrohrdefekten "
                "wie Spina bifida und Anenzephalie erheblich.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Folatwerte",
            body_html=(
                "<p>Folat kann als <strong>Serumfolat</strong> (spiegelt die aktuelle Zufuhr wider) oder als <strong>Erythrozyten-Folat (RBC-Folat)</strong> "
                "(spiegelt die Langzeitspeicher der letzten 2&ndash;3 Monate wider) gemessen werden.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marker</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serumfolat</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">RBC-Folat</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Ein Serumfolat unter 3&nbsp;ng/mL gilt als Mangel. Werte zwischen 3 und 5&nbsp;ng/mL können grenzwertig sein und "
                "erfordern weitere Abklärung&mdash;besonders bei Symptomen oder erhöhtem Homocystein.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für niedrige und hohe Folatwerte",
            body_html=(
                "<p><strong>Niedriges Folat</strong> (Mangel) wird am häufigsten verursacht durch:</p>"
                "<ul>"
                "<li><strong>Unzureichende Ernährung</strong> &ndash; Diäten mit wenig frischem Gemüse, Hülsenfrüchten und angereichertem Getreide.</li>"
                "<li><strong>Malabsorption</strong> &ndash; Zöliakie, Morbus Crohn und entzündliche Darmerkrankungen.</li>"
                "<li><strong>Alkoholismus</strong> &ndash; chronischer Alkoholkonsum reduziert die Zufuhr und beeinträchtigt Absorption und Stoffwechsel.</li>"
                "<li><strong>Erhöhter Bedarf</strong> &ndash; Schwangerschaft, Stillzeit und schnelles Zellwachstum.</li>"
                "<li><strong>Medikamente</strong> &ndash; Methotrexat, Phenytoin, Sulfasalazin und Trimethoprim.</li>"
                "</ul>"
                "<p><strong>Erhöhtes Folat</strong> ist selten klinisch relevant. Sehr hohe Folsäurezufuhr kann jedoch einen gleichzeitigen "
                "<a href=\"/de/blog/vitamin-b12-mangel-oder-ueberschuss\">Vitamin-B12-Mangel</a> maskieren.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome eines Folatmangels",
            body_html=(
                "<p>Ein Folatmangel entwickelt sich schleichend. Mit zunehmendem Mangel werden die Symptome deutlicher:</p>"
                "<ul>"
                "<li><strong>Müdigkeit und Schwäche</strong> &ndash; durch megaloblastäre Anämie mit verminderter Sauerstofftransportkapazität.</li>"
                "<li><strong>Blässe und Kurzatmigkeit</strong> &ndash; klassische Anämiezeichen.</li>"
                "<li><strong>Mundgeschwüre und Glossitis</strong> &ndash; eine glatte, geschwollene, rote Zunge ist typisch.</li>"
                "<li><strong>Reizbarkeit und Konzentrationsstörungen</strong> &ndash; niedriges Folat kann Stimmung und Kognition beeinträchtigen.</li>"
                "<li><strong>Erhöhtes Homocystein</strong> &ndash; assoziiert mit erhöhtem kardiovaskulärem Risiko.</li>"
                "</ul>"
                "<p>Bei Schwangeren ist die schwerwiegendste Folge das Risiko von <strong>Neuralrohrdefekten</strong> beim Fötus, "
                "darunter Spina bifida und Anenzephalie.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Verwandte Laborwerte",
            body_html=(
                "<p>Folat wird selten isoliert betrachtet. Ihr Arzt kann folgende Tests anordnen:</p>"
                "<ul>"
                "<li><strong>Vitamin B12</strong> &ndash; Folat- und B12-Mangel erzeugen ähnliche Befunde. "
                "Siehe unseren <a href=\"/de/blog/vitamin-b12-mangel-oder-ueberschuss\">B12-Ratgeber</a>.</li>"
                "<li><strong>Homocystein</strong> &ndash; bei beiden Mangelzuständen erhöht.</li>"
                "<li><strong>MCV (mittleres korpuskuläres Volumen)</strong> &ndash; ein hohes MCV deutet auf makrozytäre Anämie hin.</li>"
                "<li><strong>Blutbild (CBC)</strong> &ndash; bewertet Erythrozyten, Hämoglobin und Leukozytenmorphologie.</li>"
                "<li><strong>Methylmalonsäure (MMA)</strong> &ndash; nur bei B12-Mangel erhöht; hilft bei der Differenzierung.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann Sie einen Arzt aufsuchen sollten",
            body_html=(
                "<p>Sprechen Sie mit Ihrem Arzt, wenn:</p>"
                "<ul>"
                "<li>Ihr Serumfolat unter 3&nbsp;ng/mL liegt oder Ihr RBC-Folat außerhalb des Referenzbereichs liegt.</li>"
                "<li>Sie Anämiesymptome haben: unerklärliche Müdigkeit, Blässe, Kurzatmigkeit oder eine schmerzende Zunge.</li>"
                "<li>Sie schwanger sind oder eine Schwangerschaft planen.</li>"
                "<li>Sie an einer Erkrankung leiden, die die Aufnahme beeinträchtigt (Zöliakie, Morbus Crohn, chronischer Alkoholkonsum).</li>"
                "<li>Sie Medikamente einnehmen, die Folat beeinflussen (Methotrexat, Phenytoin).</li>"
                "</ul>"
                "<p>Ihr Arzt kann feststellen, ob eine Supplementierung nötig ist, die Ursache identifizieren und Ihr Ansprechen "
                "auf die Behandlung überwachen.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie NoryaAI Ihnen bei Ihren Folatwerten hilft",
            body_html=(
                "<p>NoryaAI macht es einfach, Ihre Folat- und andere Blutwerte zu verstehen. "
                "<a href=\"/analyze\">Laden Sie Ihren Laborbefund hoch</a>&mdash;als PDF, Foto oder Scan&mdash;und unsere KI:</p>"
                "<ul>"
                "<li>Extrahiert Ihren Folatwert sowie alle weiteren Biomarker.</li>"
                "<li>Vergleicht jeden Wert mit alters- und geschlechtsspezifischen Referenzbereichen.</li>"
                "<li>Markiert auffällige Werte mit klaren, verständlichen Erklärungen.</li>"
                "<li>Hebt Zusammenhänge zwischen verwandten Markern hervor (z.&nbsp;B. Folat + B12 + Homocystein).</li>"
                "<li>Erstellt eine strukturierte, arztfertige Zusammenfassung.</li>"
                "</ul>"
                "<p>Entdecken Sie unsere <a href=\"/pricing\">Preispläne</a> und finden Sie die passende Option.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Medizinischer Haftungsausschluss",
            body_html=(
                "<p><strong>Dieser Artikel dient ausschließlich der Information und Aufklärung. Er stellt keine medizinische Beratung, "
                "Diagnose oder Behandlung dar. Konsultieren Sie immer einen qualifizierten Arzt, bevor Sie Entscheidungen auf Grundlage "
                "Ihrer Laborergebnisse treffen. NoryaAI bietet automatisierte Analysen, um Ihre Befunde verständlich zu machen, ersetzt "
                "aber kein ärztliches Urteil.</strong></p>"
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
            heading="Analyse de folate sanguin : que signifie votre résultat ?",
            body_html=(
                "<p>Le folate&mdash;également appelé <strong>vitamine B9</strong>&mdash;est une vitamine hydrosoluble essentielle "
                "à la synthèse de l&rsquo;ADN, à la formation des globules rouges et à la division cellulaire. La valeur de folate "
                "dans votre bilan sanguin reflète la quantité de cette vitamine circulant dans votre sérum ou stockée dans vos globules rouges.</p>"
                "<p>Un résultat bas peut indiquer une carence nutritionnelle, une malabsorption ou une demande accrue (par exemple pendant la grossesse). "
                "Les niveaux élevés sont rares et généralement inoffensifs. Ce guide vous aide à comprendre votre résultat.</p>"
                "<p>Cet article est éducatif et ne remplace pas un avis médical. Discutez toujours de vos résultats avec votre médecin.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu'est-ce que le folate et pourquoi est-il important ?",
            body_html=(
                "<p>Le <strong>folate</strong> est la forme naturelle de la vitamine B9 présente dans les légumes-feuilles foncés, "
                "les légumineuses et les agrumes. L&rsquo;<strong>acide folique</strong> est la forme synthétique utilisée dans les compléments "
                "et les aliments enrichis. Les deux sont convertis en tétrahydrofolate (THF) dans l&rsquo;organisme, la coenzyme active "
                "nécessaire à la synthèse des nucléotides et aux réactions de méthylation.</p>"
                "<p>Le folate est indispensable à la production de globules rouges sains. En cas d&rsquo;insuffisance, la moelle osseuse "
                "produit des cellules anormalement grandes et immatures appelées <em>mégaloblastes</em>, entraînant une "
                "<strong>anémie mégaloblastique</strong>. Le même type d&rsquo;anémie survient en cas de "
                "<a href=\"/fr/blog/carence-vitamine-b12\">carence en vitamine B12</a>.</p>"
                "<p>Pendant la grossesse, le folate est crucial pour la fermeture du tube neural fœtal au cours des 28 premiers jours. "
                "Un apport adéquat avant la conception réduit considérablement le risque de défauts du tube neural tels que le spina bifida.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de folate",
            body_html=(
                "<p>Le folate peut être mesuré sous forme de <strong>folate sérique</strong> (reflète l&rsquo;apport récent) ou de "
                "<strong>folate érythrocytaire (RBC)</strong> (reflète les réserves à long terme sur 2&ndash;3 mois).</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marqueur</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valeurs normales</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Folate sérique</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Folate RBC</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Un folate sérique inférieur à 3&nbsp;ng/mL est généralement considéré comme déficient. Des valeurs entre 3 et 5&nbsp;ng/mL "
                "peuvent être limites et nécessitent une évaluation complémentaire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un folate bas ou élevé",
            body_html=(
                "<p>Les causes les plus fréquentes de <strong>folate bas</strong> sont :</p>"
                "<ul>"
                "<li><strong>Apport alimentaire insuffisant</strong> &ndash; régimes pauvres en légumes frais, légumineuses et céréales enrichies.</li>"
                "<li><strong>Malabsorption</strong> &ndash; maladie cœliaque, maladie de Crohn et maladies inflammatoires intestinales.</li>"
                "<li><strong>Alcoolisme</strong> &ndash; l&rsquo;alcool chronique réduit l&rsquo;apport et altère l&rsquo;absorption et le métabolisme du folate.</li>"
                "<li><strong>Demande accrue</strong> &ndash; grossesse, allaitement et périodes de croissance cellulaire rapide.</li>"
                "<li><strong>Médicaments</strong> &ndash; méthotrexate, phénytoïne, sulfasalazine et triméthoprime.</li>"
                "</ul>"
                "<p>Un <strong>folate élevé</strong> est rarement significatif cliniquement. Cependant, des doses élevées d&rsquo;acide folique "
                "peuvent masquer une <a href=\"/fr/blog/carence-vitamine-b12\">carence en B12</a> concomitante.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes de la carence en folate",
            body_html=(
                "<p>La carence en folate se développe progressivement. Les symptômes deviennent plus marqués au fil du temps :</p>"
                "<ul>"
                "<li><strong>Fatigue et faiblesse</strong> &ndash; dues à l&rsquo;anémie mégaloblastique.</li>"
                "<li><strong>Pâleur et essoufflement</strong> &ndash; signes classiques d&rsquo;anémie.</li>"
                "<li><strong>Aphtes et glossite</strong> &ndash; langue lisse, gonflée et rouge.</li>"
                "<li><strong>Irritabilité et troubles de la concentration</strong> &ndash; le folate bas affecte l&rsquo;humeur.</li>"
                "<li><strong>Homocystéine élevée</strong> &ndash; associée à un risque cardiovasculaire accru.</li>"
                "</ul>"
                "<p>Chez les femmes enceintes, la conséquence la plus grave est le risque de <strong>défauts du tube neural</strong> "
                "chez le fœtus, notamment le spina bifida et l&rsquo;anencéphalie.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Analyses associées",
            body_html=(
                "<p>Le folate est rarement interprété isolément. Votre médecin peut prescrire :</p>"
                "<ul>"
                "<li><strong>Vitamine B12</strong> &ndash; les carences en folate et B12 produisent des résultats similaires. "
                "Voir notre <a href=\"/fr/blog/carence-vitamine-b12\">guide B12</a>.</li>"
                "<li><strong>Homocystéine</strong> &ndash; élevée dans les deux carences.</li>"
                "<li><strong>VGM (Volume Globulaire Moyen)</strong> &ndash; un VGM élevé suggère une anémie macrocytaire.</li>"
                "<li><strong>Hémogramme complet (NFS)</strong> &ndash; évalue les globules rouges, l&rsquo;hémoglobine et la morphologie leucocytaire.</li>"
                "<li><strong>Acide méthylmalonique (MMA)</strong> &ndash; élevé uniquement en cas de carence en B12.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin",
            body_html=(
                "<p>Consultez votre médecin si :</p>"
                "<ul>"
                "<li>Votre folate sérique est inférieur à 3&nbsp;ng/mL ou votre folate RBC est hors de la fourchette de référence.</li>"
                "<li>Vous présentez des symptômes d&rsquo;anémie : fatigue inexpliquée, pâleur, essoufflement ou langue douloureuse.</li>"
                "<li>Vous êtes enceinte ou envisagez une grossesse.</li>"
                "<li>Vous souffrez d&rsquo;une maladie affectant l&rsquo;absorption (cœliaque, Crohn, consommation chronique d&rsquo;alcool).</li>"
                "<li>Vous prenez des médicaments interférant avec le folate (méthotrexate, phénytoïne).</li>"
                "</ul>"
                "<p>Votre médecin déterminera la nécessité d&rsquo;une supplémentation, identifiera la cause et surveillera votre réponse.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment NoryaAI vous aide à comprendre vos résultats de folate",
            body_html=(
                "<p>NoryaAI simplifie la compréhension de vos résultats de folate et autres analyses sanguines. "
                "<a href=\"/analyze\">Téléchargez votre bilan</a>&mdash;PDF, photo ou scan&mdash;et notre IA :</p>"
                "<ul>"
                "<li>Extrait votre folate et tous les autres biomarqueurs du rapport.</li>"
                "<li>Compare chaque résultat aux valeurs de référence selon l&rsquo;âge et le sexe.</li>"
                "<li>Signale les valeurs anormales avec des explications claires.</li>"
                "<li>Met en évidence les liens entre marqueurs associés (ex. folate + B12 + homocystéine).</li>"
                "<li>Génère un résumé structuré prêt pour votre médecin.</li>"
                "</ul>"
                "<p>Découvrez nos <a href=\"/pricing\">formules tarifaires</a> pour trouver celle qui vous convient.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement médical",
            body_html=(
                "<p><strong>Cet article est fourni à titre informatif et éducatif uniquement. Il ne constitue pas un avis médical, "
                "un diagnostic ou un traitement. Consultez toujours un professionnel de santé qualifié avant de prendre des décisions "
                "basées sur vos résultats de laboratoire. NoryaAI propose une analyse automatisée pour vous aider à comprendre vos bilans, "
                "mais ne remplace pas le jugement médical professionnel.</strong></p>"
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
            heading="Analisi del folato nel sangue: cosa significa il tuo risultato",
            body_html=(
                "<p>Il folato&mdash;noto anche come <strong>vitamina B9</strong>&mdash;è una vitamina idrosolubile essenziale "
                "per la sintesi del DNA, la formazione dei globuli rossi e la divisione cellulare. Il valore di folato nel tuo esame "
                "del sangue riflette la quantità di questa vitamina che circola nel siero o è immagazzinata nei globuli rossi.</p>"
                "<p>Un risultato basso può indicare carenza nutrizionale, malassorbimento o aumento della domanda (ad esempio in gravidanza). "
                "I livelli elevati sono rari e generalmente innocui. Questa guida ti aiuta a comprendere il tuo risultato.</p>"
                "<p>Questo articolo è a scopo educativo e non sostituisce il parere medico. Discuti sempre i tuoi risultati con il tuo medico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Cos'è il folato e perché è importante?",
            body_html=(
                "<p>Il <strong>folato</strong> è la forma naturale della vitamina B9 presente in alimenti come verdure a foglia scura, "
                "legumi e agrumi. L&rsquo;<strong>acido folico</strong> è la forma sintetica usata negli integratori e nei cibi arricchiti. "
                "Entrambi vengono convertiti nell&rsquo;organismo in tetraidrofolato (THF), il coenzima biologicamente attivo per la sintesi "
                "dei nucleotidi e le reazioni di metilazione.</p>"
                "<p>Il folato è necessario per la produzione di globuli rossi sani. Quando insufficiente, il midollo osseo produce cellule "
                "anormalmente grandi e immature chiamate <em>megaloblasti</em>, causando <strong>anemia megaloblastica</strong>. "
                "Lo stesso tipo di anemia si osserva nella <a href=\"/it/blog/carenza-vitamina-b12\">carenza di vitamina B12</a>.</p>"
                "<p>In gravidanza, il folato è fondamentale per la chiusura del tubo neurale fetale nei primi 28 giorni di gestazione. "
                "Un apporto adeguato riduce drasticamente il rischio di difetti del tubo neurale come spina bifida e anencefalia.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del folato",
            body_html=(
                "<p>Il folato può essere misurato come <strong>folato sierico</strong> (riflette l&rsquo;assunzione recente) o come "
                "<strong>folato eritrocitario (RBC)</strong> (riflette le riserve a lungo termine degli ultimi 2&ndash;3 mesi).</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marcatore</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Folato sierico</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Folato RBC</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Un folato sierico inferiore a 3&nbsp;ng/mL è generalmente considerato carente. Valori tra 3 e 5&nbsp;ng/mL possono "
                "essere borderline e richiedere ulteriori accertamenti.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di folato basso e alto",
            body_html=(
                "<p>Le cause più frequenti di <strong>folato basso</strong> includono:</p>"
                "<ul>"
                "<li><strong>Apporto alimentare inadeguato</strong> &ndash; diete povere di verdure fresche, legumi e cereali arricchiti.</li>"
                "<li><strong>Malassorbimento</strong> &ndash; celiachia, malattia di Crohn e malattie infiammatorie intestinali.</li>"
                "<li><strong>Alcolismo</strong> &ndash; l&rsquo;alcol cronico riduce l&rsquo;assunzione e compromette assorbimento e metabolismo.</li>"
                "<li><strong>Domanda aumentata</strong> &ndash; gravidanza, allattamento e periodi di rapida crescita cellulare.</li>"
                "<li><strong>Farmaci</strong> &ndash; metotrexato, fenitoina, sulfasalazina e trimetoprim.</li>"
                "</ul>"
                "<p>Il <strong>folato elevato</strong> è raramente clinicamente significativo. Tuttavia, dosi elevate di acido folico possono "
                "mascherare una <a href=\"/it/blog/carenza-vitamina-b12\">carenza di B12</a> concomitante.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi della carenza di folato",
            body_html=(
                "<p>La carenza di folato si sviluppa gradualmente. Con l&rsquo;aggravarsi del deficit i sintomi diventano più evidenti:</p>"
                "<ul>"
                "<li><strong>Stanchezza e debolezza</strong> &ndash; dovute all&rsquo;anemia megaloblastica.</li>"
                "<li><strong>Pallore e dispnea</strong> &ndash; segni classici di anemia.</li>"
                "<li><strong>Afte e glossite</strong> &ndash; lingua liscia, gonfia e arrossata.</li>"
                "<li><strong>Irritabilità e difficoltà di concentrazione</strong> &ndash; il folato basso influisce sull&rsquo;umore.</li>"
                "<li><strong>Omocisteina elevata</strong> &ndash; associata a maggior rischio cardiovascolare.</li>"
                "</ul>"
                "<p>Nelle donne in gravidanza, la conseguenza più grave è il rischio di <strong>difetti del tubo neurale</strong> "
                "nel feto, inclusi spina bifida e anencefalia.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p>Il folato viene raramente interpretato isolatamente. Il medico può prescrivere:</p>"
                "<ul>"
                "<li><strong>Vitamina B12</strong> &ndash; le carenze di folato e B12 producono reperti simili. "
                "Consulta la nostra <a href=\"/it/blog/carenza-vitamina-b12\">guida sulla B12</a>.</li>"
                "<li><strong>Omocisteina</strong> &ndash; elevata in entrambe le carenze.</li>"
                "<li><strong>MCV (Volume Corpuscolare Medio)</strong> &ndash; un MCV alto suggerisce anemia macrocitica.</li>"
                "<li><strong>Emocromo completo (CBC)</strong> &ndash; valuta globuli rossi, emoglobina e morfologia leucocitaria.</li>"
                "<li><strong>Acido metilmalonico (MMA)</strong> &ndash; elevato solo nella carenza di B12.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico",
            body_html=(
                "<p>Consulta il tuo medico se:</p>"
                "<ul>"
                "<li>Il tuo folato sierico è sotto 3&nbsp;ng/mL o il folato RBC è fuori intervallo.</li>"
                "<li>Hai sintomi di anemia: stanchezza inspiegabile, pallore, dispnea o lingua dolente.</li>"
                "<li>Sei in gravidanza o stai pianificando una gravidanza.</li>"
                "<li>Hai una condizione che compromette l&rsquo;assorbimento (celiachia, Crohn, uso cronico di alcol).</li>"
                "<li>Assumi farmaci che interferiscono con il folato (metotrexato, fenitoina).</li>"
                "</ul>"
                "<p>Il medico valuterà se è necessaria un&rsquo;integrazione, identificherà la causa e monitorerà la risposta al trattamento.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come NoryaAI ti aiuta a capire i tuoi risultati di folato",
            body_html=(
                "<p>NoryaAI rende semplice comprendere i tuoi risultati di folato e altri esami del sangue. "
                "<a href=\"/analyze\">Carica il tuo referto</a>&mdash;PDF, foto o scansione&mdash;e la nostra IA:</p>"
                "<ul>"
                "<li>Estrae il folato e tutti gli altri biomarcatori dal referto.</li>"
                "<li>Confronta ogni risultato con intervalli di riferimento specifici per età e sesso.</li>"
                "<li>Segnala i valori anomali con spiegazioni chiare e comprensibili.</li>"
                "<li>Evidenzia le connessioni tra marcatori correlati (es. folato + B12 + omocisteina).</li>"
                "<li>Genera un riepilogo strutturato pronto per il medico.</li>"
                "</ul>"
                "<p>Scopri i nostri <a href=\"/pricing\">piani tariffari</a> per trovare l&rsquo;opzione adatta a te.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza medica",
            body_html=(
                "<p><strong>Questo articolo è fornito a solo scopo informativo ed educativo. Non costituisce consulenza medica, "
                "diagnosi o trattamento. Consulta sempre un professionista sanitario qualificato prima di prendere decisioni basate "
                "sui tuoi risultati di laboratorio. NoryaAI offre analisi automatizzate per aiutarti a comprendere i tuoi referti, "
                "ma non sostituisce il giudizio medico professionale.</strong></p>"
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
            heading="בדיקת פולאט בדם: מה המשמעות של התוצאה שלך?",
            body_html=(
                "<p>פולאט&mdash;הידוע גם כ<strong>ויטמין B9</strong>&mdash;הוא ויטמין מסיס במים החיוני לסינתזת DNA, "
                "ליצירת כדוריות דם אדומות ולחלוקת תאים. ערך הפולאט בבדיקת הדם שלך משקף את כמות הויטמין הזה "
                "במחזור הדם או המאוחסן בכדוריות הדם האדומות.</p>"
                "<p>תוצאה נמוכה עשויה להצביע על חוסר תזונתי, תת-ספיגה או צורך מוגבר (כמו בהריון). "
                "רמות גבוהות נדירות ובדרך כלל אינן מזיקות. מדריך זה נועד לעזור לך להבין את התוצאה שלך.</p>"
                "<p>מאמר זה הוא חינוכי בלבד ואינו מהווה ייעוץ רפואי. תמיד דון בתוצאות הבדיקות עם הרופא שלך.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהו פולאט ומדוע הוא חשוב?",
            body_html=(
                "<p><strong>פולאט</strong> הוא הצורה הטבעית של ויטמין B9 הנמצאת במזונות כמו ירקות עליים כהים, "
                "קטניות ופירות הדר. <strong>חומצה פולית</strong> היא הצורה הסינתטית בתוספי מזון ומזונות מועשרים. "
                "שניהם מומרים בגוף לטטרהידרופולאט (THF), הקו-אנזים הפעיל הנחוץ לסינתזת נוקלאוטידים ותגובות מתילציה.</p>"
                "<p>פולאט נחוץ לייצור כדוריות דם אדומות בריאות. כשהוא חסר, מח העצם מייצר תאים גדולים ובלתי בשלים "
                "הנקראים <em>מגלובלסטים</em>, מה שמוביל ל<strong>אנמיה מגלובלסטית</strong>&mdash;אותו סוג אנמיה "
                "הנראה ב<a href=\"/he/blog/vitamin-b12-deficiency-or-excess\">חסר ויטמין B12</a>.</p>"
                "<p>בהריון, פולאט הכרחי לסגירת צינור העצבים העוברי ב-28 הימים הראשונים. "
                "צריכה מספקת לפני ההריון ובתחילתו מפחיתה דרמטית את הסיכון לפגמים בצינור העצבים כמו ספינה ביפידה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי פולאט תקינים",
            body_html=(
                "<p>ניתן למדוד פולאט כ<strong>פולאט בסרום</strong> (משקף צריכה אחרונה) או כ<strong>פולאט בכדוריות אדומות (RBC)</strong> "
                "(משקף מאגרים לטווח ארוך ב-2&ndash;3 החודשים האחרונים).</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">סמן</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח תקין</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">פולאט בסרום</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">פולאט RBC</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>פולאט בסרום מתחת ל-3 ng/mL נחשב בדרך כלל לחסר. ערכים בין 3 ל-5 ng/mL עשויים להיות גבוליים "
                "ומחייבים הערכה נוספת, במיוחד אם יש תסמינים או הומוציסטאין מוגבר.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לפולאט נמוך וגבוה",
            body_html=(
                "<p>הגורמים השכיחים ביותר ל<strong>פולאט נמוך</strong> (חסר) הם:</p>"
                "<ul>"
                "<li><strong>צריכה תזונתית לא מספקת</strong> &ndash; תזונה דלה בירקות טריים, קטניות ודגנים מועשרים.</li>"
                "<li><strong>תת-ספיגה</strong> &ndash; צליאק, מחלת קרוהן ומחלות מעי דלקתיות.</li>"
                "<li><strong>אלכוהוליזם</strong> &ndash; שימוש כרוני באלכוהול מפחית הן את הצריכה והן את הספיגה.</li>"
                "<li><strong>צורך מוגבר</strong> &ndash; הריון, הנקה ותקופות של צמיחת תאים מהירה.</li>"
                "<li><strong>תרופות</strong> &ndash; מתוטרקסט, פניטואין, סולפסאלזין וטרימתופרים.</li>"
                "</ul>"
                "<p><strong>פולאט גבוה</strong> לרוב אינו משמעותי קלינית. עם זאת, מינונים גבוהים של חומצה פולית "
                "עלולים להסוות <a href=\"/he/blog/vitamin-b12-deficiency-or-excess\">חסר B12</a> במקביל.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמיני חסר פולאט",
            body_html=(
                "<p>חסר פולאט מתפתח בהדרגה. ככל שהחסר מחמיר, התסמינים נעשים בולטים יותר:</p>"
                "<ul>"
                "<li><strong>עייפות וחולשה</strong> &ndash; עקב אנמיה מגלובלסטית שמפחיתה את יכולת נשיאת החמצן.</li>"
                "<li><strong>חיוורון וקוצר נשימה</strong> &ndash; סימנים קלאסיים של אנמיה.</li>"
                "<li><strong>פצעים בפה וגלוסיטיס</strong> &ndash; לשון חלקה, נפוחה ואדומה.</li>"
                "<li><strong>עצבנות וקשיי ריכוז</strong> &ndash; פולאט נמוך עשוי להשפיע על מצב הרוח והקוגניציה.</li>"
                "<li><strong>הומוציסטאין מוגבר</strong> &ndash; קשור לסיכון קרדיווסקולרי מוגבר.</li>"
                "</ul>"
                "<p>בנשים בהריון, התוצאה החמורה ביותר היא הסיכון ל<strong>פגמים בצינור העצבים</strong> בעובר.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות קשורות",
            body_html=(
                "<p>פולאט ממעט להתפרש בבידוד. הרופא שלך עשוי להזמין:</p>"
                "<ul>"
                "<li><strong>ויטמין B12</strong> &ndash; חסר פולאט ו-B12 יוצרים ממצאים דומים. "
                "ראה את <a href=\"/he/blog/vitamin-b12-deficiency-or-excess\">מדריך ה-B12</a> שלנו.</li>"
                "<li><strong>הומוציסטאין</strong> &ndash; מוגבר בשני סוגי החסר.</li>"
                "<li><strong>MCV (נפח כדורית ממוצע)</strong> &ndash; MCV גבוה מרמז על אנמיה מקרוציטית.</li>"
                "<li><strong>ספירת דם מלאה (CBC)</strong> &ndash; מעריכה כדוריות אדומות, המוגלובין ומורפולוגיית תאים לבנים.</li>"
                "<li><strong>חומצה מתילמלונית (MMA)</strong> &ndash; מוגברת רק בחסר B12.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא",
            body_html=(
                "<p>יש לדון בתוצאת הפולאט שלך עם רופא אם:</p>"
                "<ul>"
                "<li>הפולאט בסרום שלך מתחת ל-3 ng/mL או הפולאט ב-RBC מחוץ לטווח.</li>"
                "<li>יש לך תסמיני אנמיה: עייפות בלתי מוסברת, חיוורון, קוצר נשימה או לשון כואבת.</li>"
                "<li>את בהריון או מתכננת הריון.</li>"
                "<li>יש לך מצב הפוגע בספיגה (צליאק, קרוהן, שימוש כרוני באלכוהול).</li>"
                "<li>את נוטלת תרופות המפריעות לפולאט (מתוטרקסט, פניטואין).</li>"
                "</ul>"
                "<p>הרופא שלך יכול לקבוע אם יש צורך בתיסוף, לזהות את הגורם ולעקוב אחר תגובתך לטיפול.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך NoryaAI עוזר לך להבין את תוצאות הפולאט",
            body_html=(
                "<p>NoryaAI מקל על הבנת תוצאות הפולאט ובדיקות הדם האחרות שלך. "
                "<a href=\"/analyze\">העלה את דוח המעבדה שלך</a>&mdash;PDF, תמונה או סריקה&mdash;ומנוע ה-AI שלנו:</p>"
                "<ul>"
                "<li>מחלץ את ערך הפולאט שלך יחד עם כל הסמנים הביולוגיים האחרים.</li>"
                "<li>משווה כל תוצאה לטווחי ייחוס ספציפיים לגיל ולמין.</li>"
                "<li>מסמן ערכים חריגים עם הסברים ברורים ופשוטים.</li>"
                "<li>מדגיש קשרים בין סמנים קשורים (למשל פולאט + B12 + הומוציסטאין).</li>"
                "<li>מייצר סיכום מובנה מוכן לרופא.</li>"
                "</ul>"
                "<p>גלה את <a href=\"/pricing\">תוכניות התמחור</a> שלנו כדי למצוא את האפשרות המתאימה לך.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הצהרה רפואית",
            body_html=(
                "<p><strong>מאמר זה מיועד למטרות מידע וחינוך בלבד. הוא אינו מהווה ייעוץ רפואי, אבחון או טיפול. "
                "התייעץ תמיד עם איש מקצוע רפואי מוסמך לפני קבלת החלטות על סמך תוצאות מעבדה. "
                "NoryaAI מספק ניתוח אוטומטי כדי לעזור לך להבין את הדוחות שלך, אך אינו מחליף שיקול דעת רפואי מקצועי.</strong></p>"
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
            heading="फोलेट रक्त परीक्षण: आपके परिणाम का क्या मतलब है?",
            body_html=(
                "<p>फोलेट&mdash;जिसे <strong>विटामिन B9</strong> भी कहा जाता है&mdash;एक आवश्यक जलघुलनशील विटामिन है "
                "जो DNA संश्लेषण, लाल रक्त कोशिका निर्माण और कोशिका विभाजन में महत्वपूर्ण भूमिका निभाता है। "
                "आपकी रक्त जाँच में फोलेट का स्तर इस विटामिन की मात्रा को दर्शाता है जो आपके सीरम में घूम रही है "
                "या आपकी लाल रक्त कोशिकाओं में संग्रहीत है।</p>"
                "<p>कम फोलेट पोषण की कमी, कुअवशोषण, या बढ़ी हुई माँग (जैसे गर्भावस्था) की ओर इशारा कर सकता है। "
                "ऊँचे स्तर दुर्लभ हैं और आमतौर पर हानिरहित होते हैं। यह गाइड आपके परिणाम को समझने में मदद करती है।</p>"
                "<p>यह लेख शैक्षिक है और चिकित्सा सलाह का विकल्प नहीं है। अपने परिणाम हमेशा डॉक्टर से चर्चा करें।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="फोलेट क्या है और यह क्यों महत्वपूर्ण है?",
            body_html=(
                "<p><strong>फोलेट</strong> विटामिन B9 का प्राकृतिक रूप है जो गहरे हरे पत्तेदार सब्ज़ियों, फलियों और "
                "खट्टे फलों में पाया जाता है। <strong>फोलिक एसिड</strong> सप्लीमेंट्स और फोर्टिफाइड खाद्य पदार्थों में "
                "उपयोग किया जाने वाला सिंथेटिक रूप है। दोनों शरीर में टेट्राहाइड्रोफोलेट (THF) में परिवर्तित होते हैं, "
                "जो न्यूक्लियोटाइड संश्लेषण और मेथिलेशन प्रतिक्रियाओं के लिए आवश्यक जैविक रूप से सक्रिय कोएंज़ाइम है।</p>"
                "<p>स्वस्थ लाल रक्त कोशिकाओं के उत्पादन के लिए फोलेट आवश्यक है। जब यह अपर्याप्त होता है, "
                "तो अस्थि मज्जा असामान्य रूप से बड़ी, अपरिपक्व कोशिकाएँ बनाती है जिन्हें <em>मेगालोब्लास्ट</em> कहा जाता है, "
                "जिससे <strong>मेगालोब्लास्टिक एनीमिया</strong> होता है। यही प्रकार का एनीमिया "
                "<a href=\"/hi/blog/vitamin-b12-deficiency-or-excess\">विटामिन B12 की कमी</a> में भी देखा जाता है।</p>"
                "<p>गर्भावस्था में, भ्रूण के न्यूरल ट्यूब की बंद होने की प्रक्रिया के लिए फोलेट अत्यंत महत्वपूर्ण है। "
                "गर्भधारण से पहले और प्रारंभिक गर्भावस्था में पर्याप्त फोलेट सेवन स्पाइना बिफिडा जैसे न्यूरल ट्यूब दोषों के "
                "जोखिम को काफ़ी कम करता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य फोलेट स्तर",
            body_html=(
                "<p>फोलेट को <strong>सीरम फोलेट</strong> (हालिया सेवन दर्शाता है) या <strong>RBC फोलेट</strong> "
                "(पिछले 2&ndash;3 महीनों के दीर्घकालिक भंडार दर्शाता है) के रूप में मापा जा सकता है।</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">मार्कर</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य सीमा</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">सीरम फोलेट</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">RBC फोलेट</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>3 ng/mL से कम सीरम फोलेट को आमतौर पर कमी माना जाता है। 3 से 5 ng/mL के बीच के मान सीमा रेखा पर हो "
                "सकते हैं और आगे की जाँच की आवश्यकता हो सकती है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="कम और उच्च फोलेट के कारण",
            body_html=(
                "<p><strong>कम फोलेट</strong> (कमी) के सबसे आम कारण:</p>"
                "<ul>"
                "<li><strong>अपर्याप्त आहार सेवन</strong> &ndash; ताज़ी सब्ज़ियों, फलियों और फोर्टिफाइड अनाज में कमी वाला आहार।</li>"
                "<li><strong>कुअवशोषण</strong> &ndash; सीलिएक रोग, क्रोहन रोग और सूजन आंत्र रोग।</li>"
                "<li><strong>शराब की लत</strong> &ndash; पुरानी शराब का सेवन अवशोषण और चयापचय दोनों को बाधित करता है।</li>"
                "<li><strong>बढ़ी हुई माँग</strong> &ndash; गर्भावस्था, स्तनपान और तेज़ कोशिका वृद्धि के दौर।</li>"
                "<li><strong>दवाएँ</strong> &ndash; मेथोट्रेक्सेट, फ़ेनीटोइन, सल्फ़ासैलाज़ीन और ट्राइमेथोप्रिम।</li>"
                "</ul>"
                "<p><strong>उच्च फोलेट</strong> शायद ही कभी चिकित्सकीय रूप से महत्वपूर्ण होता है, लेकिन उच्च खुराक फोलिक एसिड "
                "एक साथ मौजूद <a href=\"/hi/blog/vitamin-b12-deficiency-or-excess\">B12 की कमी</a> को छिपा सकता है।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="फोलेट की कमी के लक्षण",
            body_html=(
                "<p>फोलेट की कमी धीरे-धीरे विकसित होती है। जैसे-जैसे कमी बढ़ती है, लक्षण अधिक स्पष्ट होते जाते हैं:</p>"
                "<ul>"
                "<li><strong>थकान और कमज़ोरी</strong> &ndash; मेगालोब्लास्टिक एनीमिया के कारण ऑक्सीजन ले जाने की क्षमता कम होती है।</li>"
                "<li><strong>पीलापन और साँस फूलना</strong> &ndash; एनीमिया के क्लासिक संकेत।</li>"
                "<li><strong>मुँह के छाले और ग्लोसाइटिस</strong> &ndash; चिकनी, सूजी हुई, लाल जीभ फोलेट की कमी की विशेषता है।</li>"
                "<li><strong>चिड़चिड़ापन और एकाग्रता में कठिनाई</strong> &ndash; कम फोलेट मूड और संज्ञानात्मक कार्य को प्रभावित कर सकता है।</li>"
                "<li><strong>बढ़ा हुआ होमोसिस्टीन</strong> &ndash; हृदय संबंधी जोखिम से जुड़ा हुआ।</li>"
                "</ul>"
                "<p>गर्भवती महिलाओं में सबसे गंभीर परिणाम भ्रूण में <strong>न्यूरल ट्यूब दोष</strong> का जोखिम है।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित परीक्षण",
            body_html=(
                "<p>फोलेट को शायद ही कभी अकेले व्याख्या किया जाता है। आपके डॉक्टर ये परीक्षण भी माँग सकते हैं:</p>"
                "<ul>"
                "<li><strong>विटामिन B12</strong> &ndash; फोलेट और B12 की कमी समान रक्त निष्कर्ष देती हैं। "
                "हमारी <a href=\"/hi/blog/vitamin-b12-deficiency-or-excess\">B12 गाइड</a> देखें।</li>"
                "<li><strong>होमोसिस्टीन</strong> &ndash; दोनों कमियों में बढ़ता है।</li>"
                "<li><strong>MCV (मीन कॉर्पस्कुलर वॉल्यूम)</strong> &ndash; उच्च MCV मैक्रोसाइटिक एनीमिया का सुझाव देता है।</li>"
                "<li><strong>पूर्ण रक्त गणना (CBC)</strong> &ndash; लाल कोशिकाओं, हीमोग्लोबिन और सफ़ेद कोशिका आकारिकी का मूल्यांकन करती है।</li>"
                "<li><strong>मिथाइलमैलोनिक एसिड (MMA)</strong> &ndash; केवल B12 की कमी में बढ़ता है।</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें",
            body_html=(
                "<p>इन स्थितियों में अपने फोलेट परिणाम पर डॉक्टर से चर्चा करें:</p>"
                "<ul>"
                "<li>आपका सीरम फोलेट 3 ng/mL से कम है या RBC फोलेट संदर्भ सीमा से बाहर है।</li>"
                "<li>आपमें एनीमिया के लक्षण हैं: अस्पष्ट थकान, पीलापन, साँस फूलना या दर्दनाक जीभ।</li>"
                "<li>आप गर्भवती हैं या गर्भधारण की योजना बना रही हैं।</li>"
                "<li>आपकी कोई ऐसी स्थिति है जो अवशोषण को प्रभावित करती है (सीलिएक, क्रोहन, पुरानी शराब)।</li>"
                "<li>आप फोलेट में हस्तक्षेप करने वाली दवाएँ ले रहे हैं (मेथोट्रेक्सेट, फ़ेनीटोइन)।</li>"
                "</ul>"
                "<p>आपके डॉक्टर यह निर्धारित कर सकते हैं कि पूरकता की ज़रूरत है या नहीं, कारण की पहचान कर सकते हैं "
                "और उपचार पर आपकी प्रतिक्रिया की निगरानी कर सकते हैं।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI आपके फोलेट परिणामों को समझने में कैसे मदद करता है",
            body_html=(
                "<p>NoryaAI आपके फोलेट और अन्य रक्त परीक्षण परिणामों को आसानी से समझने में मदद करता है। "
                "<a href=\"/analyze\">अपनी लैब रिपोर्ट अपलोड करें</a>&mdash;PDF, फ़ोटो या स्कैन&mdash;और हमारा AI इंजन:</p>"
                "<ul>"
                "<li>रिपोर्ट से आपके फोलेट मान और अन्य सभी बायोमार्कर को निकालता है।</li>"
                "<li>प्रत्येक परिणाम की आयु और लिंग-विशिष्ट संदर्भ सीमाओं से तुलना करता है।</li>"
                "<li>असामान्य मानों को स्पष्ट, सरल भाषा में समझाता है।</li>"
                "<li>संबंधित मार्करों के बीच संबंध उजागर करता है (जैसे फोलेट + B12 + होमोसिस्टीन)।</li>"
                "<li>डॉक्टर के लिए तैयार एक संरचित सारांश तैयार करता है।</li>"
                "</ul>"
                "<p>हमारी <a href=\"/pricing\">मूल्य निर्धारण योजनाएँ</a> देखें और अपनी ज़रूरत के अनुसार विकल्प चुनें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="चिकित्सा अस्वीकरण",
            body_html=(
                "<p><strong>यह लेख केवल सूचनात्मक और शैक्षिक उद्देश्यों के लिए है। यह चिकित्सा सलाह, निदान या उपचार नहीं है। "
                "अपने लैब परिणामों के आधार पर कोई भी निर्णय लेने से पहले हमेशा एक योग्य स्वास्थ्य पेशेवर से परामर्श करें। "
                "NoryaAI आपकी रिपोर्ट को समझने में मदद के लिए स्वचालित विश्लेषण प्रदान करता है, लेकिन यह पेशेवर चिकित्सा "
                "निर्णय का विकल्प नहीं है।</strong></p>"
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
            heading="تحليل الفولات في الدم: ماذا تعني نتيجتك؟",
            body_html=(
                "<p>الفولات&mdash;المعروف أيضاً بـ<strong>فيتامين B9</strong>&mdash;هو فيتامين أساسي قابل للذوبان في الماء "
                "يلعب دوراً حاسماً في تخليق الحمض النووي وتكوين خلايا الدم الحمراء وانقسام الخلايا. "
                "يعكس مستوى الفولات في تحليل الدم كمية هذا الفيتامين المتداولة في مصل الدم أو المخزّنة في كريات الدم الحمراء.</p>"
                "<p>قد تشير نتيجة منخفضة إلى نقص غذائي أو سوء امتصاص أو زيادة في الاحتياج (كالحمل). "
                "المستويات المرتفعة نادرة وعادة غير ضارة. يهدف هذا الدليل لمساعدتك على فهم نتيجتك.</p>"
                "<p>هذا المقال تثقيفي ولا يحل محل الاستشارة الطبية. ناقش نتائجك دائماً مع طبيبك.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو الفولات ولماذا هو مهم؟",
            body_html=(
                "<p><strong>الفولات</strong> هو الشكل الطبيعي لفيتامين B9 الموجود في الأطعمة مثل الخضروات الورقية الداكنة "
                "والبقوليات والحمضيات. <strong>حمض الفوليك</strong> هو الشكل الصناعي المستخدم في المكملات والأطعمة المدعّمة. "
                "يتم تحويل كليهما في الجسم إلى تتراهيدروفولات (THF)، وهو الإنزيم المساعد النشط اللازم لتخليق النيوكليوتيدات "
                "وتفاعلات المثيلة.</p>"
                "<p>الفولات ضروري لإنتاج خلايا دم حمراء سليمة. عند نقصه، ينتج نخاع العظم خلايا كبيرة غير ناضجة تسمى "
                "<em>أرومات ضخمة</em>، مما يؤدي إلى <strong>فقر الدم الأرومي الضخم</strong>. وهو نفس نوع فقر الدم الذي يُرى "
                "في <a href=\"/ar/blog/vitamin-b12-deficiency-or-excess\">نقص فيتامين B12</a>.</p>"
                "<p>أثناء الحمل، يعد الفولات حاسماً لإغلاق الأنبوب العصبي للجنين خلال أول 28 يوماً. "
                "التناول الكافي قبل الحمل وفي بدايته يقلل بشكل كبير من خطر عيوب الأنبوب العصبي مثل الصلب المشقوق.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدلات الطبيعية للفولات",
            body_html=(
                "<p>يمكن قياس الفولات كـ<strong>فولات مصلي</strong> (يعكس التناول الأخير) أو <strong>فولات كريات الدم الحمراء (RBC)</strong> "
                "(يعكس المخازن طويلة الأمد خلال 2&ndash;3 أشهر الماضية).</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المؤشر</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق الطبيعي</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">فولات مصلي</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&thinsp;3 ng/mL (&gt;&thinsp;7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">فولات RBC</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140&ndash;628 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>يُعتبر فولات مصلي أقل من 3 ng/mL ناقصاً عادة. القيم بين 3 و5 ng/mL قد تكون حدّية "
                "وتحتاج تقييماً إضافياً، خاصة مع وجود أعراض أو ارتفاع الهوموسيستين.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب الفولات المنخفض والمرتفع",
            body_html=(
                "<p>الأسباب الأكثر شيوعاً لـ<strong>الفولات المنخفض</strong> (النقص):</p>"
                "<ul>"
                "<li><strong>تناول غذائي غير كافٍ</strong> &ndash; أنظمة غذائية فقيرة بالخضروات الطازجة والبقوليات.</li>"
                "<li><strong>سوء الامتصاص</strong> &ndash; الداء البطني ومرض كرون وأمراض الأمعاء الالتهابية.</li>"
                "<li><strong>إدمان الكحول</strong> &ndash; يقلل التناول ويعطل امتصاص الفولات واستقلابه.</li>"
                "<li><strong>زيادة الاحتياج</strong> &ndash; الحمل والرضاعة وفترات النمو الخلوي السريع.</li>"
                "<li><strong>الأدوية</strong> &ndash; الميثوتريكسات والفينيتوين والسلفاسالازين والتريميثوبريم.</li>"
                "</ul>"
                "<p><strong>الفولات المرتفع</strong> نادراً ما يكون ذا أهمية سريرية، لكن جرعات عالية من حمض الفوليك "
                "قد تخفي <a href=\"/ar/blog/vitamin-b12-deficiency-or-excess\">نقص B12</a> المصاحب.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض نقص الفولات",
            body_html=(
                "<p>يتطور نقص الفولات تدريجياً. مع تفاقم النقص تصبح الأعراض أكثر وضوحاً:</p>"
                "<ul>"
                "<li><strong>إرهاق وضعف</strong> &ndash; بسبب فقر الدم الأرومي الضخم الذي يقلل قدرة الدم على حمل الأكسجين.</li>"
                "<li><strong>شحوب وضيق تنفس</strong> &ndash; علامات كلاسيكية لفقر الدم.</li>"
                "<li><strong>تقرحات الفم والتهاب اللسان</strong> &ndash; لسان أملس ومتورم وأحمر.</li>"
                "<li><strong>سرعة الانفعال وصعوبة التركيز</strong> &ndash; نقص الفولات يؤثر على المزاج والإدراك.</li>"
                "<li><strong>ارتفاع الهوموسيستين</strong> &ndash; مرتبط بزيادة خطر أمراض القلب والأوعية الدموية.</li>"
                "</ul>"
                "<p>عند النساء الحوامل، أخطر نتيجة هي خطر <strong>عيوب الأنبوب العصبي</strong> لدى الجنين.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="التحاليل المرتبطة",
            body_html=(
                "<p>نادراً ما يُفسّر الفولات بمعزل عن غيره. قد يطلب طبيبك:</p>"
                "<ul>"
                "<li><strong>فيتامين B12</strong> &ndash; نقص الفولات وB12 ينتجان نتائج مشابهة. "
                "انظر <a href=\"/ar/blog/vitamin-b12-deficiency-or-excess\">دليل B12</a>.</li>"
                "<li><strong>الهوموسيستين</strong> &ndash; يرتفع في كلا النقصين.</li>"
                "<li><strong>MCV (متوسط حجم الكرية)</strong> &ndash; MCV مرتفع يشير إلى فقر دم كبير الكريات.</li>"
                "<li><strong>تعداد الدم الكامل (CBC)</strong> &ndash; يقيّم الكريات الحمراء والهيموغلوبين والبنية الخلوية.</li>"
                "<li><strong>حمض الميثيل مالونيك (MMA)</strong> &ndash; يرتفع فقط في نقص B12.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب",
            body_html=(
                "<p>يجب مناقشة نتيجة الفولات مع طبيب إذا:</p>"
                "<ul>"
                "<li>فولات المصل لديك أقل من 3 ng/mL أو فولات RBC خارج النطاق.</li>"
                "<li>لديك أعراض فقر دم: إرهاق غير مبرر، شحوب، ضيق تنفس أو لسان مؤلم.</li>"
                "<li>أنتِ حامل أو تخططين للحمل.</li>"
                "<li>لديك حالة تؤثر على الامتصاص (داء بطني، كرون، استخدام كحول مزمن).</li>"
                "<li>تتناول أدوية تتداخل مع الفولات (ميثوتريكسات، فينيتوين).</li>"
                "</ul>"
                "<p>يمكن لطبيبك تحديد ما إذا كنت بحاجة لمكملات، وتحديد السبب الأساسي، ومراقبة استجابتك للعلاج.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يساعدك NoryaAI في فهم نتائج الفولات",
            body_html=(
                "<p>NoryaAI يسهّل فهم نتائج الفولات وتحاليل الدم الأخرى. "
                "<a href=\"/analyze\">ارفع تقرير مختبرك</a>&mdash;PDF أو صورة أو مسح ضوئي&mdash;ومحرك الذكاء الاصطناعي لدينا:</p>"
                "<ul>"
                "<li>يستخرج قيمة الفولات لديك مع جميع المؤشرات الحيوية الأخرى.</li>"
                "<li>يقارن كل نتيجة بنطاقات مرجعية خاصة بالعمر والجنس.</li>"
                "<li>يُبرز القيم غير الطبيعية مع شروحات واضحة وبسيطة.</li>"
                "<li>يُظهر الروابط بين المؤشرات المرتبطة (مثل الفولات + B12 + الهوموسيستين).</li>"
                "<li>ينشئ ملخصاً منظماً جاهزاً للطبيب.</li>"
                "</ul>"
                "<p>اكتشف <a href=\"/pricing\">خطط الأسعار</a> لدينا للعثور على الخيار المناسب لك.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية الطبية",
            body_html=(
                "<p><strong>هذا المقال لأغراض إعلامية وتثقيفية فقط. لا يشكّل نصيحة طبية أو تشخيصاً أو علاجاً. "
                "استشر دائماً مختصاً صحياً مؤهلاً قبل اتخاذ أي قرارات بناءً على نتائج مختبرك. "
                "يوفر NoryaAI تحليلاً آلياً لمساعدتك على فهم تقاريرك، لكنه ليس بديلاً عن الحكم الطبي المهني.</strong></p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Aggregators
# ---------------------------------------------------------------------------
def get_folate_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Folate article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_folate_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Folate article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a folate blood test?",
             "answer": "A folate blood test measures the level of vitamin B9 in your blood. It can be measured as serum folate (reflecting recent intake) or RBC folate (reflecting stores over 2–3 months). Normal serum folate is above 3 ng/mL (>7 nmol/L)."},
            {"question": "What causes low folate levels?",
             "answer": "Common causes include poor dietary intake of leafy greens and legumes, malabsorption conditions like celiac or Crohn's disease, chronic alcohol use, increased demand during pregnancy, and medications such as methotrexate and phenytoin."},
            {"question": "What are the symptoms of folate deficiency?",
             "answer": "Symptoms include fatigue and weakness from megaloblastic anemia, pallor, shortness of breath, mouth sores, a smooth red tongue (glossitis), irritability, difficulty concentrating, and elevated homocysteine levels."},
            {"question": "Is folate the same as folic acid?",
             "answer": "Not exactly. Folate is the natural form of vitamin B9 found in foods, while folic acid is the synthetic form used in supplements and fortified foods. Both are converted to the active form (tetrahydrofolate) in the body."},
        ],
        "tr": [
            {"question": "Folat kan testi nedir?",
             "answer": "Folat kan testi, kanınızdaki B9 vitamini düzeyini ölçer. Serum folatı (son alımı yansıtır) veya RBC folatı (2–3 aylık depoları yansıtır) olarak ölçülebilir. Normal serum folatı 3 ng/mL'nin üzerindedir."},
            {"question": "Düşük folat seviyesinin nedenleri nelerdir?",
             "answer": "Yetersiz yeşil yapraklı sebze ve baklagil tüketimi, çölyak veya Crohn gibi emilim bozuklukları, kronik alkol kullanımı, gebelikteki artan ihtiyaç ve metotreksat, fenitoin gibi ilaçlar en sık nedenlerdir."},
            {"question": "Folat eksikliğinin belirtileri nelerdir?",
             "answer": "Megaloblastik anemiye bağlı yorgunluk ve halsizlik, soluk cilt, nefes darlığı, ağız yaraları, pürüzsüz kırmızı dil (glossit), huzursuzluk, konsantrasyon güçlüğü ve yüksek homosistein sayılabilir."},
            {"question": "Folat ile folik asit aynı şey midir?",
             "answer": "Tam olarak değil. Folat, gıdalarda bulunan B9 vitamininin doğal formudur; folik asit ise takviyelerde ve zenginleştirilmiş gıdalarda kullanılan sentetik formdur. Her ikisi de vücutta aktif forma dönüştürülür."},
        ],
        "es": [
            {"question": "¿Qué es un análisis de folato en sangre?",
             "answer": "Un análisis de folato mide el nivel de vitamina B9 en la sangre. Puede medirse como folato sérico (ingesta reciente) o folato eritrocitario (reservas a largo plazo). El valor normal de folato sérico es superior a 3 ng/mL."},
            {"question": "¿Qué causa niveles bajos de folato?",
             "answer": "Las causas comunes incluyen dieta pobre en verduras y legumbres, enfermedades de malabsorción como celiaquía o Crohn, consumo crónico de alcohol, mayor demanda en el embarazo y medicamentos como metotrexato y fenitoína."},
            {"question": "¿Cuáles son los síntomas de deficiencia de folato?",
             "answer": "Los síntomas incluyen fatiga y debilidad por anemia megaloblástica, palidez, dificultad para respirar, úlceras bucales, lengua lisa y roja (glositis), irritabilidad y homocisteína elevada."},
            {"question": "¿El folato es lo mismo que el ácido fólico?",
             "answer": "No exactamente. El folato es la forma natural de la vitamina B9 en los alimentos, mientras que el ácido fólico es la forma sintética usada en suplementos y alimentos fortificados."},
        ],
        "de": [
            {"question": "Was ist ein Folat-Bluttest?",
             "answer": "Ein Folat-Bluttest misst den Vitamin-B9-Spiegel im Blut. Er kann als Serumfolat (aktuelle Zufuhr) oder Erythrozyten-Folat (Langzeitspeicher über 2–3 Monate) bestimmt werden. Normales Serumfolat liegt über 3 ng/mL."},
            {"question": "Was verursacht niedrige Folatwerte?",
             "answer": "Häufige Ursachen sind unzureichende Ernährung mit wenig Gemüse und Hülsenfrüchten, Malabsorption bei Zöliakie oder Morbus Crohn, chronischer Alkoholkonsum, erhöhter Bedarf in der Schwangerschaft und Medikamente wie Methotrexat."},
            {"question": "Welche Symptome hat ein Folatmangel?",
             "answer": "Symptome umfassen Müdigkeit und Schwäche durch megaloblastäre Anämie, Blässe, Kurzatmigkeit, Mundgeschwüre, glatte rote Zunge (Glossitis), Reizbarkeit und erhöhtes Homocystein."},
            {"question": "Ist Folat dasselbe wie Folsäure?",
             "answer": "Nicht ganz. Folat ist die natürliche Form von Vitamin B9 in Lebensmitteln, während Folsäure die synthetische Form in Nahrungsergänzungsmitteln und angereicherten Lebensmitteln ist."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'une analyse de folate sanguin ?",
             "answer": "Une analyse de folate mesure le taux de vitamine B9 dans le sang. Il peut être mesuré en folate sérique (apport récent) ou folate érythrocytaire (réserves sur 2–3 mois). La normale du folate sérique est supérieure à 3 ng/mL."},
            {"question": "Quelles sont les causes d'un folate bas ?",
             "answer": "Les causes courantes incluent un régime pauvre en légumes et légumineuses, des maladies de malabsorption (cœliaque, Crohn), l'alcoolisme chronique, une demande accrue en grossesse et des médicaments comme le méthotrexate."},
            {"question": "Quels sont les symptômes d'une carence en folate ?",
             "answer": "Les symptômes comprennent fatigue et faiblesse liées à l'anémie mégaloblastique, pâleur, essoufflement, aphtes, langue lisse et rouge (glossite), irritabilité et homocystéine élevée."},
            {"question": "Le folate et l'acide folique sont-ils la même chose ?",
             "answer": "Pas exactement. Le folate est la forme naturelle de la vitamine B9 dans les aliments, tandis que l'acide folique est la forme synthétique utilisée dans les compléments et aliments enrichis."},
        ],
        "it": [
            {"question": "Cos'è un esame del folato nel sangue?",
             "answer": "Un esame del folato misura il livello di vitamina B9 nel sangue. Può essere misurato come folato sierico (assunzione recente) o folato eritrocitario (riserve a lungo termine su 2–3 mesi). Il valore normale del folato sierico è superiore a 3 ng/mL."},
            {"question": "Cosa causa livelli bassi di folato?",
             "answer": "Le cause comuni includono dieta povera di verdure e legumi, malassorbimento da celiachia o Crohn, alcolismo cronico, aumento della domanda in gravidanza e farmaci come metotrexato e fenitoina."},
            {"question": "Quali sono i sintomi della carenza di folato?",
             "answer": "I sintomi includono stanchezza e debolezza da anemia megaloblastica, pallore, dispnea, afte, lingua liscia e rossa (glossite), irritabilità e omocisteina elevata."},
            {"question": "Il folato e l'acido folico sono la stessa cosa?",
             "answer": "Non esattamente. Il folato è la forma naturale della vitamina B9 negli alimenti, mentre l'acido folico è la forma sintetica usata negli integratori e nei cibi arricchiti."},
        ],
        "he": [
            {"question": "מהי בדיקת פולאט בדם?",
             "answer": "בדיקת פולאט מודדת את רמת ויטמין B9 בדם. ניתן למדוד כפולאט בסרום (צריכה אחרונה) או פולאט RBC (מאגרים לאורך 2–3 חודשים). פולאט תקין בסרום מעל 3 ng/mL."},
            {"question": "מה גורם לרמות פולאט נמוכות?",
             "answer": "גורמים שכיחים כוללים תזונה דלה בירקות ובקטניות, מצבי תת-ספיגה כמו צליאק או קרוהן, שימוש כרוני באלכוהול, צורך מוגבר בהריון ותרופות כמו מתוטרקסט ופניטואין."},
            {"question": "מהם תסמיני חסר פולאט?",
             "answer": "התסמינים כוללים עייפות וחולשה מאנמיה מגלובלסטית, חיוורון, קוצר נשימה, פצעים בפה, לשון חלקה ואדומה (גלוסיטיס), עצבנות והומוציסטאין מוגבר."},
            {"question": "האם פולאט וחומצה פולית זה אותו דבר?",
             "answer": "לא בדיוק. פולאט הוא הצורה הטבעית של ויטמין B9 במזון, בעוד חומצה פולית היא הצורה הסינתטית בתוספי מזון ומזונות מועשרים. שניהם מומרים לצורה הפעילה בגוף."},
        ],
        "hi": [
            {"question": "फोलेट रक्त परीक्षण क्या है?",
             "answer": "फोलेट रक्त परीक्षण आपके रक्त में विटामिन B9 के स्तर को मापता है। इसे सीरम फोलेट (हालिया सेवन) या RBC फोलेट (2–3 महीनों के भंडार) के रूप में मापा जा सकता है। सामान्य सीरम फोलेट 3 ng/mL से ऊपर होता है।"},
            {"question": "कम फोलेट के कारण क्या हैं?",
             "answer": "सामान्य कारणों में सब्ज़ियों और फलियों की कमी वाला आहार, सीलिएक या क्रोहन जैसे कुअवशोषण रोग, पुरानी शराब, गर्भावस्था में बढ़ी माँग और मेथोट्रेक्सेट, फ़ेनीटोइन जैसी दवाएँ शामिल हैं।"},
            {"question": "फोलेट की कमी के लक्षण क्या हैं?",
             "answer": "लक्षणों में मेगालोब्लास्टिक एनीमिया से थकान और कमज़ोरी, पीलापन, साँस फूलना, मुँह के छाले, चिकनी लाल जीभ (ग्लोसाइटिस), चिड़चिड़ापन और बढ़ा हुआ होमोसिस्टीन शामिल हैं।"},
            {"question": "क्या फोलेट और फोलिक एसिड एक ही हैं?",
             "answer": "बिल्कुल नहीं। फोलेट खाद्य पदार्थों में पाया जाने वाला विटामिन B9 का प्राकृतिक रूप है, जबकि फोलिक एसिड सप्लीमेंट्स और फोर्टिफाइड खाद्य पदार्थों में उपयोग किया जाने वाला सिंथेटिक रूप है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل الفولات في الدم؟",
             "answer": "تحليل الفولات يقيس مستوى فيتامين B9 في الدم. يمكن قياسه كفولات مصلي (يعكس التناول الأخير) أو فولات كريات الدم الحمراء (يعكس المخازن لمدة 2–3 أشهر). الفولات المصلي الطبيعي أعلى من 3 ng/mL."},
            {"question": "ما أسباب انخفاض الفولات؟",
             "answer": "الأسباب الشائعة تشمل نظاماً غذائياً فقيراً بالخضروات والبقوليات، اضطرابات سوء الامتصاص كالداء البطني وكرون، إدمان الكحول المزمن، زيادة الاحتياج أثناء الحمل وأدوية مثل الميثوتريكسات والفينيتوين."},
            {"question": "ما أعراض نقص الفولات؟",
             "answer": "تشمل الأعراض الإرهاق والضعف من فقر الدم الأرومي الضخم، والشحوب، وضيق التنفس، وتقرحات الفم، ولسان أملس أحمر (التهاب اللسان)، والانفعال، وارتفاع الهوموسيستين."},
            {"question": "هل الفولات وحمض الفوليك نفس الشيء؟",
             "answer": "ليس تماماً. الفولات هو الشكل الطبيعي لفيتامين B9 في الأغذية، بينما حمض الفوليك هو الشكل الصناعي المستخدم في المكملات والأطعمة المدعّمة. يتم تحويل كليهما إلى الشكل النشط في الجسم."},
        ],
    }
