# -*- coding: utf-8 -*-
"""
LDH (Lactate Dehydrogenase) blog article — full body content for all 9 languages.
Used by blog_i18n._article_ldh().
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
            heading="LDH kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>LDH testi</strong> (laktat dehidrojenaz), vücuttaki hemen hemen tüm dokularda bulunan "
                "bir enzimin kandaki düzeyini ölçer. <strong>Laktat dehidrojenaz</strong>, hücrelerin enerji üretim "
                "sürecinde (glikoliz) önemli bir rol oynayan intrasellüler bir enzimdir. Hücre hasarı veya yıkımı "
                "meydana geldiğinde LDH kana sızar ve <strong>LDH düzeyleri</strong> yükselir; bu nedenle LDH, "
                "genel bir doku hasar göstergesi olarak kullanılır.</p>"
                "<p><strong>LDH kan testi</strong>, spesifik bir hastalığı tanılamak yerine vücuttaki hücresel "
                "hasarın varlığını ve boyutunu değerlendirmek amacıyla istenir. Yüksek LDH düzeyleri lenfoma, "
                "lösemi gibi kanser türlerinden hemolitik anemiye, karaciğer hastalıklarından miyokard "
                "enfarktüsüne kadar geniş bir yelpazede görülebilir. Bu rehberde <strong>LDH normal değerleri</strong>, "
                "<strong>yüksek LDH</strong> nedenlerini ve ne zaman doktora başvurmanız gerektiğini bulacaksınız.</p>"
                "<p>LDH testi genellikle tam kan sayımı ve diğer biyokimya testleriyle birlikte istenir. "
                "Sonuçlar klinik bulgular ve ek laboratuvar verileriyle birlikte yorumlanmalıdır; tek başına "
                "LDH değeri kesin tanı koydurtmaz. Buradaki bilgiler eğitim amaçlıdır — tanı ve tedavi için "
                "mutlaka bir sağlık uzmanına danışın.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="LDH normal değerleri (referans aralıkları)",
            body_html=(
                "<p><strong>LDH normal aralığı</strong> laboratuvarlar arasında farklılık gösterebilir; "
                "ancak genel olarak kabul edilen yetişkin referans değerleri aşağıdaki tabloda özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">LDH normal aralığı</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yetişkinler</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yenidoğanlar</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Bebekler (1–12 ay)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Çocuklar (1–14 yaş)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>Referans aralığı test yöntemi ve laboratuvar cihazına göre değişebilir; bu nedenle kendi "
                "raporunuzdaki referans değerlerini esas almalısınız. <strong>LDH düzeyleri</strong> normalin "
                "üzerindeyse hekiminiz altta yatan nedeni araştırmak için ek testler (LDH izoenzim analizi, "
                "karaciğer fonksiyon testleri, periferik yayma vb.) isteyecektir.</p>"
                "<p>LDH beş farklı izoenzim formunda bulunur: LDH-1 ve LDH-2 ağırlıklı olarak kalpte ve "
                "eritrositlerde, LDH-3 akciğerlerde, LDH-4 ve LDH-5 ise karaciğer ve iskelet kasında "
                "yoğunlaşır. İzoenzim dağılımı, hasarın hangi organdan kaynaklandığını belirlemeye yardımcı olur.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="LDH yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Yüksek LDH</strong> düzeyleri geniş bir klinik tablo yelpazesinde karşımıza çıkabilir. "
                "<strong>Yüksek LDH</strong> değeri her zaman ciddi bir hastalık anlamına gelmez; ancak altta yatan "
                "nedenin araştırılması gerekir. LDH düzeylerini artırabilecek başlıca durumlar şunlardır:</p>"
                "<ul>"
                "<li><strong>Hemolitik anemi:</strong> Eritrositlerin normalden hızlı yıkılması, LDH (özellikle "
                "LDH-1 ve LDH-2) düzeylerinin belirgin şekilde yükselmesine neden olur.</li>"
                "<li><strong>Kanser (lenfoma, lösemi):</strong> Hızlı hücre döngüsü ve tümör lizisi sonucunda "
                "LDH düzeyleri artar. LDH, lenfomada prognoz ve tedavi yanıtını izlemek için önemli bir "
                "göstergedir.</li>"
                "<li><strong>Karaciğer hastalıkları:</strong> Hepatit, siroz ve karaciğer metastazları karaciğer "
                "hücre hasarına bağlı LDH (özellikle LDH-5) yüksekliğine yol açabilir.</li>"
                "<li><strong>Miyokard enfarktüsü (kalp krizi):</strong> Kalp kası hasarı, LDH-1 ve LDH-2 "
                "izoenzimlerinin yükselmesiyle sonuçlanır; ancak günümüzde troponin testleri daha spesifik "
                "kardiyak belirteçler olarak tercih edilmektedir.</li>"
                "<li><strong>Pulmoner emboli ve akciğer hasarı:</strong> Akciğer dokusu hasarı LDH-3 yüksekliğine "
                "neden olabilir.</li>"
                "<li><strong>Kas hasarı ve rabdomiyoliz:</strong> Yoğun egzersiz, travma veya iskelet kası "
                "hasarı LDH-4 ve LDH-5 düzeylerini yükseltebilir.</li>"
                "<li><strong>Enfeksiyon ve inflamasyon:</strong> Mononükleoz, menenjit gibi enfeksiyöz hastalıklar "
                "ve sistemik inflamasyon da LDH artışına yol açabilir.</li>"
                "</ul>"
                "<p>LDH izoenzim analizi, yüksekliğin hangi organ veya dokudan kaynaklandığını belirlemeye "
                "yardımcı olur. Doktorunuz klinik tabloya göre izoenzim dağılımı, görüntüleme ve ek kan "
                "testleri isteyebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p><strong>LDH kan testi</strong> sonucunuz referans aralığının üstünde çıktıysa panik yapmayın; "
                "ancak mutlaka bir hekime danışın. Özellikle açıklanamayan yorgunluk, gece terlemeleri, nedensiz "
                "kilo kaybı, sarılık veya koyu renkli idrar gibi belirtiler eşlik ediyorsa değerlendirme "
                "geciktirilmemelidir.</p>"
                "<p>LDH, tedavi izleme sürecinde de önemli bir belirteçtir. Lenfoma veya lösemi gibi kanser "
                "tedavisi sırasında LDH düzeylerindeki değişim, tedaviye yanıtı ve hastalığın seyrini "
                "takip etmek için kullanılır. Tedavi altındaki hastalar düzenli aralıklarla LDH kontrolü "
                "yaptırmalıdır.</p>"
                "<p>Unutmayın: <strong>yüksek LDH</strong> tek başına bir tanı değildir. Doktorunuz ek tetkiklerle "
                "altta yatan nedeni belirleyecek ve uygun tedavi planını oluşturacaktır. Erken teşhis ve düzenli "
                "takip, birçok hastalıkta tedavi başarısını önemli ölçüde artırır.</p>"
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
            heading="LDH blood test: what your results mean",
            body_html=(
                "<p>The <strong>LDH blood test</strong> measures the level of <strong>lactate dehydrogenase</strong>, "
                "an enzyme found in nearly every tissue in the body. LDH plays a key role in cellular energy "
                "production (glycolysis). When cells are damaged or destroyed, LDH leaks into the bloodstream "
                "and <strong>LDH levels</strong> rise — making it a general marker of tissue damage.</p>"
                "<p>An <strong>LDH test</strong> is not ordered to diagnose a specific disease but rather to "
                "assess the presence and extent of cellular injury. <strong>Elevated LDH</strong> can be seen "
                "in a wide range of conditions, from cancers such as lymphoma and leukaemia to haemolytic "
                "anaemia, liver disease and myocardial infarction. In this guide you will find the "
                "<strong>LDH normal range</strong>, common causes of <strong>high LDH</strong>, and when to "
                "consult a doctor.</p>"
                "<p>The LDH blood test is usually ordered alongside a complete blood count and other chemistry "
                "panels. Results must be interpreted together with clinical findings and additional laboratory "
                "data — a single LDH value is not diagnostic on its own. The information here is educational; "
                "always consult a healthcare professional for diagnosis and treatment.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="LDH normal range (reference intervals)",
            body_html=(
                "<p>The <strong>LDH normal range</strong> can vary between laboratories, but generally accepted "
                "adult reference values are summarised in the table below:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">LDH normal range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adults</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Newborns</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Infants (1–12 months)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Children (1–14 years)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>Reference intervals depend on the assay method and analyser used, so always compare your "
                "result with the range printed on your own report. If your <strong>LDH levels</strong> are "
                "above normal, your doctor may order additional tests — such as LDH isoenzyme analysis, liver "
                "function tests or a peripheral blood smear — to identify the underlying cause.</p>"
                "<p><strong>Lactate dehydrogenase</strong> exists in five isoenzyme forms: LDH-1 and LDH-2 are "
                "concentrated in the heart and red blood cells, LDH-3 in the lungs, and LDH-4 and LDH-5 in "
                "the liver and skeletal muscle. The isoenzyme pattern helps pinpoint which organ is affected.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high LDH levels",
            body_html=(
                "<p><strong>High LDH</strong> can occur in a wide variety of clinical settings. An "
                "<strong>elevated LDH</strong> result does not always mean a serious illness, but the "
                "underlying cause should be investigated. The most common causes of raised LDH include:</p>"
                "<ul>"
                "<li><strong>Haemolytic anaemia:</strong> Accelerated destruction of red blood cells causes a "
                "marked rise in LDH (particularly LDH-1 and LDH-2).</li>"
                "<li><strong>Cancer (lymphoma, leukaemia):</strong> Rapid cell turnover and tumour lysis "
                "increase LDH levels. LDH is an important prognostic marker in lymphoma and is used to "
                "monitor treatment response.</li>"
                "<li><strong>Liver disease:</strong> Hepatitis, cirrhosis and liver metastases can elevate "
                "LDH (especially LDH-5) due to hepatocyte damage.</li>"
                "<li><strong>Myocardial infarction (heart attack):</strong> Cardiac muscle damage raises "
                "LDH-1 and LDH-2; however, troponin tests are now preferred as more specific cardiac "
                "biomarkers.</li>"
                "<li><strong>Pulmonary embolism and lung injury:</strong> Lung tissue damage can elevate "
                "LDH-3.</li>"
                "<li><strong>Muscle injury and rhabdomyolysis:</strong> Intense exercise, trauma or "
                "skeletal muscle damage can raise LDH-4 and LDH-5.</li>"
                "<li><strong>Infection and inflammation:</strong> Infectious diseases such as mononucleosis "
                "and meningitis, as well as systemic inflammation, can cause LDH to rise.</li>"
                "</ul>"
                "<p>An LDH isoenzyme analysis can help determine which organ or tissue is the source of "
                "the elevation. Your doctor may also order imaging studies and additional blood tests based "
                "on the clinical picture.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your <strong>LDH blood test</strong> result is above the reference range, do not "
                "panic — but do consult a doctor. Evaluation should not be delayed if you experience "
                "unexplained fatigue, night sweats, unintentional weight loss, jaundice or dark urine.</p>"
                "<p>LDH is also an important marker during treatment monitoring. In cancers such as lymphoma "
                "or leukaemia, changes in <strong>LDH levels</strong> are used to track treatment response "
                "and disease progression. Patients undergoing treatment should have their LDH checked at "
                "regular intervals.</p>"
                "<p>Remember: <strong>high LDH</strong> is not a diagnosis in itself. Your doctor will use "
                "further tests to identify the underlying cause and formulate an appropriate treatment plan. "
                "Early detection and regular follow-up significantly improve outcomes in many conditions.</p>"
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
            heading="Prueba de LDH en sangre: qué significan sus resultados",
            body_html=(
                "<p>La <strong>prueba de LDH</strong> mide el nivel de <strong>lactato deshidrogenasa</strong>, "
                "una enzima presente en prácticamente todos los tejidos del cuerpo. La LDH desempeña un papel "
                "clave en la producción de energía celular (glucólisis). Cuando las células se dañan o "
                "destruyen, la LDH se libera al torrente sanguíneo y los <strong>niveles de LDH</strong> "
                "aumentan, lo que la convierte en un marcador general de daño tisular.</p>"
                "<p>La <strong>prueba de LDH en sangre</strong> no se solicita para diagnosticar una enfermedad "
                "específica, sino para evaluar la presencia y el alcance de la lesión celular. La "
                "<strong>LDH elevada</strong> puede observarse en un amplio abanico de afecciones: desde "
                "cánceres como el linfoma y la leucemia hasta la anemia hemolítica, las enfermedades hepáticas "
                "y el infarto de miocardio. En esta guía encontrará el <strong>rango normal de LDH</strong>, "
                "las causas de <strong>LDH alta</strong> y cuándo consultar al médico.</p>"
                "<p>La prueba de LDH suele solicitarse junto con un hemograma completo y otros paneles "
                "bioquímicos. Los resultados deben interpretarse junto con los hallazgos clínicos y datos "
                "de laboratorio adicionales; un valor aislado de LDH no es diagnóstico. Esta información "
                "es educativa — consulte siempre a un profesional de la salud.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rango normal de LDH (intervalos de referencia)",
            body_html=(
                "<p>El <strong>rango normal de LDH</strong> puede variar entre laboratorios, pero los valores "
                "de referencia generalmente aceptados para adultos se resumen en la siguiente tabla:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal de LDH</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adultos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Recién nacidos</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Lactantes (1–12 meses)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Niños (1–14 años)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>Los intervalos de referencia dependen del método analítico y del equipo utilizado, por "
                "lo que debe comparar siempre su resultado con el rango indicado en su propio informe. Si "
                "sus <strong>niveles de LDH</strong> están por encima de lo normal, su médico podrá solicitar "
                "pruebas adicionales — como un análisis de isoenzimas de LDH, pruebas hepáticas o un frotis "
                "de sangre periférica — para identificar la causa.</p>"
                "<p>La <strong>lactato deshidrogenasa</strong> existe en cinco isoenzimas: LDH-1 y LDH-2 se "
                "concentran en el corazón y los glóbulos rojos, LDH-3 en los pulmones, y LDH-4 y LDH-5 en "
                "el hígado y el músculo esquelético. El patrón de isoenzimas ayuda a determinar qué órgano "
                "está afectado.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de LDH alta",
            body_html=(
                "<p>Una <strong>LDH alta</strong> puede aparecer en una amplia variedad de situaciones "
                "clínicas. Una <strong>LDH elevada</strong> no siempre indica una enfermedad grave, pero "
                "la causa subyacente debe investigarse. Las causas más frecuentes incluyen:</p>"
                "<ul>"
                "<li><strong>Anemia hemolítica:</strong> La destrucción acelerada de glóbulos rojos provoca "
                "un aumento notable de LDH (sobre todo LDH-1 y LDH-2).</li>"
                "<li><strong>Cáncer (linfoma, leucemia):</strong> El recambio celular rápido y la lisis "
                "tumoral elevan los niveles de LDH. La LDH es un marcador pronóstico importante en el "
                "linfoma.</li>"
                "<li><strong>Enfermedades hepáticas:</strong> Hepatitis, cirrosis y metástasis hepáticas "
                "pueden elevar la LDH (especialmente LDH-5) por daño hepatocelular.</li>"
                "<li><strong>Infarto de miocardio:</strong> El daño del músculo cardíaco eleva LDH-1 y "
                "LDH-2; sin embargo, actualmente se prefieren las troponinas como biomarcadores cardíacos "
                "más específicos.</li>"
                "<li><strong>Embolia pulmonar y lesión pulmonar:</strong> El daño del tejido pulmonar puede "
                "elevar la LDH-3.</li>"
                "<li><strong>Lesión muscular y rabdomiólisis:</strong> Ejercicio intenso, traumatismos o "
                "daño del músculo esquelético pueden elevar LDH-4 y LDH-5.</li>"
                "<li><strong>Infección e inflamación:</strong> Enfermedades infecciosas como la mononucleosis "
                "y la meningitis, así como la inflamación sistémica, pueden elevar la LDH.</li>"
                "</ul>"
                "<p>Un análisis de isoenzimas de LDH puede ayudar a determinar de qué órgano o tejido "
                "procede la elevación. Su médico podrá solicitar estudios de imagen y análisis adicionales "
                "según el cuadro clínico.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si su <strong>prueba de LDH en sangre</strong> arroja un resultado por encima del "
                "rango de referencia, no se alarme, pero consulte a un médico. La evaluación no debe "
                "retrasarse si presenta fatiga inexplicable, sudoración nocturna, pérdida de peso "
                "involuntaria, ictericia u orina oscura.</p>"
                "<p>La LDH es también un marcador importante en el seguimiento del tratamiento. En cánceres "
                "como el linfoma o la leucemia, los cambios en los <strong>niveles de LDH</strong> se "
                "utilizan para evaluar la respuesta al tratamiento y la progresión de la enfermedad. "
                "Los pacientes en tratamiento deben controlar sus niveles de LDH con regularidad.</p>"
                "<p>Recuerde: una <strong>LDH alta</strong> no es un diagnóstico en sí misma. Su médico "
                "realizará pruebas adicionales para identificar la causa subyacente y establecer un plan "
                "de tratamiento adecuado. La detección temprana y el seguimiento regular mejoran "
                "significativamente los resultados en muchas enfermedades.</p>"
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
            heading="LDH-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>LDH-Test</strong> misst den Spiegel der <strong>Laktatdehydrogenase</strong>, "
                "eines Enzyms, das in nahezu jedem Gewebe des Körpers vorkommt. LDH spielt eine zentrale Rolle "
                "bei der zellulären Energiegewinnung (Glykolyse). Werden Zellen geschädigt oder zerstört, "
                "gelangt LDH ins Blut und die <strong>LDH-Werte</strong> steigen — daher dient LDH als "
                "allgemeiner Marker für Gewebeschäden.</p>"
                "<p>Ein <strong>LDH-Bluttest</strong> wird nicht zur Diagnose einer bestimmten Erkrankung "
                "eingesetzt, sondern um das Vorhandensein und Ausmaß zellulärer Schäden zu beurteilen. "
                "<strong>Erhöhte LDH-Werte</strong> können bei zahlreichen Erkrankungen auftreten — von "
                "Krebsarten wie Lymphom und Leukämie über hämolytische Anämie bis hin zu Lebererkrankungen "
                "und Myokardinfarkt. In diesem Ratgeber finden Sie den <strong>LDH-Normalbereich</strong>, "
                "Ursachen für eine <strong>hohe LDH</strong> und wann Sie einen Arzt aufsuchen sollten.</p>"
                "<p>Der LDH-Test wird in der Regel zusammen mit einem Blutbild und anderen klinisch-chemischen "
                "Untersuchungen angefordert. Die Ergebnisse müssen im Zusammenhang mit klinischen Befunden "
                "und zusätzlichen Labordaten interpretiert werden — ein einzelner LDH-Wert ist für sich "
                "genommen nicht diagnostisch. Die Informationen hier dienen der Aufklärung; für Diagnose "
                "und Therapie wenden Sie sich bitte an einen Arzt.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="LDH-Normalwerte (Referenzbereiche)",
            body_html=(
                "<p>Der <strong>LDH-Normalbereich</strong> kann zwischen Laboren variieren; allgemein "
                "akzeptierte Referenzwerte für Erwachsene sind in der folgenden Tabelle zusammengefasst:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">LDH-Normalbereich</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erwachsene</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neugeborene</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Säuglinge (1–12 Monate)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kinder (1–14 Jahre)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>Referenzbereiche hängen von der Analysemethode und dem verwendeten Gerät ab; vergleichen "
                "Sie Ihr Ergebnis daher immer mit dem Bereich auf Ihrem eigenen Befund. Liegen Ihre "
                "<strong>LDH-Werte</strong> über dem Normalbereich, wird Ihr Arzt zusätzliche Untersuchungen "
                "anordnen — etwa eine LDH-Isoenzym-Analyse, Leberfunktionstests oder einen peripheren "
                "Blutausstrich — um die Ursache zu ermitteln.</p>"
                "<p>Die <strong>Laktatdehydrogenase</strong> existiert in fünf Isoenzymformen: LDH-1 und "
                "LDH-2 sind im Herz und in den roten Blutkörperchen konzentriert, LDH-3 in der Lunge und "
                "LDH-4 sowie LDH-5 in Leber und Skelettmuskulatur. Das Isoenzymmuster hilft festzustellen, "
                "welches Organ betroffen ist.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für einen erhöhten LDH-Wert",
            body_html=(
                "<p>Eine <strong>hohe LDH</strong> kann in vielen verschiedenen klinischen Situationen "
                "auftreten. Ein <strong>erhöhter LDH-Wert</strong> bedeutet nicht immer eine schwere "
                "Erkrankung, die zugrunde liegende Ursache sollte jedoch abgeklärt werden. Die häufigsten "
                "Ursachen sind:</p>"
                "<ul>"
                "<li><strong>Hämolytische Anämie:</strong> Die beschleunigte Zerstörung roter Blutkörperchen "
                "führt zu einem deutlichen Anstieg der LDH (insbesondere LDH-1 und LDH-2).</li>"
                "<li><strong>Krebs (Lymphom, Leukämie):</strong> Schneller Zellumsatz und Tumorlyse erhöhen "
                "die LDH-Werte. LDH ist ein wichtiger Prognosemarker beim Lymphom.</li>"
                "<li><strong>Lebererkrankungen:</strong> Hepatitis, Zirrhose und Lebermetastasen können die "
                "LDH (vor allem LDH-5) durch Hepatozytenschäden erhöhen.</li>"
                "<li><strong>Myokardinfarkt (Herzinfarkt):</strong> Die Schädigung des Herzmuskels erhöht "
                "LDH-1 und LDH-2; heutzutage werden jedoch Troponintests als spezifischere kardiale "
                "Biomarker bevorzugt.</li>"
                "<li><strong>Lungenembolie und Lungenschädigung:</strong> Eine Schädigung des Lungengewebes "
                "kann LDH-3 erhöhen.</li>"
                "<li><strong>Muskelverletzung und Rhabdomyolyse:</strong> Intensives Training, Trauma oder "
                "Skelettmuskelschäden können LDH-4 und LDH-5 ansteigen lassen.</li>"
                "<li><strong>Infektion und Entzündung:</strong> Infektionskrankheiten wie Mononukleose und "
                "Meningitis sowie systemische Entzündungen können die LDH ebenfalls erhöhen.</li>"
                "</ul>"
                "<p>Eine LDH-Isoenzym-Analyse kann helfen festzustellen, von welchem Organ oder Gewebe die "
                "Erhöhung ausgeht. Ihr Arzt kann je nach klinischem Bild bildgebende Verfahren und weitere "
                "Blutuntersuchungen anordnen.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Liegt Ihr <strong>LDH-Bluttest</strong>-Ergebnis über dem Referenzbereich, bewahren Sie "
                "Ruhe, suchen Sie aber einen Arzt auf. Eine Abklärung sollte nicht verzögert werden, wenn "
                "Sie unter unerklärlicher Müdigkeit, Nachtschweiß, ungewolltem Gewichtsverlust, Gelbsucht "
                "oder dunklem Urin leiden.</p>"
                "<p>LDH ist auch ein wichtiger Marker bei der Therapieüberwachung. Bei Krebserkrankungen wie "
                "Lymphom oder Leukämie werden Veränderungen der <strong>LDH-Werte</strong> genutzt, um das "
                "Therapieansprechen und den Krankheitsverlauf zu verfolgen. Patienten unter Behandlung "
                "sollten ihre LDH regelmäßig kontrollieren lassen.</p>"
                "<p>Denken Sie daran: Ein <strong>erhöhter LDH-Wert</strong> ist allein keine Diagnose. Ihr "
                "Arzt wird zusätzliche Untersuchungen durchführen, um die Ursache zu ermitteln und einen "
                "geeigneten Behandlungsplan zu erstellen. Früherkennung und regelmäßige Kontrollen verbessern "
                "die Prognose bei vielen Erkrankungen erheblich.</p>"
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
            heading="Test LDH : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test LDH</strong> mesure le taux de <strong>lactate déshydrogénase</strong>, "
                "une enzyme présente dans la quasi-totalité des tissus de l'organisme. La LDH joue un rôle "
                "clé dans la production d'énergie cellulaire (glycolyse). Lorsque des cellules sont "
                "endommagées ou détruites, la LDH passe dans la circulation sanguine et les "
                "<strong>taux de LDH</strong> augmentent, ce qui en fait un marqueur général de "
                "lésion tissulaire.</p>"
                "<p>Le <strong>test LDH</strong> n'est pas prescrit pour diagnostiquer une maladie précise "
                "mais plutôt pour évaluer la présence et l'étendue d'une atteinte cellulaire. Une "
                "<strong>LDH élevée</strong> peut s'observer dans de nombreuses affections, des cancers "
                "comme le lymphome et la leucémie à l'anémie hémolytique, aux maladies hépatiques et à "
                "l'infarctus du myocarde. Dans ce guide vous trouverez les <strong>valeurs normales de "
                "LDH</strong>, les causes d'une <strong>LDH élevée</strong> et quand consulter un médecin.</p>"
                "<p>Le test LDH est généralement prescrit conjointement avec un hémogramme et d'autres "
                "bilans biochimiques. Les résultats doivent être interprétés en tenant compte des "
                "données cliniques et de laboratoire complémentaires ; une valeur isolée de LDH n'est "
                "pas diagnostique. Ces informations sont à visée éducative — consultez toujours un "
                "professionnel de santé.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de LDH (intervalles de référence)",
            body_html=(
                "<p>Les <strong>valeurs normales de LDH</strong> peuvent varier d'un laboratoire à l'autre ; "
                "les valeurs de référence généralement admises pour les adultes sont résumées dans le "
                "tableau ci-dessous :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valeurs normales de LDH</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adultes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Nouveau-nés</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Nourrissons (1–12 mois)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Enfants (1–14 ans)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>Les intervalles de référence dépendent de la méthode d'analyse et de l'appareil utilisé ; "
                "comparez donc toujours votre résultat avec la plage indiquée sur votre propre rapport. "
                "Si vos <strong>taux de LDH</strong> sont supérieurs à la normale, votre médecin pourra "
                "demander des examens complémentaires — analyse des isoenzymes de LDH, bilan hépatique ou "
                "frottis sanguin — pour identifier la cause.</p>"
                "<p>La <strong>lactate déshydrogénase</strong> existe sous cinq formes d'isoenzymes : LDH-1 "
                "et LDH-2 sont concentrées dans le cœur et les globules rouges, LDH-3 dans les poumons, "
                "et LDH-4 et LDH-5 dans le foie et les muscles squelettiques. Le profil des isoenzymes "
                "permet d'identifier l'organe touché.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une LDH élevée",
            body_html=(
                "<p>Une <strong>LDH élevée</strong> peut survenir dans de nombreux contextes cliniques. "
                "Un résultat de <strong>LDH élevée</strong> ne signifie pas toujours une maladie grave, "
                "mais la cause sous-jacente doit être explorée. Les causes les plus fréquentes sont :</p>"
                "<ul>"
                "<li><strong>Anémie hémolytique :</strong> La destruction accélérée des globules rouges "
                "entraîne une élévation marquée de la LDH (surtout LDH-1 et LDH-2).</li>"
                "<li><strong>Cancer (lymphome, leucémie) :</strong> Le renouvellement cellulaire rapide et "
                "la lyse tumorale augmentent les taux de LDH. La LDH est un marqueur pronostique important "
                "dans le lymphome.</li>"
                "<li><strong>Maladies hépatiques :</strong> Hépatite, cirrhose et métastases hépatiques "
                "peuvent élever la LDH (notamment LDH-5) par lésion hépatocytaire.</li>"
                "<li><strong>Infarctus du myocarde :</strong> L'atteinte du muscle cardiaque élève LDH-1 et "
                "LDH-2 ; toutefois, les troponines sont aujourd'hui préférées comme biomarqueurs cardiaques "
                "plus spécifiques.</li>"
                "<li><strong>Embolie pulmonaire et lésion pulmonaire :</strong> L'atteinte du tissu "
                "pulmonaire peut élever la LDH-3.</li>"
                "<li><strong>Lésion musculaire et rhabdomyolyse :</strong> Un exercice intense, un "
                "traumatisme ou une atteinte du muscle squelettique peuvent augmenter LDH-4 et LDH-5.</li>"
                "<li><strong>Infection et inflammation :</strong> Des maladies infectieuses telles que la "
                "mononucléose et la méningite, ainsi que l'inflammation systémique, peuvent faire monter "
                "la LDH.</li>"
                "</ul>"
                "<p>Une analyse des isoenzymes de LDH peut aider à déterminer quel organe ou tissu est à "
                "l'origine de l'élévation. Votre médecin pourra également prescrire des examens d'imagerie "
                "et des analyses sanguines supplémentaires selon le tableau clinique.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si le résultat de votre <strong>test LDH</strong> dépasse l'intervalle de référence, "
                "ne paniquez pas, mais consultez un médecin. L'évaluation ne doit pas être retardée si vous "
                "présentez une fatigue inexpliquée, des sueurs nocturnes, une perte de poids involontaire, "
                "un ictère ou des urines foncées.</p>"
                "<p>La LDH est également un marqueur important dans le suivi thérapeutique. Dans les cancers "
                "tels que le lymphome ou la leucémie, les variations des <strong>taux de LDH</strong> servent "
                "à évaluer la réponse au traitement et la progression de la maladie. Les patients sous "
                "traitement doivent faire contrôler régulièrement leur LDH.</p>"
                "<p>N'oubliez pas : une <strong>LDH élevée</strong> n'est pas un diagnostic en soi. Votre "
                "médecin effectuera des examens complémentaires pour identifier la cause sous-jacente et "
                "établir un plan de traitement adapté. Le dépistage précoce et un suivi régulier améliorent "
                "significativement le pronostic dans de nombreuses pathologies.</p>"
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
            heading="Test LDH: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test LDH</strong> misura il livello di <strong>lattato deidrogenasi</strong>, "
                "un enzima presente in quasi tutti i tessuti dell'organismo. La LDH svolge un ruolo chiave "
                "nella produzione di energia cellulare (glicolisi). Quando le cellule vengono danneggiate o "
                "distrutte, la LDH passa nel sangue e i <strong>livelli di LDH</strong> aumentano, rendendola "
                "un marcatore generale di danno tissutale.</p>"
                "<p>Il <strong>test LDH nel sangue</strong> non viene richiesto per diagnosticare una malattia "
                "specifica, ma per valutare la presenza e l'entità del danno cellulare. Una <strong>LDH "
                "elevata</strong> può essere riscontrata in una vasta gamma di condizioni: da tumori come il "
                "linfoma e la leucemia all'anemia emolitica, dalle malattie epatiche all'infarto del miocardio. "
                "In questa guida troverai l'<strong>intervallo normale della LDH</strong>, le cause della "
                "<strong>LDH alta</strong> e quando rivolgersi al medico.</p>"
                "<p>Il test LDH viene solitamente richiesto insieme a un emocromo completo e ad altri esami "
                "di chimica clinica. I risultati devono essere interpretati nel contesto clinico e insieme "
                "ad altri dati di laboratorio; un singolo valore di LDH non è diagnostico. Le informazioni "
                "qui riportate hanno scopo educativo — consultate sempre un professionista sanitario.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali della LDH (intervalli di riferimento)",
            body_html=(
                "<p>L'<strong>intervallo normale della LDH</strong> può variare tra i laboratori; i valori "
                "di riferimento generalmente accettati per gli adulti sono riassunti nella tabella seguente:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale LDH</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adulti</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Neonati</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Lattanti (1–12 mesi)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Bambini (1–14 anni)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>Gli intervalli di riferimento dipendono dal metodo analitico e dallo strumento utilizzato; "
                "confrontate sempre il vostro risultato con l'intervallo indicato nel vostro referto. Se i "
                "vostri <strong>livelli di LDH</strong> sono superiori alla norma, il medico potrà richiedere "
                "esami aggiuntivi — come l'analisi degli isoenzimi della LDH, i test di funzionalità epatica "
                "o uno striscio di sangue periferico — per individuare la causa.</p>"
                "<p>La <strong>lattato deidrogenasi</strong> esiste in cinque forme isoenzimatiche: LDH-1 e "
                "LDH-2 sono concentrate nel cuore e nei globuli rossi, LDH-3 nei polmoni, LDH-4 e LDH-5 "
                "nel fegato e nel muscolo scheletrico. Il profilo isoenzimatico aiuta a identificare quale "
                "organo è interessato.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di LDH alta",
            body_html=(
                "<p>Una <strong>LDH alta</strong> può presentarsi in un'ampia varietà di contesti clinici. "
                "Un valore di <strong>LDH elevata</strong> non indica necessariamente una malattia grave, "
                "ma la causa sottostante deve essere indagata. Le cause più comuni includono:</p>"
                "<ul>"
                "<li><strong>Anemia emolitica:</strong> La distruzione accelerata dei globuli rossi provoca "
                "un aumento marcato della LDH (in particolare LDH-1 e LDH-2).</li>"
                "<li><strong>Cancro (linfoma, leucemia):</strong> Il rapido ricambio cellulare e la lisi "
                "tumorale innalzano i livelli di LDH. La LDH è un importante marcatore prognostico nel "
                "linfoma.</li>"
                "<li><strong>Malattie epatiche:</strong> Epatite, cirrosi e metastasi epatiche possono "
                "elevare la LDH (soprattutto LDH-5) a causa del danno epatocitario.</li>"
                "<li><strong>Infarto del miocardio:</strong> Il danno al muscolo cardiaco eleva LDH-1 e "
                "LDH-2; tuttavia, i test della troponina sono oggi preferiti come biomarcatori cardiaci "
                "più specifici.</li>"
                "<li><strong>Embolia polmonare e danno polmonare:</strong> Il danno al tessuto polmonare "
                "può elevare la LDH-3.</li>"
                "<li><strong>Lesione muscolare e rabdomiolisi:</strong> Esercizio intenso, traumi o danni "
                "al muscolo scheletrico possono aumentare LDH-4 e LDH-5.</li>"
                "<li><strong>Infezione e infiammazione:</strong> Malattie infettive come la mononucleosi e "
                "la meningite, nonché l'infiammazione sistemica, possono causare un aumento della LDH.</li>"
                "</ul>"
                "<p>L'analisi degli isoenzimi della LDH può aiutare a determinare da quale organo o tessuto "
                "proviene l'elevazione. Il medico potrà inoltre prescrivere esami di imaging e analisi del "
                "sangue aggiuntive in base al quadro clinico.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se il risultato del vostro <strong>test LDH nel sangue</strong> supera l'intervallo di "
                "riferimento, non allarmatevi, ma consultate un medico. La valutazione non deve essere "
                "ritardata se accusate stanchezza inspiegabile, sudorazione notturna, perdita di peso "
                "involontaria, ittero o urine scure.</p>"
                "<p>La LDH è anche un marcatore importante nel monitoraggio terapeutico. Nei tumori come "
                "il linfoma o la leucemia, le variazioni dei <strong>livelli di LDH</strong> vengono "
                "utilizzate per valutare la risposta al trattamento e la progressione della malattia. "
                "I pazienti in terapia dovrebbero controllare regolarmente i livelli di LDH.</p>"
                "<p>Ricordate: una <strong>LDH alta</strong> non è di per sé una diagnosi. Il vostro medico "
                "effettuerà ulteriori esami per individuare la causa sottostante e definire un piano "
                "terapeutico adeguato. La diagnosi precoce e il follow-up regolare migliorano "
                "significativamente gli esiti in molte patologie.</p>"
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
            heading="בדיקת LDH בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>בדיקת <strong>LDH</strong> מודדת את רמת האנזים <strong>לקטט דהידרוגנאז</strong> "
                "בדם — אנזים הנמצא כמעט בכל רקמה בגוף. LDH ממלא תפקיד מרכזי בייצור אנרגיה "
                "תאית (גליקוליזה). כאשר תאים ניזוקים או נהרסים, LDH דולף לזרם הדם ו<strong>רמות "
                "LDH</strong> עולות — מה שהופך אותו לסמן כללי של נזק רקמתי.</p>"
                "<p><strong>בדיקת LDH בדם</strong> אינה מיועדת לאבחון מחלה ספציפית אלא להערכת "
                "נוכחות והיקף הנזק התאי. <strong>LDH מוגבר</strong> יכול להופיע במגוון רחב של "
                "מצבים — מסרטנים כמו לימפומה ולוקמיה ועד אנמיה המוליטית, מחלות כבד ואוטם "
                "שריר הלב. במדריך זה תמצאו את <strong>טווח הנורמה של LDH</strong>, גורמים "
                "ל<strong>LDH גבוה</strong> ומתי יש לפנות לרופא.</p>"
                "<p>בדיקת LDH מוזמנת בדרך כלל יחד עם ספירת דם מלאה ובדיקות ביוכימיות נוספות. "
                "יש לפרש את התוצאות בשילוב עם ממצאים קליניים ונתוני מעבדה נוספים; ערך LDH "
                "בודד אינו מאבחן בפני עצמו. המידע כאן הוא לצורכי הסברה בלבד — התייעצו תמיד "
                "עם רופא.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי LDH תקינים (טווחי ייחוס)",
            body_html=(
                "<p><strong>טווח הנורמה של LDH</strong> עשוי להשתנות בין מעבדות; ערכי הייחוס "
                "המקובלים לכלל מסוכמים בטבלה הבאה:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח LDH תקין</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">מבוגרים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">יילודים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">תינוקות (12–1 חודשים)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ילדים (14–1 שנים)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>טווחי הייחוס תלויים בשיטת הבדיקה ובמכשיר; לכן השוו תמיד את התוצאה שלכם "
                "לטווח המופיע בדוח שלכם. אם <strong>רמות ה-LDH</strong> שלכם מעל הנורמה, "
                "הרופא עשוי להזמין בדיקות נוספות — כגון ניתוח איזואנזימים של LDH, בדיקות "
                "תפקודי כבד או משטח דם היקפי — לזיהוי הסיבה.</p>"
                "<p><strong>לקטט דהידרוגנאז</strong> קיים בחמש צורות איזואנזימטיות: LDH-1 "
                "ו-LDH-2 מרוכזים בלב ובכדוריות הדם האדומות, LDH-3 בריאות, ו-LDH-4 ו-LDH-5 "
                "בכבד ובשריר השלד. פרופיל האיזואנזימים מסייע לקבוע איזה איבר מעורב.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות LDH גבוהות",
            body_html=(
                "<p><strong>LDH גבוה</strong> יכול להופיע במגוון רחב של מצבים קליניים. "
                "ערך <strong>LDH מוגבר</strong> אינו מעיד בהכרח על מחלה חמורה, אך יש "
                "לברר את הסיבה הבסיסית. הגורמים השכיחים ביותר כוללים:</p>"
                "<ul>"
                "<li><strong>אנמיה המוליטית:</strong> הרס מואץ של כדוריות דם אדומות גורם "
                "לעלייה ניכרת ב-LDH (בעיקר LDH-1 ו-LDH-2).</li>"
                "<li><strong>סרטן (לימפומה, לוקמיה):</strong> מחזור תאים מהיר וליזיס "
                "גידולי מעלים את רמות ה-LDH. LDH הוא סמן פרוגנוסטי חשוב בלימפומה.</li>"
                "<li><strong>מחלות כבד:</strong> דלקת כבד, שחמת וגרורות בכבד עלולות להעלות "
                "את ה-LDH (בעיקר LDH-5) עקב נזק להפטוציטים.</li>"
                "<li><strong>אוטם שריר הלב (התקף לב):</strong> נזק לשריר הלב מעלה LDH-1 "
                "ו-LDH-2; עם זאת, בדיקות טרופונין מועדפות כיום כסמנים לבביים ספציפיים יותר.</li>"
                "<li><strong>תסחיף ריאתי ופגיעה ריאתית:</strong> נזק לרקמת הריאה עלול "
                "להעלות את LDH-3.</li>"
                "<li><strong>פגיעה בשרירים ורבדומיוליזיס:</strong> אימון אינטנסיבי, טראומה "
                "או נזק לשריר השלד עלולים להעלות LDH-4 ו-LDH-5.</li>"
                "<li><strong>זיהום ודלקת:</strong> מחלות זיהומיות כמו מונונוקלאוזיס ודלקת "
                "קרום המוח, וכן דלקת מערכתית, עלולים לגרום לעליית LDH.</li>"
                "</ul>"
                "<p>ניתוח איזואנזימים של LDH יכול לעזור לקבוע מאיזה איבר או רקמה מגיעה "
                "העלייה. הרופא עשוי גם להזמין בדיקות הדמיה ובדיקות דם נוספות בהתאם לתמונה "
                "הקלינית.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם תוצאת <strong>בדיקת LDH בדם</strong> שלכם מעל טווח הייחוס, אל "
                "תיבהלו — אך פנו לרופא. אין לדחות את הבירור אם אתם סובלים מעייפות בלתי "
                "מוסברת, הזעות לילה, ירידה בלתי מכוונת במשקל, צהבת או שתן כהה.</p>"
                "<p>LDH הוא גם סמן חשוב במעקב טיפולי. בסרטנים כמו לימפומה או לוקמיה, "
                "שינויים ב<strong>רמות LDH</strong> משמשים לניטור תגובה לטיפול והתקדמות "
                "המחלה. מטופלים בטיפול צריכים לבדוק את רמת ה-LDH במרווחים סדירים.</p>"
                "<p>זכרו: <strong>LDH גבוה</strong> אינו אבחנה בפני עצמו. הרופא שלכם "
                "יבצע בדיקות נוספות לזיהוי הסיבה הבסיסית ולגיבוש תוכנית טיפול מתאימה. "
                "גילוי מוקדם ומעקב סדיר משפרים משמעותית את התוצאות במחלות רבות.</p>"
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
            heading="LDH ब्लड टेस्ट: आपके रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>LDH टेस्ट</strong> रक्त में <strong>लैक्टेट डिहाइड्रोजनेज़</strong> नामक एंज़ाइम "
                "के स्तर को मापता है — यह एंज़ाइम शरीर के लगभग हर ऊतक में पाया जाता है। LDH कोशिकीय ऊर्जा "
                "उत्पादन (ग्लाइकोलिसिस) में महत्वपूर्ण भूमिका निभाता है। जब कोशिकाएँ क्षतिग्रस्त या नष्ट "
                "होती हैं, तो LDH रक्तप्रवाह में आ जाता है और <strong>LDH का स्तर</strong> बढ़ जाता है — "
                "इसलिए इसे ऊतक क्षति का एक सामान्य मार्कर माना जाता है।</p>"
                "<p><strong>LDH ब्लड टेस्ट</strong> किसी विशिष्ट बीमारी का निदान करने के लिए नहीं, बल्कि "
                "कोशिकीय क्षति की उपस्थिति और सीमा का आकलन करने के लिए किया जाता है। <strong>उच्च LDH</strong> "
                "कई स्थितियों में दिखाई दे सकता है — लिम्फोमा और ल्यूकेमिया जैसे कैंसर से लेकर हेमोलिटिक "
                "एनीमिया, लिवर की बीमारी और मायोकार्डियल इन्फ़ार्क्शन तक। इस गाइड में आपको "
                "<strong>LDH की नॉर्मल रेंज</strong>, <strong>हाई LDH</strong> के कारण और डॉक्टर से कब "
                "मिलना चाहिए, इन सबकी जानकारी मिलेगी।</p>"
                "<p>LDH टेस्ट आमतौर पर कम्प्लीट ब्लड काउंट और अन्य बायोकेमिस्ट्री पैनल के साथ कराया "
                "जाता है। रिज़ल्ट को क्लिनिकल फ़ाइंडिंग्स और अतिरिक्त लैब डेटा के साथ मिलाकर समझना "
                "चाहिए; अकेला LDH मान डायग्नोस्टिक नहीं होता। यहाँ दी गई जानकारी शैक्षिक उद्देश्य "
                "से है — निदान और उपचार के लिए हमेशा डॉक्टर से परामर्श करें।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="LDH की नॉर्मल रेंज (रेफ़रेंस इंटरवल)",
            body_html=(
                "<p><strong>LDH की नॉर्मल रेंज</strong> लैब के अनुसार अलग-अलग हो सकती है; सामान्य रूप "
                "से स्वीकृत रेफ़रेंस वैल्यू नीचे दी गई तालिका में संक्षेपित हैं:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">LDH नॉर्मल रेंज</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">नवजात</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">शिशु (1–12 महीने)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">बच्चे (1–14 वर्ष)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>रेफ़रेंस इंटरवल टेस्ट मेथड और एनालाइज़र पर निर्भर करता है; इसलिए अपनी रिपोर्ट पर "
                "छपी रेंज से हमेशा तुलना करें। अगर आपके <strong>LDH का स्तर</strong> सामान्य से ऊपर है, "
                "तो डॉक्टर अतिरिक्त टेस्ट — जैसे LDH आइसोएंज़ाइम एनालिसिस, लिवर फ़ंक्शन टेस्ट या "
                "पेरिफ़ेरल ब्लड स्मीयर — करवा सकते हैं।</p>"
                "<p><strong>लैक्टेट डिहाइड्रोजनेज़</strong> पाँच आइसोएंज़ाइम रूपों में मौजूद होता है: "
                "LDH-1 और LDH-2 हृदय और लाल रक्त कोशिकाओं में, LDH-3 फेफड़ों में, और LDH-4 तथा "
                "LDH-5 लिवर और कंकाल पेशियों में सबसे अधिक होते हैं। आइसोएंज़ाइम पैटर्न यह पहचानने "
                "में मदद करता है कि किस अंग को नुकसान हुआ है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई LDH के कारण",
            body_html=(
                "<p><strong>हाई LDH</strong> कई अलग-अलग क्लिनिकल स्थितियों में दिखाई दे सकता है। "
                "<strong>उच्च LDH</strong> का मतलब हमेशा गंभीर बीमारी नहीं होता, लेकिन अंतर्निहित "
                "कारण की जाँच ज़रूरी है। सबसे सामान्य कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>हेमोलिटिक एनीमिया:</strong> लाल रक्त कोशिकाओं का तेज़ी से टूटना LDH "
                "(विशेषकर LDH-1 और LDH-2) में उल्लेखनीय वृद्धि का कारण बनता है।</li>"
                "<li><strong>कैंसर (लिम्फोमा, ल्यूकेमिया):</strong> तेज़ कोशिका चक्र और ट्यूमर "
                "लाइसिस LDH के स्तर को बढ़ाते हैं। लिम्फोमा में LDH एक महत्वपूर्ण प्रोग्नोस्टिक "
                "मार्कर है।</li>"
                "<li><strong>लिवर की बीमारियाँ:</strong> हेपेटाइटिस, सिरोसिस और लिवर मेटास्टेसिस "
                "हेपेटोसाइट क्षति के कारण LDH (विशेषकर LDH-5) बढ़ा सकती हैं।</li>"
                "<li><strong>मायोकार्डियल इन्फ़ार्क्शन (हार्ट अटैक):</strong> हृदय की मांसपेशी "
                "के नुकसान से LDH-1 और LDH-2 बढ़ते हैं; हालाँकि आजकल ट्रोपोनिन टेस्ट अधिक "
                "विशिष्ट कार्डियक बायोमार्कर के रूप में पसंद किए जाते हैं।</li>"
                "<li><strong>पल्मोनरी एम्बोलिज़्म और फेफड़ों की चोट:</strong> फेफड़ों के ऊतक "
                "को नुकसान LDH-3 बढ़ा सकता है।</li>"
                "<li><strong>मांसपेशियों की चोट और रबडोमायोलिसिस:</strong> तीव्र व्यायाम, "
                "आघात या कंकाल पेशी की क्षति LDH-4 और LDH-5 को बढ़ा सकती है।</li>"
                "<li><strong>संक्रमण और सूजन:</strong> मोनोन्यूक्लिओसिस और मेनिनजाइटिस जैसी "
                "संक्रामक बीमारियाँ, साथ ही प्रणालीगत सूजन, LDH बढ़ने का कारण बन सकती हैं।</li>"
                "</ul>"
                "<p>LDH आइसोएंज़ाइम एनालिसिस यह निर्धारित करने में मदद कर सकता है कि बढ़ोतरी "
                "किस अंग या ऊतक से हो रही है। डॉक्टर क्लिनिकल स्थिति के अनुसार इमेजिंग और "
                "अतिरिक्त ब्लड टेस्ट भी करवा सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपके <strong>LDH ब्लड टेस्ट</strong> का रिज़ल्ट रेफ़रेंस रेंज से ऊपर है, तो "
                "घबराएँ नहीं — लेकिन डॉक्टर से ज़रूर मिलें। अगर बिना वजह थकान, रात को पसीना आना, "
                "अनजाने में वज़न घटना, पीलिया या गहरे रंग का पेशाब जैसे लक्षण हैं तो मूल्यांकन में "
                "देरी नहीं करनी चाहिए।</p>"
                "<p>LDH उपचार की निगरानी में भी एक महत्वपूर्ण मार्कर है। लिम्फोमा या ल्यूकेमिया "
                "जैसे कैंसर में <strong>LDH के स्तर</strong> में बदलाव का उपयोग उपचार प्रतिक्रिया "
                "और बीमारी की प्रगति को ट्रैक करने के लिए किया जाता है। उपचारधीन मरीज़ों को "
                "नियमित अंतराल पर LDH की जाँच करानी चाहिए।</p>"
                "<p>याद रखें: <strong>हाई LDH</strong> अपने आप में कोई निदान नहीं है। आपके डॉक्टर "
                "अंतर्निहित कारण की पहचान करने और उचित उपचार योजना बनाने के लिए अतिरिक्त जाँच "
                "करेंगे। शीघ्र पहचान और नियमित फ़ॉलो-अप कई बीमारियों में परिणामों को काफ़ी बेहतर "
                "बनाते हैं।</p>"
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
            heading="اختبار LDH في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>يقيس اختبار <strong>LDH</strong> مستوى إنزيم <strong>نازعة هيدروجين اللاكتات</strong> "
                "في الدم — وهو إنزيم موجود في جميع أنسجة الجسم تقريباً. يؤدي LDH دوراً رئيسياً في "
                "إنتاج الطاقة الخلوية (تحلل الغلوكوز). عندما تتضرر الخلايا أو تُدمَّر، يتسرب LDH "
                "إلى مجرى الدم وترتفع <strong>مستويات LDH</strong>، مما يجعله مؤشراً عاماً على "
                "تلف الأنسجة.</p>"
                "<p>لا يُطلب <strong>اختبار LDH في الدم</strong> لتشخيص مرض محدد، بل لتقييم وجود "
                "ومدى الضرر الخلوي. يمكن أن يظهر <strong>ارتفاع LDH</strong> في مجموعة واسعة من "
                "الحالات — من السرطانات مثل اللمفومة وسرطان الدم إلى فقر الدم الانحلالي وأمراض "
                "الكبد واحتشاء عضلة القلب. ستجد في هذا الدليل <strong>المعدل الطبيعي لـ LDH</strong> "
                "وأسباب <strong>ارتفاع LDH</strong> ومتى يجب مراجعة الطبيب.</p>"
                "<p>يُطلب اختبار LDH عادةً مع تعداد الدم الكامل وفحوصات كيميائية أخرى. يجب تفسير "
                "النتائج إلى جانب المعطيات السريرية والمخبرية الإضافية؛ قيمة LDH واحدة ليست "
                "تشخيصية بحد ذاتها. المعلومات هنا تثقيفية — استشر دائماً طبيباً مختصاً.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدل الطبيعي لـ LDH (النطاقات المرجعية)",
            body_html=(
                "<p>قد يختلف <strong>المعدل الطبيعي لـ LDH</strong> بين المختبرات؛ القيم المرجعية "
                "المقبولة عموماً ملخصة في الجدول التالي:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المعدل الطبيعي لـ LDH</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">البالغون</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–246 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">حديثو الولادة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">160–450 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الرضّع (1–12 شهراً)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">150–360 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الأطفال (1–14 سنة)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">120–300 U/L</td></tr>'
                "</tbody></table>"
                "<p>تعتمد النطاقات المرجعية على طريقة الفحص والجهاز المستخدم؛ لذا قارن دائماً "
                "نتيجتك بالنطاق المطبوع في تقريرك. إذا كانت <strong>مستويات LDH</strong> لديك "
                "أعلى من الطبيعي، فقد يطلب الطبيب فحوصات إضافية — مثل تحليل الإنزيمات المتماثلة "
                "لـ LDH، واختبارات وظائف الكبد، أو مسحة الدم المحيطية — لتحديد السبب.</p>"
                "<p>يوجد إنزيم <strong>نازعة هيدروجين اللاكتات</strong> في خمسة أشكال متماثلة: "
                "LDH-1 وLDH-2 يتركزان في القلب وكريات الدم الحمراء، LDH-3 في الرئتين، وLDH-4 "
                "وLDH-5 في الكبد والعضلات الهيكلية. يساعد نمط الإنزيمات المتماثلة في تحديد "
                "العضو المصاب.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع مستويات LDH",
            body_html=(
                "<p>يمكن أن يظهر <strong>ارتفاع LDH</strong> في مجموعة متنوعة من الحالات السريرية. "
                "لا يعني <strong>ارتفاع LDH</strong> دائماً مرضاً خطيراً، لكن يجب التحقيق في "
                "السبب الكامن. تشمل الأسباب الأكثر شيوعاً:</p>"
                "<ul>"
                "<li><strong>فقر الدم الانحلالي:</strong> التدمير المتسارع لكريات الدم الحمراء "
                "يسبب ارتفاعاً ملحوظاً في LDH (خاصةً LDH-1 وLDH-2).</li>"
                "<li><strong>السرطان (اللمفومة، سرطان الدم):</strong> دوران الخلايا السريع وانحلال "
                "الورم يرفعان مستويات LDH. يُعدّ LDH مؤشراً تنبؤياً مهماً في اللمفومة.</li>"
                "<li><strong>أمراض الكبد:</strong> التهاب الكبد والتليف والانبثاث الكبدي قد ترفع "
                "LDH (خاصةً LDH-5) نتيجة تلف الخلايا الكبدية.</li>"
                "<li><strong>احتشاء عضلة القلب (النوبة القلبية):</strong> تلف عضلة القلب يرفع "
                "LDH-1 وLDH-2؛ ومع ذلك، يُفضّل حالياً اختبار التروبونين كمؤشر قلبي أكثر "
                "تخصصاً.</li>"
                "<li><strong>الانصمام الرئوي وإصابة الرئة:</strong> تلف النسيج الرئوي قد يرفع "
                "LDH-3.</li>"
                "<li><strong>إصابة العضلات وانحلال الربيدات:</strong> التمارين المكثفة أو "
                "الإصابات أو تلف العضلات الهيكلية قد ترفع LDH-4 وLDH-5.</li>"
                "<li><strong>العدوى والالتهاب:</strong> الأمراض المعدية مثل كثرة الوحيدات "
                "والتهاب السحايا، وكذلك الالتهاب الجهازي، قد تسبب ارتفاع LDH.</li>"
                "</ul>"
                "<p>يمكن أن يساعد تحليل الإنزيمات المتماثلة لـ LDH في تحديد العضو أو النسيج "
                "المسؤول عن الارتفاع. قد يطلب الطبيب أيضاً فحوصات تصوير وتحاليل دم إضافية "
                "بناءً على الصورة السريرية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كانت نتيجة <strong>اختبار LDH في الدم</strong> أعلى من النطاق المرجعي، "
                "فلا تقلق ولكن راجع الطبيب. لا ينبغي تأخير التقييم إذا كنت تعاني من إرهاق غير "
                "مبرّر، أو تعرّق ليلي، أو فقدان وزن غير مقصود، أو يرقان، أو بول داكن.</p>"
                "<p>يُعدّ LDH أيضاً مؤشراً مهماً في مراقبة العلاج. في السرطانات مثل اللمفومة أو "
                "سرطان الدم، تُستخدم التغيرات في <strong>مستويات LDH</strong> لمتابعة الاستجابة "
                "للعلاج وتطور المرض. يجب على المرضى الخاضعين للعلاج فحص LDH بانتظام.</p>"
                "<p>تذكّر: <strong>ارتفاع LDH</strong> ليس تشخيصاً بحد ذاته. سيُجري طبيبك فحوصات "
                "إضافية لتحديد السبب الكامن ووضع خطة علاج مناسبة. الاكتشاف المبكر والمتابعة "
                "المنتظمة يُحسّنان بشكل كبير نتائج العلاج في كثير من الأمراض.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_ldh_sections_by_lang() -> dict:
    """Returns sections dict for LDH article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_ldh_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for LDH article (all 9 languages)."""
    return {
        "tr": [
            {"question": "LDH testi nedir?",
             "answer": "LDH testi, kandaki laktat dehidrojenaz enziminin düzeyini ölçen bir kan testidir. Hücre hasarı veya yıkımı olduğunda LDH kana sızar; bu nedenle test, doku hasarının varlığını ve boyutunu değerlendirmek amacıyla kullanılır."},
            {"question": "LDH normal değeri kaçtır?",
             "answer": "Yetişkinlerde LDH normal aralığı genellikle 120–246 U/L kabul edilir. Ancak bu değer laboratuvar yöntemine göre farklılık gösterebilir; kendi raporunuzdaki referans aralığına bakmalısınız."},
            {"question": "LDH yüksekliği kanser mi demek?",
             "answer": "Hayır, LDH yüksekliği birçok nedene bağlı olabilir: hemolitik anemi, karaciğer hastalığı, kas hasarı, enfeksiyon veya kanser. Tek başına LDH değeri tanı koydurtmaz; altta yatan nedeni belirlemek için ek testler gerekir."},
        ],
        "en": [
            {"question": "What is an LDH test?",
             "answer": "An LDH test measures the level of lactate dehydrogenase enzyme in the blood. When cells are damaged or destroyed, LDH leaks into the bloodstream; the test is therefore used to assess the presence and extent of tissue damage."},
            {"question": "What is the normal LDH range?",
             "answer": "The generally accepted LDH normal range for adults is 120–246 U/L. However, reference intervals can vary by laboratory method, so always compare your result with the range on your own report."},
            {"question": "Does high LDH mean cancer?",
             "answer": "No. Elevated LDH can result from many conditions including haemolytic anaemia, liver disease, muscle injury, infection, or cancer. A single LDH value is not diagnostic; additional tests are needed to determine the underlying cause."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de LDH?",
             "answer": "La prueba de LDH mide el nivel de la enzima lactato deshidrogenasa en la sangre. Cuando las células se dañan o destruyen, la LDH se libera al torrente sanguíneo; por eso se utiliza para evaluar la presencia y el alcance del daño tisular."},
            {"question": "¿Cuál es el rango normal de LDH?",
             "answer": "El rango normal de LDH para adultos generalmente aceptado es de 120–246 U/L. Sin embargo, los intervalos de referencia pueden variar según el método del laboratorio, por lo que debe comparar siempre su resultado con el rango de su propio informe."},
            {"question": "¿LDH alta significa cáncer?",
             "answer": "No. La LDH elevada puede deberse a muchas causas: anemia hemolítica, enfermedad hepática, lesión muscular, infección o cáncer. Un valor aislado de LDH no es diagnóstico; se necesitan pruebas adicionales para determinar la causa."},
        ],
        "de": [
            {"question": "Was ist ein LDH-Test?",
             "answer": "Ein LDH-Test misst den Spiegel des Enzyms Laktatdehydrogenase im Blut. Werden Zellen geschädigt oder zerstört, gelangt LDH in den Blutkreislauf; der Test dient daher zur Beurteilung von Vorhandensein und Ausmaß eines Gewebeschadens."},
            {"question": "Was sind die LDH-Normalwerte?",
             "answer": "Der allgemein akzeptierte LDH-Normalbereich für Erwachsene liegt bei 120–246 U/L. Die Referenzbereiche können jedoch je nach Labormethode variieren; vergleichen Sie Ihr Ergebnis daher immer mit dem Bereich auf Ihrem eigenen Befund."},
            {"question": "Bedeutet ein erhöhter LDH-Wert Krebs?",
             "answer": "Nein. Ein erhöhter LDH-Wert kann viele Ursachen haben: hämolytische Anämie, Lebererkrankungen, Muskelverletzungen, Infektionen oder Krebs. Ein einzelner LDH-Wert ist nicht diagnostisch; zusätzliche Untersuchungen sind nötig, um die Ursache zu klären."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test LDH ?",
             "answer": "Le test LDH mesure le taux de l'enzyme lactate déshydrogénase dans le sang. Lorsque des cellules sont endommagées ou détruites, la LDH passe dans la circulation sanguine ; ce test est donc utilisé pour évaluer la présence et l'étendue d'un dommage tissulaire."},
            {"question": "Quelles sont les valeurs normales de LDH ?",
             "answer": "Les valeurs normales de LDH chez l'adulte se situent généralement entre 120 et 246 U/L. Les intervalles de référence peuvent varier selon la méthode du laboratoire ; comparez toujours votre résultat avec la plage indiquée sur votre propre rapport."},
            {"question": "Un taux de LDH élevé signifie-t-il un cancer ?",
             "answer": "Non. Une LDH élevée peut résulter de nombreuses causes : anémie hémolytique, maladie hépatique, lésion musculaire, infection ou cancer. Un seul dosage de LDH n'est pas diagnostique ; des examens supplémentaires sont nécessaires pour déterminer la cause."},
        ],
        "it": [
            {"question": "Cos'è il test LDH?",
             "answer": "Il test LDH misura il livello dell'enzima lattato deidrogenasi nel sangue. Quando le cellule vengono danneggiate o distrutte, la LDH passa nel sangue; il test viene quindi utilizzato per valutare la presenza e l'entità del danno tissutale."},
            {"question": "Quali sono i valori normali della LDH?",
             "answer": "L'intervallo normale della LDH per gli adulti è generalmente compreso tra 120 e 246 U/L. Gli intervalli di riferimento possono variare in base al metodo del laboratorio; confrontate sempre il vostro risultato con l'intervallo indicato nel vostro referto."},
            {"question": "LDH alta significa cancro?",
             "answer": "No. La LDH elevata può derivare da molte cause: anemia emolitica, malattie epatiche, lesioni muscolari, infezioni o cancro. Un singolo valore di LDH non è diagnostico; sono necessari ulteriori esami per identificare la causa sottostante."},
        ],
        "he": [
            {"question": "מהי בדיקת LDH?",
             "answer": "בדיקת LDH מודדת את רמת האנזים לקטט דהידרוגנאז בדם. כאשר תאים ניזוקים או נהרסים, LDH דולף לזרם הדם; לכן הבדיקה משמשת להערכת נוכחות והיקף הנזק הרקמתי."},
            {"question": "מהו טווח הנורמה של LDH?",
             "answer": "טווח הנורמה המקובל של LDH למבוגרים הוא 120–246 U/L. טווחי הייחוס עשויים להשתנות לפי שיטת המעבדה; השוו תמיד את התוצאה שלכם לטווח המופיע בדוח שלכם."},
            {"question": "האם LDH גבוה פירושו סרטן?",
             "answer": "לא. LDH מוגבר יכול לנבוע מסיבות רבות: אנמיה המוליטית, מחלות כבד, פגיעה בשרירים, זיהום או סרטן. ערך LDH בודד אינו מאבחן; נדרשות בדיקות נוספות לזיהוי הסיבה הבסיסית."},
        ],
        "hi": [
            {"question": "LDH टेस्ट क्या है?",
             "answer": "LDH टेस्ट रक्त में लैक्टेट डिहाइड्रोजनेज़ एंज़ाइम के स्तर को मापता है। जब कोशिकाएँ क्षतिग्रस्त या नष्ट होती हैं तो LDH रक्तप्रवाह में आ जाता है; इसलिए इस टेस्ट का उपयोग ऊतक क्षति की उपस्थिति और सीमा का आकलन करने के लिए किया जाता है।"},
            {"question": "LDH की नॉर्मल रेंज क्या है?",
             "answer": "वयस्कों के लिए LDH की सामान्य रूप से स्वीकृत नॉर्मल रेंज 120–246 U/L है। हालाँकि, रेफ़रेंस इंटरवल लैब मेथड के अनुसार भिन्न हो सकता है; अपनी रिपोर्ट पर छपी रेंज से हमेशा तुलना करें।"},
            {"question": "क्या हाई LDH का मतलब कैंसर है?",
             "answer": "नहीं। उच्च LDH कई कारणों से हो सकता है: हेमोलिटिक एनीमिया, लिवर की बीमारी, मांसपेशियों की चोट, संक्रमण या कैंसर। अकेला LDH मान डायग्नोस्टिक नहीं होता; अंतर्निहित कारण जानने के लिए अतिरिक्त जाँच ज़रूरी है।"},
        ],
        "ar": [
            {"question": "ما هو اختبار LDH؟",
             "answer": "اختبار LDH يقيس مستوى إنزيم نازعة هيدروجين اللاكتات في الدم. عندما تتضرر الخلايا أو تُدمَّر، يتسرب LDH إلى مجرى الدم؛ لذلك يُستخدم هذا الاختبار لتقييم وجود ومدى تلف الأنسجة."},
            {"question": "ما هو المعدل الطبيعي لـ LDH؟",
             "answer": "المعدل الطبيعي المقبول عموماً لـ LDH عند البالغين هو 120–246 U/L. قد تختلف النطاقات المرجعية حسب طريقة المختبر؛ قارن دائماً نتيجتك بالنطاق المطبوع في تقريرك."},
            {"question": "هل ارتفاع LDH يعني سرطاناً؟",
             "answer": "لا. يمكن أن ينتج ارتفاع LDH عن أسباب عديدة: فقر الدم الانحلالي، أمراض الكبد، إصابة العضلات، العدوى أو السرطان. قيمة LDH واحدة ليست تشخيصية؛ تلزم فحوصات إضافية لتحديد السبب الكامن."},
        ],
    }
