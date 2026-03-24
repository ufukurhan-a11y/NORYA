# -*- coding: utf-8 -*-
"""
Procalcitonin (PCT) blog article — full body content for all 9 languages.
Used by blog_i18n._article_procalcitonin().
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

_PCT_TABLE_TR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Prokalsitonin Düzeyi (ng/mL)</th>"
    f"<th {_TH}>Klinik Yorum</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0,1</td>"
    f"<td {_TD}>Normal — bakteriyel enfeksiyon olasılığı çok düşük</td></tr>"
    f"<tr><td {_TD}>0,1 – 0,25</td>"
    f"<td {_TD}>Bakteriyel enfeksiyon olası değil; antibiyotik genellikle önerilmez</td></tr>"
    f"<tr><td {_TD}>0,25 – 0,5</td>"
    f"<td {_TD}>Olası bakteriyel enfeksiyon; antibiyotik düşünülebilir</td></tr>"
    f"<tr><td {_TD}>0,5 – 2</td>"
    f"<td {_TD}>Bakteriyel enfeksiyon muhtemel; antibiyotik kuvvetle önerilir</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>Sepsis olasılığı yüksek; yoğun antimikrobiyal tedavi gerekir</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>Ağır sepsis / septik şok; acil müdahale gerektirir</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_EN = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Procalcitonin Level (ng/mL)</th>"
    f"<th {_TH}>Clinical Interpretation</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0.1</td>"
    f"<td {_TD}>Normal — bacterial infection very unlikely</td></tr>"
    f"<tr><td {_TD}>0.1 – 0.25</td>"
    f"<td {_TD}>Bacterial infection unlikely; antibiotics generally not recommended</td></tr>"
    f"<tr><td {_TD}>0.25 – 0.5</td>"
    f"<td {_TD}>Possible bacterial infection; consider antibiotics</td></tr>"
    f"<tr><td {_TD}>0.5 – 2</td>"
    f"<td {_TD}>Bacterial infection likely; antibiotics strongly recommended</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>Sepsis likely; intensive antimicrobial therapy required</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>Severe sepsis / septic shock; urgent intervention needed</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_ES = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Nivel de procalcitonina (ng/mL)</th>"
    f"<th {_TH}>Interpretación clínica</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0,1</td>"
    f"<td {_TD}>Normal — infección bacteriana muy improbable</td></tr>"
    f"<tr><td {_TD}>0,1 – 0,25</td>"
    f"<td {_TD}>Infección bacteriana improbable; antibióticos generalmente no indicados</td></tr>"
    f"<tr><td {_TD}>0,25 – 0,5</td>"
    f"<td {_TD}>Posible infección bacteriana; considerar antibióticos</td></tr>"
    f"<tr><td {_TD}>0,5 – 2</td>"
    f"<td {_TD}>Infección bacteriana probable; antibióticos fuertemente recomendados</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>Sepsis probable; terapia antimicrobiana intensiva necesaria</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>Sepsis grave / choque séptico; intervención urgente</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_DE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Procalcitonin-Spiegel (ng/mL)</th>"
    f"<th {_TH}>Klinische Interpretation</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0,1</td>"
    f"<td {_TD}>Normal — bakterielle Infektion sehr unwahrscheinlich</td></tr>"
    f"<tr><td {_TD}>0,1 – 0,25</td>"
    f"<td {_TD}>Bakterielle Infektion unwahrscheinlich; Antibiotika in der Regel nicht empfohlen</td></tr>"
    f"<tr><td {_TD}>0,25 – 0,5</td>"
    f"<td {_TD}>Mögliche bakterielle Infektion; Antibiotika in Betracht ziehen</td></tr>"
    f"<tr><td {_TD}>0,5 – 2</td>"
    f"<td {_TD}>Bakterielle Infektion wahrscheinlich; Antibiotika dringend empfohlen</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>Sepsis wahrscheinlich; intensive antimikrobielle Therapie erforderlich</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>Schwere Sepsis / septischer Schock; sofortige Intervention erforderlich</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_FR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Taux de procalcitonine (ng/mL)</th>"
    f"<th {_TH}>Interprétation clinique</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0,1</td>"
    f"<td {_TD}>Normal — infection bactérienne très improbable</td></tr>"
    f"<tr><td {_TD}>0,1 – 0,25</td>"
    f"<td {_TD}>Infection bactérienne improbable ; antibiotiques généralement non recommandés</td></tr>"
    f"<tr><td {_TD}>0,25 – 0,5</td>"
    f"<td {_TD}>Infection bactérienne possible ; envisager des antibiotiques</td></tr>"
    f"<tr><td {_TD}>0,5 – 2</td>"
    f"<td {_TD}>Infection bactérienne probable ; antibiotiques fortement recommandés</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>Sepsis probable ; antibiothérapie intensive nécessaire</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>Sepsis sévère / choc septique ; intervention urgente requise</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_IT = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>Livello di procalcitonina (ng/mL)</th>"
    f"<th {_TH}>Interpretazione clinica</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0,1</td>"
    f"<td {_TD}>Normale — infezione batterica molto improbabile</td></tr>"
    f"<tr><td {_TD}>0,1 – 0,25</td>"
    f"<td {_TD}>Infezione batterica improbabile; antibiotici generalmente non indicati</td></tr>"
    f"<tr><td {_TD}>0,25 – 0,5</td>"
    f"<td {_TD}>Possibile infezione batterica; valutare antibiotici</td></tr>"
    f"<tr><td {_TD}>0,5 – 2</td>"
    f"<td {_TD}>Infezione batterica probabile; antibiotici fortemente raccomandati</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>Sepsi probabile; terapia antimicrobica intensiva necessaria</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>Sepsi grave / shock settico; intervento urgente necessario</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_HE = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>רמת פרוקלציטונין (ng/mL)</th>"
    f"<th {_TH_RTL}>פרשנות קלינית</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0.1</td>"
    f"<td {_TD}>תקין — זיהום חיידקי בלתי סביר מאוד</td></tr>"
    f"<tr><td {_TD}>0.1 – 0.25</td>"
    f"<td {_TD}>זיהום חיידקי לא סביר; אנטיביוטיקה בדרך כלל לא מומלצת</td></tr>"
    f"<tr><td {_TD}>0.25 – 0.5</td>"
    f"<td {_TD}>זיהום חיידקי אפשרי; יש לשקול אנטיביוטיקה</td></tr>"
    f"<tr><td {_TD}>0.5 – 2</td>"
    f"<td {_TD}>זיהום חיידקי סביר; אנטיביוטיקה מומלצת בחום</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>אלח דם סביר; טיפול אנטימיקרוביאלי אינטנסיבי נדרש</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>אלח דם חמור / הלם ספטי; התערבות דחופה נדרשת</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_HI = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH}>प्रोकैल्सीटोनिन स्तर (ng/mL)</th>"
    f"<th {_TH}>क्लिनिकल व्याख्या</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0.1</td>"
    f"<td {_TD}>सामान्य — बैक्टीरियल इंफेक्शन की संभावना बहुत कम</td></tr>"
    f"<tr><td {_TD}>0.1 – 0.25</td>"
    f"<td {_TD}>बैक्टीरियल इंफेक्शन असंभव; एंटीबायोटिक आमतौर पर अनुशंसित नहीं</td></tr>"
    f"<tr><td {_TD}>0.25 – 0.5</td>"
    f"<td {_TD}>संभावित बैक्टीरियल इंफेक्शन; एंटीबायोटिक पर विचार करें</td></tr>"
    f"<tr><td {_TD}>0.5 – 2</td>"
    f"<td {_TD}>बैक्टीरियल इंफेक्शन की प्रबल संभावना; एंटीबायोटिक की दृढ़ अनुशंसा</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>सेप्सिस की संभावना; गहन एंटीमाइक्रोबियल थेरेपी आवश्यक</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>गंभीर सेप्सिस / सेप्टिक शॉक; तत्काल हस्तक्षेप ज़रूरी</td></tr>"
    "</tbody></table>"
)

_PCT_TABLE_AR = (
    f'<table {_TBL}>'
    f"<thead><tr><th {_TH_RTL}>مستوى البروكالسيتونين (ng/mL)</th>"
    f"<th {_TH_RTL}>التفسير السريري</th></tr></thead>"
    "<tbody>"
    f"<tr><td {_TD}>&lt; 0.1</td>"
    f"<td {_TD}>طبيعي — عدوى بكتيرية غير مرجّحة جداً</td></tr>"
    f"<tr><td {_TD}>0.1 – 0.25</td>"
    f"<td {_TD}>عدوى بكتيرية غير مرجّحة؛ المضادات الحيوية غير موصى بها عادةً</td></tr>"
    f"<tr><td {_TD}>0.25 – 0.5</td>"
    f"<td {_TD}>عدوى بكتيرية محتملة؛ يُنظر في إعطاء مضادات حيوية</td></tr>"
    f"<tr><td {_TD}>0.5 – 2</td>"
    f"<td {_TD}>عدوى بكتيرية مرجّحة؛ المضادات الحيوية موصى بها بشدة</td></tr>"
    f"<tr><td {_TD}>2 – 10</td>"
    f"<td {_TD}>إنتان مرجّح؛ علاج مضاد للميكروبات مكثّف مطلوب</td></tr>"
    f"<tr><td {_TD}>&gt; 10</td>"
    f"<td {_TD}>إنتان شديد / صدمة إنتانية؛ تدخل عاجل مطلوب</td></tr>"
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
            heading="Prokalsitonin (PCT) kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>Prokalsitonin testi</strong>, vücuttaki bakteriyel enfeksiyonların "
                "şiddetini değerlendirmek için kullanılan önemli bir <strong>bakteriyel enfeksiyon "
                "kan testi</strong>dir. Prokalsitonin (PCT), tiroid bezinde kalsitonin hormonunun "
                "öncü proteini olarak üretilir; sağlıklı bireylerde kandaki düzeyi çok düşüktür. "
                "Ancak ciddi bakteriyel enfeksiyonlarda ve özellikle <strong>sepsiste</strong> "
                "karaciğer, böbrek, akciğer ve kas dokuları dahil birçok organdan kana salınarak "
                "<strong>prokalsitonin düzeyleri</strong> dramatik şekilde yükselir.</p>"
                "<p><strong>PCT kan testi</strong>, bakteriyel enfeksiyonu viral enfeksiyondan ayırt "
                "etmede en değerli biyobelirteçlerden biridir. Viral enfeksiyonlarda interferon-γ "
                "etkisiyle PCT sentezi baskılanırken, bakteriyel enfeksiyonlarda bakteri toksinleri "
                "ve proinflamatuar sitokinler PCT üretimini güçlü bir şekilde uyarır. Bu özellik "
                "sayesinde acil servislerde, yoğun bakım ünitelerinde (YBÜ) ve ayaktan hasta "
                "değerlendirmelerinde antibiyotik başlama ve sonlandırma kararlarına yol gösteren "
                "bir <strong>antibiyotik yönetimi</strong> aracı olarak kullanılmaktadır.</p>"
                "<p>Bu rehberde <strong>prokalsitonin normal değerleri</strong>, "
                "<strong>yüksek prokalsitonin</strong> nedenlerini ve ne zaman doktora başvurmanız "
                "gerektiğini öğreneceksiniz. Sonuçlarınızı doğru yorumlamak için klinik tablo ve "
                "diğer laboratuvar bulgularıyla birlikte değerlendirme yapılması gerektiğini "
                "unutmayın.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Prokalsitonin normal değerleri",
            body_html=(
                "<p><strong>Prokalsitonin normal aralığı</strong> genellikle 0,1 ng/mL'nin "
                "altındadır. Bu seviyedeki değerler ciddi bir bakteriyel enfeksiyon bulunmadığına "
                "işaret eder. PCT düzeyleri yükseldikçe bakteriyel enfeksiyon ve sepsis olasılığı "
                "artar; klinisyenler bu değerlere göre antibiyotik başlama veya kesilme kararı "
                "verir.</p>"
                "<p>Aşağıdaki tabloda <strong>prokalsitonin düzeyleri</strong> ve klinik "
                "yorumları özetlenmiştir:</p>"
                + _PCT_TABLE_TR +
                "<p>Bu eşik değerler kılavuz niteliğindedir; hastanın klinik durumu, komorbiditeleri "
                "ve enfeksiyonun odağı da değerlendirmeye katılmalıdır. Yenidoğanlarda ilk 48 saatte "
                "fizyolojik PCT yüksekliği görülebileceğinden, yorumlamada yaşa özgü referans "
                "aralıkları dikkate alınmalıdır.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Prokalsitonin yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Yüksek prokalsitonin</strong> ağırlıklı olarak ciddi bakteriyel "
                "enfeksiyonlara işaret eder, ancak başka klinik durumlarda da görülebilir. "
                "PCT yüksekliğine yol açabilecek başlıca nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Bakteriyel sepsis ve septik şok:</strong> PCT'nin en yüksek seviyelere "
                "ulaştığı durumdur. Gram-negatif bakteriyemilerde PCT düzeyleri özellikle belirgin "
                "olarak artar.</li>"
                "<li><strong>Bakteriyel pnömoni:</strong> Toplum kökenli veya hastane kökenli "
                "bakteriyel pnömonide PCT yükselirken, viral pnömonide düşük kalması ayırıcı "
                "tanıda yardımcıdır.</li>"
                "<li><strong>Bakteriyel menenjit:</strong> Bakteriyel menenjitte PCT belirgin "
                "şekilde yükselirken, viral menenjitte genellikle düşük seyreder.</li>"
                "<li><strong>İntra-abdominal enfeksiyonlar:</strong> Peritonit, apse ve kolesistit "
                "gibi ciddi abdominal enfeksiyonlar PCT artışına neden olur.</li>"
                "<li><strong>Üriner sistem enfeksiyonları (piyelonefrit):</strong> Üst üriner "
                "sistem enfeksiyonlarında özellikle bakteriyemi eşliğinde PCT yükselebilir.</li>"
                "<li><strong>Büyük cerrahi ve travma:</strong> Major cerrahi sonrası ve ciddi "
                "travmalarda steril inflamasyon nedeniyle PCT geçici olarak yükselebilir; "
                "ancak bu yükselme genellikle 2 ng/mL'nin altında kalır ve hızla düşer.</li>"
                "<li><strong>Ağır yanıklar:</strong> Geniş yanık yaralanmalarında doku hasarı "
                "ve enfeksiyon riski PCT artışına yol açabilir.</li>"
                "</ul>"
                "<p>Viral enfeksiyonlarda, otoimmün hastalıklarda ve lokalize bakteriyel "
                "enfeksiyonlarda PCT genellikle düşük kalır. Bu nedenle PCT testi, gereksiz "
                "antibiyotik kullanımını azaltan etkili bir <strong>antibiyotik yönetimi</strong> "
                "aracıdır. Seri PCT ölçümleri tedaviye yanıtı izlemede ve antibiyotik süresini "
                "kısaltmada altın standart olarak kabul edilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Yüksek ateş, titreme, hızlı kalp atışı, hızlı solunum, düşük tansiyon, "
                "bilinç bulanıklığı veya genel durumda ani kötüleşme gibi belirtiler yaşıyorsanız "
                "derhal acil servise başvurun. Bu semptomlar <strong>sepsis</strong> belirtileri "
                "olabilir ve <strong>prokalsitonin testi</strong> ile hızlı değerlendirme hayati "
                "önem taşır.</p>"
                "<p><strong>PCT kan testi</strong> sonucunuz yüksek çıktıysa panik yapmayın ancak "
                "sonucu mutlaka enfeksiyon hastalıkları veya yoğun bakım uzmanıyla paylaşın. "
                "<strong>Yüksek prokalsitonin</strong>, bakteriyel enfeksiyonun ciddiyetini ve "
                "tedaviye yanıtı değerlendirmede kritik bir göstergedir. Doktorunuz kan kültürü, "
                "tam kan sayımı, CRP ve görüntüleme yöntemleriyle birlikte klinik tabloyu "
                "netleştirecektir.</p>"
                "<p>Unutmayın: tek başına bir PCT değeri tanı koymaz. Ancak seri PCT ölçümleri, "
                "antibiyotik tedavisinin ne zaman başlatılacağını, değiştirilmesini veya "
                "sonlandırılmasını yönlendirmede kanıta dayalı güçlü bir araçtır. Sonuçlarınızı "
                "internet araştırması yerine mutlaka hekiminizle değerlendirin.</p>"
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
            heading="Procalcitonin (PCT) blood test: what your results mean",
            body_html=(
                "<p>The <strong>procalcitonin test</strong> is a key "
                "<strong>bacterial infection blood test</strong> used to assess the severity of "
                "bacterial infections and guide antibiotic therapy. Procalcitonin (PCT) is a "
                "precursor protein of calcitonin produced by the thyroid gland; in healthy "
                "individuals <strong>procalcitonin levels</strong> in the blood are extremely low. "
                "During serious bacterial infections — and especially in "
                "<strong>procalcitonin sepsis</strong> scenarios — multiple organs including the "
                "liver, kidneys, lungs, and muscle tissue release PCT into the bloodstream, "
                "causing levels to rise dramatically.</p>"
                "<p>The <strong>PCT blood test</strong> is one of the most valuable biomarkers for "
                "differentiating bacterial infections from viral infections. Viral infections "
                "trigger interferon-γ, which suppresses PCT synthesis, while bacterial toxins and "
                "pro-inflammatory cytokines strongly stimulate PCT production. This property makes "
                "procalcitonin an essential antibiotic stewardship tool in emergency departments, "
                "intensive care units (ICUs), and outpatient settings — guiding decisions on when "
                "to start or stop antibiotics.</p>"
                "<p>In this guide you will learn the <strong>procalcitonin normal range</strong>, "
                "the causes of <strong>high procalcitonin</strong>, and when to seek medical "
                "attention. Always remember that accurate interpretation requires evaluating your "
                "results alongside the clinical picture and other laboratory findings.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Procalcitonin normal range",
            body_html=(
                "<p>The <strong>procalcitonin normal range</strong> is generally below "
                "0.1 ng/mL. Values at this level indicate that a significant bacterial infection "
                "is very unlikely. As <strong>procalcitonin levels</strong> rise, the probability "
                "of bacterial infection and sepsis increases; clinicians use these thresholds to "
                "decide whether to initiate or discontinue antibiotic therapy.</p>"
                "<p>The table below summarises <strong>procalcitonin levels</strong> and their "
                "clinical interpretation:</p>"
                + _PCT_TABLE_EN +
                "<p>These cut-off values serve as guidelines; the patient's clinical status, "
                "comorbidities, and the focus of infection must also be considered. In neonates, "
                "a physiological PCT surge may occur during the first 48 hours of life, so "
                "age-specific reference ranges should be applied when interpreting results.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of high procalcitonin levels",
            body_html=(
                "<p><strong>High procalcitonin</strong> primarily signals severe bacterial "
                "infections, but elevations can occur in other clinical scenarios as well. The "
                "main causes of elevated <strong>procalcitonin levels</strong> include:</p>"
                "<ul>"
                "<li><strong>Bacterial sepsis and septic shock:</strong> PCT reaches its highest "
                "levels in sepsis. Gram-negative bacteraemia in particular drives markedly "
                "elevated values.</li>"
                "<li><strong>Bacterial pneumonia:</strong> Community-acquired or hospital-acquired "
                "bacterial pneumonia raises PCT, while viral pneumonia typically keeps it low — "
                "a distinction valuable for differential diagnosis.</li>"
                "<li><strong>Bacterial meningitis:</strong> PCT rises significantly in bacterial "
                "meningitis but usually remains low in viral meningitis.</li>"
                "<li><strong>Intra-abdominal infections:</strong> Peritonitis, abscesses, and "
                "cholecystitis can cause substantial PCT elevation.</li>"
                "<li><strong>Urinary tract infections (pyelonephritis):</strong> Upper urinary "
                "tract infections, especially with concurrent bacteraemia, can raise PCT.</li>"
                "<li><strong>Major surgery and trauma:</strong> Sterile inflammation after major "
                "surgery or severe trauma may transiently elevate PCT, though levels typically "
                "remain below 2 ng/mL and decline quickly.</li>"
                "<li><strong>Severe burns:</strong> Extensive burn injuries can cause PCT elevation "
                "due to tissue damage and heightened infection risk.</li>"
                "</ul>"
                "<p>In viral infections, autoimmune diseases, and localised bacterial infections, "
                "PCT generally remains low. This makes the <strong>procalcitonin test</strong> an "
                "effective antibiotic stewardship tool that helps reduce unnecessary antibiotic "
                "use. Serial PCT measurements are the gold standard for monitoring treatment "
                "response and shortening antibiotic duration.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If you experience high fever, chills, rapid heartbeat, rapid breathing, low "
                "blood pressure, confusion, or a sudden deterioration in your general condition, "
                "go to an emergency department immediately. These symptoms may indicate "
                "<strong>sepsis</strong>, and rapid evaluation with a "
                "<strong>procalcitonin test</strong> is critically important.</p>"
                "<p>If your <strong>PCT blood test</strong> result is elevated, do not panic but "
                "share the result with an infectious-disease specialist or intensivist without "
                "delay. <strong>High procalcitonin</strong> is a critical indicator for assessing "
                "the severity of a bacterial infection and monitoring treatment response. Your "
                "doctor will use blood cultures, a complete blood count, CRP, and imaging studies "
                "to clarify the clinical picture.</p>"
                "<p>Remember: a single PCT value is not a diagnosis. However, serial PCT "
                "measurements are a powerful evidence-based tool for guiding when to start, "
                "adjust, or stop antibiotic therapy. Always discuss your results with your "
                "physician rather than relying on internet research alone.</p>"
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
            heading="Prueba de procalcitonina (PCT): qué significan sus resultados",
            body_html=(
                "<p>La <strong>prueba de procalcitonina</strong> es un "
                "<strong>análisis de sangre para infección bacteriana</strong> clave que se "
                "utiliza para evaluar la gravedad de las infecciones bacterianas y guiar la "
                "terapia antibiótica. La procalcitonina (PCT) es una proteína precursora de la "
                "calcitonina producida por la glándula tiroides; en personas sanas los "
                "<strong>niveles de procalcitonina</strong> en sangre son extremadamente bajos. "
                "Sin embargo, en infecciones bacterianas graves — y especialmente en la "
                "<strong>sepsis</strong> — múltiples órganos, incluidos hígado, riñones, pulmones "
                "y tejido muscular, liberan PCT al torrente sanguíneo, provocando una elevación "
                "drástica.</p>"
                "<p>La <strong>prueba de PCT en sangre</strong> es uno de los biomarcadores más "
                "valiosos para diferenciar infecciones bacterianas de virales. Las infecciones "
                "virales activan el interferón-γ, que suprime la síntesis de PCT, mientras que "
                "las toxinas bacterianas y las citocinas proinflamatorias estimulan poderosamente "
                "la producción de PCT. Esta propiedad convierte a la procalcitonina en una "
                "herramienta esencial de gestión antibiótica en urgencias, unidades de cuidados "
                "intensivos (UCI) y en la atención ambulatoria.</p>"
                "<p>En esta guía conocerá el <strong>rango normal de procalcitonina</strong>, las "
                "causas de <strong>procalcitonina alta</strong> y cuándo buscar atención médica. "
                "Recuerde que una interpretación precisa requiere evaluar los resultados junto con "
                "el cuadro clínico y otros hallazgos de laboratorio.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de procalcitonina",
            body_html=(
                "<p>El <strong>rango normal de procalcitonina</strong> se sitúa generalmente por "
                "debajo de 0,1 ng/mL. Valores en este nivel indican que una infección bacteriana "
                "significativa es muy improbable. A medida que los "
                "<strong>niveles de procalcitonina</strong> aumentan, la probabilidad de infección "
                "bacteriana y sepsis crece; los clínicos utilizan estos umbrales para decidir si "
                "iniciar o suspender la antibioterapia.</p>"
                "<p>La siguiente tabla resume los <strong>niveles de procalcitonina</strong> y su "
                "interpretación clínica:</p>"
                + _PCT_TABLE_ES +
                "<p>Estos valores de corte son orientativos; el estado clínico del paciente, sus "
                "comorbilidades y el foco infeccioso también deben considerarse. En neonatos puede "
                "producirse una elevación fisiológica de PCT durante las primeras 48 horas de vida, "
                "por lo que deben aplicarse rangos de referencia específicos por edad.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de procalcitonina alta",
            body_html=(
                "<p>La <strong>procalcitonina alta</strong> indica principalmente infecciones "
                "bacterianas graves, aunque puede elevarse en otros escenarios clínicos. Las "
                "principales causas de elevación de los "
                "<strong>niveles de procalcitonina</strong> incluyen:</p>"
                "<ul>"
                "<li><strong>Sepsis bacteriana y choque séptico:</strong> La PCT alcanza sus "
                "valores más altos en la sepsis. La bacteriemia por gramnegativos produce "
                "elevaciones particularmente marcadas.</li>"
                "<li><strong>Neumonía bacteriana:</strong> La neumonía bacteriana comunitaria u "
                "hospitalaria eleva la PCT, mientras que la neumonía viral suele mantenerla baja, "
                "lo que es útil en el diagnóstico diferencial.</li>"
                "<li><strong>Meningitis bacteriana:</strong> La PCT se eleva significativamente en "
                "la meningitis bacteriana pero suele permanecer baja en la viral.</li>"
                "<li><strong>Infecciones intraabdominales:</strong> Peritonitis, abscesos y "
                "colecistitis pueden causar una elevación sustancial de la PCT.</li>"
                "<li><strong>Infecciones urinarias (pielonefritis):</strong> Las infecciones del "
                "tracto urinario superior, especialmente con bacteriemia concomitante, pueden "
                "elevar la PCT.</li>"
                "<li><strong>Cirugía mayor y traumatismos:</strong> La inflamación estéril tras "
                "cirugía mayor o traumatismo grave puede elevar transitoriamente la PCT, aunque "
                "suele permanecer por debajo de 2 ng/mL y desciende rápidamente.</li>"
                "<li><strong>Quemaduras graves:</strong> Las lesiones extensas por quemadura "
                "pueden provocar elevación de la PCT por daño tisular y riesgo elevado de "
                "infección.</li>"
                "</ul>"
                "<p>En infecciones virales, enfermedades autoinmunes e infecciones bacterianas "
                "localizadas, la PCT generalmente permanece baja. Esto convierte a la "
                "<strong>prueba de procalcitonina</strong> en una herramienta eficaz de gestión "
                "antibiótica que ayuda a reducir el uso innecesario de antibióticos. Las "
                "mediciones seriadas de PCT son el estándar de oro para monitorizar la respuesta "
                "al tratamiento y acortar la duración antibiótica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Si experimenta fiebre alta, escalofríos, frecuencia cardíaca rápida, "
                "respiración acelerada, presión arterial baja, confusión o un deterioro súbito "
                "de su estado general, acuda de inmediato a un servicio de urgencias. Estos "
                "síntomas pueden indicar <strong>sepsis</strong>, y la evaluación rápida mediante "
                "una <strong>prueba de procalcitonina</strong> es de vital importancia.</p>"
                "<p>Si su resultado de <strong>PCT en sangre</strong> está elevado, no se alarme "
                "pero comparta el resultado sin demora con un especialista en enfermedades "
                "infecciosas o un intensivista. La <strong>procalcitonina alta</strong> es un "
                "indicador crítico para evaluar la gravedad de una infección bacteriana y "
                "monitorizar la respuesta al tratamiento. Su médico utilizará hemocultivos, "
                "hemograma completo, PCR y estudios de imagen para esclarecer el cuadro "
                "clínico.</p>"
                "<p>Recuerde: un valor aislado de PCT no es un diagnóstico. Sin embargo, las "
                "mediciones seriadas de PCT son una herramienta basada en la evidencia para "
                "orientar cuándo iniciar, ajustar o suspender la antibioterapia. Consulte siempre "
                "a su médico en lugar de confiar únicamente en búsquedas en internet.</p>"
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
            heading="Procalcitonin (PCT)-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>Procalcitonin-Test</strong> ist ein zentraler "
                "<strong>Bluttest für bakterielle Infektionen</strong>, der zur Beurteilung des "
                "Schweregrads bakterieller Infektionen und zur Steuerung der Antibiotikatherapie "
                "eingesetzt wird. Procalcitonin (PCT) ist ein Vorläuferprotein des Calcitonins, "
                "das von der Schilddrüse produziert wird; bei gesunden Personen sind die "
                "<strong>Procalcitonin-Spiegel</strong> im Blut äußerst niedrig. Bei schweren "
                "bakteriellen Infektionen — insbesondere bei <strong>Sepsis</strong> — setzen "
                "Leber, Nieren, Lungen und Muskelgewebe PCT in die Blutbahn frei, was zu einem "
                "dramatischen Anstieg führt.</p>"
                "<p>Der <strong>PCT-Bluttest</strong> ist einer der wertvollsten Biomarker zur "
                "Unterscheidung bakterieller von viralen Infektionen. Virale Infektionen lösen "
                "Interferon-γ aus, das die PCT-Synthese unterdrückt, während bakterielle Toxine "
                "und proinflammatorische Zytokine die PCT-Produktion stark stimulieren. Diese "
                "Eigenschaft macht Procalcitonin zu einem unverzichtbaren Instrument des "
                "Antibiotic Stewardship in Notaufnahmen, Intensivstationen und im ambulanten "
                "Bereich — es leitet Entscheidungen über den Beginn und das Absetzen von "
                "Antibiotika.</p>"
                "<p>In diesem Ratgeber erfahren Sie die "
                "<strong>Procalcitonin-Normalwerte</strong>, die Ursachen für "
                "<strong>erhöhtes Procalcitonin</strong> und wann Sie ärztliche Hilfe suchen "
                "sollten. Denken Sie daran, dass eine korrekte Interpretation die Bewertung "
                "Ihrer Ergebnisse im Zusammenhang mit dem klinischen Bild und anderen "
                "Laborbefunden erfordert.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Procalcitonin-Normalwerte",
            body_html=(
                "<p>Der <strong>Procalcitonin-Normalbereich</strong> liegt in der Regel unter "
                "0,1 ng/mL. Werte in diesem Bereich deuten darauf hin, dass eine signifikante "
                "bakterielle Infektion sehr unwahrscheinlich ist. Mit steigenden "
                "<strong>Procalcitonin-Spiegeln</strong> nimmt die Wahrscheinlichkeit einer "
                "bakteriellen Infektion und Sepsis zu; Kliniker nutzen diese Schwellenwerte, "
                "um über den Beginn oder das Absetzen einer Antibiotikatherapie zu "
                "entscheiden.</p>"
                "<p>Die folgende Tabelle fasst die <strong>Procalcitonin-Spiegel</strong> und "
                "ihre klinische Interpretation zusammen:</p>"
                + _PCT_TABLE_DE +
                "<p>Diese Grenzwerte dienen als Leitlinie; der klinische Zustand des Patienten, "
                "Begleiterkrankungen und der Infektionsherd müssen ebenfalls berücksichtigt "
                "werden. Bei Neugeborenen kann in den ersten 48 Lebensstunden ein physiologischer "
                "PCT-Anstieg auftreten, weshalb bei der Interpretation altersspezifische "
                "Referenzbereiche heranzuziehen sind.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für erhöhte Procalcitonin-Werte",
            body_html=(
                "<p><strong>Erhöhtes Procalcitonin</strong> weist in erster Linie auf schwere "
                "bakterielle Infektionen hin, kann jedoch auch in anderen klinischen Situationen "
                "auftreten. Die wichtigsten Ursachen erhöhter "
                "<strong>Procalcitonin-Spiegel</strong> sind:</p>"
                "<ul>"
                "<li><strong>Bakterielle Sepsis und septischer Schock:</strong> In der Sepsis "
                "erreicht PCT seine höchsten Werte. Gramnegative Bakteriämien führen zu besonders "
                "ausgeprägten Anstiegen.</li>"
                "<li><strong>Bakterielle Pneumonie:</strong> Ambulant oder nosokomial erworbene "
                "bakterielle Pneumonien erhöhen PCT, während virale Pneumonien es typischerweise "
                "niedrig halten — ein wichtiger Unterschied für die Differenzialdiagnose.</li>"
                "<li><strong>Bakterielle Meningitis:</strong> PCT steigt bei bakterieller "
                "Meningitis deutlich an, bleibt bei viraler Meningitis jedoch meist niedrig.</li>"
                "<li><strong>Intraabdominelle Infektionen:</strong> Peritonitis, Abszesse und "
                "Cholezystitis können einen erheblichen PCT-Anstieg verursachen.</li>"
                "<li><strong>Harnwegsinfektionen (Pyelonephritis):</strong> Obere "
                "Harnwegsinfektionen, insbesondere bei gleichzeitiger Bakteriämie, können zu "
                "einem PCT-Anstieg führen.</li>"
                "<li><strong>Große Operationen und Traumata:</strong> Sterile Entzündungen nach "
                "großen Eingriffen oder schwerem Trauma können PCT vorübergehend erhöhen, wobei "
                "die Werte in der Regel unter 2 ng/mL bleiben und rasch abfallen.</li>"
                "<li><strong>Schwere Verbrennungen:</strong> Ausgedehnte Brandverletzungen können "
                "durch Gewebeschäden und erhöhtes Infektionsrisiko zu einem PCT-Anstieg "
                "führen.</li>"
                "</ul>"
                "<p>Bei viralen Infektionen, Autoimmunerkrankungen und lokalisierten bakteriellen "
                "Infektionen bleibt PCT in der Regel niedrig. Dies macht den "
                "<strong>Procalcitonin-Test</strong> zu einem wirksamen Antibiotic-Stewardship-"
                "Instrument, das unnötigen Antibiotikaeinsatz reduzieren hilft. Serielle "
                "PCT-Messungen sind der Goldstandard zur Überwachung des Therapieansprechens und "
                "zur Verkürzung der Antibiotikadauer.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Sie hohes Fieber, Schüttelfrost, schnellen Herzschlag, beschleunigte "
                "Atmung, niedrigen Blutdruck, Verwirrtheit oder eine plötzliche Verschlechterung "
                "Ihres Allgemeinzustands bemerken, suchen Sie sofort eine Notaufnahme auf. Diese "
                "Symptome können auf eine <strong>Sepsis</strong> hindeuten, und eine rasche "
                "Abklärung mittels <strong>Procalcitonin-Test</strong> ist von entscheidender "
                "Bedeutung.</p>"
                "<p>Wenn Ihr <strong>PCT-Bluttest</strong>-Ergebnis erhöht ist, bewahren Sie "
                "Ruhe, teilen Sie das Ergebnis aber unverzüglich einem Infektiologen oder "
                "Intensivmediziner mit. <strong>Erhöhtes Procalcitonin</strong> ist ein kritischer "
                "Indikator zur Beurteilung des Schweregrades einer bakteriellen Infektion und "
                "zur Überwachung des Therapieansprechens. Ihr Arzt wird Blutkulturen, ein großes "
                "Blutbild, CRP und bildgebende Verfahren zur Klärung des klinischen Bildes "
                "heranziehen.</p>"
                "<p>Denken Sie daran: Ein einzelner PCT-Wert stellt keine Diagnose. Serielle "
                "PCT-Messungen sind jedoch ein starkes evidenzbasiertes Instrument, um den "
                "Zeitpunkt für den Beginn, die Anpassung oder das Absetzen einer "
                "Antibiotikatherapie zu bestimmen. Besprechen Sie Ihre Ergebnisse stets mit "
                "Ihrem Arzt, anstatt sich allein auf Internetrecherchen zu verlassen.</p>"
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
            heading="Test de procalcitonine (PCT) : que signifient vos résultats ?",
            body_html=(
                "<p>Le <strong>test de procalcitonine</strong> est une "
                "<strong>analyse de sang pour infection bactérienne</strong> essentielle, "
                "utilisée pour évaluer la gravité des infections bactériennes et guider "
                "l'antibiothérapie. La procalcitonine (PCT) est une protéine précurseur de la "
                "calcitonine produite par la thyroïde ; chez les sujets sains, les "
                "<strong>taux de procalcitonine</strong> sanguins sont extrêmement bas. Lors "
                "d'infections bactériennes sévères — et surtout en cas de "
                "<strong>sepsis</strong> — de multiples organes, dont le foie, les reins, les "
                "poumons et les muscles, libèrent la PCT dans le sang, provoquant une élévation "
                "spectaculaire.</p>"
                "<p>Le <strong>dosage de PCT</strong> est l'un des biomarqueurs les plus précieux "
                "pour différencier les infections bactériennes des infections virales. Les "
                "infections virales déclenchent l'interféron-γ, qui inhibe la synthèse de PCT, "
                "tandis que les toxines bactériennes et les cytokines pro-inflammatoires stimulent "
                "fortement la production de PCT. Cette propriété fait de la procalcitonine un "
                "outil indispensable de bon usage des antibiotiques aux urgences, en réanimation "
                "et en ambulatoire — orientant les décisions d'initiation ou d'arrêt des "
                "antibiotiques.</p>"
                "<p>Dans ce guide, vous découvrirez les "
                "<strong>valeurs normales de procalcitonine</strong>, les causes d'une "
                "<strong>procalcitonine élevée</strong> et quand consulter un médecin. "
                "N'oubliez pas qu'une interprétation correcte nécessite d'évaluer vos résultats "
                "en parallèle avec le tableau clinique et les autres examens biologiques.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de procalcitonine",
            body_html=(
                "<p>Les <strong>valeurs normales de procalcitonine</strong> se situent "
                "généralement en dessous de 0,1 ng/mL. Des valeurs à ce niveau indiquent qu'une "
                "infection bactérienne significative est très improbable. À mesure que les "
                "<strong>taux de procalcitonine</strong> augmentent, la probabilité d'une "
                "infection bactérienne et d'un sepsis s'accroît ; les cliniciens s'appuient sur "
                "ces seuils pour décider d'initier ou d'arrêter l'antibiothérapie.</p>"
                "<p>Le tableau ci-dessous résume les <strong>taux de procalcitonine</strong> et "
                "leur interprétation clinique :</p>"
                + _PCT_TABLE_FR +
                "<p>Ces valeurs seuils sont indicatives ; l'état clinique du patient, ses "
                "comorbidités et le foyer infectieux doivent également être pris en compte. Chez "
                "le nouveau-né, une élévation physiologique de la PCT peut survenir dans les "
                "48 premières heures de vie ; des valeurs de référence spécifiques à l'âge "
                "doivent donc être appliquées.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'une procalcitonine élevée",
            body_html=(
                "<p>Une <strong>procalcitonine élevée</strong> indique principalement des "
                "infections bactériennes sévères, mais des élévations peuvent survenir dans "
                "d'autres situations cliniques. Les principales causes d'élévation des "
                "<strong>taux de procalcitonine</strong> sont :</p>"
                "<ul>"
                "<li><strong>Sepsis bactérien et choc septique :</strong> La PCT atteint ses "
                "valeurs les plus élevées lors d'un sepsis. Les bactériémies à Gram négatif "
                "entraînent des élévations particulièrement marquées.</li>"
                "<li><strong>Pneumonie bactérienne :</strong> La pneumonie bactérienne "
                "communautaire ou nosocomiale élève la PCT, tandis que la pneumonie virale la "
                "maintient généralement basse — une distinction précieuse pour le diagnostic "
                "différentiel.</li>"
                "<li><strong>Méningite bactérienne :</strong> La PCT s'élève nettement dans la "
                "méningite bactérienne mais reste habituellement basse dans la méningite "
                "virale.</li>"
                "<li><strong>Infections intra-abdominales :</strong> Péritonite, abcès et "
                "cholécystite peuvent provoquer une élévation substantielle de la PCT.</li>"
                "<li><strong>Infections urinaires (pyélonéphrite) :</strong> Les infections "
                "urinaires hautes, surtout en cas de bactériémie associée, peuvent élever la "
                "PCT.</li>"
                "<li><strong>Chirurgie majeure et traumatismes :</strong> L'inflammation stérile "
                "après une chirurgie majeure ou un traumatisme grave peut élever transitoirement "
                "la PCT, bien que les valeurs restent généralement en dessous de 2 ng/mL et "
                "diminuent rapidement.</li>"
                "<li><strong>Brûlures étendues :</strong> Les brûlures sévères peuvent provoquer "
                "une élévation de la PCT en raison des lésions tissulaires et du risque infectieux "
                "accru.</li>"
                "</ul>"
                "<p>Lors d'infections virales, de maladies auto-immunes et d'infections "
                "bactériennes localisées, la PCT reste généralement basse. Cela fait du "
                "<strong>test de procalcitonine</strong> un outil efficace de bon usage des "
                "antibiotiques, contribuant à réduire leur utilisation inutile. Les dosages "
                "sériés de PCT constituent la référence pour surveiller la réponse thérapeutique "
                "et raccourcir la durée de l'antibiothérapie.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si vous présentez une forte fièvre, des frissons, une tachycardie, une "
                "respiration rapide, une hypotension, une confusion ou une dégradation soudaine "
                "de votre état général, rendez-vous immédiatement aux urgences. Ces symptômes "
                "peuvent indiquer un <strong>sepsis</strong>, et une évaluation rapide par un "
                "<strong>test de procalcitonine</strong> est d'une importance capitale.</p>"
                "<p>Si votre résultat de <strong>dosage de PCT</strong> est élevé, ne paniquez "
                "pas mais partagez-le sans délai avec un infectiologue ou un réanimateur. Une "
                "<strong>procalcitonine élevée</strong> est un indicateur critique pour évaluer "
                "la gravité d'une infection bactérienne et suivre la réponse au traitement. "
                "Votre médecin utilisera des hémocultures, une NFS, la CRP et l'imagerie pour "
                "clarifier le tableau clinique.</p>"
                "<p>N'oubliez pas : un résultat isolé de PCT ne constitue pas un diagnostic. "
                "Cependant, les dosages sériés de PCT sont un outil puissant fondé sur les "
                "preuves pour guider l'initiation, l'adaptation ou l'arrêt de l'antibiothérapie. "
                "Consultez toujours votre médecin plutôt que de vous fier uniquement à des "
                "recherches sur internet.</p>"
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
            heading="Test della procalcitonina (PCT): cosa significano i tuoi risultati",
            body_html=(
                "<p>Il <strong>test della procalcitonina</strong> è un "
                "<strong>esame del sangue per infezione batterica</strong> fondamentale, "
                "utilizzato per valutare la gravità delle infezioni batteriche e guidare la "
                "terapia antibiotica. La procalcitonina (PCT) è una proteina precursore della "
                "calcitonina prodotta dalla tiroide; nelle persone sane i "
                "<strong>livelli di procalcitonina</strong> nel sangue sono estremamente bassi. "
                "Durante infezioni batteriche gravi — e soprattutto nella "
                "<strong>sepsi</strong> — fegato, reni, polmoni e tessuto muscolare rilasciano "
                "PCT nel circolo ematico, causando un incremento drammatico.</p>"
                "<p>Il <strong>dosaggio della PCT</strong> è uno dei biomarcatori più preziosi "
                "per distinguere le infezioni batteriche da quelle virali. Le infezioni virali "
                "attivano l'interferone-γ, che sopprime la sintesi di PCT, mentre le tossine "
                "batteriche e le citochine pro-infiammatorie stimolano potentemente la produzione "
                "di PCT. Questa proprietà rende la procalcitonina uno strumento essenziale di "
                "antimicrobial stewardship nei pronto soccorso, nelle terapie intensive e "
                "nell'ambulatorio — guidando le decisioni sull'avvio o la sospensione degli "
                "antibiotici.</p>"
                "<p>In questa guida scoprirai i "
                "<strong>valori normali di procalcitonina</strong>, le cause di "
                "<strong>procalcitonina alta</strong> e quando rivolgersi al medico. Ricorda che "
                "un'interpretazione accurata richiede la valutazione dei risultati insieme al "
                "quadro clinico e ad altri esami di laboratorio.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di procalcitonina",
            body_html=(
                "<p>I <strong>valori normali di procalcitonina</strong> sono generalmente "
                "inferiori a 0,1 ng/mL. Valori a questo livello indicano che un'infezione "
                "batterica significativa è molto improbabile. Man mano che i "
                "<strong>livelli di procalcitonina</strong> aumentano, cresce la probabilità di "
                "infezione batterica e sepsi; i clinici utilizzano queste soglie per decidere se "
                "iniziare o sospendere la terapia antibiotica.</p>"
                "<p>La tabella seguente riassume i <strong>livelli di procalcitonina</strong> e "
                "la loro interpretazione clinica:</p>"
                + _PCT_TABLE_IT +
                "<p>Questi valori soglia sono indicativi; lo stato clinico del paziente, le "
                "comorbidità e il focolaio infettivo devono essere anch'essi considerati. Nei "
                "neonati può verificarsi un aumento fisiologico della PCT nelle prime 48 ore "
                "di vita, pertanto vanno applicati intervalli di riferimento specifici per "
                "età.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di procalcitonina alta",
            body_html=(
                "<p>La <strong>procalcitonina alta</strong> segnala principalmente infezioni "
                "batteriche gravi, ma può elevarsi anche in altri contesti clinici. Le principali "
                "cause di innalzamento dei <strong>livelli di procalcitonina</strong> "
                "includono:</p>"
                "<ul>"
                "<li><strong>Sepsi batterica e shock settico:</strong> La PCT raggiunge i valori "
                "più elevati nella sepsi. Le batteriemie da Gram-negativi determinano aumenti "
                "particolarmente marcati.</li>"
                "<li><strong>Polmonite batterica:</strong> La polmonite batterica comunitaria o "
                "nosocomiale innalza la PCT, mentre la polmonite virale la mantiene tipicamente "
                "bassa — un elemento prezioso per la diagnosi differenziale.</li>"
                "<li><strong>Meningite batterica:</strong> La PCT si eleva significativamente "
                "nella meningite batterica ma resta solitamente bassa nella meningite virale.</li>"
                "<li><strong>Infezioni intra-addominali:</strong> Peritonite, ascessi e "
                "colecistite possono causare un notevole innalzamento della PCT.</li>"
                "<li><strong>Infezioni delle vie urinarie (pielonefrite):</strong> Le infezioni "
                "del tratto urinario superiore, specie in presenza di batteriemia, possono "
                "elevare la PCT.</li>"
                "<li><strong>Chirurgia maggiore e traumi:</strong> L'infiammazione sterile dopo "
                "interventi chirurgici maggiori o traumi gravi può innalzare transitoriamente la "
                "PCT, sebbene i valori restino generalmente sotto 2 ng/mL e scendano "
                "rapidamente.</li>"
                "<li><strong>Ustioni gravi:</strong> Le ustioni estese possono provocare un "
                "aumento della PCT a causa del danno tissutale e dell'elevato rischio "
                "infettivo.</li>"
                "</ul>"
                "<p>Nelle infezioni virali, nelle malattie autoimmuni e nelle infezioni "
                "batteriche localizzate, la PCT resta generalmente bassa. Questo rende il "
                "<strong>test della procalcitonina</strong> uno strumento efficace di "
                "antimicrobial stewardship che contribuisce a ridurre l'uso inappropriato di "
                "antibiotici. Le misurazioni seriali della PCT rappresentano il gold standard per "
                "monitorare la risposta terapeutica e abbreviare la durata dell'antibioticoterapia.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Se avverti febbre alta, brividi, tachicardia, respirazione rapida, pressione "
                "bassa, confusione o un peggioramento improvviso delle condizioni generali, "
                "recati immediatamente al pronto soccorso. Questi sintomi possono indicare una "
                "<strong>sepsi</strong>, e una valutazione rapida con un "
                "<strong>test della procalcitonina</strong> è di importanza cruciale.</p>"
                "<p>Se il tuo risultato del <strong>dosaggio della PCT</strong> è elevato, non "
                "allarmarti ma condividi il risultato senza indugio con un infettivologo o un "
                "intensivista. La <strong>procalcitonina alta</strong> è un indicatore critico "
                "per valutare la gravità di un'infezione batterica e monitorare la risposta al "
                "trattamento. Il tuo medico utilizzerà emocolture, emocromo completo, PCR ed "
                "esami di imaging per chiarire il quadro clinico.</p>"
                "<p>Ricorda: un singolo valore di PCT non è una diagnosi. Tuttavia, le "
                "misurazioni seriali della PCT sono uno strumento potente basato sull'evidenza "
                "per guidare l'avvio, l'adeguamento o la sospensione della terapia antibiotica. "
                "Consulta sempre il tuo medico anziché affidarti esclusivamente a ricerche su "
                "internet.</p>"
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
            heading="בדיקת פרוקלציטונין (PCT) בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>בדיקת פרוקלציטונין</strong> היא "
                "<strong>בדיקת דם לזיהום חיידקי</strong> מרכזית המשמשת להערכת חומרת זיהומים "
                "חיידקיים ולהנחיית טיפול אנטיביוטי. פרוקלציטונין (PCT) הוא חלבון מקדים של "
                "קלציטונין המיוצר בבלוטת התריס; אצל אנשים בריאים "
                "<strong>רמות הפרוקלציטונין</strong> בדם נמוכות מאוד. בזיהומים חיידקיים חמורים "
                "— ובמיוחד ב<strong>אלח דם (ספסיס)</strong> — איברים רבים כולל הכבד, הכליות, "
                "הריאות ורקמת השריר משחררים PCT לזרם הדם, וגורמים לעלייה דרמטית.</p>"
                "<p><strong>בדיקת PCT בדם</strong> היא אחד הסמנים הביולוגיים החשובים ביותר "
                "להבחנה בין זיהום חיידקי לזיהום ויראלי. זיהומים ויראליים מפעילים אינטרפרון-γ "
                "המדכא את סינתזת PCT, בעוד שרעלני חיידקים וציטוקינים פרו-דלקתיים ממריצים בעוצמה "
                "את ייצור PCT. תכונה זו הופכת את הפרוקלציטונין לכלי חיוני לניהול אנטיביוטי "
                "נכון בחדרי מיון, יחידות טיפול נמרץ ובמרפאות — ומנחה החלטות מתי להתחיל או "
                "להפסיק אנטיביוטיקה.</p>"
                "<p>במדריך זה תלמדו מהו <strong>טווח הנורמה של פרוקלציטונין</strong>, מהם "
                "הגורמים ל<strong>פרוקלציטונין גבוה</strong> ומתי לפנות לטיפול רפואי. זכרו "
                "שפרשנות מדויקת דורשת הערכת התוצאות לצד התמונה הקלינית וממצאי מעבדה "
                "נוספים.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של פרוקלציטונין",
            body_html=(
                "<p><strong>טווח הנורמה של פרוקלציטונין</strong> הוא בדרך כלל מתחת ל-0.1 "
                "ng/mL. ערכים ברמה זו מצביעים על כך שזיהום חיידקי משמעותי אינו סביר. ככל "
                "ש<strong>רמות הפרוקלציטונין</strong> עולות, כך גדלה ההסתברות לזיהום חיידקי "
                "ואלח דם; קלינאים משתמשים בספי סף אלה כדי להחליט אם להתחיל או להפסיק טיפול "
                "אנטיביוטי.</p>"
                "<p>הטבלה שלהלן מסכמת את <strong>רמות הפרוקלציטונין</strong> ואת הפרשנות "
                "הקלינית שלהן:</p>"
                + _PCT_TABLE_HE +
                "<p>ערכי סף אלה משמשים כהנחיות; מצבו הקליני של המטופל, מחלות רקע ומוקד "
                "הזיהום צריכים גם הם להילקח בחשבון. אצל יילודים עלולה להתרחש עלייה פיזיולוגית "
                "ב-PCT ב-48 השעות הראשונות לחיים, ולכן יש להשתמש בטווחי ייחוס ספציפיים "
                "לגיל.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות פרוקלציטונין גבוהות",
            body_html=(
                "<p><strong>פרוקלציטונין גבוה</strong> מצביע בעיקר על זיהומים חיידקיים חמורים, "
                "אך עליות יכולות להתרחש גם במצבים קליניים אחרים. הגורמים העיקריים לעליית "
                "<strong>רמות הפרוקלציטונין</strong> כוללים:</p>"
                "<ul>"
                "<li><strong>אלח דם חיידקי והלם ספטי:</strong> PCT מגיע לערכיו הגבוהים ביותר "
                "באלח דם. בקטרמיה מחיידקים גראם-שליליים גורמת לעליות בולטות במיוחד.</li>"
                "<li><strong>דלקת ריאות חיידקית:</strong> דלקת ריאות חיידקית קהילתית או "
                "נוזוקומיאלית מעלה PCT, בעוד שדלקת ריאות ויראלית שומרת עליו נמוך — הבחנה "
                "חשובה לאבחנה מבדלת.</li>"
                "<li><strong>דלקת קרום המוח חיידקית:</strong> PCT עולה משמעותית בדלקת קרום המוח "
                "החיידקית אך נשאר בדרך כלל נמוך בדלקת ויראלית.</li>"
                "<li><strong>זיהומים תוך-בטניים:</strong> דלקת צפק, מורסות ודלקת כיס המרה עלולים "
                "לגרום לעליית PCT משמעותית.</li>"
                "<li><strong>זיהומי דרכי השתן (פיאלונפריטיס):</strong> זיהומים בדרכי השתן "
                "העליונות, במיוחד עם בקטרמיה נלווית, עלולים להעלות PCT.</li>"
                "<li><strong>ניתוחים גדולים וטראומה:</strong> דלקת סטרילית לאחר ניתוח גדול או "
                "טראומה חמורה עלולה להעלות PCT באופן חולף, אם כי הערכים נשארים בדרך כלל מתחת "
                "ל-2 ng/mL ויורדים במהירות.</li>"
                "<li><strong>כוויות חמורות:</strong> כוויות נרחבות עלולות לגרום לעליית PCT עקב "
                "נזק רקמתי וסיכון מוגבר לזיהום.</li>"
                "</ul>"
                "<p>בזיהומים ויראליים, מחלות אוטואימוניות וזיהומים חיידקיים מקומיים, PCT נשאר "
                "בדרך כלל נמוך. זה הופך את <strong>בדיקת הפרוקלציטונין</strong> לכלי יעיל "
                "לניהול אנטיביוטי שמסייע להפחית שימוש מיותר באנטיביוטיקה. מדידות PCT סדרתיות "
                "הן תקן הזהב למעקב אחר תגובה לטיפול ולקיצור משך הטיפול האנטיביוטי.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם אתם חווים חום גבוה, צמרמורות, דופק מהיר, נשימה מהירה, לחץ דם נמוך, "
                "בלבול או הידרדרות פתאומית במצבכם הכללי, פנו מיד לחדר מיון. תסמינים אלה "
                "עלולים להצביע על <strong>אלח דם (ספסיס)</strong>, והערכה מהירה באמצעות "
                "<strong>בדיקת פרוקלציטונין</strong> חיונית ביותר.</p>"
                "<p>אם תוצאת <strong>בדיקת PCT בדם</strong> שלכם גבוהה, אל תיבהלו אך שתפו את "
                "התוצאה ללא דיחוי עם מומחה למחלות זיהומיות או רופא טיפול נמרץ. "
                "<strong>פרוקלציטונין גבוה</strong> הוא מדד קריטי להערכת חומרת זיהום חיידקי "
                "ולמעקב אחר תגובה לטיפול. הרופא שלכם ישתמש בתרביות דם, ספירת דם מלאה, CRP "
                "ובדיקות דימות כדי להבהיר את התמונה הקלינית.</p>"
                "<p>זכרו: ערך PCT בודד אינו אבחנה. עם זאת, מדידות PCT סדרתיות הן כלי רב-עוצמה "
                "מבוסס ראיות להנחיית מתי להתחיל, לשנות או להפסיק טיפול אנטיביוטי. התייעצו תמיד "
                "עם הרופא שלכם במקום להסתמך על חיפושים באינטרנט בלבד.</p>"
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
            heading="प्रोकैल्सीटोनिन (PCT) ब्लड टेस्ट: आपकी रिपोर्ट का क्या मतलब है?",
            body_html=(
                "<p><strong>प्रोकैल्सीटोनिन टेस्ट</strong> एक महत्वपूर्ण "
                "<strong>बैक्टीरियल इंफेक्शन ब्लड टेस्ट</strong> है जिसका उपयोग बैक्टीरियल "
                "इंफेक्शन की गंभीरता का आकलन करने और एंटीबायोटिक थेरेपी को निर्देशित करने के "
                "लिए किया जाता है। प्रोकैल्सीटोनिन (PCT) थायरॉयड ग्रंथि द्वारा उत्पादित "
                "कैल्सीटोनिन का एक प्रीकर्सर प्रोटीन है; स्वस्थ व्यक्तियों में रक्त में "
                "<strong>प्रोकैल्सीटोनिन का स्तर</strong> बेहद कम होता है। गंभीर बैक्टीरियल "
                "इंफेक्शन में — और विशेष रूप से <strong>सेप्सिस</strong> में — लिवर, किडनी, "
                "फेफड़े और मांसपेशी ऊतक सहित कई अंग PCT को रक्तप्रवाह में छोड़ते हैं, जिससे "
                "स्तर नाटकीय रूप से बढ़ जाता है।</p>"
                "<p><strong>PCT ब्लड टेस्ट</strong> बैक्टीरियल इंफेक्शन को वायरल इंफेक्शन से "
                "अलग करने के लिए सबसे मूल्यवान बायोमार्कर में से एक है। वायरल इंफेक्शन में "
                "इंटरफेरॉन-γ PCT संश्लेषण को दबा देता है, जबकि बैक्टीरियल टॉक्सिन और "
                "प्रो-इंफ्लेमेटरी साइटोकाइन PCT उत्पादन को तीव्रता से उत्तेजित करते हैं। यह "
                "गुण प्रोकैल्सीटोनिन को इमरजेंसी विभागों, इंटेंसिव केयर यूनिट (ICU) और "
                "OPD में एंटीबायोटिक स्टीवर्डशिप का एक अनिवार्य साधन बनाता है — एंटीबायोटिक "
                "शुरू करने या बंद करने के निर्णय को दिशा देता है।</p>"
                "<p>इस गाइड में आप <strong>प्रोकैल्सीटोनिन नॉर्मल रेंज</strong>, "
                "<strong>हाई प्रोकैल्सीटोनिन</strong> के कारण और डॉक्टर से कब मिलना चाहिए, "
                "यह जानेंगे। याद रखें कि सही व्याख्या के लिए आपके परिणामों को क्लिनिकल "
                "तस्वीर और अन्य लैब निष्कर्षों के साथ मिलाकर देखना ज़रूरी है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="प्रोकैल्सीटोनिन के सामान्य मान",
            body_html=(
                "<p><strong>प्रोकैल्सीटोनिन नॉर्मल रेंज</strong> आम तौर पर 0.1 ng/mL से "
                "कम होती है। इस स्तर पर मान इंगित करते हैं कि एक महत्वपूर्ण बैक्टीरियल "
                "इंफेक्शन की संभावना बहुत कम है। जैसे-जैसे "
                "<strong>प्रोकैल्सीटोनिन का स्तर</strong> बढ़ता है, बैक्टीरियल इंफेक्शन और "
                "सेप्सिस की संभावना बढ़ती जाती है; चिकित्सक इन थ्रेशोल्ड का उपयोग एंटीबायोटिक "
                "थेरेपी शुरू करने या बंद करने का निर्णय लेने के लिए करते हैं।</p>"
                "<p>नीचे दी गई तालिका में <strong>प्रोकैल्सीटोनिन के स्तर</strong> और उनकी "
                "क्लिनिकल व्याख्या दी गई है:</p>"
                + _PCT_TABLE_HI +
                "<p>ये कट-ऑफ़ मान दिशानिर्देश के रूप में हैं; रोगी की क्लिनिकल स्थिति, "
                "सहरुग्णताएँ और संक्रमण का केंद्र भी मूल्यांकन में शामिल किया जाना चाहिए। "
                "नवजात शिशुओं में जीवन के पहले 48 घंटों में फिज़ियोलॉजिकल PCT वृद्धि हो सकती "
                "है, इसलिए परिणामों की व्याख्या करते समय आयु-विशिष्ट रेफ़रेंस रेंज लागू की "
                "जानी चाहिए।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="हाई प्रोकैल्सीटोनिन के कारण",
            body_html=(
                "<p><strong>हाई प्रोकैल्सीटोनिन</strong> मुख्य रूप से गंभीर बैक्टीरियल "
                "इंफेक्शन का संकेत देता है, लेकिन अन्य क्लिनिकल स्थितियों में भी वृद्धि हो "
                "सकती है। <strong>प्रोकैल्सीटोनिन के स्तर</strong> बढ़ने के प्रमुख कारणों में "
                "शामिल हैं:</p>"
                "<ul>"
                "<li><strong>बैक्टीरियल सेप्सिस और सेप्टिक शॉक:</strong> सेप्सिस में PCT "
                "अपने उच्चतम स्तर पर पहुँचता है। ग्राम-नेगेटिव बैक्टेरिमिया विशेष रूप से "
                "उल्लेखनीय वृद्धि करता है।</li>"
                "<li><strong>बैक्टीरियल निमोनिया:</strong> समुदाय-अधिग्रहित या अस्पताल-"
                "अधिग्रहित बैक्टीरियल निमोनिया PCT बढ़ाता है, जबकि वायरल निमोनिया में यह "
                "आमतौर पर कम रहता है — विभेदक निदान के लिए एक महत्वपूर्ण अंतर।</li>"
                "<li><strong>बैक्टीरियल मेनिनजाइटिस:</strong> बैक्टीरियल मेनिनजाइटिस में PCT "
                "काफ़ी बढ़ता है लेकिन वायरल मेनिनजाइटिस में आमतौर पर कम रहता है।</li>"
                "<li><strong>इंट्रा-एब्डॉमिनल इंफेक्शन:</strong> पेरिटोनाइटिस, एब्सेस और "
                "कोलेसिस्टाइटिस PCT में उल्लेखनीय वृद्धि कर सकते हैं।</li>"
                "<li><strong>यूरिनरी ट्रैक्ट इंफेक्शन (पायलोनेफ्राइटिस):</strong> ऊपरी "
                "मूत्र मार्ग संक्रमण, विशेष रूप से सहवर्ती बैक्टेरिमिया के साथ, PCT बढ़ा "
                "सकता है।</li>"
                "<li><strong>मेजर सर्जरी और ट्रॉमा:</strong> बड़ी सर्जरी या गंभीर आघात के "
                "बाद स्टेराइल इंफ्लेमेशन PCT को क्षणिक रूप से बढ़ा सकता है, हालाँकि स्तर "
                "आमतौर पर 2 ng/mL से कम रहते हैं और तेज़ी से घटते हैं।</li>"
                "<li><strong>गंभीर जलन (बर्न्स):</strong> व्यापक बर्न इंजरी टिश्यू डैमेज और "
                "इंफेक्शन के बढ़े हुए जोखिम के कारण PCT वृद्धि कर सकती है।</li>"
                "</ul>"
                "<p>वायरल इंफेक्शन, ऑटोइम्यून बीमारियों और स्थानीय बैक्टीरियल इंफेक्शन में "
                "PCT आमतौर पर कम रहता है। यह <strong>प्रोकैल्सीटोनिन टेस्ट</strong> को एक "
                "प्रभावी एंटीबायोटिक स्टीवर्डशिप टूल बनाता है जो अनावश्यक एंटीबायोटिक उपयोग "
                "को कम करने में मदद करता है। सीरियल PCT माप उपचार प्रतिक्रिया की निगरानी और "
                "एंटीबायोटिक अवधि को छोटा करने का गोल्ड स्टैंडर्ड है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपको तेज़ बुखार, ठंड लगना, तेज़ धड़कन, तेज़ साँस, लो ब्लड प्रेशर, "
                "भ्रम या सामान्य स्थिति में अचानक गिरावट महसूस हो, तो तुरंत इमरजेंसी विभाग "
                "जाएँ। ये लक्षण <strong>सेप्सिस</strong> का संकेत हो सकते हैं, और "
                "<strong>प्रोकैल्सीटोनिन टेस्ट</strong> के ज़रिए तेज़ मूल्यांकन अत्यंत "
                "महत्वपूर्ण है।</p>"
                "<p>अगर आपके <strong>PCT ब्लड टेस्ट</strong> का रिज़ल्ट बढ़ा हुआ आता है, तो "
                "घबराएँ नहीं लेकिन तुरंत किसी इंफेक्शन विशेषज्ञ या इंटेंसिविस्ट से रिज़ल्ट "
                "साझा करें। <strong>हाई प्रोकैल्सीटोनिन</strong> बैक्टीरियल इंफेक्शन की "
                "गंभीरता और उपचार प्रतिक्रिया का मूल्यांकन करने का एक महत्वपूर्ण संकेतक है। "
                "आपके डॉक्टर ब्लड कल्चर, कम्पलीट ब्लड काउंट, CRP और इमेजिंग स्टडीज़ से "
                "क्लिनिकल तस्वीर स्पष्ट करेंगे।</p>"
                "<p>याद रखें: अकेला PCT मान निदान नहीं है। हालाँकि, सीरियल PCT माप एंटीबायोटिक "
                "थेरेपी कब शुरू करनी, बदलनी या बंद करनी है — इसके लिए एक शक्तिशाली "
                "साक्ष्य-आधारित उपकरण है। इंटरनेट रिसर्च पर निर्भर रहने की बजाय हमेशा अपने "
                "डॉक्टर से सलाह लें।</p>"
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
            heading="اختبار البروكالسيتونين (PCT) في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>يُعدّ <strong>اختبار البروكالسيتونين</strong> من أهم "
                "<strong>تحاليل الدم للعدوى البكتيرية</strong>، ويُستخدم لتقييم شدة العدوى "
                "البكتيرية وتوجيه العلاج بالمضادات الحيوية. البروكالسيتونين (PCT) هو بروتين "
                "سابق للكالسيتونين تُنتجه الغدة الدرقية؛ لدى الأشخاص الأصحاء تكون "
                "<strong>مستويات البروكالسيتونين</strong> في الدم منخفضة للغاية. أثناء العدوى "
                "البكتيرية الشديدة — وخاصة في حالات <strong>الإنتان (تعفن الدم)</strong> — تُطلق "
                "أعضاء متعددة بما فيها الكبد والكلى والرئتان والعضلات PCT في مجرى الدم، مما "
                "يسبب ارتفاعاً حاداً.</p>"
                "<p>يُعتبر <strong>تحليل PCT في الدم</strong> من أثمن المؤشرات الحيوية للتمييز "
                "بين العدوى البكتيرية والعدوى الفيروسية. تُفعّل العدوى الفيروسية "
                "الإنترفيرون-γ الذي يثبّط إنتاج PCT، بينما تحفّز السموم البكتيرية "
                "والسيتوكينات الالتهابية إنتاج PCT بقوة. هذه الخاصية تجعل البروكالسيتونين "
                "أداة أساسية لإدارة المضادات الحيوية في أقسام الطوارئ ووحدات العناية المركزة "
                "والعيادات الخارجية — حيث توجّه قرارات بدء المضادات الحيوية أو إيقافها.</p>"
                "<p>في هذا الدليل ستتعرفون على <strong>المستوى الطبيعي "
                "للبروكالسيتونين</strong>، وأسباب <strong>ارتفاع البروكالسيتونين</strong>، "
                "ومتى يجب طلب الرعاية الطبية. تذكروا أن التفسير الدقيق يتطلب تقييم النتائج "
                "جنباً إلى جنب مع الصورة السريرية والفحوصات المخبرية الأخرى.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية للبروكالسيتونين",
            body_html=(
                "<p>يقع <strong>المستوى الطبيعي للبروكالسيتونين</strong> عادةً تحت "
                "0.1 ng/mL. تشير القيم عند هذا المستوى إلى أن عدوى بكتيرية كبيرة غير مرجّحة "
                "جداً. مع ارتفاع <strong>مستويات البروكالسيتونين</strong> تزداد احتمالية العدوى "
                "البكتيرية والإنتان؛ يعتمد الأطباء على هذه العتبات لتحديد ما إذا كان يجب بدء "
                "العلاج بالمضادات الحيوية أو إيقافه.</p>"
                "<p>يلخّص الجدول أدناه <strong>مستويات البروكالسيتونين</strong> وتفسيرها "
                "السريري:</p>"
                + _PCT_TABLE_AR +
                "<p>تُعتبر هذه القيم الحدّية إرشادية؛ يجب أيضاً مراعاة الحالة السريرية "
                "للمريض والأمراض المصاحبة وبؤرة العدوى. عند حديثي الولادة قد تحدث ارتفاع "
                "فسيولوجي في PCT خلال الـ 48 ساعة الأولى من الحياة، لذا ينبغي تطبيق نطاقات "
                "مرجعية خاصة بالعمر.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب ارتفاع البروكالسيتونين",
            body_html=(
                "<p><strong>ارتفاع البروكالسيتونين</strong> يشير بشكل رئيسي إلى عدوى "
                "بكتيرية شديدة، لكن قد يرتفع في سياقات سريرية أخرى أيضاً. الأسباب الرئيسية "
                "لارتفاع <strong>مستويات البروكالسيتونين</strong> تشمل:</p>"
                "<ul>"
                "<li><strong>الإنتان البكتيري والصدمة الإنتانية:</strong> يصل PCT إلى أعلى "
                "مستوياته في الإنتان. تسبب تجرثم الدم بالبكتيريا سالبة الغرام ارتفاعات "
                "ملحوظة بشكل خاص.</li>"
                "<li><strong>الالتهاب الرئوي البكتيري:</strong> الالتهاب الرئوي البكتيري "
                "المكتسب من المجتمع أو المستشفى يرفع PCT، بينما يبقيه الالتهاب الرئوي "
                "الفيروسي منخفضاً عادةً — تمييز قيّم للتشخيص التفريقي.</li>"
                "<li><strong>التهاب السحايا البكتيري:</strong> يرتفع PCT بشكل ملحوظ في "
                "التهاب السحايا البكتيري لكنه يظل عادةً منخفضاً في الالتهاب الفيروسي.</li>"
                "<li><strong>العدوى داخل البطن:</strong> التهاب الصفاق والخرّاجات والتهاب "
                "المرارة يمكن أن تسبب ارتفاعاً كبيراً في PCT.</li>"
                "<li><strong>عدوى المسالك البولية (التهاب الحويضة والكلية):</strong> عدوى "
                "المسالك البولية العلوية، خاصة مع تجرثم دم مصاحب، يمكن أن ترفع PCT.</li>"
                "<li><strong>الجراحة الكبرى والصدمات:</strong> الالتهاب العقيم بعد الجراحة "
                "الكبرى أو الصدمة الشديدة قد يرفع PCT بشكل عابر، لكن القيم تبقى عادةً أقل "
                "من 2 ng/mL وتنخفض بسرعة.</li>"
                "<li><strong>الحروق الشديدة:</strong> الحروق الواسعة يمكن أن تسبب ارتفاعاً "
                "في PCT بسبب تلف الأنسجة وزيادة خطر العدوى.</li>"
                "</ul>"
                "<p>في العدوى الفيروسية وأمراض المناعة الذاتية والعدوى البكتيرية الموضعية، "
                "يبقى PCT منخفضاً بشكل عام. هذا يجعل <strong>اختبار البروكالسيتونين</strong> "
                "أداة فعّالة لإدارة المضادات الحيوية تساعد في تقليل الاستخدام غير الضروري "
                "للمضادات. القياسات المتسلسلة لـ PCT هي المعيار الذهبي لمراقبة الاستجابة "
                "العلاجية وتقصير مدة العلاج بالمضادات الحيوية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كنتم تعانون من حمى مرتفعة أو قشعريرة أو تسارع في ضربات القلب أو "
                "تنفس سريع أو انخفاض ضغط الدم أو ارتباك أو تدهور مفاجئ في حالتكم العامة، "
                "توجّهوا فوراً إلى قسم الطوارئ. هذه الأعراض قد تشير إلى "
                "<strong>إنتان (تعفن الدم)</strong>، والتقييم السريع عبر "
                "<strong>اختبار البروكالسيتونين</strong> ذو أهمية حيوية.</p>"
                "<p>إذا جاءت نتيجة <strong>تحليل PCT في الدم</strong> مرتفعة، لا تقلقوا لكن "
                "شاركوا النتيجة دون تأخير مع أخصائي أمراض معدية أو طبيب عناية مركزة. "
                "<strong>ارتفاع البروكالسيتونين</strong> مؤشر حاسم لتقييم شدة العدوى البكتيرية "
                "ومراقبة الاستجابة للعلاج. سيستخدم طبيبكم زراعة الدم وتعداد الدم الكامل وCRP "
                "وفحوصات التصوير لتوضيح الصورة السريرية.</p>"
                "<p>تذكّروا: قيمة PCT واحدة ليست تشخيصاً بحد ذاتها. لكن القياسات المتسلسلة "
                "لـ PCT أداة قوية قائمة على الأدلة لتوجيه متى يجب بدء العلاج بالمضادات "
                "الحيوية أو تعديله أو إيقافه. استشيروا دائماً طبيبكم بدلاً من الاعتماد على "
                "بحث الإنترنت فقط.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def get_procalcitonin_sections_by_lang() -> dict:
    """Returns sections dict for Procalcitonin article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_procalcitonin_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Procalcitonin article (all 9 languages, 3 Q&A each)."""
    return {
        "tr": [
            {"question": "Prokalsitonin (PCT) testi nedir?",
             "answer": "Prokalsitonin testi, kandaki PCT düzeyini ölçen bir kan testidir. Bakteriyel enfeksiyonların şiddetini değerlendirmek, bakteriyel enfeksiyonu viral enfeksiyondan ayırt etmek ve antibiyotik tedavisini yönlendirmek için acil servislerde ve yoğun bakım ünitelerinde yaygın olarak kullanılır."},
            {"question": "Prokalsitonin normal değeri kaçtır?",
             "answer": "Sağlıklı bireylerde prokalsitonin düzeyi genellikle 0,1 ng/mL'nin altındadır. 0,25 ng/mL'nin altındaki değerler bakteriyel enfeksiyonun olası olmadığını gösterirken, 0,5 ng/mL üzerindeki değerler bakteriyel enfeksiyonu, 2 ng/mL üzerindeki değerler ise sepsis olasılığını düşündürür."},
            {"question": "Prokalsitonin yüksekliği sepsis mi demektir?",
             "answer": "Her zaman değil, ancak yüksek PCT değerleri ciddi bakteriyel enfeksiyon ve sepsis olasılığını güçlü şekilde düşündürür. Kesin tanı için klinik bulgular, kan kültürü, tam kan sayımı ve CRP gibi diğer testlerle birlikte değerlendirilmelidir. Seri PCT ölçümleri tedaviye yanıtı izlemede altın standarttır."},
        ],
        "en": [
            {"question": "What is a procalcitonin (PCT) test?",
             "answer": "A procalcitonin test is a blood test that measures the level of PCT in the blood. It is widely used in emergency departments and ICUs to assess the severity of bacterial infections, differentiate bacterial from viral infections, and guide antibiotic stewardship decisions."},
            {"question": "What is the normal procalcitonin range?",
             "answer": "In healthy individuals, procalcitonin levels are generally below 0.1 ng/mL. Values below 0.25 ng/mL suggest bacterial infection is unlikely, while levels above 0.5 ng/mL indicate probable bacterial infection, and levels above 2 ng/mL raise concern for sepsis."},
            {"question": "Does high procalcitonin always mean sepsis?",
             "answer": "Not always, but elevated PCT strongly suggests serious bacterial infection or sepsis. A definitive diagnosis requires evaluation alongside clinical findings, blood cultures, complete blood count, and CRP. Serial PCT measurements are the gold standard for monitoring treatment response."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de procalcitonina (PCT)?",
             "answer": "La prueba de procalcitonina es un análisis de sangre que mide el nivel de PCT en la sangre. Se utiliza ampliamente en urgencias y UCI para evaluar la gravedad de las infecciones bacterianas, diferenciarlas de las virales y guiar la gestión antibiótica."},
            {"question": "¿Cuál es el rango normal de procalcitonina?",
             "answer": "En personas sanas, los niveles de procalcitonina están generalmente por debajo de 0,1 ng/mL. Valores inferiores a 0,25 ng/mL sugieren que la infección bacteriana es improbable, mientras que niveles superiores a 0,5 ng/mL indican infección bacteriana probable y por encima de 2 ng/mL plantean sospecha de sepsis."},
            {"question": "¿La procalcitonina alta siempre significa sepsis?",
             "answer": "No siempre, pero una PCT elevada sugiere fuertemente una infección bacteriana grave o sepsis. El diagnóstico definitivo requiere la evaluación conjunta con los hallazgos clínicos, hemocultivos, hemograma y PCR. Las mediciones seriadas de PCT son el estándar de oro para monitorizar la respuesta al tratamiento."},
        ],
        "de": [
            {"question": "Was ist ein Procalcitonin (PCT)-Test?",
             "answer": "Ein Procalcitonin-Test ist eine Blutuntersuchung, die den PCT-Spiegel im Blut misst. Er wird in Notaufnahmen und auf Intensivstationen häufig eingesetzt, um den Schweregrad bakterieller Infektionen zu beurteilen, bakterielle von viralen Infektionen zu unterscheiden und Antibiotic-Stewardship-Entscheidungen zu leiten."},
            {"question": "Was sind die Procalcitonin-Normalwerte?",
             "answer": "Bei gesunden Personen liegt der Procalcitonin-Spiegel in der Regel unter 0,1 ng/mL. Werte unter 0,25 ng/mL deuten darauf hin, dass eine bakterielle Infektion unwahrscheinlich ist, während Werte über 0,5 ng/mL eine wahrscheinliche bakterielle Infektion und Werte über 2 ng/mL den Verdacht auf Sepsis nahelegen."},
            {"question": "Bedeutet erhöhtes Procalcitonin immer eine Sepsis?",
             "answer": "Nicht immer, aber ein erhöhter PCT-Wert weist stark auf eine schwere bakterielle Infektion oder Sepsis hin. Eine definitive Diagnose erfordert die Bewertung zusammen mit klinischen Befunden, Blutkulturen, großem Blutbild und CRP. Serielle PCT-Messungen sind der Goldstandard zur Überwachung des Therapieansprechens."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'un test de procalcitonine (PCT) ?",
             "answer": "Le test de procalcitonine est une analyse de sang qui mesure le taux de PCT dans le sang. Il est largement utilisé aux urgences et en réanimation pour évaluer la gravité des infections bactériennes, les différencier des infections virales et guider les décisions de bon usage des antibiotiques."},
            {"question": "Quelles sont les valeurs normales de procalcitonine ?",
             "answer": "Chez les sujets sains, le taux de procalcitonine se situe généralement en dessous de 0,1 ng/mL. Des valeurs inférieures à 0,25 ng/mL suggèrent qu'une infection bactérienne est improbable, tandis que des niveaux supérieurs à 0,5 ng/mL indiquent une infection bactérienne probable et au-delà de 2 ng/mL, un sepsis est suspecté."},
            {"question": "La procalcitonine élevée signifie-t-elle toujours un sepsis ?",
             "answer": "Pas toujours, mais une PCT élevée évoque fortement une infection bactérienne grave ou un sepsis. Le diagnostic définitif nécessite une évaluation conjointe avec les données cliniques, les hémocultures, la NFS et la CRP. Les dosages sériés de PCT constituent la référence pour surveiller la réponse au traitement."},
        ],
        "it": [
            {"question": "Cos'è il test della procalcitonina (PCT)?",
             "answer": "Il test della procalcitonina è un esame del sangue che misura il livello di PCT nel sangue. Viene ampiamente utilizzato nei pronto soccorso e nelle terapie intensive per valutare la gravità delle infezioni batteriche, distinguerle da quelle virali e guidare le decisioni di antimicrobial stewardship."},
            {"question": "Quali sono i valori normali di procalcitonina?",
             "answer": "Nelle persone sane, i livelli di procalcitonina sono generalmente inferiori a 0,1 ng/mL. Valori sotto 0,25 ng/mL indicano che un'infezione batterica è improbabile, mentre livelli sopra 0,5 ng/mL suggeriscono un'infezione batterica probabile e sopra 2 ng/mL destano il sospetto di sepsi."},
            {"question": "La procalcitonina alta significa sempre sepsi?",
             "answer": "Non sempre, ma una PCT elevata suggerisce fortemente un'infezione batterica grave o una sepsi. La diagnosi definitiva richiede la valutazione congiunta con i dati clinici, le emocolture, l'emocromo e la PCR. Le misurazioni seriali della PCT rappresentano il gold standard per monitorare la risposta al trattamento."},
        ],
        "he": [
            {"question": "מהי בדיקת פרוקלציטונין (PCT)?",
             "answer": "בדיקת פרוקלציטונין היא בדיקת דם המודדת את רמת ה-PCT בדם. היא נמצאת בשימוש נרחב בחדרי מיון ויחידות טיפול נמרץ להערכת חומרת זיהומים חיידקיים, להבחנה בין זיהום חיידקי לויראלי ולהנחיית ניהול אנטיביוטי."},
            {"question": "מהו ערך הנורמה של פרוקלציטונין?",
             "answer": "אצל אנשים בריאים רמת הפרוקלציטונין נמצאת בדרך כלל מתחת ל-0.1 ng/mL. ערכים מתחת ל-0.25 ng/mL מרמזים שזיהום חיידקי אינו סביר, בעוד שרמות מעל 0.5 ng/mL מצביעות על זיהום חיידקי סביר ומעל 2 ng/mL מעלות חשד לאלח דם."},
            {"question": "האם פרוקלציטונין גבוה תמיד פירושו אלח דם?",
             "answer": "לא תמיד, אך PCT מוגבר מצביע בחוזקה על זיהום חיידקי חמור או אלח דם. אבחנה סופית דורשת הערכה לצד ממצאים קליניים, תרביות דם, ספירת דם מלאה ו-CRP. מדידות PCT סדרתיות הן תקן הזהב למעקב אחר תגובה לטיפול."},
        ],
        "hi": [
            {"question": "प्रोकैल्सीटोनिन (PCT) टेस्ट क्या है?",
             "answer": "प्रोकैल्सीटोनिन टेस्ट एक ब्लड टेस्ट है जो रक्त में PCT के स्तर को मापता है। इसका उपयोग इमरजेंसी विभागों और ICU में बैक्टीरियल इंफेक्शन की गंभीरता का मूल्यांकन करने, बैक्टीरियल को वायरल इंफेक्शन से अलग करने और एंटीबायोटिक स्टीवर्डशिप निर्णयों का मार्गदर्शन करने के लिए व्यापक रूप से किया जाता है।"},
            {"question": "प्रोकैल्सीटोनिन की नॉर्मल रेंज क्या है?",
             "answer": "स्वस्थ व्यक्तियों में प्रोकैल्सीटोनिन का स्तर आम तौर पर 0.1 ng/mL से कम होता है। 0.25 ng/mL से कम मान बैक्टीरियल इंफेक्शन की असंभावना दर्शाते हैं, जबकि 0.5 ng/mL से ऊपर के स्तर संभावित बैक्टीरियल इंफेक्शन और 2 ng/mL से ऊपर सेप्सिस की आशंका दर्शाते हैं।"},
            {"question": "क्या हाई प्रोकैल्सीटोनिन हमेशा सेप्सिस होता है?",
             "answer": "हमेशा नहीं, लेकिन बढ़ा हुआ PCT गंभीर बैक्टीरियल इंफेक्शन या सेप्सिस की प्रबल संभावना दर्शाता है। निश्चित निदान के लिए क्लिनिकल निष्कर्षों, ब्लड कल्चर, कम्पलीट ब्लड काउंट और CRP के साथ मूल्यांकन आवश्यक है। सीरियल PCT माप उपचार प्रतिक्रिया की निगरानी का गोल्ड स्टैंडर्ड है।"},
        ],
        "ar": [
            {"question": "ما هو اختبار البروكالسيتونين (PCT)؟",
             "answer": "اختبار البروكالسيتونين هو تحليل دم يقيس مستوى PCT في الدم. يُستخدم على نطاق واسع في أقسام الطوارئ ووحدات العناية المركزة لتقييم شدة العدوى البكتيرية، والتمييز بينها وبين العدوى الفيروسية، وتوجيه قرارات إدارة المضادات الحيوية."},
            {"question": "ما هو المستوى الطبيعي للبروكالسيتونين؟",
             "answer": "عند الأشخاص الأصحاء تكون مستويات البروكالسيتونين عادةً أقل من 0.1 ng/mL. القيم أقل من 0.25 ng/mL تشير إلى أن العدوى البكتيرية غير مرجّحة، بينما المستويات فوق 0.5 ng/mL تدل على عدوى بكتيرية محتملة وفوق 2 ng/mL تثير الشبهة بالإنتان."},
            {"question": "هل ارتفاع البروكالسيتونين يعني دائماً إنتاناً؟",
             "answer": "ليس دائماً، لكن ارتفاع PCT يشير بقوة إلى عدوى بكتيرية خطيرة أو إنتان. يتطلب التشخيص النهائي التقييم إلى جانب المعطيات السريرية وزراعة الدم وتعداد الدم الكامل وCRP. القياسات المتسلسلة لـ PCT هي المعيار الذهبي لمراقبة الاستجابة العلاجية."},
        ],
    }
