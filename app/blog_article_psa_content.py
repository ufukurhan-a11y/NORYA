# -*- coding: utf-8 -*-
"""
PSA (Prostate Specific Antigen) blog article — full body content for all 9 languages.
Used by blog_i18n._article_psa().
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
            heading="PSA kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>PSA testi</strong> (Prostat Spesifik Antijen), prostat bezi tarafından üretilen bir proteinin "
                "kandaki düzeyini ölçen basit bir kan testidir. PSA kan testi, prostat kanseri taramasında en yaygın "
                "kullanılan laboratuvar testlerinden biridir; ancak PSA yüksekliği her zaman kanser anlamına gelmez. "
                "İyi huylu prostat büyümesi (BPH), prostatit ve hatta yakın zamanda yapılan bazı fiziksel aktiviteler de "
                "PSA düzeylerini geçici olarak artırabilir.</p>"
                "<p>Bu rehberde PSA normal değerleri, PSA yüksekliğinin olası nedenleri ve ne zaman doktora başvurmanız "
                "gerektiğini açıklıyoruz. Buradaki bilgiler eğitim amaçlıdır; kesin tanı ve tedavi için mutlaka bir "
                "üroloji uzmanına danışın.</p>"
                "<p>PSA testi özellikle 50 yaş üstü erkeklerde düzenli olarak önerilir. Ailede prostat kanseri öyküsü "
                "bulunan kişilerde tarama 40-45 yaşlarında başlatılabilir. Erken teşhis, tedavi başarısını önemli ölçüde "
                "artırır; bu nedenle PSA düzeylerinin düzenli takibi büyük önem taşır.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="PSA normal değerleri (referans aralıkları)",
            body_html=(
                "<p>PSA normal değeri genellikle <strong>0–4 ng/mL</strong> aralığında kabul edilir; ancak bu eşik yaşa "
                "göre değişiklik gösterir. Yaşa göre kabul edilen PSA normal aralıkları aşağıdaki tabloda özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Yaş grubu</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PSA normal aralığı</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">40–49 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50–59 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">60–69 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">70–79 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6,5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>4 ng/mL üzerindeki PSA düzeyleri \"yüksek PSA\" olarak değerlendirilir ve ileri tetkik gerektirebilir. "
                "Ancak bazı erkeklerde PSA normal değeri 4 ng/mL altında olsa bile prostat kanseri tespit edilebilirken, "
                "yüksek PSA değerine sahip birçok erkekte kanser bulunmayabilir. Bu nedenle tek başına PSA testi "
                "tanı koydurmaz; klinik değerlendirme ile birlikte ele alınmalıdır.</p>"
                "<p>Serbest PSA / toplam PSA oranı da önemli bir göstergedir. Serbest PSA oranı düşük olan hastalarda "
                "prostat kanseri riski görece daha yüksek kabul edilir. Doktorunuz gerektiğinde serbest PSA testi de "
                "isteyebilir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="PSA yüksekliğinin nedenleri",
            body_html=(
                "<p>PSA yüksekliği birçok farklı nedene bağlı olabilir. Yüksek PSA düzeyi her zaman prostat kanseri "
                "anlamına gelmez. Aşağıda PSA düzeylerini artırabilecek başlıca durumlar sıralanmıştır:</p>"
                "<ul>"
                "<li><strong>İyi huylu prostat büyümesi (BPH):</strong> Prostat bezinin yaşla birlikte büyümesi, PSA "
                "yüksekliğinin en yaygın nedenlerinden biridir. BPH kanser değildir ancak idrar yolu semptomlarına neden olabilir.</li>"
                "<li><strong>Prostatit (prostat iltihabı):</strong> Bakteriyel veya kronik prostatit, prostat dokusundaki "
                "inflamasyon nedeniyle PSA düzeylerini belirgin şekilde yükseltebilir.</li>"
                "<li><strong>İdrar yolu enfeksiyonu:</strong> Alt üriner sistem enfeksiyonları geçici PSA yüksekliğine yol açabilir.</li>"
                "<li><strong>Prostat kanseri:</strong> Yüksek PSA değerlerinin en önemli ayırıcı tanılarından biridir. "
                "Özellikle sürekli ve hızla yükselen PSA düzeyleri daha dikkatli değerlendirilmelidir.</li>"
                "<li><strong>Fiziksel etkenler:</strong> Bisiklet sürme, cinsel aktivite, rektal muayene veya prostat "
                "biyopsisi gibi işlemler PSA düzeylerini geçici olarak yükseltebilir.</li>"
                "<li><strong>İlaçlar:</strong> 5-alfa redüktaz inhibitörleri (finasterid, dutasterid) PSA düzeyini yaklaşık "
                "%50 oranında düşürür; bu ilaçları kullanan hastalarda sonuçlar buna göre yorumlanmalıdır.</li>"
                "</ul>"
                "<p>Doktorunuz, PSA yüksekliğinin nedenini belirlemek için parmakla rektal muayene, serbest PSA testi, "
                "prostat MR'ı veya gerekirse biyopsi isteyebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>PSA testi sonucunuz referans aralığının üstünde çıktıysa panik yapmayın, ancak mutlaka bir üroloji "
                "uzmanına başvurun. Özellikle PSA düzeyleri ardışık ölçümlerde yükselme eğilimi gösteriyorsa, ailede "
                "prostat kanseri öyküsü varsa veya idrara çıkmada güçlük, sık idrara çıkma, idrarda kan gibi semptomlar "
                "eşlik ediyorsa değerlendirme geciktirilmemelidir.</p>"
                "<p>50 yaş üstü tüm erkeklere yıllık PSA kan testi ve parmakla rektal muayene önerilir. Yüksek risk "
                "grubundaki erkekler (birinci derece akrabada prostat kanseri öyküsü olanlar) 40–45 yaşından itibaren "
                "taramaya başlamalıdır. PSA testi tek başına tanı aracı olmasa da, erken tanıda en değerli tarama "
                "testlerinden biri olmaya devam etmektedir.</p>"
                "<p>Unutmayın: yüksek PSA değeri kesin kanser tanısı koymaz. Doktorunuz ek tetkiklerle durumu "
                "aydınlatacak ve gerekli tedavi planını oluşturacaktır. Düzenli takip ve erken müdahale, prostat "
                "kanseri tedavisinde başarı oranını önemli ölçüde artırır.</p>"
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
            heading="PSA blood test: what your results mean",
            body_html=(
                "<p>The <strong>PSA test</strong> (Prostate-Specific Antigen) measures the level of a protein produced by "
                "the prostate gland in your blood. A PSA blood test is one of the most widely used tools in "
                "prostate cancer screening, yet an elevated PSA does not automatically mean cancer. Benign prostatic "
                "hyperplasia (BPH), prostatitis, urinary tract infections, and even recent physical activity can all "
                "raise PSA levels temporarily.</p>"
                "<p>In this guide we explain PSA normal ranges by age, the most common causes of high PSA, and when you "
                "should see a doctor. The information here is educational&mdash;always discuss your PSA test results "
                "with a qualified healthcare professional for a proper diagnosis.</p>"
                "<p>Routine PSA blood test screening is generally recommended for men over 50. Men with a family history "
                "of prostate cancer may begin screening as early as age 40&ndash;45. Early detection significantly "
                "improves treatment outcomes, making regular monitoring of PSA levels an important part of men's health.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="PSA normal range by age",
            body_html=(
                "<p>The generally accepted <strong>PSA normal range</strong> is <strong>0–4 ng/mL</strong>, but this "
                "threshold varies with age. Age-specific reference ranges are summarised in the table below:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Age group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PSA normal range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">40–49 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50–59 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">60–69 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">70–79 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6.5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>PSA levels above 4 ng/mL are considered <strong>elevated PSA</strong> and may warrant further "
                "investigation. However, some men with PSA levels below 4 ng/mL can still have prostate cancer, while "
                "many men with high PSA values have no cancer at all. A single PSA test result does not diagnose "
                "cancer; it must be interpreted alongside clinical findings.</p>"
                "<p>The free-to-total PSA ratio is another useful marker. A lower percentage of free PSA is associated "
                "with a higher risk of prostate cancer. Your doctor may order a free PSA test to help distinguish "
                "between benign and malignant causes of elevated PSA levels.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high PSA levels",
            body_html=(
                "<p>A <strong>high PSA</strong> reading does not necessarily indicate prostate cancer. Several benign "
                "conditions can elevate PSA levels. The most common causes of elevated PSA include:</p>"
                "<ul>"
                "<li><strong>Benign prostatic hyperplasia (BPH):</strong> Age-related enlargement of the prostate gland is "
                "one of the most frequent reasons for high PSA. BPH is not cancer but can cause urinary symptoms.</li>"
                "<li><strong>Prostatitis:</strong> Bacterial or chronic inflammation of the prostate can significantly "
                "raise PSA levels due to tissue irritation and leakage of PSA into the bloodstream.</li>"
                "<li><strong>Urinary tract infection (UTI):</strong> Lower urinary tract infections can temporarily "
                "elevate PSA levels.</li>"
                "<li><strong>Prostate cancer:</strong> Persistently elevated or rapidly rising PSA levels are an important "
                "indicator that further evaluation for prostate cancer is needed.</li>"
                "<li><strong>Physical factors:</strong> Cycling, sexual activity, digital rectal examination, or prostate "
                "biopsy can temporarily increase PSA levels.</li>"
                "<li><strong>Medications:</strong> 5-alpha reductase inhibitors (finasteride, dutasteride) reduce PSA "
                "by approximately 50%; results must be interpreted accordingly in patients taking these drugs.</li>"
                "</ul>"
                "<p>To determine the cause of high PSA, your doctor may perform a digital rectal exam, order a free PSA "
                "test, request a prostate MRI, or recommend a biopsy if clinically indicated.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your PSA blood test result is above the reference range, do not panic&mdash;but do consult a "
                "urologist promptly. Evaluation should not be delayed if PSA levels show a rising trend across "
                "consecutive measurements, if there is a family history of prostate cancer, or if you experience "
                "symptoms such as difficulty urinating, frequent urination, or blood in the urine.</p>"
                "<p>Annual PSA test screening combined with a digital rectal exam is recommended for all men over 50. "
                "Men at higher risk (those with a first-degree relative who had prostate cancer) should start screening "
                "at age 40&ndash;45. While the PSA test alone is not a diagnostic tool, it remains one of the most "
                "valuable screening tests for early detection of prostate cancer.</p>"
                "<p>Remember: a high PSA value does not confirm a cancer diagnosis. Your doctor will use additional tests "
                "to clarify the situation and create an appropriate treatment plan. Regular monitoring and early "
                "intervention significantly improve outcomes in prostate cancer treatment.</p>"
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
            heading="Prueba de PSA en sangre: qué significan sus resultados",
            body_html=(
                "<p>La <strong>prueba de PSA</strong> (Antígeno Prostático Específico) mide el nivel de una proteína "
                "producida por la glándula prostática en la sangre. La prueba de PSA es una de las herramientas más "
                "utilizadas en el cribado del cáncer de próstata, aunque un PSA alto no significa automáticamente que "
                "exista cáncer. La hiperplasia benigna de próstata (HBP), la prostatitis, las infecciones urinarias e "
                "incluso la actividad física reciente pueden elevar temporalmente los niveles de PSA.</p>"
                "<p>En esta guía explicamos el rango normal de PSA según la edad, las causas más frecuentes de PSA alto "
                "y cuándo debe consultar al médico. Esta información es educativa; consulte siempre a un urólogo para "
                "un diagnóstico adecuado.</p>"
                "<p>La prueba de PSA en sangre se recomienda de forma rutinaria a hombres mayores de 50 años. Los hombres "
                "con antecedentes familiares de cáncer de próstata pueden comenzar el cribado entre los 40 y 45 años. "
                "La detección temprana mejora significativamente los resultados del tratamiento, por lo que el control "
                "regular de los niveles de PSA es fundamental para la salud masculina.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rango normal de PSA según la edad",
            body_html=(
                "<p>El <strong>rango normal de PSA</strong> generalmente aceptado es de <strong>0–4 ng/mL</strong>, "
                "aunque este umbral varía con la edad. Los rangos de referencia específicos por edad se resumen en la "
                "siguiente tabla:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo de edad</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal de PSA</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">40–49 años</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50–59 años</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">60–69 años</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">70–79 años</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6,5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Los niveles de PSA superiores a 4 ng/mL se consideran <strong>PSA alto</strong> y pueden requerir "
                "estudios complementarios. Sin embargo, algunos hombres con niveles de PSA por debajo de 4 ng/mL pueden "
                "tener cáncer de próstata, mientras que muchos con valores elevados no presentan cáncer. Una sola prueba "
                "de PSA no diagnostica cáncer; debe interpretarse junto con la evaluación clínica.</p>"
                "<p>La relación PSA libre/PSA total es otro marcador útil. Un porcentaje bajo de PSA libre se asocia con "
                "mayor riesgo de cáncer de próstata. Su médico puede solicitar una prueba de PSA libre para distinguir "
                "entre causas benignas y malignas de niveles de PSA elevados.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de niveles de PSA elevados",
            body_html=(
                "<p>Un resultado de <strong>PSA alto</strong> no indica necesariamente cáncer de próstata. Varias "
                "condiciones benignas pueden elevar los niveles de PSA. Las causas más comunes incluyen:</p>"
                "<ul>"
                "<li><strong>Hiperplasia benigna de próstata (HBP):</strong> El agrandamiento de la próstata relacionado "
                "con la edad es una de las razones más frecuentes de PSA alto. La HBP no es cáncer, pero puede causar "
                "síntomas urinarios.</li>"
                "<li><strong>Prostatitis:</strong> La inflamación bacteriana o crónica de la próstata puede elevar "
                "significativamente los niveles de PSA.</li>"
                "<li><strong>Infección del tracto urinario:</strong> Las infecciones urinarias pueden elevar "
                "temporalmente los niveles de PSA.</li>"
                "<li><strong>Cáncer de próstata:</strong> Los niveles de PSA persistentemente elevados o en aumento "
                "rápido son un indicador importante que requiere evaluación adicional.</li>"
                "<li><strong>Factores físicos:</strong> Montar en bicicleta, la actividad sexual, el tacto rectal o una "
                "biopsia prostática pueden incrementar temporalmente los niveles de PSA.</li>"
                "<li><strong>Medicamentos:</strong> Los inhibidores de la 5-alfa reductasa (finasterida, dutasterida) "
                "reducen el PSA aproximadamente un 50 %; los resultados deben interpretarse en consecuencia.</li>"
                "</ul>"
                "<p>Para determinar la causa del PSA alto, su médico puede realizar un tacto rectal, solicitar PSA libre, "
                "pedir una resonancia magnética de próstata o recomendar una biopsia si está indicado clínicamente.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si su prueba de PSA en sangre arroja un resultado por encima del rango de referencia, no se "
                "alarme, pero consulte a un urólogo sin demora. La evaluación no debe retrasarse si los niveles de "
                "PSA muestran una tendencia ascendente, si hay antecedentes familiares de cáncer de próstata o si "
                "presenta síntomas como dificultad para orinar, micción frecuente o sangre en la orina.</p>"
                "<p>Se recomienda la prueba de PSA anual junto con un tacto rectal a todos los hombres mayores de 50 "
                "años. Los hombres con mayor riesgo deben comenzar el cribado a los 40–45 años. Aunque la prueba de "
                "PSA por sí sola no es una herramienta diagnóstica, sigue siendo uno de los tests de cribado más "
                "valiosos para la detección temprana del cáncer de próstata.</p>"
                "<p>Recuerde: un valor de PSA alto no confirma un diagnóstico de cáncer. Su médico utilizará pruebas "
                "adicionales para aclarar la situación. El seguimiento regular y la intervención temprana mejoran "
                "significativamente los resultados en el tratamiento del cáncer de próstata.</p>"
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
            heading="PSA-Test: Was Ihre Blutwerte bedeuten",
            body_html=(
                "<p>Der <strong>PSA-Test</strong> (Prostata-spezifisches Antigen) misst die Konzentration eines Proteins, "
                "das von der Prostata produziert wird, in Ihrem Blut. Der PSA-Test ist eines der am häufigsten "
                "eingesetzten Verfahren beim Prostatakrebs-Screening. Ein erhöhter PSA-Wert bedeutet jedoch nicht "
                "automatisch Krebs. Die gutartige Prostatavergrößerung (BPH), eine Prostatitis, Harnwegsinfekte und "
                "sogar körperliche Aktivität können die PSA-Werte vorübergehend ansteigen lassen.</p>"
                "<p>In diesem Ratgeber erläutern wir die PSA-Normalwerte nach Alter, die häufigsten Ursachen für einen "
                "erhöhten PSA-Wert und wann Sie einen Arzt aufsuchen sollten. Die Inhalte dienen der Aufklärung&mdash;"
                "für eine Diagnose und Behandlung wenden Sie sich bitte an einen Urologen.</p>"
                "<p>Ein regelmäßiger PSA-Test wird Männern ab 50 Jahren empfohlen. Bei familiärer Vorbelastung mit "
                "Prostatakrebs kann das Screening bereits mit 40&ndash;45 Jahren beginnen. Die Früherkennung verbessert "
                "die Behandlungsergebnisse erheblich, weshalb die regelmäßige Kontrolle der PSA-Werte ein wichtiger "
                "Bestandteil der Männergesundheit ist.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="PSA-Normalwerte nach Alter",
            body_html=(
                "<p>Der allgemein akzeptierte <strong>PSA-Normalwert</strong> liegt bei <strong>0–4 ng/mL</strong>, wobei "
                "dieser Grenzwert altersabhängig variiert. Die altersspezifischen Referenzbereiche sind in der folgenden "
                "Tabelle zusammengefasst:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Altersgruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PSA-Normalwerte</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">40–49 Jahre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50–59 Jahre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">60–69 Jahre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">70–79 Jahre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6,5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>PSA-Werte über 4 ng/mL gelten als <strong>erhöhter PSA</strong> und können weitere Untersuchungen "
                "erfordern. Allerdings kann bei manchen Männern mit PSA-Werten unter 4 ng/mL dennoch Prostatakrebs "
                "vorliegen, während viele Männer mit hohem PSA-Wert keinen Krebs haben. Ein einzelner PSA-Test stellt "
                "keine Diagnose; er muss zusammen mit dem klinischen Befund interpretiert werden.</p>"
                "<p>Das Verhältnis von freiem zu gebundenem PSA ist ein weiterer hilfreicher Marker. Ein niedriger Anteil "
                "an freiem PSA wird mit einem höheren Prostatakrebs-Risiko assoziiert. Ihr Arzt kann einen Test auf "
                "freies PSA anordnen, um zwischen gutartigen und bösartigen Ursachen eines erhöhten PSA-Werts zu "
                "unterscheiden.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für einen erhöhten PSA-Wert",
            body_html=(
                "<p>Ein <strong>erhöhter PSA</strong>-Wert weist nicht zwangsläufig auf Prostatakrebs hin. Verschiedene "
                "gutartige Erkrankungen können die PSA-Werte erhöhen. Die häufigsten Ursachen sind:</p>"
                "<ul>"
                "<li><strong>Benigne Prostatahyperplasie (BPH):</strong> Die altersbedingte Vergrößerung der Prostata ist "
                "eine der häufigsten Ursachen für einen erhöhten PSA-Wert. BPH ist kein Krebs, kann aber Beschwerden beim "
                "Wasserlassen verursachen.</li>"
                "<li><strong>Prostatitis:</strong> Eine bakterielle oder chronische Entzündung der Prostata kann den "
                "PSA-Wert durch Gewebereizung deutlich erhöhen.</li>"
                "<li><strong>Harnwegsinfektion:</strong> Infektionen der unteren Harnwege können die PSA-Werte "
                "vorübergehend ansteigen lassen.</li>"
                "<li><strong>Prostatakrebs:</strong> Dauerhaft erhöhte oder schnell ansteigende PSA-Werte sind ein "
                "wichtiger Hinweis, der eine weiterführende Abklärung erfordert.</li>"
                "<li><strong>Physische Faktoren:</strong> Radfahren, sexuelle Aktivität, die digitale rektale "
                "Untersuchung oder eine Prostatabiopsie können den PSA-Wert vorübergehend erhöhen.</li>"
                "<li><strong>Medikamente:</strong> 5-Alpha-Reduktase-Hemmer (Finasterid, Dutasterid) senken den PSA-Wert "
                "um etwa 50 %; Ergebnisse müssen bei Patienten unter dieser Medikation entsprechend interpretiert werden.</li>"
                "</ul>"
                "<p>Um die Ursache eines erhöhten PSA-Werts abzuklären, kann Ihr Arzt eine rektale Tastuntersuchung "
                "durchführen, freies PSA bestimmen lassen, eine Prostata-MRT anordnen oder eine Biopsie empfehlen.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Liegt Ihr PSA-Test-Ergebnis über dem Referenzbereich, bewahren Sie Ruhe, suchen Sie aber zeitnah einen "
                "Urologen auf. Eine Abklärung sollte nicht verzögert werden, wenn die PSA-Werte in aufeinanderfolgenden "
                "Messungen ansteigen, eine familiäre Belastung mit Prostatakrebs vorliegt oder Symptome wie "
                "Schwierigkeiten beim Wasserlassen, häufiges Wasserlassen oder Blut im Urin auftreten.</p>"
                "<p>Für alle Männer über 50 wird ein jährlicher PSA-Test in Kombination mit einer rektalen "
                "Tastuntersuchung empfohlen. Männer mit erhöhtem Risiko sollten das Screening mit 40&ndash;45 Jahren "
                "beginnen. Obwohl der PSA-Test allein kein diagnostisches Verfahren ist, bleibt er einer der wertvollsten "
                "Screening-Tests für die Früherkennung von Prostatakrebs.</p>"
                "<p>Denken Sie daran: Ein erhöhter PSA-Wert bestätigt keine Krebsdiagnose. Ihr Arzt wird zusätzliche "
                "Untersuchungen durchführen, um die Ursache zu klären und gegebenenfalls einen Behandlungsplan zu "
                "erstellen. Regelmäßige Kontrollen und frühzeitiges Eingreifen verbessern die Prognose bei "
                "Prostatakrebs erheblich.</p>"
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
            heading="Test PSA : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test PSA</strong> (Antigène Prostatique Spécifique) mesure le taux d'une protéine produite "
                "par la prostate dans le sang. Le test PSA est l'un des outils les plus utilisés dans le dépistage du "
                "cancer de la prostate, mais un taux de PSA élevé ne signifie pas automatiquement un cancer. "
                "L'hypertrophie bénigne de la prostate (HBP), la prostatite, les infections urinaires et même l'activité "
                "physique récente peuvent augmenter temporairement les taux de PSA.</p>"
                "<p>Dans ce guide, nous expliquons les valeurs normales du PSA selon l'âge, les causes les plus "
                "fréquentes d'un PSA élevé et quand consulter un médecin. Ces informations sont à visée éducative&mdash;"
                "consultez toujours un urologue pour un diagnostic approprié.</p>"
                "<p>Un test PSA de dépistage est généralement recommandé pour les hommes de plus de 50 ans. Les hommes "
                "ayant des antécédents familiaux de cancer de la prostate peuvent commencer le dépistage dès 40&ndash;45 "
                "ans. La détection précoce améliore considérablement les résultats du traitement, ce qui fait du suivi "
                "régulier du taux de PSA un élément important de la santé masculine.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales du PSA selon l'âge",
            body_html=(
                "<p>La plage de <strong>valeurs normales du PSA</strong> généralement admise est de <strong>0–4 ng/mL"
                "</strong>, mais ce seuil varie avec l'âge. Les intervalles de référence par tranche d'âge sont résumés "
                "dans le tableau ci-dessous :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tranche d\'âge</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valeurs normales du PSA</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">40–49 ans</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50–59 ans</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">60–69 ans</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">70–79 ans</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6,5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Un taux de PSA supérieur à 4 ng/mL est considéré comme un <strong>PSA élevé</strong> et peut "
                "nécessiter des examens complémentaires. Cependant, certains hommes ayant un taux de PSA inférieur à "
                "4 ng/mL peuvent avoir un cancer de la prostate, tandis que de nombreux hommes avec un PSA élevé n'ont "
                "pas de cancer. Un seul résultat de test PSA ne pose pas de diagnostic ; il doit être interprété en "
                "fonction du contexte clinique.</p>"
                "<p>Le rapport PSA libre/PSA total est un autre marqueur utile. Un faible pourcentage de PSA libre est "
                "associé à un risque accru de cancer de la prostate. Votre médecin peut demander un dosage du PSA libre "
                "pour distinguer les causes bénignes des causes malignes d'un taux de PSA élevé.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un taux de PSA élevé",
            body_html=(
                "<p>Un <strong>PSA élevé</strong> ne signifie pas forcément un cancer de la prostate. Plusieurs "
                "affections bénignes peuvent augmenter les taux de PSA. Les causes les plus courantes sont :</p>"
                "<ul>"
                "<li><strong>Hypertrophie bénigne de la prostate (HBP) :</strong> L'augmentation de volume de la prostate "
                "liée à l'âge est l'une des causes les plus fréquentes d'un PSA élevé. L'HBP n'est pas un cancer mais "
                "peut provoquer des symptômes urinaires.</li>"
                "<li><strong>Prostatite :</strong> Une inflammation bactérienne ou chronique de la prostate peut "
                "augmenter significativement le taux de PSA.</li>"
                "<li><strong>Infection urinaire :</strong> Les infections des voies urinaires basses peuvent élever "
                "temporairement les taux de PSA.</li>"
                "<li><strong>Cancer de la prostate :</strong> Des taux de PSA durablement élevés ou en augmentation "
                "rapide sont un indicateur important nécessitant une évaluation approfondie.</li>"
                "<li><strong>Facteurs physiques :</strong> Le vélo, l'activité sexuelle, le toucher rectal ou une biopsie "
                "prostatique peuvent augmenter temporairement les taux de PSA.</li>"
                "<li><strong>Médicaments :</strong> Les inhibiteurs de la 5-alpha réductase (finastéride, dutastéride) "
                "réduisent le PSA d'environ 50 % ; les résultats doivent être interprétés en conséquence.</li>"
                "</ul>"
                "<p>Pour déterminer la cause d'un taux de PSA élevé, votre médecin peut réaliser un toucher rectal, "
                "doser le PSA libre, prescrire une IRM prostatique ou recommander une biopsie si nécessaire.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si votre résultat de test PSA dépasse l'intervalle de référence, ne paniquez pas, mais consultez "
                "rapidement un urologue. L'évaluation ne doit pas être retardée si les taux de PSA montrent une "
                "tendance à la hausse, s'il existe des antécédents familiaux de cancer de la prostate ou si vous "
                "présentez des symptômes tels que des difficultés à uriner, des mictions fréquentes ou du sang dans "
                "les urines.</p>"
                "<p>Un dépistage annuel par test PSA associé à un toucher rectal est recommandé à tous les hommes de "
                "plus de 50 ans. Les hommes à risque élevé devraient commencer le dépistage entre 40 et 45 ans. Bien "
                "que le test PSA seul ne soit pas un outil diagnostique, il reste l'un des tests de dépistage les plus "
                "précieux pour la détection précoce du cancer de la prostate.</p>"
                "<p>N'oubliez pas : un taux de PSA élevé ne confirme pas un diagnostic de cancer. Votre médecin "
                "effectuera des examens complémentaires pour clarifier la situation. Un suivi régulier et une "
                "intervention précoce améliorent significativement les résultats du traitement du cancer de la "
                "prostate.</p>"
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
            heading="Test del PSA: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test del PSA</strong> (Antigene Prostatico Specifico) misura il livello di una proteina "
                "prodotta dalla ghiandola prostatica nel sangue. Il test del PSA è uno degli strumenti più utilizzati "
                "nello screening del cancro alla prostata, ma un PSA alto non significa automaticamente che ci sia un "
                "tumore. L'iperplasia prostatica benigna (IPB), la prostatite, le infezioni urinarie e perfino "
                "l'attività fisica recente possono aumentare temporaneamente i livelli di PSA.</p>"
                "<p>In questa guida spieghiamo i valori normali del PSA in base all'età, le cause più comuni di PSA "
                "alto e quando è necessario rivolgersi al medico. Le informazioni qui contenute hanno scopo educativo&mdash;"
                "per una diagnosi adeguata consultate sempre un urologo.</p>"
                "<p>Lo screening con il test del PSA è generalmente raccomandato per gli uomini sopra i 50 anni. "
                "Gli uomini con una storia familiare di cancro alla prostata possono iniziare lo screening già a "
                "40&ndash;45 anni. La diagnosi precoce migliora significativamente i risultati del trattamento, "
                "rendendo il monitoraggio regolare dei livelli di PSA un elemento importante della salute maschile.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del PSA per età",
            body_html=(
                "<p>L'intervallo di <strong>valori normali del PSA</strong> generalmente accettato è di <strong>0–4 "
                "ng/mL</strong>, ma questa soglia varia con l'età. Gli intervalli di riferimento specifici per età "
                "sono riassunti nella tabella seguente:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fascia d\'età</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valori normali del PSA</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">40–49 anni</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50–59 anni</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">60–69 anni</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4,5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">70–79 anni</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6,5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>Livelli di PSA superiori a 4 ng/mL sono considerati <strong>PSA alto</strong> e possono richiedere "
                "ulteriori accertamenti. Tuttavia, alcuni uomini con livelli di PSA inferiori a 4 ng/mL possono avere "
                "il cancro alla prostata, mentre molti uomini con valori elevati non presentano alcun tumore. Un singolo "
                "risultato del test del PSA non è sufficiente per una diagnosi: deve essere interpretato nel contesto "
                "clinico complessivo.</p>"
                "<p>Il rapporto PSA libero/PSA totale è un altro marcatore utile. Una percentuale bassa di PSA libero "
                "è associata a un rischio maggiore di cancro alla prostata. Il medico può richiedere un test del PSA "
                "libero per distinguere tra cause benigne e maligne di livelli di PSA elevati.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di livelli di PSA elevati",
            body_html=(
                "<p>Un risultato di <strong>PSA alto</strong> non indica necessariamente il cancro alla prostata. "
                "Diverse condizioni benigne possono elevare i livelli di PSA. Le cause più comuni includono:</p>"
                "<ul>"
                "<li><strong>Iperplasia prostatica benigna (IPB):</strong> L'ingrossamento della prostata legato all'età "
                "è una delle ragioni più frequenti di PSA alto. L'IPB non è un tumore, ma può causare sintomi "
                "urinari.</li>"
                "<li><strong>Prostatite:</strong> L'infiammazione batterica o cronica della prostata può aumentare "
                "significativamente i livelli di PSA.</li>"
                "<li><strong>Infezione delle vie urinarie:</strong> Le infezioni urinarie possono elevare temporaneamente "
                "i livelli di PSA.</li>"
                "<li><strong>Cancro alla prostata:</strong> Livelli di PSA persistentemente elevati o in rapido aumento "
                "sono un indicatore importante che richiede ulteriori valutazioni.</li>"
                "<li><strong>Fattori fisici:</strong> Ciclismo, attività sessuale, esplorazione rettale digitale o "
                "biopsia prostatica possono aumentare temporaneamente i livelli di PSA.</li>"
                "<li><strong>Farmaci:</strong> Gli inibitori della 5-alfa reduttasi (finasteride, dutasteride) riducono "
                "il PSA di circa il 50 %; i risultati devono essere interpretati di conseguenza.</li>"
                "</ul>"
                "<p>Per determinare la causa del PSA alto, il medico può eseguire un'esplorazione rettale digitale, "
                "richiedere il dosaggio del PSA libero, prescrivere una risonanza magnetica della prostata o "
                "consigliare una biopsia se indicato clinicamente.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se il risultato del test del PSA è superiore all'intervallo di riferimento, non allarmatevi ma "
                "rivolgetevi tempestivamente a un urologo. La valutazione non deve essere ritardata se i livelli di "
                "PSA mostrano una tendenza al rialzo, se esiste una storia familiare di cancro alla prostata o se "
                "si manifestano sintomi come difficoltà a urinare, minzione frequente o sangue nelle urine.</p>"
                "<p>Si raccomanda uno screening annuale con test del PSA e un'esplorazione rettale digitale a tutti gli "
                "uomini sopra i 50 anni. Gli uomini a rischio elevato dovrebbero iniziare lo screening a 40&ndash;45 "
                "anni. Sebbene il test del PSA da solo non sia uno strumento diagnostico, resta uno dei test di "
                "screening più preziosi per la diagnosi precoce del cancro alla prostata.</p>"
                "<p>Ricordate: un valore di PSA alto non conferma una diagnosi di cancro. Il vostro medico effettuerà "
                "ulteriori esami per chiarire la situazione. Il monitoraggio regolare e l'intervento precoce migliorano "
                "significativamente i risultati nel trattamento del cancro alla prostata.</p>"
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
            heading="בדיקת PSA בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת PSA</strong> (אנטיגן ספציפי לערמונית) מודדת את רמת החלבון שמיוצר על ידי בלוטת "
                "הערמונית בדם. בדיקת PSA היא אחד הכלים הנפוצים ביותר לסקירת סרטן הערמונית, אך ערך PSA גבוה "
                "אינו מעיד בהכרח על סרטן. הגדלה שפירה של הערמונית (BPH), דלקת הערמונית, זיהומים בדרכי השתן ואפילו "
                "פעילות גופנית עשויים להעלות באופן זמני את רמות ה-PSA.</p>"
                "<p>במדריך זה נסביר את טווח ערך PSA תקין לפי גיל, את הגורמים השכיחים ביותר ל-PSA גבוה ומתי יש "
                "לפנות לרופא. המידע כאן הוא לצורכי הסברה בלבד&mdash;יש להתייעץ תמיד עם אורולוג לצורך אבחון מדויק.</p>"
                "<p>בדיקת PSA מומלצת באופן שגרתי לגברים מעל גיל 50. גברים עם היסטוריה משפחתית של סרטן הערמונית "
                "עשויים להתחיל סקירה כבר בגיל 40&ndash;45. גילוי מוקדם משפר באופן משמעותי את תוצאות הטיפול, ולכן "
                "מעקב קבוע אחר רמות ה-PSA הוא חלק חשוב מבריאות הגבר.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי PSA תקינים לפי גיל",
            body_html=(
                "<p>טווח <strong>ערך PSA תקין</strong> המקובל הוא <strong>0–4 ng/mL</strong>, אך סף זה משתנה עם "
                "הגיל. טווחי הייחוס לפי גיל מסוכמים בטבלה הבאה:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצת גיל</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">ערך PSA תקין</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">49–40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">59–50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">69–60</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">79–70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6.5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>רמות PSA מעל 4 ng/mL נחשבות <strong>PSA גבוה</strong> ועשויות לחייב בדיקות נוספות. עם זאת, "
                "בחלק מהגברים עם רמת PSA מתחת ל-4 ng/mL עדיין ניתן לאתר סרטן הערמונית, בעוד שגברים רבים עם ערך "
                "PSA גבוה אינם חולים בסרטן כלל. תוצאת בדיקת PSA בודדת אינה מאבחנת סרטן; יש לפרש אותה "
                "בהקשר הקליני.</p>"
                "<p>יחס PSA חופשי/PSA כולל הוא סמן שימושי נוסף. אחוז נמוך של PSA חופשי קשור לסיכון מוגבר "
                "לסרטן הערמונית. הרופא שלך עשוי לבקש בדיקת PSA חופשי כדי להבדיל בין סיבות שפירות לבין סיבות "
                "ממאירות לרמות PSA מוגברות.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות PSA גבוהות",
            body_html=(
                "<p>ערך <strong>PSA גבוה</strong> אינו מצביע בהכרח על סרטן הערמונית. מספר מצבים שפירים עלולים "
                "להעלות את רמות ה-PSA. הגורמים השכיחים ביותר כוללים:</p>"
                "<ul>"
                "<li><strong>הגדלה שפירה של הערמונית (BPH):</strong> הגדלה של הערמונית הקשורה לגיל היא אחד הגורמים "
                "השכיחים ביותר ל-PSA גבוה. BPH אינה סרטן אך עלולה לגרום לתסמינים במערכת השתן.</li>"
                "<li><strong>דלקת הערמונית (פרוסטטיטיס):</strong> דלקת חיידקית או כרונית של הערמונית עלולה להעלות "
                "באופן משמעותי את רמות ה-PSA.</li>"
                "<li><strong>זיהום בדרכי השתן:</strong> זיהומים בדרכי השתן התחתונות עלולים להעלות באופן זמני את "
                "רמות ה-PSA.</li>"
                "<li><strong>סרטן הערמונית:</strong> רמות PSA גבוהות בהתמדה או עולות במהירות הן אינדיקטור חשוב "
                "המחייב הערכה נוספת.</li>"
                "<li><strong>גורמים פיזיים:</strong> רכיבה על אופניים, פעילות מינית, בדיקה רקטלית דיגיטלית או ביופסיה "
                "של הערמונית עשויים להעלות באופן זמני את רמות ה-PSA.</li>"
                "<li><strong>תרופות:</strong> מעכבי 5-אלפא רדוקטאז (פינסטריד, דוטסטריד) מפחיתים את ה-PSA בכ-50%; "
                "יש לפרש את התוצאות בהתאם אצל מטופלים הנוטלים תרופות אלו.</li>"
                "</ul>"
                "<p>כדי לקבוע את הגורם ל-PSA גבוה, הרופא עשוי לבצע בדיקה רקטלית, לבקש בדיקת PSA חופשי, להפנות "
                "ל-MRI של הערמונית או להמליץ על ביופסיה בהתאם להתוויה הקלינית.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם תוצאת בדיקת PSA שלך מעל טווח הייחוס, אל תיבהל&mdash;אך פנה לאורולוג בהקדם. אין לדחות את "
                "ההערכה אם רמות ה-PSA מראות מגמת עלייה במדידות עוקבות, אם יש היסטוריה משפחתית של סרטן הערמונית, "
                "או אם אתה חווה תסמינים כמו קושי במתן שתן, הטלת שתן תכופה או דם בשתן.</p>"
                "<p>בדיקת PSA שנתית בשילוב בדיקה רקטלית דיגיטלית מומלצת לכל הגברים מעל גיל 50. גברים בסיכון גבוה "
                "יותר צריכים להתחיל סקירה בגיל 40&ndash;45. למרות שבדיקת PSA לבדה אינה כלי אבחוני, היא נותרה אחת "
                "מבדיקות הסקירה היקרות ביותר לגילוי מוקדם של סרטן הערמונית.</p>"
                "<p>זכרו: ערך PSA גבוה אינו מאשר אבחנה של סרטן. הרופא שלכם יבצע בדיקות נוספות כדי להבהיר את "
                "המצב וליצור תוכנית טיפול מתאימה. מעקב קבוע והתערבות מוקדמת משפרים משמעותית את התוצאות בטיפול "
                "בסרטן הערמונית.</p>"
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
            heading="PSA ब्लड टेस्ट: आपके रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>PSA टेस्ट</strong> (प्रोस्टेट स्पेसिफिक एंटीजन) रक्त में प्रोस्टेट ग्रंथि द्वारा उत्पादित "
                "एक प्रोटीन के स्तर को मापता है। PSA ब्लड टेस्ट प्रोस्टेट कैंसर स्क्रीनिंग में सबसे अधिक उपयोग किए "
                "जाने वाले परीक्षणों में से एक है, लेकिन हाई PSA का मतलब हमेशा कैंसर नहीं होता। सौम्य प्रोस्टेट "
                "वृद्धि (BPH), प्रोस्टेटाइटिस, मूत्र मार्ग संक्रमण और हाल की शारीरिक गतिविधि भी PSA के स्तर को "
                "अस्थायी रूप से बढ़ा सकती हैं।</p>"
                "<p>इस गाइड में हम उम्र के अनुसार PSA नॉर्मल रेंज, हाई PSA के सबसे सामान्य कारण और डॉक्टर से "
                "कब मिलना चाहिए, इन सबके बारे में बताएंगे। यहाँ दी गई जानकारी शैक्षिक उद्देश्य से है&mdash;सही "
                "निदान के लिए हमेशा यूरोलॉजिस्ट से परामर्श करें।</p>"
                "<p>50 वर्ष से अधिक उम्र के पुरुषों के लिए नियमित PSA टेस्ट की सिफारिश की जाती है। जिन पुरुषों के "
                "परिवार में प्रोस्टेट कैंसर का इतिहास है, वे 40&ndash;45 वर्ष की उम्र से ही स्क्रीनिंग शुरू कर सकते "
                "हैं। जल्दी पता लगने से उपचार के परिणाम काफी बेहतर होते हैं, इसलिए PSA के स्तर की नियमित निगरानी "
                "पुरुषों के स्वास्थ्य का एक महत्वपूर्ण हिस्सा है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="उम्र के अनुसार PSA नॉर्मल रेंज",
            body_html=(
                "<p>सामान्य रूप से स्वीकृत <strong>PSA नॉर्मल रेंज</strong> <strong>0–4 ng/mL</strong> है, लेकिन यह सीमा "
                "उम्र के साथ बदलती है। उम्र के अनुसार संदर्भ श्रेणियाँ नीचे दी गई तालिका में संक्षेपित हैं:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">आयु वर्ग</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PSA नॉर्मल रेंज</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">40–49 वर्ष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">50–59 वर्ष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">60–69 वर्ष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">70–79 वर्ष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6.5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>4 ng/mL से ऊपर PSA के स्तर को <strong>हाई PSA</strong> माना जाता है और इसके लिए आगे जाँच की "
                "आवश्यकता हो सकती है। हालांकि, कुछ पुरुषों में PSA 4 ng/mL से कम होने पर भी प्रोस्टेट कैंसर पाया "
                "जा सकता है, जबकि हाई PSA वाले कई पुरुषों में कैंसर नहीं होता। एक अकेला PSA टेस्ट कैंसर का "
                "निदान नहीं करता; इसे क्लिनिकल निष्कर्षों के साथ समझना चाहिए।</p>"
                "<p>फ्री PSA / टोटल PSA अनुपात भी एक उपयोगी मार्कर है। फ्री PSA का कम प्रतिशत प्रोस्टेट कैंसर "
                "के अधिक जोखिम से जुड़ा होता है। आपके डॉक्टर हाई PSA के सौम्य और घातक कारणों में अंतर करने के "
                "लिए फ्री PSA टेस्ट करवा सकते हैं।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई PSA के कारण",
            body_html=(
                "<p><strong>हाई PSA</strong> का मतलब हमेशा प्रोस्टेट कैंसर नहीं होता। कई सौम्य स्थितियाँ PSA के "
                "स्तर को बढ़ा सकती हैं। सबसे सामान्य कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>सौम्य प्रोस्टेट वृद्धि (BPH):</strong> उम्र से संबंधित प्रोस्टेट ग्रंथि का बढ़ना हाई "
                "PSA का सबसे आम कारणों में से एक है। BPH कैंसर नहीं है लेकिन मूत्र संबंधी लक्षण पैदा कर सकता है।</li>"
                "<li><strong>प्रोस्टेटाइटिस:</strong> प्रोस्टेट की बैक्टीरियल या क्रोनिक सूजन से PSA का स्तर काफी "
                "बढ़ सकता है।</li>"
                "<li><strong>मूत्र मार्ग संक्रमण (UTI):</strong> निचले मूत्र मार्ग के संक्रमण अस्थायी रूप से PSA "
                "के स्तर को बढ़ा सकते हैं।</li>"
                "<li><strong>प्रोस्टेट कैंसर:</strong> लगातार बढ़ा हुआ या तेज़ी से बढ़ता PSA एक महत्वपूर्ण संकेत है "
                "जिसके लिए आगे मूल्यांकन ज़रूरी है।</li>"
                "<li><strong>शारीरिक कारक:</strong> साइकिलिंग, यौन गतिविधि, डिजिटल रेक्टल परीक्षा या प्रोस्टेट "
                "बायोप्सी से PSA का स्तर अस्थायी रूप से बढ़ सकता है।</li>"
                "<li><strong>दवाइयाँ:</strong> 5-अल्फा रिडक्टेज़ इन्हिबिटर (फिनास्टराइड, डुटास्टराइड) PSA को "
                "लगभग 50% कम कर देते हैं; इन दवाओं का सेवन करने वाले रोगियों में परिणामों की व्याख्या तदनुसार "
                "की जानी चाहिए।</li>"
                "</ul>"
                "<p>हाई PSA का कारण निर्धारित करने के लिए डॉक्टर डिजिटल रेक्टल परीक्षा कर सकते हैं, फ्री PSA टेस्ट "
                "करा सकते हैं, प्रोस्टेट MRI करवा सकते हैं या ज़रूरत पड़ने पर बायोप्सी की सिफारिश कर सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपके PSA ब्लड टेस्ट का रिज़ल्ट संदर्भ सीमा से ऊपर है, तो घबराएँ नहीं&mdash;लेकिन जल्द से "
                "जल्द यूरोलॉजिस्ट से मिलें। अगर PSA के स्तर में लगातार बढ़ोतरी हो रही है, अगर परिवार में प्रोस्टेट "
                "कैंसर का इतिहास है, या अगर पेशाब करने में कठिनाई, बार-बार पेशाब आना या पेशाब में खून जैसे लक्षण "
                "हैं, तो मूल्यांकन में देरी नहीं करनी चाहिए।</p>"
                "<p>50 वर्ष से अधिक उम्र के सभी पुरुषों के लिए वार्षिक PSA टेस्ट और डिजिटल रेक्टल परीक्षा की "
                "सिफारिश की जाती है। अधिक जोखिम वाले पुरुषों को 40&ndash;45 वर्ष की उम्र से स्क्रीनिंग शुरू करनी "
                "चाहिए। हालांकि PSA टेस्ट अकेले एक डायग्नोस्टिक टूल नहीं है, यह प्रोस्टेट कैंसर के जल्दी पता "
                "लगाने के लिए सबसे मूल्यवान स्क्रीनिंग टेस्ट में से एक बना हुआ है।</p>"
                "<p>याद रखें: हाई PSA कैंसर की पुष्टि नहीं करता। आपके डॉक्टर स्थिति को स्पष्ट करने और उचित उपचार "
                "योजना बनाने के लिए अतिरिक्त परीक्षण करेंगे। नियमित निगरानी और शुरुआती हस्तक्षेप प्रोस्टेट कैंसर "
                "के उपचार में परिणामों को काफ़ी बेहतर बनाते हैं।</p>"
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
            heading="اختبار PSA في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>يقيس <strong>اختبار PSA</strong> (المستضد البروستاتي النوعي) مستوى بروتين تنتجه غدة البروستاتا "
                "في الدم. يُعد اختبار PSA أحد أكثر الأدوات استخداماً في فحص سرطان البروستاتا، إلا أن ارتفاع PSA "
                "لا يعني بالضرورة وجود سرطان. فتضخم البروستاتا الحميد (BPH) والتهاب البروستاتا وعدوى المسالك "
                "البولية وحتى النشاط البدني يمكن أن ترفع مستويات PSA بشكل مؤقت.</p>"
                "<p>في هذا الدليل نشرح مستوى PSA الطبيعي حسب العمر، والأسباب الأكثر شيوعاً لارتفاع PSA، ومتى يجب "
                "مراجعة الطبيب. المعلومات هنا تثقيفية&mdash;استشر دائماً طبيب مسالك بولية للحصول على تشخيص دقيق.</p>"
                "<p>يُوصى بإجراء اختبار PSA بشكل روتيني للرجال فوق سن الخمسين. الرجال الذين لديهم تاريخ عائلي من "
                "سرطان البروستاتا قد يبدأون الفحص في سن 40&ndash;45. يُحسّن الاكتشاف المبكر نتائج العلاج بشكل "
                "ملحوظ، مما يجعل المتابعة المنتظمة لمستويات PSA جزءاً مهماً من صحة الرجل.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="مستوى PSA الطبيعي حسب العمر",
            body_html=(
                "<p>يُعتبر <strong>مستوى PSA الطبيعي</strong> المقبول عموماً هو <strong>0–4 ng/mL</strong>، لكن هذا "
                "الحد يختلف باختلاف العمر. النطاقات المرجعية حسب الفئة العمرية ملخصة في الجدول التالي:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الفئة العمرية</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">مستوى PSA الطبيعي</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">49–40 سنة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–2.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">59–50 سنة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–3.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">69–60 سنة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–4.5 ng/mL</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">79–70 سنة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0–6.5 ng/mL</td></tr>'
                "</tbody></table>"
                "<p>تُعتبر مستويات PSA فوق 4 ng/mL <strong>ارتفاع PSA</strong> وقد تستدعي إجراء فحوصات إضافية. "
                "ومع ذلك، يمكن أن يُكتشف سرطان البروستاتا لدى بعض الرجال الذين تقل مستويات PSA لديهم عن 4 ng/mL، "
                "بينما كثير من الرجال ذوي القيم المرتفعة لا يعانون من السرطان. نتيجة اختبار PSA واحدة لا تُشخّص "
                "السرطان؛ يجب تفسيرها في السياق السريري.</p>"
                "<p>نسبة PSA الحر إلى PSA الكلي هي مؤشر مفيد آخر. ترتبط النسبة المنخفضة من PSA الحر بزيادة خطر "
                "سرطان البروستاتا. قد يطلب طبيبك اختبار PSA الحر للتمييز بين الأسباب الحميدة والخبيثة لارتفاع "
                "مستويات PSA.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع مستويات PSA",
            body_html=(
                "<p>لا يشير <strong>ارتفاع PSA</strong> بالضرورة إلى سرطان البروستاتا. يمكن أن ترتفع مستويات PSA "
                "بسبب عدة حالات حميدة. تشمل الأسباب الأكثر شيوعاً:</p>"
                "<ul>"
                "<li><strong>تضخم البروستاتا الحميد (BPH):</strong> تضخم البروستاتا المرتبط بالعمر هو أحد أكثر "
                "الأسباب شيوعاً لارتفاع PSA. تضخم البروستاتا الحميد ليس سرطاناً لكنه قد يسبب أعراضاً بولية.</li>"
                "<li><strong>التهاب البروستاتا:</strong> يمكن أن يرفع الالتهاب البكتيري أو المزمن للبروستاتا مستويات "
                "PSA بشكل ملحوظ.</li>"
                "<li><strong>عدوى المسالك البولية:</strong> يمكن أن ترفع عدوى المسالك البولية السفلية مستويات PSA "
                "بشكل مؤقت.</li>"
                "<li><strong>سرطان البروستاتا:</strong> مستويات PSA المرتفعة باستمرار أو المتصاعدة بسرعة مؤشر مهم "
                "يستدعي مزيداً من التقييم.</li>"
                "<li><strong>عوامل فيزيائية:</strong> ركوب الدراجات والنشاط الجنسي والفحص الشرجي الرقمي أو خزعة "
                "البروستاتا يمكن أن ترفع مستويات PSA مؤقتاً.</li>"
                "<li><strong>الأدوية:</strong> مثبطات إنزيم 5-ألفا ريدكتاز (فيناسترايد، دوتاسترايد) تخفض PSA بنحو "
                "50%؛ يجب تفسير النتائج وفقاً لذلك عند المرضى الذين يتناولون هذه الأدوية.</li>"
                "</ul>"
                "<p>لتحديد سبب ارتفاع PSA، قد يُجري الطبيب فحصاً شرجياً رقمياً، ويطلب اختبار PSA الحر، ويطلب "
                "تصويراً بالرنين المغناطيسي للبروستاتا، أو يوصي بأخذ خزعة إذا كان ذلك مبرراً سريرياً.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كانت نتيجة اختبار PSA لديك أعلى من النطاق المرجعي، فلا تقلق ولكن راجع طبيب مسالك بولية "
                "في أقرب وقت. لا ينبغي تأخير التقييم إذا كانت مستويات PSA تُظهر اتجاهاً تصاعدياً في القياسات "
                "المتتالية، أو إذا كان هناك تاريخ عائلي من سرطان البروستاتا، أو إذا كنت تعاني من أعراض مثل صعوبة "
                "التبول أو كثرة التبول أو وجود دم في البول.</p>"
                "<p>يُوصى بإجراء اختبار PSA سنوي مع فحص شرجي رقمي لجميع الرجال فوق سن الخمسين. يجب أن يبدأ "
                "الرجال الأكثر عرضة للخطر الفحص في سن 40&ndash;45. رغم أن اختبار PSA وحده ليس أداة تشخيصية، "
                "فإنه يظل أحد أهم اختبارات الفحص للكشف المبكر عن سرطان البروستاتا.</p>"
                "<p>تذكّر: ارتفاع PSA لا يؤكد تشخيص السرطان. سيُجري طبيبك فحوصات إضافية لتوضيح الوضع ووضع خطة "
                "علاج مناسبة. المتابعة المنتظمة والتدخل المبكر يُحسّنان بشكل كبير نتائج علاج سرطان البروستاتا.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_psa_sections_by_lang() -> dict:
    """Returns sections dict for PSA article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_psa_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for PSA article (all 9 languages)."""
    return {
        "tr": [
            {"question": "PSA testi nedir?",
             "answer": "PSA testi, kandaki prostat spesifik antijen düzeyini ölçen bir kan testidir. Prostat kanseri taramasında yaygın olarak kullanılır."},
            {"question": "PSA normal değeri kaçtır?",
             "answer": "Genel olarak 4 ng/mL altı normal kabul edilir; ancak yaşa göre değişir. 40–49 yaş için 0–2,5 ng/mL, 50–59 yaş için 0–3,5 ng/mL kabul edilen aralıklardır."},
            {"question": "PSA yüksekliği prostat kanseri mi demek?",
             "answer": "Hayır, PSA yüksekliği enfeksiyon, iyi huylu prostat büyümesi (BPH), prostatit veya kanser dahil birçok nedene bağlı olabilir. Kesin tanı için ek tetkikler gereklidir."},
        ],
        "en": [
            {"question": "What is a PSA test?",
             "answer": "A PSA test measures the level of prostate-specific antigen in the blood. It is widely used as a screening tool for prostate cancer."},
            {"question": "What is the normal PSA range?",
             "answer": "Generally, a PSA level below 4 ng/mL is considered normal, but age-specific ranges apply: 0–2.5 ng/mL for ages 40–49, 0–3.5 ng/mL for 50–59, 0–4.5 ng/mL for 60–69, and 0–6.5 ng/mL for 70–79."},
            {"question": "Does a high PSA mean prostate cancer?",
             "answer": "No. Elevated PSA can result from benign prostatic hyperplasia (BPH), prostatitis, urinary infections, or cancer. Additional tests are needed for a definitive diagnosis."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de PSA?",
             "answer": "La prueba de PSA mide el nivel de antígeno prostático específico en la sangre. Se utiliza ampliamente para el cribado del cáncer de próstata."},
            {"question": "¿Cuál es el rango normal de PSA?",
             "answer": "En general, un PSA inferior a 4 ng/mL se considera normal, aunque varía según la edad: 0–2,5 ng/mL para 40–49 años, 0–3,5 ng/mL para 50–59, 0–4,5 ng/mL para 60–69 y 0–6,5 ng/mL para 70–79."},
            {"question": "¿Un PSA alto significa cáncer de próstata?",
             "answer": "No. El PSA alto puede deberse a hiperplasia benigna de próstata (HBP), prostatitis, infecciones urinarias o cáncer. Se necesitan pruebas adicionales para un diagnóstico definitivo."},
        ],
        "de": [
            {"question": "Was ist der PSA-Test?",
             "answer": "Der PSA-Test misst den Spiegel des prostataspezifischen Antigens im Blut. Er wird häufig als Screening-Instrument für Prostatakrebs eingesetzt."},
            {"question": "Was sind die PSA-Normalwerte?",
             "answer": "Im Allgemeinen gilt ein PSA-Wert unter 4 ng/mL als normal, wobei altersspezifische Bereiche gelten: 0–2,5 ng/mL für 40–49 Jahre, 0–3,5 ng/mL für 50–59, 0–4,5 ng/mL für 60–69 und 0–6,5 ng/mL für 70–79."},
            {"question": "Bedeutet ein erhöhter PSA-Wert Prostatakrebs?",
             "answer": "Nein. Ein erhöhter PSA-Wert kann durch gutartige Prostatavergrößerung (BPH), Prostatitis, Harnwegsinfekte oder Krebs verursacht werden. Zusätzliche Untersuchungen sind für eine Diagnose erforderlich."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test PSA ?",
             "answer": "Le test PSA mesure le taux d'antigène prostatique spécifique dans le sang. Il est largement utilisé pour le dépistage du cancer de la prostate."},
            {"question": "Quelles sont les valeurs normales du PSA ?",
             "answer": "En règle générale, un taux de PSA inférieur à 4 ng/mL est considéré comme normal, avec des seuils adaptés à l'âge : 0–2,5 ng/mL pour 40–49 ans, 0–3,5 ng/mL pour 50–59, 0–4,5 ng/mL pour 60–69 et 0–6,5 ng/mL pour 70–79."},
            {"question": "Un PSA élevé signifie-t-il un cancer de la prostate ?",
             "answer": "Non. Un PSA élevé peut résulter d'une hypertrophie bénigne de la prostate (HBP), d'une prostatite, d'infections urinaires ou d'un cancer. Des examens complémentaires sont nécessaires pour un diagnostic définitif."},
        ],
        "it": [
            {"question": "Cos'è il test del PSA?",
             "answer": "Il test del PSA misura il livello dell'antigene prostatico specifico nel sangue. È ampiamente utilizzato come strumento di screening per il cancro alla prostata."},
            {"question": "Quali sono i valori normali del PSA?",
             "answer": "In generale, un PSA inferiore a 4 ng/mL è considerato normale, con intervalli specifici per età: 0–2,5 ng/mL per 40–49 anni, 0–3,5 ng/mL per 50–59, 0–4,5 ng/mL per 60–69 e 0–6,5 ng/mL per 70–79."},
            {"question": "Un PSA alto significa cancro alla prostata?",
             "answer": "No. Il PSA alto può essere causato da iperplasia prostatica benigna (IPB), prostatite, infezioni urinarie o cancro. Sono necessari ulteriori esami per una diagnosi definitiva."},
        ],
        "he": [
            {"question": "מהי בדיקת PSA?",
             "answer": "בדיקת PSA מודדת את רמת האנטיגן הספציפי לערמונית בדם. היא משמשת ככלי סקירה נפוץ לסרטן הערמונית."},
            {"question": "מהו ערך PSA תקין?",
             "answer": "באופן כללי, PSA מתחת ל-4 ng/mL נחשב תקין, אך הטווחים משתנים לפי גיל: 0–2.5 ng/mL לגילאי 40–49, 0–3.5 ng/mL לגילאי 50–59, 0–4.5 ng/mL לגילאי 60–69 ו-0–6.5 ng/mL לגילאי 70–79."},
            {"question": "האם PSA גבוה פירושו סרטן הערמונית?",
             "answer": "לא. PSA גבוה יכול לנבוע מהגדלה שפירה של הערמונית (BPH), דלקת הערמונית, זיהומים בדרכי השתן או סרטן. נדרשות בדיקות נוספות לאבחון מוחלט."},
        ],
        "hi": [
            {"question": "PSA टेस्ट क्या है?",
             "answer": "PSA टेस्ट रक्त में प्रोस्टेट स्पेसिफिक एंटीजन के स्तर को मापता है। इसका उपयोग प्रोस्टेट कैंसर की स्क्रीनिंग के लिए व्यापक रूप से किया जाता है।"},
            {"question": "PSA की नॉर्मल रेंज क्या है?",
             "answer": "सामान्यतः 4 ng/mL से कम PSA को सामान्य माना जाता है, लेकिन उम्र के अनुसार अलग-अलग रेंज लागू होती हैं: 40–49 वर्ष के लिए 0–2.5 ng/mL, 50–59 के लिए 0–3.5, 60–69 के लिए 0–4.5 और 70–79 के लिए 0–6.5 ng/mL।"},
            {"question": "क्या हाई PSA का मतलब प्रोस्टेट कैंसर है?",
             "answer": "नहीं। हाई PSA सौम्य प्रोस्टेट वृद्धि (BPH), प्रोस्टेटाइटिस, मूत्र मार्ग संक्रमण या कैंसर के कारण हो सकता है। निश्चित निदान के लिए अतिरिक्त परीक्षण आवश्यक हैं।"},
        ],
        "ar": [
            {"question": "ما هو اختبار PSA؟",
             "answer": "اختبار PSA يقيس مستوى المستضد البروستاتي النوعي في الدم. يُستخدم على نطاق واسع كأداة فحص لسرطان البروستاتا."},
            {"question": "ما هو مستوى PSA الطبيعي؟",
             "answer": "بشكل عام، يُعتبر PSA أقل من 4 ng/mL طبيعياً، مع نطاقات خاصة بالعمر: 0–2.5 ng/mL للأعمار 40–49، 0–3.5 للأعمار 50–59، 0–4.5 للأعمار 60–69، و0–6.5 ng/mL للأعمار 70–79."},
            {"question": "هل ارتفاع PSA يعني سرطان البروستاتا؟",
             "answer": "لا. يمكن أن ينتج ارتفاع PSA عن تضخم البروستاتا الحميد (BPH) أو التهاب البروستاتا أو عدوى المسالك البولية أو السرطان. تلزم فحوصات إضافية للتشخيص النهائي."},
        ],
    }
