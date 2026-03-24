# -*- coding: utf-8 -*-
"""
Homocysteine blog article — full body content for all 9 languages.
Used by blog_i18n._article_homocysteine().
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

_HCY_TABLE_TR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Kategori</th>"
    f"<th {_TH}>Homosistein Düzeyi (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Normal</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>Hafif hiperhomosisteinemi</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>Orta düzey hiperhomosisteinemi</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>Ciddi hiperhomosisteinemi</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_EN = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Category</th>"
    f"<th {_TH}>Homocysteine Level (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Normal</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>Mild hyperhomocysteinemia</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>Intermediate hyperhomocysteinemia</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>Severe hyperhomocysteinemia</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_ES = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Categoría</th>"
    f"<th {_TH}>Nivel de homocisteína (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Normal</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>Hiperhomocisteinemia leve</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>Hiperhomocisteinemia intermedia</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>Hiperhomocisteinemia grave</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_DE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Kategorie</th>"
    f"<th {_TH}>Homocystein-Spiegel (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Normal</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>Leichte Hyperhomocysteinämie</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>Mittlere Hyperhomocysteinämie</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>Schwere Hyperhomocysteinämie</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_FR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Catégorie</th>"
    f"<th {_TH}>Taux d'homocystéine (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Normal</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>Hyperhomocystéinémie légère</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>Hyperhomocystéinémie intermédiaire</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>Hyperhomocystéinémie sévère</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_IT = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Categoria</th>"
    f"<th {_TH}>Livello di omocisteina (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>Normale</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>Iperomocisteinemia lieve</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>Iperomocisteinemia intermedia</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>Iperomocisteinemia grave</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_HE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>קטגוריה</th>"
    f"<th {_TH_RTL}>רמת הומוציסטאין (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>תקין</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>היפרהומוציסטאינמיה קלה</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>היפרהומוציסטאינמיה בינונית</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>היפרהומוציסטאינמיה חמורה</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_HI = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>श्रेणी</th>"
    f"<th {_TH}>होमोसिस्टीन स्तर (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>सामान्य</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>हल्की हाइपरहोमोसिस्टीनीमिया</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>मध्यम हाइपरहोमोसिस्टीनीमिया</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>गंभीर हाइपरहोमोसिस्टीनीमिया</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
    "</tbody></table>"
)

_HCY_TABLE_AR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>الفئة</th>"
    f"<th {_TH_RTL}>مستوى الهوموسيستين (µmol/L)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>طبيعي</td>"
    f"<td {_TD}>5 – 15</td></tr>"
    f"<tr><td {_TD}>فرط هوموسيستين الدم الخفيف</td>"
    f"<td {_TD}>15 – 30</td></tr>"
    f"<tr><td {_TD}>فرط هوموسيستين الدم المتوسط</td>"
    f"<td {_TD}>30 – 100</td></tr>"
    f"<tr><td {_TD}>فرط هوموسيستين الدم الشديد</td>"
    f"<td {_TD}>&gt; 100</td></tr>"
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
            heading="Homosistein kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>Homosistein testi</strong>, kandaki homosistein aminoasit düzeyini "
                "ölçen bir <strong>homosistein kan testi</strong>dir. Homosistein, metiyonin "
                "metabolizması sırasında oluşan sülfürlü bir aminoasittir ve normalde B12, folat "
                "(B9) ve B6 vitaminleri aracılığıyla başka bileşiklere dönüştürülür. Bu "
                "vitaminlerin eksikliği veya MTHFR gen mutasyonu gibi genetik faktörler "
                "<strong>homosistein yüksekliğine</strong> yol açabilir.</p>"
                "<p><strong>Yüksek homosistein</strong> düzeyleri (<strong>hiperhomosisteinemi</strong>) "
                "kardiyovasküler hastalık, inme ve derin ven trombozu için bağımsız bir risk "
                "faktörü olarak kabul edilir. Damar endotelinde oksidatif stres oluşturarak "
                "ateroskleroz sürecini hızlandırır ve tromboz eğilimini artırır. Bu rehberde "
                "<strong>homosistein normal değerleri</strong>, yükseklik nedenlerini ve ne zaman "
                "doktora başvurmanız gerektiğini ayrıntılı şekilde öğreneceksiniz.</p>"
                "<p>Homosistein düzeyinin değerlendirilmesi özellikle ailede erken yaşta kalp "
                "hastalığı öyküsü olan, tekrarlayan düşükler yaşayan veya açıklanamayan tromboz "
                "atakları geçiren bireylerde büyük önem taşır. Erken tanı ve uygun tedavi ile "
                "kardiyovasküler risk önemli ölçüde azaltılabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Homosistein normal değerleri",
            body_html=(
                "<p><strong>Homosistein normal aralığı</strong> genellikle 5–15 µmol/L olarak "
                "kabul edilir; ancak laboratuvar yöntemine ve yaşa bağlı küçük farklılıklar "
                "olabilir. Klinik kılavuzlar <strong>homosistein düzeylerini</strong> dört "
                "kategoride sınıflandırır: normal, hafif, orta ve ciddi "
                "<strong>hiperhomosisteinemi</strong>.</p>"
                "<p>Aşağıdaki tabloda <strong>homosistein kan testi</strong> sonuçlarına göre "
                "sınıflandırma özetlenmiştir:</p>"
                + _HCY_TABLE_TR +
                "<p>Kadınlarda homosistein düzeyleri erkeklere göre genellikle daha düşüktür; "
                "menopoz sonrasında ise bu fark kapanma eğilimindedir. Böbrek fonksiyonları, "
                "beslenme alışkanlıkları ve kullanılan ilaçlar da sonuçları etkileyebilir. "
                "Sonuçlarınızı her zaman laboratuvar raporunuzdaki referans aralığıyla "
                "karşılaştırın.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Homosistein yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Yüksek homosistein</strong> düzeyine yol açan faktörler beslenme "
                "eksikliklerinden genetik mutasyonlara kadar geniş bir yelpazeye yayılır. "
                "<strong>Homosistein yüksekliğinin</strong> başlıca nedenleri şunlardır:</p>"
                "<ul>"
                "<li><strong>B12 vitamini eksikliği:</strong> Homosisteinin metiyonine geri "
                "dönüşümü için gerekli olan B12 vitamini yetersiz olduğunda homosistein birikir.</li>"
                "<li><strong>Folat (B9) eksikliği:</strong> Folat, homosistein metabolizmasında "
                "kritik bir ko-substrat olup eksikliği doğrudan <strong>homosistein "
                "yüksekliğine</strong> neden olur.</li>"
                "<li><strong>B6 vitamini eksikliği:</strong> Homosisteinin transsülfürasyon "
                "yolağıyla sistein'e dönüşümünde B6 vitamini gereklidir.</li>"
                "<li><strong>MTHFR gen mutasyonu:</strong> Metilentetrahidrofolat redüktaz (MTHFR) "
                "enzimindeki C677T veya A1298C varyantları folat metabolizmasını bozarak "
                "<strong>hiperhomosisteinemi</strong> riskini artırır.</li>"
                "<li><strong>Kronik böbrek hastalığı:</strong> Böbrek fonksiyon kaybı homosistein "
                "klirensini azaltır ve düzeylerin kronik olarak yüksek kalmasına neden olur.</li>"
                "<li><strong>Hipotiroidizm:</strong> Tiroid hormon eksikliği homosistein "
                "metabolizmasını yavaşlatarak düzeyleri yükseltebilir.</li>"
                "<li><strong>Bazı ilaçlar:</strong> Metotreksat, fenitoin, karbamazepin ve "
                "nitröz oksit gibi ilaçlar folat veya B12 metabolizmasını bozarak "
                "<strong>homosistein düzeylerini</strong> artırabilir.</li>"
                "</ul>"
                "<p><strong>Yüksek homosistein</strong> damar duvarında oksidatif hasara, "
                "endotel disfonksiyonuna ve pıhtılaşma kaskadının aktivasyonuna yol açarak "
                "ateroskleroz, inme ve derin ven trombozu riskini artırır. Bu nedenle altta "
                "yatan nedenin belirlenmesi ve tedavisi kritik önem taşır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Ailede erken yaşta kalp krizi veya inme öyküsü varsa, açıklanamayan "
                "tekrarlayan düşükler yaşıyorsanız ya da genç yaşta derin ven trombozu veya "
                "pulmoner emboli geçirdiyseniz <strong>homosistein testi</strong> yaptırmanız "
                "önerilir. Ayrıca bilinen MTHFR mutasyonu taşıyıcıları düzenli aralıklarla "
                "homosistein takibi yaptırmalıdır.</p>"
                "<p><strong>Homosistein kan testi</strong> sonucunuz yüksek çıkarsa panik "
                "yapmayın, ancak mutlaka bir dahiliye veya kardiyoloji uzmanıyla paylaşın. "
                "Doktorunuz B12, folat ve B6 düzeylerini değerlendirecek, gerekli görürse MTHFR "
                "genotipleme testi isteyecek ve uygun vitamin takviyesi veya diyet planı "
                "önerecektir. Erken müdahale ile <strong>homosistein düzeyleri</strong> çoğu "
                "durumda normal aralığa getirilebilir.</p>"
                "<p>Unutmayın: <strong>yüksek homosistein</strong> tek başına bir hastalık "
                "değil, tedavi edilebilir bir risk faktörüdür. Doğru vitamin desteği, dengeli "
                "beslenme ve düzenli takip ile kardiyovasküler riskinizi önemli ölçüde "
                "azaltabilirsiniz. Her zaman hekiminize danışın.</p>"
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
            heading="Homocysteine blood test: what your results mean",
            body_html=(
                "<p>The <strong>homocysteine test</strong> is a <strong>homocysteine blood "
                "test</strong> that measures the level of the amino acid homocysteine in your "
                "blood. Homocysteine is a sulphur-containing amino acid produced during the "
                "metabolism of methionine. Under normal conditions it is converted into other "
                "compounds with the help of vitamins B12, folate (B9) and B6. Deficiencies in "
                "these vitamins or genetic factors such as the MTHFR mutation can lead to "
                "<strong>elevated homocysteine</strong>.</p>"
                "<p><strong>High homocysteine</strong> levels — a condition known as "
                "<strong>hyperhomocysteinemia</strong> — are considered an independent risk "
                "factor for cardiovascular disease, stroke and deep-vein thrombosis. Excess "
                "homocysteine promotes oxidative stress in the vascular endothelium, accelerates "
                "atherosclerosis and increases the tendency to form blood clots. In this guide "
                "you will learn the <strong>homocysteine normal range</strong>, the causes of "
                "<strong>high homocysteine</strong> and when to seek medical attention.</p>"
                "<p>Assessing <strong>homocysteine levels</strong> is especially important for "
                "individuals with a family history of premature heart disease, recurrent "
                "pregnancy loss or unexplained thrombotic events. Early detection and appropriate "
                "treatment can significantly reduce cardiovascular risk.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Homocysteine normal range",
            body_html=(
                "<p>The <strong>homocysteine normal range</strong> is generally accepted as "
                "5–15 µmol/L, though minor variations may occur depending on the laboratory "
                "method and the patient's age. Clinical guidelines classify "
                "<strong>homocysteine levels</strong> into four categories: normal, mild, "
                "intermediate and severe <strong>hyperhomocysteinemia</strong>.</p>"
                "<p>The table below summarises the classification based on "
                "<strong>homocysteine blood test</strong> results:</p>"
                + _HCY_TABLE_EN +
                "<p>Women tend to have lower <strong>homocysteine levels</strong> than men, "
                "although this gap narrows after menopause. Kidney function, dietary habits and "
                "certain medications can also influence results. Always compare your value with "
                "the reference range printed on your own laboratory report.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high homocysteine levels",
            body_html=(
                "<p>The factors that lead to <strong>elevated homocysteine</strong> range from "
                "nutritional deficiencies to genetic mutations. The main causes of "
                "<strong>high homocysteine</strong> include:</p>"
                "<ul>"
                "<li><strong>Vitamin B12 deficiency:</strong> B12 is essential for the "
                "remethylation of homocysteine back to methionine; insufficient B12 causes "
                "homocysteine to accumulate.</li>"
                "<li><strong>Folate (B9) deficiency:</strong> Folate is a critical co-substrate "
                "in homocysteine metabolism, and its deficiency directly raises "
                "<strong>homocysteine levels</strong>.</li>"
                "<li><strong>Vitamin B6 deficiency:</strong> B6 is required for the "
                "trans-sulphuration pathway that converts homocysteine to cysteine.</li>"
                "<li><strong>MTHFR gene mutation:</strong> The C677T or A1298C variants of the "
                "methylenetetrahydrofolate reductase (MTHFR) enzyme impair folate metabolism "
                "and increase the risk of <strong>hyperhomocysteinemia</strong>.</li>"
                "<li><strong>Chronic kidney disease:</strong> Loss of renal function reduces "
                "homocysteine clearance, causing levels to remain chronically elevated.</li>"
                "<li><strong>Hypothyroidism:</strong> Thyroid hormone deficiency can slow "
                "homocysteine metabolism and raise levels.</li>"
                "<li><strong>Certain medications:</strong> Methotrexate, phenytoin, "
                "carbamazepine and nitrous oxide can interfere with folate or B12 metabolism, "
                "raising <strong>homocysteine levels</strong>.</li>"
                "</ul>"
                "<p><strong>High homocysteine</strong> causes oxidative damage to the vessel "
                "wall, endothelial dysfunction and activation of the coagulation cascade, "
                "thereby increasing the risk of atherosclerosis, stroke and deep-vein "
                "thrombosis. Identifying and treating the underlying cause is therefore "
                "critical.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>A <strong>homocysteine test</strong> is recommended if you have a family "
                "history of premature heart attack or stroke, if you experience recurrent "
                "unexplained miscarriages, or if you have suffered deep-vein thrombosis or "
                "pulmonary embolism at a young age. Individuals known to carry an MTHFR "
                "mutation should also have their homocysteine monitored regularly.</p>"
                "<p>If your <strong>homocysteine blood test</strong> result is elevated, do not "
                "panic but share it with an internist or cardiologist without delay. Your doctor "
                "will evaluate your B12, folate and B6 levels, may order MTHFR genotyping if "
                "appropriate, and will recommend suitable vitamin supplementation or dietary "
                "changes. With early intervention, <strong>homocysteine levels</strong> can be "
                "brought back to the normal range in most cases.</p>"
                "<p>Remember: <strong>elevated homocysteine</strong> is not a disease in itself "
                "but a treatable risk factor. With the right vitamin support, a balanced diet "
                "and regular monitoring you can significantly reduce your cardiovascular risk. "
                "Always consult your physician.</p>"
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
            heading="Análisis de homocisteína en sangre: qué significan sus resultados",
            body_html=(
                "<p>El <strong>análisis de homocisteína</strong> es una <strong>prueba de "
                "homocisteína en sangre</strong> que mide el nivel del aminoácido homocisteína "
                "en la sangre. La homocisteína es un aminoácido azufrado que se produce durante "
                "el metabolismo de la metionina y que, en condiciones normales, se convierte en "
                "otros compuestos gracias a las vitaminas B12, ácido fólico (B9) y B6. La "
                "deficiencia de estas vitaminas o factores genéticos como la mutación MTHFR "
                "pueden provocar <strong>niveles elevados de homocisteína</strong>.</p>"
                "<p>Los <strong>niveles altos de homocisteína</strong> — una condición conocida "
                "como <strong>hiperhomocisteinemia</strong> — se consideran un factor de riesgo "
                "independiente de enfermedad cardiovascular, ictus y trombosis venosa profunda. "
                "El exceso de homocisteína promueve el estrés oxidativo en el endotelio vascular, "
                "acelera la aterosclerosis y aumenta la tendencia a la formación de coágulos. En "
                "esta guía conocerá los <strong>valores normales de homocisteína</strong>, las "
                "causas de la <strong>homocisteína alta</strong> y cuándo buscar atención "
                "médica.</p>"
                "<p>La evaluación de los <strong>niveles de homocisteína</strong> es "
                "especialmente importante en personas con antecedentes familiares de cardiopatía "
                "prematura, abortos recurrentes o episodios trombóticos inexplicados. La "
                "detección precoz y el tratamiento adecuado pueden reducir significativamente el "
                "riesgo cardiovascular.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de homocisteína",
            body_html=(
                "<p>El <strong>rango normal de homocisteína</strong> se acepta generalmente en "
                "5–15 µmol/L, aunque pueden existir pequeñas variaciones según el método de "
                "laboratorio y la edad del paciente. Las guías clínicas clasifican los "
                "<strong>niveles de homocisteína</strong> en cuatro categorías: normal, leve, "
                "intermedia y grave <strong>hiperhomocisteinemia</strong>.</p>"
                "<p>La siguiente tabla resume la clasificación según los resultados del "
                "<strong>análisis de homocisteína en sangre</strong>:</p>"
                + _HCY_TABLE_ES +
                "<p>Las mujeres tienden a presentar <strong>niveles de homocisteína</strong> más "
                "bajos que los hombres, aunque esta diferencia se reduce tras la menopausia. La "
                "función renal, los hábitos alimentarios y ciertos medicamentos también pueden "
                "influir en los resultados. Compare siempre su valor con el rango de referencia "
                "indicado en su propio informe de laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de homocisteína alta",
            body_html=(
                "<p>Los factores que provocan <strong>niveles elevados de homocisteína</strong> "
                "abarcan desde deficiencias nutricionales hasta mutaciones genéticas. Las "
                "principales causas de <strong>homocisteína alta</strong> incluyen:</p>"
                "<ul>"
                "<li><strong>Deficiencia de vitamina B12:</strong> La B12 es esencial para la "
                "remetilación de la homocisteína a metionina; su carencia provoca acumulación de "
                "homocisteína.</li>"
                "<li><strong>Deficiencia de ácido fólico (B9):</strong> El folato es un "
                "cosustrato crítico en el metabolismo de la homocisteína y su déficit eleva "
                "directamente los <strong>niveles de homocisteína</strong>.</li>"
                "<li><strong>Deficiencia de vitamina B6:</strong> La B6 es necesaria para la "
                "vía de transulfuración que convierte la homocisteína en cisteína.</li>"
                "<li><strong>Mutación del gen MTHFR:</strong> Las variantes C677T o A1298C de "
                "la enzima metilentetrahidrofolato reductasa (MTHFR) alteran el metabolismo del "
                "folato y aumentan el riesgo de <strong>hiperhomocisteinemia</strong>.</li>"
                "<li><strong>Enfermedad renal crónica:</strong> La pérdida de función renal "
                "reduce el aclaramiento de homocisteína, manteniendo los niveles crónicamente "
                "elevados.</li>"
                "<li><strong>Hipotiroidismo:</strong> El déficit de hormona tiroidea puede "
                "ralentizar el metabolismo de la homocisteína y elevar sus niveles.</li>"
                "<li><strong>Ciertos medicamentos:</strong> Metotrexato, fenitoína, "
                "carbamazepina y óxido nitroso pueden interferir con el metabolismo del folato "
                "o la B12, elevando los <strong>niveles de homocisteína</strong>.</li>"
                "</ul>"
                "<p>La <strong>homocisteína alta</strong> causa daño oxidativo en la pared "
                "vascular, disfunción endotelial y activación de la cascada de coagulación, lo "
                "que incrementa el riesgo de aterosclerosis, ictus y trombosis venosa profunda. "
                "Identificar y tratar la causa subyacente es, por tanto, fundamental.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Se recomienda realizar un <strong>análisis de homocisteína</strong> si tiene "
                "antecedentes familiares de infarto o ictus a edad temprana, si sufre abortos "
                "recurrentes inexplicados o si ha tenido trombosis venosa profunda o embolia "
                "pulmonar en edad joven. Las personas portadoras conocidas de la mutación MTHFR "
                "también deben monitorizar periódicamente su homocisteína.</p>"
                "<p>Si su resultado del <strong>análisis de homocisteína en sangre</strong> está "
                "elevado, no se alarme pero compártalo sin demora con un internista o "
                "cardiólogo. Su médico evaluará sus niveles de B12, ácido fólico y B6, solicitará "
                "un estudio genético de MTHFR si procede y le recomendará la suplementación "
                "vitamínica o los cambios dietéticos oportunos. Con una intervención temprana, "
                "los <strong>niveles de homocisteína</strong> pueden normalizarse en la mayoría "
                "de los casos.</p>"
                "<p>Recuerde: la <strong>homocisteína elevada</strong> no es una enfermedad en "
                "sí misma, sino un factor de riesgo tratable. Con el aporte vitamínico adecuado, "
                "una dieta equilibrada y un seguimiento regular puede reducir significativamente "
                "su riesgo cardiovascular. Consulte siempre a su médico.</p>"
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
            heading="Homocystein-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>Homocystein-Test</strong> ist ein <strong>Homocystein-"
                "Bluttest</strong>, der den Spiegel der Aminosäure Homocystein in Ihrem Blut "
                "misst. Homocystein ist eine schwefelhaltige Aminosäure, die beim Abbau von "
                "Methionin entsteht und unter normalen Bedingungen mithilfe der Vitamine B12, "
                "Folsäure (B9) und B6 in andere Verbindungen umgewandelt wird. Ein Mangel an "
                "diesen Vitaminen oder genetische Faktoren wie die MTHFR-Mutation können zu "
                "<strong>erhöhtem Homocystein</strong> führen.</p>"
                "<p><strong>Hohe Homocysteinwerte</strong> — ein Zustand, der als "
                "<strong>Hyperhomocysteinämie</strong> bezeichnet wird — gelten als "
                "unabhängiger Risikofaktor für Herz-Kreislauf-Erkrankungen, Schlaganfall und "
                "tiefe Venenthrombose. Überschüssiges Homocystein fördert oxidativen Stress im "
                "Gefäßendothel, beschleunigt die Atherosklerose und erhöht die Neigung zur "
                "Thrombosebildung. In diesem Ratgeber erfahren Sie den "
                "<strong>Homocystein-Normalbereich</strong>, die Ursachen für <strong>hohes "
                "Homocystein</strong> und wann Sie ärztliche Hilfe suchen sollten.</p>"
                "<p>Die Bestimmung der <strong>Homocysteinwerte</strong> ist besonders wichtig "
                "für Personen mit familiärer Vorbelastung durch vorzeitige Herzerkrankungen, "
                "wiederkehrende Fehlgeburten oder unerklärliche thrombotische Ereignisse. "
                "Frühzeitige Erkennung und geeignete Behandlung können das kardiovaskuläre "
                "Risiko erheblich senken.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Homocystein-Normalwerte",
            body_html=(
                "<p>Der <strong>Homocystein-Normalbereich</strong> liegt allgemein bei "
                "5–15 µmol/L, wobei je nach Labormethode und Alter des Patienten leichte "
                "Abweichungen möglich sind. Klinische Leitlinien unterteilen die "
                "<strong>Homocysteinwerte</strong> in vier Kategorien: normal, leichte, "
                "mittlere und schwere <strong>Hyperhomocysteinämie</strong>.</p>"
                "<p>Die folgende Tabelle fasst die Einteilung anhand der Ergebnisse des "
                "<strong>Homocystein-Bluttests</strong> zusammen:</p>"
                + _HCY_TABLE_DE +
                "<p>Frauen weisen in der Regel niedrigere <strong>Homocysteinwerte</strong> auf "
                "als Männer; nach der Menopause verringert sich dieser Unterschied. "
                "Nierenfunktion, Ernährungsgewohnheiten und bestimmte Medikamente können die "
                "Ergebnisse ebenfalls beeinflussen. Vergleichen Sie Ihr Ergebnis stets mit dem "
                "Referenzbereich auf Ihrem eigenen Laborbefund.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für erhöhte Homocysteinwerte",
            body_html=(
                "<p>Die Faktoren, die zu <strong>erhöhtem Homocystein</strong> führen, reichen "
                "von Nährstoffmangel bis hin zu genetischen Mutationen. Die wichtigsten "
                "Ursachen für <strong>hohes Homocystein</strong> sind:</p>"
                "<ul>"
                "<li><strong>Vitamin-B12-Mangel:</strong> B12 ist für die Remethylierung von "
                "Homocystein zu Methionin unerlässlich; bei unzureichendem B12 sammelt sich "
                "Homocystein an.</li>"
                "<li><strong>Folsäuremangel (B9):</strong> Folat ist ein kritisches Ko-Substrat "
                "im Homocystein-Stoffwechsel, und sein Mangel erhöht direkt die "
                "<strong>Homocysteinwerte</strong>.</li>"
                "<li><strong>Vitamin-B6-Mangel:</strong> B6 wird für den "
                "Transsulfurierungsweg benötigt, der Homocystein in Cystein umwandelt.</li>"
                "<li><strong>MTHFR-Genmutation:</strong> Die Varianten C677T oder A1298C des "
                "Enzyms Methylentetrahydrofolat-Reduktase (MTHFR) beeinträchtigen den "
                "Folat-Stoffwechsel und erhöhen das Risiko einer "
                "<strong>Hyperhomocysteinämie</strong>.</li>"
                "<li><strong>Chronische Nierenerkrankung:</strong> Ein Verlust der "
                "Nierenfunktion verringert die Homocystein-Clearance und hält die Werte "
                "chronisch erhöht.</li>"
                "<li><strong>Hypothyreose:</strong> Ein Schilddrüsenhormonmangel kann den "
                "Homocystein-Stoffwechsel verlangsamen und die Werte anheben.</li>"
                "<li><strong>Bestimmte Medikamente:</strong> Methotrexat, Phenytoin, "
                "Carbamazepin und Lachgas können den Folat- oder B12-Stoffwechsel stören und "
                "die <strong>Homocysteinwerte</strong> erhöhen.</li>"
                "</ul>"
                "<p><strong>Hohes Homocystein</strong> verursacht oxidative Schäden an der "
                "Gefäßwand, Endotheldysfunktion und Aktivierung der Gerinnungskaskade und "
                "erhöht dadurch das Risiko für Atherosklerose, Schlaganfall und tiefe "
                "Venenthrombose. Die Identifizierung und Behandlung der zugrunde liegenden "
                "Ursache ist daher entscheidend.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Ein <strong>Homocystein-Test</strong> wird empfohlen, wenn in Ihrer Familie "
                "Herzinfarkte oder Schlaganfälle in jungem Alter vorkommen, wenn Sie "
                "wiederkehrende unerklärliche Fehlgeburten erleiden oder wenn Sie in jungen "
                "Jahren eine tiefe Venenthrombose oder Lungenembolie hatten. Auch bekannte "
                "Träger der MTHFR-Mutation sollten ihre Homocysteinwerte regelmäßig "
                "kontrollieren lassen.</p>"
                "<p>Wenn Ihr <strong>Homocystein-Bluttest</strong> erhöht ausfällt, bewahren "
                "Sie Ruhe, teilen Sie das Ergebnis aber unverzüglich einem Internisten oder "
                "Kardiologen mit. Ihr Arzt wird Ihre B12-, Folsäure- und B6-Spiegel prüfen, "
                "gegebenenfalls eine MTHFR-Genotypisierung anordnen und Ihnen eine geeignete "
                "Vitaminergänzung oder Ernährungsumstellung empfehlen. Bei frühzeitiger "
                "Intervention lassen sich die <strong>Homocysteinwerte</strong> in den meisten "
                "Fällen normalisieren.</p>"
                "<p>Denken Sie daran: <strong>Erhöhtes Homocystein</strong> ist keine "
                "eigenständige Krankheit, sondern ein behandelbarer Risikofaktor. Mit der "
                "richtigen Vitaminversorgung, einer ausgewogenen Ernährung und regelmäßiger "
                "Kontrolle können Sie Ihr kardiovaskuläres Risiko erheblich senken. Besprechen "
                "Sie Ihre Ergebnisse stets mit Ihrem Arzt.</p>"
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
            heading="Analyse de l'homocystéine : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test d'homocystéine</strong> est une <strong>analyse sanguine "
                "de l'homocystéine</strong> qui mesure le taux de cet acide aminé dans le "
                "sang. L'homocystéine est un acide aminé soufré produit lors du métabolisme de "
                "la méthionine et qui, en temps normal, est transformé en d'autres composés "
                "grâce aux vitamines B12, folate (B9) et B6. Une carence en ces vitamines ou "
                "des facteurs génétiques tels que la mutation MTHFR peuvent entraîner une "
                "<strong>élévation de l'homocystéine</strong>.</p>"
                "<p>Des <strong>taux élevés d'homocystéine</strong> — un état appelé "
                "<strong>hyperhomocystéinémie</strong> — sont considérés comme un facteur de "
                "risque indépendant de maladie cardiovasculaire, d'accident vasculaire cérébral "
                "(AVC) et de thrombose veineuse profonde. L'excès d'homocystéine favorise le "
                "stress oxydatif dans l'endothélium vasculaire, accélère l'athérosclérose et "
                "augmente la tendance à la formation de caillots. Dans ce guide, vous "
                "découvrirez les <strong>valeurs normales d'homocystéine</strong>, les causes "
                "d'une <strong>homocystéine élevée</strong> et quand consulter un médecin.</p>"
                "<p>L'évaluation des <strong>taux d'homocystéine</strong> revêt une importance "
                "particulière chez les personnes ayant des antécédents familiaux de cardiopathie "
                "précoce, de fausses couches récurrentes ou d'événements thrombotiques "
                "inexpliqués. Un dépistage précoce et un traitement adapté peuvent réduire "
                "considérablement le risque cardiovasculaire.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales d'homocystéine",
            body_html=(
                "<p>Les <strong>valeurs normales d'homocystéine</strong> se situent "
                "généralement entre 5 et 15 µmol/L, bien que de légères variations puissent "
                "exister selon la méthode de laboratoire et l'âge du patient. Les "
                "recommandations cliniques classent les <strong>taux d'homocystéine</strong> en "
                "quatre catégories : normal, légère, intermédiaire et sévère "
                "<strong>hyperhomocystéinémie</strong>.</p>"
                "<p>Le tableau ci-dessous résume la classification en fonction des résultats de "
                "l'<strong>analyse sanguine de l'homocystéine</strong> :</p>"
                + _HCY_TABLE_FR +
                "<p>Les femmes présentent généralement des <strong>taux d'homocystéine</strong> "
                "plus bas que les hommes, bien que cet écart se réduise après la ménopause. La "
                "fonction rénale, les habitudes alimentaires et certains médicaments peuvent "
                "également influencer les résultats. Comparez toujours votre valeur avec "
                "l'intervalle de référence figurant sur votre propre compte rendu de "
                "laboratoire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une homocystéine élevée",
            body_html=(
                "<p>Les facteurs entraînant une <strong>élévation de l'homocystéine</strong> "
                "vont des carences nutritionnelles aux mutations génétiques. Les principales "
                "causes d'une <strong>homocystéine élevée</strong> sont :</p>"
                "<ul>"
                "<li><strong>Carence en vitamine B12 :</strong> La B12 est essentielle à la "
                "reméthylation de l'homocystéine en méthionine ; son insuffisance entraîne une "
                "accumulation d'homocystéine.</li>"
                "<li><strong>Carence en folate (B9) :</strong> Le folate est un co-substrat "
                "critique du métabolisme de l'homocystéine et sa carence élève directement les "
                "<strong>taux d'homocystéine</strong>.</li>"
                "<li><strong>Carence en vitamine B6 :</strong> La B6 est nécessaire à la voie "
                "de transsulfuration qui convertit l'homocystéine en cystéine.</li>"
                "<li><strong>Mutation du gène MTHFR :</strong> Les variantes C677T ou A1298C "
                "de l'enzyme méthylènetétrahydrofolate réductase (MTHFR) altèrent le "
                "métabolisme du folate et augmentent le risque "
                "d'<strong>hyperhomocystéinémie</strong>.</li>"
                "<li><strong>Maladie rénale chronique :</strong> La perte de fonction rénale "
                "réduit la clairance de l'homocystéine, maintenant les taux chroniquement "
                "élevés.</li>"
                "<li><strong>Hypothyroïdie :</strong> Le déficit en hormones thyroïdiennes "
                "peut ralentir le métabolisme de l'homocystéine et augmenter ses taux.</li>"
                "<li><strong>Certains médicaments :</strong> Le méthotrexate, la phénytoïne, "
                "la carbamazépine et le protoxyde d'azote peuvent interférer avec le "
                "métabolisme du folate ou de la B12, élevant les <strong>taux "
                "d'homocystéine</strong>.</li>"
                "</ul>"
                "<p>Une <strong>homocystéine élevée</strong> provoque des dommages oxydatifs à "
                "la paroi vasculaire, une dysfonction endothéliale et une activation de la "
                "cascade de coagulation, augmentant ainsi le risque d'athérosclérose, d'AVC et "
                "de thrombose veineuse profonde. Il est donc essentiel d'identifier et de "
                "traiter la cause sous-jacente.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Un <strong>test d'homocystéine</strong> est recommandé si vous avez des "
                "antécédents familiaux d'infarctus ou d'AVC à un âge précoce, si vous subissez "
                "des fausses couches récurrentes inexpliquées ou si vous avez souffert d'une "
                "thrombose veineuse profonde ou d'une embolie pulmonaire à un jeune âge. Les "
                "personnes porteuses connues de la mutation MTHFR doivent également surveiller "
                "régulièrement leur taux d'homocystéine.</p>"
                "<p>Si votre résultat de l'<strong>analyse sanguine de "
                "l'homocystéine</strong> est élevé, ne paniquez pas mais partagez-le sans "
                "délai avec un interniste ou un cardiologue. Votre médecin évaluera vos taux "
                "de B12, de folate et de B6, demandera si nécessaire un génotypage MTHFR et "
                "vous recommandera une supplémentation vitaminique ou des modifications "
                "alimentaires adaptées. Grâce à une intervention précoce, les <strong>taux "
                "d'homocystéine</strong> peuvent être ramenés dans la norme dans la plupart "
                "des cas.</p>"
                "<p>N'oubliez pas : l'<strong>élévation de l'homocystéine</strong> n'est pas "
                "une maladie en soi mais un facteur de risque traitable. Avec un apport "
                "vitaminique adéquat, une alimentation équilibrée et un suivi régulier, vous "
                "pouvez réduire considérablement votre risque cardiovasculaire. Consultez "
                "toujours votre médecin.</p>"
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
            heading="Esame dell'omocisteina: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test dell'omocisteina</strong> è un <strong>esame del sangue "
                "dell'omocisteina</strong> che misura il livello di questo aminoacido nel "
                "sangue. L'omocisteina è un aminoacido solforato prodotto durante il "
                "metabolismo della metionina e, in condizioni normali, viene convertita in "
                "altri composti grazie alle vitamine B12, folato (B9) e B6. La carenza di "
                "queste vitamine o fattori genetici come la mutazione MTHFR possono portare a "
                "<strong>livelli elevati di omocisteina</strong>.</p>"
                "<p><strong>Alti livelli di omocisteina</strong> — una condizione nota come "
                "<strong>iperomocisteinemia</strong> — sono considerati un fattore di rischio "
                "indipendente per malattie cardiovascolari, ictus e trombosi venosa profonda. "
                "L'eccesso di omocisteina promuove lo stress ossidativo nell'endotelio "
                "vascolare, accelera l'aterosclerosi e aumenta la tendenza alla formazione di "
                "trombi. In questa guida scoprirai i <strong>valori normali di "
                "omocisteina</strong>, le cause dell'<strong>omocisteina alta</strong> e quando "
                "rivolgersi al medico.</p>"
                "<p>La valutazione dei <strong>livelli di omocisteina</strong> è particolarmente "
                "importante per le persone con familiarità per cardiopatia precoce, aborti "
                "ricorrenti o eventi trombotici inspiegati. Una diagnosi precoce e un "
                "trattamento adeguato possono ridurre significativamente il rischio "
                "cardiovascolare.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di omocisteina",
            body_html=(
                "<p>I <strong>valori normali di omocisteina</strong> sono generalmente compresi "
                "tra 5 e 15 µmol/L, sebbene possano verificarsi lievi variazioni in base al "
                "metodo di laboratorio e all'età del paziente. Le linee guida cliniche "
                "classificano i <strong>livelli di omocisteina</strong> in quattro categorie: "
                "normale, lieve, intermedia e grave "
                "<strong>iperomocisteinemia</strong>.</p>"
                "<p>La tabella seguente riassume la classificazione in base ai risultati "
                "dell'<strong>esame del sangue dell'omocisteina</strong>:</p>"
                + _HCY_TABLE_IT +
                "<p>Le donne tendono ad avere <strong>livelli di omocisteina</strong> inferiori "
                "rispetto agli uomini, anche se questa differenza si riduce dopo la menopausa. "
                "La funzionalità renale, le abitudini alimentari e alcuni farmaci possono "
                "influenzare i risultati. Confronta sempre il tuo valore con l'intervallo di "
                "riferimento indicato nel tuo referto di laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di omocisteina alta",
            body_html=(
                "<p>I fattori che portano a <strong>livelli elevati di omocisteina</strong> "
                "spaziano dalle carenze nutrizionali alle mutazioni genetiche. Le principali "
                "cause di <strong>omocisteina alta</strong> includono:</p>"
                "<ul>"
                "<li><strong>Carenza di vitamina B12:</strong> La B12 è essenziale per la "
                "rimetilazione dell'omocisteina a metionina; una sua insufficienza provoca "
                "l'accumulo di omocisteina.</li>"
                "<li><strong>Carenza di folato (B9):</strong> Il folato è un co-substrato "
                "critico nel metabolismo dell'omocisteina e la sua carenza innalza direttamente "
                "i <strong>livelli di omocisteina</strong>.</li>"
                "<li><strong>Carenza di vitamina B6:</strong> La B6 è necessaria per la via "
                "della transulfurazione che converte l'omocisteina in cisteina.</li>"
                "<li><strong>Mutazione del gene MTHFR:</strong> Le varianti C677T o A1298C "
                "dell'enzima metilentetraidrofolato reduttasi (MTHFR) compromettono il "
                "metabolismo del folato e aumentano il rischio di "
                "<strong>iperomocisteinemia</strong>.</li>"
                "<li><strong>Malattia renale cronica:</strong> La perdita di funzionalità "
                "renale riduce la clearance dell'omocisteina, mantenendo i livelli "
                "cronicamente elevati.</li>"
                "<li><strong>Ipotiroidismo:</strong> La carenza di ormoni tiroidei può "
                "rallentare il metabolismo dell'omocisteina e aumentarne i livelli.</li>"
                "<li><strong>Alcuni farmaci:</strong> Metotrexato, fenitoina, carbamazepina e "
                "protossido d'azoto possono interferire con il metabolismo del folato o della "
                "B12, innalzando i <strong>livelli di omocisteina</strong>.</li>"
                "</ul>"
                "<p>L'<strong>omocisteina alta</strong> provoca danno ossidativo alla parete "
                "vascolare, disfunzione endoteliale e attivazione della cascata coagulativa, "
                "aumentando così il rischio di aterosclerosi, ictus e trombosi venosa profonda. "
                "Identificare e trattare la causa sottostante è pertanto fondamentale.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Un <strong>test dell'omocisteina</strong> è consigliato se hai una "
                "familiarità per infarto o ictus in giovane età, se soffri di aborti "
                "ricorrenti inspiegati o se hai avuto una trombosi venosa profonda o "
                "un'embolia polmonare in età giovanile. Anche i portatori noti della mutazione "
                "MTHFR dovrebbero monitorare regolarmente i propri livelli di omocisteina.</p>"
                "<p>Se il risultato del tuo <strong>esame del sangue "
                "dell'omocisteina</strong> è elevato, non allarmarti ma condividi il risultato "
                "senza indugio con un internista o un cardiologo. Il tuo medico valuterà i "
                "livelli di B12, folato e B6, richiederà eventualmente un test genetico MTHFR "
                "e ti consiglierà un'adeguata integrazione vitaminica o modifiche alimentari. "
                "Con un intervento tempestivo, i <strong>livelli di omocisteina</strong> "
                "possono essere riportati nella norma nella maggior parte dei casi.</p>"
                "<p>Ricorda: l'<strong>omocisteina elevata</strong> non è una malattia a sé "
                "stante, bensì un fattore di rischio trattabile. Con il giusto apporto "
                "vitaminico, un'alimentazione equilibrata e un monitoraggio regolare puoi "
                "ridurre significativamente il rischio cardiovascolare. Consulta sempre il "
                "tuo medico.</p>"
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
            heading="בדיקת הומוציסטאין בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת הומוציסטאין</strong> היא <strong>בדיקת דם "
                "להומוציסטאין</strong> המודדת את רמת חומצת האמינו הומוציסטאין בדם. "
                "הומוציסטאין היא חומצת אמינו המכילה גופרית הנוצרת בתהליך חילוף החומרים של "
                "מתיונין, ובתנאים תקינים היא מומרת לתרכובות אחרות בעזרת ויטמינים B12, חומצה "
                "פולית (B9) ו-B6. מחסור בויטמינים אלה או גורמים גנטיים כגון מוטציית MTHFR "
                "עלולים לגרום ל<strong>רמות מוגברות של הומוציסטאין</strong>.</p>"
                "<p><strong>רמות גבוהות של הומוציסטאין</strong> — מצב המכונה "
                "<strong>היפרהומוציסטאינמיה</strong> — נחשבות לגורם סיכון עצמאי למחלת לב "
                "וכלי דם, שבץ מוחי ופקקת ורידים עמוקים. עודף הומוציסטאין מעודד עקה חמצונית "
                "באנדותל כלי הדם, מאיץ טרשת עורקים ומגביר את הנטייה ליצירת קרישי דם. במדריך "
                "זה תלמדו מהם <strong>ערכי הנורמה של הומוציסטאין</strong>, מהם הגורמים "
                "ל<strong>הומוציסטאין גבוה</strong> ומתי יש לפנות לטיפול רפואי.</p>"
                "<p>הערכת <strong>רמות ההומוציסטאין</strong> חשובה במיוחד עבור אנשים עם "
                "היסטוריה משפחתית של מחלת לב מוקדמת, הפלות חוזרות או אירועים תרומבוטיים "
                "בלתי מוסברים. גילוי מוקדם וטיפול מתאים יכולים להפחית באופן משמעותי את "
                "הסיכון הקרדיו-וסקולרי.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של הומוציסטאין",
            body_html=(
                "<p><strong>טווח הנורמה של הומוציסטאין</strong> מתקבל בדרך כלל כ-5–15 µmol/L, "
                "אם כי עשויים להיות הבדלים קלים בהתאם לשיטת המעבדה ולגיל המטופל. הנחיות "
                "קליניות מסווגות את <strong>רמות ההומוציסטאין</strong> לארבע קטגוריות: נורמלי, "
                "קל, בינוני וחמור של <strong>היפרהומוציסטאינמיה</strong>.</p>"
                "<p>הטבלה שלהלן מסכמת את הסיווג בהתאם לתוצאות <strong>בדיקת הדם "
                "להומוציסטאין</strong>:</p>"
                + _HCY_TABLE_HE +
                "<p>נשים נוטות להציג <strong>רמות הומוציסטאין</strong> נמוכות יותר מגברים, "
                "אם כי פער זה מצטמצם לאחר גיל המעבר. תפקוד כלייתי, הרגלי תזונה ותרופות "
                "מסוימות עשויים אף הם להשפיע על התוצאות. השוו תמיד את הערך שלכם לטווח "
                "הייחוס המופיע בדוח המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות הומוציסטאין גבוהות",
            body_html=(
                "<p>הגורמים ל<strong>רמות מוגברות של הומוציסטאין</strong> נעים ממחסור "
                "תזונתי ועד מוטציות גנטיות. הגורמים העיקריים ל<strong>הומוציסטאין "
                "גבוה</strong> כוללים:</p>"
                "<ul>"
                "<li><strong>מחסור בויטמין B12:</strong> B12 חיוני לרמתילציה של הומוציסטאין "
                "חזרה למתיונין; חוסר ב-B12 גורם להצטברות הומוציסטאין.</li>"
                "<li><strong>מחסור בחומצה פולית (B9):</strong> פולאט הוא קו-סובסטרט קריטי "
                "במטבוליזם ההומוציסטאין, ומחסורו מעלה ישירות את <strong>רמות "
                "ההומוציסטאין</strong>.</li>"
                "<li><strong>מחסור בויטמין B6:</strong> B6 נחוץ למסלול הטרנסולפורציה "
                "הממיר הומוציסטאין לציסטאין.</li>"
                "<li><strong>מוטציית גן MTHFR:</strong> הווריאנטים C677T או A1298C של "
                "האנזים מתילנטטרהידרופולאט רדוקטאז (MTHFR) פוגעים במטבוליזם הפולאט "
                "ומגבירים את הסיכון ל<strong>היפרהומוציסטאינמיה</strong>.</li>"
                "<li><strong>מחלת כליות כרונית:</strong> ירידה בתפקוד הכלייתי מפחיתה את "
                "פינוי ההומוציסטאין, ושומרת על רמות גבוהות באופן כרוני.</li>"
                "<li><strong>תת-פעילות בלוטת התריס:</strong> מחסור בהורמוני בלוטת התריס "
                "עלול להאט את חילוף החומרים של הומוציסטאין ולהעלות את הרמות.</li>"
                "<li><strong>תרופות מסוימות:</strong> מתוטרקסט, פניטואין, קרבמזפין "
                "ותחמוצת החנקן עלולים להפריע למטבוליזם הפולאט או ה-B12, ולהעלות את "
                "<strong>רמות ההומוציסטאין</strong>.</li>"
                "</ul>"
                "<p><strong>הומוציסטאין גבוה</strong> גורם לנזק חמצוני לדופן כלי הדם, "
                "תפקוד לקוי של האנדותל והפעלת מפל הקרישה, ובכך מגביר את הסיכון "
                "לטרשת עורקים, שבץ מוחי ופקקת ורידים עמוקים. זיהוי וטיפול בגורם הבסיסי "
                "הם אפוא קריטיים.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p><strong>בדיקת הומוציסטאין</strong> מומלצת אם יש לכם היסטוריה משפחתית "
                "של התקף לב או שבץ בגיל צעיר, אם אתם סובלים מהפלות חוזרות בלתי מוסברות, "
                "או אם סבלתם מפקקת ורידים עמוקים או תסחיף ריאתי בגיל צעיר. גם נשאים ידועים "
                "של מוטציית MTHFR צריכים לעקוב באופן קבוע אחר רמות ההומוציסטאין שלהם.</p>"
                "<p>אם תוצאת <strong>בדיקת הדם להומוציסטאין</strong> שלכם מוגברת, אל "
                "תיבהלו אך שתפו את התוצאה ללא דיחוי עם רופא פנימי או קרדיולוג. הרופא שלכם "
                "יבדוק את רמות ה-B12, הפולאט ו-B6, יבקש במידת הצורך בדיקת גנוטיפ MTHFR "
                "וימליץ על תוסף ויטמינים מתאים או שינויים תזונתיים. בזכות התערבות מוקדמת, "
                "ניתן להחזיר את <strong>רמות ההומוציסטאין</strong> לטווח הנורמלי ברוב "
                "המקרים.</p>"
                "<p>זכרו: <strong>הומוציסטאין מוגבר</strong> אינו מחלה כשלעצמו אלא גורם "
                "סיכון הניתן לטיפול. עם תמיכה ויטמינית נכונה, תזונה מאוזנת ומעקב סדיר "
                "תוכלו להפחית באופן משמעותי את הסיכון הקרדיו-וסקולרי שלכם. התייעצו תמיד עם "
                "הרופא שלכם.</p>"
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
            heading="होमोसिस्टीन ब्लड टेस्ट: आपकी रिपोर्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>होमोसिस्टीन टेस्ट</strong> एक <strong>होमोसिस्टीन ब्लड "
                "टेस्ट</strong> है जो रक्त में अमीनो एसिड होमोसिस्टीन के स्तर को मापता है। "
                "होमोसिस्टीन एक सल्फ़र युक्त अमीनो एसिड है जो मेथिओनीन के मेटाबॉलिज़्म के "
                "दौरान बनता है और सामान्य परिस्थितियों में विटामिन B12, फ़ोलेट (B9) और B6 की "
                "मदद से अन्य यौगिकों में बदल जाता है। इन विटामिनों की कमी या MTHFR म्यूटेशन "
                "जैसे आनुवंशिक कारक <strong>होमोसिस्टीन की ऊँची रेंज</strong> का कारण बन "
                "सकते हैं।</p>"
                "<p><strong>हाई होमोसिस्टीन</strong> लेवल — जिसे "
                "<strong>हाइपरहोमोसिस्टीनीमिया</strong> कहा जाता है — हृदय रोग, स्ट्रोक और "
                "डीप वेन थ्रॉम्बोसिस के लिए एक स्वतंत्र जोखिम कारक माना जाता है। अतिरिक्त "
                "होमोसिस्टीन वैस्कुलर एंडोथीलियम में ऑक्सीडेटिव स्ट्रेस को बढ़ावा देता है, "
                "एथेरोस्क्लेरोसिस को तेज़ करता है और रक्त के थक्के बनने की प्रवृत्ति बढ़ाता "
                "है। इस गाइड में आप <strong>होमोसिस्टीन नॉर्मल रेंज</strong>, "
                "<strong>हाई होमोसिस्टीन</strong> के कारण और डॉक्टर से कब मिलना चाहिए — यह "
                "सब जानेंगे।</p>"
                "<p><strong>होमोसिस्टीन लेवल</strong> का मूल्यांकन विशेष रूप से उन लोगों के "
                "लिए महत्वपूर्ण है जिनके परिवार में कम उम्र में हृदय रोग, बार-बार गर्भपात "
                "या अस्पष्ट थ्रॉम्बोटिक घटनाओं का इतिहास है। शुरुआती पहचान और उचित उपचार "
                "से हृदय संबंधी जोखिम को काफ़ी हद तक कम किया जा सकता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="होमोसिस्टीन के नॉर्मल वैल्यू",
            body_html=(
                "<p><strong>होमोसिस्टीन नॉर्मल रेंज</strong> आम तौर पर 5–15 µmol/L मानी "
                "जाती है, हालाँकि लैब विधि और मरीज़ की उम्र के अनुसार मामूली अंतर हो सकते "
                "हैं। क्लिनिकल गाइडलाइंस <strong>होमोसिस्टीन लेवल</strong> को चार श्रेणियों "
                "में वर्गीकृत करती हैं: सामान्य, हल्की, मध्यम और गंभीर "
                "<strong>हाइपरहोमोसिस्टीनीमिया</strong>।</p>"
                "<p>नीचे दी गई तालिका <strong>होमोसिस्टीन ब्लड टेस्ट</strong> के परिणामों के "
                "आधार पर वर्गीकरण दर्शाती है:</p>"
                + _HCY_TABLE_HI +
                "<p>महिलाओं में <strong>होमोसिस्टीन लेवल</strong> आम तौर पर पुरुषों की "
                "तुलना में कम होता है, हालाँकि मेनोपॉज़ के बाद यह अंतर कम हो जाता है। "
                "किडनी फ़ंक्शन, आहार संबंधी आदतें और कुछ दवाएँ भी परिणामों को प्रभावित कर "
                "सकती हैं। अपने रिज़ल्ट की तुलना हमेशा अपनी लैब रिपोर्ट पर छपी रेफ़रेंस "
                "रेंज से करें।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई होमोसिस्टीन के कारण",
            body_html=(
                "<p><strong>होमोसिस्टीन की ऊँची रेंज</strong> के कारण पोषण संबंधी कमियों से "
                "लेकर आनुवंशिक म्यूटेशन तक फैले हुए हैं। <strong>हाई होमोसिस्टीन</strong> "
                "के प्रमुख कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>विटामिन B12 की कमी:</strong> B12 होमोसिस्टीन को वापस "
                "मेथिओनीन में बदलने के लिए आवश्यक है; अपर्याप्त B12 होने पर होमोसिस्टीन "
                "जमा हो जाता है।</li>"
                "<li><strong>फ़ोलेट (B9) की कमी:</strong> फ़ोलेट होमोसिस्टीन "
                "मेटाबॉलिज़्म में एक महत्वपूर्ण को-सब्सट्रेट है और इसकी कमी सीधे "
                "<strong>होमोसिस्टीन लेवल</strong> को बढ़ाती है।</li>"
                "<li><strong>विटामिन B6 की कमी:</strong> B6 ट्रांससल्फ़्यूरेशन पाथवे के "
                "लिए ज़रूरी है जो होमोसिस्टीन को सिस्टीन में बदलता है।</li>"
                "<li><strong>MTHFR जीन म्यूटेशन:</strong> मिथाइलीनटेट्राहाइड्रोफ़ोलेट "
                "रिडक्टेज़ (MTHFR) एंज़ाइम के C677T या A1298C वेरिएंट फ़ोलेट मेटाबॉलिज़्म "
                "को बाधित करते हैं और <strong>हाइपरहोमोसिस्टीनीमिया</strong> का जोखिम "
                "बढ़ाते हैं।</li>"
                "<li><strong>क्रोनिक किडनी डिज़ीज़:</strong> किडनी फ़ंक्शन में गिरावट "
                "होमोसिस्टीन क्लीयरेंस को कम करती है, जिससे लेवल लंबे समय तक ऊँचा बना "
                "रहता है।</li>"
                "<li><strong>हाइपोथायरॉइडिज़्म:</strong> थायरॉइड हार्मोन की कमी "
                "होमोसिस्टीन मेटाबॉलिज़्म को धीमा कर सकती है और लेवल बढ़ा सकती है।</li>"
                "<li><strong>कुछ दवाएँ:</strong> मेथोट्रेक्सेट, फ़ेनीटोइन, कार्बमेज़ेपीन "
                "और नाइट्रस ऑक्साइड फ़ोलेट या B12 मेटाबॉलिज़्म में बाधा डालकर "
                "<strong>होमोसिस्टीन लेवल</strong> बढ़ा सकती हैं।</li>"
                "</ul>"
                "<p><strong>हाई होमोसिस्टीन</strong> रक्त वाहिका की दीवार में ऑक्सीडेटिव "
                "डैमेज, एंडोथीलियल डिसफ़ंक्शन और कोएगुलेशन कैस्केड की सक्रियता का कारण "
                "बनता है, जिससे एथेरोस्क्लेरोसिस, स्ट्रोक और डीप वेन थ्रॉम्बोसिस का "
                "जोखिम बढ़ जाता है। इसलिए अंतर्निहित कारण की पहचान और उपचार अत्यंत "
                "महत्वपूर्ण है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p><strong>होमोसिस्टीन टेस्ट</strong> की सलाह दी जाती है यदि आपके परिवार "
                "में कम उम्र में हार्ट अटैक या स्ट्रोक का इतिहास है, यदि आपको बार-बार "
                "अस्पष्ट गर्भपात हो रहे हैं, या यदि आपको कम उम्र में डीप वेन थ्रॉम्बोसिस "
                "या पल्मोनरी एम्बोलिज़्म हुआ है। MTHFR म्यूटेशन वाहकों को भी नियमित रूप "
                "से होमोसिस्टीन की निगरानी करानी चाहिए।</p>"
                "<p>यदि आपके <strong>होमोसिस्टीन ब्लड टेस्ट</strong> का रिज़ल्ट बढ़ा हुआ "
                "आता है, तो घबराएँ नहीं लेकिन तुरंत किसी इंटर्निस्ट या कार्डियोलॉजिस्ट से "
                "रिज़ल्ट साझा करें। आपके डॉक्टर B12, फ़ोलेट और B6 लेवल की जाँच करेंगे, "
                "ज़रूरत पड़ने पर MTHFR जीनोटाइपिंग करवाएँगे और उचित विटामिन सप्लीमेंट या "
                "आहार में बदलाव की सलाह देंगे। शुरुआती हस्तक्षेप से अधिकांश मामलों में "
                "<strong>होमोसिस्टीन लेवल</strong> को सामान्य रेंज में लाया जा सकता है।</p>"
                "<p>याद रखें: <strong>बढ़ा हुआ होमोसिस्टीन</strong> अपने आप में कोई बीमारी "
                "नहीं बल्कि एक उपचार योग्य जोखिम कारक है। सही विटामिन सपोर्ट, संतुलित "
                "आहार और नियमित मॉनिटरिंग से आप अपने हृदय संबंधी जोखिम को काफ़ी हद तक कम "
                "कर सकते हैं। हमेशा अपने डॉक्टर से सलाह लें।</p>"
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
            heading="تحليل الهوموسيستين في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p><strong>تحليل الهوموسيستين</strong> هو <strong>فحص دم "
                "للهوموسيستين</strong> يقيس مستوى الحمض الأميني هوموسيستين في الدم. "
                "الهوموسيستين هو حمض أميني يحتوي على الكبريت يُنتَج أثناء أيض الميثيونين، "
                "وفي الظروف الطبيعية يتحول إلى مركبات أخرى بمساعدة فيتامينات B12 والفولات "
                "(B9) وB6. يمكن أن يؤدي نقص هذه الفيتامينات أو عوامل وراثية مثل طفرة MTHFR "
                "إلى <strong>ارتفاع الهوموسيستين</strong>.</p>"
                "<p><strong>مستويات الهوموسيستين المرتفعة</strong> — وهي حالة تُعرف بـ"
                "<strong>فرط هوموسيستين الدم</strong> — تُعتبر عامل خطر مستقلاً لأمراض "
                "القلب والأوعية الدموية والسكتة الدماغية والتخثر الوريدي العميق. يعزز فائض "
                "الهوموسيستين الإجهاد التأكسدي في البطانة الوعائية ويسرّع تصلب الشرايين "
                "ويزيد الميل لتكوين الجلطات الدموية. في هذا الدليل ستتعرفون على "
                "<strong>المستوى الطبيعي للهوموسيستين</strong> وأسباب <strong>ارتفاع "
                "الهوموسيستين</strong> ومتى يجب طلب الرعاية الطبية.</p>"
                "<p>يكتسب تقييم <strong>مستويات الهوموسيستين</strong> أهمية خاصة لدى "
                "الأشخاص الذين لديهم تاريخ عائلي لأمراض القلب المبكرة أو الإجهاض المتكرر "
                "أو أحداث تخثرية غير مفسَّرة. يمكن للكشف المبكر والعلاج المناسب أن يقللا "
                "بشكل ملحوظ من خطر الإصابة بأمراض القلب والأوعية الدموية.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية للهوموسيستين",
            body_html=(
                "<p>يتراوح <strong>المستوى الطبيعي للهوموسيستين</strong> عادةً بين 5 و"
                "15 µmol/L، مع احتمال وجود فروقات طفيفة بحسب طريقة المختبر وعمر المريض. "
                "تُصنّف الإرشادات السريرية <strong>مستويات الهوموسيستين</strong> في أربع "
                "فئات: طبيعي، خفيف، متوسط وشديد من <strong>فرط هوموسيستين الدم</strong>.</p>"
                "<p>يلخّص الجدول أدناه التصنيف بناءً على نتائج <strong>فحص الدم "
                "للهوموسيستين</strong>:</p>"
                + _HCY_TABLE_AR +
                "<p>تميل النساء إلى إظهار <strong>مستويات هوموسيستين</strong> أقل من "
                "الرجال، وإن كان هذا الفارق يتقلّص بعد انقطاع الطمث. قد تؤثر وظائف "
                "الكلى والعادات الغذائية وبعض الأدوية أيضاً على النتائج. قارنوا دائماً "
                "قيمتكم بالنطاق المرجعي المطبوع على تقرير المختبر الخاص بكم.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع الهوموسيستين",
            body_html=(
                "<p>تتنوع العوامل التي تؤدي إلى <strong>ارتفاع الهوموسيستين</strong> من "
                "نقص غذائي إلى طفرات جينية. تشمل الأسباب الرئيسية "
                "ل<strong>ارتفاع الهوموسيستين</strong>:</p>"
                "<ul>"
                "<li><strong>نقص فيتامين B12:</strong> يُعدّ B12 ضرورياً لإعادة مَثْيَلة "
                "الهوموسيستين إلى ميثيونين؛ ونقصه يؤدي إلى تراكم الهوموسيستين.</li>"
                "<li><strong>نقص حمض الفوليك (B9):</strong> الفولات هو ركيزة مشتركة "
                "حيوية في أيض الهوموسيستين، ونقصه يرفع <strong>مستويات "
                "الهوموسيستين</strong> مباشرة.</li>"
                "<li><strong>نقص فيتامين B6:</strong> يُعدّ B6 ضرورياً لمسار "
                "نقل الكبريت الذي يحوّل الهوموسيستين إلى سيستين.</li>"
                "<li><strong>طفرة جين MTHFR:</strong> تؤثر المتغيرات C677T أو A1298C في "
                "إنزيم ميثيلين تتراهيدروفولات ريدكتاز (MTHFR) على أيض الفولات وتزيد "
                "خطر <strong>فرط هوموسيستين الدم</strong>.</li>"
                "<li><strong>مرض الكلى المزمن:</strong> يقلل فقدان الوظيفة الكلوية من "
                "تصفية الهوموسيستين، مما يبقي المستويات مرتفعة بشكل مزمن.</li>"
                "<li><strong>قصور الغدة الدرقية:</strong> قد يؤدي نقص هرمون الغدة "
                "الدرقية إلى إبطاء أيض الهوموسيستين ورفع مستوياته.</li>"
                "<li><strong>بعض الأدوية:</strong> قد يتداخل الميثوتريكسات والفينيتوين "
                "والكاربامازيبين وأكسيد النيتروز مع أيض الفولات أو B12، مما يرفع "
                "<strong>مستويات الهوموسيستين</strong>.</li>"
                "</ul>"
                "<p>يتسبب <strong>ارتفاع الهوموسيستين</strong> في ضرر تأكسدي لجدار "
                "الأوعية الدموية وخلل في البطانة وتنشيط شلال التخثر، مما يزيد خطر "
                "تصلب الشرايين والسكتة الدماغية والتخثر الوريدي العميق. لذلك فإن "
                "تحديد السبب الكامن وعلاجه أمر بالغ الأهمية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>يُوصى بإجراء <strong>تحليل الهوموسيستين</strong> إذا كان لديكم تاريخ "
                "عائلي للإصابة بنوبة قلبية أو سكتة دماغية في سن مبكرة، أو إذا كنتم "
                "تعانون من إجهاض متكرر غير مفسَّر، أو إذا أصبتم بتخثر وريدي عميق أو "
                "انصمام رئوي في سن صغيرة. كذلك يجب على حاملي طفرة MTHFR المعروفين مراقبة "
                "مستويات الهوموسيستين بانتظام.</p>"
                "<p>إذا جاءت نتيجة <strong>فحص الدم للهوموسيستين</strong> مرتفعة، لا "
                "تقلقوا لكن شاركوا النتيجة دون تأخير مع طبيب باطنية أو قلب. سيقوم طبيبكم "
                "بتقييم مستويات B12 والفولات وB6، وقد يطلب فحص الطراز الجيني لـ MTHFR "
                "إن لزم الأمر، وسيوصي بالمكملات الفيتامينية أو التعديلات الغذائية "
                "المناسبة. بفضل التدخل المبكر يمكن إعادة <strong>مستويات "
                "الهوموسيستين</strong> إلى النطاق الطبيعي في معظم الحالات.</p>"
                "<p>تذكّروا: <strong>ارتفاع الهوموسيستين</strong> ليس مرضاً بحد ذاته بل "
                "هو عامل خطر قابل للعلاج. بالدعم الفيتاميني المناسب والنظام الغذائي "
                "المتوازن والمتابعة المنتظمة يمكنكم تقليل خطر الإصابة بأمراض القلب "
                "والأوعية الدموية بشكل كبير. استشيروا دائماً طبيبكم.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_homocysteine_sections_by_lang() -> dict:
    """Returns sections dict for Homocysteine article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_homocysteine_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Homocysteine article (all 9 languages, 3 Q&A each)."""
    return {
        "tr": [
            {"question": "Homosistein testi nedir?",
             "answer": "Homosistein testi, kandaki homosistein aminoasit düzeyini ölçen bir kan testidir. Özellikle kardiyovasküler risk değerlendirmesinde, B12-folat eksikliği araştırmasında ve MTHFR mutasyonu taşıyıcılarında kullanılır."},
            {"question": "Homosistein normal değeri kaçtır?",
             "answer": "Homosistein normal aralığı genellikle 5–15 µmol/L'dir. 15–30 µmol/L hafif, 30–100 µmol/L orta ve 100 µmol/L üzeri ciddi hiperhomosisteinemi olarak sınıflandırılır."},
            {"question": "Homosistein yüksekliği neden önemlidir?",
             "answer": "Yüksek homosistein, damar duvarında oksidatif hasara yol açarak ateroskleroz, inme ve derin ven trombozu riskini artırır. B12, folat ve B6 vitamini takviyesiyle çoğu durumda düzeyler normale getirilebilir."},
        ],
        "en": [
            {"question": "What is a homocysteine test?",
             "answer": "A homocysteine test is a blood test that measures the level of the amino acid homocysteine. It is used primarily for cardiovascular risk assessment, investigation of B12 or folate deficiency, and monitoring individuals with an MTHFR mutation."},
            {"question": "What is the normal homocysteine range?",
             "answer": "The normal homocysteine range is generally 5–15 µmol/L. Levels of 15–30 µmol/L indicate mild, 30–100 µmol/L intermediate, and above 100 µmol/L severe hyperhomocysteinemia."},
            {"question": "Why is high homocysteine important?",
             "answer": "Elevated homocysteine causes oxidative damage to the vessel wall, increasing the risk of atherosclerosis, stroke and deep-vein thrombosis. In most cases levels can be normalised with B12, folate and B6 supplementation."},
        ],
        "es": [
            {"question": "¿Qué es el análisis de homocisteína?",
             "answer": "El análisis de homocisteína es una prueba de sangre que mide el nivel del aminoácido homocisteína. Se utiliza principalmente para la evaluación del riesgo cardiovascular, la investigación de deficiencias de B12 o ácido fólico y el seguimiento de portadores de la mutación MTHFR."},
            {"question": "¿Cuál es el rango normal de homocisteína?",
             "answer": "El rango normal de homocisteína es generalmente de 5–15 µmol/L. Niveles de 15–30 µmol/L indican hiperhomocisteinemia leve, de 30–100 µmol/L intermedia y por encima de 100 µmol/L grave."},
            {"question": "¿Por qué es importante la homocisteína alta?",
             "answer": "La homocisteína elevada causa daño oxidativo en la pared vascular, aumentando el riesgo de aterosclerosis, ictus y trombosis venosa profunda. En la mayoría de los casos, los niveles pueden normalizarse con suplementos de B12, ácido fólico y B6."},
        ],
        "de": [
            {"question": "Was ist ein Homocystein-Test?",
             "answer": "Ein Homocystein-Test ist eine Blutuntersuchung, die den Spiegel der Aminosäure Homocystein misst. Er dient vor allem der kardiovaskulären Risikoabschätzung, der Abklärung eines B12- oder Folsäuremangels und der Überwachung von MTHFR-Mutationsträgern."},
            {"question": "Was sind die Homocystein-Normalwerte?",
             "answer": "Der Normalbereich für Homocystein liegt in der Regel bei 5–15 µmol/L. Werte von 15–30 µmol/L gelten als leichte, 30–100 µmol/L als mittlere und über 100 µmol/L als schwere Hyperhomocysteinämie."},
            {"question": "Warum ist erhöhtes Homocystein wichtig?",
             "answer": "Erhöhtes Homocystein verursacht oxidative Schäden an der Gefäßwand und erhöht das Risiko für Atherosklerose, Schlaganfall und tiefe Venenthrombose. In den meisten Fällen lassen sich die Werte durch B12-, Folsäure- und B6-Supplementierung normalisieren."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'un test d'homocystéine ?",
             "answer": "Le test d'homocystéine est une analyse de sang qui mesure le taux de l'acide aminé homocystéine. Il est principalement utilisé pour l'évaluation du risque cardiovasculaire, la recherche d'une carence en B12 ou en folate et le suivi des porteurs de la mutation MTHFR."},
            {"question": "Quelles sont les valeurs normales d'homocystéine ?",
             "answer": "Les valeurs normales d'homocystéine se situent généralement entre 5 et 15 µmol/L. Des taux de 15–30 µmol/L indiquent une hyperhomocystéinémie légère, de 30–100 µmol/L intermédiaire et au-delà de 100 µmol/L sévère."},
            {"question": "Pourquoi l'homocystéine élevée est-elle importante ?",
             "answer": "L'homocystéine élevée provoque des dommages oxydatifs à la paroi vasculaire, augmentant le risque d'athérosclérose, d'AVC et de thrombose veineuse profonde. Dans la plupart des cas, les taux peuvent être normalisés grâce à une supplémentation en B12, folate et B6."},
        ],
        "it": [
            {"question": "Cos'è il test dell'omocisteina?",
             "answer": "Il test dell'omocisteina è un esame del sangue che misura il livello dell'aminoacido omocisteina. Viene utilizzato principalmente per la valutazione del rischio cardiovascolare, l'indagine di carenze di B12 o folato e il monitoraggio dei portatori della mutazione MTHFR."},
            {"question": "Quali sono i valori normali di omocisteina?",
             "answer": "I valori normali di omocisteina sono generalmente compresi tra 5 e 15 µmol/L. Livelli di 15–30 µmol/L indicano iperomocisteinemia lieve, 30–100 µmol/L intermedia e oltre 100 µmol/L grave."},
            {"question": "Perché l'omocisteina alta è importante?",
             "answer": "L'omocisteina elevata causa danno ossidativo alla parete vascolare, aumentando il rischio di aterosclerosi, ictus e trombosi venosa profonda. Nella maggior parte dei casi i livelli possono essere normalizzati con l'integrazione di B12, folato e B6."},
        ],
        "he": [
            {"question": "מהי בדיקת הומוציסטאין?",
             "answer": "בדיקת הומוציסטאין היא בדיקת דם המודדת את רמת חומצת האמינו הומוציסטאין. היא משמשת בעיקר להערכת סיכון קרדיו-וסקולרי, לבירור מחסור ב-B12 או בפולאט ולמעקב אחר נשאי מוטציית MTHFR."},
            {"question": "מהם ערכי הנורמה של הומוציסטאין?",
             "answer": "טווח הנורמה של הומוציסטאין הוא בדרך כלל 5–15 µmol/L. רמות של 15–30 µmol/L מעידות על היפרהומוציסטאינמיה קלה, 30–100 µmol/L בינונית ומעל 100 µmol/L חמורה."},
            {"question": "מדוע הומוציסטאין גבוה חשוב?",
             "answer": "הומוציסטאין מוגבר גורם לנזק חמצוני לדופן כלי הדם ומגביר את הסיכון לטרשת עורקים, שבץ מוחי ופקקת ורידים עמוקים. ברוב המקרים ניתן לנרמל את הרמות באמצעות תוספי B12, פולאט ו-B6."},
        ],
        "hi": [
            {"question": "होमोसिस्टीन टेस्ट क्या है?",
             "answer": "होमोसिस्टीन टेस्ट एक ब्लड टेस्ट है जो अमीनो एसिड होमोसिस्टीन के स्तर को मापता है। इसका उपयोग मुख्य रूप से हृदय संबंधी जोखिम मूल्यांकन, B12 या फ़ोलेट की कमी की जाँच और MTHFR म्यूटेशन वाहकों की निगरानी के लिए किया जाता है।"},
            {"question": "होमोसिस्टीन की नॉर्मल रेंज क्या है?",
             "answer": "होमोसिस्टीन की सामान्य रेंज आम तौर पर 5–15 µmol/L होती है। 15–30 µmol/L हल्की, 30–100 µmol/L मध्यम और 100 µmol/L से अधिक गंभीर हाइपरहोमोसिस्टीनीमिया दर्शाती है।"},
            {"question": "हाई होमोसिस्टीन क्यों महत्वपूर्ण है?",
             "answer": "बढ़ा हुआ होमोसिस्टीन रक्त वाहिका की दीवार में ऑक्सीडेटिव डैमेज करता है, जिससे एथेरोस्क्लेरोसिस, स्ट्रोक और डीप वेन थ्रॉम्बोसिस का जोखिम बढ़ जाता है। अधिकांश मामलों में B12, फ़ोलेट और B6 सप्लीमेंट से लेवल सामान्य किए जा सकते हैं।"},
        ],
        "ar": [
            {"question": "ما هو تحليل الهوموسيستين؟",
             "answer": "تحليل الهوموسيستين هو فحص دم يقيس مستوى الحمض الأميني هوموسيستين. يُستخدم بشكل رئيسي لتقييم خطر الإصابة بأمراض القلب والأوعية الدموية، والكشف عن نقص B12 أو الفولات، ومتابعة حاملي طفرة MTHFR."},
            {"question": "ما هو المستوى الطبيعي للهوموسيستين؟",
             "answer": "يتراوح المستوى الطبيعي للهوموسيستين عادةً بين 5 و15 µmol/L. تشير مستويات 15–30 µmol/L إلى فرط خفيف، و30–100 µmol/L إلى فرط متوسط، وأكثر من 100 µmol/L إلى فرط شديد في هوموسيستين الدم."},
            {"question": "لماذا يُعدّ ارتفاع الهوموسيستين مهماً؟",
             "answer": "يسبب ارتفاع الهوموسيستين ضرراً تأكسدياً لجدار الأوعية الدموية، مما يزيد خطر تصلب الشرايين والسكتة الدماغية والتخثر الوريدي العميق. في معظم الحالات يمكن تطبيع المستويات بمكملات B12 والفولات وB6."},
        ],
    }
