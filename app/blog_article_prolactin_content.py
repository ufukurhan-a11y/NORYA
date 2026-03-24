# -*- coding: utf-8 -*-
"""
Prolactin (Prolaktin) blog article — full body content for all 9 languages.
Used by blog_i18n._article_prolactin().
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
            heading="Prolaktin kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>prolaktin</strong> değerini gördüğünüzde bu hormonun "
                "ne anlama geldiğini ve yüksek ya da düşük çıkmasının sağlığınızı nasıl etkileyebileceğini "
                "merak etmeniz doğaldır. Prolaktin, hipofiz bezinin ön lobundan salgılanan ve başta "
                "laktasyon (süt üretimi) olmak üzere üreme sistemi, bağışıklık ve metabolizma üzerinde "
                "geniş etkileri olan bir peptit hormondur.</p>"
                "<p>Bu rehber prolaktin kan testinin ne anlama geldiğini, normal referans aralıklarını, "
                "<strong>prolaktin yüksekliği</strong> (hiperprolaktinemi) nedenlerini, semptomlarını ve "
                "ne zaman doktora başvurmanız gerektiğini sade bir dille açıklamayı amaçlıyor. Amacımız "
                "teşhis koymak değil; sonuçlarınızı daha iyi anlayarak hekiminizle verimli bir görüşme "
                "yapmanıza yardımcı olmaktır.</p>"
                "<p>Prolaktin düzeyindeki anormallikler özellikle kadınlarda adet düzensizlikleri ve "
                "infertilite, erkeklerde ise cinsel işlev bozukluğu ile kendini gösterebilir. Erken "
                "tanı ve doğru tedaviyle bu sorunların büyük çoğunluğu başarıyla yönetilebilir.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Prolaktin nedir?",
            body_html=(
                "<p><strong>Prolaktin</strong>, hipofiz bezinin (pitüiter bez) ön lobundaki laktotrop "
                "hücreler tarafından üretilen 199 amino asitlik bir polipeptit hormondur. Adını &ldquo;süt "
                "üretimini teşvik etme&rdquo; işlevinden alır; ancak vücuttaki rolleri laktasyonla sınırlı "
                "değildir. Prolaktin ayrıca üreme fonksiyonları, bağışıklık sistemi düzenlemesi ve "
                "ozmotik dengenin sağlanmasında da görev alır.</p>"
                "<p>Prolaktin salgılanması hipotalamus tarafından ağırlıklı olarak <strong>dopamin</strong> "
                "aracılığıyla baskılanır. Dopamin düzeyi düştüğünde veya dopaminin etkisini engelleyen "
                "ilaçlar kullanıldığında prolaktin seviyesi yükselir. Bu nedenle prolaktin, &ldquo;tonik "
                "inhibisyon&rdquo; altında olan nadir hormonlardan biridir; yani sürekli baskılanmazsa "
                "düzeyi artar.</p>"
                "<p>Hem kadınlarda hem de erkeklerde kanda belirli bir düzeyde prolaktin bulunur. "
                "Hamilelik ve emzirme döneminde kadınlarda prolaktin fizyolojik olarak çok yükselir. "
                "Bunun dışındaki yükseklikler ise çeşitli patolojik durumları işaret edebilir ve "
                "araştırılması gerekir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Prolaktin normal değerleri (referans aralıkları)",
            body_html=(
                "<p>Prolaktin düzeyi basit bir kan testiyle ölçülür. Aşağıdaki tablo yaygın olarak "
                "kabul edilen referans aralıklarını göstermektedir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadın (hamile olmayan)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hamile kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>Prolaktin seviyesi gün içinde dalgalanır; uyku sırasında en yüksek değere ulaşır ve "
                "uyanmadan birkaç saat sonra düşer. Bu nedenle kan örneği genellikle sabah, uyanmadan "
                "2&ndash;3 saat sonra alınır. Stres, egzersiz ve yüksek proteinli yemekler de geçici "
                "yüksekliğe neden olabilir.</p>"
                "<p>Laboratuvarlar arasında küçük farklılıklar olabileceğinden sonucunuzu mutlaka kendi "
                "laboratuvarınızın referans aralığıyla karşılaştırmanız önemlidir. 200&nbsp;ng/mL "
                "üzerindeki değerler güçlü bir şekilde <strong>prolaktinoma</strong> (hipofiz adenomu) "
                "şüphesi uyandırır.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Prolaktin yüksekliğinin (hiperprolaktinemi) nedenleri",
            body_html=(
                "<p><strong>Hiperprolaktinemi</strong>, yani prolaktin yüksekliği pek çok farklı "
                "nedenden kaynaklanabilir. En sık karşılaşılan nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Prolaktinoma (hipofiz adenomu):</strong> Hipofiz bezinde prolaktin üreten "
                "iyi huylu bir tümördür ve en sık patolojik nedendir. Mikroprolaktinoma (&lt;10&nbsp;mm) "
                "ve makroprolaktinoma (&ge;10&nbsp;mm) olarak ikiye ayrılır.</li>"
                "<li><strong>İlaçlar:</strong> Antipsikotikler (haloperidol, risperidon), metoklopramid, "
                "domperidon, bazı antidepresanlar ve östrojen içeren ilaçlar en yaygın ilaç nedenli "
                "hiperprolaktinemi nedenleridir. İlaçlar, tümör dışı en sık nedendir.</li>"
                "<li><strong>Hipotiroidizm:</strong> Tiroid hormon eksikliğinde TRH yükselir ve TRH, "
                "prolaktin salgılanmasını uyarır.</li>"
                "<li><strong>Göğüs duvarı irritasyonu:</strong> Herpes zoster, göğüs cerrahisi veya "
                "göğüs duvarı lezyonları refleks yollarla prolaktini artırabilir.</li>"
                "<li><strong>Polikistik over sendromu (PKOS):</strong> PKOS&rsquo;lu kadınların bir "
                "kısmında hafif prolaktin yüksekliği görülür.</li>"
                "<li><strong>Stres ve fizyolojik nedenler:</strong> Yoğun stres, uyku, egzersiz ve "
                "meme stimülasyonu geçici yüksekliğe neden olabilir.</li>"
                "<li><strong>Böbrek yetmezliği:</strong> Prolaktinin renal klirensi azaldığında "
                "serum düzeyi artar.</li>"
                "</ul>"
                "<p>Prolaktin düzeyi 200&nbsp;ng/mL&rsquo;nin üzerindeyse prolaktinoma olasılığı "
                "yüksektir. 25&ndash;100&nbsp;ng/mL arası değerlerde ise ilaç kullanımı, hipotiroidizm "
                "ve diğer nedenler öncelikle araştırılmalıdır.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Yüksek prolaktin belirtileri",
            body_html=(
                "<p>Prolaktin yüksekliğinin belirtileri cinsiyete göre farklılık gösterir. "
                "Kadınlarda en sık görülen semptomlar şunlardır:</p>"
                "<ul>"
                "<li><strong>Adet düzensizlikleri:</strong> Oligomenore (seyrek adet) veya amenore "
                "(adet kesilmesi) hiperprolaktineminin en belirgin bulgusudur.</li>"
                "<li><strong>Galaktore:</strong> Hamilelik veya emzirme dışında memeden süt benzeri "
                "bir sıvı gelmesidir.</li>"
                "<li><strong>İnfertilite:</strong> Prolaktin yüksekliği ovülasyonu baskılayarak "
                "gebe kalamama sorununa yol açabilir.</li>"
                "</ul>"
                "<p>Erkeklerde ise belirtiler genellikle daha geç fark edilir:</p>"
                "<ul>"
                "<li><strong>Cinsel istek azalması (libido kaybı):</strong> Testosteron düzeyinin "
                "düşmesine bağlı olarak gelişir.</li>"
                "<li><strong>Erektil disfonksiyon:</strong> Yüksek prolaktin, GnRH pulsasyonunu "
                "bozarak hipogonadizme ve erektil sorunlara neden olabilir.</li>"
                "<li><strong>Jinekomasti ve nadiren galaktore:</strong> Erkeklerde meme büyümesi "
                "ve nadiren memeden akıntı görülebilir.</li>"
                "</ul>"
                "<p>Her iki cinsiyette de makroprolaktinoma durumunda <strong>baş ağrısı</strong> ve "
                "<strong>görme alanı daralması</strong> (bitemporal hemianopsi) gibi kitle etkisi "
                "semptomları ortaya çıkabilir. Tümör büyüdükçe optik kiazma üzerine bası yaparak "
                "periferik görüş kaybına yol açar.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlişkili testler",
            body_html=(
                "<p>Prolaktin yüksekliği saptandığında nedeni belirlemek için ek testler istenir. "
                "En sık kullanılan ilişkili testler şunlardır:</p>"
                "<ul>"
                "<li><strong>TSH (Tiroid Stimülan Hormon):</strong> Hipotiroidizmin prolaktin "
                "yüksekliğine neden olup olmadığını değerlendirmek için istenir.</li>"
                "<li><strong>LH ve FSH:</strong> Gonadotropin düzeyleri üreme fonksiyonlarının "
                "değerlendirilmesinde önemlidir.</li>"
                "<li><strong>Gebelik testi (beta-hCG):</strong> Doğurganlık çağındaki kadınlarda "
                "hamileliğin dışlanması için mutlaka yapılmalıdır.</li>"
                "<li><strong>Hipofiz MRG:</strong> Prolaktinoma şüphesinde hipofiz bezinin "
                "görüntülenmesi için altın standart tetkiktir.</li>"
                "<li><strong>Testosteron (erkeklerde):</strong> Hipogonadizm değerlendirmesi için "
                "total ve serbest testosteron ölçülür.</li>"
                "<li><strong>Makroprolaktin:</strong> Bazı durumlarda prolaktin molekülleri "
                "immünoglobülinlerle kompleks oluşturarak yanlış yüksek sonuçlara neden olabilir; "
                "bu durumda makroprolaktin taraması yapılır.</li>"
                "</ul>"
                "<p>Bu testlerin birlikte değerlendirilmesi, yüksek prolaktinin nedenine yönelik "
                "doğru tanı ve tedavi planlamasında kritik öneme sahiptir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda bir endokrinoloji veya kadın hastalıkları uzmanına "
                "başvurmanız önerilir:</p>"
                "<ul>"
                "<li>Kan tahlilinde prolaktin değeriniz referans aralığının üstünde çıktıysa</li>"
                "<li>Açıklanamayan adet düzensizliği veya amenore yaşıyorsanız</li>"
                "<li>Hamilelik veya emzirme dışında memeden akıntı fark ettiyseniz</li>"
                "<li>Cinsel istek kaybı, erektil disfonksiyon veya infertilite sorunu varsa</li>"
                "<li>Sürekli baş ağrısı ve/veya görme bozuklukları yaşıyorsanız</li>"
                "</ul>"
                "<p>Erken tanı özellikle prolaktinoma durumunda büyük önem taşır. Mikroprolaktinomalar "
                "genellikle dopamin agonistleri (kabergolin, bromokriptin) ile medikal tedaviye çok iyi "
                "yanıt verir ve çoğu durumda cerrahi gerektirmez. Tedavisiz bırakılan "
                "makroprolaktinomalar ise büyüyerek görme kaybı ve hipopitüitarizm gibi ciddi "
                "komplikasyonlara yol açabilir.</p>"
                "<p>Prolaktin yüksekliği ilaç kullanımına bağlıysa, ilacın değiştirilmesi veya "
                "dozunun ayarlanması genellikle sorunu çözer. Ancak bu kararı mutlaka hekiminizle "
                "birlikte vermelisiniz; ilacınızı kendiniz bırakmayın.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI prolaktin sonuçlarınızı nasıl değerlendirir?",
            body_html=(
                "<p><strong>NoryaAI</strong>, kan tahlili raporunuzu yüklediğinizde prolaktin dahil "
                "tüm biyobelirteçlerinizi yaşınıza, cinsiyetinize ve klinik bağlamınıza göre analiz "
                "eder. Yapay zekâ destekli sistemimiz referans aralık dışı değerleri vurgular, olası "
                "nedenleri özetler ve hekiminize sormak isteyebileceğiniz soruları önerir.</p>"
                "<p>Sonuçlarınızı hemen değerlendirmek için <a href=\"/analyze\">lab raporunuzu "
                "yükleyin</a>. Farklı plan seçeneklerimiz hakkında bilgi almak için "
                "<a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edebilirsiniz. NoryaAI "
                "hekim muayenesinin yerini almaz; amacımız sizi bilgilendirerek doktorunuzla daha "
                "verimli bir görüşme yapmanızı sağlamaktır.</p>"
                "<p>Prolaktin değeriniz normalin dışındaysa panik yapmayın; pek çok neden tedavi "
                "edilebilir. Ancak sonuçlarınızı bir sağlık profesyoneli ile paylaşmanız her zaman "
                "en doğru adımdır.</p>"
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
            heading="Prolactin blood test: what your results mean",
            body_html=(
                "<p>If your lab report shows an abnormal <strong>prolactin</strong> level, you are "
                "probably wondering what this hormone does and whether you should be concerned. "
                "Prolactin is a peptide hormone produced by the anterior pituitary gland, best known "
                "for stimulating breast-milk production, but it also influences reproduction, immune "
                "function, and metabolism in both women and men.</p>"
                "<p>This guide explains what a <strong>prolactin blood test</strong> measures, "
                "normal reference ranges, common causes of <strong>high prolactin</strong> "
                "(hyperprolactinemia), associated symptoms, and when you should see a doctor. Our "
                "goal is not to diagnose — it is to help you understand your results so you can have "
                "a more productive conversation with your healthcare provider.</p>"
                "<p>Abnormal prolactin levels can lead to menstrual irregularities and infertility in "
                "women, and sexual dysfunction in men. The good news is that most causes of "
                "hyperprolactinemia are treatable once correctly identified.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="What is prolactin?",
            body_html=(
                "<p><strong>Prolactin</strong> is a 199-amino-acid polypeptide hormone synthesized by "
                "lactotroph cells in the anterior pituitary gland. Although its name literally means "
                "&ldquo;for milk,&rdquo; prolactin plays roles far beyond lactation, including "
                "regulation of reproductive function, immune modulation, and osmotic balance.</p>"
                "<p>Prolactin secretion is primarily controlled by the hypothalamus through "
                "<strong>dopamine</strong>, which acts as a prolactin-inhibiting factor. When dopamine "
                "levels drop or when medications block dopamine receptors, prolactin rises. This makes "
                "prolactin somewhat unusual among pituitary hormones — it is under tonic inhibition, "
                "meaning it increases whenever its brake is released.</p>"
                "<p>Both women and men have measurable circulating prolactin. During pregnancy and "
                "breastfeeding, prolactin rises dramatically — this is entirely physiological. Elevations "
                "outside these contexts, however, deserve investigation because they may point to a "
                "pituitary adenoma, medication side-effect, or another underlying condition.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal prolactin levels (reference ranges)",
            body_html=(
                "<p>Prolactin is measured with a simple blood draw. The table below shows commonly "
                "accepted reference ranges:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Men</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Non-pregnant women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Pregnant women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>Prolactin follows a circadian rhythm — it peaks during sleep and falls within a few "
                "hours of waking. For this reason, blood samples are usually drawn in the morning, "
                "2&ndash;3 hours after waking. Stress, vigorous exercise, and high-protein meals can "
                "cause transient elevations, so a mildly elevated result may warrant a repeat test.</p>"
                "<p>Levels above 200&nbsp;ng/mL strongly suggest a <strong>prolactinoma</strong> "
                "(prolactin-secreting pituitary adenoma). Values between 25 and 100&nbsp;ng/mL are more "
                "commonly associated with medications, hypothyroidism, or other non-tumour causes. "
                "Always compare your result with your own laboratory&rsquo;s reference range.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high prolactin (hyperprolactinemia)",
            body_html=(
                "<p><strong>Hyperprolactinemia</strong> can result from a wide variety of causes. The "
                "most frequently encountered are:</p>"
                "<ul>"
                "<li><strong>Prolactinoma (pituitary adenoma):</strong> A benign prolactin-secreting "
                "tumour of the pituitary gland and the most common pathological cause. It is classified "
                "as a microprolactinoma (&lt;10&nbsp;mm) or macroprolactinoma (&ge;10&nbsp;mm).</li>"
                "<li><strong>Medications:</strong> Antipsychotics (haloperidol, risperidone), "
                "metoclopramide, domperidone, certain antidepressants, and oestrogen-containing drugs "
                "are the most common drug-induced causes. Medications are the leading non-tumour cause "
                "of hyperprolactinemia.</li>"
                "<li><strong>Hypothyroidism:</strong> Low thyroid hormone triggers elevated TRH, which "
                "in turn stimulates prolactin release.</li>"
                "<li><strong>Chest-wall irritation:</strong> Herpes zoster, chest surgery, or chest-wall "
                "lesions can raise prolactin via reflex neural pathways.</li>"
                "<li><strong>Polycystic ovary syndrome (PCOS):</strong> Mild prolactin elevation is seen "
                "in a subset of women with PCOS.</li>"
                "<li><strong>Stress and physiological factors:</strong> Intense stress, sleep, exercise, "
                "and nipple stimulation can cause transient increases.</li>"
                "<li><strong>Renal failure:</strong> Reduced renal clearance of prolactin leads to "
                "elevated serum levels.</li>"
                "</ul>"
                "<p>When prolactin exceeds 200&nbsp;ng/mL, a prolactinoma is highly likely. For values "
                "between 25 and 100&nbsp;ng/mL, drug use, hypothyroidism, and other non-tumour causes "
                "should be evaluated first.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of high prolactin",
            body_html=(
                "<p>The symptoms of hyperprolactinemia differ between women and men. In women the most "
                "common signs include:</p>"
                "<ul>"
                "<li><strong>Menstrual irregularities:</strong> Oligomenorrhea (infrequent periods) or "
                "amenorrhea (absence of periods) is the hallmark symptom.</li>"
                "<li><strong>Galactorrhea:</strong> A milky discharge from the breasts outside of "
                "pregnancy or breastfeeding.</li>"
                "<li><strong>Infertility:</strong> Elevated prolactin suppresses ovulation, making "
                "conception difficult.</li>"
                "</ul>"
                "<p>In men, symptoms are often recognised later:</p>"
                "<ul>"
                "<li><strong>Decreased libido:</strong> Driven by the secondary drop in testosterone.</li>"
                "<li><strong>Erectile dysfunction:</strong> High prolactin disrupts GnRH pulsatility, "
                "leading to hypogonadism and erectile problems.</li>"
                "<li><strong>Gynaecomastia and rarely galactorrhea:</strong> Breast tissue enlargement "
                "and, in rare cases, nipple discharge may occur.</li>"
                "</ul>"
                "<p>In both sexes, a macroprolactinoma can produce mass-effect symptoms such as "
                "<strong>headaches</strong> and <strong>visual field defects</strong> (bitemporal "
                "hemianopia). As the tumour grows it compresses the optic chiasm, causing progressive "
                "loss of peripheral vision.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>When an elevated prolactin is found, additional tests help pinpoint the cause:</p>"
                "<ul>"
                "<li><strong>TSH (Thyroid-Stimulating Hormone):</strong> Rules out hypothyroidism as "
                "the underlying trigger.</li>"
                "<li><strong>LH and FSH:</strong> Gonadotropin levels are important for evaluating "
                "reproductive function.</li>"
                "<li><strong>Pregnancy test (beta-hCG):</strong> Must be performed in women of "
                "childbearing age to exclude pregnancy.</li>"
                "<li><strong>Pituitary MRI:</strong> The gold standard imaging study when a "
                "prolactinoma is suspected.</li>"
                "<li><strong>Testosterone (in men):</strong> Total and free testosterone are "
                "measured to assess for hypogonadism.</li>"
                "<li><strong>Macroprolactin screening:</strong> In some cases prolactin molecules "
                "form complexes with immunoglobulins, producing falsely elevated results. A "
                "macroprolactin assay can clarify this.</li>"
                "</ul>"
                "<p>Evaluating these tests together is critical for accurate diagnosis and "
                "appropriate treatment planning.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>You should consult an endocrinologist or gynaecologist if:</p>"
                "<ul>"
                "<li>Your blood test shows prolactin above the reference range</li>"
                "<li>You experience unexplained menstrual irregularities or amenorrhea</li>"
                "<li>You notice nipple discharge outside of pregnancy or breastfeeding</li>"
                "<li>You have decreased libido, erectile dysfunction, or infertility</li>"
                "<li>You suffer from persistent headaches and/or visual disturbances</li>"
                "</ul>"
                "<p>Early diagnosis is especially important in prolactinoma. Microprolactinomas respond "
                "very well to dopamine agonists (cabergoline, bromocriptine) and rarely require surgery. "
                "Left untreated, macroprolactinomas can grow and cause serious complications such as "
                "vision loss and hypopituitarism.</p>"
                "<p>If the elevation is drug-induced, switching or adjusting the medication usually "
                "resolves the problem. However, never stop a prescribed medication on your own — always "
                "discuss changes with your doctor.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How NoryaAI helps you understand prolactin results",
            body_html=(
                "<p><strong>NoryaAI</strong> analyses your full blood-test report — including prolactin — "
                "in the context of your age, sex, and clinical background. Our AI-powered system "
                "highlights out-of-range values, summarises possible causes, and suggests questions you "
                "may want to ask your doctor.</p>"
                "<p>Ready to get started? <a href=\"/analyze\">Upload your lab report</a> for an instant "
                "analysis. Visit our <a href=\"/pricing\">pricing page</a> to explore plan options. "
                "NoryaAI does not replace a physician; our goal is to empower you with information so "
                "your next medical consultation is more productive.</p>"
                "<p>If your prolactin is outside the normal range, do not panic — many causes are "
                "treatable. The most important step is to share your results with a qualified "
                "healthcare professional.</p>"
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
        Section(
            id="intro", level=2,
            heading="Análisis de prolactina en sangre: qué significan sus resultados",
            body_html=(
                "<p>Si su informe de laboratorio muestra un nivel anormal de <strong>prolactina</strong>, "
                "es natural preguntarse qué significa esta hormona y si debe preocuparse. La prolactina "
                "es una hormona peptídica producida por la hipófisis anterior, conocida sobre todo por "
                "estimular la producción de leche materna, pero también influye en la reproducción, la "
                "inmunidad y el metabolismo tanto en mujeres como en hombres.</p>"
                "<p>Esta guía explica qué mide el <strong>análisis de prolactina</strong>, los rangos de "
                "referencia normales, las causas frecuentes de <strong>prolactina alta</strong> "
                "(hiperprolactinemia), los síntomas asociados y cuándo consultar al médico. Nuestro "
                "objetivo no es diagnosticar, sino ayudarle a comprender sus resultados para que pueda "
                "mantener una conversación más productiva con su profesional de salud.</p>"
                "<p>Los niveles anormales de prolactina pueden causar irregularidades menstruales e "
                "infertilidad en mujeres, y disfunción sexual en hombres. La buena noticia es que la "
                "mayoría de las causas de hiperprolactinemia son tratables una vez identificadas "
                "correctamente.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="¿Qué es la prolactina?",
            body_html=(
                "<p>La <strong>prolactina</strong> es un polipéptido de 199 aminoácidos sintetizado por "
                "las células lactotropas de la hipófisis anterior. Aunque su nombre significa "
                "&laquo;a favor de la leche&raquo;, sus funciones van mucho más allá de la lactancia: "
                "regula la función reproductiva, modula el sistema inmunitario y contribuye al "
                "equilibrio osmótico.</p>"
                "<p>La secreción de prolactina está controlada principalmente por la "
                "<strong>dopamina</strong> hipotalámica, que actúa como factor inhibidor. Cuando la "
                "dopamina disminuye o se bloquean sus receptores, la prolactina sube. Esto convierte a "
                "la prolactina en una hormona inusual: está bajo inhibición tónica, es decir, aumenta "
                "siempre que se libera su freno.</p>"
                "<p>Tanto mujeres como hombres tienen prolactina circulante medible. Durante el embarazo "
                "y la lactancia, la prolactina se eleva de forma fisiológica. Las elevaciones fuera de "
                "estos contextos requieren investigación, ya que pueden indicar un adenoma hipofisario, "
                "un efecto secundario farmacológico u otra patología subyacente.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de prolactina (rangos de referencia)",
            body_html=(
                "<p>La prolactina se mide mediante una simple extracción de sangre. La siguiente tabla "
                "muestra los rangos de referencia más aceptados:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres no embarazadas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres embarazadas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>La prolactina sigue un ritmo circadiano: alcanza su pico durante el sueño y desciende "
                "unas horas después de despertar. Por ello, la muestra suele tomarse por la mañana, "
                "2&ndash;3 horas después de levantarse. El estrés, el ejercicio intenso y las comidas "
                "ricas en proteínas pueden provocar elevaciones transitorias.</p>"
                "<p>Valores superiores a 200&nbsp;ng/mL sugieren fuertemente un <strong>prolactinoma</strong>. "
                "Valores entre 25 y 100&nbsp;ng/mL suelen asociarse a fármacos, hipotiroidismo u otras "
                "causas no tumorales. Compare siempre su resultado con el rango de su laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de prolactina alta (hiperprolactinemia)",
            body_html=(
                "<p>La <strong>hiperprolactinemia</strong> puede deberse a múltiples causas. Las más "
                "frecuentes son:</p>"
                "<ul>"
                "<li><strong>Prolactinoma (adenoma hipofisario):</strong> Tumor benigno secretor de "
                "prolactina; es la causa patológica más común. Se clasifica en microprolactinoma "
                "(&lt;10&nbsp;mm) y macroprolactinoma (&ge;10&nbsp;mm).</li>"
                "<li><strong>Fármacos:</strong> Antipsicóticos, metoclopramida, domperidona, ciertos "
                "antidepresivos y estrógenos. Los medicamentos son la primera causa no tumoral.</li>"
                "<li><strong>Hipotiroidismo:</strong> El déficit de hormona tiroidea eleva la TRH, que "
                "a su vez estimula la prolactina.</li>"
                "<li><strong>Irritación de la pared torácica:</strong> Herpes zóster, cirugía torácica "
                "o lesiones de la pared del tórax.</li>"
                "<li><strong>Síndrome de ovario poliquístico (SOP):</strong> Una proporción de mujeres "
                "con SOP presenta elevación leve.</li>"
                "<li><strong>Estrés y factores fisiológicos:</strong> Estrés intenso, sueño, ejercicio "
                "y estimulación del pezón.</li>"
                "<li><strong>Insuficiencia renal:</strong> La disminución del aclaramiento renal eleva "
                "los niveles séricos.</li>"
                "</ul>"
                "<p>Cuando la prolactina supera los 200&nbsp;ng/mL, la probabilidad de prolactinoma es "
                "alta. Entre 25 y 100&nbsp;ng/mL deben investigarse primero fármacos, hipotiroidismo y "
                "otras causas no tumorales.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de prolactina alta",
            body_html=(
                "<p>Los síntomas varían según el sexo. En mujeres los signos más frecuentes son:</p>"
                "<ul>"
                "<li><strong>Irregularidades menstruales:</strong> Oligomenorrea o amenorrea es el "
                "síntoma más característico.</li>"
                "<li><strong>Galactorrea:</strong> Secreción lechosa por el pezón fuera del embarazo "
                "o la lactancia.</li>"
                "<li><strong>Infertilidad:</strong> La prolactina elevada suprime la ovulación.</li>"
                "</ul>"
                "<p>En hombres, los síntomas suelen reconocerse más tarde:</p>"
                "<ul>"
                "<li><strong>Disminución de la libido:</strong> Por la caída secundaria de "
                "testosterona.</li>"
                "<li><strong>Disfunción eréctil:</strong> La prolactina alta altera la pulsatilidad "
                "de GnRH, provocando hipogonadismo.</li>"
                "<li><strong>Ginecomastia y galactorrea (rara):</strong> Aumento del tejido mamario "
                "y, en raras ocasiones, secreción por el pezón.</li>"
                "</ul>"
                "<p>En ambos sexos, un macroprolactinoma puede provocar <strong>cefalea</strong> y "
                "<strong>defectos del campo visual</strong> (hemianopsia bitemporal) por compresión "
                "del quiasma óptico.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Pruebas relacionadas",
            body_html=(
                "<p>Ante una prolactina elevada, se solicitan pruebas adicionales:</p>"
                "<ul>"
                "<li><strong>TSH:</strong> Descarta hipotiroidismo como causa.</li>"
                "<li><strong>LH y FSH:</strong> Evalúan la función reproductiva.</li>"
                "<li><strong>Prueba de embarazo (beta-hCG):</strong> Imprescindible en mujeres en "
                "edad fértil.</li>"
                "<li><strong>RM hipofisaria:</strong> Estudio de imagen de elección para detectar "
                "un prolactinoma.</li>"
                "<li><strong>Testosterona (en hombres):</strong> Para valorar hipogonadismo.</li>"
                "<li><strong>Macroprolactina:</strong> Descarta falsos positivos por complejos de "
                "inmunoglobulinas.</li>"
                "</ul>"
                "<p>La interpretación conjunta de estos análisis es esencial para establecer un "
                "diagnóstico preciso y planificar el tratamiento adecuado.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Consulte a un endocrinólogo o ginecólogo si:</p>"
                "<ul>"
                "<li>Su análisis muestra prolactina por encima del rango de referencia</li>"
                "<li>Presenta irregularidades menstruales o amenorrea sin explicación</li>"
                "<li>Nota secreción mamaria fuera del embarazo o la lactancia</li>"
                "<li>Tiene disminución de la libido, disfunción eréctil o infertilidad</li>"
                "<li>Sufre cefaleas persistentes y/o alteraciones visuales</li>"
                "</ul>"
                "<p>El diagnóstico precoz es clave en el prolactinoma. Los microprolactinomas responden "
                "muy bien a agonistas dopaminérgicos (cabergolina, bromocriptina) y rara vez necesitan "
                "cirugía. Sin tratamiento, los macroprolactinomas pueden crecer y causar complicaciones "
                "graves como pérdida de visión e hipopituitarismo.</p>"
                "<p>Si la elevación es farmacológica, cambiar o ajustar la medicación suele resolver el "
                "problema. No suspenda nunca un medicamento por su cuenta; consúltelo siempre con su "
                "médico.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo le ayuda NoryaAI con sus resultados de prolactina",
            body_html=(
                "<p><strong>NoryaAI</strong> analiza su informe completo de análisis de sangre, incluida "
                "la prolactina, teniendo en cuenta su edad, sexo y contexto clínico. Nuestro sistema "
                "basado en IA resalta los valores fuera de rango, resume las posibles causas y sugiere "
                "preguntas para su médico.</p>"
                "<p>¿Listo para comenzar? <a href=\"/analyze\">Suba su informe de laboratorio</a> para un "
                "análisis instantáneo. Visite nuestra <a href=\"/pricing\">página de precios</a> para "
                "conocer los planes disponibles. NoryaAI no sustituye al médico; nuestro objetivo es "
                "empoderarle con información para que su próxima consulta sea más productiva.</p>"
                "<p>Si su prolactina está fuera del rango normal, no se alarme: la mayoría de las causas "
                "tienen tratamiento. Lo más importante es compartir sus resultados con un profesional "
                "sanitario cualificado.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso legal",
            body_html=(
                "<p><strong>Este contenido es meramente informativo y no constituye consejo médico, "
                "diagnóstico ni tratamiento.</strong> Consulte siempre sus resultados con un profesional "
                "sanitario cualificado. NoryaAI no sustituye una consulta médica. Tome todas las "
                "decisiones de salud en consulta con su médico. "
                '<a href="/analyze">Visite nuestra página de análisis</a> para obtener información '
                "preliminar sobre sus resultados.</p>"
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
            heading="Prolaktin-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Wenn Ihr Laborbericht einen auffälligen <strong>Prolaktin</strong>-Wert zeigt, fragen "
                "Sie sich wahrscheinlich, welche Rolle dieses Hormon spielt und ob Sie sich Sorgen machen "
                "sollten. Prolaktin ist ein Peptidhormon, das im Hypophysenvorderlappen gebildet wird und "
                "vor allem für die Milchproduktion bekannt ist, aber auch Reproduktion, Immunfunktion und "
                "Stoffwechsel bei Frauen und Männern beeinflusst.</p>"
                "<p>Dieser Ratgeber erklärt, was der <strong>Prolaktin-Bluttest</strong> misst, welche "
                "Referenzbereiche gelten, welche Ursachen <strong>erhöhtes Prolaktin</strong> "
                "(Hyperprolaktinämie) haben kann, welche Symptome auftreten und wann Sie einen Arzt "
                "aufsuchen sollten. Unser Ziel ist es nicht, eine Diagnose zu stellen, sondern Ihnen zu "
                "helfen, Ihre Ergebnisse besser zu verstehen.</p>"
                "<p>Abnormale Prolaktinwerte können bei Frauen zu Zyklusstörungen und Unfruchtbarkeit, "
                "bei Männern zu sexueller Dysfunktion führen. Die gute Nachricht: Die meisten Ursachen "
                "einer Hyperprolaktinämie sind behandelbar, sobald sie korrekt identifiziert werden.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Was ist Prolaktin?",
            body_html=(
                "<p><strong>Prolaktin</strong> ist ein 199 Aminosäuren langes Polypeptidhormon, das von "
                "den laktotropen Zellen des Hypophysenvorderlappens synthetisiert wird. Obwohl sein Name "
                "&bdquo;für die Milch&ldquo; bedeutet, reichen seine Funktionen weit über die Laktation "
                "hinaus: Regulation der Reproduktion, Immunmodulation und osmotisches Gleichgewicht.</p>"
                "<p>Die Prolaktinsekretion wird hauptsächlich durch <strong>Dopamin</strong> aus dem "
                "Hypothalamus gehemmt. Sinkt der Dopaminspiegel oder werden Dopaminrezeptoren blockiert, "
                "steigt Prolaktin an. Damit ist Prolaktin unter den Hypophysenhormonen ungewöhnlich — es "
                "steht unter tonischer Hemmung und steigt an, sobald die Bremse gelöst wird.</p>"
                "<p>Sowohl Frauen als auch Männer haben messbares Prolaktin im Blut. In Schwangerschaft "
                "und Stillzeit steigt es physiologisch stark an. Erhöhungen außerhalb dieser Situationen "
                "sollten abgeklärt werden, da sie auf ein Hypophysenadenom, eine Medikamentennebenwirkung "
                "oder eine andere Grunderkrankung hinweisen können.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Prolaktinwerte (Referenzbereiche)",
            body_html=(
                "<p>Prolaktin wird mit einer einfachen Blutentnahme bestimmt. Die folgende Tabelle zeigt "
                "die gängigen Referenzbereiche:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Nicht schwangere Frauen</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Schwangere Frauen</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>Prolaktin folgt einem zirkadianen Rhythmus — es erreicht seinen Höchstwert im Schlaf "
                "und fällt einige Stunden nach dem Aufwachen ab. Die Blutentnahme erfolgt daher meist "
                "morgens, 2&ndash;3&nbsp;Stunden nach dem Aufstehen. Stress, intensiver Sport und "
                "proteinreiche Mahlzeiten können vorübergehende Anstiege verursachen.</p>"
                "<p>Werte über 200&nbsp;ng/mL deuten stark auf ein <strong>Prolaktinom</strong> hin. "
                "Werte zwischen 25 und 100&nbsp;ng/mL sind häufiger mit Medikamenten, Hypothyreose oder "
                "anderen nicht-tumorbedingten Ursachen assoziiert. Vergleichen Sie Ihr Ergebnis immer "
                "mit dem Referenzbereich Ihres Labors.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen von erhöhtem Prolaktin (Hyperprolaktinämie)",
            body_html=(
                "<p>Eine <strong>Hyperprolaktinämie</strong> kann zahlreiche Ursachen haben. Die "
                "häufigsten sind:</p>"
                "<ul>"
                "<li><strong>Prolaktinom (Hypophysenadenom):</strong> Ein gutartiger, "
                "prolaktinproduzierender Tumor der Hypophyse — die häufigste pathologische Ursache. "
                "Unterschieden werden Mikroprolaktinome (&lt;10&nbsp;mm) und Makroprolaktinome "
                "(&ge;10&nbsp;mm).</li>"
                "<li><strong>Medikamente:</strong> Antipsychotika, Metoclopramid, Domperidon, bestimmte "
                "Antidepressiva und Östrogenpräparate. Medikamente sind die häufigste nicht-tumorbedingte "
                "Ursache.</li>"
                "<li><strong>Hypothyreose:</strong> Ein Schilddrüsenhormonmangel erhöht TRH, das "
                "wiederum Prolaktin stimuliert.</li>"
                "<li><strong>Brustwandreizung:</strong> Herpes Zoster, Thoraxoperationen oder "
                "Brustwandläsionen können Prolaktin über Reflexwege erhöhen.</li>"
                "<li><strong>Polyzystisches Ovarialsyndrom (PCOS):</strong> Ein Teil der betroffenen "
                "Frauen zeigt eine leichte Prolaktinerhöhung.</li>"
                "<li><strong>Stress und physiologische Faktoren:</strong> Intensiver Stress, Schlaf, "
                "Sport und Brustwarzenreizung.</li>"
                "<li><strong>Niereninsuffizienz:</strong> Verringerte renale Clearance führt zu "
                "erhöhten Serumspiegeln.</li>"
                "</ul>"
                "<p>Liegt Prolaktin über 200&nbsp;ng/mL, ist ein Prolaktinom sehr wahrscheinlich. Bei "
                "Werten zwischen 25 und 100&nbsp;ng/mL sollten zunächst Medikamente, Hypothyreose und "
                "andere nicht-tumorbedingte Ursachen abgeklärt werden.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome eines erhöhten Prolaktins",
            body_html=(
                "<p>Die Symptome unterscheiden sich je nach Geschlecht. Bei Frauen sind die häufigsten "
                "Anzeichen:</p>"
                "<ul>"
                "<li><strong>Zyklusstörungen:</strong> Oligomenorrhoe (seltene Regelblutung) oder "
                "Amenorrhoe (Ausbleiben der Regel) ist das Leitsymptom.</li>"
                "<li><strong>Galaktorrhoe:</strong> Milchige Sekretion aus der Brustwarze außerhalb "
                "von Schwangerschaft und Stillzeit.</li>"
                "<li><strong>Infertilität:</strong> Erhöhtes Prolaktin unterdrückt den Eisprung.</li>"
                "</ul>"
                "<p>Bei Männern werden die Symptome oft später erkannt:</p>"
                "<ul>"
                "<li><strong>Libidoverlust:</strong> Durch den sekundären Testosteronabfall.</li>"
                "<li><strong>Erektile Dysfunktion:</strong> Hohes Prolaktin stört die GnRH-Pulsatilität "
                "und führt zu Hypogonadismus.</li>"
                "<li><strong>Gynäkomastie und selten Galaktorrhoe:</strong> Vergrößerung des "
                "Brustdrüsengewebes und in seltenen Fällen Sekretion.</li>"
                "</ul>"
                "<p>Bei beiden Geschlechtern kann ein Makroprolaktinom <strong>Kopfschmerzen</strong> und "
                "<strong>Gesichtsfelddefekte</strong> (bitemporale Hemianopsie) durch Kompression des "
                "Chiasma opticum verursachen.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Verwandte Untersuchungen",
            body_html=(
                "<p>Bei erhöhtem Prolaktin werden ergänzende Tests angeordnet:</p>"
                "<ul>"
                "<li><strong>TSH:</strong> Schließt Hypothyreose als Ursache aus.</li>"
                "<li><strong>LH und FSH:</strong> Beurteilen die Fortpflanzungsfunktion.</li>"
                "<li><strong>Schwangerschaftstest (Beta-hCG):</strong> Bei Frauen im gebärfähigen "
                "Alter obligatorisch.</li>"
                "<li><strong>MRT der Hypophyse:</strong> Goldstandard-Bildgebung bei "
                "Prolaktinomverdacht.</li>"
                "<li><strong>Testosteron (bei Männern):</strong> Gesamt- und freies Testosteron zur "
                "Hypogonadismus-Beurteilung.</li>"
                "<li><strong>Makroprolaktin-Screening:</strong> Schließt falsch-positive Ergebnisse "
                "durch Immunglobulin-Komplexe aus.</li>"
                "</ul>"
                "<p>Die gemeinsame Bewertung dieser Tests ist entscheidend für eine präzise Diagnose "
                "und eine angemessene Therapieplanung.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Suchen Sie einen Endokrinologen oder Gynäkologen auf, wenn:</p>"
                "<ul>"
                "<li>Ihr Bluttest einen Prolaktinwert über dem Referenzbereich zeigt</li>"
                "<li>Sie unerklärliche Zyklusstörungen oder Amenorrhoe haben</li>"
                "<li>Sie außerhalb von Schwangerschaft oder Stillzeit Brustsekretion bemerken</li>"
                "<li>Sie unter Libidoverlust, erektiler Dysfunktion oder Unfruchtbarkeit leiden</li>"
                "<li>Sie anhaltende Kopfschmerzen und/oder Sehstörungen haben</li>"
                "</ul>"
                "<p>Frühzeitige Diagnose ist besonders beim Prolaktinom wichtig. Mikroprolaktinome "
                "sprechen sehr gut auf Dopaminagonisten (Cabergolin, Bromocriptin) an und erfordern "
                "selten eine Operation. Unbehandelt können Makroprolaktinome wachsen und schwere "
                "Komplikationen wie Sehverlust und Hypopituitarismus verursachen.</p>"
                "<p>Ist die Erhöhung medikamentenbedingt, löst ein Wechsel oder eine Dosisanpassung "
                "das Problem meist. Setzen Sie ein verordnetes Medikament jedoch nie eigenständig ab "
                "— besprechen Sie Änderungen immer mit Ihrem Arzt.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie NoryaAI Ihnen bei Prolaktin-Ergebnissen hilft",
            body_html=(
                "<p><strong>NoryaAI</strong> analysiert Ihren vollständigen Bluttestbericht — "
                "einschließlich Prolaktin — unter Berücksichtigung von Alter, Geschlecht und klinischem "
                "Kontext. Unser KI-gestütztes System hebt auffällige Werte hervor, fasst mögliche "
                "Ursachen zusammen und schlägt Fragen vor, die Sie Ihrem Arzt stellen können.</p>"
                "<p>Bereit loszulegen? <a href=\"/analyze\">Laden Sie Ihren Laborbericht hoch</a> für "
                "eine sofortige Analyse. Besuchen Sie unsere <a href=\"/pricing\">Preisseite</a>, um die "
                "verfügbaren Pläne zu entdecken. NoryaAI ersetzt keinen Arzt — unser Ziel ist es, Sie "
                "mit Wissen auszustatten, damit Ihr nächster Arztbesuch produktiver wird.</p>"
                "<p>Wenn Ihr Prolaktinwert außerhalb des Normalbereichs liegt, geraten Sie nicht in "
                "Panik — viele Ursachen sind behandelbar. Der wichtigste Schritt ist, Ihre Ergebnisse "
                "mit einer qualifizierten Fachkraft zu besprechen.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Haftungsausschluss",
            body_html=(
                "<p><strong>Dieser Inhalt dient ausschließlich Informationszwecken und stellt keine "
                "medizinische Beratung, Diagnose oder Behandlung dar.</strong> Besprechen Sie Ihre "
                "Blutwerte stets mit einer qualifizierten medizinischen Fachkraft. NoryaAI ersetzt "
                "keine ärztliche Konsultation. Treffen Sie alle gesundheitsbezogenen Entscheidungen "
                "in Absprache mit Ihrem Arzt. "
                '<a href="/analyze">Besuchen Sie unsere Analyseseite</a> für erste Einblicke in Ihre '
                "Ergebnisse.</p>"
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
            heading="Analyse de la prolactine : que signifient vos résultats ?",
            body_html=(
                "<p>Si votre bilan sanguin révèle un taux anormal de <strong>prolactine</strong>, il est "
                "naturel de se demander à quoi sert cette hormone et si vous devez vous inquiéter. La "
                "prolactine est une hormone peptidique produite par l&rsquo;antéhypophyse, principalement "
                "connue pour stimuler la production de lait maternel, mais elle influence aussi la "
                "reproduction, l&rsquo;immunité et le métabolisme chez la femme comme chez l&rsquo;homme.</p>"
                "<p>Ce guide explique ce que mesure le <strong>dosage de la prolactine</strong>, les "
                "valeurs de référence normales, les causes fréquentes d&rsquo;une <strong>prolactine "
                "élevée</strong> (hyperprolactinémie), les symptômes associés et quand consulter. Notre "
                "objectif n&rsquo;est pas de poser un diagnostic mais de vous aider à comprendre vos "
                "résultats pour un échange plus productif avec votre médecin.</p>"
                "<p>Un taux anormal de prolactine peut entraîner des troubles du cycle et une infertilité "
                "chez la femme, et un dysfonctionnement sexuel chez l&rsquo;homme. La bonne nouvelle est "
                "que la plupart des causes d&rsquo;hyperprolactinémie sont traitables une fois "
                "correctement identifiées.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Qu&rsquo;est-ce que la prolactine ?",
            body_html=(
                "<p>La <strong>prolactine</strong> est un polypeptide de 199 acides aminés synthétisé par "
                "les cellules lactotropes de l&rsquo;antéhypophyse. Bien que son nom signifie "
                "&laquo;&nbsp;pour le lait&nbsp;&raquo;, ses fonctions dépassent largement la lactation : "
                "régulation de la reproduction, modulation immunitaire et équilibre osmotique.</p>"
                "<p>La sécrétion de prolactine est principalement inhibée par la <strong>dopamine</strong> "
                "hypothalamique. Lorsque la dopamine diminue ou que ses récepteurs sont bloqués, la "
                "prolactine augmente. Cela fait de la prolactine une hormone atypique : elle est sous "
                "inhibition tonique, c&rsquo;est-à-dire qu&rsquo;elle augmente dès que son frein est "
                "relâché.</p>"
                "<p>Femmes et hommes ont un taux mesurable de prolactine dans le sang. Pendant la "
                "grossesse et l&rsquo;allaitement, la prolactine augmente physiologiquement. En dehors "
                "de ces situations, une élévation mérite une investigation car elle peut révéler un "
                "adénome hypophysaire, un effet médicamenteux ou une autre pathologie.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de prolactine (intervalles de référence)",
            body_html=(
                "<p>La prolactine est mesurée par une simple prise de sang. Le tableau ci-dessous "
                "présente les intervalles de référence courants :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Valeurs normales (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes non enceintes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes enceintes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>La prolactine suit un rythme circadien : elle atteint son pic durant le sommeil et "
                "redescend quelques heures après le réveil. Le prélèvement se fait donc le matin, "
                "2&ndash;3&nbsp;heures après le lever. Le stress, l&rsquo;exercice intense et les repas "
                "riches en protéines peuvent provoquer des élévations passagères.</p>"
                "<p>Un taux supérieur à 200&nbsp;ng/mL oriente fortement vers un "
                "<strong>prolactinome</strong>. Entre 25 et 100&nbsp;ng/mL, les médicaments, "
                "l&rsquo;hypothyroïdie et d&rsquo;autres causes non tumorales sont à explorer en "
                "priorité. Comparez toujours votre résultat avec l&rsquo;intervalle de votre "
                "laboratoire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d&rsquo;une prolactine élevée (hyperprolactinémie)",
            body_html=(
                "<p>L&rsquo;<strong>hyperprolactinémie</strong> peut avoir de nombreuses origines. "
                "Les plus fréquentes sont :</p>"
                "<ul>"
                "<li><strong>Prolactinome (adénome hypophysaire) :</strong> Tumeur bénigne sécrétant "
                "de la prolactine — cause pathologique la plus courante. On distingue le "
                "microprolactinome (&lt;10&nbsp;mm) du macroprolactinome (&ge;10&nbsp;mm).</li>"
                "<li><strong>Médicaments :</strong> Antipsychotiques, métoclopramide, dompéridone, "
                "certains antidépresseurs et &oelig;strogènes. Les médicaments sont la première cause "
                "non tumorale.</li>"
                "<li><strong>Hypothyroïdie :</strong> Le déficit en hormones thyroïdiennes élève la TRH, "
                "qui stimule à son tour la prolactine.</li>"
                "<li><strong>Irritation de la paroi thoracique :</strong> Zona, chirurgie thoracique ou "
                "lésions pariétales.</li>"
                "<li><strong>Syndrome des ovaires polykystiques (SOPK) :</strong> Élévation légère chez "
                "une partie des femmes concernées.</li>"
                "<li><strong>Stress et facteurs physiologiques :</strong> Stress intense, sommeil, "
                "exercice, stimulation mamelonnaire.</li>"
                "<li><strong>Insuffisance rénale :</strong> La diminution de la clairance rénale "
                "augmente les taux sériques.</li>"
                "</ul>"
                "<p>Au-delà de 200&nbsp;ng/mL, la probabilité d&rsquo;un prolactinome est élevée. Entre "
                "25 et 100&nbsp;ng/mL, médicaments, hypothyroïdie et autres causes non tumorales doivent "
                "être recherchés en premier.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d&rsquo;une prolactine élevée",
            body_html=(
                "<p>Les symptômes varient selon le sexe. Chez la femme, les signes les plus fréquents "
                "sont :</p>"
                "<ul>"
                "<li><strong>Troubles du cycle :</strong> Oligoménorrhée ou aménorrhée, signe le plus "
                "caractéristique.</li>"
                "<li><strong>Galactorrhée :</strong> Écoulement laiteux du mamelon en dehors de la "
                "grossesse ou de l&rsquo;allaitement.</li>"
                "<li><strong>Infertilité :</strong> La prolactine élevée inhibe l&rsquo;ovulation.</li>"
                "</ul>"
                "<p>Chez l&rsquo;homme, les symptômes sont souvent reconnus tardivement :</p>"
                "<ul>"
                "<li><strong>Baisse de la libido :</strong> Liée à la chute secondaire de "
                "testostérone.</li>"
                "<li><strong>Dysfonction érectile :</strong> La prolactine élevée perturbe la "
                "pulsatilité de la GnRH, entraînant un hypogonadisme.</li>"
                "<li><strong>Gynécomastie et rarement galactorrhée :</strong> Augmentation du tissu "
                "mammaire et, rarement, écoulement mamelonnaire.</li>"
                "</ul>"
                "<p>Dans les deux sexes, un macroprolactinome peut provoquer des "
                "<strong>céphalées</strong> et des <strong>déficits du champ visuel</strong> "
                "(hémianopsie bitemporale) par compression du chiasma optique.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Examens complémentaires",
            body_html=(
                "<p>Face à une prolactine élevée, des examens supplémentaires sont prescrits :</p>"
                "<ul>"
                "<li><strong>TSH :</strong> Exclut l&rsquo;hypothyroïdie comme cause.</li>"
                "<li><strong>LH et FSH :</strong> Évaluent la fonction reproductive.</li>"
                "<li><strong>Test de grossesse (bêta-hCG) :</strong> Indispensable chez la femme en "
                "âge de procréer.</li>"
                "<li><strong>IRM hypophysaire :</strong> Examen d&rsquo;imagerie de référence pour "
                "détecter un prolactinome.</li>"
                "<li><strong>Testostérone (chez l&rsquo;homme) :</strong> Testostérone totale et libre "
                "pour évaluer un hypogonadisme.</li>"
                "<li><strong>Macroprolactine :</strong> Élimine les faux positifs liés à des complexes "
                "d&rsquo;immunoglobulines.</li>"
                "</ul>"
                "<p>L&rsquo;interprétation conjointe de ces examens est essentielle pour un diagnostic "
                "précis et une prise en charge appropriée.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez un endocrinologue ou un gynécologue si :</p>"
                "<ul>"
                "<li>Votre bilan montre une prolactine au-dessus de l&rsquo;intervalle de référence</li>"
                "<li>Vous présentez des troubles du cycle ou une aménorrhée inexpliqués</li>"
                "<li>Vous observez un écoulement mamelonnaire en dehors de la grossesse ou de "
                "l&rsquo;allaitement</li>"
                "<li>Vous souffrez de baisse de libido, de dysfonction érectile ou d&rsquo;infertilité</li>"
                "<li>Vous avez des céphalées persistantes et/ou des troubles visuels</li>"
                "</ul>"
                "<p>Le diagnostic précoce est particulièrement important en cas de prolactinome. Les "
                "microprolactinomes répondent très bien aux agonistes dopaminergiques (cabergoline, "
                "bromocriptine) et nécessitent rarement une chirurgie. Non traités, les "
                "macroprolactinomes peuvent croître et entraîner des complications graves comme une "
                "perte de vision et un hypopituitarisme.</p>"
                "<p>Si l&rsquo;élévation est d&rsquo;origine médicamenteuse, un changement ou un "
                "ajustement du traitement résout généralement le problème. Ne cessez jamais un "
                "médicament de votre propre initiative — discutez toujours avec votre médecin.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment NoryaAI vous aide avec vos résultats de prolactine",
            body_html=(
                "<p><strong>NoryaAI</strong> analyse l&rsquo;ensemble de votre bilan sanguin, y compris "
                "la prolactine, en tenant compte de votre âge, de votre sexe et de votre contexte "
                "clinique. Notre système d&rsquo;IA met en évidence les valeurs hors normes, résume les "
                "causes possibles et suggère des questions à poser à votre médecin.</p>"
                "<p>Prêt à commencer ? <a href=\"/analyze\">Téléchargez votre bilan</a> pour une analyse "
                "instantanée. Consultez notre <a href=\"/pricing\">page tarifs</a> pour découvrir nos "
                "formules. NoryaAI ne remplace pas un médecin ; notre objectif est de vous armer "
                "d&rsquo;informations pour que votre prochaine consultation soit plus productive.</p>"
                "<p>Si votre prolactine est en dehors des normes, ne paniquez pas — la plupart des "
                "causes sont traitables. L&rsquo;étape la plus importante est de partager vos résultats "
                "avec un professionnel de santé qualifié.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                "<p><strong>Ce contenu est fourni à titre informatif uniquement et ne constitue pas un "
                "avis médical, un diagnostic ou un traitement.</strong> Discutez toujours de vos "
                "résultats avec un professionnel de santé qualifié. NoryaAI ne remplace pas une "
                "consultation médicale. Prenez toutes vos décisions de santé en concertation avec "
                'votre médecin. <a href="/analyze">Visitez notre page d&rsquo;analyse</a> pour des '
                "informations préliminaires sur vos résultats.</p>"
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
            heading="Esame della prolattina: cosa significano i risultati",
            body_html=(
                "<p>Se il referto del vostro esame del sangue mostra un livello anomalo di "
                "<strong>prolattina</strong>, è naturale chiedersi cosa significhi e se ci sia motivo "
                "di preoccupazione. La prolattina è un ormone peptidico prodotto dall&rsquo;ipofisi "
                "anteriore, noto soprattutto per stimolare la produzione di latte materno, ma "
                "influenza anche la riproduzione, l&rsquo;immunità e il metabolismo sia nelle donne "
                "che negli uomini.</p>"
                "<p>Questa guida spiega cosa misura l&rsquo;esame della <strong>prolattina</strong>, i "
                "valori di riferimento normali, le cause più comuni di <strong>prolattina alta</strong> "
                "(iperprolattinemia), i sintomi associati e quando consultare il medico. Il nostro "
                "obiettivo non è formulare una diagnosi, ma aiutarvi a comprendere i risultati per un "
                "colloquio più produttivo con il vostro medico.</p>"
                "<p>Livelli anomali di prolattina possono causare irregolarità mestruali e infertilità "
                "nella donna, e disfunzione sessuale nell&rsquo;uomo. La buona notizia è che la "
                "maggior parte delle cause di iperprolattinemia è trattabile una volta correttamente "
                "identificata.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="Che cos&rsquo;è la prolattina?",
            body_html=(
                "<p>La <strong>prolattina</strong> è un polipeptide di 199 amminoacidi sintetizzato dalle "
                "cellule lattotrope dell&rsquo;ipofisi anteriore. Sebbene il nome significhi "
                "&laquo;a favore del latte&raquo;, le sue funzioni vanno ben oltre la lattazione: "
                "regolazione della funzione riproduttiva, modulazione immunitaria e equilibrio "
                "osmotico.</p>"
                "<p>La secrezione di prolattina è controllata principalmente dalla "
                "<strong>dopamina</strong> ipotalamica, che funge da fattore inibitore. Quando la "
                "dopamina diminuisce o i suoi recettori vengono bloccati, la prolattina sale. Ciò rende "
                "la prolattina insolita tra gli ormoni ipofisari: è sotto inibizione tonica, cioè "
                "aumenta ogni volta che il suo freno viene rilasciato.</p>"
                "<p>Sia le donne sia gli uomini hanno livelli misurabili di prolattina circolante. "
                "Durante la gravidanza e l&rsquo;allattamento la prolattina sale fisiologicamente. "
                "Elevazioni al di fuori di questi contesti meritano indagini perché possono indicare un "
                "adenoma ipofisario, un effetto farmacologico o un&rsquo;altra condizione.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali della prolattina (intervalli di riferimento)",
            body_html=(
                "<p>La prolattina viene misurata con un semplice prelievo di sangue. La tabella seguente "
                "mostra gli intervalli di riferimento comunemente accettati:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne non in gravidanza</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne in gravidanza</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>La prolattina segue un ritmo circadiano: raggiunge il picco durante il sonno e scende "
                "alcune ore dopo il risveglio. Il prelievo viene quindi effettuato al mattino, "
                "2&ndash;3&nbsp;ore dopo essersi alzati. Stress, esercizio intenso e pasti ricchi di "
                "proteine possono causare innalzamenti transitori.</p>"
                "<p>Valori superiori a 200&nbsp;ng/mL orientano fortemente verso un "
                "<strong>prolattinoma</strong>. Tra 25 e 100&nbsp;ng/mL è più comune l&rsquo;associazione "
                "con farmaci, ipotiroidismo o altre cause non tumorali. Confrontate sempre il vostro "
                "risultato con l&rsquo;intervallo del vostro laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di prolattina alta (iperprolattinemia)",
            body_html=(
                "<p>L&rsquo;<strong>iperprolattinemia</strong> può avere numerose cause. Le più "
                "frequenti sono:</p>"
                "<ul>"
                "<li><strong>Prolattinoma (adenoma ipofisario):</strong> Tumore benigno che secerne "
                "prolattina — la causa patologica più comune. Si distinguono microprolattinomi "
                "(&lt;10&nbsp;mm) e macroprolattinomi (&ge;10&nbsp;mm).</li>"
                "<li><strong>Farmaci:</strong> Antipsicotici, metoclopramide, domperidone, alcuni "
                "antidepressivi ed estrogeni. I farmaci sono la prima causa non tumorale.</li>"
                "<li><strong>Ipotiroidismo:</strong> Il deficit di ormone tiroideo aumenta il TRH, "
                "che a sua volta stimola la prolattina.</li>"
                "<li><strong>Irritazione della parete toracica:</strong> Herpes zoster, chirurgia "
                "toracica o lesioni parietali.</li>"
                "<li><strong>Sindrome dell&rsquo;ovaio policistico (PCOS):</strong> Una parte delle "
                "donne affette presenta un&rsquo;elevazione lieve.</li>"
                "<li><strong>Stress e fattori fisiologici:</strong> Stress intenso, sonno, esercizio, "
                "stimolazione del capezzolo.</li>"
                "<li><strong>Insufficienza renale:</strong> La ridotta clearance renale aumenta i "
                "livelli sierici.</li>"
                "</ul>"
                "<p>Quando la prolattina supera 200&nbsp;ng/mL, la probabilità di prolattinoma è "
                "elevata. Tra 25 e 100&nbsp;ng/mL vanno indagati prima farmaci, ipotiroidismo e altre "
                "cause non tumorali.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi di prolattina alta",
            body_html=(
                "<p>I sintomi variano in base al sesso. Nella donna i segni più frequenti sono:</p>"
                "<ul>"
                "<li><strong>Irregolarità mestruali:</strong> Oligomenorrea o amenorrea è il sintomo "
                "più caratteristico.</li>"
                "<li><strong>Galattorrea:</strong> Secrezione lattescente dal capezzolo al di fuori "
                "della gravidanza o dell&rsquo;allattamento.</li>"
                "<li><strong>Infertilità:</strong> La prolattina elevata sopprime l&rsquo;ovulazione.</li>"
                "</ul>"
                "<p>Nell&rsquo;uomo i sintomi vengono spesso riconosciuti più tardi:</p>"
                "<ul>"
                "<li><strong>Calo della libido:</strong> Dovuto alla diminuzione secondaria del "
                "testosterone.</li>"
                "<li><strong>Disfunzione erettile:</strong> La prolattina elevata altera la pulsatilità "
                "del GnRH, causando ipogonadismo.</li>"
                "<li><strong>Ginecomastia e raramente galattorrea:</strong> Aumento del tessuto "
                "mammario e, in rari casi, secrezione dal capezzolo.</li>"
                "</ul>"
                "<p>In entrambi i sessi, un macroprolattinoma può provocare <strong>cefalea</strong> e "
                "<strong>difetti del campo visivo</strong> (emianopsia bitemporale) per compressione del "
                "chiasma ottico.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Esami correlati",
            body_html=(
                "<p>In caso di prolattina elevata vengono prescritti esami aggiuntivi:</p>"
                "<ul>"
                "<li><strong>TSH:</strong> Esclude l&rsquo;ipotiroidismo come causa.</li>"
                "<li><strong>LH e FSH:</strong> Valutano la funzione riproduttiva.</li>"
                "<li><strong>Test di gravidanza (beta-hCG):</strong> Obbligatorio nelle donne in età "
                "fertile.</li>"
                "<li><strong>RM ipofisaria:</strong> Esame di imaging di riferimento per rilevare un "
                "prolattinoma.</li>"
                "<li><strong>Testosterone (nell&rsquo;uomo):</strong> Testosterone totale e libero per "
                "valutare un ipogonadismo.</li>"
                "<li><strong>Macroprolattina:</strong> Esclude falsi positivi da complessi "
                "immunoglobulinici.</li>"
                "</ul>"
                "<p>L&rsquo;interpretazione congiunta di questi esami è essenziale per una diagnosi "
                "accurata e una pianificazione terapeutica adeguata.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Consultate un endocrinologo o un ginecologo se:</p>"
                "<ul>"
                "<li>Il vostro esame del sangue mostra prolattina superiore all&rsquo;intervallo di "
                "riferimento</li>"
                "<li>Avete irregolarità mestruali o amenorrea inspiegabili</li>"
                "<li>Notate secrezione dal capezzolo al di fuori della gravidanza o "
                "dell&rsquo;allattamento</li>"
                "<li>Soffrite di calo della libido, disfunzione erettile o infertilità</li>"
                "<li>Avete cefalea persistente e/o disturbi visivi</li>"
                "</ul>"
                "<p>La diagnosi precoce è particolarmente importante nel prolattinoma. I "
                "microprolattinomi rispondono molto bene agli agonisti dopaminergici (cabergolina, "
                "bromocriptina) e raramente necessitano di chirurgia. Senza trattamento, i "
                "macroprolattinomi possono crescere e causare complicanze gravi come perdita della vista "
                "e ipopituitarismo.</p>"
                "<p>Se l&rsquo;elevazione è farmaco-indotta, la modifica o l&rsquo;aggiustamento della "
                "terapia risolve generalmente il problema. Non sospendete mai un farmaco di vostra "
                "iniziativa — discutete sempre con il vostro medico.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come NoryaAI vi aiuta con i risultati della prolattina",
            body_html=(
                "<p><strong>NoryaAI</strong> analizza l&rsquo;intero referto del vostro esame del sangue "
                "— inclusa la prolattina — tenendo conto di età, sesso e contesto clinico. Il nostro "
                "sistema basato su IA evidenzia i valori fuori norma, riassume le possibili cause e "
                "suggerisce domande da porre al medico.</p>"
                "<p>Pronti a iniziare? <a href=\"/analyze\">Caricate il vostro referto</a> per "
                "un&rsquo;analisi istantanea. Visitate la nostra <a href=\"/pricing\">pagina prezzi</a> "
                "per scoprire i piani disponibili. NoryaAI non sostituisce il medico; il nostro obiettivo "
                "è fornirvi informazioni affinché la vostra prossima visita sia più produttiva.</p>"
                "<p>Se la vostra prolattina è fuori norma, non fatevi prendere dal panico — la maggior "
                "parte delle cause è trattabile. Il passo più importante è condividere i risultati con "
                "un professionista sanitario qualificato.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza",
            body_html=(
                "<p><strong>Questo contenuto è fornito a solo scopo informativo e non costituisce "
                "consulenza medica, diagnosi o trattamento.</strong> Discutete sempre i vostri risultati "
                "con un professionista sanitario qualificato. NoryaAI non sostituisce una visita medica. "
                "Prendete tutte le decisioni relative alla salute in consultazione con il vostro medico. "
                '<a href="/analyze">Visitate la nostra pagina di analisi</a> per informazioni '
                "preliminari sui vostri risultati.</p>"
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
            heading="בדיקת פרולקטין בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>אם תוצאות בדיקת הדם שלך מראות רמת <strong>פרולקטין</strong> חריגה, סביר שתרצו "
                "להבין מהו ההורמון הזה ומה המשמעות של הממצא. פרולקטין הוא הורמון פפטידי המיוצר "
                "באונה הקדמית של בלוטת יותרת המוח (ההיפופיזה), הידוע בעיקר בזכות תפקידו בייצור "
                "חלב אם, אך הוא משפיע גם על הפוריות, מערכת החיסון והמטבוליזם בנשים ובגברים כאחד.</p>"
                "<p>מדריך זה מסביר מה מודדת <strong>בדיקת פרולקטין</strong>, מהם טווחי הייחוס "
                "התקינים, הגורמים השכיחים ל<strong>פרולקטין גבוה</strong> (היפרפרולקטינמיה), "
                "התסמינים הנלווים ומתי כדאי לפנות לרופא. המטרה שלנו אינה לאבחן — אלא לעזור לכם "
                "להבין את התוצאות כדי שתוכלו לקיים שיחה פרודוקטיבית יותר עם הרופא שלכם.</p>"
                "<p>רמות פרולקטין חריגות עלולות לגרום להפרעות במחזור ולאי-פוריות בנשים, ולהפרעות "
                "בתפקוד המיני בגברים. החדשות הטובות הן שרוב הגורמים להיפרפרולקטינמיה ניתנים "
                "לטיפול לאחר זיהוי נכון.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="מהו פרולקטין?",
            body_html=(
                "<p><strong>פרולקטין</strong> הוא הורמון פוליפפטידי בן 199 חומצות אמינו, המיוצר "
                "על ידי תאים לקטוטרופיים באונה הקדמית של ההיפופיזה. למרות ששמו פירושו "
                "\"לטובת החלב\", תפקידיו חורגים הרבה מעבר להנקה — ויסות הפוריות, אפנון מערכת "
                "החיסון ושמירה על איזון אוסמוטי.</p>"
                "<p>הפרשת פרולקטין נשלטת בעיקר על ידי <strong>דופמין</strong> מההיפותלמוס, המשמש "
                "כגורם מעכב. כאשר רמות הדופמין יורדות או כשתרופות חוסמות את הקולטנים לדופמין, "
                "הפרולקטין עולה. זה הופך את הפרולקטין לחריג בין הורמוני ההיפופיזה — הוא תחת עיכוב "
                "טוני, כלומר הוא עולה בכל פעם שהבלם שלו משתחרר.</p>"
                "<p>גם לנשים וגם לגברים יש רמות מדידות של פרולקטין בדם. במהלך הריון והנקה, "
                "הפרולקטין עולה באופן פיזיולוגי. עליות מחוץ להקשרים אלה מצדיקות בירור כי הן עשויות "
                "להצביע על אדנומה של ההיפופיזה, תופעת לוואי תרופתית או מצב בסיסי אחר.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ייחוס תקינים של פרולקטין",
            body_html=(
                "<p>פרולקטין נמדד באמצעות בדיקת דם פשוטה. הטבלה הבאה מציגה את טווחי הייחוס "
                "המקובלים:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח תקין (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים שאינן בהריון</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים בהריון</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>לפרולקטין מקצב צירקדי — הוא מגיע לשיא בשינה ויורד כמה שעות לאחר ההתעוררות. "
                "לכן דגימת הדם נלקחת בדרך כלל בבוקר, 2–3 שעות לאחר ההתעוררות. מתח, פעילות גופנית "
                "אינטנסיבית וארוחות עתירות חלבון עלולים לגרום לעליות חולפות.</p>"
                "<p>ערכים מעל 200&nbsp;ng/mL מעלים חשד חזק ל<strong>פרולקטינומה</strong> (אדנומה "
                "מפרישת פרולקטין). ערכים בין 25 ל-100&nbsp;ng/mL קשורים לרוב לתרופות, תת-פעילות "
                "של בלוטת התריס או גורמים לא-גידוליים אחרים. השוו תמיד את התוצאה עם טווח "
                "הייחוס של המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לפרולקטין גבוה (היפרפרולקטינמיה)",
            body_html=(
                "<p><strong>היפרפרולקטינמיה</strong> יכולה לנבוע ממגוון סיבות. השכיחות ביותר הן:</p>"
                "<ul>"
                "<li><strong>פרולקטינומה (אדנומה של ההיפופיזה):</strong> גידול שפיר המפריש "
                "פרולקטין — הגורם הפתולוגי השכיח ביותר. מחולקת למיקרופרולקטינומה "
                "(&lt;10&nbsp;מ\"מ) ומקרופרולקטינומה (&ge;10&nbsp;מ\"מ).</li>"
                "<li><strong>תרופות:</strong> אנטי-פסיכוטיים (הלופרידול, ריספרידון), "
                "מטוקלופרמיד, דומפרידון, חלק מתרופות נוגדות דיכאון ואסטרוגנים. תרופות הן "
                "הגורם הלא-גידולי השכיח ביותר.</li>"
                "<li><strong>תת-פעילות בלוטת התריס:</strong> חסר בהורמון בלוטת התריס מעלה TRH, "
                "שבתורו מגרה הפרשת פרולקטין.</li>"
                "<li><strong>גירוי דופן בית החזה:</strong> הרפס זוסטר, ניתוחים בחזה או נגעים "
                "בדופן בית החזה.</li>"
                "<li><strong>תסמונת השחלות הפוליציסטיות (PCOS):</strong> חלק מהנשים עם PCOS "
                "מציגות עלייה קלה.</li>"
                "<li><strong>מתח וגורמים פיזיולוגיים:</strong> מתח חריף, שינה, פעילות גופנית "
                "וגירוי הפטמות.</li>"
                "<li><strong>אי-ספיקת כליות:</strong> ירידה בפינוי הכלייתי מעלה את רמות "
                "הסרום.</li>"
                "</ul>"
                "<p>כאשר הפרולקטין עולה מעל 200&nbsp;ng/mL, ההסתברות לפרולקטינומה גבוהה. בטווח "
                "25–100&nbsp;ng/mL יש לבדוק תחילה תרופות, תת-פעילות בלוטת התריס וגורמים "
                "לא-גידוליים אחרים.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של פרולקטין גבוה",
            body_html=(
                "<p>התסמינים שונים בין המינים. בנשים הסימנים השכיחים ביותר הם:</p>"
                "<ul>"
                "<li><strong>הפרעות במחזור:</strong> אוליגומנוריאה (מחזורים נדירים) או אמנוריאה "
                "(היעדר מחזור) — הסימפטום הבולט ביותר.</li>"
                "<li><strong>גלקטוריאה:</strong> הפרשה חלבית מהפטמה שלא בהריון או בהנקה.</li>"
                "<li><strong>אי-פוריות:</strong> פרולקטין גבוה מדכא את הביוץ.</li>"
                "</ul>"
                "<p>בגברים, התסמינים מזוהים לרוב מאוחר יותר:</p>"
                "<ul>"
                "<li><strong>ירידה בחשק המיני:</strong> כתוצאה מירידה משנית ברמת הטסטוסטרון.</li>"
                "<li><strong>הפרעות בזקפה:</strong> פרולקטין גבוה פוגע בפולסטיליות של GnRH וגורם "
                "להיפוגונדיזם.</li>"
                "<li><strong>גינקומסטיה ולעיתים נדירות גלקטוריאה:</strong> הגדלת רקמת השד "
                "ובמקרים נדירים הפרשה מהפטמה.</li>"
                "</ul>"
                "<p>בשני המינים, מקרופרולקטינומה עלולה לגרום ל<strong>כאבי ראש</strong> "
                "ול<strong>פגמים בשדה הראייה</strong> (המיאנופסיה ביטמפורלית) עקב לחץ על הכיאזמה "
                "האופטית.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="בדיקות קשורות",
            body_html=(
                "<p>כשמתגלה פרולקטין גבוה, נדרשות בדיקות נוספות לאיתור הסיבה:</p>"
                "<ul>"
                "<li><strong>TSH:</strong> שולל תת-פעילות בלוטת התריס כגורם.</li>"
                "<li><strong>LH ו-FSH:</strong> מעריכים את תפקוד מערכת הפוריות.</li>"
                "<li><strong>בדיקת הריון (בטא-hCG):</strong> חובה בנשים בגיל הפוריות.</li>"
                "<li><strong>MRI של ההיפופיזה:</strong> בדיקת ההדמיה המובילה לאיתור "
                "פרולקטינומה.</li>"
                "<li><strong>טסטוסטרון (בגברים):</strong> טסטוסטרון כולל וחופשי להערכת "
                "היפוגונדיזם.</li>"
                "<li><strong>מקרופרולקטין:</strong> שולל תוצאות חיוביות כוזבות הנובעות מקומפלקסים "
                "של אימונוגלובולינים.</li>"
                "</ul>"
                "<p>פרשנות משולבת של בדיקות אלה חיונית לאבחון מדויק ולתכנון טיפול מתאים.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>פנו לאנדוקרינולוג או לגינקולוג אם:</p>"
                "<ul>"
                "<li>בדיקת הדם שלכם מראה פרולקטין מעל טווח הייחוס</li>"
                "<li>אתם חווים הפרעות במחזור או אמנוריאה ללא הסבר</li>"
                "<li>אתם מבחינים בהפרשה מהפטמה שלא בהריון או בהנקה</li>"
                "<li>אתם סובלים מירידה בחשק המיני, הפרעות בזקפה או אי-פוריות</li>"
                "<li>אתם סובלים מכאבי ראש מתמשכים ו/או הפרעות בראייה</li>"
                "</ul>"
                "<p>אבחון מוקדם חשוב במיוחד בפרולקטינומה. מיקרופרולקטינומות מגיבות היטב "
                "לאגוניסטים דופמינרגיים (קברגולין, ברומוקריפטין) ולעיתים נדירות דורשות ניתוח. "
                "ללא טיפול, מקרופרולקטינומות עלולות לגדול ולגרום לסיבוכים חמורים כמו אובדן ראייה "
                "והיפופיטואיטריזם.</p>"
                "<p>אם העלייה נגרמת מתרופה, החלפה או התאמת מינון פותרת בדרך כלל את הבעיה. "
                "אל תפסיקו לעולם תרופה בכוחות עצמכם — היוועצו תמיד עם הרופא שלכם.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד NoryaAI עוזר לכם עם תוצאות הפרולקטין",
            body_html=(
                "<p><strong>NoryaAI</strong> מנתח את כל דוח בדיקת הדם שלכם — כולל פרולקטין — "
                "בהתחשב בגיל, מין והקשר קליני. מערכת הבינה המלאכותית שלנו מדגישה ערכים חריגים, "
                "מסכמת סיבות אפשריות ומציעה שאלות שאולי תרצו לשאול את הרופא.</p>"
                "<p>מוכנים להתחיל? <a href=\"/analyze\">העלו את דוח המעבדה שלכם</a> לניתוח מיידי. "
                "בקרו ב<a href=\"/pricing\">עמוד התמחור</a> שלנו לסקירת התוכניות הזמינות. NoryaAI "
                "אינו מחליף רופא; המטרה שלנו היא להעצים אתכם במידע כדי שהביקור הבא אצל הרופא "
                "יהיה פרודוקטיבי יותר.</p>"
                "<p>אם הפרולקטין שלכם מחוץ לטווח התקין, אל תיבהלו — רוב הגורמים ניתנים לטיפול. "
                "הצעד החשוב ביותר הוא לשתף את התוצאות עם איש מקצוע רפואי מוסמך.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הבהרה משפטית",
            body_html=(
                "<p><strong>תוכן זה מוגש למטרות מידע בלבד ואינו מהווה ייעוץ רפואי, אבחנה או "
                "טיפול.</strong> דונו תמיד בתוצאות בדיקות הדם שלכם עם איש מקצוע רפואי מוסמך. "
                "NoryaAI אינו תחליף לייעוץ רפואי. קבלו את כל ההחלטות הבריאותיות בהתייעצות עם "
                'הרופא שלכם. <a href="/analyze">בקרו בעמוד הניתוח שלנו</a> לקבלת תובנות ראשוניות '
                "על התוצאות שלכם.</p>"
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
            heading="प्रोलैक्टिन ब्लड टेस्ट: आपके रिज़ल्ट्स का क्या मतलब है?",
            body_html=(
                "<p>अगर आपकी ब्लड टेस्ट रिपोर्ट में <strong>प्रोलैक्टिन</strong> का लेवल असामान्य "
                "आया है, तो आप सोच रहे होंगे कि यह हार्मोन क्या है और क्या आपको चिंतित होना चाहिए। "
                "प्रोलैक्टिन एक पेप्टाइड हार्मोन है जो पिट्यूटरी ग्रंथि (मस्तिष्क के तल पर स्थित) "
                "के अग्र भाग से स्रावित होता है, जो मुख्य रूप से स्तन दूध उत्पादन के लिए जाना जाता है, "
                "लेकिन यह प्रजनन, प्रतिरक्षा और चयापचय को भी प्रभावित करता है।</p>"
                "<p>यह गाइड बताती है कि <strong>प्रोलैक्टिन ब्लड टेस्ट</strong> क्या मापता है, सामान्य "
                "रेफरेंस रेंज, <strong>हाई प्रोलैक्टिन</strong> (हाइपरप्रोलैक्टिनेमिया) के सामान्य "
                "कारण, संबंधित लक्षण और कब डॉक्टर से मिलना चाहिए। हमारा लक्ष्य डायग्नोसिस करना नहीं "
                "है — बल्कि आपके रिज़ल्ट्स को बेहतर समझने में मदद करना है ताकि आप अपने डॉक्टर से "
                "अधिक उत्पादक बातचीत कर सकें।</p>"
                "<p>असामान्य प्रोलैक्टिन लेवल महिलाओं में मासिक धर्म अनियमितता और बांझपन, और पुरुषों "
                "में यौन क्रिया में गड़बड़ी का कारण बन सकते हैं। अच्छी खबर यह है कि "
                "हाइपरप्रोलैक्टिनेमिया के अधिकांश कारण सही पहचान के बाद उपचार योग्य होते हैं।</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="प्रोलैक्टिन क्या है?",
            body_html=(
                "<p><strong>प्रोलैक्टिन</strong> 199 अमीनो एसिड वाला एक पॉलीपेप्टाइड हार्मोन है "
                "जो पिट्यूटरी ग्रंथि के अग्र भाग में लैक्टोट्रॉफ कोशिकाओं द्वारा बनाया जाता है। "
                "हालांकि इसके नाम का अर्थ \"दूध के लिए\" है, इसकी भूमिकाएं स्तनपान से कहीं आगे "
                "जाती हैं — प्रजनन कार्य का विनियमन, प्रतिरक्षा प्रणाली का संतुलन और ऑस्मोटिक "
                "संतुलन बनाए रखना।</p>"
                "<p>प्रोलैक्टिन का स्राव मुख्य रूप से हाइपोथैलेमस से <strong>डोपामाइन</strong> "
                "द्वारा नियंत्रित होता है, जो एक अवरोधक कारक के रूप में कार्य करता है। जब डोपामाइन "
                "का स्तर गिरता है या जब दवाएं डोपामाइन रिसेप्टर्स को ब्लॉक करती हैं, तो प्रोलैक्टिन "
                "बढ़ जाता है। यह प्रोलैक्टिन को पिट्यूटरी हार्मोन में असामान्य बनाता है — यह \"टॉनिक "
                "इनहिबिशन\" के अधीन है, यानी जब भी इसका ब्रेक हटता है, यह बढ़ जाता है।</p>"
                "<p>महिलाओं और पुरुषों दोनों के खून में प्रोलैक्टिन का मापन योग्य स्तर होता है। "
                "गर्भावस्था और स्तनपान के दौरान प्रोलैक्टिन शारीरिक रूप से बहुत बढ़ जाता है। इन "
                "स्थितियों के बाहर बढ़ा हुआ स्तर जांच का हकदार है क्योंकि यह पिट्यूटरी एडिनोमा, "
                "दवा के साइड इफेक्ट या किसी अन्य अंतर्निहित स्थिति की ओर इशारा कर सकता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="प्रोलैक्टिन के सामान्य मान (रेफरेंस रेंज)",
            body_html=(
                "<p>प्रोलैक्टिन एक साधारण ब्लड टेस्ट से मापा जाता है। नीचे दी गई तालिका सामान्य "
                "रूप से स्वीकृत रेफरेंस रेंज दिखाती है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य रेंज (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">पुरुष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">गैर-गर्भवती महिलाएं</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">गर्भवती महिलाएं</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>प्रोलैक्टिन एक सर्कैडियन रिदम का पालन करता है — यह नींद के दौरान चरम पर होता है "
                "और जागने के कुछ घंटे बाद गिर जाता है। इसलिए ब्लड सैंपल आमतौर पर सुबह, जागने के "
                "2–3 घंटे बाद लिया जाता है। तनाव, तीव्र व्यायाम और प्रोटीन-समृद्ध भोजन अस्थायी "
                "वृद्धि का कारण बन सकते हैं।</p>"
                "<p>200&nbsp;ng/mL से ऊपर के मान <strong>प्रोलैक्टिनोमा</strong> (प्रोलैक्टिन-स्रावी "
                "पिट्यूटरी एडिनोमा) का दृढ़ता से संकेत देते हैं। 25 से 100&nbsp;ng/mL के बीच के मान "
                "आमतौर पर दवाओं, हाइपोथायरायडिज्म या अन्य गैर-ट्यूमर कारणों से जुड़े होते हैं।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई प्रोलैक्टिन (हाइपरप्रोलैक्टिनेमिया) के कारण",
            body_html=(
                "<p><strong>हाइपरप्रोलैक्टिनेमिया</strong> कई अलग-अलग कारणों से हो सकती है। सबसे "
                "आम कारण हैं:</p>"
                "<ul>"
                "<li><strong>प्रोलैक्टिनोमा (पिट्यूटरी एडिनोमा):</strong> पिट्यूटरी ग्रंथि का एक "
                "सौम्य (गैर-कैंसरयुक्त) ट्यूमर जो प्रोलैक्टिन बनाता है — सबसे आम पैथोलॉजिकल कारण। "
                "इसे माइक्रोप्रोलैक्टिनोमा (&lt;10&nbsp;mm) और मैक्रोप्रोलैक्टिनोमा "
                "(&ge;10&nbsp;mm) में वर्गीकृत किया जाता है।</li>"
                "<li><strong>दवाएं:</strong> एंटीसाइकोटिक्स (हेलोपेरिडॉल, रिस्पेरिडोन), "
                "मेटोक्लोप्रामाइड, डोमपेरिडोन, कुछ एंटीडिप्रेसेंट और एस्ट्रोजन-युक्त दवाएं। "
                "दवाएं गैर-ट्यूमर कारणों में सबसे प्रमुख हैं।</li>"
                "<li><strong>हाइपोथायरायडिज्म:</strong> थायरॉइड हार्मोन की कमी TRH को बढ़ाती है, "
                "जो बदले में प्रोलैक्टिन को उत्तेजित करता है।</li>"
                "<li><strong>छाती की दीवार में जलन:</strong> हर्पीज जोस्टर, छाती की सर्जरी या "
                "छाती की दीवार के घाव।</li>"
                "<li><strong>पॉलीसिस्टिक ओवरी सिंड्रोम (PCOS):</strong> PCOS वाली कुछ महिलाओं "
                "में हल्की वृद्धि दिखती है।</li>"
                "<li><strong>तनाव और शारीरिक कारक:</strong> तीव्र तनाव, नींद, व्यायाम और "
                "निपल स्टिमुलेशन।</li>"
                "<li><strong>किडनी फेलियर:</strong> प्रोलैक्टिन के रीनल क्लीयरेंस में कमी से "
                "सीरम लेवल बढ़ता है।</li>"
                "</ul>"
                "<p>जब प्रोलैक्टिन 200&nbsp;ng/mL से अधिक होता है, तो प्रोलैक्टिनोमा की संभावना "
                "बहुत अधिक होती है। 25–100&nbsp;ng/mL के बीच के मानों में पहले दवाओं, "
                "हाइपोथायरायडिज्म और अन्य गैर-ट्यूमर कारणों की जांच करनी चाहिए।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="हाई प्रोलैक्टिन के लक्षण",
            body_html=(
                "<p>लक्षण लिंग के अनुसार भिन्न होते हैं। महिलाओं में सबसे आम संकेत हैं:</p>"
                "<ul>"
                "<li><strong>मासिक धर्म अनियमितता:</strong> ऑलिगोमेनोरिया (कम पीरियड्स) या "
                "एमेनोरिया (पीरियड्स का न आना) — सबसे प्रमुख लक्षण।</li>"
                "<li><strong>गैलेक्टोरिया:</strong> गर्भावस्था या स्तनपान के बिना स्तनों से "
                "दूध जैसा स्राव।</li>"
                "<li><strong>बांझपन:</strong> बढ़ा हुआ प्रोलैक्टिन ओव्यूलेशन को दबा देता है।</li>"
                "</ul>"
                "<p>पुरुषों में, लक्षणों की पहचान अक्सर देर से होती है:</p>"
                "<ul>"
                "<li><strong>कामेच्छा में कमी:</strong> टेस्टोस्टेरोन में द्वितीयक गिरावट के "
                "कारण।</li>"
                "<li><strong>इरेक्टाइल डिसफंक्शन:</strong> हाई प्रोलैक्टिन GnRH पल्सेटिलिटी को "
                "बाधित करता है, जिससे हाइपोगोनाडिज्म होता है।</li>"
                "<li><strong>गाइनेकोमैस्टिया और शायद ही कभी गैलेक्टोरिया:</strong> स्तन ऊतक का "
                "बढ़ना और दुर्लभ मामलों में निपल से स्राव।</li>"
                "</ul>"
                "<p>दोनों लिंगों में, मैक्रोप्रोलैक्टिनोमा <strong>सिरदर्द</strong> और "
                "<strong>दृष्टि क्षेत्र दोष</strong> (बाइटेम्पोरल हेमियानोप्सिया) जैसे मास-इफेक्ट "
                "लक्षण पैदा कर सकता है, जो ऑप्टिक कायज़्मा पर दबाव के कारण होते हैं।</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="संबंधित जांचें",
            body_html=(
                "<p>जब प्रोलैक्टिन बढ़ा हुआ पाया जाता है, तो कारण की पहचान के लिए अतिरिक्त "
                "जांचें की जाती हैं:</p>"
                "<ul>"
                "<li><strong>TSH:</strong> हाइपोथायरायडिज्म को कारण के रूप में बाहर करता है।</li>"
                "<li><strong>LH और FSH:</strong> प्रजनन कार्य का मूल्यांकन करते हैं।</li>"
                "<li><strong>गर्भावस्था परीक्षण (बीटा-hCG):</strong> प्रसव उम्र की महिलाओं में "
                "अनिवार्य।</li>"
                "<li><strong>पिट्यूटरी MRI:</strong> प्रोलैक्टिनोमा के संदेह में गोल्ड स्टैंडर्ड "
                "इमेजिंग।</li>"
                "<li><strong>टेस्टोस्टेरोन (पुरुषों में):</strong> हाइपोगोनाडिज्म के मूल्यांकन "
                "के लिए टोटल और फ्री टेस्टोस्टेरोन।</li>"
                "<li><strong>मैक्रोप्रोलैक्टिन स्क्रीनिंग:</strong> इम्युनोग्लोबुलिन कॉम्प्लेक्स "
                "से होने वाले फॉल्स पॉज़िटिव को बाहर करती है।</li>"
                "</ul>"
                "<p>इन जांचों की संयुक्त व्याख्या सटीक निदान और उचित उपचार योजना के लिए "
                "महत्वपूर्ण है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>एंडोक्राइनोलॉजिस्ट या गायनेकोलॉजिस्ट से मिलें अगर:</p>"
                "<ul>"
                "<li>आपका ब्लड टेस्ट रेफरेंस रेंज से ऊपर प्रोलैक्टिन दिखाता है</li>"
                "<li>आप बिना कारण मासिक धर्म अनियमितता या एमेनोरिया अनुभव कर रही हैं</li>"
                "<li>गर्भावस्था या स्तनपान के बाहर निपल डिस्चार्ज दिखाई दे</li>"
                "<li>कामेच्छा में कमी, इरेक्टाइल डिसफंक्शन या बांझपन की समस्या हो</li>"
                "<li>लगातार सिरदर्द और/या दृष्टि संबंधी समस्याएं हों</li>"
                "</ul>"
                "<p>प्रोलैक्टिनोमा में शुरुआती निदान विशेष रूप से महत्वपूर्ण है। "
                "माइक्रोप्रोलैक्टिनोमा डोपामाइन एगोनिस्ट (कैबर्गोलिन, ब्रोमोक्रिप्टिन) पर बहुत "
                "अच्छी तरह प्रतिक्रिया करते हैं और शायद ही कभी सर्जरी की जरूरत होती है। "
                "उपचार न किया जाए तो मैक्रोप्रोलैक्टिनोमा बढ़ सकता है और दृष्टि हानि व "
                "हाइपोपिट्यूटरिज़्म जैसी गंभीर जटिलताएं पैदा कर सकता है।</p>"
                "<p>अगर वृद्धि दवा-प्रेरित है, तो दवा बदलने या खुराक समायोजित करने से आमतौर पर "
                "समस्या हल हो जाती है। हालांकि, अपने आप कभी कोई निर्धारित दवा बंद न करें — "
                "हमेशा अपने डॉक्टर से चर्चा करें।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI आपके प्रोलैक्टिन रिज़ल्ट्स में कैसे मदद करता है",
            body_html=(
                "<p><strong>NoryaAI</strong> आपकी पूरी ब्लड टेस्ट रिपोर्ट का विश्लेषण करता है — "
                "प्रोलैक्टिन सहित — आपकी उम्र, लिंग और क्लीनिकल बैकग्राउंड को ध्यान में रखते हुए। "
                "हमारी AI-संचालित प्रणाली असामान्य मानों को हाइलाइट करती है, संभावित कारणों का "
                "सारांश देती है और ऐसे सवाल सुझाती है जो आप अपने डॉक्टर से पूछना चाह सकते हैं।</p>"
                "<p>शुरू करने के लिए तैयार हैं? तत्काल विश्लेषण के लिए "
                "<a href=\"/analyze\">अपनी लैब रिपोर्ट अपलोड करें</a>। प्लान विकल्पों के लिए हमारी "
                "<a href=\"/pricing\">प्राइसिंग पेज</a> देखें। NoryaAI डॉक्टर का विकल्प नहीं है; "
                "हमारा लक्ष्य आपको जानकारी से सशक्त बनाना है ताकि आपकी अगली मेडिकल "
                "कंसल्टेशन अधिक उत्पादक हो।</p>"
                "<p>अगर आपका प्रोलैक्टिन सामान्य सीमा से बाहर है, तो घबराएं नहीं — अधिकांश कारण "
                "उपचार योग्य हैं। सबसे महत्वपूर्ण कदम अपने रिज़ल्ट्स को एक योग्य स्वास्थ्य "
                "पेशेवर के साथ साझा करना है।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                "<p><strong>यह सामग्री केवल सूचनात्मक उद्देश्यों के लिए है और चिकित्सा सलाह, "
                "निदान या उपचार का गठन नहीं करती।</strong> अपनी ब्लड टेस्ट रिपोर्ट हमेशा किसी "
                "योग्य स्वास्थ्य पेशेवर के साथ चर्चा करें। NoryaAI चिकित्सा परामर्श का विकल्प "
                "नहीं है। सभी स्वास्थ्य संबंधी निर्णय अपने डॉक्टर की सलाह से लें। "
                '<a href="/analyze">हमारे विश्लेषण पेज पर जाएं</a> अपने रिज़ल्ट्स के बारे में '
                "प्रारंभिक जानकारी के लिए।</p>"
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
            heading="تحليل البرولاكتين في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>إذا أظهرت نتائج تحليل الدم لديك مستوى غير طبيعي من <strong>البرولاكتين</strong>، "
                "فمن الطبيعي أن تتساءل عن هذا الهرمون وما إذا كان هناك داعٍ للقلق. البرولاكتين "
                "هرمون ببتيدي تُنتجه الغدة النخامية الأمامية، يُعرف بشكل رئيسي بدوره في تحفيز "
                "إنتاج حليب الأم، لكنه يؤثر أيضاً على الإنجاب والمناعة والاستقلاب لدى "
                "النساء والرجال على حد سواء.</p>"
                "<p>يشرح هذا الدليل ما يقيسه <strong>تحليل البرولاكتين</strong>، والنطاقات "
                "المرجعية الطبيعية، والأسباب الشائعة لـ<strong>ارتفاع البرولاكتين</strong> "
                "(فرط برولاكتين الدم)، والأعراض المرتبطة، ومتى يجب مراجعة الطبيب. هدفنا ليس "
                "التشخيص — بل مساعدتك على فهم نتائجك لإجراء حوار أكثر فاعلية مع طبيبك.</p>"
                "<p>يمكن أن تسبب مستويات البرولاكتين غير الطبيعية اضطرابات في الدورة الشهرية "
                "والعقم لدى النساء، واختلال الوظيفة الجنسية لدى الرجال. والخبر السار أن معظم "
                "أسباب فرط برولاكتين الدم قابلة للعلاج بمجرد تحديدها بشكل صحيح.</p>"
            ),
        ),
        Section(
            id="what-is", level=2,
            heading="ما هو البرولاكتين؟",
            body_html=(
                "<p><strong>البرولاكتين</strong> هو هرمون بولي ببتيدي مكون من 199 حمضاً أمينياً، "
                "تُصنّعه الخلايا اللبنية في الفص الأمامي للغدة النخامية. رغم أن اسمه يعني "
                "\"لصالح الحليب\"، فإن وظائفه تتجاوز الإرضاع بكثير — تنظيم الوظيفة الإنجابية، "
                "تعديل الجهاز المناعي، والحفاظ على التوازن الأسموزي.</p>"
                "<p>يُسيطر على إفراز البرولاكتين بشكل رئيسي <strong>الدوبامين</strong> من تحت "
                "المهاد، الذي يعمل كعامل مثبّط. عندما تنخفض مستويات الدوبامين أو تُحظر "
                "مستقبلاته بالأدوية، يرتفع البرولاكتين. وهذا يجعل البرولاكتين فريداً بين هرمونات "
                "الغدة النخامية — فهو تحت تثبيط مستمر، أي أنه يرتفع كلما أُزيل كابحه.</p>"
                "<p>لدى كل من النساء والرجال مستويات قابلة للقياس من البرولاكتين. خلال الحمل "
                "والرضاعة يرتفع البرولاكتين بشكل فسيولوجي. أما الارتفاعات خارج هذه السياقات "
                "فتستدعي التقصي لأنها قد تشير إلى ورم نخامي، أو أثر جانبي دوائي، أو حالة "
                "كامنة أخرى.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المستويات الطبيعية للبرولاكتين (النطاقات المرجعية)",
            body_html=(
                "<p>يُقاس البرولاكتين بسحب دم بسيط. يوضح الجدول أدناه النطاقات المرجعية "
                "المقبولة عموماً:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق الطبيعي (ng/mL)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">الرجال</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 18</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">النساء غير الحوامل</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2 – 29</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">النساء الحوامل</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">10 – 209</td>'
                "</tr></tbody></table>"
                "<p>يتبع البرولاكتين إيقاعاً يومياً — يبلغ ذروته أثناء النوم وينخفض بعد "
                "الاستيقاظ بساعات. لذلك تُؤخذ العينة عادة في الصباح بعد 2–3 ساعات من "
                "الاستيقاظ. قد يسبب التوتر والتمارين المكثفة والوجبات الغنية بالبروتين ارتفاعات "
                "عابرة.</p>"
                "<p>القيم التي تتجاوز 200&nbsp;ng/mL تُشير بقوة إلى <strong>ورم برولاكتيني</strong> "
                "(أدينوما نخامية مفرزة للبرولاكتين). القيم بين 25 و100&nbsp;ng/mL ترتبط غالباً "
                "بالأدوية أو قصور الغدة الدرقية أو أسباب غير ورمية أخرى. قارن نتيجتك دائماً "
                "بالنطاق المرجعي لمختبرك.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع البرولاكتين (فرط برولاكتين الدم)",
            body_html=(
                "<p>يمكن أن ينتج <strong>فرط برولاكتين الدم</strong> عن أسباب متعددة. أكثرها "
                "شيوعاً هي:</p>"
                "<ul>"
                "<li><strong>الورم البرولاكتيني (أدينوما نخامية):</strong> ورم حميد يُفرز "
                "البرولاكتين — السبب المرضي الأكثر شيوعاً. يُصنّف إلى ورم برولاكتيني مجهري "
                "(&lt;10&nbsp;مم) وورم برولاكتيني كبير (&ge;10&nbsp;مم).</li>"
                "<li><strong>الأدوية:</strong> مضادات الذهان (هالوبيريدول، ريسبيريدون)، "
                "ميتوكلوبراميد، دومبيريدون، بعض مضادات الاكتئاب والإستروجين. الأدوية هي "
                "السبب الأول غير الورمي.</li>"
                "<li><strong>قصور الغدة الدرقية:</strong> نقص هرمون الغدة الدرقية يرفع TRH، "
                "الذي بدوره يحفّز إفراز البرولاكتين.</li>"
                "<li><strong>تهيّج جدار الصدر:</strong> الحزام الناري، جراحة الصدر أو آفات "
                "جدار الصدر.</li>"
                "<li><strong>متلازمة المبيض المتعدد الكيسات (PCOS):</strong> نسبة من النساء "
                "المصابات تظهر لديهن ارتفاع طفيف.</li>"
                "<li><strong>التوتر والعوامل الفسيولوجية:</strong> التوتر الشديد والنوم والتمارين "
                "وتحفيز الحلمة.</li>"
                "<li><strong>الفشل الكلوي:</strong> انخفاض التصفية الكلوية يرفع المستويات "
                "المصلية.</li>"
                "</ul>"
                "<p>عندما يتجاوز البرولاكتين 200&nbsp;ng/mL، تكون احتمالية الورم البرولاكتيني "
                "مرتفعة. في النطاق 25–100&nbsp;ng/mL يجب البحث أولاً عن الأدوية وقصور "
                "الغدة الدرقية والأسباب غير الورمية الأخرى.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض ارتفاع البرولاكتين",
            body_html=(
                "<p>تختلف الأعراض بين الجنسين. عند النساء أكثر العلامات شيوعاً هي:</p>"
                "<ul>"
                "<li><strong>اضطرابات الدورة الشهرية:</strong> قلة الطمث أو انقطاعه — "
                "العَرَض الأبرز.</li>"
                "<li><strong>ثرّ اللبن (Galactorrhea):</strong> إفراز حليبي من الحلمة خارج "
                "الحمل أو الرضاعة.</li>"
                "<li><strong>العقم:</strong> البرولاكتين المرتفع يُثبّط الإباضة.</li>"
                "</ul>"
                "<p>عند الرجال، غالباً ما تُكتشف الأعراض متأخراً:</p>"
                "<ul>"
                "<li><strong>انخفاض الرغبة الجنسية:</strong> بسبب الانخفاض الثانوي في "
                "التستوستيرون.</li>"
                "<li><strong>ضعف الانتصاب:</strong> البرولاكتين المرتفع يُعطّل نبضية GnRH "
                "ويسبب قصور الغدد التناسلية.</li>"
                "<li><strong>التثدي ونادراً ثرّ اللبن:</strong> تضخم نسيج الثدي، وفي حالات "
                "نادرة إفراز من الحلمة.</li>"
                "</ul>"
                "<p>في كلا الجنسين، قد يسبب الورم البرولاكتيني الكبير <strong>صداعاً</strong> "
                "و<strong>عيوباً في مجال الرؤية</strong> (عمى نصفي صدغي) بسبب الضغط على "
                "التصالب البصري.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="الفحوصات ذات الصلة",
            body_html=(
                "<p>عند اكتشاف ارتفاع البرولاكتين، تُطلب فحوصات إضافية لتحديد السبب:</p>"
                "<ul>"
                "<li><strong>TSH:</strong> يستبعد قصور الغدة الدرقية كسبب.</li>"
                "<li><strong>LH وFSH:</strong> يقيّمان الوظيفة الإنجابية.</li>"
                "<li><strong>اختبار الحمل (بيتا-hCG):</strong> ضروري لدى النساء في سن "
                "الإنجاب.</li>"
                "<li><strong>تصوير الغدة النخامية بالرنين المغناطيسي:</strong> الفحص التصويري "
                "المعياري لاكتشاف الورم البرولاكتيني.</li>"
                "<li><strong>التستوستيرون (عند الرجال):</strong> الكلي والحر لتقييم "
                "قصور الغدد التناسلية.</li>"
                "<li><strong>الماكروبرولاكتين:</strong> يستبعد النتائج الإيجابية الكاذبة "
                "الناتجة عن مركّبات الغلوبولين المناعي.</li>"
                "</ul>"
                "<p>التفسير المشترك لهذه الفحوصات ضروري للتشخيص الدقيق والتخطيط العلاجي "
                "المناسب.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>راجع طبيب غدد صماء أو طبيب نساء إذا:</p>"
                "<ul>"
                "<li>أظهر تحليل الدم مستوى برولاكتين أعلى من النطاق المرجعي</li>"
                "<li>تعاني من اضطرابات في الدورة الشهرية أو انقطاعها دون تفسير</li>"
                "<li>لاحظت إفرازاً من الحلمة خارج الحمل أو الرضاعة</li>"
                "<li>تعاني من انخفاض الرغبة الجنسية أو ضعف الانتصاب أو العقم</li>"
                "<li>تعاني من صداع مستمر و/أو اضطرابات بصرية</li>"
                "</ul>"
                "<p>التشخيص المبكر مهم بشكل خاص في حالة الورم البرولاكتيني. تستجيب الأورام "
                "البرولاكتينية المجهرية بشكل ممتاز لمنبّهات الدوبامين (كابيرغولين، بروموكريبتين) "
                "ونادراً ما تحتاج جراحة. بدون علاج، قد تنمو الأورام البرولاكتينية الكبيرة وتسبب "
                "مضاعفات خطيرة مثل فقدان البصر وقصور الغدة النخامية.</p>"
                "<p>إذا كان الارتفاع ناجماً عن دواء، فإن تغيير الدواء أو تعديل الجرعة يحل "
                "المشكلة عادة. لا تتوقف أبداً عن تناول دواء موصوف من تلقاء نفسك — ناقش "
                "التغييرات دائماً مع طبيبك.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يساعدك NoryaAI في فهم نتائج البرولاكتين",
            body_html=(
                "<p>يقوم <strong>NoryaAI</strong> بتحليل تقرير فحص الدم الكامل — بما في ذلك "
                "البرولاكتين — مع مراعاة عمرك وجنسك وسياقك السريري. يُبرز نظامنا القائم على "
                "الذكاء الاصطناعي القيم الخارجة عن النطاق، ويلخص الأسباب المحتملة، ويقترح "
                "أسئلة قد ترغب في طرحها على طبيبك.</p>"
                "<p>هل أنت مستعد للبدء؟ <a href=\"/analyze\">ارفع تقرير المختبر الخاص بك</a> "
                "للحصول على تحليل فوري. تفضل بزيارة <a href=\"/pricing\">صفحة الأسعار</a> "
                "لاستكشاف الخطط المتاحة. NoryaAI لا يحل محل الطبيب؛ هدفنا تمكينك بالمعلومات "
                "ليكون موعدك الطبي القادم أكثر إنتاجية.</p>"
                "<p>إذا كان البرولاكتين لديك خارج النطاق الطبيعي، فلا تقلق — معظم الأسباب "
                "قابلة للعلاج. الخطوة الأهم هي مشاركة نتائجك مع متخصص رعاية صحية مؤهل.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                "<p><strong>هذا المحتوى لأغراض إعلامية فقط ولا يُشكّل نصيحة طبية أو تشخيصاً "
                "أو علاجاً.</strong> ناقش نتائج فحوصاتك دائماً مع متخصص رعاية صحية مؤهل. "
                "NoryaAI ليس بديلاً عن الاستشارة الطبية. اتخذ جميع القرارات الصحية بالتشاور "
                'مع طبيبك. <a href="/analyze">قم بزيارة صفحة التحليل الخاصة بنا</a> للحصول '
                "على رؤى أولية حول نتائجك.</p>"
            ),
        ),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_prolactin_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Prolactin article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_prolactin_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Prolactin article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is prolactin and what does it do?",
             "answer": "Prolactin is a hormone produced by the pituitary gland. It is best known for stimulating breast-milk production, but it also plays roles in reproduction, immune regulation, and metabolism in both women and men."},
            {"question": "What is a normal prolactin level?",
             "answer": "Normal prolactin levels are approximately 2–18 ng/mL for men, 2–29 ng/mL for non-pregnant women, and 10–209 ng/mL during pregnancy. Levels fluctuate throughout the day and are highest during sleep. Always compare with your laboratory's reference range."},
            {"question": "What causes high prolactin (hyperprolactinemia)?",
             "answer": "Common causes include prolactinoma (a benign pituitary tumour), medications such as antipsychotics and metoclopramide, hypothyroidism, PCOS, chest-wall irritation, renal failure, and stress. Medications are the most common non-tumour cause."},
            {"question": "What are the symptoms of high prolactin?",
             "answer": "In women, high prolactin can cause irregular or absent periods, milky nipple discharge (galactorrhea), and infertility. In men, it may lead to decreased libido, erectile dysfunction, and rarely breast enlargement. Large pituitary tumours can cause headaches and vision problems."},
        ],
        "tr": [
            {"question": "Prolaktin nedir ve ne işe yarar?",
             "answer": "Prolaktin, hipofiz bezinden salgılanan bir hormondur. En çok süt üretimini uyarmasıyla bilinir; ancak üreme, bağışıklık sistemi ve metabolizma üzerinde de önemli etkileri vardır."},
            {"question": "Normal prolaktin değeri nedir?",
             "answer": "Normal prolaktin değerleri erkeklerde yaklaşık 2–18 ng/mL, hamile olmayan kadınlarda 2–29 ng/mL ve hamilelikte 10–209 ng/mL aralığındadır. Gün içinde dalgalanma gösterir ve uyku sırasında en yüksek seviyeye ulaşır."},
            {"question": "Prolaktin yüksekliğinin nedenleri nelerdir?",
             "answer": "En sık nedenler prolaktinoma (iyi huylu hipofiz tümörü), antipsikotikler ve metoklopramid gibi ilaçlar, hipotiroidizm, PKOS, göğüs duvarı irritasyonu, böbrek yetmezliği ve strestir. İlaçlar tümör dışı en sık nedendir."},
            {"question": "Yüksek prolaktinin belirtileri nelerdir?",
             "answer": "Kadınlarda adet düzensizliği veya kesilmesi, memeden süt gelmesi (galaktore) ve kısırlık görülebilir. Erkeklerde cinsel istek azalması, erektil disfonksiyon ve nadiren meme büyümesi olabilir. Büyük tümörlerde baş ağrısı ve görme bozuklukları da eklenebilir."},
        ],
        "es": [
            {"question": "¿Qué es la prolactina y para qué sirve?",
             "answer": "La prolactina es una hormona producida por la hipófisis. Es conocida por estimular la producción de leche materna, pero también interviene en la reproducción, la inmunidad y el metabolismo en ambos sexos."},
            {"question": "¿Cuál es un nivel normal de prolactina?",
             "answer": "Los niveles normales son aproximadamente 2–18 ng/mL en hombres, 2–29 ng/mL en mujeres no embarazadas y 10–209 ng/mL durante el embarazo. Fluctúan a lo largo del día y alcanzan su pico durante el sueño."},
            {"question": "¿Qué causa la prolactina alta?",
             "answer": "Las causas más frecuentes incluyen prolactinoma (tumor hipofisario benigno), fármacos como antipsicóticos y metoclopramida, hipotiroidismo, SOP, irritación torácica, insuficiencia renal y estrés."},
            {"question": "¿Cuáles son los síntomas de la prolactina alta?",
             "answer": "En mujeres puede causar irregularidades menstruales, secreción mamaria lechosa e infertilidad. En hombres, disminución de la libido, disfunción eréctil y raramente ginecomastia. Los tumores grandes pueden provocar cefalea y problemas visuales."},
        ],
        "de": [
            {"question": "Was ist Prolaktin und welche Funktion hat es?",
             "answer": "Prolaktin ist ein Hormon der Hypophyse. Es ist vor allem für die Milchproduktion bekannt, beeinflusst aber auch Reproduktion, Immunregulation und Stoffwechsel bei beiden Geschlechtern."},
            {"question": "Was ist ein normaler Prolaktinwert?",
             "answer": "Normalwerte liegen bei Männern bei ca. 2–18 ng/mL, bei nicht schwangeren Frauen bei 2–29 ng/mL und in der Schwangerschaft bei 10–209 ng/mL. Prolaktin unterliegt einem Tagesrhythmus mit Höchstwerten im Schlaf."},
            {"question": "Was verursacht erhöhtes Prolaktin?",
             "answer": "Häufige Ursachen sind Prolaktinom (gutartiger Hypophysentumor), Medikamente wie Antipsychotika und Metoclopramid, Hypothyreose, PCOS, Brustwandreizung, Niereninsuffizienz und Stress."},
            {"question": "Welche Symptome hat erhöhtes Prolaktin?",
             "answer": "Bei Frauen kann es Zyklusstörungen, milchige Brustsekretion und Unfruchtbarkeit verursachen. Bei Männern Libidoverlust, erektile Dysfunktion und selten Gynäkomastie. Große Tumoren können Kopfschmerzen und Sehstörungen hervorrufen."},
        ],
        "fr": [
            {"question": "Qu'est-ce que la prolactine et à quoi sert-elle ?",
             "answer": "La prolactine est une hormone produite par l'hypophyse. Elle est surtout connue pour stimuler la production de lait, mais elle intervient aussi dans la reproduction, l'immunité et le métabolisme chez les deux sexes."},
            {"question": "Quel est un taux normal de prolactine ?",
             "answer": "Les valeurs normales sont d'environ 2–18 ng/mL chez l'homme, 2–29 ng/mL chez la femme non enceinte et 10–209 ng/mL pendant la grossesse. Le taux fluctue au cours de la journée et atteint son pic pendant le sommeil."},
            {"question": "Quelles sont les causes d'une prolactine élevée ?",
             "answer": "Les causes fréquentes comprennent le prolactinome (adénome hypophysaire bénin), les médicaments (antipsychotiques, métoclopramide), l'hypothyroïdie, le SOPK, l'irritation de la paroi thoracique, l'insuffisance rénale et le stress."},
            {"question": "Quels sont les symptômes d'une prolactine élevée ?",
             "answer": "Chez la femme : troubles du cycle, écoulement laiteux du sein et infertilité. Chez l'homme : baisse de la libido, dysfonction érectile et rarement gynécomastie. Les gros adénomes peuvent entraîner céphalées et troubles visuels."},
        ],
        "it": [
            {"question": "Che cos'è la prolattina e a cosa serve?",
             "answer": "La prolattina è un ormone prodotto dall'ipofisi. È nota soprattutto per stimolare la produzione di latte materno, ma influenza anche la riproduzione, l'immunità e il metabolismo in entrambi i sessi."},
            {"question": "Qual è un valore normale di prolattina?",
             "answer": "I valori normali sono circa 2–18 ng/mL negli uomini, 2–29 ng/mL nelle donne non in gravidanza e 10–209 ng/mL in gravidanza. Seguono un ritmo circadiano con picco durante il sonno."},
            {"question": "Quali sono le cause di prolattina alta?",
             "answer": "Le cause più frequenti includono prolattinoma (adenoma ipofisario benigno), farmaci come antipsicotici e metoclopramide, ipotiroidismo, PCOS, irritazione della parete toracica, insufficienza renale e stress."},
            {"question": "Quali sono i sintomi di prolattina alta?",
             "answer": "Nella donna: irregolarità mestruali, secrezione lattescente dal capezzolo e infertilità. Nell'uomo: calo della libido, disfunzione erettile e raramente ginecomastia. Tumori grandi possono causare cefalea e disturbi visivi."},
        ],
        "he": [
            {"question": "מהו פרולקטין ומה תפקידו?",
             "answer": "פרולקטין הוא הורמון המיוצר בבלוטת יותרת המוח. הוא ידוע בעיקר בזכות תפקידו בייצור חלב אם, אך הוא משפיע גם על הפוריות, מערכת החיסון והמטבוליזם בנשים ובגברים כאחד."},
            {"question": "מהי רמת פרולקטין תקינה?",
             "answer": "ערכים תקינים הם כ-2–18 ng/mL בגברים, 2–29 ng/mL בנשים שאינן בהריון ו-10–209 ng/mL בהריון. הרמות משתנות במהלך היום ומגיעות לשיא בשינה."},
            {"question": "מה גורם לפרולקטין גבוה?",
             "answer": "גורמים שכיחים כוללים פרולקטינומה (גידול שפיר בהיפופיזה), תרופות כמו אנטי-פסיכוטיים ומטוקלופרמיד, תת-פעילות בלוטת התריס, PCOS, גירוי דופן בית החזה, אי-ספיקת כליות ומתח."},
            {"question": "מהם התסמינים של פרולקטין גבוה?",
             "answer": "בנשים: הפרעות במחזור, הפרשה חלבית מהשד ואי-פוריות. בגברים: ירידה בחשק המיני, הפרעות בזקפה ולעיתים נדירות גינקומסטיה. גידולים גדולים עלולים לגרום לכאבי ראש ולבעיות ראייה."},
        ],
        "hi": [
            {"question": "प्रोलैक्टिन क्या है और यह क्या करता है?",
             "answer": "प्रोलैक्टिन पिट्यूटरी ग्रंथि द्वारा उत्पादित एक हार्मोन है। यह मुख्य रूप से स्तन दूध उत्पादन को प्रेरित करने के लिए जाना जाता है, लेकिन यह प्रजनन, प्रतिरक्षा और चयापचय को भी प्रभावित करता है।"},
            {"question": "सामान्य प्रोलैक्टिन लेवल क्या है?",
             "answer": "सामान्य मान पुरुषों में लगभग 2–18 ng/mL, गैर-गर्भवती महिलाओं में 2–29 ng/mL और गर्भावस्था में 10–209 ng/mL हैं। यह दिन में उतार-चढ़ाव करता है और नींद के दौरान चरम पर होता है।"},
            {"question": "हाई प्रोलैक्टिन के कारण क्या हैं?",
             "answer": "सामान्य कारणों में प्रोलैक्टिनोमा (सौम्य पिट्यूटरी ट्यूमर), एंटीसाइकोटिक्स और मेटोक्लोप्रामाइड जैसी दवाएं, हाइपोथायरायडिज्म, PCOS, छाती की दीवार में जलन, किडनी फेलियर और तनाव शामिल हैं।"},
            {"question": "हाई प्रोलैक्टिन के लक्षण क्या हैं?",
             "answer": "महिलाओं में मासिक धर्म अनियमितता, स्तनों से दूध जैसा स्राव और बांझपन हो सकता है। पुरुषों में कामेच्छा में कमी, इरेक्टाइल डिसफंक्शन और शायद ही कभी गाइनेकोमैस्टिया। बड़े ट्यूमर सिरदर्द और दृष्टि समस्याएं पैदा कर सकते हैं।"},
        ],
        "ar": [
            {"question": "ما هو البرولاكتين وما وظيفته؟",
             "answer": "البرولاكتين هرمون تنتجه الغدة النخامية. يُعرف بشكل رئيسي بتحفيز إنتاج حليب الأم، لكنه يؤثر أيضاً على الإنجاب والمناعة والاستقلاب لدى النساء والرجال."},
            {"question": "ما هو المستوى الطبيعي للبرولاكتين؟",
             "answer": "القيم الطبيعية تقريباً 2–18 ng/mL للرجال، 2–29 ng/mL للنساء غير الحوامل، و10–209 ng/mL أثناء الحمل. يتذبذب خلال اليوم ويبلغ ذروته أثناء النوم."},
            {"question": "ما أسباب ارتفاع البرولاكتين؟",
             "answer": "تشمل الأسباب الشائعة الورم البرولاكتيني (ورم نخامي حميد)، أدوية مثل مضادات الذهان والميتوكلوبراميد، قصور الغدة الدرقية، متلازمة تكيّس المبايض، تهيّج جدار الصدر، الفشل الكلوي والتوتر."},
            {"question": "ما أعراض ارتفاع البرولاكتين؟",
             "answer": "عند النساء: اضطرابات الدورة الشهرية، إفراز حليبي من الثدي والعقم. عند الرجال: انخفاض الرغبة الجنسية، ضعف الانتصاب ونادراً التثدي. الأورام الكبيرة قد تسبب صداعاً واضطرابات بصرية."},
        ],
    }
