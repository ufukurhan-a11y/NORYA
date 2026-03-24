# -*- coding: utf-8 -*-
"""
Neutrophils blog article — full body content for all 9 languages.
Used by blog_i18n._article_neutrophils().
Sections: intro, what-are-neutrophils, normal-ranges, high-neutrophils-causes,
low-neutrophils-causes, absolute-vs-percentage, symptoms, related-tests,
when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="Nötrofil yüksekliği ve düşüklüğü: kan testiniz ne anlama geliyor?",
            body_html=(
                "<p><strong>Nötrofiller</strong>, bağışıklık sisteminin ön cephe savunma hücreleri olup beyaz kan hücrelerinin "
                "(lökositler) en kalabalık grubunu oluşturur. Bakteri ve mantar enfeksiyonlarına karşı ilk yanıt veren hücrelerdir; "
                "enfeksiyon bölgesine hızla göç ederek patojenleri fagosite ederler (yutup sindirirler). Tam kan sayımının (CBC) "
                "ayrılmaz parçası olan nötrofil değeri, enfeksiyon, inflamasyon ve kemik iliği fonksiyonu hakkında kritik bilgi sağlar.</p>"
                "<p>Nötrofil sayısının normalin üzerinde olması <strong>nötrofili</strong>, altında olması <strong>nötropeni</strong> "
                "olarak adlandırılır. Her iki durum da farklı nedenlere bağlı olabilir ve klinik değerlendirme gerektirir.</p>"
                "<p>Bu rehber bilgilendirme amaçlıdır ve tıbbi tavsiye yerine geçmez. Sonuçlarınızı mutlaka doktorunuzla görüşün.</p>"
            ),
        ),
        Section(
            id="what-are-neutrophils", level=2,
            heading="Nötrofiller nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Nötrofiller</strong>, kemik iliğinde üretilen ve kana salınan granülositlerdir. Dolaşımdaki beyaz kan "
                "hücrelerinin yaklaşık %50&ndash;70&rsquo;ini oluşturur ve ortalama ömürleri sadece 5&ndash;90 saattir; "
                "bu nedenle kemik iliği sürekli yeni nötrofil üretmek zorundadır.</p>"
                "<p>Nötrofillerin enfeksiyona karşı temel mekanizmaları şunlardır:</p>"
                "<ul>"
                "<li><strong>Fagositoz</strong> &ndash; bakterileri ve mantar hücrelerini yutarak hücre içi enzimleriyle parçalarlar.</li>"
                "<li><strong>Degranülasyon</strong> &ndash; antimikrobiyal proteinler içeren granüllerini dışarı salarlar.</li>"
                "<li><strong>NET (nötrofil ekstraselüler tuzaklar)</strong> &ndash; DNA ipliklerinden oluşan ağ benzeri yapılar salgılayarak "
                "patojenleri hapsederler.</li>"
                "</ul>"
                "<p>Nötrofillerin ağır düşüklüğü (mutlak sayı &lt;500/µL), ciddi enfeksiyon riskine yol açar ve "
                "<strong>şiddetli nötropeni</strong> olarak adlandırılır. Bu durum özellikle kemoterapi alan hastalarda "
                "yaşamı tehdit edici olabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal nötrofil değerleri",
            body_html=(
                "<p>Nötrofiller hem mutlak sayı (ANC) hem de yüzde olarak raporlanır:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parametre</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mutlak nötrofil sayısı (ANC)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.500&ndash;7.000 hücre/&micro;L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Nötrofil yüzdesi</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">%40&ndash;%70</td></tr>'
                "</tbody></table>"
                "<p>ANC, toplam beyaz küre sayısının nötrofil yüzdesiyle çarpılmasıyla hesaplanır: "
                "<em>ANC = WBC &times; nötrofil % / 100</em>. Klinik kararlar genellikle yüzde yerine mutlak sayıya göre verilir; "
                "çünkü toplam WBC değiştiğinde yüzde yanıltıcı olabilir.</p>"
                "<p><strong>Nötropeni sınıflandırması:</strong> hafif (1.000&ndash;1.500/µL), orta (500&ndash;1.000/µL), "
                "ağır (&lt;500/µL). Ağır nötropeni ciddi enfeksiyon riski taşır.</p>"
            ),
        ),
        Section(
            id="high-neutrophils-causes", level=2,
            heading="Nötrofil yüksekliğinin (nötrofili) nedenleri",
            body_html=(
                "<p><strong>Nötrofili</strong>, nötrofil sayısının 7.000/µL&rsquo;nin üzerine çıkması olarak tanımlanır. En yaygın nedenler:</p>"
                "<ul>"
                "<li><strong>Bakteriyel enfeksiyonlar</strong> &ndash; en sık neden; pnömoni, üriner enfeksiyon, selülit, apseler. "
                "Vücut enfeksiyonla savaşmak için kemik iliğinden hızla nötrofil salgılar.</li>"
                "<li><strong>Akut inflamasyon</strong> &ndash; cerrahi sonrası, travma, yanık, miyokard enfarktüsü gibi doku hasarı durumları.</li>"
                "<li><strong>Stres yanıtı</strong> &ndash; akut fiziksel veya duygusal stres, kortizol aracılığıyla nötrofillerin "
                "marjinal havuzdan dolaşıma geçmesine neden olur.</li>"
                "<li><strong>Kortikosteroid kullanımı</strong> &ndash; prednizon, deksametazon gibi ilaçlar nötrofil sayısını yükseltir; "
                "bu etki nötrofillerin damar duvarından ayrılmasını artırmalarından kaynaklanır.</li>"
                "<li><strong>Sigara</strong> &ndash; kronik hafif nötrofiliye neden olabilir.</li>"
                "<li><strong>Miyeloproliferatif hastalıklar</strong> &ndash; kronik miyeloid lösemi (KML) ve polisitemia vera gibi "
                "kemik iliği kaynaklı neoplaziler.</li>"
                "</ul>"
                "<p>Nötrofilinin kendi başına bir hastalık olmadığını, altta yatan bir duruma bağlı olarak geliştiğini "
                "hatırlamak önemlidir. Nedene yönelik değerlendirme gerekir.</p>"
            ),
        ),
        Section(
            id="low-neutrophils-causes", level=2,
            heading="Nötrofil düşüklüğünün (nötropeni) nedenleri",
            body_html=(
                "<p><strong>Nötropeni</strong>, mutlak nötrofil sayısının 1.500/µL&rsquo;nin altına düşmesi olarak tanımlanır. Başlıca nedenler:</p>"
                "<ul>"
                "<li><strong>Viral enfeksiyonlar</strong> &ndash; grip, HIV, hepatit, EBV gibi virüsler kemik iliği üretimini "
                "geçici olarak baskılayabilir veya nötrofilleri dokulara çekebilir.</li>"
                "<li><strong>İlaçlar</strong> &ndash; kemoterapötik ajanlar (en sık neden), kloramfenikol, karbamazepin, "
                "klozapin, metamizol, tiyonamidler (metimazol) gibi ilaçlar.</li>"
                "<li><strong>Otoimmün nötropeni</strong> &ndash; nötrofillere karşı antikor oluşumu sonucu yıkımlarının artması.</li>"
                "<li><strong>Kemik iliği yetmezliği</strong> &ndash; aplastik anemi, miyelodisplastik sendrom veya kemik iliği "
                "infiltrasyonu (lösemi, lenfoma, metastatik kanser).</li>"
                "<li><strong>Ağır enfeksiyonlar (sepsis)</strong> &ndash; paradoks olarak çok şiddetli enfeksiyonlarda nötrofil "
                "tüketimi üretimi aşarak nötropeni oluşabilir; bu kötü prognoz işaretidir.</li>"
                "<li><strong>Benign etnik nötropeni</strong> &ndash; Afrika, Ortadoğu ve Akdeniz kökenli bireylerde genetik olarak "
                "ANC 1.000&ndash;1.500/µL arasında olabilir, bu patolojik değildir.</li>"
                "</ul>"
                "<p>Nötropeni şiddeti arttıkça enfeksiyon riski üstel olarak yükselir. ANC &lt;500/µL olan hastalar "
                "ateş geliştirdiğinde &ldquo;febril nötropeni&rdquo; acildir ve hemen geniş spektrumlu antibiyotik başlanmalıdır.</p>"
            ),
        ),
        Section(
            id="absolute-vs-percentage", level=2,
            heading="Mutlak nötrofil sayısı (ANC) ve nötrofil yüzdesi farkı",
            body_html=(
                "<p>Kan testi raporlarında nötrofiller genellikle iki şekilde belirtilir:</p>"
                "<ul>"
                "<li><strong>Yüzde (%)</strong> &ndash; toplam beyaz kan hücreleri içindeki nötrofil oranı. "
                "Örneğin WBC = 10.000/µL ve nötrofil = %60 ise ANC = 6.000/µL.</li>"
                "<li><strong>Mutlak sayı (ANC)</strong> &ndash; mikrolitre başına nötrofil sayısı. "
                "Klinik açıdan daha güvenilir bir göstergedir.</li>"
                "</ul>"
                "<p>Yüzde tek başına yanıltıcı olabilir. Örneğin WBC = 3.000/µL ve nötrofil = %60 ise ANC = 1.800/µL olup "
                "aslında nötropeni sınırındadır; ancak yüzdeye bakıldığında &ldquo;normal&rdquo; görünür. "
                "Bu nedenle doktorlar ve klinik rehberler değerlendirmelerini her zaman mutlak sayıya dayandırır.</p>"
                "<p>Norya raporlarında hem yüzde hem de mutlak sayı gösterilir ve referans aralıklarıyla karşılaştırılır, "
                "böylece doktorunuzla paylaşmak için net bir resim elde edersiniz.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Nötrofil bozukluklarının belirtileri",
            body_html=(
                "<p><strong>Nötrofilinin kendine özgü bir belirtisi genellikle yoktur</strong>; belirtiler altta yatan "
                "nedene bağlıdır (örneğin enfeksiyon belirtileri: ateş, kızarıklık, şişlik).</p>"
                "<p><strong>Nötropeni belirtileri</strong> enfeksiyon eğilimiyle ilişkilidir:</p>"
                "<ul>"
                "<li>Tekrarlayan veya uzun süren ateşli enfeksiyonlar</li>"
                "<li>Ağız ülserleri (aftöz stomatit)</li>"
                "<li>Dişeti iltihabı ve periodontal hastalık</li>"
                "<li>Cilt enfeksiyonları, apseler</li>"
                "<li>Solunum yolu enfeksiyonları (pnömoni)</li>"
                "<li>Ateş&mdash;nötropenik hastada tek belirti sadece ateş olabilir, çünkü enflamatuar yanıt "
                "baskılandığından tipik enfeksiyon bulguları (kızarıklık, cerahat) oluşmayabilir</li>"
                "</ul>"
                "<p>Nötropenik hastada ateş tıbbi acil kabul edilir ve derhal değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlgili testler",
            body_html=(
                "<p>Nötrofil değerlendirmesi genellikle tam kan sayımı ve lökosit formülü (diferansiyel) kapsamında yapılır:</p>"
                "<ul>"
                "<li><strong>Toplam beyaz küre sayısı (WBC)</strong> &ndash; nötrofil mutlak sayısının hesaplanması için gereklidir.</li>"
                "<li><strong>Lenfositler</strong> &ndash; viral enfeksiyonlarda artabilir; nötrofil/lenfosit oranı (NLR) inflamasyon belirteci olarak kullanılır.</li>"
                "<li><strong>Monositler</strong> &ndash; kronik enfeksiyonlarda artabilir.</li>"
                "<li><strong>Eozinofiller</strong> &ndash; alerjik durumlar ve paraziter enfeksiyonlarda artar.</li>"
                "<li><strong>Bazofiller</strong> &ndash; nadir durumlarda değerlendirilir.</li>"
                "<li><strong>CRP (C-reaktif protein)</strong> &ndash; sistemik inflamasyonun belirteci; nötrofili ile birlikte değerlendirilir.</li>"
                "<li><strong>Prokalsitonin</strong> &ndash; bakteriyel enfeksiyon için daha spesifik bir belirteç.</li>"
                "<li><strong>Periferik yayma</strong> &ndash; nötrofillerin morfolojisini (toksik granülasyon, band formları) değerlendirir.</li>"
                "</ul>"
                "<p>Bu testlerin kombinasyonu, nötrofil değişikliğinin nedenini daraltmaya yardımcı olur.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Doktora ne zaman başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda bir sağlık uzmanına danışın:</p>"
                "<ul>"
                "<li>Nötrofil sayınız referans aralığının dışında çıktıysa</li>"
                "<li>Tekrarlayan veya uzun süreli enfeksiyonlar yaşıyorsanız</li>"
                "<li>Ağız ülserleri, dişeti kanaması veya cilt enfeksiyonlarınız varsa</li>"
                "<li>Kemoterapi veya immunosupresif tedavi alıyorsanız</li>"
                "</ul>"
                "<p><strong>Acil durum (febril nötropeni):</strong> ANC &lt;500/µL olan bir hastada 38,3°C ve üzeri ateş "
                "(veya bir saat süren 38,0°C ateş) acil müdahale gerektirir. Gecikmiş antibiyotik tedavisi yaşamı tehdit edebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;doktor ziyaretinize hazırlanmanıza yardımcı olur. "
                "Kan tahlili raporunuzu <a href=\"/analyze\">noryaai.com/analyze</a> sayfasına yükleyin; "
                "yapay zekâ motorumuz nötrofil mutlak sayısı ve yüzdesini, toplam WBC&rsquo;yi ve diğer lökosit alt tiplerini "
                "otomatik olarak çıkarır, referans aralıklarıyla karşılaştırır ve anlaşılır bir rapor oluşturur.</p>"
                "<p>Abonelik seçenekleri için <a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
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
            heading="Neutrophils high or low: what your blood test means",
            body_html=(
                "<p><strong>Neutrophils</strong> are the most abundant type of white blood cell and serve as the immune system&rsquo;s "
                "first responders. They are the frontline defence against bacterial and fungal infections, rushing to the site of "
                "invasion to engulf and destroy pathogens through phagocytosis. Neutrophil counts are a key component of the "
                "<strong>complete blood count (CBC)</strong> with differential and provide critical insight into infection, "
                "inflammation, and bone marrow function.</p>"
                "<p>An elevated count is called <strong>neutrophilia</strong>, while a reduced count is called <strong>neutropenia</strong>. "
                "Both conditions can arise from a wide range of causes and warrant clinical evaluation.</p>"
                "<p>This guide is educational and does not replace medical advice. Always discuss your results with a healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-are-neutrophils", level=2,
            heading="What are neutrophils and why do they matter?",
            body_html=(
                "<p><strong>Neutrophils</strong> are granulocytes produced in the bone marrow and released into the bloodstream. "
                "They make up approximately 50&ndash;70% of circulating white blood cells and have a remarkably short lifespan of "
                "just 5&ndash;90 hours in circulation, which means the bone marrow must continuously produce new neutrophils "
                "at an estimated rate of 10<sup>11</sup> cells per day.</p>"
                "<p>Neutrophils fight infection through several mechanisms:</p>"
                "<ul>"
                "<li><strong>Phagocytosis</strong> &ndash; engulfing bacteria and fungi, then destroying them with intracellular enzymes "
                "and reactive oxygen species.</li>"
                "<li><strong>Degranulation</strong> &ndash; releasing antimicrobial proteins and enzymes from cytoplasmic granules.</li>"
                "<li><strong>NETs (neutrophil extracellular traps)</strong> &ndash; extruding web-like structures of DNA and antimicrobial "
                "proteins to trap and kill pathogens.</li>"
                "</ul>"
                "<p>Severely low neutrophil counts (absolute count &lt;500/&micro;L) leave the body vulnerable to life-threatening "
                "infections, a state known as <strong>severe neutropenia</strong>. This is particularly dangerous in patients "
                "undergoing chemotherapy.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal neutrophil ranges",
            body_html=(
                "<p>Neutrophils are reported as both an absolute count (ANC) and a percentage of total white blood cells:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parameter</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Absolute Neutrophil Count (ANC)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,500&ndash;7,000 cells/&micro;L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neutrophil percentage</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70%</td></tr>'
                "</tbody></table>"
                "<p>The ANC is calculated by multiplying the total WBC count by the neutrophil percentage: "
                "<em>ANC = WBC &times; neutrophil % / 100</em>. Clinical decisions are based on the absolute count rather than "
                "the percentage, because the percentage can be misleading when the total WBC is abnormal.</p>"
                "<p><strong>Neutropenia grading:</strong> mild (1,000&ndash;1,500/&micro;L), moderate (500&ndash;1,000/&micro;L), "
                "severe (&lt;500/&micro;L). Severe neutropenia carries significant infection risk.</p>"
            ),
        ),
        Section(
            id="high-neutrophils-causes", level=2,
            heading="Causes of high neutrophils (neutrophilia)",
            body_html=(
                "<p><strong>Neutrophilia</strong> is defined as an ANC above 7,000/&micro;L. The most common causes include:</p>"
                "<ul>"
                "<li><strong>Bacterial infections</strong> &ndash; the most frequent trigger. Pneumonia, urinary tract infections, "
                "cellulitis, and abscesses all provoke rapid neutrophil mobilization from the bone marrow.</li>"
                "<li><strong>Acute inflammation</strong> &ndash; post-surgical tissue injury, trauma, burns, and myocardial infarction "
                "cause neutrophil recruitment to damaged tissue.</li>"
                "<li><strong>Physiological stress response</strong> &ndash; acute physical or emotional stress causes cortisol-mediated "
                "demargination of neutrophils from blood vessel walls into the circulating pool.</li>"
                "<li><strong>Corticosteroid medications</strong> &ndash; prednisone, dexamethasone, and similar drugs increase the "
                "neutrophil count by promoting demargination and reducing neutrophil migration out of blood vessels.</li>"
                "<li><strong>Smoking</strong> &ndash; chronic low-grade inflammation from smoking can cause persistent mild neutrophilia.</li>"
                "<li><strong>Myeloproliferative disorders</strong> &ndash; chronic myeloid leukaemia (CML), polycythemia vera, "
                "and essential thrombocythemia may present with markedly elevated neutrophils.</li>"
                "</ul>"
                "<p>Neutrophilia is a response to an underlying process, not a disease in itself. Identifying the trigger "
                "is essential for appropriate management.</p>"
            ),
        ),
        Section(
            id="low-neutrophils-causes", level=2,
            heading="Causes of low neutrophils (neutropenia)",
            body_html=(
                "<p><strong>Neutropenia</strong> is defined as an ANC below 1,500/&micro;L. Principal causes include:</p>"
                "<ul>"
                "<li><strong>Viral infections</strong> &ndash; influenza, HIV, hepatitis, EBV, and other viruses can temporarily "
                "suppress bone marrow production or redistribute neutrophils to tissues.</li>"
                "<li><strong>Medications</strong> &ndash; chemotherapy agents (the most common cause of severe neutropenia), "
                "chloramphenicol, carbamazepine, clozapine, metamizole, and thionamides (methimazole).</li>"
                "<li><strong>Autoimmune neutropenia</strong> &ndash; antibodies directed against neutrophils cause increased destruction.</li>"
                "<li><strong>Bone marrow failure</strong> &ndash; aplastic anemia, myelodysplastic syndromes, or bone marrow "
                "infiltration (leukaemia, lymphoma, metastatic cancer).</li>"
                "<li><strong>Severe infections (sepsis)</strong> &ndash; paradoxically, overwhelming infections can consume neutrophils "
                "faster than the marrow can produce them, leading to neutropenia&mdash;a poor prognostic sign.</li>"
                "<li><strong>Benign ethnic neutropenia</strong> &ndash; individuals of African, Middle Eastern, and Mediterranean "
                "descent may have a constitutionally lower ANC (1,000&ndash;1,500/&micro;L) without increased infection risk.</li>"
                "</ul>"
                "<p>As neutropenia deepens, infection risk increases exponentially. A neutropenic patient who develops fever "
                "(≥38.3°C or sustained ≥38.0°C for one hour) has <strong>febrile neutropenia</strong>&mdash;a medical emergency "
                "requiring immediate broad-spectrum antibiotics.</p>"
            ),
        ),
        Section(
            id="absolute-vs-percentage", level=2,
            heading="Absolute neutrophil count (ANC) vs. percentage: why it matters",
            body_html=(
                "<p>Blood test reports typically display neutrophils in two ways:</p>"
                "<ul>"
                "<li><strong>Percentage (%)</strong> &ndash; the proportion of total white blood cells that are neutrophils. "
                "For example, if WBC = 10,000/&micro;L and neutrophils = 60%, then ANC = 6,000/&micro;L.</li>"
                "<li><strong>Absolute count (ANC)</strong> &ndash; the actual number of neutrophils per microlitre of blood. "
                "This is clinically more reliable.</li>"
                "</ul>"
                "<p>The percentage can be misleading on its own. Consider a patient with WBC = 3,000/&micro;L and neutrophils = 60%. "
                "The percentage appears &ldquo;normal,&rdquo; but the ANC is only 1,800/&micro;L&mdash;approaching the neutropenia "
                "threshold. Conversely, a high neutrophil percentage with a low total WBC may mask a truly low ANC.</p>"
                "<p>Clinical guidelines and treatment decisions (especially for febrile neutropenia) are always based on the "
                "absolute count, not the percentage. Norya reports display both values and compare each against reference ranges "
                "so you have a clear picture to share with your doctor.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of neutrophil disorders",
            body_html=(
                "<p><strong>Neutrophilia usually has no symptoms of its own</strong>&mdash;symptoms are those of the underlying cause "
                "(e.g. fever, redness, swelling from an infection).</p>"
                "<p><strong>Neutropenia symptoms</strong> relate to increased infection susceptibility:</p>"
                "<ul>"
                "<li>Recurrent or prolonged febrile infections</li>"
                "<li>Mouth ulcers (aphthous stomatitis)</li>"
                "<li>Gum inflammation and periodontal disease</li>"
                "<li>Skin infections and abscesses</li>"
                "<li>Respiratory infections (pneumonia)</li>"
                "<li>Fever may be the <em>only</em> sign in a neutropenic patient, because the suppressed inflammatory response "
                "may prevent typical infection signs (redness, pus formation) from appearing</li>"
                "</ul>"
                "<p>Fever in a neutropenic patient is treated as a medical emergency and requires immediate evaluation.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>Neutrophil evaluation is part of the CBC with differential and is interpreted alongside:</p>"
                "<ul>"
                "<li><strong>Total white blood cell count (WBC)</strong> &ndash; required for calculating the ANC.</li>"
                "<li><strong>Lymphocytes</strong> &ndash; may rise in viral infections; the neutrophil-to-lymphocyte ratio (NLR) "
                "is used as an inflammation marker.</li>"
                "<li><strong>Monocytes</strong> &ndash; may increase in chronic infections and granulomatous diseases.</li>"
                "<li><strong>Eosinophils</strong> &ndash; elevated in allergic conditions and parasitic infections.</li>"
                "<li><strong>Basophils</strong> &ndash; evaluated in rare conditions.</li>"
                "<li><strong>CRP (C-reactive protein)</strong> &ndash; a systemic inflammation marker often evaluated alongside neutrophilia.</li>"
                "<li><strong>Procalcitonin</strong> &ndash; a more specific marker for bacterial infection.</li>"
                "<li><strong>Peripheral blood smear</strong> &ndash; allows morphological assessment of neutrophils (toxic granulation, "
                "band forms, hypersegmentation).</li>"
                "</ul>"
                "<p>The combination of these tests helps narrow down the cause of abnormal neutrophil counts.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult a healthcare professional if:</p>"
                "<ul>"
                "<li>Your neutrophil count is outside the reference range</li>"
                "<li>You experience recurrent or prolonged infections</li>"
                "<li>You develop mouth ulcers, gum bleeding, or skin infections</li>"
                "<li>You are receiving chemotherapy or immunosuppressive therapy</li>"
                "</ul>"
                "<p><strong>Emergency (febrile neutropenia):</strong> If your ANC is &lt;500/&micro;L and you develop a fever of "
                "38.3°C (101°F) or higher (or sustained 38.0°C for one hour), seek emergency medical care immediately. "
                "Delayed antibiotic treatment can be life-threatening.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare for your doctor visit. Upload your blood test report at "
                "<a href=\"/analyze\">noryaai.com/analyze</a> and our AI engine automatically extracts your neutrophil absolute "
                "count and percentage, total WBC, and other leukocyte subtypes, compares them against reference ranges, "
                "and generates a clear, structured report.</p>"
                "<p>For subscription options, visit our <a href=\"/pricing\">pricing page</a>.</p>"
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
        Section(id="intro", level=2, heading="Neutrófilos altos o bajos: qué significan en tu análisis de sangre",
                body_html="<p>Los <strong>neutrófilos</strong> son el tipo más abundante de glóbulo blanco y actúan como primera línea de defensa del sistema inmunitario contra infecciones bacterianas y fúngicas. Su recuento forma parte del <strong>hemograma completo (CBC)</strong> y aporta información clave sobre infecciones, inflamación y función de la médula ósea.</p><p>Un recuento elevado se denomina <strong>neutrofilia</strong> y uno bajo <strong>neutropenia</strong>. Ambas situaciones pueden tener múltiples causas y requieren valoración clínica.</p><p>Esta guía es educativa y no sustituye el consejo médico profesional.</p>"),
        Section(id="what-are-neutrophils", level=2, heading="¿Qué son los neutrófilos?",
                body_html="<p>Los <strong>neutrófilos</strong> son granulocitos producidos en la médula ósea. Representan el 50&ndash;70% de los leucocitos circulantes y tienen una vida media de solo 5&ndash;90 horas. Combaten las infecciones mediante fagocitosis, degranulación y trampas extracelulares de neutrófilos (NETs).</p><p>Una neutropenia grave (ANC &lt;500/µL) deja al organismo vulnerable a infecciones potencialmente mortales, especialmente en pacientes que reciben quimioterapia.</p>"),
        Section(id="normal-ranges", level=2, heading="Valores normales de neutrófilos",
                body_html="<p>Los neutrófilos se expresan como recuento absoluto (ANC) y porcentaje:</p><table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Parámetro</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Rango normal</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">ANC</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">2.500&ndash;7.000 células/µL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Porcentaje</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">40&ndash;70%</td></tr></tbody></table><p>ANC = WBC &times; % neutrófilos / 100. Las decisiones clínicas se basan en el recuento absoluto. Neutropenia: leve 1.000&ndash;1.500, moderada 500&ndash;1.000, grave &lt;500/µL.</p>"),
        Section(id="high-neutrophils-causes", level=2, heading="Causas de neutrófilos altos (neutrofilia)",
                body_html="<p>Las causas más frecuentes de <strong>neutrofilia</strong> (ANC &gt;7.000/µL) incluyen: infecciones bacterianas (neumonía, ITU, celulitis), inflamación aguda (cirugía, traumatismo, infarto), respuesta al estrés (liberación de cortisol), corticosteroides, tabaquismo y trastornos mieloproliferativos (LMC, policitemia vera).</p><p>La neutrofilia es una respuesta a un proceso subyacente, no una enfermedad en sí misma.</p>"),
        Section(id="low-neutrophils-causes", level=2, heading="Causas de neutrófilos bajos (neutropenia)",
                body_html="<p>La <strong>neutropenia</strong> (ANC &lt;1.500/µL) puede deberse a: infecciones virales (gripe, VIH, hepatitis), fármacos (quimioterapia, clozapina, metamizol), neutropenia autoinmune, insuficiencia medular (anemia aplásica, mielodisplasia), sepsis grave y neutropenia étnica benigna.</p><p>La neutropenia febril (ANC &lt;500 + fiebre ≥38,3°C) es una emergencia que requiere antibióticos de amplio espectro inmediatos.</p>"),
        Section(id="absolute-vs-percentage", level=2, heading="Recuento absoluto vs. porcentaje",
                body_html="<p>El porcentaje puede ser engañoso por sí solo. Ejemplo: WBC = 3.000/µL con 60% de neutrófilos da un ANC de solo 1.800/µL, que está cerca de la neutropenia, aunque el porcentaje parezca normal. Las guías clínicas siempre usan el recuento absoluto (ANC) para tomar decisiones terapéuticas.</p>"),
        Section(id="symptoms", level=2, heading="Síntomas de alteraciones de neutrófilos",
                body_html="<p><strong>Neutrofilia:</strong> generalmente sin síntomas propios; los síntomas son los de la causa subyacente. <strong>Neutropenia:</strong> infecciones recurrentes, úlceras orales, gingivitis, infecciones cutáneas, neumonía. La fiebre puede ser el único signo en un paciente neutropénico.</p>"),
        Section(id="related-tests", level=2, heading="Pruebas relacionadas",
                body_html="<p>WBC total, linfocitos, monocitos, eosinófilos, basófilos, PCR, procalcitonina y frotis de sangre periférica. La ratio neutrófilos/linfocitos (NLR) se usa como marcador inflamatorio.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Cuándo consultar al médico",
                body_html="<p>Consulte si los neutrófilos están fuera del rango, si tiene infecciones recurrentes o si recibe quimioterapia. <strong>Urgencia:</strong> ANC &lt;500/µL con fiebre ≥38,3°C requiere atención de emergencia inmediata.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo ayuda Norya",
                body_html="<p>Suba su análisis en <a href=\"/analyze\">noryaai.com/analyze</a> y nuestra IA extraerá el ANC, el porcentaje de neutrófilos y otros subtipos leucocitarios, comparándolos con los rangos de referencia. Visite nuestra <a href=\"/pricing\">página de precios</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Neutrophile hoch oder niedrig: Was bedeutet Ihr Blutwert?",
                body_html="<p><strong>Neutrophile Granulozyten</strong> sind die häufigsten weißen Blutkörperchen und die Erstverteidiger des Immunsystems gegen bakterielle und Pilzinfektionen. Ihr Wert ist ein zentraler Bestandteil des <strong>großen Blutbilds</strong> und liefert wichtige Informationen über Infektionen, Entzündungen und die Knochenmarkfunktion.</p><p>Ein erhöhter Wert heißt <strong>Neutrophilie</strong>, ein erniedrigter <strong>Neutropenie</strong>. Beide Zustände können vielfältige Ursachen haben und erfordern ärztliche Abklärung.</p><p>Dieser Leitfaden dient der Information und ersetzt keine ärztliche Beratung.</p>"),
        Section(id="what-are-neutrophils", level=2, heading="Was sind Neutrophile?",
                body_html="<p><strong>Neutrophile</strong> sind Granulozyten aus dem Knochenmark, die 50&ndash;70% der zirkulierenden Leukozyten ausmachen. Ihre Lebensdauer beträgt nur 5&ndash;90 Stunden. Sie bekämpfen Infektionen durch Phagozytose, Degranulation und NETs (neutrophile extrazelluläre Fallen).</p><p>Schwere Neutropenie (ANC &lt;500/µL) hinterlässt den Körper anfällig für lebensbedrohliche Infektionen.</p>"),
        Section(id="normal-ranges", level=2, heading="Normale Neutrophilen-Werte",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Parameter</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Normalbereich</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">ANC</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">2.500&ndash;7.000 Zellen/µL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Neutrophile %</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">40&ndash;70%</td></tr></tbody></table><p>ANC = WBC &times; Neutrophile % / 100. Neutropenie-Grade: leicht 1.000&ndash;1.500, mäßig 500&ndash;1.000, schwer &lt;500/µL.</p>"),
        Section(id="high-neutrophils-causes", level=2, heading="Ursachen für erhöhte Neutrophile (Neutrophilie)",
                body_html="<p>Häufige Ursachen: bakterielle Infektionen, akute Entzündung (postoperativ, Trauma), Stressreaktion, Kortikosteroide, Rauchen und myeloproliferative Erkrankungen (CML, Polycythaemia vera).</p><p>Neutrophilie ist eine Reaktion auf einen zugrunde liegenden Prozess.</p>"),
        Section(id="low-neutrophils-causes", level=2, heading="Ursachen für niedrige Neutrophile (Neutropenie)",
                body_html="<p>Häufige Ursachen: Virusinfektionen, Medikamente (Chemotherapie, Clozapin, Metamizol), Autoimmun-Neutropenie, Knochenmarkversagen, schwere Sepsis und benigne ethnische Neutropenie. Febrile Neutropenie (ANC &lt;500 + Fieber ≥38,3°C) ist ein Notfall.</p>"),
        Section(id="absolute-vs-percentage", level=2, heading="Absoluter Wert vs. Prozentsatz",
                body_html="<p>Der Prozentsatz allein kann irreführend sein. Beispiel: WBC = 3.000/µL bei 60% Neutrophilen ergibt einen ANC von nur 1.800/µL. Klinische Entscheidungen basieren stets auf dem absoluten Wert.</p>"),
        Section(id="symptoms", level=2, heading="Symptome",
                body_html="<p><strong>Neutrophilie:</strong> meist keine eigenen Symptome. <strong>Neutropenie:</strong> rezidivierende Infektionen, Mundulzera, Gingivitis, Hautinfektionen. Fieber kann das einzige Zeichen sein.</p>"),
        Section(id="related-tests", level=2, heading="Verwandte Untersuchungen",
                body_html="<p>Gesamt-WBC, Lymphozyten, Monozyten, Eosinophile, Basophile, CRP, Procalcitonin und peripherer Blutausstrich. Der Neutrophilen-Lymphozyten-Quotient (NLR) wird als Entzündungsmarker verwendet.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann zum Arzt?",
                body_html="<p>Suchen Sie einen Arzt auf bei Neutrophilen außerhalb des Referenzbereichs, wiederkehrenden Infektionen oder unter Chemotherapie. <strong>Notfall:</strong> ANC &lt;500/µL mit Fieber ≥38,3°C erfordert sofortige Notfallbehandlung.</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie Norya hilft",
                body_html="<p>Laden Sie Ihren Befund unter <a href=\"/analyze\">noryaai.com/analyze</a> hoch. Unsere KI extrahiert ANC, Neutrophilen-%, Gesamt-WBC und weitere Leukozyten-Subtypen. <a href=\"/pricing\">Preisseite</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Polynucléaires neutrophiles : que signifie un taux élevé ou bas ?",
                body_html="<p>Les <strong>polynucléaires neutrophiles</strong> (PNN) sont les globules blancs les plus abondants et constituent la première ligne de défense de l&rsquo;organisme contre les infections bactériennes et fongiques. Leur numération fait partie de la <strong>NFS (numération formule sanguine)</strong> et fournit des informations essentielles sur l&rsquo;infection, l&rsquo;inflammation et la moelle osseuse.</p><p>Un taux élevé est appelé <strong>neutrophilie</strong>, un taux bas <strong>neutropénie</strong>. Les deux nécessitent une évaluation médicale.</p><p>Ce guide est informatif et ne remplace pas un avis médical.</p>"),
        Section(id="what-are-neutrophils", level=2, heading="Que sont les neutrophiles ?",
                body_html="<p>Les <strong>neutrophiles</strong> sont des granulocytes produits par la moelle osseuse, représentant 50&ndash;70% des leucocytes circulants. Durée de vie : 5&ndash;90 heures. Mécanismes de défense : phagocytose, dégranulation et NETs (pièges extracellulaires). Une neutropénie sévère (PNN &lt;500/µL) expose à des infections graves.</p>"),
        Section(id="normal-ranges", level=2, heading="Valeurs normales des neutrophiles",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Paramètre</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Valeur normale</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">PNN absolus</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">2 500&ndash;7 000/µL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Pourcentage</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">40&ndash;70%</td></tr></tbody></table><p>PNN = GB &times; % neutrophiles / 100. Neutropénie : légère 1 000&ndash;1 500, modérée 500&ndash;1 000, sévère &lt;500/µL.</p>"),
        Section(id="high-neutrophils-causes", level=2, heading="Causes de neutrophiles élevés (neutrophilie)",
                body_html="<p>Causes fréquentes : infections bactériennes, inflammation aiguë, stress, corticoïdes, tabagisme et syndromes myéloprolifératifs (LMC, polyglobulie de Vaquez). La neutrophilie est une réponse à un processus sous-jacent.</p>"),
        Section(id="low-neutrophils-causes", level=2, heading="Causes de neutrophiles bas (neutropénie)",
                body_html="<p>Causes : infections virales, médicaments (chimiothérapie, clozapine, métamizole), neutropénie auto-immune, insuffisance médullaire, sepsis sévère et neutropénie ethnique bénigne. La neutropénie fébrile (PNN &lt;500 + fièvre ≥38,3°C) est une urgence.</p>"),
        Section(id="absolute-vs-percentage", level=2, heading="Valeur absolue vs. pourcentage",
                body_html="<p>Le pourcentage seul peut induire en erreur. Exemple : GB = 3 000/µL avec 60% PNN = 1 800/µL (quasi neutropénie). Les décisions cliniques reposent toujours sur la valeur absolue.</p>"),
        Section(id="symptoms", level=2, heading="Symptômes",
                body_html="<p><strong>Neutrophilie :</strong> pas de symptômes propres. <strong>Neutropénie :</strong> infections récurrentes, aphtes, gingivite, infections cutanées. La fièvre peut être le seul signe chez un patient neutropénique.</p>"),
        Section(id="related-tests", level=2, heading="Examens associés",
                body_html="<p>GB totaux, lymphocytes, monocytes, éosinophiles, basophiles, CRP, procalcitonine et frottis sanguin. Le rapport neutrophiles/lymphocytes (NLR) est un marqueur inflammatoire.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter ?",
                body_html="<p>Consultez si les PNN sont hors des valeurs de référence ou en cas d&rsquo;infections récurrentes. <strong>Urgence :</strong> PNN &lt;500/µL + fièvre ≥38,3°C nécessite une prise en charge urgente.</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment Norya peut vous aider",
                body_html="<p>Téléchargez votre bilan sur <a href=\"/analyze\">noryaai.com/analyze</a>. Notre IA extraira PNN absolus, pourcentage et autres sous-types leucocytaires. <a href=\"/pricing\">Page tarifs</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Neutrofili alti o bassi: cosa significano nel tuo esame del sangue",
                body_html="<p>I <strong>neutrofili</strong> sono i globuli bianchi più abbondanti e rappresentano la prima linea di difesa contro le infezioni batteriche e fungine. Il loro valore è parte integrante dell&rsquo;<strong>emocromo completo</strong> e fornisce informazioni fondamentali su infezioni, infiammazione e funzione midollare.</p><p>Un valore elevato è detto <strong>neutrofilia</strong>, uno basso <strong>neutropenia</strong>. Entrambi richiedono valutazione medica.</p><p>Questa guida è informativa e non sostituisce il parere medico.</p>"),
        Section(id="what-are-neutrophils", level=2, heading="Cosa sono i neutrofili?",
                body_html="<p>I <strong>neutrofili</strong> sono granulociti prodotti dal midollo osseo, pari al 50&ndash;70% dei leucociti circolanti. Durata di vita: 5&ndash;90 ore. Meccanismi: fagocitosi, degranulazione e NETs. La neutropenia grave (ANC &lt;500/µL) espone a infezioni potenzialmente letali.</p>"),
        Section(id="normal-ranges", level=2, heading="Valori normali dei neutrofili",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Parametro</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Intervallo normale</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">ANC</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">2.500&ndash;7.000 cellule/µL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Percentuale</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">40&ndash;70%</td></tr></tbody></table><p>ANC = WBC &times; % neutrofili / 100. Neutropenia: lieve 1.000&ndash;1.500, moderata 500&ndash;1.000, grave &lt;500/µL.</p>"),
        Section(id="high-neutrophils-causes", level=2, heading="Cause di neutrofili alti (neutrofilia)",
                body_html="<p>Cause comuni: infezioni batteriche, infiammazione acuta, stress, corticosteroidi, fumo e disordini mieloproliferativi (LMC, policitemia vera). La neutrofilia è una risposta a un processo sottostante.</p>"),
        Section(id="low-neutrophils-causes", level=2, heading="Cause di neutrofili bassi (neutropenia)",
                body_html="<p>Cause: infezioni virali, farmaci (chemioterapia, clozapina, metamizolo), neutropenia autoimmune, insufficienza midollare, sepsi grave e neutropenia etnica benigna. La neutropenia febbrile (ANC &lt;500 + febbre ≥38,3°C) è un&rsquo;emergenza.</p>"),
        Section(id="absolute-vs-percentage", level=2, heading="Conta assoluta vs. percentuale",
                body_html="<p>La percentuale da sola può trarre in inganno. Esempio: WBC = 3.000/µL con 60% neutrofili = ANC 1.800/µL (quasi neutropenia). Le decisioni cliniche si basano sempre sul valore assoluto.</p>"),
        Section(id="symptoms", level=2, heading="Sintomi",
                body_html="<p><strong>Neutrofilia:</strong> generalmente asintomatica. <strong>Neutropenia:</strong> infezioni ricorrenti, afte orali, gengivite, infezioni cutanee. La febbre può essere l&rsquo;unico segno nel paziente neutropenico.</p>"),
        Section(id="related-tests", level=2, heading="Esami correlati",
                body_html="<p>WBC totali, linfociti, monociti, eosinofili, basofili, PCR, procalcitonina e striscio di sangue periferico. Il rapporto neutrofili/linfociti (NLR) è un marcatore infiammatorio.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico",
                body_html="<p>Consultate il medico se i neutrofili sono fuori intervallo, se avete infezioni ricorrenti o se ricevete chemioterapia. <strong>Emergenza:</strong> ANC &lt;500/µL con febbre ≥38,3°C richiede intervento immediato.</p>"),
        Section(id="how-norya-helps", level=2, heading="Come Norya può aiutarti",
                body_html="<p>Caricate il vostro esame su <a href=\"/analyze\">noryaai.com/analyze</a>. La nostra IA estrarrà ANC, percentuale di neutrofili e altri sottotipi leucocitari. <a href=\"/pricing\">Pagina prezzi</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="נויטרופילים: מה המשמעות של ערך גבוה או נמוך?",
                body_html="<p><strong>נויטרופילים</strong> הם תאי הדם הלבנים הנפוצים ביותר ומהווים קו ההגנה הראשון של מערכת החיסון נגד זיהומים חיידקיים ופטרייתיים. ספירתם היא חלק מ<strong>ספירת דם מלאה (CBC)</strong> ומספקת מידע חיוני על זיהומים, דלקת ותפקוד מח העצם.</p><p>ספירה גבוהה נקראת <strong>נויטרופיליה</strong>, נמוכה <strong>נויטרופניה</strong>. שני המצבים דורשים הערכה רפואית.</p><p>מדריך זה חינוכי בלבד ואינו מחליף ייעוץ רפואי.</p>"),
        Section(id="what-are-neutrophils", level=2, heading="מהם נויטרופילים?",
                body_html="<p><strong>נויטרופילים</strong> הם גרנולוציטים המיוצרים במח העצם, המהווים 50&ndash;70% מהלויקוציטים. אורך חייהם 5&ndash;90 שעות בלבד. מנגנוני לחימה: פגוציטוזה, דגרנולציה ו-NETs. נויטרופניה חמורה (ANC &lt;500/µL) חושפת לזיהומים מסכני חיים.</p>"),
        Section(id="normal-ranges", level=2, heading="טווחי נויטרופילים תקינים",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">פרמטר</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">טווח תקין</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">ANC</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">2,500&ndash;7,000 תאים/µL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">אחוז</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">40&ndash;70%</td></tr></tbody></table><p>ANC = WBC &times; % נויטרופילים / 100. דרגות נויטרופניה: קלה 1,000&ndash;1,500, בינונית 500&ndash;1,000, חמורה &lt;500/µL.</p>"),
        Section(id="high-neutrophils-causes", level=2, heading="גורמים לנויטרופילים גבוהים",
                body_html="<p>גורמים: זיהומים חיידקיים, דלקת חריפה, סטרס, קורטיקוסטרואידים, עישון והפרעות מיאלופרוליפרטיביות (CML, פוליציתמיה ורה). נויטרופיליה היא תגובה לתהליך בסיסי.</p>"),
        Section(id="low-neutrophils-causes", level=2, heading="גורמים לנויטרופילים נמוכים",
                body_html="<p>גורמים: זיהומים ויראליים, תרופות (כימותרפיה, קלוזפין, מטמיזול), נויטרופניה אוטואימונית, כשל מח עצם, אלח דם חמור ונויטרופניה אתנית שפירה. נויטרופניה חום (ANC &lt;500 + חום ≥38.3°C) היא מצב חירום.</p>"),
        Section(id="absolute-vs-percentage", level=2, heading="ספירה מוחלטת לעומת אחוז",
                body_html="<p>האחוז לבדו עלול להטעות. דוגמה: WBC = 3,000/µL עם 60% נויטרופילים = ANC 1,800/µL בלבד (קרוב לנויטרופניה). ההחלטות הקליניות מבוססות תמיד על הספירה המוחלטת.</p>"),
        Section(id="symptoms", level=2, heading="תסמינים",
                body_html="<p><strong>נויטרופיליה:</strong> ללא תסמינים ייחודיים בדרך כלל. <strong>נויטרופניה:</strong> זיהומים חוזרים, אפטות בפה, דלקת חניכיים, זיהומי עור. חום עשוי להיות הסימן היחיד בחולה נויטרופני.</p>"),
        Section(id="related-tests", level=2, heading="בדיקות קשורות",
                body_html="<p>WBC כולל, לימפוציטים, מונוציטים, אאוזינופילים, בזופילים, CRP, פרוקלציטונין ומשטח דם היקפי. יחס נויטרופילים/לימפוציטים (NLR) משמש כסמן דלקתי.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא?",
                body_html="<p>פנו לרופא אם הנויטרופילים מחוץ לטווח או בזיהומים חוזרים. <strong>חירום:</strong> ANC &lt;500/µL עם חום ≥38.3°C דורש טיפול חירום מיידי.</p>"),
        Section(id="how-norya-helps", level=2, heading="איך Norya עוזרת",
                body_html="<p>העלו את בדיקת הדם ב-<a href=\"/analyze\">noryaai.com/analyze</a>. ה-AI שלנו יחלץ ANC, אחוז נויטרופילים ותתי-סוגי לויקוציטים נוספים. <a href=\"/pricing\">עמוד תמחור</a>.</p>"),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="न्यूट्रोफिल उच्च या निम्न: आपकी रक्त जाँच का क्या मतलब है?",
                body_html="<p><strong>न्यूट्रोफिल</strong> सबसे प्रचुर प्रकार की श्वेत रक्त कोशिकाएँ हैं और बैक्टीरियल तथा फंगल संक्रमणों के खिलाफ प्रतिरक्षा प्रणाली की पहली पंक्ति हैं। इनकी गिनती <strong>कम्प्लीट ब्लड काउंट (CBC)</strong> का अभिन्न हिस्सा है।</p><p>बढ़ी हुई गिनती को <strong>न्यूट्रोफिलिया</strong>, कम गिनती को <strong>न्यूट्रोपेनिया</strong> कहते हैं। दोनों स्थितियाँ चिकित्सा मूल्यांकन की माँग करती हैं।</p><p>यह गाइड शैक्षणिक है और चिकित्सा सलाह का विकल्प नहीं है।</p>"),
        Section(id="what-are-neutrophils", level=2, heading="न्यूट्रोफिल क्या हैं?",
                body_html="<p><strong>न्यूट्रोफिल</strong> अस्थि मज्जा में बनने वाले ग्रैनुलोसाइट्स हैं जो परिसंचारी श्वेत रक्त कोशिकाओं का 50&ndash;70% हिस्सा हैं। उनका जीवनकाल केवल 5&ndash;90 घंटे है। वे फैगोसाइटोसिस, डीग्रैनुलेशन और NETs द्वारा संक्रमण से लड़ते हैं। गंभीर न्यूट्रोपेनिया (ANC &lt;500/µL) जानलेवा संक्रमणों का खतरा बढ़ाती है।</p>"),
        Section(id="normal-ranges", level=2, heading="सामान्य न्यूट्रोफिल मान",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">पैरामीटर</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">सामान्य सीमा</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">ANC</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">2,500&ndash;7,000 कोशिकाएँ/µL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">प्रतिशत</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">40&ndash;70%</td></tr></tbody></table><p>ANC = WBC &times; न्यूट्रोफिल % / 100। न्यूट्रोपेनिया: हल्की 1,000&ndash;1,500, मध्यम 500&ndash;1,000, गंभीर &lt;500/µL।</p>"),
        Section(id="high-neutrophils-causes", level=2, heading="उच्च न्यूट्रोफिल (न्यूट्रोफिलिया) के कारण",
                body_html="<p>मुख्य कारण: बैक्टीरियल संक्रमण, तीव्र सूजन, तनाव, कॉर्टिकोस्टेरॉइड, धूम्रपान और माइलोप्रोलिफ़ेरेटिव विकार (CML, पॉलीसाइथेमिया वेरा)। न्यूट्रोफिलिया अपने आप में रोग नहीं बल्कि अंतर्निहित प्रक्रिया की प्रतिक्रिया है।</p>"),
        Section(id="low-neutrophils-causes", level=2, heading="कम न्यूट्रोफिल (न्यूट्रोपेनिया) के कारण",
                body_html="<p>कारण: वायरल संक्रमण, दवाएँ (कीमोथेरेपी, क्लोज़ापिन, मेटामिज़ोल), ऑटोइम्यून न्यूट्रोपेनिया, अस्थि मज्जा विफलता, गंभीर सेप्सिस और बिनाइन एथनिक न्यूट्रोपेनिया। ज्वर-संबंधी न्यूट्रोपेनिया (ANC &lt;500 + बुखार ≥38.3°C) आपातकालीन स्थिति है।</p>"),
        Section(id="absolute-vs-percentage", level=2, heading="मुतलक़ गिनती (ANC) बनाम प्रतिशत",
                body_html="<p>अकेले प्रतिशत भ्रामक हो सकता है। उदाहरण: WBC = 3,000/µL और न्यूट्रोफिल 60% = ANC केवल 1,800/µL (लगभग न्यूट्रोपेनिया)। चिकित्सा निर्णय हमेशा मुतलक़ गिनती पर आधारित होते हैं।</p>"),
        Section(id="symptoms", level=2, heading="लक्षण",
                body_html="<p><strong>न्यूट्रोफिलिया:</strong> आमतौर पर स्वयं के लक्षण नहीं। <strong>न्यूट्रोपेनिया:</strong> बार-बार संक्रमण, मुँह के छाले, मसूड़ों की सूजन, त्वचा संक्रमण। न्यूट्रोपेनिक रोगी में बुखार एकमात्र संकेत हो सकता है।</p>"),
        Section(id="related-tests", level=2, heading="संबंधित परीक्षण",
                body_html="<p>कुल WBC, लिम्फोसाइट्स, मोनोसाइट्स, इओसिनोफिल्स, बेसोफिल्स, CRP, प्रोकैल्सीटोनिन और पेरिफ़ेरल ब्लड स्मीयर। NLR (न्यूट्रोफिल-लिम्फोसाइट अनुपात) सूजन मार्कर के रूप में उपयोग होता है।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें?",
                body_html="<p>डॉक्टर से मिलें यदि न्यूट्रोफिल सामान्य सीमा से बाहर हैं या बार-बार संक्रमण हो। <strong>आपातकाल:</strong> ANC &lt;500/µL और बुखार ≥38.3°C में तुरंत आपातकालीन चिकित्सा लें।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya कैसे मदद करता है",
                body_html="<p>अपनी रक्त रिपोर्ट <a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें। हमारा AI ANC, न्यूट्रोफिल % और अन्य ल्यूकोसाइट उपप्रकार निकालेगा। <a href=\"/pricing\">मूल्य निर्धारण पृष्ठ</a>।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="العدلات (النيوتروفيل): ماذا يعني ارتفاعها أو انخفاضها؟",
                body_html="<p><strong>العدلات (النيوتروفيل)</strong> هي أكثر أنواع كريات الدم البيضاء شيوعاً وتمثّل خط الدفاع الأول لجهاز المناعة ضد العدوى البكتيرية والفطرية. تعدادها جزء أساسي من <strong>تعداد الدم الكامل (CBC)</strong>.</p><p>الارتفاع يُسمى <strong>كثرة العدلات</strong> والانخفاض <strong>قلة العدلات</strong>. كلا الحالتين يتطلبان تقييماً طبياً.</p><p>هذا الدليل تثقيفي ولا يحل محل الاستشارة الطبية.</p>"),
        Section(id="what-are-neutrophils", level=2, heading="ما هي العدلات؟",
                body_html="<p><strong>العدلات</strong> خلايا حبيبية تُنتج في نخاع العظم وتشكّل 50&ndash;70% من الكريات البيضاء الدائرة. عمرها 5&ndash;90 ساعة فقط. تقاوم العدوى بالبلعمة وإفراز الحبيبات وشبكات NET. قلة العدلات الشديدة (ANC &lt;500/µL) تعرّض لعدوى مهددة للحياة.</p>"),
        Section(id="normal-ranges", level=2, heading="المعدلات الطبيعية للعدلات",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">المعيار</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">الطبيعي</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">ANC</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">2,500&ndash;7,000 خلية/µL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">النسبة المئوية</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">40&ndash;70%</td></tr></tbody></table><p>ANC = WBC &times; % العدلات / 100. قلة العدلات: خفيفة 1,000&ndash;1,500، متوسطة 500&ndash;1,000، شديدة &lt;500/µL.</p>"),
        Section(id="high-neutrophils-causes", level=2, heading="أسباب ارتفاع العدلات",
                body_html="<p>الأسباب: عدوى بكتيرية، التهاب حاد، إجهاد، كورتيكوستيرويدات، تدخين واضطرابات تكاثرية نقيية (CML، كثرة الحمر الحقيقية). كثرة العدلات استجابة لعملية أساسية.</p>"),
        Section(id="low-neutrophils-causes", level=2, heading="أسباب انخفاض العدلات",
                body_html="<p>الأسباب: عدوى فيروسية، أدوية (كيماوي، كلوزابين، ميتاميزول)، قلة عدلات مناعية ذاتية، فشل نخاع العظم، إنتان شديد وقلة عدلات عرقية حميدة. قلة العدلات الحموية (ANC &lt;500 + حرارة ≥38.3°C) حالة طوارئ.</p>"),
        Section(id="absolute-vs-percentage", level=2, heading="العدد المطلق مقابل النسبة المئوية",
                body_html="<p>النسبة وحدها قد تكون مضللة. مثال: WBC = 3,000/µL مع 60% عدلات = ANC 1,800/µL فقط (قرب قلة العدلات). القرارات السريرية تعتمد دائماً على العدد المطلق.</p>"),
        Section(id="symptoms", level=2, heading="الأعراض",
                body_html="<p><strong>كثرة العدلات:</strong> عادةً بلا أعراض خاصة. <strong>قلة العدلات:</strong> عدوى متكررة، تقرحات فموية، التهاب لثة، عدوى جلدية. الحمى قد تكون العلامة الوحيدة.</p>"),
        Section(id="related-tests", level=2, heading="فحوصات ذات صلة",
                body_html="<p>WBC الكلي، لمفاويات، وحيدات، حمضات، قاعدات، CRP، بروكالسيتونين ومسحة دم محيطية. نسبة العدلات/اللمفاويات (NLR) تُستخدم كمؤشر التهابي.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى تراجع الطبيب؟",
                body_html="<p>راجع الطبيب إذا كانت العدلات خارج النطاق أو عند عدوى متكررة. <strong>طوارئ:</strong> ANC &lt;500/µL مع حرارة ≥38.3°C يتطلب علاجاً طارئاً فورياً.</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف تساعدك Norya",
                body_html="<p>ارفع تقريرك على <a href=\"/analyze\">noryaai.com/analyze</a> وسيستخرج الذكاء الاصطناعي ANC ونسبة العدلات وأنواع الكريات البيضاء الأخرى. <a href=\"/pricing\">صفحة الأسعار</a>.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ============================================================================
# Public API
# ============================================================================

def get_neutrophils_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for neutrophils article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_neutrophils_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for neutrophils article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal neutrophil count?",
             "answer": "The normal absolute neutrophil count (ANC) is 2,500–7,000 cells/µL, representing 40–70% of total white blood cells. Clinical decisions are based on the absolute count, not the percentage."},
            {"question": "What causes high neutrophils?",
             "answer": "Common causes include bacterial infections, acute inflammation (surgery, trauma), physiological stress, corticosteroid medications, smoking, and myeloproliferative disorders such as chronic myeloid leukaemia."},
            {"question": "What causes low neutrophils?",
             "answer": "Causes include viral infections, medications (especially chemotherapy), autoimmune neutropenia, bone marrow failure, severe sepsis, and benign ethnic neutropenia. Severe neutropenia (ANC < 500) increases infection risk dramatically."},
            {"question": "What is febrile neutropenia?",
             "answer": "Febrile neutropenia is a medical emergency defined as fever ≥38.3°C (or sustained ≥38.0°C for one hour) in a patient with ANC < 500/µL. It requires immediate broad-spectrum antibiotic treatment."},
            {"question": "What is the difference between absolute neutrophil count and percentage?",
             "answer": "The percentage shows the proportion of WBCs that are neutrophils, while the absolute count (ANC) is the actual number per microlitre. ANC is clinically more reliable because the percentage can be misleading when total WBC is abnormal."},
        ],
        "tr": [
            {"question": "Normal nötrofil sayısı nedir?",
             "answer": "Normal ANC 2.500–7.000 hücre/µL, toplam WBC'nin %40–70'idir. Klinik kararlar mutlak sayıya göre verilir."},
            {"question": "Nötrofil yüksekliğinin nedenleri nelerdir?",
             "answer": "Bakteriyel enfeksiyonlar, akut inflamasyon, stres, kortikosteroidler, sigara ve miyeloproliferatif hastalıklar (KML) başlıca nedenlerdir."},
            {"question": "Nötrofil düşüklüğünün nedenleri nelerdir?",
             "answer": "Viral enfeksiyonlar, ilaçlar (kemoterapi), otoimmün nötropeni, kemik iliği yetmezliği, ağır sepsis ve benign etnik nötropeni."},
            {"question": "Febril nötropeni nedir?",
             "answer": "ANC <500/µL olan hastada 38,3°C ve üzeri ateş. Acil geniş spektrumlu antibiyotik gerektirir."},
        ],
        "es": [
            {"question": "¿Cuál es el recuento normal de neutrófilos?",
             "answer": "ANC normal: 2.500–7.000 células/µL (40–70% del total de leucocitos). Las decisiones clínicas se basan en el recuento absoluto."},
            {"question": "¿Qué causa neutrófilos altos?",
             "answer": "Infecciones bacterianas, inflamación aguda, estrés, corticosteroides, tabaquismo y trastornos mieloproliferativos."},
            {"question": "¿Qué es la neutropenia febril?",
             "answer": "Fiebre ≥38,3°C con ANC <500/µL. Es una emergencia que requiere antibióticos inmediatos."},
        ],
        "de": [
            {"question": "Was ist eine normale Neutrophilenzahl?",
             "answer": "Normaler ANC: 2.500–7.000 Zellen/µL (40–70% der Gesamt-WBC). Klinische Entscheidungen basieren auf dem absoluten Wert."},
            {"question": "Was verursacht erhöhte Neutrophile?",
             "answer": "Bakterielle Infektionen, akute Entzündung, Stress, Kortikosteroide, Rauchen und myeloproliferative Erkrankungen."},
            {"question": "Was ist febrile Neutropenie?",
             "answer": "Fieber ≥38,3°C bei ANC <500/µL. Ein Notfall, der sofortige Breitspektrum-Antibiotika erfordert."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de neutrophiles ?",
             "answer": "PNN normal : 2 500–7 000/µL (40–70% des GB). Les décisions cliniques reposent sur la valeur absolue."},
            {"question": "Quelles sont les causes de neutrophiles élevés ?",
             "answer": "Infections bactériennes, inflammation aiguë, stress, corticoïdes, tabagisme et syndromes myéloprolifératifs."},
            {"question": "Qu'est-ce que la neutropénie fébrile ?",
             "answer": "Fièvre ≥38,3°C avec PNN <500/µL. Urgence nécessitant des antibiotiques à large spectre immédiats."},
        ],
        "it": [
            {"question": "Qual è la conta normale dei neutrofili?",
             "answer": "ANC normale: 2.500–7.000 cellule/µL (40–70% dei WBC totali). Le decisioni cliniche si basano sul valore assoluto."},
            {"question": "Cosa causa i neutrofili alti?",
             "answer": "Infezioni batteriche, infiammazione acuta, stress, corticosteroidi, fumo e disordini mieloproliferativi."},
            {"question": "Cos'è la neutropenia febbrile?",
             "answer": "Febbre ≥38,3°C con ANC <500/µL. Un'emergenza che richiede antibiotici ad ampio spettro immediati."},
        ],
        "he": [
            {"question": "מהי ספירת נויטרופילים תקינה?",
             "answer": "ANC תקין: 2,500–7,000 תאים/µL (40–70% מסך הלויקוציטים). החלטות קליניות מבוססות על הספירה המוחלטת."},
            {"question": "מה גורם לנויטרופילים גבוהים?",
             "answer": "זיהומים חיידקיים, דלקת חריפה, סטרס, קורטיקוסטרואידים, עישון והפרעות מיאלופרוליפרטיביות."},
            {"question": "מהי נויטרופניה חום?",
             "answer": "חום ≥38.3°C עם ANC <500/µL. מצב חירום הדורש אנטיביוטיקה רחבת טווח מיידית."},
        ],
        "hi": [
            {"question": "सामान्य न्यूट्रोफिल गिनती कितनी होनी चाहिए?",
             "answer": "सामान्य ANC: 2,500–7,000 कोशिकाएँ/µL (कुल WBC का 40–70%)। चिकित्सा निर्णय मुतलक़ गिनती पर आधारित होते हैं।"},
            {"question": "न्यूट्रोफिल बढ़ने के कारण क्या हैं?",
             "answer": "बैक्टीरियल संक्रमण, तीव्र सूजन, तनाव, कॉर्टिकोस्टेरॉइड, धूम्रपान और माइलोप्रोलिफ़ेरेटिव विकार।"},
            {"question": "फ़ेब्राइल न्यूट्रोपेनिया क्या है?",
             "answer": "ANC <500/µL वाले रोगी में बुखार ≥38.3°C। यह आपातकालीन स्थिति है जिसमें तुरंत व्यापक स्पेक्ट्रम एंटीबायोटिक चाहिए।"},
        ],
        "ar": [
            {"question": "ما هو العدد الطبيعي للعدلات؟",
             "answer": "ANC الطبيعي: 2,500–7,000 خلية/µL (40–70% من مجموع الكريات البيضاء). القرارات السريرية تعتمد على العدد المطلق."},
            {"question": "ما أسباب ارتفاع العدلات؟",
             "answer": "عدوى بكتيرية، التهاب حاد، إجهاد، كورتيكوستيرويدات، تدخين واضطرابات تكاثرية نقيية."},
            {"question": "ما هي قلة العدلات الحموية؟",
             "answer": "حمى ≥38.3°C مع ANC <500/µL. حالة طوارئ تتطلب مضادات حيوية واسعة الطيف فورية."},
        ],
    }
