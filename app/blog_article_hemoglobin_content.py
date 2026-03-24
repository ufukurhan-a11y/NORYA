# -*- coding: utf-8 -*-
"""
Hemoglobin blog article — full body content for all 9 languages.
Used by blog_i18n._article_hemoglobin().
Sections: intro, what-is-hemoglobin, normal-ranges, high-hemoglobin-causes,
low-hemoglobin-causes, symptoms, related-tests, when-to-see-doctor,
how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# TURKISH
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Hemoglobin nedir? Yüksek ve düşük hemoglobin ne anlama gelir?",
            body_html=(
                "<p><strong>Hemoglobin (Hb)</strong>, kırmızı kan hücrelerinde bulunan ve akciğerlerden dokulara oksijen taşıyan, "
                "dokulardan akciğerlere karbondioksit geri getiren demir içeren bir proteindir. Tam kan sayımı (CBC) testinin en temel "
                "parametrelerinden biri olan hemoglobin, vücudun oksijen taşıma kapasitesi hakkında doğrudan bilgi verir.</p>"
                "<p>Hemoglobin seviyesi düşük olduğunda <strong>anemi</strong> (kansızlık) tablosu ortaya çıkar; yüksek olduğunda ise "
                "kan yoğunluğu artarak dolaşım sorunlarına yol açabilir. Her iki durum da altta yatan önemli sağlık sorunlarına "
                "işaret edebilir ve doktor değerlendirmesi gerektirir.</p>"
                "<p>Bu rehber, hemoglobin değerlerinizi anlamanıza yardımcı olmak amacıyla hazırlanmıştır. "
                "Tıbbi tavsiye yerine geçmez&mdash;sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Hemoglobin nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Hemoglobin</strong>, her biri bir <em>hem</em> grubu (demir atomu içeren porfirin halkası) ve bir "
                "<em>globin</em> zincirinden oluşan dört alt birimli bir proteindir. Yetişkinlerde en yaygın formu <strong>HbA</strong> "
                "(iki alfa ve iki beta zinciri) olup toplam hemoglobinin yaklaşık %95&ndash;98&rsquo;ini oluşturur. "
                "Her hemoglobin molekülü dört oksijen molekülü bağlayabilir; bu sayede tek bir kırmızı kan hücresi "
                "yaklaşık 270&nbsp;milyon hemoglobin molekülü taşır.</p>"
                "<p>Hemoglobinin başlıca görevleri şunlardır:</p>"
                "<ul>"
                "<li><strong>Oksijen taşınması</strong> &ndash; akciğer alveollerinde oksijeni bağlar, dokulara ulaştığında serbest bırakır.</li>"
                "<li><strong>Karbondioksit taşınması</strong> &ndash; doku metabolizması sonucu oluşan CO₂&rsquo;nin yaklaşık %20&rsquo;sini akciğerlere geri taşır.</li>"
                "<li><strong>pH tamponlama</strong> &ndash; kan pH&rsquo;sının dar bir aralıkta (7,35&ndash;7,45) kalmasına yardımcı olur.</li>"
                "</ul>"
                "<p>Hemoglobin düzeyi, demir depolarına, B12 ve folat düzeylerine, kemik iliği fonksiyonuna ve eritropoietin (EPO) "
                "hormonuna bağlıdır. Bu nedenle hemoglobin değeri tek başına bir hastalık tanısı koymaz; "
                "ancak birçok durumun önemli bir göstergesidir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal hemoglobin değerleri",
            body_html=(
                "<p>Hemoglobin referans aralıkları yaş, cinsiyet ve laboratuvara göre değişebilir. "
                "Genel kabul gören yetişkin değerleri aşağıdaki tabloda özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkek (yetişkin)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadın (yetişkin)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hamile kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yenidoğan</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Çocuk (1&ndash;12 yaş)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,5 g/dL</td></tr>'
                "</tbody></table>"
                "<p>Yüksek rakımlı bölgelerde yaşayan kişilerde hemoglobin düzeyi fizyolojik olarak daha yüksek olabilir. "
                "Ayrıca dehidrasyon (su kaybı) gibi durumlar hemoglobin değerini yapay olarak yüksek gösterebilir. "
                "Bu nedenle tek bir değer üzerinden karar vermek yerine, klinik tabloyla birlikte değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Hemoglobin yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Yüksek hemoglobin (polisitemi)</strong>, kanın oksijen taşıma kapasitesinin artması veya plazma hacminin "
                "azalması sonucu ortaya çıkar. Başlıca nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Dehidrasyon</strong> &ndash; vücuttaki sıvı kaybı plazma hacmini azaltır ve hemoglobin konsantrasyonu "
                "göreceli olarak yükselir. Yeterli sıvı alımıyla düzelir.</li>"
                "<li><strong>Polisitemia vera</strong> &ndash; kemik iliğinde aşırı kırmızı kan hücresi üretimi ile karakterize "
                "bir miyeloproliferatif hastalıktır. JAK2 mutasyonu ile ilişkilidir.</li>"
                "<li><strong>Kronik akciğer hastalığı (KOAH, amfizem)</strong> &ndash; kronik hipoksi nedeniyle böbrekler daha fazla "
                "eritropoietin (EPO) salgılar ve kemik iliği daha fazla kırmızı kan hücresi üretir.</li>"
                "<li><strong>Yüksek rakımda yaşam</strong> &ndash; deniz seviyesine göre daha düşük oksijen basıncı, vücudu "
                "telafi mekanizması olarak daha fazla hemoglobin üretmeye yönlendirir.</li>"
                "<li><strong>Sigara kullanımı</strong> &ndash; karbonmonoksit hemoglobine bağlanarak fonksiyonel oksijen taşıma "
                "kapasitesini düşürür; vücut bunu telafi etmek için daha fazla hemoglobin üretir.</li>"
                "<li><strong>Konjenital kalp hastalıkları</strong> &ndash; siyanotik kalp defektleri kronik hipoksiye yol açar.</li>"
                "</ul>"
                "<p>Yüksek hemoglobin kan viskozitesini (akışkanlığını) artırarak tromboz (pıhtı oluşumu), baş ağrısı, "
                "baş dönmesi ve görme bozuklukları gibi semptomlara neden olabilir. Polisitemia vera gibi ciddi durumlarda "
                "flebotomi (kan alma) tedavisi uygulanabilir.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Hemoglobin düşüklüğünün nedenleri (anemi)",
            body_html=(
                "<p><strong>Düşük hemoglobin</strong> durumu <strong>anemi</strong> olarak adlandırılır ve dünya genelinde en yaygın "
                "kan bozukluğudur. Dünya Sağlık Örgütü&rsquo;ne göre dünya nüfusunun yaklaşık üçte biri anemiden etkilenmektedir. "
                "Başlıca nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Demir eksikliği anemisi</strong> &ndash; en yaygın anemi türüdür. Yetersiz demir alımı, "
                "emilim bozukluğu (çölyak hastalığı, mide ameliyatı) veya kronik kan kaybı (ağır adet kanaması, "
                "gastrointestinal kanama) sonucu gelişir. <a href=\"/tr/blog/iron-low-or-high\">Demir testi hakkında daha fazla bilgi</a>.</li>"
                "<li><strong>B12 vitamini ve folat eksikliği</strong> &ndash; megaloblastik anemiye neden olur. "
                "DNA sentezi bozulduğundan kırmızı kan hücreleri normalden büyük (makrositik) olur.</li>"
                "<li><strong>Kronik hastalık anemisi</strong> &ndash; kanser, böbrek yetmezliği, romatoid artrit gibi "
                "kronik inflamatuar durumlar eritropoietin üretimini ve demir metabolizmasını olumsuz etkiler.</li>"
                "<li><strong>Kan kaybı</strong> &ndash; akut (travma, ameliyat) veya kronik (GİS kanaması, hemoroid) kan kaybı.</li>"
                "<li><strong>Talasemi</strong> &ndash; globin zinciri üretiminde genetik bozukluk. Akdeniz ülkelerinde sık görülür.</li>"
                "<li><strong>Aplastik anemi</strong> &ndash; kemik iliğinin yeterli kan hücresi üretememesi.</li>"
                "<li><strong>Hemolitik anemiler</strong> &ndash; kırmızı kan hücrelerinin normalden hızlı yıkılması "
                "(otoimmün, orak hücreli anemi, G6PD eksikliği).</li>"
                "</ul>"
                "<p>Anemi tedavisi nedene göre belirlenir: demir eksikliğinde demir takviyesi, B12 eksikliğinde B12 enjeksiyonu, "
                "kronik hastalıkta altta yatan durumun kontrolü gibi. Şiddetli anemide kan transfüzyonu gerekebilir.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Yüksek ve düşük hemoglobin belirtileri",
            body_html=(
                "<p><strong>Düşük hemoglobin (anemi) belirtileri:</strong></p>"
                "<ul>"
                "<li>Halsizlik ve yorgunluk</li>"
                "<li>Soluk cilt, tırnak yatağı ve mukoza</li>"
                "<li>Nefes darlığı (özellikle efor sırasında)</li>"
                "<li>Baş dönmesi ve baş ağrısı</li>"
                "<li>Çarpıntı (taşikardi)</li>"
                "<li>El ve ayaklarda soğukluk</li>"
                "<li>Kırılgan tırnaklar, saç dökülmesi (demir eksikliğinde)</li>"
                "<li>Pika (buz, toprak gibi besin dışı maddeleri yeme isteği)</li>"
                "</ul>"
                "<p><strong>Yüksek hemoglobin belirtileri:</strong></p>"
                "<ul>"
                "<li>Baş ağrısı ve baş dönmesi</li>"
                "<li>Görme bozuklukları (bulanık görme)</li>"
                "<li>Yüzde kızarıklık</li>"
                "<li>Kaşıntı (özellikle sıcak duştan sonra, polisitemia vera&rsquo;da tipiktir)</li>"
                "<li>El ve ayak parmaklarında karıncalanma</li>"
                "<li>Tromboz riski artışı (derin ven trombozu, pulmoner emboli)</li>"
                "</ul>"
                "<p>Hafif anemi uzun süre belirti vermeyebilir; şiddetli anemi ise kalp yetmezliği riskini artırır. "
                "Yüksek hemoglobin de gözden kaçırılmamalıdır çünkü pıhtılaşma riskini önemli ölçüde yükseltir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlgili kan testleri",
            body_html=(
                "<p>Hemoglobin değeri tek başına değerlendirilmez; genellikle tam kan sayımının diğer parametreleriyle birlikte "
                "yorumlanır:</p>"
                "<ul>"
                "<li><strong>Hematokrit (Hct)</strong> &ndash; kanın kırmızı kan hücrelerinden oluşan yüzdesidir. "
                "Hemoglobinle paralel hareket eder. <a href=\"/tr/blog/hematocrit-high-or-low\">Hematokrit hakkında daha fazla bilgi</a>.</li>"
                "<li><strong>Kırmızı kan hücresi sayısı (RBC)</strong> &ndash; eritrosit sayısı.</li>"
                "<li><strong>MCV (Ortalama eritrosit hacmi)</strong> &ndash; kırmızı kan hücrelerinin büyüklüğü; "
                "mikrositik (küçük, demir eksikliği), normositik veya makrositik (büyük, B12 eksikliği) ayrımı yapılır.</li>"
                "<li><strong>MCH ve MCHC</strong> &ndash; her bir eritrositteki ortalama hemoglobin miktarı ve konsantrasyonu.</li>"
                "<li><strong>RDW</strong> &ndash; eritrosit dağılım genişliği; hücre boyutu çeşitliliğini gösterir.</li>"
                "<li><strong>Demir paneli</strong> &ndash; serum demiri, ferritin, TIBC (toplam demir bağlama kapasitesi), "
                "transferrin satürasyonu.</li>"
                "<li><strong>Retikülosit sayısı</strong> &ndash; kemik iliğinin yeni kırmızı kan hücresi üretim hızını gösterir.</li>"
                "<li><strong>B12 ve folat</strong> &ndash; megaloblastik anemi araştırmasında.</li>"
                "</ul>"
                "<p>Bu testlerin kombinasyonu, aneminin türünü ve nedenini belirlemeye yardımcı olur. "
                "Örneğin düşük hemoglobin + düşük MCV + düşük ferritin = demir eksikliği anemisi; "
                "düşük hemoglobin + yüksek MCV + düşük B12 = B12 eksikliği anemisi.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Doktora ne zaman başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda mutlaka bir hekime başvurun:</p>"
                "<ul>"
                "<li>Hemoglobin değeriniz referans aralığının altında veya üstünde çıktıysa</li>"
                "<li>Açıklanamayan yorgunluk, halsizlik, soluk cilt veya nefes darlığı yaşıyorsanız</li>"
                "<li>Ağır adet kanaması, dışkıda veya idrarda kan fark ettiyseniz</li>"
                "<li>Ani ve şiddetli baş ağrısı, görme bozukluğu veya göğüs ağrısı varsa</li>"
                "<li>Bilinen bir kronik hastalığınız varsa ve hemoglobin değerinizde belirgin değişim olduysa</li>"
                "</ul>"
                "<p><strong>Acil durum:</strong> Hemoglobin 7&nbsp;g/dL&rsquo;nin altına düştüğünde veya aktif kanama varsa "
                "acil müdahale gerekebilir. Aşırı yüksek hemoglobin (>20&nbsp;g/dL) de pıhtı riski nedeniyle acil değerlendirme gerektirir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;doktor ziyaretinize hazırlanmanıza yardımcı olur. "
                "Kan tahlili raporunuzu <a href=\"/analyze\">noryaai.com/analyze</a> sayfasına yükleyin; "
                "yapay zekâ motorumuz hemoglobin, hematokrit, MCV ve diğer biyobelirteçleri otomatik olarak çıkarır, "
                "referans aralıklarıyla karşılaştırır ve anlaşılır bir rapor oluşturur.</p>"
                "<p>İster ilk kez kan testi sonuçlarınızı inceliyor olun, ister kronik bir durumu takip ediyor olun, "
                "Norya sonuçlarınızı yapılandırılmış bir şekilde düzenleyerek doktorunuzla görüşmenize hazırlar. "
                "Abonelik seçenekleri için <a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                'Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. '
                '<a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# ENGLISH
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Hemoglobin levels: what high or low hemoglobin means",
            body_html=(
                "<p><strong>Hemoglobin (Hb)</strong> is the iron-containing protein inside red blood cells responsible for carrying "
                "oxygen from the lungs to every tissue in the body and returning carbon dioxide back to the lungs for exhalation. "
                "It is one of the most fundamental parameters measured in a <strong>complete blood count (CBC)</strong> and provides "
                "a direct indicator of the blood&rsquo;s oxygen-carrying capacity.</p>"
                "<p>When hemoglobin is too low, the condition is called <strong>anemia</strong>&mdash;a global health concern affecting "
                "roughly one-third of the world&rsquo;s population according to the WHO. When hemoglobin is too high, blood viscosity "
                "increases and circulation problems can arise. Both situations may signal underlying medical conditions that require "
                "investigation.</p>"
                "<p>This guide is educational and does not replace medical advice. Always discuss your hemoglobin results with a "
                "qualified healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="What is hemoglobin and why does it matter?",
            body_html=(
                "<p><strong>Hemoglobin</strong> is a tetrameric protein composed of four subunits, each containing a <em>heme</em> group "
                "(a porphyrin ring with a central iron atom) and a <em>globin</em> chain. In adults, the predominant form is "
                "<strong>HbA</strong> (two alpha and two beta chains), making up about 95&ndash;98% of total hemoglobin. Each hemoglobin "
                "molecule can bind up to four oxygen molecules, and a single red blood cell contains roughly 270&nbsp;million "
                "hemoglobin molecules.</p>"
                "<p>Key functions of hemoglobin include:</p>"
                "<ul>"
                "<li><strong>Oxygen transport</strong> &ndash; binds O₂ in the lung alveoli and releases it in peripheral tissues "
                "where oxygen tension is low.</li>"
                "<li><strong>Carbon dioxide transport</strong> &ndash; carries approximately 20% of CO₂ produced by tissue metabolism "
                "back to the lungs as carbaminohemoglobin.</li>"
                "<li><strong>pH buffering</strong> &ndash; helps maintain blood pH within the narrow range of 7.35&ndash;7.45.</li>"
                "</ul>"
                "<p>Hemoglobin levels depend on iron stores, vitamin B12 and folate status, bone marrow function, and erythropoietin "
                "(EPO) production by the kidneys. A single hemoglobin value does not diagnose a disease, but it is a critical "
                "screening tool for a wide range of conditions.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal hemoglobin ranges",
            body_html=(
                "<p>Reference ranges vary by age, sex, and laboratory. The following table summarizes widely accepted adult values:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adult men</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adult women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Pregnant women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Newborns</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Children (1&ndash;12 years)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.5 g/dL</td></tr>'
                "</tbody></table>"
                "<p>People living at high altitudes may have physiologically higher hemoglobin levels as a compensatory response "
                "to lower atmospheric oxygen pressure. Dehydration can also falsely elevate hemoglobin by reducing plasma volume. "
                "A single result should always be interpreted in clinical context.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Causes of high hemoglobin",
            body_html=(
                "<p><strong>Elevated hemoglobin (polycythemia)</strong> occurs when the blood&rsquo;s oxygen-carrying capacity increases "
                "or when plasma volume decreases. The main causes include:</p>"
                "<ul>"
                "<li><strong>Dehydration</strong> &ndash; reduced plasma volume concentrates red blood cells, causing a relative rise in "
                "hemoglobin. This resolves with adequate fluid intake.</li>"
                "<li><strong>Polycythemia vera</strong> &ndash; a myeloproliferative neoplasm characterized by uncontrolled red blood cell "
                "production in the bone marrow. It is associated with the <em>JAK2 V617F</em> mutation in over 95% of cases.</li>"
                "<li><strong>Chronic lung disease (COPD, emphysema)</strong> &ndash; chronic hypoxia stimulates the kidneys to release more "
                "erythropoietin (EPO), driving increased red blood cell production.</li>"
                "<li><strong>Living at high altitude</strong> &ndash; lower atmospheric O₂ pressure triggers a compensatory increase in "
                "hemoglobin synthesis.</li>"
                "<li><strong>Smoking</strong> &ndash; carbon monoxide binds hemoglobin (forming carboxyhemoglobin) with 200&times; the "
                "affinity of oxygen, reducing functional oxygen delivery. The body compensates by producing more hemoglobin.</li>"
                "<li><strong>Congenital heart disease</strong> &ndash; cyanotic heart defects lead to chronic hypoxia and secondary "
                "polycythemia.</li>"
                "</ul>"
                "<p>Elevated hemoglobin increases blood viscosity, which raises the risk of thrombosis (blood clots), stroke, and "
                "heart attack. In polycythemia vera, therapeutic phlebotomy (controlled blood removal) is a mainstay of treatment "
                "to keep hematocrit below target levels. "
                "<a href=\"/en/blog/hematocrit-high-or-low\">Learn more about hematocrit</a>.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Causes of low hemoglobin (anemia)",
            body_html=(
                "<p><strong>Low hemoglobin</strong> defines <strong>anemia</strong>, the most common blood disorder worldwide. "
                "The causes are broadly classified by the mechanism:</p>"
                "<ul>"
                "<li><strong>Iron deficiency anemia</strong> &ndash; the most prevalent form globally. Results from inadequate dietary "
                "iron, impaired absorption (celiac disease, gastric surgery), or chronic blood loss (heavy menstruation, "
                "gastrointestinal bleeding). <a href=\"/en/blog/iron-low-or-high\">Read more about iron tests</a>.</li>"
                "<li><strong>Vitamin B12 and folate deficiency</strong> &ndash; causes megaloblastic anemia where red blood cells are "
                "abnormally large (macrocytic) due to impaired DNA synthesis.</li>"
                "<li><strong>Anemia of chronic disease</strong> &ndash; associated with cancer, chronic kidney disease, rheumatoid "
                "arthritis, and other inflammatory conditions that impair erythropoietin production and iron metabolism.</li>"
                "<li><strong>Blood loss</strong> &ndash; acute (trauma, surgery) or chronic (GI bleeding, hemorrhoids).</li>"
                "<li><strong>Thalassemia</strong> &ndash; inherited disorders of globin chain synthesis, particularly common in "
                "Mediterranean, Middle Eastern, and Southeast Asian populations.</li>"
                "<li><strong>Aplastic anemia</strong> &ndash; bone marrow failure resulting in reduced production of all blood cell lines.</li>"
                "<li><strong>Hemolytic anemias</strong> &ndash; accelerated destruction of red blood cells (autoimmune, sickle cell "
                "disease, G6PD deficiency).</li>"
                "</ul>"
                "<p>Treatment depends on the underlying cause: iron supplementation for iron deficiency, B12 injections for B12 "
                "deficiency, erythropoiesis-stimulating agents for chronic kidney disease, and blood transfusion for severe anemia. "
                "Identifying and correcting the root cause is essential for long-term management.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of high and low hemoglobin",
            body_html=(
                "<p><strong>Low hemoglobin (anemia) symptoms:</strong></p>"
                "<ul>"
                "<li>Fatigue and weakness</li>"
                "<li>Pale skin, nail beds, and mucous membranes</li>"
                "<li>Shortness of breath, especially on exertion</li>"
                "<li>Dizziness and headache</li>"
                "<li>Rapid heartbeat (tachycardia) and palpitations</li>"
                "<li>Cold hands and feet</li>"
                "<li>Brittle nails and hair loss (particularly in iron deficiency)</li>"
                "<li>Pica (craving non-food items such as ice or dirt)</li>"
                "</ul>"
                "<p><strong>High hemoglobin symptoms:</strong></p>"
                "<ul>"
                "<li>Headache and dizziness</li>"
                "<li>Blurred or impaired vision</li>"
                "<li>Facial flushing (ruddy complexion)</li>"
                "<li>Itching, especially after a warm shower (classic in polycythemia vera)</li>"
                "<li>Tingling in fingers and toes</li>"
                "<li>Increased risk of thrombotic events (deep vein thrombosis, pulmonary embolism, stroke)</li>"
                "</ul>"
                "<p>Mild anemia may be asymptomatic for extended periods; severe anemia (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) can lead to "
                "heart failure if untreated. High hemoglobin should not be ignored either, as it significantly elevates the risk of "
                "life-threatening blood clots.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related blood tests",
            body_html=(
                "<p>Hemoglobin is never interpreted in isolation. It is evaluated alongside other complete blood count parameters:</p>"
                "<ul>"
                "<li><strong>Hematocrit (Hct)</strong> &ndash; the percentage of blood volume occupied by red blood cells; moves in "
                "parallel with hemoglobin. <a href=\"/en/blog/hematocrit-high-or-low\">Learn more about hematocrit</a>.</li>"
                "<li><strong>Red blood cell count (RBC)</strong> &ndash; the total number of erythrocytes per unit volume.</li>"
                "<li><strong>MCV (Mean Corpuscular Volume)</strong> &ndash; average size of red blood cells; helps classify anemia as "
                "microcytic (low MCV, e.g. iron deficiency), normocytic, or macrocytic (high MCV, e.g. B12 deficiency).</li>"
                "<li><strong>MCH and MCHC</strong> &ndash; mean hemoglobin content and concentration per red blood cell.</li>"
                "<li><strong>RDW (Red Cell Distribution Width)</strong> &ndash; measures variability in red blood cell size.</li>"
                "<li><strong>Iron panel</strong> &ndash; serum iron, ferritin, TIBC (total iron-binding capacity), transferrin "
                "saturation. <a href=\"/en/blog/iron-low-or-high\">Read more about iron</a>.</li>"
                "<li><strong>Reticulocyte count</strong> &ndash; indicates how fast the bone marrow is producing new red blood cells.</li>"
                "<li><strong>Vitamin B12 and folate</strong> &ndash; evaluated when macrocytic anemia is suspected.</li>"
                "</ul>"
                "<p>The combination of these tests helps pinpoint the type and cause of anemia. For example, low hemoglobin + low "
                "MCV + low ferritin strongly suggests iron deficiency anemia, while low hemoglobin + high MCV + low B12 points to "
                "vitamin B12 deficiency.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult a healthcare professional if:</p>"
                "<ul>"
                "<li>Your hemoglobin result is above or below the reference range</li>"
                "<li>You experience unexplained fatigue, weakness, pale skin, or shortness of breath</li>"
                "<li>You notice heavy menstrual bleeding, blood in stool, or blood in urine</li>"
                "<li>You develop sudden severe headache, vision changes, or chest pain</li>"
                "<li>You have a known chronic condition and notice a significant change in hemoglobin</li>"
                "</ul>"
                "<p><strong>Emergency:</strong> Hemoglobin below 7&nbsp;g/dL or active hemorrhage may require emergency intervention "
                "including blood transfusion. Extremely high hemoglobin (&gt;20&nbsp;g/dL) also warrants urgent evaluation due to "
                "thrombosis risk.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare for your doctor visit. Upload your blood test report at "
                "<a href=\"/analyze\">noryaai.com/analyze</a> and our AI engine automatically extracts hemoglobin, hematocrit, MCV, "
                "and other biomarkers, compares them against reference ranges, and generates a clear, structured report.</p>"
                "<p>Whether you are reviewing blood test results for the first time or monitoring a chronic condition, "
                "Norya organises your results to help you have a more informed conversation with your doctor. "
                "For subscription options, visit our <a href=\"/pricing\">pricing page</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace medical advice or diagnosis.</strong> '
                'Always discuss your results with a healthcare professional. '
                '<a href="/analyze">Start analysis with Norya</a></p>'
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
            heading="Hemoglobina: qué significa tenerla alta o baja",
            body_html=(
                "<p>La <strong>hemoglobina (Hb)</strong> es la proteína rica en hierro presente en los glóbulos rojos que transporta "
                "oxígeno desde los pulmones a todos los tejidos del cuerpo y devuelve dióxido de carbono a los pulmones para su "
                "exhalación. Es uno de los parámetros más importantes del <strong>hemograma completo (CBC)</strong>.</p>"
                "<p>Cuando la hemoglobina es demasiado baja se produce <strong>anemia</strong>, una condición que afecta a cerca de "
                "un tercio de la población mundial según la OMS. Cuando es demasiado alta, la viscosidad de la sangre aumenta y "
                "pueden surgir problemas circulatorios. Ambas situaciones requieren evaluación médica.</p>"
                "<p>Esta guía es educativa y no sustituye el consejo médico profesional.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="¿Qué es la hemoglobina y por qué es importante?",
            body_html=(
                "<p>La <strong>hemoglobina</strong> es una proteína tetramérica formada por cuatro subunidades, cada una con un grupo "
                "<em>hemo</em> (anillo de porfirina con un átomo de hierro central) y una cadena de <em>globina</em>. En adultos, "
                "la forma predominante es la <strong>HbA</strong> (dos cadenas alfa y dos beta), que representa el 95&ndash;98% "
                "del total. Cada molécula de hemoglobina puede unir hasta cuatro moléculas de oxígeno.</p>"
                "<p>Funciones principales:</p>"
                "<ul>"
                "<li><strong>Transporte de oxígeno</strong> &ndash; capta O₂ en los alvéolos pulmonares y lo libera en los tejidos.</li>"
                "<li><strong>Transporte de CO₂</strong> &ndash; lleva aproximadamente el 20% del CO₂ producido por el metabolismo tisular.</li>"
                "<li><strong>Amortiguación del pH</strong> &ndash; contribuye a mantener el pH sanguíneo entre 7,35 y 7,45.</li>"
                "</ul>"
                "<p>Los niveles de hemoglobina dependen de las reservas de hierro, la vitamina B12, el ácido fólico, la función de "
                "la médula ósea y la producción de eritropoyetina (EPO) por los riñones.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de hemoglobina",
            body_html=(
                "<p>Los intervalos de referencia varían según la edad, el sexo y el laboratorio:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres adultos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres adultas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Embarazadas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Recién nacidos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0 g/dL</td></tr>'
                "</tbody></table>"
                "<p>La deshidratación puede elevar artificialmente la hemoglobina al reducir el volumen plasmático. "
                "Las personas que viven en altitudes elevadas suelen tener valores más altos como mecanismo compensatorio.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Causas de hemoglobina alta",
            body_html=(
                "<p><strong>La hemoglobina elevada (policitemia)</strong> puede deberse a:</p>"
                "<ul>"
                "<li><strong>Deshidratación</strong> &ndash; reduce el volumen plasmático y concentra los glóbulos rojos.</li>"
                "<li><strong>Policitemia vera</strong> &ndash; neoplasia mieloproliferativa con producción descontrolada de eritrocitos, "
                "asociada a la mutación <em>JAK2 V617F</em>.</li>"
                "<li><strong>Enfermedad pulmonar crónica (EPOC)</strong> &ndash; la hipoxia crónica estimula la producción de EPO.</li>"
                "<li><strong>Vida en altitudes elevadas</strong> &ndash; menor presión de O₂ atmosférico.</li>"
                "<li><strong>Tabaquismo</strong> &ndash; el monóxido de carbono ocupa los sitios de unión del O₂ en la hemoglobina.</li>"
                "<li><strong>Cardiopatías congénitas cianóticas</strong> &ndash; generan hipoxia crónica.</li>"
                "</ul>"
                "<p>La hemoglobina alta aumenta la viscosidad sanguínea y el riesgo de trombosis, ictus e infarto de miocardio.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Causas de hemoglobina baja (anemia)",
            body_html=(
                "<p>La <strong>anemia</strong> es el trastorno sanguíneo más común en el mundo. Sus causas principales incluyen:</p>"
                "<ul>"
                "<li><strong>Anemia ferropénica</strong> &ndash; la más frecuente; por ingesta insuficiente de hierro, malabsorción "
                "o pérdida crónica de sangre.</li>"
                "<li><strong>Déficit de B12 y ácido fólico</strong> &ndash; provoca anemia megaloblástica con eritrocitos grandes.</li>"
                "<li><strong>Anemia de enfermedad crónica</strong> &ndash; asociada a cáncer, insuficiencia renal o enfermedades inflamatorias.</li>"
                "<li><strong>Pérdida de sangre</strong> &ndash; aguda (traumatismo) o crónica (hemorragia digestiva).</li>"
                "<li><strong>Talasemia</strong> &ndash; trastorno hereditario de la síntesis de globina.</li>"
                "<li><strong>Anemia aplásica</strong> &ndash; fallo de la médula ósea.</li>"
                "<li><strong>Anemias hemolíticas</strong> &ndash; destrucción acelerada de glóbulos rojos.</li>"
                "</ul>"
                "<p>El tratamiento depende de la causa: suplementos de hierro, inyecciones de B12, agentes estimulantes de la "
                "eritropoyesis o transfusión sanguínea en casos graves.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de hemoglobina alta y baja",
            body_html=(
                "<p><strong>Síntomas de anemia:</strong> fatiga, palidez, disnea de esfuerzo, mareos, taquicardia, manos y pies "
                "fríos, uñas frágiles y caída del cabello. En déficit de hierro puede aparecer pica (deseo de ingerir hielo o tierra).</p>"
                "<p><strong>Síntomas de hemoglobina alta:</strong> cefalea, visión borrosa, rubor facial, prurito (especialmente tras "
                "la ducha caliente en la policitemia vera), hormigueo en las extremidades y aumento del riesgo trombótico.</p>"
                "<p>La anemia leve puede ser asintomática durante largos períodos. La anemia grave (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) "
                "puede causar insuficiencia cardíaca si no se trata.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p>La hemoglobina se interpreta junto con otros parámetros del hemograma:</p>"
                "<ul>"
                "<li><strong>Hematocrito</strong> &ndash; porcentaje de sangre ocupado por glóbulos rojos.</li>"
                "<li><strong>Recuento de eritrocitos (RBC)</strong></li>"
                "<li><strong>VCM (Volumen Corpuscular Medio)</strong> &ndash; clasifica la anemia en microcítica, normocítica o macrocítica.</li>"
                "<li><strong>HCM y CHCM</strong> &ndash; hemoglobina media y concentración por eritrocito.</li>"
                "<li><strong>ADE (Ancho de Distribución Eritrocitaria)</strong></li>"
                "<li><strong>Panel de hierro</strong> &ndash; hierro sérico, ferritina, TIBC, saturación de transferrina.</li>"
                "<li><strong>Reticulocitos</strong> &ndash; velocidad de producción de eritrocitos nuevos.</li>"
                "<li><strong>B12 y ácido fólico</strong></li>"
                "</ul>"
                "<p>Por ejemplo: hemoglobina baja + VCM bajo + ferritina baja = anemia ferropénica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Consulte a un profesional sanitario si su hemoglobina está fuera del rango de referencia, si presenta fatiga "
                "inexplicable, palidez, disnea, sangrado abundante o cambios visuales súbitos.</p>"
                "<p><strong>Urgencia:</strong> hemoglobina por debajo de 7&nbsp;g/dL o hemorragia activa requieren atención de "
                "emergencia. La hemoglobina muy elevada (&gt;20&nbsp;g/dL) también necesita evaluación urgente.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo ayuda Norya",
            body_html=(
                "<p>Norya no diagnostica&mdash;le ayuda a prepararse para su cita médica. Suba su análisis de sangre en "
                "<a href=\"/analyze\">noryaai.com/analyze</a> y nuestro motor de IA extraerá hemoglobina, hematocrito, VCM y otros "
                "biomarcadores, los comparará con los rangos de referencia y generará un informe claro y estructurado.</p>"
                "<p>Visite nuestra <a href=\"/pricing\">página de precios</a> para las opciones de suscripción.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> '
                'Consulte siempre sus resultados con un profesional sanitario. '
                '<a href="/analyze">Iniciar análisis con Norya</a></p>'
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
            heading="Hämoglobin: Was bedeuten hohe oder niedrige Werte?",
            body_html=(
                "<p><strong>Hämoglobin (Hb)</strong> ist das eisenhaltige Protein in den roten Blutkörperchen, das Sauerstoff von "
                "der Lunge zu allen Geweben transportiert und Kohlendioxid zurück zur Lunge bringt. Es ist einer der wichtigsten "
                "Parameter im <strong>großen Blutbild (CBC)</strong>.</p>"
                "<p>Zu niedriges Hämoglobin wird als <strong>Anämie</strong> (Blutarmut) bezeichnet und betrifft laut WHO etwa ein "
                "Drittel der Weltbevölkerung. Zu hohes Hämoglobin erhöht die Blutviskosität und kann Durchblutungsstörungen "
                "verursachen. Beide Zustände erfordern ärztliche Abklärung.</p>"
                "<p>Dieser Leitfaden dient der Information und ersetzt keine ärztliche Beratung.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Was ist Hämoglobin und warum ist es wichtig?",
            body_html=(
                "<p><strong>Hämoglobin</strong> ist ein tetrameres Protein aus vier Untereinheiten mit jeweils einer <em>Häm</em>-Gruppe "
                "(Porphyrinring mit zentralem Eisenatom) und einer <em>Globin</em>-Kette. Bei Erwachsenen ist <strong>HbA</strong> "
                "(zwei Alpha- und zwei Betaketten) die Hauptform und macht 95&ndash;98&nbsp;% des Gesamthämoglobins aus.</p>"
                "<p>Hauptfunktionen:</p>"
                "<ul>"
                "<li><strong>Sauerstofftransport</strong> &ndash; bindet O₂ in den Lungenalveolen und gibt es im Gewebe frei.</li>"
                "<li><strong>CO₂-Transport</strong> &ndash; transportiert ca. 20&nbsp;% des Kohlendioxids zurück zur Lunge.</li>"
                "<li><strong>pH-Pufferung</strong> &ndash; hält den Blut-pH im Bereich 7,35&ndash;7,45.</li>"
                "</ul>"
                "<p>Der Hämoglobinspiegel hängt von den Eisenspeichern, Vitamin B12, Folsäure, der Knochenmarkfunktion und der "
                "Erythropoietin-Produktion (EPO) der Nieren ab.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Hämoglobin-Werte",
            body_html=(
                "<p>Referenzbereiche variieren nach Alter, Geschlecht und Labor:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frauen</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Schwangere</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neugeborene</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0 g/dL</td></tr>'
                "</tbody></table>"
                "<p>Dehydration kann den Hämoglobinwert falsch erhöhen. Bewohner von Hochgebirgsregionen haben physiologisch "
                "höhere Werte als Kompensation für den niedrigeren Sauerstoffdruck.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Ursachen für erhöhtes Hämoglobin",
            body_html=(
                "<p><strong>Erhöhtes Hämoglobin (Polyzythämie)</strong> kann folgende Ursachen haben:</p>"
                "<ul>"
                "<li><strong>Dehydration</strong> &ndash; verringert das Plasmavolumen und konzentriert die Erythrozyten.</li>"
                "<li><strong>Polycythaemia vera</strong> &ndash; myeloproliferative Neoplasie mit unkontrollierter Erythrozyten-Produktion, "
                "assoziiert mit der <em>JAK2</em>-Mutation.</li>"
                "<li><strong>Chronische Lungenerkrankung (COPD)</strong> &ndash; chronische Hypoxie stimuliert die EPO-Produktion.</li>"
                "<li><strong>Leben in großer Höhe</strong> &ndash; kompensatorische Steigerung der Hämoglobinsynthese.</li>"
                "<li><strong>Rauchen</strong> &ndash; Kohlenmonoxid blockiert Sauerstoff-Bindungsstellen am Hämoglobin.</li>"
                "</ul>"
                "<p>Erhöhtes Hämoglobin steigert die Blutviskosität und damit das Risiko für Thrombosen, Schlaganfall und Herzinfarkt.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Ursachen für niedriges Hämoglobin (Anämie)",
            body_html=(
                "<p><strong>Anämie</strong> ist die weltweit häufigste Bluterkrankung. Hauptursachen:</p>"
                "<ul>"
                "<li><strong>Eisenmangelanämie</strong> &ndash; häufigste Form; durch unzureichende Eisenaufnahme, Malabsorption "
                "oder chronischen Blutverlust.</li>"
                "<li><strong>Vitamin-B12- und Folsäuremangel</strong> &ndash; verursacht megaloblastische Anämie mit vergrößerten Erythrozyten.</li>"
                "<li><strong>Anämie chronischer Erkrankungen</strong> &ndash; bei Krebs, chronischer Niereninsuffizienz oder Entzündungen.</li>"
                "<li><strong>Blutverlust</strong> &ndash; akut (Trauma) oder chronisch (gastrointestinale Blutung).</li>"
                "<li><strong>Thalassämie</strong> &ndash; erbliche Störung der Globinkettensynthese.</li>"
                "<li><strong>Aplastische Anämie</strong> &ndash; Knochenmarkversagen.</li>"
                "<li><strong>Hämolytische Anämien</strong> &ndash; beschleunigter Abbau der Erythrozyten.</li>"
                "</ul>"
                "<p>Die Therapie richtet sich nach der Ursache: Eisensupplementation, B12-Injektionen, EPO-stimulierende Mittel "
                "oder Bluttransfusion bei schwerer Anämie.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome bei hohem und niedrigem Hämoglobin",
            body_html=(
                "<p><strong>Anämie-Symptome:</strong> Müdigkeit, Blässe, Belastungsdyspnoe, Schwindel, Tachykardie, kalte Hände "
                "und Füße, brüchige Nägel und Haarausfall. Bei Eisenmangel kann Pica auftreten.</p>"
                "<p><strong>Symptome bei hohem Hämoglobin:</strong> Kopfschmerzen, verschwommenes Sehen, Gesichtsrötung, Juckreiz "
                "(besonders nach warmem Duschen bei Polycythaemia vera), Kribbeln in den Extremitäten und erhöhtes Thromboserisiko.</p>"
                "<p>Eine leichte Anämie kann lange symptomfrei bleiben; schwere Anämie (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) kann "
                "ohne Behandlung zu Herzinsuffizienz führen.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Verwandte Laboruntersuchungen",
            body_html=(
                "<p>Hämoglobin wird zusammen mit anderen Blutbildparametern beurteilt:</p>"
                "<ul>"
                "<li><strong>Hämatokrit</strong> &ndash; Anteil der Erythrozyten am Blutvolumen.</li>"
                "<li><strong>Erythrozytenzahl (RBC)</strong></li>"
                "<li><strong>MCV</strong> &ndash; mittleres Erythrozytenvolumen; klassifiziert Anämie als mikro-, normo- oder makrozytär.</li>"
                "<li><strong>MCH und MCHC</strong></li>"
                "<li><strong>RDW</strong> &ndash; Erythrozytenverteilungsbreite.</li>"
                "<li><strong>Eisenstatus</strong> &ndash; Serumeisen, Ferritin, Transferrinsättigung, TIBC.</li>"
                "<li><strong>Retikulozyten</strong> &ndash; Maß für die Neubildungsrate der Erythrozyten.</li>"
                "<li><strong>B12 und Folsäure</strong></li>"
                "</ul>"
                "<p>Beispiel: niedriges Hb + niedriges MCV + niedriges Ferritin = Eisenmangelanämie.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann zum Arzt?",
            body_html=(
                "<p>Suchen Sie einen Arzt auf, wenn Ihr Hämoglobin außerhalb des Referenzbereichs liegt, bei unerklärlicher "
                "Müdigkeit, Blässe, Atemnot, starken Blutungen oder plötzlichen Sehstörungen.</p>"
                "<p><strong>Notfall:</strong> Hämoglobin unter 7&nbsp;g/dL oder aktive Blutung erfordern eine Notfallbehandlung. "
                "Extrem hohes Hämoglobin (&gt;20&nbsp;g/dL) erfordert ebenfalls eine dringende Abklärung.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya hilft",
            body_html=(
                "<p>Norya stellt keine Diagnosen&mdash;wir helfen Ihnen, sich auf Ihren Arztbesuch vorzubereiten. "
                "Laden Sie Ihren Blutbefund unter <a href=\"/analyze\">noryaai.com/analyze</a> hoch. Unsere KI extrahiert Hämoglobin, "
                "Hämatokrit, MCV und weitere Biomarker, vergleicht sie mit Referenzbereichen und erstellt einen verständlichen Bericht.</p>"
                "<p>Abonnement-Optionen finden Sie auf unserer <a href=\"/pricing\">Preisseite</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> '
                'Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. '
                '<a href="/analyze">Analyse mit Norya starten</a></p>'
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
            heading="Hémoglobine : que signifie un taux élevé ou bas ?",
            body_html=(
                "<p>L&rsquo;<strong>hémoglobine (Hb)</strong> est la protéine riche en fer des globules rouges qui transporte "
                "l&rsquo;oxygène des poumons vers tous les tissus et ramène le dioxyde de carbone aux poumons. "
                "C&rsquo;est l&rsquo;un des paramètres les plus importants de la <strong>numération formule sanguine (NFS)</strong>.</p>"
                "<p>Un taux trop bas s&rsquo;appelle <strong>anémie</strong> et touche environ un tiers de la population mondiale "
                "selon l&rsquo;OMS. Un taux trop élevé augmente la viscosité du sang et peut entraîner des troubles circulatoires. "
                "Les deux situations justifient une évaluation médicale.</p>"
                "<p>Ce guide est informatif et ne remplace pas un avis médical.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Qu&rsquo;est-ce que l&rsquo;hémoglobine ?",
            body_html=(
                "<p>L&rsquo;<strong>hémoglobine</strong> est une protéine tétramérique composée de quatre sous-unités, chacune "
                "contenant un groupe <em>hème</em> (anneau porphyrine avec un atome de fer) et une chaîne de <em>globine</em>. "
                "Chez l&rsquo;adulte, la forme prédominante est l&rsquo;<strong>HbA</strong> (deux chaînes alpha et deux bêta).</p>"
                "<p>Fonctions clés :</p>"
                "<ul>"
                "<li><strong>Transport d&rsquo;O₂</strong> &ndash; capte l&rsquo;oxygène dans les alvéoles et le libère dans les tissus.</li>"
                "<li><strong>Transport de CO₂</strong> &ndash; environ 20&nbsp;% du CO₂ métabolique est transporté par l&rsquo;hémoglobine.</li>"
                "<li><strong>Tampon pH</strong> &ndash; maintient le pH sanguin entre 7,35 et 7,45.</li>"
                "</ul>"
                "<p>Le taux d&rsquo;hémoglobine dépend des réserves en fer, de la vitamine B12, de l&rsquo;acide folique, "
                "de la moelle osseuse et de l&rsquo;érythropoïétine (EPO) rénale.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de l&rsquo;hémoglobine",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervalle normal</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes adultes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes adultes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes enceintes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Nouveau-nés</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0 g/dL</td></tr>'
                "</tbody></table>"
                "<p>La déshydratation peut faussement élever l&rsquo;hémoglobine. Les résidents d&rsquo;altitude élevée ont "
                "physiologiquement des valeurs plus hautes.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Causes d&rsquo;une hémoglobine élevée",
            body_html=(
                "<p><strong>L&rsquo;hémoglobine élevée (polyglobulie)</strong> peut résulter de :</p>"
                "<ul>"
                "<li><strong>Déshydratation</strong> &ndash; concentration relative des globules rouges.</li>"
                "<li><strong>Polyglobulie de Vaquez</strong> &ndash; néoplasie myéloproliférative avec mutation <em>JAK2</em>.</li>"
                "<li><strong>Maladies pulmonaires chroniques (BPCO)</strong> &ndash; hypoxie chronique stimulant l&rsquo;EPO.</li>"
                "<li><strong>Vie en haute altitude</strong> &ndash; compensation de la pression d&rsquo;O₂ réduite.</li>"
                "<li><strong>Tabagisme</strong> &ndash; le CO se lie à l&rsquo;hémoglobine avec une affinité 200&times; supérieure à l&rsquo;O₂.</li>"
                "</ul>"
                "<p>Une hémoglobine élevée augmente la viscosité sanguine et le risque de thrombose, d&rsquo;AVC et d&rsquo;infarctus.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Causes d&rsquo;une hémoglobine basse (anémie)",
            body_html=(
                "<p>L&rsquo;<strong>anémie</strong> est le trouble sanguin le plus répandu au monde. Causes principales :</p>"
                "<ul>"
                "<li><strong>Anémie ferriprive</strong> &ndash; la plus fréquente ; apport insuffisant, malabsorption ou perte de sang chronique.</li>"
                "<li><strong>Carence en B12 et acide folique</strong> &ndash; anémie mégaloblastique avec érythrocytes macrocytaires.</li>"
                "<li><strong>Anémie des maladies chroniques</strong> &ndash; cancer, insuffisance rénale, inflammations.</li>"
                "<li><strong>Perte de sang</strong> &ndash; aiguë ou chronique.</li>"
                "<li><strong>Thalassémie</strong> &ndash; trouble génétique de la synthèse de la globine.</li>"
                "<li><strong>Anémie aplasique</strong> &ndash; insuffisance médullaire.</li>"
                "<li><strong>Anémies hémolytiques</strong> &ndash; destruction accélérée des globules rouges.</li>"
                "</ul>"
                "<p>Le traitement dépend de la cause : supplémentation en fer, injections de B12, agents stimulant l&rsquo;érythropoïèse "
                "ou transfusion en cas d&rsquo;anémie sévère.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d&rsquo;hémoglobine haute et basse",
            body_html=(
                "<p><strong>Symptômes d&rsquo;anémie :</strong> fatigue, pâleur, dyspnée d&rsquo;effort, vertiges, tachycardie, "
                "mains et pieds froids, ongles cassants, chute de cheveux.</p>"
                "<p><strong>Symptômes d&rsquo;hémoglobine élevée :</strong> céphalées, vision floue, rougeur du visage, prurit "
                "(surtout après une douche chaude), paresthésies et risque thrombotique accru.</p>"
                "<p>L&rsquo;anémie légère peut rester asymptomatique. L&rsquo;anémie sévère (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) "
                "peut conduire à l&rsquo;insuffisance cardiaque.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens associés",
            body_html=(
                "<p>L&rsquo;hémoglobine est interprétée avec d&rsquo;autres paramètres de la NFS :</p>"
                "<ul>"
                "<li><strong>Hématocrite</strong></li>"
                "<li><strong>Numération des globules rouges</strong></li>"
                "<li><strong>VGM</strong> &ndash; classifie l&rsquo;anémie en microcytaire, normocytaire ou macrocytaire.</li>"
                "<li><strong>TCMH et CCMH</strong></li>"
                "<li><strong>IDR (Indice de Distribution des Rouges)</strong></li>"
                "<li><strong>Bilan martial</strong> &ndash; fer sérique, ferritine, CTF, saturation de la transferrine.</li>"
                "<li><strong>Réticulocytes</strong></li>"
                "<li><strong>B12 et folates</strong></li>"
                "</ul>"
                "<p>Exemple : Hb basse + VGM bas + ferritine basse = anémie ferriprive.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez si votre hémoglobine est hors des valeurs de référence, en cas de fatigue inexpliquée, pâleur, "
                "dyspnée, saignements abondants ou troubles visuels soudains.</p>"
                "<p><strong>Urgence :</strong> Hb inférieure à 7&nbsp;g/dL ou hémorragie active nécessitent une prise en charge urgente.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya peut vous aider",
            body_html=(
                "<p>Norya ne pose pas de diagnostic&mdash;nous vous aidons à préparer votre rendez-vous médical. "
                "Téléchargez votre bilan sanguin sur <a href=\"/analyze\">noryaai.com/analyze</a> et notre IA extraira hémoglobine, "
                "hématocrite, VGM et autres biomarqueurs pour générer un rapport clair et structuré.</p>"
                "<p>Découvrez nos options sur notre <a href=\"/pricing\">page tarifs</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> '
                'Discutez toujours de vos résultats avec un professionnel de santé. '
                '<a href="/analyze">Commencer l\'analyse avec Norya</a></p>'
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
            heading="Emoglobina: cosa significa un valore alto o basso",
            body_html=(
                "<p>L&rsquo;<strong>emoglobina (Hb)</strong> è la proteina contenente ferro nei globuli rossi che trasporta ossigeno "
                "dai polmoni a tutti i tessuti e riporta anidride carbonica ai polmoni. È uno dei parametri principali "
                "dell&rsquo;<strong>emocromo completo (CBC)</strong>.</p>"
                "<p>Quando l&rsquo;emoglobina è troppo bassa si parla di <strong>anemia</strong>, che colpisce circa un terzo della "
                "popolazione mondiale secondo l&rsquo;OMS. Quando è troppo alta, la viscosità del sangue aumenta con possibili "
                "problemi circolatori. Entrambe le condizioni richiedono una valutazione medica.</p>"
                "<p>Questa guida è informativa e non sostituisce il parere medico.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="Cos&rsquo;è l&rsquo;emoglobina e perché è importante?",
            body_html=(
                "<p>L&rsquo;<strong>emoglobina</strong> è una proteina tetramerica con quattro subunità, ciascuna contenente un gruppo "
                "<em>eme</em> (anello porfirinico con un atomo di ferro) e una catena di <em>globina</em>. Nell&rsquo;adulto, la forma "
                "principale è l&rsquo;<strong>HbA</strong> (due catene alfa e due beta), pari al 95&ndash;98% del totale.</p>"
                "<p>Funzioni principali:</p>"
                "<ul>"
                "<li><strong>Trasporto di O₂</strong> &ndash; lega l&rsquo;ossigeno negli alveoli e lo rilascia nei tessuti.</li>"
                "<li><strong>Trasporto di CO₂</strong> &ndash; trasporta circa il 20% della CO₂ metabolica.</li>"
                "<li><strong>Tampone del pH</strong> &ndash; mantiene il pH ematico tra 7,35 e 7,45.</li>"
                "</ul>"
                "<p>I livelli di emoglobina dipendono dalle riserve di ferro, dalla vitamina B12, dall&rsquo;acido folico, "
                "dal midollo osseo e dalla produzione di eritropoietina (EPO) da parte dei reni.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali dell&rsquo;emoglobina",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini adulti</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13,5&ndash;17,5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne adulte</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,0&ndash;16,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Gravidanza</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11,0&ndash;14,0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neonati</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14,0&ndash;24,0 g/dL</td></tr>'
                "</tbody></table>"
                "<p>La disidratazione può elevare artificialmente l&rsquo;emoglobina. Chi vive in alta quota ha fisiologicamente "
                "valori più elevati.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="Cause di emoglobina alta",
            body_html=(
                "<p><strong>L&rsquo;emoglobina elevata (policitemia)</strong> può derivare da:</p>"
                "<ul>"
                "<li><strong>Disidratazione</strong> &ndash; concentrazione relativa dei globuli rossi.</li>"
                "<li><strong>Policitemia vera</strong> &ndash; neoplasia mieloproliferativa con mutazione <em>JAK2</em>.</li>"
                "<li><strong>Malattie polmonari croniche (BPCO)</strong> &ndash; ipossia cronica che stimola l&rsquo;EPO.</li>"
                "<li><strong>Vita in alta quota</strong> &ndash; compenso alla ridotta pressione di O₂.</li>"
                "<li><strong>Fumo</strong> &ndash; il CO si lega all&rsquo;emoglobina con affinità 200&times; superiore all&rsquo;O₂.</li>"
                "</ul>"
                "<p>L&rsquo;emoglobina alta aumenta la viscosità ematica e il rischio di trombosi, ictus e infarto.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="Cause di emoglobina bassa (anemia)",
            body_html=(
                "<p>L&rsquo;<strong>anemia</strong> è il disturbo ematologico più comune al mondo. Cause principali:</p>"
                "<ul>"
                "<li><strong>Anemia sideropenica</strong> &ndash; la più frequente; apporto insufficiente, malassorbimento o perdita ematica cronica.</li>"
                "<li><strong>Carenza di B12 e acido folico</strong> &ndash; anemia megaloblastica con eritrociti macrocitici.</li>"
                "<li><strong>Anemia delle malattie croniche</strong> &ndash; cancro, insufficienza renale, infiammazioni.</li>"
                "<li><strong>Perdita di sangue</strong> &ndash; acuta o cronica.</li>"
                "<li><strong>Talassemia</strong> &ndash; difetto genetico della sintesi della globina.</li>"
                "<li><strong>Anemia aplastica</strong> &ndash; insufficienza midollare.</li>"
                "<li><strong>Anemie emolitiche</strong> &ndash; distruzione accelerata dei globuli rossi.</li>"
                "</ul>"
                "<p>La terapia dipende dalla causa: ferro, B12, agenti stimolanti l&rsquo;eritropoiesi o trasfusione nei casi gravi.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi di emoglobina alta e bassa",
            body_html=(
                "<p><strong>Sintomi di anemia:</strong> affaticamento, pallore, dispnea da sforzo, vertigini, tachicardia, "
                "mani e piedi freddi, unghie fragili, caduta dei capelli.</p>"
                "<p><strong>Sintomi di emoglobina alta:</strong> cefalea, visione offuscata, rossore facciale, prurito "
                "(specie dopo doccia calda nella policitemia vera), parestesie e rischio trombotico aumentato.</p>"
                "<p>L&rsquo;anemia lieve può restare asintomatica a lungo. L&rsquo;anemia grave (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) "
                "può portare a insufficienza cardiaca.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p>L&rsquo;emoglobina va interpretata con gli altri parametri dell&rsquo;emocromo:</p>"
                "<ul>"
                "<li><strong>Ematocrito</strong></li>"
                "<li><strong>Conta dei globuli rossi (RBC)</strong></li>"
                "<li><strong>MCV</strong> &ndash; classifica l&rsquo;anemia in microcitica, normocitica o macrocitica.</li>"
                "<li><strong>MCH e MCHC</strong></li>"
                "<li><strong>RDW</strong></li>"
                "<li><strong>Assetto marziale</strong> &ndash; sideremia, ferritina, TIBC, saturazione della transferrina.</li>"
                "<li><strong>Reticolociti</strong></li>"
                "<li><strong>B12 e folati</strong></li>"
                "</ul>"
                "<p>Esempio: Hb bassa + MCV basso + ferritina bassa = anemia sideropenica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico",
            body_html=(
                "<p>Rivolgetevi al medico se l&rsquo;emoglobina è fuori dall&rsquo;intervallo di riferimento, in caso di "
                "affaticamento inspiegabile, pallore, dispnea, sanguinamenti abbondanti o disturbi visivi improvvisi.</p>"
                "<p><strong>Emergenza:</strong> Hb inferiore a 7&nbsp;g/dL o emorragia attiva richiedono intervento urgente.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya può aiutarti",
            body_html=(
                "<p>Norya non formula diagnosi&mdash;vi aiuta a prepararvi per la visita medica. "
                "Caricate il vostro esame del sangue su <a href=\"/analyze\">noryaai.com/analyze</a>: la nostra IA estrarrà emoglobina, "
                "ematocrito, MCV e altri biomarcatori, confrontandoli con gli intervalli di riferimento e generando un report chiaro.</p>"
                "<p>Scoprite le opzioni sulla nostra <a href=\"/pricing\">pagina prezzi</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> '
                'Discutete sempre i risultati con un professionista sanitario. '
                '<a href="/analyze">Inizia l\'analisi con Norya</a></p>'
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
            heading="המוגלובין: מה המשמעות של ערך גבוה או נמוך?",
            body_html=(
                "<p><strong>המוגלובין (Hb)</strong> הוא חלבון עשיר בברזל בתוך כדוריות הדם האדומות, האחראי על העברת חמצן "
                "מהריאות אל כל רקמות הגוף והחזרת פחמן דו-חמצני לריאות. הוא אחד הפרמטרים החשובים ביותר ב<strong>ספירת דם מלאה (CBC)</strong>.</p>"
                "<p>כשהמוגלובין נמוך מדי, המצב נקרא <strong>אנמיה</strong> (מחסור בדם)&mdash;מצב שפוגע בכשליש מאוכלוסיית העולם "
                "לפי ארגון הבריאות העולמי. כשהמוגלובין גבוה מדי, צמיגות הדם עולה ועלולות להופיע בעיות במחזור הדם.</p>"
                "<p>מדריך זה הוא חינוכי בלבד ואינו מחליף ייעוץ רפואי. דונו תמיד בתוצאות עם רופא מוסמך.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="מהו המוגלובין ולמה הוא חשוב?",
            body_html=(
                "<p><strong>המוגלובין</strong> הוא חלבון טטרמרי המורכב מארבע תת-יחידות, כל אחת מכילה קבוצת <em>heme</em> "
                "(טבעת פורפירין עם אטום ברזל מרכזי) ושרשרת <em>גלובין</em>. אצל מבוגרים, הצורה השלטת היא "
                "<strong>HbA</strong> (שתי שרשראות אלפא ושתי בטא), המהווה 95&ndash;98% מסך ההמוגלובין.</p>"
                "<p>תפקידים מרכזיים:</p>"
                "<ul>"
                "<li><strong>הובלת חמצן</strong> &ndash; קושר O₂ באלוואולות הריאה ומשחרר אותו ברקמות.</li>"
                "<li><strong>הובלת CO₂</strong> &ndash; מעביר כ-20% מה-CO₂ המטבולי חזרה לריאות.</li>"
                "<li><strong>חציצת pH</strong> &ndash; מסייע לשמור על pH הדם בטווח 7.35&ndash;7.45.</li>"
                "</ul>"
                "<p>רמות המוגלובין תלויות במאגרי הברזל, ויטמין B12, חומצה פולית, תפקוד מח העצם וייצור אריתרופויאטין (EPO) בכליות.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי המוגלובין תקינים",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח תקין</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים בוגרים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים בוגרות</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים בהיריון</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">יילודים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0 g/dL</td></tr>'
                "</tbody></table>"
                "<p>התייבשות עלולה להעלות את ההמוגלובין באופן מלאכותי. תושבי אזורים גבוהים מציגים ערכים גבוהים יותר כמנגנון פיצוי.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="גורמים להמוגלובין גבוה",
            body_html=(
                "<p><strong>המוגלובין גבוה (פוליציתמיה)</strong> עשוי לנבוע מ:</p>"
                "<ul>"
                "<li><strong>התייבשות</strong> &ndash; ריכוז יחסי של כדוריות אדומות.</li>"
                "<li><strong>פוליציתמיה ורה</strong> &ndash; ניאופלזמה מיאלופרוליפרטיבית עם מוטציית <em>JAK2</em>.</li>"
                "<li><strong>מחלות ריאה כרוניות (COPD)</strong> &ndash; היפוקסיה כרונית מגרה ייצור EPO.</li>"
                "<li><strong>חיים בגובה רב</strong> &ndash; פיצוי ללחץ O₂ אטמוספרי נמוך.</li>"
                "<li><strong>עישון</strong> &ndash; CO נקשר להמוגלובין בזיקה של פי 200&times; מחמצן.</li>"
                "</ul>"
                "<p>המוגלובין גבוה מעלה את צמיגות הדם ואת הסיכון לפקקת, שבץ מוחי ואוטם שריר הלב.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="גורמים להמוגלובין נמוך (אנמיה)",
            body_html=(
                "<p><strong>אנמיה</strong> היא הפרעת הדם הנפוצה ביותר בעולם. גורמים עיקריים:</p>"
                "<ul>"
                "<li><strong>אנמיה מחוסר ברזל</strong> &ndash; הנפוצה ביותר; צריכה לא מספקת, ספיגה לקויה או איבוד דם כרוני.</li>"
                "<li><strong>חוסר B12 וחומצה פולית</strong> &ndash; אנמיה מגלובלסטית עם כדוריות מאקרוציטיות.</li>"
                "<li><strong>אנמיה של מחלה כרונית</strong> &ndash; סרטן, אי-ספיקת כליות, דלקות.</li>"
                "<li><strong>איבוד דם</strong> &ndash; חריף או כרוני.</li>"
                "<li><strong>תלסמיה</strong> &ndash; הפרעה גנטית בסינתזת הגלובין, שכיחה באגן הים התיכון.</li>"
                "<li><strong>אנמיה אפלסטית</strong> &ndash; כשל מח עצם.</li>"
                "<li><strong>אנמיות המוליטיות</strong> &ndash; הרס מואץ של כדוריות אדומות.</li>"
                "</ul>"
                "<p>הטיפול תלוי בגורם: תוספי ברזל, זריקות B12, סוכנים מגרי אריתרופואזיס או עירוי דם במקרים חמורים.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של המוגלובין גבוה ונמוך",
            body_html=(
                "<p><strong>תסמיני אנמיה:</strong> עייפות, חיוורון, קוצר נשימה במאמץ, סחרחורת, דופק מהיר, "
                "ידיים ורגליים קרות, ציפורניים שבירות ונשירת שיער.</p>"
                "<p><strong>תסמיני המוגלובין גבוה:</strong> כאבי ראש, ראייה מטושטשת, סמקת פנים, גירוד "
                "(במיוחד אחרי מקלחת חמה בפוליציתמיה ורה), נימול בקצוות וסיכון פקקתי מוגבר.</p>"
                "<p>אנמיה קלה עלולה להיות אסימפטומטית לאורך זמן. אנמיה חמורה (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) "
                "עלולה לגרום לאי-ספיקת לב ללא טיפול.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות דם קשורות",
            body_html=(
                "<p>המוגלובין מתפרש יחד עם פרמטרים נוספים מספירת הדם:</p>"
                "<ul>"
                "<li><strong>המטוקריט</strong> &ndash; אחוז נפח הדם המורכב מכדוריות אדומות.</li>"
                "<li><strong>ספירת כדוריות אדומות (RBC)</strong></li>"
                "<li><strong>MCV</strong> &ndash; נפח ממוצע של כדורית; מסווג אנמיה כמיקרוציטית, נורמוציטית או מאקרוציטית.</li>"
                "<li><strong>MCH ו-MCHC</strong></li>"
                "<li><strong>RDW</strong></li>"
                "<li><strong>פאנל ברזל</strong> &ndash; ברזל בסרום, פריטין, TIBC, רוויון טרנספרין.</li>"
                "<li><strong>רטיקולוציטים</strong></li>"
                "<li><strong>B12 וחומצה פולית</strong></li>"
                "</ul>"
                "<p>דוגמה: Hb נמוך + MCV נמוך + פריטין נמוך = אנמיה מחוסר ברזל.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>פנו לרופא אם ההמוגלובין מחוץ לטווח הייחוס, בעייפות בלתי מוסברת, חיוורון, קוצר נשימה, "
                "דימום חריג או הפרעות ראייה פתאומיות.</p>"
                "<p><strong>חירום:</strong> המוגלובין מתחת ל-7&nbsp;g/dL או דימום פעיל דורשים טיפול חירום. "
                "המוגלובין גבוה מאוד (&gt;20&nbsp;g/dL) דורש הערכה דחופה בשל סיכון פקקתי.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת",
            body_html=(
                "<p>Norya אינה מאבחנת&mdash;אנחנו עוזרים לכם להתכונן לביקור אצל הרופא. "
                "העלו את תוצאות בדיקת הדם שלכם ב-<a href=\"/analyze\">noryaai.com/analyze</a> ומנוע ה-AI שלנו יחלץ אוטומטית "
                "המוגלובין, המטוקריט, MCV ומדדים נוספים, ישווה אותם לטווחים תקינים ויפיק דוח ברור ומובנה.</p>"
                "<p>למידע על מנויים, בקרו ב<a href=\"/pricing\">עמוד התמחור</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הודעה",
            body_html=(
                '<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> '
                'דונו תמיד בתוצאות עם איש מקצוע רפואי. '
                '<a href="/analyze">התחל ניתוח עם Norya</a></p>'
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
            heading="हीमोग्लोबिन: उच्च या निम्न स्तर का क्या मतलब है?",
            body_html=(
                "<p><strong>हीमोग्लोबिन (Hb)</strong> लाल रक्त कोशिकाओं में पाया जाने वाला लौह-युक्त प्रोटीन है जो फेफड़ों से शरीर "
                "के सभी ऊतकों तक ऑक्सीजन ले जाता है और कार्बन डाइऑक्साइड को वापस फेफड़ों तक लाता है। "
                "यह <strong>कम्प्लीट ब्लड काउंट (CBC)</strong> के सबसे महत्वपूर्ण मापदंडों में से एक है।</p>"
                "<p>जब हीमोग्लोबिन बहुत कम होता है तो इसे <strong>एनीमिया</strong> (खून की कमी) कहते हैं&mdash;WHO के अनुसार "
                "विश्व की लगभग एक-तिहाई जनसंख्या इससे प्रभावित है। जब हीमोग्लोबिन बहुत अधिक होता है तो रक्त गाढ़ा हो जाता है "
                "और रक्त संचार में समस्याएँ हो सकती हैं।</p>"
                "<p>यह गाइड शैक्षणिक है और चिकित्सा सलाह का विकल्प नहीं है। अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें।</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="हीमोग्लोबिन क्या है और यह क्यों महत्वपूर्ण है?",
            body_html=(
                "<p><strong>हीमोग्लोबिन</strong> एक टेट्रामेरिक प्रोटीन है जिसमें चार उप-इकाइयाँ होती हैं, प्रत्येक में एक "
                "<em>हीम</em> समूह (लौह परमाणु सहित पॉर्फिरिन रिंग) और एक <em>ग्लोबिन</em> श्रृंखला होती है। वयस्कों में "
                "प्रमुख रूप <strong>HbA</strong> (दो अल्फ़ा और दो बीटा श्रृंखलाएँ) है, जो कुल हीमोग्लोबिन का 95&ndash;98% होता है।</p>"
                "<p>प्रमुख कार्य:</p>"
                "<ul>"
                "<li><strong>ऑक्सीजन परिवहन</strong> &ndash; फेफड़ों के एल्वियोली में O₂ को बाँधता है और ऊतकों में छोड़ता है।</li>"
                "<li><strong>CO₂ परिवहन</strong> &ndash; चयापचय से उत्पन्न CO₂ का लगभग 20% वापस फेफड़ों तक ले जाता है।</li>"
                "<li><strong>pH बफ़रिंग</strong> &ndash; रक्त pH को 7.35&ndash;7.45 के बीच बनाए रखने में सहायक।</li>"
                "</ul>"
                "<p>हीमोग्लोबिन का स्तर लौह भंडार, विटामिन B12, फ़ोलेट, अस्थि मज्जा कार्य और गुर्दों द्वारा "
                "एरिथ्रोपोइटिन (EPO) उत्पादन पर निर्भर करता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य हीमोग्लोबिन मान",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य सीमा</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क पुरुष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क महिला</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">गर्भवती महिला</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">नवजात</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0 g/dL</td></tr>'
                "</tbody></table>"
                "<p>निर्जलीकरण (डिहाइड्रेशन) हीमोग्लोबिन को कृत्रिम रूप से बढ़ा सकता है। ऊँचाई पर रहने वाले लोगों में "
                "शारीरिक रूप से अधिक मान सामान्य है।</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="उच्च हीमोग्लोबिन के कारण",
            body_html=(
                "<p><strong>उच्च हीमोग्लोबिन (पॉलीसाइथेमिया)</strong> के कारण:</p>"
                "<ul>"
                "<li><strong>डिहाइड्रेशन</strong> &ndash; प्लाज़्मा आयतन कम होने से लाल रक्त कोशिकाओं की सांद्रता बढ़ जाती है।</li>"
                "<li><strong>पॉलीसाइथेमिया वेरा</strong> &ndash; <em>JAK2</em> म्यूटेशन से जुड़ी माइलोप्रोलिफ़ेरेटिव बीमारी।</li>"
                "<li><strong>क्रॉनिक फेफड़ों की बीमारी (COPD)</strong> &ndash; क्रॉनिक हाइपोक्सिया EPO उत्पादन बढ़ाता है।</li>"
                "<li><strong>ऊँचाई पर निवास</strong> &ndash; कम वायुमंडलीय O₂ दबाव के लिए प्रतिपूरक।</li>"
                "<li><strong>धूम्रपान</strong> &ndash; कार्बन मोनोऑक्साइड O₂ से 200&times; अधिक ज़िक़ से Hb से जुड़ता है।</li>"
                "</ul>"
                "<p>उच्च हीमोग्लोबिन रक्त की चिपचिपाहट बढ़ाता है और थ्रॉम्बोसिस, स्ट्रोक और हृदयाघात का जोखिम बढ़ता है।</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="कम हीमोग्लोबिन (एनीमिया) के कारण",
            body_html=(
                "<p><strong>एनीमिया</strong> दुनिया में सबसे आम रक्त विकार है। प्रमुख कारण:</p>"
                "<ul>"
                "<li><strong>आयरन की कमी से एनीमिया</strong> &ndash; सबसे आम; अपर्याप्त आहार, अवशोषण दोष या पुरानी रक्त हानि।</li>"
                "<li><strong>B12 और फ़ोलेट की कमी</strong> &ndash; मेगालोब्लास्टिक एनीमिया जिसमें RBC बड़ी (मैक्रोसाइटिक) होती हैं।</li>"
                "<li><strong>क्रॉनिक रोग एनीमिया</strong> &ndash; कैंसर, गुर्दे की विफलता, सूजन सम्बन्धी रोग।</li>"
                "<li><strong>रक्त हानि</strong> &ndash; तीव्र (आघात) या दीर्घकालिक (GI ब्लीडिंग)।</li>"
                "<li><strong>थैलेसीमिया</strong> &ndash; ग्लोबिन श्रृंखला संश्लेषण का आनुवंशिक विकार।</li>"
                "<li><strong>अप्लास्टिक एनीमिया</strong> &ndash; अस्थि मज्जा विफलता।</li>"
                "<li><strong>हीमोलिटिक एनीमिया</strong> &ndash; लाल रक्त कोशिकाओं का त्वरित विनाश।</li>"
                "</ul>"
                "<p>उपचार कारण पर निर्भर करता है: आयरन सप्लीमेंट, B12 इंजेक्शन, EPO-उत्तेजक एजेंट या गंभीर मामलों में रक्ताधान।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="उच्च और निम्न हीमोग्लोबिन के लक्षण",
            body_html=(
                "<p><strong>एनीमिया के लक्षण:</strong> थकान, पीली त्वचा, सांस फूलना, चक्कर, तेज़ हृदय गति, "
                "हाथ-पैर ठंडे, भंगुर नाखून, बाल गिरना। आयरन की कमी में पाइका (बर्फ़/मिट्टी खाने की इच्छा) हो सकती है।</p>"
                "<p><strong>उच्च हीमोग्लोबिन के लक्षण:</strong> सिरदर्द, धुंधली दृष्टि, चेहरे का लाल होना, खुजली "
                "(विशेषकर गर्म स्नान के बाद), उँगलियों में झुनझुनी और थ्रॉम्बोसिस का बढ़ा जोखिम।</p>"
                "<p>हल्की एनीमिया लंबे समय तक लक्षणहीन हो सकती है। गंभीर एनीमिया (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) "
                "बिना इलाज हृदय विफलता का कारण बन सकती है।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित रक्त परीक्षण",
            body_html=(
                "<p>हीमोग्लोबिन को CBC के अन्य मापदंडों के साथ मिलाकर पढ़ा जाता है:</p>"
                "<ul>"
                "<li><strong>हेमैटोक्रिट</strong> &ndash; रक्त में लाल रक्त कोशिकाओं का प्रतिशत।</li>"
                "<li><strong>RBC गिनती</strong></li>"
                "<li><strong>MCV</strong> &ndash; एनीमिया को माइक्रोसाइटिक, नॉर्मोसाइटिक या मैक्रोसाइटिक में वर्गीकृत करता है।</li>"
                "<li><strong>MCH और MCHC</strong></li>"
                "<li><strong>RDW</strong></li>"
                "<li><strong>आयरन पैनल</strong> &ndash; सीरम आयरन, फ़ेरिटिन, TIBC, ट्रांसफ़ेरिन सैचुरेशन।</li>"
                "<li><strong>रेटिकुलोसाइट काउंट</strong></li>"
                "<li><strong>B12 और फ़ोलेट</strong></li>"
                "</ul>"
                "<p>उदाहरण: कम Hb + कम MCV + कम फ़ेरिटिन = आयरन की कमी से एनीमिया।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>डॉक्टर से मिलें यदि हीमोग्लोबिन सामान्य सीमा से बाहर है, अस्पष्ट थकान, पीलापन, सांस फूलना, "
                "अत्यधिक रक्तस्राव या अचानक दृष्टि बदलाव हो।</p>"
                "<p><strong>आपातकाल:</strong> Hb 7&nbsp;g/dL से नीचे या सक्रिय रक्तस्राव में आपातकालीन चिकित्सा आवश्यक है। "
                "अत्यधिक उच्च Hb (&gt;20&nbsp;g/dL) को भी तत्काल मूल्यांकन की ज़रूरत है।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya कैसे मदद करता है",
            body_html=(
                "<p>Norya निदान नहीं करता&mdash;हम आपको डॉक्टर की विज़िट के लिए तैयार करने में मदद करते हैं। "
                "अपनी रक्त जाँच रिपोर्ट <a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें और हमारा AI इंजन "
                "हीमोग्लोबिन, हेमैटोक्रिट, MCV और अन्य बायोमार्कर निकालकर संदर्भ सीमाओं से तुलना करेगा और एक स्पष्ट रिपोर्ट बनाएगा।</p>"
                "<p>सब्सक्रिप्शन विकल्पों के लिए <a href=\"/pricing\">मूल्य निर्धारण पृष्ठ</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> '
                'अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। '
                '<a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
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
            heading="الهيموغلوبين: ماذا يعني ارتفاعه أو انخفاضه؟",
            body_html=(
                "<p><strong>الهيموغلوبين (Hb)</strong> هو البروتين الغني بالحديد داخل كريات الدم الحمراء، المسؤول عن نقل "
                "الأكسجين من الرئتين إلى جميع أنسجة الجسم وإعادة ثاني أكسيد الكربون إلى الرئتين. "
                "يُعدّ من أهم المعايير في <strong>تعداد الدم الكامل (CBC)</strong>.</p>"
                "<p>عندما يكون الهيموغلوبين منخفضاً جداً تُسمى الحالة <strong>فقر الدم (أنيميا)</strong>&mdash;وهي تصيب "
                "نحو ثلث سكان العالم وفقاً لمنظمة الصحة العالمية. وعندما يرتفع كثيراً تزداد لزوجة الدم وقد تظهر مشاكل "
                "في الدورة الدموية. كلا الحالتين تستدعيان تقييماً طبياً.</p>"
                "<p>هذا الدليل تثقيفي ولا يحلّ محل الاستشارة الطبية. ناقش نتائجك دائماً مع طبيب مؤهّل.</p>"
            ),
        ),
        Section(
            id="what-is-hemoglobin", level=2,
            heading="ما هو الهيموغلوبين ولماذا هو مهم؟",
            body_html=(
                "<p><strong>الهيموغلوبين</strong> بروتين رباعي التركيب يتكون من أربع وحدات فرعية، كل واحدة تحتوي على مجموعة "
                "<em>هيم</em> (حلقة بورفيرين بها ذرة حديد مركزية) وسلسلة <em>غلوبين</em>. الشكل السائد عند البالغين هو "
                "<strong>HbA</strong> (سلسلتا ألفا وسلسلتا بيتا)، ويشكّل 95&ndash;98% من إجمالي الهيموغلوبين.</p>"
                "<p>الوظائف الرئيسية:</p>"
                "<ul>"
                "<li><strong>نقل الأكسجين</strong> &ndash; يرتبط بالأكسجين في الحويصلات الرئوية ويطلقه في الأنسجة.</li>"
                "<li><strong>نقل CO₂</strong> &ndash; ينقل نحو 20% من ثاني أكسيد الكربون الأيضي عائداً إلى الرئتين.</li>"
                "<li><strong>تنظيم pH</strong> &ndash; يساعد في الحفاظ على درجة حموضة الدم بين 7.35 و7.45.</li>"
                "</ul>"
                "<p>تعتمد مستويات الهيموغلوبين على مخازن الحديد وفيتامين B12 وحمض الفوليك ووظيفة نخاع العظم "
                "وإنتاج الإريثروبويتين (EPO) بواسطة الكلى.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="نطاقات الهيموغلوبين الطبيعية",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الفئة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق الطبيعي</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الرجال البالغون</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">13.5&ndash;17.5 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">النساء البالغات</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.0&ndash;16.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الحوامل</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11.0&ndash;14.0 g/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">حديثو الولادة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">14.0&ndash;24.0 g/dL</td></tr>'
                "</tbody></table>"
                "<p>قد يرفع الجفاف الهيموغلوبين بشكل زائف. سكان المرتفعات لديهم قيم أعلى فسيولوجياً كآلية تعويضية.</p>"
            ),
        ),
        Section(
            id="high-hemoglobin-causes", level=2,
            heading="أسباب ارتفاع الهيموغلوبين",
            body_html=(
                "<p><strong>ارتفاع الهيموغلوبين (كثرة الحمر)</strong> قد ينتج عن:</p>"
                "<ul>"
                "<li><strong>الجفاف</strong> &ndash; تركيز نسبي لكريات الدم الحمراء بسبب نقص البلازما.</li>"
                "<li><strong>كثرة الحمر الحقيقية (Polycythemia Vera)</strong> &ndash; ورم تكاثري نقيي مع طفرة <em>JAK2</em>.</li>"
                "<li><strong>أمراض الرئة المزمنة (COPD)</strong> &ndash; نقص الأكسجة المزمن يحفّز إنتاج EPO.</li>"
                "<li><strong>العيش في المرتفعات</strong> &ndash; تعويض لانخفاض ضغط O₂ الجوي.</li>"
                "<li><strong>التدخين</strong> &ndash; أول أكسيد الكربون يرتبط بالهيموغلوبين بقوة تفوق الأكسجين 200&times;.</li>"
                "</ul>"
                "<p>الهيموغلوبين المرتفع يزيد لزوجة الدم وخطر الخثار والسكتة الدماغية والنوبة القلبية.</p>"
            ),
        ),
        Section(
            id="low-hemoglobin-causes", level=2,
            heading="أسباب انخفاض الهيموغلوبين (فقر الدم)",
            body_html=(
                "<p><strong>فقر الدم</strong> هو أكثر اضطرابات الدم شيوعاً في العالم. الأسباب الرئيسية:</p>"
                "<ul>"
                "<li><strong>فقر الدم بعوز الحديد</strong> &ndash; الأكثر شيوعاً؛ نقص في المدخول أو سوء امتصاص أو فقدان دم مزمن.</li>"
                "<li><strong>نقص B12 وحمض الفوليك</strong> &ndash; فقر دم ضخم الأرومات مع كريات كبيرة الحجم.</li>"
                "<li><strong>فقر دم الأمراض المزمنة</strong> &ndash; سرطان، قصور كلوي، أمراض التهابية.</li>"
                "<li><strong>فقدان الدم</strong> &ndash; حاد أو مزمن.</li>"
                "<li><strong>الثلاسيميا</strong> &ndash; اضطراب وراثي في تركيب الغلوبين، شائع في حوض المتوسط.</li>"
                "<li><strong>فقر الدم اللاتنسجي</strong> &ndash; فشل نخاع العظم.</li>"
                "<li><strong>فقر الدم الانحلالي</strong> &ndash; تدمير متسارع لكريات الدم الحمراء.</li>"
                "</ul>"
                "<p>يعتمد العلاج على السبب: مكملات حديد، حقن B12، عوامل محفّزة للإريثروبويتين أو نقل دم في الحالات الشديدة.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض الهيموغلوبين المرتفع والمنخفض",
            body_html=(
                "<p><strong>أعراض فقر الدم:</strong> إرهاق، شحوب، ضيق تنفس عند الجهد، دوخة، تسارع نبضات القلب، "
                "برودة اليدين والقدمين، أظافر هشة وتساقط الشعر. في نقص الحديد قد تظهر بيكا (رغبة في أكل الثلج أو التراب).</p>"
                "<p><strong>أعراض الهيموغلوبين المرتفع:</strong> صداع، رؤية ضبابية، احمرار الوجه، حكة "
                "(خاصة بعد الاستحمام الساخن في كثرة الحمر الحقيقية)، تنميل في الأطراف وزيادة خطر التخثر.</p>"
                "<p>فقر الدم الخفيف قد يبقى بلا أعراض لفترة طويلة. فقر الدم الشديد (Hb&nbsp;&lt;&nbsp;7&nbsp;g/dL) "
                "قد يؤدي إلى قصور القلب دون علاج.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="فحوصات ذات صلة",
            body_html=(
                "<p>يُفسَّر الهيموغلوبين مع بقية معايير تعداد الدم الكامل:</p>"
                "<ul>"
                "<li><strong>الهيماتوكريت</strong> &ndash; نسبة حجم الدم المكوّن من كريات حمراء.</li>"
                "<li><strong>عدد كريات الدم الحمراء (RBC)</strong></li>"
                "<li><strong>MCV</strong> &ndash; يصنّف فقر الدم إلى صغير الكريات أو طبيعي الكريات أو كبير الكريات.</li>"
                "<li><strong>MCH وMCHC</strong></li>"
                "<li><strong>RDW</strong></li>"
                "<li><strong>مؤشرات الحديد</strong> &ndash; حديد المصل، الفيريتين، TIBC، إشباع الترانسفيرين.</li>"
                "<li><strong>الخلايا الشبكية</strong></li>"
                "<li><strong>B12 وحمض الفوليك</strong></li>"
                "</ul>"
                "<p>مثال: Hb منخفض + MCV منخفض + فيريتين منخفض = فقر دم بعوز الحديد.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب؟",
            body_html=(
                "<p>راجع الطبيب إذا كان الهيموغلوبين خارج النطاق المرجعي، أو عند إرهاق غير مبرر، شحوب، "
                "ضيق تنفس، نزيف غزير أو تغيّرات بصرية مفاجئة.</p>"
                "<p><strong>طوارئ:</strong> هيموغلوبين أقل من 7&nbsp;g/dL أو نزيف فعّال يتطلب تدخلاً طارئاً. "
                "الهيموغلوبين المرتفع جداً (&gt;20&nbsp;g/dL) يحتاج أيضاً تقييماً عاجلاً بسبب خطر التخثر.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya",
            body_html=(
                "<p>Norya لا تُشخّص&mdash;نساعدك على الاستعداد لزيارة الطبيب. ارفع تقرير فحص الدم على "
                "<a href=\"/analyze\">noryaai.com/analyze</a> وسيستخرج محرك الذكاء الاصطناعي الهيموغلوبين والهيماتوكريت وMCV "
                "ومؤشرات أخرى، يقارنها بالنطاقات المرجعية ويُنشئ تقريراً واضحاً ومنظّماً.</p>"
                "<p>لخيارات الاشتراك، زُر <a href=\"/pricing\">صفحة الأسعار</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> '
                'ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. '
                '<a href="/analyze">ابدأ التحليل مع Norya</a></p>'
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
             "answer": "Normal hemoglobin is 13.5–17.5 g/dL for adult men and 12.0–16.0 g/dL for adult women. Pregnant women have a lower threshold of 11.0 g/dL. Values vary slightly between laboratories."},
            {"question": "What causes low hemoglobin?",
             "answer": "The most common cause is iron deficiency anemia, resulting from inadequate dietary iron, impaired absorption, or chronic blood loss. Other causes include B12/folate deficiency, chronic disease, thalassemia, and hemolytic anemias."},
            {"question": "What causes high hemoglobin?",
             "answer": "High hemoglobin can be caused by dehydration, polycythemia vera, chronic lung disease (COPD), living at high altitude, smoking, or congenital heart disease. It increases blood viscosity and thrombosis risk."},
            {"question": "What are the symptoms of low hemoglobin?",
             "answer": "Symptoms include fatigue, pale skin, shortness of breath on exertion, dizziness, rapid heartbeat, cold extremities, brittle nails, and hair loss. Severe anemia (Hb < 7 g/dL) can cause heart failure."},
            {"question": "How is hemoglobin related to hematocrit?",
             "answer": "Hematocrit measures the percentage of blood volume occupied by red blood cells, while hemoglobin measures the oxygen-carrying protein inside them. They move in parallel—when one is low, the other typically is too."},
        ],
        "tr": [
            {"question": "Normal hemoglobin değeri nedir?",
             "answer": "Yetişkin erkeklerde 13,5–17,5 g/dL, yetişkin kadınlarda 12,0–16,0 g/dL normaldir. Hamilelikte alt sınır 11,0 g/dL'dir."},
            {"question": "Hemoglobin düşüklüğünün nedenleri nelerdir?",
             "answer": "En yaygın neden demir eksikliği anemisidir. Diğer nedenler arasında B12/folat eksikliği, kronik hastalık, talasemi ve hemolitik anemiler yer alır."},
            {"question": "Hemoglobin yüksekliğinin nedenleri nelerdir?",
             "answer": "Dehidrasyon, polisitemia vera, kronik akciğer hastalığı (KOAH), yüksek rakımda yaşam, sigara kullanımı veya konjenital kalp hastalığı neden olabilir."},
            {"question": "Düşük hemoglobin belirtileri nelerdir?",
             "answer": "Halsizlik, soluk cilt, efor sırasında nefes darlığı, baş dönmesi, çarpıntı, soğuk el ve ayaklar, kırılgan tırnaklar ve saç dökülmesi. Şiddetli anemi kalp yetmezliğine yol açabilir."},
            {"question": "Hemoglobin ve hematokrit arasındaki ilişki nedir?",
             "answer": "Hematokrit, kanın kırmızı kan hücrelerinden oluşan yüzdesini ölçer; hemoglobin ise bu hücrelerin içindeki oksijen taşıyan proteini ölçer. İkisi paralel hareket eder."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de hemoglobina?",
             "answer": "Hombres: 13,5–17,5 g/dL. Mujeres: 12,0–16,0 g/dL. Embarazadas: umbral inferior de 11,0 g/dL."},
            {"question": "¿Qué causa la hemoglobina baja?",
             "answer": "La causa más común es la anemia ferropénica. Otras: déficit de B12/folato, enfermedad crónica, talasemia y anemias hemolíticas."},
            {"question": "¿Qué causa la hemoglobina alta?",
             "answer": "Deshidratación, policitemia vera, EPOC, vida en altitud, tabaquismo o cardiopatía congénita."},
            {"question": "¿Cuáles son los síntomas de hemoglobina baja?",
             "answer": "Fatiga, palidez, disnea de esfuerzo, mareos, taquicardia, extremidades frías, uñas frágiles y caída del cabello."},
        ],
        "de": [
            {"question": "Was ist ein normaler Hämoglobinwert?",
             "answer": "Männer: 13,5–17,5 g/dL. Frauen: 12,0–16,0 g/dL. Schwangere: Untergrenze 11,0 g/dL."},
            {"question": "Was verursacht niedriges Hämoglobin?",
             "answer": "Die häufigste Ursache ist Eisenmangelanämie. Weitere: B12-/Folsäuremangel, chronische Erkrankungen, Thalassämie und hämolytische Anämien."},
            {"question": "Was verursacht hohes Hämoglobin?",
             "answer": "Dehydration, Polycythaemia vera, COPD, Leben in großer Höhe, Rauchen oder angeborene Herzfehler."},
            {"question": "Was sind Symptome von niedrigem Hämoglobin?",
             "answer": "Müdigkeit, Blässe, Belastungsdyspnoe, Schwindel, Tachykardie, kalte Extremitäten, brüchige Nägel und Haarausfall."},
        ],
        "fr": [
            {"question": "Quel est le taux normal d'hémoglobine ?",
             "answer": "Hommes : 13,5–17,5 g/dL. Femmes : 12,0–16,0 g/dL. Femmes enceintes : seuil de 11,0 g/dL."},
            {"question": "Quelles sont les causes d'une hémoglobine basse ?",
             "answer": "La cause la plus fréquente est l'anémie ferriprive. Autres : carence en B12/folates, maladie chronique, thalassémie et anémies hémolytiques."},
            {"question": "Quelles sont les causes d'une hémoglobine élevée ?",
             "answer": "Déshydratation, polyglobulie de Vaquez, BPCO, vie en altitude, tabagisme ou cardiopathie congénitale."},
            {"question": "Quels sont les symptômes d'une hémoglobine basse ?",
             "answer": "Fatigue, pâleur, dyspnée d'effort, vertiges, tachycardie, extrémités froides, ongles cassants et chute de cheveux."},
        ],
        "it": [
            {"question": "Qual è il valore normale dell'emoglobina?",
             "answer": "Uomini: 13,5–17,5 g/dL. Donne: 12,0–16,0 g/dL. Gravidanza: soglia inferiore 11,0 g/dL."},
            {"question": "Cosa causa l'emoglobina bassa?",
             "answer": "La causa più comune è l'anemia sideropenica. Altre: carenza di B12/folati, malattie croniche, talassemia e anemie emolitiche."},
            {"question": "Cosa causa l'emoglobina alta?",
             "answer": "Disidratazione, policitemia vera, BPCO, vita in alta quota, fumo o cardiopatie congenite."},
            {"question": "Quali sono i sintomi dell'emoglobina bassa?",
             "answer": "Affaticamento, pallore, dispnea da sforzo, vertigini, tachicardia, estremità fredde, unghie fragili e caduta dei capelli."},
        ],
        "he": [
            {"question": "מהו ערך המוגלובין תקין?",
             "answer": "גברים: 13.5–17.5 g/dL. נשים: 12.0–16.0 g/dL. בהיריון: סף תחתון 11.0 g/dL."},
            {"question": "מה גורם להמוגלובין נמוך?",
             "answer": "הסיבה השכיחה ביותר היא אנמיה מחוסר ברזל. סיבות נוספות: חוסר B12/פולאט, מחלה כרונית, תלסמיה ואנמיות המוליטיות."},
            {"question": "מה גורם להמוגלובין גבוה?",
             "answer": "התייבשות, פוליציתמיה ורה, COPD, חיים בגובה רב, עישון או מום לב מולד."},
            {"question": "מתי לפנות לרופא בגלל המוגלובין?",
             "answer": "פנו לרופא אם ההמוגלובין מחוץ לטווח, בעייפות בלתי מוסברת, חיוורון, קוצר נשימה או דימום חריג. חירום: Hb מתחת ל-7 g/dL."},
        ],
        "hi": [
            {"question": "सामान्य हीमोग्लोबिन कितना होना चाहिए?",
             "answer": "पुरुष: 13.5–17.5 g/dL। महिला: 12.0–16.0 g/dL। गर्भवती: निचली सीमा 11.0 g/dL।"},
            {"question": "हीमोग्लोबिन कम होने के कारण क्या हैं?",
             "answer": "सबसे आम कारण आयरन की कमी से एनीमिया है। अन्य: B12/फ़ोलेट की कमी, क्रॉनिक रोग, थैलेसीमिया और हीमोलिटिक एनीमिया।"},
            {"question": "हीमोग्लोबिन बढ़ने के कारण क्या हैं?",
             "answer": "डिहाइड्रेशन, पॉलीसाइथेमिया वेरा, COPD, ऊँचाई पर रहना, धूम्रपान या जन्मजात हृदय रोग।"},
            {"question": "कम हीमोग्लोबिन के लक्षण क्या हैं?",
             "answer": "थकान, पीली त्वचा, परिश्रम पर सांस फूलना, चक्कर, तेज़ हृदय गति, ठंडे हाथ-पैर, भंगुर नाखून और बाल गिरना।"},
        ],
        "ar": [
            {"question": "ما هو مستوى الهيموغلوبين الطبيعي؟",
             "answer": "الرجال: 13.5–17.5 g/dL. النساء: 12.0–16.0 g/dL. الحوامل: حد أدنى 11.0 g/dL."},
            {"question": "ما أسباب انخفاض الهيموغلوبين؟",
             "answer": "السبب الأشيع هو فقر الدم بعوز الحديد. أسباب أخرى: نقص B12/فولات، مرض مزمن، ثلاسيميا وفقر دم انحلالي."},
            {"question": "ما أسباب ارتفاع الهيموغلوبين؟",
             "answer": "الجفاف، كثرة الحمر الحقيقية، COPD، العيش في المرتفعات، التدخين أو عيوب قلب خلقية."},
            {"question": "ما أعراض الهيموغلوبين المنخفض؟",
             "answer": "إرهاق، شحوب، ضيق تنفس عند الجهد، دوخة، تسارع نبض، برودة أطراف، أظافر هشة وتساقط شعر."},
        ],
    }
