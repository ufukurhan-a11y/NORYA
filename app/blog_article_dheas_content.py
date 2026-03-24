# -*- coding: utf-8 -*-
"""
DHEA-S (DHEA Sulfate) blog article — full body content for all 9 languages.
Used by blog_i18n._article_dheas().
Sections: intro, normal-ranges, causes, when-to-see-doctor.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_TBL = (
    'class="w-full border border-slate-200 text-sm my-4" '
    'style="border-collapse: collapse;"'
)
_TH = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
_TH_RTL = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;"'
_TD = 'style="border:1px solid #cbd5e1;padding:8px 12px;"'


# ---------------------------------------------------------------------------
# Reference-range tables — one per language
# ---------------------------------------------------------------------------

_DHEAS_TABLE_TR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Yaş</th>"
    f"<th {_TH}>Erkek (µg/dL)</th>"
    f"<th {_TH}>Kadın (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_EN = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Age</th>"
    f"<th {_TH}>Male (µg/dL)</th>"
    f"<th {_TH}>Female (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_ES = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Edad</th>"
    f"<th {_TH}>Hombre (µg/dL)</th>"
    f"<th {_TH}>Mujer (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_DE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Alter</th>"
    f"<th {_TH}>Männer (µg/dL)</th>"
    f"<th {_TH}>Frauen (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_FR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Âge</th>"
    f"<th {_TH}>Homme (µg/dL)</th>"
    f"<th {_TH}>Femme (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_IT = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Età</th>"
    f"<th {_TH}>Uomini (µg/dL)</th>"
    f"<th {_TH}>Donne (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_HE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>גיל</th>"
    f"<th {_TH_RTL}>גברים (µg/dL)</th>"
    f"<th {_TH_RTL}>נשים (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_HI = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>आयु</th>"
    f"<th {_TH}>पुरुष (µg/dL)</th>"
    f"<th {_TH}>महिला (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)

_DHEAS_TABLE_AR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>العمر</th>"
    f"<th {_TH_RTL}>ذكور (µg/dL)</th>"
    f"<th {_TH_RTL}>إناث (µg/dL)</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>18–19</td><td {_TD}>108–441</td><td {_TD}>145–395</td></tr>"
    f"<tr><td {_TD}>20–29</td><td {_TD}>280–640</td><td {_TD}>65–380</td></tr>"
    f"<tr><td {_TD}>30–39</td><td {_TD}>120–520</td><td {_TD}>45–270</td></tr>"
    f"<tr><td {_TD}>40–49</td><td {_TD}>95–530</td><td {_TD}>32–240</td></tr>"
    f"<tr><td {_TD}>50–59</td><td {_TD}>70–310</td><td {_TD}>26–200</td></tr>"
    f"<tr><td {_TD}>60–69</td><td {_TD}>42–290</td><td {_TD}>13–130</td></tr>"
    f"<tr><td {_TD}>70+</td><td {_TD}>28–175</td><td {_TD}>10–90</td></tr>"
    "</tbody></table>"
)


# ---------------------------------------------------------------------------
# Turkish
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="DHEA-S kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>DHEA-S testi</strong> (dehidroepiandrosteron sülfat), böbreküstü bezlerinin "
                "ürettiği en bol <strong>adrenal hormon</strong> olan DHEA'nın sülfatlanmış formunun "
                "kandaki düzeyini ölçen bir <strong>DHEA sülfat kan testi</strong>dir. DHEA-S, vücutta "
                "testosteron ve östrojen gibi seks hormonlarına dönüştürülebilen bir öncül hormondur "
                "ve adrenal bez fonksiyonunun en güvenilir göstergelerinden biri olarak kabul edilir.</p>"
                "<p><strong>DHEA-S testi</strong> özellikle kadınlarda aşırı kıllanma (hirsutizm), akne "
                "veya düzensiz adet gibi <strong>yüksek DHEA-S</strong> belirtileri araştırılırken ya da "
                "kronik yorgunluk, kas güçsüzlüğü gibi <strong>düşük DHEA-S</strong> semptomları "
                "değerlendirilirken istenir. Polikistik over sendromu (PKOS), konjenital adrenal "
                "hiperplazi (KAH) ve adrenal tümör gibi durumların tanısında kritik rol oynar.</p>"
                "<p>DHEA-S düzeyleri yaşla birlikte doğal olarak azalır; bu süreç adrenopoz olarak "
                "bilinir. Zirve değerler genellikle 20'li yaşlarda görülür ve sonrasında her on yılda "
                "belirgin bir düşüş başlar. Bu nedenle <strong>DHEA-S normal aralığı</strong> "
                "değerlendirilirken yaş ve cinsiyet mutlaka göz önünde bulundurulmalıdır.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="DHEA-S normal değerleri (yaşa ve cinsiyete göre)",
            body_html=(
                "<p><strong>DHEA-S normal aralığı</strong>, yaş ve cinsiyete göre önemli ölçüde "
                "değişir. Aşağıdaki tabloda yetişkinler için yaygın olarak kabul edilen referans "
                "değerleri özetlenmiştir. Sonuçlar genellikle mikrogram/desilitre (µg/dL) cinsinden "
                "raporlanır; bazı laboratuvarlar µmol/L kullanabilir (1 µg/dL ≈ 0,027 µmol/L).</p>"
                "<p>Aşağıdaki tablo, yaş gruplarına göre erkek ve kadın <strong>DHEA sülfat "
                "düzeyleri</strong>ni göstermektedir:</p>"
                + _DHEAS_TABLE_TR +
                "<p>DHEA-S düzeyleri 20–30 yaş arasında en yüksek seviyeye ulaşır ve ardından "
                "her on yılda yaklaşık %10–20 oranında azalır. 70 yaş üzerinde değerler zirvenin "
                "yaklaşık %20–30'una düşebilir. Sonuçlarınızı değerlendirirken laboratuvarınızın "
                "raporundaki yaşa ve cinsiyete özgü referans aralığını esas alın.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="DHEA-S yüksekliği veya düşüklüğünün nedenleri",
            body_html=(
                "<p><strong>Yüksek DHEA-S</strong> veya <strong>düşük DHEA-S</strong> birçok farklı "
                "klinik durumun göstergesi olabilir. Değerlerin yorumlanması klinik bulgularla "
                "birlikte yapılmalıdır. Başlıca nedenler şunlardır:</p>"
                "<p><strong>DHEA-S yüksekliği nedenleri:</strong></p>"
                "<ul>"
                "<li><strong>Polikistik over sendromu (PKOS):</strong> Kadınlarda en sık yüksek "
                "DHEA-S nedeni olan PKOS, hiperandrojenizm, düzensiz adet ve polikistik overlere "
                "yol açar.</li>"
                "<li><strong>Konjenital adrenal hiperplazi (KAH):</strong> Adrenal steroid sentez "
                "enzimlerindeki genetik bozukluklar DHEA-S'nin aşırı üretilmesine neden olur.</li>"
                "<li><strong>Adrenal tümörler:</strong> Adrenal bez adenomu veya karsinomu, "
                "DHEA-S düzeylerini belirgin şekilde yükseltebilir; çok yüksek değerler malignite "
                "açısından uyarıcıdır.</li>"
                "<li><strong>Cushing sendromu:</strong> ACTH bağımlı formlarında adrenal androjenlerin "
                "aşırı üretimi görülebilir.</li>"
                "</ul>"
                "<p><strong>DHEA-S düşüklüğü nedenleri:</strong></p>"
                "<ul>"
                "<li><strong>Adrenal yetmezlik (Addison hastalığı):</strong> Böbreküstü bezlerinin "
                "yetersiz hormon üretmesi DHEA-S düzeylerinin düşmesine yol açar.</li>"
                "<li><strong>Hipopitüitarizm:</strong> Hipofiz bezinin ACTH üretimindeki azalma "
                "adrenal fonksiyonu baskılayarak DHEA-S'yi düşürür.</li>"
                "<li><strong>Adrenopoz (yaşa bağlı düşüş):</strong> Doğal yaşlanma sürecinde "
                "DHEA-S üretimi fizyolojik olarak azalır.</li>"
                "<li><strong>Uzun süreli kortikosteroid kullanımı:</strong> Eksojen steroidler "
                "hipotalamus-hipofiz-adrenal aksını baskılayarak DHEA-S düzeylerini düşürebilir.</li>"
                "</ul>"
                "<p>Tanıda DHEA-S, diğer adrenal hormonlar (kortizol, ACTH, 17-OH progesteron) "
                "ve gerektiğinde görüntüleme yöntemleriyle birlikte değerlendirilir. Tek bir "
                "DHEA-S sonucu kendi başına tanı koydurmaz.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Kadınlarda aşırı yüz veya vücut kıllanması, şiddetli akne, saç dökülmesi, "
                "adet düzensizliği veya kısırlık gibi belirtiler yaşıyorsanız bir endokrinoloji "
                "veya jinekoloji uzmanına başvurarak <strong>DHEA-S testi</strong> yaptırmanız "
                "önerilir. Bu belirtiler PKOS veya adrenal kaynaklı hiperandrojenizme işaret "
                "edebilir.</p>"
                "<p>Kronik yorgunluk, kas güçsüzlüğü, kilo kaybı, baş dönmesi veya düşük tansiyon "
                "gibi belirtiler ise <strong>düşük DHEA-S</strong> ve olası adrenal yetmezliğin "
                "habercisi olabilir. Bu semptomlarla birlikte cilt renginde koyulaşma fark ediyorsanız "
                "derhal tıbbi değerlendirme yaptırın çünkü Addison hastalığı tedavi edilmediğinde "
                "hayati tehlike oluşturabilir.</p>"
                "<p>Unutmayın: DHEA-S sonuçları tek başına değil, klinik tablo, diğer hormon testleri "
                "ve gerekli görüntüleme yöntemleriyle birlikte değerlendirilmelidir. Sonuçlarınız "
                "normalden sapmışsa bir uzman hekimle paylaşın; internet araştırmasına dayalı "
                "kendi kendinize tedavi uygulamayın.</p>"
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
            heading="DHEA-S blood test: what your results mean",
            body_html=(
                "<p>The <strong>DHEA-S test</strong> (dehydroepiandrosterone sulfate) measures the "
                "blood level of DHEA-S, the sulfated form of DHEA — the most abundant "
                "<strong>adrenal hormone</strong> produced by the adrenal glands. DHEA-S serves as "
                "a precursor that the body can convert into sex hormones such as testosterone and "
                "estrogen, and it is considered one of the most reliable markers of adrenal "
                "function.</p>"
                "<p>A <strong>DHEA sulfate blood test</strong> is commonly ordered when symptoms "
                "of <strong>high DHEA-S</strong> are investigated — such as excess body hair "
                "(hirsutism), severe acne, or irregular periods in women — or when "
                "<strong>low DHEA-S</strong> symptoms like chronic fatigue and muscle weakness are "
                "evaluated. It plays a critical role in diagnosing conditions such as polycystic "
                "ovary syndrome (PCOS), congenital adrenal hyperplasia (CAH), and adrenal "
                "tumors.</p>"
                "<p>DHEA-S levels decline naturally with age, a process known as adrenopause. Peak "
                "values typically occur in the 20s, followed by a steady decrease of roughly "
                "10–20 % per decade. For this reason the <strong>DHEA-S normal range</strong> must "
                "always be interpreted in the context of age and sex.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="DHEA-S normal range (by age and sex)",
            body_html=(
                "<p>The <strong>DHEA-S normal range</strong> varies considerably by age and sex. "
                "The table below summarises the commonly accepted reference values for adults. "
                "Results are typically reported in micrograms per decilitre (µg/dL); some "
                "laboratories use µmol/L (1 µg/dL ≈ 0.027 µmol/L).</p>"
                "<p>The following table shows male and female <strong>DHEA sulfate levels</strong> "
                "by age group:</p>"
                + _DHEAS_TABLE_EN +
                "<p><strong>DHEA sulfate levels</strong> reach their highest point between the "
                "ages of 20 and 30 and then decline by approximately 10–20 % per decade. By age "
                "70+ values may fall to roughly 20–30 % of their peak. Always compare your result "
                "with the age- and sex-specific reference range on your own laboratory report.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high or low DHEA-S",
            body_html=(
                "<p><strong>High DHEA-S</strong> or <strong>low DHEA-S</strong> can point to a "
                "variety of clinical conditions. Interpretation should always be combined with "
                "clinical findings. The main causes include:</p>"
                "<p><strong>Causes of high DHEA-S:</strong></p>"
                "<ul>"
                "<li><strong>Polycystic ovary syndrome (PCOS):</strong> The most common cause of "
                "elevated DHEA-S in women, PCOS leads to hyperandrogenism, irregular periods, and "
                "polycystic ovaries.</li>"
                "<li><strong>Congenital adrenal hyperplasia (CAH):</strong> Genetic defects in "
                "adrenal steroid-synthesis enzymes cause overproduction of DHEA-S.</li>"
                "<li><strong>Adrenal tumors:</strong> Adrenal adenomas or carcinomas can markedly "
                "elevate DHEA-S; very high values are a red flag for malignancy.</li>"
                "<li><strong>Cushing syndrome:</strong> ACTH-dependent forms may drive excess "
                "adrenal androgen production.</li>"
                "</ul>"
                "<p><strong>Causes of low DHEA-S:</strong></p>"
                "<ul>"
                "<li><strong>Adrenal insufficiency (Addison disease):</strong> Inadequate hormone "
                "production by the adrenal glands leads to low DHEA-S.</li>"
                "<li><strong>Hypopituitarism:</strong> Reduced ACTH output from the pituitary "
                "suppresses adrenal function and lowers DHEA-S.</li>"
                "<li><strong>Adrenopause (age-related decline):</strong> DHEA-S production "
                "physiologically decreases as part of normal ageing.</li>"
                "<li><strong>Long-term corticosteroid use:</strong> Exogenous steroids suppress "
                "the hypothalamic-pituitary-adrenal axis and can lower DHEA-S.</li>"
                "</ul>"
                "<p>For diagnosis, DHEA-S is evaluated alongside other <strong>adrenal hormone "
                "test</strong> results (cortisol, ACTH, 17-OH progesterone) and imaging when "
                "needed. A single DHEA-S result alone is not diagnostic.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If you are a woman experiencing excess facial or body hair, severe acne, hair "
                "loss, irregular periods, or infertility, consult an endocrinologist or "
                "gynaecologist and request a <strong>DHEA-S test</strong>. These symptoms may "
                "indicate PCOS or adrenal-origin hyperandrogenism.</p>"
                "<p>Chronic fatigue, muscle weakness, weight loss, dizziness, or low blood "
                "pressure may signal <strong>low DHEA-S</strong> and possible adrenal "
                "insufficiency. If you also notice skin darkening, seek medical evaluation "
                "promptly because untreated Addison disease can be life-threatening.</p>"
                "<p>Remember: DHEA-S results should not be evaluated in isolation. They must be "
                "considered together with the clinical picture, other hormone tests, and imaging "
                "as needed. If your results fall outside the normal range share them with a "
                "specialist — do not attempt self-treatment based on internet research alone.</p>"
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
            heading="Análisis de DHEA-S en sangre: qué significan sus resultados",
            body_html=(
                "<p>El <strong>análisis de DHEA-S</strong> (sulfato de dehidroepiandrosterona) mide "
                "el nivel en sangre de DHEA-S, la forma sulfatada de la DHEA, la <strong>hormona "
                "suprarrenal</strong> más abundante que producen las glándulas adrenales. La DHEA-S "
                "es un precursor hormonal que el organismo puede transformar en hormonas sexuales "
                "como la testosterona y el estrógeno, y se considera uno de los marcadores más "
                "fiables de la función suprarrenal.</p>"
                "<p>Un <strong>análisis de sulfato de DHEA</strong> se solicita habitualmente cuando "
                "se investigan síntomas de <strong>DHEA-S alta</strong> — como exceso de vello "
                "(hirsutismo), acné severo o períodos irregulares en mujeres — o cuando se evalúan "
                "síntomas de <strong>DHEA-S baja</strong> como fatiga crónica y debilidad muscular. "
                "Desempeña un papel crítico en el diagnóstico del síndrome de ovario poliquístico "
                "(SOP), la hiperplasia suprarrenal congénita (HSC) y los tumores suprarrenales.</p>"
                "<p>Los niveles de DHEA-S disminuyen de forma natural con la edad, un proceso "
                "conocido como adrenopausia. Los valores máximos suelen observarse en la década de "
                "los 20, seguidos de un descenso constante de aproximadamente un 10–20 % por década. "
                "Por ello, el <strong>rango normal de DHEA-S</strong> debe interpretarse siempre en "
                "función de la edad y el sexo.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de DHEA-S (por edad y sexo)",
            body_html=(
                "<p>El <strong>rango normal de DHEA-S</strong> varía considerablemente según la "
                "edad y el sexo. La tabla siguiente resume los valores de referencia generalmente "
                "aceptados para adultos. Los resultados suelen expresarse en microgramos por "
                "decilitro (µg/dL); algunos laboratorios usan µmol/L "
                "(1 µg/dL ≈ 0,027 µmol/L).</p>"
                "<p>La siguiente tabla muestra los <strong>niveles de sulfato de DHEA</strong> "
                "para hombres y mujeres por grupo de edad:</p>"
                + _DHEAS_TABLE_ES +
                "<p>Los <strong>niveles de sulfato de DHEA</strong> alcanzan su punto máximo entre "
                "los 20 y los 30 años y luego descienden aproximadamente un 10–20 % por década. A "
                "partir de los 70 años los valores pueden reducirse al 20–30 % de su pico. Compare "
                "siempre su resultado con el rango de referencia específico por edad y sexo de su "
                "propio informe de laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de DHEA-S alta o baja",
            body_html=(
                "<p>Una <strong>DHEA-S alta</strong> o <strong>DHEA-S baja</strong> puede ser "
                "indicativa de diversas afecciones clínicas. La interpretación debe realizarse "
                "siempre en conjunto con los hallazgos clínicos. Las principales causas son:</p>"
                "<p><strong>Causas de DHEA-S alta:</strong></p>"
                "<ul>"
                "<li><strong>Síndrome de ovario poliquístico (SOP):</strong> La causa más frecuente "
                "de DHEA-S elevada en mujeres; provoca hiperandrogenismo, períodos irregulares y "
                "ovarios poliquísticos.</li>"
                "<li><strong>Hiperplasia suprarrenal congénita (HSC):</strong> Defectos genéticos "
                "en las enzimas de síntesis de esteroides suprarrenales que causan sobreproducción "
                "de DHEA-S.</li>"
                "<li><strong>Tumores suprarrenales:</strong> Los adenomas o carcinomas adrenales "
                "pueden elevar marcadamente la DHEA-S; valores muy altos son una señal de alerta "
                "de malignidad.</li>"
                "<li><strong>Síndrome de Cushing:</strong> Las formas dependientes de ACTH pueden "
                "impulsar la producción excesiva de andrógenos suprarrenales.</li>"
                "</ul>"
                "<p><strong>Causas de DHEA-S baja:</strong></p>"
                "<ul>"
                "<li><strong>Insuficiencia suprarrenal (enfermedad de Addison):</strong> La "
                "producción hormonal inadecuada por las glándulas adrenales lleva a niveles bajos "
                "de DHEA-S.</li>"
                "<li><strong>Hipopituitarismo:</strong> La reducción de la producción de ACTH por "
                "la hipófisis suprime la función suprarrenal y disminuye la DHEA-S.</li>"
                "<li><strong>Adrenopausia (descenso relacionado con la edad):</strong> La "
                "producción de DHEA-S disminuye fisiológicamente como parte del envejecimiento "
                "normal.</li>"
                "<li><strong>Uso prolongado de corticosteroides:</strong> Los esteroides exógenos "
                "suprimen el eje hipotálamo-hipófiso-suprarrenal y pueden reducir la DHEA-S.</li>"
                "</ul>"
                "<p>Para el diagnóstico, la DHEA-S se evalúa junto con otros resultados de "
                "<strong>pruebas hormonales suprarrenales</strong> (cortisol, ACTH, "
                "17-OH progesterona) y estudios de imagen cuando es necesario. Un resultado "
                "aislado de DHEA-S no es diagnóstico por sí solo.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si es mujer y experimenta exceso de vello facial o corporal, acné severo, "
                "caída del cabello, períodos irregulares o infertilidad, consulte a un "
                "endocrinólogo o ginecólogo y solicite un <strong>análisis de DHEA-S</strong>. "
                "Estos síntomas pueden indicar SOP o hiperandrogenismo de origen suprarrenal.</p>"
                "<p>La fatiga crónica, la debilidad muscular, la pérdida de peso, los mareos o "
                "la presión arterial baja pueden ser señales de <strong>DHEA-S baja</strong> y "
                "de una posible insuficiencia suprarrenal. Si además nota oscurecimiento de la "
                "piel, busque evaluación médica con prontitud, ya que la enfermedad de Addison "
                "sin tratamiento puede ser potencialmente mortal.</p>"
                "<p>Recuerde: los resultados de DHEA-S no deben evaluarse de forma aislada. "
                "Deben considerarse junto con el cuadro clínico, otras pruebas hormonales y "
                "estudios de imagen según sea necesario. Si sus resultados están fuera del rango "
                "normal, compártalos con un especialista; no intente automedicarse basándose "
                "únicamente en búsquedas en internet.</p>"
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
            heading="DHEA-S-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>DHEA-S-Test</strong> (Dehydroepiandrosteron-Sulfat) misst den "
                "Blutspiegel von DHEA-S, der sulfatierten Form von DHEA — dem am häufigsten "
                "vorkommenden <strong>Nebennierenhormon</strong> der Nebennieren. DHEA-S dient als "
                "Vorstufe, die der Körper in Sexualhormone wie Testosteron und Östrogen umwandeln "
                "kann, und gilt als einer der zuverlässigsten Marker der Nebennierenfunktion.</p>"
                "<p>Ein <strong>DHEA-Sulfat-Bluttest</strong> wird häufig angeordnet, wenn Symptome "
                "eines <strong>hohen DHEA-S</strong> untersucht werden — wie übermäßige "
                "Körperbehaarung (Hirsutismus), schwere Akne oder unregelmäßige Menstruation bei "
                "Frauen — oder wenn <strong>niedrige DHEA-S</strong>-Symptome wie chronische "
                "Müdigkeit und Muskelschwäche bewertet werden. Er spielt eine entscheidende Rolle "
                "bei der Diagnose von Erkrankungen wie dem polyzystischen Ovarialsyndrom (PCOS), "
                "der kongenitalen Nebennierenhyperplasie (CAH) und Nebennierentumoren.</p>"
                "<p>Die DHEA-S-Werte sinken mit zunehmendem Alter auf natürliche Weise — ein "
                "Vorgang, der als Adrenopause bekannt ist. Spitzenwerte treten typischerweise in "
                "den 20er Jahren auf, gefolgt von einem stetigen Rückgang von etwa 10–20 % pro "
                "Dekade. Daher muss der <strong>DHEA-S-Normalbereich</strong> stets im Kontext von "
                "Alter und Geschlecht interpretiert werden.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="DHEA-S-Normalwerte (nach Alter und Geschlecht)",
            body_html=(
                "<p>Der <strong>DHEA-S-Normalbereich</strong> variiert erheblich nach Alter und "
                "Geschlecht. Die folgende Tabelle fasst die allgemein anerkannten Referenzwerte "
                "für Erwachsene zusammen. Ergebnisse werden in der Regel in Mikrogramm pro "
                "Deziliter (µg/dL) angegeben; einige Labore verwenden µmol/L "
                "(1 µg/dL ≈ 0,027 µmol/L).</p>"
                "<p>Die Tabelle zeigt die <strong>DHEA-Sulfat-Spiegel</strong> für Männer und "
                "Frauen nach Altersgruppe:</p>"
                + _DHEAS_TABLE_DE +
                "<p>Die <strong>DHEA-Sulfat-Spiegel</strong> erreichen ihren Höchstwert zwischen "
                "dem 20. und 30. Lebensjahr und sinken dann pro Dekade um etwa 10–20 %. Ab dem "
                "70. Lebensjahr können die Werte auf etwa 20–30 % ihres Höchstwerts fallen. "
                "Vergleichen Sie Ihr Ergebnis stets mit dem alters- und geschlechtsspezifischen "
                "Referenzbereich Ihres eigenen Laborbefunds.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für hohes oder niedriges DHEA-S",
            body_html=(
                "<p><strong>Hohes DHEA-S</strong> oder <strong>niedriges DHEA-S</strong> kann auf "
                "verschiedene klinische Erkrankungen hinweisen. Die Interpretation sollte stets "
                "zusammen mit den klinischen Befunden erfolgen. Die wichtigsten Ursachen sind:</p>"
                "<p><strong>Ursachen für hohes DHEA-S:</strong></p>"
                "<ul>"
                "<li><strong>Polyzystisches Ovarialsyndrom (PCOS):</strong> Die häufigste Ursache "
                "erhöhter DHEA-S-Werte bei Frauen; PCOS führt zu Hyperandrogenismus, "
                "unregelmäßiger Menstruation und polyzystischen Ovarien.</li>"
                "<li><strong>Kongenitale Nebennierenhyperplasie (CAH):</strong> Genetische Defekte "
                "in den Enzymen der Nebennieren-Steroidsynthese führen zu einer Überproduktion von "
                "DHEA-S.</li>"
                "<li><strong>Nebennierentumoren:</strong> Nebennierenadenome oder -karzinome können "
                "den DHEA-S-Spiegel deutlich erhöhen; sehr hohe Werte sind ein Warnzeichen für "
                "Malignität.</li>"
                "<li><strong>Cushing-Syndrom:</strong> ACTH-abhängige Formen können eine übermäßige "
                "Produktion adrenaler Androgene verursachen.</li>"
                "</ul>"
                "<p><strong>Ursachen für niedriges DHEA-S:</strong></p>"
                "<ul>"
                "<li><strong>Nebenniereninsuffizienz (Morbus Addison):</strong> Eine unzureichende "
                "Hormonproduktion der Nebennieren führt zu niedrigen DHEA-S-Werten.</li>"
                "<li><strong>Hypopituitarismus:</strong> Eine verminderte ACTH-Ausschüttung der "
                "Hypophyse unterdrückt die Nebennierenfunktion und senkt DHEA-S.</li>"
                "<li><strong>Adrenopause (altersbedingte Abnahme):</strong> Die DHEA-S-Produktion "
                "nimmt im Rahmen des normalen Alterungsprozesses physiologisch ab.</li>"
                "<li><strong>Langfristige Kortikosteroideinnahme:</strong> Exogene Steroide "
                "unterdrücken die Hypothalamus-Hypophysen-Nebennieren-Achse und können DHEA-S "
                "senken.</li>"
                "</ul>"
                "<p>Für die Diagnose wird DHEA-S zusammen mit anderen "
                "<strong>Nebennierenhormon-Tests</strong> (Cortisol, ACTH, 17-OH-Progesteron) und "
                "bei Bedarf mit Bildgebung bewertet. Ein einzelner DHEA-S-Wert allein ist nicht "
                "diagnostisch.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Sie als Frau unter übermäßiger Gesichts- oder Körperbehaarung, schwerer "
                "Akne, Haarausfall, unregelmäßiger Menstruation oder Unfruchtbarkeit leiden, "
                "wenden Sie sich an einen Endokrinologen oder Gynäkologen und lassen Sie einen "
                "<strong>DHEA-S-Test</strong> durchführen. Diese Symptome können auf PCOS oder "
                "einen adrenalen Hyperandrogenismus hindeuten.</p>"
                "<p>Chronische Müdigkeit, Muskelschwäche, Gewichtsverlust, Schwindel oder "
                "niedriger Blutdruck können auf <strong>niedriges DHEA-S</strong> und eine "
                "mögliche Nebenniereninsuffizienz hinweisen. Wenn Sie zusätzlich eine "
                "Hautverdunkelung bemerken, suchen Sie umgehend ärztliche Hilfe, da ein "
                "unbehandelter Morbus Addison lebensbedrohlich sein kann.</p>"
                "<p>Denken Sie daran: DHEA-S-Ergebnisse sollten nicht isoliert bewertet werden. "
                "Sie müssen zusammen mit dem klinischen Bild, anderen Hormontests und ggf. "
                "Bildgebung betrachtet werden. Wenn Ihre Ergebnisse außerhalb des Normalbereichs "
                "liegen, besprechen Sie diese mit einem Facharzt — versuchen Sie keine "
                "Selbstbehandlung auf Basis von Internetrecherchen.</p>"
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
            heading="Test de DHEA-S : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test de DHEA-S</strong> (sulfate de déhydroépiandrostérone) mesure "
                "le taux sanguin de DHEA-S, la forme sulfatée de la DHEA — l'<strong>hormone "
                "surrénalienne</strong> la plus abondante produite par les glandes surrénales. La "
                "DHEA-S sert de précurseur que l'organisme peut convertir en hormones sexuelles "
                "telles que la testostérone et l'œstrogène, et elle est considérée comme l'un des "
                "marqueurs les plus fiables de la fonction surrénalienne.</p>"
                "<p>Une <strong>analyse sanguine de sulfate de DHEA</strong> est couramment "
                "prescrite lorsque des symptômes d'un <strong>DHEA-S élevé</strong> sont explorés "
                "— tels qu'une pilosité excessive (hirsutisme), une acné sévère ou des règles "
                "irrégulières chez la femme — ou lorsque des symptômes de <strong>DHEA-S "
                "bas</strong> comme une fatigue chronique et une faiblesse musculaire sont évalués. "
                "Il joue un rôle essentiel dans le diagnostic du syndrome des ovaires polykystiques "
                "(SOPK), de l'hyperplasie congénitale des surrénales (HCS) et des tumeurs "
                "surrénaliennes.</p>"
                "<p>Les taux de DHEA-S diminuent naturellement avec l'âge, un processus connu sous "
                "le nom d'adrénopause. Les valeurs maximales apparaissent généralement vers la "
                "vingtaine, suivies d'une baisse régulière d'environ 10 à 20 % par décennie. "
                "C'est pourquoi les <strong>valeurs normales de DHEA-S</strong> doivent toujours "
                "être interprétées en fonction de l'âge et du sexe.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de DHEA-S (par âge et sexe)",
            body_html=(
                "<p>Les <strong>valeurs normales de DHEA-S</strong> varient considérablement selon "
                "l'âge et le sexe. Le tableau ci-dessous résume les valeurs de référence "
                "généralement acceptées pour les adultes. Les résultats sont habituellement "
                "exprimés en microgrammes par décilitre (µg/dL) ; certains laboratoires utilisent "
                "les µmol/L (1 µg/dL ≈ 0,027 µmol/L).</p>"
                "<p>Le tableau suivant présente les <strong>taux de sulfate de DHEA</strong> "
                "pour les hommes et les femmes par tranche d'âge :</p>"
                + _DHEAS_TABLE_FR +
                "<p>Les <strong>taux de sulfate de DHEA</strong> atteignent leur maximum entre 20 "
                "et 30 ans, puis diminuent d'environ 10 à 20 % par décennie. Après 70 ans, les "
                "valeurs peuvent tomber à environ 20–30 % de leur pic. Comparez toujours votre "
                "résultat avec l'intervalle de référence spécifique à l'âge et au sexe figurant "
                "sur votre propre rapport de laboratoire.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un DHEA-S élevé ou bas",
            body_html=(
                "<p>Un <strong>DHEA-S élevé</strong> ou un <strong>DHEA-S bas</strong> peut "
                "indiquer diverses affections cliniques. L'interprétation doit toujours être "
                "associée aux résultats cliniques. Les principales causes sont :</p>"
                "<p><strong>Causes d'un DHEA-S élevé :</strong></p>"
                "<ul>"
                "<li><strong>Syndrome des ovaires polykystiques (SOPK) :</strong> La cause la "
                "plus fréquente d'élévation de la DHEA-S chez la femme ; le SOPK entraîne un "
                "hyperandrogénisme, des règles irrégulières et des ovaires polykystiques.</li>"
                "<li><strong>Hyperplasie congénitale des surrénales (HCS) :</strong> Des anomalies "
                "génétiques des enzymes de synthèse des stéroïdes surrénaliens provoquent une "
                "surproduction de DHEA-S.</li>"
                "<li><strong>Tumeurs surrénaliennes :</strong> Les adénomes ou carcinomes "
                "surrénaliens peuvent élever nettement la DHEA-S ; des valeurs très élevées "
                "constituent un signal d'alerte de malignité.</li>"
                "<li><strong>Syndrome de Cushing :</strong> Les formes ACTH-dépendantes peuvent "
                "stimuler la production excessive d'androgènes surrénaliens.</li>"
                "</ul>"
                "<p><strong>Causes d'un DHEA-S bas :</strong></p>"
                "<ul>"
                "<li><strong>Insuffisance surrénalienne (maladie d'Addison) :</strong> Une "
                "production hormonale insuffisante par les glandes surrénales entraîne un taux "
                "de DHEA-S bas.</li>"
                "<li><strong>Hypopituitarisme :</strong> La diminution de la sécrétion d'ACTH par "
                "l'hypophyse supprime la fonction surrénalienne et abaisse la DHEA-S.</li>"
                "<li><strong>Adrénopause (déclin lié à l'âge) :</strong> La production de DHEA-S "
                "diminue physiologiquement dans le cadre du vieillissement normal.</li>"
                "<li><strong>Utilisation prolongée de corticostéroïdes :</strong> Les stéroïdes "
                "exogènes suppriment l'axe hypothalamo-hypophyso-surrénalien et peuvent abaisser "
                "la DHEA-S.</li>"
                "</ul>"
                "<p>Pour le diagnostic, la DHEA-S est évaluée parallèlement aux autres résultats "
                "de <strong>tests hormonaux surrénaliens</strong> (cortisol, ACTH, "
                "17-OH progestérone) et à l'imagerie si nécessaire. Un résultat isolé de DHEA-S "
                "n'est pas diagnostique.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si vous êtes une femme et que vous présentez une pilosité excessive du visage "
                "ou du corps, une acné sévère, une chute de cheveux, des règles irrégulières ou "
                "une infertilité, consultez un endocrinologue ou un gynécologue et demandez un "
                "<strong>test de DHEA-S</strong>. Ces symptômes peuvent indiquer un SOPK ou un "
                "hyperandrogénisme d'origine surrénalienne.</p>"
                "<p>Une fatigue chronique, une faiblesse musculaire, une perte de poids, des "
                "vertiges ou une pression artérielle basse peuvent signaler un <strong>DHEA-S "
                "bas</strong> et une éventuelle insuffisance surrénalienne. Si vous remarquez "
                "également un assombrissement de la peau, consultez rapidement, car la maladie "
                "d'Addison non traitée peut mettre la vie en danger.</p>"
                "<p>N'oubliez pas : les résultats de DHEA-S ne doivent pas être évalués "
                "isolément. Ils doivent être considérés avec le tableau clinique, d'autres tests "
                "hormonaux et l'imagerie si nécessaire. Si vos résultats sont hors des valeurs "
                "normales, partagez-les avec un spécialiste — n'essayez pas de vous traiter "
                "vous-même sur la base de recherches sur internet.</p>"
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
            heading="Esame del DHEA-S: cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test del DHEA-S</strong> (deidroepiandrosterone solfato) misura il "
                "livello ematico di DHEA-S, la forma solfatata del DHEA — il più abbondante "
                "<strong>ormone surrenalico</strong> prodotto dalle ghiandole surrenali. Il DHEA-S "
                "è un precursore ormonale che l'organismo può convertire in ormoni sessuali come "
                "testosterone ed estrogeni, ed è considerato uno dei marcatori più affidabili della "
                "funzione surrenalica.</p>"
                "<p>Un <strong>esame del sangue del DHEA solfato</strong> viene comunemente "
                "richiesto quando si indagano sintomi di <strong>DHEA-S alto</strong> — come "
                "eccesso di peluria (irsutismo), acne severa o ciclo irregolare nelle donne — "
                "oppure quando si valutano sintomi di <strong>DHEA-S basso</strong> come "
                "stanchezza cronica e debolezza muscolare. Svolge un ruolo critico nella diagnosi "
                "di condizioni quali la sindrome dell'ovaio policistico (PCOS), l'iperplasia "
                "surrenalica congenita (CAH) e i tumori surrenalici.</p>"
                "<p>I livelli di DHEA-S diminuiscono naturalmente con l'età, un processo noto come "
                "adrenopausa. I valori massimi si osservano tipicamente intorno ai 20 anni, seguiti "
                "da un calo costante di circa il 10–20 % per decennio. Per questo motivo i "
                "<strong>valori normali di DHEA-S</strong> devono sempre essere interpretati in "
                "relazione all'età e al sesso.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di DHEA-S (per età e sesso)",
            body_html=(
                "<p>I <strong>valori normali di DHEA-S</strong> variano considerevolmente in base "
                "all'età e al sesso. La tabella seguente riassume i valori di riferimento "
                "comunemente accettati per gli adulti. I risultati vengono generalmente espressi "
                "in microgrammi per decilitro (µg/dL); alcuni laboratori utilizzano µmol/L "
                "(1 µg/dL ≈ 0,027 µmol/L).</p>"
                "<p>La tabella mostra i <strong>livelli di DHEA solfato</strong> per uomini e "
                "donne suddivisi per fascia d'età:</p>"
                + _DHEAS_TABLE_IT +
                "<p>I <strong>livelli di DHEA solfato</strong> raggiungono il picco tra i 20 e "
                "i 30 anni e poi diminuiscono di circa il 10–20 % per decennio. Oltre i 70 anni "
                "i valori possono scendere al 20–30 % del picco. Confronta sempre il tuo "
                "risultato con l'intervallo di riferimento specifico per età e sesso riportato "
                "nel tuo referto di laboratorio.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di DHEA-S alto o basso",
            body_html=(
                "<p>Un <strong>DHEA-S alto</strong> o un <strong>DHEA-S basso</strong> può "
                "indicare diverse condizioni cliniche. L'interpretazione deve sempre essere "
                "associata ai riscontri clinici. Le principali cause includono:</p>"
                "<p><strong>Cause di DHEA-S alto:</strong></p>"
                "<ul>"
                "<li><strong>Sindrome dell'ovaio policistico (PCOS):</strong> La causa più "
                "comune di DHEA-S elevato nelle donne; la PCOS provoca iperandrogenismo, ciclo "
                "irregolare e ovaie policistiche.</li>"
                "<li><strong>Iperplasia surrenalica congenita (CAH):</strong> Difetti genetici "
                "negli enzimi di sintesi degli steroidi surrenalici causano una sovrapproduzione "
                "di DHEA-S.</li>"
                "<li><strong>Tumori surrenalici:</strong> Adenomi o carcinomi surrenalici possono "
                "elevare marcatamente il DHEA-S; valori molto alti rappresentano un campanello "
                "d'allarme per la malignità.</li>"
                "<li><strong>Sindrome di Cushing:</strong> Le forme ACTH-dipendenti possono "
                "stimolare la produzione eccessiva di androgeni surrenalici.</li>"
                "</ul>"
                "<p><strong>Cause di DHEA-S basso:</strong></p>"
                "<ul>"
                "<li><strong>Insufficienza surrenalica (malattia di Addison):</strong> Una "
                "produzione ormonale inadeguata da parte delle ghiandole surrenali porta a livelli "
                "bassi di DHEA-S.</li>"
                "<li><strong>Ipopituitarismo:</strong> La ridotta produzione di ACTH da parte "
                "dell'ipofisi sopprime la funzione surrenalica e abbassa il DHEA-S.</li>"
                "<li><strong>Adrenopausa (declino legato all'età):</strong> La produzione di "
                "DHEA-S diminuisce fisiologicamente come parte del normale invecchiamento.</li>"
                "<li><strong>Uso prolungato di corticosteroidi:</strong> Gli steroidi esogeni "
                "sopprimono l'asse ipotalamo-ipofisi-surrene e possono ridurre il DHEA-S.</li>"
                "</ul>"
                "<p>Per la diagnosi, il DHEA-S viene valutato insieme ad altri risultati di "
                "<strong>test ormonali surrenalici</strong> (cortisolo, ACTH, "
                "17-OH progesterone) e all'imaging quando necessario. Un singolo risultato di "
                "DHEA-S non è diagnostico di per sé.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se sei una donna e presenti eccesso di peluria sul viso o sul corpo, acne "
                "severa, perdita di capelli, ciclo irregolare o infertilità, consulta un "
                "endocrinologo o un ginecologo e richiedi un <strong>esame del DHEA-S</strong>. "
                "Questi sintomi possono indicare PCOS o iperandrogenismo di origine "
                "surrenalica.</p>"
                "<p>Stanchezza cronica, debolezza muscolare, perdita di peso, capogiri o "
                "pressione sanguigna bassa possono segnalare un <strong>DHEA-S basso</strong> e "
                "una possibile insufficienza surrenalica. Se noti anche un inscurimento della "
                "pelle, rivolgiti prontamente a un medico perché la malattia di Addison non "
                "trattata può essere pericolosa per la vita.</p>"
                "<p>Ricorda: i risultati del DHEA-S non devono essere valutati isolatamente. "
                "Devono essere considerati insieme al quadro clinico, ad altri test ormonali e "
                "all'imaging se necessario. Se i tuoi risultati sono fuori dai valori normali, "
                "condividili con uno specialista — non tentare l'automedicazione basandoti "
                "esclusivamente su ricerche su internet.</p>"
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
            heading="בדיקת DHEA-S בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת DHEA-S</strong> (דהידרואפיאנדרוסטרון סולפט) מודדת את רמת "
                "ה-DHEA-S בדם — הצורה הסולפטית של DHEA, <strong>הורמון האדרנל</strong> השכיח "
                "ביותר שמיוצר בבלוטות יותרת הכליה. DHEA-S משמש כמבשר (פרה-קורסור) שהגוף יכול "
                "להמיר להורמוני מין כמו טסטוסטרון ואסטרוגן, והוא נחשב לאחד הסמנים האמינים "
                "ביותר לתפקוד האדרנל.</p>"
                "<p><strong>בדיקת דם של DHEA סולפט</strong> נדרשת בדרך כלל כאשר חוקרים תסמינים "
                "של <strong>DHEA-S גבוה</strong> — כמו שעירות יתר (הירסוטיזם), אקנה חמורה או "
                "מחזורים לא סדירים אצל נשים — או כאשר מעריכים תסמינים של <strong>DHEA-S "
                "נמוך</strong> כמו עייפות כרונית וחולשת שרירים. הבדיקה ממלאת תפקיד קריטי "
                "באבחון מצבים כמו תסמונת השחלות הפוליציסטיות (PCOS), היפרפלזיה אדרנלית "
                "מולדת (CAH) וגידולים באדרנל.</p>"
                "<p>רמות DHEA-S יורדות באופן טבעי עם הגיל, תהליך הידוע בשם אדרנופאוזה. ערכי "
                "שיא מופיעים בדרך כלל בשנות ה-20, ולאחר מכן חלה ירידה הדרגתית של כ-10–20% "
                "בכל עשור. לכן <strong>טווח הנורמה של DHEA-S</strong> חייב תמיד להתפרש בהקשר "
                "של גיל ומין.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של DHEA-S (לפי גיל ומין)",
            body_html=(
                "<p><strong>טווח הנורמה של DHEA-S</strong> משתנה באופן ניכר לפי גיל ומין. "
                "הטבלה שלהלן מסכמת את ערכי הייחוס המקובלים עבור מבוגרים. התוצאות מדווחות "
                "בדרך כלל במיקרוגרם לדציליטר (µg/dL); חלק מהמעבדות משתמשות ב-µmol/L "
                "(1 µg/dL ≈ 0.027 µmol/L).</p>"
                "<p>הטבלה הבאה מציגה את <strong>רמות DHEA סולפט</strong> לגברים ולנשים לפי "
                "קבוצת גיל:</p>"
                + _DHEAS_TABLE_HE +
                "<p><strong>רמות DHEA סולפט</strong> מגיעות לשיאן בין גיל 20 ל-30 ולאחר מכן "
                "יורדות בכ-10–20% בכל עשור. מעל גיל 70 הערכים עלולים לרדת ל-20–30% מהשיא. "
                "השוו תמיד את התוצאה שלכם לטווח הייחוס הספציפי לגיל ולמין המופיע בדוח "
                "המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים ל-DHEA-S גבוה או נמוך",
            body_html=(
                "<p><strong>DHEA-S גבוה</strong> או <strong>DHEA-S נמוך</strong> עשוי להצביע "
                "על מגוון מצבים קליניים. הפרשנות צריכה תמיד להתבצע בשילוב עם ממצאים קליניים. "
                "הגורמים העיקריים כוללים:</p>"
                "<p><strong>גורמים ל-DHEA-S גבוה:</strong></p>"
                "<ul>"
                "<li><strong>תסמונת השחלות הפוליציסטיות (PCOS):</strong> הגורם השכיח ביותר "
                "ל-DHEA-S מוגבה בנשים; PCOS מוביל להיפראנדרוגניזם, מחזורים לא סדירים "
                "ושחלות פוליציסטיות.</li>"
                "<li><strong>היפרפלזיה אדרנלית מולדת (CAH):</strong> פגמים גנטיים באנזימי "
                "סינתזת סטרואידים אדרנליים גורמים לייצור יתר של DHEA-S.</li>"
                "<li><strong>גידולים באדרנל:</strong> אדנומות או קרצינומות של האדרנל עלולים "
                "להעלות את ה-DHEA-S באופן ניכר; ערכים גבוהים מאוד מהווים דגל אדום "
                "לממאירות.</li>"
                "<li><strong>תסמונת קושינג:</strong> צורות תלויות ACTH עלולות לגרום לייצור "
                "עודף של אנדרוגנים אדרנליים.</li>"
                "</ul>"
                "<p><strong>גורמים ל-DHEA-S נמוך:</strong></p>"
                "<ul>"
                "<li><strong>אי-ספיקת אדרנל (מחלת אדיסון):</strong> ייצור הורמונלי לא "
                "מספק של בלוטות יותרת הכליה מוביל ל-DHEA-S נמוך.</li>"
                "<li><strong>היפופיטואיטריזם:</strong> ירידה בהפרשת ACTH מבלוטת יותרת "
                "המוח מדכאת את תפקוד האדרנל ומורידה את ה-DHEA-S.</li>"
                "<li><strong>אדרנופאוזה (ירידה הקשורה לגיל):</strong> ייצור DHEA-S יורד "
                "באופן פיזיולוגי כחלק מההזדקנות הטבעית.</li>"
                "<li><strong>שימוש ממושך בקורטיקוסטרואידים:</strong> סטרואידים חיצוניים "
                "מדכאים את ציר ההיפותלמוס-היפופיזה-אדרנל ועלולים להוריד את ה-DHEA-S.</li>"
                "</ul>"
                "<p>לצורך אבחון, DHEA-S מוערך לצד תוצאות <strong>בדיקות הורמוני "
                "אדרנל</strong> אחרות (קורטיזול, ACTH,‏ 17-OH פרוגסטרון) ובדיקות הדמיה "
                "בעת הצורך. תוצאת DHEA-S בודדת אינה אבחנתית כשלעצמה.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם את אישה החווה שעירות יתר בפנים או בגוף, אקנה חמורה, נשירת שיער, "
                "מחזורים לא סדירים או אי-פוריות, פני לאנדוקרינולוג או גינקולוג ובקשי "
                "<strong>בדיקת DHEA-S</strong>. תסמינים אלה עשויים להצביע על PCOS או "
                "היפראנדרוגניזם ממקור אדרנלי.</p>"
                "<p>עייפות כרונית, חולשת שרירים, ירידה במשקל, סחרחורת או לחץ דם נמוך עלולים "
                "לרמז על <strong>DHEA-S נמוך</strong> ועל אי-ספיקת אדרנל אפשרית. אם אתם "
                "מבחינים גם בהכהיית עור, פנו מיד להערכה רפואית כי מחלת אדיסון ללא טיפול "
                "עלולה לסכן חיים.</p>"
                "<p>זכרו: תוצאות DHEA-S לא צריכות להיבדק בבידוד. יש לשקול אותן יחד עם "
                "התמונה הקלינית, בדיקות הורמונליות אחרות והדמיה לפי הצורך. אם התוצאות שלכם "
                "חורגות מהנורמה, שתפו אותן עם מומחה — אל תנסו טיפול עצמי על סמך חיפוש "
                "באינטרנט בלבד.</p>"
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
            heading="DHEA-S ब्लड टेस्ट: आपकी रिपोर्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>DHEA-S टेस्ट</strong> (डीहाइड्रोएपिएंड्रोस्टेरोन सल्फेट) रक्त में "
                "DHEA-S के स्तर को मापता है — यह DHEA का सल्फेटेड रूप है जो एड्रीनल ग्रंथियों "
                "द्वारा उत्पादित सबसे प्रचुर <strong>एड्रीनल हार्मोन</strong> है। DHEA-S एक "
                "प्रीकर्सर हार्मोन है जिसे शरीर टेस्टोस्टेरोन और एस्ट्रोजन जैसे सेक्स "
                "हार्मोन में बदल सकता है, और इसे एड्रीनल फंक्शन का सबसे विश्वसनीय मार्कर "
                "माना जाता है।</p>"
                "<p><strong>DHEA सल्फेट ब्लड टेस्ट</strong> आमतौर पर तब किया जाता है जब "
                "<strong>हाई DHEA-S</strong> के लक्षणों की जांच होती है — जैसे अत्यधिक "
                "बॉडी हेयर (हिर्सुटिज़्म), गंभीर एक्ने या महिलाओं में अनियमित पीरियड्स — "
                "या जब <strong>लो DHEA-S</strong> के लक्षण जैसे क्रोनिक थकान और मांसपेशियों "
                "की कमज़ोरी का मूल्यांकन किया जाता है। यह पॉलीसिस्टिक ओवरी सिंड्रोम (PCOS), "
                "कंजेनिटल एड्रीनल हाइपरप्लेसिया (CAH) और एड्रीनल ट्यूमर जैसी स्थितियों के "
                "निदान में महत्वपूर्ण भूमिका निभाता है।</p>"
                "<p>DHEA-S का स्तर उम्र के साथ स्वाभाविक रूप से घटता है; इस प्रक्रिया को "
                "एड्रीनोपॉज़ कहते हैं। शिखर मान आम तौर पर 20 के दशक में होते हैं और उसके बाद "
                "हर दशक में लगभग 10–20% की गिरावट होती है। इसलिए <strong>DHEA-S नॉर्मल "
                "रेंज</strong> की व्याख्या हमेशा उम्र और लिंग के संदर्भ में की जानी चाहिए।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="DHEA-S के नॉर्मल वैल्यू (उम्र और लिंग के अनुसार)",
            body_html=(
                "<p><strong>DHEA-S नॉर्मल रेंज</strong> उम्र और लिंग के अनुसार काफ़ी भिन्न "
                "होती है। नीचे दी गई तालिका वयस्कों के लिए आम तौर पर स्वीकृत रेफ़रेंस "
                "वैल्यू को सारांशित करती है। रिज़ल्ट आमतौर पर माइक्रोग्राम प्रति डेसीलीटर "
                "(µg/dL) में रिपोर्ट किए जाते हैं; कुछ लैब µmol/L का उपयोग करती हैं "
                "(1 µg/dL ≈ 0.027 µmol/L)।</p>"
                "<p>निम्न तालिका आयु वर्ग के अनुसार पुरुष और महिला <strong>DHEA सल्फेट "
                "लेवल</strong> दर्शाती है:</p>"
                + _DHEAS_TABLE_HI +
                "<p><strong>DHEA सल्फेट लेवल</strong> 20 से 30 वर्ष की आयु में अपने चरम पर "
                "होते हैं और फिर हर दशक में लगभग 10–20% कम होते हैं। 70+ वर्ष की आयु में "
                "वैल्यू अपने शिखर की लगभग 20–30% तक गिर सकती है। अपने रिज़ल्ट की तुलना "
                "हमेशा अपनी लैब रिपोर्ट पर दी गई उम्र- और लिंग-विशिष्ट रेफ़रेंस रेंज "
                "से करें।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई या लो DHEA-S के कारण",
            body_html=(
                "<p><strong>हाई DHEA-S</strong> या <strong>लो DHEA-S</strong> कई अलग-अलग "
                "क्लिनिकल स्थितियों का संकेत हो सकता है। व्याख्या हमेशा क्लिनिकल निष्कर्षों "
                "के साथ मिलकर की जानी चाहिए। प्रमुख कारणों में शामिल हैं:</p>"
                "<p><strong>हाई DHEA-S के कारण:</strong></p>"
                "<ul>"
                "<li><strong>पॉलीसिस्टिक ओवरी सिंड्रोम (PCOS):</strong> महिलाओं में ऊंचे "
                "DHEA-S का सबसे आम कारण; PCOS हाइपरएंड्रोजेनिज़्म, अनियमित पीरियड्स और "
                "पॉलीसिस्टिक ओवरीज़ का कारण बनता है।</li>"
                "<li><strong>कंजेनिटल एड्रीनल हाइपरप्लेसिया (CAH):</strong> एड्रीनल स्टेरॉइड "
                "सिंथेसिस एंज़ाइम में जेनेटिक दोषों के कारण DHEA-S का अत्यधिक उत्पादन "
                "होता है।</li>"
                "<li><strong>एड्रीनल ट्यूमर:</strong> एड्रीनल एडेनोमा या कार्सिनोमा "
                "DHEA-S को उल्लेखनीय रूप से बढ़ा सकते हैं; बहुत ऊंचे मान मैलिग्नेंसी का "
                "रेड फ्लैग हैं।</li>"
                "<li><strong>कुशिंग सिंड्रोम:</strong> ACTH-निर्भर रूप एड्रीनल एंड्रोजन के "
                "अत्यधिक उत्पादन को बढ़ावा दे सकते हैं।</li>"
                "</ul>"
                "<p><strong>लो DHEA-S के कारण:</strong></p>"
                "<ul>"
                "<li><strong>एड्रीनल इन्सफ़िशिएंसी (एडिसन रोग):</strong> एड्रीनल ग्रंथियों "
                "द्वारा अपर्याप्त हार्मोन उत्पादन DHEA-S को कम करता है।</li>"
                "<li><strong>हाइपोपिट्यूटेरिज़्म:</strong> पिट्यूटरी से कम ACTH आउटपुट "
                "एड्रीनल फंक्शन को दबाता है और DHEA-S को कम करता है।</li>"
                "<li><strong>एड्रीनोपॉज़ (उम्र से संबंधित गिरावट):</strong> सामान्य उम्र "
                "बढ़ने के हिस्से के रूप में DHEA-S उत्पादन शारीरिक रूप से कम हो जाता है।</li>"
                "<li><strong>लंबे समय तक कॉर्टिकोस्टेरॉइड का उपयोग:</strong> बाहरी स्टेरॉइड "
                "हाइपोथैलेमिक-पिट्यूटरी-एड्रीनल अक्ष को दबाते हैं और DHEA-S कम कर "
                "सकते हैं।</li>"
                "</ul>"
                "<p>निदान के लिए DHEA-S का मूल्यांकन अन्य <strong>एड्रीनल हार्मोन "
                "टेस्ट</strong> रिज़ल्ट (कोर्टिसोल, ACTH, 17-OH प्रोजेस्टेरोन) और ज़रूरत "
                "पड़ने पर इमेजिंग के साथ किया जाता है। अकेला DHEA-S रिज़ल्ट डायग्नोस्टिक "
                "नहीं होता।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आप एक महिला हैं और चेहरे या शरीर पर अत्यधिक बाल, गंभीर एक्ने, "
                "बालों का झड़ना, अनियमित पीरियड्स या इनफ़र्टिलिटी का अनुभव कर रही हैं, तो "
                "एंडोक्रिनोलॉजिस्ट या गाइनेकोलॉजिस्ट से मिलें और <strong>DHEA-S "
                "टेस्ट</strong> कराएँ। ये लक्षण PCOS या एड्रीनल-मूल के हाइपरएंड्रोजेनिज़्म "
                "का संकेत हो सकते हैं।</p>"
                "<p>क्रोनिक थकान, मांसपेशियों की कमज़ोरी, वज़न घटना, चक्कर आना या लो ब्लड "
                "प्रेशर <strong>लो DHEA-S</strong> और संभावित एड्रीनल इन्सफ़िशिएंसी का संकेत "
                "हो सकता है। अगर आपको त्वचा का रंग गहरा होते हुए भी दिखे, तो तुरंत चिकित्सा "
                "मूल्यांकन कराएँ क्योंकि अनुपचारित एडिसन रोग जानलेवा हो सकता है।</p>"
                "<p>याद रखें: DHEA-S रिज़ल्ट को अकेले नहीं आंकना चाहिए। उन्हें क्लिनिकल "
                "तस्वीर, अन्य हार्मोन टेस्ट और ज़रूरत अनुसार इमेजिंग के साथ मिलकर देखना "
                "चाहिए। अगर आपके रिज़ल्ट नॉर्मल रेंज से बाहर हैं तो किसी विशेषज्ञ से साझा "
                "करें — केवल इंटरनेट रिसर्च पर आधारित स्वयं उपचार का प्रयास न करें।</p>"
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
            heading="تحليل DHEA-S في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>يقيس <strong>تحليل DHEA-S</strong> (كبريتات ديهيدرو إيبي أندروستيرون) "
                "مستوى DHEA-S في الدم — الشكل الكبريتي من DHEA، وهو أكثر <strong>هرمون "
                "كظري</strong> وفرة تنتجه الغدتان الكظريتان. يعمل DHEA-S بوصفه طليعة هرمونية "
                "يمكن للجسم تحويلها إلى هرمونات جنسية مثل التستوستيرون والإستروجين، ويُعتبر "
                "من أكثر المؤشرات موثوقية لوظيفة الغدة الكظرية.</p>"
                "<p>يُطلب <strong>تحليل دم كبريتات DHEA</strong> عادةً عند استقصاء أعراض "
                "<strong>DHEA-S المرتفع</strong> — مثل فرط الشعر (الشعرانية) أو حب الشباب "
                "الشديد أو عدم انتظام الدورة الشهرية عند النساء — أو عند تقييم أعراض "
                "<strong>DHEA-S المنخفض</strong> كالإرهاق المزمن وضعف العضلات. يلعب دوراً "
                "محورياً في تشخيص حالات مثل متلازمة المبيض متعدد الكيسات (PCOS)، وفرط تنسج "
                "الكظر الخلقي (CAH)، وأورام الغدة الكظرية.</p>"
                "<p>تنخفض مستويات DHEA-S بشكل طبيعي مع التقدم في العمر، في عملية تُعرف "
                "بانقطاع الأدرينالين (أدرينوبوز). تظهر القيم القصوى عادةً في العشرينيات، "
                "يليها انخفاض مطرد بنحو 10–20% في كل عقد. لذلك يجب تفسير <strong>النطاق "
                "الطبيعي لـ DHEA-S</strong> دائماً في سياق العمر والجنس.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية لـ DHEA-S (حسب العمر والجنس)",
            body_html=(
                "<p>يختلف <strong>النطاق الطبيعي لـ DHEA-S</strong> بشكل كبير حسب العمر "
                "والجنس. يلخّص الجدول أدناه القيم المرجعية المقبولة عموماً للبالغين. تُعبَّر "
                "النتائج عادةً بالميكروغرام لكل ديسيلتر (µg/dL)؛ بعض المختبرات تستخدم "
                "µmol/L‏ (1 µg/dL ≈ 0.027 µmol/L).</p>"
                "<p>يُظهر الجدول التالي <strong>مستويات كبريتات DHEA</strong> للذكور والإناث "
                "حسب الفئة العمرية:</p>"
                + _DHEAS_TABLE_AR +
                "<p>تصل <strong>مستويات كبريتات DHEA</strong> إلى ذروتها بين سن 20 و30 "
                "ثم تنخفض بنحو 10–20% في كل عقد. بعد سن 70 قد تهبط القيم إلى نحو 20–30% "
                "من ذروتها. قارنوا دائماً نتيجتكم بالنطاق المرجعي المحدد حسب العمر والجنس "
                "على تقرير المختبر الخاص بكم.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع أو انخفاض DHEA-S",
            body_html=(
                "<p>قد يشير <strong>DHEA-S المرتفع</strong> أو <strong>DHEA-S المنخفض</strong> "
                "إلى مجموعة متنوعة من الحالات السريرية. يجب دائماً الجمع بين التفسير "
                "والنتائج السريرية. تشمل الأسباب الرئيسية:</p>"
                "<p><strong>أسباب ارتفاع DHEA-S:</strong></p>"
                "<ul>"
                "<li><strong>متلازمة المبيض متعدد الكيسات (PCOS):</strong> السبب الأكثر "
                "شيوعاً لارتفاع DHEA-S عند النساء؛ يؤدي إلى فرط الأندروجين وعدم انتظام "
                "الدورة ومبايض متعددة الكيسات.</li>"
                "<li><strong>فرط تنسج الكظر الخلقي (CAH):</strong> عيوب وراثية في إنزيمات "
                "تصنيع الستيرويدات الكظرية تسبب إفراطاً في إنتاج DHEA-S.</li>"
                "<li><strong>أورام الغدة الكظرية:</strong> الأورام الغدية أو السرطانية "
                "الكظرية قد ترفع DHEA-S بشكل ملحوظ؛ القيم المرتفعة جداً علامة تحذيرية "
                "على وجود ورم خبيث.</li>"
                "<li><strong>متلازمة كوشينغ:</strong> الأشكال المعتمدة على ACTH قد تحفّز "
                "إنتاج مفرط للأندروجينات الكظرية.</li>"
                "</ul>"
                "<p><strong>أسباب انخفاض DHEA-S:</strong></p>"
                "<ul>"
                "<li><strong>قصور الغدة الكظرية (مرض أديسون):</strong> عدم كفاية إنتاج "
                "الهرمونات من الغدد الكظرية يؤدي إلى انخفاض DHEA-S.</li>"
                "<li><strong>قصور الغدة النخامية:</strong> انخفاض إفراز ACTH من الغدة "
                "النخامية يثبط وظيفة الكظر ويخفض DHEA-S.</li>"
                "<li><strong>أدرينوبوز (تراجع مرتبط بالعمر):</strong> ينخفض إنتاج DHEA-S "
                "بشكل فيزيولوجي كجزء من الشيخوخة الطبيعية.</li>"
                "<li><strong>الاستخدام المطوّل للكورتيكوستيرويدات:</strong> الستيرويدات "
                "الخارجية تثبط محور الوطاء-النخامية-الكظر وقد تخفض DHEA-S.</li>"
                "</ul>"
                "<p>لأغراض التشخيص يُقيَّم DHEA-S إلى جانب نتائج <strong>اختبارات الهرمونات "
                "الكظرية</strong> الأخرى (الكورتيزول، ACTH،‏ 17-OH بروجسترون) والتصوير عند "
                "الحاجة. نتيجة DHEA-S وحدها ليست تشخيصية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كنتِ امرأة وتعانين من شعر زائد في الوجه أو الجسم أو حب شباب شديد "
                "أو تساقط الشعر أو عدم انتظام الدورة الشهرية أو العقم، راجعي طبيب غدد "
                "صماء أو طبيب نسائية واطلبي إجراء <strong>تحليل DHEA-S</strong>. قد تشير هذه "
                "الأعراض إلى متلازمة المبيض متعدد الكيسات أو فرط الأندروجين من مصدر "
                "كظري.</p>"
                "<p>الإرهاق المزمن وضعف العضلات وفقدان الوزن والدوخة أو انخفاض ضغط الدم "
                "قد تكون إشارات على <strong>DHEA-S منخفض</strong> وقصور كظري محتمل. إذا "
                "لاحظتم أيضاً اسمرار الجلد، اطلبوا تقييماً طبياً فوراً لأن مرض أديسون غير "
                "المعالج قد يهدد الحياة.</p>"
                "<p>تذكّروا: لا ينبغي تقييم نتائج DHEA-S بمعزل عن السياق. يجب أخذها بعين "
                "الاعتبار مع الصورة السريرية واختبارات هرمونية أخرى والتصوير عند الحاجة. إذا "
                "كانت نتائجكم خارج النطاق الطبيعي، شاركوها مع أخصائي — ولا تحاولوا العلاج "
                "الذاتي بناءً على بحث الإنترنت فقط.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_dheas_sections_by_lang() -> dict:
    """Returns sections dict for DHEA-S article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_dheas_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for DHEA-S article (all 9 languages, 3 Q&A each)."""
    return {
        "tr": [
            {"question": "DHEA-S testi nedir?",
             "answer": "DHEA-S testi, böbreküstü bezlerinin ürettiği dehidroepiandrosteron sülfat hormonunun kandaki düzeyini ölçen bir adrenal hormon testidir. Adrenal bez fonksiyonunun değerlendirilmesinde, PKOS ve adrenal tümör gibi durumların tanısında kullanılır."},
            {"question": "DHEA-S normal değeri kaçtır?",
             "answer": "DHEA-S normal değerleri yaşa ve cinsiyete göre değişir. Örneğin 20–29 yaş arası erkeklerde 280–640 µg/dL, kadınlarda 65–380 µg/dL kabul edilir. Değerler 30'lu yaşlardan itibaren her on yılda yaklaşık %10–20 düşer."},
            {"question": "DHEA-S yüksekliği ne anlama gelir?",
             "answer": "Yüksek DHEA-S; polikistik over sendromu (PKOS), konjenital adrenal hiperplazi, adrenal tümörler veya Cushing sendromu gibi durumlara işaret edebilir. Doğru tanı için klinik bulgular, diğer hormon testleri ve görüntüleme ile birlikte değerlendirilmelidir."},
        ],
        "en": [
            {"question": "What is a DHEA-S test?",
             "answer": "A DHEA-S test is an adrenal hormone test that measures the blood level of dehydroepiandrosterone sulfate, the most abundant hormone produced by the adrenal glands. It is used to evaluate adrenal function and help diagnose conditions such as PCOS and adrenal tumors."},
            {"question": "What is the normal DHEA-S range?",
             "answer": "The DHEA-S normal range varies by age and sex. For example, in men aged 20–29 it is typically 280–640 µg/dL, and in women of the same age 65–380 µg/dL. Levels decline by roughly 10–20 % per decade from the 30s onward."},
            {"question": "What does high DHEA-S mean?",
             "answer": "High DHEA-S may indicate polycystic ovary syndrome (PCOS), congenital adrenal hyperplasia, adrenal tumors, or Cushing syndrome. Accurate diagnosis requires evaluation alongside clinical findings, other hormone tests, and imaging when needed."},
        ],
        "es": [
            {"question": "¿Qué es el análisis de DHEA-S?",
             "answer": "El análisis de DHEA-S es una prueba hormonal suprarrenal que mide el nivel sanguíneo de sulfato de dehidroepiandrosterona, la hormona más abundante producida por las glándulas suprarrenales. Se utiliza para evaluar la función suprarrenal y ayudar a diagnosticar afecciones como el SOP y los tumores suprarrenales."},
            {"question": "¿Cuál es el rango normal de DHEA-S?",
             "answer": "El rango normal de DHEA-S varía según la edad y el sexo. Por ejemplo, en hombres de 20 a 29 años suele ser de 280–640 µg/dL, y en mujeres de la misma edad de 65–380 µg/dL. Los niveles disminuyen aproximadamente un 10–20 % por década a partir de los 30 años."},
            {"question": "¿Qué significa DHEA-S alta?",
             "answer": "Un DHEA-S alto puede indicar síndrome de ovario poliquístico (SOP), hiperplasia suprarrenal congénita, tumores suprarrenales o síndrome de Cushing. Un diagnóstico preciso requiere evaluación junto con hallazgos clínicos, otras pruebas hormonales e imagen cuando sea necesario."},
        ],
        "de": [
            {"question": "Was ist ein DHEA-S-Test?",
             "answer": "Ein DHEA-S-Test ist ein Nebennierenhormon-Test, der den Blutspiegel von Dehydroepiandrosteron-Sulfat misst — dem am häufigsten vorkommenden Hormon der Nebennieren. Er dient der Beurteilung der Nebennierenfunktion und der Diagnose von Erkrankungen wie PCOS und Nebennierentumoren."},
            {"question": "Was sind die DHEA-S-Normalwerte?",
             "answer": "Der DHEA-S-Normalbereich variiert nach Alter und Geschlecht. Bei Männern im Alter von 20–29 Jahren liegt er typischerweise bei 280–640 µg/dL, bei Frauen gleichen Alters bei 65–380 µg/dL. Die Werte sinken ab dem 30. Lebensjahr pro Dekade um etwa 10–20 %."},
            {"question": "Was bedeutet ein erhöhter DHEA-S-Wert?",
             "answer": "Ein hohes DHEA-S kann auf ein polyzystisches Ovarialsyndrom (PCOS), eine kongenitale Nebennierenhyperplasie, Nebennierentumoren oder ein Cushing-Syndrom hinweisen. Eine genaue Diagnose erfordert die Bewertung zusammen mit klinischen Befunden, anderen Hormontests und ggf. Bildgebung."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'un test de DHEA-S ?",
             "answer": "Le test de DHEA-S est un test hormonal surrénalien qui mesure le taux sanguin de sulfate de déhydroépiandrostérone, l'hormone la plus abondante produite par les glandes surrénales. Il est utilisé pour évaluer la fonction surrénalienne et aider au diagnostic d'affections telles que le SOPK et les tumeurs surrénaliennes."},
            {"question": "Quelles sont les valeurs normales de DHEA-S ?",
             "answer": "Les valeurs normales de DHEA-S varient selon l'âge et le sexe. Par exemple, chez les hommes de 20 à 29 ans, elles se situent généralement entre 280 et 640 µg/dL, et chez les femmes du même âge entre 65 et 380 µg/dL. Les taux diminuent d'environ 10 à 20 % par décennie à partir de 30 ans."},
            {"question": "Que signifie un DHEA-S élevé ?",
             "answer": "Un DHEA-S élevé peut indiquer un syndrome des ovaires polykystiques (SOPK), une hyperplasie congénitale des surrénales, des tumeurs surrénaliennes ou un syndrome de Cushing. Un diagnostic précis nécessite une évaluation combinée aux résultats cliniques, à d'autres tests hormonaux et à l'imagerie si nécessaire."},
        ],
        "it": [
            {"question": "Cos'è il test del DHEA-S?",
             "answer": "Il test del DHEA-S è un esame ormonale surrenalico che misura il livello ematico di deidroepiandrosterone solfato, l'ormone più abbondante prodotto dalle ghiandole surrenali. Viene utilizzato per valutare la funzione surrenalica e contribuire alla diagnosi di condizioni come la PCOS e i tumori surrenalici."},
            {"question": "Quali sono i valori normali di DHEA-S?",
             "answer": "I valori normali di DHEA-S variano in base all'età e al sesso. Ad esempio, negli uomini tra i 20 e i 29 anni il range è tipicamente 280–640 µg/dL, nelle donne della stessa età 65–380 µg/dL. I livelli diminuiscono di circa il 10–20 % per decennio a partire dai 30 anni."},
            {"question": "Cosa significa un DHEA-S alto?",
             "answer": "Un DHEA-S alto può indicare sindrome dell'ovaio policistico (PCOS), iperplasia surrenalica congenita, tumori surrenalici o sindrome di Cushing. Una diagnosi accurata richiede la valutazione insieme ai riscontri clinici, ad altri test ormonali e all'imaging quando necessario."},
        ],
        "he": [
            {"question": "מהי בדיקת DHEA-S?",
             "answer": "בדיקת DHEA-S היא בדיקת הורמון אדרנל המודדת את רמת הדהידרואפיאנדרוסטרון סולפט בדם — ההורמון השכיח ביותר שמיוצר בבלוטות יותרת הכליה. היא משמשת להערכת תפקוד האדרנל ולסיוע באבחון מצבים כמו PCOS וגידולים באדרנל."},
            {"question": "מהו הטווח התקין של DHEA-S?",
             "answer": "טווח הנורמה של DHEA-S משתנה לפי גיל ומין. למשל, בגברים בגילאי 20–29 הוא בדרך כלל 280–640 µg/dL, ובנשים באותו גיל 65–380 µg/dL. הרמות יורדות בכ-10–20% בכל עשור מגיל 30."},
            {"question": "מה המשמעות של DHEA-S גבוה?",
             "answer": "DHEA-S גבוה עשוי להצביע על תסמונת השחלות הפוליציסטיות (PCOS), היפרפלזיה אדרנלית מולדת, גידולים באדרנל או תסמונת קושינג. אבחון מדויק דורש הערכה לצד ממצאים קליניים, בדיקות הורמונליות אחרות והדמיה בעת הצורך."},
        ],
        "hi": [
            {"question": "DHEA-S टेस्ट क्या है?",
             "answer": "DHEA-S टेस्ट एक एड्रीनल हार्मोन टेस्ट है जो रक्त में डीहाइड्रोएपिएंड्रोस्टेरोन सल्फेट के स्तर को मापता है — यह एड्रीनल ग्रंथियों द्वारा उत्पादित सबसे प्रचुर हार्मोन है। इसका उपयोग एड्रीनल फंक्शन का मूल्यांकन करने और PCOS तथा एड्रीनल ट्यूमर जैसी स्थितियों के निदान में किया जाता है।"},
            {"question": "DHEA-S की नॉर्मल रेंज क्या है?",
             "answer": "DHEA-S नॉर्मल रेंज उम्र और लिंग के अनुसार भिन्न होती है। उदाहरण के लिए, 20–29 वर्ष के पुरुषों में यह आम तौर पर 280–640 µg/dL और समान आयु की महिलाओं में 65–380 µg/dL होती है। 30 की उम्र से हर दशक में लेवल लगभग 10–20% कम होते हैं।"},
            {"question": "हाई DHEA-S का क्या मतलब है?",
             "answer": "हाई DHEA-S पॉलीसिस्टिक ओवरी सिंड्रोम (PCOS), कंजेनिटल एड्रीनल हाइपरप्लेसिया, एड्रीनल ट्यूमर या कुशिंग सिंड्रोम का संकेत हो सकता है। सटीक निदान के लिए क्लिनिकल निष्कर्षों, अन्य हार्मोन टेस्ट और ज़रूरत पड़ने पर इमेजिंग के साथ मूल्यांकन आवश्यक है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل DHEA-S؟",
             "answer": "تحليل DHEA-S هو اختبار هرمون كظري يقيس مستوى كبريتات ديهيدرو إيبي أندروستيرون في الدم — وهو أكثر الهرمونات وفرة التي تنتجها الغدتان الكظريتان. يُستخدم لتقييم وظيفة الغدة الكظرية والمساعدة في تشخيص حالات مثل متلازمة المبيض متعدد الكيسات وأورام الغدة الكظرية."},
            {"question": "ما هو النطاق الطبيعي لـ DHEA-S؟",
             "answer": "يختلف النطاق الطبيعي لـ DHEA-S حسب العمر والجنس. مثلاً، لدى الذكور بعمر 20–29 عاماً يتراوح عادةً بين 280–640 µg/dL، ولدى الإناث بنفس العمر بين 65–380 µg/dL. تنخفض المستويات بنحو 10–20% في كل عقد بدءاً من الثلاثينيات."},
            {"question": "ماذا يعني ارتفاع DHEA-S؟",
             "answer": "قد يشير ارتفاع DHEA-S إلى متلازمة المبيض متعدد الكيسات (PCOS) أو فرط تنسج الكظر الخلقي أو أورام الغدة الكظرية أو متلازمة كوشينغ. يتطلب التشخيص الدقيق تقييماً جنباً إلى جنب مع النتائج السريرية واختبارات هرمونية أخرى والتصوير عند الحاجة."},
        ],
    }
