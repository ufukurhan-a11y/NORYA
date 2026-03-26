# -*- coding: utf-8 -*-
"""
Amylase blog article — full body content for all 9 languages.
Used by blog_i18n._article_amylase().
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

_AMY_TABLE_TR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Grup</th>"
    f"<th {_TH}>Amilaz Normal Aralığı</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Yetişkinler (serum)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>Pankreatik amilaz (P-amilaz)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>İdrar amilaz</td>"
    f"<td {_TD}>24–408 U/L (24 saat)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_EN = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Group</th>"
    f"<th {_TH}>Amylase Normal Range</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Adults (serum)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>Pancreatic amylase (P-amylase)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>Urine amylase</td>"
    f"<td {_TD}>24–408 U/L (24-hour)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_ES = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Grupo</th>"
    f"<th {_TH}>Rango normal de amilasa</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Adultos (suero)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>Amilasa pancreática (P-amilasa)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>Amilasa en orina</td>"
    f"<td {_TD}>24–408 U/L (24 horas)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_DE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Gruppe</th>"
    f"<th {_TH}>Amylase-Normalbereich</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Erwachsene (Serum)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>Pankreas-Amylase (P-Amylase)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>Urin-Amylase</td>"
    f"<td {_TD}>24–408 U/L (24 Stunden)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_FR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Groupe</th>"
    f"<th {_TH}>Amylase — plage normale</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Adultes (sérum)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>Amylase pancréatique (P-amylase)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>Amylase urinaire</td>"
    f"<td {_TD}>24–408 U/L (24 heures)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_IT = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Gruppo</th>"
    f"<th {_TH}>Range normale dell'amilasi</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Adulti (siero)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>Amilasi pancreatica (P-amilasi)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>Amilasi urinaria</td>"
    f"<td {_TD}>24–408 U/L (24 ore)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_HE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>קבוצה</th>"
    f"<th {_TH_RTL}>טווח נורמלי של עמילאז</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>מבוגרים (סרום)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>עמילאז לבלבי (P-amylase)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>עמילאז בשתן</td>"
    f"<td {_TD}>24–408 U/L ‏(24 שעות)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_HI = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>समूह</th>"
    f"<th {_TH}>एमाइलेज़ नॉर्मल रेंज</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>वयस्क (सीरम)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>पैंक्रिएटिक एमाइलेज़ (P-amylase)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>यूरिन एमाइलेज़</td>"
    f"<td {_TD}>24–408 U/L (24 घंटे)</td></tr>"
    "</tbody></table>"
)

_AMY_TABLE_AR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>المجموعة</th>"
    f"<th {_TH_RTL}>النطاق الطبيعي للأميلاز</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>البالغون (مصل الدم)</td>"
    f"<td {_TD}>28–100 U/L</td></tr>"
    f"<tr><td {_TD}>الأميلاز البنكرياسي (P-amylase)</td>"
    f"<td {_TD}>13–53 U/L</td></tr>"
    f"<tr><td {_TD}>أميلاز البول</td>"
    f"<td {_TD}>24–408 U/L ‏(24 ساعة)</td></tr>"
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
            heading="Amilaz kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>Amilaz testi</strong>, nişastayı parçalayan bir sindirim enzimi olan "
                "<strong>amilaz</strong> düzeyini kanda ölçen bir laboratuvar testidir. Amilaz "
                "başlıca pankreas ve tükürük bezlerinde üretilir; bu nedenle <strong>pankreatik "
                "amilaz</strong> ve tükürük (salivary) amilaz olmak üzere iki ana izoformu vardır. "
                "Sağlıklı bireylerde <strong>amilaz düzeyleri</strong> düşük ve stabil seyreder; "
                "pankreas ya da tükürük bezi hasarı oluştuğunda ise belirgin şekilde yükselir.</p>"
                "<p><strong>Amilaz kan testi</strong>, özellikle akut pankreatit şüphesinde ilk "
                "istenen testlerden biridir. Lipaz testiyle birlikte değerlendirildiğinde pankreatit "
                "tanısında duyarlılık artar. Lipaz pankreasa daha özgüdür, ancak amilaz daha erken "
                "yükselip daha erken normale döner ve tükürük bezi kaynaklı patolojileri de "
                "yakalar. Bu rehberde <strong>amilaz normal değerleri</strong>, <strong>yüksek "
                "amilaz</strong> nedenlerini ve ne zaman doktora başvurmanız gerektiğini "
                "öğreneceksiniz.</p>"
                "<p>Amilaz düzeylerinin doğru yorumlanması klinik semptomlar, lipaz düzeyi ve "
                "görüntüleme bulguları ile birlikte yapılmalıdır. Tek başına bir amilaz sonucu "
                "kesin tanı koydurmaz; yükseklik veya düşüklük her zaman altta yatan nedeni "
                "araştırmayı gerektirir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Amilaz normal değerleri",
            body_html=(
                "<p><strong>Amilaz normal aralığı</strong> kullanılan test yöntemine ve "
                "laboratuvara göre farklılık gösterebilir. Genel olarak yetişkinler için serum "
                "amilazı 28–100 U/L kabul edilir. Pankreasa özgü <strong>pankreatik "
                "amilaz</strong> (P-amilaz) alt fraksiyonu ise 13–53 U/L aralığında "
                "değerlendirilir.</p>"
                "<p>Aşağıdaki tabloda yaygın referans değerleri özetlenmiştir:</p>"
                + _AMY_TABLE_TR +
                "<p>Amilaz düzeyinin normalin üç katından fazla yükselmesi akut pankreatit "
                "açısından güçlü bir göstergedir. Ancak pankreatit şiddetiyle amilaz düzeyi "
                "arasında doğrusal bir ilişki yoktur; hafif vakalarda çok yüksek değerler "
                "görülebilirken, ağır nekrotizan pankreatitte pankreas dokusu harap olduğu için "
                "amilaz paradoks olarak düşük kalabilir. Sonuçlarınızı her zaman kendi laboratuvar "
                "raporunuzdaki referans aralığıyla karşılaştırın.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Amilaz yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Yüksek amilaz</strong> birçok farklı klinik durumda ortaya çıkabilir. "
                "<strong>Amilaz düzeyleri</strong> yalnızca pankreas hastalıklarında değil, "
                "tükürük bezi ve gastrointestinal patolojilerde de yükselir. Başlıca nedenler "
                "şunlardır:</p>"
                "<ul>"
                "<li><strong>Akut pankreatit:</strong> Amilaz yüksekliğinin en sık ve en önemli "
                "nedenidir. Genellikle semptom başlangıcından 6–12 saat sonra yükselir ve 3–5 "
                "günde normale döner. Lipaz ile birlikte değerlendirilmesi tanıyı güçlendirir.</li>"
                "<li><strong>Kronik pankreatit:</strong> İlerleyen pankreas hasarı nedeniyle amilaz "
                "hafif yükselebilir veya pankreas atrofisine bağlı olarak paradoks şekilde normal "
                "ya da düşük kalabilir.</li>"
                "<li><strong>Tükürük bezi hastalıkları:</strong> Kabakulak (parotit), tükürük bezi "
                "taşları (sialolitiyaz) ve sialadenit gibi durumlarda tükürük amilazı belirgin "
                "şekilde artar.</li>"
                "<li><strong>Bağırsak tıkanıklığı (ileus):</strong> Mekanik veya paralitik "
                "intestinal obstrüksiyonda amilaz düzeyleri yükselebilir.</li>"
                "<li><strong>Diyabetik ketoasidoz (DKA):</strong> DKA sırasında metabolik "
                "değişiklikler ve hafif pankreatik inflamasyon amilaz artışına yol açabilir.</li>"
                "<li><strong>Makroamilazemi:</strong> Amilazın immünoglobulinlerle kompleks "
                "oluşturarak böbreklerden atılamaması sonucu serumda birikmesidir. Klinik olarak "
                "zararsızdır ancak yanlış tanıya yol açabilir; idrar amilazının düşük olması "
                "tanıda yardımcıdır.</li>"
                "</ul>"
                "<p><strong>Yüksek amilaz</strong> saptandığında lipaz düzeyi, karaciğer "
                "fonksiyon testleri ve karın görüntülemesi (ultrason, BT) ile birlikte "
                "değerlendirilmesi doğru tanıya ulaşmak için kritik öneme sahiptir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Şiddetli üst karın ağrısı (özellikle sırta yayılan), bulantı, kusma ve "
                "ateş gibi belirtiler yaşıyorsanız derhal acil servise başvurun. Bu semptomlar "
                "akut pankreatitin habercisi olabilir ve erken müdahale komplikasyon riskini "
                "önemli ölçüde azaltır.</p>"
                "<p><strong>Amilaz testi</strong> yüksek çıktıysa panik yapmayın ancak sonucu "
                "mutlaka bir gastroenteroloji uzmanıyla paylaşın. Yüksek amilaz pankreatitten "
                "tükürük bezi hastalıklarına, bağırsak tıkanıklığından makroamilazemiye kadar "
                "geniş bir yelpazede değerlendirilmesi gereken bir bulgudur. Doktorunuz lipaz "
                "testi, karın ultrasonografisi veya bilgisayarlı tomografi ile klinik tabloyu "
                "netleştirecektir.</p>"
                "<p>Unutmayın: amilaz sonucu tek başına tanı koymaz. Klinik semptomlar, lipaz "
                "düzeyi ve görüntüleme bulguları ile birlikte değerlendirildiğinde doğru tanıya "
                "ulaşılır. Bilgi amaçlı internet araştırması yerine mutlaka hekiminize "
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
            heading="Amylase blood test: what your results mean",
            body_html=(
                "<p>The <strong>amylase test</strong> measures the blood level of "
                "<strong>amylase</strong>, a digestive enzyme that breaks down starch. Amylase "
                "is produced primarily by the pancreas and the salivary glands; accordingly, two "
                "main isoforms exist — <strong>pancreatic amylase</strong> (P-amylase) and "
                "salivary amylase (S-amylase). In healthy individuals, <strong>amylase "
                "levels</strong> remain low and stable; when the pancreas or salivary glands are "
                "damaged, levels rise sharply.</p>"
                "<p>The <strong>amylase blood test</strong> is one of the first tests ordered "
                "when acute pancreatitis is suspected. When evaluated alongside lipase — an "
                "enzyme more specific to the pancreas — diagnostic sensitivity for pancreatitis "
                "increases. Amylase rises earlier and returns to normal sooner than lipase, and "
                "it also detects salivary-gland pathology. In this guide you will learn the "
                "<strong>amylase normal range</strong>, the causes of <strong>high "
                "amylase</strong>, and when to seek medical attention.</p>"
                "<p>Accurate interpretation of <strong>amylase levels</strong> requires "
                "correlation with clinical symptoms, the lipase level, and imaging findings. A "
                "single amylase result alone is not diagnostic — any elevation or decrease "
                "warrants investigation of the underlying cause.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Amylase normal range",
            body_html=(
                "<p>The <strong>amylase normal range</strong> may vary depending on the assay "
                "method and the laboratory. In general, the accepted adult serum amylase range "
                "is 28–100 U/L. The pancreas-specific fraction, <strong>pancreatic "
                "amylase</strong> (P-amylase), is typically evaluated at 13–53 U/L.</p>"
                "<p>The table below summarises common reference values:</p>"
                + _AMY_TABLE_EN +
                "<p>A serum amylase level more than three times the upper limit of normal is a "
                "strong indicator of acute pancreatitis. However, there is no linear correlation "
                "between the severity of pancreatitis and the amylase level; mild cases may show "
                "very high values, while in severe necrotising pancreatitis the amylase may "
                "paradoxically remain low because the pancreatic tissue is destroyed. Always "
                "compare your result with the reference range on your own laboratory report.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high amylase levels",
            body_html=(
                "<p><strong>High amylase</strong> can arise in many clinical settings. "
                "<strong>Amylase levels</strong> rise not only in pancreatic diseases but also "
                "in salivary-gland and gastrointestinal pathologies. The main causes of "
                "<strong>elevated amylase</strong> include:</p>"
                "<ul>"
                "<li><strong>Acute pancreatitis:</strong> The most common and most important "
                "cause of elevated amylase. Levels typically rise 6–12 hours after symptom "
                "onset and return to normal within 3–5 days. Co-evaluation with lipase "
                "strengthens the diagnosis.</li>"
                "<li><strong>Chronic pancreatitis:</strong> Ongoing pancreatic damage may cause "
                "mildly elevated amylase, or — paradoxically — normal or low values when the "
                "gland becomes atrophic.</li>"
                "<li><strong>Salivary gland disease:</strong> Mumps (parotitis), salivary "
                "stones (sialolithiasis), and sialadenitis raise salivary amylase "
                "significantly.</li>"
                "<li><strong>Bowel obstruction (ileus):</strong> Mechanical or paralytic "
                "intestinal obstruction can elevate amylase levels.</li>"
                "<li><strong>Diabetic ketoacidosis (DKA):</strong> Metabolic derangements and "
                "mild pancreatic inflammation during DKA may increase amylase.</li>"
                "<li><strong>Macroamylasaemia:</strong> Amylase forms complexes with "
                "immunoglobulins that are too large for renal filtration, causing serum "
                "accumulation. It is clinically benign but can lead to misdiagnosis; a low "
                "urine amylase aids differentiation.</li>"
                "</ul>"
                "<p>When <strong>elevated amylase</strong> is detected, evaluation alongside "
                "the lipase level, liver function tests, and abdominal imaging (ultrasound, CT) "
                "is critical for reaching the correct diagnosis.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If you experience severe upper-abdominal pain — especially pain radiating "
                "to the back — nausea, vomiting, and fever, go to an emergency department "
                "immediately. These symptoms may herald acute pancreatitis, and early "
                "intervention significantly reduces the risk of complications.</p>"
                "<p>If your <strong>amylase test</strong> comes back elevated, do not panic but "
                "share the result with a gastroenterologist without delay. <strong>High "
                "amylase</strong> is a finding that must be evaluated across a wide spectrum — "
                "from pancreatitis and salivary gland disease to bowel obstruction and "
                "macroamylasaemia. Your doctor will use a lipase test, abdominal ultrasound, "
                "or computed tomography to clarify the clinical picture.</p>"
                "<p>Remember: an amylase result on its own is not a diagnosis. An accurate "
                "diagnosis is reached when clinical symptoms, the lipase level, and imaging "
                "findings are considered together. Always consult your physician rather than "
                "relying on internet research alone.</p>"
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
            heading="Prueba de amilasa en sangre: qué significan sus resultados",
            body_html=(
                "<p>La <strong>prueba de amilasa</strong> mide el nivel en sangre de la "
                "<strong>amilasa</strong>, una enzima digestiva que descompone el almidón. La "
                "amilasa se produce principalmente en el páncreas y en las glándulas salivales; "
                "por ello existen dos isoformas principales: la <strong>amilasa "
                "pancreática</strong> (P-amilasa) y la amilasa salival (S-amilasa). En personas "
                "sanas, los <strong>niveles de amilasa</strong> se mantienen bajos y estables; "
                "cuando el páncreas o las glándulas salivales se dañan, los niveles se elevan de "
                "forma notable.</p>"
                "<p>La <strong>prueba de amilasa en sangre</strong> es una de las primeras que "
                "se solicita ante la sospecha de pancreatitis aguda. Cuando se evalúa junto con "
                "la lipasa — una enzima más específica del páncreas — la sensibilidad diagnóstica "
                "para la pancreatitis aumenta. La amilasa se eleva antes y vuelve a la normalidad "
                "más rápido que la lipasa, y también detecta patologías de las glándulas salivales. "
                "En esta guía conocerá el <strong>rango normal de amilasa</strong>, las causas de "
                "la <strong>amilasa alta</strong> y cuándo buscar atención médica.</p>"
                "<p>La interpretación correcta de los <strong>niveles de amilasa</strong> requiere "
                "la correlación con los síntomas clínicos, el nivel de lipasa y los hallazgos de "
                "imagen. Un resultado aislado de amilasa no es diagnóstico; cualquier elevación o "
                "descenso justifica la investigación de la causa subyacente.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de amilasa",
            body_html=(
                "<p>El <strong>rango normal de amilasa</strong> puede variar según el método "
                "de ensayo y el laboratorio. En general, la amilasa sérica aceptada para adultos "
                "oscila entre 28 y 100 U/L. La fracción específica del páncreas, la "
                "<strong>amilasa pancreática</strong> (P-amilasa), se evalúa típicamente en un "
                "rango de 13–53 U/L.</p>"
                "<p>La siguiente tabla resume los valores de referencia habituales:</p>"
                + _AMY_TABLE_ES +
                "<p>Un nivel de amilasa sérica superior a tres veces el límite superior de la "
                "normalidad es un indicador sólido de pancreatitis aguda. Sin embargo, no existe "
                "una correlación lineal entre la gravedad de la pancreatitis y el nivel de "
                "amilasa; en casos leves pueden observarse valores muy altos, mientras que en la "
                "pancreatitis necrosante grave la amilasa puede permanecer paradójicamente baja "
                "porque el tejido pancreático está destruido. Compare siempre su resultado con "
                "el rango de referencia de su propio informe de laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de amilasa alta",
            body_html=(
                "<p>La <strong>amilasa alta</strong> puede presentarse en múltiples contextos "
                "clínicos. Los <strong>niveles de amilasa</strong> se elevan no solo en "
                "enfermedades pancreáticas, sino también en patologías de las glándulas salivales "
                "y gastrointestinales. Las principales causas de <strong>amilasa elevada</strong> "
                "incluyen:</p>"
                "<ul>"
                "<li><strong>Pancreatitis aguda:</strong> Es la causa más frecuente e importante "
                "de amilasa elevada. Los niveles suelen aumentar entre 6 y 12 horas después del "
                "inicio de los síntomas y se normalizan en 3–5 días. La evaluación conjunta con "
                "la lipasa refuerza el diagnóstico.</li>"
                "<li><strong>Pancreatitis crónica:</strong> El daño pancreático progresivo puede "
                "producir una elevación leve de la amilasa o, paradójicamente, valores normales "
                "o bajos cuando la glándula se atrofia.</li>"
                "<li><strong>Enfermedades de las glándulas salivales:</strong> Las paperas "
                "(parotiditis), los cálculos salivales (sialolitiasis) y la sialoadenitis "
                "elevan significativamente la amilasa salival.</li>"
                "<li><strong>Obstrucción intestinal (íleo):</strong> La obstrucción intestinal "
                "mecánica o paralítica puede elevar los niveles de amilasa.</li>"
                "<li><strong>Cetoacidosis diabética (CAD):</strong> Las alteraciones metabólicas "
                "y la inflamación pancreática leve durante la CAD pueden aumentar la amilasa.</li>"
                "<li><strong>Macroamilasemia:</strong> La amilasa forma complejos con "
                "inmunoglobulinas demasiado grandes para la filtración renal, acumulándose en el "
                "suero. Es clínicamente benigna pero puede llevar a un diagnóstico erróneo; una "
                "amilasa urinaria baja ayuda a diferenciarla.</li>"
                "</ul>"
                "<p>Cuando se detecta <strong>amilasa elevada</strong>, la evaluación junto con "
                "el nivel de lipasa, las pruebas de función hepática y la imagen abdominal "
                "(ecografía, TC) es fundamental para llegar al diagnóstico correcto.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si experimenta dolor abdominal superior intenso — especialmente dolor que "
                "se irradia a la espalda —, náuseas, vómitos y fiebre, acuda de inmediato a un "
                "servicio de urgencias. Estos síntomas pueden indicar una pancreatitis aguda y "
                "la intervención temprana reduce significativamente el riesgo de "
                "complicaciones.</p>"
                "<p>Si su <strong>prueba de amilasa</strong> resulta elevada, no se alarme, "
                "pero comparta el resultado con un gastroenterólogo sin demora. La "
                "<strong>amilasa alta</strong> es un hallazgo que debe evaluarse en un amplio "
                "espectro — desde la pancreatitis y las enfermedades de las glándulas salivales "
                "hasta la obstrucción intestinal y la macroamilasemia. Su médico utilizará una "
                "prueba de lipasa, una ecografía abdominal o una tomografía computarizada para "
                "esclarecer el cuadro clínico.</p>"
                "<p>Recuerde: un resultado de amilasa por sí solo no constituye un diagnóstico. "
                "Se llega al diagnóstico correcto cuando se consideran en conjunto los síntomas "
                "clínicos, el nivel de lipasa y los hallazgos de imagen. Consulte siempre a su "
                "médico en lugar de confiar únicamente en búsquedas en internet.</p>"
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
            heading="Amylase-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>Amylase-Test</strong> misst den Blutspiegel der "
                "<strong>Amylase</strong>, eines Verdauungsenzyms, das Stärke abbaut. Amylase "
                "wird hauptsächlich in der Bauchspeicheldrüse und den Speicheldrüsen produziert; "
                "dementsprechend gibt es zwei Hauptisoformen: <strong>Pankreas-Amylase</strong> "
                "(P-Amylase) und Speichel-Amylase (S-Amylase). Bei gesunden Personen bleiben die "
                "<strong>Amylasewerte</strong> niedrig und stabil; bei einer Schädigung der "
                "Bauchspeicheldrüse oder der Speicheldrüsen steigen sie deutlich an.</p>"
                "<p>Der <strong>Amylase-Bluttest</strong> gehört zu den ersten Untersuchungen, "
                "die bei Verdacht auf eine akute Pankreatitis angeordnet werden. In Kombination "
                "mit der Lipase — einem pankreasspezifischeren Enzym — steigt die diagnostische "
                "Sensitivität für Pankreatitis. Amylase steigt früher an und normalisiert sich "
                "schneller als Lipase und erfasst zusätzlich Speicheldrüsenerkrankungen. In "
                "diesem Ratgeber erfahren Sie die <strong>Amylase-Normalwerte</strong>, die "
                "Ursachen für <strong>erhöhte Amylase</strong> und wann Sie ärztliche Hilfe "
                "suchen sollten.</p>"
                "<p>Eine korrekte Interpretation der <strong>Amylasewerte</strong> erfordert die "
                "Zusammenschau mit klinischen Symptomen, dem Lipase-Spiegel und "
                "Bildgebungsbefunden. Ein einzelner Amylase-Wert allein ist nicht diagnostisch "
                "— jede Erhöhung oder Erniedrigung erfordert die Abklärung der Ursache.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Amylase-Normalwerte",
            body_html=(
                "<p>Der <strong>Amylase-Normalbereich</strong> kann je nach Testmethode und "
                "Labor variieren. Im Allgemeinen gilt für Erwachsene ein Serum-Amylase-Bereich "
                "von 28–100 U/L. Die pankreasspezifische Fraktion, die <strong>Pankreas-"
                "Amylase</strong> (P-Amylase), wird typischerweise im Bereich von 13–53 U/L "
                "bewertet.</p>"
                "<p>Die folgende Tabelle fasst gängige Referenzwerte zusammen:</p>"
                + _AMY_TABLE_DE +
                "<p>Ein Serum-Amylase-Spiegel, der das Dreifache der oberen Normgrenze "
                "übersteigt, ist ein starker Hinweis auf eine akute Pankreatitis. Es besteht "
                "jedoch kein linearer Zusammenhang zwischen dem Schweregrad der Pankreatitis "
                "und dem Amylasewert; bei leichten Fällen können sehr hohe Werte auftreten, "
                "während bei schwerer nekrotisierender Pankreatitis die Amylase paradoxerweise "
                "niedrig bleiben kann, weil das Pankreasgewebe zerstört ist. Vergleichen Sie "
                "Ihr Ergebnis stets mit dem Referenzbereich auf Ihrem eigenen Laborbefund.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für erhöhte Amylasewerte",
            body_html=(
                "<p><strong>Erhöhte Amylase</strong> kann in vielen klinischen Situationen "
                "auftreten. Die <strong>Amylasewerte</strong> steigen nicht nur bei "
                "Pankreaserkrankungen, sondern auch bei Speicheldrüsen- und gastrointestinalen "
                "Pathologien. Die wichtigsten Ursachen für <strong>erhöhte Amylase</strong> "
                "sind:</p>"
                "<ul>"
                "<li><strong>Akute Pankreatitis:</strong> Die häufigste und wichtigste Ursache "
                "für eine Amylase-Erhöhung. Die Werte steigen in der Regel 6–12 Stunden nach "
                "Symptombeginn und normalisieren sich innerhalb von 3–5 Tagen. Die gleichzeitige "
                "Beurteilung mit der Lipase stärkt die Diagnose.</li>"
                "<li><strong>Chronische Pankreatitis:</strong> Fortschreitende Pankreasschädigung "
                "kann zu leicht erhöhter Amylase führen — oder paradoxerweise zu normalen oder "
                "niedrigen Werten, wenn die Drüse atrophiert.</li>"
                "<li><strong>Speicheldrüsenerkrankungen:</strong> Mumps (Parotitis), "
                "Speichelsteine (Sialolithiasis) und Sialadenitis erhöhen die Speichel-Amylase "
                "deutlich.</li>"
                "<li><strong>Darmverschluss (Ileus):</strong> Ein mechanischer oder paralytischer "
                "Darmverschluss kann die Amylasewerte erhöhen.</li>"
                "<li><strong>Diabetische Ketoazidose (DKA):</strong> Metabolische Entgleisungen "
                "und eine leichte Pankreasentzündung bei DKA können die Amylase steigern.</li>"
                "<li><strong>Makroamylasämie:</strong> Amylase bildet Komplexe mit "
                "Immunglobulinen, die zu groß für die renale Filtration sind und sich im Serum "
                "anreichern. Klinisch ist sie harmlos, kann jedoch zu Fehldiagnosen führen; eine "
                "niedrige Urin-Amylase hilft bei der Abgrenzung.</li>"
                "</ul>"
                "<p>Wird eine <strong>erhöhte Amylase</strong> festgestellt, ist die "
                "Beurteilung zusammen mit dem Lipase-Spiegel, Leberfunktionstests und "
                "abdomineller Bildgebung (Ultraschall, CT) entscheidend für die richtige "
                "Diagnose.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Sie starke Oberbauchschmerzen — insbesondere in den Rücken "
                "ausstrahlend —, Übelkeit, Erbrechen und Fieber verspüren, suchen Sie sofort "
                "eine Notaufnahme auf. Diese Symptome können auf eine akute Pankreatitis "
                "hindeuten, und eine frühzeitige Behandlung senkt das Komplikationsrisiko "
                "erheblich.</p>"
                "<p>Wenn Ihr <strong>Amylase-Test</strong> erhöht ausfällt, bewahren Sie Ruhe, "
                "teilen Sie das Ergebnis aber unverzüglich einem Gastroenterologen mit. "
                "<strong>Erhöhte Amylase</strong> muss in einem breiten Spektrum bewertet "
                "werden — von Pankreatitis und Speicheldrüsenerkrankungen über Darmverschluss "
                "bis hin zur Makroamylasämie. Ihr Arzt wird einen Lipase-Test, eine "
                "Abdomensonografie oder eine Computertomografie heranziehen, um das klinische "
                "Bild zu klären.</p>"
                "<p>Denken Sie daran: Ein Amylase-Ergebnis allein stellt keine Diagnose. "
                "Eine zutreffende Diagnose ergibt sich erst aus der Zusammenschau von "
                "klinischen Symptomen, Lipase-Spiegel und Bildgebungsbefunden. Besprechen Sie "
                "Ihre Ergebnisse stets mit Ihrem Arzt, anstatt sich allein auf "
                "Internetrecherchen zu verlassen.</p>"
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
            heading="Test d'amylase sanguine : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test d'amylase</strong> mesure le taux sanguin de "
                "l'<strong>amylase</strong>, une enzyme digestive qui dégrade l'amidon. "
                "L'amylase est principalement produite par le pancréas et les glandes "
                "salivaires ; il existe donc deux isoformes principales : l'<strong>amylase "
                "pancréatique</strong> (P-amylase) et l'amylase salivaire (S-amylase). Chez "
                "les sujets sains, les <strong>taux d'amylase</strong> restent bas et stables ; "
                "en cas de lésion du pancréas ou des glandes salivaires, ils augmentent de façon "
                "marquée.</p>"
                "<p>Le <strong>test d'amylase sanguine</strong> fait partie des premiers examens "
                "prescrits en cas de suspicion de pancréatite aiguë. Associé à la lipase — une "
                "enzyme plus spécifique du pancréas — la sensibilité diagnostique pour la "
                "pancréatite augmente. L'amylase s'élève plus tôt et revient à la normale plus "
                "rapidement que la lipase, et elle détecte également les pathologies des glandes "
                "salivaires. Dans ce guide, vous découvrirez les <strong>valeurs normales "
                "d'amylase</strong>, les causes d'une <strong>amylase élevée</strong> et quand "
                "consulter un médecin.</p>"
                "<p>L'interprétation correcte des <strong>taux d'amylase</strong> nécessite une "
                "corrélation avec les symptômes cliniques, le taux de lipase et les résultats "
                "d'imagerie. Un résultat isolé d'amylase ne constitue pas un diagnostic — toute "
                "élévation ou diminution justifie la recherche de la cause sous-jacente.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales d'amylase",
            body_html=(
                "<p>Les <strong>valeurs normales d'amylase</strong> peuvent varier selon la "
                "méthode de dosage et le laboratoire. En règle générale, la plage normale de "
                "l'amylase sérique chez l'adulte est de 28–100 U/L. La fraction spécifique du "
                "pancréas, l'<strong>amylase pancréatique</strong> (P-amylase), est généralement "
                "évaluée dans une plage de 13–53 U/L.</p>"
                "<p>Le tableau ci-dessous résume les valeurs de référence courantes :</p>"
                + _AMY_TABLE_FR +
                "<p>Un taux d'amylase sérique supérieur à trois fois la limite supérieure de "
                "la normale est un indicateur fort de pancréatite aiguë. Cependant, il n'existe "
                "pas de corrélation linéaire entre la sévérité de la pancréatite et le taux "
                "d'amylase ; des cas bénins peuvent afficher des valeurs très élevées, tandis "
                "que dans la pancréatite nécrosante sévère l'amylase peut paradoxalement rester "
                "basse en raison de la destruction du tissu pancréatique. Comparez toujours "
                "votre résultat avec l'intervalle de référence figurant sur votre propre compte "
                "rendu de laboratoire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une amylase élevée",
            body_html=(
                "<p>Une <strong>amylase élevée</strong> peut survenir dans de nombreux contextes "
                "cliniques. Les <strong>taux d'amylase</strong> s'élèvent non seulement dans les "
                "maladies pancréatiques, mais aussi dans les pathologies des glandes salivaires "
                "et gastro-intestinales. Les principales causes d'<strong>amylase élevée</strong> "
                "sont :</p>"
                "<ul>"
                "<li><strong>Pancréatite aiguë :</strong> La cause la plus fréquente et la plus "
                "importante d'élévation de l'amylase. Les taux augmentent généralement 6 à "
                "12 heures après le début des symptômes et se normalisent en 3 à 5 jours. "
                "L'évaluation conjointe avec la lipase renforce le diagnostic.</li>"
                "<li><strong>Pancréatite chronique :</strong> Les lésions pancréatiques "
                "progressives peuvent entraîner une légère élévation de l'amylase ou, "
                "paradoxalement, des valeurs normales ou basses lorsque la glande s'atrophie.</li>"
                "<li><strong>Maladies des glandes salivaires :</strong> Les oreillons "
                "(parotidite), les calculs salivaires (sialolithiase) et la sialadénite "
                "augmentent significativement l'amylase salivaire.</li>"
                "<li><strong>Occlusion intestinale (iléus) :</strong> Une obstruction "
                "intestinale mécanique ou paralytique peut élever les taux d'amylase.</li>"
                "<li><strong>Acidocétose diabétique (ACD) :</strong> Les perturbations "
                "métaboliques et l'inflammation pancréatique légère lors d'une ACD peuvent "
                "augmenter l'amylase.</li>"
                "<li><strong>Macroamylasémie :</strong> L'amylase forme des complexes avec des "
                "immunoglobulines trop volumineux pour la filtration rénale, s'accumulant dans "
                "le sérum. C'est cliniquement bénin mais peut conduire à un diagnostic erroné ; "
                "une amylase urinaire basse aide à la différenciation.</li>"
                "</ul>"
                "<p>Lorsqu'une <strong>amylase élevée</strong> est détectée, l'évaluation "
                "conjointe avec le taux de lipase, les tests de fonction hépatique et l'imagerie "
                "abdominale (échographie, TDM) est essentielle pour poser le bon diagnostic.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si vous ressentez une douleur abdominale haute intense — surtout irradiant "
                "dans le dos —, des nausées, des vomissements et de la fièvre, rendez-vous "
                "immédiatement aux urgences. Ces symptômes peuvent signaler une pancréatite "
                "aiguë, et une prise en charge précoce réduit considérablement le risque de "
                "complications.</p>"
                "<p>Si votre <strong>test d'amylase</strong> est élevé, ne paniquez pas mais "
                "partagez le résultat sans délai avec un gastro-entérologue. Une <strong>amylase "
                "élevée</strong> est un signe qui doit être évalué dans un large spectre — de la "
                "pancréatite et des maladies des glandes salivaires à l'occlusion intestinale et "
                "à la macroamylasémie. Votre médecin utilisera un dosage de la lipase, une "
                "échographie abdominale ou un scanner pour clarifier le tableau clinique.</p>"
                "<p>N'oubliez pas : un résultat d'amylase seul ne constitue pas un diagnostic. "
                "Un diagnostic précis repose sur l'association des symptômes cliniques, du taux "
                "de lipase et des résultats d'imagerie. Consultez toujours votre médecin plutôt "
                "que de vous fier uniquement à des recherches sur internet.</p>"
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
            heading="Test dell'amilasi nel sangue: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test dell'amilasi</strong> misura il livello ematico "
                "dell'<strong>amilasi</strong>, un enzima digestivo che scinde l'amido. L'amilasi "
                "è prodotta principalmente dal pancreas e dalle ghiandole salivari; pertanto "
                "esistono due isoforme principali: l'<strong>amilasi pancreatica</strong> "
                "(P-amilasi) e l'amilasi salivare (S-amilasi). Nelle persone sane, i "
                "<strong>livelli di amilasi</strong> restano bassi e stabili; quando il pancreas "
                "o le ghiandole salivari subiscono un danno, i livelli aumentano in modo "
                "significativo.</p>"
                "<p>Il <strong>test dell'amilasi nel sangue</strong> è uno dei primi esami "
                "richiesti in caso di sospetta pancreatite acuta. Quando valutato insieme alla "
                "lipasi — un enzima più specifico per il pancreas — la sensibilità diagnostica "
                "per la pancreatite aumenta. L'amilasi sale prima e torna alla normalità più "
                "rapidamente della lipasi, e rileva anche le patologie delle ghiandole salivari. "
                "In questa guida scoprirai i <strong>valori normali di amilasi</strong>, le "
                "cause dell'<strong>amilasi alta</strong> e quando rivolgersi al medico.</p>"
                "<p>Un'interpretazione corretta dei <strong>livelli di amilasi</strong> richiede "
                "la correlazione con i sintomi clinici, il livello di lipasi e i reperti di "
                "imaging. Un singolo risultato di amilasi non è diagnostico — qualsiasi "
                "elevazione o diminuzione richiede l'indagine della causa sottostante.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di amilasi",
            body_html=(
                "<p>I <strong>valori normali di amilasi</strong> possono variare in base al "
                "metodo di analisi e al laboratorio. In generale, il range sierico normale per "
                "gli adulti è 28–100 U/L. La frazione specifica del pancreas, l'<strong>amilasi "
                "pancreatica</strong> (P-amilasi), viene tipicamente valutata nell'intervallo "
                "13–53 U/L.</p>"
                "<p>La tabella seguente riassume i valori di riferimento comuni:</p>"
                + _AMY_TABLE_IT +
                "<p>Un livello sierico di amilasi superiore a tre volte il limite superiore della "
                "norma è un forte indicatore di pancreatite acuta. Tuttavia, non esiste una "
                "correlazione lineare tra la gravità della pancreatite e il livello di amilasi; "
                "casi lievi possono mostrare valori molto alti, mentre nella pancreatite "
                "necrotizzante grave l'amilasi può paradossalmente rimanere bassa perché il "
                "tessuto pancreatico è distrutto. Confronta sempre il tuo risultato con "
                "l'intervallo di riferimento indicato nel tuo referto di laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di amilasi alta",
            body_html=(
                "<p>L'<strong>amilasi alta</strong> può verificarsi in molti contesti clinici. "
                "I <strong>livelli di amilasi</strong> si innalzano non solo nelle malattie "
                "pancreatiche, ma anche nelle patologie delle ghiandole salivari e "
                "gastrointestinali. Le principali cause di <strong>amilasi elevata</strong> "
                "includono:</p>"
                "<ul>"
                "<li><strong>Pancreatite acuta:</strong> La causa più comune e più importante "
                "di amilasi elevata. I livelli generalmente aumentano 6–12 ore dopo l'esordio "
                "dei sintomi e si normalizzano entro 3–5 giorni. La valutazione congiunta con "
                "la lipasi rafforza la diagnosi.</li>"
                "<li><strong>Pancreatite cronica:</strong> Il danno pancreatico progressivo può "
                "causare una lieve elevazione dell'amilasi o, paradossalmente, valori normali "
                "o bassi quando la ghiandola diventa atrofica.</li>"
                "<li><strong>Malattie delle ghiandole salivari:</strong> La parotite (orecchioni), "
                "i calcoli salivari (scialolitiasi) e la scialoadenite innalzano "
                "significativamente l'amilasi salivare.</li>"
                "<li><strong>Ostruzione intestinale (ileo):</strong> Un'ostruzione intestinale "
                "meccanica o paralitica può elevare i livelli di amilasi.</li>"
                "<li><strong>Chetoacidosi diabetica (DKA):</strong> Le alterazioni metaboliche "
                "e la lieve infiammazione pancreatica durante la DKA possono aumentare "
                "l'amilasi.</li>"
                "<li><strong>Macroamilasemia:</strong> L'amilasi forma complessi con "
                "immunoglobuline troppo grandi per la filtrazione renale, accumulandosi nel "
                "siero. È clinicamente benigna ma può portare a diagnosi errate; un'amilasi "
                "urinaria bassa aiuta nella differenziazione.</li>"
                "</ul>"
                "<p>Quando viene rilevata un'<strong>amilasi elevata</strong>, la valutazione "
                "congiunta con il livello di lipasi, i test di funzionalità epatica e l'imaging "
                "addominale (ecografia, TC) è fondamentale per giungere alla diagnosi "
                "corretta.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se avverti un forte dolore addominale superiore — soprattutto se si irradia "
                "alla schiena —, nausea, vomito e febbre, recati immediatamente al pronto "
                "soccorso. Questi sintomi possono segnalare una pancreatite acuta, e un "
                "intervento precoce riduce significativamente il rischio di complicanze.</p>"
                "<p>Se il tuo <strong>test dell'amilasi</strong> risulta elevato, non allarmarti "
                "ma condividi il risultato senza indugio con un gastroenterologo. "
                "L'<strong>amilasi alta</strong> è un reperto che deve essere valutato in un "
                "ampio spettro — dalla pancreatite e dalle malattie delle ghiandole salivari "
                "all'ostruzione intestinale e alla macroamilasemia. Il tuo medico utilizzerà "
                "un dosaggio della lipasi, un'ecografia addominale o una TC per chiarire il "
                "quadro clinico.</p>"
                "<p>Ricorda: un risultato di amilasi da solo non è una diagnosi. Una diagnosi "
                "accurata si ottiene quando si considerano insieme i sintomi clinici, il livello "
                "di lipasi e i reperti di imaging. Consulta sempre il tuo medico anziché "
                "affidarti esclusivamente a ricerche su internet.</p>"
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
            heading="בדיקת עמילאז בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת עמילאז</strong> מודדת את רמת ה<strong>עמילאז</strong> בדם — "
                "אנזים עיכול המפרק עמילן. עמילאז מיוצר בעיקר בלבלב ובבלוטות הרוק; לכן קיימות "
                "שתי איזופורמות עיקריות: <strong>עמילאז לבלבי</strong> (P-amylase) ועמילאז רוקי "
                "(S-amylase). אצל אנשים בריאים <strong>רמות העמילאז</strong> נשארות נמוכות "
                "ויציבות; כאשר הלבלב או בלוטות הרוק נפגעים, הרמות עולות באופן ניכר.</p>"
                "<p><strong>בדיקת עמילאז בדם</strong> היא אחת הבדיקות הראשונות שנדרשות בחשד "
                "לדלקת לבלב חריפה. כאשר היא מוערכת לצד ליפאז — אנזים ספציפי יותר ללבלב — "
                "הרגישות האבחנתית לפנקראטיטיס עולה. עמילאז עולה מוקדם יותר וחוזר לנורמה מהר "
                "יותר מליפאז, והוא גם מזהה פתולוגיות של בלוטות הרוק. במדריך זה תלמדו מהו "
                "<strong>טווח הנורמה של עמילאז</strong>, מהם הגורמים ל<strong>עמילאז "
                "גבוה</strong> ומתי יש לפנות לטיפול רפואי.</p>"
                "<p>פרשנות נכונה של <strong>רמות העמילאז</strong> דורשת התאמה לסימפטומים "
                "קליניים, רמת הליפאז וממצאי הדמיה. תוצאת עמילאז בודדת אינה אבחנתית — כל "
                "עלייה או ירידה מצדיקה חקירת הגורם הבסיסי.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של עמילאז",
            body_html=(
                "<p><strong>טווח הנורמה של עמילאז</strong> עשוי להשתנות בהתאם לשיטת הבדיקה "
                "ולמעבדה. באופן כללי, טווח עמילאז הסרום המקובל למבוגרים הוא 28–100 U/L. "
                "הפרקציה הספציפית ללבלב, <strong>עמילאז לבלבי</strong> (P-amylase), מוערכת "
                "בדרך כלל בטווח של 13–53 U/L.</p>"
                "<p>הטבלה שלהלן מסכמת ערכי ייחוס נפוצים:</p>"
                + _AMY_TABLE_HE +
                "<p>רמת עמילאז בסרום הגבוהה פי שלושה מהגבול העליון של הנורמה היא מדד חזק "
                "לדלקת לבלב חריפה. עם זאת, אין קורלציה ליניארית בין חומרת הפנקראטיטיס לרמת "
                "העמילאז; במקרים קלים ייתכנו ערכים גבוהים מאוד, בעוד שבפנקראטיטיס נמקית "
                "חמורה העמילאז עלול באופן פרדוקסלי להישאר נמוך כי רקמת הלבלב הרוסה. השוו "
                "תמיד את התוצאה שלכם לטווח הייחוס המופיע בדוח המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות עמילאז גבוהות",
            body_html=(
                "<p><strong>עמילאז גבוה</strong> יכול להתרחש במצבים קליניים רבים. "
                "<strong>רמות העמילאז</strong> עולות לא רק במחלות לבלב אלא גם בפתולוגיות של "
                "בלוטות הרוק ומערכת העיכול. הגורמים העיקריים ל<strong>עמילאז מוגבר</strong> "
                "כוללים:</p>"
                "<ul>"
                "<li><strong>דלקת לבלב חריפה (פנקראטיטיס):</strong> הגורם השכיח והחשוב ביותר "
                "לעליית עמילאז. הרמות עולות בדרך כלל 6–12 שעות לאחר הופעת הסימפטומים וחוזרות "
                "לנורמה תוך 3–5 ימים. הערכה משולבת עם ליפאז מחזקת את האבחנה.</li>"
                "<li><strong>דלקת לבלב כרונית:</strong> נזק לבלבי מתקדם עלול לגרום לעליית "
                "עמילאז קלה או, באופן פרדוקסלי, לערכים תקינים או נמוכים כאשר הבלוטה "
                "מתנוונת.</li>"
                "<li><strong>מחלות בלוטות הרוק:</strong> חזרת (פרוטיטיס), אבני רוק "
                "(סיאלוליתיאזיס) וסיאלאדניטיס מעלות באופן משמעותי את עמילאז הרוק.</li>"
                "<li><strong>חסימת מעי (אילאוס):</strong> חסימת מעי מכנית או שיתוקית עלולה "
                "להעלות את רמות העמילאז.</li>"
                "<li><strong>חמצת קטונית סוכרתית (DKA):</strong> הפרעות מטבוליות ודלקת לבלבית "
                "קלה במהלך DKA עלולות להגביר את העמילאז.</li>"
                "<li><strong>מקרואמילאזמיה:</strong> עמילאז יוצר קומפלקסים עם אימונוגלובולינים "
                "גדולים מדי לסינון כלייתי, מה שגורם להצטברות בסרום. מצב זה שפיר קלינית אך "
                "עלול להוביל לאבחנה שגויה; עמילאז נמוך בשתן מסייע בהבחנה.</li>"
                "</ul>"
                "<p>כאשר מתגלה <strong>עמילאז מוגבר</strong>, הערכה לצד רמת הליפאז, בדיקות "
                "תפקודי כבד והדמיה בטנית (אולטרסאונד, CT) חיונית להגעה לאבחנה הנכונה.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם אתם חווים כאב עז בבטן העליונה — במיוחד כאב המקרין לגב —, בחילות, "
                "הקאות וחום, פנו מיד לחדר מיון. תסמינים אלה עלולים לרמז על דלקת לבלב חריפה, "
                "והתערבות מוקדמת מפחיתה באופן משמעותי את הסיכון לסיבוכים.</p>"
                "<p>אם תוצאת <strong>בדיקת העמילאז</strong> שלכם גבוהה, אל תיבהלו אך שתפו "
                "את התוצאה עם גסטרואנטרולוג ללא דיחוי. <strong>עמילאז גבוה</strong> הוא ממצא "
                "שיש להעריך במגוון רחב — מדלקת לבלב ומחלות בלוטות רוק ועד חסימת מעי "
                "ומקרואמילאזמיה. הרופא שלכם ישתמש בבדיקת ליפאז, אולטרסאונד בטני או CT כדי "
                "להבהיר את התמונה הקלינית.</p>"
                "<p>זכרו: תוצאת עמילאז בפני עצמה אינה אבחנה. אבחנה מדויקת מושגת כאשר "
                "שוקלים יחד את הסימפטומים הקליניים, רמת הליפאז וממצאי הדמיה. התייעצו תמיד עם "
                "הרופא שלכם במקום להסתמך על חיפושים באינטרנט בלבד.</p>"
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
            heading="एमाइलेज़ ब्लड टेस्ट: आपकी रिपोर्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>एमाइलेज़ टेस्ट</strong> रक्त में <strong>एमाइलेज़</strong> के "
                "स्तर को मापता है — यह एक पाचक एंज़ाइम है जो स्टार्च को तोड़ता है। एमाइलेज़ "
                "मुख्य रूप से अग्न्याशय (पैंक्रियास) और लार ग्रंथियों में बनता है; इसलिए दो "
                "प्रमुख आइसोफ़ॉर्म होते हैं — <strong>पैंक्रिएटिक एमाइलेज़</strong> "
                "(P-amylase) और सैलिवरी एमाइलेज़ (S-amylase)। स्वस्थ व्यक्तियों में "
                "<strong>एमाइलेज़ लेवल</strong> कम और स्थिर रहता है; जब पैंक्रियास या लार "
                "ग्रंथियाँ क्षतिग्रस्त होती हैं, तो स्तर तेज़ी से बढ़ जाता है।</p>"
                "<p><strong>एमाइलेज़ ब्लड टेस्ट</strong> एक्यूट पैंक्रिएटाइटिस की आशंका में "
                "सबसे पहले माँगी जाने वाली जाँचों में से एक है। जब लाइपेज़ — पैंक्रियास के "
                "लिए अधिक विशिष्ट एंज़ाइम — के साथ मूल्यांकन किया जाता है, तो पैंक्रिएटाइटिस "
                "के लिए डायग्नोस्टिक सेंसिटिविटी बढ़ जाती है। एमाइलेज़ लाइपेज़ से पहले "
                "बढ़ता है और जल्दी सामान्य होता है, और यह लार ग्रंथि की बीमारियों को भी "
                "पकड़ता है। इस गाइड में आप <strong>एमाइलेज़ नॉर्मल रेंज</strong>, "
                "<strong>हाई एमाइलेज़</strong> के कारण और डॉक्टर से कब मिलना चाहिए, यह "
                "जानेंगे।</p>"
                "<p><strong>एमाइलेज़ लेवल</strong> की सही व्याख्या के लिए क्लिनिकल लक्षणों, "
                "लाइपेज़ लेवल और इमेजिंग निष्कर्षों के साथ तुलना ज़रूरी है। अकेला एमाइलेज़ "
                "रिज़ल्ट डायग्नोस्टिक नहीं होता — किसी भी वृद्धि या कमी में अंतर्निहित "
                "कारण की जाँच आवश्यक है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="एमाइलेज़ के नॉर्मल वैल्यू",
            body_html=(
                "<p><strong>एमाइलेज़ नॉर्मल रेंज</strong> टेस्ट मेथड और लैब के अनुसार भिन्न "
                "हो सकती है। सामान्य तौर पर वयस्कों के लिए सीरम एमाइलेज़ 28–100 U/L मानी "
                "जाती है। पैंक्रियास-स्पेसिफ़िक फ़्रैक्शन, <strong>पैंक्रिएटिक "
                "एमाइलेज़</strong> (P-amylase), आमतौर पर 13–53 U/L के रेंज में आँकी "
                "जाती है।</p>"
                "<p>नीचे दी गई तालिका में सामान्य रेफ़रेंस वैल्यू दिए गए हैं:</p>"
                + _AMY_TABLE_HI +
                "<p>सीरम एमाइलेज़ का सामान्य ऊपरी सीमा से तीन गुना से अधिक बढ़ना एक्यूट "
                "पैंक्रिएटाइटिस का मज़बूत संकेत है। हालाँकि, पैंक्रिएटाइटिस की गंभीरता और "
                "एमाइलेज़ लेवल के बीच कोई रैखिक संबंध नहीं है; हल्के मामलों में बहुत ऊँचे "
                "मान दिख सकते हैं, जबकि गंभीर नेक्रोटाइज़िंग पैंक्रिएटाइटिस में एमाइलेज़ "
                "विरोधाभासी रूप से कम रह सकता है क्योंकि पैंक्रियास ऊतक नष्ट हो चुका होता "
                "है। अपने रिज़ल्ट की तुलना हमेशा अपनी लैब रिपोर्ट पर छपी रेफ़रेंस रेंज "
                "से करें।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई एमाइलेज़ के कारण",
            body_html=(
                "<p><strong>हाई एमाइलेज़</strong> कई क्लिनिकल स्थितियों में हो सकता है। "
                "<strong>एमाइलेज़ लेवल</strong> केवल पैंक्रियास की बीमारियों में नहीं बल्कि "
                "लार ग्रंथि और गैस्ट्रोइंटेस्टाइनल पैथोलॉजी में भी बढ़ता है। "
                "<strong>एमाइलेज़ बढ़ने</strong> के प्रमुख कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>एक्यूट पैंक्रिएटाइटिस:</strong> एमाइलेज़ बढ़ने का सबसे आम और "
                "सबसे महत्वपूर्ण कारण। लेवल आमतौर पर लक्षण शुरू होने के 6–12 घंटे बाद बढ़ता "
                "है और 3–5 दिनों में सामान्य हो जाता है। लाइपेज़ के साथ मिलकर मूल्यांकन "
                "डायग्नोसिस को मज़बूत करता है।</li>"
                "<li><strong>क्रोनिक पैंक्रिएटाइटिस:</strong> पैंक्रियास को लगातार नुकसान "
                "से एमाइलेज़ में हल्की वृद्धि हो सकती है — या विरोधाभासी रूप से ग्रंथि के "
                "एट्रॉफ़ी होने पर सामान्य या कम रह सकता है।</li>"
                "<li><strong>लार ग्रंथि रोग:</strong> मम्प्स (पैरोटाइटिस), लार ग्रंथि की "
                "पथरी (सियालोलिथियासिस) और सियालाडेनाइटिस सैलिवरी एमाइलेज़ को काफ़ी "
                "बढ़ाते हैं।</li>"
                "<li><strong>आंतों की रुकावट (इलियस):</strong> मैकेनिकल या पैरालिटिक आंतों "
                "की बाधा एमाइलेज़ लेवल बढ़ा सकती है।</li>"
                "<li><strong>डायबिटिक कीटोएसिडोसिस (DKA):</strong> DKA के दौरान मेटाबोलिक "
                "गड़बड़ी और हल्की पैंक्रिएटिक सूजन एमाइलेज़ बढ़ा सकती है।</li>"
                "<li><strong>मैक्रोएमाइलेज़ीमिया:</strong> एमाइलेज़ इम्युनोग्लोबुलिन के "
                "साथ कॉम्प्लेक्स बनाता है जो किडनी फ़िल्ट्रेशन के लिए बहुत बड़े होते हैं, "
                "जिससे सीरम में जमा हो जाता है। यह क्लिनिकली हानिरहित है लेकिन ग़लत निदान "
                "का कारण बन सकता है; यूरिन एमाइलेज़ का कम होना विभेदन में सहायक है।</li>"
                "</ul>"
                "<p>जब <strong>एमाइलेज़ बढ़ा हुआ</strong> पाया जाता है, तो लाइपेज़ लेवल, "
                "लिवर फ़ंक्शन टेस्ट और एब्डोमिनल इमेजिंग (अल्ट्रासाउंड, CT) के साथ "
                "मूल्यांकन सही निदान के लिए अत्यंत महत्वपूर्ण है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपको ऊपरी पेट में तेज़ दर्द — ख़ासकर पीठ की तरफ़ फैलने वाला —, "
                "जी मिचलाना, उल्टी और बुख़ार हो, तो तुरंत इमरजेंसी विभाग जाएँ। ये लक्षण "
                "एक्यूट पैंक्रिएटाइटिस का संकेत हो सकते हैं और जल्दी इलाज जटिलताओं का "
                "ख़तरा काफ़ी कम कर देता है।</p>"
                "<p>अगर आपका <strong>एमाइलेज़ टेस्ट</strong> बढ़ा हुआ आता है, तो घबराएँ "
                "नहीं लेकिन तुरंत किसी गैस्ट्रोएंटेरोलॉजिस्ट से रिज़ल्ट साझा करें। "
                "<strong>हाई एमाइलेज़</strong> एक ऐसा निष्कर्ष है जिसे पैंक्रिएटाइटिस और "
                "लार ग्रंथि रोगों से लेकर आंतों की रुकावट और मैक्रोएमाइलेज़ीमिया तक के "
                "व्यापक स्पेक्ट्रम में मूल्यांकन करना ज़रूरी है। आपके डॉक्टर लाइपेज़ टेस्ट, "
                "पेट का अल्ट्रासाउंड या CT से क्लिनिकल तस्वीर स्पष्ट करेंगे।</p>"
                "<p>याद रखें: अकेला एमाइलेज़ रिज़ल्ट निदान नहीं है। सही निदान तभी होता है "
                "जब क्लिनिकल लक्षण, लाइपेज़ लेवल और इमेजिंग निष्कर्षों को एक साथ देखा जाए। "
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
            heading="تحليل الأميلاز في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>يقيس <strong>تحليل الأميلاز</strong> مستوى <strong>الأميلاز</strong> في "
                "الدم — وهو إنزيم هضمي يفكّك النشا. يُنتَج الأميلاز بشكل رئيسي في البنكرياس "
                "والغدد اللعابية؛ لذلك توجد شكلتان إيزوية رئيسيتان: <strong>الأميلاز "
                "البنكرياسي</strong> (P-amylase) والأميلاز اللعابي (S-amylase). عند الأشخاص "
                "الأصحاء تبقى <strong>مستويات الأميلاز</strong> منخفضة ومستقرة؛ وعند تلف "
                "البنكرياس أو الغدد اللعابية ترتفع بشكل ملحوظ.</p>"
                "<p>يُعدّ <strong>تحليل الأميلاز في الدم</strong> من أولى الفحوصات المطلوبة "
                "عند الاشتباه بالتهاب البنكرياس الحاد. عند تقييمه مع الليباز — وهو إنزيم أكثر "
                "تخصصاً للبنكرياس — تزداد الحساسية التشخيصية لالتهاب البنكرياس. يرتفع "
                "الأميلاز أبكر ويعود إلى الطبيعي أسرع من الليباز، كما أنه يكشف أمراض الغدد "
                "اللعابية. في هذا الدليل ستتعرفون على <strong>المستوى الطبيعي "
                "للأميلاز</strong>، وأسباب <strong>ارتفاع الأميلاز</strong>، ومتى يجب طلب "
                "الرعاية الطبية.</p>"
                "<p>يتطلب التفسير الصحيح <strong>لمستويات الأميلاز</strong> ربطها بالأعراض "
                "السريرية ومستوى الليباز ونتائج التصوير. نتيجة أميلاز واحدة وحدها ليست "
                "تشخيصية — أي ارتفاع أو انخفاض يستدعي البحث عن السبب الكامن.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية للأميلاز",
            body_html=(
                "<p>قد يختلف <strong>المستوى الطبيعي للأميلاز</strong> حسب طريقة الفحص "
                "والمختبر. بشكل عام، يتراوح أميلاز المصل المقبول للبالغين بين 28 و100 "
                "وحدة/لتر. أما الجزء الخاص بالبنكرياس، <strong>الأميلاز البنكرياسي</strong> "
                "(P-amylase)، فيُقيَّم عادةً في نطاق 13–53 وحدة/لتر.</p>"
                "<p>يلخّص الجدول أدناه القيم المرجعية الشائعة:</p>"
                + _AMY_TABLE_AR +
                "<p>يُعدّ مستوى أميلاز المصل الذي يتجاوز ثلاثة أضعاف الحد الأعلى للطبيعي "
                "مؤشراً قوياً على التهاب البنكرياس الحاد. ومع ذلك لا توجد علاقة خطية بين "
                "شدة التهاب البنكرياس ومستوى الأميلاز؛ في الحالات الخفيفة قد تظهر قيم عالية "
                "جداً، بينما في التهاب البنكرياس النخري الشديد قد يبقى الأميلاز منخفضاً بشكل "
                "مفارق لأن نسيج البنكرياس مدمّر. قارنوا دائماً نتيجتكم بالنطاق المرجعي "
                "المطبوع على تقرير المختبر الخاص بكم.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع الأميلاز",
            body_html=(
                "<p><strong>ارتفاع الأميلاز</strong> يمكن أن يحدث في سياقات سريرية عديدة. "
                "ترتفع <strong>مستويات الأميلاز</strong> ليس فقط في أمراض البنكرياس بل أيضاً "
                "في أمراض الغدد اللعابية والجهاز الهضمي. الأسباب الرئيسية <strong>لارتفاع "
                "الأميلاز</strong> تشمل:</p>"
                "<ul>"
                "<li><strong>التهاب البنكرياس الحاد:</strong> السبب الأكثر شيوعاً وأهمية "
                "لارتفاع الأميلاز. ترتفع المستويات عادةً بعد 6–12 ساعة من بدء الأعراض وتعود "
                "للطبيعي خلال 3–5 أيام. التقييم المشترك مع الليباز يعزّز التشخيص.</li>"
                "<li><strong>التهاب البنكرياس المزمن:</strong> التلف المتقدم في البنكرياس قد "
                "يسبب ارتفاعاً طفيفاً في الأميلاز أو، بشكل مفارق، قيماً طبيعية أو منخفضة "
                "عندما تضمر الغدة.</li>"
                "<li><strong>أمراض الغدد اللعابية:</strong> النكاف (التهاب الغدة النكفية)، "
                "حصوات الغدد اللعابية (تحصّي اللعاب) والتهاب الغدد اللعابية ترفع الأميلاز "
                "اللعابي بشكل ملحوظ.</li>"
                "<li><strong>انسداد الأمعاء (العلوص):</strong> الانسداد المعوي الميكانيكي أو "
                "الشللي قد يرفع مستويات الأميلاز.</li>"
                "<li><strong>الحماض الكيتوني السكري (DKA):</strong> الاضطرابات الأيضية "
                "والالتهاب البنكرياسي الخفيف أثناء DKA قد يزيدان الأميلاز.</li>"
                "<li><strong>فرط أميلاز الدم الكبير (ماكروأميلازيميا):</strong> يشكّل الأميلاز "
                "معقّدات مع الغلوبولينات المناعية أكبر من أن تُرشَّح كلوياً، فتتراكم في "
                "المصل. هذه الحالة حميدة سريرياً لكنها قد تؤدي إلى تشخيص خاطئ؛ انخفاض "
                "أميلاز البول يساعد في التمييز.</li>"
                "</ul>"
                "<p>عند اكتشاف <strong>أميلاز مرتفع</strong>، يُعدّ التقييم بجانب مستوى "
                "الليباز واختبارات وظائف الكبد والتصوير البطني (الموجات فوق الصوتية، التصوير "
                "المقطعي) أمراً بالغ الأهمية للوصول إلى التشخيص الصحيح.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كنتم تعانون من ألم شديد في أعلى البطن — خاصةً ألم يمتد إلى الظهر —، "
                "وغثيان وقيء وحمّى، توجّهوا فوراً إلى قسم الطوارئ. هذه الأعراض قد تشير إلى "
                "التهاب بنكرياس حاد، والتدخل المبكر يقلّل بشكل كبير من خطر المضاعفات.</p>"
                "<p>إذا جاءت نتيجة <strong>تحليل الأميلاز</strong> مرتفعة، لا تقلقوا لكن "
                "شاركوا النتيجة مع طبيب جهاز هضمي دون تأخير. <strong>ارتفاع الأميلاز</strong> "
                "علامة يجب تقييمها عبر طيف واسع — من التهاب البنكرياس وأمراض الغدد اللعابية "
                "إلى انسداد الأمعاء وماكروأميلازيميا. سيستخدم طبيبكم اختبار الليباز والتصوير "
                "بالموجات فوق الصوتية أو التصوير المقطعي لتوضيح الصورة السريرية.</p>"
                "<p>تذكّروا: نتيجة الأميلاز وحدها ليست تشخيصاً. يتم التوصل إلى تشخيص دقيق "
                "عندما تُؤخذ الأعراض السريرية ومستوى الليباز ونتائج التصوير معاً بعين "
                "الاعتبار. استشيروا دائماً طبيبكم بدلاً من الاعتماد على بحث الإنترنت فقط.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_amylase_sections_by_lang() -> dict:
    """Returns sections dict for Amylase article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_amylase_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Amylase article (all 9 languages, 3 Q&A each)."""
    return {
        "tr": [
            {"question": "Amilaz testi nedir?",
             "answer": "Amilaz testi, nişastayı parçalayan bir sindirim enzimi olan amilazın kandaki düzeyini ölçen bir kan testidir. Özellikle akut pankreatit şüphesinde ilk başvurulan laboratuvar testlerinden biridir ve lipaz testi ile birlikte değerlendirilir."},
            {"question": "Amilaz normal değeri kaçtır?",
             "answer": "Yetişkinlerde serum amilazının normal aralığı genellikle 28–100 U/L'dir. Pankreatik amilaz (P-amilaz) alt fraksiyonu ise 13–53 U/L aralığında değerlendirilir. Sonuçlarınızı kendi laboratuvar raporunuzdaki referans değerleriyle karşılaştırın."},
            {"question": "Amilaz yüksekliği pankreatit mi demektir?",
             "answer": "Her zaman değil. Amilaz yüksekliği pankreatit dışında tükürük bezi hastalıkları, bağırsak tıkanıklığı, diyabetik ketoasidoz ve makroamilazemi gibi durumlarda da görülebilir. Doğru tanı için lipaz testi, karın görüntülemesi ve klinik değerlendirme birlikte yapılmalıdır."},
        ],
        "en": [
            {"question": "What is an amylase test?",
             "answer": "An amylase test is a blood test that measures the level of amylase, a digestive enzyme that breaks down starch. It is one of the first tests ordered when acute pancreatitis is suspected and is evaluated alongside lipase to support clearer clinical interpretation."},
            {"question": "What is the normal amylase range?",
             "answer": "The normal adult serum amylase range is generally 28–100 U/L. The pancreas-specific fraction, pancreatic amylase (P-amylase), is typically 13–53 U/L. Always compare your result with the reference range on your own laboratory report."},
            {"question": "Does high amylase always mean pancreatitis?",
             "answer": "Not always. Elevated amylase can also result from salivary gland disease, bowel obstruction, diabetic ketoacidosis, and macroamylasaemia. An accurate diagnosis requires a lipase test, abdominal imaging, and a full clinical assessment."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de amilasa?",
             "answer": "La prueba de amilasa es un análisis de sangre que mide el nivel de amilasa, una enzima digestiva que descompone el almidón. Es una de las primeras pruebas que se solicita ante la sospecha de pancreatitis aguda y se evalúa junto con la lipasa para mejorar la precisión diagnóstica."},
            {"question": "¿Cuál es el rango normal de amilasa?",
             "answer": "El rango normal de amilasa sérica en adultos es generalmente de 28–100 U/L. La fracción específica del páncreas, la amilasa pancreática (P-amilasa), suele ser de 13–53 U/L. Compare siempre su resultado con el rango de referencia de su propio informe de laboratorio."},
            {"question": "¿La amilasa alta siempre significa pancreatitis?",
             "answer": "No siempre. La amilasa elevada también puede deberse a enfermedades de las glándulas salivales, obstrucción intestinal, cetoacidosis diabética y macroamilasemia. Un diagnóstico preciso requiere una prueba de lipasa, imagen abdominal y una evaluación clínica completa."},
        ],
        "de": [
            {"question": "Was ist ein Amylase-Test?",
             "answer": "Ein Amylase-Test ist eine Blutuntersuchung, die den Spiegel der Amylase misst — eines Verdauungsenzyms, das Stärke abbaut. Er gehört zu den ersten Tests bei Verdacht auf akute Pankreatitis und wird zusammen mit der Lipase für eine höhere diagnostische Genauigkeit beurteilt."},
            {"question": "Was sind die Amylase-Normalwerte?",
             "answer": "Der normale Serum-Amylase-Bereich für Erwachsene liegt in der Regel bei 28–100 U/L. Die pankreasspezifische Fraktion, die Pankreas-Amylase (P-Amylase), wird typischerweise im Bereich von 13–53 U/L bewertet. Vergleichen Sie Ihr Ergebnis stets mit dem Referenzbereich auf Ihrem eigenen Laborbefund."},
            {"question": "Bedeutet erhöhte Amylase immer eine Pankreatitis?",
             "answer": "Nicht immer. Erhöhte Amylasewerte können auch durch Speicheldrüsenerkrankungen, Darmverschluss, diabetische Ketoazidose und Makroamylasämie verursacht werden. Eine korrekte Diagnose erfordert einen Lipase-Test, abdominelle Bildgebung und eine vollständige klinische Beurteilung."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'un test d'amylase ?",
             "answer": "Le test d'amylase est une analyse de sang qui mesure le taux d'amylase, une enzyme digestive qui dégrade l'amidon. C'est l'un des premiers examens prescrits en cas de suspicion de pancréatite aiguë et il est évalué conjointement avec la lipase pour améliorer la précision diagnostique."},
            {"question": "Quelles sont les valeurs normales d'amylase ?",
             "answer": "La plage normale de l'amylase sérique chez l'adulte est généralement de 28–100 U/L. La fraction spécifique du pancréas, l'amylase pancréatique (P-amylase), se situe typiquement entre 13 et 53 U/L. Comparez toujours votre résultat avec l'intervalle de référence figurant sur votre propre compte rendu de laboratoire."},
            {"question": "Une amylase élevée signifie-t-elle toujours une pancréatite ?",
             "answer": "Pas toujours. Une amylase élevée peut également résulter de maladies des glandes salivaires, d'une occlusion intestinale, d'une acidocétose diabétique ou d'une macroamylasémie. Un diagnostic précis nécessite un dosage de la lipase, une imagerie abdominale et une évaluation clinique complète."},
        ],
        "it": [
            {"question": "Cos'è il test dell'amilasi?",
             "answer": "Il test dell'amilasi è un esame del sangue che misura il livello dell'amilasi, un enzima digestivo che scinde l'amido. È uno dei primi esami richiesti in caso di sospetta pancreatite acuta e viene valutato insieme alla lipasi per una maggiore accuratezza diagnostica."},
            {"question": "Quali sono i valori normali di amilasi?",
             "answer": "Il range sierico normale dell'amilasi per gli adulti è generalmente 28–100 U/L. La frazione specifica del pancreas, l'amilasi pancreatica (P-amilasi), si colloca tipicamente tra 13 e 53 U/L. Confronta sempre il tuo risultato con l'intervallo di riferimento indicato nel tuo referto di laboratorio."},
            {"question": "L'amilasi alta significa sempre pancreatite?",
             "answer": "Non sempre. L'amilasi elevata può anche essere causata da malattie delle ghiandole salivari, ostruzione intestinale, chetoacidosi diabetica e macroamilasemia. Una diagnosi accurata richiede un dosaggio della lipasi, imaging addominale e una valutazione clinica completa."},
        ],
        "he": [
            {"question": "מהי בדיקת עמילאז?",
             "answer": "בדיקת עמילאז היא בדיקת דם המודדת את רמת העמילאז — אנזים עיכול המפרק עמילן. זוהי אחת הבדיקות הראשונות הנדרשות בחשד לדלקת לבלב חריפה והיא מוערכת לצד ליפאז לדיוק אבחנתי משופר."},
            {"question": "מהו ערך הנורמה של עמילאז?",
             "answer": "טווח עמילאז הסרום הנורמלי למבוגרים הוא בדרך כלל 28–100 U/L. הפרקציה הספציפית ללבלב, עמילאז לבלבי (P-amylase), מוערכת בדרך כלל בטווח 13–53 U/L. השוו תמיד את התוצאה שלכם לטווח הייחוס בדוח המעבדה שלכם."},
            {"question": "האם עמילאז גבוה תמיד פירושו דלקת לבלב?",
             "answer": "לא תמיד. עמילאז גבוה יכול לנבוע גם ממחלות בלוטות רוק, חסימת מעי, חמצת קטונית סוכרתית ומקרואמילאזמיה. אבחון מדויק דורש בדיקת ליפאז, הדמיה בטנית והערכה קלינית מלאה."},
        ],
        "hi": [
            {"question": "एमाइलेज़ टेस्ट क्या है?",
             "answer": "एमाइलेज़ टेस्ट एक ब्लड टेस्ट है जो एमाइलेज़ के स्तर को मापता है — यह एक पाचक एंज़ाइम है जो स्टार्च को तोड़ता है। यह एक्यूट पैंक्रिएटाइटिस की आशंका में सबसे पहले माँगी जाने वाली जाँचों में से एक है और बेहतर डायग्नोस्टिक सटीकता के लिए लाइपेज़ के साथ मूल्यांकन किया जाता है।"},
            {"question": "एमाइलेज़ की नॉर्मल रेंज क्या है?",
             "answer": "वयस्कों के लिए सीरम एमाइलेज़ की सामान्य रेंज आम तौर पर 28–100 U/L होती है। पैंक्रियास-स्पेसिफ़िक फ़्रैक्शन, पैंक्रिएटिक एमाइलेज़ (P-amylase), आमतौर पर 13–53 U/L होता है। अपने रिज़ल्ट की तुलना हमेशा अपनी लैब रिपोर्ट पर छपी रेफ़रेंस रेंज से करें।"},
            {"question": "क्या हाई एमाइलेज़ हमेशा पैंक्रिएटाइटिस होता है?",
             "answer": "हमेशा नहीं। एमाइलेज़ बढ़ने के अन्य कारणों में लार ग्रंथि रोग, आंतों की रुकावट, डायबिटिक कीटोएसिडोसिस और मैक्रोएमाइलेज़ीमिया शामिल हैं। सही निदान के लिए लाइपेज़ टेस्ट, एब्डोमिनल इमेजिंग और पूर्ण क्लिनिकल मूल्यांकन आवश्यक है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل الأميلاز؟",
             "answer": "تحليل الأميلاز هو فحص دم يقيس مستوى الأميلاز — إنزيم هضمي يفكّك النشا. وهو من أولى الفحوصات المطلوبة عند الاشتباه بالتهاب البنكرياس الحاد ويُقيَّم مع الليباز لتحسين دقة التشخيص."},
            {"question": "ما هو المستوى الطبيعي للأميلاز؟",
             "answer": "يتراوح المستوى الطبيعي لأميلاز المصل عند البالغين عادةً بين 28 و100 وحدة/لتر. أما الأميلاز البنكرياسي (P-amylase) فيُقيَّم في نطاق 13–53 وحدة/لتر. قارنوا دائماً نتيجتكم بالنطاق المرجعي المطبوع على تقرير المختبر."},
            {"question": "هل ارتفاع الأميلاز يعني دائماً التهاب بنكرياس؟",
             "answer": "ليس دائماً. يمكن أن ينتج ارتفاع الأميلاز أيضاً عن أمراض الغدد اللعابية أو انسداد الأمعاء أو الحماض الكيتوني السكري أو ماكروأميلازيميا. يتطلب التشخيص الدقيق اختبار ليباز وتصويراً بطنياً وتقييماً سريرياً شاملاً."},
        ],
    }
