# -*- coding: utf-8 -*-
"""
Fibrinogen blog article — full body content for all 9 languages.
Used by blog_i18n._article_fibrinogen().
Sections: intro, normal-ranges, causes, when-to-see-doctor.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# Turkish
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Fibrinojen kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>Fibrinojen testi</strong>, karaciğerde üretilen ve kan pıhtılaşma sürecinde kritik "
                "rol oynayan bir glikoprotein olan <strong>fibrinojen</strong> düzeyini ölçer. Fibrinojen, "
                "pıhtılaşma kaskadının son basamağında trombin tarafından fibrine dönüştürülerek pıhtının "
                "yapısal iskeletini oluşturur. Aynı zamanda bir <strong>akut faz reaktanı</strong> olarak "
                "enfeksiyon, inflamasyon ve doku hasarı durumlarında kan düzeyleri belirgin şekilde artar.</p>"
                "<p><strong>Fibrinojen kan testi</strong>, hem pıhtılaşma bozukluklarının tanısında hem de "
                "kronik inflamasyon ve kardiyovasküler risk değerlendirmesinde kullanılır. <strong>Yüksek "
                "fibrinojen</strong> düzeyleri kronik inflamasyon, enfeksiyon, kanser veya gebelik gibi "
                "durumlara işaret edebilirken, <strong>düşük fibrinojen</strong> düzeyleri yaygın damar "
                "içi pıhtılaşma (DIC), karaciğer hastalığı veya malnütrisyonla ilişkilendirilebilir.</p>"
                "<p>Bu rehberde <strong>fibrinojen normal değerleri</strong>, yükseklik ve düşüklük "
                "nedenlerini ve ne zaman bir sağlık uzmanına başvurmanız gerektiğini bulacaksınız. "
                "Buradaki bilgiler eğitim amaçlıdır — tanı ve tedavi için mutlaka bir doktora danışın.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Fibrinojen normal değerleri (referans aralıkları)",
            body_html=(
                "<p><strong>Fibrinojen normal aralığı</strong> laboratuvarlar arasında küçük farklılıklar "
                "gösterebilir; ancak genel olarak kabul edilen referans değerleri aşağıdaki tabloda "
                "özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fibrinojen normal aralığı</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yetişkinler</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yenidoğanlar</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Gebelik (3. trimester)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kritik düşük eşik</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Referans aralığı test yöntemine (Clauss yöntemi en yaygınıdır) ve laboratuvar cihazına "
                "göre değişebilir; bu nedenle kendi raporunuzdaki değerleri esas almalısınız. "
                "<strong>Fibrinojen düzeyleri</strong> normalin dışındaysa hekiminiz pıhtılaşma paneli, "
                "karaciğer fonksiyon testleri ve inflamasyon belirteçleri (CRP, sedimantasyon) gibi ek "
                "testler isteyecektir.</p>"
                "<p>Fibrinojen bir akut faz proteini olduğundan, geçici enfeksiyonlar ve cerrahi "
                "sonrasında da yükselebilir. Tek bir ölçüm her zaman kronik bir durumu yansıtmaz; "
                "klinik bağlamda değerlendirilmesi önemlidir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Fibrinojen yüksekliği veya düşüklüğünün nedenleri",
            body_html=(
                "<p><strong>Yüksek fibrinojen</strong> ve <strong>düşük fibrinojen</strong> düzeylerinin "
                "farklı klinik anlamları vardır. Her iki durumun da altta yatan nedeninin araştırılması "
                "gerekir.</p>"
                "<p><strong>Fibrinojen yüksekliği (hiperfibrinojenemi) nedenleri:</strong></p>"
                "<ul>"
                "<li><strong>Enfeksiyon:</strong> Bakteriyel ve viral enfeksiyonlar akut faz yanıtını "
                "tetikleyerek fibrinojen düzeylerini artırır.</li>"
                "<li><strong>Kronik inflamasyon:</strong> Romatoid artrit, inflamatuar bağırsak hastalığı "
                "ve vaskülitler gibi kronik inflamatuar durumlar fibrinojen yüksekliğine neden olur.</li>"
                "<li><strong>Kanser:</strong> Bazı solid tümörler ve hematolojik maligniteler fibrinojen "
                "düzeylerini artırabilir.</li>"
                "<li><strong>Gebelik:</strong> Fizyolojik bir yanıt olarak, özellikle üçüncü trimesterde "
                "fibrinojen belirgin şekilde yükselir.</li>"
                "<li><strong>Sigara kullanımı:</strong> Kronik sigara içiciliği fibrinojen düzeylerini "
                "kalıcı olarak yükseltebilir ve kardiyovasküler riski artırır.</li>"
                "</ul>"
                "<p><strong>Fibrinojen düşüklüğü (hipofibrinojenemi) nedenleri:</strong></p>"
                "<ul>"
                "<li><strong>Yaygın damar içi pıhtılaşma (DIC):</strong> Fibrinojenin aşırı tüketilmesi "
                "sonucu düzeyleri hızla düşer; bu, acil müdahale gerektiren bir durumdur.</li>"
                "<li><strong>Karaciğer hastalığı:</strong> Siroz ve ileri evre karaciğer yetmezliğinde "
                "fibrinojen sentezi azalır.</li>"
                "<li><strong>Malnütrisyon:</strong> Ciddi protein eksikliği veya yetersiz beslenme, "
                "fibrinojen üretimini olumsuz etkileyebilir.</li>"
                "<li><strong>Konjenital fibrinojen eksikliği:</strong> Nadir kalıtsal bozukluklar "
                "(afibrinojenemi, hipofibrinojenemi) fibrinojen düzeylerinin düşük veya saptanamaz "
                "olmasına neden olur.</li>"
                "</ul>"
                "<p>Doktorunuz klinik tabloya göre ek pıhtılaşma testleri (PT, aPTT, D-dimer), "
                "karaciğer fonksiyon testleri ve görüntüleme yöntemleri isteyebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p><strong>Fibrinojen kan testi</strong> sonucunuz referans aralığının dışındaysa "
                "panik yapmayın; ancak mutlaka bir hekime danışın. Özellikle açıklanamayan kanama "
                "eğilimi, ciltte morluklar, uzun süreli yara iyileşmesi veya tekrarlayan tromboz "
                "öyküsü varsa değerlendirme geciktirilmemelidir.</p>"
                "<p><strong>Yüksek fibrinojen</strong> düzeyleri, kardiyovasküler hastalık riskinin "
                "değerlendirilmesinde de önem taşır. Kronik olarak yüksek fibrinojen, ateroskleroz "
                "ve trombotik olaylar için bağımsız bir risk faktörü olarak kabul edilmektedir. "
                "Hekiminiz düzenli aralıklarla fibrinojen takibi isteyebilir.</p>"
                "<p>Unutmayın: anormal <strong>fibrinojen düzeyleri</strong> tek başına bir tanı "
                "değildir. Doktorunuz ek tetkiklerle altta yatan nedeni belirleyecek ve uygun "
                "tedavi planını oluşturacaktır. Erken teşhis ve düzenli takip, hem kanama hem "
                "de pıhtılaşma bozukluklarında tedavi başarısını artırır.</p>"
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
            heading="Fibrinogen blood test: what your results mean",
            body_html=(
                "<p>The <strong>fibrinogen blood test</strong> measures the level of "
                "<strong>fibrinogen</strong>, a glycoprotein produced by the liver that plays a "
                "critical role in blood clotting. During the final step of the coagulation cascade, "
                "thrombin converts fibrinogen into fibrin strands that form the structural scaffold "
                "of a blood clot. Fibrinogen is also an <strong>acute-phase reactant</strong>, meaning "
                "its <strong>fibrinogen levels</strong> rise significantly during infection, "
                "inflammation and tissue injury.</p>"
                "<p>A <strong>fibrinogen test</strong> is used both to diagnose clotting disorders and "
                "to assess chronic inflammation and cardiovascular risk. <strong>High fibrinogen</strong> "
                "may point to chronic inflammation, infection, cancer or pregnancy, while "
                "<strong>low fibrinogen</strong> can be associated with disseminated intravascular "
                "coagulation (DIC), liver disease or malnutrition.</p>"
                "<p>In this guide you will find the <strong>fibrinogen normal range</strong>, "
                "causes of <strong>elevated fibrinogen</strong> and low fibrinogen, and when "
                "to see a doctor. The information here is educational — always consult a "
                "healthcare professional for diagnosis and treatment.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Fibrinogen normal range (reference intervals)",
            body_html=(
                "<p>The <strong>fibrinogen normal range</strong> can vary slightly between "
                "laboratories, but generally accepted reference values are summarised in the "
                "table below:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fibrinogen normal range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adults</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Newborns</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Pregnancy (3rd trimester)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Critical low threshold</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Reference intervals depend on the assay method (the Clauss method is most common) "
                "and analyser used, so always compare your result with the range printed on your own "
                "report. If your <strong>fibrinogen levels</strong> are outside the normal range, your "
                "doctor may order additional tests such as a coagulation panel, liver function tests "
                "and inflammatory markers (CRP, ESR).</p>"
                "<p>Because fibrinogen is an acute-phase protein, it can rise temporarily after "
                "infections and surgery. A single measurement does not always reflect a chronic "
                "condition; clinical context is essential for interpretation.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high and low fibrinogen",
            body_html=(
                "<p><strong>High fibrinogen</strong> and <strong>low fibrinogen</strong> have "
                "different clinical implications. Both require investigation to identify the "
                "underlying cause.</p>"
                "<p><strong>Causes of elevated fibrinogen (hyperfibrinogenaemia):</strong></p>"
                "<ul>"
                "<li><strong>Infection:</strong> Bacterial and viral infections trigger the "
                "acute-phase response, raising <strong>fibrinogen levels</strong>.</li>"
                "<li><strong>Chronic inflammation:</strong> Conditions such as rheumatoid arthritis, "
                "inflammatory bowel disease and vasculitis cause persistently "
                "<strong>elevated fibrinogen</strong>.</li>"
                "<li><strong>Cancer:</strong> Certain solid tumours and haematological malignancies "
                "can increase fibrinogen production.</li>"
                "<li><strong>Pregnancy:</strong> Fibrinogen rises physiologically, especially in "
                "the third trimester, as part of normal haemostatic adaptation.</li>"
                "<li><strong>Smoking:</strong> Chronic tobacco use can permanently elevate "
                "<strong>fibrinogen levels</strong> and increase cardiovascular risk.</li>"
                "</ul>"
                "<p><strong>Causes of low fibrinogen (hypofibrinogenaemia):</strong></p>"
                "<ul>"
                "<li><strong>Disseminated intravascular coagulation (DIC):</strong> Excessive "
                "consumption of fibrinogen causes levels to drop rapidly; this is a medical "
                "emergency.</li>"
                "<li><strong>Liver disease:</strong> Cirrhosis and advanced liver failure reduce "
                "fibrinogen synthesis.</li>"
                "<li><strong>Malnutrition:</strong> Severe protein deficiency or inadequate "
                "nutrition can impair fibrinogen production.</li>"
                "<li><strong>Congenital fibrinogen deficiency:</strong> Rare inherited disorders "
                "(afibrinogenaemia, hypofibrinogenaemia) result in very low or undetectable "
                "fibrinogen.</li>"
                "</ul>"
                "<p>Your doctor may order additional coagulation tests (PT, aPTT, D-dimer), "
                "liver function tests and imaging studies depending on the clinical picture.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your <strong>fibrinogen blood test</strong> result falls outside the "
                "reference range, do not panic — but do consult a doctor. Evaluation should "
                "not be delayed if you experience unexplained bleeding tendency, easy bruising, "
                "prolonged wound healing or a history of recurrent thrombosis.</p>"
                "<p><strong>High fibrinogen</strong> is also relevant to cardiovascular risk "
                "assessment. Chronically <strong>elevated fibrinogen</strong> is considered an "
                "independent risk factor for atherosclerosis and thrombotic events. Your doctor "
                "may recommend regular fibrinogen monitoring as part of a broader cardiovascular "
                "evaluation.</p>"
                "<p>Remember: abnormal <strong>fibrinogen levels</strong> are not a diagnosis on "
                "their own. Your doctor will use further tests to identify the underlying cause "
                "and formulate an appropriate treatment plan. Early detection and regular follow-up "
                "improve outcomes in both bleeding and clotting disorders.</p>"
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
            heading="Prueba de fibrinógeno en sangre: qué significan sus resultados",
            body_html=(
                "<p>La <strong>prueba de fibrinógeno</strong> mide el nivel de "
                "<strong>fibrinógeno</strong>, una glucoproteína producida por el hígado que "
                "desempeña un papel fundamental en la coagulación de la sangre. En el último "
                "paso de la cascada de coagulación, la trombina convierte el fibrinógeno en "
                "fibrina, que forma el armazón estructural del coágulo sanguíneo. El fibrinógeno "
                "es además un <strong>reactante de fase aguda</strong>: sus niveles aumentan "
                "considerablemente durante infecciones, inflamaciones y lesiones tisulares.</p>"
                "<p>La <strong>prueba de fibrinógeno en sangre</strong> se utiliza tanto para "
                "diagnosticar trastornos de la coagulación como para evaluar la inflamación "
                "crónica y el riesgo cardiovascular. Un <strong>fibrinógeno alto</strong> puede "
                "indicar inflamación crónica, infección, cáncer o embarazo, mientras que un "
                "<strong>fibrinógeno bajo</strong> puede asociarse a coagulación intravascular "
                "diseminada (CID), enfermedad hepática o desnutrición.</p>"
                "<p>En esta guía encontrará el <strong>rango normal de fibrinógeno</strong>, "
                "las causas de fibrinógeno elevado o bajo y cuándo consultar al médico. "
                "Esta información es educativa — consulte siempre a un profesional de la salud.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rango normal de fibrinógeno (intervalos de referencia)",
            body_html=(
                "<p>El <strong>rango normal de fibrinógeno</strong> puede variar ligeramente "
                "entre laboratorios; los valores de referencia generalmente aceptados se "
                "resumen en la siguiente tabla:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal de fibrinógeno</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adultos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Recién nacidos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Embarazo (3.er trimestre)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Umbral crítico bajo</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Los intervalos de referencia dependen del método analítico (el método de Clauss "
                "es el más habitual) y del equipo utilizado; compare siempre su resultado con el "
                "rango indicado en su propio informe. Si sus <strong>niveles de fibrinógeno</strong> "
                "están fuera del rango normal, su médico podrá solicitar pruebas adicionales como "
                "un panel de coagulación, pruebas hepáticas y marcadores inflamatorios (PCR, VSG).</p>"
                "<p>Al ser una proteína de fase aguda, el fibrinógeno puede elevarse "
                "transitoriamente tras infecciones y cirugías. Una sola medición no siempre "
                "refleja un estado crónico; es importante valorar el contexto clínico.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de fibrinógeno alto y bajo",
            body_html=(
                "<p>El <strong>fibrinógeno alto</strong> y el <strong>fibrinógeno bajo</strong> "
                "tienen implicaciones clínicas diferentes. En ambos casos es necesario investigar "
                "la causa subyacente.</p>"
                "<p><strong>Causas de fibrinógeno elevado (hiperfibrinogenemia):</strong></p>"
                "<ul>"
                "<li><strong>Infección:</strong> Las infecciones bacterianas y virales activan "
                "la respuesta de fase aguda, elevando los niveles de fibrinógeno.</li>"
                "<li><strong>Inflamación crónica:</strong> Artritis reumatoide, enfermedad "
                "inflamatoria intestinal y vasculitis provocan un fibrinógeno persistentemente "
                "elevado.</li>"
                "<li><strong>Cáncer:</strong> Ciertos tumores sólidos y neoplasias hematológicas "
                "pueden aumentar la producción de fibrinógeno.</li>"
                "<li><strong>Embarazo:</strong> El fibrinógeno se eleva fisiológicamente, sobre "
                "todo en el tercer trimestre, como parte de la adaptación hemostática normal.</li>"
                "<li><strong>Tabaquismo:</strong> El consumo crónico de tabaco puede elevar de "
                "forma permanente los niveles de fibrinógeno y aumentar el riesgo cardiovascular.</li>"
                "</ul>"
                "<p><strong>Causas de fibrinógeno bajo (hipofibrinogenemia):</strong></p>"
                "<ul>"
                "<li><strong>Coagulación intravascular diseminada (CID):</strong> El consumo "
                "excesivo de fibrinógeno provoca un descenso rápido de sus niveles; se trata "
                "de una urgencia médica.</li>"
                "<li><strong>Enfermedad hepática:</strong> La cirrosis y la insuficiencia "
                "hepática avanzada reducen la síntesis de fibrinógeno.</li>"
                "<li><strong>Desnutrición:</strong> La deficiencia grave de proteínas o una "
                "alimentación insuficiente pueden afectar la producción de fibrinógeno.</li>"
                "<li><strong>Déficit congénito de fibrinógeno:</strong> Trastornos hereditarios "
                "poco frecuentes (afibrinogenemia, hipofibrinogenemia) resultan en niveles muy "
                "bajos o indetectables.</li>"
                "</ul>"
                "<p>Su médico podrá solicitar pruebas de coagulación adicionales (TP, TTPa, "
                "dímero D), pruebas hepáticas y estudios de imagen según el cuadro clínico.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si su <strong>prueba de fibrinógeno en sangre</strong> arroja un resultado "
                "fuera del rango de referencia, no se alarme, pero consulte a un médico. La "
                "evaluación no debe retrasarse si presenta tendencia hemorrágica inexplicable, "
                "moratones con facilidad, cicatrización lenta o antecedentes de trombosis "
                "recurrente.</p>"
                "<p>El <strong>fibrinógeno alto</strong> también es relevante en la evaluación "
                "del riesgo cardiovascular. Un fibrinógeno crónicamente elevado se considera un "
                "factor de riesgo independiente de aterosclerosis y eventos trombóticos. Su "
                "médico puede recomendar controles periódicos de fibrinógeno.</p>"
                "<p>Recuerde: unos <strong>niveles de fibrinógeno</strong> anormales no son un "
                "diagnóstico por sí solos. Su médico realizará pruebas adicionales para "
                "identificar la causa subyacente y establecer un plan de tratamiento adecuado. "
                "La detección temprana y el seguimiento regular mejoran los resultados tanto en "
                "trastornos hemorrágicos como trombóticos.</p>"
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
            heading="Fibrinogen-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>Fibrinogen-Test</strong> misst den Spiegel von "
                "<strong>Fibrinogen</strong>, einem in der Leber produzierten Glykoprotein, "
                "das eine entscheidende Rolle bei der Blutgerinnung spielt. Im letzten Schritt "
                "der Gerinnungskaskade wandelt Thrombin Fibrinogen in Fibrin um, das das "
                "strukturelle Gerüst eines Blutgerinnsels bildet. Fibrinogen ist zugleich ein "
                "<strong>Akute-Phase-Reaktant</strong>: Die <strong>Fibrinogenwerte</strong> "
                "steigen bei Infektion, Entzündung und Gewebeverletzung deutlich an.</p>"
                "<p>Der <strong>Fibrinogen-Bluttest</strong> wird sowohl zur Diagnostik von "
                "Gerinnungsstörungen als auch zur Beurteilung chronischer Entzündung und des "
                "kardiovaskulären Risikos eingesetzt. <strong>Hohe Fibrinogenwerte</strong> "
                "können auf chronische Entzündung, Infektion, Krebs oder Schwangerschaft "
                "hinweisen, während <strong>niedrige Fibrinogenwerte</strong> mit disseminierter "
                "intravasaler Gerinnung (DIC), Lebererkrankungen oder Mangelernährung in "
                "Verbindung gebracht werden.</p>"
                "<p>In diesem Ratgeber finden Sie den <strong>Fibrinogen-Normalbereich</strong>, "
                "Ursachen für erhöhtes und niedriges Fibrinogen und wann Sie einen Arzt "
                "aufsuchen sollten. Die Informationen hier dienen der Aufklärung — für "
                "Diagnose und Therapie wenden Sie sich bitte an einen Arzt.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Fibrinogen-Normalwerte (Referenzbereiche)",
            body_html=(
                "<p>Der <strong>Fibrinogen-Normalbereich</strong> kann zwischen Laboren leicht "
                "variieren; allgemein akzeptierte Referenzwerte sind in der folgenden Tabelle "
                "zusammengefasst:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fibrinogen-Normalbereich</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erwachsene</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neugeborene</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Schwangerschaft (3. Trimester)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kritische Untergrenze</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Die Referenzbereiche hängen von der Analysemethode (die Clauss-Methode ist "
                "am gebräuchlichsten) und dem Gerät ab; vergleichen Sie Ihr Ergebnis daher immer "
                "mit dem Bereich auf Ihrem eigenen Befund. Liegen Ihre "
                "<strong>Fibrinogenwerte</strong> außerhalb des Normalbereichs, kann Ihr Arzt "
                "ein Gerinnungsprofil, Leberfunktionstests und Entzündungsmarker (CRP, BSG) "
                "anordnen.</p>"
                "<p>Da Fibrinogen ein Akute-Phase-Protein ist, kann es nach Infektionen und "
                "Operationen vorübergehend ansteigen. Ein Einzelwert spiegelt nicht immer einen "
                "chronischen Zustand wider; die klinische Einordnung ist entscheidend.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für hohes und niedriges Fibrinogen",
            body_html=(
                "<p><strong>Hohes Fibrinogen</strong> und <strong>niedriges Fibrinogen</strong> "
                "haben unterschiedliche klinische Bedeutungen. In beiden Fällen sollte die "
                "zugrunde liegende Ursache abgeklärt werden.</p>"
                "<p><strong>Ursachen für erhöhtes Fibrinogen (Hyperfibrinogenämie):</strong></p>"
                "<ul>"
                "<li><strong>Infektion:</strong> Bakterielle und virale Infektionen lösen die "
                "Akute-Phase-Reaktion aus und erhöhen die Fibrinogenwerte.</li>"
                "<li><strong>Chronische Entzündung:</strong> Erkrankungen wie rheumatoide "
                "Arthritis, chronisch-entzündliche Darmerkrankungen und Vaskulitis führen zu "
                "anhaltend erhöhtem Fibrinogen.</li>"
                "<li><strong>Krebs:</strong> Bestimmte solide Tumoren und hämatologische "
                "Malignome können die Fibrinogenproduktion steigern.</li>"
                "<li><strong>Schwangerschaft:</strong> Fibrinogen steigt physiologisch an, "
                "besonders im dritten Trimester, als Teil der normalen hämostatischen "
                "Anpassung.</li>"
                "<li><strong>Rauchen:</strong> Chronischer Tabakkonsum kann die "
                "<strong>Fibrinogenwerte</strong> dauerhaft erhöhen und das kardiovaskuläre "
                "Risiko steigern.</li>"
                "</ul>"
                "<p><strong>Ursachen für niedriges Fibrinogen (Hypofibrinogenämie):</strong></p>"
                "<ul>"
                "<li><strong>Disseminierte intravasale Gerinnung (DIC):</strong> Der übermäßige "
                "Verbrauch von Fibrinogen lässt die Werte rasch sinken; dies ist ein "
                "medizinischer Notfall.</li>"
                "<li><strong>Lebererkrankungen:</strong> Zirrhose und fortgeschrittenes "
                "Leberversagen vermindern die Fibrinogensynthese.</li>"
                "<li><strong>Mangelernährung:</strong> Schwerer Proteinmangel oder unzureichende "
                "Ernährung können die Fibrinogenproduktion beeinträchtigen.</li>"
                "<li><strong>Angeborener Fibrinogenmangel:</strong> Seltene erbliche Störungen "
                "(Afibrinogenämie, Hypofibrinogenämie) führen zu sehr niedrigen oder nicht "
                "nachweisbaren Fibrinogenwerten.</li>"
                "</ul>"
                "<p>Ihr Arzt kann je nach klinischem Bild zusätzliche Gerinnungstests (PT, "
                "aPTT, D-Dimer), Leberfunktionstests und bildgebende Verfahren anordnen.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Liegt Ihr <strong>Fibrinogen-Bluttest</strong>-Ergebnis außerhalb des "
                "Referenzbereichs, bewahren Sie Ruhe, suchen Sie aber einen Arzt auf. Eine "
                "Abklärung sollte nicht verzögert werden, wenn Sie unter unerklärlicher "
                "Blutungsneigung, leichter Hämatombildung, verzögerter Wundheilung oder "
                "wiederkehrenden Thrombosen leiden.</p>"
                "<p><strong>Hohe Fibrinogenwerte</strong> sind auch für die kardiovaskuläre "
                "Risikobewertung relevant. Chronisch <strong>erhöhtes Fibrinogen</strong> gilt "
                "als unabhängiger Risikofaktor für Atherosklerose und thrombotische Ereignisse. "
                "Ihr Arzt empfiehlt möglicherweise regelmäßige Fibrinogenkontrollen.</p>"
                "<p>Denken Sie daran: Abnormale <strong>Fibrinogenwerte</strong> sind allein "
                "keine Diagnose. Ihr Arzt wird weitere Untersuchungen durchführen, um die "
                "Ursache zu ermitteln und einen geeigneten Behandlungsplan zu erstellen. "
                "Früherkennung und regelmäßige Kontrollen verbessern die Prognose bei "
                "Blutungs- und Gerinnungsstörungen erheblich.</p>"
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
            heading="Test de fibrinogène : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test de fibrinogène</strong> mesure le taux de "
                "<strong>fibrinogène</strong>, une glycoprotéine produite par le foie qui joue "
                "un rôle essentiel dans la coagulation sanguine. Lors de la dernière étape de "
                "la cascade de coagulation, la thrombine convertit le fibrinogène en fibrine, "
                "formant l'armature structurelle du caillot. Le fibrinogène est également un "
                "<strong>réactant de phase aiguë</strong> : ses taux augmentent nettement lors "
                "d'infections, d'inflammations et de lésions tissulaires.</p>"
                "<p>Le <strong>test de fibrinogène dans le sang</strong> est utilisé à la fois "
                "pour diagnostiquer les troubles de la coagulation et pour évaluer l'inflammation "
                "chronique et le risque cardiovasculaire. Un <strong>fibrinogène élevé</strong> "
                "peut indiquer une inflammation chronique, une infection, un cancer ou une "
                "grossesse, tandis qu'un <strong>fibrinogène bas</strong> peut être associé à "
                "une coagulation intravasculaire disséminée (CIVD), une maladie hépatique ou "
                "une malnutrition.</p>"
                "<p>Dans ce guide vous trouverez les <strong>valeurs normales du fibrinogène</strong>, "
                "les causes de fibrinogène élevé ou bas et quand consulter un médecin. Ces "
                "informations sont à visée éducative — consultez toujours un professionnel "
                "de santé.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales du fibrinogène (intervalles de référence)",
            body_html=(
                "<p>Les <strong>valeurs normales du fibrinogène</strong> peuvent varier "
                "légèrement d'un laboratoire à l'autre ; les valeurs de référence généralement "
                "admises sont résumées dans le tableau ci-dessous :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valeurs normales du fibrinogène</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adultes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Nouveau-nés</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Grossesse (3ᵉ trimestre)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Seuil critique bas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Les intervalles de référence dépendent de la méthode d'analyse (la méthode "
                "de Clauss est la plus courante) et de l'appareil utilisé ; comparez donc "
                "toujours votre résultat avec la plage indiquée sur votre propre rapport. Si "
                "vos <strong>taux de fibrinogène</strong> sont en dehors de la norme, votre "
                "médecin pourra demander un bilan de coagulation, un bilan hépatique et des "
                "marqueurs inflammatoires (CRP, VS).</p>"
                "<p>Le fibrinogène étant une protéine de phase aiguë, il peut s'élever "
                "temporairement après des infections et des interventions chirurgicales. "
                "Une seule mesure ne reflète pas toujours un état chronique ; le contexte "
                "clinique est indispensable à l'interprétation.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un fibrinogène élevé ou bas",
            body_html=(
                "<p>Un <strong>fibrinogène élevé</strong> et un <strong>fibrinogène bas</strong> "
                "ont des significations cliniques différentes. Dans les deux cas, il convient "
                "d'en rechercher la cause sous-jacente.</p>"
                "<p><strong>Causes de fibrinogène élevé (hyperfibrinogénémie) :</strong></p>"
                "<ul>"
                "<li><strong>Infection :</strong> Les infections bactériennes et virales "
                "déclenchent la réponse de phase aiguë et élèvent les taux de fibrinogène.</li>"
                "<li><strong>Inflammation chronique :</strong> Polyarthrite rhumatoïde, maladies "
                "inflammatoires de l'intestin et vascularites entraînent un fibrinogène "
                "durablement élevé.</li>"
                "<li><strong>Cancer :</strong> Certaines tumeurs solides et hémopathies malignes "
                "peuvent augmenter la production de fibrinogène.</li>"
                "<li><strong>Grossesse :</strong> Le fibrinogène s'élève physiologiquement, "
                "surtout au troisième trimestre, dans le cadre de l'adaptation hémostatique "
                "normale.</li>"
                "<li><strong>Tabagisme :</strong> La consommation chronique de tabac peut "
                "augmenter durablement les taux de fibrinogène et accroître le risque "
                "cardiovasculaire.</li>"
                "</ul>"
                "<p><strong>Causes de fibrinogène bas (hypofibrinogénémie) :</strong></p>"
                "<ul>"
                "<li><strong>Coagulation intravasculaire disséminée (CIVD) :</strong> La "
                "consommation excessive de fibrinogène fait chuter rapidement les taux ; "
                "il s'agit d'une urgence médicale.</li>"
                "<li><strong>Maladie hépatique :</strong> La cirrhose et l'insuffisance "
                "hépatique avancée réduisent la synthèse de fibrinogène.</li>"
                "<li><strong>Malnutrition :</strong> Une carence protéique sévère ou une "
                "alimentation insuffisante peut altérer la production de fibrinogène.</li>"
                "<li><strong>Déficit congénital en fibrinogène :</strong> Des anomalies "
                "héréditaires rares (afibrinogénémie, hypofibrinogénémie) entraînent des "
                "taux très bas ou indétectables.</li>"
                "</ul>"
                "<p>Votre médecin pourra prescrire des tests de coagulation supplémentaires "
                "(TP, TCA, D-dimères), un bilan hépatique et des examens d'imagerie selon "
                "le tableau clinique.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si le résultat de votre <strong>test de fibrinogène</strong> est en dehors "
                "de l'intervalle de référence, ne paniquez pas, mais consultez un médecin. "
                "L'évaluation ne doit pas être retardée si vous présentez une tendance "
                "hémorragique inexpliquée, des ecchymoses faciles, une cicatrisation lente "
                "ou des antécédents de thromboses récurrentes.</p>"
                "<p>Un <strong>fibrinogène élevé</strong> est également pertinent dans "
                "l'évaluation du risque cardiovasculaire. Un fibrinogène chroniquement élevé "
                "est considéré comme un facteur de risque indépendant d'athérosclérose et "
                "d'événements thrombotiques. Votre médecin pourra recommander un suivi "
                "régulier du fibrinogène.</p>"
                "<p>N'oubliez pas : des <strong>taux de fibrinogène</strong> anormaux ne "
                "constituent pas un diagnostic en soi. Votre médecin effectuera des examens "
                "complémentaires pour identifier la cause sous-jacente et établir un plan de "
                "traitement adapté. Le dépistage précoce et un suivi régulier améliorent "
                "significativement le pronostic dans les troubles hémorragiques et "
                "thrombotiques.</p>"
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
            heading="Test del fibrinogeno: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test del fibrinogeno</strong> misura il livello di "
                "<strong>fibrinogeno</strong>, una glicoproteina prodotta dal fegato che svolge "
                "un ruolo fondamentale nella coagulazione del sangue. Nell'ultimo passaggio "
                "della cascata coagulativa, la trombina converte il fibrinogeno in fibrina, che "
                "costituisce l'impalcatura strutturale del coagulo. Il fibrinogeno è anche un "
                "<strong>reagente di fase acuta</strong>: i suoi livelli aumentano "
                "significativamente durante infezioni, infiammazioni e lesioni tissutali.</p>"
                "<p>Il <strong>test del fibrinogeno nel sangue</strong> viene utilizzato sia per "
                "diagnosticare disturbi della coagulazione sia per valutare l'infiammazione "
                "cronica e il rischio cardiovascolare. Un <strong>fibrinogeno alto</strong> "
                "può indicare infiammazione cronica, infezione, cancro o gravidanza, mentre un "
                "<strong>fibrinogeno basso</strong> può essere associato a coagulazione "
                "intravascolare disseminata (CID), malattia epatica o malnutrizione.</p>"
                "<p>In questa guida troverai l'<strong>intervallo normale del fibrinogeno</strong>, "
                "le cause di fibrinogeno elevato o basso e quando rivolgersi al medico. Le "
                "informazioni qui riportate hanno scopo educativo — consultate sempre un "
                "professionista sanitario.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del fibrinogeno (intervalli di riferimento)",
            body_html=(
                "<p>L'<strong>intervallo normale del fibrinogeno</strong> può variare "
                "leggermente tra i laboratori; i valori di riferimento generalmente accettati "
                "sono riassunti nella tabella seguente:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale del fibrinogeno</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adulti</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neonati</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Gravidanza (3° trimestre)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Soglia critica bassa</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Gli intervalli di riferimento dipendono dal metodo analitico (il metodo di "
                "Clauss è il più diffuso) e dallo strumento utilizzato; confrontate sempre il "
                "vostro risultato con l'intervallo indicato nel vostro referto. Se i vostri "
                "<strong>livelli di fibrinogeno</strong> sono fuori dalla norma, il medico "
                "potrà richiedere un profilo coagulativo, test di funzionalità epatica e "
                "marcatori infiammatori (PCR, VES).</p>"
                "<p>Essendo una proteina di fase acuta, il fibrinogeno può aumentare "
                "temporaneamente dopo infezioni e interventi chirurgici. Un singolo valore "
                "non riflette sempre una condizione cronica; il contesto clinico è "
                "fondamentale.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di fibrinogeno alto e basso",
            body_html=(
                "<p>Il <strong>fibrinogeno alto</strong> e il <strong>fibrinogeno basso</strong> "
                "hanno implicazioni cliniche diverse. In entrambi i casi è necessario "
                "indagare la causa sottostante.</p>"
                "<p><strong>Cause di fibrinogeno elevato (iperfibrinogenemia):</strong></p>"
                "<ul>"
                "<li><strong>Infezione:</strong> Le infezioni batteriche e virali attivano "
                "la risposta di fase acuta, innalzando i livelli di fibrinogeno.</li>"
                "<li><strong>Infiammazione cronica:</strong> Artrite reumatoide, malattie "
                "infiammatorie intestinali e vasculiti causano un fibrinogeno persistentemente "
                "elevato.</li>"
                "<li><strong>Cancro:</strong> Alcuni tumori solidi e neoplasie ematologiche "
                "possono aumentare la produzione di fibrinogeno.</li>"
                "<li><strong>Gravidanza:</strong> Il fibrinogeno aumenta fisiologicamente, "
                "soprattutto nel terzo trimestre, come parte dell'adattamento emostatico "
                "normale.</li>"
                "<li><strong>Fumo:</strong> Il consumo cronico di tabacco può elevare "
                "permanentemente i livelli di fibrinogeno e aumentare il rischio "
                "cardiovascolare.</li>"
                "</ul>"
                "<p><strong>Cause di fibrinogeno basso (ipofibrinogenemia):</strong></p>"
                "<ul>"
                "<li><strong>Coagulazione intravascolare disseminata (CID):</strong> Il "
                "consumo eccessivo di fibrinogeno provoca un rapido calo dei livelli; si "
                "tratta di un'emergenza medica.</li>"
                "<li><strong>Malattia epatica:</strong> Cirrosi e insufficienza epatica "
                "avanzata riducono la sintesi di fibrinogeno.</li>"
                "<li><strong>Malnutrizione:</strong> Una grave carenza proteica o "
                "un'alimentazione inadeguata possono compromettere la produzione di "
                "fibrinogeno.</li>"
                "<li><strong>Deficit congenito di fibrinogeno:</strong> Rare anomalie "
                "ereditarie (afibrinogenemia, ipofibrinogenemia) comportano livelli molto "
                "bassi o non rilevabili.</li>"
                "</ul>"
                "<p>Il medico potrà prescrivere ulteriori test coagulativi (PT, aPTT, "
                "D-dimero), test di funzionalità epatica ed esami di imaging in base al "
                "quadro clinico.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se il risultato del vostro <strong>test del fibrinogeno</strong> è fuori "
                "dall'intervallo di riferimento, non allarmatevi, ma consultate un medico. "
                "La valutazione non deve essere ritardata se accusate tendenza emorragica "
                "inspiegabile, ecchimosi facili, cicatrizzazione lenta o anamnesi di "
                "trombosi ricorrenti.</p>"
                "<p>Il <strong>fibrinogeno alto</strong> è rilevante anche nella valutazione "
                "del rischio cardiovascolare. Un fibrinogeno cronicamente elevato è "
                "considerato un fattore di rischio indipendente per aterosclerosi ed "
                "eventi trombotici. Il medico può consigliare controlli regolari del "
                "fibrinogeno.</p>"
                "<p>Ricordate: <strong>livelli di fibrinogeno</strong> anomali non sono di "
                "per sé una diagnosi. Il medico effettuerà ulteriori esami per individuare "
                "la causa sottostante e definire un piano terapeutico adeguato. La diagnosi "
                "precoce e il follow-up regolare migliorano significativamente gli esiti "
                "nei disturbi emorragici e trombotici.</p>"
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
            heading="בדיקת פיברינוגן בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>בדיקת <strong>פיברינוגן</strong> מודדת את רמת ה<strong>פיברינוגן</strong> "
                "בדם — גליקופרוטאין המיוצר בכבד וממלא תפקיד קריטי בקרישת הדם. בשלב האחרון "
                "של מפל הקרישה, תרומבין הופך פיברינוגן לפיברין, היוצר את השלד המבני של "
                "הקריש. פיברינוגן הוא גם <strong>חלבון שלב חריף</strong>: רמותיו עולות "
                "משמעותית בזמן זיהום, דלקת ופגיעה רקמתית.</p>"
                "<p><strong>בדיקת פיברינוגן בדם</strong> משמשת הן לאבחון הפרעות קרישה והן "
                "להערכת דלקת כרונית וסיכון קרדיווסקולרי. <strong>פיברינוגן גבוה</strong> עשוי "
                "להצביע על דלקת כרונית, זיהום, סרטן או הריון, בעוד <strong>פיברינוגן נמוך</strong> "
                "עלול להיות קשור לקרישה תוך-כלית מפושטת (DIC), מחלת כבד או תת-תזונה.</p>"
                "<p>במדריך זה תמצאו את <strong>טווח הנורמה של פיברינוגן</strong>, גורמים "
                "לפיברינוגן גבוה או נמוך ומתי יש לפנות לרופא. המידע כאן הוא לצורכי "
                "הסברה בלבד — התייעצו תמיד עם רופא.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי פיברינוגן תקינים (טווחי ייחוס)",
            body_html=(
                "<p><strong>טווח הנורמה של פיברינוגן</strong> עשוי להשתנות מעט בין מעבדות; "
                "ערכי הייחוס המקובלים מסוכמים בטבלה הבאה:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח פיברינוגן תקין</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">מבוגרים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">יילודים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">הריון (טרימסטר 3)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">סף קריטי נמוך</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>טווחי הייחוס תלויים בשיטת הבדיקה (שיטת קלאוס היא הנפוצה ביותר) "
                "ובמכשיר; לכן השוו תמיד את התוצאה שלכם לטווח המופיע בדוח שלכם. אם "
                "<strong>רמות הפיברינוגן</strong> שלכם חורגות מהנורמה, הרופא עשוי "
                "להזמין פרופיל קרישה, בדיקות תפקודי כבד וסמני דלקת (CRP, שקיעת דם).</p>"
                "<p>מכיוון שפיברינוגן הוא חלבון שלב חריף, הוא עלול לעלות באופן זמני "
                "לאחר זיהומים וניתוחים. מדידה בודדת לא תמיד משקפת מצב כרוני; "
                "ההקשר הקליני חיוני לפרשנות.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לפיברינוגן גבוה ונמוך",
            body_html=(
                "<p>ל<strong>פיברינוגן גבוה</strong> ול<strong>פיברינוגן נמוך</strong> "
                "משמעויות קליניות שונות. בשני המקרים יש לברר את הסיבה הבסיסית.</p>"
                "<p><strong>גורמים לפיברינוגן מוגבר (היפרפיברינוגנמיה):</strong></p>"
                "<ul>"
                "<li><strong>זיהום:</strong> זיהומים חיידקיים וויראליים מפעילים את תגובת "
                "השלב החריף ומעלים את רמות הפיברינוגן.</li>"
                "<li><strong>דלקת כרונית:</strong> דלקת מפרקים שגרונית, מחלות מעי "
                "דלקתיות ודלקת כלי דם גורמות לפיברינוגן מוגבר באופן מתמשך.</li>"
                "<li><strong>סרטן:</strong> גידולים סולידיים מסוימים וממאירויות "
                "המטולוגיות עלולים להגביר את ייצור הפיברינוגן.</li>"
                "<li><strong>הריון:</strong> הפיברינוגן עולה באופן פיזיולוגי, במיוחד "
                "בטרימסטר השלישי, כחלק מההתאמה ההמוסטטית הרגילה.</li>"
                "<li><strong>עישון:</strong> עישון כרוני עלול להעלות את רמות הפיברינוגן "
                "באופן קבוע ולהגביר את הסיכון הקרדיווסקולרי.</li>"
                "</ul>"
                "<p><strong>גורמים לפיברינוגן נמוך (היפופיברינוגנמיה):</strong></p>"
                "<ul>"
                "<li><strong>קרישה תוך-כלית מפושטת (DIC):</strong> צריכה מוגזמת של "
                "פיברינוגן גורמת לירידה מהירה ברמות; זהו מצב חירום רפואי.</li>"
                "<li><strong>מחלת כבד:</strong> שחמת ואי-ספיקת כבד מתקדמת מפחיתות "
                "את סינתזת הפיברינוגן.</li>"
                "<li><strong>תת-תזונה:</strong> חסר חלבוני חמור או תזונה לקויה עלולים "
                "לפגוע בייצור הפיברינוגן.</li>"
                "<li><strong>חסר מולד של פיברינוגן:</strong> הפרעות תורשתיות נדירות "
                "(אפיברינוגנמיה, היפופיברינוגנמיה) גורמות לרמות נמוכות מאוד או בלתי "
                "ניתנות לזיהוי.</li>"
                "</ul>"
                "<p>הרופא עשוי להזמין בדיקות קרישה נוספות (PT, aPTT, D-dimer), בדיקות "
                "תפקודי כבד ובדיקות הדמיה בהתאם לתמונה הקלינית.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם תוצאת <strong>בדיקת הפיברינוגן בדם</strong> שלכם חורגת מטווח "
                "הייחוס, אל תיבהלו — אך פנו לרופא. אין לדחות את הבירור אם אתם סובלים "
                "מנטייה לדימום בלתי מוסברת, שטפי דם תת-עוריים קלים, ריפוי פצעים איטי "
                "או היסטוריה של פקקת חוזרת.</p>"
                "<p><strong>פיברינוגן גבוה</strong> רלוונטי גם להערכת הסיכון "
                "הקרדיווסקולרי. פיברינוגן מוגבר באופן כרוני נחשב לגורם סיכון עצמאי "
                "לטרשת עורקים ולאירועים פקקתיים. הרופא עשוי להמליץ על מעקב סדיר "
                "אחר רמות הפיברינוגן.</p>"
                "<p>זכרו: רמות <strong>פיברינוגן</strong> חריגות אינן אבחנה בפני "
                "עצמן. הרופא יבצע בדיקות נוספות לזיהוי הסיבה הבסיסית ולגיבוש תוכנית "
                "טיפול מתאימה. גילוי מוקדם ומעקב סדיר משפרים משמעותית את התוצאות "
                "בהפרעות דימום וקרישה כאחד.</p>"
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
            heading="फाइब्रिनोजन ब्लड टेस्ट: आपके रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>फाइब्रिनोजन टेस्ट</strong> रक्त में <strong>फाइब्रिनोजन</strong> "
                "के स्तर को मापता है — यह लिवर द्वारा निर्मित एक ग्लाइकोप्रोटीन है जो रक्त "
                "के थक्के बनने (कोएगुलेशन) में महत्वपूर्ण भूमिका निभाता है। कोएगुलेशन कैस्केड "
                "के अंतिम चरण में, थ्रोम्बिन फाइब्रिनोजन को फाइब्रिन में बदलता है, जो थक्के "
                "का संरचनात्मक ढाँचा बनाता है। फाइब्रिनोजन एक <strong>एक्यूट-फेज़ रिएक्टेंट</strong> "
                "भी है: संक्रमण, सूजन और ऊतक चोट के दौरान इसके स्तर काफ़ी बढ़ जाते हैं।</p>"
                "<p><strong>फाइब्रिनोजन ब्लड टेस्ट</strong> का उपयोग क्लॉटिंग विकारों के निदान "
                "और क्रोनिक इन्फ़्लेमेशन व कार्डियोवैस्कुलर जोखिम मूल्यांकन दोनों के लिए "
                "किया जाता है। <strong>हाई फाइब्रिनोजन</strong> क्रोनिक इन्फ़्लेमेशन, संक्रमण, "
                "कैंसर या गर्भावस्था की ओर इशारा कर सकता है, जबकि <strong>लो फाइब्रिनोजन</strong> "
                "DIC (डिसेमिनेटेड इंट्रावैस्कुलर कोएगुलेशन), लिवर रोग या कुपोषण से जुड़ा "
                "हो सकता है।</p>"
                "<p>इस गाइड में आपको <strong>फाइब्रिनोजन की नॉर्मल रेंज</strong>, उच्च और "
                "निम्न फाइब्रिनोजन के कारण और डॉक्टर से कब मिलना चाहिए, इसकी जानकारी "
                "मिलेगी। यह जानकारी शैक्षिक उद्देश्य से है — निदान और उपचार के लिए "
                "हमेशा डॉक्टर से परामर्श करें।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="फाइब्रिनोजन की नॉर्मल रेंज (रेफ़रेंस इंटरवल)",
            body_html=(
                "<p><strong>फाइब्रिनोजन की नॉर्मल रेंज</strong> लैब के अनुसार थोड़ी "
                "अलग हो सकती है; सामान्य रूप से स्वीकृत रेफ़रेंस वैल्यू नीचे दी गई "
                "तालिका में संक्षेपित हैं:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">फाइब्रिनोजन नॉर्मल रेंज</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">नवजात</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">गर्भावस्था (तीसरी तिमाही)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">गंभीर निम्न सीमा</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>रेफ़रेंस इंटरवल टेस्ट मेथड (क्लॉस मेथड सबसे सामान्य है) और एनालाइज़र "
                "पर निर्भर करता है; इसलिए अपनी रिपोर्ट पर छपी रेंज से हमेशा तुलना करें। "
                "अगर आपके <strong>फाइब्रिनोजन के स्तर</strong> नॉर्मल रेंज से बाहर हैं, "
                "तो डॉक्टर कोएगुलेशन पैनल, लिवर फ़ंक्शन टेस्ट और इन्फ़्लेमेटरी मार्कर "
                "(CRP, ESR) जैसे अतिरिक्त टेस्ट करवा सकते हैं।</p>"
                "<p>चूँकि फाइब्रिनोजन एक एक्यूट-फेज़ प्रोटीन है, यह संक्रमण और सर्जरी "
                "के बाद अस्थायी रूप से बढ़ सकता है। एक बार की माप हमेशा क्रोनिक स्थिति "
                "को नहीं दर्शाती; क्लिनिकल संदर्भ में व्याख्या ज़रूरी है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई और लो फाइब्रिनोजन के कारण",
            body_html=(
                "<p><strong>हाई फाइब्रिनोजन</strong> और <strong>लो फाइब्रिनोजन</strong> "
                "की अलग-अलग क्लिनिकल मायने हैं। दोनों मामलों में अंतर्निहित कारण "
                "जानना ज़रूरी है।</p>"
                "<p><strong>एलिवेटेड फाइब्रिनोजन (हाइपरफाइब्रिनोजनेमिया) के कारण:</strong></p>"
                "<ul>"
                "<li><strong>संक्रमण:</strong> बैक्टीरियल और वायरल संक्रमण एक्यूट-फेज़ "
                "रिस्पॉन्स को ट्रिगर करके फाइब्रिनोजन के स्तर को बढ़ाते हैं।</li>"
                "<li><strong>क्रोनिक इन्फ़्लेमेशन:</strong> रूमेटॉइड आर्थराइटिस, "
                "इन्फ़्लेमेटरी बाउल डिज़ीज़ और वैस्कुलाइटिस से फाइब्रिनोजन लगातार "
                "ऊँचा बना रहता है।</li>"
                "<li><strong>कैंसर:</strong> कुछ सॉलिड ट्यूमर और हेमेटोलॉजिकल "
                "मैलिग्नेंसी फाइब्रिनोजन उत्पादन बढ़ा सकती हैं।</li>"
                "<li><strong>गर्भावस्था:</strong> फाइब्रिनोजन शारीरिक रूप से बढ़ता है, "
                "विशेषकर तीसरी तिमाही में, सामान्य हीमोस्टैटिक अनुकूलन के हिस्से "
                "के रूप में।</li>"
                "<li><strong>धूम्रपान:</strong> लंबे समय तक तंबाकू का उपयोग "
                "फाइब्रिनोजन के स्तर को स्थायी रूप से बढ़ा सकता है और "
                "कार्डियोवैस्कुलर जोखिम बढ़ाता है।</li>"
                "</ul>"
                "<p><strong>लो फाइब्रिनोजन (हाइपोफाइब्रिनोजनेमिया) के कारण:</strong></p>"
                "<ul>"
                "<li><strong>डिसेमिनेटेड इंट्रावैस्कुलर कोएगुलेशन (DIC):</strong> "
                "फाइब्रिनोजन की अत्यधिक खपत से इसका स्तर तेज़ी से गिरता है; यह "
                "एक मेडिकल इमरजेंसी है।</li>"
                "<li><strong>लिवर रोग:</strong> सिरोसिस और एडवांस्ड लिवर फ़ेल्योर "
                "फाइब्रिनोजन संश्लेषण को कम करता है।</li>"
                "<li><strong>कुपोषण:</strong> गंभीर प्रोटीन की कमी या अपर्याप्त "
                "पोषण फाइब्रिनोजन उत्पादन को प्रभावित कर सकता है।</li>"
                "<li><strong>जन्मजात फाइब्रिनोजन की कमी:</strong> दुर्लभ वंशानुगत "
                "विकार (एफाइब्रिनोजनेमिया, हाइपोफाइब्रिनोजनेमिया) में फाइब्रिनोजन "
                "बहुत कम या पता न लगने योग्य होता है।</li>"
                "</ul>"
                "<p>डॉक्टर क्लिनिकल स्थिति के अनुसार अतिरिक्त कोएगुलेशन टेस्ट "
                "(PT, aPTT, D-dimer), लिवर फ़ंक्शन टेस्ट और इमेजिंग स्टडीज़ "
                "करवा सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपके <strong>फाइब्रिनोजन ब्लड टेस्ट</strong> का रिज़ल्ट "
                "रेफ़रेंस रेंज से बाहर है, तो घबराएँ नहीं — लेकिन डॉक्टर से ज़रूर मिलें। "
                "अगर बिना वजह ब्लीडिंग की प्रवृत्ति, आसानी से नील पड़ना, घाव भरने में "
                "देरी या बार-बार थ्रोम्बोसिस का इतिहास हो तो मूल्यांकन में देरी नहीं "
                "करनी चाहिए।</p>"
                "<p><strong>हाई फाइब्रिनोजन</strong> कार्डियोवैस्कुलर जोखिम मूल्यांकन "
                "में भी महत्वपूर्ण है। लंबे समय से ऊँचा फाइब्रिनोजन एथेरोस्क्लेरोसिस "
                "और थ्रोम्बोटिक इवेंट्स के लिए एक स्वतंत्र जोखिम कारक माना जाता है। "
                "डॉक्टर नियमित फाइब्रिनोजन मॉनिटरिंग की सलाह दे सकते हैं।</p>"
                "<p>याद रखें: असामान्य <strong>फाइब्रिनोजन के स्तर</strong> अपने आप में "
                "कोई निदान नहीं हैं। डॉक्टर अंतर्निहित कारण की पहचान करने और उचित "
                "उपचार योजना बनाने के लिए अतिरिक्त जाँच करेंगे। शीघ्र पहचान और "
                "नियमित फ़ॉलो-अप ब्लीडिंग और क्लॉटिंग दोनों विकारों में परिणामों को "
                "काफ़ी बेहतर बनाते हैं।</p>"
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
            heading="اختبار الفيبرينوجين في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>يقيس <strong>اختبار الفيبرينوجين</strong> مستوى "
                "<strong>الفيبرينوجين</strong> في الدم — وهو بروتين سكري يُنتَج في الكبد "
                "ويلعب دوراً حاسماً في تخثر الدم. في الخطوة الأخيرة من شلال التخثر، "
                "يحوّل الثرومبين الفيبرينوجين إلى فيبرين الذي يشكّل الهيكل البنيوي للخثرة "
                "الدموية. الفيبرينوجين هو أيضاً <strong>مُتفاعل الطور الحاد</strong>: ترتفع "
                "مستوياته بشكل ملحوظ أثناء العدوى والالتهاب وإصابة الأنسجة.</p>"
                "<p>يُستخدم <strong>اختبار الفيبرينوجين في الدم</strong> لتشخيص اضطرابات "
                "التخثر وكذلك لتقييم الالتهاب المزمن والمخاطر القلبية الوعائية. قد يشير "
                "<strong>ارتفاع الفيبرينوجين</strong> إلى التهاب مزمن أو عدوى أو سرطان "
                "أو حمل، بينما قد يرتبط <strong>انخفاض الفيبرينوجين</strong> بالتخثر "
                "المنتشر داخل الأوعية (DIC) أو مرض الكبد أو سوء التغذية.</p>"
                "<p>ستجد في هذا الدليل <strong>المعدل الطبيعي للفيبرينوجين</strong>، "
                "وأسباب ارتفاعه وانخفاضه، ومتى يجب مراجعة الطبيب. المعلومات هنا "
                "تثقيفية — استشر دائماً طبيباً مختصاً.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدل الطبيعي للفيبرينوجين (النطاقات المرجعية)",
            body_html=(
                "<p>قد يختلف <strong>المعدل الطبيعي للفيبرينوجين</strong> قليلاً بين "
                "المختبرات؛ القيم المرجعية المقبولة عموماً ملخصة في الجدول التالي:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المعدل الطبيعي للفيبرينوجين</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">البالغون</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200–400 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">حديثو الولادة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">125–300 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الحمل (الثلث الثالث)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">400–600 mg/dL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">العتبة الحرجة المنخفضة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;100 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>تعتمد النطاقات المرجعية على طريقة الفحص (طريقة كلاوس هي الأكثر "
                "شيوعاً) والجهاز المستخدم؛ لذا قارن دائماً نتيجتك بالنطاق المطبوع في "
                "تقريرك. إذا كانت <strong>مستويات الفيبرينوجين</strong> لديك خارج "
                "النطاق الطبيعي، فقد يطلب الطبيب ملف تخثر واختبارات وظائف الكبد "
                "وعلامات الالتهاب (CRP، سرعة الترسيب).</p>"
                "<p>نظراً لأن الفيبرينوجين بروتين طور حاد، فقد يرتفع مؤقتاً بعد "
                "العدوى والعمليات الجراحية. قياس واحد لا يعكس دائماً حالة مزمنة؛ "
                "السياق السريري ضروري للتفسير.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع وانخفاض الفيبرينوجين",
            body_html=(
                "<p>لكل من <strong>ارتفاع الفيبرينوجين</strong> "
                "و<strong>انخفاض الفيبرينوجين</strong> دلالات سريرية مختلفة. في كلتا "
                "الحالتين يجب التحقيق في السبب الكامن.</p>"
                "<p><strong>أسباب ارتفاع الفيبرينوجين (فرط فيبرينوجين الدم):</strong></p>"
                "<ul>"
                "<li><strong>العدوى:</strong> تُفعّل العدوى البكتيرية والفيروسية "
                "استجابة الطور الحاد وترفع مستويات الفيبرينوجين.</li>"
                "<li><strong>الالتهاب المزمن:</strong> التهاب المفاصل الروماتويدي "
                "وأمراض الأمعاء الالتهابية والتهاب الأوعية تسبب ارتفاعاً مستمراً في "
                "الفيبرينوجين.</li>"
                "<li><strong>السرطان:</strong> بعض الأورام الصلبة والأورام الخبيثة "
                "الدموية قد تزيد إنتاج الفيبرينوجين.</li>"
                "<li><strong>الحمل:</strong> يرتفع الفيبرينوجين فسيولوجياً، خاصةً في "
                "الثلث الثالث، كجزء من التكيّف الإرقائي الطبيعي.</li>"
                "<li><strong>التدخين:</strong> يمكن أن يؤدي التدخين المزمن إلى رفع "
                "مستويات الفيبرينوجين بشكل دائم وزيادة المخاطر القلبية الوعائية.</li>"
                "</ul>"
                "<p><strong>أسباب انخفاض الفيبرينوجين (نقص فيبرينوجين الدم):</strong></p>"
                "<ul>"
                "<li><strong>التخثر المنتشر داخل الأوعية (DIC):</strong> الاستهلاك "
                "المفرط للفيبرينوجين يؤدي إلى انخفاض سريع في مستوياته؛ وهي حالة "
                "طوارئ طبية.</li>"
                "<li><strong>مرض الكبد:</strong> تليف الكبد والفشل الكبدي المتقدم "
                "يقللان من تصنيع الفيبرينوجين.</li>"
                "<li><strong>سوء التغذية:</strong> نقص البروتين الشديد أو التغذية "
                "غير الكافية قد يُضعف إنتاج الفيبرينوجين.</li>"
                "<li><strong>نقص الفيبرينوجين الخلقي:</strong> اضطرابات وراثية نادرة "
                "(عوز الفيبرينوجين، نقص فيبرينوجين الدم) تؤدي إلى مستويات منخفضة جداً "
                "أو غير قابلة للكشف.</li>"
                "</ul>"
                "<p>قد يطلب الطبيب اختبارات تخثر إضافية (PT، aPTT، D-dimer)، "
                "واختبارات وظائف الكبد وفحوصات تصوير بناءً على الصورة السريرية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كانت نتيجة <strong>اختبار الفيبرينوجين في الدم</strong> خارج "
                "النطاق المرجعي، فلا تقلق ولكن راجع الطبيب. لا ينبغي تأخير التقييم إذا "
                "كنت تعاني من ميل نزيفي غير مبرّر، أو كدمات سهلة، أو بطء التئام "
                "الجروح، أو تاريخ من الخثار المتكرر.</p>"
                "<p><strong>ارتفاع الفيبرينوجين</strong> مهم أيضاً في تقييم المخاطر "
                "القلبية الوعائية. يُعتبر الفيبرينوجين المرتفع بشكل مزمن عامل خطر "
                "مستقلاً لتصلب الشرايين والأحداث الخثارية. قد يوصي الطبيب بمراقبة "
                "دورية لمستويات الفيبرينوجين.</p>"
                "<p>تذكّر: <strong>مستويات الفيبرينوجين</strong> غير الطبيعية ليست "
                "تشخيصاً بحد ذاتها. سيُجري طبيبك فحوصات إضافية لتحديد السبب الكامن "
                "ووضع خطة علاج مناسبة. الاكتشاف المبكر والمتابعة المنتظمة يُحسّنان "
                "بشكل كبير نتائج العلاج في اضطرابات النزيف والتخثر على حدّ سواء.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_fibrinogen_sections_by_lang() -> dict:
    """Returns sections dict for Fibrinogen article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_fibrinogen_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Fibrinogen article (all 9 languages)."""
    return {
        "tr": [
            {"question": "Fibrinojen testi nedir?",
             "answer": "Fibrinojen testi, karaciğerde üretilen ve kan pıhtılaşmasında kritik rol oynayan fibrinojen proteininin kandaki düzeyini ölçen bir kan testidir. Aynı zamanda bir akut faz reaktanı olduğu için inflamasyon ve enfeksiyon durumlarında da değerlendirilir."},
            {"question": "Fibrinojen normal değeri kaçtır?",
             "answer": "Yetişkinlerde fibrinojen normal aralığı genellikle 200–400 mg/dL kabul edilir. Gebelikte (özellikle 3. trimesterde) 400–600 mg/dL'ye kadar yükselebilir. Kendi raporunuzdaki referans aralığına bakmalısınız."},
            {"question": "Fibrinojen düşüklüğü tehlikeli midir?",
             "answer": "Evet, düşük fibrinojen ciddi kanama riskini artırabilir. Özellikle 100 mg/dL'nin altındaki değerler kritik kabul edilir ve DIC, karaciğer yetmezliği veya konjenital eksiklik gibi durumları düşündürebilir. Acil tıbbi değerlendirme gerektirir."},
        ],
        "en": [
            {"question": "What is a fibrinogen test?",
             "answer": "A fibrinogen test measures the blood level of fibrinogen, a protein produced by the liver that is essential for blood clot formation. Because fibrinogen is also an acute-phase reactant, the test is used to assess both clotting function and inflammation."},
            {"question": "What is the normal fibrinogen range?",
             "answer": "The generally accepted fibrinogen normal range for adults is 200–400 mg/dL. During pregnancy, especially in the third trimester, levels can rise to 400–600 mg/dL. Always compare your result with the reference range on your own report."},
            {"question": "Is low fibrinogen dangerous?",
             "answer": "Yes, low fibrinogen can increase the risk of serious bleeding. Levels below 100 mg/dL are considered critical and may suggest DIC, liver failure or congenital deficiency. Urgent medical evaluation is required."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de fibrinógeno?",
             "answer": "La prueba de fibrinógeno mide el nivel sanguíneo de fibrinógeno, una proteína producida por el hígado esencial para la formación de coágulos. Como el fibrinógeno también es un reactante de fase aguda, la prueba sirve para evaluar la coagulación y la inflamación."},
            {"question": "¿Cuál es el rango normal de fibrinógeno?",
             "answer": "El rango normal de fibrinógeno para adultos generalmente aceptado es de 200–400 mg/dL. Durante el embarazo, especialmente en el tercer trimestre, los niveles pueden llegar a 400–600 mg/dL. Compare siempre su resultado con el rango de referencia de su informe."},
            {"question": "¿Es peligroso el fibrinógeno bajo?",
             "answer": "Sí, el fibrinógeno bajo puede aumentar el riesgo de sangrado grave. Niveles por debajo de 100 mg/dL se consideran críticos y pueden sugerir CID, insuficiencia hepática o déficit congénito. Es necesaria una evaluación médica urgente."},
        ],
        "de": [
            {"question": "Was ist ein Fibrinogen-Test?",
             "answer": "Ein Fibrinogen-Test misst den Blutspiegel von Fibrinogen, einem in der Leber produzierten Protein, das für die Blutgerinnselbildung unverzichtbar ist. Da Fibrinogen auch ein Akute-Phase-Reaktant ist, dient der Test zur Beurteilung von Gerinnung und Entzündung."},
            {"question": "Was sind die Fibrinogen-Normalwerte?",
             "answer": "Der allgemein akzeptierte Fibrinogen-Normalbereich für Erwachsene liegt bei 200–400 mg/dL. In der Schwangerschaft, besonders im dritten Trimester, können die Werte auf 400–600 mg/dL ansteigen. Vergleichen Sie Ihr Ergebnis immer mit dem Referenzbereich auf Ihrem Befund."},
            {"question": "Ist niedriges Fibrinogen gefährlich?",
             "answer": "Ja, niedrige Fibrinogenwerte können das Risiko schwerer Blutungen erhöhen. Werte unter 100 mg/dL gelten als kritisch und können auf DIC, Leberversagen oder einen angeborenen Mangel hinweisen. Eine dringende ärztliche Abklärung ist erforderlich."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test de fibrinogène ?",
             "answer": "Le test de fibrinogène mesure le taux sanguin de fibrinogène, une protéine produite par le foie indispensable à la formation de caillots. Le fibrinogène étant aussi un réactant de phase aiguë, ce test sert à évaluer la coagulation et l'inflammation."},
            {"question": "Quelles sont les valeurs normales du fibrinogène ?",
             "answer": "Les valeurs normales du fibrinogène chez l'adulte se situent généralement entre 200 et 400 mg/dL. Pendant la grossesse, surtout au troisième trimestre, les taux peuvent atteindre 400–600 mg/dL. Comparez toujours votre résultat avec l'intervalle de référence de votre rapport."},
            {"question": "Un fibrinogène bas est-il dangereux ?",
             "answer": "Oui, un fibrinogène bas peut augmenter le risque de saignement grave. Des taux inférieurs à 100 mg/dL sont considérés critiques et peuvent évoquer une CIVD, une insuffisance hépatique ou un déficit congénital. Une évaluation médicale urgente est nécessaire."},
        ],
        "it": [
            {"question": "Cos'è il test del fibrinogeno?",
             "answer": "Il test del fibrinogeno misura il livello ematico del fibrinogeno, una proteina prodotta dal fegato indispensabile per la formazione dei coaguli. Essendo anche un reagente di fase acuta, il test serve a valutare sia la coagulazione sia l'infiammazione."},
            {"question": "Quali sono i valori normali del fibrinogeno?",
             "answer": "L'intervallo normale del fibrinogeno per gli adulti è generalmente compreso tra 200 e 400 mg/dL. In gravidanza, specialmente nel terzo trimestre, i livelli possono raggiungere 400–600 mg/dL. Confrontate sempre il risultato con l'intervallo di riferimento del vostro referto."},
            {"question": "Il fibrinogeno basso è pericoloso?",
             "answer": "Sì, il fibrinogeno basso può aumentare il rischio di sanguinamento grave. Livelli inferiori a 100 mg/dL sono considerati critici e possono suggerire CID, insufficienza epatica o deficit congenito. È necessaria una valutazione medica urgente."},
        ],
        "he": [
            {"question": "מהי בדיקת פיברינוגן?",
             "answer": "בדיקת פיברינוגן מודדת את רמת הפיברינוגן בדם — חלבון המיוצר בכבד וחיוני ליצירת קרישי דם. מכיוון שפיברינוגן הוא גם חלבון שלב חריף, הבדיקה משמשת להערכת תפקוד הקרישה והדלקת."},
            {"question": "מהו טווח הנורמה של פיברינוגן?",
             "answer": "טווח הנורמה המקובל של פיברינוגן למבוגרים הוא 200–400 mg/dL. בהריון, במיוחד בטרימסטר השלישי, הרמות עשויות לעלות ל-400–600 mg/dL. השוו תמיד את התוצאה שלכם לטווח הייחוס בדוח שלכם."},
            {"question": "האם פיברינוגן נמוך מסוכן?",
             "answer": "כן, פיברינוגן נמוך עלול להגביר את הסיכון לדימום חמור. רמות מתחת ל-100 mg/dL נחשבות קריטיות ועשויות להצביע על DIC, אי-ספיקת כבד או חסר מולד. נדרשת הערכה רפואית דחופה."},
        ],
        "hi": [
            {"question": "फाइब्रिनोजन टेस्ट क्या है?",
             "answer": "फाइब्रिनोजन टेस्ट रक्त में फाइब्रिनोजन के स्तर को मापता है — यह लिवर द्वारा निर्मित एक प्रोटीन है जो रक्त के थक्के बनने के लिए आवश्यक है। चूँकि फाइब्रिनोजन एक एक्यूट-फेज़ रिएक्टेंट भी है, इसलिए यह टेस्ट क्लॉटिंग और इन्फ़्लेमेशन दोनों के मूल्यांकन के लिए किया जाता है।"},
            {"question": "फाइब्रिनोजन की नॉर्मल रेंज क्या है?",
             "answer": "वयस्कों के लिए फाइब्रिनोजन की सामान्य रूप से स्वीकृत नॉर्मल रेंज 200–400 mg/dL है। गर्भावस्था में, विशेषकर तीसरी तिमाही में, स्तर 400–600 mg/dL तक बढ़ सकता है। अपनी रिपोर्ट पर छपी रेफ़रेंस रेंज से हमेशा तुलना करें।"},
            {"question": "क्या लो फाइब्रिनोजन खतरनाक है?",
             "answer": "हाँ, लो फाइब्रिनोजन से गंभीर ब्लीडिंग का जोखिम बढ़ सकता है। 100 mg/dL से नीचे का स्तर गंभीर माना जाता है और यह DIC, लिवर फ़ेल्योर या जन्मजात कमी का संकेत हो सकता है। तत्काल चिकित्सा मूल्यांकन आवश्यक है।"},
        ],
        "ar": [
            {"question": "ما هو اختبار الفيبرينوجين؟",
             "answer": "اختبار الفيبرينوجين يقيس مستوى الفيبرينوجين في الدم — وهو بروتين يُنتَج في الكبد وضروري لتكوين الخثرات الدموية. ولأن الفيبرينوجين أيضاً مُتفاعل طور حاد، يُستخدم هذا الاختبار لتقييم وظيفة التخثر والالتهاب معاً."},
            {"question": "ما هو المعدل الطبيعي للفيبرينوجين؟",
             "answer": "المعدل الطبيعي المقبول عموماً للفيبرينوجين عند البالغين هو 200–400 mg/dL. خلال الحمل، خاصةً في الثلث الثالث، قد ترتفع المستويات إلى 400–600 mg/dL. قارن دائماً نتيجتك بالنطاق المرجعي المطبوع في تقريرك."},
            {"question": "هل انخفاض الفيبرينوجين خطير؟",
             "answer": "نعم، يمكن أن يزيد انخفاض الفيبرينوجين من خطر النزيف الحاد. تُعتبر المستويات الأقل من 100 mg/dL حرجة وقد تشير إلى DIC أو فشل كبدي أو نقص خلقي. يلزم تقييم طبي عاجل."},
        ],
    }
