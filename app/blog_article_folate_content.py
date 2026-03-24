# -*- coding: utf-8 -*-
"""
Folate (Vitamin B9) blog article — full body content for all 9 languages.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_TBL = '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
_TH = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
_TD = 'style="border:1px solid #cbd5e1;padding:8px 12px;"'


# ─────────────────────────────────────────────────────────────────────
# TURKISH
# ─────────────────────────────────────────────────────────────────────
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Folat (Vitamin B9): Düşük folat ne anlama gelir?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızda <strong>folat (vitamin B9)</strong> değerinizin düşük "
                "çıkması, vücudunuzda DNA sentezi, hücre bölünmesi ve kırmızı kan hücresi üretimi "
                "için gerekli olan kritik bir vitaminin eksik olduğu anlamına gelebilir. Folat, suda "
                "çözünen bir B grubu vitaminidir ve vücutta depolanma kapasitesi sınırlıdır; bu nedenle "
                "düzenli olarak diyetle alınması gerekir.</p>"
                "<p>Folat eksikliği, megaloblastik anemi, nöral tüp defektleri (gebelikte), kardiyovasküler "
                "risk artışı ve nöropsikiyatrik belirtilerle ilişkilendirilmektedir. Özellikle gebe "
                "kadınlar, kronik hastalığı olanlar, alkol kullanım bozukluğu bulunanlar ve bazı ilaçları "
                "kullanan bireyler risk altındadır.</p>"
                "<p>Bu rehber, folat testinin ne anlama geldiğini, düşük folat nedenlerini, folik asit ile "
                "arasındaki farkı ve sağlıklı folat kaynakları hakkında bilgi sunmayı amaçlamaktadır. "
                "Amacımız teşhis koymak değil — sonuçlarınızı daha iyi anlayarak hekiminizle verimli "
                "bir görüşme yapmanıza yardımcı olmaktır.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="Folat (Vitamin B9) nedir?",
            body_html=(
                "<p><strong>Folat</strong>, doğal olarak gıdalarda bulunan B9 vitamininin genel adıdır. "
                "DNA ve RNA sentezinde, aminoasit metabolizmasında (özellikle homosistein-metiyonin "
                "dönüşümünde) ve kırmızı ile beyaz kan hücrelerinin kemik iliğinde üretiminde kritik "
                "roller üstlenir. Folat ayrıca metilasyon reaksiyonlarında kofaktör olarak görev yapar; "
                "bu reaksiyonlar gen ifadesinin düzenlenmesi ve nörotransmitter sentezi için gereklidir.</p>"
                "<p>Vücut folat depolarını yaklaşık 3–4 ay boyunca koruyabilir; bu süre sonunda yetersiz "
                "alım klinik eksiklik belirtilerine yol açar. Folatın aktif formu <em>tetrahidrofolat "
                "(THF)</em> ve türevleridir. Kandaki ölçüm genellikle serum folat veya eritrosit (RBC) "
                "folat olarak yapılır — eritrosit folat, uzun vadeli durumu daha iyi yansıtır.</p>"
                "<p>Folat eksikliği dünya genelinde en yaygın vitamin eksikliklerinden biridir ve özellikle "
                "gelişmekte olan ülkelerde, gebe kadınlarda ve kronik alkol kullananlarda sık görülür. "
                "Eksiklik, hücre bölünmesinin hızlı olduğu dokularda (kemik iliği, gastrointestinal "
                "mukoza) en belirgin şekilde kendini gösterir.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="Folat ile folik asit arasındaki fark",
            body_html=(
                "<p><strong>Folat</strong>, gıdalarda doğal olarak bulunan B9 vitamini formunu ifade eder. "
                "Yapraklı yeşil sebzeler, baklagiller, turunçgiller ve karaciğer gibi hayvansal ürünlerde "
                "bulunur. <strong>Folik asit</strong> ise folatın sentetik, oksitlenmiş formudur ve "
                "takviye gıdalarda (zenginleştirilmiş un, kahvaltılık gevrekler) ve vitamin "
                "preparatlarında kullanılır.</p>"
                "<p>İkisi arasındaki temel fark metabolizmalarında yatmaktadır. Folik asit, vücutta "
                "aktif forma dönüştürülmek için <em>dihidrofolat redüktaz (DHFR)</em> enzimi tarafından "
                "iki aşamalı redüksiyon gerektirir. Bu süreç sınırlı kapasiteye sahiptir ve yüksek dozda "
                "folik asit takviyesinde metabolize edilmemiş folik asit kanda birikebilir. Doğal folat "
                "ise doğrudan biyolojik olarak aktif formlara (5-metil-THF) dönüştürülebilir.</p>"
                "<p>MTHFR gen polimorfizmi (özellikle C677T varyantı) taşıyanlarda folik asidin aktif "
                "folata dönüşümü azalmış olabilir. Bu bireylerde doğrudan <em>metilfolat "
                "(5-MTHF)</em> takviyesi daha etkili olabilir. Ancak her iki form da folat eksikliğini "
                "önlemede etkindir ve birçok ülkede un ve tahıl ürünlerinin folik asitle "
                "zenginleştirilmesi nöral tüp defektlerini önemli ölçüde azaltmıştır.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Folat normal değerleri ve referans aralıkları",
            body_html=(
                "<p>Aşağıdaki tablo, folat için genel kabul gören referans aralıklarını özetlemektedir. "
                "Laboratuvarlar arasında küçük farklılıklar olabilir; sonuçlarınızı her zaman kendi "
                "laboratuvarınızın referans aralıklarıyla birlikte değerlendirin.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Test</th>'
                f'<th {_TH}>Normal Aralık</th>'
                f'<th {_TH}>Birim</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Serum Folat</td>'
                f'<td {_TD}>2,7 – 17,0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>Eritrosit (RBC) Folat</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>Serum Folat (SI birimleri)</td>'
                f'<td {_TD}>6,1 – 38,5</td>'
                f'<td {_TD}>nmol/L</td></tr>'
                f'</tbody></table>'
                "<p><strong>Serum folat</strong>, son günlerdeki folat alımını yansıtır ve kısa vadeli "
                "bir göstergedir. <strong>Eritrosit folat</strong>, kırmızı kan hücreleri içindeki folat "
                "miktarını ölçer ve son 2–3 aylık ortalama durumu gösterir; bu nedenle uzun vadeli "
                "değerlendirme için daha güvenilir kabul edilir.</p>"
                "<p>Serum folat değeri &lt; 2,7 ng/mL (&lt; 6,1 nmol/L) olduğunda <strong>folat "
                "eksikliği</strong> tanısı düşünülür. Homosistein düzeyi de dolaylı bir gösterge olarak "
                "kullanılır — folat eksikliğinde homosistein yükselir. B12 eksikliği de homosisteini "
                "yükselttiğinden, iki vitamin birlikte değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="Düşük folat nedenleri",
            body_html=(
                "<p>Folat eksikliğinin en yaygın nedenleri şunlardır:</p>"
                "<p><strong>Yetersiz diyet alımı:</strong> Yapraklı yeşil sebzeler, baklagiller ve "
                "zenginleştirilmiş tahıl ürünlerini yeterince tüketmemek, folat eksikliğinin en sık "
                "nedenidir. Yaşlılarda, yalnız yaşayanlarda ve beslenme alışkanlıkları kısıtlı olanlarda "
                "daha sık görülür. Pişirme (özellikle kaynatma) folat kaybına yol açar, çünkü folat ısıya "
                "ve suya duyarlıdır.</p>"
                "<p><strong>Malabsorbsiyon:</strong> Çölyak hastalığı, Crohn hastalığı, kısa bağırsak "
                "sendromu, tropikal spru ve inflamatuar bağırsak hastalıkları bağırsakta folat emilimini "
                "bozar. Özellikle jejunum, folatın emildiği primer bölge olduğundan, bu bölgeyi etkileyen "
                "hastalıklar ciddi eksikliğe neden olabilir.</p>"
                "<p><strong>Alkol kullanım bozukluğu:</strong> Kronik alkol kullanımı, folat emilimini "
                "azaltır, hepatik metabolizmayı bozar ve böbrekten folat kaybını artırır. Ayrıca alkol "
                "kullananlarda genellikle yetersiz diyet alımı da eşlik eder.</p>"
                "<p><strong>İlaçlar:</strong> Metotreksat (dihidrofolat redüktaz inhibitörü), "
                "antikonvülzanlar (fenitoin, karbamazepin, valproik asit), trimetoprim-sülfametoksazol "
                "ve oral kontraseptifler folat metabolizmasını veya emilimini olumsuz etkileyebilir. "
                "<strong>Artan gereksinim:</strong> Gebelik, emzirme, hemolitik anemi, kronik diyaliz "
                "ve malignite gibi durumlarda folat gereksinimi artar ve yetersiz alım durumunda "
                "eksiklik hızla gelişebilir.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="Folat eksikliği ve megaloblastik anemi",
            body_html=(
                "<p>Folat eksikliği, <strong>megaloblastik anemi</strong>'nin en önemli nedenlerinden "
                "biridir (diğeri B12 eksikliğidir). Megaloblastik anemi, kemik iliğinde DNA sentezinin "
                "bozulması sonucu kırmızı kan hücrelerinin olgunlaşmasının aksamasıyla ortaya çıkar. "
                "Hücreler normalden daha büyük (makrositik) ve anormal şekilli olur.</p>"
                "<p>Hemogram bulguları arasında <strong>yüksek MCV (ortalama eritrosit hacmi, tipik "
                "olarak &gt; 100 fL)</strong>, düşük hemoglobin, düşük hematokrit ve periferik yayımada "
                "<em>hipersegmente nötrofiller</em> yer alır. İleri olgularda trombositopeni "
                "(düşük trombosit) ve lökopeni (düşük beyaz küre) de gözlenebilir — bu durum "
                "<em>pansitopeni</em> olarak adlandırılır.</p>"
                "<p>Folat eksikliğine bağlı megaloblastik anemi, B12 eksikliğine bağlı olandan "
                "klinik olarak ayırt edilmelidir, çünkü B12 eksikliğinde ek olarak nörolojik "
                "komplikasyonlar (subakut kombine dejenerasyon) gelişebilir. Tedavide yalnızca folat "
                "vermek B12 eksikliğinin nörolojik bulgularını maskeleyebilir; bu nedenle her iki "
                "vitamin düzeyi birlikte değerlendirilmelidir. Folat takviyesi ile megaloblastik anemi "
                "genellikle birkaç hafta içinde düzelmeye başlar.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="Folat ve gebelik",
            body_html=(
                "<p>Folat, gebelikte en kritik vitaminlerden biridir. Gebeliğin erken dönemlerinde "
                "(konsepsiyondan sonraki ilk 28 gün) nöral tüp kapanması gerçekleşir ve bu süreçte "
                "yeterli folat düzeyi <strong>nöral tüp defektlerini (NTD)</strong> — spina bifida ve "
                "anensefali gibi ciddi doğumsal anomalileri — önemli ölçüde azaltır.</p>"
                "<p>Dünya Sağlık Örgütü (WHO) ve birçok ulusal kılavuz, gebe kalmayı planlayan tüm "
                "kadınlara en az konsepsiyondan <strong>1 ay önce</strong> başlayarak gebeliğin ilk "
                "<strong>12 haftasına</strong> kadar günde <strong>400 µg (mikrogram) folik asit</strong> "
                "takviyesi yapılmasını önerir. Daha önce NTD öyküsü olan kadınlarda bu doz "
                "<strong>4 mg/gün</strong>'e çıkarılır.</p>"
                "<p>Gebelik sırasında artan hücre bölünmesi (fötal büyüme, plasenta gelişimi, kan hacmi "
                "artışı) folat gereksinimini 5–10 kat artırır. Yetersiz folat alımı yalnızca NTD riski "
                "değil, aynı zamanda düşük doğum ağırlığı, prematüre doğum, plasenta dekolmanı ve "
                "gebeliğe bağlı anemi riskini de artırır. Pek çok ülkede un ve tahıl ürünlerinin folik "
                "asitle zenginleştirilmesi, toplumdaki NTD insidansını %20–50 oranında azaltmıştır.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Folat açısından zengin besinler",
            body_html=(
                "<p>Folatın en iyi kaynakları doğal olarak bu vitamini yüksek miktarda içeren "
                "gıdalardır:</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Gıda</th>'
                f'<th {_TH}>Porsiyon</th>'
                f'<th {_TH}>Folat (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Karaciğer (dana)</td>'
                f'<td {_TD}>85 g (pişmiş)</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>Ispanak (pişmiş)</td>'
                f'<td {_TD}>½ su bardağı</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>Siyah fasulye (pişmiş)</td>'
                f'<td {_TD}>½ su bardağı</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>Kuşkonmaz (pişmiş)</td>'
                f'<td {_TD}>4 sap</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>Brokoli (pişmiş)</td>'
                f'<td {_TD}>½ su bardağı</td>'
                f'<td {_TD}>~52</td></tr>'
                f'<tr><td {_TD}>Avokado</td>'
                f'<td {_TD}>½ adet</td>'
                f'<td {_TD}>~59</td></tr>'
                f'<tr><td {_TD}>Portakal</td>'
                f'<td {_TD}>1 orta boy</td>'
                f'<td {_TD}>~40</td></tr>'
                f'</tbody></table>'
                "<p>Pişirme yöntemi folat miktarını önemli ölçüde etkiler. Kaynatma en fazla kayba neden "
                "olur; buharda pişirme veya hafif soteler folat korunmasını artırır. Taze sebze ve "
                "meyveler en yüksek folat içeriğini sağlar.</p>"
                "<p>Birçok ülkede buğday unu ve tahıl ürünleri folik asitle zenginleştirilmektedir. "
                "Zenginleştirilmiş gıdalar, eksiklik riskini toplum düzeyinde azaltmada etkili olmuştur "
                "ancak bireysel ihtiyaçlar için doktor kontrolünde takviye gerekebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda bir sağlık profesyoneline danışmanız önerilir:</p>"
                "<p><strong>Anemi belirtileri:</strong> Sürekli yorgunluk, halsizlik, soluk cilt, nefes "
                "darlığı, çarpıntı, baş dönmesi. <strong>Nörolojik/psikiyatrik belirtiler:</strong> "
                "Konsantrasyon güçlüğü, hafıza sorunları, depresyon, irritabilite. Bu belirtiler folat "
                "eksikliğine bağlı olabileceği gibi B12 eksikliğini de düşündürebilir.</p>"
                "<p><strong>Gebelik planlıyorsanız:</strong> Folat takviyesine konsepsiyondan en az 1 ay "
                "önce başlanması önerilir. Doktorunuz uygun dozu belirleyecektir. Daha önce NTD öyküsü "
                "varsa yüksek doz folik asit gerekebilir.</p>"
                "<p><strong>Malabsorbsiyon hastalığınız varsa:</strong> Çölyak, Crohn veya kısa bağırsak "
                "sendromu hastalarında düzenli folat takibi önemlidir. Metotreksat veya antikonvülzan "
                "kullananlar da folat düzeylerini izletmelidir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızı <a href=\"/analyze\">Norya'ya yükleyerek</a> folat, B12, "
                "hemoglobin, MCV ve ilişkili biyobelirteçlerin yapılandırılmış, anlaşılır bir özetini "
                "dakikalar içinde alabilirsiniz. Norya, değerlerinizi referans aralıklarıyla "
                "karşılaştırır, anormal sonuçları vurgular ve hekim görüşmenize hazırlanmanız için "
                "net bir sağlık raporu oluşturur.</p>"
                "<p>Norya teşhis koymaz veya tedavi önermez — amacı, karmaşık laboratuvar verilerini "
                "sade bir dile çevirerek sizi bilinçli bir hasta yapmaktır. "
                "<a href=\"/analyze\">Hemen analizi başlatın</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Uyarı",
                body_html='<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. <a href="/analyze">Norya ile analiz başlat</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# ENGLISH
# ─────────────────────────────────────────────────────────────────────
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Folate (Vitamin B9): What does low folate mean?",
            body_html=(
                "<p><strong>Folate (vitamin B9)</strong> is a water-soluble B vitamin essential for DNA "
                "synthesis, cell division, and red blood cell formation. When your blood test shows low "
                "folate, it means your body may not have enough of this critical nutrient to support "
                "rapidly dividing cells, which can lead to anemia, impaired immune function, and — "
                "during pregnancy — serious birth defects.</p>"
                "<p>Folate deficiency is one of the most common vitamin deficiencies worldwide, "
                "particularly affecting pregnant women, the elderly, individuals with malabsorption "
                "disorders, those with alcohol use disorder, and people taking certain medications "
                "such as methotrexate or anticonvulsants. Because the body stores only about 3–4 months' "
                "worth of folate, inadequate dietary intake can lead to clinical deficiency relatively "
                "quickly.</p>"
                "<p>This guide explains what folate is, the difference between folate and folic acid, "
                "normal reference ranges, causes of low folate, its connection to anemia and pregnancy, "
                "and dietary sources. It is educational only and does not replace medical advice.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="What is folate (Vitamin B9)?",
            body_html=(
                "<p><strong>Folate</strong> is the generic term for the naturally occurring form of vitamin "
                "B9 found in foods. It plays critical roles in DNA and RNA synthesis, amino acid metabolism "
                "(particularly the homocysteine-to-methionine conversion), and the production of red and "
                "white blood cells in bone marrow. Folate also serves as a cofactor in methylation "
                "reactions, which are necessary for gene expression regulation and neurotransmitter "
                "synthesis.</p>"
                "<p>The body can maintain folate stores for approximately 3–4 months; after that, "
                "insufficient intake leads to clinical deficiency. The biologically active form of "
                "folate is <em>tetrahydrofolate (THF)</em> and its derivatives. Blood measurement is "
                "typically reported as serum folate or red blood cell (RBC) folate — RBC folate reflects "
                "long-term status more accurately, as it represents folate incorporated during "
                "erythropoiesis over the previous 2–3 months.</p>"
                "<p>Folate deficiency manifests most prominently in tissues with rapid cell turnover, "
                "such as bone marrow (leading to megaloblastic anemia) and the gastrointestinal "
                "mucosa (contributing to glossitis and oral ulcers). It also elevates serum homocysteine, "
                "which is independently associated with cardiovascular risk.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="Folate vs. folic acid: what's the difference?",
            body_html=(
                "<p><strong>Folate</strong> refers to the naturally occurring form of vitamin B9 found in "
                "foods such as leafy green vegetables, legumes, citrus fruits, and liver. "
                "<strong>Folic acid</strong> is the synthetic, oxidized form used in fortified foods "
                "(enriched flour, breakfast cereals) and dietary supplements. While both ultimately "
                "serve the same biochemical function, they differ in how the body metabolizes them.</p>"
                "<p>Folic acid requires a two-step enzymatic reduction by <em>dihydrofolate reductase "
                "(DHFR)</em> to become biologically active. This process has a limited capacity, and "
                "high doses of folic acid supplementation may result in unmetabolized folic acid "
                "circulating in the blood — the clinical significance of this is still under research. "
                "Natural food folate can be converted more directly into biologically active forms "
                "(5-methyltetrahydrofolate / 5-MTHF).</p>"
                "<p>Individuals carrying the MTHFR gene polymorphism (particularly the C677T variant) "
                "may have reduced ability to convert folic acid to active folate. For these individuals, "
                "supplementation with <em>methylfolate (5-MTHF)</em> may be more effective. However, "
                "both forms are effective at preventing folate deficiency, and many countries have "
                "implemented mandatory folic acid fortification of flour and grain products, "
                "substantially reducing neural tube defect rates.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal folate levels and reference ranges",
            body_html=(
                "<p>The table below summarizes commonly accepted reference ranges for folate. Note that "
                "slight variations may exist between laboratories; always interpret your results with "
                "your lab's specific reference intervals.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Test</th>'
                f'<th {_TH}>Normal Range</th>'
                f'<th {_TH}>Unit</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Serum Folate</td>'
                f'<td {_TD}>2.7 – 17.0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>RBC (Red Blood Cell) Folate</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>Serum Folate (SI units)</td>'
                f'<td {_TD}>6.1 – 38.5</td>'
                f'<td {_TD}>nmol/L</td></tr>'
                f'</tbody></table>'
                "<p><strong>Serum folate</strong> reflects recent dietary intake and is a short-term "
                "indicator. <strong>RBC folate</strong> measures folate within red blood cells and "
                "represents average status over the previous 2–3 months, making it more reliable for "
                "long-term assessment.</p>"
                "<p>A serum folate level below 2.7 ng/mL (&lt; 6.1 nmol/L) suggests <strong>folate "
                "deficiency</strong>. Elevated homocysteine is used as an indirect marker — it rises in "
                "both folate and B12 deficiency, so both vitamins should be evaluated together. "
                "Methylmalonic acid (MMA) is normal in folate deficiency but elevated in B12 deficiency, "
                "helping to distinguish between the two.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="Causes of low folate",
            body_html=(
                "<p>The most common causes of folate deficiency include:</p>"
                "<p><strong>Inadequate dietary intake:</strong> Insufficient consumption of leafy greens, "
                "legumes, and fortified grain products is the most frequent cause. It is more prevalent "
                "among the elderly, people living alone, and those with restrictive diets. Cooking "
                "(especially boiling) causes significant folate loss because folate is heat-sensitive "
                "and water-soluble — up to 50–90% can be destroyed during prolonged cooking.</p>"
                "<p><strong>Malabsorption:</strong> Celiac disease, Crohn's disease, short bowel syndrome, "
                "tropical sprue, and inflammatory bowel disease impair folate absorption in the intestine. "
                "The jejunum is the primary site of folate absorption, so diseases affecting this region "
                "can cause severe deficiency. Bariatric surgery patients are also at risk.</p>"
                "<p><strong>Alcohol use disorder:</strong> Chronic alcohol consumption reduces folate "
                "absorption, impairs hepatic metabolism, and increases renal folate loss. Alcohol users "
                "also tend to have poor dietary intake, compounding the deficiency.</p>"
                "<p><strong>Medications:</strong> Methotrexate (a DHFR inhibitor), anticonvulsants "
                "(phenytoin, carbamazepine, valproic acid), trimethoprim-sulfamethoxazole, and oral "
                "contraceptives can impair folate metabolism or absorption. <strong>Increased demand:</strong> "
                "Pregnancy, lactation, hemolytic anemia, chronic dialysis, and malignancy increase folate "
                "requirements, and inadequate intake during these states leads to rapid depletion.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="Folate deficiency and megaloblastic anemia",
            body_html=(
                "<p>Folate deficiency is one of the two main causes of <strong>megaloblastic anemia</strong> "
                "(the other being vitamin B12 deficiency). Megaloblastic anemia results from impaired DNA "
                "synthesis in the bone marrow, causing red blood cell precursors to fail to mature properly. "
                "The cells become abnormally large (macrocytic) and misshapen.</p>"
                "<p>Complete blood count (CBC) findings include a <strong>high MCV (mean corpuscular volume, "
                "typically &gt; 100 fL)</strong>, low hemoglobin, low hematocrit, and <em>hypersegmented "
                "neutrophils</em> on the peripheral blood smear. In advanced cases, thrombocytopenia (low "
                "platelets) and leukopenia (low white cells) may also develop — a condition called "
                "<em>pancytopenia</em>.</p>"
                "<p>It is critical to distinguish folate-deficiency megaloblastic anemia from B12-deficiency "
                "megaloblastic anemia, because B12 deficiency can cause additional irreversible neurological "
                "damage (subacute combined degeneration of the spinal cord). Treating with folate alone "
                "may correct the anemia but mask the underlying B12 deficiency, allowing neurological "
                "damage to progress. Both vitamin levels should always be checked together. With "
                "appropriate folate supplementation, megaloblastic anemia typically begins to improve "
                "within 1–2 weeks.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="Folate and pregnancy",
            body_html=(
                "<p>Folate is one of the most critical vitamins during pregnancy. Neural tube closure "
                "occurs within the first 28 days after conception, and adequate folate levels during this "
                "period significantly reduce the risk of <strong>neural tube defects (NTDs)</strong> such "
                "as spina bifida and anencephaly — devastating congenital anomalies that affect the "
                "brain and spinal cord.</p>"
                "<p>The World Health Organization (WHO) and numerous national guidelines recommend that "
                "all women planning pregnancy take at least <strong>400 µg (micrograms) of folic acid "
                "daily</strong>, starting at least <strong>1 month before conception</strong> and "
                "continuing through the first <strong>12 weeks of pregnancy</strong>. Women with a "
                "previous NTD-affected pregnancy should take <strong>4 mg/day</strong>.</p>"
                "<p>During pregnancy, the increased cell division required for fetal growth, placental "
                "development, and expanded maternal blood volume raises folate requirements 5- to 10-fold. "
                "Insufficient intake not only increases NTD risk but also raises the risk of low birth "
                "weight, preterm delivery, placental abruption, and pregnancy-related anemia. Many "
                "countries have mandated folic acid fortification of flour and grain products, reducing "
                "NTD incidence by 20–50% at the population level.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Dietary sources of folate",
            body_html=(
                "<p>The best sources of folate are foods that naturally contain high amounts of this "
                "vitamin:</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Food</th>'
                f'<th {_TH}>Serving</th>'
                f'<th {_TH}>Folate (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Beef liver (cooked)</td>'
                f'<td {_TD}>85 g (3 oz)</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>Spinach (cooked)</td>'
                f'<td {_TD}>½ cup</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>Black beans (cooked)</td>'
                f'<td {_TD}>½ cup</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>Asparagus (cooked)</td>'
                f'<td {_TD}>4 spears</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>Broccoli (cooked)</td>'
                f'<td {_TD}>½ cup</td>'
                f'<td {_TD}>~52</td></tr>'
                f'<tr><td {_TD}>Avocado</td>'
                f'<td {_TD}>½ fruit</td>'
                f'<td {_TD}>~59</td></tr>'
                f'<tr><td {_TD}>Orange</td>'
                f'<td {_TD}>1 medium</td>'
                f'<td {_TD}>~40</td></tr>'
                f'</tbody></table>'
                "<p>Cooking method significantly affects folate content. Boiling causes the greatest loss; "
                "steaming or light sautéing preserves more folate. Fresh vegetables and fruits provide "
                "the highest levels.</p>"
                "<p>Many countries fortify wheat flour and grain products with folic acid. Fortified foods "
                "have been effective at reducing deficiency at the population level, but individual "
                "needs may still require medical-supervised supplementation.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult a healthcare professional if any of the following apply:</p>"
                "<p><strong>Anemia symptoms:</strong> Persistent fatigue, weakness, pale skin, shortness "
                "of breath, palpitations, dizziness. <strong>Neurological/psychiatric symptoms:</strong> "
                "Difficulty concentrating, memory problems, depression, irritability. These symptoms may "
                "indicate folate deficiency but can also suggest B12 deficiency, which must be ruled out.</p>"
                "<p><strong>Planning pregnancy:</strong> Folate supplementation should begin at least 1 "
                "month before conception. Your doctor will determine the appropriate dose. A higher dose "
                "of folic acid may be needed if you have a history of NTD-affected pregnancy.</p>"
                "<p><strong>Malabsorption conditions:</strong> Patients with celiac disease, Crohn's "
                "disease, or short bowel syndrome should have regular folate monitoring. Those taking "
                "methotrexate or anticonvulsants should also have their folate levels checked regularly.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your results",
            body_html=(
                "<p>Upload your blood test report to <a href=\"/analyze\">Norya</a> and receive a "
                "structured, easy-to-understand summary of your folate, B12, hemoglobin, MCV, and "
                "related biomarkers within minutes. Norya compares your values against reference "
                "ranges, highlights abnormalities, and generates a clear health report to help you "
                "prepare for your doctor visit.</p>"
                "<p>Norya does not diagnose or recommend treatment — its purpose is to translate "
                "complex lab data into plain language so you become a more informed patient. "
                "<a href=\"/analyze\">Start your analysis now</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>This guide is for informational purposes only and does not replace medical advice or diagnosis.</strong> Always discuss your results with a healthcare professional. <a href="/analyze">Start analysis with Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# SPANISH
# ─────────────────────────────────────────────────────────────────────
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Folato (Vitamina B9): ¿Qué significa un folato bajo?",
            body_html=(
                "<p>El <strong>folato (vitamina B9)</strong> es una vitamina hidrosoluble esencial para "
                "la síntesis de ADN, la división celular y la formación de glóbulos rojos. Cuando tu "
                "análisis muestra folato bajo, puede indicar que tu cuerpo carece de este nutriente "
                "crítico, lo que puede causar anemia, deterioro inmunitario y, durante el embarazo, "
                "defectos congénitos graves.</p>"
                "<p>La deficiencia de folato es una de las más comunes a nivel mundial, afectando "
                "especialmente a embarazadas, ancianos, personas con trastornos de malabsorción, "
                "alcoholismo y quienes toman ciertos medicamentos como metotrexato o anticonvulsivos.</p>"
                "<p>Esta guía explica qué es el folato, la diferencia entre folato y ácido fólico, "
                "los rangos de referencia, causas de folato bajo y fuentes alimentarias. Es solo "
                "educativa y no sustituye el consejo médico.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="¿Qué es el folato (Vitamina B9)?",
            body_html=(
                "<p><strong>Folato</strong> es el término genérico para la forma natural de la vitamina B9 "
                "presente en los alimentos. Desempeña funciones críticas en la síntesis de ADN y ARN, "
                "el metabolismo de aminoácidos (conversión homocisteína-metionina) y la producción de "
                "glóbulos rojos y blancos en la médula ósea. También actúa como cofactor en reacciones "
                "de metilación necesarias para la regulación génica y la síntesis de neurotransmisores.</p>"
                "<p>El cuerpo puede mantener reservas de folato durante aproximadamente 3–4 meses. La "
                "forma activa es el <em>tetrahidrofolato (THF)</em>. La medición sanguínea se reporta "
                "como folato sérico o folato eritrocitario (RBC) — el folato RBC refleja mejor el "
                "estado a largo plazo.</p>"
                "<p>La deficiencia se manifiesta más en tejidos con rápida renovación celular (médula "
                "ósea, mucosa gastrointestinal) y eleva la homocisteína sérica, asociada "
                "independientemente con riesgo cardiovascular.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="Folato vs. ácido fólico: ¿cuál es la diferencia?",
            body_html=(
                "<p><strong>Folato</strong> se refiere a la forma natural de B9 en alimentos como "
                "verduras de hoja verde, legumbres, cítricos e hígado. <strong>Ácido fólico</strong> "
                "es la forma sintética utilizada en alimentos fortificados y suplementos.</p>"
                "<p>El ácido fólico requiere reducción enzimática en dos pasos por la "
                "<em>dihidrofolato reductasa (DHFR)</em> para activarse. Esta capacidad es limitada "
                "y las dosis altas pueden resultar en ácido fólico no metabolizado circulante. El "
                "folato natural se convierte más directamente en formas activas (5-metil-THF).</p>"
                "<p>Los portadores del polimorfismo MTHFR (variante C677T) pueden tener menor capacidad "
                "de conversión. Para ellos, la suplementación con <em>metilfolato (5-MTHF)</em> puede "
                "ser más eficaz. Ambas formas son efectivas para prevenir la deficiencia, y la "
                "fortificación obligatoria con ácido fólico ha reducido significativamente los "
                "defectos del tubo neural en muchos países.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de folato",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Prueba</th>'
                f'<th {_TH}>Rango normal</th>'
                f'<th {_TH}>Unidad</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Folato sérico</td>'
                f'<td {_TD}>2,7 – 17,0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>Folato eritrocitario (RBC)</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'</tbody></table>'
                "<p>El <strong>folato sérico</strong> refleja la ingesta reciente. El <strong>folato "
                "eritrocitario</strong> refleja el estado de los últimos 2–3 meses y es más fiable "
                "para la evaluación a largo plazo.</p>"
                "<p>Un folato sérico &lt; 2,7 ng/mL sugiere deficiencia. La homocisteína elevada es "
                "un marcador indirecto; el ácido metilmalónico (MMA) es normal en la deficiencia de "
                "folato pero elevado en la de B12, ayudando a distinguirlas.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="Causas de folato bajo",
            body_html=(
                "<p><strong>Ingesta dietética insuficiente:</strong> La causa más frecuente. Más "
                "prevalente en ancianos, personas con dietas restrictivas. La cocción (especialmente "
                "hervir) destruye hasta el 50–90% del folato.</p>"
                "<p><strong>Malabsorción:</strong> Enfermedad celíaca, enfermedad de Crohn, síndrome "
                "de intestino corto y esprue tropical alteran la absorción en el yeyuno.</p>"
                "<p><strong>Alcoholismo:</strong> El alcohol reduce la absorción, altera el metabolismo "
                "hepático y aumenta la pérdida renal de folato.</p>"
                "<p><strong>Medicamentos:</strong> Metotrexato, anticonvulsivos (fenitoína, "
                "carbamazepina, ácido valproico), trimetoprim-sulfametoxazol y anticonceptivos orales. "
                "<strong>Mayor demanda:</strong> Embarazo, lactancia, anemia hemolítica, diálisis "
                "crónica y neoplasias aumentan los requerimientos.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="Folato y anemia megaloblástica",
            body_html=(
                "<p>La deficiencia de folato es una causa principal de <strong>anemia megaloblástica</strong>. "
                "Resulta de la síntesis alterada de ADN en la médula ósea, produciendo eritrocitos "
                "anormalmente grandes (macrocíticos) y mal formados.</p>"
                "<p>Los hallazgos en el hemograma incluyen <strong>VCM elevado (&gt; 100 fL)</strong>, "
                "hemoglobina baja y <em>neutrófilos hipersegmentados</em>. En casos avanzados puede "
                "haber pancitopenia.</p>"
                "<p>Es crucial diferenciar de la deficiencia de B12, que además causa daño neurológico "
                "irreversible. Tratar solo con folato puede enmascarar la deficiencia de B12. Ambas "
                "vitaminas deben evaluarse conjuntamente. Con suplementación adecuada, la anemia "
                "mejora en 1–2 semanas.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="Folato y embarazo",
            body_html=(
                "<p>El folato es una de las vitaminas más críticas durante el embarazo. El cierre del "
                "tubo neural ocurre en los primeros 28 días tras la concepción, y niveles adecuados "
                "de folato reducen significativamente el riesgo de <strong>defectos del tubo neural "
                "(DTN)</strong> como espina bífida y anencefalia.</p>"
                "<p>La OMS recomienda <strong>400 µg de ácido fólico diarios</strong>, comenzando al "
                "menos 1 mes antes de la concepción y hasta la semana 12 de embarazo. Mujeres con "
                "antecedente de DTN deben tomar <strong>4 mg/día</strong>.</p>"
                "<p>Durante el embarazo, la división celular aumentada eleva los requerimientos de folato "
                "5–10 veces. La ingesta insuficiente aumenta no solo el riesgo de DTN sino también de "
                "bajo peso al nacer, parto prematuro y anemia gestacional. La fortificación obligatoria "
                "ha reducido la incidencia de DTN un 20–50% en muchos países.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Fuentes alimentarias de folato",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Alimento</th>'
                f'<th {_TH}>Porción</th>'
                f'<th {_TH}>Folato (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Hígado de res (cocido)</td>'
                f'<td {_TD}>85 g</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>Espinacas (cocidas)</td>'
                f'<td {_TD}>½ taza</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>Frijoles negros (cocidos)</td>'
                f'<td {_TD}>½ taza</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>Espárragos (cocidos)</td>'
                f'<td {_TD}>4 tallos</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>Aguacate</td>'
                f'<td {_TD}>½ pieza</td>'
                f'<td {_TD}>~59</td></tr>'
                f'</tbody></table>'
                "<p>El método de cocción influye significativamente: hervir causa la mayor pérdida. "
                "Cocinar al vapor conserva más folato. Las verduras y frutas frescas aportan los "
                "niveles más altos.</p>"
                "<p>Muchos países fortifican la harina de trigo con ácido fólico, reduciendo "
                "eficazmente la deficiencia poblacional.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p><strong>Síntomas de anemia:</strong> Fatiga persistente, debilidad, palidez, "
                "disnea, palpitaciones, mareos. <strong>Síntomas neurológicos/psiquiátricos:</strong> "
                "Dificultad de concentración, problemas de memoria, depresión, irritabilidad.</p>"
                "<p><strong>Si planeas un embarazo:</strong> Comienza la suplementación al menos 1 mes "
                "antes de la concepción.</p>"
                "<p><strong>Enfermedades de malabsorción:</strong> Pacientes con celíaca, Crohn o "
                "usuarios de metotrexato/anticonvulsivos deben monitorizar regularmente los niveles "
                "de folato.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya te ayuda a entender tus resultados",
            body_html=(
                "<p>Sube tu informe de análisis a <a href=\"/analyze\">Norya</a> y recibe en minutos "
                "un resumen estructurado de tu folato, B12, hemoglobina, VCM y biomarcadores "
                "relacionados. Norya compara tus valores con los rangos de referencia y genera un "
                "informe claro para tu visita médica.</p>"
                "<p>Norya no diagnostica ni recomienda tratamiento — traduce datos complejos a "
                "lenguaje sencillo. <a href=\"/analyze\">Comienza tu análisis ahora</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# GERMAN
# ─────────────────────────────────────────────────────────────────────
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Folat (Vitamin B9): Was bedeutet ein niedriger Folatspiegel?",
            body_html=(
                "<p><strong>Folat (Vitamin B9)</strong> ist ein wasserlösliches B-Vitamin, das für die "
                "DNA-Synthese, Zellteilung und Bildung roter Blutkörperchen unerlässlich ist. Ein "
                "niedriger Folatspiegel im Bluttest kann auf einen Mangel hindeuten, der zu Anämie, "
                "Immunschwäche und in der Schwangerschaft zu schweren Geburtsfehlern führen kann.</p>"
                "<p>Folatmangel betrifft besonders Schwangere, ältere Menschen, Patienten mit "
                "Malabsorptionsstörungen, Alkoholabhängige und Anwender bestimmter Medikamente wie "
                "Methotrexat oder Antikonvulsiva.</p>"
                "<p>Dieser Leitfaden erklärt, was Folat ist, den Unterschied zu Folsäure, "
                "Referenzbereiche, Ursachen niedriger Werte und Nahrungsquellen. Er dient "
                "ausschließlich der Aufklärung.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="Was ist Folat (Vitamin B9)?",
            body_html=(
                "<p><strong>Folat</strong> ist der Oberbegriff für die natürlich vorkommende Form von "
                "Vitamin B9 in Lebensmitteln. Es spielt eine zentrale Rolle bei der DNA- und "
                "RNA-Synthese, dem Aminosäurestoffwechsel (Homocystein-Methionin-Umwandlung) und der "
                "Produktion roter und weißer Blutzellen im Knochenmark.</p>"
                "<p>Der Körper kann Folatspeicher für etwa 3–4 Monate aufrechterhalten. Die biologisch "
                "aktive Form ist <em>Tetrahydrofolat (THF)</em>. Im Blut wird Serumfolat oder "
                "Erythrozytenfolat (RBC) gemessen — letzteres ist für die Langzeitbeurteilung "
                "zuverlässiger.</p>"
                "<p>Folatmangel zeigt sich am deutlichsten in Geweben mit schneller Zellerneuerung "
                "(Knochenmark, Magen-Darm-Schleimhaut) und erhöht das Serum-Homocystein, das "
                "unabhängig mit kardiovaskulärem Risiko assoziiert ist.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="Folat vs. Folsäure: Was ist der Unterschied?",
            body_html=(
                "<p><strong>Folat</strong> bezeichnet die natürliche Form in Lebensmitteln. "
                "<strong>Folsäure</strong> ist die synthetische Form in angereicherten Lebensmitteln "
                "und Nahrungsergänzungsmitteln.</p>"
                "<p>Folsäure muss durch <em>Dihydrofolat-Reduktase (DHFR)</em> in zwei Schritten "
                "aktiviert werden. Bei hoher Dosierung kann nicht metabolisierte Folsäure im Blut "
                "zirkulieren. Natürliches Folat wird direkter in aktive Formen (5-Methyl-THF) "
                "umgewandelt.</p>"
                "<p>Träger des MTHFR-Polymorphismus (C677T) haben möglicherweise eine verminderte "
                "Umwandlungskapazität. Für sie kann <em>Methylfolat (5-MTHF)</em> wirksamer sein. "
                "Die obligatorische Folsäureanreicherung von Mehlprodukten hat Neuralrohrdefekte in "
                "vielen Ländern deutlich reduziert.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Folatwerte",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Test</th>'
                f'<th {_TH}>Normalbereich</th>'
                f'<th {_TH}>Einheit</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Serumfolat</td>'
                f'<td {_TD}>2,7 – 17,0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>Erythrozytenfolat (RBC)</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'</tbody></table>'
                "<p><strong>Serumfolat</strong> spiegelt die aktuelle Aufnahme wider. "
                "<strong>Erythrozytenfolat</strong> zeigt den Status der letzten 2–3 Monate und ist "
                "zuverlässiger für die Langzeitbeurteilung.</p>"
                "<p>Ein Serumfolat &lt; 2,7 ng/mL deutet auf Mangel hin. Erhöhtes Homocystein dient "
                "als indirekter Marker; Methylmalonsäure (MMA) ist bei Folatmangel normal, bei "
                "B12-Mangel erhöht.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="Ursachen für niedrigen Folatspiegel",
            body_html=(
                "<p><strong>Unzureichende Ernährung:</strong> Häufigste Ursache. Kochen (besonders "
                "Kochen in Wasser) zerstört bis zu 50–90% des Folats.</p>"
                "<p><strong>Malabsorption:</strong> Zöliakie, Morbus Crohn, Kurzdarmsyndrom und "
                "tropische Sprue beeinträchtigen die Aufnahme im Jejunum.</p>"
                "<p><strong>Alkoholmissbrauch:</strong> Reduziert Absorption, beeinträchtigt den "
                "Leberstoffwechsel und erhöht den renalen Folatverlust.</p>"
                "<p><strong>Medikamente:</strong> Methotrexat, Antikonvulsiva (Phenytoin, Carbamazepin), "
                "Trimethoprim-Sulfamethoxazol, orale Kontrazeptiva. <strong>Erhöhter Bedarf:</strong> "
                "Schwangerschaft, Stillzeit, hämolytische Anämie, chronische Dialyse, Malignome.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="Folatmangel und megaloblastäre Anämie",
            body_html=(
                "<p>Folatmangel ist eine der Hauptursachen der <strong>megaloblastären Anämie</strong>. "
                "Durch gestörte DNA-Synthese entstehen abnorm große (makrozytäre) Erythrozyten.</p>"
                "<p>Blutbildbefunde umfassen ein <strong>erhöhtes MCV (&gt; 100 fL)</strong>, niedriges "
                "Hämoglobin und <em>hypersegmentierte Neutrophile</em>. Bei fortgeschrittenem Mangel "
                "kann sich eine Panzytopenie entwickeln.</p>"
                "<p>Die Unterscheidung von B12-Mangel ist entscheidend, da B12-Mangel zusätzlich "
                "irreversible neurologische Schäden verursachen kann. Eine alleinige Folat-Therapie "
                "kann die Anämie korrigieren, aber den B12-Mangel maskieren. Beide Vitamine sollten "
                "immer gemeinsam bestimmt werden.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="Folat und Schwangerschaft",
            body_html=(
                "<p>Folat ist eines der wichtigsten Vitamine in der Schwangerschaft. Der "
                "Neuralrohrverschluss erfolgt in den ersten 28 Tagen nach der Empfängnis. Ausreichende "
                "Folatspiegel reduzieren das Risiko von <strong>Neuralrohrdefekten (NRD)</strong> wie "
                "Spina bifida und Anenzephalie erheblich.</p>"
                "<p>Die WHO empfiehlt allen Frauen mit Kinderwunsch <strong>400 µg Folsäure "
                "täglich</strong>, mindestens 1 Monat vor der Empfängnis bis zur 12. "
                "Schwangerschaftswoche. Bei NRD-Vorgeschichte: <strong>4 mg/Tag</strong>.</p>"
                "<p>In der Schwangerschaft steigt der Folatbedarf um das 5- bis 10-Fache. Unzureichende "
                "Zufuhr erhöht nicht nur das NRD-Risiko, sondern auch das Risiko für niedriges "
                "Geburtsgewicht, Frühgeburt und Schwangerschaftsanämie.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Folatreiche Lebensmittel",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Lebensmittel</th>'
                f'<th {_TH}>Portion</th>'
                f'<th {_TH}>Folat (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Rinderleber (gegart)</td>'
                f'<td {_TD}>85 g</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>Spinat (gegart)</td>'
                f'<td {_TD}>½ Tasse</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>Schwarze Bohnen (gegart)</td>'
                f'<td {_TD}>½ Tasse</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>Spargel (gegart)</td>'
                f'<td {_TD}>4 Stangen</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>Avocado</td>'
                f'<td {_TD}>½ Frucht</td>'
                f'<td {_TD}>~59</td></tr>'
                f'</tbody></table>'
                "<p>Dampfgaren bewahrt mehr Folat als Kochen in Wasser. Frische Lebensmittel bieten "
                "die höchsten Gehalte. Die Anreicherung von Mehl mit Folsäure hat den Bevölkerungsstatus "
                "verbessert.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann Sie einen Arzt aufsuchen sollten",
            body_html=(
                "<p><strong>Anämiesymptome:</strong> Anhaltende Müdigkeit, Schwäche, Blässe, Atemnot, "
                "Herzklopfen, Schwindel. <strong>Neurologische Symptome:</strong> Konzentrations- und "
                "Gedächtnisprobleme, Depression, Reizbarkeit.</p>"
                "<p><strong>Kinderwunsch:</strong> Folsäure mindestens 1 Monat vor der Empfängnis "
                "beginnen.</p>"
                "<p><strong>Malabsorptionserkrankungen:</strong> Regelmäßige Folatkontrolle bei "
                "Zöliakie, Morbus Crohn, Methotrexat- oder Antikonvulsivagebrauch.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihre Ergebnisse zu verstehen",
            body_html=(
                "<p>Laden Sie Ihren Bluttest bei <a href=\"/analyze\">Norya</a> hoch und erhalten Sie "
                "in Minuten eine strukturierte Zusammenfassung von Folat, B12, Hämoglobin, MCV und "
                "verwandten Biomarkern. Norya vergleicht Ihre Werte mit Referenzbereichen und erstellt "
                "einen klaren Bericht für Ihren Arztbesuch.</p>"
                "<p>Norya diagnostiziert nicht und empfiehlt keine Behandlung — es übersetzt komplexe "
                "Labordaten in verständliche Sprache. <a href=\"/analyze\">Starten Sie jetzt Ihre "
                "Analyse</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# FRENCH
# ─────────────────────────────────────────────────────────────────────
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Folate (Vitamine B9) : que signifie un folate bas ?",
            body_html=(
                "<p>Le <strong>folate (vitamine B9)</strong> est une vitamine hydrosoluble essentielle à "
                "la synthèse de l'ADN, à la division cellulaire et à la formation des globules rouges. "
                "Un taux bas de folate peut indiquer un manque de ce nutriment critique, pouvant entraîner "
                "une anémie, une altération de l'immunité et, pendant la grossesse, des malformations "
                "congénitales graves.</p>"
                "<p>La carence en folate touche particulièrement les femmes enceintes, les personnes "
                "âgées, les patients souffrant de malabsorption, d'alcoolisme et ceux prenant certains "
                "médicaments comme le méthotrexate ou des anticonvulsivants.</p>"
                "<p>Ce guide est éducatif et ne remplace pas l'avis d'un professionnel de santé.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="Qu'est-ce que le folate (Vitamine B9) ?",
            body_html=(
                "<p><strong>Folate</strong> est le terme générique pour la forme naturelle de la vitamine "
                "B9 présente dans les aliments. Il joue un rôle critique dans la synthèse de l'ADN et de "
                "l'ARN, le métabolisme des acides aminés et la production de globules rouges et blancs "
                "dans la moelle osseuse.</p>"
                "<p>Le corps peut maintenir des réserves de folate pendant environ 3–4 mois. La forme "
                "active est le <em>tétrahydrofolate (THF)</em>. La mesure sanguine est rapportée en "
                "folate sérique ou folate érythrocytaire (RBC) — ce dernier reflète mieux le statut "
                "à long terme.</p>"
                "<p>La carence se manifeste surtout dans les tissus à renouvellement cellulaire rapide "
                "(moelle osseuse, muqueuse gastro-intestinale) et élève l'homocystéine sérique, "
                "associée indépendamment au risque cardiovasculaire.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="Folate vs. acide folique : quelle différence ?",
            body_html=(
                "<p><strong>Folate</strong> désigne la forme naturelle dans les aliments. "
                "<strong>Acide folique</strong> est la forme synthétique utilisée dans les aliments "
                "enrichis et les compléments alimentaires.</p>"
                "<p>L'acide folique nécessite une réduction enzymatique en deux étapes par la "
                "<em>dihydrofolate réductase (DHFR)</em>. À forte dose, de l'acide folique non "
                "métabolisé peut circuler dans le sang. Le folate naturel est converti plus directement "
                "en formes actives (5-méthyl-THF).</p>"
                "<p>Les porteurs du polymorphisme MTHFR (variante C677T) peuvent bénéficier d'une "
                "supplémentation en <em>méthylfolate (5-MTHF)</em>. La fortification obligatoire a "
                "considérablement réduit les anomalies du tube neural dans de nombreux pays.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de folate",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Test</th>'
                f'<th {_TH}>Plage normale</th>'
                f'<th {_TH}>Unité</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Folate sérique</td>'
                f'<td {_TD}>2,7 – 17,0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>Folate érythrocytaire (RBC)</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'</tbody></table>'
                "<p>Le <strong>folate sérique</strong> reflète l'apport récent. Le <strong>folate "
                "érythrocytaire</strong> montre le statut des 2–3 derniers mois.</p>"
                "<p>Un folate sérique &lt; 2,7 ng/mL suggère une carence. L'homocystéine élevée est "
                "un marqueur indirect ; l'acide méthylmalonique (MMA) est normal en carence de folate "
                "mais élevé en carence de B12.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="Causes d'un folate bas",
            body_html=(
                "<p><strong>Apport alimentaire insuffisant :</strong> Cause la plus fréquente. La cuisson "
                "(surtout l'ébullition) détruit 50–90% du folate.</p>"
                "<p><strong>Malabsorption :</strong> Maladie cœliaque, maladie de Crohn, syndrome de "
                "l'intestin court et sprue tropicale altèrent l'absorption dans le jéjunum.</p>"
                "<p><strong>Alcoolisme :</strong> L'alcool réduit l'absorption, altère le métabolisme "
                "hépatique et augmente la perte rénale de folate.</p>"
                "<p><strong>Médicaments :</strong> Méthotrexate, anticonvulsivants (phénytoïne, "
                "carbamazépine, acide valproïque), triméthoprime-sulfaméthoxazole, contraceptifs oraux. "
                "<strong>Demande accrue :</strong> Grossesse, allaitement, anémie hémolytique, dialyse "
                "chronique, cancers.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="Folate et anémie mégaloblastique",
            body_html=(
                "<p>La carence en folate est une cause majeure d'<strong>anémie mégaloblastique</strong>. "
                "La synthèse d'ADN altérée dans la moelle osseuse produit des globules rouges "
                "anormalement grands (macrocytaires).</p>"
                "<p>L'hémogramme montre un <strong>VGM élevé (&gt; 100 fL)</strong>, une hémoglobine "
                "basse et des <em>neutrophiles hypersegmentés</em>. En cas avancé : pancytopénie.</p>"
                "<p>Il est crucial de distinguer de la carence en B12, qui cause en plus des lésions "
                "neurologiques irréversibles. Le traitement par folate seul peut masquer la carence "
                "en B12. Les deux vitamines doivent être évaluées conjointement.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="Folate et grossesse",
            body_html=(
                "<p>Le folate est l'une des vitamines les plus critiques pendant la grossesse. La "
                "fermeture du tube neural se produit dans les 28 premiers jours après la conception. "
                "Des niveaux adéquats réduisent significativement le risque d'<strong>anomalies du "
                "tube neural (ATN)</strong> comme le spina bifida et l'anencéphalie.</p>"
                "<p>L'OMS recommande <strong>400 µg d'acide folique par jour</strong>, au moins 1 mois "
                "avant la conception jusqu'à la 12e semaine de grossesse. En cas d'antécédent "
                "d'ATN : <strong>4 mg/jour</strong>.</p>"
                "<p>Pendant la grossesse, les besoins en folate augmentent de 5 à 10 fois. L'apport "
                "insuffisant augmente les risques d'ATN, de faible poids de naissance et d'anémie "
                "gravidique. La fortification a réduit l'incidence des ATN de 20–50%.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Sources alimentaires de folate",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Aliment</th>'
                f'<th {_TH}>Portion</th>'
                f'<th {_TH}>Folate (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Foie de bœuf (cuit)</td>'
                f'<td {_TD}>85 g</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>Épinards (cuits)</td>'
                f'<td {_TD}>½ tasse</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>Haricots noirs (cuits)</td>'
                f'<td {_TD}>½ tasse</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>Asperges (cuites)</td>'
                f'<td {_TD}>4 tiges</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>Avocat</td>'
                f'<td {_TD}>½ fruit</td>'
                f'<td {_TD}>~59</td></tr>'
                f'</tbody></table>'
                "<p>La cuisson à la vapeur préserve mieux le folate que l'ébullition. Les légumes et "
                "fruits frais offrent les niveaux les plus élevés.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin",
            body_html=(
                "<p><strong>Symptômes d'anémie :</strong> Fatigue persistante, faiblesse, pâleur, "
                "essoufflement, palpitations, vertiges. <strong>Symptômes neurologiques :</strong> "
                "Difficultés de concentration, troubles de la mémoire, dépression.</p>"
                "<p><strong>Projet de grossesse :</strong> Commencez l'acide folique au moins 1 mois "
                "avant la conception.</p>"
                "<p><strong>Maladies de malabsorption :</strong> Surveillance régulière du folate en cas "
                "de maladie cœliaque, Crohn, méthotrexate ou anticonvulsivants.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre vos résultats",
            body_html=(
                "<p>Téléchargez votre bilan sanguin sur <a href=\"/analyze\">Norya</a> et recevez en "
                "minutes un résumé structuré de votre folate, B12, hémoglobine, VGM et biomarqueurs "
                "associés. Norya compare vos valeurs aux plages de référence et génère un rapport "
                "clair pour votre consultation.</p>"
                "<p>Norya ne diagnostique pas et ne recommande aucun traitement. "
                "<a href=\"/analyze\">Commencez votre analyse maintenant</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# ITALIAN
# ─────────────────────────────────────────────────────────────────────
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Folato (Vitamina B9): cosa significa un folato basso?",
            body_html=(
                "<p>Il <strong>folato (vitamina B9)</strong> è una vitamina idrosolubile essenziale per "
                "la sintesi del DNA, la divisione cellulare e la formazione dei globuli rossi. Un livello "
                "basso di folato nel sangue può indicare una carenza che porta ad anemia, compromissione "
                "immunitaria e, in gravidanza, gravi difetti congeniti.</p>"
                "<p>La carenza di folato colpisce in particolare le donne in gravidanza, gli anziani, "
                "i pazienti con disturbi da malassorbimento, gli alcolisti e chi assume farmaci come "
                "metotrexato o anticonvulsivanti.</p>"
                "<p>Questa guida è a scopo educativo e non sostituisce il parere medico.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="Cos'è il folato (Vitamina B9)?",
            body_html=(
                "<p><strong>Folato</strong> è il termine generico per la forma naturale della vitamina B9 "
                "presente negli alimenti. Svolge ruoli critici nella sintesi di DNA e RNA, nel metabolismo "
                "degli aminoacidi e nella produzione di globuli rossi e bianchi nel midollo osseo.</p>"
                "<p>L'organismo mantiene riserve di folato per circa 3–4 mesi. La forma attiva è il "
                "<em>tetraidrofolato (THF)</em>. Nel sangue si misura il folato sierico o eritrocitario "
                "(RBC) — quest'ultimo riflette meglio lo stato a lungo termine.</p>"
                "<p>La carenza si manifesta soprattutto nei tessuti con rapido turnover cellulare (midollo "
                "osseo, mucosa gastrointestinale) e aumenta l'omocisteina sierica, associata al rischio "
                "cardiovascolare.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="Folato vs. acido folico: qual è la differenza?",
            body_html=(
                "<p><strong>Folato</strong> è la forma naturale negli alimenti. <strong>Acido folico</strong> "
                "è la forma sintetica in alimenti fortificati e integratori.</p>"
                "<p>L'acido folico richiede una riduzione enzimatica in due fasi dalla <em>diidrofolato "
                "reduttasi (DHFR)</em>. A dosi elevate, può circolare acido folico non metabolizzato. "
                "Il folato naturale si converte più direttamente in forme attive (5-metil-THF).</p>"
                "<p>I portatori del polimorfismo MTHFR (variante C677T) possono beneficiare della "
                "supplementazione con <em>metilfolato (5-MTHF)</em>. La fortificazione obbligatoria "
                "ha ridotto significativamente i difetti del tubo neurale.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di folato",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Test</th>'
                f'<th {_TH}>Range normale</th>'
                f'<th {_TH}>Unità</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Folato sierico</td>'
                f'<td {_TD}>2,7 – 17,0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>Folato eritrocitario (RBC)</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'</tbody></table>'
                "<p>Il <strong>folato sierico</strong> riflette l'assunzione recente. Il <strong>folato "
                "eritrocitario</strong> mostra lo stato degli ultimi 2–3 mesi ed è più affidabile.</p>"
                "<p>Un folato sierico &lt; 2,7 ng/mL suggerisce carenza. L'omocisteina elevata è un "
                "marcatore indiretto; l'acido metilmalonico (MMA) è normale nella carenza di folato "
                "ma elevato in quella di B12.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="Cause di folato basso",
            body_html=(
                "<p><strong>Apporto dietetico insufficiente:</strong> Causa più frequente. La cottura "
                "(soprattutto la bollitura) distrugge fino al 50–90% del folato.</p>"
                "<p><strong>Malassorbimento:</strong> Celiachia, morbo di Crohn, sindrome dell'intestino "
                "corto e sprue tropicale compromettono l'assorbimento nel digiuno.</p>"
                "<p><strong>Alcolismo:</strong> L'alcol riduce l'assorbimento, altera il metabolismo "
                "epatico e aumenta la perdita renale di folato.</p>"
                "<p><strong>Farmaci:</strong> Metotrexato, anticonvulsivanti (fenitoina, carbamazepina), "
                "trimetoprim-sulfametossazolo, contraccettivi orali. <strong>Maggiore fabbisogno:</strong> "
                "Gravidanza, allattamento, anemia emolitica, dialisi cronica, neoplasie.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="Folato e anemia megaloblastica",
            body_html=(
                "<p>La carenza di folato è una causa principale di <strong>anemia megaloblastica</strong>. "
                "La sintesi alterata del DNA nel midollo osseo produce eritrociti anormalmente grandi "
                "(macrocitici).</p>"
                "<p>L'emocromo mostra <strong>MCV elevato (&gt; 100 fL)</strong>, emoglobina bassa e "
                "<em>neutrofili ipersegmentati</em>. Nei casi avanzati: pancitopenia.</p>"
                "<p>È fondamentale distinguere dalla carenza di B12, che causa anche danni neurologici "
                "irreversibili. Il trattamento con solo folato può mascherare la carenza di B12. Entrambe "
                "le vitamine devono essere valutate insieme.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="Folato e gravidanza",
            body_html=(
                "<p>Il folato è una delle vitamine più critiche in gravidanza. La chiusura del tubo "
                "neurale avviene nei primi 28 giorni dal concepimento. Livelli adeguati riducono "
                "significativamente il rischio di <strong>difetti del tubo neurale (DTN)</strong> come "
                "spina bifida e anencefalia.</p>"
                "<p>L'OMS raccomanda <strong>400 µg di acido folico al giorno</strong>, almeno 1 mese "
                "prima del concepimento fino alla 12ª settimana. Con precedente DTN: "
                "<strong>4 mg/giorno</strong>.</p>"
                "<p>In gravidanza il fabbisogno di folato aumenta 5–10 volte. L'apporto insufficiente "
                "aumenta i rischi di DTN, basso peso alla nascita, parto pretermine e anemia gravidica. "
                "La fortificazione obbligatoria ha ridotto l'incidenza di DTN del 20–50%.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Fonti alimentari di folato",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Alimento</th>'
                f'<th {_TH}>Porzione</th>'
                f'<th {_TH}>Folato (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Fegato di manzo (cotto)</td>'
                f'<td {_TD}>85 g</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>Spinaci (cotti)</td>'
                f'<td {_TD}>½ tazza</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>Fagioli neri (cotti)</td>'
                f'<td {_TD}>½ tazza</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>Asparagi (cotti)</td>'
                f'<td {_TD}>4 punte</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>Avocado</td>'
                f'<td {_TD}>½ frutto</td>'
                f'<td {_TD}>~59</td></tr>'
                f'</tbody></table>'
                "<p>La cottura a vapore preserva più folato della bollitura. Verdura e frutta fresca "
                "offrono i livelli più alti.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico",
            body_html=(
                "<p><strong>Sintomi di anemia:</strong> Stanchezza persistente, debolezza, pallore, "
                "dispnea, palpitazioni, vertigini. <strong>Sintomi neurologici:</strong> Difficoltà di "
                "concentrazione, problemi di memoria, depressione, irritabilità.</p>"
                "<p><strong>Se pianifichi una gravidanza:</strong> Inizia l'acido folico almeno 1 mese "
                "prima del concepimento.</p>"
                "<p><strong>Malattie da malassorbimento:</strong> Monitoraggio regolare del folato in "
                "caso di celiachia, Crohn, metotrexato o anticonvulsivanti.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a capire i tuoi risultati",
            body_html=(
                "<p>Carica il tuo referto su <a href=\"/analyze\">Norya</a> e ricevi in minuti un "
                "riepilogo strutturato di folato, B12, emoglobina, MCV e biomarcatori correlati. Norya "
                "confronta i tuoi valori con gli intervalli di riferimento e genera un report chiaro "
                "per la tua visita medica.</p>"
                "<p>Norya non diagnostica né raccomanda trattamenti. "
                "<a href=\"/analyze\">Inizia l'analisi ora</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="פולאט (ויטמין B9): מה המשמעות של פולאט נמוך?",
            body_html=(
                "<p><strong>פולאט (ויטמין B9)</strong> הוא ויטמין מסיס במים החיוני לסינתזת DNA, "
                "חלוקת תאים ויצירת כדוריות דם אדומות. כאשר בדיקת הדם מראה פולאט נמוך, ייתכן "
                "שלגופך חסר מרכיב תזונתי קריטי זה, מה שעלול להוביל לאנמיה, פגיעה חיסונית ובהריון — "
                "למומים מולדים חמורים.</p>"
                "<p>מחסור בפולאט נפוץ במיוחד בנשים בהריון, קשישים, אנשים עם הפרעות ספיגה, "
                "אלכוהוליסטים ומשתמשי תרופות כמו מתוטרקסט או נוגדי פרכוסים.</p>"
                "<p>מדריך זה חינוכי בלבד ואינו מחליף ייעוץ רפואי מקצועי.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="מהו פולאט (ויטמין B9)?",
            body_html=(
                "<p><strong>פולאט</strong> הוא השם הכללי לצורה הטבעית של ויטמין B9 במזון. הוא ממלא "
                "תפקידים קריטיים בסינתזת DNA ו-RNA, מטבוליזם חומצות אמינו (המרת הומוציסטאין "
                "למתיונין) ובייצור כדוריות דם אדומות ולבנות במח העצם.</p>"
                "<p>הגוף שומר מאגרי פולאט לכ-3–4 חודשים. הצורה הפעילה היא <em>טטראהידרופולאט "
                "(THF)</em>. במדידת דם מדווח פולאט סרום או פולאט אריתרוציטרי (RBC) — האחרון "
                "מדויק יותר להערכה ארוכת טווח.</p>"
                "<p>מחסור מתבטא בעיקר ברקמות עם חלוקת תאים מהירה (מח עצם, רירית מערכת העיכול) "
                "ומעלה הומוציסטאין, הקשור עצמאית לסיכון קרדיווסקולרי.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="פולאט מול חומצה פולית: מה ההבדל?",
            body_html=(
                "<p><strong>פולאט</strong> — הצורה הטבעית במזון. <strong>חומצה פולית</strong> — הצורה "
                "הסינתטית במזונות מועשרים ותוספי תזונה.</p>"
                "<p>חומצה פולית דורשת הפעלה אנזימטית דו-שלבית על ידי <em>דיהידרופולאט רדוקטאז "
                "(DHFR)</em>. במינונים גבוהים עלולה להסתובב בדם חומצה פולית שלא עברה מטבוליזם. "
                "פולאט טבעי מומר ישירות יותר לצורות פעילות (5-מתיל-THF).</p>"
                "<p>נשאי פולימורפיזם MTHFR (וריאנט C677T) עשויים להפיק תועלת מתוספת <em>מתילפולאט "
                "(5-MTHF)</em>. העשרת קמח חובה הפחיתה משמעותית מומי צינור עצבי.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי פולאט תקינים",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>בדיקה</th>'
                f'<th {_TH}>טווח תקין</th>'
                f'<th {_TH}>יחידה</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>פולאט סרום</td>'
                f'<td {_TD}>2.7 – 17.0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>פולאט אריתרוציטרי (RBC)</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'</tbody></table>'
                "<p><strong>פולאט סרום</strong> משקף צריכה אחרונה. <strong>פולאט אריתרוציטרי</strong> "
                "משקף מצב ב-2–3 החודשים האחרונים ואמין יותר.</p>"
                "<p>פולאט סרום &lt; 2.7 ng/mL מרמז על מחסור. הומוציסטאין מוגבר הוא סמן עקיף; MMA "
                "תקין במחסור פולאט אך מוגבר במחסור B12.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="גורמים לפולאט נמוך",
            body_html=(
                "<p><strong>צריכה תזונתית לקויה:</strong> הגורם השכיח ביותר. בישול (במיוחד הרתחה) "
                "הורס עד 50–90% מהפולאט.</p>"
                "<p><strong>תת-ספיגה:</strong> צליאק, מחלת קרוהן, תסמונת מעי קצר וספרו טרופי "
                "פוגעים בספיגה בג'חנון.</p>"
                "<p><strong>אלכוהוליזם:</strong> אלכוהול מפחית ספיגה, פוגע במטבוליזם כבדי ומגביר "
                "איבוד כלייתי של פולאט.</p>"
                "<p><strong>תרופות:</strong> מתוטרקסט, נוגדי פרכוסים (פניטואין, קרבמזפין), "
                "טרימתופרים-סולפמתוקסזול, גלולות למניעת הריון. <strong>ביקוש מוגבר:</strong> "
                "הריון, הנקה, אנמיה המוליטית, דיאליזה כרונית, ממאירויות.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="מחסור פולאט ואנמיה מגלובלסטית",
            body_html=(
                "<p>מחסור פולאט הוא גורם עיקרי ל<strong>אנמיה מגלובלסטית</strong>. סינתזת DNA "
                "לקויה במח העצם מייצרת כדוריות אדומות גדולות מהרגיל (מקרוציטיות).</p>"
                "<p>ספירת הדם מראה <strong>MCV מוגבר (&gt; 100 fL)</strong>, המוגלובין נמוך "
                "ו<em>נויטרופילים היפרסגמנטליים</em>. במקרים מתקדמים: פנציטופניה.</p>"
                "<p>חיוני להבדיל ממחסור B12, הגורם גם לנזק נוירולוגי בלתי הפיך. טיפול בפולאט "
                "בלבד עלול להסוות מחסור B12. שני הוויטמינים חייבים להיבדק יחד.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="פולאט והריון",
            body_html=(
                "<p>פולאט הוא אחד הוויטמינים הקריטיים ביותר בהריון. סגירת הצינור העצבי מתרחשת "
                "ב-28 הימים הראשונים אחרי ההפריה. רמות מספקות מפחיתות משמעותית את הסיכון "
                "ל<strong>מומי צינור עצבי (NTD)</strong> כמו ספינה ביפידה ואננצפליה.</p>"
                "<p>WHO ממליץ על <strong>400 מיקרוגרם חומצה פולית ליום</strong>, לפחות חודש לפני "
                "ההתעברות ועד שבוע 12. עם היסטוריה של NTD: <strong>4 מ\"ג/יום</strong>.</p>"
                "<p>בהריון, הצורך בפולאט גדל פי 5–10. צריכה לא מספקת מגדילה סיכון ל-NTD, "
                "משקל לידה נמוך, לידה מוקדמת ואנמיה הריונית. העשרת קמח חובה הפחיתה NTD ב-20–50%.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="מקורות תזונתיים של פולאט",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>מזון</th>'
                f'<th {_TH}>מנה</th>'
                f'<th {_TH}>פולאט (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>כבד בקר (מבושל)</td>'
                f'<td {_TD}>85 גרם</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>תרד (מבושל)</td>'
                f'<td {_TD}>½ כוס</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>שעועית שחורה (מבושלת)</td>'
                f'<td {_TD}>½ כוס</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>אספרגוס (מבושל)</td>'
                f'<td {_TD}>4 ענפים</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>אבוקדו</td>'
                f'<td {_TD}>½ פרי</td>'
                f'<td {_TD}>~59</td></tr>'
                f'</tbody></table>'
                "<p>אידוי שומר על יותר פולאט מהרתחה. ירקות ופירות טריים מספקים את הרמות "
                "הגבוהות ביותר.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא",
            body_html=(
                "<p><strong>תסמיני אנמיה:</strong> עייפות מתמשכת, חולשה, חיוורון, קוצר נשימה, "
                "דפיקות לב, סחרחורת. <strong>תסמינים נוירולוגיים:</strong> קשיי ריכוז, בעיות "
                "זיכרון, דיכאון, עצבנות.</p>"
                "<p><strong>מתכננים הריון:</strong> התחילו חומצה פולית לפחות חודש לפני ההתעברות.</p>"
                "<p><strong>מחלות תת-ספיגה:</strong> מעקב סדיר של פולאט בצליאק, קרוהן, מתוטרקסט "
                "או נוגדי פרכוסים.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד Norya עוזרת לכם להבין את התוצאות",
            body_html=(
                "<p>העלו את תוצאות בדיקת הדם ל<a href=\"/analyze\">Norya</a> וקבלו תוך דקות סיכום "
                "מובנה של פולאט, B12, המוגלובין, MCV וסמנים נלווים. Norya משווה את הערכים שלכם "
                "לטווחי הייחוס ומייצרת דוח ברור להכנה לביקור אצל הרופא.</p>"
                "<p>Norya אינה מאבחנת ואינה ממליצה על טיפול. "
                "<a href=\"/analyze\">התחילו את הניתוח עכשיו</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="फोलेट (विटामिन B9): कम फोलेट का क्या मतलब है?",
            body_html=(
                "<p><strong>फोलेट (विटामिन B9)</strong> एक पानी में घुलनशील B विटामिन है जो DNA "
                "संश्लेषण, कोशिका विभाजन और लाल रक्त कोशिकाओं के निर्माण के लिए आवश्यक है। "
                "जब आपकी रक्त जांच में फोलेट कम आता है, तो इसका मतलब हो सकता है कि आपके शरीर "
                "में इस महत्वपूर्ण पोषक तत्व की कमी है, जो एनीमिया, प्रतिरक्षा हानि और "
                "गर्भावस्था में गंभीर जन्म दोषों का कारण बन सकती है।</p>"
                "<p>फोलेट की कमी विशेष रूप से गर्भवती महिलाओं, बुजुर्गों, मैलएब्सॉर्प्शन विकारों "
                "वाले रोगियों, शराब पीने वालों और मेथोट्रेक्सेट या एंटीकॉन्वल्सेंट जैसी दवाएं "
                "लेने वालों को प्रभावित करती है।</p>"
                "<p>यह गाइड शैक्षिक है और पेशेवर चिकित्सा सलाह का विकल्प नहीं है।</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="फोलेट (विटामिन B9) क्या है?",
            body_html=(
                "<p><strong>फोलेट</strong> खाद्य पदार्थों में प्राकृतिक रूप से पाए जाने वाले विटामिन "
                "B9 का सामान्य नाम है। यह DNA और RNA संश्लेषण, अमीनो एसिड मेटाबॉलिज़्म "
                "(होमोसिस्टीन-मेथियोनीन रूपांतरण) और अस्थि मज्जा में लाल और सफेद रक्त कोशिकाओं "
                "के उत्पादन में महत्वपूर्ण भूमिका निभाता है।</p>"
                "<p>शरीर लगभग 3–4 महीने तक फोलेट भंडार बनाए रख सकता है। सक्रिय रूप "
                "<em>टेट्राहाइड्रोफोलेट (THF)</em> है। रक्त में सीरम फोलेट या RBC फोलेट मापा "
                "जाता है — RBC फोलेट दीर्घकालिक मूल्यांकन के लिए अधिक विश्वसनीय है।</p>"
                "<p>कमी तेज़ कोशिका विभाजन वाले ऊतकों (अस्थि मज्जा, जठरांत्र श्लेष्मा) में "
                "सबसे स्पष्ट होती है और सीरम होमोसिस्टीन बढ़ाती है, जो कार्डियोवैस्कुलर "
                "जोखिम से स्वतंत्र रूप से जुड़ा है।</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="फोलेट बनाम फोलिक एसिड: क्या अंतर है?",
            body_html=(
                "<p><strong>फोलेट</strong> — खाद्य पदार्थों में प्राकृतिक रूप। <strong>फोलिक "
                "एसिड</strong> — फोर्टिफाइड खाद्य और सप्लीमेंट में सिंथेटिक रूप।</p>"
                "<p>फोलिक एसिड को सक्रिय होने के लिए <em>डाइहाइड्रोफोलेट रिडक्टेज (DHFR)</em> "
                "द्वारा दो-चरणीय एंजाइमैटिक कमी की आवश्यकता होती है। उच्च खुराक में "
                "अनमेटाबोलाइज़्ड फोलिक एसिड रक्त में प्रसारित हो सकता है। प्राकृतिक फोलेट "
                "सीधे सक्रिय रूपों (5-मिथाइल-THF) में बदलता है।</p>"
                "<p>MTHFR जीन पॉलिमॉर्फिज़्म (C677T वेरिएंट) वाले व्यक्तियों को <em>मिथाइलफोलेट "
                "(5-MTHF)</em> सप्लीमेंटेशन अधिक प्रभावी हो सकता है। कई देशों में आटा और "
                "अनाज उत्पादों की अनिवार्य फोर्टिफिकेशन ने न्यूरल ट्यूब दोषों को "
                "काफी कम किया है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य फोलेट स्तर",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>परीक्षण</th>'
                f'<th {_TH}>सामान्य रेंज</th>'
                f'<th {_TH}>इकाई</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>सीरम फोलेट</td>'
                f'<td {_TD}>2.7 – 17.0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>RBC फोलेट</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'</tbody></table>'
                "<p><strong>सीरम फोलेट</strong> हाल की आहार सेवन को दर्शाता है। <strong>RBC "
                "फोलेट</strong> पिछले 2–3 महीनों की स्थिति दिखाता है और दीर्घकालिक मूल्यांकन "
                "के लिए अधिक विश्वसनीय है।</p>"
                "<p>सीरम फोलेट &lt; 2.7 ng/mL कमी का संकेत देता है। बढ़ा हुआ होमोसिस्टीन एक "
                "अप्रत्यक्ष मार्कर है; MMA फोलेट कमी में सामान्य लेकिन B12 कमी में बढ़ा "
                "होता है।</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="कम फोलेट के कारण",
            body_html=(
                "<p><strong>अपर्याप्त आहार सेवन:</strong> सबसे आम कारण। खाना पकाना (विशेष रूप "
                "से उबालना) 50–90% तक फोलेट नष्ट करता है।</p>"
                "<p><strong>मैलएब्सॉर्प्शन:</strong> सीलिएक रोग, क्रोहन रोग, शॉर्ट बाउल "
                "सिंड्रोम जेजुनम में अवशोषण को बाधित करते हैं।</p>"
                "<p><strong>अल्कोहल:</strong> शराब अवशोषण कम करती है, यकृत मेटाबॉलिज़्म को "
                "बाधित करती है और फोलेट का गुर्दे से नुकसान बढ़ाती है।</p>"
                "<p><strong>दवाएं:</strong> मेथोट्रेक्सेट, एंटीकॉन्वल्सेंट (फेनिटोइन, "
                "कार्बमेज़ेपिन), ट्राइमेथोप्रिम-सल्फामेथोक्साज़ोल, ओरल कॉन्ट्रासेप्टिव। "
                "<strong>बढ़ी हुई मांग:</strong> गर्भावस्था, स्तनपान, हेमोलिटिक एनीमिया, "
                "क्रोनिक डायलिसिस, मैलिग्नेंसी।</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="फोलेट की कमी और मेगालोब्लास्टिक एनीमिया",
            body_html=(
                "<p>फोलेट की कमी <strong>मेगालोब्लास्टिक एनीमिया</strong> का प्रमुख कारण है। "
                "अस्थि मज्जा में बाधित DNA संश्लेषण असामान्य रूप से बड़ी (मैक्रोसाइटिक) लाल "
                "रक्त कोशिकाएं उत्पन्न करता है।</p>"
                "<p>CBC में <strong>बढ़ा MCV (&gt; 100 fL)</strong>, कम हीमोग्लोबिन और "
                "<em>हाइपरसेग्मेंटेड न्यूट्रोफिल</em> दिखते हैं। उन्नत मामलों में "
                "पैनसाइटोपेनिया हो सकता है।</p>"
                "<p>B12 कमी से अंतर करना महत्वपूर्ण है, क्योंकि B12 कमी अतिरिक्त अपरिवर्तनीय "
                "न्यूरोलॉजिकल क्षति करती है। केवल फोलेट से उपचार B12 कमी को छुपा सकता है। "
                "दोनों विटामिन हमेशा साथ जांचे जाने चाहिए।</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="फोलेट और गर्भावस्था",
            body_html=(
                "<p>फोलेट गर्भावस्था में सबसे महत्वपूर्ण विटामिनों में से एक है। न्यूरल ट्यूब "
                "क्लोज़र गर्भाधान के पहले 28 दिनों में होता है। पर्याप्त फोलेट स्तर "
                "<strong>न्यूरल ट्यूब दोषों (NTD)</strong> जैसे स्पाइना बिफिडा और एनेन्सेफली "
                "के जोखिम को काफी कम करते हैं।</p>"
                "<p>WHO सभी गर्भधारण की योजना बनाने वाली महिलाओं को प्रतिदिन <strong>400 µg "
                "फोलिक एसिड</strong> की सिफ़ारिश करता है, गर्भाधान से कम से कम 1 महीना पहले "
                "से 12वें सप्ताह तक। NTD इतिहास वाली: <strong>4 mg/दिन</strong>।</p>"
                "<p>गर्भावस्था में फोलेट की मांग 5–10 गुना बढ़ जाती है। अपर्याप्त सेवन से NTD, "
                "कम जन्म वज़न, प्रीमैच्योर डिलीवरी और गर्भावस्था एनीमिया का जोखिम बढ़ता है।</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="फोलेट से भरपूर खाद्य स्रोत",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>खाद्य पदार्थ</th>'
                f'<th {_TH}>मात्रा</th>'
                f'<th {_TH}>फोलेट (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>बीफ लिवर (पका हुआ)</td>'
                f'<td {_TD}>85 ग्राम</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>पालक (पका हुआ)</td>'
                f'<td {_TD}>½ कप</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>काली फलियां (पकी हुई)</td>'
                f'<td {_TD}>½ कप</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>शतावरी (पकी हुई)</td>'
                f'<td {_TD}>4 डंडे</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>एवोकाडो</td>'
                f'<td {_TD}>½ फल</td>'
                f'<td {_TD}>~59</td></tr>'
                f'</tbody></table>'
                "<p>भाप में पकाना उबालने से अधिक फोलेट संरक्षित करता है। ताज़ी सब्जियां और "
                "फल सबसे अधिक फोलेट प्रदान करते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें",
            body_html=(
                "<p><strong>एनीमिया के लक्षण:</strong> लगातार थकान, कमज़ोरी, पीली त्वचा, "
                "सांस फूलना, धड़कन, चक्कर। <strong>न्यूरोलॉजिकल लक्षण:</strong> "
                "एकाग्रता की कठिनाई, स्मृति समस्याएं, अवसाद, चिड़चिड़ापन।</p>"
                "<p><strong>गर्भावस्था की योजना:</strong> गर्भाधान से कम से कम 1 महीने पहले "
                "फोलिक एसिड शुरू करें।</p>"
                "<p><strong>मैलएब्सॉर्प्शन रोग:</strong> सीलिएक, क्रोहन, मेथोट्रेक्सेट या "
                "एंटीकॉन्वल्सेंट उपयोगकर्ताओं में नियमित फोलेट निगरानी।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके परिणामों को समझने में कैसे मदद करता है",
            body_html=(
                "<p>अपनी रक्त परीक्षण रिपोर्ट <a href=\"/analyze\">Norya</a> पर अपलोड करें और "
                "मिनटों में फोलेट, B12, हीमोग्लोबिन, MCV और संबंधित बायोमार्करों का संरचित "
                "सारांश प्राप्त करें। Norya आपके मानों की तुलना संदर्भ सीमाओं से करता है और "
                "डॉक्टर विज़िट की तैयारी के लिए स्पष्ट रिपोर्ट बनाता है।</p>"
                "<p>Norya निदान या उपचार की सिफ़ारिश नहीं करता। "
                "<a href=\"/analyze\">अभी अपना विश्लेषण शुरू करें</a>।</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="الفولات (فيتامين B9): ماذا يعني انخفاض الفولات؟",
            body_html=(
                "<p><strong>الفولات (فيتامين B9)</strong> هو فيتامين قابل للذوبان في الماء وضروري "
                "لتخليق الحمض النووي DNA، انقسام الخلايا وتكوين كريات الدم الحمراء. عندما يُظهر "
                "تحليل الدم انخفاض الفولات، فقد يعني أن جسمك يفتقر إلى هذا المغذي الحيوي، مما قد "
                "يؤدي إلى فقر الدم وضعف المناعة وأثناء الحمل — عيوب خلقية خطيرة.</p>"
                "<p>يصيب نقص الفولات بشكل خاص الحوامل والمسنين والمصابين باضطرابات سوء الامتصاص "
                "والمدمنين على الكحول ومستخدمي أدوية مثل الميثوتريكسات أو مضادات الاختلاج.</p>"
                "<p>هذا الدليل تعليمي ولا يحل محل الاستشارة الطبية المتخصصة.</p>"
            ),
        ),
        Section(
            id="what-is-folate", level=2,
            heading="ما هو الفولات (فيتامين B9)؟",
            body_html=(
                "<p><strong>الفولات</strong> هو الاسم العام للشكل الطبيعي من فيتامين B9 الموجود في "
                "الأغذية. يلعب أدوارًا حاسمة في تخليق DNA و RNA واستقلاب الأحماض الأمينية (تحويل "
                "الهوموسيستين إلى ميثيونين) وإنتاج كريات الدم الحمراء والبيضاء في نخاع العظم.</p>"
                "<p>يحتفظ الجسم بمخزون الفولات لمدة 3–4 أشهر تقريبًا. الشكل النشط هو "
                "<em>تتراهيدروفولات (THF)</em>. في الدم يُقاس فولات المصل أو فولات كريات الدم "
                "الحمراء (RBC) — الأخير يعكس الحالة طويلة الأمد بدقة أكبر.</p>"
                "<p>يظهر النقص بشكل أوضح في الأنسجة ذات الانقسام الخلوي السريع (نخاع العظم، "
                "الغشاء المخاطي المعدي المعوي) ويرفع الهوموسيستين، المرتبط بالخطر القلبي "
                "الوعائي.</p>"
            ),
        ),
        Section(
            id="folate-vs-folic-acid", level=2,
            heading="الفولات مقابل حمض الفوليك: ما الفرق؟",
            body_html=(
                "<p><strong>الفولات</strong> — الشكل الطبيعي في الأغذية. <strong>حمض الفوليك</strong> "
                "— الشكل الصناعي في الأغذية المدعمة والمكملات.</p>"
                "<p>يتطلب حمض الفوليك اختزالًا إنزيميًا بمرحلتين بواسطة <em>ديهيدروفولات ريدكتاز "
                "(DHFR)</em>. بالجرعات العالية قد يدور حمض فوليك غير مُستقلَب في الدم. الفولات "
                "الطبيعي يتحول مباشرةً إلى أشكال نشطة (5-ميثيل-THF).</p>"
                "<p>حاملو تعدد أشكال MTHFR (المتغير C677T) قد يستفيدون من مكملات <em>ميثيلفولات "
                "(5-MTHF)</em>. تدعيم الدقيق الإلزامي خفّض عيوب الأنبوب العصبي بشكل كبير.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدلات الطبيعية للفولات",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>الاختبار</th>'
                f'<th {_TH}>النطاق الطبيعي</th>'
                f'<th {_TH}>الوحدة</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>فولات المصل</td>'
                f'<td {_TD}>2.7 – 17.0</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'<tr><td {_TD}>فولات كريات الدم الحمراء (RBC)</td>'
                f'<td {_TD}>&gt; 140</td>'
                f'<td {_TD}>ng/mL</td></tr>'
                f'</tbody></table>'
                "<p><strong>فولات المصل</strong> يعكس التناول الغذائي الأخير. <strong>فولات RBC</strong> "
                "يُظهر الحالة على مدى 2–3 أشهر وأكثر موثوقية.</p>"
                "<p>فولات المصل &lt; 2.7 ng/mL يشير إلى نقص. الهوموسيستين المرتفع مؤشر غير "
                "مباشر؛ MMA طبيعي في نقص الفولات لكن مرتفع في نقص B12.</p>"
            ),
        ),
        Section(
            id="low-folate-causes", level=2,
            heading="أسباب انخفاض الفولات",
            body_html=(
                "<p><strong>عدم كفاية الغذاء:</strong> السبب الأكثر شيوعًا. الطهي (خاصة السلق) "
                "يدمر 50–90% من الفولات.</p>"
                "<p><strong>سوء الامتصاص:</strong> الداء البطني، داء كرون، متلازمة الأمعاء القصيرة "
                "والذرب الاستوائي يعطلون الامتصاص في الصائم.</p>"
                "<p><strong>إدمان الكحول:</strong> يقلل الامتصاص ويضعف الاستقلاب الكبدي ويزيد "
                "الفقد الكلوي.</p>"
                "<p><strong>الأدوية:</strong> ميثوتريكسات، مضادات الاختلاج (فينيتوين، كاربامازبين)، "
                "تريميثوبريم-سلفاميثوكسازول، حبوب منع الحمل. <strong>زيادة الطلب:</strong> الحمل، "
                "الرضاعة، فقر الدم الانحلالي، الغسيل الكلوي المزمن، الأورام الخبيثة.</p>"
            ),
        ),
        Section(
            id="folate-and-anemia", level=2,
            heading="نقص الفولات وفقر الدم الأرومي الضخم",
            body_html=(
                "<p>نقص الفولات سبب رئيسي ل<strong>فقر الدم الأرومي الضخم (الميغالوبلاستي)</strong>. "
                "ينتج عن تخليق DNA المعطل في نخاع العظم كريات حمراء كبيرة بشكل غير طبيعي "
                "(كبيرة الخلايا).</p>"
                "<p>يُظهر تعداد الدم <strong>MCV مرتفع (&gt; 100 fL)</strong>، هيموغلوبين "
                "منخفض و<em>عدلات مفرطة التقسيم</em>. في الحالات المتقدمة: قلة الكريات الشاملة.</p>"
                "<p>من الضروري التفريق عن نقص B12 الذي يسبب أيضًا تلفًا عصبيًا لا رجعة فيه. "
                "العلاج بالفولات وحده قد يخفي نقص B12. يجب فحص الفيتامينين معًا دائمًا.</p>"
            ),
        ),
        Section(
            id="folate-and-pregnancy", level=2,
            heading="الفولات والحمل",
            body_html=(
                "<p>الفولات من أهم الفيتامينات أثناء الحمل. يحدث انغلاق الأنبوب العصبي في أول "
                "28 يومًا بعد الإخصاب. المستويات الكافية تقلل بشكل كبير خطر <strong>عيوب الأنبوب "
                "العصبي (NTD)</strong> مثل السنسنة المشقوقة وانعدام الدماغ.</p>"
                "<p>توصي منظمة الصحة العالمية بـ <strong>400 ميكروغرام حمض فوليك يوميًا</strong>، "
                "قبل شهر على الأقل من الحمل حتى الأسبوع 12. مع تاريخ NTD: "
                "<strong>4 ملغ/يوم</strong>.</p>"
                "<p>أثناء الحمل تزداد الحاجة للفولات 5–10 أضعاف. النقص يزيد خطر NTD وانخفاض "
                "وزن الولادة والولادة المبكرة وفقر الدم الحملي. التدعيم الإلزامي خفض NTD "
                "بنسبة 20–50%.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="مصادر غذائية للفولات",
            body_html=(
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>الغذاء</th>'
                f'<th {_TH}>الحصة</th>'
                f'<th {_TH}>الفولات (µg)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>كبد البقر (مطبوخ)</td>'
                f'<td {_TD}>85 غ</td>'
                f'<td {_TD}>~215</td></tr>'
                f'<tr><td {_TD}>السبانخ (مطبوخ)</td>'
                f'<td {_TD}>½ كوب</td>'
                f'<td {_TD}>~131</td></tr>'
                f'<tr><td {_TD}>الفاصوليا السوداء (مطبوخة)</td>'
                f'<td {_TD}>½ كوب</td>'
                f'<td {_TD}>~128</td></tr>'
                f'<tr><td {_TD}>الهليون (مطبوخ)</td>'
                f'<td {_TD}>4 أعواد</td>'
                f'<td {_TD}>~89</td></tr>'
                f'<tr><td {_TD}>الأفوكادو</td>'
                f'<td {_TD}>½ ثمرة</td>'
                f'<td {_TD}>~59</td></tr>'
                f'</tbody></table>'
                "<p>الطهي بالبخار يحافظ على فولات أكثر من السلق. الخضروات والفواكه الطازجة "
                "توفر أعلى المستويات.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب",
            body_html=(
                "<p><strong>أعراض فقر الدم:</strong> إرهاق مستمر، ضعف، شحوب، ضيق تنفس، "
                "خفقان، دوخة. <strong>أعراض عصبية:</strong> صعوبة التركيز، مشاكل الذاكرة، "
                "اكتئاب، سرعة الانفعال.</p>"
                "<p><strong>التخطيط للحمل:</strong> ابدئي بحمض الفوليك قبل شهر على الأقل من "
                "الحمل.</p>"
                "<p><strong>أمراض سوء الامتصاص:</strong> مراقبة منتظمة للفولات في الداء البطني، "
                "كرون، الميثوتريكسات أو مضادات الاختلاج.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم نتائجك",
            body_html=(
                "<p>ارفع تقرير تحليل الدم على <a href=\"/analyze\">Norya</a> واحصل خلال دقائق على "
                "ملخص منظم للفولات و B12 والهيموغلوبين و MCV والمؤشرات الحيوية المرتبطة. تقارن "
                "Norya قيمك بالنطاقات المرجعية وتبرز الشذوذات وتنشئ تقريرًا صحيًا واضحًا.</p>"
                "<p>Norya لا تشخّص ولا توصي بعلاج. "
                "<a href=\"/analyze\">ابدأ تحليلك الآن</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_folate_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_folate_faq_schema_qa() -> dict:
    return {
        "tr": [
            {"question": "Folat (vitamin B9) ne işe yarar?",
             "answer": "Folat, DNA sentezi, hücre bölünmesi ve kırmızı kan hücresi üretimi için gerekli olan temel bir B vitaminidir. Ayrıca homosistein metabolizmasında ve nörotransmitter sentezinde rol oynar."},
            {"question": "Normal folat değeri nedir?",
             "answer": "Serum folat için normal aralık 2,7–17,0 ng/mL'dir. Eritrosit (RBC) folat > 140 ng/mL olmalıdır. RBC folat, uzun vadeli durumu daha iyi yansıtır."},
            {"question": "Folat ile folik asit arasındaki fark nedir?",
             "answer": "Folat, gıdalarda doğal olarak bulunan B9 formudur. Folik asit, zenginleştirilmiş gıdalarda ve takviyelerde kullanılan sentetik formdur. İkisi de aynı vitaminin farklı formlarıdır."},
            {"question": "Gebelikte neden folat önemlidir?",
             "answer": "Yeterli folat, nöral tüp defektlerini (spina bifida, anensefali) önlemeye yardımcı olur. Gebe kalmayı planlayan kadınlara konsepsiyondan 1 ay önce başlayarak günde 400 µg folik asit önerilir."},
            {"question": "Folat eksikliğinin belirtileri nelerdir?",
             "answer": "Megaloblastik anemi (yorgunluk, soluk cilt, nefes darlığı), yüksek MCV, glossit, ağız yaraları, konsantrasyon güçlüğü ve depresyon görülebilir."},
        ],
        "en": [
            {"question": "What is folate (vitamin B9) used for?",
             "answer": "Folate is essential for DNA synthesis, cell division, and red blood cell production. It also plays a role in homocysteine metabolism and neurotransmitter synthesis."},
            {"question": "What is a normal folate level?",
             "answer": "Normal serum folate is 2.7–17.0 ng/mL. RBC folate should be > 140 ng/mL. RBC folate better reflects long-term status."},
            {"question": "What is the difference between folate and folic acid?",
             "answer": "Folate is the natural form of vitamin B9 found in foods. Folic acid is the synthetic form used in supplements and fortified foods. Both serve the same function but are metabolized differently."},
            {"question": "Why is folate important during pregnancy?",
             "answer": "Adequate folate prevents neural tube defects (spina bifida, anencephaly). Women planning pregnancy should take 400 µg folic acid daily, starting at least 1 month before conception."},
            {"question": "What are the symptoms of folate deficiency?",
             "answer": "Megaloblastic anemia (fatigue, pale skin, shortness of breath), elevated MCV, glossitis, mouth ulcers, difficulty concentrating, and depression."},
        ],
        "es": [
            {"question": "¿Para qué sirve el folato (vitamina B9)?",
             "answer": "El folato es esencial para la síntesis de ADN, la división celular y la producción de glóbulos rojos. También participa en el metabolismo de la homocisteína."},
            {"question": "¿Cuál es el nivel normal de folato?",
             "answer": "Folato sérico normal: 2,7–17,0 ng/mL. Folato eritrocitario (RBC): > 140 ng/mL."},
            {"question": "¿Cuál es la diferencia entre folato y ácido fólico?",
             "answer": "El folato es la forma natural en los alimentos; el ácido fólico es la forma sintética en suplementos y alimentos fortificados."},
            {"question": "¿Por qué el folato es importante en el embarazo?",
             "answer": "Previene defectos del tubo neural. Se recomiendan 400 µg de ácido fólico al día, 1 mes antes de la concepción."},
        ],
        "de": [
            {"question": "Wofür wird Folat (Vitamin B9) benötigt?",
             "answer": "Folat ist essentiell für die DNA-Synthese, Zellteilung und Bildung roter Blutkörperchen sowie den Homocystein-Stoffwechsel."},
            {"question": "Was ist ein normaler Folatspiegel?",
             "answer": "Serumfolat: 2,7–17,0 ng/mL. Erythrozytenfolat (RBC): > 140 ng/mL."},
            {"question": "Was ist der Unterschied zwischen Folat und Folsäure?",
             "answer": "Folat ist die natürliche Form in Lebensmitteln; Folsäure ist die synthetische Form in Nahrungsergänzungsmitteln und angereicherten Lebensmitteln."},
            {"question": "Warum ist Folat in der Schwangerschaft wichtig?",
             "answer": "Ausreichend Folat beugt Neuralrohrdefekten vor. 400 µg Folsäure täglich, mindestens 1 Monat vor der Empfängnis."},
        ],
        "fr": [
            {"question": "À quoi sert le folate (vitamine B9) ?",
             "answer": "Le folate est essentiel pour la synthèse de l'ADN, la division cellulaire et la production de globules rouges ainsi que le métabolisme de l'homocystéine."},
            {"question": "Quel est le niveau normal de folate ?",
             "answer": "Folate sérique : 2,7–17,0 ng/mL. Folate érythrocytaire (RBC) : > 140 ng/mL."},
            {"question": "Quelle est la différence entre folate et acide folique ?",
             "answer": "Le folate est la forme naturelle dans les aliments ; l'acide folique est la forme synthétique dans les suppléments et aliments enrichis."},
            {"question": "Pourquoi le folate est-il important pendant la grossesse ?",
             "answer": "Il prévient les anomalies du tube neural. 400 µg d'acide folique/jour recommandés, 1 mois avant la conception."},
        ],
        "it": [
            {"question": "A cosa serve il folato (vitamina B9)?",
             "answer": "Il folato è essenziale per la sintesi del DNA, la divisione cellulare e la produzione di globuli rossi, oltre che per il metabolismo dell'omocisteina."},
            {"question": "Qual è il livello normale di folato?",
             "answer": "Folato sierico: 2,7–17,0 ng/mL. Folato eritrocitario (RBC): > 140 ng/mL."},
            {"question": "Qual è la differenza tra folato e acido folico?",
             "answer": "Il folato è la forma naturale negli alimenti; l'acido folico è la forma sintetica negli integratori e negli alimenti fortificati."},
            {"question": "Perché il folato è importante in gravidanza?",
             "answer": "Previene i difetti del tubo neurale. Si raccomandano 400 µg di acido folico/giorno, 1 mese prima del concepimento."},
        ],
        "he": [
            {"question": "לשם מה משמש פולאט (ויטמין B9)?",
             "answer": "פולאט חיוני לסינתזת DNA, חלוקת תאים וייצור כדוריות דם אדומות, וכן למטבוליזם הומוציסטאין."},
            {"question": "מהו רמת הפולאט התקינה?",
             "answer": "פולאט סרום: 2.7–17.0 ng/mL. פולאט RBC: > 140 ng/mL."},
            {"question": "מה ההבדל בין פולאט לחומצה פולית?",
             "answer": "פולאט הוא הצורה הטבעית במזון; חומצה פולית היא הצורה הסינתטית בתוספים ובמזונות מועשרים."},
            {"question": "למה פולאט חשוב בהריון?",
             "answer": "מונע מומי צינור עצבי. מומלצים 400 מיקרוגרם חומצה פולית ליום, חודש לפני ההתעברות."},
        ],
        "hi": [
            {"question": "फोलेट (विटामिन B9) किसके लिए उपयोग होता है?",
             "answer": "फोलेट DNA संश्लेषण, कोशिका विभाजन और लाल रक्त कोशिका उत्पादन के साथ-साथ होमोसिस्टीन मेटाबॉलिज़्म के लिए आवश्यक है।"},
            {"question": "सामान्य फोलेट स्तर क्या है?",
             "answer": "सीरम फोलेट: 2.7–17.0 ng/mL। RBC फोलेट: > 140 ng/mL।"},
            {"question": "फोलेट और फोलिक एसिड में क्या अंतर है?",
             "answer": "फोलेट खाद्य पदार्थों में प्राकृतिक रूप है; फोलिक एसिड सप्लीमेंट और फोर्टिफाइड खाद्य में सिंथेटिक रूप है।"},
            {"question": "गर्भावस्था में फोलेट क्यों महत्वपूर्ण है?",
             "answer": "यह न्यूरल ट्यूब दोषों को रोकता है। गर्भाधान से 1 महीने पहले से 400 µg फोलिक एसिड प्रतिदिन अनुशंसित है।"},
        ],
        "ar": [
            {"question": "ما فائدة الفولات (فيتامين B9)؟",
             "answer": "الفولات ضروري لتخليق DNA، انقسام الخلايا وإنتاج كريات الدم الحمراء، بالإضافة إلى استقلاب الهوموسيستين."},
            {"question": "ما هو المستوى الطبيعي للفولات؟",
             "answer": "فولات المصل: 2.7–17.0 ng/mL. فولات RBC: > 140 ng/mL."},
            {"question": "ما الفرق بين الفولات وحمض الفوليك؟",
             "answer": "الفولات هو الشكل الطبيعي في الأغذية؛ حمض الفوليك هو الشكل الصناعي في المكملات والأغذية المدعمة."},
            {"question": "لماذا الفولات مهم أثناء الحمل؟",
             "answer": "يمنع عيوب الأنبوب العصبي. يُنصح بـ 400 ميكروغرام حمض فوليك يومياً قبل شهر من الحمل."},
        ],
    }
