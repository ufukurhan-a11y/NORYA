# -*- coding: utf-8 -*-
"""
Triglycerides blog article — full body content for all 9 languages.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ─────────────────────────────────────────────────────────────────────
# TURKISH
# ─────────────────────────────────────────────────────────────────────
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Trigliserid nedir ve neden önemlidir?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızda <strong>trigliserid</strong> değerinin yüksek "
                "çıktığını gördüğünüzde doğal olarak merak edersiniz: Bu nedir, endişelenmeli "
                "miyim? Trigliseridler, kanınızda dolaşan en yaygın yağ türüdür ve vücudunuzun "
                "enerji deposu olarak kullanır. Ancak bu değer belirli eşiklerin üzerine "
                "çıktığında kalp-damar sağlığınız açısından önemli bir risk belirteci haline gelir.</p>"
                "<p>Bu rehber, trigliseridlerin ne olduğunu, normal ve yüksek değerlerin ne "
                "anlama geldiğini, kolesterol ile farkını ve sonuçlarınızı nasıl değerlendirmeniz "
                "gerektiğini sade bir dille anlatıyor. Amacımız teşhis koymak değil — sizi "
                "doktor randevunuza daha bilinçli bir şekilde hazırlamaktır.</p>"
                "<p>Trigliserid düzeyiniz yaşam tarzı, beslenme alışkanlıkları ve genetik "
                "yatkınlığınız gibi pek çok faktörden etkilenir. Bu nedenle sonuçlarınızı "
                "tek başına değil, genel sağlık tablonuz içinde değerlendirmek büyük önem taşır.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Trigliseridler nedir?",
            body_html=(
                "<p><strong>Trigliseridler</strong>, yediğiniz yiyeceklerdeki yağlardan ve "
                "vücudunuzun karbonhidrat ve şekerlerden ürettiği yağ moleküllerinden oluşur. "
                "Kimyasal olarak bir gliserol molekülüne bağlı üç yağ asidinden meydana gelir. "
                "Yemek yedikten sonra vücudunuzun hemen kullanmadığı kaloriler trigliseride "
                "dönüştürülür ve yağ hücrelerinde depolanır.</p>"
                "<p>Öğünler arasında hormonlar bu depolanmış trigliseridleri serbest bırakarak "
                "enerji ihtiyacınızı karşılar. Bu, sağlıklı bir süreçtir. Ancak düzenli olarak "
                "ihtiyacınızdan fazla kalori alırsanız — özellikle rafine karbonhidrat ve "
                "şekerden — kandaki trigliserid düzeyiniz kronik olarak yüksek kalabilir.</p>"
                "<p>Trigliseridler, lipid panelinin önemli bir bileşenidir ve genellikle "
                "<strong>total kolesterol</strong>, <strong>LDL</strong> ve <strong>HDL</strong> "
                "kolesterol ile birlikte ölçülür. Doğru sonuç alabilmek için kan örneğinin "
                "genellikle 9–12 saatlik bir açlık sonrası alınması gerekir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Trigliserid referans aralıkları",
            body_html=(
                "<p>Trigliserid düzeyleri genellikle <strong>mg/dL</strong> biriminde raporlanır. "
                "Aşağıdaki tablo, yetişkinler için genel kabul görmüş sınıflandırmayı gösterir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Kategori</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Değer (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Sınırda yüksek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Yüksek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Çok yüksek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>Bu sınıflandırma Amerikan Kalp Derneği (AHA) ve ATP III kılavuzlarına "
                "dayanır. Ancak laboratuvarınız farklı referans aralıkları kullanıyor olabilir; "
                "sonuçlarınızı her zaman raporunuzdaki referans değerlerle karşılaştırın.</p>"
                "<p>Özellikle 500 mg/dL üzerindeki değerler <strong>akut pankreatit</strong> riski "
                "açısından dikkat gerektirir ve acil tıbbi değerlendirme gerektirebilir.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Trigliserid yüksekliğinin nedenleri",
            body_html=(
                "<p>Trigliserid düzeyinin normalin üzerine çıkmasının birçok nedeni olabilir. "
                "Bunlar genellikle yaşam tarzı, beslenme ve altta yatan sağlık durumları "
                "olarak gruplandırılır:</p>"
                "<ul>"
                "<li><strong>Rafine karbonhidrat ve şeker ağırlıklı beslenme</strong> — beyaz "
                "ekmek, şekerli içecekler, tatlılar ve işlenmiş gıdalar trigliserid "
                "üretimini artırır.</li>"
                "<li><strong>Obezite ve fazla kilo</strong> — özellikle abdominal yağlanma "
                "trigliserid yüksekliğiyle güçlü biçimde ilişkilidir.</li>"
                "<li><strong>Hareketsiz yaşam tarzı</strong> — düzenli fiziksel aktivite "
                "eksikliği yağ metabolizmasını yavaşlatır.</li>"
                "<li><strong>Aşırı alkol tüketimi</strong> — alkol, karaciğerde trigliserid "
                "sentezini doğrudan uyarır.</li>"
                "<li><strong>Tip 2 diyabet ve insülin direnci</strong> — kontrolsüz kan şekeri "
                "trigliserid düzeyini yükseltir.</li>"
                "<li><strong>Hipotiroidizm</strong> — tiroid bezinin az çalışması lipid "
                "metabolizmasını bozar.</li>"
                "<li><strong>Genetik faktörler</strong> — ailevi hipertrigliseridemi gibi "
                "kalıtsal durumlar trigliseridleri yükseltebilir.</li>"
                "</ul>"
                "<p>Bazı ilaçlar da (beta-blokerler, diüretikler, kortikosteroidler, bazı "
                "doğum kontrol hapları) trigliserid düzeyini artırabilir. Bu nedenle "
                "sonuçlarınızı değerlendirirken kullandığınız ilaçları hekiminize "
                "bildirmeniz önemlidir.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Trigliserid ile kolesterol arasındaki fark",
            body_html=(
                "<p><strong>Trigliseridler</strong> ve <strong>kolesterol</strong> her ikisi de "
                "lipid (yağ) grubuna ait olmalarına rağmen farklı işlevlere sahiptir. "
                "Trigliseridler, vücudun enerji depolaması için kullandığı yağlardır; "
                "kolesterol ise hücre zarlarının yapısında, hormon üretiminde ve D vitamini "
                "sentezinde görev alır.</p>"
                "<p>Lipid panelinde her ikisi birlikte ölçülür. <strong>LDL kolesterol</strong> "
                "(\"kötü\" kolesterol) ve <strong>HDL kolesterol</strong> (\"iyi\" kolesterol) "
                "arterlerinize etkileri açısından değerlendirilir; trigliseridler ise ayrı bir "
                "kardiyovasküler risk parametresi olarak ele alınır. Yüksek trigliserid ile "
                "düşük HDL birlikteliği <em>metabolik sendrom</em> açısından özellikle "
                "uyarıcıdır.</p>"
                "<p>Kolesterol hakkında daha ayrıntılı bilgi almak isterseniz "
                "<a href=\"/tr/blog\">kolesterol rehberimizi</a> inceleyebilirsiniz. "
                "Trigliserid ve kolesterolün birlikte değerlendirilmesi, kardiyovasküler "
                "risk profilinizin daha doğru belirlenmesini sağlar.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Kardiyovasküler risk ve trigliseridler",
            body_html=(
                "<p>Yüksek trigliserid düzeyleri, <strong>ateroskleroz</strong> (damar "
                "sertliği) sürecine katkıda bulunarak kalp krizi ve inme riskini artırabilir. "
                "Araştırmalar, yüksek trigliseridin özellikle düşük HDL kolesterol ve yüksek "
                "LDL kolesterol ile birlikte bulunduğunda kardiyovasküler olay riskini "
                "belirgin şekilde yükselttiğini göstermektedir.</p>"
                "<p>Trigliseridler, <strong>VLDL</strong> (çok düşük yoğunluklu lipoprotein) "
                "partikülleri içinde taşınır. Bu partiküller damar duvarında birikerek "
                "inflamatuar süreci tetikleyebilir. Ayrıca yüksek trigliserid düzeyleri, "
                "küçük ve yoğun LDL partiküllerinin oluşumunu teşvik eder; bu tür LDL "
                "partikülleri daha aterojenik kabul edilir.</p>"
                "<p>Metabolik sendrom bileşenleriyle (abdominal obezite, yüksek tansiyon, "
                "yüksek açlık kan şekeri, düşük HDL) birlikte yüksek trigliserid, "
                "kardiyovasküler riskin bütüncül değerlendirilmesinde önemli bir göstergedir. "
                "Hekiminiz bu parametreleri bir arada yorumlayarak size özel bir risk "
                "değerlendirmesi yapacaktır.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Yaşam tarzı ve beslenme önerileri",
            body_html=(
                "<p>Trigliserid düzeyini düşürmede yaşam tarzı değişiklikleri birincil "
                "tedavi yaklaşımıdır. İşte kanıta dayalı başlıca stratejiler:</p>"
                "<ul>"
                "<li><strong>Şeker ve rafine karbonhidrat alımını azaltın</strong> — beyaz "
                "ekmek, pasta, şekerli içecekler yerine tam tahılları tercih edin.</li>"
                "<li><strong>Omega-3 yağ asitleri tüketin</strong> — somon, sardalya, "
                "uskumru gibi yağlı balıklar trigliserid düşürücü etki gösterir.</li>"
                "<li><strong>Düzenli egzersiz yapın</strong> — haftada en az 150 dakika "
                "orta yoğunlukta aerobik aktivite trigliseridleri anlamlı ölçüde düşürür.</li>"
                "<li><strong>Kilo kontrolü sağlayın</strong> — %5–10 kilo kaybı bile "
                "trigliserid düzeyinde belirgin iyileşme sağlayabilir.</li>"
                "<li><strong>Alkol tüketimini sınırlandırın</strong> — alkol, karaciğerde "
                "trigliserid sentezini doğrudan uyardığından azaltılması veya bırakılması "
                "etkili olabilir.</li>"
                "</ul>"
                "<p>Bu değişikliklerin etkisi genellikle birkaç hafta ile birkaç ay arasında "
                "görülür. Hekiminiz, mevcut sağlık durumunuza göre size en uygun beslenme "
                "planını önerecektir. Diyetisyen desteği almak özellikle yüksek trigliserid "
                "düzeylerinde faydalı olabilir.</p>"
                "<p>Akdeniz diyeti, trigliserid yönetiminde en çok araştırılmış beslenme "
                "modellerinden biridir. Zeytinyağı, sebze, meyve, baklagiller ve tam tahıllar "
                "ağırlıklı bu beslenme tarzı, lipid profilini olumlu yönde etkileyebilir.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="İlaç tedavisi seçenekleri",
            body_html=(
                "<p>Yaşam tarzı değişikliklerinin yeterli olmadığı durumlarda hekiminiz "
                "ilaç tedavisi önerebilir. Trigliserid düşürmede kullanılan başlıca "
                "ilaç grupları şunlardır:</p>"
                "<ul>"
                "<li><strong>Fibratlar</strong> — gemfibrozil ve fenofibrat gibi ilaçlar "
                "trigliserid düzeyini %30–50 oranında düşürebilir.</li>"
                "<li><strong>Omega-3 yağ asidi preparatları</strong> — reçeteli yüksek "
                "dozlu EPA/DHA preparatları trigliserid düzeyini düşürmek için "
                "kullanılabilir.</li>"
                "<li><strong>Statinler</strong> — öncelikli olarak LDL kolesterolü düşürür "
                "ancak trigliseridlerde de ılımlı düşüş sağlayabilir.</li>"
                "<li><strong>Niasin (vitamin B3)</strong> — trigliserid ve LDL düşürücü "
                "etkiye sahiptir; ancak yan etkileri nedeniyle kullanımı sınırlıdır.</li>"
                "</ul>"
                "<p>İlaç tedavisi her zaman bir hekimin gözetiminde başlanmalı ve "
                "sürdürülmelidir. Yan etkiler, ilaç etkileşimleri ve dozaj ayarlamaları "
                "düzenli takip gerektirir. Kendi kendinize ilaç başlamamalı veya "
                "bırakmamalısınız.</p>"
                "<p>Çok yüksek trigliserid düzeylerinde (≥500 mg/dL) pankreatit riskini "
                "azaltmak için acil tedavi gerekebilir; bu durumda hekiminiz kombine "
                "tedavi yaklaşımı uygulayabilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda trigliserid düzeyinizi hekiminizle mutlaka "
                "değerlendirmenizi öneriyoruz:</p>"
                "<ul>"
                "<li>Trigliserid düzeyiniz <strong>200 mg/dL üzerindeyse</strong></li>"
                "<li>Ailenizde erken yaşta kalp-damar hastalığı öyküsü varsa</li>"
                "<li>Diyabet, obezite veya metabolik sendrom tanınız varsa</li>"
                "<li>Lipid panelinizdeki diğer değerler de (LDL yüksek, HDL düşük) "
                "anormalse</li>"
                "<li>Trigliserid değeriniz <strong>500 mg/dL üzerindeyse</strong> — bu "
                "durumda pankreatit riski nedeniyle acil değerlendirme gerekebilir</li>"
                "</ul>"
                "<p>Yılda en az bir kez lipid paneli yaptırmanız genel olarak tavsiye "
                "edilir. Risk faktörleriniz varsa hekiminiz daha sık kontrol "
                "önerebilir.</p>"
                "<p>Unutmayın, tek bir yüksek değer her zaman kalıcı bir soruna işaret "
                "etmez — ancak tekrarlayan yüksek değerler göz ardı edilmemelidir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya trigliserid sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p><strong><a href=\"/analyze\">Norya</a></strong> platformuna kan tahlili "
                "sonuçlarınızı yükleyerek trigliserid değerinizi ve tüm lipid profilinizi "
                "anlaşılır, yapılandırılmış bir sağlık özet raporuyla birkaç dakika içinde "
                "değerlendirebilirsiniz. Norya, sonuçlarınızı referans aralıklarıyla "
                "karşılaştırır ve sizin için anlamlı bir özet hazırlar.</p>"
                "<p>Bu rapor doktor ziyaretinize hazırlıklı gitmenizi sağlar: hangi "
                "değerlerinizin dikkat gerektirdiğini, hangi soruları sormanız gerektiğini "
                "daha net görebilirsiniz. <a href=\"/analyze\">Hemen analiz başlatın</a> "
                "ve sonuçlarınızı daha iyi anlayın.</p>"
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
            heading="What are triglycerides and why do they matter?",
            body_html=(
                "<p>If your blood test results show an elevated <strong>triglyceride</strong> "
                "level, you may wonder what that means for your health. Triglycerides are the "
                "most common type of fat circulating in your bloodstream, serving as your "
                "body's primary energy reserve. While some triglycerides are essential, "
                "chronically elevated levels are a well-established risk marker for "
                "cardiovascular disease.</p>"
                "<p>This guide explains what triglycerides are, what normal and abnormal "
                "levels mean, how they differ from cholesterol, and what steps you can take "
                "to manage them. Our goal is not to diagnose — but to help you walk into "
                "your doctor's appointment better informed.</p>"
                "<p>Your triglyceride level is influenced by many factors including diet, "
                "physical activity, genetics, and underlying health conditions. Understanding "
                "these factors is the first step toward a meaningful conversation with your "
                "healthcare provider.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="What are triglycerides?",
            body_html=(
                "<p><strong>Triglycerides</strong> are a type of lipid (fat) composed of a "
                "glycerol backbone bonded to three fatty acid chains. When you eat, your body "
                "converts any calories it does not need immediately into triglycerides, which "
                "are stored in fat cells. Between meals, hormones release triglycerides from "
                "fat tissue to provide energy.</p>"
                "<p>This is a normal and healthy process. However, if you consistently consume "
                "more calories than you burn — especially from refined carbohydrates and "
                "sugars — your blood triglyceride levels can remain chronically elevated, "
                "a condition known as <em>hypertriglyceridemia</em>.</p>"
                "<p>Triglycerides are measured as part of a standard <strong>lipid panel</strong>, "
                "alongside total cholesterol, LDL cholesterol, and HDL cholesterol. For accurate "
                "results, a fasting period of 9–12 hours before the blood draw is typically "
                "required.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Triglyceride reference ranges",
            body_html=(
                "<p>Triglyceride levels are usually reported in <strong>mg/dL</strong>. The "
                "following table shows the widely accepted classification for adults:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Category</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Level (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Borderline high</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">High</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Very high</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>These thresholds are based on guidelines from the American Heart Association "
                "(AHA) and ATP III. Keep in mind that your lab may use slightly different reference "
                "ranges; always compare your results with the values printed on your report.</p>"
                "<p>Levels above <strong>500 mg/dL</strong> are considered very high and carry "
                "a significant risk of <strong>acute pancreatitis</strong>, which requires "
                "urgent medical attention.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Causes of high triglycerides",
            body_html=(
                "<p>Elevated triglyceride levels can result from a combination of lifestyle "
                "factors, dietary habits, and underlying medical conditions:</p>"
                "<ul>"
                "<li><strong>Diet high in refined carbohydrates and sugar</strong> — white "
                "bread, sugary beverages, pastries, and processed foods drive triglyceride "
                "production.</li>"
                "<li><strong>Obesity and excess weight</strong> — particularly abdominal "
                "fat is strongly associated with high triglycerides.</li>"
                "<li><strong>Sedentary lifestyle</strong> — lack of regular physical "
                "activity slows fat metabolism.</li>"
                "<li><strong>Excess alcohol consumption</strong> — alcohol directly "
                "stimulates hepatic triglyceride synthesis.</li>"
                "<li><strong>Type 2 diabetes and insulin resistance</strong> — poorly "
                "controlled blood sugar raises triglyceride levels.</li>"
                "<li><strong>Hypothyroidism</strong> — an underactive thyroid disrupts "
                "lipid metabolism.</li>"
                "<li><strong>Genetic factors</strong> — hereditary conditions such as "
                "familial hypertriglyceridemia can cause elevated levels.</li>"
                "</ul>"
                "<p>Certain medications — including beta-blockers, diuretics, corticosteroids, "
                "and some oral contraceptives — may also raise triglycerides. Always inform "
                "your doctor about all medications you are taking when reviewing your "
                "lipid results.</p>"
                "<p>In many cases, multiple factors act together. Identifying and addressing "
                "the root causes is key to effective management.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglycerides vs. cholesterol",
            body_html=(
                "<p>Although both <strong>triglycerides</strong> and <strong>cholesterol</strong> "
                "belong to the lipid family, they serve different functions. Triglycerides store "
                "unused energy for later use, while cholesterol is needed to build cell membranes, "
                "produce hormones, and synthesize vitamin D.</p>"
                "<p>Both are measured on a standard lipid panel. <strong>LDL cholesterol</strong> "
                "(\"bad\" cholesterol) and <strong>HDL cholesterol</strong> (\"good\" cholesterol) "
                "reflect your arterial health, while triglycerides represent a separate "
                "cardiovascular risk parameter. The combination of high triglycerides and "
                "low HDL cholesterol is particularly concerning and is a hallmark of "
                "<em>metabolic syndrome</em>.</p>"
                "<p>Understanding both markers in context gives your doctor a more complete "
                "picture of your cardiovascular risk profile. For more on cholesterol, "
                "see our <a href=\"/en/blog\">cholesterol guide</a>.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Triglycerides and cardiovascular risk",
            body_html=(
                "<p>Elevated triglycerides contribute to <strong>atherosclerosis</strong> — "
                "the buildup of fatty deposits inside artery walls — thereby increasing the "
                "risk of heart attack and stroke. Research shows that high triglycerides, "
                "especially when combined with low HDL and high LDL cholesterol, significantly "
                "elevate cardiovascular event risk.</p>"
                "<p>Triglycerides travel in the blood inside <strong>VLDL</strong> (very-low-"
                "density lipoprotein) particles. These remnant particles can penetrate the "
                "arterial wall and trigger an inflammatory cascade. Additionally, high "
                "triglyceride levels promote the formation of small, dense LDL particles, "
                "which are considered more atherogenic.</p>"
                "<p>When high triglycerides co-exist with other metabolic syndrome components — "
                "abdominal obesity, hypertension, elevated fasting glucose, and low HDL — the "
                "overall cardiovascular risk rises substantially. Your doctor will assess these "
                "parameters together to determine your personal risk profile.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Lifestyle and dietary changes",
            body_html=(
                "<p>Lifestyle modifications are the first-line approach for lowering "
                "triglycerides. Evidence-based strategies include:</p>"
                "<ul>"
                "<li><strong>Reduce sugar and refined carbohydrates</strong> — replace white "
                "bread, pastries, and sugary drinks with whole grains.</li>"
                "<li><strong>Eat omega-3 fatty acids</strong> — fatty fish like salmon, "
                "sardines, and mackerel have proven triglyceride-lowering effects.</li>"
                "<li><strong>Exercise regularly</strong> — at least 150 minutes per week of "
                "moderate-intensity aerobic activity can meaningfully lower triglycerides.</li>"
                "<li><strong>Manage your weight</strong> — even a 5–10% weight loss can "
                "significantly improve triglyceride levels.</li>"
                "<li><strong>Limit alcohol intake</strong> — since alcohol directly stimulates "
                "hepatic triglyceride production, reducing or eliminating it can be highly "
                "effective.</li>"
                "</ul>"
                "<p>The effects of these changes typically become visible within weeks to a "
                "few months. Your doctor can recommend a nutritional plan tailored to your "
                "health profile. Working with a registered dietitian can be particularly "
                "beneficial for managing high triglycerides.</p>"
                "<p>The Mediterranean diet — rich in olive oil, vegetables, fruits, legumes, "
                "and whole grains — is one of the most studied dietary patterns for improving "
                "lipid profiles, including triglycerides.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medication options",
            body_html=(
                "<p>When lifestyle changes alone are insufficient, your doctor may recommend "
                "medication. The main drug classes used to lower triglycerides include:</p>"
                "<ul>"
                "<li><strong>Fibrates</strong> — drugs such as gemfibrozil and fenofibrate "
                "can reduce triglycerides by 30–50%.</li>"
                "<li><strong>Prescription omega-3 fatty acid supplements</strong> — high-dose "
                "EPA/DHA preparations are approved for triglyceride reduction.</li>"
                "<li><strong>Statins</strong> — primarily target LDL cholesterol but also "
                "provide a moderate triglyceride-lowering effect.</li>"
                "<li><strong>Niacin (vitamin B3)</strong> — lowers both triglycerides and "
                "LDL, though side effects limit its use.</li>"
                "</ul>"
                "<p>Medication should always be initiated and monitored by a physician. "
                "Side effects, drug interactions, and dosage adjustments require regular "
                "follow-up. Never start or stop a medication on your own.</p>"
                "<p>For very high levels (&ge;500 mg/dL), urgent treatment may be necessary "
                "to reduce the risk of pancreatitis; your doctor may use a combination "
                "therapy approach in such cases.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>We recommend discussing your triglyceride results with your doctor if:</p>"
                "<ul>"
                "<li>Your triglyceride level is <strong>above 200 mg/dL</strong></li>"
                "<li>There is a family history of early cardiovascular disease</li>"
                "<li>You have diabetes, obesity, or metabolic syndrome</li>"
                "<li>Other lipid panel values are also abnormal (high LDL, low HDL)</li>"
                "<li>Your triglycerides are <strong>above 500 mg/dL</strong> — urgent "
                "evaluation for pancreatitis risk may be needed</li>"
                "</ul>"
                "<p>A lipid panel at least once a year is generally recommended for adults. "
                "If you have risk factors, your doctor may suggest more frequent testing.</p>"
                "<p>Remember that a single elevated reading does not necessarily indicate a "
                "persistent problem — but consistently high values should not be ignored.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your triglyceride results",
            body_html=(
                "<p>Upload your blood test results to <strong><a href=\"/analyze\">Norya</a></strong> "
                "and receive a structured, easy-to-understand health summary report within "
                "minutes. Norya compares your triglyceride level and full lipid profile against "
                "reference ranges and prepares a clear summary tailored to you.</p>"
                "<p>This report helps you prepare for your doctor visit — you can quickly see "
                "which values need attention and what questions to ask. "
                "<a href=\"/analyze\">Start your analysis now</a> and take the first step "
                "toward understanding your results.</p>"
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
            heading="¿Qué son los triglicéridos y por qué importan?",
            body_html=(
                "<p>Cuando los resultados de su análisis de sangre muestran un nivel elevado de "
                "<strong>triglicéridos</strong>, es natural preguntarse qué significa eso para "
                "su salud. Los triglicéridos son el tipo de grasa más común en el torrente "
                "sanguíneo y funcionan como la principal reserva de energía del cuerpo. Sin "
                "embargo, cuando se mantienen crónicamente elevados, se convierten en un "
                "marcador de riesgo importante para enfermedades cardiovasculares.</p>"
                "<p>Esta guía explica qué son los triglicéridos, cuáles son los valores "
                "normales y anormales, cómo se diferencian del colesterol y qué medidas puede "
                "tomar. Nuestro objetivo no es diagnosticar, sino ayudarle a llegar a su cita "
                "médica mejor informado.</p>"
                "<p>Su nivel de triglicéridos depende de múltiples factores: dieta, actividad "
                "física, genética y condiciones de salud subyacentes. Comprender estos factores "
                "es el primer paso hacia una conversación productiva con su médico.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="¿Qué son los triglicéridos?",
            body_html=(
                "<p>Los <strong>triglicéridos</strong> son un tipo de lípido (grasa) formado "
                "por una molécula de glicerol unida a tres cadenas de ácidos grasos. Cuando "
                "comemos, el cuerpo convierte las calorías que no necesita inmediatamente en "
                "triglicéridos, que se almacenan en las células grasas. Entre comidas, las "
                "hormonas liberan triglicéridos del tejido adiposo para proporcionar energía.</p>"
                "<p>Este es un proceso normal y saludable. No obstante, si consume "
                "constantemente más calorías de las que quema — especialmente provenientes de "
                "carbohidratos refinados y azúcares — sus niveles de triglicéridos en sangre "
                "pueden permanecer crónicamente elevados, una condición denominada "
                "<em>hipertrigliceridemia</em>.</p>"
                "<p>Los triglicéridos se miden como parte del <strong>perfil lipídico</strong> "
                "estándar, junto con el colesterol total, el colesterol LDL y el colesterol "
                "HDL. Para obtener resultados precisos, se requiere un ayuno de 9–12 horas "
                "antes de la extracción de sangre.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos de referencia de triglicéridos",
            body_html=(
                "<p>Los niveles de triglicéridos suelen reportarse en <strong>mg/dL</strong>. "
                "La siguiente tabla muestra la clasificación aceptada para adultos:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Categoría</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Nivel (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Limítrofe alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Muy alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>Estos umbrales se basan en las directrices de la American Heart Association "
                "(AHA) y ATP III. Su laboratorio puede utilizar rangos ligeramente diferentes; "
                "compare siempre sus resultados con los valores de referencia de su informe.</p>"
                "<p>Los niveles superiores a <strong>500 mg/dL</strong> se consideran muy "
                "altos y conllevan un riesgo significativo de <strong>pancreatitis aguda</strong>, "
                "que requiere atención médica urgente.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Causas de los triglicéridos altos",
            body_html=(
                "<p>Los triglicéridos elevados pueden deberse a una combinación de factores "
                "relacionados con el estilo de vida, la alimentación y condiciones médicas "
                "subyacentes:</p>"
                "<ul>"
                "<li><strong>Dieta rica en carbohidratos refinados y azúcar</strong> — pan "
                "blanco, bebidas azucaradas, bollería y alimentos procesados aumentan la "
                "producción de triglicéridos.</li>"
                "<li><strong>Obesidad y sobrepeso</strong> — la grasa abdominal está "
                "estrechamente asociada con la hipertrigliceridemia.</li>"
                "<li><strong>Sedentarismo</strong> — la falta de actividad física regular "
                "ralentiza el metabolismo de las grasas.</li>"
                "<li><strong>Consumo excesivo de alcohol</strong> — el alcohol estimula "
                "directamente la síntesis hepática de triglicéridos.</li>"
                "<li><strong>Diabetes tipo 2 y resistencia a la insulina</strong> — un "
                "control glucémico deficiente eleva los triglicéridos.</li>"
                "<li><strong>Hipotiroidismo</strong> — una tiroides hipoactiva altera el "
                "metabolismo lipídico.</li>"
                "<li><strong>Factores genéticos</strong> — condiciones hereditarias como la "
                "hipertrigliceridemia familiar pueden causar niveles elevados.</li>"
                "</ul>"
                "<p>Algunos medicamentos — betabloqueantes, diuréticos, corticosteroides y "
                "ciertos anticonceptivos orales — también pueden elevar los triglicéridos. "
                "Informe siempre a su médico sobre todos los medicamentos que toma al "
                "revisar sus resultados lipídicos.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglicéridos frente a colesterol",
            body_html=(
                "<p>Aunque tanto los <strong>triglicéridos</strong> como el "
                "<strong>colesterol</strong> pertenecen a la familia de los lípidos, cumplen "
                "funciones diferentes. Los triglicéridos almacenan energía para uso posterior, "
                "mientras que el colesterol es necesario para construir membranas celulares, "
                "producir hormonas y sintetizar vitamina D.</p>"
                "<p>Ambos se miden en un perfil lipídico estándar. El <strong>colesterol "
                "LDL</strong> (\"malo\") y el <strong>colesterol HDL</strong> (\"bueno\") "
                "reflejan su salud arterial, mientras que los triglicéridos representan un "
                "parámetro de riesgo cardiovascular independiente. La combinación de "
                "triglicéridos altos y colesterol HDL bajo es especialmente preocupante y "
                "caracteriza al <em>síndrome metabólico</em>.</p>"
                "<p>Evaluar ambos marcadores en contexto permite a su médico obtener una "
                "imagen más completa de su perfil de riesgo cardiovascular.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Riesgo cardiovascular y triglicéridos",
            body_html=(
                "<p>Los triglicéridos elevados contribuyen a la <strong>aterosclerosis</strong> "
                "— la acumulación de depósitos grasos en las paredes arteriales —, lo que "
                "aumenta el riesgo de infarto de miocardio e ictus. Las investigaciones "
                "demuestran que los triglicéridos altos, sobre todo combinados con colesterol "
                "HDL bajo y LDL alto, elevan significativamente el riesgo de eventos "
                "cardiovasculares.</p>"
                "<p>Los triglicéridos se transportan en la sangre dentro de partículas "
                "<strong>VLDL</strong>. Estas partículas remanentes pueden penetrar la pared "
                "arterial y desencadenar una cascada inflamatoria. Además, los niveles altos "
                "de triglicéridos favorecen la formación de partículas LDL pequeñas y densas, "
                "consideradas más aterogénicas.</p>"
                "<p>Cuando los triglicéridos altos coexisten con otros componentes del "
                "síndrome metabólico — obesidad abdominal, hipertensión, glucemia en ayunas "
                "elevada y HDL bajo — el riesgo cardiovascular global aumenta sustancialmente.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Estilo de vida y cambios en la dieta",
            body_html=(
                "<p>Las modificaciones del estilo de vida son el enfoque de primera línea "
                "para reducir los triglicéridos. Las estrategias basadas en evidencia incluyen:</p>"
                "<ul>"
                "<li><strong>Reduzca el azúcar y los carbohidratos refinados</strong> — "
                "sustituya pan blanco, bollería y refrescos por cereales integrales.</li>"
                "<li><strong>Consuma ácidos grasos omega-3</strong> — pescados grasos como "
                "salmón, sardinas y caballa tienen efectos demostrados en la reducción de "
                "triglicéridos.</li>"
                "<li><strong>Haga ejercicio regularmente</strong> — al menos 150 minutos "
                "semanales de actividad aeróbica moderada pueden reducir significativamente "
                "los triglicéridos.</li>"
                "<li><strong>Controle su peso</strong> — una pérdida de peso del 5–10% "
                "puede mejorar notablemente los niveles de triglicéridos.</li>"
                "<li><strong>Limite el consumo de alcohol</strong> — reducirlo o eliminarlo "
                "puede ser muy eficaz.</li>"
                "</ul>"
                "<p>Los efectos de estos cambios suelen observarse en semanas o unos pocos "
                "meses. La dieta mediterránea — rica en aceite de oliva, verduras, frutas, "
                "legumbres y cereales integrales — es uno de los patrones dietéticos más "
                "estudiados para mejorar el perfil lipídico.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Opciones farmacológicas",
            body_html=(
                "<p>Cuando los cambios en el estilo de vida no son suficientes, su médico "
                "puede recomendar medicación. Los principales grupos farmacológicos para "
                "reducir los triglicéridos son:</p>"
                "<ul>"
                "<li><strong>Fibratos</strong> — gemfibrozilo y fenofibrato pueden reducir "
                "los triglicéridos entre un 30 y un 50%.</li>"
                "<li><strong>Suplementos de omega-3 con receta</strong> — preparados de "
                "EPA/DHA en dosis altas están aprobados para la reducción de triglicéridos.</li>"
                "<li><strong>Estatinas</strong> — dirigidas principalmente al colesterol LDL, "
                "también proporcionan una reducción moderada de triglicéridos.</li>"
                "<li><strong>Niacina (vitamina B3)</strong> — reduce triglicéridos y LDL, "
                "aunque sus efectos secundarios limitan su uso.</li>"
                "</ul>"
                "<p>La medicación debe iniciarse y supervisarse siempre bajo control médico. "
                "Los efectos secundarios, las interacciones y los ajustes de dosis requieren "
                "seguimiento regular.</p>"
                "<p>En niveles muy altos (&ge;500 mg/dL), puede ser necesario un tratamiento "
                "urgente para reducir el riesgo de pancreatitis.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Le recomendamos comentar sus resultados de triglicéridos con su médico si:</p>"
                "<ul>"
                "<li>Su nivel de triglicéridos supera los <strong>200 mg/dL</strong></li>"
                "<li>Existe antecedente familiar de enfermedad cardiovascular temprana</li>"
                "<li>Tiene diagnóstico de diabetes, obesidad o síndrome metabólico</li>"
                "<li>Otros valores del perfil lipídico también son anormales (LDL alto, "
                "HDL bajo)</li>"
                "<li>Sus triglicéridos superan los <strong>500 mg/dL</strong> — puede "
                "requerirse evaluación urgente por riesgo de pancreatitis</li>"
                "</ul>"
                "<p>Se recomienda realizar un perfil lipídico al menos una vez al año. Si "
                "presenta factores de riesgo, su médico puede sugerir controles más frecuentes.</p>"
                "<p>Recuerde que una sola lectura elevada no siempre indica un problema "
                "persistente, pero los valores elevados constantes no deben ignorarse.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya le ayuda a entender sus resultados",
            body_html=(
                "<p>Suba sus resultados de análisis de sangre a "
                "<strong><a href=\"/analyze\">Norya</a></strong> y reciba un informe de "
                "salud estructurado y fácil de entender en cuestión de minutos. Norya "
                "compara su nivel de triglicéridos y su perfil lipídico completo con los "
                "rangos de referencia y prepara un resumen claro adaptado a usted.</p>"
                "<p>Este informe le ayuda a prepararse para su cita médica: podrá ver "
                "rápidamente qué valores requieren atención y qué preguntas formular. "
                "<a href=\"/analyze\">Inicie su análisis ahora</a> y dé el primer paso "
                "para comprender sus resultados.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el '
                'diagnóstico médico.</strong> Consulte siempre sus resultados con un '
                'profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'
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
            heading="Was sind Triglyceride und warum sind sie wichtig?",
            body_html=(
                "<p>Wenn Ihr Blutbild einen erhöhten <strong>Triglycerid</strong>-Wert "
                "anzeigt, fragen Sie sich vielleicht, was das für Ihre Gesundheit bedeutet. "
                "Triglyceride sind die häufigste Fettart in Ihrem Blut und dienen als "
                "wichtigster Energiespeicher des Körpers. Chronisch erhöhte Werte gelten "
                "jedoch als anerkannter Risikomarker für Herz-Kreislauf-Erkrankungen.</p>"
                "<p>Dieser Leitfaden erklärt, was Triglyceride sind, welche Werte als normal "
                "oder auffällig gelten, wie sie sich von Cholesterin unterscheiden und welche "
                "Maßnahmen Sie ergreifen können. Unser Ziel ist es nicht, eine Diagnose zu "
                "stellen, sondern Sie auf Ihren Arzttermin besser vorzubereiten.</p>"
                "<p>Ihr Triglycerid-Spiegel wird von zahlreichen Faktoren beeinflusst — "
                "Ernährung, Bewegung, Genetik und bestehende Erkrankungen. Das Verständnis "
                "dieser Zusammenhänge ist der erste Schritt zu einem sinnvollen Gespräch mit "
                "Ihrem Arzt.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Was sind Triglyceride?",
            body_html=(
                "<p><strong>Triglyceride</strong> sind Lipide (Fette), die aus einem "
                "Glycerin-Molekül und drei Fettsäureketten bestehen. Wenn Sie essen, wandelt "
                "Ihr Körper Kalorien, die er nicht sofort benötigt, in Triglyceride um und "
                "speichert sie in den Fettzellen. Zwischen den Mahlzeiten setzen Hormone "
                "diese gespeicherten Triglyceride frei, um Energie bereitzustellen.</p>"
                "<p>Das ist ein normaler und gesunder Prozess. Wenn Sie jedoch dauerhaft mehr "
                "Kalorien aufnehmen als verbrauchen — insbesondere aus raffinierten "
                "Kohlenhydraten und Zucker —, können Ihre Triglycerid-Werte chronisch "
                "erhöht bleiben. Dieser Zustand wird als <em>Hypertriglyceridämie</em> "
                "bezeichnet.</p>"
                "<p>Triglyceride werden im Rahmen eines <strong>Lipidprofils</strong> gemessen, "
                "zusammen mit Gesamtcholesterin, LDL- und HDL-Cholesterin. Für genaue "
                "Ergebnisse ist eine Nüchternzeit von 9–12 Stunden vor der Blutentnahme "
                "erforderlich.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Triglycerid-Referenzbereiche",
            body_html=(
                "<p>Triglycerid-Werte werden üblicherweise in <strong>mg/dL</strong> angegeben. "
                "Die folgende Tabelle zeigt die allgemein anerkannte Klassifizierung für "
                "Erwachsene:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Kategorie</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Wert (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Grenzwertig hoch</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hoch</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Sehr hoch</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>Diese Schwellenwerte basieren auf den Leitlinien der American Heart "
                "Association (AHA) und ATP III. Ihr Labor kann leicht abweichende "
                "Referenzbereiche verwenden — vergleichen Sie Ihre Ergebnisse immer mit den "
                "auf Ihrem Bericht angegebenen Werten.</p>"
                "<p>Werte über <strong>500 mg/dL</strong> gelten als sehr hoch und bergen ein "
                "erhebliches Risiko für eine <strong>akute Pankreatitis</strong>, die eine "
                "dringende ärztliche Behandlung erfordert.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Ursachen erhöhter Triglyceride",
            body_html=(
                "<p>Erhöhte Triglycerid-Werte können durch eine Kombination aus "
                "Lebensstilfaktoren, Ernährungsgewohnheiten und zugrunde liegenden "
                "Erkrankungen verursacht werden:</p>"
                "<ul>"
                "<li><strong>Ernährung reich an raffinierten Kohlenhydraten und Zucker</strong> "
                "— Weißbrot, zuckerhaltige Getränke, Gebäck und verarbeitete Lebensmittel "
                "steigern die Triglycerid-Produktion.</li>"
                "<li><strong>Übergewicht und Adipositas</strong> — insbesondere abdominales "
                "Fett ist stark mit Hypertriglyceridämie assoziiert.</li>"
                "<li><strong>Bewegungsmangel</strong> — fehlende regelmäßige körperliche "
                "Aktivität verlangsamt den Fettstoffwechsel.</li>"
                "<li><strong>Übermäßiger Alkoholkonsum</strong> — Alkohol stimuliert direkt "
                "die hepatische Triglycerid-Synthese.</li>"
                "<li><strong>Typ-2-Diabetes und Insulinresistenz</strong> — schlecht "
                "eingestellter Blutzucker erhöht die Triglycerid-Werte.</li>"
                "<li><strong>Hypothyreose</strong> — eine Schilddrüsenunterfunktion stört "
                "den Fettstoffwechsel.</li>"
                "<li><strong>Genetische Faktoren</strong> — erbliche Erkrankungen wie die "
                "familiäre Hypertriglyceridämie können zu erhöhten Werten führen.</li>"
                "</ul>"
                "<p>Bestimmte Medikamente — Betablocker, Diuretika, Kortikosteroide und "
                "einige orale Kontrazeptiva — können ebenfalls die Triglyceride erhöhen. "
                "Informieren Sie Ihren Arzt stets über alle Medikamente, die Sie "
                "einnehmen.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglyceride im Vergleich zu Cholesterin",
            body_html=(
                "<p>Obwohl sowohl <strong>Triglyceride</strong> als auch "
                "<strong>Cholesterin</strong> zu den Lipiden gehören, erfüllen sie "
                "unterschiedliche Funktionen. Triglyceride speichern überschüssige Energie "
                "für späteren Verbrauch, während Cholesterin für den Aufbau von Zellmembranen, "
                "die Hormonproduktion und die Vitamin-D-Synthese benötigt wird.</p>"
                "<p>Beide werden in einem Standard-Lipidprofil gemessen. <strong>LDL-Cholesterin"
                "</strong> (&bdquo;schlechtes&ldquo; Cholesterin) und <strong>HDL-Cholesterin</strong> "
                "(&bdquo;gutes&ldquo; Cholesterin) spiegeln Ihre arterielle Gesundheit wider, während "
                "Triglyceride einen eigenständigen kardiovaskulären Risikoparameter darstellen. "
                "Die Kombination aus hohen Triglyceriden und niedrigem HDL ist besonders "
                "besorgniserregend und ein Kennzeichen des <em>metabolischen Syndroms</em>.</p>"
                "<p>Die gemeinsame Betrachtung beider Marker ermöglicht Ihrem Arzt eine "
                "umfassendere Einschätzung Ihres kardiovaskulären Risikoprofils.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Kardiovaskuläres Risiko und Triglyceride",
            body_html=(
                "<p>Erhöhte Triglyceride tragen zur <strong>Atherosklerose</strong> bei — der "
                "Ansammlung von Fettablagerungen in den Arterienwänden —, was das Risiko für "
                "Herzinfarkt und Schlaganfall erhöht. Studien zeigen, dass hohe Triglyceride, "
                "insbesondere in Verbindung mit niedrigem HDL und hohem LDL, das Risiko "
                "kardiovaskulärer Ereignisse erheblich steigern.</p>"
                "<p>Triglyceride werden im Blut in <strong>VLDL</strong>-Partikeln transportiert. "
                "Diese Remnant-Partikel können in die Arterienwand eindringen und eine "
                "entzündliche Kaskade auslösen. Darüber hinaus fördern hohe Triglycerid-Werte "
                "die Bildung kleiner, dichter LDL-Partikel, die als atherogener gelten.</p>"
                "<p>Wenn hohe Triglyceride mit anderen Komponenten des metabolischen Syndroms "
                "zusammentreffen — abdominale Adipositas, Bluthochdruck, erhöhter "
                "Nüchternblutzucker und niedriges HDL —, steigt das kardiovaskuläre "
                "Gesamtrisiko erheblich.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Lebensstil- und Ernährungsänderungen",
            body_html=(
                "<p>Lebensstiländerungen sind der erste Ansatz zur Senkung der Triglyceride. "
                "Evidenzbasierte Strategien umfassen:</p>"
                "<ul>"
                "<li><strong>Zucker und raffinierte Kohlenhydrate reduzieren</strong> — "
                "ersetzen Sie Weißbrot, Gebäck und zuckerhaltige Getränke durch "
                "Vollkornprodukte.</li>"
                "<li><strong>Omega-3-Fettsäuren essen</strong> — fetter Fisch wie Lachs, "
                "Sardinen und Makrele hat nachgewiesene triglycerid-senkende Wirkung.</li>"
                "<li><strong>Regelmäßig bewegen</strong> — mindestens 150 Minuten moderate "
                "aerobe Aktivität pro Woche können die Triglyceride deutlich senken.</li>"
                "<li><strong>Gewicht kontrollieren</strong> — schon ein Gewichtsverlust von "
                "5–10 % kann die Triglycerid-Werte spürbar verbessern.</li>"
                "<li><strong>Alkoholkonsum einschränken</strong> — da Alkohol die hepatische "
                "Triglycerid-Produktion direkt anregt, kann eine Reduktion sehr wirksam "
                "sein.</li>"
                "</ul>"
                "<p>Die Effekte dieser Veränderungen zeigen sich in der Regel innerhalb weniger "
                "Wochen bis Monate. Die Mittelmeerdiät — reich an Olivenöl, Gemüse, Obst, "
                "Hülsenfrüchten und Vollkornprodukten — ist eines der am besten untersuchten "
                "Ernährungsmuster zur Verbesserung des Lipidprofils.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medikamentöse Behandlung",
            body_html=(
                "<p>Wenn Lebensstiländerungen allein nicht ausreichen, kann Ihr Arzt "
                "Medikamente empfehlen. Die wichtigsten Wirkstoffgruppen zur Senkung der "
                "Triglyceride sind:</p>"
                "<ul>"
                "<li><strong>Fibrate</strong> — Gemfibrozil und Fenofibrat können die "
                "Triglyceride um 30–50 % senken.</li>"
                "<li><strong>Verschreibungspflichtige Omega-3-Präparate</strong> — "
                "hochdosierte EPA/DHA-Präparate sind zur Triglycerid-Senkung zugelassen.</li>"
                "<li><strong>Statine</strong> — senken primär das LDL-Cholesterin, bieten "
                "aber auch eine moderate Triglycerid-Senkung.</li>"
                "<li><strong>Niacin (Vitamin B3)</strong> — senkt Triglyceride und LDL, "
                "Nebenwirkungen begrenzen jedoch den Einsatz.</li>"
                "</ul>"
                "<p>Medikamente sollten immer unter ärztlicher Aufsicht begonnen und "
                "überwacht werden. Nebenwirkungen, Wechselwirkungen und Dosisanpassungen "
                "erfordern regelmäßige Kontrolle.</p>"
                "<p>Bei sehr hohen Werten (&ge;500 mg/dL) kann eine dringende Behandlung "
                "erforderlich sein, um das Pankreatitis-Risiko zu senken.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann zum Arzt?",
            body_html=(
                "<p>Wir empfehlen, Ihre Triglycerid-Ergebnisse mit Ihrem Arzt zu besprechen, "
                "wenn:</p>"
                "<ul>"
                "<li>Ihr Triglycerid-Wert <strong>über 200 mg/dL</strong> liegt</li>"
                "<li>Eine familiäre Vorgeschichte früher Herz-Kreislauf-Erkrankungen "
                "besteht</li>"
                "<li>Sie an Diabetes, Adipositas oder metabolischem Syndrom leiden</li>"
                "<li>Weitere Werte im Lipidprofil auffällig sind (hohes LDL, niedriges HDL)</li>"
                "<li>Ihre Triglyceride <strong>über 500 mg/dL</strong> liegen — hier kann "
                "eine dringende Beurteilung wegen Pankreatitis-Risiko nötig sein</li>"
                "</ul>"
                "<p>Ein Lipidprofil mindestens einmal jährlich wird generell empfohlen. Bei "
                "vorhandenen Risikofaktoren kann Ihr Arzt häufigere Kontrollen vorschlagen.</p>"
                "<p>Bedenken Sie: Ein einzelner erhöhter Wert muss nicht zwingend auf ein "
                "dauerhaftes Problem hindeuten — anhaltend hohe Werte sollten jedoch nicht "
                "ignoriert werden.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihre Triglycerid-Ergebnisse zu verstehen",
            body_html=(
                "<p>Laden Sie Ihre Blutuntersuchungsergebnisse auf "
                "<strong><a href=\"/analyze\">Norya</a></strong> hoch und erhalten Sie "
                "innerhalb von Minuten einen strukturierten, leicht verständlichen "
                "Gesundheitsbericht. Norya vergleicht Ihren Triglycerid-Wert und Ihr "
                "gesamtes Lipidprofil mit Referenzbereichen und erstellt eine übersichtliche "
                "Zusammenfassung.</p>"
                "<p>Dieser Bericht bereitet Sie auf Ihren Arztbesuch vor — Sie sehen auf "
                "einen Blick, welche Werte Aufmerksamkeit erfordern und welche Fragen Sie "
                "stellen sollten. <a href=\"/analyze\">Starten Sie jetzt Ihre Analyse</a> "
                "und verstehen Sie Ihre Ergebnisse besser.</p>"
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
            heading="Que sont les triglycérides et pourquoi sont-ils importants ?",
            body_html=(
                "<p>Lorsque vos résultats d'analyse de sang révèlent un taux élevé de "
                "<strong>triglycérides</strong>, il est naturel de se demander ce que cela "
                "signifie pour votre santé. Les triglycérides sont le type de graisse le plus "
                "répandu dans le sang et constituent la principale réserve d'énergie de "
                "l'organisme. Toutefois, des taux chroniquement élevés représentent un "
                "marqueur de risque reconnu pour les maladies cardiovasculaires.</p>"
                "<p>Ce guide explique ce que sont les triglycérides, quels taux sont considérés "
                "comme normaux ou élevés, en quoi ils diffèrent du cholestérol et quelles "
                "mesures vous pouvez prendre. Notre but n'est pas de poser un diagnostic, "
                "mais de vous aider à vous préparer à votre rendez-vous médical.</p>"
                "<p>Votre taux de triglycérides est influencé par de nombreux facteurs : "
                "alimentation, activité physique, génétique et état de santé général. "
                "Comprendre ces facteurs est le premier pas vers un dialogue constructif "
                "avec votre médecin.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Que sont les triglycérides ?",
            body_html=(
                "<p>Les <strong>triglycérides</strong> sont des lipides composés d'une "
                "molécule de glycérol liée à trois chaînes d'acides gras. Après un repas, "
                "le corps transforme les calories dont il n'a pas besoin immédiatement en "
                "triglycérides, qui sont stockés dans les cellules adipeuses. Entre les "
                "repas, des hormones libèrent ces triglycérides pour fournir de l'énergie.</p>"
                "<p>Ce processus est normal et sain. Cependant, si vous consommez régulièrement "
                "plus de calories que vous n'en dépensez — surtout sous forme de glucides "
                "raffinés et de sucres —, votre taux sanguin de triglycérides peut rester "
                "chroniquement élevé, un état appelé <em>hypertriglycéridémie</em>.</p>"
                "<p>Les triglycérides sont mesurés dans le cadre d'un <strong>bilan "
                "lipidique</strong> standard, aux côtés du cholestérol total, du LDL et du "
                "HDL cholestérol. Un jeûne de 9 à 12 heures avant le prélèvement sanguin "
                "est généralement nécessaire pour des résultats fiables.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs de référence des triglycérides",
            body_html=(
                "<p>Les taux de triglycérides sont habituellement exprimés en "
                "<strong>mg/dL</strong>. Le tableau ci-dessous montre la classification "
                "couramment utilisée chez l'adulte :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Catégorie</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Taux (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Limite haute</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Élevé</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Très élevé</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>Ces seuils sont basés sur les recommandations de l'American Heart "
                "Association (AHA) et l'ATP III. Votre laboratoire peut utiliser des plages "
                "de référence légèrement différentes ; comparez toujours vos résultats avec "
                "les valeurs indiquées sur votre compte-rendu.</p>"
                "<p>Les taux supérieurs à <strong>500 mg/dL</strong> sont considérés comme "
                "très élevés et comportent un risque important de <strong>pancréatite "
                "aiguë</strong>, nécessitant une prise en charge médicale urgente.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Causes des triglycérides élevés",
            body_html=(
                "<p>Les triglycérides élevés peuvent résulter d'une combinaison de facteurs "
                "liés au mode de vie, à l'alimentation et à des pathologies sous-jacentes :</p>"
                "<ul>"
                "<li><strong>Alimentation riche en glucides raffinés et en sucre</strong> — "
                "pain blanc, boissons sucrées, pâtisseries et aliments transformés augmentent "
                "la production de triglycérides.</li>"
                "<li><strong>Obésité et surpoids</strong> — la graisse abdominale est "
                "fortement associée à l'hypertriglycéridémie.</li>"
                "<li><strong>Sédentarité</strong> — le manque d'activité physique régulière "
                "ralentit le métabolisme des graisses.</li>"
                "<li><strong>Consommation excessive d'alcool</strong> — l'alcool stimule "
                "directement la synthèse hépatique des triglycérides.</li>"
                "<li><strong>Diabète de type 2 et résistance à l'insuline</strong> — un "
                "mauvais contrôle glycémique augmente les triglycérides.</li>"
                "<li><strong>Hypothyroïdie</strong> — une thyroïde hypoactive perturbe le "
                "métabolisme lipidique.</li>"
                "<li><strong>Facteurs génétiques</strong> — des affections héréditaires comme "
                "l'hypertriglycéridémie familiale peuvent entraîner des taux élevés.</li>"
                "</ul>"
                "<p>Certains médicaments — bêtabloquants, diurétiques, corticostéroïdes et "
                "certains contraceptifs oraux — peuvent également augmenter les triglycérides. "
                "Informez toujours votre médecin de tous vos traitements en cours lors de "
                "l'interprétation de vos résultats lipidiques.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Triglycérides et cholestérol : quelle différence ?",
            body_html=(
                "<p>Bien que les <strong>triglycérides</strong> et le <strong>cholestérol</strong> "
                "appartiennent tous deux à la famille des lipides, ils remplissent des fonctions "
                "différentes. Les triglycérides stockent l'énergie excédentaire, tandis que le "
                "cholestérol sert à construire les membranes cellulaires, produire des hormones "
                "et synthétiser la vitamine D.</p>"
                "<p>Tous deux sont mesurés dans le bilan lipidique standard. Le <strong>cholestérol "
                "LDL</strong> (« mauvais ») et le <strong>cholestérol HDL</strong> (« bon ») "
                "reflètent la santé artérielle, tandis que les triglycérides constituent un "
                "paramètre de risque cardiovasculaire distinct. L'association de triglycérides "
                "élevés et de HDL bas est particulièrement préoccupante et caractéristique du "
                "<em>syndrome métabolique</em>.</p>"
                "<p>Analyser ces deux marqueurs ensemble permet à votre médecin d'obtenir une "
                "image plus complète de votre profil de risque cardiovasculaire.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Risque cardiovasculaire et triglycérides",
            body_html=(
                "<p>Les triglycérides élevés contribuent à l'<strong>athérosclérose</strong> — "
                "l'accumulation de dépôts graisseux dans les parois artérielles —, augmentant "
                "ainsi le risque d'infarctus du myocarde et d'accident vasculaire cérébral. "
                "Les études montrent que des triglycérides élevés, surtout combinés à un HDL "
                "bas et un LDL élevé, accroissent significativement le risque d'événements "
                "cardiovasculaires.</p>"
                "<p>Les triglycérides circulent dans le sang au sein de particules "
                "<strong>VLDL</strong>. Ces particules résiduelles peuvent pénétrer la paroi "
                "artérielle et déclencher une cascade inflammatoire. De plus, des taux "
                "élevés de triglycérides favorisent la formation de particules LDL petites "
                "et denses, considérées comme plus athérogènes.</p>"
                "<p>Lorsque des triglycérides élevés coexistent avec d'autres composantes du "
                "syndrome métabolique — obésité abdominale, hypertension, glycémie à jeun "
                "élevée et HDL bas —, le risque cardiovasculaire global augmente "
                "considérablement.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Mode de vie et changements alimentaires",
            body_html=(
                "<p>Les modifications du mode de vie constituent l'approche de première "
                "intention pour réduire les triglycérides. Les stratégies fondées sur les "
                "preuves incluent :</p>"
                "<ul>"
                "<li><strong>Réduire le sucre et les glucides raffinés</strong> — remplacez "
                "le pain blanc, les pâtisseries et les boissons sucrées par des céréales "
                "complètes.</li>"
                "<li><strong>Consommer des acides gras oméga-3</strong> — les poissons gras "
                "comme le saumon, les sardines et le maquereau ont un effet prouvé sur la "
                "baisse des triglycérides.</li>"
                "<li><strong>Pratiquer une activité physique régulière</strong> — au moins "
                "150 minutes par semaine d'activité aérobique modérée peuvent réduire "
                "sensiblement les triglycérides.</li>"
                "<li><strong>Contrôler son poids</strong> — une perte de poids de 5 à 10 % "
                "peut améliorer significativement les taux de triglycérides.</li>"
                "<li><strong>Limiter la consommation d'alcool</strong> — la réduire ou la "
                "supprimer peut s'avérer très efficace.</li>"
                "</ul>"
                "<p>Les effets de ces changements apparaissent généralement en quelques "
                "semaines à quelques mois. Le régime méditerranéen — riche en huile d'olive, "
                "légumes, fruits, légumineuses et céréales complètes — est l'un des modèles "
                "alimentaires les plus étudiés pour améliorer le profil lipidique.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Options médicamenteuses",
            body_html=(
                "<p>Lorsque les changements de mode de vie ne suffisent pas, votre médecin "
                "peut prescrire un traitement médicamenteux. Les principales classes "
                "thérapeutiques pour réduire les triglycérides sont :</p>"
                "<ul>"
                "<li><strong>Fibrates</strong> — le gemfibrozil et le fénofibrate peuvent "
                "réduire les triglycérides de 30 à 50 %.</li>"
                "<li><strong>Suppléments d'oméga-3 sur ordonnance</strong> — des préparations "
                "à haute dose d'EPA/DHA sont approuvées pour réduire les triglycérides.</li>"
                "<li><strong>Statines</strong> — ciblent principalement le LDL-cholestérol "
                "mais offrent aussi une réduction modérée des triglycérides.</li>"
                "<li><strong>Niacine (vitamine B3)</strong> — réduit les triglycérides et le "
                "LDL, mais ses effets indésirables limitent son utilisation.</li>"
                "</ul>"
                "<p>Les médicaments doivent toujours être initiés et surveillés par un médecin. "
                "Les effets secondaires, les interactions et les ajustements de posologie "
                "nécessitent un suivi régulier.</p>"
                "<p>Pour des taux très élevés (&ge;500 mg/dL), un traitement urgent peut "
                "s'avérer nécessaire afin de réduire le risque de pancréatite.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin",
            body_html=(
                "<p>Nous vous recommandons de discuter de vos résultats de triglycérides "
                "avec votre médecin si :</p>"
                "<ul>"
                "<li>Votre taux de triglycérides dépasse <strong>200 mg/dL</strong></li>"
                "<li>Il existe des antécédents familiaux de maladie cardiovasculaire "
                "précoce</li>"
                "<li>Vous êtes atteint de diabète, d'obésité ou de syndrome métabolique</li>"
                "<li>D'autres valeurs du bilan lipidique sont anormales (LDL élevé, "
                "HDL bas)</li>"
                "<li>Vos triglycérides dépassent <strong>500 mg/dL</strong> — une "
                "évaluation urgente pour risque de pancréatite peut être nécessaire</li>"
                "</ul>"
                "<p>Un bilan lipidique au moins une fois par an est généralement recommandé. "
                "En présence de facteurs de risque, votre médecin peut proposer des contrôles "
                "plus fréquents.</p>"
                "<p>N'oubliez pas qu'une seule valeur élevée ne signifie pas nécessairement un "
                "problème persistant, mais des taux élevés répétés ne doivent pas être "
                "négligés.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre vos résultats",
            body_html=(
                "<p>Téléchargez vos résultats d'analyses sanguines sur "
                "<strong><a href=\"/analyze\">Norya</a></strong> et recevez en quelques "
                "minutes un rapport de santé structuré et facile à comprendre. Norya compare "
                "votre taux de triglycérides et l'ensemble de votre profil lipidique avec les "
                "valeurs de référence et prépare un résumé clair et personnalisé.</p>"
                "<p>Ce rapport vous aide à préparer votre consultation médicale : vous voyez "
                "rapidement quelles valeurs nécessitent une attention particulière et quelles "
                "questions poser. <a href=\"/analyze\">Commencez votre analyse maintenant</a> "
                "et faites le premier pas vers une meilleure compréhension de vos résultats.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace '
                "pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos "
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
            heading="Cosa sono i trigliceridi e perché sono importanti?",
            body_html=(
                "<p>Se i risultati delle analisi del sangue mostrano un livello elevato di "
                "<strong>trigliceridi</strong>, è naturale chiedersi cosa significhi per la "
                "propria salute. I trigliceridi sono il tipo di grasso più comune nel sangue e "
                "rappresentano la principale riserva energetica dell'organismo. Tuttavia, "
                "livelli cronicamente elevati sono un riconosciuto marcatore di rischio per le "
                "malattie cardiovascolari.</p>"
                "<p>Questa guida spiega cosa sono i trigliceridi, quali valori sono considerati "
                "normali o elevati, come si differenziano dal colesterolo e quali misure "
                "adottare. Il nostro obiettivo non è formulare una diagnosi, ma aiutarvi a "
                "presentarvi dal medico più informati.</p>"
                "<p>Il livello dei trigliceridi è influenzato da numerosi fattori: dieta, "
                "attività fisica, genetica e condizioni di salute preesistenti. Comprendere "
                "questi fattori è il primo passo verso un dialogo costruttivo con il vostro "
                "medico.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="Cosa sono i trigliceridi?",
            body_html=(
                "<p>I <strong>trigliceridi</strong> sono lipidi (grassi) composti da una "
                "molecola di glicerolo legata a tre catene di acidi grassi. Quando mangiamo, "
                "il corpo converte le calorie che non necessita immediatamente in trigliceridi, "
                "che vengono immagazzinati nelle cellule adipose. Tra i pasti, gli ormoni "
                "rilasciano questi trigliceridi dal tessuto adiposo per fornire energia.</p>"
                "<p>Si tratta di un processo normale e sano. Tuttavia, se si consumano "
                "regolarmente più calorie di quante se ne brucino — soprattutto da "
                "carboidrati raffinati e zuccheri — i livelli ematici di trigliceridi possono "
                "rimanere cronicamente elevati, una condizione denominata "
                "<em>ipertrigliceridemia</em>.</p>"
                "<p>I trigliceridi vengono misurati nel quadro di un <strong>profilo "
                "lipidico</strong> standard, insieme al colesterolo totale, al colesterolo "
                "LDL e al colesterolo HDL. Per risultati accurati è generalmente richiesto un "
                "digiuno di 9–12 ore prima del prelievo.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Intervalli di riferimento dei trigliceridi",
            body_html=(
                "<p>I livelli di trigliceridi sono solitamente espressi in "
                "<strong>mg/dL</strong>. La tabella seguente illustra la classificazione "
                "comunemente accettata per gli adulti:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Categoria</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valore (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normale</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Limite alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Molto alto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>Queste soglie si basano sulle linee guida dell'American Heart Association "
                "(AHA) e dell'ATP III. Il vostro laboratorio può utilizzare intervalli "
                "leggermente diversi; confrontate sempre i risultati con i valori di "
                "riferimento presenti nel referto.</p>"
                "<p>Livelli superiori a <strong>500 mg/dL</strong> sono considerati molto "
                "elevati e comportano un rischio significativo di <strong>pancreatite "
                "acuta</strong>, che richiede un intervento medico urgente.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="Cause dei trigliceridi alti",
            body_html=(
                "<p>I trigliceridi elevati possono derivare da una combinazione di fattori "
                "legati allo stile di vita, all'alimentazione e a condizioni mediche "
                "sottostanti:</p>"
                "<ul>"
                "<li><strong>Dieta ricca di carboidrati raffinati e zucchero</strong> — "
                "pane bianco, bevande zuccherate, dolci e alimenti trasformati aumentano la "
                "produzione di trigliceridi.</li>"
                "<li><strong>Obesità e sovrappeso</strong> — il grasso addominale è "
                "fortemente associato all'ipertrigliceridemia.</li>"
                "<li><strong>Sedentarietà</strong> — la mancanza di attività fisica regolare "
                "rallenta il metabolismo dei grassi.</li>"
                "<li><strong>Consumo eccessivo di alcol</strong> — l'alcol stimola "
                "direttamente la sintesi epatica dei trigliceridi.</li>"
                "<li><strong>Diabete di tipo 2 e resistenza all'insulina</strong> — uno "
                "scarso controllo glicemico innalza i trigliceridi.</li>"
                "<li><strong>Ipotiroidismo</strong> — una tiroide ipoattiva altera il "
                "metabolismo lipidico.</li>"
                "<li><strong>Fattori genetici</strong> — condizioni ereditarie come "
                "l'ipertrigliceridemia familiare possono causare livelli elevati.</li>"
                "</ul>"
                "<p>Alcuni farmaci — beta-bloccanti, diuretici, corticosteroidi e alcuni "
                "contraccettivi orali — possono anch'essi aumentare i trigliceridi. Informate "
                "sempre il medico di tutti i farmaci che assumete quando discutete i vostri "
                "risultati lipidici.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="Trigliceridi e colesterolo a confronto",
            body_html=(
                "<p>Sebbene <strong>trigliceridi</strong> e <strong>colesterolo</strong> "
                "appartengano entrambi alla famiglia dei lipidi, svolgono funzioni diverse. "
                "I trigliceridi immagazzinano energia per un uso successivo, mentre il "
                "colesterolo è necessario per costruire le membrane cellulari, produrre "
                "ormoni e sintetizzare la vitamina D.</p>"
                "<p>Entrambi vengono misurati nel profilo lipidico standard. Il "
                "<strong>colesterolo LDL</strong> (\"cattivo\") e il <strong>colesterolo "
                "HDL</strong> (\"buono\") riflettono la salute arteriosa, mentre i "
                "trigliceridi rappresentano un parametro di rischio cardiovascolare "
                "indipendente. La combinazione di trigliceridi alti e HDL basso è "
                "particolarmente preoccupante e tipica della <em>sindrome metabolica</em>.</p>"
                "<p>Valutare entrambi i marcatori nel contesto consente al medico di ottenere "
                "un quadro più completo del vostro profilo di rischio cardiovascolare.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="Rischio cardiovascolare e trigliceridi",
            body_html=(
                "<p>I trigliceridi elevati contribuiscono all'<strong>aterosclerosi</strong> — "
                "l'accumulo di depositi grassi nelle pareti arteriose —, aumentando il rischio "
                "di infarto miocardico e ictus. Gli studi dimostrano che trigliceridi alti, "
                "soprattutto associati a HDL basso e LDL elevato, accrescono significativamente "
                "il rischio di eventi cardiovascolari.</p>"
                "<p>I trigliceridi circolano nel sangue all'interno di particelle "
                "<strong>VLDL</strong>. Queste particelle residue possono penetrare la parete "
                "arteriosa e innescare una cascata infiammatoria. Inoltre, livelli elevati di "
                "trigliceridi favoriscono la formazione di particelle LDL piccole e dense, "
                "considerate più aterogene.</p>"
                "<p>Quando i trigliceridi elevati coesistono con altri componenti della "
                "sindrome metabolica — obesità addominale, ipertensione, glicemia a digiuno "
                "elevata e HDL basso — il rischio cardiovascolare complessivo aumenta "
                "in modo sostanziale.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="Stile di vita e modifiche alimentari",
            body_html=(
                "<p>Le modifiche dello stile di vita rappresentano il primo approccio per "
                "ridurre i trigliceridi. Le strategie basate sulle evidenze comprendono:</p>"
                "<ul>"
                "<li><strong>Ridurre zucchero e carboidrati raffinati</strong> — sostituite "
                "pane bianco, dolci e bevande zuccherate con cereali integrali.</li>"
                "<li><strong>Consumare acidi grassi omega-3</strong> — pesci grassi come "
                "salmone, sardine e sgombro hanno un effetto dimostrato sulla riduzione "
                "dei trigliceridi.</li>"
                "<li><strong>Fare esercizio fisico regolare</strong> — almeno 150 minuti "
                "settimanali di attività aerobica moderata possono ridurre sensibilmente "
                "i trigliceridi.</li>"
                "<li><strong>Controllare il peso</strong> — anche una perdita del 5–10% "
                "può migliorare significativamente i livelli di trigliceridi.</li>"
                "<li><strong>Limitare il consumo di alcol</strong> — ridurlo o eliminarlo "
                "può risultare molto efficace.</li>"
                "</ul>"
                "<p>Gli effetti di questi cambiamenti si manifestano generalmente nell'arco "
                "di alcune settimane o mesi. La dieta mediterranea — ricca di olio d'oliva, "
                "verdure, frutta, legumi e cereali integrali — è uno dei modelli alimentari "
                "più studiati per migliorare il profilo lipidico.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Opzioni farmacologiche",
            body_html=(
                "<p>Quando le modifiche dello stile di vita non sono sufficienti, il medico "
                "può prescrivere un trattamento farmacologico. Le principali classi di "
                "farmaci per ridurre i trigliceridi sono:</p>"
                "<ul>"
                "<li><strong>Fibrati</strong> — gemfibrozil e fenofibrato possono ridurre "
                "i trigliceridi del 30–50%.</li>"
                "<li><strong>Integratori di omega-3 su prescrizione</strong> — preparati ad "
                "alto dosaggio di EPA/DHA sono approvati per la riduzione dei trigliceridi.</li>"
                "<li><strong>Statine</strong> — mirate principalmente al colesterolo LDL, "
                "offrono anche una moderata riduzione dei trigliceridi.</li>"
                "<li><strong>Niacina (vitamina B3)</strong> — riduce trigliceridi e LDL, ma "
                "gli effetti collaterali ne limitano l'impiego.</li>"
                "</ul>"
                "<p>I farmaci devono sempre essere avviati e monitorati dal medico. Effetti "
                "collaterali, interazioni e aggiustamenti posologici richiedono controlli "
                "regolari.</p>"
                "<p>Per livelli molto alti (&ge;500 mg/dL) può essere necessario un "
                "trattamento urgente per ridurre il rischio di pancreatite.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico",
            body_html=(
                "<p>Vi consigliamo di discutere i risultati dei trigliceridi con il medico "
                "se:</p>"
                "<ul>"
                "<li>Il livello dei trigliceridi supera i <strong>200 mg/dL</strong></li>"
                "<li>Esistono precedenti familiari di malattia cardiovascolare precoce</li>"
                "<li>Avete una diagnosi di diabete, obesità o sindrome metabolica</li>"
                "<li>Altri valori del profilo lipidico sono alterati (LDL alto, HDL basso)</li>"
                "<li>I trigliceridi superano i <strong>500 mg/dL</strong> — potrebbe essere "
                "necessaria una valutazione urgente per il rischio di pancreatite</li>"
                "</ul>"
                "<p>Un profilo lipidico almeno una volta l'anno è generalmente raccomandato. "
                "Se presentate fattori di rischio, il medico può suggerire controlli più "
                "frequenti.</p>"
                "<p>Ricordate che un singolo valore elevato non indica necessariamente un "
                "problema persistente, ma valori costantemente alti non devono essere "
                "ignorati.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya vi aiuta a comprendere i risultati",
            body_html=(
                "<p>Caricate i risultati delle analisi del sangue su "
                "<strong><a href=\"/analyze\">Norya</a></strong> e ricevete in pochi minuti "
                "un report sanitario strutturato e facile da comprendere. Norya confronta "
                "il vostro livello di trigliceridi e l'intero profilo lipidico con gli "
                "intervalli di riferimento e prepara un riepilogo chiaro e personalizzato.</p>"
                "<p>Questo report vi aiuta a prepararvi per la visita medica: potrete "
                "vedere rapidamente quali valori richiedono attenzione e quali domande "
                "porre. <a href=\"/analyze\">Iniziate l'analisi ora</a> e fate il primo "
                "passo per comprendere i vostri risultati.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il '
                'parere o la diagnosi medica.</strong> Discutete sempre i risultati con un '
                'professionista sanitario. <a href="/analyze">Inizia l\'analisi con '
                'Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="מהם טריגליצרידים ולמה הם חשובים?",
            body_html=(
                "<p>כאשר תוצאות בדיקת הדם שלכם מראות רמה גבוהה של "
                "<strong>טריגליצרידים</strong>, טבעי לתהות מה המשמעות. "
                "טריגליצרידים הם סוג השומן הנפוץ ביותר בזרם הדם ומשמשים כמאגר "
                "האנרגיה העיקרי של הגוף. עם זאת, רמות גבוהות באופן כרוני מהוות "
                "סמן סיכון מוכר למחלות לב וכלי דם.</p>"
                "<p>מדריך זה מסביר מהם טריגליצרידים, מהן רמות תקינות וחריגות, "
                "מה ההבדל בינם לבין כולסטרול ומה ניתן לעשות. מטרתנו אינה לאבחן — "
                "אלא לעזור לכם להגיע לפגישה עם הרופא מוכנים יותר.</p>"
                "<p>רמת הטריגליצרידים שלכם מושפעת מגורמים רבים: תזונה, פעילות "
                "גופנית, גנטיקה ומצבים רפואיים קיימים. הבנת גורמים אלה היא הצעד "
                "הראשון לשיחה משמעותית עם הרופא.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="מהם טריגליצרידים?",
            body_html=(
                "<p><strong>טריגליצרידים</strong> הם שומנים (ליפידים) המורכבים ממולקולת "
                "גליצרול המחוברת לשלוש שרשראות חומצות שומן. כאשר אוכלים, הגוף ממיר "
                "קלוריות שאינו זקוק להן מיידית לטריגליצרידים, המאוחסנים בתאי שומן. "
                "בין הארוחות, הורמונים משחררים טריגליצרידים אלו כדי לספק אנרגיה.</p>"
                "<p>זהו תהליך תקין ובריא. עם זאת, אם צורכים באופן קבוע יותר קלוריות "
                "מאשר שורפים — בעיקר מפחמימות מזוקקות וסוכר — רמות הטריגליצרידים "
                "בדם עלולות להישאר גבוהות באופן כרוני, מצב הנקרא "
                "<em>היפרטריגליצרידמיה</em>.</p>"
                "<p>טריגליצרידים נמדדים כחלק מ<strong>פרופיל שומנים</strong> סטנדרטי, "
                "יחד עם כולסטרול כללי, LDL ו-HDL. לקבלת תוצאות מדויקות נדרש צום של "
                "9–12 שעות לפני לקיחת הדם.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ייחוס של טריגליצרידים",
            body_html=(
                "<p>רמות טריגליצרידים מדווחות בדרך כלל ביחידות <strong>mg/dL</strong>. "
                "הטבלה הבאה מציגה את הסיווג המקובל למבוגרים:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קטגוריה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">רמה (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">תקין</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">גבולי</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">גבוה</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">גבוה מאוד</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>ערכי סף אלה מבוססים על הנחיות האגודה האמריקאית ללב (AHA) ו-ATP III. "
                "המעבדה שלכם עשויה להשתמש בטווחי ייחוס מעט שונים; השוו תמיד את "
                "תוצאותיכם לערכים המופיעים בדוח.</p>"
                "<p>רמות מעל <strong>500 mg/dL</strong> נחשבות גבוהות מאוד ונושאות סיכון "
                "משמעותי ל<strong>דלקת לבלב חריפה</strong>, המצריכה טיפול רפואי דחוף.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="סיבות לטריגליצרידים גבוהים",
            body_html=(
                "<p>רמות טריגליצרידים מוגברות יכולות לנבוע משילוב של גורמי אורח חיים, "
                "הרגלי תזונה ומצבים רפואיים בסיסיים:</p>"
                "<ul>"
                "<li><strong>תזונה עשירה בפחמימות מזוקקות וסוכר</strong> — לחם לבן, "
                "שתייה ממותקת, מאפים ומזון מעובד מגבירים ייצור טריגליצרידים.</li>"
                "<li><strong>השמנה ועודף משקל</strong> — במיוחד שומן בטני קשור חזק "
                "להיפרטריגליצרידמיה.</li>"
                "<li><strong>אורח חיים יושבני</strong> — חוסר פעילות גופנית סדירה "
                "מאט את חילוף החומרים של שומנים.</li>"
                "<li><strong>צריכת אלכוהול מופרזת</strong> — אלכוהול מעודד ישירות "
                "סינתזה של טריגליצרידים בכבד.</li>"
                "<li><strong>סוכרת סוג 2 ועמידות לאינסולין</strong> — בקרה לקויה על "
                "סוכר בדם מעלה רמות טריגליצרידים.</li>"
                "<li><strong>תת-פעילות של בלוטת התריס</strong> — בלוטת תריס שאינה "
                "פעילה דיה משבשת את חילוף החומרים השומני.</li>"
                "<li><strong>גורמים גנטיים</strong> — מצבים תורשתיים כמו "
                "היפרטריגליצרידמיה משפחתית יכולים לגרום לרמות מוגברות.</li>"
                "</ul>"
                "<p>תרופות מסוימות — חוסמי בטא, משתנים, קורטיקוסטרואידים וחלק "
                "מגלולות למניעת הריון — עלולות גם הן להעלות טריגליצרידים. ספרו "
                "תמיד לרופא על כל התרופות שאתם נוטלים.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="טריגליצרידים מול כולסטרול",
            body_html=(
                "<p>למרות ש<strong>טריגליצרידים</strong> ו<strong>כולסטרול</strong> "
                "שניהם שייכים למשפחת השומנים, הם ממלאים תפקידים שונים. טריגליצרידים "
                "מאחסנים אנרגיה עודפת לשימוש עתידי, בעוד כולסטרול נחוץ לבניית ממברנות "
                "תאים, ייצור הורמונים וסינתזה של ויטמין D.</p>"
                "<p>שניהם נמדדים בפרופיל שומנים סטנדרטי. <strong>כולסטרול LDL</strong> "
                "(\"הרע\") ו<strong>כולסטרול HDL</strong> (\"הטוב\") משקפים את בריאות "
                "העורקים, בעוד טריגליצרידים מהווים פרמטר סיכון קרדיווסקולרי עצמאי. "
                "השילוב של טריגליצרידים גבוהים ו-HDL נמוך מעורר דאגה במיוחד "
                "ואופייני ל<em>תסמונת מטבולית</em>.</p>"
                "<p>הערכת שני הסמנים יחד מאפשרת לרופא לקבל תמונה מקיפה יותר של "
                "פרופיל הסיכון הקרדיווסקולרי שלכם.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="סיכון קרדיווסקולרי וטריגליצרידים",
            body_html=(
                "<p>טריגליצרידים מוגברים תורמים ל<strong>טרשת עורקים</strong> — "
                "הצטברות משקעי שומן בדפנות העורקים — ובכך מגבירים את הסיכון להתקף "
                "לב ושבץ מוחי. מחקרים מראים שטריגליצרידים גבוהים, במיוחד בשילוב עם "
                "HDL נמוך ו-LDL גבוה, מעלים באופן משמעותי את הסיכון לאירועים "
                "קרדיווסקולריים.</p>"
                "<p>טריגליצרידים נישאים בדם בתוך חלקיקי <strong>VLDL</strong>. "
                "חלקיקים שיוריים אלה יכולים לחדור לדופן העורק ולהפעיל מפל דלקתי. "
                "בנוסף, רמות טריגליצרידים גבוהות מעודדות יצירת חלקיקי LDL קטנים "
                "וצפופים, הנחשבים אתרוגניים יותר.</p>"
                "<p>כאשר טריגליצרידים גבוהים מתקיימים יחד עם רכיבים נוספים של "
                "התסמונת המטבולית — השמנה בטנית, יתר לחץ דם, גלוקוז בצום מוגבר "
                "ו-HDL נמוך — הסיכון הקרדיווסקולרי הכולל עולה באופן ניכר.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="שינויים באורח חיים ובתזונה",
            body_html=(
                "<p>שינויי אורח חיים הם הגישה הראשונית להורדת טריגליצרידים. "
                "אסטרטגיות מבוססות ראיות כוללות:</p>"
                "<ul>"
                "<li><strong>הפחתת סוכר ופחמימות מזוקקות</strong> — החליפו לחם לבן, "
                "מאפים ושתייה ממותקת בדגנים מלאים.</li>"
                "<li><strong>צריכת חומצות שומן אומגה-3</strong> — דגים שמנים כמו "
                "סלמון, סרדינים ומקרל מוכחים כמורידי טריגליצרידים.</li>"
                "<li><strong>פעילות גופנית סדירה</strong> — לפחות 150 דקות "
                "שבועיות של פעילות אירובית מתונה יכולות להוריד טריגליצרידים "
                "באופן משמעותי.</li>"
                "<li><strong>שמירה על משקל תקין</strong> — אפילו ירידה של 5–10% "
                "במשקל יכולה לשפר את רמות הטריגליצרידים באופן ניכר.</li>"
                "<li><strong>הגבלת צריכת אלכוהול</strong> — הפחתה או הפסקה יכולה "
                "להיות יעילה מאוד.</li>"
                "</ul>"
                "<p>השפעות שינויים אלה מופיעות בדרך כלל תוך שבועות עד חודשים "
                "ספורים. הדיאטה הים-תיכונית — עשירה בשמן זית, ירקות, פירות, "
                "קטניות ודגנים מלאים — היא אחד מדפוסי התזונה הנחקרים ביותר "
                "לשיפור פרופיל השומנים.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="אפשרויות תרופתיות",
            body_html=(
                "<p>כאשר שינויי אורח חיים אינם מספיקים, הרופא עשוי להמליץ על "
                "טיפול תרופתי. קבוצות התרופות העיקריות להורדת טריגליצרידים כוללות:</p>"
                "<ul>"
                "<li><strong>פיבראטים</strong> — גמפיברוזיל ופנופיבראט יכולים "
                "להוריד טריגליצרידים ב-30–50%.</li>"
                "<li><strong>תוספי אומגה-3 במרשם</strong> — תכשירי EPA/DHA "
                "במינון גבוה מאושרים להורדת טריגליצרידים.</li>"
                "<li><strong>סטטינים</strong> — מכוונים בעיקר לכולסטרול LDL אך "
                "מספקים גם הורדה מתונה של טריגליצרידים.</li>"
                "<li><strong>ניאצין (ויטמין B3)</strong> — מוריד טריגליצרידים "
                "ו-LDL, אך תופעות הלוואי מגבילות את השימוש.</li>"
                "</ul>"
                "<p>תרופות צריכות תמיד להינתן ולהיות מנוטרות על ידי רופא. תופעות "
                "לוואי, אינטראקציות ושינויי מינון מחייבים מעקב סדיר.</p>"
                "<p>ברמות גבוהות מאוד (&ge;500 mg/dL) ייתכן שיידרש טיפול דחוף "
                "להפחתת הסיכון לדלקת לבלב.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא",
            body_html=(
                "<p>אנו ממליצים לדון בתוצאות הטריגליצרידים עם הרופא אם:</p>"
                "<ul>"
                "<li>רמת הטריגליצרידים <strong>מעל 200 mg/dL</strong></li>"
                "<li>קיים היסטוריה משפחתית של מחלת לב וכלי דם מוקדמת</li>"
                "<li>יש אבחנה של סוכרת, השמנה או תסמונת מטבולית</li>"
                "<li>ערכים נוספים בפרופיל השומנים חריגים (LDL גבוה, HDL נמוך)</li>"
                "<li>הטריגליצרידים <strong>מעל 500 mg/dL</strong> — ייתכן שנדרשת "
                "הערכה דחופה בשל סיכון לדלקת לבלב</li>"
                "</ul>"
                "<p>בדיקת פרופיל שומנים לפחות פעם בשנה מומלצת באופן כללי. "
                "אם קיימים גורמי סיכון, הרופא עשוי להציע בדיקות תכופות יותר.</p>"
                "<p>זכרו שערך גבוה בודד לא בהכרח מעיד על בעיה מתמשכת — אך "
                "ערכים גבוהים חוזרים לא צריכים להתעלם מהם.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד Norya עוזרת לכם להבין את תוצאות הטריגליצרידים",
            body_html=(
                "<p>העלו את תוצאות בדיקות הדם שלכם ל-"
                "<strong><a href=\"/analyze\">Norya</a></strong> וקבלו תוך דקות "
                "דוח בריאות מובנה וקל להבנה. Norya משווה את רמת הטריגליצרידים "
                "ואת פרופיל השומנים המלא שלכם לטווחי הייחוס ומכינה סיכום ברור "
                "ומותאם אישית.</p>"
                "<p>דוח זה עוזר לכם להתכונן לביקור אצל הרופא — תוכלו לראות "
                "במהירות אילו ערכים דורשים תשומת לב ואילו שאלות לשאול. "
                "<a href=\"/analyze\">התחילו את הניתוח עכשיו</a> ועשו את הצעד "
                "הראשון להבנת התוצאות שלכם.</p>"
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
            heading="ट्राइग्लिसराइड्स क्या हैं और ये क्यों महत्वपूर्ण हैं?",
            body_html=(
                "<p>जब आपकी ब्लड टेस्ट रिपोर्ट में <strong>ट्राइग्लिसराइड्स</strong> "
                "का स्तर बढ़ा हुआ दिखता है, तो स्वाभाविक रूप से आप जानना चाहेंगे कि "
                "इसका आपकी सेहत के लिए क्या मतलब है। ट्राइग्लिसराइड्स ख़ून में पाई "
                "जाने वाली सबसे आम प्रकार की वसा (फ़ैट) हैं और शरीर के प्रमुख ऊर्जा "
                "भंडार के रूप में काम करती हैं। हालाँकि, लंबे समय तक बढ़ा हुआ स्तर "
                "हृदय रोग का एक मान्यता प्राप्त जोखिम संकेतक है।</p>"
                "<p>यह गाइड बताती है कि ट्राइग्लिसराइड्स क्या हैं, सामान्य और "
                "असामान्य स्तर क्या होते हैं, ये कोलेस्ट्रॉल से कैसे अलग हैं और "
                "आप क्या कदम उठा सकते हैं। हमारा लक्ष्य निदान करना नहीं है — बल्कि "
                "आपको डॉक्टर की अपॉइंटमेंट के लिए बेहतर जानकारी के साथ तैयार "
                "करना है।</p>"
                "<p>आपका ट्राइग्लिसराइड स्तर कई कारकों से प्रभावित होता है — "
                "आहार, शारीरिक गतिविधि, आनुवंशिकी और अन्य स्वास्थ्य स्थितियाँ। "
                "इन कारकों को समझना आपके डॉक्टर के साथ सार्थक बातचीत की "
                "पहली सीढ़ी है।</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="ट्राइग्लिसराइड्स क्या हैं?",
            body_html=(
                "<p><strong>ट्राइग्लिसराइड्स</strong> एक प्रकार के लिपिड (वसा) "
                "हैं जो एक ग्लिसरॉल अणु से जुड़ी तीन फ़ैटी एसिड श्रृंखलाओं से बने "
                "होते हैं। जब आप खाना खाते हैं, तो शरीर उन कैलोरीज़ को जिनकी तुरंत "
                "ज़रूरत नहीं होती, ट्राइग्लिसराइड्स में बदलकर वसा कोशिकाओं में "
                "जमा कर लेता है। भोजन के बीच, हॉर्मोन इन संग्रहित "
                "ट्राइग्लिसराइड्स को ऊर्जा के लिए मुक्त करते हैं।</p>"
                "<p>यह एक सामान्य और स्वस्थ प्रक्रिया है। लेकिन अगर आप नियमित रूप "
                "से ज़रूरत से ज़्यादा कैलोरी लेते हैं — विशेषकर रिफ़ाइंड "
                "कार्बोहाइड्रेट और चीनी से — तो रक्त में ट्राइग्लिसराइड का स्तर "
                "लगातार बढ़ा रह सकता है, जिसे <em>हाइपरट्राइग्लिसरिडेमिया</em> "
                "कहते हैं।</p>"
                "<p>ट्राइग्लिसराइड्स को मानक <strong>लिपिड पैनल</strong> के हिस्से "
                "के रूप में मापा जाता है, जिसमें टोटल कोलेस्ट्रॉल, LDL और HDL "
                "कोलेस्ट्रॉल भी शामिल होते हैं। सटीक परिणामों के लिए ब्लड सैम्पल "
                "लेने से पहले 9–12 घंटे का उपवास आवश्यक होता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ट्राइग्लिसराइड रेफ़रेंस रेंज",
            body_html=(
                "<p>ट्राइग्लिसराइड के स्तर आमतौर पर <strong>mg/dL</strong> में "
                "रिपोर्ट किए जाते हैं। नीचे दी गई तालिका वयस्कों के लिए व्यापक "
                "रूप से स्वीकृत वर्गीकरण दर्शाती है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">श्रेणी</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">स्तर (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">सामान्य</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">सीमा रेखा पर उच्च</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">उच्च</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">बहुत उच्च</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>ये सीमाएँ अमेरिकन हार्ट एसोसिएशन (AHA) और ATP III दिशानिर्देशों "
                "पर आधारित हैं। आपकी लैब थोड़ी अलग रेफ़रेंस रेंज इस्तेमाल कर "
                "सकती है; हमेशा अपने रिजल्ट की तुलना रिपोर्ट में दिए गए मानों "
                "से करें।</p>"
                "<p><strong>500 mg/dL</strong> से ऊपर के स्तर बहुत अधिक माने जाते "
                "हैं और इनमें <strong>तीव्र अग्नाशयशोथ (पैंक्रियाटाइटिस)</strong> "
                "का गंभीर जोखिम होता है, जिसे तत्काल चिकित्सा ध्यान की "
                "आवश्यकता होती है।</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="उच्च ट्राइग्लिसराइड्स के कारण",
            body_html=(
                "<p>ट्राइग्लिसराइड का बढ़ा हुआ स्तर जीवनशैली, आहार और अंतर्निहित "
                "चिकित्सा स्थितियों के संयोजन से हो सकता है:</p>"
                "<ul>"
                "<li><strong>रिफ़ाइंड कार्बोहाइड्रेट और चीनी से भरपूर आहार</strong> "
                "— मैदा, मीठे पेय, मिठाइयाँ और प्रोसेस्ड फ़ूड ट्राइग्लिसराइड "
                "उत्पादन बढ़ाते हैं।</li>"
                "<li><strong>मोटापा और अधिक वज़न</strong> — विशेषकर पेट के आसपास "
                "की चर्बी का हाइपरट्राइग्लिसरिडेमिया से गहरा संबंध है।</li>"
                "<li><strong>गतिहीन जीवनशैली</strong> — नियमित शारीरिक गतिविधि की "
                "कमी वसा चयापचय को धीमा करती है।</li>"
                "<li><strong>अत्यधिक शराब सेवन</strong> — शराब लीवर में "
                "ट्राइग्लिसराइड के उत्पादन को सीधे बढ़ाती है।</li>"
                "<li><strong>टाइप 2 डायबिटीज़ और इंसुलिन रेज़िस्टेंस</strong> — "
                "अनियंत्रित ब्लड शुगर ट्राइग्लिसराइड बढ़ाता है।</li>"
                "<li><strong>हाइपोथायरॉइडिज़्म</strong> — कम सक्रिय थायरॉइड "
                "लिपिड मेटाबॉलिज़्म को बाधित करता है।</li>"
                "<li><strong>आनुवंशिक कारक</strong> — फ़ैमिलियल "
                "हाइपरट्राइग्लिसरिडेमिया जैसी वंशानुगत स्थितियाँ स्तर बढ़ा "
                "सकती हैं।</li>"
                "</ul>"
                "<p>कुछ दवाइयाँ — बीटा-ब्लॉकर्स, डाइयुरेटिक्स, कॉर्टिकोस्टेरॉइड्स "
                "और कुछ गर्भनिरोधक गोलियाँ — भी ट्राइग्लिसराइड बढ़ा सकती हैं। "
                "लिपिड रिजल्ट की समीक्षा करते समय अपने डॉक्टर को सभी दवाइयों "
                "के बारे में ज़रूर बताएँ।</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="ट्राइग्लिसराइड्स बनाम कोलेस्ट्रॉल",
            body_html=(
                "<p>यद्यपि <strong>ट्राइग्लिसराइड्स</strong> और "
                "<strong>कोलेस्ट्रॉल</strong> दोनों लिपिड परिवार से हैं, इनके "
                "कार्य अलग-अलग हैं। ट्राइग्लिसराइड्स अतिरिक्त ऊर्जा को भविष्य "
                "के उपयोग के लिए संग्रहित करते हैं, जबकि कोलेस्ट्रॉल कोशिका "
                "झिल्लियों के निर्माण, हॉर्मोन उत्पादन और विटामिन D के "
                "संश्लेषण में आवश्यक है।</p>"
                "<p>दोनों मानक लिपिड पैनल में मापे जाते हैं। <strong>LDL "
                "कोलेस्ट्रॉल</strong> (\"बुरा\") और <strong>HDL "
                "कोलेस्ट्रॉल</strong> (\"अच्छा\") धमनियों के स्वास्थ्य को "
                "दर्शाते हैं, जबकि ट्राइग्लिसराइड्स एक स्वतंत्र हृदय रोग "
                "जोखिम पैरामीटर हैं। उच्च ट्राइग्लिसराइड्स और कम HDL का "
                "संयोजन विशेष रूप से चिंताजनक है और <em>मेटाबोलिक सिंड्रोम</em> "
                "की पहचान है।</p>"
                "<p>दोनों मार्करों को मिलाकर देखना आपके डॉक्टर को आपके "
                "हृदय रोग जोखिम प्रोफ़ाइल की अधिक संपूर्ण तस्वीर देता है।</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="हृदय रोग का जोखिम और ट्राइग्लिसराइड्स",
            body_html=(
                "<p>बढ़े हुए ट्राइग्लिसराइड्स <strong>एथेरोस्क्लेरोसिस</strong> — "
                "धमनी की दीवारों में वसा जमाव — में योगदान करते हैं, जिससे "
                "हार्ट अटैक और स्ट्रोक का ख़तरा बढ़ता है। शोध दर्शाते हैं कि "
                "उच्च ट्राइग्लिसराइड्स, विशेषकर कम HDL और उच्च LDL के साथ, "
                "हृदय संबंधी घटनाओं का जोखिम काफ़ी बढ़ाते हैं।</p>"
                "<p>ट्राइग्लिसराइड्स रक्त में <strong>VLDL</strong> कणों में "
                "यात्रा करते हैं। ये अवशिष्ट कण धमनी की दीवार में प्रवेश कर "
                "सूजन प्रक्रिया शुरू कर सकते हैं। इसके अलावा, उच्च "
                "ट्राइग्लिसराइड स्तर छोटे और घने LDL कणों के निर्माण को "
                "बढ़ावा देते हैं, जो अधिक एथेरोजेनिक माने जाते हैं।</p>"
                "<p>जब उच्च ट्राइग्लिसराइड्स मेटाबोलिक सिंड्रोम के अन्य "
                "घटकों — पेट का मोटापा, उच्च रक्तचाप, बढ़ा हुआ फ़ास्टिंग "
                "ग्लूकोज़ और कम HDL — के साथ होते हैं, तो समग्र हृदय "
                "जोखिम काफ़ी बढ़ जाता है।</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="जीवनशैली और आहार में बदलाव",
            body_html=(
                "<p>ट्राइग्लिसराइड्स कम करने के लिए जीवनशैली में बदलाव "
                "पहली-पंक्ति का उपाय है। साक्ष्य-आधारित रणनीतियों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>चीनी और रिफ़ाइंड कार्बोहाइड्रेट कम करें</strong> — "
                "मैदा, मिठाइयाँ और मीठे पेय की जगह साबुत अनाज लें।</li>"
                "<li><strong>ओमेगा-3 फ़ैटी एसिड खाएँ</strong> — सैल्मन, "
                "सार्डिन और मैकरल जैसी तैलीय मछलियाँ ट्राइग्लिसराइड कम "
                "करने में कारगर हैं।</li>"
                "<li><strong>नियमित व्यायाम करें</strong> — सप्ताह में कम से कम "
                "150 मिनट मध्यम-तीव्रता की एरोबिक गतिविधि ट्राइग्लिसराइड्स "
                "में सार्थक कमी ला सकती है।</li>"
                "<li><strong>वज़न नियंत्रित करें</strong> — 5–10% वज़न कम "
                "करने से भी ट्राइग्लिसराइड में उल्लेखनीय सुधार हो सकता है।</li>"
                "<li><strong>शराब सीमित करें</strong> — शराब कम करना या "
                "छोड़ना बहुत प्रभावी हो सकता है।</li>"
                "</ul>"
                "<p>इन बदलावों का असर आमतौर पर कुछ हफ़्तों से कुछ महीनों "
                "में दिखता है। भूमध्यसागरीय आहार (Mediterranean diet) — "
                "जैतून का तेल, सब्ज़ियाँ, फल, दालें और साबुत अनाज से भरपूर — "
                "लिपिड प्रोफ़ाइल सुधारने के लिए सबसे अधिक अध्ययन किए गए "
                "आहार पैटर्न में से एक है।</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="दवाइयों के विकल्प",
            body_html=(
                "<p>जब जीवनशैली में बदलाव पर्याप्त नहीं होते, तो डॉक्टर "
                "दवाई लिख सकते हैं। ट्राइग्लिसराइड्स कम करने वाली प्रमुख "
                "दवा श्रेणियाँ हैं:</p>"
                "<ul>"
                "<li><strong>फ़ाइब्रेट्स</strong> — जेमफ़ाइब्रोज़िल और "
                "फ़ेनोफ़ाइब्रेट ट्राइग्लिसराइड्स को 30–50% तक कम कर "
                "सकते हैं।</li>"
                "<li><strong>प्रिस्क्रिप्शन ओमेगा-3 सप्लीमेंट</strong> — उच्च "
                "खुराक EPA/DHA तैयारियाँ ट्राइग्लिसराइड कम करने के लिए "
                "स्वीकृत हैं।</li>"
                "<li><strong>स्टैटिन</strong> — मुख्य रूप से LDL कोलेस्ट्रॉल "
                "लक्षित करते हैं लेकिन ट्राइग्लिसराइड्स में भी मध्यम "
                "कमी लाते हैं।</li>"
                "<li><strong>नियासिन (विटामिन B3)</strong> — ट्राइग्लिसराइड्स "
                "और LDL दोनों कम करता है, लेकिन दुष्प्रभावों के कारण "
                "इसका उपयोग सीमित है।</li>"
                "</ul>"
                "<p>दवाई हमेशा चिकित्सक की देखरेख में शुरू और जारी रखी "
                "जानी चाहिए। दुष्प्रभाव, ड्रग इंटरैक्शन और खुराक "
                "समायोजन के लिए नियमित फ़ॉलो-अप ज़रूरी है।</p>"
                "<p>बहुत उच्च स्तर (&ge;500 mg/dL) पर पैंक्रियाटाइटिस के "
                "जोखिम को कम करने के लिए तत्काल उपचार आवश्यक हो "
                "सकता है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें",
            body_html=(
                "<p>हम सलाह देते हैं कि निम्नलिखित स्थितियों में अपने "
                "ट्राइग्लिसराइड परिणाम डॉक्टर से ज़रूर चर्चा करें:</p>"
                "<ul>"
                "<li>ट्राइग्लिसराइड स्तर <strong>200 mg/dL से अधिक</strong> हो</li>"
                "<li>परिवार में कम उम्र में हृदय रोग का इतिहास हो</li>"
                "<li>डायबिटीज़, मोटापा या मेटाबोलिक सिंड्रोम का निदान हो</li>"
                "<li>लिपिड पैनल के अन्य मान भी असामान्य हों (उच्च LDL, "
                "कम HDL)</li>"
                "<li>ट्राइग्लिसराइड्स <strong>500 mg/dL से अधिक</strong> हों — "
                "पैंक्रियाटाइटिस के ख़तरे के कारण तत्काल मूल्यांकन ज़रूरी "
                "हो सकता है</li>"
                "</ul>"
                "<p>वयस्कों के लिए साल में कम से कम एक बार लिपिड पैनल "
                "कराने की सलाह दी जाती है। जोखिम कारक होने पर डॉक्टर अधिक "
                "बार जाँच सुझा सकते हैं।</p>"
                "<p>याद रखें, एक बार का बढ़ा हुआ मान हमेशा स्थायी समस्या "
                "नहीं दर्शाता — लेकिन बार-बार उच्च मान को नज़रअंदाज़ नहीं "
                "करना चाहिए।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके ट्राइग्लिसराइड परिणाम समझने में कैसे मदद करता है",
            body_html=(
                "<p>अपने ब्लड टेस्ट रिजल्ट "
                "<strong><a href=\"/analyze\">Norya</a></strong> पर अपलोड करें "
                "और कुछ ही मिनटों में एक संरचित, समझने में आसान स्वास्थ्य "
                "सारांश रिपोर्ट प्राप्त करें। Norya आपके ट्राइग्लिसराइड स्तर "
                "और पूरे लिपिड प्रोफ़ाइल की रेफ़रेंस रेंज से तुलना करता है और "
                "आपके लिए एक स्पष्ट सारांश तैयार करता है।</p>"
                "<p>यह रिपोर्ट आपको डॉक्टर की विज़िट के लिए तैयार करती है — "
                "आप जल्दी से देख सकते हैं कि कौन से मान ध्यान माँगते हैं और "
                "कौन से सवाल पूछने हैं। <a href=\"/analyze\">अभी विश्लेषण "
                "शुरू करें</a> और अपने परिणामों को समझने की दिशा में "
                "पहला कदम उठाएँ।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या '
                'निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा '
                'डॉक्टर से चर्चा करें। '
                '<a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="ما هي الدهون الثلاثية (الترايغليسيرايد) ولماذا هي مهمة؟",
            body_html=(
                "<p>عندما تُظهر نتائج فحص الدم ارتفاعاً في مستوى "
                "<strong>الدهون الثلاثية (الترايغليسيرايد)</strong>، من الطبيعي أن "
                "تتساءل عن تأثير ذلك على صحتك. الدهون الثلاثية هي أكثر أنواع "
                "الدهون شيوعاً في الدم وتعمل كمخزن الطاقة الرئيسي في الجسم. "
                "ومع ذلك، فإن المستويات المرتفعة بشكل مزمن تُعد مؤشر خطر معترفاً "
                "به لأمراض القلب والأوعية الدموية.</p>"
                "<p>يشرح هذا الدليل ماهية الدهون الثلاثية، وما هي المستويات الطبيعية "
                "وغير الطبيعية، وكيف تختلف عن الكوليسترول، وما الخطوات التي يمكنك "
                "اتخاذها. هدفنا ليس التشخيص — بل مساعدتك على الوصول إلى موعد "
                "الطبيب وأنت أكثر اطلاعاً.</p>"
                "<p>يتأثر مستوى الدهون الثلاثية لديك بعوامل عديدة: النظام الغذائي، "
                "النشاط البدني، الوراثة والحالات الصحية الأساسية. فهم هذه العوامل "
                "هو الخطوة الأولى نحو حوار بنّاء مع طبيبك.</p>"
            ),
        ),
        Section(
            id="what-are-triglycerides", level=2,
            heading="ما هي الدهون الثلاثية؟",
            body_html=(
                "<p><strong>الدهون الثلاثية</strong> هي نوع من الدهون (الليبيدات) "
                "تتكون من جزيء غليسيرول مرتبط بثلاث سلاسل من الأحماض الدهنية. "
                "عندما تأكل، يحوّل جسمك السعرات الحرارية التي لا يحتاجها فوراً إلى "
                "دهون ثلاثية، تُخزَّن في الخلايا الدهنية. بين الوجبات، تُطلق "
                "الهرمونات هذه الدهون المخزنة لتوفير الطاقة.</p>"
                "<p>هذه عملية طبيعية وصحية. ولكن إذا كنت تتناول باستمرار سعرات "
                "حرارية أكثر مما تحرق — خاصة من الكربوهيدرات المكررة والسكريات — "
                "فقد تبقى مستويات الدهون الثلاثية في الدم مرتفعة بشكل مزمن، وهي "
                "حالة تُعرف بـ <em>فرط ثلاثي غليسيريد الدم</em>.</p>"
                "<p>تُقاس الدهون الثلاثية كجزء من <strong>تحليل الدهون</strong> "
                "القياسي، إلى جانب الكوليسترول الكلي و LDL و HDL. للحصول على "
                "نتائج دقيقة، يُطلب عادةً صيام 9–12 ساعة قبل سحب الدم.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="نطاقات مرجعية للدهون الثلاثية",
            body_html=(
                "<p>تُبلَّغ مستويات الدهون الثلاثية عادةً بوحدة <strong>mg/dL</strong>. "
                "يوضح الجدول التالي التصنيف المقبول على نطاق واسع للبالغين:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الفئة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المستوى (mg/dL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">طبيعي</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 150</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">حدّي مرتفع</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150 – 199</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">مرتفع</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 499</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">مرتفع جداً</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 500</td>'
                "</tr></tbody></table>"
                "<p>تستند هذه العتبات إلى إرشادات جمعية القلب الأمريكية (AHA) "
                "و ATP III. قد يستخدم مختبرك نطاقات مرجعية مختلفة قليلاً؛ قارن "
                "دائماً نتائجك بالقيم المطبوعة في تقريرك.</p>"
                "<p>المستويات التي تتجاوز <strong>500 mg/dL</strong> تُعتبر مرتفعة "
                "جداً وتحمل خطراً كبيراً للإصابة بـ<strong>التهاب البنكرياس "
                "الحاد</strong>، مما يستدعي عناية طبية عاجلة.</p>"
            ),
        ),
        Section(
            id="high-triglycerides-causes", level=2,
            heading="أسباب ارتفاع الدهون الثلاثية",
            body_html=(
                "<p>يمكن أن ينتج ارتفاع الدهون الثلاثية عن مزيج من عوامل نمط "
                "الحياة والعادات الغذائية والحالات الطبية الكامنة:</p>"
                "<ul>"
                "<li><strong>نظام غذائي غني بالكربوهيدرات المكررة والسكر</strong> — "
                "الخبز الأبيض والمشروبات السكرية والمعجنات والأطعمة المصنعة تزيد "
                "إنتاج الدهون الثلاثية.</li>"
                "<li><strong>السمنة وزيادة الوزن</strong> — الدهون البطنية مرتبطة "
                "بقوة بفرط ثلاثي غليسيريد الدم.</li>"
                "<li><strong>نمط الحياة الخامل</strong> — قلة النشاط البدني المنتظم "
                "تبطئ أيض الدهون.</li>"
                "<li><strong>الإفراط في تناول الكحول</strong> — يُحفّز الكحول "
                "مباشرة تخليق الدهون الثلاثية في الكبد.</li>"
                "<li><strong>السكري من النوع الثاني ومقاومة الأنسولين</strong> — "
                "ضعف التحكم بسكر الدم يرفع الدهون الثلاثية.</li>"
                "<li><strong>قصور الغدة الدرقية</strong> — الغدة الدرقية غير "
                "النشطة تُخل بأيض الدهون.</li>"
                "<li><strong>عوامل وراثية</strong> — حالات موروثة مثل فرط ثلاثي "
                "غليسيريد الدم العائلي يمكن أن تسبب مستويات مرتفعة.</li>"
                "</ul>"
                "<p>بعض الأدوية — حاصرات بيتا ومدرات البول والكورتيكوستيرويدات "
                "وبعض حبوب منع الحمل — قد تزيد أيضاً من الدهون الثلاثية. أخبر "
                "طبيبك دائماً بجميع الأدوية التي تتناولها عند مراجعة نتائج "
                "الدهون.</p>"
            ),
        ),
        Section(
            id="triglycerides-vs-cholesterol", level=2,
            heading="الدهون الثلاثية مقابل الكوليسترول",
            body_html=(
                "<p>رغم أن كلاً من <strong>الدهون الثلاثية</strong> "
                "و<strong>الكوليسترول</strong> ينتميان إلى عائلة الدهون، إلا أنهما "
                "يؤديان وظائف مختلفة. تُخزّن الدهون الثلاثية الطاقة الزائدة "
                "للاستخدام اللاحق، بينما يُستخدم الكوليسترول لبناء أغشية الخلايا "
                "وإنتاج الهرمونات وتصنيع فيتامين D.</p>"
                "<p>يُقاس كلاهما في تحليل الدهون القياسي. يعكس "
                "<strong>كوليسترول LDL</strong> (\"السيئ\") و<strong>كوليسترول "
                "HDL</strong> (\"الجيد\") صحة الشرايين، بينما تُمثل الدهون "
                "الثلاثية مؤشراً مستقلاً لخطر القلب والأوعية. الجمع بين دهون "
                "ثلاثية مرتفعة و HDL منخفض مثير للقلق بشكل خاص ويُعد سمة "
                "مميزة لـ<em>المتلازمة الأيضية</em>.</p>"
                "<p>تقييم كلا المؤشرين معاً يمنح طبيبك صورة أشمل عن ملف المخاطر "
                "القلبية الوعائية لديك.</p>"
            ),
        ),
        Section(
            id="cardiovascular-risk", level=2,
            heading="خطر أمراض القلب والأوعية الدموية والدهون الثلاثية",
            body_html=(
                "<p>تُسهم الدهون الثلاثية المرتفعة في <strong>تصلب الشرايين</strong> "
                "— تراكم الرواسب الدهنية في جدران الشرايين — مما يزيد خطر النوبات "
                "القلبية والسكتات الدماغية. تُظهر الأبحاث أن الدهون الثلاثية "
                "المرتفعة، خاصة مع HDL منخفض و LDL مرتفع، ترفع بشكل ملحوظ "
                "خطر الأحداث القلبية الوعائية.</p>"
                "<p>تُنقل الدهون الثلاثية في الدم داخل جسيمات <strong>VLDL</strong>. "
                "يمكن لهذه الجسيمات المتبقية اختراق جدار الشريان وإطلاق سلسلة "
                "التهابية. علاوة على ذلك، تعزز المستويات المرتفعة تكوين جسيمات "
                "LDL الصغيرة والكثيفة التي تُعتبر أكثر تسبباً في التصلب.</p>"
                "<p>عندما تتواجد الدهون الثلاثية المرتفعة مع مكونات أخرى للمتلازمة "
                "الأيضية — السمنة البطنية وارتفاع ضغط الدم وارتفاع سكر الدم الصائم "
                "و HDL المنخفض — يرتفع الخطر القلبي الوعائي الإجمالي بشكل "
                "كبير.</p>"
            ),
        ),
        Section(
            id="lifestyle-and-diet", level=2,
            heading="تغييرات نمط الحياة والنظام الغذائي",
            body_html=(
                "<p>تُعد تعديلات نمط الحياة النهج الأول لخفض الدهون الثلاثية. "
                "تشمل الاستراتيجيات المبنية على الأدلة:</p>"
                "<ul>"
                "<li><strong>تقليل السكر والكربوهيدرات المكررة</strong> — استبدل "
                "الخبز الأبيض والمعجنات والمشروبات السكرية بالحبوب الكاملة.</li>"
                "<li><strong>تناول أحماض أوميغا-3 الدهنية</strong> — الأسماك "
                "الدهنية مثل السلمون والسردين والماكريل لها تأثير مُثبت في "
                "خفض الدهون الثلاثية.</li>"
                "<li><strong>ممارسة الرياضة بانتظام</strong> — 150 دقيقة على "
                "الأقل أسبوعياً من النشاط الهوائي المعتدل يمكن أن تخفض الدهون "
                "الثلاثية بشكل ملموس.</li>"
                "<li><strong>التحكم بالوزن</strong> — حتى فقدان 5–10% من الوزن "
                "يمكن أن يُحسّن مستويات الدهون الثلاثية بشكل ملحوظ.</li>"
                "<li><strong>تقليل الكحول</strong> — تقليله أو الامتناع عنه يمكن "
                "أن يكون فعالاً للغاية.</li>"
                "</ul>"
                "<p>تظهر آثار هذه التغييرات عادةً في غضون أسابيع إلى بضعة أشهر. "
                "حمية البحر الأبيض المتوسط — الغنية بزيت الزيتون والخضروات "
                "والفواكه والبقوليات والحبوب الكاملة — من أكثر الأنماط الغذائية "
                "المدروسة لتحسين ملف الدهون.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="الخيارات الدوائية",
            body_html=(
                "<p>عندما لا تكفي تغييرات نمط الحياة وحدها، قد يصف الطبيب "
                "أدوية. تشمل الفئات الدوائية الرئيسية لخفض الدهون الثلاثية:</p>"
                "<ul>"
                "<li><strong>الفايبرات</strong> — جمفيبروزيل وفينوفايبرات يمكن "
                "أن يخفضا الدهون الثلاثية بنسبة 30–50%.</li>"
                "<li><strong>مكملات أوميغا-3 بوصفة طبية</strong> — مستحضرات "
                "EPA/DHA بجرعات عالية معتمدة لخفض الدهون الثلاثية.</li>"
                "<li><strong>الستاتينات</strong> — تستهدف بشكل رئيسي كوليسترول "
                "LDL لكنها توفر أيضاً خفضاً معتدلاً للدهون الثلاثية.</li>"
                "<li><strong>النياسين (فيتامين B3)</strong> — يخفض الدهون "
                "الثلاثية و LDL، لكن الآثار الجانبية تحد من استخدامه.</li>"
                "</ul>"
                "<p>يجب دائماً بدء الأدوية ومراقبتها تحت إشراف الطبيب. الآثار "
                "الجانبية والتفاعلات الدوائية وتعديلات الجرعة تتطلب متابعة "
                "منتظمة.</p>"
                "<p>في حالة المستويات المرتفعة جداً (&ge;500 mg/dL)، قد يلزم "
                "علاج عاجل لتقليل خطر التهاب البنكرياس.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب",
            body_html=(
                "<p>ننصحك بمناقشة نتائج الدهون الثلاثية مع طبيبك إذا:</p>"
                "<ul>"
                "<li>كان مستوى الدهون الثلاثية <strong>أعلى من 200 mg/dL</strong></li>"
                "<li>وجد تاريخ عائلي لأمراض القلب المبكرة</li>"
                "<li>كان لديك تشخيص بالسكري أو السمنة أو المتلازمة الأيضية</li>"
                "<li>كانت قيم أخرى في تحليل الدهون غير طبيعية (LDL مرتفع، "
                "HDL منخفض)</li>"
                "<li>تجاوزت الدهون الثلاثية <strong>500 mg/dL</strong> — قد يلزم "
                "تقييم عاجل بسبب خطر التهاب البنكرياس</li>"
                "</ul>"
                "<p>يُوصى عموماً بإجراء تحليل دهون مرة واحدة على الأقل سنوياً. "
                "إذا كانت لديك عوامل خطر، فقد يقترح طبيبك فحوصات أكثر تكراراً.</p>"
                "<p>تذكر أن قراءة مرتفعة واحدة لا تعني بالضرورة وجود مشكلة دائمة "
                "— لكن القيم المرتفعة المتكررة لا ينبغي تجاهلها.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم نتائج الدهون الثلاثية",
            body_html=(
                "<p>حمّل نتائج فحص الدم على "
                "<strong><a href=\"/analyze\">Norya</a></strong> واحصل في "
                "غضون دقائق على تقرير صحي منظم وسهل الفهم. تقارن Norya "
                "مستوى الدهون الثلاثية وملف الدهون الكامل لديك بالنطاقات "
                "المرجعية وتُعد ملخصاً واضحاً ومخصصاً لك.</p>"
                "<p>يساعدك هذا التقرير على الاستعداد لزيارة الطبيب — يمكنك "
                "رؤية القيم التي تحتاج انتباهاً بسرعة ومعرفة الأسئلة التي "
                "يجب طرحها. <a href=\"/analyze\">ابدأ التحليل الآن</a> "
                "واتخذ الخطوة الأولى نحو فهم نتائجك.</p>"
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
def get_triglycerides_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_triglycerides_faq_schema_qa() -> dict:
    return {
        "tr": [
            {"question": "Trigliserid nedir?",
             "answer": "Trigliseridler, kanınızda dolaşan en yaygın yağ türüdür. Yediğiniz gıdalardaki yağlardan ve vücudunuzun karbonhidratlardan ürettiği yağ moleküllerinden oluşur; enerji deposu olarak görev yaparlar."},
            {"question": "Trigliserid kaç olmalı?",
             "answer": "Yetişkinlerde normal trigliserid düzeyi 150 mg/dL altıdır. 150–199 sınırda yüksek, 200–499 yüksek, 500 ve üzeri çok yüksek kabul edilir. Sonuçlarınızı laboratuvar raporunuzdaki referans aralıklarıyla karşılaştırın."},
            {"question": "Yüksek trigliserid kalp hastalığına yol açar mı?",
             "answer": "Evet, kronik olarak yüksek trigliserid düzeyleri ateroskleroz sürecine katkıda bulunarak kalp krizi ve inme riskini artırabilir. Özellikle düşük HDL kolesterol ile birlikte bulunduğunda risk belirgin şekilde artar."},
            {"question": "Trigliserid nasıl düşürülür?",
             "answer": "Şeker ve rafine karbonhidrat alımını azaltmak, omega-3 zengini balıklar tüketmek, düzenli egzersiz yapmak, kilo vermek ve alkol tüketimini sınırlamak trigliserid düşürmenin kanıta dayalı yollarıdır. Gerektiğinde hekiminiz ilaç tedavisi de önerebilir."},
        ],
        "en": [
            {"question": "What are triglycerides?",
             "answer": "Triglycerides are the most common type of fat in your blood. They are made from fats in your food and from carbohydrates your body converts into fat molecules, serving as your body's main energy reserve."},
            {"question": "What is a normal triglyceride level?",
             "answer": "For adults, a normal triglyceride level is below 150 mg/dL. Levels of 150–199 are borderline high, 200–499 are high, and 500 or above are very high. Always compare your results with the reference ranges on your lab report."},
            {"question": "Can high triglycerides cause heart disease?",
             "answer": "Yes, chronically elevated triglycerides contribute to atherosclerosis and increase the risk of heart attack and stroke. The risk is particularly significant when combined with low HDL cholesterol."},
            {"question": "How can I lower my triglycerides?",
             "answer": "Reducing sugar and refined carbohydrates, eating omega-3-rich fish, exercising regularly, losing weight, and limiting alcohol are evidence-based ways to lower triglycerides. Your doctor may also prescribe medication if needed."},
        ],
        "es": [
            {"question": "¿Qué son los triglicéridos?",
             "answer": "Los triglicéridos son el tipo de grasa más común en la sangre. Se forman a partir de las grasas de los alimentos y de los carbohidratos que el cuerpo convierte en grasa, y funcionan como la principal reserva de energía del organismo."},
            {"question": "¿Cuál es el nivel normal de triglicéridos?",
             "answer": "Para adultos, un nivel normal está por debajo de 150 mg/dL. Niveles de 150–199 son limítrofes, 200–499 son altos y 500 o más son muy altos. Compare siempre sus resultados con los rangos de referencia de su informe."},
            {"question": "¿Pueden los triglicéridos altos causar enfermedades cardíacas?",
             "answer": "Sí, los triglicéridos crónicamente elevados contribuyen a la aterosclerosis y aumentan el riesgo de infarto e ictus. El riesgo es especialmente significativo cuando se combinan con colesterol HDL bajo."},
            {"question": "¿Cómo puedo bajar mis triglicéridos?",
             "answer": "Reducir azúcar y carbohidratos refinados, consumir pescado rico en omega-3, hacer ejercicio regularmente, perder peso y limitar el alcohol son formas basadas en evidencia para reducir los triglicéridos. Su médico también puede recetar medicación si es necesario."},
        ],
        "de": [
            {"question": "Was sind Triglyceride?",
             "answer": "Triglyceride sind die häufigste Fettart im Blut. Sie entstehen aus Nahrungsfetten und aus Kohlenhydraten, die der Körper in Fett umwandelt, und dienen als wichtigster Energiespeicher."},
            {"question": "Welcher Triglycerid-Wert ist normal?",
             "answer": "Für Erwachsene gilt ein Triglycerid-Wert unter 150 mg/dL als normal. Werte von 150–199 sind grenzwertig, 200–499 hoch und ab 500 sehr hoch. Vergleichen Sie Ihre Ergebnisse immer mit den Referenzbereichen auf Ihrem Laborbericht."},
            {"question": "Können hohe Triglyceride Herzkrankheiten verursachen?",
             "answer": "Ja, chronisch erhöhte Triglyceride tragen zur Atherosklerose bei und erhöhen das Risiko für Herzinfarkt und Schlaganfall. Besonders hoch ist das Risiko in Kombination mit niedrigem HDL-Cholesterin."},
            {"question": "Wie kann ich meine Triglyceride senken?",
             "answer": "Zucker und raffinierte Kohlenhydrate reduzieren, Omega-3-reichen Fisch essen, regelmäßig bewegen, abnehmen und Alkohol einschränken — das sind evidenzbasierte Maßnahmen. Ihr Arzt kann bei Bedarf auch Medikamente verschreiben."},
        ],
        "fr": [
            {"question": "Que sont les triglycérides ?",
             "answer": "Les triglycérides sont le type de graisse le plus courant dans le sang. Ils proviennent des graisses alimentaires et des glucides convertis en graisse par l'organisme, et servent de principale réserve d'énergie."},
            {"question": "Quel est le taux normal de triglycérides ?",
             "answer": "Chez l'adulte, un taux inférieur à 150 mg/dL est normal. De 150 à 199 : limite haute ; de 200 à 499 : élevé ; 500 et plus : très élevé. Comparez toujours vos résultats avec les valeurs de référence de votre rapport."},
            {"question": "Les triglycérides élevés causent-ils des maladies cardiaques ?",
             "answer": "Oui, des triglycérides chroniquement élevés contribuent à l'athérosclérose et augmentent le risque d'infarctus et d'AVC. Le risque est particulièrement significatif lorsqu'ils sont associés à un HDL bas."},
            {"question": "Comment puis-je baisser mes triglycérides ?",
             "answer": "Réduire le sucre et les glucides raffinés, manger du poisson riche en oméga-3, faire de l'exercice régulièrement, perdre du poids et limiter l'alcool sont des moyens éprouvés. Votre médecin peut aussi prescrire un traitement si nécessaire."},
        ],
        "it": [
            {"question": "Cosa sono i trigliceridi?",
             "answer": "I trigliceridi sono il tipo di grasso più comune nel sangue. Si formano dai grassi alimentari e dai carboidrati convertiti in grasso dall'organismo, fungendo da principale riserva energetica."},
            {"question": "Qual è il livello normale dei trigliceridi?",
             "answer": "Per gli adulti, un livello inferiore a 150 mg/dL è normale. Da 150 a 199: limite alto; da 200 a 499: alto; 500 e oltre: molto alto. Confrontate sempre i risultati con gli intervalli di riferimento del referto."},
            {"question": "I trigliceridi alti possono causare malattie cardiache?",
             "answer": "Sì, trigliceridi cronicamente elevati contribuiscono all'aterosclerosi e aumentano il rischio di infarto e ictus. Il rischio è particolarmente significativo in presenza di HDL basso."},
            {"question": "Come posso abbassare i trigliceridi?",
             "answer": "Ridurre zucchero e carboidrati raffinati, mangiare pesce ricco di omega-3, fare esercizio regolare, perdere peso e limitare l'alcol sono metodi basati sulle evidenze. Il medico può anche prescrivere farmaci se necessario."},
        ],
        "he": [
            {"question": "מהם טריגליצרידים?",
             "answer": "טריגליצרידים הם סוג השומן הנפוץ ביותר בדם. הם נוצרים משומנים במזון ומפחמימות שהגוף ממיר לשומן, ומשמשים כמאגר האנרגיה העיקרי של הגוף."},
            {"question": "מהי רמת טריגליצרידים תקינה?",
             "answer": "למבוגרים, רמה מתחת ל-150 mg/dL נחשבת תקינה. 150–199: גבולית; 200–499: גבוהה; 500 ומעלה: גבוהה מאוד. השוו תמיד את תוצאותיכם לטווחי הייחוס בדוח."},
            {"question": "האם טריגליצרידים גבוהים גורמים למחלות לב?",
             "answer": "כן, טריגליצרידים גבוהים באופן כרוני תורמים לטרשת עורקים ומגבירים סיכון להתקף לב ושבץ. הסיכון גבוה במיוחד בשילוב עם HDL נמוך."},
            {"question": "כיצד ניתן להוריד טריגליצרידים?",
             "answer": "הפחתת סוכר ופחמימות מזוקקות, אכילת דגים עשירים באומגה-3, פעילות גופנית סדירה, ירידה במשקל והגבלת אלכוהול הם דרכים מבוססות ראיות. הרופא עשוי גם לרשום תרופות במידת הצורך."},
        ],
        "hi": [
            {"question": "ट्राइग्लिसराइड्स क्या हैं?",
             "answer": "ट्राइग्लिसराइड्स ख़ून में सबसे आम प्रकार की वसा हैं। ये भोजन में मौजूद वसा और शरीर द्वारा कार्बोहाइड्रेट से बनाई गई वसा से बनती हैं और शरीर के मुख्य ऊर्जा भंडार के रूप में काम करती हैं।"},
            {"question": "ट्राइग्लिसराइड का सामान्य स्तर क्या है?",
             "answer": "वयस्कों में 150 mg/dL से कम सामान्य माना जाता है। 150–199: सीमा रेखा पर; 200–499: उच्च; 500 या अधिक: बहुत उच्च। अपने रिजल्ट की तुलना हमेशा रिपोर्ट की रेफ़रेंस रेंज से करें।"},
            {"question": "क्या उच्च ट्राइग्लिसराइड्स हृदय रोग का कारण बन सकते हैं?",
             "answer": "हाँ, लंबे समय तक बढ़े हुए ट्राइग्लिसराइड्स एथेरोस्क्लेरोसिस में योगदान करते हैं और हार्ट अटैक व स्ट्रोक का ख़तरा बढ़ाते हैं। कम HDL के साथ जोखिम विशेष रूप से अधिक होता है।"},
            {"question": "ट्राइग्लिसराइड कैसे कम करें?",
             "answer": "चीनी और रिफ़ाइंड कार्बोहाइड्रेट कम करना, ओमेगा-3 से भरपूर मछली खाना, नियमित व्यायाम, वज़न कम करना और शराब सीमित करना साक्ष्य-आधारित उपाय हैं। ज़रूरत पड़ने पर डॉक्टर दवाई भी लिख सकते हैं।"},
        ],
        "ar": [
            {"question": "ما هي الدهون الثلاثية؟",
             "answer": "الدهون الثلاثية هي أكثر أنواع الدهون شيوعاً في الدم. تتكون من الدهون الغذائية ومن الكربوهيدرات التي يحولها الجسم إلى دهون، وتعمل كمخزن الطاقة الرئيسي للجسم."},
            {"question": "ما هو مستوى الدهون الثلاثية الطبيعي؟",
             "answer": "للبالغين، المستوى الطبيعي أقل من 150 mg/dL. من 150 إلى 199: حدّي؛ من 200 إلى 499: مرتفع؛ 500 فأكثر: مرتفع جداً. قارن دائماً نتائجك بالنطاقات المرجعية في تقريرك."},
            {"question": "هل تسبب الدهون الثلاثية المرتفعة أمراض القلب؟",
             "answer": "نعم، الدهون الثلاثية المرتفعة بشكل مزمن تسهم في تصلب الشرايين وتزيد خطر النوبات القلبية والسكتات الدماغية. الخطر كبير بشكل خاص مع انخفاض HDL."},
            {"question": "كيف يمكنني خفض الدهون الثلاثية؟",
             "answer": "تقليل السكر والكربوهيدرات المكررة، تناول الأسماك الغنية بأوميغا-3، ممارسة الرياضة بانتظام، إنقاص الوزن والحد من الكحول هي طرق مبنية على الأدلة. قد يصف الطبيب أيضاً أدوية عند الحاجة."},
        ],
    }
