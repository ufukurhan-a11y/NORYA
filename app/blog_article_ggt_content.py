# -*- coding: utf-8 -*-
"""
GGT (Gamma-Glutamyl Transferase) blog article — full body content for all 9 languages.
Used by blog_i18n._article_ggt(). Sections: intro, what-is, normal-ranges, causes,
symptoms, related-tests, when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="GGT yüksekliği ne anlama gelir?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>GGT (Gamma-Glutamil Transferaz)</strong> değerinin "
                "yüksek çıktığını gördüğünüzde ilk soru genellikle şudur: bu ciddi mi, karaciğerimde "
                "bir sorun mu var? GGT, karaciğer ve safra yolları sağlığının en duyarlı "
                "göstergelerinden biridir ve birçok farklı nedenden etkilenebilir.</p>"
                "<p>Bu rehber, GGT'nin ne olduğunu, normal referans aralıklarını, yüksekliğinin "
                "olası nedenlerini ve ne zaman doktora başvurmanız gerektiğini sade bir dille "
                "açıklamayı amaçlıyor. Amacımız teşhis koymak değil — sonuçlarınızı daha iyi "
                "anlayarak hekiminizle verimli bir görüşme yapmanıza yardımcı olmaktır.</p>"
                "<p>GGT yüksekliği tek başına bir hastalık anlamına gelmez; sonucunuzu diğer "
                "karaciğer enzimleri ve klinik tablonuz ile birlikte değerlendirmek büyük önem taşır.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="GGT (Gamma-GT) nedir?",
            body_html=(
                "<p><strong>GGT (Gamma-Glutamil Transferaz)</strong>, başta karaciğer olmak üzere "
                "böbrekler, pankreas ve safra kanallarında bulunan bir enzimdir. Glutatyon "
                "metabolizmasında görev alır ve hücre zarından amino asitlerin taşınmasına yardımcı "
                "olur. Karaciğer hasarı veya safra yolu tıkanıklığı olduğunda GGT kana sızar ve "
                "kan düzeylerinde artış görülür.</p>"
                "<p>GGT, karaciğer fonksiyon testleri panelinin önemli bir parçasıdır ve sıklıkla "
                "<a href=\"/tr/blog/alt-ve-ast-yuksekligi-neyi-gosterir\">ALT, AST</a> gibi diğer "
                "karaciğer enzimleri ile birlikte istenir. Özellikle ALP (alkalen fosfataz) "
                "yüksekliğinin karaciğer kaynaklı mı yoksa kemik kaynaklı mı olduğunu ayırt etmede "
                "GGT kritik bir rol oynar.</p>"
                "<p>Bu enzim alkole karşı son derece hassastır; düzenli alkol kullanımı GGT'yi "
                "diğer karaciğer enzimlerinden önce yükseltebilir. Bu nedenle klinik pratikte hem "
                "karaciğer hastalıkları hem de alkol kullanım takibinde sıkça değerlendirilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="GGT normal değerleri",
            body_html=(
                "<p>GGT referans aralıkları laboratuvara, yaşa ve cinsiyete göre farklılık "
                "gösterebilir. Genel kabul gören aralıklar şöyledir:</p>"
                "<ul>"
                "<li><strong>Erkekler:</strong> 8–61 U/L</li>"
                "<li><strong>Kadınlar:</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>Erkeklerde değerler genellikle kadınlardan daha yüksektir. Yaşla birlikte GGT "
                "düzeylerinde doğal bir artış görülmesi normaldir. Bazı laboratuvarlar farklı "
                "aralıklar kullanabilir; sonuçlarınızı her zaman raporunuzdaki referans aralıklarıyla "
                "karşılaştırın.</p>"
                "<p>Hafif yükseklikler (referans aralığının hemen üzerinde) sıklıkla klinik açıdan "
                "anlamlı olmayabilir, ancak belirgin yükseklikler mutlaka hekimle paylaşılmalıdır. "
                "GGT sonucu tek başına yeterli değildir; ALT, AST, ALP ve bilirubin gibi diğer "
                "değerlerle birlikte yorumlanmalıdır.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="GGT yüksekliğinin nedenleri",
            body_html=(
                "<p>GGT yüksekliği çeşitli nedenlerden kaynaklanabilir. En sık karşılaşılan "
                "durumlar şunlardır:</p>"
                "<ul>"
                "<li><strong>Alkol kullanımı:</strong> Düzenli veya aşırı alkol tüketimi GGT'nin "
                "en yaygın yükselme nedenidir. Bırakıldığında değerler genellikle birkaç hafta "
                "içinde düşer.</li>"
                "<li><strong>Karaciğer hastalıkları:</strong> Yağlı karaciğer (steatoz), hepatit, "
                "siroz ve karaciğer tümörleri GGT yüksekliğine yol açabilir.</li>"
                "<li><strong>Safra yolu tıkanıklığı:</strong> Safra taşları veya safra kanalı "
                "darlığı GGT'yi belirgin şekilde yükseltir.</li>"
                "<li><strong>İlaçlar:</strong> Bazı antiepileptikler, barbitüratlar, NSAİİ'ler ve "
                "statinler GGT düzeyini artırabilir.</li>"
                "<li><strong>Pankreatit:</strong> Pankreas iltihabı GGT yüksekliğine neden olabilir.</li>"
                "<li><strong>Kalp yetmezliği:</strong> Konjesyona bağlı karaciğer konjesyonu "
                "GGT'yi yükseltebilir.</li>"
                "<li><strong>Diyabet ve metabolik sendrom:</strong> İnsülin direnci ve yağlı "
                "karaciğer birlikteliği GGT artışına katkıda bulunur.</li>"
                "</ul>"
                "<p>Nadir durumlarda GGT yüksekliği otoimmün hepatit, hemokromatoz veya Wilson "
                "hastalığı gibi genetik karaciğer hastalıklarının da belirtisi olabilir. "
                "Yüksekliğin nedenini belirlemek için ek testler ve klinik değerlendirme gereklidir.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="GGT yüksekliğinin belirtileri",
            body_html=(
                "<p>GGT yüksekliği tek başına genellikle belirgin belirti vermez; çoğunlukla altta "
                "yatan durumun belirtileri ön plana çıkar. Ancak karaciğer veya safra yolu "
                "sorunlarına eşlik edebilecek yaygın belirtiler şunlardır:</p>"
                "<ul>"
                "<li>Sağ üst karında ağrı veya rahatsızlık hissi</li>"
                "<li>Yorgunluk ve halsizlik</li>"
                "<li>Bulantı veya iştahsızlık</li>"
                "<li>Ciltte veya göz akında sararma (sarılık)</li>"
                "<li>Koyu renkli idrar veya açık renkli dışkı</li>"
                "<li>Kaşıntı</li>"
                "</ul>"
                "<p>Bu belirtilerin herhangi biri varsa ve GGT'niz de yüksek çıkmışsa, hekiminize "
                "başvurmanız önemlidir. Belirtiler olmadan da rastlantısal olarak saptanan GGT "
                "yüksekliği, özellikle tekrarlayan yüksek değerlerde, araştırılmaya değerdir.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="GGT ile birlikte değerlendirilen testler",
            body_html=(
                "<p>GGT sonucu tek başına kesin bir anlam taşımaz; aşağıdaki testlerle birlikte "
                "yorumlanması gerekir:</p>"
                "<ul>"
                "<li><strong><a href=\"/tr/blog/alt-ve-ast-yuksekligi-neyi-gosterir\">ALT ve AST</a>:</strong> "
                "Karaciğer hücre hasarının doğrudan göstergeleridir. GGT ile birlikte yükselmişlerse "
                "karaciğer hastalığı olasılığı artar.</li>"
                "<li><strong>ALP (Alkalen Fosfataz):</strong> GGT ile ALP birlikte yükselmişse "
                "safra yolu veya karaciğer kaynaklı sorun düşünülür; ALP tek başına yüksekse "
                "kemik hastalığı olabilir.</li>"
                "<li><strong>Bilirubin:</strong> Safra pigmenti olan bilirubin yüksekliği sarılık "
                "ile ilişkilidir ve GGT yüksekliğini destekler.</li>"
                "<li><strong>Albumin ve total protein:</strong> Karaciğerin sentez fonksiyonunu "
                "değerlendirmede kullanılır.</li>"
                "</ul>"
                "<p>Hekiminiz klinik tabloya göre karaciğer ultrasonografisi, viral hepatit "
                "serolojisi veya otoimmün belirteçler gibi ek testler de isteyebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda sonuçlarınızı bir hekimle paylaşmanız önerilir:</p>"
                "<ul>"
                "<li>GGT değeri referans aralığının belirgin üzerinde çıkmışsa</li>"
                "<li>ALT, AST veya ALP gibi diğer karaciğer enzimleri de yüksekse</li>"
                "<li>Sarılık, karın ağrısı veya açıklanamayan yorgunluk gibi belirtiler varsa</li>"
                "<li>Düzenli alkol kullanımınız varsa veya yakın zamanda ilaç değişikliği olduysa</li>"
                "<li>Tekrarlayan testlerde GGT yüksek kalmaya devam ediyorsa</li>"
                "</ul>"
                "<p>GGT yüksekliği birçok farklı durumun göstergesi olabileceğinden, sonuçlarınızı "
                "mutlaka öykünüzü ve diğer test sonuçlarınızı bilen bir hekim değerlendirmelidir. "
                "Erken değerlendirme, olası karaciğer hastalıklarının erken evrede yakalanmasına "
                "yardımcı olabilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya GGT sonucunuzu anlamanızı nasıl kolaylaştırır?",
            body_html=(
                "<p>Norya'da teşhis koymuyoruz — randevunuza hazırlanmanıza yardım ediyoruz. "
                "<a href=\"/analyze\">Kan tahlili raporunuzu yükleyerek</a> GGT dahil tüm "
                "değerlerinizin sade dilde, referans aralıkları ve bağlamıyla açıklandığı net, "
                "yapılandırılmış bir özet alabilirsiniz.</p>"
                "<p>Böylece hekiminizle sonuçlarınızı konuşurken doğru soruları sormak kolaylaşır. "
                "Norya, GGT'yi ALT, AST ve diğer ilgili değerlerle birlikte sunarak büyük resmi "
                "görmenizi sağlar. Seçenekler ve fiyatlar için "
                "<a href=\"/pricing\">fiyatlandırma sayfamıza</a> bakın.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                "<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis "
                "yerine geçmez.</strong> GGT yüksekliğinin birçok nedeni olabilir; sonucunuzu ancak "
                "öykünüzü ve bağlamını bilen bir sağlık profesyoneli doğru yorumlayabilir. "
                "Laboratuvar sonuçlarınızı her zaman bir hekimle görüşün.</p>"
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
            heading="High GGT: what does it mean in your blood test?",
            body_html=(
                "<p>If your lab report shows an elevated <strong>GGT (Gamma-Glutamyl Transferase)</strong>, "
                "you are probably asking: is this serious, and does it mean something is wrong with my "
                "liver? GGT is one of the most sensitive markers of liver and bile duct health, and it "
                "can be affected by a wide range of factors.</p>"
                "<p>This guide explains what GGT is, what normal and high values mean, common causes "
                "of elevated GGT, and when you should talk to your doctor. Our goal is not to diagnose "
                "— it is to help you understand your results so you can have a more informed "
                "conversation with your healthcare provider.</p>"
                "<p>An elevated GGT on its own does not mean you have a disease. Interpreting it "
                "alongside other liver enzymes and your clinical picture is essential for accurate "
                "assessment.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is GGT (Gamma-GT)?",
            body_html=(
                "<p><strong>GGT (Gamma-Glutamyl Transferase)</strong> is an enzyme found primarily in "
                "the liver, but also in the kidneys, pancreas, and bile ducts. It plays a role in "
                "glutathione metabolism and helps transport amino acids across cell membranes. When "
                "the liver is damaged or bile flow is obstructed, GGT leaks into the bloodstream and "
                "levels rise.</p>"
                "<p>GGT is an important component of the liver function test panel and is frequently "
                "ordered alongside other liver enzymes such as "
                "<a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">ALT and AST</a>. "
                "It is particularly useful for distinguishing whether an elevated ALP (alkaline "
                "phosphatase) is of liver origin or bone origin.</p>"
                "<p>This enzyme is extremely sensitive to alcohol; regular alcohol consumption can "
                "raise GGT before other liver enzymes become elevated. For this reason, GGT is "
                "commonly used in clinical practice to monitor both liver disease and alcohol intake.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="GGT normal ranges",
            body_html=(
                "<p>GGT reference ranges vary by laboratory, age, and sex. Generally accepted "
                "ranges are:</p>"
                "<ul>"
                "<li><strong>Men:</strong> 8–61 U/L</li>"
                "<li><strong>Women:</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>Men typically have higher GGT levels than women. A natural increase with age is "
                "considered normal. Some laboratories may use slightly different ranges, so always "
                "compare your results with the reference values on your specific lab report.</p>"
                "<p>Mildly elevated levels (just above the upper limit) may not always be clinically "
                "significant, but clearly elevated levels should always be discussed with a doctor. "
                "A GGT result should be interpreted alongside ALT, AST, ALP, and bilirubin for a "
                "complete picture.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high GGT",
            body_html=(
                "<p>Elevated GGT can result from various conditions. The most common include:</p>"
                "<ul>"
                "<li><strong>Alcohol use:</strong> Regular or heavy alcohol consumption is the "
                "most frequent cause of elevated GGT. Levels typically fall within a few weeks "
                "after stopping.</li>"
                "<li><strong>Liver diseases:</strong> Fatty liver disease (steatosis), hepatitis, "
                "cirrhosis, and liver tumours can all raise GGT.</li>"
                "<li><strong>Bile duct obstruction:</strong> Gallstones or bile duct narrowing can "
                "cause a marked GGT elevation.</li>"
                "<li><strong>Medications:</strong> Certain anticonvulsants, barbiturates, NSAIDs, "
                "and statins may increase GGT levels.</li>"
                "<li><strong>Pancreatitis:</strong> Inflammation of the pancreas can elevate GGT.</li>"
                "<li><strong>Heart failure:</strong> Liver congestion due to congestive heart failure "
                "may raise GGT.</li>"
                "<li><strong>Diabetes and metabolic syndrome:</strong> Insulin resistance and "
                "associated fatty liver contribute to GGT elevation.</li>"
                "</ul>"
                "<p>In rarer cases, elevated GGT may signal autoimmune hepatitis, haemochromatosis, "
                "or Wilson disease. Additional tests and clinical evaluation are needed to determine "
                "the underlying cause.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms associated with high GGT",
            body_html=(
                "<p>High GGT on its own usually does not produce noticeable symptoms; the symptoms "
                "of the underlying condition tend to dominate. However, common signs that may "
                "accompany liver or bile duct problems include:</p>"
                "<ul>"
                "<li>Pain or discomfort in the upper right abdomen</li>"
                "<li>Fatigue and general weakness</li>"
                "<li>Nausea or loss of appetite</li>"
                "<li>Yellowing of the skin or whites of the eyes (jaundice)</li>"
                "<li>Dark urine or pale stools</li>"
                "<li>Itching</li>"
                "</ul>"
                "<p>If you experience any of these symptoms alongside a high GGT, consult your "
                "doctor promptly. Even without symptoms, a persistently elevated GGT — especially "
                "if it recurs on repeat testing — is worth investigating.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Tests commonly evaluated alongside GGT",
            body_html=(
                "<p>A GGT result alone does not provide a definitive answer; it should be "
                "interpreted together with the following tests:</p>"
                "<ul>"
                "<li><strong><a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">ALT and AST</a>:</strong> "
                "Direct markers of liver cell damage. If elevated together with GGT, liver disease "
                "becomes more likely.</li>"
                "<li><strong>ALP (Alkaline Phosphatase):</strong> When both GGT and ALP are elevated, "
                "a liver or bile duct origin is suspected; if ALP alone is high, a bone condition "
                "may be the cause.</li>"
                "<li><strong>Bilirubin:</strong> Elevated bilirubin (a bile pigment) is associated "
                "with jaundice and supports a hepatobiliary cause of GGT elevation.</li>"
                "<li><strong>Albumin and total protein:</strong> Used to assess the liver's synthetic "
                "function.</li>"
                "</ul>"
                "<p>Depending on the clinical picture, your doctor may also order liver ultrasound, "
                "viral hepatitis serology, or autoimmune markers for further evaluation.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>You should discuss your results with a doctor if:</p>"
                "<ul>"
                "<li>Your GGT is significantly above the reference range</li>"
                "<li>Other liver enzymes such as ALT, AST, or ALP are also elevated</li>"
                "<li>You have symptoms like jaundice, abdominal pain, or unexplained fatigue</li>"
                "<li>You consume alcohol regularly or have recently changed medications</li>"
                "<li>GGT remains elevated on repeated testing</li>"
                "</ul>"
                "<p>Because elevated GGT can indicate many different conditions, it is essential that "
                "a doctor who knows your medical history and other test results evaluates the finding. "
                "Early assessment can help detect liver conditions at a treatable stage.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your GGT result",
            body_html=(
                "<p>At Norya, we do not diagnose — we help you prepare. "
                "<a href=\"/analyze\">Upload your lab report</a> and receive a clear, structured "
                "summary that explains your values — including GGT — in plain language, with "
                "reference ranges and context.</p>"
                "<p>This makes it easier to discuss your results with your doctor and to ask the "
                "right questions. Norya presents GGT alongside ALT, AST, and other relevant markers "
                "so you can see the bigger picture. For options and pricing, visit our "
                "<a href=\"/pricing\">pricing page</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This content is for information only and does not replace medical "
                "advice or diagnosis.</strong> Elevated GGT can have many causes; only a healthcare "
                "professional who knows your history and context can interpret your result properly. "
                "Always discuss your lab results with a doctor.</p>"
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
            heading="GGT alta: ¿qué significa en tu análisis de sangre?",
            body_html=(
                "<p>Si tu informe de laboratorio muestra un valor elevado de <strong>GGT "
                "(Gamma-Glutamil Transferasa)</strong>, probablemente te preguntas: ¿es grave?, "
                "¿tengo un problema en el hígado? La GGT es uno de los marcadores más sensibles de "
                "la salud del hígado y las vías biliares, y puede verse afectada por múltiples "
                "factores.</p>"
                "<p>Esta guía explica qué es la GGT, cuáles son los valores normales, las causas "
                "más frecuentes de su elevación y cuándo conviene consultar al médico. Nuestro "
                "objetivo no es diagnosticar, sino ayudarte a comprender tus resultados para que "
                "puedas hablar con tu médico de forma más informada.</p>"
                "<p>Una GGT alta por sí sola no significa enfermedad; interpretarla junto con "
                "otras enzimas hepáticas y tu cuadro clínico es fundamental.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es la GGT (Gamma-GT)?",
            body_html=(
                "<p>La <strong>GGT (Gamma-Glutamil Transferasa)</strong> es una enzima que se "
                "encuentra principalmente en el hígado, pero también en los riñones, el páncreas "
                "y los conductos biliares. Participa en el metabolismo del glutatión y facilita el "
                "transporte de aminoácidos a través de las membranas celulares. Cuando el hígado se "
                "daña o el flujo biliar se obstruye, la GGT se filtra al torrente sanguíneo y sus "
                "niveles aumentan.</p>"
                "<p>La GGT forma parte del panel de pruebas hepáticas y suele solicitarse junto con "
                "otras enzimas como <a href=\"/es/blog/que-significan-alt-y-ast-altos\">ALT y AST</a>. "
                "Es especialmente útil para distinguir si una ALP (fosfatasa alcalina) elevada "
                "tiene origen hepático u óseo.</p>"
                "<p>Esta enzima es muy sensible al alcohol; el consumo regular puede elevar la GGT "
                "antes que otras enzimas hepáticas. Por ello, se utiliza en la práctica clínica "
                "tanto para el seguimiento de enfermedades hepáticas como para monitorizar el "
                "consumo de alcohol.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de GGT",
            body_html=(
                "<p>Los rangos de referencia de la GGT varían según el laboratorio, la edad y "
                "el sexo. Los valores generalmente aceptados son:</p>"
                "<ul>"
                "<li><strong>Hombres:</strong> 8–61 U/L</li>"
                "<li><strong>Mujeres:</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>Los hombres suelen tener niveles más altos que las mujeres. Es normal que la "
                "GGT aumente ligeramente con la edad. Algunos laboratorios pueden utilizar rangos "
                "distintos; compara siempre tus resultados con los valores de referencia de tu "
                "informe.</p>"
                "<p>Elevaciones leves (justo por encima del límite superior) pueden no ser "
                "clínicamente significativas, pero elevaciones claras deben comentarse con el "
                "médico. La GGT debe interpretarse junto con ALT, AST, ALP y bilirrubina.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de GGT alta",
            body_html=(
                "<p>La elevación de la GGT puede deberse a diversas situaciones. Las más "
                "frecuentes son:</p>"
                "<ul>"
                "<li><strong>Consumo de alcohol:</strong> El alcohol es la causa más común. Los "
                "niveles suelen bajar en pocas semanas tras dejar de beber.</li>"
                "<li><strong>Enfermedades hepáticas:</strong> Hígado graso, hepatitis, cirrosis "
                "y tumores hepáticos pueden elevar la GGT.</li>"
                "<li><strong>Obstrucción de las vías biliares:</strong> Los cálculos biliares o "
                "las estenosis del conducto biliar pueden causar una elevación marcada.</li>"
                "<li><strong>Medicamentos:</strong> Anticonvulsivantes, barbitúricos, AINEs y "
                "estatinas pueden aumentar la GGT.</li>"
                "<li><strong>Pancreatitis:</strong> La inflamación del páncreas puede elevarla.</li>"
                "<li><strong>Insuficiencia cardíaca:</strong> La congestión hepática secundaria "
                "puede subir la GGT.</li>"
                "<li><strong>Diabetes y síndrome metabólico:</strong> La resistencia a la insulina "
                "y el hígado graso asociado contribuyen a la elevación.</li>"
                "</ul>"
                "<p>En casos menos frecuentes, la GGT puede señalar hepatitis autoinmune, "
                "hemocromatosis o enfermedad de Wilson. Se necesitan pruebas adicionales para "
                "determinar la causa subyacente.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas asociados a GGT alta",
            body_html=(
                "<p>La GGT elevada por sí sola rara vez produce síntomas; suelen predominar los "
                "de la enfermedad subyacente. Signos frecuentes que pueden acompañar problemas "
                "hepáticos o biliares:</p>"
                "<ul>"
                "<li>Dolor o molestia en el abdomen superior derecho</li>"
                "<li>Cansancio y debilidad general</li>"
                "<li>Náuseas o pérdida de apetito</li>"
                "<li>Coloración amarillenta de piel u ojos (ictericia)</li>"
                "<li>Orina oscura o heces claras</li>"
                "<li>Picazón</li>"
                "</ul>"
                "<p>Si presentas alguno de estos síntomas junto con GGT alta, consulta a tu médico. "
                "Incluso sin síntomas, una GGT persistentemente alta merece investigación.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas que se evalúan junto a la GGT",
            body_html=(
                "<p>La GGT sola no da un diagnóstico; debe interpretarse con estas pruebas:</p>"
                "<ul>"
                "<li><strong><a href=\"/es/blog/que-significan-alt-y-ast-altos\">ALT y AST</a>:</strong> "
                "Marcadores directos de daño hepatocelular. Si se elevan junto a la GGT, la "
                "probabilidad de enfermedad hepática aumenta.</li>"
                "<li><strong>ALP (Fosfatasa Alcalina):</strong> La elevación conjunta de GGT y ALP "
                "sugiere origen hepático o biliar; la ALP sola alta puede indicar patología ósea.</li>"
                "<li><strong>Bilirrubina:</strong> Su elevación se asocia a ictericia y apoya una "
                "causa hepatobiliar.</li>"
                "<li><strong>Albúmina y proteínas totales:</strong> Valoran la función de síntesis "
                "del hígado.</li>"
                "</ul>"
                "<p>Según el caso, el médico puede pedir ecografía hepática, serología de hepatitis "
                "viral o marcadores autoinmunes.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debo ir al médico?",
            body_html=(
                "<p>Consulta a tu médico si:</p>"
                "<ul>"
                "<li>Tu GGT está claramente por encima del rango de referencia</li>"
                "<li>Otras enzimas hepáticas (ALT, AST, ALP) también están elevadas</li>"
                "<li>Tienes ictericia, dolor abdominal o cansancio inexplicable</li>"
                "<li>Consumes alcohol con regularidad o has cambiado de medicación recientemente</li>"
                "<li>La GGT sigue alta en controles sucesivos</li>"
                "</ul>"
                "<p>Dado que la GGT alta puede indicar condiciones muy diversas, es imprescindible "
                "que un profesional con acceso a tu historial y pruebas valore el hallazgo. "
                "La detección temprana puede favorecer un tratamiento más eficaz.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya te ayuda a entender tu GGT",
            body_html=(
                "<p>En Norya no hacemos diagnósticos; te ayudamos a prepararte. "
                "<a href=\"/analyze\">Sube tu informe de laboratorio</a> y obtén un resumen claro "
                "que explique tus valores — incluida la GGT — en lenguaje sencillo, con rangos de "
                "referencia y contexto.</p>"
                "<p>Así podrás hablar con tu médico con más seguridad y hacer las preguntas "
                "adecuadas. Norya muestra la GGT junto a ALT, AST y otros marcadores para que veas "
                "el panorama completo. Consulta opciones y precios en nuestra "
                "<a href=\"/pricing\">página de precios</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                "<p><strong>Este contenido es solo informativo y no sustituye el consejo ni el "
                "diagnóstico médico.</strong> La GGT alta puede deberse a muchas causas; solo un "
                "profesional que conozca tu historia puede interpretarla correctamente. Comenta "
                "siempre tus resultados con un médico.</p>"
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
            heading="GGT erhöht: Was bedeutet das in Ihrem Blutbild?",
            body_html=(
                "<p>Wenn Ihr Laborbefund einen erhöhten <strong>GGT-Wert (Gamma-Glutamyl-"
                "Transferase)</strong> zeigt, fragen Sie sich wahrscheinlich: Ist das bedenklich? "
                "Stimmt etwas mit meiner Leber nicht? GGT ist einer der empfindlichsten Marker für "
                "die Gesundheit von Leber und Gallenwegen und kann durch viele verschiedene Faktoren "
                "beeinflusst werden.</p>"
                "<p>Dieser Ratgeber erklärt, was GGT ist, welche Normalwerte gelten, warum der Wert "
                "erhöht sein kann und wann Sie ärztlichen Rat einholen sollten. Unser Ziel ist nicht "
                "die Diagnose — wir möchten Ihnen helfen, Ihre Ergebnisse besser zu verstehen, "
                "damit Sie gut vorbereitet in Ihr Arztgespräch gehen.</p>"
                "<p>Ein erhöhter GGT-Wert allein bedeutet noch keine Erkrankung. Die Einordnung "
                "zusammen mit anderen Leberwerten und dem klinischen Gesamtbild ist entscheidend.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist GGT (Gamma-GT)?",
            body_html=(
                "<p><strong>GGT (Gamma-Glutamyl-Transferase)</strong> ist ein Enzym, das vorwiegend "
                "in der Leber vorkommt, aber auch in Nieren, Bauchspeicheldrüse und Gallengängen. "
                "Es ist am Glutathion-Stoffwechsel beteiligt und unterstützt den Transport von "
                "Aminosäuren über Zellmembranen. Bei Leberschäden oder Gallenabflussstörungen tritt "
                "GGT ins Blut über und der Wert steigt.</p>"
                "<p>GGT ist ein wichtiger Bestandteil der Leberfunktionstests und wird häufig "
                "zusammen mit anderen Leberenzymen wie "
                "<a href=\"/de/blog/was-bedeuten-erhoehte-alt-und-ast-werte\">ALT und AST</a> "
                "bestimmt. Besonders hilfreich ist GGT bei der Frage, ob eine erhöhte ALP "
                "(Alkalische Phosphatase) von der Leber oder vom Knochen stammt.</p>"
                "<p>Das Enzym reagiert äußerst empfindlich auf Alkohol; regelmäßiger Alkoholkonsum "
                "kann den GGT-Wert anheben, noch bevor andere Leberenzyme ansteigen. Deshalb wird "
                "GGT klinisch sowohl zur Beurteilung von Lebererkrankungen als auch zur Überwachung "
                "des Alkoholkonsums eingesetzt.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="GGT-Normalwerte",
            body_html=(
                "<p>Die Referenzbereiche für GGT variieren je nach Labor, Alter und Geschlecht. "
                "Allgemein anerkannte Werte sind:</p>"
                "<ul>"
                "<li><strong>Männer:</strong> 8–61 U/L</li>"
                "<li><strong>Frauen:</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>Männer haben in der Regel höhere GGT-Werte als Frauen. Ein moderater Anstieg "
                "mit zunehmendem Alter ist physiologisch. Manche Labore verwenden leicht abweichende "
                "Bereiche — vergleichen Sie Ihre Werte immer mit den Referenzangaben auf Ihrem "
                "Befund.</p>"
                "<p>Leicht erhöhte Werte (knapp über der Obergrenze) sind nicht immer klinisch "
                "bedeutsam, deutlich erhöhte Werte sollten jedoch ärztlich abgeklärt werden. "
                "Der GGT-Wert muss zusammen mit ALT, AST, ALP und Bilirubin betrachtet werden.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für erhöhte GGT",
            body_html=(
                "<p>Ein erhöhter GGT-Wert kann verschiedene Ursachen haben. Die häufigsten:</p>"
                "<ul>"
                "<li><strong>Alkoholkonsum:</strong> Regelmäßiger oder übermäßiger Alkoholgenuss ist "
                "die häufigste Ursache. Nach Abstinenz sinkt der Wert meist innerhalb weniger Wochen.</li>"
                "<li><strong>Lebererkrankungen:</strong> Fettleber (Steatose), Hepatitis, Zirrhose "
                "und Lebertumore können GGT erhöhen.</li>"
                "<li><strong>Gallenwegserkrankungen:</strong> Gallensteine oder Gallengangstenosen "
                "führen zu einem deutlichen GGT-Anstieg.</li>"
                "<li><strong>Medikamente:</strong> Bestimmte Antiepileptika, Barbiturate, NSAR und "
                "Statine können den Wert anheben.</li>"
                "<li><strong>Pankreatitis:</strong> Eine Entzündung der Bauchspeicheldrüse kann "
                "GGT erhöhen.</li>"
                "<li><strong>Herzinsuffizienz:</strong> Die Leberstauung bei Herzinsuffizienz kann "
                "den Wert steigern.</li>"
                "<li><strong>Diabetes und metabolisches Syndrom:</strong> Insulinresistenz und "
                "die damit verbundene Fettleber tragen zur GGT-Erhöhung bei.</li>"
                "</ul>"
                "<p>Seltener kann ein erhöhter GGT-Wert auf autoimmune Hepatitis, Hämochromatose "
                "oder Morbus Wilson hinweisen. Zur Klärung sind weiterführende Untersuchungen "
                "erforderlich.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome bei erhöhter GGT",
            body_html=(
                "<p>Ein erhöhter GGT-Wert verursacht für sich allein in der Regel keine Symptome; "
                "im Vordergrund stehen die Beschwerden der Grunderkrankung. Häufige Zeichen, die "
                "mit Leber- oder Gallenwegserkrankungen einhergehen können:</p>"
                "<ul>"
                "<li>Schmerzen oder Druckgefühl im rechten Oberbauch</li>"
                "<li>Müdigkeit und allgemeine Schwäche</li>"
                "<li>Übelkeit oder Appetitlosigkeit</li>"
                "<li>Gelbfärbung von Haut oder Augen (Ikterus)</li>"
                "<li>Dunkler Urin oder heller Stuhl</li>"
                "<li>Juckreiz</li>"
                "</ul>"
                "<p>Treten solche Symptome bei erhöhtem GGT auf, sollten Sie zeitnah einen Arzt "
                "aufsuchen. Auch ohne Symptome ist ein dauerhaft erhöhter GGT-Wert — besonders bei "
                "wiederholter Bestätigung — abklärungswürdig.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Tests, die zusammen mit GGT beurteilt werden",
            body_html=(
                "<p>Der GGT-Wert allein liefert keine endgültige Aussage; er sollte gemeinsam mit "
                "folgenden Tests interpretiert werden:</p>"
                "<ul>"
                "<li><strong><a href=\"/de/blog/was-bedeuten-erhoehte-alt-und-ast-werte\">ALT und "
                "AST</a>:</strong> Direkte Marker für Leberzellschäden. Sind sie zusammen mit GGT "
                "erhöht, steigt die Wahrscheinlichkeit einer Lebererkrankung.</li>"
                "<li><strong>ALP (Alkalische Phosphatase):</strong> Gemeinsam erhöhte GGT und ALP "
                "deuten auf Leber- oder Gallenwegsursache; ist nur die ALP erhöht, kann eine "
                "Knochenerkrankung vorliegen.</li>"
                "<li><strong>Bilirubin:</strong> Ein erhöhtes Bilirubin steht in Zusammenhang mit "
                "Ikterus und stützt eine hepatobiliäre Ursache.</li>"
                "<li><strong>Albumin und Gesamteiweiß:</strong> Zur Beurteilung der Syntheseleistung "
                "der Leber.</li>"
                "</ul>"
                "<p>Je nach klinischem Bild kann der Arzt zusätzlich Leber-Ultraschall, "
                "Virushepatitis-Serologie oder Autoimmunmarker veranlassen.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie zum Arzt?",
            body_html=(
                "<p>Besprechen Sie Ihre Ergebnisse mit einem Arzt, wenn:</p>"
                "<ul>"
                "<li>der GGT-Wert deutlich über dem Referenzbereich liegt</li>"
                "<li>andere Leberenzyme (ALT, AST, ALP) ebenfalls erhöht sind</li>"
                "<li>Symptome wie Ikterus, Bauchschmerzen oder unerklärliche Müdigkeit vorliegen</li>"
                "<li>Sie regelmäßig Alkohol trinken oder kürzlich Medikamente gewechselt haben</li>"
                "<li>der GGT-Wert in Folgebefunden erhöht bleibt</li>"
                "</ul>"
                "<p>Da ein erhöhter GGT viele verschiedene Ursachen haben kann, ist es wichtig, "
                "dass ein Arzt, der Ihre Vorgeschichte und übrigen Befunde kennt, den Wert "
                "einordnet. Frühzeitige Abklärung kann helfen, Lebererkrankungen in einem "
                "behandelbaren Stadium zu erkennen.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihren GGT-Wert zu verstehen",
            body_html=(
                "<p>Bei Norya stellen wir keine Diagnosen — wir helfen Ihnen bei der Vorbereitung. "
                "<a href=\"/analyze\">Laden Sie Ihren Laborbefund hoch</a> und erhalten Sie eine "
                "übersichtliche Zusammenfassung, die Ihre Werte — einschließlich GGT — in "
                "verständlicher Sprache mit Referenzbereichen und Kontext erklärt.</p>"
                "<p>So können Sie Ihre Ergebnisse sicherer mit dem Arzt besprechen und gezielt "
                "nachfragen. Norya zeigt GGT zusammen mit ALT, AST und weiteren Markern an, damit "
                "Sie das Gesamtbild sehen. Optionen und Preise finden Sie auf unserer "
                "<a href=\"/pricing\">Preisseite</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                "<p><strong>Dieser Inhalt dient ausschließlich der Information und ersetzt keine "
                "ärztliche Beratung oder Diagnose.</strong> Ein erhöhter GGT-Wert kann viele "
                "Ursachen haben; nur ein Arzt, der Ihre Vorgeschichte kennt, kann den Befund "
                "richtig einordnen. Besprechen Sie Laborergebnisse immer mit einem Arzt.</p>"
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
            heading="GGT élevée : que signifie ce résultat ?",
            body_html=(
                "<p>Si votre bilan sanguin montre une <strong>GGT (Gamma-Glutamyl Transférase)</strong> "
                "élevée, vous vous demandez probablement si c'est grave et si votre foie est "
                "concerné. La GGT est l'un des marqueurs les plus sensibles de la santé du foie et "
                "des voies biliaires, et de nombreux facteurs peuvent l'influencer.</p>"
                "<p>Ce guide explique ce qu'est la GGT, quels sont les taux normaux, les causes "
                "fréquentes d'élévation et quand consulter un médecin. Notre objectif n'est pas de "
                "poser un diagnostic mais de vous aider à mieux comprendre vos résultats afin de "
                "préparer votre consultation.</p>"
                "<p>Une GGT élevée isolément ne signifie pas que vous êtes malade. Son interprétation "
                "doit se faire en regard des autres enzymes hépatiques et de votre contexte "
                "clinique.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu'est-ce que la GGT (Gamma-GT) ?",
            body_html=(
                "<p>La <strong>GGT (Gamma-Glutamyl Transférase)</strong> est une enzyme présente "
                "principalement dans le foie, mais aussi dans les reins, le pancréas et les canaux "
                "biliaires. Elle participe au métabolisme du glutathion et au transport des acides "
                "aminés à travers les membranes cellulaires. En cas de lésion hépatique ou "
                "d'obstruction biliaire, la GGT est libérée dans le sang et son taux augmente.</p>"
                "<p>La GGT fait partie du bilan hépatique et est souvent prescrite en complément "
                "d'autres enzymes comme "
                "<a href=\"/fr/blog/que-signifient-alt-ast-eleves\">l'ALT et l'AST</a>. "
                "Elle est particulièrement utile pour déterminer si une élévation de l'ALP "
                "(phosphatase alcaline) est d'origine hépatique ou osseuse.</p>"
                "<p>Cette enzyme est extrêmement sensible à l'alcool ; une consommation régulière "
                "peut faire monter la GGT avant les autres enzymes hépatiques. C'est pourquoi elle "
                "est couramment utilisée en clinique pour surveiller les maladies du foie et la "
                "consommation d'alcool.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de GGT",
            body_html=(
                "<p>Les valeurs de référence de la GGT varient selon le laboratoire, l'âge et le "
                "sexe. Les fourchettes généralement admises sont :</p>"
                "<ul>"
                "<li><strong>Hommes :</strong> 8–61 U/L</li>"
                "<li><strong>Femmes :</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>Les hommes ont habituellement des taux plus élevés que les femmes. Une légère "
                "augmentation avec l'âge est physiologique. Certains laboratoires appliquent des "
                "normes différentes ; comparez toujours vos résultats aux valeurs de référence "
                "figurant sur votre compte rendu.</p>"
                "<p>Une élévation modérée (juste au-dessus de la limite) n'est pas toujours "
                "significative, mais une élévation nette doit être discutée avec votre médecin. "
                "La GGT doit être interprétée avec l'ALT, l'AST, l'ALP et la bilirubine.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une GGT élevée",
            body_html=(
                "<p>L'élévation de la GGT peut résulter de différentes situations :</p>"
                "<ul>"
                "<li><strong>Consommation d'alcool :</strong> C'est la cause la plus fréquente. "
                "Les taux redescendent généralement en quelques semaines après l'arrêt.</li>"
                "<li><strong>Maladies du foie :</strong> Stéatose hépatique, hépatite, cirrhose et "
                "tumeurs du foie peuvent élever la GGT.</li>"
                "<li><strong>Obstruction des voies biliaires :</strong> Calculs biliaires ou "
                "sténoses du cholédoque provoquent une hausse marquée.</li>"
                "<li><strong>Médicaments :</strong> Antiépileptiques, barbituriques, AINS et "
                "statines peuvent augmenter la GGT.</li>"
                "<li><strong>Pancréatite :</strong> L'inflammation du pancréas peut l'élever.</li>"
                "<li><strong>Insuffisance cardiaque :</strong> La congestion hépatique secondaire "
                "peut entraîner une hausse.</li>"
                "<li><strong>Diabète et syndrome métabolique :</strong> L'insulinorésistance et la "
                "stéatose associée contribuent à l'élévation.</li>"
                "</ul>"
                "<p>Plus rarement, la GGT peut signaler une hépatite auto-immune, une "
                "hémochromatose ou une maladie de Wilson. Des examens complémentaires sont "
                "nécessaires pour en identifier la cause.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes associés à une GGT élevée",
            body_html=(
                "<p>Une GGT élevée seule provoque rarement des symptômes ; ce sont ceux de "
                "l'affection sous-jacente qui prédominent. Les signes fréquents accompagnant "
                "les pathologies hépatiques ou biliaires :</p>"
                "<ul>"
                "<li>Douleur ou gêne dans l'hypocondre droit</li>"
                "<li>Fatigue et faiblesse générale</li>"
                "<li>Nausées ou perte d'appétit</li>"
                "<li>Jaunissement de la peau ou des yeux (ictère)</li>"
                "<li>Urines foncées ou selles décolorées</li>"
                "<li>Démangeaisons</li>"
                "</ul>"
                "<p>Si vous présentez ces symptômes avec une GGT élevée, consultez rapidement. "
                "Même sans symptôme, une GGT durablement haute mérite une investigation.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens évalués avec la GGT",
            body_html=(
                "<p>La GGT seule ne fournit pas de diagnostic ; elle doit être interprétée avec :</p>"
                "<ul>"
                "<li><strong><a href=\"/fr/blog/que-signifient-alt-ast-eleves\">ALT et AST</a> :"
                "</strong> Marqueurs directs de lésion hépatocellulaire. Leur élévation concomitante "
                "avec la GGT renforce la probabilité d'une atteinte hépatique.</li>"
                "<li><strong>ALP (Phosphatase alcaline) :</strong> GGT et ALP élevées ensemble "
                "orientent vers une cause hépatique ou biliaire ; l'ALP seule élevée peut indiquer "
                "une pathologie osseuse.</li>"
                "<li><strong>Bilirubine :</strong> Son élévation est associée à l'ictère et "
                "soutient une cause hépatobiliaire.</li>"
                "<li><strong>Albumine et protéines totales :</strong> Pour évaluer la fonction de "
                "synthèse du foie.</li>"
                "</ul>"
                "<p>Selon le contexte, le médecin peut aussi prescrire une échographie hépatique, "
                "une sérologie virale ou des marqueurs auto-immuns.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Parlez de vos résultats à un médecin si :</p>"
                "<ul>"
                "<li>Votre GGT dépasse nettement les valeurs de référence</li>"
                "<li>D'autres enzymes hépatiques (ALT, AST, ALP) sont également élevées</li>"
                "<li>Vous avez un ictère, des douleurs abdominales ou une fatigue inexpliquée</li>"
                "<li>Vous consommez de l'alcool régulièrement ou avez changé de médicament "
                "récemment</li>"
                "<li>La GGT reste élevée lors de contrôles successifs</li>"
                "</ul>"
                "<p>Une GGT élevée pouvant refléter des causes très diverses, seul un médecin "
                "connaissant votre dossier et vos autres résultats peut l'interpréter. Un bilan "
                "précoce peut favoriser une prise en charge plus efficace.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre votre GGT",
            body_html=(
                "<p>Chez Norya, nous ne diagnostiquons pas — nous vous aidons à vous préparer. "
                "<a href=\"/analyze\">Téléchargez votre bilan</a> et obtenez un résumé clair qui "
                "explique vos valeurs — dont la GGT — dans un langage simple, avec les intervalles "
                "de référence et du contexte.</p>"
                "<p>Vous pourrez ainsi aborder votre consultation plus sereinement et poser les "
                "bonnes questions. Norya affiche la GGT aux côtés de l'ALT, l'AST et d'autres "
                "marqueurs pour une vue d'ensemble. Consultez nos options et tarifs sur notre "
                "<a href=\"/pricing\">page de tarifs</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                "<p><strong>Ce contenu est fourni à titre informatif uniquement et ne remplace pas "
                "un avis ou un diagnostic médical.</strong> Une GGT élevée peut avoir de nombreuses "
                "causes ; seul un professionnel de santé connaissant votre historique peut "
                "interpréter votre résultat. Discutez toujours de vos résultats avec un médecin.</p>"
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
            heading="GGT alta: cosa significa nelle analisi del sangue?",
            body_html=(
                "<p>Se il referto mostra un valore elevato di <strong>GGT (Gamma-Glutamil "
                "Transferasi)</strong>, è naturale chiedersi: è grave? C'è un problema al fegato? "
                "La GGT è uno dei marcatori più sensibili della salute epatica e delle vie biliari "
                "e può essere influenzata da numerosi fattori.</p>"
                "<p>Questa guida spiega cos'è la GGT, quali sono i valori normali, le cause più "
                "comuni di elevazione e quando è opportuno consultare il medico. Il nostro obiettivo "
                "non è formulare diagnosi ma aiutarvi a comprendere i risultati per affrontare il "
                "colloquio medico con maggiore consapevolezza.</p>"
                "<p>Un valore elevato di GGT, da solo, non indica necessariamente una malattia. "
                "È fondamentale interpretarlo insieme agli altri enzimi epatici e al quadro "
                "clinico complessivo.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Che cos'è la GGT (Gamma-GT)?",
            body_html=(
                "<p>La <strong>GGT (Gamma-Glutamil Transferasi)</strong> è un enzima presente "
                "principalmente nel fegato, ma anche nei reni, nel pancreas e nei dotti biliari. "
                "Interviene nel metabolismo del glutatione e nel trasporto degli amminoacidi "
                "attraverso le membrane cellulari. In caso di danno epatico o ostruzione biliare, "
                "la GGT viene rilasciata nel sangue e i livelli aumentano.</p>"
                "<p>La GGT fa parte del pannello degli esami epatici e viene spesso richiesta "
                "insieme ad altri enzimi come "
                "<a href=\"/it/blog/cosa-significano-alt-ast-alti\">ALT e AST</a>. "
                "È particolarmente utile per distinguere se un'ALP (fosfatasi alcalina) elevata "
                "sia di origine epatica o ossea.</p>"
                "<p>Questo enzima è estremamente sensibile all'alcol: un consumo regolare può "
                "innalzare la GGT prima degli altri enzimi epatici. Per questo motivo viene "
                "comunemente utilizzata per monitorare sia le malattie del fegato sia il consumo "
                "di alcol.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali della GGT",
            body_html=(
                "<p>Gli intervalli di riferimento della GGT variano in base al laboratorio, all'età "
                "e al sesso. I valori generalmente accettati sono:</p>"
                "<ul>"
                "<li><strong>Uomini:</strong> 8–61 U/L</li>"
                "<li><strong>Donne:</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>Gli uomini tendono ad avere valori più alti delle donne. Un lieve aumento con "
                "l'età è fisiologico. Alcuni laboratori possono adottare range diversi; confrontate "
                "sempre i vostri risultati con i valori di riferimento riportati nel referto.</p>"
                "<p>Elevazioni modeste (appena sopra il limite superiore) possono non avere "
                "significato clinico, mentre valori nettamente elevati vanno discussi con il medico. "
                "La GGT va interpretata insieme ad ALT, AST, ALP e bilirubina.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di GGT alta",
            body_html=(
                "<p>L'elevazione della GGT può dipendere da diverse condizioni:</p>"
                "<ul>"
                "<li><strong>Consumo di alcol:</strong> È la causa più frequente. I valori "
                "tendono a normalizzarsi entro poche settimane dalla sospensione.</li>"
                "<li><strong>Malattie epatiche:</strong> Steatosi, epatite, cirrosi e tumori "
                "del fegato possono innalzare la GGT.</li>"
                "<li><strong>Ostruzione delle vie biliari:</strong> Calcoli biliari o stenosi "
                "del coledoco causano un aumento marcato.</li>"
                "<li><strong>Farmaci:</strong> Antiepilettici, barbiturici, FANS e statine "
                "possono aumentare la GGT.</li>"
                "<li><strong>Pancreatite:</strong> L'infiammazione del pancreas può elevarla.</li>"
                "<li><strong>Insufficienza cardiaca:</strong> La congestione epatica secondaria "
                "può alzare il valore.</li>"
                "<li><strong>Diabete e sindrome metabolica:</strong> Insulino-resistenza e "
                "steatosi associata contribuiscono all'innalzamento.</li>"
                "</ul>"
                "<p>Più raramente, la GGT elevata può segnalare epatite autoimmune, emocromatosi "
                "o malattia di Wilson. Ulteriori accertamenti sono necessari per identificare la "
                "causa.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi associati a GGT alta",
            body_html=(
                "<p>La GGT elevata di per sé raramente provoca sintomi; prevalgono quelli della "
                "patologia sottostante. Segni comuni che possono accompagnare problemi epatici o "
                "biliari:</p>"
                "<ul>"
                "<li>Dolore o fastidio nell'ipocondrio destro</li>"
                "<li>Stanchezza e debolezza generale</li>"
                "<li>Nausea o inappetenza</li>"
                "<li>Colorazione giallastra di pelle o occhi (ittero)</li>"
                "<li>Urine scure o feci chiare</li>"
                "<li>Prurito</li>"
                "</ul>"
                "<p>Se avvertite questi sintomi e la GGT è alta, consultate il medico. Anche senza "
                "sintomi, una GGT persistentemente elevata merita approfondimento.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami valutati insieme alla GGT",
            body_html=(
                "<p>La GGT da sola non fornisce una diagnosi; va interpretata con:</p>"
                "<ul>"
                "<li><strong><a href=\"/it/blog/cosa-significano-alt-ast-alti\">ALT e AST</a>:"
                "</strong> Marcatori diretti di danno epatocellulare. Se elevati insieme alla GGT, "
                "aumenta la probabilità di malattia epatica.</li>"
                "<li><strong>ALP (Fosfatasi alcalina):</strong> GGT e ALP elevate insieme "
                "suggeriscono un'origine epatica o biliare; se solo l'ALP è alta, può trattarsi "
                "di patologia ossea.</li>"
                "<li><strong>Bilirubina:</strong> La sua elevazione è correlata all'ittero e "
                "supporta una causa epatobiliare.</li>"
                "<li><strong>Albumina e proteine totali:</strong> Valutano la funzione sintetica "
                "del fegato.</li>"
                "</ul>"
                "<p>A seconda del quadro clinico, il medico può richiedere ecografia epatica, "
                "sierologia per epatiti virali o marker autoimmuni.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Parlate con il medico se:</p>"
                "<ul>"
                "<li>La GGT è nettamente sopra l'intervallo di riferimento</li>"
                "<li>Anche ALT, AST o ALP sono elevate</li>"
                "<li>Avete ittero, dolore addominale o stanchezza inspiegabile</li>"
                "<li>Bevete alcolici regolarmente o avete cambiato farmaci di recente</li>"
                "<li>La GGT resta alta nei controlli successivi</li>"
                "</ul>"
                "<p>Poiché la GGT alta può riflettere condizioni molto diverse, solo un medico "
                "che conosce la vostra storia e i vostri esami può interpretarla. Un controllo "
                "precoce può favorire l'individuazione tempestiva di patologie epatiche.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a capire la tua GGT",
            body_html=(
                "<p>Da Norya non facciamo diagnosi — vi aiutiamo a prepararvi. "
                "<a href=\"/analyze\">Caricate il vostro referto</a> e ricevete un riepilogo chiaro "
                "che spiega i vostri valori — compresa la GGT — in linguaggio semplice, con "
                "intervalli di riferimento e contesto.</p>"
                "<p>Così potrete affrontare il colloquio medico con maggiore sicurezza. Norya "
                "mostra la GGT accanto ad ALT, AST e altri marcatori per offrirvi una visione "
                "d'insieme. Consultate opzioni e prezzi sulla nostra "
                "<a href=\"/pricing\">pagina prezzi</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza",
            body_html=(
                "<p><strong>Questo contenuto ha finalità esclusivamente informative e non "
                "sostituisce il parere o la diagnosi medica.</strong> La GGT alta può avere "
                "numerose cause; solo un professionista che conosce la vostra storia può "
                "interpretarla correttamente. Discutete sempre i risultati con il vostro "
                "medico.</p>"
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
            heading="GGT גבוה: מה המשמעות בבדיקת הדם שלך?",
            body_html=(
                "<p>אם תוצאות המעבדה שלך מראות רמה מוגברת של <strong>GGT (גמא-גלוטמיל "
                "טרנספראז)</strong>, כנראה שאתה שואל: האם זה רציני? האם יש בעיה בכבד שלי? "
                "GGT הוא אחד הסמנים הרגישים ביותר לבריאות הכבד ודרכי המרה, ומגוון רחב של "
                "גורמים יכולים להשפיע עליו.</p>"
                "<p>מדריך זה מסביר מהו GGT, מהם הערכים התקינים, הגורמים השכיחים לעלייה ומתי "
                "כדאי לפנות לרופא. המטרה שלנו אינה לאבחן — אלא לעזור לך להבין את התוצאות "
                "כדי שתוכל להגיע לפגישה עם הרופא מוכן יותר.</p>"
                "<p>GGT מוגבר לבדו אינו מעיד בהכרח על מחלה. פירושו חייב להיעשות לצד "
                "אנזימי כבד אחרים והתמונה הקלינית הכוללת.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהו GGT (גמא-GT)?",
            body_html=(
                "<p><strong>GGT (גמא-גלוטמיל טרנספראז)</strong> הוא אנזים הנמצא בעיקר בכבד, "
                "אך גם בכליות, בלבלב ובדרכי המרה. הוא ממלא תפקיד במטבוליזם של גלוטתיון ומסייע "
                "בהובלת חומצות אמינו דרך ממברנות התא. כאשר הכבד ניזוק או כשזרימת המרה חסומה, "
                "GGT דולף לזרם הדם ורמתו עולה.</p>"
                "<p>GGT הוא מרכיב חשוב בפאנל תפקודי הכבד ונבדק לעיתים קרובות לצד אנזימים "
                "כמו <a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">ALT ו-AST</a>. "
                "הוא שימושי במיוחד להבחנה אם ALP (פוספטאז אלקליין) מוגבר ממקור כבדי או גרמי.</p>"
                "<p>אנזים זה רגיש במיוחד לאלכוהול; צריכה קבועה יכולה להעלות את ה-GGT עוד לפני "
                "שאנזימי כבד אחרים עולים. לכן משתמשים ב-GGT בקליניקה הן למעקב אחר מחלות כבד "
                "והן לניטור צריכת אלכוהול.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחים תקינים של GGT",
            body_html=(
                "<p>טווחי הייחוס של GGT משתנים לפי מעבדה, גיל ומין. הטווחים המקובלים:</p>"
                "<ul>"
                "<li><strong>גברים:</strong> 8–61 U/L</li>"
                "<li><strong>נשים:</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>לגברים ערכים גבוהים יותר בדרך כלל מאשר לנשים. עלייה קלה עם הגיל נחשבת "
                "תקינה. מעבדות מסוימות עשויות להשתמש בטווחים שונים מעט — השוו תמיד את התוצאות "
                "שלכם לערכי הייחוס בדוח.</p>"
                "<p>עליות קלות (מעט מעל הגבול העליון) לא תמיד משמעותיות קלינית, אבל ערכים "
                "מוגברים בבירור צריכים להידון עם רופא. יש לפרש GGT יחד עם ALT, AST, ALP "
                "ובילירובין.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים ל-GGT גבוה",
            body_html=(
                "<p>GGT מוגבר יכול לנבוע ממצבים שונים. הנפוצים ביותר:</p>"
                "<ul>"
                "<li><strong>צריכת אלכוהול:</strong> צריכה קבועה או מוגזמת היא הגורם השכיח "
                "ביותר. הרמות יורדות בדרך כלל תוך שבועות מהפסקה.</li>"
                "<li><strong>מחלות כבד:</strong> כבד שומני, דלקת כבד (הפטיטיס), שחמת ו"
                "גידולי כבד יכולים להעלות GGT.</li>"
                "<li><strong>חסימת דרכי מרה:</strong> אבני מרה או היצרות בצינור המרה גורמים "
                "לעלייה ניכרת.</li>"
                "<li><strong>תרופות:</strong> תרופות אנטי-אפילפטיות, ברביטורטים, NSAIDs "
                "וסטטינים עשויים להעלות GGT.</li>"
                "<li><strong>דלקת לבלב:</strong> דלקת בלבלב יכולה לגרום לעלייה.</li>"
                "<li><strong>אי-ספיקת לב:</strong> גודש כבדי עקב אי-ספיקת לב יכול להעלות "
                "את הערך.</li>"
                "<li><strong>סוכרת ותסמונת מטבולית:</strong> תנגודת לאינסולין וכבד שומני נלווה "
                "תורמים לעלייה.</li>"
                "</ul>"
                "<p>במקרים נדירים, GGT מוגבר עשוי להצביע על דלקת כבד אוטואימונית, "
                "המוכרומטוזיס או מחלת וילסון. נדרשות בדיקות נוספות לזיהוי הסיבה.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים הקשורים ל-GGT גבוה",
            body_html=(
                "<p>GGT מוגבר לבדו לרוב אינו גורם לתסמינים ניכרים; בדרך כלל שולטים "
                "התסמינים של המצב הבסיסי. סימנים שכיחים שעשויים ללוות בעיות בכבד או "
                "בדרכי המרה:</p>"
                "<ul>"
                "<li>כאב או אי-נוחות בבטן הימנית העליונה</li>"
                "<li>עייפות וחולשה כללית</li>"
                "<li>בחילה או ירידה בתיאבון</li>"
                "<li>הצהבה של העור או לובן העיניים (צהבת)</li>"
                "<li>שתן כהה או צואה בהירה</li>"
                "<li>גירוד</li>"
                "</ul>"
                "<p>אם יש לכם תסמינים אלו לצד GGT גבוה, פנו לרופא. גם ללא תסמינים, GGT "
                "שנשאר מוגבר — במיוחד בבדיקות חוזרות — ראוי לבירור.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות שנבדקות לצד GGT",
            body_html=(
                "<p>תוצאת GGT לבדה אינה מספיקה לאבחנה; יש לפרשה יחד עם:</p>"
                "<ul>"
                "<li><strong><a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">ALT "
                "ו-AST</a>:</strong> סמנים ישירים לנזק לתאי כבד. עלייה משותפת עם GGT מגבירה "
                "את הסבירות למחלת כבד.</li>"
                "<li><strong>ALP (פוספטאז אלקליין):</strong> GGT ו-ALP מוגברים יחד מצביעים "
                "על מקור כבדי או מרי; ALP מוגבר לבדו עשוי להעיד על בעיה גרמית.</li>"
                "<li><strong>בילירובין:</strong> עלייתו קשורה לצהבת ותומכת בסיבה "
                "הפטובילארית.</li>"
                "<li><strong>אלבומין וחלבון כולל:</strong> משמשים להערכת תפקוד הסינתזה של "
                "הכבד.</li>"
                "</ul>"
                "<p>בהתאם לתמונה הקלינית, הרופא עשוי לבקש גם אולטרסאונד כבד, סרולוגיה "
                "לדלקת כבד נגיפית או סמנים אוטואימוניים.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>כדאי לשוחח עם רופא אם:</p>"
                "<ul>"
                "<li>ה-GGT שלך גבוה משמעותית מטווח הייחוס</li>"
                "<li>אנזימי כבד נוספים (ALT, AST, ALP) גם מוגברים</li>"
                "<li>יש לך צהבת, כאבי בטן או עייפות בלתי מוסברת</li>"
                "<li>אתה צורך אלכוהול באופן קבוע או החלפת תרופות לאחרונה</li>"
                "<li>GGT נשאר מוגבר בבדיקות חוזרות</li>"
                "</ul>"
                "<p>מכיוון ש-GGT מוגבר יכול להצביע על מצבים רבים ושונים, חשוב שרופא "
                "המכיר את ההיסטוריה הרפואית שלך ותוצאות בדיקות נוספות יעריך את הממצא. "
                "הערכה מוקדמת יכולה לסייע באיתור מצבי כבד בשלב הניתן לטיפול.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת לך להבין את תוצאת ה-GGT",
            body_html=(
                "<p>ב-Norya אנחנו לא מאבחנים — אנחנו עוזרים לך להתכונן. "
                "<a href=\"/analyze\">העלו את דוח המעבדה שלכם</a> וקבלו סיכום ברור "
                "ומובנה שמסביר את הערכים — כולל GGT — בשפה פשוטה, עם טווחי ייחוס "
                "והקשר.</p>"
                "<p>כך תוכלו לדון בתוצאות עם הרופא בביטחון רב יותר ולשאול את השאלות "
                "הנכונות. Norya מציגה את GGT לצד ALT, AST וסמנים נוספים כדי שתראו את "
                "התמונה הכוללת. לאפשרויות ומחירים, בקרו ב"
                "<a href=\"/pricing\">עמוד המחירים</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הבהרה",
            body_html=(
                "<p><strong>תוכן זה מיועד למטרות מידע בלבד ואינו מחליף ייעוץ או אבחנה "
                "רפואית.</strong> GGT מוגבר יכול לנבוע מסיבות רבות; רק איש מקצוע רפואי "
                "המכיר את ההיסטוריה שלך יכול לפרש את התוצאה נכון. דונו תמיד בתוצאות "
                "המעבדה עם רופא.</p>"
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
            heading="GGT हाई: ब्लड टेस्ट में इसका क्या मतलब है?",
            body_html=(
                "<p>अगर आपकी लैब रिपोर्ट में <strong>GGT (गामा-ग्लूटामिल ट्रांसफ़रेज़)</strong> "
                "की रीडिंग बढ़ी हुई दिखती है, तो स्वाभाविक रूप से आप सोचेंगे: क्या यह गंभीर है? "
                "क्या मेरे लिवर में कोई समस्या है? GGT लिवर और पित्त नली (बाइल डक्ट) की सेहत "
                "के सबसे संवेदनशील मार्करों में से एक है और इसे कई कारक प्रभावित कर सकते हैं।</p>"
                "<p>यह गाइड बताती है कि GGT क्या है, सामान्य और उच्च मान क्या होते हैं, GGT बढ़ने "
                "के प्रमुख कारण कौन-से हैं और डॉक्टर से कब मिलना चाहिए। हमारा उद्देश्य निदान "
                "करना नहीं है — बल्कि आपको परिणाम समझने में मदद करना है ताकि आप डॉक्टर से बेहतर "
                "तैयारी के साथ बात कर सकें।</p>"
                "<p>अकेले बढ़ा हुआ GGT किसी बीमारी की पुष्टि नहीं करता। इसे अन्य लिवर "
                "एंज़ाइम्स और आपकी क्लीनिकल स्थिति के साथ मिलाकर देखना ज़रूरी है।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="GGT (गामा-GT) क्या है?",
            body_html=(
                "<p><strong>GGT (गामा-ग्लूटामिल ट्रांसफ़रेज़)</strong> एक एंज़ाइम है जो मुख्य "
                "रूप से लिवर में पाया जाता है, लेकिन किडनी, पैंक्रियास और पित्त नलिकाओं में भी "
                "मौजूद होता है। यह ग्लूटाथिओन मेटाबॉलिज़्म में भाग लेता है और कोशिका झिल्ली के "
                "आर-पार अमीनो एसिड के परिवहन में सहायता करता है। जब लिवर क्षतिग्रस्त होता है "
                "या पित्त प्रवाह बाधित होता है, तो GGT रक्तप्रवाह में रिसता है।</p>"
                "<p>GGT लिवर फ़ंक्शन टेस्ट पैनल का महत्वपूर्ण हिस्सा है और अक्सर "
                "<a href=\"/hi/blog/high-alt-ast-levels-ka-matlab\">ALT और AST</a> जैसे अन्य "
                "लिवर एंज़ाइम्स के साथ माँगा जाता है। यह विशेष रूप से यह पता लगाने में "
                "उपयोगी है कि बढ़ा हुआ ALP (एल्केलाइन फ़ॉस्फ़ेटेज़) लिवर से है या हड्डी से।</p>"
                "<p>यह एंज़ाइम अल्कोहल के प्रति अत्यंत संवेदनशील है; नियमित शराब सेवन GGT को "
                "अन्य लिवर एंज़ाइम्स से पहले बढ़ा सकता है। इसलिए GGT का उपयोग लिवर रोगों "
                "और अल्कोहल सेवन दोनों की निगरानी के लिए किया जाता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="GGT सामान्य मान (नॉर्मल रेंज)",
            body_html=(
                "<p>GGT की रेफ़रेंस रेंज लैब, उम्र और लिंग के अनुसार भिन्न हो सकती है। "
                "सामान्य रूप से स्वीकृत मान:</p>"
                "<ul>"
                "<li><strong>पुरुष:</strong> 8–61 U/L</li>"
                "<li><strong>महिलाएँ:</strong> 5–36 U/L</li>"
                "</ul>"
                "<p>पुरुषों में मान आमतौर पर महिलाओं से अधिक होते हैं। उम्र के साथ हल्की "
                "वृद्धि सामान्य मानी जाती है। कुछ लैब अलग रेंज इस्तेमाल कर सकती हैं — "
                "अपने परिणामों की तुलना हमेशा अपनी रिपोर्ट की रेफ़रेंस वैल्यू से करें।</p>"
                "<p>हल्की बढ़ोतरी (ऊपरी सीमा से थोड़ा ऊपर) हमेशा चिंताजनक नहीं होती, लेकिन "
                "स्पष्ट वृद्धि के बारे में डॉक्टर से ज़रूर बात करें। GGT को ALT, AST, ALP "
                "और बिलीरुबिन के साथ मिलाकर देखना चाहिए।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="GGT बढ़ने के कारण",
            body_html=(
                "<p>GGT बढ़ने के कई कारण हो सकते हैं। सबसे आम:</p>"
                "<ul>"
                "<li><strong>अल्कोहल सेवन:</strong> नियमित या अत्यधिक शराब सबसे आम कारण "
                "है। छोड़ने के कुछ हफ़्तों में मान आमतौर पर गिर जाते हैं।</li>"
                "<li><strong>लिवर रोग:</strong> फ़ैटी लिवर (स्टीटोसिस), हेपेटाइटिस, सिरोसिस "
                "और लिवर ट्यूमर GGT बढ़ा सकते हैं।</li>"
                "<li><strong>पित्त नली में रुकावट:</strong> पित्त की पथरी या नली में सिकुड़न "
                "से GGT काफ़ी बढ़ सकता है।</li>"
                "<li><strong>दवाइयाँ:</strong> कुछ एंटी-एपिलेप्टिक, बार्बिट्यूरेट्स, NSAIDs "
                "और स्टैटिन GGT बढ़ा सकती हैं।</li>"
                "<li><strong>पैंक्रियाटाइटिस:</strong> पैंक्रियास की सूजन GGT बढ़ा सकती है।</li>"
                "<li><strong>हार्ट फ़ेल्योर:</strong> कंजेस्टिव हार्ट फ़ेल्योर से लिवर में "
                "जमाव GGT बढ़ा सकता है।</li>"
                "<li><strong>डायबिटीज़ और मेटाबॉलिक सिंड्रोम:</strong> इंसुलिन रेज़िस्टेंस "
                "और उससे जुड़ा फ़ैटी लिवर GGT बढ़ाने में योगदान करता है।</li>"
                "</ul>"
                "<p>दुर्लभ मामलों में, बढ़ा हुआ GGT ऑटोइम्यून हेपेटाइटिस, हीमोक्रोमैटोसिस "
                "या विल्सन रोग का संकेत हो सकता है। कारण जानने के लिए अतिरिक्त जाँच "
                "ज़रूरी होती है।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="GGT बढ़ने से जुड़े लक्षण",
            body_html=(
                "<p>अकेले बढ़ा हुआ GGT शायद ही कभी स्पष्ट लक्षण देता है; आमतौर पर अंतर्निहित "
                "स्थिति के लक्षण प्रमुख होते हैं। लिवर या पित्त नली की समस्या के संभावित "
                "संकेत:</p>"
                "<ul>"
                "<li>दाईं ओर ऊपरी पेट में दर्द या बेचैनी</li>"
                "<li>थकान और कमज़ोरी</li>"
                "<li>मतली या भूख न लगना</li>"
                "<li>त्वचा या आँखों में पीलापन (पीलिया)</li>"
                "<li>गहरे रंग का पेशाब या हल्के रंग का मल</li>"
                "<li>खुजली</li>"
                "</ul>"
                "<p>यदि ये लक्षण हैं और GGT भी बढ़ा हुआ है, तो तुरंत डॉक्टर से मिलें। "
                "बिना लक्षणों के भी बार-बार बढ़ा हुआ GGT जाँच का हक़दार है।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="GGT के साथ देखी जाने वाली टेस्ट",
            body_html=(
                "<p>अकेली GGT रिपोर्ट पक्का जवाब नहीं देती; इसे इन टेस्ट के साथ पढ़ना "
                "चाहिए:</p>"
                "<ul>"
                "<li><strong><a href=\"/hi/blog/high-alt-ast-levels-ka-matlab\">ALT और AST</a>:"
                "</strong> लिवर कोशिका क्षति के सीधे मार्कर। GGT के साथ बढ़ने पर लिवर रोग "
                "की संभावना बढ़ जाती है।</li>"
                "<li><strong>ALP (एल्केलाइन फ़ॉस्फ़ेटेज़):</strong> GGT और ALP दोनों बढ़े "
                "हों तो लिवर या पित्त नली का कारण संभव; सिर्फ़ ALP बढ़ा हो तो हड्डी "
                "संबंधी कारण हो सकता है।</li>"
                "<li><strong>बिलीरुबिन:</strong> इसकी बढ़ोतरी पीलिया से जुड़ी है और "
                "हेपेटोबिलरी कारण को सपोर्ट करती है।</li>"
                "<li><strong>एल्ब्यूमिन और कुल प्रोटीन:</strong> लिवर की सिंथेसिस क्षमता "
                "का मूल्यांकन करने में उपयोगी।</li>"
                "</ul>"
                "<p>क्लीनिकल तस्वीर के अनुसार डॉक्टर लिवर अल्ट्रासाउंड, वायरल हेपेटाइटिस "
                "सीरोलॉजी या ऑटोइम्यून मार्कर भी माँग सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>इन स्थितियों में डॉक्टर से बात करें:</p>"
                "<ul>"
                "<li>GGT रेफ़रेंस रेंज से काफ़ी ऊपर है</li>"
                "<li>ALT, AST या ALP जैसे अन्य लिवर एंज़ाइम भी बढ़े हुए हैं</li>"
                "<li>पीलिया, पेट दर्द या अकारण थकान जैसे लक्षण हैं</li>"
                "<li>आप नियमित रूप से शराब पीते हैं या हाल ही में दवाइयाँ बदली हैं</li>"
                "<li>बार-बार की जाँच में GGT ऊँचा बना रहता है</li>"
                "</ul>"
                "<p>चूँकि बढ़ा हुआ GGT कई अलग-अलग स्थितियों का संकेत हो सकता है, यह ज़रूरी "
                "है कि आपकी मेडिकल हिस्ट्री और अन्य रिपोर्ट जानने वाला डॉक्टर इसकी व्याख्या "
                "करे। शुरुआती जाँच लिवर की समस्याओं को इलाज योग्य अवस्था में पकड़ने में "
                "मदद कर सकती है।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपकी GGT रिपोर्ट समझने में कैसे मदद करता है",
            body_html=(
                "<p>Norya पर हम निदान नहीं करते — हम आपको तैयार होने में मदद करते हैं। "
                "<a href=\"/analyze\">अपनी लैब रिपोर्ट अपलोड करें</a> और एक स्पष्ट, "
                "संरचित सारांश पाएँ जो आपके सभी मान — GGT सहित — आसान भाषा में, "
                "रेफ़रेंस रेंज और संदर्भ के साथ समझाता है।</p>"
                "<p>इससे डॉक्टर से बात करना और सही सवाल पूछना आसान हो जाता है। Norya GGT "
                "को ALT, AST और अन्य संबंधित मार्करों के साथ दिखाता है ताकि आप पूरी तस्वीर "
                "देख सकें। विकल्पों और कीमतों के लिए हमारा "
                "<a href=\"/pricing\">प्राइसिंग पेज</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                "<p><strong>यह सामग्री केवल सूचनात्मक उद्देश्यों के लिए है और चिकित्सा "
                "सलाह या निदान का विकल्प नहीं है।</strong> बढ़ा हुआ GGT कई कारणों से हो "
                "सकता है; केवल आपकी हिस्ट्री और संदर्भ जानने वाला स्वास्थ्य पेशेवर ही "
                "आपके परिणाम की सही व्याख्या कर सकता है। लैब रिपोर्ट हमेशा डॉक्टर के "
                "साथ चर्चा करें।</p>"
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
            heading="GGT مرتفع: ماذا يعني في تحليل الدم؟",
            body_html=(
                "<p>إذا أظهر تقرير المختبر ارتفاعاً في <strong>GGT (غاما غلوتاميل "
                "ترانسفيراز)</strong>، فمن الطبيعي أن تتساءل: هل هذا خطير؟ هل هناك مشكلة في "
                "كبدي؟ يُعدّ GGT من أكثر المؤشرات حساسيةً لصحة الكبد والقنوات الصفراوية، "
                "ويمكن أن يتأثر بعوامل متعددة.</p>"
                "<p>يشرح هذا الدليل ماهية GGT والقيم الطبيعية والأسباب الشائعة للارتفاع ومتى "
                "ينبغي مراجعة الطبيب. هدفنا ليس التشخيص — بل مساعدتك على فهم نتائجك لتكون "
                "أكثر استعداداً عند زيارة الطبيب.</p>"
                "<p>ارتفاع GGT وحده لا يعني بالضرورة وجود مرض. تفسيره يجب أن يكون إلى جانب "
                "إنزيمات الكبد الأخرى والصورة السريرية الكاملة.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو GGT (غاما-GT)؟",
            body_html=(
                "<p><strong>GGT (غاما غلوتاميل ترانسفيراز)</strong> هو إنزيم يتواجد بشكل "
                "رئيسي في الكبد، وكذلك في الكلى والبنكرياس والقنوات الصفراوية. يلعب دوراً في "
                "أيض الغلوتاثيون ويُسهّل نقل الأحماض الأمينية عبر أغشية الخلايا. عند تضرر "
                "الكبد أو انسداد تدفق الصفراء، يتسرب GGT إلى مجرى الدم وترتفع مستوياته.</p>"
                "<p>يُعدّ GGT جزءاً مهماً من فحوصات وظائف الكبد ويُطلب عادةً مع إنزيمات "
                "أخرى مثل <a href=\"/ar/blog/ma-dha-taani-mustawayat-alt-wa-ast-alalia\">ALT "
                "وAST</a>. وهو مفيد بشكل خاص في تحديد ما إذا كان ارتفاع ALP (الفوسفاتاز "
                "القلوي) من مصدر كبدي أو عظمي.</p>"
                "<p>هذا الإنزيم شديد الحساسية للكحول؛ فالاستهلاك المنتظم قد يرفع GGT قبل "
                "ارتفاع إنزيمات الكبد الأخرى. لهذا يُستخدم سريرياً لمراقبة أمراض الكبد "
                "واستهلاك الكحول على حدّ سواء.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية لـ GGT",
            body_html=(
                "<p>تختلف النطاقات المرجعية لـ GGT حسب المختبر والعمر والجنس. القيم "
                "المقبولة عموماً:</p>"
                "<ul>"
                "<li><strong>الرجال:</strong> 8–61 وحدة/لتر</li>"
                "<li><strong>النساء:</strong> 5–36 وحدة/لتر</li>"
                "</ul>"
                "<p>تكون القيم عند الرجال أعلى عادةً من النساء. الارتفاع الطفيف مع التقدم "
                "في العمر يُعتبر طبيعياً. قد تستخدم بعض المختبرات نطاقات مختلفة قليلاً — "
                "قارن دائماً نتائجك بقيم المرجع الموجودة في تقريرك.</p>"
                "<p>الارتفاعات الطفيفة (فوق الحد الأعلى بقليل) قد لا تكون ذات دلالة سريرية، "
                "لكن الارتفاعات الواضحة يجب مناقشتها مع الطبيب. ينبغي تفسير GGT مع ALT "
                "وAST وALP والبيليروبين.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع GGT",
            body_html=(
                "<p>يمكن أن ينتج ارتفاع GGT عن حالات متعددة. الأكثر شيوعاً:</p>"
                "<ul>"
                "<li><strong>تناول الكحول:</strong> الاستهلاك المنتظم أو المفرط هو السبب "
                "الأشيع. تنخفض المستويات عادةً خلال أسابيع من التوقف.</li>"
                "<li><strong>أمراض الكبد:</strong> الكبد الدهني والتهاب الكبد والتليف "
                "وأورام الكبد يمكن أن ترفع GGT.</li>"
                "<li><strong>انسداد القنوات الصفراوية:</strong> حصوات المرارة أو تضيق "
                "القنوات يسبب ارتفاعاً ملحوظاً.</li>"
                "<li><strong>الأدوية:</strong> بعض مضادات الصرع والباربيتورات ومضادات "
                "الالتهاب غير الستيرويدية والستاتينات قد ترفع GGT.</li>"
                "<li><strong>التهاب البنكرياس:</strong> التهاب البنكرياس يمكن أن يرفعه.</li>"
                "<li><strong>قصور القلب:</strong> احتقان الكبد الناتج عن قصور القلب "
                "الاحتقاني قد يرفع القيمة.</li>"
                "<li><strong>السكري ومتلازمة الأيض:</strong> مقاومة الإنسولين والكبد "
                "الدهني المرتبط بها يساهمان في الارتفاع.</li>"
                "</ul>"
                "<p>في حالات نادرة، قد يشير GGT المرتفع إلى التهاب كبد مناعي ذاتي أو "
                "داء ترسب الأصبغة الدموية أو داء ويلسون. تحتاج فحوصات إضافية لتحديد السبب.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض مرتبطة بارتفاع GGT",
            body_html=(
                "<p>ارتفاع GGT وحده نادراً ما يسبب أعراضاً ملحوظة؛ عادةً تسيطر أعراض "
                "الحالة الأساسية. علامات شائعة قد ترافق مشاكل الكبد أو القنوات الصفراوية:</p>"
                "<ul>"
                "<li>ألم أو انزعاج في الجزء العلوي الأيمن من البطن</li>"
                "<li>إرهاق وضعف عام</li>"
                "<li>غثيان أو فقدان الشهية</li>"
                "<li>اصفرار الجلد أو بياض العينين (يرقان)</li>"
                "<li>بول داكن أو براز فاتح اللون</li>"
                "<li>حكة</li>"
                "</ul>"
                "<p>إذا ظهرت هذه الأعراض مع GGT مرتفع، راجع طبيبك. حتى بدون أعراض، "
                "فإن GGT المرتفع باستمرار — خاصةً في فحوصات متكررة — يستحق التقصي.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="فحوصات تُقيّم مع GGT",
            body_html=(
                "<p>نتيجة GGT وحدها لا تكفي للتشخيص؛ يجب تفسيرها مع:</p>"
                "<ul>"
                "<li><strong><a href=\"/ar/blog/ma-dha-taani-mustawayat-alt-wa-ast-alalia\">ALT "
                "وAST</a>:</strong> مؤشرات مباشرة على تلف خلايا الكبد. ارتفاعها مع GGT يزيد "
                "احتمالية مرض كبدي.</li>"
                "<li><strong>ALP (الفوسفاتاز القلوي):</strong> ارتفاع GGT وALP معاً يشير "
                "لسبب كبدي أو صفراوي؛ ارتفاع ALP وحده قد يدل على مشكلة عظمية.</li>"
                "<li><strong>البيليروبين:</strong> ارتفاعه مرتبط باليرقان ويدعم سبباً "
                "كبدياً صفراوياً.</li>"
                "<li><strong>الألبومين والبروتين الكلي:</strong> يُستخدمان لتقييم قدرة "
                "الكبد التصنيعية.</li>"
                "</ul>"
                "<p>حسب الصورة السريرية، قد يطلب الطبيب أيضاً تصوير الكبد بالموجات فوق "
                "الصوتية أو مصليات التهاب الكبد الفيروسي أو مؤشرات المناعة الذاتية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>ناقش نتائجك مع طبيب إذا:</p>"
                "<ul>"
                "<li>GGT أعلى بكثير من النطاق المرجعي</li>"
                "<li>إنزيمات كبد أخرى (ALT، AST، ALP) مرتفعة أيضاً</li>"
                "<li>لديك يرقان أو ألم بطني أو إرهاق غير مبرر</li>"
                "<li>تتناول الكحول بانتظام أو غيّرت أدويتك مؤخراً</li>"
                "<li>GGT يظل مرتفعاً في فحوصات متتالية</li>"
                "</ul>"
                "<p>نظراً لأن ارتفاع GGT قد يعكس حالات متنوعة جداً، فمن الضروري أن يُقيّم "
                "النتيجة طبيب يعرف تاريخك الطبي ونتائج فحوصاتك الأخرى. التقييم المبكر "
                "يساعد في كشف أمراض الكبد في مرحلة قابلة للعلاج.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يساعدك Norya في فهم نتيجة GGT",
            body_html=(
                "<p>في Norya لا نشخّص — بل نساعدك على الاستعداد. "
                "<a href=\"/analyze\">ارفع تقرير المختبر الخاص بك</a> واحصل على ملخص واضح "
                "ومنظم يشرح قيمك — بما فيها GGT — بلغة بسيطة مع النطاقات المرجعية "
                "والسياق.</p>"
                "<p>هذا يسهّل مناقشة نتائجك مع طبيبك وطرح الأسئلة الصحيحة. يعرض Norya "
                "GGT إلى جانب ALT وAST ومؤشرات أخرى لتتمكن من رؤية الصورة الكاملة. "
                "للاطلاع على الخيارات والأسعار، زوروا "
                "<a href=\"/pricing\">صفحة الأسعار</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء مسؤولية",
            body_html=(
                "<p><strong>هذا المحتوى لأغراض إعلامية فقط ولا يحل محل الاستشارة أو التشخيص "
                "الطبي.</strong> ارتفاع GGT قد يكون له أسباب عديدة؛ فقط أخصائي رعاية صحية "
                "يعرف تاريخك يمكنه تفسير نتيجتك بشكل صحيح. ناقش دائماً نتائج المختبر مع "
                "طبيبك.</p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_ggt_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_ggt_faq_schema_qa() -> dict:
    return {
        "tr": [
            {"question": "GGT nedir?",
             "answer": "GGT (Gamma-Glutamil Transferaz), başta karaciğer olmak üzere böbrekler, pankreas ve safra kanallarında bulunan bir enzimdir. Glutatyon metabolizmasında görev alır ve karaciğer hasarı veya safra yolu tıkanıklığı olduğunda kanda yükselir."},
            {"question": "GGT normal değeri kaç olmalıdır?",
             "answer": "Erkeklerde 8–61 U/L, kadınlarda 5–36 U/L genel kabul gören normal aralıklardır. Laboratuvara göre küçük farklar olabilir; sonuçlarınızı raporunuzdaki referans aralıklarıyla karşılaştırın."},
            {"question": "GGT yüksekliğinin en sık nedeni nedir?",
             "answer": "Düzenli veya aşırı alkol tüketimi GGT yüksekliğinin en yaygın nedenidir. Bunun dışında karaciğer hastalıkları, safra yolu tıkanıklığı, bazı ilaçlar, pankreatit, kalp yetmezliği ve diyabet de GGT'yi yükseltebilir."},
            {"question": "GGT yüksek çıktığında ne yapmalıyım?",
             "answer": "GGT referans aralığının üzerinde çıktıysa, özellikle ALT, AST veya ALP gibi diğer karaciğer enzimleri de yüksekse, hekiminize danışmanız önerilir. Hekim sonucu öykünüz ve diğer test sonuçlarınız ile birlikte değerlendirecektir."},
        ],
        "en": [
            {"question": "What is GGT?",
             "answer": "GGT (Gamma-Glutamyl Transferase) is an enzyme found mainly in the liver, kidneys, pancreas, and bile ducts. It plays a role in glutathione metabolism and rises in the blood when the liver is damaged or bile flow is obstructed."},
            {"question": "What is a normal GGT level?",
             "answer": "Generally accepted normal ranges are 8–61 U/L for men and 5–36 U/L for women. Ranges may vary slightly between laboratories; always compare your results with the reference values on your report."},
            {"question": "What is the most common cause of high GGT?",
             "answer": "Regular or heavy alcohol consumption is the most common cause of elevated GGT. Other causes include liver diseases, bile duct obstruction, certain medications, pancreatitis, heart failure, and diabetes."},
            {"question": "What should I do if my GGT is high?",
             "answer": "If your GGT is above the reference range — especially if other liver enzymes like ALT, AST, or ALP are also elevated — consult your doctor. They will evaluate the result in context with your medical history and other tests."},
        ],
        "es": [
            {"question": "¿Qué es la GGT?",
             "answer": "La GGT (Gamma-Glutamil Transferasa) es una enzima presente sobre todo en el hígado, los riñones, el páncreas y los conductos biliares. Participa en el metabolismo del glutatión y se eleva en sangre cuando el hígado está dañado o el flujo biliar está obstruido."},
            {"question": "¿Cuál es el valor normal de GGT?",
             "answer": "Los rangos normales aceptados son 8–61 U/L en hombres y 5–36 U/L en mujeres. Los rangos pueden variar ligeramente entre laboratorios; compare sus resultados con los valores de referencia de su informe."},
            {"question": "¿Cuál es la causa más frecuente de GGT alta?",
             "answer": "El consumo regular o excesivo de alcohol es la causa más común. Otras causas incluyen enfermedades hepáticas, obstrucción biliar, ciertos medicamentos, pancreatitis, insuficiencia cardíaca y diabetes."},
            {"question": "¿Qué debo hacer si mi GGT está alta?",
             "answer": "Si su GGT supera el rango de referencia, especialmente si otras enzimas hepáticas como ALT, AST o ALP también están elevadas, consulte a su médico. Evaluará el resultado en el contexto de su historial y otras pruebas."},
        ],
        "de": [
            {"question": "Was ist GGT?",
             "answer": "GGT (Gamma-Glutamyl-Transferase) ist ein Enzym, das hauptsächlich in der Leber, aber auch in Nieren, Bauchspeicheldrüse und Gallenwegen vorkommt. Es ist am Glutathion-Stoffwechsel beteiligt und steigt im Blut bei Leberschäden oder Gallenabflussstörungen an."},
            {"question": "Welcher GGT-Wert ist normal?",
             "answer": "Allgemein gelten für Männer 8–61 U/L und für Frauen 5–36 U/L als normal. Referenzbereiche können zwischen Laboren leicht variieren; vergleichen Sie Ihre Ergebnisse mit den Angaben auf Ihrem Befund."},
            {"question": "Was ist die häufigste Ursache für erhöhte GGT?",
             "answer": "Regelmäßiger oder übermäßiger Alkoholkonsum ist die häufigste Ursache. Weitere Ursachen sind Lebererkrankungen, Gallenwegserkrankungen, bestimmte Medikamente, Pankreatitis, Herzinsuffizienz und Diabetes."},
            {"question": "Was soll ich tun, wenn mein GGT erhöht ist?",
             "answer": "Wenn Ihr GGT-Wert über dem Referenzbereich liegt — insbesondere wenn auch andere Leberenzyme wie ALT, AST oder ALP erhöht sind — sollten Sie Ihren Arzt konsultieren. Er wird den Befund im Zusammenhang mit Ihrer Vorgeschichte und weiteren Tests bewerten."},
        ],
        "fr": [
            {"question": "Qu'est-ce que la GGT ?",
             "answer": "La GGT (Gamma-Glutamyl Transférase) est une enzyme présente principalement dans le foie, mais aussi dans les reins, le pancréas et les voies biliaires. Elle intervient dans le métabolisme du glutathion et augmente dans le sang en cas de lésion hépatique ou d'obstruction biliaire."},
            {"question": "Quel est le taux normal de GGT ?",
             "answer": "Les valeurs normales sont généralement de 8 à 61 U/L pour les hommes et de 5 à 36 U/L pour les femmes. Les valeurs de référence peuvent varier entre laboratoires ; comparez toujours vos résultats avec ceux de votre compte rendu."},
            {"question": "Quelle est la cause la plus fréquente de GGT élevée ?",
             "answer": "La consommation régulière ou excessive d'alcool est la cause la plus courante. D'autres causes incluent les maladies du foie, les obstructions biliaires, certains médicaments, la pancréatite, l'insuffisance cardiaque et le diabète."},
            {"question": "Que faire si ma GGT est élevée ?",
             "answer": "Si votre GGT dépasse les valeurs de référence — surtout si d'autres enzymes hépatiques comme l'ALT, l'AST ou l'ALP sont aussi élevées — consultez votre médecin. Il interprétera le résultat en tenant compte de votre historique et de vos autres examens."},
        ],
        "it": [
            {"question": "Cos'è la GGT?",
             "answer": "La GGT (Gamma-Glutamil Transferasi) è un enzima presente soprattutto nel fegato, ma anche nei reni, nel pancreas e nei dotti biliari. Interviene nel metabolismo del glutatione e aumenta nel sangue in caso di danno epatico o ostruzione biliare."},
            {"question": "Qual è il valore normale della GGT?",
             "answer": "I valori normali sono generalmente 8–61 U/L per gli uomini e 5–36 U/L per le donne. I range possono variare leggermente tra laboratori; confrontate i vostri risultati con i valori di riferimento del referto."},
            {"question": "Qual è la causa più comune di GGT alta?",
             "answer": "Il consumo regolare o eccessivo di alcol è la causa più frequente. Altre cause includono malattie epatiche, ostruzione biliare, alcuni farmaci, pancreatite, insufficienza cardiaca e diabete."},
            {"question": "Cosa devo fare se la GGT è alta?",
             "answer": "Se la GGT supera l'intervallo di riferimento, soprattutto se anche ALT, AST o ALP sono elevate, consultate il medico. Valuterà il risultato nel contesto della vostra storia clinica e degli altri esami."},
        ],
        "he": [
            {"question": "מהו GGT?",
             "answer": "GGT (גמא-גלוטמיל טרנספראז) הוא אנזים הנמצא בעיקר בכבד, אך גם בכליות, בלבלב ובדרכי המרה. הוא ממלא תפקיד במטבוליזם של גלוטתיון ועולה בדם כאשר הכבד ניזוק או כשזרימת המרה חסומה."},
            {"question": "מהו ערך GGT תקין?",
             "answer": "הטווחים המקובלים הם 8–61 U/L לגברים ו-5–36 U/L לנשים. הטווחים עשויים להשתנות מעט בין מעבדות; השוו תמיד את תוצאותיכם לערכי הייחוס בדוח."},
            {"question": "מהי הסיבה השכיחה ביותר ל-GGT גבוה?",
             "answer": "צריכת אלכוהול קבועה או מופרזת היא הסיבה השכיחה ביותר. סיבות נוספות כוללות מחלות כבד, חסימת דרכי מרה, תרופות מסוימות, דלקת לבלב, אי-ספיקת לב וסוכרת."},
            {"question": "מה עליי לעשות אם ה-GGT שלי גבוה?",
             "answer": "אם ה-GGT שלכם מעל טווח הייחוס — במיוחד אם גם אנזימי כבד אחרים כמו ALT, AST או ALP מוגברים — פנו לרופא. הוא יעריך את התוצאה בהקשר ההיסטוריה הרפואית שלכם ובדיקות אחרות."},
        ],
        "hi": [
            {"question": "GGT क्या है?",
             "answer": "GGT (गामा-ग्लूटामिल ट्रांसफ़रेज़) एक एंज़ाइम है जो मुख्य रूप से लिवर में पाया जाता है, लेकिन किडनी, पैंक्रियास और पित्त नलिकाओं में भी होता है। यह ग्लूटाथिओन मेटाबॉलिज़्म में भूमिका निभाता है और लिवर क्षति या पित्त प्रवाह बाधित होने पर रक्त में बढ़ जाता है।"},
            {"question": "GGT का सामान्य मान कितना होता है?",
             "answer": "सामान्य रेंज पुरुषों में 8–61 U/L और महिलाओं में 5–36 U/L मानी जाती है। लैब के अनुसार मामूली अंतर हो सकता है; अपने परिणामों की तुलना हमेशा अपनी रिपोर्ट की रेफ़रेंस वैल्यू से करें।"},
            {"question": "GGT बढ़ने का सबसे आम कारण क्या है?",
             "answer": "नियमित या अत्यधिक शराब सेवन सबसे आम कारण है। अन्य कारणों में लिवर रोग, पित्त नली में रुकावट, कुछ दवाइयाँ, पैंक्रियाटाइटिस, हार्ट फ़ेल्योर और डायबिटीज़ शामिल हैं।"},
            {"question": "GGT बढ़ा हो तो क्या करना चाहिए?",
             "answer": "अगर GGT रेफ़रेंस रेंज से ऊपर है — ख़ासकर अगर ALT, AST या ALP जैसे अन्य लिवर एंज़ाइम भी बढ़े हैं — तो डॉक्टर से मिलें। वे आपकी मेडिकल हिस्ट्री और अन्य रिपोर्ट के साथ मिलाकर परिणाम का मूल्यांकन करेंगे।"},
        ],
        "ar": [
            {"question": "ما هو GGT؟",
             "answer": "GGT (غاما غلوتاميل ترانسفيراز) هو إنزيم يتواجد بشكل رئيسي في الكبد، وكذلك في الكلى والبنكرياس والقنوات الصفراوية. يلعب دوراً في أيض الغلوتاثيون ويرتفع في الدم عند تضرر الكبد أو انسداد تدفق الصفراء."},
            {"question": "ما هي القيمة الطبيعية لـ GGT؟",
             "answer": "النطاقات الطبيعية المقبولة هي 8–61 وحدة/لتر للرجال و5–36 وحدة/لتر للنساء. قد تختلف النطاقات قليلاً بين المختبرات؛ قارن دائماً نتائجك بالقيم المرجعية في تقريرك."},
            {"question": "ما السبب الأكثر شيوعاً لارتفاع GGT؟",
             "answer": "تناول الكحول بانتظام أو بإفراط هو السبب الأشيع. أسباب أخرى تشمل أمراض الكبد وانسداد القنوات الصفراوية وبعض الأدوية والتهاب البنكرياس وقصور القلب والسكري."},
            {"question": "ماذا أفعل إذا كان GGT مرتفعاً؟",
             "answer": "إذا كان GGT أعلى من النطاق المرجعي — خاصةً إذا كانت إنزيمات كبد أخرى مثل ALT وAST وALP مرتفعة أيضاً — استشر طبيبك. سيقيّم النتيجة في سياق تاريخك الطبي وفحوصاتك الأخرى."},
        ],
    }
