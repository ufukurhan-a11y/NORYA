# -*- coding: utf-8 -*-
"""
Neutrophils high or low blog article — full body content for all 9 languages.
Used by blog_i18n._article_neutrophils().
Sections: intro, what-are-neutrophils, normal-ranges, high-neutrophils-causes,
low-neutrophils-causes, absolute-vs-percentage, symptoms, related-tests,
when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="Neutrophils high or low: understanding your white blood cell differential",
            body_html=(
                "<p>When your complete blood count (CBC) includes a white blood cell differential, neutrophils are usually the first line your eyes land on. "
                "They are the most abundant type of white blood cell, and shifts in their number&mdash;up or down&mdash;can signal everything from a common bacterial infection "
                "to medication side effects. But a single neutrophil count, like any lab value, needs context to be meaningful.</p>"
                "<p>This guide explains what neutrophils are, how to read the reference ranges on your report, the most common reasons for high or low counts, "
                "and when you should involve a healthcare professional. It is intended for education, not diagnosis&mdash;always discuss your results with a doctor.</p>"
            ),
        ),
        Section(
            id="what-are-neutrophils", level=2,
            heading="What are neutrophils and what do they do?",
            body_html=(
                "<p><strong>Neutrophils</strong> are a type of granulocyte&mdash;a white blood cell that contains tiny granules filled with enzymes capable of destroying bacteria and fungi. "
                "They are produced in the bone marrow and released into the bloodstream, where they circulate for only 6&ndash;12&nbsp;hours before migrating into tissues. "
                "Despite their short lifespan, they are the immune system&rsquo;s rapid-response force: the first cells to arrive at the site of an infection or injury.</p>"
                "<p>Neutrophils work by engulfing (phagocytosing) pathogens and releasing antimicrobial substances. "
                "They also form neutrophil extracellular traps (NETs)&mdash;web-like structures of DNA and proteins that physically snare bacteria. "
                "Because they are so central to innate immunity, a significant drop in their number leaves the body vulnerable to infections, "
                "while a dramatic rise usually indicates the immune system is actively fighting something.</p>"
                "<p>On a lab report, neutrophils may appear as &ldquo;Neutrophils (Absolute)&rdquo; or &ldquo;Neut %&rdquo; (percentage of total WBC). "
                "Both values are important; the absolute count is generally considered more clinically useful because it is not influenced by changes in other cell types.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal neutrophil ranges",
            body_html=(
                "<p>Reference ranges vary between laboratories and populations. The values below are widely used in adults. "
                "Always compare your result with the range printed on <em>your</em> report.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parameter</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typical adult range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Absolute neutrophil count (ANC)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,500&ndash;7,000 cells/&mu;L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neutrophil percentage</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70 % of total WBC</td></tr>'
                "</tbody></table>"
                "<p>Some ethnic groups, particularly people of African, Middle Eastern, or Caribbean descent, may have a lower baseline neutrophil count "
                "(a benign condition called <strong>benign ethnic neutropenia</strong>). Children&rsquo;s ranges differ from adults and change with age. "
                "Pregnancy can also raise the neutrophil count physiologically.</p>"
            ),
        ),
        Section(
            id="high-neutrophils-causes", level=2,
            heading="Causes of high neutrophils (neutrophilia)",
            body_html=(
                "<p>A neutrophil count above the upper reference limit is called <strong>neutrophilia</strong>. "
                "The most common trigger is <strong>bacterial infection</strong>: when bacteria invade, the bone marrow ramps up production and the spleen and blood vessel walls "
                "release stored neutrophils into the circulation. Urinary tract infections, pneumonia, skin infections, and abscesses are classic examples.</p>"
                "<p><strong>Acute inflammation</strong> from non-infectious causes&mdash;surgery, trauma, burns, myocardial infarction, or autoimmune flares&mdash;can also elevate neutrophils. "
                "<strong>Physiological stress</strong> (intense exercise, emotional distress, pain) produces a short-lived &ldquo;stress leukocytosis&rdquo; driven mainly by neutrophils. "
                "<strong>Corticosteroids</strong> are a well-known pharmacological cause: they reduce neutrophil migration from blood into tissues, artificially raising the circulating count.</p>"
                "<p><strong>Smoking</strong> chronically raises neutrophils through low-grade airway inflammation. "
                "Less commonly, persistent or very high neutrophilia may point to <strong>myeloproliferative neoplasms</strong> (e.g.&nbsp;chronic myeloid leukaemia) "
                "or other bone marrow disorders. Your doctor will consider the degree of elevation, the trend over time, and the overall clinical picture.</p>"
            ),
        ),
        Section(
            id="low-neutrophils-causes", level=2,
            heading="Causes of low neutrophils (neutropenia)",
            body_html=(
                "<p>A neutrophil count below 2,500&nbsp;cells/&mu;L is called <strong>neutropenia</strong>. Severity matters: mild neutropenia (1,000&ndash;2,500) is often clinically benign, "
                "while severe neutropenia (&lt;&nbsp;500) significantly increases infection risk. "
                "The most common cause in everyday practice is <strong>viral infection</strong>&mdash;influenza, hepatitis, HIV, EBV, and many other viruses can temporarily suppress neutrophil production or increase their consumption.</p>"
                "<p><strong>Medications</strong> are another frequent cause. Chemotherapy drugs are the best-known example, but antibiotics (e.g.&nbsp;trimethoprim-sulfamethoxazole), "
                "anticonvulsants (e.g.&nbsp;carbamazepine), antithyroid medications (e.g.&nbsp;methimazole), and some anti-inflammatory agents can all lower neutrophils. "
                "Drug-induced neutropenia is usually reversible once the offending medication is stopped.</p>"
                "<p><strong>Autoimmune neutropenia</strong> occurs when the body produces antibodies against its own neutrophils. "
                "<strong>Nutritional deficiencies</strong> (B12, folate, copper) can impair production. "
                "<strong>Severe infections</strong> (sepsis) can paradoxically lower neutrophils by consuming them faster than the marrow can replace them. "
                "Inherited conditions like <strong>cyclic neutropenia</strong> and <strong>severe congenital neutropenia</strong> are rare but important in paediatric settings.</p>"
            ),
        ),
        Section(
            id="absolute-vs-percentage", level=2,
            heading="Absolute count vs. percentage: which matters more?",
            body_html=(
                "<p>Your report may show neutrophils as a <strong>percentage</strong> (e.g.&nbsp;&ldquo;Neut 65&nbsp;%&rdquo;) and/or as an <strong>absolute count</strong> "
                "(e.g.&nbsp;&ldquo;Neut# 4,200 cells/&mu;L&rdquo;). While both are informative, the <strong>absolute neutrophil count (ANC)</strong> is generally more reliable "
                "for clinical decisions. The reason: a percentage can be misleading if the total WBC is abnormal. "
                "For example, a patient with a very high lymphocyte count may appear to have a &ldquo;low&rdquo; neutrophil percentage even though the absolute number is perfectly normal.</p>"
                "<p>ANC is often calculated automatically by the analyser, but you can estimate it yourself: "
                "<strong>ANC = WBC &times; (Neutrophil&nbsp;% &divide; 100)</strong>. "
                "If your WBC is 8,000 and neutrophils are 60&nbsp;%, your ANC is 4,800&mdash;well within the normal range. "
                "When your doctor assesses infection risk (e.g.&nbsp;during chemotherapy), they almost always focus on ANC.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms associated with neutrophil changes",
            body_html=(
                "<p><strong>Neutrophilia</strong> itself rarely causes symptoms&mdash;instead the symptoms come from the underlying condition (e.g.&nbsp;fever and cough in pneumonia, "
                "pain and swelling at an injury site). You may not notice high neutrophils unless told by a blood test.</p>"
                "<p><strong>Neutropenia</strong> can be silent if mild. When severe (&lt;&nbsp;500 cells/&mu;L), the body struggles to fight infections, "
                "so recurrent or unusually severe infections become the hallmark: mouth ulcers, sore throat, skin infections, fever, or infections that don&rsquo;t respond as expected to treatment. "
                "Febrile neutropenia (fever + severe neutropenia) is a medical emergency, particularly in chemotherapy patients.</p>"
                "<p>If you have been told your neutrophils are low and you develop a fever (&ge;&nbsp;38&nbsp;&deg;C / 100.4&nbsp;&deg;F), "
                "contact your doctor or go to the emergency department immediately&mdash;prompt antibiotic treatment can be lifesaving.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests your doctor may review",
            body_html=(
                "<p>Neutrophils are part of the WBC differential, which also includes <a href=\"/en/blog/lymphocytes-high-or-low\">lymphocytes</a>, "
                "<a href=\"/en/blog/monocytes-high-meaning\">monocytes</a>, <a href=\"/en/blog/eosinophils-high-meaning\">eosinophils</a>, "
                "and <a href=\"/en/blog/basophils-high-meaning\">basophils</a>. Together they reveal which arm of the immune system is active.</p>"
                "<p>Depending on the clinical picture, the doctor may also request <strong>CRP</strong> or <strong>procalcitonin</strong> (to gauge inflammation or infection severity), "
                "<strong>blood cultures</strong>, a <strong>peripheral blood smear</strong> (to look at cell morphology), <strong>bone marrow biopsy</strong> (if a marrow disorder is suspected), "
                "or specific tests such as <strong>anti-neutrophil antibodies</strong> for autoimmune neutropenia. "
                "Serial CBCs to track the trend over days or weeks are often more informative than a single snapshot.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Discuss any neutrophil result outside the reference range with your doctor. "
                "Seek <strong>urgent</strong> medical attention if you have neutropenia and develop a fever, chills, sore throat, mouth ulcers, or any sign of infection. "
                "Febrile neutropenia is a time-sensitive emergency.</p>"
                "<p>For high neutrophils, the urgency depends on the underlying cause&mdash;but if you have unexplained persistent neutrophilia, particularly with fatigue, "
                "night sweats, or weight loss, a haematology referral may be warranted. Even mild or borderline abnormalities deserve a conversation with your healthcare provider.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare. Upload your blood test at <a href=\"/analyze\">noryaai.com/analyze</a> and receive a clear, structured summary "
                "that explains your neutrophil count and the rest of the CBC differential in plain language, with reference ranges and context. "
                "This makes it easier to understand the numbers and have a productive conversation with your doctor.</p>"
                "<p>Whether you are monitoring neutropenia during treatment or simply curious about a &ldquo;Neut# 1,800&rdquo; on your report, "
                "Norya organises your results so you can ask the right questions. For plans and pricing, see our <a href=\"/pricing\">pricing page</a>.</p>"
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
            heading="Nötrofil yüksek veya düşük: lökosit formülünüzü anlamak",
            body_html=(
                "<p>Tam kan sayımınızda (CBC) lökosit formülü yer aldığında, nötrofil genellikle ilk dikkat çeken satırdır. "
                "Beyaz kan hücrelerinin en bol tipi olan nötrofiller, sayısındaki artış veya azalma yaygın bakteriyel enfeksiyonlardan ilaç yan etkilerine kadar pek çok duruma işaret edebilir. "
                "Ancak tek bir nötrofil değeri, her laboratuvar sonucu gibi, anlamlı olabilmesi için bağlam gerektirir.</p>"
                "<p>Bu rehber nötrofillerin ne olduğunu, raporunuzdaki referans aralıklarını, yüksek veya düşük sayının yaygın nedenlerini "
                "ve ne zaman bir sağlık uzmanıyla görüşmeniz gerektiğini açıklar. Eğitim amaçlıdır, teşhis değildir.</p>"
            ),
        ),
        Section(
            id="what-are-neutrophils", level=2,
            heading="Nötrofil nedir ve ne işe yarar?",
            body_html=(
                "<p><strong>Nötrofiller</strong>, bakteri ve mantarları yok edebilen enzimlerle dolu küçük granüller içeren bir beyaz kan hücresi (granülosit) türüdür. "
                "Kemik iliğinde üretilir ve kan dolaşımına salınırlar; orada yalnızca 6&ndash;12&nbsp;saat dolaştıktan sonra dokulara göç ederler. "
                "Kısa ömürlerine rağmen bağışıklık sisteminin acil müdahale gücüdürler: enfeksiyon veya yaralanma bölgesine ilk ulaşan hücrelerdir.</p>"
                "<p>Nötrofiller patojenleri yutarak (fagositoz) ve antimikrobiyal maddeler salgılayarak çalışır. "
                "Ayrıca bakterileri fiziksel olarak yakalayan DNA ve protein ağları olan nötrofil hücre dışı tuzaklar (NET) oluştururlar. "
                "Doğal bağışıklıkta bu kadar merkezi oldukları için sayılarındaki belirgin düşüş vücudu enfeksiyonlara savunmasız bırakır.</p>"
                "<p>Laboratuvar raporunda nötrofiller &ldquo;Nötrofil (Mutlak)&rdquo; veya &ldquo;Neut&nbsp;%&rdquo; olarak görünebilir. "
                "Her iki değer de önemlidir; mutlak sayı genellikle klinik olarak daha kullanışlıdır çünkü diğer hücre tiplerindeki değişikliklerden etkilenmez.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal nötrofil aralıkları",
            body_html=(
                "<p>Referans aralıkları laboratuvarlar ve popülasyonlar arasında farklılık gösterebilir. Aşağıdaki değerler yetişkinlerde yaygın olarak kullanılır.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parametre</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tipik yetişkin aralığı</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mutlak nötrofil sayısı (ANC)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.500&ndash;7.000 hücre/&mu;L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Nötrofil yüzdesi</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">%40&ndash;70</td></tr>'
                "</tbody></table>"
                "<p>Bazı etnik gruplarda, özellikle Afrika, Orta Doğu veya Karayip kökenli kişilerde başlangıç nötrofil sayısı daha düşük olabilir "
                "(iyi huylu etnik nötropeni). Çocuk aralıkları yetişkinlerden farklıdır. Hamilelik de nötrofil sayısını fizyolojik olarak yükseltebilir.</p>"
            ),
        ),
        Section(
            id="high-neutrophils-causes", level=2,
            heading="Nötrofil yüksekliğinin nedenleri (nötrofili)",
            body_html=(
                "<p>Üst referans sınırını aşan nötrofil sayısı <strong>nötrofili</strong> olarak adlandırılır. "
                "En sık tetikleyici <strong>bakteriyel enfeksiyon</strong>dur: bakteri istilasında kemik iliği üretimi artırır, dalak ve damar duvarları depolanmış nötrofilleri salar. "
                "İdrar yolu enfeksiyonları, pnömoni, cilt enfeksiyonları ve apseler klasik örneklerdir.</p>"
                "<p>Enfeksiyon dışı nedenlerden kaynaklanan <strong>akut inflamasyon</strong>&mdash;cerrahi, travma, yanıklar, miyokard enfarktüsü veya otoimmün alevlenmeler&mdash;de nötrofilleri yükseltebilir. "
                "<strong>Fizyolojik stres</strong> (yoğun egzersiz, duygusal sıkıntı, ağrı) ağırlıklı olarak nötrofillerin yönlendirdiği kısa süreli bir &ldquo;stres lökositozu&rdquo; üretir. "
                "<strong>Kortikosteroidler</strong> iyi bilinen farmakolojik bir nedendir: nötrofillerin kandan dokulara göçünü azaltarak dolaşımdaki sayıyı yapay olarak yükseltirler.</p>"
                "<p><strong>Sigara</strong>, havayolu inflamasyonu yoluyla nötrofilleri kronik olarak yükseltir. "
                "Daha nadir olarak, inatçı veya çok yüksek nötrofili <strong>miyeloproliferatif neoplazmlara</strong> (kronik miyeloid lösemi gibi) işaret edebilir. "
                "Hekiminiz yükselme derecesini, zamanla gidişatı ve genel klinik tabloyu değerlendirecektir.</p>"
            ),
        ),
        Section(
            id="low-neutrophils-causes", level=2,
            heading="Nötrofil düşüklüğünün nedenleri (nötropeni)",
            body_html=(
                "<p>2.500&nbsp;hücre/&mu;L altındaki nötrofil sayısına <strong>nötropeni</strong> denir. Şiddeti önemlidir: hafif nötropeni (1.000&ndash;2.500) genellikle klinik olarak iyi huyludur; "
                "ciddi nötropeni (&lt;&nbsp;500) enfeksiyon riskini belirgin artırır. "
                "Günlük pratikte en sık neden <strong>viral enfeksiyon</strong>dur&mdash;influenza, hepatit, HIV, EBV gibi birçok virüs nötrofil üretimini geçici olarak baskılayabilir.</p>"
                "<p><strong>İlaçlar</strong> bir diğer sık nedendir. Kemoterapi ilaçları en bilinen örnek olsa da bazı antibiyotikler (TMP-SMX), antikonvülzanlar (karbamazepin), "
                "antitiroid ilaçlar (metimazol) ve bazı anti-inflamatuvar ajanlar da nötrofilleri düşürebilir. İlaca bağlı nötropeni genellikle ilaç kesildikten sonra geri dönüşümlüdür.</p>"
                "<p><strong>Otoimmün nötropeni</strong>, vücudun kendi nötrofillerine karşı antikor üretmesiyle oluşur. "
                "<strong>Besinsel eksiklikler</strong> (B12, folat, bakır) üretimi bozabilir. "
                "<strong>Ciddi enfeksiyonlar</strong> (sepsis), kemik iliğinin karşılayamayacağı kadar hızlı tüketim nedeniyle paradoks olarak nötrofilleri düşürebilir. "
                "<strong>Siklik nötropeni</strong> ve <strong>ciddi konjenital nötropeni</strong> gibi kalıtsal durumlar nadir ancak pediatri pratiğinde önemlidir.</p>"
            ),
        ),
        Section(
            id="absolute-vs-percentage", level=2,
            heading="Mutlak sayı mı, yüzde mi: hangisi daha önemli?",
            body_html=(
                "<p>Raporunuzda nötrofiller <strong>yüzde</strong> (&ldquo;Neut %65&rdquo;) ve/veya <strong>mutlak sayı</strong> (&ldquo;Neut# 4.200 hücre/&mu;L&rdquo;) olarak görünebilir. "
                "Her ikisi de bilgilendirici olmakla birlikte, klinik kararlar için genellikle <strong>mutlak nötrofil sayısı (ANC)</strong> daha güvenilirdir. "
                "Nedeni: toplam WBC anormalse yüzde yanıltıcı olabilir.</p>"
                "<p>ANC genellikle analizör tarafından otomatik hesaplanır; kendiniz de tahmin edebilirsiniz: "
                "<strong>ANC = WBC &times; (Nötrofil&nbsp;% &divide; 100)</strong>. "
                "WBC&rsquo;niz 8.000 ve nötrofil %60 ise ANC&rsquo;niz 4.800&mdash;normal aralıkta. "
                "Hekiminiz enfeksiyon riskini değerlendirirken (örn. kemoterapi sırasında) neredeyse her zaman ANC&rsquo;ye odaklanır.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Nötrofil değişiklikleriyle ilişkili belirtiler",
            body_html=(
                "<p><strong>Nötrofili</strong> kendisi nadiren belirtiye neden olur&mdash;belirtiler altta yatan durumdan gelir (pnömonide ateş ve öksürük, yaralanma bölgesinde ağrı ve şişlik gibi). "
                "Kan testinde söylenmediği sürece yüksek nötrofilleri fark etmeyebilirsiniz.</p>"
                "<p><strong>Nötropeni</strong> hafifse sessiz kalabilir. Ciddi olduğunda (&lt;&nbsp;500 hücre/&mu;L) vücut enfeksiyonlarla mücadelede zorlanır; "
                "tekrarlayan veya olağandışı şiddetli enfeksiyonlar (ağız ülserleri, boğaz ağrısı, cilt enfeksiyonları, ateş) ön plana çıkar. "
                "Febril nötropeni (ateş + ciddi nötropeni) özellikle kemoterapi hastalarında tıbbi acildir.</p>"
                "<p>Nötrofillerinizin düşük olduğu söylenmiş ve ateşiniz çıkıyorsa (&ge;&nbsp;38&nbsp;&deg;C), "
                "derhal doktorunuzu arayın veya acil servise gidin&mdash;hızlı antibiyotik tedavisi hayat kurtarıcı olabilir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Hekimin değerlendirebileceği ilişkili testler",
            body_html=(
                "<p>Nötrofiller, <a href=\"/tr/blog/lymphocytes-high-or-low\">lenfosit</a>, "
                "<a href=\"/tr/blog/monocytes-high-meaning\">monosit</a>, <a href=\"/tr/blog/eosinophils-high-meaning\">eozinofil</a> "
                "ve <a href=\"/tr/blog/basophils-high-meaning\">bazofilleri</a> de içeren lökosit formülünün bir parçasıdır. "
                "Birlikte bağışıklık sisteminin hangi kolunun aktif olduğunu gösterirler.</p>"
                "<p>Klinik tabloya bağlı olarak hekim <strong>CRP</strong> veya <strong>prokalsitonin</strong>, <strong>kan kültürü</strong>, "
                "<strong>periferik yayma</strong>, <strong>kemik iliği biyopsisi</strong> veya <strong>anti-nötrofil antikorları</strong> gibi testler de isteyebilir. "
                "Günler veya haftalar içinde trendi izlemek için seri CBC&rsquo;ler genellikle tek bir ölçümden daha bilgilendiricidir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman hekime başvurmalısınız?",
            body_html=(
                "<p>Referans aralığı dışındaki herhangi bir nötrofil sonucunu hekiminizle görüşün. "
                "Nötropeniniz varsa ve ateş, titreme, boğaz ağrısı, ağız ülserleri veya herhangi bir enfeksiyon belirtisi geliştirirseniz <strong>acil</strong> tıbbi yardım alın. "
                "Febril nötropeni zamana duyarlı bir acildir.</p>"
                "<p>Yüksek nötrofiller için aciliyet altta yatan nedene bağlıdır; ancak açıklanamayan inatçı nötrofili, özellikle yorgunluk, "
                "gece terlemesi veya kilo kaybıyla birlikteyse hematoloji yönlendirmesi gerekebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;randevunuza hazırlanmanıza yardımcı olur. Kan tahlili raporunuzu <a href=\"/analyze\">noryaai.com/analyze</a> adresinden yükleyin "
                "ve nötrofil sayınız ile CBC formülünün geri kalanını sade dilde, referans aralıkları ve bağlamlarıyla açıklayan net, yapılandırılmış bir özet alın.</p>"
                "<p>İster tedavi sırasında nötropeniyi takip edin, ister raporunuzdaki &ldquo;Neut# 1.800&rdquo; değerini merak edin; "
                "Norya sonuçlarınızı düzenler ve doğru soruları sormanıza yardımcı olur. Plan ve fiyatlar: <a href=\"/pricing\">fiyatlandırma sayfası</a>.</p>"
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
        Section(id="intro", level=2, heading="Neutrófilos altos o bajos: entiende tu fórmula leucocitaria",
                body_html=(
                    "<p>Cuando el hemograma incluye una fórmula leucocitaria, los neutrófilos suelen ser la primera línea en la que te fijas. "
                    "Son el tipo más abundante de glóbulos blancos, y los cambios en su número pueden indicar desde una infección bacteriana común hasta efectos secundarios de medicamentos.</p>"
                    "<p>Esta guía explica qué son los neutrófilos, cómo leer los rangos de referencia, las causas más frecuentes de valores altos o bajos, "
                    "y cuándo consultar al médico. Es educativa, no diagnóstica.</p>")),
        Section(id="what-are-neutrophils", level=2, heading="¿Qué son los neutrófilos y qué hacen?",
                body_html=(
                    "<p><strong>Los neutrófilos</strong> son un tipo de granulocito: un glóbulo blanco que contiene gránulos llenos de enzimas capaces de destruir bacterias y hongos. "
                    "Se producen en la médula ósea y circulan en sangre solo 6&ndash;12&nbsp;horas antes de migrar a los tejidos. Son la fuerza de respuesta rápida del sistema inmunitario.</p>"
                    "<p>Funcionan fagocitando patógenos y liberando sustancias antimicrobianas. También forman trampas extracelulares (NETs) que atrapan bacterias físicamente. "
                    "En el informe aparecen como &ldquo;Neutrófilos (Absoluto)&rdquo; o &ldquo;Neut %&rdquo;; el recuento absoluto suele ser más útil clínicamente.</p>")),
        Section(id="normal-ranges", level=2, heading="Rangos normales de neutrófilos",
                body_html=(
                    "<p>Los rangos de referencia varían entre laboratorios. Los valores siguientes se usan ampliamente en adultos.</p>"
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parámetro</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango adulto típico</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Recuento absoluto (ANC)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.500&ndash;7.000 cél./&mu;L</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Porcentaje</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70 %</td></tr>'
                    "</tbody></table>"
                    "<p>Algunos grupos étnicos tienen un recuento basal inferior (neutropenia étnica benigna). Los rangos infantiles difieren y cambian con la edad. El embarazo eleva fisiológicamente los neutrófilos.</p>")),
        Section(id="high-neutrophils-causes", level=2, heading="Causas de neutrófilos altos (neutrofilia)",
                body_html=(
                    "<p>La causa más frecuente es la <strong>infección bacteriana</strong>: la médula aumenta la producción y se liberan neutrófilos almacenados. "
                    "Infecciones urinarias, neumonía, infecciones cutáneas y abscesos son ejemplos clásicos.</p>"
                    "<p>La <strong>inflamación aguda</strong> no infecciosa (cirugía, trauma, quemaduras), el <strong>estrés fisiológico</strong> (ejercicio intenso, dolor) "
                    "y los <strong>corticosteroides</strong> también pueden elevar los neutrófilos. El <strong>tabaquismo</strong> los eleva crónicamente.</p>"
                    "<p>Más raramente, una neutrofilia persistente o muy alta puede apuntar a <strong>neoplasias mieloproliferativas</strong>. El médico evaluará el grado, la tendencia y el cuadro clínico.</p>")),
        Section(id="low-neutrophils-causes", level=2, heading="Causas de neutrófilos bajos (neutropenia)",
                body_html=(
                    "<p>La causa más común es la <strong>infección viral</strong> (gripe, hepatitis, HIV). La neutropenia grave (&lt;&nbsp;500) aumenta significativamente el riesgo de infección.</p>"
                    "<p><strong>Medicamentos</strong> como quimioterapia, ciertos antibióticos, anticonvulsivos y antitiroideos pueden reducir los neutrófilos. Suele ser reversible al retirar el fármaco.</p>"
                    "<p><strong>Neutropenia autoinmunitaria</strong>, <strong>déficit de B12/folato</strong> e infecciones graves (sepsis) son otras causas. Condiciones hereditarias como la neutropenia cíclica son raras pero importantes en pediatría.</p>")),
        Section(id="absolute-vs-percentage", level=2, heading="Recuento absoluto vs. porcentaje",
                body_html=(
                    "<p>El <strong>recuento absoluto (ANC)</strong> es más fiable que el porcentaje para decisiones clínicas, porque el porcentaje puede ser engañoso si el WBC total es anormal.</p>"
                    "<p>Cálculo: <strong>ANC = WBC &times; (Neut&nbsp;% &divide; 100)</strong>. Si WBC es 8.000 y Neut 60&nbsp;%, ANC = 4.800, dentro del rango normal.</p>")),
        Section(id="symptoms", level=2, heading="Síntomas asociados a cambios en neutrófilos",
                body_html=(
                    "<p><strong>Neutrofilia</strong> en sí rara vez causa síntomas; los síntomas provienen de la causa subyacente.</p>"
                    "<p><strong>Neutropenia grave</strong> (&lt;&nbsp;500) reduce la capacidad de combatir infecciones: úlceras bucales, dolor de garganta, infecciones cutáneas y fiebre. "
                    "La neutropenia febril es una urgencia médica, especialmente en pacientes con quimioterapia.</p>")),
        Section(id="related-tests", level=2, heading="Pruebas relacionadas",
                body_html=(
                    "<p>Los neutrófilos forman parte de la fórmula leucocitaria junto con <a href=\"/es/blog/lymphocytes-high-or-low\">linfocitos</a>, "
                    "<a href=\"/es/blog/monocytes-high-meaning\">monocitos</a>, eosinófilos y basófilos.</p>"
                    "<p>Según el caso: PCR, procalcitonina, hemocultivos, frotis periférico, biopsia de médula ósea o anticuerpos antineutrófilos.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="¿Cuándo acudir al médico?",
                body_html=(
                    "<p>Comenta cualquier neutrófilos fuera de rango con tu médico. Busca atención <strong>urgente</strong> si tienes neutropenia y fiebre, escalofríos o signos de infección.</p>"
                    "<p>Para neutrofilia persistente inexplicada, especialmente con fatiga, sudores nocturnos o pérdida de peso, puede estar indicada una derivación a hematología.</p>")),
        Section(id="how-norya-helps", level=2, heading="Cómo ayuda Norya",
                body_html=(
                    "<p>Norya no diagnostica&mdash;te ayuda a prepararte. Sube tu analítica en <a href=\"/analyze\">noryaai.com/analyze</a> y recibe un resumen claro "
                    "de tus neutrófilos y la fórmula leucocitaria en lenguaje sencillo.</p>"
                    "<p>Ya sea que monitorices neutropenia o quieras entender un &ldquo;Neut# 1.800&rdquo;, Norya organiza tus resultados. "
                    "Opciones y precios: <a href=\"/pricing\">página de precios</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html=(
                    '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> '
                    'Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>')),
    ]


# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Neutrophile hoch oder niedrig: Differentialblutbild verstehen",
                body_html=(
                    "<p>Wenn Ihr Blutbild ein Differentialblutbild enthält, sind Neutrophile meist die erste Zeile, die ins Auge fällt. "
                    "Sie sind die häufigsten weißen Blutkörperchen, und Veränderungen ihrer Zahl können von einer banalen Infektion bis zu Medikamentennebenwirkungen reichen.</p>"
                    "<p>Dieser Ratgeber erklärt, was Neutrophile sind, wie Sie die Referenzbereiche lesen, häufige Ursachen für hohe oder niedrige Werte "
                    "und wann Sie einen Arzt aufsuchen sollten.</p>")),
        Section(id="what-are-neutrophils", level=2, heading="Was sind Neutrophile und was machen sie?",
                body_html=(
                    "<p><strong>Neutrophile</strong> sind Granulozyten mit Enzymen, die Bakterien und Pilze zerstören können. "
                    "Sie werden im Knochenmark gebildet und zirkulieren nur 6&ndash;12&nbsp;Stunden im Blut, bevor sie ins Gewebe wandern&mdash;die Schnelleingreiftruppe des Immunsystems.</p>"
                    "<p>Sie phagozytieren Erreger und bilden neutrophile extrazelluläre Fallen (NETs). "
                    "Im Laborbericht erscheinen sie als &bdquo;Neutrophile (absolut)&ldquo; oder &bdquo;Neut %&ldquo;; der absolute Wert ist klinisch meist aussagekräftiger.</p>")),
        Section(id="normal-ranges", level=2, heading="Normale Neutrophilen-Bereiche",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parameter</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typischer Erwachsenenbereich</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Absolute Neutrophilenzahl (ANC)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.500&ndash;7.000 Zellen/&mu;L</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Prozent</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70 %</td></tr>'
                    "</tbody></table>"
                    "<p>Manche Ethnien haben physiologisch niedrigere Ausgangswerte (benigne ethnische Neutropenie). Kinderwerte unterscheiden sich. Schwangerschaft erhöht die Neutrophilen physiologisch.</p>")),
        Section(id="high-neutrophils-causes", level=2, heading="Ursachen erhöhter Neutrophiler (Neutrophilie)",
                body_html=(
                    "<p>Häufigster Auslöser ist eine <strong>bakterielle Infektion</strong>. Auch <strong>akute Entzündung</strong> (OP, Trauma, Verbrennung), "
                    "<strong>Stress</strong>, <strong>Kortikosteroide</strong> und <strong>Rauchen</strong> können den Wert erhöhen.</p>"
                    "<p>Seltener deutet eine anhaltend sehr hohe Neutrophilie auf <strong>myeloproliferative Neoplasien</strong> hin. "
                    "Der Arzt beurteilt Ausmaß, Trend und klinisches Bild.</p>")),
        Section(id="low-neutrophils-causes", level=2, heading="Ursachen niedriger Neutrophiler (Neutropenie)",
                body_html=(
                    "<p>Die häufigste Ursache sind <strong>Virusinfektionen</strong>. Schwere Neutropenie (&lt;&nbsp;500) erhöht das Infektionsrisiko erheblich.</p>"
                    "<p><strong>Medikamente</strong> (Chemotherapie, bestimmte Antibiotika, Antikonvulsiva, Thyreostatika) sind eine weitere häufige Ursache&mdash;meist reversibel nach Absetzen.</p>"
                    "<p>Weitere Ursachen: autoimmune Neutropenie, B12-/Folsäure-/Kupfermangel, Sepsis und seltene erbliche Formen.</p>")),
        Section(id="absolute-vs-percentage", level=2, heading="Absolutzahl vs. Prozentsatz",
                body_html=(
                    "<p>Die <strong>absolute Neutrophilenzahl (ANC)</strong> ist klinisch aussagekräftiger als der Prozentsatz, "
                    "da der Prozentsatz bei abweichendem Gesamt-WBC irreführend sein kann.</p>"
                    "<p>Berechnung: <strong>ANC = WBC &times; (Neut % &divide; 100)</strong>.</p>")),
        Section(id="symptoms", level=2, heading="Symptome bei Neutrophilen-Veränderungen",
                body_html=(
                    "<p><strong>Neutrophilie</strong> verursacht selbst selten Beschwerden; Symptome stammen von der Grunderkrankung.</p>"
                    "<p><strong>Schwere Neutropenie</strong> macht anfällig für Infektionen: Mundulzera, Halsentzündung, Hautinfektionen, Fieber. "
                    "Febrile Neutropenie ist ein Notfall, besonders bei Chemotherapie.</p>")),
        Section(id="related-tests", level=2, heading="Verwandte Tests",
                body_html=(
                    "<p>Neutrophile gehören zum Differentialblutbild mit <a href=\"/de/blog/lymphocytes-high-or-low\">Lymphozyten</a>, "
                    "<a href=\"/de/blog/monocytes-high-meaning\">Monozyten</a>, Eosinophilen und Basophilen.</p>"
                    "<p>Je nach Situation: CRP, Procalcitonin, Blutkulturen, Blutausstrich, Knochenmarkbiopsie oder Anti-Neutrophilen-Antikörper.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="Wann zum Arzt?",
                body_html=(
                    "<p>Besprechen Sie jeden Wert außerhalb des Referenzbereichs mit Ihrem Arzt. "
                    "<strong>Dringende</strong> Vorstellung bei Neutropenie mit Fieber, Schüttelfrost oder Infektionszeichen.</p>"
                    "<p>Anhaltende unerklärte Neutrophilie mit Müdigkeit, Nachtschweiß oder Gewichtsverlust sollte hämatologisch abgeklärt werden.</p>")),
        Section(id="how-norya-helps", level=2, heading="Wie Norya hilft",
                body_html=(
                    "<p>Norya stellt keine Diagnosen&mdash;wir helfen bei der Vorbereitung. Laden Sie Ihren Laborbericht unter <a href=\"/analyze\">noryaai.com/analyze</a> hoch "
                    "und erhalten Sie eine klare Zusammenfassung Ihrer Neutrophilenzahl und des Differentialblutbilds.</p>"
                    "<p>Optionen und Preise: <a href=\"/pricing\">Preisseite</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html=(
                    '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> '
                    'Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>')),
    ]


# ---------------------------------------------------------------------------
# French
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Neutrophiles hauts ou bas : comprendre votre formule leucocytaire",
                body_html=(
                    "<p>Quand votre NFS comprend une formule leucocytaire, les neutrophiles sont souvent la première ligne que l&rsquo;on regarde. "
                    "Ce sont les globules blancs les plus nombreux ; des variations de leur nombre peuvent signaler une infection bactérienne, un effet médicamenteux ou un stress.</p>"
                    "<p>Ce guide explique ce que sont les neutrophiles, comment lire les fourchettes, les causes de valeurs hautes ou basses, et quand consulter.</p>")),
        Section(id="what-are-neutrophils", level=2, heading="Que sont les neutrophiles et quel est leur rôle ?",
                body_html=(
                    "<p><strong>Les neutrophiles</strong> sont des granulocytes contenant des enzymes capables de détruire bactéries et champignons. "
                    "Produits dans la moelle, ils circulent 6&ndash;12&nbsp;h avant de migrer dans les tissus&mdash;la force d&rsquo;intervention rapide de l&rsquo;immunité.</p>"
                    "<p>Ils phagocytent les pathogènes et forment des pièges extracellulaires (NETs). Sur le bilan, ils apparaissent en valeur absolue ou en pourcentage ; "
                    "le compte absolu (PNN) est généralement plus fiable cliniquement.</p>")),
        Section(id="normal-ranges", level=2, heading="Valeurs normales des neutrophiles",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Paramètre</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fourchette adulte</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">PNN (polynucléaires neutrophiles)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 500&ndash;7 000 /&mu;L</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Pourcentage</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70 %</td></tr>'
                    "</tbody></table>"
                    "<p>Certaines origines ethniques ont un taux de base plus faible (neutropénie ethnique bénigne). La grossesse élève physiologiquement les PNN.</p>")),
        Section(id="high-neutrophils-causes", level=2, heading="Causes de neutrophiles élevés (neutrophilie)",
                body_html=(
                    "<p>Le déclencheur le plus fréquent est l&rsquo;<strong>infection bactérienne</strong>. L&rsquo;inflammation aiguë non infectieuse, le stress, "
                    "les corticoïdes et le tabac peuvent aussi les augmenter.</p>"
                    "<p>Une neutrophilie très élevée et persistante peut orienter vers une <strong>néoplasie myéloproliférative</strong>.</p>")),
        Section(id="low-neutrophils-causes", level=2, heading="Causes de neutrophiles bas (neutropénie)",
                body_html=(
                    "<p>Cause la plus courante : <strong>infection virale</strong>. Une neutropénie sévère (&lt;&nbsp;500) augmente nettement le risque infectieux.</p>"
                    "<p><strong>Médicaments</strong> (chimiothérapie, certains antibiotiques, antiépileptiques, antithyroïdiens) sont une cause fréquente, en général réversible.</p>"
                    "<p>Autres causes : neutropénie auto-immune, carences (B12, folates, cuivre), sepsis et formes héréditaires rares.</p>")),
        Section(id="absolute-vs-percentage", level=2, heading="Valeur absolue vs pourcentage",
                body_html=(
                    "<p>Le <strong>PNN absolu</strong> est plus fiable que le pourcentage car ce dernier peut être trompeur si le nombre total de GB est anormal.</p>"
                    "<p>Calcul : <strong>PNN = GB totaux &times; (Neut % &divide; 100)</strong>.</p>")),
        Section(id="symptoms", level=2, heading="Symptômes liés aux variations de neutrophiles",
                body_html=(
                    "<p>La <strong>neutrophilie</strong> elle-même donne rarement des symptômes ; ceux-ci viennent de la cause sous-jacente.</p>"
                    "<p>La <strong>neutropénie sévère</strong> expose aux infections : aphtes, angine, infections cutanées, fièvre. "
                    "La neutropénie fébrile est une urgence, surtout sous chimiothérapie.</p>")),
        Section(id="related-tests", level=2, heading="Examens complémentaires",
                body_html=(
                    "<p>Les neutrophiles font partie de la formule qui inclut <a href=\"/fr/blog/lymphocytes-high-or-low\">lymphocytes</a>, "
                    "<a href=\"/fr/blog/monocytes-high-meaning\">monocytes</a>, éosinophiles et basophiles.</p>"
                    "<p>Selon le contexte : CRP, procalcitonine, hémocultures, frottis, biopsie médullaire ou anticorps anti-neutrophiles.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter ?",
                body_html=(
                    "<p>Parlez-en à votre médecin si les neutrophiles sont hors fourchette. Consultez <strong>en urgence</strong> si neutropénie + fièvre ou signe d&rsquo;infection.</p>"
                    "<p>Une neutrophilie persistante inexpliquée avec fatigue, sueurs nocturnes ou perte de poids justifie un avis hématologique.</p>")),
        Section(id="how-norya-helps", level=2, heading="Comment Norya vous aide",
                body_html=(
                    "<p>Norya ne pose pas de diagnostic&mdash;nous vous aidons à préparer votre rendez-vous. "
                    "Envoyez votre bilan sur <a href=\"/analyze\">noryaai.com/analyze</a> pour un résumé clair de vos neutrophiles.</p>"
                    "<p>Options et tarifs : <a href=\"/pricing\">page tarifs</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html=(
                    '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> '
                    "Discutez toujours de vos résultats avec un professionnel de santé. <a href=\"/analyze\">Commencer l'analyse avec Norya</a></p>")),
    ]


# ---------------------------------------------------------------------------
# Italian
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Neutrofili alti o bassi: capire la formula leucocitaria",
                body_html=(
                    "<p>Quando l&rsquo;emocromo include la formula leucocitaria, i neutrofili sono di solito la prima riga su cui cade l&rsquo;occhio. "
                    "Sono il tipo più abbondante di globuli bianchi e le variazioni del loro numero possono segnalare infezioni batteriche, effetti di farmaci o stress.</p>"
                    "<p>Questa guida spiega cosa sono i neutrofili, come leggere gli intervalli, le cause di valori alti o bassi e quando consultare il medico.</p>")),
        Section(id="what-are-neutrophils", level=2, heading="Cosa sono i neutrofili e a che cosa servono?",
                body_html=(
                    "<p><strong>I neutrofili</strong> sono granulociti con enzimi capaci di distruggere batteri e funghi. "
                    "Prodotti nel midollo osseo, circolano 6&ndash;12&nbsp;ore prima di migrare nei tessuti: la forza di risposta rapida dell&rsquo;immunità.</p>"
                    "<p>Fagocitano i patogeni e formano trappole extracellulari (NET). Nel referto appaiono come valore assoluto o percentuale; "
                    "il conteggio assoluto è generalmente più affidabile.</p>")),
        Section(id="normal-ranges", level=2, heading="Valori normali dei neutrofili",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parametro</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo adulto</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Conta assoluta (ANC)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.500&ndash;7.000 cellule/&mu;L</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Percentuale</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70 %</td></tr>'
                    "</tbody></table>"
                    "<p>Alcune etnie hanno valori basali inferiori (neutropenia etnica benigna). La gravidanza eleva fisiologicamente i neutrofili.</p>")),
        Section(id="high-neutrophils-causes", level=2, heading="Cause di neutrofili alti (neutrofilia)",
                body_html=(
                    "<p>Causa più frequente: <strong>infezione batterica</strong>. Anche infiammazione acuta, stress, cortisonici e fumo possono alzarli.</p>"
                    "<p>Una neutrofilia molto alta e persistente può orientare verso <strong>neoplasie mieloproliferative</strong>.</p>")),
        Section(id="low-neutrophils-causes", level=2, heading="Cause di neutrofili bassi (neutropenia)",
                body_html=(
                    "<p>Causa più comune: <strong>infezione virale</strong>. Neutropenia grave (&lt;&nbsp;500) aumenta molto il rischio infettivo.</p>"
                    "<p><strong>Farmaci</strong> (chemioterapia, alcuni antibiotici, antiepilettici, antitiroidei) sono un&rsquo;altra causa frequente, di solito reversibile.</p>"
                    "<p>Altre cause: neutropenia autoimmune, carenze (B12, folati, rame), sepsi e forme ereditarie rare.</p>")),
        Section(id="absolute-vs-percentage", level=2, heading="Conta assoluta vs percentuale",
                body_html=(
                    "<p>La <strong>conta assoluta (ANC)</strong> è clinicamente più affidabile della percentuale, che può ingannare se il WBC totale è anomalo.</p>"
                    "<p>Calcolo: <strong>ANC = WBC &times; (Neut % &divide; 100)</strong>.</p>")),
        Section(id="symptoms", level=2, heading="Sintomi legati alle variazioni dei neutrofili",
                body_html=(
                    "<p>La <strong>neutrofilia</strong> di per sé raramente provoca sintomi; quelli avvertiti derivano dalla causa sottostante.</p>"
                    "<p>La <strong>neutropenia grave</strong> espone a infezioni: afte, mal di gola, infezioni cutanee, febbre. La neutropenia febbrile è un&rsquo;emergenza.</p>")),
        Section(id="related-tests", level=2, heading="Esami correlati",
                body_html=(
                    "<p>I neutrofili fanno parte della formula che include <a href=\"/it/blog/lymphocytes-high-or-low\">linfociti</a>, "
                    "<a href=\"/it/blog/monocytes-high-meaning\">monociti</a>, eosinofili e basofili.</p>"
                    "<p>A seconda del caso: PCR, procalcitonina, emocolture, striscio, biopsia midollare o anticorpi anti-neutrofili.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="Quando rivolgersi al medico",
                body_html=(
                    "<p>Parla con il medico se i neutrofili sono fuori intervallo. Cerca assistenza <strong>urgente</strong> se neutropenia + febbre o segni di infezione.</p>"
                    "<p>Neutrofilia persistente inspiegata con stanchezza, sudorazioni notturne o calo di peso richiede un parere ematologico.</p>")),
        Section(id="how-norya-helps", level=2, heading="Come Norya ti aiuta",
                body_html=(
                    "<p>Norya non fa diagnosi&mdash;ti aiuta a prepararti. Carica il referto su <a href=\"/analyze\">noryaai.com/analyze</a> "
                    "per un riepilogo chiaro dei neutrofili e della formula.</p>"
                    "<p>Opzioni e prezzi: <a href=\"/pricing\">pagina prezzi</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html=(
                    '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> '
                    'Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>')),
    ]


# ---------------------------------------------------------------------------
# Hebrew
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="נויטרופילים גבוהים או נמוכים: הבנת ספירת הדם הלבנה",
                body_html=(
                    "<p>כשספירת הדם כוללת נוסחת דם, הנויטרופילים הם בדרך כלל השורה הראשונה שאליה מסתכלים. "
                    "הם סוג תאי הדם הלבנים השכיח ביותר, ושינויים במספרם יכולים להצביע על זיהום חיידקי, תופעות לוואי של תרופות או מתח.</p>"
                    "<p>מדריך זה מסביר מהם נויטרופילים, כיצד לקרוא את הטווחים, גורמים לערכים גבוהים או נמוכים, ומתי לפנות לרופא.</p>")),
        Section(id="what-are-neutrophils", level=2, heading="מהם נויטרופילים ומה הם עושים?",
                body_html=(
                    "<p><strong>נויטרופילים</strong> הם גרנולוציטים המכילים אנזימים שמשמידים חיידקים ופטריות. "
                    "הם מיוצרים במח העצם וסובבים בדם 6&ndash;12 שעות לפני שנודדים לרקמות&mdash;כוח התגובה המהירה של מערכת החיסון.</p>"
                    "<p>הם בולעים פתוגנים ויוצרים מלכודות חוץ-תאיות (NETs). בדוח הם מופיעים כערך מוחלט או אחוז; הספירה המוחלטת בדרך כלל אמינה יותר קלינית.</p>")),
        Section(id="normal-ranges", level=2, heading="טווחים תקינים של נויטרופילים",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">פרמטר</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח בוגרים</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ספירה מוחלטת (ANC)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,500&ndash;7,000 תאים/&mu;L</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">אחוז</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70%</td></tr>'
                    "</tbody></table>"
                    "<p>בקרב קבוצות אתניות מסוימות הספירה הבסיסית נמוכה יותר (נויטרופניה אתנית שפירה). הריון מעלה את הנויטרופילים באופן פיזיולוגי.</p>")),
        Section(id="high-neutrophils-causes", level=2, heading="גורמים לנויטרופילים גבוהים (נויטרופיליה)",
                body_html=(
                    "<p>הגורם השכיח ביותר הוא <strong>זיהום חיידקי</strong>. גם דלקת חריפה, מתח, קורטיקוסטרואידים ועישון יכולים להעלות.</p>"
                    "<p>נויטרופיליה גבוהה מאוד ומתמשכת עשויה להצביע על <strong>ניאופלזמות מיאלופרוליפרטיביות</strong>.</p>")),
        Section(id="low-neutrophils-causes", level=2, heading="גורמים לנויטרופילים נמוכים (נויטרופניה)",
                body_html=(
                    "<p>הגורם השכיח ביותר הוא <strong>זיהום נגיפי</strong>. נויטרופניה חמורה (&lt;&nbsp;500) מגבירה מאוד את סיכון הזיהום.</p>"
                    "<p><strong>תרופות</strong> (כימותרפיה, אנטיביוטיקות מסוימות, נוגדי פרכוסים, אנטי-תירואידים)&mdash;בדרך כלל הפיך.</p>"
                    "<p>גורמים נוספים: נויטרופניה אוטואימונית, חוסרי B12/פולאט/נחושת, אלח דם וצורות תורשתיות נדירות.</p>")),
        Section(id="absolute-vs-percentage", level=2, heading="ספירה מוחלטת מול אחוז",
                body_html=(
                    "<p><strong>הספירה המוחלטת (ANC)</strong> אמינה יותר קלינית מהאחוז, כי האחוז עלול להטעות אם ה-WBC הכולל חריג.</p>"
                    "<p>חישוב: <strong>ANC = WBC &times; (Neut % &divide; 100)</strong>.</p>")),
        Section(id="symptoms", level=2, heading="תסמינים הקשורים לשינויי נויטרופילים",
                body_html=(
                    "<p><strong>נויטרופיליה</strong> עצמה לרוב אינה גורמת תסמינים; התסמינים מגיעים מהגורם הבסיסי.</p>"
                    "<p><strong>נויטרופניה חמורה</strong> חושפת לזיהומים: אפטות בפה, כאב גרון, זיהומי עור, חום. נויטרופניה חום היא מצב חירום רפואי.</p>")),
        Section(id="related-tests", level=2, heading="בדיקות קשורות",
                body_html=(
                    "<p>נויטרופילים הם חלק מנוסחת הדם הכוללת <a href=\"/he/blog/lymphocytes-high-or-low\">לימפוציטים</a>, "
                    "<a href=\"/he/blog/monocytes-high-meaning\">מונוציטים</a>, אאוזינופילים ובזופילים.</p>"
                    "<p>לפי ההקשר: CRP, פרוקלציטונין, תרביות דם, משטח דם, ביופסיית מח עצם או נוגדני אנטי-נויטרופילים.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא?",
                body_html=(
                    "<p>דברו עם הרופא אם הנויטרופילים חורגים מהטווח. פנו <strong>בדחיפות</strong> אם יש נויטרופניה + חום או סימני זיהום.</p>"
                    "<p>נויטרופיליה מתמשכת לא מוסברת עם עייפות, הזעות לילה או ירידה במשקל מצדיקה הפניה להמטולוג.</p>")),
        Section(id="how-norya-helps", level=2, heading="איך Norya עוזרת",
                body_html=(
                    "<p>Norya לא מאבחנת&mdash;אנחנו עוזרים לכם להתכונן. העלו את הדוח ב-<a href=\"/analyze\">noryaai.com/analyze</a> "
                    "לסיכום ברור של הנויטרופילים ונוסחת הדם.</p>"
                    "<p>אפשרויות ומחירים: <a href=\"/pricing\">עמוד מחירים</a>.</p>")),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html=(
                    '<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> '
                    'דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>')),
    ]


# ---------------------------------------------------------------------------
# Hindi
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="न्यूट्रोफिल हाई या लो: आपकी WBC डिफरेंशियल को समझें",
                body_html=(
                    "<p>जब CBC में WBC डिफरेंशियल शामिल होता है, तो न्यूट्रोफिल आमतौर पर पहली लाइन होती है जिस पर नज़र जाती है। "
                    "ये सबसे प्रचुर प्रकार की वाइट ब्लड सेल हैं और इनकी संख्या में बदलाव बैक्टीरियल इन्फेक्शन से लेकर दवा के साइड इफेक्ट तक कई चीज़ें बता सकता है।</p>"
                    "<p>यह गाइड बताती है कि न्यूट्रोफिल क्या हैं, रिफरेंस रेंज कैसे पढ़ें, हाई या लो काउंट के कारण, और कब डॉक्टर से मिलें।</p>")),
        Section(id="what-are-neutrophils", level=2, heading="न्यूट्रोफिल क्या हैं और क्या करते हैं?",
                body_html=(
                    "<p><strong>न्यूट्रोफिल</strong> ग्रैनुलोसाइट हैं जिनमें बैक्टीरिया और फंगस को नष्ट करने वाले एंज़ाइम होते हैं। "
                    "बोन मैरो में बनते हैं और ब्लड में सिर्फ 6&ndash;12 घंटे घूमते हैं, फिर टिश्यू में चले जाते हैं&mdash;इम्यून सिस्टम की रैपिड रिस्पॉन्स फ़ोर्स।</p>"
                    "<p>ये पैथोजन को निगलते (फ़ैगोसाइटोसिस) हैं और न्यूट्रोफिल एक्स्ट्रासेलुलर ट्रैप्स (NETs) बनाते हैं। "
                    "रिपोर्ट में ये एब्सोल्यूट काउंट या % के रूप में दिखते हैं; एब्सोल्यूट काउंट क्लिनिकली अधिक उपयोगी माना जाता है।</p>")),
        Section(id="normal-ranges", level=2, heading="सामान्य न्यूट्रोफिल रेंज",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">पैरामीटर</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य वयस्क रेंज</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">एब्सोल्यूट न्यूट्रोफिल काउंट (ANC)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,500&ndash;7,000 सेल/&mu;L</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">प्रतिशत</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70%</td></tr>'
                    "</tbody></table>"
                    "<p>कुछ एथनिक ग्रुप्स में बेसलाइन काउंट कम होता है (बिनाइन एथनिक न्यूट्रोपीनिया)। प्रेग्नेंसी फिज़ियोलॉजिकली न्यूट्रोफिल बढ़ाती है।</p>")),
        Section(id="high-neutrophils-causes", level=2, heading="हाई न्यूट्रोफिल के कारण (न्यूट्रोफीलिया)",
                body_html=(
                    "<p>सबसे आम ट्रिगर <strong>बैक्टीरियल इन्फेक्शन</strong> है। एक्यूट इन्फ्लेमेशन, स्ट्रेस, कॉर्टिकोस्टेरॉइड्स और स्मोकिंग भी बढ़ा सकते हैं।</p>"
                    "<p>बहुत ज़्यादा और लगातार न्यूट्रोफीलिया <strong>माइलोप्रोलिफ़ेरेटिव नियोप्लाज़्म</strong> की ओर इशारा कर सकता है।</p>")),
        Section(id="low-neutrophils-causes", level=2, heading="लो न्यूट्रोफिल के कारण (न्यूट्रोपीनिया)",
                body_html=(
                    "<p>सबसे आम कारण <strong>वायरल इन्फेक्शन</strong> है। गंभीर न्यूट्रोपीनिया (&lt;&nbsp;500) इन्फेक्शन का ख़तरा काफ़ी बढ़ा देता है।</p>"
                    "<p><strong>दवाएं</strong> (कीमोथेरेपी, कुछ एंटीबायोटिक्स, एंटीकॉन्वल्सेंट्स, एंटी-थायरॉइड)&mdash;आमतौर पर दवा बंद करने पर ठीक हो जाता है।</p>"
                    "<p>अन्य कारण: ऑटोइम्यून न्यूट्रोपीनिया, B12/फ़ोलेट/कॉपर की कमी, सेप्सिस और दुर्लभ वंशानुगत रूप।</p>")),
        Section(id="absolute-vs-percentage", level=2, heading="एब्सोल्यूट काउंट बनाम प्रतिशत",
                body_html=(
                    "<p><strong>ANC (एब्सोल्यूट न्यूट्रोफिल काउंट)</strong> क्लिनिकल फ़ैसलों के लिए % से ज़्यादा विश्वसनीय है।</p>"
                    "<p>कैलकुलेशन: <strong>ANC = WBC &times; (Neut % &divide; 100)</strong>।</p>")),
        Section(id="symptoms", level=2, heading="न्यूट्रोफिल बदलाव से जुड़े लक्षण",
                body_html=(
                    "<p><strong>न्यूट्रोफीलिया</strong> खुद शायद ही लक्षण पैदा करता है; लक्षण अंतर्निहित कारण से आते हैं।</p>"
                    "<p><strong>गंभीर न्यूट्रोपीनिया</strong> इन्फेक्शन के प्रति संवेदनशील बनाता है: मुंह के छाले, गले में दर्द, त्वचा संक्रमण, बुखार। "
                    "फ़ेब्राइल न्यूट्रोपीनिया मेडिकल इमरजेंसी है।</p>")),
        Section(id="related-tests", level=2, heading="संबंधित टेस्ट",
                body_html=(
                    "<p>न्यूट्रोफिल WBC डिफरेंशियल का हिस्सा हैं जिसमें <a href=\"/hi/blog/lymphocytes-high-or-low\">लिम्फोसाइट्स</a>, "
                    "<a href=\"/hi/blog/monocytes-high-meaning\">मोनोसाइट्स</a>, इओसिनोफिल्स और बेसोफिल्स भी शामिल हैं।</p>"
                    "<p>स्थिति के अनुसार: CRP, प्रोकैल्सिटोनिन, ब्लड कल्चर, पेरिफ़ेरल स्मीयर, बोन मैरो बायोप्सी।</p>")),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें?",
                body_html=(
                    "<p>रिफरेंस रेंज से बाहर कोई भी न्यूट्रोफिल रिज़ल्ट डॉक्टर से चर्चा करें। "
                    "न्यूट्रोपीनिया + बुखार या इन्फेक्शन के लक्षण हों तो <strong>तुरंत</strong> मेडिकल अटेंशन लें।</p>"
                    "<p>अस्पष्ट लगातार न्यूट्रोफीलिया, खासकर थकान, रात को पसीना या वजन कम होने के साथ, हेमैटोलॉजी रेफ़रल की आवश्यकता हो सकती है।</p>")),
        Section(id="how-norya-helps", level=2, heading="Norya कैसे मदद करता है",
                body_html=(
                    "<p>Norya डायग्नोज़ नहीं करता&mdash;तैयारी में मदद करता है। अपनी ब्लड रिपोर्ट <a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें "
                    "और न्यूट्रोफिल काउंट का स्पष्ट सारांश पाएं।</p>"
                    "<p>प्लान और कीमत: <a href=\"/pricing\">प्राइसिंग पेज</a>।</p>")),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html=(
                    '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> '
                    'अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>')),
    ]


# ---------------------------------------------------------------------------
# Arabic
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="العدلات مرتفعة أو منخفضة: فهم تفريق كريات الدم البيضاء",
                body_html=(
                    "<p>عندما يتضمن تحليل الدم تفريق كريات الدم البيضاء، تكون العدلات (النيوتروفيل) عادة أول سطر تنظر إليه. "
                    "هي أكثر أنواع الكريات البيضاء وفرة، وتغيرات عددها قد تشير إلى عدوى بكتيرية أو تأثيرات دوائية أو إجهاد.</p>"
                    "<p>يشرح هذا الدليل ماهية العدلات، كيفية قراءة النطاقات، أسباب الارتفاع أو الانخفاض، ومتى تستشير الطبيب.</p>")),
        Section(id="what-are-neutrophils", level=2, heading="ما هي العدلات وما وظيفتها؟",
                body_html=(
                    "<p><strong>العدلات</strong> خلايا حبيبية تحتوي إنزيمات قادرة على تدمير البكتيريا والفطريات. "
                    "تُنتج في نقي العظم وتدور في الدم 6&ndash;12 ساعة قبل أن تهاجر للأنسجة&mdash;قوة التدخل السريع للمناعة.</p>"
                    "<p>تبتلع الجراثيم وتُشكّل شِراكاً خارج خلوية (NETs). في التقرير تظهر كقيمة مطلقة أو نسبة مئوية؛ القيمة المطلقة أكثر موثوقية سريرياً.</p>")),
        Section(id="normal-ranges", level=2, heading="النطاقات الطبيعية للعدلات",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المعامل</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق الطبيعي للبالغين</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">العد المطلق (ANC)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,500&ndash;7,000 خلية/&mu;L</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">النسبة المئوية</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">40&ndash;70%</td></tr>'
                    "</tbody></table>"
                    "<p>بعض المجموعات العرقية لديها عد أساسي أقل (نقص عدلات عرقي حميد). الحمل يرفع العدلات فسيولوجياً.</p>")),
        Section(id="high-neutrophils-causes", level=2, heading="أسباب ارتفاع العدلات (كثرة العدلات)",
                body_html=(
                    "<p>السبب الأكثر شيوعاً هو <strong>العدوى البكتيرية</strong>. الالتهاب الحاد والإجهاد والكورتيكوستيرويدات والتدخين يمكنها أيضاً الرفع.</p>"
                    "<p>كثرة عدلات مرتفعة جداً ومستمرة قد تشير إلى <strong>أورام تكاثرية نقوية</strong>.</p>")),
        Section(id="low-neutrophils-causes", level=2, heading="أسباب انخفاض العدلات (قلة العدلات)",
                body_html=(
                    "<p>السبب الأكثر شيوعاً هو <strong>العدوى الفيروسية</strong>. قلة العدلات الشديدة (&lt;&nbsp;500) تزيد خطر العدوى بشكل كبير.</p>"
                    "<p><strong>الأدوية</strong> (كيميائي، بعض المضادات الحيوية، مضادات الاختلاج، مضادات الدرقية)&mdash;عادة قابلة للعكس بعد الإيقاف.</p>"
                    "<p>أسباب أخرى: قلة عدلات مناعية ذاتية، نقص B12/فولات/نحاس، إنتان وأشكال وراثية نادرة.</p>")),
        Section(id="absolute-vs-percentage", level=2, heading="العد المطلق مقابل النسبة المئوية",
                body_html=(
                    "<p><strong>العد المطلق (ANC)</strong> أكثر موثوقية سريرياً من النسبة، لأنها قد تكون مضللة إذا كان WBC الكلي غير طبيعي.</p>"
                    "<p>الحساب: <strong>ANC = WBC &times; (Neut % &divide; 100)</strong>.</p>")),
        Section(id="symptoms", level=2, heading="أعراض مرتبطة بتغيرات العدلات",
                body_html=(
                    "<p><strong>كثرة العدلات</strong> نادراً ما تسبب أعراضاً بذاتها؛ الأعراض تأتي من السبب الكامن.</p>"
                    "<p><strong>قلة العدلات الشديدة</strong> تعرض للعدوى: تقرحات فموية، التهاب حلق، عدوى جلدية، حمى. قلة العدلات الحموية حالة طوارئ طبية.</p>")),
        Section(id="related-tests", level=2, heading="فحوصات ذات صلة",
                body_html=(
                    "<p>العدلات جزء من التفريق الذي يشمل <a href=\"/ar/blog/lymphocytes-high-or-low\">اللمفاويات</a>، "
                    "<a href=\"/ar/blog/monocytes-high-meaning\">الوحيدات</a>، الحمضات والقعدات.</p>"
                    "<p>حسب الحالة: CRP، بروكالسيتونين، مزارع دم، لطاخة محيطية، خزعة نقي عظم أو أضداد مضادة للعدلات.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="متى تراجع الطبيب؟",
                body_html=(
                    "<p>ناقش أي نتيجة عدلات خارج النطاق مع طبيبك. اطلب مساعدة <strong>طارئة</strong> إذا كان لديك قلة عدلات + حمى أو علامات عدوى.</p>"
                    "<p>كثرة عدلات مستمرة غير مفسرة مع إرهاق أو تعرق ليلي أو نقص وزن قد تستدعي إحالة لأمراض الدم.</p>")),
        Section(id="how-norya-helps", level=2, heading="كيف تساعد Norya",
                body_html=(
                    "<p>Norya لا تُشخّص&mdash;نساعدك على التحضير. ارفع تقريرك على <a href=\"/analyze\">noryaai.com/analyze</a> "
                    "للحصول على ملخص واضح للعدلات وتفريق الكريات.</p>"
                    "<p>الخيارات والأسعار: <a href=\"/pricing\">صفحة الأسعار</a>.</p>")),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html=(
                    '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> '
                    'ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>')),
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
            {"question": "What is a normal neutrophil count?", "answer": "The normal absolute neutrophil count (ANC) for adults is roughly 2,500–7,000 cells/μL, or 40–70% of total white blood cells. Ranges may vary between labs."},
            {"question": "What causes high neutrophils?", "answer": "The most common cause is bacterial infection. Other causes include acute inflammation, physiological stress, corticosteroid use, and smoking. Rarely, myeloproliferative disorders can be responsible."},
            {"question": "What causes low neutrophils?", "answer": "Viral infections are the most common cause. Medications (chemotherapy, certain antibiotics, anticonvulsants), autoimmune conditions, nutritional deficiencies, and severe infections can also lower neutrophils."},
            {"question": "What is the difference between absolute and percentage neutrophils?", "answer": "The absolute count (ANC) tells you the actual number of neutrophils per volume of blood, while the percentage shows neutrophils as a fraction of all white cells. ANC is generally more clinically reliable because it is not skewed by changes in other cell types."},
            {"question": "When is low neutrophil count dangerous?", "answer": "Severe neutropenia (ANC below 500 cells/μL) significantly increases infection risk. If you have known neutropenia and develop a fever, seek immediate medical attention as febrile neutropenia is a medical emergency."},
        ],
        "tr": [
            {"question": "Normal nötrofil sayısı nedir?", "answer": "Yetişkinlerde normal mutlak nötrofil sayısı (ANC) yaklaşık 2.500–7.000 hücre/μL veya toplam beyaz kürelerin %40–70'idir."},
            {"question": "Nötrofil yüksekliğine ne sebep olur?", "answer": "En sık neden bakteriyel enfeksiyondur. Akut inflamasyon, stres, kortikosteroidler ve sigara da yükseltebilir. Nadir olarak miyeloproliferatif hastalıklar sorumlu olabilir."},
            {"question": "Nötrofil düşüklüğü ne zaman tehlikelidir?", "answer": "Ciddi nötropeni (ANC 500'ün altında) enfeksiyon riskini belirgin artırır. Nötropeniniz biliniyorsa ve ateşiniz çıkıyorsa febril nötropeni acildir; derhal tıbbi yardım alın."},
        ],
        "es": [
            {"question": "¿Cuál es el recuento normal de neutrófilos?", "answer": "El ANC normal para adultos es aproximadamente 2.500–7.000 células/μL, o 40–70% del total de leucocitos."},
            {"question": "¿Qué causa neutrófilos altos?", "answer": "La causa más frecuente es la infección bacteriana. Inflamación aguda, estrés, corticosteroides y tabaco también los elevan."},
            {"question": "¿Cuándo es peligroso tener neutrófilos bajos?", "answer": "La neutropenia grave (ANC < 500) aumenta mucho el riesgo de infección. Si tiene neutropenia conocida y aparece fiebre, busque atención médica inmediata."},
        ],
        "de": [
            {"question": "Was ist eine normale Neutrophilenzahl?", "answer": "Die normale ANC bei Erwachsenen liegt bei ca. 2.500–7.000 Zellen/μL oder 40–70 % des Gesamt-WBC."},
            {"question": "Was verursacht hohe Neutrophile?", "answer": "Häufigste Ursache ist eine bakterielle Infektion. Entzündung, Stress, Kortikosteroide und Rauchen können den Wert ebenfalls erhöhen."},
            {"question": "Wann sind niedrige Neutrophile gefährlich?", "answer": "Schwere Neutropenie (ANC < 500) erhöht das Infektionsrisiko erheblich. Fieber bei bekannter Neutropenie ist ein Notfall."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de neutrophiles ?", "answer": "Le PNN normal chez l'adulte est environ 2 500–7 000/μL, soit 40–70 % des globules blancs."},
            {"question": "Quelles sont les causes de neutrophiles élevés ?", "answer": "L'infection bactérienne est la cause la plus fréquente. Inflammation aiguë, stress, corticoïdes et tabac peuvent aussi les augmenter."},
            {"question": "Quand la neutropénie est-elle dangereuse ?", "answer": "La neutropénie sévère (PNN < 500) augmente nettement le risque infectieux. Fièvre + neutropénie connue = urgence médicale."},
        ],
        "it": [
            {"question": "Qual è la conta normale dei neutrofili?", "answer": "L'ANC normale negli adulti è circa 2.500–7.000 cellule/μL, ovvero 40–70% dei globuli bianchi totali."},
            {"question": "Cosa causa neutrofili alti?", "answer": "La causa più frequente è l'infezione batterica. Anche infiammazione, stress, cortisonici e fumo possono alzarli."},
            {"question": "Quando la neutropenia è pericolosa?", "answer": "Neutropenia grave (ANC < 500) aumenta molto il rischio infettivo. Febbre + neutropenia nota = emergenza medica."},
        ],
        "he": [
            {"question": "מהי ספירת נויטרופילים תקינה?", "answer": "ANC תקין במבוגרים הוא כ-2,500–7,000 תאים/μL, או 40–70% מכלל הלויקוציטים."},
            {"question": "מה גורם לנויטרופילים גבוהים?", "answer": "הגורם השכיח ביותר הוא זיהום חיידקי. גם דלקת, מתח, קורטיקוסטרואידים ועישון יכולים להעלות."},
            {"question": "מתי נויטרופילים נמוכים מסוכנים?", "answer": "נויטרופניה חמורה (ANC מתחת ל-500) מגבירה מאוד את סיכון הזיהום. חום + נויטרופניה = מצב חירום."},
        ],
        "hi": [
            {"question": "सामान्य न्यूट्रोफिल काउंट कितना होता है?", "answer": "वयस्कों में सामान्य ANC लगभग 2,500–7,000 सेल/μL या कुल WBC का 40–70% है।"},
            {"question": "हाई न्यूट्रोफिल किससे होता है?", "answer": "सबसे आम कारण बैक्टीरियल इन्फेक्शन है। इन्फ्लेमेशन, स्ट्रेस, कॉर्टिकोस्टेरॉइड्स और स्मोकिंग भी बढ़ा सकते हैं।"},
            {"question": "लो न्यूट्रोफिल कब ख़तरनाक होता है?", "answer": "गंभीर न्यूट्रोपीनिया (ANC < 500) इन्फेक्शन का ख़तरा काफ़ी बढ़ा देता है। बुखार + ज्ञात न्यूट्रोपीनिया = मेडिकल इमरजेंसी।"},
        ],
        "ar": [
            {"question": "ما هو العدد الطبيعي للعدلات؟", "answer": "العد المطلق الطبيعي (ANC) للبالغين حوالي 2,500–7,000 خلية/μL أو 40–70% من إجمالي الكريات البيضاء."},
            {"question": "ما أسباب ارتفاع العدلات؟", "answer": "السبب الأكثر شيوعاً هو العدوى البكتيرية. الالتهاب الحاد والإجهاد والكورتيكوستيرويدات والتدخين يمكنها أيضاً الرفع."},
            {"question": "متى يكون انخفاض العدلات خطيراً؟", "answer": "قلة العدلات الشديدة (ANC أقل من 500) تزيد خطر العدوى بشكل كبير. حمى + قلة عدلات معروفة = حالة طوارئ طبية."},
        ],
    }
