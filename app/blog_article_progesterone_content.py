# -*- coding: utf-8 -*-
"""
Progesterone blog article — full body content for all 9 languages.
Used by blog_i18n._article_progesterone().
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
            heading="Progesteron kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>progesteron</strong> değerini gördüğünüzde bu hormonun "
                "ne anlama geldiğini merak etmeniz doğaldır. Progesteron, yumurtalıklardaki korpus luteum "
                "tarafından üretilen ve menstrüel döngüyü, ovülasyonu ve gebeliği düzenleyen başlıca steroid "
                "hormonlardan biridir. <strong>Progesteron testi</strong>, özellikle fertilite değerlendirmesi, "
                "luteal faz yeterliliği ve erken gebelik takibinde sıklıkla istenen bir tetkiktir.</p>"
                "<p>Bu rehber <strong>progesteron kan testi</strong> sonuçlarını nasıl yorumlayacağınızı, "
                "<strong>progesteron normal değeri</strong> aralıklarını, <strong>düşük progesteron</strong> "
                "veya yüksek progesteron nedenlerini ve ne zaman doktora başvurmanız gerektiğini sade bir "
                "dille açıklamayı amaçlıyor. Amacımız teşhis koymak değil; sonuçlarınızı anlayarak "
                "hekiminizle verimli bir görüşme yapmanıza yardımcı olmaktır.</p>"
                "<p><strong>Hamilelikte progesteron</strong> düzeyi fizyolojik olarak önemli ölçüde yükselir "
                "ve endometriyumun gebeliği desteklemesi, uterus kasılmalarının baskılanması ve plasentanın "
                "sağlıklı gelişimi için kritik rol oynar. Progesteron yetersizliği erken gebelik kaybı, "
                "luteal faz defekti ve infertilite ile ilişkilendirilebilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Progesteron normal değerleri (referans aralıkları)",
            body_html=(
                "<p><strong>Progesteron seviyeleri</strong> menstrüel döngünün fazına, gebelik durumuna, "
                "cinsiyete ve yaşa göre önemli ölçüde değişir. Aşağıdaki tablo yaygın olarak kabul edilen "
                "referans aralıklarını özetlemektedir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Dönem / Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Foliküler faz</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Luteal faz</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1. Trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">2. Trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">3. Trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Menopoz sonrası</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,5</td></tr>'
                "</tbody></table>"
                "<p>Luteal fazda <strong>progesteron normal değeri</strong> genellikle 5&nbsp;ng/mL üzerinde "
                "beklenir; ovülasyonun gerçekleştiğini doğrulamak için siklusun 21.&nbsp;gününde (ya da "
                "beklenen adet tarihinden 7&nbsp;gün önce) alınan kan örneği değerlendirilir. "
                "10&nbsp;ng/mL&rsquo;nin altındaki luteal faz değerleri luteal faz defekti şüphesi uyandırabilir.</p>"
                "<p>Laboratuvarlar arasında küçük farklılıklar olabileceğinden sonucunuzu mutlaka kendi "
                "laboratuvarınızın referans aralığıyla karşılaştırmanız önemlidir. Gebelikte progesteron "
                "trimester ilerledikçe yükselir ve üçüncü trimesterde en yüksek düzeye ulaşır.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Progesteron düşüklüğü veya yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Düşük progesteron</strong> çeşitli nedenlerden kaynaklanabilir ve özellikle "
                "fertilite ile erken gebelik açısından önemlidir. En sık karşılaşılan nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Anovülasyon:</strong> Ovülasyon gerçekleşmediğinde korpus luteum oluşmaz ve "
                "progesteron üretimi yetersiz kalır. Polikistik over sendromu (PKOS) en sık anovülasyon "
                "nedenidir.</li>"
                "<li><strong>Luteal faz defekti:</strong> Korpus luteum yeterli progesteron üretememesi "
                "sonucunda endometriyum implantasyona hazır hâle gelemez ve infertilite veya erken "
                "gebelik kaybı riski artar.</li>"
                "<li><strong>Tiroid bozuklukları:</strong> Hipotiroidizm ve hiperprolaktinemi progesteron "
                "sentezini dolaylı olarak baskılayabilir.</li>"
                "<li><strong>Aşırı egzersiz ve stres:</strong> Hipotalamik amenore yoluyla ovülasyonu "
                "baskılayabilir.</li>"
                "<li><strong>Perimenopoz:</strong> Menopoza geçiş döneminde ovülasyon sıklığı azalır ve "
                "progesteron düzeyi düşer.</li>"
                "</ul>"
                "<p>Yüksek progesteron ise genellikle fizyolojik bir durum olup en sık <strong>gebelikte</strong> "
                "görülür. Patolojik nedenler arasında konjenital adrenal hiperplazi, over kistleri, adrenal "
                "tümörler ve mol gebelik sayılabilir.</p>"
                "<p>Progesteron düzeyini değerlendirirken menstrüel döngünün hangi gününde kan alındığı "
                "kritik öneme sahiptir; foliküler fazda alınan düşük bir değer normal kabul edilirken, "
                "luteal fazda aynı değer klinik olarak anlamlı olabilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda bir kadın doğum uzmanı veya endokrinologa başvurmanız önerilir:</p>"
                "<ul>"
                "<li>Düzensiz veya ağrılı adet döngüleri, anovülasyon şüphesi</li>"
                "<li>Bir yılı aşkın süredir gebe kalamama (infertilite)</li>"
                "<li>Tekrarlayan erken gebelik kayıpları</li>"
                "<li>Luteal faz kısalığı (adet kanaması ovülasyondan &lt;10&nbsp;gün sonra başlıyorsa)</li>"
                "<li>Hamileliğin erken haftalarında lekelenme ve karın ağrısı</li>"
                "</ul>"
                "<p>Hekiminiz <strong>progesteron kan testi</strong> yanında LH, FSH, östradiol, tiroid "
                "paneli ve gerekirse pelvik ultrason isteyerek kapsamlı bir değerlendirme yapacaktır. "
                "Düşük progesteron tanısı konulduğunda oral veya vajinal progesteron takviyesi, "
                "ovülasyon indüksiyonu veya altta yatan nedenin tedavisi planlanabilir.</p>"
                "<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi teşhis veya tedavi yerine "
                "geçmez.</strong> Tahlil sonuçlarınızı mutlaka bir sağlık profesyoneli ile değerlendirin. "
                'NoryaAI tıbbi danışmanlık yerine geçmez. <a href="/analyze">Analiz sayfamızı ziyaret '
                "ederek</a> sonuçlarınız hakkında ön bilgi edinebilirsiniz.</p>"
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
            heading="Progesterone blood test: what your results mean",
            body_html=(
                "<p>When your lab report shows a <strong>progesterone</strong> value, understanding what this "
                "hormone does and why its level matters can feel overwhelming. Progesterone is a steroid hormone "
                "produced primarily by the corpus luteum in the ovaries after ovulation. It plays a central role "
                "in regulating the menstrual cycle, preparing the endometrium for implantation, and maintaining "
                "early pregnancy. A <strong>progesterone test</strong> is one of the most commonly ordered "
                "hormone tests in fertility work-ups and pregnancy monitoring.</p>"
                "<p>This guide explains how to interpret your <strong>progesterone blood test</strong> results, "
                "what constitutes normal <strong>progesterone levels</strong>, common causes of "
                "<strong>low progesterone</strong> or elevated values, and when to consult a doctor. "
                "Our goal is educational&mdash;not diagnostic. Always discuss your results with a qualified "
                "healthcare professional.</p>"
                "<p><strong>Progesterone in pregnancy</strong> rises dramatically as the placenta takes over "
                "production from the corpus luteum around weeks 8&ndash;10. Adequate progesterone is essential "
                "for suppressing uterine contractions, supporting placental development, and sustaining the "
                "pregnancy to term. Insufficient levels in early pregnancy have been associated with threatened "
                "miscarriage and luteal phase deficiency.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Progesterone normal range by cycle phase and trimester",
            body_html=(
                "<p><strong>Progesterone levels</strong> vary significantly depending on the phase of the "
                "menstrual cycle, pregnancy status, sex, and age. The table below summarises widely accepted "
                "reference ranges for a <strong>progesterone blood test</strong>:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Phase / Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Follicular phase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Luteal phase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1st trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">2nd trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">3rd trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Post-menopausal</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Males</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.5</td></tr>'
                "</tbody></table>"
                "<p>To confirm ovulation, a blood sample is typically drawn on cycle day 21 (or 7 days before "
                "the expected period). A mid-luteal <strong>progesterone level</strong> above 5&nbsp;ng/mL "
                "generally indicates that ovulation occurred, while values below 10&nbsp;ng/mL may suggest "
                "a luteal phase defect. <strong>Progesterone levels by week</strong> rise steadily throughout "
                "pregnancy, peaking in the third trimester.</p>"
                "<p>Reference ranges can vary between laboratories, so always compare your result with the "
                "specific range printed on your report. Timing of the blood draw relative to ovulation is "
                "critical for accurate interpretation.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of low or high progesterone",
            body_html=(
                "<p><strong>Low progesterone</strong> is particularly significant for fertility and early "
                "pregnancy outcomes. The most common causes include:</p>"
                "<ul>"
                "<li><strong>Anovulation:</strong> Without ovulation, no corpus luteum forms, so progesterone "
                "remains at follicular-phase levels. Polycystic ovary syndrome (PCOS) is the leading cause "
                "of chronic anovulation.</li>"
                "<li><strong>Luteal phase defect:</strong> The corpus luteum produces insufficient progesterone, "
                "leaving the endometrium inadequately prepared for implantation. This can contribute to "
                "infertility or recurrent early pregnancy loss.</li>"
                "<li><strong>Thyroid disorders:</strong> Hypothyroidism and hyperprolactinaemia can indirectly "
                "suppress progesterone production by disrupting the HPG axis.</li>"
                "<li><strong>Excessive exercise and chronic stress:</strong> These may lead to hypothalamic "
                "amenorrhoea, suppressing ovulation and consequently progesterone output.</li>"
                "<li><strong>Perimenopause:</strong> As women approach menopause, ovulation becomes less "
                "frequent and progesterone levels decline.</li>"
                "</ul>"
                "<p>Elevated progesterone is most commonly a physiological finding during "
                "<strong>pregnancy</strong>. Pathological causes include congenital adrenal hyperplasia (CAH), "
                "ovarian cysts, adrenal tumours, and molar pregnancy.</p>"
                "<p>When interpreting <strong>progesterone levels</strong>, the day of the menstrual cycle on "
                "which blood was drawn is crucial. A low value during the follicular phase is entirely normal, "
                "whereas the same value in the luteal phase may be clinically significant.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>Consider consulting a gynaecologist or reproductive endocrinologist if you experience:</p>"
                "<ul>"
                "<li>Irregular or painful menstrual cycles, suspected anovulation</li>"
                "<li>Inability to conceive after 12 months of unprotected intercourse (infertility)</li>"
                "<li>Recurrent early pregnancy losses</li>"
                "<li>A short luteal phase (menstruation starting &lt;10&nbsp;days after ovulation)</li>"
                "<li>Spotting and cramping in early pregnancy</li>"
                "</ul>"
                "<p>Your doctor may order a <strong>progesterone blood test</strong> alongside LH, FSH, "
                "oestradiol, thyroid panel, and possibly a pelvic ultrasound for a comprehensive evaluation. "
                "If <strong>low progesterone</strong> is confirmed, treatment options include oral or vaginal "
                "progesterone supplementation, ovulation induction, or addressing the underlying cause.</p>"
                "<p><strong>This content is for informational purposes only and does not constitute medical "
                "advice, diagnosis, or treatment.</strong> Always discuss your test results with a qualified "
                "healthcare professional. NoryaAI is not a substitute for medical consultation. "
                '<a href="/analyze">Visit our analysis page</a> for preliminary insights into your results.</p>'
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
            heading="Análisis de progesterona en sangre: ¿qué significan sus resultados?",
            body_html=(
                "<p>Cuando en su análisis de sangre aparece un valor de <strong>progesterona</strong>, es "
                "natural preguntarse qué significa. La progesterona es una hormona esteroide producida "
                "principalmente por el cuerpo lúteo en los ovarios tras la ovulación. Desempeña un papel "
                "central en la regulación del ciclo menstrual, la preparación del endometrio para la "
                "implantación y el mantenimiento del embarazo temprano. La <strong>prueba de progesterona</strong> "
                "es una de las determinaciones hormonales más solicitadas en estudios de fertilidad y "
                "seguimiento gestacional.</p>"
                "<p>Esta guía explica cómo interpretar los resultados de su análisis de progesterona en "
                "sangre, los rangos normales según la fase del ciclo y el trimestre de embarazo, las causas "
                "de <strong>progesterona baja</strong> o elevada y cuándo consultar a un médico. Nuestro "
                "objetivo es educativo, no diagnóstico; consulte siempre con un profesional sanitario.</p>"
                "<p>La <strong>progesterona en el embarazo</strong> aumenta de forma significativa a medida "
                "que la placenta asume la producción hormonal alrededor de las semanas 8&ndash;10. Unos "
                "niveles adecuados son esenciales para inhibir las contracciones uterinas, favorecer el "
                "desarrollo placentario y mantener la gestación a término.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de progesterona",
            body_html=(
                "<p>Los <strong>niveles de progesterona</strong> varían según la fase del ciclo menstrual, "
                "el estado gestacional, el sexo y la edad. La siguiente tabla resume los rangos de referencia "
                "más aceptados:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fase / Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Fase folicular</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Fase lútea</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1.er trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">2.º trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">3.er trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Posmenopausia</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,5</td></tr>'
                "</tbody></table>"
                "<p>Para confirmar la ovulación se extrae sangre el día 21 del ciclo (o 7 días antes de la "
                "fecha prevista de menstruación). Un valor lúteo superior a 5&nbsp;ng/mL indica ovulación, "
                "mientras que valores inferiores a 10&nbsp;ng/mL pueden sugerir un defecto de la fase lútea.</p>"
                "<p>Los rangos pueden variar entre laboratorios; compare siempre su resultado con el rango "
                "impreso en su informe. El momento de la extracción dentro del ciclo es fundamental para "
                "una interpretación correcta.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de progesterona baja o alta",
            body_html=(
                "<p>La <strong>progesterona baja</strong> es especialmente relevante para la fertilidad y "
                "el pronóstico del embarazo temprano. Las causas más frecuentes son:</p>"
                "<ul>"
                "<li><strong>Anovulación:</strong> Sin ovulación no se forma el cuerpo lúteo, por lo que "
                "la progesterona permanece en niveles propios de la fase folicular. El síndrome de ovario "
                "poliquístico (SOP) es la causa principal de anovulación crónica.</li>"
                "<li><strong>Defecto de fase lútea:</strong> El cuerpo lúteo produce progesterona insuficiente, "
                "lo que impide la preparación adecuada del endometrio para la implantación.</li>"
                "<li><strong>Trastornos tiroideos:</strong> El hipotiroidismo y la hiperprolactinemia pueden "
                "suprimir indirectamente la producción de progesterona.</li>"
                "<li><strong>Ejercicio excesivo y estrés crónico:</strong> Pueden provocar amenorrea "
                "hipotalámica y suprimir la ovulación.</li>"
                "<li><strong>Perimenopausia:</strong> La frecuencia de ovulación disminuye y con ella "
                "los niveles de progesterona.</li>"
                "</ul>"
                "<p>La progesterona elevada suele ser un hallazgo fisiológico durante el "
                "<strong>embarazo</strong>. Entre las causas patológicas se encuentran la hiperplasia "
                "suprarrenal congénita, los quistes ováricos, los tumores suprarrenales y el embarazo molar.</p>"
                "<p>Al evaluar la <strong>prueba de progesterona</strong>, el día del ciclo en que se extrajo "
                "la sangre resulta determinante: un valor bajo en fase folicular es normal, pero el mismo "
                "valor en fase lútea puede tener relevancia clínica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Se recomienda acudir a un ginecólogo o endocrinólogo reproductivo si presenta:</p>"
                "<ul>"
                "<li>Ciclos menstruales irregulares o dolorosos, sospecha de anovulación</li>"
                "<li>Incapacidad para concebir tras 12 meses de relaciones sin protección</li>"
                "<li>Pérdidas gestacionales recurrentes en el primer trimestre</li>"
                "<li>Fase lútea corta (menstruación &lt;10&nbsp;días después de la ovulación)</li>"
                "<li>Manchado y dolor abdominal en las primeras semanas de embarazo</li>"
                "</ul>"
                "<p>Su médico podrá solicitar una <strong>prueba de progesterona</strong> junto con LH, FSH, "
                "estradiol, panel tiroideo y, si es necesario, una ecografía pélvica. Si se confirma "
                "<strong>progesterona baja</strong>, las opciones de tratamiento incluyen suplementación con "
                "progesterona oral o vaginal, inducción de la ovulación o tratamiento de la causa subyacente.</p>"
                "<p><strong>Este contenido es meramente informativo y no constituye consejo médico, "
                "diagnóstico ni tratamiento.</strong> Comente siempre sus resultados con un profesional "
                "sanitario cualificado. NoryaAI no sustituye la consulta médica. "
                '<a href="/analyze">Visite nuestra página de análisis</a> para obtener información '
                "preliminar sobre sus resultados.</p>"
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
            heading="Progesteron-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Wenn in Ihrem Laborbericht ein <strong>Progesteron</strong>-Wert auftaucht, fragen Sie "
                "sich vielleicht, was dieses Hormon bedeutet und warum es wichtig ist. Progesteron ist ein "
                "Steroidhormon, das hauptsächlich vom Gelbkörper (Corpus luteum) in den Eierstöcken nach dem "
                "Eisprung produziert wird. Es spielt eine zentrale Rolle bei der Regulierung des "
                "Menstruationszyklus, der Vorbereitung der Gebärmutterschleimhaut auf die Einnistung und der "
                "Aufrechterhaltung einer frühen Schwangerschaft. Ein <strong>Progesteron-Test</strong> gehört "
                "zu den am häufigsten angeordneten Hormonuntersuchungen bei Fertilitätsabklärungen und in der "
                "Schwangerschaftsüberwachung.</p>"
                "<p>Dieser Leitfaden erklärt, wie Sie Ihre Progesteron-Blutwerte interpretieren, welche "
                "Referenzbereiche als normal gelten, was die Ursachen für einen "
                "<strong>niedrigen Progesteronspiegel</strong> oder erhöhte Werte sind und wann Sie einen "
                "Arzt aufsuchen sollten. Unser Ziel ist die Aufklärung&mdash;keine Diagnosestellung. "
                "Besprechen Sie Ihre Ergebnisse stets mit einem qualifizierten Arzt.</p>"
                "<p><strong>Progesteron in der Schwangerschaft</strong> steigt deutlich an, sobald die "
                "Plazenta ab etwa der 8.&ndash;10.&nbsp;Woche die Hormonproduktion vom Gelbkörper übernimmt. "
                "Ausreichende Progesteronspiegel sind entscheidend, um Uteruskontraktionen zu unterdrücken, "
                "die Plazentaentwicklung zu fördern und die Schwangerschaft aufrechtzuerhalten.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Progesteron-Normalwerte nach Zyklusphase und Trimester",
            body_html=(
                "<p>Die <strong>Progesteronwerte</strong> schwanken erheblich je nach Zyklusphase, "
                "Schwangerschaftsstatus, Geschlecht und Alter. Die folgende Tabelle fasst die gängigen "
                "Referenzbereiche zusammen:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Phase / Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Follikelphase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Lutealphase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1. Trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">2. Trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">3. Trimester</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Postmenopause</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,5</td></tr>'
                "</tbody></table>"
                "<p>Zur Bestätigung des Eisprungs wird die Blutprobe am 21.&nbsp;Zyklustag (bzw. 7&nbsp;Tage "
                "vor der erwarteten Periode) entnommen. Ein mittlutealer Progesteronwert über 5&nbsp;ng/mL "
                "spricht für eine stattgefundene Ovulation, während Werte unter 10&nbsp;ng/mL auf einen "
                "Lutealphasendefekt hindeuten können.</p>"
                "<p>Referenzbereiche können zwischen Laboren variieren; vergleichen Sie Ihr Ergebnis immer "
                "mit dem Bereich auf Ihrem Laborbericht. Der Zeitpunkt der Blutentnahme im Zyklus ist "
                "entscheidend für eine korrekte Interpretation.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für niedrigen oder hohen Progesteronspiegel",
            body_html=(
                "<p>Ein <strong>niedriger Progesteronspiegel</strong> ist besonders für die Fruchtbarkeit und "
                "den Verlauf einer frühen Schwangerschaft bedeutsam. Die häufigsten Ursachen sind:</p>"
                "<ul>"
                "<li><strong>Anovulation:</strong> Ohne Eisprung bildet sich kein Gelbkörper, und die "
                "Progesteronproduktion bleibt auf Follikelphasenniveau. Das polyzystische Ovarialsyndrom "
                "(PCOS) ist die häufigste Ursache chronischer Anovulation.</li>"
                "<li><strong>Lutealphasendefekt:</strong> Der Gelbkörper produziert nicht genügend "
                "Progesteron, sodass das Endometrium unzureichend auf die Einnistung vorbereitet ist.</li>"
                "<li><strong>Schilddrüsenstörungen:</strong> Hypothyreose und Hyperprolaktinämie können die "
                "Progesteronproduktion indirekt hemmen.</li>"
                "<li><strong>Übermäßige Belastung und chronischer Stress:</strong> Können zu hypothalamischer "
                "Amenorrhö führen und die Ovulation unterdrücken.</li>"
                "<li><strong>Perimenopause:</strong> Mit zunehmendem Alter nimmt die Ovulationshäufigkeit ab "
                "und der Progesteronspiegel sinkt.</li>"
                "</ul>"
                "<p>Erhöhtes Progesteron ist meist ein physiologischer Befund in der "
                "<strong>Schwangerschaft</strong>. Pathologische Ursachen umfassen kongenitale "
                "Nebennierenhyperplasie (AGS), Ovarialzysten, Nebennierentumoren und Blasenmole.</p>"
                "<p>Bei der Interpretation eines <strong>Progesteron-Tests</strong> ist der Zyklustag der "
                "Blutentnahme entscheidend: Ein niedriger Wert in der Follikelphase ist völlig normal, "
                "derselbe Wert in der Lutealphase kann dagegen klinisch relevant sein.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Ein Besuch beim Gynäkologen oder reproduktiven Endokrinologen wird empfohlen, wenn Sie:</p>"
                "<ul>"
                "<li>Unregelmäßige oder schmerzhafte Menstruationszyklen haben, Verdacht auf Anovulation</li>"
                "<li>Seit mehr als 12 Monaten trotz ungeschütztem Verkehr nicht schwanger werden</li>"
                "<li>Wiederholte Fehlgeburten im ersten Trimester erlitten haben</li>"
                "<li>Eine kurze Lutealphase haben (Menstruation &lt;10&nbsp;Tage nach Eisprung)</li>"
                "<li>Schmierblutungen und Unterleibsschmerzen in der Frühschwangerschaft bemerken</li>"
                "</ul>"
                "<p>Ihr Arzt kann neben einem <strong>Progesteron-Test</strong> auch LH, FSH, Östradiol, ein "
                "Schilddrüsenpanel und ggf. einen Beckenultraschall anordnen. Bei bestätigtem "
                "<strong>niedrigem Progesteronspiegel</strong> umfassen die Behandlungsoptionen orale oder "
                "vaginale Progesteronsupplementierung, Ovulationsinduktion oder Therapie der Grundursache.</p>"
                "<p><strong>Dieser Inhalt dient ausschließlich der Information und stellt keine ärztliche "
                "Beratung, Diagnose oder Behandlung dar.</strong> Besprechen Sie Ihre Ergebnisse immer mit "
                "einem qualifizierten Arzt. NoryaAI ersetzt keine ärztliche Beratung. "
                '<a href="/analyze">Besuchen Sie unsere Analyseseite</a> für erste Einblicke in Ihre '
                "Ergebnisse.</p>"
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
            heading="Test de progestérone : que signifient vos résultats ?",
            body_html=(
                "<p>Lorsque votre bilan sanguin affiche une valeur de <strong>progestérone</strong>, il est "
                "naturel de se demander ce que cette hormone signifie. La progestérone est une hormone "
                "stéroïde produite principalement par le corps jaune dans les ovaires après l'ovulation. "
                "Elle joue un rôle central dans la régulation du cycle menstruel, la préparation de "
                "l'endomètre à l'implantation et le maintien de la grossesse précoce. Le "
                "<strong>test de progestérone</strong> est l'un des dosages hormonaux les plus fréquemment "
                "prescrits dans les bilans de fertilité et le suivi de grossesse.</p>"
                "<p>Ce guide explique comment interpréter les résultats de votre prise de sang de "
                "progestérone, les valeurs normales selon la phase du cycle et le trimestre, les causes "
                "d'une <strong>progestérone basse</strong> ou élevée et quand consulter un médecin. "
                "Notre objectif est éducatif et non diagnostique ; discutez toujours de vos résultats "
                "avec un professionnel de santé qualifié.</p>"
                "<p>La <strong>progestérone pendant la grossesse</strong> augmente considérablement lorsque "
                "le placenta prend le relais du corps jaune vers la 8<sup>e</sup>&ndash;10<sup>e</sup>&nbsp;semaine. "
                "Des taux adéquats sont essentiels pour inhiber les contractions utérines, soutenir le "
                "développement placentaire et mener la grossesse à terme.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de progestérone",
            body_html=(
                "<p>Les <strong>taux de progestérone</strong> varient considérablement en fonction de la "
                "phase du cycle menstruel, du statut gestationnel, du sexe et de l'âge. Le tableau suivant "
                "résume les plages de référence couramment admises :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Phase / Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Plage normale (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Phase folliculaire</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Phase lutéale</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1<sup>er</sup> trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">2<sup>e</sup> trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">3<sup>e</sup> trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Post-ménopause</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,5</td></tr>'
                "</tbody></table>"
                "<p>Pour confirmer l'ovulation, le prélèvement est effectué au 21<sup>e</sup>&nbsp;jour du "
                "cycle (ou 7&nbsp;jours avant la date prévue des règles). Un taux mi-lutéal supérieur à "
                "5&nbsp;ng/mL indique généralement qu'une ovulation a eu lieu, tandis que des valeurs "
                "inférieures à 10&nbsp;ng/mL peuvent évoquer un déficit de la phase lutéale.</p>"
                "<p>Les plages de référence peuvent varier selon les laboratoires ; comparez toujours votre "
                "résultat avec la plage indiquée sur votre compte rendu. Le moment du prélèvement dans le "
                "cycle est déterminant pour une interprétation correcte.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une progestérone basse ou élevée",
            body_html=(
                "<p>Une <strong>progestérone basse</strong> revêt une importance particulière pour la "
                "fertilité et le pronostic de la grossesse précoce. Les causes les plus fréquentes sont :</p>"
                "<ul>"
                "<li><strong>Anovulation :</strong> En l'absence d'ovulation, le corps jaune ne se forme pas "
                "et la progestérone reste à des niveaux folliculaires. Le syndrome des ovaires polykystiques "
                "(SOPK) est la principale cause d'anovulation chronique.</li>"
                "<li><strong>Insuffisance lutéale :</strong> Le corps jaune ne produit pas suffisamment de "
                "progestérone, empêchant la préparation adéquate de l'endomètre pour l'implantation.</li>"
                "<li><strong>Troubles thyroïdiens :</strong> L'hypothyroïdie et l'hyperprolactinémie "
                "peuvent inhiber indirectement la production de progestérone.</li>"
                "<li><strong>Exercice excessif et stress chronique :</strong> Peuvent entraîner une "
                "aménorrhée hypothalamique et supprimer l'ovulation.</li>"
                "<li><strong>Périménopause :</strong> La fréquence des ovulations diminue progressivement, "
                "entraînant une baisse de la progestérone.</li>"
                "</ul>"
                "<p>Une progestérone élevée est le plus souvent un constat physiologique de "
                "<strong>grossesse</strong>. Les causes pathologiques incluent l'hyperplasie congénitale "
                "des surrénales, les kystes ovariens, les tumeurs surrénaliennes et la grossesse molaire.</p>"
                "<p>Lors de l'interprétation d'un <strong>test de progestérone</strong>, le jour du cycle "
                "auquel le prélèvement a été effectué est déterminant : une valeur basse en phase "
                "folliculaire est tout à fait normale, alors que la même valeur en phase lutéale peut "
                "être cliniquement significative.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Il est recommandé de consulter un gynécologue ou un endocrinologue de la reproduction "
                "si vous présentez :</p>"
                "<ul>"
                "<li>Des cycles menstruels irréguliers ou douloureux, suspicion d'anovulation</li>"
                "<li>Une impossibilité de concevoir après 12 mois de rapports non protégés</li>"
                "<li>Des fausses couches récurrentes au premier trimestre</li>"
                "<li>Une phase lutéale courte (règles &lt;10&nbsp;jours après l'ovulation)</li>"
                "<li>Des saignements et des douleurs abdominales en début de grossesse</li>"
                "</ul>"
                "<p>Votre médecin pourra prescrire un <strong>test de progestérone</strong> associé à la LH, "
                "la FSH, l'œstradiol, un bilan thyroïdien et éventuellement une échographie pelvienne. "
                "Si une <strong>progestérone basse</strong> est confirmée, les options thérapeutiques "
                "comprennent la supplémentation en progestérone orale ou vaginale, l'induction de "
                "l'ovulation ou le traitement de la cause sous-jacente.</p>"
                "<p><strong>Ce contenu est fourni à titre informatif uniquement et ne constitue pas un "
                "avis médical, un diagnostic ni un traitement.</strong> Discutez toujours de vos résultats "
                "avec un professionnel de santé qualifié. NoryaAI ne remplace pas une consultation médicale. "
                '<a href="/analyze">Visitez notre page d\'analyse</a> pour obtenir des informations '
                "préliminaires sur vos résultats.</p>"
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
            heading="Test del progesterone: cosa significano i risultati",
            body_html=(
                "<p>Quando nel referto delle analisi del sangue compare un valore di "
                "<strong>progesterone</strong>, è naturale chiedersi che cosa significhi. Il progesterone è "
                "un ormone steroideo prodotto principalmente dal corpo luteo nelle ovaie dopo l'ovulazione. "
                "Svolge un ruolo centrale nella regolazione del ciclo mestruale, nella preparazione "
                "dell'endometrio all'impianto e nel mantenimento della gravidanza iniziale. Il "
                "<strong>test del progesterone</strong> è uno dei dosaggi ormonali più richiesti negli "
                "accertamenti di fertilità e nel monitoraggio gestazionale.</p>"
                "<p>Questa guida spiega come interpretare i risultati dell'esame del sangue del progesterone, "
                "i valori normali per fase del ciclo e trimestre, le cause di "
                "<strong>progesterone basso</strong> o elevato e quando rivolgersi al medico. L'obiettivo è "
                "educativo, non diagnostico; discutete sempre i risultati con un professionista sanitario.</p>"
                "<p>Il <strong>progesterone in gravidanza</strong> aumenta in modo significativo quando la "
                "placenta subentra nella produzione ormonale intorno alla 8<sup>a</sup>&ndash;10<sup>a</sup>&nbsp;settimana. "
                "Livelli adeguati sono essenziali per inibire le contrazioni uterine, sostenere lo sviluppo "
                "placentare e portare la gravidanza a termine.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del progesterone",
            body_html=(
                "<p>I <strong>livelli di progesterone</strong> variano notevolmente in base alla fase del "
                "ciclo mestruale, allo stato gestazionale, al sesso e all'età. La tabella seguente riassume "
                "gli intervalli di riferimento più diffusi:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fase / Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Fase follicolare</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Fase luteale</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1° trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">2° trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">3° trimestre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Post-menopausa</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1 – 0,5</td></tr>'
                "</tbody></table>"
                "<p>Per confermare l'ovulazione il prelievo viene effettuato al 21°&nbsp;giorno del ciclo "
                "(o 7&nbsp;giorni prima della data prevista delle mestruazioni). Un valore medio-luteale "
                "superiore a 5&nbsp;ng/mL indica generalmente che l'ovulazione è avvenuta, mentre valori "
                "inferiori a 10&nbsp;ng/mL possono suggerire un difetto della fase luteale.</p>"
                "<p>Gli intervalli di riferimento possono variare tra laboratori; confrontate sempre il "
                "vostro risultato con l'intervallo riportato sul vostro referto. Il momento del prelievo "
                "nel ciclo è fondamentale per un'interpretazione corretta.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di progesterone basso o alto",
            body_html=(
                "<p>Il <strong>progesterone basso</strong> è particolarmente rilevante per la fertilità e "
                "l'esito della gravidanza iniziale. Le cause più comuni includono:</p>"
                "<ul>"
                "<li><strong>Anovulazione:</strong> Senza ovulazione non si forma il corpo luteo e il "
                "progesterone rimane ai livelli della fase follicolare. La sindrome dell'ovaio policistico "
                "(PCOS) è la causa principale di anovulazione cronica.</li>"
                "<li><strong>Difetto della fase luteale:</strong> Il corpo luteo produce progesterone "
                "insufficiente, impedendo un'adeguata preparazione dell'endometrio per l'impianto.</li>"
                "<li><strong>Disturbi tiroidei:</strong> L'ipotiroidismo e l'iperprolattinemia possono "
                "inibire indirettamente la produzione di progesterone.</li>"
                "<li><strong>Esercizio eccessivo e stress cronico:</strong> Possono portare ad amenorrea "
                "ipotalamica e sopprimere l'ovulazione.</li>"
                "<li><strong>Perimenopausa:</strong> Con l'avvicinarsi della menopausa, la frequenza "
                "dell'ovulazione diminuisce e i livelli di progesterone calano.</li>"
                "</ul>"
                "<p>Il progesterone elevato è nella maggior parte dei casi un riscontro fisiologico in "
                "<strong>gravidanza</strong>. Cause patologiche comprendono iperplasia surrenalica "
                "congenita, cisti ovariche, tumori surrenalici e mola idatiforme.</p>"
                "<p>Nell'interpretazione del <strong>test del progesterone</strong>, il giorno del ciclo "
                "in cui è stato effettuato il prelievo è determinante: un valore basso in fase follicolare "
                "è del tutto normale, mentre lo stesso valore in fase luteale può avere significato clinico.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Si consiglia di consultare un ginecologo o un endocrinologo della riproduzione se:</p>"
                "<ul>"
                "<li>Cicli mestruali irregolari o dolorosi, sospetto di anovulazione</li>"
                "<li>Impossibilità di concepire dopo 12 mesi di rapporti non protetti</li>"
                "<li>Aborti spontanei ricorrenti nel primo trimestre</li>"
                "<li>Fase luteale breve (mestruazione &lt;10&nbsp;giorni dopo l'ovulazione)</li>"
                "<li>Spotting e dolori addominali nelle prime settimane di gravidanza</li>"
                "</ul>"
                "<p>Il medico potrà prescrivere un <strong>test del progesterone</strong> insieme a LH, FSH, "
                "estradiolo, pannello tiroideo ed eventualmente un'ecografia pelvica. Se viene confermato un "
                "<strong>progesterone basso</strong>, le opzioni terapeutiche comprendono supplementazione "
                "con progesterone orale o vaginale, induzione dell'ovulazione o trattamento della causa "
                "sottostante.</p>"
                "<p><strong>Questo contenuto ha finalità esclusivamente informative e non costituisce "
                "consulenza medica, diagnosi né trattamento.</strong> Discutete sempre i vostri risultati "
                "con un professionista sanitario qualificato. NoryaAI non sostituisce il consulto medico. "
                '<a href="/analyze">Visitate la nostra pagina di analisi</a> per informazioni '
                "preliminari sui vostri risultati.</p>"
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
            heading="בדיקת פרוגסטרון בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>כאשר בתוצאות בדיקת הדם שלך מופיע ערך <strong>פרוגסטרון</strong>, טבעי לתהות מה "
                "המשמעות של הורמון זה. פרוגסטרון הוא הורמון סטרואידי המיוצר בעיקר על ידי הגופיף הצהוב "
                "(Corpus Luteum) בשחלות לאחר הביוץ. הוא ממלא תפקיד מרכזי בוויסות המחזור החודשי, "
                "בהכנת רירית הרחם להשתלת העובר ובשמירה על הריון מוקדם. <strong>בדיקת פרוגסטרון</strong> "
                "היא אחד מבדיקות ההורמונים הנפוצות ביותר בהערכות פוריות ובמעקב הריון.</p>"
                "<p>מדריך זה מסביר כיצד לפרש את תוצאות בדיקת הפרוגסטרון בדם, מהם טווחי הנורמה לפי שלב "
                "המחזור ושליש ההריון, מהם הגורמים ל<strong>פרוגסטרון נמוך</strong> או גבוה ומתי יש לפנות "
                "לרופא. המטרה שלנו חינוכית ולא אבחנתית; יש לדון תמיד בתוצאות עם רופא מוסמך.</p>"
                "<p><strong>פרוגסטרון בהריון</strong> עולה באופן משמעותי כאשר השליה משתלטת על ייצור "
                "ההורמון סביב שבועות 8&ndash;10. רמות מספקות חיוניות לדיכוי התכווצויות רחם, לתמיכה "
                "בהתפתחות השליה ולשמירה על ההריון עד ללידה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי נורמה של פרוגסטרון",
            body_html=(
                "<p>רמות <strong>פרוגסטרון</strong> משתנות באופן משמעותי בהתאם לשלב במחזור החודשי, "
                "מצב ההריון, המין והגיל. הטבלה הבאה מסכמת את טווחי הייחוס המקובלים:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">שלב / קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח נורמלי (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">שלב פוליקולרי</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">שלב לוטאלי</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">שליש ראשון</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">שליש שני</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">שליש שלישי</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">לאחר גיל המעבר</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.5</td></tr>'
                "</tbody></table>"
                "<p>לאישור ביוץ, דגימת הדם נלקחת בדרך כלל ביום ה-21 למחזור (או 7 ימים לפני המחזור "
                "הצפוי). ערך פרוגסטרון אמצע-לוטאלי מעל 5&nbsp;ng/mL מצביע בדרך כלל על כך שהתרחש ביוץ, "
                "בעוד שערכים מתחת ל-10&nbsp;ng/mL עשויים לרמז על ליקוי בשלב הלוטאלי.</p>"
                "<p>טווחי ייחוס עשויים להשתנות בין מעבדות; השוו תמיד את התוצאה שלכם עם הטווח המופיע "
                "בדוח המעבדה. עיתוי לקיחת הדם ביחס לביוץ הוא קריטי לפרשנות נכונה.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לפרוגסטרון נמוך או גבוה",
            body_html=(
                "<p><strong>פרוגסטרון נמוך</strong> משמעותי במיוחד עבור פוריות ותוצאות הריון מוקדם. "
                "הגורמים הנפוצים ביותר כוללים:</p>"
                "<ul>"
                "<li><strong>אנובולציה (חוסר ביוץ):</strong> ללא ביוץ, הגופיף הצהוב לא נוצר והפרוגסטרון "
                "נשאר ברמות השלב הפוליקולרי. תסמונת השחלות הפוליציסטיות (PCOS) היא הגורם המוביל "
                "לאנובולציה כרונית.</li>"
                "<li><strong>ליקוי בשלב הלוטאלי:</strong> הגופיף הצהוב מייצר פרוגסטרון בלתי מספק, מה "
                "שמונע הכנה נאותה של רירית הרחם להשתלה.</li>"
                "<li><strong>הפרעות בבלוטת התריס:</strong> תת-פעילות של בלוטת התריס והיפרפרולקטינמיה "
                "עלולות לדכא בעקיפין את ייצור הפרוגסטרון.</li>"
                "<li><strong>פעילות גופנית מוגזמת ומתח כרוני:</strong> עלולים לגרום לאמנוריאה "
                "היפותלמית ולדכא את הביוץ.</li>"
                "<li><strong>פרימנופאוזה:</strong> עם התקרבות גיל המעבר, תדירות הביוץ יורדת ורמות "
                "הפרוגסטרון יורדות.</li>"
                "</ul>"
                "<p>פרוגסטרון גבוה הוא בדרך כלל ממצא פיזיולוגי ב<strong>הריון</strong>. גורמים פתולוגיים "
                "כוללים היפרפלזיה מולדת של יותרת הכליה, ציסטות שחלתיות, גידולי אדרנל והריון טרופובלסטי.</p>"
                "<p>בעת פירוש <strong>בדיקת פרוגסטרון</strong>, יום המחזור בו נלקחה הדגימה הוא קריטי: "
                "ערך נמוך בשלב הפוליקולרי הוא נורמלי לחלוטין, בעוד שאותו ערך בשלב הלוטאלי עשוי "
                "להיות בעל משמעות קלינית.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>מומלץ לפנות לרופא/ת נשים או אנדוקרינולוג/ית פוריות אם:</p>"
                "<ul>"
                "<li>מחזורים לא סדירים או כואבים, חשד לחוסר ביוץ</li>"
                "<li>חוסר יכולת להרות לאחר 12 חודשי ניסיון (אי-פוריות)</li>"
                "<li>הפלות חוזרות בשליש הראשון</li>"
                "<li>שלב לוטאלי קצר (מחזור מתחיל פחות מ-10 ימים אחרי ביוץ)</li>"
                "<li>דימום קל וכאבי בטן בשבועות הראשונים של הריון</li>"
                "</ul>"
                "<p>הרופא/ה עשוי/ה להפנות ל<strong>בדיקת פרוגסטרון</strong> לצד LH, FSH, אסטרדיול, "
                "בדיקות בלוטת התריס ובמידת הצורך אולטרסאונד אגני. אם מאושר "
                "<strong>פרוגסטרון נמוך</strong>, אפשרויות הטיפול כוללות תוספת פרוגסטרון אוראלי או "
                "וגינלי, השראת ביוץ או טיפול בגורם הבסיסי.</p>"
                "<p><strong>תוכן זה מיועד למטרות מידע בלבד ואינו מהווה ייעוץ רפואי, אבחנה או "
                "טיפול.</strong> דונו תמיד בתוצאות הבדיקות שלכם עם רופא/ה מוסמך/ת. "
                "NoryaAI אינו תחליף לייעוץ רפואי. "
                '<a href="/analyze">בקרו בדף הניתוח שלנו</a> לקבלת תובנות ראשוניות על התוצאות שלכם.</p>'
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
            heading="प्रोजेस्टेरोन ब्लड टेस्ट: आपके रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p>जब आपकी ब्लड रिपोर्ट में <strong>प्रोजेस्टेरोन</strong> की वैल्यू दिखती है, तो यह "
                "स्वाभाविक है कि आप जानना चाहें कि इस हार्मोन का क्या मतलब है। प्रोजेस्टेरोन एक स्टेरॉइड "
                "हार्मोन है जो मुख्य रूप से ओव्यूलेशन के बाद अंडाशय में कॉर्पस ल्यूटियम द्वारा बनाया "
                "जाता है। यह मासिक चक्र को नियंत्रित करने, एंडोमेट्रियम को इम्प्लांटेशन के लिए तैयार "
                "करने और शुरुआती गर्भावस्था को बनाए रखने में केंद्रीय भूमिका निभाता है। "
                "<strong>प्रोजेस्टेरोन टेस्ट</strong> फर्टिलिटी जाँच और प्रेगनेंसी मॉनिटरिंग में "
                "सबसे अधिक ऑर्डर किए जाने वाले हार्मोन टेस्ट में से एक है।</p>"
                "<p>यह गाइड बताती है कि अपने प्रोजेस्टेरोन ब्लड टेस्ट के रिज़ल्ट को कैसे समझें, "
                "सामान्य प्रोजेस्टेरोन लेवल क्या हैं, <strong>लो प्रोजेस्टेरोन</strong> या हाई वैल्यू "
                "के कारण क्या हैं और डॉक्टर से कब मिलें। हमारा उद्देश्य शैक्षिक है, डायग्नोस्टिक नहीं; "
                "अपने रिज़ल्ट हमेशा किसी योग्य हेल्थकेयर प्रोफ़ेशनल से चर्चा करें।</p>"
                "<p><strong>प्रेगनेंसी में प्रोजेस्टेरोन</strong> का स्तर तेज़ी से बढ़ता है जब लगभग "
                "8&ndash;10 सप्ताह में प्लेसेंटा कॉर्पस ल्यूटियम से हार्मोन प्रोडक्शन की ज़िम्मेदारी "
                "लेता है। पर्याप्त प्रोजेस्टेरोन गर्भाशय के संकुचन को दबाने, प्लेसेंटा के विकास में "
                "सहायता करने और गर्भावस्था को पूर्ण अवधि तक बनाए रखने के लिए आवश्यक है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="प्रोजेस्टेरोन के सामान्य मान (रेफ़रेंस रेंज)",
            body_html=(
                "<p><strong>प्रोजेस्टेरोन लेवल</strong> मासिक चक्र के चरण, गर्भावस्था की स्थिति, लिंग "
                "और उम्र के अनुसार काफ़ी भिन्न होते हैं। नीचे दी गई तालिका आमतौर पर स्वीकृत "
                "रेफ़रेंस रेंज को सारांशित करती है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">चरण / समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य रेंज (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">फ़ॉलिक्युलर फ़ेज़</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ल्यूटियल फ़ेज़</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">पहली तिमाही</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">दूसरी तिमाही</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">तीसरी तिमाही</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">मेनोपॉज़ के बाद</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">पुरुष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.5</td></tr>'
                "</tbody></table>"
                "<p>ओव्यूलेशन की पुष्टि के लिए, ब्लड सैंपल आमतौर पर साइकल के 21वें दिन (या अपेक्षित "
                "पीरियड से 7 दिन पहले) लिया जाता है। मिड-ल्यूटियल प्रोजेस्टेरोन लेवल 5&nbsp;ng/mL "
                "से ऊपर होना आम तौर पर दर्शाता है कि ओव्यूलेशन हुआ, जबकि 10&nbsp;ng/mL से नीचे "
                "की वैल्यू ल्यूटियल फ़ेज़ डिफ़ेक्ट का संकेत दे सकती है।</p>"
                "<p>रेफ़रेंस रेंज प्रयोगशालाओं के बीच भिन्न हो सकती हैं; अपने रिज़ल्ट की तुलना हमेशा "
                "अपनी रिपोर्ट पर छपी रेंज से करें। सही व्याख्या के लिए ओव्यूलेशन के संदर्भ में "
                "ब्लड लेने का समय महत्वपूर्ण है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="लो या हाई प्रोजेस्टेरोन के कारण",
            body_html=(
                "<p><strong>लो प्रोजेस्टेरोन</strong> फर्टिलिटी और शुरुआती प्रेगनेंसी के परिणामों के "
                "लिए विशेष रूप से महत्वपूर्ण है। सबसे आम कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>एनोव्यूलेशन:</strong> बिना ओव्यूलेशन के कॉर्पस ल्यूटियम नहीं बनता, "
                "इसलिए प्रोजेस्टेरोन फ़ॉलिक्युलर फ़ेज़ लेवल पर ही रहता है। पॉलीसिस्टिक ओवेरी "
                "सिंड्रोम (PCOS) क्रॉनिक एनोव्यूलेशन का प्रमुख कारण है।</li>"
                "<li><strong>ल्यूटियल फ़ेज़ डिफ़ेक्ट:</strong> कॉर्पस ल्यूटियम अपर्याप्त प्रोजेस्टेरोन "
                "बनाता है, जिससे एंडोमेट्रियम इम्प्लांटेशन के लिए ठीक से तैयार नहीं होता।</li>"
                "<li><strong>थायरॉइड विकार:</strong> हाइपोथायरॉइडिज़्म और हाइपरप्रोलैक्टिनेमिया "
                "अप्रत्यक्ष रूप से प्रोजेस्टेरोन उत्पादन को दबा सकते हैं।</li>"
                "<li><strong>अत्यधिक व्यायाम और पुराना तनाव:</strong> हाइपोथैलेमिक एमेनोरिया का कारण "
                "बन सकते हैं और ओव्यूलेशन को दबा सकते हैं।</li>"
                "<li><strong>पेरिमेनोपॉज़:</strong> मेनोपॉज़ के करीब आने पर ओव्यूलेशन की आवृत्ति कम "
                "हो जाती है और प्रोजेस्टेरोन लेवल गिर जाते हैं।</li>"
                "</ul>"
                "<p>प्रोजेस्टेरोन का ऊँचा स्तर आमतौर पर <strong>प्रेगनेंसी</strong> में एक शारीरिक "
                "स्थिति होती है। पैथोलॉजिकल कारणों में कंजेनिटल एड्रीनल हाइपरप्लेसिया, ओवेरियन सिस्ट, "
                "एड्रीनल ट्यूमर और मोलर प्रेगनेंसी शामिल हैं।</p>"
                "<p><strong>प्रोजेस्टेरोन टेस्ट</strong> की व्याख्या करते समय, जिस दिन ब्लड लिया गया "
                "वह साइकल का कौन सा दिन था, यह महत्वपूर्ण है। फ़ॉलिक्युलर फ़ेज़ में कम वैल्यू पूरी "
                "तरह सामान्य है, जबकि ल्यूटियल फ़ेज़ में वही वैल्यू क्लिनिकली महत्वपूर्ण हो सकती है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>निम्नलिखित स्थितियों में स्त्री रोग विशेषज्ञ या प्रजनन एंडोक्रिनोलॉजिस्ट से "
                "परामर्श करने की सलाह दी जाती है:</p>"
                "<ul>"
                "<li>अनियमित या दर्दनाक मासिक चक्र, एनोव्यूलेशन की आशंका</li>"
                "<li>12 महीने की असुरक्षित कोशिश के बाद भी गर्भधारण न होना (इनफ़र्टिलिटी)</li>"
                "<li>बार-बार पहली तिमाही में गर्भपात होना</li>"
                "<li>छोटा ल्यूटियल फ़ेज़ (ओव्यूलेशन के 10 दिन से कम बाद पीरियड शुरू होना)</li>"
                "<li>शुरुआती प्रेगनेंसी में स्पॉटिंग और पेट दर्द</li>"
                "</ul>"
                "<p>आपके डॉक्टर <strong>प्रोजेस्टेरोन टेस्ट</strong> के साथ LH, FSH, एस्ट्राडायोल, "
                "थायरॉइड पैनल और ज़रूरत पड़ने पर पेल्विक अल्ट्रासाउंड करवा सकते हैं। अगर "
                "<strong>लो प्रोजेस्टेरोन</strong> की पुष्टि होती है, तो उपचार विकल्पों में ओरल या "
                "वैजाइनल प्रोजेस्टेरोन सप्लीमेंटेशन, ओव्यूलेशन इंडक्शन या मूल कारण का इलाज "
                "शामिल हैं।</p>"
                "<p><strong>यह सामग्री केवल सूचनात्मक उद्देश्यों के लिए है और चिकित्सा सलाह, निदान या "
                "उपचार का विकल्प नहीं है।</strong> अपने टेस्ट रिज़ल्ट हमेशा योग्य हेल्थकेयर "
                "प्रोफ़ेशनल के साथ चर्चा करें। NoryaAI मेडिकल कंसल्टेशन का विकल्प नहीं है। "
                '<a href="/analyze">हमारे एनालिसिस पेज पर जाएँ</a> अपने रिज़ल्ट के बारे में '
                "प्रारंभिक जानकारी के लिए।</p>"
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
            heading="اختبار البروجسترون في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>عندما يظهر في تقرير تحليل الدم قيمة <strong>البروجسترون</strong>، فمن الطبيعي أن "
                "تتساءل عن معنى هذا الهرمون. البروجسترون هو هرمون ستيرويدي يُنتَج بشكل رئيسي من الجسم "
                "الأصفر (Corpus Luteum) في المبيضين بعد الإباضة. يلعب دوراً محورياً في تنظيم الدورة "
                "الشهرية، وتحضير بطانة الرحم للزرع، والحفاظ على الحمل المبكر. يُعدّ "
                "<strong>اختبار البروجسترون</strong> من أكثر الفحوصات الهرمونية طلباً في تقييم الخصوبة "
                "ومتابعة الحمل.</p>"
                "<p>يشرح هذا الدليل كيفية تفسير نتائج تحليل البروجسترون في الدم، والمعدلات الطبيعية "
                "حسب مرحلة الدورة وثلث الحمل، وأسباب <strong>انخفاض البروجسترون</strong> أو ارتفاعه، "
                "ومتى يجب مراجعة الطبيب. هدفنا تثقيفي وليس تشخيصياً؛ ناقش نتائجك دائماً مع "
                "متخصص رعاية صحية مؤهل.</p>"
                "<p>يرتفع <strong>البروجسترون أثناء الحمل</strong> بشكل ملحوظ عندما تتولّى المشيمة "
                "إنتاج الهرمون من الجسم الأصفر حوالي الأسبوع 8&ndash;10. المستويات الكافية ضرورية "
                "لتثبيط تقلّصات الرحم، ودعم نمو المشيمة، والحفاظ على الحمل حتى الولادة.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدلات الطبيعية للبروجسترون",
            body_html=(
                "<p>تتفاوت مستويات <strong>البروجسترون</strong> بشكل كبير حسب مرحلة الدورة الشهرية "
                "وحالة الحمل والجنس والعمر. يلخّص الجدول التالي نطاقات المرجع المقبولة على نطاق واسع:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المرحلة / المجموعة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق الطبيعي (ng/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">المرحلة الجُريبية</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">المرحلة الأصفرية</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 25</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الثلث الأول</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">9 – 47</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الثلث الثاني</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">17 – 146</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الثلث الثالث</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">55 – 200</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">بعد انقطاع الطمث</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.4</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الرجال</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1 – 0.5</td></tr>'
                "</tbody></table>"
                "<p>لتأكيد الإباضة، تُسحب عينة الدم عادةً في اليوم 21 من الدورة (أو قبل 7 أيام من "
                "موعد الدورة المتوقع). مستوى بروجسترون منتصف المرحلة الأصفرية أعلى من 5&nbsp;ng/mL "
                "يشير عموماً إلى حدوث الإباضة، بينما قد تشير القيم أقل من 10&nbsp;ng/mL إلى قصور "
                "في المرحلة الأصفرية.</p>"
                "<p>قد تختلف نطاقات المرجع بين المختبرات؛ قارن دائماً نتيجتك بالنطاق المطبوع على "
                "تقريرك. توقيت سحب الدم بالنسبة للإباضة حاسم للتفسير الصحيح.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب انخفاض أو ارتفاع البروجسترون",
            body_html=(
                "<p><strong>انخفاض البروجسترون</strong> له أهمية خاصة بالنسبة للخصوبة ونتائج الحمل "
                "المبكر. تشمل الأسباب الأكثر شيوعاً:</p>"
                "<ul>"
                "<li><strong>انعدام الإباضة:</strong> بدون إباضة لا يتكوّن الجسم الأصفر ويبقى "
                "البروجسترون عند مستويات المرحلة الجُريبية. متلازمة تكيّس المبايض (PCOS) هي السبب "
                "الرئيسي لانعدام الإباضة المزمن.</li>"
                "<li><strong>قصور المرحلة الأصفرية:</strong> ينتج الجسم الأصفر بروجسترون غير كافٍ، "
                "مما يمنع التحضير الملائم لبطانة الرحم للزرع.</li>"
                "<li><strong>اضطرابات الغدة الدرقية:</strong> قصور الغدة الدرقية وفرط البرولاكتين قد "
                "يثبّطان إنتاج البروجسترون بشكل غير مباشر.</li>"
                "<li><strong>الإفراط في التمارين والإجهاد المزمن:</strong> قد يؤديان إلى انقطاع الطمث "
                "الوطائي وتثبيط الإباضة.</li>"
                "<li><strong>ما قبل انقطاع الطمث:</strong> مع اقتراب سن اليأس تقلّ وتيرة الإباضة "
                "وتنخفض مستويات البروجسترون.</li>"
                "</ul>"
                "<p>ارتفاع البروجسترون عادةً ما يكون نتيجة فسيولوجية أثناء <strong>الحمل</strong>. "
                "تشمل الأسباب المرضية فرط تنسّج الكظر الخلقي، أكياس المبيض، أورام الغدة الكظرية "
                "والحمل العنقودي.</p>"
                "<p>عند تفسير <strong>اختبار البروجسترون</strong>، يُعدّ يوم الدورة الذي سُحبت فيه "
                "العينة أمراً حاسماً: قيمة منخفضة في المرحلة الجُريبية طبيعية تماماً، بينما قد تكون "
                "نفس القيمة في المرحلة الأصفرية ذات دلالة سريرية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>يُنصح بمراجعة طبيب/ة أمراض النساء أو أخصائي/ة الغدد الصماء التناسلية إذا كنتِ "
                "تعانين من:</p>"
                "<ul>"
                "<li>دورات شهرية غير منتظمة أو مؤلمة، اشتباه بانعدام الإباضة</li>"
                "<li>عدم القدرة على الحمل بعد 12 شهراً من المحاولة (العقم)</li>"
                "<li>إجهاضات متكررة في الثلث الأول</li>"
                "<li>مرحلة أصفرية قصيرة (نزول الدورة بعد أقل من 10 أيام من الإباضة)</li>"
                "<li>تبقيع وألم في البطن في الأسابيع الأولى من الحمل</li>"
                "</ul>"
                "<p>قد يطلب طبيبك <strong>اختبار البروجسترون</strong> إلى جانب LH وFSH والإستراديول "
                "ولوحة الغدة الدرقية وربما تصوير الحوض بالموجات فوق الصوتية. إذا تأكد "
                "<strong>انخفاض البروجسترون</strong>، تشمل خيارات العلاج المكمّلات الفموية أو المهبلية "
                "للبروجسترون، تحفيز الإباضة أو علاج السبب الكامن.</p>"
                "<p><strong>هذا المحتوى لأغراض إعلامية فقط ولا يُشكّل نصيحة طبية أو تشخيصاً "
                "أو علاجاً.</strong> ناقش نتائج فحوصاتك دائماً مع متخصص رعاية صحية مؤهل. "
                "NoryaAI ليس بديلاً عن الاستشارة الطبية. "
                '<a href="/analyze">قم بزيارة صفحة التحليل الخاصة بنا</a> للحصول على رؤى أولية '
                "حول نتائجك.</p>"
            ),
        ),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_progesterone_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Progesterone article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_progesterone_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Progesterone article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a progesterone blood test and why is it ordered?",
             "answer": "A progesterone blood test measures the level of progesterone hormone in your blood. It is most commonly ordered to confirm ovulation, evaluate luteal phase adequacy, monitor early pregnancy, and investigate causes of infertility or recurrent miscarriage."},
            {"question": "What is a normal progesterone level?",
             "answer": "Normal progesterone levels depend on the menstrual cycle phase: follicular phase 0.1–0.7 ng/mL, luteal phase 2–25 ng/mL, first trimester 9–47 ng/mL, second trimester 17–146 ng/mL, and third trimester 55–200 ng/mL. Post-menopausal women typically have levels below 0.4 ng/mL."},
            {"question": "What causes low progesterone and how is it treated?",
             "answer": "Low progesterone is commonly caused by anovulation (often due to PCOS), luteal phase defect, thyroid disorders, hyperprolactinaemia, excessive exercise, chronic stress, or perimenopause. Treatment may include oral or vaginal progesterone supplementation, ovulation induction, or management of the underlying condition."},
        ],
        "tr": [
            {"question": "Progesteron kan testi nedir ve neden istenir?",
             "answer": "Progesteron kan testi, kandaki progesteron hormon düzeyini ölçer. En sık ovülasyonun doğrulanması, luteal faz yeterliliğinin değerlendirilmesi, erken gebelik takibi ve infertilite veya tekrarlayan düşük nedenlerinin araştırılması amacıyla istenir."},
            {"question": "Normal progesteron değeri nedir?",
             "answer": "Normal progesteron değerleri menstrüel döngü fazına göre değişir: foliküler faz 0,1–0,7 ng/mL, luteal faz 2–25 ng/mL, 1. trimester 9–47 ng/mL, 2. trimester 17–146 ng/mL ve 3. trimester 55–200 ng/mL. Menopoz sonrası kadınlarda genellikle 0,4 ng/mL altındadır."},
            {"question": "Düşük progesteronun nedenleri ve tedavisi nedir?",
             "answer": "Düşük progesteron en sık anovülasyon (genellikle PKOS'a bağlı), luteal faz defekti, tiroid bozuklukları, hiperprolaktinemi, aşırı egzersiz, kronik stres veya perimenopozdan kaynaklanır. Tedavide oral veya vajinal progesteron takviyesi, ovülasyon indüksiyonu veya altta yatan nedenin tedavisi uygulanabilir."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de progesterona en sangre y por qué se solicita?",
             "answer": "La prueba de progesterona mide el nivel de esta hormona en la sangre. Se solicita principalmente para confirmar la ovulación, evaluar la fase lútea, monitorizar el embarazo temprano e investigar causas de infertilidad o abortos recurrentes."},
            {"question": "¿Cuál es un nivel normal de progesterona?",
             "answer": "Los niveles normales dependen de la fase del ciclo: fase folicular 0,1–0,7 ng/mL, fase lútea 2–25 ng/mL, primer trimestre 9–47 ng/mL, segundo trimestre 17–146 ng/mL y tercer trimestre 55–200 ng/mL. En la posmenopausia suele ser inferior a 0,4 ng/mL."},
            {"question": "¿Qué causa la progesterona baja y cómo se trata?",
             "answer": "La progesterona baja suele deberse a anovulación (frecuentemente por SOP), defecto de fase lútea, trastornos tiroideos, hiperprolactinemia, ejercicio excesivo, estrés crónico o perimenopausia. El tratamiento puede incluir suplementos de progesterona oral o vaginal, inducción de la ovulación o manejo de la causa subyacente."},
        ],
        "de": [
            {"question": "Was ist ein Progesteron-Bluttest und warum wird er angeordnet?",
             "answer": "Ein Progesteron-Bluttest misst den Progesteronspiegel im Blut. Er wird am häufigsten angeordnet, um den Eisprung zu bestätigen, die Lutealphase zu beurteilen, eine frühe Schwangerschaft zu überwachen und Ursachen von Unfruchtbarkeit oder wiederholten Fehlgeburten abzuklären."},
            {"question": "Was ist ein normaler Progesteronwert?",
             "answer": "Normale Progesteronwerte hängen von der Zyklusphase ab: Follikelphase 0,1–0,7 ng/mL, Lutealphase 2–25 ng/mL, 1. Trimester 9–47 ng/mL, 2. Trimester 17–146 ng/mL und 3. Trimester 55–200 ng/mL. Nach der Menopause liegt der Wert typischerweise unter 0,4 ng/mL."},
            {"question": "Was verursacht niedrigen Progesteronspiegel und wie wird er behandelt?",
             "answer": "Niedriges Progesteron entsteht häufig durch Anovulation (oft bei PCOS), Lutealphasendefekt, Schilddrüsenstörungen, Hyperprolaktinämie, übermäßige Belastung, chronischen Stress oder Perimenopause. Die Behandlung kann orale oder vaginale Progesteronsupplementierung, Ovulationsinduktion oder Therapie der Grundursache umfassen."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'un test de progestérone et pourquoi est-il prescrit ?",
             "answer": "Le test de progestérone mesure le taux de cette hormone dans le sang. Il est principalement prescrit pour confirmer l'ovulation, évaluer la phase lutéale, surveiller une grossesse précoce et rechercher les causes d'infertilité ou de fausses couches récurrentes."},
            {"question": "Quel est un taux normal de progestérone ?",
             "answer": "Les taux normaux dépendent de la phase du cycle : phase folliculaire 0,1–0,7 ng/mL, phase lutéale 2–25 ng/mL, 1er trimestre 9–47 ng/mL, 2e trimestre 17–146 ng/mL et 3e trimestre 55–200 ng/mL. Après la ménopause, le taux est généralement inférieur à 0,4 ng/mL."},
            {"question": "Quelles sont les causes d'une progestérone basse et comment la traiter ?",
             "answer": "Une progestérone basse est souvent due à l'anovulation (fréquemment liée au SOPK), à une insuffisance lutéale, à des troubles thyroïdiens, à une hyperprolactinémie, à un exercice excessif, au stress chronique ou à la périménopause. Le traitement peut inclure une supplémentation en progestérone orale ou vaginale, l'induction de l'ovulation ou la prise en charge de la cause sous-jacente."},
        ],
        "it": [
            {"question": "Che cos'è il test del progesterone e perché viene prescritto?",
             "answer": "Il test del progesterone misura il livello di questo ormone nel sangue. Viene prescritto principalmente per confermare l'ovulazione, valutare la fase luteale, monitorare una gravidanza iniziale e indagare le cause di infertilità o aborti ricorrenti."},
            {"question": "Qual è un valore normale di progesterone?",
             "answer": "I valori normali dipendono dalla fase del ciclo: fase follicolare 0,1–0,7 ng/mL, fase luteale 2–25 ng/mL, 1° trimestre 9–47 ng/mL, 2° trimestre 17–146 ng/mL e 3° trimestre 55–200 ng/mL. Dopo la menopausa il valore è tipicamente inferiore a 0,4 ng/mL."},
            {"question": "Quali sono le cause del progesterone basso e come si tratta?",
             "answer": "Il progesterone basso è spesso dovuto ad anovulazione (frequentemente per PCOS), difetto della fase luteale, disturbi tiroidei, iperprolattinemia, esercizio eccessivo, stress cronico o perimenopausa. Il trattamento può comprendere supplementazione con progesterone orale o vaginale, induzione dell'ovulazione o gestione della causa sottostante."},
        ],
        "he": [
            {"question": "מהי בדיקת פרוגסטרון בדם ולמה היא מבוצעת?",
             "answer": "בדיקת פרוגסטרון בדם מודדת את רמת הורמון הפרוגסטרון בדם. היא מבוצעת בעיקר לאישור ביוץ, הערכת השלב הלוטאלי, מעקב הריון מוקדם וחקירת גורמים לאי-פוריות או הפלות חוזרות."},
            {"question": "מהי רמת פרוגסטרון תקינה?",
             "answer": "רמות פרוגסטרון תקינות תלויות בשלב המחזור: שלב פוליקולרי 0.1–0.7 ng/mL, שלב לוטאלי 2–25 ng/mL, שליש ראשון 9–47 ng/mL, שליש שני 17–146 ng/mL ושליש שלישי 55–200 ng/mL. לאחר גיל המעבר הרמה בדרך כלל מתחת ל-0.4 ng/mL."},
            {"question": "מה גורם לפרוגסטרון נמוך ואיך מטפלים?",
             "answer": "פרוגסטרון נמוך נגרם בדרך כלל מחוסר ביוץ (לעיתים קרובות עקב PCOS), ליקוי בשלב הלוטאלי, הפרעות בבלוטת התריס, היפרפרולקטינמיה, פעילות גופנית מוגזמת, מתח כרוני או פרימנופאוזה. הטיפול עשוי לכלול תוספי פרוגסטרון אוראליים או וגינליים, השראת ביוץ או טיפול בגורם הבסיסי."},
        ],
        "hi": [
            {"question": "प्रोजेस्टेरोन ब्लड टेस्ट क्या है और यह क्यों किया जाता है?",
             "answer": "प्रोजेस्टेरोन ब्लड टेस्ट आपके रक्त में प्रोजेस्टेरोन हार्मोन के स्तर को मापता है। यह मुख्य रूप से ओव्यूलेशन की पुष्टि, ल्यूटियल फ़ेज़ की पर्याप्तता का मूल्यांकन, शुरुआती प्रेगनेंसी की निगरानी और इनफ़र्टिलिटी या बार-बार गर्भपात के कारणों की जाँच के लिए किया जाता है।"},
            {"question": "सामान्य प्रोजेस्टेरोन लेवल क्या है?",
             "answer": "सामान्य प्रोजेस्टेरोन लेवल मासिक चक्र के चरण पर निर्भर करते हैं: फ़ॉलिक्युलर फ़ेज़ 0.1–0.7 ng/mL, ल्यूटियल फ़ेज़ 2–25 ng/mL, पहली तिमाही 9–47 ng/mL, दूसरी तिमाही 17–146 ng/mL और तीसरी तिमाही 55–200 ng/mL। मेनोपॉज़ के बाद महिलाओं में आमतौर पर 0.4 ng/mL से कम होता है।"},
            {"question": "लो प्रोजेस्टेरोन के कारण क्या हैं और इसका इलाज कैसे होता है?",
             "answer": "लो प्रोजेस्टेरोन आमतौर पर एनोव्यूलेशन (अक्सर PCOS के कारण), ल्यूटियल फ़ेज़ डिफ़ेक्ट, थायरॉइड विकार, हाइपरप्रोलैक्टिनेमिया, अत्यधिक व्यायाम, पुराने तनाव या पेरिमेनोपॉज़ से होता है। उपचार में ओरल या वैजाइनल प्रोजेस्टेरोन सप्लीमेंटेशन, ओव्यूलेशन इंडक्शन या मूल कारण का इलाज शामिल हो सकता है।"},
        ],
        "ar": [
            {"question": "ما هو اختبار البروجسترون في الدم ولماذا يُطلب؟",
             "answer": "اختبار البروجسترون يقيس مستوى هرمون البروجسترون في الدم. يُطلب بشكل رئيسي لتأكيد الإباضة، وتقييم المرحلة الأصفرية، ومتابعة الحمل المبكر، والتحقيق في أسباب العقم أو الإجهاضات المتكررة."},
            {"question": "ما هو المستوى الطبيعي للبروجسترون؟",
             "answer": "تعتمد المستويات الطبيعية على مرحلة الدورة: المرحلة الجُريبية 0.1–0.7 ng/mL، المرحلة الأصفرية 2–25 ng/mL، الثلث الأول 9–47 ng/mL، الثلث الثاني 17–146 ng/mL والثلث الثالث 55–200 ng/mL. بعد انقطاع الطمث يكون المستوى عادةً أقل من 0.4 ng/mL."},
            {"question": "ما أسباب انخفاض البروجسترون وكيف يُعالج؟",
             "answer": "ينتج انخفاض البروجسترون عادةً عن انعدام الإباضة (غالباً بسبب تكيّس المبايض)، قصور المرحلة الأصفرية، اضطرابات الغدة الدرقية، فرط البرولاكتين، الإفراط في التمارين، الإجهاد المزمن أو ما قبل انقطاع الطمث. قد يشمل العلاج مكملات البروجسترون الفموية أو المهبلية، تحفيز الإباضة أو علاج السبب الكامن."},
        ],
    }
