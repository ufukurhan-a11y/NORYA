# -*- coding: utf-8 -*-
"""
D-Dimer blog article — full body content for all 9 languages.
Used by blog_i18n._article_d_dimer().
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
            heading="D-Dimer kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>D-Dimer</strong> değerini gördüğünüzde bu testin ne "
                "anlama geldiğini ve yüksek çıkmasının sağlığınız açısından ne ifade ettiğini merak "
                "etmeniz doğaldır. D-Dimer, vücutta kan pıhtılaşması ve pıhtı yıkımı süreçlerinin "
                "aktif olduğunu gösteren bir <strong>fibrin yıkım ürünü</strong>dür ve özellikle derin "
                "ven trombozu (DVT) ile pulmoner emboli (PE) gibi ciddi pıhtılaşma bozukluklarının "
                "değerlendirilmesinde kritik bir rol oynar.</p>"
                "<p>Bu rehber D-Dimer testinin ne ölçtüğünü, normal referans aralıklarını, "
                "<strong>D-Dimer yüksekliğinin</strong> nedenlerini, klinik önemini ve ne zaman "
                "doktora başvurmanız gerektiğini sade bir dille açıklamayı amaçlıyor. Amacımız "
                "teşhis koymak değil; sonuçlarınızı daha iyi anlayarak hekiminizle verimli bir "
                "görüşme yapmanıza yardımcı olmaktır.</p>"
                "<p>D-Dimer testinin en önemli klinik özelliği yüksek <em>duyarlılığı</em> ancak "
                "düşük <em>özgüllüğü</em>dür: normal bir D-Dimer değeri düşük riskli hastalarda "
                "DVT/PE&rsquo;yi büyük ölçüde dışlayabilir; ancak pek çok farklı durum D-Dimer&rsquo;i "
                "yükseltebilir. Bu nedenle sonuç her zaman klinik bağlamda değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="D-Dimer nedir?",
            body_html=(
                "<p><strong>D-Dimer</strong>, fibrin pıhtısının plazmin tarafından parçalanması "
                "sonucu oluşan küçük bir protein fragmanıdır. Vücutta pıhtılaşma süreci (koagülasyon) "
                "aktive olduğunda, fibrinojen fibrin ağlarına dönüşür ve bu ağlar pıhtıyı bir arada "
                "tutar. Eş zamanlı olarak fibrinolitik sistem devreye girerek pıhtıyı çözer; bu çözülme "
                "sırasında D-Dimer fragmanları kana salınır.</p>"
                "<p>Dolayısıyla kanda D-Dimer bulunması, yakın zamanda hem pıhtı oluştuğunu hem de "
                "pıhtı yıkımının gerçekleştiğini gösterir. Sağlıklı bireylerde D-Dimer düzeyi çok "
                "düşüktür çünkü fizyolojik koşullarda yaygın pıhtı oluşumu ve yıkımı beklenmez.</p>"
                "<p>D-Dimer testi özellikle tromboembolik hastalıkların (DVT, PE) dışlanmasında "
                "kullanılır. Negatif (düşük) bir D-Dimer sonucu, düşük klinik olasılıkla birleştiğinde "
                "pıhtı varlığını yüksek doğrulukla ekarte eder. Ancak pozitif (yüksek) bir sonuç "
                "tek başına tanı koydurmaz; ek görüntüleme ile doğrulanması gerekir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="D-Dimer normal değerleri (referans aralıkları)",
            body_html=(
                "<p>D-Dimer düzeyi basit bir kan testiyle ölçülür. Yaygın olarak kabul edilen "
                "eşik değer aşağıdaki tabloda özetlenmiştir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Ölçüm birimi</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal üst sınır</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU (Fibrinojen Eşdeğer Birimi)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,5 µg/mL</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU (D-Dimer Birimi)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td>'
                "</tr></tbody></table>"
                "<p><strong>50 yaş üstü hastalarda yaşa göre ayarlanmış eşik değer</strong> "
                "kullanılabilir: <em>yaş &times; 10&nbsp;ng/mL</em> (DDU birimi ile). Örneğin 70 "
                "yaşında bir hasta için eşik 700&nbsp;ng/mL&rsquo;ye yükseltilir. Bu ayarlama "
                "gereksiz görüntüleme sayısını azaltırken tanısal duyarlılığı korur.</p>"
                "<p>Laboratuvarlar arasında küçük farklılıklar olabileceğinden sonucunuzu mutlaka "
                "kendi laboratuvarınızın referans aralığı ve birim sistemiyle karşılaştırmanız "
                "önemlidir. FEU ve DDU birimleri arasında yaklaşık iki kat fark vardır; bu nedenle "
                "hangi birimin kullanıldığını bilmek kritik öneme sahiptir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="D-Dimer yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>D-Dimer yüksekliği</strong>, vücutta aktif pıhtı oluşumu ve yıkımının "
                "işaretçisidir. Ancak pek çok farklı durum D-Dimer&rsquo;i yükseltebilir:</p>"
                "<ul>"
                "<li><strong>Derin ven trombozu (DVT):</strong> Bacak damarlarında oluşan kan "
                "pıhtıları D-Dimer&rsquo;in en sık araştırılan nedenidir.</li>"
                "<li><strong>Pulmoner emboli (PE):</strong> Akciğer damarlarına pıhtı göçü; "
                "D-Dimer testi PE dışlamada kilit rol oynar.</li>"
                "<li><strong>Dissemine intravasküler koagülasyon (DİK):</strong> Yaygın damar içi "
                "pıhtılaşma ve eş zamanlı kanama sendromu; D-Dimer çok yüksek olur.</li>"
                "<li><strong>Cerrahi ve travma:</strong> Operasyon veya yaralanma sonrası doku hasarı "
                "pıhtılaşma kaskadını aktive eder.</li>"
                "<li><strong>Hamilelik:</strong> Gebelikte fizyolojik olarak D-Dimer yükselir ve "
                "trimester ilerledikçe artmaya devam eder.</li>"
                "<li><strong>Kanser:</strong> Malign tümörler prokoagülan duruma yol açarak "
                "D-Dimer&rsquo;i artırır.</li>"
                "<li><strong>Enfeksiyon ve sepsis:</strong> Ağır enfeksiyonlar koagülasyon sistemini "
                "aktive eder.</li>"
                "<li><strong>Karaciğer hastalığı:</strong> Pıhtılaşma faktörlerinin sentez ve yıkım "
                "dengesindeki bozukluk D-Dimer&rsquo;i yükseltebilir.</li>"
                "<li><strong>İleri yaş:</strong> Yaşla birlikte bazal D-Dimer düzeyi doğal olarak "
                "artar; bu nedenle yaşa uyarlanmış eşik değerler önerilmektedir.</li>"
                "</ul>"
                "<p>D-Dimer testinin <strong>duyarlılığı yüksek</strong> ancak <strong>özgüllüğü "
                "düşüktür</strong>. Yani normal bir D-Dimer düşük riskli hastalarda pıhtıyı büyük "
                "ölçüde dışlar; ancak yüksek D-Dimer pek çok farklı durumda görülebilir ve tek "
                "başına tanı koydurmaz.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="DVT ve PE belirtileri",
            body_html=(
                "<p>D-Dimer testinin en sık istendiği klinik senaryolar DVT ve PE şüphesidir. Bu "
                "durumların tipik belirtileri şunlardır:</p>"
                "<p><strong>Derin ven trombozu (DVT) belirtileri:</strong></p>"
                "<ul>"
                "<li>Genellikle tek bacakta şişlik, ağrı ve kızarıklık</li>"
                "<li>Etkilenen bacakta sıcaklık artışı</li>"
                "<li>Baldır ağrısı, özellikle yürürken veya ayağı yukarı bükerken</li>"
                "</ul>"
                "<p><strong>Pulmoner emboli (PE) belirtileri:</strong></p>"
                "<ul>"
                "<li>Ani nefes darlığı</li>"
                "<li>Göğüs ağrısı (özellikle derin nefes alırken artan, plöretik tip)</li>"
                "<li>Hızlı kalp atışı (taşikardi)</li>"
                "<li>Hemoptizi (kanlı balgam) — bazı hastalarda</li>"
                "<li>Baş dönmesi veya bayılma hissi</li>"
                "</ul>"
                "<p>Bu belirtiler acil tıbbi müdahale gerektiren ciddi durumlara işaret edebilir. "
                "Özellikle PE potansiyel olarak hayatı tehdit edici bir durumdur ve erken tanı yaşam "
                "kurtarıcıdır.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlişkili testler",
            body_html=(
                "<p>D-Dimer yüksekliği saptandığında veya tromboembolik hastalık şüphesinde ek "
                "testler istenir:</p>"
                "<ul>"
                "<li><strong>PT/INR:</strong> Dışsal pıhtılaşma yolunu değerlendirir; warfarin "
                "tedavisinin izlenmesinde de kullanılır.</li>"
                "<li><strong>aPTT:</strong> İçsel pıhtılaşma yolunu değerlendirir; heparin "
                "takibinde önemlidir.</li>"
                "<li><strong>Fibrinojen:</strong> Pıhtılaşma sürecinin ana yapı taşı; DİK gibi "
                "durumlarda azalabilir.</li>"
                "<li><strong>Trombosit sayısı:</strong> Pıhtılaşma ve kanama dengesini "
                "değerlendirmek için gereklidir.</li>"
                "<li><strong>BT anjiyografi (pulmoner):</strong> PE tanısında altın standart "
                "görüntüleme yöntemidir.</li>"
                "<li><strong>Doppler ultrasonografi:</strong> DVT tanısında bacak damarlarının "
                "değerlendirilmesi için kullanılır.</li>"
                "</ul>"
                "<p>Bu testlerin birlikte yorumlanması, klinik olasılık skorları (Wells skoru, "
                "Geneva skoru) ile birleştirildiğinde doğru tanı ve tedavi planlamasında kritik "
                "öneme sahiptir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda <strong>acil olarak</strong> tıbbi yardım almalısınız:</p>"
                "<ul>"
                "<li>Ani başlayan nefes darlığı veya göğüs ağrısı</li>"
                "<li>Tek bacakta ani şişlik, ağrı ve kızarıklık</li>"
                "<li>Kan tahlilinde D-Dimer yüksekliği ile birlikte yukarıdaki belirtiler</li>"
                "<li>Kanlı balgam veya bayılma hissi</li>"
                "</ul>"
                "<p>Pulmoner emboli yaşam tehdit eden bir durumdur ve acil tedavi gerektirir. DVT "
                "tedavi edilmezse pıhtı akciğerlere göç ederek PE&rsquo;ye neden olabilir. Erken "
                "tanı ve antikoagülan tedavi (kan sulandırıcılar) komplikasyon riskini dramatik "
                "şekilde azaltır.</p>"
                "<p>D-Dimer yüksekliği tek başına bir tanı değildir; ancak klinik şüphe ile birlikte "
                "değerlendirildiğinde ileri tetkiklerin yapılmasını zorunlu kılar. Sonucunuzu bir "
                "sağlık profesyoneli ile mutlaka paylaşın.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI D-Dimer sonuçlarınızı nasıl değerlendirir?",
            body_html=(
                "<p><strong>NoryaAI</strong>, kan tahlili raporunuzu yüklediğinizde D-Dimer dahil "
                "tüm biyobelirteçlerinizi yaşınıza, cinsiyetinize ve klinik bağlamınıza göre analiz "
                "eder. Yapay zekâ destekli sistemimiz referans aralık dışı değerleri vurgular, olası "
                "nedenleri özetler ve hekiminize sormak isteyebileceğiniz soruları önerir.</p>"
                "<p>Sonuçlarınızı hemen değerlendirmek için <a href=\"/analyze\">lab raporunuzu "
                "yükleyin</a>. Farklı plan seçeneklerimiz hakkında bilgi almak için "
                "<a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edebilirsiniz. NoryaAI "
                "hekim muayenesinin yerini almaz; amacımız sizi bilgilendirerek doktorunuzla daha "
                "verimli bir görüşme yapmanızı sağlamaktır.</p>"
                "<p>D-Dimer değeriniz yüksekse panik yapmayın; ancak nefes darlığı veya bacak "
                "şişliği gibi belirtileriniz varsa vakit kaybetmeden acil tıbbi değerlendirme "
                "yaptırmanız önemlidir.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Yasal uyarı",
            body_html=(
                "<p><strong>Bu içerik yalnızca bilgilendirme amacıyla hazırlanmıştır ve tıbbi tavsiye, "
                "tanı veya tedavi yerine geçmez.</strong> Kan tahlili sonuçlarınızı mutlaka bir sağlık "
                "profesyoneli ile birlikte değerlendirin. NoryaAI bir hekim muayenesi veya tıbbi "
                "konsültasyon yerine geçmez. Sağlık kararlarınızı her zaman doktorunuza danışarak verin. "
                '<a href="/analyze">Analiz sayfamızda</a> sonuçlarınız hakkında ön bilgi edinebilirsiniz.</p>'
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
            heading="D-Dimer blood test: what your results mean",
            body_html=(
                "<p>If your lab report shows an elevated <strong>D-Dimer</strong> level, you may be "
                "wondering what this test measures and whether you should be concerned. D-Dimer is a "
                "<strong>fibrin degradation product</strong> — a small protein fragment released when "
                "blood clots are broken down — and it plays a critical role in evaluating serious "
                "clotting disorders such as deep vein thrombosis (DVT) and pulmonary embolism (PE).</p>"
                "<p>This guide explains what the <strong>D-Dimer blood test</strong> measures, normal "
                "reference ranges, causes of <strong>elevated D-Dimer</strong>, its clinical "
                "significance, and when you should see a doctor. Our goal is not to diagnose — it is "
                "to help you understand your results so you can have a more productive conversation "
                "with your healthcare provider.</p>"
                "<p>The key clinical feature of the D-Dimer test is its high <em>sensitivity</em> but "
                "low <em>specificity</em>: a normal D-Dimer can help <strong>rule out</strong> DVT/PE "
                "in low-risk patients, but many different conditions can cause it to be elevated. "
                "Results must always be interpreted in clinical context.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is D-Dimer?",
            body_html=(
                "<p><strong>D-Dimer</strong> is a small protein fragment produced when a fibrin blood "
                "clot is broken down by plasmin. When the coagulation cascade is activated, fibrinogen "
                "is converted into fibrin strands that hold a clot together. Simultaneously, the "
                "fibrinolytic system works to dissolve the clot, and D-Dimer fragments are released "
                "into the blood during this process.</p>"
                "<p>The presence of D-Dimer in the blood therefore indicates that both clot formation "
                "and clot breakdown have recently occurred. In healthy individuals, D-Dimer levels are "
                "very low because widespread clot formation and breakdown are not expected under normal "
                "physiological conditions.</p>"
                "<p>The D-Dimer test is used primarily to help <strong>rule out</strong> "
                "thromboembolic disease (DVT, PE). A negative (low) D-Dimer result, combined with a "
                "low clinical probability, can exclude a clot with high accuracy. However, a positive "
                "(elevated) result does not diagnose a clot by itself — further imaging is needed for "
                "confirmation.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal D-Dimer levels (reference ranges)",
            body_html=(
                "<p>D-Dimer is measured with a simple blood draw. The commonly used cut-off values "
                "are summarised below:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Unit</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal upper limit</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU (Fibrinogen Equivalent Units)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.5 µg/mL</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU (D-Dimer Units)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td>'
                "</tr></tbody></table>"
                "<p>For patients <strong>over 50 years of age</strong>, an age-adjusted cut-off may "
                "be used: <em>age &times; 10&nbsp;ng/mL</em> (DDU). For example, in a 70-year-old "
                "patient the threshold would be raised to 700&nbsp;ng/mL. This adjustment reduces "
                "unnecessary imaging while maintaining diagnostic sensitivity.</p>"
                "<p>Note that FEU and DDU units differ by approximately a factor of two — knowing "
                "which unit your laboratory uses is critical for correct interpretation. Always "
                "compare your result with your own laboratory&rsquo;s reference range and unit "
                "system.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high D-Dimer",
            body_html=(
                "<p>An elevated <strong>D-Dimer</strong> indicates active clot formation and breakdown "
                "somewhere in the body. However, many conditions can raise it:</p>"
                "<ul>"
                "<li><strong>Deep vein thrombosis (DVT):</strong> Blood clots in the leg veins are "
                "the most commonly investigated cause of elevated D-Dimer.</li>"
                "<li><strong>Pulmonary embolism (PE):</strong> Migration of a clot to the pulmonary "
                "arteries; D-Dimer testing is central to PE exclusion.</li>"
                "<li><strong>Disseminated intravascular coagulation (DIC):</strong> Widespread "
                "intravascular clotting with simultaneous bleeding; D-Dimer is markedly elevated.</li>"
                "<li><strong>Surgery and trauma:</strong> Tissue damage activates the coagulation "
                "cascade.</li>"
                "<li><strong>Pregnancy:</strong> D-Dimer rises physiologically during pregnancy and "
                "continues to increase with each trimester.</li>"
                "<li><strong>Cancer:</strong> Malignancies create a procoagulant state that increases "
                "D-Dimer.</li>"
                "<li><strong>Infection and sepsis:</strong> Severe infections activate the coagulation "
                "system.</li>"
                "<li><strong>Liver disease:</strong> Disrupted synthesis and breakdown of clotting "
                "factors can elevate D-Dimer.</li>"
                "<li><strong>Ageing:</strong> Baseline D-Dimer naturally rises with age, which is why "
                "age-adjusted cut-offs are recommended for patients over 50.</li>"
                "</ul>"
                "<p>The D-Dimer test has <strong>high sensitivity but low specificity</strong>. A "
                "normal D-Dimer largely rules out clots in low-risk patients, but an elevated D-Dimer "
                "can occur in many conditions and does not confirm a diagnosis on its own.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of DVT and PE",
            body_html=(
                "<p>The two most common clinical scenarios prompting a D-Dimer test are suspected "
                "DVT and PE. Their typical symptoms include:</p>"
                "<p><strong>Deep vein thrombosis (DVT) symptoms:</strong></p>"
                "<ul>"
                "<li>Swelling, pain, and redness usually in one leg</li>"
                "<li>Warmth over the affected area</li>"
                "<li>Calf pain, especially when walking or flexing the foot upward</li>"
                "</ul>"
                "<p><strong>Pulmonary embolism (PE) symptoms:</strong></p>"
                "<ul>"
                "<li>Sudden shortness of breath</li>"
                "<li>Chest pain (often pleuritic — worsens with deep breathing)</li>"
                "<li>Rapid heart rate (tachycardia)</li>"
                "<li>Haemoptysis (coughing up blood) — in some patients</li>"
                "<li>Dizziness or feeling faint</li>"
                "</ul>"
                "<p>These symptoms may indicate life-threatening conditions requiring emergency "
                "medical care. PE in particular can be fatal if not diagnosed and treated promptly.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>When D-Dimer is elevated or thromboembolic disease is suspected, additional "
                "tests are ordered:</p>"
                "<ul>"
                "<li><strong>PT/INR:</strong> Evaluates the extrinsic coagulation pathway; also "
                "used to monitor warfarin therapy.</li>"
                "<li><strong>aPTT:</strong> Evaluates the intrinsic coagulation pathway; important "
                "for heparin monitoring.</li>"
                "<li><strong>Fibrinogen:</strong> The main building block of clots; may be consumed "
                "in conditions like DIC.</li>"
                "<li><strong>Platelet count:</strong> Essential for assessing the balance between "
                "clotting and bleeding.</li>"
                "<li><strong>CT pulmonary angiography (CTPA):</strong> The gold-standard imaging "
                "study for diagnosing PE.</li>"
                "<li><strong>Doppler ultrasound:</strong> Used to visualise leg veins and detect "
                "DVT.</li>"
                "</ul>"
                "<p>Interpreting these tests together with clinical probability scores (Wells score, "
                "Geneva score) is essential for accurate diagnosis and treatment planning.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>Seek <strong>emergency medical attention</strong> if you experience:</p>"
                "<ul>"
                "<li>Sudden shortness of breath or chest pain</li>"
                "<li>Sudden swelling, pain, and redness in one leg</li>"
                "<li>An elevated D-Dimer alongside the symptoms above</li>"
                "<li>Coughing up blood or feeling faint</li>"
                "</ul>"
                "<p>Pulmonary embolism is a life-threatening condition that requires immediate "
                "treatment. Untreated DVT can progress to PE if the clot migrates to the lungs. Early "
                "diagnosis and anticoagulant therapy (blood thinners) dramatically reduce the risk of "
                "complications.</p>"
                "<p>An elevated D-Dimer is not a diagnosis in itself, but when combined with clinical "
                "suspicion it mandates further investigation. Always share your results with a "
                "qualified healthcare professional.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How NoryaAI helps you understand D-Dimer results",
            body_html=(
                "<p><strong>NoryaAI</strong> analyses your full blood-test report — including D-Dimer — "
                "in the context of your age, sex, and clinical background. Our AI-powered system "
                "highlights out-of-range values, summarises possible causes, and suggests questions "
                "you may want to ask your doctor.</p>"
                "<p>Ready to get started? <a href=\"/analyze\">Upload your lab report</a> for an "
                "instant analysis. Visit our <a href=\"/pricing\">pricing page</a> to explore plan "
                "options. NoryaAI does not replace a physician; our goal is to empower you with "
                "information so your next medical consultation is more productive.</p>"
                "<p>If your D-Dimer is elevated, do not panic — but if you have symptoms such as "
                "shortness of breath or leg swelling, seek emergency evaluation without delay.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This content is for informational purposes only and does not constitute "
                "medical advice, diagnosis, or treatment.</strong> Always discuss your blood-test "
                "results with a qualified healthcare professional. NoryaAI is not a substitute for a "
                "medical consultation. Make all health-related decisions in consultation with your "
                'doctor. <a href="/analyze">Visit our analysis page</a> for preliminary insights '
                "into your results.</p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# SPANISH
# ─────────────────────────────────────────────────────────────────────
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Análisis de D-Dímero en sangre: qué significan sus resultados", body_html=(
            "<p>Si su informe de laboratorio muestra un nivel elevado de <strong>D-Dímero</strong>, es natural preguntarse qué mide esta prueba y si debe preocuparse. El D-Dímero es un <strong>producto de degradación de la fibrina</strong> que indica actividad de formación y destrucción de coágulos en el organismo, y es fundamental en la evaluación de la trombosis venosa profunda (TVP) y la embolia pulmonar (EP).</p>"
            "<p>Esta guía explica qué mide el <strong>análisis de D-Dímero</strong>, los valores de referencia, las causas de un <strong>D-Dímero elevado</strong>, su relevancia clínica y cuándo consultar al médico. Nuestro objetivo es ayudarle a comprender sus resultados.</p>"
            "<p>La característica clave del D-Dímero es su alta <em>sensibilidad</em> pero baja <em>especificidad</em>: un resultado normal puede descartar TVP/EP en pacientes de bajo riesgo, pero muchas condiciones pueden elevarlo.</p>"
        )),
        Section(id="what-is", level=2, heading="¿Qué es el D-Dímero?", body_html=(
            "<p>El <strong>D-Dímero</strong> es un fragmento proteico producido cuando la plasmina degrada un coágulo de fibrina. Cuando se activa la cascada de coagulación, el fibrinógeno se convierte en hebras de fibrina que mantienen el coágulo. Simultáneamente, el sistema fibrinolítico disuelve el coágulo liberando fragmentos de D-Dímero.</p>"
            "<p>Su presencia indica que recientemente ha habido formación y destrucción de coágulos. En personas sanas los niveles son muy bajos porque no se espera coagulación generalizada en condiciones normales.</p>"
            "<p>La prueba se usa principalmente para <strong>descartar</strong> enfermedad tromboembólica. Un resultado negativo con baja probabilidad clínica excluye un coágulo con alta precisión; un resultado positivo no confirma por sí solo la existencia de un trombo.</p>"
        )),
        Section(id="normal-ranges", level=2, heading="Valores normales de D-Dímero", body_html=(
            "<p>El D-Dímero se mide con una simple extracción de sangre:</p>"
            '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Unidad</th>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Límite superior normal</th>'
            '</tr></thead><tbody><tr>'
            '<td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU</td>'
            '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,5 µg/mL</td>'
            '</tr><tr>'
            '<td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU</td>'
            '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td>'
            '</tr></tbody></table>'
            "<p>Para pacientes <strong>mayores de 50 años</strong> se puede usar un umbral ajustado por edad: <em>edad &times; 10&nbsp;ng/mL</em> (DDU). Esto reduce las pruebas de imagen innecesarias sin perder sensibilidad diagnóstica.</p>"
            "<p>Las unidades FEU y DDU difieren aproximadamente en un factor de dos. Compare siempre con el rango y unidades de su laboratorio.</p>"
        )),
        Section(id="causes", level=2, heading="Causas de D-Dímero elevado", body_html=(
            "<p>Un <strong>D-Dímero elevado</strong> indica actividad de coagulación y fibrinólisis. Son muchas las condiciones que pueden elevarlo:</p>"
            "<ul>"
            "<li><strong>TVP:</strong> Coágulos en las venas de las piernas — causa más frecuentemente investigada.</li>"
            "<li><strong>EP:</strong> Migración de un coágulo a las arterias pulmonares.</li>"
            "<li><strong>CID:</strong> Coagulación intravascular diseminada con sangrado simultáneo.</li>"
            "<li><strong>Cirugía y trauma:</strong> El daño tisular activa la cascada de coagulación.</li>"
            "<li><strong>Embarazo:</strong> El D-Dímero sube fisiológicamente durante la gestación.</li>"
            "<li><strong>Cáncer:</strong> Los tumores crean un estado procoagulante.</li>"
            "<li><strong>Infección y sepsis:</strong> Infecciones graves activan la coagulación.</li>"
            "<li><strong>Enfermedad hepática:</strong> Alteración de la síntesis de factores.</li>"
            "<li><strong>Edad avanzada:</strong> El D-Dímero basal aumenta con la edad.</li>"
            "</ul>"
            "<p>Alta sensibilidad, baja especificidad: un resultado normal descarta coágulos en pacientes de bajo riesgo; un resultado elevado no confirma diagnóstico por sí solo.</p>"
        )),
        Section(id="symptoms", level=2, heading="Síntomas de TVP y EP", body_html=(
            "<p><strong>TVP:</strong></p><ul><li>Hinchazón, dolor y enrojecimiento en una pierna</li><li>Calor en la zona afectada</li><li>Dolor en la pantorrilla al caminar</li></ul>"
            "<p><strong>EP:</strong></p><ul><li>Disnea súbita</li><li>Dolor torácico pleurítico</li><li>Taquicardia</li><li>Hemoptisis en algunos pacientes</li><li>Mareo o sensación de desmayo</li></ul>"
            "<p>Estos síntomas requieren atención médica de emergencia. La EP puede ser mortal sin diagnóstico y tratamiento rápidos.</p>"
        )),
        Section(id="related-tests", level=2, heading="Pruebas relacionadas", body_html=(
            "<p>Ante D-Dímero elevado se solicitan:</p><ul>"
            "<li><strong>TP/INR:</strong> Vía extrínseca; monitorización de warfarina.</li>"
            "<li><strong>TTPa:</strong> Vía intrínseca; seguimiento de heparina.</li>"
            "<li><strong>Fibrinógeno:</strong> Puede consumirse en CID.</li>"
            "<li><strong>Recuento plaquetario:</strong> Equilibrio coagulación-sangrado.</li>"
            "<li><strong>Angio-TC pulmonar:</strong> Estándar de oro para EP.</li>"
            "<li><strong>Eco-Doppler venoso:</strong> Detección de TVP.</li></ul>"
            "<p>La interpretación conjunta con escalas de probabilidad clínica (Wells, Ginebra) es esencial.</p>"
        )),
        Section(id="when-to-see-doctor", level=2, heading="¿Cuándo consultar al médico?", body_html=(
            "<p>Busque <strong>atención de emergencia</strong> si:</p><ul><li>Disnea o dolor torácico súbitos</li><li>Hinchazón y dolor repentinos en una pierna</li><li>D-Dímero elevado con estos síntomas</li><li>Hemoptisis o sensación de desmayo</li></ul>"
            "<p>La EP es potencialmente mortal y requiere tratamiento inmediato. La TVP no tratada puede progresar a EP. El tratamiento anticoagulante precoz reduce drásticamente las complicaciones.</p>"
            "<p>Un D-Dímero elevado no es un diagnóstico, pero junto con sospecha clínica obliga a más estudios.</p>"
        )),
        Section(id="how-norya-helps", level=2, heading="Cómo le ayuda NoryaAI con el D-Dímero", body_html=(
            "<p><strong>NoryaAI</strong> analiza su informe completo, incluido el D-Dímero, considerando edad, sexo y contexto clínico. Resaltamos valores fuera de rango y sugerimos preguntas para su médico.</p>"
            "<p><a href=\"/analyze\">Suba su informe</a> para un análisis instantáneo. Visite nuestra <a href=\"/pricing\">página de precios</a>. NoryaAI no sustituye al médico; le ayuda a llegar más informado.</p>"
            "<p>Si su D-Dímero está elevado y tiene síntomas como disnea o hinchazón en una pierna, busque evaluación de emergencia.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Aviso legal", body_html=(
            "<p><strong>Este contenido es informativo y no constituye consejo médico, diagnóstico ni tratamiento.</strong> Consulte sus resultados con un profesional sanitario. NoryaAI no sustituye una consulta médica. "
            '<a href="/analyze">Visite nuestra página de análisis</a> para información preliminar.</p>'
        )),
    ]


# ─────────────────────────────────────────────────────────────────────
# GERMAN
# ─────────────────────────────────────────────────────────────────────
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="D-Dimer-Bluttest: Was Ihre Ergebnisse bedeuten", body_html=(
            "<p>Wenn Ihr Laborbericht einen erhöhten <strong>D-Dimer</strong>-Wert zeigt, fragen Sie sich wahrscheinlich, was dieser Test misst und ob Anlass zur Sorge besteht. D-Dimer ist ein <strong>Fibrin-Abbauprodukt</strong>, das bei der Auflösung von Blutgerinnseln entsteht. Es spielt eine zentrale Rolle bei der Abklärung von tiefer Venenthrombose (TVT) und Lungenembolie (LE).</p>"
            "<p>Dieser Ratgeber erklärt, was der <strong>D-Dimer-Test</strong> misst, welche Referenzwerte gelten, welche Ursachen ein <strong>erhöhtes D-Dimer</strong> haben kann und wann Sie ärztliche Hilfe suchen sollten.</p>"
            "<p>Das D-Dimer besitzt eine hohe <em>Sensitivität</em>, aber niedrige <em>Spezifität</em>: Ein normaler Wert schließt TVT/LE bei Niedrigrisikopatienten weitgehend aus; viele Zustände können ihn jedoch erhöhen.</p>"
        )),
        Section(id="what-is", level=2, heading="Was ist D-Dimer?", body_html=(
            "<p><strong>D-Dimer</strong> ist ein kleines Proteinfragment, das bei der Auflösung eines Fibringerinnsels durch Plasmin entsteht. Bei Aktivierung der Gerinnungskaskade wird Fibrinogen in Fibrinstränge umgewandelt; gleichzeitig löst das fibrinolytische System das Gerinnsel auf und setzt D-Dimer-Fragmente frei.</p>"
            "<p>D-Dimer im Blut zeigt daher an, dass kürzlich sowohl Gerinnselbildung als auch -auflösung stattgefunden hat. Bei Gesunden ist der Spiegel sehr niedrig.</p>"
            "<p>Der Test dient primär dem <strong>Ausschluss</strong> thromboembolischer Erkrankungen. Ein negatives Ergebnis bei niedriger klinischer Wahrscheinlichkeit schließt ein Gerinnsel mit hoher Sicherheit aus; ein positives Ergebnis allein stellt keine Diagnose.</p>"
        )),
        Section(id="normal-ranges", level=2, heading="Normale D-Dimer-Werte", body_html=(
            '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Einheit</th>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Obere Normgrenze</th></tr></thead><tbody>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,5 µg/mL</td></tr>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td></tr></tbody></table>'
            "<p>Für Patienten <strong>über 50 Jahre</strong> kann ein altersadjustierter Grenzwert verwendet werden: <em>Alter &times; 10&nbsp;ng/mL</em> (DDU). Das reduziert unnötige Bildgebung bei erhaltener Sensitivität.</p>"
            "<p>FEU und DDU unterscheiden sich um den Faktor zwei. Vergleichen Sie Ihr Ergebnis immer mit dem Referenzbereich und dem Einheitensystem Ihres Labors.</p>"
        )),
        Section(id="causes", level=2, heading="Ursachen eines erhöhten D-Dimers", body_html=(
            "<p>Zahlreiche Zustände können D-Dimer erhöhen:</p><ul>"
            "<li><strong>TVT:</strong> Blutgerinnsel in den Beinvenen.</li>"
            "<li><strong>Lungenembolie:</strong> Verschleppung eines Gerinnsels in die Lungenarterien.</li>"
            "<li><strong>DIC:</strong> Disseminierte intravasale Gerinnung.</li>"
            "<li><strong>Operation und Trauma:</strong> Gewebeschäden aktivieren die Kaskade.</li>"
            "<li><strong>Schwangerschaft:</strong> Physiologischer Anstieg.</li>"
            "<li><strong>Krebs:</strong> Prokoagulanter Zustand.</li>"
            "<li><strong>Infektionen und Sepsis:</strong> Aktivierung des Gerinnungssystems.</li>"
            "<li><strong>Lebererkrankung:</strong> Gestörte Faktorensynthese.</li>"
            "<li><strong>Alter:</strong> Basaler Anstieg mit zunehmendem Alter.</li></ul>"
            "<p>Hohe Sensitivität, niedrige Spezifität: Ein normaler Wert schließt Gerinnsel bei Niedrigrisikopatienten aus; ein erhöhter Wert allein bestätigt keine Diagnose.</p>"
        )),
        Section(id="symptoms", level=2, heading="Symptome von TVT und LE", body_html=(
            "<p><strong>TVT:</strong></p><ul><li>Schwellung, Schmerz und Rötung meist in einem Bein</li><li>Wärme im betroffenen Bereich</li><li>Wadenschmerz beim Gehen</li></ul>"
            "<p><strong>LE:</strong></p><ul><li>Plötzliche Atemnot</li><li>Brustschmerz (pleuritisch)</li><li>Tachykardie</li><li>Hämoptyse (Bluthusten) bei einigen Patienten</li><li>Schwindel oder Ohnmachtsgefühl</li></ul>"
            "<p>Diese Symptome können lebensbedrohlich sein und erfordern sofortige ärztliche Versorgung.</p>"
        )),
        Section(id="related-tests", level=2, heading="Verwandte Untersuchungen", body_html=(
            "<ul><li><strong>PT/INR:</strong> Extrinsischer Gerinnungsweg; Warfarin-Monitoring.</li>"
            "<li><strong>aPTT:</strong> Intrinsischer Weg; Heparin-Monitoring.</li>"
            "<li><strong>Fibrinogen:</strong> Kann bei DIC verbraucht werden.</li>"
            "<li><strong>Thrombozytenzahl:</strong> Gerinnungs-/Blutungsgleichgewicht.</li>"
            "<li><strong>CT-Pulmonalisangiographie:</strong> Goldstandard bei LE-Verdacht.</li>"
            "<li><strong>Doppler-Ultraschall:</strong> Detektion einer TVT.</li></ul>"
            "<p>Die gemeinsame Interpretation mit klinischen Scores (Wells, Genf) ist entscheidend.</p>"
        )),
        Section(id="when-to-see-doctor", level=2, heading="Wann sollten Sie einen Arzt aufsuchen?", body_html=(
            "<p>Suchen Sie <strong>sofort die Notaufnahme</strong> auf bei:</p><ul><li>Plötzlicher Atemnot oder Brustschmerz</li><li>Plötzlicher Schwellung und Schmerz in einem Bein</li><li>Erhöhtem D-Dimer mit diesen Symptomen</li><li>Bluthusten oder Ohnmachtsgefühl</li></ul>"
            "<p>Eine LE ist lebensbedrohlich und erfordert sofortige Behandlung. Eine unbehandelte TVT kann zu einer LE fortschreiten. Frühzeitige Antikoagulation senkt das Risiko deutlich.</p>"
        )),
        Section(id="how-norya-helps", level=2, heading="Wie NoryaAI bei D-Dimer-Ergebnissen hilft", body_html=(
            "<p><strong>NoryaAI</strong> analysiert Ihren Blutbefund einschließlich D-Dimer. <a href=\"/analyze\">Laden Sie Ihren Bericht hoch</a> für eine sofortige Analyse. Besuchen Sie unsere <a href=\"/pricing\">Preisseite</a>. NoryaAI ersetzt keinen Arzt — wir helfen Ihnen, informiert zu bleiben.</p>"
            "<p>Bei erhöhtem D-Dimer mit Atemnot oder Beinschwellung suchen Sie sofort ärztliche Hilfe.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Haftungsausschluss", body_html=(
            "<p><strong>Dieser Inhalt dient ausschließlich Informationszwecken und stellt keine medizinische Beratung dar.</strong> Besprechen Sie Ihre Ergebnisse mit einer Fachkraft. NoryaAI ersetzt keine ärztliche Konsultation. "
            '<a href="/analyze">Besuchen Sie unsere Analyseseite</a> für erste Einblicke.</p>'
        )),
    ]


# ─────────────────────────────────────────────────────────────────────
# FRENCH
# ─────────────────────────────────────────────────────────────────────
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Analyse des D-Dimères : que signifient vos résultats ?", body_html=(
            "<p>Si votre bilan sanguin révèle un taux élevé de <strong>D-Dimères</strong>, il est naturel de s&rsquo;interroger sur la signification de ce marqueur. Les D-Dimères sont des <strong>produits de dégradation de la fibrine</strong> libérés lors de la dissolution de caillots sanguins. Ils jouent un rôle central dans l&rsquo;évaluation de la thrombose veineuse profonde (TVP) et de l&rsquo;embolie pulmonaire (EP).</p>"
            "<p>Ce guide explique ce que mesure le <strong>dosage des D-Dimères</strong>, les valeurs de référence, les causes d&rsquo;élévation, leur signification clinique et quand consulter. Notre objectif est de vous aider à comprendre vos résultats.</p>"
            "<p>Le test des D-Dimères possède une haute <em>sensibilité</em> mais une faible <em>spécificité</em> : un taux normal peut exclure une TVP/EP chez les patients à faible risque, mais de nombreuses situations peuvent l&rsquo;élever.</p>"
        )),
        Section(id="what-is", level=2, heading="Que sont les D-Dimères ?", body_html=(
            "<p>Les <strong>D-Dimères</strong> sont des fragments protéiques issus de la dégradation de la fibrine par la plasmine. Leur présence indique une activité récente de coagulation et de fibrinolyse. Chez les personnes saines, les taux sont très bas.</p>"
            "<p>Le dosage sert principalement à <strong>exclure</strong> une maladie thromboembolique. Un résultat négatif avec faible probabilité clinique exclut un caillot ; un résultat positif seul ne confirme pas de diagnostic.</p>"
            "<p>Les D-Dimères sont un outil de triage puissant, mais ils doivent toujours être interprétés dans le contexte clinique global.</p>"
        )),
        Section(id="normal-ranges", level=2, heading="Valeurs normales des D-Dimères", body_html=(
            '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Unité</th>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Limite supérieure normale</th></tr></thead><tbody>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,5 µg/mL</td></tr>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td></tr></tbody></table>'
            "<p>Pour les patients de <strong>plus de 50 ans</strong>, un seuil ajusté à l&rsquo;âge peut être utilisé : <em>âge &times; 10&nbsp;ng/mL</em> (DDU). Les unités FEU et DDU diffèrent d&rsquo;un facteur deux environ. Comparez toujours avec l&rsquo;intervalle de votre laboratoire.</p>"
        )),
        Section(id="causes", level=2, heading="Causes d&rsquo;un D-Dimères élevé", body_html=(
            "<p>De nombreuses situations élèvent les D-Dimères :</p><ul>"
            "<li><strong>TVP :</strong> Caillots dans les veines des jambes.</li>"
            "<li><strong>EP :</strong> Migration d&rsquo;un caillot vers les artères pulmonaires.</li>"
            "<li><strong>CIVD :</strong> Coagulation intravasculaire disséminée.</li>"
            "<li><strong>Chirurgie et traumatisme :</strong> Activation de la cascade.</li>"
            "<li><strong>Grossesse :</strong> Élévation physiologique.</li>"
            "<li><strong>Cancer :</strong> État procoagulant.</li>"
            "<li><strong>Infection et sepsis :</strong> Activation de la coagulation.</li>"
            "<li><strong>Hépatopathie :</strong> Déséquilibre de la synthèse des facteurs.</li>"
            "<li><strong>Vieillissement :</strong> Augmentation basale avec l&rsquo;âge.</li></ul>"
            "<p>Haute sensibilité, faible spécificité : un résultat normal exclut les caillots chez les patients à faible risque ; un résultat élevé ne confirme rien seul.</p>"
        )),
        Section(id="symptoms", level=2, heading="Symptômes de TVP et EP", body_html=(
            "<p><strong>TVP :</strong></p><ul><li>Gonflement, douleur et rougeur d&rsquo;une jambe</li><li>Chaleur locale</li><li>Douleur au mollet à la marche</li></ul>"
            "<p><strong>EP :</strong></p><ul><li>Dyspnée brutale</li><li>Douleur thoracique pleurétique</li><li>Tachycardie</li><li>Hémoptysie chez certains patients</li><li>Vertiges ou malaise</li></ul>"
            "<p>Ces symptômes nécessitent une prise en charge urgente. L&rsquo;EP peut être fatale sans traitement rapide.</p>"
        )),
        Section(id="related-tests", level=2, heading="Examens complémentaires", body_html=(
            "<ul><li><strong>TP/INR :</strong> Voie extrinsèque ; suivi des AVK.</li>"
            "<li><strong>TCA :</strong> Voie intrinsèque ; suivi de l&rsquo;héparine.</li>"
            "<li><strong>Fibrinogène :</strong> Peut être consommé dans la CIVD.</li>"
            "<li><strong>Numération plaquettaire :</strong> Équilibre coagulation-saignement.</li>"
            "<li><strong>Angioscanner pulmonaire :</strong> Référence pour l&rsquo;EP.</li>"
            "<li><strong>Écho-Doppler veineux :</strong> Détection de TVP.</li></ul>"
            "<p>L&rsquo;interprétation conjointe avec les scores cliniques (Wells, Genève) est essentielle.</p>"
        )),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter en urgence ?", body_html=(
            "<p>Consultez <strong>immédiatement</strong> si :</p><ul><li>Dyspnée ou douleur thoracique soudaines</li><li>Gonflement brutal d&rsquo;une jambe</li><li>D-Dimères élevés avec ces symptômes</li><li>Hémoptysie ou malaise</li></ul>"
            "<p>L&rsquo;EP est une urgence vitale. La TVP non traitée peut migrer vers les poumons. L&rsquo;anticoagulation précoce réduit drastiquement les complications.</p>"
        )),
        Section(id="how-norya-helps", level=2, heading="Comment NoryaAI vous aide", body_html=(
            "<p><strong>NoryaAI</strong> analyse votre bilan complet, y compris les D-Dimères. <a href=\"/analyze\">Téléchargez votre bilan</a> pour une analyse instantanée. Consultez notre <a href=\"/pricing\">page tarifs</a>. NoryaAI ne remplace pas le médecin.</p>"
            "<p>Si vos D-Dimères sont élevés et que vous avez des symptômes, consultez sans tarder.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Avertissement", body_html=(
            "<p><strong>Ce contenu est informatif et ne constitue pas un avis médical.</strong> Discutez vos résultats avec un professionnel de santé. NoryaAI ne remplace pas une consultation. "
            '<a href="/analyze">Visitez notre page d&rsquo;analyse</a> pour des informations préliminaires.</p>'
        )),
    ]


# ─────────────────────────────────────────────────────────────────────
# ITALIAN
# ─────────────────────────────────────────────────────────────────────
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Esame del D-Dimero: cosa significano i risultati", body_html=(
            "<p>Se il vostro referto mostra un livello elevato di <strong>D-Dimero</strong>, è naturale chiedersi cosa misuri questo test. Il D-Dimero è un <strong>prodotto di degradazione della fibrina</strong> che indica attività di formazione e dissoluzione di coaguli, ed è fondamentale nella valutazione della trombosi venosa profonda (TVP) e dell&rsquo;embolia polmonare (EP).</p>"
            "<p>Questa guida spiega cosa misura il <strong>D-Dimero</strong>, gli intervalli di riferimento, le cause di elevazione e quando consultare il medico.</p>"
            "<p>Il test ha alta <em>sensibilità</em> ma bassa <em>specificità</em>: un valore normale può escludere TVP/EP nei pazienti a basso rischio, ma molte condizioni possono innalzarlo.</p>"
        )),
        Section(id="what-is", level=2, heading="Che cos&rsquo;è il D-Dimero?", body_html=(
            "<p>Il <strong>D-Dimero</strong> è un frammento proteico prodotto dalla degradazione della fibrina ad opera della plasmina. La sua presenza indica attività recente di coagulazione e fibrinolisi. Nei soggetti sani i livelli sono molto bassi.</p>"
            "<p>Il test serve principalmente a <strong>escludere</strong> la malattia tromboembolica. Un risultato negativo con bassa probabilità clinica esclude un coagulo con elevata accuratezza; un risultato positivo da solo non conferma la diagnosi.</p>"
            "<p>Il D-Dimero è uno strumento di triage potente ma va sempre interpretato nel contesto clinico.</p>"
        )),
        Section(id="normal-ranges", level=2, heading="Valori normali del D-Dimero", body_html=(
            '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Unità</th>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Limite superiore normale</th></tr></thead><tbody>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0,5 µg/mL</td></tr>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td></tr></tbody></table>'
            "<p>Per i pazienti <strong>oltre i 50 anni</strong> si può usare un cut-off aggiustato per età: <em>età &times; 10&nbsp;ng/mL</em> (DDU). Le unità FEU e DDU differiscono di un fattore due. Confrontate sempre con il vostro laboratorio.</p>"
        )),
        Section(id="causes", level=2, heading="Cause di D-Dimero alto", body_html=(
            "<p>Molte condizioni possono elevare il D-Dimero:</p><ul>"
            "<li><strong>TVP:</strong> Coaguli nelle vene delle gambe.</li>"
            "<li><strong>EP:</strong> Migrazione del coagulo alle arterie polmonari.</li>"
            "<li><strong>CID:</strong> Coagulazione intravascolare disseminata.</li>"
            "<li><strong>Chirurgia e trauma:</strong> Danno tissutale.</li>"
            "<li><strong>Gravidanza:</strong> Aumento fisiologico.</li>"
            "<li><strong>Cancro:</strong> Stato procoagulante.</li>"
            "<li><strong>Infezione e sepsi:</strong> Attivazione della coagulazione.</li>"
            "<li><strong>Epatopatia:</strong> Alterata sintesi dei fattori.</li>"
            "<li><strong>Età avanzata:</strong> Aumento basale.</li></ul>"
            "<p>Alta sensibilità, bassa specificità: un valore normale esclude coaguli nei pazienti a basso rischio; un valore elevato da solo non conferma nulla.</p>"
        )),
        Section(id="symptoms", level=2, heading="Sintomi di TVP ed EP", body_html=(
            "<p><strong>TVP:</strong></p><ul><li>Gonfiore, dolore e rossore di solito a una gamba</li><li>Calore locale</li><li>Dolore al polpaccio camminando</li></ul>"
            "<p><strong>EP:</strong></p><ul><li>Dispnea improvvisa</li><li>Dolore toracico pleuritico</li><li>Tachicardia</li><li>Emottisi in alcuni pazienti</li><li>Vertigini o sensazione di svenimento</li></ul>"
            "<p>Questi sintomi richiedono assistenza medica d&rsquo;emergenza. L&rsquo;EP può essere fatale senza diagnosi e trattamento tempestivi.</p>"
        )),
        Section(id="related-tests", level=2, heading="Esami correlati", body_html=(
            "<ul><li><strong>PT/INR:</strong> Via estrinseca; monitoraggio warfarin.</li>"
            "<li><strong>aPTT:</strong> Via intrinseca; monitoraggio eparina.</li>"
            "<li><strong>Fibrinogeno:</strong> Può essere consumato nella CID.</li>"
            "<li><strong>Conta piastrinica:</strong> Equilibrio coagulazione-sanguinamento.</li>"
            "<li><strong>Angio-TC polmonare:</strong> Gold standard per EP.</li>"
            "<li><strong>Eco-Doppler venoso:</strong> Rilevamento TVP.</li></ul>"
            "<p>L&rsquo;interpretazione congiunta con gli score clinici (Wells, Ginevra) è essenziale.</p>"
        )),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico?", body_html=(
            "<p>Recatevi al <strong>pronto soccorso</strong> se:</p><ul><li>Dispnea o dolore toracico improvvisi</li><li>Gonfiore improvviso di una gamba</li><li>D-Dimero elevato con questi sintomi</li><li>Emottisi o sensazione di svenimento</li></ul>"
            "<p>L&rsquo;EP è potenzialmente letale. La TVP non trattata può progredire in EP. L&rsquo;anticoagulazione precoce riduce drasticamente le complicanze.</p>"
        )),
        Section(id="how-norya-helps", level=2, heading="Come NoryaAI vi aiuta col D-Dimero", body_html=(
            "<p><strong>NoryaAI</strong> analizza il referto completo, incluso il D-Dimero. <a href=\"/analyze\">Caricate il referto</a> per un&rsquo;analisi istantanea. Visitate la <a href=\"/pricing\">pagina prezzi</a>. NoryaAI non sostituisce il medico.</p>"
            "<p>Se il D-Dimero è elevato e avete sintomi, cercate assistenza immediata.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Avvertenza", body_html=(
            "<p><strong>Contenuto informativo, non consulenza medica.</strong> Discutete i risultati con un professionista. NoryaAI non sostituisce una visita. "
            '<a href="/analyze">Pagina di analisi</a> per informazioni preliminari.</p>'
        )),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="בדיקת D-Dimer בדם: מה המשמעות של התוצאות שלך?", body_html=(
            "<p>אם תוצאות בדיקת הדם שלך מראות רמת <strong>D-Dimer</strong> גבוהה, סביר שתרצו להבין מהו הבדיקה הזו ומה המשמעות. D-Dimer הוא <strong>תוצר פירוק פיברין</strong> — פרגמנט חלבוני קטן המשתחרר כאשר קרישי דם מתפרקים — והוא ממלא תפקיד מרכזי בהערכת פקקת ורידים עמוקים (DVT) ותסחיף ריאתי (PE).</p>"
            "<p>מדריך זה מסביר מה מודדת בדיקת <strong>D-Dimer</strong>, טווחי ייחוס, גורמים לעלייה ומתי לפנות לרופא.</p>"
            "<p>לבדיקה <em>רגישות</em> גבוהה אך <em>סגוליות</em> נמוכה: D-Dimer תקין יכול לשלול DVT/PE בחולים בסיכון נמוך, אך מצבים רבים יכולים להעלות אותו.</p>"
        )),
        Section(id="what-is", level=2, heading="מהו D-Dimer?", body_html=(
            "<p><strong>D-Dimer</strong> הוא פרגמנט חלבוני המיוצר כאשר פלסמין מפרק קריש פיברין. נוכחותו בדם מעידה על פעילות של יצירת קרישים ופירוקם. אצל אנשים בריאים הרמות נמוכות מאוד.</p>"
            "<p>הבדיקה משמשת בעיקר ל<strong>שלילת</strong> מחלה תרומבואמבולית. תוצאה שלילית עם הסתברות קלינית נמוכה שוללת קריש ברמת דיוק גבוהה; תוצאה חיובית לבדה אינה מאשרת אבחנה.</p>"
            "<p>D-Dimer הוא כלי מיון רב עוצמה, אך יש לפרשו תמיד בהקשר הקליני הכולל.</p>"
        )),
        Section(id="normal-ranges", level=2, heading="טווחי ייחוס תקינים של D-Dimer", body_html=(
            '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">יחידה</th>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">גבול עליון תקין</th></tr></thead><tbody>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.5 µg/mL</td></tr>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td></tr></tbody></table>'
            "<p>למטופלים <strong>מעל גיל 50</strong> ניתן להשתמש בסף מותאם גיל: <em>גיל &times; 10&nbsp;ng/mL</em> (DDU). יחידות FEU ו-DDU שונות בפקטור של כ-2. השוו תמיד עם טווח הייחוס של המעבדה שלכם.</p>"
        )),
        Section(id="causes", level=2, heading="גורמים ל-D-Dimer גבוה", body_html=(
            "<p>מצבים רבים יכולים להעלות D-Dimer:</p><ul>"
            "<li><strong>DVT:</strong> קרישי דם בוורידי הרגליים.</li>"
            "<li><strong>PE:</strong> נדידת קריש לעורקי הריאה.</li>"
            "<li><strong>DIC:</strong> קרישה תוך-כלית מפושטת.</li>"
            "<li><strong>ניתוח וטראומה:</strong> נזק רקמתי מפעיל את מפל הקרישה.</li>"
            "<li><strong>הריון:</strong> עלייה פיזיולוגית.</li>"
            "<li><strong>סרטן:</strong> מצב פרו-קרישתי.</li>"
            "<li><strong>זיהום וספסיס:</strong> הפעלת מערכת הקרישה.</li>"
            "<li><strong>מחלת כבד:</strong> חוסר איזון בסינתזת גורמים.</li>"
            "<li><strong>הזדקנות:</strong> עלייה בסיסית עם הגיל.</li></ul>"
            "<p>רגישות גבוהה, סגוליות נמוכה: D-Dimer תקין שולל קרישים בחולים בסיכון נמוך; ערך גבוה לבדו אינו מאשר אבחנה.</p>"
        )),
        Section(id="symptoms", level=2, heading="תסמיני DVT ו-PE", body_html=(
            "<p><strong>DVT:</strong></p><ul><li>נפיחות, כאב ואדמומיות בדרך כלל ברגל אחת</li><li>חום מקומי</li><li>כאב בשוק בהליכה</li></ul>"
            "<p><strong>PE:</strong></p><ul><li>קוצר נשימה פתאומי</li><li>כאב בחזה (פלאוריטי)</li><li>טכיקרדיה</li><li>שיעול דמי בחלק מהמטופלים</li><li>סחרחורת או תחושת עילפון</li></ul>"
            "<p>תסמינים אלה מצריכים טיפול חירום. PE עלול להיות קטלני ללא אבחון וטיפול מהירים.</p>"
        )),
        Section(id="related-tests", level=2, heading="בדיקות קשורות", body_html=(
            "<ul><li><strong>PT/INR:</strong> המסלול החיצוני; מעקב וורפרין.</li>"
            "<li><strong>aPTT:</strong> המסלול הפנימי; מעקב הפרין.</li>"
            "<li><strong>פיברינוגן:</strong> עלול להתכלות ב-DIC.</li>"
            "<li><strong>ספירת טסיות:</strong> איזון קרישה-דימום.</li>"
            "<li><strong>CT אנגיוגרפיה ריאתית:</strong> סטנדרט הזהב ל-PE.</li>"
            "<li><strong>דופלר ורידי:</strong> איתור DVT.</li></ul>"
            "<p>פרשנות משולבת עם ציוני הסתברות קליניים (Wells, ז'נבה) חיונית.</p>"
        )),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא?", body_html=(
            "<p>פנו <strong>מיד למיון</strong> אם:</p><ul><li>קוצר נשימה או כאב בחזה פתאומיים</li><li>נפיחות פתאומית ברגל</li><li>D-Dimer גבוה עם תסמינים אלה</li><li>שיעול דמי או תחושת עילפון</li></ul>"
            "<p>PE הוא מצב מסכן חיים הדורש טיפול מיידי. DVT לא מטופל עלול להתקדם ל-PE. טיפול נוגד קרישה מוקדם מפחית דרמטית את הסיכון.</p>"
        )),
        Section(id="how-norya-helps", level=2, heading="כיצד NoryaAI עוזר עם תוצאות D-Dimer", body_html=(
            "<p><strong>NoryaAI</strong> מנתח את דוח הדם המלא שלכם, כולל D-Dimer. <a href=\"/analyze\">העלו את הדוח</a> לניתוח מיידי. בקרו ב<a href=\"/pricing\">עמוד התמחור</a>. NoryaAI אינו מחליף רופא.</p>"
            "<p>אם ה-D-Dimer גבוה ויש לכם תסמינים, פנו מיד לטיפול רפואי.</p>"
        )),
        Section(id="disclaimer", level=2, heading="הבהרה משפטית", body_html=(
            "<p><strong>תוכן זה למטרות מידע בלבד ואינו ייעוץ רפואי.</strong> דונו בתוצאות עם איש מקצוע. NoryaAI אינו תחליף לייעוץ רפואי. "
            '<a href="/analyze">עמוד הניתוח שלנו</a> לתובנות ראשוניות.</p>'
        )),
    ]


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="D-Dimer ब्लड टेस्ट: आपके रिज़ल्ट्स का क्या मतलब है?", body_html=(
            "<p>अगर आपकी लैब रिपोर्ट में <strong>D-Dimer</strong> का स्तर बढ़ा हुआ दिखाई दे रहा है, तो आप सोच रहे होंगे कि यह टेस्ट क्या मापता है। D-Dimer एक <strong>फ़ाइब्रिन डिग्रेडेशन प्रोडक्ट</strong> है — एक छोटा प्रोटीन फ्रैगमेंट जो रक्त के थक्कों के टूटने पर निकलता है — और यह डीप वेन थ्रोम्बोसिस (DVT) और पल्मोनरी एम्बोलिज़्म (PE) जैसी गंभीर क्लॉटिंग स्थितियों के मूल्यांकन में महत्वपूर्ण भूमिका निभाता है।</p>"
            "<p>यह गाइड बताती है कि <strong>D-Dimer ब्लड टेस्ट</strong> क्या मापता है, सामान्य रेफरेंस रेंज, बढ़े हुए D-Dimer के कारण और कब डॉक्टर से मिलना चाहिए।</p>"
            "<p>D-Dimer टेस्ट की <em>संवेदनशीलता</em> उच्च लेकिन <em>विशिष्टता</em> कम होती है: सामान्य D-Dimer कम जोखिम वाले रोगियों में DVT/PE को काफी हद तक बाहर कर सकता है, लेकिन कई स्थितियां इसे बढ़ा सकती हैं।</p>"
        )),
        Section(id="what-is", level=2, heading="D-Dimer क्या है?", body_html=(
            "<p><strong>D-Dimer</strong> एक छोटा प्रोटीन फ्रैगमेंट है जो प्लास्मिन द्वारा फ़ाइब्रिन क्लॉट के टूटने पर बनता है। रक्त में इसकी उपस्थिति दर्शाती है कि हाल ही में थक्का बनना और थक्का टूटना दोनों हुए हैं। स्वस्थ व्यक्तियों में स्तर बहुत कम होता है।</p>"
            "<p>यह टेस्ट मुख्य रूप से थ्रोम्बोएम्बोलिक बीमारी को <strong>रूल आउट</strong> करने के लिए उपयोग किया जाता है। कम क्लीनिकल संभावना के साथ नेगेटिव D-Dimer क्लॉट को उच्च सटीकता से बाहर करता है; पॉज़िटिव रिज़ल्ट अकेले निदान की पुष्टि नहीं करता।</p>"
            "<p>D-Dimer एक शक्तिशाली ट्रायज टूल है लेकिन इसे हमेशा क्लीनिकल संदर्भ में व्याख्यायित किया जाना चाहिए।</p>"
        )),
        Section(id="normal-ranges", level=2, heading="D-Dimer के सामान्य मान", body_html=(
            '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">यूनिट</th>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य ऊपरी सीमा</th></tr></thead><tbody>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.5 µg/mL</td></tr>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td></tr></tbody></table>'
            "<p><strong>50 वर्ष से अधिक</strong> उम्र के रोगियों के लिए आयु-समायोजित कटऑफ़: <em>आयु &times; 10&nbsp;ng/mL</em> (DDU)। FEU और DDU इकाइयां लगभग दोगुने के अंतर से भिन्न होती हैं। अपनी लैब की रेफरेंस रेंज से तुलना करें।</p>"
        )),
        Section(id="causes", level=2, heading="हाई D-Dimer के कारण", body_html=(
            "<p>कई स्थितियां D-Dimer बढ़ा सकती हैं:</p><ul>"
            "<li><strong>DVT:</strong> पैर की नसों में रक्त के थक्के।</li>"
            "<li><strong>PE:</strong> फेफड़ों की धमनियों में थक्के का प्रवास।</li>"
            "<li><strong>DIC:</strong> व्यापक इंट्रावास्कुलर कोगुलेशन।</li>"
            "<li><strong>सर्जरी और आघात:</strong> ऊतक क्षति कोगुलेशन कैस्केड को सक्रिय करती है।</li>"
            "<li><strong>गर्भावस्था:</strong> शारीरिक वृद्धि।</li>"
            "<li><strong>कैंसर:</strong> प्रोकोगुलेंट अवस्था।</li>"
            "<li><strong>संक्रमण और सेप्सिस:</strong> कोगुलेशन सिस्टम की सक्रियता।</li>"
            "<li><strong>लिवर की बीमारी:</strong> क्लॉटिंग फ़ैक्टर के संश्लेषण में गड़बड़ी।</li>"
            "<li><strong>उम्र बढ़ना:</strong> बेसल D-Dimer उम्र के साथ बढ़ता है।</li></ul>"
            "<p>उच्च संवेदनशीलता, कम विशिष्टता: सामान्य D-Dimer कम जोखिम वाले रोगियों में क्लॉट को बाहर करता है; बढ़ा हुआ D-Dimer अकेले निदान की पुष्टि नहीं करता।</p>"
        )),
        Section(id="symptoms", level=2, heading="DVT और PE के लक्षण", body_html=(
            "<p><strong>DVT:</strong></p><ul><li>आमतौर पर एक पैर में सूजन, दर्द और लालिमा</li><li>प्रभावित क्षेत्र में गर्मी</li><li>चलते समय पिंडली में दर्द</li></ul>"
            "<p><strong>PE:</strong></p><ul><li>अचानक सांस की तकलीफ</li><li>सीने में दर्द (प्लूरिटिक)</li><li>तेज़ हृदय गति</li><li>कुछ रोगियों में खूनी खांसी</li><li>चक्कर या बेहोशी की भावना</li></ul>"
            "<p>ये लक्षण आपातकालीन चिकित्सा की आवश्यकता को दर्शाते हैं। PE बिना निदान और उपचार के घातक हो सकता है।</p>"
        )),
        Section(id="related-tests", level=2, heading="संबंधित जांचें", body_html=(
            "<ul><li><strong>PT/INR:</strong> एक्सट्रिन्सिक पाथवे; वारफ़ेरिन मॉनिटरिंग।</li>"
            "<li><strong>aPTT:</strong> इंट्रिन्सिक पाथवे; हेपरिन मॉनिटरिंग।</li>"
            "<li><strong>फ़ाइब्रिनोजन:</strong> DIC में कम हो सकता है।</li>"
            "<li><strong>प्लेटलेट काउंट:</strong> क्लॉटिंग-ब्लीडिंग बैलेंस।</li>"
            "<li><strong>CT पल्मोनरी एंजियोग्राफी:</strong> PE के लिए गोल्ड स्टैंडर्ड।</li>"
            "<li><strong>डॉपलर अल्ट्रासाउंड:</strong> DVT का पता लगाना।</li></ul>"
            "<p>क्लीनिकल प्रोबेबिलिटी स्कोर (Wells, Geneva) के साथ संयुक्त व्याख्या आवश्यक है।</p>"
        )),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें?", body_html=(
            "<p><strong>तुरंत इमरजेंसी</strong> में जाएं अगर:</p><ul><li>अचानक सांस की तकलीफ या सीने में दर्द</li><li>एक पैर में अचानक सूजन और दर्द</li><li>इन लक्षणों के साथ D-Dimer बढ़ा हुआ</li><li>खूनी खांसी या बेहोशी की भावना</li></ul>"
            "<p>PE जानलेवा है और तत्काल उपचार चाहिए। अनुपचारित DVT PE में बदल सकता है। जल्दी एंटीकोगुलेंट थेरेपी जटिलताओं को नाटकीय रूप से कम करती है।</p>"
        )),
        Section(id="how-norya-helps", level=2, heading="NoryaAI D-Dimer रिज़ल्ट्स में कैसे मदद करता है", body_html=(
            "<p><strong>NoryaAI</strong> आपकी पूरी रिपोर्ट का विश्लेषण करता है, D-Dimer सहित। <a href=\"/analyze\">अपनी लैब रिपोर्ट अपलोड करें</a> तत्काल विश्लेषण के लिए। <a href=\"/pricing\">प्राइसिंग पेज</a> पर प्लान देखें। NoryaAI डॉक्टर का विकल्प नहीं है।</p>"
            "<p>अगर D-Dimer बढ़ा हुआ है और सांस की तकलीफ या पैर में सूजन है, तो तुरंत आपातकालीन मूल्यांकन करवाएं।</p>"
        )),
        Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html=(
            "<p><strong>यह सामग्री केवल सूचनात्मक है और चिकित्सा सलाह नहीं है।</strong> रिज़ल्ट्स योग्य पेशेवर के साथ चर्चा करें। NoryaAI चिकित्सा परामर्श का विकल्प नहीं है। "
            '<a href="/analyze">विश्लेषण पेज</a> पर प्रारंभिक जानकारी पाएं।</p>'
        )),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="تحليل D-Dimer في الدم: ماذا تعني نتائجك؟", body_html=(
            "<p>إذا أظهرت نتائج تحليل الدم مستوى مرتفعاً من <strong>D-Dimer</strong>، فقد تتساءل عما يقيسه هذا التحليل. D-Dimer هو <strong>ناتج تحلل الفيبرين</strong> — جزء بروتيني صغير يُطلق عند تفكك الخثرات — ويلعب دوراً محورياً في تقييم التخثر الوريدي العميق (DVT) والانصمام الرئوي (PE).</p>"
            "<p>يشرح هذا الدليل ما يقيسه <strong>تحليل D-Dimer</strong>، النطاقات المرجعية، أسباب الارتفاع ومتى يجب مراجعة الطبيب.</p>"
            "<p>للتحليل <em>حساسية</em> عالية لكن <em>نوعية</em> منخفضة: D-Dimer طبيعي يستبعد DVT/PE عند المرضى منخفضي الخطورة، لكن حالات كثيرة ترفعه.</p>"
        )),
        Section(id="what-is", level=2, heading="ما هو D-Dimer؟", body_html=(
            "<p><strong>D-Dimer</strong> جزء بروتيني صغير ينتج عن تحلل خثرة الفيبرين بواسطة البلازمين. وجوده يدل على نشاط تخثري وانحلالي حديث. لدى الأصحاء المستويات منخفضة جداً.</p>"
            "<p>يُستخدم التحليل أساساً <strong>لاستبعاد</strong> المرض الخثري الانسدادي. نتيجة سلبية مع احتمال سريري منخفض تستبعد الخثرة بدقة عالية؛ نتيجة إيجابية وحدها لا تؤكد التشخيص.</p>"
            "<p>D-Dimer أداة فرز قوية لكن يجب تفسيره دائماً في السياق السريري.</p>"
        )),
        Section(id="normal-ranges", level=2, heading="المستويات الطبيعية لـ D-Dimer", body_html=(
            '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الوحدة</th>'
            '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الحد الأعلى الطبيعي</th></tr></thead><tbody>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">FEU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 0.5 µg/mL</td></tr>'
            '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">DDU</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 250 ng/mL</td></tr></tbody></table>'
            "<p>للمرضى <strong>فوق 50 عاماً</strong> يمكن استخدام عتبة معدّلة حسب العمر: <em>العمر &times; 10&nbsp;ng/mL</em> (DDU). وحدتا FEU وDDU تختلفان بمعامل اثنين تقريباً. قارن دائماً بنطاق مختبرك.</p>"
        )),
        Section(id="causes", level=2, heading="أسباب ارتفاع D-Dimer", body_html=(
            "<p>حالات عديدة ترفع D-Dimer:</p><ul>"
            "<li><strong>DVT:</strong> خثرات في أوردة الساقين.</li>"
            "<li><strong>PE:</strong> انتقال الخثرة إلى الشرايين الرئوية.</li>"
            "<li><strong>DIC:</strong> تخثر منتشر داخل الأوعية.</li>"
            "<li><strong>الجراحة والإصابات:</strong> تلف الأنسجة ينشط سلسلة التخثر.</li>"
            "<li><strong>الحمل:</strong> ارتفاع فسيولوجي.</li>"
            "<li><strong>السرطان:</strong> حالة تخثرية.</li>"
            "<li><strong>العدوى والإنتان:</strong> تفعيل جهاز التخثر.</li>"
            "<li><strong>مرض كبدي:</strong> اختلال تصنيع العوامل.</li>"
            "<li><strong>التقدم في العمر:</strong> ارتفاع قاعدي مع السن.</li></ul>"
            "<p>حساسية عالية، نوعية منخفضة: D-Dimer طبيعي يستبعد الخثرات عند منخفضي الخطورة؛ ارتفاعه وحده لا يؤكد تشخيصاً.</p>"
        )),
        Section(id="symptoms", level=2, heading="أعراض DVT وPE", body_html=(
            "<p><strong>DVT:</strong></p><ul><li>تورم وألم واحمرار عادة في ساق واحدة</li><li>حرارة موضعية</li><li>ألم في الربلة عند المشي</li></ul>"
            "<p><strong>PE:</strong></p><ul><li>ضيق تنفس مفاجئ</li><li>ألم صدري جنبي</li><li>تسارع ضربات القلب</li><li>نفث دم عند بعض المرضى</li><li>دوار أو شعور بالإغماء</li></ul>"
            "<p>هذه الأعراض تستدعي رعاية طبية طارئة. PE قد يكون مميتاً دون تشخيص وعلاج سريعين.</p>"
        )),
        Section(id="related-tests", level=2, heading="الفحوصات ذات الصلة", body_html=(
            "<ul><li><strong>PT/INR:</strong> المسار الخارجي؛ مراقبة الوارفارين.</li>"
            "<li><strong>aPTT:</strong> المسار الداخلي؛ مراقبة الهيبارين.</li>"
            "<li><strong>الفيبرينوجين:</strong> قد يُستهلك في DIC.</li>"
            "<li><strong>عدد الصفائح:</strong> توازن التخثر والنزف.</li>"
            "<li><strong>التصوير المقطعي الرئوي:</strong> المعيار الذهبي لـ PE.</li>"
            "<li><strong>الدوبلر الوريدي:</strong> كشف DVT.</li></ul>"
            "<p>التفسير المشترك مع مقاييس الاحتمال السريري (ويلز، جنيف) ضروري.</p>"
        )),
        Section(id="when-to-see-doctor", level=2, heading="متى يجب مراجعة الطبيب؟", body_html=(
            "<p>اطلب <strong>رعاية طارئة فوراً</strong> إذا:</p><ul><li>ضيق تنفس أو ألم صدري مفاجئ</li><li>تورم مفاجئ في ساق</li><li>D-Dimer مرتفع مع هذه الأعراض</li><li>نفث دم أو شعور بالإغماء</li></ul>"
            "<p>PE حالة مهددة للحياة تتطلب علاجاً فورياً. DVT غير المعالج قد يتطور إلى PE. منع التخثر المبكر يقلل المضاعفات بشكل كبير.</p>"
        )),
        Section(id="how-norya-helps", level=2, heading="كيف يساعدك NoryaAI مع D-Dimer", body_html=(
            "<p><strong>NoryaAI</strong> يحلل تقريرك الكامل، بما فيه D-Dimer. <a href=\"/analyze\">ارفع تقرير المختبر</a> لتحليل فوري. زر <a href=\"/pricing\">صفحة الأسعار</a>. NoryaAI لا يحل محل الطبيب.</p>"
            "<p>إذا كان D-Dimer مرتفعاً ولديك أعراض كضيق التنفس أو تورم الساق، اطلب تقييماً طارئاً فوراً.</p>"
        )),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية", body_html=(
            "<p><strong>هذا المحتوى إعلامي فقط وليس نصيحة طبية.</strong> ناقش نتائجك مع متخصص مؤهل. NoryaAI ليس بديلاً عن الاستشارة الطبية. "
            '<a href="/analyze">صفحة التحليل</a> لرؤى أولية.</p>'
        )),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_d_dimer_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for D-Dimer article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_d_dimer_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for D-Dimer article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is D-Dimer and what does it measure?",
             "answer": "D-Dimer is a fibrin degradation product — a small protein fragment released when blood clots are broken down. The D-Dimer blood test measures its level to help evaluate whether active clot formation and breakdown is occurring in the body."},
            {"question": "What is a normal D-Dimer level?",
             "answer": "The normal upper limit is typically <0.5 µg/mL (FEU) or <250 ng/mL (DDU). For patients over 50, an age-adjusted cut-off of age × 10 ng/mL (DDU) may be used. Always check which unit your laboratory uses."},
            {"question": "What causes high D-Dimer?",
             "answer": "Common causes include DVT (deep vein thrombosis), PE (pulmonary embolism), DIC, surgery, trauma, pregnancy, cancer, infection/sepsis, liver disease, and ageing. D-Dimer has high sensitivity but low specificity — many conditions can raise it."},
            {"question": "Can a normal D-Dimer rule out blood clots?",
             "answer": "Yes, in low-risk patients. A normal D-Dimer combined with a low clinical probability score (such as the Wells score) can effectively rule out DVT and PE, avoiding unnecessary imaging. However, an elevated D-Dimer alone does not confirm a clot — further imaging is needed."},
        ],
        "tr": [
            {"question": "D-Dimer nedir ve neyi ölçer?",
             "answer": "D-Dimer, kan pıhtılarının parçalanması sırasında ortaya çıkan bir fibrin yıkım ürünüdür. Testteki yükseklik, vücutta aktif pıhtı oluşumu ve yıkımının gerçekleştiğine işaret eder."},
            {"question": "Normal D-Dimer değeri nedir?",
             "answer": "Normal üst sınır genellikle <0,5 µg/mL (FEU) veya <250 ng/mL (DDU) olarak kabul edilir. 50 yaş üstü hastalarda yaşa göre ayarlanmış eşik (yaş × 10 ng/mL) kullanılabilir."},
            {"question": "D-Dimer yüksekliğinin nedenleri nelerdir?",
             "answer": "Sık nedenler DVT, pulmoner emboli, DİK, cerrahi, travma, hamilelik, kanser, enfeksiyon/sepsis, karaciğer hastalığı ve ileri yaştır. D-Dimer duyarlılığı yüksek ancak özgüllüğü düşük bir testtir."},
            {"question": "Normal D-Dimer kan pıhtısını dışlayabilir mi?",
             "answer": "Evet, düşük riskli hastalarda normal D-Dimer, düşük klinik olasılık skoru ile birlikte DVT/PE'yi büyük ölçüde dışlayabilir. Ancak yüksek D-Dimer tek başına tanı koymaz; görüntüleme ile doğrulanması gerekir."},
        ],
        "es": [
            {"question": "¿Qué es el D-Dímero y qué mide?",
             "answer": "El D-Dímero es un producto de degradación de la fibrina que se libera cuando los coágulos sanguíneos se descomponen. El análisis mide su nivel para evaluar si existe formación y destrucción activa de coágulos."},
            {"question": "¿Cuál es un nivel normal de D-Dímero?",
             "answer": "El límite superior normal es <0,5 µg/mL (FEU) o <250 ng/mL (DDU). En mayores de 50 años se puede usar un umbral ajustado: edad × 10 ng/mL (DDU)."},
            {"question": "¿Qué causa un D-Dímero elevado?",
             "answer": "Causas frecuentes: TVP, EP, CID, cirugía, trauma, embarazo, cáncer, infección/sepsis, enfermedad hepática y envejecimiento. Alta sensibilidad, baja especificidad."},
            {"question": "¿Un D-Dímero normal descarta coágulos?",
             "answer": "Sí, en pacientes de bajo riesgo. Un D-Dímero normal con baja probabilidad clínica descarta TVP/EP eficazmente. Un resultado elevado solo no confirma el diagnóstico."},
        ],
        "de": [
            {"question": "Was ist D-Dimer und was misst es?",
             "answer": "D-Dimer ist ein Fibrin-Abbauprodukt, das beim Zerfall von Blutgerinnseln freigesetzt wird. Der Test misst seinen Spiegel, um aktive Gerinnselbildung und -auflösung zu beurteilen."},
            {"question": "Was ist ein normaler D-Dimer-Wert?",
             "answer": "Die obere Normgrenze liegt bei <0,5 µg/mL (FEU) oder <250 ng/mL (DDU). Ab 50 Jahren kann ein altersadjustierter Grenzwert (Alter × 10 ng/mL) verwendet werden."},
            {"question": "Was verursacht erhöhtes D-Dimer?",
             "answer": "Häufige Ursachen: TVT, Lungenembolie, DIC, OP, Trauma, Schwangerschaft, Krebs, Infektionen, Lebererkrankung und Alter. Hohe Sensitivität, niedrige Spezifität."},
            {"question": "Kann ein normales D-Dimer Gerinnsel ausschließen?",
             "answer": "Ja, bei Niedrigrisikopatienten. Ein normales D-Dimer plus niedrige klinische Wahrscheinlichkeit schließt TVT/LE wirksam aus. Ein erhöhter Wert allein bestätigt keine Diagnose."},
        ],
        "fr": [
            {"question": "Qu'est-ce que les D-Dimères et que mesurent-ils ?",
             "answer": "Les D-Dimères sont des produits de dégradation de la fibrine libérés lors de la dissolution des caillots. Le dosage évalue l'activité de coagulation et de fibrinolyse."},
            {"question": "Quel est un taux normal de D-Dimères ?",
             "answer": "La limite supérieure normale est <0,5 µg/mL (FEU) ou <250 ng/mL (DDU). Après 50 ans, un seuil ajusté (âge × 10 ng/mL) peut être utilisé."},
            {"question": "Quelles sont les causes d'un D-Dimères élevé ?",
             "answer": "Causes fréquentes : TVP, EP, CIVD, chirurgie, traumatisme, grossesse, cancer, infection/sepsis, hépatopathie et vieillissement. Haute sensibilité, faible spécificité."},
            {"question": "Un D-Dimères normal peut-il exclure un caillot ?",
             "answer": "Oui, chez les patients à faible risque. Un D-Dimères normal avec faible probabilité clinique exclut efficacement TVP/EP. Un résultat élevé seul ne confirme pas le diagnostic."},
        ],
        "it": [
            {"question": "Che cos'è il D-Dimero e cosa misura?",
             "answer": "Il D-Dimero è un prodotto di degradazione della fibrina rilasciato durante la dissoluzione dei coaguli. Il test misura il suo livello per valutare l'attività di coagulazione e fibrinolisi."},
            {"question": "Qual è un valore normale di D-Dimero?",
             "answer": "Il limite superiore normale è <0,5 µg/mL (FEU) o <250 ng/mL (DDU). Sopra i 50 anni si può usare un cut-off aggiustato: età × 10 ng/mL (DDU)."},
            {"question": "Quali sono le cause di D-Dimero alto?",
             "answer": "Cause comuni: TVP, EP, CID, chirurgia, trauma, gravidanza, cancro, infezione/sepsi, epatopatia e invecchiamento. Alta sensibilità, bassa specificità."},
            {"question": "Un D-Dimero normale può escludere coaguli?",
             "answer": "Sì, nei pazienti a basso rischio. Un D-Dimero normale con bassa probabilità clinica esclude efficacemente TVP/EP. Un risultato elevato da solo non conferma la diagnosi."},
        ],
        "he": [
            {"question": "מהו D-Dimer ומה הוא מודד?",
             "answer": "D-Dimer הוא תוצר פירוק פיברין המשתחרר כאשר קרישי דם מתפרקים. הבדיקה מודדת את רמתו כדי להעריך אם יש פעילות יצירה ופירוק של קרישים."},
            {"question": "מהי רמת D-Dimer תקינה?",
             "answer": "הגבול העליון התקין הוא <0.5 µg/mL (FEU) או <250 ng/mL (DDU). מעל גיל 50 ניתן להשתמש בסף מותאם גיל: גיל × 10 ng/mL (DDU)."},
            {"question": "מה גורם ל-D-Dimer גבוה?",
             "answer": "גורמים שכיחים: DVT, PE, DIC, ניתוח, טראומה, הריון, סרטן, זיהום/ספסיס, מחלת כבד והזדקנות. רגישות גבוהה, סגוליות נמוכה."},
            {"question": "האם D-Dimer תקין יכול לשלול קרישי דם?",
             "answer": "כן, בחולים בסיכון נמוך. D-Dimer תקין בשילוב הסתברות קלינית נמוכה שולל DVT/PE ביעילות. ערך גבוה לבדו אינו מאשר אבחנה."},
        ],
        "hi": [
            {"question": "D-Dimer क्या है और यह क्या मापता है?",
             "answer": "D-Dimer एक फ़ाइब्रिन डिग्रेडेशन प्रोडक्ट है जो रक्त के थक्कों के टूटने पर निकलता है। टेस्ट इसके स्तर को मापता है ताकि सक्रिय क्लॉट बनने और टूटने का मूल्यांकन किया जा सके।"},
            {"question": "सामान्य D-Dimer लेवल क्या है?",
             "answer": "सामान्य ऊपरी सीमा <0.5 µg/mL (FEU) या <250 ng/mL (DDU) है। 50 वर्ष से अधिक उम्र के लिए आयु-समायोजित कटऑफ़: आयु × 10 ng/mL (DDU)।"},
            {"question": "हाई D-Dimer के कारण क्या हैं?",
             "answer": "सामान्य कारण: DVT, PE, DIC, सर्जरी, आघात, गर्भावस्था, कैंसर, संक्रमण/सेप्सिस, लिवर रोग और उम्र बढ़ना। उच्च संवेदनशीलता, कम विशिष्टता।"},
            {"question": "क्या सामान्य D-Dimer ब्लड क्लॉट को रूल आउट कर सकता है?",
             "answer": "हां, कम जोखिम वाले रोगियों में। सामान्य D-Dimer कम क्लीनिकल प्रोबेबिलिटी के साथ DVT/PE को प्रभावी ढंग से बाहर कर सकता है। बढ़ा हुआ D-Dimer अकेले निदान की पुष्टि नहीं करता।"},
        ],
        "ar": [
            {"question": "ما هو D-Dimer وماذا يقيس؟",
             "answer": "D-Dimer ناتج تحلل الفيبرين يُطلق عند تفكك الخثرات. يقيس التحليل مستواه لتقييم نشاط تكوّن الخثرات وتحللها."},
            {"question": "ما هو المستوى الطبيعي لـ D-Dimer؟",
             "answer": "الحد الأعلى الطبيعي <0.5 µg/mL (FEU) أو <250 ng/mL (DDU). فوق 50 عاماً يمكن استخدام عتبة معدّلة: العمر × 10 ng/mL (DDU)."},
            {"question": "ما أسباب ارتفاع D-Dimer؟",
             "answer": "أسباب شائعة: DVT، PE، DIC، جراحة، إصابة، حمل، سرطان، عدوى/إنتان، مرض كبدي وتقدم العمر. حساسية عالية، نوعية منخفضة."},
            {"question": "هل يستبعد D-Dimer الطبيعي الخثرات؟",
             "answer": "نعم، عند المرضى منخفضي الخطورة. D-Dimer طبيعي مع احتمال سريري منخفض يستبعد DVT/PE بفاعلية. الارتفاع وحده لا يؤكد التشخيص."},
        ],
    }
