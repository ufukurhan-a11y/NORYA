# -*- coding: utf-8 -*-
"""
CK / CPK (Creatine Kinase) blog article — full body content for all 9 languages.
Used by blog_i18n._article_ck().
Sections: intro, normal-ranges, causes, when-to-see-doctor.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_CK_TABLE_TR = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Cinsiyet</th><th>CK Normal Aralığı (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>Erkek</td><td>39 – 308</td></tr>"
    "<tr><td>Kadın</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_EN = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Sex</th><th>CK Normal Range (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>Male</td><td>39 – 308</td></tr>"
    "<tr><td>Female</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_ES = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Sexo</th><th>Rango normal de CK (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>Hombre</td><td>39 – 308</td></tr>"
    "<tr><td>Mujer</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_DE = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Geschlecht</th><th>CK-Normbereich (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>Männer</td><td>39 – 308</td></tr>"
    "<tr><td>Frauen</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_FR = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Sexe</th><th>Valeurs normales de CK (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>Homme</td><td>39 – 308</td></tr>"
    "<tr><td>Femme</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_IT = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Sesso</th><th>Intervallo normale di CK (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>Uomo</td><td>39 – 308</td></tr>"
    "<tr><td>Donna</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_HE = (
    '<table class="table table-bordered table-sm mt-3 mb-3" dir="rtl">'
    "<thead><tr><th>מין</th><th>טווח נורמלי של CK&rlm; (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>גבר</td><td>39 – 308</td></tr>"
    "<tr><td>אישה</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_HI = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>लिंग</th><th>CK नॉर्मल रेंज (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>पुरुष</td><td>39 – 308</td></tr>"
    "<tr><td>महिला</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)

_CK_TABLE_AR = (
    '<table class="table table-bordered table-sm mt-3 mb-3" dir="rtl">'
    "<thead><tr><th>الجنس</th><th>النطاق الطبيعي لـ CK&rlm; (U/L)</th></tr></thead>"
    "<tbody>"
    "<tr><td>ذكر</td><td>39 – 308</td></tr>"
    "<tr><td>أنثى</td><td>26 – 192</td></tr>"
    "</tbody></table>"
)


# ─────────────────────────────────────────────────────────────────────
# TURKISH
# ─────────────────────────────────────────────────────────────────────
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="CK (Kreatin Kinaz) kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>CK kan testi</strong> (kreatin kinaz, eski adıyla <strong>CPK testi</strong>), "
                "kas ve kalp dokusunda yoğun olarak bulunan bir enzimin kandaki düzeyini ölçer. "
                "Kreatin kinaz, hücrelerin enerji üretiminde kritik rol oynar; kas lifleri hasar "
                "gördüğünde enzim kana sızarak <strong>CK yüksekliğine</strong> neden olur. Bu "
                "nedenle CK, klinik pratikte güvenilir bir <strong>kas hasarı kan testi</strong> "
                "olarak kabul edilir.</p>"
                "<p>CK enziminin üç ana izoformu vardır: iskelet kasında baskın olan <em>CK-MM</em>, "
                "kalp kasında yoğunlaşan <strong>CK-MB</strong> ve beyin dokusunda bulunan "
                "<em>CK-BB</em>. Özellikle <strong>CK-MB</strong> izoformu, akut miyokard "
                "enfarktüsü (kalp krizi) tanısında yıllardır kullanılan önemli bir biyobelirteçtir. "
                "Toplam CK düzeyindeki artış ise kas hasarının genel bir göstergesidir.</p>"
                "<p>Bu rehberde <strong>CK normal değerlerini</strong>, yüksek CK'nın olası "
                "nedenlerini — yoğun egzersizden rabdomiyolize, statin yan etkilerinden kalp "
                "krizine kadar — ve ne zaman doktora başvurmanız gerektiğini ayrıntılı olarak "
                "öğreneceksiniz.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="CK normal değerleri (referans aralıkları)",
            body_html=(
                "<p><strong>CK normal aralığı</strong> cinsiyete, kas kütlesine ve laboratuvar "
                "yöntemine göre değişiklik gösterir. Erkeklerde kas kütlesi daha fazla olduğundan "
                "üst sınır kadınlara kıyasla yüksektir. Aşağıdaki tabloda yetişkinler için genel "
                "kabul görmüş <strong>CK referans aralıkları</strong> verilmiştir:</p>"
                + _CK_TABLE_TR +
                "<p>Yoğun fiziksel aktivite sonrasında CK düzeyi sağlıklı bireylerde bile normalin "
                "birkaç katına çıkabilir; bu durum genellikle 3–5 gün içinde kendiliğinden düzelir. "
                "Koyu tenli bireylerde, kas kütlesi yüksek sporcularda ve çocuklarda referans "
                "aralıkları farklılık gösterebilir. Sonuçlarınızı her zaman laboratuvar raporunuzdaki "
                "referans aralığıyla karşılaştırmalısınız.</p>"
                "<p>CK düzeyinin normalin beş katını aşması klinik açıdan anlamlı kabul edilir "
                "ve altta yatan bir patoloji araştırılmalıdır. On katı geçen değerlerde "
                "rabdomiyoliz riski ciddi biçimde değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="CK yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>CK yüksekliği</strong> (veya <strong>CPK yüksekliği</strong>) çok "
                "çeşitli nedenlerden kaynaklanabilir. Yüksek CK her zaman ciddi bir hastalığı "
                "işaret etmez; ancak bazı durumlarda acil müdahale gerektirebilir. Başlıca "
                "nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Yoğun egzersiz:</strong> Ağırlık antrenmanı, maraton koşusu veya "
                "alışılmadık fiziksel aktivite CK'yı geçici olarak belirgin ölçüde artırabilir.</li>"
                "<li><strong>Rabdomiyoliz:</strong> Kas liflerinin aşırı yıkımı sonucu "
                "miyoglobin ve CK kana büyük miktarda salınır; tedavi edilmezse akut böbrek "
                "yetmezliğine yol açabilir.</li>"
                "<li><strong>Miyokard enfarktüsü (kalp krizi):</strong> Kalp kası hasarında "
                "<strong>CK-MB</strong> belirgin şekilde yükselir; troponin ile birlikte tanıda "
                "kullanılır.</li>"
                "<li><strong>Statin yan etkileri:</strong> Kolesterol düşürücü statin grubu "
                "ilaçlar bazı hastalarda kas ağrısı (miyalji) ve CK yüksekliğine neden "
                "olabilir; nadir durumlarda statin miyopatisi gelişebilir.</li>"
                "<li><strong>Kas hastalıkları:</strong> Müsküler distrofi, polimiyozit, "
                "dermatomiyozit gibi inflamatuvar ve genetik kas hastalıkları kronik CK "
                "yüksekliğine yol açar.</li>"
                "<li><strong>Travma ve cerrahi:</strong> Kas dokusuna yönelik fiziksel hasar "
                "veya büyük cerrahi işlemler sonrası CK düzeyi yükselir.</li>"
                "<li><strong>Hipotiroidizm:</strong> Tiroid hormon eksikliği kas metabolizmasını "
                "bozarak CK artışına neden olabilir.</li>"
                "</ul>"
                "<p>CK düzeyi tek başına tanı koydurmaz. Yüksekliğin nedeni; klinik bulgular, "
                "CK izoformları (CK-MB, CK-MM), troponin, böbrek fonksiyon testleri ve kas "
                "enzimlerinin seri takibi ile birlikte değerlendirilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>CK kan testi sonucunuz yüksek çıktığında veya aşağıdaki belirtilerden herhangi "
                "biri eşlik ettiğinde vakit kaybetmeden doktora başvurmanız önerilir:</p>"
                "<ul>"
                "<li>Şiddetli ve yaygın kas ağrısı, güçsüzlük veya şişlik</li>"
                "<li>Koyu renkli (çay renginde) idrar — rabdomiyoliz belirtisi olabilir</li>"
                "<li>Göğüs ağrısı, nefes darlığı veya sol kola yayılan ağrı — kalp krizi "
                "olasılığında acil yardım arayın</li>"
                "<li>Statin kullanırken ortaya çıkan açıklanamayan kas ağrıları</li>"
                "<li>CK düzeyinin ardışık ölçümlerde düşmemesi veya artmaya devam etmesi</li>"
                "</ul>"
                "<p>Egzersiz sonrası hafif CK yükselmesi genellikle endişe verici değildir; "
                "ancak değer normalin on katını aşıyorsa veya böbrek fonksiyonlarınız "
                "bozulmuşsa acil tıbbi değerlendirme şarttır. Sonuçlarınızı kendi başınıza "
                "yorumlamak yerine mutlaka hekiminizle paylaşın.</p>"
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
            heading="CK blood test: what your results mean",
            body_html=(
                "<p>The <strong>CK blood test</strong> (creatine kinase, formerly known as the "
                "<strong>CPK test</strong>) measures the level of an enzyme found predominantly "
                "in skeletal muscle, the heart, and the brain. Creatine kinase plays a key role "
                "in cellular energy production; when muscle fibres are damaged the enzyme leaks "
                "into the bloodstream, causing <strong>high CK levels</strong>. This makes CK a "
                "reliable <strong>muscle damage blood test</strong> in clinical practice.</p>"
                "<p>CK exists in three main isoforms: <em>CK-MM</em>, which predominates in "
                "skeletal muscle; <strong>CK-MB</strong>, concentrated in the heart muscle; and "
                "<em>CK-BB</em>, found in brain tissue. The <strong>CK-MB</strong> isoform has "
                "historically been an important biomarker for diagnosing acute myocardial "
                "infarction (heart attack). A rise in total CK serves as a general indicator "
                "of muscle injury.</p>"
                "<p>In this guide you will learn the <strong>CK normal range</strong>, the "
                "possible causes of <strong>CPK elevated</strong> results — from intense "
                "exercise to rhabdomyolysis, statin side effects to heart attack — and when "
                "you should see a doctor.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="CK normal range (reference intervals)",
            body_html=(
                "<p>The <strong>CK normal range</strong> varies by sex, muscle mass, and "
                "laboratory method. Because men generally have greater muscle mass, the upper "
                "limit is higher than in women. The table below shows the widely accepted "
                "reference intervals for adults:</p>"
                + _CK_TABLE_EN +
                "<p>After intense physical activity, CK can rise several-fold even in healthy "
                "individuals; levels typically normalise within 3–5 days. Reference ranges may "
                "also differ in people of African descent, high-performance athletes, and "
                "children. Always compare your result with the reference range printed on your "
                "own laboratory report.</p>"
                "<p>A CK level exceeding five times the upper limit of normal is considered "
                "clinically significant and warrants investigation. Values above ten times normal "
                "raise serious concern for rhabdomyolysis and require urgent evaluation.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high CK levels",
            body_html=(
                "<p><strong>High CK levels</strong> (or <strong>CPK elevated</strong>) can stem "
                "from a wide variety of causes. An elevated CK does not always point to serious "
                "disease, but in certain situations it may require urgent intervention. The main "
                "causes include:</p>"
                "<ul>"
                "<li><strong>Intense exercise:</strong> Weight training, marathon running, or "
                "unaccustomed physical activity can temporarily raise CK significantly.</li>"
                "<li><strong>Rhabdomyolysis:</strong> Excessive breakdown of muscle fibres "
                "releases large amounts of myoglobin and CK into the bloodstream; if untreated, "
                "it can lead to acute kidney failure.</li>"
                "<li><strong>Myocardial infarction (heart attack):</strong> Damage to the heart "
                "muscle causes a marked rise in <strong>CK-MB</strong>, which is used alongside "
                "troponin for diagnosis.</li>"
                "<li><strong>Statin side effects:</strong> Cholesterol-lowering statin drugs "
                "can cause muscle pain (myalgia) and elevated CK in some patients; in rare "
                "cases statin myopathy may develop.</li>"
                "<li><strong>Muscle diseases:</strong> Muscular dystrophy, polymyositis, and "
                "dermatomyositis cause chronically elevated CK.</li>"
                "<li><strong>Trauma and surgery:</strong> Physical injury to muscle tissue or "
                "major surgical procedures raise CK levels.</li>"
                "<li><strong>Hypothyroidism:</strong> Thyroid hormone deficiency can impair "
                "muscle metabolism, leading to CK elevation.</li>"
                "</ul>"
                "<p>CK alone is not diagnostic. The cause of an elevated result is determined "
                "by clinical findings, CK isoforms (CK-MB, CK-MM), troponin levels, kidney "
                "function tests, and serial monitoring of muscle enzymes.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your <strong>CK blood test</strong> result is elevated or you experience "
                "any of the following symptoms, seek medical advice promptly:</p>"
                "<ul>"
                "<li>Severe, widespread muscle pain, weakness, or swelling</li>"
                "<li>Dark (tea-coloured) urine — a possible sign of rhabdomyolysis</li>"
                "<li>Chest pain, shortness of breath, or pain radiating to the left arm — "
                "call emergency services if a heart attack is suspected</li>"
                "<li>Unexplained muscle aches while taking statins</li>"
                "<li>CK levels that do not decline or continue to rise on repeat testing</li>"
                "</ul>"
                "<p>A mild post-exercise CK elevation is usually not a cause for concern. "
                "However, if the value exceeds ten times the upper limit of normal or your "
                "kidney function is compromised, urgent medical evaluation is essential. "
                "Always discuss your results with your doctor rather than interpreting them "
                "on your own.</p>"
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
            heading="Análisis de CK en sangre: qué significan tus resultados",
            body_html=(
                "<p>El <strong>análisis de CK</strong> (creatina quinasa, antes conocido como "
                "<strong>prueba de CPK</strong>) mide el nivel de una enzima que se encuentra "
                "principalmente en el músculo esquelético, el corazón y el cerebro. La creatina "
                "quinasa desempeña un papel clave en la producción de energía celular; cuando "
                "las fibras musculares se dañan, la enzima se libera al torrente sanguíneo "
                "provocando <strong>niveles elevados de CK</strong>. Por ello, la CK es "
                "considerada una <strong>prueba de daño muscular en sangre</strong> fiable.</p>"
                "<p>Existen tres isoformas principales de CK: <em>CK-MM</em>, predominante en "
                "el músculo esquelético; <strong>CK-MB</strong>, concentrada en el músculo "
                "cardíaco; y <em>CK-BB</em>, presente en el tejido cerebral. La isoforma "
                "<strong>CK-MB</strong> ha sido históricamente un biomarcador importante para "
                "el diagnóstico del infarto agudo de miocardio. Un aumento de la CK total "
                "constituye un indicador general de lesión muscular.</p>"
                "<p>En esta guía conocerás el <strong>rango normal de CK</strong>, las posibles "
                "causas de una <strong>CPK elevada</strong> — desde el ejercicio intenso hasta "
                "la rabdomiólisis, los efectos secundarios de las estatinas y el infarto — y "
                "cuándo consultar al médico.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de CK (intervalos de referencia)",
            body_html=(
                "<p>El <strong>rango normal de CK</strong> varía según el sexo, la masa muscular "
                "y el método de laboratorio. Dado que los hombres suelen tener mayor masa muscular, "
                "el límite superior es más alto que en las mujeres. La siguiente tabla muestra los "
                "intervalos de referencia aceptados para adultos:</p>"
                + _CK_TABLE_ES +
                "<p>Tras una actividad física intensa, la CK puede elevarse varias veces su "
                "valor normal incluso en personas sanas; los niveles suelen normalizarse en "
                "3–5 días. Los rangos de referencia pueden diferir en personas de ascendencia "
                "africana, deportistas de alto rendimiento y niños. Compara siempre tu resultado "
                "con el rango indicado en tu propio informe de laboratorio.</p>"
                "<p>Un nivel de CK que supere cinco veces el límite superior de la normalidad "
                "se considera clínicamente significativo y requiere investigación. Valores por "
                "encima de diez veces el límite normal generan seria preocupación por "
                "rabdomiólisis y exigen evaluación urgente.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de CK elevada",
            body_html=(
                "<p>Los <strong>niveles elevados de CK</strong> (o <strong>CPK elevada</strong>) "
                "pueden deberse a causas muy diversas. Una CK alta no siempre indica una "
                "enfermedad grave, pero en determinadas situaciones puede requerir intervención "
                "urgente. Las principales causas son:</p>"
                "<ul>"
                "<li><strong>Ejercicio intenso:</strong> El entrenamiento con pesas, las "
                "carreras de maratón o la actividad física no habitual pueden elevar la CK "
                "transitoriamente de forma notable.</li>"
                "<li><strong>Rabdomiólisis:</strong> La destrucción excesiva de fibras musculares "
                "libera grandes cantidades de mioglobina y CK al torrente sanguíneo; sin "
                "tratamiento puede provocar insuficiencia renal aguda.</li>"
                "<li><strong>Infarto de miocardio:</strong> El daño al músculo cardíaco provoca "
                "un aumento marcado de la <strong>CK-MB</strong>, que se utiliza junto con la "
                "troponina para el diagnóstico.</li>"
                "<li><strong>Efectos secundarios de las estatinas:</strong> Los fármacos "
                "hipolipemiantes del grupo de las estatinas pueden causar dolor muscular "
                "(mialgia) y elevación de la CK; en casos raros se desarrolla miopatía "
                "por estatinas.</li>"
                "<li><strong>Enfermedades musculares:</strong> La distrofia muscular, la "
                "polimiositis y la dermatomiositis cursan con CK crónicamente elevada.</li>"
                "<li><strong>Traumatismos y cirugía:</strong> Las lesiones físicas del tejido "
                "muscular o las intervenciones quirúrgicas mayores elevan la CK.</li>"
                "<li><strong>Hipotiroidismo:</strong> El déficit de hormonas tiroideas puede "
                "alterar el metabolismo muscular, provocando un aumento de la CK.</li>"
                "</ul>"
                "<p>La CK por sí sola no es diagnóstica. La causa de la elevación se determina "
                "mediante hallazgos clínicos, isoformas de CK (CK-MB, CK-MM), troponina, "
                "pruebas de función renal y seguimiento seriado de enzimas musculares.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debes consultar al médico?",
            body_html=(
                "<p>Si tu resultado de CK es elevado o presentas alguno de los siguientes "
                "síntomas, busca atención médica sin demora:</p>"
                "<ul>"
                "<li>Dolor muscular intenso y generalizado, debilidad o hinchazón</li>"
                "<li>Orina oscura (color té) — posible signo de rabdomiólisis</li>"
                "<li>Dolor en el pecho, dificultad para respirar o dolor irradiado al brazo "
                "izquierdo — llama a urgencias si se sospecha un infarto</li>"
                "<li>Dolores musculares inexplicables mientras tomas estatinas</li>"
                "<li>Niveles de CK que no descienden o siguen aumentando en mediciones sucesivas</li>"
                "</ul>"
                "<p>Una elevación leve de la CK tras el ejercicio no suele ser motivo de "
                "preocupación. Sin embargo, si el valor supera diez veces el límite superior "
                "de la normalidad o tu función renal está comprometida, es imprescindible una "
                "evaluación médica urgente. Consulta siempre a tu médico en lugar de interpretar "
                "los resultados por tu cuenta.</p>"
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
            heading="CK-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>CK-Bluttest</strong> (Kreatinkinase, früher als <strong>CPK-Test</strong> "
                "bezeichnet) misst den Spiegel eines Enzyms, das vor allem in der Skelettmuskulatur, "
                "im Herzen und im Gehirn vorkommt. Kreatinkinase spielt eine zentrale Rolle bei der "
                "zellulären Energieproduktion; werden Muskelfasern geschädigt, gelangt das Enzym "
                "ins Blut und verursacht <strong>hohe CK-Werte</strong>. Daher gilt CK als "
                "zuverlässiger <strong>Bluttest für Muskelschäden</strong> in der klinischen Praxis.</p>"
                "<p>CK liegt in drei Hauptisoformen vor: <em>CK-MM</em>, vorherrschend in der "
                "Skelettmuskulatur; <strong>CK-MB</strong>, konzentriert im Herzmuskel; und "
                "<em>CK-BB</em>, im Hirngewebe. Die Isoform <strong>CK-MB</strong> war "
                "traditionell ein wichtiger Biomarker für die Diagnose des akuten Myokardinfarkts "
                "(Herzinfarkt). Ein Anstieg der Gesamt-CK ist ein allgemeiner Indikator für "
                "Muskelverletzungen.</p>"
                "<p>In diesem Ratgeber erfahren Sie den <strong>CK-Normbereich</strong>, die "
                "möglichen Ursachen einer <strong>erhöhten CPK</strong> — von intensivem Sport "
                "über Rhabdomyolyse und Statin-Nebenwirkungen bis zum Herzinfarkt — und wann "
                "Sie einen Arzt aufsuchen sollten.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="CK-Normwerte (Referenzbereiche)",
            body_html=(
                "<p>Der <strong>CK-Normbereich</strong> variiert je nach Geschlecht, Muskelmasse "
                "und Labormethode. Da Männer in der Regel eine größere Muskelmasse haben, liegt "
                "die Obergrenze höher als bei Frauen. Die folgende Tabelle zeigt die allgemein "
                "anerkannten Referenzbereiche für Erwachsene:</p>"
                + _CK_TABLE_DE +
                "<p>Nach intensiver körperlicher Aktivität kann der CK-Wert selbst bei gesunden "
                "Personen auf das Mehrfache ansteigen; die Werte normalisieren sich in der Regel "
                "innerhalb von 3–5 Tagen. Referenzbereiche können bei Menschen afrikanischer "
                "Abstammung, Leistungssportlern und Kindern abweichen. Vergleichen Sie Ihr "
                "Ergebnis stets mit dem Referenzbereich auf Ihrem eigenen Laborbefund.</p>"
                "<p>Ein CK-Wert, der das Fünffache der oberen Normgrenze übersteigt, gilt als "
                "klinisch relevant und sollte abgeklärt werden. Werte über dem Zehnfachen der "
                "Normgrenze lassen ernsthaft an eine Rhabdomyolyse denken und erfordern eine "
                "dringende Abklärung.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für hohe CK-Werte",
            body_html=(
                "<p><strong>Hohe CK-Werte</strong> (oder <strong>erhöhte CPK</strong>) können "
                "vielfältige Ursachen haben. Eine erhöhte CK weist nicht immer auf eine schwere "
                "Erkrankung hin, kann aber in bestimmten Situationen eine dringende Behandlung "
                "erfordern. Die wichtigsten Ursachen sind:</p>"
                "<ul>"
                "<li><strong>Intensiver Sport:</strong> Krafttraining, Marathonlauf oder "
                "ungewohnte körperliche Belastung können die CK vorübergehend deutlich erhöhen.</li>"
                "<li><strong>Rhabdomyolyse:</strong> Der übermäßige Zerfall von Muskelfasern setzt "
                "große Mengen Myoglobin und CK ins Blut frei; unbehandelt kann dies zu akutem "
                "Nierenversagen führen.</li>"
                "<li><strong>Myokardinfarkt (Herzinfarkt):</strong> Die Schädigung des Herzmuskels "
                "führt zu einem deutlichen Anstieg der <strong>CK-MB</strong>, die zusammen mit "
                "Troponin zur Diagnose herangezogen wird.</li>"
                "<li><strong>Statin-Nebenwirkungen:</strong> Cholesterinsenkende Statine können bei "
                "manchen Patienten Muskelschmerzen (Myalgie) und eine CK-Erhöhung verursachen; "
                "in seltenen Fällen kann sich eine Statin-Myopathie entwickeln.</li>"
                "<li><strong>Muskelerkrankungen:</strong> Muskeldystrophie, Polymyositis und "
                "Dermatomyositis führen zu chronisch erhöhten CK-Werten.</li>"
                "<li><strong>Trauma und Operationen:</strong> Physische Verletzungen des "
                "Muskelgewebes oder größere chirurgische Eingriffe erhöhen die CK.</li>"
                "<li><strong>Hypothyreose:</strong> Ein Mangel an Schilddrüsenhormonen kann den "
                "Muskelstoffwechsel beeinträchtigen und zu einem CK-Anstieg führen.</li>"
                "</ul>"
                "<p>Die CK allein ist nicht diagnostisch. Die Ursache einer Erhöhung wird anhand "
                "klinischer Befunde, CK-Isoformen (CK-MB, CK-MM), Troponinwerten, "
                "Nierenfunktionstests und serieller Überwachung der Muskelenzyme beurteilt.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie zum Arzt gehen?",
            body_html=(
                "<p>Wenn Ihr <strong>CK-Bluttest</strong> erhöhte Werte zeigt oder Sie eines "
                "der folgenden Symptome bemerken, suchen Sie zeitnah ärztlichen Rat:</p>"
                "<ul>"
                "<li>Starke, ausgedehnte Muskelschmerzen, Schwäche oder Schwellung</li>"
                "<li>Dunkler (teefarbener) Urin — mögliches Zeichen einer Rhabdomyolyse</li>"
                "<li>Brustschmerzen, Atemnot oder in den linken Arm ausstrahlende Schmerzen — "
                "rufen Sie bei Verdacht auf einen Herzinfarkt sofort den Notarzt</li>"
                "<li>Unerklärliche Muskelschmerzen unter Statin-Therapie</li>"
                "<li>CK-Werte, die bei Kontrollmessungen nicht sinken oder weiter ansteigen</li>"
                "</ul>"
                "<p>Eine leichte CK-Erhöhung nach dem Sport ist in der Regel unbedenklich. "
                "Übersteigt der Wert jedoch das Zehnfache der oberen Normgrenze oder ist Ihre "
                "Nierenfunktion beeinträchtigt, ist eine dringende ärztliche Beurteilung "
                "unerlässlich. Besprechen Sie Ihre Ergebnisse stets mit Ihrem Arzt, anstatt "
                "sie eigenständig zu interpretieren.</p>"
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
            heading="Analyse de CK (CPK) : que signifient vos résultats ?",
            body_html=(
                "<p>L'<strong>analyse de CK</strong> (créatine kinase, anciennement appelée "
                "<strong>test CPK</strong>) mesure le taux d'une enzyme présente principalement "
                "dans le muscle squelettique, le cœur et le cerveau. La créatine kinase joue un "
                "rôle essentiel dans la production d'énergie cellulaire ; lorsque les fibres "
                "musculaires sont endommagées, l'enzyme passe dans le sang, entraînant des "
                "<strong>taux élevés de CK</strong>. C'est pourquoi la CK est considérée comme "
                "un <strong>marqueur sanguin fiable de lésion musculaire</strong>.</p>"
                "<p>La CK existe sous trois isoformes principales : <em>CK-MM</em>, prédominante "
                "dans le muscle squelettique ; <strong>CK-MB</strong>, concentrée dans le muscle "
                "cardiaque ; et <em>CK-BB</em>, présente dans le tissu cérébral. L'isoforme "
                "<strong>CK-MB</strong> est historiquement un biomarqueur important pour le "
                "diagnostic de l'infarctus aigu du myocarde (crise cardiaque). Une élévation de "
                "la CK totale constitue un indicateur général de lésion musculaire.</p>"
                "<p>Dans ce guide, vous découvrirez les <strong>valeurs normales de CK</strong>, "
                "les causes possibles d'une <strong>CPK élevée</strong> — de l'exercice intense "
                "à la rhabdomyolyse, en passant par les effets secondaires des statines et "
                "l'infarctus — et quand consulter un médecin.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de CK (intervalles de référence)",
            body_html=(
                "<p>Les <strong>valeurs normales de CK</strong> varient selon le sexe, la masse "
                "musculaire et la méthode de laboratoire. Les hommes ayant généralement une masse "
                "musculaire plus importante, la limite supérieure est plus élevée que chez les "
                "femmes. Le tableau ci-dessous présente les intervalles de référence couramment "
                "admis pour les adultes :</p>"
                + _CK_TABLE_FR +
                "<p>Après une activité physique intense, la CK peut augmenter de plusieurs fois "
                "sa valeur normale même chez des personnes en bonne santé ; les taux se "
                "normalisent généralement en 3 à 5 jours. Les intervalles de référence peuvent "
                "aussi différer chez les personnes d'origine africaine, les sportifs de haut "
                "niveau et les enfants. Comparez toujours votre résultat avec l'intervalle "
                "figurant sur votre propre compte rendu de laboratoire.</p>"
                "<p>Un taux de CK dépassant cinq fois la limite supérieure de la normale est "
                "considéré comme cliniquement significatif et justifie des investigations. "
                "Des valeurs supérieures à dix fois la normale font craindre une rhabdomyolyse "
                "et nécessitent une évaluation urgente.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une CK élevée",
            body_html=(
                "<p>Des <strong>taux élevés de CK</strong> (ou <strong>CPK élevée</strong>) "
                "peuvent avoir des origines très diverses. Une CK élevée ne traduit pas toujours "
                "une maladie grave, mais dans certaines situations elle peut nécessiter une prise "
                "en charge urgente. Les principales causes sont :</p>"
                "<ul>"
                "<li><strong>Exercice intense :</strong> La musculation, le marathon ou toute "
                "activité physique inhabituelle peuvent élever temporairement la CK de façon "
                "significative.</li>"
                "<li><strong>Rhabdomyolyse :</strong> La destruction excessive de fibres "
                "musculaires libère de grandes quantités de myoglobine et de CK dans le sang ; "
                "sans traitement, elle peut entraîner une insuffisance rénale aiguë.</li>"
                "<li><strong>Infarctus du myocarde :</strong> L'atteinte du muscle cardiaque "
                "provoque une élévation marquée de la <strong>CK-MB</strong>, utilisée "
                "conjointement avec la troponine pour le diagnostic.</li>"
                "<li><strong>Effets secondaires des statines :</strong> Les statines "
                "hypolipémiantes peuvent provoquer des douleurs musculaires (myalgies) et une "
                "élévation de la CK chez certains patients ; dans de rares cas, une myopathie "
                "aux statines peut se développer.</li>"
                "<li><strong>Maladies musculaires :</strong> La dystrophie musculaire, la "
                "polymyosite et la dermatomyosite entraînent une CK chroniquement élevée.</li>"
                "<li><strong>Traumatismes et chirurgie :</strong> Les lésions physiques du tissu "
                "musculaire ou les interventions chirurgicales majeures élèvent la CK.</li>"
                "<li><strong>Hypothyroïdie :</strong> Un déficit en hormones thyroïdiennes peut "
                "perturber le métabolisme musculaire, provoquant une élévation de la CK.</li>"
                "</ul>"
                "<p>La CK seule n'est pas diagnostique. L'origine de l'élévation est déterminée "
                "par les données cliniques, les isoformes de CK (CK-MB, CK-MM), le dosage de "
                "la troponine, les tests de fonction rénale et le suivi sérié des enzymes "
                "musculaires.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si votre analyse de CK est élevée ou si vous présentez l'un des symptômes "
                "suivants, consultez rapidement un médecin :</p>"
                "<ul>"
                "<li>Douleurs musculaires sévères et diffuses, faiblesse ou gonflement</li>"
                "<li>Urines foncées (couleur thé) — signe possible de rhabdomyolyse</li>"
                "<li>Douleur thoracique, essoufflement ou douleur irradiant dans le bras "
                "gauche — appelez les urgences en cas de suspicion d'infarctus</li>"
                "<li>Douleurs musculaires inexpliquées sous traitement par statines</li>"
                "<li>Taux de CK qui ne diminuent pas ou continuent d'augmenter lors des "
                "contrôles successifs</li>"
                "</ul>"
                "<p>Une légère élévation de la CK après le sport n'est généralement pas "
                "préoccupante. Toutefois, si la valeur dépasse dix fois la limite supérieure "
                "de la normale ou si votre fonction rénale est altérée, une évaluation médicale "
                "urgente s'impose. Discutez toujours de vos résultats avec votre médecin plutôt "
                "que de les interpréter vous-même.</p>"
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
            heading="Esame CK (CPK): cosa significano i tuoi risultati",
            body_html=(
                "<p>L'<strong>esame CK</strong> (creatina chinasi, un tempo noto come "
                "<strong>test CPK</strong>) misura il livello di un enzima presente "
                "principalmente nel muscolo scheletrico, nel cuore e nel cervello. La creatina "
                "chinasi svolge un ruolo chiave nella produzione di energia cellulare; quando "
                "le fibre muscolari vengono danneggiate, l'enzima si riversa nel sangue causando "
                "<strong>livelli elevati di CK</strong>. Per questo motivo la CK è considerata "
                "un affidabile <strong>esame del sangue per danno muscolare</strong>.</p>"
                "<p>La CK esiste in tre isoformi principali: <em>CK-MM</em>, predominante nel "
                "muscolo scheletrico; <strong>CK-MB</strong>, concentrata nel muscolo cardiaco; "
                "e <em>CK-BB</em>, presente nel tessuto cerebrale. L'isoforma <strong>CK-MB</strong> "
                "è storicamente un biomarcatore importante per la diagnosi di infarto miocardico "
                "acuto. Un aumento della CK totale rappresenta un indicatore generale di danno "
                "muscolare.</p>"
                "<p>In questa guida scoprirai l'<strong>intervallo normale di CK</strong>, le "
                "cause possibili di una <strong>CPK elevata</strong> — dall'esercizio intenso "
                "alla rabdomiolisi, dagli effetti collaterali delle statine all'infarto — e "
                "quando consultare il medico.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di CK (intervalli di riferimento)",
            body_html=(
                "<p>L'<strong>intervallo normale di CK</strong> varia in base al sesso, alla "
                "massa muscolare e al metodo di laboratorio. Poiché gli uomini hanno in genere "
                "una massa muscolare maggiore, il limite superiore è più alto rispetto alle "
                "donne. La tabella seguente riporta gli intervalli di riferimento comunemente "
                "accettati per gli adulti:</p>"
                + _CK_TABLE_IT +
                "<p>Dopo un'attività fisica intensa, la CK può aumentare di diverse volte "
                "rispetto al normale anche in soggetti sani; i livelli si normalizzano "
                "tipicamente entro 3–5 giorni. Gli intervalli di riferimento possono differire "
                "nelle persone di origine africana, negli atleti di alto livello e nei bambini. "
                "Confronta sempre il tuo risultato con l'intervallo indicato nel tuo referto "
                "di laboratorio.</p>"
                "<p>Un livello di CK che supera cinque volte il limite superiore della norma è "
                "considerato clinicamente significativo e richiede approfondimenti. Valori "
                "superiori a dieci volte la norma destano seria preoccupazione per rabdomiolisi "
                "e necessitano di valutazione urgente.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di CK elevata",
            body_html=(
                "<p>I <strong>livelli elevati di CK</strong> (o <strong>CPK elevata</strong>) "
                "possono derivare da cause molto diverse. Una CK alta non indica sempre una "
                "malattia grave, ma in determinate situazioni può richiedere un intervento "
                "urgente. Le principali cause includono:</p>"
                "<ul>"
                "<li><strong>Esercizio intenso:</strong> L'allenamento con i pesi, la maratona "
                "o un'attività fisica inconsueta possono innalzare temporaneamente la CK in "
                "modo significativo.</li>"
                "<li><strong>Rabdomiolisi:</strong> La distruzione eccessiva di fibre muscolari "
                "libera grandi quantità di mioglobina e CK nel sangue; se non trattata, può "
                "portare a insufficienza renale acuta.</li>"
                "<li><strong>Infarto miocardico:</strong> Il danno al muscolo cardiaco provoca "
                "un aumento marcato della <strong>CK-MB</strong>, utilizzata insieme alla "
                "troponina per la diagnosi.</li>"
                "<li><strong>Effetti collaterali delle statine:</strong> Le statine ipocolesterolemizzanti "
                "possono causare dolore muscolare (mialgia) e aumento della CK in alcuni pazienti; "
                "in rari casi si sviluppa una miopatia da statine.</li>"
                "<li><strong>Malattie muscolari:</strong> Distrofia muscolare, polimiosite e "
                "dermatomiosite causano una CK cronicamente elevata.</li>"
                "<li><strong>Traumi e chirurgia:</strong> Le lesioni fisiche al tessuto muscolare "
                "o gli interventi chirurgici maggiori innalzano la CK.</li>"
                "<li><strong>Ipotiroidismo:</strong> La carenza di ormoni tiroidei può alterare "
                "il metabolismo muscolare, provocando un aumento della CK.</li>"
                "</ul>"
                "<p>La CK da sola non è diagnostica. La causa dell'elevazione viene determinata "
                "attraverso i reperti clinici, le isoformi di CK (CK-MB, CK-MM), i livelli di "
                "troponina, i test di funzionalità renale e il monitoraggio seriato degli enzimi "
                "muscolari.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Se il tuo esame CK è elevato o presenti uno dei seguenti sintomi, rivolgiti "
                "tempestivamente al medico:</p>"
                "<ul>"
                "<li>Dolore muscolare grave e diffuso, debolezza o gonfiore</li>"
                "<li>Urine scure (color tè) — possibile segno di rabdomiolisi</li>"
                "<li>Dolore al petto, difficoltà respiratorie o dolore irradiato al braccio "
                "sinistro — chiama il pronto soccorso in caso di sospetto infarto</li>"
                "<li>Dolori muscolari inspiegabili durante l'assunzione di statine</li>"
                "<li>Livelli di CK che non diminuiscono o continuano ad aumentare nei controlli "
                "successivi</li>"
                "</ul>"
                "<p>Un lieve aumento della CK dopo l'esercizio di solito non è motivo di "
                "preoccupazione. Tuttavia, se il valore supera dieci volte il limite superiore "
                "della norma o la funzionalità renale è compromessa, una valutazione medica "
                "urgente è indispensabile. Discuti sempre i tuoi risultati con il medico "
                "anziché interpretarli autonomamente.</p>"
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
            heading="בדיקת CK (קריאטין קינאז) בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת CK בדם</strong> (קריאטין קינאז, שנקראה בעבר <strong>בדיקת CPK</strong>) "
                "מודדת את רמת האנזים הנמצא בעיקר בשריר השלד, בלב ובמוח. קריאטין קינאז ממלא "
                "תפקיד מפתח בייצור אנרגיה תאית; כאשר סיבי שריר נפגעים, האנזים דולף לזרם הדם "
                "וגורם ל<strong>רמות CK גבוהות</strong>. לכן CK נחשבת ל<strong>בדיקת דם "
                "אמינה לנזק שרירי</strong> בפרקטיקה הקלינית.</p>"
                "<p>ל-CK שלוש איזופורמות עיקריות: <em>CK-MM</em>, הדומיננטית בשריר השלד; "
                "<strong>CK-MB</strong>, המרוכזת בשריר הלב; ו-<em>CK-BB</em>, הנמצאת ברקמת "
                "המוח. האיזופורמה <strong>CK-MB</strong> שימשה היסטורית כסמן ביולוגי חשוב "
                "לאבחון אוטם שריר הלב החריף (התקף לב). עלייה ב-CK הכוללת מהווה אינדיקטור כללי "
                "לפגיעה בשריר.</p>"
                "<p>במדריך זה תלמדו על <strong>טווח הנורמה של CK</strong>, הגורמים האפשריים "
                "ל<strong>CPK מוגבר</strong> — מפעילות גופנית אינטנסיבית דרך רבדומיוליזיס, "
                "תופעות לוואי של סטטינים ועד להתקף לב — ומתי יש לפנות לרופא.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של CK (טווחי ייחוס)",
            body_html=(
                "<p><strong>טווח הנורמה של CK</strong> משתנה בהתאם למין, למסת השריר ולשיטת "
                "המעבדה. מכיוון שלגברים יש בדרך כלל מסת שריר גדולה יותר, הגבול העליון גבוה "
                "יותר מאשר אצל נשים. הטבלה שלהלן מציגה את טווחי הייחוס המקובלים למבוגרים:</p>"
                + _CK_TABLE_HE +
                "<p>לאחר פעילות גופנית אינטנסיבית, CK עשויה לעלות פי כמה גם אצל אנשים בריאים; "
                "הרמות חוזרות בדרך כלל לנורמה תוך 3–5 ימים. טווחי הייחוס עשויים להיות שונים "
                "אצל אנשים ממוצא אפריקאי, ספורטאים מקצועיים וילדים. יש להשוות תמיד את התוצאה "
                "שלכם לטווח המופיע בדוח המעבדה שלכם.</p>"
                "<p>רמת CK העולה על פי חמישה מהגבול העליון של הנורמה נחשבת משמעותית מבחינה "
                "קלינית ומצריכה בירור. ערכים מעל פי עשרה מהנורמה מעלים חשש רציני לרבדומיוליזיס "
                "ודורשים הערכה דחופה.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות CK גבוהות",
            body_html=(
                "<p><strong>רמות CK גבוהות</strong> (או <strong>CPK מוגבר</strong>) יכולות "
                "לנבוע ממגוון רחב של גורמים. CK מוגברת לא תמיד מעידה על מחלה חמורה, אך "
                "במצבים מסוימים היא עשויה לדרוש התערבות דחופה. הגורמים העיקריים כוללים:</p>"
                "<ul>"
                "<li><strong>פעילות גופנית אינטנסיבית:</strong> אימוני כוח, ריצת מרתון או "
                "פעילות גופנית בלתי שגרתית עלולים להעלות את ה-CK באופן זמני ומשמעותי.</li>"
                "<li><strong>רבדומיוליזיס:</strong> פירוק מוגזם של סיבי שריר משחרר כמויות "
                "גדולות של מיוגלובין ו-CK לזרם הדם; ללא טיפול, הדבר עלול להוביל לאי-ספיקת "
                "כליות חריפה.</li>"
                "<li><strong>אוטם שריר הלב (התקף לב):</strong> נזק לשריר הלב גורם לעלייה "
                "ניכרת ב-<strong>CK-MB</strong>, המשמשת לצד טרופונין לאבחון.</li>"
                "<li><strong>תופעות לוואי של סטטינים:</strong> תרופות להורדת כולסטרול מקבוצת "
                "הסטטינים עלולות לגרום לכאבי שרירים (מיאלגיה) ולעליית CK; במקרים נדירים "
                "עלולה להתפתח מיופתיית סטטינים.</li>"
                "<li><strong>מחלות שריר:</strong> ניוון שרירים, פולימיוזיטיס ודרמטומיוזיטיס "
                "גורמים ל-CK מוגברת באופן כרוני.</li>"
                "<li><strong>טראומה וניתוחים:</strong> פגיעה פיזית ברקמת השריר או ניתוחים "
                "גדולים מעלים את ה-CK.</li>"
                "<li><strong>תת-פעילות בלוטת התריס:</strong> חוסר בהורמוני בלוטת התריס עלול "
                "לפגוע בחילוף החומרים של השריר ולגרום לעליית CK.</li>"
                "</ul>"
                "<p>CK לבדה אינה מאבחנת. הגורם לעלייה נקבע על סמך ממצאים קליניים, איזופורמות "
                "של CK (CK-MB, CK-MM), רמות טרופונין, בדיקות תפקודי כליות ומעקב סדרתי אחר "
                "אנזימי שריר.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם תוצאת <strong>בדיקת CK בדם</strong> שלכם גבוהה או שאתם חווים אחד "
                "מהתסמינים הבאים, פנו לרופא בהקדם:</p>"
                "<ul>"
                "<li>כאבי שרירים עזים ומפושטים, חולשה או נפיחות</li>"
                "<li>שתן כהה (בצבע תה) — סימן אפשרי לרבדומיוליזיס</li>"
                "<li>כאב בחזה, קוצר נשימה או כאב מקרין לזרוע שמאל — התקשרו למד\"א אם יש "
                "חשד להתקף לב</li>"
                "<li>כאבי שרירים בלתי מוסברים בזמן נטילת סטטינים</li>"
                "<li>רמות CK שאינן יורדות או ממשיכות לעלות בבדיקות חוזרות</li>"
                "</ul>"
                "<p>עלייה קלה ב-CK לאחר פעילות גופנית בדרך כלל אינה מדאיגה. עם זאת, אם "
                "הערך עולה על פי עשרה מהגבול העליון של הנורמה או שתפקוד הכליות שלכם לקוי, "
                "הערכה רפואית דחופה הכרחית. דונו תמיד בתוצאות שלכם עם הרופא במקום לפרש "
                "אותן בעצמכם.</p>"
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
            heading="CK (क्रिएटिन काइनेज) ब्लड टेस्ट: आपकी रिपोर्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>CK ब्लड टेस्ट</strong> (क्रिएटिन काइनेज, जिसे पहले <strong>CPK टेस्ट</strong> "
                "कहा जाता था) मुख्य रूप से कंकाल की मांसपेशियों, हृदय और मस्तिष्क में पाए जाने "
                "वाले एक एंज़ाइम के ब्लड लेवल को मापता है। क्रिएटिन काइनेज कोशिकाओं में ऊर्जा "
                "उत्पादन में अहम भूमिका निभाता है; जब मांसपेशी के तंतु क्षतिग्रस्त होते हैं तो "
                "एंज़ाइम रक्तप्रवाह में आ जाता है, जिससे <strong>CK लेवल बढ़ जाता है</strong>। "
                "इसीलिए CK को क्लिनिकल प्रैक्टिस में एक विश्वसनीय <strong>मांसपेशी क्षति "
                "ब्लड टेस्ट</strong> माना जाता है।</p>"
                "<p>CK की तीन प्रमुख आइसोफ़ॉर्म हैं: <em>CK-MM</em>, जो कंकाल की मांसपेशी में "
                "प्रमुख है; <strong>CK-MB</strong>, जो हृदय की मांसपेशी में केंद्रित है; और "
                "<em>CK-BB</em>, जो मस्तिष्क के ऊतक में पाई जाती है। <strong>CK-MB</strong> "
                "आइसोफ़ॉर्म ऐतिहासिक रूप से एक्यूट मायोकार्डियल इन्फ़ार्क्शन (हार्ट अटैक) के "
                "निदान में एक महत्वपूर्ण बायोमार्कर रही है। कुल CK में वृद्धि मांसपेशी चोट "
                "का सामान्य संकेतक है।</p>"
                "<p>इस गाइड में आप जानेंगे कि <strong>CK का नॉर्मल रेंज</strong> क्या है, "
                "<strong>CPK बढ़ने</strong> के संभावित कारण — तीव्र व्यायाम से रैबडोमायोलिसिस, "
                "स्टैटिन के साइड इफ़ेक्ट से हार्ट अटैक तक — और डॉक्टर से कब मिलना चाहिए।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="CK के नॉर्मल वैल्यू (रेफ़रेंस रेंज)",
            body_html=(
                "<p><strong>CK का नॉर्मल रेंज</strong> लिंग, मांसपेशी द्रव्यमान और लैब विधि "
                "के अनुसार भिन्न होता है। पुरुषों में मांसपेशी द्रव्यमान अधिक होने के कारण "
                "ऊपरी सीमा महिलाओं की तुलना में अधिक होती है। नीचे दी गई तालिका में वयस्कों "
                "के लिए सामान्य रूप से स्वीकृत रेफ़रेंस रेंज दी गई है:</p>"
                + _CK_TABLE_HI +
                "<p>तीव्र शारीरिक गतिविधि के बाद CK स्वस्थ व्यक्तियों में भी सामान्य से कई "
                "गुना बढ़ सकता है; लेवल आमतौर पर 3–5 दिनों में सामान्य हो जाता है। अफ़्रीकी "
                "मूल के लोगों, उच्च-स्तरीय एथलीटों और बच्चों में रेफ़रेंस रेंज भिन्न हो "
                "सकती है। अपनी रिपोर्ट पर छपी रेफ़रेंस रेंज से हमेशा तुलना करें।</p>"
                "<p>CK लेवल यदि ऊपरी सामान्य सीमा से पाँच गुना अधिक है तो इसे क्लिनिकली "
                "महत्वपूर्ण माना जाता है और जाँच ज़रूरी है। दस गुना से अधिक वैल्यू "
                "रैबडोमायोलिसिस की गंभीर चिंता उत्पन्न करती है और तत्काल मूल्यांकन "
                "आवश्यक है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="CK बढ़ने के कारण",
            body_html=(
                "<p><strong>CK लेवल बढ़ना</strong> (या <strong>CPK बढ़ना</strong>) कई अलग-अलग "
                "कारणों से हो सकता है। बढ़ी हुई CK हमेशा गंभीर बीमारी का संकेत नहीं होती, "
                "लेकिन कुछ स्थितियों में तत्काल हस्तक्षेप ज़रूरी हो सकता है। प्रमुख कारण "
                "हैं:</p>"
                "<ul>"
                "<li><strong>तीव्र व्यायाम:</strong> वेट ट्रेनिंग, मैराथन दौड़ या असामान्य "
                "शारीरिक गतिविधि CK को अस्थायी रूप से काफ़ी बढ़ा सकती है।</li>"
                "<li><strong>रैबडोमायोलिसिस:</strong> मांसपेशी तंतुओं के अत्यधिक टूटने से "
                "बड़ी मात्रा में मायोग्लोबिन और CK रक्तप्रवाह में आ जाते हैं; इलाज न होने पर "
                "एक्यूट किडनी फ़ेल्योर हो सकता है।</li>"
                "<li><strong>मायोकार्डियल इन्फ़ार्क्शन (हार्ट अटैक):</strong> हृदय की "
                "मांसपेशी को नुकसान से <strong>CK-MB</strong> स्पष्ट रूप से बढ़ जाता है, "
                "जिसे ट्रोपोनिन के साथ निदान में इस्तेमाल किया जाता है।</li>"
                "<li><strong>स्टैटिन के साइड इफ़ेक्ट:</strong> कोलेस्ट्रॉल कम करने वाली "
                "स्टैटिन दवाएँ कुछ रोगियों में मांसपेशी दर्द (मायलजिया) और CK वृद्धि कर "
                "सकती हैं; दुर्लभ मामलों में स्टैटिन मायोपैथी विकसित हो सकती है।</li>"
                "<li><strong>मांसपेशी रोग:</strong> मस्कुलर डिस्ट्रॉफ़ी, पॉलीमायोसाइटिस "
                "और डर्मेटोमायोसाइटिस क्रॉनिकली बढ़ी हुई CK का कारण बनते हैं।</li>"
                "<li><strong>ट्रॉमा और सर्जरी:</strong> मांसपेशी ऊतक को शारीरिक चोट या "
                "बड़ी सर्जिकल प्रक्रियाएँ CK बढ़ाती हैं।</li>"
                "<li><strong>हाइपोथायरॉइडिज़्म:</strong> थायरॉइड हार्मोन की कमी मांसपेशी "
                "मेटाबॉलिज़्म को प्रभावित कर CK वृद्धि कर सकती है।</li>"
                "</ul>"
                "<p>CK अकेली डायग्नोस्टिक नहीं है। बढ़ोतरी का कारण क्लिनिकल निष्कर्षों, "
                "CK आइसोफ़ॉर्म (CK-MB, CK-MM), ट्रोपोनिन लेवल, किडनी फ़ंक्शन टेस्ट और "
                "मांसपेशी एंज़ाइम की सीरियल मॉनिटरिंग से तय किया जाता है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपकी <strong>CK ब्लड टेस्ट</strong> रिपोर्ट बढ़ी हुई आई है या "
                "नीचे दिए गए किसी भी लक्षण का अनुभव हो रहा है, तो बिना देर किए डॉक्टर "
                "से मिलें:</p>"
                "<ul>"
                "<li>गंभीर और व्यापक मांसपेशी दर्द, कमज़ोरी या सूजन</li>"
                "<li>गहरे रंग का (चाय जैसा) पेशाब — रैबडोमायोलिसिस का संभावित संकेत</li>"
                "<li>छाती में दर्द, साँस फूलना या बाईं बाँह में दर्द — हार्ट अटैक की "
                "आशंका हो तो तुरंत इमरजेंसी सेवाओं को कॉल करें</li>"
                "<li>स्टैटिन लेते समय अस्पष्ट मांसपेशी दर्द</li>"
                "<li>बार-बार टेस्ट में CK लेवल का कम न होना या बढ़ते रहना</li>"
                "</ul>"
                "<p>व्यायाम के बाद CK में हल्की वृद्धि आमतौर पर चिंता की बात नहीं है। "
                "हालाँकि, अगर वैल्यू ऊपरी सामान्य सीमा से दस गुना अधिक है या किडनी "
                "फ़ंक्शन प्रभावित है, तो तत्काल चिकित्सा मूल्यांकन अनिवार्य है। रिज़ल्ट "
                "ख़ुद से व्याख्या करने के बजाय हमेशा अपने डॉक्टर से चर्चा करें।</p>"
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
            heading="تحليل CK (كرياتين كيناز) في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p><strong>تحليل CK في الدم</strong> (كرياتين كيناز، المعروف سابقاً باسم "
                "<strong>تحليل CPK</strong>) يقيس مستوى إنزيم يوجد بشكل رئيسي في العضلات "
                "الهيكلية والقلب والدماغ. يلعب الكرياتين كيناز دوراً محورياً في إنتاج الطاقة "
                "الخلوية؛ وعند تلف ألياف العضلات يتسرب الإنزيم إلى مجرى الدم مسبباً "
                "<strong>ارتفاع مستوى CK</strong>. لذلك يُعدّ CK <strong>اختبار دم موثوقاً "
                "لتلف العضلات</strong> في الممارسة السريرية.</p>"
                "<p>يوجد CK في ثلاثة أشكال إنزيمية رئيسية: <em>CK-MM</em> السائد في العضلات "
                "الهيكلية، و<strong>CK-MB</strong> المتركز في عضلة القلب، و<em>CK-BB</em> "
                "الموجود في أنسجة الدماغ. يُعدّ الشكل الإنزيمي <strong>CK-MB</strong> تاريخياً "
                "واسماً حيوياً مهماً لتشخيص احتشاء عضلة القلب الحاد (النوبة القلبية). "
                "ويُشكّل ارتفاع CK الكلي مؤشراً عاماً على إصابة العضلات.</p>"
                "<p>في هذا الدليل ستتعرفون على <strong>النطاق الطبيعي لـ CK</strong>، "
                "والأسباب المحتملة <strong>لارتفاع CPK</strong> — من التمارين المكثفة إلى "
                "انحلال الربيدات، ومن الآثار الجانبية للستاتين إلى النوبة القلبية — ومتى "
                "يجب مراجعة الطبيب.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية لـ CK (النطاقات المرجعية)",
            body_html=(
                "<p>يختلف <strong>النطاق الطبيعي لـ CK</strong> بحسب الجنس والكتلة العضلية "
                "وطريقة المختبر. وبما أن الرجال يمتلكون عادةً كتلة عضلية أكبر، فإن الحد "
                "الأعلى يكون أعلى مما هو عليه لدى النساء. يعرض الجدول أدناه النطاقات المرجعية "
                "المقبولة عموماً للبالغين:</p>"
                + _CK_TABLE_AR +
                "<p>بعد النشاط البدني المكثف، قد يرتفع CK عدة أضعاف حتى لدى الأشخاص "
                "الأصحاء؛ وتعود المستويات عادةً إلى طبيعتها خلال 3–5 أيام. قد تختلف "
                "النطاقات المرجعية لدى الأشخاص من أصول أفريقية والرياضيين المحترفين "
                "والأطفال. قارن دائماً نتيجتك بالنطاق المرجعي المطبوع في تقرير مختبرك.</p>"
                "<p>يُعدّ مستوى CK الذي يتجاوز خمسة أضعاف الحد الأعلى للطبيعي ذا أهمية "
                "سريرية ويستدعي التقصي. القيم التي تتجاوز عشرة أضعاف الطبيعي تثير قلقاً "
                "جدياً بشأن انحلال الربيدات وتتطلب تقييماً عاجلاً.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع مستوى CK",
            body_html=(
                "<p>يمكن أن ينتج <strong>ارتفاع CK</strong> (أو <strong>ارتفاع CPK</strong>) "
                "عن أسباب متنوعة. لا يشير ارتفاع CK دائماً إلى مرض خطير، لكن في بعض "
                "الحالات قد يتطلب تدخلاً عاجلاً. تشمل الأسباب الرئيسية:</p>"
                "<ul>"
                "<li><strong>التمارين المكثفة:</strong> تدريبات الأثقال أو سباقات الماراثون "
                "أو النشاط البدني غير المعتاد يمكن أن ترفع CK مؤقتاً بشكل ملحوظ.</li>"
                "<li><strong>انحلال الربيدات (رابدوميوليسيس):</strong> يؤدي التحلل المفرط "
                "لألياف العضلات إلى إطلاق كميات كبيرة من الميوغلوبين وCK في الدم؛ وبدون "
                "علاج قد يسبب فشلاً كلوياً حاداً.</li>"
                "<li><strong>احتشاء عضلة القلب (النوبة القلبية):</strong> يسبب تلف عضلة القلب "
                "ارتفاعاً ملحوظاً في <strong>CK-MB</strong>، يُستخدم مع التروبونين في "
                "التشخيص.</li>"
                "<li><strong>الآثار الجانبية للستاتين:</strong> قد تسبب أدوية الستاتين الخافضة "
                "للكوليسترول آلاماً عضلية (ألم عضلي) وارتفاعاً في CK لدى بعض المرضى؛ "
                "وفي حالات نادرة قد يتطور اعتلال عضلي بالستاتين.</li>"
                "<li><strong>أمراض العضلات:</strong> الحثل العضلي والتهاب العضلات المتعدد "
                "والتهاب الجلد والعضلات تسبب ارتفاعاً مزمناً في CK.</li>"
                "<li><strong>الإصابات والعمليات الجراحية:</strong> الإصابة الجسدية لأنسجة "
                "العضلات أو العمليات الجراحية الكبرى ترفع مستوى CK.</li>"
                "<li><strong>قصور الغدة الدرقية:</strong> قد يؤدي نقص هرمونات الغدة الدرقية "
                "إلى اضطراب أيض العضلات وبالتالي ارتفاع CK.</li>"
                "</ul>"
                "<p>CK وحده ليس تشخيصياً. يُحدَّد سبب الارتفاع من خلال النتائج السريرية "
                "وأشكال CK الإنزيمية (CK-MB، CK-MM) ومستويات التروبونين واختبارات وظائف "
                "الكلى والمتابعة المتسلسلة لإنزيمات العضلات.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كانت نتيجة <strong>تحليل CK في الدم</strong> مرتفعة أو كنتم تعانون "
                "من أي من الأعراض التالية، فاطلبوا الاستشارة الطبية فوراً:</p>"
                "<ul>"
                "<li>ألم عضلي شديد ومنتشر أو ضعف أو تورم</li>"
                "<li>بول داكن (بلون الشاي) — علامة محتملة على انحلال الربيدات</li>"
                "<li>ألم في الصدر أو ضيق تنفس أو ألم يمتد إلى الذراع اليسرى — اتصلوا "
                "بالطوارئ إذا اشتُبه في نوبة قلبية</li>"
                "<li>آلام عضلية غير مبررة أثناء تناول الستاتين</li>"
                "<li>مستويات CK لا تنخفض أو تستمر في الارتفاع عند تكرار الفحص</li>"
                "</ul>"
                "<p>الارتفاع الطفيف في CK بعد التمارين عادةً لا يدعو للقلق. ومع ذلك، إذا "
                "تجاوزت القيمة عشرة أضعاف الحد الأعلى للطبيعي أو كانت وظائف الكلى لديكم "
                "متأثرة، فإن التقييم الطبي العاجل ضروري. ناقشوا دائماً نتائجكم مع طبيبكم "
                "بدلاً من تفسيرها بأنفسكم.</p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC ACCESSORS
# ─────────────────────────────────────────────────────────────────────

def get_ck_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for CK/CPK article (all 9 languages)."""
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


