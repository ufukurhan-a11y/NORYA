# -*- coding: utf-8 -*-
"""
T3 & T4 thyroid hormones blog article — full body content for all 9 languages.
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
            heading="T3 ve T4: Tiroid Hormonlarınızı Anlamak",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>T3</strong> ve <strong>T4</strong> değerlerini "
                "gördüğünüzde aklınıza ilk gelen soru genellikle şudur: Bu hormonlar ne işe yarıyor "
                "ve sonuçlarım normal mi? Triiyodotironin (T3) ve tiroksin (T4), tiroid bezinin "
                "ürettiği ve vücudun metabolizmasını, enerji dengesini, büyüme ve gelişmeyi düzenleyen "
                "temel hormonlardır. Neredeyse her hücreyi etkileyen bu hormonların düzeyleri; "
                "yorgunluktan kilo değişimlerine, kalp hızından saç dökülmesine kadar pek çok belirti "
                "ile ilişkilendirilebilir.</p>"
                "<p>Bu rehber, T3 ve T4 hormonlarının ne olduğunu, aralarındaki farkları, referans "
                "aralıklarını ve anormal sonuçların olası nedenlerini sade bir dille açıklamayı "
                "amaçlamaktadır. Amacımız teşhis koymak değil; sonuçlarınızı daha iyi anlayarak "
                "hekiminizle verimli bir görüşme yapmanıza yardımcı olmaktır.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="T3 ve T4 nedir?",
            body_html=(
                "<p><strong>T3 (triiyodotironin)</strong> ve <strong>T4 (tiroksin)</strong>, boyundaki "
                "kelebek biçimli tiroid bezi tarafından üretilen hormonlardır. T4, tiroidin en fazla "
                "salgıladığı hormondur ve dolaşımdaki tiroid hormonlarının yaklaşık %80'ini oluşturur. "
                "Ancak T4'ün biyolojik aktivitesi nispeten düşüktür; vücutta enzimatik yolla bir iyot "
                "atomu ayrılarak daha aktif olan T3'e dönüştürülür. T3, hücre düzeyinde metabolizmayı "
                "doğrudan hızlandıran asıl efektör hormondur.</p>"
                "<p>Her iki hormon da protein sentezi, oksijen tüketimi, kalp debisi, bağırsak "
                "motilitesi ve beyin gelişimi gibi temel fizyolojik süreçleri etkiler. Çocukluk "
                "çağında büyüme ve nörolojik olgunlaşma için kritik öneme sahipken, yetişkinlerde "
                "metabolik hızın korunmasında merkezi rol oynar. Tiroid hormon düzeylerinin çok yüksek "
                "veya çok düşük olması, vücudun hemen her sistemi üzerinde gözle görülür değişikliklere "
                "yol açabilir.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="T3 ile T4 arasındaki fark nedir?",
            body_html=(
                "<p><strong>T4</strong>, tiroidin birincil ürünüdür ve kanda daha yüksek "
                "konsantrasyonda bulunur. Yarı ömrü yaklaşık 6–7 gündür; bu nedenle kan düzeyleri "
                "gün içinde nispeten kararlıdır ve laboratuvar testlerinde güvenilir bir göstergedir. "
                "<strong>T3</strong> ise T4'ten 3–5 kat daha güçlü olmasına rağmen kanda çok daha "
                "düşük miktarlarda bulunur ve yarı ömrü yalnızca yaklaşık 1 gündür. Dolaşımdaki T3'ün "
                "büyük bölümü karaciğer ve böbrek gibi çevresel dokularda T4'ten dönüşüm yoluyla elde "
                "edilir.</p>"
                "<p>Klinik pratikte genellikle önce <em>serbest T4</em> (Free T4) ve <em>TSH</em> "
                "ölçülür. T3, özellikle T4 normal olup TSH baskılı olduğunda veya hipertiroidi "
                "düşünüldüğünde ek bilgi sağlamak amacıyla istenir. Her iki hormonun birlikte "
                "değerlendirilmesi, tiroid fonksiyonunun tam resmini ortaya koyar.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="Serbest ve total hormon farkı",
            body_html=(
                "<p>Kanda dolaşan T3 ve T4'ün büyük çoğunluğu <strong>taşıyıcı proteinlere</strong> "
                "(başta tiroksin bağlayıcı globülin — TBG) bağlı hâlde taşınır. Bu bağlı fraksiyon "
                "biyolojik olarak aktif değildir; yalnızca <strong>serbest (free)</strong> fraksiyon "
                "hücrelere girerek etki gösterir. Total T4 ve Total T3, bağlı ve serbest formların "
                "toplamını ölçerken, Serbest T4 (FT4) ve Serbest T3 (FT3) yalnızca aktif olan serbest "
                "kısmı ölçer.</p>"
                "<p>Hamilelik, östrojen tedavisi, karaciğer hastalığı veya genetik TBG varyantları "
                "gibi durumlarda taşıyıcı protein düzeyleri değişebilir; bu da total değerleri "
                "etkilerken serbest hormon düzeylerini genellikle etkilemez. Bu nedenle günümüzde "
                "tiroid fonksiyonunun değerlendirilmesinde <em>serbest hormon</em> ölçümleri tercih "
                "edilmektedir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="T3 ve T4 referans aralıkları",
            body_html=(
                "<p>Aşağıdaki tablo, yetişkinler için yaygın olarak kabul edilen tiroid hormon "
                "referans aralıklarını göstermektedir. Laboratuvarlar arasında yöntem farklılıkları "
                "nedeniyle bu değerler küçük sapmalar gösterebilir; raporunuzdaki referans aralığını "
                "esas almanız önerilir.</p>"
                f'{_TBL}<thead><tr><th {_TH}>Test</th>'
                f'<th {_TH}>Referans Aralığı</th></tr></thead><tbody>'
                f'<tr><td {_TD}>Serbest T4 (Free T4)</td><td {_TD}>0,8 – 1,8 ng/dL</td></tr>'
                f'<tr><td {_TD}>Serbest T3 (Free T3)</td><td {_TD}>2,3 – 4,2 pg/mL</td></tr>'
                f'<tr><td {_TD}>Total T4</td><td {_TD}>4,5 – 12,5 μg/dL</td></tr>'
                f'<tr><td {_TD}>Total T3</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0,4 – 4,0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>Bu değerler genel yetişkin popülasyonu içindir. Hamilelik, yaş, kullanılan "
                "ilaçlar ve kronik hastalıklar referans aralıklarını değiştirebilir. Sonuçlarınızı "
                "daima kendi laboratuvarınızın referans aralığı ve klinik bağlamınızla birlikte "
                "değerlendirin.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="T3 ve T4 yüksekliği (hipertiroidizm) nedenleri",
            body_html=(
                "<p>T3 ve/veya T4 düzeylerinin referans aralığının üzerinde olmasına "
                "<strong>hipertiroidizm</strong> denir. En sık nedenleri şunlardır: "
                "<strong>Graves hastalığı</strong> (tiroid bezini uyaran otoantikorlar nedeniyle aşırı "
                "hormon üretimi), <strong>toksik nodüler guatr</strong> (otonom çalışan tiroid "
                "nodülleri), <strong>tiroidit</strong> (bezin iltihaplanmasıyla depolanmış hormonun "
                "kana karışması) ve <strong>aşırı tiroid ilacı kullanımı</strong>.</p>"
                "<p>Hipertiroidizmde metabolizma hızlanır; çarpıntı, kilo kaybı, terleme, tremor, "
                "huzursuzluk ve ishal gibi belirtiler görülebilir. Bazı hastalarda T3 yalnız başına "
                "yükselebilir (<em>T3 tirotoksikozu</em>) ve T4 normal kalabilir. Teşhis, klinik "
                "belirti ve laboratuvar sonuçlarının birlikte değerlendirilmesini gerektirir.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="T3 ve T4 düşüklüğü (hipotiroidizm) nedenleri",
            body_html=(
                "<p>T3 ve/veya T4 düzeylerinin referans aralığının altında olması "
                "<strong>hipotiroidizm</strong> olarak adlandırılır. Dünya genelinde en yaygın nedeni "
                "<strong>Hashimoto tiroiditi</strong>dir; bağışıklık sistemi tiroid dokusuna saldırarak "
                "hormonal üretimi azaltır. Diğer nedenler arasında <strong>iyot eksikliği</strong>, "
                "<strong>hipofiz bezi hastalıkları</strong> (sekonder hipotiroidizm), tiroid cerrahisi "
                "veya radyoaktif iyot tedavisi sonrası durum ve <strong>bazı ilaçlar</strong> (lityum, "
                "amiodaron) yer alır.</p>"
                "<p>Hipotiroidizmde metabolizma yavaşlar; halsizlik, kilo artışı, üşüme, kabızlık, "
                "kuru cilt, saç dökülmesi ve depresif ruh hâli gibi belirtiler sık görülür. Tanı "
                "genellikle yüksek TSH ve düşük Serbest T4 kombinasyonuyla konulur; tedavide sentetik "
                "tiroksin (levotiroksin) replasmanı kullanılır.</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="TSH ile T3-T4 arasındaki ilişki",
            body_html=(
                "<p><strong>TSH (tiroid uyarıcı hormon)</strong>, hipofiz bezinden salgılanır ve "
                "tiroid bezine ne kadar T3-T4 üretmesi gerektiğini söyler. Kanda tiroid hormonu "
                "azaldığında hipofiz daha fazla TSH salgılayarak tiroides uyarır "
                "(<em>negatif geri bildirim</em>); hormon yeterli düzeye ulaştığında TSH baskılanır. "
                "Bu dinamik denge sayesinde vücut metabolik hızını dar bir aralıkta tutar.</p>"
                "<p>Klinik pratikte TSH en hassas tarama testidir: erken hipotiroidizmde T4 henüz "
                "normalken TSH yükselmeye başlar (<em>subklinik hipotiroidizm</em>); erken "
                "hipertiroidizmde ise T4 henüz sınırda yüksekken TSH baskılanır. Bu nedenle doktorlar "
                "genellikle önce TSH'ye bakar, gerekirse Serbest T4 ve T3 ile tamamlar. TSH'nin "
                "normal aralığı genel olarak <strong>0,4–4,0 mIU/L</strong> kabul edilir, ancak "
                "bireysel hedefler yaşa ve klinik duruma göre farklılık gösterebilir.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Tiroid hormon dengesizliğinin belirtileri",
            body_html=(
                "<p><strong>Hipertiroidi belirtileri:</strong> çarpıntı, kilo kaybı, aşırı terleme, "
                "sıcak intoleransı, tremor (el titremesi), huzursuzluk, uykusuzluk, sık dışkılama "
                "veya ishal, kas güçsüzlüğü ve kadınlarda adet düzensizliği. Graves hastalığında göz "
                "bulguları (ekzoftalmus) da eşlik edebilir.</p>"
                "<p><strong>Hipotiroidi belirtileri:</strong> yorgunluk, halsizlik, kilo artışı, "
                "soğuk intoleransı, kabızlık, kuru cilt, saç ve kaş dökülmesi, ödem (özellikle yüz "
                "ve göz çevresinde), depresif ruh hâli, hafıza güçlüğü ve bradikardi (düşük kalp "
                "hızı). Belirtiler yavaş geliştiğinden hasta tarafından fark edilmesi gecikebilir.</p>"
                "<p>Her iki durumda da belirtiler özgül değildir; yalnızca belirtilere bakarak kesin "
                "tanı konulamaz. Laboratuvar testleri ve klinik değerlendirme birlikte ele "
                "alınmalıdır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman hekime başvurmalısınız?",
            body_html=(
                "<p>Tahlil sonuçlarınızda T3, T4 veya TSH değerlerinden herhangi biri referans "
                "aralığı dışındaysa bir hekimle görüşmeniz önerilir. Özellikle açıklanamayan kilo "
                "değişimi, sürekli yorgunluk, çarpıntı, tremor, saç dökülmesi, kabızlık veya ishal, "
                "ruh hâli değişimleri ya da boyunda şişlik fark ederseniz endokrinoloji veya dahiliye "
                "uzmanına başvurmak doğru adımdır.</p>"
                "<p>Tiroid hastalıklarında erken tanı tedavi başarısını artırır. Ailede tiroid "
                "hastalığı öyküsü olanlar, otoimmün hastalığı bulunanlar, hamile veya hamilelik "
                "planlayan kadınlar ve daha önce boyun bölgesine radyoterapi almış kişiler düzenli "
                "tiroid taraması yaptırmalıdır. Subklinik tablolarda bile hekiminiz takip planı "
                "önerebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya tiroid sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Norya'da teşhis koymuyoruz; kan tahlili raporunuzu anlamanızı ve hekiminize "
                "hazırlıklı gitmenizi kolaylaştırıyoruz. <a href=\"/analyze\">Raporunuzu "
                "yükleyerek</a> T3, T4 ve TSH dahil tüm değerlerinizin sade dilde, referans "
                "aralıklarıyla birlikte açıklandığı yapılandırılmış bir özet alabilirsiniz. Bu özet, "
                "doktorunuzla görüşmenizi daha verimli hâle getirir.</p>"
                "<p>Birkaç dakika içinde hazırlanan bu rapor, hangi değerlerinizin normal, "
                "hangilerinin sınır dışı olduğunu net biçimde gösterir. Sorularınızı hekiminize "
                "sormadan önce düzenlemenize yardımcı olur. Seçenekler ve fiyatlar için "
                "<a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edebilirsiniz.</p>"
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
            heading="T3 & T4: Understanding Your Thyroid Hormones",
            body_html=(
                "<p>When you see <strong>T3</strong> and <strong>T4</strong> on your blood test "
                "report, the first question is often: what do these hormones do, and are my results "
                "normal? Triiodothyronine (T3) and thyroxine (T4) are the primary hormones produced "
                "by the thyroid gland. They play a central role in regulating metabolism, energy "
                "production, growth, and development. Because they influence virtually every cell in "
                "the body, abnormal levels can manifest as symptoms ranging from fatigue and weight "
                "changes to heart-rate disturbances and hair loss.</p>"
                "<p>This guide explains what T3 and T4 are, how they differ, what the reference "
                "ranges mean, and what can cause abnormal results. Our goal is not to diagnose but "
                "to help you understand your results so you can have a more productive conversation "
                "with your doctor.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="What are T3 and T4?",
            body_html=(
                "<p><strong>T3 (triiodothyronine)</strong> and <strong>T4 (thyroxine)</strong> are "
                "hormones produced by the butterfly-shaped thyroid gland in the neck. T4 is the "
                "thyroid's primary secretory product and accounts for roughly 80 % of circulating "
                "thyroid hormone. However, T4 has relatively low biological activity; it is converted "
                "in peripheral tissues—mainly the liver and kidneys—into the more potent T3 by "
                "enzymatic removal of one iodine atom. T3 is the principal effector hormone that "
                "directly accelerates cellular metabolism.</p>"
                "<p>Together, these hormones regulate protein synthesis, oxygen consumption, cardiac "
                "output, gut motility, and brain development. During childhood they are critical for "
                "growth and neurological maturation, while in adults they maintain basal metabolic "
                "rate. When thyroid hormone levels are too high or too low, virtually every organ "
                "system in the body can be affected.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="T3 vs T4: what is the difference?",
            body_html=(
                "<p><strong>T4</strong> is the thyroid's main product and circulates at higher "
                "concentrations in the blood. Its half-life is approximately 6–7 days, making blood "
                "levels relatively stable throughout the day and a reliable laboratory marker. "
                "<strong>T3</strong> is 3–5 times more biologically potent than T4 but circulates in "
                "much smaller quantities; its half-life is only about 1 day. Most circulating T3 is "
                "produced by conversion from T4 in peripheral tissues rather than by direct thyroid "
                "secretion.</p>"
                "<p>In clinical practice, <em>Free T4</em> and <em>TSH</em> are usually measured "
                "first. T3 is added when T4 is normal but TSH is suppressed, or when hyperthyroidism "
                "is clinically suspected, because some patients have isolated T3 elevation "
                "(<em>T3 thyrotoxicosis</em>). Evaluating both hormones together provides the most "
                "complete picture of thyroid function.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="Free vs total hormones",
            body_html=(
                "<p>The majority of T3 and T4 circulating in the blood is bound to <strong>carrier "
                "proteins</strong>—primarily thyroxine-binding globulin (TBG). The bound fraction is "
                "biologically inactive; only the <strong>free (unbound)</strong> fraction can enter "
                "cells and exert metabolic effects. Total T4 and Total T3 measure the sum of bound "
                "and free forms, while Free T4 (FT4) and Free T3 (FT3) measure only the active "
                "unbound portion.</p>"
                "<p>Conditions such as pregnancy, estrogen therapy, liver disease, or genetic TBG "
                "variants can alter carrier-protein levels, shifting total values without necessarily "
                "changing the free hormone concentration. For this reason, modern thyroid assessment "
                "relies primarily on <em>free hormone</em> measurements, which more accurately "
                "reflect the biologically active hormone available to tissues.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="T3 and T4 reference ranges",
            body_html=(
                "<p>The table below shows commonly accepted reference ranges for thyroid hormones in "
                "adults. Because methodologies vary between laboratories, slight differences are "
                "normal; always refer to the reference range printed on your own report.</p>"
                f'{_TBL}<thead><tr><th {_TH}>Test</th>'
                f'<th {_TH}>Normal Range</th></tr></thead><tbody>'
                f'<tr><td {_TD}>Free T4</td><td {_TD}>0.8 – 1.8 ng/dL</td></tr>'
                f'<tr><td {_TD}>Free T3</td><td {_TD}>2.3 – 4.2 pg/mL</td></tr>'
                f'<tr><td {_TD}>Total T4</td><td {_TD}>4.5 – 12.5 μg/dL</td></tr>'
                f'<tr><td {_TD}>Total T3</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0.4 – 4.0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>These values apply to the general adult population. Pregnancy, age, medications, "
                "and chronic illnesses can shift reference ranges. Always interpret your results "
                "alongside your own laboratory's reference range and clinical context.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="Causes of high T3 and T4 (hyperthyroidism)",
            body_html=(
                "<p>When T3 and/or T4 levels are above the reference range, the condition is called "
                "<strong>hyperthyroidism</strong>. The most common causes include: "
                "<strong>Graves' disease</strong> (autoantibodies stimulate the thyroid to "
                "overproduce hormone), <strong>toxic nodular goiter</strong> (autonomously functioning "
                "thyroid nodules), <strong>thyroiditis</strong> (inflammation of the gland that "
                "releases stored hormone into the bloodstream), and <strong>excess thyroid "
                "medication</strong>.</p>"
                "<p>In hyperthyroidism the metabolic rate increases, potentially causing palpitations, "
                "weight loss, excessive sweating, tremor, nervousness, and diarrhea. In some patients "
                "only T3 is elevated (<em>T3 thyrotoxicosis</em>) while T4 remains normal. Diagnosis "
                "requires combining clinical signs with laboratory findings and, in some cases, "
                "thyroid imaging.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="Causes of low T3 and T4 (hypothyroidism)",
            body_html=(
                "<p>When T3 and/or T4 levels fall below the reference range, the condition is called "
                "<strong>hypothyroidism</strong>. The most common cause worldwide is "
                "<strong>Hashimoto's thyroiditis</strong>, an autoimmune condition in which the immune "
                "system attacks thyroid tissue, gradually reducing hormone production. Other causes "
                "include <strong>iodine deficiency</strong>, <strong>pituitary gland disorders</strong> "
                "(secondary hypothyroidism), post-surgical or post-radioactive-iodine states, and "
                "<strong>certain medications</strong> such as lithium and amiodarone.</p>"
                "<p>In hypothyroidism the metabolic rate slows, leading to fatigue, weight gain, cold "
                "intolerance, constipation, dry skin, hair loss, facial puffiness, depressed mood, "
                "memory difficulties, and bradycardia. Diagnosis is typically based on elevated TSH "
                "combined with low Free T4; treatment usually involves synthetic thyroxine "
                "(levothyroxine) replacement.</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="The TSH–T3–T4 feedback loop",
            body_html=(
                "<p><strong>TSH (thyroid-stimulating hormone)</strong> is secreted by the pituitary "
                "gland and tells the thyroid how much T3 and T4 to produce. When circulating thyroid "
                "hormone levels drop, the pituitary releases more TSH to stimulate the thyroid "
                "(<em>negative feedback</em>); when hormone levels are adequate, TSH is suppressed. "
                "This dynamic equilibrium keeps the metabolic rate within a narrow range.</p>"
                "<p>Clinically, TSH is the most sensitive screening test: in early hypothyroidism, "
                "TSH begins to rise before T4 falls below normal (<em>subclinical "
                "hypothyroidism</em>); in early hyperthyroidism, TSH is suppressed before T4 is "
                "frankly elevated. Doctors therefore usually check TSH first and add Free T4 and T3 "
                "as needed. The generally accepted normal range for TSH is "
                "<strong>0.4–4.0 mIU/L</strong>, although individual targets may vary with age and "
                "clinical context.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of thyroid hormone imbalance",
            body_html=(
                "<p><strong>Hyperthyroid symptoms:</strong> palpitations, unintended weight loss, "
                "excessive sweating, heat intolerance, tremor (especially of the hands), "
                "restlessness, insomnia, frequent bowel movements or diarrhea, muscle weakness, and "
                "menstrual irregularities in women. In Graves' disease, eye abnormalities "
                "(exophthalmos) may also be present.</p>"
                "<p><strong>Hypothyroid symptoms:</strong> fatigue, weight gain, cold intolerance, "
                "constipation, dry skin, hair and eyebrow thinning, edema (particularly around the "
                "face and eyes), depressed mood, memory problems, and bradycardia. Because symptoms "
                "develop gradually, patients may not notice them for months or even years.</p>"
                "<p>In both conditions, symptoms are non-specific and cannot alone confirm a "
                "diagnosis. Laboratory tests and clinical evaluation must be considered together.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If any of your T3, T4, or TSH values fall outside the reference range, "
                "consulting a doctor is recommended. Seek medical attention especially if you notice "
                "unexplained weight changes, persistent fatigue, palpitations, tremor, hair loss, "
                "constipation or diarrhea, mood disturbances, or a visible swelling in the neck.</p>"
                "<p>Early detection of thyroid disorders improves treatment outcomes. Individuals "
                "with a family history of thyroid disease, those with autoimmune conditions, women "
                "who are pregnant or planning pregnancy, and anyone who has received radiation "
                "therapy to the neck area should undergo regular thyroid screening. Even in "
                "subclinical cases, your doctor may recommend a monitoring plan.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your thyroid results",
            body_html=(
                "<p>At Norya we don't diagnose—we make it easier for you to understand your blood "
                "test and prepare for your doctor's visit. You can <a href=\"/analyze\">upload your "
                "report</a> and receive a clear, structured summary that explains your T3, T4, and "
                "TSH values in plain language alongside reference ranges. This summary helps you walk "
                "into your appointment better prepared.</p>"
                "<p>Ready in just a few minutes, the report highlights which values are within range "
                "and which fall outside, helping you organize your questions before you see your "
                "doctor. For options and pricing, visit our <a href=\"/pricing\">pricing page</a>.</p>"
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
            heading="T3 y T4: comprender las hormonas tiroideas",
            body_html=(
                "<p>Cuando ve los valores de <strong>T3</strong> y <strong>T4</strong> en su análisis "
                "de sangre, la primera pregunta suele ser: ¿para qué sirven estas hormonas y mis "
                "resultados son normales? La triyodotironina (T3) y la tiroxina (T4) son las hormonas "
                "principales producidas por la glándula tiroides y desempeñan un papel central en la "
                "regulación del metabolismo, la producción de energía, el crecimiento y el desarrollo. "
                "Dado que influyen en prácticamente todas las células del cuerpo, los niveles anormales "
                "pueden manifestarse con síntomas que van desde fatiga y cambios de peso hasta "
                "alteraciones del ritmo cardíaco y caída del cabello.</p>"
                "<p>Esta guía explica qué son la T3 y la T4, en qué se diferencian, qué significan "
                "los rangos de referencia y cuáles pueden ser las causas de resultados anormales. "
                "Nuestro objetivo no es diagnosticar, sino ayudarle a comprender sus resultados para "
                "que la conversación con su médico sea más productiva.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="¿Qué son la T3 y la T4?",
            body_html=(
                "<p>La <strong>T3 (triyodotironina)</strong> y la <strong>T4 (tiroxina)</strong> son "
                "hormonas producidas por la glándula tiroides, situada en la parte frontal del cuello. "
                "La T4 es el principal producto de secreción tiroidea y representa aproximadamente el "
                "80 % de la hormona tiroidea circulante. Sin embargo, su actividad biológica es "
                "relativamente baja; se convierte en los tejidos periféricos—sobre todo hígado y "
                "riñones—en la más potente T3 mediante la eliminación enzimática de un átomo de "
                "yodo.</p>"
                "<p>Ambas hormonas regulan la síntesis de proteínas, el consumo de oxígeno, el gasto "
                "cardíaco, la motilidad intestinal y el desarrollo cerebral. Durante la infancia son "
                "esenciales para el crecimiento y la maduración neurológica, mientras que en la edad "
                "adulta mantienen la tasa metabólica basal. Niveles demasiado altos o bajos pueden "
                "afectar prácticamente a todos los sistemas orgánicos.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="Diferencia entre T3 y T4",
            body_html=(
                "<p>La <strong>T4</strong> es el producto principal de la tiroides y circula a "
                "concentraciones más altas. Su vida media es de unos 6–7 días, lo que hace que sus "
                "niveles sanguíneos sean estables y constituyan un marcador de laboratorio fiable. La "
                "<strong>T3</strong> es de 3 a 5 veces más potente que la T4, pero circula en "
                "cantidades mucho menores y su vida media es de solo un día aproximadamente. La mayor "
                "parte de la T3 circulante se produce por conversión periférica de T4.</p>"
                "<p>En la práctica clínica se miden primero la <em>T4 libre</em> y la <em>TSH</em>. "
                "La T3 se solicita cuando la T4 es normal pero la TSH está suprimida, o cuando se "
                "sospecha hipertiroidismo, ya que algunos pacientes presentan elevación aislada de T3 "
                "(<em>tirotoxicosis por T3</em>). La evaluación conjunta de ambas hormonas ofrece el "
                "panorama más completo de la función tiroidea.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="Hormona libre frente a total",
            body_html=(
                "<p>La mayor parte de la T3 y la T4 en sangre circula unida a <strong>proteínas "
                "transportadoras</strong>, principalmente la globulina fijadora de tiroxina (TBG). La "
                "fracción unida es biológicamente inactiva; solo la <strong>fracción libre</strong> "
                "puede entrar en las células y ejercer efectos metabólicos. La T4 total y la T3 total "
                "miden la suma de las formas unidas y libres, mientras que la T4 libre (FT4) y la T3 "
                "libre (FT3) miden únicamente la porción activa no unida.</p>"
                "<p>El embarazo, el tratamiento con estrógenos, las enfermedades hepáticas o las "
                "variantes genéticas de TBG pueden alterar los niveles de proteínas transportadoras, "
                "modificando los valores totales sin cambiar necesariamente la concentración de "
                "hormona libre. Por ello, la evaluación tiroidea moderna se basa fundamentalmente en "
                "las mediciones de <em>hormona libre</em>.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos de referencia de T3 y T4",
            body_html=(
                "<p>La siguiente tabla muestra los rangos de referencia generalmente aceptados para "
                "las hormonas tiroideas en adultos. Dado que las metodologías varían entre "
                "laboratorios, pueden existir pequeñas diferencias; consulte siempre el rango impreso "
                "en su propio informe.</p>"
                f'{_TBL}<thead><tr><th {_TH}>Prueba</th>'
                f'<th {_TH}>Rango normal</th></tr></thead><tbody>'
                f'<tr><td {_TD}>T4 libre</td><td {_TD}>0,8 – 1,8 ng/dL</td></tr>'
                f'<tr><td {_TD}>T3 libre</td><td {_TD}>2,3 – 4,2 pg/mL</td></tr>'
                f'<tr><td {_TD}>T4 total</td><td {_TD}>4,5 – 12,5 μg/dL</td></tr>'
                f'<tr><td {_TD}>T3 total</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0,4 – 4,0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>Estos valores son para la población adulta general. El embarazo, la edad, los "
                "medicamentos y las enfermedades crónicas pueden modificar los rangos. Interprete "
                "siempre sus resultados junto con el rango de referencia de su laboratorio y su "
                "contexto clínico.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="Causas de T3 y T4 altas (hipertiroidismo)",
            body_html=(
                "<p>Cuando los niveles de T3 y/o T4 están por encima del rango de referencia se "
                "habla de <strong>hipertiroidismo</strong>. Las causas más frecuentes son: "
                "<strong>enfermedad de Graves</strong> (autoanticuerpos estimulan la tiroides a "
                "producir hormona en exceso), <strong>bocio multinodular tóxico</strong> (nódulos "
                "tiroideos que funcionan de forma autónoma), <strong>tiroiditis</strong> (inflamación "
                "de la glándula que libera hormona almacenada al torrente sanguíneo) y "
                "<strong>exceso de medicación tiroidea</strong>.</p>"
                "<p>El hipertiroidismo acelera el metabolismo y puede provocar palpitaciones, pérdida "
                "de peso, sudoración excesiva, temblor, nerviosismo y diarrea. En algunos pacientes "
                "solo se eleva la T3 (<em>tirotoxicosis por T3</em>) mientras la T4 permanece normal. "
                "El diagnóstico requiere combinar los signos clínicos con los hallazgos de "
                "laboratorio.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="Causas de T3 y T4 bajas (hipotiroidismo)",
            body_html=(
                "<p>Cuando los niveles de T3 y/o T4 están por debajo del rango de referencia se "
                "denomina <strong>hipotiroidismo</strong>. La causa más frecuente a nivel mundial es "
                "la <strong>tiroiditis de Hashimoto</strong>, una enfermedad autoinmune en la que el "
                "sistema inmunitario ataca el tejido tiroideo, reduciendo gradualmente la producción "
                "hormonal. Otras causas incluyen el <strong>déficit de yodo</strong>, las "
                "<strong>enfermedades hipofisarias</strong> (hipotiroidismo secundario), el estado "
                "posterior a cirugía o yodo radiactivo y <strong>ciertos fármacos</strong> como el "
                "litio y la amiodarona.</p>"
                "<p>En el hipotiroidismo el metabolismo se enlentece, provocando fatiga, aumento de "
                "peso, intolerancia al frío, estreñimiento, piel seca, caída del cabello, edema "
                "facial, ánimo deprimido, dificultades de memoria y bradicardia. El diagnóstico se "
                "basa habitualmente en TSH elevada con T4 libre baja; el tratamiento consiste en "
                "reemplazo con tiroxina sintética (levotiroxina).</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="Relación entre TSH, T3 y T4",
            body_html=(
                "<p>La <strong>TSH (hormona estimulante de la tiroides)</strong> es secretada por la "
                "hipófisis e indica a la tiroides cuánta T3 y T4 debe producir. Cuando los niveles de "
                "hormona tiroidea descienden, la hipófisis libera más TSH para estimular la tiroides "
                "(<em>retroalimentación negativa</em>); cuando son suficientes, la TSH se suprime. "
                "Este equilibrio dinámico mantiene la tasa metabólica en un rango estrecho.</p>"
                "<p>Clínicamente, la TSH es la prueba de cribado más sensible: en el hipotiroidismo "
                "temprano la TSH comienza a subir antes de que la T4 descienda (<em>hipotiroidismo "
                "subclínico</em>); en el hipertiroidismo temprano la TSH se suprime antes de que la "
                "T4 esté francamente elevada. Por ello los médicos suelen pedir primero la TSH y "
                "complementar con T4 y T3 libre. El rango normal de TSH se acepta generalmente en "
                "<strong>0,4–4,0 mIU/L</strong>, aunque los objetivos individuales pueden variar con "
                "la edad y el contexto clínico.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas del desequilibrio de hormonas tiroideas",
            body_html=(
                "<p><strong>Síntomas de hipertiroidismo:</strong> palpitaciones, pérdida de peso "
                "involuntaria, sudoración excesiva, intolerancia al calor, temblor (especialmente en "
                "las manos), inquietud, insomnio, tránsito intestinal acelerado o diarrea, debilidad "
                "muscular e irregularidades menstruales en mujeres. En la enfermedad de Graves pueden "
                "aparecer alteraciones oculares (exoftalmos).</p>"
                "<p><strong>Síntomas de hipotiroidismo:</strong> fatiga, aumento de peso, "
                "intolerancia al frío, estreñimiento, piel seca, adelgazamiento del cabello y las "
                "cejas, edema (sobre todo en cara y párpados), ánimo deprimido, problemas de memoria "
                "y bradicardia. Como los síntomas se desarrollan gradualmente, pueden pasar meses o "
                "años antes de que el paciente los perciba.</p>"
                "<p>En ambas condiciones los síntomas son inespecíficos y no bastan por sí solos para "
                "confirmar un diagnóstico. Las pruebas de laboratorio y la evaluación clínica deben "
                "considerarse conjuntamente.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe acudir al médico?",
            body_html=(
                "<p>Si alguno de sus valores de T3, T4 o TSH se encuentra fuera del rango de "
                "referencia, se recomienda consultar a un médico. Busque atención especialmente si "
                "presenta cambios de peso inexplicables, fatiga persistente, palpitaciones, temblor, "
                "caída del cabello, estreñimiento o diarrea, alteraciones del ánimo o una hinchazón "
                "visible en el cuello.</p>"
                "<p>La detección temprana de los trastornos tiroideos mejora los resultados del "
                "tratamiento. Las personas con antecedentes familiares de enfermedad tiroidea, quienes "
                "padecen enfermedades autoinmunes, las mujeres embarazadas o que planean un embarazo, "
                "y cualquiera que haya recibido radioterapia en el cuello deben someterse a controles "
                "tiroideos periódicos. Incluso en casos subclínicos, el médico puede recomendar un "
                "plan de seguimiento.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya le ayuda a entender sus resultados tiroideos",
            body_html=(
                "<p>En Norya no hacemos diagnósticos; facilitamos que comprenda su análisis de sangre "
                "y llegue preparado a la consulta. Puede <a href=\"/analyze\">subir su informe</a> y "
                "obtener un resumen claro y estructurado que explica sus valores de T3, T4 y TSH en "
                "lenguaje sencillo junto con los rangos de referencia. Este resumen le ayuda a ir a "
                "la cita con su médico mejor informado.</p>"
                "<p>Listo en pocos minutos, el informe destaca qué valores están dentro del rango y "
                "cuáles fuera, ayudándole a organizar sus preguntas antes de la visita. Para opciones "
                "y precios, consulte nuestra <a href=\"/pricing\">página de precios</a>.</p>"
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
            heading="T3 & T4: Ihre Schilddrüsenhormone verstehen",
            body_html=(
                "<p>Wenn Sie auf Ihrem Laborbefund die Werte <strong>T3</strong> und <strong>T4</strong> "
                "sehen, lautet die erste Frage häufig: Wofür stehen diese Hormone und sind meine Werte "
                "normal? Trijodthyronin (T3) und Thyroxin (T4) sind die wichtigsten Hormone der "
                "Schilddrüse. Sie spielen eine zentrale Rolle bei der Regulierung von Stoffwechsel, "
                "Energiehaushalt, Wachstum und Entwicklung. Da sie praktisch jede Zelle des Körpers "
                "beeinflussen, können Abweichungen Symptome von Müdigkeit und Gewichtsveränderungen "
                "bis hin zu Herzrhythmusstörungen und Haarausfall verursachen.</p>"
                "<p>Dieser Ratgeber erklärt, was T3 und T4 sind, worin sie sich unterscheiden, was "
                "die Referenzbereiche bedeuten und welche Ursachen hinter auffälligen Ergebnissen "
                "stecken können. Unser Ziel ist nicht die Diagnose, sondern Ihnen zu helfen, Ihre "
                "Ergebnisse besser zu verstehen, damit das Gespräch mit Ihrem Arzt ergiebiger "
                "wird.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="Was sind T3 und T4?",
            body_html=(
                "<p><strong>T3 (Trijodthyronin)</strong> und <strong>T4 (Thyroxin)</strong> werden "
                "von der schmetterlingsförmigen Schilddrüse im Hals produziert. T4 ist das "
                "Hauptprodukt und macht etwa 80 % des zirkulierenden Schilddrüsenhormons aus. "
                "Seine biologische Aktivität ist jedoch vergleichsweise gering; in den peripheren "
                "Geweben—vor allem Leber und Nieren—wird es durch enzymatische Abspaltung eines "
                "Jodatoms in das deutlich wirksamere T3 umgewandelt. T3 ist das eigentliche "
                "Effektorhormon, das den Zellstoffwechsel direkt beschleunigt.</p>"
                "<p>Beide Hormone steuern Proteinsynthese, Sauerstoffverbrauch, Herzleistung, "
                "Darmmotilität und Gehirnentwicklung. Im Kindesalter sind sie für Wachstum und "
                "neurologische Reifung unverzichtbar, im Erwachsenenalter halten sie den "
                "Grundumsatz aufrecht. Zu hohe oder zu niedrige Spiegel können nahezu jedes "
                "Organsystem sichtbar beeinflussen.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="T3 vs. T4: Was ist der Unterschied?",
            body_html=(
                "<p><strong>T4</strong> ist das primäre Schilddrüsenprodukt und zirkuliert in höherer "
                "Konzentration im Blut. Seine Halbwertszeit beträgt ca. 6–7 Tage, weshalb die "
                "Blutwerte über den Tag stabil bleiben und einen zuverlässigen Labormarker darstellen. "
                "<strong>T3</strong> ist 3- bis 5-mal wirksamer, kommt aber in deutlich geringeren "
                "Mengen vor und hat eine Halbwertszeit von nur rund einem Tag. Der Großteil des "
                "zirkulierenden T3 entsteht durch Konversion von T4 in peripheren Geweben.</p>"
                "<p>In der Praxis werden zunächst <em>freies T4</em> und <em>TSH</em> bestimmt. T3 "
                "wird ergänzt, wenn T4 normal ist, aber TSH supprimiert, oder bei Verdacht auf "
                "Hyperthyreose—denn einige Patienten zeigen eine isolierte T3-Erhöhung "
                "(<em>T3-Thyreotoxikose</em>). Die gemeinsame Betrachtung beider Hormone liefert "
                "das vollständigste Bild der Schilddrüsenfunktion.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="Freies vs. Gesamt-Hormon",
            body_html=(
                "<p>Der überwiegende Teil von T3 und T4 im Blut ist an <strong>Transportproteine"
                "</strong>—vor allem Thyroxin-bindendes Globulin (TBG)—gebunden. Diese gebundene "
                "Fraktion ist biologisch inaktiv; nur die <strong>freie (ungebundene)</strong> "
                "Fraktion kann in die Zellen gelangen und ihre Wirkung entfalten. Gesamt-T4 und "
                "Gesamt-T3 messen die Summe aus gebundener und freier Form, während freies T4 (FT4) "
                "und freies T3 (FT3) ausschließlich den aktiven Anteil erfassen.</p>"
                "<p>Schwangerschaft, Östrogentherapie, Lebererkrankungen oder genetische "
                "TBG-Varianten können die Transportproteinspiegel verändern und damit die "
                "Gesamtwerte verschieben, ohne die freie Hormonfraktion wesentlich zu beeinflussen. "
                "Deshalb stützt sich die moderne Schilddrüsendiagnostik bevorzugt auf "
                "<em>freie Hormon</em>-Messungen.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Referenzbereiche für T3 und T4",
            body_html=(
                "<p>Die folgende Tabelle zeigt die allgemein anerkannten Referenzbereiche für "
                "Schilddrüsenhormone bei Erwachsenen. Da die Messmethoden zwischen Laboren variieren, "
                "sind geringe Abweichungen normal; maßgeblich ist der Bereich auf Ihrem eigenen "
                "Befund.</p>"
                f'{_TBL}<thead><tr><th {_TH}>Test</th>'
                f'<th {_TH}>Referenzbereich</th></tr></thead><tbody>'
                f'<tr><td {_TD}>Freies T4</td><td {_TD}>0,8 – 1,8 ng/dL</td></tr>'
                f'<tr><td {_TD}>Freies T3</td><td {_TD}>2,3 – 4,2 pg/mL</td></tr>'
                f'<tr><td {_TD}>Gesamt-T4</td><td {_TD}>4,5 – 12,5 μg/dL</td></tr>'
                f'<tr><td {_TD}>Gesamt-T3</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0,4 – 4,0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>Diese Werte gelten für die allgemeine Erwachsenenbevölkerung. Schwangerschaft, "
                "Alter, Medikamente und chronische Erkrankungen können die Bereiche verschieben. "
                "Interpretieren Sie Ihre Ergebnisse stets im Zusammenhang mit dem Referenzbereich "
                "Ihres Labors und Ihrem klinischen Kontext.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="Ursachen für erhöhte T3- und T4-Werte (Hyperthyreose)",
            body_html=(
                "<p>Liegen T3 und/oder T4 über dem Referenzbereich, spricht man von "
                "<strong>Hyperthyreose</strong>. Die häufigsten Ursachen sind: "
                "<strong>Morbus Basedow</strong> (Autoantikörper regen die Schilddrüse zu übermäßiger "
                "Hormonproduktion an), <strong>toxische Knotenstruma</strong> (autonom arbeitende "
                "Schilddrüsenknoten), <strong>Thyreoiditis</strong> (Entzündung der Drüse, bei der "
                "gespeichertes Hormon freigesetzt wird) und <strong>Überdosierung von "
                "Schilddrüsenmedikamenten</strong>.</p>"
                "<p>Bei Hyperthyreose steigt der Stoffwechsel; Herzrasen, Gewichtsverlust, "
                "Schwitzen, Tremor, Nervosität und Durchfall können auftreten. Bei manchen Patienten "
                "ist nur T3 erhöht (<em>T3-Thyreotoxikose</em>), während T4 normal bleibt. Die "
                "Diagnose erfordert die Zusammenschau von klinischen Zeichen und Laborergebnissen.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="Ursachen für niedrige T3- und T4-Werte (Hypothyreose)",
            body_html=(
                "<p>Liegen T3 und/oder T4 unter dem Referenzbereich, spricht man von "
                "<strong>Hypothyreose</strong>. Die weltweit häufigste Ursache ist die "
                "<strong>Hashimoto-Thyreoiditis</strong>, bei der das Immunsystem Schilddrüsengewebe "
                "angreift und die Hormonproduktion schrittweise verringert. Weitere Ursachen sind "
                "<strong>Jodmangel</strong>, <strong>Hypophysenerkrankungen</strong> (sekundäre "
                "Hypothyreose), Zustand nach Schilddrüsen-OP oder Radiojodtherapie sowie "
                "<strong>bestimmte Medikamente</strong> (Lithium, Amiodaron).</p>"
                "<p>Bei Hypothyreose verlangsamt sich der Stoffwechsel; Müdigkeit, Gewichtszunahme, "
                "Kälteempfindlichkeit, Verstopfung, trockene Haut, Haarausfall und depressive "
                "Verstimmung sind häufig. Die Diagnose stützt sich in der Regel auf erhöhtes TSH "
                "bei erniedrigtem freiem T4; die Therapie besteht aus synthetischem Thyroxin "
                "(Levothyroxin).</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="Der Zusammenhang zwischen TSH, T3 und T4",
            body_html=(
                "<p><strong>TSH (thyreoideastimulierendes Hormon)</strong> wird von der Hypophyse "
                "ausgeschüttet und signalisiert der Schilddrüse, wie viel T3 und T4 sie produzieren "
                "soll. Sinkt der Schilddrüsenhormonspiegel, schüttet die Hypophyse mehr TSH aus "
                "(<em>negative Rückkopplung</em>); bei ausreichendem Hormonspiegel wird TSH "
                "supprimiert. Dieses dynamische Gleichgewicht hält den Stoffwechsel in einem engen "
                "Bereich.</p>"
                "<p>Klinisch ist TSH der empfindlichste Screening-Test: Bei früher Hypothyreose "
                "steigt TSH, bevor T4 absinkt (<em>subklinische Hypothyreose</em>); bei früher "
                "Hyperthyreose wird TSH supprimiert, bevor T4 deutlich erhöht ist. Ärzte bestimmen "
                "daher meist zuerst TSH und ergänzen bei Bedarf freies T4 und T3. Der allgemein "
                "akzeptierte Normalbereich für TSH liegt bei <strong>0,4–4,0 mIU/L</strong>, wobei "
                "individuelle Zielwerte nach Alter und klinischer Situation abweichen können.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome eines Schilddrüsenhormon-Ungleichgewichts",
            body_html=(
                "<p><strong>Hyperthyreose-Symptome:</strong> Herzrasen, Gewichtsverlust, übermäßiges "
                "Schwitzen, Wärmeintoleranz, Tremor (besonders der Hände), Unruhe, Schlaflosigkeit, "
                "häufiger Stuhlgang oder Durchfall, Muskelschwäche und Zyklusstörungen bei Frauen. "
                "Beim Morbus Basedow können Augensymptome (Exophthalmus) hinzukommen.</p>"
                "<p><strong>Hypothyreose-Symptome:</strong> Müdigkeit, Gewichtszunahme, "
                "Kälteempfindlichkeit, Verstopfung, trockene Haut, Haar- und Augenbrauenausfall, "
                "Ödeme (besonders im Gesicht), depressive Stimmung, Gedächtnisprobleme und "
                "Bradykardie. Da sich die Symptome schleichend entwickeln, werden sie von Betroffenen "
                "oft erst nach Monaten bemerkt.</p>"
                "<p>Bei beiden Zuständen sind die Symptome unspezifisch und reichen allein nicht für "
                "eine Diagnose. Labortests und klinische Beurteilung müssen gemeinsam betrachtet "
                "werden.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie zum Arzt?",
            body_html=(
                "<p>Wenn T3, T4 oder TSH außerhalb des Referenzbereichs liegen, ist ein Arztbesuch "
                "ratsam. Suchen Sie besonders dann ärztliche Hilfe, wenn Sie unerklärliche "
                "Gewichtsveränderungen, anhaltende Müdigkeit, Herzrasen, Tremor, Haarausfall, "
                "Verstopfung oder Durchfall, Stimmungsschwankungen oder eine sichtbare Schwellung "
                "am Hals bemerken.</p>"
                "<p>Frühzeitige Erkennung von Schilddrüsenerkrankungen verbessert den "
                "Behandlungserfolg. Menschen mit familiärer Vorbelastung, Autoimmunerkrankungen, "
                "Schwangere oder Frauen mit Kinderwunsch sowie Personen nach Bestrahlung im "
                "Halsbereich sollten regelmäßige Schilddrüsenkontrollen durchführen lassen. "
                "Selbst bei subklinischen Befunden kann Ihr Arzt einen Überwachungsplan "
                "empfehlen.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihre Schilddrüsenwerte zu verstehen",
            body_html=(
                "<p>Bei Norya stellen wir keine Diagnosen—wir helfen Ihnen, Ihren Laborbefund zu "
                "verstehen und gut vorbereitet zum Arzt zu gehen. Sie können "
                "<a href=\"/analyze\">Ihren Befund hochladen</a> und erhalten eine klare, "
                "strukturierte Auswertung, die Ihre T3-, T4- und TSH-Werte in einfacher Sprache "
                "mit Referenzbereichen erklärt. So wird das Arztgespräch ergiebiger.</p>"
                "<p>Der Bericht ist in wenigen Minuten fertig und zeigt übersichtlich, welche Werte "
                "im Normbereich liegen und welche auffällig sind. Optionen und Preise finden Sie auf "
                "unserer <a href=\"/pricing\">Preisseite</a>.</p>"
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
            heading="T3 et T4 : comprendre vos hormones thyroïdiennes",
            body_html=(
                "<p>Lorsque vous voyez les valeurs <strong>T3</strong> et <strong>T4</strong> sur "
                "votre bilan sanguin, la première question est souvent : à quoi servent ces hormones "
                "et mes résultats sont-ils normaux ? La triiodothyronine (T3) et la thyroxine (T4) "
                "sont les principales hormones produites par la glande thyroïde. Elles jouent un rôle "
                "central dans la régulation du métabolisme, de la production d'énergie, de la "
                "croissance et du développement. Parce qu'elles influencent pratiquement chaque "
                "cellule du corps, des niveaux anormaux peuvent se manifester par des symptômes allant "
                "de la fatigue aux troubles du rythme cardiaque en passant par les variations de "
                "poids et la chute de cheveux.</p>"
                "<p>Ce guide explique ce que sont la T3 et la T4, leurs différences, la signification "
                "des fourchettes de référence et les causes possibles de résultats anormaux. Notre "
                "objectif n'est pas de diagnostiquer mais de vous aider à comprendre vos résultats "
                "afin que la discussion avec votre médecin soit plus productive.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="Que sont la T3 et la T4 ?",
            body_html=(
                "<p>La <strong>T3 (triiodothyronine)</strong> et la <strong>T4 (thyroxine)</strong> "
                "sont des hormones produites par la glande thyroïde en forme de papillon située dans "
                "le cou. La T4 est le principal produit de sécrétion et représente environ 80 % de "
                "l'hormone thyroïdienne circulante. Son activité biologique est cependant relativement "
                "faible ; elle est convertie dans les tissus périphériques—principalement le foie et "
                "les reins—en T3, plus puissante, par retrait enzymatique d'un atome d'iode. La T3 "
                "est l'hormone effectrice qui accélère directement le métabolisme cellulaire.</p>"
                "<p>Ensemble, ces hormones régulent la synthèse protéique, la consommation d'oxygène, "
                "le débit cardiaque, la motilité intestinale et le développement cérébral. Pendant "
                "l'enfance elles sont essentielles à la croissance et à la maturation neurologique ; "
                "chez l'adulte elles maintiennent le métabolisme de base. Des niveaux trop élevés ou "
                "trop bas peuvent affecter pratiquement tous les systèmes organiques.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="T3 vs T4 : quelle différence ?",
            body_html=(
                "<p>La <strong>T4</strong> est le produit principal de la thyroïde et circule à des "
                "concentrations plus élevées. Sa demi-vie est d'environ 6–7 jours, ce qui rend les "
                "taux sanguins stables et en fait un marqueur de laboratoire fiable. La "
                "<strong>T3</strong> est 3 à 5 fois plus puissante mais circule en quantités bien "
                "moindres ; sa demi-vie n'est que d'environ 1 jour. La majeure partie de la T3 "
                "circulante provient de la conversion périphérique de la T4.</p>"
                "<p>En pratique clinique, on mesure d'abord la <em>T4 libre</em> et la <em>TSH</em>. "
                "La T3 est ajoutée lorsque la T4 est normale mais la TSH supprimée, ou en cas de "
                "suspicion d'hyperthyroïdie, car certains patients présentent une élévation isolée "
                "de la T3 (<em>thyrotoxicose à T3</em>). L'évaluation conjointe des deux hormones "
                "donne l'image la plus complète de la fonction thyroïdienne.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="Hormone libre vs totale",
            body_html=(
                "<p>La majorité de la T3 et de la T4 circulantes est liée à des <strong>protéines "
                "de transport</strong>, principalement la TBG (thyroxin-binding globulin). La "
                "fraction liée est biologiquement inactive ; seule la <strong>fraction libre "
                "(non liée)</strong> peut pénétrer dans les cellules et exercer ses effets "
                "métaboliques. La T4 totale et la T3 totale mesurent la somme des formes liées et "
                "libres, tandis que la T4 libre (FT4) et la T3 libre (FT3) ne mesurent que la "
                "partie active non liée.</p>"
                "<p>La grossesse, un traitement œstrogénique, les maladies hépatiques ou les "
                "variants génétiques de la TBG peuvent modifier les niveaux de protéines de "
                "transport, faisant varier les valeurs totales sans nécessairement changer la "
                "concentration d'hormone libre. C'est pourquoi l'évaluation thyroïdienne moderne "
                "repose principalement sur les mesures d'<em>hormone libre</em>.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Fourchettes de référence de la T3 et de la T4",
            body_html=(
                "<p>Le tableau ci-dessous présente les fourchettes de référence couramment admises "
                "pour les hormones thyroïdiennes chez l'adulte. Les méthodologies variant entre "
                "laboratoires, de légères différences sont normales ; référez-vous toujours aux "
                "valeurs imprimées sur votre propre compte rendu.</p>"
                f'{_TBL}<thead><tr><th {_TH}>Examen</th>'
                f'<th {_TH}>Fourchette normale</th></tr></thead><tbody>'
                f'<tr><td {_TD}>T4 libre</td><td {_TD}>0,8 – 1,8 ng/dL</td></tr>'
                f'<tr><td {_TD}>T3 libre</td><td {_TD}>2,3 – 4,2 pg/mL</td></tr>'
                f'<tr><td {_TD}>T4 totale</td><td {_TD}>4,5 – 12,5 μg/dL</td></tr>'
                f'<tr><td {_TD}>T3 totale</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0,4 – 4,0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>Ces valeurs concernent la population adulte générale. La grossesse, l'âge, les "
                "médicaments et les maladies chroniques peuvent modifier les fourchettes. Interprétez "
                "toujours vos résultats en tenant compte du référentiel de votre laboratoire et de "
                "votre contexte clinique.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="Causes de T3 et T4 élevées (hyperthyroïdie)",
            body_html=(
                "<p>Lorsque les niveaux de T3 et/ou T4 dépassent la fourchette de référence, on "
                "parle d'<strong>hyperthyroïdie</strong>. Les causes les plus fréquentes sont : "
                "la <strong>maladie de Basedow</strong> (des auto-anticorps stimulent la thyroïde à "
                "surproduire), le <strong>goitre multinodulaire toxique</strong> (nodules autonomes), "
                "la <strong>thyroïdite</strong> (inflammation libérant l'hormone stockée) et un "
                "<strong>excès de médicament thyroïdien</strong>.</p>"
                "<p>L'hyperthyroïdie accélère le métabolisme, pouvant provoquer palpitations, perte "
                "de poids, transpiration excessive, tremblements, nervosité et diarrhée. Chez "
                "certains patients seule la T3 est élevée (<em>thyrotoxicose à T3</em>) tandis que "
                "la T4 reste normale. Le diagnostic repose sur la combinaison des signes cliniques "
                "et des résultats de laboratoire.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="Causes de T3 et T4 basses (hypothyroïdie)",
            body_html=(
                "<p>Lorsque les niveaux de T3 et/ou T4 sont inférieurs à la fourchette de référence, "
                "on parle d'<strong>hypothyroïdie</strong>. La cause la plus fréquente dans le monde "
                "est la <strong>thyroïdite de Hashimoto</strong>, une maladie auto-immune dans "
                "laquelle le système immunitaire attaque le tissu thyroïdien, réduisant "
                "progressivement la production hormonale. Parmi les autres causes : la "
                "<strong>carence en iode</strong>, les <strong>maladies hypophysaires</strong> "
                "(hypothyroïdie secondaire), l'état post-chirurgical ou post-iode radioactif et "
                "<strong>certains médicaments</strong> (lithium, amiodarone).</p>"
                "<p>L'hypothyroïdie ralentit le métabolisme, entraînant fatigue, prise de poids, "
                "frilosité, constipation, peau sèche, chute de cheveux, œdème facial, humeur "
                "dépressive, troubles de la mémoire et bradycardie. Le diagnostic repose "
                "généralement sur une TSH élevée associée à une T4 libre basse ; le traitement "
                "consiste en un remplacement par thyroxine synthétique (lévothyroxine).</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="Le lien entre TSH, T3 et T4",
            body_html=(
                "<p>La <strong>TSH (thyréostimuline)</strong> est sécrétée par l'hypophyse et "
                "indique à la thyroïde combien de T3 et T4 produire. Lorsque les hormones "
                "thyroïdiennes baissent, l'hypophyse libère davantage de TSH pour stimuler la "
                "glande (<em>rétrocontrôle négatif</em>) ; lorsque les taux sont suffisants, la "
                "TSH est supprimée. Cet équilibre dynamique maintient le métabolisme dans une "
                "fourchette étroite.</p>"
                "<p>En clinique, la TSH est le test de dépistage le plus sensible : dans "
                "l'hypothyroïdie débutante, la TSH monte avant que la T4 ne baisse "
                "(<em>hypothyroïdie subclinique</em>) ; dans l'hyperthyroïdie débutante, la TSH "
                "est supprimée avant que la T4 ne soit franchement élevée. Les médecins dosent donc "
                "d'abord la TSH, puis complètent si nécessaire avec T4 et T3 libres. La fourchette "
                "normale de la TSH est généralement de <strong>0,4–4,0 mIU/L</strong>, bien que "
                "les cibles individuelles puissent varier selon l'âge et le contexte clinique.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d'un déséquilibre des hormones thyroïdiennes",
            body_html=(
                "<p><strong>Symptômes d'hyperthyroïdie :</strong> palpitations, perte de poids "
                "involontaire, transpiration excessive, intolérance à la chaleur, tremblements "
                "(surtout des mains), agitation, insomnie, transit accéléré ou diarrhée, faiblesse "
                "musculaire et irrégularités menstruelles. Dans la maladie de Basedow, des anomalies "
                "oculaires (exophtalmie) peuvent s'y ajouter.</p>"
                "<p><strong>Symptômes d'hypothyroïdie :</strong> fatigue, prise de poids, frilosité, "
                "constipation, peau sèche, amincissement des cheveux et des sourcils, œdème "
                "(surtout au visage), humeur dépressive, troubles de la mémoire et bradycardie. Les "
                "symptômes apparaissant progressivement, le patient peut ne pas les remarquer pendant "
                "des mois, voire des années.</p>"
                "<p>Dans les deux cas, les symptômes sont non spécifiques et ne suffisent pas à "
                "confirmer un diagnostic. Les tests de laboratoire et l'évaluation clinique doivent "
                "être considérés ensemble.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si l'un de vos taux de T3, T4 ou TSH sort de la fourchette de référence, il "
                "est recommandé de consulter un médecin. Consultez en particulier en cas de "
                "variations de poids inexpliquées, fatigue persistante, palpitations, tremblements, "
                "chute de cheveux, constipation ou diarrhée, troubles de l'humeur ou gonflement "
                "visible au niveau du cou.</p>"
                "<p>Le dépistage précoce des troubles thyroïdiens améliore les résultats du "
                "traitement. Les personnes ayant des antécédents familiaux de maladie thyroïdienne, "
                "celles souffrant de maladies auto-immunes, les femmes enceintes ou en projet de "
                "grossesse, et toute personne ayant reçu une radiothérapie cervicale devraient "
                "effectuer des bilans thyroïdiens réguliers. Même en cas de résultats subcliniques, "
                "votre médecin peut recommander un suivi.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre vos résultats thyroïdiens",
            body_html=(
                "<p>Chez Norya, nous ne posons pas de diagnostic—nous facilitons la compréhension de "
                "votre bilan sanguin et votre préparation au rendez-vous médical. Vous pouvez "
                "<a href=\"/analyze\">envoyer votre bilan</a> et obtenir un résumé clair et "
                "structuré qui explique vos valeurs de T3, T4 et TSH en langage simple avec les "
                "fourchettes de référence. Ce résumé vous permet d'arriver mieux préparé chez votre "
                "médecin.</p>"
                "<p>Prêt en quelques minutes, le rapport met en évidence les valeurs dans la norme "
                "et celles qui en sortent, vous aidant à organiser vos questions avant la "
                "consultation. Pour les options et les tarifs, consultez notre "
                "<a href=\"/pricing\">page tarifs</a>.</p>"
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
            heading="T3 e T4: capire gli ormoni tiroidei",
            body_html=(
                "<p>Quando sul referto delle analisi del sangue trovate i valori di <strong>T3</strong> "
                "e <strong>T4</strong>, la prima domanda è spesso: a cosa servono questi ormoni e i "
                "miei risultati sono nella norma? La triiodotironina (T3) e la tiroxina (T4) sono i "
                "principali ormoni prodotti dalla ghiandola tiroidea e svolgono un ruolo centrale "
                "nella regolazione del metabolismo, della produzione di energia, della crescita e "
                "dello sviluppo. Poiché influenzano praticamente ogni cellula del corpo, livelli "
                "anomali possono manifestarsi con sintomi che vanno dalla stanchezza alle variazioni "
                "di peso, dalle alterazioni del battito cardiaco alla caduta dei capelli.</p>"
                "<p>Questa guida spiega cosa sono T3 e T4, in che cosa si differenziano, cosa "
                "significano gli intervalli di riferimento e quali possono essere le cause di "
                "risultati anomali. Il nostro obiettivo non è formulare diagnosi, ma aiutarvi a "
                "comprendere i risultati per affrontare il colloquio con il medico in modo più "
                "consapevole.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="Cosa sono T3 e T4?",
            body_html=(
                "<p>La <strong>T3 (triiodotironina)</strong> e la <strong>T4 (tiroxina)</strong> "
                "sono ormoni prodotti dalla ghiandola tiroidea, a forma di farfalla, situata nella "
                "parte anteriore del collo. La T4 è il principale prodotto di secrezione e "
                "rappresenta circa l'80 % dell'ormone tiroideo circolante. Tuttavia la sua attività "
                "biologica è relativamente bassa; viene convertita nei tessuti periferici—soprattutto "
                "fegato e reni—nella più potente T3 mediante rimozione enzimatica di un atomo di "
                "iodio. La T3 è l'ormone effettore che accelera direttamente il metabolismo "
                "cellulare.</p>"
                "<p>Insieme, questi ormoni regolano la sintesi proteica, il consumo di ossigeno, la "
                "gittata cardiaca, la motilità intestinale e lo sviluppo cerebrale. Nell'infanzia "
                "sono essenziali per crescita e maturazione neurologica, mentre nell'adulto "
                "mantengono il metabolismo basale. Livelli troppo alti o troppo bassi possono "
                "ripercuotersi su praticamente ogni sistema dell'organismo.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="Differenza tra T3 e T4",
            body_html=(
                "<p>La <strong>T4</strong> è il prodotto principale della tiroide e circola a "
                "concentrazioni più elevate nel sangue. La sua emivita è di circa 6–7 giorni, il che "
                "rende i livelli ematici stabili e un marcatore di laboratorio affidabile. La "
                "<strong>T3</strong> è da 3 a 5 volte più potente della T4 ma circola in quantità "
                "molto inferiori, con un'emivita di circa 1 giorno. La maggior parte della T3 "
                "circolante deriva dalla conversione periferica della T4.</p>"
                "<p>Nella pratica clinica si misurano prima la <em>T4 libera</em> e la <em>TSH</em>. "
                "La T3 viene aggiunta quando la T4 è normale ma la TSH è soppressa, oppure quando si "
                "sospetta ipertiroidismo, poiché alcuni pazienti presentano un'elevazione isolata "
                "della T3 (<em>tireotossicosi da T3</em>). La valutazione congiunta di entrambi gli "
                "ormoni fornisce il quadro più completo della funzione tiroidea.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="Ormone libero vs totale",
            body_html=(
                "<p>La maggior parte della T3 e della T4 in circolo è legata a <strong>proteine di "
                "trasporto</strong>, in primis la TBG (thyroxine-binding globulin). La frazione "
                "legata è biologicamente inattiva; solo la <strong>frazione libera (non legata)"
                "</strong> può entrare nelle cellule ed esercitare effetti metabolici. La T4 totale "
                "e la T3 totale misurano la somma delle forme legate e libere, mentre la T4 libera "
                "(FT4) e la T3 libera (FT3) misurano esclusivamente la porzione attiva non legata.</p>"
                "<p>Gravidanza, terapia estrogenica, malattie epatiche o varianti genetiche della TBG "
                "possono alterare i livelli delle proteine di trasporto, modificando i valori totali "
                "senza necessariamente cambiare la concentrazione di ormone libero. Per questo motivo "
                "la valutazione tiroidea moderna si basa prevalentemente sulle misurazioni "
                "dell'<em>ormone libero</em>.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Intervalli di riferimento per T3 e T4",
            body_html=(
                "<p>La tabella seguente riporta gli intervalli di riferimento generalmente accettati "
                "per gli ormoni tiroidei negli adulti. Poiché le metodiche variano tra i laboratori, "
                "lievi differenze sono normali; fate sempre riferimento all'intervallo indicato sul "
                "vostro referto.</p>"
                f'{_TBL}<thead><tr><th {_TH}>Esame</th>'
                f'<th {_TH}>Intervallo normale</th></tr></thead><tbody>'
                f'<tr><td {_TD}>T4 libera</td><td {_TD}>0,8 – 1,8 ng/dL</td></tr>'
                f'<tr><td {_TD}>T3 libera</td><td {_TD}>2,3 – 4,2 pg/mL</td></tr>'
                f'<tr><td {_TD}>T4 totale</td><td {_TD}>4,5 – 12,5 μg/dL</td></tr>'
                f'<tr><td {_TD}>T3 totale</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0,4 – 4,0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>Questi valori riguardano la popolazione adulta generale. Gravidanza, età, farmaci "
                "e patologie croniche possono modificare gli intervalli. Interpretate sempre i "
                "risultati insieme all'intervallo di riferimento del vostro laboratorio e al contesto "
                "clinico.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="Cause di T3 e T4 alte (ipertiroidismo)",
            body_html=(
                "<p>Quando i livelli di T3 e/o T4 superano l'intervallo di riferimento si parla di "
                "<strong>ipertiroidismo</strong>. Le cause più frequenti sono: il <strong>morbo di "
                "Basedow-Graves</strong> (autoanticorpi stimolano la tiroide a produrre ormone in "
                "eccesso), il <strong>gozzo multinodulare tossico</strong> (noduli tiroidei "
                "autonomi), la <strong>tiroidite</strong> (infiammazione che rilascia l'ormone "
                "immagazzinato) e l'<strong>eccesso di farmaco tiroideo</strong>.</p>"
                "<p>L'ipertiroidismo accelera il metabolismo e può causare palpitazioni, perdita di "
                "peso, sudorazione eccessiva, tremori, nervosismo e diarrea. In alcuni pazienti solo "
                "la T3 è elevata (<em>tireotossicosi da T3</em>) mentre la T4 resta normale. La "
                "diagnosi richiede la combinazione di segni clinici e risultati di laboratorio.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="Cause di T3 e T4 basse (ipotiroidismo)",
            body_html=(
                "<p>Quando i livelli di T3 e/o T4 scendono sotto l'intervallo di riferimento si "
                "parla di <strong>ipotiroidismo</strong>. La causa più comune al mondo è la "
                "<strong>tiroidite di Hashimoto</strong>, una malattia autoimmune in cui il sistema "
                "immunitario attacca il tessuto tiroideo, riducendo progressivamente la produzione "
                "ormonale. Altre cause includono la <strong>carenza di iodio</strong>, le "
                "<strong>malattie ipofisarie</strong> (ipotiroidismo secondario), lo stato post-"
                "chirurgico o post-radioiodio e <strong>alcuni farmaci</strong> (litio, "
                "amiodarone).</p>"
                "<p>Nell'ipotiroidismo il metabolismo rallenta, provocando stanchezza, aumento di "
                "peso, intolleranza al freddo, stitichezza, pelle secca, perdita di capelli, edema "
                "facciale, umore depresso, difficoltà di memoria e bradicardia. La diagnosi si basa "
                "di solito su TSH elevato con T4 libera bassa; il trattamento consiste nella "
                "sostituzione con tiroxina sintetica (levotiroxina).</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="Il legame tra TSH, T3 e T4",
            body_html=(
                "<p>Il <strong>TSH (ormone tireostimolante)</strong> è secreto dall'ipofisi e indica "
                "alla tiroide quanta T3 e T4 produrre. Quando i livelli di ormone tiroideo scendono, "
                "l'ipofisi rilascia più TSH per stimolare la ghiandola (<em>feedback negativo</em>); "
                "quando i livelli sono adeguati, il TSH viene soppresso. Questo equilibrio dinamico "
                "mantiene il metabolismo in un intervallo ristretto.</p>"
                "<p>In clinica, il TSH è il test di screening più sensibile: nell'ipotiroidismo "
                "iniziale il TSH sale prima che la T4 scenda (<em>ipotiroidismo subclinico</em>); "
                "nell'ipertiroidismo iniziale il TSH è soppresso prima che la T4 risulti "
                "francamente elevata. Per questo i medici dosano prima il TSH e aggiungono T4 e T3 "
                "libere se necessario. L'intervallo normale del TSH è generalmente "
                "<strong>0,4–4,0 mIU/L</strong>, sebbene gli obiettivi individuali possano variare "
                "con l'età e il contesto clinico.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi dello squilibrio degli ormoni tiroidei",
            body_html=(
                "<p><strong>Sintomi di ipertiroidismo:</strong> palpitazioni, perdita di peso "
                "involontaria, sudorazione eccessiva, intolleranza al caldo, tremori (soprattutto "
                "alle mani), irrequietezza, insonnia, aumento della frequenza delle evacuazioni o "
                "diarrea, debolezza muscolare e irregolarità mestruali nelle donne. Nel morbo di "
                "Basedow possono comparire alterazioni oculari (esoftalmo).</p>"
                "<p><strong>Sintomi di ipotiroidismo:</strong> stanchezza, aumento di peso, "
                "intolleranza al freddo, stitichezza, pelle secca, diradamento di capelli e "
                "sopracciglia, edema (soprattutto al viso), umore depresso, problemi di memoria e "
                "bradicardia. Poiché i sintomi si sviluppano gradualmente, possono passare mesi o "
                "anni prima che il paziente li noti.</p>"
                "<p>In entrambe le condizioni i sintomi sono aspecifici e non bastano da soli a "
                "confermare una diagnosi. Esami di laboratorio e valutazione clinica vanno "
                "considerati insieme.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se uno qualsiasi dei vostri valori di T3, T4 o TSH è fuori dall'intervallo di "
                "riferimento, è consigliabile consultare un medico. Rivolgetevi in particolare se "
                "notate variazioni di peso inspiegabili, stanchezza persistente, palpitazioni, "
                "tremori, caduta dei capelli, stitichezza o diarrea, alterazioni dell'umore o un "
                "rigonfiamento visibile al collo.</p>"
                "<p>La diagnosi precoce dei disturbi tiroidei migliora gli esiti del trattamento. "
                "Le persone con familiarità per malattie tiroidee, chi soffre di patologie "
                "autoimmuni, le donne in gravidanza o che la pianificano, e chiunque abbia ricevuto "
                "radioterapia al collo dovrebbero sottoporsi a controlli tiroidei regolari. Anche in "
                "caso di risultati subclinici, il medico può raccomandare un piano di "
                "monitoraggio.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya vi aiuta a capire i risultati tiroidei",
            body_html=(
                "<p>In Norya non facciamo diagnosi—vi aiutiamo a comprendere le vostre analisi del "
                "sangue e a presentarvi preparati dal medico. Potete "
                "<a href=\"/analyze\">caricare il referto</a> e ottenere un riepilogo chiaro e "
                "strutturato che spiega i valori di T3, T4 e TSH in linguaggio semplice con gli "
                "intervalli di riferimento. Questo riepilogo vi permette di arrivare alla visita "
                "più informati.</p>"
                "<p>Pronto in pochi minuti, il report evidenzia quali valori sono nella norma e "
                "quali ne escono, aiutandovi a organizzare le domande prima dell'appuntamento. Per "
                "opzioni e prezzi, consultate la nostra <a href=\"/pricing\">pagina prezzi</a>.</p>"
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
            heading="T3 ו-T4: להבין את הורמוני בלוטת התריס",
            body_html=(
                "<p>כשאתם רואים את ערכי <strong>T3</strong> ו-<strong>T4</strong> בתוצאות בדיקת הדם, "
                "השאלה הראשונה היא בדרך כלל: מה ההורמונים האלה עושים והאם התוצאות שלי תקינות? "
                "טריודותירונין (T3) ותירוקסין (T4) הם ההורמונים העיקריים שמייצרת בלוטת התריס, והם ממלאים "
                "תפקיד מרכזי בוויסות חילוף החומרים, ייצור אנרגיה, צמיחה והתפתחות. מכיוון שהם משפיעים "
                "על כמעט כל תא בגוף, רמות חריגות עלולות להתבטא בתסמינים מעייפות ושינויי משקל ועד הפרעות "
                "בקצב הלב ונשירת שיער.</p>"
                "<p>מדריך זה מסביר מהם T3 ו-T4, מה ההבדל ביניהם, מה המשמעות של טווחי הייחוס ומה עלול "
                "לגרום לתוצאות חריגות. המטרה שלנו אינה לאבחן אלא לעזור לכם להבין את התוצאות כדי "
                "שהשיחה עם הרופא תהיה פרודוקטיבית יותר.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="מהם T3 ו-T4?",
            body_html=(
                "<p><strong>T3 (טריודותירונין)</strong> ו-<strong>T4 (תירוקסין)</strong> הם הורמונים "
                "המיוצרים על ידי בלוטת התריס בצורת פרפר הממוקמת בצוואר. T4 הוא המוצר העיקרי של "
                "הבלוטה ומהווה כ-80% מהורמון התריס בדם. אולם הפעילות הביולוגית שלו נמוכה יחסית; הוא "
                "עובר המרה ברקמות היקפיות — בעיקר בכבד ובכליות — ל-T3 הפעיל יותר, על ידי הסרה "
                "אנזימטית של אטום יוד אחד. T3 הוא ההורמון האפקטורי שמאיץ ישירות את חילוף החומרים "
                "בתאים.</p>"
                "<p>יחד, הורמונים אלה מווסתים סינתזת חלבונים, צריכת חמצן, תפוקת לב, תנועתיות מעיים "
                "והתפתחות מוחית. בילדות הם חיוניים לצמיחה ולהבשלה נוירולוגית, ובבגרות הם שומרים על "
                "קצב חילוף החומרים הבסיסי. רמות גבוהות או נמוכות מדי עלולות להשפיע על כמעט כל מערכת "
                "איברים בגוף.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="T3 מול T4: מה ההבדל?",
            body_html=(
                "<p><strong>T4</strong> הוא המוצר העיקרי של בלוטת התריס וזורם בדם בריכוזים גבוהים "
                "יותר. זמן מחצית החיים שלו כ-6–7 ימים, ולכן רמותיו בדם יציבות יחסית ומהוות סמן "
                "מעבדתי אמין. <strong>T3</strong> חזק פי 3–5 מ-T4, אך זורם בכמויות הרבה יותר קטנות "
                "וזמן מחצית החיים שלו כיום אחד בלבד. רוב ה-T3 בדם נוצר מהמרת T4 ברקמות "
                "היקפיות.</p>"
                "<p>בפרקטיקה הקלינית נמדדים תחילה <em>T4 חופשי</em> ו-<em>TSH</em>. T3 נוסף כאשר T4 "
                "תקין אך TSH מדוכא, או כשיש חשד קליני ליתר פעילות התריס — כי חלק מהמטופלים מציגים "
                "עלייה מבודדת ב-T3 (<em>תירוטוקסיקוזיס מ-T3</em>). הערכת שני ההורמונים יחד מספקת "
                "את התמונה המלאה ביותר של תפקוד בלוטת התריס.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="הורמון חופשי מול כולל",
            body_html=(
                "<p>רוב ה-T3 וה-T4 בדם קשורים ל<strong>חלבוני נשא</strong> — בעיקר TBG (Thyroxine-"
                "Binding Globulin). הפרקציה הקשורה אינה פעילה ביולוגית; רק הפרקציה <strong>החופשית "
                "(הלא-קשורה)</strong> יכולה להיכנס לתאים ולהשפיע על חילוף החומרים. T4 כולל ו-T3 כולל "
                "מודדים את הסכום של צורות קשורות וחופשיות, בעוד T4 חופשי (FT4) ו-T3 חופשי (FT3) מודדים "
                "רק את החלק הפעיל הלא-קשור.</p>"
                "<p>הריון, טיפול באסטרוגן, מחלות כבד או וריאנטים גנטיים של TBG עלולים לשנות את רמות "
                "חלבוני הנשא ובכך להשפיע על ערכים כוללים מבלי לשנות בהכרח את ריכוז ההורמון החופשי. "
                "לכן ההערכה המודרנית של תפקוד התריס מסתמכת בעיקר על מדידת <em>הורמון חופשי</em>.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ייחוס ל-T3 ול-T4",
            body_html=(
                "<p>הטבלה הבאה מציגה את טווחי הייחוס המקובלים להורמוני בלוטת התריס במבוגרים. "
                "מכיוון שהמתודולוגיות משתנות בין מעבדות, הבדלים קלים הם נורמליים; עיינו תמיד בטווח "
                "המצוין בדו\"ח שלכם.</p>"
                f'{_TBL}<thead><tr><th {_TH}>בדיקה</th>'
                f'<th {_TH}>טווח תקין</th></tr></thead><tbody>'
                f'<tr><td {_TD}>T4 חופשי</td><td {_TD}>0.8 – 1.8 ng/dL</td></tr>'
                f'<tr><td {_TD}>T3 חופשי</td><td {_TD}>2.3 – 4.2 pg/mL</td></tr>'
                f'<tr><td {_TD}>T4 כולל</td><td {_TD}>4.5 – 12.5 μg/dL</td></tr>'
                f'<tr><td {_TD}>T3 כולל</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0.4 – 4.0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>ערכים אלה מתייחסים לאוכלוסייה הבוגרת הכללית. הריון, גיל, תרופות ומחלות כרוניות "
                "עשויים לשנות את הטווחים. פרשו תמיד את התוצאות יחד עם טווח הייחוס של המעבדה שלכם "
                "ועם ההקשר הקליני.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="גורמים ל-T3 ו-T4 גבוהים (יתר פעילות התריס)",
            body_html=(
                "<p>כאשר רמות T3 ו/או T4 מעל טווח הייחוס, המצב נקרא <strong>היפרתירואידיזם</strong> "
                "(יתר פעילות בלוטת התריס). הגורמים הנפוצים ביותר הם: <strong>מחלת גרייבס</strong> "
                "(נוגדנים עצמיים מגרים את הבלוטה לייצר הורמון ביתר), <strong>זפק רב-גושי רעיל</strong> "
                "(גושים אוטונומיים), <strong>דלקת בלוטת התריס</strong> (תהליך דלקתי שמשחרר הורמון "
                "מאוחסן לזרם הדם) ו<strong>מינון יתר של תרופות לתריס</strong>.</p>"
                "<p>ביתר פעילות התריס קצב חילוף החומרים עולה ועלולים להופיע דפיקות לב, ירידה במשקל, "
                "הזעה יתרה, רעד, עצבנות ושלשולים. בחלק מהמטופלים רק T3 מוגבר (<em>תירוטוקסיקוזיס "
                "מ-T3</em>) בעוד T4 תקין. האבחנה מחייבת שילוב של סימנים קליניים עם ממצאי "
                "מעבדה.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="גורמים ל-T3 ו-T4 נמוכים (תת-פעילות התריס)",
            body_html=(
                "<p>כאשר רמות T3 ו/או T4 מתחת לטווח הייחוס, המצב נקרא <strong>היפותירואידיזם</strong> "
                "(תת-פעילות בלוטת התריס). הגורם הנפוץ ביותר בעולם הוא <strong>דלקת תריס של "
                "האשימוטו</strong>, מחלה אוטואימונית שבה מערכת החיסון תוקפת את רקמת התריס ומפחיתה "
                "בהדרגה את ייצור ההורמון. גורמים נוספים: <strong>חוסר ביוד</strong>, <strong>מחלות של "
                "בלוטת יותרת המוח</strong> (היפותירואידיזם שניוני), מצב לאחר ניתוח או יוד רדיואקטיבי "
                "ו<strong>תרופות מסוימות</strong> (ליתיום, אמיודרון).</p>"
                "<p>בתת-פעילות התריס חילוף החומרים מואט ועלולים להופיע עייפות, עלייה במשקל, רגישות "
                "לקור, עצירות, עור יבש, נשירת שיער, נפיחות בפנים, מצב רוח ירוד, קשיי זיכרון "
                "וברדיקרדיה. האבחנה מבוססת בדרך כלל על TSH גבוה בשילוב T4 חופשי נמוך; הטיפול כולל "
                "תחליף תירוקסין סינתטי (לבותירוקסין).</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="הקשר בין TSH, T3 ו-T4",
            body_html=(
                "<p><strong>TSH (הורמון מגרה בלוטת התריס)</strong> מופרש מבלוטת יותרת המוח ומורה "
                "לבלוטת התריס כמה T3 ו-T4 לייצר. כשרמות הורמון התריס בדם יורדות, יותרת המוח משחררת "
                "יותר TSH כדי לגרות את הבלוטה (<em>משוב שלילי</em>); כשהרמות מספיקות, ה-TSH מדוכא. "
                "שיווי משקל דינמי זה שומר על קצב חילוף החומרים בטווח צר.</p>"
                "<p>קלינית, TSH הוא בדיקת הסקר הרגישה ביותר: בהיפותירואידיזם מוקדם TSH עולה לפני "
                "ש-T4 יורד מתחת לנורמה (<em>היפותירואידיזם תת-קליני</em>); בהיפרתירואידיזם מוקדם TSH "
                "מדוכא לפני ש-T4 עולה בבירור. לכן רופאים בודקים בדרך כלל תחילה TSH ומוסיפים T4 ו-T3 "
                "חופשיים בהתאם לצורך. הטווח התקין של TSH מקובל כ-<strong>0.4–4.0 mIU/L</strong>, אם "
                "כי יעדים אישיים עשויים להשתנות לפי גיל והקשר קליני.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של חוסר איזון בהורמוני התריס",
            body_html=(
                "<p><strong>תסמיני יתר פעילות:</strong> דפיקות לב, ירידה לא מכוונת במשקל, הזעה "
                "מוגברת, אי-סבילות לחום, רעד (בעיקר בידיים), אי-שקט, נדודי שינה, תנועות מעיים "
                "תכופות או שלשולים, חולשת שרירים והפרעות במחזור אצל נשים. במחלת גרייבס עלולים להופיע "
                "ממצאים עיניים (אקזופתלמוס).</p>"
                "<p><strong>תסמיני תת-פעילות:</strong> עייפות, עלייה במשקל, רגישות לקור, עצירות, עור "
                "יבש, דילול שיער וגבות, בצקת (בעיקר בפנים), מצב רוח ירוד, בעיות זיכרון וברדיקרדיה. "
                "מכיוון שהתסמינים מתפתחים בהדרגה, המטופל עשוי שלא להבחין בהם במשך חודשים ואף "
                "שנים.</p>"
                "<p>בשני המצבים התסמינים אינם ספציפיים ואינם מספיקים לבדם לאשר אבחנה. בדיקות מעבדה "
                "והערכה קלינית חייבות להילקח בחשבון יחד.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם אחד מערכי ה-T3, T4 או TSH שלכם חורג מטווח הייחוס, מומלץ להתייעץ עם רופא. "
                "פנו במיוחד אם אתם מבחינים בשינויי משקל לא מוסברים, עייפות מתמשכת, דפיקות לב, רעד, "
                "נשירת שיער, עצירות או שלשולים, שינויים במצב הרוח או נפיחות נראית לעין בצוואר.</p>"
                "<p>גילוי מוקדם של הפרעות בתריס משפר את תוצאות הטיפול. אנשים עם היסטוריה משפחתית של "
                "מחלת תריס, סובלים ממחלות אוטואימוניות, נשים בהריון או המתכננות הריון, וכל מי שעבר "
                "הקרנה באזור הצוואר — כולם צריכים לעבור בדיקות תריס סדירות. גם במקרים תת-קליניים "
                "הרופא עשוי להמליץ על תוכנית מעקב.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת לכם להבין את תוצאות התריס",
            body_html=(
                "<p>ב-Norya אנחנו לא מאבחנים — אנחנו עוזרים לכם להבין את בדיקת הדם ולהגיע מוכנים "
                "יותר לרופא. אתם יכולים <a href=\"/analyze\">להעלות את הדו\"ח</a> ולקבל סיכום ברור "
                "ומסודר שמסביר את ערכי ה-T3, T4 ו-TSH שלכם בשפה פשוטה עם טווחי ייחוס. הסיכום הזה "
                "עוזר לכם להגיע לפגישה מוכנים יותר.</p>"
                "<p>מוכן תוך דקות ספורות, הדו\"ח מדגיש אילו ערכים בטווח ואילו חורגים ממנו, ועוזר "
                "לכם לארגן את השאלות לפני הביקור אצל הרופא. לאפשרויות ומחירים בקרו "
                "ב<a href=\"/pricing\">עמוד המחירים</a> שלנו.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# HINDI  — STUB
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="T3 और T4: थायरॉइड हॉर्मोन को समझें",
            body_html=(
                "<p>जब आप अपनी ब्लड टेस्ट रिपोर्ट में <strong>T3</strong> और <strong>T4</strong> "
                "के मान देखते हैं तो पहला सवाल अक्सर यही होता है: ये हॉर्मोन क्या करते हैं और क्या "
                "मेरे नतीजे सामान्य हैं? ट्राईआयोडोथायरोनिन (T3) और थायरॉक्सिन (T4) थायरॉइड ग्रंथि "
                "द्वारा बनाए जाने वाले प्रमुख हॉर्मोन हैं जो मेटाबॉलिज़्म, ऊर्जा उत्पादन, वृद्धि "
                "और विकास को नियंत्रित करते हैं। चूँकि ये शरीर की लगभग हर कोशिका को प्रभावित करते "
                "हैं, असामान्य स्तर थकान, वज़न बदलाव, हृदय गति में गड़बड़ी और बालों के झड़ने जैसे "
                "लक्षण पैदा कर सकते हैं।</p>"
                "<p>यह गाइड बताती है कि T3 और T4 क्या हैं, उनमें क्या अंतर है, रेफरेंस रेंज का क्या "
                "मतलब है और असामान्य नतीजों के संभावित कारण क्या हो सकते हैं। हमारा उद्देश्य निदान "
                "करना नहीं बल्कि आपको नतीजे समझने में मदद करना है ताकि डॉक्टर से बातचीत अधिक "
                "उपयोगी हो।</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="T3 और T4 क्या हैं?",
            body_html=(
                "<p><strong>T3 (ट्राईआयोडोथायरोनिन)</strong> और <strong>T4 (थायरॉक्सिन)</strong> गले "
                "में स्थित तितली के आकार की थायरॉइड ग्रंथि द्वारा बनाए जाने वाले हॉर्मोन हैं। T4 "
                "ग्रंथि का मुख्य उत्पाद है और रक्त में प्रवाहित थायरॉइड हॉर्मोन का लगभग 80% बनाता "
                "है। हालाँकि इसकी जैविक सक्रियता अपेक्षाकृत कम है; यह परिधीय ऊतकों — मुख्यतः लिवर "
                "और किडनी — में एक आयोडीन परमाणु हटाकर अधिक शक्तिशाली T3 में बदल जाता है। T3 वह "
                "प्रभावकारी हॉर्मोन है जो सीधे कोशिकीय मेटाबॉलिज़्म को तेज़ करता है।</p>"
                "<p>ये दोनों हॉर्मोन मिलकर प्रोटीन संश्लेषण, ऑक्सीजन खपत, हृदय की पंपिंग, आँतों "
                "की गतिशीलता और मस्तिष्क विकास को नियंत्रित करते हैं। बचपन में ये वृद्धि और तंत्रिका "
                "विकास के लिए अनिवार्य हैं, जबकि वयस्कों में बेसल मेटाबॉलिक रेट बनाए रखते हैं। "
                "बहुत अधिक या बहुत कम स्तर शरीर की लगभग हर प्रणाली को प्रभावित कर सकते हैं।</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="T3 बनाम T4: क्या अंतर है?",
            body_html=(
                "<p><strong>T4</strong> थायरॉइड का प्रमुख उत्पाद है और रक्त में अधिक सांद्रता में "
                "पाया जाता है। इसकी अर्ध-आयु लगभग 6–7 दिन है, जिससे रक्त स्तर स्थिर रहते हैं और "
                "यह एक विश्वसनीय लैब मार्कर बनता है। <strong>T3</strong> जैविक रूप से T4 से 3–5 गुना "
                "अधिक शक्तिशाली है लेकिन बहुत कम मात्रा में पाया जाता है; इसकी अर्ध-आयु केवल "
                "लगभग 1 दिन है। अधिकांश T3 परिधीय ऊतकों में T4 से रूपांतरण द्वारा बनता है।</p>"
                "<p>क्लिनिकल प्रैक्टिस में पहले <em>फ्री T4</em> और <em>TSH</em> मापे जाते हैं। T3 "
                "तब जोड़ा जाता है जब T4 सामान्य हो लेकिन TSH दबा हुआ हो, या जब हाइपरथायरॉइडिज़्म "
                "का नैदानिक संदेह हो — क्योंकि कुछ रोगियों में केवल T3 बढ़ा होता है "
                "(<em>T3 थायरोटॉक्सिकोसिस</em>)। दोनों हॉर्मोन का मिलाकर मूल्यांकन थायरॉइड "
                "फ़ंक्शन की सबसे पूरी तस्वीर देता है।</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="फ्री बनाम टोटल हॉर्मोन",
            body_html=(
                "<p>रक्त में T3 और T4 का बड़ा हिस्सा <strong>वाहक प्रोटीन</strong> — मुख्यतः "
                "TBG (थायरॉक्सिन-बाइंडिंग ग्लोब्युलिन) — से बँधा रहता है। बँधा हुआ अंश जैविक रूप "
                "से निष्क्रिय है; केवल <strong>फ्री (अनबाउंड)</strong> अंश ही कोशिकाओं में प्रवेश कर "
                "चयापचय प्रभाव डाल सकता है। टोटल T4 और टोटल T3 बाउंड और फ्री दोनों का योग मापते "
                "हैं, जबकि फ्री T4 (FT4) और फ्री T3 (FT3) केवल सक्रिय अनबाउंड भाग मापते हैं।</p>"
                "<p>गर्भावस्था, एस्ट्रोजन थेरेपी, लिवर रोग या TBG के आनुवंशिक वेरिएंट वाहक प्रोटीन "
                "स्तर बदल सकते हैं, जिससे टोटल मान प्रभावित होते हैं लेकिन फ्री हॉर्मोन सांद्रता "
                "ज़रूरी नहीं कि बदले। इसलिए आधुनिक थायरॉइड मूल्यांकन मुख्य रूप से <em>फ्री "
                "हॉर्मोन</em> माप पर निर्भर करता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="T3 और T4 रेफरेंस रेंज",
            body_html=(
                "<p>नीचे दी गई तालिका वयस्कों के लिए थायरॉइड हॉर्मोन की सामान्य रूप से स्वीकृत "
                "रेफरेंस रेंज दर्शाती है। लैब पद्धतियों में भिन्नता के कारण मामूली अंतर सामान्य "
                "है; हमेशा अपनी रिपोर्ट पर छपी रेफरेंस रेंज देखें।</p>"
                f'{_TBL}<thead><tr><th {_TH}>टेस्ट</th>'
                f'<th {_TH}>सामान्य रेंज</th></tr></thead><tbody>'
                f'<tr><td {_TD}>फ्री T4</td><td {_TD}>0.8 – 1.8 ng/dL</td></tr>'
                f'<tr><td {_TD}>फ्री T3</td><td {_TD}>2.3 – 4.2 pg/mL</td></tr>'
                f'<tr><td {_TD}>टोटल T4</td><td {_TD}>4.5 – 12.5 μg/dL</td></tr>'
                f'<tr><td {_TD}>टोटल T3</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0.4 – 4.0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>ये मान सामान्य वयस्क आबादी के लिए हैं। गर्भावस्था, उम्र, दवाइयाँ और पुरानी "
                "बीमारियाँ रेंज बदल सकती हैं। अपने नतीजों की व्याख्या हमेशा अपनी लैब की रेफरेंस "
                "रेंज और क्लिनिकल संदर्भ के साथ करें।</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="T3 और T4 बढ़ने के कारण (हाइपरथायरॉइडिज़्म)",
            body_html=(
                "<p>जब T3 और/या T4 का स्तर रेफरेंस रेंज से ऊपर हो तो इसे "
                "<strong>हाइपरथायरॉइडिज़्म</strong> कहते हैं। सबसे आम कारणों में शामिल हैं: "
                "<strong>ग्रेव्स रोग</strong> (ऑटोएंटीबॉडी थायरॉइड को अत्यधिक हॉर्मोन बनाने के लिए "
                "उत्तेजित करती हैं), <strong>टॉक्सिक नॉड्यूलर गॉइटर</strong> (स्वतंत्र रूप से काम "
                "करने वाले नॉड्यूल), <strong>थायरॉइडाइटिस</strong> (ग्रंथि की सूजन जो संग्रहीत "
                "हॉर्मोन रक्त में छोड़ती है) और <strong>अत्यधिक थायरॉइड दवा</strong>।</p>"
                "<p>हाइपरथायरॉइडिज़्म में मेटाबॉलिक रेट बढ़ जाता है जिससे धड़कन, वज़न कम होना, "
                "ज़्यादा पसीना, कंपन, बेचैनी और दस्त हो सकते हैं। कुछ रोगियों में केवल T3 बढ़ता "
                "है (<em>T3 थायरोटॉक्सिकोसिस</em>) जबकि T4 सामान्य रहता है। निदान में क्लिनिकल "
                "संकेतों और लैब निष्कर्षों दोनों की ज़रूरत होती है।</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="T3 और T4 घटने के कारण (हाइपोथायरॉइडिज़्म)",
            body_html=(
                "<p>जब T3 और/या T4 का स्तर रेफरेंस रेंज से नीचे आ जाए तो इसे "
                "<strong>हाइपोथायरॉइडिज़्म</strong> कहते हैं। विश्व स्तर पर सबसे आम कारण "
                "<strong>हाशिमोटो थायरॉइडाइटिस</strong> है — एक ऑटोइम्यून बीमारी जिसमें प्रतिरक्षा "
                "प्रणाली थायरॉइड ऊतक पर हमला करती है और हॉर्मोन उत्पादन धीरे-धीरे कम करती है। अन्य "
                "कारणों में <strong>आयोडीन की कमी</strong>, <strong>पिट्यूटरी ग्रंथि के विकार</strong> "
                "(सेकेंडरी हाइपोथायरॉइडिज़्म), सर्जरी या रेडियोआयोडीन के बाद की स्थिति और "
                "<strong>कुछ दवाइयाँ</strong> (लिथियम, एमियोडेरोन) शामिल हैं।</p>"
                "<p>हाइपोथायरॉइडिज़्म में मेटाबॉलिज़्म धीमा होता है जिससे थकान, वज़न बढ़ना, ठंड "
                "लगना, कब्ज़, रूखी त्वचा, बालों का झड़ना, चेहरे पर सूजन, उदास मनोदशा, याददाश्त "
                "की समस्या और ब्रैडीकार्डिया हो सकता है। निदान आमतौर पर बढ़े TSH और कम फ्री T4 पर "
                "आधारित होता है; उपचार में सिंथेटिक थायरॉक्सिन (लेवोथायरॉक्सिन) दिया जाता है।</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="TSH और T3-T4 के बीच का संबंध",
            body_html=(
                "<p><strong>TSH (थायरॉइड-स्टिमुलेटिंग हॉर्मोन)</strong> पिट्यूटरी ग्रंथि से स्रावित "
                "होता है और थायरॉइड को बताता है कि कितना T3 और T4 बनाना है। जब रक्त में थायरॉइड "
                "हॉर्मोन कम होता है तो पिट्यूटरी अधिक TSH छोड़ती है (<em>नेगेटिव फ़ीडबैक</em>); "
                "जब स्तर पर्याप्त होते हैं तो TSH दब जाता है। यह गतिशील संतुलन मेटाबॉलिक रेट को "
                "एक सँकरी रेंज में रखता है।</p>"
                "<p>क्लिनिकली TSH सबसे संवेदनशील स्क्रीनिंग टेस्ट है: शुरुआती हाइपोथायरॉइडिज़्म में "
                "T4 गिरने से पहले TSH बढ़ने लगता है (<em>सबक्लिनिकल हाइपोथायरॉइडिज़्म</em>); "
                "शुरुआती हाइपरथायरॉइडिज़्म में T4 स्पष्ट रूप से बढ़ने से पहले TSH दब जाता है। "
                "इसलिए डॉक्टर आमतौर पर पहले TSH देखते हैं और ज़रूरत पड़ने पर फ्री T4 और T3 जोड़ते "
                "हैं। TSH की सामान्य रेंज आम तौर पर <strong>0.4–4.0 mIU/L</strong> मानी जाती है, "
                "हालाँकि व्यक्तिगत लक्ष्य उम्र और क्लिनिकल स्थिति के अनुसार भिन्न हो सकते "
                "हैं।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="थायरॉइड हॉर्मोन असंतुलन के लक्षण",
            body_html=(
                "<p><strong>हाइपरथायरॉइड के लक्षण:</strong> धड़कन बढ़ना, अनजाने में वज़न कम होना, "
                "ज़्यादा पसीना, गर्मी सहन न होना, कंपन (विशेषकर हाथों में), बेचैनी, अनिद्रा, "
                "बार-बार मल त्याग या दस्त, मांसपेशियों में कमज़ोरी और महिलाओं में मासिक धर्म "
                "अनियमितता। ग्रेव्स रोग में आँखों की समस्या (एक्सोफ़्थैल्मोस) भी हो सकती है।</p>"
                "<p><strong>हाइपोथायरॉइड के लक्षण:</strong> थकान, वज़न बढ़ना, ठंड लगना, कब्ज़, रूखी "
                "त्वचा, बालों और भौंहों का पतला होना, सूजन (विशेषकर चेहरे पर), उदास मनोदशा, "
                "याददाश्त की कठिनाई और ब्रैडीकार्डिया। चूँकि लक्षण धीरे-धीरे विकसित होते हैं, "
                "मरीज़ को महीनों या सालों तक पता नहीं चलता।</p>"
                "<p>दोनों स्थितियों में लक्षण अविशिष्ट होते हैं और अकेले निदान की पुष्टि नहीं कर "
                "सकते। लैब टेस्ट और क्लिनिकल मूल्यांकन दोनों ज़रूरी हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर के पास कब जाएँ?",
            body_html=(
                "<p>यदि आपके T3, T4 या TSH में से कोई भी मान रेफरेंस रेंज से बाहर है तो डॉक्टर "
                "से मिलना उचित है। विशेष रूप से अगर अस्पष्ट वज़न परिवर्तन, लगातार थकान, धड़कन, "
                "कंपन, बालों का झड़ना, कब्ज़ या दस्त, मूड में बदलाव या गर्दन में दिखाई देने वाली "
                "सूजन दिखे तो तुरंत ध्यान दें।</p>"
                "<p>थायरॉइड विकारों का जल्दी पता लगने से उपचार के परिणाम बेहतर होते हैं। जिन लोगों "
                "के परिवार में थायरॉइड बीमारी का इतिहास है, ऑटोइम्यून रोग है, गर्भवती या गर्भ की "
                "योजना बना रही महिलाएँ, और जिन्होंने गर्दन क्षेत्र में रेडिएशन थेरेपी ली है — सभी "
                "को नियमित थायरॉइड जाँच करानी चाहिए। सबक्लिनिकल मामलों में भी डॉक्टर मॉनिटरिंग "
                "प्लान सुझा सकते हैं।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके थायरॉइड नतीजे समझने में कैसे मदद करता है",
            body_html=(
                "<p>Norya पर हम निदान नहीं करते — हम आपकी ब्लड टेस्ट रिपोर्ट समझने और डॉक्टर के "
                "पास तैयार होकर जाने में मदद करते हैं। आप <a href=\"/analyze\">अपनी रिपोर्ट "
                "अपलोड</a> कर सकते हैं और T3, T4 व TSH समेत सभी वैल्यू का सरल भाषा में, रेफरेंस "
                "रेंज सहित, साफ़ और संरचित सारांश प्राप्त कर सकते हैं। यह सारांश आपको अपॉइंटमेंट "
                "में बेहतर तैयार होकर जाने में मदद करता है।</p>"
                "<p>कुछ ही मिनटों में तैयार, यह रिपोर्ट दिखाती है कि कौन-से मान सामान्य हैं और "
                "कौन-से बाहर हैं, जिससे डॉक्टर से मिलने से पहले अपने सवाल व्यवस्थित कर सकें। "
                "विकल्पों और कीमत के लिए <a href=\"/pricing\">प्राइसिंग पेज</a> देखें।</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC  — STUB
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="T3 وT4: فهم هرمونات الغدة الدرقية",
            body_html=(
                "<p>عندما ترى قيم <strong>T3</strong> و<strong>T4</strong> في تقرير تحليل الدم، يكون "
                "السؤال الأول عادةً: ما وظيفة هذه الهرمونات وهل نتائجي طبيعية؟ ثلاثي يود الثيرونين "
                "(T3) والثيروكسين (T4) هما الهرمونان الرئيسيان اللذان تنتجهما الغدة الدرقية، ويلعبان "
                "دوراً محورياً في تنظيم الأيض وإنتاج الطاقة والنمو والتطور. ولأنهما يؤثران فعلياً على "
                "كل خلية في الجسم، فإن مستوياتهما غير الطبيعية قد تظهر بأعراض تتراوح بين الإرهاق "
                "وتغيرات الوزن واضطرابات نظم القلب وتساقط الشعر.</p>"
                "<p>يشرح هذا الدليل ماهية T3 وT4، والفرق بينهما، ومعنى النطاقات المرجعية، والأسباب "
                "المحتملة للنتائج غير الطبيعية. هدفنا ليس التشخيص بل مساعدتك على فهم نتائجك لتكون "
                "المحادثة مع طبيبك أكثر إنتاجية.</p>"
            ),
        ),
        Section(
            id="what-are-t3-t4", level=2,
            heading="ما هما T3 وT4؟",
            body_html=(
                "<p><strong>T3 (ثلاثي يود الثيرونين)</strong> و<strong>T4 (الثيروكسين)</strong> "
                "هرمونات تنتجها الغدة الدرقية ذات الشكل الفراشي في الرقبة. T4 هو المنتج الإفرازي "
                "الرئيسي ويشكل نحو 80% من هرمون الغدة الدرقية في الدم. غير أن نشاطه البيولوجي منخفض "
                "نسبياً؛ إذ يتحول في الأنسجة الطرفية — لا سيما الكبد والكلى — إلى T3 الأكثر فعالية "
                "بإزالة إنزيمية لذرة يود واحدة. T3 هو الهرمون المؤثر الذي يُسرّع الأيض الخلوي "
                "مباشرة.</p>"
                "<p>يعمل هذان الهرمونان معاً على تنظيم تخليق البروتين واستهلاك الأكسجين والنتاج "
                "القلبي وحركية الأمعاء ونمو الدماغ. في مرحلة الطفولة يكونان حيويين للنمو والنضج "
                "العصبي، بينما يحافظان عند البالغين على معدل الأيض الأساسي. المستويات المرتفعة أو "
                "المنخفضة جداً يمكن أن تؤثر على كل جهاز عضوي تقريباً.</p>"
            ),
        ),
        Section(
            id="t3-vs-t4", level=2,
            heading="الفرق بين T3 وT4",
            body_html=(
                "<p><strong>T4</strong> هو المنتج الرئيسي للغدة الدرقية ويدور بتركيزات أعلى في الدم. "
                "عمر النصف له حوالي 6–7 أيام مما يجعل مستوياته مستقرة على مدار اليوم وعلامة مخبرية "
                "موثوقة. <strong>T3</strong> أقوى بيولوجياً بـ3–5 مرات لكنه يدور بكميات أقل بكثير؛ "
                "عمر النصف له نحو يوم واحد فقط. معظم T3 في الدم يُنتج بتحويل T4 في الأنسجة الطرفية "
                "وليس بإفراز مباشر من الغدة.</p>"
                "<p>في الممارسة السريرية يُقاس عادةً <em>T4 الحر</em> و<em>TSH</em> أولاً. يُضاف T3 "
                "عندما يكون T4 طبيعياً لكن TSH مكبوتاً، أو عند الاشتباه سريرياً بفرط نشاط الغدة — "
                "لأن بعض المرضى يظهرون ارتفاعاً معزولاً في T3 (<em>انسمام درقي بـT3</em>). تقييم "
                "الهرمونين معاً يوفر الصورة الأكمل لوظيفة الغدة الدرقية.</p>"
            ),
        ),
        Section(
            id="free-vs-total", level=2,
            heading="الهرمون الحر مقابل الكلي",
            body_html=(
                "<p>الجزء الأكبر من T3 وT4 في الدم مرتبط بـ<strong>بروتينات نقل</strong> — أساساً "
                "TBG (الغلوبيولين الرابط للثيروكسين). الجزء المرتبط غير نشط بيولوجياً؛ فقط "
                "<strong>الجزء الحر (غير المرتبط)</strong> يمكنه دخول الخلايا وإحداث تأثيرات أيضية. "
                "T4 الكلي وT3 الكلي يقيسان مجموع الأشكال المرتبطة والحرة، بينما T4 الحر (FT4) وT3 "
                "الحر (FT3) يقيسان الجزء النشط غير المرتبط فقط.</p>"
                "<p>الحمل والعلاج بالإستروجين وأمراض الكبد والمتغيرات الوراثية لـTBG قد تغيّر مستويات "
                "بروتينات النقل، فتؤثر على القيم الكلية دون أن تغيّر بالضرورة تركيز الهرمون الحر. "
                "لذلك يعتمد التقييم الحديث للغدة الدرقية بشكل رئيسي على قياس <em>الهرمون "
                "الحر</em>.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="النطاقات المرجعية لـT3 وT4",
            body_html=(
                "<p>يعرض الجدول أدناه النطاقات المرجعية المقبولة عموماً لهرمونات الغدة الدرقية عند "
                "البالغين. نظراً لاختلاف المنهجيات بين المختبرات، فإن فروقاً طفيفة طبيعية؛ ارجع "
                "دائماً إلى النطاق المطبوع على تقريرك.</p>"
                f'{_TBL}<thead><tr><th {_TH}>الفحص</th>'
                f'<th {_TH}>النطاق الطبيعي</th></tr></thead><tbody>'
                f'<tr><td {_TD}>T4 الحر</td><td {_TD}>0.8 – 1.8 ng/dL</td></tr>'
                f'<tr><td {_TD}>T3 الحر</td><td {_TD}>2.3 – 4.2 pg/mL</td></tr>'
                f'<tr><td {_TD}>T4 الكلي</td><td {_TD}>4.5 – 12.5 μg/dL</td></tr>'
                f'<tr><td {_TD}>T3 الكلي</td><td {_TD}>80 – 200 ng/dL</td></tr>'
                f'<tr><td {_TD}>TSH</td><td {_TD}>0.4 – 4.0 mIU/L</td></tr>'
                "</tbody></table>"
                "<p>هذه القيم للسكان البالغين عموماً. الحمل والعمر والأدوية والأمراض المزمنة قد "
                "تغيّر النطاقات. فسّر نتائجك دائماً بالتوازي مع النطاق المرجعي لمختبرك وسياقك "
                "السريري.</p>"
            ),
        ),
        Section(
            id="high-thyroid-causes", level=2,
            heading="أسباب ارتفاع T3 وT4 (فرط نشاط الغدة الدرقية)",
            body_html=(
                "<p>عندما تتجاوز مستويات T3 و/أو T4 النطاق المرجعي، يُسمى ذلك "
                "<strong>فرط نشاط الغدة الدرقية</strong>. أكثر الأسباب شيوعاً: <strong>داء "
                "غريفز</strong> (أجسام مضادة ذاتية تحفز الغدة على الإنتاج المفرط)، "
                "<strong>الدراق العقدي السام</strong> (عقيدات درقية مستقلة الوظيفة)، <strong>التهاب "
                "الغدة الدرقية</strong> (التهاب يطلق الهرمون المخزّن إلى الدم) و<strong>جرعة زائدة "
                "من أدوية الغدة</strong>.</p>"
                "<p>في فرط النشاط يزداد معدل الأيض وقد تظهر خفقان وفقدان وزن وتعرق مفرط ورجفة "
                "وتوتر وإسهال. لدى بعض المرضى يرتفع T3 فقط (<em>انسمام درقي بـT3</em>) بينما يبقى "
                "T4 طبيعياً. يتطلب التشخيص دمج العلامات السريرية مع نتائج المختبر.</p>"
            ),
        ),
        Section(
            id="low-thyroid-causes", level=2,
            heading="أسباب انخفاض T3 وT4 (قصور الغدة الدرقية)",
            body_html=(
                "<p>عندما تنخفض مستويات T3 و/أو T4 عن النطاق المرجعي، يُسمى ذلك <strong>قصور الغدة "
                "الدرقية</strong>. السبب الأكثر شيوعاً عالمياً هو <strong>التهاب هاشيموتو</strong>، "
                "مرض مناعي ذاتي يهاجم فيه الجهاز المناعي نسيج الغدة ويقلل تدريجياً إنتاج الهرمون. "
                "تشمل الأسباب الأخرى <strong>نقص اليود</strong>، <strong>أمراض الغدة "
                "النخامية</strong> (قصور ثانوي)، حالة ما بعد الجراحة أو اليود المشع، "
                "و<strong>بعض الأدوية</strong> مثل الليثيوم والأميودارون.</p>"
                "<p>في قصور الغدة يبطؤ الأيض فتظهر إرهاق وزيادة وزن وعدم تحمل البرد وإمساك وجفاف "
                "جلد وتساقط شعر وانتفاخ وجه ومزاج مكتئب وصعوبات في الذاكرة وبطء في القلب. يعتمد "
                "التشخيص عادةً على TSH مرتفع مع T4 حر منخفض؛ ويكون العلاج ببديل الثيروكسين "
                "الصناعي (ليفوثيروكسين).</p>"
            ),
        ),
        Section(
            id="tsh-connection", level=2,
            heading="العلاقة بين TSH وT3 وT4",
            body_html=(
                "<p><strong>TSH (الهرمون المحفز للغدة الدرقية)</strong> يُفرز من الغدة النخامية "
                "ويخبر الغدة الدرقية بكمية T3 وT4 التي يجب إنتاجها. عندما تنخفض مستويات هرمون "
                "الغدة في الدم، تُطلق النخامية مزيداً من TSH لتحفيز الغدة (<em>التغذية الراجعة "
                "السلبية</em>)؛ وعندما تكون المستويات كافية يُثبَّط TSH. هذا التوازن الديناميكي يبقي "
                "معدل الأيض ضمن نطاق ضيق.</p>"
                "<p>سريرياً TSH هو اختبار الفحص الأكثر حساسية: في القصور المبكر يبدأ TSH بالارتفاع "
                "قبل أن ينخفض T4 (<em>قصور تحت سريري</em>)؛ وفي فرط النشاط المبكر يُثبّط TSH قبل "
                "أن يرتفع T4 بوضوح. لذا يفحص الأطباء عادةً TSH أولاً ثم يضيفون T4 وT3 الحرين عند "
                "الحاجة. النطاق الطبيعي المقبول لـTSH هو عموماً <strong>0.4–4.0 mIU/L</strong>، "
                "وإن كانت الأهداف الفردية قد تختلف حسب العمر والسياق السريري.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض اختلال هرمونات الغدة الدرقية",
            body_html=(
                "<p><strong>أعراض فرط النشاط:</strong> خفقان، فقدان وزن غير مقصود، تعرق مفرط، "
                "عدم تحمل الحرارة، رجفة (خصوصاً في اليدين)، قلق، أرق، إسهال أو تكرر حركة الأمعاء، "
                "ضعف عضلي واضطرابات في الدورة الشهرية لدى النساء. في داء غريفز قد تظهر مشكلات "
                "بالعين (جحوظ).</p>"
                "<p><strong>أعراض القصور:</strong> إرهاق، زيادة وزن، عدم تحمل البرد، إمساك، جفاف "
                "جلد، ترقق الشعر والحاجبين، انتفاخ (خصوصاً في الوجه)، مزاج مكتئب، مشكلات ذاكرة "
                "وبطء قلب. لأن الأعراض تتطور تدريجياً، قد لا يلاحظها المريض لأشهر أو حتى سنوات.</p>"
                "<p>في الحالتين الأعراض غير نوعية ولا تكفي وحدها لتأكيد التشخيص. يجب الأخذ "
                "بالاعتبار الفحوص المخبرية والتقييم السريري معاً.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كان أي من قيم T3 أو T4 أو TSH لديك خارج النطاق المرجعي، يُنصح بمراجعة "
                "الطبيب. اطلب الرعاية خصوصاً إذا لاحظت تغيرات وزن غير مفسرة، إرهاقاً مستمراً، "
                "خفقاناً، رجفة، تساقط شعر، إمساكاً أو إسهالاً، اضطرابات مزاجية أو تورماً مرئياً "
                "في الرقبة.</p>"
                "<p>الكشف المبكر عن اضطرابات الغدة الدرقية يحسّن نتائج العلاج. الأشخاص ذوو التاريخ "
                "العائلي لأمراض الغدة، ومن يعانون أمراضاً مناعية ذاتية، والنساء الحوامل أو "
                "المخططات للحمل، وأي شخص تلقى علاجاً إشعاعياً في منطقة الرقبة — يجب أن يخضعوا "
                "لفحوص درقية منتظمة. حتى في الحالات تحت السريرية قد يوصي الطبيب بخطة متابعة.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم نتائج الغدة الدرقية",
            body_html=(
                "<p>في Norya لا نشخّص — بل نسهّل عليك فهم تحليل الدم والتحضير لزيارة الطبيب. يمكنك "
                "<a href=\"/analyze\">رفع تقريرك</a> والحصول على ملخص واضح ومنظم يشرح قيم T3 وT4 "
                "وTSH بلغة بسيطة مع النطاقات المرجعية. هذا الملخص يساعدك على الذهاب إلى موعدك أكثر "
                "استعداداً.</p>"
                "<p>يكون التقرير جاهزاً في دقائق ويبرز القيم الطبيعية وتلك الخارجة عن النطاق، "
                "مما يساعدك على ترتيب أسئلتك قبل زيارة الطبيب. للخيارات والأسعار تفضل بزيارة "
                "<a href=\"/pricing\">صفحة الأسعار</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_t3_t4_sections_by_lang():
    """Returns sections_by_lang dict for T3 & T4 article (all 9 languages)."""
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


def get_t3_t4_faq_schema_qa():
    """Returns faq_schema_qa dict for T3 & T4 article (all 9 languages)."""
    return {
        "tr": [
            {"question": "T3 ve T4 hormonları ne işe yarar?",
             "answer": "T3 (triiyodotironin) ve T4 (tiroksin), tiroid bezinin ürettiği ve metabolizmayı, enerji dengesini, büyüme ve gelişmeyi düzenleyen temel hormonlardır. T4, dokularda daha aktif olan T3'e dönüştürülür."},
            {"question": "Serbest T4 normal aralığı nedir?",
             "answer": "Yetişkinlerde serbest T4 için yaygın kabul edilen referans aralığı 0,8–1,8 ng/dL'dir; ancak laboratuvarlar arasında küçük farklılıklar olabilir."},
            {"question": "T3 ve T4 yüksekliğinin nedenleri nelerdir?",
             "answer": "En sık nedenler Graves hastalığı, toksik nodüler guatr, tiroidit ve aşırı tiroid ilacı kullanımıdır."},
            {"question": "Serbest T4 ile total T4 arasındaki fark nedir?",
             "answer": "Serbest T4 yalnızca bağlanmamış, biyolojik olarak aktif hormonu ölçerken, total T4 hem bağlı hem serbest fraksiyonların toplamını ölçer."},
        ],
        "en": [
            {"question": "What do T3 and T4 hormones do?",
             "answer": "T3 (triiodothyronine) and T4 (thyroxine) are thyroid hormones that regulate metabolism, energy production, growth, and development. T4 is converted into the more active T3 in peripheral tissues."},
            {"question": "What is the normal range for Free T4?",
             "answer": "The commonly accepted reference range for Free T4 in adults is 0.8–1.8 ng/dL, though slight variations exist between laboratories."},
            {"question": "What causes high T3 and T4 levels?",
             "answer": "Common causes of elevated thyroid hormones include Graves' disease, toxic nodular goiter, thyroiditis, and excess thyroid medication."},
            {"question": "What is the difference between Free T4 and Total T4?",
             "answer": "Free T4 measures only the unbound, biologically active hormone, while Total T4 includes both the protein-bound and free fractions."},
            {"question": "How are TSH, T3, and T4 related?",
             "answer": "TSH from the pituitary gland controls thyroid hormone production via a negative feedback loop. When T3/T4 levels drop, TSH rises to stimulate the thyroid; when they rise, TSH falls."},
        ],
        "es": [
            {"question": "¿Para qué sirven las hormonas T3 y T4?",
             "answer": "La T3 (triyodotironina) y la T4 (tiroxina) son hormonas tiroideas que regulan el metabolismo, la producción de energía, el crecimiento y el desarrollo. La T4 se convierte en la más activa T3 en los tejidos periféricos."},
            {"question": "¿Cuál es el rango normal de T4 libre?",
             "answer": "El rango de referencia comúnmente aceptado para la T4 libre en adultos es 0,8–1,8 ng/dL, aunque puede variar ligeramente entre laboratorios."},
            {"question": "¿Qué causa T3 y T4 altas?",
             "answer": "Las causas más frecuentes son la enfermedad de Graves, el bocio multinodular tóxico, la tiroiditis y el exceso de medicación tiroidea."},
            {"question": "¿Cuál es la diferencia entre T4 libre y T4 total?",
             "answer": "La T4 libre mide solo la hormona no unida y biológicamente activa; la T4 total incluye tanto la fracción unida a proteínas como la libre."},
        ],
        "de": [
            {"question": "Wofür sind die Hormone T3 und T4 zuständig?",
             "answer": "T3 (Trijodthyronin) und T4 (Thyroxin) sind Schilddrüsenhormone, die Stoffwechsel, Energieproduktion, Wachstum und Entwicklung regulieren. T4 wird in den Geweben in das aktivere T3 umgewandelt."},
            {"question": "Was ist der Normalbereich für freies T4?",
             "answer": "Der allgemein akzeptierte Referenzbereich für freies T4 bei Erwachsenen liegt bei 0,8–1,8 ng/dL; zwischen Laboren kann es geringe Abweichungen geben."},
            {"question": "Was verursacht erhöhte T3- und T4-Werte?",
             "answer": "Häufige Ursachen sind Morbus Basedow, toxische Knotenstruma, Thyreoiditis und eine übermäßige Schilddrüsenmedikation."},
            {"question": "Was ist der Unterschied zwischen freiem T4 und Gesamt-T4?",
             "answer": "Freies T4 misst nur das ungebundene, biologisch aktive Hormon; Gesamt-T4 umfasst sowohl die proteingebundene als auch die freie Fraktion."},
        ],
        "fr": [
            {"question": "À quoi servent les hormones T3 et T4 ?",
             "answer": "La T3 (triiodothyronine) et la T4 (thyroxine) sont des hormones thyroïdiennes qui régulent le métabolisme, la production d'énergie, la croissance et le développement. La T4 est convertie en T3, plus active, dans les tissus périphériques."},
            {"question": "Quelle est la fourchette normale de T4 libre ?",
             "answer": "La fourchette de référence couramment acceptée pour la T4 libre chez l'adulte est de 0,8 à 1,8 ng/dL, avec de légères variations selon les laboratoires."},
            {"question": "Quelles sont les causes de T3 et T4 élevées ?",
             "answer": "Les causes les plus fréquentes sont la maladie de Basedow, le goitre multinodulaire toxique, la thyroïdite et un excès de médicament thyroïdien."},
            {"question": "Quelle est la différence entre T4 libre et T4 totale ?",
             "answer": "La T4 libre mesure uniquement l'hormone non liée et biologiquement active ; la T4 totale comprend les fractions liées aux protéines et libres."},
        ],
        "it": [
            {"question": "A cosa servono gli ormoni T3 e T4?",
             "answer": "T3 (triiodotironina) e T4 (tiroxina) sono ormoni tiroidei che regolano metabolismo, produzione di energia, crescita e sviluppo. La T4 viene convertita nella più attiva T3 nei tessuti periferici."},
            {"question": "Qual è l'intervallo normale della T4 libera?",
             "answer": "L'intervallo di riferimento comunemente accettato per la T4 libera negli adulti è 0,8–1,8 ng/dL, con lievi variazioni tra i laboratori."},
            {"question": "Quali sono le cause di T3 e T4 alte?",
             "answer": "Le cause più comuni sono il morbo di Graves (Basedow), il gozzo multinodulare tossico, la tiroidite e un eccesso di farmaco tiroideo."},
            {"question": "Qual è la differenza tra T4 libera e T4 totale?",
             "answer": "La T4 libera misura solo l'ormone non legato e biologicamente attivo; la T4 totale include sia la frazione legata alle proteine sia quella libera."},
        ],
        "he": [
            {"question": "מה תפקידם של הורמוני T3 ו-T4?",
             "answer": "T3 (טריודותירונין) ו-T4 (תירוקסין) הם הורמוני בלוטת התריס האחראים על חילוף חומרים, ייצור אנרגיה, צמיחה והתפתחות. T4 מומר ברקמות ל-T3 הפעיל יותר."},
            {"question": "מהו הטווח התקין של T4 חופשי?",
             "answer": "טווח הייחוס המקובל ל-T4 חופשי במבוגרים הוא 0.8–1.8 ng/dL, עם סטיות קלות בין מעבדות."},
            {"question": "מה גורם ל-T3 ו-T4 גבוהים?",
             "answer": "הגורמים הנפוצים הם מחלת גרייבס, זפק רב-גושי רעיל, דלקת בלוטת התריס ומינון יתר של תרופות לבלוטת התריס."},
            {"question": "מה ההבדל בין T4 חופשי ל-T4 כולל?",
             "answer": "T4 חופשי מודד רק את ההורמון הלא-קשור והפעיל ביולוגית; T4 כולל כולל גם את החלק הקשור לחלבון וגם את החופשי."},
        ],
        "hi": [
            {"question": "T3 और T4 हॉर्मोन क्या करते हैं?",
             "answer": "T3 (ट्राईआयोडोथायरोनिन) और T4 (थायरॉक्सिन) थायरॉइड ग्रंथि के हॉर्मोन हैं जो मेटाबॉलिज़्म, ऊर्जा उत्पादन, विकास को नियंत्रित करते हैं। T4 ऊतकों में अधिक सक्रिय T3 में बदलता है।"},
            {"question": "फ्री T4 का सामान्य रेंज क्या है?",
             "answer": "वयस्कों में फ्री T4 का सामान्य रेफरेंस रेंज 0.8–1.8 ng/dL है, हालांकि लैब के अनुसार मामूली अंतर हो सकता है।"},
            {"question": "T3 और T4 बढ़ने के क्या कारण हैं?",
             "answer": "आम कारणों में ग्रेव्स रोग, टॉक्सिक नॉड्यूलर गॉइटर, थायरॉइडाइटिस और अत्यधिक थायरॉइड दवा शामिल हैं।"},
            {"question": "फ्री T4 और टोटल T4 में क्या अंतर है?",
             "answer": "फ्री T4 केवल अनबाउंड, जैविक रूप से सक्रिय हॉर्मोन मापता है; टोटल T4 में प्रोटीन-बाउंड और फ्री दोनों फ्रैक्शन शामिल हैं।"},
        ],
        "ar": [
            {"question": "ما وظيفة هرموني T3 وT4؟",
             "answer": "T3 (ثلاثي يود الثيرونين) وT4 (الثيروكسين) هرمونات الغدة الدرقية المسؤولة عن تنظيم الأيض وإنتاج الطاقة والنمو. يتحول T4 في الأنسجة إلى T3 الأكثر نشاطاً."},
            {"question": "ما النطاق الطبيعي لـ T4 الحر؟",
             "answer": "النطاق المرجعي المقبول عموماً لـ T4 الحر عند البالغين هو 0.8–1.8 ng/dL، مع اختلافات طفيفة بين المختبرات."},
            {"question": "ما أسباب ارتفاع T3 وT4؟",
             "answer": "الأسباب الشائعة تشمل داء غريفز، الدراق العقدي السام، التهاب الغدة الدرقية، والجرعة الزائدة من أدوية الغدة الدرقية."},
            {"question": "ما الفرق بين T4 الحر وT4 الكلي؟",
             "answer": "T4 الحر يقيس الهرمون غير المرتبط والنشط بيولوجياً فقط؛ بينما T4 الكلي يشمل الجزء المرتبط بالبروتين والجزء الحر معاً."},
        ],
    }
