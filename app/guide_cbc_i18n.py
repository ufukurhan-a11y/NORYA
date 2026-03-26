"""How to Read a CBC — guide page i18n."""
from __future__ import annotations

CBC_GUIDE_SLUGS: dict[str, str] = {
    "en": "guides/how-to-read-cbc",
    "tr": "rehber/hemogram-nasil-okunur",
    "de": "ratgeber/blutbild-lesen",
    "es": "guias/como-leer-hemograma",
    "fr": "guides/comment-lire-nfs",
    "it": "guide/come-leggere-emocromo",
    "he": "guides/how-to-read-cbc",
    "hi": "guides/how-to-read-cbc",
    "ar": "guides/how-to-read-cbc",
}


# ---------------------------------------------------------------------------
# English
# ---------------------------------------------------------------------------
def _en() -> dict:
    return {
        "meta_title": "How to Read a CBC Report | Complete Blood Count Explained | NoryaAI",
        "meta_description": "Learn how to read CBC results step by step. Understand WBC, RBC, hemoglobin, hematocrit, platelets, MCV, MCH, and RDW with plain-language explanations and reference ranges.",
        "badge": "Lab Guide",
        "hero_title": "How to Read a CBC Report",
        "hero_sub": "A complete blood count (CBC) is one of the most common blood tests ordered worldwide. This guide explains how to read CBC results line by line, what abbreviations like WBC, RBC, HGB, HCT, PLT, and MCV mean, and how to make sense of the numbers on your report.",
        "sections": [
            {
                "title": "What is a CBC?",
                "intro": "A complete blood count (CBC) measures the cells that make up your blood: red cells, white cells, and platelets. Doctors use it as a general screening tool to check for infections, anemia, clotting issues, and overall health. It is often part of a routine physical or a first step when investigating symptoms like fatigue, bruising, or recurring infections.",
                "paragraphs": [
                    "Your CBC report typically includes 10–20 individual values. Each one describes a different aspect of your blood — how many cells you have, how large they are, how much hemoglobin they carry, and how varied they are in size.",
                    "The sections below break these down into groups so they are easier to understand.",
                ],
            },
            {
                "title": "White blood cells (WBC)",
                "intro": "White blood cells are part of your immune system. A CBC measures their total count and sometimes breaks them into subtypes (a differential).",
                "markers": [
                    {
                        "name": "White blood cell count",
                        "abbr": "WBC",
                        "desc": "The total number of white blood cells in a given volume of blood. A high count may suggest infection or inflammation; a low count may indicate a weakened immune response. Many temporary factors — stress, exercise, medications — can shift this number.",
                        "range": "4,500–11,000 cells/µL",
                    },
                    {
                        "name": "Neutrophils",
                        "abbr": "NEUT",
                        "desc": "The most common type of white blood cell. Neutrophils are usually the first responders to bacterial infections. Their percentage and absolute count are reported separately.",
                        "range": "40–70% of WBC",
                    },
                    {
                        "name": "Lymphocytes",
                        "abbr": "LYMPH",
                        "desc": "Involved in viral defense and long-term immunity. A rise in lymphocytes can occur with viral infections; a decrease may appear in certain immune conditions.",
                        "range": "20–40% of WBC",
                    },
                ],
            },
            {
                "title": "Red blood cells, hemoglobin, and hematocrit",
                "intro": "Red blood cells carry oxygen from your lungs to the rest of your body. Several CBC values describe their count, their oxygen-carrying capacity, and their proportion in your blood.",
                "markers": [
                    {
                        "name": "Red blood cell count",
                        "abbr": "RBC",
                        "desc": "The total number of red blood cells per volume of blood. Values vary by sex and age. A low count is one sign that may be associated with anemia; a high count may be seen in dehydration or other conditions.",
                        "range": "4.5–5.5 million cells/µL (men) · 4.0–5.0 (women)",
                    },
                    {
                        "name": "Hemoglobin",
                        "abbr": "HGB / Hb",
                        "desc": "The protein inside red blood cells that binds oxygen. Hemoglobin is one of the most commonly checked values in a CBC. Low hemoglobin is a key marker associated with anemia.",
                        "range": "13.5–17.5 g/dL (men) · 12.0–16.0 g/dL (women)",
                    },
                    {
                        "name": "Hematocrit",
                        "abbr": "HCT",
                        "desc": "The percentage of your blood volume that is made up of red blood cells. It rises with dehydration and falls with blood loss or reduced red cell production.",
                        "range": "38.3–48.6% (men) · 35.5–44.9% (women)",
                    },
                ],
            },
            {
                "title": "Platelets",
                "intro": "Platelets are small cell fragments that help your blood clot. A CBC reports their count and sometimes their average size.",
                "markers": [
                    {
                        "name": "Platelet count",
                        "abbr": "PLT",
                        "desc": "The number of platelets per volume of blood. A low count (thrombocytopenia) can increase bleeding risk; a high count (thrombocytosis) may be reactive or, less commonly, related to a bone marrow condition.",
                        "range": "150,000–400,000 /µL",
                    },
                    {
                        "name": "Mean platelet volume",
                        "abbr": "MPV",
                        "desc": "The average size of your platelets. Larger platelets are often younger and may indicate that your body is producing them faster to replace ones being used up.",
                        "range": "7.5–12.0 fL",
                    },
                ],
            },
            {
                "title": "Red cell indices",
                "intro": "Indices describe the size and hemoglobin content of your red blood cells. They help characterize the type of anemia if one is present.",
                "markers": [
                    {
                        "name": "Mean corpuscular volume",
                        "abbr": "MCV",
                        "desc": "The average size of a single red blood cell. A high MCV (macrocytic) can be associated with B12 or folate issues; a low MCV (microcytic) can be associated with iron-related conditions.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "Mean corpuscular hemoglobin",
                        "abbr": "MCH",
                        "desc": "The average amount of hemoglobin in a single red blood cell. It usually tracks with MCV — small cells carry less hemoglobin, large cells carry more.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "Mean corpuscular hemoglobin concentration",
                        "abbr": "MCHC",
                        "desc": "The average concentration of hemoglobin within red blood cells. Low MCHC suggests the cells are paler than usual (hypochromic).",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "Red cell distribution width",
                        "abbr": "RDW",
                        "desc": "Measures how much variation there is in the size of your red blood cells. A high RDW means your cells vary more in size, which can be an early sign that something is affecting red cell production.",
                        "range": "11.5–14.5%",
                    },
                ],
            },
            {
                "title": "What reference ranges actually mean",
                "intro": None,
                "paragraphs": [
                    "Reference ranges represent the middle 95% of results from a healthy population tested by that specific lab. They are not absolute cutoffs for health or disease. A value slightly outside the range does not automatically mean something is wrong, and a value inside the range does not guarantee everything is fine.",
                    "Ranges vary between labs because of differences in equipment, reagents, and the population samples used to establish them. Age, sex, altitude, hydration, and even the time of day can influence your results. This is why comparing your numbers against a single “normal” value from the internet can be misleading.",
                    "The most useful way to interpret your CBC is in context: how do your values compare to your own previous results, and what does your doctor think given your symptoms and history?",
                ],
            },
            {
                "title": "Why one result alone is not the whole picture",
                "intro": None,
                "points": [
                    {
                        "title": "Values interact with each other",
                        "desc": "A low hemoglobin means more when MCV is also low (suggesting a possible iron-related cause) than when MCV is normal. Individual numbers gain meaning from the pattern they form together.",
                    },
                    {
                        "title": "Temporary factors matter",
                        "desc": "Dehydration, a recent meal, intense exercise, stress, or medication can shift your numbers for hours or days. One slightly out-of-range result is often repeated before any conclusion is drawn.",
                    },
                    {
                        "title": "Trends are more informative than snapshots",
                        "desc": "A hemoglobin of 12.0 g/dL means something different if your last three results were 14.5, 13.8, and 12.8 than if they have been stable around 12.0 for years.",
                    },
                    {
                        "title": "Clinical context is essential",
                        "desc": "Your doctor interprets your CBC alongside your symptoms, medical history, physical exam, and other tests. A lab report alone — without that context — can be misleading.",
                    },
                ],
            },
            {
                "title": "When people want a clearer summary",
                "intro": None,
                "paragraphs": [
                    "Many people receive a CBC report and feel lost. The abbreviations are unfamiliar, the reference ranges are hard to compare, and there is no plain-language explanation included.",
                    "Some look up individual values online, but that gives scattered, generic answers without showing how the numbers relate to each other. Others wait for their doctor appointment, which may be days or weeks away.",
                    "A structured tool like NoryaAI can help bridge that gap. It reads your report, organizes the values into categories, flags anything outside the reference range, and provides plain-language context — all in a single, downloadable summary you can review on your own time or bring to your next appointment.",
                    "It does not replace your doctor. But it can make the conversation more productive.",
                ],
            },
        ],
        "mid_cta_title": "Have CBC results you want explained?",
        "mid_cta_sub": "Upload your report and get a structured CBC summary with plain-language explanations, flagged markers, and a health score.",
        "mid_cta_primary": "Upload your report",
        "mid_cta_secondary": "See a sample report",
        "faqs": [
            {
                "q": "What does CBC stand for?",
                "a": "CBC stands for complete blood count. It is a routine blood test that measures the cells in your blood — red blood cells, white blood cells, and platelets — along with related values like hemoglobin, hematocrit, and cell indices.",
            },
            {
                "q": "How do I read CBC results line by line?",
                "a": "Start with the main groups: white blood cells, red blood cells, hemoglobin and hematocrit, platelets, and red cell indices like MCV and RDW. Then compare each value with the reference range shown by your lab. The pattern across several CBC markers is usually more meaningful than one value on its own.",
            },
            {
                "q": "What does it mean if one value is slightly out of range?",
                "a": "A single value slightly outside the reference range is common and not always a cause for concern. Temporary factors like hydration, exercise, or stress can shift your numbers. Doctors typically look at the overall pattern and may repeat the test before drawing conclusions.",
            },
            {
                "q": "Can NoryaAI interpret my CBC results?",
                "a": "NoryaAI can read your CBC report, organize each marker with its reference range, flag values outside normal limits, and provide plain-language explanations. It does not diagnose conditions — it structures your results so they are easier to understand.",
            },
            {
                "q": "Is this guide a substitute for medical advice?",
                "a": "No. This guide is educational and intended to help you understand the components of a CBC report. It does not diagnose or recommend treatment. Always consult a qualified healthcare professional for medical decisions about your results.",
            },
            {
                "q": "Why do reference ranges differ between labs?",
                "a": "Labs use different equipment, reagents, and population samples to establish their ranges. Factors like age, sex, and geographic location also influence what is considered “normal.” This is why the same result may be flagged at one lab but considered within range at another.",
            },
        ],
        "cta_title": "Ready to make sense of your CBC results?",
        "cta_sub": "Upload your report and get a structured, easy-to-read CBC summary with reference ranges and plain-language explanations in minutes.",
        "cta_primary": "Upload and analyze now",
        "cta_secondary": "View pricing",
        "internal_links": [
            {"label": "Blood Test Results Explained", "path": "/en/blood-test-results-explained"},
            {"label": "Blood Test Interpretation Online", "path": "/en/blood-test-results"},
            {"label": "Upload Results", "path": "/en/upload-blood-test-results"},
            {"label": "AI Blood Test Analyzer", "path": "/en/ai-blood-test-analyzer"},
            {"label": "Pricing", "path": "/pricing"},
            {"label": "How it works", "path": "/how-it-works"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# Turkish
# ---------------------------------------------------------------------------
def _tr() -> dict:
    return {
        "meta_title": "Hemogram Nasıl Okunur — Tam Kan Sayımı Rehberi | NoryaAI",
        "meta_description": "Hemogram (tam kan sayımı) raporunuzu nasıl okuyacağınızı öğrenin. WBC, RBC, hemoglobin, hematokrit, trombosit ve indeksler — referans aralıklarıyla birlikte sade bir dille açıklanıyor.",
        "badge": "Laboratuvar Rehberi",
        "hero_title": "Hemogram Nasıl Okunur",
        "hero_sub": "Tam kan sayımı, dünya genelinde en sık istenen kan testlerinden biridir. Bu rehber her bir bileşeni adım adım açıklıyor — neyi ölçtüğünü, kısaltmaların ne anlama geldiğini ve raporunuzdaki sayıları nasıl yorumlayacağınızı.",
        "sections": [
            {
                "title": "Hemogram (CBC) nedir?",
                "intro": "Tam kan sayımı (CBC/hemogram), kanınızı oluşturan hücreleri ölçer: kırmızı kan hücreleri, beyaz kan hücreleri ve trombositler. Doktorlar bunu enfeksiyonları, anemiyi, pıhtılaşma sorunlarını ve genel sağlığı kontrol etmek için genel bir tarama aracı olarak kullanır. Genellikle rutin muayenenin bir parçasıdır veya yorgunluk, morarma ya da tekrarlayan enfeksiyonlar gibi belirtiler araştırılırken ilk adım olarak istenir.",
                "paragraphs": [
                    "Hemogram raporunuz genellikle 10–20 ayrı değer içerir. Her biri kanınızın farklı bir yönünü tanımlar — kaç hücreniz olduğunu, ne kadar büyük olduklarını, ne kadar hemoglobin taşıdıklarını ve boyut olarak ne kadar farklılık gösterdiklerini.",
                    "Aşağıdaki bölümler bunları daha kolay anlaşılması için gruplara ayırır.",
                ],
            },
            {
                "title": "Beyaz kan hücreleri (WBC)",
                "intro": "Beyaz kan hücreleri bağışıklık sisteminizin bir parçasıdır. Hemogram toplam sayılarını ölçer ve bazen bunları alt tiplere ayırır (diferansiyel).",
                "markers": [
                    {
                        "name": "Beyaz kan hücresi sayısı",
                        "abbr": "WBC",
                        "desc": "Belirli bir kan hacmindeki toplam beyaz kan hücresi sayısı. Yüksek bir sayı enfeksiyon veya iltihabı düşündürebilir; düşük bir sayı bağışıklık yanıtının zayıfladığını gösterebilir. Stres, egzersiz, ilaçlar gibi birçok geçici faktör bu sayıyı değiştirebilir.",
                        "range": "4.500–11.000 hücre/µL",
                    },
                    {
                        "name": "Nötrofiller",
                        "abbr": "NEUT",
                        "desc": "En yaygın beyaz kan hücresi türü. Nötrofiller genellikle bakteriyel enfeksiyonlara ilk müdahale edenlerdir. Yüzdeleri ve mutlak sayıları ayrı ayrı raporlanır.",
                        "range": "WBC'nin %40–70'i",
                    },
                    {
                        "name": "Lenfositler",
                        "abbr": "LYMPH",
                        "desc": "Viral savunma ve uzun vadeli bağışıklıkta rol oynar. Viral enfeksiyonlarda lenfosit artışı görülebilir; bazı bağışıklık durumlarında azalma olabilir.",
                        "range": "WBC'nin %20–40'ı",
                    },
                ],
            },
            {
                "title": "Kırmızı kan hücreleri, hemoglobin ve hematokrit",
                "intro": "Kırmızı kan hücreleri akciğerlerinizden vücudunuzun geri kalanına oksijen taşır. Birkaç hemogram değeri bunların sayısını, oksijen taşıma kapasitelerini ve kanınızdaki oranlarını tanımlar.",
                "markers": [
                    {
                        "name": "Kırmızı kan hücresi sayısı",
                        "abbr": "RBC",
                        "desc": "Birim kan hacmindeki toplam kırmızı kan hücresi sayısı. Değerler cinsiyete ve yaşa göre değişir. Düşük sayı anemi ile ilişkilendirilebilecek bir bulgu olabilir; yüksek sayı dehidratasyon veya diğer durumlarda görülebilir.",
                        "range": "4,5–5,5 milyon hücre/µL (erkek) · 4,0–5,0 (kadın)",
                    },
                    {
                        "name": "Hemoglobin",
                        "abbr": "HGB / Hb",
                        "desc": "Kırmızı kan hücrelerinin içindeki oksijen bağlayan protein. Hemoglobin, hemogramda en sık kontrol edilen değerlerden biridir. Düşük hemoglobin, anemi ile ilişkilendirilen önemli bir belirteçtir.",
                        "range": "13,5–17,5 g/dL (erkek) · 12,0–16,0 g/dL (kadın)",
                    },
                    {
                        "name": "Hematokrit",
                        "abbr": "HCT",
                        "desc": "Kan hacminizin yüzde kaçının kırmızı kan hücrelerinden oluştuğunu gösterir. Dehidratasyonda yükselir, kan kaybında veya kırmızı hücre üretiminin azalmasında düşer.",
                        "range": "%38,3–48,6 (erkek) · %35,5–44,9 (kadın)",
                    },
                ],
            },
            {
                "title": "Trombositler",
                "intro": "Trombositler, kanınızın pıhtılaşmasına yardımcı olan küçük hücre parçacıklarıdır. Hemogram bunların sayısını ve bazen ortalama boyutlarını raporlar.",
                "markers": [
                    {
                        "name": "Trombosit sayısı",
                        "abbr": "PLT",
                        "desc": "Birim kan hacmindeki trombosit sayısı. Düşük sayı (trombositopeni) kanama riskini artırabilir; yüksek sayı (trombositoz) reaktif olabilir veya daha nadir olarak kemik iliği durumu ile ilişkili olabilir.",
                        "range": "150.000–400.000 /µL",
                    },
                    {
                        "name": "Ortalama trombosit hacmi",
                        "abbr": "MPV",
                        "desc": "Trombositlerinizin ortalama boyutu. Daha büyük trombositler genellikle daha genç olup vücudunuzun kullanılanların yerine daha hızlı ürettiğini gösterebilir.",
                        "range": "7,5–12,0 fL",
                    },
                ],
            },
            {
                "title": "Kırmızı hücre indeksleri",
                "intro": "İndeksler, kırmızı kan hücrelerinizin boyutunu ve hemoglobin içeriğini tanımlar. Anemi varsa tipini belirlemeye yardımcı olurlar.",
                "markers": [
                    {
                        "name": "Ortalama eritrosit hacmi",
                        "abbr": "MCV",
                        "desc": "Tek bir kırmızı kan hücresinin ortalama boyutu. Yüksek MCV (makrositik) B12 veya folat sorunlarıyla ilişkilendirilebilir; düşük MCV (mikrositik) demir ile ilgili durumlarla ilişkilendirilebilir.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "Ortalama eritrosit hemoglobini",
                        "abbr": "MCH",
                        "desc": "Tek bir kırmızı kan hücresindeki ortalama hemoglobin miktarı. Genellikle MCV ile paralel seyreder — küçük hücreler daha az, büyük hücreler daha fazla hemoglobin taşır.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "Ortalama eritrosit hemoglobin konsantrasyonu",
                        "abbr": "MCHC",
                        "desc": "Kırmızı kan hücrelerindeki ortalama hemoglobin konsantrasyonu. Düşük MCHC, hücrelerin normalden daha soluk olduğunu (hipokromik) düşündürür.",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "Kırmızı hücre dağılım genişliği",
                        "abbr": "RDW",
                        "desc": "Kırmızı kan hücrelerinizin boyutundaki varyasyonu ölçer. Yüksek RDW, hücrelerinizin boyut olarak daha fazla farklılık gösterdiği anlamına gelir; bu, kırmızı hücre üretimini etkileyen bir durumun erken belirtisi olabilir.",
                        "range": "%11,5–14,5",
                    },
                ],
            },
            {
                "title": "Referans aralıkları gerçekte ne anlama gelir",
                "intro": None,
                "paragraphs": [
                    "Referans aralıkları, ilgili laboratuvar tarafından test edilen sağlıklı bir popülasyonun sonuçlarının ortadaki %95'ini temsil eder. Sağlık veya hastalık için mutlak kesim noktaları değildir. Aralığın biraz dışında bir değer otomatik olarak bir sorun olduğu anlamına gelmez ve aralık içinde bir değer her şeyin iyi olduğunu garanti etmez.",
                    "Aralıklar laboratuvarlar arasında farklılık gösterir çünkü kullanılan ekipman, reaktifler ve bunları belirlemek için kullanılan popülasyon örnekleri farklıdır. Yaş, cinsiyet, rakım, hidrasyon ve hatta günün saati bile sonuçlarınızı etkileyebilir. Bu yüzden sayılarınızı internetten alınan tek bir \"normal\" değerle karşılaştırmak yanıltıcı olabilir.",
                    "Hemogramınızı yorumlamanın en yararlı yolu bağlam içinde değerlendirmektir: değerleriniz kendi önceki sonuçlarınızla nasıl karşılaştırılıyor ve doktorunuz belirtileriniz ve geçmişiniz göz önüne alındığında ne düşünüyor?",
                ],
            },
            {
                "title": "Tek bir sonuç neden tüm resmi göstermez",
                "intro": None,
                "points": [
                    {
                        "title": "Değerler birbirleriyle etkileşim halindedir",
                        "desc": "Düşük hemoglobin, MCV de düşükse (olası bir demir ilişkili nedeni düşündüren) MCV normal olduğundakinden daha anlamlıdır. Bireysel sayılar, birlikte oluşturdukları örüntüden anlam kazanır.",
                    },
                    {
                        "title": "Geçici faktörler önemlidir",
                        "desc": "Dehidratasyon, yakın zamanda yenen bir yemek, yoğun egzersiz, stres veya ilaçlar sayılarınızı saatlerce veya günlerce değiştirebilir. Biraz aralık dışı olan bir sonuç, herhangi bir sonuca varılmadan önce genellikle tekrarlanır.",
                    },
                    {
                        "title": "Trendler anlık görüntülerden daha bilgilendiricidir",
                        "desc": "12,0 g/dL hemoglobin, son üç sonucunuz 14,5, 13,8 ve 12,8 ise yıllardır yaklaşık 12,0 civarında stabil olmasından farklı bir anlam taşır.",
                    },
                    {
                        "title": "Klinik bağlam esastır",
                        "desc": "Doktorunuz hemogramınızı belirtileriniz, tıbbi geçmişiniz, fizik muayeneniz ve diğer testlerinizle birlikte yorumlar. Tek başına bir laboratuvar raporu — bu bağlam olmadan — yanıltıcı olabilir.",
                    },
                ],
            },
            {
                "title": "Daha net bir özet isteyenler için",
                "intro": None,
                "paragraphs": [
                    "Birçok kişi hemogram raporunu alır ve ne anlama geldiğini anlayamaz. Kısaltmalar tanıdık değildir, referans aralıklarını karşılaştırmak zordur ve sade bir dilde açıklama yoktur.",
                    "Bazıları internette tek tek değerleri arar, ancak bu sayıların birbirleriyle nasıl ilişkili olduğunu göstermeden dağınık, genel yanıtlar verir. Diğerleri günler veya haftalar sonra olabilecek doktor randevusunu bekler.",
                    "NoryaAI gibi yapılandırılmış bir araç bu boşluğu doldurmaya yardımcı olabilir. Raporunuzu okur, değerleri kategorilere ayırır, referans aralığının dışındaki her şeyi işaretler ve sade bir dilde bağlam sağlar — tümü tek bir indirilebilir özette, kendi zamanınızda inceleyebilir veya bir sonraki randevunuza götürebilirsiniz.",
                    "Doktorunuzun yerini almaz. Ancak görüşmeyi daha verimli hale getirebilir.",
                ],
            },
        ],
        "mid_cta_title": "Anlamak istediğiniz bir hemogram raporunuz var mı?",
        "mid_cta_sub": "Yükleyin, sade dilde açıklamalar, işaretlenmiş belirteçler ve sağlık puanı içeren yapılandırılmış bir özet alın.",
        "mid_cta_primary": "Raporunuzu yükleyin",
        "mid_cta_secondary": "Örnek rapor görün",
        "faqs": [
            {
                "q": "CBC (hemogram) ne anlama gelir?",
                "a": "CBC, tam kan sayımı (complete blood count) anlamına gelir. Kanınızdaki hücreleri — kırmızı kan hücreleri, beyaz kan hücreleri ve trombositler — hemoglobin, hematokrit ve hücre indeksleri gibi ilişkili değerlerle birlikte ölçen rutin bir kan testidir.",
            },
            {
                "q": "Ne sıklıkta hemogram yaptırmalıyım?",
                "a": "Evrensel bir takvim yoktur. Birçok doktor yıllık kontrollere hemogram ekler. Belirtileriniz, kronik bir hastalığınız varsa veya kan hücresi sayısını etkileyen ilaçlar kullanıyorsanız daha sık istenebilir. Doktorunuz sizin için doğru sıklığı önerecektir.",
            },
            {
                "q": "Bir değer biraz aralık dışındaysa ne anlama gelir?",
                "a": "Referans aralığının biraz dışındaki tek bir değer yaygındır ve her zaman endişe sebebi değildir. Hidrasyon, egzersiz veya stres gibi geçici faktörler sayılarınızı değiştirebilir. Doktorlar genellikle genel örüntüye bakar ve sonuç çıkarmadan önce testi tekrarlayabilir.",
            },
            {
                "q": "NoryaAI hemogram sonuçlarımı yorumlayabilir mi?",
                "a": "NoryaAI hemogram raporunuzu okuyabilir, her belirteci referans aralığıyla birlikte düzenleyebilir, normal sınırların dışındaki değerleri işaretleyebilir ve sade dilde açıklamalar sunabilir. Hastalık teşhisi koymaz — sonuçlarınızı daha kolay anlaşılır hale getirir.",
            },
            {
                "q": "Bu rehber tıbbi tavsiye yerine geçer mi?",
                "a": "Hayır. Bu rehber eğitim amaçlıdır ve hemogram rapor bileşenlerini anlamanıza yardımcı olmayı amaçlar. Teşhis koymaz veya tedavi önermez. Sonuçlarınızla ilgili tıbbi kararlar için her zaman nitelikli bir sağlık uzmanına danışın.",
            },
            {
                "q": "Referans aralıkları neden laboratuvarlar arasında farklılık gösterir?",
                "a": "Laboratuvarlar aralıklarını belirlemek için farklı ekipman, reaktif ve popülasyon örnekleri kullanır. Yaş, cinsiyet ve coğrafi konum gibi faktörler de \"normal\" kabul edileni etkiler. Bu yüzden aynı sonuç bir laboratuvarda işaretlenebilirken diğerinde aralık içinde kabul edilebilir.",
            },
        ],
        "cta_title": "Hemogramınızı anlamaya hazır mısınız?",
        "cta_sub": "Raporunuzu yükleyin ve dakikalar içinde yapılandırılmış, okunması kolay bir özet alın.",
        "cta_primary": "Yükle ve analiz et",
        "cta_secondary": "Fiyatlandırmayı gör",
        "internal_links": [
            {"label": "Kan Tahlili Sonuçları Açıklama", "path": "/tr/kan-tahlili-sonuclari-aciklama"},
            {"label": "Sonuçları Yükle", "path": "/tr/kan-tahlili-yukle"},
            {"label": "Yapay Zeka Kan Tahlili Analizi", "path": "/tr/yapay-zeka-kan-tahlili-analizi"},
            {"label": "Fiyatlandırma", "path": "/pricing"},
            {"label": "Nasıl çalışır", "path": "/how-it-works"},
            {"label": "Blog", "path": "/tr/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------
def _de() -> dict:
    return {
        "meta_title": "Blutbild lesen — Großes Blutbild einfach erklärt | NoryaAI",
        "meta_description": "Erfahren Sie, wie Sie ein großes Blutbild (CBC) lesen. WBC, RBC, Hämoglobin, Hämatokrit, Thrombozyten und Indizes — mit Referenzbereichen verständlich erklärt.",
        "badge": "Labor-Ratgeber",
        "hero_title": "Blutbild lesen",
        "hero_sub": "Das große Blutbild gehört zu den am häufigsten angeordneten Blutuntersuchungen weltweit. Dieser Ratgeber erklärt jede Komponente — was sie misst, was die Abkürzungen bedeuten und wie Sie die Zahlen in Ihrem Befund verstehen.",
        "sections": [
            {
                "title": "Was ist ein Blutbild (CBC)?",
                "intro": "Ein großes Blutbild (CBC) misst die Zellen in Ihrem Blut: rote Blutkörperchen, weiße Blutkörperchen und Thrombozyten. Ärzte nutzen es als allgemeines Screening-Instrument, um Infektionen, Anämie, Gerinnungsprobleme und den allgemeinen Gesundheitszustand zu überprüfen. Es ist oft Teil einer Routineuntersuchung oder ein erster Schritt bei der Abklärung von Symptomen wie Müdigkeit, Blutergüssen oder wiederkehrenden Infektionen.",
                "paragraphs": [
                    "Ihr Blutbild umfasst in der Regel 10–20 Einzelwerte. Jeder beschreibt einen anderen Aspekt Ihres Blutes — wie viele Zellen vorhanden sind, wie groß sie sind, wie viel Hämoglobin sie tragen und wie unterschiedlich sie in der Größe sind.",
                    "Die folgenden Abschnitte gliedern diese in Gruppen, damit sie leichter zu verstehen sind.",
                ],
            },
            {
                "title": "Weiße Blutkörperchen (WBC)",
                "intro": "Weiße Blutkörperchen sind Teil Ihres Immunsystems. Ein Blutbild misst ihre Gesamtzahl und unterteilt sie manchmal in Untertypen (Differentialblutbild).",
                "markers": [
                    {
                        "name": "Leukozytenzahl",
                        "abbr": "WBC",
                        "desc": "Die Gesamtzahl der weißen Blutkörperchen in einem bestimmten Blutvolumen. Ein hoher Wert kann auf eine Infektion oder Entzündung hindeuten; ein niedriger Wert kann auf eine geschwächte Immunantwort hinweisen. Viele vorübergehende Faktoren — Stress, Bewegung, Medikamente — können diesen Wert beeinflussen.",
                        "range": "4.500–11.000 Zellen/µL",
                    },
                    {
                        "name": "Neutrophile",
                        "abbr": "NEUT",
                        "desc": "Der häufigste Typ weißer Blutkörperchen. Neutrophile sind in der Regel die ersten Helfer bei bakteriellen Infektionen. Ihr prozentualer Anteil und ihre absolute Zahl werden separat angegeben.",
                        "range": "40–70 % der WBC",
                    },
                    {
                        "name": "Lymphozyten",
                        "abbr": "LYMPH",
                        "desc": "Beteiligt an der Virenabwehr und der Langzeitimmunität. Ein Anstieg der Lymphozyten kann bei Virusinfektionen auftreten; ein Rückgang kann bei bestimmten Immunerkrankungen vorkommen.",
                        "range": "20–40 % der WBC",
                    },
                ],
            },
            {
                "title": "Rote Blutkörperchen, Hämoglobin und Hämatokrit",
                "intro": "Rote Blutkörperchen transportieren Sauerstoff von der Lunge in den Rest des Körpers. Mehrere Blutwerte beschreiben ihre Anzahl, ihre Sauerstofftransportkapazität und ihren Anteil im Blut.",
                "markers": [
                    {
                        "name": "Erythrozytenzahl",
                        "abbr": "RBC",
                        "desc": "Die Gesamtzahl der roten Blutkörperchen pro Blutvolumen. Die Werte variieren nach Geschlecht und Alter. Ein niedriger Wert kann ein Hinweis auf eine Anämie sein; ein hoher Wert kann bei Dehydration oder anderen Zuständen auftreten.",
                        "range": "4,5–5,5 Mio. Zellen/µL (Männer) · 4,0–5,0 (Frauen)",
                    },
                    {
                        "name": "Hämoglobin",
                        "abbr": "HGB / Hb",
                        "desc": "Das Protein in den roten Blutkörperchen, das Sauerstoff bindet. Hämoglobin ist einer der am häufigsten überprüften Werte im Blutbild. Niedriges Hämoglobin ist ein wichtiger Marker, der mit Anämie in Verbindung gebracht wird.",
                        "range": "13,5–17,5 g/dL (Männer) · 12,0–16,0 g/dL (Frauen)",
                    },
                    {
                        "name": "Hämatokrit",
                        "abbr": "HCT",
                        "desc": "Der prozentuale Anteil Ihres Blutvolumens, der aus roten Blutkörperchen besteht. Er steigt bei Dehydration und sinkt bei Blutverlust oder verminderter Produktion roter Blutkörperchen.",
                        "range": "38,3–48,6 % (Männer) · 35,5–44,9 % (Frauen)",
                    },
                ],
            },
            {
                "title": "Thrombozyten",
                "intro": "Thrombozyten sind kleine Zellfragmente, die bei der Blutgerinnung helfen. Ein Blutbild gibt ihre Anzahl und manchmal ihre durchschnittliche Größe an.",
                "markers": [
                    {
                        "name": "Thrombozytenzahl",
                        "abbr": "PLT",
                        "desc": "Die Anzahl der Thrombozyten pro Blutvolumen. Ein niedriger Wert (Thrombozytopenie) kann das Blutungsrisiko erhöhen; ein hoher Wert (Thrombozytose) kann reaktiv sein oder, seltener, mit einer Knochenmarkerkrankung zusammenhängen.",
                        "range": "150.000–400.000 /µL",
                    },
                    {
                        "name": "Mittleres Thrombozytenvolumen",
                        "abbr": "MPV",
                        "desc": "Die durchschnittliche Größe Ihrer Thrombozyten. Größere Thrombozyten sind oft jünger und können darauf hindeuten, dass Ihr Körper sie schneller produziert, um verbrauchte zu ersetzen.",
                        "range": "7,5–12,0 fL",
                    },
                ],
            },
            {
                "title": "Erythrozytenindizes",
                "intro": "Indizes beschreiben die Größe und den Hämoglobingehalt Ihrer roten Blutkörperchen. Sie helfen, die Art einer Anämie zu bestimmen, falls eine vorliegt.",
                "markers": [
                    {
                        "name": "Mittleres korpuskuläres Volumen",
                        "abbr": "MCV",
                        "desc": "Die durchschnittliche Größe eines einzelnen roten Blutkörperchens. Ein hoher MCV (makrozytär) kann mit B12- oder Folatproblemen in Verbindung stehen; ein niedriger MCV (mikrozytär) kann mit eisenbedingten Zuständen zusammenhängen.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "Mittleres korpuskuläres Hämoglobin",
                        "abbr": "MCH",
                        "desc": "Die durchschnittliche Hämoglobinmenge in einem einzelnen roten Blutkörperchen. Sie korreliert in der Regel mit dem MCV — kleine Zellen tragen weniger Hämoglobin, große Zellen mehr.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "Mittlere korpuskuläre Hämoglobinkonzentration",
                        "abbr": "MCHC",
                        "desc": "Die durchschnittliche Hämoglobinkonzentration in den roten Blutkörperchen. Ein niedriger MCHC deutet darauf hin, dass die Zellen blasser als üblich sind (hypochrom).",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "Erythrozytenverteilungsbreite",
                        "abbr": "RDW",
                        "desc": "Misst die Größenvariation Ihrer roten Blutkörperchen. Ein hoher RDW bedeutet, dass Ihre Zellen stärker in der Größe variieren, was ein frühes Zeichen sein kann, dass etwas die Produktion roter Blutkörperchen beeinflusst.",
                        "range": "11,5–14,5 %",
                    },
                ],
            },
            {
                "title": "Was Referenzbereiche wirklich bedeuten",
                "intro": None,
                "paragraphs": [
                    "Referenzbereiche stellen die mittleren 95 % der Ergebnisse einer gesunden Population dar, die von dem jeweiligen Labor getestet wurde. Sie sind keine absoluten Grenzwerte für Gesundheit oder Krankheit. Ein Wert leicht außerhalb des Bereichs bedeutet nicht automatisch, dass etwas nicht stimmt, und ein Wert innerhalb des Bereichs garantiert nicht, dass alles in Ordnung ist.",
                    "Die Bereiche variieren zwischen Laboren aufgrund unterschiedlicher Geräte, Reagenzien und Populationsproben. Alter, Geschlecht, Höhenlage, Hydration und sogar die Tageszeit können Ihre Ergebnisse beeinflussen. Deshalb kann der Vergleich Ihrer Werte mit einem einzelnen \u201Enormalen\u201C Wert aus dem Internet irreführend sein.",
                    "Der nützlichste Weg, Ihr Blutbild zu interpretieren, ist im Kontext: Wie verhalten sich Ihre Werte im Vergleich zu Ihren eigenen früheren Ergebnissen, und was denkt Ihr Arzt angesichts Ihrer Symptome und Vorgeschichte?",
                ],
            },
            {
                "title": "Warum ein einzelnes Ergebnis nicht das ganze Bild zeigt",
                "intro": None,
                "points": [
                    {
                        "title": "Werte interagieren miteinander",
                        "desc": "Ein niedriges Hämoglobin bedeutet mehr, wenn auch der MCV niedrig ist (was auf eine mögliche eisenbedingte Ursache hindeutet), als wenn der MCV normal ist. Einzelne Zahlen gewinnen ihre Bedeutung aus dem Muster, das sie zusammen bilden.",
                    },
                    {
                        "title": "Vorübergehende Faktoren spielen eine Rolle",
                        "desc": "Dehydration, eine kürzliche Mahlzeit, intensives Training, Stress oder Medikamente können Ihre Werte stunden- oder tagelang verändern. Ein leicht abweichendes Ergebnis wird oft wiederholt, bevor Schlüsse gezogen werden.",
                    },
                    {
                        "title": "Trends sind aussagekräftiger als Momentaufnahmen",
                        "desc": "Ein Hämoglobin von 12,0 g/dL bedeutet etwas anderes, wenn Ihre letzten drei Ergebnisse 14,5, 13,8 und 12,8 waren, als wenn sie seit Jahren stabil bei 12,0 liegen.",
                    },
                    {
                        "title": "Der klinische Kontext ist entscheidend",
                        "desc": "Ihr Arzt interpretiert Ihr Blutbild zusammen mit Ihren Symptomen, Ihrer Krankengeschichte, der körperlichen Untersuchung und anderen Tests. Ein Laborbericht allein — ohne diesen Kontext — kann irreführend sein.",
                    },
                ],
            },
            {
                "title": "Wenn man sich eine klarere Zusammenfassung wünscht",
                "intro": None,
                "paragraphs": [
                    "Viele Menschen erhalten einen Blutbild-Befund und fühlen sich überfordert. Die Abkürzungen sind unbekannt, die Referenzbereiche schwer zu vergleichen und es gibt keine verständliche Erklärung.",
                    "Manche suchen einzelne Werte online nach, aber das liefert verstreute, allgemeine Antworten, ohne zu zeigen, wie die Zahlen zusammenhängen. Andere warten auf ihren Arzttermin, der Tage oder Wochen entfernt sein kann.",
                    "Ein strukturiertes Tool wie NoryaAI kann diese Lücke überbrücken. Es liest Ihren Befund, ordnet die Werte in Kategorien, markiert alles außerhalb des Referenzbereichs und liefert verständliche Erklärungen — alles in einer einzigen, herunterladbaren Zusammenfassung, die Sie in Ruhe durchsehen oder zum nächsten Termin mitbringen können.",
                    "Es ersetzt nicht Ihren Arzt. Aber es kann das Gespräch produktiver machen.",
                ],
            },
        ],
        "mid_cta_title": "Haben Sie ein Blutbild, das Sie verstehen möchten?",
        "mid_cta_sub": "Laden Sie es hoch und erhalten Sie eine strukturierte Zusammenfassung mit verständlichen Erklärungen, markierten Werten und einem Gesundheits-Score.",
        "mid_cta_primary": "Befund hochladen",
        "mid_cta_secondary": "Beispielbericht ansehen",
        "faqs": [
            {
                "q": "Wofür steht CBC?",
                "a": "CBC steht für Complete Blood Count (großes Blutbild). Es ist eine routinemäßige Blutuntersuchung, die die Zellen in Ihrem Blut misst — rote Blutkörperchen, weiße Blutkörperchen und Thrombozyten — zusammen mit verwandten Werten wie Hämoglobin, Hämatokrit und Zellindizes.",
            },
            {
                "q": "Wie oft sollte ich ein Blutbild machen lassen?",
                "a": "Es gibt keinen universellen Zeitplan. Viele Ärzte nehmen ein Blutbild in die jährliche Vorsorgeuntersuchung auf. Es kann häufiger angeordnet werden, wenn Sie Symptome haben, eine chronische Erkrankung vorliegt oder Sie Medikamente einnehmen, die die Blutzellzahlen beeinflussen. Ihr Arzt wird die richtige Häufigkeit für Sie empfehlen.",
            },
            {
                "q": "Was bedeutet es, wenn ein Wert leicht außerhalb des Bereichs liegt?",
                "a": "Ein einzelner Wert leicht außerhalb des Referenzbereichs ist häufig und nicht immer ein Grund zur Sorge. Vorübergehende Faktoren wie Hydration, Bewegung oder Stress können Ihre Werte verschieben. Ärzte betrachten in der Regel das Gesamtmuster und wiederholen den Test möglicherweise, bevor sie Schlüsse ziehen.",
            },
            {
                "q": "Kann NoryaAI meine Blutbild-Ergebnisse interpretieren?",
                "a": "NoryaAI kann Ihren Blutbild-Befund lesen, jeden Marker mit seinem Referenzbereich organisieren, Werte außerhalb der Normgrenzen markieren und verständliche Erklärungen liefern. Es stellt keine Diagnosen — es strukturiert Ihre Ergebnisse, damit sie leichter zu verstehen sind.",
            },
            {
                "q": "Ersetzt dieser Ratgeber ärztlichen Rat?",
                "a": "Nein. Dieser Ratgeber ist informativ und soll Ihnen helfen, die Bestandteile eines Blutbild-Befunds zu verstehen. Er diagnostiziert nicht und empfiehlt keine Behandlung. Konsultieren Sie immer einen qualifizierten Arzt für medizinische Entscheidungen zu Ihren Ergebnissen.",
            },
            {
                "q": "Warum unterscheiden sich Referenzbereiche zwischen Laboren?",
                "a": "Labore verwenden unterschiedliche Geräte, Reagenzien und Populationsproben zur Bestimmung ihrer Bereiche. Faktoren wie Alter, Geschlecht und geografische Lage beeinflussen ebenfalls, was als \u201Enormal\u201C gilt. Deshalb kann dasselbe Ergebnis in einem Labor markiert und in einem anderen als im Bereich liegend betrachtet werden.",
            },
        ],
        "cta_title": "Bereit, Ihr Blutbild zu verstehen?",
        "cta_sub": "Laden Sie Ihren Befund hoch und erhalten Sie eine strukturierte, leicht lesbare Zusammenfassung — in wenigen Minuten.",
        "cta_primary": "Hochladen und analysieren",
        "cta_secondary": "Preise ansehen",
        "internal_links": [
            {"label": "Blutwerte erklärt", "path": "/de/blutwerte-erklart"},
            {"label": "Ergebnisse hochladen", "path": "/de/bluttest-ergebnisse-hochladen"},
            {"label": "KI Bluttest-Analyse", "path": "/de/ki-bluttest-analysator"},
            {"label": "Preise", "path": "/pricing"},
            {"label": "So funktioniert's", "path": "/how-it-works"},
            {"label": "Blog", "path": "/de/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# Spanish
# ---------------------------------------------------------------------------
def _es() -> dict:
    return {
        "meta_title": "Cómo leer un hemograma — Guía completa | NoryaAI",
        "meta_description": "Aprenda a leer un hemograma (CBC). Entienda WBC, RBC, hemoglobina, hematocrito, plaquetas e índices — con rangos de referencia explicados en lenguaje sencillo.",
        "badge": "Guía de laboratorio",
        "hero_title": "Cómo leer un hemograma",
        "hero_sub": "El hemograma es una de las pruebas de sangre más solicitadas en todo el mundo. Esta guía repasa cada componente — qué mide, qué significan las abreviaturas y cómo interpretar los números de su informe.",
        "sections": [
            {
                "title": "¿Qué es un hemograma (CBC)?",
                "intro": "Un hemograma completo (CBC) mide las células que componen su sangre: glóbulos rojos, glóbulos blancos y plaquetas. Los médicos lo usan como herramienta general de detección para verificar infecciones, anemia, problemas de coagulación y el estado general de salud. A menudo forma parte de un examen físico de rutina o es el primer paso al investigar síntomas como fatiga, moretones o infecciones recurrentes.",
                "paragraphs": [
                    "Su informe de hemograma normalmente incluye entre 10 y 20 valores individuales. Cada uno describe un aspecto diferente de su sangre — cuántas células tiene, qué tamaño tienen, cuánta hemoglobina transportan y cuánta variación hay en su tamaño.",
                    "Las secciones siguientes los desglosan en grupos para facilitar su comprensión.",
                ],
            },
            {
                "title": "Glóbulos blancos (WBC)",
                "intro": "Los glóbulos blancos forman parte de su sistema inmunológico. Un hemograma mide su recuento total y a veces los desglosa en subtipos (diferencial).",
                "markers": [
                    {
                        "name": "Recuento de glóbulos blancos",
                        "abbr": "WBC",
                        "desc": "El número total de glóbulos blancos en un volumen determinado de sangre. Un recuento alto puede sugerir infección o inflamación; un recuento bajo puede indicar una respuesta inmune debilitada. Muchos factores temporales — estrés, ejercicio, medicamentos — pueden alterar este número.",
                        "range": "4.500–11.000 células/µL",
                    },
                    {
                        "name": "Neutrófilos",
                        "abbr": "NEUT",
                        "desc": "El tipo más común de glóbulo blanco. Los neutrófilos suelen ser los primeros en responder a las infecciones bacterianas. Su porcentaje y recuento absoluto se reportan por separado.",
                        "range": "40–70 % del WBC",
                    },
                    {
                        "name": "Linfocitos",
                        "abbr": "LYMPH",
                        "desc": "Participan en la defensa viral y la inmunidad a largo plazo. Un aumento de linfocitos puede ocurrir con infecciones virales; una disminución puede aparecer en ciertas condiciones inmunológicas.",
                        "range": "20–40 % del WBC",
                    },
                ],
            },
            {
                "title": "Glóbulos rojos, hemoglobina y hematocrito",
                "intro": "Los glóbulos rojos transportan oxígeno desde los pulmones al resto del cuerpo. Varios valores del hemograma describen su recuento, su capacidad de transporte de oxígeno y su proporción en la sangre.",
                "markers": [
                    {
                        "name": "Recuento de glóbulos rojos",
                        "abbr": "RBC",
                        "desc": "El número total de glóbulos rojos por volumen de sangre. Los valores varían según el sexo y la edad. Un recuento bajo es un signo que puede estar asociado con anemia; un recuento alto puede verse en deshidratación u otras condiciones.",
                        "range": "4,5–5,5 millones de células/µL (hombres) · 4,0–5,0 (mujeres)",
                    },
                    {
                        "name": "Hemoglobina",
                        "abbr": "HGB / Hb",
                        "desc": "La proteína dentro de los glóbulos rojos que se une al oxígeno. La hemoglobina es uno de los valores más frecuentemente revisados en un hemograma. La hemoglobina baja es un marcador clave asociado con la anemia.",
                        "range": "13,5–17,5 g/dL (hombres) · 12,0–16,0 g/dL (mujeres)",
                    },
                    {
                        "name": "Hematocrito",
                        "abbr": "HCT",
                        "desc": "El porcentaje de su volumen sanguíneo compuesto por glóbulos rojos. Aumenta con la deshidratación y disminuye con la pérdida de sangre o la reducción en la producción de glóbulos rojos.",
                        "range": "38,3–48,6 % (hombres) · 35,5–44,9 % (mujeres)",
                    },
                ],
            },
            {
                "title": "Plaquetas",
                "intro": "Las plaquetas son pequeños fragmentos celulares que ayudan a la coagulación de la sangre. Un hemograma reporta su recuento y a veces su tamaño promedio.",
                "markers": [
                    {
                        "name": "Recuento de plaquetas",
                        "abbr": "PLT",
                        "desc": "El número de plaquetas por volumen de sangre. Un recuento bajo (trombocitopenia) puede aumentar el riesgo de sangrado; un recuento alto (trombocitosis) puede ser reactivo o, menos comúnmente, estar relacionado con una condición de la médula ósea.",
                        "range": "150.000–400.000 /µL",
                    },
                    {
                        "name": "Volumen plaquetario medio",
                        "abbr": "MPV",
                        "desc": "El tamaño promedio de sus plaquetas. Las plaquetas más grandes suelen ser más jóvenes y pueden indicar que su cuerpo las está produciendo más rápido para reemplazar las que se están usando.",
                        "range": "7,5–12,0 fL",
                    },
                ],
            },
            {
                "title": "Índices eritrocitarios",
                "intro": "Los índices describen el tamaño y el contenido de hemoglobina de sus glóbulos rojos. Ayudan a caracterizar el tipo de anemia si existe alguna.",
                "markers": [
                    {
                        "name": "Volumen corpuscular medio",
                        "abbr": "MCV",
                        "desc": "El tamaño promedio de un solo glóbulo rojo. Un MCV alto (macrocítico) puede estar asociado con problemas de B12 o folato; un MCV bajo (microcítico) puede estar asociado con condiciones relacionadas con el hierro.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "Hemoglobina corpuscular media",
                        "abbr": "MCH",
                        "desc": "La cantidad promedio de hemoglobina en un solo glóbulo rojo. Generalmente sigue al MCV — las células pequeñas llevan menos hemoglobina, las grandes llevan más.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "Concentración de hemoglobina corpuscular media",
                        "abbr": "MCHC",
                        "desc": "La concentración promedio de hemoglobina dentro de los glóbulos rojos. Un MCHC bajo sugiere que las células son más pálidas de lo normal (hipocrómicas).",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "Amplitud de distribución eritrocitaria",
                        "abbr": "RDW",
                        "desc": "Mide cuánta variación hay en el tamaño de sus glóbulos rojos. Un RDW alto significa que sus células varían más en tamaño, lo cual puede ser un signo temprano de que algo está afectando la producción de glóbulos rojos.",
                        "range": "11,5–14,5 %",
                    },
                ],
            },
            {
                "title": "Qué significan realmente los rangos de referencia",
                "intro": None,
                "paragraphs": [
                    "Los rangos de referencia representan el 95 % central de los resultados de una población sana analizada por ese laboratorio específico. No son puntos de corte absolutos para la salud o la enfermedad. Un valor ligeramente fuera del rango no significa automáticamente que algo esté mal, y un valor dentro del rango no garantiza que todo esté bien.",
                    "Los rangos varían entre laboratorios debido a diferencias en equipos, reactivos y las muestras de población utilizadas para establecerlos. La edad, el sexo, la altitud, la hidratación e incluso la hora del día pueden influir en sus resultados. Por eso, comparar sus números con un único valor «normal» de internet puede ser engañoso.",
                    "La forma más útil de interpretar su hemograma es en contexto: ¿cómo se comparan sus valores con sus propios resultados anteriores y qué piensa su médico considerando sus síntomas e historial?",
                ],
            },
            {
                "title": "Por qué un solo resultado no muestra el panorama completo",
                "intro": None,
                "points": [
                    {
                        "title": "Los valores interactúan entre sí",
                        "desc": "Una hemoglobina baja significa más cuando el MCV también es bajo (sugiriendo una posible causa relacionada con el hierro) que cuando el MCV es normal. Los números individuales cobran sentido a partir del patrón que forman juntos.",
                    },
                    {
                        "title": "Los factores temporales importan",
                        "desc": "La deshidratación, una comida reciente, el ejercicio intenso, el estrés o la medicación pueden alterar sus números durante horas o días. Un resultado ligeramente fuera de rango a menudo se repite antes de sacar conclusiones.",
                    },
                    {
                        "title": "Las tendencias son más informativas que las instantáneas",
                        "desc": "Una hemoglobina de 12,0 g/dL significa algo diferente si sus últimos tres resultados fueron 14,5, 13,8 y 12,8 que si han sido estables alrededor de 12,0 durante años.",
                    },
                    {
                        "title": "El contexto clínico es esencial",
                        "desc": "Su médico interpreta su hemograma junto con sus síntomas, historial médico, examen físico y otras pruebas. Un informe de laboratorio solo — sin ese contexto — puede ser engañoso.",
                    },
                ],
            },
            {
                "title": "Cuando se desea un resumen más claro",
                "intro": None,
                "paragraphs": [
                    "Muchas personas reciben un informe de hemograma y se sienten perdidas. Las abreviaturas son desconocidas, los rangos de referencia son difíciles de comparar y no hay una explicación en lenguaje sencillo incluida.",
                    "Algunos buscan valores individuales en línea, pero eso da respuestas dispersas y genéricas sin mostrar cómo se relacionan los números entre sí. Otros esperan su cita médica, que puede ser días o semanas después.",
                    "Una herramienta estructurada como NoryaAI puede ayudar a cerrar esa brecha. Lee su informe, organiza los valores en categorías, señala todo lo que esté fuera del rango de referencia y proporciona contexto en lenguaje sencillo — todo en un resumen único y descargable que puede revisar en su tiempo o llevar a su próxima cita.",
                    "No reemplaza a su médico. Pero puede hacer la conversación más productiva.",
                ],
            },
        ],
        "mid_cta_title": "¿Tiene un hemograma que quiere entender?",
        "mid_cta_sub": "Súbalo y obtenga un resumen estructurado con explicaciones en lenguaje sencillo, marcadores señalados y una puntuación de salud.",
        "mid_cta_primary": "Suba su informe",
        "mid_cta_secondary": "Vea un informe de ejemplo",
        "faqs": [
            {
                "q": "¿Qué significa CBC?",
                "a": "CBC significa hemograma completo (complete blood count). Es una prueba de sangre rutinaria que mide las células de su sangre — glóbulos rojos, glóbulos blancos y plaquetas — junto con valores relacionados como hemoglobina, hematocrito e índices celulares.",
            },
            {
                "q": "¿Con qué frecuencia debo hacerme un hemograma?",
                "a": "No hay un calendario universal. Muchos médicos incluyen un hemograma en los chequeos anuales. Puede solicitarse con más frecuencia si tiene síntomas, una condición crónica o está tomando medicamentos que afectan los recuentos de células sanguíneas. Su médico le recomendará la frecuencia adecuada para usted.",
            },
            {
                "q": "¿Qué significa si un valor está ligeramente fuera de rango?",
                "a": "Un valor ligeramente fuera del rango de referencia es común y no siempre es motivo de preocupación. Factores temporales como la hidratación, el ejercicio o el estrés pueden alterar sus números. Los médicos generalmente observan el patrón general y pueden repetir la prueba antes de sacar conclusiones.",
            },
            {
                "q": "¿Puede NoryaAI interpretar mis resultados de hemograma?",
                "a": "NoryaAI puede leer su informe de hemograma, organizar cada marcador con su rango de referencia, señalar valores fuera de los límites normales y proporcionar explicaciones en lenguaje sencillo. No diagnostica condiciones — estructura sus resultados para que sean más fáciles de entender.",
            },
            {
                "q": "¿Esta guía sustituye el consejo médico?",
                "a": "No. Esta guía es educativa y está destinada a ayudarle a comprender los componentes de un informe de hemograma. No diagnostica ni recomienda tratamiento. Siempre consulte a un profesional de la salud calificado para decisiones médicas sobre sus resultados.",
            },
            {
                "q": "¿Por qué los rangos de referencia difieren entre laboratorios?",
                "a": "Los laboratorios utilizan diferentes equipos, reactivos y muestras de población para establecer sus rangos. Factores como la edad, el sexo y la ubicación geográfica también influyen en lo que se considera «normal». Por eso, el mismo resultado puede ser señalado en un laboratorio pero considerado dentro del rango en otro.",
            },
        ],
        "cta_title": "¿Listo para entender su hemograma?",
        "cta_sub": "Suba su informe y obtenga un resumen estructurado y fácil de leer — en minutos.",
        "cta_primary": "Subir y analizar ahora",
        "cta_secondary": "Ver precios",
        "internal_links": [
            {"label": "Resultados de análisis explicados", "path": "/es/blood-test-results-explained"},
            {"label": "Subir resultados", "path": "/es/upload-blood-test-results"},
            {"label": "Analizador de sangre con IA", "path": "/es/ai-blood-test-analyzer"},
            {"label": "Precios", "path": "/pricing"},
            {"label": "Cómo funciona", "path": "/how-it-works"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# French
# ---------------------------------------------------------------------------
def _fr() -> dict:
    return {
        "meta_title": "Comment lire une NFS — Numération formule sanguine expliquée | NoryaAI",
        "meta_description": "Apprenez à lire un hémogramme (NFS/CBC). Comprenez les WBC, RBC, hémoglobine, hématocrite, plaquettes et indices — avec les plages de référence expliquées simplement.",
        "badge": "Guide labo",
        "hero_title": "Comment lire une NFS",
        "hero_sub": "La numération formule sanguine est l'une des analyses de sang les plus prescrites au monde. Ce guide passe en revue chaque composant — ce qu'il mesure, ce que signifient les abréviations et comment interpréter les chiffres de votre bilan.",
        "sections": [
            {
                "title": "Qu'est-ce qu'une NFS (CBC) ?",
                "intro": "Une numération formule sanguine (NFS/CBC) mesure les cellules qui composent votre sang : globules rouges, globules blancs et plaquettes. Les médecins l'utilisent comme outil de dépistage général pour vérifier les infections, l'anémie, les problèmes de coagulation et l'état de santé général. Elle fait souvent partie d'un bilan de routine ou constitue la première étape pour investiguer des symptômes comme la fatigue, les ecchymoses ou les infections récurrentes.",
                "paragraphs": [
                    "Votre bilan NFS comprend généralement 10 à 20 valeurs individuelles. Chacune décrit un aspect différent de votre sang — combien de cellules vous avez, quelle est leur taille, combien d'hémoglobine elles transportent et quelle est la variation de leur taille.",
                    "Les sections ci-dessous les décomposent en groupes pour les rendre plus faciles à comprendre.",
                ],
            },
            {
                "title": "Globules blancs (WBC)",
                "intro": "Les globules blancs font partie de votre système immunitaire. Une NFS mesure leur nombre total et les décompose parfois en sous-types (formule leucocytaire).",
                "markers": [
                    {
                        "name": "Numération des globules blancs",
                        "abbr": "WBC",
                        "desc": "Le nombre total de globules blancs dans un volume de sang donné. Un nombre élevé peut suggérer une infection ou une inflammation ; un nombre bas peut indiquer une réponse immunitaire affaiblie. De nombreux facteurs temporaires — stress, exercice, médicaments — peuvent modifier ce nombre.",
                        "range": "4 500–11 000 cellules/µL",
                    },
                    {
                        "name": "Neutrophiles",
                        "abbr": "NEUT",
                        "desc": "Le type le plus courant de globule blanc. Les neutrophiles sont généralement les premiers à intervenir lors d'infections bactériennes. Leur pourcentage et leur nombre absolu sont rapportés séparément.",
                        "range": "40–70 % des WBC",
                    },
                    {
                        "name": "Lymphocytes",
                        "abbr": "LYMPH",
                        "desc": "Impliqués dans la défense virale et l'immunité à long terme. Une hausse des lymphocytes peut survenir lors d'infections virales ; une baisse peut apparaître dans certaines conditions immunitaires.",
                        "range": "20–40 % des WBC",
                    },
                ],
            },
            {
                "title": "Globules rouges, hémoglobine et hématocrite",
                "intro": "Les globules rouges transportent l'oxygène des poumons vers le reste du corps. Plusieurs valeurs de la NFS décrivent leur nombre, leur capacité de transport d'oxygène et leur proportion dans le sang.",
                "markers": [
                    {
                        "name": "Numération des globules rouges",
                        "abbr": "RBC",
                        "desc": "Le nombre total de globules rouges par volume de sang. Les valeurs varient selon le sexe et l'âge. Un nombre bas est un signe qui peut être associé à une anémie ; un nombre élevé peut être observé en cas de déshydratation ou d'autres conditions.",
                        "range": "4,5–5,5 millions de cellules/µL (hommes) · 4,0–5,0 (femmes)",
                    },
                    {
                        "name": "Hémoglobine",
                        "abbr": "HGB / Hb",
                        "desc": "La protéine à l'intérieur des globules rouges qui fixe l'oxygène. L'hémoglobine est l'une des valeurs les plus couramment vérifiées dans une NFS. Une hémoglobine basse est un marqueur clé associé à l'anémie.",
                        "range": "13,5–17,5 g/dL (hommes) · 12,0–16,0 g/dL (femmes)",
                    },
                    {
                        "name": "Hématocrite",
                        "abbr": "HCT",
                        "desc": "Le pourcentage de votre volume sanguin constitué de globules rouges. Il augmente en cas de déshydratation et diminue en cas de perte de sang ou de réduction de la production de globules rouges.",
                        "range": "38,3–48,6 % (hommes) · 35,5–44,9 % (femmes)",
                    },
                ],
            },
            {
                "title": "Plaquettes",
                "intro": "Les plaquettes sont de petits fragments cellulaires qui aident votre sang à coaguler. Une NFS rapporte leur nombre et parfois leur taille moyenne.",
                "markers": [
                    {
                        "name": "Numération plaquettaire",
                        "abbr": "PLT",
                        "desc": "Le nombre de plaquettes par volume de sang. Un nombre bas (thrombocytopénie) peut augmenter le risque de saignement ; un nombre élevé (thrombocytose) peut être réactif ou, plus rarement, lié à une pathologie médullaire.",
                        "range": "150 000–400 000 /µL",
                    },
                    {
                        "name": "Volume plaquettaire moyen",
                        "abbr": "MPV",
                        "desc": "La taille moyenne de vos plaquettes. Les plaquettes plus grandes sont souvent plus jeunes et peuvent indiquer que votre corps les produit plus rapidement pour remplacer celles qui sont consommées.",
                        "range": "7,5–12,0 fL",
                    },
                ],
            },
            {
                "title": "Indices érythrocytaires",
                "intro": "Les indices décrivent la taille et la teneur en hémoglobine de vos globules rouges. Ils aident à caractériser le type d'anémie si une est présente.",
                "markers": [
                    {
                        "name": "Volume globulaire moyen",
                        "abbr": "MCV",
                        "desc": "La taille moyenne d'un seul globule rouge. Un MCV élevé (macrocytaire) peut être associé à des problèmes de B12 ou de folate ; un MCV bas (microcytaire) peut être associé à des conditions liées au fer.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "Teneur corpusculaire moyenne en hémoglobine",
                        "abbr": "MCH",
                        "desc": "La quantité moyenne d'hémoglobine dans un seul globule rouge. Elle suit généralement le MCV — les petites cellules transportent moins d'hémoglobine, les grandes en transportent plus.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "Concentration corpusculaire moyenne en hémoglobine",
                        "abbr": "MCHC",
                        "desc": "La concentration moyenne d'hémoglobine dans les globules rouges. Un MCHC bas suggère que les cellules sont plus pâles que la normale (hypochromes).",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "Indice de distribution des globules rouges",
                        "abbr": "RDW",
                        "desc": "Mesure la variation de taille de vos globules rouges. Un RDW élevé signifie que vos cellules varient davantage en taille, ce qui peut être un signe précoce que quelque chose affecte la production de globules rouges.",
                        "range": "11,5–14,5 %",
                    },
                ],
            },
            {
                "title": "Ce que signifient réellement les plages de référence",
                "intro": None,
                "paragraphs": [
                    "Les plages de référence représentent les 95 % centraux des résultats d'une population saine testée par ce laboratoire spécifique. Ce ne sont pas des seuils absolus de santé ou de maladie. Une valeur légèrement en dehors de la plage ne signifie pas automatiquement que quelque chose ne va pas, et une valeur dans la plage ne garantit pas que tout va bien.",
                    "Les plages varient entre les laboratoires en raison de différences d'équipements, de réactifs et des échantillons de population utilisés pour les établir. L'âge, le sexe, l'altitude, l'hydratation et même l'heure de la journée peuvent influencer vos résultats. C'est pourquoi comparer vos chiffres à une seule valeur « normale » trouvée sur internet peut être trompeur.",
                    "La manière la plus utile d'interpréter votre NFS est en contexte : comment vos valeurs se comparent-elles à vos propres résultats précédents, et qu'en pense votre médecin compte tenu de vos symptômes et de votre historique ?",
                ],
            },
            {
                "title": "Pourquoi un seul résultat ne montre pas tout le tableau",
                "intro": None,
                "points": [
                    {
                        "title": "Les valeurs interagissent entre elles",
                        "desc": "Une hémoglobine basse a plus de signification lorsque le MCV est aussi bas (suggérant une cause possible liée au fer) que lorsque le MCV est normal. Les chiffres individuels prennent leur sens dans le schéma qu'ils forment ensemble.",
                    },
                    {
                        "title": "Les facteurs temporaires comptent",
                        "desc": "La déshydratation, un repas récent, un exercice intense, le stress ou des médicaments peuvent modifier vos chiffres pendant des heures ou des jours. Un résultat légèrement hors plage est souvent répété avant de tirer des conclusions.",
                    },
                    {
                        "title": "Les tendances sont plus informatives que les instantanés",
                        "desc": "Une hémoglobine de 12,0 g/dL a une signification différente si vos trois derniers résultats étaient 14,5, 13,8 et 12,8 que s'ils sont stables autour de 12,0 depuis des années.",
                    },
                    {
                        "title": "Le contexte clinique est essentiel",
                        "desc": "Votre médecin interprète votre NFS en tenant compte de vos symptômes, de vos antécédents médicaux, de l'examen clinique et d'autres tests. Un rapport de laboratoire seul — sans ce contexte — peut être trompeur.",
                    },
                ],
            },
            {
                "title": "Quand on souhaite un résumé plus clair",
                "intro": None,
                "paragraphs": [
                    "Beaucoup de personnes reçoivent un bilan NFS et se sentent perdues. Les abréviations sont inconnues, les plages de référence sont difficiles à comparer et il n'y a pas d'explication en langage courant.",
                    "Certains recherchent des valeurs individuelles en ligne, mais cela donne des réponses dispersées et génériques sans montrer comment les chiffres sont liés entre eux. D'autres attendent leur rendez-vous médical, qui peut être dans plusieurs jours ou semaines.",
                    "Un outil structuré comme NoryaAI peut aider à combler ce fossé. Il lit votre bilan, organise les valeurs en catégories, signale tout ce qui est en dehors de la plage de référence et fournit un contexte en langage courant — le tout dans un résumé unique et téléchargeable que vous pouvez consulter à votre rythme ou apporter à votre prochain rendez-vous.",
                    "Il ne remplace pas votre médecin. Mais il peut rendre la conversation plus productive.",
                ],
            },
        ],
        "mid_cta_title": "Vous avez un bilan NFS que vous souhaitez comprendre ?",
        "mid_cta_sub": "Téléchargez-le et obtenez un résumé structuré avec des explications en langage courant, des marqueurs signalés et un score de santé.",
        "mid_cta_primary": "Télécharger votre bilan",
        "mid_cta_secondary": "Voir un rapport exemple",
        "faqs": [
            {
                "q": "Que signifie CBC ?",
                "a": "CBC signifie numération formule sanguine complète (complete blood count). C'est une analyse de sang de routine qui mesure les cellules de votre sang — globules rouges, globules blancs et plaquettes — ainsi que des valeurs associées comme l'hémoglobine, l'hématocrite et les indices cellulaires.",
            },
            {
                "q": "À quelle fréquence devrais-je faire une NFS ?",
                "a": "Il n'y a pas de calendrier universel. Beaucoup de médecins incluent une NFS dans les bilans annuels. Elle peut être prescrite plus fréquemment si vous avez des symptômes, une maladie chronique ou si vous prenez des médicaments qui affectent les numération cellulaire. Votre médecin vous recommandera la bonne fréquence.",
            },
            {
                "q": "Que signifie une valeur légèrement en dehors de la plage ?",
                "a": "Une seule valeur légèrement en dehors de la plage de référence est courante et n'est pas toujours préoccupante. Des facteurs temporaires comme l'hydratation, l'exercice ou le stress peuvent modifier vos chiffres. Les médecins examinent généralement le schéma global et peuvent répéter l'analyse avant de tirer des conclusions.",
            },
            {
                "q": "NoryaAI peut-il interpréter mes résultats de NFS ?",
                "a": "NoryaAI peut lire votre bilan NFS, organiser chaque marqueur avec sa plage de référence, signaler les valeurs hors limites normales et fournir des explications en langage courant. Il ne diagnostique pas — il structure vos résultats pour les rendre plus faciles à comprendre.",
            },
            {
                "q": "Ce guide remplace-t-il un avis médical ?",
                "a": "Non. Ce guide est éducatif et vise à vous aider à comprendre les composants d'un bilan NFS. Il ne diagnostique pas et ne recommande pas de traitement. Consultez toujours un professionnel de santé qualifié pour les décisions médicales concernant vos résultats.",
            },
            {
                "q": "Pourquoi les plages de référence diffèrent-elles entre les laboratoires ?",
                "a": "Les laboratoires utilisent des équipements, des réactifs et des échantillons de population différents pour établir leurs plages. Des facteurs comme l'âge, le sexe et la localisation géographique influencent également ce qui est considéré comme « normal ». C'est pourquoi le même résultat peut être signalé dans un laboratoire mais considéré comme normal dans un autre.",
            },
        ],
        "cta_title": "Prêt à comprendre votre NFS ?",
        "cta_sub": "Téléchargez votre bilan et obtenez un résumé structuré et facile à lire — en quelques minutes.",
        "cta_primary": "Télécharger et analyser",
        "cta_secondary": "Voir les tarifs",
        "internal_links": [
            {"label": "Résultats d'analyses expliqués", "path": "/fr/blood-test-results-explained"},
            {"label": "Télécharger vos résultats", "path": "/fr/upload-blood-test-results"},
            {"label": "Analyseur sanguin IA", "path": "/fr/ai-blood-test-analyzer"},
            {"label": "Tarifs", "path": "/pricing"},
            {"label": "Comment ça marche", "path": "/how-it-works"},
            {"label": "Blog", "path": "/en/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# Italian
# ---------------------------------------------------------------------------
def _it() -> dict:
    return {
        "meta_title": "Come leggere un emocromo — Esame emocromocitometrico spiegato | NoryaAI",
        "meta_description": "Scopri come leggere un emocromo (CBC). Comprendi WBC, RBC, emoglobina, ematocrito, piastrine e indici — con i range di riferimento spiegati in modo semplice.",
        "badge": "Guida di laboratorio",
        "hero_title": "Come leggere un emocromo",
        "hero_sub": "L'emocromo è uno degli esami del sangue più richiesti al mondo. Questa guida esamina ogni componente — cosa misura, cosa significano le abbreviazioni e come interpretare i numeri del referto.",
        "sections": [
            {
                "title": "Cos'è un emocromo (CBC)?",
                "intro": "Un esame emocromocitometrico (CBC/emocromo) misura le cellule che compongono il sangue: globuli rossi, globuli bianchi e piastrine. I medici lo usano come strumento di screening generale per verificare infezioni, anemia, problemi di coagulazione e lo stato di salute generale. Spesso fa parte di un controllo di routine o è il primo passo per indagare sintomi come stanchezza, lividi o infezioni ricorrenti.",
                "paragraphs": [
                    "Il referto dell'emocromo include in genere 10–20 valori individuali. Ognuno descrive un aspetto diverso del sangue — quante cellule ci sono, quanto sono grandi, quanta emoglobina trasportano e quanto variano in dimensioni.",
                    "Le sezioni seguenti li suddividono in gruppi per renderli più facili da capire.",
                ],
            },
            {
                "title": "Globuli bianchi (WBC)",
                "intro": "I globuli bianchi fanno parte del sistema immunitario. Un emocromo misura il loro conteggio totale e talvolta li suddivide in sottotipi (formula leucocitaria).",
                "markers": [
                    {
                        "name": "Conteggio dei globuli bianchi",
                        "abbr": "WBC",
                        "desc": "Il numero totale di globuli bianchi in un dato volume di sangue. Un conteggio alto può suggerire un'infezione o un'infiammazione; un conteggio basso può indicare una risposta immunitaria indebolita. Molti fattori temporanei — stress, esercizio, farmaci — possono influenzare questo valore.",
                        "range": "4.500–11.000 cellule/µL",
                    },
                    {
                        "name": "Neutrofili",
                        "abbr": "NEUT",
                        "desc": "Il tipo più comune di globulo bianco. I neutrofili sono solitamente i primi a rispondere alle infezioni batteriche. La loro percentuale e il conteggio assoluto vengono riportati separatamente.",
                        "range": "40–70 % dei WBC",
                    },
                    {
                        "name": "Linfociti",
                        "abbr": "LYMPH",
                        "desc": "Coinvolti nella difesa virale e nell'immunità a lungo termine. Un aumento dei linfociti può verificarsi con infezioni virali; una diminuzione può apparire in certe condizioni immunitarie.",
                        "range": "20–40 % dei WBC",
                    },
                ],
            },
            {
                "title": "Globuli rossi, emoglobina ed ematocrito",
                "intro": "I globuli rossi trasportano l'ossigeno dai polmoni al resto del corpo. Diversi valori dell'emocromo descrivono il loro conteggio, la capacità di trasporto dell'ossigeno e la loro proporzione nel sangue.",
                "markers": [
                    {
                        "name": "Conteggio dei globuli rossi",
                        "abbr": "RBC",
                        "desc": "Il numero totale di globuli rossi per volume di sangue. I valori variano in base a sesso ed età. Un conteggio basso è un segno che può essere associato ad anemia; un conteggio alto può essere osservato in caso di disidratazione o altre condizioni.",
                        "range": "4,5–5,5 milioni di cellule/µL (uomini) · 4,0–5,0 (donne)",
                    },
                    {
                        "name": "Emoglobina",
                        "abbr": "HGB / Hb",
                        "desc": "La proteina all'interno dei globuli rossi che lega l'ossigeno. L'emoglobina è uno dei valori più comunemente controllati in un emocromo. Un'emoglobina bassa è un marcatore chiave associato all'anemia.",
                        "range": "13,5–17,5 g/dL (uomini) · 12,0–16,0 g/dL (donne)",
                    },
                    {
                        "name": "Ematocrito",
                        "abbr": "HCT",
                        "desc": "La percentuale del volume sanguigno composta da globuli rossi. Aumenta con la disidratazione e diminuisce con la perdita di sangue o la ridotta produzione di globuli rossi.",
                        "range": "38,3–48,6 % (uomini) · 35,5–44,9 % (donne)",
                    },
                ],
            },
            {
                "title": "Piastrine",
                "intro": "Le piastrine sono piccoli frammenti cellulari che aiutano il sangue a coagulare. Un emocromo riporta il loro conteggio e talvolta la loro dimensione media.",
                "markers": [
                    {
                        "name": "Conteggio piastrinico",
                        "abbr": "PLT",
                        "desc": "Il numero di piastrine per volume di sangue. Un conteggio basso (trombocitopenia) può aumentare il rischio di sanguinamento; un conteggio alto (trombocitosi) può essere reattivo o, meno comunemente, correlato a una condizione del midollo osseo.",
                        "range": "150.000–400.000 /µL",
                    },
                    {
                        "name": "Volume piastrinico medio",
                        "abbr": "MPV",
                        "desc": "La dimensione media delle piastrine. Le piastrine più grandi sono spesso più giovani e possono indicare che il corpo le sta producendo più velocemente per sostituire quelle consumate.",
                        "range": "7,5–12,0 fL",
                    },
                ],
            },
            {
                "title": "Indici eritrocitari",
                "intro": "Gli indici descrivono la dimensione e il contenuto di emoglobina dei globuli rossi. Aiutano a caratterizzare il tipo di anemia, se presente.",
                "markers": [
                    {
                        "name": "Volume corpuscolare medio",
                        "abbr": "MCV",
                        "desc": "La dimensione media di un singolo globulo rosso. Un MCV alto (macrocitico) può essere associato a problemi di B12 o folati; un MCV basso (microcitico) può essere associato a condizioni legate al ferro.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "Emoglobina corpuscolare media",
                        "abbr": "MCH",
                        "desc": "La quantità media di emoglobina in un singolo globulo rosso. Di solito segue il MCV — le cellule piccole trasportano meno emoglobina, le grandi ne trasportano di più.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "Concentrazione emoglobinica corpuscolare media",
                        "abbr": "MCHC",
                        "desc": "La concentrazione media di emoglobina nei globuli rossi. Un MCHC basso suggerisce che le cellule sono più pallide del normale (ipocromiche).",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "Ampiezza di distribuzione eritrocitaria",
                        "abbr": "RDW",
                        "desc": "Misura la variazione dimensionale dei globuli rossi. Un RDW alto significa che le cellule variano di più in dimensioni, il che può essere un segno precoce che qualcosa sta influenzando la produzione di globuli rossi.",
                        "range": "11,5–14,5 %",
                    },
                ],
            },
            {
                "title": "Cosa significano realmente i range di riferimento",
                "intro": None,
                "paragraphs": [
                    "I range di riferimento rappresentano il 95 % centrale dei risultati di una popolazione sana testata da quel laboratorio specifico. Non sono soglie assolute per salute o malattia. Un valore leggermente fuori dal range non significa automaticamente che qualcosa non va, e un valore all'interno del range non garantisce che tutto sia a posto.",
                    "I range variano tra i laboratori a causa di differenze nelle apparecchiature, nei reagenti e nei campioni di popolazione utilizzati per stabilirli. Età, sesso, altitudine, idratazione e persino l'ora del giorno possono influenzare i risultati. Ecco perché confrontare i propri numeri con un singolo valore «normale» trovato su internet può essere fuorviante.",
                    "Il modo più utile per interpretare il proprio emocromo è nel contesto: come si confrontano i valori con i propri risultati precedenti, e cosa ne pensa il medico considerando i sintomi e la storia clinica?",
                ],
            },
            {
                "title": "Perché un singolo risultato non mostra il quadro completo",
                "intro": None,
                "points": [
                    {
                        "title": "I valori interagiscono tra loro",
                        "desc": "Un'emoglobina bassa è più significativa quando anche il MCV è basso (suggerendo una possibile causa legata al ferro) rispetto a quando il MCV è normale. I singoli numeri acquistano significato dal pattern che formano insieme.",
                    },
                    {
                        "title": "I fattori temporanei contano",
                        "desc": "Disidratazione, un pasto recente, esercizio intenso, stress o farmaci possono alterare i valori per ore o giorni. Un risultato leggermente fuori range viene spesso ripetuto prima di trarre conclusioni.",
                    },
                    {
                        "title": "Le tendenze sono più informative delle istantanee",
                        "desc": "Un'emoglobina di 12,0 g/dL ha un significato diverso se gli ultimi tre risultati erano 14,5, 13,8 e 12,8 rispetto a quando sono stabili intorno a 12,0 da anni.",
                    },
                    {
                        "title": "Il contesto clinico è essenziale",
                        "desc": "Il medico interpreta l'emocromo insieme ai sintomi, alla storia clinica, all'esame fisico e ad altri test. Un referto di laboratorio da solo — senza quel contesto — può essere fuorviante.",
                    },
                ],
            },
            {
                "title": "Quando si desidera un riepilogo più chiaro",
                "intro": None,
                "paragraphs": [
                    "Molte persone ricevono un referto dell'emocromo e si sentono perse. Le abbreviazioni sono sconosciute, i range di riferimento sono difficili da confrontare e non c'è una spiegazione in linguaggio semplice.",
                    "Alcuni cercano singoli valori online, ma questo dà risposte sparse e generiche senza mostrare come i numeri siano collegati tra loro. Altri aspettano l'appuntamento dal medico, che può essere giorni o settimane dopo.",
                    "Uno strumento strutturato come NoryaAI può aiutare a colmare questo divario. Legge il referto, organizza i valori in categorie, segnala tutto ciò che è fuori dal range di riferimento e fornisce un contesto in linguaggio semplice — il tutto in un unico riepilogo scaricabile da consultare con calma o portare al prossimo appuntamento.",
                    "Non sostituisce il medico. Ma può rendere la conversazione più produttiva.",
                ],
            },
        ],
        "mid_cta_title": "Hai un emocromo che vuoi capire?",
        "mid_cta_sub": "Caricalo e ottieni un riepilogo strutturato con spiegazioni in linguaggio semplice, marcatori segnalati e un punteggio di salute.",
        "mid_cta_primary": "Carica il referto",
        "mid_cta_secondary": "Vedi un referto di esempio",
        "faqs": [
            {
                "q": "Cosa significa CBC?",
                "a": "CBC sta per emocromo completo (complete blood count). È un esame del sangue di routine che misura le cellule del sangue — globuli rossi, globuli bianchi e piastrine — insieme a valori correlati come emoglobina, ematocrito e indici cellulari.",
            },
            {
                "q": "Ogni quanto dovrei fare un emocromo?",
                "a": "Non esiste un calendario universale. Molti medici includono un emocromo nei controlli annuali. Può essere prescritto più frequentemente se hai sintomi, una condizione cronica o stai assumendo farmaci che influenzano i conteggi delle cellule del sangue. Il medico raccomanderà la frequenza giusta per te.",
            },
            {
                "q": "Cosa significa se un valore è leggermente fuori range?",
                "a": "Un singolo valore leggermente fuori dal range di riferimento è comune e non sempre motivo di preoccupazione. Fattori temporanei come idratazione, esercizio o stress possono alterare i valori. I medici generalmente osservano il pattern complessivo e possono ripetere l'esame prima di trarre conclusioni.",
            },
            {
                "q": "NoryaAI può interpretare i miei risultati dell'emocromo?",
                "a": "NoryaAI può leggere il referto dell'emocromo, organizzare ogni marcatore con il suo range di riferimento, segnalare i valori fuori dai limiti normali e fornire spiegazioni in linguaggio semplice. Non diagnostica condizioni — struttura i risultati per renderli più facili da capire.",
            },
            {
                "q": "Questa guida sostituisce il parere medico?",
                "a": "No. Questa guida è educativa e mira ad aiutarti a comprendere i componenti di un referto dell'emocromo. Non diagnostica né raccomanda trattamenti. Consulta sempre un professionista sanitario qualificato per decisioni mediche sui tuoi risultati.",
            },
            {
                "q": "Perché i range di riferimento differiscono tra i laboratori?",
                "a": "I laboratori utilizzano apparecchiature, reagenti e campioni di popolazione diversi per stabilire i loro range. Fattori come età, sesso e posizione geografica influenzano anche ciò che è considerato «normale». Ecco perché lo stesso risultato può essere segnalato in un laboratorio ma considerato nel range in un altro.",
            },
        ],
        "cta_title": "Pronto a capire il tuo emocromo?",
        "cta_sub": "Carica il tuo referto e ottieni un riepilogo strutturato e facile da leggere — in pochi minuti.",
        "cta_primary": "Carica e analizza ora",
        "cta_secondary": "Vedi i prezzi",
        "internal_links": [
            {"label": "Risultati esami spiegati", "path": "/it/blood-test-results-explained"},
            {"label": "Carica risultati", "path": "/it/upload-blood-test-results"},
            {"label": "Analizzatore sangue IA", "path": "/it/ai-blood-test-analyzer"},
            {"label": "Prezzi", "path": "/pricing"},
            {"label": "Come funziona", "path": "/how-it-works"},
            {"label": "Blog", "path": "/it/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# Hebrew
# ---------------------------------------------------------------------------
def _he() -> dict:
    return {
        "meta_title": "איך לקרוא ספירת דם — המדריך המלא | NoryaAI",
        "meta_description": "למדו איך לקרוא תוצאות ספירת דם (CBC). הבינו WBC, RBC, המוגלובין, המטוקריט, טסיות ומדדים — עם טווחי ייחוס מוסברים בשפה פשוטה.",
        "badge": "מדריך מעבדה",
        "hero_title": "איך לקרוא ספירת דם",
        "hero_sub": "ספירת דם מלאה היא אחת מבדיקות הדם הנפוצות ביותר בעולם. מדריך זה עובר על כל רכיב — מה הוא מודד, מה המשמעות של הקיצורים, ואיך להבין את המספרים בדוח שלכם.",
        "sections": [
            {
                "title": "מהי ספירת דם (CBC)?",
                "intro": "ספירת דם מלאה (CBC) מודדת את התאים המרכיבים את הדם שלכם: תאי דם אדומים, תאי דם לבנים וטסיות. רופאים משתמשים בה ככלי סינון כללי לבדיקת זיהומים, אנמיה, בעיות קרישה ומצב בריאותי כללי. היא לעיתים קרובות חלק מבדיקה שגרתית או צעד ראשון בחקירת תסמינים כמו עייפות, חבורות או זיהומים חוזרים.",
                "paragraphs": [
                    "דוח ספירת הדם שלכם כולל בדרך כלל 10–20 ערכים בודדים. כל אחד מתאר היבט שונה של הדם — כמה תאים יש לכם, מה גודלם, כמה המוגלובין הם נושאים ועד כמה הם שונים בגודלם.",
                    "הסעיפים הבאים מחלקים אותם לקבוצות כדי שיהיה קל יותר להבין.",
                ],
            },
            {
                "title": "תאי דם לבנים (WBC)",
                "intro": "תאי דם לבנים הם חלק ממערכת החיסון שלכם. ספירת דם מודדת את המספר הכולל שלהם ולפעמים מחלקת אותם לתת-סוגים (ספירה דיפרנציאלית).",
                "markers": [
                    {
                        "name": "ספירת תאי דם לבנים",
                        "abbr": "WBC",
                        "desc": "המספר הכולל של תאי דם לבנים בנפח דם נתון. ספירה גבוהה עשויה להצביע על זיהום או דלקת; ספירה נמוכה עשויה להצביע על תגובה חיסונית מוחלשת. גורמים זמניים רבים — מתח, פעילות גופנית, תרופות — יכולים לשנות מספר זה.",
                        "range": "4,500–11,000 תאים/µL",
                    },
                    {
                        "name": "נויטרופילים",
                        "abbr": "NEUT",
                        "desc": "הסוג הנפוץ ביותר של תאי דם לבנים. נויטרופילים הם בדרך כלל המגיבים הראשונים לזיהומים חיידקיים. האחוז והספירה המוחלטת שלהם מדווחים בנפרד.",
                        "range": "40–70% מה-WBC",
                    },
                    {
                        "name": "לימפוציטים",
                        "abbr": "LYMPH",
                        "desc": "מעורבים בהגנה מפני נגיפים ובחסינות ארוכת טווח. עלייה בלימפוציטים יכולה להתרחש עם זיהומים נגיפיים; ירידה עשויה להופיע במצבים חיסוניים מסוימים.",
                        "range": "20–40% מה-WBC",
                    },
                ],
            },
            {
                "title": "תאי דם אדומים, המוגלובין והמטוקריט",
                "intro": "תאי דם אדומים נושאים חמצן מהריאות לשאר הגוף. מספר ערכים בספירת דם מתארים את מספרם, יכולת נשיאת החמצן שלהם ואת שיעורם בדם.",
                "markers": [
                    {
                        "name": "ספירת תאי דם אדומים",
                        "abbr": "RBC",
                        "desc": "המספר הכולל של תאי דם אדומים לנפח דם. הערכים משתנים לפי מין וגיל. ספירה נמוכה היא סימן שעשוי להיות קשור לאנמיה; ספירה גבוהה עשויה להיראות בהתייבשות או במצבים אחרים.",
                        "range": "4.5–5.5 מיליון תאים/µL (גברים) · 4.0–5.0 (נשים)",
                    },
                    {
                        "name": "המוגלובין",
                        "abbr": "HGB / Hb",
                        "desc": "החלבון בתוך תאי דם אדומים שקושר חמצן. המוגלובין הוא אחד הערכים הנבדקים ביותר בספירת דם. המוגלובין נמוך הוא סמן מרכזי הקשור לאנמיה.",
                        "range": "13.5–17.5 g/dL (גברים) · 12.0–16.0 g/dL (נשים)",
                    },
                    {
                        "name": "המטוקריט",
                        "abbr": "HCT",
                        "desc": "האחוז מנפח הדם שלכם שמורכב מתאי דם אדומים. הוא עולה עם התייבשות ויורד עם איבוד דם או ייצור מופחת של תאי דם אדומים.",
                        "range": "38.3–48.6% (גברים) · 35.5–44.9% (נשים)",
                    },
                ],
            },
            {
                "title": "טסיות",
                "intro": "טסיות הן שברי תאים קטנים שעוזרים לדם שלכם להיקרש. ספירת דם מדווחת על מספרם ולפעמים על גודלם הממוצע.",
                "markers": [
                    {
                        "name": "ספירת טסיות",
                        "abbr": "PLT",
                        "desc": "מספר הטסיות לנפח דם. ספירה נמוכה (טרומבוציטופניה) עלולה להגביר סיכון לדימום; ספירה גבוהה (טרומבוציטוזיס) עשויה להיות תגובתית או, בנדיר, קשורה למצב של מח העצם.",
                        "range": "150,000–400,000 /µL",
                    },
                    {
                        "name": "נפח טסיות ממוצע",
                        "abbr": "MPV",
                        "desc": "הגודל הממוצע של הטסיות שלכם. טסיות גדולות יותר הן לעיתים צעירות יותר ועשויות להצביע על כך שהגוף מייצר אותן מהר יותר כדי להחליף את אלו שנצרכו.",
                        "range": "7.5–12.0 fL",
                    },
                ],
            },
            {
                "title": "מדדי תאי דם אדומים",
                "intro": "מדדים מתארים את גודל ותכולת ההמוגלובין של תאי הדם האדומים שלכם. הם עוזרים לאפיין את סוג האנמיה אם קיימת.",
                "markers": [
                    {
                        "name": "נפח גופיפי ממוצע",
                        "abbr": "MCV",
                        "desc": "הגודל הממוצע של תא דם אדום בודד. MCV גבוה (מקרוציטי) עשוי להיות קשור לבעיות B12 או פולאט; MCV נמוך (מיקרוציטי) עשוי להיות קשור למצבים הקשורים לברזל.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "המוגלובין גופיפי ממוצע",
                        "abbr": "MCH",
                        "desc": "כמות ההמוגלובין הממוצעת בתא דם אדום בודד. בדרך כלל הולך בקנה אחד עם MCV — תאים קטנים נושאים פחות המוגלובין, תאים גדולים נושאים יותר.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "ריכוז המוגלובין גופיפי ממוצע",
                        "abbr": "MCHC",
                        "desc": "ריכוז ההמוגלובין הממוצע בתוך תאי דם אדומים. MCHC נמוך מרמז שהתאים חיוורים מהרגיל (היפוכרומיים).",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "רוחב התפלגות תאי דם אדומים",
                        "abbr": "RDW",
                        "desc": "מודד כמה שונות יש בגודל תאי הדם האדומים שלכם. RDW גבוה אומר שהתאים שלכם שונים יותר בגודלם, מה שעשוי להיות סימן מוקדם שמשהו משפיע על ייצור תאי דם אדומים.",
                        "range": "11.5–14.5%",
                    },
                ],
            },
            {
                "title": "מה באמת אומרים טווחי הייחוס",
                "intro": None,
                "paragraphs": [
                    "טווחי ייחוס מייצגים את 95% האמצעיים של תוצאות מאוכלוסייה בריאה שנבדקה על ידי אותה מעבדה ספציפית. הם אינם נקודות חיתוך מוחלטות לבריאות או מחלה. ערך מעט מחוץ לטווח לא אומר אוטומטית שמשהו לא בסדר, וערך בתוך הטווח לא מבטיח שהכל תקין.",
                    "הטווחים משתנים בין מעבדות בגלל הבדלים בציוד, בריאגנטים ובדגימות האוכלוסייה ששימשו לקביעתם. גיל, מין, גובה מעל פני הים, הידרציה ואפילו שעת היום יכולים להשפיע על התוצאות שלכם. לכן, השוואת המספרים שלכם לערך \"נורמלי\" יחיד מהאינטרנט עלולה להיות מטעה.",
                    "הדרך המועילה ביותר לפרש את ספירת הדם שלכם היא בהקשר: איך הערכים שלכם משתווים לתוצאות הקודמות שלכם, ומה הרופא שלכם חושב בהתחשב בתסמינים ובהיסטוריה שלכם?",
                ],
            },
            {
                "title": "למה תוצאה אחת לבדה לא מראה את התמונה המלאה",
                "intro": None,
                "points": [
                    {
                        "title": "ערכים מקיימים אינטראקציה זה עם זה",
                        "desc": "המוגלובין נמוך משמעותי יותר כאשר גם MCV נמוך (מה שמרמז על סיבה אפשרית הקשורה לברזל) מאשר כאשר MCV תקין. מספרים בודדים מקבלים משמעות מהדפוס שהם יוצרים יחד.",
                    },
                    {
                        "title": "גורמים זמניים חשובים",
                        "desc": "התייבשות, ארוחה אחרונה, פעילות גופנית אינטנסיבית, מתח או תרופות יכולים לשנות את המספרים שלכם לשעות או ימים. תוצאה מעט מחוץ לטווח לעיתים קרובות חוזרת על עצמה לפני שמסיקים מסקנות.",
                    },
                    {
                        "title": "מגמות אינפורמטיביות יותר מתמונות רגע",
                        "desc": "המוגלובין של 12.0 g/dL משמעותו שונה אם שלוש התוצאות האחרונות שלכם היו 14.5, 13.8 ו-12.8 לעומת אם הן היו יציבות סביב 12.0 במשך שנים.",
                    },
                    {
                        "title": "ההקשר הקליני חיוני",
                        "desc": "הרופא שלכם מפרש את ספירת הדם שלכם לצד התסמינים, ההיסטוריה הרפואית, הבדיקה הגופנית ובדיקות אחרות. דוח מעבדה לבדו — ללא ההקשר הזה — עלול להיות מטעה.",
                    },
                ],
            },
            {
                "title": "כשרוצים סיכום ברור יותר",
                "intro": None,
                "paragraphs": [
                    "אנשים רבים מקבלים דוח ספירת דם ומרגישים אבודים. הקיצורים לא מוכרים, טווחי הייחוס קשים להשוואה ואין הסבר בשפה פשוטה.",
                    "חלק מחפשים ערכים בודדים באינטרנט, אבל זה נותן תשובות מפוזרות וגנריות בלי להראות איך המספרים קשורים זה לזה. אחרים מחכים לתור לרופא, שעשוי להיות ימים או שבועות.",
                    "כלי מובנה כמו NoryaAI יכול לעזור לגשר על הפער הזה. הוא קורא את הדוח שלכם, מארגן את הערכים לקטגוריות, מסמן כל מה שמחוץ לטווח הייחוס ומספק הקשר בשפה פשוטה — הכל בסיכום יחיד שניתן להורדה שאתם יכולים לעיין בו בזמנכם או להביא לתור הבא.",
                    "הוא לא מחליף את הרופא שלכם. אבל הוא יכול להפוך את השיחה ליותר פרודוקטיבית.",
                ],
            },
        ],
        "mid_cta_title": "יש לכם דוח ספירת דם שאתם רוצים להבין?",
        "mid_cta_sub": "העלו אותו וקבלו סיכום מובנה עם הסברים בשפה פשוטה, סמנים מסומנים וציון בריאות.",
        "mid_cta_primary": "העלו את הדוח שלכם",
        "mid_cta_secondary": "ראו דוח לדוגמה",
        "faqs": [
            {
                "q": "מה זה CBC?",
                "a": "CBC ראשי תיבות של ספירת דם מלאה (complete blood count). זוהי בדיקת דם שגרתית המודדת את התאים בדם שלכם — תאי דם אדומים, תאי דם לבנים וטסיות — יחד עם ערכים קשורים כמו המוגלובין, המטוקריט ומדדי תאים.",
            },
            {
                "q": "כמה פעמים כדאי לעשות ספירת דם?",
                "a": "אין לוח זמנים אוניברסלי. רופאים רבים כוללים ספירת דם בבדיקות שנתיות. היא עשויה להיות מוזמנת בתדירות גבוהה יותר אם יש לכם תסמינים, מצב כרוני או שאתם נוטלים תרופות המשפיעות על ספירת תאי דם. הרופא שלכם ימליץ על התדירות הנכונה עבורכם.",
            },
            {
                "q": "מה המשמעות אם ערך אחד מעט מחוץ לטווח?",
                "a": "ערך בודד מעט מחוץ לטווח הייחוס הוא שכיח ולא תמיד סיבה לדאגה. גורמים זמניים כמו הידרציה, פעילות גופנית או מתח יכולים לשנות את המספרים שלכם. רופאים בדרך כלל מסתכלים על הדפוס הכללי ועשויים לחזור על הבדיקה לפני שמסיקים מסקנות.",
            },
            {
                "q": "האם NoryaAI יכולה לפרש את תוצאות ספירת הדם שלי?",
                "a": "NoryaAI יכולה לקרוא את דוח ספירת הדם שלכם, לארגן כל סמן עם טווח הייחוס שלו, לסמן ערכים מחוץ לגבולות הנורמליים ולספק הסברים בשפה פשוטה. היא לא מאבחנת מצבים — היא מבנה את התוצאות שלכם כדי שיהיו קלות יותר להבנה.",
            },
            {
                "q": "האם המדריך הזה מחליף ייעוץ רפואי?",
                "a": "לא. מדריך זה הוא חינוכי ונועד לעזור לכם להבין את מרכיבי דוח ספירת דם. הוא לא מאבחן ולא ממליץ על טיפול. התייעצו תמיד עם איש מקצוע רפואי מוסמך לגבי החלטות רפואיות על התוצאות שלכם.",
            },
            {
                "q": "למה טווחי ייחוס שונים בין מעבדות?",
                "a": "מעבדות משתמשות בציוד, ריאגנטים ודגימות אוכלוסייה שונים לקביעת הטווחים שלהן. גורמים כמו גיל, מין ומיקום גיאוגרפי גם משפיעים על מה שנחשב \"נורמלי\". לכן, אותה תוצאה עשויה להיות מסומנת במעבדה אחת אך להיחשב בטווח במעבדה אחרת.",
            },
        ],
        "cta_title": "מוכנים להבין את ספירת הדם שלכם?",
        "cta_sub": "העלו את הדוח שלכם וקבלו סיכום מובנה וקל לקריאה — בדקות.",
        "cta_primary": "העלו ונתחו עכשיו",
        "cta_secondary": "צפו במחירים",
        "internal_links": [
            {"label": "תוצאות בדיקות דם מוסברות", "path": "/he/blood-test-results-explained"},
            {"label": "העלאת תוצאות", "path": "/he/upload-blood-test-results"},
            {"label": "מנתח בדיקות דם AI", "path": "/he/ai-blood-test-analyzer"},
            {"label": "מחירים", "path": "/pricing"},
            {"label": "איך זה עובד", "path": "/how-it-works"},
            {"label": "בלוג", "path": "/en/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# Hindi
# ---------------------------------------------------------------------------
def _hi() -> dict:
    return {
        "meta_title": "CBC कैसे पढ़ें — पूर्ण रक्त गणना गाइड | NoryaAI",
        "meta_description": "CBC (पूर्ण रक्त गणना) रिपोर्ट कैसे पढ़ें सीखें। WBC, RBC, हीमोग्लोबिन, हेमेटोक्रिट, प्लेटलेट्स और इंडेक्स — संदर्भ रेंज के साथ सरल भाषा में समझाया गया।",
        "badge": "लैब गाइड",
        "hero_title": "CBC कैसे पढ़ें",
        "hero_sub": "पूर्ण रक्त गणना दुनिया भर में सबसे अधिक मांगी जाने वाली रक्त जांचों में से एक है। यह गाइड प्रत्येक घटक को समझाती है — यह क्या मापता है, संक्षिप्त नामों का क्या अर्थ है, और अपनी रिपोर्ट में संख्याओं को कैसे समझें।",
        "sections": [
            {
                "title": "CBC क्या है?",
                "intro": "पूर्ण रक्त गणना (CBC) आपके रक्त की कोशिकाओं को मापती है: लाल कोशिकाएं, सफेद कोशिकाएं और प्लेटलेट्स। डॉक्टर इसे संक्रमण, एनीमिया, थक्के की समस्याओं और समग्र स्वास्थ्य की जांच के लिए एक सामान्य स्क्रीनिंग टूल के रूप में उपयोग करते हैं। यह अक्सर नियमित शारीरिक जांच का हिस्सा होता है या थकान, नीलापन, या बार-बार होने वाले संक्रमणों जैसे लक्षणों की जांच का पहला कदम होता है।",
                "paragraphs": [
                    "आपकी CBC रिपोर्ट में आमतौर पर 10–20 अलग-अलग मान शामिल होते हैं। प्रत्येक आपके रक्त के एक अलग पहलू का वर्णन करता है — कितनी कोशिकाएं हैं, वे कितनी बड़ी हैं, कितना हीमोग्लोबिन वे वहन करती हैं, और उनके आकार में कितनी भिन्नता है।",
                    "नीचे के खंड इन्हें समूहों में विभाजित करते हैं ताकि इन्हें समझना आसान हो।",
                ],
            },
            {
                "title": "सफेद रक्त कोशिकाएं (WBC)",
                "intro": "सफेद रक्त कोशिकाएं आपकी प्रतिरक्षा प्रणाली का हिस्सा हैं। CBC उनकी कुल गिनती मापती है और कभी-कभी उन्हें उप-प्रकारों में विभाजित करती है (डिफरेंशियल)।",
                "markers": [
                    {
                        "name": "सफेद रक्त कोशिका गणना",
                        "abbr": "WBC",
                        "desc": "रक्त की एक निश्चित मात्रा में सफेद रक्त कोशिकाओं की कुल संख्या। उच्च गिनती संक्रमण या सूजन का संकेत दे सकती है; कम गिनती कमजोर प्रतिरक्षा प्रतिक्रिया का संकेत दे सकती है। कई अस्थायी कारक — तनाव, व्यायाम, दवाइयां — इस संख्या को बदल सकते हैं।",
                        "range": "4,500–11,000 कोशिकाएं/µL",
                    },
                    {
                        "name": "न्यूट्रोफिल",
                        "abbr": "NEUT",
                        "desc": "सफेद रक्त कोशिका का सबसे आम प्रकार। न्यूट्रोफिल आमतौर पर जीवाणु संक्रमणों के प्रति पहले प्रतिक्रिया करते हैं। उनका प्रतिशत और पूर्ण गणना अलग-अलग रिपोर्ट की जाती है।",
                        "range": "WBC का 40–70%",
                    },
                    {
                        "name": "लिम्फोसाइट्स",
                        "abbr": "LYMPH",
                        "desc": "वायरल रक्षा और दीर्घकालिक प्रतिरक्षा में शामिल। वायरल संक्रमणों के साथ लिम्फोसाइट्स में वृद्धि हो सकती है; कुछ प्रतिरक्षा स्थितियों में कमी दिखाई दे सकती है।",
                        "range": "WBC का 20–40%",
                    },
                ],
            },
            {
                "title": "लाल रक्त कोशिकाएं, हीमोग्लोबिन और हेमेटोक्रिट",
                "intro": "लाल रक्त कोशिकाएं आपके फेफड़ों से शरीर के बाकी हिस्सों तक ऑक्सीजन ले जाती हैं। कई CBC मान उनकी गिनती, ऑक्सीजन ले जाने की क्षमता और रक्त में उनके अनुपात का वर्णन करते हैं।",
                "markers": [
                    {
                        "name": "लाल रक्त कोशिका गणना",
                        "abbr": "RBC",
                        "desc": "प्रति रक्त मात्रा में लाल रक्त कोशिकाओं की कुल संख्या। मान लिंग और उम्र के अनुसार भिन्न होते हैं। कम गिनती एनीमिया से जुड़ा एक संकेत हो सकती है; उच्च गिनती निर्जलीकरण या अन्य स्थितियों में देखी जा सकती है।",
                        "range": "4.5–5.5 मिलियन कोशिकाएं/µL (पुरुष) · 4.0–5.0 (महिला)",
                    },
                    {
                        "name": "हीमोग्लोबिन",
                        "abbr": "HGB / Hb",
                        "desc": "लाल रक्त कोशिकाओं के अंदर का प्रोटीन जो ऑक्सीजन को बांधता है। हीमोग्लोबिन CBC में सबसे अधिक जांचे जाने वाले मानों में से एक है। कम हीमोग्लोबिन एनीमिया से जुड़ा एक प्रमुख मार्कर है।",
                        "range": "13.5–17.5 g/dL (पुरुष) · 12.0–16.0 g/dL (महिला)",
                    },
                    {
                        "name": "हेमेटोक्रिट",
                        "abbr": "HCT",
                        "desc": "आपके रक्त की मात्रा का वह प्रतिशत जो लाल रक्त कोशिकाओं से बना है। यह निर्जलीकरण के साथ बढ़ता है और रक्त हानि या कम लाल कोशिका उत्पादन के साथ गिरता है।",
                        "range": "38.3–48.6% (पुरुष) · 35.5–44.9% (महिला)",
                    },
                ],
            },
            {
                "title": "प्लेटलेट्स",
                "intro": "प्लेटलेट्स छोटे कोशिका टुकड़े हैं जो आपके रक्त को जमने में मदद करते हैं। CBC उनकी गिनती और कभी-कभी उनके औसत आकार की रिपोर्ट करती है।",
                "markers": [
                    {
                        "name": "प्लेटलेट गणना",
                        "abbr": "PLT",
                        "desc": "प्रति रक्त मात्रा में प्लेटलेट्स की संख्या। कम गिनती (थ्रोम्बोसाइटोपेनिया) रक्तस्राव का खतरा बढ़ा सकती है; उच्च गिनती (थ्रोम्बोसाइटोसिस) प्रतिक्रियात्मक हो सकती है या, कम सामान्यतः, अस्थि मज्जा की स्थिति से संबंधित हो सकती है।",
                        "range": "150,000–400,000 /µL",
                    },
                    {
                        "name": "औसत प्लेटलेट मात्रा",
                        "abbr": "MPV",
                        "desc": "आपके प्लेटलेट्स का औसत आकार। बड़े प्लेटलेट्स अक्सर छोटे होते हैं और यह संकेत कर सकते हैं कि आपका शरीर उपयोग किए गए प्लेटलेट्स को बदलने के लिए तेजी से उत्पादन कर रहा है।",
                        "range": "7.5–12.0 fL",
                    },
                ],
            },
            {
                "title": "लाल कोशिका सूचकांक",
                "intro": "सूचकांक आपकी लाल रक्त कोशिकाओं के आकार और हीमोग्लोबिन सामग्री का वर्णन करते हैं। वे एनीमिया के प्रकार को चिह्नित करने में मदद करते हैं यदि कोई मौजूद है।",
                "markers": [
                    {
                        "name": "औसत कणिका आयतन",
                        "abbr": "MCV",
                        "desc": "एक एकल लाल रक्त कोशिका का औसत आकार। उच्च MCV (मैक्रोसाइटिक) B12 या फोलेट की समस्याओं से जुड़ा हो सकता है; कम MCV (माइक्रोसाइटिक) आयरन संबंधी स्थितियों से जुड़ा हो सकता है।",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "औसत कणिका हीमोग्लोबिन",
                        "abbr": "MCH",
                        "desc": "एक एकल लाल रक्त कोशिका में हीमोग्लोबिन की औसत मात्रा। यह आमतौर पर MCV के साथ जाता है — छोटी कोशिकाएं कम हीमोग्लोबिन वहन करती हैं, बड़ी कोशिकाएं अधिक।",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "औसत कणिका हीमोग्लोबिन सांद्रता",
                        "abbr": "MCHC",
                        "desc": "लाल रक्त कोशिकाओं के भीतर हीमोग्लोबिन की औसत सांद्रता। कम MCHC बताता है कि कोशिकाएं सामान्य से अधिक पीली हैं (हाइपोक्रोमिक)।",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "लाल कोशिका वितरण चौड़ाई",
                        "abbr": "RDW",
                        "desc": "आपकी लाल रक्त कोशिकाओं के आकार में कितनी भिन्नता है यह मापता है। उच्च RDW का अर्थ है कि आपकी कोशिकाएं आकार में अधिक भिन्न हैं, जो लाल कोशिका उत्पादन को प्रभावित करने वाली किसी चीज़ का प्रारंभिक संकेत हो सकता है।",
                        "range": "11.5–14.5%",
                    },
                ],
            },
            {
                "title": "संदर्भ रेंज का वास्तव में क्या अर्थ है",
                "intro": None,
                "paragraphs": [
                    "संदर्भ रेंज उस विशिष्ट प्रयोगशाला द्वारा परीक्षित स्वस्थ जनसंख्या के परिणामों के मध्य 95% का प्रतिनिधित्व करती हैं। वे स्वास्थ्य या बीमारी के लिए पूर्ण कटऑफ नहीं हैं। रेंज से थोड़ा बाहर का मान स्वचालित रूप से यह नहीं दर्शाता कि कुछ गलत है, और रेंज के भीतर का मान यह गारंटी नहीं देता कि सब ठीक है।",
                    "उपकरण, अभिकर्मकों और उन्हें स्थापित करने के लिए उपयोग किए गए जनसंख्या नमूनों में अंतर के कारण रेंज प्रयोगशालाओं के बीच भिन्न होती हैं। उम्र, लिंग, ऊंचाई, जलयोजन और दिन का समय भी आपके परिणामों को प्रभावित कर सकता है। यही कारण है कि इंटरनेट से एक \"सामान्य\" मान के साथ अपनी संख्याओं की तुलना करना भ्रामक हो सकता है।",
                    "अपनी CBC की व्याख्या करने का सबसे उपयोगी तरीका संदर्भ में है: आपके मान आपके स्वयं के पिछले परिणामों की तुलना में कैसे हैं, और आपके लक्षणों और इतिहास को देखते हुए आपके डॉक्टर क्या सोचते हैं?",
                ],
            },
            {
                "title": "एक अकेला परिणाम पूरी तस्वीर क्यों नहीं दिखाता",
                "intro": None,
                "points": [
                    {
                        "title": "मान एक दूसरे के साथ बातचीत करते हैं",
                        "desc": "कम हीमोग्लोबिन तब अधिक अर्थपूर्ण होता है जब MCV भी कम हो (संभावित आयरन संबंधित कारण का सुझाव) बजाय इसके कि MCV सामान्य हो। व्यक्तिगत संख्याएं उस पैटर्न से अर्थ प्राप्त करती हैं जो वे एक साथ बनाती हैं।",
                    },
                    {
                        "title": "अस्थायी कारक मायने रखते हैं",
                        "desc": "निर्जलीकरण, हाल का भोजन, तीव्र व्यायाम, तनाव या दवा आपकी संख्याओं को घंटों या दिनों तक बदल सकते हैं। किसी भी निष्कर्ष पर पहुंचने से पहले थोड़ा बाहर रेंज परिणाम अक्सर दोहराया जाता है।",
                    },
                    {
                        "title": "रुझान स्नैपशॉट्स से अधिक जानकारीपूर्ण हैं",
                        "desc": "12.0 g/dL का हीमोग्लोबिन कुछ अलग अर्थ रखता है यदि आपके पिछले तीन परिणाम 14.5, 13.8 और 12.8 थे बनाम यदि वे वर्षों से 12.0 के आसपास स्थिर रहे हैं।",
                    },
                    {
                        "title": "नैदानिक संदर्भ आवश्यक है",
                        "desc": "आपके डॉक्टर आपकी CBC की व्याख्या आपके लक्षणों, चिकित्सा इतिहास, शारीरिक परीक्षा और अन्य परीक्षणों के साथ करते हैं। एक प्रयोगशाला रिपोर्ट अकेले — उस संदर्भ के बिना — भ्रामक हो सकती है।",
                    },
                ],
            },
            {
                "title": "जब लोग एक स्पष्ट सारांश चाहते हैं",
                "intro": None,
                "paragraphs": [
                    "बहुत से लोग CBC रिपोर्ट प्राप्त करते हैं और भ्रमित महसूस करते हैं। संक्षिप्त नाम अपरिचित हैं, संदर्भ रेंज की तुलना करना कठिन है, और सरल भाषा में कोई स्पष्टीकरण शामिल नहीं है।",
                    "कुछ लोग ऑनलाइन अलग-अलग मान खोजते हैं, लेकिन यह बिखरे, सामान्य उत्तर देता है बिना यह दिखाए कि संख्याएं एक दूसरे से कैसे संबंधित हैं। अन्य अपनी डॉक्टर की अपॉइंटमेंट का इंतजार करते हैं, जो दिनों या हफ्तों बाद हो सकती है।",
                    "NoryaAI जैसा संरचित टूल इस अंतर को पाटने में मदद कर सकता है। यह आपकी रिपोर्ट पढ़ता है, मानों को श्रेणियों में व्यवस्थित करता है, संदर्भ रेंज से बाहर किसी भी चीज़ को चिह्नित करता है, और सरल भाषा में संदर्भ प्रदान करता है — सभी एक ही डाउनलोड करने योग्य सारांश में जिसे आप अपने समय पर देख सकते हैं या अपनी अगली अपॉइंटमेंट में ला सकते हैं।",
                    "यह आपके डॉक्टर की जगह नहीं लेता। लेकिन यह बातचीत को अधिक उत्पादक बना सकता है।",
                ],
            },
        ],
        "mid_cta_title": "क्या आपके पास एक CBC रिपोर्ट है जिसे आप समझना चाहते हैं?",
        "mid_cta_sub": "इसे अपलोड करें और सरल भाषा में स्पष्टीकरण, चिह्नित मार्कर और स्वास्थ्य स्कोर के साथ एक संरचित सारांश प्राप्त करें।",
        "mid_cta_primary": "अपनी रिपोर्ट अपलोड करें",
        "mid_cta_secondary": "नमूना रिपोर्ट देखें",
        "faqs": [
            {
                "q": "CBC का मतलब क्या है?",
                "a": "CBC का मतलब है पूर्ण रक्त गणना (complete blood count)। यह एक नियमित रक्त जांच है जो आपके रक्त में कोशिकाओं को मापती है — लाल रक्त कोशिकाएं, सफेद रक्त कोशिकाएं और प्लेटलेट्स — साथ ही हीमोग्लोबिन, हेमेटोक्रिट और कोशिका सूचकांकों जैसे संबंधित मान।",
            },
            {
                "q": "मुझे कितनी बार CBC करवानी चाहिए?",
                "a": "कोई सार्वभौमिक कार्यक्रम नहीं है। कई डॉक्टर वार्षिक जांच में CBC शामिल करते हैं। यदि आपके लक्षण हैं, कोई पुरानी बीमारी है, या आप रक्त कोशिका गणना को प्रभावित करने वाली दवाइयां ले रहे हैं तो इसे अधिक बार मांगा जा सकता है। आपके डॉक्टर आपके लिए सही आवृत्ति की सिफारिश करेंगे।",
            },
            {
                "q": "एक मान थोड़ा रेंज से बाहर होने का क्या मतलब है?",
                "a": "संदर्भ रेंज से थोड़ा बाहर एक अकेला मान आम है और हमेशा चिंता का कारण नहीं होता। जलयोजन, व्यायाम या तनाव जैसे अस्थायी कारक आपकी संख्याओं को बदल सकते हैं। डॉक्टर आमतौर पर समग्र पैटर्न देखते हैं और निष्कर्ष निकालने से पहले परीक्षण दोहरा सकते हैं।",
            },
            {
                "q": "क्या NoryaAI मेरे CBC परिणामों की व्याख्या कर सकता है?",
                "a": "NoryaAI आपकी CBC रिपोर्ट पढ़ सकता है, प्रत्येक मार्कर को उसकी संदर्भ रेंज के साथ व्यवस्थित कर सकता है, सामान्य सीमाओं से बाहर के मानों को चिह्नित कर सकता है, और सरल भाषा में स्पष्टीकरण प्रदान कर सकता है। यह स्थितियों का निदान नहीं करता — यह आपके परिणामों को समझने में आसान बनाता है।",
            },
            {
                "q": "क्या यह गाइड चिकित्सा सलाह का विकल्प है?",
                "a": "नहीं। यह गाइड शैक्षिक है और CBC रिपोर्ट के घटकों को समझने में आपकी मदद करने के लिए है। यह निदान या उपचार की सिफारिश नहीं करती। अपने परिणामों के बारे में चिकित्सा निर्णयों के लिए हमेशा एक योग्य स्वास्थ्य पेशेवर से परामर्श करें।",
            },
            {
                "q": "संदर्भ रेंज प्रयोगशालाओं के बीच क्यों भिन्न होती हैं?",
                "a": "प्रयोगशालाएं अपनी रेंज स्थापित करने के लिए विभिन्न उपकरण, अभिकर्मक और जनसंख्या नमूनों का उपयोग करती हैं। उम्र, लिंग और भौगोलिक स्थान जैसे कारक भी प्रभावित करते हैं कि \"सामान्य\" क्या माना जाता है। यही कारण है कि एक ही परिणाम एक प्रयोगशाला में चिह्नित हो सकता है लेकिन दूसरी में रेंज के भीतर माना जा सकता है।",
            },
        ],
        "cta_title": "अपनी CBC समझने के लिए तैयार हैं?",
        "cta_sub": "अपनी रिपोर्ट अपलोड करें और मिनटों में एक संरचित, पढ़ने में आसान सारांश प्राप्त करें।",
        "cta_primary": "अपलोड करें और अभी विश्लेषण करें",
        "cta_secondary": "मूल्य देखें",
        "internal_links": [
            {"label": "रक्त परीक्षण परिणाम समझाया", "path": "/hi/blood-test-results-explained"},
            {"label": "परिणाम अपलोड करें", "path": "/hi/upload-blood-test-results"},
            {"label": "AI रक्त परीक्षण विश्लेषक", "path": "/hi/ai-blood-test-analyzer"},
            {"label": "मूल्य निर्धारण", "path": "/pricing"},
            {"label": "यह कैसे काम करता है", "path": "/how-it-works"},
            {"label": "ब्लॉग", "path": "/en/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# Arabic
# ---------------------------------------------------------------------------
def _ar() -> dict:
    return {
        "meta_title": "كيف تقرأ تحليل CBC — دليل صورة الدم الكاملة | NoryaAI",
        "meta_description": "تعلم كيف تقرأ تقرير CBC (صورة الدم الكاملة). افهم WBC وRBC والهيموجلوبين والهيماتوكريت والصفائح والمؤشرات — مع نطاقات المرجعية موضحة بلغة بسيطة.",
        "badge": "دليل المختبر",
        "hero_title": "كيف تقرأ تحليل CBC",
        "hero_sub": "صورة الدم الكاملة هي أحد أكثر تحاليل الدم طلباً في العالم. يستعرض هذا الدليل كل مكوّن — ماذا يقيس، وما معنى الاختصارات، وكيف تفهم الأرقام في تقريرك.",
        "sections": [
            {
                "title": "ما هو تحليل CBC؟",
                "intro": "صورة الدم الكاملة (CBC) تقيس الخلايا التي يتكون منها دمك: كريات الدم الحمراء وكريات الدم البيضاء والصفائح الدموية. يستخدمها الأطباء كأداة فحص عامة للتحقق من العدوى وفقر الدم ومشاكل التخثر والصحة العامة. غالباً ما تكون جزءاً من الفحص الروتيني أو خطوة أولى عند التحقيق في أعراض مثل التعب أو الكدمات أو العدوى المتكررة.",
                "paragraphs": [
                    "يتضمن تقرير CBC عادةً 10–20 قيمة فردية. كل قيمة تصف جانباً مختلفاً من دمك — كم عدد الخلايا لديك، وما حجمها، وكم هيموجلوبين تحمله، ومدى تباينها في الحجم.",
                    "تقسم الأقسام أدناه هذه القيم إلى مجموعات لتسهيل فهمها.",
                ],
            },
            {
                "title": "كريات الدم البيضاء (WBC)",
                "intro": "كريات الدم البيضاء جزء من جهازك المناعي. يقيس تحليل CBC عددها الإجمالي وأحياناً يقسمها إلى أنواع فرعية (التعداد التفريقي).",
                "markers": [
                    {
                        "name": "تعداد كريات الدم البيضاء",
                        "abbr": "WBC",
                        "desc": "العدد الإجمالي لكريات الدم البيضاء في حجم معين من الدم. قد يشير العدد المرتفع إلى عدوى أو التهاب؛ وقد يشير العدد المنخفض إلى ضعف الاستجابة المناعية. العديد من العوامل المؤقتة — الإجهاد والتمارين والأدوية — يمكن أن تغير هذا الرقم.",
                        "range": "4,500–11,000 خلية/µL",
                    },
                    {
                        "name": "العدلات",
                        "abbr": "NEUT",
                        "desc": "النوع الأكثر شيوعاً من كريات الدم البيضاء. العدلات عادة هي أول المستجيبين للعدوى البكتيرية. يتم الإبلاغ عن نسبتها المئوية وعددها المطلق بشكل منفصل.",
                        "range": "40–70% من WBC",
                    },
                    {
                        "name": "الخلايا اللمفاوية",
                        "abbr": "LYMPH",
                        "desc": "تشارك في الدفاع ضد الفيروسات والمناعة طويلة المدى. قد يحدث ارتفاع في الخلايا اللمفاوية مع العدوى الفيروسية؛ وقد يظهر انخفاض في بعض الحالات المناعية.",
                        "range": "20–40% من WBC",
                    },
                ],
            },
            {
                "title": "كريات الدم الحمراء والهيموجلوبين والهيماتوكريت",
                "intro": "تنقل كريات الدم الحمراء الأكسجين من رئتيك إلى بقية جسمك. عدة قيم في CBC تصف عددها وقدرتها على نقل الأكسجين ونسبتها في الدم.",
                "markers": [
                    {
                        "name": "تعداد كريات الدم الحمراء",
                        "abbr": "RBC",
                        "desc": "العدد الإجمالي لكريات الدم الحمراء لكل حجم من الدم. تختلف القيم حسب الجنس والعمر. العدد المنخفض هو علامة قد ترتبط بفقر الدم؛ العدد المرتفع قد يُلاحظ في الجفاف أو حالات أخرى.",
                        "range": "4.5–5.5 مليون خلية/µL (رجال) · 4.0–5.0 (نساء)",
                    },
                    {
                        "name": "الهيموجلوبين",
                        "abbr": "HGB / Hb",
                        "desc": "البروتين داخل كريات الدم الحمراء الذي يرتبط بالأكسجين. الهيموجلوبين هو أحد أكثر القيم فحصاً في CBC. انخفاض الهيموجلوبين مؤشر رئيسي مرتبط بفقر الدم.",
                        "range": "13.5–17.5 g/dL (رجال) · 12.0–16.0 g/dL (نساء)",
                    },
                    {
                        "name": "الهيماتوكريت",
                        "abbr": "HCT",
                        "desc": "النسبة المئوية من حجم دمك التي تتكون من كريات الدم الحمراء. يرتفع مع الجفاف وينخفض مع فقدان الدم أو انخفاض إنتاج كريات الدم الحمراء.",
                        "range": "38.3–48.6% (رجال) · 35.5–44.9% (نساء)",
                    },
                ],
            },
            {
                "title": "الصفائح الدموية",
                "intro": "الصفائح الدموية هي شظايا خلوية صغيرة تساعد دمك على التخثر. يُبلغ تحليل CBC عن عددها وأحياناً متوسط حجمها.",
                "markers": [
                    {
                        "name": "تعداد الصفائح الدموية",
                        "abbr": "PLT",
                        "desc": "عدد الصفائح الدموية لكل حجم من الدم. العدد المنخفض (نقص الصفيحات) قد يزيد خطر النزيف؛ العدد المرتفع (كثرة الصفيحات) قد يكون تفاعلياً أو نادراً مرتبطاً بحالة في نخاع العظم.",
                        "range": "150,000–400,000 /µL",
                    },
                    {
                        "name": "متوسط حجم الصفائح",
                        "abbr": "MPV",
                        "desc": "متوسط حجم صفائحك الدموية. الصفائح الأكبر غالباً ما تكون أصغر سناً وقد تشير إلى أن جسمك ينتجها بشكل أسرع لتعويض المستهلكة.",
                        "range": "7.5–12.0 fL",
                    },
                ],
            },
            {
                "title": "مؤشرات كريات الدم الحمراء",
                "intro": "تصف المؤشرات حجم ومحتوى الهيموجلوبين في كريات الدم الحمراء. تساعد في تحديد نوع فقر الدم إن وُجد.",
                "markers": [
                    {
                        "name": "متوسط الحجم الكريوي",
                        "abbr": "MCV",
                        "desc": "متوسط حجم كرية دم حمراء واحدة. MCV مرتفع (كبير الكريات) قد يرتبط بمشاكل B12 أو الفولات؛ MCV منخفض (صغير الكريات) قد يرتبط بحالات متعلقة بالحديد.",
                        "range": "80–100 fL",
                    },
                    {
                        "name": "متوسط الهيموجلوبين الكريوي",
                        "abbr": "MCH",
                        "desc": "متوسط كمية الهيموجلوبين في كرية دم حمراء واحدة. عادةً يتبع MCV — الخلايا الصغيرة تحمل هيموجلوبين أقل، والكبيرة تحمل أكثر.",
                        "range": "27–33 pg",
                    },
                    {
                        "name": "تركيز الهيموجلوبين الكريوي المتوسط",
                        "abbr": "MCHC",
                        "desc": "متوسط تركيز الهيموجلوبين داخل كريات الدم الحمراء. MCHC منخفض يشير إلى أن الخلايا أكثر شحوباً من المعتاد (ناقصة الصبغ).",
                        "range": "32–36 g/dL",
                    },
                    {
                        "name": "عرض توزيع كريات الدم الحمراء",
                        "abbr": "RDW",
                        "desc": "يقيس مدى التباين في حجم كريات الدم الحمراء. RDW مرتفع يعني أن خلاياك تتباين أكثر في الحجم، مما قد يكون علامة مبكرة على شيء يؤثر على إنتاج كريات الدم الحمراء.",
                        "range": "11.5–14.5%",
                    },
                ],
            },
            {
                "title": "ماذا تعني نطاقات المرجعية فعلاً",
                "intro": None,
                "paragraphs": [
                    "تمثل نطاقات المرجعية الـ 95% الوسطى من نتائج السكان الأصحاء الذين تم اختبارهم بواسطة ذلك المختبر المحدد. ليست نقاط قطع مطلقة للصحة أو المرض. قيمة خارج النطاق قليلاً لا تعني تلقائياً أن هناك مشكلة، وقيمة داخل النطاق لا تضمن أن كل شيء على ما يرام.",
                    "تختلف النطاقات بين المختبرات بسبب الاختلافات في المعدات والكواشف وعينات السكان المستخدمة لتحديدها. العمر والجنس والارتفاع والترطيب وحتى وقت اليوم يمكن أن تؤثر على نتائجك. لذلك فإن مقارنة أرقامك بقيمة «طبيعية» واحدة من الإنترنت قد تكون مضللة.",
                    "الطريقة الأكثر فائدة لتفسير CBC الخاص بك هي في السياق: كيف تقارن قيمك بنتائجك السابقة، وماذا يعتقد طبيبك بالنظر إلى أعراضك وتاريخك؟",
                ],
            },
            {
                "title": "لماذا نتيجة واحدة لا تُظهر الصورة الكاملة",
                "intro": None,
                "points": [
                    {
                        "title": "القيم تتفاعل مع بعضها",
                        "desc": "هيموجلوبين منخفض يعني أكثر عندما يكون MCV أيضاً منخفضاً (مما يشير إلى سبب محتمل متعلق بالحديد) مقارنة بكون MCV طبيعياً. الأرقام الفردية تكتسب معنى من النمط الذي تشكله معاً.",
                    },
                    {
                        "title": "العوامل المؤقتة مهمة",
                        "desc": "الجفاف أو وجبة حديثة أو تمرين مكثف أو الإجهاد أو الأدوية يمكن أن تغير أرقامك لساعات أو أيام. نتيجة خارج النطاق قليلاً غالباً ما تُعاد قبل استخلاص أي استنتاجات.",
                    },
                    {
                        "title": "الاتجاهات أكثر إفادة من اللقطات",
                        "desc": "هيموجلوبين 12.0 g/dL يعني شيئاً مختلفاً إذا كانت نتائجك الثلاث الأخيرة 14.5 و13.8 و12.8 عما إذا كانت مستقرة حول 12.0 لسنوات.",
                    },
                    {
                        "title": "السياق السريري ضروري",
                        "desc": "يفسر طبيبك CBC الخاص بك إلى جانب أعراضك وتاريخك الطبي والفحص البدني واختبارات أخرى. تقرير مختبر وحده — بدون هذا السياق — قد يكون مضللاً.",
                    },
                ],
            },
            {
                "title": "عندما يريد الناس ملخصاً أوضح",
                "intro": None,
                "paragraphs": [
                    "كثير من الناس يتلقون تقرير CBC ويشعرون بالضياع. الاختصارات غير مألوفة، ونطاقات المرجعية صعبة المقارنة، ولا يوجد شرح بلغة بسيطة.",
                    "البعض يبحث عن قيم فردية عبر الإنترنت، لكن ذلك يعطي إجابات متفرقة وعامة دون إظهار كيف ترتبط الأرقام ببعضها. آخرون ينتظرون موعد الطبيب الذي قد يكون بعد أيام أو أسابيع.",
                    "أداة منظمة مثل NoryaAI يمكن أن تساعد في سد هذه الفجوة. تقرأ تقريرك، تنظم القيم في فئات، تُعلّم أي شيء خارج نطاق المرجعية، وتقدم سياقاً بلغة بسيطة — كل ذلك في ملخص واحد قابل للتحميل يمكنك مراجعته في وقتك أو إحضاره لموعدك القادم.",
                    "لا يحل محل طبيبك. لكنه يمكن أن يجعل المحادثة أكثر إنتاجية.",
                ],
            },
        ],
        "mid_cta_title": "لديك تقرير CBC تريد فهمه؟",
        "mid_cta_sub": "ارفعه واحصل على ملخص منظم مع شروحات بلغة بسيطة ومؤشرات مُعلَّمة ودرجة صحية.",
        "mid_cta_primary": "ارفع تقريرك",
        "mid_cta_secondary": "شاهد تقريراً نموذجياً",
        "faqs": [
            {
                "q": "ما معنى CBC؟",
                "a": "CBC اختصار لصورة الدم الكاملة (complete blood count). هو تحليل دم روتيني يقيس خلايا دمك — كريات الدم الحمراء وكريات الدم البيضاء والصفائح الدموية — مع قيم مرتبطة مثل الهيموجلوبين والهيماتوكريت ومؤشرات الخلايا.",
            },
            {
                "q": "كم مرة يجب أن أجري تحليل CBC؟",
                "a": "لا يوجد جدول زمني عالمي. كثير من الأطباء يدرجون CBC في الفحوصات السنوية. قد يُطلب بشكل أكثر تكراراً إذا كانت لديك أعراض أو حالة مزمنة أو تتناول أدوية تؤثر على تعداد خلايا الدم. سيوصي طبيبك بالتكرار المناسب لك.",
            },
            {
                "q": "ماذا يعني أن تكون قيمة واحدة خارج النطاق قليلاً؟",
                "a": "قيمة واحدة خارج نطاق المرجعية قليلاً أمر شائع وليس دائماً سبباً للقلق. عوامل مؤقتة مثل الترطيب والتمارين والإجهاد يمكن أن تغير أرقامك. الأطباء عادة ينظرون إلى النمط العام وقد يكررون الاختبار قبل استخلاص الاستنتاجات.",
            },
            {
                "q": "هل يمكن لـ NoryaAI تفسير نتائج CBC الخاصة بي؟",
                "a": "يمكن لـ NoryaAI قراءة تقرير CBC الخاص بك، وتنظيم كل مؤشر مع نطاقه المرجعي، وتعليم القيم خارج الحدود الطبيعية، وتقديم شروحات بلغة بسيطة. لا يشخص حالات — بل يُنظم نتائجك لتكون أسهل في الفهم.",
            },
            {
                "q": "هل هذا الدليل بديل عن المشورة الطبية؟",
                "a": "لا. هذا الدليل تعليمي ويهدف لمساعدتك في فهم مكونات تقرير CBC. لا يشخص ولا يوصي بعلاج. استشر دائماً متخصصاً صحياً مؤهلاً للقرارات الطبية بشأن نتائجك.",
            },
            {
                "q": "لماذا تختلف نطاقات المرجعية بين المختبرات؟",
                "a": "تستخدم المختبرات معدات وكواشف وعينات سكانية مختلفة لتحديد نطاقاتها. عوامل مثل العمر والجنس والموقع الجغرافي تؤثر أيضاً على ما يُعتبر «طبيعياً». لهذا قد تُعلَّم نفس النتيجة في مختبر لكنها تُعتبر ضمن النطاق في مختبر آخر.",
            },
        ],
        "cta_title": "مستعد لفهم تحليل CBC الخاص بك؟",
        "cta_sub": "ارفع تقريرك واحصل على ملخص منظم وسهل القراءة — في دقائق.",
        "cta_primary": "ارفع وحلّل الآن",
        "cta_secondary": "عرض الأسعار",
        "internal_links": [
            {"label": "نتائج تحاليل الدم موضحة", "path": "/ar/blood-test-results-explained"},
            {"label": "رفع النتائج", "path": "/ar/upload-blood-test-results"},
            {"label": "محلل تحاليل الدم بالذكاء الاصطناعي", "path": "/ar/ai-blood-test-analyzer"},
            {"label": "الأسعار", "path": "/pricing"},
            {"label": "كيف يعمل", "path": "/how-it-works"},
            {"label": "المدونة", "path": "/en/blog"},
        ],
    }


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
_CONTENT: dict[str, callable] = {
    "en": _en,
    "tr": _tr,
    "de": _de,
    "es": _es,
    "fr": _fr,
    "it": _it,
    "he": _he,
    "hi": _hi,
    "ar": _ar,
}


def get_cbc_guide_content(lang: str) -> dict:
    """Return CBC guide content dict for *lang*, falling back to English."""
    fn = _CONTENT.get(lang, _CONTENT["en"])
    return fn()


def get_cbc_guide_slug(lang: str) -> str:
    """Return the URL slug for the CBC guide in *lang*."""
    return CBC_GUIDE_SLUGS.get(lang, CBC_GUIDE_SLUGS["en"])
