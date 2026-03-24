# -*- coding: utf-8 -*-
"""
ANA (Antinuclear Antibody) blog article — full body content for all 9 languages.
Used by blog_i18n._article_ana().
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
            heading="ANA (antinükleer antikor) testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>ANA testi</strong> (antinükleer antikor testi), bağışıklık sisteminin vücudun kendi hücre "
                "çekirdeklerine karşı antikor üretip üretmediğini ölçen bir <strong>otoimmün kan testidir</strong>. "
                "ANA kan testi; sistemik lupus eritematozus (SLE), Sjögren sendromu, skleroderma ve romatoid artrit "
                "gibi otoimmün hastalıkların taranmasında en sık başvurulan laboratuvar testlerinden biridir. "
                "Ancak <strong>ANA pozitif</strong> çıkması her zaman bir hastalık anlamına gelmez; sağlıklı "
                "bireylerin yaklaşık %15-20'sinde düşük titrede pozitiflik saptanabilir.</p>"
                "<p>Bu rehberde ANA test sonuçlarının nasıl yorumlanacağını, ANA titreleri ile boyanma paternlerinin "
                "klinik önemini ve hangi durumlarda doktora başvurmanız gerektiğini açıklıyoruz. Buradaki bilgiler "
                "eğitim amaçlıdır; kesin tanı ve tedavi için mutlaka bir romatoloji veya iç hastalıkları uzmanına "
                "danışın.</p>"
                "<p>ANA testi genellikle eklem ağrısı, cilt döküntüleri, açıklanamayan yorgunluk veya tekrarlayan "
                "ateş gibi otoimmün hastalık belirtileri gösteren hastalara istenir. Test, dolaylı immünofloresan "
                "(IFA) yöntemiyle yapılır ve hem titreyi hem de boyanma paternini raporlar.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ANA test sonuçları nasıl yorumlanır?",
            body_html=(
                "<p><strong>ANA test sonuçları</strong> titre (seyreltme oranı) ve boyanma paterni olmak üzere iki "
                "bileşenle değerlendirilir. Titre ne kadar yüksekse, otoimmün hastalık olasılığı o kadar artar; "
                "ancak tek başına titre tanı koydurmaz. Aşağıdaki tabloda <strong>ANA titrelerinin</strong> genel "
                "klinik yorumu özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">ANA titresi</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Yorum</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Düşük pozitiflik; sağlıklı bireylerde sık görülür, klinik önemi genellikle sınırlıdır</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Sınırda pozitiflik; semptomlar eşliğinde değerlendirilmeli</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Orta düzeyde pozitiflik; otoimmün hastalık olasılığı artar</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 ve üzeri</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Yüksek pozitiflik; otoimmün hastalık ile güçlü ilişki, ileri tetkik gerektirir</td></tr>'
                "</tbody></table>"
                "<p>Boyanma paterni de tanıya yol gösterir. <strong>Homojen (diffüz)</strong> patern SLE ile, "
                "<strong>benekli (speckled)</strong> patern Sjögren sendromu ve mikst bağ dokusu hastalığı ile, "
                "<strong>nükleolar</strong> patern skleroderma ile, <strong>sentromer</strong> paterni ise sınırlı "
                "skleroderma (CREST sendromu) ile sıklıkla ilişkilendirilir.</p>"
                "<p><strong>ANA pozitif</strong> sonucu alan herkesin otoimmün bir hastalığı olduğu söylenemez. "
                "Yaşlı bireylerde, bazı enfeksiyonlarda ve bazı ilaçların kullanımında da yanlış pozitiflik "
                "görülebilir. Bu nedenle ANA test sonuçları mutlaka klinik bulgular ve ek laboratuvar testleriyle "
                "birlikte değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="ANA pozitifliğinin nedenleri",
            body_html=(
                "<p><strong>Pozitif ANA</strong> sonucu birçok farklı durumda ortaya çıkabilir. <strong>ANA pozitif "
                "anlamı</strong> her zaman bir otoimmün hastalık olduğu değildir; sonucun klinik bağlamda "
                "değerlendirilmesi gerekir. ANA pozitifliğine neden olabilecek başlıca durumlar şunlardır:</p>"
                "<ul>"
                "<li><strong>Sistemik lupus eritematozus (SLE):</strong> ANA pozitifliğinin en bilinen nedenidir; "
                "SLE hastalarının %95'inden fazlasında ANA pozitif saptanır.</li>"
                "<li><strong>Sjögren sendromu:</strong> Ağız ve göz kuruluğu ile karakterize bu otoimmün hastalıkta "
                "ANA sıklıkla pozitiftir ve benekli patern görülür.</li>"
                "<li><strong>Skleroderma (sistemik skleroz):</strong> Cilt ve iç organlarda sertleşmeye yol açan bu "
                "hastalıkta nükleolar veya sentromer paterni beklenir.</li>"
                "<li><strong>Romatoid artrit:</strong> Eklem iltihabı ile seyreden romatoid artritte ANA pozitifliği "
                "hastaların bir kısmında görülür.</li>"
                "<li><strong>İlaca bağlı lupus:</strong> Hidralazin, prokainamid, izoniazid gibi ilaçlar geçici ANA "
                "pozitifliğine yol açabilir.</li>"
                "<li><strong>Enfeksiyonlar:</strong> Hepatit C, Epstein-Barr virüsü gibi kronik enfeksiyonlar düşük "
                "titrede ANA pozitifliğine neden olabilir.</li>"
                "<li><strong>Sağlıklı bireyler:</strong> Genel popülasyonun %15-20'sinde, özellikle yaşlı kadınlarda, "
                "düşük titrede (1:40–1:80) ANA pozitifliği herhangi bir hastalık olmaksızın saptanabilir.</li>"
                "</ul>"
                "<p>Doktorunuz ANA pozitifliğinin nedenini belirlemek için anti-dsDNA, anti-Smith, anti-SSA/SSB, "
                "anti-Scl-70 gibi spesifik otoantikor testleri ve tam kan sayımı, sedimentasyon, CRP gibi ek "
                "laboratuvar tetkikleri isteyebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>ANA kan testi sonucunuz pozitif çıktıysa panik yapmayın, ancak özellikle yüksek titrede "
                "(1:160 ve üzeri) pozitiflik varsa veya eklem ağrısı, cilt döküntüleri, ağız-göz kuruluğu, "
                "açıklanamayan ateş ya da saç dökülmesi gibi belirtiler eşlik ediyorsa bir romatoloji uzmanına "
                "başvurmanız önerilir.</p>"
                "<p>Düşük titrede ANA pozitifliği sağlıklı bireylerde de görülebileceğinden, tek başına ANA "
                "pozitifliği kesin bir hastalık tanısı koymaz. Doktorunuz klinik muayene, detaylı öykü ve ek "
                "laboratuvar tetkikleri ile durumu değerlendirecektir. Erken tanı, otoimmün hastalıkların organ "
                "hasarını önlemede kritik öneme sahiptir.</p>"
                "<p>Unutmayın: <strong>ANA test sonuçları</strong> yalnızca bir tarama aracıdır. Pozitif sonuç "
                "alan herkes otoimmün hasta değildir ve negatif sonuç otoimmün hastalığı tamamen dışlamaz. "
                "Semptomlarınız devam ediyorsa düzenli takip ve gerektiğinde tekrarlayan testler büyük önem "
                "taşır.</p>"
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
            heading="ANA blood test: what your results mean",
            body_html=(
                "<p>The <strong>ANA test</strong> (antinuclear antibody test) is an <strong>autoimmune blood test</strong> "
                "that detects antibodies directed against the nuclei of your own cells. An <strong>ANA blood test</strong> "
                "is one of the first-line screening tools for autoimmune diseases such as systemic lupus erythematosus "
                "(SLE), Sjögren's syndrome, scleroderma, and rheumatoid arthritis. However, a <strong>positive ANA</strong> "
                "result does not automatically confirm an autoimmune disease&mdash;approximately 15&ndash;20% of healthy "
                "individuals test positive at low titers.</p>"
                "<p>In this guide we explain how to interpret your <strong>ANA test results</strong>, what "
                "<strong>ANA titers</strong> and staining patterns mean clinically, and when you should see a doctor. "
                "The information here is educational&mdash;always discuss your results with a qualified rheumatologist or "
                "internal medicine specialist for a proper diagnosis.</p>"
                "<p>An ANA blood test is typically ordered when a patient presents with joint pain, skin rashes, "
                "unexplained fatigue, or recurrent fevers suggestive of an autoimmune condition. The test is performed "
                "using indirect immunofluorescence (IFA) and reports both the titer and the staining pattern.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="How to interpret ANA test results",
            body_html=(
                "<p><strong>ANA test results</strong> are evaluated by two components: the titer (dilution ratio) and "
                "the staining pattern. The higher the <strong>ANA titer</strong>, the greater the likelihood of an "
                "autoimmune disease, but titer alone does not establish a diagnosis. The table below summarises the "
                "general clinical interpretation of ANA titers:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">ANA titer</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretation</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Low positive; common in healthy individuals, usually of limited clinical significance</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Borderline positive; should be evaluated in the context of symptoms</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Moderate positive; increased probability of autoimmune disease</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 and above</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">High positive; strongly associated with autoimmune disease, further investigation required</td></tr>'
                "</tbody></table>"
                "<p>The staining pattern also guides diagnosis. A <strong>homogeneous (diffuse)</strong> pattern is "
                "frequently associated with SLE, a <strong>speckled</strong> pattern with Sjögren's syndrome and mixed "
                "connective tissue disease, a <strong>nucleolar</strong> pattern with scleroderma, and a "
                "<strong>centromere</strong> pattern with limited scleroderma (CREST syndrome).</p>"
                "<p>Not everyone with a <strong>positive ANA</strong> has an autoimmune disease. False positives can "
                "occur in elderly individuals, during certain infections, and with some medications. Therefore, "
                "<strong>ANA test results</strong> must always be interpreted alongside clinical findings and "
                "additional laboratory tests.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of a positive ANA result",
            body_html=(
                "<p>A <strong>positive ANA</strong> result can arise in many different situations. The "
                "<strong>positive ANA meaning</strong> is not always an autoimmune disease&mdash;the result must be "
                "evaluated in its clinical context. The most common causes of ANA positivity include:</p>"
                "<ul>"
                "<li><strong>Systemic lupus erythematosus (SLE):</strong> The best-known cause of ANA positivity; "
                "over 95% of SLE patients test ANA positive.</li>"
                "<li><strong>Sjögren's syndrome:</strong> This autoimmune condition characterised by dry mouth and "
                "dry eyes frequently produces a positive ANA with a speckled pattern.</li>"
                "<li><strong>Scleroderma (systemic sclerosis):</strong> This disease causes hardening of the skin and "
                "internal organs; nucleolar or centromere patterns are expected.</li>"
                "<li><strong>Rheumatoid arthritis:</strong> ANA positivity is observed in a proportion of patients "
                "with this chronic joint-inflammatory condition.</li>"
                "<li><strong>Drug-induced lupus:</strong> Medications such as hydralazine, procainamide, and isoniazid "
                "can cause transient ANA positivity.</li>"
                "<li><strong>Infections:</strong> Chronic infections such as hepatitis C and Epstein-Barr virus may "
                "produce low-titer ANA positivity.</li>"
                "<li><strong>Healthy individuals:</strong> Approximately 15&ndash;20% of the general population, "
                "especially older women, may test ANA positive at low titers (1:40&ndash;1:80) without any underlying "
                "disease.</li>"
                "</ul>"
                "<p>To determine the cause of ANA positivity, your doctor may order specific autoantibody tests such "
                "as anti-dsDNA, anti-Smith, anti-SSA/SSB, and anti-Scl-70, along with a complete blood count, ESR, "
                "and CRP.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your <strong>ANA blood test</strong> result is positive, do not panic, but consult a "
                "rheumatologist&mdash;especially if the titer is 1:160 or higher, or if you experience symptoms such "
                "as joint pain, skin rashes, dry mouth or eyes, unexplained fever, or hair loss.</p>"
                "<p>Because low-titer ANA positivity can also occur in healthy individuals, a positive ANA alone does "
                "not confirm an autoimmune diagnosis. Your doctor will perform a clinical examination, take a detailed "
                "history, and order additional laboratory tests to clarify the situation. Early diagnosis is critical "
                "in preventing organ damage from autoimmune diseases.</p>"
                "<p>Remember: <strong>ANA test results</strong> are only a screening tool. Not everyone who tests "
                "positive has an autoimmune disease, and a negative result does not completely rule one out. If your "
                "symptoms persist, regular follow-up and repeat testing when appropriate are essential.</p>"
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
            heading="Prueba de ANA en sangre: qué significan sus resultados",
            body_html=(
                "<p>La <strong>prueba de ANA</strong> (anticuerpos antinucleares) es un <strong>análisis de sangre "
                "autoinmune</strong> que detecta anticuerpos dirigidos contra los núcleos de las propias células del "
                "organismo. La prueba de ANA en sangre es una de las herramientas de cribado de primera línea para "
                "enfermedades autoinmunes como el lupus eritematoso sistémico (LES), el síndrome de Sjögren, la "
                "esclerodermia y la artritis reumatoide. Sin embargo, un resultado <strong>ANA positivo</strong> no "
                "confirma automáticamente una enfermedad autoinmune; aproximadamente el 15&ndash;20 % de las personas "
                "sanas da positivo a títulos bajos.</p>"
                "<p>En esta guía explicamos cómo interpretar los <strong>resultados de la prueba de ANA</strong>, qué "
                "significan los <strong>títulos de ANA</strong> y los patrones de tinción, y cuándo debe consultar al "
                "médico. Esta información es educativa; consulte siempre a un reumatólogo para un diagnóstico "
                "adecuado.</p>"
                "<p>La prueba de ANA suele solicitarse cuando un paciente presenta dolor articular, erupciones "
                "cutáneas, fatiga inexplicable o fiebre recurrente sugestivos de una enfermedad autoinmune. Se "
                "realiza mediante inmunofluorescencia indirecta (IFI) y reporta tanto el título como el patrón de "
                "tinción.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="¿Cómo interpretar los resultados de la prueba de ANA?",
            body_html=(
                "<p>Los <strong>resultados de la prueba de ANA</strong> se evalúan mediante dos componentes: el "
                "título (proporción de dilución) y el patrón de tinción. Cuanto mayor es el <strong>título de "
                "ANA</strong>, mayor es la probabilidad de enfermedad autoinmune, pero el título por sí solo no "
                "establece un diagnóstico. La siguiente tabla resume la interpretación clínica general:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Título de ANA</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretación</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo bajo; frecuente en personas sanas, significación clínica generalmente limitada</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo limítrofe; debe evaluarse en el contexto de los síntomas</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo moderado; aumenta la probabilidad de enfermedad autoinmune</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 y superior</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo alto; fuerte asociación con enfermedad autoinmune, requiere investigación adicional</td></tr>'
                "</tbody></table>"
                "<p>El patrón de tinción también orienta el diagnóstico. Un patrón <strong>homogéneo (difuso)"
                "</strong> se asocia frecuentemente con el LES, un patrón <strong>moteado (speckled)</strong> con "
                "el síndrome de Sjögren y la enfermedad mixta del tejido conectivo, un patrón <strong>nucleolar"
                "</strong> con la esclerodermia y un patrón de <strong>centrómero</strong> con la esclerodermia "
                "limitada (síndrome CREST).</p>"
                "<p>No todas las personas con <strong>ANA positivo</strong> tienen una enfermedad autoinmune. Los "
                "falsos positivos pueden ocurrir en personas mayores, durante ciertas infecciones y con algunos "
                "medicamentos. Por ello, los resultados de ANA deben interpretarse siempre junto con los hallazgos "
                "clínicos y pruebas de laboratorio complementarias.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de un resultado ANA positivo",
            body_html=(
                "<p>Un resultado <strong>ANA positivo</strong> puede presentarse en muchas situaciones diferentes. "
                "El significado de un ANA positivo no siempre es una enfermedad autoinmune; el resultado debe "
                "evaluarse en su contexto clínico. Las causas más frecuentes incluyen:</p>"
                "<ul>"
                "<li><strong>Lupus eritematoso sistémico (LES):</strong> La causa más conocida de positividad de "
                "ANA; más del 95 % de los pacientes con LES presentan ANA positivo.</li>"
                "<li><strong>Síndrome de Sjögren:</strong> Esta enfermedad autoinmune caracterizada por sequedad "
                "bucal y ocular produce con frecuencia ANA positivo con patrón moteado.</li>"
                "<li><strong>Esclerodermia (esclerosis sistémica):</strong> Produce endurecimiento de la piel y "
                "órganos internos; se esperan patrones nucleolar o centrómero.</li>"
                "<li><strong>Artritis reumatoide:</strong> La positividad de ANA se observa en una proporción de "
                "pacientes con esta enfermedad inflamatoria articular crónica.</li>"
                "<li><strong>Lupus inducido por fármacos:</strong> Medicamentos como hidralazina, procainamida e "
                "isoniazida pueden provocar positividad de ANA transitoria.</li>"
                "<li><strong>Infecciones:</strong> Infecciones crónicas como la hepatitis C y el virus de "
                "Epstein-Barr pueden producir positividad de ANA a títulos bajos.</li>"
                "<li><strong>Personas sanas:</strong> Aproximadamente el 15&ndash;20 % de la población general, "
                "especialmente mujeres mayores, puede dar positivo a títulos bajos (1:40&ndash;1:80) sin ninguna "
                "enfermedad subyacente.</li>"
                "</ul>"
                "<p>Para determinar la causa de la positividad de ANA, su médico puede solicitar pruebas de "
                "autoanticuerpos específicos como anti-ADNds, anti-Smith, anti-SSA/SSB y anti-Scl-70, junto con "
                "hemograma completo, VSG y PCR.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si su prueba de ANA en sangre resulta positiva, no se alarme, pero consulte a un reumatólogo, "
                "especialmente si el título es de 1:160 o superior, o si presenta síntomas como dolor articular, "
                "erupciones cutáneas, sequedad bucal u ocular, fiebre inexplicable o caída del cabello.</p>"
                "<p>Dado que la positividad de ANA a títulos bajos también puede darse en personas sanas, un ANA "
                "positivo por sí solo no confirma un diagnóstico autoinmune. Su médico realizará un examen clínico, "
                "tomará un historial detallado y solicitará pruebas de laboratorio adicionales. El diagnóstico "
                "precoz es fundamental para prevenir el daño orgánico de las enfermedades autoinmunes.</p>"
                "<p>Recuerde: los resultados de la prueba de ANA son solo una herramienta de cribado. No todas "
                "las personas con resultado positivo tienen una enfermedad autoinmune, y un resultado negativo no "
                "la descarta por completo. Si sus síntomas persisten, el seguimiento regular y la repetición de "
                "pruebas cuando sea apropiado son esenciales.</p>"
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
            heading="ANA-Test: Was Ihre Blutwerte bedeuten",
            body_html=(
                "<p>Der <strong>ANA-Test</strong> (Antinukleäre-Antikörper-Test) ist ein <strong>Autoimmun-Bluttest"
                "</strong>, der Antikörper gegen die Zellkerne des eigenen Körpers nachweist. Der ANA-Bluttest "
                "gehört zu den wichtigsten Screening-Verfahren für Autoimmunerkrankungen wie systemischen Lupus "
                "erythematodes (SLE), Sjögren-Syndrom, Sklerodermie und rheumatoide Arthritis. Ein <strong>positiver "
                "ANA</strong>-Befund bedeutet jedoch nicht automatisch eine Erkrankung&mdash;bei etwa 15&ndash;20 % "
                "gesunder Personen wird ein niedrig-titriger positiver ANA-Befund nachgewiesen.</p>"
                "<p>In diesem Ratgeber erläutern wir, wie Sie Ihre <strong>ANA-Testergebnisse</strong> interpretieren, "
                "welche klinische Bedeutung <strong>ANA-Titer</strong> und Fluoreszenzmuster haben und wann Sie einen "
                "Arzt aufsuchen sollten. Die Inhalte dienen der Aufklärung&mdash;für eine Diagnose wenden Sie sich "
                "bitte an einen Rheumatologen oder Internisten.</p>"
                "<p>Ein ANA-Bluttest wird typischerweise angeordnet, wenn Gelenkschmerzen, Hautausschläge, "
                "unerklärliche Müdigkeit oder wiederkehrendes Fieber auf eine Autoimmunerkrankung hindeuten. "
                "Der Test erfolgt mittels indirekter Immunfluoreszenz (IIF) und gibt sowohl den Titer als auch "
                "das Fluoreszenzmuster an.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ANA-Testergebnisse richtig interpretieren",
            body_html=(
                "<p><strong>ANA-Testergebnisse</strong> werden anhand von zwei Komponenten bewertet: dem Titer "
                "(Verdünnungsverhältnis) und dem Fluoreszenzmuster. Je höher der <strong>ANA-Titer</strong>, desto "
                "wahrscheinlicher ist eine Autoimmunerkrankung; der Titer allein stellt jedoch keine Diagnose. Die "
                "folgende Tabelle fasst die allgemeine klinische Interpretation zusammen:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">ANA-Titer</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretation</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Niedrig positiv; häufig bei Gesunden, klinische Bedeutung meist gering</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Grenzwertig positiv; sollte im Zusammenhang mit Symptomen bewertet werden</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mäßig positiv; erhöhte Wahrscheinlichkeit einer Autoimmunerkrankung</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 und höher</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hoch positiv; starke Assoziation mit Autoimmunerkrankung, weitere Abklärung erforderlich</td></tr>'
                "</tbody></table>"
                "<p>Das Fluoreszenzmuster liefert ebenfalls diagnostische Hinweise. Ein <strong>homogenes (diffuses)"
                "</strong> Muster wird häufig mit SLE assoziiert, ein <strong>gesprenkeltes (speckled)</strong> Muster "
                "mit dem Sjögren-Syndrom und Mischkollagenosen, ein <strong>nukleoläres</strong> Muster mit "
                "Sklerodermie und ein <strong>Zentromer-</strong>Muster mit der limitierten Sklerodermie "
                "(CREST-Syndrom).</p>"
                "<p>Nicht jeder mit einem <strong>positiven ANA</strong>-Befund hat eine Autoimmunerkrankung. "
                "Falsch-positive Ergebnisse können bei älteren Menschen, bestimmten Infektionen und unter bestimmten "
                "Medikamenten auftreten. Daher müssen ANA-Testergebnisse stets zusammen mit klinischen Befunden und "
                "ergänzenden Laboruntersuchungen interpretiert werden.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für einen positiven ANA-Befund",
            body_html=(
                "<p>Ein <strong>positiver ANA</strong>-Befund kann in vielen unterschiedlichen Situationen auftreten. "
                "Die Bedeutung eines positiven ANA ist nicht immer eine Autoimmunerkrankung&mdash;das Ergebnis muss "
                "im klinischen Kontext bewertet werden. Die häufigsten Ursachen sind:</p>"
                "<ul>"
                "<li><strong>Systemischer Lupus erythematodes (SLE):</strong> Die bekannteste Ursache für ANA-"
                "Positivität; über 95 % der SLE-Patienten sind ANA-positiv.</li>"
                "<li><strong>Sjögren-Syndrom:</strong> Diese durch Mund- und Augentrockenheit gekennzeichnete "
                "Autoimmunerkrankung geht häufig mit einem positiven ANA und einem gesprenkelten Muster einher.</li>"
                "<li><strong>Sklerodermie (systemische Sklerose):</strong> Diese Erkrankung verursacht eine Verhärtung "
                "der Haut und innerer Organe; nukleoläre oder Zentromer-Muster werden erwartet.</li>"
                "<li><strong>Rheumatoide Arthritis:</strong> ANA-Positivität wird bei einem Teil der Patienten mit "
                "dieser chronisch-entzündlichen Gelenkerkrankung beobachtet.</li>"
                "<li><strong>Medikamenten-induzierter Lupus:</strong> Medikamente wie Hydralazin, Procainamid und "
                "Isoniazid können eine vorübergehende ANA-Positivität auslösen.</li>"
                "<li><strong>Infektionen:</strong> Chronische Infektionen wie Hepatitis C und das Epstein-Barr-Virus "
                "können eine niedrig-titrige ANA-Positivität verursachen.</li>"
                "<li><strong>Gesunde Personen:</strong> Bei etwa 15&ndash;20 % der Allgemeinbevölkerung, insbesondere "
                "bei älteren Frauen, kann ein niedrig-titriger (1:40&ndash;1:80) positiver ANA ohne zugrunde liegende "
                "Erkrankung nachgewiesen werden.</li>"
                "</ul>"
                "<p>Um die Ursache der ANA-Positivität zu klären, kann Ihr Arzt spezifische Autoantikörper-Tests wie "
                "Anti-dsDNA, Anti-Smith, Anti-SSA/SSB und Anti-Scl-70 sowie ein Blutbild, BSG und CRP anordnen.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Ihr <strong>ANA-Bluttest</strong> positiv ausfällt, bewahren Sie Ruhe, suchen Sie aber einen "
                "Rheumatologen auf&mdash;insbesondere bei einem Titer von 1:160 oder höher oder wenn Symptome wie "
                "Gelenkschmerzen, Hautausschläge, Mund- oder Augentrockenheit, unerklärliches Fieber oder "
                "Haarausfall auftreten.</p>"
                "<p>Da eine niedrig-titrige ANA-Positivität auch bei gesunden Personen vorkommen kann, bestätigt ein "
                "positiver ANA allein keine Autoimmundiagnose. Ihr Arzt wird eine klinische Untersuchung durchführen, "
                "eine ausführliche Anamnese erheben und ergänzende Labortests anordnen. Eine frühe Diagnose ist "
                "entscheidend, um Organschäden durch Autoimmunerkrankungen zu verhindern.</p>"
                "<p>Denken Sie daran: <strong>ANA-Testergebnisse</strong> sind lediglich ein Screening-Instrument. "
                "Nicht jeder mit positivem Befund hat eine Autoimmunerkrankung, und ein negatives Ergebnis schließt "
                "eine solche nicht vollständig aus. Bei anhaltenden Symptomen sind regelmäßige Kontrollen und "
                "gegebenenfalls wiederholte Tests von großer Bedeutung.</p>"
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
            heading="Test ANA : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test ANA</strong> (anticorps antinucléaires) est un <strong>bilan sanguin auto-immun"
                "</strong> qui détecte les anticorps dirigés contre les noyaux de vos propres cellules. Le test ANA "
                "est l'un des outils de dépistage de première ligne des maladies auto-immunes telles que le lupus "
                "érythémateux systémique (LES), le syndrome de Sjögren, la sclérodermie et la polyarthrite "
                "rhumatoïde. Cependant, un résultat <strong>ANA positif</strong> ne confirme pas automatiquement une "
                "maladie auto-immune&mdash;environ 15 à 20 % des personnes en bonne santé sont positives à des "
                "titres faibles.</p>"
                "<p>Dans ce guide, nous expliquons comment interpréter vos <strong>résultats du test ANA</strong>, "
                "la signification clinique des <strong>titres d'ANA</strong> et des patterns de fluorescence, et "
                "quand consulter un médecin. Ces informations sont à visée éducative&mdash;consultez toujours un "
                "rhumatologue pour un diagnostic approprié.</p>"
                "<p>Un test ANA est généralement prescrit lorsqu'un patient présente des douleurs articulaires, des "
                "éruptions cutanées, une fatigue inexpliquée ou une fièvre récurrente évocatrices d'une maladie "
                "auto-immune. Le test est réalisé par immunofluorescence indirecte (IFI) et rapporte à la fois le "
                "titre et le pattern de fluorescence.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Comment interpréter les résultats du test ANA ?",
            body_html=(
                "<p>Les <strong>résultats du test ANA</strong> sont évalués selon deux composantes : le titre (rapport "
                "de dilution) et le pattern de fluorescence. Plus le <strong>titre d'ANA</strong> est élevé, plus la "
                "probabilité d'une maladie auto-immune augmente, mais le titre seul ne pose pas de diagnostic. Le "
                "tableau ci-dessous résume l'interprétation clinique générale :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Titre d\'ANA</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interprétation</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Faiblement positif ; fréquent chez les personnes en bonne santé, signification clinique généralement limitée</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positif limite ; à évaluer dans le contexte des symptômes</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positif modéré ; probabilité accrue de maladie auto-immune</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 et plus</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positif élevé ; forte association avec une maladie auto-immune, investigation complémentaire requise</td></tr>'
                "</tbody></table>"
                "<p>Le pattern de fluorescence oriente également le diagnostic. Un pattern <strong>homogène (diffus)"
                "</strong> est fréquemment associé au LES, un pattern <strong>moucheté (speckled)</strong> au syndrome "
                "de Sjögren et aux connectivites mixtes, un pattern <strong>nucléolaire</strong> à la sclérodermie et "
                "un pattern <strong>centromère</strong> à la sclérodermie limitée (syndrome CREST).</p>"
                "<p>Toutes les personnes ayant un <strong>ANA positif</strong> ne souffrent pas d'une maladie "
                "auto-immune. Les faux positifs peuvent survenir chez les personnes âgées, lors de certaines "
                "infections et avec certains médicaments. Les résultats du test ANA doivent donc toujours être "
                "interprétés en parallèle des données cliniques et de tests biologiques complémentaires.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un résultat ANA positif",
            body_html=(
                "<p>Un résultat <strong>ANA positif</strong> peut apparaître dans de nombreuses situations. La "
                "signification d'un ANA positif n'est pas toujours une maladie auto-immune&mdash;le résultat doit "
                "être évalué dans son contexte clinique. Les causes les plus fréquentes sont :</p>"
                "<ul>"
                "<li><strong>Lupus érythémateux systémique (LES) :</strong> La cause la plus connue de positivité "
                "ANA ; plus de 95 % des patients atteints de LES sont ANA positifs.</li>"
                "<li><strong>Syndrome de Sjögren :</strong> Cette maladie auto-immune caractérisée par une sécheresse "
                "buccale et oculaire produit fréquemment un ANA positif avec un pattern moucheté.</li>"
                "<li><strong>Sclérodermie (sclérose systémique) :</strong> Cette maladie provoque un durcissement de "
                "la peau et des organes internes ; on attend des patterns nucléolaire ou centromère.</li>"
                "<li><strong>Polyarthrite rhumatoïde :</strong> La positivité ANA est observée chez une proportion "
                "de patients atteints de cette maladie inflammatoire articulaire chronique.</li>"
                "<li><strong>Lupus médicamenteux :</strong> Des médicaments tels que l'hydralazine, le procaïnamide "
                "et l'isoniazide peuvent provoquer une positivité ANA transitoire.</li>"
                "<li><strong>Infections :</strong> Des infections chroniques comme l'hépatite C et le virus "
                "d'Epstein-Barr peuvent produire une positivité ANA à titres faibles.</li>"
                "<li><strong>Personnes en bonne santé :</strong> Environ 15 à 20 % de la population générale, "
                "en particulier les femmes âgées, peuvent être ANA positives à des titres faibles (1:40&ndash;1:80) "
                "sans aucune maladie sous-jacente.</li>"
                "</ul>"
                "<p>Pour déterminer la cause de la positivité ANA, votre médecin peut prescrire des tests "
                "d'auto-anticorps spécifiques tels que anti-ADNdb, anti-Smith, anti-SSA/SSB et anti-Scl-70, ainsi "
                "qu'un hémogramme complet, une VS et une CRP.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si votre <strong>test ANA</strong> est positif, ne paniquez pas, mais consultez un rhumatologue, "
                "surtout si le titre est de 1:160 ou plus, ou si vous présentez des symptômes tels que des douleurs "
                "articulaires, des éruptions cutanées, une sécheresse buccale ou oculaire, une fièvre inexpliquée ou "
                "une chute de cheveux.</p>"
                "<p>La positivité ANA à titres faibles pouvant également survenir chez des personnes en bonne santé, "
                "un ANA positif seul ne confirme pas un diagnostic auto-immun. Votre médecin effectuera un examen "
                "clinique, recueillera un historique détaillé et prescrira des analyses complémentaires. Un diagnostic "
                "précoce est essentiel pour prévenir les atteintes d'organes liées aux maladies auto-immunes.</p>"
                "<p>N'oubliez pas : les <strong>résultats du test ANA</strong> ne sont qu'un outil de dépistage. "
                "Toutes les personnes positives n'ont pas de maladie auto-immune, et un résultat négatif ne l'exclut "
                "pas totalement. Si vos symptômes persistent, un suivi régulier et des tests répétés le cas échéant "
                "sont indispensables.</p>"
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
            heading="Test ANA: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test ANA</strong> (anticorpi antinucleo) è un <strong>esame del sangue autoimmune"
                "</strong> che rileva la presenza di anticorpi diretti contro i nuclei delle proprie cellule. "
                "Il test ANA è uno dei principali strumenti di screening per malattie autoimmuni come il lupus "
                "eritematoso sistemico (LES), la sindrome di Sjögren, la sclerodermia e l'artrite reumatoide. "
                "Tuttavia, un risultato <strong>ANA positivo</strong> non conferma automaticamente una malattia "
                "autoimmune&mdash;circa il 15&ndash;20 % delle persone sane risulta positivo a titoli bassi.</p>"
                "<p>In questa guida spieghiamo come interpretare i <strong>risultati del test ANA</strong>, il "
                "significato clinico dei <strong>titoli ANA</strong> e dei pattern di fluorescenza e quando "
                "rivolgersi al medico. Le informazioni qui contenute hanno scopo educativo&mdash;per una diagnosi "
                "adeguata consultate sempre un reumatologo.</p>"
                "<p>Il test ANA viene generalmente richiesto quando un paziente presenta dolori articolari, eruzioni "
                "cutanee, stanchezza inspiegabile o febbre ricorrente suggestivi di una malattia autoimmune. "
                "L'esame si esegue mediante immunofluorescenza indiretta (IFI) e riporta sia il titolo sia il "
                "pattern di fluorescenza.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Come interpretare i risultati del test ANA",
            body_html=(
                "<p>I <strong>risultati del test ANA</strong> vengono valutati in base a due componenti: il titolo "
                "(rapporto di diluizione) e il pattern di fluorescenza. Più alto è il <strong>titolo ANA</strong>, "
                "maggiore è la probabilità di una malattia autoimmune, ma il titolo da solo non consente di porre "
                "diagnosi. La tabella seguente riassume l'interpretazione clinica generale:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Titolo ANA</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretazione</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Basso positivo; frequente nei soggetti sani, significato clinico generalmente limitato</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo borderline; da valutare nel contesto dei sintomi</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo moderato; aumentata probabilità di malattia autoimmune</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 e oltre</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto positivo; forte associazione con malattia autoimmune, necessari ulteriori accertamenti</td></tr>'
                "</tbody></table>"
                "<p>Anche il pattern di fluorescenza orienta la diagnosi. Un pattern <strong>omogeneo (diffuso)"
                "</strong> è frequentemente associato al LES, un pattern <strong>punteggiato (speckled)</strong> "
                "alla sindrome di Sjögren e alla connettivite mista, un pattern <strong>nucleolare</strong> alla "
                "sclerodermia e un pattern <strong>centromerica</strong> alla sclerodermia limitata (sindrome "
                "CREST).</p>"
                "<p>Non tutti coloro che hanno un <strong>ANA positivo</strong> soffrono di una malattia autoimmune. "
                "I falsi positivi possono verificarsi nelle persone anziane, durante alcune infezioni e con alcuni "
                "farmaci. Pertanto, i risultati del test ANA devono essere sempre interpretati insieme ai dati "
                "clinici e ad esami di laboratorio aggiuntivi.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di un risultato ANA positivo",
            body_html=(
                "<p>Un risultato <strong>ANA positivo</strong> può presentarsi in molte situazioni diverse. Il "
                "significato di un ANA positivo non è sempre una malattia autoimmune; il risultato va valutato nel "
                "contesto clinico. Le cause più comuni includono:</p>"
                "<ul>"
                "<li><strong>Lupus eritematoso sistemico (LES):</strong> La causa più nota di positività ANA; oltre "
                "il 95 % dei pazienti con LES risulta ANA positivo.</li>"
                "<li><strong>Sindrome di Sjögren:</strong> Questa malattia autoimmune caratterizzata da secchezza "
                "orale e oculare produce frequentemente un ANA positivo con pattern punteggiato.</li>"
                "<li><strong>Sclerodermia (sclerosi sistemica):</strong> Questa patologia causa indurimento della "
                "pelle e degli organi interni; si attendono pattern nucleolare o centromerica.</li>"
                "<li><strong>Artrite reumatoide:</strong> La positività ANA si osserva in una proporzione di pazienti "
                "con questa malattia infiammatoria articolare cronica.</li>"
                "<li><strong>Lupus da farmaci:</strong> Farmaci come idralazina, procainamide e isoniazide possono "
                "causare una positività ANA transitoria.</li>"
                "<li><strong>Infezioni:</strong> Infezioni croniche come l'epatite C e il virus di Epstein-Barr "
                "possono produrre una positività ANA a titoli bassi.</li>"
                "<li><strong>Soggetti sani:</strong> Circa il 15&ndash;20 % della popolazione generale, in "
                "particolare le donne anziane, può risultare ANA positivo a titoli bassi (1:40&ndash;1:80) senza "
                "alcuna malattia sottostante.</li>"
                "</ul>"
                "<p>Per determinare la causa della positività ANA, il medico può richiedere test autoanticorpali "
                "specifici come anti-dsDNA, anti-Smith, anti-SSA/SSB e anti-Scl-70, oltre a emocromo completo, "
                "VES e PCR.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se il risultato del <strong>test ANA nel sangue</strong> è positivo, non allarmatevi, ma "
                "rivolgetevi a un reumatologo, soprattutto se il titolo è pari o superiore a 1:160 o se presentate "
                "sintomi come dolori articolari, eruzioni cutanee, secchezza orale o oculare, febbre inspiegabile "
                "o perdita di capelli.</p>"
                "<p>Poiché la positività ANA a titoli bassi può verificarsi anche in soggetti sani, un ANA positivo "
                "da solo non conferma una diagnosi autoimmune. Il medico eseguirà un esame clinico, raccoglierà "
                "un'anamnesi dettagliata e prescriverà esami di laboratorio aggiuntivi. La diagnosi precoce è "
                "fondamentale per prevenire il danno d'organo legato alle malattie autoimmuni.</p>"
                "<p>Ricordate: i <strong>risultati del test ANA</strong> sono solo uno strumento di screening. Non "
                "tutti coloro che risultano positivi hanno una malattia autoimmune e un risultato negativo non la "
                "esclude completamente. Se i sintomi persistono, il monitoraggio regolare e la ripetizione dei test "
                "quando opportuno sono essenziali.</p>"
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
            heading="בדיקת ANA בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת ANA</strong> (נוגדנים אנטי-גרעיניים) היא <strong>בדיקת דם אוטואימונית</strong> "
                "המזהה נוגדנים המופנים נגד גרעיני התאים של הגוף עצמו. בדיקת ANA בדם היא אחד מכלי הסקירה "
                "הראשוניים למחלות אוטואימוניות כמו זאבת אדמנתית מערכתית (SLE), תסמונת שגרן, סקלרודרמה ודלקת "
                "מפרקים שגרונית. עם זאת, תוצאה <strong>ANA חיובית</strong> אינה מאשרת אוטומטית מחלה "
                "אוטואימונית&mdash;כ-15&ndash;20% מהאנשים הבריאים נמצאים חיוביים בטיטרים נמוכים.</p>"
                "<p>במדריך זה נסביר כיצד לפרש את <strong>תוצאות בדיקת ANA</strong>, מה המשמעות הקלינית של "
                "<strong>טיטרי ANA</strong> ודפוסי הצביעה ומתי לפנות לרופא. המידע כאן חינוכי בלבד&mdash;התייעצו "
                "תמיד עם ראומטולוג לאבחון מדויק.</p>"
                "<p>בדיקת ANA מוזמנת בדרך כלל כאשר מטופל מציג כאבי מפרקים, פריחות עור, עייפות בלתי מוסברת או "
                "חום חוזר המרמזים על מצב אוטואימוני. הבדיקה מתבצעת באמצעות אימונופלואורסצנציה עקיפה (IFA) "
                "ומדווחת הן את הטיטר והן את דפוס הצביעה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="כיצד לפרש תוצאות בדיקת ANA?",
            body_html=(
                "<p><strong>תוצאות בדיקת ANA</strong> מוערכות לפי שני מרכיבים: הטיטר (יחס דילול) ודפוס הצביעה. "
                "ככל ש<strong>טיטר ה-ANA</strong> גבוה יותר, כך עולה ההסתברות למחלה אוטואימונית, אך הטיטר לבדו "
                "אינו קובע אבחנה. הטבלה הבאה מסכמת את הפרשנות הקלינית הכללית:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טיטר ANA</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">פרשנות</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">חיובי נמוך; שכיח אצל אנשים בריאים, משמעות קלינית מוגבלת בדרך כלל</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">חיובי גבולי; יש להעריך בהקשר של תסמינים</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">חיובי בינוני; הסתברות מוגברת למחלה אוטואימונית</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 ומעלה</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">חיובי גבוה; קשר חזק עם מחלה אוטואימונית, נדרש בירור נוסף</td></tr>'
                "</tbody></table>"
                "<p>דפוס הצביעה גם מנחה את האבחנה. דפוס <strong>הומוגני (דיפוזי)</strong> קשור לעתים קרובות "
                "ל-SLE, דפוס <strong>מנוקד (speckled)</strong> לתסמונת שגרן ולמחלת רקמת חיבור מעורבת, דפוס "
                "<strong>נוקלאולרי</strong> לסקלרודרמה ודפוס <strong>צנטרומרי</strong> לסקלרודרמה מוגבלת (תסמונת "
                "CREST).</p>"
                "<p>לא כל מי שיש לו <strong>ANA חיובי</strong> סובל ממחלה אוטואימונית. תוצאות חיוביות כוזבות "
                "עלולות להופיע אצל קשישים, בזמן זיהומים מסוימים ועם תרופות מסוימות. לכן, תוצאות בדיקת ANA חייבות "
                "תמיד להתפרש לצד ממצאים קליניים ובדיקות מעבדה נוספות.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לתוצאת ANA חיובית",
            body_html=(
                "<p>תוצאת <strong>ANA חיובית</strong> יכולה להופיע במצבים שונים רבים. המשמעות של ANA חיובי אינה "
                "תמיד מחלה אוטואימונית; יש להעריך את התוצאה בהקשרה הקליני. הגורמים השכיחים ביותר כוללים:</p>"
                "<ul>"
                "<li><strong>זאבת אדמנתית מערכתית (SLE):</strong> הגורם הידוע ביותר לחיוביות ANA; מעל 95% "
                "מחולי SLE נמצאים ANA חיובי.</li>"
                "<li><strong>תסמונת שגרן:</strong> מחלה אוטואימונית זו המאופיינת ביובש בפה ובעיניים מייצרת "
                "לעתים קרובות ANA חיובי עם דפוס מנוקד.</li>"
                "<li><strong>סקלרודרמה (טרשת מערכתית):</strong> מחלה זו גורמת להתקשות של העור והאיברים "
                "הפנימיים; צפויים דפוסים נוקלאולריים או צנטרומריים.</li>"
                "<li><strong>דלקת מפרקים שגרונית:</strong> חיוביות ANA נצפית בחלק מהמטופלים עם מחלה דלקתית "
                "כרונית זו של המפרקים.</li>"
                "<li><strong>זאבת מושרית על ידי תרופות:</strong> תרופות כמו הידרלזין, פרוקאינאמיד ואיזוניאזיד "
                "עלולות לגרום לחיוביות ANA חולפת.</li>"
                "<li><strong>זיהומים:</strong> זיהומים כרוניים כמו הפטיטיס C ווירוס אפשטיין-בר עלולים לייצר "
                "חיוביות ANA בטיטרים נמוכים.</li>"
                "<li><strong>אנשים בריאים:</strong> כ-15&ndash;20% מהאוכלוסייה הכללית, בעיקר נשים מבוגרות, עשויים "
                "להימצא ANA חיובי בטיטרים נמוכים (1:40&ndash;1:80) ללא כל מחלה בסיסית.</li>"
                "</ul>"
                "<p>כדי לקבוע את הגורם לחיוביות ANA, הרופא עשוי להזמין בדיקות נוגדנים עצמיים ספציפיות כמו "
                "anti-dsDNA, anti-Smith, anti-SSA/SSB ו-anti-Scl-70, לצד ספירת דם מלאה, שקיעת דם ו-CRP.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם תוצאת <strong>בדיקת ANA בדם</strong> שלך חיובית, אל תיבהל, אך פנה לראומטולוג&mdash;במיוחד "
                "אם הטיטר הוא 1:160 ומעלה, או אם אתה חווה תסמינים כמו כאבי מפרקים, פריחות עור, יובש בפה או "
                "בעיניים, חום בלתי מוסבר או נשירת שיער.</p>"
                "<p>מכיוון שחיוביות ANA בטיטרים נמוכים יכולה להופיע גם אצל אנשים בריאים, ANA חיובי לבדו אינו "
                "מאשר אבחנה אוטואימונית. הרופא שלך יבצע בדיקה קלינית, ייקח אנמנזה מפורטת ויזמין בדיקות מעבדה "
                "נוספות. אבחון מוקדם חיוני למניעת נזק לאיברים ממחלות אוטואימוניות.</p>"
                "<p>זכרו: <strong>תוצאות בדיקת ANA</strong> הן רק כלי סקירה. לא כל מי שנמצא חיובי סובל ממחלה "
                "אוטואימונית, ותוצאה שלילית אינה שוללת אותה לחלוטין. אם התסמינים נמשכים, מעקב קבוע ובדיקות "
                "חוזרות בעת הצורך הם חיוניים.</p>"
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
            heading="ANA ब्लड टेस्ट: आपके रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>ANA टेस्ट</strong> (एंटीन्यूक्लियर एंटीबॉडी टेस्ट) एक <strong>ऑटोइम्यून ब्लड "
                "टेस्ट</strong> है जो आपकी अपनी कोशिकाओं के नाभिक (न्यूक्लियस) के विरुद्ध बनने वाले एंटीबॉडीज़ "
                "का पता लगाता है। ANA ब्लड टेस्ट सिस्टेमिक ल्यूपस एरिथेमेटोसस (SLE), शोग्रेन सिंड्रोम, "
                "स्क्लेरोडर्मा और रुमेटॉइड आर्थराइटिस जैसी ऑटोइम्यून बीमारियों की स्क्रीनिंग के लिए सबसे अधिक "
                "उपयोग किए जाने वाले परीक्षणों में से एक है। हालांकि, <strong>ANA पॉज़िटिव</strong> रिज़ल्ट का "
                "मतलब हमेशा ऑटोइम्यून बीमारी नहीं होता&mdash;लगभग 15&ndash;20% स्वस्थ लोगों में कम टाइटर पर "
                "पॉज़िटिव रिज़ल्ट आ सकता है।</p>"
                "<p>इस गाइड में हम बताएंगे कि <strong>ANA टेस्ट रिज़ल्ट</strong> की व्याख्या कैसे करें, "
                "<strong>ANA टाइटर</strong> और स्टेनिंग पैटर्न का क्लिनिकल महत्व क्या है और डॉक्टर से कब मिलना "
                "चाहिए। यहाँ दी गई जानकारी शैक्षिक उद्देश्य से है&mdash;सही निदान के लिए हमेशा रुमेटोलॉजिस्ट "
                "से परामर्श करें।</p>"
                "<p>ANA ब्लड टेस्ट आमतौर पर तब किया जाता है जब किसी मरीज़ में जोड़ों का दर्द, त्वचा पर "
                "चकत्ते, अस्पष्ट थकान या बार-बार बुखार जैसे ऑटोइम्यून बीमारी के लक्षण दिखाई देते हैं। यह "
                "टेस्ट इनडायरेक्ट इम्यूनोफ्लोरेसेंस (IFA) विधि से किया जाता है और टाइटर तथा स्टेनिंग पैटर्न "
                "दोनों की रिपोर्ट देता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ANA टेस्ट रिज़ल्ट की व्याख्या कैसे करें?",
            body_html=(
                "<p><strong>ANA टेस्ट रिज़ल्ट</strong> दो घटकों के आधार पर मूल्यांकित किए जाते हैं: टाइटर "
                "(डाइल्यूशन अनुपात) और स्टेनिंग पैटर्न। <strong>ANA टाइटर</strong> जितना अधिक होगा, ऑटोइम्यून "
                "बीमारी की संभावना उतनी ही बढ़ जाती है, लेकिन अकेले टाइटर से निदान नहीं होता। नीचे दी गई "
                "तालिका में ANA टाइटर की सामान्य क्लिनिकल व्याख्या दी गई है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">ANA टाइटर</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">व्याख्या</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">कम पॉज़िटिव; स्वस्थ लोगों में आम, क्लिनिकल महत्व आमतौर पर सीमित</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">बॉर्डरलाइन पॉज़िटिव; लक्षणों के संदर्भ में मूल्यांकन किया जाना चाहिए</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">मध्यम पॉज़िटिव; ऑटोइम्यून बीमारी की संभावना बढ़ जाती है</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 और उससे ऊपर</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">उच्च पॉज़िटिव; ऑटोइम्यून बीमारी से मज़बूत संबंध, आगे की जांच ज़रूरी</td></tr>'
                "</tbody></table>"
                "<p>स्टेनिंग पैटर्न भी निदान में मदद करता है। <strong>होमोजीनस (डिफ्यूज़)</strong> पैटर्न "
                "अक्सर SLE से, <strong>स्पेकल्ड</strong> पैटर्न शोग्रेन सिंड्रोम और मिक्स्ड कनेक्टिव टिशू "
                "डिज़ीज़ से, <strong>न्यूक्लियोलर</strong> पैटर्न स्क्लेरोडर्मा से और <strong>सेंट्रोमियर</strong> "
                "पैटर्न लिमिटेड स्क्लेरोडर्मा (CREST सिंड्रोम) से जुड़ा होता है।</p>"
                "<p>हर <strong>ANA पॉज़िटिव</strong> व्यक्ति को ऑटोइम्यून बीमारी नहीं होती। बुज़ुर्गों में, कुछ "
                "संक्रमणों के दौरान और कुछ दवाइयों से फ़ॉल्स पॉज़िटिव हो सकता है। इसलिए ANA टेस्ट रिज़ल्ट को "
                "हमेशा क्लिनिकल निष्कर्षों और अतिरिक्त लैब टेस्ट के साथ समझना चाहिए।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="ANA पॉज़िटिव होने के कारण",
            body_html=(
                "<p><strong>ANA पॉज़िटिव</strong> रिज़ल्ट कई अलग-अलग स्थितियों में आ सकता है। <strong>पॉज़िटिव "
                "ANA का मतलब</strong> हमेशा ऑटोइम्यून बीमारी नहीं होता; रिज़ल्ट को क्लिनिकल संदर्भ में "
                "मूल्यांकित किया जाना चाहिए। सबसे आम कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>सिस्टेमिक ल्यूपस एरिथेमेटोसस (SLE):</strong> ANA पॉज़िटिविटी का सबसे प्रसिद्ध "
                "कारण; 95% से अधिक SLE रोगी ANA पॉज़िटिव होते हैं।</li>"
                "<li><strong>शोग्रेन सिंड्रोम:</strong> मुंह और आंखों की सूखापन वाली यह ऑटोइम्यून बीमारी "
                "अक्सर स्पेकल्ड पैटर्न के साथ ANA पॉज़िटिव देती है।</li>"
                "<li><strong>स्क्लेरोडर्मा (सिस्टेमिक स्क्लेरोसिस):</strong> यह बीमारी त्वचा और आंतरिक अंगों "
                "को कठोर बनाती है; न्यूक्लियोलर या सेंट्रोमियर पैटर्न अपेक्षित है।</li>"
                "<li><strong>रुमेटॉइड आर्थराइटिस:</strong> इस क्रोनिक जोड़ों की सूजन वाली बीमारी के कुछ "
                "रोगियों में ANA पॉज़िटिविटी देखी जाती है।</li>"
                "<li><strong>दवा-प्रेरित ल्यूपस:</strong> हाइड्रैलेज़ीन, प्रोकेनामाइड और आइसोनियाज़िड जैसी "
                "दवाइयां अस्थायी ANA पॉज़िटिविटी पैदा कर सकती हैं।</li>"
                "<li><strong>संक्रमण:</strong> हेपेटाइटिस C और एपस्टीन-बार वायरस जैसे क्रोनिक संक्रमण कम "
                "टाइटर पर ANA पॉज़िटिविटी दे सकते हैं।</li>"
                "<li><strong>स्वस्थ व्यक्ति:</strong> सामान्य आबादी का लगभग 15&ndash;20%, विशेषकर वृद्ध महिलाएं, "
                "कम टाइटर (1:40&ndash;1:80) पर बिना किसी बीमारी के ANA पॉज़िटिव हो सकती हैं।</li>"
                "</ul>"
                "<p>ANA पॉज़िटिविटी का कारण निर्धारित करने के लिए डॉक्टर anti-dsDNA, anti-Smith, anti-SSA/SSB "
                "और anti-Scl-70 जैसे विशिष्ट ऑटोएंटीबॉडी टेस्ट के साथ CBC, ESR और CRP करवा सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपके <strong>ANA ब्लड टेस्ट</strong> का रिज़ल्ट पॉज़िटिव आता है तो घबराएं नहीं, लेकिन "
                "रुमेटोलॉजिस्ट से ज़रूर मिलें&mdash;विशेषकर अगर टाइटर 1:160 या उससे अधिक है, या अगर आपको "
                "जोड़ों का दर्द, त्वचा पर चकत्ते, मुंह या आंखों का सूखापन, अस्पष्ट बुखार या बाल झड़ने जैसे "
                "लक्षण हैं।</p>"
                "<p>चूंकि कम टाइटर पर ANA पॉज़िटिविटी स्वस्थ व्यक्तियों में भी हो सकती है, अकेले ANA पॉज़िटिव "
                "रिज़ल्ट ऑटोइम्यून निदान की पुष्टि नहीं करता। डॉक्टर क्लिनिकल जांच, विस्तृत इतिहास और "
                "अतिरिक्त लैब टेस्ट से स्थिति का मूल्यांकन करेंगे। ऑटोइम्यून बीमारियों में ऑर्गन डैमेज "
                "को रोकने के लिए शुरुआती निदान बेहद ज़रूरी है।</p>"
                "<p>याद रखें: <strong>ANA टेस्ट रिज़ल्ट</strong> केवल एक स्क्रीनिंग टूल है। पॉज़िटिव आने वाले "
                "हर व्यक्ति को ऑटोइम्यून बीमारी नहीं होती, और नेगेटिव रिज़ल्ट इसे पूरी तरह ख़ारिज नहीं करता। "
                "अगर लक्षण बने रहते हैं तो नियमित फ़ॉलो-अप और ज़रूरत पड़ने पर दोबारा टेस्ट करवाना बहुत "
                "ज़रूरी है।</p>"
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
            heading="تحليل ANA في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p><strong>تحليل ANA</strong> (الأجسام المضادة للنواة) هو <strong>فحص دم مناعي ذاتي</strong> "
                "يكشف عن وجود أجسام مضادة موجهة ضد نوى خلايا الجسم نفسه. يُعد تحليل ANA في الدم أحد أهم أدوات "
                "الفحص الأولية للأمراض المناعية الذاتية مثل الذئبة الحمراء الجهازية (SLE) ومتلازمة شوغرن وتصلب "
                "الجلد والتهاب المفاصل الروماتويدي. إلا أن نتيجة <strong>ANA إيجابية</strong> لا تؤكد تلقائياً "
                "وجود مرض مناعي ذاتي&mdash;فنحو 15&ndash;20% من الأشخاص الأصحاء يظهرون إيجابية عند عيارات "
                "منخفضة.</p>"
                "<p>في هذا الدليل نشرح كيفية تفسير <strong>نتائج تحليل ANA</strong>، والأهمية السريرية "
                "لـ<strong>عيار ANA</strong> وأنماط التلوين، ومتى يجب مراجعة الطبيب. المعلومات هنا تثقيفية "
                "بحتة&mdash;استشر دائماً طبيب أمراض الروماتيزم للحصول على تشخيص دقيق.</p>"
                "<p>يُطلب تحليل ANA عادةً عندما يعاني المريض من آلام المفاصل أو طفح جلدي أو إرهاق غير مفسّر "
                "أو حمى متكررة تشير إلى حالة مناعية ذاتية. يتم إجراء الفحص بطريقة التألق المناعي غير المباشر "
                "(IFA) ويُبلَّغ عن كل من العيار ونمط التلوين.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="كيف تُفسَّر نتائج تحليل ANA؟",
            body_html=(
                "<p>تُقيَّم <strong>نتائج تحليل ANA</strong> وفقاً لعنصرين: العيار (نسبة التخفيف) ونمط التلوين. "
                "كلما ارتفع <strong>عيار ANA</strong>، زادت احتمالية وجود مرض مناعي ذاتي، لكن العيار وحده لا "
                "يُشخِّص المرض. يلخص الجدول التالي التفسير السريري العام:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">عيار ANA</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">التفسير</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:40</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">إيجابي منخفض؛ شائع لدى الأصحاء، أهمية سريرية محدودة عادةً</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:80</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">إيجابي حدّي؛ يجب تقييمه في سياق الأعراض</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:160</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">إيجابي متوسط؛ احتمالية متزايدة لمرض مناعي ذاتي</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">1:320 وأعلى</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">إيجابي مرتفع؛ ارتباط قوي بمرض مناعي ذاتي، يتطلب فحوصات إضافية</td></tr>'
                "</tbody></table>"
                "<p>يوجّه نمط التلوين أيضاً نحو التشخيص. النمط <strong>المتجانس (المنتشر)</strong> يرتبط غالباً "
                "بالذئبة الحمراء، والنمط <strong>المنقّط (speckled)</strong> بمتلازمة شوغرن ومرض النسيج الضام "
                "المختلط، والنمط <strong>النُوَيْوي (nucleolar)</strong> بتصلب الجلد، ونمط <strong>القُسيم المركزي "
                "(centromere)</strong> بتصلب الجلد المحدود (متلازمة CREST).</p>"
                "<p>ليس كل من لديه <strong>ANA إيجابي</strong> مصاباً بمرض مناعي ذاتي. يمكن أن تحدث نتائج إيجابية "
                "كاذبة لدى كبار السن وأثناء بعض العدوى ومع بعض الأدوية. لذلك يجب دائماً تفسير نتائج تحليل ANA "
                "إلى جانب المعطيات السريرية والفحوصات المخبرية الإضافية.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب نتيجة ANA إيجابية",
            body_html=(
                "<p>يمكن أن تظهر نتيجة <strong>ANA إيجابية</strong> في حالات عديدة مختلفة. معنى ANA الإيجابي "
                "ليس دائماً مرضاً مناعياً ذاتياً؛ يجب تقييم النتيجة في سياقها السريري. تشمل الأسباب الأكثر "
                "شيوعاً:</p>"
                "<ul>"
                "<li><strong>الذئبة الحمراء الجهازية (SLE):</strong> السبب الأشهر لإيجابية ANA؛ أكثر من 95% من "
                "مرضى SLE يكونون ANA إيجابيين.</li>"
                "<li><strong>متلازمة شوغرن:</strong> هذا المرض المناعي الذاتي المميز بجفاف الفم والعينين ينتج "
                "غالباً ANA إيجابياً بنمط منقّط.</li>"
                "<li><strong>تصلب الجلد (التصلب الجهازي):</strong> يسبب هذا المرض تصلب الجلد والأعضاء الداخلية؛ "
                "يُتوقع نمط نُوَيوي أو نمط قُسيم مركزي.</li>"
                "<li><strong>التهاب المفاصل الروماتويدي:</strong> تُلاحَظ إيجابية ANA لدى نسبة من المرضى المصابين "
                "بهذا المرض الالتهابي المزمن للمفاصل.</li>"
                "<li><strong>الذئبة الناتجة عن الأدوية:</strong> أدوية مثل الهيدرالازين والبروكاييناميد "
                "والأيزونيازيد قد تسبب إيجابية ANA مؤقتة.</li>"
                "<li><strong>العدوى:</strong> العدوى المزمنة مثل التهاب الكبد C وفيروس إبشتاين بار قد تنتج "
                "إيجابية ANA عند عيارات منخفضة.</li>"
                "<li><strong>الأشخاص الأصحاء:</strong> نحو 15&ndash;20% من عموم السكان، خصوصاً النساء الأكبر "
                "سناً، قد يظهرون إيجابية ANA عند عيارات منخفضة (1:40&ndash;1:80) دون أي مرض كامن.</li>"
                "</ul>"
                "<p>لتحديد سبب إيجابية ANA، قد يطلب الطبيب فحوصات أجسام مضادة ذاتية محددة مثل anti-dsDNA "
                "وanti-Smith وanti-SSA/SSB وanti-Scl-70، بالإضافة إلى تعداد دم كامل وسرعة ترسيب و-CRP.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كانت نتيجة <strong>تحليل ANA في الدم</strong> إيجابية، فلا تقلق لكن راجع طبيب أمراض "
                "الروماتيزم&mdash;خصوصاً إذا كان العيار 1:160 أو أعلى، أو إذا كنت تعاني من أعراض مثل آلام "
                "المفاصل أو طفح جلدي أو جفاف الفم أو العينين أو حمى غير مفسّرة أو تساقط الشعر.</p>"
                "<p>نظراً لأن إيجابية ANA عند عيارات منخفضة قد تحدث أيضاً لدى أشخاص أصحاء، فإن ANA الإيجابي "
                "وحده لا يؤكد تشخيص مرض مناعي ذاتي. سيُجري طبيبك فحصاً سريرياً ويأخذ تاريخاً مرضياً مفصلاً "
                "ويطلب فحوصات مخبرية إضافية. التشخيص المبكر ضروري لمنع تلف الأعضاء الناجم عن الأمراض المناعية "
                "الذاتية.</p>"
                "<p>تذكّر: <strong>نتائج تحليل ANA</strong> ليست سوى أداة فحص أولية. ليس كل من تظهر نتيجته "
                "إيجابية مصاباً بمرض مناعي ذاتي، والنتيجة السلبية لا تستبعده تماماً. إذا استمرت أعراضك، فإن "
                "المتابعة المنتظمة وإعادة الفحص عند الحاجة أمران أساسيان.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_ana_sections_by_lang() -> dict:
    """Returns sections dict for ANA article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_ana_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for ANA article (all 9 languages)."""
    return {
        "tr": [
            {"question": "ANA testi nedir?",
             "answer": "ANA testi (antinükleer antikor testi), bağışıklık sisteminin vücudun kendi hücre çekirdeklerine karşı antikor üretip üretmediğini ölçen bir otoimmün kan testidir. Lupus, Sjögren sendromu ve skleroderma gibi otoimmün hastalıkların taranmasında kullanılır."},
            {"question": "ANA pozitif çıkması ne anlama gelir?",
             "answer": "ANA pozitifliği otoimmün bir hastalığa işaret edebilir, ancak sağlıklı bireylerin %15-20'sinde de düşük titrede pozitiflik görülebilir. Tek başına ANA pozitifliği kesin tanı koymaz; sonuç, klinik bulgular ve ek testlerle birlikte değerlendirilmelidir."},
            {"question": "ANA titresi ne anlama gelir?",
             "answer": "ANA titresi, kandaki antinükleer antikorların konsantrasyonunu gösterir. 1:40 düşük pozitiflik, 1:80 sınırda, 1:160 orta ve 1:320 üzeri yüksek pozitiflik olarak yorumlanır. Yüksek titre otoimmün hastalık olasılığını artırır."},
        ],
        "en": [
            {"question": "What is an ANA test?",
             "answer": "An ANA test (antinuclear antibody test) is an autoimmune blood test that detects antibodies directed against the nuclei of your own cells. It is used to screen for autoimmune diseases such as lupus, Sjögren's syndrome, and scleroderma."},
            {"question": "What does a positive ANA mean?",
             "answer": "A positive ANA may indicate an autoimmune disease, but approximately 15–20% of healthy individuals also test positive at low titers. A positive ANA alone does not confirm a diagnosis; it must be evaluated alongside clinical findings and additional tests."},
            {"question": "What do ANA titers mean?",
             "answer": "ANA titers reflect the concentration of antinuclear antibodies in the blood. A titer of 1:40 is low positive, 1:80 is borderline, 1:160 is moderate, and 1:320 or above is high positive. Higher titers increase the likelihood of autoimmune disease."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de ANA?",
             "answer": "La prueba de ANA (anticuerpos antinucleares) es un análisis de sangre autoinmune que detecta anticuerpos dirigidos contra los núcleos de las propias células. Se utiliza para el cribado de enfermedades autoinmunes como el lupus, el síndrome de Sjögren y la esclerodermia."},
            {"question": "¿Qué significa un ANA positivo?",
             "answer": "Un ANA positivo puede indicar una enfermedad autoinmune, pero aproximadamente el 15–20 % de las personas sanas también da positivo a títulos bajos. Un ANA positivo por sí solo no confirma un diagnóstico; debe evaluarse junto con los hallazgos clínicos y pruebas adicionales."},
            {"question": "¿Qué significan los títulos de ANA?",
             "answer": "Los títulos de ANA reflejan la concentración de anticuerpos antinucleares en la sangre. Un título de 1:40 es positivo bajo, 1:80 es limítrofe, 1:160 es moderado y 1:320 o superior es positivo alto. Títulos más altos aumentan la probabilidad de enfermedad autoinmune."},
        ],
        "de": [
            {"question": "Was ist ein ANA-Test?",
             "answer": "Der ANA-Test (Antinukleäre-Antikörper-Test) ist ein Autoimmun-Bluttest, der Antikörper gegen die Zellkerne des eigenen Körpers nachweist. Er wird zum Screening auf Autoimmunerkrankungen wie Lupus, Sjögren-Syndrom und Sklerodermie eingesetzt."},
            {"question": "Was bedeutet ein positiver ANA-Befund?",
             "answer": "Ein positiver ANA kann auf eine Autoimmunerkrankung hinweisen, aber etwa 15–20 % der gesunden Personen sind bei niedrigen Titern ebenfalls positiv. Ein positiver ANA allein bestätigt keine Diagnose; er muss zusammen mit klinischen Befunden und weiteren Tests bewertet werden."},
            {"question": "Was bedeuten ANA-Titer?",
             "answer": "ANA-Titer spiegeln die Konzentration antinukleärer Antikörper im Blut wider. Ein Titer von 1:40 gilt als niedrig positiv, 1:80 als grenzwertig, 1:160 als mäßig und 1:320 oder höher als hoch positiv. Höhere Titer erhöhen die Wahrscheinlichkeit einer Autoimmunerkrankung."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test ANA ?",
             "answer": "Le test ANA (anticorps antinucléaires) est un bilan sanguin auto-immun qui détecte les anticorps dirigés contre les noyaux de vos propres cellules. Il est utilisé pour le dépistage des maladies auto-immunes telles que le lupus, le syndrome de Sjögren et la sclérodermie."},
            {"question": "Que signifie un ANA positif ?",
             "answer": "Un ANA positif peut indiquer une maladie auto-immune, mais environ 15 à 20 % des personnes en bonne santé sont également positives à des titres faibles. Un ANA positif seul ne confirme pas un diagnostic ; il doit être évalué avec les données cliniques et des tests complémentaires."},
            {"question": "Que signifient les titres d'ANA ?",
             "answer": "Les titres d'ANA reflètent la concentration des anticorps antinucléaires dans le sang. Un titre de 1:40 est faiblement positif, 1:80 est limite, 1:160 est modéré et 1:320 ou plus est fortement positif. Des titres plus élevés augmentent la probabilité d'une maladie auto-immune."},
        ],
        "it": [
            {"question": "Cos'è il test ANA?",
             "answer": "Il test ANA (anticorpi antinucleo) è un esame del sangue autoimmune che rileva anticorpi diretti contro i nuclei delle proprie cellule. Viene utilizzato per lo screening di malattie autoimmuni come il lupus, la sindrome di Sjögren e la sclerodermia."},
            {"question": "Cosa significa un ANA positivo?",
             "answer": "Un ANA positivo può indicare una malattia autoimmune, ma circa il 15–20 % delle persone sane risulta positivo a titoli bassi. Un ANA positivo da solo non conferma una diagnosi; deve essere valutato insieme ai dati clinici e a esami aggiuntivi."},
            {"question": "Cosa significano i titoli ANA?",
             "answer": "I titoli ANA riflettono la concentrazione di anticorpi antinucleo nel sangue. Un titolo di 1:40 è basso positivo, 1:80 è borderline, 1:160 è moderato e 1:320 o superiore è alto positivo. Titoli più alti aumentano la probabilità di malattia autoimmune."},
        ],
        "he": [
            {"question": "מהי בדיקת ANA?",
             "answer": "בדיקת ANA (נוגדנים אנטי-גרעיניים) היא בדיקת דם אוטואימונית המזהה נוגדנים המופנים נגד גרעיני התאים של הגוף. היא משמשת לסקירה של מחלות אוטואימוניות כמו זאבת, תסמונת שגרן וסקלרודרמה."},
            {"question": "מה המשמעות של ANA חיובי?",
             "answer": "ANA חיובי עשוי להצביע על מחלה אוטואימונית, אך כ-15–20% מהאנשים הבריאים גם נמצאים חיוביים בטיטרים נמוכים. ANA חיובי לבדו אינו מאשר אבחנה; יש לפרשו לצד ממצאים קליניים ובדיקות נוספות."},
            {"question": "מה המשמעות של טיטרי ANA?",
             "answer": "טיטרי ANA משקפים את ריכוז הנוגדנים האנטי-גרעיניים בדם. טיטר של 1:40 הוא חיובי נמוך, 1:80 גבולי, 1:160 בינוני ו-1:320 ומעלה חיובי גבוה. טיטרים גבוהים יותר מגבירים את ההסתברות למחלה אוטואימונית."},
        ],
        "hi": [
            {"question": "ANA टेस्ट क्या है?",
             "answer": "ANA टेस्ट (एंटीन्यूक्लियर एंटीबॉडी टेस्ट) एक ऑटोइम्यून ब्लड टेस्ट है जो आपकी अपनी कोशिकाओं के नाभिक के विरुद्ध बनने वाले एंटीबॉडीज़ का पता लगाता है। इसका उपयोग ल्यूपस, शोग्रेन सिंड्रोम और स्क्लेरोडर्मा जैसी ऑटोइम्यून बीमारियों की स्क्रीनिंग के लिए किया जाता है।"},
            {"question": "ANA पॉज़िटिव होने का क्या मतलब है?",
             "answer": "ANA पॉज़िटिव ऑटोइम्यून बीमारी का संकेत हो सकता है, लेकिन लगभग 15–20% स्वस्थ लोगों में भी कम टाइटर पर पॉज़िटिव रिज़ल्ट आता है। अकेले ANA पॉज़िटिव निदान की पुष्टि नहीं करता; इसे क्लिनिकल निष्कर्षों और अतिरिक्त टेस्ट के साथ मूल्यांकित किया जाना चाहिए।"},
            {"question": "ANA टाइटर का क्या मतलब है?",
             "answer": "ANA टाइटर रक्त में एंटीन्यूक्लियर एंटीबॉडीज़ की सांद्रता को दर्शाता है। 1:40 टाइटर कम पॉज़िटिव, 1:80 बॉर्डरलाइन, 1:160 मध्यम और 1:320 या उससे ऊपर उच्च पॉज़िटिव माना जाता है। अधिक टाइटर ऑटोइम्यून बीमारी की संभावना बढ़ाता है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل ANA؟",
             "answer": "تحليل ANA (الأجسام المضادة للنواة) هو فحص دم مناعي ذاتي يكشف عن أجسام مضادة موجهة ضد نوى خلايا الجسم. يُستخدم لفحص الأمراض المناعية الذاتية مثل الذئبة الحمراء ومتلازمة شوغرن وتصلب الجلد."},
            {"question": "ماذا تعني نتيجة ANA إيجابية؟",
             "answer": "قد تشير نتيجة ANA الإيجابية إلى مرض مناعي ذاتي، لكن نحو 15–20% من الأصحاء يظهرون أيضاً إيجابية عند عيارات منخفضة. نتيجة ANA الإيجابية وحدها لا تؤكد التشخيص؛ يجب تقييمها مع المعطيات السريرية والفحوصات الإضافية."},
            {"question": "ماذا يعني عيار ANA؟",
             "answer": "يعكس عيار ANA تركيز الأجسام المضادة للنواة في الدم. عيار 1:40 إيجابي منخفض، 1:80 حدّي، 1:160 متوسط، و1:320 أو أعلى إيجابي مرتفع. العيارات الأعلى تزيد من احتمالية وجود مرض مناعي ذاتي."},
        ],
    }
