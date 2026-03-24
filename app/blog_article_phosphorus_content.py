# -*- coding: utf-8 -*-
"""
Phosphorus blog article — full body content for all 9 languages.
Used by blog_i18n._article_phosphorus().
Sections: intro, what-is, normal-ranges, causes, symptoms,
related-tests, when-to-see-doctor, how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# ENGLISH
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Phosphorus blood test: what your result means",
            body_html=(
                "<p>Phosphorus (phosphate) is the second most abundant mineral in the human body after calcium. "
                "It is essential for bone formation, energy metabolism, and the structural integrity of cell membranes. "
                "When your blood test reports a phosphorus level, it measures the inorganic phosphate dissolved in your serum.</p>"
                "<p>Abnormal phosphorus levels&mdash;either high (<strong>hyperphosphatemia</strong>) or low (<strong>hypophosphatemia</strong>)&mdash;"
                "can indicate kidney disease, hormonal imbalances, nutritional deficiencies, or other medical conditions. "
                "Understanding what the number means helps you have a more informed conversation with your doctor.</p>"
                "<p>This article is for educational purposes only and does not replace medical advice. "
                "Always discuss your lab results with a qualified healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is phosphorus and why does it matter?",
            body_html=(
                "<p><strong>Phosphorus</strong> is a mineral that works closely with <a href=\"/en/blog/calcium-high-meaning\">calcium</a> "
                "to build and maintain strong bones and teeth. About 85% of the body&rsquo;s phosphorus is stored in bones, "
                "while the remaining 15% is distributed across soft tissues and body fluids.</p>"
                "<p>Beyond bone health, phosphorus plays vital roles in:</p>"
                "<ul>"
                "<li><strong>Energy production</strong> &ndash; phosphorus is a key component of adenosine triphosphate (ATP), the body&rsquo;s primary energy currency.</li>"
                "<li><strong>DNA and RNA structure</strong> &ndash; the backbone of nucleic acids is made of phosphate groups.</li>"
                "<li><strong>Cell membrane integrity</strong> &ndash; phospholipids form the bilayer of every cell membrane.</li>"
                "<li><strong>Acid-base balance</strong> &ndash; phosphate acts as a buffer to maintain blood pH.</li>"
                "</ul>"
                "<p>Phosphorus levels in the blood are tightly regulated by the kidneys, parathyroid hormone (PTH), and vitamin D. "
                "When this regulatory system is disrupted&mdash;most commonly by kidney disease&mdash;phosphorus levels can deviate "
                "from the normal range and cause significant health consequences.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal phosphorus ranges",
            body_html=(
                "<p>The phosphorus level on your blood test reflects serum inorganic phosphate. Reference ranges differ slightly "
                "between laboratories, but the following are widely accepted:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adults</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5&ndash;4.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.81&ndash;1.45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Children</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4.0&ndash;7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.29&ndash;2.26</td></tr>'
                "</tbody></table>"
                "<p>Children naturally have higher phosphorus levels than adults because of active bone growth. "
                "Phosphorus levels also fluctuate throughout the day and are affected by meals (especially high-phosphorus foods), "
                "so your doctor may ask you to fast before the test for accurate results.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high and low phosphorus",
            body_html=(
                "<p><strong>High phosphorus (hyperphosphatemia)</strong> is most commonly caused by:</p>"
                "<ul>"
                "<li><strong>Kidney disease</strong> &ndash; the most frequent cause. Failing kidneys cannot excrete phosphorus efficiently, "
                "leading to accumulation. See our <a href=\"/en/blog/creatinine-egfr-kidney-function\">creatinine &amp; eGFR guide</a>.</li>"
                "<li><strong>Hypoparathyroidism</strong> &ndash; low PTH reduces phosphorus excretion by the kidneys.</li>"
                "<li><strong>Excess vitamin D</strong> &ndash; increases intestinal absorption of phosphorus.</li>"
                "<li><strong>Diabetic ketoacidosis (DKA)</strong> &ndash; shifts phosphorus out of cells into the blood.</li>"
                "<li><strong>Rhabdomyolysis</strong> &ndash; massive muscle breakdown releases intracellular phosphorus.</li>"
                "</ul>"
                "<p><strong>Low phosphorus (hypophosphatemia)</strong> can result from:</p>"
                "<ul>"
                "<li><strong>Hyperparathyroidism</strong> &ndash; excess PTH drives urinary phosphorus loss.</li>"
                "<li><strong>Vitamin D deficiency</strong> &ndash; reduces intestinal phosphorus absorption.</li>"
                "<li><strong>Malnutrition and refeeding syndrome</strong> &ndash; when severely malnourished patients are refed, "
                "phosphorus shifts rapidly into cells, causing dangerous drops in serum levels.</li>"
                "<li><strong>Chronic antacid use</strong> &ndash; aluminium- and magnesium-containing antacids bind phosphorus in the gut.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of abnormal phosphorus levels",
            body_html=(
                "<p><strong>Hyperphosphatemia</strong> is often asymptomatic in its early stages, especially in chronic kidney disease. "
                "Over time, high phosphorus binds with calcium to form deposits in soft tissues, blood vessels, and joints, leading to:</p>"
                "<ul>"
                "<li>Vascular calcification and increased cardiovascular risk.</li>"
                "<li>Itchy skin (pruritus).</li>"
                "<li>Joint pain and bone disease (renal osteodystrophy).</li>"
                "<li>Red eyes due to calcium-phosphate deposits in the conjunctiva.</li>"
                "</ul>"
                "<p><strong>Hypophosphatemia</strong> symptoms depend on severity:</p>"
                "<ul>"
                "<li><strong>Mild</strong> &ndash; often no symptoms.</li>"
                "<li><strong>Moderate</strong> &ndash; muscle weakness, bone pain, fatigue.</li>"
                "<li><strong>Severe</strong> &ndash; confusion, seizures, respiratory failure (due to diaphragm weakness), "
                "hemolytic anemia, and rhabdomyolysis. Severe hypophosphatemia is a medical emergency.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>Phosphorus is almost always interpreted alongside other markers. Your doctor may order:</p>"
                "<ul>"
                "<li><strong>Calcium</strong> &ndash; phosphorus and calcium have an inverse relationship; when one rises, the other tends to fall. "
                "See our <a href=\"/en/blog/calcium-high-meaning\">calcium guide</a>.</li>"
                "<li><strong>PTH (Parathyroid Hormone)</strong> &ndash; regulates both calcium and phosphorus; essential for diagnosing "
                "parathyroid disorders.</li>"
                "<li><strong>Vitamin D (25-OH)</strong> &ndash; affects phosphorus absorption in the gut and reabsorption in the kidneys.</li>"
                "<li><strong>Creatinine &amp; eGFR</strong> &ndash; assesses kidney function, the primary regulator of phosphorus excretion. "
                "See our <a href=\"/en/blog/creatinine-egfr-kidney-function\">kidney function guide</a>.</li>"
                "<li><strong>Alkaline phosphatase (ALP)</strong> &ndash; may be elevated in bone diseases associated with phosphorus imbalance.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>You should discuss your phosphorus result with a healthcare provider if:</p>"
                "<ul>"
                "<li>Your phosphorus is above 4.5&nbsp;mg/dL or below 2.5&nbsp;mg/dL (adult reference).</li>"
                "<li>You have known kidney disease&mdash;phosphorus management is critical in CKD.</li>"
                "<li>You experience symptoms such as unexplained bone pain, muscle weakness, persistent itching, or fatigue.</li>"
                "<li>Your calcium level is also abnormal, suggesting a parathyroid or vitamin D disorder.</li>"
                "<li>You are recovering from severe illness or malnutrition (risk of refeeding syndrome).</li>"
                "</ul>"
                "<p>Your doctor can identify the underlying cause, adjust medications if needed, recommend dietary changes, "
                "and order follow-up labs to monitor your progress.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How NoryaAI helps you understand your phosphorus results",
            body_html=(
                "<p>NoryaAI makes it easy to understand your phosphorus and other blood test results. Simply "
                "<a href=\"/analyze\">upload your lab report</a>&mdash;whether it is a PDF, photo, or scan&mdash;and our AI engine will:</p>"
                "<ul>"
                "<li>Extract your phosphorus value along with all other biomarkers on the report.</li>"
                "<li>Compare each result against age- and sex-specific reference ranges.</li>"
                "<li>Flag abnormal values with clear, plain-language explanations.</li>"
                "<li>Highlight connections between related markers (e.g.&nbsp;phosphorus + calcium + PTH + vitamin D + creatinine).</li>"
                "<li>Generate a structured, doctor-ready summary you can share at your next appointment.</li>"
                "</ul>"
                "<p>Explore our <a href=\"/pricing\">pricing plans</a> to see which option fits your needs. "
                "NoryaAI is designed to help you prepare for&mdash;not replace&mdash;a conversation with your doctor.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Medical disclaimer",
            body_html=(
                "<p><strong>This article is for informational and educational purposes only. It does not constitute medical advice, "
                "diagnosis, or treatment. Always consult a qualified healthcare professional before making any decisions based on "
                "your lab results. NoryaAI provides automated analysis to help you understand your reports, but it is not a substitute "
                "for professional medical judgment.</strong></p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# TURKISH
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Fosfor kan testi: sonucunuz ne anlama geliyor?",
            body_html=(
                "<p>Fosfor (fosfat), kalsiyumdan sonra insan vücudundaki en bol ikinci mineraldir. "
                "Kemik oluşumu, enerji metabolizması ve hücre zarlarının yapısal bütünlüğü için hayati önem taşır. "
                "Kan testinizdeki fosfor değeri, serumunuzdaki inorganik fosfat miktarını ölçer.</p>"
                "<p>Anormal fosfor seviyeleri&mdash;yüksek (<strong>hiperfosfatemi</strong>) veya düşük (<strong>hipofosfatemi</strong>)&mdash;"
                "böbrek hastalığı, hormonal dengesizlikler, beslenme yetersizlikleri veya diğer tıbbi durumları gösterebilir.</p>"
                "<p>Bu makale eğitim amaçlıdır ve tıbbi tavsiye yerine geçmez. Sonuçlarınızı her zaman bir hekimle değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Fosfor nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Fosfor</strong>, güçlü kemikler ve dişler oluşturmak için <a href=\"/tr/blog/kalsiyum-yuksekligi-ne-anlama-gelir\">kalsiyum</a> "
                "ile yakın işbirliği içinde çalışan bir mineraldir. Vücuttaki fosforun yaklaşık %85&rsquo;i kemiklerde depolanır; "
                "kalan %15&rsquo;i yumuşak dokular ve vücut sıvılarına dağılır.</p>"
                "<p>Kemik sağlığının ötesinde fosfor şu işlevlerde de kritik rol oynar:</p>"
                "<ul>"
                "<li><strong>Enerji üretimi</strong> &ndash; ATP&rsquo;nin (adenozin trifosfat) temel bileşeni olan fosfor, vücudun birincil enerji kaynağıdır.</li>"
                "<li><strong>DNA ve RNA yapısı</strong> &ndash; nükleik asitlerin omurgası fosfat gruplarından oluşur.</li>"
                "<li><strong>Hücre zarı bütünlüğü</strong> &ndash; fosfolipitler her hücre zarının çift tabakasını oluşturur.</li>"
                "<li><strong>Asit-baz dengesi</strong> &ndash; fosfat, kan pH&rsquo;ını korumak için tampon görevi görür.</li>"
                "</ul>"
                "<p>Kandaki fosfor düzeyleri böbrekler, paratiroid hormonu (PTH) ve D vitamini tarafından sıkı bir şekilde düzenlenir. "
                "Bu düzenleyici sistem bozulduğunda&mdash;en sık böbrek hastalığıyla&mdash;fosfor seviyeleri normal aralıktan sapabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal fosfor aralıkları",
            body_html=(
                "<p>Kan testinizdeki fosfor değeri serum inorganik fosfatı yansıtır. Referans aralıkları laboratuvarlar arasında "
                "hafif farklılık gösterebilir; ancak aşağıdaki değerler yaygın olarak kabul edilir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yetişkinler</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5&ndash;4,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,81&ndash;1,45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Çocuklar</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4,0&ndash;7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,29&ndash;2,26</td></tr>'
                "</tbody></table>"
                "<p>Çocuklarda aktif kemik büyümesi nedeniyle fosfor seviyeleri doğal olarak yetişkinlerden yüksektir. "
                "Fosfor gün içinde dalgalanır ve yemeklerden etkilenir; bu nedenle doktorunuz test öncesi açlık isteyebilir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Yüksek ve düşük fosfor nedenleri",
            body_html=(
                "<p><strong>Yüksek fosfor (hiperfosfatemi)</strong> en sık şu nedenlerle ortaya çıkar:</p>"
                "<ul>"
                "<li><strong>Böbrek hastalığı</strong> &ndash; en yaygın neden. Yetersiz çalışan böbrekler fosforu yeterince atamaz. "
                "<a href=\"/tr/blog/kreatinin-egfr-bobrek-fonksiyonu\">Kreatinin ve eGFR rehberimize</a> bakın.</li>"
                "<li><strong>Hipoparatiroidizm</strong> &ndash; düşük PTH böbreklerde fosfor atılımını azaltır.</li>"
                "<li><strong>Aşırı D vitamini</strong> &ndash; bağırsaktan fosfor emilimini artırır.</li>"
                "<li><strong>Diyabetik ketoasidoz (DKA)</strong> &ndash; fosforu hücrelerden kana kaydırır.</li>"
                "<li><strong>Rabdomiyoliz</strong> &ndash; yaygın kas yıkımı hücre içi fosforu serbest bırakır.</li>"
                "</ul>"
                "<p><strong>Düşük fosfor (hipofosfatemi)</strong> şu durumlardan kaynaklanabilir:</p>"
                "<ul>"
                "<li><strong>Hiperparatiroidizm</strong> &ndash; fazla PTH idrarla fosfor kaybını artırır.</li>"
                "<li><strong>D vitamini eksikliği</strong> &ndash; bağırsaktan fosfor emilimini azaltır.</li>"
                "<li><strong>Malnütrisyon ve yeniden beslenme sendromu</strong> &ndash; ciddi malnütrisyonlu hastalar beslenmeye başladığında "
                "fosfor hızla hücrelere kayar ve serum düzeyleri tehlikeli biçimde düşer.</li>"
                "<li><strong>Kronik antiasit kullanımı</strong> &ndash; alüminyum ve magnezyum içeren antiasitler bağırsakta fosforu bağlar.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Anormal fosfor düzeylerinin belirtileri",
            body_html=(
                "<p><strong>Hiperfosfatemi</strong> özellikle kronik böbrek hastalığında başlangıçta genellikle belirtisizdir. "
                "Zamanla yüksek fosfor kalsiyumla birleşerek yumuşak dokularda, damarlarda ve eklemlerde birikintilere yol açar:</p>"
                "<ul>"
                "<li>Damar kalsifikasyonu ve artmış kardiyovasküler risk.</li>"
                "<li>Kaşıntılı cilt (pruritus).</li>"
                "<li>Eklem ağrısı ve kemik hastalığı (renal osteodistrofi).</li>"
                "<li>Konjunktivada kalsiyum-fosfat birikimleri nedeniyle kırmızı gözler.</li>"
                "</ul>"
                "<p><strong>Hipofosfatemi</strong> belirtileri şiddetine bağlıdır:</p>"
                "<ul>"
                "<li><strong>Hafif</strong> &ndash; genellikle belirtisiz.</li>"
                "<li><strong>Orta</strong> &ndash; kas güçsüzlüğü, kemik ağrısı, yorgunluk.</li>"
                "<li><strong>Şiddetli</strong> &ndash; konfüzyon, nöbetler, solunum yetmezliği, hemolitik anemi ve rabdomiyoliz. "
                "Şiddetli hipofosfatemi tıbbi bir acildir.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlişkili testler",
            body_html=(
                "<p>Fosfor neredeyse her zaman diğer belirteçlerle birlikte yorumlanır:</p>"
                "<ul>"
                "<li><strong>Kalsiyum</strong> &ndash; fosfor ve kalsiyum ters orantılı bir ilişkiye sahiptir. "
                "<a href=\"/tr/blog/kalsiyum-yuksekligi-ne-anlama-gelir\">Kalsiyum rehberimize</a> bakın.</li>"
                "<li><strong>PTH (Paratiroid Hormonu)</strong> &ndash; hem kalsiyum hem fosforu düzenler.</li>"
                "<li><strong>D Vitamini (25-OH)</strong> &ndash; bağırsakta fosfor emilimini etkiler.</li>"
                "<li><strong>Kreatinin ve eGFR</strong> &ndash; böbrek fonksiyonunu değerlendirir. "
                "<a href=\"/tr/blog/kreatinin-egfr-bobrek-fonksiyonu\">Böbrek fonksiyon rehberimize</a> bakın.</li>"
                "<li><strong>Alkalen fosfataz (ALP)</strong> &ndash; fosfor dengesizliğiyle ilişkili kemik hastalıklarında yükselebilir.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda fosfor sonucunuzu bir hekimle değerlendirmelisiniz:</p>"
                "<ul>"
                "<li>Fosforunuz 4,5&nbsp;mg/dL&rsquo;nin üstünde veya 2,5&nbsp;mg/dL&rsquo;nin altında.</li>"
                "<li>Bilinen böbrek hastalığınız var&mdash;KBH&rsquo;de fosfor yönetimi kritiktir.</li>"
                "<li>Açıklanamayan kemik ağrısı, kas güçsüzlüğü, sürekli kaşıntı veya yorgunluk yaşıyorsunuz.</li>"
                "<li>Kalsiyum değeriniz de anormal&mdash;bu paratiroid veya D vitamini bozukluğu düşündürür.</li>"
                "<li>Ciddi hastalık veya malnütrisyondan iyileşiyorsunuz (yeniden beslenme sendromu riski).</li>"
                "</ul>"
                "<p>Doktorunuz altta yatan nedeni belirleyebilir, gerekirse ilaçları ayarlayabilir, diyet değişiklikleri önerebilir "
                "ve ilerlemenizi takip etmek için kontrol testleri isteyebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI fosfor sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>NoryaAI, fosfor ve diğer kan testi sonuçlarınızı kolayca anlamanızı sağlar. "
                "<a href=\"/analyze\">Laboratuvar raporunuzu yükleyin</a>&mdash;PDF, fotoğraf veya tarama&mdash;yapay zeka motorumuz:</p>"
                "<ul>"
                "<li>Rapordaki fosfor değerini ve diğer tüm biyobelirteçleri çıkarır.</li>"
                "<li>Her sonucu yaş ve cinsiyete özel referans aralıklarıyla karşılaştırır.</li>"
                "<li>Anormal değerleri sade açıklamalarla işaretler.</li>"
                "<li>İlişkili belirteçler arasındaki bağlantıları vurgular (fosfor + kalsiyum + PTH + D vitamini + kreatinin).</li>"
                "<li>Doktorunuza götürebileceğiniz yapılandırılmış bir özet oluşturur.</li>"
                "</ul>"
                "<p><a href=\"/pricing\">Fiyatlandırma planlarımızı</a> inceleyerek size uygun seçeneği bulun.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Tıbbi sorumluluk reddi",
            body_html=(
                "<p><strong>Bu makale yalnızca bilgilendirme ve eğitim amaçlıdır. Tıbbi tavsiye, teşhis veya tedavi niteliği taşımaz. "
                "Laboratuvar sonuçlarınıza dayalı herhangi bir karar vermeden önce mutlaka nitelikli bir sağlık uzmanına danışın. "
                "NoryaAI, raporlarınızı anlamanıza yardımcı olmak için otomatik analiz sunar ancak profesyonel tıbbi değerlendirmenin "
                "yerini tutmaz.</strong></p>"
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
            heading="Análisis de fósforo en sangre: qué significa tu resultado",
            body_html=(
                "<p>El fósforo (fosfato) es el segundo mineral más abundante en el cuerpo humano después del calcio. "
                "Es esencial para la formación ósea, el metabolismo energético y la integridad estructural de las membranas celulares. "
                "El valor de fósforo en tu análisis mide el fosfato inorgánico disuelto en el suero.</p>"
                "<p>Niveles anormales&mdash;altos (<strong>hiperfosfatemia</strong>) o bajos (<strong>hipofosfatemia</strong>)&mdash;"
                "pueden indicar enfermedad renal, desequilibrios hormonales o deficiencias nutricionales.</p>"
                "<p>Este artículo es educativo y no sustituye el consejo médico. Comenta tus resultados con tu médico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es el fósforo y por qué es importante?",
            body_html=(
                "<p>El <strong>fósforo</strong> trabaja estrechamente con el <a href=\"/es/blog/calcio-alto-significado\">calcio</a> "
                "para formar huesos y dientes fuertes. Aproximadamente el 85% del fósforo corporal se almacena en los huesos.</p>"
                "<p>Además de la salud ósea, el fósforo participa en:</p>"
                "<ul>"
                "<li><strong>Producción de energía</strong> &ndash; componente clave del ATP.</li>"
                "<li><strong>Estructura del ADN y ARN</strong> &ndash; la columna vertebral de los ácidos nucleicos está formada por grupos fosfato.</li>"
                "<li><strong>Integridad de la membrana celular</strong> &ndash; los fosfolípidos forman la bicapa de cada membrana.</li>"
                "<li><strong>Equilibrio ácido-base</strong> &ndash; el fosfato actúa como tampón para mantener el pH sanguíneo.</li>"
                "</ul>"
                "<p>Los niveles de fósforo están regulados por los riñones, la PTH y la vitamina D. Cuando este sistema se altera, "
                "generalmente por enfermedad renal, los niveles pueden desviarse del rango normal.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos normales de fósforo",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adultos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5&ndash;4,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,81&ndash;1,45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Niños</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4,0&ndash;7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,29&ndash;2,26</td></tr>'
                "</tbody></table>"
                "<p>Los niños tienen niveles más altos de forma natural por el crecimiento óseo activo. "
                "Los niveles fluctúan durante el día y se ven afectados por las comidas.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de fósforo alto y bajo",
            body_html=(
                "<p><strong>Fósforo alto (hiperfosfatemia)</strong>:</p>"
                "<ul>"
                "<li><strong>Enfermedad renal</strong> &ndash; causa más frecuente; los riñones no pueden excretar el fósforo. "
                "Consulta nuestra <a href=\"/es/blog/creatinina-egfr-funcion-renal\">guía de función renal</a>.</li>"
                "<li><strong>Hipoparatiroidismo</strong> &ndash; la PTH baja reduce la excreción renal de fósforo.</li>"
                "<li><strong>Exceso de vitamina D</strong> &ndash; aumenta la absorción intestinal.</li>"
                "<li><strong>Cetoacidosis diabética</strong> &ndash; desplaza el fósforo de las células a la sangre.</li>"
                "<li><strong>Rabdomiólisis</strong> &ndash; la destrucción muscular masiva libera fósforo intracelular.</li>"
                "</ul>"
                "<p><strong>Fósforo bajo (hipofosfatemia)</strong>:</p>"
                "<ul>"
                "<li><strong>Hiperparatiroidismo</strong> &ndash; el exceso de PTH provoca pérdida urinaria de fósforo.</li>"
                "<li><strong>Deficiencia de vitamina D</strong> &ndash; reduce la absorción intestinal.</li>"
                "<li><strong>Malnutrición y síndrome de realimentación</strong> &ndash; el fósforo se desplaza rápidamente a las células al reintroducir alimentos.</li>"
                "<li><strong>Uso crónico de antiácidos</strong> &ndash; los antiácidos con aluminio o magnesio unen el fósforo intestinal.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de niveles anormales de fósforo",
            body_html=(
                "<p>La <strong>hiperfosfatemia</strong> suele ser asintomática al principio. Con el tiempo, el fósforo alto forma depósitos "
                "de calcio-fosfato en tejidos blandos y vasos sanguíneos, causando calcificación vascular, prurito, dolor articular "
                "y osteodistrofia renal.</p>"
                "<p>La <strong>hipofosfatemia</strong> varía según la gravedad:</p>"
                "<ul>"
                "<li><strong>Leve</strong> &ndash; generalmente sin síntomas.</li>"
                "<li><strong>Moderada</strong> &ndash; debilidad muscular, dolor óseo, fatiga.</li>"
                "<li><strong>Grave</strong> &ndash; confusión, convulsiones, insuficiencia respiratoria, anemia hemolítica. Es una emergencia médica.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p>El fósforo se interpreta junto con otros marcadores:</p>"
                "<ul>"
                "<li><strong>Calcio</strong> &ndash; relación inversa con el fósforo. <a href=\"/es/blog/calcio-alto-significado\">Guía de calcio</a>.</li>"
                "<li><strong>PTH</strong> &ndash; regula calcio y fósforo.</li>"
                "<li><strong>Vitamina D</strong> &ndash; afecta la absorción de fósforo.</li>"
                "<li><strong>Creatinina y eGFR</strong> &ndash; evalúan la función renal. <a href=\"/es/blog/creatinina-egfr-funcion-renal\">Guía renal</a>.</li>"
                "<li><strong>Fosfatasa alcalina (ALP)</strong> &ndash; puede elevarse en enfermedades óseas.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Consulta si tu fósforo está fuera del rango (adultos: 2,5&ndash;4,5 mg/dL), tienes enfermedad renal conocida, "
                "presentas dolor óseo, debilidad muscular o picazón persistente, tu calcio también es anormal, "
                "o te estás recuperando de desnutrición severa.</p>"
                "<p>Tu médico identificará la causa, ajustará medicamentos si es necesario y solicitará controles de seguimiento.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo NoryaAI te ayuda con tu fósforo",
            body_html=(
                "<p>NoryaAI facilita la comprensión de tus análisis. <a href=\"/analyze\">Sube tu informe</a>&mdash;PDF, foto o escaneo&mdash;y nuestra IA:</p>"
                "<ul>"
                "<li>Extrae tu fósforo y todos los biomarcadores.</li>"
                "<li>Compara cada resultado con rangos de referencia por edad y sexo.</li>"
                "<li>Señala valores anormales con explicaciones claras.</li>"
                "<li>Destaca relaciones entre marcadores (fósforo + calcio + PTH + vitamina D).</li>"
                "<li>Genera un resumen estructurado listo para tu médico.</li>"
                "</ul>"
                "<p>Explora nuestros <a href=\"/pricing\">planes de precios</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso médico",
            body_html=(
                "<p><strong>Este artículo es solo informativo y educativo. No constituye consejo médico, diagnóstico ni tratamiento. "
                "Consulta siempre a un profesional de salud cualificado. NoryaAI ofrece análisis automatizado pero no sustituye "
                "el criterio médico profesional.</strong></p>"
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
            heading="Phosphor-Bluttest: Was Ihr Ergebnis bedeutet",
            body_html=(
                "<p>Phosphor (Phosphat) ist nach Kalzium das zweithäufigste Mineral im menschlichen Körper. "
                "Es ist essentiell für den Knochenaufbau, den Energiestoffwechsel und die strukturelle Integrität der Zellmembranen. "
                "Der Phosphorwert in Ihrer Blutuntersuchung misst das anorganische Phosphat in Ihrem Serum.</p>"
                "<p>Abnormale Phosphorwerte&mdash;erhöht (<strong>Hyperphosphatämie</strong>) oder erniedrigt (<strong>Hypophosphatämie</strong>)&mdash;"
                "können auf Nierenerkrankungen, hormonelle Störungen oder Ernährungsdefizite hinweisen.</p>"
                "<p>Dieser Artikel dient der Aufklärung und ersetzt keine ärztliche Beratung.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist Phosphor und warum ist es wichtig?",
            body_html=(
                "<p><strong>Phosphor</strong> arbeitet eng mit <a href=\"/de/blog/kalzium-hoch-bedeutung\">Kalzium</a> zusammen, "
                "um starke Knochen und Zähne aufzubauen. Etwa 85% des Körperphosphors ist in den Knochen gespeichert.</p>"
                "<p>Phosphor spielt außerdem wichtige Rollen bei:</p>"
                "<ul>"
                "<li><strong>Energieproduktion</strong> &ndash; Schlüsselkomponente von ATP.</li>"
                "<li><strong>DNA- und RNA-Struktur</strong> &ndash; das Rückgrat der Nukleinsäuren besteht aus Phosphatgruppen.</li>"
                "<li><strong>Zellmembranintegrität</strong> &ndash; Phospholipide bilden die Doppelschicht jeder Zellmembran.</li>"
                "<li><strong>Säure-Basen-Gleichgewicht</strong> &ndash; Phosphat wirkt als Puffer.</li>"
                "</ul>"
                "<p>Die Phosphorspiegel werden von den Nieren, dem Parathormon (PTH) und Vitamin D reguliert. "
                "Bei Störungen&mdash;am häufigsten durch Nierenerkrankungen&mdash;weichen die Werte vom Normalbereich ab.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Phosphorwerte",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erwachsene</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5&ndash;4,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,81&ndash;1,45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kinder</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4,0&ndash;7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,29&ndash;2,26</td></tr>'
                "</tbody></table>"
                "<p>Kinder haben natürlicherweise höhere Phosphorwerte aufgrund des aktiven Knochenwachstums. "
                "Die Werte schwanken im Tagesverlauf und werden durch Mahlzeiten beeinflusst.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für hohen und niedrigen Phosphor",
            body_html=(
                "<p><strong>Hoher Phosphor (Hyperphosphatämie)</strong>:</p>"
                "<ul>"
                "<li><strong>Nierenerkrankung</strong> &ndash; häufigste Ursache. <a href=\"/de/blog/kreatinin-egfr-nierenfunktion\">Nierenfunktions-Ratgeber</a>.</li>"
                "<li><strong>Hypoparathyreoidismus</strong> &ndash; niedriges PTH vermindert die Phosphorausscheidung.</li>"
                "<li><strong>Vitamin-D-Überschuss</strong> &ndash; erhöht die intestinale Absorption.</li>"
                "<li><strong>Diabetische Ketoazidose</strong> &ndash; verschiebt Phosphor aus den Zellen ins Blut.</li>"
                "<li><strong>Rhabdomyolyse</strong> &ndash; massiver Muskelzerfall setzt intrazelluläres Phosphor frei.</li>"
                "</ul>"
                "<p><strong>Niedriger Phosphor (Hypophosphatämie)</strong>:</p>"
                "<ul>"
                "<li><strong>Hyperparathyreoidismus</strong> &ndash; übermäßiges PTH fördert den Phosphorverlust über den Urin.</li>"
                "<li><strong>Vitamin-D-Mangel</strong> &ndash; reduziert die intestinale Absorption.</li>"
                "<li><strong>Mangelernährung und Refeeding-Syndrom</strong> &ndash; Phosphor verschiebt sich beim Wiederaufbau schnell in die Zellen.</li>"
                "<li><strong>Chronischer Antazida-Gebrauch</strong> &ndash; bindet Phosphor im Darm.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome abnormaler Phosphorwerte",
            body_html=(
                "<p><strong>Hyperphosphatämie</strong> verläuft anfangs oft symptomlos. Langfristig bildet hoher Phosphor Kalzium-Phosphat-Ablagerungen "
                "in Weichgeweben und Gefäßen: vaskuläre Kalzifikation, Juckreiz, Gelenkschmerzen und renale Osteodystrophie.</p>"
                "<p><strong>Hypophosphatämie</strong>:</p>"
                "<ul>"
                "<li><strong>Leicht</strong> &ndash; meist symptomlos.</li>"
                "<li><strong>Mittel</strong> &ndash; Muskelschwäche, Knochenschmerzen, Müdigkeit.</li>"
                "<li><strong>Schwer</strong> &ndash; Verwirrtheit, Krampfanfälle, Atemversagen, hämolytische Anämie. Dies ist ein medizinischer Notfall.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Verwandte Laborwerte",
            body_html=(
                "<p>Phosphor wird fast immer mit anderen Markern interpretiert:</p>"
                "<ul>"
                "<li><strong>Kalzium</strong> &ndash; inverse Beziehung zu Phosphor. <a href=\"/de/blog/kalzium-hoch-bedeutung\">Kalzium-Ratgeber</a>.</li>"
                "<li><strong>PTH</strong> &ndash; reguliert Kalzium und Phosphor.</li>"
                "<li><strong>Vitamin D</strong> &ndash; beeinflusst die Phosphorabsorption.</li>"
                "<li><strong>Kreatinin &amp; eGFR</strong> &ndash; beurteilt die Nierenfunktion. <a href=\"/de/blog/kreatinin-egfr-nierenfunktion\">Nieren-Ratgeber</a>.</li>"
                "<li><strong>Alkalische Phosphatase (ALP)</strong> &ndash; bei Knochenerkrankungen erhöht.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann Sie einen Arzt aufsuchen sollten",
            body_html=(
                "<p>Sprechen Sie mit Ihrem Arzt, wenn Ihr Phosphor außerhalb des Referenzbereichs liegt (Erwachsene: 2,5&ndash;4,5 mg/dL), "
                "Sie an einer Nierenerkrankung leiden, unerklärliche Knochenschmerzen, Muskelschwäche oder Juckreiz haben, "
                "Ihr Kalzium ebenfalls auffällig ist, oder Sie sich von schwerer Mangelernährung erholen.</p>"
                "<p>Ihr Arzt wird die Ursache identifizieren, Medikamente anpassen und Nachkontrollen anordnen.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie NoryaAI bei Ihren Phosphorwerten hilft",
            body_html=(
                "<p>NoryaAI macht es einfach, Ihre Phosphor- und andere Blutwerte zu verstehen. "
                "<a href=\"/analyze\">Laden Sie Ihren Befund hoch</a>&mdash;PDF, Foto oder Scan&mdash;und unsere KI:</p>"
                "<ul>"
                "<li>Extrahiert Ihren Phosphorwert und alle weiteren Biomarker.</li>"
                "<li>Vergleicht jeden Wert mit alters- und geschlechtsspezifischen Bereichen.</li>"
                "<li>Markiert auffällige Werte mit verständlichen Erklärungen.</li>"
                "<li>Hebt Zusammenhänge hervor (Phosphor + Kalzium + PTH + Vitamin D + Kreatinin).</li>"
                "<li>Erstellt eine arztfertige Zusammenfassung.</li>"
                "</ul>"
                "<p>Entdecken Sie unsere <a href=\"/pricing\">Preispläne</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Medizinischer Haftungsausschluss",
            body_html=(
                "<p><strong>Dieser Artikel dient ausschließlich der Information und Aufklärung. Er stellt keine medizinische Beratung, "
                "Diagnose oder Behandlung dar. Konsultieren Sie immer einen qualifizierten Arzt. NoryaAI bietet automatisierte Analysen, "
                "ersetzt aber kein ärztliches Urteil.</strong></p>"
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
            heading="Analyse du phosphore sanguin : que signifie votre résultat ?",
            body_html=(
                "<p>Le phosphore (phosphate) est le deuxième minéral le plus abondant dans le corps humain après le calcium. "
                "Il est essentiel à la formation osseuse, au métabolisme énergétique et à l&rsquo;intégrité des membranes cellulaires. "
                "La valeur de phosphore dans votre bilan mesure le phosphate inorganique dans votre sérum.</p>"
                "<p>Des niveaux anormaux&mdash;élevés (<strong>hyperphosphatémie</strong>) ou bas (<strong>hypophosphatémie</strong>)&mdash;"
                "peuvent indiquer une maladie rénale, des déséquilibres hormonaux ou des carences nutritionnelles.</p>"
                "<p>Cet article est éducatif et ne remplace pas un avis médical.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu'est-ce que le phosphore et pourquoi est-il important ?",
            body_html=(
                "<p>Le <strong>phosphore</strong> travaille avec le <a href=\"/fr/blog/calcium-eleve-signification\">calcium</a> pour construire "
                "des os solides. Environ 85% du phosphore se trouve dans les os.</p>"
                "<p>Le phosphore intervient également dans :</p>"
                "<ul>"
                "<li><strong>Production d&rsquo;énergie</strong> &ndash; composant clé de l&rsquo;ATP.</li>"
                "<li><strong>Structure de l&rsquo;ADN et de l&rsquo;ARN</strong> &ndash; les groupes phosphate forment le squelette des acides nucléiques.</li>"
                "<li><strong>Intégrité membranaire</strong> &ndash; les phospholipides forment la bicouche cellulaire.</li>"
                "<li><strong>Équilibre acido-basique</strong> &ndash; le phosphate agit comme tampon.</li>"
                "</ul>"
                "<p>Les niveaux sont régulés par les reins, la PTH et la vitamine D. Une perturbation&mdash;le plus souvent rénale&mdash;"
                "entraîne des écarts par rapport à la normale.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales du phosphore",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adultes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5&ndash;4,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,81&ndash;1,45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Enfants</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4,0&ndash;7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,29&ndash;2,26</td></tr>'
                "</tbody></table>"
                "<p>Les enfants ont naturellement des niveaux plus élevés en raison de la croissance osseuse active. "
                "Les niveaux fluctuent au cours de la journée et sont influencés par les repas.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un phosphore élevé ou bas",
            body_html=(
                "<p><strong>Phosphore élevé (hyperphosphatémie)</strong> :</p>"
                "<ul>"
                "<li><strong>Maladie rénale</strong> &ndash; cause la plus fréquente. <a href=\"/fr/blog/creatinine-egfr-fonction-renale\">Guide rénal</a>.</li>"
                "<li><strong>Hypoparathyroïdie</strong> &ndash; PTH basse réduit l&rsquo;excrétion rénale.</li>"
                "<li><strong>Excès de vitamine D</strong> &ndash; augmente l&rsquo;absorption intestinale.</li>"
                "<li><strong>Acidocétose diabétique</strong> &ndash; déplace le phosphore des cellules vers le sang.</li>"
                "<li><strong>Rhabdomyolyse</strong> &ndash; destruction musculaire massive libérant le phosphore intracellulaire.</li>"
                "</ul>"
                "<p><strong>Phosphore bas (hypophosphatémie)</strong> :</p>"
                "<ul>"
                "<li><strong>Hyperparathyroïdie</strong> &ndash; excès de PTH provoquant la perte urinaire de phosphore.</li>"
                "<li><strong>Carence en vitamine D</strong> &ndash; réduit l&rsquo;absorption intestinale.</li>"
                "<li><strong>Malnutrition et syndrome de renutrition</strong> &ndash; le phosphore se déplace rapidement dans les cellules.</li>"
                "<li><strong>Antiacides chroniques</strong> &ndash; lient le phosphore dans l&rsquo;intestin.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes de niveaux anormaux de phosphore",
            body_html=(
                "<p>L&rsquo;<strong>hyperphosphatémie</strong> est souvent asymptomatique au début. À terme, des dépôts de calcium-phosphate "
                "se forment dans les tissus mous et les vaisseaux : calcification vasculaire, prurit, douleurs articulaires, ostéodystrophie rénale.</p>"
                "<p>L&rsquo;<strong>hypophosphatémie</strong> :</p>"
                "<ul>"
                "<li><strong>Légère</strong> &ndash; souvent asymptomatique.</li>"
                "<li><strong>Modérée</strong> &ndash; faiblesse musculaire, douleurs osseuses, fatigue.</li>"
                "<li><strong>Sévère</strong> &ndash; confusion, convulsions, insuffisance respiratoire, anémie hémolytique. C&rsquo;est une urgence médicale.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Analyses associées",
            body_html=(
                "<ul>"
                "<li><strong>Calcium</strong> &ndash; relation inverse avec le phosphore. <a href=\"/fr/blog/calcium-eleve-signification\">Guide calcium</a>.</li>"
                "<li><strong>PTH</strong> &ndash; régule le calcium et le phosphore.</li>"
                "<li><strong>Vitamine D</strong> &ndash; influence l&rsquo;absorption du phosphore.</li>"
                "<li><strong>Créatinine et DFGe</strong> &ndash; évalue la fonction rénale. <a href=\"/fr/blog/creatinine-egfr-fonction-renale\">Guide rénal</a>.</li>"
                "<li><strong>Phosphatase alcaline (PAL)</strong> &ndash; élevée dans les maladies osseuses.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin",
            body_html=(
                "<p>Consultez si votre phosphore est hors normes (adultes : 2,5&ndash;4,5 mg/dL), si vous avez une maladie rénale connue, "
                "des douleurs osseuses, une faiblesse musculaire, un prurit persistant, un calcium anormal, "
                "ou si vous vous remettez d&rsquo;une malnutrition sévère.</p>"
                "<p>Votre médecin identifiera la cause, ajustera le traitement et prescrira un suivi.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment NoryaAI vous aide avec votre phosphore",
            body_html=(
                "<p>NoryaAI simplifie la compréhension de vos résultats. <a href=\"/analyze\">Téléchargez votre bilan</a>&mdash;PDF, photo ou scan&mdash;et notre IA :</p>"
                "<ul>"
                "<li>Extrait votre phosphore et tous les biomarqueurs.</li>"
                "<li>Compare chaque résultat aux valeurs de référence.</li>"
                "<li>Signale les anomalies avec des explications claires.</li>"
                "<li>Met en évidence les liens (phosphore + calcium + PTH + vitamine D).</li>"
                "<li>Génère un résumé structuré pour votre médecin.</li>"
                "</ul>"
                "<p>Découvrez nos <a href=\"/pricing\">formules tarifaires</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement médical",
            body_html=(
                "<p><strong>Cet article est fourni à titre informatif et éducatif uniquement. Il ne constitue pas un avis médical. "
                "Consultez toujours un professionnel de santé qualifié. NoryaAI propose une analyse automatisée mais ne remplace pas "
                "le jugement médical professionnel.</strong></p>"
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
            heading="Analisi del fosforo nel sangue: cosa significa il tuo risultato",
            body_html=(
                "<p>Il fosforo (fosfato) è il secondo minerale più abbondante nel corpo umano dopo il calcio. "
                "È essenziale per la formazione ossea, il metabolismo energetico e l&rsquo;integrità delle membrane cellulari. "
                "Il valore di fosforo nel tuo esame del sangue misura il fosfato inorganico nel siero.</p>"
                "<p>Livelli anomali&mdash;alti (<strong>iperfosfatemia</strong>) o bassi (<strong>ipofosfatemia</strong>)&mdash;"
                "possono indicare malattie renali, squilibri ormonali o carenze nutrizionali.</p>"
                "<p>Questo articolo è educativo e non sostituisce il parere medico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Cos'è il fosforo e perché è importante?",
            body_html=(
                "<p>Il <strong>fosforo</strong> lavora con il <a href=\"/it/blog/calcio-alto-significato\">calcio</a> per costruire ossa e denti forti. "
                "Circa l&rsquo;85% del fosforo è nelle ossa.</p>"
                "<p>Il fosforo partecipa anche a:</p>"
                "<ul>"
                "<li><strong>Produzione di energia</strong> &ndash; componente chiave dell&rsquo;ATP.</li>"
                "<li><strong>Struttura di DNA e RNA</strong> &ndash; gruppi fosfato formano lo scheletro degli acidi nucleici.</li>"
                "<li><strong>Integrità della membrana cellulare</strong> &ndash; i fosfolipidi formano il doppio strato.</li>"
                "<li><strong>Equilibrio acido-base</strong> &ndash; il fosfato funge da tampone.</li>"
                "</ul>"
                "<p>I livelli sono regolati da reni, PTH e vitamina D. Un&rsquo;alterazione porta a deviazioni dalla norma.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del fosforo",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adulti</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5&ndash;4,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,81&ndash;1,45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Bambini</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4,0&ndash;7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,29&ndash;2,26</td></tr>'
                "</tbody></table>"
                "<p>I bambini hanno livelli naturalmente più alti per la crescita ossea attiva. "
                "I livelli fluttuano durante il giorno e sono influenzati dai pasti.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di fosforo alto e basso",
            body_html=(
                "<p><strong>Fosforo alto (iperfosfatemia)</strong>:</p>"
                "<ul>"
                "<li><strong>Malattia renale</strong> &ndash; causa più frequente. <a href=\"/it/blog/creatinina-egfr-funzione-renale\">Guida renale</a>.</li>"
                "<li><strong>Ipoparatiroidismo</strong> &ndash; PTH basso riduce l&rsquo;escrezione.</li>"
                "<li><strong>Eccesso di vitamina D</strong> &ndash; aumenta l&rsquo;assorbimento intestinale.</li>"
                "<li><strong>Chetoacidosi diabetica</strong> &ndash; sposta il fosforo dalle cellule al sangue.</li>"
                "<li><strong>Rabdomiolisi</strong> &ndash; distruzione muscolare massiva rilascia fosforo intracellulare.</li>"
                "</ul>"
                "<p><strong>Fosforo basso (ipofosfatemia)</strong>:</p>"
                "<ul>"
                "<li><strong>Iperparatiroidismo</strong> &ndash; eccesso di PTH causa perdita urinaria.</li>"
                "<li><strong>Carenza di vitamina D</strong> &ndash; riduce l&rsquo;assorbimento intestinale.</li>"
                "<li><strong>Malnutrizione e sindrome da rialimentazione</strong> &ndash; il fosforo si sposta rapidamente nelle cellule.</li>"
                "<li><strong>Antiacidi cronici</strong> &ndash; legano il fosforo nell&rsquo;intestino.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi di livelli anomali di fosforo",
            body_html=(
                "<p>L&rsquo;<strong>iperfosfatemia</strong> è spesso asintomatica all&rsquo;inizio. Nel tempo, depositi di calcio-fosfato "
                "si formano nei tessuti molli e nei vasi: calcificazione vascolare, prurito, dolore articolare, osteodistrofia renale.</p>"
                "<p>L&rsquo;<strong>ipofosfatemia</strong>:</p>"
                "<ul>"
                "<li><strong>Lieve</strong> &ndash; spesso asintomatica.</li>"
                "<li><strong>Moderata</strong> &ndash; debolezza muscolare, dolore osseo, stanchezza.</li>"
                "<li><strong>Grave</strong> &ndash; confusione, convulsioni, insufficienza respiratoria, anemia emolitica. È un&rsquo;emergenza medica.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<ul>"
                "<li><strong>Calcio</strong> &ndash; relazione inversa. <a href=\"/it/blog/calcio-alto-significato\">Guida calcio</a>.</li>"
                "<li><strong>PTH</strong> &ndash; regola calcio e fosforo.</li>"
                "<li><strong>Vitamina D</strong> &ndash; influenza l&rsquo;assorbimento del fosforo.</li>"
                "<li><strong>Creatinina ed eGFR</strong> &ndash; valuta la funzione renale. <a href=\"/it/blog/creatinina-egfr-funzione-renale\">Guida renale</a>.</li>"
                "<li><strong>Fosfatasi alcalina (ALP)</strong> &ndash; elevata nelle malattie ossee.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico",
            body_html=(
                "<p>Consulta se il fosforo è fuori range (adulti: 2,5&ndash;4,5 mg/dL), hai una malattia renale nota, "
                "presenti dolore osseo, debolezza muscolare o prurito, il calcio è anomalo, "
                "o ti stai riprendendo da malnutrizione severa.</p>"
                "<p>Il medico identificherà la causa, adeguerà la terapia e prescriverà controlli di follow-up.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come NoryaAI ti aiuta con il fosforo",
            body_html=(
                "<p>NoryaAI semplifica la comprensione dei tuoi esami. <a href=\"/analyze\">Carica il tuo referto</a>&mdash;PDF, foto o scansione&mdash;e la nostra IA:</p>"
                "<ul>"
                "<li>Estrae il fosforo e tutti i biomarcatori.</li>"
                "<li>Confronta ogni risultato con intervalli di riferimento per età e sesso.</li>"
                "<li>Segnala anomalie con spiegazioni chiare.</li>"
                "<li>Evidenzia le connessioni (fosforo + calcio + PTH + vitamina D).</li>"
                "<li>Genera un riepilogo strutturato per il medico.</li>"
                "</ul>"
                "<p>Scopri i nostri <a href=\"/pricing\">piani tariffari</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza medica",
            body_html=(
                "<p><strong>Questo articolo è solo informativo ed educativo. Non costituisce consulenza medica, diagnosi o trattamento. "
                "Consulta sempre un professionista sanitario qualificato. NoryaAI offre analisi automatizzate ma non sostituisce "
                "il giudizio medico professionale.</strong></p>"
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
            heading="בדיקת זרחן בדם: מה המשמעות של התוצאה שלך?",
            body_html=(
                "<p>זרחן (פוספט) הוא המינרל השני בשכיחותו בגוף האדם אחרי סידן. "
                "הוא חיוני לבניית עצמות, מטבוליזם אנרגטי ושלמות מבנית של ממברנות התא. "
                "ערך הזרחן בבדיקת הדם שלך מודד את הפוספט האנאורגני בסרום.</p>"
                "<p>רמות חריגות&mdash;גבוהות (<strong>היפרפוספטמיה</strong>) או נמוכות (<strong>היפופוספטמיה</strong>)&mdash;"
                "עשויות להצביע על מחלת כליות, חוסר איזון הורמונלי או חוסרים תזונתיים.</p>"
                "<p>מאמר זה חינוכי בלבד ואינו מחליף ייעוץ רפואי.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהו זרחן ומדוע הוא חשוב?",
            body_html=(
                "<p><strong>זרחן</strong> פועל בשיתוף עם <a href=\"/he/blog/calcium-high-meaning\">סידן</a> לבניית עצמות ושיניים חזקות. "
                "כ-85% מהזרחן בגוף נמצא בעצמות.</p>"
                "<p>זרחן גם מעורב ב:</p>"
                "<ul>"
                "<li><strong>ייצור אנרגיה</strong> &ndash; מרכיב מפתח של ATP.</li>"
                "<li><strong>מבנה DNA ו-RNA</strong> &ndash; שלד חומצות הגרעין מורכב מקבוצות פוספט.</li>"
                "<li><strong>שלמות ממברנת התא</strong> &ndash; פוספוליפידים יוצרים את הדו-שכבה.</li>"
                "<li><strong>איזון חומצה-בסיס</strong> &ndash; פוספט פועל כחוצץ.</li>"
                "</ul>"
                "<p>רמות הזרחן מווסתות על ידי הכליות, הורמון הפרתירואיד (PTH) וויטמין D. "
                "כשהמערכת מופרעת&mdash;לרוב בשל מחלת כליות&mdash;הרמות סוטות מהנורמה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי זרחן תקינים",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">מבוגרים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5&ndash;4.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.81&ndash;1.45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ילדים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4.0&ndash;7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.29&ndash;2.26</td></tr>'
                "</tbody></table>"
                "<p>לילדים רמות גבוהות יותר באופן טבעי בשל גדילה עצמית פעילה. הרמות משתנות במהלך היום ומושפעות מארוחות.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לזרחן גבוה ונמוך",
            body_html=(
                "<p><strong>זרחן גבוה (היפרפוספטמיה)</strong>:</p>"
                "<ul>"
                "<li><strong>מחלת כליות</strong> &ndash; הגורם השכיח ביותר. <a href=\"/he/blog/creatinine-egfr-kidney-function\">מדריך כליות</a>.</li>"
                "<li><strong>היפופרתירואידיזם</strong> &ndash; PTH נמוך מפחית את הפרשת הזרחן.</li>"
                "<li><strong>עודף ויטמין D</strong> &ndash; מגביר ספיגה מעיית.</li>"
                "<li><strong>חמצת קטונית סוכרתית</strong> &ndash; מעביר זרחן מהתאים לדם.</li>"
                "<li><strong>רבדומיוליזיס</strong> &ndash; פירוק שרירים מסיבי משחרר זרחן תוך-תאי.</li>"
                "</ul>"
                "<p><strong>זרחן נמוך (היפופוספטמיה)</strong>:</p>"
                "<ul>"
                "<li><strong>היפרפרתירואידיזם</strong> &ndash; עודף PTH גורם לאיבוד זרחן בשתן.</li>"
                "<li><strong>חוסר ויטמין D</strong> &ndash; מפחית ספיגה מעיית.</li>"
                "<li><strong>תת-תזונה ותסמונת האכלה מחדש</strong> &ndash; זרחן עובר במהירות לתאים.</li>"
                "<li><strong>שימוש כרוני בנוגדי חומצה</strong> &ndash; קושרים זרחן במעי.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של רמות זרחן חריגות",
            body_html=(
                "<p><strong>היפרפוספטמיה</strong> לעתים קרובות ללא תסמינים בשלב מוקדם. עם הזמן, זרחן גבוה יוצר משקעי סידן-פוספט "
                "ברקמות רכות וכלי דם: הסתיידות כלי דם, גרד, כאבי מפרקים ואוסטאודיסטרופיה כלייתית.</p>"
                "<p><strong>היפופוספטמיה</strong>:</p>"
                "<ul>"
                "<li><strong>קלה</strong> &ndash; לרוב ללא תסמינים.</li>"
                "<li><strong>בינונית</strong> &ndash; חולשת שרירים, כאבי עצמות, עייפות.</li>"
                "<li><strong>חמורה</strong> &ndash; בלבול, פרכוסים, אי-ספיקת נשימה, אנמיה המוליטית. זהו מצב חירום רפואי.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות קשורות",
            body_html=(
                "<ul>"
                "<li><strong>סידן</strong> &ndash; יחס הפוך עם זרחן. <a href=\"/he/blog/calcium-high-meaning\">מדריך סידן</a>.</li>"
                "<li><strong>PTH</strong> &ndash; מווסת סידן וזרחן.</li>"
                "<li><strong>ויטמין D</strong> &ndash; משפיע על ספיגת זרחן.</li>"
                "<li><strong>קריאטינין ו-eGFR</strong> &ndash; מעריך תפקוד כלייתי. <a href=\"/he/blog/creatinine-egfr-kidney-function\">מדריך כליות</a>.</li>"
                "<li><strong>פוספטאז אלקלי (ALP)</strong> &ndash; עולה במחלות עצמות.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא",
            body_html=(
                "<p>פנה לרופא אם הזרחן שלך מחוץ לטווח (מבוגרים: 2.5–4.5 mg/dL), יש לך מחלת כליות ידועה, "
                "אתה חווה כאבי עצמות, חולשת שרירים או גרד מתמשך, הסידן שלך גם חריג, "
                "או אתה מתאושש מתת-תזונה חמורה.</p>"
                "<p>הרופא שלך יזהה את הגורם, יתאים תרופות וייקבע בדיקות מעקב.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך NoryaAI עוזר לך עם תוצאות הזרחן",
            body_html=(
                "<p>NoryaAI מקל על הבנת תוצאות הזרחן ובדיקות הדם שלך. "
                "<a href=\"/analyze\">העלה את הדוח שלך</a>&mdash;PDF, תמונה או סריקה&mdash;ומנוע ה-AI:</p>"
                "<ul>"
                "<li>מחלץ את ערך הזרחן וכל הסמנים האחרים.</li>"
                "<li>משווה כל תוצאה לטווחי ייחוס לפי גיל ומין.</li>"
                "<li>מסמן ערכים חריגים עם הסברים ברורים.</li>"
                "<li>מדגיש קשרים (זרחן + סידן + PTH + ויטמין D).</li>"
                "<li>מייצר סיכום מובנה מוכן לרופא.</li>"
                "</ul>"
                "<p>גלה את <a href=\"/pricing\">תוכניות התמחור</a> שלנו.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הצהרה רפואית",
            body_html=(
                "<p><strong>מאמר זה למטרות מידע וחינוך בלבד. אינו מהווה ייעוץ רפואי, אבחון או טיפול. "
                "התייעץ תמיד עם איש מקצוע רפואי מוסמך. NoryaAI מספק ניתוח אוטומטי אך אינו מחליף שיקול דעת רפואי.</strong></p>"
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
            heading="फॉस्फोरस रक्त परीक्षण: आपके परिणाम का क्या मतलब है?",
            body_html=(
                "<p>फॉस्फोरस (फॉस्फेट) कैल्शियम के बाद मानव शरीर में सबसे प्रचुर मात्रा में पाया जाने वाला दूसरा खनिज है। "
                "यह हड्डियों के निर्माण, ऊर्जा चयापचय और कोशिका झिल्ली की संरचनात्मक अखंडता के लिए आवश्यक है। "
                "आपकी रक्त जाँच में फॉस्फोरस मान सीरम में अकार्बनिक फॉस्फेट को मापता है।</p>"
                "<p>असामान्य स्तर&mdash;उच्च (<strong>हाइपरफॉस्फेटीमिया</strong>) या कम (<strong>हाइपोफॉस्फेटीमिया</strong>)&mdash;"
                "गुर्दे की बीमारी, हार्मोनल असंतुलन या पोषण संबंधी कमियों का संकेत हो सकते हैं।</p>"
                "<p>यह लेख शैक्षिक है और चिकित्सा सलाह का विकल्प नहीं है।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="फॉस्फोरस क्या है और यह क्यों महत्वपूर्ण है?",
            body_html=(
                "<p><strong>फॉस्फोरस</strong> <a href=\"/hi/blog/calcium-high-meaning\">कैल्शियम</a> के साथ मिलकर मज़बूत हड्डियाँ "
                "और दाँत बनाता है। शरीर के फॉस्फोरस का लगभग 85% हड्डियों में होता है।</p>"
                "<p>फॉस्फोरस इन कार्यों में भी भूमिका निभाता है:</p>"
                "<ul>"
                "<li><strong>ऊर्जा उत्पादन</strong> &ndash; ATP का प्रमुख घटक।</li>"
                "<li><strong>DNA और RNA संरचना</strong> &ndash; न्यूक्लिक एसिड का कंकाल फॉस्फेट समूहों से बना है।</li>"
                "<li><strong>कोशिका झिल्ली अखंडता</strong> &ndash; फॉस्फोलिपिड दोहरी परत बनाते हैं।</li>"
                "<li><strong>अम्ल-क्षार संतुलन</strong> &ndash; फॉस्फेट बफ़र के रूप में कार्य करता है।</li>"
                "</ul>"
                "<p>फॉस्फोरस के स्तर को गुर्दे, PTH और विटामिन D द्वारा नियंत्रित किया जाता है। "
                "जब यह प्रणाली बाधित होती है&mdash;अक्सर गुर्दे की बीमारी से&mdash;स्तर सामान्य से विचलित हो जाते हैं।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य फॉस्फोरस स्तर",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5&ndash;4.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.81&ndash;1.45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">बच्चे</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4.0&ndash;7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.29&ndash;2.26</td></tr>'
                "</tbody></table>"
                "<p>सक्रिय हड्डी वृद्धि के कारण बच्चों में स्वाभाविक रूप से उच्च स्तर होते हैं। "
                "स्तर दिन भर में बदलते हैं और भोजन से प्रभावित होते हैं।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="उच्च और कम फॉस्फोरस के कारण",
            body_html=(
                "<p><strong>उच्च फॉस्फोरस (हाइपरफॉस्फेटीमिया)</strong>:</p>"
                "<ul>"
                "<li><strong>गुर्दे की बीमारी</strong> &ndash; सबसे आम कारण। <a href=\"/hi/blog/creatinine-egfr-kidney-function\">गुर्दा गाइड</a>.</li>"
                "<li><strong>हाइपोपैराथायरॉइडिज़्म</strong> &ndash; कम PTH गुर्दे द्वारा फॉस्फोरस उत्सर्जन को कम करता है।</li>"
                "<li><strong>अत्यधिक विटामिन D</strong> &ndash; आंतों से अवशोषण बढ़ाता है।</li>"
                "<li><strong>डायबिटिक कीटोएसिडोसिस</strong> &ndash; फॉस्फोरस को कोशिकाओं से रक्त में स्थानांतरित करता है।</li>"
                "<li><strong>रैबडोमायोलिसिस</strong> &ndash; बड़े पैमाने पर मांसपेशी टूटने से अंतःकोशिकीय फॉस्फोरस मुक्त होता है।</li>"
                "</ul>"
                "<p><strong>कम फॉस्फोरस (हाइपोफॉस्फेटीमिया)</strong>:</p>"
                "<ul>"
                "<li><strong>हाइपरपैराथायरॉइडिज़्म</strong> &ndash; अधिक PTH मूत्र में फॉस्फोरस हानि करता है।</li>"
                "<li><strong>विटामिन D की कमी</strong> &ndash; आंतों से अवशोषण कम करती है।</li>"
                "<li><strong>कुपोषण और रीफ़ीडिंग सिंड्रोम</strong> &ndash; फॉस्फोरस तेज़ी से कोशिकाओं में चला जाता है।</li>"
                "<li><strong>दीर्घकालिक एंटासिड उपयोग</strong> &ndash; आंत में फॉस्फोरस को बाँधते हैं।</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="असामान्य फॉस्फोरस स्तरों के लक्षण",
            body_html=(
                "<p><strong>हाइपरफॉस्फेटीमिया</strong> शुरू में अक्सर लक्षणहीन होती है। समय के साथ कैल्शियम-फॉस्फेट जमा "
                "नरम ऊतकों और रक्त वाहिकाओं में बनते हैं: संवहनी कैल्सीफिकेशन, खुजली, जोड़ों का दर्द, रीनल ऑस्टियोडिस्ट्रॉफी।</p>"
                "<p><strong>हाइपोफॉस्फेटीमिया</strong>:</p>"
                "<ul>"
                "<li><strong>हल्की</strong> &ndash; आमतौर पर कोई लक्षण नहीं।</li>"
                "<li><strong>मध्यम</strong> &ndash; मांसपेशियों में कमज़ोरी, हड्डी दर्द, थकान।</li>"
                "<li><strong>गंभीर</strong> &ndash; भ्रम, दौरे, श्वसन विफलता, हेमोलिटिक एनीमिया। यह चिकित्सा आपातकाल है।</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित परीक्षण",
            body_html=(
                "<ul>"
                "<li><strong>कैल्शियम</strong> &ndash; फॉस्फोरस से विपरीत संबंध। <a href=\"/hi/blog/calcium-high-meaning\">कैल्शियम गाइड</a>.</li>"
                "<li><strong>PTH</strong> &ndash; कैल्शियम और फॉस्फोरस को नियंत्रित करता है।</li>"
                "<li><strong>विटामिन D</strong> &ndash; फॉस्फोरस अवशोषण को प्रभावित करता है।</li>"
                "<li><strong>क्रिएटिनिन और eGFR</strong> &ndash; गुर्दा कार्य का मूल्यांकन। <a href=\"/hi/blog/creatinine-egfr-kidney-function\">गुर्दा गाइड</a>.</li>"
                "<li><strong>एल्कलाइन फॉस्फेटेज़ (ALP)</strong> &ndash; हड्डी रोगों में बढ़ सकता है।</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें",
            body_html=(
                "<p>डॉक्टर से मिलें यदि फॉस्फोरस सीमा से बाहर है (वयस्क: 2.5–4.5 mg/dL), आपको गुर्दे की बीमारी है, "
                "अस्पष्ट हड्डी दर्द, मांसपेशियों की कमज़ोरी या लगातार खुजली है, कैल्शियम भी असामान्य है, "
                "या आप गंभीर कुपोषण से ठीक हो रहे हैं।</p>"
                "<p>डॉक्टर कारण की पहचान करेंगे, दवाएँ समायोजित करेंगे और फ़ॉलो-अप परीक्षण करेंगे।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI आपके फॉस्फोरस परिणामों में कैसे मदद करता है",
            body_html=(
                "<p>NoryaAI आपके रक्त परीक्षण को समझना आसान बनाता है। "
                "<a href=\"/analyze\">अपनी रिपोर्ट अपलोड करें</a>&mdash;PDF, फ़ोटो या स्कैन&mdash;और हमारा AI:</p>"
                "<ul>"
                "<li>फॉस्फोरस और सभी बायोमार्कर निकालता है।</li>"
                "<li>प्रत्येक परिणाम की आयु और लिंग-विशिष्ट सीमाओं से तुलना करता है।</li>"
                "<li>असामान्य मानों को स्पष्ट व्याख्या के साथ चिह्नित करता है।</li>"
                "<li>संबंधित मार्करों (फॉस्फोरस + कैल्शियम + PTH + विटामिन D) के बीच संबंध दर्शाता है।</li>"
                "<li>डॉक्टर के लिए तैयार सारांश बनाता है।</li>"
                "</ul>"
                "<p>हमारी <a href=\"/pricing\">मूल्य निर्धारण योजनाएँ</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="चिकित्सा अस्वीकरण",
            body_html=(
                "<p><strong>यह लेख केवल सूचनात्मक और शैक्षिक उद्देश्यों के लिए है। यह चिकित्सा सलाह, निदान या उपचार नहीं है। "
                "हमेशा एक योग्य स्वास्थ्य पेशेवर से परामर्श करें। NoryaAI स्वचालित विश्लेषण प्रदान करता है लेकिन "
                "पेशेवर चिकित्सा निर्णय का विकल्प नहीं है।</strong></p>"
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
            heading="تحليل الفوسفور في الدم: ماذا تعني نتيجتك؟",
            body_html=(
                "<p>الفوسفور (الفوسفات) هو ثاني أكثر المعادن وفرة في جسم الإنسان بعد الكالسيوم. "
                "وهو ضروري لتكوين العظام والتمثيل الغذائي للطاقة وسلامة أغشية الخلايا. "
                "يقيس مستوى الفوسفور في تحليل الدم الفوسفات غير العضوي في المصل.</p>"
                "<p>مستويات غير طبيعية&mdash;مرتفعة (<strong>فرط فوسفات الدم</strong>) أو منخفضة (<strong>نقص فوسفات الدم</strong>)&mdash;"
                "قد تشير إلى مرض كلوي أو اختلال هرموني أو نقص غذائي.</p>"
                "<p>هذا المقال تثقيفي ولا يحل محل الاستشارة الطبية.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو الفوسفور ولماذا هو مهم؟",
            body_html=(
                "<p><strong>الفوسفور</strong> يعمل مع <a href=\"/ar/blog/calcium-high-meaning\">الكالسيوم</a> لبناء عظام وأسنان قوية. "
                "حوالي 85% من فوسفور الجسم موجود في العظام.</p>"
                "<p>يشارك الفوسفور أيضاً في:</p>"
                "<ul>"
                "<li><strong>إنتاج الطاقة</strong> &ndash; مكون رئيسي لـ ATP.</li>"
                "<li><strong>بنية DNA و RNA</strong> &ndash; هيكل الأحماض النووية مصنوع من مجموعات الفوسفات.</li>"
                "<li><strong>سلامة غشاء الخلية</strong> &ndash; الفوسفوليبيدات تشكل الطبقة المزدوجة.</li>"
                "<li><strong>التوازن الحمضي القاعدي</strong> &ndash; الفوسفات يعمل كمحلول منظم.</li>"
                "</ul>"
                "<p>يتم تنظيم مستويات الفوسفور بواسطة الكلى وهرمون الغدة الجار درقية (PTH) وفيتامين D. "
                "عند اضطراب هذا النظام&mdash;غالباً بسبب مرض الكلى&mdash;تنحرف المستويات عن المعدل الطبيعي.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدلات الطبيعية للفوسفور",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mmol/L</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">البالغون</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5&ndash;4.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.81&ndash;1.45</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الأطفال</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">4.0&ndash;7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.29&ndash;2.26</td></tr>'
                "</tbody></table>"
                "<p>الأطفال لديهم مستويات أعلى بشكل طبيعي بسبب نمو العظام النشط. "
                "المستويات تتقلب خلال اليوم وتتأثر بالوجبات.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب الفوسفور المرتفع والمنخفض",
            body_html=(
                "<p><strong>فوسفور مرتفع (فرط فوسفات الدم)</strong>:</p>"
                "<ul>"
                "<li><strong>مرض الكلى</strong> &ndash; السبب الأكثر شيوعاً. <a href=\"/ar/blog/creatinine-egfr-kidney-function\">دليل الكلى</a>.</li>"
                "<li><strong>قصور الغدة الجار درقية</strong> &ndash; PTH منخفض يقلل إفراز الفوسفور.</li>"
                "<li><strong>فائض فيتامين D</strong> &ndash; يزيد الامتصاص المعوي.</li>"
                "<li><strong>الحماض الكيتوني السكري</strong> &ndash; ينقل الفوسفور من الخلايا إلى الدم.</li>"
                "<li><strong>انحلال الربيدات</strong> &ndash; تحلل عضلي هائل يحرر الفوسفور داخل الخلايا.</li>"
                "</ul>"
                "<p><strong>فوسفور منخفض (نقص فوسفات الدم)</strong>:</p>"
                "<ul>"
                "<li><strong>فرط نشاط الغدة الجار درقية</strong> &ndash; فائض PTH يسبب فقدان بولي.</li>"
                "<li><strong>نقص فيتامين D</strong> &ndash; يقلل الامتصاص المعوي.</li>"
                "<li><strong>سوء التغذية ومتلازمة إعادة التغذية</strong> &ndash; الفوسفور ينتقل بسرعة إلى الخلايا.</li>"
                "<li><strong>استخدام مزمن لمضادات الحموضة</strong> &ndash; تربط الفوسفور في الأمعاء.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض مستويات الفوسفور غير الطبيعية",
            body_html=(
                "<p><strong>فرط فوسفات الدم</strong> غالباً بدون أعراض في البداية. مع الوقت تتشكل ترسبات كالسيوم-فوسفات "
                "في الأنسجة الرخوة والأوعية: تكلس وعائي، حكة، آلام مفصلية، حثل عظمي كلوي.</p>"
                "<p><strong>نقص فوسفات الدم</strong>:</p>"
                "<ul>"
                "<li><strong>خفيف</strong> &ndash; غالباً بدون أعراض.</li>"
                "<li><strong>متوسط</strong> &ndash; ضعف عضلي، ألم عظمي، إرهاق.</li>"
                "<li><strong>شديد</strong> &ndash; ارتباك، نوبات، فشل تنفسي، فقر دم انحلالي. هذه حالة طوارئ طبية.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="التحاليل المرتبطة",
            body_html=(
                "<ul>"
                "<li><strong>الكالسيوم</strong> &ndash; علاقة عكسية مع الفوسفور. <a href=\"/ar/blog/calcium-high-meaning\">دليل الكالسيوم</a>.</li>"
                "<li><strong>PTH</strong> &ndash; ينظم الكالسيوم والفوسفور.</li>"
                "<li><strong>فيتامين D</strong> &ndash; يؤثر على امتصاص الفوسفور.</li>"
                "<li><strong>الكرياتينين و eGFR</strong> &ndash; يقيّم وظائف الكلى. <a href=\"/ar/blog/creatinine-egfr-kidney-function\">دليل الكلى</a>.</li>"
                "<li><strong>الفوسفاتاز القلوي (ALP)</strong> &ndash; يرتفع في أمراض العظام.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب",
            body_html=(
                "<p>راجع طبيبك إذا كان الفوسفور خارج النطاق (بالغون: 2.5–4.5 mg/dL)، لديك مرض كلوي معروف، "
                "تعاني من آلام عظمية أو ضعف عضلي أو حكة مستمرة، الكالسيوم أيضاً غير طبيعي، "
                "أو أنت في مرحلة تعافٍ من سوء تغذية شديد.</p>"
                "<p>سيحدد طبيبك السبب ويعدّل العلاج ويطلب متابعة مخبرية.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يساعدك NoryaAI في فهم نتائج الفوسفور",
            body_html=(
                "<p>NoryaAI يسهّل فهم تحاليلك. <a href=\"/analyze\">ارفع تقريرك</a>&mdash;PDF أو صورة أو مسح ضوئي&mdash;ومحرك AI:</p>"
                "<ul>"
                "<li>يستخرج الفوسفور وجميع المؤشرات الحيوية.</li>"
                "<li>يقارن كل نتيجة بنطاقات مرجعية حسب العمر والجنس.</li>"
                "<li>يُبرز القيم غير الطبيعية مع شروحات واضحة.</li>"
                "<li>يُظهر الروابط (فوسفور + كالسيوم + PTH + فيتامين D).</li>"
                "<li>ينشئ ملخصاً منظماً جاهزاً للطبيب.</li>"
                "</ul>"
                "<p>اكتشف <a href=\"/pricing\">خطط الأسعار</a> لدينا.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية الطبية",
            body_html=(
                "<p><strong>هذا المقال لأغراض إعلامية وتثقيفية فقط. لا يشكّل نصيحة طبية أو تشخيصاً أو علاجاً. "
                "استشر دائماً مختصاً صحياً مؤهلاً. NoryaAI يوفر تحليلاً آلياً لكنه ليس بديلاً عن الحكم الطبي المهني.</strong></p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Aggregators
# ---------------------------------------------------------------------------
def get_phosphorus_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Phosphorus article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_phosphorus_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Phosphorus article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal phosphorus level?",
             "answer": "Normal phosphorus for adults is 2.5–4.5 mg/dL (0.81–1.45 mmol/L). Children have higher levels (4.0–7.0 mg/dL) due to active bone growth. Ranges may vary slightly between labs."},
            {"question": "What causes high phosphorus in blood?",
             "answer": "The most common cause is kidney disease, where the kidneys cannot excrete phosphorus efficiently. Other causes include hypoparathyroidism, excess vitamin D, diabetic ketoacidosis, and rhabdomyolysis."},
            {"question": "What are the symptoms of low phosphorus?",
             "answer": "Mild low phosphorus often has no symptoms. Moderate deficiency causes muscle weakness, bone pain, and fatigue. Severe hypophosphatemia can lead to confusion, seizures, respiratory failure, and is a medical emergency."},
            {"question": "How is phosphorus related to calcium?",
             "answer": "Phosphorus and calcium have an inverse relationship regulated by PTH and vitamin D. When phosphorus rises, calcium tends to fall, and vice versa. They work together for bone health and are usually tested together."},
        ],
        "tr": [
            {"question": "Normal fosfor seviyesi nedir?",
             "answer": "Yetişkinlerde normal fosfor 2,5–4,5 mg/dL (0,81–1,45 mmol/L) arasındadır. Çocuklarda aktif kemik büyümesi nedeniyle daha yüksektir (4,0–7,0 mg/dL)."},
            {"question": "Kanda yüksek fosforun nedenleri nelerdir?",
             "answer": "En yaygın neden böbrek hastalığıdır. Diğer nedenler arasında hipoparatiroidizm, aşırı D vitamini, diyabetik ketoasidoz ve rabdomiyoliz sayılabilir."},
            {"question": "Düşük fosforun belirtileri nelerdir?",
             "answer": "Hafif düşüklük genellikle belirtisizdir. Orta düzeyde kas güçsüzlüğü, kemik ağrısı ve yorgunluk olabilir. Şiddetli hipofosfatemi konfüzyon, nöbetler ve solunum yetmezliğine yol açabilir."},
            {"question": "Fosfor ve kalsiyum arasındaki ilişki nedir?",
             "answer": "Fosfor ve kalsiyum PTH ve D vitamini tarafından düzenlenen ters orantılı bir ilişkiye sahiptir. Biri yükseldiğinde diğeri düşme eğilimi gösterir. Kemik sağlığı için birlikte çalışırlar."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de fósforo?",
             "answer": "El fósforo normal en adultos es 2,5–4,5 mg/dL (0,81–1,45 mmol/L). Los niños tienen niveles más altos (4,0–7,0 mg/dL) por el crecimiento óseo activo."},
            {"question": "¿Qué causa el fósforo alto en sangre?",
             "answer": "La causa más común es la enfermedad renal. Otras causas incluyen hipoparatiroidismo, exceso de vitamina D, cetoacidosis diabética y rabdomiólisis."},
            {"question": "¿Cuáles son los síntomas del fósforo bajo?",
             "answer": "El fósforo bajo leve suele ser asintomático. El déficit moderado causa debilidad muscular, dolor óseo y fatiga. La hipofosfatemia grave puede causar confusión, convulsiones e insuficiencia respiratoria."},
            {"question": "¿Cuál es la relación entre fósforo y calcio?",
             "answer": "Fósforo y calcio tienen una relación inversa regulada por PTH y vitamina D. Cuando uno sube, el otro tiende a bajar. Ambos trabajan juntos para la salud ósea."},
        ],
        "de": [
            {"question": "Was ist ein normaler Phosphorwert?",
             "answer": "Normaler Phosphor bei Erwachsenen: 2,5–4,5 mg/dL (0,81–1,45 mmol/L). Kinder haben höhere Werte (4,0–7,0 mg/dL) wegen des aktiven Knochenwachstums."},
            {"question": "Was verursacht hohen Phosphor im Blut?",
             "answer": "Die häufigste Ursache ist Nierenerkrankung. Weitere Ursachen: Hypoparathyreoidismus, Vitamin-D-Überschuss, diabetische Ketoazidose und Rhabdomyolyse."},
            {"question": "Welche Symptome hat niedriger Phosphor?",
             "answer": "Leichter Mangel ist oft symptomlos. Mäßiger Mangel verursacht Muskelschwäche, Knochenschmerzen und Müdigkeit. Schwere Hypophosphatämie kann zu Verwirrtheit, Krämpfen und Atemversagen führen."},
            {"question": "Wie hängen Phosphor und Kalzium zusammen?",
             "answer": "Phosphor und Kalzium haben eine inverse Beziehung, reguliert durch PTH und Vitamin D. Wenn einer steigt, sinkt der andere tendenziell."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de phosphore ?",
             "answer": "Le phosphore normal chez l'adulte est de 2,5–4,5 mg/dL (0,81–1,45 mmol/L). Les enfants ont des taux plus élevés (4,0–7,0 mg/dL) en raison de la croissance osseuse."},
            {"question": "Quelles sont les causes d'un phosphore élevé ?",
             "answer": "La cause la plus fréquente est la maladie rénale. Autres causes : hypoparathyroïdie, excès de vitamine D, acidocétose diabétique et rhabdomyolyse."},
            {"question": "Quels sont les symptômes d'un phosphore bas ?",
             "answer": "Un déficit léger est souvent asymptomatique. Un déficit modéré cause faiblesse musculaire, douleurs osseuses et fatigue. L'hypophosphatémie sévère peut provoquer confusion, convulsions et insuffisance respiratoire."},
            {"question": "Quel est le lien entre phosphore et calcium ?",
             "answer": "Phosphore et calcium ont une relation inverse régulée par la PTH et la vitamine D. Quand l'un monte, l'autre tend à baisser."},
        ],
        "it": [
            {"question": "Qual è il livello normale di fosforo?",
             "answer": "Il fosforo normale negli adulti è 2,5–4,5 mg/dL (0,81–1,45 mmol/L). I bambini hanno livelli più alti (4,0–7,0 mg/dL) per la crescita ossea attiva."},
            {"question": "Cosa causa il fosforo alto nel sangue?",
             "answer": "La causa più comune è la malattia renale. Altre cause: ipoparatiroidismo, eccesso di vitamina D, chetoacidosi diabetica e rabdomiolisi."},
            {"question": "Quali sono i sintomi del fosforo basso?",
             "answer": "Il deficit lieve è spesso asintomatico. Quello moderato causa debolezza muscolare, dolore osseo e stanchezza. L'ipofosfatemia grave può causare confusione, convulsioni e insufficienza respiratoria."},
            {"question": "Qual è il rapporto tra fosforo e calcio?",
             "answer": "Fosforo e calcio hanno una relazione inversa regolata da PTH e vitamina D. Quando uno sale, l'altro tende a scendere."},
        ],
        "he": [
            {"question": "מהי רמת זרחן תקינה?",
             "answer": "זרחן תקין במבוגרים: 2.5–4.5 mg/dL (0.81–1.45 mmol/L). לילדים רמות גבוהות יותר (4.0–7.0 mg/dL) בשל גדילה עצמית פעילה."},
            {"question": "מה גורם לזרחן גבוה בדם?",
             "answer": "הגורם השכיח ביותר הוא מחלת כליות. גורמים נוספים: היפופרתירואידיזם, עודף ויטמין D, חמצת קטונית סוכרתית ורבדומיוליזיס."},
            {"question": "מהם התסמינים של זרחן נמוך?",
             "answer": "חסר קל הוא לעתים ללא תסמינים. חסר בינוני גורם חולשת שרירים, כאבי עצמות ועייפות. היפופוספטמיה חמורה עלולה לגרום לבלבול, פרכוסים ואי-ספיקת נשימה."},
            {"question": "מה הקשר בין זרחן לסידן?",
             "answer": "לזרחן וסידן יחס הפוך המווסת על ידי PTH וויטמין D. כשאחד עולה, השני נוטה לרדת. שניהם עובדים יחד לבריאות העצמות."},
        ],
        "hi": [
            {"question": "सामान्य फॉस्फोरस स्तर क्या है?",
             "answer": "वयस्कों में सामान्य फॉस्फोरस 2.5–4.5 mg/dL (0.81–1.45 mmol/L) है। सक्रिय हड्डी वृद्धि के कारण बच्चों में उच्च स्तर (4.0–7.0 mg/dL) होता है।"},
            {"question": "रक्त में उच्च फॉस्फोरस का कारण क्या है?",
             "answer": "सबसे आम कारण गुर्दे की बीमारी है। अन्य कारणों में हाइपोपैराथायरॉइडिज़्म, अत्यधिक विटामिन D, डायबिटिक कीटोएसिडोसिस और रैबडोमायोलिसिस शामिल हैं।"},
            {"question": "कम फॉस्फोरस के लक्षण क्या हैं?",
             "answer": "हल्की कमी अक्सर लक्षणहीन होती है। मध्यम कमी से मांसपेशियों में कमज़ोरी, हड्डी दर्द और थकान होती है। गंभीर हाइपोफॉस्फेटीमिया भ्रम, दौरे और श्वसन विफलता का कारण बन सकती है।"},
            {"question": "फॉस्फोरस और कैल्शियम के बीच क्या संबंध है?",
             "answer": "फॉस्फोरस और कैल्शियम का PTH और विटामिन D द्वारा विनियमित विपरीत संबंध है। जब एक बढ़ता है, दूसरा गिरने लगता है।"},
        ],
        "ar": [
            {"question": "ما هو المستوى الطبيعي للفوسفور؟",
             "answer": "الفوسفور الطبيعي للبالغين هو 2.5–4.5 mg/dL (0.81–1.45 mmol/L). الأطفال لديهم مستويات أعلى (4.0–7.0 mg/dL) بسبب النمو العظمي النشط."},
            {"question": "ما أسباب ارتفاع الفوسفور في الدم؟",
             "answer": "السبب الأكثر شيوعاً هو مرض الكلى. أسباب أخرى تشمل قصور الغدة الجار درقية وفائض فيتامين D والحماض الكيتوني السكري وانحلال الربيدات."},
            {"question": "ما أعراض انخفاض الفوسفور؟",
             "answer": "النقص الخفيف غالباً بدون أعراض. النقص المتوسط يسبب ضعف عضلي وألم عظمي وإرهاق. نقص الفوسفات الشديد قد يسبب ارتباك ونوبات وفشل تنفسي."},
            {"question": "ما العلاقة بين الفوسفور والكالسيوم؟",
             "answer": "الفوسفور والكالسيوم لهما علاقة عكسية ينظمها PTH وفيتامين D. عندما يرتفع أحدهما يميل الآخر للانخفاض."},
        ],
    }