def get_ck_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for CK/CPK article (all 9 languages, 3 Q&A each)."""
    return {
        "tr": [
            {"question": "CK (kreatin kinaz) kan testi nedir?",
             "answer": "CK kan testi, kas ve kalp dokusunda yoğun olarak bulunan kreatin kinaz enziminin kandaki düzeyini ölçer. Kas hasarı, kalp krizi veya rabdomiyoliz gibi durumları değerlendirmek için kullanılır. CK-MB izoformu özellikle kalp kası hasarını saptamada önemlidir."},
            {"question": "CK yüksekliğine ne sebep olur?",
             "answer": "CK yüksekliğinin en sık nedenleri yoğun egzersiz, kas travması, rabdomiyoliz, kalp krizi (miyokard enfarktüsü), statin grubu ilaçlar ve kas hastalıklarıdır. Hipotiroidizm ve büyük cerrahi işlemler de CK düzeyini artırabilir."},
            {"question": "CK normal değeri kaç olmalıdır?",
             "answer": "Yetişkin erkeklerde CK normal aralığı genellikle 39–308 U/L, kadınlarda ise 26–192 U/L olarak kabul edilir. Egzersiz sonrası geçici yükselmeler normaldir; ancak normalin beş katını aşan değerler klinik olarak anlamlıdır ve araştırılmalıdır."},
        ],
        "en": [
            {"question": "What is a CK (creatine kinase) blood test?",
             "answer": "A CK blood test measures the level of creatine kinase, an enzyme found mainly in skeletal muscle, the heart, and the brain. It is used to evaluate conditions such as muscle damage, heart attack, and rhabdomyolysis. The CK-MB isoform is particularly important for detecting heart muscle injury."},
            {"question": "What causes high CK levels?",
             "answer": "The most common causes of high CK levels include intense exercise, muscle trauma, rhabdomyolysis, myocardial infarction (heart attack), statin medications, and muscle diseases. Hypothyroidism and major surgery can also raise CK."},
            {"question": "What is the normal range for CK?",
             "answer": "The normal CK range is typically 39–308 U/L for adult males and 26–192 U/L for adult females. Temporary elevations after exercise are normal, but values exceeding five times the upper limit are clinically significant and should be investigated."},
        ],
        "es": [
            {"question": "¿Qué es el análisis de CK (creatina quinasa)?",
             "answer": "El análisis de CK mide el nivel de creatina quinasa, una enzima presente principalmente en el músculo esquelético, el corazón y el cerebro. Se utiliza para evaluar daño muscular, infarto de miocardio y rabdomiólisis. La isoforma CK-MB es especialmente relevante para detectar lesión del músculo cardíaco."},
            {"question": "¿Qué causa niveles elevados de CK?",
             "answer": "Las causas más frecuentes de CK elevada incluyen ejercicio intenso, traumatismo muscular, rabdomiólisis, infarto de miocardio, estatinas y enfermedades musculares. El hipotiroidismo y las cirugías mayores también pueden elevar la CK."},
            {"question": "¿Cuál es el rango normal de CK?",
             "answer": "El rango normal de CK es generalmente de 39–308 U/L en hombres adultos y de 26–192 U/L en mujeres adultas. Las elevaciones temporales tras el ejercicio son normales, pero valores que superen cinco veces el límite superior son clínicamente significativos y deben investigarse."},
        ],
        "de": [
            {"question": "Was ist ein CK-Bluttest (Kreatinkinase)?",
             "answer": "Ein CK-Bluttest misst den Spiegel der Kreatinkinase, eines Enzyms, das hauptsächlich in der Skelettmuskulatur, im Herzen und im Gehirn vorkommt. Er wird zur Beurteilung von Muskelschäden, Herzinfarkt und Rhabdomyolyse eingesetzt. Die Isoform CK-MB ist besonders wichtig für den Nachweis einer Herzmuskelschädigung."},
            {"question": "Was verursacht hohe CK-Werte?",
             "answer": "Die häufigsten Ursachen erhöhter CK-Werte sind intensiver Sport, Muskeltrauma, Rhabdomyolyse, Myokardinfarkt (Herzinfarkt), Statine und Muskelerkrankungen. Auch Hypothyreose und größere Operationen können die CK erhöhen."},
            {"question": "Wie hoch ist der Normalwert für CK?",
             "answer": "Der CK-Normbereich liegt bei erwachsenen Männern in der Regel bei 39–308 U/L und bei Frauen bei 26–192 U/L. Vorübergehende Erhöhungen nach dem Sport sind normal; Werte über dem Fünffachen der oberen Normgrenze gelten jedoch als klinisch relevant und sollten abgeklärt werden."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'une analyse de CK (créatine kinase) ?",
             "answer": "L'analyse de CK mesure le taux de créatine kinase, une enzyme présente principalement dans le muscle squelettique, le cœur et le cerveau. Elle sert à évaluer les lésions musculaires, l'infarctus du myocarde et la rhabdomyolyse. L'isoforme CK-MB est particulièrement importante pour détecter une atteinte du muscle cardiaque."},
            {"question": "Quelles sont les causes d'une CK élevée ?",
             "answer": "Les causes les plus fréquentes d'une CK élevée comprennent l'exercice intense, les traumatismes musculaires, la rhabdomyolyse, l'infarctus du myocarde, les statines et les maladies musculaires. L'hypothyroïdie et les chirurgies majeures peuvent également augmenter la CK."},
            {"question": "Quelle est la valeur normale de la CK ?",
             "answer": "Les valeurs normales de CK sont généralement de 39–308 U/L chez les hommes adultes et de 26–192 U/L chez les femmes adultes. Les élévations temporaires après le sport sont normales, mais des valeurs dépassant cinq fois la limite supérieure sont cliniquement significatives et doivent être investiguées."},
        ],
        "it": [
            {"question": "Cos'è l'esame CK (creatina chinasi)?",
             "answer": "L'esame CK misura il livello di creatina chinasi, un enzima presente soprattutto nel muscolo scheletrico, nel cuore e nel cervello. Viene utilizzato per valutare il danno muscolare, l'infarto miocardico e la rabdomiolisi. L'isoforma CK-MB è particolarmente importante per rilevare lesioni al muscolo cardiaco."},
            {"question": "Quali sono le cause di CK elevata?",
             "answer": "Le cause più comuni di CK elevata includono esercizio intenso, trauma muscolare, rabdomiolisi, infarto miocardico, statine e malattie muscolari. Anche l'ipotiroidismo e gli interventi chirurgici maggiori possono aumentare la CK."},
            {"question": "Qual è il range normale della CK?",
             "answer": "Il range normale di CK è generalmente 39–308 U/L per gli uomini adulti e 26–192 U/L per le donne adulte. Le elevazioni temporanee dopo l'esercizio sono normali, ma valori superiori a cinque volte il limite superiore sono clinicamente significativi e vanno indagati."},
        ],
        "he": [
            {"question": "מהי בדיקת CK (קריאטין קינאז) בדם?",
             "answer": "בדיקת CK בדם מודדת את רמת הקריאטין קינאז, אנזים הנמצא בעיקר בשריר השלד, בלב ובמוח. היא משמשת להערכת נזק שרירי, התקף לב ורבדומיוליזיס. האיזופורמה CK-MB חשובה במיוחד לזיהוי פגיעה בשריר הלב."},
            {"question": "מה גורם לרמות CK גבוהות?",
             "answer": "הגורמים השכיחים ביותר לרמות CK גבוהות כוללים פעילות גופנית אינטנסיבית, טראומה לשרירים, רבדומיוליזיס, אוטם שריר הלב (התקף לב), סטטינים ומחלות שריר. גם תת-פעילות בלוטת התריס וניתוחים גדולים עלולים להעלות את ה-CK."},
            {"question": "מהו הטווח הנורמלי של CK?",
             "answer": "טווח הנורמה של CK הוא בדרך כלל 39–308 U/L לגברים בוגרים ו-26–192 U/L לנשים בוגרות. עליות זמניות לאחר פעילות גופנית הן תקינות, אך ערכים העולים על פי חמישה מהגבול העליון נחשבים משמעותיים קלינית ויש לברר אותם."},
        ],
        "hi": [
            {"question": "CK (क्रिएटिन काइनेज) ब्लड टेस्ट क्या है?",
             "answer": "CK ब्लड टेस्ट क्रिएटिन काइनेज के लेवल को मापता है, जो मुख्य रूप से कंकाल की मांसपेशियों, हृदय और मस्तिष्क में पाया जाने वाला एंज़ाइम है। इसका उपयोग मांसपेशी क्षति, हार्ट अटैक और रैबडोमायोलिसिस जैसी स्थितियों के मूल्यांकन के लिए किया जाता है। CK-MB आइसोफ़ॉर्म विशेष रूप से हृदय की मांसपेशी की चोट का पता लगाने में महत्वपूर्ण है।"},
            {"question": "CK लेवल बढ़ने का क्या कारण है?",
             "answer": "CK बढ़ने के सबसे आम कारणों में तीव्र व्यायाम, मांसपेशी ट्रॉमा, रैबडोमायोलिसिस, मायोकार्डियल इन्फ़ार्क्शन (हार्ट अटैक), स्टैटिन दवाएँ और मांसपेशी रोग शामिल हैं। हाइपोथायरॉइडिज़्म और बड़ी सर्जरी भी CK बढ़ा सकते हैं।"},
            {"question": "CK का नॉर्मल रेंज कितना होता है?",
             "answer": "वयस्क पुरुषों में CK का सामान्य रेंज आमतौर पर 39–308 U/L और वयस्क महिलाओं में 26–192 U/L होता है। व्यायाम के बाद अस्थायी वृद्धि सामान्य है, लेकिन ऊपरी सीमा से पाँच गुना अधिक वैल्यू क्लिनिकली महत्वपूर्ण है और जाँच की जानी चाहिए।"},
        ],
        "ar": [
            {"question": "ما هو تحليل CK (كرياتين كيناز) في الدم؟",
             "answer": "تحليل CK في الدم يقيس مستوى الكرياتين كيناز، وهو إنزيم يوجد بشكل رئيسي في العضلات الهيكلية والقلب والدماغ. يُستخدم لتقييم حالات مثل تلف العضلات والنوبة القلبية وانحلال الربيدات. الشكل الإنزيمي CK-MB مهم بشكل خاص للكشف عن إصابة عضلة القلب."},
            {"question": "ما أسباب ارتفاع مستوى CK؟",
             "answer": "تشمل الأسباب الأكثر شيوعاً لارتفاع CK التمارين المكثفة وإصابات العضلات وانحلال الربيدات واحتشاء عضلة القلب (النوبة القلبية) وأدوية الستاتين وأمراض العضلات. كما أن قصور الغدة الدرقية والعمليات الجراحية الكبرى قد ترفع مستوى CK."},
            {"question": "ما هو النطاق الطبيعي لـ CK؟",
             "answer": "النطاق الطبيعي لـ CK عادةً 39–308 وحدة/لتر للرجال البالغين و26–192 وحدة/لتر للنساء البالغات. الارتفاعات المؤقتة بعد التمارين طبيعية، لكن القيم التي تتجاوز خمسة أضعاف الحد الأعلى ذات أهمية سريرية ويجب التقصي عنها."},
        ],
    }
