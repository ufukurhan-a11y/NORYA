# -*- coding: utf-8 -*-
"""
Estradiol (Östrojen / E2) blog article — full body content for all 9 languages.
Used by blog_i18n._article_estradiol().
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
            heading="Estradiol (E2) kan testi nedir ve neden önemlidir?",
            body_html=(
                "<p><strong>Estradiol testi</strong>, vücuttaki en güçlü östrojen formu olan "
                "<strong>E2</strong> hormonunun kan düzeyini ölçen önemli bir laboratuvar "
                "tetkikidir. Östrojen düzeyi kadın sağlığında adet düzeni, kemik yoğunluğu, "
                "kardiyovasküler koruma ve üreme fonksiyonları açısından kritik rol oynar. "
                "<strong>Estradiol kan testi</strong> yalnızca kadınlarda değil, erkeklerde de "
                "hormonal dengeyi değerlendirmek için sıklıkla istenir.</p>"
                "<p>Over, adrenal bezler ve yağ dokusu tarafından üretilen estradiol, "
                "menstrüel döngünün düzenlenmesinde anahtar görev üstlenir. "
                "<strong>Düşük östrojen</strong> seviyesi menopoz, over yetmezliği veya "
                "yeme bozuklukları gibi durumlarla ilişkiliyken, <strong>yüksek östrojen</strong> "
                "endometriozis, polikistik over sendromu (PCOS) veya östrojen üreten tümörlerle "
                "birlikte görülebilir. E2 kan testi sonuçlarınızı doğru yorumlamak, hekiminizle "
                "birlikte sağlığınız hakkında bilinçli kararlar almanıza yardımcı olur.</p>"
                "<p>Bu yazıda <strong>östrojen düzeyi</strong> ile ilgili merak ettiğiniz "
                "soruları yanıtlıyoruz: estradiol normal değerleri nedir, düşük veya yüksek "
                "östrojen belirtileri nelerdir ve hangi durumlarda doktora başvurmalısınız? "
                "Rehberimiz tıbbi bir tanı aracı değildir; amacı sizi bilgilendirmek ve "
                "hekiminizle daha verimli bir görüşme yapmanızı sağlamaktır.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Estradiol normal değerleri: referans aralıkları",
            body_html=(
                "<p><strong>Estradiol normal aralığı</strong> yaş, cinsiyet ve kadınlarda "
                "menstrüel döngünün evresine göre önemli ölçüde değişir. Aşağıdaki tablo "
                "yaygın olarak kabul edilen <strong>E2 kan testi</strong> referans "
                "aralıklarını özetlemektedir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup / Dönem</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadın – Foliküler faz</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadın – Ovülasyon doruk</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadın – Luteal faz</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Postmenopozal kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkek (yetişkin)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7,63 – 42,6</td></tr>'
                "</tbody></table>"
                "<p><strong>Östrojen düzeyi</strong> kadınlarda adet döngüsü boyunca dramatik "
                "biçimde dalgalanır. Foliküler fazda yavaşça yükselen estradiol, ovülasyon "
                "öncesinde zirveye ulaşır ve luteal fazda tekrar düşer. Bu nedenle "
                "<strong>estradiol testi</strong> sonucunuz tek başına değerlendirilmemeli; "
                "döngünüzün hangi gününde alındığı mutlaka dikkate alınmalıdır.</p>"
                "<p>Menopoz sonrası dönemde <strong>östrojen düzeyi</strong> belirgin şekilde "
                "düşer ve genellikle 30 pg/mL&rsquo;nin altında seyreder. Hormon replasman "
                "tedavisi (HRT) alan kadınlarda ise hedef aralık hekimin önerisine göre "
                "belirlenir. Erkeklerde estradiol, testosteronun aromataz enzimi ile "
                "dönüşümünden elde edilir; düzeyi kemik sağlığı ve kardiyovasküler sistem "
                "için önemlidir.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Düşük ve yüksek östrojen nedenleri",
            body_html=(
                "<p><strong>Düşük östrojen</strong> (düşük estradiol) birçok farklı nedene "
                "bağlı olabilir. Aşağıda en sık karşılaşılan durumlar listelenmiştir:</p>"
                "<ul>"
                "<li><strong>Menopoz ve perimenopoz:</strong> Over fonksiyonlarının azalmasıyla "
                "östrojen üretimi fizyolojik olarak düşer.</li>"
                "<li><strong>Prematür over yetmezliği:</strong> 40 yaşından önce overlerin "
                "işlev kaybetmesi düşük E2 düzeyine yol açar.</li>"
                "<li><strong>Hipotalamik amenore:</strong> Aşırı egzersiz, düşük vücut ağırlığı "
                "veya yoğun stres hipotalamus-hipofiz-over eksenini baskılayarak östrojen "
                "seviyesini düşürür.</li>"
                "<li><strong>Hipopitüitarizm:</strong> Hipofiz bezinin yetersiz çalışması "
                "gonadotropin salgılanmasını azaltır ve dolaylı olarak estradiol düşer.</li>"
                "<li><strong>Turner sendromu:</strong> Doğuştan gelen bu genetik durumda "
                "overler normal gelişemez.</li>"
                "</ul>"
                "<p><strong>Yüksek östrojen</strong> (yüksek estradiol) ise şu durumlarda "
                "görülebilir:</p>"
                "<ul>"
                "<li><strong>PCOS (Polikistik Over Sendromu):</strong> Hormonal dengesizlik "
                "nedeniyle östrojen düzeyleri göreceli olarak yüksek kalabilir.</li>"
                "<li><strong>Obezite:</strong> Yağ dokusu aromataz enzimi aracılığıyla ekstra "
                "östrojen üretir ve östrojen düzeyini artırır.</li>"
                "<li><strong>Östrojen üreten tümörler:</strong> Nadir görülen over veya "
                "adrenal tümörler estradiol seviyesini belirgin şekilde yükseltebilir.</li>"
                "<li><strong>Karaciğer hastalıkları:</strong> Karaciğer, östrojeni metabolize "
                "eder; karaciğer yetmezliğinde östrojen birikimi olabilir.</li>"
                "<li><strong>Ekzojen östrojen kullanımı:</strong> Hormon tedavisi, oral "
                "kontraseptifler veya fitoöstrojen içeren takviyeler E2 düzeyini artırabilir.</li>"
                "</ul>"
                "<p>Hem <strong>düşük östrojen</strong> hem de <strong>yüksek östrojen</strong> "
                "belirtileri kişinin yaşam kalitesini önemli ölçüde etkileyebilir. Düşük "
                "östrojen belirtileri arasında sıcak basması, vajinal kuruluk, kemik kaybı ve "
                "ruh hali değişiklikleri yer alırken, yüksek östrojen şişkinlik, göğüs "
                "hassasiyeti, düzensiz kanama ve baş ağrısına neden olabilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p><strong>Estradiol kan testi</strong> sonuçlarınız referans aralığının "
                "dışındaysa veya hormonal dengesizliği düşündüren belirtiler yaşıyorsanız "
                "bir sağlık profesyoneline danışmanız önerilir. Özellikle şu durumlarda "
                "hekime başvurmanız önemlidir:</p>"
                "<ul>"
                "<li>Üç aydan uzun süredir adet görmüyorsanız (amenore)</li>"
                "<li>Düzensiz veya aşırı ağrılı adet döngüleri yaşıyorsanız</li>"
                "<li>Menopoz belirtileri (sıcak basması, gece terlemeleri, uyku bozukluğu) "
                "günlük yaşamınızı olumsuz etkiliyorsa</li>"
                "<li>İnfertilite (kısırlık) araştırması yapılıyorsa</li>"
                "<li>Tüp bebek (IVF) veya yardımcı üreme tedavisi planlıyorsanız</li>"
                "<li>Erkeklerde jinekomasti veya cinsel işlev bozukluğu varsa</li>"
                "</ul>"
                "<p>Hekiminiz <strong>E2 kan testi</strong> sonucunu FSH, LH, progesteron "
                "ve diğer hormonlarla birlikte değerlendirerek altta yatan nedeni belirler. "
                "Gerekirse pelvik ultrason, kemik yoğunluğu ölçümü veya ileri hormonal "
                "testler istenebilir. Tedavi seçenekleri arasında hormon replasman tedavisi, "
                "doğum kontrol hapları, yaşam tarzı değişiklikleri veya altta yatan hastalığın "
                "tedavisi yer alabilir.</p>"
                "<p>Unutmayın: tek bir <strong>estradiol testi</strong> sonucu kesin tanı "
                "koymak için yeterli değildir. Sonuçlarınız klinik bulgularınız, "
                "şikayetleriniz ve diğer laboratuvar testleriyle birlikte bir bütün olarak "
                "değerlendirilmelidir. Bu rehber bilgilendirme amaçlıdır; kendi kendinize "
                "tanı koymak veya tedavi planlamak yerine mutlaka uzman hekiminize "
                "danışmanızı öneriyoruz.</p>"
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
            heading="What is an estradiol test and why does it matter?",
            body_html=(
                "<p>An <strong>estradiol test</strong> (also called an <strong>E2 test</strong>) "
                "measures the level of estradiol in your blood — the most potent form of "
                "estrogen produced primarily by the ovaries. <strong>Estrogen levels</strong> "
                "play a central role in the menstrual cycle, bone health, cardiovascular "
                "protection, and fertility. While the <strong>estradiol blood test</strong> "
                "is most often ordered for women, it is also valuable for evaluating hormonal "
                "balance in men.</p>"
                "<p>Estradiol is synthesised mainly by the ovarian follicles, with smaller "
                "amounts coming from the adrenal glands and adipose tissue. During the "
                "menstrual cycle it drives follicle maturation, endometrial thickening, and "
                "ovulation. <strong>Low estrogen</strong> can signal menopause, ovarian "
                "insufficiency, or hypothalamic amenorrhoea, whereas <strong>high estrogen</strong> "
                "may be linked to PCOS, obesity, or oestrogen-secreting tumours. Understanding "
                "your <strong>estradiol blood test</strong> results empowers you to have a more "
                "informed conversation with your doctor.</p>"
                "<p>In this guide we explain the <strong>estradiol normal range</strong> across "
                "different life stages, common causes of abnormal <strong>estrogen levels</strong>, "
                "symptoms to watch for, and when you should seek medical advice. This article "
                "is educational and does not replace professional medical consultation.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Estradiol normal range: reference values by life stage",
            body_html=(
                "<p>The <strong>estradiol normal range</strong> varies significantly by sex, "
                "age, and — in premenopausal women — by the phase of the menstrual cycle. "
                "The table below summarises commonly accepted reference intervals for the "
                "<strong>E2 test</strong>:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group / Phase</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Female – Follicular phase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Female – Ovulation peak</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Female – Luteal phase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Postmenopausal female</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Adult male</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7.63 – 42.6</td></tr>'
                "</tbody></table>"
                "<p><strong>Estrogen levels</strong> in women fluctuate dramatically throughout "
                "the menstrual cycle. Estradiol rises steadily during the follicular phase, "
                "peaks just before ovulation, and then declines in the luteal phase. Therefore, "
                "your <strong>estradiol test</strong> result must always be interpreted in the "
                "context of the day of your cycle on which the blood was drawn.</p>"
                "<p>After menopause, <strong>estrogen levels</strong> drop markedly and "
                "typically remain below 30 pg/mL. Women on hormone replacement therapy (HRT) "
                "will have target ranges set by their clinician. In men, estradiol is produced "
                "by aromatase conversion of testosterone and is important for bone density and "
                "cardiovascular health.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of low and high estrogen levels",
            body_html=(
                "<p><strong>Low estrogen</strong> (low estradiol) can result from a variety "
                "of conditions. The most common causes include:</p>"
                "<ul>"
                "<li><strong>Menopause and perimenopause:</strong> Ovarian function naturally "
                "declines, leading to reduced oestrogen production.</li>"
                "<li><strong>Premature ovarian insufficiency (POI):</strong> Loss of ovarian "
                "function before age 40 causes persistently low E2 levels.</li>"
                "<li><strong>Hypothalamic amenorrhoea:</strong> Excessive exercise, low body "
                "weight, or severe stress can suppress the hypothalamic-pituitary-ovarian axis "
                "and lower <strong>estrogen levels</strong>.</li>"
                "<li><strong>Hypopituitarism:</strong> Reduced gonadotropin secretion from the "
                "pituitary gland indirectly lowers estradiol.</li>"
                "<li><strong>Turner syndrome:</strong> A congenital condition in which the "
                "ovaries do not develop normally.</li>"
                "</ul>"
                "<p><strong>High estrogen</strong> (elevated estradiol) may occur in the "
                "following situations:</p>"
                "<ul>"
                "<li><strong>PCOS (Polycystic Ovary Syndrome):</strong> Hormonal imbalance "
                "can keep <strong>estrogen levels</strong> relatively elevated.</li>"
                "<li><strong>Obesity:</strong> Adipose tissue produces extra oestrogen via "
                "the aromatase enzyme.</li>"
                "<li><strong>Oestrogen-secreting tumours:</strong> Rare ovarian or adrenal "
                "tumours can markedly raise estradiol.</li>"
                "<li><strong>Liver disease:</strong> The liver metabolises oestrogen; impaired "
                "liver function can lead to accumulation.</li>"
                "<li><strong>Exogenous oestrogen:</strong> HRT, oral contraceptives, or "
                "phytoestrogen supplements can elevate E2 levels.</li>"
                "</ul>"
                "<p>Symptoms of <strong>low estrogen</strong> include hot flushes, vaginal "
                "dryness, bone loss, mood swings, and fatigue. Symptoms of <strong>high "
                "estrogen</strong> may include bloating, breast tenderness, irregular bleeding, "
                "headaches, and weight gain. Recognising these signs and discussing them with "
                "your healthcare provider can lead to earlier diagnosis and treatment.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your <strong>estradiol blood test</strong> result falls outside the "
                "reference range or you are experiencing symptoms suggestive of hormonal "
                "imbalance, you should consult a healthcare professional. Consider seeking "
                "medical advice in the following situations:</p>"
                "<ul>"
                "<li>You have missed your period for three or more consecutive months (amenorrhoea)</li>"
                "<li>You experience irregular or unusually painful menstrual cycles</li>"
                "<li>Menopausal symptoms such as hot flushes, night sweats, or sleep disturbance "
                "are significantly affecting your quality of life</li>"
                "<li>You are undergoing a fertility evaluation or planning assisted reproduction "
                "(IVF)</li>"
                "<li>Men experiencing gynaecomastia or sexual dysfunction</li>"
                "</ul>"
                "<p>Your doctor will typically evaluate your <strong>E2 test</strong> result "
                "alongside FSH, LH, progesterone, and other hormones to identify the underlying "
                "cause. Additional investigations may include pelvic ultrasound, bone density "
                "scans, or advanced hormonal panels. Treatment options range from hormone "
                "replacement therapy and oral contraceptives to lifestyle modifications or "
                "management of the underlying condition.</p>"
                "<p>Remember: a single <strong>estradiol test</strong> result is not sufficient "
                "for a definitive diagnosis. Your results should be interpreted alongside your "
                "clinical history, symptoms, and other laboratory findings. This guide is for "
                "informational purposes only — always consult your physician before making "
                "decisions about your health.</p>"
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
            heading="¿Qué es la prueba de estradiol y por qué es importante?",
            body_html=(
                "<p>La <strong>prueba de estradiol</strong> mide el nivel sanguíneo de "
                "estradiol (E2), la forma más potente de estrógeno producida principalmente "
                "por los ovarios. Los <strong>niveles de estradiol</strong> desempeñan un "
                "papel fundamental en el ciclo menstrual, la salud ósea, la protección "
                "cardiovascular y la fertilidad. Aunque el <strong>análisis de estradiol</strong> "
                "se solicita con mayor frecuencia en mujeres, también es útil para evaluar "
                "el equilibrio hormonal en hombres.</p>"
                "<p>El estradiol es sintetizado principalmente por los folículos ováricos, con "
                "cantidades menores procedentes de las glándulas suprarrenales y el tejido "
                "adiposo. Un <strong>estrógeno bajo</strong> puede indicar menopausia, "
                "insuficiencia ovárica o amenorrea hipotalámica, mientras que un "
                "<strong>estrógeno alto</strong> puede estar asociado al síndrome de ovario "
                "poliquístico (SOP), la obesidad o tumores secretores de estrógeno.</p>"
                "<p>En esta guía explicamos los rangos normales de estradiol según la etapa de "
                "la vida, las causas frecuentes de <strong>niveles de estradiol</strong> "
                "anormales, los síntomas a tener en cuenta y cuándo consultar al médico. Este "
                "artículo es educativo y no sustituye la consulta médica profesional.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de estradiol: rangos de referencia",
            body_html=(
                "<p>El rango normal de estradiol varía según el sexo, la edad y, en mujeres "
                "premenopáusicas, la fase del ciclo menstrual. La siguiente tabla resume los "
                "intervalos de referencia comúnmente aceptados para la <strong>prueba de "
                "estradiol</strong>:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo / Fase</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujer – Fase folicular</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujer – Pico ovulatorio</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujer – Fase lútea</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujer posmenopáusica</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombre adulto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7,63 – 42,6</td></tr>'
                "</tbody></table>"
                "<p>Los <strong>niveles de estradiol</strong> en mujeres fluctúan de forma "
                "notable a lo largo del ciclo menstrual. El estradiol sube durante la fase "
                "folicular, alcanza su máximo justo antes de la ovulación y luego desciende en "
                "la fase lútea. Por ello, el resultado de la <strong>prueba de estradiol</strong> "
                "siempre debe interpretarse teniendo en cuenta el día del ciclo en que se "
                "extrajo la muestra.</p>"
                "<p>Tras la menopausia, los <strong>niveles de estradiol</strong> descienden "
                "marcadamente y suelen mantenerse por debajo de 30 pg/mL. En hombres, el "
                "estradiol se produce por conversión de la testosterona mediante la enzima "
                "aromatasa y es importante para la salud ósea y cardiovascular.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de estrógeno bajo y estrógeno alto",
            body_html=(
                "<p>Un <strong>estrógeno bajo</strong> (estradiol bajo) puede deberse a "
                "diversas causas. Las más frecuentes son:</p>"
                "<ul>"
                "<li><strong>Menopausia y perimenopausia:</strong> La función ovárica "
                "disminuye de forma natural, reduciendo la producción de estrógeno.</li>"
                "<li><strong>Insuficiencia ovárica prematura:</strong> La pérdida de función "
                "ovárica antes de los 40 años provoca niveles persistentemente bajos de E2.</li>"
                "<li><strong>Amenorrea hipotalámica:</strong> El ejercicio excesivo, el bajo "
                "peso corporal o el estrés intenso suprimen el eje hipotálamo-hipófisis-ovario.</li>"
                "<li><strong>Hipopituitarismo:</strong> La secreción reducida de gonadotropinas "
                "disminuye indirectamente el estradiol.</li>"
                "<li><strong>Síndrome de Turner:</strong> Afección genética congénita en la que "
                "los ovarios no se desarrollan normalmente.</li>"
                "</ul>"
                "<p>Un <strong>estrógeno alto</strong> (estradiol elevado) puede aparecer en "
                "las siguientes situaciones:</p>"
                "<ul>"
                "<li><strong>SOP (Síndrome de Ovario Poliquístico):</strong> El desequilibrio "
                "hormonal puede mantener los <strong>niveles de estradiol</strong> relativamente "
                "elevados.</li>"
                "<li><strong>Obesidad:</strong> El tejido adiposo produce estrógeno adicional "
                "mediante la enzima aromatasa.</li>"
                "<li><strong>Tumores secretores de estrógeno:</strong> Tumores ováricos o "
                "suprarrenales poco frecuentes pueden elevar notablemente el estradiol.</li>"
                "<li><strong>Enfermedades hepáticas:</strong> El hígado metaboliza el estrógeno; "
                "la insuficiencia hepática puede causar acumulación.</li>"
                "<li><strong>Estrógeno exógeno:</strong> La terapia hormonal, los anticonceptivos "
                "orales o los suplementos con fitoestrógenos pueden elevar el E2.</li>"
                "</ul>"
                "<p>Los síntomas de <strong>estrógeno bajo</strong> incluyen sofocos, sequedad "
                "vaginal, pérdida ósea, cambios de humor y fatiga. Los síntomas de "
                "<strong>estrógeno alto</strong> pueden incluir hinchazón, sensibilidad mamaria, "
                "sangrado irregular, cefaleas y aumento de peso.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Si el resultado de su <strong>prueba de estradiol</strong> se encuentra "
                "fuera del rango de referencia o presenta síntomas que sugieran un desequilibrio "
                "hormonal, le recomendamos consultar a un profesional de la salud. Considere "
                "buscar atención médica en las siguientes situaciones:</p>"
                "<ul>"
                "<li>Ausencia de menstruación durante tres meses o más (amenorrea)</li>"
                "<li>Ciclos menstruales irregulares o excesivamente dolorosos</li>"
                "<li>Síntomas menopáusicos (sofocos, sudoración nocturna, insomnio) que afectan "
                "significativamente su calidad de vida</li>"
                "<li>Evaluación de fertilidad o planificación de reproducción asistida (FIV)</li>"
                "<li>Hombres con ginecomastia o disfunción sexual</li>"
                "</ul>"
                "<p>Su médico evaluará el resultado del análisis de estradiol junto con FSH, "
                "LH, progesterona y otras hormonas para identificar la causa subyacente. "
                "Entre las opciones de tratamiento se encuentran la terapia hormonal "
                "sustitutiva, los anticonceptivos orales, cambios en el estilo de vida o el "
                "tratamiento de la afección de base.</p>"
                "<p>Recuerde: un único resultado de la <strong>prueba de estradiol</strong> no "
                "es suficiente para un diagnóstico definitivo. Sus resultados deben interpretarse "
                "junto con su historial clínico, sus síntomas y otros hallazgos de laboratorio. "
                "Esta guía es meramente informativa; consulte siempre a su médico.</p>"
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
            heading="Was ist ein Östradiol-Test und warum ist er wichtig?",
            body_html=(
                "<p>Der <strong>Östradiol-Test</strong> (auch <strong>E2-Test</strong> genannt) "
                "misst den Blutspiegel von Östradiol — der wirksamsten Form des Östrogens, die "
                "hauptsächlich von den Eierstöcken produziert wird. Der "
                "<strong>Östrogenspiegel</strong> spielt eine zentrale Rolle für den "
                "Menstruationszyklus, die Knochengesundheit, den kardiovaskulären Schutz und "
                "die Fruchtbarkeit. Der <strong>Östradiol-Bluttest</strong> wird nicht nur bei "
                "Frauen, sondern auch bei Männern zur Beurteilung des Hormonhaushalts "
                "eingesetzt.</p>"
                "<p>Östradiol wird vorwiegend von den Eierstockfollikeln synthetisiert, kleinere "
                "Mengen stammen aus den Nebennieren und dem Fettgewebe. Ein <strong>niedriger "
                "Östrogenspiegel</strong> kann auf Menopause, Ovarialinsuffizienz oder "
                "hypothalamische Amenorrhö hinweisen, während ein <strong>hoher "
                "Östrogenspiegel</strong> mit PCOS, Adipositas oder östrogenbildenden Tumoren "
                "assoziiert sein kann.</p>"
                "<p>In diesem Ratgeber erklären wir die Östradiol-Normwerte nach Lebensphase, "
                "häufige Ursachen abweichender <strong>Östrogenspiegel</strong>, Symptome und "
                "wann Sie ärztlichen Rat suchen sollten. Dieser Artikel dient der Aufklärung "
                "und ersetzt keine ärztliche Beratung.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Östradiol-Normalwerte: Referenzbereiche nach Lebensphase",
            body_html=(
                "<p>Der normale <strong>Östradiol-Wert</strong> variiert je nach Geschlecht, "
                "Alter und bei prämenopausalen Frauen je nach Phase des Menstruationszyklus. "
                "Die folgende Tabelle fasst die gängigen Referenzbereiche für den "
                "<strong>Östradiol-Test</strong> zusammen:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe / Phase</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frau – Follikelphase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frau – Ovulationsgipfel</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frau – Lutealphase</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Postmenopausale Frau</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erwachsener Mann</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7,63 – 42,6</td></tr>'
                "</tbody></table>"
                "<p>Der <strong>Östrogenspiegel</strong> bei Frauen schwankt im Verlauf des "
                "Menstruationszyklus erheblich. Östradiol steigt in der Follikelphase an, "
                "erreicht kurz vor dem Eisprung seinen Höhepunkt und sinkt in der Lutealphase "
                "wieder ab. Daher muss das Ergebnis des <strong>Östradiol-Tests</strong> immer "
                "im Kontext des Zyklustages interpretiert werden.</p>"
                "<p>Nach der Menopause sinkt der <strong>Östrogenspiegel</strong> deutlich und "
                "liegt in der Regel unter 30 pg/mL. Bei Männern entsteht Östradiol durch die "
                "Aromatase-Umwandlung von Testosteron und ist für Knochengesundheit und das "
                "Herz-Kreislauf-System relevant.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für niedrigen und hohen Östrogenspiegel",
            body_html=(
                "<p>Ein <strong>niedriger Östrogenspiegel</strong> (niedriges Östradiol) kann "
                "verschiedene Ursachen haben. Zu den häufigsten gehören:</p>"
                "<ul>"
                "<li><strong>Menopause und Perimenopause:</strong> Die Eierstockfunktion nimmt "
                "auf natürliche Weise ab, die Östrogenproduktion sinkt.</li>"
                "<li><strong>Prämature Ovarialinsuffizienz (POI):</strong> Verlust der "
                "Eierstockfunktion vor dem 40. Lebensjahr führt zu dauerhaft niedrigen "
                "E2-Werten.</li>"
                "<li><strong>Hypothalamische Amenorrhö:</strong> Übermäßiger Sport, "
                "Untergewicht oder starker Stress unterdrücken die Hypothalamus-Hypophysen-"
                "Ovarial-Achse.</li>"
                "<li><strong>Hypopituitarismus:</strong> Verminderte Gonadotropin-Ausschüttung "
                "der Hypophyse senkt indirekt Östradiol.</li>"
                "<li><strong>Turner-Syndrom:</strong> Eine angeborene genetische Erkrankung, bei "
                "der sich die Eierstöcke nicht normal entwickeln.</li>"
                "</ul>"
                "<p>Ein <strong>hoher Östrogenspiegel</strong> (erhöhtes Östradiol) kann in "
                "folgenden Situationen auftreten:</p>"
                "<ul>"
                "<li><strong>PCOS (Polyzystisches Ovarialsyndrom):</strong> Hormonelles "
                "Ungleichgewicht hält den <strong>Östrogenspiegel</strong> relativ hoch.</li>"
                "<li><strong>Adipositas:</strong> Fettgewebe produziert über das Enzym "
                "Aromatase zusätzliches Östrogen.</li>"
                "<li><strong>Östrogenbildende Tumoren:</strong> Seltene Eierstock- oder "
                "Nebennierentumoren können Östradiol deutlich erhöhen.</li>"
                "<li><strong>Lebererkrankungen:</strong> Die Leber metabolisiert Östrogen; bei "
                "Leberfunktionsstörungen kann es zur Akkumulation kommen.</li>"
                "<li><strong>Exogene Östrogenzufuhr:</strong> Hormonersatztherapie, orale "
                "Kontrazeptiva oder Phytoöstrogen-Präparate können E2 erhöhen.</li>"
                "</ul>"
                "<p>Symptome eines <strong>niedrigen Östrogenspiegels</strong> umfassen "
                "Hitzewallungen, Scheidentrockenheit, Knochenschwund, Stimmungsschwankungen und "
                "Müdigkeit. Symptome eines <strong>hohen Östrogenspiegels</strong> können "
                "Blähungen, Brustspannen, unregelmäßige Blutungen, Kopfschmerzen und "
                "Gewichtszunahme sein.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie eine Ärztin oder einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Ihr <strong>Östradiol-Bluttest</strong>-Ergebnis außerhalb des "
                "Referenzbereichs liegt oder Sie Symptome haben, die auf ein hormonelles "
                "Ungleichgewicht hindeuten, sollten Sie ärztlichen Rat einholen. Suchen Sie "
                "insbesondere in folgenden Situationen eine Ärztin oder einen Arzt auf:</p>"
                "<ul>"
                "<li>Ausbleiben der Periode seit drei oder mehr Monaten (Amenorrhö)</li>"
                "<li>Unregelmäßige oder ungewöhnlich schmerzhafte Menstruationszyklen</li>"
                "<li>Menopause-Symptome (Hitzewallungen, Nachtschweiß, Schlafstörungen), die "
                "Ihre Lebensqualität erheblich beeinträchtigen</li>"
                "<li>Kinderwunschabklärung oder geplante assistierte Reproduktion (IVF)</li>"
                "<li>Gynäkomastie oder sexuelle Funktionsstörungen bei Männern</li>"
                "</ul>"
                "<p>Ihre Ärztin oder Ihr Arzt wird das Ergebnis des <strong>E2-Tests</strong> "
                "zusammen mit FSH, LH, Progesteron und weiteren Hormonen bewerten, um die "
                "zugrunde liegende Ursache zu ermitteln. Behandlungsmöglichkeiten reichen von "
                "Hormonersatztherapie und oralen Kontrazeptiva über Lebensstiländerungen bis "
                "zur Therapie der Grunderkrankung.</p>"
                "<p>Bedenken Sie: Ein einzelnes Ergebnis des <strong>Östradiol-Tests</strong> "
                "reicht für eine definitive Diagnose nicht aus. Ihre Werte sollten zusammen mit "
                "Ihrer Krankengeschichte, Ihren Beschwerden und anderen Laborergebnissen "
                "beurteilt werden. Dieser Ratgeber dient der Information — konsultieren Sie "
                "immer Ihre Ärztin oder Ihren Arzt.</p>"
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
            heading="Qu'est-ce que le test d'œstradiol et pourquoi est-il important ?",
            body_html=(
                "<p>Le <strong>test d'œstradiol</strong> (également appelé <strong>test E2"
                "</strong>) mesure le taux sanguin d'œstradiol, la forme la plus active "
                "d'œstrogène produite principalement par les ovaires. Le <strong>taux "
                "d'œstradiol</strong> joue un rôle essentiel dans le cycle menstruel, la santé "
                "osseuse, la protection cardiovasculaire et la fertilité. Bien que le "
                "<strong>dosage de l'œstradiol</strong> soit le plus souvent prescrit chez les "
                "femmes, il est également utile pour évaluer l'équilibre hormonal chez les "
                "hommes.</p>"
                "<p>L'œstradiol est principalement synthétisé par les follicules ovariens, avec "
                "de petites quantités provenant des glandes surrénales et du tissu adipeux. "
                "Un <strong>œstrogène bas</strong> peut indiquer une ménopause, une "
                "insuffisance ovarienne ou une aménorrhée hypothalamique, tandis qu'un "
                "<strong>œstrogène élevé</strong> peut être associé au SOPK, à l'obésité ou "
                "à des tumeurs sécrétant de l'œstrogène.</p>"
                "<p>Dans ce guide, nous expliquons les valeurs normales d'œstradiol selon "
                "l'étape de vie, les causes fréquentes de <strong>taux d'œstradiol</strong> "
                "anormaux, les symptômes à surveiller et quand consulter un médecin. Cet "
                "article est éducatif et ne remplace pas une consultation médicale.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales d'œstradiol : intervalles de référence",
            body_html=(
                "<p>Le <strong>taux normal d'œstradiol</strong> varie considérablement selon "
                "le sexe, l'âge et, chez les femmes non ménopausées, la phase du cycle "
                "menstruel. Le tableau ci-dessous résume les intervalles de référence courants "
                "pour le <strong>test d'œstradiol</strong> :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe / Phase</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervalle normal (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femme – Phase folliculaire</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femme – Pic ovulatoire</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femme – Phase lutéale</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femme ménopausée</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Homme adulte</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7,63 – 42,6</td></tr>'
                "</tbody></table>"
                "<p>Les <strong>taux d'œstradiol</strong> chez la femme fluctuent de manière "
                "importante tout au long du cycle menstruel. L'œstradiol augmente pendant la "
                "phase folliculaire, atteint son pic juste avant l'ovulation, puis redescend "
                "en phase lutéale. Le résultat du <strong>test d'œstradiol</strong> doit "
                "toujours être interprété en tenant compte du jour du cycle auquel le "
                "prélèvement a été effectué.</p>"
                "<p>Après la ménopause, le <strong>taux d'œstradiol</strong> chute nettement "
                "et reste généralement en dessous de 30 pg/mL. Chez l'homme, l'œstradiol est "
                "produit par conversion de la testostérone via l'enzyme aromatase et contribue "
                "à la santé osseuse et cardiovasculaire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un œstrogène bas et d'un œstrogène élevé",
            body_html=(
                "<p>Un <strong>œstrogène bas</strong> (œstradiol bas) peut résulter de "
                "diverses situations. Les causes les plus fréquentes sont :</p>"
                "<ul>"
                "<li><strong>Ménopause et périménopause :</strong> La fonction ovarienne "
                "décline naturellement, entraînant une baisse de la production d'œstrogène.</li>"
                "<li><strong>Insuffisance ovarienne prématurée (IOP) :</strong> Perte de la "
                "fonction ovarienne avant 40 ans, provoquant un taux d'E2 durablement bas.</li>"
                "<li><strong>Aménorrhée hypothalamique :</strong> Exercice excessif, faible "
                "poids corporel ou stress intense supprimant l'axe hypothalamo-hypophyso-"
                "ovarien.</li>"
                "<li><strong>Hypopituitarisme :</strong> Diminution de la sécrétion de "
                "gonadotrophines abaissant indirectement l'œstradiol.</li>"
                "<li><strong>Syndrome de Turner :</strong> Affection génétique congénitale "
                "empêchant le développement normal des ovaires.</li>"
                "</ul>"
                "<p>Un <strong>œstrogène élevé</strong> (œstradiol élevé) peut survenir dans "
                "les situations suivantes :</p>"
                "<ul>"
                "<li><strong>SOPK (Syndrome des Ovaires Polykystiques) :</strong> Le "
                "déséquilibre hormonal peut maintenir le <strong>taux d'œstradiol</strong> "
                "relativement élevé.</li>"
                "<li><strong>Obésité :</strong> Le tissu adipeux produit de l'œstrogène "
                "supplémentaire via l'enzyme aromatase.</li>"
                "<li><strong>Tumeurs sécrétant de l'œstrogène :</strong> Des tumeurs ovariennes "
                "ou surrénaliennes rares peuvent nettement augmenter l'œstradiol.</li>"
                "<li><strong>Maladies hépatiques :</strong> Le foie métabolise l'œstrogène ; "
                "une insuffisance hépatique peut entraîner une accumulation.</li>"
                "<li><strong>Œstrogène exogène :</strong> THS, contraceptifs oraux ou "
                "compléments de phyto-œstrogènes peuvent élever le taux d'E2.</li>"
                "</ul>"
                "<p>Les symptômes d'un <strong>œstrogène bas</strong> incluent bouffées de "
                "chaleur, sécheresse vaginale, perte osseuse, sautes d'humeur et fatigue. "
                "Les symptômes d'un <strong>œstrogène élevé</strong> peuvent inclure "
                "ballonnements, tension mammaire, saignements irréguliers, maux de tête et "
                "prise de poids.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si le résultat de votre <strong>test d'œstradiol</strong> se situe en "
                "dehors de l'intervalle de référence ou si vous présentez des symptômes "
                "évocateurs d'un déséquilibre hormonal, il est recommandé de consulter un "
                "professionnel de santé. Consultez notamment dans les situations suivantes :</p>"
                "<ul>"
                "<li>Absence de règles depuis trois mois ou plus (aménorrhée)</li>"
                "<li>Cycles menstruels irréguliers ou anormalement douloureux</li>"
                "<li>Symptômes ménopausiques (bouffées de chaleur, sueurs nocturnes, troubles "
                "du sommeil) affectant significativement votre qualité de vie</li>"
                "<li>Bilan de fertilité ou projet de procréation médicalement assistée (FIV)</li>"
                "<li>Gynécomastie ou dysfonction sexuelle chez l'homme</li>"
                "</ul>"
                "<p>Votre médecin évaluera le résultat du <strong>dosage de l'œstradiol</strong> "
                "en parallèle de la FSH, la LH, la progestérone et d'autres hormones pour "
                "identifier la cause sous-jacente. Les options thérapeutiques incluent le "
                "traitement hormonal substitutif, les contraceptifs oraux, des modifications "
                "du mode de vie ou le traitement de la pathologie causale.</p>"
                "<p>Rappelez-vous : un seul résultat de <strong>test d'œstradiol</strong> ne "
                "suffit pas à poser un diagnostic définitif. Vos résultats doivent être "
                "interprétés en regard de vos antécédents, de vos symptômes et de vos autres "
                "examens biologiques. Ce guide est à visée informative — consultez toujours "
                "votre médecin.</p>"
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
            heading="Cos'è il test dell'estradiolo e perché è importante?",
            body_html=(
                "<p>Il <strong>test dell'estradiolo</strong> (noto anche come <strong>test "
                "E2</strong>) misura il livello ematico di estradiolo, la forma più potente "
                "di estrogeno prodotta principalmente dalle ovaie. I <strong>livelli di "
                "estradiolo</strong> svolgono un ruolo centrale nel ciclo mestruale, nella "
                "salute ossea, nella protezione cardiovascolare e nella fertilità. Sebbene "
                "l'esame venga prescritto più frequentemente alle donne, è utile anche per "
                "valutare l'equilibrio ormonale nell'uomo.</p>"
                "<p>L'estradiolo è sintetizzato principalmente dai follicoli ovarici, con "
                "quantità minori provenienti dalle ghiandole surrenali e dal tessuto adiposo. "
                "<strong>Estrogeni bassi</strong> possono indicare menopausa, insufficienza "
                "ovarica o amenorrea ipotalamica, mentre <strong>estrogeni alti</strong> possono "
                "essere associati a PCOS, obesità o tumori estrogeno-secernenti.</p>"
                "<p>In questa guida spieghiamo i valori normali di estradiolo per fascia d'età, "
                "le cause più comuni di <strong>livelli di estradiolo</strong> anomali, i "
                "sintomi da osservare e quando rivolgersi al medico. Questo articolo ha "
                "finalità educativa e non sostituisce il consulto medico professionale.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di estradiolo: intervalli di riferimento",
            body_html=(
                "<p>L'intervallo normale dell'estradiolo varia significativamente in base al "
                "sesso, all'età e, nelle donne in età fertile, alla fase del ciclo mestruale. "
                "La tabella seguente riassume gli intervalli di riferimento comunemente "
                "accettati per il <strong>test dell'estradiolo</strong>:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo / Fase</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donna – Fase follicolare</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12,5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donna – Picco ovulatorio</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donna – Fase luteale</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donna in menopausa</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54,7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomo adulto</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7,63 – 42,6</td></tr>'
                "</tbody></table>"
                "<p>I <strong>livelli di estradiolo</strong> nelle donne fluttuano notevolmente "
                "durante il ciclo mestruale. L'estradiolo sale nella fase follicolare, raggiunge "
                "il picco poco prima dell'ovulazione e poi scende nella fase luteale. Pertanto "
                "il risultato del <strong>test dell'estradiolo</strong> va sempre interpretato "
                "considerando il giorno del ciclo in cui è stato effettuato il prelievo.</p>"
                "<p>Dopo la menopausa, i <strong>livelli di estradiolo</strong> calano "
                "marcatamente e in genere restano sotto i 30 pg/mL. Nell'uomo, l'estradiolo è "
                "prodotto dalla conversione del testosterone tramite l'enzima aromatasi ed è "
                "importante per la salute ossea e cardiovascolare.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di estrogeni bassi ed estrogeni alti",
            body_html=(
                "<p><strong>Estrogeni bassi</strong> (estradiolo basso) possono derivare da "
                "diverse condizioni. Le cause più comuni includono:</p>"
                "<ul>"
                "<li><strong>Menopausa e perimenopausa:</strong> La funzione ovarica diminuisce "
                "naturalmente, riducendo la produzione di estrogeno.</li>"
                "<li><strong>Insufficienza ovarica prematura (POI):</strong> Perdita della "
                "funzione ovarica prima dei 40 anni con livelli di E2 persistentemente bassi.</li>"
                "<li><strong>Amenorrea ipotalamica:</strong> Esercizio eccessivo, basso peso "
                "corporeo o stress severo sopprimono l'asse ipotalamo-ipofisi-ovaio.</li>"
                "<li><strong>Ipopituitarismo:</strong> Ridotta secrezione di gonadotropine che "
                "abbassa indirettamente l'estradiolo.</li>"
                "<li><strong>Sindrome di Turner:</strong> Condizione genetica congenita in cui "
                "le ovaie non si sviluppano normalmente.</li>"
                "</ul>"
                "<p><strong>Estrogeni alti</strong> (estradiolo elevato) possono verificarsi "
                "nelle seguenti situazioni:</p>"
                "<ul>"
                "<li><strong>PCOS (Sindrome dell'Ovaio Policistico):</strong> Lo squilibrio "
                "ormonale può mantenere i <strong>livelli di estradiolo</strong> relativamente "
                "elevati.</li>"
                "<li><strong>Obesità:</strong> Il tessuto adiposo produce estrogeno aggiuntivo "
                "tramite l'enzima aromatasi.</li>"
                "<li><strong>Tumori estrogeno-secernenti:</strong> Rari tumori ovarici o "
                "surrenalici possono innalzare notevolmente l'estradiolo.</li>"
                "<li><strong>Malattie epatiche:</strong> Il fegato metabolizza l'estrogeno; "
                "l'insufficienza epatica può causarne l'accumulo.</li>"
                "<li><strong>Estrogeni esogeni:</strong> TOS, contraccettivi orali o integratori "
                "di fitoestrogeni possono elevare il livello di E2.</li>"
                "</ul>"
                "<p>I sintomi di <strong>estrogeni bassi</strong> comprendono vampate di calore, "
                "secchezza vaginale, perdita ossea, sbalzi d'umore e stanchezza. I sintomi di "
                "<strong>estrogeni alti</strong> possono includere gonfiore, tensione mammaria, "
                "sanguinamento irregolare, cefalea e aumento di peso.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Se il risultato del <strong>test dell'estradiolo</strong> è al di fuori "
                "dell'intervallo di riferimento o se avvertite sintomi che suggeriscono uno "
                "squilibrio ormonale, è consigliabile rivolgersi a un professionista sanitario. "
                "Consultate il medico in particolare nelle seguenti situazioni:</p>"
                "<ul>"
                "<li>Assenza di mestruazioni per tre mesi o più (amenorrea)</li>"
                "<li>Cicli mestruali irregolari o eccessivamente dolorosi</li>"
                "<li>Sintomi menopausali (vampate di calore, sudorazione notturna, disturbi del "
                "sonno) che compromettono significativamente la qualità della vita</li>"
                "<li>Percorso di valutazione della fertilità o progetto di procreazione "
                "medicalmente assistita (FIVET)</li>"
                "<li>Ginecomastia o disfunzione sessuale nell'uomo</li>"
                "</ul>"
                "<p>Il medico valuterà il risultato del <strong>test dell'estradiolo</strong> "
                "insieme a FSH, LH, progesterone e altri ormoni per individuare la causa "
                "sottostante. Le opzioni terapeutiche comprendono la terapia ormonale "
                "sostitutiva, i contraccettivi orali, modifiche dello stile di vita o il "
                "trattamento della patologia di base.</p>"
                "<p>Ricordate: un singolo risultato del <strong>test dell'estradiolo</strong> "
                "non è sufficiente per una diagnosi definitiva. I risultati devono essere "
                "interpretati insieme alla vostra anamnesi, ai sintomi e ad altri esami di "
                "laboratorio. Questa guida ha scopo informativo — consultate sempre il "
                "vostro medico.</p>"
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
            heading="מהי בדיקת אסטרדיול ומדוע היא חשובה?",
            body_html=(
                "<p><strong>בדיקת אסטרדיול</strong> (הידועה גם בשם <strong>בדיקת E2</strong>) "
                "מודדת את רמת האסטרדיול בדם — הצורה החזקה ביותר של אסטרוגן, המיוצרת בעיקר "
                "על ידי השחלות. <strong>רמות אסטרוגן</strong> ממלאות תפקיד מרכזי במחזור "
                "החודשי, בבריאות העצם, בהגנה על מערכת הלב וכלי הדם ובפוריות. בעוד "
                "<strong>בדיקת אסטרדיול בדם</strong> נדרשת לרוב אצל נשים, היא חשובה גם "
                "להערכת האיזון ההורמונלי אצל גברים.</p>"
                "<p>אסטרדיול מסונתז בעיקר על ידי הזקיקים השחלתיים, עם כמויות קטנות "
                "המגיעות מבלוטות יותרת הכליה ומרקמת השומן. <strong>אסטרוגן נמוך</strong> "
                "עשוי להצביע על מנופאוזה, אי-ספיקה שחלתית או אמנוריאה היפותלמית, "
                "בעוד ש<strong>אסטרוגן גבוה</strong> עשוי להיות קשור לתסמונת השחלות "
                "הפוליציסטיות (PCOS), השמנה או גידולים מפרישי אסטרוגן.</p>"
                "<p>במדריך זה נסביר את טווחי הנורמה של אסטרדיול לפי שלבי חיים, גורמים "
                "שכיחים ל<strong>רמות אסטרוגן</strong> חריגות, תסמינים שיש לשים לב אליהם "
                "ומתי לפנות לרופא. מאמר זה חינוכי ואינו מחליף ייעוץ רפואי מקצועי.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של אסטרדיול: טווחי ייחוס",
            body_html=(
                "<p>טווח הנורמה של אסטרדיול משתנה באופן משמעותי בהתאם למין, גיל ובנשים "
                "לפני גיל המעבר — לפי שלב במחזור החודשי. הטבלה הבאה מסכמת את טווחי "
                "הייחוס המקובלים ל<strong>בדיקת אסטרדיול</strong>:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה / שלב</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח תקין (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">אישה – שלב פוליקולרי</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">אישה – שיא ביוץ</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">אישה – שלב לוטאלי</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">אישה לאחר גיל המעבר</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גבר בוגר</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7.63 – 42.6</td></tr>'
                "</tbody></table>"
                "<p><strong>רמות אסטרוגן</strong> אצל נשים משתנות באופן דרמטי לאורך המחזור "
                "החודשי. האסטרדיול עולה בשלב הפוליקולרי, מגיע לשיא ממש לפני הביוץ ויורד "
                "בשלב הלוטאלי. לכן, יש לפרש את תוצאת <strong>בדיקת האסטרדיול</strong> תמיד "
                "בהתאם ליום במחזור שבו נלקחה דגימת הדם.</p>"
                "<p>לאחר גיל המעבר, <strong>רמות האסטרוגן</strong> יורדות באופן ניכר "
                "ובדרך כלל נשארות מתחת ל-30 pg/mL. אצל גברים, אסטרדיול מיוצר על ידי "
                "המרת טסטוסטרון באמצעות אנזים הארומטאז והוא חשוב לבריאות העצם ולמערכת "
                "הלב וכלי הדם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לאסטרוגן נמוך ואסטרוגן גבוה",
            body_html=(
                "<p><strong>אסטרוגן נמוך</strong> (אסטרדיול נמוך) יכול לנבוע ממגוון "
                "מצבים. הגורמים השכיחים ביותר כוללים:</p>"
                "<ul>"
                "<li><strong>מנופאוזה ופרימנופאוזה:</strong> תפקוד השחלות יורד באופן טבעי "
                "והפקת האסטרוגן פוחתת.</li>"
                "<li><strong>אי-ספיקה שחלתית מוקדמת (POI):</strong> אובדן תפקוד שחלתי "
                "לפני גיל 40 גורם לרמות E2 נמוכות באופן מתמשך.</li>"
                "<li><strong>אמנוריאה היפותלמית:</strong> פעילות גופנית מוגזמת, משקל גוף "
                "נמוך או מתח חמור מדכאים את ציר ההיפותלמוס-היפופיזה-שחלות.</li>"
                "<li><strong>היפופיטואיטריזם:</strong> ירידה בהפרשת גונדוטרופינים מורידה "
                "בעקיפין את האסטרדיול.</li>"
                "<li><strong>תסמונת טרנר:</strong> מצב גנטי מולד שבו השחלות אינן "
                "מתפתחות כראוי.</li>"
                "</ul>"
                "<p><strong>אסטרוגן גבוה</strong> (אסטרדיול מוגבר) עלול להתרחש במצבים "
                "הבאים:</p>"
                "<ul>"
                "<li><strong>PCOS (תסמונת השחלות הפוליציסטיות):</strong> חוסר איזון הורמונלי "
                "עשוי לשמור את <strong>רמות האסטרוגן</strong> גבוהות יחסית.</li>"
                "<li><strong>השמנה:</strong> רקמת שומן מייצרת אסטרוגן נוסף באמצעות אנזים "
                "הארומטאז.</li>"
                "<li><strong>גידולים מפרישי אסטרוגן:</strong> גידולים שחלתיים או אדרנליים "
                "נדירים עלולים להעלות את האסטרדיול באופן ניכר.</li>"
                "<li><strong>מחלות כבד:</strong> הכבד מפרק אסטרוגן; אי-ספיקת כבד עלולה "
                "לגרום להצטברות.</li>"
                "<li><strong>אסטרוגן חיצוני:</strong> טיפול הורמונלי חליפי, גלולות "
                "למניעת הריון או תוספי פיטואסטרוגנים עלולים להעלות את רמת ה-E2.</li>"
                "</ul>"
                "<p>תסמינים של <strong>אסטרוגן נמוך</strong> כוללים גלי חום, יובש בנרתיק, "
                "אובדן מסת עצם, תנודות במצב הרוח ועייפות. תסמינים של <strong>אסטרוגן "
                "גבוה</strong> עשויים לכלול נפיחות, רגישות בשדיים, דימום לא סדיר, כאבי "
                "ראש ועלייה במשקל.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם תוצאת <strong>בדיקת האסטרדיול בדם</strong> שלכם חורגת מטווח "
                "הייחוס או שאתם חווים תסמינים המרמזים על חוסר איזון הורמונלי, מומלץ "
                "לפנות לאיש מקצוע רפואי. שקלו פנייה לרופא במקרים הבאים:</p>"
                "<ul>"
                "<li>היעדר וסת במשך שלושה חודשים או יותר (אמנוריאה)</li>"
                "<li>מחזורים לא סדירים או כואבים במיוחד</li>"
                "<li>תסמיני מנופאוזה (גלי חום, הזעות לילה, הפרעות שינה) הפוגעים "
                "משמעותית באיכות החיים</li>"
                "<li>הערכת פוריות או תכנון טיפולי הפריה (IVF)</li>"
                "<li>גינקומסטיה או הפרעות בתפקוד המיני אצל גברים</li>"
                "</ul>"
                "<p>הרופא יעריך את תוצאת <strong>בדיקת ה-E2</strong> שלכם לצד FSH, LH, "
                "פרוגסטרון והורמונים נוספים כדי לזהות את הגורם הבסיסי. בדיקות נוספות "
                "עשויות לכלול אולטרסאונד אגני, בדיקת צפיפות עצם או פאנל הורמונלי "
                "מורחב. אפשרויות הטיפול כוללות טיפול הורמונלי חליפי, גלולות למניעת "
                "הריון, שינויים באורח החיים או טיפול במצב הרפואי הבסיסי.</p>"
                "<p>זכרו: תוצאה בודדת של <strong>בדיקת אסטרדיול</strong> אינה מספיקה "
                "לאבחנה סופית. יש לפרש את התוצאות יחד עם ההיסטוריה הרפואית שלכם, "
                "התסמינים וממצאי מעבדה נוספים. מדריך זה נועד למטרות מידע בלבד — פנו "
                "תמיד לרופא שלכם.</p>"
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
            heading="एस्ट्राडियोल टेस्ट क्या है और यह क्यों ज़रूरी है?",
            body_html=(
                "<p><strong>एस्ट्राडियोल टेस्ट</strong> (जिसे <strong>E2 टेस्ट</strong> भी "
                "कहा जाता है) आपके रक्त में एस्ट्राडियोल के स्तर को मापता है — यह एस्ट्रोजन "
                "का सबसे शक्तिशाली रूप है जो मुख्य रूप से अंडाशय (ओवरी) द्वारा बनाया जाता "
                "है। <strong>एस्ट्रोजन लेवल</strong> मासिक धर्म चक्र, हड्डियों की सेहत, "
                "हृदय सुरक्षा और प्रजनन क्षमता में अहम भूमिका निभाता है। हालांकि "
                "<strong>एस्ट्राडियोल ब्लड टेस्ट</strong> अधिकतर महिलाओं के लिए किया जाता "
                "है, पुरुषों में हार्मोनल संतुलन मूल्यांकन के लिए भी यह महत्वपूर्ण है।</p>"
                "<p>एस्ट्राडियोल मुख्य रूप से अंडाशय के फॉलिकल्स द्वारा संश्लेषित होता है, "
                "थोड़ी मात्रा एड्रीनल ग्रंथियों और वसा ऊतक से आती है। <strong>कम "
                "एस्ट्रोजन</strong> मेनोपॉज़, ओवेरियन अपर्याप्तता या हाइपोथैलेमिक "
                "एमेनोरिया का संकेत हो सकता है, जबकि <strong>हाई एस्ट्रोजन</strong> PCOS, "
                "मोटापे या एस्ट्रोजन-स्रावी ट्यूमर से जुड़ा हो सकता है।</p>"
                "<p>इस गाइड में हम विभिन्न जीवन चरणों के अनुसार एस्ट्राडियोल के सामान्य "
                "मान, असामान्य <strong>एस्ट्रोजन लेवल</strong> के कारण, लक्षण और डॉक्टर "
                "से कब मिलना चाहिए — यह सब समझाते हैं। यह लेख शैक्षिक है और पेशेवर "
                "चिकित्सा परामर्श का विकल्प नहीं है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="एस्ट्राडियोल के सामान्य मान: रेफरेंस रेंज",
            body_html=(
                "<p>एस्ट्राडियोल की सामान्य सीमा लिंग, उम्र और प्रीमेनोपॉज़ल महिलाओं "
                "में मासिक चक्र के चरण के अनुसार काफ़ी बदलती है। नीचे दी गई तालिका "
                "<strong>एस्ट्राडियोल टेस्ट</strong> के सामान्यतः स्वीकृत रेफरेंस "
                "इंटरवल दर्शाती है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह / चरण</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य सीमा (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">महिला – फॉलिक्युलर फ़ेज़</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">महिला – ओव्यूलेशन पीक</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">महिला – ल्यूटियल फ़ेज़</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">पोस्टमेनोपॉज़ल महिला</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">वयस्क पुरुष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7.63 – 42.6</td></tr>'
                "</tbody></table>"
                "<p>महिलाओं में <strong>एस्ट्रोजन लेवल</strong> मासिक धर्म चक्र के दौरान "
                "नाटकीय रूप से बदलता है। फॉलिक्युलर फ़ेज़ में एस्ट्राडियोल धीरे-धीरे "
                "बढ़ता है, ओव्यूलेशन से ठीक पहले अपने चरम पर पहुँचता है और फिर ल्यूटियल "
                "फ़ेज़ में गिरता है। इसलिए <strong>एस्ट्राडियोल टेस्ट</strong> का परिणाम "
                "हमेशा उस दिन के संदर्भ में पढ़ा जाना चाहिए जिस दिन रक्त का नमूना लिया "
                "गया था।</p>"
                "<p>मेनोपॉज़ के बाद <strong>एस्ट्रोजन लेवल</strong> काफ़ी कम हो जाता है "
                "और आमतौर पर 30 pg/mL से नीचे रहता है। पुरुषों में एस्ट्राडियोल टेस्टोस्टेरोन "
                "के एरोमाटेज़ रूपांतरण से बनता है और हड्डियों तथा हृदय स्वास्थ्य के लिए "
                "महत्वपूर्ण है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="कम एस्ट्रोजन और हाई एस्ट्रोजन के कारण",
            body_html=(
                "<p><strong>कम एस्ट्रोजन</strong> (कम एस्ट्राडियोल) कई स्थितियों के "
                "कारण हो सकता है। सबसे सामान्य कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>मेनोपॉज़ और पेरीमेनोपॉज़:</strong> अंडाशय का कार्य स्वाभाविक "
                "रूप से कम होता है, जिससे एस्ट्रोजन उत्पादन घटता है।</li>"
                "<li><strong>प्रीमैच्योर ओवेरियन अपर्याप्तता (POI):</strong> 40 साल से "
                "पहले अंडाशय के कार्य का नुकसान, जिससे E2 लगातार कम रहता है।</li>"
                "<li><strong>हाइपोथैलेमिक एमेनोरिया:</strong> अत्यधिक व्यायाम, कम शरीर "
                "का वज़न या गंभीर तनाव हाइपोथैलेमस-पिट्यूटरी-ओवेरियन अक्ष को दबाता है।</li>"
                "<li><strong>हाइपोपिट्यूटरिज़्म:</strong> पिट्यूटरी ग्रंथि से गोनाडोट्रोपिन "
                "का कम स्राव अप्रत्यक्ष रूप से एस्ट्राडियोल को कम करता है।</li>"
                "<li><strong>टर्नर सिंड्रोम:</strong> एक जन्मजात आनुवंशिक स्थिति जिसमें "
                "अंडाशय सामान्य रूप से विकसित नहीं होते।</li>"
                "</ul>"
                "<p><strong>हाई एस्ट्रोजन</strong> (ऊँचा एस्ट्राडियोल) निम्नलिखित "
                "स्थितियों में देखा जा सकता है:</p>"
                "<ul>"
                "<li><strong>PCOS (पॉलीसिस्टिक ओवरी सिंड्रोम):</strong> हार्मोनल असंतुलन "
                "<strong>एस्ट्रोजन लेवल</strong> को अपेक्षाकृत ऊँचा रख सकता है।</li>"
                "<li><strong>मोटापा:</strong> वसा ऊतक एरोमाटेज़ एंज़ाइम के माध्यम से अतिरिक्त "
                "एस्ट्रोजन पैदा करता है।</li>"
                "<li><strong>एस्ट्रोजन-स्रावी ट्यूमर:</strong> दुर्लभ ओवेरियन या एड्रीनल "
                "ट्यूमर एस्ट्राडियोल को काफ़ी बढ़ा सकते हैं।</li>"
                "<li><strong>लिवर की बीमारियाँ:</strong> लिवर एस्ट्रोजन को मेटाबोलाइज़ "
                "करता है; लिवर फ़ेलियर से एस्ट्रोजन जमा हो सकता है।</li>"
                "<li><strong>बाहरी एस्ट्रोजन:</strong> HRT, गर्भनिरोधक गोलियाँ या "
                "फ़ाइटोएस्ट्रोजन सप्लीमेंट E2 लेवल बढ़ा सकते हैं।</li>"
                "</ul>"
                "<p><strong>कम एस्ट्रोजन</strong> के लक्षणों में हॉट फ़्लैशेज़, योनि का "
                "सूखापन, हड्डियों का क्षय, मूड स्विंग्स और थकान शामिल हैं। <strong>हाई "
                "एस्ट्रोजन</strong> के लक्षणों में सूजन, स्तन में कोमलता, अनियमित "
                "रक्तस्राव, सिरदर्द और वज़न बढ़ना शामिल हो सकते हैं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>यदि आपकी <strong>एस्ट्राडियोल ब्लड टेस्ट</strong> रिपोर्ट रेफरेंस "
                "रेंज से बाहर है या आपको हार्मोनल असंतुलन के लक्षण अनुभव हो रहे हैं, "
                "तो चिकित्सा विशेषज्ञ से परामर्श करना उचित है। निम्नलिखित स्थितियों "
                "में डॉक्टर से मिलें:</p>"
                "<ul>"
                "<li>तीन या अधिक महीनों से पीरियड्स न आना (एमेनोरिया)</li>"
                "<li>अनियमित या असामान्य रूप से दर्दनाक मासिक चक्र</li>"
                "<li>मेनोपॉज़ के लक्षण (हॉट फ़्लैशेज़, रात को पसीना, नींद में गड़बड़ी) "
                "जो आपकी जीवन गुणवत्ता को काफ़ी प्रभावित कर रहे हों</li>"
                "<li>प्रजनन क्षमता मूल्यांकन या सहायक प्रजनन (IVF) की योजना</li>"
                "<li>पुरुषों में गाइनेकोमैस्टिया या यौन रोग</li>"
                "</ul>"
                "<p>आपके डॉक्टर <strong>E2 टेस्ट</strong> के परिणाम को FSH, LH, "
                "प्रोजेस्टेरोन और अन्य हार्मोन के साथ मिलाकर मूल कारण का पता लगाएँगे। "
                "अतिरिक्त जाँचों में पेल्विक अल्ट्रासाउंड, बोन डेंसिटी स्कैन या "
                "उन्नत हार्मोनल पैनल शामिल हो सकते हैं। उपचार विकल्पों में हार्मोन "
                "रिप्लेसमेंट थेरेपी, गर्भनिरोधक गोलियाँ, जीवनशैली में बदलाव या "
                "अंतर्निहित स्थिति का उपचार शामिल है।</p>"
                "<p>याद रखें: <strong>एस्ट्राडियोल टेस्ट</strong> का एक ही परिणाम निश्चित "
                "निदान के लिए पर्याप्त नहीं है। आपके परिणामों को आपके चिकित्सा इतिहास, "
                "लक्षणों और अन्य प्रयोगशाला निष्कर्षों के साथ समझा जाना चाहिए। यह "
                "गाइड केवल जानकारी के लिए है — अपने स्वास्थ्य के बारे में निर्णय लेने "
                "से पहले हमेशा अपने डॉक्टर से सलाह लें।</p>"
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
            heading="ما هو اختبار الاستراديول ولماذا هو مهم؟",
            body_html=(
                "<p>يقيس <strong>اختبار الاستراديول</strong> (المعروف أيضاً باسم "
                "<strong>اختبار E2</strong>) مستوى الاستراديول في الدم — وهو الشكل الأقوى "
                "من الإستروجين الذي يُنتج بشكل رئيسي من المبيضين. يلعب <strong>مستوى "
                "الإستروجين</strong> دوراً محورياً في الدورة الشهرية وصحة العظام والحماية "
                "القلبية الوعائية والخصوبة. ورغم أن <strong>تحليل الاستراديول في الدم</strong> "
                "يُطلب في الغالب للنساء، إلا أنه مفيد أيضاً لتقييم التوازن الهرموني عند "
                "الرجال.</p>"
                "<p>يُصنّع الاستراديول بشكل أساسي بواسطة الجريبات المبيضية، مع كميات صغيرة "
                "تأتي من الغدد الكظرية والأنسجة الدهنية. قد يشير <strong>انخفاض "
                "الإستروجين</strong> إلى انقطاع الطمث أو قصور المبيض أو انقطاع الطمث "
                "الوطائي، بينما قد يرتبط <strong>ارتفاع الإستروجين</strong> بمتلازمة تكيّس "
                "المبايض (PCOS) أو السمنة أو أورام مفرزة للإستروجين.</p>"
                "<p>في هذا الدليل نشرح القيم الطبيعية للاستراديول حسب المرحلة العمرية، "
                "والأسباب الشائعة لاختلال <strong>مستوى الإستروجين</strong>، والأعراض التي "
                "يجب الانتباه لها، ومتى يجب استشارة الطبيب. هذا المقال تثقيفي ولا يُغني "
                "عن الاستشارة الطبية المتخصصة.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية للاستراديول: النطاقات المرجعية",
            body_html=(
                "<p>يتفاوت النطاق الطبيعي للاستراديول بشكل ملحوظ وفقاً للجنس والعمر، "
                "وعند النساء قبل انقطاع الطمث — وفقاً لمرحلة الدورة الشهرية. يلخّص الجدول "
                "التالي النطاقات المرجعية المقبولة عموماً ل<strong>اختبار "
                "الاستراديول</strong>:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse:collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة / المرحلة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق الطبيعي (pg/mL)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">أنثى – الطور الجريبي</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">12.5 – 166</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">أنثى – ذروة الإباضة</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">85 – 498</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">أنثى – الطور الأصفري</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">43 – 211</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">أنثى بعد انقطاع الطمث</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt; 6 – 54.7</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ذكر بالغ</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">7.63 – 42.6</td></tr>'
                "</tbody></table>"
                "<p>تتقلّب <strong>مستويات الإستروجين</strong> لدى النساء بشكل كبير خلال "
                "الدورة الشهرية. يرتفع الاستراديول تدريجياً في الطور الجريبي ويبلغ ذروته "
                "قبل الإباضة مباشرة ثم ينخفض في الطور الأصفري. لذلك يجب دائماً تفسير "
                "نتيجة <strong>اختبار الاستراديول</strong> مع مراعاة يوم الدورة الذي سُحبت "
                "فيه عيّنة الدم.</p>"
                "<p>بعد انقطاع الطمث ينخفض <strong>مستوى الإستروجين</strong> بشكل ملحوظ "
                "وعادةً ما يبقى أقل من 30 pg/mL. عند الرجال يُنتج الاستراديول عن طريق "
                "تحويل التستوستيرون بواسطة إنزيم الأروماتاز وهو مهم لصحة العظام والقلب "
                "والأوعية الدموية.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب انخفاض الإستروجين وارتفاع الإستروجين",
            body_html=(
                "<p>يمكن أن ينجم <strong>انخفاض الإستروجين</strong> (انخفاض الاستراديول) "
                "عن حالات متعددة. تشمل الأسباب الأكثر شيوعاً:</p>"
                "<ul>"
                "<li><strong>انقطاع الطمث وما قبله:</strong> تتراجع وظيفة المبيض بشكل "
                "طبيعي مما يقلل إنتاج الإستروجين.</li>"
                "<li><strong>قصور المبيض المبكر (POI):</strong> فقدان وظيفة المبيض قبل سن "
                "الأربعين يسبّب مستويات E2 منخفضة باستمرار.</li>"
                "<li><strong>انقطاع الطمث الوطائي:</strong> التمارين المفرطة أو انخفاض "
                "وزن الجسم أو الإجهاد الشديد يثبّط محور الوطاء-النخامية-المبيض.</li>"
                "<li><strong>قصور النخامية:</strong> انخفاض إفراز الغدد التناسلية يقلل "
                "الاستراديول بشكل غير مباشر.</li>"
                "<li><strong>متلازمة تيرنر:</strong> حالة وراثية خلقية لا يتطور فيها "
                "المبيضان بشكل طبيعي.</li>"
                "</ul>"
                "<p>قد يحدث <strong>ارتفاع الإستروجين</strong> (ارتفاع الاستراديول) في "
                "الحالات التالية:</p>"
                "<ul>"
                "<li><strong>متلازمة تكيّس المبايض (PCOS):</strong> الخلل الهرموني قد "
                "يُبقي <strong>مستوى الإستروجين</strong> مرتفعاً نسبياً.</li>"
                "<li><strong>السمنة:</strong> تنتج الأنسجة الدهنية إستروجيناً إضافياً "
                "عبر إنزيم الأروماتاز.</li>"
                "<li><strong>أورام مفرزة للإستروجين:</strong> أورام مبيضية أو كظرية "
                "نادرة يمكنها رفع الاستراديول بشكل ملحوظ.</li>"
                "<li><strong>أمراض الكبد:</strong> يُستقلب الإستروجين في الكبد؛ القصور "
                "الكبدي قد يسبّب تراكمه.</li>"
                "<li><strong>الإستروجين الخارجي:</strong> العلاج الهرموني البديل أو حبوب "
                "منع الحمل أو مكمّلات الفيتوإستروجين قد ترفع مستوى E2.</li>"
                "</ul>"
                "<p>تشمل أعراض <strong>انخفاض الإستروجين</strong> الهبّات الساخنة وجفاف "
                "المهبل وفقدان كتلة العظام وتقلّب المزاج والإرهاق. أما أعراض "
                "<strong>ارتفاع الإستروجين</strong> فقد تشمل الانتفاخ وألم الثدي والنزيف "
                "غير المنتظم والصداع وزيادة الوزن.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب استشارة الطبيب؟",
            body_html=(
                "<p>إذا كانت نتيجة <strong>تحليل الاستراديول في الدم</strong> خارج النطاق "
                "المرجعي أو كنت تعاني من أعراض تشير إلى خلل هرموني، فمن المستحسن استشارة "
                "مختصّ في الرعاية الصحية. اطلب المشورة الطبية بشكل خاص في الحالات التالية:</p>"
                "<ul>"
                "<li>غياب الدورة الشهرية لمدة ثلاثة أشهر أو أكثر (انقطاع الطمث)</li>"
                "<li>دورات شهرية غير منتظمة أو مؤلمة بشكل غير طبيعي</li>"
                "<li>أعراض انقطاع الطمث (هبّات ساخنة، تعرّق ليلي، اضطراب النوم) تؤثر "
                "بشكل كبير على جودة حياتك</li>"
                "<li>تقييم الخصوبة أو التخطيط للمساعدة على الإنجاب (أطفال الأنابيب / IVF)</li>"
                "<li>التثدّي أو الضعف الجنسي عند الرجال</li>"
                "</ul>"
                "<p>سيقيّم طبيبك نتيجة <strong>اختبار E2</strong> إلى جانب FSH وLH "
                "والبروجسترون وهرمونات أخرى لتحديد السبب الكامن. قد تشمل الفحوصات "
                "الإضافية تصوير الحوض بالموجات فوق الصوتية وقياس كثافة العظام أو لوحة "
                "هرمونية موسّعة. تتراوح خيارات العلاج بين العلاج الهرموني البديل وحبوب "
                "منع الحمل وتعديلات نمط الحياة ومعالجة الحالة الأساسية.</p>"
                "<p>تذكّر: نتيجة واحدة من <strong>اختبار الاستراديول</strong> لا تكفي "
                "للتشخيص النهائي. يجب تفسير نتائجك مع تاريخك الطبي وأعراضك ونتائج "
                "الفحوصات المخبرية الأخرى. هذا الدليل لأغراض تثقيفية فقط — استشر طبيبك "
                "دائماً قبل اتخاذ أي قرار يتعلق بصحتك.</p>"
            ),
        ),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_estradiol_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Estradiol article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_estradiol_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Estradiol article (all 9 languages, 3 FAQ items each)."""
    return {
        "tr": [
            {"question": "Estradiol (E2) nedir?",
             "answer": "Estradiol, vücuttaki en güçlü östrojen formudur. Ağırlıklı olarak overler tarafından üretilir ve menstrüel döngü, kemik yoğunluğu, kardiyovasküler sağlık ve üreme fonksiyonları açısından kritik öneme sahiptir. Erkeklerde de testosteronun aromataz enzimi ile dönüşümünden elde edilir."},
            {"question": "Estradiol normal değeri kaçtır?",
             "answer": "Estradiol normal değerleri kadınlarda döngü fazına göre değişir: foliküler faz 12,5–166 pg/mL, ovülasyon doruk 85–498 pg/mL, luteal faz 43–211 pg/mL. Postmenopozal kadınlarda <6–54,7 pg/mL, erkeklerde 7,63–42,6 pg/mL aralığındadır."},
            {"question": "Düşük östrojen belirtileri nelerdir?",
             "answer": "Düşük östrojen belirtileri arasında sıcak basması, gece terlemeleri, vajinal kuruluk, kemik kaybı (osteoporoz riski), ruh hali değişiklikleri, uyku bozuklukları ve adet düzensizliği yer alır. Bu belirtiler özellikle menopoz ve prematür over yetmezliğinde sık görülür."},
        ],
        "en": [
            {"question": "What is estradiol (E2)?",
             "answer": "Estradiol is the most potent form of estrogen in the body. It is produced primarily by the ovaries and plays a critical role in the menstrual cycle, bone density, cardiovascular health, and reproductive function. In men, it is produced through aromatase conversion of testosterone."},
            {"question": "What is a normal estradiol level?",
             "answer": "Normal estradiol levels in women vary by cycle phase: follicular phase 12.5–166 pg/mL, ovulation peak 85–498 pg/mL, luteal phase 43–211 pg/mL. In postmenopausal women the range is <6–54.7 pg/mL, and in adult men 7.63–42.6 pg/mL."},
            {"question": "What are the symptoms of low estrogen?",
             "answer": "Low estrogen symptoms include hot flushes, night sweats, vaginal dryness, bone loss (increased osteoporosis risk), mood swings, sleep disturbances, and menstrual irregularity. These symptoms are particularly common in menopause and premature ovarian insufficiency."},
        ],
        "es": [
            {"question": "¿Qué es el estradiol (E2)?",
             "answer": "El estradiol es la forma más potente de estrógeno en el organismo. Es producido principalmente por los ovarios y desempeña un papel esencial en el ciclo menstrual, la densidad ósea, la salud cardiovascular y la función reproductiva. En hombres se produce mediante la conversión de testosterona por la enzima aromatasa."},
            {"question": "¿Cuál es el nivel normal de estradiol?",
             "answer": "Los niveles normales de estradiol en mujeres varían según la fase del ciclo: fase folicular 12,5–166 pg/mL, pico ovulatorio 85–498 pg/mL, fase lútea 43–211 pg/mL. En mujeres posmenopáusicas <6–54,7 pg/mL y en hombres adultos 7,63–42,6 pg/mL."},
            {"question": "¿Cuáles son los síntomas de estrógeno bajo?",
             "answer": "Los síntomas de estrógeno bajo incluyen sofocos, sudoración nocturna, sequedad vaginal, pérdida ósea (mayor riesgo de osteoporosis), cambios de humor, trastornos del sueño e irregularidad menstrual. Estos síntomas son especialmente frecuentes en la menopausia y la insuficiencia ovárica prematura."},
        ],
        "de": [
            {"question": "Was ist Östradiol (E2)?",
             "answer": "Östradiol ist die wirksamste Form des Östrogens im Körper. Es wird hauptsächlich von den Eierstöcken produziert und spielt eine entscheidende Rolle im Menstruationszyklus, bei der Knochendichte, der kardiovaskulären Gesundheit und der Fortpflanzungsfunktion. Bei Männern entsteht es durch Aromatase-Umwandlung von Testosteron."},
            {"question": "Was ist ein normaler Östradiol-Wert?",
             "answer": "Normale Östradiol-Werte bei Frauen variieren je nach Zyklusphase: Follikelphase 12,5–166 pg/mL, Ovulationsgipfel 85–498 pg/mL, Lutealphase 43–211 pg/mL. Bei postmenopausalen Frauen liegt der Bereich bei <6–54,7 pg/mL, bei erwachsenen Männern bei 7,63–42,6 pg/mL."},
            {"question": "Was sind die Symptome eines niedrigen Östrogenspiegels?",
             "answer": "Symptome eines niedrigen Östrogenspiegels umfassen Hitzewallungen, Nachtschweiß, Scheidentrockenheit, Knochenschwund (erhöhtes Osteoporoserisiko), Stimmungsschwankungen, Schlafstörungen und Zyklusunregelmäßigkeiten. Diese Symptome treten besonders häufig in der Menopause und bei prämaturerem Ovarialinsuffizienz auf."},
        ],
        "fr": [
            {"question": "Qu'est-ce que l'œstradiol (E2) ?",
             "answer": "L'œstradiol est la forme la plus active d'œstrogène dans l'organisme. Il est principalement produit par les ovaires et joue un rôle essentiel dans le cycle menstruel, la densité osseuse, la santé cardiovasculaire et la fonction reproductive. Chez l'homme, il est produit par conversion de la testostérone via l'enzyme aromatase."},
            {"question": "Quel est le taux normal d'œstradiol ?",
             "answer": "Les taux normaux d'œstradiol chez la femme varient selon la phase du cycle : phase folliculaire 12,5–166 pg/mL, pic ovulatoire 85–498 pg/mL, phase lutéale 43–211 pg/mL. Chez la femme ménopausée <6–54,7 pg/mL et chez l'homme adulte 7,63–42,6 pg/mL."},
            {"question": "Quels sont les symptômes d'un œstrogène bas ?",
             "answer": "Les symptômes d'un œstrogène bas comprennent bouffées de chaleur, sueurs nocturnes, sécheresse vaginale, perte osseuse (risque accru d'ostéoporose), sautes d'humeur, troubles du sommeil et irrégularités menstruelles. Ces symptômes sont particulièrement fréquents lors de la ménopause et de l'insuffisance ovarienne prématurée."},
        ],
        "it": [
            {"question": "Che cos'è l'estradiolo (E2)?",
             "answer": "L'estradiolo è la forma più potente di estrogeno nell'organismo. È prodotto principalmente dalle ovaie e svolge un ruolo fondamentale nel ciclo mestruale, nella densità ossea, nella salute cardiovascolare e nella funzione riproduttiva. Nell'uomo è prodotto dalla conversione del testosterone tramite l'enzima aromatasi."},
            {"question": "Qual è il valore normale di estradiolo?",
             "answer": "I valori normali di estradiolo nelle donne variano in base alla fase del ciclo: fase follicolare 12,5–166 pg/mL, picco ovulatorio 85–498 pg/mL, fase luteale 43–211 pg/mL. Nella donna in menopausa <6–54,7 pg/mL e nell'uomo adulto 7,63–42,6 pg/mL."},
            {"question": "Quali sono i sintomi degli estrogeni bassi?",
             "answer": "I sintomi degli estrogeni bassi includono vampate di calore, sudorazione notturna, secchezza vaginale, perdita ossea (maggior rischio di osteoporosi), sbalzi d'umore, disturbi del sonno e irregolarità mestruali. Questi sintomi sono particolarmente comuni in menopausa e nell'insufficienza ovarica prematura."},
        ],
        "he": [
            {"question": "מהו אסטרדיול (E2)?",
             "answer": "אסטרדיול הוא הצורה החזקה ביותר של אסטרוגן בגוף. הוא מיוצר בעיקר על ידי השחלות וממלא תפקיד מרכזי במחזור החודשי, בצפיפות העצם, בבריאות הלב וכלי הדם ובתפקוד הרבייה. אצל גברים הוא מיוצר על ידי המרת טסטוסטרון באמצעות אנזים הארומטאז."},
            {"question": "מהי רמת אסטרדיול תקינה?",
             "answer": "רמות אסטרדיול תקינות בנשים משתנות לפי שלב המחזור: שלב פוליקולרי 12.5–166 pg/mL, שיא ביוץ 85–498 pg/mL, שלב לוטאלי 43–211 pg/mL. בנשים לאחר גיל המעבר <6–54.7 pg/mL ובגברים בוגרים 7.63–42.6 pg/mL."},
            {"question": "מהם התסמינים של אסטרוגן נמוך?",
             "answer": "תסמיני אסטרוגן נמוך כוללים גלי חום, הזעות לילה, יובש בנרתיק, אובדן מסת עצם (סיכון מוגבר לאוסטיאופורוזיס), תנודות במצב הרוח, הפרעות שינה ואי-סדירות במחזור. תסמינים אלה שכיחים במיוחד במנופאוזה ובאי-ספיקה שחלתית מוקדמת."},
        ],
        "hi": [
            {"question": "एस्ट्राडियोल (E2) क्या है?",
             "answer": "एस्ट्राडियोल शरीर में एस्ट्रोजन का सबसे शक्तिशाली रूप है। यह मुख्य रूप से अंडाशय द्वारा उत्पादित होता है और मासिक धर्म चक्र, हड्डियों के घनत्व, हृदय स्वास्थ्य और प्रजनन कार्य में महत्वपूर्ण भूमिका निभाता है। पुरुषों में यह टेस्टोस्टेरोन के एरोमाटेज़ रूपांतरण से बनता है।"},
            {"question": "सामान्य एस्ट्राडियोल लेवल क्या है?",
             "answer": "महिलाओं में सामान्य एस्ट्राडियोल स्तर चक्र चरण के अनुसार भिन्न होता है: फॉलिक्युलर फ़ेज़ 12.5–166 pg/mL, ओव्यूलेशन पीक 85–498 pg/mL, ल्यूटियल फ़ेज़ 43–211 pg/mL। पोस्टमेनोपॉज़ल महिलाओं में <6–54.7 pg/mL और वयस्क पुरुषों में 7.63–42.6 pg/mL होता है।"},
            {"question": "कम एस्ट्रोजन के लक्षण क्या हैं?",
             "answer": "कम एस्ट्रोजन के लक्षणों में हॉट फ़्लैशेज़, रात को पसीना, योनि का सूखापन, हड्डियों का क्षय (ऑस्टियोपोरोसिस का बढ़ा जोखिम), मूड स्विंग्स, नींद की गड़बड़ी और अनियमित मासिक धर्म शामिल हैं। ये लक्षण मेनोपॉज़ और प्रीमैच्योर ओवेरियन अपर्याप्तता में विशेष रूप से सामान्य हैं।"},
        ],
        "ar": [
            {"question": "ما هو الاستراديول (E2)؟",
             "answer": "الاستراديول هو الشكل الأقوى من الإستروجين في الجسم. يُنتج بشكل رئيسي من المبيضين ويلعب دوراً محورياً في الدورة الشهرية وكثافة العظام وصحة القلب والأوعية الدموية والوظيفة الإنجابية. عند الرجال يُنتج عبر تحويل التستوستيرون بواسطة إنزيم الأروماتاز."},
            {"question": "ما هو المستوى الطبيعي للاستراديول؟",
             "answer": "تتفاوت مستويات الاستراديول الطبيعية عند النساء حسب مرحلة الدورة: الطور الجريبي 12.5–166 pg/mL، ذروة الإباضة 85–498 pg/mL، الطور الأصفري 43–211 pg/mL. عند النساء بعد انقطاع الطمث <6–54.7 pg/mL وعند الرجال البالغين 7.63–42.6 pg/mL."},
            {"question": "ما أعراض انخفاض الإستروجين؟",
             "answer": "تشمل أعراض انخفاض الإستروجين الهبّات الساخنة والتعرّق الليلي وجفاف المهبل وفقدان كتلة العظام (زيادة خطر هشاشة العظام) وتقلّب المزاج واضطرابات النوم وعدم انتظام الدورة الشهرية. تظهر هذه الأعراض بشكل خاص عند انقطاع الطمث وقصور المبيض المبكر."},
        ],
    }
