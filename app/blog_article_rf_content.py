# -*- coding: utf-8 -*-
"""
Rheumatoid Factor (RF) blog article — full body content for all 9 languages.
Used by blog_i18n._article_rf().
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
            heading="Romatoid faktör (RF) kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>Romatoid faktör (RF)</strong>, bağışıklık sistemi tarafından üretilen ve vücudun kendi "
                "sağlıklı dokularına saldırabilen bir <strong>otoantikordur</strong> (genellikle IgM sınıfı). "
                "<strong>RF kan testi</strong>, başta <strong>romatoid artrit</strong> olmak üzere çeşitli otoimmün "
                "ve enflamatuar hastalıkların tanı ve takibinde kullanılan önemli bir laboratuvar testidir. "
                "Ancak <strong>RF pozitif</strong> çıkması tek başına hastalık anlamına gelmez; sağlıklı bireylerin "
                "yaklaşık %5-10'unda, özellikle yaşlılarda, düşük düzeyde RF pozitifliği saptanabilir.</p>"
                "<p>Bu rehberde <strong>RF test</strong> sonuçlarının nasıl yorumlanacağını, <strong>RF normal "
                "değerleri</strong>ni, <strong>yüksek RF</strong> nedenlerini ve hangi durumlarda doktora "
                "başvurmanız gerektiğini ayrıntılı şekilde açıklıyoruz. Buradaki bilgiler eğitim amaçlıdır; "
                "kesin tanı ve tedavi için mutlaka bir romatoloji uzmanına danışın.</p>"
                "<p><strong>Romatoid artrit kan testi</strong> olarak da bilinen RF testi, genellikle eklem ağrısı, "
                "şişlik, sabah tutukluğu veya açıklanamayan yorgunluk şikâyetleri olan hastalara istenir. "
                "Test, nefelometri veya türbidimetri yöntemiyle kanınızdaki RF düzeyini IU/mL cinsinden ölçer "
                "ve sonuç anti-CCP (anti-siklik sitrüline peptit) gibi diğer otoantikor testleriyle birlikte "
                "değerlendirilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="RF normal değerleri",
            body_html=(
                "<p><strong>RF test sonuçları</strong> genellikle IU/mL (Uluslararası Birim/mililitre) cinsinden "
                "raporlanır. Çoğu laboratuvarda <strong>RF normal aralığı</strong> &lt;14 IU/mL (negatif) olarak "
                "kabul edilir, ancak referans değerler laboratuvardan laboratuvara küçük farklılıklar "
                "gösterebilir. Aşağıdaki tabloda genel RF değerlendirme sınıflaması özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">RF düzeyi (IU/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Yorum</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Negatif (normal)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Düşük pozitiflik; klinik bulgularla birlikte değerlendirilmeli</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Orta düzeyde pozitiflik; otoimmün hastalık olasılığı artar</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Yüksek pozitiflik; romatoid artrit veya diğer otoimmün hastalıklarla güçlü ilişki</td></tr>'
                "</tbody></table>"
                "<p><strong>Yüksek RF</strong> düzeyleri romatoid artrit ile güçlü bir şekilde ilişkilendirilse de, "
                "RF tek başına tanı koydurmaz. Romatoid artrit hastalarının yaklaşık %70-80'inde RF pozitif "
                "saptanırken, hastaların %20-30'unda RF negatif olabilir (serongatif romatoid artrit). "
                "Bu nedenle <strong>anti-CCP antikoru</strong> gibi daha spesifik testler tanıya katkı sağlar; "
                "anti-CCP, romatoid artrit için %95'in üzerinde özgüllüğe sahiptir.</p>"
                "<p>RF düzeyi yaşla birlikte doğal olarak artabilir. 65 yaş üzerindeki sağlıklı bireylerin "
                "%15-25'inde düşük düzeyde RF pozitifliği herhangi bir hastalık olmaksızın saptanabilir. "
                "Sonuçlarınızı mutlaka klinik bulgular, anti-CCP, CRP ve sedimentasyon gibi ek testlerle "
                "birlikte değerlendirin.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="RF pozitifliğinin nedenleri",
            body_html=(
                "<p><strong>Romatoid faktör pozitif</strong> sonucu birçok farklı durumda ortaya çıkabilir. "
                "<strong>Yüksek RF</strong> her zaman romatoid artrit anlamına gelmez; sonucun klinik bağlamda "
                "değerlendirilmesi gerekir. RF pozitifliğine neden olabilecek başlıca durumlar şunlardır:</p>"
                "<ul>"
                "<li><strong>Romatoid artrit (RA):</strong> RF pozitifliğinin en bilinen nedenidir; hastaların "
                "%70-80'inde pozitif saptanır. Yüksek RF düzeyleri daha agresif hastalık seyri ve eklem dışı "
                "tutulum ile ilişkilendirilir.</li>"
                "<li><strong>Sjögren sendromu:</strong> Ağız ve göz kuruluğu ile karakterize bu otoimmün hastalıkta "
                "RF hastaların %75-95'inde pozitiftir.</li>"
                "<li><strong>Mikst kriyoglobulinemi:</strong> Özellikle hepatit C ile ilişkili mikst "
                "kriyoglobulinemide RF yüksek düzeylerde saptanır.</li>"
                "<li><strong>Kronik enfeksiyonlar:</strong> Hepatit C (HCV), hepatit B, tüberküloz, "
                "enfektif endokardit ve kronik viral enfeksiyonlar düşük-orta düzeyde RF pozitifliğine "
                "neden olabilir.</li>"
                "<li><strong>Diğer otoimmün hastalıklar:</strong> Sistemik lupus eritematozus (SLE), "
                "skleroderma ve polimiyozit gibi hastalıklarda da RF pozitifliği görülebilir.</li>"
                "<li><strong>Yaşlanma:</strong> 65 yaş üzerindeki sağlıklı bireylerin %15-25'inde düşük "
                "düzeyde RF pozitifliği saptanabilir.</li>"
                "<li><strong>Sigara kullanımı:</strong> Kronik sigara içiciliği düşük düzeyde RF üretimini "
                "uyarabilir ve romatoid artrit riskini artırır.</li>"
                "</ul>"
                "<p>Doktorunuz RF pozitifliğinin nedenini belirlemek için <strong>anti-CCP</strong>, ANA, "
                "tam kan sayımı, CRP, sedimentasyon ve hepatit serolojisi gibi ek testler isteyebilir. "
                "Anti-CCP, romatoid artrit için RF'ye göre çok daha yüksek özgüllüğe sahiptir ve iki testin "
                "birlikte pozitif olması tanı olasılığını önemli ölçüde artırır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p><strong>RF kan testi</strong> sonucunuz pozitif çıktıysa panik yapmayın, ancak özellikle "
                "<strong>yüksek RF</strong> düzeyleri (&gt;50 IU/mL) varsa veya eklem ağrısı, sabah tutukluğu "
                "(30 dakikadan uzun süren), eklem şişliği, açıklanamayan yorgunluk ya da ağız-göz kuruluğu "
                "gibi belirtiler eşlik ediyorsa bir romatoloji uzmanına başvurmanız önerilir.</p>"
                "<p>Düşük düzeyde RF pozitifliği sağlıklı bireylerde, özellikle yaşlılarda ve sigara "
                "içenlerde de görülebileceğinden, tek başına RF pozitifliği kesin bir hastalık tanısı "
                "koymaz. Doktorunuz klinik muayene, detaylı öykü, anti-CCP, görüntüleme yöntemleri ve ek "
                "laboratuvar tetkikleri ile durumu değerlendirecektir. Romatoid artritte erken tanı, eklem "
                "hasarını ve deformiteyi önlemede kritik öneme sahiptir.</p>"
                "<p>Unutmayın: <strong>RF test sonuçları</strong> yalnızca bir tarama aracıdır. Pozitif sonuç "
                "alan herkes romatoid artrit hastası değildir ve negatif sonuç hastalığı tamamen dışlamaz "
                "(seronegatif RA). Semptomlarınız devam ediyorsa düzenli takip ve gerektiğinde tekrarlayan "
                "testler büyük önem taşır.</p>"
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
            heading="Rheumatoid factor (RF) blood test: what your results mean",
            body_html=(
                "<p><strong>Rheumatoid factor (RF)</strong> is an <strong>autoantibody</strong> (typically IgM class) "
                "produced by the immune system that can attack the body's own healthy tissues. The "
                "<strong>RF blood test</strong> is an important laboratory test used in diagnosing and monitoring "
                "various autoimmune and inflammatory conditions, particularly <strong>rheumatoid arthritis</strong>. "
                "However, a <strong>rheumatoid factor positive</strong> result does not automatically mean disease; "
                "approximately 5&ndash;10% of healthy individuals, especially the elderly, may have low-level "
                "RF positivity.</p>"
                "<p>In this guide we explain how to interpret your <strong>RF test</strong> results, what the "
                "<strong>RF normal range</strong> is, common causes of <strong>high RF</strong>, and when you "
                "should see a doctor. The information here is educational&mdash;always discuss your results with "
                "a qualified rheumatologist for a proper diagnosis.</p>"
                "<p>Also known as a <strong>rheumatoid arthritis blood test</strong>, the RF test is typically "
                "ordered when a patient presents with joint pain, swelling, morning stiffness, or unexplained "
                "fatigue. The test measures RF levels in your blood in IU/mL using nephelometry or turbidimetry, "
                "and the result is evaluated alongside other autoantibody tests such as anti-CCP (anti-cyclic "
                "citrullinated peptide).</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="RF normal range and how to interpret results",
            body_html=(
                "<p><strong>RF test results</strong> are typically reported in IU/mL (International Units per "
                "millilitre). In most laboratories the <strong>RF normal range</strong> is &lt;14 IU/mL (negative), "
                "although reference values may vary slightly between labs. The table below summarises the general "
                "classification of RF levels:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">RF level (IU/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretation</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Negative (normal)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Low positive; should be evaluated alongside clinical findings</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Moderate positive; increased probability of autoimmune disease</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">High positive; strongly associated with rheumatoid arthritis or other autoimmune conditions</td></tr>'
                "</tbody></table>"
                "<p>Although <strong>high RF</strong> levels are strongly associated with rheumatoid arthritis, "
                "RF alone does not establish a diagnosis. Approximately 70&ndash;80% of RA patients test RF "
                "positive, while 20&ndash;30% may be RF negative (seronegative rheumatoid arthritis). For this "
                "reason the <strong>anti-CCP antibody</strong> test, which has over 95% specificity for RA, "
                "is often ordered alongside RF to support clearer clinical interpretation.</p>"
                "<p>RF levels can naturally increase with age. In 15&ndash;25% of healthy individuals over 65, "
                "low-level RF positivity may be detected without any underlying disease. Always interpret your "
                "results alongside clinical findings, anti-CCP, CRP, and ESR.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of a positive rheumatoid factor",
            body_html=(
                "<p>A <strong>rheumatoid factor positive</strong> result can arise in many different situations. "
                "<strong>High RF</strong> does not always indicate rheumatoid arthritis&mdash;the result must be "
                "evaluated in its clinical context. The most common causes of RF positivity include:</p>"
                "<ul>"
                "<li><strong>Rheumatoid arthritis (RA):</strong> The best-known cause of RF positivity; "
                "70&ndash;80% of RA patients test positive. Higher RF levels are associated with more aggressive "
                "disease and extra-articular manifestations.</li>"
                "<li><strong>Sj&ouml;gren&rsquo;s syndrome:</strong> RF is positive in 75&ndash;95% of patients "
                "with this autoimmune condition characterised by dry mouth and dry eyes.</li>"
                "<li><strong>Mixed cryoglobulinaemia:</strong> Particularly when associated with hepatitis C, "
                "mixed cryoglobulinaemia produces high RF levels.</li>"
                "<li><strong>Chronic infections:</strong> Hepatitis C (HCV), hepatitis B, tuberculosis, "
                "infective endocarditis, and chronic viral infections can cause low-to-moderate RF positivity.</li>"
                "<li><strong>Other autoimmune diseases:</strong> Systemic lupus erythematosus (SLE), scleroderma, "
                "and polymyositis may also produce RF positivity.</li>"
                "<li><strong>Ageing:</strong> 15&ndash;25% of healthy individuals over 65 may have low-level "
                "RF positivity without any disease.</li>"
                "<li><strong>Smoking:</strong> Chronic smoking can stimulate low-level RF production and increases "
                "the risk of developing rheumatoid arthritis.</li>"
                "</ul>"
                "<p>To determine the cause of RF positivity, your doctor may order <strong>anti-CCP</strong>, "
                "ANA, complete blood count, CRP, ESR, and hepatitis serology. Anti-CCP has much higher "
                "specificity for RA than RF, and both tests being positive together significantly increases "
                "diagnostic confidence.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your <strong>RF blood test</strong> result is positive, do not panic, but consult a "
                "rheumatologist&mdash;especially if your <strong>RF</strong> level is above 50 IU/mL, or if "
                "you experience symptoms such as joint pain, morning stiffness lasting more than 30 minutes, "
                "joint swelling, unexplained fatigue, or dry mouth and eyes.</p>"
                "<p>Because low-level RF positivity can also occur in healthy individuals, particularly the "
                "elderly and smokers, a positive RF alone does not confirm a diagnosis. Your doctor will perform "
                "a clinical examination, take a detailed history, and order anti-CCP, imaging studies, and "
                "additional laboratory tests to clarify the situation. Early diagnosis of rheumatoid arthritis "
                "is critical in preventing joint damage and deformity.</p>"
                "<p>Remember: <strong>RF test results</strong> are only a screening tool. Not everyone who tests "
                "<strong>rheumatoid factor positive</strong> has rheumatoid arthritis, and a negative result does "
                "not completely rule it out (seronegative RA). If your symptoms persist, regular follow-up and "
                "repeat testing when appropriate are essential.</p>"
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
            heading="Factor reumatoide (FR): qué significan sus resultados",
            body_html=(
                "<p>El <strong>factor reumatoide (FR)</strong> es un <strong>autoanticuerpo</strong> (generalmente "
                "de clase IgM) producido por el sistema inmunitario que puede atacar los propios tejidos sanos del "
                "organismo. El <strong>análisis de FR en sangre</strong> es una prueba de laboratorio importante "
                "para el diagnóstico y seguimiento de diversas enfermedades autoinmunes e inflamatorias, "
                "especialmente la <strong>artritis reumatoide</strong>. Sin embargo, un resultado <strong>FR "
                "positivo</strong> no significa automáticamente enfermedad; aproximadamente el 5&ndash;10 % de "
                "las personas sanas, sobre todo en edades avanzadas, puede presentar niveles bajos de FR.</p>"
                "<p>En esta guía explicamos cómo interpretar los resultados de la <strong>prueba de FR</strong>, "
                "cuáles son los <strong>valores normales de FR</strong>, las causas de un <strong>FR elevado</strong> "
                "y cuándo debe consultar al médico. Esta información es educativa; consulte siempre a un "
                "reumatólogo para un diagnóstico adecuado.</p>"
                "<p>La prueba de FR, también conocida como <strong>análisis de sangre para artritis reumatoide"
                "</strong>, suele solicitarse cuando un paciente presenta dolor articular, hinchazón, rigidez "
                "matutina o fatiga inexplicable. Se mide mediante nefelometría o turbidimetría en IU/mL y se "
                "evalúa junto con el anticuerpo anti-CCP.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de factor reumatoide",
            body_html=(
                "<p>Los <strong>resultados de la prueba de FR</strong> se expresan habitualmente en IU/mL. "
                "En la mayoría de los laboratorios el <strong>rango normal de FR</strong> es &lt;14 IU/mL "
                "(negativo). La siguiente tabla resume la clasificación general:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Nivel de FR (IU/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretación</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Negativo (normal)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo bajo; debe evaluarse con los hallazgos clínicos</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo moderado; aumenta la probabilidad de enfermedad autoinmune</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo alto; fuerte asociación con artritis reumatoide u otras enfermedades autoinmunes</td></tr>'
                "</tbody></table>"
                "<p>Un <strong>FR elevado</strong> se asocia fuertemente con la artritis reumatoide, pero el "
                "FR por sí solo no establece diagnóstico. El 70&ndash;80 % de los pacientes con AR presenta FR "
                "positivo, mientras que el 20&ndash;30 % puede ser negativo (AR seronegativa). El anticuerpo "
                "<strong>anti-CCP</strong>, con una especificidad superior al 95 %, complementa al FR.</p>"
                "<p>El FR puede aumentar fisiológicamente con la edad. En el 15&ndash;25 % de los mayores de "
                "65 años puede detectarse FR positivo bajo sin enfermedad subyacente.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de un factor reumatoide positivo",
            body_html=(
                "<p>Un resultado <strong>FR positivo</strong> puede presentarse en muchas situaciones. Un "
                "<strong>FR elevado</strong> no siempre indica artritis reumatoide; debe evaluarse en su "
                "contexto clínico. Las causas más frecuentes incluyen:</p>"
                "<ul>"
                "<li><strong>Artritis reumatoide (AR):</strong> La causa más conocida; el 70&ndash;80 % de los "
                "pacientes con AR presenta FR positivo. Niveles altos se asocian con enfermedad más agresiva.</li>"
                "<li><strong>Síndrome de Sjögren:</strong> FR positivo en el 75&ndash;95 % de los pacientes con "
                "sequedad bucal y ocular característica.</li>"
                "<li><strong>Crioglobulinemia mixta:</strong> Especialmente asociada a hepatitis C, produce "
                "niveles altos de FR.</li>"
                "<li><strong>Infecciones crónicas:</strong> Hepatitis C (VHC), hepatitis B, tuberculosis, "
                "endocarditis infecciosa e infecciones virales crónicas.</li>"
                "<li><strong>Otras enfermedades autoinmunes:</strong> LES, esclerodermia y polimiositis.</li>"
                "<li><strong>Envejecimiento:</strong> El 15&ndash;25 % de los mayores de 65 años sanos puede "
                "presentar FR positivo bajo.</li>"
                "<li><strong>Tabaquismo:</strong> El consumo crónico de tabaco puede estimular la producción "
                "de FR y aumenta el riesgo de artritis reumatoide.</li>"
                "</ul>"
                "<p>Para determinar la causa, su médico puede solicitar <strong>anti-CCP</strong>, ANA, "
                "hemograma completo, PCR, VSG y serología de hepatitis.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si su prueba de <strong>FR en sangre</strong> resulta positiva, no se alarme, pero consulte "
                "a un reumatólogo, especialmente si el FR es superior a 50 IU/mL o si presenta dolor articular, "
                "rigidez matutina prolongada, hinchazón articular, fatiga inexplicable o sequedad bucal y ocular.</p>"
                "<p>Dado que la positividad de FR a niveles bajos también puede darse en personas sanas, "
                "especialmente en mayores y fumadores, un FR positivo por sí solo no confirma un diagnóstico. "
                "Su médico realizará exploración clínica, historia detallada, anti-CCP, pruebas de imagen y "
                "análisis adicionales. El diagnóstico precoz de la artritis reumatoide es fundamental para "
                "prevenir el daño articular y la deformidad.</p>"
                "<p>Recuerde: los resultados de la prueba de FR son solo una herramienta de cribado. No todos "
                "los pacientes con FR positivo tienen artritis reumatoide, y un resultado negativo no la "
                "descarta por completo (AR seronegativa). El seguimiento regular y la repetición de pruebas "
                "cuando sea apropiado son esenciales.</p>"
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
            heading="Rheumafaktor (RF) Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>Rheumafaktor (RF)</strong> ist ein <strong>Autoantikörper</strong> (meist der "
                "IgM-Klasse), der vom Immunsystem produziert wird und körpereigenes gesundes Gewebe angreifen "
                "kann. Der <strong>RF-Bluttest</strong> ist ein wichtiges Laborverfahren zur Diagnose und "
                "Überwachung verschiedener Autoimmun- und Entzündungserkrankungen, insbesondere der "
                "<strong>rheumatoiden Arthritis</strong>. Ein <strong>RF-positiver</strong> Befund bedeutet "
                "jedoch nicht automatisch eine Erkrankung&mdash;bei etwa 5&ndash;10 % gesunder Personen, "
                "vor allem bei älteren Menschen, kann ein niedrig-positiver RF nachgewiesen werden.</p>"
                "<p>In diesem Ratgeber erläutern wir, wie Sie Ihre <strong>RF-Testergebnisse</strong> "
                "interpretieren, was der <strong>RF-Normalbereich</strong> ist, welche Ursachen ein "
                "<strong>erhöhter RF</strong> haben kann und wann Sie einen Arzt aufsuchen sollten. Die Inhalte "
                "dienen der Aufklärung&mdash;für eine Diagnose wenden Sie sich bitte an einen Rheumatologen.</p>"
                "<p>Der RF-Bluttest, auch als <strong>Bluttest auf rheumatoide Arthritis</strong> bekannt, wird "
                "typischerweise bei Gelenkschmerzen, Schwellungen, Morgensteifigkeit oder unerklärlicher "
                "Müdigkeit angeordnet. Der RF-Spiegel wird mittels Nephelometrie oder Turbidimetrie in IU/mL "
                "gemessen und zusammen mit dem Anti-CCP-Antikörper bewertet.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="RF-Normalwerte und Ergebnisinterpretation",
            body_html=(
                "<p><strong>RF-Testergebnisse</strong> werden in IU/mL angegeben. In den meisten Laboren gilt "
                "ein <strong>RF-Normalbereich</strong> von &lt;14 IU/mL (negativ). Die folgende Tabelle fasst "
                "die allgemeine Klassifikation zusammen:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">RF-Spiegel (IU/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretation</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Negativ (normal)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Niedrig positiv; sollte zusammen mit klinischen Befunden bewertet werden</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mäßig positiv; erhöhte Wahrscheinlichkeit einer Autoimmunerkrankung</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hoch positiv; starke Assoziation mit rheumatoider Arthritis oder anderen Autoimmunerkrankungen</td></tr>'
                "</tbody></table>"
                "<p>Ein <strong>erhöhter RF</strong> ist stark mit rheumatoider Arthritis assoziiert, stellt "
                "jedoch allein keine Diagnose. Ca. 70&ndash;80 % der RA-Patienten sind RF-positiv, während "
                "20&ndash;30 % RF-negativ sein können (seronegative RA). Der <strong>Anti-CCP-Antikörper</strong> "
                "mit einer Spezifität von über 95 % ergänzt den RF.</p>"
                "<p>Der RF-Spiegel kann mit dem Alter natürlich ansteigen. Bei 15&ndash;25 % der gesunden "
                "Personen über 65 kann ein niedrig-positiver RF ohne zugrunde liegende Erkrankung nachgewiesen "
                "werden.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für einen positiven Rheumafaktor",
            body_html=(
                "<p>Ein <strong>RF-positiver</strong> Befund kann in vielen unterschiedlichen Situationen "
                "auftreten. Ein <strong>erhöhter RF</strong> bedeutet nicht immer rheumatoide Arthritis; das "
                "Ergebnis muss im klinischen Kontext bewertet werden. Die häufigsten Ursachen sind:</p>"
                "<ul>"
                "<li><strong>Rheumatoide Arthritis (RA):</strong> Die bekannteste Ursache; 70&ndash;80 % der "
                "RA-Patienten sind RF-positiv. Hohe Werte korrelieren mit aggressiverem Verlauf.</li>"
                "<li><strong>Sjögren-Syndrom:</strong> RF-positiv bei 75&ndash;95 % der Patienten mit dieser "
                "durch Mund- und Augentrockenheit gekennzeichneten Erkrankung.</li>"
                "<li><strong>Gemischte Kryoglobulinämie:</strong> Besonders bei Hepatitis-C-Assoziation treten "
                "hohe RF-Spiegel auf.</li>"
                "<li><strong>Chronische Infektionen:</strong> Hepatitis C, Hepatitis B, Tuberkulose, infektiöse "
                "Endokarditis und chronische Virusinfektionen.</li>"
                "<li><strong>Andere Autoimmunerkrankungen:</strong> SLE, Sklerodermie und Polymyositis.</li>"
                "<li><strong>Alter:</strong> 15&ndash;25 % der gesunden Personen über 65 können niedrig-positive "
                "RF-Werte aufweisen.</li>"
                "<li><strong>Rauchen:</strong> Chronisches Rauchen kann die RF-Produktion anregen und erhöht das "
                "RA-Risiko.</li>"
                "</ul>"
                "<p>Zur Klärung der Ursache kann Ihr Arzt <strong>Anti-CCP</strong>, ANA, Blutbild, CRP, BSG "
                "und Hepatitis-Serologie anordnen.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Ihr <strong>RF-Bluttest</strong> positiv ausfällt, bewahren Sie Ruhe, suchen Sie aber "
                "einen Rheumatologen auf&mdash;insbesondere bei RF-Werten über 50 IU/mL oder bei Symptomen wie "
                "Gelenkschmerzen, anhaltender Morgensteifigkeit, Gelenkschwellung, unerklärlicher Müdigkeit oder "
                "Mund- und Augentrockenheit.</p>"
                "<p>Da ein niedrig-positiver RF auch bei gesunden Personen, vor allem bei Älteren und Rauchern, "
                "vorkommen kann, bestätigt ein positiver RF allein keine Diagnose. Ihr Arzt wird eine klinische "
                "Untersuchung durchführen, eine ausführliche Anamnese erheben und Anti-CCP, bildgebende Verfahren "
                "sowie ergänzende Labortests anordnen. Eine frühe Diagnose der rheumatoiden Arthritis ist "
                "entscheidend, um Gelenkschäden und Deformitäten zu verhindern.</p>"
                "<p><strong>RF-Testergebnisse</strong> sind lediglich ein Screening-Instrument. Nicht jeder "
                "mit positivem Befund hat rheumatoide Arthritis, und ein negatives Ergebnis schließt sie nicht "
                "vollständig aus (seronegative RA). Bei anhaltenden Symptomen sind regelmäßige Kontrollen und "
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
            heading="Facteur rhumatoïde (FR) : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>facteur rhumatoïde (FR)</strong> est un <strong>auto-anticorps</strong> "
                "(généralement de classe IgM) produit par le système immunitaire pouvant attaquer les tissus "
                "sains de l'organisme. Le <strong>dosage du FR sanguin</strong> est un examen de laboratoire "
                "important pour le diagnostic et le suivi de diverses maladies auto-immunes et inflammatoires, "
                "en particulier la <strong>polyarthrite rhumatoïde</strong>. Cependant, un résultat "
                "<strong>FR positif</strong> ne confirme pas automatiquement une maladie&mdash;environ "
                "5 à 10 % des personnes en bonne santé, surtout les personnes âgées, peuvent présenter un "
                "FR faiblement positif.</p>"
                "<p>Dans ce guide nous expliquons comment interpréter vos <strong>résultats du test FR</strong>, "
                "quelles sont les <strong>valeurs normales du FR</strong>, les causes d'un <strong>FR élevé"
                "</strong> et quand consulter un médecin. Ces informations sont à visée éducative&mdash;consultez "
                "toujours un rhumatologue pour un diagnostic approprié.</p>"
                "<p>Le dosage du FR, également appelé <strong>bilan sanguin pour polyarthrite rhumatoïde"
                "</strong>, est généralement prescrit devant des douleurs articulaires, un gonflement, une "
                "raideur matinale ou une fatigue inexpliquée. Le taux est mesuré par néphélométrie ou "
                "turbidimétrie en UI/mL et évalué conjointement avec l'anticorps anti-CCP.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales du facteur rhumatoïde",
            body_html=(
                "<p>Les <strong>résultats du test FR</strong> sont exprimés en UI/mL. Dans la plupart des "
                "laboratoires la <strong>valeur normale du FR</strong> est &lt;14 UI/mL (négatif). Le tableau "
                "ci-dessous résume la classification générale :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Taux de FR (UI/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interprétation</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Négatif (normal)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Faiblement positif ; à évaluer avec les données cliniques</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positif modéré ; probabilité accrue de maladie auto-immune</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positif élevé ; forte association avec la polyarthrite rhumatoïde ou d\'autres maladies auto-immunes</td></tr>'
                "</tbody></table>"
                "<p>Un <strong>FR élevé</strong> est fortement associé à la polyarthrite rhumatoïde, mais le "
                "FR seul ne pose pas de diagnostic. Environ 70 à 80 % des patients atteints de PR sont FR "
                "positifs, tandis que 20 à 30 % peuvent être FR négatifs (PR séronégative). L'anticorps "
                "<strong>anti-CCP</strong>, avec une spécificité supérieure à 95 %, complète le FR.</p>"
                "<p>Le FR peut augmenter physiologiquement avec l'âge. Chez 15 à 25 % des personnes saines de "
                "plus de 65 ans, un FR faiblement positif peut être détecté sans maladie sous-jacente.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un facteur rhumatoïde positif",
            body_html=(
                "<p>Un résultat <strong>FR positif</strong> peut apparaître dans de nombreuses situations. Un "
                "<strong>FR élevé</strong> ne signifie pas toujours polyarthrite rhumatoïde; le résultat doit "
                "être évalué dans son contexte clinique. Les causes les plus fréquentes sont :</p>"
                "<ul>"
                "<li><strong>Polyarthrite rhumatoïde (PR) :</strong> La cause la plus connue ; 70 à 80 % des "
                "patients PR sont FR positifs. Des taux élevés sont associés à une maladie plus agressive.</li>"
                "<li><strong>Syndrome de Sjögren :</strong> FR positif chez 75 à 95 % des patients présentant "
                "sécheresse buccale et oculaire.</li>"
                "<li><strong>Cryoglobulinémie mixte :</strong> Surtout associée à l'hépatite C, elle produit "
                "des taux élevés de FR.</li>"
                "<li><strong>Infections chroniques :</strong> Hépatite C, hépatite B, tuberculose, endocardite "
                "infectieuse et infections virales chroniques.</li>"
                "<li><strong>Autres maladies auto-immunes :</strong> LES, sclérodermie et polymyosite.</li>"
                "<li><strong>Vieillissement :</strong> 15 à 25 % des personnes saines de plus de 65 ans peuvent "
                "être faiblement FR positives.</li>"
                "<li><strong>Tabagisme :</strong> Le tabagisme chronique peut stimuler la production de FR et "
                "augmente le risque de polyarthrite rhumatoïde.</li>"
                "</ul>"
                "<p>Pour déterminer la cause, votre médecin peut prescrire <strong>anti-CCP</strong>, ANA, "
                "hémogramme, CRP, VS et sérologie hépatite.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si votre <strong>test FR sanguin</strong> est positif, ne paniquez pas, mais consultez un "
                "rhumatologue, surtout si le taux dépasse 50 UI/mL ou si vous présentez des douleurs "
                "articulaires, une raideur matinale prolongée, un gonflement articulaire, une fatigue "
                "inexpliquée ou une sécheresse buccale et oculaire.</p>"
                "<p>Un FR faiblement positif pouvant survenir chez des personnes en bonne santé, notamment les "
                "personnes âgées et les fumeurs, un FR positif seul ne confirme pas un diagnostic. Votre "
                "médecin effectuera un examen clinique, recueillera un historique détaillé et prescrira anti-CCP, "
                "imagerie et analyses complémentaires. Un diagnostic précoce de la polyarthrite rhumatoïde est "
                "essentiel pour prévenir les lésions et déformations articulaires.</p>"
                "<p>N'oubliez pas : les <strong>résultats du test FR</strong> ne sont qu'un outil de dépistage. "
                "Toutes les personnes FR positives n'ont pas de polyarthrite rhumatoïde, et un résultat négatif "
                "ne l'exclut pas totalement (PR séronégative). Un suivi régulier et des tests répétés le cas "
                "échéant sont indispensables.</p>"
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
            heading="Fattore reumatoide (FR): cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>fattore reumatoide (FR)</strong> è un <strong>autoanticorpo</strong> (generalmente "
                "di classe IgM) prodotto dal sistema immunitario che può attaccare i tessuti sani dell'organismo. "
                "Il <strong>test del FR nel sangue</strong> è un esame di laboratorio importante per la diagnosi "
                "e il monitoraggio di diverse malattie autoimmuni e infiammatorie, in particolare l'<strong>artrite "
                "reumatoide</strong>. Tuttavia, un risultato <strong>FR positivo</strong> non conferma "
                "automaticamente una malattia&mdash;circa il 5&ndash;10 % delle persone sane, soprattutto gli "
                "anziani, può presentare livelli bassi di FR.</p>"
                "<p>In questa guida spieghiamo come interpretare i <strong>risultati del test FR</strong>, "
                "qual è il <strong>range normale del FR</strong>, le cause di un <strong>FR elevato</strong> e "
                "quando rivolgersi al medico. Le informazioni hanno scopo educativo&mdash;consultate sempre un "
                "reumatologo per una diagnosi adeguata.</p>"
                "<p>Il test del FR, noto anche come <strong>esame del sangue per artrite reumatoide</strong>, "
                "viene generalmente richiesto in presenza di dolori articolari, gonfiore, rigidità mattutina o "
                "stanchezza inspiegabile. Il livello viene misurato tramite nefelometria o turbidimetria in "
                "UI/mL e valutato insieme all'anticorpo anti-CCP.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali del fattore reumatoide",
            body_html=(
                "<p>I <strong>risultati del test FR</strong> sono espressi in UI/mL. Nella maggior parte dei "
                "laboratori il <strong>range normale del FR</strong> è &lt;14 UI/mL (negativo). La tabella "
                "seguente riassume la classificazione generale:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Livello FR (UI/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretazione</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Negativo (normale)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Basso positivo; da valutare con i dati clinici</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Positivo moderato; aumentata probabilità di malattia autoimmune</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto positivo; forte associazione con artrite reumatoide o altre malattie autoimmuni</td></tr>'
                "</tbody></table>"
                "<p>Un <strong>FR elevato</strong> è fortemente associato all'artrite reumatoide, ma il FR da "
                "solo non consente di porre diagnosi. Circa il 70&ndash;80 % dei pazienti con AR risulta FR "
                "positivo, mentre il 20&ndash;30 % può essere FR negativo (AR sieronegativa). L'anticorpo "
                "<strong>anti-CCP</strong>, con una specificità superiore al 95 %, integra il FR.</p>"
                "<p>Il FR può aumentare fisiologicamente con l'età. Nel 15&ndash;25 % dei soggetti sani "
                "oltre i 65 anni può essere rilevato un FR basso positivo senza alcuna malattia sottostante.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di un fattore reumatoide positivo",
            body_html=(
                "<p>Un risultato <strong>FR positivo</strong> può presentarsi in molte situazioni diverse. Un "
                "<strong>FR elevato</strong> non significa sempre artrite reumatoide; il risultato va valutato "
                "nel contesto clinico. Le cause più comuni includono:</p>"
                "<ul>"
                "<li><strong>Artrite reumatoide (AR):</strong> La causa più nota; il 70&ndash;80 % dei pazienti "
                "con AR risulta FR positivo. Livelli elevati sono associati a malattia più aggressiva.</li>"
                "<li><strong>Sindrome di Sjögren:</strong> FR positivo nel 75&ndash;95 % dei pazienti con "
                "secchezza orale e oculare.</li>"
                "<li><strong>Crioglobulinemia mista:</strong> Soprattutto associata all'epatite C, produce "
                "livelli elevati di FR.</li>"
                "<li><strong>Infezioni croniche:</strong> Epatite C, epatite B, tubercolosi, endocardite "
                "infettiva e infezioni virali croniche.</li>"
                "<li><strong>Altre malattie autoimmuni:</strong> LES, sclerodermia e polimiosite.</li>"
                "<li><strong>Invecchiamento:</strong> Il 15&ndash;25 % dei soggetti sani oltre i 65 anni può "
                "presentare FR basso positivo.</li>"
                "<li><strong>Fumo:</strong> Il fumo cronico può stimolare la produzione di FR e aumenta il "
                "rischio di artrite reumatoide.</li>"
                "</ul>"
                "<p>Per determinare la causa, il medico può richiedere <strong>anti-CCP</strong>, ANA, "
                "emocromo completo, PCR, VES e sierologia per epatite.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se il risultato del <strong>test FR nel sangue</strong> è positivo, non allarmatevi, ma "
                "rivolgetevi a un reumatologo, soprattutto se il FR supera 50 UI/mL o se presentate dolori "
                "articolari, rigidità mattutina prolungata, gonfiore articolare, stanchezza inspiegabile o "
                "secchezza orale e oculare.</p>"
                "<p>Poiché un FR basso positivo può verificarsi anche in soggetti sani, in particolare anziani "
                "e fumatori, un FR positivo da solo non conferma una diagnosi. Il medico eseguirà un esame "
                "clinico, raccoglierà un'anamnesi dettagliata e prescriverà anti-CCP, esami di imaging e "
                "analisi aggiuntive. La diagnosi precoce dell'artrite reumatoide è fondamentale per prevenire "
                "il danno e la deformità articolare.</p>"
                "<p>Ricordate: i <strong>risultati del test FR</strong> sono solo uno strumento di screening. "
                "Non tutti coloro che risultano FR positivi hanno un'artrite reumatoide, e un risultato "
                "negativo non la esclude completamente (AR sieronegativa). Il monitoraggio regolare e la "
                "ripetizione dei test quando opportuno sono essenziali.</p>"
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
            heading="בדיקת גורם שגרוני (RF) בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>גורם שגרוני (RF)</strong> הוא <strong>נוגדן עצמי</strong> (בדרך כלל מסוג IgM) "
                "המיוצר על ידי מערכת החיסון ועלול לתקוף רקמות בריאות של הגוף עצמו. <strong>בדיקת RF בדם</strong> "
                "היא בדיקת מעבדה חשובה לאבחון ומעקב אחר מחלות אוטואימוניות ודלקתיות שונות, בעיקר "
                "<strong>דלקת מפרקים שגרונית</strong> (ראומטואיד ארתריטיס). עם זאת, תוצאה <strong>RF חיובית"
                "</strong> אינה מעידה אוטומטית על מחלה&mdash;כ-5&ndash;10% מהאנשים הבריאים, בעיקר קשישים, "
                "עשויים להציג רמות נמוכות של RF.</p>"
                "<p>במדריך זה נסביר כיצד לפרש את <strong>תוצאות בדיקת RF</strong>, מהו <strong>הטווח התקין של "
                "RF</strong>, מהם הגורמים ל<strong>RF גבוה</strong> ומתי לפנות לרופא. המידע כאן חינוכי "
                "בלבד&mdash;התייעצו תמיד עם ראומטולוג לאבחון מדויק.</p>"
                "<p>בדיקת RF, הידועה גם כ<strong>בדיקת דם לדלקת מפרקים שגרונית</strong>, מוזמנת בדרך כלל "
                "כאשר מטופל מציג כאבי מפרקים, נפיחות, נוקשות בוקר או עייפות בלתי מוסברת. רמת ה-RF נמדדת "
                "בנפלומטריה או טורבידימטריה ב-IU/mL ומוערכת יחד עם נוגדן anti-CCP.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכים תקינים של גורם שגרוני",
            body_html=(
                "<p><strong>תוצאות בדיקת RF</strong> מדווחות ב-IU/mL. ברוב המעבדות <strong>הטווח התקין של "
                "RF</strong> הוא &lt;14 IU/mL (שלילי). הטבלה הבאה מסכמת את הסיווג הכללי:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">רמת RF (IU/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">פרשנות</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">שלילי (תקין)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">חיובי נמוך; יש להעריך לצד ממצאים קליניים</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">חיובי בינוני; הסתברות מוגברת למחלה אוטואימונית</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">חיובי גבוה; קשר חזק עם דלקת מפרקים שגרונית או מחלות אוטואימוניות אחרות</td></tr>'
                "</tbody></table>"
                "<p><strong>RF גבוה</strong> קשור בחוזקה לדלקת מפרקים שגרונית, אך RF לבדו אינו קובע אבחנה. "
                "כ-70&ndash;80% מחולי RA נמצאים RF חיובי, בעוד 20&ndash;30% עשויים להיות RF שלילי (RA "
                "סרונגטיבית). הנוגדן <strong>anti-CCP</strong>, בעל סגוליות של מעל 95%, משלים את ה-RF.</p>"
                "<p>רמת RF יכולה לעלות באופן טבעי עם הגיל. ב-15&ndash;25% מהאנשים הבריאים מעל גיל 65 ניתן "
                "לזהות RF חיובי נמוך ללא מחלה בסיסית.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים ל-RF חיובי",
            body_html=(
                "<p>תוצאת <strong>RF חיובית</strong> יכולה להופיע במצבים שונים רבים. <strong>RF גבוה</strong> "
                "לא תמיד מעיד על דלקת מפרקים שגרונית; יש להעריך את התוצאה בהקשרה הקליני. הגורמים השכיחים "
                "ביותר כוללים:</p>"
                "<ul>"
                "<li><strong>דלקת מפרקים שגרונית (RA):</strong> הגורם הידוע ביותר; 70&ndash;80% מחולי RA "
                "נמצאים RF חיובי. רמות גבוהות קשורות למהלך מחלה אגרסיבי יותר.</li>"
                "<li><strong>תסמונת שגרן:</strong> RF חיובי ב-75&ndash;95% מהמטופלים עם יובש בפה ובעיניים.</li>"
                "<li><strong>קריוגלובולינמיה מעורבת:</strong> במיוחד בקשר להפטיטיס C, מייצרת רמות גבוהות "
                "של RF.</li>"
                "<li><strong>זיהומים כרוניים:</strong> הפטיטיס C, הפטיטיס B, שחפת, אנדוקרדיטיס זיהומית "
                "וזיהומים ויראליים כרוניים.</li>"
                "<li><strong>מחלות אוטואימוניות אחרות:</strong> זאבת (SLE), סקלרודרמה ופולימיוזיטיס.</li>"
                "<li><strong>הזדקנות:</strong> 15&ndash;25% מהאנשים הבריאים מעל גיל 65 עשויים להציג RF "
                "חיובי נמוך.</li>"
                "<li><strong>עישון:</strong> עישון כרוני עלול לעורר ייצור RF ומגביר את הסיכון לדלקת "
                "מפרקים שגרונית.</li>"
                "</ul>"
                "<p>כדי לקבוע את הגורם, הרופא עשוי להזמין <strong>anti-CCP</strong>, ANA, ספירת דם מלאה, "
                "CRP, שקיעת דם וסרולוגיית הפטיטיס.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם תוצאת <strong>בדיקת RF בדם</strong> שלך חיובית, אל תיבהל, אך פנה לראומטולוג"
                "&mdash;במיוחד אם רמת ה-RF מעל 50 IU/mL, או אם אתה חווה תסמינים כמו כאבי מפרקים, "
                "נוקשות בוקר ממושכת, נפיחות במפרקים, עייפות בלתי מוסברת או יובש בפה ובעיניים.</p>"
                "<p>מכיוון ש-RF חיובי נמוך יכול להופיע גם אצל אנשים בריאים, בעיקר קשישים ומעשנים, RF "
                "חיובי לבדו אינו מאשר אבחנה. הרופא שלך יבצע בדיקה קלינית, ייקח אנמנזה מפורטת ויזמין "
                "anti-CCP, בדיקות הדמיה ובדיקות מעבדה נוספות. אבחון מוקדם של דלקת מפרקים שגרונית חיוני "
                "למניעת נזק ועיוות במפרקים.</p>"
                "<p>זכרו: <strong>תוצאות בדיקת RF</strong> הן רק כלי סקירה. לא כל מי שנמצא RF חיובי סובל "
                "מדלקת מפרקים שגרונית, ותוצאה שלילית אינה שוללת אותה לחלוטין (RA סרונגטיבית). אם התסמינים "
                "נמשכים, מעקב קבוע ובדיקות חוזרות בעת הצורך הם חיוניים.</p>"
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
            heading="रुमेटॉइड फ़ैक्टर (RF) ब्लड टेस्ट: आपके रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>रुमेटॉइड फ़ैक्टर (RF)</strong> एक <strong>ऑटोएंटीबॉडी</strong> (आमतौर पर IgM वर्ग) "
                "है जो प्रतिरक्षा प्रणाली द्वारा उत्पादित होता है और शरीर के अपने स्वस्थ ऊतकों पर हमला कर "
                "सकता है। <strong>RF ब्लड टेस्ट</strong> विभिन्न ऑटोइम्यून और सूजन संबंधी बीमारियों, विशेष "
                "रूप से <strong>रुमेटॉइड आर्थराइटिस</strong> के निदान और निगरानी के लिए एक महत्वपूर्ण "
                "प्रयोगशाला परीक्षण है। हालांकि, <strong>RF पॉज़िटिव</strong> रिज़ल्ट का मतलब हमेशा बीमारी "
                "नहीं होता&mdash;लगभग 5&ndash;10% स्वस्थ लोगों में, विशेषकर बुज़ुर्गों में, कम स्तर पर RF "
                "पॉज़िटिव आ सकता है।</p>"
                "<p>इस गाइड में हम बताएंगे कि <strong>RF टेस्ट</strong> रिज़ल्ट की व्याख्या कैसे करें, "
                "<strong>RF का सामान्य रेंज</strong> क्या है, <strong>उच्च RF</strong> के कारण क्या हैं और "
                "डॉक्टर से कब मिलना चाहिए। यहाँ दी गई जानकारी शैक्षिक उद्देश्य से है&mdash;सही निदान के "
                "लिए हमेशा रुमेटोलॉजिस्ट से परामर्श करें।</p>"
                "<p><strong>रुमेटॉइड आर्थराइटिस ब्लड टेस्ट</strong> के रूप में भी जाना जाने वाला RF टेस्ट "
                "आमतौर पर तब किया जाता है जब किसी मरीज़ में जोड़ों का दर्द, सूजन, सुबह की अकड़न या "
                "अस्पष्ट थकान जैसे लक्षण दिखाई देते हैं। टेस्ट नेफ़ेलोमेट्री या टर्बिडिमेट्री द्वारा "
                "IU/mL में RF स्तर मापता है और anti-CCP जैसे अन्य ऑटोएंटीबॉडी टेस्ट के साथ मूल्यांकित "
                "किया जाता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="RF सामान्य रेंज और रिज़ल्ट की व्याख्या",
            body_html=(
                "<p><strong>RF टेस्ट रिज़ल्ट</strong> IU/mL में रिपोर्ट किए जाते हैं। अधिकांश प्रयोगशालाओं "
                "में <strong>RF का सामान्य रेंज</strong> &lt;14 IU/mL (नेगेटिव) माना जाता है। नीचे दी गई "
                "तालिका में सामान्य RF वर्गीकरण दिया गया है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">RF स्तर (IU/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">व्याख्या</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">नेगेटिव (सामान्य)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">कम पॉज़िटिव; क्लिनिकल निष्कर्षों के साथ मूल्यांकन किया जाना चाहिए</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">मध्यम पॉज़िटिव; ऑटोइम्यून बीमारी की संभावना बढ़ जाती है</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">उच्च पॉज़िटिव; रुमेटॉइड आर्थराइटिस या अन्य ऑटोइम्यून बीमारियों से मज़बूत संबंध</td></tr>'
                "</tbody></table>"
                "<p><strong>उच्च RF</strong> रुमेटॉइड आर्थराइटिस से मज़बूत रूप से जुड़ा है, लेकिन अकेले "
                "RF से निदान नहीं होता। लगभग 70&ndash;80% RA रोगी RF पॉज़िटिव होते हैं, जबकि 20&ndash;30% "
                "RF नेगेटिव हो सकते हैं (सेरोनेगेटिव RA)। <strong>Anti-CCP एंटीबॉडी</strong>, जिसकी RA के "
                "लिए 95% से अधिक विशिष्टता है, RF का पूरक है।</p>"
                "<p>RF स्तर उम्र के साथ स्वाभाविक रूप से बढ़ सकता है। 65 वर्ष से अधिक उम्र के 15&ndash;25% "
                "स्वस्थ व्यक्तियों में बिना किसी बीमारी के कम स्तर पर RF पॉज़िटिव मिल सकता है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="RF पॉज़िटिव होने के कारण",
            body_html=(
                "<p><strong>RF पॉज़िटिव</strong> रिज़ल्ट कई अलग-अलग स्थितियों में आ सकता है। <strong>उच्च "
                "RF</strong> का मतलब हमेशा रुमेटॉइड आर्थराइटिस नहीं होता; रिज़ल्ट को क्लिनिकल संदर्भ में "
                "मूल्यांकित किया जाना चाहिए। सबसे आम कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>रुमेटॉइड आर्थराइटिस (RA):</strong> RF पॉज़िटिविटी का सबसे प्रसिद्ध कारण; "
                "70&ndash;80% RA रोगी RF पॉज़िटिव होते हैं। उच्च स्तर अधिक आक्रामक बीमारी से जुड़े हैं।</li>"
                "<li><strong>शोग्रेन सिंड्रोम:</strong> मुंह और आंखों की सूखापन वाले 75&ndash;95% रोगियों "
                "में RF पॉज़िटिव होता है।</li>"
                "<li><strong>मिक्स्ड क्रायोग्लोबुलिनीमिया:</strong> विशेषकर हेपेटाइटिस C से जुड़ा होने पर, "
                "उच्च RF स्तर पैदा करता है।</li>"
                "<li><strong>क्रोनिक संक्रमण:</strong> हेपेटाइटिस C (HCV), हेपेटाइटिस B, तपेदिक, "
                "इन्फ़ेक्टिव एंडोकार्डाइटिस और क्रोनिक वायरल संक्रमण।</li>"
                "<li><strong>अन्य ऑटोइम्यून बीमारियां:</strong> SLE, स्क्लेरोडर्मा और पॉलीमायोसिटिस।</li>"
                "<li><strong>बुढ़ापा:</strong> 65 वर्ष से अधिक उम्र के 15&ndash;25% स्वस्थ व्यक्तियों में "
                "कम स्तर पर RF पॉज़िटिव हो सकता है।</li>"
                "<li><strong>धूम्रपान:</strong> क्रोनिक धूम्रपान कम स्तर पर RF उत्पादन को उत्तेजित कर "
                "सकता है और रुमेटॉइड आर्थराइटिस का जोखिम बढ़ाता है।</li>"
                "</ul>"
                "<p>कारण निर्धारित करने के लिए डॉक्टर <strong>anti-CCP</strong>, ANA, CBC, CRP, ESR और "
                "हेपेटाइटिस सेरोलॉजी करवा सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपके <strong>RF ब्लड टेस्ट</strong> का रिज़ल्ट पॉज़िटिव आता है तो घबराएं नहीं, "
                "लेकिन रुमेटोलॉजिस्ट से ज़रूर मिलें&mdash;विशेषकर अगर RF स्तर 50 IU/mL से अधिक है, या "
                "अगर आपको जोड़ों का दर्द, 30 मिनट से अधिक चलने वाली सुबह की अकड़न, जोड़ों की सूजन, "
                "अस्पष्ट थकान या मुंह और आंखों का सूखापन जैसे लक्षण हैं।</p>"
                "<p>चूंकि कम स्तर पर RF पॉज़िटिविटी स्वस्थ व्यक्तियों, विशेषकर बुज़ुर्गों और धूम्रपान "
                "करने वालों में भी हो सकती है, अकेले RF पॉज़िटिव रिज़ल्ट निदान की पुष्टि नहीं करता। "
                "डॉक्टर क्लिनिकल जांच, विस्तृत इतिहास, anti-CCP, इमेजिंग और अतिरिक्त लैब टेस्ट से स्थिति "
                "का मूल्यांकन करेंगे। रुमेटॉइड आर्थराइटिस में शुरुआती निदान जोड़ों के नुकसान और विकृति "
                "को रोकने के लिए बेहद ज़रूरी है।</p>"
                "<p>याद रखें: <strong>RF टेस्ट रिज़ल्ट</strong> केवल एक स्क्रीनिंग टूल है। RF पॉज़िटिव "
                "आने वाले हर व्यक्ति को रुमेटॉइड आर्थराइटिस नहीं होती, और नेगेटिव रिज़ल्ट इसे पूरी तरह "
                "ख़ारिज नहीं करता (सेरोनेगेटिव RA)। अगर लक्षण बने रहते हैं तो नियमित फ़ॉलो-अप और ज़रूरत "
                "पड़ने पर दोबारा टेस्ट करवाना बहुत ज़रूरी है।</p>"
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
            heading="تحليل عامل الروماتويد (RF) في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p><strong>عامل الروماتويد (RF)</strong> هو <strong>جسم مضاد ذاتي</strong> (عادةً من نوع IgM) "
                "يُنتجه الجهاز المناعي ويمكن أن يهاجم أنسجة الجسم السليمة. يُعد <strong>تحليل RF في الدم"
                "</strong> فحصاً مخبرياً مهماً لتشخيص ومتابعة أمراض المناعة الذاتية والالتهابات المختلفة، "
                "وخاصة <strong>التهاب المفاصل الروماتويدي</strong>. إلا أن نتيجة <strong>RF إيجابية</strong> "
                "لا تعني بالضرورة وجود مرض&mdash;فنحو 5&ndash;10% من الأشخاص الأصحاء، خصوصاً كبار السن، "
                "قد يُظهرون مستويات منخفضة من RF.</p>"
                "<p>في هذا الدليل نشرح كيفية تفسير <strong>نتائج تحليل RF</strong>، والنطاق الطبيعي لـ RF، "
                "وأسباب <strong>ارتفاع RF</strong>، ومتى يجب مراجعة الطبيب. المعلومات هنا تثقيفية "
                "بحتة&mdash;استشر دائماً طبيب أمراض الروماتيزم للحصول على تشخيص دقيق.</p>"
                "<p>تحليل RF، المعروف أيضاً بـ<strong>فحص دم لالتهاب المفاصل الروماتويدي</strong>، يُطلب "
                "عادةً عندما يعاني المريض من آلام المفاصل أو تورّم أو تيبّس صباحي أو إرهاق غير مفسّر. "
                "يُقاس مستوى RF بطريقة النيفيلومتري أو التوربيديمتري بوحدة IU/mL ويُقيَّم مع الجسم المضاد "
                "anti-CCP.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية لعامل الروماتويد",
            body_html=(
                "<p>تُعبَّر <strong>نتائج تحليل RF</strong> بوحدة IU/mL. في معظم المختبرات يُعتبر "
                "<strong>النطاق الطبيعي لـ RF</strong> أقل من 14 IU/mL (سلبي). يلخص الجدول التالي "
                "التصنيف العام:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">مستوى RF (IU/mL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">التفسير</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;14</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">سلبي (طبيعي)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">14 &ndash; 50</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">إيجابي منخفض؛ يجب تقييمه مع المعطيات السريرية</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">51 &ndash; 100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">إيجابي متوسط؛ احتمالية متزايدة لمرض مناعي ذاتي</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;100</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">إيجابي مرتفع؛ ارتباط قوي بالتهاب المفاصل الروماتويدي أو أمراض مناعية ذاتية أخرى</td></tr>'
                "</tbody></table>"
                "<p><strong>RF المرتفع</strong> يرتبط بقوة بالتهاب المفاصل الروماتويدي، لكن RF وحده لا "
                "يُشخِّص المرض. نحو 70&ndash;80% من مرضى RA يكونون RF إيجابيين، بينما 20&ndash;30% قد "
                "يكونون RF سلبيين (RA سلبية المصل). الجسم المضاد <strong>anti-CCP</strong>، بنوعية تتجاوز "
                "95%، يُكمّل RF.</p>"
                "<p>قد يرتفع مستوى RF طبيعياً مع التقدم بالعمر. في 15&ndash;25% من الأصحاء فوق 65 سنة "
                "يمكن اكتشاف RF إيجابي منخفض دون أي مرض كامن.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب عامل الروماتويد الإيجابي",
            body_html=(
                "<p>يمكن أن تظهر نتيجة <strong>RF إيجابية</strong> في حالات عديدة مختلفة. <strong>RF "
                "المرتفع</strong> لا يعني دائماً التهاب مفاصل روماتويدي؛ يجب تقييم النتيجة في سياقها "
                "السريري. تشمل الأسباب الأكثر شيوعاً:</p>"
                "<ul>"
                "<li><strong>التهاب المفاصل الروماتويدي (RA):</strong> السبب الأشهر؛ 70&ndash;80% من مرضى "
                "RA يكونون RF إيجابيين. المستويات المرتفعة ترتبط بمرض أكثر عدوانية.</li>"
                "<li><strong>متلازمة شوغرن:</strong> RF إيجابي في 75&ndash;95% من المرضى المصابين بجفاف "
                "الفم والعينين.</li>"
                "<li><strong>الغلوبولينات البردية المختلطة:</strong> خاصة عند ارتباطها بالتهاب الكبد C، "
                "تُنتج مستويات مرتفعة من RF.</li>"
                "<li><strong>العدوى المزمنة:</strong> التهاب الكبد C، التهاب الكبد B، السل، التهاب الشغاف "
                "العدوائي والعدوى الفيروسية المزمنة.</li>"
                "<li><strong>أمراض مناعية ذاتية أخرى:</strong> الذئبة الحمراء (SLE)، تصلب الجلد والتهاب "
                "العضلات المتعدد.</li>"
                "<li><strong>التقدم بالعمر:</strong> 15&ndash;25% من الأصحاء فوق 65 سنة قد يُظهرون RF "
                "إيجابياً منخفضاً.</li>"
                "<li><strong>التدخين:</strong> التدخين المزمن قد يحفّز إنتاج RF ويزيد خطر التهاب المفاصل "
                "الروماتويدي.</li>"
                "</ul>"
                "<p>لتحديد السبب، قد يطلب الطبيب <strong>anti-CCP</strong> وANA وتعداد دم كامل وCRP "
                "وسرعة ترسيب وسيرولوجيا التهاب الكبد.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كانت نتيجة <strong>تحليل RF في الدم</strong> إيجابية، فلا تقلق لكن راجع طبيب "
                "أمراض الروماتيزم&mdash;خصوصاً إذا كان مستوى RF أعلى من 50 IU/mL، أو إذا كنت تعاني من "
                "آلام المفاصل أو تيبّس صباحي يستمر أكثر من 30 دقيقة أو تورّم المفاصل أو إرهاق غير مفسّر "
                "أو جفاف الفم والعينين.</p>"
                "<p>نظراً لأن RF الإيجابي المنخفض قد يحدث أيضاً لدى أشخاص أصحاء، خاصة كبار السن والمدخنين، "
                "فإن RF الإيجابي وحده لا يؤكد التشخيص. سيُجري طبيبك فحصاً سريرياً ويأخذ تاريخاً مرضياً "
                "مفصلاً ويطلب anti-CCP وتصويراً وفحوصات مخبرية إضافية. التشخيص المبكر لالتهاب المفاصل "
                "الروماتويدي ضروري لمنع تلف المفاصل وتشوّهها.</p>"
                "<p>تذكّر: <strong>نتائج تحليل RF</strong> ليست سوى أداة فحص أولية. ليس كل من يظهر RF "
                "إيجابياً مصاباً بالتهاب المفاصل الروماتويدي، والنتيجة السلبية لا تستبعده تماماً (RA سلبية "
                "المصل). إذا استمرت أعراضك، فإن المتابعة المنتظمة وإعادة الفحص عند الحاجة أمران "
                "أساسيان.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_rf_sections_by_lang() -> dict:
    """Returns sections dict for RF article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_rf_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for RF article (all 9 languages)."""
    return {
        "tr": [
            {"question": "Romatoid faktör (RF) testi nedir?",
             "answer": "Romatoid faktör testi, bağışıklık sistemi tarafından üretilen ve vücudun kendi dokularına saldırabilen IgM sınıfı bir otoantikorun kanınızdaki düzeyini ölçen bir kan testidir. Başta romatoid artrit olmak üzere otoimmün hastalıkların taranmasında kullanılır."},
            {"question": "RF pozitif çıkması ne anlama gelir?",
             "answer": "RF pozitifliği romatoid artrit, Sjögren sendromu veya kronik enfeksiyonlara işaret edebilir; ancak sağlıklı bireylerin %5-10'unda da düşük düzeyde pozitiflik görülebilir. Tek başına RF pozitifliği kesin tanı koymaz; sonuç anti-CCP ve klinik bulgularla birlikte değerlendirilmelidir."},
            {"question": "RF normal değeri kaçtır?",
             "answer": "Çoğu laboratuvarda RF normal değeri 14 IU/mL'nin altıdır (negatif). 14-50 IU/mL düşük pozitiflik, 51-100 orta pozitiflik, 100 üzeri yüksek pozitiflik olarak değerlendirilir."},
        ],
        "en": [
            {"question": "What is a rheumatoid factor (RF) test?",
             "answer": "A rheumatoid factor test measures the level of RF, an IgM-class autoantibody, in your blood. It is used to screen for autoimmune diseases, particularly rheumatoid arthritis, and is often ordered alongside the anti-CCP antibody test."},
            {"question": "What does a positive rheumatoid factor mean?",
             "answer": "A positive RF may indicate rheumatoid arthritis, Sjögren's syndrome, or chronic infections such as hepatitis C. However, 5–10% of healthy individuals, especially the elderly, may test positive at low levels. A positive RF alone does not confirm a diagnosis and must be evaluated with clinical findings and anti-CCP."},
            {"question": "What is the normal range for rheumatoid factor?",
             "answer": "In most laboratories the normal RF level is below 14 IU/mL (negative). Values of 14–50 IU/mL are low positive, 51–100 moderate positive, and above 100 high positive."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de factor reumatoide (FR)?",
             "answer": "La prueba de factor reumatoide mide el nivel de FR, un autoanticuerpo de clase IgM, en la sangre. Se utiliza para detectar enfermedades autoinmunes, especialmente la artritis reumatoide, y suele solicitarse junto con el anticuerpo anti-CCP."},
            {"question": "¿Qué significa un factor reumatoide positivo?",
             "answer": "Un FR positivo puede indicar artritis reumatoide, síndrome de Sjögren o infecciones crónicas como la hepatitis C. Sin embargo, el 5–10 % de las personas sanas puede dar positivo a niveles bajos. Un FR positivo por sí solo no confirma diagnóstico."},
            {"question": "¿Cuál es el valor normal del factor reumatoide?",
             "answer": "En la mayoría de los laboratorios el valor normal de FR es inferior a 14 IU/mL (negativo). Valores de 14–50 son positivo bajo, 51–100 positivo moderado y superior a 100 positivo alto."},
        ],
        "de": [
            {"question": "Was ist ein Rheumafaktor (RF)-Test?",
             "answer": "Der Rheumafaktor-Test misst den RF-Spiegel, einen IgM-Autoantikörper, im Blut. Er wird zum Screening auf Autoimmunerkrankungen, insbesondere rheumatoide Arthritis, eingesetzt und oft zusammen mit dem Anti-CCP-Antikörper bestimmt."},
            {"question": "Was bedeutet ein positiver Rheumafaktor?",
             "answer": "Ein positiver RF kann auf rheumatoide Arthritis, Sjögren-Syndrom oder chronische Infektionen wie Hepatitis C hinweisen. Allerdings sind 5–10 % der gesunden Personen bei niedrigen Spiegeln ebenfalls RF-positiv. Ein positiver RF allein bestätigt keine Diagnose."},
            {"question": "Was ist der Normalwert für Rheumafaktor?",
             "answer": "In den meisten Laboren gilt ein RF-Wert unter 14 IU/mL als normal (negativ). Werte von 14–50 sind niedrig positiv, 51–100 mäßig positiv und über 100 hoch positiv."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test du facteur rhumatoïde (FR) ?",
             "answer": "Le test du facteur rhumatoïde mesure le taux de FR, un auto-anticorps de classe IgM, dans le sang. Il est utilisé pour dépister les maladies auto-immunes, en particulier la polyarthrite rhumatoïde, et est souvent prescrit avec l'anticorps anti-CCP."},
            {"question": "Que signifie un facteur rhumatoïde positif ?",
             "answer": "Un FR positif peut indiquer une polyarthrite rhumatoïde, un syndrome de Sjögren ou des infections chroniques comme l'hépatite C. Cependant, 5 à 10 % des personnes en bonne santé peuvent être positives à de faibles niveaux. Un FR positif seul ne confirme pas un diagnostic."},
            {"question": "Quelle est la valeur normale du facteur rhumatoïde ?",
             "answer": "Dans la plupart des laboratoires, la valeur normale du FR est inférieure à 14 UI/mL (négatif). Des valeurs de 14–50 sont faiblement positives, 51–100 modérément positives et au-dessus de 100 fortement positives."},
        ],
        "it": [
            {"question": "Cos'è il test del fattore reumatoide (FR)?",
             "answer": "Il test del fattore reumatoide misura il livello di FR, un autoanticorpo di classe IgM, nel sangue. Viene utilizzato per lo screening di malattie autoimmuni, in particolare l'artrite reumatoide, e spesso viene richiesto insieme all'anticorpo anti-CCP."},
            {"question": "Cosa significa un fattore reumatoide positivo?",
             "answer": "Un FR positivo può indicare artrite reumatoide, sindrome di Sjögren o infezioni croniche come l'epatite C. Tuttavia, il 5–10 % delle persone sane può risultare positivo a livelli bassi. Un FR positivo da solo non conferma una diagnosi."},
            {"question": "Qual è il valore normale del fattore reumatoide?",
             "answer": "Nella maggior parte dei laboratori il valore normale del FR è inferiore a 14 UI/mL (negativo). Valori di 14–50 sono basso positivo, 51–100 moderato positivo e oltre 100 alto positivo."},
        ],
        "he": [
            {"question": "מהי בדיקת גורם שגרוני (RF)?",
             "answer": "בדיקת גורם שגרוני מודדת את רמת ה-RF, נוגדן עצמי מסוג IgM, בדם. היא משמשת לסקירה של מחלות אוטואימוניות, בעיקר דלקת מפרקים שגרונית, ולעתים קרובות מוזמנת יחד עם הנוגדן anti-CCP."},
            {"question": "מה המשמעות של RF חיובי?",
             "answer": "RF חיובי עשוי להצביע על דלקת מפרקים שגרונית, תסמונת שגרן או זיהומים כרוניים כמו הפטיטיס C. עם זאת, 5–10% מהאנשים הבריאים עשויים להיות חיוביים ברמות נמוכות. RF חיובי לבדו אינו מאשר אבחנה."},
            {"question": "מהו הערך התקין של גורם שגרוני?",
             "answer": "ברוב המעבדות ערך RF תקין הוא מתחת ל-14 IU/mL (שלילי). ערכים של 14–50 הם חיובי נמוך, 51–100 חיובי בינוני ומעל 100 חיובי גבוה."},
        ],
        "hi": [
            {"question": "रुमेटॉइड फ़ैक्टर (RF) टेस्ट क्या है?",
             "answer": "रुमेटॉइड फ़ैक्टर टेस्ट रक्त में RF, एक IgM वर्ग के ऑटोएंटीबॉडी, के स्तर को मापता है। इसका उपयोग ऑटोइम्यून बीमारियों, विशेषकर रुमेटॉइड आर्थराइटिस की स्क्रीनिंग के लिए किया जाता है और अक्सर anti-CCP एंटीबॉडी टेस्ट के साथ किया जाता है।"},
            {"question": "RF पॉज़िटिव होने का क्या मतलब है?",
             "answer": "RF पॉज़िटिव रुमेटॉइड आर्थराइटिस, शोग्रेन सिंड्रोम या हेपेटाइटिस C जैसे क्रोनिक संक्रमण का संकेत हो सकता है। हालांकि, 5–10% स्वस्थ लोगों में भी कम स्तर पर पॉज़िटिव रिज़ल्ट आता है। अकेले RF पॉज़िटिव निदान की पुष्टि नहीं करता।"},
            {"question": "RF का सामान्य मान क्या है?",
             "answer": "अधिकांश प्रयोगशालाओं में सामान्य RF स्तर 14 IU/mL से कम (नेगेटिव) होता है। 14–50 कम पॉज़िटिव, 51–100 मध्यम पॉज़िटिव और 100 से अधिक उच्च पॉज़िटिव माना जाता है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل عامل الروماتويد (RF)؟",
             "answer": "تحليل عامل الروماتويد يقيس مستوى RF، وهو جسم مضاد ذاتي من نوع IgM، في الدم. يُستخدم لفحص الأمراض المناعية الذاتية، خاصة التهاب المفاصل الروماتويدي، وغالباً يُطلب مع الجسم المضاد anti-CCP."},
            {"question": "ماذا يعني عامل الروماتويد الإيجابي؟",
             "answer": "قد يشير RF الإيجابي إلى التهاب المفاصل الروماتويدي أو متلازمة شوغرن أو عدوى مزمنة مثل التهاب الكبد C. إلا أن 5–10% من الأصحاء قد يظهرون إيجابية عند مستويات منخفضة. RF الإيجابي وحده لا يؤكد التشخيص."},
            {"question": "ما هو المستوى الطبيعي لعامل الروماتويد؟",
             "answer": "في معظم المختبرات يُعتبر مستوى RF الطبيعي أقل من 14 IU/mL (سلبي). قيم 14–50 إيجابي منخفض، 51–100 إيجابي متوسط، وأكثر من 100 إيجابي مرتفع."},
        ],
    }
