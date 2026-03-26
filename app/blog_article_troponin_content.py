# -*- coding: utf-8 -*-
"""
Troponin blog article — full body content for all 9 languages.
Used by blog_i18n._article_troponin().
Sections: intro, normal-ranges, causes, when-to-see-doctor.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_TBL = (
    'class="w-full border border-slate-200 text-sm my-4" '
    'style="border-collapse: collapse;"'
)
_TH = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
_TH_RTL = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;"'
_TD = 'style="border:1px solid #cbd5e1;padding:8px 12px;"'


# ---------------------------------------------------------------------------
# Reference-range tables — one per language
# ---------------------------------------------------------------------------

_TROP_TABLE_TR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Belirteç</th>"
    f"<th {_TH}>99. Persentil (Üst Referans Sınırı)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Troponin I (konvansiyonel)</td>"
    f"<td {_TD}>&lt; 0,04 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponin T (konvansiyonel)</td>"
    f"<td {_TD}>&lt; 0,01 ng/mL</td></tr>"
    f"<tr><td {_TD}>Yüksek duyarlıklı troponin I (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (kadın) / &lt; 34 ng/L (erkek)</td></tr>"
    f"<tr><td {_TD}>Yüksek duyarlıklı troponin T (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_EN = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Marker</th>"
    f"<th {_TH}>99th Percentile (Upper Reference Limit)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Troponin I (conventional)</td>"
    f"<td {_TD}>&lt; 0.04 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponin T (conventional)</td>"
    f"<td {_TD}>&lt; 0.01 ng/mL</td></tr>"
    f"<tr><td {_TD}>High-sensitivity troponin I (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (women) / &lt; 34 ng/L (men)</td></tr>"
    f"<tr><td {_TD}>High-sensitivity troponin T (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_ES = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Marcador</th>"
    f"<th {_TH}>Percentil 99 (Límite de referencia superior)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Troponina I (convencional)</td>"
    f"<td {_TD}>&lt; 0,04 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponina T (convencional)</td>"
    f"<td {_TD}>&lt; 0,01 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponina I de alta sensibilidad (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (mujeres) / &lt; 34 ng/L (hombres)</td></tr>"
    f"<tr><td {_TD}>Troponina T de alta sensibilidad (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_DE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Marker</th>"
    f"<th {_TH}>99. Perzentile (oberer Referenzwert)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Troponin I (konventionell)</td>"
    f"<td {_TD}>&lt; 0,04 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponin T (konventionell)</td>"
    f"<td {_TD}>&lt; 0,01 ng/mL</td></tr>"
    f"<tr><td {_TD}>Hochsensitives Troponin I (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (Frauen) / &lt; 34 ng/L (Männer)</td></tr>"
    f"<tr><td {_TD}>Hochsensitives Troponin T (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_FR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Marqueur</th>"
    f"<th {_TH}>99e percentile (limite de référence supérieure)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Troponine I (conventionnelle)</td>"
    f"<td {_TD}>&lt; 0,04 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponine T (conventionnelle)</td>"
    f"<td {_TD}>&lt; 0,01 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponine I ultrasensible (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (femmes) / &lt; 34 ng/L (hommes)</td></tr>"
    f"<tr><td {_TD}>Troponine T ultrasensible (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_IT = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Marcatore</th>"
    f"<th {_TH}>99° percentile (limite di riferimento superiore)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Troponina I (convenzionale)</td>"
    f"<td {_TD}>&lt; 0,04 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponina T (convenzionale)</td>"
    f"<td {_TD}>&lt; 0,01 ng/mL</td></tr>"
    f"<tr><td {_TD}>Troponina I ad alta sensibilità (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (donne) / &lt; 34 ng/L (uomini)</td></tr>"
    f"<tr><td {_TD}>Troponina T ad alta sensibilità (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_HE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>סמן</th>"
    f"<th {_TH_RTL}>אחוזון 99 (גבול ייחוס עליון)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>טרופונין I (קונבנציונלי)</td>"
    f"<td {_TD}>&lt; 0.04 ng/mL</td></tr>"
    f"<tr><td {_TD}>טרופונין T (קונבנציונלי)</td>"
    f"<td {_TD}>&lt; 0.01 ng/mL</td></tr>"
    f"<tr><td {_TD}>טרופונין I רגיש במיוחד (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (נשים) / &lt; 34 ng/L (גברים)</td></tr>"
    f"<tr><td {_TD}>טרופונין T רגיש במיוחד (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_HI = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>मार्कर</th>"
    f"<th {_TH}>99वाँ परसेंटाइल (ऊपरी संदर्भ सीमा)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>ट्रोपोनिन I (कन्वेंशनल)</td>"
    f"<td {_TD}>&lt; 0.04 ng/mL</td></tr>"
    f"<tr><td {_TD}>ट्रोपोनिन T (कन्वेंशनल)</td>"
    f"<td {_TD}>&lt; 0.01 ng/mL</td></tr>"
    f"<tr><td {_TD}>हाई-सेंसिटिविटी ट्रोपोनिन I (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (महिला) / &lt; 34 ng/L (पुरुष)</td></tr>"
    f"<tr><td {_TD}>हाई-सेंसिटिविटी ट्रोपोनिन T (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)

_TROP_TABLE_AR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>المؤشر</th>"
    f"<th {_TH_RTL}>المئين 99 (الحد المرجعي الأعلى)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>تروبونين I (تقليدي)</td>"
    f"<td {_TD}>&lt; 0.04 ng/mL</td></tr>"
    f"<tr><td {_TD}>تروبونين T (تقليدي)</td>"
    f"<td {_TD}>&lt; 0.01 ng/mL</td></tr>"
    f"<tr><td {_TD}>تروبونين I عالي الحساسية (hs-cTnI)</td>"
    f"<td {_TD}>&lt; 26 ng/L (نساء) / &lt; 34 ng/L (رجال)</td></tr>"
    f"<tr><td {_TD}>تروبونين T عالي الحساسية (hs-cTnT)</td>"
    f"<td {_TD}>&lt; 14 ng/L</td></tr>"
    "</tbody></table>"
)


# ---------------------------------------------------------------------------
# Turkish
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Troponin kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>Troponin testi</strong>, kalp kası hücrelerinde bulunan ve hasar "
                "durumunda kana salınan <strong>kardiyak troponin</strong> proteinlerinin düzeyini "
                "ölçen bir <strong>kalp krizi kan testi</strong>dir. Troponin I ve Troponin T olmak "
                "üzere iki alt tipi klinik pratikte kullanılır. Bu proteinler sağlıklı bireylerde "
                "kanda çok düşük konsantrasyonlarda bulunur; miyokard hasarı oluştuğunda ise "
                "belirgin şekilde yükselir.</p>"
                "<p>Acil servislerde göğüs ağrısı ile başvuran hastalarda <strong>troponin testi</strong> "
                "miyokard enfarktüsünü (kalp krizi) doğrulamak veya dışlamak için ilk başvurulan "
                "laboratuvar testidir. Yüksek duyarlıklı troponin (hs-cTn) yöntemleri sayesinde "
                "çok küçük miyokard hasarları bile saptanabilir hâle gelmiştir. Bu rehberde "
                "<strong>troponin normal değerleri</strong>, <strong>yüksek troponin</strong> "
                "nedenlerini ve ne zaman doktora başvurmanız gerektiğini öğreneceksiniz.</p>"
                "<p>Troponin düzeyleri kalp kası hasarının en güvenilir biyokimyasal göstergesi "
                "olarak kabul edilir. Değerlerin doğru yorumlanması klinik tablo, EKG bulguları "
                "ve seri ölçümlerle birlikte yapılmalıdır; tek başına bir troponin sonucu tanı "
                "koydurmaz.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Troponin normal değerleri",
            body_html=(
                "<p><strong>Troponin normal aralığı</strong>, kullanılan teste (konvansiyonel veya "
                "yüksek duyarlıklı) ve laboratuvara göre farklılık gösterir. Klinik kılavuzlar, "
                "her troponin testinin 99. persentil değerini üst referans sınırı olarak kabul "
                "eder. Bu sınırın üzerindeki değerler miyokard hasarını düşündürür.</p>"
                "<p>Aşağıdaki tabloda yaygın olarak kullanılan <strong>troponin I</strong> ve "
                "<strong>troponin T</strong> testlerinin referans değerleri özetlenmiştir:</p>"
                + _TROP_TABLE_TR +
                "<p>Yüksek duyarlıklı testlerde kadın ve erkek için farklı eşik değerler "
                "tanımlanmıştır; bu cinsiyete özgü sınırlar tanı doğruluğunu artırır. Sonuçlarınızı "
                "her zaman laboratuvar raporunuzdaki referans aralığıyla karşılaştırın.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Troponin yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Yüksek troponin</strong> her zaman klasik kalp krizi anlamına gelmez. "
                "Miyokard hasarı birçok farklı klinik durumda ortaya çıkabilir. Troponin "
                "düzeylerini artırabilecek başlıca nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Akut miyokard enfarktüsü (kalp krizi):</strong> Koroner arterlerin "
                "tıkanması sonucu kalp kasının oksijensiz kalmasıdır; troponin yüksekliğinin en "
                "acil ve önemli nedenidir.</li>"
                "<li><strong>Miyokardit:</strong> Viral veya otoimmün nedenlerle kalp kasının "
                "iltihaplanması troponin seviyelerini belirgin şekilde yükseltebilir.</li>"
                "<li><strong>Pulmoner emboli (PE):</strong> Akciğer arterlerindeki pıhtı, sağ "
                "ventrikül üzerine binen yük nedeniyle troponin artışına yol açabilir.</li>"
                "<li><strong>Böbrek yetmezliği:</strong> Kronik böbrek hastalığında troponin "
                "klirensinin azalması ve eşlik eden kardiyak stres nedeniyle troponin düzeyleri "
                "sürekli yüksek seyredebilir.</li>"
                "<li><strong>Sepsis:</strong> Ağır enfeksiyonlarda sistemik inflamasyon ve "
                "hipotansiyon, miyokardiyal hasar yoluyla troponin yükselmesine neden olabilir.</li>"
                "<li><strong>Kalp yetmezliği ve kardiyomiyopati:</strong> Kronik kalp yetmezliğinde "
                "süregelen miyokardiyal gerilme, düşük düzeyde troponin artışına yol açabilir.</li>"
                "</ul>"
                "<p>Tanıda kritik olan, troponin değerinin zamana bağlı değişim örüntüsüdür "
                "(yükselme ve/veya düşme). Tek bir ölçüm yerine seri troponin takibi, akut "
                "miyokard enfarktüsünü kronik yükseklikten ayırt etmede altın standarttır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Göğüs ağrısı, nefes darlığı, sol kola veya çeneye yayılan ağrı, soğuk "
                "terleme ya da ani hâlsizlik gibi belirtiler yaşıyorsanız derhal acil servise "
                "başvurun. Bu semptomlar akut miyokard enfarktüsünün (kalp krizi) habercisi "
                "olabilir ve troponin testi ile hızlı değerlendirme hayat kurtarıcıdır.</p>"
                "<p>Troponin testiniz yüksek çıktıysa panik yapmayın ancak sonucu mutlaka bir "
                "kardiyoloji uzmanıyla paylaşın. Yüksek troponin düzeyi, kalp krizinden miyokardite, "
                "pulmoner emboliden böbrek yetmezliğine kadar geniş bir yelpazede değerlendirilmesi "
                "gereken bir bulgudur. Doktorunuz EKG, ekokardiyografi ve seri troponin ölçümleri "
                "ile klinik tabloyu netleştirecektir.</p>"
                "<p>Unutmayın: troponin sonucu tek başına tanı koymaz. Klinik semptomlar, EKG "
                "değişiklikleri ve görüntüleme bulguları ile birlikte değerlendirildiğinde doğru "
                "tanıya ulaşılır. Bilgi amaçlı internet araştırması yerine mutlaka hekiminize "
                "danışın.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# English
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Troponin blood test: what your results mean",
            body_html=(
                "<p>The <strong>troponin test</strong> measures the blood level of "
                "<strong>cardiac troponin</strong> proteins that are released when heart-muscle "
                "cells are damaged. Two subtypes — <strong>troponin I</strong> and "
                "<strong>troponin T</strong> — are used in clinical practice. In healthy "
                "individuals these proteins circulate at very low concentrations; when myocardial "
                "injury occurs, <strong>troponin levels</strong> rise sharply.</p>"
                "<p>In emergency departments the <strong>troponin test</strong> is the first-line "
                "<strong>heart attack blood test</strong> used to confirm or rule out myocardial "
                "infarction in patients presenting with chest pain. High-sensitivity cardiac "
                "troponin (hs-cTn) assays can now detect even minor myocardial damage. In this "
                "guide you will learn the <strong>troponin normal range</strong>, the causes of "
                "<strong>high troponin</strong>, and when to seek medical attention.</p>"
                "<p>Troponin levels are considered the most reliable biochemical marker of "
                "cardiac muscle injury. Accurate interpretation requires correlation with the "
                "clinical picture, ECG findings, and serial measurements — a single troponin "
                "result alone is not diagnostic.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Troponin normal range",
            body_html=(
                "<p>The <strong>troponin normal range</strong> varies depending on the assay "
                "(conventional vs. high-sensitivity) and the laboratory. Clinical guidelines "
                "define the 99th percentile of a healthy reference population as the upper "
                "reference limit for each <strong>cardiac troponin</strong> test. Values above "
                "this threshold suggest myocardial injury.</p>"
                "<p>The table below summarises the reference values for the most commonly used "
                "<strong>troponin I</strong> and <strong>troponin T</strong> assays:</p>"
                + _TROP_TABLE_EN +
                "<p>High-sensitivity assays use sex-specific cut-offs — separate thresholds for "
                "women and men — which supports clearer clinical interpretation. Always compare your result "
                "with the reference range printed on your own laboratory report.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high troponin levels",
            body_html=(
                "<p><strong>High troponin</strong> does not always mean a classic heart attack. "
                "Myocardial injury can arise in many clinical settings. The main causes of "
                "elevated <strong>troponin levels</strong> include:</p>"
                "<ul>"
                "<li><strong>Acute myocardial infarction (heart attack):</strong> Blockage of a "
                "coronary artery deprives the heart muscle of oxygen and is the most urgent and "
                "important cause of elevated troponin.</li>"
                "<li><strong>Myocarditis:</strong> Inflammation of the heart muscle due to viral "
                "or autoimmune causes can raise troponin levels significantly.</li>"
                "<li><strong>Pulmonary embolism (PE):</strong> A blood clot in the pulmonary "
                "arteries can strain the right ventricle and cause a troponin rise.</li>"
                "<li><strong>Renal failure:</strong> In chronic kidney disease, reduced troponin "
                "clearance and concurrent cardiac stress may keep troponin levels chronically "
                "elevated.</li>"
                "<li><strong>Sepsis:</strong> Severe infection can cause systemic inflammation "
                "and hypotension, leading to myocardial injury and elevated troponin.</li>"
                "<li><strong>Heart failure and cardiomyopathy:</strong> Ongoing myocardial "
                "strain in chronic heart failure can produce low-level troponin elevations.</li>"
                "</ul>"
                "<p>The key to diagnosis is the pattern of troponin change over time — a rise "
                "and/or fall. Serial troponin measurements, rather than a single value, are the "
                "gold standard for distinguishing acute myocardial infarction from chronically "
                "elevated levels.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If you experience chest pain, shortness of breath, pain radiating to the "
                "left arm or jaw, cold sweats, or sudden fatigue, go to an emergency department "
                "immediately. These symptoms may signal an acute myocardial infarction (heart "
                "attack), and rapid evaluation with a <strong>troponin test</strong> can be "
                "life-saving.</p>"
                "<p>If your troponin result comes back elevated, do not panic but share the "
                "result with a cardiologist without delay. <strong>High troponin</strong> is a "
                "finding that must be evaluated across a wide spectrum — from heart attack and "
                "myocarditis to pulmonary embolism and renal failure. Your doctor will use an "
                "ECG, echocardiography, and serial troponin measurements to clarify the clinical "
                "picture.</p>"
                "<p>Remember: a troponin result on its own is not a diagnosis. An accurate "
                "diagnosis is reached when clinical symptoms, ECG changes, and imaging findings "
                "are considered together. Always consult your physician rather than relying on "
                "internet research alone.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Spanish
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Prueba de troponina en sangre: qué significan sus resultados",
            body_html=(
                "<p>La <strong>prueba de troponina</strong> mide el nivel en sangre de las "
                "proteínas de <strong>troponina cardíaca</strong> que se liberan cuando las "
                "células del músculo cardíaco sufren daño. En la práctica clínica se utilizan "
                "dos subtipos: <strong>troponina I</strong> y <strong>troponina T</strong>. En "
                "personas sanas estas proteínas circulan en concentraciones muy bajas; cuando se "
                "produce una lesión miocárdica, los <strong>niveles de troponina</strong> se "
                "elevan de forma notable.</p>"
                "<p>En los servicios de urgencias, la <strong>prueba de troponina</strong> es el "
                "<strong>análisis de sangre para infarto</strong> de primera línea que se emplea "
                "para confirmar o descartar un infarto de miocardio en pacientes con dolor "
                "torácico. Los ensayos de troponina cardíaca de alta sensibilidad (hs-cTn) "
                "permiten detectar incluso lesiones miocárdicas menores. En esta guía conocerá "
                "el <strong>rango normal de troponina</strong>, las causas de la "
                "<strong>troponina alta</strong> y cuándo buscar atención médica.</p>"
                "<p>Los niveles de troponina se consideran el marcador bioquímico más fiable "
                "de lesión del músculo cardíaco. Su interpretación correcta requiere la "
                "correlación con el cuadro clínico, los hallazgos del ECG y las mediciones "
                "seriadas; un resultado aislado de troponina no es diagnóstico por sí solo.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de troponina",
            body_html=(
                "<p>El <strong>rango normal de troponina</strong> varía según el tipo de ensayo "
                "(convencional o de alta sensibilidad) y el laboratorio. Las guías clínicas "
                "definen el percentil 99 de una población sana de referencia como el límite "
                "superior de referencia para cada prueba de <strong>troponina cardíaca</strong>. "
                "Los valores por encima de este umbral sugieren lesión miocárdica.</p>"
                "<p>La siguiente tabla resume los valores de referencia de los ensayos de "
                "<strong>troponina I</strong> y <strong>troponina T</strong> más utilizados:</p>"
                + _TROP_TABLE_ES +
                "<p>Los ensayos de alta sensibilidad emplean puntos de corte específicos por "
                "sexo — umbrales diferentes para mujeres y hombres — lo que mejora la precisión "
                "diagnóstica. Compare siempre su resultado con el rango de referencia indicado "
                "en su propio informe de laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de troponina alta",
            body_html=(
                "<p>Una <strong>troponina alta</strong> no siempre significa un infarto clásico. "
                "La lesión miocárdica puede producirse en múltiples contextos clínicos. Las "
                "principales causas de elevación de los <strong>niveles de troponina</strong> "
                "incluyen:</p>"
                "<ul>"
                "<li><strong>Infarto agudo de miocardio (ataque cardíaco):</strong> La "
                "obstrucción de una arteria coronaria priva al músculo cardíaco de oxígeno y "
                "constituye la causa más urgente e importante de troponina elevada.</li>"
                "<li><strong>Miocarditis:</strong> La inflamación del músculo cardíaco por "
                "causas virales o autoinmunes puede elevar significativamente los niveles de "
                "troponina.</li>"
                "<li><strong>Embolia pulmonar (EP):</strong> Un coágulo en las arterias "
                "pulmonares puede sobrecargar el ventrículo derecho y provocar un aumento de "
                "troponina.</li>"
                "<li><strong>Insuficiencia renal:</strong> En la enfermedad renal crónica, la "
                "reducción del aclaramiento de troponina y el estrés cardíaco concomitante "
                "pueden mantener los niveles crónicamente elevados.</li>"
                "<li><strong>Sepsis:</strong> Las infecciones graves pueden causar inflamación "
                "sistémica e hipotensión, provocando daño miocárdico y elevación de "
                "troponina.</li>"
                "<li><strong>Insuficiencia cardíaca y miocardiopatía:</strong> La sobrecarga "
                "miocárdica continua en la insuficiencia cardíaca crónica puede producir "
                "elevaciones leves de troponina.</li>"
                "</ul>"
                "<p>La clave del diagnóstico es el patrón de cambio de la troponina en el "
                "tiempo (ascenso y/o descenso). Las mediciones seriadas de troponina, y no un "
                "valor aislado, constituyen el estándar de oro para diferenciar un infarto "
                "agudo de miocardio de una elevación crónica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si experimenta dolor torácico, dificultad para respirar, dolor que se "
                "irradia al brazo izquierdo o la mandíbula, sudoración fría o fatiga súbita, "
                "acuda de inmediato a un servicio de urgencias. Estos síntomas pueden indicar "
                "un infarto agudo de miocardio y la evaluación rápida mediante una "
                "<strong>prueba de troponina</strong> puede salvar la vida.</p>"
                "<p>Si su resultado de troponina está elevado, no se alarme, pero comparta el "
                "resultado con un cardiólogo sin demora. La <strong>troponina alta</strong> es "
                "un hallazgo que debe evaluarse en un amplio espectro — desde infarto y "
                "miocarditis hasta embolia pulmonar e insuficiencia renal. Su médico utilizará "
                "un ECG, ecocardiografía y mediciones seriadas de troponina para esclarecer el "
                "cuadro clínico.</p>"
                "<p>Recuerde: un resultado de troponina por sí solo no constituye un "
                "diagnóstico. Se llega al diagnóstico correcto cuando se consideran en "
                "conjunto los síntomas clínicos, los cambios del ECG y los hallazgos de "
                "imagen. Consulte siempre a su médico en lugar de confiar únicamente en "
                "búsquedas en internet.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Troponin-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>Troponin-Test</strong> misst die Blutkonzentration von "
                "<strong>kardialem Troponin</strong> — Proteinen, die bei einer Schädigung von "
                "Herzmuskelzellen ins Blut freigesetzt werden. In der klinischen Praxis werden "
                "zwei Subtypen verwendet: <strong>Troponin I</strong> und "
                "<strong>Troponin T</strong>. Bei gesunden Personen zirkulieren diese Proteine "
                "in sehr niedrigen Konzentrationen; bei einem Myokardschaden steigen die "
                "<strong>Troponinwerte</strong> deutlich an.</p>"
                "<p>In der Notaufnahme ist der <strong>Troponin-Test</strong> der "
                "<strong>Herzinfarkt-Bluttest</strong> der ersten Wahl, um bei Patienten mit "
                "Brustschmerzen einen Myokardinfarkt zu bestätigen oder auszuschließen. "
                "Hochsensitive kardiale Troponin-Assays (hs-cTn) können heute selbst kleinste "
                "Myokardschäden nachweisen. In diesem Ratgeber erfahren Sie die "
                "<strong>Troponin-Normalwerte</strong>, die Ursachen für <strong>erhöhtes "
                "Troponin</strong> und wann Sie ärztliche Hilfe suchen sollten.</p>"
                "<p>Troponinwerte gelten als der zuverlässigste biochemische Marker für eine "
                "Herzmuskelschädigung. Eine korrekte Interpretation erfordert die Zusammenschau "
                "mit dem klinischen Bild, EKG-Befunden und seriellen Messungen — ein einzelner "
                "Troponinwert allein ist nicht diagnostisch.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Troponin-Normalwerte",
            body_html=(
                "<p>Der <strong>Troponin-Normalbereich</strong> hängt vom verwendeten Test "
                "(konventionell vs. hochsensitiv) und vom jeweiligen Labor ab. Klinische "
                "Leitlinien definieren die 99. Perzentile einer gesunden Referenzpopulation "
                "als oberen Referenzwert für jeden <strong>kardialen Troponin</strong>-Test. "
                "Werte oberhalb dieses Grenzwerts deuten auf eine Myokardschädigung hin.</p>"
                "<p>Die folgende Tabelle fasst die Referenzwerte der am häufigsten verwendeten "
                "<strong>Troponin-I</strong>- und <strong>Troponin-T</strong>-Assays zusammen:</p>"
                + _TROP_TABLE_DE +
                "<p>Hochsensitive Tests verwenden geschlechtsspezifische Grenzwerte — "
                "unterschiedliche Schwellen für Frauen und Männer — was die diagnostische "
                "Genauigkeit verbessert. Vergleichen Sie Ihr Ergebnis stets mit dem "
                "Referenzbereich auf Ihrem eigenen Laborbefund.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für erhöhte Troponinwerte",
            body_html=(
                "<p><strong>Erhöhtes Troponin</strong> bedeutet nicht immer einen klassischen "
                "Herzinfarkt. Myokardschäden können in vielen klinischen Situationen auftreten. "
                "Die wichtigsten Ursachen erhöhter <strong>Troponinwerte</strong> sind:</p>"
                "<ul>"
                "<li><strong>Akuter Myokardinfarkt (Herzinfarkt):</strong> Der Verschluss "
                "einer Koronararterie unterbricht die Sauerstoffversorgung des Herzmuskels und "
                "ist die dringlichste und wichtigste Ursache für einen Troponin-Anstieg.</li>"
                "<li><strong>Myokarditis:</strong> Eine virale oder autoimmune Entzündung des "
                "Herzmuskels kann die Troponinwerte deutlich erhöhen.</li>"
                "<li><strong>Lungenembolie (LE):</strong> Ein Blutgerinnsel in den "
                "Lungenarterien kann den rechten Ventrikel belasten und zu einem "
                "Troponin-Anstieg führen.</li>"
                "<li><strong>Nierenversagen:</strong> Bei chronischer Nierenerkrankung können "
                "eine verminderte Troponin-Clearance und begleitender kardialer Stress zu "
                "chronisch erhöhten Troponinwerten führen.</li>"
                "<li><strong>Sepsis:</strong> Schwere Infektionen können systemische Entzündung "
                "und Hypotonie verursachen und so zu einer Myokardschädigung und einem "
                "Troponin-Anstieg führen.</li>"
                "<li><strong>Herzinsuffizienz und Kardiomyopathie:</strong> Anhaltende "
                "myokardiale Belastung bei chronischer Herzinsuffizienz kann niedriggradige "
                "Troponin-Erhöhungen verursachen.</li>"
                "</ul>"
                "<p>Entscheidend für die Diagnose ist das Verlaufsmuster des Troponins — ein "
                "Anstieg und/oder Abfall über die Zeit. Serielle Troponin-Messungen statt eines "
                "Einzelwerts sind der Goldstandard zur Unterscheidung eines akuten "
                "Myokardinfarkts von chronisch erhöhten Werten.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Sie Brustschmerzen, Atemnot, in den linken Arm oder Kiefer "
                "ausstrahlende Schmerzen, kalten Schweiß oder plötzliche Erschöpfung verspüren, "
                "suchen Sie sofort eine Notaufnahme auf. Diese Symptome können auf einen akuten "
                "Myokardinfarkt (Herzinfarkt) hindeuten, und eine schnelle Abklärung mittels "
                "<strong>Troponin-Test</strong> kann lebensrettend sein.</p>"
                "<p>Wenn Ihr Troponin-Ergebnis erhöht ist, bewahren Sie Ruhe, teilen Sie das "
                "Ergebnis aber unverzüglich einem Kardiologen mit. <strong>Erhöhtes "
                "Troponin</strong> muss in einem breiten Spektrum bewertet werden — von "
                "Herzinfarkt und Myokarditis über Lungenembolie bis hin zu Nierenversagen. "
                "Ihr Arzt wird ein EKG, eine Echokardiographie und serielle Troponin-Messungen "
                "heranziehen, um das klinische Bild zu klären.</p>"
                "<p>Denken Sie daran: Ein Troponin-Ergebnis allein stellt keine Diagnose. "
                "Eine zutreffende Diagnose ergibt sich erst aus der Zusammenschau von klinischen "
                "Symptomen, EKG-Veränderungen und Bildgebungsbefunden. Besprechen Sie Ihre "
                "Ergebnisse stets mit Ihrem Arzt, anstatt sich allein auf Internetrecherchen "
                "zu verlassen.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# French
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Test de troponine : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test de troponine</strong> mesure le taux sanguin des protéines "
                "de <strong>troponine cardiaque</strong> libérées lorsque les cellules du muscle "
                "cardiaque sont endommagées. Deux sous-types sont utilisés en pratique clinique : "
                "la <strong>troponine I</strong> et la <strong>troponine T</strong>. Chez les "
                "sujets sains, ces protéines circulent à des concentrations très faibles ; en "
                "cas de lésion myocardique, les <strong>taux de troponine</strong> augmentent "
                "fortement.</p>"
                "<p>Aux urgences, le <strong>test de troponine</strong> est l'<strong>analyse de "
                "sang pour infarctus</strong> de première intention pour confirmer ou exclure un "
                "infarctus du myocarde chez les patients présentant une douleur thoracique. Les "
                "dosages de troponine cardiaque ultrasensible (hs-cTn) permettent désormais de "
                "détecter des lésions myocardiques même mineures. Dans ce guide, vous découvrirez "
                "les <strong>valeurs normales de troponine</strong>, les causes d'une "
                "<strong>troponine élevée</strong> et quand consulter un médecin.</p>"
                "<p>Les taux de troponine sont considérés comme le marqueur biochimique le plus "
                "fiable d'une lésion du muscle cardiaque. Leur interprétation correcte nécessite "
                "une corrélation avec le tableau clinique, les résultats de l'ECG et des mesures "
                "sériées — un résultat isolé de troponine ne constitue pas un diagnostic.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de troponine",
            body_html=(
                "<p>Les <strong>valeurs normales de troponine</strong> varient selon le type "
                "d'analyse (conventionnelle ou ultrasensible) et le laboratoire. Les "
                "recommandations cliniques définissent le 99e percentile d'une population saine "
                "de référence comme la limite supérieure de référence pour chaque test de "
                "<strong>troponine cardiaque</strong>. Les valeurs dépassant ce seuil évoquent "
                "une lésion myocardique.</p>"
                "<p>Le tableau ci-dessous résume les valeurs de référence des dosages de "
                "<strong>troponine I</strong> et <strong>troponine T</strong> les plus "
                "couramment utilisés :</p>"
                + _TROP_TABLE_FR +
                "<p>Les dosages ultrasensibles utilisent des seuils spécifiques au sexe — des "
                "limites différentes pour les femmes et les hommes — ce qui améliore la "
                "précision diagnostique. Comparez toujours votre résultat avec l'intervalle "
                "de référence figurant sur votre propre compte rendu de laboratoire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une troponine élevée",
            body_html=(
                "<p>Une <strong>troponine élevée</strong> ne signifie pas toujours un infarctus "
                "classique. Une lésion myocardique peut survenir dans de nombreux contextes "
                "cliniques. Les principales causes d'élévation des <strong>taux de "
                "troponine</strong> sont :</p>"
                "<ul>"
                "<li><strong>Infarctus aigu du myocarde (crise cardiaque) :</strong> "
                "L'obstruction d'une artère coronaire prive le muscle cardiaque d'oxygène et "
                "constitue la cause la plus urgente et la plus importante d'élévation de la "
                "troponine.</li>"
                "<li><strong>Myocardite :</strong> L'inflammation du muscle cardiaque d'origine "
                "virale ou auto-immune peut augmenter significativement les taux de "
                "troponine.</li>"
                "<li><strong>Embolie pulmonaire (EP) :</strong> Un caillot dans les artères "
                "pulmonaires peut surcharger le ventricule droit et provoquer une élévation de "
                "la troponine.</li>"
                "<li><strong>Insuffisance rénale :</strong> Dans la maladie rénale chronique, "
                "la diminution de la clairance de la troponine et le stress cardiaque "
                "concomitant peuvent maintenir les taux chroniquement élevés.</li>"
                "<li><strong>Sepsis :</strong> Les infections sévères peuvent entraîner une "
                "inflammation systémique et une hypotension, causant des lésions myocardiques "
                "et une élévation de la troponine.</li>"
                "<li><strong>Insuffisance cardiaque et cardiomyopathie :</strong> La contrainte "
                "myocardique continue dans l'insuffisance cardiaque chronique peut produire des "
                "élévations modérées de troponine.</li>"
                "</ul>"
                "<p>L'élément clé du diagnostic est le profil d'évolution de la troponine dans "
                "le temps (hausse et/ou baisse). Les mesures sériées de troponine, et non une "
                "valeur isolée, constituent la référence pour distinguer un infarctus aigu du "
                "myocarde d'une élévation chronique.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si vous ressentez une douleur thoracique, un essoufflement, une douleur "
                "irradiant vers le bras gauche ou la mâchoire, des sueurs froides ou une "
                "fatigue soudaine, rendez-vous immédiatement aux urgences. Ces symptômes "
                "peuvent signaler un infarctus aigu du myocarde (crise cardiaque) et une "
                "évaluation rapide par un <strong>test de troponine</strong> peut sauver "
                "la vie.</p>"
                "<p>Si votre résultat de troponine est élevé, ne paniquez pas mais partagez-le "
                "sans délai avec un cardiologue. Une <strong>troponine élevée</strong> est un "
                "signe qui doit être évalué dans un large spectre — de l'infarctus et de la "
                "myocardite à l'embolie pulmonaire et à l'insuffisance rénale. Votre médecin "
                "utilisera un ECG, une échocardiographie et des dosages sériés de troponine "
                "pour clarifier le tableau clinique.</p>"
                "<p>N'oubliez pas : un résultat de troponine seul ne constitue pas un "
                "diagnostic. Un diagnostic précis repose sur l'association des symptômes "
                "cliniques, des modifications de l'ECG et des résultats de l'imagerie. "
                "Consultez toujours votre médecin plutôt que de vous fier uniquement à des "
                "recherches sur internet.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Italian
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Test della troponina: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test della troponina</strong> misura il livello ematico delle "
                "proteine di <strong>troponina cardiaca</strong> che vengono rilasciate quando "
                "le cellule del muscolo cardiaco subiscono un danno. In pratica clinica si "
                "utilizzano due sottotipi: <strong>troponina I</strong> e "
                "<strong>troponina T</strong>. Nelle persone sane queste proteine circolano a "
                "concentrazioni molto basse; in caso di lesione miocardica, i <strong>livelli "
                "di troponina</strong> aumentano in modo significativo.</p>"
                "<p>Nei pronto soccorso il <strong>test della troponina</strong> è l'<strong>esame "
                "del sangue per infarto</strong> di prima scelta per confermare o escludere un "
                "infarto miocardico nei pazienti con dolore toracico. I dosaggi di troponina "
                "cardiaca ad alta sensibilità (hs-cTn) consentono oggi di rilevare anche danni "
                "miocardici minimi. In questa guida scoprirai i <strong>valori normali di "
                "troponina</strong>, le cause di <strong>troponina alta</strong> e quando "
                "rivolgersi al medico.</p>"
                "<p>I livelli di troponina sono considerati il marcatore biochimico più "
                "affidabile di danno al muscolo cardiaco. Un'interpretazione corretta richiede "
                "la correlazione con il quadro clinico, i reperti dell'ECG e le misurazioni "
                "seriali — un singolo risultato di troponina non è di per sé diagnostico.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di troponina",
            body_html=(
                "<p>I <strong>valori normali di troponina</strong> variano in base al tipo di "
                "dosaggio (convenzionale o ad alta sensibilità) e al laboratorio. Le linee guida "
                "cliniche definiscono il 99° percentile di una popolazione sana di riferimento "
                "come limite di riferimento superiore per ogni test di <strong>troponina "
                "cardiaca</strong>. Valori al di sopra di questa soglia suggeriscono una lesione "
                "miocardica.</p>"
                "<p>La tabella seguente riassume i valori di riferimento dei dosaggi di "
                "<strong>troponina I</strong> e <strong>troponina T</strong> più comunemente "
                "utilizzati:</p>"
                + _TROP_TABLE_IT +
                "<p>I dosaggi ad alta sensibilità utilizzano valori soglia specifici per sesso "
                "— limiti diversi per donne e uomini — migliorando così l'accuratezza "
                "diagnostica. Confronta sempre il tuo risultato con l'intervallo di riferimento "
                "indicato nel tuo referto di laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di troponina alta",
            body_html=(
                "<p>Una <strong>troponina alta</strong> non indica sempre un infarto classico. "
                "Il danno miocardico può verificarsi in molteplici contesti clinici. Le "
                "principali cause di elevazione dei <strong>livelli di troponina</strong> "
                "includono:</p>"
                "<ul>"
                "<li><strong>Infarto miocardico acuto (attacco cardiaco):</strong> L'ostruzione "
                "di un'arteria coronaria priva il muscolo cardiaco di ossigeno ed è la causa "
                "più urgente e importante di troponina elevata.</li>"
                "<li><strong>Miocardite:</strong> L'infiammazione del muscolo cardiaco da cause "
                "virali o autoimmuni può innalzare significativamente i livelli di "
                "troponina.</li>"
                "<li><strong>Embolia polmonare (EP):</strong> Un coagulo nelle arterie "
                "polmonari può sovraccaricare il ventricolo destro e provocare un aumento della "
                "troponina.</li>"
                "<li><strong>Insufficienza renale:</strong> Nella malattia renale cronica, la "
                "riduzione della clearance della troponina e lo stress cardiaco concomitante "
                "possono mantenere livelli cronicamente elevati.</li>"
                "<li><strong>Sepsi:</strong> Le infezioni gravi possono causare infiammazione "
                "sistemica e ipotensione, determinando danno miocardico e innalzamento della "
                "troponina.</li>"
                "<li><strong>Insufficienza cardiaca e cardiomiopatia:</strong> Lo sforzo "
                "miocardico continuo nell'insufficienza cardiaca cronica può produrre aumenti "
                "lievi della troponina.</li>"
                "</ul>"
                "<p>L'elemento chiave per la diagnosi è il profilo di variazione della "
                "troponina nel tempo (aumento e/o diminuzione). Le misurazioni seriali della "
                "troponina, e non un valore isolato, rappresentano il gold standard per "
                "distinguere un infarto miocardico acuto da un'elevazione cronica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se avverti dolore toracico, difficoltà respiratoria, dolore che si irradia "
                "al braccio sinistro o alla mandibola, sudorazione fredda o stanchezza "
                "improvvisa, recati immediatamente al pronto soccorso. Questi sintomi possono "
                "segnalare un infarto miocardico acuto (attacco cardiaco) e una valutazione "
                "rapida con un <strong>test della troponina</strong> può salvare la vita.</p>"
                "<p>Se il tuo risultato di troponina è elevato, non allarmarti ma condividi "
                "il risultato senza indugio con un cardiologo. Una <strong>troponina "
                "alta</strong> è un reperto che deve essere valutato in un ampio spettro — "
                "dall'infarto e dalla miocardite all'embolia polmonare e all'insufficienza "
                "renale. Il tuo medico utilizzerà un ECG, un'ecocardiografia e misurazioni "
                "seriali della troponina per chiarire il quadro clinico.</p>"
                "<p>Ricorda: un risultato di troponina da solo non è una diagnosi. Una diagnosi "
                "accurata si ottiene quando si considerano insieme i sintomi clinici, le "
                "alterazioni dell'ECG e i reperti dell'imaging. Consulta sempre il tuo medico "
                "anziché affidarti esclusivamente a ricerche su internet.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hebrew
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="בדיקת טרופונין בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת טרופונין</strong> מודדת את רמת חלבוני "
                "<strong>הטרופונין הלבבי</strong> בדם — חלבונים המשתחררים כאשר תאי שריר הלב "
                "נפגעים. בפרקטיקה הקלינית נעשה שימוש בשני תת-סוגים: <strong>טרופונין I</strong> "
                "ו<strong>טרופונין T</strong>. אצל אנשים בריאים חלבונים אלה מסתובבים בריכוזים "
                "נמוכים מאוד; כאשר מתרחש נזק למיוקרד, <strong>רמות הטרופונין</strong> עולות "
                "באופן ניכר.</p>"
                "<p>בחדרי מיון <strong>בדיקת הטרופונין</strong> היא <strong>בדיקת דם לאוטם "
                "לבבי</strong> ראשונית המשמשת לאישור או שלילה של אוטם שריר הלב בחולים עם כאב "
                "חזה. בדיקות טרופונין לבבי רגישות במיוחד (hs-cTn) מאפשרות כיום לגלות אפילו "
                "נזקי מיוקרד קטנים. במדריך זה תלמדו מהו <strong>טווח הנורמה של "
                "טרופונין</strong>, מהם הגורמים ל<strong>טרופונין גבוה</strong> ומתי יש לפנות "
                "לטיפול רפואי.</p>"
                "<p>רמות טרופונין נחשבות לסמן הביוכימי האמין ביותר לנזק לשריר הלב. פרשנות "
                "נכונה דורשת התאמה לתמונה הקלינית, ממצאי אק\"ג ומדידות סדרתיות — תוצאת "
                "טרופונין בודדת אינה אבחנתית כשלעצמה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של טרופונין",
            body_html=(
                "<p><strong>טווח הנורמה של טרופונין</strong> משתנה בהתאם לסוג הבדיקה "
                "(קונבנציונלית לעומת רגישה במיוחד) ולמעבדה. הנחיות קליניות מגדירות את "
                "האחוזון ה-99 של אוכלוסיית ייחוס בריאה כגבול הייחוס העליון לכל בדיקת "
                "<strong>טרופונין לבבי</strong>. ערכים מעל סף זה מרמזים על נזק למיוקרד.</p>"
                "<p>הטבלה שלהלן מסכמת את ערכי הייחוס של בדיקות <strong>טרופונין I</strong> "
                "ו<strong>טרופונין T</strong> הנפוצות ביותר:</p>"
                + _TROP_TABLE_HE +
                "<p>בדיקות רגישות במיוחד משתמשות בסף ספציפי למין — ערכים שונים לנשים "
                "ולגברים — מה שמשפר את דיוק האבחון. השוו תמיד את התוצאה שלכם לטווח הייחוס "
                "המופיע בדוח המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות טרופונין גבוהות",
            body_html=(
                "<p><strong>טרופונין גבוה</strong> לא תמיד פירושו התקף לב קלאסי. נזק "
                "למיוקרד יכול להתרחש במצבים קליניים רבים. הגורמים העיקריים לעליית "
                "<strong>רמות הטרופונין</strong> כוללים:</p>"
                "<ul>"
                "<li><strong>אוטם חריף של שריר הלב (התקף לב):</strong> חסימה של עורק "
                "כלילי מונעת אספקת חמצן לשריר הלב והיא הגורם הדחוף והחשוב ביותר לעליית "
                "טרופונין.</li>"
                "<li><strong>דלקת שריר הלב (מיוקרדיטיס):</strong> דלקת של שריר הלב ממקור "
                "ויראלי או אוטואימוני עלולה להעלות באופן משמעותי את רמות הטרופונין.</li>"
                "<li><strong>תסחיף ריאתי (PE):</strong> קריש דם בעורקי הריאה עלול להעמיס "
                "על החדר הימני ולגרום לעליית טרופונין.</li>"
                "<li><strong>אי-ספיקת כליות:</strong> במחלת כליות כרונית, ירידה בפינוי "
                "הטרופונין ועקה לבבית נלווית עלולים לשמור על רמות טרופונין גבוהות באופן "
                "כרוני.</li>"
                "<li><strong>אלח דם (ספסיס):</strong> זיהום חמור עלול לגרום לדלקת מערכתית "
                "ולירידת לחץ דם, ובכך לנזק מיוקרדיאלי ולעליית טרופונין.</li>"
                "<li><strong>אי-ספיקת לב וקרדיומיופתיה:</strong> עומס מיוקרדיאלי מתמשך "
                "באי-ספיקת לב כרונית עלול לגרום לעליות קלות בטרופונין.</li>"
                "</ul>"
                "<p>המפתח לאבחון הוא דפוס שינוי הטרופונין לאורך זמן — עלייה ו/או ירידה. "
                "מדידות טרופונין סדרתיות, ולא ערך בודד, הן תקן הזהב להבחנה בין אוטם חריף "
                "של שריר הלב לבין עלייה כרונית.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם אתם חווים כאב חזה, קוצר נשימה, כאב המקרין לזרוע שמאל או ללסת, "
                "הזעה קרה או עייפות פתאומית, פנו מיד לחדר מיון. תסמינים אלה עלולים לרמז על "
                "אוטם חריף של שריר הלב (התקף לב), והערכה מהירה באמצעות <strong>בדיקת "
                "טרופונין</strong> עשויה להציל חיים.</p>"
                "<p>אם תוצאת הטרופונין שלכם גבוהה, אל תיבהלו אך שתפו את התוצאה עם קרדיולוג "
                "ללא דיחוי. <strong>טרופונין גבוה</strong> הוא ממצא שיש להעריך במגוון רחב — "
                "מהתקף לב ומיוקרדיטיס ועד תסחיף ריאתי ואי-ספיקת כליות. הרופא שלכם ישתמש "
                "באק\"ג, באקו-לב ובמדידות טרופונין סדרתיות כדי להבהיר את התמונה הקלינית.</p>"
                "<p>זכרו: תוצאת טרופונין בפני עצמה אינה אבחנה. אבחנה מדויקת מושגת כאשר "
                "שוקלים יחד את הסימפטומים הקליניים, שינויי אק\"ג וממצאי הדמיה. התייעצו תמיד "
                "עם הרופא שלכם במקום להסתמך על חיפושים באינטרנט בלבד.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hindi
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="ट्रोपोनिन ब्लड टेस्ट: आपकी रिपोर्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>ट्रोपोनिन टेस्ट</strong> रक्त में <strong>कार्डिएक ट्रोपोनिन</strong> "
                "प्रोटीन के स्तर को मापता है — ये प्रोटीन हृदय की मांसपेशी कोशिकाओं के "
                "क्षतिग्रस्त होने पर रक्त में छोड़े जाते हैं। क्लिनिकल प्रैक्टिस में दो उपप्रकार "
                "उपयोग किए जाते हैं: <strong>ट्रोपोनिन I</strong> और <strong>ट्रोपोनिन T</strong>। "
                "स्वस्थ व्यक्तियों में ये प्रोटीन बहुत कम मात्रा में होते हैं; जब मायोकार्डियल "
                "इंजरी होती है, तो <strong>ट्रोपोनिन लेवल</strong> तेज़ी से बढ़ जाता है।</p>"
                "<p>इमरजेंसी विभागों में <strong>ट्रोपोनिन टेस्ट</strong> छाती में दर्द वाले "
                "मरीज़ों में मायोकार्डियल इन्फ्रैक्शन (हार्ट अटैक) की पुष्टि या निषेध के लिए "
                "प्रयोग किया जाने वाला प्राथमिक <strong>हार्ट अटैक ब्लड टेस्ट</strong> है। "
                "हाई-सेंसिटिविटी कार्डिएक ट्रोपोनिन (hs-cTn) परीक्षण अब मामूली मायोकार्डियल "
                "डैमेज का भी पता लगा सकते हैं। इस गाइड में आप <strong>ट्रोपोनिन नॉर्मल "
                "रेंज</strong>, <strong>हाई ट्रोपोनिन</strong> के कारण और डॉक्टर से कब मिलना "
                "चाहिए, यह जानेंगे।</p>"
                "<p>ट्रोपोनिन लेवल को हृदय की मांसपेशी की चोट का सबसे विश्वसनीय बायोकेमिकल "
                "मार्कर माना जाता है। सही व्याख्या के लिए क्लिनिकल तस्वीर, ईसीजी निष्कर्षों "
                "और सीरियल माप के साथ तुलना ज़रूरी है — अकेला ट्रोपोनिन रिज़ल्ट डायग्नोस्टिक "
                "नहीं होता।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ट्रोपोनिन के नॉर्मल वैल्यू",
            body_html=(
                "<p><strong>ट्रोपोनिन नॉर्मल रेंज</strong> उपयोग किए गए टेस्ट (कन्वेंशनल बनाम "
                "हाई-सेंसिटिविटी) और लैब के अनुसार भिन्न होती है। क्लिनिकल गाइडलाइंस स्वस्थ "
                "रेफ़रेंस आबादी के 99वें परसेंटाइल को प्रत्येक <strong>कार्डिएक ट्रोपोनिन</strong> "
                "टेस्ट की ऊपरी संदर्भ सीमा के रूप में परिभाषित करती हैं। इस सीमा से ऊपर के मान "
                "मायोकार्डियल इंजरी का संकेत देते हैं।</p>"
                "<p>नीचे दी गई तालिका में सबसे आम <strong>ट्रोपोनिन I</strong> और "
                "<strong>ट्रोपोनिन T</strong> परीक्षणों के रेफ़रेंस वैल्यू दिए गए हैं:</p>"
                + _TROP_TABLE_HI +
                "<p>हाई-सेंसिटिविटी परीक्षणों में लिंग-विशिष्ट कट-ऑफ होते हैं — महिलाओं और "
                "पुरुषों के लिए अलग-अलग सीमाएँ — जो डायग्नोस्टिक सटीकता बढ़ाती हैं। अपने "
                "रिज़ल्ट की तुलना हमेशा अपनी लैब रिपोर्ट पर छपी रेफ़रेंस रेंज से करें।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई ट्रोपोनिन के कारण",
            body_html=(
                "<p><strong>हाई ट्रोपोनिन</strong> हमेशा क्लासिक हार्ट अटैक नहीं होता। "
                "मायोकार्डियल इंजरी कई क्लिनिकल स्थितियों में हो सकती है। "
                "<strong>ट्रोपोनिन लेवल</strong> बढ़ने के प्रमुख कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>एक्यूट मायोकार्डियल इन्फ्रैक्शन (हार्ट अटैक):</strong> कोरोनरी "
                "आर्टरी में रुकावट से हृदय की मांसपेशी को ऑक्सीजन नहीं मिलती और यह ट्रोपोनिन "
                "बढ़ने का सबसे ज़रूरी और महत्वपूर्ण कारण है।</li>"
                "<li><strong>मायोकार्डिटिस:</strong> वायरल या ऑटोइम्यून कारणों से हृदय की "
                "मांसपेशी में सूजन ट्रोपोनिन लेवल को काफ़ी बढ़ा सकती है।</li>"
                "<li><strong>पल्मोनरी एम्बोलिज़्म (PE):</strong> फेफड़ों की धमनियों में खून "
                "का थक्का दाएँ वेंट्रिकल पर दबाव डालकर ट्रोपोनिन बढ़ा सकता है।</li>"
                "<li><strong>किडनी फ़ेल्योर:</strong> क्रोनिक किडनी डिज़ीज़ में ट्रोपोनिन "
                "क्लीयरेंस कम होने और साथ में कार्डिएक स्ट्रेस के कारण ट्रोपोनिन लेवल लंबे "
                "समय तक बढ़ा रह सकता है।</li>"
                "<li><strong>सेप्सिस:</strong> गंभीर इंफेक्शन में सिस्टेमिक इन्फ़्लेमेशन और "
                "हाइपोटेंशन से मायोकार्डियल डैमेज और ट्रोपोनिन बढ़ सकता है।</li>"
                "<li><strong>हार्ट फ़ेल्योर और कार्डियोमायोपैथी:</strong> क्रोनिक हार्ट "
                "फ़ेल्योर में लगातार मायोकार्डियल स्ट्रेन से ट्रोपोनिन में हल्की वृद्धि हो "
                "सकती है।</li>"
                "</ul>"
                "<p>निदान की कुंजी समय के साथ ट्रोपोनिन में बदलाव का पैटर्न है — बढ़ना और/या "
                "गिरना। एक अकेले मान की बजाय सीरियल ट्रोपोनिन माप, एक्यूट मायोकार्डियल "
                "इन्फ्रैक्शन को क्रोनिक एलिवेशन से अलग करने का गोल्ड स्टैंडर्ड है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपको छाती में दर्द, सांस की तकलीफ़, बाएँ हाथ या जबड़े में फैलने वाला "
                "दर्द, ठंडा पसीना या अचानक थकान महसूस हो, तो तुरंत इमरजेंसी विभाग जाएँ। ये "
                "लक्षण एक्यूट मायोकार्डियल इन्फ्रैक्शन (हार्ट अटैक) का संकेत हो सकते हैं और "
                "<strong>ट्रोपोनिन टेस्ट</strong> के ज़रिए तेज़ मूल्यांकन जान बचा सकता है।</p>"
                "<p>अगर आपका ट्रोपोनिन रिज़ल्ट बढ़ा हुआ आता है, तो घबराएँ नहीं लेकिन तुरंत "
                "किसी कार्डियोलॉजिस्ट से रिज़ल्ट साझा करें। <strong>हाई ट्रोपोनिन</strong> एक "
                "ऐसा निष्कर्ष है जिसे हार्ट अटैक और मायोकार्डिटिस से लेकर पल्मोनरी एम्बोलिज़्म "
                "और किडनी फ़ेल्योर तक के व्यापक स्पेक्ट्रम में मूल्यांकन करना ज़रूरी है। आपके "
                "डॉक्टर ईसीजी, इकोकार्डियोग्राफ़ी और सीरियल ट्रोपोनिन माप से क्लिनिकल तस्वीर "
                "स्पष्ट करेंगे।</p>"
                "<p>याद रखें: अकेला ट्रोपोनिन रिज़ल्ट निदान नहीं है। सही निदान तभी होता है जब "
                "क्लिनिकल लक्षण, ईसीजी परिवर्तन और इमेजिंग निष्कर्षों को एक साथ देखा जाए। "
                "इंटरनेट रिसर्च पर निर्भर रहने की बजाय हमेशा अपने डॉक्टर से सलाह लें।</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Arabic
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="اختبار التروبونين في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>يقيس <strong>اختبار التروبونين</strong> مستوى بروتينات "
                "<strong>التروبونين القلبي</strong> في الدم — وهي بروتينات تُطلَق عندما تتضرر "
                "خلايا عضلة القلب. يُستخدم في الممارسة السريرية نوعان فرعيان: "
                "<strong>تروبونين I</strong> و<strong>تروبونين T</strong>. عند الأشخاص "
                "الأصحاء تدور هذه البروتينات بتركيزات منخفضة جداً؛ وعند حدوث إصابة في "
                "عضلة القلب ترتفع <strong>مستويات التروبونين</strong> بشكل ملحوظ.</p>"
                "<p>في أقسام الطوارئ، يُعدّ <strong>اختبار التروبونين</strong> "
                "<strong>تحليل الدم للنوبة القلبية</strong> الأول الذي يُستخدم لتأكيد أو "
                "نفي احتشاء عضلة القلب لدى المرضى الذين يعانون من ألم في الصدر. تتيح "
                "فحوصات التروبونين القلبي عالية الحساسية (hs-cTn) الآن اكتشاف حتى الأضرار "
                "الطفيفة في عضلة القلب. في هذا الدليل ستتعرفون على <strong>المستوى الطبيعي "
                "للتروبونين</strong>، وأسباب <strong>ارتفاع التروبونين</strong>، ومتى يجب "
                "طلب الرعاية الطبية.</p>"
                "<p>تُعتبر مستويات التروبونين المؤشر البيوكيميائي الأكثر موثوقية لإصابة "
                "عضلة القلب. يتطلب التفسير الصحيح ربطها بالصورة السريرية ونتائج تخطيط القلب "
                "والقياسات المتسلسلة — نتيجة تروبونين واحدة وحدها ليست تشخيصية.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية للتروبونين",
            body_html=(
                "<p>يختلف <strong>المستوى الطبيعي للتروبونين</strong> باختلاف نوع الفحص "
                "(تقليدي أو عالي الحساسية) والمختبر. تحدّد الإرشادات السريرية المئين 99 "
                "لسكان مرجعيين أصحاء كحد مرجعي أعلى لكل اختبار <strong>تروبونين "
                "قلبي</strong>. القيم فوق هذا الحد تشير إلى إصابة في عضلة القلب.</p>"
                "<p>يلخّص الجدول أدناه القيم المرجعية لفحوصات <strong>تروبونين I</strong> "
                "و<strong>تروبونين T</strong> الأكثر استخداماً:</p>"
                + _TROP_TABLE_AR +
                "<p>تستخدم الفحوصات عالية الحساسية عتبات مختلفة حسب الجنس — حدود منفصلة "
                "للنساء والرجال — مما يحسّن دقة التشخيص. قارنوا دائماً نتيجتكم بالنطاق "
                "المرجعي المطبوع على تقرير المختبر الخاص بكم.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع التروبونين",
            body_html=(
                "<p><strong>ارتفاع التروبونين</strong> لا يعني دائماً نوبة قلبية كلاسيكية. "
                "يمكن أن تحدث إصابة عضلة القلب في سياقات سريرية عديدة. الأسباب الرئيسية "
                "لارتفاع <strong>مستويات التروبونين</strong> تشمل:</p>"
                "<ul>"
                "<li><strong>احتشاء عضلة القلب الحاد (النوبة القلبية):</strong> انسداد أحد "
                "الشرايين التاجية يحرم عضلة القلب من الأكسجين وهو السبب الأكثر إلحاحاً "
                "وأهمية لارتفاع التروبونين.</li>"
                "<li><strong>التهاب عضلة القلب (الميوكارديتيس):</strong> التهاب عضلة القلب "
                "بسبب فيروسي أو مناعي ذاتي يمكن أن يرفع مستويات التروبونين بشكل ملحوظ.</li>"
                "<li><strong>الانصمام الرئوي (PE):</strong> جلطة دموية في الشرايين الرئوية "
                "قد تُثقل كاهل البطين الأيمن وتسبب ارتفاعاً في التروبونين.</li>"
                "<li><strong>الفشل الكلوي:</strong> في مرض الكلى المزمن، قد يؤدي انخفاض "
                "تصفية التروبونين والإجهاد القلبي المصاحب إلى إبقاء المستويات مرتفعة "
                "بشكل مزمن.</li>"
                "<li><strong>الإنتان (تعفن الدم):</strong> العدوى الشديدة قد تسبب التهاباً "
                "جهازياً وانخفاضاً في ضغط الدم، مما يؤدي إلى تلف عضلة القلب وارتفاع "
                "التروبونين.</li>"
                "<li><strong>قصور القلب واعتلال عضلة القلب:</strong> الإجهاد المستمر لعضلة "
                "القلب في قصور القلب المزمن قد يُنتج ارتفاعات طفيفة في التروبونين.</li>"
                "</ul>"
                "<p>العنصر الأساسي في التشخيص هو نمط تغيّر التروبونين عبر الزمن — ارتفاع "
                "و/أو انخفاض. القياسات المتسلسلة للتروبونين، وليس قيمة واحدة، هي المعيار "
                "الذهبي للتمييز بين احتشاء عضلة القلب الحاد والارتفاع المزمن.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كنتم تعانون من ألم في الصدر أو ضيق في التنفس أو ألم يمتد إلى "
                "الذراع اليسرى أو الفك أو تعرّق بارد أو إرهاق مفاجئ، توجّهوا فوراً إلى "
                "قسم الطوارئ. هذه الأعراض قد تشير إلى احتشاء حاد في عضلة القلب (نوبة "
                "قلبية)، والتقييم السريع عبر <strong>اختبار التروبونين</strong> قد يكون "
                "منقذاً للحياة.</p>"
                "<p>إذا جاءت نتيجة التروبونين مرتفعة، لا تقلقوا لكن شاركوا النتيجة مع "
                "طبيب قلب دون تأخير. <strong>ارتفاع التروبونين</strong> هو علامة يجب "
                "تقييمها عبر طيف واسع — من النوبة القلبية والتهاب عضلة القلب إلى الانصمام "
                "الرئوي والفشل الكلوي. سيستخدم طبيبكم تخطيط القلب وتصوير القلب بالصدى "
                "وقياسات التروبونين المتسلسلة لتوضيح الصورة السريرية.</p>"
                "<p>تذكّروا: نتيجة التروبونين وحدها ليست تشخيصاً. يتم التوصل إلى تشخيص "
                "دقيق عندما تُؤخذ الأعراض السريرية وتغيرات تخطيط القلب ونتائج التصوير "
                "معاً بعين الاعتبار. استشيروا دائماً طبيبكم بدلاً من الاعتماد على بحث "
                "الإنترنت فقط.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_troponin_sections_by_lang() -> dict:
    """Returns sections dict for Troponin article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_troponin_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Troponin article (all 9 languages, 3 Q&A each)."""
    return {
        "tr": [
            {"question": "Troponin testi nedir?",
             "answer": "Troponin testi, kalp kası hücrelerinde bulunan kardiyak troponin proteinlerinin kandaki düzeyini ölçen bir kan testidir. Akut miyokard enfarktüsünü (kalp krizi) doğrulamak veya dışlamak için acil servislerde ilk başvurulan laboratuvar testidir."},
            {"question": "Troponin normal değeri kaçtır?",
             "answer": "Konvansiyonel troponin I için normal sınır genellikle 0,04 ng/mL altı, troponin T için 0,01 ng/mL altıdır. Yüksek duyarlıklı testlerde hs-cTnT için 14 ng/L, hs-cTnI için kadınlarda 26 ng/L ve erkeklerde 34 ng/L 99. persentil sınır değerleri olarak kabul edilir."},
            {"question": "Troponin yüksekliği kalp krizi mi demektir?",
             "answer": "Her zaman değil. Troponin yüksekliği kalp krizi dışında miyokardit, pulmoner emboli, böbrek yetmezliği, sepsis ve kalp yetmezliği gibi durumlarda da görülebilir. Doğru tanı için seri troponin ölçümleri, EKG ve klinik değerlendirme birlikte yapılmalıdır."},
        ],
        "en": [
            {"question": "What is a troponin test?",
             "answer": "A troponin test is a blood test that measures the level of cardiac troponin proteins released when heart-muscle cells are damaged. It is the first-line heart attack blood test used in emergency departments to confirm or rule out myocardial infarction."},
            {"question": "What is the normal troponin range?",
             "answer": "For conventional troponin I the upper limit is generally below 0.04 ng/mL, and for troponin T below 0.01 ng/mL. High-sensitivity assays define the 99th percentile at 14 ng/L for hs-cTnT, and at 26 ng/L (women) or 34 ng/L (men) for hs-cTnI."},
            {"question": "Does high troponin always mean a heart attack?",
             "answer": "Not always. Elevated troponin can also result from myocarditis, pulmonary embolism, renal failure, sepsis, and heart failure. An accurate diagnosis requires serial troponin measurements, an ECG, and a full clinical assessment."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de troponina?",
             "answer": "La prueba de troponina es un análisis de sangre que mide el nivel de proteínas de troponina cardíaca liberadas cuando las células del músculo cardíaco se dañan. Es el análisis de sangre de primera línea para infarto utilizado en urgencias para confirmar o descartar un infarto de miocardio."},
            {"question": "¿Cuál es el rango normal de troponina?",
             "answer": "Para la troponina I convencional el límite superior suele ser inferior a 0,04 ng/mL y para la troponina T inferior a 0,01 ng/mL. Los ensayos de alta sensibilidad establecen el percentil 99 en 14 ng/L para hs-cTnT y en 26 ng/L (mujeres) o 34 ng/L (hombres) para hs-cTnI."},
            {"question": "¿La troponina alta siempre significa un infarto?",
             "answer": "No siempre. La troponina elevada también puede deberse a miocarditis, embolia pulmonar, insuficiencia renal, sepsis e insuficiencia cardíaca. Un diagnóstico preciso requiere mediciones seriadas de troponina, un ECG y una evaluación clínica completa."},
        ],
        "de": [
            {"question": "Was ist ein Troponin-Test?",
             "answer": "Ein Troponin-Test ist eine Blutuntersuchung, die den Spiegel kardialer Troponin-Proteine misst, die bei einer Schädigung der Herzmuskelzellen freigesetzt werden. Er ist der Herzinfarkt-Bluttest der ersten Wahl in Notaufnahmen, um einen Myokardinfarkt zu bestätigen oder auszuschließen."},
            {"question": "Was sind die Troponin-Normalwerte?",
             "answer": "Beim konventionellen Troponin I liegt die Obergrenze in der Regel unter 0,04 ng/mL, beim Troponin T unter 0,01 ng/mL. Hochsensitive Tests definieren die 99. Perzentile bei 14 ng/L für hs-cTnT und bei 26 ng/L (Frauen) bzw. 34 ng/L (Männer) für hs-cTnI."},
            {"question": "Bedeutet erhöhtes Troponin immer einen Herzinfarkt?",
             "answer": "Nicht immer. Erhöhte Troponinwerte können auch durch Myokarditis, Lungenembolie, Nierenversagen, Sepsis und Herzinsuffizienz verursacht werden. Eine korrekte Diagnose erfordert serielle Troponin-Messungen, ein EKG und eine vollständige klinische Beurteilung."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'un test de troponine ?",
             "answer": "Le test de troponine est une analyse de sang qui mesure le taux de protéines de troponine cardiaque libérées lors d'une lésion des cellules du muscle cardiaque. C'est l'analyse de sang de première intention pour l'infarctus utilisée aux urgences pour confirmer ou exclure un infarctus du myocarde."},
            {"question": "Quelles sont les valeurs normales de troponine ?",
             "answer": "Pour la troponine I conventionnelle, la limite supérieure est généralement inférieure à 0,04 ng/mL, et pour la troponine T inférieure à 0,01 ng/mL. Les dosages ultrasensibles fixent le 99e percentile à 14 ng/L pour la hs-cTnT, et à 26 ng/L (femmes) ou 34 ng/L (hommes) pour la hs-cTnI."},
            {"question": "Une troponine élevée signifie-t-elle toujours un infarctus ?",
             "answer": "Pas toujours. Une troponine élevée peut également résulter d'une myocardite, d'une embolie pulmonaire, d'une insuffisance rénale, d'un sepsis ou d'une insuffisance cardiaque. Un diagnostic précis nécessite des dosages sériés de troponine, un ECG et une évaluation clinique complète."},
        ],
        "it": [
            {"question": "Cos'è il test della troponina?",
             "answer": "Il test della troponina è un esame del sangue che misura il livello delle proteine di troponina cardiaca rilasciate quando le cellule del muscolo cardiaco subiscono un danno. È l'esame del sangue di prima linea per l'infarto, utilizzato nei pronto soccorso per confermare o escludere un infarto miocardico."},
            {"question": "Quali sono i valori normali di troponina?",
             "answer": "Per la troponina I convenzionale il limite superiore è generalmente inferiore a 0,04 ng/mL, per la troponina T inferiore a 0,01 ng/mL. I dosaggi ad alta sensibilità definiscono il 99° percentile a 14 ng/L per la hs-cTnT e a 26 ng/L (donne) o 34 ng/L (uomini) per la hs-cTnI."},
            {"question": "La troponina alta significa sempre un infarto?",
             "answer": "Non sempre. La troponina elevata può anche essere causata da miocardite, embolia polmonare, insufficienza renale, sepsi e insufficienza cardiaca. Una diagnosi accurata richiede misurazioni seriali della troponina, un ECG e una valutazione clinica completa."},
        ],
        "he": [
            {"question": "מהי בדיקת טרופונין?",
             "answer": "בדיקת טרופונין היא בדיקת דם המודדת את רמת חלבוני הטרופונין הלבבי המשתחררים כאשר תאי שריר הלב נפגעים. זוהי בדיקת הדם הראשונית לאבחון אוטם שריר הלב בחדרי מיון."},
            {"question": "מהו ערך הנורמה של טרופונין?",
             "answer": "עבור טרופונין I קונבנציונלי הגבול העליון הוא בדרך כלל מתחת ל-0.04 ng/mL, ועבור טרופונין T מתחת ל-0.01 ng/mL. בדיקות רגישות במיוחד מגדירות את האחוזון ה-99 ב-14 ng/L עבור hs-cTnT, וב-26 ng/L (נשים) או 34 ng/L (גברים) עבור hs-cTnI."},
            {"question": "האם טרופונין גבוה תמיד פירושו התקף לב?",
             "answer": "לא תמיד. טרופונין גבוה יכול לנבוע גם ממיוקרדיטיס, תסחיף ריאתי, אי-ספיקת כליות, אלח דם ואי-ספיקת לב. אבחון מדויק דורש מדידות טרופונין סדרתיות, אק\"ג והערכה קלינית מלאה."},
        ],
        "hi": [
            {"question": "ट्रोपोनिन टेस्ट क्या है?",
             "answer": "ट्रोपोनिन टेस्ट एक ब्लड टेस्ट है जो हृदय की मांसपेशी कोशिकाओं के क्षतिग्रस्त होने पर रिलीज़ होने वाले कार्डिएक ट्रोपोनिन प्रोटीन के स्तर को मापता है। यह मायोकार्डियल इन्फ्रैक्शन (हार्ट अटैक) की पुष्टि या निषेध के लिए इमरजेंसी विभागों में उपयोग किया जाने वाला प्राथमिक हार्ट अटैक ब्लड टेस्ट है।"},
            {"question": "ट्रोपोनिन की नॉर्मल रेंज क्या है?",
             "answer": "कन्वेंशनल ट्रोपोनिन I की ऊपरी सीमा आम तौर पर 0.04 ng/mL से कम और ट्रोपोनिन T की 0.01 ng/mL से कम होती है। हाई-सेंसिटिविटी परीक्षण 99वें परसेंटाइल को hs-cTnT के लिए 14 ng/L और hs-cTnI के लिए 26 ng/L (महिला) या 34 ng/L (पुरुष) पर परिभाषित करते हैं।"},
            {"question": "क्या हाई ट्रोपोनिन हमेशा हार्ट अटैक होता है?",
             "answer": "हमेशा नहीं। ट्रोपोनिन बढ़ने के अन्य कारणों में मायोकार्डिटिस, पल्मोनरी एम्बोलिज़्म, किडनी फ़ेल्योर, सेप्सिस और हार्ट फ़ेल्योर शामिल हैं। सही निदान के लिए सीरियल ट्रोपोनिन माप, ईसीजी और पूर्ण क्लिनिकल मूल्यांकन आवश्यक है।"},
        ],
        "ar": [
            {"question": "ما هو اختبار التروبونين؟",
             "answer": "اختبار التروبونين هو تحليل دم يقيس مستوى بروتينات التروبونين القلبي التي تُطلَق عندما تتضرر خلايا عضلة القلب. وهو تحليل الدم الأول المستخدم في أقسام الطوارئ لتأكيد أو نفي احتشاء عضلة القلب."},
            {"question": "ما هو المستوى الطبيعي للتروبونين؟",
             "answer": "بالنسبة للتروبونين I التقليدي يكون الحد الأعلى عادةً أقل من 0.04 ng/mL، وللتروبونين T أقل من 0.01 ng/mL. تحدّد الفحوصات عالية الحساسية المئين 99 عند 14 ng/L للـ hs-cTnT، وعند 26 ng/L (نساء) أو 34 ng/L (رجال) للـ hs-cTnI."},
            {"question": "هل ارتفاع التروبونين يعني دائماً نوبة قلبية؟",
             "answer": "ليس دائماً. يمكن أن ينتج ارتفاع التروبونين أيضاً عن التهاب عضلة القلب أو الانصمام الرئوي أو الفشل الكلوي أو الإنتان أو قصور القلب. يتطلب التشخيص الدقيق قياسات متسلسلة للتروبونين وتخطيط قلب وتقييماً سريرياً شاملاً."},
        ],
    }
