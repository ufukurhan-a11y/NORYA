# -*- coding: utf-8 -*-
"""
High fasting insulin blog article — full body content for all 9 languages.
Used by blog_i18n._article_fasting_insulin_high().
Sections: intro, what-is-fasting-insulin, what-high-means, insulin-resistance-link,
homa-ir-connection, glucose-normal-insulin-high, related-tests, not-enough-alone,
when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="Açlık insülini yüksekse ne anlama gelir?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızda <strong>açlık insülini</strong> değerinin yüksek "
                "çıktığını gördüğünüzde aklınıza pek çok soru gelebilir: Bu tehlikeli mi? "
                "Diyabet mi oluyorum? Neden kan şekerim normal görünürken insülin yüksek? "
                "Bu rehber, açlık insülininin ne olduğunu, yüksek çıkmasının neler ifade "
                "edebileceğini ve sonucunuzu nasıl değerlendirmeniz gerektiğini sade bir "
                "dille açıklıyor.</p>"
                "<p>Amacımız teşhis koymak değil — sizi doktor randevunuza daha bilinçli "
                "hazırlamak. Açlık insülini, metabolik sağlığınız hakkında erken ipuçları "
                "verebilen değerli bir gösterge olabilir; ancak tek başına hiçbir zaman "
                "kesin bir tanı aracı olarak kullanılmamalıdır.</p>"
            ),
        ),
        Section(
            id="what-is-fasting-insulin", level=2,
            heading="Açlık insülini nedir ve nasıl ölçülür?",
            body_html=(
                "<p><strong>İnsülin</strong>, pankreas tarafından üretilen ve kan şekerinin "
                "(glukozun) hücrelere girmesini sağlayan bir hormondur. Yemek yediğinizde "
                "kan şekeriniz yükselir ve pankreas buna yanıt olarak insülin salgılar. "
                "<strong>Açlık insülini</strong> ise genellikle 8–12 saatlik bir açlık "
                "döneminin ardından alınan kan örneğinde ölçülür; bu sayede yemeğin etkisi "
                "aradan çıkarılarak vücudunuzun bazal insülin düzeyi değerlendirilir.</p>"
                "<p>Sonuçlar genellikle <strong>μU/mL</strong> (veya μIU/mL) biriminde "
                "raporlanır. Referans aralıkları laboratuvara göre değişmekle birlikte, "
                "yaygın olarak 2–25 μU/mL aralığı normal kabul edilir. Pek çok klinisyen "
                "optimal düzeyi 10 μU/mL altı olarak değerlendirse de bu eşik evrensel "
                "değildir; yaş, cinsiyet, beden kitle indeksi ve laboratuvar yöntemi sonucu "
                "etkiler. Sonucunuzu her zaman hekiminiz, kendi referans aralığınız ve klinik "
                "bağlamınız çerçevesinde değerlendirmelidir.</p>"
            ),
        ),
        Section(
            id="what-high-means", level=2,
            heading="Açlık insülininin yüksek çıkması ne anlama gelebilir?",
            body_html=(
                "<p>Açlık insülininin yüksek olması, vücudunuzun kan şekerini normal "
                "aralıkta tutmak için beklenenden daha fazla insülin üretmek zorunda "
                "kaldığına işaret edebilir. Bu durum <strong>kompansatuvar "
                "hiperinsulinemi</strong> olarak adlandırılır ve genellikle hücrelerin "
                "insüline duyarlılığının azaldığını gösterir.</p>"
                "<p>Yüksek açlık insülini ile ilişkilendirilebilen durumlar şunlardır:</p>"
                "<ul>"
                "<li><strong>İnsülin direnci</strong> — hücrelerin insüline verdiği yanıtın "
                "azalması</li>"
                "<li><strong>Metabolik sendrom</strong> — abdominal obezite, yüksek "
                "trigliserid, düşük HDL, yüksek tansiyon ve kan şekeri bozukluğunun bir "
                "arada bulunması</li>"
                "<li><strong>Polikistik over sendromu (PCOS)</strong> — kadınlarda sık "
                "görülen hormonal bir durum</li>"
                "<li><strong>Non-alkolik yağlı karaciğer hastalığı (NAFLD)</strong></li>"
                "<li><strong>Kardiyovasküler risk artışı</strong></li>"
                "</ul>"
                "<p>Ancak yüksek bir değer bu durumlardan herhangi birinin kesin varlığı "
                "anlamına gelmez. Pek çok faktör açlık insülin düzeyini geçici olarak "
                "etkileyebilir: stres, uyku düzensizliği, bazı ilaçlar ve hatta kan "
                "alımından kısa süre önce yapılan fiziksel aktivite. Yorum her zaman "
                "hekiminize aittir.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-link", level=2,
            heading="İnsülin direnci ile ilişkisi",
            body_html=(
                "<p><strong>İnsülin direnci</strong>, kas, yağ ve karaciğer hücrelerinin "
                "insülinin sinyaline yeterince yanıt vermemesi durumudur. Bu olduğunda "
                "pankreas dengeyi korumak için daha fazla insülin üretir; dolayısıyla "
                "kanda insülin seviyesi yükselir. İlk aşamada bu mekanizma işe yarar ve "
                "kan şekeri normal kalır — ancak yıllar içinde pankreas bu artan talebe "
                "yetişemezse kan şekeri de yükselmeye başlar ve prediyabet veya tip 2 "
                "diyabet riski artar.</p>"
                "<p>Bu nedenle yüksek açlık insülini, kan şekeri henüz yükselmeden "
                "<em>önce</em> ortaya çıkabilen bir erken uyarı sinyali olarak "
                "değerlendirilir. Ancak insülin direnci tanısı tek bir kan değerine "
                "bakılarak konmaz; hekiminiz öykünüzü, fizik muayenenizi ve diğer "
                "laboratuvar sonuçlarınızı bir bütün olarak ele alır.</p>"
            ),
        ),
        Section(
            id="homa-ir-connection", level=2,
            heading="HOMA-IR ile bağlantısı",
            body_html=(
                "<p>Açlık insülin düzeyinizi daha anlamlı bir bağlama oturtmanın yaygın "
                "yollarından biri <strong>HOMA-IR</strong> indeksini hesaplamaktır. HOMA-IR, "
                "açlık insülini ve açlık glukozu kullanılarak elde edilen basit bir "
                "formüldür ve insülin direncinin derecesini tahmin etmeye yardımcı olur.</p>"
                "<p>Formül şöyledir: <em>Açlık insülini (μU/mL) × Açlık glukozu (mg/dL) "
                "÷ 405</em>. Pek çok kaynakta 1,0 altı optimal kabul edilirken, 2,5 üzeri "
                "değerler insülin direncine işaret edebilir — ancak eşik değerleri "
                "popülasyona ve laboratuvar yöntemine göre değişir.</p>"
                "<p>HOMA-IR hakkında daha ayrıntılı bilgi almak isterseniz "
                "<a href=\"/tr/blog/homa-ir-nedir\">HOMA-IR rehberimizi</a> "
                "incelemenizi öneriyoruz. Bu yazı, açlık insülininin HOMA-IR hesaplamasındaki "
                "rolünü ve tek başına insülin değerine göre neden daha geniş bir perspektif "
                "sunduğunu ayrıntılı şekilde açıklıyor.</p>"
            ),
        ),
        Section(
            id="glucose-normal-insulin-high", level=2,
            heading="Kan şekeri normal olsa bile insülin neden yüksek olabilir?",
            body_html=(
                "<p>Bu, pek çok kişiyi şaşırtan bir durumdur: "
                "<a href=\"/tr/blog/aclik-kan-sekeri-sonucu-nasil-degerlendirilir\">açlık "
                "kan şekeri</a> normal aralıkta görünürken açlık insülini yüksek çıkar. "
                "Bunun nedeni, vücudun kan şekerini normal tutmak için fazla çalışıyor "
                "olmasıdır. Pankreas, hücrelerin azalan duyarlılığını telafi etmek için "
                "daha fazla insülin salgılar ve bu mekanizma başarılı olduğu sürece kan "
                "şekeri normalmiş gibi görünür.</p>"
                "<p>Bu tabloya <strong>kompansatuvar hiperinsulinemi</strong> denir. "
                "Yalnızca açlık glukozuna bakıldığında her şey yolunda gibi gözükebilir; "
                "oysa insülin düzeyi, metabolik stresin çoktan başladığını gösteriyor "
                "olabilir. Bu yüzden bazı hekimler, özellikle aile öyküsünde diyabet "
                "bulunan veya metabolik sendrom risk faktörleri taşıyan bireylerde açlık "
                "insülinini de istemektedir.</p>"
                "<p>Kısaca: normal glukoz, sağlığınızın iyi olduğunun tek göstergesi "
                "değildir — insülin düzeyine birlikte bakmak daha geniş bir resim "
                "sunar.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Hangi diğer testlerle birlikte değerlendirilir?",
            body_html=(
                "<p>Açlık insülini tek başına yorumlanmamalıdır. Hekiminiz genellikle "
                "aşağıdaki testlerin bir kısmını veya tamamını birlikte değerlendirir:</p>"
                "<ul>"
                "<li><strong>Açlık glukozu (kan şekeri)</strong> — insülinle birlikte "
                "HOMA-IR hesaplamasına girer</li>"
                "<li><strong><a href=\"/tr/blog/hba1c-sonucu-ne-anlama-gelir\">HbA1c</a>"
                "</strong> — son 2–3 aydaki ortalama kan şekerini yansıtır</li>"
                "<li><strong>Trigliserid ve HDL kolesterol</strong> — metabolik sendrom "
                "belirteçleri arasındadır</li>"
                "<li><strong>C-peptid</strong> — pankreasın insülin üretim kapasitesini "
                "gösterir; tip 1 ve tip 2 diyabet ayrımında kullanılabilir</li>"
                "<li><strong>OGTT (oral glukoz tolerans testi)</strong> — şeker yükleme "
                "sonrası vücudun yanıtını ölçer</li>"
                "<li><strong>Bel çevresi ve beden kitle indeksi</strong> — fiziksel "
                "muayene parametreleri olarak metabolik risk değerlendirmesine katkıda "
                "bulunur</li>"
                "</ul>"
                "<p>Bu testlerden hangilerinin istendiği, klinik duruma ve hekiminizin "
                "değerlendirmesine bağlıdır. Amaç, tek bir sayıya değil, bir bütün olarak "
                "metabolik tablonuza bakmaktır.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Sonuçlar neden tek başına yorumlanmamalı?",
            body_html=(
                "<p>Tek bir açlık insülini değeri, sağlık durumunuzu tanımlayamaz. "
                "Aynı gün ikinci bir ölçümde bile farklı sonuç çıkabilir — çünkü stres, "
                "uyku kalitesi, bir gece önce yediğiniz yemek ve hatta kan alma "
                "prosedürünün kendisi sonucu etkileyebilir.</p>"
                "<p>Laboratuvar referans aralıkları da tek tip değildir; bir laboratuvar "
                "\"normal\" dediği değeri başka bir laboratuvar \"sınırda yüksek\" olarak "
                "raporlayabilir. Bu nedenle sonucunuzu her zaman:</p>"
                "<ul>"
                "<li>Kendi laboratuvarınızın referans aralığıyla</li>"
                "<li>Diğer kan değerlerinizle (glukoz, HbA1c, lipid paneli vb.)</li>"
                "<li>Tıbbi öykünüz ve aile öykünüzle</li>"
                "<li>Hekiminizin klinik muayene bulgularıyla</li>"
                "</ul>"
                "<p>birlikte değerlendirmeniz gerekir. İnternetten okunan eşik değerler "
                "bilgi edinmek için faydalı olabilir, ancak kişisel sağlık kararlarının "
                "yerine geçmez.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlardan herhangi biri geçerliyse sonucunuzu bir "
                "hekimle paylaşmanızı öneririz:</p>"
                "<ul>"
                "<li>Açlık insülin değeriniz laboratuvar referans aralığının üzerinde "
                "çıktıysa</li>"
                "<li>Ailenizde tip 2 diyabet, metabolik sendrom veya kalp-damar "
                "hastalığı öyküsü varsa</li>"
                "<li>Aşırı kilo, bel bölgesinde yağlanma veya PCOS belirtileri "
                "yaşıyorsanız</li>"
                "<li>Yorgunluk, sürekli açlık hissi veya açıklanamayan kilo değişimi "
                "gibi belirtileriniz varsa</li>"
                "<li>Kan şekeriniz normal olsa bile insülin düzeyiniz yüksek çıktıysa</li>"
                "</ul>"
                "<p>Belirtiniz olmasa bile, rutin tahlillerinizde anormal bir değer "
                "gördüğünüzde hekiminize sormak her zaman doğru adımdır. Erken farkındalık, "
                "yaşam tarzı değişiklikleriyle metabolik riskinizi yönetme şansı "
                "tanıyabilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya ile sonuçlarınızı daha anlaşılır hale getirin",
            body_html=(
                "<p>Norya'da teşhis koymuyoruz — ancak kan tahlili sonuçlarınızı "
                "anlamanızı kolaylaştırıyoruz. <a href=\"/analyze\">Laboratuvar raporunuzu "
                "yükleyerek</a> açlık insülini dahil tüm değerlerinizi sade dilde, referans "
                "aralıkları ve bağlamıyla birlikte gösteren yapılandırılmış bir özet "
                "alabilirsiniz.</p>"
                "<p>Bu özet, hekiminizle konuşurken doğru soruları sormanıza ve sonuçlarınızı "
                "daha bilinçli değerlendirmenize yardımcı olur. Seçenekleri ve fiyatları "
                "görmek için <a href=\"/pricing\">fiyatlandırma sayfamıza</a> göz "
                "atabilirsiniz.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                "<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye "
                "veya teşhis yerine geçmez.</strong> Yüksek açlık insülini birçok nedene "
                "bağlı olabilir; sonucunuzu ancak öykünüzü ve bağlamınızı bilen bir sağlık "
                "profesyoneli doğru yorumlayabilir. Laboratuvar sonuçlarınızı her zaman "
                "bir hekimle görüşün.</p>"
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
            heading="What does high fasting insulin mean?",
            body_html=(
                "<p>If your lab report shows an elevated <strong>fasting insulin</strong> "
                "level, you probably have questions: Is this serious? Does it mean I have "
                "diabetes? Why is my blood sugar normal but my insulin high? This guide "
                "explains what fasting insulin is, what a high result can tell you, and how "
                "to think about it in the right context.</p>"
                "<p>Our goal is not to diagnose — it is to help you walk into your next "
                "doctor's appointment better informed. Fasting insulin can be an early "
                "metabolic signal, but it is never a standalone diagnosis. Understanding "
                "what it measures and what it does not is the first step toward making "
                "sense of your result.</p>"
            ),
        ),
        Section(
            id="what-is-fasting-insulin", level=2,
            heading="What is fasting insulin and how is it measured?",
            body_html=(
                "<p><strong>Insulin</strong> is a hormone produced by the pancreas that "
                "allows glucose (blood sugar) to enter your cells for energy. When you eat, "
                "blood sugar rises and the pancreas releases insulin in response. "
                "<strong>Fasting insulin</strong> is the level measured after you have not "
                "eaten for 8–12 hours, which removes the influence of a recent meal and "
                "reflects your body's baseline insulin activity.</p>"
                "<p>Results are usually reported in <strong>μU/mL</strong> (or μIU/mL). "
                "Reference ranges vary by laboratory, but a common range is roughly "
                "2–25 μU/mL. Many clinicians consider values below 10 μU/mL as optimal, "
                "though this threshold is not universal. Age, sex, body mass index, and "
                "the assay method can all influence the result. Your doctor interprets "
                "your number within your own reference range and clinical picture.</p>"
            ),
        ),
        Section(
            id="what-high-means", level=2,
            heading="What can high fasting insulin indicate?",
            body_html=(
                "<p>A high fasting insulin level suggests that your body is producing more "
                "insulin than expected to keep blood sugar within normal limits. This is "
                "sometimes called <strong>compensatory hyperinsulinaemia</strong> and is "
                "often an early sign that cells are becoming less responsive to insulin.</p>"
                "<p>Conditions commonly associated with elevated fasting insulin include:</p>"
                "<ul>"
                "<li><strong>Insulin resistance</strong> — reduced cellular response to "
                "insulin's signal</li>"
                "<li><strong>Metabolic syndrome</strong> — a cluster of abdominal obesity, "
                "high triglycerides, low HDL, elevated blood pressure, and impaired glucose</li>"
                "<li><strong>Polycystic ovary syndrome (PCOS)</strong> — a hormonal condition "
                "common in women of reproductive age</li>"
                "<li><strong>Non-alcoholic fatty liver disease (NAFLD)</strong></li>"
                "<li><strong>Increased cardiovascular risk</strong></li>"
                "</ul>"
                "<p>However, a single elevated value does not confirm any of these. Stress, "
                "poor sleep, certain medications, and even recent vigorous exercise can "
                "transiently raise fasting insulin. Interpretation always belongs to your "
                "doctor.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-link", level=2,
            heading="The relationship with insulin resistance",
            body_html=(
                "<p><strong>Insulin resistance</strong> means that muscle, fat, and liver "
                "cells do not respond efficiently to insulin. To compensate, the pancreas "
                "ramps up insulin production so that blood sugar stays in range. In the "
                "early stages this compensatory mechanism works: glucose levels remain "
                "normal while insulin quietly climbs. Over years, if the pancreas can no "
                "longer keep pace, blood sugar begins to rise — first into the prediabetes "
                "range and eventually, for some people, into type 2 diabetes.</p>"
                "<p>This is why a high fasting insulin level can appear <em>before</em> "
                "blood sugar becomes abnormal. It is sometimes described as a metabolic "
                "\"early warning\" — a sign that the system is under strain even though "
                "the headline glucose number still looks fine. That said, insulin resistance "
                "is not diagnosed from a single lab value; your doctor will consider your "
                "history, examination, and a combination of tests.</p>"
            ),
        ),
        Section(
            id="homa-ir-connection", level=2,
            heading="How fasting insulin connects to HOMA-IR",
            body_html=(
                "<p>One of the most common ways to put a fasting insulin result into "
                "context is the <strong>HOMA-IR</strong> index. HOMA-IR combines fasting "
                "insulin and fasting glucose in a simple formula to estimate the degree "
                "of insulin resistance:</p>"
                "<p><em>Fasting insulin (μU/mL) × Fasting glucose (mg/dL) ÷ 405</em></p>"
                "<p>Many references cite a HOMA-IR below 1.0 as optimal, while values "
                "above 2.5 may suggest insulin resistance — though cut-offs vary by "
                "population and method. The advantage of HOMA-IR over fasting insulin "
                "alone is that it accounts for glucose as well, giving a more balanced "
                "picture of the insulin–glucose relationship.</p>"
                "<p>For a deeper look at what HOMA-IR is and how to interpret it, see "
                "<a href=\"/en/blog/what-is-homa-ir\">our HOMA-IR guide</a>. That article "
                "explains the formula, reference ranges, and why HOMA-IR is a screening "
                "tool rather than a diagnostic test.</p>"
            ),
        ),
        Section(
            id="glucose-normal-insulin-high", level=2,
            heading="Why can glucose be normal while insulin is high?",
            body_html=(
                "<p>This is one of the most frequently asked questions — and one of the "
                "most important ones. Your "
                "<a href=\"/en/blog/how-to-read-fasting-blood-sugar-results\">fasting "
                "blood sugar</a> may look perfectly fine while your fasting insulin is "
                "already elevated. The reason is that your pancreas is working overtime: "
                "it produces extra insulin to push glucose into cells that have become "
                "resistant, and as long as this compensation succeeds, glucose stays "
                "within the normal range.</p>"
                "<p>This state is called <strong>compensatory hyperinsulinaemia</strong>. "
                "If you only look at fasting glucose, everything appears normal. But the "
                "insulin value reveals the metabolic effort taking place behind the scenes. "
                "This is one reason some clinicians order fasting insulin alongside glucose, "
                "especially for patients with a family history of diabetes or features of "
                "metabolic syndrome.</p>"
                "<p>In short: a normal glucose result does not automatically mean your "
                "metabolic health is optimal — adding insulin to the picture provides a "
                "wider view.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="What other tests are evaluated alongside fasting insulin?",
            body_html=(
                "<p>Fasting insulin is rarely interpreted in isolation. Your doctor may "
                "also review some or all of the following:</p>"
                "<ul>"
                "<li><strong>Fasting glucose</strong> — together with insulin, it feeds "
                "into the HOMA-IR calculation</li>"
                "<li><strong><a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c"
                "</a></strong> — reflects average blood sugar over the past 2–3 months</li>"
                "<li><strong>Triglycerides and HDL cholesterol</strong> — markers of "
                "metabolic syndrome</li>"
                "<li><strong>C-peptide</strong> — indicates how much insulin the pancreas "
                "is producing; can help distinguish type 1 from type 2 diabetes</li>"
                "<li><strong>OGTT (oral glucose tolerance test)</strong> — measures the "
                "body's response to a standardised glucose load</li>"
                "<li><strong>Waist circumference and BMI</strong> — physical parameters "
                "that contribute to metabolic risk assessment</li>"
                "</ul>"
                "<p>Which tests are ordered depends on your clinical situation and your "
                "doctor's judgement. The goal is to look at your metabolic picture as a "
                "whole, not at a single number.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Why a single result should not be interpreted alone",
            body_html=(
                "<p>A single fasting insulin measurement cannot define your health. Even "
                "a repeat test on the same day might yield a different number — because "
                "stress, sleep quality, your dinner the night before, and even the blood "
                "draw procedure itself can influence the result.</p>"
                "<p>Laboratory reference ranges are also not uniform; what one lab calls "
                "\"normal\" another may flag as \"borderline high\". For this reason, you "
                "should always consider your result together with:</p>"
                "<ul>"
                "<li>Your own laboratory's reference range</li>"
                "<li>Other blood values (glucose, HbA1c, lipid panel, etc.)</li>"
                "<li>Your medical and family history</li>"
                "<li>Your doctor's clinical examination findings</li>"
                "</ul>"
                "<p>Online reference values are useful for general orientation but should "
                "never replace a personalised medical assessment.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>Consider discussing your result with a healthcare professional if any "
                "of the following apply:</p>"
                "<ul>"
                "<li>Your fasting insulin is above the laboratory's reference range</li>"
                "<li>You have a family history of type 2 diabetes, metabolic syndrome, or "
                "cardiovascular disease</li>"
                "<li>You carry excess weight, especially around the waist, or have symptoms "
                "of PCOS</li>"
                "<li>You experience persistent fatigue, frequent hunger, or unexplained "
                "weight changes</li>"
                "<li>Your blood sugar appears normal but your insulin level is elevated</li>"
                "</ul>"
                "<p>Even without symptoms, sharing an abnormal result with your doctor is "
                "always a sensible step. Early awareness can open the door to lifestyle "
                "modifications that may reduce your metabolic risk over time.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Make your results easier to understand with Norya",
            body_html=(
                "<p>At Norya we do not diagnose — but we make it easier to understand your "
                "lab results. You can <a href=\"/analyze\">upload your lab report</a> and "
                "receive a structured summary that explains your values — including fasting "
                "insulin — in plain language, with reference ranges and context.</p>"
                "<p>This summary helps you ask the right questions when you talk to your "
                "doctor and evaluate your results more confidently. To see options and "
                "pricing, visit our <a href=\"/pricing\">pricing page</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This content is for information only and does not replace "
                "medical advice or diagnosis.</strong> Elevated fasting insulin can have "
                "many causes; only a healthcare professional who knows your history and "
                "context can interpret your result properly. Always discuss your lab "
                "results with a doctor.</p>"
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
            heading="Was bedeutet ein erhöhtes Nüchterninsulin?",
            body_html=(
                "<p>Wenn in Ihrem Laborbefund ein erhöhter <strong>Nüchterninsulin</strong>-Wert "
                "steht, tauchen schnell Fragen auf: Ist das gefährlich? Habe ich Diabetes? "
                "Warum ist mein Blutzucker normal, aber das Insulin hoch? Dieser Ratgeber "
                "erklärt, was Nüchterninsulin ist, was ein erhöhter Wert bedeuten kann und "
                "wie Sie Ihr Ergebnis richtig einordnen.</p>"
                "<p>Unser Ziel ist keine Diagnose — sondern Sie besser auf Ihr nächstes "
                "Arztgespräch vorzubereiten. Das Nüchterninsulin kann ein früher Hinweis "
                "auf metabolische Veränderungen sein, doch es ist niemals allein ein "
                "Diagnoseinstrument.</p>"
            ),
        ),
        Section(
            id="what-is-fasting-insulin", level=2,
            heading="Was ist Nüchterninsulin und wie wird es gemessen?",
            body_html=(
                "<p><strong>Insulin</strong> ist ein Hormon der Bauchspeicheldrüse, das "
                "Glukose (Blutzucker) in die Zellen schleust. Nach einer Mahlzeit steigt "
                "der Blutzucker, und die Bauchspeicheldrüse schüttet Insulin aus. "
                "<strong>Nüchterninsulin</strong> wird nach 8–12 Stunden ohne "
                "Nahrungsaufnahme gemessen, damit der Einfluss der letzten Mahlzeit "
                "entfällt und der basale Insulinspiegel bewertet werden kann.</p>"
                "<p>Die Ergebnisse werden meist in <strong>μU/mL</strong> (oder μIU/mL) "
                "angegeben. Referenzbereiche sind laborabhängig; häufig gilt etwa "
                "2–25 μU/mL als Normalbereich. Viele Ärzte sehen Werte unter 10 μU/mL "
                "als optimal an, doch diese Schwelle ist nicht universell. Alter, "
                "Geschlecht, BMI und die Messmethode beeinflussen das Ergebnis. Ihr "
                "Arzt beurteilt den Wert im Rahmen Ihres individuellen Befundes.</p>"
            ),
        ),
        Section(
            id="what-high-means", level=2,
            heading="Was kann ein erhöhtes Nüchterninsulin bedeuten?",
            body_html=(
                "<p>Ein hoher Nüchterninsulinwert deutet darauf hin, dass der Körper mehr "
                "Insulin produziert als erwartet, um den Blutzucker im Normalbereich zu "
                "halten. Man spricht von <strong>kompensatorischer Hyperinsulinämie</strong> "
                "— häufig ein frühes Zeichen nachlassender Insulinempfindlichkeit.</p>"
                "<p>Zustände, die mit erhöhtem Nüchterninsulin in Verbindung gebracht "
                "werden:</p>"
                "<ul>"
                "<li><strong>Insulinresistenz</strong> — verminderte zelluläre Reaktion "
                "auf Insulin</li>"
                "<li><strong>Metabolisches Syndrom</strong> — Kombination aus Bauchfett, "
                "hohen Triglyceriden, niedrigem HDL, Bluthochdruck und gestörtem "
                "Glukosestoffwechsel</li>"
                "<li><strong>Polyzystisches Ovarialsyndrom (PCOS)</strong></li>"
                "<li><strong>Nicht-alkoholische Fettleber (NAFLD)</strong></li>"
                "<li><strong>Erhöhtes kardiovaskuläres Risiko</strong></li>"
                "</ul>"
                "<p>Ein einzelner erhöhter Wert bestätigt jedoch keine dieser Diagnosen. "
                "Stress, Schlafmangel, bestimmte Medikamente und körperliche Anstrengung "
                "vor der Blutabnahme können das Ergebnis vorübergehend beeinflussen. Die "
                "Einordnung obliegt Ihrem Arzt.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-link", level=2,
            heading="Zusammenhang mit Insulinresistenz",
            body_html=(
                "<p><strong>Insulinresistenz</strong> bedeutet, dass Muskel-, Fett- und "
                "Leberzellen nicht mehr ausreichend auf Insulin reagieren. Die "
                "Bauchspeicheldrüse kompensiert, indem sie mehr Insulin ausschüttet. "
                "Im Frühstadium funktioniert das: Der Blutzucker bleibt normal, während "
                "der Insulinspiegel still ansteigt. Über Jahre kann die Bauchspeicheldrüse "
                "dieses Mehrpensum nicht aufrechterhalten — der Blutzucker steigt, zunächst "
                "in den Prädiabetes-Bereich, später möglicherweise in den Diabetes-Bereich.</p>"
                "<p>Ein erhöhtes Nüchterninsulin kann daher <em>vor</em> einer "
                "Blutzuckererhöhung auffallen und als metabolisches Frühwarnsignal gelten. "
                "Die Diagnose einer Insulinresistenz stützt sich nie auf einen einzelnen "
                "Laborwert; Ihr Arzt wird Anamnese, Untersuchung und weitere Befunde "
                "einbeziehen.</p>"
            ),
        ),
        Section(
            id="homa-ir-connection", level=2,
            heading="Verbindung zum HOMA-IR",
            body_html=(
                "<p>Ein verbreiteter Weg, das Nüchterninsulin in einen größeren "
                "Zusammenhang zu stellen, ist der <strong>HOMA-IR</strong>-Index. Er "
                "kombiniert Nüchterninsulin und Nüchternglukose in einer einfachen Formel, "
                "um den Grad der Insulinresistenz abzuschätzen:</p>"
                "<p><em>Nüchterninsulin (μU/mL) × Nüchternglukose (mg/dL) ÷ 405</em></p>"
                "<p>Viele Quellen betrachten einen HOMA-IR unter 1,0 als optimal; Werte "
                "über 2,5 können auf Insulinresistenz hinweisen — die Grenzwerte variieren "
                "aber je nach Population und Labormethode. Detaillierte Informationen "
                "finden Sie in <a href=\"/de/blog/homa-ir-was-bedeutet-das\">unserem "
                "HOMA-IR-Ratgeber</a>, der Formel, Referenzbereiche und die Grenzen des "
                "Index ausführlich erläutert.</p>"
            ),
        ),
        Section(
            id="glucose-normal-insulin-high", level=2,
            heading="Warum kann der Blutzucker normal sein, obwohl das Insulin hoch ist?",
            body_html=(
                "<p>Diese Frage stellen sich viele Patienten. Der "
                "<a href=\"/de/blog/nuechternblutzucker-verstehen\">Nüchternblutzucker</a> "
                "liegt im Normalbereich, doch das Nüchterninsulin ist erhöht. Der Grund: "
                "Die Bauchspeicheldrüse arbeitet härter als nötig, um die nachlassende "
                "Insulinempfindlichkeit auszugleichen. Solange diese Kompensation "
                "funktioniert, bleibt der Blutzucker unauffällig.</p>"
                "<p>Dieser Zustand heißt <strong>kompensatorische Hyperinsulinämie</strong>. "
                "Wer nur den Blutzucker betrachtet, übersieht möglicherweise die metabolische "
                "Belastung, die bereits begonnen hat. Deshalb fordern manche Ärzte — vor "
                "allem bei familiärer Diabetesbelastung oder Merkmalen des metabolischen "
                "Syndroms — gezielt das Nüchterninsulin an.</p>"
                "<p>Kurz gesagt: Ein normaler Blutzucker allein garantiert keine optimale "
                "Stoffwechsellage — das Insulin liefert ein zusätzliches Puzzleteil.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Welche weiteren Tests werden herangezogen?",
            body_html=(
                "<p>Nüchterninsulin wird selten isoliert betrachtet. Ihr Arzt bewertet "
                "häufig auch:</p>"
                "<ul>"
                "<li><strong>Nüchternglukose</strong> — zusammen mit Insulin geht sie in "
                "die HOMA-IR-Berechnung ein</li>"
                "<li><strong><a href=\"/de/blog/hba1c-verstehen-was-bedeutet-der-wert\">"
                "HbA1c</a></strong> — spiegelt den mittleren Blutzucker über 2–3 Monate "
                "wider</li>"
                "<li><strong>Triglyceride und HDL-Cholesterin</strong> — Marker des "
                "metabolischen Syndroms</li>"
                "<li><strong>C-Peptid</strong> — zeigt, wie viel Insulin die "
                "Bauchspeicheldrüse produziert</li>"
                "<li><strong>oGTT (oraler Glukosetoleranztest)</strong> — misst die "
                "Reaktion auf eine standardisierte Glukosebelastung</li>"
                "<li><strong>Bauchumfang und BMI</strong> — körperliche Parameter zur "
                "Risikobewertung</li>"
                "</ul>"
                "<p>Welche Tests angefordert werden, hängt von der klinischen "
                "Fragestellung ab. Ziel ist es, das metabolische Gesamtbild zu erfassen, "
                "nicht einen einzelnen Wert zu bewerten.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Warum reicht ein einzelner Wert nicht aus?",
            body_html=(
                "<p>Ein einzelner Nüchterninsulinwert definiert Ihren Gesundheitszustand "
                "nicht. Selbst eine Wiederholungsmessung am selben Tag kann abweichen — "
                "Stress, Schlafqualität, die Mahlzeit am Vorabend und sogar die "
                "Blutabnahme selbst können den Wert beeinflussen.</p>"
                "<p>Auch Referenzbereiche sind nicht einheitlich; was ein Labor als "
                "\"normal\" einstuft, kann anderswo als \"grenzwertig\" gelten. Deshalb "
                "sollten Sie Ihr Ergebnis immer zusammen mit dem eigenen Laborbereich, "
                "anderen Blutwerten, Ihrer Kranken- und Familiengeschichte sowie dem "
                "klinischen Befund Ihres Arztes betrachten. Online gelesene Schwellenwerte "
                "helfen bei der Orientierung, ersetzen aber keine ärztliche Beurteilung.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Sprechen Sie Ihr Ergebnis mit einem Arzt, wenn:</p>"
                "<ul>"
                "<li>Ihr Nüchterninsulin über dem Referenzbereich liegt</li>"
                "<li>In Ihrer Familie Typ-2-Diabetes, metabolisches Syndrom oder "
                "Herz-Kreislauf-Erkrankungen vorkommen</li>"
                "<li>Sie Übergewicht, besonders am Bauch, oder PCOS-Symptome haben</li>"
                "<li>Sie unter anhaltender Müdigkeit, häufigem Hunger oder unerklärlicher "
                "Gewichtsveränderung leiden</li>"
                "<li>Ihr Blutzucker normal, aber das Insulin erhöht ist</li>"
                "</ul>"
                "<p>Auch ohne Beschwerden ist es sinnvoll, auffällige Werte dem Arzt "
                "mitzuteilen. Frühes Erkennen ermöglicht Lebensstilanpassungen, die das "
                "metabolische Risiko langfristig senken können.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Verstehen Sie Ihre Ergebnisse besser mit Norya",
            body_html=(
                "<p>Bei Norya stellen wir keine Diagnosen — aber wir machen es leichter, "
                "Ihre Laborergebnisse zu verstehen. <a href=\"/analyze\">Laden Sie Ihren "
                "Laborbefund hoch</a> und erhalten Sie eine strukturierte Zusammenfassung, "
                "die Ihre Werte — einschließlich Nüchterninsulin — in verständlicher "
                "Sprache mit Referenzbereichen und Kontext erklärt.</p>"
                "<p>So können Sie im Arztgespräch die richtigen Fragen stellen. "
                "Optionen und Preise finden Sie auf unserer "
                "<a href=\"/pricing\">Preisseite</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                "<p><strong>Dieser Inhalt dient ausschließlich der Information und "
                "ersetzt keine ärztliche Beratung oder Diagnose.</strong> Ein erhöhtes "
                "Nüchterninsulin kann viele Ursachen haben; nur ein Arzt, der Ihre "
                "Vorgeschichte kennt, kann Ihr Ergebnis sachgerecht beurteilen. "
                "Besprechen Sie Ihre Laborergebnisse immer mit einem Arzt.</p>"
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
            heading="¿Qué significa tener la insulina en ayunas alta?",
            body_html=(
                "<p>Si en tu análisis de sangre aparece un valor elevado de "
                "<strong>insulina en ayunas</strong>, es natural que surjan preguntas: "
                "¿Es grave? ¿Tengo diabetes? ¿Por qué mi glucosa sale normal pero la "
                "insulina está alta? Esta guía explica qué es la insulina en ayunas, qué "
                "puede indicar un resultado alto y cómo interpretarlo correctamente.</p>"
                "<p>Nuestro objetivo no es diagnosticar, sino ayudarte a llegar a tu "
                "próxima consulta médica mejor informado. La insulina en ayunas puede ser "
                "una señal metabólica temprana, pero nunca es, por sí sola, un diagnóstico.</p>"
            ),
        ),
        Section(
            id="what-is-fasting-insulin", level=2,
            heading="¿Qué es la insulina en ayunas y cómo se mide?",
            body_html=(
                "<p>La <strong>insulina</strong> es una hormona producida por el páncreas "
                "que permite que la glucosa entre en las células para obtener energía. "
                "Después de comer, la glucosa sube y el páncreas libera insulina. La "
                "<strong>insulina en ayunas</strong> se mide tras 8–12 horas sin ingerir "
                "alimentos, eliminando el efecto de la última comida y reflejando el nivel "
                "basal de insulina del organismo.</p>"
                "<p>Los resultados suelen expresarse en <strong>μU/mL</strong>. Los "
                "rangos de referencia varían según el laboratorio; un intervalo habitual "
                "es 2–25 μU/mL, y muchos clínicos consideran óptimo un valor inferior a "
                "10 μU/mL. La edad, el sexo, el IMC y el método analítico influyen en el "
                "resultado. Tu médico lo interpretará dentro de tu propio contexto clínico.</p>"
            ),
        ),
        Section(
            id="what-high-means", level=2,
            heading="¿Qué puede indicar una insulina en ayunas elevada?",
            body_html=(
                "<p>Un valor alto sugiere que el organismo produce más insulina de lo "
                "esperado para mantener la glucosa en rango. Esto se conoce como "
                "<strong>hiperinsulinemia compensatoria</strong> y suele ser un indicio "
                "temprano de que las células responden menos a la insulina.</p>"
                "<p>Situaciones asociadas con insulina en ayunas elevada:</p>"
                "<ul>"
                "<li><strong>Resistencia a la insulina</strong></li>"
                "<li><strong>Síndrome metabólico</strong> — obesidad abdominal, "
                "triglicéridos altos, HDL bajo, tensión arterial elevada y glucosa "
                "alterada</li>"
                "<li><strong>Síndrome de ovario poliquístico (SOP)</strong></li>"
                "<li><strong>Hígado graso no alcohólico (HGNA)</strong></li>"
                "<li><strong>Mayor riesgo cardiovascular</strong></li>"
                "</ul>"
                "<p>Un único valor elevado no confirma ninguna de estas condiciones. "
                "El estrés, el insomnio, ciertos medicamentos y el ejercicio intenso "
                "reciente pueden elevar la insulina de forma transitoria. La "
                "interpretación corresponde siempre al médico.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-link", level=2,
            heading="Relación con la resistencia a la insulina",
            body_html=(
                "<p>La <strong>resistencia a la insulina</strong> se produce cuando las "
                "células de músculo, grasa e hígado dejan de responder eficientemente a la "
                "insulina. El páncreas compensa aumentando la producción: la glucosa se "
                "mantiene normal mientras la insulina sube silenciosamente. Con el tiempo, "
                "si el páncreas ya no puede seguir el ritmo, la glucosa empieza a "
                "elevarse — primero prediabetes y, en algunos casos, diabetes tipo 2.</p>"
                "<p>Por eso la insulina en ayunas alta puede aparecer <em>antes</em> de "
                "que la glucosa se altere, actuando como una señal de alarma metabólica "
                "temprana. La resistencia a la insulina no se diagnostica con un solo "
                "valor: el médico valorará historia, exploración y otros análisis.</p>"
            ),
        ),
        Section(
            id="homa-ir-connection", level=2,
            heading="Conexión con el HOMA-IR",
            body_html=(
                "<p>Una forma habitual de contextualizar la insulina en ayunas es calcular "
                "el <strong>HOMA-IR</strong>, que combina insulina y glucosa en ayunas:</p>"
                "<p><em>Insulina en ayunas (μU/mL) × Glucosa en ayunas (mg/dL) ÷ 405</em></p>"
                "<p>Muchas referencias consideran óptimo un HOMA-IR inferior a 1,0; "
                "valores por encima de 2,5 pueden sugerir resistencia a la insulina, "
                "aunque los puntos de corte varían. Para entender a fondo el HOMA-IR, "
                "consulta <a href=\"/es/blog/que-es-homa-ir\">nuestra guía de HOMA-IR</a>, "
                "que explica la fórmula, los rangos y sus limitaciones.</p>"
            ),
        ),
        Section(
            id="glucose-normal-insulin-high", level=2,
            heading="¿Por qué la glucosa puede ser normal con la insulina alta?",
            body_html=(
                "<p>Tu <a href=\"/es/blog/como-leer-glucosa-en-ayunas\">glucosa en ayunas"
                "</a> puede aparecer en rango normal mientras la insulina ya está elevada. "
                "La razón: el páncreas trabaja de más para compensar la resistencia "
                "celular. Mientras lo consiga, la glucosa se mantiene dentro de límites.</p>"
                "<p>Este estado se llama <strong>hiperinsulinemia compensatoria</strong>. "
                "Mirar solo la glucosa puede dar una falsa sensación de normalidad; la "
                "insulina revela el esfuerzo metabólico que ya está en marcha. Por eso "
                "algunos médicos solicitan insulina en ayunas, sobre todo si hay "
                "antecedentes familiares de diabetes o rasgos de síndrome metabólico.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="¿Qué otros análisis se valoran junto a la insulina en ayunas?",
            body_html=(
                "<p>La insulina en ayunas rara vez se interpreta sola. Tu médico puede "
                "valorar también:</p>"
                "<ul>"
                "<li><strong>Glucosa en ayunas</strong> — junto con la insulina, permite "
                "calcular el HOMA-IR</li>"
                "<li><strong><a href=\"/es/blog/hba1c-que-significa-el-resultado\">HbA1c"
                "</a></strong> — refleja la glucosa media de los últimos 2–3 meses</li>"
                "<li><strong>Triglicéridos y colesterol HDL</strong></li>"
                "<li><strong>Péptido C</strong> — indica la capacidad de producción de "
                "insulina del páncreas</li>"
                "<li><strong>SOG (sobrecarga oral de glucosa)</strong></li>"
                "<li><strong>Perímetro de cintura e IMC</strong></li>"
                "</ul>"
                "<p>El objetivo es ver el cuadro metabólico completo, no un número "
                "aislado.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="¿Por qué un solo resultado no basta?",
            body_html=(
                "<p>Un único valor de insulina en ayunas no define tu salud. Incluso "
                "repitiendo la prueba el mismo día, el resultado puede variar por estrés, "
                "sueño, alimentación previa o la propia extracción de sangre. Además, "
                "los rangos de referencia difieren entre laboratorios.</p>"
                "<p>Valora siempre tu resultado junto con tu rango de laboratorio, otros "
                "análisis (glucosa, HbA1c, lípidos), tu historia clínica y familiar, y "
                "la exploración de tu médico. Los valores que lees en internet son "
                "orientativos, pero no sustituyen la valoración personalizada.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo deberías consultar al médico?",
            body_html=(
                "<p>Comenta tu resultado con un profesional sanitario si:</p>"
                "<ul>"
                "<li>Tu insulina en ayunas supera el rango de referencia</li>"
                "<li>Hay antecedentes familiares de diabetes tipo 2, síndrome metabólico "
                "o enfermedad cardiovascular</li>"
                "<li>Tienes sobrepeso abdominal o síntomas de SOP</li>"
                "<li>Experimentas fatiga persistente, hambre frecuente o cambios de peso "
                "sin explicación</li>"
                "<li>Tu glucosa es normal pero la insulina sale elevada</li>"
                "</ul>"
                "<p>Incluso sin síntomas, compartir un valor anormal con tu médico siempre "
                "es una buena decisión. La detección precoz abre la puerta a cambios de "
                "estilo de vida que pueden reducir el riesgo metabólico.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Entiende mejor tus resultados con Norya",
            body_html=(
                "<p>En Norya no diagnosticamos, pero te ayudamos a entender tus análisis. "
                "<a href=\"/analyze\">Sube tu informe</a> y recibe un resumen estructurado "
                "que explica tus valores — incluida la insulina en ayunas — en lenguaje "
                "claro, con rangos de referencia y contexto.</p>"
                "<p>Así podrás hacer las preguntas adecuadas en tu consulta. Consulta "
                "opciones y precios en nuestra <a href=\"/pricing\">página de precios</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                "<p><strong>Este contenido es solo informativo y no sustituye el consejo "
                "médico ni un diagnóstico.</strong> La insulina en ayunas elevada puede "
                "tener muchas causas; solo un profesional que conozca tu historial puede "
                "interpretar correctamente tu resultado. Comenta siempre tus análisis "
                "con un médico.</p>"
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
            heading="Que signifie une insuline à jeun élevée ?",
            body_html=(
                "<p>Si votre bilan sanguin indique un taux d\u2019<strong>insuline à jeun"
                "</strong> élevé, des questions surgissent : est-ce grave ? Ai-je du "
                "diabète ? Pourquoi ma glycémie est-elle normale alors que l\u2019insuline "
                "est haute ? Ce guide explique ce qu\u2019est l\u2019insuline à jeun, ce "
                "qu\u2019un résultat élevé peut signifier et comment l\u2019interpréter.</p>"
                "<p>Notre objectif n\u2019est pas de poser un diagnostic mais de vous "
                "aider à préparer votre prochaine consultation. L\u2019insuline à jeun "
                "peut être un signal métabolique précoce, mais elle n\u2019est jamais un "
                "diagnostic à elle seule.</p>"
            ),
        ),
        Section(
            id="what-is-fasting-insulin", level=2,
            heading="Qu\u2019est-ce que l\u2019insuline à jeun et comment est-elle mesurée ?",
            body_html=(
                "<p>L\u2019<strong>insuline</strong> est une hormone produite par le "
                "pancréas qui permet au glucose d\u2019entrer dans les cellules. Après un "
                "repas, la glycémie augmente et le pancréas sécrète de l\u2019insuline. "
                "L\u2019<strong>insuline à jeun</strong> est dosée après 8 à 12 heures "
                "sans nourriture, ce qui élimine l\u2019influence du dernier repas et "
                "reflète le niveau basal d\u2019insuline.</p>"
                "<p>Les résultats sont généralement exprimés en <strong>μU/mL</strong>. "
                "Les fourchettes de référence varient ; un intervalle courant est "
                "2–25 μU/mL, et de nombreux praticiens considèrent une valeur inférieure "
                "à 10 μU/mL comme optimale. Âge, sexe, IMC et méthode de dosage influencent "
                "le résultat. Votre médecin l\u2019interprète dans votre contexte clinique.</p>"
            ),
        ),
        Section(
            id="what-high-means", level=2,
            heading="Que peut indiquer une insuline à jeun élevée ?",
            body_html=(
                "<p>Un taux élevé suggère que l\u2019organisme produit plus d\u2019insuline "
                "que prévu pour maintenir la glycémie. C\u2019est ce qu\u2019on appelle "
                "<strong>hyperinsulinémie compensatoire</strong>, souvent un signe précoce "
                "de baisse de la sensibilité à l\u2019insuline.</p>"
                "<p>Situations fréquemment associées :</p>"
                "<ul>"
                "<li><strong>Insulinorésistance</strong></li>"
                "<li><strong>Syndrome métabolique</strong> — obésité abdominale, "
                "triglycérides élevés, HDL bas, HTA, glycémie altérée</li>"
                "<li><strong>Syndrome des ovaires polykystiques (SOPK)</strong></li>"
                "<li><strong>Stéatose hépatique non alcoolique (NAFLD)</strong></li>"
                "<li><strong>Risque cardiovasculaire accru</strong></li>"
                "</ul>"
                "<p>Une seule valeur élevée ne confirme aucun de ces diagnostics. Le "
                "stress, le manque de sommeil, certains médicaments ou un effort physique "
                "récent peuvent élever transitoirement l\u2019insuline. L\u2019interprétation "
                "revient toujours au médecin.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-link", level=2,
            heading="Le lien avec l\u2019insulinorésistance",
            body_html=(
                "<p>L\u2019<strong>insulinorésistance</strong> signifie que les cellules "
                "musculaires, adipeuses et hépatiques répondent moins bien à l\u2019insuline. "
                "Le pancréas compense en produisant davantage. Au début, la glycémie reste "
                "normale ; au fil du temps, si le pancréas ne suit plus, la glycémie "
                "s\u2019élève — d\u2019abord vers le prédiabète, puis éventuellement le "
                "diabète de type 2.</p>"
                "<p>Une insuline à jeun élevée peut donc apparaître <em>avant</em> toute "
                "anomalie glycémique, constituant un signal d\u2019alerte métabolique "
                "précoce. Le diagnostic d\u2019insulinorésistance repose sur l\u2019ensemble "
                "du bilan clinique et biologique.</p>"
            ),
        ),
        Section(
            id="homa-ir-connection", level=2,
            heading="Le lien avec le HOMA-IR",
            body_html=(
                "<p>Pour contextualiser l\u2019insuline à jeun, on calcule souvent le "
                "<strong>HOMA-IR</strong>, qui combine insuline et glycémie à jeun :</p>"
                "<p><em>Insuline à jeun (μU/mL) × Glycémie à jeun (mg/dL) ÷ 405</em></p>"
                "<p>Un HOMA-IR inférieur à 1,0 est souvent considéré comme optimal ; "
                "au-delà de 2,5 une insulinorésistance est possible. Pour approfondir, "
                "consultez <a href=\"/fr/blog/quest-ce-que-homa-ir\">notre guide HOMA-IR"
                "</a> qui détaille la formule et ses limites.</p>"
            ),
        ),
        Section(
            id="glucose-normal-insulin-high", level=2,
            heading="Pourquoi la glycémie peut-elle être normale alors que l\u2019insuline est haute ?",
            body_html=(
                "<p>Votre <a href=\"/fr/blog/comment-lire-glycemie-a-jeun\">glycémie à "
                "jeun</a> peut être dans les normes tandis que l\u2019insuline est élevée. "
                "Le pancréas travaille en surrégime pour compenser la résistance cellulaire ; "
                "tant que cette compensation fonctionne, la glycémie reste dans les "
                "limites.</p>"
                "<p>Cet état s\u2019appelle <strong>hyperinsulinémie compensatoire</strong>. "
                "Se fier à la seule glycémie peut masquer un effort métabolique déjà en "
                "cours. C\u2019est pourquoi certains médecins prescrivent l\u2019insuline "
                "à jeun, en particulier en cas d\u2019antécédents familiaux de diabète ou "
                "de facteurs de risque métabolique.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Quels autres examens sont évalués ?",
            body_html=(
                "<p>L\u2019insuline à jeun est rarement interprétée seule. Votre médecin "
                "peut également examiner :</p>"
                "<ul>"
                "<li><strong>Glycémie à jeun</strong> — entre dans le calcul du HOMA-IR</li>"
                "<li><strong><a href=\"/fr/blog/hba1c-comprendre-resultat\">HbA1c</a>"
                "</strong> — reflet de la glycémie moyenne sur 2–3 mois</li>"
                "<li><strong>Triglycérides et HDL</strong></li>"
                "<li><strong>Peptide C</strong></li>"
                "<li><strong>HGPO (hyperglycémie provoquée orale)</strong></li>"
                "<li><strong>Tour de taille et IMC</strong></li>"
                "</ul>"
                "<p>L\u2019objectif est de dresser un tableau métabolique global, pas de "
                "juger un chiffre isolé.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Pourquoi un seul résultat ne suffit-il pas ?",
            body_html=(
                "<p>Un dosage isolé d\u2019insuline à jeun ne définit pas votre santé. "
                "Le stress, le sommeil, le repas de la veille et la prise de sang "
                "elle-même peuvent influencer le chiffre. Les fourchettes de référence "
                "diffèrent d\u2019un laboratoire à l\u2019autre.</p>"
                "<p>Évaluez toujours votre résultat en tenant compte de vos normes de "
                "laboratoire, de vos autres bilans, de vos antécédents et de l\u2019examen "
                "clinique de votre médecin. Les valeurs trouvées en ligne orientent mais "
                "ne remplacent pas un avis médical personnalisé.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Parlez de votre résultat à un professionnel de santé si :</p>"
                "<ul>"
                "<li>Votre insuline à jeun dépasse la fourchette de référence</li>"
                "<li>Vous avez des antécédents familiaux de diabète de type 2 ou de "
                "syndrome métabolique</li>"
                "<li>Vous présentez un surpoids abdominal ou des symptômes de SOPK</li>"
                "<li>Vous ressentez une fatigue persistante, une faim fréquente ou des "
                "variations de poids inexpliquées</li>"
                "<li>Votre glycémie est normale mais votre insuline est haute</li>"
                "</ul>"
                "<p>Même sans symptôme, signaler une valeur anormale à votre médecin est "
                "toujours judicieux. Une prise de conscience précoce ouvre la voie à des "
                "ajustements de mode de vie.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comprenez mieux vos résultats avec Norya",
            body_html=(
                "<p>Chez Norya, nous ne diagnostiquons pas — mais nous vous aidons à "
                "comprendre vos analyses. <a href=\"/analyze\">Téléchargez votre bilan"
                "</a> et recevez un résumé structuré qui explique vos valeurs — y compris "
                "l\u2019insuline à jeun — en langage clair, avec fourchettes et contexte.</p>"
                "<p>Consultez nos <a href=\"/pricing\">tarifs</a> pour en savoir plus.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                "<p><strong>Ce contenu est fourni à titre informatif et ne remplace ni "
                "un avis médical ni un diagnostic.</strong> Une insuline à jeun élevée "
                "peut avoir de nombreuses causes ; seul un professionnel de santé "
                "connaissant votre dossier peut interpréter correctement votre résultat. "
                "Discutez toujours de vos analyses avec un médecin.</p>"
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
            heading="Cosa significa avere l\u2019insulina a digiuno alta?",
            body_html=(
                "<p>Se nel referto del tuo esame del sangue compare un valore elevato di "
                "<strong>insulina a digiuno</strong>, le domande sorgono spontanee: è "
                "grave? Ho il diabete? Perché la glicemia è normale ma l\u2019insulina è "
                "alta? Questa guida spiega cos\u2019è l\u2019insulina a digiuno, cosa può "
                "indicare un risultato alto e come inquadrare correttamente il valore.</p>"
                "<p>Il nostro obiettivo non è formulare diagnosi, ma aiutarti ad arrivare "
                "al prossimo appuntamento medico più consapevole. L\u2019insulina a digiuno "
                "può essere un segnale metabolico precoce, ma da sola non è mai una "
                "diagnosi.</p>"
            ),
        ),
        Section(
            id="what-is-fasting-insulin", level=2,
            heading="Cos\u2019è l\u2019insulina a digiuno e come si misura?",
            body_html=(
                "<p>L\u2019<strong>insulina</strong> è un ormone prodotto dal pancreas che "
                "consente al glucosio di entrare nelle cellule. Dopo un pasto, la glicemia "
                "sale e il pancreas rilascia insulina. L\u2019<strong>insulina a digiuno"
                "</strong> viene dosata dopo 8–12 ore senza cibo, così da eliminare "
                "l\u2019effetto dell\u2019ultimo pasto e valutare il livello insulinemico "
                "basale.</p>"
                "<p>I risultati si esprimono in <strong>μU/mL</strong>. Gli intervalli di "
                "riferimento variano; tipicamente 2–25 μU/mL è considerato normale, e "
                "molti medici ritengono ottimale un valore sotto 10 μU/mL. Età, sesso, "
                "BMI e metodo analitico influiscono. Il medico interpreta il dato nel "
                "tuo contesto clinico.</p>"
            ),
        ),
        Section(
            id="what-high-means", level=2,
            heading="Cosa può indicare un\u2019insulina a digiuno elevata?",
            body_html=(
                "<p>Un valore alto suggerisce che l\u2019organismo produce più insulina "
                "del previsto per tenere la glicemia entro i limiti. Si parla di "
                "<strong>iperinsulinemia compensatoria</strong>, spesso segno precoce di "
                "ridotta sensibilità all\u2019insulina.</p>"
                "<p>Situazioni comunemente associate:</p>"
                "<ul>"
                "<li><strong>Resistenza insulinica</strong></li>"
                "<li><strong>Sindrome metabolica</strong> — obesità addominale, "
                "trigliceridi alti, HDL basso, pressione elevata, glicemia alterata</li>"
                "<li><strong>Sindrome dell\u2019ovaio policistico (PCOS)</strong></li>"
                "<li><strong>Steatosi epatica non alcolica (NAFLD)</strong></li>"
                "<li><strong>Aumento del rischio cardiovascolare</strong></li>"
                "</ul>"
                "<p>Un singolo valore elevato non conferma alcuna di queste condizioni. "
                "Stress, sonno insufficiente, farmaci e attività fisica intensa prima "
                "del prelievo possono influenzare transitoriamente il risultato. "
                "L\u2019interpretazione spetta sempre al medico.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-link", level=2,
            heading="Il legame con la resistenza insulinica",
            body_html=(
                "<p>La <strong>resistenza insulinica</strong> indica che le cellule "
                "muscolari, adipose ed epatiche rispondono meno all\u2019insulina. Il "
                "pancreas compensa producendone di più: inizialmente la glicemia resta "
                "normale; nel tempo, se il pancreas non riesce più a tenere il ritmo, la "
                "glicemia sale — prima verso il prediabete, poi potenzialmente verso il "
                "diabete di tipo 2.</p>"
                "<p>Un\u2019insulina a digiuno elevata può quindi comparire <em>prima</em> "
                "di qualsiasi anomalia glicemica, fungendo da segnale di allarme "
                "metabolico precoce. La diagnosi si basa su un quadro clinico completo, "
                "non su un singolo dato.</p>"
            ),
        ),
        Section(
            id="homa-ir-connection", level=2,
            heading="Collegamento con il HOMA-IR",
            body_html=(
                "<p>Per contestualizzare l\u2019insulina a digiuno si calcola spesso "
                "il <strong>HOMA-IR</strong>, che unisce insulinemia e glicemia a digiuno:</p>"
                "<p><em>Insulina a digiuno (μU/mL) × Glicemia a digiuno (mg/dL) ÷ 405</em></p>"
                "<p>Un HOMA-IR sotto 1,0 è spesso considerato ottimale; sopra 2,5 potrebbe "
                "indicare resistenza insulinica. Per un approfondimento, leggi "
                "<a href=\"/it/blog/cos-e-homa-ir\">la nostra guida HOMA-IR</a> con "
                "formula, intervalli e limiti dell\u2019indice.</p>"
            ),
        ),
        Section(
            id="glucose-normal-insulin-high", level=2,
            heading="Perché la glicemia può essere normale con l\u2019insulina alta?",
            body_html=(
                "<p>La tua <a href=\"/it/blog/come-leggere-glicemia-a-digiuno\">glicemia "
                "a digiuno</a> può risultare normale mentre l\u2019insulina è già elevata. "
                "Il pancreas lavora più del dovuto per compensare la minore risposta "
                "cellulare; finché la compensazione riesce, la glicemia resta nei limiti.</p>"
                "<p>Questo stato è detto <strong>iperinsulinemia compensatoria</strong>. "
                "Guardare solo la glicemia può dare una falsa impressione di normalità; "
                "l\u2019insulina rivela lo sforzo metabolico in atto. Ecco perché alcuni "
                "medici richiedono l\u2019insulinemia a digiuno, specie in presenza di "
                "familiarità diabetica o fattori di rischio metabolico.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Quali altri esami vengono valutati insieme?",
            body_html=(
                "<p>L\u2019insulina a digiuno non si interpreta da sola. Il medico può "
                "valutare anche:</p>"
                "<ul>"
                "<li><strong>Glicemia a digiuno</strong> — con l\u2019insulina entra nel "
                "calcolo del HOMA-IR</li>"
                "<li><strong><a href=\"/it/blog/hba1c-cosa-significa-il-valore\">HbA1c"
                "</a></strong> — glicemia media degli ultimi 2–3 mesi</li>"
                "<li><strong>Trigliceridi e colesterolo HDL</strong></li>"
                "<li><strong>Peptide C</strong></li>"
                "<li><strong>OGTT (test da carico orale di glucosio)</strong></li>"
                "<li><strong>Circonferenza vita e BMI</strong></li>"
                "</ul>"
                "<p>L\u2019obiettivo è avere un quadro metabolico completo, non giudicare "
                "un singolo numero.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Perché un singolo risultato non basta?",
            body_html=(
                "<p>Un unico dosaggio di insulina a digiuno non definisce la tua salute. "
                "Anche ripetendo l\u2019esame nello stesso giorno il valore può variare "
                "per stress, qualità del sonno, cena della sera prima e procedura di "
                "prelievo. Gli intervalli di riferimento differiscono tra laboratori.</p>"
                "<p>Valuta sempre il risultato insieme alle tue norme di laboratorio, "
                "agli altri esami (glicemia, HbA1c, profilo lipidico), alla tua storia "
                "clinica e familiare e alla visita medica. I valori trovati online sono "
                "indicativi, non sostitutivi di una valutazione personalizzata.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Parla del tuo risultato con un professionista sanitario se:</p>"
                "<ul>"
                "<li>La tua insulina a digiuno supera l\u2019intervallo di riferimento</li>"
                "<li>Hai familiarità per diabete di tipo 2, sindrome metabolica o "
                "malattie cardiovascolari</li>"
                "<li>Presenti sovrappeso addominale o sintomi di PCOS</li>"
                "<li>Soffri di stanchezza persistente, fame frequente o variazioni di "
                "peso inspiegabili</li>"
                "<li>La tua glicemia è normale ma l\u2019insulina è alta</li>"
                "</ul>"
                "<p>Anche in assenza di sintomi, segnalare un valore anomalo al medico è "
                "sempre la scelta giusta. La consapevolezza precoce apre la strada a "
                "modifiche dello stile di vita.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comprendi meglio i tuoi risultati con Norya",
            body_html=(
                "<p>In Norya non formuliamo diagnosi, ma ti aiutiamo a capire i tuoi "
                "esami. <a href=\"/analyze\">Carica il tuo referto</a> e ricevi un "
                "riepilogo strutturato che spiega i tuoi valori — compresa l\u2019insulina "
                "a digiuno — in linguaggio chiaro, con intervalli e contesto.</p>"
                "<p>Per opzioni e prezzi, visita la nostra <a href=\"/pricing\">pagina "
                "prezzi</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>Questo contenuto ha finalità esclusivamente informative e non "
                "sostituisce il parere medico né una diagnosi.</strong> Un\u2019insulina a "
                "digiuno elevata può avere molteplici cause; solo un professionista che "
                "conosce la tua storia può interpretare correttamente il risultato. "
                "Discuti sempre i tuoi esami con un medico.</p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW (RTL)
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="\u05de\u05d4 \u05de\u05e9\u05de\u05e2\u05d5\u05ea \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4?",
            body_html=(
                "<p>\u05d0\u05dd \u05d1\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05d4\u05d3\u05dd \u05e9\u05dc\u05db\u05dd \u05de\u05d5\u05e4\u05d9\u05e2 \u05e2\u05e8\u05da \u05d2\u05d1\u05d5\u05d4 \u05e9\u05dc "
                "<strong>\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd</strong>, \u05d8\u05d1\u05e2\u05d9 \u05e9\u05ea\u05e9\u05d0\u05dc\u05d5: \u05d4\u05d0\u05dd "
                "\u05d6\u05d4 \u05de\u05e1\u05d5\u05db\u05df? \u05d4\u05d0\u05dd \u05d9\u05e9 \u05dc\u05d9 \u05e1\u05d5\u05db\u05e8\u05ea? \u05dc\u05de\u05d4 \u05d4\u05e1\u05d5\u05db\u05e8 "
                "\u05ea\u05e7\u05d9\u05df \u05d0\u05d1\u05dc \u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d2\u05d1\u05d5\u05d4? \u05de\u05d3\u05e8\u05d9\u05da \u05d6\u05d4 "
                "\u05de\u05e1\u05d1\u05d9\u05e8 \u05de\u05d4\u05d5 \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd, \u05de\u05d4 \u05e2\u05e8\u05da "
                "\u05d2\u05d1\u05d5\u05d4 \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05e6\u05d1\u05d9\u05e2, \u05d5\u05d0\u05d9\u05da \u05dc\u05e4\u05e8\u05e9 "
                "\u05d0\u05ea \u05d4\u05ea\u05d5\u05e6\u05d0\u05d4 \u05d1\u05d4\u05e7\u05e9\u05e8 \u05d4\u05e0\u05db\u05d5\u05df.</p>"
                "<p>\u05d4\u05de\u05d8\u05e8\u05d4 \u05e9\u05dc\u05e0\u05d5 \u05d0\u05d9\u05e0\u05d4 \u05dc\u05d0\u05d1\u05d7\u05df \u2014 \u05d0\u05dc\u05d0 "
                "\u05dc\u05e2\u05d6\u05d5\u05e8 \u05dc\u05db\u05dd \u05dc\u05d4\u05d2\u05d9\u05e2 \u05dc\u05e4\u05d2\u05d9\u05e9\u05d4 \u05e2\u05dd "
                "\u05d4\u05e8\u05d5\u05e4\u05d0 \u05de\u05d5\u05db\u05e0\u05d9\u05dd \u05d9\u05d5\u05ea\u05e8. \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df "
                "\u05d1\u05e6\u05d5\u05dd \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05d9\u05d5\u05ea \u05d0\u05d5\u05ea \u05de\u05d8\u05d1\u05d5\u05dc\u05d9 "
                "\u05de\u05d5\u05e7\u05d3\u05dd, \u05d0\u05da \u05dc\u05e2\u05d5\u05dc\u05dd \u05d0\u05d9\u05e0\u05d5 \u05d0\u05d1\u05d7\u05e0\u05d4 "
                "\u05d1\u05e4\u05e0\u05d9 \u05e2\u05e6\u05de\u05d5.</p>"
            ),
        ),
        Section(
            id="what-is-fasting-insulin", level=2,
            heading="\u05de\u05d4\u05d5 \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d5\u05d0\u05d9\u05da \u05d4\u05d5\u05d0 \u05e0\u05de\u05d3\u05d3?",
            body_html=(
                "<p><strong>\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df</strong> \u05d4\u05d5\u05d0 \u05d4\u05d5\u05e8\u05de\u05d5\u05df "
                "\u05e9\u05de\u05d9\u05d5\u05e6\u05e8 \u05e2\u05dc \u05d9\u05d3\u05d9 \u05d4\u05dc\u05d1\u05dc\u05d1 \u05d5\u05de\u05d0\u05e4\u05e9\u05e8 "
                "\u05dc\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05dc\u05d4\u05d9\u05db\u05e0\u05e1 \u05dc\u05ea\u05d0\u05d9\u05dd. \u05d0\u05d7\u05e8\u05d9 "
                "\u05d0\u05e8\u05d5\u05d7\u05d4 \u05e8\u05de\u05ea \u05d4\u05e1\u05d5\u05db\u05e8 \u05e2\u05d5\u05dc\u05d4 \u05d5\u05d4\u05dc\u05d1\u05dc\u05d1 "
                "\u05de\u05e4\u05e8\u05d9\u05e9 \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df. <strong>\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df "
                "\u05d1\u05e6\u05d5\u05dd</strong> \u05e0\u05de\u05d3\u05d3 \u05dc\u05d0\u05d7\u05e8 8\u201312 \u05e9\u05e2\u05d5\u05ea \u05dc\u05dc\u05d0 "
                "\u05d0\u05db\u05d9\u05dc\u05d4, \u05db\u05d3\u05d9 \u05dc\u05d4\u05e2\u05e8\u05d9\u05da \u05d0\u05ea \u05e8\u05de\u05ea "
                "\u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d4\u05d1\u05e1\u05d9\u05e1\u05d9\u05ea.</p>"
                "<p>\u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05de\u05d3\u05d5\u05d5\u05d7\u05d5\u05ea \u05d1\u05d3\u05e8\u05da \u05db\u05dc\u05dc "
                "\u05d1-<strong>\u03bcU/mL</strong>. \u05d8\u05d5\u05d5\u05d7 \u05e0\u05e4\u05d5\u05e5 \u05d4\u05d5\u05d0 \u05d1\u05e2\u05e8\u05da "
                "2\u201325 \u03bcU/mL; \u05e8\u05d5\u05e4\u05d0\u05d9\u05dd \u05e8\u05d1\u05d9\u05dd \u05e8\u05d5\u05d0\u05d9\u05dd \u05d1\u05e2\u05e8\u05da "
                "\u05de\u05ea\u05d7\u05ea 10 \u03bcU/mL \u05db\u05d0\u05d5\u05e4\u05d8\u05d9\u05de\u05dc\u05d9. \u05d2\u05d9\u05dc, \u05de\u05d9\u05df, "
                "BMI \u05d5\u05e9\u05d9\u05d8\u05ea \u05d4\u05d1\u05d3\u05d9\u05e7\u05d4 \u05de\u05e9\u05e4\u05d9\u05e2\u05d9\u05dd \u05e2\u05dc "
                "\u05d4\u05ea\u05d5\u05e6\u05d0\u05d4. \u05d4\u05e8\u05d5\u05e4\u05d0 \u05de\u05e4\u05e8\u05e9 \u05d1\u05d4\u05e7\u05e9\u05e8 "
                "\u05d4\u05e7\u05dc\u05d9\u05e0\u05d9 \u05e9\u05dc\u05db\u05dd.</p>"
            ),
        ),
        Section(
            id="what-high-means", level=2,
            heading="\u05de\u05d4 \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05e6\u05d1\u05d9\u05e2 \u05e2\u05e8\u05da \u05d2\u05d1\u05d5\u05d4?",
            body_html=(
                "<p>\u05e2\u05e8\u05da \u05d2\u05d1\u05d5\u05d4 \u05de\u05e8\u05de\u05d6 \u05e9\u05d4\u05d2\u05d5\u05e3 \u05de\u05d9\u05d9\u05e6\u05e8 "
                "\u05d9\u05d5\u05ea\u05e8 \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05de\u05d4\u05e6\u05e4\u05d5\u05d9 \u05db\u05d3\u05d9 "
                "\u05dc\u05e9\u05de\u05d5\u05e8 \u05e2\u05dc \u05e8\u05de\u05ea \u05e1\u05d5\u05db\u05e8 \u05ea\u05e7\u05d9\u05e0\u05d4. \u05de\u05e6\u05d1 "
                "\u05d6\u05d4 \u05e0\u05e7\u05e8\u05d0 <strong>\u05d4\u05d9\u05e4\u05e8\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05e0\u05de\u05d9\u05d4 "
                "\u05de\u05e4\u05e6\u05d4</strong> \u2014 \u05dc\u05e2\u05d9\u05ea\u05d9\u05dd \u05e7\u05e8\u05d5\u05d1\u05d5\u05ea \u05e1\u05d9\u05de\u05df "
                "\u05de\u05d5\u05e7\u05d3\u05dd \u05dc\u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df.</p>"
                "<p>\u05de\u05e6\u05d1\u05d9\u05dd \u05e9\u05e2\u05e9\u05d5\u05d9\u05d9\u05dd \u05dc\u05d4\u05d9\u05d5\u05ea \u05e7\u05e9\u05d5\u05e8\u05d9\u05dd:</p>"
                "<ul>"
                "<li><strong>\u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df</strong></li>"
                "<li><strong>\u05ea\u05e1\u05de\u05d5\u05e0\u05ea \u05de\u05d8\u05d1\u05d5\u05dc\u05d9\u05ea</strong></li>"
                "<li><strong>PCOS</strong></li>"
                "<li><strong>\u05db\u05d1\u05d3 \u05e9\u05d5\u05de\u05e0\u05d9 (NAFLD)</strong></li>"
                "<li><strong>\u05e1\u05d9\u05db\u05d5\u05df \u05e7\u05e8\u05d3\u05d9\u05d5\u05d5\u05e1\u05e7\u05d5\u05dc\u05e8\u05d9 \u05de\u05d5\u05d2\u05d1\u05e8</strong></li>"
                "</ul>"
                "<p>\u05e2\u05e8\u05da \u05d2\u05d1\u05d5\u05d4 \u05d1\u05d5\u05d3\u05d3 \u05d0\u05d9\u05e0\u05d5 \u05de\u05d0\u05e9\u05e8 \u05d0\u05e3 "
                "\u05d0\u05d7\u05d3 \u05de\u05d0\u05dc\u05d4. \u05dc\u05d7\u05e5, \u05e9\u05d9\u05e0\u05d4, \u05ea\u05e8\u05d5\u05e4\u05d5\u05ea "
                "\u05d5\u05e4\u05e2\u05d9\u05dc\u05d5\u05ea \u05d2\u05d5\u05e4\u05e0\u05d9\u05ea \u05d9\u05db\u05d5\u05dc\u05d9\u05dd \u05dc\u05d4\u05e9\u05e4\u05d9\u05e2 "
                "\u05d6\u05de\u05e0\u05d9\u05ea. \u05d4\u05e4\u05d9\u05e8\u05d5\u05e9 \u05ea\u05de\u05d9\u05d3 \u05d1\u05d9\u05d3\u05d9 \u05d4\u05e8\u05d5\u05e4\u05d0.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-link", level=2,
            heading="\u05d4\u05e7\u05e9\u05e8 \u05dc\u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df",
            body_html=(
                "<p><strong>\u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df</strong> \u05e4\u05d9\u05e8\u05d5\u05e9\u05d4 "
                "\u05e9\u05ea\u05d0\u05d9 \u05e9\u05e8\u05d9\u05e8, \u05e9\u05d5\u05de\u05df \u05d5\u05db\u05d1\u05d3 \u05de\u05d2\u05d9\u05d1\u05d9\u05dd "
                "\u05e4\u05d7\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df. \u05d4\u05dc\u05d1\u05dc\u05d1 \u05de\u05e4\u05e6\u05d4 "
                "\u05d1\u05d9\u05d9\u05e6\u05d5\u05e8 \u05de\u05d5\u05d2\u05d1\u05e8. \u05d1\u05e9\u05dc\u05d1 \u05d4\u05de\u05d5\u05e7\u05d3\u05dd "
                "\u05d4\u05e1\u05d5\u05db\u05e8 \u05e0\u05e9\u05d0\u05e8 \u05ea\u05e7\u05d9\u05df; \u05e2\u05dd \u05d4\u05d6\u05de\u05df, "
                "\u05d0\u05dd \u05d4\u05dc\u05d1\u05dc\u05d1 \u05dc\u05d0 \u05e2\u05d5\u05de\u05d3 \u05d1\u05e7\u05e6\u05d1, "
                "\u05d4\u05e1\u05d5\u05db\u05e8 \u05e2\u05d5\u05dc\u05d4 \u2014 \u05ea\u05d7\u05d9\u05dc\u05d4 \u05e4\u05e8\u05d4-\u05e1\u05d5\u05db\u05e8\u05ea, "
                "\u05d5\u05dc\u05e2\u05d9\u05ea\u05d9\u05dd \u05e1\u05d5\u05db\u05e8\u05ea \u05e1\u05d5\u05d2 2.</p>"
                "<p>\u05dc\u05db\u05df \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4 \u05e2\u05e9\u05d5\u05d9 "
                "\u05dc\u05d4\u05d5\u05e4\u05d9\u05e2 <em>\u05dc\u05e4\u05e0\u05d9</em> \u05e9\u05d4\u05e1\u05d5\u05db\u05e8 "
                "\u05e2\u05d5\u05dc\u05d4 \u2014 \u05d0\u05d5\u05ea \u05de\u05d8\u05d1\u05d5\u05dc\u05d9 \u05de\u05d5\u05e7\u05d3\u05dd. "
                "\u05d0\u05d1\u05d7\u05e0\u05d4 \u05de\u05ea\u05d1\u05e1\u05e1\u05ea \u05e2\u05dc \u05d4\u05ea\u05de\u05d5\u05e0\u05d4 "
                "\u05d4\u05e7\u05dc\u05d9\u05e0\u05d9\u05ea \u05d4\u05de\u05dc\u05d0\u05d4.</p>"
            ),
        ),
        Section(
            id="homa-ir-connection", level=2,
            heading="\u05d4\u05e7\u05e9\u05e8 \u05dc-HOMA-IR",
            body_html=(
                "<p>\u05d3\u05e8\u05da \u05e0\u05e4\u05d5\u05e6\u05d4 \u05dc\u05e9\u05d9\u05dd \u05d0\u05ea \u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df "
                "\u05d1\u05d4\u05e7\u05e9\u05e8 \u05d4\u05d9\u05d0 \u05d7\u05d9\u05e9\u05d5\u05d1 <strong>HOMA-IR</strong>:</p>"
                "<p><em>\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd (\u03bcU/mL) \u00d7 "
                "\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05d1\u05e6\u05d5\u05dd (mg/dL) \u00f7 405</em></p>"
                "<p>HOMA-IR \u05de\u05ea\u05d7\u05ea 1.0 \u05e0\u05d7\u05e9\u05d1 \u05d0\u05d5\u05e4\u05d8\u05d9\u05de\u05dc\u05d9; "
                "\u05de\u05e2\u05dc 2.5 \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d4\u05e6\u05d1\u05d9\u05e2 \u05e2\u05dc \u05e2\u05de\u05d9\u05d3\u05d5\u05ea "
                "\u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df. \u05dc\u05de\u05d9\u05d3\u05e2 \u05e0\u05d5\u05e1\u05e3, \u05e7\u05e8\u05d0\u05d5 "
                "\u05d0\u05ea <a href=\"/he/blog/\u05de\u05d4-\u05d6\u05d4-homa-ir\">\u05de\u05d3\u05e8\u05d9\u05da "
                "\u05d4-HOMA-IR \u05e9\u05dc\u05e0\u05d5</a>.</p>"
            ),
        ),
        Section(
            id="glucose-normal-insulin-high", level=2,
            heading="\u05dc\u05de\u05d4 \u05d4\u05e1\u05d5\u05db\u05e8 \u05ea\u05e7\u05d9\u05df \u05d0\u05d1\u05dc \u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d2\u05d1\u05d5\u05d4?",
            body_html=(
                "<p>\u05d4\u05e1\u05d5\u05db\u05e8 \u05d1\u05e6\u05d5\u05dd \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05d9\u05d5\u05ea \u05ea\u05e7\u05d9\u05df "
                "\u05d1\u05e2\u05d5\u05d3 \u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05db\u05d1\u05e8 \u05d2\u05d1\u05d5\u05d4. \u05d4\u05e1\u05d9\u05d1\u05d4: "
                "\u05d4\u05dc\u05d1\u05dc\u05d1 \u05e2\u05d5\u05d1\u05d3 \u05d9\u05ea\u05e8 \u05de\u05d3\u05d9 \u05db\u05d3\u05d9 \u05dc\u05e4\u05e6\u05d5\u05ea "
                "\u05e2\u05dc \u05d4\u05ea\u05e0\u05d2\u05d3\u05d5\u05ea \u05d4\u05ea\u05d0\u05d9\u05dd. \u05db\u05dc \u05e2\u05d5\u05d3 "
                "\u05e9\u05d4\u05e4\u05d9\u05e6\u05d5\u05d9 \u05de\u05e6\u05dc\u05d9\u05d7, \u05d4\u05e1\u05d5\u05db\u05e8 \u05e0\u05e8\u05d0\u05d4 \u05ea\u05e7\u05d9\u05df.</p>"
                "<p>\u05de\u05e6\u05d1 \u05d6\u05d4 \u05e0\u05e7\u05e8\u05d0 <strong>\u05d4\u05d9\u05e4\u05e8\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05e0\u05de\u05d9\u05d4 "
                "\u05de\u05e4\u05e6\u05d4</strong>. \u05d4\u05e1\u05ea\u05db\u05dc\u05d5\u05ea \u05e8\u05e7 \u05e2\u05dc "
                "\u05d4\u05e1\u05d5\u05db\u05e8 \u05e2\u05dc\u05d5\u05dc\u05d4 \u05dc\u05d4\u05d7\u05de\u05d9\u05e5 \u05d0\u05ea "
                "\u05d4\u05de\u05d0\u05de\u05e5 \u05d4\u05de\u05d8\u05d1\u05d5\u05dc\u05d9 \u05e9\u05db\u05d1\u05e8 \u05d4\u05d7\u05dc. "
                "\u05dc\u05db\u05df \u05d7\u05dc\u05e7 \u05de\u05d4\u05e8\u05d5\u05e4\u05d0\u05d9\u05dd \u05de\u05d1\u05e7\u05e9\u05d9\u05dd "
                "\u05d2\u05dd \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd, \u05d1\u05de\u05d9\u05d5\u05d7\u05d3 "
                "\u05db\u05e9\u05d9\u05e9 \u05d4\u05d9\u05e1\u05d8\u05d5\u05e8\u05d9\u05d4 \u05de\u05e9\u05e4\u05d7\u05ea\u05d9\u05ea.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="\u05d0\u05d9\u05dc\u05d5 \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05e0\u05d5\u05e1\u05e4\u05d5\u05ea \u05de\u05d5\u05e2\u05e8\u05db\u05d5\u05ea?",
            body_html=(
                "<p>\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05dc\u05d0 \u05de\u05e4\u05d5\u05e8\u05e9 "
                "\u05dc\u05d1\u05d3\u05d5. \u05d4\u05e8\u05d5\u05e4\u05d0 \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d1\u05d3\u05d5\u05e7 \u05d2\u05dd:</p>"
                "<ul>"
                "<li><strong>\u05d2\u05dc\u05d5\u05e7\u05d5\u05d6 \u05d1\u05e6\u05d5\u05dd</strong> \u2014 \u05e0\u05db\u05e0\u05e1 "
                "\u05dc\u05d7\u05d9\u05e9\u05d5\u05d1 HOMA-IR</li>"
                "<li><strong>HbA1c</strong> \u2014 \u05de\u05e9\u05e7\u05e3 \u05d0\u05ea \u05de\u05de\u05d5\u05e6\u05e2 "
                "\u05d4\u05e1\u05d5\u05db\u05e8 \u05dc-2\u20133 \u05d7\u05d5\u05d3\u05e9\u05d9\u05dd</li>"
                "<li><strong>\u05d8\u05e8\u05d9\u05d2\u05dc\u05d9\u05e6\u05e8\u05d9\u05d3\u05d9\u05dd \u05d5-HDL</strong></li>"
                "<li><strong>C-\u05e4\u05e4\u05d8\u05d9\u05d3</strong></li>"
                "<li><strong>OGTT</strong></li>"
                "<li><strong>\u05d4\u05d9\u05e7\u05e3 \u05de\u05d5\u05ea\u05df \u05d5-BMI</strong></li>"
                "</ul>"
                "<p>\u05d4\u05de\u05d8\u05e8\u05d4 \u2014 \u05dc\u05e8\u05d0\u05d5\u05ea \u05d0\u05ea \u05d4\u05ea\u05de\u05d5\u05e0\u05d4 "
                "\u05d4\u05de\u05d8\u05d1\u05d5\u05dc\u05d9\u05ea \u05d4\u05e9\u05dc\u05de\u05d4, \u05dc\u05d0 \u05de\u05e1\u05e4\u05e8 \u05d1\u05d5\u05d3\u05d3.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="\u05dc\u05de\u05d4 \u05ea\u05d5\u05e6\u05d0\u05d4 \u05d0\u05d7\u05ea \u05dc\u05d0 \u05de\u05e1\u05e4\u05d9\u05e7\u05d4?",
            body_html=(
                "<p>\u05de\u05d3\u05d9\u05d3\u05d4 \u05d1\u05d5\u05d3\u05d3\u05ea \u05e9\u05dc \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df "
                "\u05d1\u05e6\u05d5\u05dd \u05d0\u05d9\u05e0\u05d4 \u05de\u05d2\u05d3\u05d9\u05e8\u05d4 \u05d0\u05ea \u05d1\u05e8\u05d9\u05d0\u05d5\u05ea\u05db\u05dd. "
                "\u05d2\u05dd \u05d1\u05d3\u05d9\u05e7\u05d4 \u05d7\u05d5\u05d6\u05e8\u05ea \u05d1\u05d0\u05d5\u05ea\u05d5 \u05d9\u05d5\u05dd "
                "\u05d4\u05ea\u05d5\u05e6\u05d0\u05d4 \u05e2\u05e9\u05d5\u05d9\u05d4 \u05dc\u05d4\u05e9\u05ea\u05e0\u05d5\u05ea. \u05dc\u05d7\u05e5, "
                "\u05e9\u05d9\u05e0\u05d4, \u05d0\u05e8\u05d5\u05d7\u05ea \u05d4\u05e2\u05e8\u05d1 \u05d5\u05ea\u05d4\u05dc\u05d9\u05da "
                "\u05d4\u05d3\u05d2\u05d9\u05de\u05d4 \u05e2\u05e6\u05de\u05d5 \u05de\u05e9\u05e4\u05d9\u05e2\u05d9\u05dd.</p>"
                "<p>\u05d4\u05e2\u05e8\u05d9\u05db\u05d5 \u05ea\u05de\u05d9\u05d3 \u05d1\u05d4\u05e7\u05e9\u05e8 \u05dc\u05d8\u05d5\u05d5\u05d7 "
                "\u05d4\u05d9\u05d9\u05d7\u05d5\u05e1 \u05e9\u05dc \u05d4\u05de\u05e2\u05d1\u05d3\u05d4, \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea "
                "\u05e0\u05d5\u05e1\u05e4\u05d5\u05ea, \u05d4\u05d9\u05e1\u05d8\u05d5\u05e8\u05d9\u05d4 \u05e8\u05e4\u05d5\u05d0\u05d9\u05ea "
                "\u05d5\u05de\u05e9\u05e4\u05d7\u05ea\u05d9\u05ea, \u05d5\u05d4\u05de\u05de\u05e6\u05d0\u05d9\u05dd \u05d4\u05e7\u05dc\u05d9\u05e0\u05d9\u05d9\u05dd "
                "\u05e9\u05dc \u05d4\u05e8\u05d5\u05e4\u05d0.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="\u05de\u05ea\u05d9 \u05dc\u05e4\u05e0\u05d5\u05ea \u05dc\u05e8\u05d5\u05e4\u05d0?",
            body_html=(
                "<p>\u05e9\u05d5\u05d7\u05d7\u05d5 \u05e2\u05dd \u05e8\u05d5\u05e4\u05d0 \u05d0\u05dd:</p>"
                "<ul>"
                "<li>\u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05e9\u05dc\u05db\u05dd "
                "\u05de\u05e2\u05dc \u05dc\u05d8\u05d5\u05d5\u05d7 \u05d4\u05d9\u05d9\u05d7\u05d5\u05e1</li>"
                "<li>\u05d9\u05e9 \u05d4\u05d9\u05e1\u05d8\u05d5\u05e8\u05d9\u05d4 \u05de\u05e9\u05e4\u05d7\u05ea\u05d9\u05ea "
                "\u05e9\u05dc \u05e1\u05d5\u05db\u05e8\u05ea \u05e1\u05d5\u05d2 2 \u05d0\u05d5 \u05ea\u05e1\u05de\u05d5\u05e0\u05ea "
                "\u05de\u05d8\u05d1\u05d5\u05dc\u05d9\u05ea</li>"
                "<li>\u05e2\u05d5\u05d3\u05e3 \u05de\u05e9\u05e7\u05dc, \u05e9\u05d5\u05de\u05df \u05d1\u05d8\u05e0\u05d9 "
                "\u05d0\u05d5 \u05ea\u05e1\u05de\u05d9\u05e0\u05d9 PCOS</li>"
                "<li>\u05e2\u05d9\u05d9\u05e4\u05d5\u05ea, \u05e8\u05e2\u05d1 \u05ea\u05db\u05d5\u05e3 "
                "\u05d0\u05d5 \u05e9\u05d9\u05e0\u05d5\u05d9\u05d9 \u05de\u05e9\u05e7\u05dc \u05dc\u05dc\u05d0 \u05d4\u05e1\u05d1\u05e8</li>"
                "<li>\u05d4\u05e1\u05d5\u05db\u05e8 \u05ea\u05e7\u05d9\u05df \u05d0\u05d1\u05dc \u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d2\u05d1\u05d5\u05d4</li>"
                "</ul>"
                "<p>\u05d2\u05dd \u05dc\u05dc\u05d0 \u05ea\u05e1\u05de\u05d9\u05e0\u05d9\u05dd, \u05d3\u05d9\u05d5\u05d5\u05d7 \u05e2\u05dc \u05ea\u05d5\u05e6\u05d0\u05d4 "
                "\u05d7\u05e8\u05d9\u05d2\u05d4 \u05dc\u05e8\u05d5\u05e4\u05d0 \u05d4\u05d5\u05d0 \u05ea\u05de\u05d9\u05d3 \u05e6\u05e2\u05d3 \u05e0\u05db\u05d5\u05df.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="\u05d4\u05d1\u05d9\u05e0\u05d5 \u05d0\u05ea \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea \u05d8\u05d5\u05d1 \u05d9\u05d5\u05ea\u05e8 \u05e2\u05dd Norya",
            body_html=(
                "<p>\u05d1-Norya \u05d0\u05e0\u05d7\u05e0\u05d5 \u05dc\u05d0 \u05de\u05d0\u05d1\u05d7\u05e0\u05d9\u05dd \u2014 \u05d0\u05dc\u05d0 "
                "\u05e2\u05d5\u05d6\u05e8\u05d9\u05dd \u05dc\u05db\u05dd \u05dc\u05d4\u05d1\u05d9\u05df \u05d0\u05ea \u05d4\u05ea\u05d5\u05e6\u05d0\u05d5\u05ea. "
                "<a href=\"/analyze\">\u05d4\u05e2\u05dc\u05d5 \u05d0\u05ea \u05d4\u05d3\u05d5\u05d7</a> "
                "\u05d5\u05e7\u05d1\u05dc\u05d5 \u05e1\u05d9\u05db\u05d5\u05dd \u05de\u05e1\u05d5\u05d3\u05e8 \u05d1\u05e9\u05e4\u05d4 "
                "\u05e4\u05e9\u05d5\u05d8\u05d4, \u05e2\u05dd \u05d8\u05d5\u05d5\u05d7\u05d9 \u05d9\u05d9\u05d7\u05d5\u05e1 \u05d5\u05d4\u05e7\u05e9\u05e8. "
                "<a href=\"/pricing\">\u05de\u05d7\u05d9\u05e8\u05d5\u05df</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="\u05d4\u05d5\u05d3\u05e2\u05d4",
            body_html=(
                "<p><strong>\u05ea\u05d5\u05db\u05df \u05d6\u05d4 \u05dc\u05de\u05d9\u05d3\u05e2 \u05d1\u05dc\u05d1\u05d3 "
                "\u05d5\u05d0\u05d9\u05e0\u05d5 \u05de\u05d7\u05dc\u05d9\u05e3 \u05d9\u05d9\u05e2\u05d5\u05e5 \u05e8\u05e4\u05d5\u05d0\u05d9 "
                "\u05d0\u05d5 \u05d0\u05d1\u05d7\u05e0\u05d4.</strong> \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd "
                "\u05d2\u05d1\u05d5\u05d4 \u05d9\u05db\u05d5\u05dc \u05dc\u05e0\u05d1\u05d5\u05e2 \u05de\u05e1\u05d9\u05d1\u05d5\u05ea "
                "\u05e8\u05d1\u05d5\u05ea; \u05e8\u05e7 \u05d0\u05d9\u05e9 \u05de\u05e7\u05e6\u05d5\u05e2 \u05e9\u05de\u05db\u05d9\u05e8 "
                "\u05d0\u05ea \u05d4\u05e8\u05e7\u05e2 \u05e9\u05dc\u05db\u05dd \u05d9\u05db\u05d5\u05dc \u05dc\u05e4\u05e8\u05e9 "
                "\u05e0\u05db\u05d5\u05df. \u05e9\u05d5\u05d7\u05d7\u05d5 \u05ea\u05de\u05d9\u05d3 \u05e2\u05dd \u05e8\u05d5\u05e4\u05d0.</p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="फ़ास्टिंग इंसुलिन हाई होने का क्या मतलब है?", body_html="<p>अगर आपकी ब्लड रिपोर्ट में <strong>फ़ास्टिंग इंसुलिन</strong> का लेवल ज़्यादा आया है तो मन में सवाल उठना स्वाभाविक है: क्या यह गंभीर है? क्या मुझे डायबिटीज़ है? ब्लड शुगर नॉर्मल है तो इंसुलिन क्यों बढ़ा हुआ है? यह गाइड बताती है कि फ़ास्टिंग इंसुलिन क्या है, हाई रिज़ल्ट का क्या मतलब हो सकता है, और इसे सही संदर्भ में कैसे समझें।</p><p>हमारा उद्देश्य निदान करना नहीं है — बल्कि आपको अगली डॉक्टर विज़िट के लिए बेहतर तैयार करना है।</p>"),
        Section(id="what-is-fasting-insulin", level=2, heading="फ़ास्टिंग इंसुलिन क्या है और कैसे मापा जाता है?", body_html="<p><strong>इंसुलिन</strong> पैंक्रियाज़ द्वारा बनाया जाने वाला हॉर्मोन है जो ग्लूकोज़ को सेल्स में पहुँचाता है। खाने के बाद ब्लड शुगर बढ़ता है और पैंक्रियाज़ इंसुलिन रिलीज़ करता है। <strong>फ़ास्टिंग इंसुलिन</strong> 8–12 घंटे बिना कुछ खाए नापा जाता है ताकि बेसल इंसुलिन लेवल का पता चले।</p><p>रिज़ल्ट आमतौर पर <strong>μU/mL</strong> में आता है। सामान्य रेंज लैब के अनुसार बदलती है; आम तौर पर 2–25 μU/mL मानी जाती है और कई डॉक्टर 10 μU/mL से कम को बेहतर मानते हैं। उम्र, लिंग, BMI और लैब मेथड रिज़ल्ट को प्रभावित करते हैं। अपने डॉक्टर से अपनी रिपोर्ट की व्याख्या कराएं।</p>"),
        Section(id="what-high-means", level=2, heading="हाई फ़ास्टिंग इंसुलिन का क्या मतलब हो सकता है?", body_html="<p>हाई वैल्यू बताती है कि शरीर ब्लड शुगर को नॉर्मल रखने के लिए ज़रूरत से ज़्यादा इंसुलिन बना रहा है — इसे <strong>कम्पेन्सेटरी हाइपरइंसुलिनीमिया</strong> कहते हैं।</p><ul><li><strong>इंसुलिन रेज़िस्टेंस</strong></li><li><strong>मेटाबोलिक सिंड्रोम</strong></li><li><strong>PCOS</strong></li><li><strong>नॉन-अल्कोहोलिक फ़ैटी लिवर (NAFLD)</strong></li><li><strong>कार्डियोवैस्कुलर रिस्क</strong></li></ul><p>एक अकेली हाई वैल्यू इनमें से किसी की भी पुष्टि नहीं करती। स्ट्रेस, नींद, दवाइयाँ और हाल की एक्सरसाइज़ अस्थायी रूप से असर डाल सकती हैं। व्याख्या हमेशा डॉक्टर की होती है।</p>"),
        Section(id="insulin-resistance-link", level=2, heading="इंसुलिन रेज़िस्टेंस से संबंध", body_html="<p><strong>इंसुलिन रेज़िस्टेंस</strong> में मसल, फ़ैट और लिवर सेल्स इंसुलिन के सिग्नल का ठीक से जवाब नहीं देतीं। पैंक्रियाज़ ज़्यादा इंसुलिन बनाकर कम्पेंसेट करता है। शुरू में ग्लूकोज़ नॉर्मल रहता है लेकिन सालों में अगर पैंक्रियाज़ साथ नहीं दे पाता तो शुगर बढ़ने लगता है — पहले प्री-डायबिटीज़, फिर टाइप 2 डायबिटीज़।</p><p>इसलिए हाई फ़ास्टिंग इंसुलिन शुगर बढ़ने <em>से पहले</em> दिख सकता है — एक अर्ली वॉर्निंग सिग्नल। डायग्नोसिस सिर्फ़ एक वैल्यू से नहीं होता; डॉक्टर पूरी क्लिनिकल पिक्चर देखते हैं।</p>"),
        Section(id="homa-ir-connection", level=2, heading="HOMA-IR से कनेक्शन", body_html="<p>फ़ास्टिंग इंसुलिन को संदर्भ में रखने का एक तरीक़ा <strong>HOMA-IR</strong> है:</p><p><em>फ़ास्टिंग इंसुलिन (μU/mL) × फ़ास्टिंग ग्लूकोज़ (mg/dL) ÷ 405</em></p><p>1.0 से कम ऑप्टिमल माना जाता है; 2.5 से ऊपर इंसुलिन रेज़िस्टेंस का संकेत हो सकता है। विस्तार से जानने के लिए <a href=\"/hi/blog/homa-ir-kya-hai\">हमारी HOMA-IR गाइड</a> पढ़ें।</p>"),
        Section(id="glucose-normal-insulin-high", level=2, heading="ग्लूकोज़ नॉर्मल लेकिन इंसुलिन हाई — क्यों?", body_html="<p>ब्लड शुगर नॉर्मल दिख सकता है जबकि इंसुलिन पहले से बढ़ा हुआ हो। कारण: पैंक्रियाज़ ओवरटाइम काम कर रहा है। जब तक यह कम्पेंसेशन सफल रहता है, ग्लूकोज़ नॉर्मल रेंज में रहता है।</p><p>इसे <strong>कम्पेन्सेटरी हाइपरइंसुलिनीमिया</strong> कहते हैं। सिर्फ़ ग्लूकोज़ देखने से मेटाबोलिक स्ट्रेस छूट सकता है। इसलिए कुछ डॉक्टर, ख़ासकर फ़ैमिली हिस्ट्री होने पर, इंसुलिन भी चेक करते हैं।</p>"),
        Section(id="related-tests", level=2, heading="कौन से अन्य टेस्ट साथ में देखे जाते हैं?", body_html="<p>फ़ास्टिंग इंसुलिन अकेले नहीं पढ़ा जाता। डॉक्टर ये भी देख सकते हैं:</p><ul><li><strong>फ़ास्टिंग ग्लूकोज़</strong> — HOMA-IR के लिए</li><li><strong>HbA1c</strong> — पिछले 2–3 महीनों का औसत शुगर</li><li><strong>ट्राइग्लिसराइड्स और HDL</strong></li><li><strong>C-पेप्टाइड</strong></li><li><strong>OGTT</strong></li><li><strong>कमर का माप और BMI</strong></li></ul><p>लक्ष्य है पूरी मेटाबोलिक तस्वीर देखना, एक अकेला नंबर नहीं।</p>"),
        Section(id="not-enough-alone", level=2, heading="एक रिज़ल्ट काफ़ी क्यों नहीं?", body_html="<p>एक अकेली फ़ास्टिंग इंसुलिन वैल्यू आपकी सेहत तय नहीं करती। स्ट्रेस, नींद, रात का खाना और ख़ून निकालने की प्रक्रिया ख़ुद रिज़ल्ट बदल सकती है। लैब रेफ़रेंस रेंज भी अलग-अलग होती हैं।</p><p>अपना रिज़ल्ट हमेशा अपनी लैब रेंज, बाक़ी ब्लड वैल्यूज़, मेडिकल हिस्ट्री और डॉक्टर की जाँच के साथ मिलाकर देखें।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें?", body_html="<p>डॉक्टर से बात करें अगर:</p><ul><li>फ़ास्टिंग इंसुलिन रेफ़रेंस रेंज से ऊपर है</li><li>परिवार में टाइप 2 डायबिटीज़ या मेटाबोलिक सिंड्रोम है</li><li>पेट के आसपास वज़न ज़्यादा है या PCOS के लक्षण हैं</li><li>लगातार थकान, बार-बार भूख या अनजानी वज़न बदलाव है</li><li>ग्लूकोज़ नॉर्मल लेकिन इंसुलिन हाई है</li></ul><p>बिना लक्षणों के भी, असामान्य रिपोर्ट डॉक्टर को दिखाना सही क़दम है।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya से अपने रिज़ल्ट बेहतर समझें", body_html="<p>Norya में हम डायग्नोज़ नहीं करते — लेकिन आपकी रिपोर्ट समझने में मदद करते हैं। <a href=\"/analyze\">अपनी लैब रिपोर्ट अपलोड करें</a> और सरल भाषा में स्ट्रक्चर्ड समरी पाएं। <a href=\"/pricing\">प्राइसिंग</a> के लिए यहाँ देखें।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण", body_html="<p><strong>यह सामग्री केवल जानकारी के लिए है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> हाई फ़ास्टिंग इंसुलिन के कई कारण हो सकते हैं; केवल आपकी हिस्ट्री जानने वाला डॉक्टर ही सही व्याख्या कर सकता है। अपने लैब रिज़ल्ट हमेशा डॉक्टर से दिखाएं।</p>"),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC (RTL)
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="\u0645\u0627\u0630\u0627 \u064a\u0639\u0646\u064a \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u061f", body_html="<p>\u0625\u0630\u0627 \u0623\u0638\u0647\u0631 \u062a\u0642\u0631\u064a\u0631 \u0641\u062d\u0648\u0635\u0627\u062a\u0643 \u0627\u0631\u062a\u0641\u0627\u0639\u064b\u0627 \u0641\u064a \u0645\u0633\u062a\u0648\u0649 <strong>\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645</strong>\u060c \u0641\u0645\u0646 \u0627\u0644\u0637\u0628\u064a\u0639\u064a \u0623\u0646 \u062a\u062a\u0633\u0627\u0621\u0644: \u0647\u0644 \u0647\u0630\u0627 \u062e\u0637\u064a\u0631\u061f \u0647\u0644 \u0644\u062f\u064a\u0651 \u0633\u0643\u0631\u064a\u061f \u0644\u0645\u0627\u0630\u0627 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0637\u0628\u064a\u0639\u064a \u0644\u0643\u0646 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0645\u0631\u062a\u0641\u0639\u061f \u064a\u0634\u0631\u062d \u0647\u0630\u0627 \u0627\u0644\u062f\u0644\u064a\u0644 \u0645\u0627\u0647\u064a\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0648\u0645\u0627 \u064a\u0645\u0643\u0646 \u0623\u0646 \u062a\u0639\u0646\u064a\u0647 \u0642\u064a\u0645\u0629 \u0645\u0631\u062a\u0641\u0639\u0629.</p><p>\u0647\u062f\u0641\u0646\u0627 \u0644\u064a\u0633 \u0627\u0644\u062a\u0634\u062e\u064a\u0635 \u2014 \u0628\u0644 \u0645\u0633\u0627\u0639\u062f\u062a\u0643 \u0639\u0644\u0649 \u0641\u0647\u0645 \u0646\u062a\u064a\u062c\u062a\u0643 \u0644\u062a\u0630\u0647\u0628 \u0625\u0644\u0649 \u0645\u0648\u0639\u062f\u0643 \u0627\u0644\u0637\u0628\u064a \u0623\u0643\u062b\u0631 \u0627\u0633\u062a\u0639\u062f\u0627\u062f\u064b\u0627.</p>"),
        Section(id="what-is-fasting-insulin", level=2, heading="\u0645\u0627 \u0647\u0648 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0648\u0643\u064a\u0641 \u064a\u064f\u0642\u0627\u0633\u061f", body_html="<p><strong>\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646</strong> \u0647\u0631\u0645\u0648\u0646 \u064a\u0641\u0631\u0632\u0647 \u0627\u0644\u0628\u0646\u0643\u0631\u064a\u0627\u0633 \u064a\u0633\u0645\u062d \u0644\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0628\u0627\u0644\u062f\u062e\u0648\u0644 \u0625\u0644\u0649 \u0627\u0644\u062e\u0644\u0627\u064a\u0627. \u0628\u0639\u062f \u0627\u0644\u0623\u0643\u0644 \u064a\u0631\u062a\u0641\u0639 \u0627\u0644\u0633\u0643\u0631 \u0648\u064a\u0641\u0631\u0632 \u0627\u0644\u0628\u0646\u0643\u0631\u064a\u0627\u0633 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646. <strong>\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645</strong> \u064a\u064f\u0642\u0627\u0633 \u0628\u0639\u062f 8\u201312 \u0633\u0627\u0639\u0629 \u0635\u064a\u0627\u0645 \u0644\u062a\u0642\u064a\u064a\u0645 \u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0642\u0627\u0639\u062f\u064a.</p><p>\u0627\u0644\u0646\u062a\u0627\u0626\u062c \u062a\u064f\u0639\u0637\u0649 \u0628\u0640 <strong>\u03bcU/mL</strong>. \u0627\u0644\u0646\u0637\u0627\u0642 \u0627\u0644\u0645\u0631\u062c\u0639\u064a \u0627\u0644\u0634\u0627\u0626\u0639 2\u201325 \u03bcU/mL\u060c \u0648\u0643\u062b\u064a\u0631 \u0645\u0646 \u0627\u0644\u0623\u0637\u0628\u0627\u0621 \u064a\u0639\u062a\u0628\u0631\u0648\u0646 \u0623\u0642\u0644 \u0645\u0646 10 \u03bcU/mL \u0645\u062b\u0627\u0644\u064a\u064b\u0627. \u0627\u0644\u0639\u0645\u0631 \u0648\u0627\u0644\u062c\u0646\u0633 \u0648BMI \u0648\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u0641\u062d\u0635 \u062a\u0624\u062b\u0631 \u0641\u064a \u0627\u0644\u0646\u062a\u064a\u062c\u0629. \u0627\u0644\u0637\u0628\u064a\u0628 \u064a\u064f\u0641\u0633\u0651\u0631 \u0641\u064a \u0627\u0644\u0633\u064a\u0627\u0642 \u0627\u0644\u0633\u0631\u064a\u0631\u064a.</p>"),
        Section(id="what-high-means", level=2, heading="\u0645\u0627\u0630\u0627 \u064a\u0639\u0646\u064a \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0642\u064a\u0645\u0629\u061f", body_html="<p>\u0642\u064a\u0645\u0629 \u0645\u0631\u062a\u0641\u0639\u0629 \u062a\u0634\u064a\u0631 \u0625\u0644\u0649 \u0623\u0646 \u0627\u0644\u062c\u0633\u0645 \u064a\u0646\u062a\u062c \u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0623\u0643\u062b\u0631 \u0645\u0646 \u0627\u0644\u0645\u062a\u0648\u0642\u0639 \u0644\u0644\u062d\u0641\u0627\u0638 \u0639\u0644\u0649 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0637\u0628\u064a\u0639\u064a\u064b\u0627. \u064a\u064f\u0633\u0645\u0651\u0649 \u0647\u0630\u0627 <strong>\u0641\u0631\u0637 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u062a\u0639\u0648\u064a\u0636\u064a</strong>.</p><ul><li><strong>\u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646</strong></li><li><strong>\u0627\u0644\u0645\u062a\u0644\u0627\u0632\u0645\u0629 \u0627\u0644\u0623\u064a\u0636\u064a\u0629</strong></li><li><strong>\u062a\u0643\u064a\u0651\u0633 \u0627\u0644\u0645\u0628\u0627\u064a\u0636 (PCOS)</strong></li><li><strong>\u0627\u0644\u0643\u0628\u062f \u0627\u0644\u062f\u0647\u0646\u064a (NAFLD)</strong></li><li><strong>\u0632\u064a\u0627\u062f\u0629 \u0627\u0644\u062e\u0637\u0631 \u0627\u0644\u0642\u0644\u0628\u064a \u0627\u0644\u0648\u0639\u0627\u0626\u064a</strong></li></ul><p>\u0642\u064a\u0645\u0629 \u0648\u0627\u062d\u062f\u0629 \u0645\u0631\u062a\u0641\u0639\u0629 \u0644\u0627 \u062a\u0624\u0643\u062f \u0623\u064a\u064b\u0627 \u0645\u0646 \u0647\u0630\u0647. \u0627\u0644\u062a\u0648\u062a\u0631 \u0648\u0627\u0644\u0646\u0648\u0645 \u0648\u0627\u0644\u0623\u062f\u0648\u064a\u0629 \u0648\u0627\u0644\u062a\u0645\u0627\u0631\u064a\u0646 \u0642\u062f \u062a\u0624\u062b\u0631 \u0645\u0624\u0642\u062a\u064b\u0627. \u0627\u0644\u062a\u0641\u0633\u064a\u0631 \u0644\u0644\u0637\u0628\u064a\u0628.</p>"),
        Section(id="insulin-resistance-link", level=2, heading="\u0627\u0644\u0639\u0644\u0627\u0642\u0629 \u0628\u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646", body_html="<p><strong>\u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646</strong> \u062a\u0639\u0646\u064a \u0623\u0646 \u062e\u0644\u0627\u064a\u0627 \u0627\u0644\u0639\u0636\u0644 \u0648\u0627\u0644\u062f\u0647\u0648\u0646 \u0648\u0627\u0644\u0643\u0628\u062f \u0644\u0627 \u062a\u0633\u062a\u062c\u064a\u0628 \u0643\u0641\u0627\u064a\u0629\u064b \u0644\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646. \u0627\u0644\u0628\u0646\u0643\u0631\u064a\u0627\u0633 \u064a\u0639\u0648\u0651\u0636 \u0628\u0625\u0646\u062a\u0627\u062c \u0627\u0644\u0645\u0632\u064a\u062f. \u0641\u064a \u0627\u0644\u0628\u062f\u0627\u064a\u0629 \u064a\u0628\u0642\u0649 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0637\u0628\u064a\u0639\u064a\u064b\u0627\u061b \u0645\u0639 \u0627\u0644\u0648\u0642\u062a \u0625\u0646 \u0644\u0645 \u064a\u0648\u0627\u0643\u0628 \u0627\u0644\u0628\u0646\u0643\u0631\u064a\u0627\u0633\u060c \u064a\u0631\u062a\u0641\u0639 \u0627\u0644\u0633\u0643\u0631 \u2014 \u0645\u0627 \u0642\u0628\u0644 \u0627\u0644\u0633\u0643\u0631\u064a \u062b\u0645 \u0633\u0643\u0631\u064a \u0627\u0644\u0646\u0648\u0639 2.</p><p>\u0644\u0630\u0627 \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0642\u062f \u064a\u0638\u0647\u0631 <em>\u0642\u0628\u0644</em> \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0633\u0643\u0631 \u2014 \u0625\u0646\u0630\u0627\u0631 \u0645\u0628\u0643\u0631. \u0627\u0644\u062a\u0634\u062e\u064a\u0635 \u064a\u0639\u062a\u0645\u062f \u0639\u0644\u0649 \u0627\u0644\u0635\u0648\u0631\u0629 \u0627\u0644\u0633\u0631\u064a\u0631\u064a\u0629 \u0627\u0644\u0643\u0627\u0645\u0644\u0629.</p>"),
        Section(id="homa-ir-connection", level=2, heading="\u0627\u0644\u0631\u0628\u0637 \u0628\u0640 HOMA-IR", body_html="<p>\u0637\u0631\u064a\u0642\u0629 \u0634\u0627\u0626\u0639\u0629 \u0644\u0648\u0636\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0641\u064a \u0633\u064a\u0627\u0642\u0647 \u0647\u064a \u062d\u0633\u0627\u0628 <strong>HOMA-IR</strong>:</p><p><em>\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 (\u03bcU/mL) \u00d7 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0627\u0644\u0635\u0627\u0626\u0645 (mg/dL) \u00f7 405</em></p><p>HOMA-IR \u0623\u0642\u0644 \u0645\u0646 1.0 \u064a\u064f\u0639\u062a\u0628\u0631 \u0645\u062b\u0627\u0644\u064a\u064b\u0627\u061b \u0641\u0648\u0642 2.5 \u0642\u062f \u064a\u0634\u064a\u0631 \u0625\u0644\u0649 \u0645\u0642\u0627\u0648\u0645\u0629. \u0644\u0644\u0645\u0632\u064a\u062f \u0627\u0642\u0631\u0623 <a href=\"/ar/blog/\u0645\u0627-\u0647\u0648-homa-ir\">\u062f\u0644\u064a\u0644 HOMA-IR</a>.</p>"),
        Section(id="glucose-normal-insulin-high", level=2, heading="\u0644\u0645\u0627\u0630\u0627 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0637\u0628\u064a\u0639\u064a \u0644\u0643\u0646 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0645\u0631\u062a\u0641\u0639\u061f", body_html="<p>\u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0627\u0644\u0635\u0627\u0626\u0645 \u0642\u062f \u064a\u0643\u0648\u0646 \u0637\u0628\u064a\u0639\u064a\u064b\u0627 \u0628\u064a\u0646\u0645\u0627 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0645\u0631\u062a\u0641\u0639 \u0628\u0627\u0644\u0641\u0639\u0644. \u0627\u0644\u0633\u0628\u0628: \u0627\u0644\u0628\u0646\u0643\u0631\u064a\u0627\u0633 \u064a\u0639\u0645\u0644 \u0628\u062c\u0647\u062f \u0632\u0627\u0626\u062f \u0644\u062a\u0639\u0648\u064a\u0636 \u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u062e\u0644\u0627\u064a\u0627. \u0645\u0627 \u062f\u0627\u0645 \u0627\u0644\u062a\u0639\u0648\u064a\u0636 \u0646\u0627\u062c\u062d\u064b\u0627\u060c \u064a\u0628\u0642\u0649 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0637\u0628\u064a\u0639\u064a\u064b\u0627.</p><p>\u0647\u0630\u0627 \u064a\u064f\u0633\u0645\u0651\u0649 <strong>\u0641\u0631\u0637 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u062a\u0639\u0648\u064a\u0636\u064a</strong>. \u0627\u0644\u0627\u0639\u062a\u0645\u0627\u062f \u0639\u0644\u0649 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0648\u062d\u062f\u0647 \u0642\u062f \u064a\u062e\u0641\u064a \u0627\u0644\u062c\u0647\u062f \u0627\u0644\u0623\u064a\u0636\u064a \u0627\u0644\u062c\u0627\u0631\u064a. \u0644\u0630\u0644\u0643 \u064a\u0637\u0644\u0628 \u0628\u0639\u0636 \u0627\u0644\u0623\u0637\u0628\u0627\u0621 \u0641\u062d\u0635 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0623\u064a\u0636\u064b\u0627\u060c \u062e\u0627\u0635\u0629\u064b \u0639\u0646\u062f \u0648\u062c\u0648\u062f \u062a\u0627\u0631\u064a\u062e \u0639\u0627\u0626\u0644\u064a.</p>"),
        Section(id="related-tests", level=2, heading="\u0623\u064a \u0641\u062d\u0648\u0635\u0627\u062a \u0623\u062e\u0631\u0649 \u062a\u064f\u0642\u064a\u0651\u0645 \u0645\u0639\u0647\u061f", body_html="<p>\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0644\u0627 \u064a\u064f\u0641\u0633\u0651\u0631 \u0648\u062d\u062f\u0647. \u0627\u0644\u0637\u0628\u064a\u0628 \u0642\u062f \u064a\u0637\u0644\u0628 \u0623\u064a\u0636\u064b\u0627:</p><ul><li><strong>\u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0627\u0644\u0635\u0627\u0626\u0645</strong> \u2014 \u064a\u062f\u062e\u0644 \u0641\u064a \u062d\u0633\u0627\u0628 HOMA-IR</li><li><strong>HbA1c</strong> \u2014 \u0645\u062a\u0648\u0633\u0637 \u0627\u0644\u0633\u0643\u0631 \u0644\u0640 2\u20133 \u0623\u0634\u0647\u0631</li><li><strong>\u0627\u0644\u062f\u0647\u0648\u0646 \u0627\u0644\u062b\u0644\u0627\u062b\u064a\u0629 \u0648HDL</strong></li><li><strong>C-\u0628\u0628\u062a\u064a\u062f</strong></li><li><strong>OGTT</strong></li><li><strong>\u0645\u062d\u064a\u0637 \u0627\u0644\u062e\u0635\u0631 \u0648BMI</strong></li></ul><p>\u0627\u0644\u0647\u062f\u0641 \u2014 \u0631\u0624\u064a\u0629 \u0627\u0644\u0635\u0648\u0631\u0629 \u0627\u0644\u0623\u064a\u0636\u064a\u0629 \u0627\u0644\u0643\u0627\u0645\u0644\u0629 \u0648\u0644\u064a\u0633 \u0631\u0642\u0645\u064b\u0627 \u0648\u0627\u062d\u062f\u064b\u0627.</p>"),
        Section(id="not-enough-alone", level=2, heading="\u0644\u0645\u0627\u0630\u0627 \u0646\u062a\u064a\u062c\u0629 \u0648\u0627\u062d\u062f\u0629 \u0644\u0627 \u062a\u0643\u0641\u064a\u061f", body_html="<p>\u0642\u064a\u0627\u0633 \u0648\u0627\u062d\u062f \u0644\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0644\u0627 \u064a\u062d\u062f\u062f \u062d\u0627\u0644\u062a\u0643 \u0627\u0644\u0635\u062d\u064a\u0629. \u0627\u0644\u062a\u0648\u062a\u0631 \u0648\u0627\u0644\u0646\u0648\u0645 \u0648\u0648\u062c\u0628\u0629 \u0627\u0644\u0639\u0634\u0627\u0621 \u0648\u0625\u062c\u0631\u0627\u0621 \u0633\u062d\u0628 \u0627\u0644\u062f\u0645 \u0646\u0641\u0633\u0647 \u0642\u062f \u062a\u0624\u062b\u0631 \u0641\u064a \u0627\u0644\u0631\u0642\u0645. \u0627\u0644\u0646\u0637\u0627\u0642\u0627\u062a \u0627\u0644\u0645\u0631\u062c\u0639\u064a\u0629 \u062a\u062e\u062a\u0644\u0641 \u0628\u064a\u0646 \u0627\u0644\u0645\u062e\u062a\u0628\u0631\u0627\u062a.</p><p>\u0642\u064a\u0651\u0645 \u0646\u062a\u064a\u062c\u062a\u0643 \u062f\u0627\u0626\u0645\u064b\u0627 \u0645\u0639 \u0646\u0637\u0627\u0642 \u0645\u062e\u062a\u0628\u0631\u0643\u060c \u0641\u062d\u0648\u0635\u0627\u062a\u0643 \u0627\u0644\u0623\u062e\u0631\u0649\u060c \u062a\u0627\u0631\u064a\u062e\u0643 \u0627\u0644\u0637\u0628\u064a\u060c \u0648\u0641\u062d\u0635 \u0627\u0644\u0637\u0628\u064a\u0628 \u0627\u0644\u0633\u0631\u064a\u0631\u064a.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="\u0645\u062a\u0649 \u064a\u062c\u0628 \u0645\u0631\u0627\u062c\u0639\u0629 \u0627\u0644\u0637\u0628\u064a\u0628\u061f", body_html="<p>\u062a\u062d\u062f\u0651\u062b \u0645\u0639 \u0637\u0628\u064a\u0628\u0643 \u0625\u0630\u0627:</p><ul><li>\u0623\u0646\u0633\u0648\u0644\u064a\u0646\u0643 \u0627\u0644\u0635\u0627\u0626\u0645 \u0641\u0648\u0642 \u0627\u0644\u0646\u0637\u0627\u0642 \u0627\u0644\u0645\u0631\u062c\u0639\u064a</li><li>\u062a\u0627\u0631\u064a\u062e \u0639\u0627\u0626\u0644\u064a \u0644\u0633\u0643\u0631\u064a \u0627\u0644\u0646\u0648\u0639 2 \u0623\u0648 \u0645\u062a\u0644\u0627\u0632\u0645\u0629 \u0623\u064a\u0636\u064a\u0629</li><li>\u0632\u064a\u0627\u062f\u0629 \u0648\u0632\u0646 \u0641\u064a \u0627\u0644\u0628\u0637\u0646 \u0623\u0648 \u0623\u0639\u0631\u0627\u0636 PCOS</li><li>\u0625\u0631\u0647\u0627\u0642 \u0645\u0633\u062a\u0645\u0631\u060c \u062c\u0648\u0639 \u0645\u062a\u0643\u0631\u0631\u060c \u062a\u063a\u064a\u0651\u0631\u0627\u062a \u0648\u0632\u0646 \u063a\u064a\u0631 \u0645\u0628\u0631\u0631\u0629</li><li>\u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0637\u0628\u064a\u0639\u064a \u0644\u0643\u0646 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0645\u0631\u062a\u0641\u0639</li></ul><p>\u062d\u062a\u0649 \u0628\u062f\u0648\u0646 \u0623\u0639\u0631\u0627\u0636\u060c \u0627\u0644\u0625\u0628\u0644\u0627\u063a \u0639\u0646 \u0646\u062a\u064a\u062c\u0629 \u063a\u064a\u0631 \u0637\u0628\u064a\u0639\u064a\u0629 \u0644\u0644\u0637\u0628\u064a\u0628 \u062e\u0637\u0648\u0629 \u062d\u0643\u064a\u0645\u0629.</p>"),
        Section(id="how-norya-helps", level=2, heading="\u0627\u0641\u0647\u0645 \u0646\u062a\u0627\u0626\u062c\u0643 \u0623\u0641\u0636\u0644 \u0645\u0639 Norya", body_html="<p>\u0641\u064a Norya \u0644\u0627 \u0646\u064f\u0634\u062e\u0651\u0635 \u2014 \u0644\u0643\u0646\u0646\u0627 \u0646\u0633\u0627\u0639\u062f\u0643 \u0639\u0644\u0649 \u0641\u0647\u0645 \u0641\u062d\u0648\u0635\u0627\u062a\u0643. <a href=\"/analyze\">\u0627\u0631\u0641\u0639 \u062a\u0642\u0631\u064a\u0631\u0643</a> \u0648\u0627\u062d\u0635\u0644 \u0639\u0644\u0649 \u0645\u0644\u062e\u0635 \u0645\u0646\u0638\u0651\u0645 \u0628\u0644\u063a\u0629 \u0648\u0627\u0636\u062d\u0629 \u0645\u0639 \u0646\u0637\u0627\u0642\u0627\u062a \u0645\u0631\u062c\u0639\u064a\u0629. <a href=\"/pricing\">\u0627\u0644\u0623\u0633\u0639\u0627\u0631</a>.</p>"),
        Section(id="disclaimer", level=2, heading="\u0625\u062e\u0644\u0627\u0621 \u0627\u0644\u0645\u0633\u0624\u0648\u0644\u064a\u0629", body_html="<p><strong>\u0647\u0630\u0627 \u0627\u0644\u0645\u062d\u062a\u0648\u0649 \u0644\u0623\u063a\u0631\u0627\u0636 \u0625\u0639\u0644\u0627\u0645\u064a\u0629 \u0641\u0642\u0637 \u0648\u0644\u0627 \u064a\u062d\u0644 \u0645\u062d\u0644 \u0627\u0644\u0627\u0633\u062a\u0634\u0627\u0631\u0629 \u0627\u0644\u0637\u0628\u064a\u0629 \u0623\u0648 \u0627\u0644\u062a\u0634\u062e\u064a\u0635.</strong> \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0642\u062f \u064a\u0643\u0648\u0646 \u0644\u0623\u0633\u0628\u0627\u0628 \u0639\u062f\u064a\u062f\u0629\u061b \u0627\u0644\u0637\u0628\u064a\u0628 \u0627\u0644\u0630\u064a \u064a\u0639\u0631\u0641 \u062a\u0627\u0631\u064a\u062e\u0643 \u0647\u0648 \u0648\u062d\u062f\u0647 \u0627\u0644\u0642\u0627\u062f\u0631 \u0639\u0644\u0649 \u0627\u0644\u062a\u0641\u0633\u064a\u0631 \u0627\u0644\u0635\u062d\u064a\u062d. \u0646\u0627\u0642\u0634 \u062a\u062d\u0627\u0644\u064a\u0644\u0643 \u062f\u0627\u0626\u0645\u064b\u0627 \u0645\u0639 \u0637\u0628\u064a\u0628.</p>"),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_fasting_insulin_sections_by_lang():
    """Returns sections_by_lang dict for High Fasting Insulin article (all 9 languages)."""
    return {
        "tr": _sections_tr(),
        "en": _sections_en(),
        "es": _sections_es(),
        "de": _sections_de(),
        "fr": _sections_fr(),
        "it": _sections_it(),
        "he": _sections_he(),
        "hi": _sections_hi(),
        "ar": _sections_ar(),
    }


def get_fasting_insulin_faq_schema_qa():
    """Returns faq_schema_qa dict for High Fasting Insulin article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is fasting insulin?",
             "answer": "Fasting insulin is the level of insulin in your blood after 8–12 hours without food. It reflects your body's baseline insulin activity and is used alongside fasting glucose to assess insulin resistance."},
            {"question": "What does high fasting insulin mean?",
             "answer": "A high fasting insulin level suggests your body is producing more insulin than expected to keep blood sugar in range. This may indicate early insulin resistance, but a single value is not a diagnosis — your doctor interprets it with other tests and your clinical history."},
            {"question": "Can fasting glucose be normal while fasting insulin is high?",
             "answer": "Yes. This is called compensatory hyperinsulinaemia: the pancreas works harder to push glucose into resistant cells, keeping glucose normal while insulin rises. It can be an early sign of metabolic strain even when glucose looks fine."},
        ],
        "tr": [
            {"question": "Açlık insülini nedir?",
             "answer": "Açlık insülini, 8–12 saat yemek yemeden alınan kan örneğinde ölçülen insülin düzeyidir. Vücudun bazal insülin aktivitesini yansıtır ve insülin direncini değerlendirmek için açlık glukozu ile birlikte kullanılır."},
            {"question": "Açlık insülini yüksekse ne anlama gelir?",
             "answer": "Yüksek açlık insülini, vücudun kan şekerini normal aralıkta tutmak için beklenenden fazla insülin ürettiğine işaret eder. Erken insülin direncinin belirtisi olabilir; ancak tek bir değer teşhis koymaz — hekim diğer testler ve klinik öykünüzle birlikte yorumlar."},
            {"question": "Kan şekeri normal olsa bile insülin yüksek çıkabilir mi?",
             "answer": "Evet. Buna kompansatuvar hiperinsulinemi denir: pankreas, dirençli hücrelere glukozu sokmak için daha fazla çalışır ve glukoz normal kalırken insülin yükselir. Glukoz iyi görünse bile metabolik zorlama başlamış olabilir."},
        ],
        "es": [
            {"question": "¿Qué es la insulina en ayunas?",
             "answer": "La insulina en ayunas es el nivel de insulina en sangre tras 8–12 horas sin comer. Refleja la actividad basal de insulina y se usa junto con la glucosa en ayunas para evaluar la resistencia a la insulina."},
            {"question": "¿Qué significa tener la insulina en ayunas alta?",
             "answer": "Un nivel alto sugiere que el cuerpo produce más insulina de lo esperado para mantener la glucosa en rango. Puede indicar resistencia a la insulina temprana, pero un solo valor no es diagnóstico; el médico lo interpreta con otros análisis y tu historial."},
            {"question": "¿Puede la glucosa ser normal con la insulina alta?",
             "answer": "Sí. Se llama hiperinsulinemia compensatoria: el páncreas trabaja más para mantener la glucosa normal mientras la insulina sube. Puede ser una señal temprana de esfuerzo metabólico."},
        ],
        "de": [
            {"question": "Was ist Nüchterninsulin?",
             "answer": "Nüchterninsulin ist der Insulinspiegel im Blut nach 8–12 Stunden Nahrungskarenz. Er zeigt die basale Insulinaktivität und wird zusammen mit der Nüchternglukose zur Beurteilung einer Insulinresistenz herangezogen."},
            {"question": "Was bedeutet ein erhöhtes Nüchterninsulin?",
             "answer": "Ein hoher Wert deutet darauf hin, dass der Körper mehr Insulin produziert als erwartet, um den Blutzucker im Normalbereich zu halten. Das kann ein frühes Zeichen für Insulinresistenz sein — ein einzelner Wert ist jedoch keine Diagnose; der Arzt beurteilt ihn zusammen mit anderen Befunden."},
            {"question": "Kann der Blutzucker normal sein, obwohl das Insulin hoch ist?",
             "answer": "Ja. Man spricht von kompensatorischer Hyperinsulinämie: Die Bauchspeicheldrüse arbeitet stärker, um den Blutzucker trotz nachlassender Insulinempfindlichkeit normal zu halten. Das kann ein frühes Zeichen metabolischer Belastung sein."},
        ],
        "fr": [
            {"question": "Qu'est-ce que l'insuline à jeun ?",
             "answer": "L'insuline à jeun est le taux d'insuline mesuré après 8–12 heures sans nourriture. Il reflète l'activité insulinique basale et est utilisé avec la glycémie à jeun pour évaluer l'insulinorésistance."},
            {"question": "Que signifie une insuline à jeun élevée ?",
             "answer": "Un taux élevé suggère que l'organisme produit plus d'insuline que prévu pour maintenir la glycémie. Cela peut indiquer une insulinorésistance précoce, mais un seul dosage ne fait pas un diagnostic — le médecin l'interprète avec d'autres examens."},
            {"question": "La glycémie peut-elle être normale avec une insuline élevée ?",
             "answer": "Oui. On parle d'hyperinsulinémie compensatoire : le pancréas travaille davantage pour maintenir la glycémie normale malgré la résistance. C'est parfois un signe précoce de stress métabolique."},
        ],
        "it": [
            {"question": "Cos'è l'insulina a digiuno?",
             "answer": "L'insulina a digiuno è il livello di insulina nel sangue dopo 8–12 ore senza cibo. Riflette l'attività insulinica basale e viene usata con la glicemia a digiuno per valutare la resistenza insulinica."},
            {"question": "Cosa significa avere l'insulina a digiuno alta?",
             "answer": "Un valore elevato suggerisce che l'organismo produce più insulina del previsto per mantenere la glicemia nei limiti. Può indicare una resistenza insulinica precoce, ma un singolo valore non è una diagnosi; il medico lo interpreta con altri esami."},
            {"question": "La glicemia può essere normale con l'insulina alta?",
             "answer": "Sì. Si chiama iperinsulinemia compensatoria: il pancreas lavora di più per mantenere la glicemia normale nonostante la resistenza cellulare. Può essere un segnale precoce di stress metabolico."},
        ],
        "he": [
            {"question": "\u05de\u05d4\u05d5 \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd?",
             "answer": "\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d4\u05d5\u05d0 \u05e8\u05de\u05ea \u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05d3\u05dd \u05d0\u05d7\u05e8\u05d9 8\u201312 \u05e9\u05e2\u05d5\u05ea \u05dc\u05dc\u05d0 \u05d0\u05db\u05d9\u05dc\u05d4. \u05d4\u05d5\u05d0 \u05de\u05e9\u05e7\u05e3 \u05d0\u05ea \u05e4\u05e2\u05d9\u05dc\u05d5\u05ea \u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d4\u05d1\u05e1\u05d9\u05e1\u05d9\u05ea \u05d5\u05de\u05e9\u05de\u05e9 \u05dc\u05d4\u05e2\u05e8\u05db\u05ea \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05dc\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df."},
            {"question": "\u05de\u05d4 \u05de\u05e9\u05de\u05e2\u05d5\u05ea \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d1\u05e6\u05d5\u05dd \u05d2\u05d1\u05d5\u05d4?",
             "answer": "\u05e2\u05e8\u05da \u05d2\u05d1\u05d5\u05d4 \u05de\u05e8\u05de\u05d6 \u05e9\u05d4\u05d2\u05d5\u05e3 \u05de\u05d9\u05d9\u05e6\u05e8 \u05d9\u05d5\u05ea\u05e8 \u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05de\u05d4\u05e6\u05e4\u05d5\u05d9 \u05dc\u05e9\u05de\u05d9\u05e8\u05d4 \u05e2\u05dc \u05e8\u05de\u05ea \u05e1\u05d5\u05db\u05e8 \u05ea\u05e7\u05d9\u05e0\u05d4. \u05d6\u05d4 \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d4\u05e6\u05d1\u05d9\u05e2 \u05e2\u05dc \u05e2\u05de\u05d9\u05d3\u05d5\u05ea \u05de\u05d5\u05e7\u05d3\u05de\u05ea, \u05d0\u05da \u05e2\u05e8\u05da \u05d1\u05d5\u05d3\u05d3 \u05d0\u05d9\u05e0\u05d5 \u05d0\u05d1\u05d7\u05e0\u05d4 \u2014 \u05d4\u05e8\u05d5\u05e4\u05d0 \u05de\u05e4\u05e8\u05e9 \u05e2\u05dd \u05d1\u05d3\u05d9\u05e7\u05d5\u05ea \u05e0\u05d5\u05e1\u05e4\u05d5\u05ea."},
            {"question": "\u05d4\u05d0\u05dd \u05d4\u05e1\u05d5\u05db\u05e8 \u05d9\u05db\u05d5\u05dc \u05dc\u05d4\u05d9\u05d5\u05ea \u05ea\u05e7\u05d9\u05df \u05db\u05e9\u05d4\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05df \u05d2\u05d1\u05d5\u05d4?",
             "answer": "\u05db\u05df. \u05d6\u05d4 \u05e0\u05e7\u05e8\u05d0 \u05d4\u05d9\u05e4\u05e8\u05d0\u05d9\u05e0\u05e1\u05d5\u05dc\u05d9\u05e0\u05de\u05d9\u05d4 \u05de\u05e4\u05e6\u05d4: \u05d4\u05dc\u05d1\u05dc\u05d1 \u05e2\u05d5\u05d1\u05d3 \u05d7\u05d6\u05e7 \u05d9\u05d5\u05ea\u05e8 \u05dc\u05e9\u05de\u05d5\u05e8 \u05e2\u05dc \u05e1\u05d5\u05db\u05e8 \u05ea\u05e7\u05d9\u05df \u05dc\u05de\u05e8\u05d5\u05ea \u05e2\u05de\u05d9\u05d3\u05d5\u05ea. \u05d6\u05d4 \u05e2\u05e9\u05d5\u05d9 \u05dc\u05d4\u05d9\u05d5\u05ea \u05e1\u05d9\u05de\u05df \u05de\u05d5\u05e7\u05d3\u05dd \u05dc\u05e2\u05d5\u05de\u05e1 \u05d0\u05d9\u05e6\u05d9."},
        ],
        "hi": [
            {"question": "फ़ास्टिंग इंसुलिन क्या है?",
             "answer": "फ़ास्टिंग इंसुलिन 8–12 घंटे बिना कुछ खाए ब्लड में इंसुलिन का लेवल है। यह बेसल इंसुलिन एक्टिविटी दिखाता है और इंसुलिन रेज़िस्टेंस का आकलन करने के लिए फ़ास्टिंग ग्लूकोज़ के साथ इस्तेमाल होता है।"},
            {"question": "हाई फ़ास्टिंग इंसुलिन का क्या मतलब है?",
             "answer": "हाई वैल्यू बताती है कि शरीर ब्लड शुगर नॉर्मल रखने के लिए ज़्यादा इंसुलिन बना रहा है। यह अर्ली इंसुलिन रेज़िस्टेंस का संकेत हो सकता है, लेकिन अकेली वैल्यू निदान नहीं है — डॉक्टर बाक़ी टेस्ट और हिस्ट्री के साथ पढ़ते हैं।"},
            {"question": "क्या ग्लूकोज़ नॉर्मल होकर भी इंसुलिन हाई हो सकता है?",
             "answer": "हाँ। इसे कम्पेन्सेटरी हाइपरइंसुलिनीमिया कहते हैं: पैंक्रियाज़ ज़्यादा काम करता है ताकि रेज़िस्टेंट सेल्स में ग्लूकोज़ जाए और शुगर नॉर्मल रहे। यह मेटाबोलिक स्ट्रेस का अर्ली साइन हो सकता है।"},
        ],
        "ar": [
            {"question": "\u0645\u0627 \u0647\u0648 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u061f",
             "answer": "\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645 \u0647\u0648 \u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0641\u064a \u0627\u0644\u062f\u0645 \u0628\u0639\u062f 8\u201312 \u0633\u0627\u0639\u0629 \u0635\u064a\u0627\u0645. \u064a\u0639\u0643\u0633 \u0627\u0644\u0646\u0634\u0627\u0637 \u0627\u0644\u0642\u0627\u0639\u062f\u064a \u0644\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0648\u064a\u064f\u0633\u062a\u062e\u062f\u0645 \u0645\u0639 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0644\u062a\u0642\u064a\u064a\u0645 \u0645\u0642\u0627\u0648\u0645\u0629 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646."},
            {"question": "\u0645\u0627\u0630\u0627 \u064a\u0639\u0646\u064a \u0627\u0631\u062a\u0641\u0627\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u0635\u0627\u0626\u0645\u061f",
             "answer": "\u0642\u064a\u0645\u0629 \u0645\u0631\u062a\u0641\u0639\u0629 \u062a\u0634\u064a\u0631 \u0625\u0644\u0649 \u0623\u0646 \u0627\u0644\u062c\u0633\u0645 \u064a\u0646\u062a\u062c \u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0623\u0643\u062b\u0631 \u0644\u0644\u062d\u0641\u0627\u0638 \u0639\u0644\u0649 \u0627\u0644\u0633\u0643\u0631 \u0637\u0628\u064a\u0639\u064a\u064b\u0627. \u0642\u062f \u064a\u062f\u0644 \u0639\u0644\u0649 \u0645\u0642\u0627\u0648\u0645\u0629 \u0645\u0628\u0643\u0631\u0629\u060c \u0644\u0643\u0646 \u0642\u064a\u0645\u0629 \u0648\u0627\u062d\u062f\u0629 \u0644\u064a\u0633\u062a \u062a\u0634\u062e\u064a\u0635\u064b\u0627 \u2014 \u0627\u0644\u0637\u0628\u064a\u0628 \u064a\u064f\u0641\u0633\u0651\u0631\u0647\u0627 \u0645\u0639 \u0641\u062d\u0648\u0635\u0627\u062a \u0648\u062a\u0627\u0631\u064a\u062e \u0633\u0631\u064a\u0631\u064a."},
            {"question": "\u0647\u0644 \u064a\u0645\u0643\u0646 \u0623\u0646 \u064a\u0643\u0648\u0646 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0637\u0628\u064a\u0639\u064a\u064b\u0627 \u0648\u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0645\u0631\u062a\u0641\u0639\u064b\u0627\u061f",
             "answer": "\u0646\u0639\u0645. \u064a\u064f\u0633\u0645\u0651\u0649 \u0641\u0631\u0637 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646 \u0627\u0644\u062a\u0639\u0648\u064a\u0636\u064a: \u0627\u0644\u0628\u0646\u0643\u0631\u064a\u0627\u0633 \u064a\u0639\u0645\u0644 \u0628\u062c\u0647\u062f \u0623\u0643\u0628\u0631 \u0644\u0625\u062f\u062e\u0627\u0644 \u0627\u0644\u063a\u0644\u0648\u0643\u0648\u0632 \u0625\u0644\u0649 \u062e\u0644\u0627\u064a\u0627 \u0645\u0642\u0627\u0648\u0645\u0629\u060c \u0641\u064a\u0628\u0642\u0649 \u0627\u0644\u0633\u0643\u0631 \u0637\u0628\u064a\u0639\u064a\u064b\u0627 \u0628\u064a\u0646\u0645\u0627 \u064a\u0631\u062a\u0641\u0639 \u0627\u0644\u0623\u0646\u0633\u0648\u0644\u064a\u0646. \u0642\u062f \u064a\u0643\u0648\u0646 \u0625\u0646\u0630\u0627\u0631 \u0623\u064a\u0636\u064a \u0645\u0628\u0643\u0631."},
        ],
    }
