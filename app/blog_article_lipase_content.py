# -*- coding: utf-8 -*-
"""
Lipase (Lipaz) blog article — full body content for all 9 languages.
Used by blog_i18n._article_lipase().
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
            heading="Lipaz kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>lipaz</strong> değerini gördüğünüzde bu enzimin "
                "ne anlama geldiğini ve yüksek çıkmasının sağlığınız açısından ne ifade ettiğini merak "
                "etmeniz doğaldır. Lipaz, başta pankreas olmak üzere sindirim sistemindeki yağların "
                "parçalanmasında kritik rol oynayan bir enzimdir ve <strong>lipaz yüksekliği</strong> "
                "özellikle pankreatit başta olmak üzere çeşitli hastalıklara işaret edebilir.</p>"
                "<p>Bu rehber lipaz kan testinin ne anlama geldiğini, normal referans aralıklarını, "
                "yükseklik nedenlerini, pankreatit belirtilerini ve ne zaman doktora başvurmanız "
                "gerektiğini sade bir dille açıklamayı amaçlıyor. Amacımız teşhis koymak değil; "
                "sonuçlarınızı daha iyi anlayarak hekiminizle verimli bir görüşme yapmanıza yardımcı "
                "olmaktır.</p>"
                "<p>Lipaz, pankreatik hastalıkların tanısında amilazdan daha spesifik bir belirteçtir. "
                "Yüksek lipaz seviyesi her zaman pankreatit anlamına gelmez; ancak normalin 3 katını "
                "aşan değerler klinik olarak çok anlamlıdır ve acil değerlendirme gerektirir.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Lipaz nedir?",
            body_html=(
                "<p><strong>Lipaz</strong>, trigliseritleri (yağları) yağ asitleri ve gliserole parçalayan "
                "bir hidrolaz enzimidir. Vücutta başlıca pankreas tarafından üretilir; ancak mide, dil, "
                "karaciğer ve bağırsak mukozası gibi farklı dokular da az miktarda lipaz salgılar. "
                "Pankreatik lipaz, yağ sindiriminin en önemli bileşenidir.</p>"
                "<p>Pankreas, lipazı inaktif bir öncü (zimogen) form olan <em>prolipaz</em> olarak "
                "salgılar; bu enzim duodenumda (onikiparmak bağırsağı) kolipaz ve safra tuzlarının "
                "yardımıyla aktif hale gelir. Aktif lipaz, besinlerle alınan yağların emilimi için "
                "zorunludur — bu enzim olmadan yağ sindirimi büyük ölçüde bozulur.</p>"
                "<p>Kanda normalde az miktarda lipaz bulunur. Pankreas hasarlandığında veya pankreas "
                "kanalı tıkandığında, enzim kana sızar ve serum lipaz düzeyi yükselir. Bu nedenle "
                "lipaz testi, pankreatik hastalıkların tanısında en değerli laboratuvar "
                "araçlarından biridir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Lipaz normal değerleri (referans aralıkları)",
            body_html=(
                "<p>Lipaz düzeyi basit bir kan testiyle ölçülür. Yaygın olarak kabul edilen referans "
                "aralığı aşağıdaki tabloda özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Durum</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Lipaz (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Pankreatit şüphesi (3× üst sınır)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p><strong>Normal serum lipaz aralığı genellikle 0&ndash;60&nbsp;U/L</strong> olarak kabul "
                "edilir; ancak laboratuvarlar arasında küçük farklılıklar olabilir. Akut pankreatit tanısı "
                "için lipaz değerinin normalin üst sınırının <em>en az 3 katı</em> olması (genellikle "
                "&gt;180&nbsp;U/L) klinik kriter olarak kullanılır.</p>"
                "<p>Lipaz düzeyi yemek yeme veya açlık durumundan çok az etkilenir, bu nedenle test "
                "genellikle aç karnına yapılması zorunlu değildir. Ancak bazı laboratuvarlar 8&ndash;12 "
                "saatlik açlık önerebilir. Sonucunuzu kendi laboratuvarınızın referans aralığıyla "
                "karşılaştırmanız önemlidir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Lipaz yüksekliğinin nedenleri",
            body_html=(
                "<p>Serum lipaz düzeyinin yükselmesi çeşitli nedenlere bağlı olabilir. En sık "
                "karşılaşılan durumlar şunlardır:</p>"
                "<ul>"
                "<li><strong>Akut pankreatit:</strong> Lipaz yüksekliğinin en yaygın ve en önemli "
                "nedenidir. Genellikle normalin 3 katından fazla yükselir ve safra taşları ile alkol "
                "kullanımı başlıca tetikleyicilerdir.</li>"
                "<li><strong>Kronik pankreatit:</strong> İlerleyen pankreas hasarında lipaz düzeyinde "
                "hafif-orta derecede yükseklik görülebilir; ancak ileri evrelerde pankreas harap "
                "olduğundan lipaz paradoks olarak düşük kalabilir.</li>"
                "<li><strong>Safra taşları (kolelitiyaz):</strong> Safra kanalını tıkayan taşlar "
                "pankreas kanalına da bası yaparak lipaz yüksekliğine neden olabilir.</li>"
                "<li><strong>Pankreas kanseri:</strong> Pankreas tümörleri kanalı tıkayarak veya "
                "doku hasarı yaparak enzim sızıntısına yol açabilir.</li>"
                "<li><strong>Böbrek hastalığı:</strong> Lipaz böbreklerden atıldığından, böbrek "
                "fonksiyon bozukluğunda serum düzeyi yükselebilir.</li>"
                "<li><strong>Bağırsak tıkanıklığı:</strong> İleus veya mekanik obstrüksiyonda lipaz "
                "hafifçe yükselebilir.</li>"
                "<li><strong>İlaçlar:</strong> Bazı ilaçlar (örneğin opioidler, tiazid diüretikler, "
                "valproik asit) pankreatite veya doğrudan enzim yüksekliğine neden olabilir.</li>"
                "</ul>"
                "<p>Lipaz, pankreatik hastalıklarda amilazdan daha spesifik bir belirteçtir. Amilaz "
                "tükürük bezleri gibi pankreas dışı kaynaklardan da yükselebilirken, lipaz yüksekliği "
                "pankreasa daha güçlü bir şekilde işaret eder. İlgili karaciğer enzimleri hakkında "
                "daha fazla bilgi için <a href=\"/tr/blog/alt-ast-liver-enzymes-meaning\">ALT &amp; AST "
                "rehberimizi</a> okuyabilirsiniz.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Pankreatit belirtileri",
            body_html=(
                "<p>Lipaz yüksekliğinin en sık nedeni olan akut pankreatitin tipik belirtileri "
                "şunlardır:</p>"
                "<ul>"
                "<li><strong>Şiddetli karın ağrısı:</strong> Genellikle üst karında başlar ve sırta "
                "doğru yayılır. Yemek yedikten sonra kötüleşebilir ve öne eğilmekle hafifleyebilir.</li>"
                "<li><strong>Bulantı ve kusma:</strong> Ağrıyla birlikte sıklıkla görülür ve "
                "dehidrasyona yol açabilir.</li>"
                "<li><strong>Ateş:</strong> Enflamasyon veya enfeksiyona bağlı olarak ortaya "
                "çıkabilir.</li>"
                "<li><strong>Abdominal hassasiyet ve şişkinlik:</strong> Karına dokunulduğunda ağrı "
                "ve batında distansiyon görülebilir.</li>"
                "<li><strong>Hızlı nabız:</strong> Şiddetli ağrı ve dehidrasyona bağlı olarak "
                "taşikardi gelişebilir.</li>"
                "</ul>"
                "<p>Kronik pankreatitte ise tekrarlayan karın ağrısı, kilo kaybı, yağlı dışkı "
                "(steatore) ve diyabet gelişimi gibi uzun süreli belirtiler ön plana çıkar. Belirtiler "
                "kişiden kişiye değişebilir; hafif lipaz yüksekliği bazen tamamen asemptomatik "
                "olabilir.</p>"
                "<p>Akut pankreatit ciddi bir acildir; yukarıdaki belirtiler varsa derhal tıbbi yardım "
                "alınmalıdır.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlişkili testler",
            body_html=(
                "<p>Lipaz yüksekliği saptandığında nedeni belirlemek ve pankreası değerlendirmek için "
                "ek testler istenir:</p>"
                "<ul>"
                "<li><strong>Amilaz:</strong> Lipazla birlikte pankreatit değerlendirmesinde kullanılır; "
                "ancak lipaz daha spesifiktir.</li>"
                "<li><strong>ALT ve AST:</strong> Karaciğer enzim yüksekliği safra taşına bağlı "
                "pankreatit şüphesini artırır. Detaylı bilgi için "
                "<a href=\"/tr/blog/alt-ast-liver-enzymes-meaning\">ALT &amp; AST rehberimize</a> "
                "bakabilirsiniz.</li>"
                "<li><strong>GGT ve bilirubin:</strong> Safra yolu tıkanıklığını değerlendirmek "
                "için kullanılır.</li>"
                "<li><strong>Karın ultrasonografisi:</strong> Safra taşları ve pankreas "
                "morfolojisini değerlendirmek için ilk tercih görüntüleme yöntemidir.</li>"
                "<li><strong>Abdominal BT (bilgisayarlı tomografi):</strong> Pankreatit şiddetini, "
                "nekroz varlığını ve komplikasyonları değerlendirmede altın standarttır.</li>"
                "<li><strong>Trigliseritler:</strong> Çok yüksek trigliserit düzeyleri "
                "(&gt;1000&nbsp;mg/dL) pankreatite neden olabilir.</li>"
                "</ul>"
                "<p>Bu testlerin birlikte değerlendirilmesi, doğru tanı ve tedavi planlaması için "
                "büyük önem taşır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda acil olarak bir gastroenteroloji uzmanına veya acil servise "
                "başvurmanız gerekir:</p>"
                "<ul>"
                "<li>Şiddetli, sürekli üst karın ağrısı (özellikle sırta yayılıyorsa)</li>"
                "<li>Kontrol edilemeyen bulantı ve kusma</li>"
                "<li>Yüksek ateş ve genel kötü hissediyorsanız</li>"
                "<li>Kan tahlilinde lipaz değeriniz normalin 3 katından fazlaysa</li>"
                "<li>Bilinen safra taşı öykünüz varsa ve yukarıdaki belirtiler eşlik ediyorsa</li>"
                "</ul>"
                "<p>Akut pankreatit hayatı tehdit edebilecek ciddi bir durumdur ve hastane ortamında "
                "tedavi gerektirir. Erken müdahale komplikasyon riskini önemli ölçüde azaltır. "
                "Tedavide intravenöz sıvı desteği, ağrı kontrolü ve gerekirse girişimsel prosedürler "
                "uygulanır.</p>"
                "<p>Hafif lipaz yüksekliği (normalin 1&ndash;3 katı arası) her zaman acil değildir; "
                "ancak altta yatan nedeni belirlemek için yine de hekiminizle görüşmelisiniz.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI lipaz sonuçlarınızı nasıl değerlendirir?",
            body_html=(
                "<p><strong>NoryaAI</strong>, kan tahlili raporunuzu yüklediğinizde lipaz dahil tüm "
                "biyobelirteçlerinizi yaşınıza, cinsiyetinize ve klinik bağlamınıza göre analiz eder. "
                "Yapay zekâ destekli sistemimiz referans aralık dışı değerleri vurgular, olası nedenleri "
                "özetler ve hekiminize sormak isteyebileceğiniz soruları önerir.</p>"
                "<p>Sonuçlarınızı hemen değerlendirmek için <a href=\"/analyze\">lab raporunuzu "
                "yükleyin</a>. Farklı plan seçeneklerimiz hakkında bilgi almak için "
                "<a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edebilirsiniz. NoryaAI "
                "hekim muayenesinin yerini almaz; amacımız sizi bilgilendirerek doktorunuzla daha "
                "verimli bir görüşme yapmanızı sağlamaktır.</p>"
                "<p>Lipaz değeriniz yüksekse panik yapmayın; ancak özellikle karın ağrısı gibi "
                "belirtiler eşlik ediyorsa bir sağlık profesyonelinden vakit kaybetmeden "
                "değerlendirme almanız önemlidir.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Yasal uyarı",
            body_html=(
                "<p><strong>Bu içerik yalnızca bilgilendirme amacıyla hazırlanmıştır ve tıbbi tavsiye, "
                "tanı veya tedavi yerine geçmez.</strong> Kan tahlili sonuçlarınızı mutlaka bir sağlık "
                "profesyoneli ile birlikte değerlendirin. NoryaAI bir hekim muayenesi veya tıbbi "
                "konsültasyon yerine geçmez. Sağlık kararlarınızı her zaman doktorunuza danışarak verin. "
                '<a href="/analyze">Analiz sayfamızda</a> sonuçlarınız hakkında ön bilgi edinebilirsiniz.</p>'
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
            heading="Lipase blood test: what your results mean",
            body_html=(
                "<p>If your lab report shows an elevated <strong>lipase</strong> level, you may be "
                "wondering what this enzyme does and whether you should be worried. Lipase is a "
                "digestive enzyme produced primarily by the pancreas, and a <strong>high lipase</strong> "
                "result is one of the most important clues to pancreatic disease, particularly acute "
                "pancreatitis.</p>"
                "<p>This guide explains what a <strong>lipase blood test</strong> measures, normal "
                "reference ranges, causes of elevated lipase, symptoms of pancreatitis, and when to "
                "seek medical attention. Our goal is not to diagnose — it is to help you understand "
                "your results so you can have a more productive conversation with your doctor.</p>"
                "<p>Lipase is more specific for pancreatic disease than amylase, the other commonly "
                "tested pancreatic enzyme. A lipase level more than three times the upper limit of "
                "normal is clinically very significant and warrants urgent evaluation.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is lipase?",
            body_html=(
                "<p><strong>Lipase</strong> is a hydrolase enzyme that breaks down triglycerides (fats) "
                "into fatty acids and glycerol. It is produced mainly by the pancreas, although smaller "
                "amounts are also secreted by the stomach, tongue, liver, and intestinal mucosa. "
                "Pancreatic lipase is the single most important enzyme for dietary fat digestion.</p>"
                "<p>The pancreas releases lipase in an inactive precursor form called <em>prolipase</em>, "
                "which is activated in the duodenum by colipase and bile salts. Without active lipase, "
                "fat digestion is severely impaired, leading to malabsorption and steatorrhea (fatty "
                "stools).</p>"
                "<p>In healthy individuals, only small amounts of lipase circulate in the blood. When "
                "the pancreas is damaged or its duct is obstructed, lipase leaks into the bloodstream "
                "and serum levels rise. This is why the lipase test is one of the most valuable "
                "laboratory tools for diagnosing pancreatic disease.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal lipase levels (reference ranges)",
            body_html=(
                "<p>Lipase is measured with a simple blood draw. The table below summarises the "
                "commonly accepted reference range:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Status</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Lipase (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Pancreatitis threshold (3× upper limit)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p>The <strong>normal serum lipase range is generally 0&ndash;60&nbsp;U/L</strong>, "
                "although exact cut-offs may vary between laboratories. For the diagnosis of acute "
                "pancreatitis, a lipase level at least <em>three times</em> the upper limit of normal "
                "(typically &gt;180&nbsp;U/L) is used as a clinical criterion.</p>"
                "<p>Lipase is minimally affected by food intake, so fasting is not strictly required "
                "before the test, though some laboratories recommend an 8&ndash;12-hour fast. Always "
                "compare your result with your own laboratory&rsquo;s reference range.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high lipase",
            body_html=(
                "<p>An elevated serum lipase can result from several conditions. The most common "
                "are:</p>"
                "<ul>"
                "<li><strong>Acute pancreatitis:</strong> By far the most important cause. Lipase "
                "typically rises to more than three times the upper limit of normal. The two leading "
                "triggers are gallstones and alcohol use.</li>"
                "<li><strong>Chronic pancreatitis:</strong> Ongoing pancreatic damage may cause mild "
                "to moderate lipase elevations, although in advanced disease the gland may be so "
                "destroyed that lipase is paradoxically low.</li>"
                "<li><strong>Gallstones (cholelithiasis):</strong> Stones blocking the common bile "
                "duct can obstruct the pancreatic duct, causing lipase to rise.</li>"
                "<li><strong>Pancreatic cancer:</strong> Tumours may obstruct the duct or damage "
                "tissue, leading to enzyme leakage.</li>"
                "<li><strong>Kidney disease:</strong> Because lipase is cleared by the kidneys, "
                "impaired renal function can elevate serum levels.</li>"
                "<li><strong>Bowel obstruction:</strong> Ileus or mechanical obstruction may cause "
                "a mild lipase increase.</li>"
                "<li><strong>Medications:</strong> Opioids, thiazide diuretics, and valproic acid, "
                "among others, can trigger pancreatitis or directly raise lipase.</li>"
                "</ul>"
                "<p>Lipase is more specific for pancreatic disease than amylase. Amylase can be "
                "elevated by salivary-gland disorders and other non-pancreatic sources, whereas "
                "lipase elevation points more strongly to the pancreas. For more on liver enzymes "
                "that are often assessed alongside lipase, see our "
                "<a href=\"/en/blog/alt-ast-liver-enzymes-meaning\">ALT &amp; AST guide</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of pancreatitis",
            body_html=(
                "<p>Because acute pancreatitis is the most common reason for a significantly elevated "
                "lipase, here are its hallmark symptoms:</p>"
                "<ul>"
                "<li><strong>Severe upper abdominal pain:</strong> Typically starts suddenly in the "
                "epigastric area and radiates to the back. It may worsen after eating and improve "
                "when leaning forward.</li>"
                "<li><strong>Nausea and vomiting:</strong> Frequently accompany the pain and can "
                "lead to dehydration.</li>"
                "<li><strong>Fever:</strong> May develop due to inflammation or secondary infection.</li>"
                "<li><strong>Abdominal tenderness and distension:</strong> The abdomen may be tender "
                "to touch with visible bloating.</li>"
                "<li><strong>Rapid pulse:</strong> Tachycardia can result from severe pain and "
                "dehydration.</li>"
                "</ul>"
                "<p>In chronic pancreatitis, symptoms include recurring abdominal pain, weight loss, "
                "fatty stools (steatorrhea), and the development of diabetes. Symptoms vary among "
                "individuals; a mildly elevated lipase may sometimes be completely asymptomatic.</p>"
                "<p>Acute pancreatitis is a medical emergency — if you experience the symptoms above, "
                "seek medical attention immediately.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>When lipase is elevated, additional tests help identify the cause and assess the "
                "pancreas:</p>"
                "<ul>"
                "<li><strong>Amylase:</strong> Often ordered alongside lipase for pancreatitis "
                "evaluation, though lipase is more specific.</li>"
                "<li><strong>ALT and AST:</strong> Elevated liver enzymes raise suspicion for "
                "gallstone-induced pancreatitis. Learn more in our "
                "<a href=\"/en/blog/alt-ast-liver-enzymes-meaning\">ALT &amp; AST guide</a>.</li>"
                "<li><strong>GGT and bilirubin:</strong> Used to evaluate bile-duct obstruction.</li>"
                "<li><strong>Abdominal ultrasound:</strong> First-line imaging to detect gallstones "
                "and assess pancreatic morphology.</li>"
                "<li><strong>Abdominal CT scan:</strong> The gold standard for grading pancreatitis "
                "severity, detecting necrosis, and evaluating complications.</li>"
                "<li><strong>Triglycerides:</strong> Very high triglyceride levels "
                "(&gt;1,000&nbsp;mg/dL) can trigger pancreatitis.</li>"
                "</ul>"
                "<p>Evaluating these tests together is essential for accurate diagnosis and treatment "
                "planning.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>Seek urgent medical attention — including the emergency department — if:</p>"
                "<ul>"
                "<li>You have severe, persistent upper abdominal pain (especially if radiating to "
                "the back)</li>"
                "<li>You experience uncontrollable nausea and vomiting</li>"
                "<li>You develop a high fever and feel generally unwell</li>"
                "<li>Your blood test shows lipase more than three times the upper limit of normal</li>"
                "<li>You have a known history of gallstones with accompanying symptoms</li>"
                "</ul>"
                "<p>Acute pancreatitis is a potentially life-threatening condition that requires "
                "hospital-based treatment. Early intervention significantly reduces the risk of "
                "complications. Treatment typically involves intravenous fluids, pain management, "
                "and potentially interventional procedures.</p>"
                "<p>A mild lipase elevation (1&ndash;3 times normal) is not always an emergency but "
                "should still be discussed with your doctor to identify the underlying cause.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How NoryaAI helps you understand lipase results",
            body_html=(
                "<p><strong>NoryaAI</strong> analyses your full blood-test report — including lipase — "
                "in the context of your age, sex, and clinical background. Our AI-powered system "
                "highlights out-of-range values, summarises possible causes, and suggests questions you "
                "may want to ask your doctor.</p>"
                "<p>Ready to get started? <a href=\"/analyze\">Upload your lab report</a> for an instant "
                "analysis. Visit our <a href=\"/pricing\">pricing page</a> to explore plan options. "
                "NoryaAI does not replace a physician; our goal is to empower you with information so "
                "your next medical consultation is more productive.</p>"
                "<p>If your lipase is elevated, do not panic — but if you are experiencing abdominal "
                "pain or other symptoms of pancreatitis, seek prompt medical evaluation.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This content is for informational purposes only and does not constitute "
                "medical advice, diagnosis, or treatment.</strong> Always discuss your blood-test "
                "results with a qualified healthcare professional. NoryaAI is not a substitute for a "
                "medical consultation. Make all health-related decisions in consultation with your "
                'doctor. <a href="/analyze">Visit our analysis page</a> for preliminary insights '
                "into your results.</p>"
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
            heading="Análisis de lipasa en sangre: qué significan sus resultados",
            body_html=(
                "<p>Si su informe de laboratorio muestra un nivel elevado de <strong>lipasa</strong>, "
                "es natural preguntarse qué hace esta enzima y si debe preocuparse. La lipasa es una "
                "enzima digestiva producida principalmente por el páncreas, y un resultado "
                "<strong>elevado de lipasa</strong> es una de las pistas más importantes de enfermedad "
                "pancreática, especialmente pancreatitis aguda.</p>"
                "<p>Esta guía explica qué mide el <strong>análisis de lipasa</strong>, los rangos de "
                "referencia normales, las causas de la lipasa elevada, los síntomas de pancreatitis y "
                "cuándo buscar atención médica. Nuestro objetivo no es diagnosticar, sino ayudarle a "
                "comprender sus resultados para una consulta más productiva con su médico.</p>"
                "<p>La lipasa es más específica para la enfermedad pancreática que la amilasa. Un nivel "
                "de lipasa superior a tres veces el límite superior normal es clínicamente muy "
                "significativo y requiere evaluación urgente.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es la lipasa?",
            body_html=(
                "<p>La <strong>lipasa</strong> es una enzima hidrolasa que descompone los triglicéridos "
                "(grasas) en ácidos grasos y glicerol. Se produce principalmente en el páncreas, aunque "
                "también la secretan en pequeñas cantidades el estómago, la lengua, el hígado y la "
                "mucosa intestinal. La lipasa pancreática es la enzima más importante para la digestión "
                "de grasas de la dieta.</p>"
                "<p>El páncreas libera lipasa en una forma precursora inactiva llamada <em>prolipasa</em>, "
                "que se activa en el duodeno por la colipasa y las sales biliares. Sin lipasa activa, "
                "la digestión de grasas se deteriora gravemente, provocando malabsorción y esteatorrea "
                "(heces grasas).</p>"
                "<p>En personas sanas, solo circulan pequeñas cantidades de lipasa en sangre. Cuando el "
                "páncreas se daña o su conducto se obstruye, la lipasa se filtra al torrente sanguíneo y "
                "los niveles séricos aumentan. Por ello, la lipasa es una de las herramientas de "
                "laboratorio más valiosas para el diagnóstico pancreático.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de lipasa (rangos de referencia)",
            body_html=(
                "<p>La lipasa se mide con una simple extracción de sangre. La siguiente tabla resume "
                "el rango de referencia habitualmente aceptado:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Estado</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Lipasa (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Umbral de pancreatitis (3× límite superior)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p>El <strong>rango normal de lipasa sérica es generalmente 0&ndash;60&nbsp;U/L</strong>, "
                "aunque puede variar entre laboratorios. Para el diagnóstico de pancreatitis aguda se "
                "utiliza como criterio un nivel de lipasa al menos <em>tres veces</em> el límite "
                "superior normal.</p>"
                "<p>La lipasa se ve poco afectada por la ingesta de alimentos, por lo que el ayuno no "
                "es estrictamente necesario. Compare siempre su resultado con el rango de su "
                "laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de lipasa alta",
            body_html=(
                "<p>Una lipasa sérica elevada puede deberse a diversas causas. Las más frecuentes "
                "son:</p>"
                "<ul>"
                "<li><strong>Pancreatitis aguda:</strong> La causa más importante. La lipasa suele "
                "superar 3 veces el límite superior. Los desencadenantes principales son los cálculos "
                "biliares y el consumo de alcohol.</li>"
                "<li><strong>Pancreatitis crónica:</strong> Daño pancreático progresivo con elevaciones "
                "leves a moderadas.</li>"
                "<li><strong>Cálculos biliares:</strong> Pueden obstruir el conducto pancreático.</li>"
                "<li><strong>Cáncer de páncreas:</strong> Obstrucción ductal o daño tisular.</li>"
                "<li><strong>Enfermedad renal:</strong> Disminución del aclaramiento renal de "
                "lipasa.</li>"
                "<li><strong>Obstrucción intestinal:</strong> Íleo o obstrucción mecánica.</li>"
                "<li><strong>Fármacos:</strong> Opioides, diuréticos tiazídicos, ácido valproico, "
                "entre otros.</li>"
                "</ul>"
                "<p>La lipasa es más específica para enfermedad pancreática que la amilasa. Para más "
                "información sobre enzimas hepáticas, consulte nuestra "
                "<a href=\"/es/blog/alt-ast-liver-enzymes-meaning\">guía de ALT y AST</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de pancreatitis",
            body_html=(
                "<p>Los síntomas típicos de la pancreatitis aguda, la causa más frecuente de lipasa "
                "muy elevada, incluyen:</p>"
                "<ul>"
                "<li><strong>Dolor abdominal superior intenso:</strong> Comienza en el epigastrio y "
                "se irradia a la espalda. Empeora tras comer y puede aliviarse al inclinarse hacia "
                "delante.</li>"
                "<li><strong>Náuseas y vómitos:</strong> Acompañan frecuentemente al dolor y pueden "
                "provocar deshidratación.</li>"
                "<li><strong>Fiebre:</strong> Por inflamación o infección secundaria.</li>"
                "<li><strong>Sensibilidad abdominal y distensión:</strong> Dolor a la palpación y "
                "abdomen hinchado.</li>"
                "<li><strong>Taquicardia:</strong> Por dolor intenso y deshidratación.</li>"
                "</ul>"
                "<p>En la pancreatitis crónica predominan dolor recurrente, pérdida de peso, "
                "esteatorrea y desarrollo de diabetes. Una elevación leve de lipasa puede ser "
                "asintomática.</p>"
                "<p>La pancreatitis aguda es una urgencia médica — si presenta estos síntomas, "
                "busque atención inmediata.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p>Ante una lipasa elevada se solicitan pruebas complementarias:</p>"
                "<ul>"
                "<li><strong>Amilasa:</strong> Se solicita junto con la lipasa, aunque esta última "
                "es más específica.</li>"
                "<li><strong>ALT y AST:</strong> Su elevación sugiere pancreatitis biliar. Vea "
                "nuestra <a href=\"/es/blog/alt-ast-liver-enzymes-meaning\">guía de ALT y AST</a>.</li>"
                "<li><strong>GGT y bilirrubina:</strong> Para evaluar obstrucción biliar.</li>"
                "<li><strong>Ecografía abdominal:</strong> Primera línea para detectar cálculos "
                "biliares.</li>"
                "<li><strong>TC abdominal:</strong> Referencia para valorar la gravedad de la "
                "pancreatitis.</li>"
                "<li><strong>Triglicéridos:</strong> Niveles muy altos (&gt;1.000&nbsp;mg/dL) "
                "pueden causar pancreatitis.</li>"
                "</ul>"
                "<p>La evaluación conjunta de estas pruebas es fundamental para un diagnóstico "
                "y tratamiento adecuados.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Busque atención médica urgente si:</p>"
                "<ul>"
                "<li>Tiene dolor abdominal superior intenso y persistente</li>"
                "<li>Presenta náuseas y vómitos incontrolables</li>"
                "<li>Desarrolla fiebre alta y malestar general</li>"
                "<li>Su lipasa supera 3 veces el límite superior normal</li>"
                "<li>Tiene antecedentes de cálculos biliares con síntomas acompañantes</li>"
                "</ul>"
                "<p>La pancreatitis aguda es potencialmente mortal y requiere tratamiento hospitalario. "
                "La intervención temprana reduce significativamente el riesgo de complicaciones.</p>"
                "<p>Una elevación leve de lipasa no siempre es urgente, pero debe comentarse con su "
                "médico para identificar la causa subyacente.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo le ayuda NoryaAI con sus resultados de lipasa",
            body_html=(
                "<p><strong>NoryaAI</strong> analiza su informe completo de análisis de sangre, incluida "
                "la lipasa, teniendo en cuenta su edad, sexo y contexto clínico. Nuestro sistema de IA "
                "resalta los valores fuera de rango y sugiere preguntas para su médico.</p>"
                "<p><a href=\"/analyze\">Suba su informe de laboratorio</a> para un análisis instantáneo. "
                "Visite nuestra <a href=\"/pricing\">página de precios</a> para conocer los planes "
                "disponibles. NoryaAI no sustituye al médico; le ayuda a llegar más informado a su "
                "consulta.</p>"
                "<p>Si su lipasa está elevada, no se alarme, pero si tiene dolor abdominal u otros "
                "síntomas de pancreatitis, busque evaluación médica sin demora.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso legal",
            body_html=(
                "<p><strong>Este contenido es meramente informativo y no constituye consejo médico, "
                "diagnóstico ni tratamiento.</strong> Consulte siempre sus resultados con un profesional "
                "sanitario cualificado. NoryaAI no sustituye una consulta médica. "
                '<a href="/analyze">Visite nuestra página de análisis</a> para información preliminar '
                "sobre sus resultados.</p>"
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
            heading="Lipase-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Wenn Ihr Laborbericht einen erhöhten <strong>Lipase</strong>-Wert zeigt, fragen Sie "
                "sich möglicherweise, welche Funktion dieses Enzym hat und ob Anlass zur Sorge besteht. "
                "Lipase ist ein Verdauungsenzym, das hauptsächlich von der Bauchspeicheldrüse produziert "
                "wird, und eine <strong>erhöhte Lipase</strong> ist einer der wichtigsten Hinweise auf "
                "eine Pankreaserkrankung, insbesondere akute Pankreatitis.</p>"
                "<p>Dieser Ratgeber erklärt, was der <strong>Lipase-Bluttest</strong> misst, welche "
                "Referenzbereiche gelten, welche Ursachen eine Lipase-Erhöhung haben kann, welche "
                "Symptome bei Pankreatitis auftreten und wann Sie ärztliche Hilfe suchen sollten.</p>"
                "<p>Lipase ist für Pankreaserkrankungen spezifischer als Amylase. Ein Lipasewert über "
                "dem Dreifachen des oberen Grenzwerts ist klinisch sehr bedeutsam und erfordert eine "
                "dringende Abklärung.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist Lipase?",
            body_html=(
                "<p><strong>Lipase</strong> ist ein Hydrolase-Enzym, das Triglyzeride (Fette) in "
                "Fettsäuren und Glycerol spaltet. Sie wird hauptsächlich von der Bauchspeicheldrüse "
                "produziert; kleinere Mengen werden auch von Magen, Zunge, Leber und Darmschleimhaut "
                "sezerniert. Die Pankreaslipase ist das wichtigste Enzym für die Fettverdauung.</p>"
                "<p>Das Pankreas setzt Lipase als inaktive Vorstufe (<em>Prolipase</em>) frei, die im "
                "Duodenum durch Colipase und Gallensalze aktiviert wird. Ohne aktive Lipase ist die "
                "Fettverdauung stark beeinträchtigt, was zu Malabsorption und Steatorrhoe führt.</p>"
                "<p>Bei gesunden Menschen zirkuliert nur wenig Lipase im Blut. Bei Pankreasschädigung "
                "oder Gangobstruktion gelangt Lipase in den Blutkreislauf und der Serumspiegel steigt. "
                "Daher ist der Lipasetest eines der wertvollsten diagnostischen Werkzeuge für "
                "Pankreaserkrankungen.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Lipasewerte (Referenzbereiche)",
            body_html=(
                "<p>Lipase wird durch eine einfache Blutentnahme bestimmt:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Status</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Lipase (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Pankreatitis-Schwelle (3× Obergrenze)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p>Der <strong>normale Bereich liegt bei 0&ndash;60&nbsp;U/L</strong>. Für die Diagnose "
                "einer akuten Pankreatitis gilt ein Lipasewert von mindestens dem Dreifachen der oberen "
                "Normgrenze als klinisches Kriterium. Lipase wird durch Nahrungsaufnahme kaum "
                "beeinflusst. Vergleichen Sie Ihr Ergebnis mit dem Referenzbereich Ihres Labors.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen erhöhter Lipase",
            body_html=(
                "<p>Eine erhöhte Serumlipase kann verschiedene Ursachen haben:</p>"
                "<ul>"
                "<li><strong>Akute Pankreatitis:</strong> Die wichtigste Ursache. Lipase steigt meist "
                "auf über das Dreifache. Hauptauslöser sind Gallensteine und Alkohol.</li>"
                "<li><strong>Chronische Pankreatitis:</strong> Leichte bis mäßige Erhöhungen bei "
                "fortschreitendem Pankreasschaden.</li>"
                "<li><strong>Gallensteine:</strong> Können den Pankreasgang obstruieren.</li>"
                "<li><strong>Pankreaskarzinom:</strong> Gangobstruktion oder Gewebeschädigung.</li>"
                "<li><strong>Nierenerkrankung:</strong> Verminderte renale Clearance.</li>"
                "<li><strong>Darmobstruktion:</strong> Ileus oder mechanische Obstruktion.</li>"
                "<li><strong>Medikamente:</strong> Opioide, Thiazid-Diuretika, Valproinsäure u.&nbsp;a.</li>"
                "</ul>"
                "<p>Lipase ist für Pankreaserkrankungen spezifischer als Amylase. Mehr über "
                "Leberenzyme erfahren Sie in unserem "
                "<a href=\"/de/blog/alt-ast-liver-enzymes-meaning\">ALT-&amp;-AST-Ratgeber</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome einer Pankreatitis",
            body_html=(
                "<p>Die typischen Symptome der akuten Pankreatitis sind:</p>"
                "<ul>"
                "<li><strong>Starke Oberbauchschmerzen:</strong> Beginnen plötzlich und strahlen in "
                "den Rücken aus. Verschlechtern sich nach dem Essen, bessern sich beim "
                "Vorbeugen.</li>"
                "<li><strong>Übelkeit und Erbrechen:</strong> Häufig begleitend, können zur "
                "Dehydratation führen.</li>"
                "<li><strong>Fieber:</strong> Durch Entzündung oder Sekundärinfektion.</li>"
                "<li><strong>Druckschmerzhaftigkeit und Blähung:</strong> Der Bauch ist druckempfindlich "
                "und aufgebläht.</li>"
                "<li><strong>Schneller Puls:</strong> Tachykardie durch Schmerz und Flüssigkeitsverlust.</li>"
                "</ul>"
                "<p>Bei chronischer Pankreatitis stehen wiederkehrende Schmerzen, Gewichtsverlust, "
                "Steatorrhoe und Diabetes im Vordergrund. Akute Pankreatitis ist ein Notfall — suchen "
                "Sie sofort ärztliche Hilfe.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Verwandte Untersuchungen",
            body_html=(
                "<p>Bei erhöhter Lipase werden ergänzende Tests angeordnet:</p>"
                "<ul>"
                "<li><strong>Amylase:</strong> Wird oft zusammen mit Lipase bestimmt.</li>"
                "<li><strong>ALT und AST:</strong> Erhöhte Leberwerte deuten auf biliäre Ursache. "
                "Siehe unseren <a href=\"/de/blog/alt-ast-liver-enzymes-meaning\">ALT-&amp;-AST-"
                "Ratgeber</a>.</li>"
                "<li><strong>GGT und Bilirubin:</strong> Bewertung einer Gallengangsverlegung.</li>"
                "<li><strong>Abdomensonographie:</strong> Erste Bildgebung zur Detektion von "
                "Gallensteinen.</li>"
                "<li><strong>Abdomen-CT:</strong> Goldstandard zur Schweregradbeurteilung.</li>"
                "<li><strong>Triglyzeride:</strong> Sehr hohe Werte (&gt;1.000&nbsp;mg/dL) können "
                "Pankreatitis auslösen.</li>"
                "</ul>"
                "<p>Die Zusammenschau dieser Befunde ist für Diagnose und Therapieplanung "
                "entscheidend.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Suchen Sie dringend ärztliche Hilfe, wenn:</p>"
                "<ul>"
                "<li>Sie starke, anhaltende Oberbauchschmerzen haben</li>"
                "<li>Unkontrollierbares Erbrechen auftritt</li>"
                "<li>Hohes Fieber und allgemeines Krankheitsgefühl hinzukommen</li>"
                "<li>Ihre Lipase das Dreifache des Grenzwerts übersteigt</li>"
                "<li>Sie bekannte Gallensteine haben und Symptome auftreten</li>"
                "</ul>"
                "<p>Akute Pankreatitis ist ein lebensbedrohlicher Notfall, der stationär behandelt "
                "werden muss. Frühzeitige Behandlung senkt das Komplikationsrisiko deutlich.</p>"
                "<p>Eine leichte Lipaseerhöhung ist nicht immer ein Notfall, sollte aber mit Ihrem "
                "Arzt besprochen werden.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie NoryaAI Ihnen bei Lipase-Ergebnissen hilft",
            body_html=(
                "<p><strong>NoryaAI</strong> analysiert Ihren vollständigen Blutbefund einschließlich "
                "Lipase unter Berücksichtigung von Alter, Geschlecht und klinischem Kontext. Unser "
                "KI-System hebt auffällige Werte hervor und schlägt Fragen für Ihren Arzt vor.</p>"
                "<p><a href=\"/analyze\">Laden Sie Ihren Laborbericht hoch</a> für eine sofortige "
                "Analyse. Besuchen Sie unsere <a href=\"/pricing\">Preisseite</a> für die Planoptionen. "
                "NoryaAI ersetzt keinen Arzt — wir helfen Ihnen, informiert in Ihre nächste "
                "Konsultation zu gehen.</p>"
                "<p>Wenn Ihre Lipase erhöht ist und Sie Bauchschmerzen haben, suchen Sie umgehend "
                "ärztliche Bewertung.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Haftungsausschluss",
            body_html=(
                "<p><strong>Dieser Inhalt dient ausschließlich Informationszwecken und stellt keine "
                "medizinische Beratung, Diagnose oder Behandlung dar.</strong> Besprechen Sie Ihre "
                "Ergebnisse stets mit einer qualifizierten Fachkraft. NoryaAI ersetzt keine ärztliche "
                'Konsultation. <a href="/analyze">Besuchen Sie unsere Analyseseite</a> für erste '
                "Einblicke.</p>"
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
            heading="Analyse de la lipase : que signifient vos résultats ?",
            body_html=(
                "<p>Si votre bilan sanguin révèle un taux élevé de <strong>lipase</strong>, vous vous "
                "demandez probablement quel est le rôle de cette enzyme et s&rsquo;il y a lieu de "
                "s&rsquo;inquiéter. La lipase est une enzyme digestive produite principalement par le "
                "pancréas, et une <strong>lipase élevée</strong> constitue l&rsquo;un des indices les "
                "plus importants d&rsquo;une maladie pancréatique, en particulier la pancréatite aiguë.</p>"
                "<p>Ce guide explique ce que mesure le <strong>dosage de la lipase</strong>, les valeurs "
                "de référence normales, les causes d&rsquo;élévation, les symptômes de pancréatite et "
                "quand consulter. Notre objectif est de vous aider à comprendre vos résultats pour un "
                "dialogue plus fructueux avec votre médecin.</p>"
                "<p>La lipase est plus spécifique de l&rsquo;atteinte pancréatique que l&rsquo;amylase. "
                "Un taux supérieur à trois fois la limite supérieure de la normale est cliniquement très "
                "significatif et nécessite une évaluation urgente.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu&rsquo;est-ce que la lipase ?",
            body_html=(
                "<p>La <strong>lipase</strong> est une enzyme hydrolase qui décompose les triglycérides "
                "(graisses) en acides gras et glycérol. Elle est produite principalement par le pancréas, "
                "mais aussi en petites quantités par l&rsquo;estomac, la langue, le foie et la muqueuse "
                "intestinale. La lipase pancréatique est l&rsquo;enzyme la plus importante pour la "
                "digestion des graisses alimentaires.</p>"
                "<p>Le pancréas libère la lipase sous forme de précurseur inactif (<em>prolipase</em>), "
                "activé dans le duodénum par la colipase et les sels biliaires. Sans lipase active, la "
                "digestion des graisses est sévèrement altérée, entraînant malabsorption et stéatorrhée.</p>"
                "<p>Chez les personnes en bonne santé, seules de petites quantités de lipase circulent "
                "dans le sang. Lorsque le pancréas est endommagé ou son canal obstrué, la lipase fuit "
                "dans la circulation et le taux sérique augmente.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de lipase (intervalles de référence)",
            body_html=(
                "<p>La lipase est mesurée par une simple prise de sang :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">État</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Lipase (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Seuil de pancréatite (3× limite sup.)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p>Le <strong>taux normal se situe entre 0 et 60&nbsp;U/L</strong>. Pour la pancréatite "
                "aiguë, un taux au moins <em>trois fois</em> supérieur à la limite normale est retenu "
                "comme critère. Le jeûne n&rsquo;est généralement pas requis. Comparez toujours avec "
                "l&rsquo;intervalle de votre laboratoire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d&rsquo;une lipase élevée",
            body_html=(
                "<p>Une lipase sérique élevée peut résulter de plusieurs affections :</p>"
                "<ul>"
                "<li><strong>Pancréatite aiguë :</strong> Cause la plus importante. La lipase dépasse "
                "généralement 3 fois la limite supérieure. Calculs biliaires et alcool sont les "
                "déclencheurs principaux.</li>"
                "<li><strong>Pancréatite chronique :</strong> Dommage pancréatique progressif avec "
                "élévations modérées.</li>"
                "<li><strong>Calculs biliaires :</strong> Peuvent obstruer le canal pancréatique.</li>"
                "<li><strong>Cancer du pancréas :</strong> Obstruction canalaire ou lésion "
                "tissulaire.</li>"
                "<li><strong>Maladie rénale :</strong> Diminution de la clairance rénale.</li>"
                "<li><strong>Occlusion intestinale :</strong> Iléus ou obstruction mécanique.</li>"
                "<li><strong>Médicaments :</strong> Opioïdes, diurétiques thiazidiques, acide "
                "valproïque, etc.</li>"
                "</ul>"
                "<p>La lipase est plus spécifique que l&rsquo;amylase pour le pancréas. Pour en savoir "
                "plus sur les enzymes hépatiques, consultez notre "
                "<a href=\"/fr/blog/alt-ast-liver-enzymes-meaning\">guide ALT &amp; AST</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes de la pancréatite",
            body_html=(
                "<p>Les symptômes typiques de la pancréatite aiguë sont :</p>"
                "<ul>"
                "<li><strong>Douleur épigastrique intense :</strong> Irradiant dans le dos, aggravée "
                "après les repas, soulagée en se penchant en avant.</li>"
                "<li><strong>Nausées et vomissements :</strong> Fréquents et pouvant entraîner une "
                "déshydratation.</li>"
                "<li><strong>Fièvre :</strong> Liée à l&rsquo;inflammation ou à une surinfection.</li>"
                "<li><strong>Défense abdominale et distension :</strong> Abdomen sensible et "
                "ballonné.</li>"
                "<li><strong>Tachycardie :</strong> Par douleur et déshydratation.</li>"
                "</ul>"
                "<p>Dans la pancréatite chronique, douleurs récurrentes, amaigrissement, stéatorrhée et "
                "diabète prédominent. La pancréatite aiguë est une urgence — consultez "
                "immédiatement.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens complémentaires",
            body_html=(
                "<p>En cas de lipase élevée, des examens supplémentaires sont prescrits :</p>"
                "<ul>"
                "<li><strong>Amylase :</strong> Souvent dosée en parallèle.</li>"
                "<li><strong>ALT et AST :</strong> Leur élévation évoque une cause biliaire. Voir "
                "notre <a href=\"/fr/blog/alt-ast-liver-enzymes-meaning\">guide ALT &amp; AST</a>.</li>"
                "<li><strong>GGT et bilirubine :</strong> Évaluation d&rsquo;une obstruction "
                "biliaire.</li>"
                "<li><strong>Échographie abdominale :</strong> Première imagerie pour les calculs.</li>"
                "<li><strong>Scanner abdominal :</strong> Référence pour évaluer la sévérité.</li>"
                "<li><strong>Triglycérides :</strong> Des taux très élevés (&gt;1&nbsp;000&nbsp;mg/dL) "
                "peuvent déclencher une pancréatite.</li>"
                "</ul>"
                "<p>L&rsquo;analyse conjointe de ces examens est indispensable pour un diagnostic "
                "et un traitement adaptés.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez en urgence si :</p>"
                "<ul>"
                "<li>Douleur épigastrique intense et persistante</li>"
                "<li>Nausées et vomissements incontrôlables</li>"
                "<li>Fièvre élevée et altération de l&rsquo;état général</li>"
                "<li>Lipase supérieure à 3 fois la limite normale</li>"
                "<li>Antécédents de calculs biliaires avec symptômes</li>"
                "</ul>"
                "<p>La pancréatite aiguë est une urgence vitale nécessitant une hospitalisation. "
                "Une prise en charge précoce réduit significativement le risque de complications.</p>"
                "<p>Une élévation modérée de la lipase n&rsquo;est pas toujours urgente mais doit "
                "être discutée avec votre médecin.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment NoryaAI vous aide avec vos résultats de lipase",
            body_html=(
                "<p><strong>NoryaAI</strong> analyse l&rsquo;ensemble de votre bilan sanguin, y compris "
                "la lipase, en tenant compte de votre contexte clinique. Notre IA met en évidence les "
                "valeurs hors normes et suggère des questions pour votre médecin.</p>"
                "<p><a href=\"/analyze\">Téléchargez votre bilan</a> pour une analyse instantanée. "
                "Consultez notre <a href=\"/pricing\">page tarifs</a> pour nos formules. NoryaAI ne "
                "remplace pas le médecin ; nous vous aidons à mieux comprendre vos résultats.</p>"
                "<p>Si votre lipase est élevée et que vous avez des douleurs abdominales, consultez "
                "sans tarder.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                "<p><strong>Ce contenu est fourni à titre informatif uniquement et ne constitue pas un "
                "avis médical, un diagnostic ou un traitement.</strong> Discutez toujours de vos résultats "
                "avec un professionnel de santé. NoryaAI ne remplace pas une consultation médicale. "
                '<a href="/analyze">Visitez notre page d&rsquo;analyse</a> pour des informations '
                "préliminaires.</p>"
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
            heading="Esame della lipasi: cosa significano i risultati",
            body_html=(
                "<p>Se il vostro referto mostra un livello elevato di <strong>lipasi</strong>, è naturale "
                "chiedersi cosa faccia questo enzima e se ci sia motivo di preoccupazione. La lipasi è un "
                "enzima digestivo prodotto principalmente dal pancreas e un valore di <strong>lipasi "
                "alta</strong> è uno degli indizi più importanti di malattia pancreatica, in particolare "
                "la pancreatite acuta.</p>"
                "<p>Questa guida spiega cosa misura l&rsquo;esame della lipasi, gli intervalli di "
                "riferimento normali, le cause dell&rsquo;elevazione, i sintomi della pancreatite e "
                "quando consultare il medico. Il nostro obiettivo è aiutarvi a comprendere i risultati "
                "per un colloquio più produttivo con il vostro medico.</p>"
                "<p>La lipasi è più specifica per le malattie pancreatiche dell&rsquo;amilasi. Un "
                "valore superiore a tre volte il limite superiore della norma è clinicamente molto "
                "significativo e richiede una valutazione urgente.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Che cos&rsquo;è la lipasi?",
            body_html=(
                "<p>La <strong>lipasi</strong> è un enzima idrolasi che scinde i trigliceridi (grassi) "
                "in acidi grassi e glicerolo. È prodotta principalmente dal pancreas, con piccole "
                "quantità secrete anche da stomaco, lingua, fegato e mucosa intestinale. La lipasi "
                "pancreatica è l&rsquo;enzima più importante per la digestione dei grassi alimentari.</p>"
                "<p>Il pancreas rilascia la lipasi come precursore inattivo (<em>prolipasi</em>), "
                "attivato nel duodeno da colipasi e sali biliari. Senza lipasi attiva, la digestione "
                "dei grassi è gravemente compromessa, causando malassorbimento e steatorrea.</p>"
                "<p>Negli individui sani circolano solo piccole quantità di lipasi nel sangue. Quando "
                "il pancreas è danneggiato o il suo dotto ostruito, la lipasi passa nel circolo "
                "ematico e i livelli sierici aumentano.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali della lipasi (intervalli di riferimento)",
            body_html=(
                "<p>La lipasi si misura con un semplice prelievo di sangue:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Stato</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Lipasi (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normale</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Soglia di pancreatite (3× limite sup.)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p>L&rsquo;intervallo <strong>normale è 0&ndash;60&nbsp;U/L</strong>. Per la diagnosi "
                "di pancreatite acuta si usa come criterio un valore almeno <em>tre volte</em> il "
                "limite superiore. Il digiuno non è strettamente necessario. Confrontate sempre con "
                "l&rsquo;intervallo del vostro laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di lipasi alta",
            body_html=(
                "<p>Una lipasi sierica elevata può essere causata da:</p>"
                "<ul>"
                "<li><strong>Pancreatite acuta:</strong> La causa più importante. Lipasi generalmente "
                "&gt;3× il limite. Calcoli biliari e alcol sono i trigger principali.</li>"
                "<li><strong>Pancreatite cronica:</strong> Danno pancreatico progressivo.</li>"
                "<li><strong>Calcoli biliari:</strong> Ostruzione del dotto pancreatico.</li>"
                "<li><strong>Tumore del pancreas:</strong> Ostruzione duttale o danno tessutale.</li>"
                "<li><strong>Malattia renale:</strong> Ridotta clearance renale.</li>"
                "<li><strong>Occlusione intestinale:</strong> Ileo o ostruzione meccanica.</li>"
                "<li><strong>Farmaci:</strong> Oppioidi, tiazidici, acido valproico, ecc.</li>"
                "</ul>"
                "<p>La lipasi è più specifica dell&rsquo;amilasi per la patologia pancreatica. Per "
                "approfondire gli enzimi epatici, leggete la nostra "
                "<a href=\"/it/blog/alt-ast-liver-enzymes-meaning\">guida ALT &amp; AST</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi della pancreatite",
            body_html=(
                "<p>I sintomi tipici della pancreatite acuta sono:</p>"
                "<ul>"
                "<li><strong>Dolore epigastrico intenso:</strong> Irradiato al dorso, peggiora dopo "
                "i pasti, si allevia inclinandosi in avanti.</li>"
                "<li><strong>Nausea e vomito:</strong> Frequenti e potenzialmente causa di "
                "disidratazione.</li>"
                "<li><strong>Febbre:</strong> Da infiammazione o sovrainfezione.</li>"
                "<li><strong>Dolorabilità addominale e distensione:</strong> Addome dolente e "
                "gonfio.</li>"
                "<li><strong>Tachicardia:</strong> Da dolore e disidratazione.</li>"
                "</ul>"
                "<p>Nella pancreatite cronica prevalgono dolore ricorrente, dimagrimento, steatorrea "
                "e sviluppo di diabete. La pancreatite acuta è un&rsquo;emergenza — recatevi "
                "immediatamente al pronto soccorso.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p>In caso di lipasi elevata vengono prescritti esami aggiuntivi:</p>"
                "<ul>"
                "<li><strong>Amilasi:</strong> Spesso dosata insieme alla lipasi.</li>"
                "<li><strong>ALT e AST:</strong> Il loro aumento suggerisce causa biliare. Vedi la "
                "nostra <a href=\"/it/blog/alt-ast-liver-enzymes-meaning\">guida ALT &amp; AST</a>.</li>"
                "<li><strong>GGT e bilirubina:</strong> Per valutare l&rsquo;ostruzione biliare.</li>"
                "<li><strong>Ecografia addominale:</strong> Prima scelta per i calcoli.</li>"
                "<li><strong>TC addominale:</strong> Gold standard per la gravità.</li>"
                "<li><strong>Trigliceridi:</strong> Livelli molto alti (&gt;1.000&nbsp;mg/dL) possono "
                "causare pancreatite.</li>"
                "</ul>"
                "<p>La lettura congiunta di questi esami è essenziale per la diagnosi e il piano "
                "terapeutico.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Recatevi urgentemente al pronto soccorso se:</p>"
                "<ul>"
                "<li>Avete dolore addominale superiore intenso e persistente</li>"
                "<li>Nausea e vomito incontrollabili</li>"
                "<li>Febbre alta e malessere generale</li>"
                "<li>La lipasi supera 3 volte il limite superiore</li>"
                "<li>Avete storia di calcoli biliari con sintomi associati</li>"
                "</ul>"
                "<p>La pancreatite acuta è potenzialmente letale e richiede ricovero ospedaliero. "
                "Il trattamento precoce riduce significativamente il rischio di complicanze.</p>"
                "<p>Un&rsquo;elevazione lieve di lipasi non è sempre urgente, ma va comunque discussa "
                "con il medico.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come NoryaAI vi aiuta con i risultati della lipasi",
            body_html=(
                "<p><strong>NoryaAI</strong> analizza l&rsquo;intero referto, inclusa la lipasi, "
                "considerando età, sesso e contesto clinico. La nostra IA evidenzia i valori fuori "
                "norma e suggerisce domande per il medico.</p>"
                "<p><a href=\"/analyze\">Caricate il vostro referto</a> per un&rsquo;analisi istantanea. "
                "Visitate la <a href=\"/pricing\">pagina prezzi</a> per i piani disponibili. NoryaAI "
                "non sostituisce il medico; vi aiuta ad arrivare più informati alla visita.</p>"
                "<p>Se la lipasi è elevata e avete dolori addominali, cercate assistenza medica "
                "immediata.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza",
            body_html=(
                "<p><strong>Questo contenuto è fornito a solo scopo informativo e non costituisce "
                "consulenza medica, diagnosi o trattamento.</strong> Discutete sempre i risultati con "
                "un professionista sanitario. NoryaAI non sostituisce una visita medica. "
                '<a href="/analyze">Visitate la nostra pagina di analisi</a> per informazioni '
                "preliminari.</p>"
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
            heading="בדיקת ליפאז בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>אם תוצאות בדיקת הדם שלך מראות רמת <strong>ליפאז</strong> גבוהה, סביר שתרצו "
                "להבין מהו האנזים הזה ומה המשמעות הקלינית. ליפאז הוא אנזים עיכולי המיוצר בעיקר "
                "על ידי הלבלב, ורמת <strong>ליפאז גבוהה</strong> היא אחד הרמזים החשובים ביותר "
                "למחלת לבלב, בפרט דלקת לבלב חריפה (פנקראטיטיס).</p>"
                "<p>מדריך זה מסביר מה מודדת בדיקת הליפאז, טווחי ייחוס תקינים, גורמים לעלייה, "
                "תסמיני דלקת לבלב ומתי לפנות לרופא. המטרה שלנו אינה לאבחן — אלא לעזור לכם "
                "להבין את התוצאות לשיחה פרודוקטיבית יותר עם הרופא.</p>"
                "<p>ליפאז ספציפי יותר למחלות לבלב מאשר עמילאז. רמת ליפאז מעל פי שלושה מהגבול "
                "העליון של הנורמה משמעותית קלינית מאוד ומצריכה הערכה דחופה.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהו ליפאז?",
            body_html=(
                "<p><strong>ליפאז</strong> הוא אנזים הידרולאז המפרק טריגליצרידים (שומנים) לחומצות "
                "שומן וגליצרול. הוא מיוצר בעיקר בלבלב, אם כי כמויות קטנות מופרשות גם בקיבה, "
                "בלשון, בכבד ובריירית המעי. ליפאז לבלבי הוא האנזים החשוב ביותר לעיכול שומנים.</p>"
                "<p>הלבלב משחרר ליפאז בצורה לא פעילה (<em>פרוליפאז</em>) שמופעלת בתריסריון על ידי "
                "קוליפאז ומלחי מרה. ללא ליפאז פעיל, עיכול השומנים נפגע קשות, מה שמוביל לתת-ספיגה "
                "וסטאטוריאה (צואה שומנית).</p>"
                "<p>אצל אנשים בריאים, רק כמויות קטנות של ליפאז מסתובבות בדם. כאשר הלבלב נפגע או "
                "הצינור שלו חסום, ליפאז דולף לזרם הדם ורמת הסרום עולה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ייחוס תקינים של ליפאז",
            body_html=(
                "<p>ליפאז נמדד בבדיקת דם פשוטה:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">מצב</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">ליפאז (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>תקין</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">סף דלקת לבלב (3× גבול עליון)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p>הטווח <strong>התקין הוא בדרך כלל 0–60&nbsp;U/L</strong>. לאבחון דלקת לבלב חריפה, "
                "נדרש ליפאז לפחות <em>פי שלושה</em> מהגבול העליון. צום אינו הכרחי בדרך כלל. השוו "
                "תמיד עם טווח הייחוס של המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לליפאז גבוה",
            body_html=(
                "<p>ליפאז מוגבר בסרום יכול לנבוע ממספר מצבים:</p>"
                "<ul>"
                "<li><strong>דלקת לבלב חריפה:</strong> הגורם החשוב ביותר. הליפאז עולה בדרך כלל "
                "מעל פי 3. אבני מרה ואלכוהול הם הטריגרים המובילים.</li>"
                "<li><strong>דלקת לבלב כרונית:</strong> נזק לבלבי מתמשך עם עליות קלות עד בינוניות.</li>"
                "<li><strong>אבני מרה:</strong> חסימת צינור הלבלב.</li>"
                "<li><strong>סרטן הלבלב:</strong> חסימת צינור או נזק רקמתי.</li>"
                "<li><strong>מחלת כליות:</strong> ירידה בפינוי הכלייתי.</li>"
                "<li><strong>חסימת מעי:</strong> אילאוס או חסימה מכנית.</li>"
                "<li><strong>תרופות:</strong> אופיואידים, תיאזידים, חומצה ולפרואית ועוד.</li>"
                "</ul>"
                "<p>ליפאז ספציפי יותר לפתולוגיה לבלבית מאשר עמילאז. למידע נוסף על אנזימי כבד, "
                "קראו את <a href=\"/he/blog/alt-ast-liver-enzymes-meaning\">המדריך שלנו "
                "ל-ALT ו-AST</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמיני דלקת לבלב",
            body_html=(
                "<p>התסמינים האופייניים של דלקת לבלב חריפה:</p>"
                "<ul>"
                "<li><strong>כאב בטן עליון חמור:</strong> מתחיל באזור האפיגסטרי ומקרין לגב. "
                "מחמיר אחרי אכילה ועשוי להקל בכיפוף קדימה.</li>"
                "<li><strong>בחילות והקאות:</strong> מלוות לעיתים קרובות את הכאב ויכולות "
                "לגרום להתייבשות.</li>"
                "<li><strong>חום:</strong> מדלקת או זיהום משני.</li>"
                "<li><strong>רגישות בטנית ונפיחות:</strong> הבטן רגישה למגע ומנופחת.</li>"
                "<li><strong>דופק מהיר:</strong> טכיקרדיה מכאב והתייבשות.</li>"
                "</ul>"
                "<p>בדלקת לבלב כרונית: כאבים חוזרים, ירידה במשקל, סטאטוריאה והתפתחות סוכרת. "
                "דלקת לבלב חריפה היא מצב חירום — פנו מיד לעזרה רפואית.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות קשורות",
            body_html=(
                "<p>כשמתגלה ליפאז גבוה, נדרשות בדיקות נוספות:</p>"
                "<ul>"
                "<li><strong>עמילאז:</strong> נבדק לעיתים יחד עם ליפאז.</li>"
                "<li><strong>ALT ו-AST:</strong> עלייה מרמזת על גורם מרתי. ראו את "
                "<a href=\"/he/blog/alt-ast-liver-enzymes-meaning\">המדריך שלנו "
                "ל-ALT ו-AST</a>.</li>"
                "<li><strong>GGT ובילירובין:</strong> להערכת חסימת דרכי מרה.</li>"
                "<li><strong>אולטרסאונד בטני:</strong> בדיקת ההדמיה הראשונית לגילוי אבני מרה.</li>"
                "<li><strong>CT בטני:</strong> הסטנדרט לדירוג חומרת דלקת לבלב.</li>"
                "<li><strong>טריגליצרידים:</strong> רמות גבוהות מאוד (&gt;1,000&nbsp;mg/dL) "
                "עלולות לגרום לדלקת לבלב.</li>"
                "</ul>"
                "<p>פרשנות משולבת של בדיקות אלה חיונית לאבחון ולתכנון טיפול.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>פנו לחדר מיון או לרופא בדחיפות אם:</p>"
                "<ul>"
                "<li>יש לכם כאב בטן עליון חמור ומתמשך</li>"
                "<li>בחילות והקאות בלתי נשלטות</li>"
                "<li>חום גבוה ותחושת חולי כללית</li>"
                "<li>הליפאז מעל פי 3 מהגבול העליון</li>"
                "<li>יש לכם היסטוריה של אבני מרה עם תסמינים נלווים</li>"
                "</ul>"
                "<p>דלקת לבלב חריפה היא מצב מסכן חיים הדורש אשפוז. טיפול מוקדם מפחית "
                "משמעותית את הסיכון לסיבוכים.</p>"
                "<p>עלייה קלה בליפאז אינה תמיד חירום, אך צריכה להידון עם הרופא.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד NoryaAI עוזר לכם עם תוצאות הליפאז",
            body_html=(
                "<p><strong>NoryaAI</strong> מנתח את כל דוח בדיקת הדם שלכם, כולל ליפאז, בהתחשב "
                "בגיל, מין והקשר קליני. מערכת הבינה המלאכותית שלנו מדגישה ערכים חריגים ומציעה "
                "שאלות לרופא.</p>"
                "<p><a href=\"/analyze\">העלו את דוח המעבדה שלכם</a> לניתוח מיידי. בקרו "
                "ב<a href=\"/pricing\">עמוד התמחור</a> שלנו. NoryaAI אינו מחליף רופא; אנו עוזרים "
                "לכם להגיע מיודעים יותר לביקור הבא.</p>"
                "<p>אם הליפאז שלכם גבוה ויש לכם כאבי בטן, פנו לטיפול רפואי מיידי.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הבהרה משפטית",
            body_html=(
                "<p><strong>תוכן זה מוגש למטרות מידע בלבד ואינו מהווה ייעוץ רפואי, אבחנה או "
                "טיפול.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי מוסמך. NoryaAI אינו "
                'תחליף לייעוץ רפואי. <a href="/analyze">בקרו בעמוד הניתוח שלנו</a> לתובנות '
                "ראשוניות.</p>"
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
            heading="लाइपेज ब्लड टेस्ट: आपके रिज़ल्ट्स का क्या मतलब है?",
            body_html=(
                "<p>अगर आपकी लैब रिपोर्ट में <strong>लाइपेज</strong> का स्तर बढ़ा हुआ दिखाई दे रहा "
                "है, तो आप सोच रहे होंगे कि यह एंज़ाइम क्या करता है और क्या आपको चिंतित होना चाहिए। "
                "लाइपेज एक पाचन एंज़ाइम है जो मुख्य रूप से अग्न्याशय (पैंक्रियास) द्वारा बनाया जाता "
                "है, और <strong>हाई लाइपेज</strong> अग्न्याशय रोग, विशेष रूप से तीव्र अग्नाशयशोथ "
                "(एक्यूट पैंक्रिएटाइटिस) का सबसे महत्वपूर्ण संकेत है।</p>"
                "<p>यह गाइड बताती है कि <strong>लाइपेज ब्लड टेस्ट</strong> क्या मापता है, सामान्य "
                "रेफरेंस रेंज, बढ़े हुए लाइपेज के कारण, पैंक्रिएटाइटिस के लक्षण और कब डॉक्टर से "
                "मिलना चाहिए।</p>"
                "<p>लाइपेज, अग्न्याशय रोग के लिए एमाइलेज़ से अधिक विशिष्ट है। ऊपरी सीमा से तीन "
                "गुना से अधिक का लाइपेज स्तर चिकित्सकीय रूप से बहुत महत्वपूर्ण है और तत्काल "
                "मूल्यांकन की आवश्यकता होती है।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="लाइपेज क्या है?",
            body_html=(
                "<p><strong>लाइपेज</strong> एक हाइड्रोलेज़ एंज़ाइम है जो ट्राइग्लिसराइड्स (वसा) को "
                "फैटी एसिड और ग्लिसरॉल में तोड़ता है। यह मुख्य रूप से अग्न्याशय द्वारा बनाया जाता "
                "है, हालांकि पेट, जीभ, यकृत और आंत्र म्यूकोसा भी छोटी मात्रा में इसे स्रावित करते हैं। "
                "पैंक्रियाटिक लाइपेज आहार वसा के पाचन के लिए सबसे महत्वपूर्ण एंज़ाइम है।</p>"
                "<p>अग्न्याशय लाइपेज को एक निष्क्रिय अग्रदूत रूप (<em>प्रोलाइपेज़</em>) में छोड़ता "
                "है, जो ड्यूओडेनम में कोलाइपेज़ और पित्त लवण द्वारा सक्रिय होता है। सक्रिय लाइपेज "
                "के बिना, वसा पाचन गंभीर रूप से बाधित होता है।</p>"
                "<p>स्वस्थ व्यक्तियों में, रक्त में केवल थोड़ी मात्रा में लाइपेज होता है। जब "
                "अग्न्याशय क्षतिग्रस्त होता है या उसकी नली अवरुद्ध होती है, तो लाइपेज रक्तप्रवाह "
                "में रिसता है और सीरम स्तर बढ़ जाता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="लाइपेज के सामान्य मान (रेफरेंस रेंज)",
            body_html=(
                "<p>लाइपेज एक साधारण ब्लड टेस्ट से मापा जाता है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">स्थिति</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">लाइपेज (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>सामान्य</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">पैंक्रिएटाइटिस सीमा (3× ऊपरी सीमा)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p><strong>सामान्य रेंज 0–60&nbsp;U/L</strong> है। एक्यूट पैंक्रिएटाइटिस के निदान "
                "के लिए ऊपरी सीमा से कम से कम <em>तीन गुना</em> लाइपेज की आवश्यकता होती है। "
                "उपवास आवश्यक नहीं है। अपनी लैब की रेफरेंस रेंज से तुलना करें।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई लाइपेज के कारण",
            body_html=(
                "<p>बढ़ा हुआ सीरम लाइपेज कई स्थितियों से हो सकता है:</p>"
                "<ul>"
                "<li><strong>एक्यूट पैंक्रिएटाइटिस:</strong> सबसे महत्वपूर्ण कारण। लाइपेज "
                "आमतौर पर 3 गुना से अधिक बढ़ता है। पित्त पथरी और शराब प्रमुख ट्रिगर हैं।</li>"
                "<li><strong>क्रोनिक पैंक्रिएटाइटिस:</strong> निरंतर अग्न्याशय क्षति।</li>"
                "<li><strong>पित्त पथरी:</strong> अग्न्याशय नली को अवरुद्ध कर सकती है।</li>"
                "<li><strong>अग्न्याशय कैंसर:</strong> नली अवरोध या ऊतक क्षति।</li>"
                "<li><strong>किडनी की बीमारी:</strong> कम रीनल क्लीयरेंस।</li>"
                "<li><strong>आंत्र रुकावट:</strong> इलियस या यांत्रिक अवरोध।</li>"
                "<li><strong>दवाएं:</strong> ओपिओइड, थायज़ाइड डाइयुरेटिक्स, वैल्प्रोइक एसिड आदि।</li>"
                "</ul>"
                "<p>लाइपेज, एमाइलेज़ से अग्न्याशय रोग के लिए अधिक विशिष्ट है। लिवर एंज़ाइम्स के "
                "बारे में अधिक जानकारी के लिए हमारी "
                "<a href=\"/hi/blog/alt-ast-liver-enzymes-meaning\">ALT और AST गाइड</a> पढ़ें।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="पैंक्रिएटाइटिस के लक्षण",
            body_html=(
                "<p>एक्यूट पैंक्रिएटाइटिस के विशिष्ट लक्षण:</p>"
                "<ul>"
                "<li><strong>गंभीर ऊपरी पेट दर्द:</strong> अचानक शुरू होता है और पीठ की ओर "
                "फैलता है। खाने के बाद बिगड़ता है।</li>"
                "<li><strong>मतली और उल्टी:</strong> दर्द के साथ बार-बार होती है।</li>"
                "<li><strong>बुखार:</strong> सूजन या संक्रमण के कारण।</li>"
                "<li><strong>पेट में सूजन और कोमलता:</strong> पेट छूने पर दर्दनाक और फूला "
                "हुआ।</li>"
                "<li><strong>तेज़ नब्ज़:</strong> दर्द और डिहाइड्रेशन से।</li>"
                "</ul>"
                "<p>क्रोनिक पैंक्रिएटाइटिस में बार-बार पेट दर्द, वज़न कम होना, चिकनी दस्त और "
                "डायबिटीज विकसित होती है। एक्यूट पैंक्रिएटाइटिस एक मेडिकल इमरजेंसी है — "
                "तुरंत चिकित्सा सहायता लें।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित जांचें",
            body_html=(
                "<p>लाइपेज बढ़ने पर अतिरिक्त जांचें की जाती हैं:</p>"
                "<ul>"
                "<li><strong>एमाइलेज़:</strong> अक्सर लाइपेज के साथ मांगा जाता है।</li>"
                "<li><strong>ALT और AST:</strong> बढ़ा हुआ स्तर बिलियरी कारण का संकेत देता है। "
                "हमारी <a href=\"/hi/blog/alt-ast-liver-enzymes-meaning\">ALT और AST गाइड</a> "
                "देखें।</li>"
                "<li><strong>GGT और बिलीरुबिन:</strong> पित्त नली अवरोध के मूल्यांकन के लिए।</li>"
                "<li><strong>पेट का अल्ट्रासाउंड:</strong> पित्त पथरी का पता लगाने के लिए।</li>"
                "<li><strong>पेट का सीटी स्कैन:</strong> गंभीरता के आकलन का गोल्ड स्टैंडर्ड।</li>"
                "<li><strong>ट्राइग्लिसराइड्स:</strong> बहुत उच्च स्तर (&gt;1,000&nbsp;mg/dL) "
                "पैंक्रिएटाइटिस का कारण बन सकते हैं।</li>"
                "</ul>"
                "<p>इन जांचों की संयुक्त व्याख्या निदान और उपचार के लिए आवश्यक है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>तत्काल चिकित्सा सहायता लें अगर:</p>"
                "<ul>"
                "<li>गंभीर, लगातार ऊपरी पेट दर्द हो</li>"
                "<li>अनियंत्रित मतली और उल्टी हो</li>"
                "<li>तेज़ बुखार और सामान्य अस्वस्थता हो</li>"
                "<li>लाइपेज ऊपरी सीमा से 3 गुना से अधिक हो</li>"
                "<li>पित्त पथरी का इतिहास हो और लक्षण दिखें</li>"
                "</ul>"
                "<p>एक्यूट पैंक्रिएटाइटिस जानलेवा हो सकता है और अस्पताल में इलाज ज़रूरी है। "
                "जल्दी उपचार जटिलताओं का जोखिम काफी कम कर देता है।</p>"
                "<p>हल्की लाइपेज वृद्धि हमेशा आपातकालीन नहीं होती, लेकिन डॉक्टर से चर्चा "
                "ज़रूर करें।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI आपके लाइपेज रिज़ल्ट्स में कैसे मदद करता है",
            body_html=(
                "<p><strong>NoryaAI</strong> आपकी पूरी ब्लड टेस्ट रिपोर्ट का विश्लेषण करता है — "
                "लाइपेज सहित — आपकी उम्र, लिंग और क्लीनिकल बैकग्राउंड को ध्यान में रखते हुए।</p>"
                "<p><a href=\"/analyze\">अपनी लैब रिपोर्ट अपलोड करें</a> तत्काल विश्लेषण के लिए। "
                "<a href=\"/pricing\">प्राइसिंग पेज</a> पर प्लान देखें। NoryaAI डॉक्टर का विकल्प "
                "नहीं है; हम आपको जानकारी से सशक्त बनाते हैं।</p>"
                "<p>अगर लाइपेज बढ़ा हुआ है और पेट दर्द है, तो तुरंत चिकित्सा मूल्यांकन "
                "करवाएं।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                "<p><strong>यह सामग्री केवल सूचनात्मक उद्देश्यों के लिए है और चिकित्सा सलाह, "
                "निदान या उपचार का गठन नहीं करती।</strong> अपने रिज़ल्ट्स हमेशा योग्य स्वास्थ्य "
                "पेशेवर के साथ चर्चा करें। NoryaAI चिकित्सा परामर्श का विकल्प नहीं है। "
                '<a href="/analyze">हमारे विश्लेषण पेज पर जाएं</a> प्रारंभिक जानकारी के लिए।</p>'
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
            heading="تحليل الليباز في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>إذا أظهرت نتائج تحليل الدم لديك مستوى مرتفعاً من <strong>الليباز</strong>، "
                "فقد تتساءل عن وظيفة هذا الإنزيم وعما إذا كان هناك داعٍ للقلق. الليباز إنزيم "
                "هضمي يُنتج بشكل رئيسي من البنكرياس، و<strong>ارتفاع الليباز</strong> من أهم "
                "المؤشرات على أمراض البنكرياس، خاصة التهاب البنكرياس الحاد.</p>"
                "<p>يشرح هذا الدليل ما يقيسه تحليل الليباز، النطاقات المرجعية، أسباب الارتفاع، "
                "أعراض التهاب البنكرياس ومتى يجب مراجعة الطبيب. هدفنا مساعدتك على فهم نتائجك "
                "لحوار أكثر فاعلية مع طبيبك.</p>"
                "<p>الليباز أكثر نوعية لأمراض البنكرياس من الأميلاز. مستوى ليباز يتجاوز ثلاثة "
                "أضعاف الحد الأعلى للطبيعي ذو دلالة سريرية كبيرة ويستدعي تقييماً عاجلاً.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو الليباز؟",
            body_html=(
                "<p><strong>الليباز</strong> إنزيم هيدرولاز يُفكك الدهون الثلاثية (الشحوم) إلى "
                "أحماض دهنية وغليسرول. يُنتج بشكل رئيسي من البنكرياس، وتُفرز كميات صغيرة "
                "أيضاً من المعدة واللسان والكبد والغشاء المخاطي المعوي. الليباز البنكرياسي هو "
                "الإنزيم الأهم لهضم الدهون الغذائية.</p>"
                "<p>يُفرز البنكرياس الليباز بصورة غير فعالة (<em>البروليباز</em>) تُنشَّط في "
                "الاثني عشر بواسطة الكوليباز والأملاح الصفراوية. بدون ليباز فعّال، يتعطل هضم "
                "الدهون بشكل خطير مما يؤدي إلى سوء الامتصاص وبراز دهني.</p>"
                "<p>لدى الأصحاء، تسري كميات ضئيلة فقط من الليباز في الدم. عند تلف البنكرياس "
                "أو انسداد قناته، يتسرب الليباز إلى مجرى الدم ويرتفع مستوى المصل.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المستويات الطبيعية للليباز (النطاقات المرجعية)",
            body_html=(
                "<p>يُقاس الليباز بسحب دم بسيط:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الحالة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">ليباز (U/L)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>طبيعي</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0 – 60</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">عتبة التهاب البنكرياس (3× الحد الأعلى)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt; 180</td>'
                "</tr></tbody></table>"
                "<p>النطاق <strong>الطبيعي 0–60&nbsp;U/L</strong>. لتشخيص التهاب البنكرياس الحاد "
                "يُستخدم معيار تجاوز <em>ثلاثة أضعاف</em> الحد الأعلى. الصيام ليس ضرورياً عادة. "
                "قارن نتيجتك بنطاق مختبرك.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع الليباز",
            body_html=(
                "<p>يمكن أن ينتج ارتفاع الليباز عن عدة حالات:</p>"
                "<ul>"
                "<li><strong>التهاب البنكرياس الحاد:</strong> السبب الأهم. يرتفع الليباز عادة "
                "فوق 3 أضعاف. حصوات المرارة والكحول أبرز المحفّزات.</li>"
                "<li><strong>التهاب البنكرياس المزمن:</strong> تلف بنكرياسي تدريجي.</li>"
                "<li><strong>حصوات المرارة:</strong> قد تسدّ قناة البنكرياس.</li>"
                "<li><strong>سرطان البنكرياس:</strong> انسداد القناة أو تلف الأنسجة.</li>"
                "<li><strong>مرض كلوي:</strong> انخفاض التصفية الكلوية.</li>"
                "<li><strong>انسداد معوي:</strong> عِلّوص أو انسداد ميكانيكي.</li>"
                "<li><strong>أدوية:</strong> مسكنات أفيونية، مُدرّات ثيازيدية، حمض الفالبرويك "
                "وغيرها.</li>"
                "</ul>"
                "<p>الليباز أكثر نوعية من الأميلاز للبنكرياس. لمزيد من المعلومات عن إنزيمات "
                "الكبد، اقرأ <a href=\"/ar/blog/alt-ast-liver-enzymes-meaning\">دليلنا عن "
                "ALT وAST</a>.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض التهاب البنكرياس",
            body_html=(
                "<p>أعراض التهاب البنكرياس الحاد النموذجية:</p>"
                "<ul>"
                "<li><strong>ألم شديد في أعلى البطن:</strong> يبدأ فجأة ويمتد إلى الظهر. يسوء "
                "بعد الأكل وقد يخف بالانحناء للأمام.</li>"
                "<li><strong>غثيان وقيء:</strong> يصاحب الألم بشكل متكرر.</li>"
                "<li><strong>حمّى:</strong> من الالتهاب أو العدوى الثانوية.</li>"
                "<li><strong>إيلام بطني وانتفاخ:</strong> البطن مؤلم عند اللمس ومنتفخ.</li>"
                "<li><strong>تسارع النبض:</strong> من الألم والجفاف.</li>"
                "</ul>"
                "<p>في التهاب البنكرياس المزمن: ألم متكرر، فقدان وزن، براز دهني وتطور السكري. "
                "التهاب البنكرياس الحاد حالة طوارئ — اطلب المساعدة فوراً.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="الفحوصات ذات الصلة",
            body_html=(
                "<p>عند ارتفاع الليباز تُطلب فحوصات إضافية:</p>"
                "<ul>"
                "<li><strong>الأميلاز:</strong> يُطلب غالباً مع الليباز.</li>"
                "<li><strong>ALT وAST:</strong> ارتفاعهما يشير لسبب صفراوي. اقرأ "
                "<a href=\"/ar/blog/alt-ast-liver-enzymes-meaning\">دليلنا عن "
                "ALT وAST</a>.</li>"
                "<li><strong>GGT والبيليروبين:</strong> لتقييم انسداد القنوات الصفراوية.</li>"
                "<li><strong>الموجات فوق الصوتية البطنية:</strong> الفحص الأول لكشف الحصوات.</li>"
                "<li><strong>الأشعة المقطعية البطنية:</strong> المعيار لتقييم شدة الالتهاب.</li>"
                "<li><strong>الدهون الثلاثية:</strong> مستويات مرتفعة جداً "
                "(&gt;1,000&nbsp;mg/dL) قد تسبب التهاب البنكرياس.</li>"
                "</ul>"
                "<p>التحليل المشترك لهذه الفحوصات ضروري للتشخيص والعلاج.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>اطلب رعاية طبية عاجلة إذا:</p>"
                "<ul>"
                "<li>ألم شديد ومستمر في أعلى البطن</li>"
                "<li>غثيان وقيء لا يمكن السيطرة عليهما</li>"
                "<li>حمّى مرتفعة وشعور عام بالتوعك</li>"
                "<li>الليباز أكثر من 3 أضعاف الحد الأعلى</li>"
                "<li>لديك تاريخ بحصوات مرارية مع أعراض مرافقة</li>"
                "</ul>"
                "<p>التهاب البنكرياس الحاد حالة مهددة للحياة تتطلب علاجاً بالمستشفى. التدخل "
                "المبكر يقلل خطر المضاعفات بشكل كبير.</p>"
                "<p>ارتفاع طفيف في الليباز ليس دائماً طارئاً لكن يجب مناقشته مع طبيبك.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يساعدك NoryaAI في فهم نتائج الليباز",
            body_html=(
                "<p>يقوم <strong>NoryaAI</strong> بتحليل تقرير فحص الدم بالكامل، بما في ذلك "
                "الليباز، مع مراعاة سياقك السريري. يُبرز نظامنا القيم الخارجة ويقترح أسئلة "
                "لطبيبك.</p>"
                "<p><a href=\"/analyze\">ارفع تقرير المختبر</a> لتحليل فوري. زر "
                "<a href=\"/pricing\">صفحة الأسعار</a> لاستكشاف الخطط. NoryaAI لا يحل محل "
                "الطبيب؛ نساعدك على الوصول أكثر اطلاعاً.</p>"
                "<p>إذا كان الليباز مرتفعاً ولديك ألم بطني، اطلب تقييماً طبياً فورياً.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                "<p><strong>هذا المحتوى لأغراض إعلامية فقط ولا يُشكّل نصيحة طبية أو تشخيصاً "
                "أو علاجاً.</strong> ناقش نتائجك دائماً مع متخصص مؤهل. NoryaAI ليس بديلاً عن "
                'الاستشارة الطبية. <a href="/analyze">قم بزيارة صفحة التحليل</a> لرؤى أولية.</p>'
            ),
        ),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_lipase_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Lipase article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_lipase_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Lipase article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is lipase and what does it do?",
             "answer": "Lipase is a digestive enzyme produced mainly by the pancreas. It breaks down dietary fats (triglycerides) into fatty acids and glycerol so they can be absorbed by the body."},
            {"question": "What is a normal lipase level?",
             "answer": "The normal serum lipase range is generally 0–60 U/L, though exact cut-offs vary between laboratories. A level more than three times the upper limit of normal (>180 U/L) is a key criterion for diagnosing acute pancreatitis."},
            {"question": "What causes high lipase?",
             "answer": "The most important cause is acute pancreatitis, usually triggered by gallstones or alcohol. Other causes include chronic pancreatitis, pancreatic cancer, kidney disease, bowel obstruction, and certain medications. Lipase is more specific for pancreatic disease than amylase."},
            {"question": "Is high lipase always pancreatitis?",
             "answer": "No. While acute pancreatitis is the most common cause of significantly elevated lipase (>3× normal), milder elevations can result from kidney disease, bowel obstruction, medications, or other conditions. Clinical symptoms and additional tests are needed for diagnosis."},
        ],
        "tr": [
            {"question": "Lipaz nedir ve ne işe yarar?",
             "answer": "Lipaz, başta pankreas tarafından üretilen bir sindirim enzimidir. Besinlerdeki yağları (trigliseritleri) yağ asitleri ve gliserole parçalayarak vücudun emilimini sağlar."},
            {"question": "Normal lipaz değeri nedir?",
             "answer": "Normal serum lipaz aralığı genellikle 0–60 U/L'dir. Akut pankreatit tanısı için lipaz değerinin normalin üst sınırının en az 3 katı (>180 U/L) olması klinik kriter olarak kullanılır."},
            {"question": "Lipaz yüksekliğinin nedenleri nelerdir?",
             "answer": "En önemli neden akut pankreatittir; genellikle safra taşları veya alkol tetikler. Diğer nedenler arasında kronik pankreatit, pankreas kanseri, böbrek hastalığı, bağırsak tıkanıklığı ve bazı ilaçlar yer alır."},
            {"question": "Yüksek lipaz her zaman pankreatit mi demektir?",
             "answer": "Hayır. Normalin 3 katının üzerindeki değerler genellikle pankreatiti düşündürür; ancak hafif yükseklikler böbrek hastalığı, ilaçlar veya bağırsak sorunlarından da kaynaklanabilir. Tanı için klinik belirtiler ve ek testler gereklidir."},
        ],
        "es": [
            {"question": "¿Qué es la lipasa y para qué sirve?",
             "answer": "La lipasa es una enzima digestiva producida principalmente por el páncreas. Descompone las grasas de la dieta en ácidos grasos y glicerol para que el cuerpo pueda absorberlos."},
            {"question": "¿Cuál es un nivel normal de lipasa?",
             "answer": "El rango normal suele ser 0–60 U/L. Un nivel superior a 3 veces el límite superior (>180 U/L) es criterio clave para el diagnóstico de pancreatitis aguda."},
            {"question": "¿Qué causa la lipasa alta?",
             "answer": "La causa más importante es la pancreatitis aguda, generalmente por cálculos biliares o alcohol. Otras causas incluyen pancreatitis crónica, cáncer pancreático, enfermedad renal y ciertos fármacos."},
            {"question": "¿La lipasa alta siempre significa pancreatitis?",
             "answer": "No. Elevaciones leves pueden deberse a enfermedad renal, obstrucción intestinal o medicamentos. Se necesitan síntomas clínicos y pruebas adicionales para el diagnóstico."},
        ],
        "de": [
            {"question": "Was ist Lipase und was macht sie?",
             "answer": "Lipase ist ein Verdauungsenzym, das hauptsächlich von der Bauchspeicheldrüse produziert wird. Sie spaltet Nahrungsfette (Triglyzeride) in Fettsäuren und Glycerol."},
            {"question": "Was ist ein normaler Lipasewert?",
             "answer": "Der Normalbereich liegt bei 0–60 U/L. Ein Wert über dem Dreifachen des oberen Grenzwerts (>180 U/L) ist ein Schlüsselkriterium für die Diagnose einer akuten Pankreatitis."},
            {"question": "Was verursacht erhöhte Lipase?",
             "answer": "Die wichtigste Ursache ist akute Pankreatitis, meist durch Gallensteine oder Alkohol. Weitere Ursachen sind chronische Pankreatitis, Pankreaskarzinom, Nierenerkrankung und Medikamente."},
            {"question": "Bedeutet erhöhte Lipase immer Pankreatitis?",
             "answer": "Nein. Leichte Erhöhungen können durch Nierenerkrankung, Darmobstruktion oder Medikamente bedingt sein. Für die Diagnose sind klinische Symptome und Zusatzuntersuchungen nötig."},
        ],
        "fr": [
            {"question": "Qu'est-ce que la lipase et à quoi sert-elle ?",
             "answer": "La lipase est une enzyme digestive produite principalement par le pancréas. Elle décompose les graisses alimentaires (triglycérides) en acides gras et glycérol."},
            {"question": "Quel est un taux normal de lipase ?",
             "answer": "Le taux normal est généralement de 0 à 60 U/L. Un taux supérieur à 3 fois la limite supérieure (>180 U/L) est un critère clé pour le diagnostic de pancréatite aiguë."},
            {"question": "Quelles sont les causes d'une lipase élevée ?",
             "answer": "La cause la plus importante est la pancréatite aiguë, généralement due aux calculs biliaires ou à l'alcool. D'autres causes incluent pancréatite chronique, cancer du pancréas, maladie rénale et certains médicaments."},
            {"question": "Une lipase élevée signifie-t-elle toujours une pancréatite ?",
             "answer": "Non. Des élévations modérées peuvent résulter d'une maladie rénale, d'une occlusion intestinale ou de médicaments. Des symptômes cliniques et des examens complémentaires sont nécessaires pour le diagnostic."},
        ],
        "it": [
            {"question": "Che cos'è la lipasi e a cosa serve?",
             "answer": "La lipasi è un enzima digestivo prodotto principalmente dal pancreas. Scinde i grassi alimentari (trigliceridi) in acidi grassi e glicerolo per l'assorbimento."},
            {"question": "Qual è un valore normale di lipasi?",
             "answer": "L'intervallo normale è generalmente 0–60 U/L. Un valore superiore a 3 volte il limite (>180 U/L) è criterio chiave per la diagnosi di pancreatite acuta."},
            {"question": "Quali sono le cause di lipasi alta?",
             "answer": "La causa più importante è la pancreatite acuta, solitamente da calcoli biliari o alcol. Altre cause includono pancreatite cronica, tumore del pancreas, malattia renale e farmaci."},
            {"question": "La lipasi alta significa sempre pancreatite?",
             "answer": "No. Elevazioni lievi possono derivare da malattia renale, ostruzione intestinale o farmaci. Servono sintomi clinici e ulteriori esami per la diagnosi."},
        ],
        "he": [
            {"question": "מהו ליפאז ומה תפקידו?",
             "answer": "ליפאז הוא אנזים עיכולי המיוצר בעיקר בלבלב. הוא מפרק שומנים (טריגליצרידים) לחומצות שומן וגליצרול לספיגה בגוף."},
            {"question": "מהי רמת ליפאז תקינה?",
             "answer": "הטווח התקין הוא בדרך כלל 0–60 U/L. רמה מעל פי 3 מהגבול העליון (>180 U/L) היא קריטריון מפתח לאבחון דלקת לבלב חריפה."},
            {"question": "מה גורם לליפאז גבוה?",
             "answer": "הגורם החשוב ביותר הוא דלקת לבלב חריפה, בדרך כלל מאבני מרה או אלכוהול. גורמים נוספים: דלקת לבלב כרונית, סרטן הלבלב, מחלת כליות, חסימת מעי ותרופות."},
            {"question": "האם ליפאז גבוה תמיד מעיד על דלקת לבלב?",
             "answer": "לא. עליות קלות יכולות לנבוע ממחלת כליות, חסימת מעי או תרופות. נדרשים תסמינים קליניים ובדיקות נוספות לאבחון."},
        ],
        "hi": [
            {"question": "लाइपेज क्या है और यह क्या करता है?",
             "answer": "लाइपेज एक पाचन एंज़ाइम है जो मुख्य रूप से अग्न्याशय द्वारा बनाया जाता है। यह आहार वसा (ट्राइग्लिसराइड्स) को फैटी एसिड और ग्लिसरॉल में तोड़ता है।"},
            {"question": "सामान्य लाइपेज लेवल क्या है?",
             "answer": "सामान्य रेंज आमतौर पर 0–60 U/L है। ऊपरी सीमा से 3 गुना से अधिक (>180 U/L) एक्यूट पैंक्रिएटाइटिस के निदान का मुख्य मानदंड है।"},
            {"question": "हाई लाइपेज के कारण क्या हैं?",
             "answer": "सबसे महत्वपूर्ण कारण एक्यूट पैंक्रिएटाइटिस है, आमतौर पर पित्त पथरी या शराब से। अन्य कारणों में क्रोनिक पैंक्रिएटाइटिस, अग्न्याशय कैंसर, किडनी रोग और दवाएं शामिल हैं।"},
            {"question": "क्या हाई लाइपेज हमेशा पैंक्रिएटाइटिस है?",
             "answer": "नहीं। हल्की वृद्धि किडनी रोग, आंत्र रुकावट या दवाओं से हो सकती है। निदान के लिए क्लीनिकल लक्षण और अतिरिक्त जांचें आवश्यक हैं।"},
        ],
        "ar": [
            {"question": "ما هو الليباز وما وظيفته؟",
             "answer": "الليباز إنزيم هضمي يُنتج بشكل رئيسي من البنكرياس. يُفكك الدهون الغذائية (الشحوم الثلاثية) إلى أحماض دهنية وغليسرول ليمتصها الجسم."},
            {"question": "ما هو المستوى الطبيعي للليباز؟",
             "answer": "النطاق الطبيعي عادة 0–60 U/L. مستوى يتجاوز 3 أضعاف الحد الأعلى (>180 U/L) معيار رئيسي لتشخيص التهاب البنكرياس الحاد."},
            {"question": "ما أسباب ارتفاع الليباز؟",
             "answer": "أهم سبب هو التهاب البنكرياس الحاد، عادة بسبب حصوات المرارة أو الكحول. أسباب أخرى تشمل التهاب البنكرياس المزمن، سرطان البنكرياس، مرض كلوي وأدوية معينة."},
            {"question": "هل يعني ارتفاع الليباز دائماً التهاب البنكرياس؟",
             "answer": "لا. ارتفاعات طفيفة قد تنتج عن مرض كلوي أو انسداد معوي أو أدوية. يلزم تقييم الأعراض وإجراء فحوصات إضافية للتشخيص."},
        ],
    }
