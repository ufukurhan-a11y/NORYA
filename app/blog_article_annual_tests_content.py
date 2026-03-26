"""Pillar blog article: Essential Blood Tests Every Adult Should Get Annually.

Gateway/pillar content piece helping readers understand the basic blood tests
they need each year.  Registered in blog_i18n.py.
"""
from datetime import date


# ---------------------------------------------------------------------------
# English
# ---------------------------------------------------------------------------
def _sections_en():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="Why Annual Blood Tests Matter",
            body_html=(
                "<p>Blood tests are one of the most effective ways to catch health problems "
                "before they become serious. Many conditions — including diabetes, thyroid "
                "disorders, kidney disease, and high cholesterol — develop silently with no "
                "obvious symptoms for years.</p>"
                "<p>An annual blood panel gives you a <strong>baseline</strong> for your "
                "health. By tracking your values year over year, you and your doctor can "
                "spot trends early and intervene before a small imbalance becomes a "
                "chronic condition.</p>"
                "<ul>"
                "<li><strong>Early detection</strong> — catch issues like prediabetes or "
                "iron deficiency before symptoms appear</li>"
                "<li><strong>Trend tracking</strong> — one abnormal result may be noise; "
                "a rising trend across years is a signal</li>"
                "<li><strong>Preventive savings</strong> — treating early-stage conditions "
                "costs far less than managing advanced disease</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="Complete Blood Count (CBC)",
            body_html=(
                "<p>The CBC is the cornerstone blood test. It evaluates your red blood "
                "cells, white blood cells, hemoglobin, hematocrit, and platelets — giving "
                "a snapshot of your overall health.</p>"
                "<ul>"
                "<li><strong>Red blood cells &amp; hemoglobin</strong> — detect anemia, "
                "dehydration, and bone marrow issues</li>"
                "<li><strong>White blood cells</strong> — reveal infections, immune "
                "disorders, or allergic responses</li>"
                "<li><strong>Platelets</strong> — assess clotting ability and bleeding "
                "risk</li>"
                "</ul>"
                "<p>A CBC is quick, inexpensive, and included in virtually every routine "
                "check-up. Abnormal results often prompt follow-up tests to pinpoint the "
                "exact cause.</p>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="Comprehensive Metabolic Panel (CMP / BMP)",
            body_html=(
                "<p>The CMP measures 14 substances in your blood that reflect how well "
                "your kidneys, liver, and metabolism are functioning:</p>"
                "<ul>"
                "<li><strong>Glucose</strong> — screens for diabetes and prediabetes</li>"
                "<li><strong>BUN &amp; Creatinine</strong> — evaluate kidney function</li>"
                "<li><strong>ALT &amp; AST</strong> — assess liver health</li>"
                "<li><strong>Electrolytes (Na, K, Cl, CO₂)</strong> — monitor fluid "
                "balance, nerve function, and acid-base status</li>"
                "<li><strong>Calcium</strong> — important for bones, heart, and nerves</li>"
                "<li><strong>Albumin &amp; Total Protein</strong> — reflect nutritional "
                "status and liver/kidney function</li>"
                "</ul>"
                "<p>A <strong>Basic Metabolic Panel (BMP)</strong> is a shorter version "
                "that focuses on glucose, electrolytes, and kidney markers. Your doctor "
                "will choose the appropriate panel based on your history.</p>"
                "<p>If you want a dedicated walkthrough of <strong>CMP vs BMP</strong>, "
                "marker groups, and common follow-up patterns, see our "
                "<a href=\"/en/blog/metabolic-panel-results-explained\">metabolic panel results explained</a> guide.</p>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="Lipid Panel — Cholesterol &amp; Triglycerides",
            body_html=(
                "<p>Heart disease remains the leading cause of death worldwide. A lipid "
                "panel measures the fats in your blood that directly influence "
                "cardiovascular risk:</p>"
                "<ul>"
                "<li><strong>Total Cholesterol</strong> — overall cholesterol level; "
                "desirable &lt; 200 mg/dL</li>"
                "<li><strong>LDL (&ldquo;bad&rdquo;) Cholesterol</strong> — builds up in arteries; "
                "optimal &lt; 100 mg/dL</li>"
                "<li><strong>HDL (&ldquo;good&rdquo;) Cholesterol</strong> — removes cholesterol "
                "from arteries; target ≥ 60 mg/dL</li>"
                "<li><strong>Triglycerides</strong> — linked to heart disease and "
                "pancreatitis; normal &lt; 150 mg/dL</li>"
                "</ul>"
                "<p>Adults 20 and older should have a lipid panel every 4–6 years at "
                "minimum. Those with risk factors (family history, obesity, smoking) may "
                "need annual testing.</p>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="Thyroid Panel — TSH, T3 &amp; T4",
            body_html=(
                "<p>Your thyroid gland controls metabolism, energy, and body temperature. "
                "Thyroid disorders affect an estimated 12% of the population, and many "
                "cases go undiagnosed.</p>"
                "<ul>"
                "<li><strong>TSH (Thyroid-Stimulating Hormone)</strong> — the primary "
                "screening marker; normal 0.4–4.0 mIU/L</li>"
                "<li><strong>Free T4</strong> — the main thyroid hormone; low = "
                "hypothyroidism</li>"
                "<li><strong>Free T3</strong> — the more active hormone; useful when TSH "
                "is abnormal</li>"
                "</ul>"
                "<p><strong>Hypothyroidism</strong> (high TSH, low T4) causes fatigue, "
                "weight gain, cold intolerance, and depression. <strong>Hyperthyroidism"
                "</strong> (low TSH, high T4) causes weight loss, rapid heartbeat, and "
                "anxiety. Both are treatable once diagnosed.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="Diabetes Screening — HbA1c &amp; Fasting Glucose",
            body_html=(
                "<p>Over 10% of adults worldwide have diabetes, and a significant "
                "proportion are undiagnosed. Two key markers provide the clearest "
                "picture:</p>"
                "<ul>"
                "<li><strong>Fasting Blood Glucose</strong> — measures blood sugar after "
                "an 8-12 hour fast. Normal &lt; 100 mg/dL; prediabetes 100–125 mg/dL; "
                "diabetes ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c (Glycated Hemoglobin)</strong> — reflects average "
                "blood sugar over 2–3 months. Normal &lt; 5.7%; prediabetes 5.7–6.4%; "
                "diabetes ≥ 6.5%</li>"
                "</ul>"
                "<p>HbA1c is especially valuable because it doesn't require fasting and "
                "isn't affected by day-to-day fluctuations. If either marker is in the "
                "prediabetic range, lifestyle changes can often prevent progression to "
                "type 2 diabetes.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="Vitamin &amp; Mineral Tests — D, B12, Iron &amp; Ferritin",
            body_html=(
                "<p>Nutrient deficiencies are surprisingly common, even in developed "
                "countries. The most important ones to test annually:</p>"
                "<ul>"
                "<li><strong>Vitamin D (25-OH)</strong> — essential for bones, immunity, "
                "and mood. Optimal: 30–60 ng/mL. Deficiency is widespread, especially in "
                "northern climates.</li>"
                "<li><strong>Vitamin B12</strong> — critical for nerve function and red "
                "blood cell production. Deficiency causes fatigue, tingling, and cognitive "
                "issues. Common in vegetarians/vegans and older adults.</li>"
                "<li><strong>Iron &amp; Ferritin</strong> — iron is needed for oxygen "
                "transport; ferritin reflects iron stores. Low ferritin is the earliest "
                "marker of iron deficiency, often appearing before anemia develops.</li>"
                "</ul>"
                "<p>These tests are inexpensive and deficiencies are easy to correct with "
                "supplementation — but only if you know about them.</p>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="Inflammation Markers — CRP &amp; ESR",
            body_html=(
                "<p>Chronic low-grade inflammation is increasingly linked to heart "
                "disease, autoimmune conditions, and even cancer. Two accessible markers "
                "to monitor:</p>"
                "<ul>"
                "<li><strong>CRP (C-Reactive Protein)</strong> — produced by the liver "
                "in response to inflammation. hs-CRP &lt; 1 mg/L = low cardiovascular "
                "risk; 1–3 mg/L = moderate; &gt; 3 mg/L = high risk.</li>"
                "<li><strong>ESR (Erythrocyte Sedimentation Rate)</strong> — measures how "
                "quickly red blood cells settle. Elevated ESR suggests inflammation but "
                "is non-specific; useful for monitoring autoimmune diseases like "
                "rheumatoid arthritis or lupus.</li>"
                "</ul>"
                "<p>If either marker is elevated without an obvious cause (like an acute "
                "infection), your doctor may investigate further with additional tests.</p>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="How Often to Test &amp; How NoryaAI Helps",
            body_html=(
                "<p>Testing frequency depends on your age, risk factors, and existing "
                "conditions:</p>"
                "<ul>"
                "<li><strong>Ages 18–30</strong> — baseline CBC, metabolic panel, and "
                "lipid panel every 2–3 years; vitamin D and B12 if symptomatic</li>"
                "<li><strong>Ages 30–45</strong> — annual CBC, CMP, lipid panel; add "
                "thyroid (TSH) and HbA1c every 2–3 years</li>"
                "<li><strong>Ages 45+</strong> — full annual panel including CBC, CMP, "
                "lipids, thyroid, HbA1c, vitamin D, B12, ferritin, and CRP</li>"
                "<li><strong>Any age with risk factors</strong> (family history, obesity, "
                "chronic conditions) — more frequent, tailored testing</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> makes understanding your results effortless. "
                "Upload your lab report — PDF or photo — and NoryaAI will:</p>"
                "<ul>"
                "<li>Identify every biomarker on your report</li>"
                "<li>Compare each value to age- and sex-specific reference ranges</li>"
                "<li>Flag abnormal results with clear, plain-language explanations</li>"
                "<li>Generate a structured, doctor-ready health summary</li>"
                "</ul>"
                "<p>No manual data entry. Upload and get your personalized analysis in "
                "minutes.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Turkish
# ---------------------------------------------------------------------------
def _sections_tr():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="Yıllık Kan Tahlilleri Neden Önemlidir?",
            body_html=(
                "<p>Kan tahlilleri, sağlık sorunlarını ciddi hale gelmeden önce yakalamanın "
                "en etkili yollarından biridir. Diyabet, tiroid bozuklukları, böbrek "
                "hastalıkları ve yüksek kolesterol gibi birçok durum yıllarca belirgin "
                "bir belirti göstermeden sessizce ilerler.</p>"
                "<p>Yıllık kan paneli sağlığınız için bir <strong>referans değer</strong> "
                "oluşturur. Değerlerinizi yıldan yıla takip ederek, siz ve doktorunuz "
                "küçük bir dengesizlik kronik bir hastalığa dönüşmeden önce müdahale "
                "edebilirsiniz.</p>"
                "<ul>"
                "<li><strong>Erken teşhis</strong> — prediyabet veya demir eksikliği gibi "
                "sorunları belirtiler ortaya çıkmadan yakalayın</li>"
                "<li><strong>Trend takibi</strong> — tek bir anormal sonuç gürültü "
                "olabilir; yıllar boyunca yükselen bir trend sinyaldir</li>"
                "<li><strong>Önleyici tasarruf</strong> — erken evre durumları tedavi "
                "etmek, ileri hastalığı yönetmekten çok daha ucuzdur</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="Tam Kan Sayımı (CBC / Hemogram)",
            body_html=(
                "<p>CBC, temel kan testidir. Kırmızı kan hücreleri, beyaz kan hücreleri, "
                "hemoglobin, hematokrit ve trombositleri değerlendirerek genel sağlığınızın "
                "bir görüntüsünü sunar.</p>"
                "<ul>"
                "<li><strong>Kırmızı kan hücreleri ve hemoglobin</strong> — anemi, "
                "dehidrasyon ve kemik iliği sorunlarını tespit eder</li>"
                "<li><strong>Beyaz kan hücreleri</strong> — enfeksiyonları, bağışıklık "
                "bozukluklarını veya alerjik tepkileri ortaya koyar</li>"
                "<li><strong>Trombositler</strong> — pıhtılaşma yeteneğini ve kanama "
                "riskini değerlendirir</li>"
                "</ul>"
                "<p>CBC hızlı, ucuz ve hemen hemen her rutin kontrolde yer alır. Anormal "
                "sonuçlar genellikle kesin nedeni belirlemek için ek testleri gerektirir.</p>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="Kapsamlı Metabolik Panel (CMP / BMP)",
            body_html=(
                "<p>CMP, böbreklerinizin, karaciğerinizin ve metabolizmanızın ne kadar "
                "iyi çalıştığını yansıtan 14 maddeyi ölçer:</p>"
                "<ul>"
                "<li><strong>Glukoz</strong> — diyabet ve prediyabet taraması</li>"
                "<li><strong>BUN ve Kreatinin</strong> — böbrek fonksiyonunu "
                "değerlendirir</li>"
                "<li><strong>ALT ve AST</strong> — karaciğer sağlığını kontrol eder</li>"
                "<li><strong>Elektrolitler (Na, K, Cl, CO₂)</strong> — sıvı dengesi, "
                "sinir fonksiyonu ve asit-baz durumunu izler</li>"
                "<li><strong>Kalsiyum</strong> — kemikler, kalp ve sinirler için "
                "önemlidir</li>"
                "<li><strong>Albümin ve Total Protein</strong> — beslenme durumunu ve "
                "karaciğer/böbrek fonksiyonunu yansıtır</li>"
                "</ul>"
                "<p><strong>Temel Metabolik Panel (BMP)</strong>, glukoz, elektrolitler "
                "ve böbrek belirteçlerine odaklanan daha kısa bir versiyondur.</p>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="Lipit Paneli — Kolesterol ve Trigliseritler",
            body_html=(
                "<p>Kalp hastalıkları dünya çapında önde gelen ölüm nedenidir. Lipit "
                "paneli, kardiyovasküler riski doğrudan etkileyen kan yağlarını ölçer:</p>"
                "<ul>"
                "<li><strong>Total Kolesterol</strong> — ideal &lt; 200 mg/dL</li>"
                "<li><strong>LDL (\"kötü\") Kolesterol</strong> — damarları tıkar; "
                "optimal &lt; 100 mg/dL</li>"
                "<li><strong>HDL (\"iyi\") Kolesterol</strong> — damarlardan kolesterolü "
                "temizler; hedef ≥ 60 mg/dL</li>"
                "<li><strong>Trigliseritler</strong> — kalp hastalığı ve pankreatit ile "
                "ilişkili; normal &lt; 150 mg/dL</li>"
                "</ul>"
                "<p>20 yaş ve üzeri yetişkinler en az 4–6 yılda bir lipit paneli "
                "yaptırmalıdır. Risk faktörleri olanlar (aile öyküsü, obezite, sigara) "
                "yıllık teste ihtiyaç duyabilir.</p>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="Tiroid Paneli — TSH, T3 ve T4",
            body_html=(
                "<p>Tiroid beziniz metabolizmayı, enerji düzeyini ve vücut sıcaklığını "
                "kontrol eder. Tiroid bozuklukları nüfusun tahminen %12'sini etkiler ve "
                "birçok vaka teşhis edilmeden kalır.</p>"
                "<ul>"
                "<li><strong>TSH</strong> — birincil tarama belirteci; normal "
                "0,4–4,0 mIU/L</li>"
                "<li><strong>Serbest T4</strong> — ana tiroid hormonu; düşük = "
                "hipotiroidizm</li>"
                "<li><strong>Serbest T3</strong> — daha aktif hormon; TSH anormal "
                "olduğunda değerlidir</li>"
                "</ul>"
                "<p><strong>Hipotiroidizm</strong> (yüksek TSH, düşük T4) yorgunluk, "
                "kilo artışı ve soğuğa hassasiyete neden olur. <strong>Hipertiroidizm"
                "</strong> (düşük TSH, yüksek T4) kilo kaybı, çarpıntı ve anksiyeteye "
                "yol açar. Her ikisi de teşhis edildiğinde tedavi edilebilir.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="Diyabet Taraması — HbA1c ve Açlık Glukozu",
            body_html=(
                "<p>Dünya çapında yetişkinlerin %10'undan fazlasında diyabet vardır ve "
                "önemli bir kısmı teşhis edilmemiştir. İki temel belirteç en net tabloyu "
                "sunar:</p>"
                "<ul>"
                "<li><strong>Açlık Kan Şekeri</strong> — 8-12 saatlik açlık sonrası "
                "ölçülür. Normal &lt; 100 mg/dL; prediyabet 100–125 mg/dL; "
                "diyabet ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — son 2-3 aydaki ortalama kan şekerini "
                "yansıtır. Normal &lt; %5,7; prediyabet %5,7–6,4; "
                "diyabet ≥ %6,5</li>"
                "</ul>"
                "<p>HbA1c özellikle değerlidir çünkü açlık gerektirmez ve günlük "
                "dalgalanmalardan etkilenmez. Her iki belirteçten biri prediyabetik "
                "aralıktaysa, yaşam tarzı değişiklikleri genellikle tip 2 diyabete "
                "ilerlemeyi önleyebilir.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="Vitamin ve Mineral Testleri — D, B12, Demir ve Ferritin",
            body_html=(
                "<p>Besin eksiklikleri gelişmiş ülkelerde bile şaşırtıcı derecede "
                "yaygındır. Yıllık olarak test edilmesi gereken en önemlileri:</p>"
                "<ul>"
                "<li><strong>D Vitamini (25-OH)</strong> — kemikler, bağışıklık ve ruh "
                "hali için gereklidir. Optimal: 30–60 ng/mL. Özellikle kuzey iklimlerde "
                "eksiklik yaygındır.</li>"
                "<li><strong>B12 Vitamini</strong> — sinir fonksiyonu ve kırmızı kan "
                "hücresi üretimi için kritiktir. Eksiklik yorgunluk, karıncalanma ve "
                "bilişsel sorunlara neden olur.</li>"
                "<li><strong>Demir ve Ferritin</strong> — demir oksijen taşınması için "
                "gereklidir; ferritin demir depolarını yansıtır. Düşük ferritin, demir "
                "eksikliğinin en erken belirtecidir.</li>"
                "</ul>"
                "<p>Bu testler ucuzdur ve eksiklikler takviyeyle kolayca düzeltilebilir "
                "— ancak yalnızca farkındaysanız.</p>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="İnflamasyon Belirteçleri — CRP ve ESR",
            body_html=(
                "<p>Kronik düşük dereceli inflamasyon kalp hastalığı, otoimmün durumlar "
                "ve hatta kanserle giderek daha fazla ilişkilendirilmektedir:</p>"
                "<ul>"
                "<li><strong>CRP (C-Reaktif Protein)</strong> — karaciğerin inflamasyona "
                "yanıt olarak ürettiği protein. hs-CRP &lt; 1 mg/L = düşük "
                "kardiyovasküler risk; 1–3 mg/L = orta; &gt; 3 mg/L = yüksek risk.</li>"
                "<li><strong>ESR (Eritrosit Sedimentasyon Hızı)</strong> — kırmızı kan "
                "hücrelerinin ne kadar hızlı çöktüğünü ölçer. Yükselen ESR inflamasyonu "
                "düşündürür ancak spesifik değildir; romatoid artrit veya lupus gibi "
                "otoimmün hastalıkların takibinde faydalıdır.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="Ne Sıklıkta Test Yapılmalı ve NoryaAI Nasıl Yardımcı Olur?",
            body_html=(
                "<p>Test sıklığı yaşınıza, risk faktörlerinize ve mevcut durumlarınıza "
                "bağlıdır:</p>"
                "<ul>"
                "<li><strong>18–30 yaş</strong> — 2-3 yılda bir CBC, metabolik panel "
                "ve lipit paneli; belirtiler varsa D ve B12 vitamini</li>"
                "<li><strong>30–45 yaş</strong> — yıllık CBC, CMP, lipit paneli; "
                "2-3 yılda bir tiroid (TSH) ve HbA1c ekleyin</li>"
                "<li><strong>45+ yaş</strong> — CBC, CMP, lipitler, tiroid, HbA1c, "
                "D vitamini, B12, ferritin ve CRP dahil tam yıllık panel</li>"
                "<li><strong>Risk faktörleri olan herhangi bir yaş</strong> — daha sık, "
                "kişiye özel testler</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> sonuçlarınızı anlamayı kolaylaştırır. "
                "Laboratuvar raporunuzu — PDF veya fotoğraf — yükleyin, NoryaAI şunları "
                "yapar:</p>"
                "<ul>"
                "<li>Raporunuzdaki her biyobelirteci tanımlar</li>"
                "<li>Her değeri yaş ve cinsiyete özel referans aralıklarıyla "
                "karşılaştırır</li>"
                "<li>Anormal sonuçları net, anlaşılır açıklamalarla işaretler</li>"
                "<li>Yapılandırılmış, doktora hazır bir sağlık özeti oluşturur</li>"
                "</ul>"
                "<p>Manuel veri girişi gerekmez. Yükleyin ve kişisel analizinizi dakikalar "
                "içinde alın.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------
def _sections_de():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="Warum jährliche Bluttests wichtig sind",
            body_html=(
                "<p>Bluttests gehören zu den wirksamsten Methoden, um Gesundheitsprobleme "
                "frühzeitig zu erkennen. Viele Erkrankungen — darunter Diabetes, "
                "Schilddrüsenstörungen, Nierenerkrankungen und hoher Cholesterinspiegel "
                "— entwickeln sich über Jahre hinweg still und ohne offensichtliche "
                "Symptome.</p>"
                "<p>Ein jährliches Blutbild schafft eine <strong>Ausgangsbasis</strong> "
                "für Ihre Gesundheit. Durch die jährliche Verfolgung Ihrer Werte können "
                "Sie und Ihr Arzt Trends frühzeitig erkennen und eingreifen, bevor ein "
                "kleines Ungleichgewicht zu einer chronischen Erkrankung wird.</p>"
                "<ul>"
                "<li><strong>Früherkennung</strong> — Probleme wie Prädiabetes oder "
                "Eisenmangel erkennen, bevor Symptome auftreten</li>"
                "<li><strong>Trendverfolgung</strong> — ein einzelner abnormaler Wert "
                "kann Zufall sein; ein steigender Trend über Jahre hinweg ist ein "
                "Signal</li>"
                "<li><strong>Präventive Einsparungen</strong> — die Behandlung von "
                "Frühstadien kostet weit weniger als die Versorgung fortgeschrittener "
                "Erkrankungen</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="Großes Blutbild (CBC)",
            body_html=(
                "<p>Das große Blutbild ist der grundlegende Bluttest. Es bewertet rote "
                "Blutkörperchen, weiße Blutkörperchen, Hämoglobin, Hämatokrit und "
                "Thrombozyten — eine Momentaufnahme Ihrer allgemeinen Gesundheit.</p>"
                "<ul>"
                "<li><strong>Rote Blutkörperchen &amp; Hämoglobin</strong> — erkennen "
                "Anämie, Dehydration und Knochenmarkprobleme</li>"
                "<li><strong>Weiße Blutkörperchen</strong> — zeigen Infektionen, "
                "Immunstörungen oder allergische Reaktionen an</li>"
                "<li><strong>Thrombozyten</strong> — bewerten die Gerinnungsfähigkeit "
                "und das Blutungsrisiko</li>"
                "</ul>"
                "<p>Ein Blutbild ist schnell, kostengünstig und in fast jeder "
                "Routineuntersuchung enthalten.</p>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="Umfassendes Stoffwechselpanel (CMP / BMP)",
            body_html=(
                "<p>Das CMP misst 14 Substanzen in Ihrem Blut, die die Funktion von "
                "Nieren, Leber und Stoffwechsel widerspiegeln:</p>"
                "<ul>"
                "<li><strong>Glukose</strong> — Screening auf Diabetes und "
                "Prädiabetes</li>"
                "<li><strong>BUN &amp; Kreatinin</strong> — bewerten die "
                "Nierenfunktion</li>"
                "<li><strong>ALT &amp; AST</strong> — beurteilen die "
                "Lebergesundheit</li>"
                "<li><strong>Elektrolyte (Na, K, Cl, CO₂)</strong> — überwachen "
                "Flüssigkeitshaushalt, Nervenfunktion und Säure-Basen-Status</li>"
                "<li><strong>Kalzium</strong> — wichtig für Knochen, Herz und "
                "Nerven</li>"
                "<li><strong>Albumin &amp; Gesamtprotein</strong> — spiegeln "
                "Ernährungszustand und Leber-/Nierenfunktion wider</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="Lipidpanel — Cholesterin &amp; Triglyceride",
            body_html=(
                "<p>Herzkrankheiten sind weltweit die häufigste Todesursache. Ein "
                "Lipidpanel misst die Blutfette, die das kardiovaskuläre Risiko direkt "
                "beeinflussen:</p>"
                "<ul>"
                "<li><strong>Gesamtcholesterin</strong> — wünschenswert "
                "&lt; 200 mg/dL</li>"
                "<li><strong>LDL (&bdquo;schlechtes&ldquo;) Cholesterin</strong> — lagert sich in "
                "Arterien ab; optimal &lt; 100 mg/dL</li>"
                "<li><strong>HDL (&bdquo;gutes&ldquo;) Cholesterin</strong> — entfernt Cholesterin "
                "aus Arterien; Ziel ≥ 60 mg/dL</li>"
                "<li><strong>Triglyceride</strong> — mit Herzkrankheit und Pankreatitis "
                "verbunden; normal &lt; 150 mg/dL</li>"
                "</ul>"
                "<p>Erwachsene ab 20 Jahren sollten mindestens alle 4–6 Jahre ein "
                "Lipidpanel durchführen lassen.</p>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="Schilddrüsenpanel — TSH, T3 &amp; T4",
            body_html=(
                "<p>Ihre Schilddrüse steuert Stoffwechsel, Energie und "
                "Körpertemperatur. Schilddrüsenerkrankungen betreffen schätzungsweise "
                "12 % der Bevölkerung.</p>"
                "<ul>"
                "<li><strong>TSH</strong> — primärer Screening-Marker; normal "
                "0,4–4,0 mIU/L</li>"
                "<li><strong>Freies T4</strong> — das Hauptschilddrüsenhormon</li>"
                "<li><strong>Freies T3</strong> — das aktivere Hormon</li>"
                "</ul>"
                "<p><strong>Hypothyreose</strong> (hoher TSH, niedriges T4) verursacht "
                "Müdigkeit, Gewichtszunahme und Kälteempfindlichkeit. "
                "<strong>Hyperthyreose</strong> (niedriger TSH, hohes T4) verursacht "
                "Gewichtsverlust, Herzrasen und Angstgefühle.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="Diabetes-Screening — HbA1c &amp; Nüchternglukose",
            body_html=(
                "<p>Über 10 % der Erwachsenen weltweit haben Diabetes, und ein erheblicher "
                "Anteil ist nicht diagnostiziert:</p>"
                "<ul>"
                "<li><strong>Nüchternblutzucker</strong> — normal &lt; 100 mg/dL; "
                "Prädiabetes 100–125 mg/dL; Diabetes ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — spiegelt den durchschnittlichen Blutzucker "
                "der letzten 2–3 Monate wider. Normal &lt; 5,7 %; Prädiabetes "
                "5,7–6,4 %; Diabetes ≥ 6,5 %</li>"
                "</ul>"
                "<p>HbA1c ist besonders wertvoll, da es kein Nüchternsein erfordert und "
                "nicht von täglichen Schwankungen beeinflusst wird.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="Vitamin- &amp; Mineralstofftests — D, B12, Eisen &amp; Ferritin",
            body_html=(
                "<p>Nährstoffmängel sind überraschend häufig. Die wichtigsten jährlichen "
                "Tests:</p>"
                "<ul>"
                "<li><strong>Vitamin D (25-OH)</strong> — wichtig für Knochen, Immunität "
                "und Stimmung. Optimal: 30–60 ng/mL.</li>"
                "<li><strong>Vitamin B12</strong> — entscheidend für Nervenfunktion und "
                "Bildung roter Blutkörperchen. Mangel verursacht Müdigkeit und kognitive "
                "Probleme.</li>"
                "<li><strong>Eisen &amp; Ferritin</strong> — Eisen wird für den "
                "Sauerstofftransport benötigt; Ferritin spiegelt die Eisenspeicher "
                "wider.</li>"
                "</ul>"
                "<p>Diese Tests sind kostengünstig und Mängel lassen sich leicht durch "
                "Supplementierung beheben.</p>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="Entzündungsmarker — CRP &amp; BSG",
            body_html=(
                "<p>Chronische niedriggradige Entzündungen werden zunehmend mit "
                "Herzkrankheiten und Autoimmunerkrankungen in Verbindung gebracht:</p>"
                "<ul>"
                "<li><strong>CRP (C-reaktives Protein)</strong> — hs-CRP &lt; 1 mg/L = "
                "niedriges kardiovaskuläres Risiko; 1–3 mg/L = moderat; "
                "&gt; 3 mg/L = hohes Risiko.</li>"
                "<li><strong>BSG (Blutsenkungsgeschwindigkeit)</strong> — misst, wie "
                "schnell rote Blutkörperchen absinken. Erhöhte BSG deutet auf Entzündung "
                "hin, ist aber unspezifisch.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="Wie oft testen &amp; wie NoryaAI hilft",
            body_html=(
                "<p>Die Testhäufigkeit hängt von Alter, Risikofaktoren und bestehenden "
                "Erkrankungen ab:</p>"
                "<ul>"
                "<li><strong>18–30 Jahre</strong> — alle 2–3 Jahre Blutbild, "
                "Stoffwechselpanel und Lipidpanel</li>"
                "<li><strong>30–45 Jahre</strong> — jährlich Blutbild, CMP, Lipidpanel; "
                "alle 2–3 Jahre TSH und HbA1c</li>"
                "<li><strong>45+ Jahre</strong> — jährliches Vollpanel inkl. Blutbild, "
                "CMP, Lipide, Schilddrüse, HbA1c, Vitamin D, B12, Ferritin, CRP</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> macht das Verstehen Ihrer Ergebnisse "
                "mühelos. Laden Sie Ihren Laborbericht hoch — PDF oder Foto — und "
                "NoryaAI wird:</p>"
                "<ul>"
                "<li>Jeden Biomarker auf Ihrem Bericht identifizieren</li>"
                "<li>Jeden Wert mit alters- und geschlechtsspezifischen Referenzbereichen "
                "vergleichen</li>"
                "<li>Auffällige Ergebnisse mit klaren Erklärungen kennzeichnen</li>"
                "<li>Eine strukturierte, arztfertige Gesundheitsübersicht erstellen</li>"
                "</ul>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Spanish
# ---------------------------------------------------------------------------
def _sections_es():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="¿Por qué importan los análisis de sangre anuales?",
            body_html=(
                "<p>Los análisis de sangre son una de las formas más efectivas de detectar "
                "problemas de salud antes de que se agraven. Muchas enfermedades — como "
                "la diabetes, los trastornos tiroideos, las enfermedades renales y el "
                "colesterol alto — se desarrollan silenciosamente durante años sin "
                "síntomas evidentes.</p>"
                "<p>Un panel de sangre anual establece una <strong>línea base</strong> "
                "para su salud. Al rastrear sus valores año tras año, usted y su médico "
                "pueden detectar tendencias tempranamente e intervenir antes de que un "
                "pequeño desequilibrio se convierta en una enfermedad crónica.</p>"
                "<ul>"
                "<li><strong>Detección temprana</strong> — detecte prediabetes o "
                "deficiencia de hierro antes de que aparezcan los síntomas</li>"
                "<li><strong>Seguimiento de tendencias</strong> — un solo resultado "
                "anormal puede ser ruido; una tendencia ascendente a lo largo de los "
                "años es una señal</li>"
                "<li><strong>Ahorro preventivo</strong> — tratar afecciones en etapa "
                "temprana cuesta mucho menos que manejar enfermedades avanzadas</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="Hemograma completo (CBC)",
            body_html=(
                "<p>El hemograma es el análisis de sangre fundamental. Evalúa glóbulos "
                "rojos, glóbulos blancos, hemoglobina, hematocrito y plaquetas.</p>"
                "<ul>"
                "<li><strong>Glóbulos rojos y hemoglobina</strong> — detectan anemia, "
                "deshidratación y problemas de médula ósea</li>"
                "<li><strong>Glóbulos blancos</strong> — revelan infecciones, trastornos "
                "inmunitarios o respuestas alérgicas</li>"
                "<li><strong>Plaquetas</strong> — evalúan la capacidad de coagulación</li>"
                "</ul>"
                "<p>El hemograma es rápido, económico y está incluido en prácticamente "
                "todos los chequeos de rutina.</p>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="Panel Metabólico Completo (CMP / BMP)",
            body_html=(
                "<p>El CMP mide 14 sustancias en su sangre que reflejan el funcionamiento "
                "de los riñones, el hígado y el metabolismo:</p>"
                "<ul>"
                "<li><strong>Glucosa</strong> — detección de diabetes y prediabetes</li>"
                "<li><strong>BUN y creatinina</strong> — evalúan la función renal</li>"
                "<li><strong>ALT y AST</strong> — evalúan la salud del hígado</li>"
                "<li><strong>Electrolitos (Na, K, Cl, CO₂)</strong> — monitorean el "
                "equilibrio de líquidos y la función nerviosa</li>"
                "<li><strong>Calcio</strong> — importante para huesos, corazón y "
                "nervios</li>"
                "<li><strong>Albúmina y proteínas totales</strong> — reflejan el estado "
                "nutricional y la función hepática/renal</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="Panel lipídico — Colesterol y triglicéridos",
            body_html=(
                "<p>Las enfermedades cardíacas siguen siendo la principal causa de muerte "
                "en el mundo. Un panel lipídico mide las grasas en la sangre que influyen "
                "directamente en el riesgo cardiovascular:</p>"
                "<ul>"
                "<li><strong>Colesterol total</strong> — deseable &lt; 200 mg/dL</li>"
                "<li><strong>Colesterol LDL (\"malo\")</strong> — se acumula en las "
                "arterias; óptimo &lt; 100 mg/dL</li>"
                "<li><strong>Colesterol HDL (\"bueno\")</strong> — elimina el colesterol "
                "de las arterias; objetivo ≥ 60 mg/dL</li>"
                "<li><strong>Triglicéridos</strong> — normal &lt; 150 mg/dL</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="Panel tiroideo — TSH, T3 y T4",
            body_html=(
                "<p>La tiroides controla el metabolismo, la energía y la temperatura "
                "corporal. Los trastornos tiroideos afectan aproximadamente al 12 % de "
                "la población.</p>"
                "<ul>"
                "<li><strong>TSH</strong> — marcador de detección primario; normal "
                "0,4–4,0 mUI/L</li>"
                "<li><strong>T4 libre</strong> — la principal hormona tiroidea</li>"
                "<li><strong>T3 libre</strong> — la hormona más activa</li>"
                "</ul>"
                "<p><strong>Hipotiroidismo</strong> (TSH alto, T4 bajo) causa fatiga, "
                "aumento de peso e intolerancia al frío. <strong>Hipertiroidismo</strong> "
                "(TSH bajo, T4 alto) causa pérdida de peso, taquicardia y ansiedad.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="Detección de diabetes — HbA1c y glucosa en ayunas",
            body_html=(
                "<p>Más del 10 % de los adultos en todo el mundo tienen diabetes:</p>"
                "<ul>"
                "<li><strong>Glucosa en ayunas</strong> — normal &lt; 100 mg/dL; "
                "prediabetes 100–125 mg/dL; diabetes ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — refleja el azúcar en sangre promedio de "
                "los últimos 2-3 meses. Normal &lt; 5,7 %; prediabetes 5,7–6,4 %; "
                "diabetes ≥ 6,5 %</li>"
                "</ul>"
                "<p>La HbA1c es especialmente valiosa porque no requiere ayuno y no se "
                "ve afectada por las fluctuaciones diarias.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="Pruebas de vitaminas y minerales — D, B12, hierro y ferritina",
            body_html=(
                "<p>Las deficiencias nutricionales son sorprendentemente comunes:</p>"
                "<ul>"
                "<li><strong>Vitamina D (25-OH)</strong> — esencial para huesos, "
                "inmunidad y estado de ánimo. Óptimo: 30–60 ng/mL.</li>"
                "<li><strong>Vitamina B12</strong> — crítica para la función nerviosa. "
                "La deficiencia causa fatiga, hormigueo y problemas cognitivos.</li>"
                "<li><strong>Hierro y ferritina</strong> — el hierro es necesario para "
                "el transporte de oxígeno; la ferritina refleja las reservas de hierro. "
                "La ferritina baja es el marcador más temprano de deficiencia de "
                "hierro.</li>"
                "</ul>"
                "<p>Estas pruebas son económicas y las deficiencias se corrigen "
                "fácilmente con suplementación.</p>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="Marcadores de inflamación — PCR y VSG",
            body_html=(
                "<p>La inflamación crónica de bajo grado se vincula cada vez más con "
                "enfermedades cardíacas y autoinmunes:</p>"
                "<ul>"
                "<li><strong>PCR (Proteína C Reactiva)</strong> — hs-PCR &lt; 1 mg/L = "
                "riesgo cardiovascular bajo; 1–3 mg/L = moderado; "
                "&gt; 3 mg/L = alto.</li>"
                "<li><strong>VSG (Velocidad de Sedimentación Globular)</strong> — mide "
                "la velocidad a la que los glóbulos rojos se sedimentan. Una VSG elevada "
                "sugiere inflamación pero es inespecífica.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="Frecuencia de las pruebas y cómo ayuda NoryaAI",
            body_html=(
                "<p>La frecuencia depende de la edad, factores de riesgo y condiciones "
                "existentes:</p>"
                "<ul>"
                "<li><strong>18–30 años</strong> — hemograma, panel metabólico y "
                "lipídico cada 2–3 años</li>"
                "<li><strong>30–45 años</strong> — hemograma, CMP y lípidos anuales; "
                "TSH y HbA1c cada 2–3 años</li>"
                "<li><strong>45+ años</strong> — panel completo anual incluyendo "
                "hemograma, CMP, lípidos, tiroides, HbA1c, vitamina D, B12, ferritina "
                "y PCR</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> facilita la comprensión de sus resultados. "
                "Suba su informe de laboratorio — PDF o foto — y NoryaAI:</p>"
                "<ul>"
                "<li>Identificará cada biomarcador de su informe</li>"
                "<li>Comparará cada valor con rangos de referencia específicos por edad "
                "y sexo</li>"
                "<li>Marcará resultados anormales con explicaciones claras</li>"
                "<li>Generará un resumen de salud estructurado, listo para su médico</li>"
                "</ul>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# French
# ---------------------------------------------------------------------------
def _sections_fr():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="Pourquoi les bilans sanguins annuels sont importants",
            body_html=(
                "<p>Les analyses de sang sont l'un des moyens les plus efficaces pour "
                "détecter les problèmes de santé avant qu'ils ne deviennent graves. "
                "De nombreuses maladies — diabète, troubles thyroïdiens, maladies "
                "rénales, hypercholestérolémie — se développent silencieusement pendant "
                "des années sans symptômes évidents.</p>"
                "<p>Un bilan sanguin annuel établit une <strong>valeur de référence"
                "</strong> pour votre santé. En suivant vos valeurs d'année en année, "
                "vous et votre médecin pouvez repérer les tendances précocement.</p>"
                "<ul>"
                "<li><strong>Détection précoce</strong> — repérer le prédiabète ou la "
                "carence en fer avant l'apparition des symptômes</li>"
                "<li><strong>Suivi des tendances</strong> — un seul résultat anormal "
                "peut être du bruit ; une tendance à la hausse sur plusieurs années est "
                "un signal</li>"
                "<li><strong>Économies préventives</strong> — traiter les stades "
                "précoces coûte bien moins que gérer une maladie avancée</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="Numération formule sanguine (NFS / CBC)",
            body_html=(
                "<p>La NFS est l'analyse de sang fondamentale. Elle évalue les globules "
                "rouges, les globules blancs, l'hémoglobine, l'hématocrite et les "
                "plaquettes.</p>"
                "<ul>"
                "<li><strong>Globules rouges et hémoglobine</strong> — détectent "
                "l'anémie, la déshydratation et les problèmes de moelle osseuse</li>"
                "<li><strong>Globules blancs</strong> — révèlent les infections et "
                "les troubles immunitaires</li>"
                "<li><strong>Plaquettes</strong> — évaluent la capacité de "
                "coagulation</li>"
                "</ul>"
                "<p>La NFS est rapide, peu coûteuse et incluse dans pratiquement "
                "tout bilan de routine.</p>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="Bilan métabolique complet (CMP / BMP)",
            body_html=(
                "<p>Le CMP mesure 14 substances dans votre sang reflétant le "
                "fonctionnement des reins, du foie et du métabolisme :</p>"
                "<ul>"
                "<li><strong>Glucose</strong> — dépistage du diabète et du "
                "prédiabète</li>"
                "<li><strong>Urée et créatinine</strong> — évaluent la fonction "
                "rénale</li>"
                "<li><strong>ALT et AST</strong> — évaluent la santé du foie</li>"
                "<li><strong>Électrolytes (Na, K, Cl, CO₂)</strong> — surveillent "
                "l'équilibre hydrique et la fonction nerveuse</li>"
                "<li><strong>Calcium</strong> — important pour les os, le cœur et les "
                "nerfs</li>"
                "<li><strong>Albumine et protéines totales</strong> — reflètent l'état "
                "nutritionnel et la fonction hépatique/rénale</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="Bilan lipidique — Cholestérol et triglycérides",
            body_html=(
                "<p>Les maladies cardiovasculaires restent la première cause de décès "
                "dans le monde. Un bilan lipidique mesure les graisses sanguines qui "
                "influencent directement le risque cardiovasculaire :</p>"
                "<ul>"
                "<li><strong>Cholestérol total</strong> — souhaitable "
                "&lt; 200 mg/dL</li>"
                "<li><strong>Cholestérol LDL (« mauvais »)</strong> — s'accumule dans "
                "les artères ; optimal &lt; 100 mg/dL</li>"
                "<li><strong>Cholestérol HDL (« bon »)</strong> — élimine le "
                "cholestérol des artères ; objectif ≥ 60 mg/dL</li>"
                "<li><strong>Triglycérides</strong> — normal &lt; 150 mg/dL</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="Bilan thyroïdien — TSH, T3 et T4",
            body_html=(
                "<p>La thyroïde contrôle le métabolisme, l'énergie et la température "
                "corporelle. Les troubles thyroïdiens touchent environ 12 % de la "
                "population.</p>"
                "<ul>"
                "<li><strong>TSH</strong> — marqueur de dépistage primaire ; normal "
                "0,4–4,0 mUI/L</li>"
                "<li><strong>T4 libre</strong> — la principale hormone thyroïdienne</li>"
                "<li><strong>T3 libre</strong> — l'hormone la plus active</li>"
                "</ul>"
                "<p><strong>L'hypothyroïdie</strong> (TSH élevée, T4 basse) provoque "
                "fatigue, prise de poids et intolérance au froid. "
                "<strong>L'hyperthyroïdie</strong> (TSH basse, T4 élevée) provoque perte "
                "de poids, tachycardie et anxiété.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="Dépistage du diabète — HbA1c et glycémie à jeun",
            body_html=(
                "<p>Plus de 10 % des adultes dans le monde sont diabétiques :</p>"
                "<ul>"
                "<li><strong>Glycémie à jeun</strong> — normale &lt; 100 mg/dL ; "
                "prédiabète 100–125 mg/dL ; diabète ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — reflète la glycémie moyenne des 2-3 "
                "derniers mois. Normale &lt; 5,7 % ; prédiabète 5,7–6,4 % ; "
                "diabète ≥ 6,5 %</li>"
                "</ul>"
                "<p>L'HbA1c est particulièrement précieuse car elle ne nécessite pas "
                "de jeûne et n'est pas affectée par les fluctuations quotidiennes.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="Tests de vitamines et minéraux — D, B12, fer et ferritine",
            body_html=(
                "<p>Les carences nutritionnelles sont étonnamment fréquentes :</p>"
                "<ul>"
                "<li><strong>Vitamine D (25-OH)</strong> — essentielle pour les os, "
                "l'immunité et l'humeur. Optimal : 30–60 ng/mL.</li>"
                "<li><strong>Vitamine B12</strong> — essentielle pour la fonction "
                "nerveuse. La carence provoque fatigue, picotements et problèmes "
                "cognitifs.</li>"
                "<li><strong>Fer et ferritine</strong> — le fer est nécessaire au "
                "transport de l'oxygène ; la ferritine reflète les réserves en fer.</li>"
                "</ul>"
                "<p>Ces tests sont peu coûteux et les carences se corrigent facilement "
                "par supplémentation.</p>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="Marqueurs d'inflammation — CRP et VS",
            body_html=(
                "<p>L'inflammation chronique de bas grade est de plus en plus liée aux "
                "maladies cardiovasculaires et auto-immunes :</p>"
                "<ul>"
                "<li><strong>CRP (Protéine C-réactive)</strong> — hs-CRP "
                "&lt; 1 mg/L = risque cardiovasculaire faible ; 1–3 mg/L = modéré ; "
                "&gt; 3 mg/L = élevé.</li>"
                "<li><strong>VS (Vitesse de Sédimentation)</strong> — mesure la vitesse "
                "à laquelle les globules rouges se déposent. Une VS élevée suggère une "
                "inflammation mais est non spécifique.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="Fréquence des tests et comment NoryaAI vous aide",
            body_html=(
                "<p>La fréquence dépend de l'âge, des facteurs de risque et des "
                "conditions existantes :</p>"
                "<ul>"
                "<li><strong>18–30 ans</strong> — NFS, bilan métabolique et lipidique "
                "tous les 2–3 ans</li>"
                "<li><strong>30–45 ans</strong> — NFS, CMP et lipides annuels ; TSH et "
                "HbA1c tous les 2–3 ans</li>"
                "<li><strong>45+ ans</strong> — bilan annuel complet incluant NFS, CMP, "
                "lipides, thyroïde, HbA1c, vitamine D, B12, ferritine et CRP</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> facilite la compréhension de vos résultats. "
                "Téléchargez votre rapport de laboratoire — PDF ou photo — et NoryaAI :</p>"
                "<ul>"
                "<li>Identifiera chaque biomarqueur de votre rapport</li>"
                "<li>Comparera chaque valeur aux plages de référence spécifiques à l'âge "
                "et au sexe</li>"
                "<li>Signalera les résultats anormaux avec des explications claires</li>"
                "<li>Générera un résumé de santé structuré, prêt pour votre médecin</li>"
                "</ul>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Italian
# ---------------------------------------------------------------------------
def _sections_it():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="Perché gli esami del sangue annuali sono importanti",
            body_html=(
                "<p>Gli esami del sangue sono uno dei modi più efficaci per individuare "
                "problemi di salute prima che diventino gravi. Molte condizioni — tra cui "
                "diabete, disturbi tiroidei, malattie renali e colesterolo alto — si "
                "sviluppano silenziosamente per anni senza sintomi evidenti.</p>"
                "<p>Un pannello ematico annuale stabilisce un <strong>valore di base"
                "</strong> per la vostra salute. Monitorando i valori anno dopo anno, "
                "voi e il vostro medico potete individuare le tendenze precocemente.</p>"
                "<ul>"
                "<li><strong>Rilevamento precoce</strong> — individuare il prediabete o "
                "la carenza di ferro prima della comparsa dei sintomi</li>"
                "<li><strong>Monitoraggio delle tendenze</strong> — un singolo risultato "
                "anomalo può essere casuale; una tendenza al rialzo nel tempo è un "
                "segnale</li>"
                "<li><strong>Risparmio preventivo</strong> — trattare le condizioni in "
                "fase iniziale costa molto meno che gestire malattie avanzate</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="Emocromo completo (CBC)",
            body_html=(
                "<p>L'emocromo è l'esame del sangue fondamentale. Valuta globuli rossi, "
                "globuli bianchi, emoglobina, ematocrito e piastrine.</p>"
                "<ul>"
                "<li><strong>Globuli rossi ed emoglobina</strong> — rilevano anemia, "
                "disidratazione e problemi del midollo osseo</li>"
                "<li><strong>Globuli bianchi</strong> — rivelano infezioni, disturbi "
                "immunitari o risposte allergiche</li>"
                "<li><strong>Piastrine</strong> — valutano la capacità di "
                "coagulazione</li>"
                "</ul>"
                "<p>L'emocromo è rapido, economico e incluso in praticamente tutti i "
                "controlli di routine.</p>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="Pannello metabolico completo (CMP / BMP)",
            body_html=(
                "<p>Il CMP misura 14 sostanze nel sangue che riflettono il funzionamento "
                "di reni, fegato e metabolismo:</p>"
                "<ul>"
                "<li><strong>Glucosio</strong> — screening per diabete e prediabete</li>"
                "<li><strong>BUN e creatinina</strong> — valutano la funzione renale</li>"
                "<li><strong>ALT e AST</strong> — valutano la salute del fegato</li>"
                "<li><strong>Elettroliti (Na, K, Cl, CO₂)</strong> — monitorano "
                "l'equilibrio dei fluidi e la funzione nervosa</li>"
                "<li><strong>Calcio</strong> — importante per ossa, cuore e nervi</li>"
                "<li><strong>Albumina e proteine totali</strong> — riflettono lo stato "
                "nutrizionale e la funzione epatica/renale</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="Profilo lipidico — Colesterolo e trigliceridi",
            body_html=(
                "<p>Le malattie cardiache rimangono la principale causa di morte nel "
                "mondo. Il profilo lipidico misura i grassi nel sangue che influenzano "
                "direttamente il rischio cardiovascolare:</p>"
                "<ul>"
                "<li><strong>Colesterolo totale</strong> — desiderabile "
                "&lt; 200 mg/dL</li>"
                "<li><strong>Colesterolo LDL (\"cattivo\")</strong> — si accumula nelle "
                "arterie; ottimale &lt; 100 mg/dL</li>"
                "<li><strong>Colesterolo HDL (\"buono\")</strong> — rimuove il "
                "colesterolo dalle arterie; obiettivo ≥ 60 mg/dL</li>"
                "<li><strong>Trigliceridi</strong> — normale &lt; 150 mg/dL</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="Pannello tiroideo — TSH, T3 e T4",
            body_html=(
                "<p>La tiroide controlla il metabolismo, l'energia e la temperatura "
                "corporea. I disturbi tiroidei colpiscono circa il 12% della "
                "popolazione.</p>"
                "<ul>"
                "<li><strong>TSH</strong> — marcatore di screening primario; normale "
                "0,4–4,0 mUI/L</li>"
                "<li><strong>T4 libero</strong> — il principale ormone tiroideo</li>"
                "<li><strong>T3 libero</strong> — l'ormone più attivo</li>"
                "</ul>"
                "<p><strong>L'ipotiroidismo</strong> (TSH alto, T4 basso) causa "
                "stanchezza, aumento di peso e intolleranza al freddo. "
                "<strong>L'ipertiroidismo</strong> (TSH basso, T4 alto) causa perdita "
                "di peso, tachicardia e ansia.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="Screening del diabete — HbA1c e glicemia a digiuno",
            body_html=(
                "<p>Oltre il 10% degli adulti nel mondo ha il diabete:</p>"
                "<ul>"
                "<li><strong>Glicemia a digiuno</strong> — normale &lt; 100 mg/dL; "
                "prediabete 100–125 mg/dL; diabete ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — riflette la glicemia media degli ultimi "
                "2-3 mesi. Normale &lt; 5,7%; prediabete 5,7–6,4%; "
                "diabete ≥ 6,5%</li>"
                "</ul>"
                "<p>L'HbA1c è particolarmente preziosa perché non richiede il digiuno e "
                "non è influenzata dalle fluttuazioni giornaliere.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="Test di vitamine e minerali — D, B12, ferro e ferritina",
            body_html=(
                "<p>Le carenze nutrizionali sono sorprendentemente comuni:</p>"
                "<ul>"
                "<li><strong>Vitamina D (25-OH)</strong> — essenziale per ossa, "
                "immunità e umore. Ottimale: 30–60 ng/mL.</li>"
                "<li><strong>Vitamina B12</strong> — fondamentale per la funzione "
                "nervosa. La carenza causa stanchezza, formicolio e problemi "
                "cognitivi.</li>"
                "<li><strong>Ferro e ferritina</strong> — il ferro è necessario per il "
                "trasporto dell'ossigeno; la ferritina riflette le riserve di ferro.</li>"
                "</ul>"
                "<p>Questi test sono economici e le carenze si correggono facilmente con "
                "l'integrazione.</p>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="Marcatori di infiammazione — PCR e VES",
            body_html=(
                "<p>L'infiammazione cronica di basso grado è sempre più collegata a "
                "malattie cardiovascolari e autoimmuni:</p>"
                "<ul>"
                "<li><strong>PCR (Proteina C-reattiva)</strong> — hs-PCR &lt; 1 mg/L = "
                "rischio cardiovascolare basso; 1–3 mg/L = moderato; "
                "&gt; 3 mg/L = alto.</li>"
                "<li><strong>VES (Velocità di Eritrosedimentazione)</strong> — misura la "
                "velocità con cui i globuli rossi si depositano. Una VES elevata suggerisce "
                "infiammazione ma è aspecifica.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="Frequenza dei test e come NoryaAI ti aiuta",
            body_html=(
                "<p>La frequenza dipende dall'età, dai fattori di rischio e dalle "
                "condizioni esistenti:</p>"
                "<ul>"
                "<li><strong>18–30 anni</strong> — emocromo, pannello metabolico e "
                "lipidico ogni 2–3 anni</li>"
                "<li><strong>30–45 anni</strong> — emocromo, CMP e lipidi annuali; TSH "
                "e HbA1c ogni 2–3 anni</li>"
                "<li><strong>45+ anni</strong> — pannello annuale completo inclusi "
                "emocromo, CMP, lipidi, tiroide, HbA1c, vitamina D, B12, ferritina e "
                "PCR</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> rende semplice la comprensione dei risultati. "
                "Carica il tuo referto — PDF o foto — e NoryaAI:</p>"
                "<ul>"
                "<li>Identificherà ogni biomarcatore nel referto</li>"
                "<li>Confronterà ogni valore con intervalli di riferimento specifici per "
                "età e sesso</li>"
                "<li>Segnalerà i risultati anomali con spiegazioni chiare</li>"
                "<li>Genererà un riepilogo sanitario strutturato, pronto per il "
                "medico</li>"
                "</ul>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hebrew
# ---------------------------------------------------------------------------
def _sections_he():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="למה בדיקות דם שנתיות חשובות?",
            body_html=(
                "<p>בדיקות דם הן אחת הדרכים היעילות ביותר לזהות בעיות בריאותיות "
                "לפני שהן הופכות לחמורות. מצבים רבים — כולל סוכרת, הפרעות בבלוטת "
                "התריס, מחלות כליות וכולסטרול גבוה — מתפתחים בשקט במשך שנים ללא "
                "תסמינים ברורים.</p>"
                "<p>פאנל דם שנתי יוצר <strong>קו בסיס</strong> לבריאות שלך. "
                "מעקב אחר הערכים שלך משנה לשנה מאפשר לך ולרופא לזהות מגמות "
                "מוקדם ולהתערב לפני שחוסר איזון קטן הופך למצב כרוני.</p>"
                "<ul>"
                "<li><strong>גילוי מוקדם</strong> — זיהוי טרום-סוכרת או מחסור בברזל "
                "לפני הופעת תסמינים</li>"
                "<li><strong>מעקב מגמות</strong> — תוצאה חריגה בודדת עשויה להיות "
                "רעש; מגמה עולה לאורך שנים היא אות</li>"
                "<li><strong>חיסכון מונע</strong> — טיפול במצבים בשלב מוקדם עולה "
                "הרבה פחות מניהול מחלה מתקדמת</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="ספירת דם מלאה (CBC)",
            body_html=(
                "<p>ספירת הדם המלאה היא בדיקת הדם הבסיסית. היא מעריכה כדוריות "
                "דם אדומות, כדוריות דם לבנות, המוגלובין, המטוקריט וטסיות דם.</p>"
                "<ul>"
                "<li><strong>כדוריות אדומות והמוגלובין</strong> — מזהים אנמיה, "
                "התייבשות ובעיות במח העצם</li>"
                "<li><strong>כדוריות לבנות</strong> — חושפים זיהומים, הפרעות "
                "חיסוניות או תגובות אלרגיות</li>"
                "<li><strong>טסיות דם</strong> — מעריכים את יכולת הקרישה</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="פאנל מטבולי מקיף (CMP / BMP)",
            body_html=(
                "<p>ה-CMP מודד 14 חומרים בדם המשקפים את תפקוד הכליות, הכבד "
                "והמטבוליזם:</p>"
                "<ul>"
                "<li><strong>גלוקוז</strong> — סינון לסוכרת וטרום-סוכרת</li>"
                "<li><strong>BUN וקראטינין</strong> — הערכת תפקוד הכליות</li>"
                "<li><strong>ALT ו-AST</strong> — הערכת בריאות הכבד</li>"
                "<li><strong>אלקטרוליטים (Na, K, Cl, CO₂)</strong> — ניטור "
                "מאזן נוזלים ותפקוד עצבי</li>"
                "<li><strong>סידן</strong> — חשוב לעצמות, לב ועצבים</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="פרופיל שומנים — כולסטרול וטריגליצרידים",
            body_html=(
                "<p>מחלות לב הן עדיין גורם המוות המוביל בעולם. פרופיל שומנים מודד "
                "את השומנים בדם המשפיעים ישירות על הסיכון הקרדיווסקולרי:</p>"
                "<ul>"
                "<li><strong>כולסטרול כללי</strong> — רצוי &lt; 200 mg/dL</li>"
                "<li><strong>כולסטרול LDL (\"רע\")</strong> — מצטבר בעורקים; "
                "אופטימלי &lt; 100 mg/dL</li>"
                "<li><strong>כולסטרול HDL (\"טוב\")</strong> — מסיר כולסטרול "
                "מהעורקים; יעד ≥ 60 mg/dL</li>"
                "<li><strong>טריגליצרידים</strong> — תקין &lt; 150 mg/dL</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="פאנל בלוטת התריס — TSH, T3 ו-T4",
            body_html=(
                "<p>בלוטת התריס שולטת במטבוליזם, באנרגיה ובטמפרטורת הגוף. "
                "הפרעות בתריס משפיעות על כ-12% מהאוכלוסייה.</p>"
                "<ul>"
                "<li><strong>TSH</strong> — סמן הסינון הראשי; תקין "
                "0.4–4.0 mIU/L</li>"
                "<li><strong>T4 חופשי</strong> — ההורמון העיקרי של התריס</li>"
                "<li><strong>T3 חופשי</strong> — ההורמון הפעיל יותר</li>"
                "</ul>"
                "<p><strong>תת-פעילות התריס</strong> (TSH גבוה, T4 נמוך) גורמת "
                "לעייפות, עלייה במשקל ורגישות לקור. <strong>יתר-פעילות התריס"
                "</strong> (TSH נמוך, T4 גבוה) גורמת לירידה במשקל, דופק מהיר "
                "וחרדה.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="סינון סוכרת — HbA1c וגלוקוז בצום",
            body_html=(
                "<p>למעלה מ-10% מהמבוגרים בעולם סובלים מסוכרת:</p>"
                "<ul>"
                "<li><strong>גלוקוז בצום</strong> — תקין &lt; 100 mg/dL; "
                "טרום-סוכרת 100–125 mg/dL; סוכרת ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — משקף את ממוצע הסוכר בדם ב-2-3 "
                "החודשים האחרונים. תקין &lt; 5.7%; טרום-סוכרת 5.7–6.4%; "
                "סוכרת ≥ 6.5%</li>"
                "</ul>"
                "<p>HbA1c חשוב במיוחד כי הוא לא דורש צום ולא מושפע "
                "מתנודות יומיות.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="בדיקות ויטמינים ומינרלים — D, B12, ברזל ופריטין",
            body_html=(
                "<p>מחסורים תזונתיים נפוצים באופן מפתיע:</p>"
                "<ul>"
                "<li><strong>ויטמין D (25-OH)</strong> — חיוני לעצמות, חסינות "
                "ומצב רוח. אופטימלי: 30–60 ng/mL.</li>"
                "<li><strong>ויטמין B12</strong> — קריטי לתפקוד עצבי. מחסור גורם "
                "לעייפות, נימול ובעיות קוגניטיביות.</li>"
                "<li><strong>ברזל ופריטין</strong> — ברזל נחוץ להובלת חמצן; "
                "פריטין משקף מאגרי ברזל.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="סמני דלקת — CRP ו-ESR",
            body_html=(
                "<p>דלקת כרונית ברמה נמוכה קשורה יותר ויותר למחלות לב ולמצבים "
                "אוטואימוניים:</p>"
                "<ul>"
                "<li><strong>CRP (חלבון C-ריאקטיבי)</strong> — hs-CRP "
                "&lt; 1 mg/L = סיכון קרדיווסקולרי נמוך; 1–3 mg/L = בינוני; "
                "&gt; 3 mg/L = גבוה.</li>"
                "<li><strong>ESR (שקיעת דם)</strong> — מודד את מהירות שקיעת "
                "כדוריות הדם האדומות. ESR מוגבה מרמז על דלקת אך אינו ספציפי.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="תדירות הבדיקות ואיך NoryaAI עוזר",
            body_html=(
                "<p>תדירות הבדיקות תלויה בגיל, גורמי סיכון ומצבים קיימים:</p>"
                "<ul>"
                "<li><strong>גילאי 18–30</strong> — ספירת דם, פאנל מטבולי "
                "ופרופיל שומנים כל 2–3 שנים</li>"
                "<li><strong>גילאי 30–45</strong> — ספירת דם, CMP ושומנים שנתיים; "
                "TSH ו-HbA1c כל 2–3 שנים</li>"
                "<li><strong>גיל 45+</strong> — פאנל שנתי מלא כולל ספירת דם, CMP, "
                "שומנים, תריס, HbA1c, ויטמין D, B12, פריטין ו-CRP</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> הופך את הבנת התוצאות לפשוטה. "
                "העלה את דוח המעבדה — PDF או תמונה — ו-NoryaAI:</p>"
                "<ul>"
                "<li>יזהה כל סמן ביולוגי בדוח</li>"
                "<li>ישווה כל ערך לטווחי ייחוס ספציפיים לגיל ומגדר</li>"
                "<li>יסמן תוצאות חריגות עם הסברים ברורים</li>"
                "<li>ייצר סיכום בריאותי מובנה, מוכן לרופא</li>"
                "</ul>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hindi
# ---------------------------------------------------------------------------
def _sections_hi():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="वार्षिक रक्त परीक्षण क्यों महत्वपूर्ण हैं?",
            body_html=(
                "<p>रक्त परीक्षण स्वास्थ्य समस्याओं को गंभीर होने से पहले पकड़ने "
                "के सबसे प्रभावी तरीकों में से एक हैं। मधुमेह, थायरॉइड विकार, "
                "गुर्दे की बीमारी और उच्च कोलेस्ट्रॉल जैसी कई स्थितियाँ बिना "
                "स्पष्ट लक्षणों के वर्षों तक चुपचाप विकसित होती हैं।</p>"
                "<p>एक वार्षिक रक्त पैनल आपके स्वास्थ्य के लिए एक "
                "<strong>आधार रेखा</strong> बनाता है। साल दर साल अपने मूल्यों "
                "को ट्रैक करके, आप और आपके डॉक्टर रुझानों को जल्दी पहचान सकते "
                "हैं।</p>"
                "<ul>"
                "<li><strong>शीघ्र पहचान</strong> — लक्षण प्रकट होने से पहले "
                "प्रीडायबिटीज या आयरन की कमी का पता लगाएं</li>"
                "<li><strong>ट्रेंड ट्रैकिंग</strong> — एक असामान्य परिणाम शोर "
                "हो सकता है; वर्षों में बढ़ता रुझान एक संकेत है</li>"
                "<li><strong>निवारक बचत</strong> — प्रारंभिक अवस्था की स्थितियों "
                "का इलाज उन्नत बीमारी के प्रबंधन से कहीं सस्ता है</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="पूर्ण रक्त गणना (CBC)",
            body_html=(
                "<p>CBC मूलभूत रक्त परीक्षण है। यह लाल रक्त कोशिकाओं, श्वेत "
                "रक्त कोशिकाओं, हीमोग्लोबिन, हेमेटोक्रिट और प्लेटलेट्स का "
                "मूल्यांकन करता है।</p>"
                "<ul>"
                "<li><strong>लाल रक्त कोशिकाएं और हीमोग्लोबिन</strong> — एनीमिया, "
                "निर्जलीकरण और अस्थि मज्जा की समस्याओं का पता लगाते हैं</li>"
                "<li><strong>श्वेत रक्त कोशिकाएं</strong> — संक्रमण, प्रतिरक्षा "
                "विकार या एलर्जी प्रतिक्रियाएं प्रकट करती हैं</li>"
                "<li><strong>प्लेटलेट्स</strong> — थक्के बनाने की क्षमता का "
                "मूल्यांकन करते हैं</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="व्यापक मेटाबोलिक पैनल (CMP / BMP)",
            body_html=(
                "<p>CMP आपके रक्त में 14 पदार्थों को मापता है जो गुर्दे, "
                "यकृत और चयापचय के कार्य को दर्शाते हैं:</p>"
                "<ul>"
                "<li><strong>ग्लूकोज</strong> — मधुमेह और प्रीडायबिटीज की "
                "जांच</li>"
                "<li><strong>BUN और क्रिएटिनिन</strong> — गुर्दे की कार्यप्रणाली "
                "का मूल्यांकन</li>"
                "<li><strong>ALT और AST</strong> — यकृत स्वास्थ्य का "
                "मूल्यांकन</li>"
                "<li><strong>इलेक्ट्रोलाइट्स (Na, K, Cl, CO₂)</strong> — "
                "द्रव संतुलन और तंत्रिका कार्य की निगरानी</li>"
                "<li><strong>कैल्शियम</strong> — हड्डियों, हृदय और "
                "तंत्रिकाओं के लिए महत्वपूर्ण</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="लिपिड पैनल — कोलेस्ट्रॉल और ट्राइग्लिसराइड्स",
            body_html=(
                "<p>हृदय रोग दुनिया भर में मृत्यु का प्रमुख कारण बना हुआ है। "
                "लिपिड पैनल रक्त में वसा को मापता है:</p>"
                "<ul>"
                "<li><strong>कुल कोलेस्ट्रॉल</strong> — वांछनीय "
                "&lt; 200 mg/dL</li>"
                "<li><strong>LDL (\"खराब\") कोलेस्ट्रॉल</strong> — धमनियों में "
                "जमा होता है; इष्टतम &lt; 100 mg/dL</li>"
                "<li><strong>HDL (\"अच्छा\") कोलेस्ट्रॉल</strong> — धमनियों से "
                "कोलेस्ट्रॉल हटाता है; लक्ष्य ≥ 60 mg/dL</li>"
                "<li><strong>ट्राइग्लिसराइड्स</strong> — सामान्य "
                "&lt; 150 mg/dL</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="थायरॉइड पैनल — TSH, T3 और T4",
            body_html=(
                "<p>आपकी थायरॉइड ग्रंथि चयापचय, ऊर्जा और शरीर के तापमान "
                "को नियंत्रित करती है। थायरॉइड विकार लगभग 12% आबादी को "
                "प्रभावित करते हैं।</p>"
                "<ul>"
                "<li><strong>TSH</strong> — प्राथमिक स्क्रीनिंग मार्कर; "
                "सामान्य 0.4–4.0 mIU/L</li>"
                "<li><strong>फ्री T4</strong> — मुख्य थायरॉइड हार्मोन</li>"
                "<li><strong>फ्री T3</strong> — अधिक सक्रिय हार्मोन</li>"
                "</ul>"
                "<p><strong>हाइपोथायरायडिज्म</strong> (उच्च TSH, कम T4) थकान, "
                "वजन बढ़ना और ठंड असहिष्णुता का कारण बनता है। "
                "<strong>हाइपरथायरायडिज्म</strong> (कम TSH, उच्च T4) वजन घटना, "
                "तेज़ दिल की धड़कन और चिंता का कारण बनता है।</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="मधुमेह जांच — HbA1c और उपवास ग्लूकोज",
            body_html=(
                "<p>दुनिया भर में 10% से अधिक वयस्कों को मधुमेह है:</p>"
                "<ul>"
                "<li><strong>उपवास रक्त शर्करा</strong> — सामान्य "
                "&lt; 100 mg/dL; प्रीडायबिटीज 100–125 mg/dL; "
                "मधुमेह ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — पिछले 2-3 महीनों की औसत रक्त "
                "शर्करा को दर्शाता है। सामान्य &lt; 5.7%; प्रीडायबिटीज "
                "5.7–6.4%; मधुमेह ≥ 6.5%</li>"
                "</ul>"
                "<p>HbA1c विशेष रूप से मूल्यवान है क्योंकि इसके लिए उपवास "
                "की आवश्यकता नहीं होती और यह दैनिक उतार-चढ़ाव से प्रभावित "
                "नहीं होता।</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="विटामिन और खनिज परीक्षण — D, B12, आयरन और फेरिटिन",
            body_html=(
                "<p>पोषक तत्वों की कमी आश्चर्यजनक रूप से आम है:</p>"
                "<ul>"
                "<li><strong>विटामिन D (25-OH)</strong> — हड्डियों, प्रतिरक्षा "
                "और मनोदशा के लिए आवश्यक। इष्टतम: 30–60 ng/mL।</li>"
                "<li><strong>विटामिन B12</strong> — तंत्रिका कार्य के लिए "
                "महत्वपूर्ण। कमी से थकान, झुनझुनी और संज्ञानात्मक समस्याएं "
                "होती हैं।</li>"
                "<li><strong>आयरन और फेरिटिन</strong> — आयरन ऑक्सीजन "
                "परिवहन के लिए आवश्यक है; फेरिटिन आयरन भंडार को "
                "दर्शाता है।</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="सूजन मार्कर — CRP और ESR",
            body_html=(
                "<p>पुरानी निम्न-स्तरीय सूजन हृदय रोग और स्वप्रतिरक्षी "
                "स्थितियों से तेजी से जुड़ी हुई है:</p>"
                "<ul>"
                "<li><strong>CRP (सी-रिएक्टिव प्रोटीन)</strong> — hs-CRP "
                "&lt; 1 mg/L = कम हृदय जोखिम; 1–3 mg/L = मध्यम; "
                "&gt; 3 mg/L = उच्च।</li>"
                "<li><strong>ESR (एरिथ्रोसाइट सेडिमेंटेशन रेट)</strong> — "
                "मापता है कि लाल रक्त कोशिकाएं कितनी तेजी से बैठती हैं। "
                "बढ़ा हुआ ESR सूजन का संकेत देता है लेकिन गैर-विशिष्ट है।</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="कितनी बार जांच करें और NoryaAI कैसे मदद करता है",
            body_html=(
                "<p>परीक्षण की आवृत्ति आपकी उम्र, जोखिम कारकों और मौजूदा "
                "स्थितियों पर निर्भर करती है:</p>"
                "<ul>"
                "<li><strong>18–30 वर्ष</strong> — हर 2–3 साल में CBC, "
                "मेटाबोलिक पैनल और लिपिड पैनल</li>"
                "<li><strong>30–45 वर्ष</strong> — वार्षिक CBC, CMP और लिपिड; "
                "हर 2–3 साल में TSH और HbA1c</li>"
                "<li><strong>45+ वर्ष</strong> — CBC, CMP, लिपिड, थायरॉइड, "
                "HbA1c, विटामिन D, B12, फेरिटिन और CRP सहित पूर्ण "
                "वार्षिक पैनल</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> आपके परिणामों को समझना आसान "
                "बनाता है। अपनी लैब रिपोर्ट अपलोड करें — PDF या फोटो — "
                "और NoryaAI:</p>"
                "<ul>"
                "<li>आपकी रिपोर्ट में हर बायोमार्कर की पहचान करेगा</li>"
                "<li>प्रत्येक मूल्य की तुलना आयु और लिंग-विशिष्ट संदर्भ "
                "सीमाओं से करेगा</li>"
                "<li>असामान्य परिणामों को स्पष्ट व्याख्या के साथ चिह्नित "
                "करेगा</li>"
                "<li>एक संरचित, डॉक्टर-तैयार स्वास्थ्य सारांश तैयार "
                "करेगा</li>"
                "</ul>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Arabic
# ---------------------------------------------------------------------------
def _sections_ar():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-why-annual-tests", level=2,
            heading="لماذا تُعدّ فحوصات الدم السنوية مهمة؟",
            body_html=(
                "<p>تُعدّ فحوصات الدم من أكثر الطرق فعالية للكشف عن المشكلات "
                "الصحية قبل أن تصبح خطيرة. تتطور حالات عديدة — بما في ذلك "
                "السكري واضطرابات الغدة الدرقية وأمراض الكلى وارتفاع "
                "الكوليسترول — بصمت لسنوات دون أعراض واضحة.</p>"
                "<p>يُنشئ فحص الدم السنوي <strong>خط أساس</strong> لصحتك. "
                "من خلال تتبع قيمك سنة بعد سنة، يمكنك أنت وطبيبك اكتشاف "
                "الاتجاهات مبكرًا والتدخل قبل أن يتحول اختلال بسيط إلى "
                "حالة مزمنة.</p>"
                "<ul>"
                "<li><strong>الكشف المبكر</strong> — اكتشاف مقدمات السكري أو "
                "نقص الحديد قبل ظهور الأعراض</li>"
                "<li><strong>تتبع الاتجاهات</strong> — نتيجة غير طبيعية واحدة "
                "قد تكون عشوائية؛ اتجاه صاعد عبر السنوات هو إشارة</li>"
                "<li><strong>التوفير الوقائي</strong> — علاج الحالات في مراحلها "
                "المبكرة يكلف أقل بكثير من إدارة المرض المتقدم</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-cbc", level=2,
            heading="تعداد الدم الكامل (CBC)",
            body_html=(
                "<p>تعداد الدم الكامل هو فحص الدم الأساسي. يُقيّم كريات "
                "الدم الحمراء والبيضاء والهيموغلوبين والهيماتوكريت "
                "والصفائح الدموية.</p>"
                "<ul>"
                "<li><strong>كريات الدم الحمراء والهيموغلوبين</strong> — "
                "تكشف فقر الدم والجفاف ومشاكل نخاع العظم</li>"
                "<li><strong>كريات الدم البيضاء</strong> — تكشف العدوى "
                "واضطرابات المناعة والتفاعلات التحسسية</li>"
                "<li><strong>الصفائح الدموية</strong> — تُقيّم قدرة "
                "التخثر</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-metabolic-panel", level=2,
            heading="لوحة الأيض الشاملة (CMP / BMP)",
            body_html=(
                "<p>يقيس CMP أربع عشرة مادة في دمك تعكس وظائف الكلى "
                "والكبد والأيض:</p>"
                "<ul>"
                "<li><strong>الغلوكوز</strong> — فحص السكري ومقدمات "
                "السكري</li>"
                "<li><strong>BUN والكرياتينين</strong> — تقييم وظائف "
                "الكلى</li>"
                "<li><strong>ALT وAST</strong> — تقييم صحة الكبد</li>"
                "<li><strong>الإلكتروليتات (Na, K, Cl, CO₂)</strong> — "
                "مراقبة توازن السوائل ووظائف الأعصاب</li>"
                "<li><strong>الكالسيوم</strong> — مهم للعظام والقلب "
                "والأعصاب</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-lipid-panel", level=2,
            heading="لوحة الدهون — الكوليسترول والدهون الثلاثية",
            body_html=(
                "<p>تظل أمراض القلب السبب الرئيسي للوفاة في العالم. تقيس "
                "لوحة الدهون الدهون في دمك التي تؤثر مباشرة على مخاطر "
                "القلب والأوعية الدموية:</p>"
                "<ul>"
                "<li><strong>الكوليسترول الكلي</strong> — المرغوب "
                "&lt; 200 mg/dL</li>"
                "<li><strong>كوليسترول LDL (\"الضار\")</strong> — يتراكم في "
                "الشرايين؛ الأمثل &lt; 100 mg/dL</li>"
                "<li><strong>كوليسترول HDL (\"النافع\")</strong> — يزيل "
                "الكوليسترول من الشرايين؛ الهدف ≥ 60 mg/dL</li>"
                "<li><strong>الدهون الثلاثية</strong> — الطبيعي "
                "&lt; 150 mg/dL</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-thyroid-panel", level=2,
            heading="لوحة الغدة الدرقية — TSH وT3 وT4",
            body_html=(
                "<p>تتحكم الغدة الدرقية في الأيض والطاقة ودرجة حرارة "
                "الجسم. تصيب اضطرابات الغدة الدرقية نحو 12% من "
                "السكان.</p>"
                "<ul>"
                "<li><strong>TSH</strong> — مؤشر الفحص الأولي؛ الطبيعي "
                "0.4–4.0 mIU/L</li>"
                "<li><strong>T4 الحر</strong> — الهرمون الدرقي الرئيسي</li>"
                "<li><strong>T3 الحر</strong> — الهرمون الأكثر نشاطًا</li>"
                "</ul>"
                "<p><strong>قصور الغدة الدرقية</strong> (TSH مرتفع، T4 منخفض) "
                "يسبب الإرهاق وزيادة الوزن وعدم تحمل البرد. "
                "<strong>فرط نشاط الغدة الدرقية</strong> (TSH منخفض، T4 مرتفع) "
                "يسبب فقدان الوزن وتسارع ضربات القلب والقلق.</p>"
            ),
        ),
        Section(
            id="section-diabetes-screening", level=2,
            heading="فحص السكري — HbA1c وغلوكوز الصيام",
            body_html=(
                "<p>أكثر من 10% من البالغين حول العالم مصابون بالسكري:</p>"
                "<ul>"
                "<li><strong>غلوكوز الصيام</strong> — الطبيعي "
                "&lt; 100 mg/dL؛ مقدمات السكري 100–125 mg/dL؛ "
                "السكري ≥ 126 mg/dL</li>"
                "<li><strong>HbA1c</strong> — يعكس متوسط سكر الدم خلال "
                "2-3 أشهر الماضية. الطبيعي &lt; 5.7%؛ مقدمات السكري "
                "5.7–6.4%؛ السكري ≥ 6.5%</li>"
                "</ul>"
                "<p>HbA1c ذو قيمة خاصة لأنه لا يتطلب صيامًا ولا يتأثر "
                "بالتقلبات اليومية.</p>"
            ),
        ),
        Section(
            id="section-vitamins-minerals", level=2,
            heading="فحوصات الفيتامينات والمعادن — D وB12 والحديد والفيريتين",
            body_html=(
                "<p>نقص العناصر الغذائية شائع بشكل مفاجئ:</p>"
                "<ul>"
                "<li><strong>فيتامين D (25-OH)</strong> — ضروري للعظام "
                "والمناعة والمزاج. الأمثل: 30–60 ng/mL.</li>"
                "<li><strong>فيتامين B12</strong> — حيوي لوظائف الأعصاب. "
                "النقص يسبب الإرهاق والوخز ومشاكل الإدراك.</li>"
                "<li><strong>الحديد والفيريتين</strong> — الحديد ضروري "
                "لنقل الأكسجين؛ الفيريتين يعكس مخازن الحديد.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-inflammation-markers", level=2,
            heading="مؤشرات الالتهاب — CRP وESR",
            body_html=(
                "<p>يرتبط الالتهاب المزمن منخفض الدرجة بشكل متزايد "
                "بأمراض القلب والحالات المناعية الذاتية:</p>"
                "<ul>"
                "<li><strong>CRP (البروتين التفاعلي C)</strong> — hs-CRP "
                "&lt; 1 mg/L = خطر قلبي وعائي منخفض؛ 1–3 mg/L = متوسط؛ "
                "&gt; 3 mg/L = مرتفع.</li>"
                "<li><strong>ESR (سرعة ترسب الدم)</strong> — يقيس سرعة "
                "ترسب كريات الدم الحمراء. ارتفاعه يشير إلى التهاب لكنه "
                "غير محدد.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-frequency-norya", level=2,
            heading="عدد مرات الفحص وكيف يساعد NoryaAI",
            body_html=(
                "<p>يعتمد تواتر الفحوصات على العمر وعوامل الخطر والحالات "
                "القائمة:</p>"
                "<ul>"
                "<li><strong>18–30 سنة</strong> — تعداد دم ولوحة أيض "
                "ودهون كل 2–3 سنوات</li>"
                "<li><strong>30–45 سنة</strong> — تعداد دم وCMP ودهون "
                "سنويًا؛ TSH وHbA1c كل 2–3 سنوات</li>"
                "<li><strong>45+ سنة</strong> — لوحة سنوية شاملة تشمل "
                "تعداد الدم وCMP والدهون والغدة الدرقية وHbA1c وفيتامين D "
                "وB12 والفيريتين وCRP</li>"
                "</ul>"
                "<p><strong>NoryaAI</strong> يجعل فهم نتائجك سهلاً. "
                "حمّل تقرير مختبرك — PDF أو صورة — وسيقوم NoryaAI بـ:</p>"
                "<ul>"
                "<li>تحديد كل مؤشر حيوي في تقريرك</li>"
                "<li>مقارنة كل قيمة بنطاقات مرجعية حسب العمر والجنس</li>"
                "<li>تمييز النتائج غير الطبيعية مع شروحات واضحة</li>"
                "<li>إنشاء ملخص صحي منظم وجاهز للطبيب</li>"
                "</ul>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------
def build_annual_tests_article():
    """Build the Annual Blood Tests Pillar Article. Called from blog_i18n.py."""
    from app.blog_i18n import Article

    slugs = {
        "en": "essential-annual-blood-tests",
        "tr": "yillik-kan-tahlili-rehberi",
        "de": "jaehrliche-bluttests-leitfaden",
        "es": "analisis-sangre-anuales",
        "fr": "analyses-sang-annuelles",
        "it": "esami-sangue-annuali",
        "he": "essential-annual-blood-tests",
        "hi": "essential-annual-blood-tests",
        "ar": "essential-annual-blood-tests",
    }

    return Article(
        id="essential-annual-blood-tests",
        published_at=date(2026, 3, 25),
        read_minutes=12,
        cover_image="/static/images/blog/annual-blood-tests-hero.jpg",
        category={
            "en": "Blood Tests",
            "tr": "Kan Testleri",
            "de": "Bluttests",
            "es": "Análisis de Sangre",
            "fr": "Analyses de Sang",
            "it": "Esami del Sangue",
            "he": "בדיקות דם",
            "hi": "रक्त परीक्षण",
            "ar": "فحوصات الدم",
        },
        slugs=slugs,
        titles={
            "en": "Essential Blood Tests Every Adult Should Get Annually",
            "tr": "Her Yetişkinin Yıllık Yaptırması Gereken Temel Kan Tahlilleri",
            "de": "Wichtige Bluttests, die jeder Erwachsene jährlich machen sollte",
            "es": "Análisis de sangre esenciales que todo adulto debería hacerse anualmente",
            "fr": "Les analyses de sang essentielles à faire chaque année",
            "it": "Esami del sangue essenziali da fare ogni anno",
            "he": "בדיקות דם חיוניות שכל מבוגר צריך לעשות מדי שנה",
            "hi": "हर वयस्क को सालाना करवानी चाहिए ये ज़रूरी रक्त जांचें",
            "ar": "فحوصات الدم الأساسية التي يجب على كل بالغ إجراؤها سنويًا",
        },
        subtitles={
            "en": "From CBC to cholesterol, thyroid, and diabetes screening — a complete guide to the blood tests you need and how often to get them.",
            "tr": "CBC'den kolesterole, tiroidten diyabet taramasına — ihtiyacınız olan kan tahlilleri ve ne sıklıkta yaptırmanız gerektiği hakkında eksiksiz rehber.",
            "de": "Vom Blutbild bis Cholesterin, Schilddrüse und Diabetes-Screening — ein vollständiger Leitfaden zu den Bluttests, die Sie brauchen.",
            "es": "Del hemograma al colesterol, tiroides y detección de diabetes — guía completa de los análisis de sangre que necesita.",
            "fr": "De la NFS au cholestérol, en passant par la thyroïde et le dépistage du diabète — guide complet des analyses à faire.",
            "it": "Dall'emocromo al colesterolo, tiroide e screening del diabete — guida completa agli esami del sangue necessari.",
            "he": "מספירת דם ועד כולסטרול, בלוטת תריס וסינון סוכרת — מדריך מלא לבדיקות הדם שאתם צריכים.",
            "hi": "CBC से लेकर कोलेस्ट्रॉल, थायरॉइड और मधुमेह जांच तक — आवश्यक रक्त परीक्षणों की पूरी गाइड।",
            "ar": "من تعداد الدم إلى الكوليسترول والغدة الدرقية وفحص السكري — دليل شامل لفحوصات الدم التي تحتاجها.",
        },
        excerpts={
            "en": "A comprehensive guide to the essential blood tests every adult should get annually — CBC, metabolic panel, lipids, thyroid, diabetes screening, vitamins, and inflammation markers.",
            "tr": "Her yetişkinin yıllık olarak yaptırması gereken temel kan tahlillerine kapsamlı rehber — CBC, metabolik panel, lipitler, tiroid, diyabet taraması, vitaminler ve inflamasyon belirteçleri.",
            "de": "Ein umfassender Leitfaden zu den wichtigsten jährlichen Bluttests — Blutbild, Stoffwechselpanel, Lipide, Schilddrüse, Diabetes-Screening, Vitamine und Entzündungsmarker.",
            "es": "Guía completa de los análisis de sangre anuales esenciales — hemograma, panel metabólico, lípidos, tiroides, detección de diabetes, vitaminas y marcadores de inflamación.",
            "fr": "Guide complet des analyses de sang annuelles essentielles — NFS, bilan métabolique, lipides, thyroïde, dépistage du diabète, vitamines et marqueurs d'inflammation.",
            "it": "Guida completa agli esami del sangue annuali essenziali — emocromo, pannello metabolico, lipidi, tiroide, screening diabete, vitamine e marcatori di infiammazione.",
            "he": "מדריך מקיף לבדיקות הדם השנתיות החיוניות — ספירת דם, פאנל מטבולי, שומנים, תריס, סינון סוכרת, ויטמינים ומדדי דלקת.",
            "hi": "आवश्यक वार्षिक रक्त परीक्षणों की व्यापक मार्गदर्शिका — CBC, मेटाबोलिक पैनल, लिपिड, थायरॉइड, मधुमेह जांच, विटामिन और सूजन मार्कर।",
            "ar": "دليل شامل لفحوصات الدم السنوية الأساسية — تعداد الدم، لوحة الأيض، الدهون، الغدة الدرقية، فحص السكري، الفيتامينات ومؤشرات الالتهاب.",
        },
        seo_titles={
            "en": "Essential Blood Tests Every Adult Should Get Annually — 2026 Guide | NoryaAI",
            "tr": "Yıllık Kan Tahlili Rehberi — Her Yetişkinin Yaptırması Gereken Testler 2026 | NoryaAI",
            "de": "Jährliche Bluttests Leitfaden — Wichtige Tests für Erwachsene 2026 | NoryaAI",
            "es": "Análisis de Sangre Anuales Esenciales — Guía 2026 | NoryaAI",
            "fr": "Analyses de Sang Annuelles Essentielles — Guide 2026 | NoryaAI",
            "it": "Esami del Sangue Annuali Essenziali — Guida 2026 | NoryaAI",
            "he": "בדיקות דם שנתיות חיוניות — מדריך 2026 | NoryaAI",
            "hi": "आवश्यक वार्षिक रक्त जांच — 2026 गाइड | NoryaAI",
            "ar": "فحوصات الدم السنوية الأساسية — دليل 2026 | NoryaAI",
        },
        seo_descriptions={
            "en": "Complete guide to annual blood tests for adults. Learn about CBC, metabolic panel, lipid panel, thyroid, HbA1c, vitamin D, B12, ferritin, CRP, and recommended testing frequency by age.",
            "tr": "Yetişkinler için yıllık kan tahlilleri rehberi. CBC, metabolik panel, lipit paneli, tiroid, HbA1c, D vitamini, B12, ferritin, CRP ve yaşa göre önerilen test sıklığı hakkında bilgi edinin.",
            "de": "Vollständiger Leitfaden zu jährlichen Bluttests für Erwachsene. Erfahren Sie mehr über Blutbild, Stoffwechselpanel, Lipidpanel, Schilddrüse, HbA1c, Vitamin D, B12, Ferritin und CRP.",
            "es": "Guía completa de análisis de sangre anuales. Conozca el hemograma, panel metabólico, lípidos, tiroides, HbA1c, vitamina D, B12, ferritina y frecuencia recomendada por edad.",
            "fr": "Guide complet des analyses de sang annuelles. NFS, bilan métabolique, lipides, thyroïde, HbA1c, vitamine D, B12, ferritine, CRP et fréquence recommandée selon l'âge.",
            "it": "Guida completa agli esami del sangue annuali. Emocromo, pannello metabolico, lipidi, tiroide, HbA1c, vitamina D, B12, ferritina, PCR e frequenza raccomandata per età.",
            "he": "מדריך מלא לבדיקות דם שנתיות למבוגרים. ספירת דם, פאנל מטבולי, שומנים, תריס, HbA1c, ויטמין D, B12, פריטין, CRP ותדירות מומלצת לפי גיל.",
            "hi": "वयस्कों के लिए वार्षिक रक्त परीक्षण गाइड। CBC, मेटाबोलिक पैनल, लिपिड पैनल, थायरॉइड, HbA1c, विटामिन D, B12, फेरिटिन, CRP और उम्र के अनुसार अनुशंसित जांच आवृत्ति।",
            "ar": "دليل شامل لفحوصات الدم السنوية للبالغين. تعرف على تعداد الدم، لوحة الأيض، الدهون، الغدة الدرقية، HbA1c، فيتامين D، B12، الفيريتين، CRP وتواتر الفحص الموصى به حسب العمر.",
        },
        sections_by_lang={
            "en": _sections_en(),
            "tr": _sections_tr(),
            "de": _sections_de(),
            "es": _sections_es(),
            "fr": _sections_fr(),
            "it": _sections_it(),
            "he": _sections_he(),
            "hi": _sections_hi(),
            "ar": _sections_ar(),
        },
        last_updated=date(2026, 3, 25),
        faq_schema_qa={
            "en": [
                {"question": "What blood tests should I get every year?", "answer": "At minimum, adults should get a Complete Blood Count (CBC), Comprehensive Metabolic Panel (CMP), and Lipid Panel annually. Depending on age and risk factors, add thyroid (TSH), HbA1c, vitamin D, B12, ferritin, and CRP."},
                {"question": "How much do annual blood tests cost?", "answer": "Basic annual panels (CBC, CMP, lipid panel) typically cost $100–$300 without insurance. Many insurance plans cover routine blood work fully as part of preventive care."},
                {"question": "Do I need to fast before blood tests?", "answer": "Yes, for accurate lipid panel and fasting glucose results, an 8–12 hour fast is recommended. HbA1c, CBC, thyroid, and vitamin tests do not require fasting."},
                {"question": "At what age should I start getting regular blood tests?", "answer": "Adults should start baseline blood work by age 18–20. From age 30+, annual panels become more important. After 45, comprehensive annual testing is strongly recommended."},
            ],
            "tr": [
                {"question": "Her yıl hangi kan tahlillerini yaptırmalıyım?", "answer": "En azından yetişkinler yıllık olarak Tam Kan Sayımı (CBC), Kapsamlı Metabolik Panel (CMP) ve Lipit Paneli yaptırmalıdır. Yaş ve risk faktörlerine bağlı olarak tiroid (TSH), HbA1c, D vitamini, B12, ferritin ve CRP eklenmelidir."},
                {"question": "Yıllık kan tahlillerinin maliyeti ne kadardır?", "answer": "Temel yıllık paneller (CBC, CMP, lipit paneli) sigortasız genellikle 100–300 dolar arasındadır. Birçok sigorta planı koruyucu bakım kapsamında rutin kan tahlillerini tam olarak karşılar."},
                {"question": "Kan tahlili öncesi aç kalmam gerekiyor mu?", "answer": "Evet, doğru lipit paneli ve açlık glukozu sonuçları için 8–12 saatlik açlık önerilir. HbA1c, CBC, tiroid ve vitamin testleri açlık gerektirmez."},
                {"question": "Düzenli kan tahlillerine kaç yaşında başlamalıyım?", "answer": "Yetişkinler 18-20 yaşında temel kan tahlillerine başlamalıdır. 30 yaşından itibaren yıllık paneller daha önemli hale gelir. 45 yaşından sonra kapsamlı yıllık test şiddetle tavsiye edilir."},
            ],
            "de": [
                {"question": "Welche Bluttests sollte ich jedes Jahr machen lassen?", "answer": "Mindestens sollten Erwachsene jährlich ein großes Blutbild (CBC), ein umfassendes Stoffwechselpanel (CMP) und ein Lipidpanel durchführen lassen. Je nach Alter und Risikofaktoren kommen Schilddrüse (TSH), HbA1c, Vitamin D, B12, Ferritin und CRP hinzu."},
                {"question": "Muss ich vor Bluttests nüchtern sein?", "answer": "Ja, für genaue Lipidpanel- und Nüchternglukose-Ergebnisse wird ein 8–12-stündiges Fasten empfohlen. HbA1c, Blutbild, Schilddrüse und Vitamintests erfordern kein Fasten."},
                {"question": "Ab welchem Alter sollte ich regelmäßige Bluttests machen?", "answer": "Erwachsene sollten mit 18–20 Jahren mit Basis-Blutuntersuchungen beginnen. Ab 30 werden jährliche Panels wichtiger. Nach 45 wird eine umfassende jährliche Untersuchung dringend empfohlen."},
            ],
            "es": [
                {"question": "¿Qué análisis de sangre debo hacerme cada año?", "answer": "Como mínimo, los adultos deben hacerse anualmente un hemograma completo (CBC), un panel metabólico completo (CMP) y un panel lipídico. Según la edad y factores de riesgo, añada tiroides (TSH), HbA1c, vitamina D, B12, ferritina y PCR."},
                {"question": "¿Necesito ayunar antes de los análisis de sangre?", "answer": "Sí, para resultados precisos del panel lipídico y la glucosa en ayunas, se recomienda un ayuno de 8–12 horas. HbA1c, hemograma, tiroides y vitaminas no requieren ayuno."},
                {"question": "¿A qué edad debo empezar con análisis regulares?", "answer": "Los adultos deben comenzar con análisis básicos a los 18–20 años. A partir de los 30, los paneles anuales son más importantes. Después de los 45, se recomienda encarecidamente una evaluación anual completa."},
            ],
            "fr": [
                {"question": "Quelles analyses de sang dois-je faire chaque année ?", "answer": "Au minimum, les adultes devraient faire annuellement une NFS, un bilan métabolique complet (CMP) et un bilan lipidique. Selon l'âge et les facteurs de risque, ajoutez thyroïde (TSH), HbA1c, vitamine D, B12, ferritine et CRP."},
                {"question": "Dois-je être à jeun avant les analyses de sang ?", "answer": "Oui, pour des résultats précis du bilan lipidique et de la glycémie à jeun, un jeûne de 8–12 heures est recommandé. L'HbA1c, la NFS, la thyroïde et les vitamines ne nécessitent pas de jeûne."},
                {"question": "À quel âge commencer les bilans sanguins réguliers ?", "answer": "Les adultes devraient commencer un bilan de base vers 18–20 ans. À partir de 30 ans, les bilans annuels deviennent plus importants. Après 45 ans, un bilan annuel complet est fortement recommandé."},
            ],
            "it": [
                {"question": "Quali esami del sangue devo fare ogni anno?", "answer": "Come minimo, gli adulti dovrebbero fare annualmente un emocromo completo (CBC), un pannello metabolico completo (CMP) e un profilo lipidico. In base all'età e ai fattori di rischio, aggiungere tiroide (TSH), HbA1c, vitamina D, B12, ferritina e PCR."},
                {"question": "Devo essere a digiuno prima degli esami del sangue?", "answer": "Sì, per risultati accurati del profilo lipidico e della glicemia a digiuno, si raccomanda un digiuno di 8–12 ore. HbA1c, emocromo, tiroide e vitamine non richiedono il digiuno."},
                {"question": "A che età dovrei iniziare con gli esami regolari?", "answer": "Gli adulti dovrebbero iniziare con gli esami di base a 18–20 anni. Dai 30 anni, i controlli annuali diventano più importanti. Dopo i 45, un check-up annuale completo è fortemente raccomandato."},
            ],
            "he": [
                {"question": "אילו בדיקות דם עלי לבצע מדי שנה?", "answer": "לכל הפחות, מבוגרים צריכים לבצע מדי שנה ספירת דם מלאה (CBC), פאנל מטבולי מקיף (CMP) ופרופיל שומנים. בהתאם לגיל ולגורמי סיכון, יש להוסיף בלוטת תריס (TSH), HbA1c, ויטמין D, B12, פריטין ו-CRP."},
                {"question": "האם צריך לצום לפני בדיקות דם?", "answer": "כן, לתוצאות מדויקות של פרופיל שומנים וגלוקוז בצום מומלץ צום של 8–12 שעות. HbA1c, ספירת דם, תריס ובדיקות ויטמינים אינן דורשות צום."},
                {"question": "באיזה גיל כדאי להתחיל בדיקות דם סדירות?", "answer": "מבוגרים צריכים להתחיל בדיקות דם בסיסיות בגיל 18–20. מגיל 30 ומעלה בדיקות שנתיות הופכות חשובות יותר. אחרי גיל 45 מומלצת בדיקה שנתית מקיפה."},
            ],
            "hi": [
                {"question": "मुझे हर साल कौन से रक्त परीक्षण करवाने चाहिए?", "answer": "न्यूनतम रूप से, वयस्कों को सालाना पूर्ण रक्त गणना (CBC), व्यापक मेटाबोलिक पैनल (CMP) और लिपिड पैनल करवाना चाहिए। उम्र और जोखिम कारकों के आधार पर थायरॉइड (TSH), HbA1c, विटामिन D, B12, फेरिटिन और CRP जोड़ें।"},
                {"question": "क्या रक्त परीक्षण से पहले उपवास करना ज़रूरी है?", "answer": "हाँ, सटीक लिपिड पैनल और उपवास ग्लूकोज परिणामों के लिए 8–12 घंटे का उपवास अनुशंसित है। HbA1c, CBC, थायरॉइड और विटामिन परीक्षणों के लिए उपवास की आवश्यकता नहीं है।"},
                {"question": "नियमित रक्त परीक्षण किस उम्र में शुरू करने चाहिए?", "answer": "वयस्कों को 18–20 वर्ष की आयु में बुनियादी रक्त परीक्षण शुरू करने चाहिए। 30 वर्ष से अधिक आयु में वार्षिक पैनल अधिक महत्वपूर्ण हो जाते हैं। 45 के बाद व्यापक वार्षिक जांच की दृढ़ता से सिफारिश की जाती है।"},
            ],
            "ar": [
                {"question": "ما فحوصات الدم التي يجب إجراؤها كل عام؟", "answer": "كحد أدنى، يجب على البالغين إجراء تعداد دم كامل (CBC) ولوحة أيض شاملة (CMP) ولوحة دهون سنويًا. حسب العمر وعوامل الخطر، أضف الغدة الدرقية (TSH) وHbA1c وفيتامين D وB12 والفيريتين وCRP."},
                {"question": "هل يجب الصيام قبل فحوصات الدم؟", "answer": "نعم، للحصول على نتائج دقيقة للوحة الدهون وغلوكوز الصيام، يُوصى بصيام 8–12 ساعة. لا تتطلب فحوصات HbA1c وتعداد الدم والغدة الدرقية والفيتامينات صيامًا."},
                {"question": "في أي عمر يجب البدء بفحوصات الدم المنتظمة؟", "answer": "يجب أن يبدأ البالغون بفحوصات الدم الأساسية في سن 18–20. من سن 30 فصاعدًا تصبح اللوحات السنوية أكثر أهمية. بعد 45 يُوصى بشدة بفحص سنوي شامل."},
            ],
        },
    )
