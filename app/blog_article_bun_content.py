# -*- coding: utf-8 -*-
"""
BUN (Blood Urea Nitrogen) blog article — full body content for all 9 languages.
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
            heading="BUN (Kan Üre Azotu) testi: Sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızda <strong>BUN (Blood Urea Nitrogen — Kan Üre Azotu)</strong> "
                "değerinin normalden yüksek ya da düşük çıkması böbrek fonksiyonları hakkında önemli "
                "ipuçları verebilir. BUN, vücutta protein metabolizması sonucu karaciğerde üretilen "
                "üre azotunun kandaki miktarını ölçen yaygın bir biyokimyasal testtir.</p>"
                "<p>Bu rehber, BUN testinin ne anlama geldiğini, sonuçlarınızı nasıl "
                "yorumlayabileceğinizi ve doktor görüşmenize nasıl hazırlanacağınızı anlatmaktadır. "
                "Amacımız teşhis koymak değil — sizi doktor randevunuza daha bilinçli "
                "hazırlamaktır. BUN değerinizi tek başına değerlendirmek yerine "
                "<em>kreatinin</em>, <em>eGFR</em> ve <em>BUN/Kreatinin oranı</em> gibi "
                "ilişkili değerlerle birlikte ele almak çok önemlidir.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="BUN (Kan Üre Azotu) nedir?",
            body_html=(
                "<p><strong>BUN (Blood Urea Nitrogen)</strong>, kandaki üre azotu miktarını ölçen "
                "bir testtir. Proteinler sindirildiğinde aminoasitlere ayrılır ve bu aminoasitlerin "
                "metabolizması sonucu amonyak oluşur. Amonyak, karaciğerde <em>üre döngüsü</em> "
                "yoluyla daha az toksik olan üreye dönüştürülür.</p>"
                "<p>Üre kana karışır ve böbrekler tarafından süzülerek idrarla atılır. BUN testi, "
                "bu sürecin ne kadar etkili çalıştığını değerlendirmek için kullanılır. Sonuçlar "
                "genellikle <strong>mg/dL</strong> biriminde raporlanır. BUN, böbrek fonksiyonlarının "
                "temel göstergelerinden biridir ancak tek başına böbrek hastalığı tanısı koymak "
                "için yeterli değildir.</p>"
                "<p>BUN testi, rutin kan panellerinin (metabolik panel) bir parçası olarak sıklıkla "
                "istenir. Dehidrasyon, yüksek proteinli diyet ve bazı ilaçlar gibi böbrek dışı "
                "faktörler de BUN düzeyini etkileyebilir.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN ve böbrek fonksiyonu ilişkisi",
            body_html=(
                "<p>Böbrekler, kanı süzerek atık maddeleri uzaklaştıran ve sıvı-elektrolit dengesini "
                "koruyan hayati organlardır. Üre, böbreklerin süzme kapasitesinin en önemli "
                "göstergelerinden biridir. Böbrek fonksiyonları azaldığında üre yeterince "
                "süzülemez ve kanda birikir — bu durum <strong>azotemi</strong> olarak adlandırılır.</p>"
                "<p>BUN düzeyi yalnızca böbrek fonksiyonlarına değil, aynı zamanda protein alımına, "
                "karaciğer fonksiyonuna ve hidrasyon durumuna da bağlıdır. Bu nedenle BUN, böbrek "
                "hastalığının taranmasında tek başına yeterli bir belirteç değildir; <em>kreatinin</em> "
                "ve <em>eGFR</em> ile birlikte değerlendirilmelidir.</p>"
                "<p>Akut böbrek hasarı, kronik böbrek hastalığı ve böbrek yetmezliği gibi durumlarda "
                "BUN belirgin şekilde yükselir. Ancak prerenal (böbrek öncesi), renal (böbrek kaynaklı) "
                "ve postrenal (böbrek sonrası) nedenlerin ayırt edilmesi için ek testler gereklidir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="BUN normal değerleri ve referans aralıkları",
            body_html=(
                "<p>Aşağıdaki tablo, BUN ve ilişkili böbrek fonksiyon parametreleri için genel kabul "
                "gören referans aralıklarını özetlemektedir. Laboratuvarlar arasında küçük "
                "farklılıklar olabilir; sonuçlarınızı her zaman kendi laboratuvarınızın referans "
                "aralığıyla karşılaştırın.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parametre</th>'
                f'<th {_TH}>Referans Aralığı</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>Kreatinin</td><td {_TD}>0,6–1,2 mg/dL (erkek) / 0,5–1,1 mg/dL (kadın)</td></tr>'
                f'<tr><td {_TD}>BUN/Kreatinin Oranı</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>eGFR</td><td {_TD}>&gt;60 mL/min/1,73m² (normal)</td></tr>'
                "</tbody></table>"
                "<p>Tek bir yüksek veya düşük değer her zaman hastalık anlamına gelmez. "
                "Dehidrasyon, beslenme alışkanlıkları ve kullanılan ilaçlar sonuçları "
                "etkileyebilir. Hekiminiz klinik tablonuzla birlikte değerlendirecektir.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="Yüksek BUN (azotemi) nedenleri",
            body_html=(
                "<p><strong>Yüksek BUN</strong> (azotemi), böbrek fonksiyon bozukluğunun en sık "
                "göstergelerinden biridir ancak pek çok farklı neden bu duruma yol açabilir:</p>"
                "<ul>"
                "<li><strong>Böbrek hastalığı/yetmezliği</strong> — akut veya kronik böbrek "
                "hasarında üre atılımı azalır</li>"
                "<li><strong>Dehidrasyon</strong> — sıvı kaybı kanı yoğunlaştırır ve BUN'u "
                "orantısız şekilde yükseltir</li>"
                "<li><strong>Yüksek proteinli diyet</strong> — aşırı protein alımı üre üretimini "
                "artırır</li>"
                "<li><strong>Kalp yetmezliği</strong> — böbreklere giden kan akımı azalır (prerenal)</li>"
                "<li><strong>Üst GI kanaması</strong> — sindirilen kan proteini üre üretimini artırır</li>"
                "<li><strong>Yanıklar ve şok</strong> — doku yıkımı ve kan hacmi kaybı</li>"
                "<li><strong>İlaçlar</strong> — kortikosteroidler, tetrasiklinler</li>"
                "<li><strong>Üriner sistem obstrüksiyonu</strong> — idrar yolu tıkanıklığı (postrenal)</li>"
                "</ul>"
                "<p>Prerenal, renal ve postrenal nedenler arasında ayrım yapmak tedavi stratejisi "
                "açısından kritik öneme sahiptir. Hekiminiz <em>BUN/Kreatinin oranı</em>, "
                "idrar tetkikleri ve görüntüleme yöntemleriyle altta yatan nedeni belirleyecektir.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="Düşük BUN nedenleri",
            body_html=(
                "<p><strong>Düşük BUN</strong> daha az sık görülür ancak bazı önemli durumların "
                "habercisi olabilir:</p>"
                "<ul>"
                "<li><strong>Karaciğer hastalığı/yetmezliği</strong> — üre sentezi azalır çünkü "
                "üre döngüsü karaciğerde gerçekleşir</li>"
                "<li><strong>Yetersiz beslenme / düşük proteinli diyet</strong> — substrat azlığı "
                "üre üretimini düşürür</li>"
                "<li><strong>Aşırı hidrasyon</strong> — kanın seyrelmesi (hemodilüsyon)</li>"
                "<li><strong>Gebelik</strong> — artan kan hacmi ve hemodilüsyon BUN düzeyini "
                "düşürebilir</li>"
                "<li><strong>Çölyak hastalığı</strong> — protein emiliminin bozulması</li>"
                "<li><strong>SIADH</strong> — uygunsuz ADH salınımı sıvı tutulumuna yol açar</li>"
                "</ul>"
                "<p>Düşük BUN genellikle tek başına acil bir durum işaret etmez; ancak altta yatan "
                "nedeni anlamak için ek değerlendirme yapılmalıdır. Özellikle karaciğer hastalığı "
                "şüphesinde ALT, AST ve albümin gibi testler de istenebilir.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="BUN/Kreatinin oranı ne anlama gelir?",
            body_html=(
                "<p><strong>BUN/Kreatinin oranı</strong>, yüksek BUN'un nedenini belirlemeye "
                "yardımcı olan önemli bir klinik göstergedir. Normal oran genellikle "
                "<strong>10:1 ile 20:1</strong> arasındadır.</p>"
                "<p><strong>Yüksek oran (&gt;20:1)</strong> — genellikle prerenal nedenlere işaret "
                "eder: dehidrasyon, kalp yetmezliği, üst GI kanaması. Bu durumlarda BUN kreatininden "
                "orantısız olarak daha fazla yükselir çünkü böbrekler üreyi geri emer ancak "
                "kreatinini geri emilmez.</p>"
                "<p><strong>Düşük oran (&lt;10:1)</strong> — karaciğer hastalığı, yetersiz beslenme "
                "veya rabdomiyoliz gibi durumları düşündürür. Karaciğer hastalığında üre üretimi "
                "azalırken kreatinin düzeyi nispeten korunabilir.</p>"
                "<p>Bu oran, hekimlerin prerenal, renal ve postrenal nedenleri birbirinden "
                "ayırt etmesine yardımcı olan pratik bir araçtır. Klinik değerlendirmenin "
                "önemli bir parçasıdır.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="Dehidrasyonun BUN üzerindeki etkisi",
            body_html=(
                "<p><strong>Dehidrasyon</strong>, BUN düzeyini yükselten en yaygın böbrek dışı "
                "nedenlerden biridir. Vücut yeterli sıvı alamadığında kan yoğunlaşır ve böbreklerin "
                "süzme kapasitesi azalır. Bu durumda üre geri emilimi artar ve BUN düzeyi "
                "orantısız şekilde yükselir.</p>"
                "<p>Dehidrasyona bağlı BUN yüksekliğinde <em>kreatinin</em> düzeyi genellikle "
                "normal veya hafif yüksek kalır. Bu nedenle <strong>BUN/Kreatinin oranı "
                "20:1'in üzerine</strong> çıkar — bu da prerenal bir nedeni düşündüren önemli "
                "bir ipucudur.</p>"
                "<p>Yeterli sıvı alımından sonra BUN düzeyinin normale dönmesi, yüksekliğin "
                "dehidrasyona bağlı olduğunu doğrulayan önemli bir klinik bulgudur. Uzun süreli "
                "veya tekrarlayan dehidrasyon ise böbreklere zarar verebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda BUN sonuçlarınızı bir sağlık uzmanıyla değerlendirmeniz "
                "önerilir:</p>"
                "<ul>"
                "<li>BUN değeriniz referans aralığının üstünde veya altındaysa</li>"
                "<li>Sürekli yorgunluk, halsizlik veya iştahsızlık yaşıyorsanız</li>"
                "<li>Ayak bileklerinde veya yüzde <strong>ödem</strong> (şişlik) fark ediyorsanız</li>"
                "<li>İdrar miktarında, renginde veya sıklığında değişiklikler varsa</li>"
                "<li>Bulantı, kusma veya nefes darlığı gibi belirtiler eşlik ediyorsa</li>"
                "</ul>"
                "<p>Bu belirtiler böbrek fonksiyon bozukluğunun ya da diğer sistemik hastalıkların "
                "işareti olabilir. Erken tanı ve müdahale, özellikle böbrek hastalıklarında, "
                "hastalığın ilerlemesini yavaşlatmak açısından büyük önem taşır.</p>"
                "<p>Kan tahlili sonuçlarınızı hekiminizle paylaşmadan önce bir ön değerlendirme "
                "yapmak, sorularınızı netleştirmenize ve randevunuzu daha verimli geçirmenize "
                "yardımcı olabilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya ile BUN sonuçlarınızı anlayın",
            body_html=(
                "<p>Kan tahlili sonuçlarınızı anlamak karmaşık olabilir. <strong>Norya</strong>, "
                "laboratuvar raporunuzu yüklemenize ve dakikalar içinde yapılandırılmış, anlaşılır "
                "bir sağlık özeti almanıza olanak tanır. BUN, kreatinin ve diğer böbrek "
                "belirteçleriniz net bir şekilde açıklanır.</p>"
                "<p>Hemen <a href=\"/analyze\">kan tahlilinizi yükleyin</a> ve doktor randevunuza "
                "daha hazırlıklı gidin. Fiyatlandırma bilgileri için "
                "<a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine '
                'geçmez.</strong> Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. '
                '<a href="/analyze">Norya ile analiz başlat</a></p>'
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
            heading="BUN (Blood Urea Nitrogen) test: What your results mean",
            body_html=(
                "<p>If your blood test results show an abnormal <strong>BUN (Blood Urea Nitrogen)</strong> "
                "level, it may indicate important clues about your kidney function and overall health. "
                "BUN measures the amount of urea nitrogen in your blood — a waste product formed when "
                "the liver breaks down protein.</p>"
                "<p>This guide explains what the BUN test measures, how to interpret your results, and "
                "how to prepare for your doctor's appointment. Our goal is not to diagnose — it's to "
                "help you arrive at your consultation more informed. It's essential to evaluate your "
                "BUN alongside related markers like <em>creatinine</em>, <em>eGFR</em>, and the "
                "<em>BUN/creatinine ratio</em> for a complete picture.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="What is BUN (Blood Urea Nitrogen)?",
            body_html=(
                "<p><strong>BUN (Blood Urea Nitrogen)</strong> is a blood test that measures the "
                "amount of urea nitrogen in your bloodstream. When your body digests protein, it "
                "produces ammonia as a byproduct. The liver converts this ammonia into urea through "
                "the <em>urea cycle</em>, a less toxic compound that enters the bloodstream.</p>"
                "<p>The kidneys then filter urea out of the blood and excrete it in urine. The BUN "
                "test evaluates how effectively this process is working. Results are typically "
                "reported in <strong>mg/dL</strong> (milligrams per deciliter). While BUN is one "
                "of the most commonly ordered kidney function markers, it is not specific to the "
                "kidneys alone.</p>"
                "<p>BUN is routinely included in basic and comprehensive metabolic panels. Factors "
                "beyond kidney function — such as dehydration, high-protein diets, and certain "
                "medications — can also influence BUN levels significantly.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN and kidney function",
            body_html=(
                "<p>The kidneys are vital organs that filter waste products from the blood, maintain "
                "fluid and electrolyte balance, and regulate blood pressure. Urea is one of the key "
                "waste products the kidneys remove. When kidney function declines, urea accumulates "
                "in the blood — a condition known as <strong>azotemia</strong>.</p>"
                "<p>However, BUN levels are influenced by more than just kidney function. Protein "
                "intake, liver function, hydration status, and tissue breakdown all affect BUN. "
                "This is why BUN alone is not sufficient for diagnosing kidney disease; it must be "
                "interpreted alongside <em>creatinine</em> and <em>eGFR</em> for clinical accuracy.</p>"
                "<p>In conditions like acute kidney injury (AKI), chronic kidney disease (CKD), and "
                "end-stage renal disease (ESRD), BUN rises significantly. Differentiating between "
                "prerenal, renal, and postrenal causes requires additional laboratory and imaging "
                "studies.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="BUN normal ranges and reference values",
            body_html=(
                "<p>The following table summarizes generally accepted reference ranges for BUN and "
                "related kidney function parameters. Slight variations may exist between laboratories; "
                "always compare your results against your own lab's reference range.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parameter</th>'
                f'<th {_TH}>Reference Range</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>Creatinine</td><td {_TD}>0.6–1.2 mg/dL (men) / 0.5–1.1 mg/dL (women)</td></tr>'
                f'<tr><td {_TD}>BUN/Creatinine Ratio</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>eGFR</td><td {_TD}>&gt;60 mL/min/1.73m² (normal)</td></tr>'
                "</tbody></table>"
                "<p>A single abnormal value does not always indicate disease. Dehydration, dietary "
                "habits, and medications can affect results. Your physician will interpret findings "
                "in the context of your overall clinical picture.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="High BUN (azotemia) causes",
            body_html=(
                "<p><strong>Elevated BUN</strong> (azotemia) is one of the most common indicators of "
                "impaired kidney function, but numerous other conditions can also raise BUN levels:</p>"
                "<ul>"
                "<li><strong>Kidney disease/failure</strong> — acute or chronic kidney damage reduces "
                "urea excretion</li>"
                "<li><strong>Dehydration</strong> — fluid loss concentrates the blood and raises BUN "
                "disproportionately</li>"
                "<li><strong>High-protein diet</strong> — excess protein intake increases urea "
                "production</li>"
                "<li><strong>Heart failure</strong> — reduced blood flow to the kidneys (prerenal)</li>"
                "<li><strong>Upper GI bleeding</strong> — digested blood protein increases urea "
                "production</li>"
                "<li><strong>Burns and shock</strong> — tissue breakdown and blood volume loss</li>"
                "<li><strong>Medications</strong> — corticosteroids, tetracyclines</li>"
                "<li><strong>Urinary tract obstruction</strong> — blockage (postrenal cause)</li>"
                "</ul>"
                "<p>Distinguishing between prerenal, renal, and postrenal causes is critical for "
                "guiding treatment. Your doctor will use the <em>BUN/creatinine ratio</em>, urinalysis, "
                "and imaging studies to identify the underlying cause.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="Low BUN causes",
            body_html=(
                "<p><strong>Low BUN</strong> is less common than elevated BUN but can signal several "
                "important conditions:</p>"
                "<ul>"
                "<li><strong>Liver disease/failure</strong> — reduced urea synthesis because the "
                "urea cycle occurs in the liver</li>"
                "<li><strong>Malnutrition / low-protein diet</strong> — insufficient substrate for "
                "urea production</li>"
                "<li><strong>Overhydration</strong> — dilution of the blood (hemodilution)</li>"
                "<li><strong>Pregnancy</strong> — increased blood volume and hemodilution can "
                "lower BUN</li>"
                "<li><strong>Celiac disease</strong> — impaired protein absorption</li>"
                "<li><strong>SIADH</strong> — syndrome of inappropriate ADH secretion causes fluid "
                "retention</li>"
                "</ul>"
                "<p>Low BUN alone rarely signals an emergency, but identifying the underlying cause "
                "is important. When liver disease is suspected, additional tests such as ALT, AST, "
                "and albumin may be ordered.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="What does the BUN/Creatinine ratio mean?",
            body_html=(
                "<p>The <strong>BUN/Creatinine ratio</strong> is a valuable clinical tool that helps "
                "determine the cause of elevated BUN. The normal ratio is generally between "
                "<strong>10:1 and 20:1</strong>.</p>"
                "<p><strong>High ratio (&gt;20:1)</strong> — typically points to prerenal causes: "
                "dehydration, heart failure, or upper GI bleeding. In these situations, BUN rises "
                "disproportionately to creatinine because the kidneys reabsorb urea but not "
                "creatinine when blood flow is reduced.</p>"
                "<p><strong>Low ratio (&lt;10:1)</strong> — may suggest liver disease, malnutrition, "
                "or rhabdomyolysis. In liver disease, urea production decreases while creatinine "
                "levels remain relatively stable.</p>"
                "<p>This ratio is a practical tool that helps clinicians differentiate between "
                "prerenal, renal, and postrenal causes of azotemia. It is an integral part of the "
                "clinical evaluation when BUN is abnormal.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="How dehydration affects BUN levels",
            body_html=(
                "<p><strong>Dehydration</strong> is one of the most common non-renal causes of "
                "elevated BUN. When the body doesn't receive enough fluids, blood becomes more "
                "concentrated and the kidneys' filtering capacity decreases. This leads to increased "
                "urea reabsorption and a disproportionate rise in BUN.</p>"
                "<p>In dehydration-related BUN elevation, <em>creatinine</em> levels typically remain "
                "normal or only mildly elevated. Consequently, the <strong>BUN/creatinine ratio "
                "exceeds 20:1</strong> — a key indicator suggesting a prerenal cause rather than "
                "intrinsic kidney disease.</p>"
                "<p>BUN returning to normal after adequate rehydration is an important clinical "
                "confirmation that the elevation was dehydration-related. However, prolonged or "
                "recurrent dehydration can cause lasting kidney damage over time.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>You should discuss your BUN results with a healthcare professional if any of the "
                "following apply:</p>"
                "<ul>"
                "<li>Your BUN level is above or below the reference range</li>"
                "<li>You experience persistent fatigue, weakness, or loss of appetite</li>"
                "<li>You notice <strong>edema</strong> (swelling) in your ankles, feet, or face</li>"
                "<li>There are changes in urination frequency, volume, or color</li>"
                "<li>Symptoms such as nausea, vomiting, or shortness of breath are present</li>"
                "</ul>"
                "<p>These symptoms may indicate kidney dysfunction or other systemic conditions. "
                "Early detection and intervention — especially for kidney disease — are crucial for "
                "slowing disease progression and preserving kidney function.</p>"
                "<p>Reviewing your blood test results before your appointment can help you clarify "
                "questions and make your consultation more productive.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Understand your BUN results with Norya",
            body_html=(
                "<p>Understanding your blood test results can be complex. <strong>Norya</strong> lets "
                "you upload your lab report and receive a structured, easy-to-understand health "
                "summary within minutes. Your BUN, creatinine, and other kidney markers are clearly "
                "explained in plain language.</p>"
                "<p>Upload your blood test now at <a href=\"/analyze\">our analysis page</a> and "
                "arrive at your doctor's appointment better prepared. Visit our "
                "<a href=\"/pricing\">pricing page</a> for plan details.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace '
                'medical advice or diagnosis.</strong> Always discuss your results with a healthcare '
                'professional. <a href="/analyze">Start analysis with Norya</a></p>'
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
            heading="Prueba de BUN (nitrógeno ureico en sangre): ¿Qué significan sus resultados?",
            body_html=(
                "<p>Si sus resultados de análisis de sangre muestran un nivel anormal de "
                "<strong>BUN (Blood Urea Nitrogen — nitrógeno ureico en sangre)</strong>, puede "
                "ser un indicador importante de su función renal y salud general. El BUN mide "
                "la cantidad de nitrógeno ureico en la sangre, un producto de desecho generado "
                "cuando el hígado metaboliza las proteínas.</p>"
                "<p>Esta guía explica qué mide la prueba de BUN, cómo interpretar sus resultados "
                "y cómo prepararse para su consulta médica. Nuestro objetivo no es diagnosticar, "
                "sino ayudarle a llegar a su cita médica mejor informado. Es fundamental evaluar "
                "el BUN junto con marcadores relacionados como la <em>creatinina</em>, la "
                "<em>TFGe</em> y la <em>relación BUN/creatinina</em>.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="¿Qué es el BUN (nitrógeno ureico en sangre)?",
            body_html=(
                "<p>El <strong>BUN</strong> es un análisis de sangre que mide la cantidad de "
                "nitrógeno ureico en el torrente sanguíneo. Cuando el cuerpo digiere proteínas, "
                "se produce amoníaco como subproducto. El hígado convierte este amoníaco en urea "
                "a través del <em>ciclo de la urea</em>, un compuesto menos tóxico que pasa a la "
                "sangre.</p>"
                "<p>Los riñones filtran la urea de la sangre y la excretan en la orina. La prueba "
                "de BUN evalúa la eficacia de este proceso. Los resultados se expresan generalmente "
                "en <strong>mg/dL</strong>. El BUN es uno de los marcadores renales más solicitados, "
                "pero no es específico exclusivamente de los riñones.</p>"
                "<p>El BUN se incluye de forma rutinaria en los paneles metabólicos. Factores como "
                "la deshidratación, las dietas ricas en proteínas y ciertos medicamentos también "
                "pueden influir significativamente en los niveles de BUN.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN y función renal",
            body_html=(
                "<p>Los riñones son órganos vitales que filtran los productos de desecho de la "
                "sangre, mantienen el equilibrio de líquidos y electrolitos, y regulan la presión "
                "arterial. La urea es uno de los principales desechos que eliminan los riñones. "
                "Cuando la función renal disminuye, la urea se acumula en la sangre — una "
                "condición conocida como <strong>azotemia</strong>.</p>"
                "<p>Sin embargo, los niveles de BUN no solo dependen de la función renal. La "
                "ingesta de proteínas, la función hepática, el estado de hidratación y la "
                "destrucción tisular también afectan el BUN. Por eso, el BUN por sí solo no es "
                "suficiente para diagnosticar enfermedad renal; debe interpretarse junto con la "
                "<em>creatinina</em> y la <em>TFGe</em>.</p>"
                "<p>En condiciones como la lesión renal aguda (LRA), la enfermedad renal crónica "
                "(ERC) y la insuficiencia renal terminal, el BUN se eleva significativamente. "
                "Diferenciar entre causas prerrenales, renales y postrrenales requiere estudios "
                "adicionales.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de BUN y rangos de referencia",
            body_html=(
                "<p>La siguiente tabla resume los rangos de referencia generalmente aceptados para "
                "el BUN y los parámetros de función renal relacionados. Pueden existir ligeras "
                "variaciones entre laboratorios; compare siempre sus resultados con el rango de "
                "referencia de su propio laboratorio.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parámetro</th>'
                f'<th {_TH}>Rango de Referencia</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>Creatinina</td><td {_TD}>0,6–1,2 mg/dL (hombres) / 0,5–1,1 mg/dL (mujeres)</td></tr>'
                f'<tr><td {_TD}>Relación BUN/Creatinina</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>TFGe</td><td {_TD}>&gt;60 mL/min/1,73m² (normal)</td></tr>'
                "</tbody></table>"
                "<p>Un valor anormal aislado no siempre indica enfermedad. La deshidratación, "
                "los hábitos alimentarios y los medicamentos pueden afectar los resultados. Su "
                "médico los interpretará en el contexto de su cuadro clínico completo.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="Causas de BUN alto (azotemia)",
            body_html=(
                "<p>El <strong>BUN elevado</strong> (azotemia) es uno de los indicadores más comunes "
                "de disfunción renal, pero numerosas condiciones pueden elevar los niveles:</p>"
                "<ul>"
                "<li><strong>Enfermedad/insuficiencia renal</strong> — el daño renal agudo o crónico "
                "reduce la excreción de urea</li>"
                "<li><strong>Deshidratación</strong> — la pérdida de líquidos concentra la sangre y "
                "eleva el BUN desproporcionadamente</li>"
                "<li><strong>Dieta hiperproteica</strong> — el exceso de proteínas aumenta la "
                "producción de urea</li>"
                "<li><strong>Insuficiencia cardíaca</strong> — reducción del flujo sanguíneo a los "
                "riñones (prerrenal)</li>"
                "<li><strong>Hemorragia GI alta</strong> — la sangre digerida incrementa la "
                "producción de urea</li>"
                "<li><strong>Quemaduras y shock</strong> — destrucción tisular y pérdida de volumen</li>"
                "<li><strong>Medicamentos</strong> — corticosteroides, tetraciclinas</li>"
                "<li><strong>Obstrucción del tracto urinario</strong> — bloqueo (causa postrrenal)</li>"
                "</ul>"
                "<p>Distinguir entre causas prerrenales, renales y postrrenales es fundamental para "
                "orientar el tratamiento. Su médico utilizará la <em>relación BUN/creatinina</em>, "
                "el análisis de orina y estudios de imagen para identificar la causa subyacente.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="Causas de BUN bajo",
            body_html=(
                "<p>El <strong>BUN bajo</strong> es menos frecuente que el BUN elevado, pero puede "
                "señalar condiciones importantes:</p>"
                "<ul>"
                "<li><strong>Enfermedad/insuficiencia hepática</strong> — síntesis reducida de urea "
                "ya que el ciclo de la urea ocurre en el hígado</li>"
                "<li><strong>Desnutrición / dieta baja en proteínas</strong> — sustrato insuficiente "
                "para la producción de urea</li>"
                "<li><strong>Sobrehidratación</strong> — dilución de la sangre (hemodilución)</li>"
                "<li><strong>Embarazo</strong> — el aumento del volumen sanguíneo y la hemodilución "
                "pueden reducir el BUN</li>"
                "<li><strong>Enfermedad celíaca</strong> — absorción deficiente de proteínas</li>"
                "<li><strong>SIADH</strong> — la secreción inadecuada de ADH causa retención "
                "de líquidos</li>"
                "</ul>"
                "<p>El BUN bajo por sí solo rara vez indica una emergencia, pero es importante "
                "identificar la causa subyacente. Cuando se sospecha enfermedad hepática, se pueden "
                "solicitar pruebas adicionales como ALT, AST y albúmina.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="¿Qué significa la relación BUN/Creatinina?",
            body_html=(
                "<p>La <strong>relación BUN/Creatinina</strong> es una herramienta clínica valiosa "
                "que ayuda a determinar la causa del BUN elevado. La relación normal generalmente "
                "se encuentra entre <strong>10:1 y 20:1</strong>.</p>"
                "<p><strong>Relación alta (&gt;20:1)</strong> — generalmente indica causas "
                "prerrenales: deshidratación, insuficiencia cardíaca o hemorragia GI alta. En estas "
                "situaciones, el BUN se eleva desproporcionadamente respecto a la creatinina porque "
                "los riñones reabsorben urea pero no creatinina cuando el flujo sanguíneo disminuye.</p>"
                "<p><strong>Relación baja (&lt;10:1)</strong> — puede sugerir enfermedad hepática, "
                "desnutrición o rabdomiólisis. En la enfermedad hepática, la producción de urea "
                "disminuye mientras que los niveles de creatinina se mantienen relativamente estables.</p>"
                "<p>Esta relación es una herramienta práctica que ayuda a los médicos a diferenciar "
                "entre causas prerrenales, renales y postrrenales de azotemia.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="Efecto de la deshidratación en los niveles de BUN",
            body_html=(
                "<p>La <strong>deshidratación</strong> es una de las causas no renales más comunes "
                "de BUN elevado. Cuando el cuerpo no recibe suficientes líquidos, la sangre se "
                "concentra y la capacidad de filtración de los riñones disminuye, lo que provoca "
                "un aumento desproporcionado en la reabsorción de urea y en el BUN.</p>"
                "<p>En la elevación de BUN por deshidratación, los niveles de <em>creatinina</em> "
                "suelen permanecer normales o solo ligeramente elevados. En consecuencia, la "
                "<strong>relación BUN/creatinina supera 20:1</strong> — un indicador clave que "
                "sugiere una causa prerrenal en lugar de enfermedad renal intrínseca.</p>"
                "<p>La normalización del BUN tras una rehidratación adecuada es una confirmación "
                "clínica importante de que la elevación estaba relacionada con la deshidratación. "
                "Sin embargo, la deshidratación prolongada o recurrente puede causar daño renal "
                "permanente a largo plazo.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar a un médico?",
            body_html=(
                "<p>Debe comentar sus resultados de BUN con un profesional de salud si se aplica "
                "alguna de las siguientes situaciones:</p>"
                "<ul>"
                "<li>Su nivel de BUN está por encima o por debajo del rango de referencia</li>"
                "<li>Experimenta fatiga persistente, debilidad o pérdida de apetito</li>"
                "<li>Nota <strong>edema</strong> (hinchazón) en tobillos, pies o cara</li>"
                "<li>Hay cambios en la frecuencia, volumen o color de la orina</li>"
                "<li>Presenta síntomas como náuseas, vómitos o dificultad para respirar</li>"
                "</ul>"
                "<p>Estos síntomas pueden indicar disfunción renal u otras condiciones sistémicas. "
                "La detección e intervención temprana — especialmente en enfermedad renal — son "
                "cruciales para frenar la progresión de la enfermedad.</p>"
                "<p>Revisar sus resultados de análisis antes de su cita puede ayudarle a aclarar "
                "dudas y hacer su consulta más productiva.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Entienda sus resultados de BUN con Norya",
            body_html=(
                "<p>Comprender sus resultados de análisis de sangre puede ser complejo. "
                "<strong>Norya</strong> le permite subir su informe de laboratorio y recibir un "
                "resumen de salud estructurado y fácil de entender en minutos. Su BUN, creatinina "
                "y otros marcadores renales se explican claramente.</p>"
                "<p>Suba su análisis ahora en <a href=\"/analyze\">nuestra página de análisis</a> "
                "y llegue a su cita médica mejor preparado. Visite nuestra "
                "<a href=\"/pricing\">página de precios</a> para más información.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico '
                'médico.</strong> Consulte siempre sus resultados con un profesional sanitario. '
                '<a href="/analyze">Iniciar análisis con Norya</a></p>'
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
            heading="BUN (Blut-Harnstoff-Stickstoff) Test: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Wenn Ihr Bluttest einen abweichenden <strong>BUN (Blood Urea Nitrogen — "
                "Blut-Harnstoff-Stickstoff)</strong>-Wert zeigt, kann dies wichtige Hinweise auf "
                "Ihre Nierenfunktion und Ihre allgemeine Gesundheit geben. BUN misst die Menge "
                "an Harnstoff-Stickstoff im Blut — ein Abfallprodukt, das entsteht, wenn die "
                "Leber Protein abbaut.</p>"
                "<p>Dieser Leitfaden erklärt, was der BUN-Test misst, wie Sie Ihre Ergebnisse "
                "interpretieren können und wie Sie sich auf Ihren Arzttermin vorbereiten. Unser "
                "Ziel ist keine Diagnose — sondern Sie besser informiert in Ihr Arztgespräch "
                "gehen zu lassen. Es ist wichtig, den BUN zusammen mit verwandten Markern wie "
                "<em>Kreatinin</em>, <em>eGFR</em> und dem <em>BUN/Kreatinin-Verhältnis</em> "
                "zu bewerten.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="Was ist BUN (Blut-Harnstoff-Stickstoff)?",
            body_html=(
                "<p><strong>BUN</strong> ist ein Bluttest, der die Menge an Harnstoff-Stickstoff "
                "im Blut misst. Wenn Ihr Körper Proteine verdaut, entsteht Ammoniak als "
                "Nebenprodukt. Die Leber wandelt dieses Ammoniak über den <em>Harnstoffzyklus</em> "
                "in Harnstoff um — eine weniger toxische Verbindung, die ins Blut gelangt.</p>"
                "<p>Die Nieren filtern Harnstoff aus dem Blut und scheiden ihn mit dem Urin aus. "
                "Der BUN-Test bewertet, wie effektiv dieser Prozess funktioniert. Die Ergebnisse "
                "werden in <strong>mg/dL</strong> angegeben. Obwohl BUN einer der am häufigsten "
                "angeforderten Nierenfunktionsmarker ist, ist er nicht ausschließlich "
                "nierenspezifisch.</p>"
                "<p>BUN wird routinemäßig im Rahmen von Stoffwechselpanels bestimmt. Faktoren "
                "wie Dehydration, proteinreiche Ernährung und bestimmte Medikamente können die "
                "BUN-Werte erheblich beeinflussen.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN und Nierenfunktion",
            body_html=(
                "<p>Die Nieren sind lebenswichtige Organe, die Abfallprodukte aus dem Blut filtern, "
                "den Flüssigkeits- und Elektrolythaushalt aufrechterhalten und den Blutdruck "
                "regulieren. Harnstoff ist eines der wichtigsten Abfallprodukte, die die Nieren "
                "entfernen. Bei nachlassender Nierenfunktion reichert sich Harnstoff im Blut an "
                "— ein Zustand, der als <strong>Azotämie</strong> bezeichnet wird.</p>"
                "<p>Allerdings werden BUN-Werte nicht nur von der Nierenfunktion beeinflusst. "
                "Proteinaufnahme, Leberfunktion, Hydratationsstatus und Gewebeabbau wirken sich "
                "ebenfalls auf den BUN aus. Deshalb reicht BUN allein nicht für die Diagnose von "
                "Nierenerkrankungen aus — er muss zusammen mit <em>Kreatinin</em> und <em>eGFR</em> "
                "interpretiert werden.</p>"
                "<p>Bei Erkrankungen wie akuter Nierenschädigung (AKI), chronischer "
                "Nierenerkrankung (CKD) und terminaler Niereninsuffizienz steigt der BUN deutlich "
                "an. Die Unterscheidung zwischen prärenalen, renalen und postrenalen Ursachen "
                "erfordert zusätzliche Labor- und Bildgebungsuntersuchungen.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="BUN-Normalwerte und Referenzbereiche",
            body_html=(
                "<p>Die folgende Tabelle fasst die allgemein anerkannten Referenzbereiche für BUN "
                "und verwandte Nierenfunktionsparameter zusammen. Zwischen Laboren können leichte "
                "Abweichungen bestehen; vergleichen Sie Ihre Ergebnisse immer mit dem "
                "Referenzbereich Ihres eigenen Labors.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parameter</th>'
                f'<th {_TH}>Referenzbereich</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>Kreatinin</td><td {_TD}>0,6–1,2 mg/dL (Männer) / 0,5–1,1 mg/dL (Frauen)</td></tr>'
                f'<tr><td {_TD}>BUN/Kreatinin-Verhältnis</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>eGFR</td><td {_TD}>&gt;60 mL/min/1,73m² (normal)</td></tr>'
                "</tbody></table>"
                "<p>Ein einzelner abweichender Wert bedeutet nicht immer eine Erkrankung. "
                "Dehydration, Ernährungsgewohnheiten und Medikamente können die Ergebnisse "
                "beeinflussen. Ihr Arzt wird die Befunde im Kontext Ihres gesamten klinischen "
                "Bildes interpretieren.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="Ursachen für hohen BUN (Azotämie)",
            body_html=(
                "<p><strong>Erhöhter BUN</strong> (Azotämie) ist einer der häufigsten Indikatoren "
                "für eine eingeschränkte Nierenfunktion, aber auch zahlreiche andere Zustände "
                "können den BUN erhöhen:</p>"
                "<ul>"
                "<li><strong>Nierenerkrankung/-insuffizienz</strong> — akute oder chronische "
                "Nierenschäden verringern die Harnstoffausscheidung</li>"
                "<li><strong>Dehydration</strong> — Flüssigkeitsverlust konzentriert das Blut und "
                "erhöht den BUN überproportional</li>"
                "<li><strong>Proteinreiche Ernährung</strong> — übermäßige Proteinaufnahme steigert "
                "die Harnstoffproduktion</li>"
                "<li><strong>Herzinsuffizienz</strong> — reduzierter Blutfluss zu den Nieren "
                "(prärenal)</li>"
                "<li><strong>Obere GI-Blutung</strong> — verdautes Blutprotein erhöht die "
                "Harnstoffproduktion</li>"
                "<li><strong>Verbrennungen und Schock</strong> — Gewebezerfall und "
                "Blutvolumenverlust</li>"
                "<li><strong>Medikamente</strong> — Kortikosteroide, Tetracycline</li>"
                "<li><strong>Harnwegsobstruktion</strong> — Verstopfung (postrenale Ursache)</li>"
                "</ul>"
                "<p>Die Unterscheidung zwischen prärenalen, renalen und postrenalen Ursachen ist "
                "für die Therapieplanung entscheidend. Ihr Arzt wird das "
                "<em>BUN/Kreatinin-Verhältnis</em>, Urinanalysen und Bildgebung zur Klärung "
                "der Ursache einsetzen.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="Ursachen für niedrigen BUN",
            body_html=(
                "<p><strong>Niedriger BUN</strong> kommt seltener vor als erhöhter BUN, kann aber "
                "auf wichtige Zustände hinweisen:</p>"
                "<ul>"
                "<li><strong>Lebererkrankung/-insuffizienz</strong> — verminderte Harnstoffsynthese, "
                "da der Harnstoffzyklus in der Leber stattfindet</li>"
                "<li><strong>Mangelernährung / proteinarme Diät</strong> — unzureichendes Substrat "
                "für die Harnstoffproduktion</li>"
                "<li><strong>Überhydratation</strong> — Verdünnung des Blutes (Hämodilution)</li>"
                "<li><strong>Schwangerschaft</strong> — erhöhtes Blutvolumen und Hämodilution "
                "können den BUN senken</li>"
                "<li><strong>Zöliakie</strong> — gestörte Proteinabsorption</li>"
                "<li><strong>SIADH</strong> — Syndrom der inadäquaten ADH-Sekretion führt zu "
                "Flüssigkeitsretention</li>"
                "</ul>"
                "<p>Ein niedriger BUN allein signalisiert selten einen Notfall, aber die "
                "Identifizierung der zugrunde liegenden Ursache ist wichtig. Bei Verdacht auf "
                "Lebererkrankung können zusätzliche Tests wie ALT, AST und Albumin angeordnet "
                "werden.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="Was bedeutet das BUN/Kreatinin-Verhältnis?",
            body_html=(
                "<p>Das <strong>BUN/Kreatinin-Verhältnis</strong> ist ein wertvolles klinisches "
                "Werkzeug, das hilft, die Ursache eines erhöhten BUN zu bestimmen. Das normale "
                "Verhältnis liegt in der Regel zwischen <strong>10:1 und 20:1</strong>.</p>"
                "<p><strong>Hohes Verhältnis (&gt;20:1)</strong> — deutet typischerweise auf "
                "prärenale Ursachen hin: Dehydration, Herzinsuffizienz oder obere GI-Blutung. "
                "In diesen Situationen steigt der BUN überproportional zum Kreatinin, da die "
                "Nieren bei reduziertem Blutfluss Harnstoff rückresorbieren, Kreatinin jedoch "
                "nicht.</p>"
                "<p><strong>Niedriges Verhältnis (&lt;10:1)</strong> — kann auf Lebererkrankung, "
                "Mangelernährung oder Rhabdomyolyse hindeuten. Bei Lebererkrankung nimmt die "
                "Harnstoffproduktion ab, während die Kreatininwerte relativ stabil bleiben.</p>"
                "<p>Dieses Verhältnis ist ein praktisches Werkzeug, das Klinikern hilft, zwischen "
                "prärenalen, renalen und postrenalen Ursachen der Azotämie zu differenzieren.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="Auswirkung von Dehydration auf den BUN-Wert",
            body_html=(
                "<p><strong>Dehydration</strong> ist eine der häufigsten nicht-renalen Ursachen "
                "für erhöhten BUN. Wenn der Körper nicht genügend Flüssigkeit erhält, konzentriert "
                "sich das Blut und die Filterleistung der Nieren nimmt ab. Dies führt zu einer "
                "verstärkten Harnstoffrückresorption und einem überproportionalen BUN-Anstieg.</p>"
                "<p>Bei dehydrationsbedingter BUN-Erhöhung bleiben die <em>Kreatininwerte</em> "
                "typischerweise normal oder nur leicht erhöht. Folglich übersteigt das "
                "<strong>BUN/Kreatinin-Verhältnis 20:1</strong> — ein wichtiger Hinweis auf eine "
                "prärenale Ursache statt einer intrinsischen Nierenerkrankung.</p>"
                "<p>Die Normalisierung des BUN nach ausreichender Rehydratation ist eine wichtige "
                "klinische Bestätigung, dass die Erhöhung dehydrationsbedingt war. Langfristige "
                "oder wiederkehrende Dehydration kann jedoch zu dauerhaften Nierenschäden führen.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Sie sollten Ihre BUN-Ergebnisse mit einem Arzt besprechen, wenn einer der "
                "folgenden Punkte zutrifft:</p>"
                "<ul>"
                "<li>Ihr BUN-Wert liegt über oder unter dem Referenzbereich</li>"
                "<li>Sie leiden unter anhaltender Müdigkeit, Schwäche oder Appetitlosigkeit</li>"
                "<li>Sie bemerken <strong>Ödeme</strong> (Schwellungen) an Knöcheln, Füßen oder "
                "im Gesicht</li>"
                "<li>Es gibt Veränderungen bei Häufigkeit, Menge oder Farbe des Urins</li>"
                "<li>Symptome wie Übelkeit, Erbrechen oder Atemnot bestehen</li>"
                "</ul>"
                "<p>Diese Symptome können auf eine Nierenfunktionsstörung oder andere systemische "
                "Erkrankungen hinweisen. Früherkennung und Intervention — insbesondere bei "
                "Nierenerkrankungen — sind entscheidend, um das Fortschreiten der Krankheit zu "
                "verlangsamen.</p>"
                "<p>Die Überprüfung Ihrer Blutergebnisse vor Ihrem Termin kann helfen, Fragen zu "
                "klären und Ihre Konsultation produktiver zu gestalten.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Verstehen Sie Ihre BUN-Ergebnisse mit Norya",
            body_html=(
                "<p>Das Verstehen Ihrer Bluttestergebnisse kann komplex sein. <strong>Norya</strong> "
                "ermöglicht es Ihnen, Ihren Laborbericht hochzuladen und innerhalb von Minuten eine "
                "strukturierte, leicht verständliche Gesundheitszusammenfassung zu erhalten. Ihr "
                "BUN, Kreatinin und andere Nierenmarker werden in klarer Sprache erklärt.</p>"
                "<p>Laden Sie Ihren Bluttest jetzt auf <a href=\"/analyze\">unserer Analyseseite</a> "
                "hoch und gehen Sie besser vorbereitet zu Ihrem Arzttermin. Besuchen Sie unsere "
                "<a href=\"/pricing\">Preisseite</a> für Plandetails.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche '
                'Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem '
                'Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'
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
            heading="Test BUN (azote uréique sanguin) : que signifient vos résultats ?",
            body_html=(
                "<p>Si vos résultats d'analyse sanguine montrent un taux anormal de "
                "<strong>BUN (Blood Urea Nitrogen — azote uréique sanguin)</strong>, cela peut "
                "fournir des indices importants sur votre fonction rénale et votre santé globale. "
                "Le BUN mesure la quantité d'azote uréique dans le sang — un déchet produit "
                "lorsque le foie métabolise les protéines.</p>"
                "<p>Ce guide explique ce que mesure le test BUN, comment interpréter vos résultats "
                "et comment vous préparer à votre rendez-vous médical. Notre objectif n'est pas "
                "de diagnostiquer — mais de vous aider à arriver mieux informé à votre "
                "consultation. Il est essentiel d'évaluer le BUN avec des marqueurs associés comme "
                "la <em>créatinine</em>, le <em>DFGe</em> et le <em>rapport BUN/créatinine</em>.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="Qu'est-ce que le BUN (azote uréique sanguin) ?",
            body_html=(
                "<p>Le <strong>BUN</strong> est une analyse de sang qui mesure la quantité d'azote "
                "uréique dans le sang. Lorsque votre corps digère les protéines, de l'ammoniac "
                "est produit comme sous-produit. Le foie convertit cet ammoniac en urée via le "
                "<em>cycle de l'urée</em> — un composé moins toxique qui passe dans le sang.</p>"
                "<p>Les reins filtrent ensuite l'urée du sang et l'éliminent dans l'urine. Le test "
                "BUN évalue l'efficacité de ce processus. Les résultats sont généralement "
                "exprimés en <strong>mg/dL</strong>. Bien que le BUN soit l'un des marqueurs "
                "rénaux les plus couramment demandés, il n'est pas spécifique aux reins.</p>"
                "<p>Le BUN est inclus de routine dans les bilans métaboliques. Des facteurs comme "
                "la déshydratation, un régime riche en protéines et certains médicaments peuvent "
                "influencer significativement les taux de BUN.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN et fonction rénale",
            body_html=(
                "<p>Les reins sont des organes vitaux qui filtrent les déchets du sang, "
                "maintiennent l'équilibre hydro-électrolytique et régulent la pression artérielle. "
                "L'urée est l'un des principaux déchets éliminés par les reins. Lorsque la "
                "fonction rénale décline, l'urée s'accumule dans le sang — un état connu sous le "
                "nom d'<strong>azotémie</strong>.</p>"
                "<p>Cependant, les taux de BUN ne dépendent pas uniquement de la fonction rénale. "
                "L'apport protéique, la fonction hépatique, l'état d'hydratation et la "
                "destruction tissulaire influencent également le BUN. C'est pourquoi le BUN seul "
                "ne suffit pas pour diagnostiquer une maladie rénale ; il doit être interprété "
                "avec la <em>créatinine</em> et le <em>DFGe</em>.</p>"
                "<p>Dans des pathologies comme l'insuffisance rénale aiguë (IRA), la maladie "
                "rénale chronique (MRC) et l'insuffisance rénale terminale, le BUN augmente "
                "considérablement. La distinction entre causes prérénales, rénales et postrénales "
                "nécessite des examens complémentaires.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales du BUN et intervalles de référence",
            body_html=(
                "<p>Le tableau suivant résume les intervalles de référence généralement acceptés "
                "pour le BUN et les paramètres de fonction rénale associés. De légères variations "
                "peuvent exister entre les laboratoires ; comparez toujours vos résultats avec "
                "l'intervalle de référence de votre propre laboratoire.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Paramètre</th>'
                f'<th {_TH}>Intervalle de Référence</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>Créatinine</td><td {_TD}>0,6–1,2 mg/dL (hommes) / 0,5–1,1 mg/dL (femmes)</td></tr>'
                f'<tr><td {_TD}>Rapport BUN/Créatinine</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>DFGe</td><td {_TD}>&gt;60 mL/min/1,73m² (normal)</td></tr>'
                "</tbody></table>"
                "<p>Une seule valeur anormale ne signifie pas toujours une maladie. La "
                "déshydratation, les habitudes alimentaires et les médicaments peuvent affecter "
                "les résultats. Votre médecin interprétera les résultats dans le contexte de "
                "votre tableau clinique global.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="Causes d'un BUN élevé (azotémie)",
            body_html=(
                "<p>Un <strong>BUN élevé</strong> (azotémie) est l'un des indicateurs les plus "
                "courants d'altération de la fonction rénale, mais de nombreuses autres conditions "
                "peuvent aussi élever le BUN :</p>"
                "<ul>"
                "<li><strong>Maladie/insuffisance rénale</strong> — les lésions rénales aiguës ou "
                "chroniques réduisent l'excrétion d'urée</li>"
                "<li><strong>Déshydratation</strong> — la perte de liquides concentre le sang et "
                "élève le BUN de façon disproportionnée</li>"
                "<li><strong>Régime hyperprotéiné</strong> — un apport excessif en protéines "
                "augmente la production d'urée</li>"
                "<li><strong>Insuffisance cardiaque</strong> — flux sanguin réduit vers les reins "
                "(prérénale)</li>"
                "<li><strong>Hémorragie GI haute</strong> — le sang digéré augmente la production "
                "d'urée</li>"
                "<li><strong>Brûlures et choc</strong> — destruction tissulaire et perte de volume</li>"
                "<li><strong>Médicaments</strong> — corticostéroïdes, tétracyclines</li>"
                "<li><strong>Obstruction des voies urinaires</strong> — blocage (cause postrénale)</li>"
                "</ul>"
                "<p>La distinction entre causes prérénales, rénales et postrénales est essentielle "
                "pour orienter le traitement. Votre médecin utilisera le <em>rapport "
                "BUN/créatinine</em>, l'analyse d'urine et l'imagerie pour identifier la cause.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="Causes d'un BUN bas",
            body_html=(
                "<p>Un <strong>BUN bas</strong> est moins fréquent qu'un BUN élevé mais peut "
                "signaler des conditions importantes :</p>"
                "<ul>"
                "<li><strong>Maladie/insuffisance hépatique</strong> — synthèse réduite d'urée "
                "car le cycle de l'urée se déroule dans le foie</li>"
                "<li><strong>Malnutrition / régime pauvre en protéines</strong> — substrat "
                "insuffisant pour la production d'urée</li>"
                "<li><strong>Surhydratation</strong> — dilution du sang (hémodilution)</li>"
                "<li><strong>Grossesse</strong> — l'augmentation du volume sanguin et "
                "l'hémodilution peuvent abaisser le BUN</li>"
                "<li><strong>Maladie cœliaque</strong> — absorption déficiente des protéines</li>"
                "<li><strong>SIADH</strong> — la sécrétion inadéquate d'ADH provoque une "
                "rétention hydrique</li>"
                "</ul>"
                "<p>Un BUN bas seul indique rarement une urgence, mais l'identification de la "
                "cause sous-jacente est importante. En cas de suspicion de maladie hépatique, "
                "des tests supplémentaires comme ALAT, ASAT et albumine peuvent être demandés.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="Que signifie le rapport BUN/Créatinine ?",
            body_html=(
                "<p>Le <strong>rapport BUN/Créatinine</strong> est un outil clinique précieux qui "
                "aide à déterminer la cause d'un BUN élevé. Le rapport normal est généralement "
                "compris entre <strong>10:1 et 20:1</strong>.</p>"
                "<p><strong>Rapport élevé (&gt;20:1)</strong> — indique typiquement des causes "
                "prérénales : déshydratation, insuffisance cardiaque ou hémorragie GI haute. "
                "Dans ces situations, le BUN augmente de façon disproportionnée par rapport à la "
                "créatinine car les reins réabsorbent l'urée mais pas la créatinine lorsque le "
                "débit sanguin est réduit.</p>"
                "<p><strong>Rapport bas (&lt;10:1)</strong> — peut suggérer une maladie hépatique, "
                "une malnutrition ou une rhabdomyolyse. Dans la maladie hépatique, la production "
                "d'urée diminue tandis que les taux de créatinine restent relativement stables.</p>"
                "<p>Ce rapport est un outil pratique qui aide les cliniciens à différencier les "
                "causes prérénales, rénales et postrénales d'azotémie.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="Effet de la déshydratation sur les taux de BUN",
            body_html=(
                "<p>La <strong>déshydratation</strong> est l'une des causes non rénales les plus "
                "courantes de BUN élevé. Lorsque l'organisme ne reçoit pas suffisamment de "
                "liquides, le sang se concentre et la capacité de filtration des reins diminue, "
                "entraînant une réabsorption accrue de l'urée et une élévation disproportionnée "
                "du BUN.</p>"
                "<p>Lors d'une élévation du BUN liée à la déshydratation, les taux de "
                "<em>créatinine</em> restent généralement normaux ou seulement légèrement élevés. "
                "En conséquence, le <strong>rapport BUN/créatinine dépasse 20:1</strong> — un "
                "indicateur clé suggérant une cause prérénale plutôt qu'une maladie rénale "
                "intrinsèque.</p>"
                "<p>Le retour du BUN à la normale après une réhydratation adéquate est une "
                "confirmation clinique importante que l'élévation était liée à la déshydratation. "
                "Cependant, une déshydratation prolongée ou récurrente peut causer des dommages "
                "rénaux permanents.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand devez-vous consulter un médecin ?",
            body_html=(
                "<p>Vous devriez discuter de vos résultats de BUN avec un professionnel de santé "
                "si l'une des situations suivantes s'applique :</p>"
                "<ul>"
                "<li>Votre taux de BUN est au-dessus ou en dessous de l'intervalle de référence</li>"
                "<li>Vous éprouvez une fatigue persistante, une faiblesse ou une perte d'appétit</li>"
                "<li>Vous remarquez un <strong>œdème</strong> (gonflement) aux chevilles, pieds ou "
                "au visage</li>"
                "<li>Il y a des changements dans la fréquence, le volume ou la couleur des urines</li>"
                "<li>Des symptômes comme nausées, vomissements ou essoufflement sont présents</li>"
                "</ul>"
                "<p>Ces symptômes peuvent indiquer une dysfonction rénale ou d'autres pathologies "
                "systémiques. La détection et l'intervention précoces — en particulier pour les "
                "maladies rénales — sont cruciales pour ralentir la progression de la maladie.</p>"
                "<p>Revoir vos résultats d'analyses avant votre rendez-vous peut vous aider à "
                "clarifier vos questions et rendre votre consultation plus productive.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comprenez vos résultats de BUN avec Norya",
            body_html=(
                "<p>Comprendre vos résultats d'analyses sanguines peut être complexe. "
                "<strong>Norya</strong> vous permet de télécharger votre rapport de laboratoire et "
                "de recevoir un résumé de santé structuré et facile à comprendre en quelques "
                "minutes. Votre BUN, créatinine et autres marqueurs rénaux sont clairement "
                "expliqués.</p>"
                "<p>Téléchargez votre analyse maintenant sur "
                "<a href=\"/analyze\">notre page d'analyse</a> et arrivez mieux préparé à votre "
                "rendez-vous médical. Consultez notre <a href=\"/pricing\">page de tarifs</a> "
                "pour les détails.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas '
                'un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats '
                'avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec '
                'Norya</a></p>'
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
            heading="Test BUN (azoto ureico nel sangue): cosa significano i tuoi risultati",
            body_html=(
                "<p>Se i risultati delle tue analisi del sangue mostrano un valore anomalo di "
                "<strong>BUN (Blood Urea Nitrogen — azoto ureico nel sangue)</strong>, ciò può "
                "fornire indizi importanti sulla tua funzione renale e sulla salute generale. "
                "Il BUN misura la quantità di azoto ureico nel sangue — un prodotto di scarto "
                "generato quando il fegato metabolizza le proteine.</p>"
                "<p>Questa guida spiega cosa misura il test BUN, come interpretare i risultati "
                "e come prepararsi alla visita medica. Il nostro obiettivo non è formulare una "
                "diagnosi — ma aiutarti ad arrivare alla tua consulta più informato. È essenziale "
                "valutare il BUN insieme a marcatori correlati come la <em>creatinina</em>, "
                "l'<em>eGFR</em> e il <em>rapporto BUN/creatinina</em>.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="Cos'è il BUN (azoto ureico nel sangue)?",
            body_html=(
                "<p>Il <strong>BUN</strong> è un esame del sangue che misura la quantità di azoto "
                "ureico nel circolo sanguigno. Quando il corpo digerisce le proteine, produce "
                "ammoniaca come sottoprodotto. Il fegato converte questa ammoniaca in urea "
                "attraverso il <em>ciclo dell'urea</em> — un composto meno tossico che entra "
                "nel sangue.</p>"
                "<p>I reni filtrano poi l'urea dal sangue e la eliminano con le urine. Il test "
                "BUN valuta l'efficacia di questo processo. I risultati sono generalmente espressi "
                "in <strong>mg/dL</strong>. Sebbene il BUN sia uno dei marcatori di funzione "
                "renale più richiesti, non è specifico esclusivamente dei reni.</p>"
                "<p>Il BUN è incluso di routine nei pannelli metabolici. Fattori come la "
                "disidratazione, le diete iperproteiche e alcuni farmaci possono influenzare "
                "significativamente i livelli di BUN.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN e funzione renale",
            body_html=(
                "<p>I reni sono organi vitali che filtrano i prodotti di scarto dal sangue, "
                "mantengono l'equilibrio idro-elettrolitico e regolano la pressione arteriosa. "
                "L'urea è uno dei principali prodotti di scarto rimossi dai reni. Quando la "
                "funzione renale declina, l'urea si accumula nel sangue — una condizione nota "
                "come <strong>azotemia</strong>.</p>"
                "<p>Tuttavia, i livelli di BUN sono influenzati da più fattori oltre alla "
                "funzione renale. L'assunzione di proteine, la funzione epatica, lo stato di "
                "idratazione e la distruzione tissutale incidono tutti sul BUN. Per questo il "
                "BUN da solo non è sufficiente per diagnosticare una malattia renale; deve essere "
                "interpretato insieme a <em>creatinina</em> ed <em>eGFR</em>.</p>"
                "<p>In condizioni come il danno renale acuto (AKI), la malattia renale cronica "
                "(CKD) e l'insufficienza renale terminale, il BUN aumenta significativamente. "
                "La differenziazione tra cause prerenali, renali e postrenali richiede esami "
                "aggiuntivi.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del BUN e intervalli di riferimento",
            body_html=(
                "<p>La tabella seguente riassume gli intervalli di riferimento generalmente "
                "accettati per il BUN e i parametri di funzione renale correlati. Possono "
                "esistere lievi variazioni tra i laboratori; confronta sempre i tuoi risultati "
                "con l'intervallo di riferimento del tuo laboratorio.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>Parametro</th>'
                f'<th {_TH}>Intervallo di Riferimento</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>Creatinina</td><td {_TD}>0,6–1,2 mg/dL (uomini) / 0,5–1,1 mg/dL (donne)</td></tr>'
                f'<tr><td {_TD}>Rapporto BUN/Creatinina</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>eGFR</td><td {_TD}>&gt;60 mL/min/1,73m² (normale)</td></tr>'
                "</tbody></table>"
                "<p>Un singolo valore anomalo non significa sempre malattia. La disidratazione, "
                "le abitudini alimentari e i farmaci possono influenzare i risultati. Il tuo "
                "medico interpreterà i risultati nel contesto del tuo quadro clinico complessivo.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="Cause di BUN alto (azotemia)",
            body_html=(
                "<p>Il <strong>BUN elevato</strong> (azotemia) è uno degli indicatori più comuni "
                "di funzione renale compromessa, ma numerose altre condizioni possono alzare i "
                "livelli di BUN:</p>"
                "<ul>"
                "<li><strong>Malattia/insufficienza renale</strong> — il danno renale acuto o "
                "cronico riduce l'escrezione di urea</li>"
                "<li><strong>Disidratazione</strong> — la perdita di liquidi concentra il sangue "
                "e alza il BUN in modo sproporzionato</li>"
                "<li><strong>Dieta iperproteica</strong> — un eccesso di proteine aumenta la "
                "produzione di urea</li>"
                "<li><strong>Insufficienza cardiaca</strong> — flusso sanguigno ridotto ai reni "
                "(prerenale)</li>"
                "<li><strong>Emorragia GI alta</strong> — il sangue digerito aumenta la produzione "
                "di urea</li>"
                "<li><strong>Ustioni e shock</strong> — distruzione tissutale e perdita di volume</li>"
                "<li><strong>Farmaci</strong> — corticosteroidi, tetracicline</li>"
                "<li><strong>Ostruzione delle vie urinarie</strong> — blocco (causa postrenale)</li>"
                "</ul>"
                "<p>Distinguere tra cause prerenali, renali e postrenali è fondamentale per "
                "guidare il trattamento. Il medico utilizzerà il <em>rapporto BUN/creatinina</em>, "
                "l'esame delle urine e l'imaging per identificare la causa.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="Cause di BUN basso",
            body_html=(
                "<p>Il <strong>BUN basso</strong> è meno frequente del BUN elevato ma può "
                "segnalare condizioni importanti:</p>"
                "<ul>"
                "<li><strong>Malattia/insufficienza epatica</strong> — sintesi ridotta di urea "
                "poiché il ciclo dell'urea avviene nel fegato</li>"
                "<li><strong>Malnutrizione / dieta ipoproteica</strong> — substrato insufficiente "
                "per la produzione di urea</li>"
                "<li><strong>Iperidratazione</strong> — diluizione del sangue (emodiluizione)</li>"
                "<li><strong>Gravidanza</strong> — l'aumento del volume ematico e l'emodiluizione "
                "possono abbassare il BUN</li>"
                "<li><strong>Celiachia</strong> — assorbimento proteico compromesso</li>"
                "<li><strong>SIADH</strong> — la secrezione inappropriata di ADH causa ritenzione "
                "idrica</li>"
                "</ul>"
                "<p>Un BUN basso da solo raramente indica un'emergenza, ma identificare la causa "
                "sottostante è importante. Quando si sospetta una malattia epatica, possono essere "
                "richiesti test aggiuntivi come ALT, AST e albumina.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="Cosa significa il rapporto BUN/Creatinina?",
            body_html=(
                "<p>Il <strong>rapporto BUN/Creatinina</strong> è uno strumento clinico prezioso "
                "che aiuta a determinare la causa di un BUN elevato. Il rapporto normale è "
                "generalmente compreso tra <strong>10:1 e 20:1</strong>.</p>"
                "<p><strong>Rapporto alto (&gt;20:1)</strong> — indica tipicamente cause prerenali: "
                "disidratazione, insufficienza cardiaca o emorragia GI alta. In queste situazioni "
                "il BUN aumenta in modo sproporzionato rispetto alla creatinina perché i reni "
                "riassorbono l'urea ma non la creatinina quando il flusso sanguigno è ridotto.</p>"
                "<p><strong>Rapporto basso (&lt;10:1)</strong> — può suggerire malattia epatica, "
                "malnutrizione o rabdomiolisi. Nella malattia epatica la produzione di urea "
                "diminuisce mentre i livelli di creatinina restano relativamente stabili.</p>"
                "<p>Questo rapporto è uno strumento pratico che aiuta i clinici a differenziare "
                "tra cause prerenali, renali e postrenali di azotemia.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="Effetto della disidratazione sui livelli di BUN",
            body_html=(
                "<p>La <strong>disidratazione</strong> è una delle cause non renali più comuni di "
                "BUN elevato. Quando il corpo non riceve abbastanza liquidi, il sangue si "
                "concentra e la capacità di filtrazione dei reni diminuisce, portando a un aumento "
                "del riassorbimento dell'urea e a un'elevazione sproporzionata del BUN.</p>"
                "<p>Nell'elevazione del BUN legata alla disidratazione, i livelli di "
                "<em>creatinina</em> restano generalmente normali o solo leggermente elevati. "
                "Di conseguenza, il <strong>rapporto BUN/creatinina supera 20:1</strong> — un "
                "indicatore chiave che suggerisce una causa prerenale piuttosto che una malattia "
                "renale intrinseca.</p>"
                "<p>Il ritorno del BUN alla normalità dopo un'adeguata reidratazione è una "
                "conferma clinica importante che l'elevazione era legata alla disidratazione. "
                "Tuttavia, una disidratazione prolungata o ricorrente può causare danni renali "
                "permanenti.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando dovresti consultare un medico?",
            body_html=(
                "<p>Dovresti discutere i tuoi risultati di BUN con un professionista sanitario "
                "se si verifica una delle seguenti situazioni:</p>"
                "<ul>"
                "<li>Il tuo livello di BUN è sopra o sotto l'intervallo di riferimento</li>"
                "<li>Avverti stanchezza persistente, debolezza o perdita di appetito</li>"
                "<li>Noti un <strong>edema</strong> (gonfiore) a caviglie, piedi o viso</li>"
                "<li>Ci sono cambiamenti nella frequenza, nel volume o nel colore delle urine</li>"
                "<li>Sono presenti sintomi come nausea, vomito o difficoltà respiratorie</li>"
                "</ul>"
                "<p>Questi sintomi possono indicare una disfunzione renale o altre condizioni "
                "sistemiche. La diagnosi e l'intervento precoci — soprattutto per le malattie "
                "renali — sono cruciali per rallentare la progressione della malattia.</p>"
                "<p>Rivedere i tuoi risultati prima dell'appuntamento può aiutarti a chiarire "
                "le domande e rendere la tua consulta più produttiva.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comprendi i tuoi risultati di BUN con Norya",
            body_html=(
                "<p>Comprendere i risultati delle analisi del sangue può essere complesso. "
                "<strong>Norya</strong> ti permette di caricare il tuo referto di laboratorio e "
                "ricevere un riepilogo sanitario strutturato e facile da capire in pochi minuti. "
                "Il tuo BUN, creatinina e altri marcatori renali vengono spiegati chiaramente.</p>"
                "<p>Carica le tue analisi ora su <a href=\"/analyze\">la nostra pagina di "
                "analisi</a> e arriva al tuo appuntamento medico più preparato. Visita la nostra "
                "<a href=\"/pricing\">pagina prezzi</a> per i dettagli dei piani.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere '
                'o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista '
                'sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'
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
            heading="בדיקת BUN (חנקן אוריאה בדם): מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>אם תוצאות בדיקת הדם שלך מראות רמת <strong>BUN (Blood Urea Nitrogen — "
                "חנקן אוריאה בדם)</strong> חריגה, הדבר עשוי לספק רמזים חשובים על תפקוד הכליות "
                "והבריאות הכללית שלך. BUN מודד את כמות חנקן האוריאה בדם — תוצר פסולת שנוצר "
                "כאשר הכבד מפרק חלבונים.</p>"
                "<p>מדריך זה מסביר מה מודדת בדיקת BUN, כיצד לפרש את התוצאות וכיצד להתכונן "
                "לפגישה עם הרופא. המטרה שלנו אינה לאבחן — אלא לעזור לך להגיע למפגש הרפואי "
                "מיודע יותר. חשוב להעריך את ה-BUN יחד עם סמנים קשורים כמו <em>קריאטינין</em>, "
                "<em>eGFR</em> ו-<em>יחס BUN/קריאטינין</em>.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="מהו BUN (חנקן אוריאה בדם)?",
            body_html=(
                "<p><strong>BUN</strong> היא בדיקת דם המודדת את כמות חנקן האוריאה בזרם הדם. "
                "כאשר הגוף מעכל חלבונים, נוצרת אמוניה כתוצר לוואי. הכבד ממיר אמוניה זו "
                "לאוריאה דרך <em>מחזור האוריאה</em> — תרכובת פחות רעילה שנכנסת לזרם הדם.</p>"
                "<p>הכליות מסננות את האוריאה מהדם ומפרישות אותה בשתן. בדיקת BUN מעריכה עד כמה "
                "תהליך זה יעיל. התוצאות מדווחות בדרך כלל ב-<strong>mg/dL</strong>. למרות "
                "ש-BUN הוא אחד מסמני תפקוד הכליות הנפוצים ביותר, הוא אינו ספציפי לכליות בלבד.</p>"
                "<p>BUN נכלל באופן שגרתי בפאנלים מטבוליים. גורמים כמו התייבשות, תזונה עתירת "
                "חלבון ותרופות מסוימות יכולים להשפיע משמעותית על רמות ה-BUN.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN ותפקוד הכליות",
            body_html=(
                "<p>הכליות הן איברים חיוניים המסננים תוצרי פסולת מהדם, שומרים על איזון נוזלים "
                "ואלקטרוליטים ומווסתים לחץ דם. אוריאה היא אחד מתוצרי הפסולת העיקריים שהכליות "
                "מסירות. כאשר תפקוד הכליות יורד, אוריאה מצטברת בדם — מצב הידוע בשם "
                "<strong>אזוטמיה</strong>.</p>"
                "<p>עם זאת, רמות BUN מושפעות מגורמים נוספים מעבר לתפקוד הכליות. צריכת חלבון, "
                "תפקוד הכבד, מצב ההידרציה ופירוק רקמות משפיעים כולם על ה-BUN. לכן BUN לבדו "
                "אינו מספיק לאבחון מחלת כליות; יש לפרש אותו יחד עם <em>קריאטינין</em> "
                "ו-<em>eGFR</em>.</p>"
                "<p>במצבים כמו פגיעה כלייתית חדה (AKI), מחלת כליות כרונית (CKD) ואי-ספיקת "
                "כליות סופנית, ה-BUN עולה באופן משמעותי. הבחנה בין סיבות פרה-רנליות, רנליות "
                "ופוסט-רנליות מחייבת בדיקות נוספות.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי BUN תקינים וטווחי ייחוס",
            body_html=(
                "<p>הטבלה הבאה מסכמת את טווחי הייחוס המקובלים עבור BUN ופרמטרים קשורים של "
                "תפקוד כלייתי. ייתכנו הבדלים קלים בין מעבדות; השווה תמיד את תוצאותיך לטווח "
                "הייחוס של המעבדה שלך.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>פרמטר</th>'
                f'<th {_TH}>טווח ייחוס</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>קריאטינין</td><td {_TD}>0.6–1.2 mg/dL (גברים) / 0.5–1.1 mg/dL (נשים)</td></tr>'
                f'<tr><td {_TD}>יחס BUN/קריאטינין</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>eGFR</td><td {_TD}>&gt;60 mL/min/1.73m² (תקין)</td></tr>'
                "</tbody></table>"
                "<p>ערך חריג בודד לא תמיד מעיד על מחלה. התייבשות, הרגלי תזונה ותרופות יכולים "
                "להשפיע על התוצאות. הרופא שלך יפרש את הממצאים בהקשר הקליני הכולל.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="סיבות ל-BUN גבוה (אזוטמיה)",
            body_html=(
                "<p><strong>BUN מוגבר</strong> (אזוטמיה) הוא אחד האינדיקטורים השכיחים ביותר "
                "לתפקוד כלייתי לקוי, אך מצבים רבים נוספים יכולים להעלות את רמות ה-BUN:</p>"
                "<ul>"
                "<li><strong>מחלת/אי-ספיקת כליות</strong> — פגיעה כלייתית חדה או כרונית מפחיתה "
                "את הפרשת האוריאה</li>"
                "<li><strong>התייבשות</strong> — איבוד נוזלים מרכז את הדם ומעלה BUN באופן לא "
                "פרופורציונלי</li>"
                "<li><strong>תזונה עתירת חלבון</strong> — צריכת חלבון מופרזת מגדילה ייצור "
                "אוריאה</li>"
                "<li><strong>אי-ספיקת לב</strong> — זרימת דם מופחתת לכליות (פרה-רנלי)</li>"
                "<li><strong>דימום GI עליון</strong> — חלבון דם מעוכל מגביר ייצור אוריאה</li>"
                "<li><strong>כוויות והלם</strong> — פירוק רקמות ואיבוד נפח דם</li>"
                "<li><strong>תרופות</strong> — קורטיקוסטרואידים, טטרציקלינים</li>"
                "<li><strong>חסימת דרכי השתן</strong> — חסימה (סיבה פוסט-רנלית)</li>"
                "</ul>"
                "<p>הבחנה בין סיבות פרה-רנליות, רנליות ופוסט-רנליות חיונית לתכנון הטיפול. "
                "הרופא שלך ישתמש ב-<em>יחס BUN/קריאטינין</em>, בבדיקת שתן ובהדמיה לזיהוי "
                "הסיבה.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="סיבות ל-BUN נמוך",
            body_html=(
                "<p><strong>BUN נמוך</strong> שכיח פחות מ-BUN מוגבר אך עשוי להצביע על מצבים "
                "חשובים:</p>"
                "<ul>"
                "<li><strong>מחלת/אי-ספיקת כבד</strong> — סינתזה מופחתת של אוריאה מכיוון "
                "שמחזור האוריאה מתרחש בכבד</li>"
                "<li><strong>תת-תזונה / תזונה דלת חלבון</strong> — מצע לא מספיק לייצור "
                "אוריאה</li>"
                "<li><strong>הידרציית יתר</strong> — דילול הדם (המודילוציה)</li>"
                "<li><strong>הריון</strong> — עלייה בנפח הדם והמודילוציה עשויות להוריד BUN</li>"
                "<li><strong>צליאק</strong> — ספיגת חלבון לקויה</li>"
                "<li><strong>SIADH</strong> — הפרשה לא מתאימה של ADH גורמת לאגירת נוזלים</li>"
                "</ul>"
                "<p>BUN נמוך לבדו לעיתים רחוקות מצביע על מצב חירום, אך חשוב לזהות את הסיבה "
                "הבסיסית. כאשר חשד למחלת כבד, ניתן להזמין בדיקות נוספות כמו ALT, AST "
                "ואלבומין.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="מה המשמעות של יחס BUN/קריאטינין?",
            body_html=(
                "<p><strong>יחס BUN/קריאטינין</strong> הוא כלי קליני חשוב המסייע לקבוע את "
                "הסיבה ל-BUN מוגבר. היחס התקין הוא בדרך כלל בין <strong>10:1 ל-20:1</strong>.</p>"
                "<p><strong>יחס גבוה (&gt;20:1)</strong> — מצביע בדרך כלל על סיבות פרה-רנליות: "
                "התייבשות, אי-ספיקת לב או דימום GI עליון. במצבים אלה BUN עולה באופן לא "
                "פרופורציונלי לקריאטינין מכיוון שהכליות סופגות מחדש אוריאה אך לא קריאטינין "
                "כאשר זרימת הדם מופחתת.</p>"
                "<p><strong>יחס נמוך (&lt;10:1)</strong> — עשוי להצביע על מחלת כבד, תת-תזונה "
                "או רבדומיוליזיס. במחלת כבד, ייצור אוריאה יורד בעוד רמות קריאטינין נשארות "
                "יציבות יחסית.</p>"
                "<p>יחס זה הוא כלי מעשי המסייע לרופאים להבחין בין סיבות פרה-רנליות, רנליות "
                "ופוסט-רנליות לאזוטמיה.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="השפעת התייבשות על רמות BUN",
            body_html=(
                "<p><strong>התייבשות</strong> היא אחת הסיבות הלא-כליתיות השכיחות ביותר ל-BUN "
                "מוגבר. כאשר הגוף לא מקבל מספיק נוזלים, הדם מתרכז ויכולת הסינון של הכליות "
                "יורדת, מה שמוביל לספיגה מחדש מוגברת של אוריאה ולעלייה לא פרופורציונלית "
                "ב-BUN.</p>"
                "<p>בעליית BUN הקשורה להתייבשות, רמות <em>קריאטינין</em> נשארות בדרך כלל "
                "תקינות או רק מעט מוגברות. כתוצאה מכך, <strong>יחס BUN/קריאטינין עולה מעל "
                "20:1</strong> — אינדיקטור מפתח המרמז על סיבה פרה-רנלית ולא על מחלת כליות "
                "פנימית.</p>"
                "<p>חזרת ה-BUN לנורמה לאחר הידרציה מספקת היא אישור קליני חשוב שהעלייה הייתה "
                "קשורה להתייבשות. עם זאת, התייבשות ממושכת או חוזרת עלולה לגרום נזק כלייתי "
                "קבוע לאורך זמן.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>עליך לדון בתוצאות ה-BUN שלך עם איש מקצוע רפואי אם אחד מהמצבים הבאים "
                "מתקיים:</p>"
                "<ul>"
                "<li>רמת ה-BUN שלך מעל או מתחת לטווח הייחוס</li>"
                "<li>אתה חווה עייפות מתמשכת, חולשה או אובדן תיאבון</li>"
                "<li>אתה מבחין ב-<strong>בצקת</strong> (נפיחות) בקרסוליים, ברגליים או בפנים</li>"
                "<li>ישנם שינויים בתדירות, בנפח או בצבע השתן</li>"
                "<li>קיימים תסמינים כמו בחילה, הקאות או קוצר נשימה</li>"
                "</ul>"
                "<p>תסמינים אלה עשויים להצביע על תפקוד כלייתי לקוי או מצבים מערכתיים אחרים. "
                "גילוי והתערבות מוקדמים — במיוחד במחלות כליות — חיוניים להאטת התקדמות "
                "המחלה.</p>"
                "<p>סקירת תוצאות בדיקות הדם שלך לפני הפגישה יכולה לעזור לך להבהיר שאלות "
                "ולהפוך את הייעוץ ליעיל יותר.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="הבן את תוצאות ה-BUN שלך עם Norya",
            body_html=(
                "<p>הבנת תוצאות בדיקות הדם שלך יכולה להיות מורכבת. <strong>Norya</strong> "
                "מאפשרת לך להעלות את דוח המעבדה ולקבל סיכום בריאותי מובנה וקל להבנה תוך "
                "דקות. ה-BUN, קריאטינין וסמנים כליתיים נוספים מוסברים בשפה ברורה.</p>"
                "<p>העלה את בדיקת הדם שלך עכשיו ב-<a href=\"/analyze\">דף הניתוח שלנו</a> "
                "והגע לפגישה עם הרופא מוכן יותר. בקר ב-<a href=\"/pricing\">דף המחירים</a> "
                "שלנו לפרטים.</p>"
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


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="BUN (ब्लड यूरिया नाइट्रोजन) टेस्ट: आपके परिणामों का क्या मतलब है?",
            body_html=(
                "<p>यदि आपकी रक्त जांच में <strong>BUN (Blood Urea Nitrogen — ब्लड यूरिया "
                "नाइट्रोजन)</strong> का स्तर असामान्य आता है, तो यह आपकी किडनी के कार्य और "
                "समग्र स्वास्थ्य के बारे में महत्वपूर्ण संकेत दे सकता है। BUN रक्त में यूरिया "
                "नाइट्रोजन की मात्रा मापता है — यह एक अपशिष्ट उत्पाद है जो लीवर द्वारा प्रोटीन "
                "के चयापचय से बनता है।</p>"
                "<p>यह गाइड बताती है कि BUN टेस्ट क्या मापता है, अपने परिणामों की व्याख्या कैसे "
                "करें और डॉक्टर की अपॉइंटमेंट के लिए कैसे तैयार हों। हमारा उद्देश्य निदान "
                "करना नहीं है — बल्कि आपको अपनी चिकित्सा परामर्श में अधिक जानकारीपूर्ण बनाना "
                "है। BUN का मूल्यांकन <em>क्रिएटिनिन</em>, <em>eGFR</em> और "
                "<em>BUN/क्रिएटिनिन अनुपात</em> जैसे संबंधित मार्करों के साथ करना आवश्यक है।</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="BUN (ब्लड यूरिया नाइट्रोजन) क्या है?",
            body_html=(
                "<p><strong>BUN</strong> एक रक्त परीक्षण है जो आपके रक्तप्रवाह में यूरिया "
                "नाइट्रोजन की मात्रा मापता है। जब आपका शरीर प्रोटीन पचाता है, तो उपोत्पाद "
                "के रूप में अमोनिया बनता है। लीवर इस अमोनिया को <em>यूरिया चक्र</em> के "
                "माध्यम से यूरिया में बदलता है — एक कम विषैला यौगिक जो रक्त में मिल जाता है।</p>"
                "<p>किडनी फिर रक्त से यूरिया को छानकर मूत्र के माध्यम से बाहर निकालती है। BUN "
                "टेस्ट इस प्रक्रिया की प्रभावशीलता का आकलन करता है। परिणाम आमतौर पर "
                "<strong>mg/dL</strong> में रिपोर्ट किए जाते हैं। BUN किडनी कार्य के सबसे आम "
                "मार्करों में से एक है, लेकिन यह केवल किडनी के लिए विशिष्ट नहीं है।</p>"
                "<p>BUN नियमित रूप से मेटाबॉलिक पैनल में शामिल किया जाता है। डिहाइड्रेशन, "
                "उच्च-प्रोटीन आहार और कुछ दवाएं भी BUN स्तर को काफी प्रभावित कर सकती हैं।</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN और किडनी का कार्य",
            body_html=(
                "<p>किडनी महत्वपूर्ण अंग हैं जो रक्त से अपशिष्ट पदार्थों को छानते हैं, "
                "द्रव-इलेक्ट्रोलाइट संतुलन बनाए रखते हैं और रक्तचाप को नियंत्रित करते हैं। "
                "यूरिया उन प्रमुख अपशिष्ट उत्पादों में से एक है जिन्हें किडनी हटाती है। जब "
                "किडनी का कार्य घटता है, तो यूरिया रक्त में जमा हो जाता है — इस स्थिति को "
                "<strong>एज़ोटेमिया</strong> कहा जाता है।</p>"
                "<p>हालांकि, BUN स्तर केवल किडनी कार्य से प्रभावित नहीं होते। प्रोटीन सेवन, "
                "लीवर कार्य, हाइड्रेशन स्थिति और ऊतक टूटना सभी BUN को प्रभावित करते हैं। "
                "इसलिए BUN अकेले किडनी रोग का निदान करने के लिए पर्याप्त नहीं है; इसे "
                "<em>क्रिएटिनिन</em> और <em>eGFR</em> के साथ व्याख्या किया जाना चाहिए।</p>"
                "<p>एक्यूट किडनी इंजरी (AKI), क्रोनिक किडनी डिजीज (CKD) और एंड-स्टेज रीनल "
                "डिजीज जैसी स्थितियों में BUN काफी बढ़ जाता है। प्रीरीनल, रीनल और पोस्टरीनल "
                "कारणों के बीच अंतर करने के लिए अतिरिक्त जांच आवश्यक है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="BUN सामान्य मान और संदर्भ सीमाएं",
            body_html=(
                "<p>निम्न तालिका BUN और संबंधित किडनी कार्य मापदंडों के लिए आम तौर पर "
                "स्वीकृत संदर्भ सीमाओं का सारांश प्रस्तुत करती है। प्रयोगशालाओं के बीच "
                "मामूली भिन्नताएं हो सकती हैं; अपने परिणामों की तुलना हमेशा अपनी प्रयोगशाला "
                "की संदर्भ सीमा से करें।</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>पैरामीटर</th>'
                f'<th {_TH}>संदर्भ सीमा</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>क्रिएटिनिन</td><td {_TD}>0.6–1.2 mg/dL (पुरुष) / 0.5–1.1 mg/dL (महिला)</td></tr>'
                f'<tr><td {_TD}>BUN/क्रिएटिनिन अनुपात</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>eGFR</td><td {_TD}>&gt;60 mL/min/1.73m² (सामान्य)</td></tr>'
                "</tbody></table>"
                "<p>एक असामान्य मान का मतलब हमेशा बीमारी नहीं होता। डिहाइड्रेशन, खान-पान "
                "की आदतें और दवाएं परिणामों को प्रभावित कर सकती हैं। आपके चिकित्सक आपकी "
                "समग्र नैदानिक तस्वीर के संदर्भ में परिणामों की व्याख्या करेंगे।</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="उच्च BUN (एज़ोटेमिया) के कारण",
            body_html=(
                "<p><strong>बढ़ा हुआ BUN</strong> (एज़ोटेमिया) बिगड़े किडनी कार्य के सबसे आम "
                "संकेतकों में से एक है, लेकिन कई अन्य स्थितियां भी BUN बढ़ा सकती हैं:</p>"
                "<ul>"
                "<li><strong>किडनी रोग/विफलता</strong> — तीव्र या पुरानी किडनी क्षति यूरिया "
                "उत्सर्जन को कम करती है</li>"
                "<li><strong>डिहाइड्रेशन</strong> — द्रव हानि रक्त को केंद्रित करती है और BUN "
                "को असमान रूप से बढ़ाती है</li>"
                "<li><strong>उच्च-प्रोटीन आहार</strong> — अधिक प्रोटीन सेवन यूरिया उत्पादन "
                "बढ़ाता है</li>"
                "<li><strong>हृदय विफलता</strong> — किडनी में रक्त प्रवाह कम होता है "
                "(प्रीरीनल)</li>"
                "<li><strong>ऊपरी GI रक्तस्राव</strong> — पचा हुआ रक्त प्रोटीन यूरिया "
                "उत्पादन बढ़ाता है</li>"
                "<li><strong>जलन और शॉक</strong> — ऊतक टूटना और रक्त मात्रा हानि</li>"
                "<li><strong>दवाएं</strong> — कॉर्टिकोस्टेरॉइड, टेट्रासाइक्लिन</li>"
                "<li><strong>मूत्र पथ अवरोध</strong> — रुकावट (पोस्टरीनल कारण)</li>"
                "</ul>"
                "<p>प्रीरीनल, रीनल और पोस्टरीनल कारणों के बीच अंतर करना उपचार मार्गदर्शन "
                "के लिए महत्वपूर्ण है। आपके डॉक्टर <em>BUN/क्रिएटिनिन अनुपात</em>, मूत्र "
                "विश्लेषण और इमेजिंग से मूल कारण की पहचान करेंगे।</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="कम BUN के कारण",
            body_html=(
                "<p><strong>कम BUN</strong> बढ़े हुए BUN की तुलना में कम आम है लेकिन कई "
                "महत्वपूर्ण स्थितियों का संकेत दे सकता है:</p>"
                "<ul>"
                "<li><strong>लीवर रोग/विफलता</strong> — यूरिया संश्लेषण कम हो जाता है क्योंकि "
                "यूरिया चक्र लीवर में होता है</li>"
                "<li><strong>कुपोषण / कम प्रोटीन आहार</strong> — यूरिया उत्पादन के लिए "
                "अपर्याप्त सब्सट्रेट</li>"
                "<li><strong>अत्यधिक हाइड्रेशन</strong> — रक्त का तनुकरण (हीमोडायल्यूशन)</li>"
                "<li><strong>गर्भावस्था</strong> — बढ़ा हुआ रक्त मात्रा और हीमोडायल्यूशन BUN "
                "को कम कर सकता है</li>"
                "<li><strong>सीलिएक रोग</strong> — बिगड़ा हुआ प्रोटीन अवशोषण</li>"
                "<li><strong>SIADH</strong> — अनुपयुक्त ADH स्राव द्रव प्रतिधारण का कारण "
                "बनता है</li>"
                "</ul>"
                "<p>कम BUN अकेले शायद ही कभी आपातकालीन स्थिति का संकेत देता है, लेकिन "
                "अंतर्निहित कारण की पहचान करना महत्वपूर्ण है। जब लीवर रोग का संदेह हो, तो "
                "ALT, AST और एल्ब्यूमिन जैसी अतिरिक्त जांच की जा सकती हैं।</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="BUN/क्रिएटिनिन अनुपात का क्या मतलब है?",
            body_html=(
                "<p><strong>BUN/क्रिएटिनिन अनुपात</strong> एक मूल्यवान नैदानिक उपकरण है जो "
                "बढ़े हुए BUN के कारण को निर्धारित करने में मदद करता है। सामान्य अनुपात "
                "आमतौर पर <strong>10:1 से 20:1</strong> के बीच होता है।</p>"
                "<p><strong>उच्च अनुपात (&gt;20:1)</strong> — आमतौर पर प्रीरीनल कारणों की ओर "
                "इशारा करता है: डिहाइड्रेशन, हृदय विफलता या ऊपरी GI रक्तस्राव। इन स्थितियों "
                "में BUN क्रिएटिनिन की तुलना में असमान रूप से बढ़ता है क्योंकि किडनी रक्त "
                "प्रवाह कम होने पर यूरिया को पुनः अवशोषित करती है लेकिन क्रिएटिनिन को नहीं।</p>"
                "<p><strong>कम अनुपात (&lt;10:1)</strong> — लीवर रोग, कुपोषण या रैब्डोमायोलिसिस "
                "का सुझाव दे सकता है। लीवर रोग में यूरिया उत्पादन घटता है जबकि क्रिएटिनिन "
                "स्तर अपेक्षाकृत स्थिर रहता है।</p>"
                "<p>यह अनुपात एक व्यावहारिक उपकरण है जो चिकित्सकों को एज़ोटेमिया के "
                "प्रीरीनल, रीनल और पोस्टरीनल कारणों में अंतर करने में मदद करता है।</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="डिहाइड्रेशन का BUN स्तर पर प्रभाव",
            body_html=(
                "<p><strong>डिहाइड्रेशन</strong> बढ़े हुए BUN के सबसे आम गैर-गुर्दे कारणों "
                "में से एक है। जब शरीर को पर्याप्त तरल पदार्थ नहीं मिलते, तो रक्त अधिक "
                "केंद्रित हो जाता है और किडनी की छानने की क्षमता कम हो जाती है, जिससे "
                "यूरिया का पुनः अवशोषण बढ़ता है और BUN असमान रूप से बढ़ता है।</p>"
                "<p>डिहाइड्रेशन-संबंधी BUN वृद्धि में <em>क्रिएटिनिन</em> का स्तर आमतौर पर "
                "सामान्य या केवल थोड़ा बढ़ा हुआ रहता है। इसलिए <strong>BUN/क्रिएटिनिन अनुपात "
                "20:1 से अधिक</strong> हो जाता है — यह एक प्रमुख संकेतक है जो आंतरिक किडनी "
                "रोग के बजाय प्रीरीनल कारण का सुझाव देता है।</p>"
                "<p>पर्याप्त पुनर्जलीकरण के बाद BUN का सामान्य होना एक महत्वपूर्ण नैदानिक "
                "पुष्टि है कि वृद्धि डिहाइड्रेशन से संबंधित थी। हालांकि, लंबे समय तक या "
                "बार-बार होने वाला डिहाइड्रेशन समय के साथ किडनी को स्थायी नुकसान पहुंचा "
                "सकता है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>आपको निम्नलिखित स्थितियों में अपने BUN परिणामों पर स्वास्थ्य पेशेवर से "
                "चर्चा करनी चाहिए:</p>"
                "<ul>"
                "<li>आपका BUN स्तर संदर्भ सीमा से ऊपर या नीचे है</li>"
                "<li>आप लगातार थकान, कमजोरी या भूख न लगना अनुभव कर रहे हैं</li>"
                "<li>टखनों, पैरों या चेहरे पर <strong>एडिमा</strong> (सूजन) दिखाई देती है</li>"
                "<li>पेशाब की आवृत्ति, मात्रा या रंग में बदलाव है</li>"
                "<li>मतली, उल्टी या सांस की तकलीफ जैसे लक्षण मौजूद हैं</li>"
                "</ul>"
                "<p>ये लक्षण किडनी की शिथिलता या अन्य प्रणालीगत स्थितियों का संकेत दे सकते "
                "हैं। जल्दी पता लगाना और हस्तक्षेप — विशेष रूप से किडनी रोग के लिए — रोग "
                "की प्रगति को धीमा करने और किडनी कार्य को संरक्षित करने के लिए महत्वपूर्ण है।</p>"
                "<p>अपनी अपॉइंटमेंट से पहले अपने रक्त परीक्षण परिणामों की समीक्षा करना "
                "प्रश्नों को स्पष्ट करने और परामर्श को अधिक उत्पादक बनाने में मदद कर "
                "सकता है।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya के साथ अपने BUN परिणाम समझें",
            body_html=(
                "<p>अपने रक्त परीक्षण के परिणामों को समझना जटिल हो सकता है। "
                "<strong>Norya</strong> आपको अपनी लैब रिपोर्ट अपलोड करने और मिनटों में एक "
                "संरचित, समझने में आसान स्वास्थ्य सारांश प्राप्त करने की सुविधा देता है। "
                "आपके BUN, क्रिएटिनिन और अन्य किडनी मार्कर स्पष्ट भाषा में समझाए जाते हैं।</p>"
                "<p>अभी <a href=\"/analyze\">हमारे विश्लेषण पृष्ठ</a> पर अपना रक्त परीक्षण "
                "अपलोड करें और डॉक्टर की अपॉइंटमेंट में बेहतर तैयारी से जाएं। योजना विवरण "
                "के लिए <a href=\"/pricing\">हमारा मूल्य निर्धारण पृष्ठ</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प '
                'नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। '
                '<a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
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
            heading="تحليل BUN (نيتروجين اليوريا في الدم): ماذا تعني نتائجك؟",
            body_html=(
                "<p>إذا أظهرت نتائج فحص الدم لديك مستوى غير طبيعي من "
                "<strong>BUN (Blood Urea Nitrogen — نيتروجين اليوريا في الدم)</strong>، فقد يوفر "
                "ذلك أدلة مهمة حول وظائف الكلى وصحتك العامة. يقيس BUN كمية نيتروجين اليوريا "
                "في الدم — وهو ناتج فضلات ينتج عندما يقوم الكبد بتكسير البروتين.</p>"
                "<p>يشرح هذا الدليل ما يقيسه تحليل BUN، وكيفية تفسير نتائجك، وكيفية "
                "الاستعداد لموعد الطبيب. هدفنا ليس التشخيص — بل مساعدتك في الوصول إلى "
                "استشارتك الطبية بمعرفة أكبر. من الضروري تقييم BUN مع علامات مرتبطة مثل "
                "<em>الكرياتينين</em> و<em>eGFR</em> و<em>نسبة BUN/الكرياتينين</em>.</p>"
            ),
        ),
        Section(
            id="what-is-bun", level=2,
            heading="ما هو تحليل BUN (نيتروجين اليوريا في الدم)؟",
            body_html=(
                "<p><strong>BUN</strong> هو تحليل دم يقيس كمية نيتروجين اليوريا في مجرى الدم. "
                "عندما يهضم جسمك البروتين، ينتج الأمونيا كناتج ثانوي. يحوّل الكبد هذه "
                "الأمونيا إلى يوريا من خلال <em>دورة اليوريا</em> — وهو مركب أقل سمية يدخل "
                "مجرى الدم.</p>"
                "<p>تقوم الكلى بترشيح اليوريا من الدم وإفرازها في البول. يقيّم تحليل BUN مدى "
                "كفاءة هذه العملية. تُعبَّر النتائج عادةً بوحدة <strong>mg/dL</strong>. رغم أن "
                "BUN هو أحد أكثر علامات وظائف الكلى طلباً، إلا أنه ليس خاصاً بالكلى وحدها.</p>"
                "<p>يُدرج BUN بشكل روتيني في اللوحات الأيضية. عوامل مثل الجفاف والنظام الغذائي "
                "الغني بالبروتين وبعض الأدوية يمكن أن تؤثر بشكل كبير على مستويات BUN.</p>"
            ),
        ),
        Section(
            id="bun-and-kidney", level=2,
            heading="BUN ووظائف الكلى",
            body_html=(
                "<p>الكلى أعضاء حيوية تقوم بترشيح الفضلات من الدم، والحفاظ على توازن السوائل "
                "والكهارل، وتنظيم ضغط الدم. اليوريا هي أحد نواتج الفضلات الرئيسية التي "
                "تزيلها الكلى. عندما تتراجع وظائف الكلى، تتراكم اليوريا في الدم — وهي حالة "
                "تُعرف باسم <strong>آزوتيميا</strong>.</p>"
                "<p>ومع ذلك، تتأثر مستويات BUN بأكثر من وظائف الكلى. تناول البروتين، ووظائف "
                "الكبد، وحالة الترطيب، وتحلل الأنسجة تؤثر جميعها على BUN. لذلك لا يكفي BUN "
                "وحده لتشخيص أمراض الكلى؛ يجب تفسيره مع <em>الكرياتينين</em> و<em>eGFR</em> "
                "للدقة السريرية.</p>"
                "<p>في حالات مثل إصابة الكلى الحادة (AKI) ومرض الكلى المزمن (CKD) والفشل "
                "الكلوي النهائي، يرتفع BUN بشكل ملحوظ. التمييز بين الأسباب قبل الكلوية "
                "والكلوية وبعد الكلوية يتطلب فحوصات إضافية.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية لـ BUN ونطاقات المرجع",
            body_html=(
                "<p>يلخص الجدول التالي نطاقات المرجع المقبولة عموماً لـ BUN ومعايير وظائف "
                "الكلى المرتبطة. قد توجد اختلافات طفيفة بين المختبرات؛ قارن دائماً نتائجك "
                "بالنطاق المرجعي لمختبرك.</p>"
                + _TABLE_STYLE
                + "<thead><tr>"
                f'<th {_TH}>المعيار</th>'
                f'<th {_TH}>النطاق المرجعي</th>'
                "</tr></thead><tbody>"
                f'<tr><td {_TD}>BUN</td><td {_TD}>7–20 mg/dL</td></tr>'
                f'<tr><td {_TD}>الكرياتينين</td><td {_TD}>0.6–1.2 mg/dL (رجال) / 0.5–1.1 mg/dL (نساء)</td></tr>'
                f'<tr><td {_TD}>نسبة BUN/الكرياتينين</td><td {_TD}>10:1 – 20:1</td></tr>'
                f'<tr><td {_TD}>eGFR</td><td {_TD}>&gt;60 mL/min/1.73m² (طبيعي)</td></tr>'
                "</tbody></table>"
                "<p>قيمة غير طبيعية واحدة لا تعني دائماً وجود مرض. الجفاف والعادات الغذائية "
                "والأدوية يمكن أن تؤثر على النتائج. سيفسر طبيبك النتائج في سياق صورتك "
                "السريرية الشاملة.</p>"
            ),
        ),
        Section(
            id="high-bun-causes", level=2,
            heading="أسباب ارتفاع BUN (آزوتيميا)",
            body_html=(
                "<p><strong>ارتفاع BUN</strong> (آزوتيميا) هو أحد أكثر المؤشرات شيوعاً على "
                "ضعف وظائف الكلى، لكن العديد من الحالات الأخرى يمكن أن ترفع مستويات BUN:</p>"
                "<ul>"
                "<li><strong>أمراض/فشل الكلى</strong> — تلف الكلى الحاد أو المزمن يقلل إفراز "
                "اليوريا</li>"
                "<li><strong>الجفاف</strong> — فقدان السوائل يركّز الدم ويرفع BUN بشكل غير "
                "متناسب</li>"
                "<li><strong>نظام غذائي غني بالبروتين</strong> — الإفراط في البروتين يزيد إنتاج "
                "اليوريا</li>"
                "<li><strong>قصور القلب</strong> — انخفاض تدفق الدم للكلى (قبل كلوي)</li>"
                "<li><strong>نزيف الجهاز الهضمي العلوي</strong> — الدم المهضوم يزيد إنتاج "
                "اليوريا</li>"
                "<li><strong>الحروق والصدمة</strong> — تحلل الأنسجة وفقدان حجم الدم</li>"
                "<li><strong>الأدوية</strong> — الكورتيكوستيرويدات، التتراسيكلين</li>"
                "<li><strong>انسداد المسالك البولية</strong> — انسداد (سبب بعد كلوي)</li>"
                "</ul>"
                "<p>التمييز بين الأسباب قبل الكلوية والكلوية وبعد الكلوية ضروري لتوجيه العلاج. "
                "سيستخدم طبيبك <em>نسبة BUN/الكرياتينين</em> وتحليل البول والتصوير لتحديد "
                "السبب الأساسي.</p>"
            ),
        ),
        Section(
            id="low-bun-causes", level=2,
            heading="أسباب انخفاض BUN",
            body_html=(
                "<p><strong>انخفاض BUN</strong> أقل شيوعاً من ارتفاعه لكنه قد يشير إلى حالات "
                "مهمة:</p>"
                "<ul>"
                "<li><strong>أمراض/فشل الكبد</strong> — انخفاض تخليق اليوريا لأن دورة اليوريا "
                "تحدث في الكبد</li>"
                "<li><strong>سوء التغذية / نظام غذائي منخفض البروتين</strong> — ركيزة غير كافية "
                "لإنتاج اليوريا</li>"
                "<li><strong>فرط الترطيب</strong> — تخفيف الدم (تمييع الدم)</li>"
                "<li><strong>الحمل</strong> — زيادة حجم الدم وتمييع الدم قد يخفضان BUN</li>"
                "<li><strong>الداء البطني (السيلياك)</strong> — ضعف امتصاص البروتين</li>"
                "<li><strong>SIADH</strong> — إفراز ADH غير المناسب يسبب احتباس السوائل</li>"
                "</ul>"
                "<p>انخفاض BUN وحده نادراً ما يشير إلى حالة طوارئ، لكن تحديد السبب الكامن "
                "مهم. عند الاشتباه بمرض كبدي، قد تُطلب فحوصات إضافية مثل ALT وAST "
                "والألبومين.</p>"
            ),
        ),
        Section(
            id="bun-creatinine-ratio", level=2,
            heading="ماذا تعني نسبة BUN/الكرياتينين؟",
            body_html=(
                "<p><strong>نسبة BUN/الكرياتينين</strong> هي أداة سريرية قيّمة تساعد في تحديد "
                "سبب ارتفاع BUN. النسبة الطبيعية تتراوح عادةً بين "
                "<strong>10:1 و20:1</strong>.</p>"
                "<p><strong>نسبة مرتفعة (&gt;20:1)</strong> — تشير عادةً إلى أسباب قبل كلوية: "
                "الجفاف، قصور القلب أو نزيف الجهاز الهضمي العلوي. في هذه الحالات يرتفع BUN "
                "بشكل غير متناسب مقارنة بالكرياتينين لأن الكلى تعيد امتصاص اليوريا لكن ليس "
                "الكرياتينين عند انخفاض تدفق الدم.</p>"
                "<p><strong>نسبة منخفضة (&lt;10:1)</strong> — قد تشير إلى مرض كبدي، سوء "
                "تغذية أو انحلال الربيدات. في مرض الكبد، ينخفض إنتاج اليوريا بينما تبقى "
                "مستويات الكرياتينين مستقرة نسبياً.</p>"
                "<p>هذه النسبة أداة عملية تساعد الأطباء في التمييز بين الأسباب قبل الكلوية "
                "والكلوية وبعد الكلوية للآزوتيميا.</p>"
            ),
        ),
        Section(
            id="dehydration-effect", level=2,
            heading="تأثير الجفاف على مستويات BUN",
            body_html=(
                "<p><strong>الجفاف</strong> هو أحد أكثر الأسباب غير الكلوية شيوعاً لارتفاع "
                "BUN. عندما لا يحصل الجسم على كمية كافية من السوائل، يتركز الدم وتنخفض قدرة "
                "الكلى على الترشيح، مما يؤدي إلى زيادة إعادة امتصاص اليوريا وارتفاع غير "
                "متناسب في BUN.</p>"
                "<p>في ارتفاع BUN المرتبط بالجفاف، تبقى مستويات <em>الكرياتينين</em> عادةً "
                "طبيعية أو مرتفعة قليلاً فقط. وبالتالي <strong>تتجاوز نسبة BUN/الكرياتينين "
                "20:1</strong> — وهو مؤشر رئيسي يشير إلى سبب قبل كلوي وليس مرض كلوي "
                "جوهري.</p>"
                "<p>عودة BUN إلى الطبيعي بعد الترطيب الكافي هو تأكيد سريري مهم أن الارتفاع "
                "كان مرتبطاً بالجفاف. ومع ذلك، قد يسبب الجفاف المطول أو المتكرر تلفاً "
                "كلوياً دائماً مع مرور الوقت.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>يجب مناقشة نتائج BUN مع متخصص في الرعاية الصحية إذا انطبقت أي من "
                "الحالات التالية:</p>"
                "<ul>"
                "<li>مستوى BUN لديك أعلى أو أقل من النطاق المرجعي</li>"
                "<li>تعاني من إرهاق مستمر أو ضعف أو فقدان الشهية</li>"
                "<li>تلاحظ <strong>وذمة</strong> (تورم) في الكاحلين أو القدمين أو الوجه</li>"
                "<li>هناك تغييرات في تكرار التبول أو كميته أو لونه</li>"
                "<li>توجد أعراض مثل الغثيان أو القيء أو ضيق التنفس</li>"
                "</ul>"
                "<p>قد تشير هذه الأعراض إلى خلل في وظائف الكلى أو حالات جهازية أخرى. "
                "الكشف المبكر والتدخل — خاصة في أمراض الكلى — ضروريان لإبطاء تقدم المرض "
                "والحفاظ على وظائف الكلى.</p>"
                "<p>مراجعة نتائج فحص الدم قبل موعدك يمكن أن تساعدك في توضيح أسئلتك وجعل "
                "استشارتك أكثر إنتاجية.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="افهم نتائج BUN الخاصة بك مع Norya",
            body_html=(
                "<p>قد يكون فهم نتائج تحليل الدم معقداً. <strong>Norya</strong> يتيح لك تحميل "
                "تقرير المختبر والحصول على ملخص صحي منظم وسهل الفهم في دقائق. يتم شرح BUN "
                "والكرياتينين وعلامات الكلى الأخرى بوضوح بلغة بسيطة.</p>"
                "<p>حمّل تحليل الدم الآن على <a href=\"/analyze\">صفحة التحليل</a> واذهب "
                "إلى موعد الطبيب مستعداً بشكل أفضل. قم بزيارة "
                "<a href=\"/pricing\">صفحة الأسعار</a> لمعرفة التفاصيل.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص '
                'الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. '
                '<a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_bun_sections_by_lang():
    """Returns sections_by_lang dict for BUN article (all 9 languages)."""
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


def get_bun_faq_schema_qa():
    """Returns faq_schema_qa dict for BUN article (all 9 languages)."""
    return {
        "tr": [
            {"question": "BUN (Kan Üre Azotu) testi nedir?",
             "answer": "BUN testi, kandaki üre azotu miktarını ölçen bir kan testidir. Üre, karaciğerde protein metabolizması sonucu oluşur ve böbrekler tarafından süzülerek idrarla atılır. BUN, böbrek fonksiyonlarının en temel göstergelerinden biridir ve rutin metabolik panellerin parçasıdır."},
            {"question": "Yüksek BUN ne anlama gelir?",
             "answer": "Yüksek BUN (azotemi), böbrek hastalığı veya yetmezliği, dehidrasyon, yüksek proteinli diyet, kalp yetmezliği, üst GI kanaması, yanıklar, bazı ilaçlar (kortikosteroidler, tetrasiklinler) veya üriner sistem obstrüksiyonu gibi nedenlerden kaynaklanabilir."},
            {"question": "Düşük BUN ne anlama gelir?",
             "answer": "Düşük BUN, karaciğer hastalığı veya yetmezliği, yetersiz beslenme veya düşük proteinli diyet, aşırı hidrasyon, gebelik, çölyak hastalığı veya SIADH gibi durumların göstergesi olabilir. Karaciğer üre sentezinden sorumlu olduğu için karaciğer hastalıklarında BUN düşer."},
            {"question": "BUN/Kreatinin oranı nedir?",
             "answer": "BUN/Kreatinin oranı, yüksek BUN'un nedenini belirlemeye yardımcı olan klinik bir göstergedir. Normal oran 10:1 ile 20:1 arasındadır. 20:1'in üzerindeki oran dehidrasyon veya kalp yetmezliği gibi prerenal nedenleri, 10:1'in altındaki oran ise karaciğer hastalığı veya yetersiz beslenmeyi düşündürür."},
            {"question": "Dehidrasyon BUN değerini etkiler mi?",
             "answer": "Evet, dehidrasyon BUN düzeyini yükselten en yaygın böbrek dışı nedenlerden biridir. Sıvı kaybı kanı yoğunlaştırır ve üre geri emilimini artırır. Dehidrasyonda BUN/Kreatinin oranı 20:1'in üzerine çıkar, bu da prerenal bir nedeni düşündürür."},
        ],
        "en": [
            {"question": "What is a BUN (Blood Urea Nitrogen) blood test?",
             "answer": "A BUN test measures the amount of urea nitrogen in your blood. Urea is a waste product formed when the liver breaks down protein. It enters the bloodstream and is filtered by the kidneys into urine. BUN is one of the most common kidney function markers and is part of routine metabolic panels."},
            {"question": "What does high BUN mean?",
             "answer": "High BUN (azotemia) can be caused by kidney disease or failure, dehydration, high-protein diet, heart failure, upper GI bleeding, burns, certain medications (corticosteroids, tetracyclines), or urinary tract obstruction. The BUN/creatinine ratio helps differentiate between causes."},
            {"question": "What does low BUN mean?",
             "answer": "Low BUN may indicate liver disease or failure (reduced urea synthesis), malnutrition or low-protein diet, overhydration, pregnancy (hemodilution), celiac disease, or SIADH. Since the urea cycle occurs in the liver, liver dysfunction directly reduces BUN levels."},
            {"question": "What is the BUN/creatinine ratio?",
             "answer": "The BUN/creatinine ratio helps determine the cause of elevated BUN. A normal ratio is 10:1 to 20:1. A ratio above 20:1 suggests prerenal causes like dehydration or heart failure. A ratio below 10:1 may indicate liver disease or malnutrition."},
            {"question": "Can dehydration affect BUN levels?",
             "answer": "Yes, dehydration is one of the most common non-renal causes of elevated BUN. Fluid loss concentrates the blood and increases urea reabsorption. In dehydration, the BUN/creatinine ratio typically exceeds 20:1, suggesting a prerenal cause rather than intrinsic kidney disease."},
        ],
        "es": [
            {"question": "¿Qué es el análisis de BUN (nitrógeno ureico en sangre)?",
             "answer": "El BUN mide la cantidad de nitrógeno ureico en la sangre. La urea es un producto de desecho que se forma cuando el hígado descompone las proteínas, pasa al torrente sanguíneo y es filtrada por los riñones hacia la orina. Es uno de los marcadores más comunes de función renal."},
            {"question": "¿Qué significa un BUN alto?",
             "answer": "Un BUN alto (azotemia) puede deberse a enfermedad renal, deshidratación, dieta hiperproteica, insuficiencia cardíaca, hemorragia GI alta, quemaduras, medicamentos (corticosteroides, tetraciclinas) u obstrucción del tracto urinario. La relación BUN/creatinina ayuda a diferenciar las causas."},
            {"question": "¿Qué significa un BUN bajo?",
             "answer": "Un BUN bajo puede indicar enfermedad hepática (síntesis reducida de urea), desnutrición o dieta baja en proteínas, sobrehidratación, embarazo (hemodilución), enfermedad celíaca o SIADH. La disfunción hepática reduce directamente los niveles de BUN."},
            {"question": "¿Qué es la relación BUN/Creatinina?",
             "answer": "La relación BUN/Creatinina ayuda a determinar la causa del BUN elevado. Lo normal es 10:1 a 20:1. Una relación superior a 20:1 sugiere causas prerrenales como deshidratación. Una relación inferior a 10:1 puede indicar enfermedad hepática o desnutrición."},
            {"question": "¿Puede la deshidratación afectar los niveles de BUN?",
             "answer": "Sí, la deshidratación es una de las causas no renales más comunes de BUN elevado. La pérdida de líquidos concentra la sangre y aumenta la reabsorción de urea. En la deshidratación, la relación BUN/creatinina supera típicamente 20:1."},
        ],
        "de": [
            {"question": "Was ist ein BUN (Blut-Harnstoff-Stickstoff) Test?",
             "answer": "Der BUN-Test misst die Menge an Harnstoff-Stickstoff im Blut. Harnstoff ist ein Abfallprodukt, das bei der Proteinverdauung in der Leber entsteht, ins Blut gelangt und von den Nieren über den Urin ausgeschieden wird. BUN ist einer der häufigsten Nierenfunktionsmarker."},
            {"question": "Was bedeutet ein hoher BUN-Wert?",
             "answer": "Ein hoher BUN (Azotämie) kann durch Nierenerkrankung, Dehydration, proteinreiche Ernährung, Herzinsuffizienz, obere GI-Blutung, Verbrennungen, Medikamente (Kortikosteroide, Tetracycline) oder Harnwegsobstruktion verursacht werden."},
            {"question": "Was bedeutet ein niedriger BUN-Wert?",
             "answer": "Ein niedriger BUN kann auf Lebererkrankung (verminderte Harnstoffsynthese), Mangelernährung, Überhydratation, Schwangerschaft, Zöliakie oder SIADH hinweisen. Da der Harnstoffzyklus in der Leber stattfindet, senkt Leberdysfunktion direkt den BUN."},
            {"question": "Was ist das BUN/Kreatinin-Verhältnis?",
             "answer": "Das BUN/Kreatinin-Verhältnis hilft, die Ursache eines erhöhten BUN zu bestimmen. Normal ist 10:1 bis 20:1. Über 20:1 deutet auf prärenale Ursachen wie Dehydration hin. Unter 10:1 kann auf Lebererkrankung oder Mangelernährung hindeuten."},
            {"question": "Kann Dehydration den BUN-Wert beeinflussen?",
             "answer": "Ja, Dehydration ist eine der häufigsten nicht-renalen Ursachen für erhöhten BUN. Flüssigkeitsverlust konzentriert das Blut und erhöht die Harnstoffrückresorption. Bei Dehydration übersteigt das BUN/Kreatinin-Verhältnis typischerweise 20:1."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test BUN (azote uréique sanguin) ?",
             "answer": "Le test BUN mesure la quantité d'azote uréique dans le sang. L'urée est un déchet produit par le foie lors de la dégradation des protéines, qui passe dans le sang et est filtrée par les reins dans l'urine. Le BUN est l'un des marqueurs de fonction rénale les plus courants."},
            {"question": "Que signifie un BUN élevé ?",
             "answer": "Un BUN élevé (azotémie) peut être causé par une maladie rénale, une déshydratation, un régime hyperprotéiné, une insuffisance cardiaque, une hémorragie GI haute, des brûlures, des médicaments (corticostéroïdes, tétracyclines) ou une obstruction urinaire."},
            {"question": "Que signifie un BUN bas ?",
             "answer": "Un BUN bas peut indiquer une maladie hépatique (synthèse réduite d'urée), une malnutrition, une surhydratation, une grossesse (hémodilution), une maladie cœliaque ou un SIADH. La dysfonction hépatique réduit directement les niveaux de BUN."},
            {"question": "Qu'est-ce que le rapport BUN/Créatinine ?",
             "answer": "Le rapport BUN/Créatinine aide à déterminer la cause d'un BUN élevé. Le rapport normal est de 10:1 à 20:1. Au-dessus de 20:1, il suggère des causes prérénales comme la déshydratation. En dessous de 10:1, il peut indiquer une maladie hépatique."},
            {"question": "La déshydratation peut-elle affecter les niveaux de BUN ?",
             "answer": "Oui, la déshydratation est l'une des causes non rénales les plus courantes de BUN élevé. La perte de liquides concentre le sang et augmente la réabsorption de l'urée. En cas de déshydratation, le rapport BUN/créatinine dépasse typiquement 20:1."},
        ],
        "it": [
            {"question": "Cos'è il test BUN (azoto ureico nel sangue)?",
             "answer": "Il test BUN misura la quantità di azoto ureico nel sangue. L'urea è un prodotto di scarto formato dal fegato durante la digestione delle proteine, che entra nel sangue e viene filtrata dai reni nelle urine. È uno dei marcatori di funzione renale più comuni."},
            {"question": "Cosa significa BUN alto?",
             "answer": "Un BUN elevato (azotemia) può essere causato da malattia renale, disidratazione, dieta iperproteica, insufficienza cardiaca, emorragia GI alta, ustioni, farmaci (corticosteroidi, tetracicline) o ostruzione delle vie urinarie."},
            {"question": "Cosa significa BUN basso?",
             "answer": "Un BUN basso può indicare malattia epatica (sintesi ridotta di urea), malnutrizione, iperidratazione, gravidanza (emodiluizione), celiachia o SIADH. La disfunzione epatica riduce direttamente i livelli di BUN."},
            {"question": "Cos'è il rapporto BUN/Creatinina?",
             "answer": "Il rapporto BUN/Creatinina aiuta a determinare la causa di un BUN elevato. Il rapporto normale è da 10:1 a 20:1. Sopra 20:1 suggerisce cause prerenali come disidratazione. Sotto 10:1 può indicare malattia epatica o malnutrizione."},
            {"question": "La disidratazione può influenzare i livelli di BUN?",
             "answer": "Sì, la disidratazione è una delle cause non renali più comuni di BUN elevato. La perdita di liquidi concentra il sangue e aumenta il riassorbimento dell'urea. In caso di disidratazione, il rapporto BUN/creatinina supera tipicamente 20:1."},
        ],
        "he": [
            {"question": "מהי בדיקת BUN (חנקן אוריאה בדם)?",
             "answer": "בדיקת BUN מודדת את כמות חנקן האוריאה בדם. אוריאה היא תוצר פסולת שנוצר כאשר הכבד מפרק חלבונים, נכנס לזרם הדם ומסונן על ידי הכליות לשתן. BUN הוא אחד מסמני תפקוד הכליות הנפוצים ביותר."},
            {"question": "מה המשמעות של BUN גבוה?",
             "answer": "BUN גבוה (אזוטמיה) יכול להיגרם ממחלת כליות, התייבשות, תזונה עתירת חלבון, אי-ספיקת לב, דימום GI עליון, כוויות, תרופות (קורטיקוסטרואידים, טטרציקלינים) או חסימת דרכי השתן."},
            {"question": "מה המשמעות של BUN נמוך?",
             "answer": "BUN נמוך עשוי להצביע על מחלת כבד (סינתזה מופחתת של אוריאה), תת-תזונה, הידרציית יתר, הריון (המודילוציה), צליאק או SIADH. מכיוון שמחזור האוריאה מתרחש בכבד, תפקוד כבד לקוי מוריד ישירות רמות BUN."},
            {"question": "מהו יחס BUN/קריאטינין?",
             "answer": "יחס BUN/קריאטינין מסייע לקבוע את סיבת ה-BUN המוגבר. היחס התקין הוא 10:1 עד 20:1. מעל 20:1 מרמז על סיבות פרה-רנליות כמו התייבשות. מתחת ל-10:1 עשוי להצביע על מחלת כבד או תת-תזונה."},
            {"question": "האם התייבשות יכולה להשפיע על רמות BUN?",
             "answer": "כן, התייבשות היא אחת הסיבות הלא-כליתיות השכיחות ביותר ל-BUN מוגבר. איבוד נוזלים מרכז את הדם ומגביר ספיגה מחדש של אוריאה. בהתייבשות, יחס BUN/קריאטינין עולה בדרך כלל מעל 20:1."},
        ],
        "hi": [
            {"question": "BUN (ब्लड यूरिया नाइट्रोजन) रक्त परीक्षण क्या है?",
             "answer": "BUN टेस्ट रक्त में यूरिया नाइट्रोजन की मात्रा मापता है। यूरिया एक अपशिष्ट उत्पाद है जो लीवर द्वारा प्रोटीन के चयापचय से बनता है, रक्तप्रवाह में प्रवेश करता है और किडनी द्वारा मूत्र में छान लिया जाता है। BUN सबसे आम किडनी कार्य मार्करों में से एक है।"},
            {"question": "उच्च BUN का क्या मतलब है?",
             "answer": "उच्च BUN (एज़ोटेमिया) किडनी रोग, डिहाइड्रेशन, उच्च-प्रोटीन आहार, हृदय विफलता, ऊपरी GI रक्तस्राव, जलन, दवाओं (कॉर्टिकोस्टेरॉइड, टेट्रासाइक्लिन) या मूत्र पथ अवरोध के कारण हो सकता है।"},
            {"question": "कम BUN का क्या मतलब है?",
             "answer": "कम BUN लीवर रोग (कम यूरिया संश्लेषण), कुपोषण, अत्यधिक हाइड्रेशन, गर्भावस्था (हीमोडायल्यूशन), सीलिएक रोग या SIADH का संकेत दे सकता है। चूंकि यूरिया चक्र लीवर में होता है, लीवर की शिथिलता सीधे BUN को कम करती है।"},
            {"question": "BUN/क्रिएटिनिन अनुपात क्या है?",
             "answer": "BUN/क्रिएटिनिन अनुपात बढ़े हुए BUN के कारण को निर्धारित करने में मदद करता है। सामान्य अनुपात 10:1 से 20:1 है। 20:1 से ऊपर डिहाइड्रेशन जैसे प्रीरीनल कारणों का सुझाव देता है। 10:1 से नीचे लीवर रोग या कुपोषण का संकेत दे सकता है।"},
            {"question": "क्या डिहाइड्रेशन BUN स्तर को प्रभावित कर सकता है?",
             "answer": "हां, डिहाइड्रेशन बढ़े हुए BUN के सबसे आम गैर-गुर्दे कारणों में से एक है। द्रव हानि रक्त को केंद्रित करती है और यूरिया पुनः अवशोषण बढ़ाती है। डिहाइड्रेशन में BUN/क्रिएटिनिन अनुपात आमतौर पर 20:1 से अधिक हो जाता है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل BUN (نيتروجين اليوريا في الدم)؟",
             "answer": "تحليل BUN يقيس كمية نيتروجين اليوريا في الدم. اليوريا هي ناتج فضلات يتكون عندما يقوم الكبد بتكسير البروتين، وتدخل مجرى الدم وتُرشَّح بواسطة الكلى إلى البول. BUN هو أحد أكثر علامات وظائف الكلى شيوعاً."},
            {"question": "ماذا يعني ارتفاع BUN؟",
             "answer": "ارتفاع BUN (آزوتيميا) قد يكون بسبب أمراض الكلى، الجفاف، نظام غذائي غني بالبروتين، قصور القلب، نزيف الجهاز الهضمي العلوي، الحروق، أدوية (كورتيكوستيرويدات، تتراسيكلين) أو انسداد المسالك البولية."},
            {"question": "ماذا يعني انخفاض BUN؟",
             "answer": "انخفاض BUN قد يشير إلى مرض كبدي (تخليق يوريا منخفض)، سوء تغذية، فرط ترطيب، حمل (تمييع الدم)، الداء البطني أو SIADH. بما أن دورة اليوريا تحدث في الكبد، فإن خلل الكبد يخفض مباشرة مستويات BUN."},
            {"question": "ما هي نسبة BUN/الكرياتينين؟",
             "answer": "نسبة BUN/الكرياتينين تساعد في تحديد سبب ارتفاع BUN. النسبة الطبيعية 10:1 إلى 20:1. فوق 20:1 تشير إلى أسباب قبل كلوية مثل الجفاف. أقل من 10:1 قد تشير إلى مرض كبدي أو سوء تغذية."},
            {"question": "هل يمكن للجفاف أن يؤثر على مستويات BUN؟",
             "answer": "نعم، الجفاف هو أحد أكثر الأسباب غير الكلوية شيوعاً لارتفاع BUN. فقدان السوائل يركز الدم ويزيد إعادة امتصاص اليوريا. في حالات الجفاف، تتجاوز نسبة BUN/الكرياتينين عادةً 20:1."},
        ],
    }
