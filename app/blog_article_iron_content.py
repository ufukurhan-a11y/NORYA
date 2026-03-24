# -*- coding: utf-8 -*-
"""
Iron blood test blog article — full body content for all 9 languages.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_TABLE_STYLE = (
    '<table class="w-full border border-slate-200 text-sm my-4" '
    'style="border-collapse: collapse;">'
)
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
            heading="Serum demir kan testi: Düşük veya yüksek çıkarsa ne anlama gelir?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızda <strong>serum demir</strong> değerinin normalden "
                "düşük ya da yüksek çıkması endişe yaratabilir. Demir, vücudumuzda hemoglobin "
                "üretimi, oksijen taşınması, enerji metabolizması ve bağışıklık sistemi için "
                "vazgeçilmez bir mineraldir. Bu rehber, serum demir testinin ne anlama geldiğini, "
                "sonuçlarınızı nasıl yorumlayabileceğinizi ve doktor görüşmenize nasıl "
                "hazırlanacağınızı anlatmaktadır.</p>"
                "<p>Amacımız teşhis koymak değil — sizi doktor randevunuza daha bilinçli "
                "hazırlamaktır. Serum demir düzeyinizi tek başına değerlendirmek yerine "
                "<em>ferritin</em>, <em>TIBC</em> ve <em>transferrin satürasyonu</em> gibi "
                "ilişkili değerlerle birlikte ele almak çok önemlidir.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="Serum demir testi nedir?",
            body_html=(
                "<p><strong>Serum demir testi</strong>, kanınızdaki transferrine bağlı dolaşımdaki "
                "demir miktarını ölçer. Vücuttaki toplam demirin çok küçük bir kısmı kanda "
                "dolaşır; büyük bölümü hemoglobin içinde (eritrositlerde) ve ferritin olarak "
                "depolarda bulunur. Test, dolaşımdaki anlık demir düzeyini yansıtır.</p>"
                "<p>Sonuçlar genellikle <strong>μg/dL</strong> (mikrogram/desilitre) biriminde "
                "raporlanır. Serum demir düzeyi gün içinde dalgalanma gösterir — sabah saatlerinde "
                "genellikle daha yüksek, akşam saatlerinde daha düşüktür. Bu nedenle test "
                "genellikle sabah açlık durumunda yapılır. Demir eksikliği, anemi, kronik "
                "hastalıklar ve hemokromatoz gibi durumların değerlendirilmesinde sıklıkla "
                "istenir.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="Demir metabolizması nasıl çalışır?",
            body_html=(
                "<p>Demir metabolizması karmaşık ama düzenli bir sistemdir. Diyetle alınan demir "
                "başlıca <strong>duodenumda</strong> (onikiparmak bağırsağı) emilir. Hem-demir "
                "(hayvansal kaynaklı) emilimi, hem-olmayan demire (bitkisel kaynaklı) göre çok "
                "daha verimlidir. Emilen demir, kan dolaşımına geçerek <em>transferrin</em> "
                "proteinine bağlanır ve ihtiyaç duyulan dokulara taşınır.</p>"
                "<p>Kullanılmayan demir, karaciğer, dalak ve kemik iliğinde <em>ferritin</em> "
                "olarak depolanır. Vücuttaki demir dengesi büyük ölçüde karaciğerden salgılanan "
                "<strong>hepsidin</strong> hormonu tarafından düzenlenir. Hepsidin düzeyi "
                "yükseldiğinde bağırsak emilimi ve demir salınımı azalır; düştüğünde artar. "
                "Bu mekanizma, enfeksiyon ve inflamasyon durumlarında demirin mikroplara "
                "ulaşmasını engellemek için de devreye girer.</p>"
                "<p>Demir, hemoglobin sentezinde kritik rol oynar; ayrıca miyoglobin, "
                "sitokrom enzimleri ve DNA sentezi gibi süreçlerde de gereklidir. Hem eksikliği "
                "hem de fazlalığı ciddi sağlık sorunlarına yol açabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Demir normal değerleri",
            body_html=(
                "<p>Aşağıdaki tablo, serum demir ve ilişkili parametreler için genel kabul "
                "gören referans aralıklarını özetlemektedir. Laboratuvarlar arasında küçük "
                "farklılıklar olabilir; sonuçlarınızı her zaman kendi laboratuvarınızın "
                "referans aralığıyla karşılaştırın.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parametre</th>'
                f'<th {_TH}>Erkekler</th>'
                f'<th {_TH}>Kadınlar</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>Serum Demir</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>Transferrin Satürasyonu</td><td {_TD}>%20–50</td><td {_TD}>%15–50</td></tr>'
                f'<tr><td {_TD}>Ferritin</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Tek bir düşük veya yüksek değer her zaman hastalık anlamına gelmez. "
                "Gün içi dalgalanmalar, beslenme, hidrasyon ve stres gibi faktörler sonucu "
                "etkileyebilir. Hekiminiz klinik tablonuzla birlikte değerlendirecektir.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="Düşük demir (hipoferemi) nedenleri",
            body_html=(
                "<p><strong>Demir eksikliği anemisi</strong> dünya genelinde en yaygın beslenme "
                "eksikliğidir. Serum demirin düşük çıkmasının başlıca nedenleri şunlardır:</p>"
                "<ul>"
                "<li><strong>Yetersiz diyet alımı</strong> — özellikle vejetaryen ve vegan "
                "beslenme düzenlerinde hem-demir alımı düşüktür</li>"
                "<li><strong>Kan kaybı</strong> — yoğun menstrüasyon, gastrointestinal "
                "kanama (ülser, polip, kanser), sık kan bağışı</li>"
                "<li><strong>Malabsorpsiyon</strong> — çölyak hastalığı, inflamatuvar bağırsak "
                "hastalığı (IBD), mide ameliyatları emilimi bozabilir</li>"
                "<li><strong>Gebelik</strong> — artan demir ihtiyacı karşılanamadığında</li>"
                "<li><strong>Kronik hastalık anemisi</strong> — inflamasyon hepsidin düzeyini "
                "artırarak demirin dolaşıma çıkmasını engeller</li>"
                "</ul>"
                "<p>Demir eksikliği tanısı için serum demir tek başına yeterli değildir; "
                "<em>ferritin</em>, <em>TIBC</em> ve <em>transferrin satürasyonu</em> "
                "birlikte değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="Yüksek demir (hiperferemi) nedenleri",
            body_html=(
                "<p>Serum demir düzeyinin normalin üzerine çıkması da dikkatle "
                "değerlendirilmesi gereken bir bulgudur. Başlıca nedenleri:</p>"
                "<ul>"
                "<li><strong>Herediter hemokromatoz</strong> — genetik olarak bağırsaktan "
                "aşırı demir emilimi; tedavi edilmezse karaciğer, kalp ve pankreasa "
                "zarar verebilir</li>"
                "<li><strong>Aşırı demir takviyesi</strong> — gereksiz yere yüksek doz "
                "demir preparatı kullanımı</li>"
                "<li><strong>Hemolitik anemi</strong> — eritrositlerin erken yıkımı sonucu "
                "demir dolaşıma salınır</li>"
                "<li><strong>Karaciğer hastalığı</strong> — hepatit veya siroz ferritin "
                "ve serum demir düzeyini artırabilir</li>"
                "<li><strong>Çoklu kan transfüzyonları</strong> — her ünite kan ek demir "
                "yükü getirir</li>"
                "<li><strong>Demir zehirlenmesi</strong> — özellikle çocuklarda kazara "
                "yüksek doz alımı</li>"
                "</ul>"
                "<p>Yüksek demir uzun vadede organlarda birikime (<em>demir yükü</em>) neden "
                "olabilir. Erken tanı ve tedavi organ hasarını önlemek için çok önemlidir.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="Demir ve ferritin arasındaki fark",
            body_html=(
                "<p><strong>Serum demir</strong>, kanda transferrine bağlı dolaşan demir "
                "miktarının anlık bir ölçümüdür. Gün içinde önemli dalgalanmalar gösterir "
                "— sabah yüksek, akşam düşük olabilir — ve son yenilen öğünden "
                "etkilenebilir. Bu nedenle tek başına güvenilirliği sınırlıdır.</p>"
                "<p><strong>Ferritin</strong> ise vücuttaki demir depolarını yansıtır ve "
                "çok daha kararlı bir göstergedir. Düşük ferritin, demir depolarının "
                "tükendiğinin neredeyse kesin kanıtıdır. Ancak ferritin aynı zamanda bir "
                "<em>akut faz reaktanı</em> olduğundan, inflamasyon, enfeksiyon ve "
                "karaciğer hastalığı durumlarında demir depoları düşük olsa bile ferritin "
                "yüksek çıkabilir.</p>"
                "<p>Tam bir demir değerlendirmesi için her iki test birlikte — tercihen "
                "TIBC ve transferrin satürasyonu ile birlikte — yorumlanmalıdır. Hekiminiz "
                "bu parametrelerin birlikte oluşturduğu tabloya bakarak doğru tanıya "
                "ulaşacaktır.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC ve transferrin satürasyonu",
            body_html=(
                "<p><strong>TIBC (Toplam Demir Bağlama Kapasitesi)</strong>, kandaki "
                "transferrin proteininin taşıyabileceği toplam demir miktarını ölçer. "
                "Demir eksikliğinde vücut daha fazla transferrin üretir ve TIBC yükselir; "
                "demir fazlalığında veya kronik hastalıklarda TIBC düşer.</p>"
                "<p><strong>Transferrin satürasyonu</strong>, serum demirinin TIBC'ye "
                "oranı olarak hesaplanır: <em>(Serum Demir / TIBC) × 100</em>. Sağlıklı "
                "bireylerde genellikle %20–50 arasındadır. %20'nin altı demir eksikliğini, "
                "%50'nin üstü demir yüklenmesini düşündürür.</p>"
                "<p>Bu parametreler, serum demir ve ferritin ile birlikte "
                "değerlendirildiğinde demir metabolizması bozukluklarının ayırıcı tanısında "
                "güçlü bir araç oluşturur. Örneğin: düşük serum demir + yüksek TIBC + "
                "düşük ferritin = demir eksikliği anemisi; düşük serum demir + düşük "
                "TIBC + normal/yüksek ferritin = kronik hastalık anemisi.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Düşük ve yüksek demir belirtileri",
            body_html=(
                "<p><strong>Düşük demir belirtileri:</strong> Yorgunluk, halsizlik, soluk "
                "cilt, nefes darlığı, kırılgan tırnaklar, soğuk el ve ayaklar, baş "
                "dönmesi ve pika (toprak, buz gibi yenmeyen maddelere istek) en sık "
                "görülen şikayetlerdir. Ağır vakalarda taşikardi ve çarpıntı "
                "görülebilir.</p>"
                "<p><strong>Yüksek demir belirtileri:</strong> Eklem ağrısı (özellikle "
                "el ve parmak eklemleri), kronik yorgunluk, karın ağrısı, cilt renginin "
                "bronzlaşması, karaciğer büyümesi ve fonksiyon bozukluğu yüksek demir "
                "birikimine işaret edebilir. Hemokromatoz tedavi edilmezse diyabet, "
                "kardiyomiyopati ve siroz gibi ciddi komplikasyonlara neden olabilir.</p>"
                "<p>Her iki durumda da belirtiler yavaş gelişebilir ve başka nedenlere "
                "bağlanabilir. Düzenli kan tahlili, özellikle risk grubundaki kişilerde "
                "erken tanı için çok önemlidir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Kan tahlilinde serum demir değeriniz referans aralığının dışındaysa "
                "mutlaka bir hekime danışın. Özellikle aşağıdaki durumlarda gecikmeden "
                "tıbbi değerlendirme önerilir:</p>"
                "<ul>"
                "<li>Açıklanamayan yorgunluk, soluk cilt veya nefes darlığı</li>"
                "<li>Ailede hemokromatoz öyküsü</li>"
                "<li>Yoğun menstrüasyon veya gastrointestinal kanama şüphesi</li>"
                "<li>Ferritin çok düşük veya çok yüksek</li>"
                "<li>Transferrin satürasyonu %20 altı veya %50 üstü</li>"
                "</ul>"
                "<p>Hekiminiz gerektiğinde ek testler (tam kan sayımı, periferik yayma, "
                "B12 ve folat düzeyleri, genetik testler) isteyerek altta yatan nedeni "
                "belirleyecektir. Erken tanı ve tedavi, komplikasyonların önlenmesinde "
                "büyük önem taşır.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya size nasıl yardımcı olabilir?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızı anlamak bazen kafa karıştırıcı olabilir. "
                "<strong>Norya</strong>, kan tahlili raporunuzu yükleyerek dakikalar içinde "
                "yapılandırılmış, anlaşılır bir sağlık özeti almanızı sağlar. Sonuçlarınız "
                "referans aralıklarıyla karşılaştırılır ve size kolay anlaşılır bir dille "
                "açıklanır.</p>"
                "<p>Norya bir tanı aracı değildir — amacı sizi doktor görüşmenize daha "
                "bilinçli ve hazırlıklı hale getirmektir. Hemen "
                "<a href=\"/analyze\">Norya ile analiz başlatın</a> ve sonuçlarınızın ne "
                "anlama geldiğini keşfedin. Fiyatlandırma detayları için "
                "<a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis '
                'yerine geçmez.</strong> Sonuçlarınızı mutlaka bir sağlık uzmanıyla '
                'değerlendirin. <a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ENGLISH
# ─────────────────────────────────────────────────────────────────────
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Serum iron blood test: what low or high results mean",
            body_html=(
                "<p>A serum iron test is one of the key markers doctors order when evaluating "
                "iron status, anemia, or unexplained fatigue. Whether your result comes back "
                "flagged as low or high, it naturally raises questions: <em>should I worry?</em> "
                "The answer depends on the full clinical picture — serum iron alone is a snapshot, "
                "not a diagnosis.</p>"
                "<p>This guide explains what serum iron measures, how iron is metabolised, what "
                "the reference ranges mean, and when you should consult a healthcare professional. "
                "It is educational, not diagnostic — always discuss your results with a doctor.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="What is a serum iron test?",
            body_html=(
                "<p>A <strong>serum iron test</strong> measures the amount of iron circulating "
                "in your blood that is bound to the transport protein <em>transferrin</em>. "
                "Only a small fraction of total body iron is found in serum; the majority is "
                "incorporated into hemoglobin inside red blood cells or stored as ferritin "
                "in the liver, spleen, and bone marrow.</p>"
                "<p>Results are typically reported in <strong>μg/dL</strong> (micrograms per "
                "decilitre). Serum iron levels fluctuate throughout the day — they tend to be "
                "highest in the morning and lowest in the evening — and can be influenced by "
                "recent meals. For this reason, the test is usually drawn in the morning after "
                "an overnight fast.</p>"
                "<p>Serum iron is most useful when interpreted alongside related markers such "
                "as <em>ferritin</em>, <em>TIBC</em> (total iron-binding capacity), and "
                "<em>transferrin saturation</em>, which together paint a more complete picture "
                "of iron metabolism.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="How iron metabolism works",
            body_html=(
                "<p>Iron is absorbed primarily in the <strong>duodenum</strong> (the first "
                "part of the small intestine). Heme iron from animal sources is absorbed far "
                "more efficiently than non-heme iron from plant-based foods. Once absorbed, "
                "iron enters the bloodstream and binds to <em>transferrin</em>, the main "
                "iron-transport protein, which delivers it to tissues that need it — above all "
                "the bone marrow, where it is incorporated into hemoglobin.</p>"
                "<p>Surplus iron is stored as <em>ferritin</em> in the liver, spleen, and bone "
                "marrow. The body has no active excretion pathway for iron; losses occur mainly "
                "through shed intestinal cells, menstruation, and minor bleeding. Iron balance "
                "is therefore regulated at the point of absorption by <strong>hepcidin</strong>, "
                "a hormone produced by the liver. When iron stores are adequate or inflammation "
                "is present, hepcidin rises and blocks further absorption; when stores are low, "
                "hepcidin falls and absorption increases.</p>"
                "<p>Beyond hemoglobin, iron is essential for <em>myoglobin</em> (muscle oxygen "
                "storage), cytochrome enzymes (energy production), and DNA synthesis. Both "
                "deficiency and overload can have serious health consequences.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal ranges for iron parameters",
            body_html=(
                "<p>Reference ranges vary slightly between laboratories. The table below "
                "summarises widely accepted values. Always compare your result against the "
                "specific range printed on your lab report.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parameter</th>'
                f'<th {_TH}>Men</th>'
                f'<th {_TH}>Women</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>Serum Iron</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>Transferrin Saturation</td><td {_TD}>20–50%</td><td {_TD}>15–50%</td></tr>'
                f'<tr><td {_TD}>Ferritin</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>A single result slightly outside the range is not always cause for concern. "
                "Diurnal variation, recent meals, hydration status, and stress can all affect "
                "serum iron. Your doctor will interpret the result in the context of your "
                "symptoms and other laboratory findings.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="Causes of low serum iron",
            body_html=(
                "<p><strong>Iron deficiency</strong> is the most common nutritional deficiency "
                "worldwide and the leading cause of anemia. Low serum iron can result from:</p>"
                "<ul>"
                "<li><strong>Iron deficiency anemia</strong> — insufficient dietary intake or "
                "increased demand that outpaces supply</li>"
                "<li><strong>Blood loss</strong> — heavy menstruation, gastrointestinal bleeding "
                "(ulcers, polyps, colon cancer), frequent blood donation</li>"
                "<li><strong>Malabsorption</strong> — celiac disease, inflammatory bowel disease "
                "(IBD), gastric bypass surgery can impair iron uptake</li>"
                "<li><strong>Vegetarian or vegan diet</strong> — lower heme-iron intake reduces "
                "overall absorption efficiency</li>"
                "<li><strong>Pregnancy</strong> — expanded blood volume and fetal demands increase "
                "iron requirements substantially</li>"
                "<li><strong>Chronic disease anemia</strong> — inflammation raises hepcidin, "
                "trapping iron in storage and lowering serum levels</li>"
                "</ul>"
                "<p>Serum iron alone is not sufficient to diagnose iron deficiency. Your doctor "
                "will evaluate ferritin, TIBC, and transferrin saturation together to confirm "
                "the diagnosis and identify the underlying cause.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="Causes of high serum iron",
            body_html=(
                "<p>Elevated serum iron also warrants medical attention. Common causes include:</p>"
                "<ul>"
                "<li><strong>Hereditary hemochromatosis</strong> — a genetic disorder causing "
                "excessive iron absorption from the gut; if untreated, iron accumulates in the "
                "liver, heart, and pancreas, leading to organ damage</li>"
                "<li><strong>Excessive iron supplementation</strong> — taking high-dose iron "
                "tablets without medical supervision</li>"
                "<li><strong>Hemolytic anemia</strong> — premature destruction of red blood cells "
                "releases iron back into the bloodstream</li>"
                "<li><strong>Liver disease</strong> — hepatitis or cirrhosis can elevate both "
                "ferritin and serum iron</li>"
                "<li><strong>Multiple blood transfusions</strong> — each unit of transfused blood "
                "adds approximately 200–250 mg of iron</li>"
                "<li><strong>Iron poisoning</strong> — accidental ingestion of large doses, "
                "particularly dangerous in children</li>"
                "</ul>"
                "<p>Chronic iron overload leads to iron deposition in organs, a condition known "
                "as <em>hemosiderosis</em>. Early detection through routine blood work and "
                "genetic screening (for hemochromatosis) is critical to prevent irreversible "
                "organ damage.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="Iron vs. ferritin: what is the difference?",
            body_html=(
                "<p><strong>Serum iron</strong> is a snapshot of the iron currently circulating "
                "in the blood, bound to transferrin. It fluctuates significantly throughout the "
                "day — higher in the morning, lower in the evening — and is affected by recent "
                "food intake. Because of this variability, a single measurement has limited "
                "reliability on its own.</p>"
                "<p><strong>Ferritin</strong> reflects the body's iron stores and is a much more "
                "stable marker. Low ferritin is nearly definitive evidence that iron stores are "
                "depleted. However, ferritin is also an <em>acute-phase reactant</em>, meaning "
                "it rises during inflammation, infection, and liver disease — potentially masking "
                "underlying iron deficiency.</p>"
                "<p>For a complete assessment of iron status, both tests should be interpreted "
                "together, ideally alongside TIBC and transferrin saturation. This combination "
                "allows your doctor to distinguish between iron deficiency anemia, chronic "
                "disease anemia, and iron overload conditions.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC and transferrin saturation explained",
            body_html=(
                "<p><strong>TIBC (Total Iron-Binding Capacity)</strong> measures the maximum "
                "amount of iron that transferrin in the blood can carry. In iron deficiency, "
                "the body produces more transferrin to capture every available iron atom, so "
                "TIBC rises. In iron overload or chronic disease, transferrin production "
                "decreases and TIBC falls.</p>"
                "<p><strong>Transferrin saturation</strong> is calculated as: "
                "<em>(Serum Iron ÷ TIBC) × 100</em>. In healthy individuals it typically "
                "ranges from 20% to 50%. A saturation below 20% suggests iron deficiency; "
                "above 50% raises concern for iron overload, particularly hemochromatosis.</p>"
                "<p>When evaluated alongside serum iron and ferritin, these markers form a "
                "powerful diagnostic panel. For example: low serum iron + high TIBC + low "
                "ferritin = iron deficiency anemia; low serum iron + low TIBC + normal or "
                "elevated ferritin = anemia of chronic disease.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of low and high iron",
            body_html=(
                "<p><strong>Low iron symptoms:</strong> Fatigue, pallor, shortness of breath "
                "on exertion, brittle nails, cold hands and feet, dizziness, headache, and "
                "<em>pica</em> (craving non-food items such as ice or clay) are hallmark signs "
                "of iron deficiency. In severe cases, tachycardia, chest pain, and restless "
                "legs syndrome may develop.</p>"
                "<p><strong>High iron symptoms:</strong> Joint pain (especially in the hands), "
                "chronic fatigue, abdominal pain, skin bronzing (a grayish-brown discolouration), "
                "liver enlargement, and impaired liver function can signal iron overload. "
                "Untreated hemochromatosis may progress to diabetes, cardiomyopathy, and "
                "cirrhosis.</p>"
                "<p>Symptoms in both directions tend to develop gradually, making them easy to "
                "overlook. Regular blood testing — especially for those with a family history of "
                "iron disorders — is the most reliable way to catch problems early.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>You should consult a healthcare professional if your serum iron falls "
                "outside the reference range. Seek timely medical evaluation especially if:</p>"
                "<ul>"
                "<li>You experience unexplained fatigue, pallor, or shortness of breath</li>"
                "<li>There is a family history of hemochromatosis or iron disorders</li>"
                "<li>You have heavy menstrual periods or suspected gastrointestinal bleeding</li>"
                "<li>Your ferritin is very low or very high</li>"
                "<li>Transferrin saturation is below 20% or above 50%</li>"
                "</ul>"
                "<p>Your doctor may order additional tests — complete blood count, peripheral "
                "smear, B12 and folate levels, genetic testing for HFE mutations — to identify "
                "the underlying cause. Early diagnosis and treatment are essential to prevent "
                "complications such as organ damage or severe anemia.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya can help",
            body_html=(
                "<p>Understanding blood test results can sometimes be overwhelming. "
                "<strong>Norya</strong> lets you upload your blood test report and receive a "
                "structured, easy-to-understand health summary in minutes. Your results are "
                "compared against reference ranges and explained in plain language.</p>"
                "<p>Norya is not a diagnostic tool — its purpose is to prepare you for a more "
                "informed conversation with your doctor. "
                "<a href=\"/analyze\">Start your analysis with Norya</a> and discover what "
                "your results mean. For pricing details, visit our "
                "<a href=\"/pricing\">pricing page</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace '
                'medical advice or diagnosis.</strong> Always discuss your results with a '
                'healthcare professional. <a href="/analyze">Start analysis with Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# SPANISH
# ─────────────────────────────────────────────────────────────────────
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Análisis de hierro sérico: qué significa un resultado alto o bajo",
            body_html=(
                "<p>Cuando los resultados de su analítica muestran un nivel de <strong>hierro "
                "sérico</strong> fuera de lo normal, es natural preocuparse. El hierro es un "
                "mineral esencial para la producción de hemoglobina, el transporte de oxígeno, "
                "el metabolismo energético y la función inmunitaria. Esta guía le explica qué "
                "mide la prueba de hierro sérico, cómo interpretar los resultados y cuándo "
                "consultar a un profesional sanitario.</p>"
                "<p>Nuestro objetivo no es diagnosticar, sino prepararle para su consulta "
                "médica con mayor conocimiento. El hierro sérico debe evaluarse siempre junto "
                "con la <em>ferritina</em>, el <em>TIBC</em> y la <em>saturación de "
                "transferrina</em> para obtener una imagen completa.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="¿Qué es la prueba de hierro sérico?",
            body_html=(
                "<p>La <strong>prueba de hierro sérico</strong> mide la cantidad de hierro "
                "circulante en la sangre unido a la proteína de transporte <em>transferrina</em>. "
                "Solo una pequeña fracción del hierro total del cuerpo se encuentra en el suero; "
                "la mayor parte está incorporada en la hemoglobina o almacenada como ferritina "
                "en el hígado, el bazo y la médula ósea.</p>"
                "<p>Los resultados se expresan en <strong>μg/dL</strong>. Los niveles de hierro "
                "sérico fluctúan a lo largo del día — son más altos por la mañana y más bajos "
                "por la noche — y se ven influidos por la ingesta reciente. Por ello, la "
                "extracción suele realizarse en ayunas por la mañana.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="¿Cómo funciona el metabolismo del hierro?",
            body_html=(
                "<p>El hierro se absorbe principalmente en el <strong>duodeno</strong>. El "
                "hierro hemo (de origen animal) se absorbe con mucha mayor eficacia que el "
                "hierro no hemo (de origen vegetal). Una vez absorbido, pasa a la sangre y "
                "se une a la <em>transferrina</em>, que lo transporta a los tejidos que lo "
                "necesitan, especialmente la médula ósea para la síntesis de hemoglobina.</p>"
                "<p>El hierro sobrante se almacena como <em>ferritina</em> en el hígado, el "
                "bazo y la médula ósea. El organismo no dispone de un mecanismo activo de "
                "excreción de hierro; las pérdidas se producen por descamación intestinal, "
                "menstruación y pequeños sangrados. El equilibrio se regula mediante la "
                "<strong>hepcidina</strong>, una hormona hepática que reduce la absorción "
                "cuando los depósitos están llenos o hay inflamación.</p>"
                "<p>Además de la hemoglobina, el hierro es esencial para la <em>mioglobina</em>, "
                "las enzimas citocromo y la síntesis de ADN. Tanto el déficit como el exceso "
                "pueden tener consecuencias graves para la salud.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de hierro",
            body_html=(
                "<p>Los intervalos de referencia pueden variar ligeramente entre laboratorios. "
                "La tabla siguiente resume los valores generalmente aceptados. Compare siempre "
                "su resultado con el rango impreso en su informe de laboratorio.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parámetro</th>'
                f'<th {_TH}>Hombres</th>'
                f'<th {_TH}>Mujeres</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>Hierro Sérico</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>Saturación de Transferrina</td><td {_TD}>20–50%</td><td {_TD}>15–50%</td></tr>'
                f'<tr><td {_TD}>Ferritina</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Un valor ligeramente fuera del rango no siempre indica enfermedad. La "
                "variación diurna, la alimentación reciente y el estado de hidratación pueden "
                "influir. Su médico interpretará el resultado junto con su cuadro clínico.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="Causas de hierro sérico bajo",
            body_html=(
                "<p>La <strong>deficiencia de hierro</strong> es la carencia nutricional más "
                "frecuente en el mundo. Las principales causas de hierro sérico bajo son:</p>"
                "<ul>"
                "<li><strong>Anemia ferropénica</strong> — ingesta dietética insuficiente o "
                "aumento de la demanda</li>"
                "<li><strong>Pérdida de sangre</strong> — menstruación abundante, sangrado "
                "gastrointestinal (úlceras, pólipos, cáncer de colon)</li>"
                "<li><strong>Malabsorción</strong> — enfermedad celíaca, enfermedad inflamatoria "
                "intestinal (EII), cirugía gástrica</li>"
                "<li><strong>Dieta vegetariana o vegana</strong> — menor ingesta de hierro hemo</li>"
                "<li><strong>Embarazo</strong> — aumento del volumen sanguíneo y demandas fetales</li>"
                "<li><strong>Anemia de enfermedad crónica</strong> — la inflamación eleva la "
                "hepcidina, reteniendo el hierro en los depósitos</li>"
                "</ul>"
                "<p>El hierro sérico por sí solo no basta para diagnosticar la deficiencia. "
                "Su médico evaluará ferritina, TIBC y saturación de transferrina de forma "
                "conjunta.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="Causas de hierro sérico alto",
            body_html=(
                "<p>Un nivel elevado de hierro sérico también requiere atención médica. "
                "Las causas más comunes incluyen:</p>"
                "<ul>"
                "<li><strong>Hemocromatosis hereditaria</strong> — trastorno genético que causa "
                "absorción excesiva de hierro en el intestino</li>"
                "<li><strong>Suplementación excesiva de hierro</strong> — uso de dosis altas "
                "sin supervisión médica</li>"
                "<li><strong>Anemia hemolítica</strong> — destrucción prematura de glóbulos "
                "rojos que libera hierro al torrente sanguíneo</li>"
                "<li><strong>Enfermedad hepática</strong> — hepatitis o cirrosis pueden elevar "
                "el hierro y la ferritina</li>"
                "<li><strong>Transfusiones múltiples</strong> — cada unidad de sangre aporta "
                "aproximadamente 200–250 mg de hierro adicional</li>"
                "<li><strong>Intoxicación por hierro</strong> — ingestión accidental de dosis "
                "elevadas, especialmente peligrosa en niños</li>"
                "</ul>"
                "<p>La sobrecarga crónica de hierro provoca depósito en órganos "
                "(<em>hemosiderosis</em>). La detección precoz es clave para prevenir daño "
                "orgánico irreversible.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="Hierro vs. ferritina: ¿cuál es la diferencia?",
            body_html=(
                "<p>El <strong>hierro sérico</strong> es una instantánea del hierro circulante, "
                "unido a la transferrina. Fluctúa notablemente durante el día y se ve afectado "
                "por la ingesta reciente, lo que limita su fiabilidad como marcador aislado.</p>"
                "<p>La <strong>ferritina</strong> refleja los depósitos de hierro del organismo "
                "y es un marcador mucho más estable. Una ferritina baja es evidencia casi "
                "definitiva de que los depósitos están agotados. Sin embargo, como "
                "<em>reactante de fase aguda</em>, puede elevarse con la inflamación, la "
                "infección o la enfermedad hepática, enmascarando una deficiencia subyacente.</p>"
                "<p>Para una valoración completa del estado del hierro, ambas pruebas deben "
                "interpretarse juntas, idealmente con TIBC y saturación de transferrina. "
                "Esta combinación permite a su médico distinguir entre anemia ferropénica, "
                "anemia de enfermedad crónica y sobrecarga de hierro.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC y saturación de transferrina",
            body_html=(
                "<p>El <strong>TIBC (Capacidad Total de Fijación del Hierro)</strong> mide la "
                "cantidad máxima de hierro que la transferrina puede transportar. En la "
                "deficiencia de hierro, el organismo produce más transferrina y el TIBC sube; "
                "en la sobrecarga o enfermedad crónica, el TIBC baja.</p>"
                "<p>La <strong>saturación de transferrina</strong> se calcula como: "
                "<em>(Hierro Sérico ÷ TIBC) × 100</em>. En personas sanas suele estar entre "
                "el 20% y el 50%. Por debajo del 20% sugiere deficiencia de hierro; por encima "
                "del 50% sugiere sobrecarga, especialmente hemocromatosis.</p>"
                "<p>Evaluados junto con el hierro sérico y la ferritina, estos marcadores "
                "forman un panel diagnóstico potente. Por ejemplo: hierro sérico bajo + TIBC "
                "alto + ferritina baja = anemia ferropénica; hierro sérico bajo + TIBC bajo + "
                "ferritina normal o elevada = anemia de enfermedad crónica.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de hierro bajo y alto",
            body_html=(
                "<p><strong>Síntomas de hierro bajo:</strong> Fatiga, palidez, disnea de "
                "esfuerzo, uñas quebradizas, manos y pies fríos, mareos, cefalea y "
                "<em>pica</em> (deseo de ingerir sustancias no alimentarias como hielo o "
                "tierra). En casos graves pueden aparecer taquicardia y dolor torácico.</p>"
                "<p><strong>Síntomas de hierro alto:</strong> Dolor articular (especialmente "
                "en manos), fatiga crónica, dolor abdominal, coloración bronceada de la piel, "
                "hepatomegalia y disfunción hepática. Si no se trata, la hemocromatosis puede "
                "evolucionar a diabetes, miocardiopatía y cirrosis.</p>"
                "<p>Los síntomas en ambas direcciones suelen desarrollarse gradualmente, lo "
                "que facilita que pasen inadvertidos. Los análisis de sangre periódicos son la "
                "forma más fiable de detectar anomalías a tiempo.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Debe consultar a un profesional sanitario si su hierro sérico está fuera "
                "del rango de referencia. Se recomienda evaluación médica especialmente si:</p>"
                "<ul>"
                "<li>Presenta fatiga inexplicable, palidez o disnea</li>"
                "<li>Tiene antecedentes familiares de hemocromatosis</li>"
                "<li>Sufre menstruaciones abundantes o sospecha de sangrado digestivo</li>"
                "<li>Su ferritina es muy baja o muy alta</li>"
                "<li>La saturación de transferrina está por debajo del 20% o por encima del 50%</li>"
                "</ul>"
                "<p>Su médico podrá solicitar pruebas adicionales — hemograma completo, frotis "
                "periférico, B12, folato y pruebas genéticas — para identificar la causa. "
                "El diagnóstico y tratamiento tempranos son fundamentales para evitar "
                "complicaciones.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="¿Cómo le ayuda Norya?",
            body_html=(
                "<p>Entender los resultados de un análisis de sangre puede resultar confuso. "
                "<strong>Norya</strong> le permite subir su informe de análisis y recibir en "
                "minutos un resumen de salud estructurado y fácil de comprender. Sus resultados "
                "se comparan con los rangos de referencia y se explican en un lenguaje claro.</p>"
                "<p>Norya no es una herramienta de diagnóstico — su objetivo es prepararle para "
                "una conversación más informada con su médico. "
                "<a href=\"/analyze\">Inicie su análisis con Norya</a> y descubra qué significan "
                "sus resultados. Para detalles de precios, visite nuestra "
                "<a href=\"/pricing\">página de precios</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el '
                'diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional '
                'sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# GERMAN
# ─────────────────────────────────────────────────────────────────────
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Serumeisen-Bluttest: Was niedrige oder hohe Werte bedeuten",
            body_html=(
                "<p>Wenn Ihr Blutbild einen <strong>Serumeisen</strong>-Wert außerhalb des "
                "Normbereichs zeigt, ist Verunsicherung verständlich. Eisen ist ein essenzielles "
                "Mineral für die Hämoglobinproduktion, den Sauerstofftransport, den "
                "Energiestoffwechsel und die Immunfunktion. Dieser Leitfaden erklärt, was der "
                "Serumeisen-Test misst, wie Sie die Ergebnisse einordnen und wann Sie ärztlichen "
                "Rat einholen sollten.</p>"
                "<p>Unser Ziel ist nicht die Diagnosestellung, sondern Ihre Vorbereitung auf "
                "ein informiertes Arztgespräch. Serumeisen sollte stets zusammen mit "
                "<em>Ferritin</em>, <em>TIBC</em> und <em>Transferrinsättigung</em> beurteilt "
                "werden.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="Was ist ein Serumeisen-Test?",
            body_html=(
                "<p>Der <strong>Serumeisen-Test</strong> misst die Menge an Eisen im Blut, "
                "die an das Transportprotein <em>Transferrin</em> gebunden ist. Nur ein kleiner "
                "Teil des Gesamteisenbestands zirkuliert im Serum; der Großteil ist im "
                "Hämoglobin der roten Blutkörperchen eingebaut oder als Ferritin in Leber, "
                "Milz und Knochenmark gespeichert.</p>"
                "<p>Die Ergebnisse werden in <strong>μg/dL</strong> angegeben. Der "
                "Serumeisenspiegel schwankt im Tagesverlauf — morgens höher, abends niedriger "
                "— und wird durch kürzliche Mahlzeiten beeinflusst. Daher wird die Blutentnahme "
                "in der Regel morgens nüchtern durchgeführt.</p>"
                "<p>Serumeisen ist am aussagekräftigsten in Kombination mit <em>Ferritin</em>, "
                "<em>TIBC</em> und <em>Transferrinsättigung</em>, die zusammen ein umfassendes "
                "Bild des Eisenstoffwechsels ergeben.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="Wie funktioniert der Eisenstoffwechsel?",
            body_html=(
                "<p>Eisen wird hauptsächlich im <strong>Duodenum</strong> (Zwölffingerdarm) "
                "aufgenommen. Häm-Eisen aus tierischen Quellen wird wesentlich effizienter "
                "resorbiert als Nicht-Häm-Eisen aus pflanzlichen Lebensmitteln. Nach der "
                "Aufnahme gelangt Eisen ins Blut und bindet an <em>Transferrin</em>, das es "
                "zu den Zielgeweben transportiert — vor allem zum Knochenmark für die "
                "Hämoglobinsynthese.</p>"
                "<p>Überschüssiges Eisen wird als <em>Ferritin</em> in Leber, Milz und "
                "Knochenmark gespeichert. Der Körper besitzt keinen aktiven "
                "Eisenausscheidungsmechanismus; Verluste erfolgen über abgeschilferte "
                "Darmzellen, Menstruation und kleinere Blutungen. Die Eisenbalance wird "
                "daher am Absorptionspunkt durch <strong>Hepcidin</strong> reguliert, ein "
                "Leberhormon, das bei vollen Speichern oder Entzündung die Aufnahme hemmt.</p>"
                "<p>Neben Hämoglobin ist Eisen auch für <em>Myoglobin</em>, "
                "Cytochrom-Enzyme und die DNA-Synthese unverzichtbar. Sowohl Mangel als "
                "auch Überladung können schwerwiegende gesundheitliche Folgen haben.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normwerte für Eisenparameter",
            body_html=(
                "<p>Referenzbereiche können zwischen Laboren leicht variieren. Die folgende "
                "Tabelle fasst allgemein anerkannte Werte zusammen. Vergleichen Sie Ihr "
                "Ergebnis immer mit dem auf Ihrem Laborbefund angegebenen Bereich.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parameter</th>'
                f'<th {_TH}>Männer</th>'
                f'<th {_TH}>Frauen</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>Serumeisen</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>Transferrinsättigung</td><td {_TD}>20–50 %</td><td {_TD}>15–50 %</td></tr>'
                f'<tr><td {_TD}>Ferritin</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Ein einzelner Wert leicht außerhalb des Bereichs ist nicht immer "
                "besorgniserregend. Tageszeitliche Schwankungen, kürzliche Mahlzeiten und "
                "der Hydratationszustand können das Serumeisen beeinflussen. Ihr Arzt wird "
                "das Ergebnis im Kontext Ihrer Symptome und weiterer Laborbefunde "
                "interpretieren.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="Ursachen für niedriges Serumeisen",
            body_html=(
                "<p><strong>Eisenmangel</strong> ist weltweit der häufigste Nährstoffmangel. "
                "Mögliche Ursachen für niedriges Serumeisen:</p>"
                "<ul>"
                "<li><strong>Eisenmangelanämie</strong> — unzureichende Zufuhr oder erhöhter "
                "Bedarf, der das Angebot übersteigt</li>"
                "<li><strong>Blutverlust</strong> — starke Menstruation, gastrointestinale "
                "Blutungen (Ulkus, Polypen, Darmkrebs), häufige Blutspenden</li>"
                "<li><strong>Malabsorption</strong> — Zöliakie, chronisch-entzündliche "
                "Darmerkrankungen (CED), Magenbypass-Operationen</li>"
                "<li><strong>Vegetarische oder vegane Ernährung</strong> — geringere Aufnahme "
                "von Häm-Eisen</li>"
                "<li><strong>Schwangerschaft</strong> — erhöhtes Blutvolumen und fetaler Bedarf</li>"
                "<li><strong>Anämie bei chronischer Erkrankung</strong> — Entzündung erhöht "
                "Hepcidin und hält Eisen in den Speichern zurück</li>"
                "</ul>"
                "<p>Serumeisen allein reicht für die Diagnose eines Eisenmangels nicht aus. "
                "Ihr Arzt wird Ferritin, TIBC und Transferrinsättigung gemeinsam beurteilen.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="Ursachen für hohes Serumeisen",
            body_html=(
                "<p>Auch ein erhöhter Serumeisenwert bedarf ärztlicher Abklärung. "
                "Häufige Ursachen:</p>"
                "<ul>"
                "<li><strong>Hereditäre Hämochromatose</strong> — genetische Störung mit "
                "übermäßiger Eisenaufnahme aus dem Darm; unbehandelt führt sie zu "
                "Organschäden an Leber, Herz und Pankreas</li>"
                "<li><strong>Übermäßige Eisensupplementation</strong> — Einnahme hochdosierter "
                "Eisenpräparate ohne ärztliche Aufsicht</li>"
                "<li><strong>Hämolytische Anämie</strong> — vorzeitiger Abbau roter "
                "Blutkörperchen setzt Eisen frei</li>"
                "<li><strong>Lebererkrankung</strong> — Hepatitis oder Zirrhose können Ferritin "
                "und Serumeisen erhöhen</li>"
                "<li><strong>Wiederholte Bluttransfusionen</strong> — jede Einheit Blut liefert "
                "ca.&nbsp;200–250 mg Eisen</li>"
                "<li><strong>Eisenvergiftung</strong> — versehentliche Einnahme hoher Dosen, "
                "besonders gefährlich bei Kindern</li>"
                "</ul>"
                "<p>Chronische Eisenüberladung führt zur Eisenablagerung in Organen "
                "(<em>Hämosiderose</em>). Frühzeitige Erkennung ist entscheidend, um "
                "irreversible Schäden zu verhindern.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="Eisen vs. Ferritin: Was ist der Unterschied?",
            body_html=(
                "<p><strong>Serumeisen</strong> ist eine Momentaufnahme des aktuell "
                "zirkulierenden Eisens, gebunden an Transferrin. Es schwankt im Tagesverlauf "
                "erheblich und wird durch Mahlzeiten beeinflusst, was seine Aussagekraft als "
                "alleiniger Marker einschränkt.</p>"
                "<p><strong>Ferritin</strong> spiegelt die Eisenspeicher des Körpers wider und "
                "ist ein wesentlich stabilerer Marker. Niedriges Ferritin ist nahezu "
                "beweisend für leere Eisenspeicher. Da Ferritin jedoch auch ein "
                "<em>Akute-Phase-Protein</em> ist, kann es bei Entzündung, Infektion oder "
                "Lebererkrankung erhöht sein — und so einen bestehenden Eisenmangel "
                "verschleiern.</p>"
                "<p>Für eine vollständige Beurteilung des Eisenstatus sollten beide Tests "
                "zusammen interpretiert werden, idealerweise mit TIBC und "
                "Transferrinsättigung. So kann Ihr Arzt zwischen Eisenmangelanämie, "
                "Entzündungsanämie und Eisenüberladung unterscheiden.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC und Transferrinsättigung erklärt",
            body_html=(
                "<p>Die <strong>TIBC (Totale Eisenbindungskapazität)</strong> misst die "
                "maximale Eisenmenge, die Transferrin im Blut transportieren kann. Bei "
                "Eisenmangel produziert der Körper mehr Transferrin, sodass die TIBC steigt; "
                "bei Eisenüberladung oder chronischer Erkrankung sinkt sie.</p>"
                "<p>Die <strong>Transferrinsättigung</strong> wird berechnet als: "
                "<em>(Serumeisen ÷ TIBC) × 100</em>. Bei gesunden Erwachsenen liegt sie "
                "typischerweise zwischen 20 % und 50 %. Unter 20 % spricht für Eisenmangel; "
                "über 50 % weckt den Verdacht auf Eisenüberladung, insbesondere "
                "Hämochromatose.</p>"
                "<p>Zusammen mit Serumeisen und Ferritin bilden diese Marker ein "
                "leistungsfähiges Diagnosepanel. Beispiel: niedriges Serumeisen + hohe TIBC "
                "+ niedriges Ferritin = Eisenmangelanämie; niedriges Serumeisen + niedrige "
                "TIBC + normales/erhöhtes Ferritin = Entzündungsanämie.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome bei niedrigem und hohem Eisen",
            body_html=(
                "<p><strong>Symptome bei Eisenmangel:</strong> Müdigkeit, Blässe, Kurzatmigkeit "
                "bei Belastung, brüchige Nägel, kalte Hände und Füße, Schwindel, Kopfschmerzen "
                "und <em>Pica</em> (Verlangen nach nicht-essbaren Substanzen wie Eis oder Erde). "
                "In schweren Fällen können Tachykardie und Brustschmerzen auftreten.</p>"
                "<p><strong>Symptome bei Eisenüberladung:</strong> Gelenkschmerzen (besonders in "
                "den Händen), chronische Müdigkeit, Bauchschmerzen, bronzefarbene Hautverfärbung, "
                "Lebervergrößerung und eingeschränkte Leberfunktion. Unbehandelte Hämochromatose "
                "kann zu Diabetes, Kardiomyopathie und Zirrhose fortschreiten.</p>"
                "<p>In beiden Fällen entwickeln sich die Symptome häufig schleichend und werden "
                "leicht übersehen. Regelmäßige Blutuntersuchungen — besonders bei familiärer "
                "Vorbelastung — sind der zuverlässigste Weg zur Früherkennung.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Suchen Sie ärztlichen Rat, wenn Ihr Serumeisen außerhalb des "
                "Referenzbereichs liegt. Eine zeitnahe Abklärung ist besonders wichtig bei:</p>"
                "<ul>"
                "<li>Ungeklärter Müdigkeit, Blässe oder Kurzatmigkeit</li>"
                "<li>Familiärer Vorgeschichte mit Hämochromatose</li>"
                "<li>Starker Menstruation oder Verdacht auf gastrointestinale Blutung</li>"
                "<li>Sehr niedrigem oder sehr hohem Ferritin</li>"
                "<li>Transferrinsättigung unter 20 % oder über 50 %</li>"
                "</ul>"
                "<p>Ihr Arzt kann zusätzliche Tests anordnen — Blutbild, peripherer Abstrich, "
                "B12, Folsäure und HFE-Gentests — um die Ursache zu identifizieren. "
                "Früherkennung und Behandlung sind essenziell, um Komplikationen wie "
                "Organschäden oder schwere Anämie zu verhindern.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen helfen kann",
            body_html=(
                "<p>Bluttestergebnisse zu verstehen kann manchmal überwältigend sein. "
                "<strong>Norya</strong> ermöglicht es Ihnen, Ihren Laborbefund hochzuladen "
                "und in Minuten eine strukturierte, leicht verständliche Gesundheitsübersicht "
                "zu erhalten. Ihre Werte werden mit Referenzbereichen verglichen und in "
                "einfacher Sprache erklärt.</p>"
                "<p>Norya ist kein Diagnosetool — es bereitet Sie auf ein informierteres "
                "Gespräch mit Ihrem Arzt vor. "
                "<a href=\"/analyze\">Starten Sie Ihre Analyse mit Norya</a> und erfahren Sie, "
                "was Ihre Ergebnisse bedeuten. Preisdetails finden Sie auf unserer "
                "<a href=\"/pricing\">Preisseite</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine '
                'ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse '
                'immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# FRENCH
# ─────────────────────────────────────────────────────────────────────
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Fer sérique : que signifie un résultat bas ou élevé ?",
            body_html=(
                "<p>Lorsque vos résultats sanguins indiquent un taux de <strong>fer "
                "sérique</strong> en dehors de la normale, il est naturel de s'inquiéter. "
                "Le fer est un minéral essentiel à la production d'hémoglobine, au transport "
                "de l'oxygène, au métabolisme énergétique et à la fonction immunitaire. Ce "
                "guide vous explique ce que mesure le test de fer sérique, comment interpréter "
                "vos résultats et quand consulter un professionnel de santé.</p>"
                "<p>Notre objectif n'est pas de poser un diagnostic, mais de vous préparer à "
                "un échange éclairé avec votre médecin. Le fer sérique doit toujours être "
                "évalué conjointement avec la <em>ferritine</em>, la <em>CTF (TIBC)</em> et "
                "le <em>coefficient de saturation de la transferrine</em>.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="Qu'est-ce que le test de fer sérique ?",
            body_html=(
                "<p>Le <strong>test de fer sérique</strong> mesure la quantité de fer circulant "
                "dans le sang, liée à la protéine de transport <em>transferrine</em>. Seule "
                "une petite fraction du fer total de l'organisme se trouve dans le sérum ; la "
                "majeure partie est incorporée dans l'hémoglobine ou stockée sous forme de "
                "ferritine dans le foie, la rate et la moelle osseuse.</p>"
                "<p>Les résultats sont exprimés en <strong>μg/dL</strong>. Le taux de fer "
                "sérique fluctue au cours de la journée — plus élevé le matin, plus bas le "
                "soir — et est influencé par les repas récents. Le prélèvement est donc "
                "généralement effectué à jeun le matin.</p>"
                "<p>Le fer sérique est le plus informatif lorsqu'il est interprété avec la "
                "<em>ferritine</em>, la <em>CTF</em> et le <em>coefficient de saturation</em>, "
                "qui ensemble offrent une image plus complète du métabolisme du fer.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="Comment fonctionne le métabolisme du fer ?",
            body_html=(
                "<p>Le fer est absorbé principalement dans le <strong>duodénum</strong>. Le "
                "fer héminique (d'origine animale) est absorbé beaucoup plus efficacement que "
                "le fer non héminique (d'origine végétale). Une fois absorbé, il passe dans le "
                "sang et se lie à la <em>transferrine</em>, qui le transporte vers les tissus "
                "qui en ont besoin, notamment la moelle osseuse pour la synthèse de "
                "l'hémoglobine.</p>"
                "<p>Le fer excédentaire est stocké sous forme de <em>ferritine</em> dans le "
                "foie, la rate et la moelle osseuse. L'organisme ne dispose pas de mécanisme "
                "actif d'excrétion du fer ; les pertes surviennent par desquamation "
                "intestinale, menstruation et saignements mineurs. L'équilibre est régulé par "
                "l'<strong>hepcidine</strong>, une hormone hépatique qui réduit l'absorption "
                "quand les réserves sont pleines ou en cas d'inflammation.</p>"
                "<p>Au-delà de l'hémoglobine, le fer est nécessaire à la <em>myoglobine</em>, "
                "aux enzymes cytochromes et à la synthèse d'ADN. Tant la carence que la "
                "surcharge peuvent avoir des conséquences graves sur la santé.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales du fer",
            body_html=(
                "<p>Les intervalles de référence varient légèrement selon les laboratoires. "
                "Le tableau ci-dessous résume les valeurs généralement acceptées. Comparez "
                "toujours votre résultat avec l'intervalle indiqué sur votre compte rendu "
                "de laboratoire.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Paramètre</th>'
                f'<th {_TH}>Hommes</th>'
                f'<th {_TH}>Femmes</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>Fer Sérique</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>CTF (TIBC)</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>Saturation de la Transferrine</td><td {_TD}>20–50 %</td><td {_TD}>15–50 %</td></tr>'
                f'<tr><td {_TD}>Ferritine</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Une valeur légèrement en dehors de l'intervalle n'est pas toujours "
                "préoccupante. Les variations nycthémérales, les repas récents et l'état "
                "d'hydratation peuvent influencer le fer sérique. Votre médecin interprétera "
                "le résultat en tenant compte de vos symptômes et des autres bilans.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="Causes d'un fer sérique bas",
            body_html=(
                "<p>La <strong>carence en fer</strong> est la carence nutritionnelle la plus "
                "fréquente au monde. Les principales causes d'un fer sérique bas sont :</p>"
                "<ul>"
                "<li><strong>Anémie ferriprive</strong> — apport alimentaire insuffisant ou "
                "besoins accrus dépassant l'apport</li>"
                "<li><strong>Pertes sanguines</strong> — règles abondantes, saignement "
                "gastro-intestinal (ulcère, polypes, cancer colorectal)</li>"
                "<li><strong>Malabsorption</strong> — maladie cœliaque, maladie inflammatoire "
                "chronique de l'intestin (MICI), chirurgie gastrique</li>"
                "<li><strong>Régime végétarien ou végan</strong> — moindre apport en fer "
                "héminique</li>"
                "<li><strong>Grossesse</strong> — augmentation du volume sanguin et besoins "
                "fœtaux</li>"
                "<li><strong>Anémie des maladies chroniques</strong> — l'inflammation élève "
                "l'hepcidine, séquestrant le fer dans les réserves</li>"
                "</ul>"
                "<p>Le fer sérique seul ne suffit pas à diagnostiquer une carence. Votre "
                "médecin évaluera la ferritine, la CTF et le coefficient de saturation "
                "conjointement.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="Causes d'un fer sérique élevé",
            body_html=(
                "<p>Un taux élevé de fer sérique nécessite également une évaluation médicale. "
                "Les causes les plus courantes :</p>"
                "<ul>"
                "<li><strong>Hémochromatose héréditaire</strong> — maladie génétique entraînant "
                "une absorption intestinale excessive de fer</li>"
                "<li><strong>Supplémentation excessive en fer</strong> — prise de comprimés "
                "de fer à haute dose sans avis médical</li>"
                "<li><strong>Anémie hémolytique</strong> — destruction prématurée des globules "
                "rouges libérant du fer</li>"
                "<li><strong>Maladie hépatique</strong> — hépatite ou cirrhose pouvant élever "
                "la ferritine et le fer sérique</li>"
                "<li><strong>Transfusions multiples</strong> — chaque unité de sang apporte "
                "environ 200–250 mg de fer</li>"
                "<li><strong>Intoxication au fer</strong> — ingestion accidentelle de doses "
                "élevées, particulièrement dangereuse chez l'enfant</li>"
                "</ul>"
                "<p>La surcharge chronique en fer entraîne des dépôts dans les organes "
                "(<em>hémosidérose</em>). Le dépistage précoce est essentiel pour prévenir "
                "des dommages irréversibles.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="Fer vs. ferritine : quelle différence ?",
            body_html=(
                "<p>Le <strong>fer sérique</strong> est un instantané du fer circulant, lié à "
                "la transferrine. Il fluctue significativement au cours de la journée et est "
                "influencé par les repas, ce qui limite sa fiabilité en tant que marqueur "
                "isolé.</p>"
                "<p>La <strong>ferritine</strong> reflète les réserves en fer de l'organisme "
                "et constitue un marqueur bien plus stable. Une ferritine basse est quasiment "
                "la preuve que les réserves sont épuisées. Toutefois, en tant que "
                "<em>protéine de la phase aiguë</em>, elle peut s'élever en cas "
                "d'inflammation, d'infection ou de maladie hépatique — masquant potentiellement "
                "une carence sous-jacente.</p>"
                "<p>Pour une évaluation complète du statut en fer, les deux tests doivent être "
                "interprétés ensemble, idéalement avec la CTF et le coefficient de saturation. "
                "Cette combinaison permet à votre médecin de distinguer anémie ferriprive, "
                "anémie inflammatoire et surcharge en fer.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="CTF (TIBC) et saturation de la transferrine",
            body_html=(
                "<p>La <strong>CTF (Capacité Totale de Fixation du Fer)</strong> mesure la "
                "quantité maximale de fer que la transferrine peut transporter. En cas de "
                "carence en fer, l'organisme produit davantage de transferrine et la CTF "
                "augmente ; en cas de surcharge ou de maladie chronique, la CTF diminue.</p>"
                "<p>Le <strong>coefficient de saturation de la transferrine</strong> se calcule "
                "ainsi : <em>(Fer Sérique ÷ CTF) × 100</em>. Chez un sujet sain, il se situe "
                "généralement entre 20 % et 50 %. En dessous de 20 %, on suspecte une carence "
                "en fer ; au-dessus de 50 %, une surcharge, notamment l'hémochromatose.</p>"
                "<p>Évalués conjointement avec le fer sérique et la ferritine, ces marqueurs "
                "forment un puissant panel diagnostique. Exemple : fer sérique bas + CTF "
                "élevée + ferritine basse = anémie ferriprive ; fer sérique bas + CTF basse + "
                "ferritine normale ou élevée = anémie inflammatoire.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d'un fer bas et d'un fer élevé",
            body_html=(
                "<p><strong>Symptômes d'un fer bas :</strong> Fatigue, pâleur, essoufflement "
                "à l'effort, ongles cassants, extrémités froides, vertiges, céphalées et "
                "<em>pica</em> (envie de substances non alimentaires comme la glace ou la "
                "terre). Dans les cas sévères, tachycardie et douleur thoracique peuvent "
                "survenir.</p>"
                "<p><strong>Symptômes d'un fer élevé :</strong> Douleurs articulaires "
                "(surtout aux mains), fatigue chronique, douleurs abdominales, teint bronzé, "
                "hépatomégalie et dysfonction hépatique. Non traitée, l'hémochromatose peut "
                "évoluer vers le diabète, la cardiomyopathie et la cirrhose.</p>"
                "<p>Les symptômes, dans les deux cas, se développent souvent progressivement "
                "et sont facilement ignorés. Des analyses de sang régulières — en particulier "
                "en cas d'antécédents familiaux — sont le moyen le plus fiable de détecter "
                "les anomalies à temps.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez un professionnel de santé si votre fer sérique est en dehors "
                "de l'intervalle de référence. Une évaluation rapide est particulièrement "
                "recommandée si :</p>"
                "<ul>"
                "<li>Vous présentez une fatigue inexpliquée, une pâleur ou un essoufflement</li>"
                "<li>Vous avez des antécédents familiaux d'hémochromatose</li>"
                "<li>Vous avez des règles abondantes ou suspectez un saignement digestif</li>"
                "<li>Votre ferritine est très basse ou très élevée</li>"
                "<li>Le coefficient de saturation est inférieur à 20 % ou supérieur à 50 %</li>"
                "</ul>"
                "<p>Votre médecin pourra prescrire des examens complémentaires — NFS, frottis "
                "sanguin, B12, folates, tests génétiques HFE — pour identifier la cause. "
                "Un diagnostic et un traitement précoces sont essentiels pour prévenir les "
                "complications.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya peut vous aider",
            body_html=(
                "<p>Comprendre les résultats d'un bilan sanguin peut parfois être déroutant. "
                "<strong>Norya</strong> vous permet de télécharger votre rapport d'analyse et "
                "de recevoir en quelques minutes un résumé de santé structuré et facile à "
                "comprendre. Vos résultats sont comparés aux valeurs de référence et expliqués "
                "dans un langage clair.</p>"
                "<p>Norya n'est pas un outil de diagnostic — il vous prépare à un échange "
                "plus éclairé avec votre médecin. "
                "<a href=\"/analyze\">Commencez votre analyse avec Norya</a> et découvrez ce "
                "que vos résultats signifient. Pour les détails tarifaires, visitez notre "
                "<a href=\"/pricing\">page de tarification</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace '
                'pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos '
                "résultats avec un professionnel de santé. "
                '<a href="/analyze">Commencer l\'analyse avec Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ITALIAN
# ─────────────────────────────────────────────────────────────────────
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Sideremia: cosa significa un valore alto o basso",
            body_html=(
                "<p>Quando le analisi del sangue mostrano un livello di <strong>ferro "
                "sierico (sideremia)</strong> fuori norma, è naturale preoccuparsi. Il ferro "
                "è un minerale essenziale per la produzione di emoglobina, il trasporto "
                "dell'ossigeno, il metabolismo energetico e la funzione immunitaria. Questa "
                "guida spiega cosa misura il test della sideremia, come interpretare i "
                "risultati e quando rivolgersi a un medico.</p>"
                "<p>Il nostro obiettivo non è formulare diagnosi, ma prepararvi a un colloquio "
                "più consapevole con il vostro medico. La sideremia va sempre valutata insieme "
                "a <em>ferritina</em>, <em>TIBC</em> e <em>saturazione della "
                "transferrina</em>.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="Cos'è il test della sideremia?",
            body_html=(
                "<p>Il <strong>test della sideremia</strong> misura la quantità di ferro "
                "circolante nel sangue, legata alla proteina di trasporto "
                "<em>transferrina</em>. Solo una piccola quota del ferro totale si trova nel "
                "siero; la maggior parte è incorporata nell'emoglobina dei globuli rossi o "
                "immagazzinata come ferritina nel fegato, nella milza e nel midollo osseo.</p>"
                "<p>I risultati sono espressi in <strong>μg/dL</strong>. La sideremia oscilla "
                "nel corso della giornata — più alta al mattino, più bassa alla sera — e "
                "risente dei pasti recenti. Per questo il prelievo viene solitamente effettuato "
                "al mattino a digiuno.</p>"
                "<p>La sideremia è più significativa se interpretata insieme a <em>ferritina</em>, "
                "<em>TIBC</em> e <em>saturazione della transferrina</em>, che insieme offrono "
                "un quadro completo del metabolismo del ferro.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="Come funziona il metabolismo del ferro?",
            body_html=(
                "<p>Il ferro viene assorbito principalmente nel <strong>duodeno</strong>. Il "
                "ferro eme (di origine animale) viene assorbito molto più efficientemente del "
                "ferro non eme (di origine vegetale). Una volta assorbito, entra nel circolo "
                "ematico e si lega alla <em>transferrina</em>, che lo trasporta ai tessuti che "
                "ne necessitano, soprattutto al midollo osseo per la sintesi di emoglobina.</p>"
                "<p>Il ferro in eccesso viene immagazzinato come <em>ferritina</em> nel fegato, "
                "nella milza e nel midollo osseo. L'organismo non possiede un meccanismo attivo "
                "di escrezione del ferro; le perdite avvengono tramite desquamazione "
                "intestinale, mestruazioni e piccole emorragie. L'equilibrio è regolato "
                "dall'<strong>epcidina</strong>, un ormone epatico che riduce l'assorbimento "
                "quando le riserve sono piene o in presenza di infiammazione.</p>"
                "<p>Oltre all'emoglobina, il ferro è essenziale per la <em>mioglobina</em>, "
                "gli enzimi citocromo e la sintesi del DNA. Sia la carenza che il sovraccarico "
                "possono avere gravi conseguenze per la salute.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del ferro",
            body_html=(
                "<p>Gli intervalli di riferimento possono variare leggermente tra i "
                "laboratori. La tabella seguente riassume i valori generalmente accettati. "
                "Confrontate sempre il vostro risultato con l'intervallo riportato sul vostro "
                "referto di laboratorio.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parametro</th>'
                f'<th {_TH}>Uomini</th>'
                f'<th {_TH}>Donne</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>Sideremia</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>Saturazione della Transferrina</td><td {_TD}>20–50%</td><td {_TD}>15–50%</td></tr>'
                f'<tr><td {_TD}>Ferritina</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Un valore lievemente fuori norma non è sempre motivo di preoccupazione. "
                "Le variazioni circadiane, i pasti recenti e lo stato di idratazione possono "
                "influenzare la sideremia. Il medico interpreterà il risultato nel contesto "
                "dei sintomi e degli altri esami.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="Cause di sideremia bassa",
            body_html=(
                "<p>La <strong>carenza di ferro</strong> è la carenza nutrizionale più "
                "diffusa al mondo. Le principali cause di sideremia bassa sono:</p>"
                "<ul>"
                "<li><strong>Anemia sideropenica</strong> — apporto alimentare insufficiente "
                "o fabbisogno aumentato</li>"
                "<li><strong>Perdita di sangue</strong> — mestruazioni abbondanti, sanguinamento "
                "gastrointestinale (ulcera, polipi, cancro del colon)</li>"
                "<li><strong>Malassorbimento</strong> — celiachia, malattia infiammatoria "
                "cronica intestinale (MICI), chirurgia gastrica</li>"
                "<li><strong>Dieta vegetariana o vegana</strong> — minore assunzione di ferro eme</li>"
                "<li><strong>Gravidanza</strong> — aumento del volume ematico e fabbisogno "
                "fetale</li>"
                "<li><strong>Anemia da malattia cronica</strong> — l'infiammazione aumenta "
                "l'epcidina, trattenendo il ferro nelle riserve</li>"
                "</ul>"
                "<p>La sideremia da sola non basta per diagnosticare una carenza. Il medico "
                "valuterà ferritina, TIBC e saturazione della transferrina "
                "congiuntamente.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="Cause di sideremia alta",
            body_html=(
                "<p>Anche una sideremia elevata richiede attenzione medica. Le cause più "
                "comuni sono:</p>"
                "<ul>"
                "<li><strong>Emocromatosi ereditaria</strong> — malattia genetica con "
                "assorbimento eccessivo di ferro dall'intestino</li>"
                "<li><strong>Integrazione eccessiva di ferro</strong> — assunzione di "
                "integratori ad alto dosaggio senza supervisione medica</li>"
                "<li><strong>Anemia emolitica</strong> — distruzione prematura dei globuli "
                "rossi che rilascia ferro nel sangue</li>"
                "<li><strong>Malattia epatica</strong> — epatite o cirrosi possono elevare "
                "ferritina e sideremia</li>"
                "<li><strong>Trasfusioni multiple</strong> — ogni unità di sangue apporta "
                "circa 200–250 mg di ferro</li>"
                "<li><strong>Avvelenamento da ferro</strong> — ingestione accidentale di "
                "dosi elevate, particolarmente pericolosa nei bambini</li>"
                "</ul>"
                "<p>Il sovraccarico cronico di ferro porta a depositi negli organi "
                "(<em>emosiderosi</em>). La diagnosi precoce è fondamentale per prevenire "
                "danni irreversibili.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="Ferro vs. ferritina: qual è la differenza?",
            body_html=(
                "<p>La <strong>sideremia</strong> è un'istantanea del ferro circolante, "
                "legato alla transferrina. Oscilla significativamente nel corso della giornata "
                "e risente dei pasti, limitando la sua affidabilità come marcatore isolato.</p>"
                "<p>La <strong>ferritina</strong> riflette le riserve di ferro dell'organismo "
                "ed è un marcatore molto più stabile. Una ferritina bassa è praticamente "
                "la prova che le riserve sono esaurite. Tuttavia, essendo anche un "
                "<em>reattante di fase acuta</em>, può elevarsi in caso di infiammazione, "
                "infezione o malattia epatica — mascherando potenzialmente una carenza "
                "sottostante.</p>"
                "<p>Per una valutazione completa dello stato del ferro, entrambi i test "
                "devono essere interpretati insieme, idealmente con TIBC e saturazione della "
                "transferrina. Questa combinazione permette al medico di distinguere tra "
                "anemia sideropenica, anemia da malattia cronica e sovraccarico di ferro.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC e saturazione della transferrina",
            body_html=(
                "<p>La <strong>TIBC (Capacità Totale di Legame del Ferro)</strong> misura la "
                "quantità massima di ferro che la transferrina può trasportare. Nella carenza "
                "di ferro, l'organismo produce più transferrina e la TIBC sale; nel "
                "sovraccarico o nella malattia cronica, la TIBC scende.</p>"
                "<p>La <strong>saturazione della transferrina</strong> si calcola come: "
                "<em>(Sideremia ÷ TIBC) × 100</em>. In soggetti sani si colloca "
                "tipicamente tra il 20% e il 50%. Al di sotto del 20% si sospetta carenza "
                "di ferro; al di sopra del 50% si sospetta sovraccarico, in particolare "
                "emocromatosi.</p>"
                "<p>Valutati insieme a sideremia e ferritina, questi marcatori formano un "
                "potente pannello diagnostico. Esempio: sideremia bassa + TIBC alta + "
                "ferritina bassa = anemia sideropenica; sideremia bassa + TIBC bassa + "
                "ferritina normale o elevata = anemia da malattia cronica.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi di ferro basso e alto",
            body_html=(
                "<p><strong>Sintomi di ferro basso:</strong> Stanchezza, pallore, dispnea da "
                "sforzo, unghie fragili, mani e piedi freddi, vertigini, cefalea e "
                "<em>pica</em> (desiderio di sostanze non alimentari come ghiaccio o terra). "
                "Nei casi gravi possono comparire tachicardia e dolore toracico.</p>"
                "<p><strong>Sintomi di ferro alto:</strong> Dolore articolare (soprattutto "
                "alle mani), stanchezza cronica, dolore addominale, colorazione bronzea "
                "della pelle, epatomegalia e compromissione della funzionalità epatica. "
                "L'emocromatosi non trattata può progredire verso diabete, cardiomiopatia "
                "e cirrosi.</p>"
                "<p>In entrambi i casi, i sintomi tendono a svilupparsi gradualmente e "
                "vengono facilmente trascurati. Esami del sangue regolari — specialmente "
                "per chi ha familiarità — sono il modo più affidabile per individuare "
                "precocemente le anomalie.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Consultate un medico se la vostra sideremia è fuori dall'intervallo di "
                "riferimento. Una valutazione tempestiva è particolarmente importante se:</p>"
                "<ul>"
                "<li>Avvertite stanchezza inspiegabile, pallore o dispnea</li>"
                "<li>Avete familiarità per emocromatosi</li>"
                "<li>Avete mestruazioni abbondanti o sospettate sanguinamento digestivo</li>"
                "<li>La ferritina è molto bassa o molto alta</li>"
                "<li>La saturazione della transferrina è sotto il 20% o sopra il 50%</li>"
                "</ul>"
                "<p>Il medico potrà prescrivere esami aggiuntivi — emocromo, striscio "
                "periferico, B12, folati, test genetico HFE — per identificare la causa. "
                "Diagnosi e trattamento precoci sono essenziali per prevenire "
                "complicanze.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya può aiutarti",
            body_html=(
                "<p>Comprendere i risultati degli esami del sangue può essere talvolta "
                "complicato. <strong>Norya</strong> vi consente di caricare il vostro referto "
                "e ricevere in pochi minuti un riepilogo di salute strutturato e facile da "
                "capire. I vostri risultati vengono confrontati con gli intervalli di "
                "riferimento e spiegati in un linguaggio semplice.</p>"
                "<p>Norya non è uno strumento diagnostico — il suo scopo è prepararvi a un "
                "colloquio più informato con il medico. "
                "<a href=\"/analyze\">Iniziate l'analisi con Norya</a> e scoprite cosa "
                "significano i vostri risultati. Per i dettagli sui prezzi, visitate la "
                "nostra <a href=\"/pricing\">pagina prezzi</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il '
                'parere o la diagnosi medica.</strong> Discutete sempre i risultati con un '
                'professionista sanitario. '
                '<a href="/analyze">Inizia l\'analisi con Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW (RTL)
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="בדיקת ברזל בדם: מה המשמעות של תוצאה נמוכה או גבוהה?",
            body_html=(
                "<p>כאשר תוצאות בדיקת הדם שלכם מראות רמת <strong>ברזל בסרום</strong> מחוץ "
                "לטווח הנורמה, זה טבעי להיות מודאגים. ברזל הוא מינרל חיוני לייצור "
                "המוגלובין, העברת חמצן, מטבוליזם אנרגטי ותפקוד מערכת החיסון. מדריך זה "
                "מסביר מה מודדת בדיקת ברזל בסרום, כיצד לפרש את התוצאות ומתי לפנות "
                "לרופא.</p>"
                "<p>המטרה שלנו אינה לאבחן — אלא להכין אתכם לשיחה מושכלת עם הרופא. "
                "רמת הברזל בסרום צריכה תמיד להיבדק יחד עם <em>פריטין</em>, "
                "<em>TIBC</em> ו<em>רוויון טרנספרין</em> לקבלת תמונה מלאה.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="מהי בדיקת ברזל בסרום?",
            body_html=(
                "<p><strong>בדיקת ברזל בסרום</strong> מודדת את כמות הברזל הזורמת בדם, "
                "הקשורה לחלבון ההעברה <em>טרנספרין</em>. רק חלק קטן מהברזל הכולל בגוף "
                "נמצא בסרום; רובו מושקע בהמוגלובין בתוך תאי דם אדומים או מאוחסן "
                "כפריטין בכבד, בטחול ובמח העצם.</p>"
                "<p>התוצאות מדווחות בדרך כלל ב-<strong>μg/dL</strong>. רמת הברזל בסרום "
                "משתנה במהלך היום — גבוהה יותר בבוקר, נמוכה יותר בערב — ומושפעת "
                "מארוחות אחרונות. לכן הבדיקה מבוצעת בדרך כלל בבוקר בצום.</p>"
                "<p>הברזל בסרום אינפורמטיבי במיוחד כאשר מפרשים אותו יחד עם "
                "<em>פריטין</em>, <em>TIBC</em> ו<em>רוויון טרנספרין</em>, שיחד "
                "נותנים תמונה שלמה יותר של מטבוליזם הברזל.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="כיצד פועל מטבוליזם הברזל?",
            body_html=(
                "<p>ברזל נספג בעיקר ב<strong>תריסריון</strong> (החלק הראשון של המעי "
                "הדק). ברזל הֵם ממקורות מן החי נספג ביעילות רבה יותר מברזל שאינו הֵם "
                "ממקורות צמחיים. לאחר הספיגה, הברזל עובר לזרם הדם ונקשר "
                "ל<em>טרנספרין</em>, שמעביר אותו לרקמות הזקוקות לו — בעיקר למח "
                "העצם לסינתזה של המוגלובין.</p>"
                "<p>עודף ברזל מאוחסן כ<em>פריטין</em> בכבד, בטחול ובמח העצם. לגוף "
                "אין מנגנון הפרשה פעיל לברזל; אובדן מתרחש בעיקר דרך תאי מעי "
                "שנשרים, מחזור חודשי ודימומים קטנים. איזון הברזל מווסת על ידי "
                "<strong>הפצידין</strong>, הורמון כבדי שמעכב ספיגה כשהמאגרים מלאים "
                "או בנוכחות דלקת.</p>"
                "<p>מעבר להמוגלובין, ברזל חיוני ל<em>מיוגלובין</em>, אנזימי "
                "ציטוכרום וסינתזה של DNA. הן מחסור והן עודף עלולים לגרום לבעיות "
                "בריאותיות חמורות.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי נורמה לפרמטרים של ברזל",
            body_html=(
                "<p>טווחי ההתייחסות עשויים להשתנות מעט בין מעבדות. הטבלה הבאה מסכמת "
                "ערכים מקובלים. השוו תמיד את התוצאה שלכם לטווח המודפס בדוח "
                "המעבדה שלכם.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>פרמטר</th>'
                f'<th {_TH}>גברים</th>'
                f'<th {_TH}>נשים</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>ברזל בסרום</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>רוויון טרנספרין</td><td {_TD}>20–50%</td><td {_TD}>15–50%</td></tr>'
                f'<tr><td {_TD}>פריטין</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>תוצאה בודדת מעט מחוץ לטווח אינה תמיד סיבה לדאגה. תנודות "
                "יממתיות, ארוחות אחרונות ומצב הידרציה יכולים להשפיע. הרופא שלכם "
                "יפרש את התוצאה בהקשר של הסימפטומים וממצאי מעבדה נוספים.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="סיבות לברזל נמוך בסרום",
            body_html=(
                "<p><strong>מחסור בברזל</strong> הוא החסר התזונתי השכיח ביותר בעולם. "
                "הגורמים העיקריים לברזל נמוך בסרום כוללים:</p>"
                "<ul>"
                "<li><strong>אנמיה מחוסר ברזל</strong> — צריכה תזונתית לא מספקת או "
                "דרישה מוגברת</li>"
                "<li><strong>איבוד דם</strong> — מחזורים חודשיים כבדים, דימום "
                "במערכת העיכול (כיב, פוליפים, סרטן המעי הגס)</li>"
                "<li><strong>חוסר ספיגה</strong> — צליאק, מחלת מעי דלקתית (IBD), "
                "ניתוח קיבה</li>"
                "<li><strong>תזונה צמחונית או טבעונית</strong> — פחות ברזל הֵם</li>"
                "<li><strong>הריון</strong> — נפח דם מוגדל ודרישות העובר</li>"
                "<li><strong>אנמיה של מחלה כרונית</strong> — דלקת מעלה הפצידין "
                "ולוכדת ברזל במאגרים</li>"
                "</ul>"
                "<p>ברזל בסרום לבד אינו מספיק לאבחון מחסור. הרופא יעריך פריטין, "
                "TIBC ורוויון טרנספרין יחד.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="סיבות לברזל גבוה בסרום",
            body_html=(
                "<p>גם רמת ברזל גבוהה בסרום מצריכה הערכה רפואית. הגורמים השכיחים "
                "כוללים:</p>"
                "<ul>"
                "<li><strong>המוכרומטוזיס תורשתי</strong> — הפרעה גנטית הגורמת "
                "לספיגת יתר של ברזל מהמעי</li>"
                "<li><strong>תוסף ברזל מוגזם</strong> — נטילת מינונים גבוהים ללא "
                "פיקוח רפואי</li>"
                "<li><strong>אנמיה המוליטית</strong> — הרס מוקדם של תאי דם אדומים "
                "משחרר ברזל לדם</li>"
                "<li><strong>מחלת כבד</strong> — דלקת כבד או שחמת עלולות להעלות "
                "פריטין וברזל בסרום</li>"
                "<li><strong>עירויי דם חוזרים</strong> — כל יחידת דם מוסיפה כ-200–250 "
                "מ\"ג ברזל</li>"
                "<li><strong>הרעלת ברזל</strong> — בליעה מקרית של מינונים גבוהים, "
                "מסוכנת במיוחד בילדים</li>"
                "</ul>"
                "<p>עומס ברזל כרוני מוביל לשקיעת ברזל באיברים (<em>המוזידרוזיס</em>). "
                "גילוי מוקדם חיוני למניעת נזק בלתי הפיך.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="ברזל לעומת פריטין: מה ההבדל?",
            body_html=(
                "<p><strong>ברזל בסרום</strong> הוא תמונת מצב של הברזל הזורם ברגע "
                "הבדיקה, קשור לטרנספרין. הוא משתנה משמעותית במהלך היום ומושפע "
                "מארוחות, מה שמגביל את מהימנותו כסמן בודד.</p>"
                "<p><strong>פריטין</strong> משקף את מאגרי הברזל בגוף ומהווה סמן "
                "יציב הרבה יותר. פריטין נמוך הוא כמעט הוכחה ודאית שהמאגרים "
                "מרוקנים. עם זאת, כ<em>חלבון פאזה חריפה</em>, פריטין עלול לעלות "
                "בדלקת, זיהום ומחלת כבד — ולהסתיר מחסור בסיסי.</p>"
                "<p>להערכה מלאה של מצב הברזל, שני הבדיקות צריכות להתפרש יחד, "
                "באופן אידיאלי עם TIBC ורוויון טרנספרין. שילוב זה מאפשר לרופא "
                "להבחין בין אנמיה מחוסר ברזל, אנמיה של מחלה כרונית ועומס ברזל.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC ורוויון טרנספרין",
            body_html=(
                "<p><strong>TIBC (כושר קשירת ברזל כולל)</strong> מודד את כמות הברזל "
                "המרבית שטרנספרין בדם יכול לשאת. במחסור ברזל, הגוף מייצר יותר "
                "טרנספרין ו-TIBC עולה; בעומס ברזל או מחלה כרונית, TIBC יורד.</p>"
                "<p><strong>רוויון טרנספרין</strong> מחושב כ: "
                "<em>(ברזל בסרום ÷ TIBC) × 100</em>. באנשים בריאים הוא נע "
                "בדרך כלל בין 20% ל-50%. מתחת ל-20% מרמז על מחסור בברזל; "
                "מעל 50% מעלה חשד לעומס ברזל, במיוחד המוכרומטוזיס.</p>"
                "<p>בהערכה יחד עם ברזל בסרום ופריטין, סמנים אלו מהווים פאנל "
                "אבחנתי רב-עוצמה. לדוגמה: ברזל בסרום נמוך + TIBC גבוה + פריטין "
                "נמוך = אנמיה מחוסר ברזל; ברזל בסרום נמוך + TIBC נמוך + פריטין "
                "תקין או מוגבה = אנמיה של מחלה כרונית.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של ברזל נמוך וגבוה",
            body_html=(
                "<p><strong>תסמינים של ברזל נמוך:</strong> עייפות, חיוורון, קוצר "
                "נשימה במאמץ, ציפורניים שבירות, ידיים ורגליים קרות, סחרחורת, "
                "כאבי ראש ו<em>פיקה</em> (תשוקה לחומרים שאינם מזון כמו קרח או "
                "חימר). במקרים חמורים עלולים להופיע טכיקרדיה וכאב בחזה.</p>"
                "<p><strong>תסמינים של ברזל גבוה:</strong> כאבי מפרקים (בעיקר "
                "בידיים), עייפות כרונית, כאבי בטן, גוון עור ברונזי, הגדלת כבד "
                "ופגיעה בתפקוד הכבד. המוכרומטוזיס שלא מטופל עלול להתקדם לסוכרת, "
                "קרדיומיופתיה ושחמת.</p>"
                "<p>בשני הכיוונים, התסמינים נוטים להתפתח בהדרגה ולהתעלם מהם. "
                "בדיקות דם סדירות — במיוחד למי שיש היסטוריה משפחתית — הן "
                "הדרך האמינה ביותר לגלות בעיות מוקדם.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>יש לפנות לרופא אם רמת הברזל בסרום מחוץ לטווח ההתייחסות. "
                "הערכה מהירה חשובה במיוחד אם:</p>"
                "<ul>"
                "<li>אתם חווים עייפות בלתי מוסברת, חיוורון או קוצר נשימה</li>"
                "<li>יש היסטוריה משפחתית של המוכרומטוזיס</li>"
                "<li>יש מחזורים חודשיים כבדים או חשד לדימום במערכת העיכול</li>"
                "<li>הפריטין נמוך מאוד או גבוה מאוד</li>"
                "<li>רוויון טרנספרין מתחת ל-20% או מעל 50%</li>"
                "</ul>"
                "<p>הרופא עשוי להזמין בדיקות נוספות — ספירת דם, משטח פריפרי, "
                "B12, חומצה פולית, בדיקות גנטיות HFE — לזיהוי הגורם. אבחון "
                "וטיפול מוקדמים חיוניים למניעת סיבוכים.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד Norya יכול לעזור?",
            body_html=(
                "<p>הבנת תוצאות בדיקות דם יכולה להיות לעיתים מבלבלת. "
                "<strong>Norya</strong> מאפשר לכם להעלות את דוח הבדיקה שלכם "
                "ולקבל תוך דקות סיכום בריאות מובנה וקל להבנה. התוצאות שלכם "
                "מושוות לטווחי ההתייחסות ומוסברות בשפה פשוטה.</p>"
                "<p>Norya אינו כלי אבחון — מטרתו להכין אתכם לשיחה מושכלת "
                "עם הרופא. <a href=\"/analyze\">התחילו את הניתוח עם Norya</a> "
                "וגלו מה המשמעות של התוצאות שלכם. לפרטי מחירים, בקרו "
                "ב<a href=\"/pricing\">דף המחירים</a> שלנו.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הודעה",
            body_html=(
                '<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון '
                'רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. '
                '<a href="/analyze">התחל ניתוח עם Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="सीरम आयरन रक्त परीक्षण: कम या अधिक होने का क्या मतलब है?",
            body_html=(
                "<p>जब आपकी रक्त जांच रिपोर्ट में <strong>सीरम आयरन</strong> का स्तर "
                "सामान्य सीमा से बाहर दिखता है, तो चिंतित होना स्वाभाविक है। आयरन "
                "हीमोग्लोबिन उत्पादन, ऑक्सीजन परिवहन, ऊर्जा चयापचय और प्रतिरक्षा "
                "प्रणाली के लिए एक आवश्यक खनिज है। यह मार्गदर्शिका बताती है कि "
                "सीरम आयरन टेस्ट क्या मापता है, परिणामों की व्याख्या कैसे करें "
                "और डॉक्टर से कब मिलें।</p>"
                "<p>हमारा उद्देश्य निदान करना नहीं है — बल्कि आपको डॉक्टर से "
                "बेहतर चर्चा के लिए तैयार करना है। सीरम आयरन का मूल्यांकन हमेशा "
                "<em>फेरिटिन</em>, <em>TIBC</em> और <em>ट्रांसफेरिन संतृप्ति</em> "
                "के साथ किया जाना चाहिए।</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="सीरम आयरन टेस्ट क्या है?",
            body_html=(
                "<p><strong>सीरम आयरन टेस्ट</strong> रक्त में परिवहन प्रोटीन "
                "<em>ट्रांसफेरिन</em> से बंधे हुए आयरन की मात्रा को मापता है। "
                "शरीर के कुल आयरन का केवल एक छोटा हिस्सा सीरम में होता है; "
                "अधिकांश हीमोग्लोबिन में या यकृत, प्लीहा और अस्थि मज्जा में "
                "फेरिटिन के रूप में संग्रहित होता है।</p>"
                "<p>परिणाम आमतौर पर <strong>μg/dL</strong> में बताए जाते हैं। "
                "सीरम आयरन का स्तर दिन भर बदलता रहता है — सुबह अधिक और शाम को "
                "कम होता है — और हाल के भोजन से प्रभावित होता है। इसलिए यह "
                "परीक्षण आमतौर पर सुबह खाली पेट किया जाता है।</p>"
                "<p>सीरम आयरन सबसे उपयोगी तब होता है जब इसे <em>फेरिटिन</em>, "
                "<em>TIBC</em> और <em>ट्रांसफेरिन संतृप्ति</em> के साथ मिलाकर "
                "देखा जाए, जो मिलकर आयरन चयापचय की पूरी तस्वीर प्रस्तुत "
                "करते हैं।</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="आयरन चयापचय कैसे काम करता है?",
            body_html=(
                "<p>आयरन मुख्य रूप से <strong>ड्यूओडेनम</strong> (छोटी आंत का पहला "
                "भाग) में अवशोषित होता है। पशु स्रोतों से मिलने वाला हीम-आयरन, "
                "पौधों से मिलने वाले नॉन-हीम आयरन की तुलना में बहुत अधिक कुशलता "
                "से अवशोषित होता है। अवशोषण के बाद, आयरन रक्तप्रवाह में प्रवेश "
                "करता है और <em>ट्रांसफेरिन</em> से जुड़ जाता है, जो इसे जरूरतमंद "
                "ऊतकों — विशेषकर अस्थि मज्जा — तक पहुंचाता है।</p>"
                "<p>अतिरिक्त आयरन यकृत, प्लीहा और अस्थि मज्जा में <em>फेरिटिन</em> "
                "के रूप में संग्रहित होता है। शरीर में आयरन के सक्रिय उत्सर्जन का "
                "कोई मार्ग नहीं है; हानि मुख्य रूप से आंतों की कोशिकाओं के झड़ने, "
                "मासिक धर्म और मामूली रक्तस्राव से होती है। आयरन संतुलन "
                "<strong>हेप्सिडिन</strong> द्वारा नियंत्रित होता है, जो यकृत से "
                "निकलने वाला एक हार्मोन है।</p>"
                "<p>हीमोग्लोबिन के अलावा, आयरन <em>मायोग्लोबिन</em>, साइटोक्रोम "
                "एंजाइम और DNA संश्लेषण के लिए भी आवश्यक है। कमी और अधिकता "
                "दोनों ही गंभीर स्वास्थ्य समस्याएं पैदा कर सकती हैं।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="आयरन के सामान्य मान",
            body_html=(
                "<p>संदर्भ सीमाएं प्रयोगशालाओं के बीच थोड़ी भिन्न हो सकती हैं। "
                "नीचे दी गई तालिका सामान्य रूप से स्वीकृत मानों को सारांशित "
                "करती है। अपने परिणाम की तुलना हमेशा अपनी प्रयोगशाला रिपोर्ट पर "
                "दी गई सीमा से करें।</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>पैरामीटर</th>'
                f'<th {_TH}>पुरुष</th>'
                f'<th {_TH}>महिलाएं</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>सीरम आयरन</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>ट्रांसफेरिन संतृप्ति</td><td {_TD}>20–50%</td><td {_TD}>15–50%</td></tr>'
                f'<tr><td {_TD}>फेरिटिन</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>सीमा से थोड़ा बाहर एक परिणाम हमेशा चिंता का कारण नहीं "
                "होता। दैनिक उतार-चढ़ाव, हाल का भोजन और जलयोजन स्थिति सीरम "
                "आयरन को प्रभावित कर सकते हैं। आपके डॉक्टर लक्षणों और अन्य "
                "प्रयोगशाला निष्कर्षों के संदर्भ में परिणाम की व्याख्या करेंगे।</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="सीरम आयरन कम होने के कारण",
            body_html=(
                "<p><strong>आयरन की कमी</strong> दुनिया भर में सबसे आम पोषक तत्व "
                "की कमी है। सीरम आयरन कम होने के मुख्य कारण:</p>"
                "<ul>"
                "<li><strong>आयरन की कमी से एनीमिया</strong> — अपर्याप्त आहार "
                "सेवन या बढ़ी हुई मांग</li>"
                "<li><strong>रक्त हानि</strong> — भारी मासिक धर्म, गैस्ट्रोइंटेस्टाइनल "
                "रक्तस्राव (अल्सर, पॉलीप्स, कोलन कैंसर)</li>"
                "<li><strong>कुअवशोषण</strong> — सीलिएक रोग, सूजन आंत्र रोग (IBD), "
                "गैस्ट्रिक बाईपास सर्जरी</li>"
                "<li><strong>शाकाहारी या वीगन आहार</strong> — कम हीम-आयरन सेवन</li>"
                "<li><strong>गर्भावस्था</strong> — रक्त मात्रा में वृद्धि और भ्रूण "
                "की आवश्यकताएं</li>"
                "<li><strong>पुरानी बीमारी का एनीमिया</strong> — सूजन हेप्सिडिन "
                "बढ़ाती है, आयरन को भंडार में रोक कर रखती है</li>"
                "</ul>"
                "<p>आयरन की कमी का निदान करने के लिए सीरम आयरन अकेला पर्याप्त "
                "नहीं है। डॉक्टर फेरिटिन, TIBC और ट्रांसफेरिन संतृप्ति का "
                "एक साथ मूल्यांकन करेंगे।</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="सीरम आयरन अधिक होने के कारण",
            body_html=(
                "<p>सीरम आयरन का बढ़ा हुआ स्तर भी चिकित्सकीय ध्यान की आवश्यकता "
                "रखता है। सामान्य कारण:</p>"
                "<ul>"
                "<li><strong>वंशानुगत हेमोक्रोमैटोसिस</strong> — आंत से अत्यधिक "
                "आयरन अवशोषण कराने वाला आनुवंशिक विकार</li>"
                "<li><strong>अत्यधिक आयरन सप्लीमेंटेशन</strong> — बिना चिकित्सकीय "
                "देखरेख के उच्च खुराक लेना</li>"
                "<li><strong>हेमोलिटिक एनीमिया</strong> — लाल रक्त कोशिकाओं का "
                "समय से पहले विनाश</li>"
                "<li><strong>यकृत रोग</strong> — हेपेटाइटिस या सिरोसिस</li>"
                "<li><strong>बहुविध रक्त आधान</strong> — प्रत्येक इकाई लगभग "
                "200–250 मिग्रा आयरन जोड़ती है</li>"
                "<li><strong>आयरन विषाक्तता</strong> — आकस्मिक उच्च खुराक सेवन, "
                "बच्चों में विशेष रूप से खतरनाक</li>"
                "</ul>"
                "<p>दीर्घकालिक आयरन अधिभार अंगों में आयरन जमाव "
                "(<em>हीमोसाइडरोसिस</em>) का कारण बनता है। अपरिवर्तनीय अंग "
                "क्षति को रोकने के लिए शीघ्र पहचान महत्वपूर्ण है।</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="आयरन बनाम फेरिटिन: क्या अंतर है?",
            body_html=(
                "<p><strong>सीरम आयरन</strong> ट्रांसफेरिन से बंधे हुए वर्तमान "
                "में रक्त में घूम रहे आयरन का एक स्नैपशॉट है। यह दिन भर "
                "काफी बदलता रहता है और भोजन से प्रभावित होता है, जिससे अकेले "
                "इसकी विश्वसनीयता सीमित होती है।</p>"
                "<p><strong>फेरिटिन</strong> शरीर के आयरन भंडार को दर्शाता है "
                "और बहुत अधिक स्थिर मार्कर है। कम फेरिटिन लगभग निश्चित "
                "प्रमाण है कि भंडार समाप्त हो गए हैं। हालांकि, "
                "<em>तीव्र-चरण अभिकारक</em> होने के कारण, फेरिटिन सूजन, "
                "संक्रमण और यकृत रोग में बढ़ सकता है — संभावित रूप से "
                "अंतर्निहित कमी को छुपा सकता है।</p>"
                "<p>आयरन स्थिति के पूर्ण मूल्यांकन के लिए, दोनों परीक्षणों की "
                "व्याख्या TIBC और ट्रांसफेरिन संतृप्ति के साथ मिलकर की जानी "
                "चाहिए। यह संयोजन डॉक्टर को आयरन की कमी से एनीमिया, "
                "पुरानी बीमारी के एनीमिया और आयरन अधिभार में भेद करने में "
                "सक्षम बनाता है।</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC और ट्रांसफेरिन संतृप्ति की व्याख्या",
            body_html=(
                "<p><strong>TIBC (कुल आयरन-बाइंडिंग क्षमता)</strong> रक्त में "
                "ट्रांसफेरिन द्वारा वहन की जा सकने वाली अधिकतम आयरन मात्रा "
                "को मापता है। आयरन की कमी में, शरीर अधिक ट्रांसफेरिन बनाता "
                "है और TIBC बढ़ जाता है; आयरन अधिभार या पुरानी बीमारी में, "
                "TIBC घट जाता है।</p>"
                "<p><strong>ट्रांसफेरिन संतृप्ति</strong> की गणना इस प्रकार की "
                "जाती है: <em>(सीरम आयरन ÷ TIBC) × 100</em>। स्वस्थ व्यक्तियों "
                "में यह आमतौर पर 20% से 50% के बीच होती है। 20% से नीचे "
                "आयरन की कमी का सुझाव देता है; 50% से ऊपर आयरन अधिभार, "
                "विशेष रूप से हेमोक्रोमैटोसिस की चिंता पैदा करता है।</p>"
                "<p>सीरम आयरन और फेरिटिन के साथ मूल्यांकन करने पर, ये मार्कर "
                "एक शक्तिशाली नैदानिक पैनल बनाते हैं। उदाहरण: कम सीरम आयरन "
                "+ उच्च TIBC + कम फेरिटिन = आयरन की कमी से एनीमिया; कम सीरम "
                "आयरन + कम TIBC + सामान्य/ऊंचा फेरिटिन = पुरानी बीमारी का "
                "एनीमिया।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="कम और अधिक आयरन के लक्षण",
            body_html=(
                "<p><strong>कम आयरन के लक्षण:</strong> थकान, पीलापन, परिश्रम "
                "पर सांस फूलना, भंगुर नाखून, ठंडे हाथ-पैर, चक्कर आना, सिरदर्द "
                "और <em>पिका</em> (बर्फ या मिट्टी जैसी गैर-खाद्य वस्तुओं की "
                "लालसा)। गंभीर मामलों में टैकीकार्डिया और सीने में दर्द हो "
                "सकता है।</p>"
                "<p><strong>अधिक आयरन के लक्षण:</strong> जोड़ों का दर्द (विशेषकर "
                "हाथों में), पुरानी थकान, पेट दर्द, त्वचा का कांस्य रंग, यकृत "
                "वृद्धि और बिगड़ा हुआ यकृत कार्य। अनुपचारित हेमोक्रोमैटोसिस "
                "मधुमेह, कार्डियोमायोपैथी और सिरोसिस तक बढ़ सकता है।</p>"
                "<p>दोनों दिशाओं में लक्षण धीरे-धीरे विकसित होते हैं और आसानी "
                "से अनदेखा किए जा सकते हैं। नियमित रक्त परीक्षण — विशेषकर "
                "पारिवारिक इतिहास वालों के लिए — समस्याओं को जल्दी पकड़ने का "
                "सबसे विश्वसनीय तरीका है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>यदि आपका सीरम आयरन संदर्भ सीमा से बाहर है तो डॉक्टर से "
                "परामर्श करें। विशेष रूप से निम्नलिखित स्थितियों में शीघ्र "
                "चिकित्सकीय मूल्यांकन की सिफारिश की जाती है:</p>"
                "<ul>"
                "<li>अस्पष्टीकृत थकान, पीलापन या सांस फूलना</li>"
                "<li>हेमोक्रोमैटोसिस का पारिवारिक इतिहास</li>"
                "<li>भारी मासिक धर्म या गैस्ट्रोइंटेस्टाइनल रक्तस्राव का संदेह</li>"
                "<li>फेरिटिन बहुत कम या बहुत अधिक</li>"
                "<li>ट्रांसफेरिन संतृप्ति 20% से नीचे या 50% से ऊपर</li>"
                "</ul>"
                "<p>डॉक्टर अतिरिक्त परीक्षण — पूर्ण रक्त गणना, परिधीय स्मीयर, "
                "B12, फोलेट, HFE आनुवंशिक परीक्षण — का आदेश दे सकते हैं। "
                "शीघ्र निदान और उपचार जटिलताओं को रोकने के लिए आवश्यक है।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya कैसे मदद कर सकता है?",
            body_html=(
                "<p>रक्त परीक्षण के परिणामों को समझना कभी-कभी भ्रमित करने वाला "
                "हो सकता है। <strong>Norya</strong> आपको अपनी रक्त जांच रिपोर्ट "
                "अपलोड करने और मिनटों में एक संरचित, समझने में आसान स्वास्थ्य "
                "सारांश प्राप्त करने की अनुमति देता है। आपके परिणामों की तुलना "
                "संदर्भ सीमाओं से की जाती है और सरल भाषा में समझाया जाता है।</p>"
                "<p>Norya एक नैदानिक उपकरण नहीं है — इसका उद्देश्य आपको "
                "डॉक्टर के साथ अधिक जानकारीपूर्ण बातचीत के लिए तैयार करना "
                "है। <a href=\"/analyze\">Norya से विश्लेषण शुरू करें</a> और "
                "जानें कि आपके परिणामों का क्या अर्थ है। मूल्य विवरण के लिए "
                "हमारा <a href=\"/pricing\">मूल्य निर्धारण पृष्ठ</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान '
                'का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से '
                'चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC (RTL)
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="تحليل الحديد في الدم: ماذا يعني ارتفاعه أو انخفاضه؟",
            body_html=(
                "<p>عندما تُظهر نتائج تحليل الدم أن مستوى <strong>الحديد في "
                "المصل</strong> خارج النطاق الطبيعي، فمن الطبيعي أن تشعر بالقلق. "
                "الحديد معدن أساسي لإنتاج الهيموجلوبين ونقل الأكسجين واستقلاب "
                "الطاقة ووظيفة المناعة. يشرح هذا الدليل ما يقيسه تحليل الحديد "
                "في المصل، وكيفية تفسير النتائج، ومتى يجب مراجعة الطبيب.</p>"
                "<p>هدفنا ليس التشخيص — بل إعدادك لمحادثة أكثر وعياً مع طبيبك. "
                "يجب دائماً تقييم الحديد في المصل مع <em>الفيريتين</em> و"
                "<em>TIBC</em> و<em>تشبع الترانسفيرين</em> للحصول على صورة "
                "كاملة.</p>"
            ),
        ),
        Section(
            id="what-is-serum-iron", level=2,
            heading="ما هو تحليل الحديد في المصل؟",
            body_html=(
                "<p><strong>تحليل الحديد في المصل</strong> يقيس كمية الحديد "
                "الموجودة في الدم والمرتبطة ببروتين النقل <em>الترانسفيرين</em>. "
                "جزء صغير فقط من إجمالي حديد الجسم يوجد في المصل؛ الجزء الأكبر "
                "مدمج في الهيموجلوبين داخل كريات الدم الحمراء أو مخزّن على "
                "شكل فيريتين في الكبد والطحال ونخاع العظم.</p>"
                "<p>تُعبَّر النتائج عادةً بوحدة <strong>μg/dL</strong>. يتذبذب "
                "مستوى الحديد في المصل خلال اليوم — أعلى في الصباح وأقل في "
                "المساء — ويتأثر بالوجبات الأخيرة. لذلك يُجرى التحليل عادةً "
                "صباحاً على الريق.</p>"
                "<p>الحديد في المصل يكون أكثر فائدة عند تفسيره مع <em>الفيريتين</em> "
                "و<em>TIBC</em> و<em>تشبع الترانسفيرين</em>، التي تعطي معاً "
                "صورة أكمل عن استقلاب الحديد.</p>"
            ),
        ),
        Section(
            id="iron-metabolism", level=2,
            heading="كيف يعمل استقلاب الحديد؟",
            body_html=(
                "<p>يُمتص الحديد بشكل رئيسي في <strong>الاثني عشر</strong> "
                "(الجزء الأول من الأمعاء الدقيقة). الحديد الهيمي من المصادر "
                "الحيوانية يُمتص بكفاءة أعلى بكثير من الحديد غير الهيمي من "
                "المصادر النباتية. بعد الامتصاص، يدخل الحديد مجرى الدم ويرتبط "
                "بـ<em>الترانسفيرين</em>، الذي ينقله إلى الأنسجة التي تحتاجه — "
                "خاصة نخاع العظم لتصنيع الهيموجلوبين.</p>"
                "<p>يُخزَّن الحديد الزائد على شكل <em>فيريتين</em> في الكبد "
                "والطحال ونخاع العظم. لا يملك الجسم آلية إفراز نشطة للحديد؛ "
                "الفقد يحدث عبر تقشّر خلايا الأمعاء والحيض والنزيف البسيط. "
                "يُنظَّم توازن الحديد عند نقطة الامتصاص بواسطة "
                "<strong>الهيبسيدين</strong>، وهو هرمون كبدي يقلل الامتصاص "
                "عندما تكون المخازن ممتلئة أو في حالة الالتهاب.</p>"
                "<p>بالإضافة إلى الهيموجلوبين، الحديد ضروري لـ<em>الميوجلوبين</em> "
                "وإنزيمات السيتوكروم وتصنيع الحمض النووي. كل من النقص والفائض "
                "يمكن أن يكون له عواقب صحية خطيرة.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية لمعايير الحديد",
            body_html=(
                "<p>قد تختلف النطاقات المرجعية قليلاً بين المختبرات. يلخّص الجدول "
                "أدناه القيم المقبولة عموماً. قارن دائماً نتيجتك بالنطاق المطبوع "
                "في تقرير مختبرك.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>المعيار</th>'
                f'<th {_TH}>الرجال</th>'
                f'<th {_TH}>النساء</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>الحديد في المصل</td><td {_TD}>65–175 μg/dL</td><td {_TD}>50–170 μg/dL</td></tr>'
                f'<tr><td {_TD}>TIBC</td><td {_TD}>250–370 μg/dL</td><td {_TD}>250–370 μg/dL</td></tr>'
                f'<tr><td {_TD}>تشبع الترانسفيرين</td><td {_TD}>20–50%</td><td {_TD}>15–50%</td></tr>'
                f'<tr><td {_TD}>الفيريتين</td><td {_TD}>20–250 ng/mL</td><td {_TD}>10–120 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>نتيجة واحدة خارج النطاق بقليل ليست دائماً مدعاة للقلق. "
                "التذبذبات اليومية والوجبات الأخيرة وحالة الترطيب يمكن أن تؤثر "
                "على الحديد في المصل. سيفسّر طبيبك النتيجة في سياق أعراضك "
                "ونتائج المختبر الأخرى.</p>"
            ),
        ),
        Section(
            id="low-iron-causes", level=2,
            heading="أسباب انخفاض الحديد في المصل",
            body_html=(
                "<p><strong>نقص الحديد</strong> هو أكثر حالات نقص العناصر الغذائية "
                "شيوعاً في العالم. الأسباب الرئيسية لانخفاض الحديد في المصل:</p>"
                "<ul>"
                "<li><strong>فقر الدم بسبب نقص الحديد</strong> — تناول غذائي "
                "غير كافٍ أو طلب متزايد</li>"
                "<li><strong>فقدان الدم</strong> — الحيض الغزير، النزيف المعدي "
                "المعوي (قرحة، سلائل، سرطان القولون)</li>"
                "<li><strong>سوء الامتصاص</strong> — الداء البطني، مرض الأمعاء "
                "الالتهابي (IBD)، جراحة المعدة</li>"
                "<li><strong>النظام الغذائي النباتي</strong> — تناول أقل من الحديد "
                "الهيمي</li>"
                "<li><strong>الحمل</strong> — زيادة حجم الدم واحتياجات الجنين</li>"
                "<li><strong>فقر الدم المصاحب للأمراض المزمنة</strong> — الالتهاب "
                "يرفع الهيبسيدين ويحبس الحديد في المخازن</li>"
                "</ul>"
                "<p>الحديد في المصل وحده لا يكفي لتشخيص نقص الحديد. سيقيّم "
                "طبيبك الفيريتين وTIBC وتشبع الترانسفيرين معاً.</p>"
            ),
        ),
        Section(
            id="high-iron-causes", level=2,
            heading="أسباب ارتفاع الحديد في المصل",
            body_html=(
                "<p>ارتفاع الحديد في المصل يستوجب أيضاً تقييماً طبياً. "
                "الأسباب الشائعة تشمل:</p>"
                "<ul>"
                "<li><strong>داء ترسب الأصبغة الدموية الوراثي</strong> — اضطراب "
                "جيني يسبب امتصاصاً مفرطاً للحديد من الأمعاء</li>"
                "<li><strong>الإفراط في تناول مكملات الحديد</strong> — جرعات "
                "عالية دون إشراف طبي</li>"
                "<li><strong>فقر الدم الانحلالي</strong> — التدمير المبكر لكريات "
                "الدم الحمراء يطلق الحديد في الدم</li>"
                "<li><strong>أمراض الكبد</strong> — التهاب الكبد أو تشمّعه</li>"
                "<li><strong>نقل الدم المتكرر</strong> — كل وحدة دم تضيف حوالي "
                "200–250 ملغ من الحديد</li>"
                "<li><strong>التسمم بالحديد</strong> — ابتلاع عرضي لجرعات عالية، "
                "خطير بشكل خاص عند الأطفال</li>"
                "</ul>"
                "<p>فرط الحديد المزمن يؤدي إلى ترسبه في الأعضاء "
                "(<em>داء الهيموسيديرين</em>). الكشف المبكر ضروري لمنع "
                "تلف الأعضاء الذي لا يمكن عكسه.</p>"
            ),
        ),
        Section(
            id="iron-vs-ferritin", level=2,
            heading="الحديد مقابل الفيريتين: ما الفرق؟",
            body_html=(
                "<p><strong>الحديد في المصل</strong> هو لقطة سريعة للحديد المتدفق "
                "حالياً في الدم، المرتبط بالترانسفيرين. يتذبذب بشكل ملحوظ خلال "
                "اليوم ويتأثر بالوجبات، مما يحد من موثوقيته كمؤشر منفرد.</p>"
                "<p><strong>الفيريتين</strong> يعكس مخازن الحديد في الجسم وهو "
                "مؤشر أكثر ثباتاً بكثير. الفيريتين المنخفض دليل شبه مؤكد على "
                "نفاد المخازن. ومع ذلك، بوصفه <em>بروتين المرحلة الحادة</em>، "
                "قد يرتفع الفيريتين أثناء الالتهاب والعدوى وأمراض الكبد — مما "
                "قد يخفي نقصاً أساسياً.</p>"
                "<p>للتقييم الشامل لحالة الحديد، يجب تفسير كلا الاختبارين معاً، "
                "ويفضّل مع TIBC وتشبع الترانسفيرين. يتيح هذا المزيج لطبيبك "
                "التمييز بين فقر الدم الناتج عن نقص الحديد، وفقر الدم المزمن، "
                "وفرط الحديد.</p>"
            ),
        ),
        Section(
            id="tibc-and-transferrin", level=2,
            heading="TIBC وتشبع الترانسفيرين",
            body_html=(
                "<p><strong>TIBC (السعة الكلية لربط الحديد)</strong> يقيس الحد "
                "الأقصى من الحديد الذي يمكن للترانسفيرين حمله. في نقص الحديد، "
                "ينتج الجسم مزيداً من الترانسفيرين فيرتفع TIBC؛ في فرط الحديد "
                "أو الأمراض المزمنة، ينخفض TIBC.</p>"
                "<p><strong>تشبع الترانسفيرين</strong> يُحسب كالتالي: "
                "<em>(الحديد في المصل ÷ TIBC) × 100</em>. في الأشخاص الأصحاء "
                "يتراوح عادة بين 20% و50%. أقل من 20% يشير إلى نقص الحديد؛ "
                "فوق 50% يثير القلق بشأن فرط الحديد، خاصة داء ترسب الأصبغة "
                "الدموية.</p>"
                "<p>عند تقييمها مع الحديد في المصل والفيريتين، تشكّل هذه المؤشرات "
                "لوحة تشخيصية قوية. مثال: حديد منخفض + TIBC مرتفع + فيريتين "
                "منخفض = فقر دم ناتج عن نقص الحديد؛ حديد منخفض + TIBC منخفض + "
                "فيريتين طبيعي أو مرتفع = فقر دم مزمن.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض انخفاض وارتفاع الحديد",
            body_html=(
                "<p><strong>أعراض انخفاض الحديد:</strong> التعب، الشحوب، ضيق "
                "التنفس عند المجهود، هشاشة الأظافر، برودة الأطراف، الدوخة، "
                "الصداع و<em>البيكا</em> (الرغبة في تناول مواد غير غذائية مثل "
                "الثلج أو الطين). في الحالات الشديدة قد يظهر تسارع القلب "
                "وألم الصدر.</p>"
                "<p><strong>أعراض ارتفاع الحديد:</strong> آلام المفاصل (خاصة "
                "في اليدين)، التعب المزمن، آلام البطن، تلوّن الجلد بالبرونزي، "
                "تضخم الكبد وضعف وظائفه. داء ترسب الأصبغة الدموية غير المعالج "
                "قد يتطور إلى سكري واعتلال عضلة القلب وتشمع الكبد.</p>"
                "<p>في كلا الاتجاهين، تميل الأعراض إلى التطور تدريجياً ويسهل "
                "تجاهلها. الفحوصات الدورية — خاصة لمن لديهم تاريخ عائلي — هي "
                "الطريقة الأكثر موثوقية لاكتشاف المشكلات مبكراً.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>يجب مراجعة الطبيب إذا كان مستوى الحديد في المصل خارج "
                "النطاق المرجعي. يُنصح بتقييم طبي سريع بشكل خاص إذا:</p>"
                "<ul>"
                "<li>تعانين من تعب أو شحوب أو ضيق تنفس غير مبرر</li>"
                "<li>يوجد تاريخ عائلي لداء ترسب الأصبغة الدموية</li>"
                "<li>لديكِ دورات شهرية غزيرة أو اشتباه بنزيف معدي معوي</li>"
                "<li>الفيريتين منخفض جداً أو مرتفع جداً</li>"
                "<li>تشبع الترانسفيرين أقل من 20% أو أعلى من 50%</li>"
                "</ul>"
                "<p>قد يطلب الطبيب فحوصات إضافية — تعداد دم كامل، لطاخة "
                "محيطية، B12، حمض الفوليك، فحص جيني HFE — لتحديد السبب. "
                "التشخيص والعلاج المبكران ضروريان لمنع المضاعفات.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يمكن لـ Norya مساعدتك؟",
            body_html=(
                "<p>فهم نتائج تحاليل الدم قد يكون محيراً أحياناً. "
                "<strong>Norya</strong> يتيح لك رفع تقرير تحليل الدم والحصول "
                "في دقائق على ملخص صحي منظّم وسهل الفهم. تُقارَن نتائجك "
                "بالنطاقات المرجعية وتُشرح بلغة واضحة.</p>"
                "<p>Norya ليس أداة تشخيص — هدفه إعدادك لمحادثة أكثر وعياً "
                "مع طبيبك. <a href=\"/analyze\">ابدأ التحليل مع Norya</a> "
                "واكتشف ماذا تعني نتائجك. لمعرفة تفاصيل الأسعار، تفضّل بزيارة "
                "<a href=\"/pricing\">صفحة الأسعار</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة '
                'أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في '
                'الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_iron_sections_by_lang():
    """Returns sections_by_lang dict for Iron article (all 9 languages)."""
    return {
        "tr": _sections_tr(),
        "en": _sections_en(),
        "es": _sections_es(),
        "de": _sections_de(),
        "fr": _sections_fr(),
        "it": _sections_it(),
        "he": _sections_he(),
        "hi": _sections_hi(),
        "ar": _sections_ar(),
    }


def get_iron_faq_schema_qa():
    """Returns faq_schema_qa dict for Iron article (all 9 languages)."""
    return {
        "tr": [
            {"question": "Serum demir testi nedir?",
             "answer": "Serum demir testi, kanınızdaki transferrine bağlı dolaşımdaki demir miktarını ölçer. Genellikle sabah açlık durumunda yapılır ve sonuçlar μg/dL cinsinden raporlanır. Demir eksikliği, anemi ve hemokromatoz gibi durumların değerlendirilmesinde kullanılır."},
            {"question": "Demir ve ferritin arasındaki fark nedir?",
             "answer": "Serum demir, kanda dolaşan anlık demir düzeyini gösterir ve gün içinde dalgalanır. Ferritin ise vücuttaki demir depolarını yansıtır ve çok daha kararlı bir göstergedir. Tam bir değerlendirme için her ikisi birlikte yorumlanmalıdır."},
            {"question": "Düşük demir seviyesinin nedenleri nelerdir?",
             "answer": "Başlıca nedenler arasında demir eksikliği anemisi, kan kaybı (menstrüasyon, GI kanama), malabsorpsiyon (çölyak, IBD), vejetaryen/vegan diyet, gebelik ve kronik hastalık anemisi sayılabilir."},
            {"question": "Yüksek demir seviyesinin nedenleri nelerdir?",
             "answer": "Yüksek demir; herediter hemokromatoz, aşırı demir takviyesi, hemolitik anemi, karaciğer hastalığı, çoklu kan transfüzyonları ve demir zehirlenmesi gibi durumlarda görülebilir. Tedavi edilmezse organlarda hasar oluşabilir."},
            {"question": "TIBC ve transferrin satürasyonu nedir?",
             "answer": "TIBC, transferrinin taşıyabileceği toplam demir miktarını ölçer. Transferrin satürasyonu ise (Serum Demir / TIBC) × 100 formülüyle hesaplanır. %20 altı demir eksikliğini, %50 üstü demir yüklenmesini düşündürür."},
        ],
        "en": [
            {"question": "What is a serum iron test?",
             "answer": "A serum iron test measures the amount of iron circulating in the blood, bound to the transport protein transferrin. It is usually performed in the morning after fasting, and results are reported in μg/dL. It is used to evaluate iron deficiency, anemia, and hemochromatosis."},
            {"question": "What is the difference between iron and ferritin?",
             "answer": "Serum iron reflects the iron currently circulating in the blood and fluctuates throughout the day. Ferritin reflects iron stores and is a more stable marker. Both should be interpreted together for a complete assessment of iron status."},
            {"question": "What causes low iron levels?",
             "answer": "Common causes include iron deficiency anemia, blood loss (menstruation, GI bleeding), malabsorption (celiac disease, IBD), vegetarian or vegan diet, pregnancy, and anemia of chronic disease where inflammation traps iron in stores."},
            {"question": "What causes high iron levels?",
             "answer": "Elevated iron can result from hereditary hemochromatosis, excessive iron supplementation, hemolytic anemia, liver disease, multiple blood transfusions, and iron poisoning. Untreated overload can cause organ damage."},
            {"question": "What is TIBC and transferrin saturation?",
             "answer": "TIBC (Total Iron-Binding Capacity) measures the maximum iron that transferrin can carry. Transferrin saturation is calculated as (Serum Iron ÷ TIBC) × 100. Below 20% suggests iron deficiency; above 50% suggests iron overload."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de hierro sérico?",
             "answer": "La prueba de hierro sérico mide la cantidad de hierro circulante en la sangre, unido a la proteína de transporte transferrina. Se realiza generalmente por la mañana en ayunas y los resultados se expresan en μg/dL. Se utiliza para evaluar deficiencia de hierro, anemia y hemocromatosis."},
            {"question": "¿Cuál es la diferencia entre hierro y ferritina?",
             "answer": "El hierro sérico refleja el hierro que circula actualmente y fluctúa durante el día. La ferritina refleja los depósitos de hierro y es un marcador más estable. Ambos deben interpretarse juntos para una evaluación completa."},
            {"question": "¿Qué causa niveles bajos de hierro?",
             "answer": "Las causas comunes incluyen anemia ferropénica, pérdida de sangre (menstruación, sangrado GI), malabsorción (enfermedad celíaca, EII), dieta vegetariana o vegana, embarazo y anemia de enfermedad crónica."},
            {"question": "¿Qué causa niveles altos de hierro?",
             "answer": "El hierro elevado puede deberse a hemocromatosis hereditaria, suplementación excesiva, anemia hemolítica, enfermedad hepática, transfusiones múltiples e intoxicación por hierro. La sobrecarga no tratada puede causar daño orgánico."},
            {"question": "¿Qué es el TIBC y la saturación de transferrina?",
             "answer": "El TIBC mide la cantidad máxima de hierro que la transferrina puede transportar. La saturación de transferrina se calcula como (Hierro Sérico ÷ TIBC) × 100. Por debajo del 20% sugiere deficiencia; por encima del 50% sugiere sobrecarga."},
        ],
        "de": [
            {"question": "Was ist ein Serumeisen-Test?",
             "answer": "Ein Serumeisen-Test misst die Menge an Eisen im Blut, die an das Transportprotein Transferrin gebunden ist. Er wird üblicherweise morgens nüchtern durchgeführt und die Ergebnisse werden in μg/dL angegeben. Er dient zur Beurteilung von Eisenmangel, Anämie und Hämochromatose."},
            {"question": "Was ist der Unterschied zwischen Eisen und Ferritin?",
             "answer": "Serumeisen zeigt den aktuell zirkulierenden Eisenspiegel und schwankt im Tagesverlauf. Ferritin spiegelt die Eisenspeicher wider und ist ein stabilerer Marker. Beide sollten gemeinsam interpretiert werden."},
            {"question": "Was verursacht niedrige Eisenwerte?",
             "answer": "Häufige Ursachen sind Eisenmangelanämie, Blutverlust (Menstruation, GI-Blutung), Malabsorption (Zöliakie, CED), vegetarische oder vegane Ernährung, Schwangerschaft und Entzündungsanämie."},
            {"question": "Was verursacht hohe Eisenwerte?",
             "answer": "Erhöhte Eisenwerte können durch hereditäre Hämochromatose, übermäßige Eisensupplementation, hämolytische Anämie, Lebererkrankung, wiederholte Transfusionen und Eisenvergiftung verursacht werden. Unbehandelte Überladung kann zu Organschäden führen."},
            {"question": "Was sind TIBC und Transferrinsättigung?",
             "answer": "Die TIBC misst die maximale Eisenmenge, die Transferrin transportieren kann. Die Transferrinsättigung berechnet sich als (Serumeisen ÷ TIBC) × 100. Unter 20 % spricht für Eisenmangel; über 50 % für Eisenüberladung."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test de fer sérique ?",
             "answer": "Le test de fer sérique mesure la quantité de fer circulant dans le sang, lié à la protéine de transport transferrine. Il est généralement réalisé à jeun le matin et les résultats sont exprimés en μg/dL. Il sert à évaluer la carence en fer, l'anémie et l'hémochromatose."},
            {"question": "Quelle est la différence entre le fer et la ferritine ?",
             "answer": "Le fer sérique reflète le fer actuellement en circulation et fluctue au cours de la journée. La ferritine reflète les réserves en fer et constitue un marqueur plus stable. Les deux doivent être interprétés conjointement pour une évaluation complète."},
            {"question": "Quelles sont les causes d'un fer bas ?",
             "answer": "Les causes courantes comprennent l'anémie ferriprive, les pertes sanguines (règles, saignement GI), la malabsorption (maladie cœliaque, MICI), le régime végétarien ou végan, la grossesse et l'anémie des maladies chroniques."},
            {"question": "Quelles sont les causes d'un fer élevé ?",
             "answer": "Un fer élevé peut résulter d'une hémochromatose héréditaire, d'une supplémentation excessive, d'une anémie hémolytique, d'une maladie hépatique, de transfusions multiples ou d'une intoxication au fer. La surcharge non traitée peut causer des dommages organiques."},
            {"question": "Qu'est-ce que la CTF (TIBC) et la saturation de la transferrine ?",
             "answer": "La CTF mesure la quantité maximale de fer que la transferrine peut transporter. La saturation de la transferrine se calcule : (Fer Sérique ÷ CTF) × 100. En dessous de 20 %, on suspecte une carence ; au-dessus de 50 %, une surcharge."},
        ],
        "it": [
            {"question": "Cos'è il test della sideremia?",
             "answer": "Il test della sideremia misura la quantità di ferro circolante nel sangue, legata alla proteina di trasporto transferrina. Viene solitamente eseguito al mattino a digiuno e i risultati sono espressi in μg/dL. Serve per valutare carenza di ferro, anemia ed emocromatosi."},
            {"question": "Qual è la differenza tra ferro e ferritina?",
             "answer": "La sideremia riflette il ferro attualmente circolante e oscilla nel corso della giornata. La ferritina riflette le riserve di ferro ed è un marcatore più stabile. Entrambi devono essere interpretati insieme per una valutazione completa."},
            {"question": "Quali sono le cause di sideremia bassa?",
             "answer": "Le cause comuni includono anemia sideropenica, perdita di sangue (mestruazioni, sanguinamento GI), malassorbimento (celiachia, MICI), dieta vegetariana o vegana, gravidanza e anemia da malattia cronica."},
            {"question": "Quali sono le cause di sideremia alta?",
             "answer": "La sideremia elevata può essere causata da emocromatosi ereditaria, integrazione eccessiva, anemia emolitica, malattia epatica, trasfusioni multiple e avvelenamento da ferro. Il sovraccarico non trattato può causare danni agli organi."},
            {"question": "Cosa sono TIBC e saturazione della transferrina?",
             "answer": "La TIBC misura la quantità massima di ferro che la transferrina può trasportare. La saturazione della transferrina si calcola: (Sideremia ÷ TIBC) × 100. Sotto il 20% suggerisce carenza; sopra il 50% suggerisce sovraccarico."},
        ],
        "he": [
            {"question": "מהי בדיקת ברזל בסרום?",
             "answer": "בדיקת ברזל בסרום מודדת את כמות הברזל הזורמת בדם, הקשורה לחלבון ההעברה טרנספרין. היא מבוצעת בדרך כלל בבוקר בצום והתוצאות מדווחות ב-μg/dL. משמשת להערכת מחסור בברזל, אנמיה והמוכרומטוזיס."},
            {"question": "מה ההבדל בין ברזל לפריטין?",
             "answer": "ברזל בסרום משקף את הברזל הזורם כעת ומשתנה במהלך היום. פריטין משקף את מאגרי הברזל ומהווה סמן יציב יותר. שניהם צריכים להתפרש יחד להערכה מלאה."},
            {"question": "מה גורם לרמות ברזל נמוכות?",
             "answer": "הגורמים השכיחים כוללים אנמיה מחוסר ברזל, איבוד דם (מחזור חודשי, דימום GI), חוסר ספיגה (צליאק, IBD), תזונה צמחונית או טבעונית, הריון ואנמיה של מחלה כרונית."},
            {"question": "מה גורם לרמות ברזל גבוהות?",
             "answer": "ברזל גבוה יכול לנבוע מהמוכרומטוזיס תורשתי, תוסף ברזל מוגזם, אנמיה המוליטית, מחלת כבד, עירויי דם חוזרים והרעלת ברזל. עומס ברזל שלא מטופל עלול לגרום נזק לאיברים."},
            {"question": "מהם TIBC ורוויון טרנספרין?",
             "answer": "TIBC מודד את כמות הברזל המרבית שטרנספרין יכול לשאת. רוויון טרנספרין מחושב כ-(ברזל בסרום ÷ TIBC) × 100. מתחת ל-20% מרמז על מחסור; מעל 50% מרמז על עומס ברזל."},
        ],
        "hi": [
            {"question": "सीरम आयरन टेस्ट क्या है?",
             "answer": "सीरम आयरन टेस्ट रक्त में ट्रांसफेरिन से बंधे हुए आयरन की मात्रा को मापता है। यह आमतौर पर सुबह खाली पेट किया जाता है और परिणाम μg/dL में दिए जाते हैं। इसका उपयोग आयरन की कमी, एनीमिया और हेमोक्रोमैटोसिस के मूल्यांकन के लिए किया जाता है।"},
            {"question": "आयरन और फेरिटिन में क्या अंतर है?",
             "answer": "सीरम आयरन वर्तमान में रक्त में घूम रहे आयरन को दर्शाता है और दिन भर बदलता रहता है। फेरिटिन आयरन भंडार को दर्शाता है और अधिक स्थिर मार्कर है। पूर्ण मूल्यांकन के लिए दोनों की व्याख्या एक साथ की जानी चाहिए।"},
            {"question": "आयरन का स्तर कम होने के क्या कारण हैं?",
             "answer": "सामान्य कारणों में आयरन की कमी से एनीमिया, रक्त हानि (मासिक धर्म, GI रक्तस्राव), कुअवशोषण (सीलिएक, IBD), शाकाहारी या वीगन आहार, गर्भावस्था और पुरानी बीमारी का एनीमिया शामिल हैं।"},
            {"question": "आयरन का स्तर अधिक होने के क्या कारण हैं?",
             "answer": "अधिक आयरन वंशानुगत हेमोक्रोमैटोसिस, अत्यधिक आयरन सप्लीमेंट, हेमोलिटिक एनीमिया, यकृत रोग, बहुविध रक्त आधान और आयरन विषाक्तता के कारण हो सकता है। अनुपचारित अधिभार अंग क्षति का कारण बन सकता है।"},
            {"question": "TIBC और ट्रांसफेरिन संतृप्ति क्या है?",
             "answer": "TIBC ट्रांसफेरिन द्वारा वहन की जा सकने वाली अधिकतम आयरन मात्रा को मापता है। ट्रांसफेरिन संतृप्ति (सीरम आयरन ÷ TIBC) × 100 से गणना की जाती है। 20% से नीचे कमी का सुझाव देता है; 50% से ऊपर अधिभार का सुझाव देता है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل الحديد في المصل؟",
             "answer": "تحليل الحديد في المصل يقيس كمية الحديد الموجودة في الدم والمرتبطة ببروتين النقل الترانسفيرين. يُجرى عادةً صباحاً على الريق وتُعبَّر النتائج بوحدة μg/dL. يُستخدم لتقييم نقص الحديد وفقر الدم وداء ترسب الأصبغة الدموية."},
            {"question": "ما الفرق بين الحديد والفيريتين؟",
             "answer": "الحديد في المصل يعكس الحديد المتدفق حالياً ويتذبذب خلال اليوم. الفيريتين يعكس مخازن الحديد وهو مؤشر أكثر ثباتاً. يجب تفسير كليهما معاً لتقييم شامل."},
            {"question": "ما أسباب انخفاض مستوى الحديد؟",
             "answer": "تشمل الأسباب الشائعة فقر الدم بسبب نقص الحديد، فقدان الدم (الحيض، النزيف المعدي المعوي)، سوء الامتصاص (الداء البطني، مرض الأمعاء الالتهابي)، النظام النباتي، الحمل وفقر الدم المزمن."},
            {"question": "ما أسباب ارتفاع مستوى الحديد؟",
             "answer": "قد ينتج ارتفاع الحديد عن داء ترسب الأصبغة الدموية الوراثي، الإفراط في مكملات الحديد، فقر الدم الانحلالي، أمراض الكبد، نقل الدم المتكرر والتسمم بالحديد. فرط الحديد غير المعالج قد يسبب تلف الأعضاء."},
            {"question": "ما هو TIBC وتشبع الترانسفيرين؟",
             "answer": "TIBC يقيس الحد الأقصى من الحديد الذي يمكن للترانسفيرين حمله. تشبع الترانسفيرين يُحسب: (الحديد في المصل ÷ TIBC) × 100. أقل من 20% يشير إلى نقص؛ فوق 50% يشير إلى فرط حديد."},
        ],
    }
