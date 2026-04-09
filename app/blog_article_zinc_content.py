# -*- coding: utf-8 -*-
"""
Zinc blog article — full body content for all 9 languages.
Used by blog_i18n._article_zinc().
Sections: intro, what-is, normal-ranges, causes, symptoms,
related-tests, when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="Zinc blood test: what your result means",
            body_html=(
                "<p>Zinc is an essential trace mineral that participates in more than 300 enzymatic reactions in the body. "
                "It is vital for immune function, wound healing, protein synthesis, DNA formation, and normal growth and development. "
                "Despite its importance, zinc deficiency is surprisingly common&mdash;the World Health Organization estimates that "
                "roughly one-third of the global population is at risk.</p>"
                "<p>When your blood test reports a zinc level, it measures the concentration of zinc in your serum or plasma. "
                "A low value can affect immunity, skin health, taste perception, and more. This guide explains what the number means "
                "and when to take action.</p>"
                "<p>This article is educational and does not replace medical advice. Always discuss your lab results with a qualified "
                "healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is zinc and why does it matter?",
            body_html=(
                "<p><strong>Zinc (Zn)</strong> is the second most abundant trace element in the body after iron. "
                "It is found in every cell and is essential for the function of over 300 enzymes that drive metabolism, digestion, "
                "nerve function, and many other processes. Unlike iron, the body has no specialized zinc storage system, "
                "so a continuous dietary supply is necessary.</p>"
                "<p>Key roles of zinc include:</p>"
                "<ul>"
                "<li><strong>Immune defence</strong> &ndash; zinc is required for the development and function of neutrophils, "
                "natural killer cells, and T lymphocytes. Deficiency impairs both innate and adaptive immunity.</li>"
                "<li><strong>Wound healing</strong> &ndash; zinc supports collagen synthesis and cell proliferation in damaged tissue.</li>"
                "<li><strong>Taste and smell</strong> &ndash; the enzyme gustin, which is zinc-dependent, is essential for normal taste perception.</li>"
                "<li><strong>Growth and development</strong> &ndash; adequate zinc is critical for childhood growth, puberty, and pregnancy.</li>"
                "<li><strong>Skin and hair health</strong> &ndash; zinc deficiency is a recognized cause of dermatitis, hair loss, and nail abnormalities.</li>"
                "</ul>"
                "<p>The body contains approximately 2&ndash;3&nbsp;grams of zinc, distributed across muscle (60%), bone (30%), "
                "skin and liver (5%), and the remaining 5% in other tissues. Only about 0.1% of total body zinc is in the blood, "
                "which is why serum zinc is an imperfect&mdash;but clinically useful&mdash;marker of zinc status.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal zinc ranges",
            body_html=(
                "<p>Zinc is most commonly measured in serum or plasma. Reference ranges differ slightly between laboratories:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Marker</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serum zinc (adults)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">60&ndash;120 &micro;g/dL (9.2&ndash;18.4 &micro;mol/L)</td></tr>'
                "</tbody></table>"
                "<p>Zinc levels are affected by time of day (lower in the afternoon), recent meals, inflammation, "
                "and certain medications. A morning fasting sample provides the most reliable result. "
                "During acute illness or inflammation, serum zinc can drop temporarily even when stores are adequate, "
                "because zinc redistributes to the liver as part of the acute-phase response.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of low and high zinc",
            body_html=(
                "<p><strong>Low zinc (deficiency)</strong> is caused by:</p>"
                "<ul>"
                "<li><strong>Inadequate dietary intake</strong> &ndash; diets low in meat, shellfish, legumes, and seeds. "
                "Vegetarian and vegan diets carry higher risk because phytates in grains and legumes inhibit zinc absorption.</li>"
                "<li><strong>Malabsorption</strong> &ndash; celiac disease, Crohn&rsquo;s disease, short bowel syndrome, "
                "and chronic diarrhea reduce zinc absorption in the gut.</li>"
                "<li><strong>Chronic liver disease</strong> &ndash; impaired zinc metabolism and increased urinary zinc loss.</li>"
                "<li><strong>Chronic kidney disease</strong> &ndash; urinary losses and reduced intestinal absorption.</li>"
                "<li><strong>Pregnancy and lactation</strong> &ndash; increased demand for fetal/infant growth.</li>"
                "<li><strong>Alcoholism</strong> &ndash; ethanol reduces zinc absorption and increases urinary excretion.</li>"
                "<li><strong>Medications</strong> &ndash; diuretics, ACE inhibitors, and long-term proton pump inhibitors can lower zinc.</li>"
                "</ul>"
                "<p><strong>High zinc (excess)</strong> is uncommon and usually results from excessive supplementation. "
                "Chronic zinc excess (&gt;150&nbsp;mg/day) can cause <strong>copper deficiency</strong>, because zinc and copper "
                "compete for absorption. Symptoms of zinc excess include nausea, vomiting, and diarrhea.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of zinc deficiency",
            body_html=(
                "<p>Zinc deficiency manifests across multiple organ systems because of zinc&rsquo;s wide-ranging roles:</p>"
                "<ul>"
                "<li><strong>Impaired immunity</strong> &ndash; frequent infections, prolonged colds, and poor vaccine response.</li>"
                "<li><strong>Hair loss (alopecia)</strong> &ndash; thinning hair or diffuse hair loss, sometimes with dull, brittle strands.</li>"
                "<li><strong>Poor wound healing</strong> &ndash; cuts and scrapes take longer to heal.</li>"
                "<li><strong>Changes in taste and smell</strong> &ndash; decreased ability to taste food (hypogeusia) or altered taste (dysgeusia).</li>"
                "<li><strong>Skin rashes</strong> &ndash; acrodermatitis enteropathica (a classic zinc-deficiency dermatitis) presents as scaly, "
                "red lesions around the mouth, hands, and feet.</li>"
                "<li><strong>Growth retardation</strong> &ndash; in children, zinc deficiency can stunt linear growth and delay puberty.</li>"
                "<li><strong>Night blindness</strong> &ndash; zinc is needed for retinol (vitamin A) metabolism.</li>"
                "<li><strong>Mood disturbances</strong> &ndash; irritability, depression, and impaired cognitive function have been linked to low zinc.</li>"
                "</ul>"
                "<p>Severe zinc deficiency is rare in developed countries but mild-to-moderate deficiency is common, "
                "especially in the elderly, pregnant women, vegetarians, and individuals with chronic GI diseases.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>Zinc is often interpreted alongside other markers:</p>"
                "<ul>"
                "<li><strong>Copper</strong> &ndash; zinc and copper compete for absorption; high zinc supplements can cause copper deficiency "
                "and vice versa. Both should be checked if either is abnormal.</li>"
                "<li><strong>Albumin</strong> &ndash; zinc circulates bound to albumin; low albumin (e.g.&nbsp;in liver disease or malnutrition) "
                "can reduce serum zinc even when true stores are adequate.</li>"
                "<li><strong>Complete Blood Count (CBC)</strong> &ndash; zinc deficiency can cause lymphopenia and impaired neutrophil function.</li>"
                "<li><strong>Iron studies (ferritin, serum iron, TIBC)</strong> &ndash; zinc and iron deficiency often coexist in malnutrition "
                "or malabsorption. See our <a href=\"/en/blog/iron-deficiency-ferritin-meaning\">iron &amp; ferritin guide</a>.</li>"
                "<li><strong>Alkaline phosphatase (ALP)</strong> &ndash; ALP is a zinc-dependent enzyme; low ALP may indicate zinc deficiency.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>You should discuss your zinc result with a healthcare provider if:</p>"
                "<ul>"
                "<li>Your serum zinc is below 60&nbsp;&micro;g/dL.</li>"
                "<li>You have symptoms consistent with zinc deficiency: frequent infections, hair loss, poor wound healing, "
                "or changes in taste/smell.</li>"
                "<li>You follow a vegetarian or vegan diet and have not been monitoring zinc intake.</li>"
                "<li>You have a chronic condition that impairs absorption (celiac, Crohn&rsquo;s, liver disease, kidney disease).</li>"
                "<li>You are pregnant or breastfeeding.</li>"
                "<li>You take high-dose zinc supplements&mdash;your doctor should monitor for copper deficiency.</li>"
                "</ul>"
                "<p>Your doctor can confirm deficiency, identify the underlying cause, recommend appropriate supplementation "
                "(typically 15&ndash;30&nbsp;mg/day of elemental zinc for mild deficiency), and monitor your response.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How NoryaAI helps you understand your zinc results",
            body_html=(
                "<p>NoryaAI makes it easy to understand your zinc and other blood test results. Simply "
                "<a href=\"/analyze\">upload your lab report</a>&mdash;whether it is a PDF, photo, or scan&mdash;and our AI engine will:</p>"
                "<ul>"
                "<li>Extract your zinc value along with all other biomarkers on the report.</li>"
                "<li>Compare each result against age- and sex-specific reference ranges.</li>"
                "<li>Flag abnormal values with clear, plain-language explanations.</li>"
                "<li>Highlight connections between related markers (e.g.&nbsp;zinc + copper + albumin + iron studies).</li>"
                "<li>Generate a structured, doctor-ready summary you can share at your next appointment.</li>"
                "</ul>"
                "<p>Explore our <a href=\"/pricing\">pricing plans</a> to see which option fits your needs. "
                "NoryaAI is designed to help you prepare for&mdash;not replace&mdash;a conversation with your doctor.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Medical disclaimer",
            body_html=(
                "<p><strong>This article is for informational and educational purposes only. It does not constitute medical advice, "
                "diagnosis, or treatment. Always consult a qualified healthcare professional before making any decisions based on "
                "your lab results. NoryaAI provides automated analysis to help you understand your reports, but it is not a substitute "
                "for professional medical judgment.</strong></p>"
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
            heading="Çinko kan testi: sonucunuz ne anlama geliyor?",
            body_html=(
                "<p>Çinko, vücutta 300&rsquo;den fazla enzimatik reaksiyona katılan esansiyel bir eser elementtir. "
                "Bağışıklık fonksiyonu, yara iyileşmesi, protein sentezi, DNA oluşumu ve normal büyüme-gelişim için hayati önem taşır. "
                "Önemine rağmen çinko eksikliği şaşırtıcı derecede yaygındır.</p>"
                "<p>Kan testinizdeki çinko değeri, serumunuzdaki çinko konsantrasyonunu ölçer. Düşük bir değer bağışıklığı, "
                "cilt sağlığını, tat algısını ve daha birçok fonksiyonu etkileyebilir. Bu rehber sonucunuzu anlamanıza yardımcı olur.</p>"
                "<p>Bu makale eğitim amaçlıdır ve tıbbi tavsiye yerine geçmez. Sonuçlarınızı bir hekimle değerlendirin.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Çinko nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Çinko (Zn)</strong>, demirden sonra vücuttaki en bol ikinci eser elementtir. Her hücrede bulunur "
                "ve metabolizmayı, sindirim, sinir fonksiyonu ve birçok süreci yönlendiren 300&rsquo;den fazla enzimin işlevi için "
                "gereklidir. Demirden farklı olarak vücutta özel bir çinko depolama sistemi yoktur; bu nedenle sürekli diyet yoluyla "
                "alım gereklidir.</p>"
                "<p>Çinkonun temel rolleri şunlardır:</p>"
                "<ul>"
                "<li><strong>Bağışıklık savunması</strong> &ndash; nötrofiller, doğal öldürücü hücreler ve T lenfositlerin gelişimi için gereklidir.</li>"
                "<li><strong>Yara iyileşmesi</strong> &ndash; kolajen sentezini ve hasarlı dokuda hücre çoğalmasını destekler.</li>"
                "<li><strong>Tat ve koku</strong> &ndash; çinkoya bağımlı gustin enzimi normal tat algısı için gereklidir.</li>"
                "<li><strong>Büyüme ve gelişme</strong> &ndash; çocukluk büyümesi, ergenlik ve gebelik için kritiktir.</li>"
                "<li><strong>Cilt ve saç sağlığı</strong> &ndash; eksiklik dermatit, saç dökülmesi ve tırnak bozukluklarına neden olabilir.</li>"
                "</ul>"
                "<p>Vücuttaki toplam çinko yaklaşık 2&ndash;3&nbsp;gramdır; %60&rsquo;ı kasta, %30&rsquo;u kemiklerde bulunur. "
                "Kandaki oran yalnızca %0,1 civarındadır; bu nedenle serum çinkosu tam olmasa da klinik açıdan faydalı bir göstergedir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal çinko aralıkları",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Belirteç</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Serum çinko (yetişkin)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">60&ndash;120 &micro;g/dL (9,2&ndash;18,4 &micro;mol/L)</td></tr>'
                "</tbody></table>"
                "<p>Çinko düzeyleri günün saatine (öğleden sonra düşer), yakın zamandaki öğünlere, inflamasyona ve bazı ilaçlara "
                "göre değişir. Sabah açlık örneği en güvenilir sonucu verir. Akut hastalık sırasında çinko, akut faz yanıtının "
                "parçası olarak karaciğere yeniden dağıtıldığından geçici olarak düşebilir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Düşük ve yüksek çinko nedenleri",
            body_html=(
                "<p><strong>Düşük çinko (eksiklik)</strong> nedenleri:</p>"
                "<ul>"
                "<li><strong>Yetersiz diyet alımı</strong> &ndash; et, kabuklu deniz ürünleri, baklagiller ve tohumlar açısından fakir diyetler. "
                "Vejetaryen ve vegan diyetler daha yüksek risk taşır çünkü tahıl ve baklagillerdeki fitatlar çinko emilimini engeller.</li>"
                "<li><strong>Emilim bozukluğu</strong> &ndash; çölyak, Crohn, kısa bağırsak sendromu ve kronik ishal.</li>"
                "<li><strong>Kronik karaciğer hastalığı</strong> &ndash; bozulmuş çinko metabolizması ve artmış idrar kaybı.</li>"
                "<li><strong>Kronik böbrek hastalığı</strong> &ndash; idrar kayıpları ve azalmış bağırsak emilimi.</li>"
                "<li><strong>Gebelik ve emzirme</strong> &ndash; fetal/bebek büyümesi için artan talep.</li>"
                "<li><strong>Alkolizm</strong> &ndash; etanol çinko emilimini azaltır ve idrarla atılımı artırır.</li>"
                "<li><strong>İlaçlar</strong> &ndash; diüretikler, ACE inhibitörleri ve uzun süreli PPI kullanımı çinkoyu düşürebilir.</li>"
                "</ul>"
                "<p><strong>Yüksek çinko (fazlalık)</strong> nadirdir ve genellikle aşırı takviye kullanımından kaynaklanır. "
                "Kronik çinko fazlalığı (&gt;150&nbsp;mg/gün) <strong>bakır eksikliğine</strong> yol açabilir çünkü çinko ve bakır "
                "emilim için yarışır.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Çinko eksikliği belirtileri",
            body_html=(
                "<p>Çinko eksikliği, çinkonun geniş kapsamlı rolleri nedeniyle birçok organ sisteminde kendini gösterir:</p>"
                "<ul>"
                "<li><strong>Bağışıklık bozukluğu</strong> &ndash; sık enfeksiyonlar, uzun süren soğuk algınlıkları.</li>"
                "<li><strong>Saç dökülmesi (alopesi)</strong> &ndash; incelen veya yaygın saç dökülmesi.</li>"
                "<li><strong>Zayıf yara iyileşmesi</strong> &ndash; kesikler ve sıyrıklar daha uzun sürede iyileşir.</li>"
                "<li><strong>Tat ve koku değişiklikleri</strong> &ndash; azalmış tat algısı (hipogeüzi) veya değişmiş tat.</li>"
                "<li><strong>Cilt döküntüleri</strong> &ndash; ağız, el ve ayak çevresinde pullu, kırmızı lezyonlar (akrodermatitis enteropatika).</li>"
                "<li><strong>Büyüme geriliği</strong> &ndash; çocuklarda boy uzaması yavaşlayabilir ve ergenlik gecikebilir.</li>"
                "<li><strong>Gece körlüğü</strong> &ndash; çinko, retinol (A vitamini) metabolizması için gereklidir.</li>"
                "<li><strong>Ruhsal bozukluklar</strong> &ndash; huzursuzluk, depresyon ve bilişsel işlev bozukluğu.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlişkili testler",
            body_html=(
                "<ul>"
                "<li><strong>Bakır</strong> &ndash; çinko ve bakır emilim için yarışır; biri anormal ise diğeri de kontrol edilmelidir.</li>"
                "<li><strong>Albümin</strong> &ndash; çinko albümine bağlı dolaşır; düşük albümin serum çinkoyu düşürebilir.</li>"
                "<li><strong>Tam Kan Sayımı (CBC)</strong> &ndash; eksiklik lenfopeni ve nötrofil işlev bozukluğuna neden olabilir.</li>"
                "<li><strong>Demir testleri (ferritin, serum demir, TIBC)</strong> &ndash; çinko ve demir eksikliği sıklıkla birlikte görülür. "
                "<a href=\"/tr/blog/demir-eksikligi-ferritin-anlami\">Demir ve ferritin rehberimize</a> bakın.</li>"
                "<li><strong>Alkalen fosfataz (ALP)</strong> &ndash; çinkoya bağımlı bir enzimdir; düşük ALP çinko eksikliğine işaret edebilir.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda çinko sonucunuzu bir hekimle görüşmelisiniz:</p>"
                "<ul>"
                "<li>Serum çinkonuz 60&nbsp;&micro;g/dL&rsquo;nin altında.</li>"
                "<li>Eksiklik belirtileriniz var: sık enfeksiyon, saç dökülmesi, yavaş yara iyileşmesi, tat/koku değişiklikleri.</li>"
                "<li>Vejetaryen veya vegan besleniyorsunuz ve çinko alımınızı izlemiyorsunuz.</li>"
                "<li>Emilimi bozan kronik bir hastalığınız var (çölyak, Crohn, karaciğer, böbrek).</li>"
                "<li>Hamilesiniz veya emziriyorsunuz.</li>"
                "<li>Yüksek doz çinko takviyesi alıyorsunuz&mdash;bakır eksikliği açısından izlem gerekir.</li>"
                "</ul>"
                "<p>Doktorunuz eksikliği doğrulayabilir, nedenini belirleyebilir ve uygun takviye (hafif eksiklikte genellikle "
                "günlük 15&ndash;30&nbsp;mg elemental çinko) önerebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI çinko sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>NoryaAI, çinko ve diğer kan testi sonuçlarınızı kolayca anlamanızı sağlar. "
                "<a href=\"/analyze\">Laboratuvar raporunuzu yükleyin</a>&mdash;PDF, fotoğraf veya tarama&mdash;analiz motorumuz:</p>"
                "<ul>"
                "<li>Rapordaki çinko değerini ve diğer tüm biyobelirteçleri çıkarır.</li>"
                "<li>Her sonucu yaş ve cinsiyete özel referans aralıklarıyla karşılaştırır.</li>"
                "<li>Anormal değerleri sade açıklamalarla işaretler.</li>"
                "<li>İlişkili belirteçler arasındaki bağlantıları vurgular (çinko + bakır + albümin + demir).</li>"
                "<li>Doktorunuza götürebileceğiniz yapılandırılmış bir özet oluşturur.</li>"
                "</ul>"
                "<p><a href=\"/pricing\">Fiyatlandırma planlarımızı</a> inceleyin.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Tıbbi sorumluluk reddi",
            body_html=(
                "<p><strong>Bu makale yalnızca bilgilendirme ve eğitim amaçlıdır. Tıbbi tavsiye, teşhis veya tedavi niteliği taşımaz. "
                "Laboratuvar sonuçlarınıza dayalı herhangi bir karar vermeden önce mutlaka nitelikli bir sağlık uzmanına danışın. "
                "NoryaAI, raporlarınızı anlamanıza yardımcı olmak için otomatik analiz sunar ancak profesyonel tıbbi değerlendirmenin "
                "yerini tutmaz.</strong></p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# SPANISH
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Análisis de zinc en sangre: qué significa tu resultado",
                body_html="<p>El zinc es un oligoelemento esencial que participa en más de 300 reacciones enzimáticas. Es vital para la función inmunológica, la cicatrización, la síntesis de proteínas y el crecimiento normal. La deficiencia de zinc es sorprendentemente común a nivel mundial.</p><p>El valor de zinc en tu análisis mide la concentración en suero o plasma. Un valor bajo puede afectar la inmunidad, la piel y la percepción del gusto.</p><p>Este artículo es educativo y no sustituye el consejo médico.</p>"),
        Section(id="what-is", level=2, heading="¿Qué es el zinc y por qué es importante?",
                body_html="<p>El <strong>zinc (Zn)</strong> es el segundo oligoelemento más abundante en el cuerpo después del hierro. Es necesario para más de 300 enzimas que impulsan el metabolismo, la digestión y la función nerviosa. A diferencia del hierro, el cuerpo no tiene un sistema especializado de almacenamiento de zinc.</p><p>Funciones clave: defensa inmunitaria, cicatrización de heridas, percepción del gusto y olfato, crecimiento y desarrollo, y salud de piel y cabello. El cuerpo contiene 2–3 gramos de zinc, distribuidos en músculos (60%), huesos (30%) y otros tejidos.</p>"),
        Section(id="normal-ranges", level=2, heading="Rangos normales de zinc",
                body_html="<p>El zinc sérico normal en adultos es <strong>60–120 µg/dL</strong> (9,2–18,4 µmol/L). Los niveles se ven afectados por la hora del día, las comidas recientes, la inflamación y ciertos medicamentos. Una muestra en ayunas por la mañana proporciona el resultado más fiable.</p>"),
        Section(id="causes", level=2, heading="Causas de zinc bajo y alto",
                body_html="<p><strong>Zinc bajo</strong>: ingesta dietética inadecuada (especialmente en dietas vegetarianas/veganas), malabsorción (celiaquía, Crohn), enfermedad hepática o renal crónica, embarazo, alcoholismo y medicamentos (diuréticos, IBP). <strong>Zinc alto</strong>: raro, generalmente por suplementación excesiva. El exceso crónico (>150 mg/día) puede causar <strong>deficiencia de cobre</strong>.</p>"),
        Section(id="symptoms", level=2, heading="Síntomas de la deficiencia de zinc",
                body_html="<p>Incluyen: inmunidad deteriorada con infecciones frecuentes, caída del cabello, mala cicatrización, cambios en gusto y olfato, erupciones cutáneas (acrodermatitis enteropática), retraso del crecimiento en niños, ceguera nocturna y alteraciones del ánimo. La deficiencia leve-moderada es común en ancianos, embarazadas y vegetarianos.</p>"),
        Section(id="related-tests", level=2, heading="Pruebas relacionadas",
                body_html="<p>El zinc se interpreta junto con: <strong>cobre</strong> (compiten por absorción), <strong>albúmina</strong> (el zinc circula unido a ella), <strong>hemograma</strong>, <strong>estudios de hierro</strong> (<a href=\"/es/blog/deficit-hierro-ferritina\">guía de hierro</a>) y <strong>fosfatasa alcalina</strong> (enzima dependiente de zinc).</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Cuándo consultar al médico",
                body_html="<p>Consulta si tu zinc sérico está por debajo de 60 µg/dL, tienes síntomas de deficiencia, sigues una dieta vegetariana/vegana sin control de zinc, tienes una enfermedad crónica que afecta la absorción, estás embarazada, o tomas suplementos de zinc en dosis altas.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo NoryaAI te ayuda con tu zinc",
                body_html="<p><a href=\"/analyze\">Sube tu informe</a> y nuestra IA extrae tu zinc y todos los biomarcadores, compara con rangos de referencia, señala anomalías y genera un resumen para tu médico. Explora nuestros <a href=\"/pricing\">planes de precios</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso médico",
                body_html="<p><strong>Este artículo es solo informativo y educativo. No constituye consejo médico. Consulta siempre a un profesional de salud cualificado. NoryaAI ofrece análisis automatizado pero no sustituye el criterio médico profesional.</strong></p>"),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Zink-Bluttest: Was Ihr Ergebnis bedeutet",
                body_html="<p>Zink ist ein essentielles Spurenelement, das an über 300 enzymatischen Reaktionen beteiligt ist. Es ist lebenswichtig für die Immunfunktion, Wundheilung, Proteinsynthese und normale Entwicklung. Trotz seiner Bedeutung ist Zinkmangel überraschend häufig.</p><p>Der Zinkwert in Ihrer Blutuntersuchung misst die Zinkkonzentration im Serum. Ein niedriger Wert kann Immunität, Haut und Geschmackswahrnehmung beeinträchtigen.</p><p>Dieser Artikel dient der Aufklärung und ersetzt keine ärztliche Beratung.</p>"),
        Section(id="what-is", level=2, heading="Was ist Zink und warum ist es wichtig?",
                body_html="<p><strong>Zink (Zn)</strong> ist nach Eisen das zweithäufigste Spurenelement im Körper. Es ist für über 300 Enzyme essentiell. Schlüsselfunktionen: Immunabwehr, Wundheilung, Geschmack und Geruch, Wachstum und Entwicklung sowie Haut- und Haargesundheit. Der Körper enthält 2–3 g Zink, verteilt auf Muskeln (60%), Knochen (30%) und andere Gewebe.</p>"),
        Section(id="normal-ranges", level=2, heading="Normale Zinkwerte",
                body_html="<p>Normaler Serumzink bei Erwachsenen: <strong>60–120 µg/dL</strong> (9,2–18,4 µmol/L). Die Werte werden durch Tageszeit, Mahlzeiten, Entzündung und Medikamente beeinflusst. Eine morgendliche Nüchternprobe liefert das zuverlässigste Ergebnis.</p>"),
        Section(id="causes", level=2, heading="Ursachen für niedrige und hohe Zinkwerte",
                body_html="<p><strong>Niedriges Zink</strong>: unzureichende Ernährung (besonders vegetarisch/vegan), Malabsorption (Zöliakie, Morbus Crohn), chronische Leber- oder Nierenerkrankung, Schwangerschaft, Alkoholismus und Medikamente. <strong>Hohes Zink</strong>: selten, meist durch übermäßige Supplementierung. Chronischer Überschuss (>150 mg/Tag) kann <strong>Kupfermangel</strong> verursachen.</p>"),
        Section(id="symptoms", level=2, heading="Symptome eines Zinkmangels",
                body_html="<p>Beeinträchtigte Immunität, Haarausfall, schlechte Wundheilung, Geschmacks- und Geruchsstörungen, Hautausschläge (Acrodermatitis enteropathica), Wachstumsverzögerung bei Kindern, Nachtblindheit und Stimmungsstörungen. Leichter bis mäßiger Mangel ist häufig bei älteren Menschen, Schwangeren und Vegetariern.</p>"),
        Section(id="related-tests", level=2, heading="Verwandte Laborwerte",
                body_html="<p>Zink wird zusammen mit <strong>Kupfer</strong>, <strong>Albumin</strong>, <strong>Blutbild</strong>, <strong>Eisenstudien</strong> (<a href=\"/de/blog/eisenmangel-ferritin-bedeutung\">Eisen-Ratgeber</a>) und <strong>alkalischer Phosphatase</strong> (zinkabhängiges Enzym) interpretiert.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann Sie einen Arzt aufsuchen sollten",
                body_html="<p>Sprechen Sie mit Ihrem Arzt, wenn Ihr Zink unter 60 µg/dL liegt, Sie Mangelsymptome haben, sich vegetarisch/vegan ernähren, eine chronische Erkrankung mit Malabsorption haben, schwanger sind oder hochdosierte Zinksupplemente einnehmen.</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie NoryaAI bei Ihren Zinkwerten hilft",
                body_html="<p><a href=\"/analyze\">Laden Sie Ihren Befund hoch</a> und unsere KI extrahiert Zink und alle Biomarker, vergleicht mit Referenzbereichen, markiert Auffälligkeiten und erstellt eine arztfertige Zusammenfassung. <a href=\"/pricing\">Preispläne</a> entdecken.</p>"),
        Section(id="disclaimer", level=2, heading="Medizinischer Haftungsausschluss",
                body_html="<p><strong>Dieser Artikel dient ausschließlich der Information. Er stellt keine medizinische Beratung dar. Konsultieren Sie immer einen qualifizierten Arzt. NoryaAI bietet automatisierte Analysen, ersetzt aber kein ärztliches Urteil.</strong></p>"),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Analyse du zinc sanguin : que signifie votre résultat ?",
                body_html="<p>Le zinc est un oligo-élément essentiel impliqué dans plus de 300 réactions enzymatiques. Il est vital pour l&rsquo;immunité, la cicatrisation, la synthèse protéique et la croissance. La carence en zinc est étonnamment fréquente dans le monde.</p><p>Le taux de zinc dans votre bilan mesure la concentration sérique. Un taux bas affecte l&rsquo;immunité, la peau et le goût.</p><p>Cet article est éducatif et ne remplace pas un avis médical.</p>"),
        Section(id="what-is", level=2, heading="Qu'est-ce que le zinc et pourquoi est-il important ?",
                body_html="<p>Le <strong>zinc (Zn)</strong> est le deuxième oligo-élément le plus abondant après le fer. Il est nécessaire à plus de 300 enzymes. Rôles clés : défense immunitaire, cicatrisation, goût et odorat, croissance, santé de la peau et des cheveux. Le corps contient 2–3 g de zinc, répartis entre muscles (60%), os (30%) et autres tissus.</p>"),
        Section(id="normal-ranges", level=2, heading="Valeurs normales du zinc",
                body_html="<p>Zinc sérique normal chez l&rsquo;adulte : <strong>60–120 µg/dL</strong> (9,2–18,4 µmol/L). Les niveaux varient selon l&rsquo;heure, les repas, l&rsquo;inflammation et les médicaments. Un prélèvement à jeun le matin donne le résultat le plus fiable.</p>"),
        Section(id="causes", level=2, heading="Causes d'un zinc bas ou élevé",
                body_html="<p><strong>Zinc bas</strong> : apport alimentaire insuffisant (surtout régimes végétariens/végans), malabsorption (cœliaque, Crohn), maladie hépatique ou rénale chronique, grossesse, alcoolisme et médicaments. <strong>Zinc élevé</strong> : rare, généralement dû à une supplémentation excessive. L&rsquo;excès chronique (>150 mg/jour) peut causer une <strong>carence en cuivre</strong>.</p>"),
        Section(id="symptoms", level=2, heading="Symptômes de la carence en zinc",
                body_html="<p>Immunité altérée, chute de cheveux, mauvaise cicatrisation, troubles du goût et de l&rsquo;odorat, éruptions cutanées (acrodermatitis enteropathica), retard de croissance chez l&rsquo;enfant, cécité nocturne et troubles de l&rsquo;humeur. La carence légère à modérée est fréquente chez les personnes âgées, les femmes enceintes et les végétariens.</p>"),
        Section(id="related-tests", level=2, heading="Analyses associées",
                body_html="<p>Le zinc est interprété avec : <strong>cuivre</strong>, <strong>albumine</strong>, <strong>hémogramme</strong>, <strong>bilan martial</strong> (<a href=\"/fr/blog/carence-fer-ferritine\">guide fer</a>) et <strong>phosphatase alcaline</strong> (enzyme zinc-dépendante).</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter un médecin",
                body_html="<p>Consultez si votre zinc est sous 60 µg/dL, si vous avez des symptômes de carence, suivez un régime végétarien/végan, avez une maladie chronique avec malabsorption, êtes enceinte, ou prenez des suppléments de zinc à haute dose.</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment NoryaAI vous aide avec votre zinc",
                body_html="<p><a href=\"/analyze\">Téléchargez votre bilan</a> et notre IA extrait le zinc et tous les biomarqueurs, compare aux valeurs de référence, signale les anomalies et génère un résumé pour votre médecin. <a href=\"/pricing\">Formules tarifaires</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement médical",
                body_html="<p><strong>Cet article est fourni à titre informatif uniquement. Consultez toujours un professionnel de santé. NoryaAI propose une analyse automatisée mais ne remplace pas le jugement médical professionnel.</strong></p>"),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Analisi dello zinco nel sangue: cosa significa il tuo risultato",
                body_html="<p>Lo zinco è un oligoelemento essenziale coinvolto in oltre 300 reazioni enzimatiche. È vitale per l&rsquo;immunità, la guarigione delle ferite, la sintesi proteica e la crescita. La carenza di zinco è sorprendentemente comune in tutto il mondo.</p><p>Il valore di zinco nel tuo esame misura la concentrazione sierica. Un valore basso può influenzare immunità, pelle e percezione del gusto.</p><p>Questo articolo è educativo e non sostituisce il parere medico.</p>"),
        Section(id="what-is", level=2, heading="Cos'è lo zinco e perché è importante?",
                body_html="<p>Lo <strong>zinco (Zn)</strong> è il secondo oligoelemento più abbondante dopo il ferro. È necessario per oltre 300 enzimi. Ruoli chiave: difesa immunitaria, cicatrizzazione, gusto e olfatto, crescita, salute di pelle e capelli. Il corpo contiene 2–3 g di zinco, distribuiti tra muscoli (60%), ossa (30%) e altri tessuti.</p>"),
        Section(id="normal-ranges", level=2, heading="Valori normali dello zinco",
                body_html="<p>Zinco sierico normale negli adulti: <strong>60–120 µg/dL</strong> (9,2–18,4 µmol/L). I livelli sono influenzati dall&rsquo;ora del giorno, dai pasti, dall&rsquo;infiammazione e da farmaci. Un prelievo a digiuno mattutino fornisce il risultato più attendibile.</p>"),
        Section(id="causes", level=2, heading="Cause di zinco basso e alto",
                body_html="<p><strong>Zinco basso</strong>: apporto alimentare inadeguato (specie diete vegetariane/vegane), malassorbimento (celiachia, Crohn), epatopatia o nefropatia cronica, gravidanza, alcolismo e farmaci. <strong>Zinco alto</strong>: raro, di solito da integrazione eccessiva. L&rsquo;eccesso cronico (>150 mg/die) può causare <strong>carenza di rame</strong>.</p>"),
        Section(id="symptoms", level=2, heading="Sintomi della carenza di zinco",
                body_html="<p>Immunità compromessa, perdita di capelli, scarsa guarigione, alterazioni del gusto e dell&rsquo;olfatto, eruzioni cutanee (acrodermatite enteropatica), ritardo della crescita nei bambini, cecità notturna e disturbi dell&rsquo;umore. La carenza lieve-moderata è comune in anziani, donne in gravidanza e vegetariani.</p>"),
        Section(id="related-tests", level=2, heading="Esami correlati",
                body_html="<p>Lo zinco si interpreta con: <strong>rame</strong>, <strong>albumina</strong>, <strong>emocromo</strong>, <strong>assetto marziale</strong> (<a href=\"/it/blog/carenza-ferro-ferritina\">guida ferro</a>) e <strong>fosfatasi alcalina</strong> (enzima zinco-dipendente).</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico",
                body_html="<p>Consulta se lo zinco è sotto 60 µg/dL, hai sintomi di carenza, segui una dieta vegetariana/vegana, hai una malattia cronica con malassorbimento, sei in gravidanza o assumi integratori di zinco ad alto dosaggio.</p>"),
        Section(id="how-norya-helps", level=2, heading="Come NoryaAI ti aiuta con lo zinco",
                body_html="<p><a href=\"/analyze\">Carica il referto</a> e la nostra IA estrae zinco e biomarcatori, confronta con i riferimenti, segnala anomalie e genera un riepilogo per il medico. <a href=\"/pricing\">Piani tariffari</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avvertenza medica",
                body_html="<p><strong>Questo articolo è solo informativo. Non costituisce consulenza medica. Consulta sempre un professionista sanitario. NoryaAI offre analisi automatizzate ma non sostituisce il giudizio medico.</strong></p>"),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="בדיקת אבץ בדם: מה המשמעות של התוצאה שלך?",
                body_html="<p>אבץ הוא יסוד קורט חיוני המשתתף ביותר מ-300 תגובות אנזימטיות בגוף. הוא חיוני לתפקוד חיסוני, ריפוי פצעים, סינתזת חלבונים וגדילה תקינה. למרות חשיבותו, חסר אבץ נפוץ להפליא&mdash;ארגון הבריאות העולמי מעריך שכשליש מאוכלוסיית העולם בסיכון.</p><p>ערך האבץ בבדיקת הדם שלך מודד את ריכוז האבץ בסרום. ערך נמוך עשוי להשפיע על חסינות, בריאות העור ותפיסת הטעם.</p><p>מאמר זה חינוכי בלבד ואינו מחליף ייעוץ רפואי.</p>"),
        Section(id="what-is", level=2, heading="מהו אבץ ומדוע הוא חשוב?",
                body_html="<p><strong>אבץ (Zn)</strong> הוא יסוד הקורט השני בשכיחותו בגוף אחרי ברזל. הוא נחוץ ליותר מ-300 אנזימים. תפקידים מפתח: הגנה חיסונית, ריפוי פצעים, טעם וריח, גדילה והתפתחות, בריאות עור ושיער. הגוף מכיל 2–3 גרם אבץ, מפוזרים בשרירים (60%), עצמות (30%) ורקמות אחרות.</p>"),
        Section(id="normal-ranges", level=2, heading="טווחי אבץ תקינים",
                body_html="<p>אבץ תקין בסרום למבוגרים: <strong>60–120 µg/dL</strong> (9.2–18.4 µmol/L). הרמות מושפעות משעת היום, ארוחות, דלקת ותרופות. דגימת צום בוקר נותנת את התוצאה האמינה ביותר.</p>"),
        Section(id="causes", level=2, heading="גורמים לאבץ נמוך וגבוה",
                body_html="<p><strong>אבץ נמוך</strong>: צריכה תזונתית לא מספקת (במיוחד בתזונה צמחונית/טבעונית), תת-ספיגה (צליאק, קרוהן), מחלת כבד או כליות כרונית, הריון, אלכוהוליזם ותרופות. <strong>אבץ גבוה</strong>: נדיר, בדרך כלל מתיסוף מופרז. עודף כרוני (&gt;150 mg/יום) עלול לגרום <strong>לחסר נחושת</strong>.</p>"),
        Section(id="symptoms", level=2, heading="תסמיני חסר אבץ",
                body_html="<p>חסינות לקויה עם זיהומים תכופים, נשירת שיער, ריפוי פצעים איטי, שינויים בטעם ובריח, פריחות עור (אקרודרמטיטיס אנטרופתיקה), עיכוב גדילה בילדים, עיוורון לילה והפרעות מצב רוח. חסר קל עד בינוני שכיח בקשישים, נשים בהריון וצמחונים.</p>"),
        Section(id="related-tests", level=2, heading="בדיקות קשורות",
                body_html="<p>אבץ מתפרש יחד עם: <strong>נחושת</strong>, <strong>אלבומין</strong>, <strong>ספירת דם</strong>, <strong>בדיקות ברזל</strong> (<a href=\"/he/blog/iron-deficiency-ferritin-meaning\">מדריך ברזל</a>) ו<strong>פוספטאז אלקלי</strong> (אנזים תלוי-אבץ).</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא",
                body_html="<p>פנה לרופא אם האבץ שלך מתחת ל-60 µg/dL, יש לך תסמיני חסר, אתה צמחוני/טבעוני ללא מעקב, יש לך מחלה כרונית עם תת-ספיגה, את בהריון, או שאתה נוטל תוספי אבץ במינון גבוה.</p>"),
        Section(id="how-norya-helps", level=2, heading="איך NoryaAI עוזר לך עם תוצאות האבץ",
                body_html="<p><a href=\"/analyze\">העלה את הדוח שלך</a> ומנוע ה-AI מחלץ אבץ וכל הסמנים, משווה לטווחי ייחוס, מסמן חריגים ומייצר סיכום לרופא. <a href=\"/pricing\">תוכניות תמחור</a>.</p>"),
        Section(id="disclaimer", level=2, heading="הצהרה רפואית",
                body_html="<p><strong>מאמר זה למטרות מידע וחינוך בלבד. אינו מהווה ייעוץ רפואי. התייעץ תמיד עם איש מקצוע מוסמך. NoryaAI מספק ניתוח אוטומטי אך אינו מחליף שיקול דעת רפואי.</strong></p>"),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="ज़िंक रक्त परीक्षण: आपके परिणाम का क्या मतलब है?",
                body_html="<p>ज़िंक एक आवश्यक ट्रेस मिनरल है जो शरीर में 300 से अधिक एंज़ाइमेटिक प्रतिक्रियाओं में भाग लेता है। यह प्रतिरक्षा कार्य, घाव भरने, प्रोटीन संश्लेषण और सामान्य वृद्धि के लिए महत्वपूर्ण है। इसके महत्व के बावजूद, ज़िंक की कमी आश्चर्यजनक रूप से आम है।</p><p>आपकी रक्त जाँच में ज़िंक मान सीरम में ज़िंक की सांद्रता को मापता है। कम मान प्रतिरक्षा, त्वचा और स्वाद को प्रभावित कर सकता है।</p><p>यह लेख शैक्षिक है और चिकित्सा सलाह का विकल्प नहीं है।</p>"),
        Section(id="what-is", level=2, heading="ज़िंक क्या है और यह क्यों महत्वपूर्ण है?",
                body_html="<p><strong>ज़िंक (Zn)</strong> आयरन के बाद शरीर में सबसे प्रचुर दूसरा ट्रेस तत्व है। 300 से अधिक एंज़ाइमों के लिए आवश्यक है। मुख्य भूमिकाएँ: प्रतिरक्षा रक्षा, घाव भरना, स्वाद और गंध, वृद्धि और विकास, त्वचा और बालों का स्वास्थ्य। शरीर में 2–3 ग्राम ज़िंक होता है जो मांसपेशियों (60%), हड्डियों (30%) और अन्य ऊतकों में वितरित है।</p>"),
        Section(id="normal-ranges", level=2, heading="सामान्य ज़िंक स्तर",
                body_html="<p>वयस्कों में सामान्य सीरम ज़िंक: <strong>60–120 µg/dL</strong> (9.2–18.4 µmol/L)। स्तर दिन के समय, भोजन, सूजन और दवाओं से प्रभावित होते हैं। सुबह का उपवास नमूना सबसे विश्वसनीय परिणाम देता है।</p>"),
        Section(id="causes", level=2, heading="कम और उच्च ज़िंक के कारण",
                body_html="<p><strong>कम ज़िंक</strong>: अपर्याप्त आहार (विशेषकर शाकाहारी/वीगन), कुअवशोषण (सीलिएक, क्रोहन), पुरानी लिवर या किडनी रोग, गर्भावस्था, शराब की लत और दवाएँ। <strong>उच्च ज़िंक</strong>: दुर्लभ, आमतौर पर अत्यधिक सप्लीमेंट से। दीर्घकालिक अतिरिक्त (&gt;150 mg/दिन) <strong>कॉपर की कमी</strong> का कारण बन सकता है।</p>"),
        Section(id="symptoms", level=2, heading="ज़िंक की कमी के लक्षण",
                body_html="<p>बिगड़ी प्रतिरक्षा, बालों का झड़ना, खराब घाव भरना, स्वाद/गंध में बदलाव, त्वचा पर चकत्ते (एक्रोडर्मेटाइटिस एंटेरोपैथिका), बच्चों में विकास मंदता, रतौंधी और मूड विकार। हल्की से मध्यम कमी बुजुर्गों, गर्भवती महिलाओं और शाकाहारियों में आम है।</p>"),
        Section(id="related-tests", level=2, heading="संबंधित परीक्षण",
                body_html="<p>ज़िंक की व्याख्या इनके साथ की जाती है: <strong>कॉपर</strong>, <strong>एल्बुमिन</strong>, <strong>CBC</strong>, <strong>आयरन स्टडीज़</strong> (<a href=\"/hi/blog/iron-deficiency-ferritin-meaning\">आयरन गाइड</a>) और <strong>एल्कलाइन फॉस्फेटेज़</strong> (ज़िंक-निर्भर एंज़ाइम)।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें",
                body_html="<p>डॉक्टर से मिलें यदि ज़िंक 60 µg/dL से कम है, कमी के लक्षण हैं, शाकाहारी/वीगन हैं और ज़िंक की निगरानी नहीं कर रहे, कुअवशोषण वाली पुरानी बीमारी है, गर्भवती हैं, या उच्च खुराक ज़िंक सप्लीमेंट ले रहे हैं।</p>"),
        Section(id="how-norya-helps", level=2, heading="NoryaAI आपके ज़िंक परिणामों में कैसे मदद करता है",
                body_html="<p><a href=\"/analyze\">रिपोर्ट अपलोड करें</a> और हमारा AI ज़िंक और सभी बायोमार्कर निकालता है, संदर्भ सीमाओं से तुलना करता है, असामान्यताएँ चिह्नित करता है और डॉक्टर के लिए सारांश बनाता है। <a href=\"/pricing\">मूल्य निर्धारण</a>।</p>"),
        Section(id="disclaimer", level=2, heading="चिकित्सा अस्वीकरण",
                body_html="<p><strong>यह लेख केवल सूचनात्मक है। चिकित्सा सलाह नहीं है। हमेशा योग्य स्वास्थ्य पेशेवर से परामर्श करें। NoryaAI स्वचालित विश्लेषण प्रदान करता है लेकिन पेशेवर चिकित्सा निर्णय का विकल्प नहीं है।</strong></p>"),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="تحليل الزنك في الدم: ماذا تعني نتيجتك؟",
                body_html="<p>الزنك عنصر شحيح أساسي يشارك في أكثر من 300 تفاعل إنزيمي في الجسم. وهو حيوي للمناعة وشفاء الجروح وتخليق البروتين والنمو الطبيعي. رغم أهميته، فإن نقص الزنك شائع بشكل مفاجئ&mdash;تقدر منظمة الصحة العالمية أن نحو ثلث سكان العالم معرضون للخطر.</p><p>يقيس مستوى الزنك في تحليل الدم تركيز الزنك في المصل. قيمة منخفضة قد تؤثر على المناعة والبشرة وإدراك الطعم.</p><p>هذا المقال تثقيفي ولا يحل محل الاستشارة الطبية.</p>"),
        Section(id="what-is", level=2, heading="ما هو الزنك ولماذا هو مهم؟",
                body_html="<p><strong>الزنك (Zn)</strong> هو ثاني أكثر العناصر الشحيحة وفرة في الجسم بعد الحديد. وهو ضروري لأكثر من 300 إنزيم. أدوار رئيسية: الدفاع المناعي، شفاء الجروح، التذوق والشم، النمو والتطور، صحة الجلد والشعر. يحتوي الجسم على 2–3 غرام من الزنك موزعة بين العضلات (60%) والعظام (30%) والأنسجة الأخرى.</p>"),
        Section(id="normal-ranges", level=2, heading="المعدلات الطبيعية للزنك",
                body_html="<p>الزنك المصلي الطبيعي للبالغين: <strong>60–120 µg/dL</strong> (9.2–18.4 µmol/L). تتأثر المستويات بالوقت من اليوم والوجبات والالتهاب والأدوية. عينة صيام صباحية تعطي النتيجة الأكثر موثوقية.</p>"),
        Section(id="causes", level=2, heading="أسباب الزنك المنخفض والمرتفع",
                body_html="<p><strong>زنك منخفض</strong>: تناول غذائي غير كافٍ (خاصة الأنظمة النباتية)، سوء امتصاص (داء بطني، كرون)، مرض كبدي أو كلوي مزمن، حمل، إدمان كحول وأدوية. <strong>زنك مرتفع</strong>: نادر، عادة من تكميل مفرط. الفائض المزمن (&gt;150 مغ/يوم) قد يسبب <strong>نقص النحاس</strong>.</p>"),
        Section(id="symptoms", level=2, heading="أعراض نقص الزنك",
                body_html="<p>ضعف المناعة مع عدوى متكررة، تساقط الشعر، بطء التئام الجروح، تغيرات في الطعم والرائحة، طفح جلدي (التهاب الجلد الطرفي المعوي)، تأخر النمو عند الأطفال، عشى ليلي واضطرابات مزاجية. النقص الخفيف إلى المتوسط شائع عند كبار السن والحوامل والنباتيين.</p>"),
        Section(id="related-tests", level=2, heading="التحاليل المرتبطة",
                body_html="<p>يُفسّر الزنك مع: <strong>النحاس</strong>، <strong>الألبومين</strong>، <strong>تعداد الدم</strong>، <strong>دراسات الحديد</strong> (<a href=\"/ar/blog/iron-deficiency-ferritin-meaning\">دليل الحديد</a>) و<strong>الفوسفاتاز القلوي</strong> (إنزيم يعتمد على الزنك).</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى تراجع الطبيب",
                body_html="<p>راجع طبيبك إذا كان الزنك أقل من 60 µg/dL، لديك أعراض نقص، تتبع نظاماً نباتياً دون مراقبة، لديك مرض مزمن مع سوء امتصاص، أنتِ حامل، أو تتناول مكملات زنك بجرعة عالية.</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف يساعدك NoryaAI في فهم نتائج الزنك",
                body_html="<p><a href=\"/analyze\">ارفع تقريرك</a> ومحرك AI يستخرج الزنك وجميع المؤشرات، يقارن بالنطاقات المرجعية، يُبرز الشذوذ وينشئ ملخصاً للطبيب. <a href=\"/pricing\">خطط الأسعار</a>.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية الطبية",
                body_html="<p><strong>هذا المقال لأغراض إعلامية فقط. لا يشكّل نصيحة طبية. استشر دائماً مختصاً صحياً مؤهلاً. NoryaAI يوفر تحليلاً آلياً لكنه ليس بديلاً عن الحكم الطبي المهني.</strong></p>"),
    ]


# ---------------------------------------------------------------------------
# Aggregators
# ---------------------------------------------------------------------------
def get_zinc_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Zinc article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_zinc_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Zinc article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal zinc level?",
             "answer": "Normal serum zinc for adults is 60–120 µg/dL (9.2–18.4 µmol/L). Levels fluctuate with time of day, meals, and inflammation, so a morning fasting sample is most reliable."},
            {"question": "What causes low zinc levels?",
             "answer": "Common causes include inadequate dietary intake (especially vegetarian/vegan diets), malabsorption from celiac or Crohn's disease, chronic liver or kidney disease, pregnancy, alcoholism, and certain medications like diuretics and PPIs."},
            {"question": "What are the symptoms of zinc deficiency?",
             "answer": "Symptoms include frequent infections (impaired immunity), hair loss, poor wound healing, changes in taste and smell, skin rashes, growth retardation in children, night blindness, and mood disturbances."},
            {"question": "Can too much zinc be harmful?",
             "answer": "Yes. Chronic zinc excess (>150 mg/day from supplements) can cause copper deficiency, nausea, vomiting, and diarrhea. Zinc and copper compete for absorption, so high zinc intake depletes copper stores over time."},
        ],
        "tr": [
            {"question": "Normal çinko seviyesi nedir?",
             "answer": "Yetişkinlerde normal serum çinkosu 60–120 µg/dL (9,2–18,4 µmol/L) arasındadır. Sabah açlık örneği en güvenilir sonucu verir."},
            {"question": "Düşük çinko seviyesinin nedenleri nelerdir?",
             "answer": "Yetersiz beslenme (özellikle vejetaryen/vegan), emilim bozuklukları, kronik karaciğer veya böbrek hastalığı, gebelik, alkolizm ve diüretik, PPI gibi ilaçlar en sık nedenlerdir."},
            {"question": "Çinko eksikliğinin belirtileri nelerdir?",
             "answer": "Sık enfeksiyonlar, saç dökülmesi, yavaş yara iyileşmesi, tat ve koku değişiklikleri, cilt döküntüleri, çocuklarda büyüme geriliği, gece körlüğü ve ruhsal bozukluklar."},
            {"question": "Fazla çinko zararlı olabilir mi?",
             "answer": "Evet. Kronik çinko fazlalığı (günde >150 mg) bakır eksikliğine, bulantı, kusma ve ishale neden olabilir. Çinko ve bakır emilim için yarışır."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de zinc?",
             "answer": "El zinc sérico normal en adultos es 60–120 µg/dL (9,2–18,4 µmol/L). Una muestra en ayunas por la mañana es más fiable."},
            {"question": "¿Qué causa niveles bajos de zinc?",
             "answer": "Dieta insuficiente (especialmente vegetariana/vegana), malabsorción, enfermedad hepática o renal crónica, embarazo, alcoholismo y medicamentos como diuréticos e IBP."},
            {"question": "¿Cuáles son los síntomas de deficiencia de zinc?",
             "answer": "Infecciones frecuentes, caída del cabello, mala cicatrización, cambios en gusto y olfato, erupciones cutáneas, retraso del crecimiento, ceguera nocturna y alteraciones del ánimo."},
            {"question": "¿El exceso de zinc es perjudicial?",
             "answer": "Sí. El exceso crónico (>150 mg/día) puede causar deficiencia de cobre, náuseas, vómitos y diarrea."},
        ],
        "de": [
            {"question": "Was ist ein normaler Zinkwert?",
             "answer": "Normaler Serumzink bei Erwachsenen: 60–120 µg/dL (9,2–18,4 µmol/L). Eine Nüchternprobe am Morgen ist am zuverlässigsten."},
            {"question": "Was verursacht niedrige Zinkwerte?",
             "answer": "Unzureichende Ernährung (besonders vegetarisch/vegan), Malabsorption, chronische Leber- oder Nierenerkrankung, Schwangerschaft, Alkoholismus und Medikamente wie Diuretika und PPI."},
            {"question": "Welche Symptome hat Zinkmangel?",
             "answer": "Häufige Infektionen, Haarausfall, schlechte Wundheilung, Geschmacks- und Geruchsstörungen, Hautausschläge, Wachstumsverzögerung bei Kindern, Nachtblindheit und Stimmungsstörungen."},
            {"question": "Kann zu viel Zink schaden?",
             "answer": "Ja. Chronischer Überschuss (>150 mg/Tag) kann Kupfermangel, Übelkeit, Erbrechen und Durchfall verursachen."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de zinc ?",
             "answer": "Le zinc sérique normal chez l'adulte est de 60–120 µg/dL (9,2–18,4 µmol/L). Un prélèvement à jeun le matin est le plus fiable."},
            {"question": "Quelles sont les causes d'un zinc bas ?",
             "answer": "Apport alimentaire insuffisant (surtout régimes végétariens/végans), malabsorption, maladie hépatique ou rénale chronique, grossesse, alcoolisme et médicaments comme les diurétiques et les IPP."},
            {"question": "Quels sont les symptômes de la carence en zinc ?",
             "answer": "Infections fréquentes, chute de cheveux, mauvaise cicatrisation, troubles du goût et de l'odorat, éruptions cutanées, retard de croissance, cécité nocturne et troubles de l'humeur."},
            {"question": "L'excès de zinc est-il nocif ?",
             "answer": "Oui. L'excès chronique (>150 mg/jour) peut causer une carence en cuivre, des nausées, vomissements et diarrhée."},
        ],
        "it": [
            {"question": "Qual è il livello normale di zinco?",
             "answer": "Lo zinco sierico normale negli adulti è 60–120 µg/dL (9,2–18,4 µmol/L). Un prelievo a digiuno mattutino è il più attendibile."},
            {"question": "Cosa causa lo zinco basso?",
             "answer": "Apporto alimentare inadeguato (specie diete vegetariane/vegane), malassorbimento, epatopatia o nefropatia cronica, gravidanza, alcolismo e farmaci come diuretici e IPP."},
            {"question": "Quali sono i sintomi della carenza di zinco?",
             "answer": "Infezioni frequenti, perdita di capelli, scarsa cicatrizzazione, alterazioni del gusto e dell'olfatto, eruzioni cutanee, ritardo della crescita, cecità notturna e disturbi dell'umore."},
            {"question": "L'eccesso di zinco è dannoso?",
             "answer": "Sì. L'eccesso cronico (>150 mg/die) può causare carenza di rame, nausea, vomito e diarrea."},
        ],
        "he": [
            {"question": "מהי רמת אבץ תקינה?",
             "answer": "אבץ תקין בסרום למבוגרים: 60–120 µg/dL (9.2–18.4 µmol/L). דגימת צום בוקר היא האמינה ביותר."},
            {"question": "מה גורם לרמות אבץ נמוכות?",
             "answer": "צריכה תזונתית לא מספקת (במיוחד תזונה צמחונית/טבעונית), תת-ספיגה, מחלת כבד או כליות כרונית, הריון, אלכוהוליזם ותרופות כמו משתנים ו-PPI."},
            {"question": "מהם תסמיני חסר אבץ?",
             "answer": "זיהומים תכופים, נשירת שיער, ריפוי פצעים איטי, שינויים בטעם ובריח, פריחות עור, עיכוב גדילה בילדים, עיוורון לילה והפרעות מצב רוח."},
            {"question": "האם עודף אבץ מזיק?",
             "answer": "כן. עודף כרוני (>150 מ\"ג/יום) עלול לגרום חסר נחושת, בחילות, הקאות ושלשולים."},
        ],
        "hi": [
            {"question": "सामान्य ज़िंक स्तर क्या है?",
             "answer": "वयस्कों में सामान्य सीरम ज़िंक 60–120 µg/dL (9.2–18.4 µmol/L) है। सुबह का उपवास नमूना सबसे विश्वसनीय होता है।"},
            {"question": "कम ज़िंक के कारण क्या हैं?",
             "answer": "अपर्याप्त आहार (विशेषकर शाकाहारी/वीगन), कुअवशोषण, पुरानी लिवर या किडनी रोग, गर्भावस्था, शराब की लत और डाइयूरेटिक्स, PPI जैसी दवाएँ।"},
            {"question": "ज़िंक की कमी के लक्षण क्या हैं?",
             "answer": "बार-बार संक्रमण, बालों का झड़ना, खराब घाव भरना, स्वाद/गंध में बदलाव, चकत्ते, बच्चों में विकास मंदता, रतौंधी और मूड विकार।"},
            {"question": "क्या अत्यधिक ज़िंक हानिकारक है?",
             "answer": "हाँ। दीर्घकालिक अतिरिक्त (>150 mg/दिन) कॉपर की कमी, मतली, उल्टी और दस्त का कारण बन सकता है।"},
        ],
        "ar": [
            {"question": "ما هو المستوى الطبيعي للزنك؟",
             "answer": "الزنك المصلي الطبيعي للبالغين: 60–120 µg/dL (9.2–18.4 µmol/L). عينة صيام صباحية تعطي النتيجة الأكثر موثوقية."},
            {"question": "ما أسباب انخفاض الزنك؟",
             "answer": "تناول غذائي غير كافٍ (خاصة الأنظمة النباتية)، سوء امتصاص، مرض كبدي أو كلوي مزمن، حمل، إدمان كحول وأدوية مثل مدرات البول ومثبطات مضخة البروتون."},
            {"question": "ما أعراض نقص الزنك؟",
             "answer": "عدوى متكررة، تساقط الشعر، بطء التئام الجروح، تغيرات في الطعم والرائحة، طفح جلدي، تأخر النمو عند الأطفال، عشى ليلي واضطرابات مزاجية."},
            {"question": "هل الزنك الزائد ضار؟",
             "answer": "نعم. الفائض المزمن (>150 مغ/يوم) قد يسبب نقص النحاس وغثياناً وقيئاً وإسهالاً."},
        ],
    }
