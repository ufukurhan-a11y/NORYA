# -*- coding: utf-8 -*-
"""
Testosterone blog article — full body content for all 9 languages.
Used by blog_i18n._article_testosterone().
Sections: intro, what-is, normal-ranges, causes, symptoms,
related-tests, when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="Testosterone levels: what your blood test result means",
            body_html=(
                "<p>Testosterone is the primary male sex hormone, but it plays important roles in both men and women. "
                "When a blood test flags your testosterone as high or low, it is natural to wonder what it means for your health. "
                "Testosterone influences muscle mass, bone density, fat distribution, red blood cell production, mood, and libido.</p>"
                "<p>This guide explains what testosterone does, how to read your result against sex-specific reference ranges, "
                "the most common causes of abnormal levels, associated symptoms, and when to talk to your doctor. "
                "It is educational content, not a medical diagnosis&mdash;always discuss your results with a healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is testosterone and why does it matter?",
            body_html=(
                "<p><strong>Testosterone</strong> is an androgen hormone produced mainly by the Leydig cells in the testes in men "
                "and in smaller amounts by the ovaries and adrenal glands in women. Its production is regulated by the "
                "<strong>hypothalamic-pituitary-gonadal (HPG) axis</strong>: the hypothalamus releases GnRH, stimulating the pituitary to secrete "
                "<strong>LH</strong> (luteinising hormone) and <strong>FSH</strong> (follicle-stimulating hormone), which in turn stimulate testosterone synthesis. "
                "Testosterone feeds back to suppress GnRH and LH, maintaining hormonal balance.</p>"
                "<p>In men, testosterone drives the development of male secondary sexual characteristics during puberty (voice deepening, facial hair, "
                "muscle growth), supports spermatogenesis, and maintains bone and muscle mass throughout adulthood. "
                "In women, testosterone contributes to libido, bone strength, and overall energy levels, "
                "but elevated levels can cause unwanted effects like hirsutism and acne.</p>"
                "<p>Most circulating testosterone is bound to <strong>SHBG</strong> (sex hormone-binding globulin) and albumin. "
                "Only about 1&ndash;3% circulates as <strong>free testosterone</strong>, the biologically active form. "
                "Your doctor may order both total and free testosterone to get a complete picture, especially if SHBG levels are suspected to be abnormal.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal testosterone ranges",
            body_html=(
                "<p>Testosterone levels vary by sex, age, and time of day (levels peak in the morning). "
                "Blood is typically drawn in the morning (before 10 AM) for the most reliable measurement.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typical range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adult men</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">300&ndash;1,000 ng/dL (10.4&ndash;34.7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adult women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">15&ndash;70 ng/dL (0.5&ndash;2.4 nmol/L)</td></tr>'
                "</tbody></table>"
                "<p>Testosterone declines gradually with age in men&mdash;roughly 1&ndash;2% per year after age 30. "
                "A value near the lower end of the range in an older man may not be abnormal. "
                "In women, levels are much lower and fluctuate with the menstrual cycle. "
                "Always compare your result to the specific range on your laboratory report.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of abnormal testosterone levels",
            body_html=(
                "<p><strong>Low testosterone in men (male hypogonadism)</strong> can be classified as primary (testicular failure) "
                "or secondary (hypothalamic-pituitary dysfunction). Common causes include <strong>aging</strong>, "
                "<strong>obesity</strong> (excess fat tissue converts testosterone to estrogen via aromatase), "
                "<strong>type 2 diabetes</strong>, <strong>pituitary disorders</strong> (adenomas, hypopituitarism), "
                "<strong>chronic illness</strong> (liver disease, HIV, chronic kidney disease), <strong>Klinefelter syndrome</strong>, "
                "and <strong>medications</strong> (opioids, glucocorticoids, some antidepressants). "
                "Testicular injury, infection (orchitis), or cancer treatment (chemotherapy, radiation) can also reduce production.</p>"
                "<p><strong>High testosterone in women</strong> is most commonly associated with <strong>polycystic ovary syndrome (PCOS)</strong>, "
                "a condition characterised by irregular periods, ovarian cysts, and hyperandrogenism. "
                "Other causes include <strong>adrenal disorders</strong> (congenital adrenal hyperplasia, adrenal tumours), "
                "<strong>ovarian tumours</strong>, and <strong>medications</strong> (anabolic steroids, danazol). "
                "In men, exogenous testosterone use (anabolic steroids) raises levels supraphysiologically.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of abnormal testosterone",
            body_html=(
                "<p><strong>Low testosterone in men</strong> may present with <strong>fatigue</strong>, <strong>decreased libido</strong>, "
                "<strong>erectile dysfunction</strong>, <strong>mood changes</strong> (depression, irritability, difficulty concentrating), "
                "<strong>decreased muscle mass</strong>, <strong>increased body fat</strong> (especially abdominal), "
                "<strong>reduced bone density</strong>, <strong>decreased body hair</strong>, and sometimes breast tissue enlargement (gynecomastia). "
                "Symptoms often develop gradually and may be attributed to aging or stress before the diagnosis is made.</p>"
                "<p><strong>High testosterone in women</strong> can cause <strong>hirsutism</strong> (excess facial and body hair), "
                "<strong>acne</strong>, <strong>deepening of the voice</strong>, <strong>irregular or absent periods</strong>, "
                "<strong>male-pattern hair loss</strong>, and <strong>weight gain</strong>. In the context of PCOS, "
                "infertility is a common concern. Elevated androgens can also affect metabolic health, increasing the risk of insulin resistance and cardiovascular disease.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests your doctor may order",
            body_html=(
                "<p>When evaluating testosterone abnormalities, your doctor will consider the clinical context and often order additional tests. "
                "<strong>LH</strong> and <strong>FSH</strong> help distinguish primary from secondary hypogonadism: "
                "high LH/FSH with low testosterone suggests testicular failure, while low LH/FSH suggests a pituitary or hypothalamic problem.</p>"
                "<p><strong>SHBG</strong> (sex hormone-binding globulin) affects how much testosterone is biologically available; "
                "conditions like obesity lower SHBG, while hyperthyroidism and liver disease raise it. "
                "<strong>Free testosterone</strong> or calculated free testosterone provides additional clarity. "
                "Other commonly ordered tests include <strong>prolactin</strong> (elevated prolactin can suppress testosterone), "
                "<strong>thyroid function</strong>, <strong>estradiol</strong> (in men with gynecomastia), "
                "and <strong>DHEA-S</strong> or <strong>17-hydroxyprogesterone</strong> (in women with suspected adrenal androgen excess).</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Men should talk to their doctor if they experience persistent fatigue, decreased libido, erectile dysfunction, "
                "mood changes, or loss of muscle mass&mdash;especially if a blood test shows low testosterone. "
                "The diagnosis of hypogonadism requires at least <strong>two morning blood samples</strong> showing low total testosterone, "
                "combined with consistent symptoms, before treatment is considered.</p>"
                "<p>Women should consult their doctor if they notice excess hair growth, acne, irregular periods, or difficulty conceiving, "
                "as these may indicate elevated androgens. A hormonal workup can help determine whether PCOS, adrenal disorders, "
                "or other conditions are responsible. Early diagnosis and management can improve both symptoms and long-term health outcomes.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your testosterone",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare. Upload your blood test report at "
                "<a href=\"/analyze\">noryaai.com/analyze</a> and receive a clear, structured summary that highlights your testosterone level "
                "alongside related hormonal markers like LH, FSH, and SHBG. The report flags out-of-range values "
                "and provides context so you can have a more informed discussion with your doctor.</p>"
                "<p>Whether you are investigating symptoms of low testosterone or monitoring a hormonal condition, "
                "Norya organises your results so you can focus on the conversation that matters. "
                "For plan options and pricing, visit our <a href=\"/pricing\">pricing page</a>.</p>"
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
            heading="Testosteron düzeyi: kan tahlili sonucunuz ne anlama geliyor?",
            body_html=(
                "<p>Testosteron birincil erkek cinsiyet hormonudur, ancak hem erkeklerde hem de kadınlarda önemli roller oynar. "
                "Kan testiniz testosteronunuzu yüksek veya düşük olarak işaretlediğinde, bunun sağlığınız için ne anlama geldiğini merak etmeniz doğaldır. "
                "Testosteron kas kütlesini, kemik yoğunluğunu, yağ dağılımını, kırmızı kan hücresi üretimini, ruh halini ve libidoyu etkiler.</p>"
                "<p>Bu rehber testosteronun ne yaptığını, sonucunuzu cinsiyete özgü referans aralıklarına göre nasıl okuyacağınızı, "
                "anormal düzeylerin yaygın nedenlerini, ilişkili belirtileri ve ne zaman hekime danışmanız gerektiğini açıklar. "
                "Eğitim amaçlıdır, teşhis değildir&mdash;sonuçlarınızı mutlaka bir sağlık profesyoneliyle değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Testosteron nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Testosteron</strong>, erkeklerde esas olarak testislerdeki Leydig hücreleri, kadınlarda ise daha az miktarda yumurtalıklar ve adrenal bezler "
                "tarafından üretilen bir androjen hormondur. Üretimi <strong>hipotalamus-hipofiz-gonad (HPG) ekseni</strong> tarafından düzenlenir: "
                "hipotalamus GnRH salgılar, hipofiz LH ve FSH üretir, bunlar da testosteron sentezini uyarır. "
                "Testosteron geri bildirim yoluyla GnRH ve LH&rsquo;yi baskılayarak hormonal dengeyi korur.</p>"
                "<p>Erkeklerde testosteron ergenlikte ikincil cinsiyet özelliklerinin gelişmesini (sesin kalınlaşması, yüz kılları, kas büyümesi) yönlendirir, "
                "spermatogenezi destekler ve yetişkinlik boyunca kemik ve kas kütlesini korur. "
                "Kadınlarda libido, kemik gücü ve genel enerji düzeylerine katkıda bulunur; ancak yüksek düzeyler hirsutizm ve akne gibi istenmeyen etkilere neden olabilir.</p>"
                "<p>Dolaşımdaki testosteronun çoğu <strong>SHBG</strong> (cinsiyet hormonu bağlayıcı globulin) ve albümine bağlıdır. "
                "Yalnızca yaklaşık %1&ndash;3&rsquo;ü biyolojik olarak aktif form olan <strong>serbest testosteron</strong> olarak dolaşır. "
                "SHBG düzeylerinin anormal olduğundan şüpheleniliyorsa hekiminiz hem total hem serbest testosteron isteyebilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal testosteron aralıkları",
            body_html=(
                "<p>Testosteron düzeyleri cinsiyete, yaşa ve günün saatine göre değişir (sabah en yüksektir). "
                "En güvenilir ölçüm için kan genellikle sabah (saat 10:00 öncesi) alınır.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tipik aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yetişkin erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">300&ndash;1.000 ng/dL (10,4&ndash;34,7 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yetişkin kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">15&ndash;70 ng/dL (0,5&ndash;2,4 nmol/L)</td></tr>'
                "</tbody></table>"
                "<p>Erkeklerde testosteron 30 yaşından sonra yılda yaklaşık %1&ndash;2 oranında kademeli olarak düşer. "
                "Yaşlı bir erkekte aralığın alt sınırına yakın bir değer anormal olmayabilir. "
                "Kadınlarda düzeyler çok daha düşüktür ve menstrüel döngüye göre dalgalanır. "
                "Sonucunuzu her zaman laboratuvar raporunuzdaki spesifik aralıkla karşılaştırın.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Anormal testosteron düzeylerinin nedenleri",
            body_html=(
                "<p><strong>Erkeklerde düşük testosteron (erkek hipogonadizmi)</strong> primer (testiküler yetmezlik) "
                "veya sekonder (hipotalamus-hipofiz işlev bozukluğu) olarak sınıflandırılır. Yaygın nedenler: <strong>yaşlanma</strong>, "
                "<strong>obezite</strong> (fazla yağ dokusu aromataz yoluyla testosteronu östrojene dönüştürür), "
                "<strong>tip 2 diyabet</strong>, <strong>hipofiz bozuklukları</strong>, <strong>kronik hastalık</strong> (karaciğer hastalığı, HIV, kronik böbrek hastalığı), "
                "<strong>Klinefelter sendromu</strong> ve <strong>ilaçlar</strong> (opioidler, glukokortikoidler, bazı antidepresanlar). "
                "Testiküler yaralanma, enfeksiyon (orşit) veya kanser tedavisi (kemoterapi, radyasyon) de üretimi azaltabilir.</p>"
                "<p><strong>Kadınlarda yüksek testosteron</strong> en sık <strong>polikistik over sendromu (PKOS)</strong> ile ilişkilidir; "
                "düzensiz adetler, over kistleri ve hiperandrojenizm ile karakterize bir durumdur. "
                "Diğer nedenler: <strong>adrenal bozukluklar</strong> (konjenital adrenal hiperplazi, adrenal tümörler), "
                "<strong>over tümörleri</strong> ve <strong>ilaçlar</strong> (anabolik steroidler, danazol).</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Anormal testosteron belirtileri",
            body_html=(
                "<p><strong>Erkeklerde düşük testosteron</strong> belirtileri: <strong>yorgunluk</strong>, <strong>azalmış libido</strong>, "
                "<strong>erektil disfonksiyon</strong>, <strong>ruh hali değişiklikleri</strong> (depresyon, irritabilite, konsantrasyon güçlüğü), "
                "<strong>azalmış kas kütlesi</strong>, <strong>artmış vücut yağı</strong> (özellikle karın bölgesinde), "
                "<strong>azalmış kemik yoğunluğu</strong>, <strong>azalmış vücut kılları</strong> ve bazen meme dokusu büyümesi (jinekomasti). "
                "Belirtiler genellikle kademeli olarak gelişir ve tanı konulmadan önce yaşlanma veya strese bağlanabilir.</p>"
                "<p><strong>Kadınlarda yüksek testosteron</strong> belirtileri: <strong>hirsutizm</strong> (yüz ve vücutta fazla kıllanma), "
                "<strong>akne</strong>, <strong>sesin kalınlaşması</strong>, <strong>düzensiz veya kesilmiş adetler</strong>, "
                "<strong>erkek tipi saç dökülmesi</strong> ve <strong>kilo artışı</strong>. PKOS bağlamında infertilite sık görülen bir endişedir. "
                "Yüksek androjenler insülin direnci ve kardiyovasküler hastalık riskini de artırabilir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Hekiminizin isteyebileceği ilişkili testler",
            body_html=(
                "<p>Testosteron anormalliklerini değerlendirirken hekiminiz klinik bağlamı göz önünde bulundurur ve genellikle ek testler ister. "
                "<strong>LH</strong> ve <strong>FSH</strong>, primer ile sekonder hipogonadizmi ayırt etmeye yardımcı olur: "
                "düşük testosteron ile yüksek LH/FSH testiküler yetmezliği, düşük LH/FSH ise hipofiz veya hipotalamus sorununu düşündürür.</p>"
                "<p><strong>SHBG</strong>, <strong>serbest testosteron</strong>, <strong>prolaktin</strong> (yüksek prolaktin testosteronu baskılayabilir), "
                "<strong>tiroid fonksiyon testleri</strong>, <strong>estradiol</strong> (jinekomastisi olan erkeklerde) "
                "ve kadınlarda adrenal androjen fazlalığı şüphesinde <strong>DHEA-S</strong> veya <strong>17-hidroksiprogesteron</strong> istenebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Sürekli yorgunluk, azalmış libido, erektil disfonksiyon, ruh hali değişiklikleri veya kas kütlesi kaybı yaşayan erkekler "
                "hekimlerine danışmalıdır&mdash;özellikle kan testinde düşük testosteron görüldüyse. "
                "Hipogonadizm tanısı için tedavi düşünülmeden önce tutarlı belirtilerle birlikte en az <strong>iki sabah kan örneğinde</strong> "
                "düşük total testosteron gösterilmesi gerekir.</p>"
                "<p>Fazla kıllanma, akne, düzensiz adetler veya gebe kalmada güçlük yaşayan kadınlar hekimine danışmalıdır; "
                "çünkü bunlar yüksek androjen düzeylerini gösterebilir. Hormonal değerlendirme PKOS, adrenal bozukluklar "
                "veya diğer durumların sorumlu olup olmadığını belirlemeye yardımcı olabilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya testosteronunuzu anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;hazırlanmanıza yardımcı olur. Kan tahlili raporunuzu "
                "<a href=\"/analyze\">noryaai.com/analyze</a> adresine yükleyin ve testosteron düzeyinizi "
                "LH, FSH ve SHBG gibi ilişkili hormonal belirteçlerle birlikte açıklayan yapılandırılmış bir özet alın.</p>"
                "<p>Düşük testosteron belirtilerini araştırıyor veya hormonal bir durumu takip ediyor olun, "
                "Norya sonuçlarınızı önemli olan konuşmaya odaklanabilmeniz için düzenler. "
                "Plan seçenekleri ve fiyatlandırma için <a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Yasal uyarı",
            body_html=(
                '<p><strong>Bu rehber yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                'Sonuçlarınızı mutlaka bir sağlık profesyoneliyle değerlendirin. <a href="/analyze">Norya ile analize başlayın</a></p>'
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
            heading="Niveles de testosterona: qué significa tu análisis de sangre",
            body_html=(
                "<p>La testosterona es la principal hormona sexual masculina, pero desempeña funciones importantes tanto en hombres como en mujeres. "
                "Cuando un análisis de sangre marca tu testosterona como alta o baja, es natural preguntarse qué implica para la salud. "
                "La testosterona influye en la masa muscular, la densidad ósea, la distribución de grasa, la libido y el estado de ánimo.</p>"
                "<p>Esta guía explica qué hace la testosterona, cómo interpretar tu resultado, las causas comunes de niveles anormales, "
                "los síntomas asociados y cuándo consultar al médico. Es contenido educativo, no un diagnóstico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es la testosterona y por qué es importante?",
            body_html=(
                "<p><strong>La testosterona</strong> es un andrógeno producido principalmente por las células de Leydig en los testículos (hombres) "
                "y en menor cantidad por los ovarios y las glándulas suprarrenales (mujeres). Su producción se regula por el "
                "<strong>eje hipotálamo-hipófisis-gónada (HPG)</strong>. En hombres, impulsa el desarrollo de caracteres sexuales secundarios, "
                "la espermatogénesis y el mantenimiento de masa ósea y muscular. En mujeres, contribuye a la libido y la salud ósea.</p>"
                "<p>La mayor parte de la testosterona circulante está unida a <strong>SHBG</strong> y albúmina. "
                "Solo el 1&ndash;3 % circula como <strong>testosterona libre</strong>, la forma biológicamente activa.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos normales de testosterona",
            body_html=(
                "<p>Los niveles varían por sexo, edad y hora del día (pico matutino). La sangre se extrae antes de las 10 AM:</p>"
                "<ul>"
                "<li><strong>Hombres adultos:</strong> 300&ndash;1.000 ng/dL (10,4&ndash;34,7 nmol/L)</li>"
                "<li><strong>Mujeres adultas:</strong> 15&ndash;70 ng/dL (0,5&ndash;2,4 nmol/L)</li>"
                "</ul>"
                "<p>En hombres, la testosterona desciende ~1&ndash;2 % al año tras los 30. "
                "En mujeres, los niveles son mucho más bajos y fluctúan con el ciclo menstrual. "
                "Compara siempre con el rango de tu informe.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de testosterona anormal",
            body_html=(
                "<p><strong>Testosterona baja en hombres (hipogonadismo):</strong> envejecimiento, obesidad, diabetes tipo 2, "
                "trastornos hipofisarios, enfermedad crónica (hepática, renal, VIH), síndrome de Klinefelter "
                "y medicamentos (opioides, glucocorticoides). Lesión testicular, infecciones o tratamiento oncológico también la reducen.</p>"
                "<p><strong>Testosterona alta en mujeres:</strong> <strong>síndrome de ovario poliquístico (SOP)</strong> es la causa más frecuente. "
                "Otros: trastornos suprarrenales (hiperplasia suprarrenal congénita, tumores), tumores ováricos y esteroides anabólicos.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de testosterona anormal",
            body_html=(
                "<p><strong>Baja en hombres:</strong> fatiga, disminución de la libido, disfunción eréctil, cambios de humor, "
                "pérdida muscular, aumento de grasa corporal, reducción de la densidad ósea y ginecomastia.</p>"
                "<p><strong>Alta en mujeres:</strong> hirsutismo, acné, engrosamiento de la voz, irregularidades menstruales, "
                "alopecia de patrón masculino y aumento de peso. En el contexto de SOP, la infertilidad es frecuente.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p><strong>LH</strong> y <strong>FSH</strong> distinguen hipogonadismo primario de secundario. "
                "<strong>SHBG</strong> y <strong>testosterona libre</strong> dan información adicional. "
                "Otras pruebas: <strong>prolactina</strong>, función tiroidea, estradiol (en hombres con ginecomastia) "
                "y <strong>DHEA-S</strong> o <strong>17-OH-progesterona</strong> (en mujeres con exceso androgénico suprarrenal sospechado).</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Los hombres deben consultar ante fatiga persistente, disminución de la libido, disfunción eréctil o pérdida de masa muscular. "
                "El diagnóstico de hipogonadismo requiere al menos <strong>dos muestras matutinas</strong> con testosterona baja y síntomas compatibles.</p>"
                "<p>Las mujeres deben consultar ante hirsutismo, acné, irregularidades menstruales o dificultad para concebir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya te ayuda a entender tu testosterona",
            body_html=(
                "<p>Norya no diagnostica&mdash;te ayuda a prepararte. Sube tu análisis en "
                "<a href=\"/analyze\">noryaai.com/analyze</a> y recibe un resumen claro con testosterona, LH, FSH y SHBG.</p>"
                "<p>Norya organiza tus resultados para centrarte en la conversación con tu médico. "
                "Para planes y precios: <a href=\"/pricing\">página de precios</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso legal",
            body_html=(
                '<p><strong>Esta guía es solo informativa y no sustituye el consejo ni el diagnóstico médico.</strong> '
                'Comenta siempre tus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'
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
            heading="Testosteronspiegel: was Ihr Bluttest bedeutet",
            body_html=(
                "<p>Testosteron ist das primäre männliche Sexualhormon, spielt aber auch bei Frauen eine Rolle. "
                "Wenn Ihr Bluttest Testosteron als hoch oder niedrig markiert, ist es natürlich zu fragen, was das für Ihre Gesundheit bedeutet. "
                "Testosteron beeinflusst Muskelmasse, Knochendichte, Fettverteilung, Libido und Stimmung.</p>"
                "<p>Dieser Ratgeber erklärt, was Testosteron tut, wie Sie Ihr Ergebnis einordnen, häufige Ursachen und wann Sie einen Arzt aufsuchen sollten.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist Testosteron und warum ist es wichtig?",
            body_html=(
                "<p><strong>Testosteron</strong> ist ein Androgen, das bei Männern hauptsächlich von den Leydig-Zellen der Hoden und bei Frauen in geringeren Mengen "
                "von Ovarien und Nebennieren produziert wird. Die Steuerung erfolgt über die <strong>HPG-Achse</strong> (Hypothalamus-Hypophyse-Gonade). "
                "Bei Männern fördert es die Entwicklung sekundärer Geschlechtsmerkmale, die Spermatogenese und den Erhalt von Knochen- und Muskelmasse. "
                "Bei Frauen trägt es zu Libido und Knochenstärke bei.</p>"
                "<p>Der Großteil des Testosterons ist an <strong>SHBG</strong> und Albumin gebunden. Nur 1&ndash;3 % zirkulieren als biologisch aktives "
                "<strong>freies Testosteron</strong>.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Testosteronwerte",
            body_html=(
                "<p>Die Werte variieren nach Geschlecht, Alter und Tageszeit (morgens am höchsten). Blut wird vor 10 Uhr abgenommen:</p>"
                "<ul>"
                "<li><strong>Erwachsene Männer:</strong> 300&ndash;1.000 ng/dL (10,4&ndash;34,7 nmol/L)</li>"
                "<li><strong>Erwachsene Frauen:</strong> 15&ndash;70 ng/dL (0,5&ndash;2,4 nmol/L)</li>"
                "</ul>"
                "<p>Bei Männern sinkt Testosteron ab 30 Jahren um ca. 1&ndash;2 % pro Jahr. "
                "Vergleichen Sie immer mit dem Referenzbereich Ihres Laborbefunds.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen abnormaler Testosteronwerte",
            body_html=(
                "<p><strong>Niedriges Testosteron beim Mann (Hypogonadismus):</strong> Alterung, Adipositas, Typ-2-Diabetes, "
                "Hypophysenstörungen, chronische Erkrankungen (Leber, Niere, HIV), Klinefelter-Syndrom und Medikamente (Opioide, Glukokortikoide).</p>"
                "<p><strong>Hohes Testosteron bei Frauen:</strong> <strong>PCOS</strong> ist die häufigste Ursache. "
                "Weitere: Nebennierenstörungen, Ovarialtumoren, anabole Steroide.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome bei abnormalem Testosteron",
            body_html=(
                "<p><strong>Niedrig beim Mann:</strong> Müdigkeit, verminderte Libido, erektile Dysfunktion, Stimmungsschwankungen, "
                "Muskelabbau, Zunahme des Körperfetts, verringerte Knochendichte und Gynäkomastie.</p>"
                "<p><strong>Hoch bei Frauen:</strong> Hirsutismus, Akne, tiefere Stimme, Zyklusunregelmäßigkeiten, "
                "androgenetische Alopezie und Gewichtszunahme. Bei PCOS ist Unfruchtbarkeit häufig.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Ergänzende Untersuchungen",
            body_html=(
                "<p><strong>LH</strong> und <strong>FSH</strong> helfen, primären von sekundärem Hypogonadismus zu unterscheiden. "
                "<strong>SHBG</strong>, <strong>freies Testosteron</strong>, <strong>Prolaktin</strong>, Schilddrüsenfunktion, "
                "Estradiol (bei Männern mit Gynäkomastie) und <strong>DHEA-S</strong>/<strong>17-OH-Progesteron</strong> (bei Frauen) werden je nach Klinik bestimmt.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann zum Arzt?",
            body_html=(
                "<p>Männer sollten bei anhaltender Müdigkeit, Libidoverlust, erektiler Dysfunktion oder Muskelabbau den Arzt aufsuchen. "
                "Die Diagnose erfordert mindestens <strong>zwei morgendliche Blutentnahmen</strong> mit niedrigem Testosteron plus passenden Symptomen.</p>"
                "<p>Frauen sollten bei Hirsutismus, Akne, Zyklusstörungen oder Kinderwunschproblemen den Arzt konsultieren.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihr Testosteron zu verstehen",
            body_html=(
                "<p>Norya stellt keine Diagnosen&mdash;wir helfen bei der Vorbereitung. Laden Sie Ihren Blutbefund unter "
                "<a href=\"/analyze\">noryaai.com/analyze</a> hoch und erhalten Sie eine Zusammenfassung mit Testosteron, LH, FSH und SHBG.</p>"
                "<p>Norya ordnet Ihre Ergebnisse für das Arztgespräch. "
                "Pläne und Preise auf unserer <a href=\"/pricing\">Preisseite</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Haftungsausschluss",
            body_html=(
                '<p><strong>Dieser Ratgeber dient ausschließlich der Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> '
                'Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'
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
            heading="Taux de testostérone : que signifie votre analyse de sang ?",
            body_html=(
                "<p>La testostérone est la principale hormone sexuelle masculine, mais elle joue un rôle chez les deux sexes. "
                "Quand une analyse de sang indique un taux haut ou bas, il est naturel de s&rsquo;interroger sur son impact. "
                "La testostérone influence la masse musculaire, la densité osseuse, la libido et l&rsquo;humeur.</p>"
                "<p>Ce guide explique ce que fait la testostérone, comment interpréter votre résultat, les causes fréquentes de niveaux anormaux, "
                "les symptômes associés et quand consulter. Il est éducatif et ne constitue pas un diagnostic.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu'est-ce que la testostérone et pourquoi est-elle importante ?",
            body_html=(
                "<p><strong>La testostérone</strong> est un androgène produit principalement par les cellules de Leydig des testicules (hommes) "
                "et en moindre quantité par les ovaires et les surrénales (femmes). Sa production est régulée par l&rsquo;<strong>axe HPG</strong>. "
                "Chez l&rsquo;homme, elle favorise les caractères sexuels secondaires, la spermatogenèse et le maintien de la masse osseuse et musculaire. "
                "Chez la femme, elle contribue à la libido et à la santé osseuse.</p>"
                "<p>La majorité est liée à la <strong>SHBG</strong> et à l&rsquo;albumine ; seuls 1&ndash;3 % circulent sous forme de "
                "<strong>testostérone libre</strong>, biologiquement active.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de la testostérone",
            body_html=(
                "<p>Les niveaux varient selon le sexe, l&rsquo;âge et l&rsquo;heure (pic matinal). Le prélèvement se fait avant 10 h :</p>"
                "<ul>"
                "<li><strong>Hommes adultes :</strong> 300&ndash;1 000 ng/dL (10,4&ndash;34,7 nmol/L)</li>"
                "<li><strong>Femmes adultes :</strong> 15&ndash;70 ng/dL (0,5&ndash;2,4 nmol/L)</li>"
                "</ul>"
                "<p>Chez l&rsquo;homme, la testostérone diminue d&rsquo;environ 1&ndash;2 % par an après 30 ans. "
                "Comparez toujours votre résultat à la plage de votre compte-rendu.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une testostérone anormale",
            body_html=(
                "<p><strong>Testostérone basse chez l&rsquo;homme (hypogonadisme) :</strong> vieillissement, obésité, diabète de type 2, "
                "troubles hypophysaires, maladies chroniques, syndrome de Klinefelter et médicaments (opioïdes, corticoïdes).</p>"
                "<p><strong>Testostérone élevée chez la femme :</strong> <strong>SOPK</strong> (la cause la plus fréquente), "
                "troubles surrénaliens, tumeurs ovariennes et stéroïdes anabolisants.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d'une testostérone anormale",
            body_html=(
                "<p><strong>Basse chez l&rsquo;homme :</strong> fatigue, baisse de la libido, dysfonction érectile, troubles de l&rsquo;humeur, "
                "perte musculaire, augmentation de la masse grasse et gynécomastie.</p>"
                "<p><strong>Élevée chez la femme :</strong> hirsutisme, acné, voix plus grave, irrégularités menstruelles, "
                "alopécie androgénique et prise de poids. Le SOPK s&rsquo;accompagne souvent de difficultés de conception.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens complémentaires",
            body_html=(
                "<p><strong>LH</strong> et <strong>FSH</strong> distinguent hypogonadisme primaire et secondaire. "
                "<strong>SHBG</strong>, <strong>testostérone libre</strong>, <strong>prolactine</strong>, bilan thyroïdien, "
                "estradiol et <strong>DHEA-S</strong>/<strong>17-OH-progestérone</strong> complètent le bilan selon le contexte.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Les hommes doivent consulter en cas de fatigue persistante, baisse de libido, dysfonction érectile ou perte musculaire. "
                "Le diagnostic d&rsquo;hypogonadisme nécessite <strong>deux prélèvements matinaux</strong> montrant une testostérone basse avec symptômes.</p>"
                "<p>Les femmes doivent consulter en cas d&rsquo;hirsutisme, d&rsquo;acné, d&rsquo;irrégularités menstruelles ou de difficultés à concevoir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre votre testostérone",
            body_html=(
                "<p>Norya ne pose pas de diagnostic&mdash;nous vous aidons à vous préparer. Téléversez votre bilan sur "
                "<a href=\"/analyze\">noryaai.com/analyze</a> et recevez un résumé clair avec testostérone, LH, FSH et SHBG.</p>"
                "<p>Norya organise vos résultats pour l&rsquo;échange avec votre médecin. "
                "Formules et tarifs sur notre <a href=\"/pricing\">page tarifs</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis médical ou un diagnostic.</strong> '
                'Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'
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
            heading="Livelli di testosterone: cosa significa il tuo esame del sangue",
            body_html=(
                "<p>Il testosterone è il principale ormone sessuale maschile, ma svolge un ruolo in entrambi i sessi. "
                "Quando un&rsquo;analisi del sangue segnala il testosterone come alto o basso, è naturale chiedersi cosa significhi. "
                "Il testosterone influenza massa muscolare, densità ossea, distribuzione del grasso, libido e umore.</p>"
                "<p>Questa guida spiega cosa fa il testosterone, come interpretare il risultato, le cause comuni di valori anomali, "
                "i sintomi associati e quando consultare il medico. È a scopo educativo, non diagnostico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Cos'è il testosterone e perché è importante?",
            body_html=(
                "<p><strong>Il testosterone</strong> è un androgeno prodotto dalle cellule di Leydig nei testicoli (uomini) "
                "e in quantità minore da ovaie e surreni (donne). La regolazione avviene tramite l&rsquo;<strong>asse HPG</strong>. "
                "Nell&rsquo;uomo promuove i caratteri sessuali secondari, la spermatogenesi e il mantenimento di massa ossea e muscolare. "
                "Nella donna contribuisce a libido e salute ossea.</p>"
                "<p>La maggior parte è legata a <strong>SHBG</strong> e albumina; solo l&rsquo;1&ndash;3 % circola come "
                "<strong>testosterone libero</strong>, la forma biologicamente attiva.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del testosterone",
            body_html=(
                "<p>I livelli variano per sesso, età e ora del giorno (picco mattutino). Il prelievo si esegue prima delle 10:</p>"
                "<ul>"
                "<li><strong>Uomini adulti:</strong> 300&ndash;1.000 ng/dL (10,4&ndash;34,7 nmol/L)</li>"
                "<li><strong>Donne adulte:</strong> 15&ndash;70 ng/dL (0,5&ndash;2,4 nmol/L)</li>"
                "</ul>"
                "<p>Negli uomini, il testosterone cala di circa 1&ndash;2 % all&rsquo;anno dopo i 30. "
                "Confronta il risultato con l&rsquo;intervallo del referto.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause del testosterone anomalo",
            body_html=(
                "<p><strong>Basso nell&rsquo;uomo (ipogonadismo):</strong> invecchiamento, obesità, diabete tipo 2, "
                "disturbi ipofisari, malattie croniche, sindrome di Klinefelter e farmaci (oppioidi, corticosteroidi).</p>"
                "<p><strong>Alto nella donna:</strong> <strong>PCOS</strong> è la causa più frequente. "
                "Altre: disturbi surrenalici, tumori ovarici, steroidi anabolizzanti.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi del testosterone anomalo",
            body_html=(
                "<p><strong>Basso nell&rsquo;uomo:</strong> stanchezza, calo della libido, disfunzione erettile, "
                "alterazioni dell&rsquo;umore, perdita muscolare, aumento del grasso corporeo e ginecomastia.</p>"
                "<p><strong>Alto nella donna:</strong> irsutismo, acne, voce più grave, irregolarità mestruali, "
                "alopecia androgenetica e aumento di peso. Nella PCOS, l&rsquo;infertilità è frequente.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p><strong>LH</strong> e <strong>FSH</strong> distinguono ipogonadismo primario e secondario. "
                "<strong>SHBG</strong>, <strong>testosterone libero</strong>, <strong>prolattina</strong>, funzione tiroidea, "
                "estradiolo e <strong>DHEA-S</strong>/<strong>17-OH-progesterone</strong> completano il quadro clinico.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico",
            body_html=(
                "<p>Gli uomini dovrebbero consultare il medico in caso di stanchezza persistente, calo della libido, disfunzione erettile "
                "o perdita muscolare. La diagnosi di ipogonadismo richiede almeno <strong>due prelievi mattutini</strong> con testosterone basso e sintomi compatibili.</p>"
                "<p>Le donne dovrebbero consultare in caso di irsutismo, acne, irregolarità mestruali o difficoltà a concepire.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a capire il tuo testosterone",
            body_html=(
                "<p>Norya non fa diagnosi&mdash;ti aiuta a prepararti. Carica le tue analisi su "
                "<a href=\"/analyze\">noryaai.com/analyze</a> e ricevi un riepilogo con testosterone, LH, FSH e SHBG.</p>"
                "<p>Norya organizza i tuoi risultati per il dialogo con il medico. "
                "Piani e prezzi sulla nostra <a href=\"/pricing\">pagina prezzi</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza",
            body_html=(
                '<p><strong>Questa guida ha finalità esclusivamente informative e non sostituisce il parere medico o la diagnosi.</strong> '
                'Discuti sempre i tuoi risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'
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
            heading="רמות טסטוסטרון: מה המשמעות של בדיקת הדם שלך",
            body_html=(
                "<p>טסטוסטרון הוא הורמון המין הגברי העיקרי, אך הוא ממלא תפקידים חשובים גם בנשים. "
                "כאשר בדיקת דם מסמנת טסטוסטרון גבוה או נמוך, טבעי לתהות מה זה אומר על בריאותכם. "
                "טסטוסטרון משפיע על מסת שריר, צפיפות עצם, חלוקת שומן, ליבידו ומצב רוח.</p>"
                "<p>מדריך זה מסביר מה טסטוסטרון עושה, כיצד לקרוא את התוצאה, גורמים שכיחים לרמות חריגות, "
                "תסמינים קשורים ומתי לפנות לרופא. הוא חינוכי ואינו מהווה אבחנה&mdash;"
                "שוחחו תמיד עם רופא על התוצאות שלכם.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהו טסטוסטרון ולמה הוא חשוב?",
            body_html=(
                "<p><strong>טסטוסטרון</strong> הוא הורמון אנדרוגני המיוצר בעיקר בתאי ליידיג באשכים (גברים) "
                "ובכמויות קטנות יותר בשחלות ובבלוטות האדרנל (נשים). הוויסות נעשה דרך <strong>ציר HPG</strong>. "
                "בגברים הוא מניע התפתחות מאפיינים מיניים משניים, ספרמטוגנזה ושמירה על מסת עצם ושריר. "
                "בנשים הוא תורם לליבידו ולחוזק העצמות.</p>"
                "<p>רוב הטסטוסטרון קשור ל<strong>SHBG</strong> ואלבומין; רק 1&ndash;3% מסתובב כ<strong>טסטוסטרון חופשי</strong>, "
                "הצורה הפעילה ביולוגית.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי טסטוסטרון תקינים",
            body_html=(
                "<p>הרמות משתנות לפי מין, גיל ושעה ביום (שיא בבוקר). דם נלקח לפני 10:00:</p>"
                "<ul>"
                "<li><strong>גברים בוגרים:</strong> 300&ndash;1,000 ng/dL (10.4&ndash;34.7 nmol/L)</li>"
                "<li><strong>נשים בוגרות:</strong> 15&ndash;70 ng/dL (0.5&ndash;2.4 nmol/L)</li>"
                "</ul>"
                "<p>בגברים, טסטוסטרון יורד בערך 1&ndash;2% בשנה אחרי גיל 30. "
                "השוו תמיד את התוצאה לטווח בדוח המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לטסטוסטרון חריג",
            body_html=(
                "<p><strong>נמוך בגברים (היפוגונדיזם):</strong> הזדקנות, השמנת יתר, סוכרת סוג 2, "
                "הפרעות בהיפופיזה, מחלות כרוניות (כבד, כליות, HIV), תסמונת קליינפלטר ותרופות (אופיואידים, גלוקוקורטיקואידים).</p>"
                "<p><strong>גבוה בנשים:</strong> <strong>PCOS</strong> הוא הגורם השכיח ביותר. "
                "גורמים נוספים: הפרעות אדרנל, גידולי שחלה, סטרואידים אנבוליים.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של טסטוסטרון חריג",
            body_html=(
                "<p><strong>נמוך בגברים:</strong> עייפות, ירידה בליבידו, הפרעת זיקפה, שינויי מצב רוח, "
                "אובדן מסת שריר, עלייה בשומן גוף וגינקומסטיה.</p>"
                "<p><strong>גבוה בנשים:</strong> שעירות יתר, אקנה, קול עמוק יותר, אי-סדירות במחזור, "
                "התקרחות אנדרוגנית ועלייה במשקל. ב-PCOS, אי-פוריות שכיחה.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות נלוות",
            body_html=(
                "<p><strong>LH</strong> ו-<strong>FSH</strong> מבדילים בין היפוגונדיזם ראשוני למשני. "
                "<strong>SHBG</strong>, <strong>טסטוסטרון חופשי</strong>, <strong>פרולקטין</strong>, תפקוד תריס, "
                "אסטרדיול ו-<strong>DHEA-S</strong>/<strong>17-OH-progesterone</strong> משלימים את הבירור.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>גברים צריכים לפנות לרופא בעייפות מתמשכת, ירידה בליבידו, הפרעת זיקפה או אובדן מסת שריר. "
                "אבחנת היפוגונדיזם דורשת לפחות <strong>שתי דגימות דם בוקר</strong> עם טסטוסטרון נמוך ותסמינים תואמים.</p>"
                "<p>נשים צריכות לפנות בשעירות יתר, אקנה, אי-סדירות במחזור או קושי להיכנס להריון.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת לכם להבין את הטסטוסטרון",
            body_html=(
                "<p>Norya לא מאבחנת&mdash;אנחנו עוזרים לכם להתכונן. העלו את הדוח ב-"
                "<a href=\"/analyze\">noryaai.com/analyze</a> וקבלו סיכום ברור עם טסטוסטרון, LH, FSH ו-SHBG.</p>"
                "<p>Norya מארגנת את התוצאות לקראת השיחה עם הרופא. "
                "לאפשרויות מנוי ומחירים: <a href=\"/pricing\">עמוד המחירים</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הבהרה",
            body_html=(
                '<p><strong>מדריך זה מיועד למטרות מידע בלבד ואינו מהווה תחליף לייעוץ רפואי או אבחנה.</strong> '
                'שוחחו תמיד עם רופא על התוצאות שלכם. <a href="/analyze">התחילו ניתוח עם Norya</a></p>'
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
            heading="टेस्टोस्टेरोन स्तर: आपकी ब्लड टेस्ट रिपोर्ट का क्या मतलब है",
            body_html=(
                "<p>टेस्टोस्टेरोन प्राथमिक पुरुष सेक्स हार्मोन है, लेकिन यह पुरुषों और महिलाओं दोनों में महत्वपूर्ण भूमिका निभाता है। "
                "जब ब्लड टेस्ट आपके टेस्टोस्टेरोन को उच्च या निम्न दिखाता है, तो यह जानना स्वाभाविक है कि इसका स्वास्थ्य पर क्या प्रभाव है। "
                "टेस्टोस्टेरोन मांसपेशी, हड्डी घनत्व, वसा वितरण, लिबिडो और मूड को प्रभावित करता है।</p>"
                "<p>यह गाइड बताती है कि टेस्टोस्टेरोन क्या करता है, रिजल्ट कैसे पढ़ें, असामान्य स्तरों के कारण, "
                "संबंधित लक्षण और डॉक्टर से कब मिलें। यह शैक्षिक है, निदान नहीं&mdash;अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="टेस्टोस्टेरोन क्या है और यह क्यों महत्वपूर्ण है?",
            body_html=(
                "<p><strong>टेस्टोस्टेरोन</strong> एक एंड्रोजन हार्मोन है जो पुरुषों में मुख्य रूप से अंडकोष की लेडिग कोशिकाओं में "
                "और महिलाओं में कम मात्रा में अंडाशय और एड्रेनल ग्रंथियों में बनता है। इसका उत्पादन <strong>HPG एक्सिस</strong> द्वारा नियंत्रित होता है। "
                "पुरुषों में यह द्वितीयक यौन विशेषताओं, शुक्राणु उत्पादन और हड्डी-मांसपेशी संरक्षण को बढ़ावा देता है। "
                "महिलाओं में यह लिबिडो और हड्डी की मजबूती में योगदान देता है।</p>"
                "<p>अधिकांश टेस्टोस्टेरोन <strong>SHBG</strong> और एल्बुमिन से बंधा होता है; केवल 1&ndash;3% <strong>फ्री टेस्टोस्टेरोन</strong> "
                "के रूप में होता है जो बायोलॉजिकली एक्टिव है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य टेस्टोस्टेरोन रेंज",
            body_html=(
                "<p>स्तर लिंग, उम्र और दिन के समय (सुबह चरम) के अनुसार बदलते हैं। ब्लड सुबह 10 AM से पहले लिया जाता है:</p>"
                "<ul>"
                "<li><strong>वयस्क पुरुष:</strong> 300&ndash;1,000 ng/dL (10.4&ndash;34.7 nmol/L)</li>"
                "<li><strong>वयस्क महिलाएँ:</strong> 15&ndash;70 ng/dL (0.5&ndash;2.4 nmol/L)</li>"
                "</ul>"
                "<p>पुरुषों में 30 की उम्र के बाद टेस्टोस्टेरोन सालाना ~1&ndash;2% गिरता है। "
                "अपने रिजल्ट की तुलना हमेशा अपनी लैब रिपोर्ट की रेंज से करें।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="असामान्य टेस्टोस्टेरोन के कारण",
            body_html=(
                "<p><strong>पुरुषों में कम (हाइपोगोनेडिज़्म):</strong> उम्र बढ़ना, मोटापा, टाइप 2 डायबिटीज़, "
                "पिट्यूटरी विकार, क्रोनिक बीमारी (लिवर, किडनी, HIV), क्लाइनफेल्टर सिंड्रोम "
                "और दवाएँ (ओपिओइड, ग्लूकोकोर्टिकोइड)।</p>"
                "<p><strong>महिलाओं में अधिक:</strong> <strong>PCOS</strong> सबसे आम कारण है। "
                "अन्य: एड्रेनल विकार, ओवेरियन ट्यूमर, एनाबॉलिक स्टेरॉइड।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="असामान्य टेस्टोस्टेरोन के लक्षण",
            body_html=(
                "<p><strong>पुरुषों में कम:</strong> थकान, कम लिबिडो, इरेक्टाइल डिसफंक्शन, मूड बदलाव, "
                "मांसपेशी कम होना, शरीर में वसा बढ़ना और गाइनेकोमैस्टिया।</p>"
                "<p><strong>महिलाओं में अधिक:</strong> हिर्सुटिज़्म (अतिरिक्त बाल), एक्ने, आवाज़ गहरी होना, "
                "अनियमित पीरियड्स, पुरुष-पैटर्न बाल झड़ना और वज़न बढ़ना। PCOS में बांझपन एक आम चिंता है।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित जाँचें",
            body_html=(
                "<p><strong>LH</strong> और <strong>FSH</strong> प्राइमरी व सेकेंडरी हाइपोगोनेडिज़्म में अंतर करते हैं। "
                "<strong>SHBG</strong>, <strong>फ्री टेस्टोस्टेरोन</strong>, <strong>प्रोलैक्टिन</strong>, थायरॉइड फंक्शन, "
                "एस्ट्राडियोल और <strong>DHEA-S</strong>/<strong>17-OH-प्रोजेस्टेरोन</strong> क्लिनिकल संदर्भ के अनुसार मँगवाए जा सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>पुरुषों को लगातार थकान, कम लिबिडो, इरेक्टाइल डिसफंक्शन या मांसपेशी कम होने पर डॉक्टर से मिलना चाहिए। "
                "हाइपोगोनेडिज़्म के निदान के लिए कम से कम <strong>दो सुबह के ब्लड सैंपल</strong> में कम टेस्टोस्टेरोन और मिलते-जुलते लक्षण ज़रूरी हैं।</p>"
                "<p>महिलाओं को अतिरिक्त बालों, एक्ने, अनियमित पीरियड्स या गर्भधारण में कठिनाई होने पर डॉक्टर से मिलना चाहिए।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके टेस्टोस्टेरोन को समझने में कैसे मदद करता है",
            body_html=(
                "<p>Norya निदान नहीं करता&mdash;हम आपको तैयार होने में मदद करते हैं। अपनी ब्लड रिपोर्ट "
                "<a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें और टेस्टोस्टेरोन, LH, FSH व SHBG सहित स्पष्ट सारांश प्राप्त करें।</p>"
                "<p>Norya आपके परिणामों को व्यवस्थित करता है ताकि आप डॉक्टर से बातचीत पर ध्यान दे सकें। "
                "प्लान व मूल्य के लिए <a href=\"/pricing\">प्राइसिंग पेज</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचना के उद्देश्य से है और चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> '
                'अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya के साथ विश्लेषण शुरू करें</a></p>'
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
            heading="مستويات التستوستيرون: ماذا يعني تحليل الدم الخاص بك",
            body_html=(
                "<p>التستوستيرون هو الهرمون الجنسي الذكوري الرئيسي لكنه يلعب أدواراً مهمة عند الجنسين. "
                "عندما يشير تحليل الدم إلى تستوستيرون مرتفع أو منخفض، من الطبيعي التساؤل عن المعنى الصحي. "
                "يؤثر التستوستيرون على الكتلة العضلية وكثافة العظام وتوزيع الدهون والرغبة الجنسية والمزاج.</p>"
                "<p>يشرح هذا الدليل ما يفعله التستوستيرون وكيفية قراءة النتيجة والأسباب الشائعة لمستويات غير طبيعية "
                "والأعراض المرتبطة ومتى يجب مراجعة الطبيب. هو تثقيفي وليس تشخيصياً.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو التستوستيرون ولماذا هو مهم؟",
            body_html=(
                "<p><strong>التستوستيرون</strong> هو هرمون أندروجيني يُنتَج بشكل رئيسي في خلايا ليدغ بالخصيتين (رجال) "
                "وبكميات أقل في المبيضين والغدد الكظرية (نساء). تنظيمه يتم عبر <strong>محور HPG</strong>. "
                "عند الرجل يحفّز الصفات الجنسية الثانوية وتكوين الحيوانات المنوية وصيانة العظام والعضلات. "
                "عند المرأة يساهم في الرغبة الجنسية وقوة العظام.</p>"
                "<p>معظم التستوستيرون مرتبط بـ<strong>SHBG</strong> والألبومين؛ 1&ndash;3% فقط يدور بشكل "
                "<strong>تستوستيرون حر</strong>، الشكل الفعّال بيولوجياً.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="نطاقات التستوستيرون الطبيعية",
            body_html=(
                "<p>المستويات تختلف حسب الجنس والعمر والوقت (ذروة صباحية). يُسحب الدم قبل 10 صباحاً:</p>"
                "<ul>"
                "<li><strong>رجال بالغون:</strong> 300&ndash;1,000 ng/dL (10.4&ndash;34.7 nmol/L)</li>"
                "<li><strong>نساء بالغات:</strong> 15&ndash;70 ng/dL (0.5&ndash;2.4 nmol/L)</li>"
                "</ul>"
                "<p>عند الرجال ينخفض التستوستيرون ~1&ndash;2% سنوياً بعد سن 30. "
                "قارن دائماً نتيجتك بنطاق تقرير مختبرك.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب التستوستيرون غير الطبيعي",
            body_html=(
                "<p><strong>منخفض عند الرجال (قصور الغدد التناسلية):</strong> التقدم في العمر، السمنة، السكري من النوع 2، "
                "اضطرابات النخامية، أمراض مزمنة (كبد، كلى، HIV)، متلازمة كلاينفلتر وأدوية (مسكنات أفيونية، كورتيكوستيرويدات).</p>"
                "<p><strong>مرتفع عند النساء:</strong> <strong>متلازمة المبيض متعدد الكيسات (PCOS)</strong> هو الأكثر شيوعاً. "
                "أسباب أخرى: اضطرابات كظرية، أورام مبيضية، ستيرويدات بنائية.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض التستوستيرون غير الطبيعي",
            body_html=(
                "<p><strong>منخفض عند الرجال:</strong> إرهاق، انخفاض الرغبة الجنسية، ضعف الانتصاب، "
                "تقلبات مزاجية، فقدان الكتلة العضلية، زيادة الدهون وتثدّي.</p>"
                "<p><strong>مرتفع عند النساء:</strong> شعرانية، حب شباب، تغلّظ الصوت، عدم انتظام الدورة، "
                "تساقط شعر أندروجيني وزيادة في الوزن. في PCOS، العقم شائع.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="فحوصات ذات صلة",
            body_html=(
                "<p><strong>LH</strong> و<strong>FSH</strong> يميّزان بين قصور أولي وثانوي. "
                "<strong>SHBG</strong>، <strong>تستوستيرون حر</strong>، <strong>برولاكتين</strong>، وظائف الغدة الدرقية، "
                "استراديول و<strong>DHEA-S</strong>/<strong>17-OH-progesterone</strong> تكمل الصورة حسب السياق السريري.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب؟",
            body_html=(
                "<p>يجب على الرجال مراجعة الطبيب عند إرهاق مستمر أو انخفاض الرغبة الجنسية أو ضعف الانتصاب أو فقدان الكتلة العضلية. "
                "تشخيص قصور الغدد التناسلية يتطلب <strong>عيّنتي دم صباحيتين</strong> على الأقل مع تستوستيرون منخفض وأعراض متوافقة.</p>"
                "<p>يجب على النساء المراجعة عند شعرانية أو حب شباب أو عدم انتظام الدورة أو صعوبة في الحمل.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم التستوستيرون",
            body_html=(
                "<p>Norya لا تُشخّص&mdash;نحن نساعدك على الاستعداد. ارفع تقريرك على "
                "<a href=\"/analyze\">noryaai.com/analyze</a> واحصل على ملخص واضح يشمل التستوستيرون وLH وFSH وSHBG.</p>"
                "<p>تنظّم Norya نتائجك لتحضيرك لموعد الطبيب. "
                "لخيارات الاشتراك والأسعار: <a href=\"/pricing\">صفحة الأسعار</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء مسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض تثقيفية فقط ولا يحل محل الاستشارة الطبية أو التشخيص.</strong> '
                'ناقش نتائجك دائماً مع طبيب مختص. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


# ============================================================================
# Public API
# ============================================================================

def get_testosterone_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for testosterone article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_testosterone_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for testosterone article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal testosterone level for men?",
             "answer": "Normal total testosterone for adult men is roughly 300–1,000 ng/dL (10.4–34.7 nmol/L). Levels peak in the morning and decline with age—about 1–2% per year after age 30."},
            {"question": "What causes low testosterone in men?",
             "answer": "Common causes include aging, obesity, type 2 diabetes, pituitary disorders, chronic illness (liver, kidney, HIV), Klinefelter syndrome, and medications like opioids and glucocorticoids."},
            {"question": "What causes high testosterone in women?",
             "answer": "Polycystic ovary syndrome (PCOS) is the most common cause. Other causes include adrenal disorders (congenital adrenal hyperplasia, adrenal tumours), ovarian tumours, and anabolic steroids."},
            {"question": "What are symptoms of low testosterone?",
             "answer": "In men: fatigue, decreased libido, erectile dysfunction, mood changes, loss of muscle mass, increased body fat, reduced bone density, and sometimes gynecomastia. Symptoms often develop gradually."},
        ],
        "tr": [
            {"question": "Erkeklerde normal testosteron değeri nedir?",
             "answer": "Yetişkin erkeklerde normal total testosteron yaklaşık 300–1.000 ng/dL'dir (10,4–34,7 nmol/L). Düzeyler sabah en yüksektir ve 30 yaşından sonra yılda ~%1–2 düşer."},
            {"question": "Erkeklerde testosteron düşüklüğünün nedenleri nelerdir?",
             "answer": "Yaygın nedenler: yaşlanma, obezite, tip 2 diyabet, hipofiz bozuklukları, kronik hastalık, Klinefelter sendromu ve opioidler veya glukokortikoidler gibi ilaçlar."},
            {"question": "Kadınlarda testosteron yüksekliğinin nedenleri nelerdir?",
             "answer": "Polikistik over sendromu (PKOS) en yaygın nedendir. Diğerleri: adrenal bozukluklar, over tümörleri ve anabolik steroidler."},
            {"question": "Düşük testosteron belirtileri nelerdir?",
             "answer": "Erkeklerde: yorgunluk, azalmış libido, erektil disfonksiyon, ruh hali değişiklikleri, kas kütlesi kaybı, vücut yağı artışı ve bazen jinekomasti."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de testosterona en hombres?",
             "answer": "La testosterona total normal en hombres adultos es aproximadamente 300–1.000 ng/dL (10,4–34,7 nmol/L). Los niveles alcanzan su pico por la mañana y disminuyen con la edad."},
            {"question": "¿Qué causa la testosterona baja en hombres?",
             "answer": "Envejecimiento, obesidad, diabetes tipo 2, trastornos hipofisarios, enfermedades crónicas, síndrome de Klinefelter y medicamentos como opioides y glucocorticoides."},
            {"question": "¿Qué causa la testosterona alta en mujeres?",
             "answer": "El SOP (síndrome de ovario poliquístico) es la causa más frecuente. Otras: trastornos suprarrenales, tumores ováricos y esteroides anabólicos."},
            {"question": "¿Cuáles son los síntomas de testosterona baja?",
             "answer": "En hombres: fatiga, disminución de la libido, disfunción eréctil, cambios de humor, pérdida muscular y aumento de grasa corporal."},
        ],
        "de": [
            {"question": "Was ist ein normaler Testosteronwert für Männer?",
             "answer": "Normales Gesamttestosteron: ca. 300–1.000 ng/dL (10,4–34,7 nmol/L). Die Spiegel sind morgens am höchsten und sinken ab 30 um ~1–2 % pro Jahr."},
            {"question": "Was verursacht niedrigen Testosteronspiegel beim Mann?",
             "answer": "Alterung, Adipositas, Typ-2-Diabetes, Hypophysenstörungen, chronische Erkrankungen, Klinefelter-Syndrom und Medikamente (Opioide, Glukokortikoide)."},
            {"question": "Was verursacht hohen Testosteronspiegel bei Frauen?",
             "answer": "PCOS ist die häufigste Ursache. Weitere: Nebennierenstörungen, Ovarialtumoren und anabole Steroide."},
            {"question": "Was sind Symptome von niedrigem Testosteron?",
             "answer": "Müdigkeit, verminderte Libido, erektile Dysfunktion, Stimmungsschwankungen, Muskelabbau, Zunahme des Körperfetts und Gynäkomastie."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de testostérone chez l'homme ?",
             "answer": "La testostérone totale normale est d'environ 300–1 000 ng/dL (10,4–34,7 nmol/L). Les taux sont maximaux le matin et diminuent avec l'âge."},
            {"question": "Quelles sont les causes d'une testostérone basse chez l'homme ?",
             "answer": "Vieillissement, obésité, diabète de type 2, troubles hypophysaires, maladies chroniques, syndrome de Klinefelter et médicaments (opioïdes, corticoïdes)."},
            {"question": "Quelles sont les causes d'une testostérone élevée chez la femme ?",
             "answer": "Le SOPK est la cause la plus fréquente. Autres : troubles surrénaliens, tumeurs ovariennes et stéroïdes anabolisants."},
            {"question": "Quels sont les symptômes d'une testostérone basse ?",
             "answer": "Chez l'homme : fatigue, baisse de la libido, dysfonction érectile, troubles de l'humeur, perte musculaire et augmentation de la masse grasse."},
        ],
        "it": [
            {"question": "Qual è il valore normale del testosterone nell'uomo?",
             "answer": "Il testosterone totale normale è circa 300–1.000 ng/dL (10,4–34,7 nmol/L). I livelli sono massimi al mattino e diminuiscono con l'età."},
            {"question": "Cosa causa il testosterone basso nell'uomo?",
             "answer": "Invecchiamento, obesità, diabete tipo 2, disturbi ipofisari, malattie croniche, sindrome di Klinefelter e farmaci (oppioidi, corticosteroidi)."},
            {"question": "Cosa causa il testosterone alto nella donna?",
             "answer": "La PCOS è la causa più frequente. Altre: disturbi surrenalici, tumori ovarici e steroidi anabolizzanti."},
            {"question": "Quali sono i sintomi del testosterone basso?",
             "answer": "Nell'uomo: stanchezza, calo della libido, disfunzione erettile, alterazioni dell'umore, perdita muscolare e aumento del grasso corporeo."},
        ],
        "he": [
            {"question": "מהו ערך טסטוסטרון תקין לגברים?",
             "answer": "טסטוסטרון כולל תקין לגברים: כ-300–1,000 ng/dL (10.4–34.7 nmol/L). הרמות גבוהות ביותר בבוקר ויורדות עם הגיל."},
            {"question": "מה גורם לטסטוסטרון נמוך בגברים?",
             "answer": "הזדקנות, השמנת יתר, סוכרת סוג 2, הפרעות בהיפופיזה, מחלות כרוניות, תסמונת קליינפלטר ותרופות (אופיואידים, גלוקוקורטיקואידים)."},
            {"question": "מה גורם לטסטוסטרון גבוה בנשים?",
             "answer": "PCOS הוא הגורם השכיח ביותר. גורמים נוספים: הפרעות אדרנל, גידולי שחלה וסטרואידים אנבוליים."},
            {"question": "מהם התסמינים של טסטוסטרון נמוך?",
             "answer": "בגברים: עייפות, ירידה בליבידו, הפרעת זיקפה, שינויי מצב רוח, אובדן מסת שריר, עלייה בשומן גוף וגינקומסטיה."},
        ],
        "hi": [
            {"question": "पुरुषों में सामान्य टेस्टोस्टेरोन कितना होना चाहिए?",
             "answer": "वयस्क पुरुषों में सामान्य टोटल टेस्टोस्टेरोन लगभग 300–1,000 ng/dL (10.4–34.7 nmol/L) है। स्तर सुबह सबसे अधिक होते हैं और 30 के बाद सालाना ~1–2% गिरते हैं।"},
            {"question": "पुरुषों में टेस्टोस्टेरोन कम होने के कारण क्या हैं?",
             "answer": "उम्र बढ़ना, मोटापा, टाइप 2 डायबिटीज़, पिट्यूटरी विकार, क्रोनिक बीमारी, क्लाइनफेल्टर सिंड्रोम और दवाएँ (ओपिओइड, ग्लूकोकोर्टिकोइड)।"},
            {"question": "महिलाओं में टेस्टोस्टेरोन बढ़ने के कारण क्या हैं?",
             "answer": "PCOS सबसे आम कारण है। अन्य: एड्रेनल विकार, ओवेरियन ट्यूमर और एनाबॉलिक स्टेरॉइड।"},
            {"question": "कम टेस्टोस्टेरोन के लक्षण क्या हैं?",
             "answer": "पुरुषों में: थकान, कम लिबिडो, इरेक्टाइल डिसफंक्शन, मूड बदलाव, मांसपेशी कम होना, शरीर में वसा बढ़ना और गाइनेकोमैस्टिया।"},
        ],
        "ar": [
            {"question": "ما هو مستوى التستوستيرون الطبيعي للرجال؟",
             "answer": "التستوستيرون الكلي الطبيعي للرجال البالغين حوالي 300–1,000 ng/dL (10.4–34.7 nmol/L). المستويات تكون أعلى صباحاً وتنخفض مع التقدم في العمر."},
            {"question": "ما أسباب انخفاض التستوستيرون عند الرجال؟",
             "answer": "التقدم في العمر، السمنة، السكري من النوع 2، اضطرابات النخامية، أمراض مزمنة، متلازمة كلاينفلتر وأدوية (مسكنات أفيونية، كورتيكوستيرويدات)."},
            {"question": "ما أسباب ارتفاع التستوستيرون عند النساء؟",
             "answer": "متلازمة المبيض متعدد الكيسات (PCOS) هي الأكثر شيوعاً. أسباب أخرى: اضطرابات كظرية، أورام مبيضية وستيرويدات بنائية."},
            {"question": "ما أعراض انخفاض التستوستيرون؟",
             "answer": "عند الرجال: إرهاق، انخفاض الرغبة الجنسية، ضعف الانتصاب، تقلبات مزاجية، فقدان الكتلة العضلية، زيادة الدهون وتثدّي."},
        ],
    }
