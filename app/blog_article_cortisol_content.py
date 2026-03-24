# -*- coding: utf-8 -*-
"""
Cortisol blog article — full body content for all 9 languages.
Used by blog_i18n._article_cortisol().
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
            heading="Cortisol levels: what your blood test result means",
            body_html=(
                "<p>Cortisol is often called the <em>stress hormone</em> because it surges when your body perceives a threat, "
                "but its role goes far beyond the fight-or-flight response. Cortisol helps regulate blood sugar, blood pressure, "
                "immune function, and metabolism around the clock. A cortisol blood test is ordered when your doctor suspects "
                "either too much or too little of this vital hormone.</p>"
                "<p>This guide explains what cortisol does, how to read your result, the most common causes of abnormal levels, "
                "associated symptoms, and when you should follow up with your doctor. "
                "It is educational content, not a medical diagnosis&mdash;always discuss your results with a healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is cortisol and why does it matter?",
            body_html=(
                "<p><strong>Cortisol</strong> is a glucocorticoid hormone produced by the adrenal glands, which sit on top of each kidney. "
                "Its secretion is controlled by the <strong>hypothalamic-pituitary-adrenal (HPA) axis</strong>: the hypothalamus releases CRH, "
                "which stimulates the pituitary to secrete <strong>ACTH</strong>, which in turn tells the adrenal cortex to produce cortisol. "
                "Cortisol then feeds back to suppress CRH and ACTH, creating a tightly regulated loop.</p>"
                "<p>Cortisol follows a <strong>diurnal rhythm</strong>: levels peak in the early morning (around 6&ndash;8 AM) to help you wake up "
                "and gradually decline throughout the day, reaching their lowest point around midnight. "
                "This rhythm is important because the timing of the blood draw affects what is considered &ldquo;normal.&rdquo;</p>"
                "<p>Key functions of cortisol include mobilising glucose from the liver (gluconeogenesis), suppressing non-essential immune responses "
                "during acute stress, maintaining vascular tone and blood pressure, and influencing mood and cognitive function. "
                "Both chronic excess and deficiency of cortisol can have serious health consequences.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal cortisol ranges",
            body_html=(
                "<p>Because of the diurnal rhythm, <strong>morning cortisol (6&ndash;8 AM)</strong> is the standard measurement. "
                "Reference ranges vary between laboratories, but widely accepted values for adults are:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Time of draw</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typical range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Morning (6&ndash;8 AM)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Evening (around 4 PM)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2&ndash;14 &micro;g/dL</td></tr>'
                "</tbody></table>"
                "<p>Stress, illness, certain medications, and even the act of having blood drawn can temporarily raise cortisol. "
                "A single borderline result may not be clinically significant. Your doctor may order repeat testing or dynamic tests "
                "(such as a dexamethasone suppression test or ACTH stimulation test) to clarify the picture.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of abnormal cortisol levels",
            body_html=(
                "<p><strong>High cortisol (hypercortisolism)</strong> can result from several conditions. "
                "<strong>Cushing syndrome</strong> is the classic example: it may be caused by a pituitary adenoma secreting excess ACTH (Cushing disease), "
                "an adrenal tumour producing cortisol autonomously, or ectopic ACTH secretion by a non-pituitary tumour. "
                "The most common cause of Cushing-like features in clinical practice is <strong>exogenous glucocorticoid use</strong>&mdash;"
                "patients taking prednisone, dexamethasone, or similar medications for inflammatory or autoimmune conditions.</p>"
                "<p><strong>Chronic psychological stress</strong>, <strong>depression</strong>, <strong>alcoholism</strong>, "
                "and <strong>severe obesity</strong> can also raise cortisol to abnormal levels (sometimes called &ldquo;pseudo-Cushing&rdquo; states). "
                "These conditions must be distinguished from true Cushing syndrome through careful clinical evaluation and dynamic testing.</p>"
                "<p><strong>Low cortisol (hypocortisolism)</strong> is most commonly caused by <strong>Addison disease</strong> (primary adrenal insufficiency), "
                "in which the adrenal glands are damaged, often by autoimmune destruction. <strong>Secondary adrenal insufficiency</strong> occurs when the pituitary "
                "does not produce enough ACTH, or when long-term exogenous steroid use suppresses the HPA axis and the medication is withdrawn too quickly. "
                "Low cortisol is a medical emergency if severe (adrenal crisis).</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of abnormal cortisol",
            body_html=(
                "<p><strong>High cortisol</strong> symptoms develop gradually and may include <strong>weight gain</strong>&mdash;particularly around the face "
                "(&ldquo;moon face&rdquo;), upper back (&ldquo;buffalo hump&rdquo;), and abdomen&mdash;<strong>high blood pressure</strong>, "
                "<strong>elevated blood sugar</strong> (sometimes progressing to diabetes), <strong>mood changes</strong> (anxiety, irritability, depression), "
                "<strong>thinning skin</strong> with easy bruising, <strong>muscle weakness</strong> (especially in the thighs and upper arms), "
                "purple stretch marks (striae), and <strong>menstrual irregularities</strong> in women. Prolonged hypercortisolism increases the risk of infections and osteoporosis.</p>"
                "<p><strong>Low cortisol</strong> symptoms include <strong>severe fatigue</strong>, <strong>weight loss</strong>, <strong>low blood pressure</strong> "
                "(especially upon standing), <strong>dizziness</strong>, <strong>nausea</strong>, <strong>salt cravings</strong>, "
                "and <strong>darkening of the skin</strong> (hyperpigmentation, characteristic of Addison disease). "
                "An adrenal crisis can present with sudden severe abdominal pain, vomiting, confusion, and shock&mdash;it requires immediate emergency treatment.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests your doctor may order",
            body_html=(
                "<p>A single morning cortisol measurement is a starting point, but further testing is usually needed to confirm a diagnosis. "
                "For suspected <strong>high cortisol</strong>: a <strong>24-hour urinary free cortisol</strong> collection, "
                "a <strong>late-night salivary cortisol</strong> test, and a <strong>low-dose dexamethasone suppression test (DST)</strong> "
                "are standard screening tools. If these are abnormal, imaging (pituitary MRI, adrenal CT) and additional biochemistry (ACTH level, high-dose DST) help localise the cause.</p>"
                "<p>For suspected <strong>low cortisol</strong>: an <strong>ACTH stimulation test (Synacthen test)</strong> is the gold standard. "
                "If the adrenals fail to respond, primary adrenal insufficiency is confirmed. "
                "The doctor will also check <strong>ACTH levels</strong> to distinguish primary from secondary insufficiency, "
                "and may order <strong>glucose</strong>, <strong>electrolytes</strong>, and <strong>thyroid function</strong> tests "
                "because adrenal insufficiency can coexist with other endocrine disorders (polyglandular syndromes).</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Talk to your doctor if your cortisol level is outside the reference range, or if you are experiencing symptoms suggestive of cortisol excess "
                "or deficiency&mdash;such as unexplained weight changes, persistent fatigue, new-onset high blood pressure, easy bruising, or skin darkening.</p>"
                "<p>Seek <strong>emergency</strong> medical care if you experience signs of an adrenal crisis: sudden severe abdominal pain, "
                "vomiting, extreme weakness, confusion, or loss of consciousness. Patients known to have adrenal insufficiency should carry "
                "an emergency hydrocortisone injection and wear a medical alert bracelet.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your cortisol",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare. Upload your blood test report at "
                "<a href=\"/analyze\">noryaai.com/analyze</a> and receive a clear, structured summary that highlights your cortisol level "
                "alongside related markers in plain language. The report flags out-of-range values and provides context "
                "so you can have a more informed conversation with your doctor.</p>"
                "<p>Whether you are investigating unexplained symptoms or monitoring an existing endocrine condition, "
                "Norya organises your results so you can focus on what matters. "
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
            heading="Kortizol seviyesi: kan tahlili sonucunuz ne anlama geliyor?",
            body_html=(
                "<p>Kortizol, vücudunuz bir tehdit algıladığında yükseldiği için sıklıkla <em>stres hormonu</em> olarak anılır; "
                "ancak görevi savaş ya da kaç tepkisinin çok ötesine geçer. Kortizol kan şekerini, kan basıncını, bağışıklık fonksiyonunu "
                "ve metabolizmayı gün boyu düzenlemeye yardımcı olur. Hekiminiz bu hayati hormonun fazla veya eksik olduğundan şüphelendiğinde "
                "kortizol kan testi ister.</p>"
                "<p>Bu rehber kortisolün ne yaptığını, sonucunuzu nasıl okuyacağınızı, anormal düzeylerin yaygın nedenlerini, "
                "ilişkili belirtileri ve ne zaman hekiminize danışmanız gerektiğini açıklar. "
                "Eğitim amaçlıdır, teşhis değildir&mdash;sonuçlarınızı mutlaka bir sağlık profesyoneliyle değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Kortizol nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Kortizol</strong>, her böbreğin üstünde yer alan adrenal bezler tarafından üretilen bir glukokortikoid hormondur. "
                "Salgılanması <strong>hipotalamus-hipofiz-adrenal (HPA) ekseni</strong> tarafından kontrol edilir: hipotalamus CRH salgılar, "
                "hipofiz ACTH üretir, ACTH de adrenal kortekse kortizol üretmesini söyler. Kortizol geri bildirim yoluyla CRH ve ACTH&rsquo;yi baskılayarak "
                "sıkı bir şekilde düzenlenen bir döngü oluşturur.</p>"
                "<p>Kortizol <strong>diürnal ritim</strong> izler: seviyeler sabah erken saatlerde (06:00&ndash;08:00 civarı) zirve yaparak uyanmanıza yardımcı olur "
                "ve gün boyunca kademeli olarak düşerek gece yarısı civarında en düşük noktaya ulaşır. "
                "Bu ritim önemlidir çünkü kan alımının zamanlaması &ldquo;normal&rdquo; kabul edilen değeri etkiler.</p>"
                "<p>Kortisolün temel işlevleri arasında karaciğerden glukoz mobilizasyonu (glukoneogenez), akut stres sırasında gereksiz bağışıklık tepkilerinin baskılanması, "
                "vasküler tonüs ve kan basıncının sürdürülmesi ile ruh hali ve bilişsel fonksiyon üzerindeki etkileri yer alır.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal kortizol aralıkları",
            body_html=(
                "<p>Diürnal ritim nedeniyle <strong>sabah kortizolü (06:00&ndash;08:00)</strong> standart ölçümdür. "
                "Yetişkinler için yaygın kabul gören değerler:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Kan alım zamanı</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tipik aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Sabah (06:00&ndash;08:00)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Akşam (16:00 civarı)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2&ndash;14 &micro;g/dL</td></tr>'
                "</tbody></table>"
                "<p>Stres, hastalık, bazı ilaçlar ve kan alımının kendisi bile kortizolü geçici olarak yükseltebilir. "
                "Tek bir sınır değeri her zaman klinik olarak anlamlı olmayabilir; hekiminiz tekrar test veya dinamik testler isteyebilir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Anormal kortizol düzeylerinin nedenleri",
            body_html=(
                "<p><strong>Yüksek kortizol (hiperkortizolizm)</strong> birçok durumdan kaynaklanabilir. "
                "<strong>Cushing sendromu</strong> klasik örnektir: fazla ACTH salgılayan hipofiz adenomu (Cushing hastalığı), "
                "otonom kortizol üreten adrenal tümör veya hipofiz dışı bir tümörün ektopik ACTH salgılaması neden olabilir. "
                "Klinik pratikte Cushing benzeri bulguların en sık nedeni <strong>eksojen glukokortikoid kullanımı</strong>&mdash;"
                "prednizon, deksametazon gibi ilaçlar alan hastalardır.</p>"
                "<p><strong>Kronik psikolojik stres</strong>, <strong>depresyon</strong>, <strong>alkolizm</strong> ve <strong>ciddi obezite</strong> "
                "de kortizolü anormal seviyelere çıkarabilir (&ldquo;psödo-Cushing&rdquo;). "
                "Bunların gerçek Cushing sendromundan ayırt edilmesi dinamik testlerle yapılır.</p>"
                "<p><strong>Düşük kortizol (hipokortizolizm)</strong> en sık <strong>Addison hastalığı</strong> (primer adrenal yetmezlik) nedeniyle olur; "
                "adrenal bezler hasar görür, genellikle otoimmün yıkım sonucu. <strong>Sekonder adrenal yetmezlik</strong> hipofizin yeterli ACTH üretmemesi "
                "veya uzun süreli dışarıdan steroid kullanımı sonrası ilacın çok hızlı kesilmesi ile ortaya çıkar. "
                "Ciddi düşük kortizol (adrenal kriz) tıbbi bir acildir.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Anormal kortizol belirtileri",
            body_html=(
                "<p><strong>Yüksek kortizol</strong> belirtileri yavaş gelişir: yüzde (&ldquo;ay yüzü&rdquo;), sırtta (&ldquo;bufalo hörgücü&rdquo;) "
                "ve karında <strong>kilo artışı</strong>, <strong>yüksek tansiyon</strong>, <strong>yüksek kan şekeri</strong>, "
                "<strong>ruh hali değişiklikleri</strong> (anksiyete, irritabilite, depresyon), <strong>incelmiş cilt</strong> ve kolay çürükler, "
                "<strong>kas güçsüzlüğü</strong>, mor çatlaklar (stria) ve kadınlarda <strong>adet düzensizlikleri</strong> olabilir. "
                "Uzun süreli hiperkortizolizm enfeksiyon ve osteoporoz riskini artırır.</p>"
                "<p><strong>Düşük kortizol</strong> belirtileri arasında <strong>şiddetli yorgunluk</strong>, <strong>kilo kaybı</strong>, "
                "<strong>düşük tansiyon</strong> (özellikle ayağa kalkınca), baş dönmesi, bulantı, tuz isteği ve "
                "<strong>ciltte koyulaşma</strong> (hiperpigmentasyon, Addison hastalığına özgü) yer alır. "
                "Adrenal kriz ani şiddetli karın ağrısı, kusma, konfüzyon ve şok ile kendini gösterebilir&mdash;acil tedavi gerektirir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Hekiminizin isteyebileceği ilişkili testler",
            body_html=(
                "<p>Tek bir sabah kortizol ölçümü başlangıç noktasıdır; tanıyı doğrulamak için genellikle ek testler gerekir. "
                "<strong>Yüksek kortizol</strong> şüphesinde: <strong>24 saatlik idrar serbest kortizolü</strong>, "
                "<strong>gece geç salivari kortizol</strong> ve <strong>düşük doz deksametazon baskılama testi (DST)</strong> standart taramalardır. "
                "Bunlar anormalse hipofiz MR, adrenal BT ve ACTH düzeyi ile lokalizasyon yapılır.</p>"
                "<p><strong>Düşük kortizol</strong> şüphesinde: <strong>ACTH stimülasyon testi (Synacthen testi)</strong> altın standarttır. "
                "Hekiminiz ayrıca <strong>ACTH düzeyi</strong>, <strong>glukoz</strong>, <strong>elektrolit</strong> ve "
                "<strong>tiroid fonksiyon testleri</strong> isteyebilir çünkü adrenal yetmezlik diğer endokrin bozukluklarla birlikte görülebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Kortizol düzeyiniz referans aralığı dışındaysa veya açıklanamayan kilo değişimleri, sürekli yorgunluk, "
                "yeni başlayan yüksek tansiyon, kolay çürükler veya cilt koyulaşması gibi belirtileriniz varsa hekiminize danışın.</p>"
                "<p>Adrenal kriz belirtileri&mdash;ani şiddetli karın ağrısı, kusma, aşırı güçsüzlük, konfüzyon veya bilinç kaybı&mdash;yaşarsanız "
                "<strong>acil</strong> tıbbi yardım alın. Adrenal yetmezlik tanısı olan hastalar acil hidrokortizon enjeksiyonu taşımalı "
                "ve tıbbi uyarı bilekliği takmalıdır.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya kortizolünüzü anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;hazırlanmanıza yardımcı olur. Kan tahlili raporunuzu "
                "<a href=\"/analyze\">noryaai.com/analyze</a> adresine yükleyin ve kortizol seviyenizi ilişkili belirteçlerle birlikte "
                "sade dilde açıklayan yapılandırılmış bir özet alın.</p>"
                "<p>Açıklanamayan belirtileri araştırıyor veya mevcut bir endokrin durumu takip ediyor olun, "
                "Norya sonuçlarınızı önemli olana odaklanabilmeniz için düzenler. "
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
            heading="Niveles de cortisol: qué significa tu análisis de sangre",
            body_html=(
                "<p>El cortisol se conoce a menudo como la <em>hormona del estrés</em> porque se eleva cuando el cuerpo percibe una amenaza, "
                "pero su función va mucho más allá de la respuesta de lucha o huida. El cortisol ayuda a regular el azúcar en sangre, la presión arterial, "
                "la función inmunitaria y el metabolismo. Tu médico solicita un análisis de cortisol cuando sospecha un exceso o un déficit.</p>"
                "<p>Esta guía explica qué hace el cortisol, cómo interpretar tu resultado, las causas comunes de niveles anormales, "
                "los síntomas asociados y cuándo acudir al médico. Es contenido educativo, no un diagnóstico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es el cortisol y por qué es importante?",
            body_html=(
                "<p><strong>El cortisol</strong> es una hormona glucocorticoide producida por las glándulas suprarrenales, situadas sobre cada riñón. "
                "Su secreción es controlada por el <strong>eje hipotálamo-hipófisis-suprarrenal (HPA)</strong>: el hipotálamo libera CRH, "
                "la hipófisis secreta ACTH y esta indica a la corteza suprarrenal que produzca cortisol. "
                "El cortisol retroalimenta para suprimir CRH y ACTH, creando un circuito autorregulado.</p>"
                "<p>El cortisol sigue un <strong>ritmo circadiano</strong>: los niveles alcanzan su pico por la mañana temprano (6&ndash;8 AM) "
                "y descienden gradualmente hasta alcanzar el punto más bajo alrededor de medianoche. "
                "Este ritmo es importante porque la hora de la extracción afecta al valor considerado normal.</p>"
                "<p>Las funciones clave del cortisol incluyen la movilización de glucosa hepática (gluconeogénesis), "
                "la supresión de respuestas inmunitarias no esenciales durante el estrés agudo, "
                "el mantenimiento de la presión arterial y la influencia en el estado de ánimo y la cognición.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos normales de cortisol",
            body_html=(
                "<p>El <strong>cortisol matutino (6&ndash;8 AM)</strong> es la medición estándar. Valores habituales en adultos:</p>"
                "<ul>"
                "<li><strong>Mañana (6&ndash;8 AM):</strong> 6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</li>"
                "<li><strong>Tarde (hacia las 16 h):</strong> 2&ndash;14 &micro;g/dL</li>"
                "</ul>"
                "<p>El estrés, la enfermedad y ciertos medicamentos pueden elevar el cortisol de forma transitoria. "
                "Un resultado limítrofe aislado puede no ser significativo; tu médico puede solicitar pruebas dinámicas como el test de supresión con dexametasona.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de cortisol anormal",
            body_html=(
                "<p><strong>Cortisol alto (hipercortisolismo):</strong> el <strong>síndrome de Cushing</strong> es el ejemplo clásico "
                "(adenoma hipofisario, tumor suprarrenal o secreción ectópica de ACTH). La causa más frecuente en la práctica clínica es "
                "el <strong>uso de glucocorticoides exógenos</strong> (prednisona, dexametasona). "
                "El estrés crónico, la depresión, el alcoholismo y la obesidad grave también elevan el cortisol (&ldquo;pseudo-Cushing&rdquo;).</p>"
                "<p><strong>Cortisol bajo (hipocortisolismo):</strong> la <strong>enfermedad de Addison</strong> (insuficiencia suprarrenal primaria) es la causa más común. "
                "La <strong>insuficiencia suprarrenal secundaria</strong> ocurre cuando la hipófisis no produce suficiente ACTH "
                "o cuando se retiran esteroides exógenos demasiado rápido. El cortisol bajo grave (crisis suprarrenal) es una emergencia médica.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de cortisol anormal",
            body_html=(
                "<p><strong>Cortisol alto:</strong> aumento de peso (cara, espalda, abdomen), hipertensión, hiperglucemia, "
                "cambios de humor, piel adelgazada con hematomas fáciles, debilidad muscular, estrías violáceas e irregularidades menstruales.</p>"
                "<p><strong>Cortisol bajo:</strong> fatiga intensa, pérdida de peso, hipotensión (especialmente ortostática), mareos, náuseas, "
                "antojos de sal y oscurecimiento de la piel (hiperpigmentación, típica de Addison). "
                "La crisis suprarrenal se presenta con dolor abdominal severo, vómitos, confusión y shock&mdash;requiere tratamiento de emergencia.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p>Para <strong>cortisol alto</strong>: cortisol libre urinario de 24 horas, cortisol salival nocturno y test de supresión con dexametasona. "
                "Si son anormales, RMN hipofisaria, TC suprarrenal y niveles de ACTH ayudan a localizar la causa.</p>"
                "<p>Para <strong>cortisol bajo</strong>: test de estimulación con ACTH (Synacthen). "
                "El médico también comprobará ACTH, glucosa, electrolitos y función tiroidea, "
                "ya que la insuficiencia suprarrenal puede coexistir con otros trastornos endocrinos.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Consulta si tu cortisol está fuera del rango o si experimentas cambios de peso inexplicables, fatiga persistente, "
                "hipertensión de inicio reciente, hematomas fáciles u oscurecimiento de la piel.</p>"
                "<p>Busca atención de <strong>emergencia</strong> ante signos de crisis suprarrenal: dolor abdominal severo, vómitos, "
                "debilidad extrema, confusión o pérdida de conciencia.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya te ayuda a entender tu cortisol",
            body_html=(
                "<p>Norya no diagnostica&mdash;te ayuda a prepararte. Sube tu análisis de sangre en "
                "<a href=\"/analyze\">noryaai.com/analyze</a> y recibe un resumen claro que destaca tu nivel de cortisol en lenguaje sencillo.</p>"
                "<p>Ya sea que investigues síntomas inexplicables o monitorices una condición endocrina, "
                "Norya organiza tus resultados para centrarte en lo importante. "
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
            heading="Cortisolwerte: was Ihr Bluttest bedeutet",
            body_html=(
                "<p>Cortisol wird häufig als <em>Stresshormon</em> bezeichnet, doch seine Rolle geht weit über die Kampf-oder-Flucht-Reaktion hinaus. "
                "Cortisol reguliert Blutzucker, Blutdruck, Immunfunktion und Stoffwechsel rund um die Uhr. "
                "Ein Cortisol-Bluttest wird angeordnet, wenn Ihr Arzt einen Überschuss oder Mangel dieses Hormons vermutet.</p>"
                "<p>Dieser Ratgeber erklärt, was Cortisol tut, wie Sie Ihr Ergebnis einordnen, häufige Ursachen abnormaler Werte, "
                "zugehörige Symptome und wann Sie einen Arzt aufsuchen sollten.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist Cortisol und warum ist es wichtig?",
            body_html=(
                "<p><strong>Cortisol</strong> ist ein Glucocorticoid-Hormon, das von den Nebennieren produziert wird. "
                "Seine Ausschüttung wird über die <strong>Hypothalamus-Hypophysen-Nebennieren-Achse (HPA)</strong> gesteuert. "
                "Cortisol folgt einem <strong>zirkadianen Rhythmus</strong>: Die Spiegel sind morgens (6&ndash;8 Uhr) am höchsten "
                "und fallen bis Mitternacht auf den Tiefpunkt. Dieser Rhythmus ist wichtig, weil der Zeitpunkt der Blutentnahme beeinflusst, "
                "was als &bdquo;normal&ldquo; gilt.</p>"
                "<p>Wichtige Funktionen: Glukosemobilisierung (Glukoneogenese), Immunsuppression bei akutem Stress, "
                "Aufrechterhaltung von Gefäßtonus und Blutdruck sowie Einfluss auf Stimmung und Kognition. "
                "Sowohl chronischer Überschuss als auch Mangel können ernste Folgen haben.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Cortisolwerte",
            body_html=(
                "<p>Der <strong>morgendliche Cortisolwert (6&ndash;8 Uhr)</strong> ist die Standardmessung:</p>"
                "<ul>"
                "<li><strong>Morgens:</strong> 6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</li>"
                "<li><strong>Abends (ca. 16 Uhr):</strong> 2&ndash;14 &micro;g/dL</li>"
                "</ul>"
                "<p>Stress, Erkrankung und Medikamente können Cortisol vorübergehend erhöhen. "
                "Ein einzelner Grenzwert ist nicht immer klinisch bedeutsam; dynamische Tests können folgen.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen abnormaler Cortisolwerte",
            body_html=(
                "<p><strong>Hohes Cortisol:</strong> <strong>Cushing-Syndrom</strong> (Hypophysenadenom, Nebennierentumor, ektope ACTH-Sekretion), "
                "<strong>exogene Glucocorticoide</strong> (die häufigste Ursache in der Praxis), chronischer Stress, Depression, Alkoholismus und schwere Adipositas.</p>"
                "<p><strong>Niedriges Cortisol:</strong> <strong>Morbus Addison</strong> (primäre Nebenniereninsuffizienz, oft autoimmun), "
                "sekundäre Nebenniereninsuffizienz (zu wenig ACTH oder zu schnelles Absetzen von Steroiden). "
                "Ein schwerer Cortisolmangel (Nebennierenkrise) ist ein medizinischer Notfall.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome bei abnormalem Cortisol",
            body_html=(
                "<p><strong>Hohes Cortisol:</strong> Gewichtszunahme (Gesicht, Rücken, Bauch), Bluthochdruck, Hyperglykämie, "
                "Stimmungsschwankungen, dünne Haut mit Hämatomen, Muskelschwäche, lila Streifen und Menstruationsstörungen.</p>"
                "<p><strong>Niedriges Cortisol:</strong> starke Müdigkeit, Gewichtsverlust, Hypotonie (besonders beim Aufstehen), "
                "Schwindel, Übelkeit, Salzgelüste und Hautverdunkelung (Hyperpigmentierung bei Addison). "
                "Die Nebennierenkrise zeigt sich mit plötzlichen Bauchschmerzen, Erbrechen, Verwirrtheit und Schock&mdash;sofortige Notfallbehandlung nötig.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Ergänzende Untersuchungen",
            body_html=(
                "<p><strong>Hohes Cortisol:</strong> 24-h-Urin-Cortisol, nächtliches Speichelcortisol und Dexamethason-Suppressionstest. "
                "Bei auffälligen Ergebnissen: Hypophysen-MRT, Nebennieren-CT und ACTH-Bestimmung.</p>"
                "<p><strong>Niedriges Cortisol:</strong> ACTH-Stimulationstest (Synacthen). "
                "Zusätzlich: ACTH, Glukose, Elektrolyte und Schilddrüsenfunktion, "
                "da Nebenniereninsuffizienz mit anderen Endokrinopathien einhergehen kann.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann zum Arzt?",
            body_html=(
                "<p>Sprechen Sie mit Ihrem Arzt, wenn Cortisol außerhalb des Referenzbereichs liegt oder wenn Sie ungeklärte Gewichtsveränderungen, "
                "anhaltende Müdigkeit, neu aufgetretenen Bluthochdruck, leichte Blutergüsse oder Hautverdunkelung bemerken.</p>"
                "<p>Suchen Sie <strong>Notfallhilfe</strong> bei Zeichen einer Nebennierenkrise: plötzliche starke Bauchschmerzen, "
                "Erbrechen, extreme Schwäche, Verwirrtheit oder Bewusstlosigkeit.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihr Cortisol zu verstehen",
            body_html=(
                "<p>Norya stellt keine Diagnosen&mdash;wir helfen bei der Vorbereitung. Laden Sie Ihren Blutbefund unter "
                "<a href=\"/analyze\">noryaai.com/analyze</a> hoch und erhalten Sie eine Zusammenfassung, "
                "die Ihren Cortisolwert zusammen mit verwandten Markern verständlich erklärt.</p>"
                "<p>Ob Sie Symptome abklären oder eine Endokrinopathie überwachen&mdash;"
                "Norya ordnet Ihre Ergebnisse für das Arztgespräch. "
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
            heading="Taux de cortisol : que signifie votre analyse de sang ?",
            body_html=(
                "<p>Le cortisol est souvent appelé <em>hormone du stress</em> car il augmente lorsque le corps perçoit une menace, "
                "mais son rôle dépasse largement la réponse de fuite ou combat. Le cortisol régule la glycémie, la pression artérielle, "
                "l&rsquo;immunité et le métabolisme. Votre médecin prescrit un dosage du cortisol en cas de suspicion d&rsquo;excès ou de déficit.</p>"
                "<p>Ce guide explique ce que fait le cortisol, comment interpréter votre résultat, les causes fréquentes de niveaux anormaux, "
                "les symptômes associés et quand consulter. Il est éducatif et ne constitue pas un diagnostic.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu'est-ce que le cortisol et pourquoi est-il important ?",
            body_html=(
                "<p><strong>Le cortisol</strong> est un glucocorticoïde produit par les glandes surrénales, contrôlé par "
                "l&rsquo;<strong>axe hypothalamo-hypophyso-surrénalien (HPA)</strong>. Il suit un <strong>rythme circadien</strong> : "
                "pic le matin (6&ndash;8 h) et nadir vers minuit. Ce rythme est crucial car l&rsquo;heure du prélèvement influence la valeur normale.</p>"
                "<p>Fonctions clés : mobilisation du glucose (néoglucogenèse), suppression des réponses immunitaires non essentielles en cas de stress aigu, "
                "maintien du tonus vasculaire et influence sur l&rsquo;humeur. L&rsquo;excès comme le déficit chroniques ont des conséquences sérieuses.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales du cortisol",
            body_html=(
                "<p>Le <strong>cortisol matinal (6&ndash;8 h)</strong> est la mesure standard :</p>"
                "<ul>"
                "<li><strong>Matin :</strong> 6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</li>"
                "<li><strong>Après-midi (vers 16 h) :</strong> 2&ndash;14 &micro;g/dL</li>"
                "</ul>"
                "<p>Le stress, la maladie et certains médicaments peuvent élever le cortisol temporairement. "
                "Un résultat limite isolé n&rsquo;est pas toujours significatif ; des tests dynamiques peuvent suivre.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un cortisol anormal",
            body_html=(
                "<p><strong>Cortisol élevé :</strong> <strong>syndrome de Cushing</strong> (adénome hypophysaire, tumeur surrénalienne, ACTH ectopique), "
                "<strong>glucocorticoïdes exogènes</strong> (cause la plus fréquente en pratique), stress chronique, dépression, alcoolisme et obésité sévère.</p>"
                "<p><strong>Cortisol bas :</strong> <strong>maladie d&rsquo;Addison</strong> (insuffisance surrénale primaire, souvent auto-immune), "
                "insuffisance surrénale secondaire (ACTH insuffisant ou sevrage stéroïdien trop rapide). "
                "Le déficit sévère (crise surrénale) est une urgence médicale.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d'un cortisol anormal",
            body_html=(
                "<p><strong>Cortisol élevé :</strong> prise de poids (visage, dos, abdomen), hypertension, hyperglycémie, "
                "troubles de l&rsquo;humeur, peau amincie, ecchymoses faciles, faiblesse musculaire, vergetures pourpres et troubles menstruels.</p>"
                "<p><strong>Cortisol bas :</strong> fatigue intense, perte de poids, hypotension orthostatique, vertiges, nausées, "
                "envies de sel et assombrissement cutané (hyperpigmentation, typique d&rsquo;Addison). "
                "La crise surrénale se manifeste par des douleurs abdominales soudaines, des vomissements, une confusion et un état de choc&mdash;urgence absolue.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens complémentaires",
            body_html=(
                "<p><strong>Cortisol élevé :</strong> cortisol libre urinaire des 24 heures, cortisol salivaire nocturne et test de freinage à la dexaméthasone. "
                "Si anormaux : IRM hypophysaire, scanner surrénalien et dosage de l&rsquo;ACTH.</p>"
                "<p><strong>Cortisol bas :</strong> test de stimulation à l&rsquo;ACTH (Synacthène). "
                "Également : ACTH, glycémie, ionogramme et bilan thyroïdien.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez si votre cortisol est hors norme ou si vous avez des variations de poids inexpliquées, "
                "une fatigue persistante, une HTA récente, des ecchymoses faciles ou un assombrissement cutané.</p>"
                "<p>Appelez les <strong>urgences</strong> en cas de crise surrénale : douleur abdominale soudaine, "
                "vomissements, faiblesse extrême, confusion ou perte de conscience.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre votre cortisol",
            body_html=(
                "<p>Norya ne pose pas de diagnostic&mdash;nous vous aidons à vous préparer. Téléversez votre bilan sur "
                "<a href=\"/analyze\">noryaai.com/analyze</a> et recevez un résumé clair de votre cortisol et des marqueurs associés.</p>"
                "<p>Que vous investiguiez des symptômes ou suiviez une pathologie endocrinienne, "
                "Norya organise vos résultats pour l&rsquo;échange avec votre médecin. "
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
            heading="Livelli di cortisolo: cosa significa il tuo esame del sangue",
            body_html=(
                "<p>Il cortisolo è spesso definito <em>ormone dello stress</em> perché aumenta quando il corpo percepisce una minaccia, "
                "ma il suo ruolo va ben oltre la risposta di lotta o fuga. Il cortisolo regola glicemia, pressione, sistema immunitario e metabolismo. "
                "Il medico prescrive il dosaggio del cortisolo quando sospetta un eccesso o un deficit.</p>"
                "<p>Questa guida spiega cosa fa il cortisolo, come interpretare il risultato, le cause comuni di valori anomali, "
                "i sintomi associati e quando consultare il medico. È a scopo educativo, non diagnostico.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Cos'è il cortisolo e perché è importante?",
            body_html=(
                "<p><strong>Il cortisolo</strong> è un glucocorticoide prodotto dalle ghiandole surrenali, controllato dall&rsquo;"
                "<strong>asse ipotalamo-ipofisi-surrene (HPA)</strong>. Segue un <strong>ritmo circadiano</strong>: picco al mattino (6&ndash;8) "
                "e nadir verso mezzanotte. L&rsquo;ora del prelievo influenza il valore considerato normale.</p>"
                "<p>Funzioni chiave: mobilizzazione del glucosio (gluconeogenesi), soppressione immunitaria durante lo stress acuto, "
                "mantenimento del tono vascolare e influenza sull&rsquo;umore. Eccesso e deficit cronici possono avere conseguenze gravi.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del cortisolo",
            body_html=(
                "<p>Il <strong>cortisolo mattutino (6&ndash;8)</strong> è la misura standard:</p>"
                "<ul>"
                "<li><strong>Mattino:</strong> 6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</li>"
                "<li><strong>Pomeriggio (verso le 16):</strong> 2&ndash;14 &micro;g/dL</li>"
                "</ul>"
                "<p>Stress, malattia e farmaci possono elevare temporaneamente il cortisolo. "
                "Un risultato borderline isolato potrebbe non essere significativo; possono seguire test dinamici.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di cortisolo anomalo",
            body_html=(
                "<p><strong>Cortisolo alto:</strong> <strong>sindrome di Cushing</strong> (adenoma ipofisario, tumore surrenalico, ACTH ectopico), "
                "<strong>glucocorticoidi esogeni</strong> (causa più frequente nella pratica), stress cronico, depressione, alcolismo e obesità grave.</p>"
                "<p><strong>Cortisolo basso:</strong> <strong>morbo di Addison</strong> (insufficienza surrenalica primaria, spesso autoimmune), "
                "insufficienza surrenalica secondaria (ACTH insufficiente o sospensione troppo rapida di steroidi). "
                "La crisi surrenalica è un&rsquo;emergenza medica.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi del cortisolo anomalo",
            body_html=(
                "<p><strong>Cortisolo alto:</strong> aumento di peso (viso, schiena, addome), ipertensione, iperglicemia, "
                "alterazioni dell&rsquo;umore, cute assottigliata con lividi, debolezza muscolare, strie purpuree e irregolarità mestruali.</p>"
                "<p><strong>Cortisolo basso:</strong> stanchezza marcata, perdita di peso, ipotensione ortostatica, vertigini, nausea, "
                "desiderio di sale e iperpigmentazione cutanea (tipica di Addison). "
                "La crisi surrenalica si presenta con dolore addominale improvviso, vomito, confusione e shock&mdash;emergenza assoluta.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p><strong>Cortisolo alto:</strong> cortisolo libero urinario 24 ore, cortisolo salivare notturno e test di soppressione al desametasone. "
                "Se anomali: RMN ipofisaria, TC surrenalica e dosaggio ACTH.</p>"
                "<p><strong>Cortisolo basso:</strong> test di stimolazione con ACTH (Synacthen). "
                "Inoltre: ACTH, glicemia, elettroliti e funzione tiroidea.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico",
            body_html=(
                "<p>Consultate il medico se il cortisolo è fuori intervallo o se avete variazioni di peso inspiegabili, "
                "stanchezza persistente, ipertensione di recente insorgenza, lividi facili o iperpigmentazione.</p>"
                "<p>Cercate assistenza d&rsquo;<strong>emergenza</strong> in caso di crisi surrenalica: dolore addominale improvviso, "
                "vomito, debolezza estrema, confusione o perdita di coscienza.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a capire il tuo cortisolo",
            body_html=(
                "<p>Norya non fa diagnosi&mdash;ti aiuta a prepararti. Carica le tue analisi su "
                "<a href=\"/analyze\">noryaai.com/analyze</a> e ricevi un riepilogo chiaro del cortisolo e dei marcatori correlati.</p>"
                "<p>Che tu stia indagando sintomi o monitorando una condizione endocrina, "
                "Norya organizza i tuoi risultati per il dialogo con il medico. "
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
            heading="רמות קורטיזול: מה המשמעות של בדיקת הדם שלך",
            body_html=(
                "<p>קורטיזול מכונה לעיתים קרובות <em>הורמון הסטרס</em> כי הוא עולה כשהגוף חש באיום, "
                "אך תפקידו רחב בהרבה מתגובת הילחם-או-ברח. קורטיזול מסייע בוויסות סוכר בדם, לחץ דם, חיסון ומטבוליזם. "
                "הרופא מזמין בדיקת קורטיזול כשהוא חושד בעודף או בחסר של הורמון חיוני זה.</p>"
                "<p>מדריך זה מסביר מה קורטיזול עושה, כיצד לקרוא את התוצאה, גורמים שכיחים לרמות חריגות, "
                "תסמינים קשורים ומתי לפנות לרופא. הוא חינוכי ואינו מהווה אבחנה&mdash;"
                "שוחחו תמיד עם רופא על התוצאות שלכם.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהו קורטיזול ולמה הוא חשוב?",
            body_html=(
                "<p><strong>קורטיזול</strong> הוא הורמון גלוקוקורטיקואיד המיוצר בבלוטות האדרנל, הנשלט על ידי "
                "<strong>ציר ההיפותלמוס-היפופיזה-אדרנל (HPA)</strong>. קורטיזול עוקב אחר <strong>מקצב יממתי</strong>: "
                "הרמות מגיעות לשיא בבוקר המוקדם (6&ndash;8) ויורדות בהדרגה עד חצות. "
                "מקצב זה חשוב כי מועד לקיחת הדם משפיע על מה שנחשב &ldquo;תקין&rdquo;.</p>"
                "<p>תפקידים מרכזיים: גיוס גלוקוז מהכבד (גלוקונאוגנזה), דיכוי תגובות חיסוניות לא חיוניות בזמן סטרס חריף, "
                "שמירה על טונוס כלי דם ולחץ דם, והשפעה על מצב רוח ותפקוד קוגניטיבי.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי קורטיזול תקינים",
            body_html=(
                "<p><strong>קורטיזול בוקר (6&ndash;8)</strong> הוא המדידה הסטנדרטית:</p>"
                "<ul>"
                "<li><strong>בוקר:</strong> 6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</li>"
                "<li><strong>אחה\"צ (סביב 16:00):</strong> 2&ndash;14 &micro;g/dL</li>"
                "</ul>"
                "<p>סטרס, מחלה ותרופות מסוימות יכולים להעלות קורטיזול באופן זמני. "
                "תוצאה גבולית בודדת אינה תמיד משמעותית קלינית; הרופא עשוי לבקש בדיקות דינמיות.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לקורטיזול חריג",
            body_html=(
                "<p><strong>קורטיזול גבוה:</strong> <strong>תסמונת קושינג</strong> (אדנומה בהיפופיזה, גידול אדרנל, ACTH אקטופי), "
                "<strong>גלוקוקורטיקואידים חיצוניים</strong> (הגורם השכיח ביותר), סטרס כרוני, דיכאון, אלכוהוליזם והשמנת יתר חמורה.</p>"
                "<p><strong>קורטיזול נמוך:</strong> <strong>מחלת אדיסון</strong> (אי-ספיקת אדרנל ראשונית, לרוב אוטואימונית), "
                "אי-ספיקת אדרנל משנית (ACTH לא מספיק או הפסקה מהירה מדי של סטרואידים). "
                "חסר חמור (משבר אדרנל) הוא מצב חירום רפואי.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של קורטיזול חריג",
            body_html=(
                "<p><strong>קורטיזול גבוה:</strong> עלייה במשקל (פנים, גב, בטן), יתר לחץ דם, היפרגליקמיה, "
                "שינויי מצב רוח, עור דק עם שטפי דם קלים, חולשת שרירים, סימני מתיחה סגולים והפרעות במחזור.</p>"
                "<p><strong>קורטיזול נמוך:</strong> עייפות קשה, ירידה במשקל, לחץ דם נמוך (בעיקר בעמידה), "
                "סחרחורת, בחילה, תשוקה למלח והכהיית עור (היפרפיגמנטציה, אופיינית לאדיסון). "
                "משבר אדרנל מתבטא בכאב בטן פתאומי חמור, הקאות, בלבול ושוק&mdash;דורש טיפול חירום מיידי.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות נלוות",
            body_html=(
                "<p><strong>קורטיזול גבוה:</strong> קורטיזול חופשי בשתן 24 שעות, קורטיזול רוקי לילי ובדיקת דיכוי דקסמתזון. "
                "אם חריגים: MRI היפופיזה, CT אדרנל ורמת ACTH.</p>"
                "<p><strong>קורטיזול נמוך:</strong> בדיקת גירוי ACTH (סינקטן). "
                "בנוסף: ACTH, גלוקוז, אלקטרוליטים ותפקוד בלוטת התריס.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>שוחחו עם הרופא אם הקורטיזול מחוץ לטווח או אם יש שינויי משקל לא מוסברים, "
                "עייפות מתמשכת, יתר לחץ דם חדש, שטפי דם קלים או הכהיית עור.</p>"
                "<p>פנו ל<strong>חירום</strong> בסימני משבר אדרנל: כאב בטן פתאומי חמור, הקאות, "
                "חולשה קיצונית, בלבול או אובדן הכרה.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת לכם להבין את הקורטיזול",
            body_html=(
                "<p>Norya לא מאבחנת&mdash;אנחנו עוזרים לכם להתכונן. העלו את הדוח ב-"
                "<a href=\"/analyze\">noryaai.com/analyze</a> וקבלו סיכום ברור המסביר את רמת הקורטיזול לצד סמנים נלווים בשפה פשוטה.</p>"
                "<p>בין אם אתם חוקרים תסמינים או עוקבים אחרי מצב אנדוקריני, "
                "Norya מארגנת את התוצאות לקראת השיחה עם הרופא. "
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
            heading="कोर्टिसोल स्तर: आपकी ब्लड टेस्ट रिपोर्ट का क्या मतलब है",
            body_html=(
                "<p>कोर्टिसोल को अक्सर <em>स्ट्रेस हार्मोन</em> कहा जाता है क्योंकि यह तब बढ़ता है जब शरीर को खतरा महसूस होता है, "
                "लेकिन इसकी भूमिका फाइट-या-फ्लाइट प्रतिक्रिया से कहीं आगे जाती है। कोर्टिसोल ब्लड शुगर, ब्लड प्रेशर, "
                "इम्यून फंक्शन और मेटाबोलिज़्म को नियंत्रित करने में मदद करता है। डॉक्टर कोर्टिसोल ब्लड टेस्ट तब मँगवाते हैं "
                "जब इस हार्मोन के अधिक या कम होने की शंका होती है।</p>"
                "<p>यह गाइड बताती है कि कोर्टिसोल क्या करता है, रिजल्ट कैसे पढ़ें, असामान्य स्तरों के कारण, "
                "संबंधित लक्षण और डॉक्टर से कब मिलें। यह शैक्षिक है, निदान नहीं&mdash;अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="कोर्टिसोल क्या है और यह क्यों महत्वपूर्ण है?",
            body_html=(
                "<p><strong>कोर्टिसोल</strong> एड्रेनल ग्रंथियों द्वारा उत्पादित एक ग्लूकोकोर्टिकोइड हार्मोन है, "
                "जो <strong>हाइपोथैलेमस-पिट्यूटरी-एड्रेनल (HPA) एक्सिस</strong> द्वारा नियंत्रित होता है। "
                "कोर्टिसोल <strong>दैनिक लय (diurnal rhythm)</strong> का पालन करता है: सुबह जल्दी (6&ndash;8 AM) चरम पर होता है "
                "और आधी रात तक धीरे-धीरे गिरता है। यह लय महत्वपूर्ण है क्योंकि ब्लड लेने का समय &ldquo;सामान्य&rdquo; मान को प्रभावित करता है।</p>"
                "<p>प्रमुख कार्य: लिवर से ग्लूकोज मोबिलाइज़ेशन, तीव्र तनाव में गैर-आवश्यक इम्यून रिस्पॉन्स का दमन, "
                "ब्लड प्रेशर बनाए रखना और मूड व संज्ञानात्मक कार्य पर प्रभाव।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य कोर्टिसोल रेंज",
            body_html=(
                "<p><strong>सुबह का कोर्टिसोल (6&ndash;8 AM)</strong> मानक माप है:</p>"
                "<ul>"
                "<li><strong>सुबह:</strong> 6&ndash;23 µg/dL (166&ndash;635 nmol/L)</li>"
                "<li><strong>शाम (लगभग 4 PM):</strong> 2&ndash;14 µg/dL</li>"
                "</ul>"
                "<p>तनाव, बीमारी और कुछ दवाएँ कोर्टिसोल को अस्थायी रूप से बढ़ा सकती हैं। "
                "एक अलग-थलग बॉर्डरलाइन रिजल्ट हमेशा चिकित्सकीय रूप से महत्वपूर्ण नहीं होता; डॉक्टर डायनामिक टेस्ट मँगवा सकते हैं।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="असामान्य कोर्टिसोल के कारण",
            body_html=(
                "<p><strong>उच्च कोर्टिसोल:</strong> <strong>कुशिंग सिंड्रोम</strong> (पिट्यूटरी एडेनोमा, एड्रेनल ट्यूमर, एक्टोपिक ACTH), "
                "<strong>बाहरी ग्लूकोकोर्टिकोइड</strong> (सबसे आम कारण), क्रोनिक स्ट्रेस, डिप्रेशन, अल्कोहलिज़्म और गंभीर मोटापा।</p>"
                "<p><strong>निम्न कोर्टिसोल:</strong> <strong>एडिसन रोग</strong> (प्राइमरी एड्रेनल इंसफिशिएंसी, अक्सर ऑटोइम्यून), "
                "सेकेंडरी एड्रेनल इंसफिशिएंसी (ACTH कम या स्टेरॉइड बहुत तेज़ी से बंद करना)। "
                "गंभीर कमी (एड्रेनल क्राइसिस) एक मेडिकल इमरजेंसी है।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="असामान्य कोर्टिसोल के लक्षण",
            body_html=(
                "<p><strong>उच्च कोर्टिसोल:</strong> वज़न बढ़ना (चेहरा, पीठ, पेट), हाई ब्लड प्रेशर, हाई ब्लड शुगर, "
                "मूड बदलाव, पतली त्वचा और आसान नील, माँसपेशियों में कमज़ोरी, बैंगनी स्ट्रेच मार्क्स और मासिक धर्म अनियमितता।</p>"
                "<p><strong>निम्न कोर्टिसोल:</strong> गंभीर थकान, वज़न कम होना, लो ब्लड प्रेशर (खड़े होने पर), "
                "चक्कर, मतली, नमक की तीव्र इच्छा और त्वचा का काला पड़ना (एडिसन में हाइपरपिगमेंटेशन)। "
                "एड्रेनल क्राइसिस: अचानक तीव्र पेट दर्द, उल्टी, भ्रम और शॉक&mdash;तुरंत आपातकालीन उपचार ज़रूरी।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित जाँचें",
            body_html=(
                "<p><strong>उच्च कोर्टिसोल:</strong> 24 घंटे यूरिनरी फ्री कोर्टिसोल, रात का सैलिवरी कोर्टिसोल और डेक्सामेथासोन सप्रेशन टेस्ट। "
                "यदि असामान्य: पिट्यूटरी MRI, एड्रेनल CT और ACTH स्तर।</p>"
                "<p><strong>निम्न कोर्टिसोल:</strong> ACTH स्टिमुलेशन टेस्ट (सिनैक्थेन)। "
                "इसके अलावा: ACTH, ग्लूकोज, इलेक्ट्रोलाइट्स और थायरॉइड फंक्शन टेस्ट।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>कोर्टिसोल रेफरेंस रेंज से बाहर हो या अस्पष्ट वज़न बदलाव, लगातार थकान, "
                "नया हाई BP, आसान नील या त्वचा का काला पड़ना हो तो डॉक्टर से बात करें।</p>"
                "<p>एड्रेनल क्राइसिस के संकेत&mdash;अचानक गंभीर पेट दर्द, उल्टी, अत्यधिक कमज़ोरी, भ्रम या बेहोशी&mdash;"
                "होने पर <strong>तुरंत</strong> इमरजेंसी सहायता लें।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके कोर्टिसोल को समझने में कैसे मदद करता है",
            body_html=(
                "<p>Norya निदान नहीं करता&mdash;हम आपको तैयार होने में मदद करते हैं। अपनी ब्लड रिपोर्ट "
                "<a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें और कोर्टिसोल स्तर को संबंधित मार्कर के साथ "
                "सरल भाषा में समझाने वाला स्पष्ट सारांश प्राप्त करें।</p>"
                "<p>चाहे आप लक्षणों की जाँच कर रहे हों या किसी एंडोक्राइन स्थिति की निगरानी कर रहे हों, "
                "Norya आपके परिणामों को व्यवस्थित करता है। प्लान व मूल्य के लिए <a href=\"/pricing\">प्राइसिंग पेज</a> देखें।</p>"
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
            heading="مستويات الكورتيزول: ماذا يعني تحليل الدم الخاص بك",
            body_html=(
                "<p>يُعرف الكورتيزول غالباً بـ<em>هرمون التوتر</em> لأنه يرتفع عندما يشعر الجسم بخطر، "
                "لكن دوره يتجاوز بكثير استجابة الكر أو الفر. ينظّم الكورتيزول سكر الدم وضغط الدم والمناعة والأيض. "
                "يطلب الطبيب فحص الكورتيزول عند الاشتباه بزيادة أو نقص هذا الهرمون الحيوي.</p>"
                "<p>يشرح هذا الدليل ما يفعله الكورتيزول وكيفية قراءة نتيجتك والأسباب الشائعة لمستويات غير طبيعية "
                "والأعراض المرتبطة ومتى يجب مراجعة الطبيب. هو تثقيفي وليس تشخيصياً&mdash;"
                "ناقش نتائجك دائماً مع طبيب مؤهل.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو الكورتيزول ولماذا هو مهم؟",
            body_html=(
                "<p><strong>الكورتيزول</strong> هرمون غلوكوكورتيكويد تنتجه الغدتان الكظريتان، يتحكم فيه "
                "<strong>محور الوطاء-النخامية-الكظر (HPA)</strong>. يتبع <strong>إيقاعاً يومياً</strong>: "
                "يبلغ ذروته صباحاً (6&ndash;8) وينخفض تدريجياً حتى منتصف الليل. "
                "هذا الإيقاع مهم لأن توقيت سحب الدم يؤثر على القيمة المعتبرة &ldquo;طبيعية&rdquo;.</p>"
                "<p>الوظائف الرئيسية: تعبئة الغلوكوز من الكبد (استحداث السكر)، كبت الاستجابات المناعية غير الضرورية أثناء الإجهاد الحاد، "
                "الحفاظ على التوتر الوعائي وضغط الدم، والتأثير على المزاج والإدراك.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="نطاقات الكورتيزول الطبيعية",
            body_html=(
                "<p><strong>كورتيزول الصباح (6&ndash;8)</strong> هو القياس المعياري:</p>"
                "<ul>"
                "<li><strong>صباحاً:</strong> 6&ndash;23 &micro;g/dL (166&ndash;635 nmol/L)</li>"
                "<li><strong>مساءً (حوالي 16:00):</strong> 2&ndash;14 &micro;g/dL</li>"
                "</ul>"
                "<p>التوتر والمرض وبعض الأدوية يمكن أن ترفع الكورتيزول مؤقتاً. "
                "نتيجة حدّية واحدة قد لا تكون ذات دلالة سريرية؛ قد يطلب الطبيب اختبارات ديناميكية.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب الكورتيزول غير الطبيعي",
            body_html=(
                "<p><strong>كورتيزول مرتفع:</strong> <strong>متلازمة كوشينغ</strong> (ورم نخامي، ورم كظري، ACTH منتبذ)، "
                "<strong>غلوكوكورتيكويدات خارجية</strong> (السبب الأكثر شيوعاً)، إجهاد مزمن، اكتئاب، إدمان كحول وسمنة مفرطة.</p>"
                "<p><strong>كورتيزول منخفض:</strong> <strong>مرض أديسون</strong> (قصور كظري أولي، غالباً مناعي ذاتي)، "
                "قصور كظري ثانوي (ACTH غير كافٍ أو وقف الستيرويدات بسرعة). "
                "النقص الشديد (أزمة كظرية) حالة طوارئ طبية.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض الكورتيزول غير الطبيعي",
            body_html=(
                "<p><strong>كورتيزول مرتفع:</strong> زيادة في الوزن (الوجه، الظهر، البطن)، ارتفاع ضغط الدم، ارتفاع سكر الدم، "
                "تقلبات مزاجية، ترقق الجلد مع كدمات سهلة، ضعف عضلي، خطوط تمدد أرجوانية واضطرابات في الدورة الشهرية.</p>"
                "<p><strong>كورتيزول منخفض:</strong> إرهاق شديد، فقدان وزن، انخفاض ضغط الدم (خاصة عند الوقوف)، "
                "دوخة، غثيان، اشتهاء الملح واسمرار الجلد (فرط تصبّغ، نموذجي لأديسون). "
                "الأزمة الكظرية: ألم بطني مفاجئ شديد، قيء، ارتباك وصدمة&mdash;تتطلب علاجاً طارئاً فورياً.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="فحوصات ذات صلة",
            body_html=(
                "<p><strong>كورتيزول مرتفع:</strong> كورتيزول حر في البول 24 ساعة، كورتيزول لعابي ليلي واختبار التثبيط بالدكساميثازون. "
                "إذا كانت غير طبيعية: رنين مغناطيسي للنخامية، تصوير مقطعي للكظر ومستوى ACTH.</p>"
                "<p><strong>كورتيزول منخفض:</strong> اختبار تحفيز ACTH (سيناكثين). "
                "أيضاً: ACTH، غلوكوز، شوارد ووظائف الغدة الدرقية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب؟",
            body_html=(
                "<p>تحدث مع طبيبك إذا كان الكورتيزول خارج النطاق أو إذا كنت تعاني من تغيرات وزن غير مفسَّرة، "
                "إرهاق مستمر، ارتفاع ضغط دم جديد، كدمات سهلة أو اسمرار الجلد.</p>"
                "<p>اطلب رعاية <strong>طارئة</strong> عند علامات أزمة كظرية: ألم بطني مفاجئ شديد، "
                "قيء، ضعف شديد، ارتباك أو فقدان وعي.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم الكورتيزول",
            body_html=(
                "<p>Norya لا تُشخّص&mdash;نحن نساعدك على الاستعداد. ارفع تقريرك على "
                "<a href=\"/analyze\">noryaai.com/analyze</a> واحصل على ملخص واضح يشرح مستوى الكورتيزول مع المؤشرات المرتبطة بلغة بسيطة.</p>"
                "<p>سواء كنت تبحث في أعراض أو تراقب حالة غددية، "
                "تنظّم Norya نتائجك لتحضيرك لموعد الطبيب. "
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

def get_cortisol_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for cortisol article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_cortisol_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for cortisol article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal cortisol level?",
             "answer": "Normal morning cortisol (6–8 AM) is roughly 6–23 µg/dL (166–635 nmol/L). Evening levels are lower, around 2–14 µg/dL. Ranges vary between labs."},
            {"question": "What causes high cortisol?",
             "answer": "Common causes include Cushing syndrome (pituitary or adrenal tumours, ectopic ACTH), exogenous steroid use, chronic stress, depression, alcoholism, and severe obesity."},
            {"question": "What are symptoms of high cortisol?",
             "answer": "Weight gain (face, upper back, abdomen), high blood pressure, elevated blood sugar, mood changes, thinning skin with easy bruising, muscle weakness, and purple stretch marks."},
            {"question": "What causes low cortisol?",
             "answer": "Addison disease (autoimmune adrenal destruction) is the most common cause of primary adrenal insufficiency. Secondary insufficiency occurs when the pituitary does not produce enough ACTH or when steroids are stopped too quickly."},
        ],
        "tr": [
            {"question": "Normal kortizol değeri nedir?",
             "answer": "Sabah kortizolü (06:00–08:00) yaklaşık 6–23 µg/dL (166–635 nmol/L), akşam ise 2–14 µg/dL'dir. Aralıklar laboratuvarlar arasında farklılık gösterebilir."},
            {"question": "Kortizol yüksekliğinin nedenleri nelerdir?",
             "answer": "Cushing sendromu, eksojen steroid kullanımı, kronik stres, depresyon, alkolizm ve ciddi obezite en yaygın nedenlerdir."},
            {"question": "Yüksek kortizol belirtileri nelerdir?",
             "answer": "Yüzde, sırtta ve karında kilo artışı, yüksek tansiyon, yüksek kan şekeri, ruh hali değişiklikleri, incelmiş cilt ve kolay çürükler, kas güçsüzlüğü ve mor çatlaklar."},
            {"question": "Düşük kortizolün nedenleri nelerdir?",
             "answer": "Addison hastalığı (otoimmün adrenal yıkım) primer adrenal yetmezliğin en sık nedenidir. Sekonder yetmezlik hipofizin yeterli ACTH üretmemesi veya steroidlerin çok hızlı kesilmesiyle ortaya çıkar."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de cortisol?",
             "answer": "El cortisol matutino (6–8 AM) normal es aproximadamente 6–23 µg/dL (166–635 nmol/L). Los niveles vespertinos son más bajos, alrededor de 2–14 µg/dL."},
            {"question": "¿Qué causa el cortisol alto?",
             "answer": "Síndrome de Cushing, uso de esteroides exógenos, estrés crónico, depresión, alcoholismo y obesidad severa."},
            {"question": "¿Cuáles son los síntomas de cortisol alto?",
             "answer": "Aumento de peso (cara, espalda, abdomen), hipertensión, hiperglucemia, cambios de humor, piel adelgazada con hematomas fáciles y debilidad muscular."},
            {"question": "¿Qué causa el cortisol bajo?",
             "answer": "La enfermedad de Addison es la causa más común. La insuficiencia suprarrenal secundaria ocurre por ACTH insuficiente o retirada rápida de esteroides."},
        ],
        "de": [
            {"question": "Was ist ein normaler Cortisolwert?",
             "answer": "Normales Morgencortisol (6–8 Uhr): ca. 6–23 µg/dL (166–635 nmol/L). Abendwerte sind niedriger, ca. 2–14 µg/dL."},
            {"question": "Was verursacht hohes Cortisol?",
             "answer": "Cushing-Syndrom, exogene Steroide, chronischer Stress, Depression, Alkoholismus und schwere Adipositas."},
            {"question": "Was sind Symptome von hohem Cortisol?",
             "answer": "Gewichtszunahme (Gesicht, Rücken, Bauch), Bluthochdruck, Hyperglykämie, Stimmungsschwankungen, dünne Haut mit Blutergüssen und Muskelschwäche."},
            {"question": "Was verursacht niedriges Cortisol?",
             "answer": "Morbus Addison (autoimmune Zerstörung der Nebennieren) ist die häufigste Ursache. Sekundäre Insuffizienz entsteht bei zu wenig ACTH oder zu schnellem Steroidentzug."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de cortisol ?",
             "answer": "Le cortisol matinal (6–8 h) normal est d'environ 6–23 µg/dL (166–635 nmol/L). Les taux du soir sont plus bas, environ 2–14 µg/dL."},
            {"question": "Quelles sont les causes d'un cortisol élevé ?",
             "answer": "Syndrome de Cushing, glucocorticoïdes exogènes, stress chronique, dépression, alcoolisme et obésité sévère."},
            {"question": "Quels sont les symptômes d'un cortisol élevé ?",
             "answer": "Prise de poids (visage, dos, abdomen), hypertension, hyperglycémie, troubles de l'humeur, peau amincie avec ecchymoses et faiblesse musculaire."},
            {"question": "Quelles sont les causes d'un cortisol bas ?",
             "answer": "La maladie d'Addison est la cause la plus fréquente. L'insuffisance surrénale secondaire survient par ACTH insuffisant ou sevrage stéroïdien rapide."},
        ],
        "it": [
            {"question": "Qual è il valore normale del cortisolo?",
             "answer": "Il cortisolo mattutino (6–8) normale è circa 6–23 µg/dL (166–635 nmol/L). I valori serali sono più bassi, circa 2–14 µg/dL."},
            {"question": "Cosa causa il cortisolo alto?",
             "answer": "Sindrome di Cushing, glucocorticoidi esogeni, stress cronico, depressione, alcolismo e obesità grave."},
            {"question": "Quali sono i sintomi del cortisolo alto?",
             "answer": "Aumento di peso (viso, schiena, addome), ipertensione, iperglicemia, alterazioni dell'umore, cute assottigliata con lividi e debolezza muscolare."},
            {"question": "Cosa causa il cortisolo basso?",
             "answer": "Il morbo di Addison è la causa più comune. L'insufficienza surrenalica secondaria si verifica per ACTH insufficiente o sospensione rapida di steroidi."},
        ],
        "he": [
            {"question": "מהו ערך קורטיזול תקין?",
             "answer": "קורטיזול בוקר (6–8) תקין הוא בערך 6–23 µg/dL (166–635 nmol/L). ערכי ערב נמוכים יותר, סביב 2–14 µg/dL."},
            {"question": "מה גורם לקורטיזול גבוה?",
             "answer": "תסמונת קושינג, גלוקוקורטיקואידים חיצוניים, סטרס כרוני, דיכאון, אלכוהוליזם והשמנת יתר חמורה."},
            {"question": "מה גורם לקורטיזול נמוך?",
             "answer": "מחלת אדיסון (הרס אוטואימוני של האדרנל) היא הגורם השכיח ביותר. אי-ספיקה משנית נגרמת מ-ACTH לא מספיק או הפסקה מהירה מדי של סטרואידים."},
            {"question": "מתי לפנות לרופא בגלל קורטיזול?",
             "answer": "פנו לרופא אם הקורטיזול מחוץ לטווח. פנו לחירום בכאב בטן פתאומי חמור, הקאות, חולשה קיצונית או בלבול."},
        ],
        "hi": [
            {"question": "सामान्य कोर्टिसोल कितना होना चाहिए?",
             "answer": "सुबह का सामान्य कोर्टिसोल (6–8 AM) लगभग 6–23 µg/dL (166–635 nmol/L) है। शाम का स्तर कम, लगभग 2–14 µg/dL होता है।"},
            {"question": "कोर्टिसोल बढ़ने के कारण क्या हैं?",
             "answer": "कुशिंग सिंड्रोम, बाहरी स्टेरॉइड उपयोग, क्रोनिक स्ट्रेस, डिप्रेशन, अल्कोहलिज़्म और गंभीर मोटापा।"},
            {"question": "उच्च कोर्टिसोल के लक्षण क्या हैं?",
             "answer": "चेहरे, पीठ और पेट पर वज़न बढ़ना, हाई ब्लड प्रेशर, हाई ब्लड शुगर, मूड बदलाव, पतली त्वचा और आसान नील, माँसपेशियों में कमज़ोरी।"},
            {"question": "कोर्टिसोल कम होने के कारण क्या हैं?",
             "answer": "एडिसन रोग (ऑटोइम्यून एड्रेनल विनाश) सबसे आम कारण है। सेकेंडरी इंसफिशिएंसी ACTH कम होने या स्टेरॉइड तेज़ी से बंद करने से होती है।"},
        ],
        "ar": [
            {"question": "ما هو مستوى الكورتيزول الطبيعي؟",
             "answer": "كورتيزول الصباح (6–8) الطبيعي حوالي 6–23 µg/dL (166–635 nmol/L). مستويات المساء أقل، حوالي 2–14 µg/dL."},
            {"question": "ما أسباب ارتفاع الكورتيزول؟",
             "answer": "متلازمة كوشينغ، غلوكوكورتيكويدات خارجية، إجهاد مزمن، اكتئاب، إدمان كحول وسمنة مفرطة."},
            {"question": "ما أعراض الكورتيزول المرتفع؟",
             "answer": "زيادة في الوزن (الوجه، الظهر، البطن)، ارتفاع ضغط الدم، ارتفاع سكر الدم، تقلبات مزاجية، ترقق الجلد مع كدمات وضعف عضلي."},
            {"question": "ما أسباب انخفاض الكورتيزول؟",
             "answer": "مرض أديسون (تدمير مناعي ذاتي للكظر) هو الأكثر شيوعاً. القصور الثانوي يحدث بسبب ACTH غير كافٍ أو إيقاف الستيرويدات بسرعة."},
        ],
    }
