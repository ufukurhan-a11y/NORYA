# -*- coding: utf-8 -*-
"""
ESR (Erythrocyte Sedimentation Rate) blog article — full body content for all 9 languages.
Used by blog_i18n._article_esr().
Sections: intro, what-is, normal-ranges, causes, symptoms,
related-tests, when-to-see-doctor, how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# English
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="ESR high: what your erythrocyte sedimentation rate means",
            body_html=(
                "<p>The erythrocyte sedimentation rate (ESR), often called the <em>sed rate</em>, is one of the oldest and simplest blood tests still in routine use. "
                "It measures how quickly red blood cells settle to the bottom of a vertical tube over one hour. A faster-than-normal rate suggests that something in the body "
                "is driving inflammation, but the ESR cannot tell you exactly what. Think of it as a general alarm bell rather than a precise diagnosis.</p>"
                "<p>This guide explains what ESR measures, how to read your result against age- and sex-specific reference ranges, "
                "the most common reasons for an elevated or low ESR, and when to follow up with your doctor. "
                "It is educational content, not a medical diagnosis&mdash;always discuss your results with a healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is ESR and how is it measured?",
            body_html=(
                "<p>The <strong>erythrocyte sedimentation rate</strong> measures the distance (in millimetres) that red blood cells fall in a standardised tube over 60 minutes. "
                "Under normal conditions, red cells repel each other due to their negative surface charge and settle slowly. "
                "When inflammation is present, the liver produces higher levels of acute-phase proteins&mdash;especially <strong>fibrinogen</strong>&mdash;"
                "that neutralise the surface charge and cause red cells to clump together into stacks called <em>rouleaux</em>. "
                "These stacks are heavier and fall faster, producing a higher ESR reading.</p>"
                "<p>The test is typically performed using the <strong>Westergren method</strong>: blood mixed with sodium citrate is drawn into a 200 mm vertical tube "
                "and left undisturbed for one hour. The result is reported as mm/hr. Although simple, the ESR remains a useful screening tool "
                "for detecting and monitoring inflammatory and infectious diseases.</p>"
                "<p>It is important to understand that ESR is a <strong>non-specific</strong> marker. An elevated result tells your doctor that inflammation is likely present, "
                "but it does not identify the cause. Additional tests are needed to pinpoint the source.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal ESR ranges",
            body_html=(
                "<p>ESR reference ranges depend on age and sex. The widely used Westergren upper limits are:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Upper limit (mm/hr)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Men under 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 15</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Men over 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Women under 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Women over 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 30</td></tr>'
                "</tbody></table>"
                "<p>A common rule of thumb is: upper limit for men = age ÷ 2; for women = (age + 10) ÷ 2. "
                "ESR tends to rise with age and is generally higher in women. Pregnancy can also physiologically increase ESR. "
                "Always compare your result to the reference range on your own laboratory report.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high ESR",
            body_html=(
                "<p>A moderately elevated ESR (20&ndash;60 mm/hr) can occur with a wide range of conditions. "
                "<strong>Infections</strong>&mdash;bacterial, viral, or fungal&mdash;are among the most common triggers. "
                "<strong>Autoimmune and inflammatory diseases</strong> such as rheumatoid arthritis, systemic lupus erythematosus (SLE), "
                "polymyalgia rheumatica, and giant-cell arteritis characteristically raise the ESR, sometimes markedly.</p>"
                "<p><strong>Cancer</strong>&mdash;particularly lymphoma, multiple myeloma, and metastatic disease&mdash;can push the ESR above 100 mm/hr. "
                "An ESR above 100 is considered highly elevated and warrants a thorough clinical workup including evaluation for malignancy, "
                "severe infection, and renal disease. <strong>Anemia</strong> also increases ESR because fewer red cells settle more quickly in plasma.</p>"
                "<p>Other common causes include <strong>pregnancy</strong>, <strong>advanced age</strong>, <strong>obesity</strong>, "
                "and <strong>chronic kidney disease</strong>. Certain medications (e.g. oral contraceptives, heparin) can also influence the result. "
                "Conversely, conditions such as polycythemia, sickle cell disease, and extreme leukocytosis can cause a <em>low</em> ESR "
                "by interfering with rouleaux formation. Because the list of causes is so broad, an elevated ESR always requires clinical correlation&mdash;"
                "your doctor will interpret it in the context of your symptoms, physical examination, and other lab results such as "
                "<a href=\"/en/blog/crp-inflammation-marker\">CRP</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms associated with elevated ESR",
            body_html=(
                "<p>ESR itself does not cause symptoms&mdash;it is a laboratory marker that reflects an underlying process. "
                "The symptoms you experience depend entirely on the condition driving the inflammation. "
                "Patients with infections may have fever, chills, and localised pain. Those with autoimmune diseases may experience joint pain, "
                "stiffness, skin rashes, and fatigue. Cancer-related elevations may present with unexplained weight loss, night sweats, or lymphadenopathy.</p>"
                "<p>Some people with a mildly elevated ESR have no symptoms at all&mdash;the finding may be incidental on routine blood work. "
                "Even in this case, your doctor may recommend follow-up testing to determine whether an underlying condition is present. "
                "A very high ESR (above 100 mm/hr) with constitutional symptoms (fever, weight loss, fatigue) should prompt an urgent clinical evaluation.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests your doctor may order",
            body_html=(
                "<p>Because ESR is non-specific, it is almost always paired with more targeted tests. "
                "<strong><a href=\"/en/blog/crp-inflammation-marker\">C-reactive protein (CRP)</a></strong> is another acute-phase reactant "
                "that rises and falls more quickly than ESR, making it useful for tracking short-term changes in inflammation. "
                "Together, ESR and CRP provide complementary information&mdash;CRP can confirm that the ESR elevation is due to active inflammation "
                "rather than other factors like anemia or aging.</p>"
                "<p>A <strong>complete blood count (CBC)</strong> is essential to check for anemia, infection (elevated white cells), "
                "or blood cancers. If autoimmune disease is suspected, tests such as <strong>ANA</strong> (antinuclear antibodies), "
                "<strong>RF</strong> (rheumatoid factor), and <strong>anti-CCP</strong> may be ordered. "
                "For suspected malignancy, protein electrophoresis (SPEP), imaging studies, and sometimes a biopsy are considered.</p>"
                "<p>Your doctor will choose the appropriate investigations based on the clinical picture. "
                "An isolated mildly elevated ESR in an otherwise healthy person may only need repeat testing in a few weeks to see if it normalises.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Discuss any ESR result outside the reference range with your healthcare provider. "
                "Although a mildly elevated ESR can be benign&mdash;especially in older adults or during pregnancy&mdash;it deserves at least a conversation. "
                "Seek <strong>prompt</strong> medical attention if your ESR is very high (above 100 mm/hr) or if you are experiencing symptoms such as "
                "unexplained fever, significant weight loss, severe joint pain, persistent fatigue, or night sweats.</p>"
                "<p>If you have a known inflammatory condition (e.g. rheumatoid arthritis, lupus, polymyalgia rheumatica), "
                "your doctor may use serial ESR measurements to monitor disease activity and treatment response. "
                "A rising ESR in this context may indicate a flare, while a falling ESR suggests improvement.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your ESR",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare. Upload your blood test report at "
                "<a href=\"/analyze\">noryaai.com/analyze</a> and receive a clear, structured summary that flags your ESR alongside related markers "
                "like CRP and CBC values. The report provides context on what the numbers may mean and helps you ask more informed questions at your appointment.</p>"
                "<p>Whether you are monitoring a chronic inflammatory condition or seeing an unexpected elevation on routine blood work, "
                "Norya organises your results so you can focus on the conversation with your doctor. "
                "For plan options and pricing, visit our <a href=\"/pricing\">pricing page</a>.</p>"
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
# Turkish
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Sedimentasyon (ESR) yüksekliği: sonucunuz ne anlama geliyor?",
            body_html=(
                "<p>Eritrosit sedimentasyon hızı (ESR), halk arasında <em>sedimentasyon</em> veya <em>çökelme hızı</em> olarak bilinen, "
                "hâlâ rutin kullanımdaki en eski ve en basit kan testlerinden biridir. Kırmızı kan hücrelerinin dikey bir tüpte bir saat içinde ne kadar hızlı çökeldiğini ölçer. "
                "Normalden hızlı bir çökelme, vücutta bir şeyin iltihaplanmayı tetiklediğini düşündürür; ancak ESR tek başına nedenini söyleyemez. "
                "Onu kesin bir tanı yerine genel bir alarm zili olarak düşünün.</p>"
                "<p>Bu rehber ESR&rsquo;nin ne ölçtüğünü, yaşa ve cinsiyete göre referans aralıklarını, yüksek veya düşük ESR&rsquo;nin en yaygın nedenlerini "
                "ve ne zaman hekime başvurmanız gerektiğini açıklar. Eğitim amaçlıdır, teşhis değildir&mdash;"
                "sonuçlarınızı mutlaka bir sağlık profesyoneliyle değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ESR (sedimentasyon) nedir ve nasıl ölçülür?",
            body_html=(
                "<p><strong>Eritrosit sedimentasyon hızı</strong>, kırmızı kan hücrelerinin standart bir tüpte 60 dakikada düştüğü mesafeyi (milimetre cinsinden) ölçer. "
                "Normal koşullarda kırmızı hücreler yüzey yüklerinin birbirini itmesi nedeniyle yavaş çökelir. "
                "İltihap olduğunda karaciğer daha fazla akut faz proteini&mdash;özellikle <strong>fibrinojen</strong>&mdash;üretir; "
                "bu proteinler yüzey yükünü nötralize ederek kırmızı hücrelerin <em>rulo</em> denilen yığınlar halinde birleşmesine neden olur. "
                "Bu yığınlar daha ağırdır ve daha hızlı düşerek yüksek ESR değeri verir.</p>"
                "<p>Test genellikle <strong>Westergren yöntemi</strong> ile yapılır: sodyum sitratla karıştırılmış kan 200 mm&rsquo;lik dikey bir tüpe çekilerek "
                "bir saat bozulmadan bırakılır. Sonuç mm/saat olarak raporlanır. Basit olmasına rağmen ESR, inflamatuar ve enfeksiyöz hastalıkları "
                "tespit etmek ve izlemek için hâlâ yararlı bir tarama aracıdır.</p>"
                "<p>ESR&rsquo;nin <strong>spesifik olmayan</strong> bir belirteç olduğunu anlamak önemlidir. Yüksek bir sonuç hekiminize "
                "iltihaplanmanın muhtemelen mevcut olduğunu söyler, ancak nedeni belirlemez. Kaynağı saptamak için ek testler gerekir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal sedimentasyon (ESR) aralıkları",
            body_html=(
                "<p>ESR referans aralıkları yaşa ve cinsiyete bağlıdır. Yaygın kullanılan Westergren üst sınırları:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Üst sınır (mm/saat)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50 yaş altı erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 15</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50 yaş üstü erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50 yaş altı kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50 yaş üstü kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 30</td></tr>'
                "</tbody></table>"
                "<p>Genel kural: erkeklerde üst sınır ≈ yaş ÷ 2; kadınlarda ≈ (yaş + 10) ÷ 2. "
                "ESR yaşla birlikte yükselme eğilimindedir ve kadınlarda genellikle daha yüksektir. Gebelik ESR&rsquo;yi fizyolojik olarak artırabilir. "
                "Sonucunuzu her zaman kendi laboratuvar raporunuzdaki referans aralığıyla karşılaştırın.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Sedimentasyon (ESR) yüksekliğinin nedenleri",
            body_html=(
                "<p>Orta düzeyde yüksek ESR (20&ndash;60 mm/saat) pek çok durumda görülebilir. "
                "<strong>Enfeksiyonlar</strong>&mdash;bakteriyel, viral veya fungal&mdash;en yaygın tetikleyiciler arasındadır. "
                "<strong>Otoimmün ve inflamatuar hastalıklar</strong> (romatoid artrit, sistemik lupus eritematozus, polimiyalji romatika, dev hücreli arterit) "
                "karakteristik olarak ESR&rsquo;yi yükseltir, bazen belirgin şekilde.</p>"
                "<p><strong>Kanser</strong>&mdash;özellikle lenfoma, multipl miyelom ve metastatik hastalık&mdash;ESR&rsquo;yi 100 mm/saat&rsquo;in üzerine çıkarabilir. "
                "100&rsquo;ün üzerindeki ESR çok yüksek kabul edilir ve malignite, ciddi enfeksiyon ve böbrek hastalığı dahil kapsamlı bir klinik değerlendirme gerektirir. "
                "<strong>Anemi</strong> de ESR&rsquo;yi artırır çünkü daha az sayıda kırmızı hücre plazmada daha hızlı çökelir.</p>"
                "<p>Diğer yaygın nedenler arasında <strong>gebelik</strong>, <strong>ileri yaş</strong>, <strong>obezite</strong> ve "
                "<strong>kronik böbrek hastalığı</strong> sayılabilir. Bazı ilaçlar (oral kontraseptifler, heparin vb.) da sonucu etkileyebilir. "
                "Öte yandan polisitemi, orak hücre hastalığı ve aşırı lökositoz gibi durumlar rulo oluşumunu bozarak ESR&rsquo;yi <em>düşürebilir</em>. "
                "Nedenlerin listesi çok geniş olduğundan, yüksek ESR her zaman klinik korelasyon gerektirir&mdash;hekiminiz bunu belirtileriniz, "
                "muayene bulguları ve <a href=\"/tr/blog/crp-inflamasyon-belirteci\">CRP</a> gibi diğer sonuçlarla birlikte yorumlayacaktır.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Yüksek ESR ile ilişkili belirtiler",
            body_html=(
                "<p>ESR&rsquo;nin kendisi belirti oluşturmaz&mdash;altta yatan süreci yansıtan bir laboratuvar belirtecidir. "
                "Yaşadığınız belirtiler tamamen iltihaplanmayı tetikleyen duruma bağlıdır. "
                "Enfeksiyonu olan hastalarda ateş, titreme ve lokalize ağrı olabilir. Otoimmün hastalığı olanlarda eklem ağrısı, "
                "sertlik, deri döküntüleri ve yorgunluk görülebilir. Kanserle ilişkili yükselmelerde açıklanamayan kilo kaybı, "
                "gece terlemeleri veya lenfadenopati olabilir.</p>"
                "<p>Hafif yüksek ESR&rsquo;si olan bazı kişilerin hiç belirtisi yoktur&mdash;bulgu rutin kan çalışmasında rastlantısal olarak ortaya çıkabilir. "
                "Bu durumda bile hekiminiz altta yatan bir durum olup olmadığını belirlemek için takip testleri önerebilir. "
                "Ateş, kilo kaybı ve yorgunluk gibi genel belirtilerle birlikte çok yüksek ESR (100 mm/saat üzerinde) acil klinik değerlendirme gerektirmelidir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Hekiminizin isteyebileceği ilişkili testler",
            body_html=(
                "<p>ESR spesifik olmadığından neredeyse her zaman daha hedefli testlerle birlikte değerlendirilir. "
                "<strong><a href=\"/tr/blog/crp-inflamasyon-belirteci\">C-reaktif protein (CRP)</a></strong>, ESR&rsquo;den daha hızlı yükselip düşen "
                "bir akut faz reaktanıdır ve kısa vadeli iltihap değişikliklerini izlemek için yararlıdır. "
                "Birlikte değerlendirildiklerinde ESR ve CRP tamamlayıcı bilgi sunar.</p>"
                "<p><strong>Tam kan sayımı (CBC)</strong>, anemi, enfeksiyon veya kan kanserleri açısından kontrol için gereklidir. "
                "Otoimmün hastalık şüphesinde <strong>ANA</strong>, <strong>RF</strong> ve <strong>anti-CCP</strong> gibi testler istenebilir. "
                "Malignite şüphesinde protein elektroforezi (SPEP), görüntüleme ve bazen biyopsi düşünülür.</p>"
                "<p>Hekiminiz klinik tabloya göre uygun incelemeleri seçecektir. Sağlıklı bir kişide izole hafif ESR yüksekliği, "
                "normalleşip normalleşmediğini görmek için birkaç hafta sonra tekrar test gerektirebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Referans aralığı dışındaki herhangi bir ESR sonucunu sağlık hizmet sağlayıcınızla tartışın. "
                "Hafif yüksek ESR&mdash;özellikle yaşlılarda veya hamilelikte&mdash;selim olabilse de en azından bir konuşma hak eder. "
                "ESR çok yüksekse (100 mm/saat üzeri) veya açıklanamayan ateş, belirgin kilo kaybı, şiddetli eklem ağrısı, "
                "sürekli yorgunluk veya gece terlemeleri gibi belirtileriniz varsa <strong>acilen</strong> tıbbi yardım alın.</p>"
                "<p>Bilinen bir inflamatuar durumunuz varsa (romatoid artrit, lupus, polimiyalji romatika), "
                "hekiminiz hastalık aktivitesini ve tedaviye yanıtı izlemek için seri ESR ölçümleri kullanabilir. "
                "Bu bağlamda yükselen ESR bir alevlenmeyi, düşen ESR ise iyileşmeyi gösterebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya sedimentasyonunuzu anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;hazırlanmanıza yardımcı olur. Kan tahlili raporunuzu "
                "<a href=\"/analyze\">noryaai.com/analyze</a> adresine yükleyin ve ESR&rsquo;nizi CRP ve CBC değerleri gibi ilişkili belirteçlerle birlikte "
                "açıklayan yapılandırılmış bir özet alın.</p>"
                "<p>Kronik bir inflamatuar durumu takip ediyor veya rutin kan çalışmasında beklenmedik bir yükselme görüyor olun, "
                "Norya sonuçlarınızı düzenler ve hekiminizle yapacağınız görüşmeye odaklanmanızı sağlar. "
                "Plan seçenekleri ve fiyatlandırma için <a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Yasal uyarı",
            body_html=(
                '<p><strong>Bu rehber yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                'Sonuçlarınızı mutlaka bir sağlık profesyoneliyle değerlendirin. <a href="/analyze">Norya ile analize başlayın</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Spanish
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="VSG alta: qué significa tu velocidad de sedimentación",
            body_html=(
                "<p>La velocidad de sedimentación globular (VSG o ESR) es una de las pruebas de sangre más antiguas y sencillas que siguen en uso rutinario. "
                "Mide la rapidez con la que los glóbulos rojos se depositan en el fondo de un tubo vertical en una hora. "
                "Una velocidad superior a la normal sugiere inflamación, pero la VSG no puede precisar la causa exacta.</p>"
                "<p>Esta guía explica qué mide la VSG, cómo interpretar tu resultado según los rangos de referencia por edad y sexo, "
                "las causas más frecuentes de VSG elevada o baja, y cuándo consultar al médico. "
                "Es contenido educativo, no un diagnóstico médico&mdash;comenta siempre tus resultados con un profesional sanitario.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es la VSG y cómo se mide?",
            body_html=(
                "<p>La <strong>velocidad de sedimentación globular</strong> mide la distancia (en milímetros) que recorren los glóbulos rojos al descender en un tubo "
                "estandarizado durante 60 minutos. En condiciones normales, los eritrocitos se repelen por su carga negativa superficial y sedimentan lentamente. "
                "Cuando hay inflamación, el hígado produce más proteínas de fase aguda&mdash;especialmente <strong>fibrinógeno</strong>&mdash;que neutralizan "
                "la carga y hacen que los eritrocitos se apilen en formaciones llamadas <em>rouleaux</em>, más pesadas y que caen más rápido.</p>"
                "<p>La prueba suele realizarse con el <strong>método de Westergren</strong>: la sangre mezclada con citrato sódico se introduce en un tubo vertical "
                "de 200 mm y se deja reposar una hora. El resultado se informa en mm/h. A pesar de su sencillez, la VSG sigue siendo útil "
                "para detectar y monitorizar enfermedades inflamatorias e infecciosas.</p>"
                "<p>Es importante comprender que la VSG es un marcador <strong>inespecífico</strong>: indica inflamación probable, "
                "pero no identifica la causa. Se necesitan pruebas adicionales para determinar el origen.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos normales de la VSG",
            body_html=(
                "<p>Los rangos de referencia dependen de la edad y el sexo. Límites superiores habituales (Westergren):</p>"
                "<ul>"
                "<li><strong>Hombres &lt; 50 años:</strong> &lt; 15 mm/h</li>"
                "<li><strong>Hombres &gt; 50 años:</strong> &lt; 20 mm/h</li>"
                "<li><strong>Mujeres &lt; 50 años:</strong> &lt; 20 mm/h</li>"
                "<li><strong>Mujeres &gt; 50 años:</strong> &lt; 30 mm/h</li>"
                "</ul>"
                "<p>La VSG tiende a aumentar con la edad y suele ser más alta en mujeres. El embarazo también la eleva fisiológicamente. "
                "Compara siempre tu resultado con el rango de tu informe de laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de VSG alta",
            body_html=(
                "<p>Una VSG moderadamente elevada (20&ndash;60 mm/h) puede aparecer en múltiples situaciones. "
                "Las <strong>infecciones</strong> (bacterianas, víricas o fúngicas) se encuentran entre los desencadenantes más comunes. "
                "Las <strong>enfermedades autoinmunes e inflamatorias</strong> (artritis reumatoide, lupus, polimialgia reumática, arteritis de células gigantes) "
                "elevan la VSG de forma característica.</p>"
                "<p>El <strong>cáncer</strong>&mdash;especialmente linfoma, mieloma múltiple y enfermedad metastásica&mdash;puede elevar la VSG por encima de 100 mm/h. "
                "La <strong>anemia</strong> también la incrementa porque menos eritrocitos sedimentan más rápido. "
                "Otros factores: embarazo, edad avanzada, obesidad y enfermedad renal crónica. "
                "Tu médico interpretará el resultado junto con los síntomas y otras pruebas como "
                "<a href=\"/es/blog/crp-marcador-inflamacion\">CRP</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas asociados a la VSG elevada",
            body_html=(
                "<p>La VSG en sí no causa síntomas; es un marcador del proceso subyacente. "
                "Los síntomas dependen de la enfermedad responsable: fiebre e infección, dolor articular en la artritis, "
                "pérdida de peso inexplicable en el cáncer, etc.</p>"
                "<p>Algunas personas con VSG ligeramente elevada no presentan síntomas; puede ser un hallazgo casual en analíticas rutinarias. "
                "Una VSG muy alta (&gt; 100 mm/h) con síntomas constitucionales (fiebre, pérdida de peso, fatiga) requiere evaluación clínica urgente.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p>La VSG suele acompañarse de pruebas más específicas: "
                "<strong><a href=\"/es/blog/crp-marcador-inflamacion\">proteína C reactiva (PCR)</a></strong>, que sube y baja más rápido que la VSG; "
                "<strong>hemograma completo</strong> para evaluar anemia, infección o neoplasias hematológicas; "
                "y pruebas autoinmunes como <strong>ANA</strong>, <strong>FR</strong> y <strong>anti-CCP</strong> cuando se sospecha enfermedad autoinmune.</p>"
                "<p>En caso de sospecha de malignidad, pueden realizarse electroforesis de proteínas, estudios de imagen y biopsia.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Consulta con tu médico cualquier VSG fuera de rango, aunque te sientas bien. "
                "Busca atención <strong>urgente</strong> si la VSG supera 100 mm/h o si tienes fiebre inexplicable, pérdida de peso significativa, "
                "dolor articular intenso o sudoración nocturna.</p>"
                "<p>Si tienes una enfermedad inflamatoria conocida, tu médico puede usar mediciones seriadas de VSG "
                "para monitorizar la actividad y la respuesta al tratamiento.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya te ayuda a entender tu VSG",
            body_html=(
                "<p>Norya no diagnostica&mdash;te ayuda a prepararte. Sube tu análisis de sangre en "
                "<a href=\"/analyze\">noryaai.com/analyze</a> y recibe un resumen claro que señala tu VSG junto con marcadores relacionados "
                "como PCR y hemograma.</p>"
                "<p>Ya sea que estés monitorizando una condición inflamatoria crónica o veas un resultado inesperado, "
                "Norya organiza tus resultados para centrarte en la conversación con tu médico. "
                "Para opciones de plan y precios, visita nuestra <a href=\"/pricing\">página de precios</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso legal",
            body_html=(
                '<p><strong>Esta guía es solo informativa y no sustituye el consejo ni el diagnóstico médico.</strong> '
                'Comenta siempre tus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Blutsenkung (BSG) erhöht: was Ihr Ergebnis bedeutet",
            body_html=(
                "<p>Die Blutsenkungsgeschwindigkeit (BSG oder ESR) ist einer der ältesten und einfachsten Bluttests, die noch routinemäßig eingesetzt werden. "
                "Sie misst, wie schnell rote Blutkörperchen in einem vertikalen Röhrchen innerhalb einer Stunde absinken. "
                "Eine erhöhte Senkungsgeschwindigkeit deutet auf Entzündung hin, kann aber die genaue Ursache nicht bestimmen.</p>"
                "<p>Dieser Ratgeber erklärt, was die BSG misst, wie Sie Ihr Ergebnis anhand alters- und geschlechtsspezifischer Referenzbereiche einordnen, "
                "die häufigsten Ursachen einer erhöhten oder niedrigen BSG und wann Sie einen Arzt aufsuchen sollten.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist die BSG und wie wird sie gemessen?",
            body_html=(
                "<p>Die <strong>Blutsenkungsgeschwindigkeit</strong> misst die Strecke (in Millimetern), die Erythrozyten in einem standardisierten Röhrchen innerhalb von 60 Minuten zurücklegen. "
                "Normalerweise stoßen sich die roten Blutkörperchen aufgrund ihrer negativen Oberflächenladung ab und sinken langsam. "
                "Bei Entzündungen produziert die Leber mehr Akute-Phase-Proteine&mdash;insbesondere <strong>Fibrinogen</strong>&mdash;, die die Ladung neutralisieren "
                "und zur Bildung von <em>Geldrollenformationen</em> (Rouleaux) führen, die schwerer sind und schneller sinken.</p>"
                "<p>Die Messung erfolgt meist nach der <strong>Westergren-Methode</strong>. Das Ergebnis wird in mm/h angegeben. "
                "Die BSG ist ein <strong>unspezifischer</strong> Marker: Sie zeigt an, dass wahrscheinlich eine Entzündung vorliegt, identifiziert aber nicht die Ursache.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale BSG-Werte",
            body_html=(
                "<p>Die Referenzbereiche hängen von Alter und Geschlecht ab:</p>"
                "<ul>"
                "<li><strong>Männer &lt; 50 Jahre:</strong> &lt; 15 mm/h</li>"
                "<li><strong>Männer &gt; 50 Jahre:</strong> &lt; 20 mm/h</li>"
                "<li><strong>Frauen &lt; 50 Jahre:</strong> &lt; 20 mm/h</li>"
                "<li><strong>Frauen &gt; 50 Jahre:</strong> &lt; 30 mm/h</li>"
                "</ul>"
                "<p>Die BSG steigt tendenziell mit dem Alter und ist bei Frauen höher. Schwangerschaft kann die BSG physiologisch erhöhen. "
                "Vergleichen Sie Ihr Ergebnis immer mit dem Referenzbereich auf Ihrem Laborbefund.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen einer erhöhten BSG",
            body_html=(
                "<p>Eine mäßig erhöhte BSG (20&ndash;60 mm/h) kann bei vielen Zuständen auftreten: "
                "<strong>Infektionen</strong>, <strong>Autoimmunerkrankungen</strong> (rheumatoide Arthritis, Lupus, Polymyalgia rheumatica, Riesenzellarteriitis) "
                "und <strong>Krebs</strong> (insbesondere Lymphom, multiples Myelom). Eine BSG über 100 mm/h erfordert eine gründliche Abklärung.</p>"
                "<p><strong>Anämie</strong>, Schwangerschaft, Adipositas und chronische Nierenerkrankung erhöhen die BSG ebenfalls. "
                "Umgekehrt können Polyzythämie, Sichelzellanämie und extreme Leukozytose die BSG senken. "
                "Ihr Arzt wird das Ergebnis im klinischen Kontext zusammen mit Tests wie "
                "<a href=\"/de/blog/crp-entzuendungsmarker\">CRP</a> bewerten.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome bei erhöhter BSG",
            body_html=(
                "<p>Die BSG selbst verursacht keine Symptome&mdash;sie spiegelt den zugrunde liegenden Prozess wider. "
                "Die Symptome hängen von der auslösenden Erkrankung ab: Fieber bei Infektionen, Gelenkschmerzen bei Autoimmunerkrankungen, "
                "Gewichtsverlust bei Krebs.</p>"
                "<p>Manche Menschen mit leicht erhöhter BSG sind beschwerdefrei. "
                "Eine sehr hohe BSG (&gt; 100 mm/h) mit konstitutionellen Symptomen erfordert eine dringliche Abklärung.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Ergänzende Untersuchungen",
            body_html=(
                "<p>Die BSG wird fast immer zusammen mit gezielteren Tests bewertet: "
                "<strong><a href=\"/de/blog/crp-entzuendungsmarker\">CRP</a></strong>, <strong>Blutbild</strong>, "
                "und bei Verdacht auf Autoimmunerkrankung <strong>ANA</strong>, <strong>RF</strong> und <strong>Anti-CCP</strong>. "
                "Bei Malignitätsverdacht können Proteinelektrophorese, Bildgebung und Biopsie folgen.</p>"
                "<p>Eine isolierte leichte BSG-Erhöhung bei einem ansonsten gesunden Patienten kann zunächst nur eine Verlaufskontrolle erfordern.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann zum Arzt?",
            body_html=(
                "<p>Besprechen Sie jeden auffälligen BSG-Wert mit Ihrem Arzt. "
                "Suchen Sie <strong>umgehend</strong> Hilfe, wenn die BSG über 100 mm/h liegt oder wenn Sie ungeklärtes Fieber, "
                "erheblichen Gewichtsverlust, starke Gelenkschmerzen oder Nachtschweiß haben.</p>"
                "<p>Bei bekannter entzündlicher Erkrankung kann Ihr Arzt serielle BSG-Messungen zur Verlaufsbeurteilung nutzen.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihre BSG zu verstehen",
            body_html=(
                "<p>Norya stellt keine Diagnosen&mdash;wir helfen bei der Vorbereitung. Laden Sie Ihren Blutbefund unter "
                "<a href=\"/analyze\">noryaai.com/analyze</a> hoch und erhalten Sie eine Zusammenfassung, "
                "die Ihre BSG zusammen mit CRP und Blutbild in verständlicher Sprache erklärt.</p>"
                "<p>Ob Sie eine chronische Entzündung verfolgen oder ein unerwartetes Ergebnis sehen&mdash;"
                "Norya ordnet Ihre Ergebnisse für das Arztgespräch. "
                "Pläne und Preise auf unserer <a href=\"/pricing\">Preisseite</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Haftungsausschluss",
            body_html=(
                '<p><strong>Dieser Ratgeber dient ausschließlich der Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> '
                'Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# French
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="VS élevée : que signifie votre vitesse de sédimentation ?",
            body_html=(
                "<p>La vitesse de sédimentation (VS ou ESR) est l&rsquo;un des tests sanguins les plus anciens et les plus simples encore utilisés en routine. "
                "Elle mesure la vitesse à laquelle les globules rouges se déposent dans un tube vertical en une heure. "
                "Une valeur supérieure à la normale suggère une inflammation, mais la VS ne peut pas en identifier la cause précise.</p>"
                "<p>Ce guide explique ce que mesure la VS, comment interpréter votre résultat, "
                "les causes fréquentes d&rsquo;une VS élevée ou basse, et quand consulter. "
                "Il est éducatif et ne constitue pas un diagnostic&mdash;discutez toujours de vos résultats avec un professionnel de santé.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu'est-ce que la VS et comment est-elle mesurée ?",
            body_html=(
                "<p>La <strong>vitesse de sédimentation</strong> mesure la distance (en millimètres) parcourue par les globules rouges en 60 minutes dans un tube standardisé. "
                "En conditions normales, les érythrocytes se repoussent par leur charge de surface négative et sédimentent lentement. "
                "En cas d&rsquo;inflammation, le foie produit davantage de protéines de phase aiguë&mdash;notamment le <strong>fibrinogène</strong>&mdash;"
                "qui neutralisent la charge et provoquent la formation de <em>rouleaux</em>, plus lourds et qui tombent plus vite.</p>"
                "<p>La mesure se fait habituellement par la <strong>méthode de Westergren</strong>. Le résultat est exprimé en mm/h. "
                "La VS est un marqueur <strong>non spécifique</strong> : elle signale une inflammation probable mais n&rsquo;en identifie pas la cause.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de la VS",
            body_html=(
                "<p>Les valeurs de référence varient selon l&rsquo;âge et le sexe :</p>"
                "<ul>"
                "<li><strong>Hommes &lt; 50 ans :</strong> &lt; 15 mm/h</li>"
                "<li><strong>Hommes &gt; 50 ans :</strong> &lt; 20 mm/h</li>"
                "<li><strong>Femmes &lt; 50 ans :</strong> &lt; 20 mm/h</li>"
                "<li><strong>Femmes &gt; 50 ans :</strong> &lt; 30 mm/h</li>"
                "</ul>"
                "<p>La VS augmente avec l&rsquo;âge, est généralement plus élevée chez les femmes et peut s&rsquo;élever physiologiquement pendant la grossesse. "
                "Comparez toujours votre résultat à la plage de votre compte-rendu.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une VS élevée",
            body_html=(
                "<p>Les <strong>infections</strong>, les <strong>maladies auto-immunes</strong> (polyarthrite rhumatoïde, lupus, polymyalgie rhumatismale) "
                "et le <strong>cancer</strong> (lymphome, myélome multiple) sont parmi les causes les plus fréquentes. "
                "L&rsquo;<strong>anémie</strong>, la grossesse, l&rsquo;obésité et l&rsquo;insuffisance rénale chronique élèvent également la VS.</p>"
                "<p>Une VS supérieure à 100 mm/h nécessite un bilan approfondi incluant recherche de néoplasie, infection sévère et maladie rénale. "
                "Votre médecin interprétera le résultat avec les symptômes et d&rsquo;autres examens comme "
                "<a href=\"/fr/blog/crp-marqueur-inflammation\">la CRP</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes associés à une VS élevée",
            body_html=(
                "<p>La VS ne provoque pas de symptômes en elle-même ; elle reflète le processus sous-jacent. "
                "Les symptômes dépendent de la cause : fièvre en cas d&rsquo;infection, douleurs articulaires en cas de maladie auto-immune, "
                "perte de poids en cas de cancer.</p>"
                "<p>Certaines personnes avec une VS légèrement élevée sont asymptomatiques. "
                "Une VS très haute (&gt; 100 mm/h) accompagnée de symptômes généraux justifie une évaluation clinique urgente.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens complémentaires",
            body_html=(
                "<p>La VS est presque toujours associée à des tests plus ciblés : "
                "<strong><a href=\"/fr/blog/crp-marqueur-inflammation\">CRP</a></strong>, <strong>hémogramme</strong>, "
                "et, en cas de suspicion auto-immune, <strong>ANA</strong>, <strong>FR</strong> et <strong>anti-CCP</strong>. "
                "En cas de suspicion de malignité, électrophorèse des protéines, imagerie et biopsie peuvent être envisagées.</p>"
                "<p>Une VS légèrement élevée isolée chez un sujet sain peut ne nécessiter qu&rsquo;un contrôle à quelques semaines.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Parlez à votre médecin de tout résultat de VS hors norme. "
                "Consultez en <strong>urgence</strong> si la VS dépasse 100 mm/h ou si vous présentez fièvre inexpliquée, perte de poids, "
                "douleurs articulaires sévères ou sueurs nocturnes.</p>"
                "<p>Si vous avez une maladie inflammatoire connue, votre médecin peut utiliser la VS en série pour surveiller l&rsquo;activité et la réponse au traitement.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre votre VS",
            body_html=(
                "<p>Norya ne pose pas de diagnostic&mdash;nous vous aidons à vous préparer. Téléversez votre bilan sur "
                "<a href=\"/analyze\">noryaai.com/analyze</a> et recevez un résumé clair expliquant votre VS, votre CRP et votre hémogramme.</p>"
                "<p>Que vous suiviez une maladie inflammatoire ou découvriez un résultat inattendu, "
                "Norya organise vos résultats pour votre rendez-vous médical. "
                "Formules et tarifs sur notre <a href=\"/pricing\">page tarifs</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis médical ou un diagnostic.</strong> '
                'Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Italian
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="VES alta: cosa significa la tua velocità di eritrosedimentazione",
            body_html=(
                "<p>La velocità di eritrosedimentazione (VES o ESR) è uno degli esami del sangue più antichi e semplici ancora in uso routinario. "
                "Misura la velocità con cui i globuli rossi si depositano sul fondo di una provetta verticale in un&rsquo;ora. "
                "Un valore superiore alla norma suggerisce infiammazione, ma la VES non può identificarne la causa precisa.</p>"
                "<p>Questa guida spiega cosa misura la VES, come interpretare il risultato, "
                "le cause più comuni di VES elevata o bassa e quando consultare il medico. "
                "È a scopo educativo, non diagnostico&mdash;discuti sempre i tuoi risultati con un medico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Cos'è la VES e come si misura?",
            body_html=(
                "<p>La <strong>velocità di eritrosedimentazione</strong> misura la distanza (in millimetri) percorsa dai globuli rossi in una provetta standardizzata in 60 minuti. "
                "In condizioni normali, gli eritrociti si respingono per la loro carica superficiale negativa e sedimentano lentamente. "
                "In presenza di infiammazione, il fegato produce più proteine di fase acuta&mdash;soprattutto <strong>fibrinogeno</strong>&mdash;che "
                "neutralizzano la carica e causano la formazione di <em>rouleaux</em>, più pesanti e che cadono più rapidamente.</p>"
                "<p>La misura si effettua di solito con il <strong>metodo Westergren</strong>. Il risultato è espresso in mm/h. "
                "La VES è un marcatore <strong>aspecifico</strong>: segnala un&rsquo;infiammazione probabile ma non ne identifica la causa.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali della VES",
            body_html=(
                "<p>I valori di riferimento dipendono da età e sesso:</p>"
                "<ul>"
                "<li><strong>Uomini &lt; 50 anni:</strong> &lt; 15 mm/h</li>"
                "<li><strong>Uomini &gt; 50 anni:</strong> &lt; 20 mm/h</li>"
                "<li><strong>Donne &lt; 50 anni:</strong> &lt; 20 mm/h</li>"
                "<li><strong>Donne &gt; 50 anni:</strong> &lt; 30 mm/h</li>"
                "</ul>"
                "<p>La VES tende ad aumentare con l&rsquo;età ed è generalmente più alta nelle donne. La gravidanza può elevarla fisiologicamente. "
                "Confronta sempre il risultato con l&rsquo;intervallo del tuo referto.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause della VES alta",
            body_html=(
                "<p>Le <strong>infezioni</strong>, le <strong>malattie autoimmuni</strong> (artrite reumatoide, lupus, polimialgia reumatica) "
                "e il <strong>cancro</strong> (linfoma, mieloma multiplo) sono tra le cause più frequenti. "
                "L&rsquo;<strong>anemia</strong>, la gravidanza, l&rsquo;obesità e l&rsquo;insufficienza renale cronica aumentano anch&rsquo;esse la VES.</p>"
                "<p>Una VES superiore a 100 mm/h richiede un&rsquo;indagine approfondita. "
                "Il medico interpreterà il risultato insieme ai sintomi e ad altri esami come "
                "<a href=\"/it/blog/crp-marcatore-infiammazione\">la PCR</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi associati alla VES elevata",
            body_html=(
                "<p>La VES di per sé non causa sintomi; riflette il processo sottostante. "
                "I sintomi dipendono dalla causa: febbre nelle infezioni, dolori articolari nelle malattie autoimmuni, "
                "perdita di peso nel cancro.</p>"
                "<p>Alcune persone con VES lievemente elevata sono asintomatiche. "
                "Una VES molto alta (&gt; 100 mm/h) con sintomi costituzionali richiede una valutazione clinica urgente.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p>La VES è quasi sempre associata a test più mirati: "
                "<strong><a href=\"/it/blog/crp-marcatore-infiammazione\">PCR</a></strong>, <strong>emocromo</strong>, "
                "e, in caso di sospetto autoimmune, <strong>ANA</strong>, <strong>FR</strong> e <strong>anti-CCP</strong>. "
                "Per sospetta neoplasia: elettroforesi proteica, imaging e biopsia.</p>"
                "<p>Una VES lievemente elevata isolata in un soggetto sano può richiedere solo un controllo a distanza di settimane.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico",
            body_html=(
                "<p>Discutete con il medico qualsiasi VES fuori intervallo. "
                "Cercate assistenza <strong>urgente</strong> se la VES supera 100 mm/h o se avete febbre inspiegabile, "
                "perdita di peso, forte dolore articolare o sudorazione notturna.</p>"
                "<p>Se avete una malattia infiammatoria nota, il medico può utilizzare misurazioni seriali della VES per monitorare l&rsquo;attività.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a capire la tua VES",
            body_html=(
                "<p>Norya non fa diagnosi&mdash;ti aiuta a prepararti. Carica le tue analisi su "
                "<a href=\"/analyze\">noryaai.com/analyze</a> e ricevi un riepilogo chiaro che spiega VES, PCR ed emocromo in linguaggio semplice.</p>"
                "<p>Che tu stia monitorando un&rsquo;infiammazione cronica o abbia trovato un valore inatteso, "
                "Norya organizza i tuoi risultati per il dialogo con il medico. "
                "Piani e prezzi sulla nostra <a href=\"/pricing\">pagina prezzi</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza",
            body_html=(
                '<p><strong>Questa guida ha finalità esclusivamente informative e non sostituisce il parere medico o la diagnosi.</strong> '
                'Discuti sempre i tuoi risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hebrew
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="שקיעת דם (ESR) גבוהה: מה המשמעות של התוצאה שלך",
            body_html=(
                "<p>שקיעת הדם (ESR), הנקראת גם <em>שקיעת כדוריות</em>, היא אחת מבדיקות הדם הוותיקות והפשוטות ביותר שעדיין בשימוש שגרתי. "
                "היא מודדת כמה מהר כדוריות דם אדומות שוקעות לתחתית מבחנה אנכית תוך שעה. קצב מהיר מהרגיל מעיד על דלקת בגוף, "
                "אך הבדיקה לא יכולה לזהות את הסיבה המדויקת.</p>"
                "<p>מדריך זה מסביר מה ESR מודד, כיצד לפרש את התוצאה, הגורמים הנפוצים ל-ESR גבוה או נמוך, ומתי לפנות לרופא. "
                "הוא חינוכי ואינו מהווה אבחנה&mdash;שוחחו תמיד עם רופא על התוצאות שלכם.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהי שקיעת דם (ESR) וכיצד היא נמדדת?",
            body_html=(
                "<p><strong>קצב שקיעת אריתרוציטים</strong> מודד את המרחק (במילימטרים) שכדוריות דם אדומות נופלות במבחנה סטנדרטית תוך 60 דקות. "
                "בתנאים רגילים, כדוריות אדומות דוחות זו את זו בשל המטען השלילי על פניהן ושוקעות לאט. "
                "כשיש דלקת, הכבד מייצר יותר חלבוני שלב חריף&mdash;במיוחד <strong>פיברינוגן</strong>&mdash;שמנטרלים את המטען "
                "וגורמים לכדוריות להיערם ב<em>רולו</em> (Rouleaux), שהם כבדים יותר ושוקעים מהר יותר.</p>"
                "<p>הבדיקה נעשית בדרך כלל בשיטת <strong>וסטרגרן</strong>. התוצאה מדווחת ב-mm/h. "
                "ESR הוא סמן <strong>לא ספציפי</strong>: הוא מעיד על דלקת סבירה אך לא מזהה את הגורם.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ESR תקינים",
            body_html=(
                "<p>טווחי הייחוס תלויים בגיל ובמין:</p>"
                "<ul>"
                "<li><strong>גברים מתחת ל-50:</strong> &lt; 15 mm/h</li>"
                "<li><strong>גברים מעל 50:</strong> &lt; 20 mm/h</li>"
                "<li><strong>נשים מתחת ל-50:</strong> &lt; 20 mm/h</li>"
                "<li><strong>נשים מעל 50:</strong> &lt; 30 mm/h</li>"
                "</ul>"
                "<p>ESR נוטה לעלות עם הגיל וגבוהה יותר בנשים. הריון יכול להעלות את ESR באופן פיזיולוגי. "
                "השוו תמיד את התוצאה לטווח בדוח המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים ל-ESR גבוהה",
            body_html=(
                "<p><strong>זיהומים</strong>, <strong>מחלות אוטואימוניות</strong> (דלקת מפרקים שגרונית, לופוס, פולימיאלגיה ראומטיקה) "
                "ו<strong>סרטן</strong> (לימפומה, מיאלומה נפוצה) הם בין הגורמים השכיחים ביותר. "
                "<strong>אנמיה</strong>, הריון, השמנת יתר ומחלת כליות כרונית גם מעלים ESR.</p>"
                "<p>ESR מעל 100 mm/h דורש בירור מקיף. הרופא יפרש את התוצאה יחד עם התסמינים ובדיקות נוספות כמו "
                "<a href=\"/he/blog/crp-inflammation-marker\">CRP</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים הקשורים ל-ESR גבוהה",
            body_html=(
                "<p>ESR עצמו לא גורם לתסמינים; הוא משקף את התהליך הבסיסי. "
                "התסמינים תלויים בגורם: חום בזיהום, כאבי מפרקים במחלה אוטואימונית, ירידה במשקל בסרטן.</p>"
                "<p>חלק מהאנשים עם ESR מעט גבוה הם ללא תסמינים. "
                "ESR גבוהה מאוד (&gt; 100 mm/h) עם תסמינים מערכתיים מחייבת הערכה קלינית דחופה.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות נלוות",
            body_html=(
                "<p>ESR כמעט תמיד נבדק יחד עם: "
                "<strong><a href=\"/he/blog/crp-inflammation-marker\">CRP</a></strong>, <strong>ספירת דם מלאה</strong>, "
                "ובחשד למחלה אוטואימונית&mdash;<strong>ANA</strong>, <strong>RF</strong> ו-<strong>anti-CCP</strong>. "
                "בחשד לממאירות: אלקטרופורזה של חלבונים, הדמיה וביופסיה.</p>"
                "<p>ESR מעט גבוה בודד באדם בריא עשוי לדרוש רק בדיקה חוזרת בעוד מספר שבועות.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>שוחחו עם הרופא על כל תוצאת ESR מחוץ לטווח. "
                "פנו ל<strong>טיפול דחוף</strong> אם ESR מעל 100 mm/h או אם יש חום לא מוסבר, ירידה משמעותית במשקל, "
                "כאבי מפרקים חמורים או הזעות לילה.</p>"
                "<p>אם יש לכם מחלה דלקתית ידועה, הרופא עשוי להשתמש במדידות ESR סדרתיות לניטור פעילות המחלה.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת לכם להבין את ה-ESR",
            body_html=(
                "<p>Norya לא מאבחנת&mdash;אנחנו עוזרים לכם להתכונן. העלו את הדוח ב-"
                "<a href=\"/analyze\">noryaai.com/analyze</a> וקבלו סיכום ברור המסביר את ה-ESR לצד CRP וספירת דם בשפה פשוטה.</p>"
                "<p>בין אם אתם עוקבים אחרי מצב דלקתי כרוני או מצאתם ערך בלתי צפוי, "
                "Norya מארגנת את התוצאות לקראת הפגישה עם הרופא. "
                "לאפשרויות מנוי ומחירים, בקרו ב<a href=\"/pricing\">עמוד המחירים</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הבהרה",
            body_html=(
                '<p><strong>מדריך זה מיועד למטרות מידע בלבד ואינו מהווה תחליף לייעוץ רפואי או אבחנה.</strong> '
                'שוחחו תמיד עם רופא על התוצאות שלכם. <a href="/analyze">התחילו ניתוח עם Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hindi
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="ESR (सेडिमेंटेशन रेट) अधिक: आपकी रिपोर्ट का क्या मतलब है",
            body_html=(
                "<p>एरिथ्रोसाइट सेडिमेंटेशन रेट (ESR), जिसे <em>सेड रेट</em> या <em>ब्लड सेडिमेंटेशन</em> भी कहते हैं, "
                "अभी भी नियमित उपयोग में सबसे पुरानी और सरल ब्लड टेस्ट में से एक है। यह मापता है कि एक घंटे में लाल रक्त कोशिकाएँ "
                "एक ऊर्ध्वाधर ट्यूब में कितनी तेज़ी से नीचे बैठती हैं। सामान्य से तेज़ दर शरीर में सूजन का संकेत देती है, "
                "लेकिन ESR अकेले कारण नहीं बता सकता।</p>"
                "<p>यह गाइड बताती है कि ESR क्या मापता है, रिफरेंस रेंज, उच्च या निम्न ESR के सामान्य कारण, "
                "और डॉक्टर से कब मिलना चाहिए। यह शैक्षिक है, निदान नहीं&mdash;अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ESR क्या है और कैसे मापा जाता है?",
            body_html=(
                "<p><strong>एरिथ्रोसाइट सेडिमेंटेशन रेट</strong> उस दूरी (मिलीमीटर में) को मापता है जो लाल रक्त कोशिकाएँ "
                "एक मानकीकृत ट्यूब में 60 मिनट में तय करती हैं। सामान्य परिस्थितियों में, लाल कोशिकाएँ अपने नकारात्मक सतह चार्ज "
                "के कारण एक-दूसरे को दूर करती हैं और धीरे-धीरे बैठती हैं। सूजन होने पर लिवर अधिक एक्यूट फेज प्रोटीन&mdash;"
                "विशेषकर <strong>फाइब्रिनोजन</strong>&mdash;बनाता है, जो चार्ज को न्यूट्रल कर देते हैं और कोशिकाएँ <em>रूलो</em> बनाकर "
                "तेज़ी से नीचे गिरती हैं।</p>"
                "<p>टेस्ट आमतौर पर <strong>वेस्टरग्रेन विधि</strong> से किया जाता है। परिणाम mm/hr में रिपोर्ट होता है। "
                "ESR एक <strong>नॉन-स्पेसिफिक</strong> मार्कर है: यह सूजन की संभावना बताता है लेकिन कारण नहीं।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य ESR रेंज",
            body_html=(
                "<p>ESR रिफरेंस रेंज उम्र और लिंग पर निर्भर करती है:</p>"
                "<ul>"
                "<li><strong>50 वर्ष से कम पुरुष:</strong> &lt; 15 mm/hr</li>"
                "<li><strong>50 वर्ष से अधिक पुरुष:</strong> &lt; 20 mm/hr</li>"
                "<li><strong>50 वर्ष से कम महिलाएँ:</strong> &lt; 20 mm/hr</li>"
                "<li><strong>50 वर्ष से अधिक महिलाएँ:</strong> &lt; 30 mm/hr</li>"
                "</ul>"
                "<p>ESR उम्र के साथ बढ़ने की प्रवृत्ति रखता है और महिलाओं में आमतौर पर अधिक होता है। गर्भावस्था ESR को शारीरिक रूप से बढ़ा सकती है। "
                "अपने परिणाम की तुलना हमेशा अपनी लैब रिपोर्ट पर दी गई रेंज से करें।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="ESR बढ़ने के कारण",
            body_html=(
                "<p><strong>संक्रमण</strong> (बैक्टीरियल, वायरल या फंगल), <strong>ऑटोइम्यून रोग</strong> "
                "(रुमेटॉइड आर्थराइटिस, ल्यूपस, पॉलीमायल्जिया रूमेटिका) और <strong>कैंसर</strong> (लिम्फोमा, मल्टीपल मायलोमा) "
                "सबसे आम कारणों में हैं। <strong>एनीमिया</strong>, गर्भावस्था, मोटापा और क्रोनिक किडनी डिजीज भी ESR बढ़ाते हैं।</p>"
                "<p>100 mm/hr से अधिक ESR को बहुत उच्च माना जाता है और इसमें गहन जाँच ज़रूरी है। "
                "डॉक्टर परिणाम का मूल्यांकन लक्षणों और अन्य टेस्ट जैसे "
                "<a href=\"/hi/blog/crp-inflammation-marker\">CRP</a> के साथ करेंगे।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="उच्च ESR से जुड़े लक्षण",
            body_html=(
                "<p>ESR स्वयं लक्षण नहीं पैदा करता; यह अंतर्निहित प्रक्रिया को दर्शाता है। "
                "लक्षण कारण पर निर्भर करते हैं: संक्रमण में बुखार, ऑटोइम्यून रोगों में जोड़ों का दर्द, कैंसर में वज़न घटना।</p>"
                "<p>कुछ लोगों में हल्की ESR वृद्धि के साथ कोई लक्षण नहीं होते। "
                "बहुत उच्च ESR (&gt; 100 mm/hr) के साथ बुखार, वज़न कम होना और थकान होने पर तुरंत डॉक्टर से मिलें।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित जाँचें",
            body_html=(
                "<p>ESR लगभग हमेशा अधिक लक्षित टेस्ट के साथ जाँचा जाता है: "
                "<strong><a href=\"/hi/blog/crp-inflammation-marker\">CRP</a></strong>, <strong>CBC (पूर्ण रक्त गणना)</strong>, "
                "और ऑटोइम्यून संदेह में <strong>ANA</strong>, <strong>RF</strong> व <strong>anti-CCP</strong>। "
                "कैंसर की शंका में प्रोटीन इलेक्ट्रोफोरेसिस, इमेजिंग और बायोप्सी हो सकती है।</p>"
                "<p>स्वस्थ व्यक्ति में अलग-थलग हल्की ESR वृद्धि को कुछ हफ्तों बाद दोहराने की ज़रूरत हो सकती है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>रेफरेंस रेंज से बाहर किसी भी ESR परिणाम पर डॉक्टर से बात करें। "
                "ESR 100 mm/hr से अधिक हो या अस्पष्ट बुखार, वज़न घटना, गंभीर जोड़ दर्द या रात में पसीना आता हो "
                "तो <strong>तुरंत</strong> चिकित्सा सहायता लें।</p>"
                "<p>यदि आपको कोई ज्ञात सूजन संबंधी रोग है, तो डॉक्टर रोग की गतिविधि की निगरानी के लिए क्रमिक ESR माप कर सकते हैं।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपकी ESR समझने में कैसे मदद करता है",
            body_html=(
                "<p>Norya निदान नहीं करता&mdash;हम आपको तैयार होने में मदद करते हैं। अपनी ब्लड रिपोर्ट "
                "<a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें और ESR, CRP व CBC को सरल भाषा में समझाने वाला स्पष्ट सारांश प्राप्त करें।</p>"
                "<p>चाहे आप क्रोनिक इन्फ्लेमेटरी कंडीशन ट्रैक कर रहे हों या अनपेक्षित रिजल्ट देखा हो, "
                "Norya आपके परिणामों को व्यवस्थित करता है। प्लान विकल्प व मूल्य के लिए <a href=\"/pricing\">प्राइसिंग पेज</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचना के उद्देश्य से है और चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> '
                'अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya के साथ विश्लेषण शुरू करें</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Arabic
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="سرعة الترسيب (ESR) مرتفعة: ماذا تعني نتيجتك",
            body_html=(
                "<p>معدل ترسيب كريات الدم الحمراء (ESR)، المعروف أيضاً بـ<em>سرعة الترسيب</em>، هو أحد أقدم وأبسط فحوصات الدم التي لا تزال مستخدمة بشكل روتيني. "
                "يقيس سرعة ترسّب الكريات الحمراء في أنبوب عمودي خلال ساعة واحدة. معدل أسرع من الطبيعي يدل على وجود التهاب، "
                "لكن الفحص لا يستطيع تحديد السبب بدقة.</p>"
                "<p>يشرح هذا الدليل ما يقيسه ESR، كيفية قراءة النتيجة، الأسباب الشائعة لارتفاعه، ومتى يجب مراجعة الطبيب. "
                "هو تثقيفي وليس تشخيصياً&mdash;ناقش نتائجك دائماً مع طبيب مؤهل.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو ESR وكيف يُقاس؟",
            body_html=(
                "<p><strong>معدل ترسيب كريات الدم الحمراء</strong> يقيس المسافة (بالمليمترات) التي تقطعها الكريات الحمراء في أنبوب معياري خلال 60 دقيقة. "
                "في الظروف العادية، تتنافر الكريات بسبب شحنتها السطحية السالبة وتترسب ببطء. "
                "عند وجود التهاب، ينتج الكبد مزيداً من بروتينات المرحلة الحادة&mdash;خاصة <strong>الفيبرينوجين</strong>&mdash;"
                "التي تُعادل الشحنة وتُسبب تكدّس الكريات في تشكيلات تُسمى <em>رولو</em>، أثقل وتسقط أسرع.</p>"
                "<p>يُجرى القياس عادة بطريقة <strong>وسترغرين</strong>. النتيجة تُعبَّر بـ mm/h. "
                "ESR مؤشر <strong>غير نوعي</strong>: يشير إلى التهاب محتمل لكن لا يحدد السبب.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="نطاقات ESR الطبيعية",
            body_html=(
                "<p>تعتمد النطاقات المرجعية على العمر والجنس:</p>"
                "<ul>"
                "<li><strong>رجال أقل من 50 سنة:</strong> &lt; 15 mm/h</li>"
                "<li><strong>رجال فوق 50 سنة:</strong> &lt; 20 mm/h</li>"
                "<li><strong>نساء أقل من 50 سنة:</strong> &lt; 20 mm/h</li>"
                "<li><strong>نساء فوق 50 سنة:</strong> &lt; 30 mm/h</li>"
                "</ul>"
                "<p>يميل ESR للارتفاع مع التقدم في العمر ويكون أعلى عند النساء عموماً. الحمل يرفعه فسيولوجياً. "
                "قارن دائماً نتيجتك بالنطاق المحدد في تقرير مختبرك.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع ESR",
            body_html=(
                "<p><strong>العدوى</strong>، <strong>أمراض المناعة الذاتية</strong> (التهاب المفاصل الروماتويدي، الذئبة، ألم العضلات الروماتيزمي) "
                "و<strong>السرطان</strong> (ليمفوما، ورم نقوي متعدد) هي من أكثر الأسباب شيوعاً. "
                "<strong>فقر الدم</strong> والحمل والسمنة ومرض الكلى المزمن ترفع أيضاً ESR.</p>"
                "<p>ESR فوق 100 mm/h يتطلب تقييماً شاملاً. سيُفسّر الطبيب النتيجة مع الأعراض وفحوصات أخرى مثل "
                "<a href=\"/ar/blog/crp-inflammation-marker\">CRP</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض مرتبطة بارتفاع ESR",
            body_html=(
                "<p>ESR بحد ذاته لا يسبب أعراضاً؛ إنه يعكس العملية الأساسية. "
                "الأعراض تعتمد على السبب: حمى في العدوى، آلام مفاصل في المناعة الذاتية، فقدان وزن في السرطان.</p>"
                "<p>بعض الأشخاص مع ESR مرتفع قليلاً لا يشكون من أعراض. "
                "ESR مرتفع جداً (&gt; 100 mm/h) مع أعراض عامة يستوجب تقييماً سريرياً عاجلاً.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="فحوصات ذات صلة",
            body_html=(
                "<p>ESR يُقيَّم دائماً تقريباً مع فحوصات أكثر استهدافاً: "
                "<strong><a href=\"/ar/blog/crp-inflammation-marker\">CRP</a></strong>، <strong>تعداد دم شامل</strong>، "
                "وعند الاشتباه بمرض مناعي&mdash;<strong>ANA</strong> و<strong>RF</strong> و<strong>anti-CCP</strong>. "
                "عند الاشتباه بورم: رحلان بروتيني وتصوير وخزعة.</p>"
                "<p>ارتفاع ESR المعزول الخفيف في شخص سليم قد يحتاج فقط إلى إعادة فحص بعد أسابيع.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب؟",
            body_html=(
                "<p>ناقش أي نتيجة ESR خارج النطاق مع طبيبك. "
                "اطلب رعاية <strong>عاجلة</strong> إذا تجاوز ESR الـ100 mm/h أو إذا عانيت من حمى غير مفسَّرة أو فقدان وزن كبير "
                "أو ألم مفاصل شديد أو تعرّق ليلي.</p>"
                "<p>إذا كان لديك مرض التهابي معروف، قد يستخدم الطبيب قياسات ESR متسلسلة لمراقبة نشاط المرض والاستجابة للعلاج.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم ESR",
            body_html=(
                "<p>Norya لا تُشخّص&mdash;نحن نساعدك على الاستعداد. ارفع تقريرك على "
                "<a href=\"/analyze\">noryaai.com/analyze</a> واحصل على ملخص واضح يشرح ESR مع CRP وتعداد الدم بلغة بسيطة.</p>"
                "<p>سواء كنت تراقب حالة التهابية مزمنة أو وجدت نتيجة غير متوقعة، "
                "تنظّم Norya نتائجك لتحضيرك لموعد الطبيب. "
                "لخيارات الاشتراك والأسعار: <a href=\"/pricing\">صفحة الأسعار</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء مسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض تثقيفية فقط ولا يحل محل الاستشارة الطبية أو التشخيص.</strong> '
                'ناقش نتائجك دائماً مع طبيب مختص. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


# ============================================================================
# Public API
# ============================================================================

def get_esr_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for ESR article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_esr_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for ESR article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal ESR level?",
             "answer": "Normal ESR depends on age and sex. General upper limits: men under 50: <15 mm/hr, men over 50: <20 mm/hr, women under 50: <20 mm/hr, women over 50: <30 mm/hr."},
            {"question": "What causes high ESR?",
             "answer": "Common causes include infections, autoimmune diseases (rheumatoid arthritis, lupus), cancer (lymphoma, myeloma), anemia, pregnancy, and chronic kidney disease. ESR is non-specific and requires clinical correlation."},
            {"question": "Is ESR the same as CRP?",
             "answer": "No. Both are markers of inflammation, but CRP rises and falls more quickly than ESR. They provide complementary information; doctors often order both together to assess inflammation."},
            {"question": "When should I see a doctor about my ESR?",
             "answer": "See a doctor if your ESR is outside the reference range. Seek urgent attention if ESR is above 100 mm/hr or if you have unexplained fever, weight loss, severe joint pain, or night sweats."},
        ],
        "tr": [
            {"question": "Normal sedimentasyon (ESR) değeri nedir?",
             "answer": "Normal ESR yaş ve cinsiyete göre değişir. Genel üst sınırlar: 50 altı erkek <15 mm/saat, 50 üstü erkek <20, 50 altı kadın <20, 50 üstü kadın <30 mm/saat."},
            {"question": "Sedimentasyon yüksekliğinin nedenleri nelerdir?",
             "answer": "Yaygın nedenler enfeksiyonlar, otoimmün hastalıklar (romatoid artrit, lupus), kanser (lenfoma, miyelom), anemi, gebelik ve kronik böbrek hastalığıdır. ESR spesifik değildir ve klinik korelasyon gerektirir."},
            {"question": "ESR ile CRP aynı şey mi?",
             "answer": "Hayır. Her ikisi de inflamasyon belirtecidir ancak CRP, ESR'den daha hızlı yükselip düşer. Tamamlayıcı bilgi sağlarlar; hekimler genellikle ikisini birlikte ister."},
            {"question": "Sedimentasyon sonucu için ne zaman doktora başvurmalıyım?",
             "answer": "ESR referans aralığı dışındaysa doktora danışın. 100 mm/saat üzerinde ise veya açıklanamayan ateş, kilo kaybı veya şiddetli eklem ağrısı varsa acilen yardım alın."},
        ],
        "es": [
            {"question": "¿Cuál es la VSG normal?",
             "answer": "Depende de la edad y el sexo. Límites superiores: hombres <50 años: <15 mm/h, >50: <20; mujeres <50: <20, >50: <30 mm/h."},
            {"question": "¿Qué causa la VSG alta?",
             "answer": "Infecciones, enfermedades autoinmunes, cáncer, anemia, embarazo y enfermedad renal crónica. La VSG es inespecífica y necesita correlación clínica."},
            {"question": "¿La VSG y la PCR son lo mismo?",
             "answer": "No. Ambas son marcadores de inflamación, pero la PCR sube y baja más rápido. Se complementan y los médicos suelen solicitar ambas."},
        ],
        "de": [
            {"question": "Was ist ein normaler BSG-Wert?",
             "answer": "Hängt von Alter und Geschlecht ab. Obergrenzen: Männer <50: <15 mm/h, >50: <20; Frauen <50: <20, >50: <30 mm/h."},
            {"question": "Was verursacht eine erhöhte BSG?",
             "answer": "Häufige Ursachen sind Infektionen, Autoimmunerkrankungen, Krebs, Anämie, Schwangerschaft und chronische Nierenerkrankung."},
            {"question": "Wann zum Arzt bei erhöhter BSG?",
             "answer": "Sprechen Sie mit Ihrem Arzt bei jeder auffälligen BSG. Dringende Abklärung bei >100 mm/h oder ungeklärtem Fieber, Gewichtsverlust oder Nachtschweiß."},
        ],
        "fr": [
            {"question": "Quelle est la VS normale ?",
             "answer": "Dépend de l'âge et du sexe. Limites : hommes <50 ans : <15 mm/h, >50 : <20 ; femmes <50 : <20, >50 : <30 mm/h."},
            {"question": "Quelles sont les causes d'une VS élevée ?",
             "answer": "Infections, maladies auto-immunes, cancer, anémie, grossesse et insuffisance rénale chronique. La VS est non spécifique."},
            {"question": "Quand consulter pour la VS ?",
             "answer": "Consultez si la VS est hors norme. Urgence si >100 mm/h ou fièvre inexpliquée, perte de poids, douleurs articulaires sévères."},
        ],
        "it": [
            {"question": "Qual è la VES normale?",
             "answer": "Dipende da età e sesso. Limiti: uomini <50 anni: <15 mm/h, >50: <20; donne <50: <20, >50: <30 mm/h."},
            {"question": "Cosa causa la VES alta?",
             "answer": "Infezioni, malattie autoimmuni, cancro, anemia, gravidanza e insufficienza renale cronica. La VES è aspecifica."},
            {"question": "Quando rivolgersi al medico per la VES?",
             "answer": "Parlate con il medico se la VES è fuori intervallo. Urgenza se >100 mm/h o febbre inspiegabile, perdita di peso, dolori articolari severi."},
        ],
        "he": [
            {"question": "מהו ערך ESR תקין?",
             "answer": "תלוי בגיל ובמין. גבולות עליונים: גברים <50: <15 mm/h, >50: <20; נשים <50: <20, >50: <30 mm/h."},
            {"question": "מה גורם ל-ESR גבוה?",
             "answer": "זיהומים, מחלות אוטואימוניות, סרטן, אנמיה, הריון ומחלת כליות כרונית. ESR הוא לא ספציפי ודורש מתאם קליני."},
            {"question": "מתי לפנות לרופא בגלל ESR?",
             "answer": "פנו לרופא בכל ESR חורג מהטווח. פנו בדחיפות אם מעל 100 mm/h או חום לא מוסבר, ירידה במשקל, כאבי מפרקים חמורים או הזעות לילה."},
        ],
        "hi": [
            {"question": "सामान्य ESR कितना होना चाहिए?",
             "answer": "यह उम्र और लिंग पर निर्भर करता है। ऊपरी सीमाएँ: 50 से कम पुरुष <15 mm/hr, 50 से अधिक <20; 50 से कम महिलाएँ <20, 50 से अधिक <30 mm/hr।"},
            {"question": "ESR बढ़ने के कारण क्या हैं?",
             "answer": "संक्रमण, ऑटोइम्यून रोग, कैंसर, एनीमिया, गर्भावस्था और क्रोनिक किडनी डिजीज। ESR नॉन-स्पेसिफिक है और क्लिनिकल कोरिलेशन ज़रूरी है।"},
            {"question": "ESR और CRP में क्या अंतर है?",
             "answer": "दोनों सूजन के मार्कर हैं लेकिन CRP, ESR से ज़्यादा तेज़ी से बढ़ता-घटता है। वे पूरक जानकारी देते हैं; डॉक्टर अक्सर दोनों मँगवाते हैं।"},
            {"question": "ESR के लिए डॉक्टर से कब मिलें?",
             "answer": "ESR रेफरेंस रेंज से बाहर हो तो डॉक्टर से बात करें। 100 mm/hr से ऊपर हो या अस्पष्ट बुखार, वज़न कम होना, गंभीर जोड़ दर्द हो तो तुरंत सहायता लें।"},
        ],
        "ar": [
            {"question": "ما هو معدل ESR الطبيعي؟",
             "answer": "يعتمد على العمر والجنس. الحدود العليا: رجال <50 سنة: <15 mm/h، >50: <20؛ نساء <50: <20، >50: <30 mm/h."},
            {"question": "ما أسباب ارتفاع ESR؟",
             "answer": "العدوى، أمراض المناعة الذاتية، السرطان، فقر الدم، الحمل ومرض الكلى المزمن. ESR غير نوعي ويحتاج ربطاً سريرياً."},
            {"question": "هل ESR نفس CRP؟",
             "answer": "لا. كلاهما مؤشرا التهاب لكن CRP يرتفع وينخفض أسرع. يقدمان معلومات متكاملة ويطلبهما الأطباء معاً عادةً."},
            {"question": "متى أراجع الطبيب بسبب ESR؟",
             "answer": "راجع الطبيب عند أي ESR خارج النطاق. اطلب رعاية عاجلة إذا تجاوز 100 mm/h أو عند حمى غير مفسَّرة أو فقدان وزن أو آلام مفاصل شديدة."},
        ],
    }
