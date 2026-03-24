# -*- coding: utf-8 -*-
"""
Hemoglobin high or low blog article — full body content for all 9 languages.
Used by blog_i18n._article_hemoglobin().
Sections: intro, what-is-hemoglobin, normal-ranges, high-hemoglobin-causes,
low-hemoglobin-causes, symptoms, related-tests, when-to-see-doctor,
how-norya-helps, disclaimer.
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
            heading="Hemoglobin high or low: what your result means",
            body_html=(
                "<p>Hemoglobin (Hb or Hgb) is one of the most frequently reported values on a complete blood count (CBC). "
                "Whether the number is flagged as high or low, it raises an immediate question: <em>should I be concerned?</em> "
                "The short answer is that hemoglobin alone cannot tell you what is wrong&mdash;but it is a powerful clue your doctor uses alongside symptoms, "
                "history, and other lab results to narrow down the cause.</p>"
                "<p>This guide explains what hemoglobin is, how to read the reference ranges on your report, what can push the value up or down, "
                "and when you should talk to a healthcare professional. It is educational, not diagnostic&mdash;always discuss your results with a doctor.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="What is hemoglobin and why does it matter?",
            body_html=(
                "<p><strong>Hemoglobin</strong> is an iron-containing protein found inside red blood cells (RBCs). Its primary job is to bind oxygen in the lungs "
                "and carry it through the bloodstream to every tissue in the body, then pick up carbon dioxide and transport it back to the lungs for exhalation. "
                "Each red blood cell contains roughly 270&nbsp;million hemoglobin molecules, making it the single most abundant protein in erythrocytes.</p>"
                "<p>Because hemoglobin is so central to oxygen delivery, even modest changes in its concentration can affect how you feel. "
                "A low hemoglobin level (anemia) may leave you tired and short of breath, while an abnormally high level can thicken the blood and raise the risk of clots. "
                "That is why the CBC almost always includes hemoglobin&mdash;it gives your doctor a quick snapshot of your blood&rsquo;s oxygen-carrying capacity.</p>"
                "<p>Hemoglobin is typically measured in grams per decilitre (g/dL) or grams per litre (g/L). "
                "Labs may also report <a href=\"/en/blog/hematocrit-high-or-low\">hematocrit</a> (the percentage of blood volume occupied by red cells), "
                "which moves in the same direction as hemoglobin and provides complementary information.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal hemoglobin ranges",
            body_html=(
                "<p>Reference ranges vary slightly between laboratories, but the values below are widely accepted. "
                "Your report will show the specific range used by the lab that processed your sample. "
                "Always compare your result against <em>that</em> range rather than a generic table.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typical range (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adult men</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adult women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Pregnant women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Children (6&ndash;12&nbsp;years)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.5&ndash;15.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Newborns</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0</td></tr>'
                "</tbody></table>"
                "<p>Hemoglobin naturally trends lower during pregnancy because blood volume expands faster than red cell production. "
                "Newborns have high levels that gradually fall during the first weeks of life. "
                "Age, altitude, hydration, and even time of day can influence the number, so a single result slightly outside the range is not always cause for alarm.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Causes of high hemoglobin",
            body_html=(
                "<p>A hemoglobin above the upper reference limit is sometimes called <strong>erythrocytosis</strong> or, more colloquially, &ldquo;thick blood.&rdquo; "
                "The most common everyday cause is <strong>dehydration</strong>: when plasma volume drops, the concentration of red cells (and hemoglobin) rises artificially. "
                "Rehydrating usually normalises the value. <strong>Living at high altitude</strong> is another frequent explanation&mdash;less oxygen in the air triggers the kidneys "
                "to produce more erythropoietin (EPO), stimulating red cell production to compensate.</p>"
                "<p><strong>Smoking</strong> raises hemoglobin because carbon monoxide from cigarette smoke binds hemoglobin tightly and reduces its oxygen-carrying efficiency, "
                "prompting the body to make more red cells. <strong>Chronic lung or heart disease</strong> (e.g.&nbsp;COPD, congenital heart defects) can have a similar effect "
                "by chronically lowering blood oxygen levels.</p>"
                "<p>Less commonly, high hemoglobin can signal <strong>polycythemia vera</strong>, a myeloproliferative neoplasm in which the bone marrow overproduces red cells. "
                "This condition requires specialist evaluation and ongoing management. Other rare causes include EPO-secreting tumours and certain inherited hemoglobin variants. "
                "Your doctor will consider the clinical picture&mdash;symptoms, other CBC values, and sometimes a JAK2 mutation test&mdash;to determine the cause.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Causes of low hemoglobin (anemia)",
            body_html=(
                "<p>Low hemoglobin&mdash;commonly called <strong>anemia</strong>&mdash;is one of the most prevalent findings in routine blood work worldwide. "
                "The single most common cause is <strong>iron deficiency</strong>, which can result from inadequate dietary intake, poor absorption (e.g.&nbsp;celiac disease), "
                "or chronic blood loss (heavy menstruation, gastrointestinal bleeding). When iron stores fall, the body cannot produce enough hemoglobin, "
                "and red cells become smaller and paler (microcytic, hypochromic anemia). "
                "Related markers such as <a href=\"/en/blog/iron-low-or-high\">serum iron</a>, ferritin, and transferrin saturation help confirm iron deficiency.</p>"
                "<p><strong>Vitamin B12 and folate deficiency</strong> can also lower hemoglobin by impairing red cell production in the bone marrow. "
                "In this case, red cells tend to be larger than normal (macrocytic anemia). B12 deficiency is especially common in older adults and in people following strict vegan diets. "
                "Folate needs increase during pregnancy, making supplementation important.</p>"
                "<p><strong>Chronic disease anemia</strong> (anemia of inflammation) occurs with long-standing infections, autoimmune disorders, cancer, or chronic kidney disease. "
                "The body&rsquo;s inflammatory signals trap iron inside storage cells, limiting its availability for hemoglobin synthesis. "
                "<strong>Hemolytic anemias</strong>&mdash;conditions in which red cells are destroyed faster than they are made&mdash;and inherited disorders such as "
                "<strong>thalassemia</strong> and <strong>sickle cell disease</strong> are other important causes. Acute or chronic <strong>blood loss</strong> (surgery, trauma, GI bleeding) "
                "can also lower hemoglobin rapidly.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of high and low hemoglobin",
            body_html=(
                "<p><strong>Low hemoglobin</strong> symptoms reflect reduced oxygen delivery: fatigue, weakness, pale skin and mucous membranes, shortness of breath on exertion, "
                "dizziness, cold hands and feet, headache, and rapid or irregular heartbeat. Severe anemia can cause chest pain or fainting. "
                "Symptoms often develop gradually, so some people adapt and do not notice mild anemia until it is detected on a blood test.</p>"
                "<p><strong>High hemoglobin</strong> symptoms are less specific and may include headache, blurred vision, flushing of the face, dizziness, and itching (especially after a warm bath). "
                "Because elevated hemoglobin thickens the blood, it can increase the risk of blood clots&mdash;deep vein thrombosis, pulmonary embolism, stroke, or heart attack&mdash;making "
                "medical evaluation important even when symptoms are mild.</p>"
                "<p>It is worth noting that many people with mildly abnormal hemoglobin have no symptoms at all. "
                "The absence of symptoms does not necessarily mean the result is insignificant; your doctor can assess whether further investigation is needed based on the degree of abnormality "
                "and your overall clinical context.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests your doctor may review",
            body_html=(
                "<p>Hemoglobin is part of the CBC, which also includes <a href=\"/en/blog/hematocrit-high-or-low\">hematocrit (HCT)</a>, red blood cell count (RBC), "
                "and red cell indices such as MCV (mean corpuscular volume), MCH (mean corpuscular hemoglobin), and MCHC. "
                "These indices help classify the type of anemia&mdash;for example, a low MCV suggests iron deficiency or thalassemia, "
                "while a high MCV may point to B12 or folate deficiency.</p>"
                "<p>Depending on the clinical picture, your doctor may also order a <strong>reticulocyte count</strong> (to see how actively the bone marrow is producing new red cells), "
                "<strong>iron studies</strong> (serum iron, ferritin, TIBC, transferrin saturation), <strong>vitamin B12 and folate levels</strong>, "
                "a <strong>peripheral blood smear</strong>, and sometimes specialised tests such as hemoglobin electrophoresis (for thalassemia or sickle cell screening) "
                "or a <strong>JAK2 mutation</strong> test (for suspected polycythemia vera). "
                "The combination of results paints a much clearer picture than hemoglobin alone.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>You should discuss your hemoglobin result with a healthcare professional if it falls outside the reference range on your report&mdash;even if you feel well. "
                "Seek <strong>prompt</strong> medical attention if you experience severe fatigue, chest pain, shortness of breath at rest, fainting, "
                "unusually rapid heartbeat, or visible blood loss (e.g.&nbsp;dark stools or heavy menstruation).</p>"
                "<p>If your hemoglobin is high, symptoms like persistent headaches, vision changes, or signs of a blood clot (leg swelling, sudden chest pain, difficulty breathing) "
                "warrant urgent evaluation. Even a mild abnormality deserves a conversation with your doctor so they can decide whether repeat testing, "
                "additional investigations, or a referral is appropriate.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare. Upload your blood test report at <a href=\"/analyze\">noryaai.com/analyze</a> and receive "
                "a clear, structured summary that explains your hemoglobin and other CBC values in plain language, complete with reference ranges and context. "
                "This makes it easier to understand what the numbers mean and to have a more informed conversation with your doctor.</p>"
                "<p>Whether you are tracking iron-deficiency anemia over time or simply want to know what &ldquo;Hgb 11.2 g/dL&rdquo; means, "
                "Norya organises your results so you can focus on asking the right questions at your next appointment. "
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
            heading="Hemoglobin yüksek veya düşük: sonucunuz ne anlama geliyor?",
            body_html=(
                "<p>Hemoglobin (Hb veya Hgb), tam kan sayımında (CBC) en sık raporlanan değerlerden biridir. "
                "Sonuç yüksek veya düşük olarak işaretlendiğinde akla hemen bir soru gelir: <em>endişelenmeli miyim?</em> "
                "Kısa yanıt şudur: hemoglobin tek başına neyin yanlış olduğunu söyleyemez&mdash;ancak hekiminizin belirtileriniz, öykünüz ve diğer laboratuvar sonuçlarıyla birlikte "
                "değerlendirdiği güçlü bir ipucudur.</p>"
                "<p>Bu rehber hemoglobinin ne olduğunu, raporunuzdaki referans aralıklarını nasıl okuyacağınızı, değeri yükselten veya düşüren nedenleri "
                "ve ne zaman bir sağlık uzmanıyla görüşmeniz gerektiğini açıklıyor. Eğitim amaçlıdır, teşhis değildir&mdash;sonuçlarınızı mutlaka bir hekimle değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Hemoglobin nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Hemoglobin</strong>, kırmızı kan hücrelerinin (eritrosit) içinde bulunan demir içerikli bir proteindir. "
                "Temel görevi akciğerlerde oksijeni bağlayıp kan dolaşımı yoluyla vücuttaki tüm dokulara taşımak, ardından karbondioksiti alıp tekrar akciğerlere geri getirmektir. "
                "Her eritrosit yaklaşık 270&nbsp;milyon hemoglobin molekülü taşır; bu da hemoglobini kırmızı kan hücrelerindeki en bol protein yapar.</p>"
                "<p>Hemoglobin oksijen taşımada bu kadar merkezi bir rol oynadığı için, konsantrasyonundaki küçük değişiklikler bile nasıl hissettiğinizi etkileyebilir. "
                "Düşük hemoglobin (anemi) yorgunluk ve nefes darlığına yol açabilirken, anormal derecede yüksek bir düzey kanı koyulaştırıp pıhtı riskini artırabilir. "
                "Bu nedenle CBC&rsquo;de neredeyse her zaman hemoglobin bulunur&mdash;hekiminize kanınızın oksijen taşıma kapasitesi hakkında hızlı bir görüntü verir.</p>"
                "<p>Hemoglobin genellikle gram/desilitre (g/dL) veya gram/litre (g/L) cinsinden ölçülür. "
                "Laboratuvarlar ayrıca <a href=\"/tr/blog/hematokrit-yuksekligi-veya-dusuklugu\">hematokrit</a> (kan hacminin kırmızı hücreler tarafından kaplanan yüzdesi) değerini de raporlayabilir; "
                "hematokrit hemoglobinle aynı yönde hareket eder ve tamamlayıcı bilgi sağlar.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal hemoglobin aralıkları",
            body_html=(
                "<p>Referans aralıkları laboratuvarlar arasında hafif farklılık gösterebilir; aşağıdaki değerler yaygın kabul gören aralıklardır. "
                "Raporunuzda numunenizi işleyen laboratuvarın kullandığı spesifik aralık yer alacaktır. "
                "Sonucunuzu her zaman genel bir tablo yerine <em>o</em> aralıkla karşılaştırın.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tipik aralık (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yetişkin erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yetişkin kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hamile kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Çocuklar (6&ndash;12&nbsp;yaş)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,5&ndash;15,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yenidoğanlar</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0</td></tr>'
                "</tbody></table>"
                "<p>Hamilelikte kan hacmi kırmızı hücre üretiminden daha hızlı arttığı için hemoglobin doğal olarak düşer. "
                "Yenidoğanlarda yüksek seviyeler yaşamın ilk haftalarında kademeli olarak düşer. "
                "Yaş, yükseklik, hidrasyon durumu ve hatta günün saati değeri etkileyebilir; bu yüzden aralığın biraz dışında kalan tek bir sonuç her zaman alarm sebebi değildir.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Hemoglobin yüksekliğinin nedenleri",
            body_html=(
                "<p>Üst referans sınırını aşan hemoglobin bazen <strong>eritrositoz</strong> olarak adlandırılır. "
                "En sık günlük neden <strong>dehidratasyon</strong>dur: plazma hacmi düştüğünde kırmızı hücre (ve hemoglobin) konsantrasyonu yapay olarak yükselir. "
                "Sıvı alımını düzeltmek genellikle değeri normalleştirir. <strong>Yüksek rakımda yaşamak</strong> bir diğer sık açıklamadır&mdash;havada daha az oksijen bulunması "
                "böbreklerin daha fazla eritropoietin (EPO) üretmesini tetikler ve kırmızı hücre üretimini artırır.</p>"
                "<p><strong>Sigara</strong> hemoglobini yükseltir çünkü sigara dumanındaki karbon monoksit hemoglobine sıkıca bağlanarak oksijen taşıma verimini düşürür; "
                "bu da vücudu daha fazla kırmızı hücre üretmeye iter. <strong>Kronik akciğer veya kalp hastalığı</strong> (KOAH, doğuştan kalp defektleri gibi) "
                "kan oksijen düzeylerini kronik olarak düşürerek benzer bir etki yapabilir.</p>"
                "<p>Daha nadir olarak yüksek hemoglobin, kemik iliğinin kırmızı hücreleri aşırı ürettiği miyeloproliferatif bir neoplazm olan <strong>polisitemi vera</strong>&rsquo;ya "
                "işaret edebilir. Bu durum uzman değerlendirmesi ve sürekli takip gerektirir. Diğer nadir nedenler arasında EPO salgılayan tümörler ve bazı kalıtsal hemoglobin varyantları bulunur. "
                "Hekiminiz belirtileri, diğer CBC değerlerini ve bazen JAK2 mutasyon testini göz önünde bulundurarak nedeni belirleyecektir.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Hemoglobin düşüklüğünün nedenleri (anemi)",
            body_html=(
                "<p>Düşük hemoglobin&mdash;yaygın adıyla <strong>anemi</strong>&mdash;dünya genelinde rutin kan tahlillerinde en sık karşılaşılan bulgulardan biridir. "
                "En sık neden <strong>demir eksikliği</strong>dir; yetersiz diyet alımı, emilim bozuklukları (örn.&nbsp;çölyak hastalığı) "
                "veya kronik kan kaybı (aşırı menstrüasyon, gastrointestinal kanama) sonucu oluşabilir. "
                "Demir depoları düştüğünde vücut yeterli hemoglobin üretemez; kırmızı hücreler küçülür ve soluklaşır (mikrositik, hipokromik anemi). "
                "<a href=\"/tr/blog/demir-eksikligi-veya-fazlaligi\">Serum demir</a>, ferritin ve transferrin satürasyonu gibi ilgili belirteçler demir eksikliğini doğrulamaya yardımcı olur.</p>"
                "<p><strong>B12 vitamini ve folat eksikliği</strong> de kemik iliğinde kırmızı hücre üretimini bozarak hemoglobini düşürebilir. "
                "Bu durumda kırmızı hücreler normalden büyük olma eğilimindedir (makrositik anemi). "
                "B12 eksikliği özellikle yaşlılarda ve katı vegan diyetleri uygulayanlarda yaygındır. Hamilelikte folat ihtiyacı artar.</p>"
                "<p><strong>Kronik hastalık anemisi</strong> (inflamasyon anemisi) uzun süreli enfeksiyonlar, otoimmün hastalıklar, kanser veya kronik böbrek hastalığı ile ortaya çıkar. "
                "<strong>Hemolitik anemiler</strong>&mdash;kırmızı hücrelerin üretildiklerinden daha hızlı yıkıldığı durumlar&mdash;ve <strong>talasemi</strong>, <strong>orak hücre hastalığı</strong> "
                "gibi kalıtsal bozukluklar da önemli nedenler arasındadır. Akut veya kronik <strong>kan kaybı</strong> (cerrahi, travma, GI kanama) hemoglobini hızla düşürebilir.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Yüksek ve düşük hemoglobin belirtileri",
            body_html=(
                "<p><strong>Düşük hemoglobin</strong> belirtileri azalmış oksijen taşınmasını yansıtır: yorgunluk, halsizlik, soluk cilt ve mukoza zarları, "
                "eforla nefes darlığı, baş dönmesi, soğuk el ve ayaklar, baş ağrısı ve hızlı veya düzensiz kalp atışı. Ciddi anemi göğüs ağrısı veya bayılmaya neden olabilir. "
                "Belirtiler genellikle yavaş gelişir; bu yüzden bazı kişiler hafif anemiyi kan testinde saptanana kadar fark etmez.</p>"
                "<p><strong>Yüksek hemoglobin</strong> belirtileri daha az spesifiktir; baş ağrısı, bulanık görme, yüzde kızarma, baş dönmesi ve kaşıntı (özellikle sıcak banyodan sonra) olabilir. "
                "Yüksek hemoglobin kanı koyulaştırdığından pıhtı riskini artırabilir&mdash;derin ven trombozu, pulmoner emboli, inme veya kalp krizi&mdash;bu da belirtiler hafif olsa bile "
                "tıbbi değerlendirmeyi önemli kılar.</p>"
                "<p>Hafif derecede anormal hemoglobini olan birçok kişinin hiç belirtisi olmadığını belirtmek gerekir. "
                "Belirtilerin olmaması sonucun önemsiz olduğu anlamına gelmez; hekiminiz anormalliğin derecesine ve genel klinik durumunuza göre ek araştırma gerekip gerekmediğini değerlendirebilir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Hekimin değerlendirebileceği ilişkili testler",
            body_html=(
                "<p>Hemoglobin, <a href=\"/tr/blog/hematokrit-yuksekligi-veya-dusuklugu\">hematokrit (HCT)</a>, kırmızı kan hücresi sayısı (RBC) "
                "ve MCV, MCH, MCHC gibi eritrosit indekslerini de içeren CBC&rsquo;nin bir parçasıdır. "
                "Bu indeksler anemi tipini sınıflandırmaya yardımcı olur&mdash;örneğin düşük MCV demir eksikliği veya talasemiyi düşündürürken, "
                "yüksek MCV B12 veya folat eksikliğine işaret edebilir.</p>"
                "<p>Klinik tabloya bağlı olarak hekiminiz <strong>retikülosit sayımı</strong>, <strong>demir çalışmaları</strong> (serum demir, ferritin, TDBK, transferrin satürasyonu), "
                "<strong>B12 ve folat düzeyleri</strong>, <strong>periferik yayma</strong> ve bazen hemoglobin elektroforezi veya <strong>JAK2 mutasyon testi</strong> gibi "
                "özel testler de isteyebilir. Sonuçların bir arada değerlendirilmesi, tek başına hemoglobinden çok daha net bir tablo ortaya koyar.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman hekime başvurmalısınız?",
            body_html=(
                "<p>Hemoglobin sonucunuz raporunuzdaki referans aralığının dışındaysa&mdash;kendinizi iyi hissetseniz bile&mdash;bir sağlık uzmanıyla görüşmelisiniz. "
                "Ciddi yorgunluk, göğüs ağrısı, istirahatte nefes darlığı, bayılma, anormal derecede hızlı kalp atışı veya görünür kan kaybı (koyu dışkı, aşırı menstrüasyon) "
                "durumunda <strong>acil</strong> tıbbi yardım alın.</p>"
                "<p>Hemoglobininiz yüksekse inatçı baş ağrıları, görme değişiklikleri veya pıhtı belirtileri (bacak şişmesi, ani göğüs ağrısı, nefes almada güçlük) "
                "acil değerlendirme gerektirir. Hafif bir anormallik bile hekiminizle konuşulmaya değerdir; tekrar test, ek araştırma veya sevk gerekip gerekmediğine karar verebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;randevunuza hazırlanmanıza yardımcı olur. Kan tahlili raporunuzu <a href=\"/analyze\">noryaai.com/analyze</a> adresinden yükleyin; "
                "hemoglobin ve diğer CBC değerlerinizi sade dilde, referans aralıkları ve bağlamlarıyla birlikte açıklayan net, yapılandırılmış bir özet alın. "
                "Bu sayede rakamların ne anlama geldiğini anlamak ve hekiminizle daha bilinçli bir görüşme yapmak kolaylaşır.</p>"
                "<p>İster demir eksikliği anemisini zaman içinde takip edin, ister &ldquo;Hgb 11,2 g/dL&rdquo; ne demek bilmek isteyin; "
                "Norya sonuçlarınızı düzenler, böylece bir sonraki randevunuzda doğru soruları sormaya odaklanabilirsiniz. "
                "Plan seçenekleri ve fiyatlar için <a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
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
# Spanish
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Hemoglobina alta o baja: qué significa tu resultado",
            body_html=(
                "<p>La hemoglobina (Hb o Hgb) es uno de los valores que más aparecen en un hemograma. "
                "Si está marcada como alta o baja, la primera pregunta es: <em>¿debo preocuparme?</em> "
                "La hemoglobina sola no dice qué ocurre, pero es una pista clave que el médico valora junto con síntomas, antecedentes y otros análisis.</p>"
                "<p>Esta guía explica qué es la hemoglobina, cómo leer los rangos de referencia, qué puede elevar o reducir el valor "
                "y cuándo consultar a un profesional de la salud. Es educativa, no diagnóstica&mdash;siempre comenta tus resultados con un médico.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="¿Qué es la hemoglobina y por qué importa?",
            body_html=(
                "<p><strong>La hemoglobina</strong> es una proteína que contiene hierro y se encuentra dentro de los glóbulos rojos. "
                "Su función principal es unir el oxígeno en los pulmones y transportarlo a través del torrente sanguíneo a todos los tejidos del cuerpo, "
                "y luego recoger el dióxido de carbono y llevarlo de vuelta a los pulmones. Cada glóbulo rojo contiene aproximadamente 270&nbsp;millones de moléculas de hemoglobina.</p>"
                "<p>Dado que la hemoglobina es tan central para el suministro de oxígeno, incluso cambios moderados en su concentración pueden afectar cómo te sientes. "
                "Un nivel bajo (anemia) puede causar cansancio y dificultad para respirar, mientras que un nivel anormalmente alto puede espesar la sangre y aumentar el riesgo de coágulos. "
                "Por eso el hemograma casi siempre incluye la hemoglobina.</p>"
                "<p>Se mide habitualmente en gramos por decilitro (g/dL). Los laboratorios suelen reportar también el "
                "<a href=\"/es/blog/hematocrito-alto-o-bajo\">hematocrito</a>, que se mueve en la misma dirección y aporta información complementaria.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos normales de hemoglobina",
            body_html=(
                "<p>Los rangos de referencia pueden variar ligeramente entre laboratorios. Los valores siguientes son ampliamente aceptados. "
                "Siempre compara tu resultado con el rango que aparece en <em>tu</em> informe.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango típico (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres adultos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres adultas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Embarazadas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Niños (6&ndash;12&nbsp;años)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,5&ndash;15,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Recién nacidos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0</td></tr>'
                "</tbody></table>"
                "<p>Durante el embarazo, la hemoglobina tiende a bajar porque el volumen sanguíneo aumenta más rápido que la producción de glóbulos rojos. "
                "Los recién nacidos presentan valores altos que descienden gradualmente en las primeras semanas. "
                "La edad, la altitud, la hidratación y la hora del día pueden influir, por lo que un resultado ligeramente fuera de rango no siempre es motivo de alarma.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Causas de hemoglobina alta",
            body_html=(
                "<p>La causa cotidiana más frecuente de hemoglobina alta es la <strong>deshidratación</strong>: al reducirse el volumen plasmático, "
                "la concentración de glóbulos rojos sube artificialmente. Rehidratarse suele normalizar el valor. "
                "<strong>Vivir a gran altitud</strong> es otra explicación habitual: el menor oxígeno ambiental estimula la producción de eritropoyetina (EPO) y de glóbulos rojos.</p>"
                "<p>El <strong>tabaquismo</strong> eleva la hemoglobina porque el monóxido de carbono del humo se une fuertemente a ella, reduciendo la eficiencia en el transporte de oxígeno "
                "y forzando al organismo a producir más glóbulos rojos. Las <strong>enfermedades pulmonares o cardíacas crónicas</strong> (EPOC, cardiopatías congénitas) pueden tener un efecto similar.</p>"
                "<p>Con menor frecuencia, la hemoglobina alta puede indicar <strong>policitemia vera</strong>, una neoplasia mieloproliferativa en la que la médula ósea produce glóbulos rojos en exceso. "
                "Otras causas raras incluyen tumores secretores de EPO y variantes hereditarias de hemoglobina. "
                "El médico evaluará el cuadro clínico&mdash;síntomas, otros valores del hemograma y a veces una prueba de mutación JAK2&mdash;para determinar la causa.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Causas de hemoglobina baja (anemia)",
            body_html=(
                "<p>La causa más común de hemoglobina baja es la <strong>deficiencia de hierro</strong>, que puede deberse a una ingesta insuficiente, "
                "mala absorción (p.&nbsp;ej.&nbsp;enfermedad celíaca) o pérdida crónica de sangre (menstruación abundante, sangrado gastrointestinal). "
                "Cuando las reservas de hierro caen, los glóbulos rojos se vuelven más pequeños y pálidos (anemia microcítica hipocrómica). "
                "Marcadores como el <a href=\"/es/blog/hierro-bajo-o-alto\">hierro sérico</a>, la ferritina y la saturación de transferrina ayudan a confirmar la deficiencia.</p>"
                "<p>La <strong>deficiencia de vitamina B12 y ácido fólico</strong> también puede reducir la hemoglobina al alterar la producción de glóbulos rojos (anemia macrocítica). "
                "La <strong>anemia de enfermedad crónica</strong> (anemia inflamatoria) aparece con infecciones prolongadas, enfermedades autoinmunitarias, cáncer o enfermedad renal crónica.</p>"
                "<p>Las <strong>anemias hemolíticas</strong> y trastornos hereditarios como la <strong>talasemia</strong> y la <strong>drepanocitosis</strong> son otras causas importantes. "
                "La <strong>pérdida de sangre</strong> aguda o crónica (cirugía, traumatismo, sangrado digestivo) también puede disminuir la hemoglobina rápidamente.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de hemoglobina alta y baja",
            body_html=(
                "<p>Los síntomas de <strong>hemoglobina baja</strong> reflejan la reducción del aporte de oxígeno: cansancio, debilidad, palidez, "
                "dificultad respiratoria al esfuerzo, mareos, manos y pies fríos, cefalea y palpitaciones. La anemia severa puede provocar dolor torácico o desmayos.</p>"
                "<p>Los síntomas de <strong>hemoglobina alta</strong> son menos específicos: cefalea, visión borrosa, enrojecimiento facial, mareos y prurito. "
                "Al espesar la sangre, aumenta el riesgo de trombosis venosa profunda, embolia pulmonar, ictus o infarto, por lo que la evaluación médica es importante.</p>"
                "<p>Muchas personas con hemoglobina levemente anormal no presentan síntomas. "
                "La ausencia de síntomas no significa que el resultado sea insignificante; el médico puede valorar si se requiere investigación adicional.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas que puede revisar el médico",
            body_html=(
                "<p>La hemoglobina forma parte del hemograma, que también incluye <a href=\"/es/blog/hematocrito-alto-o-bajo\">hematocrito</a>, recuento de glóbulos rojos "
                "e índices eritrocitarios (VCM, HCM, CHCM). Estos índices ayudan a clasificar la anemia&mdash;un VCM bajo sugiere ferropenia o talasemia, "
                "un VCM alto puede apuntar a déficit de B12 o folato.</p>"
                "<p>Según la sospecha, el médico puede solicitar reticulocitos, estudios de hierro (ferritina, TIBC, saturación de transferrina), "
                "niveles de B12 y folato, frotis de sangre periférica y pruebas especializadas como electroforesis de hemoglobina o prueba de mutación JAK2.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo acudir al médico?",
            body_html=(
                "<p>Consulta si tu hemoglobina está fuera del rango de referencia, aunque te sientas bien. "
                "Busca atención <strong>urgente</strong> si tienes fatiga intensa, dolor torácico, disnea en reposo, desmayo, "
                "taquicardia o pérdida visible de sangre (heces oscuras, menstruación abundante).</p>"
                "<p>Si la hemoglobina es alta, cefaleas persistentes, cambios visuales o signos de trombosis (hinchazón de pierna, dolor torácico súbito, dificultad respiratoria) "
                "requieren evaluación urgente.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo ayuda Norya",
            body_html=(
                "<p>Norya no diagnostica&mdash;te ayuda a prepararte. Sube tu analítica en <a href=\"/analyze\">noryaai.com/analyze</a> y recibe un resumen claro "
                "que explica tu hemoglobina y otros valores del hemograma en lenguaje sencillo, con rangos de referencia. "
                "Así entenderás mejor los números y podrás hablar con tu médico con más información.</p>"
                "<p>Ya sea que quieras seguir una anemia ferropénica o simplemente entender qué significa &ldquo;Hgb 11,2 g/dL&rdquo;, "
                "Norya organiza tus resultados. Consulta opciones y precios en nuestra <a href=\"/pricing\">página de precios</a>.</p>"
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
# German
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Hämoglobin hoch oder niedrig: Was Ihr Ergebnis bedeutet",
            body_html=(
                "<p>Hämoglobin (Hb) ist einer der am häufigsten berichteten Werte im Blutbild. "
                "Ob der Wert als hoch oder niedrig markiert ist, die erste Frage lautet: <em>Muss ich mir Sorgen machen?</em> "
                "Hämoglobin allein sagt nicht aus, was vorliegt&mdash;aber es ist ein starker Hinweis, den Ihr Arzt zusammen mit Symptomen, Anamnese und weiteren Laborwerten interpretiert.</p>"
                "<p>Dieser Ratgeber erklärt, was Hämoglobin ist, wie Sie die Referenzbereiche lesen, welche Ursachen den Wert erhöhen oder senken können "
                "und wann Sie einen Arzt aufsuchen sollten. Er dient der Information, nicht der Diagnose.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Was ist Hämoglobin und warum ist es wichtig?",
            body_html=(
                "<p><strong>Hämoglobin</strong> ist ein eisenhaltiges Protein in den roten Blutkörperchen (Erythrozyten). "
                "Es bindet Sauerstoff in der Lunge und transportiert ihn über den Blutkreislauf zu allen Geweben. "
                "Jedes rote Blutkörperchen enthält etwa 270&nbsp;Millionen Hämoglobin-Moleküle.</p>"
                "<p>Da Hämoglobin für die Sauerstoffversorgung zentral ist, können selbst moderate Veränderungen spürbar werden. "
                "Niedriges Hämoglobin (Anämie) kann zu Müdigkeit und Atemnot führen; ein abnorm hoher Wert kann das Blut verdicken und das Thromboserisiko erhöhen. "
                "Deshalb enthält das Blutbild fast immer den Hb-Wert.</p>"
                "<p>Hämoglobin wird in g/dL oder g/L angegeben. Labore berichten oft auch den "
                "<a href=\"/de/blog/haematokrit-hoch-oder-niedrig\">Hämatokrit</a>, der sich in die gleiche Richtung bewegt und ergänzende Informationen liefert.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Hämoglobin-Bereiche",
            body_html=(
                "<p>Die Referenzbereiche können zwischen Laboren leicht variieren. Die folgenden Werte gelten allgemein als typisch.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typischer Bereich (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frauen</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Schwangere</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kinder (6&ndash;12&nbsp;J.)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,5&ndash;15,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neugeborene</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0</td></tr>'
                "</tbody></table>"
                "<p>In der Schwangerschaft sinkt der Hb-Wert physiologisch, weil das Blutvolumen stärker zunimmt als die Erythrozytenproduktion. "
                "Neugeborene haben hohe Werte, die in den ersten Lebenswochen fallen. Alter, Höhenlage, Hydrierung und Tageszeit können den Wert beeinflussen.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Ursachen eines erhöhten Hämoglobins",
            body_html=(
                "<p>Die häufigste Alltagsursache ist <strong>Dehydratation</strong>: Sinkt das Plasmavolumen, steigt die Hb-Konzentration scheinbar an. "
                "Ausreichende Flüssigkeitszufuhr normalisiert den Wert. <strong>Höhenlage</strong> ist eine weitere Erklärung&mdash;weniger Sauerstoff regt die EPO-Produktion "
                "und damit die Erythrozytenbildung an.</p>"
                "<p><strong>Rauchen</strong> erhöht das Hämoglobin, weil Kohlenmonoxid die Sauerstofftransportkapazität mindert und der Körper kompensatorisch mehr rote Blutkörperchen bildet. "
                "<strong>Chronische Lungen- oder Herzerkrankungen</strong> (COPD, angeborene Herzfehler) können einen ähnlichen Mechanismus auslösen.</p>"
                "<p>Seltener deutet ein hoher Hb auf eine <strong>Polycythaemia vera</strong> hin, eine myeloproliferative Neoplasie. "
                "Weitere seltene Ursachen sind EPO-sezernierende Tumoren und erbliche Hämoglobin-Varianten. "
                "Der Arzt berücksichtigt Symptome, andere Blutwerte und ggf. eine JAK2-Mutationsanalyse.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Ursachen eines niedrigen Hämoglobins (Anämie)",
            body_html=(
                "<p>Die weltweit häufigste Ursache ist <strong>Eisenmangel</strong>&mdash;durch unzureichende Aufnahme, Malabsorption (z.&nbsp;B.&nbsp;Zöliakie) "
                "oder chronischen Blutverlust (starke Menstruation, gastrointestinale Blutung). Bei Eisenmangel werden die Erythrozyten kleiner und blasser (mikrozytäre Anämie). "
                "Begleitmarker wie <a href=\"/de/blog/eisen-niedrig-oder-hoch\">Serumeisen</a>, Ferritin und Transferrinsättigung helfen bei der Bestätigung.</p>"
                "<p><strong>Vitamin-B12- und Folsäuremangel</strong> stören die Erythrozytenproduktion und führen zu makrozytärer Anämie. "
                "Die <strong>Anämie der chronischen Erkrankung</strong> tritt bei langwierigen Infektionen, Autoimmunkrankheiten, Krebs oder chronischer Niereninsuffizienz auf.</p>"
                "<p><strong>Hämolytische Anämien</strong>, <strong>Thalassämie</strong> und <strong>Sichelzellkrankheit</strong> sind weitere wichtige Ursachen. "
                "Akuter oder chronischer <strong>Blutverlust</strong> (OP, Trauma, GI-Blutung) kann den Hb-Wert rasch senken.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome bei hohem und niedrigem Hämoglobin",
            body_html=(
                "<p><strong>Niedriges Hämoglobin:</strong> Müdigkeit, Schwäche, Blässe, Belastungsdyspnoe, Schwindel, kalte Extremitäten, Kopfschmerzen, Tachykardie. "
                "Schwere Anämie kann Brustschmerzen oder Synkopen verursachen.</p>"
                "<p><strong>Hohes Hämoglobin:</strong> Kopfschmerzen, verschwommenes Sehen, Gesichtsrötung, Juckreiz (besonders nach warmem Bad). "
                "Das dickere Blut erhöht das Risiko für tiefe Venenthrombosen, Lungenembolie, Schlaganfall oder Herzinfarkt.</p>"
                "<p>Viele Menschen mit leicht abweichendem Hb sind symptomfrei. Fehlen Beschwerden, heißt das nicht, dass der Befund unbedeutend ist&mdash;der Arzt kann abschätzen, ob Abklärung nötig ist.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Verwandte Tests",
            body_html=(
                "<p>Hämoglobin gehört zum Blutbild, das auch <a href=\"/de/blog/haematokrit-hoch-oder-niedrig\">Hämatokrit</a>, Erythrozyten (RBC) "
                "und Erythrozytenindizes (MCV, MCH, MCHC) umfasst. Diese Indizes helfen bei der Klassifikation der Anämie.</p>"
                "<p>Je nach Verdacht kann der Arzt Retikulozyten, Eisenstatus, B12/Folsäure, peripheren Blutausstrich, "
                "Hb-Elektrophorese oder eine JAK2-Analyse anordnen. Die Gesamtschau liefert ein viel klareres Bild als der Hb allein.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann zum Arzt?",
            body_html=(
                "<p>Wenn Ihr Hb außerhalb des Referenzbereichs liegt&mdash;auch ohne Beschwerden&mdash;sprechen Sie mit Ihrem Arzt. "
                "Suchen Sie <strong>dringend</strong> Hilfe bei schwerer Müdigkeit, Brustschmerzen, Ruhedyspnoe, Synkope, Tachykardie oder sichtbarem Blutverlust.</p>"
                "<p>Bei hohem Hb erfordern anhaltende Kopfschmerzen, Sehstörungen oder Thrombosezeichen (Beinschwellung, plötzlicher Brustschmerz) eine rasche Abklärung.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya hilft",
            body_html=(
                "<p>Norya stellt keine Diagnosen&mdash;wir helfen bei der Vorbereitung. Laden Sie Ihren Laborbericht unter <a href=\"/analyze\">noryaai.com/analyze</a> hoch "
                "und erhalten Sie eine klare Zusammenfassung, die Hämoglobin und andere Werte verständlich erklärt, mit Referenzbereichen und Einordnung.</p>"
                "<p>Ob Sie eine Eisenmangelanämie verfolgen oder wissen möchten, was &bdquo;Hb 11,2 g/dL&ldquo; bedeutet&mdash;Norya ordnet Ihre Ergebnisse. "
                "Optionen und Preise: <a href=\"/pricing\">Preisseite</a>.</p>"
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
# French
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Hémoglobine haute ou basse : ce que signifie votre résultat",
            body_html=(
                "<p>L&rsquo;hémoglobine (Hb) est l&rsquo;un des paramètres les plus courants de la numération formule sanguine (NFS). "
                "Qu&rsquo;il soit élevé ou bas, le premier réflexe est de se demander : <em>dois-je m&rsquo;inquiéter ?</em> "
                "L&rsquo;hémoglobine seule ne pose pas de diagnostic, mais c&rsquo;est un indice précieux que le médecin interprète avec les symptômes, l&rsquo;histoire et d&rsquo;autres résultats.</p>"
                "<p>Ce guide explique ce qu&rsquo;est l&rsquo;hémoglobine, comment lire les fourchettes de référence, les causes d&rsquo;élévation ou de baisse, "
                "et quand consulter. Il est éducatif, pas diagnostique.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Qu'est-ce que l'hémoglobine et pourquoi est-elle importante ?",
            body_html=(
                "<p><strong>L&rsquo;hémoglobine</strong> est une protéine riche en fer contenue dans les globules rouges. "
                "Elle fixe l&rsquo;oxygène dans les poumons et le transporte vers tous les tissus, puis ramène le dioxyde de carbone vers les poumons. "
                "Chaque globule rouge contient environ 270&nbsp;millions de molécules d&rsquo;hémoglobine.</p>"
                "<p>Comme l&rsquo;hémoglobine est au cœur du transport d&rsquo;oxygène, même des variations modérées peuvent provoquer des symptômes. "
                "Un taux bas (anémie) entraîne fatigue et essoufflement ; un taux anormalement élevé épaissit le sang et augmente le risque de caillots.</p>"
                "<p>L&rsquo;hémoglobine se mesure en g/dL ou g/L. Le laboratoire communique souvent aussi "
                "l&rsquo;<a href=\"/fr/blog/hematocrite-haut-ou-bas\">hématocrite</a>, qui évolue dans le même sens.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de l'hémoglobine",
            body_html=(
                "<p>Les fourchettes de référence varient légèrement selon les laboratoires. Les valeurs ci-dessous sont largement admises.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fourchette (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes adultes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes adultes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes enceintes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Enfants (6&ndash;12&nbsp;ans)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,5&ndash;15,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Nouveau-nés</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0</td></tr>'
                "</tbody></table>"
                "<p>Pendant la grossesse, l&rsquo;hémoglobine baisse physiologiquement car le volume sanguin augmente plus vite que la production de globules rouges. "
                "Les nouveau-nés ont des valeurs élevées qui diminuent progressivement. L&rsquo;âge, l&rsquo;altitude, l&rsquo;hydratation et l&rsquo;heure peuvent influencer le résultat.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Causes d'une hémoglobine élevée",
            body_html=(
                "<p>La cause quotidienne la plus fréquente est la <strong>déshydratation</strong> : la baisse du volume plasmatique fait monter artificiellement la concentration. "
                "Se réhydrater suffit généralement. <strong>Vivre en altitude</strong> est une autre explication courante : l&rsquo;hypoxie stimule la production d&rsquo;EPO et de globules rouges.</p>"
                "<p>Le <strong>tabagisme</strong> augmente l&rsquo;Hb car le monoxyde de carbone réduit l&rsquo;efficacité du transport d&rsquo;oxygène, "
                "forçant l&rsquo;organisme à produire plus de globules rouges. Les <strong>maladies pulmonaires ou cardiaques chroniques</strong> (BPCO, cardiopathies congénitales) ont un effet similaire.</p>"
                "<p>Plus rarement, un Hb élevé peut révéler une <strong>maladie de Vaquez</strong> (polyglobulie primitive), un néoplasme myéloprolifératif. "
                "D&rsquo;autres causes rares incluent les tumeurs sécrétrices d&rsquo;EPO. Le médecin évalue les symptômes, d&rsquo;autres paramètres et parfois la mutation JAK2.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Causes d'une hémoglobine basse (anémie)",
            body_html=(
                "<p>La cause la plus courante est la <strong>carence en fer</strong> : apport insuffisant, malabsorption (maladie cœliaque) "
                "ou pertes sanguines chroniques (règles abondantes, saignement digestif). Les globules rouges deviennent alors petits et pâles (anémie microcytaire). "
                "Le <a href=\"/fr/blog/fer-bas-ou-eleve\">fer sérique</a>, la ferritine et la saturation de la transferrine aident au diagnostic.</p>"
                "<p>La <strong>carence en vitamine B12 ou en folates</strong> provoque une anémie macrocytaire. "
                "L&rsquo;<strong>anémie des maladies chroniques</strong> survient lors d&rsquo;infections prolongées, de maladies auto-immunes, de cancers ou d&rsquo;insuffisance rénale chronique.</p>"
                "<p>Les <strong>anémies hémolytiques</strong>, la <strong>thalassémie</strong> et la <strong>drépanocytose</strong> sont d&rsquo;autres causes importantes. "
                "Les <strong>pertes sanguines</strong> aiguës ou chroniques (chirurgie, traumatisme, saignement digestif) abaissent rapidement l&rsquo;Hb.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d'une hémoglobine haute ou basse",
            body_html=(
                "<p><strong>Hémoglobine basse :</strong> fatigue, faiblesse, pâleur, essoufflement à l&rsquo;effort, vertiges, extrémités froides, céphalées, tachycardie. "
                "L&rsquo;anémie sévère peut provoquer douleur thoracique ou syncope.</p>"
                "<p><strong>Hémoglobine élevée :</strong> céphalées, vision floue, rougeur faciale, prurit. "
                "Le sang plus visqueux augmente le risque de thrombose veineuse profonde, d&rsquo;embolie pulmonaire, d&rsquo;AVC ou d&rsquo;infarctus.</p>"
                "<p>Beaucoup de personnes avec un Hb légèrement anormal n&rsquo;ont aucun symptôme. L&rsquo;absence de symptôme ne signifie pas que le résultat est anodin.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens complémentaires",
            body_html=(
                "<p>L&rsquo;hémoglobine fait partie de la NFS qui comprend aussi <a href=\"/fr/blog/hematocrite-haut-ou-bas\">hématocrite</a>, GR, VGM, TCMH, CCMH. "
                "Ces indices aident à classifier l&rsquo;anémie.</p>"
                "<p>Selon le contexte : réticulocytes, bilan martial (ferritine, CTF, saturation de la transferrine), "
                "B12 et folates, frottis sanguin, électrophorèse de l&rsquo;hémoglobine ou mutation JAK2.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter ?",
            body_html=(
                "<p>Parlez-en à votre médecin si l&rsquo;Hb sort de la fourchette, même sans symptôme. "
                "Consultez <strong>en urgence</strong> en cas de fatigue sévère, douleur thoracique, dyspnée de repos, syncope ou perte de sang visible.</p>"
                "<p>Si l&rsquo;Hb est élevée, des céphalées persistantes, des troubles visuels ou des signes de thrombose nécessitent une évaluation rapide.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide",
            body_html=(
                "<p>Norya ne pose pas de diagnostic&mdash;nous vous aidons à vous préparer. Envoyez votre bilan sur <a href=\"/analyze\">noryaai.com/analyze</a> "
                "et recevez un résumé clair qui explique votre hémoglobine et les autres paramètres en langage courant, avec fourchettes de référence.</p>"
                "<p>Que vous suiviez une anémie ferriprive ou souhaitiez comprendre &laquo;&nbsp;Hb 11,2 g/dL&nbsp;&raquo;, "
                "Norya structure vos résultats. Options et tarifs : <a href=\"/pricing\">page tarifs</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> '
                "Discutez toujours de vos résultats avec un professionnel de santé. <a href=\"/analyze\">Commencer l'analyse avec Norya</a></p>"
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
            heading="Emoglobina alta o bassa: cosa significa il tuo risultato",
            body_html=(
                "<p>L&rsquo;emoglobina (Hb) è uno dei parametri più frequenti nell&rsquo;emocromo. "
                "Se il valore è segnalato come alto o basso, la prima domanda è: <em>devo preoccuparmi?</em> "
                "L&rsquo;emoglobina da sola non dà una diagnosi, ma è un indizio fondamentale che il medico valuta insieme a sintomi, anamnesi e altri esami.</p>"
                "<p>Questa guida spiega cos&rsquo;è l&rsquo;emoglobina, come leggere gli intervalli di riferimento, le cause di valori alti o bassi "
                "e quando rivolgersi a un medico. È educativa, non diagnostica.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Cos'è l'emoglobina e perché è importante?",
            body_html=(
                "<p><strong>L&rsquo;emoglobina</strong> è una proteina contenente ferro presente nei globuli rossi. "
                "Lega l&rsquo;ossigeno nei polmoni e lo trasporta a tutti i tessuti, poi riporta l&rsquo;anidride carbonica ai polmoni. "
                "Ogni globulo rosso contiene circa 270&nbsp;milioni di molecole di emoglobina.</p>"
                "<p>Variazioni anche moderate della sua concentrazione possono influire sul benessere. "
                "Un valore basso (anemia) causa stanchezza e affanno; un valore troppo alto addensa il sangue e aumenta il rischio di trombi.</p>"
                "<p>Si misura in g/dL o g/L. L&rsquo;emocromo riporta spesso anche l&rsquo;<a href=\"/it/blog/ematocrito-alto-o-basso\">ematocrito</a>, che si muove nella stessa direzione.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali dell'emoglobina",
            body_html=(
                "<p>I valori di riferimento possono variare leggermente tra laboratori. Quelli sotto sono ampiamente accettati.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo tipico (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini adulti</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne adulte</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Gravidanza</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Bambini (6&ndash;12&nbsp;anni)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,5&ndash;15,5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neonati</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0</td></tr>'
                "</tbody></table>"
                "<p>In gravidanza l&rsquo;Hb scende fisiologicamente. Nei neonati i valori elevati calano nelle prime settimane. "
                "Età, altitudine, idratazione e ora del giorno possono influenzare il risultato.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Cause di emoglobina alta",
            body_html=(
                "<p>La causa più comune nella vita quotidiana è la <strong>disidratazione</strong>: la riduzione del volume plasmatico alza artificialmente la concentrazione. "
                "Reidratarsi normalizza il valore. <strong>Vivere ad alta quota</strong> stimola la produzione di EPO e di globuli rossi.</p>"
                "<p>Il <strong>fumo</strong> aumenta l&rsquo;Hb perché il monossido di carbonio riduce l&rsquo;efficienza del trasporto di ossigeno, "
                "spingendo l&rsquo;organismo a produrre più globuli rossi. Le <strong>malattie polmonari o cardiache croniche</strong> (BPCO, cardiopatie congenite) hanno un effetto simile.</p>"
                "<p>Più raramente, un&rsquo;Hb elevata può indicare una <strong>policitemia vera</strong>, una neoplasia mieloproliferativa. "
                "Altre cause rare comprendono tumori secernenti EPO e varianti ereditarie dell&rsquo;emoglobina. "
                "Il medico valuta sintomi, altri parametri e talvolta la mutazione JAK2.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Cause di emoglobina bassa (anemia)",
            body_html=(
                "<p>La causa più frequente è la <strong>carenza di ferro</strong>: insufficiente apporto alimentare, malassorbimento (celiachia) "
                "o perdite ematiche croniche (mestruazioni abbondanti, sanguinamento gastrointestinale). "
                "I globuli rossi diventano piccoli e pallidi (anemia microcitica). "
                "<a href=\"/it/blog/ferro-basso-o-alto\">Sideremia</a>, ferritina e saturazione della transferrina confermano la carenza.</p>"
                "<p>Il <strong>deficit di vitamina B12 e folati</strong> causa anemia macrocitica. "
                "L&rsquo;<strong>anemia delle malattie croniche</strong> si manifesta con infezioni prolungate, malattie autoimmuni, tumori o insufficienza renale cronica.</p>"
                "<p><strong>Anemie emolitiche</strong>, <strong>talassemia</strong> e <strong>anemia falciforme</strong> sono altre cause importanti. "
                "Le <strong>perdite ematiche</strong> acute o croniche possono abbassare rapidamente l&rsquo;Hb.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi di emoglobina alta e bassa",
            body_html=(
                "<p><strong>Emoglobina bassa:</strong> stanchezza, debolezza, pallore, dispnea da sforzo, vertigini, estremità fredde, cefalea, tachicardia. "
                "L&rsquo;anemia severa può causare dolore toracico o sincope.</p>"
                "<p><strong>Emoglobina alta:</strong> cefalea, offuscamento visivo, rossore al viso, prurito. "
                "Il sangue più denso aumenta il rischio di trombosi venosa profonda, embolia polmonare, ictus o infarto.</p>"
                "<p>Molte persone con Hb leggermente alterata non hanno sintomi. L&rsquo;assenza di sintomi non implica che il risultato sia trascurabile.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p>L&rsquo;emoglobina fa parte dell&rsquo;emocromo che include anche <a href=\"/it/blog/ematocrito-alto-o-basso\">ematocrito</a>, GR, MCV, MCH, MCHC. "
                "Gli indici aiutano a classificare il tipo di anemia.</p>"
                "<p>A seconda del sospetto: reticolociti, assetto marziale (ferritina, TIBC, saturazione transferrina), "
                "B12 e folati, striscio periferico, elettroforesi dell&rsquo;Hb o mutazione JAK2.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico",
            body_html=(
                "<p>Parla con il medico se l&rsquo;Hb esce dall&rsquo;intervallo di riferimento, anche senza sintomi. "
                "Cerca assistenza <strong>urgente</strong> in caso di affaticamento marcato, dolore toracico, dispnea a riposo, sincope o perdite ematiche visibili.</p>"
                "<p>Con Hb alta, cefalee persistenti, disturbi visivi o segni di trombosi richiedono valutazione rapida.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta",
            body_html=(
                "<p>Norya non fa diagnosi&mdash;ti aiuta a prepararti. Carica il tuo referto su <a href=\"/analyze\">noryaai.com/analyze</a> "
                "e ricevi un riepilogo chiaro che spiega emoglobina e altri valori in linguaggio semplice, con intervalli di riferimento.</p>"
                "<p>Che tu stia monitorando un&rsquo;anemia sideropenica o voglia capire &ldquo;Hb 11,2 g/dL&rdquo;, "
                "Norya organizza i risultati. Opzioni e prezzi: <a href=\"/pricing\">pagina prezzi</a>.</p>"
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
# Hebrew
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="המוגלובין גבוה או נמוך: מה המשמעות של התוצאה",
            body_html=(
                "<p>המוגלובין (Hb) הוא אחד הערכים השכיחים ביותר בספירת דם מלאה (CBC). "
                "כשהערך מסומן כגבוה או נמוך, השאלה הראשונה היא: <em>האם לדאוג?</em> "
                "המוגלובין לבדו אינו אבחנה, אך הוא רמז חשוב שהרופא מפרש יחד עם תסמינים, היסטוריה רפואית ותוצאות נוספות.</p>"
                "<p>מדריך זה מסביר מהו המוגלובין, כיצד לקרוא את טווחי הייחוס, מה יכול להעלות או להוריד את הערך, "
                "ומתי לפנות לרופא. המדריך נועד להעשרה ולא לאבחון.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="מהו המוגלובין ולמה הוא חשוב?",
            body_html=(
                "<p><strong>המוגלובין</strong> הוא חלבון המכיל ברזל הנמצא בתוך כדוריות הדם האדומות. "
                "תפקידו העיקרי הוא לקשור חמצן בריאות ולהעבירו דרך זרם הדם לכל רקמות הגוף, ואז לאסוף פחמן דו-חמצני ולהחזירו לריאות. "
                "כל כדורית דם אדומה מכילה כ-270&nbsp;מיליון מולקולות המוגלובין.</p>"
                "<p>מכיוון שהמוגלובין מרכזי כל כך להובלת חמצן, אפילו שינויים מתונים בריכוזו יכולים להשפיע על ההרגשה. "
                "ערך נמוך (אנמיה) עלול לגרום לעייפות וקוצר נשימה; ערך גבוה מדי מסמיך את הדם ומגביר סיכון לקרישים.</p>"
                "<p>המוגלובין נמדד ב-g/dL או g/L. המעבדה מדווחת לעיתים גם על "
                "<a href=\"/he/blog/hematocrit-high-or-low\">המטוקריט</a> שנע באותו כיוון ומספק מידע משלים.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי המוגלובין תקינים",
            body_html=(
                "<p>טווחי הייחוס עשויים להשתנות מעט בין מעבדות. הערכים להלן מקובלים באופן נרחב.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח טיפוסי (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים בוגרים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים בוגרות</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים בהריון</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ילדים (6&ndash;12)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.5&ndash;15.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">יילודים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0</td></tr>'
                "</tbody></table>"
                "<p>בהריון ההמוגלובין יורד באופן פיזיולוגי כי נפח הדם עולה מהר יותר מייצור כדוריות אדומות. "
                "ביילודים הערכים גבוהים ויורדים בהדרגה בשבועות הראשונים. גיל, גובה, מצב הידרציה ושעה ביום יכולים להשפיע.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="גורמים להמוגלובין גבוה",
            body_html=(
                "<p>הגורם היומיומי השכיח ביותר הוא <strong>התייבשות</strong>: כשנפח הפלזמה יורד, ריכוז ההמוגלובין עולה באופן מלאכותי. "
                "שתייה מספקת בדרך כלל מנרמלת את הערך. <strong>מגורים בגובה רב</strong> מסבירים גם: פחות חמצן מגרה ייצור EPO וכדוריות אדומות.</p>"
                "<p><strong>עישון</strong> מעלה המוגלובין כי פחמן חד-חמצני מפחית את יעילות הובלת החמצן, ומאלץ את הגוף לייצר יותר כדוריות. "
                "<strong>מחלות ריאה או לב כרוניות</strong> (COPD, מומי לב מולדים) יוצרות מנגנון דומה.</p>"
                "<p>לעיתים נדירות, המוגלובין גבוה יכול להצביע על <strong>פוליציטמיה ורה</strong>, ניאופלזמה מיאלופרוליפרטיבית. "
                "גורמים נדירים נוספים כוללים גידולים מפרישי EPO ווריאנטים תורשתיים של המוגלובין. "
                "הרופא מתחשב בתסמינים, ערכים נוספים ולעיתים בדיקת מוטציית JAK2.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="גורמים להמוגלובין נמוך (אנמיה)",
            body_html=(
                "<p>הגורם השכיח בעולם הוא <strong>חוסר ברזל</strong>&mdash;צריכה לא מספקת, ספיגה לקויה (צליאק) "
                "או איבוד דם כרוני (מחזור כבד, דימום במערכת העיכול). כדוריות הדם נעשות קטנות וחיוורות (אנמיה מיקרוציטית). "
                "סמנים כמו <a href=\"/he/blog/iron-low-or-high\">ברזל בסרום</a>, פריטין וריוויון טרנספרין עוזרים לאשר חוסר ברזל.</p>"
                "<p><strong>חוסר ויטמין B12 וחומצה פולית</strong> פוגע בייצור כדוריות אדומות וגורם לאנמיה מקרוציטית. "
                "<strong>אנמיה של מחלה כרונית</strong> מופיעה עם זיהומים ממושכים, מחלות אוטואימוניות, סרטן או אי-ספיקת כליות.</p>"
                "<p><strong>אנמיות המוליטיות</strong>, <strong>תלסמיה</strong> ו<strong>אנמיה חרמשית</strong> הם גורמים חשובים נוספים. "
                "<strong>איבוד דם</strong> חריף או כרוני (ניתוח, טראומה, דימום GI) יכול להוריד המוגלובין במהירות.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של המוגלובין גבוה ונמוך",
            body_html=(
                "<p><strong>המוגלובין נמוך:</strong> עייפות, חולשה, חיוורון, קוצר נשימה במאמץ, סחרחורת, גפיים קרות, כאב ראש, דופק מהיר. "
                "אנמיה חמורה עלולה לגרום לכאב בחזה או עילפון.</p>"
                "<p><strong>המוגלובין גבוה:</strong> כאב ראש, טשטוש ראייה, אודם בפנים, גרד (במיוחד לאחר אמבטיה חמה). "
                "דם סמיך יותר מגביר סיכון לפקקת ורידים עמוקים, תסחיף ריאתי, שבץ או התקף לב.</p>"
                "<p>אנשים רבים עם המוגלובין מעט חריג אינם חשים תסמינים כלל. העדר תסמינים אינו אומר שהתוצאה חסרת משמעות.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות קשורות",
            body_html=(
                "<p>המוגלובין הוא חלק מספירת הדם הכוללת גם <a href=\"/he/blog/hematocrit-high-or-low\">המטוקריט</a>, "
                "כדוריות אדומות (RBC) ומדדי כדוריות (MCV, MCH, MCHC) המסייעים לסווג את סוג האנמיה.</p>"
                "<p>לפי ההקשר הקליני: רטיקולוציטים, מאזן ברזל (פריטין, TIBC, ריוויון טרנספרין), "
                "B12 ופולאט, משטח דם פריפרי, אלקטרופורזת המוגלובין או בדיקת מוטציית JAK2.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>דברו עם הרופא אם ההמוגלובין חורג מטווח הייחוס, גם ללא תסמינים. "
                "פנו <strong>בדחיפות</strong> בעייפות קשה, כאב בחזה, קוצר נשימה במנוחה, עילפון או איבוד דם נראה לעין.</p>"
                "<p>אם ההמוגלובין גבוה, כאבי ראש מתמשכים, שינויי ראייה או סימני קריש (נפיחות ברגל, כאב חזה פתאומי) מצריכים בירור מהיר.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת",
            body_html=(
                "<p>Norya לא מאבחנת&mdash;אנחנו עוזרים לכם להתכונן. העלו את דוח הבדיקות שלכם ב-<a href=\"/analyze\">noryaai.com/analyze</a> "
                "וקבלו סיכום ברור המסביר המוגלובין וערכים נוספים בשפה פשוטה, עם טווחי ייחוס.</p>"
                "<p>בין אם אתם עוקבים אחר אנמיה מחוסר ברזל או רוצים להבין מה פירוש &ldquo;Hb 11.2 g/dL&rdquo;, "
                "Norya מארגנת את התוצאות. אפשרויות ומחירים: <a href=\"/pricing\">עמוד מחירים</a>.</p>"
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
# Hindi
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="हीमोग्लोबिन हाई या लो: आपके रिज़ल्ट का मतलब",
            body_html=(
                "<p>हीमोग्लोबिन (Hb या Hgb) कंप्लीट ब्लड काउंट (CBC) में सबसे ज़्यादा रिपोर्ट किए जाने वाले मानों में से एक है। "
                "अगर यह हाई या लो आता है तो पहला सवाल होता है: <em>क्या मुझे चिंता करनी चाहिए?</em> "
                "अकेले हीमोग्लोबिन किसी बीमारी की पहचान नहीं करता, लेकिन यह एक महत्वपूर्ण सुराग है जिसे डॉक्टर लक्षणों, इतिहास और दूसरे टेस्ट के साथ देखते हैं।</p>"
                "<p>यह गाइड बताती है कि हीमोग्लोबिन क्या है, रिफरेंस रेंज कैसे पढ़ें, वैल्यू बढ़ने या घटने के कारण, "
                "और कब डॉक्टर से मिलना चाहिए। यह शैक्षणिक है, डायग्नोस्टिक नहीं।</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="हीमोग्लोबिन क्या है और यह क्यों ज़रूरी है?",
            body_html=(
                "<p><strong>हीमोग्लोबिन</strong> रेड ब्लड सेल (RBC) के अंदर पाया जाने वाला आयरन-युक्त प्रोटीन है। "
                "इसका मुख्य काम फेफड़ों में ऑक्सीजन बांधना और ब्लडस्ट्रीम से शरीर के हर टिश्यू तक पहुंचाना है, फिर कार्बन डाइऑक्साइड वापस फेफड़ों तक लाना है। "
                "हर RBC में लगभग 270&nbsp;मिलियन हीमोग्लोबिन मॉलिक्यूल होते हैं।</p>"
                "<p>चूंकि हीमोग्लोबिन ऑक्सीजन डिलीवरी में इतना केंद्रीय है, इसकी सांद्रता में मामूली बदलाव भी महसूस हो सकते हैं। "
                "कम हीमोग्लोबिन (एनीमिया) थकान और सांस फूलने का कारण बन सकता है; बहुत अधिक हीमोग्लोबिन खून को गाढ़ा कर क्लॉट का खतरा बढ़ा सकता है।</p>"
                "<p>हीमोग्लोबिन g/dL या g/L में मापा जाता है। लैब अक्सर "
                "<a href=\"/hi/blog/hematocrit-high-or-low\">हीमैटोक्रिट</a> भी रिपोर्ट करती है जो उसी दिशा में चलता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य हीमोग्लोबिन रेंज",
            body_html=(
                "<p>रिफरेंस रेंज लैब के अनुसार थोड़ी भिन्न हो सकती हैं। नीचे दिए गए मान व्यापक रूप से स्वीकृत हैं।</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य रेंज (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क पुरुष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क महिलाएं</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">गर्भवती महिलाएं</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">बच्चे (6&ndash;12 वर्ष)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.5&ndash;15.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">नवजात</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0</td></tr>'
                "</tbody></table>"
                "<p>गर्भावस्था में हीमोग्लोबिन शारीरिक रूप से कम होता है क्योंकि रक्त की मात्रा RBC उत्पादन से तेज़ बढ़ती है। "
                "नवजातों में ऊंचे मान पहले हफ़्तों में धीरे-धीरे गिरते हैं। उम्र, ऊंचाई, हाइड्रेशन और दिन का समय प्रभावित कर सकते हैं।</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="हाई हीमोग्लोबिन के कारण",
            body_html=(
                "<p>सबसे आम रोज़मर्रा का कारण <strong>डिहाइड्रेशन</strong> है: जब प्लाज़्मा वॉल्यूम घटता है तो Hb कॉन्सेंट्रेशन कृत्रिम रूप से बढ़ जाती है। "
                "पर्याप्त पानी पीने से आमतौर पर सामान्य हो जाता है। <strong>अधिक ऊंचाई पर रहना</strong> भी एक कारण है&mdash;कम ऑक्सीजन EPO और RBC उत्पादन बढ़ाती है।</p>"
                "<p><strong>धूम्रपान</strong> हीमोग्लोबिन बढ़ाता है क्योंकि कार्बन मोनोऑक्साइड ऑक्सीजन ट्रांसपोर्ट क्षमता कम करता है, "
                "जिससे शरीर अधिक RBC बनाता है। <strong>क्रॉनिक फेफड़े या हृदय रोग</strong> (COPD, जन्मजात हृदय दोष) समान प्रभाव डालते हैं।</p>"
                "<p>कम आम तौर पर, हाई Hb <strong>पॉलीसाइथीमिया वेरा</strong>, एक माइलोप्रोलिफ़ेरेटिव नियोप्लाज़्म का संकेत हो सकता है। "
                "अन्य दुर्लभ कारणों में EPO स्रावित करने वाले ट्यूमर और वंशानुगत Hb वेरिएंट शामिल हैं। "
                "डॉक्टर लक्षण, अन्य CBC वैल्यू और कभी-कभी JAK2 म्यूटेशन टेस्ट देखेंगे।</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="लो हीमोग्लोबिन (एनीमिया) के कारण",
            body_html=(
                "<p>दुनिया भर में सबसे आम कारण <strong>आयरन की कमी</strong> है&mdash;अपर्याप्त आहार, खराब अवशोषण (सीलिएक रोग) "
                "या क्रॉनिक ब्लड लॉस (भारी मासिक धर्म, गैस्ट्रोइंटेस्टाइनल ब्लीडिंग)। "
                "आयरन स्टोर गिरने पर RBC छोटी और पीली हो जाती हैं (माइक्रोसाइटिक एनीमिया)। "
                "<a href=\"/hi/blog/iron-low-or-high\">सीरम आयरन</a>, फेरिटिन और ट्रांसफ़ेरिन सैचुरेशन पुष्टि में मदद करते हैं।</p>"
                "<p><strong>विटामिन B12 और फोलेट की कमी</strong> भी RBC उत्पादन प्रभावित कर हीमोग्लोबिन घटा सकती है (मैक्रोसाइटिक एनीमिया)। "
                "<strong>क्रॉनिक डिजीज़ एनीमिया</strong> लंबे संक्रमणों, ऑटोइम्यून विकारों, कैंसर या CKD के साथ होती है।</p>"
                "<p><strong>हेमोलिटिक एनीमिया</strong>, <strong>थैलेसीमिया</strong> और <strong>सिकल सेल डिजीज़</strong> अन्य महत्वपूर्ण कारण हैं। "
                "तीव्र या क्रॉनिक <strong>ब्लड लॉस</strong> (सर्जरी, ट्रॉमा, GI ब्लीडिंग) भी Hb तेज़ी से गिरा सकता है।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="हाई और लो हीमोग्लोबिन के लक्षण",
            body_html=(
                "<p><strong>लो हीमोग्लोबिन:</strong> थकान, कमज़ोरी, पीली त्वचा, मेहनत में सांस फूलना, चक्कर, ठंडे हाथ-पैर, सिरदर्द, तेज़ धड़कन। "
                "गंभीर एनीमिया में सीने में दर्द या बेहोशी हो सकती है।</p>"
                "<p><strong>हाई हीमोग्लोबिन:</strong> सिरदर्द, धुंधली दृष्टि, चेहरे पर लाली, खुजली (खासकर गर्म नहाने के बाद)। "
                "गाढ़ा खून DVT, पल्मोनरी एम्बोलिज़्म, स्ट्रोक या हार्ट अटैक का ख़तरा बढ़ाता है।</p>"
                "<p>हल्की अनॉर्मलिटी वाले कई लोगों में कोई लक्षण नहीं होते। लक्षणों की अनुपस्थिति का मतलब यह नहीं कि रिज़ल्ट महत्वहीन है।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित टेस्ट",
            body_html=(
                "<p>हीमोग्लोबिन CBC का हिस्सा है जिसमें <a href=\"/hi/blog/hematocrit-high-or-low\">हीमैटोक्रिट</a>, RBC, "
                "MCV, MCH, MCHC भी शामिल हैं। ये इंडेक्स एनीमिया के प्रकार को वर्गीकृत करने में मदद करते हैं।</p>"
                "<p>क्लिनिकल तस्वीर के अनुसार: रेटिकुलोसाइट काउंट, आयरन स्टडीज़ (फेरिटिन, TIBC, ट्रांसफ़ेरिन सैचुरेशन), "
                "B12 और फोलेट, पेरिफ़ेरल ब्लड स्मीयर, Hb इलेक्ट्रोफोरेसिस या JAK2 म्यूटेशन टेस्ट।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर हीमोग्लोबिन रिफरेंस रेंज से बाहर है&mdash;भले ही आप ठीक महसूस करें&mdash;डॉक्टर से बात करें। "
                "गंभीर थकान, सीने में दर्द, आराम में सांस फूलना, बेहोशी या दिखाई देने वाले ब्लड लॉस पर <strong>तुरंत</strong> मेडिकल अटेंशन लें।</p>"
                "<p>हाई Hb में लगातार सिरदर्द, दृष्टि बदलाव या क्लॉट के संकेत (पैर सूजना, अचानक सीने में दर्द) तत्काल मूल्यांकन की आवश्यकता रखते हैं।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya कैसे मदद करता है",
            body_html=(
                "<p>Norya डायग्नोज़ नहीं करता&mdash;हम आपकी तैयारी में मदद करते हैं। अपनी ब्लड टेस्ट रिपोर्ट <a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें "
                "और हीमोग्लोबिन व अन्य CBC वैल्यू को सरल भाषा में, रिफरेंस रेंज के साथ समझाने वाला स्पष्ट सारांश पाएं।</p>"
                "<p>चाहे आप आयरन-डेफ़िशिएंसी एनीमिया ट्रैक कर रहे हों या जानना चाहते हों कि &ldquo;Hgb 11.2 g/dL&rdquo; का मतलब क्या है, "
                "Norya आपके रिज़ल्ट व्यवस्थित करता है। प्लान और कीमत: <a href=\"/pricing\">प्राइसिंग पेज</a>।</p>"
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
# Arabic
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="الهيموغلوبين مرتفع أو منخفض: ماذا تعني نتيجتك",
            body_html=(
                "<p>الهيموغلوبين (Hb) هو أحد أكثر القيم شيوعاً في تحليل صورة الدم الكاملة (CBC). "
                "سواء كان مرتفعاً أو منخفضاً، السؤال الأول هو: <em>هل يجب أن أقلق؟</em> "
                "الهيموغلوبين وحده لا يعطي تشخيصاً، لكنه دليل مهم يفسره الطبيب مع الأعراض والتاريخ المرضي ونتائج أخرى.</p>"
                "<p>يشرح هذا الدليل ما هو الهيموغلوبين، وكيف تقرأ النطاقات المرجعية، وأسباب الارتفاع أو الانخفاض، "
                "ومتى تستشير الطبيب. هو تثقيفي وليس تشخيصياً.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="ما هو الهيموغلوبين ولماذا هو مهم؟",
            body_html=(
                "<p><strong>الهيموغلوبين</strong> بروتين يحتوي على الحديد يوجد داخل كريات الدم الحمراء. "
                "وظيفته الأساسية ربط الأكسجين في الرئتين ونقله عبر الدم إلى جميع أنسجة الجسم، ثم حمل ثاني أكسيد الكربون للرئتين. "
                "كل كرية حمراء تحتوي على حوالي 270&nbsp;مليون جزيء هيموغلوبين.</p>"
                "<p>بما أن الهيموغلوبين محوري في نقل الأكسجين، حتى التغيرات المعتدلة في تركيزه قد تؤثر على الحالة العامة. "
                "المستوى المنخفض (فقر الدم) قد يسبب إرهاقاً وضيق تنفس؛ المستوى المرتفع جداً يزيد لزوجة الدم وخطر الجلطات.</p>"
                "<p>يُقاس الهيموغلوبين بـ g/dL أو g/L. غالباً يُبلغ المختبر أيضاً عن "
                "<a href=\"/ar/blog/hematocrit-high-or-low\">الهيماتوكريت</a> الذي يتحرك في نفس الاتجاه.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="النطاقات الطبيعية للهيموغلوبين",
            body_html=(
                "<p>قد تختلف النطاقات المرجعية قليلاً بين المختبرات. القيم أدناه مقبولة على نطاق واسع.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق النموذجي (g/dL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الرجال البالغون</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">النساء البالغات</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الحوامل</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الأطفال (6&ndash;12 سنة)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.5&ndash;15.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">حديثو الولادة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0</td></tr>'
                "</tbody></table>"
                "<p>أثناء الحمل ينخفض الهيموغلوبين فسيولوجياً لأن حجم الدم يزداد أسرع من إنتاج الكريات الحمراء. "
                "عند حديثي الولادة تكون القيم مرتفعة وتنخفض تدريجياً. العمر والارتفاع والترطيب ووقت اليوم قد تؤثر.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="أسباب ارتفاع الهيموغلوبين",
            body_html=(
                "<p>السبب اليومي الأكثر شيوعاً هو <strong>الجفاف</strong>: عندما ينخفض حجم البلازما يرتفع تركيز الهيموغلوبين بشكل مصطنع. "
                "شرب سوائل كافية يُعيد القيمة عادة. <strong>العيش في ارتفاعات عالية</strong> سبب آخر&mdash;قلة الأكسجين تحفز إنتاج EPO والكريات الحمراء.</p>"
                "<p><strong>التدخين</strong> يرفع الهيموغلوبين لأن أول أكسيد الكربون يقلل كفاءة نقل الأكسجين ما يدفع الجسم لإنتاج مزيد من الكريات. "
                "<strong>أمراض الرئة أو القلب المزمنة</strong> (COPD، عيوب قلبية خلقية) تُحدث آلية مماثلة.</p>"
                "<p>بشكل أندر، قد يشير الارتفاع إلى <strong>كثرة الحمر الحقيقية</strong> (Polycythemia vera)، ورم تكاثري نقوي. "
                "أسباب نادرة أخرى تشمل أوراماً مفرزة لـ EPO ومتغيرات وراثية للهيموغلوبين. "
                "الطبيب يُقيّم الأعراض والقيم الأخرى وأحياناً طفرة JAK2.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="أسباب انخفاض الهيموغلوبين (فقر الدم)",
            body_html=(
                "<p>السبب الأكثر شيوعاً عالمياً هو <strong>نقص الحديد</strong>&mdash;نتيجة تناول غير كافٍ، سوء امتصاص (الداء البطني) "
                "أو فقدان دم مزمن (طمث غزير، نزيف هضمي). عند انخفاض مخزون الحديد تصبح الكريات صغيرة وباهتة (فقر دم صغير الكريات). "
                "<a href=\"/ar/blog/iron-low-or-high\">حديد المصل</a> والفيريتين وإشباع الترانسفيرين يساعدون في التأكيد.</p>"
                "<p><strong>نقص فيتامين B12 والفولات</strong> يسبب فقر دم كبير الكريات. "
                "<strong>فقر دم الأمراض المزمنة</strong> يظهر مع عدوى مطولة وأمراض مناعية ذاتية وسرطان وقصور كلوي مزمن.</p>"
                "<p><strong>فقر الدم الانحلالي</strong>، <strong>الثلاسيميا</strong> و<strong>فقر الدم المنجلي</strong> أسباب مهمة أخرى. "
                "<strong>فقدان الدم</strong> الحاد أو المزمن (جراحة، إصابة، نزيف هضمي) يخفض الهيموغلوبين بسرعة.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض ارتفاع وانخفاض الهيموغلوبين",
            body_html=(
                "<p><strong>هيموغلوبين منخفض:</strong> إرهاق، ضعف، شحوب، ضيق تنفس عند المجهود، دوخة، برودة الأطراف، صداع، تسارع ضربات القلب. "
                "فقر الدم الشديد قد يسبب ألم صدر أو إغماء.</p>"
                "<p><strong>هيموغلوبين مرتفع:</strong> صداع، عدم وضوح الرؤية، احمرار الوجه، حكة (خاصة بعد حمام دافئ). "
                "الدم الأكثر لزوجة يزيد خطر الخثار الوريدي العميق والانصمام الرئوي والسكتة الدماغية والنوبة القلبية.</p>"
                "<p>كثير من الأشخاص بهيموغلوبين مرتفع أو منخفض بشكل طفيف لا يعانون أعراضاً. غياب الأعراض لا يعني أن النتيجة غير مهمة.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="فحوصات ذات صلة",
            body_html=(
                "<p>الهيموغلوبين جزء من صورة الدم التي تشمل أيضاً <a href=\"/ar/blog/hematocrit-high-or-low\">الهيماتوكريت</a>، "
                "كريات الدم الحمراء (RBC) ومؤشرات الكريات (MCV، MCH، MCHC) التي تساعد في تصنيف نوع فقر الدم.</p>"
                "<p>حسب السياق السريري: الخلايا الشبكية، دراسة الحديد (فيريتين، TIBC، إشباع الترانسفيرين)، "
                "B12 وفولات، لطاخة دم محيطية، رحلان هيموغلوبين كهربائي أو فحص طفرة JAK2.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب؟",
            body_html=(
                "<p>تحدث مع طبيبك إذا كان الهيموغلوبين خارج النطاق المرجعي، حتى لو كنت تشعر بأنك بخير. "
                "اطلب مساعدة <strong>طارئة</strong> عند إرهاق شديد أو ألم صدر أو ضيق تنفس أثناء الراحة أو إغماء أو فقدان دم مرئي.</p>"
                "<p>إذا كان الهيموغلوبين مرتفعاً، فإن الصداع المستمر أو تغيرات الرؤية أو علامات الجلطة (تورم الساق، ألم صدر مفاجئ) تتطلب تقييماً سريعاً.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعد Norya",
            body_html=(
                "<p>Norya لا تُشخّص&mdash;نحن نساعدك على التحضير. ارفع تقرير فحص الدم على <a href=\"/analyze\">noryaai.com/analyze</a> "
                "واحصل على ملخص واضح يشرح الهيموغلوبين وباقي القيم بلغة بسيطة مع النطاقات المرجعية.</p>"
                "<p>سواء كنت تتابع فقر دم بنقص الحديد أو تريد فهم &ldquo;Hb 11.2 g/dL&rdquo;، "
                "Norya تنظم نتائجك. الخيارات والأسعار: <a href=\"/pricing\">صفحة الأسعار</a>.</p>"
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


# ============================================================================
# Public API
# ============================================================================

def get_hemoglobin_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for hemoglobin article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_hemoglobin_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for hemoglobin article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal hemoglobin level?",
             "answer": "Normal hemoglobin is roughly 13.5–17.5 g/dL for adult men and 12.0–16.0 g/dL for adult women, though ranges may vary slightly between laboratories. Always compare your result to the range on your own report."},
            {"question": "What causes low hemoglobin?",
             "answer": "The most common cause is iron deficiency, which can result from inadequate dietary intake, poor absorption, or chronic blood loss. Other causes include vitamin B12 or folate deficiency, chronic disease, hemolytic anemias, and inherited conditions such as thalassemia."},
            {"question": "What causes high hemoglobin?",
             "answer": "Common causes include dehydration, living at high altitude, and smoking. Less commonly, chronic lung or heart disease or polycythemia vera can raise hemoglobin."},
            {"question": "What are symptoms of low hemoglobin?",
             "answer": "Symptoms may include fatigue, weakness, pale skin, shortness of breath on exertion, dizziness, cold hands and feet, and rapid heartbeat. Severe anemia can cause chest pain or fainting."},
            {"question": "When should I see a doctor about my hemoglobin?",
             "answer": "See a doctor if your hemoglobin is outside the reference range, even without symptoms. Seek urgent attention for severe fatigue, chest pain, shortness of breath at rest, fainting, or visible blood loss."},
        ],
        "tr": [
            {"question": "Normal hemoglobin değeri nedir?",
             "answer": "Yetişkin erkeklerde yaklaşık 13,5–17,5 g/dL, kadınlarda 12,0–16,0 g/dL normal kabul edilir. Aralıklar laboratuvarlar arasında hafif farklılık gösterebilir; sonucunuzu kendi raporunuzdaki aralıkla karşılaştırın."},
            {"question": "Hemoglobin düşüklüğünün nedenleri nelerdir?",
             "answer": "En sık neden demir eksikliğidir; yetersiz beslenme, emilim bozuklukları veya kronik kan kaybından kaynaklanabilir. Diğer nedenler B12/folat eksikliği, kronik hastalık anemisi, hemolitik anemiler ve talasemidir."},
            {"question": "Hemoglobin yüksekliğinin nedenleri nelerdir?",
             "answer": "Yaygın nedenler dehidratasyon, yüksek rakımda yaşama ve sigara içmedir. Daha nadir olarak kronik akciğer/kalp hastalığı veya polisitemi vera hemoglobini yükseltebilir."},
            {"question": "Hemoglobin düşüklüğü belirtileri nelerdir?",
             "answer": "Yorgunluk, halsizlik, soluk cilt, eforla nefes darlığı, baş dönmesi, soğuk el ve ayaklar, hızlı kalp atışı olabilir. Ciddi anemi göğüs ağrısı veya bayılmaya neden olabilir."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de hemoglobina?",
             "answer": "Aproximadamente 13,5–17,5 g/dL en hombres y 12,0–16,0 g/dL en mujeres adultas. Los rangos pueden variar ligeramente entre laboratorios."},
            {"question": "¿Qué causa la hemoglobina baja?",
             "answer": "La causa más frecuente es la deficiencia de hierro, por ingesta insuficiente, mala absorción o pérdida crónica de sangre. Otras causas incluyen déficit de B12/folato, anemia de enfermedad crónica, anemias hemolíticas y talasemia."},
            {"question": "¿Cuándo debo consultar al médico por la hemoglobina?",
             "answer": "Consulta si la hemoglobina está fuera del rango de referencia, aunque te sientas bien. Busca atención urgente ante fatiga severa, dolor torácico, disnea en reposo o pérdida visible de sangre."},
        ],
        "de": [
            {"question": "Was ist ein normaler Hämoglobinwert?",
             "answer": "Bei Männern ca. 13,5–17,5 g/dL, bei Frauen 12,0–16,0 g/dL. Die Bereiche können zwischen Laboren leicht variieren."},
            {"question": "Was verursacht niedrigen Hämoglobin?",
             "answer": "Die häufigste Ursache ist Eisenmangel durch unzureichende Aufnahme, Malabsorption oder chronischen Blutverlust. Weitere Ursachen: B12-/Folsäuremangel, Anämie chronischer Erkrankungen, hämolytische Anämien und Thalassämie."},
            {"question": "Wann sollte ich wegen meines Hämoglobins zum Arzt?",
             "answer": "Sprechen Sie mit Ihrem Arzt, wenn der Hb außerhalb des Referenzbereichs liegt. Suchen Sie dringend Hilfe bei schwerer Müdigkeit, Brustschmerzen, Ruhedyspnoe oder sichtbarem Blutverlust."},
        ],
        "fr": [
            {"question": "Quel est le taux normal d'hémoglobine ?",
             "answer": "Environ 13,5–17,5 g/dL chez les hommes et 12,0–16,0 g/dL chez les femmes adultes. Les fourchettes varient légèrement selon les laboratoires."},
            {"question": "Quelles sont les causes d'une hémoglobine basse ?",
             "answer": "La plus fréquente est la carence en fer : apport insuffisant, malabsorption ou pertes sanguines chroniques. Autres causes : carence en B12/folates, anémie des maladies chroniques, anémies hémolytiques et thalassémie."},
            {"question": "Quand consulter pour son hémoglobine ?",
             "answer": "Consultez si l'Hb sort de la fourchette, même sans symptôme. Urgence en cas de fatigue sévère, douleur thoracique, dyspnée de repos ou perte de sang visible."},
        ],
        "it": [
            {"question": "Qual è il valore normale dell'emoglobina?",
             "answer": "Circa 13,5–17,5 g/dL negli uomini e 12,0–16,0 g/dL nelle donne adulte. Gli intervalli possono variare leggermente tra laboratori."},
            {"question": "Cosa causa l'emoglobina bassa?",
             "answer": "La causa più comune è la carenza di ferro: apporto insufficiente, malassorbimento o perdite ematiche croniche. Altre cause: deficit di B12/folati, anemia delle malattie croniche, anemie emolitiche e talassemia."},
            {"question": "Quando rivolgersi al medico per l'emoglobina?",
             "answer": "Parlate con il medico se l'Hb è fuori intervallo. Cercate assistenza urgente in caso di marcata stanchezza, dolore toracico, dispnea a riposo o perdite ematiche visibili."},
        ],
        "he": [
            {"question": "מהו ערך המוגלובין תקין?",
             "answer": "בגברים כ-13.5–17.5 g/dL, בנשים 12.0–16.0 g/dL. הטווחים עשויים להשתנות מעט בין מעבדות."},
            {"question": "מה גורם להמוגלובין נמוך?",
             "answer": "הגורם השכיח ביותר הוא חוסר ברזל: צריכה לא מספקת, ספיגה לקויה או איבוד דם כרוני. גורמים נוספים: חוסר B12/פולאט, אנמיה של מחלה כרונית, אנמיות המוליטיות ותלסמיה."},
            {"question": "מתי לפנות לרופא בגלל המוגלובין?",
             "answer": "פנו לרופא אם ההמוגלובין חורג מהטווח, גם ללא תסמינים. פנו בדחיפות בעייפות חמורה, כאב בחזה, קוצר נשימה במנוחה או איבוד דם נראה."},
        ],
        "hi": [
            {"question": "सामान्य हीमोग्लोबिन कितना होना चाहिए?",
             "answer": "पुरुषों में लगभग 13.5–17.5 g/dL, महिलाओं में 12.0–16.0 g/dL। रेंज लैब के अनुसार थोड़ी भिन्न हो सकती है।"},
            {"question": "लो हीमोग्लोबिन के कारण क्या हैं?",
             "answer": "सबसे आम कारण आयरन की कमी है: अपर्याप्त आहार, खराब अवशोषण या क्रॉनिक ब्लड लॉस। अन्य कारण: B12/फोलेट की कमी, क्रॉनिक डिजीज एनीमिया, हेमोलिटिक एनीमिया और थैलेसीमिया।"},
            {"question": "हीमोग्लोबिन के लिए डॉक्टर से कब मिलें?",
             "answer": "अगर Hb रिफरेंस रेंज से बाहर है तो डॉक्टर से बात करें, भले ही लक्षण न हों। गंभीर थकान, सीने में दर्द, आराम में सांस फूलना या दिखाई देने वाले ब्लड लॉस पर तुरंत अटेंशन लें।"},
        ],
        "ar": [
            {"question": "ما هو مستوى الهيموغلوبين الطبيعي؟",
             "answer": "حوالي 13.5–17.5 g/dL للرجال و12.0–16.0 g/dL للنساء البالغات. قد تختلف النطاقات قليلاً بين المختبرات."},
            {"question": "ما أسباب انخفاض الهيموغلوبين؟",
             "answer": "السبب الأكثر شيوعاً هو نقص الحديد: تناول غير كافٍ أو سوء امتصاص أو فقدان دم مزمن. أسباب أخرى: نقص B12/الفولات، فقر دم الأمراض المزمنة، فقر الدم الانحلالي والثلاسيميا."},
            {"question": "متى أراجع الطبيب بسبب الهيموغلوبين؟",
             "answer": "تحدث مع طبيبك إذا كان الهيموغلوبين خارج النطاق حتى بدون أعراض. اطلب مساعدة عاجلة عند إرهاق شديد أو ألم صدر أو ضيق تنفس أثناء الراحة أو فقدان دم مرئي."},
        ],
    }
