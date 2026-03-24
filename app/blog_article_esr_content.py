# -*- coding: utf-8 -*-
"""
ESR (Erythrocyte Sedimentation Rate) blog article — full body content for all 9 languages.
Used by blog_i18n._article_esr().
Sections: intro, what-is-esr, how-esr-works, normal-ranges, high-esr-causes,
esr-vs-crp, false-elevations, monitoring-role, when-to-see-doctor,
how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# ENGLISH
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="High ESR: what your blood test result means",
            body_html=(
                "<p>The <strong>ESR (Erythrocyte Sedimentation Rate)</strong> is one of the oldest and simplest blood tests still in routine use. "
                "It measures how quickly red blood cells (<em>erythrocytes</em>) settle to the bottom of a vertical tube over one hour. A faster "
                "settling rate indicates that inflammation is likely present in the body&mdash;though it does not pinpoint where or why.</p>"
                "<p>Despite the availability of more specific inflammation markers such as <strong>C-reactive protein (CRP)</strong>, the ESR "
                "remains valuable because it reflects chronic, low-grade inflammatory processes that CRP may not capture as well. It is widely "
                "used to help diagnose and monitor conditions like <em>temporal arteritis</em>, <em>polymyalgia rheumatica</em>, <em>rheumatoid "
                "arthritis</em>, and <em>systemic lupus erythematosus</em>.</p>"
                "<p>This guide explains what the ESR measures, how to interpret your result, common causes of elevation, and when to seek "
                "medical attention. It is for educational purposes only and does not replace a doctor's advice.</p>"
            ),
        ),
        Section(
            id="what-is-esr", level=2,
            heading="What is ESR (Erythrocyte Sedimentation Rate)?",
            body_html=(
                "<p>The ESR is a non-specific marker of inflammation. When inflammation is present in the body, the liver increases production "
                "of certain proteins&mdash;particularly <strong>fibrinogen</strong> and <strong>immunoglobulins</strong>&mdash;that cause red blood "
                "cells to stick together and form stacks called <em>rouleaux</em>. These rouleaux are heavier than individual red blood cells and "
                "therefore settle faster in the test tube, producing a higher ESR reading.</p>"
                "<p>The test was first described in the early 1900s and standardized by Westergren in 1921. The <strong>Westergren method</strong> "
                "remains the reference standard: anticoagulated blood is drawn into a 200&nbsp;mm vertical tube, and the distance the red cells "
                "have fallen from the top after exactly 60 minutes is recorded in millimeters per hour (mm/hr).</p>"
                "<p>Because the ESR depends on changes in plasma proteins rather than detecting a specific pathogen or cytokine, it is considered "
                "a <strong>non-specific</strong> test. An elevated ESR tells your doctor that <em>something</em> is causing inflammation but "
                "requires additional investigation to determine the cause. Conversely, a normal ESR does not rule out disease entirely, as some "
                "inflammatory conditions may not elevate it significantly.</p>"
            ),
        ),
        Section(
            id="how-esr-works", level=2,
            heading="How does the ESR test work?",
            body_html=(
                "<p>The physics behind ESR are straightforward. Red blood cells normally repel each other because they carry a net negative charge "
                "on their surface (the <em>zeta potential</em>). This negative charge keeps cells dispersed in plasma, causing them to settle slowly.</p>"
                "<p>When acute-phase proteins such as fibrinogen increase during inflammation, they reduce the zeta potential between red cells, "
                "allowing cells to aggregate into rouleaux formations. These multi-cell stacks have a greater mass-to-surface-area ratio and "
                "therefore sink faster through the plasma column. The rate of sedimentation is proportional to the concentration of these "
                "aggregation-promoting proteins.</p>"
                "<p>Several factors besides inflammation can alter the ESR. Anemia increases ESR because fewer red cells create less resistance "
                "to sedimentation. Polycythemia (excess red cells) has the opposite effect, slowing sedimentation. Abnormally shaped red cells "
                "(sickle cells, spherocytes) do not form rouleaux well and tend to produce falsely low ESR values. The test is also affected by "
                "temperature, tube tilt, and time delay before processing&mdash;which is why standardized conditions are important for reliable results.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal ESR ranges",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal ESR (mm/hr)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Men &lt; 50 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Men &ge; 50 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Women &lt; 50 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Women &ge; 50 years</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr>'
                "</tbody></table>"
                "<p>A commonly used <strong>age-adjusted formula</strong> is: upper limit of normal = age/2 for men and (age+10)/2 for women. "
                "This acknowledges that ESR naturally rises with age due to increased fibrinogen levels and other plasma protein changes.</p>"
                "<p>An ESR above <strong>100&nbsp;mm/hr</strong> is considered markedly elevated and strongly suggests serious underlying disease, "
                "such as infection, malignancy, or autoimmune disease. Values between 40&ndash;100 are moderately elevated and warrant investigation. "
                "Mildly elevated values (20&ndash;40) are common and may reflect minor inflammation, aging, or obesity.</p>"
            ),
        ),
        Section(
            id="high-esr-causes", level=2,
            heading="Causes of high ESR",
            body_html=(
                "<p>An elevated ESR has a broad differential diagnosis. The most important categories include:</p>"
                "<p><strong>Infections:</strong></p>"
                "<ul>"
                "<li>Bacterial infections (pneumonia, endocarditis, osteomyelitis, tuberculosis, abscess).</li>"
                "<li>Chronic infections tend to cause higher ESR elevations than acute viral infections.</li>"
                "</ul>"
                "<p><strong>Autoimmune and inflammatory diseases:</strong></p>"
                "<ul>"
                "<li><strong>Temporal (giant cell) arteritis</strong> and <strong>polymyalgia rheumatica</strong> &ndash; ESR is a key diagnostic "
                "criterion; values often exceed 50&ndash;100&nbsp;mm/hr.</li>"
                "<li><strong>Rheumatoid arthritis</strong> &ndash; ESR correlates with disease activity.</li>"
                "<li><strong>Systemic lupus erythematosus (SLE)</strong> &ndash; ESR rises during flares, though CRP may remain normal in SLE "
                "(a useful distinguishing feature).</li>"
                "<li>Inflammatory bowel disease, vasculitis, and sarcoidosis.</li>"
                "</ul>"
                "<p><strong>Malignancies:</strong> Multiple myeloma, lymphoma, and metastatic cancers can cause markedly elevated ESR. "
                "In myeloma, the excess immunoglobulins strongly promote rouleaux formation.</p>"
                "<p><strong>Other causes:</strong> Anemia, pregnancy (ESR normally rises in the second and third trimester), end-stage renal "
                "disease, heart failure, obesity, and advanced age.</p>"
            ),
        ),
        Section(
            id="esr-vs-crp", level=2,
            heading="ESR vs. CRP: which inflammation marker is better?",
            body_html=(
                "<p>Both ESR and CRP are markers of inflammation, but they behave differently and provide complementary information:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Feature</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">ESR</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">CRP</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Response speed</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Slow (days to change)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Fast (rises within 6&ndash;8 hours)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normalization</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Slow (weeks)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Rapid (days)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Affected by anemia</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Yes (falsely elevated)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">No</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Best for</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Chronic inflammation monitoring</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Acute infection detection</td></tr>'
                "</tbody></table>"
                "<p>In systemic lupus erythematosus, the ESR often rises while CRP remains normal&mdash;this discordance helps distinguish SLE "
                "flares from infections. For more on CRP, see our <a href=\"/blog/crp-high-meaning\">CRP guide</a>.</p>"
                "<p>In practice, many clinicians order both tests together to get a more complete picture of a patient's inflammatory status.</p>"
            ),
        ),
        Section(
            id="false-elevations", level=2,
            heading="False elevations and limitations of ESR",
            body_html=(
                "<p>Because ESR depends on red blood cell behavior and plasma protein composition, several non-inflammatory conditions can "
                "falsely elevate the result:</p>"
                "<ul>"
                "<li><strong>Anemia</strong> &ndash; lower hematocrit means less resistance to sedimentation, producing a falsely high ESR "
                "even without inflammation.</li>"
                "<li><strong>Obesity</strong> &ndash; adipose tissue produces pro-inflammatory cytokines that mildly elevate ESR.</li>"
                "<li><strong>Aging</strong> &ndash; ESR rises 1&ndash;2&nbsp;mm/hr per decade of age due to increasing fibrinogen.</li>"
                "<li><strong>Female sex</strong> &ndash; women tend to have higher ESR than men.</li>"
                "<li><strong>Pregnancy</strong> &ndash; physiological increase in fibrinogen and plasma volume.</li>"
                "<li><strong>Kidney failure</strong> &ndash; uremia alters plasma proteins.</li>"
                "<li><strong>Hypergammaglobulinemia</strong> &ndash; high immunoglobulins (as in myeloma or liver disease) strongly promote "
                "rouleaux formation.</li>"
                "</ul>"
                "<p>Conditions that can <strong>falsely lower</strong> ESR include polycythemia, sickle cell disease, spherocytosis, "
                "extreme leukocytosis, and certain protein abnormalities. Clinicians must interpret ESR in the context of the patient's "
                "overall clinical picture.</p>"
            ),
        ),
        Section(
            id="monitoring-role", level=2,
            heading="The role of ESR in disease monitoring",
            body_html=(
                "<p>While ESR has limited value as a screening tool in asymptomatic patients, it is extremely useful for monitoring disease "
                "activity over time in conditions where it is known to correlate with clinical status:</p>"
                "<ul>"
                "<li><strong>Temporal arteritis / polymyalgia rheumatica</strong> &ndash; ESR is followed serially during treatment with "
                "corticosteroids. A rising ESR may indicate relapse.</li>"
                "<li><strong>Rheumatoid arthritis</strong> &ndash; ESR is part of composite disease activity scores (DAS28). Declining ESR "
                "suggests treatment is working.</li>"
                "<li><strong>Infections</strong> &ndash; ESR tracks the response to antibiotic therapy in chronic infections like osteomyelitis "
                "or endocarditis.</li>"
                "<li><strong>Hodgkin lymphoma</strong> &ndash; ESR is an independent prognostic factor; high ESR at diagnosis is associated with "
                "worse outcomes.</li>"
                "</ul>"
                "<p>Because ESR changes slowly, it is best suited for tracking chronic conditions rather than acute changes. CRP is preferred "
                "when rapid response to treatment needs to be assessed. The combination of both markers provides the most informative longitudinal "
                "tracking of inflammatory disease.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult your doctor about an elevated ESR in the following situations:</p>"
                "<ul>"
                "<li>Your ESR is <strong>above the age-adjusted normal range</strong> and you have unexplained symptoms such as fatigue, weight loss, "
                "fever, or joint pain.</li>"
                "<li>Your ESR is <strong>above 100&nbsp;mm/hr</strong>&mdash;this strongly suggests serious underlying disease and requires prompt evaluation.</li>"
                "<li>You have been diagnosed with an <strong>autoimmune or inflammatory condition</strong> and your ESR is rising despite treatment.</li>"
                "<li>You have <strong>new-onset severe headache, jaw claudication, or visual changes</strong> in patients over 50&mdash;these may "
                "indicate temporal arteritis, a medical emergency.</li>"
                "<li>You have <strong>persistent unexplained anemia</strong> with high ESR, which may suggest multiple myeloma or other malignancy.</li>"
                "</ul>"
                "<p>A mildly elevated ESR in an otherwise healthy person may not require immediate action but should be noted and rechecked "
                "if symptoms develop. Context is everything when interpreting this test.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your ESR results",
            body_html=(
                "<p>Understanding your ESR result alongside other blood markers can be challenging. <strong>Norya</strong> simplifies this: "
                "upload your blood test results and receive a clear, structured health summary within minutes. Norya evaluates your ESR in the "
                "context of CRP, complete blood count, and other inflammation markers to help you see the full picture.</p>"
                "<p>The report highlights abnormal values, explains their significance in plain language, and helps you prepare the right "
                "questions for your doctor. <a href=\"/analyze\">Start your free analysis with Norya</a>.</p>"
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
# TURKISH
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Yüksek sedimentasyon (ESR): kan testi sonucunuz ne anlama geliyor?",
            body_html=(
                "<p><strong>ESR (Eritrosit Sedimentasyon Hızı)</strong>, hâlâ rutin kullanımda olan en eski ve en basit kan testlerinden biridir. "
                "Kırmızı kan hücrelerinin (<em>eritrositlerin</em>) bir saat içinde dikey bir tüpün dibine ne kadar hızlı çöktüğünü ölçer. "
                "Daha hızlı çökme, vücutta iltihabın muhtemelen mevcut olduğunu gösterir&mdash;ancak nerede veya neden olduğunu belirtmez.</p>"
                "<p><strong>C-reaktif protein (CRP)</strong> gibi daha spesifik iltihap belirteçlerinin mevcut olmasına rağmen ESR değerli olmaya "
                "devam etmektedir çünkü CRP'nin yeterince yansıtamadığı kronik, düşük dereceli iltihabi süreçleri gösterir. <em>Temporal arterit</em>, "
                "<em>polimiyalji romatika</em>, <em>romatoid artrit</em> ve <em>sistemik lupus eritematozus</em> gibi durumların tanı ve takibinde "
                "yaygın olarak kullanılır.</p>"
                "<p>Bu rehber ESR'nin ne ölçtüğünü, sonucunuzun nasıl yorumlanacağını, yükselme nedenlerini ve ne zaman tıbbi yardım almanız "
                "gerektiğini açıklar. Yalnızca eğitim amaçlıdır.</p>"
            ),
        ),
        Section(
            id="what-is-esr", level=2,
            heading="ESR (Eritrosit Sedimentasyon Hızı) nedir?",
            body_html=(
                "<p>ESR, spesifik olmayan bir iltihap belirtecidir. Vücutta iltihap olduğunda karaciğer, kırmızı kan hücrelerinin birbirine "
                "yapışıp <em>rulo</em> adı verilen yığınlar oluşturmasına neden olan <strong>fibrinojen</strong> ve <strong>immünoglobulinler</strong> "
                "gibi belirli proteinlerin üretimini artırır. Bu rulolar bireysel kırmızı kan hücrelerinden daha ağırdır ve test tüpünde daha hızlı çöker.</p>"
                "<p>Test ilk kez 1900'lerin başında tanımlanmış ve 1921'de Westergren tarafından standartlaştırılmıştır. <strong>Westergren yöntemi</strong> "
                "referans standart olarak kalmaktadır: antikoagüle edilmiş kan 200&nbsp;mm'lik dikey bir tüpe çekilir ve tam 60 dakika sonra kırmızı "
                "hücrelerin tepeden ne kadar düştüğü milimetre/saat (mm/sa) olarak kaydedilir.</p>"
                "<p>ESR belirli bir patojen veya sitokin tespit etmek yerine plazma proteinlerindeki değişikliklere dayandığından <strong>spesifik "
                "olmayan</strong> bir test olarak kabul edilir. Yüksek ESR doktorunuza <em>bir şeyin</em> iltihaplanmaya neden olduğunu söyler ancak "
                "nedenin belirlenmesi için ek araştırma gerektirir.</p>"
            ),
        ),
        Section(
            id="how-esr-works", level=2,
            heading="ESR testi nasıl çalışır?",
            body_html=(
                "<p>ESR'nin arkasındaki fizik basittir. Kırmızı kan hücreleri normalde yüzeylerinde net negatif bir yük (<em>zeta potansiyeli</em>) "
                "taşıdıkları için birbirlerini iterler. Bu negatif yük hücreleri plazmada dağınık tutar ve yavaş çökmelerine neden olur.</p>"
                "<p>İltihap sırasında fibrinojen gibi akut faz proteinleri arttığında, kırmızı hücreler arasındaki zeta potansiyelini azaltarak "
                "hücrelerin rulo formasyonlarına toplanmasına izin verirler. Bu çok hücreli yığınlar daha büyük kütle-yüzey oranına sahiptir ve "
                "bu nedenle plazma sütununda daha hızlı çökerler.</p>"
                "<p>İltihabın yanı sıra çeşitli faktörler ESR'yi değiştirebilir. Anemi, daha az kırmızı hücre nedeniyle ESR'yi artırır. "
                "Polisitemi (fazla kırmızı hücre) ise sedimentasyonu yavaşlatır. Orak hücreler ve sferositler gibi anormal şekilli kırmızı "
                "hücreler rulo oluşturamaz ve yanlış düşük ESR değerleri üretme eğilimindedir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal ESR aralıkları",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal ESR (mm/sa)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkekler &lt; 50 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkekler &ge; 50 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadınlar &lt; 50 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadınlar &ge; 50 yaş</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr>'
                "</tbody></table>"
                "<p>Yaygın olarak kullanılan <strong>yaşa göre düzeltilmiş formül</strong>: üst normal sınır = erkeklerde yaş/2, kadınlarda (yaş+10)/2.</p>"
                "<p><strong>100&nbsp;mm/sa</strong> üzerinde bir ESR belirgin şekilde yükselmiş kabul edilir ve enfeksiyon, malignite veya otoimmün "
                "hastalık gibi ciddi bir altta yatan hastalığı kuvvetle düşündürür. 40&ndash;100 arası değerler orta derecede yüksektir ve araştırma gerektirir.</p>"
            ),
        ),
        Section(
            id="high-esr-causes", level=2,
            heading="Yüksek ESR nedenleri",
            body_html=(
                "<p>Yüksek ESR'nin geniş bir ayırıcı tanısı vardır:</p>"
                "<p><strong>Enfeksiyonlar:</strong> Bakteriyel enfeksiyonlar (pnömoni, endokardit, osteomiyelit, tüberküloz). Kronik enfeksiyonlar "
                "akut viral enfeksiyonlardan daha yüksek ESR yükselmelerine neden olma eğilimindedir.</p>"
                "<p><strong>Otoimmün ve inflamatuar hastalıklar:</strong></p>"
                "<ul>"
                "<li><strong>Temporal (dev hücreli) arterit</strong> ve <strong>polimiyalji romatika</strong> &ndash; ESR kilit tanı kriteridir; değerler genellikle 50&ndash;100&nbsp;mm/sa'ı aşar.</li>"
                "<li><strong>Romatoid artrit</strong> &ndash; ESR hastalık aktivitesiyle koreledir.</li>"
                "<li><strong>Sistemik lupus eritematozus (SLE)</strong> &ndash; alevlenmelerde ESR yükselirken CRP normal kalabilir.</li>"
                "<li>İnflamatuar bağırsak hastalığı, vaskülit ve sarkoidoz.</li>"
                "</ul>"
                "<p><strong>Malignansiler:</strong> Multipl miyelom, lenfoma ve metastatik kanserler. <strong>Diğer nedenler:</strong> Anemi, gebelik, "
                "son dönem böbrek yetmezliği, kalp yetmezliği, obezite ve ileri yaş.</p>"
            ),
        ),
        Section(
            id="esr-vs-crp", level=2,
            heading="ESR ve CRP: hangi iltihap belirteci daha iyi?",
            body_html=(
                "<p>Her iki belirteç de iltihabı gösterir ancak farklı davranır ve tamamlayıcı bilgi sağlar:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Özellik</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">ESR</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">CRP</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Yanıt hızı</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Yavaş (değişmesi günler alır)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hızlı (6&ndash;8 saat içinde yükselir)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Normalleşme</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Yavaş (haftalar)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hızlı (günler)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Anemiden etkilenir mi?</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Evet (yanlış yüksek)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hayır</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">En uygun kullanım</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Kronik iltihap takibi</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Akut enfeksiyon tespiti</td></tr>'
                "</tbody></table>"
                "<p>SLE'de ESR yükselirken CRP normal kalabilir&mdash;bu uyumsuzluk SLE alevlenmelerini enfeksiyonlardan ayırmaya yardımcı olur. "
                "CRP hakkında daha fazla bilgi için <a href=\"/blog/crp-high-meaning\">CRP rehberimize</a> bakın.</p>"
            ),
        ),
        Section(
            id="false-elevations", level=2,
            heading="ESR'de yanlış yükselmeler ve sınırlamalar",
            body_html=(
                "<p>ESR kırmızı kan hücresi davranışına ve plazma protein bileşimine bağlı olduğundan, iltihapsız çeşitli durumlar sonucu yanlış "
                "yükseltebilir:</p>"
                "<ul>"
                "<li><strong>Anemi</strong> &ndash; düşük hematokrit sedimentasyona daha az direnç anlamına gelir.</li>"
                "<li><strong>Obezite</strong> &ndash; yağ dokusu pro-inflamatuar sitokinler üretir.</li>"
                "<li><strong>Yaşlanma</strong> &ndash; ESR artan fibrinojen nedeniyle on yılda 1&ndash;2&nbsp;mm/sa artar.</li>"
                "<li><strong>Kadın cinsiyet</strong> &ndash; kadınlar erkeklerden daha yüksek ESR'ye sahip olma eğilimindedir.</li>"
                "<li><strong>Gebelik</strong> &ndash; fizyolojik fibrinojen ve plazma hacmi artışı.</li>"
                "<li><strong>Böbrek yetmezliği</strong> &ndash; üremi plazma proteinlerini değiştirir.</li>"
                "</ul>"
                "<p>ESR'yi <strong>yanlış düşürebilecek</strong> durumlar: polisitemi, orak hücre hastalığı, sferositoz ve aşırı lökositoz.</p>"
            ),
        ),
        Section(
            id="monitoring-role", level=2,
            heading="ESR'nin hastalık takibindeki rolü",
            body_html=(
                "<p>ESR, asemptomatik hastalarda tarama aracı olarak sınırlı değere sahip olsa da klinik durumla korelasyon gösterdiği bilinen "
                "hastalıklarda aktivite takibinde son derece yararlıdır:</p>"
                "<ul>"
                "<li><strong>Temporal arterit / polimiyalji romatika</strong> &ndash; kortikosteroid tedavisi sırasında seri takip.</li>"
                "<li><strong>Romatoid artrit</strong> &ndash; ESR, DAS28 gibi kompozit hastalık aktivite skorlarının bir parçasıdır.</li>"
                "<li><strong>Enfeksiyonlar</strong> &ndash; osteomiyelit veya endokardit gibi kronik enfeksiyonlarda antibiyotik tedavisine yanıtı izler.</li>"
                "<li><strong>Hodgkin lenfoma</strong> &ndash; ESR bağımsız bir prognostik faktördür.</li>"
                "</ul>"
                "<p>ESR yavaş değiştiğinden, akut değişikliklerden ziyade kronik durumları takip etmeye en uygunudur.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda yüksek ESR hakkında doktorunuza danışın:</p>"
                "<ul>"
                "<li>ESR'niz <strong>yaşa göre düzeltilmiş normal aralığın üzerinde</strong> ve yorgunluk, kilo kaybı, ateş veya eklem ağrısı gibi açıklanamayan belirtileriniz var.</li>"
                "<li>ESR'niz <strong>100&nbsp;mm/sa'nın üzerinde</strong>&mdash;bu ciddi altta yatan hastalığı kuvvetle düşündürür.</li>"
                "<li><strong>Otoimmün veya inflamatuar hastalık</strong> tanınız var ve tedaviye rağmen ESR'niz yükseliyor.</li>"
                "<li>50 yaş üstü hastalarda <strong>yeni başlayan şiddetli baş ağrısı, çene kladikasyonu veya görme değişiklikleri</strong>&mdash;temporal arteriti düşündürebilir.</li>"
                "<li>Yüksek ESR ile birlikte <strong>açıklanamayan anemi</strong>&mdash;multipl miyelom düşündürebilir.</li>"
                "</ul>"
                "<p>Sağlıklı bir kişide hafif yüksek ESR acil müdahale gerektirmeyebilir ancak belirtiler gelişirse yeniden kontrol edilmelidir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya ESR sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>ESR sonucunuzu diğer kan belirteçleriyle birlikte anlamak zor olabilir. <strong>Norya</strong> bunu basitleştirir: "
                "kan testi sonuçlarınızı yükleyin ve dakikalar içinde net, yapılandırılmış bir sağlık özeti alın. Norya, ESR'nizi CRP, "
                "tam kan sayımı ve diğer iltihap belirteçleriyle birlikte değerlendirir.</p>"
                "<p>Rapor anormal değerleri vurgular, anlaşılır dilde açıklar ve doktor ziyaretiniz için hazırlanmanıza yardımcı olur. "
                "<a href=\"/analyze\">Norya ile ücretsiz analizinizi başlatın</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                'Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. <a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# SPANISH
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="VSG elevada: qué significa su resultado de análisis de sangre",
                body_html="<p>La <strong>VSG (Velocidad de Sedimentación Globular)</strong> es una de las pruebas de sangre más antiguas y sencillas. Mide la rapidez con la que los glóbulos rojos se depositan en el fondo de un tubo vertical en una hora. Una velocidad más rápida indica inflamación en el cuerpo.</p><p>A pesar de marcadores más específicos como la <strong>proteína C reactiva (PCR)</strong>, la VSG sigue siendo valiosa para procesos inflamatorios crónicos. Se usa ampliamente en el diagnóstico y seguimiento de arteritis temporal, polimialgia reumática, artritis reumatoide y lupus.</p><p>Esta guía es educativa y no sustituye el consejo médico.</p>"),
        Section(id="what-is-esr", level=2, heading="¿Qué es la VSG?",
                body_html="<p>La VSG es un marcador inespecífico de inflamación. Cuando hay inflamación, el hígado aumenta la producción de <strong>fibrinógeno</strong> e <strong>inmunoglobulinas</strong>, que hacen que los glóbulos rojos se apilen en formaciones llamadas <em>rouleaux</em>. Estos son más pesados y sedimentan más rápido.</p><p>El método de <strong>Westergren</strong> es el estándar de referencia. La VSG no indica dónde ni por qué hay inflamación; requiere investigación adicional.</p>"),
        Section(id="how-esr-works", level=2, heading="¿Cómo funciona la prueba de VSG?",
                body_html="<p>Los glóbulos rojos tienen una carga negativa neta (<em>potencial zeta</em>) que los mantiene dispersos en el plasma. Las proteínas de fase aguda como el fibrinógeno reducen este potencial, permitiendo la formación de rouleaux que sedimentan más rápido.</p><p>La anemia aumenta la VSG falsamente. La policitemia la disminuye. Las células falciformes y esferocitos no forman rouleaux adecuadamente.</p>"),
        Section(id="normal-ranges", level=2, heading="Rangos normales de VSG",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">VSG normal (mm/h)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres &lt; 50 años</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres &ge; 50 años</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres &lt; 50 años</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres &ge; 50 años</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr></tbody></table><p>Una VSG superior a <strong>100&nbsp;mm/h</strong> sugiere fuertemente enfermedad grave subyacente.</p>'),
        Section(id="high-esr-causes", level=2, heading="Causas de VSG elevada",
                body_html="<p><strong>Infecciones:</strong> neumonía, endocarditis, tuberculosis. <strong>Enfermedades autoinmunes:</strong> arteritis temporal, polimialgia reumática, artritis reumatoide, lupus. <strong>Neoplasias:</strong> mieloma múltiple, linfoma. <strong>Otros:</strong> anemia, embarazo, insuficiencia renal, obesidad, edad avanzada.</p>"),
        Section(id="esr-vs-crp", level=2, heading="VSG vs. PCR",
                body_html="<p>La VSG responde lentamente (días) y se normaliza en semanas; ideal para inflamación crónica. La PCR responde rápidamente (6-8 horas) y se normaliza en días; ideal para infección aguda. En el lupus, la VSG sube mientras la PCR puede permanecer normal. Para más información, consulte nuestra <a href=\"/blog/crp-high-meaning\">guía de PCR</a>.</p>"),
        Section(id="false-elevations", level=2, heading="Falsas elevaciones y limitaciones de la VSG",
                body_html="<p>La anemia, la obesidad, el envejecimiento, el embarazo, la insuficiencia renal y la hipergammaglobulinemia pueden elevar falsamente la VSG. La policitemia, la drepanocitosis y la esferocitosis pueden disminuirla falsamente.</p>"),
        Section(id="monitoring-role", level=2, heading="Papel de la VSG en el seguimiento de enfermedades",
                body_html="<p>La VSG es extremadamente útil para monitorizar la actividad de la arteritis temporal, la artritis reumatoide (parte del DAS28), infecciones crónicas y linfoma de Hodgkin. Como cambia lentamente, es más adecuada para condiciones crónicas.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Cuándo consultar al médico",
                body_html="<p>Consulte si: VSG por encima del rango normal ajustado por edad con síntomas inexplicables; VSG &gt;100 mm/h; enfermedad autoinmune con VSG en aumento; cefalea intensa de inicio reciente en mayores de 50 (posible arteritis temporal); o anemia inexplicable con VSG alta.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo Norya le ayuda a entender sus resultados de VSG",
                body_html="<p><strong>Norya</strong> simplifica la interpretación: suba sus resultados y reciba un resumen de salud claro en minutos. <a href=\"/analyze\">Inicie su análisis con Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Hohe BSG: Was Ihr Blutergebnis bedeutet",
                body_html="<p>Die <strong>BSG (Blutsenkungsgeschwindigkeit)</strong> misst, wie schnell rote Blutkörperchen in einem vertikalen Röhrchen sedimentieren. Eine schnellere Senkung deutet auf Entzündung hin.</p><p>Trotz spezifischerer Marker wie <strong>CRP</strong> bleibt die BSG wertvoll für chronische Entzündungsprozesse. Sie wird zur Diagnose und Überwachung von Riesenzellarteriitis, Polymyalgia rheumatica, rheumatoider Arthritis und Lupus verwendet.</p>"),
        Section(id="what-is-esr", level=2, heading="Was ist die BSG?",
                body_html="<p>Die BSG ist ein unspezifischer Entzündungsmarker. Fibrinogen und Immunglobuline lassen Erythrozyten <em>Rouleaux</em> bilden, die schneller sedimentieren. Die <strong>Westergren-Methode</strong> ist der Referenzstandard.</p>"),
        Section(id="how-esr-works", level=2, heading="Wie funktioniert die BSG?",
                body_html="<p>Erythrozyten tragen eine negative Ladung (Zetapotenzial), die sie in Suspension hält. Akute-Phase-Proteine verringern dieses Potenzial und ermöglichen die Rouleaux-Bildung. Anämie erhöht die BSG falsch, Polyzythämie verringert sie.</p>"),
        Section(id="normal-ranges", level=2, heading="Normale BSG-Werte",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normale BSG (mm/h)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer &lt; 50 Jahre</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer &ge; 50 Jahre</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frauen &lt; 50 Jahre</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frauen &ge; 50 Jahre</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr></tbody></table><p>BSG über <strong>100&nbsp;mm/h</strong> deutet stark auf schwere Grunderkrankung hin.</p>'),
        Section(id="high-esr-causes", level=2, heading="Ursachen einer hohen BSG",
                body_html="<p><strong>Infektionen:</strong> Pneumonie, Endokarditis, Tuberkulose. <strong>Autoimmunerkrankungen:</strong> Riesenzellarteriitis, Polymyalgia rheumatica, rheumatoide Arthritis, SLE. <strong>Malignome:</strong> Multiples Myelom, Lymphom. <strong>Sonstige:</strong> Anämie, Schwangerschaft, Niereninsuffizienz, Adipositas.</p>"),
        Section(id="esr-vs-crp", level=2, heading="BSG vs. CRP",
                body_html="<p>BSG reagiert langsam und eignet sich für chronische Entzündungen. CRP reagiert schnell und eignet sich für akute Infektionen. Bei SLE steigt die BSG, während CRP normal bleiben kann. Siehe unseren <a href=\"/blog/crp-high-meaning\">CRP-Leitfaden</a>.</p>"),
        Section(id="false-elevations", level=2, heading="Falsche Erhöhungen und Einschränkungen",
                body_html="<p>Anämie, Adipositas, Alter, Schwangerschaft, Nierenversagen und Hypergammaglobulinämie können die BSG falsch erhöhen. Polyzythämie und Sichelzellkrankheit können sie falsch senken.</p>"),
        Section(id="monitoring-role", level=2, heading="Rolle der BSG bei der Krankheitsüberwachung",
                body_html="<p>Die BSG ist wertvoll zur Überwachung von Riesenzellarteriitis, rheumatoider Arthritis (Teil des DAS28), chronischen Infektionen und Hodgkin-Lymphom.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann Sie einen Arzt aufsuchen sollten",
                body_html="<p>Konsultieren Sie Ihren Arzt bei: BSG über dem altersangepassten Normalbereich mit unerklärlichen Symptomen; BSG &gt;100&nbsp;mm/h; Autoimmunerkrankung mit steigender BSG; neuen starken Kopfschmerzen ab 50 Jahren (mögliche Riesenzellarteriitis).</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie Norya Ihnen hilft, Ihre BSG-Ergebnisse zu verstehen",
                body_html="<p><strong>Norya</strong> vereinfacht die Interpretation: Laden Sie Ihre Blutergebnisse hoch und erhalten Sie in Minuten einen klaren Gesundheitsbericht. <a href=\"/analyze\">Starten Sie Ihre Analyse mit Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="VS élevée : que signifie votre résultat d'analyse de sang ?",
                body_html="<p>La <strong>VS (Vitesse de Sédimentation)</strong> mesure la rapidité avec laquelle les globules rouges sédimentent au fond d'un tube vertical. Une vitesse plus rapide indique une inflammation.</p><p>Malgré des marqueurs plus spécifiques comme la <strong>CRP</strong>, la VS reste utile pour les processus inflammatoires chroniques. Ce guide est éducatif et ne remplace pas un avis médical.</p>"),
        Section(id="what-is-esr", level=2, heading="Qu'est-ce que la VS ?",
                body_html="<p>La VS est un marqueur non spécifique d'inflammation. Le fibrinogène et les immunoglobulines font que les globules rouges forment des <em>rouleaux</em> qui sédimentent plus vite. La <strong>méthode de Westergren</strong> est la référence.</p>"),
        Section(id="how-esr-works", level=2, heading="Comment fonctionne le test de VS ?",
                body_html="<p>Les globules rouges ont une charge négative (potentiel zêta) qui les maintient en suspension. Les protéines de phase aiguë réduisent ce potentiel, permettant la formation de rouleaux. L'anémie augmente faussement la VS, la polyglobulie la diminue.</p>"),
        Section(id="normal-ranges", level=2, heading="Valeurs normales de VS",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">VS normale (mm/h)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes &lt; 50 ans</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes &ge; 50 ans</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes &lt; 50 ans</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes &ge; 50 ans</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr></tbody></table><p>Une VS supérieure à <strong>100&nbsp;mm/h</strong> suggère fortement une maladie grave sous-jacente.</p>'),
        Section(id="high-esr-causes", level=2, heading="Causes d'une VS élevée",
                body_html="<p><strong>Infections :</strong> pneumonie, endocardite, tuberculose. <strong>Maladies auto-immunes :</strong> artérite temporale, polymyalgie rhumatismale, polyarthrite rhumatoïde, lupus. <strong>Cancers :</strong> myélome multiple, lymphome. <strong>Autres :</strong> anémie, grossesse, insuffisance rénale, obésité.</p>"),
        Section(id="esr-vs-crp", level=2, heading="VS vs. CRP",
                body_html="<p>La VS est lente (jours) et adaptée à l'inflammation chronique. La CRP est rapide (6-8 h) et adaptée à l'infection aiguë. Dans le lupus, la VS augmente tandis que la CRP reste souvent normale. Voir notre <a href=\"/blog/crp-high-meaning\">guide CRP</a>.</p>"),
        Section(id="false-elevations", level=2, heading="Fausses élévations et limites de la VS",
                body_html="<p>L'anémie, l'obésité, l'âge, la grossesse, l'insuffisance rénale et l'hypergammaglobulinémie peuvent faussement élever la VS. La polyglobulie et la drépanocytose peuvent la diminuer faussement.</p>"),
        Section(id="monitoring-role", level=2, heading="Rôle de la VS dans le suivi des maladies",
                body_html="<p>La VS est précieuse pour surveiller l'artérite temporale, la polyarthrite rhumatoïde (partie du DAS28), les infections chroniques et le lymphome de Hodgkin.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter un médecin",
                body_html="<p>Consultez si : VS au-dessus de la norme ajustée par l'âge avec symptômes inexpliqués ; VS &gt;100&nbsp;mm/h ; maladie auto-immune avec VS en hausse ; céphalées intenses récentes après 50 ans (artérite temporale possible).</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment Norya vous aide à comprendre vos résultats de VS",
                body_html="<p><strong>Norya</strong> simplifie l'interprétation : téléchargez vos résultats et recevez un rapport de santé clair en minutes. <a href=\"/analyze\">Commencez votre analyse avec Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="VES alta: cosa significa il risultato delle analisi del sangue",
                body_html="<p>La <strong>VES (Velocità di Eritrosedimentazione)</strong> misura la rapidità con cui i globuli rossi si depositano sul fondo di una provetta verticale. Una velocità maggiore indica infiammazione.</p><p>La VES rimane utile per i processi infiammatori cronici e il monitoraggio di arterite temporale, polimialgia reumatica, artrite reumatoide e lupus.</p>"),
        Section(id="what-is-esr", level=2, heading="Cos'è la VES?",
                body_html="<p>La VES è un marcatore aspecifico di infiammazione. Fibrinogeno e immunoglobuline fanno sì che i globuli rossi formino <em>rouleaux</em> che sedimentano più velocemente. Il <strong>metodo Westergren</strong> è lo standard di riferimento.</p>"),
        Section(id="how-esr-works", level=2, heading="Come funziona il test della VES?",
                body_html="<p>I globuli rossi hanno una carica negativa (potenziale zeta) che li mantiene dispersi nel plasma. Le proteine di fase acuta riducono questo potenziale, permettendo la formazione di rouleaux. L'anemia aumenta falsamente la VES; la policitemia la diminuisce.</p>"),
        Section(id="normal-ranges", level=2, heading="Valori normali della VES",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">VES normale (mm/h)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini &lt; 50 anni</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini &ge; 50 anni</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne &lt; 50 anni</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne &ge; 50 anni</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr></tbody></table><p>VES superiore a <strong>100&nbsp;mm/h</strong> suggerisce fortemente una malattia grave.</p>'),
        Section(id="high-esr-causes", level=2, heading="Cause di VES alta",
                body_html="<p><strong>Infezioni:</strong> polmonite, endocardite, tubercolosi. <strong>Malattie autoimmuni:</strong> arterite temporale, polimialgia reumatica, artrite reumatoide, LES. <strong>Neoplasie:</strong> mieloma multiplo, linfoma. <strong>Altro:</strong> anemia, gravidanza, insufficienza renale, obesità.</p>"),
        Section(id="esr-vs-crp", level=2, heading="VES vs. PCR",
                body_html="<p>La VES risponde lentamente ed è adatta per l'infiammazione cronica. La PCR risponde rapidamente ed è ideale per le infezioni acute. Nel lupus, la VES sale mentre la PCR può restare normale. Vedere la nostra <a href=\"/blog/crp-high-meaning\">guida PCR</a>.</p>"),
        Section(id="false-elevations", level=2, heading="False elevazioni e limiti della VES",
                body_html="<p>Anemia, obesità, età, gravidanza, insufficienza renale e ipergammaglobulinemia possono elevare falsamente la VES. Policitemia, drepanocitosi e sferocitosi possono diminuirla falsamente.</p>"),
        Section(id="monitoring-role", level=2, heading="Ruolo della VES nel monitoraggio delle malattie",
                body_html="<p>La VES è preziosa per monitorare arterite temporale, artrite reumatoide (parte del DAS28), infezioni croniche e linfoma di Hodgkin.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico",
                body_html="<p>Consultate il medico se: VES sopra il range normale aggiustato per età con sintomi inspiegabili; VES &gt;100 mm/h; malattia autoimmune con VES in aumento; cefalea intensa di nuova insorgenza dopo i 50 anni (possibile arterite temporale).</p>"),
        Section(id="how-norya-helps", level=2, heading="Come Norya ti aiuta a capire i risultati della VES",
                body_html="<p><strong>Norya</strong> semplifica l'interpretazione: caricate i risultati e ricevete un report chiaro in minuti. <a href=\"/analyze\">Iniziate l'analisi con Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="שקיעת דם (ESR) גבוהה: מה המשמעות של תוצאת בדיקת הדם שלך",
                body_html="<p><strong>ESR (קצב שקיעת אריתרוציטים)</strong> מודד את המהירות שבה כדוריות דם אדומות שוקעות לתחתית מבחנה אנכית תוך שעה. שקיעה מהירה יותר מצביעה על דלקת בגוף.</p><p>למרות זמינות סמנים ספציפיים יותר כמו <strong>CRP</strong>, ה-ESR נותר בעל ערך לתהליכים דלקתיים כרוניים. הוא נמצא בשימוש נרחב באבחון ומעקב של דלקת עורקים ענקית תאים, פולימיאלגיה ראומטיקה, דלקת מפרקים שגרונית ולופוס.</p>"),
        Section(id="what-is-esr", level=2, heading="מהו ESR?",
                body_html="<p>ESR הוא סמן דלקת לא ספציפי. פיברינוגן ואימונוגלובולינים גורמים לכדוריות אדומות ליצור <em>רולו</em> ששוקעות מהר יותר. שיטת <strong>וסטרגרן</strong> היא סטנדרט הייחוס.</p>"),
        Section(id="how-esr-works", level=2, heading="כיצד עובדת בדיקת ESR?",
                body_html="<p>כדוריות דם אדומות נושאות מטען שלילי (פוטנציאל זטא) המשמר אותן בתרחיף. חלבוני שלב חריף מפחיתים פוטנציאל זה ומאפשרים יצירת רולו. אנמיה מעלה ESR באופן שגוי; פוליציטמיה מורידה אותו.</p>"),
        Section(id="normal-ranges", level=2, heading="טווחים תקינים של ESR",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">ESR תקין (mm/hr)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים &lt; 50</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים &ge; 50</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים &lt; 50</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים &ge; 50</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr></tbody></table><p>ESR מעל <strong>100 mm/hr</strong> מרמז בחוזקה על מחלה חמורה.</p>'),
        Section(id="high-esr-causes", level=2, heading="גורמים ל-ESR גבוה",
                body_html="<p><strong>זיהומים:</strong> דלקת ריאות, אנדוקרדיטיס, שחפת. <strong>מחלות אוטואימוניות:</strong> דלקת עורקים ענקית תאים, פולימיאלגיה ראומטיקה, דלקת מפרקים שגרונית, לופוס. <strong>ממאירויות:</strong> מיאלומה, לימפומה. <strong>אחר:</strong> אנמיה, הריון, אי-ספיקת כליות, השמנה.</p>"),
        Section(id="esr-vs-crp", level=2, heading="ESR לעומת CRP",
                body_html="<p>ESR מגיב לאט (ימים) ומתאים לדלקת כרונית. CRP מגיב מהר (6-8 שעות) ומתאים לזיהום חריף. בלופוס, ESR עולה בעוד CRP עשוי להישאר תקין. ראו <a href=\"/blog/crp-high-meaning\">מדריך CRP</a>.</p>"),
        Section(id="false-elevations", level=2, heading="עליות שגויות ומגבלות של ESR",
                body_html="<p>אנמיה, השמנה, גיל, הריון, אי-ספיקת כליות והיפרגמגלובולינמיה עלולים להעלות ESR באופן שגוי. פוליציטמיה ואנמיה חרמשית עלולות להורידו באופן שגוי.</p>"),
        Section(id="monitoring-role", level=2, heading="תפקיד ESR במעקב אחר מחלות",
                body_html="<p>ESR יקר ערך למעקב אחר דלקת עורקים ענקית תאים, דלקת מפרקים שגרונית (חלק מ-DAS28), זיהומים כרוניים ולימפומת הודג'קין.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא",
                body_html="<p>פנו לרופא אם: ESR מעל הנורמה המותאמת לגיל עם תסמינים לא מוסברים; ESR מעל 100; מחלה אוטואימונית עם ESR עולה; כאב ראש חדש חמור מעל גיל 50 (חשד לדלקת עורקים ענקית תאים).</p>"),
        Section(id="how-norya-helps", level=2, heading="כיצד Norya עוזרת לך להבין את תוצאות ה-ESR",
                body_html="<p><strong>Norya</strong> מפשטת את הפרשנות: העלו תוצאות וקבלו דוח בריאות ברור תוך דקות. <a href=\"/analyze\">התחילו ניתוח עם Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="उच्च ESR: आपकी रक्त जांच के परिणाम का क्या अर्थ है",
                body_html="<p><strong>ESR (एरिथ्रोसाइट सेडिमेंटेशन रेट)</strong> सबसे पुरानी और सरल रक्त जांचों में से एक है। यह मापता है कि लाल रक्त कोशिकाएँ एक घंटे में एक ऊर्ध्वाधर ट्यूब के तल में कितनी तेजी से बैठती हैं। तेज़ बैठना शरीर में सूजन का संकेत देता है।</p><p><strong>CRP</strong> जैसे अधिक विशिष्ट मार्करों की उपलब्धता के बावजूद, ESR पुरानी, निम्न-श्रेणी की सूजन प्रक्रियाओं के लिए मूल्यवान बना हुआ है।</p>"),
        Section(id="what-is-esr", level=2, heading="ESR क्या है?",
                body_html="<p>ESR एक गैर-विशिष्ट सूजन मार्कर है। फाइब्रिनोजेन और इम्युनोग्लोबुलिन लाल रक्त कोशिकाओं को <em>रूलो</em> बनाने का कारण बनते हैं जो तेज़ी से बैठती हैं। <strong>वेस्टरग्रेन विधि</strong> संदर्भ मानक है।</p>"),
        Section(id="how-esr-works", level=2, heading="ESR परीक्षण कैसे काम करता है?",
                body_html="<p>लाल रक्त कोशिकाएँ ऋणात्मक आवेश (ज़ीटा पोटेंशियल) रखती हैं जो उन्हें प्लाज्मा में बिखरा रखता है। तीव्र-चरण प्रोटीन इस पोटेंशियल को कम करते हैं, रूलो गठन की अनुमति देते हैं। एनीमिया ESR को गलत तरीके से बढ़ाता है; पॉलीसिथेमिया इसे कम करता है।</p>"),
        Section(id="normal-ranges", level=2, heading="सामान्य ESR सीमाएँ",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य ESR (mm/hr)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">पुरुष &lt; 50 वर्ष</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">पुरुष &ge; 50 वर्ष</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">महिलाएँ &lt; 50 वर्ष</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">महिलाएँ &ge; 50 वर्ष</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr></tbody></table><p><strong>100 mm/hr</strong> से ऊपर ESR गंभीर अंतर्निहित बीमारी का संकेत देता है।</p>'),
        Section(id="high-esr-causes", level=2, heading="उच्च ESR के कारण",
                body_html="<p><strong>संक्रमण:</strong> निमोनिया, एंडोकार्डाइटिस, तपेदिक। <strong>ऑटोइम्यून:</strong> टेम्पोरल आर्टेराइटिस, पॉलीमायल्जिया रूमेटिका, रूमेटॉइड आर्थराइटिस, ल्यूपस। <strong>कैंसर:</strong> मल्टीपल मायलोमा, लिम्फोमा। <strong>अन्य:</strong> एनीमिया, गर्भावस्था, गुर्दे की विफलता, मोटापा।</p>"),
        Section(id="esr-vs-crp", level=2, heading="ESR बनाम CRP",
                body_html="<p>ESR धीरे प्रतिक्रिया करता है (दिन) और पुरानी सूजन के लिए उपयुक्त है। CRP तेज़ प्रतिक्रिया करता है (6-8 घंटे) और तीव्र संक्रमण के लिए आदर्श है। ल्यूपस में ESR बढ़ता है जबकि CRP सामान्य रह सकता है। <a href=\"/blog/crp-high-meaning\">CRP गाइड</a> देखें।</p>"),
        Section(id="false-elevations", level=2, heading="ESR की गलत ऊंचाई और सीमाएँ",
                body_html="<p>एनीमिया, मोटापा, उम्र, गर्भावस्था, गुर्दे की विफलता और हाइपरगैमाग्लोबुलिनीमिया ESR को गलत तरीके से बढ़ा सकते हैं। पॉलीसिथेमिया और सिकल सेल रोग इसे गलत तरीके से कम कर सकते हैं।</p>"),
        Section(id="monitoring-role", level=2, heading="रोग निगरानी में ESR की भूमिका",
                body_html="<p>ESR टेम्पोरल आर्टेराइटिस, रूमेटॉइड आर्थराइटिस (DAS28 का हिस्सा), पुराने संक्रमण और हॉजकिन लिम्फोमा की निगरानी के लिए अमूल्य है।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर को कब दिखाएँ",
                body_html="<p>डॉक्टर से परामर्श करें यदि: ESR आयु-समायोजित सामान्य सीमा से ऊपर; ESR &gt;100 mm/hr; ऑटोइम्यून रोग में बढ़ता ESR; 50 से अधिक उम्र में नया गंभीर सिरदर्द (संभावित टेम्पोरल आर्टेराइटिस)।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya ESR परिणामों को समझने में कैसे मदद करता है",
                body_html="<p><strong>Norya</strong> व्याख्या को सरल बनाता है: रक्त जांच के परिणाम अपलोड करें और मिनटों में स्पष्ट स्वास्थ्य रिपोर्ट प्राप्त करें। <a href=\"/analyze\">Norya के साथ विश्लेषण शुरू करें</a>।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="سرعة ترسيب الدم المرتفعة (ESR): ماذا تعني نتيجة تحليل الدم",
                body_html="<p><strong>سرعة ترسيب كريات الدم الحمراء (ESR)</strong> تقيس مدى سرعة ترسب كريات الدم الحمراء في أنبوب عمودي خلال ساعة. ترسب أسرع يشير إلى وجود التهاب في الجسم.</p><p>رغم توفر علامات أكثر تحديداً مثل <strong>البروتين التفاعلي C (CRP)</strong>، يظل ESR قيّماً للعمليات الالتهابية المزمنة. يُستخدم في تشخيص ومتابعة التهاب الشريان الصدغي والتهاب المفاصل الروماتويدي والذئبة.</p>"),
        Section(id="what-is-esr", level=2, heading="ما هو ESR؟",
                body_html="<p>ESR علامة التهاب غير نوعية. الفيبرينوجين والغلوبولينات المناعية تجعل كريات الدم الحمراء تتكدس في تشكيلات <em>رولو</em> تترسب أسرع. طريقة <strong>ويسترغرن</strong> هي المعيار المرجعي.</p>"),
        Section(id="how-esr-works", level=2, heading="كيف يعمل اختبار ESR؟",
                body_html="<p>كريات الدم الحمراء تحمل شحنة سالبة (جهد زيتا) تبقيها معلقة في البلازما. بروتينات الطور الحاد تقلل هذا الجهد وتسمح بتكوين الرولو. فقر الدم يرفع ESR زوراً؛ كثرة الحمر تخفضه.</p>"),
        Section(id="normal-ranges", level=2, heading="النطاقات الطبيعية لـ ESR",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">ESR طبيعي (mm/hr)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">رجال &lt; 50 سنة</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 15</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">رجال &ge; 50 سنة</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">نساء &lt; 50 سنة</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 20</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">نساء &ge; 50 سنة</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0 &ndash; 30</td></tr></tbody></table><p>ESR فوق <strong>100 mm/hr</strong> يشير بقوة إلى مرض أساسي خطير.</p>'),
        Section(id="high-esr-causes", level=2, heading="أسباب ارتفاع ESR",
                body_html="<p><strong>عدوى:</strong> التهاب رئوي، التهاب شغاف القلب، سل. <strong>أمراض مناعية:</strong> التهاب الشريان الصدغي، التهاب المفاصل الروماتويدي، الذئبة. <strong>أورام:</strong> المايلوما المتعددة، اللمفومة. <strong>أخرى:</strong> فقر الدم، الحمل، الفشل الكلوي، السمنة.</p>"),
        Section(id="esr-vs-crp", level=2, heading="ESR مقابل CRP",
                body_html="<p>ESR يستجيب ببطء (أيام) ومناسب للالتهاب المزمن. CRP يستجيب بسرعة (6-8 ساعات) ومناسب للعدوى الحادة. في الذئبة، يرتفع ESR بينما قد يبقى CRP طبيعياً. انظر <a href=\"/blog/crp-high-meaning\">دليل CRP</a>.</p>"),
        Section(id="false-elevations", level=2, heading="ارتفاعات خاطئة وقيود ESR",
                body_html="<p>فقر الدم، السمنة، التقدم بالعمر، الحمل، الفشل الكلوي وفرط غاماغلوبولينات الدم قد ترفع ESR زوراً. كثرة الحمر وفقر الدم المنجلي قد تخفضه زوراً.</p>"),
        Section(id="monitoring-role", level=2, heading="دور ESR في مراقبة الأمراض",
                body_html="<p>ESR ذو قيمة في متابعة التهاب الشريان الصدغي، التهاب المفاصل الروماتويدي (جزء من DAS28)، العدوى المزمنة ولمفومة هودجكين.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى يجب مراجعة الطبيب",
                body_html="<p>استشر طبيبك إذا: ESR فوق المعدل الطبيعي المعدل بالعمر مع أعراض غير مفسرة؛ ESR فوق 100؛ مرض مناعي ذاتي مع ارتفاع ESR؛ صداع شديد حديث فوق 50 سنة (التهاب الشريان الصدغي المحتمل).</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف تساعدك Norya في فهم نتائج ESR",
                body_html="<p><strong>Norya</strong> تبسّط التفسير: ارفع نتائج تحليل الدم واحصل على تقرير صحي واضح خلال دقائق. <a href=\"/analyze\">ابدأ التحليل مع Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# PUBLIC GETTERS
# ---------------------------------------------------------------------------
def get_esr_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_esr_faq_schema_qa() -> dict:
    return {
        "en": [
            {"question": "What is a normal ESR level?",
             "answer": "Normal ESR varies by age and sex: men under 50: 0-15 mm/hr, men over 50: 0-20 mm/hr, women under 50: 0-20 mm/hr, women over 50: 0-30 mm/hr. ESR naturally increases with age."},
            {"question": "What causes a high ESR?",
             "answer": "High ESR can be caused by infections, autoimmune diseases (rheumatoid arthritis, lupus, temporal arteritis), cancer (multiple myeloma, lymphoma), anemia, pregnancy, obesity, and kidney disease."},
            {"question": "What is the difference between ESR and CRP?",
             "answer": "ESR responds slowly (days) and is best for monitoring chronic inflammation. CRP responds quickly (6-8 hours) and is better for detecting acute infections. In lupus, ESR rises while CRP may stay normal."},
            {"question": "Does a high ESR always mean something is wrong?",
             "answer": "Not necessarily. ESR can be mildly elevated due to aging, obesity, or anemia without serious disease. However, very high ESR (above 100 mm/hr) strongly suggests significant underlying disease."},
            {"question": "Can ESR be falsely elevated?",
             "answer": "Yes. Anemia, obesity, aging, pregnancy, kidney failure, and high immunoglobulin levels can all cause false ESR elevations without actual inflammation."},
        ],
        "tr": [
            {"question": "Normal ESR (sedimentasyon) değeri nedir?",
             "answer": "Normal ESR yaşa ve cinsiyete göre değişir: 50 yaş altı erkekler: 0-15, 50 yaş üstü erkekler: 0-20, 50 yaş altı kadınlar: 0-20, 50 yaş üstü kadınlar: 0-30 mm/sa."},
            {"question": "Yüksek ESR'nin nedenleri nelerdir?",
             "answer": "Enfeksiyonlar, otoimmün hastalıklar (romatoid artrit, lupus, temporal arterit), kanser (multipl miyelom, lenfoma), anemi, gebelik, obezite ve böbrek hastalığı."},
            {"question": "ESR ve CRP arasındaki fark nedir?",
             "answer": "ESR yavaş tepki verir (günler) ve kronik iltihap takibi için uygundur. CRP hızlı tepki verir (6-8 saat) ve akut enfeksiyonlar için daha iyidir."},
            {"question": "ESR yanlış yüksek çıkabilir mi?",
             "answer": "Evet. Anemi, obezite, yaşlanma, gebelik, böbrek yetmezliği ve yüksek immünoglobulin düzeyleri ESR'yi yanlış yükseltebilir."},
        ],
        "es": [
            {"question": "¿Cuál es un valor normal de VSG?",
             "answer": "Hombres <50 años: 0-15, hombres ≥50: 0-20, mujeres <50: 0-20, mujeres ≥50: 0-30 mm/h."},
            {"question": "¿Qué causa una VSG elevada?",
             "answer": "Infecciones, enfermedades autoinmunes, cáncer, anemia, embarazo, obesidad y enfermedad renal."},
            {"question": "¿Cuál es la diferencia entre VSG y PCR?",
             "answer": "La VSG responde lentamente y es ideal para inflamación crónica. La PCR responde rápidamente y es mejor para infecciones agudas."},
        ],
        "de": [
            {"question": "Was ist ein normaler BSG-Wert?",
             "answer": "Männer <50: 0-15, Männer ≥50: 0-20, Frauen <50: 0-20, Frauen ≥50: 0-30 mm/h."},
            {"question": "Was verursacht eine hohe BSG?",
             "answer": "Infektionen, Autoimmunerkrankungen, Krebs, Anämie, Schwangerschaft, Adipositas und Nierenerkrankung."},
            {"question": "Was ist der Unterschied zwischen BSG und CRP?",
             "answer": "BSG reagiert langsam und eignet sich für chronische Entzündungen. CRP reagiert schnell und ist besser für akute Infektionen."},
        ],
        "fr": [
            {"question": "Quelle est une VS normale ?",
             "answer": "Hommes <50 ans : 0-15, hommes ≥50 : 0-20, femmes <50 : 0-20, femmes ≥50 : 0-30 mm/h."},
            {"question": "Quelles sont les causes d'une VS élevée ?",
             "answer": "Infections, maladies auto-immunes, cancers, anémie, grossesse, obésité et maladie rénale."},
            {"question": "Quelle est la différence entre VS et CRP ?",
             "answer": "La VS répond lentement et convient à l'inflammation chronique. La CRP répond rapidement et est meilleure pour les infections aiguës."},
        ],
        "it": [
            {"question": "Qual è un valore normale di VES?",
             "answer": "Uomini <50 anni: 0-15, uomini ≥50: 0-20, donne <50: 0-20, donne ≥50: 0-30 mm/h."},
            {"question": "Cosa causa una VES alta?",
             "answer": "Infezioni, malattie autoimmuni, tumori, anemia, gravidanza, obesità e nefropatia."},
            {"question": "Qual è la differenza tra VES e PCR?",
             "answer": "La VES risponde lentamente ed è adatta per l'infiammazione cronica. La PCR risponde rapidamente ed è migliore per le infezioni acute."},
        ],
        "he": [
            {"question": "מהו ערך ESR תקין?",
             "answer": "גברים מתחת ל-50: 0-15, גברים מעל 50: 0-20, נשים מתחת ל-50: 0-20, נשים מעל 50: 0-30 mm/hr."},
            {"question": "מה גורם ל-ESR גבוה?",
             "answer": "זיהומים, מחלות אוטואימוניות, סרטן, אנמיה, הריון, השמנה ומחלת כליות."},
            {"question": "מה ההבדל בין ESR ל-CRP?",
             "answer": "ESR מגיב לאט ומתאים לדלקת כרונית. CRP מגיב מהר ומתאים יותר לזיהומים חריפים."},
        ],
        "hi": [
            {"question": "सामान्य ESR स्तर क्या है?",
             "answer": "पुरुष <50: 0-15, पुरुष ≥50: 0-20, महिलाएँ <50: 0-20, महिलाएँ ≥50: 0-30 mm/hr."},
            {"question": "उच्च ESR का क्या कारण है?",
             "answer": "संक्रमण, ऑटोइम्यून रोग, कैंसर, एनीमिया, गर्भावस्था, मोटापा और गुर्दे की बीमारी।"},
            {"question": "ESR और CRP में क्या अंतर है?",
             "answer": "ESR धीरे प्रतिक्रिया करता है और पुरानी सूजन के लिए उपयुक्त है। CRP तेज़ प्रतिक्रिया करता है और तीव्र संक्रमण के लिए बेहतर है।"},
        ],
        "ar": [
            {"question": "ما هو مستوى ESR الطبيعي؟",
             "answer": "رجال أقل من 50: 0-15، رجال 50 فأكثر: 0-20، نساء أقل من 50: 0-20، نساء 50 فأكثر: 0-30 mm/hr."},
            {"question": "ما أسباب ارتفاع ESR؟",
             "answer": "العدوى، أمراض المناعة الذاتية، السرطان، فقر الدم، الحمل، السمنة وأمراض الكلى."},
            {"question": "ما الفرق بين ESR وCRP؟",
             "answer": "ESR يستجيب ببطء ومناسب للالتهاب المزمن. CRP يستجيب بسرعة ومناسب أكثر للعدوى الحادة."},
        ],
    }
