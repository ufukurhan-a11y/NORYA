"""Pillar blog article: Understanding Blood Sugar — comprehensive guide.

Registered in blog_i18n.py as a pillar content piece for SEO.
"""
from __future__ import annotations

from datetime import date
from typing import Dict, List, Optional

from app.blog_i18n import Article, Section

LANGS = ("tr", "en", "de", "es", "fr", "it", "he", "hi", "ar")

slugs = {
    "en": "blood-sugar-levels-guide",
    "tr": "kan-sekeri-rehberi",
    "de": "blutzuckerwerte-leitfaden",
    "es": "guia-niveles-azucar",
    "fr": "guide-glycemie",
    "it": "guida-glicemia",
    "he": "blood-sugar-levels-guide",
    "hi": "blood-sugar-levels-guide",
    "ar": "blood-sugar-levels-guide",
}

# ---------------------------------------------------------------------------
# English
# ---------------------------------------------------------------------------

def _bs_sections_en() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="What Do Blood Sugar Tests Measure?",
            body_html=(
                "<p>Blood sugar (blood glucose) tests measure the amount of <strong>glucose</strong> — your body's primary energy source — circulating in your bloodstream. "
                "Glucose comes from the foods you eat and is regulated by the hormone <strong>insulin</strong>, produced by the pancreas.</p>"
                "<p>Several types of blood sugar tests exist, each serving a different clinical purpose:</p>"
                "<ul>"
                "<li><strong>Fasting Blood Glucose (FBG)</strong> — measured after 8-12 hours of fasting; the standard screening test.</li>"
                "<li><strong>Random (non-fasting) Glucose</strong> — taken at any time; useful in emergency settings.</li>"
                "<li><strong>Oral Glucose Tolerance Test (OGTT)</strong> — measures glucose before and 2 hours after drinking a 75 g glucose solution.</li>"
                "<li><strong>HbA1c (Glycated Hemoglobin)</strong> — reflects average blood sugar over the past 2-3 months.</li>"
                "<li><strong>Fasting Insulin &amp; HOMA-IR</strong> — assess insulin resistance even before glucose rises.</li>"
                "</ul>"
                "<p>Understanding these tests is vital: the World Health Organization estimates that over <strong>422 million people</strong> worldwide live with diabetes, "
                "and many more have undiagnosed prediabetes.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="Fasting Blood Glucose: Normal, Prediabetes & Diabetes Ranges",
            body_html=(
                "<p>Fasting blood glucose (FBG) is measured after an overnight fast of at least 8 hours. It is the most widely used screening test for diabetes and prediabetes.</p>"
                "<div class='blog-definition'><strong>Reference ranges (venous plasma):</strong><br>"
                "Normal: 70–99 mg/dL (3.9–5.5 mmol/L)<br>"
                "Prediabetes (Impaired Fasting Glucose): 100–125 mg/dL (5.6–6.9 mmol/L)<br>"
                "Diabetes: ≥ 126 mg/dL (≥ 7.0 mmol/L) on two separate occasions</div>"
                "<p><strong>Low blood sugar (hypoglycemia)</strong> — below 70 mg/dL — can cause shakiness, sweating, confusion, and in severe cases, loss of consciousness. "
                "It is most common in people taking insulin or sulfonylureas.</p>"
                "<p><strong>High fasting glucose</strong> indicates your body is not producing enough insulin or your cells are not responding to it properly (insulin resistance). "
                "Even values in the upper-normal range (90-99 mg/dL) may warrant monitoring over time.</p>"
                "<div class='blog-example'><strong>Important:</strong> A single elevated reading does not diagnose diabetes. "
                "Your doctor will typically repeat the test or order an HbA1c to confirm.</div>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c (Glycated Hemoglobin): Your 3-Month Blood Sugar Average",
            body_html=(
                "<p>HbA1c measures the percentage of hemoglobin in your red blood cells that has glucose attached to it. "
                "Because red blood cells live roughly 120 days, HbA1c reflects your <strong>average blood sugar over the past 2-3 months</strong> — "
                "making it far more informative than a single fasting glucose reading.</p>"
                "<div class='blog-definition'><strong>Reference ranges:</strong><br>"
                "Normal: &lt; 5.7% (&lt; 39 mmol/mol)<br>"
                "Prediabetes: 5.7–6.4% (39–47 mmol/mol)<br>"
                "Diabetes: ≥ 6.5% (≥ 48 mmol/mol)</div>"
                "<p><strong>For people already diagnosed with diabetes:</strong></p>"
                "<ul>"
                "<li>General target: &lt; 7.0% (ADA recommendation)</li>"
                "<li>Stricter target: &lt; 6.5% for younger patients without complications</li>"
                "<li>Relaxed target: &lt; 8.0% for elderly patients or those with hypoglycemia risk</li>"
                "</ul>"
                "<p>Each 1% reduction in HbA1c lowers the risk of microvascular complications (eye, kidney, nerve damage) by approximately <strong>35-40%</strong>.</p>"
                "<div class='blog-example'><strong>Limitations:</strong> HbA1c can be inaccurate in conditions that affect red blood cell lifespan — "
                "iron deficiency anemia, hemoglobin variants (sickle cell trait), chronic kidney disease, or recent blood transfusion.</div>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="Fasting Insulin & HOMA-IR: Detecting Insulin Resistance Early",
            body_html=(
                "<p><strong>Insulin</strong> is the hormone that allows glucose to enter your cells. When cells become resistant to insulin, "
                "the pancreas compensates by producing more — leading to <strong>hyperinsulinemia</strong>. "
                "Blood glucose may remain normal for years while insulin levels climb silently.</p>"
                "<div class='blog-definition'><strong>Fasting insulin:</strong> Optimal: 2–6 µIU/mL · Normal: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (Fasting Insulin × Fasting Glucose) / 405<br>"
                "Normal: &lt; 1.0 · Borderline: 1.0–2.0 · Insulin resistant: &gt; 2.0 · Significant resistance: &gt; 3.0</div>"
                "<p>HOMA-IR is one of the most useful early markers because it can detect metabolic dysfunction <strong>years before</strong> "
                "fasting glucose or HbA1c become abnormal. It is especially valuable in:</p>"
                "<ul>"
                "<li>Polycystic Ovary Syndrome (PCOS) — insulin resistance drives many PCOS symptoms</li>"
                "<li>Metabolic syndrome screening</li>"
                "<li>Non-alcoholic fatty liver disease (NAFLD)</li>"
                "<li>Family history of type 2 diabetes</li>"
                "</ul>"
                "<div class='blog-example'><strong>Tip:</strong> If your fasting glucose is normal but you have central obesity, "
                "fatigue after meals, or skin tags / acanthosis nigricans, ask your doctor about fasting insulin and HOMA-IR.</div>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="Oral Glucose Tolerance Test (OGTT)",
            body_html=(
                "<p>The OGTT is the gold standard for diagnosing <strong>gestational diabetes</strong> and is also used when fasting glucose or HbA1c results are borderline.</p>"
                "<p><strong>How it works:</strong> After an overnight fast, a baseline blood sample is drawn. You then drink a solution containing 75 g of glucose, "
                "and blood is drawn again at the 1-hour and 2-hour marks.</p>"
                "<div class='blog-definition'><strong>2-hour OGTT values (75 g glucose):</strong><br>"
                "Normal: &lt; 140 mg/dL (7.8 mmol/L)<br>"
                "Impaired Glucose Tolerance (prediabetes): 140–199 mg/dL (7.8–11.0 mmol/L)<br>"
                "Diabetes: ≥ 200 mg/dL (≥ 11.1 mmol/L)</div>"
                "<p>The OGTT is more sensitive than fasting glucose alone — it can detect <strong>impaired glucose tolerance</strong> (IGT) "
                "even when fasting values are completely normal. This is especially important because many people with IGT progress to type 2 diabetes within 5-10 years.</p>"
                "<p><strong>For gestational diabetes</strong> (pregnancy), different thresholds apply and screening is typically done between weeks 24-28.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="Risk Factors & Symptoms of High Blood Sugar",
            body_html=(
                "<p><strong>Risk factors for elevated blood sugar / type 2 diabetes:</strong></p>"
                "<ul>"
                "<li>Overweight or obesity (especially visceral / abdominal fat)</li>"
                "<li>Sedentary lifestyle</li>"
                "<li>Family history of diabetes (first-degree relative)</li>"
                "<li>Age ≥ 45 years</li>"
                "<li>History of gestational diabetes or delivering a baby &gt; 4 kg</li>"
                "<li>Polycystic Ovary Syndrome (PCOS)</li>"
                "<li>Ethnicity (higher risk in South Asian, African, Hispanic, Middle Eastern populations)</li>"
                "<li>High blood pressure (≥ 140/90 mmHg)</li>"
                "<li>Abnormal lipid profile (high triglycerides, low HDL)</li>"
                "</ul>"
                "<p><strong>Symptoms of hyperglycemia to watch for:</strong></p>"
                "<ul>"
                "<li>Excessive thirst (polydipsia) and frequent urination (polyuria)</li>"
                "<li>Unexplained weight loss</li>"
                "<li>Fatigue and weakness</li>"
                "<li>Blurred vision</li>"
                "<li>Slow-healing wounds and frequent infections</li>"
                "<li>Tingling or numbness in hands and feet</li>"
                "<li>Dark, velvety skin patches (acanthosis nigricans)</li>"
                "</ul>"
                "<div class='blog-example'><strong>Warning:</strong> Type 2 diabetes can be <em>asymptomatic</em> for years. "
                "Many people are diagnosed only after complications arise. Regular screening is essential if you have risk factors.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="Diet & Lifestyle Tips for Healthy Blood Sugar",
            body_html=(
                "<p>Whether you have prediabetes, diabetes, or simply want to optimize metabolic health, these evidence-based strategies can help:</p>"
                "<ul>"
                "<li><strong>Choose low-glycemic foods:</strong> Whole grains, legumes, non-starchy vegetables, and most fruits have a gentler impact on blood sugar than refined carbohydrates.</li>"
                "<li><strong>Prioritize fiber:</strong> Aim for 25-30 g/day. Fiber slows glucose absorption. Excellent sources: oats, lentils, chia seeds, vegetables.</li>"
                "<li><strong>Pair carbs with protein or healthy fat:</strong> Eating an apple with almond butter, for example, reduces the glycemic spike compared to the apple alone.</li>"
                "<li><strong>Move regularly:</strong> 150 minutes of moderate exercise per week (brisk walking, cycling, swimming) improves insulin sensitivity for up to 48 hours after each session.</li>"
                "<li><strong>Maintain a healthy weight:</strong> Losing just 5-7% of body weight can reduce diabetes risk by up to 58% in people with prediabetes (DPP study).</li>"
                "<li><strong>Manage stress:</strong> Cortisol raises blood sugar. Mindfulness, deep breathing, and adequate sleep (7-9 hours) help regulate it.</li>"
                "<li><strong>Limit added sugars and sugary drinks:</strong> One sugary drink per day increases type 2 diabetes risk by approximately 26%.</li>"
                "<li><strong>Consider the Mediterranean diet:</strong> Rich in olive oil, vegetables, fish, and whole grains — consistently shown to lower HbA1c and cardiovascular risk.</li>"
                "</ul>"
                "<div class='blog-example'><strong>Quick win:</strong> A 15-minute walk after meals can reduce post-meal glucose spikes by 20-30%.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="How NoryaAI Analyzes Your Blood Sugar Results",
            body_html=(
                "<p>NoryaAI reads your complete blood work — whether it's a lab PDF or a photo — and automatically:</p>"
                "<ul>"
                "<li>Identifies fasting glucose, HbA1c, fasting insulin, HOMA-IR, and OGTT values</li>"
                "<li>Classifies results into normal, prediabetes, or diabetes ranges</li>"
                "<li>Flags insulin resistance even when glucose is still in the normal range</li>"
                "<li>Provides clear, plain-language explanations for each marker</li>"
                "<li>Generates a doctor-ready summary with trend tracking over time</li>"
                "</ul>"
                "<p>Upload your lab report and get your blood sugar analysis in minutes — no manual data entry, no medical jargon.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Turkish
# ---------------------------------------------------------------------------

def _bs_sections_tr() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="Kan Şekeri Testleri Neyi Ölçer?",
            body_html=(
                "<p>Kan şekeri (kan glukozu) testleri, vücudunuzun ana enerji kaynağı olan <strong>glukozun</strong> kan dolaşımınızdaki miktarını ölçer. "
                "Glukoz yediğiniz gıdalardan gelir ve pankreas tarafından üretilen <strong>insülin</strong> hormonu ile düzenlenir.</p>"
                "<p>Farklı klinik amaçlara hizmet eden birkaç kan şekeri testi bulunur:</p>"
                "<ul>"
                "<li><strong>Açlık Kan Şekeri (AKŞ)</strong> — 8-12 saatlik açlık sonrası ölçülür; standart tarama testidir.</li>"
                "<li><strong>Rastgele (tokluk) Glukoz</strong> — herhangi bir zamanda alınır; acil durumlarda kullanılır.</li>"
                "<li><strong>Oral Glukoz Tolerans Testi (OGTT)</strong> — 75 g glukoz solüsyonu içilmeden önce ve 2 saat sonra ölçülür.</li>"
                "<li><strong>HbA1c (Glikozile Hemoglobin)</strong> — son 2-3 aylık ortalama kan şekerini yansıtır.</li>"
                "<li><strong>Açlık İnsülini ve HOMA-IR</strong> — glukoz yükselmeden önce bile insülin direncini değerlendirir.</li>"
                "</ul>"
                "<p>Bu testleri anlamak hayati öneme sahiptir: Dünya Sağlık Örgütü, dünya genelinde <strong>422 milyondan fazla</strong> insanın diyabetle yaşadığını tahmin etmektedir.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="Açlık Kan Şekeri: Normal, Prediyabet ve Diyabet Aralıkları",
            body_html=(
                "<p>Açlık kan şekeri (AKŞ), en az 8 saatlik gece açlığı sonrası ölçülür. Diyabet ve prediyabet taraması için en yaygın kullanılan testtir.</p>"
                "<div class='blog-definition'><strong>Referans aralıkları (venöz plazma):</strong><br>"
                "Normal: 70–99 mg/dL (3,9–5,5 mmol/L)<br>"
                "Prediyabet (Bozulmuş Açlık Glukozu): 100–125 mg/dL (5,6–6,9 mmol/L)<br>"
                "Diyabet: ≥ 126 mg/dL (≥ 7,0 mmol/L) — iki ayrı ölçümde</div>"
                "<p><strong>Düşük kan şekeri (hipoglisemi)</strong> — 70 mg/dL altı — titreme, terleme, konfüzyon ve ciddi vakalarda bilinç kaybına neden olabilir.</p>"
                "<p><strong>Yüksek açlık glukozu</strong>, vücudunuzun yeterli insülin üretmediğini veya hücrelerinizin insüline düzgün yanıt vermediğini (insülin direnci) gösterir.</p>"
                "<div class='blog-example'><strong>Önemli:</strong> Tek bir yüksek ölçüm diyabet tanısı koymaz. "
                "Doktorunuz genellikle testi tekrarlar veya doğrulamak için HbA1c ister.</div>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c (Glikozile Hemoglobin): 3 Aylık Kan Şekeri Ortalamanız",
            body_html=(
                "<p>HbA1c, kırmızı kan hücrelerinizdeki hemoglobinin glukoz bağlanmış yüzdesini ölçer. "
                "Kırmızı kan hücreleri yaklaşık 120 gün yaşadığından, HbA1c son <strong>2-3 aylık ortalama kan şekerinizi</strong> yansıtır.</p>"
                "<div class='blog-definition'><strong>Referans aralıkları:</strong><br>"
                "Normal: &lt; %5,7 (&lt; 39 mmol/mol)<br>"
                "Prediyabet: %5,7–6,4 (39–47 mmol/mol)<br>"
                "Diyabet: ≥ %6,5 (≥ 48 mmol/mol)</div>"
                "<p><strong>Diyabet tanısı almış kişiler için hedefler:</strong></p>"
                "<ul>"
                "<li>Genel hedef: &lt; %7,0 (ADA önerisi)</li>"
                "<li>Sıkı hedef: &lt; %6,5 — komplikasyonsuz genç hastalar için</li>"
                "<li>Esnek hedef: &lt; %8,0 — yaşlı hastalar veya hipoglisemi riski olanlar için</li>"
                "</ul>"
                "<p>HbA1c'de her %1'lik düşüş, mikrovasküler komplikasyon riskini yaklaşık <strong>%35-40</strong> azaltır.</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="Açlık İnsülini ve HOMA-IR: İnsülin Direncinin Erken Tespiti",
            body_html=(
                "<p><strong>İnsülin</strong>, glukozun hücrelerinize girmesini sağlayan hormondur. Hücreler insüline direnç geliştirdiğinde, "
                "pankreas telafi etmek için daha fazla insülin üretir — bu da <strong>hiperinsülinemi</strong>ye yol açar.</p>"
                "<div class='blog-definition'><strong>Açlık insülini:</strong> Optimal: 2–6 µIU/mL · Normal: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (Açlık İnsülini × Açlık Glukozu) / 405<br>"
                "Normal: &lt; 1,0 · Sınırda: 1,0–2,0 · İnsülin direnci: &gt; 2,0 · Belirgin direnç: &gt; 3,0</div>"
                "<p>HOMA-IR, metabolik bozukluğu açlık glukozu veya HbA1c anormalleşmeden <strong>yıllar önce</strong> tespit edebildiğinden en değerli erken belirteçlerden biridir. Özellikle şu durumlarda önemlidir:</p>"
                "<ul>"
                "<li>Polikistik Over Sendromu (PCOS)</li>"
                "<li>Metabolik sendrom taraması</li>"
                "<li>Non-alkolik yağlı karaciğer hastalığı (NAFLD)</li>"
                "<li>Tip 2 diyabet aile öyküsü</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="Oral Glukoz Tolerans Testi (OGTT)",
            body_html=(
                "<p>OGTT, <strong>gestasyonel diyabet</strong> tanısında altın standart olup, açlık glukozu veya HbA1c sınırda olduğunda da kullanılır.</p>"
                "<p><strong>Nasıl yapılır:</strong> Gece açlığı sonrası bazal kan örneği alınır. Ardından 75 g glukoz içeren solüsyon içilir "
                "ve 1. ve 2. saatlerde kan tekrar alınır.</p>"
                "<div class='blog-definition'><strong>2 saatlik OGTT değerleri (75 g glukoz):</strong><br>"
                "Normal: &lt; 140 mg/dL (7,8 mmol/L)<br>"
                "Bozulmuş Glukoz Toleransı (prediyabet): 140–199 mg/dL (7,8–11,0 mmol/L)<br>"
                "Diyabet: ≥ 200 mg/dL (≥ 11,1 mmol/L)</div>"
                "<p>OGTT, tek başına açlık glukozundan daha hassastır — açlık değerleri tamamen normal olsa bile bozulmuş glukoz toleransını tespit edebilir.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="Risk Faktörleri ve Yüksek Kan Şekeri Belirtileri",
            body_html=(
                "<p><strong>Yüksek kan şekeri / tip 2 diyabet risk faktörleri:</strong></p>"
                "<ul>"
                "<li>Fazla kilo veya obezite (özellikle karın bölgesi yağlanması)</li>"
                "<li>Hareketsiz yaşam tarzı</li>"
                "<li>Diyabet aile öyküsü (birinci derece akraba)</li>"
                "<li>45 yaş üzeri</li>"
                "<li>Gestasyonel diyabet öyküsü veya 4 kg üzerinde bebek doğurma</li>"
                "<li>Polikistik Over Sendromu (PCOS)</li>"
                "<li>Yüksek tansiyon (≥ 140/90 mmHg)</li>"
                "<li>Anormal lipid profili (yüksek trigliserit, düşük HDL)</li>"
                "</ul>"
                "<p><strong>Hiperglisemi belirtileri:</strong></p>"
                "<ul>"
                "<li>Aşırı susama (polidipsi) ve sık idrara çıkma (poliüri)</li>"
                "<li>Açıklanamayan kilo kaybı</li>"
                "<li>Yorgunluk ve halsizlik</li>"
                "<li>Bulanık görme</li>"
                "<li>Yavaş iyileşen yaralar ve sık enfeksiyonlar</li>"
                "<li>El ve ayaklarda karıncalanma veya uyuşma</li>"
                "</ul>"
                "<div class='blog-example'><strong>Uyarı:</strong> Tip 2 diyabet yıllarca <em>belirtisiz</em> seyredebilir. "
                "Risk faktörleriniz varsa düzenli tarama şarttır.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="Sağlıklı Kan Şekeri İçin Beslenme ve Yaşam Tarzı Önerileri",
            body_html=(
                "<p>Prediyabet, diyabet veya genel metabolik sağlığınızı optimize etmek istiyorsanız, kanıta dayalı şu stratejiler yardımcı olabilir:</p>"
                "<ul>"
                "<li><strong>Düşük glisemik indeksli gıdalar tercih edin:</strong> Tam tahıllar, baklagiller, nişastasız sebzeler ve meyvelerin çoğu, rafine karbonhidratlara göre kan şekerini daha yavaş yükseltir.</li>"
                "<li><strong>Lif alımına öncelik verin:</strong> Günde 25-30 g hedefleyin. Lif, glukoz emilimini yavaşlatır. İyi kaynaklar: yulaf, mercimek, chia tohumu, sebzeler.</li>"
                "<li><strong>Karbonhidratları protein veya sağlıklı yağ ile birleştirin:</strong> Bu, glisemik yükselmeyi azaltır.</li>"
                "<li><strong>Düzenli hareket edin:</strong> Haftada 150 dakika orta yoğunlukta egzersiz (tempolu yürüyüş, bisiklet, yüzme) insülin duyarlılığını artırır.</li>"
                "<li><strong>Sağlıklı kilonuzu koruyun:</strong> Vücut ağırlığının sadece %5-7'sini kaybetmek, prediyabetli kişilerde diyabet riskini %58'e kadar azaltabilir.</li>"
                "<li><strong>Stresi yönetin:</strong> Kortizol kan şekerini yükseltir. Farkındalık, derin nefes ve yeterli uyku (7-9 saat) yardımcı olur.</li>"
                "<li><strong>Akdeniz diyetini düşünün:</strong> Zeytinyağı, sebze, balık ve tam tahıllardan zengin — HbA1c ve kardiyovasküler riski düşürdüğü kanıtlanmıştır.</li>"
                "</ul>"
                "<div class='blog-example'><strong>Hızlı ipucu:</strong> Yemeklerden sonra 15 dakikalık yürüyüş, yemek sonrası glukoz yükselmelerini %20-30 azaltabilir.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="NoryaAI Kan Şekeri Sonuçlarınızı Nasıl Analiz Eder?",
            body_html=(
                "<p>NoryaAI, tam kan tahlili raporunuzu — ister laboratuvar PDF'i ister fotoğraf olsun — okur ve otomatik olarak:</p>"
                "<ul>"
                "<li>Açlık glukozu, HbA1c, açlık insülini, HOMA-IR ve OGTT değerlerini tanımlar</li>"
                "<li>Sonuçları normal, prediyabet veya diyabet aralıklarına sınıflandırır</li>"
                "<li>Glukoz hâlâ normal aralıktayken bile insülin direncini işaretler</li>"
                "<li>Her belirteç için anlaşılır açıklamalar sunar</li>"
                "<li>Zaman içindeki değişimleri takip eden doktora hazır bir özet oluşturur</li>"
                "</ul>"
                "<p>Lab raporunuzu yükleyin ve kan şekeri analizinizi dakikalar içinde alın.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------

def _bs_sections_de() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="Was messen Blutzuckertests?",
            body_html=(
                "<p>Blutzuckertests messen die Menge an <strong>Glukose</strong> — der wichtigsten Energiequelle Ihres Körpers — in Ihrem Blutkreislauf. "
                "Glukose stammt aus der Nahrung und wird durch das Hormon <strong>Insulin</strong> reguliert, das von der Bauchspeicheldrüse produziert wird.</p>"
                "<p>Es gibt verschiedene Blutzuckertests:</p>"
                "<ul>"
                "<li><strong>Nüchternblutzucker (NBZ)</strong> — nach 8-12 Stunden Fasten gemessen; der Standard-Screening-Test.</li>"
                "<li><strong>Gelegenheits-Glukose</strong> — jederzeit abgenommen; nützlich in Notfallsituationen.</li>"
                "<li><strong>Oraler Glukosetoleranztest (oGTT)</strong> — Glukose wird vor und 2 Stunden nach Trinken einer 75-g-Glukoselösung gemessen.</li>"
                "<li><strong>HbA1c (Glykiertes Hämoglobin)</strong> — spiegelt den durchschnittlichen Blutzucker der letzten 2-3 Monate wider.</li>"
                "<li><strong>Nüchterninsulin &amp; HOMA-IR</strong> — bewerten die Insulinresistenz, noch bevor der Blutzucker ansteigt.</li>"
                "</ul>"
                "<p>Weltweit leben über <strong>422 Millionen Menschen</strong> mit Diabetes, und viele weitere haben einen unerkannten Prädiabetes.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="Nüchternblutzucker: Normal-, Prädiabetes- & Diabetes-Bereiche",
            body_html=(
                "<p>Der Nüchternblutzucker wird nach mindestens 8 Stunden Fasten über Nacht gemessen.</p>"
                "<div class='blog-definition'><strong>Referenzbereiche (venöses Plasma):</strong><br>"
                "Normal: 70–99 mg/dL (3,9–5,5 mmol/L)<br>"
                "Prädiabetes: 100–125 mg/dL (5,6–6,9 mmol/L)<br>"
                "Diabetes: ≥ 126 mg/dL (≥ 7,0 mmol/L) — bei zwei getrennten Messungen</div>"
                "<p><strong>Unterzuckerung (Hypoglykämie)</strong> — unter 70 mg/dL — kann Zittern, Schwitzen, Verwirrtheit und in schweren Fällen Bewusstlosigkeit verursachen.</p>"
                "<p><strong>Ein erhöhter Nüchternblutzucker</strong> deutet darauf hin, dass Ihr Körper nicht genügend Insulin produziert oder Ihre Zellen nicht richtig darauf ansprechen (Insulinresistenz).</p>"
                "<div class='blog-example'><strong>Wichtig:</strong> Ein einzelner erhöhter Wert diagnostiziert keinen Diabetes. Ihr Arzt wird den Test wiederholen oder einen HbA1c anfordern.</div>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c: Ihr 3-Monats-Blutzuckerdurchschnitt",
            body_html=(
                "<p>HbA1c misst den Anteil des Hämoglobins, an den Glukose gebunden ist. Da rote Blutkörperchen etwa 120 Tage leben, "
                "spiegelt HbA1c Ihren <strong>durchschnittlichen Blutzucker der letzten 2-3 Monate</strong> wider.</p>"
                "<div class='blog-definition'><strong>Referenzbereiche:</strong><br>"
                "Normal: &lt; 5,7 % (&lt; 39 mmol/mol)<br>"
                "Prädiabetes: 5,7–6,4 % (39–47 mmol/mol)<br>"
                "Diabetes: ≥ 6,5 % (≥ 48 mmol/mol)</div>"
                "<p><strong>Zielwerte für Diabetiker:</strong></p>"
                "<ul>"
                "<li>Allgemeines Ziel: &lt; 7,0 % (ADA-Empfehlung)</li>"
                "<li>Strengeres Ziel: &lt; 6,5 % für jüngere Patienten ohne Komplikationen</li>"
                "<li>Lockereres Ziel: &lt; 8,0 % für ältere Patienten oder bei Hypoglykämierisiko</li>"
                "</ul>"
                "<p>Jede Senkung des HbA1c um 1 % reduziert das Risiko mikrovaskulärer Komplikationen um etwa <strong>35-40 %</strong>.</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="Nüchterninsulin & HOMA-IR: Insulinresistenz frühzeitig erkennen",
            body_html=(
                "<p><strong>Insulin</strong> ermöglicht es Glukose, in Ihre Zellen einzutreten. Bei Insulinresistenz produziert die Bauchspeicheldrüse kompensatorisch mehr Insulin — <strong>Hyperinsulinämie</strong>.</p>"
                "<div class='blog-definition'><strong>Nüchterninsulin:</strong> Optimal: 2–6 µIU/mL · Normal: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (Nüchterninsulin × Nüchternglukose) / 405<br>"
                "Normal: &lt; 1,0 · Grenzwertig: 1,0–2,0 · Insulinresistent: &gt; 2,0 · Ausgeprägt: &gt; 3,0</div>"
                "<p>HOMA-IR kann Stoffwechselstörungen <strong>Jahre vor</strong> einem Anstieg von Nüchternglukose oder HbA1c erkennen. Besonders wertvoll bei:</p>"
                "<ul>"
                "<li>Polyzystisches Ovarsyndrom (PCOS)</li>"
                "<li>Metabolisches Syndrom</li>"
                "<li>Nicht-alkoholische Fettlebererkrankung (NAFLD)</li>"
                "<li>Familiäre Vorbelastung mit Typ-2-Diabetes</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="Oraler Glukosetoleranztest (oGTT)",
            body_html=(
                "<p>Der oGTT ist der Goldstandard zur Diagnose von <strong>Gestationsdiabetes</strong> und wird auch bei grenzwertigen Nüchternwerten eingesetzt.</p>"
                "<p><strong>Ablauf:</strong> Nach einer Nüchternblutentnahme trinken Sie eine 75-g-Glukoselösung. "
                "Blut wird nach 1 und 2 Stunden erneut abgenommen.</p>"
                "<div class='blog-definition'><strong>2-Stunden-oGTT-Werte:</strong><br>"
                "Normal: &lt; 140 mg/dL (7,8 mmol/L)<br>"
                "Gestörte Glukosetoleranz (Prädiabetes): 140–199 mg/dL<br>"
                "Diabetes: ≥ 200 mg/dL (≥ 11,1 mmol/L)</div>"
                "<p>Der oGTT ist empfindlicher als der Nüchternblutzucker allein — er kann eine gestörte Glukosetoleranz erkennen, auch wenn die Nüchternwerte normal sind.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="Risikofaktoren & Symptome eines erhöhten Blutzuckers",
            body_html=(
                "<p><strong>Risikofaktoren für erhöhten Blutzucker / Typ-2-Diabetes:</strong></p>"
                "<ul>"
                "<li>Übergewicht oder Adipositas (besonders viszerales Bauchfett)</li>"
                "<li>Bewegungsmangel</li>"
                "<li>Familiäre Vorbelastung (Verwandte ersten Grades)</li>"
                "<li>Alter ≥ 45 Jahre</li>"
                "<li>Gestationsdiabetes in der Vorgeschichte</li>"
                "<li>PCOS</li>"
                "<li>Bluthochdruck (≥ 140/90 mmHg)</li>"
                "</ul>"
                "<p><strong>Symptome einer Hyperglykämie:</strong></p>"
                "<ul>"
                "<li>Übermäßiger Durst (Polydipsie) und häufiges Wasserlassen (Polyurie)</li>"
                "<li>Unerklärlicher Gewichtsverlust</li>"
                "<li>Müdigkeit und Schwäche</li>"
                "<li>Verschwommenes Sehen</li>"
                "<li>Schlecht heilende Wunden</li>"
                "<li>Kribbeln oder Taubheit in Händen und Füßen</li>"
                "</ul>"
                "<div class='blog-example'><strong>Warnung:</strong> Typ-2-Diabetes kann <em>jahrelang symptomlos</em> verlaufen. Regelmäßige Vorsorge ist bei Risikofaktoren unerlässlich.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="Ernährung & Lebensstil für gesunde Blutzuckerwerte",
            body_html=(
                "<p>Evidenzbasierte Strategien für einen gesunden Blutzucker:</p>"
                "<ul>"
                "<li><strong>Niedrig-glykämische Lebensmittel wählen:</strong> Vollkornprodukte, Hülsenfrüchte, nicht-stärkehaltiges Gemüse.</li>"
                "<li><strong>Ballaststoffe priorisieren:</strong> 25-30 g/Tag. Gute Quellen: Haferflocken, Linsen, Chiasamen, Gemüse.</li>"
                "<li><strong>Kohlenhydrate mit Eiweiß oder gesundem Fett kombinieren</strong> — das reduziert den glykämischen Anstieg.</li>"
                "<li><strong>Regelmäßig bewegen:</strong> 150 Minuten moderate Bewegung pro Woche verbessern die Insulinsensitivität.</li>"
                "<li><strong>Gesundes Gewicht halten:</strong> Schon 5-7 % Gewichtsverlust kann das Diabetesrisiko bei Prädiabetes um bis zu 58 % senken.</li>"
                "<li><strong>Stress bewältigen:</strong> Cortisol erhöht den Blutzucker. Achtsamkeit, Atemübungen und ausreichend Schlaf (7-9 Stunden) helfen.</li>"
                "<li><strong>Mediterrane Ernährung erwägen:</strong> Reich an Olivenöl, Gemüse, Fisch und Vollkorn.</li>"
                "</ul>"
                "<div class='blog-example'><strong>Schneller Tipp:</strong> Ein 15-minütiger Spaziergang nach dem Essen kann postprandiale Glukosespitzen um 20-30 % senken.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="Wie NoryaAI Ihre Blutzuckerwerte analysiert",
            body_html=(
                "<p>NoryaAI liest Ihren vollständigen Laborbefund — ob PDF oder Foto — und analysiert automatisch:</p>"
                "<ul>"
                "<li>Nüchternglukose, HbA1c, Nüchterninsulin, HOMA-IR und oGTT-Werte</li>"
                "<li>Klassifizierung in Normal-, Prädiabetes- oder Diabetes-Bereiche</li>"
                "<li>Erkennung von Insulinresistenz, selbst bei normalen Glukosewerten</li>"
                "<li>Verständliche Erklärungen für jeden Marker</li>"
                "<li>Arztfertige Zusammenfassung mit Trendverfolgung</li>"
                "</ul>"
                "<p>Laden Sie Ihren Laborbericht hoch und erhalten Sie Ihre Analyse in Minuten.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Spanish
# ---------------------------------------------------------------------------

def _bs_sections_es() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="¿Qué miden las pruebas de azúcar en sangre?",
            body_html=(
                "<p>Las pruebas de azúcar en sangre (glucemia) miden la cantidad de <strong>glucosa</strong> — la principal fuente de energía del cuerpo — en el torrente sanguíneo. "
                "La glucosa proviene de los alimentos y es regulada por la hormona <strong>insulina</strong>, producida por el páncreas.</p>"
                "<p>Existen varios tipos de pruebas de glucemia:</p>"
                "<ul>"
                "<li><strong>Glucosa en ayunas (GA)</strong> — medida tras 8-12 horas de ayuno; la prueba de detección estándar.</li>"
                "<li><strong>Glucosa aleatoria</strong> — tomada en cualquier momento; útil en urgencias.</li>"
                "<li><strong>Prueba de tolerancia oral a la glucosa (PTOG / OGTT)</strong> — mide la glucosa antes y 2 horas después de ingerir 75 g de glucosa.</li>"
                "<li><strong>HbA1c (Hemoglobina glicosilada)</strong> — refleja el promedio de glucemia de los últimos 2-3 meses.</li>"
                "<li><strong>Insulina en ayunas y HOMA-IR</strong> — evalúan la resistencia a la insulina incluso antes de que la glucosa suba.</li>"
                "</ul>"
                "<p>La OMS estima que más de <strong>422 millones de personas</strong> en el mundo viven con diabetes.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="Glucosa en ayunas: rangos normal, prediabetes y diabetes",
            body_html=(
                "<p>La glucosa en ayunas se mide tras al menos 8 horas de ayuno nocturno.</p>"
                "<div class='blog-definition'><strong>Rangos de referencia (plasma venoso):</strong><br>"
                "Normal: 70–99 mg/dL (3,9–5,5 mmol/L)<br>"
                "Prediabetes: 100–125 mg/dL (5,6–6,9 mmol/L)<br>"
                "Diabetes: ≥ 126 mg/dL (≥ 7,0 mmol/L) en dos mediciones separadas</div>"
                "<p><strong>Hipoglucemia</strong> — por debajo de 70 mg/dL — puede causar temblores, sudoración, confusión y pérdida de conciencia.</p>"
                "<p><strong>Una glucosa en ayunas elevada</strong> indica que su cuerpo no produce suficiente insulina o que sus células no responden adecuadamente (resistencia a la insulina).</p>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c: su promedio de glucemia de 3 meses",
            body_html=(
                "<p>La HbA1c mide el porcentaje de hemoglobina con glucosa unida. Como los glóbulos rojos viven unos 120 días, "
                "la HbA1c refleja su <strong>glucemia promedio de los últimos 2-3 meses</strong>.</p>"
                "<div class='blog-definition'><strong>Rangos de referencia:</strong><br>"
                "Normal: &lt; 5,7 %<br>"
                "Prediabetes: 5,7–6,4 %<br>"
                "Diabetes: ≥ 6,5 %</div>"
                "<p><strong>Objetivos para personas con diabetes:</strong></p>"
                "<ul>"
                "<li>Objetivo general: &lt; 7,0 % (recomendación ADA)</li>"
                "<li>Objetivo estricto: &lt; 6,5 % para pacientes jóvenes sin complicaciones</li>"
                "<li>Objetivo flexible: &lt; 8,0 % para pacientes mayores o con riesgo de hipoglucemia</li>"
                "</ul>"
                "<p>Cada reducción del 1 % en HbA1c disminuye el riesgo de complicaciones microvasculares en aproximadamente un <strong>35-40 %</strong>.</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="Insulina en ayunas y HOMA-IR: detección temprana de resistencia a la insulina",
            body_html=(
                "<p>La <strong>insulina</strong> permite que la glucosa entre en las células. Cuando hay resistencia a la insulina, el páncreas produce más — causando <strong>hiperinsulinemia</strong>.</p>"
                "<div class='blog-definition'><strong>Insulina en ayunas:</strong> Óptima: 2–6 µIU/mL · Normal: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (Insulina en ayunas × Glucosa en ayunas) / 405<br>"
                "Normal: &lt; 1,0 · Límite: 1,0–2,0 · Resistencia: &gt; 2,0 · Significativa: &gt; 3,0</div>"
                "<p>El HOMA-IR puede detectar disfunción metabólica <strong>años antes</strong> de que la glucosa o la HbA1c se alteren. Especialmente útil en:</p>"
                "<ul>"
                "<li>Síndrome de Ovario Poliquístico (SOP)</li>"
                "<li>Síndrome metabólico</li>"
                "<li>Hígado graso no alcohólico (NAFLD)</li>"
                "<li>Antecedentes familiares de diabetes tipo 2</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="Prueba de tolerancia oral a la glucosa (PTOG)",
            body_html=(
                "<p>La PTOG es el estándar de oro para diagnosticar <strong>diabetes gestacional</strong> y se usa cuando los valores de glucosa en ayunas o HbA1c son limítrofes.</p>"
                "<div class='blog-definition'><strong>Valores a las 2 horas (75 g de glucosa):</strong><br>"
                "Normal: &lt; 140 mg/dL<br>"
                "Tolerancia alterada a la glucosa (prediabetes): 140–199 mg/dL<br>"
                "Diabetes: ≥ 200 mg/dL</div>"
                "<p>La PTOG es más sensible que la glucosa en ayunas sola — puede detectar intolerancia a la glucosa incluso con valores en ayunas normales.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="Factores de riesgo y síntomas de hiperglucemia",
            body_html=(
                "<p><strong>Factores de riesgo:</strong></p>"
                "<ul>"
                "<li>Sobrepeso u obesidad (especialmente grasa abdominal)</li>"
                "<li>Sedentarismo</li>"
                "<li>Antecedentes familiares de diabetes</li>"
                "<li>Edad ≥ 45 años</li>"
                "<li>Diabetes gestacional previa</li>"
                "<li>Síndrome de Ovario Poliquístico (SOP)</li>"
                "<li>Hipertensión arterial</li>"
                "</ul>"
                "<p><strong>Síntomas de hiperglucemia:</strong></p>"
                "<ul>"
                "<li>Sed excesiva (polidipsia) y micción frecuente (poliuria)</li>"
                "<li>Pérdida de peso inexplicable</li>"
                "<li>Fatiga y debilidad</li>"
                "<li>Visión borrosa</li>"
                "<li>Heridas que cicatrizan lentamente</li>"
                "<li>Hormigueo o entumecimiento en manos y pies</li>"
                "</ul>"
                "<div class='blog-example'><strong>Advertencia:</strong> La diabetes tipo 2 puede ser <em>asintomática</em> durante años. El cribado regular es esencial.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="Dieta y estilo de vida para un azúcar saludable",
            body_html=(
                "<p>Estrategias basadas en evidencia:</p>"
                "<ul>"
                "<li><strong>Alimentos de bajo índice glucémico:</strong> cereales integrales, legumbres, verduras sin almidón.</li>"
                "<li><strong>Priorizar la fibra:</strong> 25-30 g/día. Fuentes: avena, lentejas, semillas de chía, verduras.</li>"
                "<li><strong>Combinar carbohidratos con proteína o grasa saludable</strong> para reducir los picos glucémicos.</li>"
                "<li><strong>Ejercicio regular:</strong> 150 minutos semanales de actividad moderada mejoran la sensibilidad a la insulina.</li>"
                "<li><strong>Mantener un peso saludable:</strong> perder un 5-7 % del peso corporal puede reducir el riesgo de diabetes hasta un 58 %.</li>"
                "<li><strong>Gestionar el estrés:</strong> el cortisol eleva la glucemia. Meditación, respiración profunda y 7-9 horas de sueño ayudan.</li>"
                "<li><strong>Dieta mediterránea:</strong> rica en aceite de oliva, verduras, pescado y cereales integrales.</li>"
                "</ul>"
                "<div class='blog-example'><strong>Consejo rápido:</strong> Caminar 15 minutos después de comer puede reducir los picos posprandiales un 20-30 %.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="Cómo NoryaAI analiza sus resultados de glucemia",
            body_html=(
                "<p>NoryaAI lee su informe de laboratorio completo — ya sea un PDF o una foto — y automáticamente:</p>"
                "<ul>"
                "<li>Identifica glucosa en ayunas, HbA1c, insulina, HOMA-IR y valores de PTOG</li>"
                "<li>Clasifica los resultados en rangos normal, prediabetes o diabetes</li>"
                "<li>Detecta resistencia a la insulina incluso con glucosa normal</li>"
                "<li>Proporciona explicaciones claras para cada marcador</li>"
                "<li>Genera un resumen listo para el médico con seguimiento de tendencias</li>"
                "</ul>"
                "<p>Suba su informe de laboratorio y obtenga su análisis de glucemia en minutos.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# French
# ---------------------------------------------------------------------------

def _bs_sections_fr() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="Que mesurent les tests de glycémie ?",
            body_html=(
                "<p>Les tests de glycémie mesurent la quantité de <strong>glucose</strong> — la principale source d'énergie de l'organisme — dans le sang. "
                "Le glucose provient de l'alimentation et est régulé par l'<strong>insuline</strong>, une hormone produite par le pancréas.</p>"
                "<p>Plusieurs types de tests existent :</p>"
                "<ul>"
                "<li><strong>Glycémie à jeun (GAJ)</strong> — mesurée après 8-12 heures de jeûne ; le test de dépistage standard.</li>"
                "<li><strong>Glycémie aléatoire</strong> — prélevée à tout moment ; utile en urgence.</li>"
                "<li><strong>Épreuve d'hyperglycémie provoquée par voie orale (HGPO / OGTT)</strong> — mesure la glycémie avant et 2 heures après ingestion de 75 g de glucose.</li>"
                "<li><strong>HbA1c (Hémoglobine glyquée)</strong> — reflète la glycémie moyenne des 2-3 derniers mois.</li>"
                "<li><strong>Insuline à jeun &amp; HOMA-IR</strong> — évaluent la résistance à l'insuline avant même que la glycémie n'augmente.</li>"
                "</ul>"
                "<p>L'OMS estime que plus de <strong>422 millions de personnes</strong> vivent avec le diabète dans le monde.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="Glycémie à jeun : valeurs normales, prédiabète et diabète",
            body_html=(
                "<p>La glycémie à jeun est mesurée après au moins 8 heures de jeûne nocturne.</p>"
                "<div class='blog-definition'><strong>Valeurs de référence (plasma veineux) :</strong><br>"
                "Normal : 70–99 mg/dL (3,9–5,5 mmol/L)<br>"
                "Prédiabète : 100–125 mg/dL (5,6–6,9 mmol/L)<br>"
                "Diabète : ≥ 126 mg/dL (≥ 7,0 mmol/L) lors de deux mesures séparées</div>"
                "<p><strong>L'hypoglycémie</strong> — en dessous de 70 mg/dL — peut provoquer tremblements, sueurs, confusion et perte de connaissance.</p>"
                "<p><strong>Une glycémie à jeun élevée</strong> indique une production insuffisante d'insuline ou une résistance à l'insuline.</p>"
                "<div class='blog-example'><strong>Important :</strong> Une seule valeur élevée ne suffit pas à diagnostiquer le diabète. Votre médecin répétera le test ou demandera une HbA1c.</div>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c : votre moyenne glycémique sur 3 mois",
            body_html=(
                "<p>L'HbA1c mesure le pourcentage d'hémoglobine liée au glucose. Comme les globules rouges vivent environ 120 jours, "
                "l'HbA1c reflète votre <strong>glycémie moyenne des 2-3 derniers mois</strong>.</p>"
                "<div class='blog-definition'><strong>Valeurs de référence :</strong><br>"
                "Normal : &lt; 5,7 %<br>"
                "Prédiabète : 5,7–6,4 %<br>"
                "Diabète : ≥ 6,5 %</div>"
                "<p><strong>Objectifs pour les diabétiques :</strong></p>"
                "<ul>"
                "<li>Objectif général : &lt; 7,0 % (recommandation ADA)</li>"
                "<li>Objectif strict : &lt; 6,5 % pour les patients jeunes sans complications</li>"
                "<li>Objectif assoupli : &lt; 8,0 % pour les patients âgés ou à risque d'hypoglycémie</li>"
                "</ul>"
                "<p>Chaque réduction de 1 % de l'HbA1c diminue le risque de complications microvasculaires d'environ <strong>35-40 %</strong>.</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="Insuline à jeun & HOMA-IR : détecter la résistance à l'insuline",
            body_html=(
                "<p>L'<strong>insuline</strong> permet au glucose d'entrer dans les cellules. En cas de résistance, le pancréas produit davantage — c'est l'<strong>hyperinsulinémie</strong>.</p>"
                "<div class='blog-definition'><strong>Insuline à jeun :</strong> Optimale : 2–6 µIU/mL · Normale : &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (Insuline à jeun × Glycémie à jeun) / 405<br>"
                "Normal : &lt; 1,0 · Limite : 1,0–2,0 · Résistance : &gt; 2,0 · Marquée : &gt; 3,0</div>"
                "<p>Le HOMA-IR peut détecter un dysfonctionnement métabolique <strong>des années avant</strong> que la glycémie ou l'HbA1c ne s'altèrent. Particulièrement utile en cas de :</p>"
                "<ul>"
                "<li>Syndrome des ovaires polykystiques (SOPK)</li>"
                "<li>Syndrome métabolique</li>"
                "<li>Stéatose hépatique non alcoolique (NAFLD)</li>"
                "<li>Antécédents familiaux de diabète de type 2</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="Épreuve d'hyperglycémie provoquée par voie orale (HGPO)",
            body_html=(
                "<p>L'HGPO est le gold standard pour diagnostiquer le <strong>diabète gestationnel</strong> et est également utilisée lorsque les valeurs à jeun ou l'HbA1c sont limites.</p>"
                "<div class='blog-definition'><strong>Valeurs à 2 heures (75 g de glucose) :</strong><br>"
                "Normal : &lt; 140 mg/dL (7,8 mmol/L)<br>"
                "Intolérance au glucose (prédiabète) : 140–199 mg/dL<br>"
                "Diabète : ≥ 200 mg/dL (≥ 11,1 mmol/L)</div>"
                "<p>L'HGPO est plus sensible que la glycémie à jeun seule — elle peut détecter une intolérance au glucose même avec des valeurs à jeun normales.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="Facteurs de risque et symptômes de l'hyperglycémie",
            body_html=(
                "<p><strong>Facteurs de risque :</strong></p>"
                "<ul>"
                "<li>Surpoids ou obésité (en particulier graisse abdominale)</li>"
                "<li>Sédentarité</li>"
                "<li>Antécédents familiaux de diabète</li>"
                "<li>Âge ≥ 45 ans</li>"
                "<li>Diabète gestationnel antérieur</li>"
                "<li>Syndrome des ovaires polykystiques (SOPK)</li>"
                "<li>Hypertension artérielle</li>"
                "</ul>"
                "<p><strong>Symptômes d'hyperglycémie :</strong></p>"
                "<ul>"
                "<li>Soif excessive (polydipsie) et mictions fréquentes (polyurie)</li>"
                "<li>Perte de poids inexpliquée</li>"
                "<li>Fatigue et faiblesse</li>"
                "<li>Vision floue</li>"
                "<li>Cicatrisation lente des plaies</li>"
                "<li>Fourmillements ou engourdissements aux mains et pieds</li>"
                "</ul>"
                "<div class='blog-example'><strong>Attention :</strong> Le diabète de type 2 peut rester <em>asymptomatique</em> pendant des années. Le dépistage régulier est essentiel.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="Alimentation et mode de vie pour une glycémie saine",
            body_html=(
                "<p>Stratégies fondées sur les preuves :</p>"
                "<ul>"
                "<li><strong>Aliments à index glycémique bas :</strong> céréales complètes, légumineuses, légumes non féculents.</li>"
                "<li><strong>Fibres :</strong> 25-30 g/jour. Sources : flocons d'avoine, lentilles, graines de chia, légumes.</li>"
                "<li><strong>Associer glucides et protéines ou bonnes graisses</strong> pour atténuer les pics glycémiques.</li>"
                "<li><strong>Activité physique régulière :</strong> 150 minutes par semaine d'exercice modéré améliorent la sensibilité à l'insuline.</li>"
                "<li><strong>Maintenir un poids sain :</strong> perdre 5-7 % du poids corporel peut réduire le risque de diabète de 58 %.</li>"
                "<li><strong>Gérer le stress :</strong> le cortisol augmente la glycémie. Méditation, respiration profonde et 7-9 heures de sommeil.</li>"
                "<li><strong>Régime méditerranéen :</strong> riche en huile d'olive, légumes, poisson et céréales complètes.</li>"
                "</ul>"
                "<div class='blog-example'><strong>Astuce :</strong> 15 minutes de marche après les repas peuvent réduire les pics postprandiaux de 20-30 %.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="Comment NoryaAI analyse vos résultats de glycémie",
            body_html=(
                "<p>NoryaAI lit votre bilan sanguin complet — PDF ou photo — et automatiquement :</p>"
                "<ul>"
                "<li>Identifie la glycémie à jeun, HbA1c, insuline, HOMA-IR et les valeurs HGPO</li>"
                "<li>Classe les résultats en catégories normal, prédiabète ou diabète</li>"
                "<li>Détecte la résistance à l'insuline même avec une glycémie normale</li>"
                "<li>Fournit des explications claires pour chaque marqueur</li>"
                "<li>Génère un résumé prêt pour le médecin avec suivi des tendances</li>"
                "</ul>"
                "<p>Téléchargez votre bilan et obtenez votre analyse glycémique en quelques minutes.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Italian
# ---------------------------------------------------------------------------

def _bs_sections_it() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="Cosa misurano gli esami della glicemia?",
            body_html=(
                "<p>Gli esami della glicemia misurano la quantità di <strong>glucosio</strong> — la principale fonte di energia dell'organismo — nel sangue. "
                "Il glucosio proviene dagli alimenti ed è regolato dall'<strong>insulina</strong>, un ormone prodotto dal pancreas.</p>"
                "<p>Esistono diversi tipi di esami glicemici:</p>"
                "<ul>"
                "<li><strong>Glicemia a digiuno</strong> — misurata dopo 8-12 ore di digiuno; il test di screening standard.</li>"
                "<li><strong>Glicemia casuale</strong> — prelevata in qualsiasi momento; utile in emergenza.</li>"
                "<li><strong>Test di tolleranza orale al glucosio (OGTT)</strong> — misura la glicemia prima e 2 ore dopo l'ingestione di 75 g di glucosio.</li>"
                "<li><strong>HbA1c (Emoglobina glicata)</strong> — riflette la glicemia media degli ultimi 2-3 mesi.</li>"
                "<li><strong>Insulina a digiuno e HOMA-IR</strong> — valutano la resistenza all'insulina anche prima che la glicemia salga.</li>"
                "</ul>"
                "<p>L'OMS stima che oltre <strong>422 milioni di persone</strong> nel mondo vivano con il diabete.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="Glicemia a digiuno: valori normali, prediabete e diabete",
            body_html=(
                "<p>La glicemia a digiuno viene misurata dopo almeno 8 ore di digiuno notturno.</p>"
                "<div class='blog-definition'><strong>Intervalli di riferimento (plasma venoso):</strong><br>"
                "Normale: 70–99 mg/dL (3,9–5,5 mmol/L)<br>"
                "Prediabete: 100–125 mg/dL (5,6–6,9 mmol/L)<br>"
                "Diabete: ≥ 126 mg/dL (≥ 7,0 mmol/L) in due misurazioni separate</div>"
                "<p><strong>Ipoglicemia</strong> — sotto 70 mg/dL — può causare tremori, sudorazione, confusione e perdita di coscienza.</p>"
                "<p><strong>Una glicemia a digiuno elevata</strong> indica produzione insufficiente di insulina o resistenza insulinica.</p>"
                "<div class='blog-example'><strong>Importante:</strong> Un singolo valore elevato non diagnostica il diabete. Il medico ripeterà l'esame o richiederà un'HbA1c.</div>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c: la media glicemica di 3 mesi",
            body_html=(
                "<p>L'HbA1c misura la percentuale di emoglobina legata al glucosio. Poiché i globuli rossi vivono circa 120 giorni, "
                "l'HbA1c riflette la <strong>glicemia media degli ultimi 2-3 mesi</strong>.</p>"
                "<div class='blog-definition'><strong>Intervalli di riferimento:</strong><br>"
                "Normale: &lt; 5,7 %<br>"
                "Prediabete: 5,7–6,4 %<br>"
                "Diabete: ≥ 6,5 %</div>"
                "<p><strong>Obiettivi per i diabetici:</strong></p>"
                "<ul>"
                "<li>Obiettivo generale: &lt; 7,0 % (raccomandazione ADA)</li>"
                "<li>Obiettivo più stretto: &lt; 6,5 % per pazienti giovani senza complicanze</li>"
                "<li>Obiettivo più flessibile: &lt; 8,0 % per pazienti anziani o a rischio ipoglicemico</li>"
                "</ul>"
                "<p>Ogni riduzione dell'1 % dell'HbA1c diminuisce il rischio di complicanze microvascolari di circa il <strong>35-40 %</strong>.</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="Insulina a digiuno e HOMA-IR: rilevare la resistenza insulinica",
            body_html=(
                "<p>L'<strong>insulina</strong> permette al glucosio di entrare nelle cellule. In caso di resistenza, il pancreas ne produce di più — <strong>iperinsulinemia</strong>.</p>"
                "<div class='blog-definition'><strong>Insulina a digiuno:</strong> Ottimale: 2–6 µIU/mL · Normale: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (Insulina a digiuno × Glicemia a digiuno) / 405<br>"
                "Normale: &lt; 1,0 · Limite: 1,0–2,0 · Resistenza: &gt; 2,0 · Significativa: &gt; 3,0</div>"
                "<p>Il HOMA-IR può rilevare disfunzioni metaboliche <strong>anni prima</strong> che la glicemia o l'HbA1c diventino anomale. Particolarmente utile in:</p>"
                "<ul>"
                "<li>Sindrome dell'ovaio policistico (PCOS)</li>"
                "<li>Sindrome metabolica</li>"
                "<li>Steatosi epatica non alcolica (NAFLD)</li>"
                "<li>Familiarità per diabete di tipo 2</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="Test di tolleranza orale al glucosio (OGTT)",
            body_html=(
                "<p>L'OGTT è il gold standard per la diagnosi del <strong>diabete gestazionale</strong> e viene utilizzato anche con valori a digiuno o HbA1c borderline.</p>"
                "<div class='blog-definition'><strong>Valori a 2 ore (75 g di glucosio):</strong><br>"
                "Normale: &lt; 140 mg/dL (7,8 mmol/L)<br>"
                "Ridotta tolleranza al glucosio (prediabete): 140–199 mg/dL<br>"
                "Diabete: ≥ 200 mg/dL (≥ 11,1 mmol/L)</div>"
                "<p>L'OGTT è più sensibile della glicemia a digiuno da sola — può rilevare intolleranza al glucosio anche con valori a digiuno normali.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="Fattori di rischio e sintomi dell'iperglicemia",
            body_html=(
                "<p><strong>Fattori di rischio:</strong></p>"
                "<ul>"
                "<li>Sovrappeso o obesità (soprattutto grasso addominale viscerale)</li>"
                "<li>Stile di vita sedentario</li>"
                "<li>Familiarità per diabete</li>"
                "<li>Età ≥ 45 anni</li>"
                "<li>Diabete gestazionale pregresso</li>"
                "<li>Sindrome dell'ovaio policistico (PCOS)</li>"
                "<li>Ipertensione arteriosa</li>"
                "</ul>"
                "<p><strong>Sintomi dell'iperglicemia:</strong></p>"
                "<ul>"
                "<li>Sete eccessiva (polidipsia) e minzione frequente (poliuria)</li>"
                "<li>Perdita di peso inspiegabile</li>"
                "<li>Stanchezza e debolezza</li>"
                "<li>Visione offuscata</li>"
                "<li>Ferite che guariscono lentamente</li>"
                "<li>Formicolio o intorpidimento a mani e piedi</li>"
                "</ul>"
                "<div class='blog-example'><strong>Attenzione:</strong> Il diabete di tipo 2 può essere <em>asintomatico</em> per anni. Lo screening regolare è fondamentale.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="Dieta e stile di vita per una glicemia sana",
            body_html=(
                "<p>Strategie basate sull'evidenza:</p>"
                "<ul>"
                "<li><strong>Alimenti a basso indice glicemico:</strong> cereali integrali, legumi, verdure non amidacee.</li>"
                "<li><strong>Fibre:</strong> 25-30 g/giorno. Fonti: fiocchi d'avena, lenticchie, semi di chia, verdure.</li>"
                "<li><strong>Abbinare carboidrati a proteine o grassi sani</strong> per ridurre i picchi glicemici.</li>"
                "<li><strong>Attività fisica regolare:</strong> 150 minuti settimanali di esercizio moderato migliorano la sensibilità insulinica.</li>"
                "<li><strong>Mantenere un peso sano:</strong> perdere il 5-7 % del peso corporeo può ridurre il rischio di diabete fino al 58 %.</li>"
                "<li><strong>Gestire lo stress:</strong> il cortisolo alza la glicemia. Meditazione, respirazione profonda e 7-9 ore di sonno.</li>"
                "<li><strong>Dieta mediterranea:</strong> ricca di olio d'oliva, verdure, pesce e cereali integrali.</li>"
                "</ul>"
                "<div class='blog-example'><strong>Consiglio rapido:</strong> 15 minuti di passeggiata dopo i pasti possono ridurre i picchi postprandiali del 20-30 %.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="Come NoryaAI analizza i tuoi risultati glicemici",
            body_html=(
                "<p>NoryaAI legge il tuo referto completo — PDF o foto — e automaticamente:</p>"
                "<ul>"
                "<li>Identifica glicemia a digiuno, HbA1c, insulina, HOMA-IR e valori OGTT</li>"
                "<li>Classifica i risultati in intervalli normale, prediabete o diabete</li>"
                "<li>Rileva la resistenza insulinica anche con glicemia normale</li>"
                "<li>Fornisce spiegazioni chiare per ogni marcatore</li>"
                "<li>Genera un referto pronto per il medico con monitoraggio nel tempo</li>"
                "</ul>"
                "<p>Carica il tuo referto di laboratorio e ottieni la tua analisi glicemica in pochi minuti.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hebrew
# ---------------------------------------------------------------------------

def _bs_sections_he() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="מה מודדות בדיקות סוכר בדם?",
            body_html=(
                "<p>בדיקות סוכר בדם (גלוקוז) מודדות את כמות ה<strong>גלוקוז</strong> — מקור האנרגיה העיקרי של הגוף — בזרם הדם. "
                "הגלוקוז מגיע מהמזון ומווסת על ידי הורמון ה<strong>אינסולין</strong>, המיוצר בלבלב.</p>"
                "<p>קיימים מספר סוגי בדיקות:</p>"
                "<ul>"
                "<li><strong>גלוקוז בצום</strong> — נמדד לאחר 8-12 שעות צום; בדיקת הסקירה הסטנדרטית.</li>"
                "<li><strong>גלוקוז אקראי</strong> — נלקח בכל זמן; שימושי במצבי חירום.</li>"
                "<li><strong>מבחן העמסת סוכר (OGTT)</strong> — מודד גלוקוז לפני ושעתיים אחרי שתיית תמיסת 75 גרם גלוקוז.</li>"
                "<li><strong>HbA1c (המוגלובין מסוכרר)</strong> — משקף את ממוצע הסוכר בדם ב-2-3 החודשים האחרונים.</li>"
                "<li><strong>אינסולין בצום ו-HOMA-IR</strong> — מעריכים תנגודת לאינסולין עוד לפני שהגלוקוז עולה.</li>"
                "</ul>"
                "<p>ארגון הבריאות העולמי מעריך שיותר מ-<strong>422 מיליון אנשים</strong> ברחבי העולם חיים עם סוכרת.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="גלוקוז בצום: טווחים תקינים, טרום-סוכרת וסוכרת",
            body_html=(
                "<p>גלוקוז בצום נמדד לאחר צום לילי של לפחות 8 שעות.</p>"
                "<div class='blog-definition'><strong>טווחי ייחוס (פלזמה ורידית):</strong><br>"
                "תקין: 70–99 mg/dL (3.9–5.5 mmol/L)<br>"
                "טרום-סוכרת: 100–125 mg/dL (5.6–6.9 mmol/L)<br>"
                "סוכרת: ≥ 126 mg/dL (≥ 7.0 mmol/L) בשתי מדידות נפרדות</div>"
                "<p><strong>היפוגליקמיה</strong> — מתחת ל-70 mg/dL — עלולה לגרום לרעד, הזעה, בלבול ובמקרים חמורים לאיבוד הכרה.</p>"
                "<p><strong>גלוקוז בצום גבוה</strong> מעיד על ייצור לא מספק של אינסולין או על תנגודת לאינסולין.</p>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c: ממוצע הסוכר שלך ב-3 חודשים",
            body_html=(
                "<p>HbA1c מודד את אחוז ההמוגלובין שגלוקוז נקשר אליו. מכיוון שתאי דם אדומים חיים כ-120 יום, "
                "HbA1c משקף את <strong>ממוצע הסוכר בדם ב-2-3 החודשים האחרונים</strong>.</p>"
                "<div class='blog-definition'><strong>טווחי ייחוס:</strong><br>"
                "תקין: &lt; 5.7%<br>"
                "טרום-סוכרת: 5.7–6.4%<br>"
                "סוכרת: ≥ 6.5%</div>"
                "<p><strong>יעדים לחולי סוכרת:</strong></p>"
                "<ul>"
                "<li>יעד כללי: &lt; 7.0% (המלצת ADA)</li>"
                "<li>יעד הדוק: &lt; 6.5% למטופלים צעירים ללא סיבוכים</li>"
                "<li>יעד גמיש: &lt; 8.0% למטופלים מבוגרים או בסיכון להיפוגליקמיה</li>"
                "</ul>"
                "<p>כל ירידה של 1% ב-HbA1c מפחיתה סיכון לסיבוכים מיקרווסקולריים בכ-<strong>35-40%</strong>.</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="אינסולין בצום ו-HOMA-IR: גילוי מוקדם של תנגודת לאינסולין",
            body_html=(
                "<p><strong>אינסולין</strong> מאפשר לגלוקוז להיכנס לתאים. כשהתאים מפתחים תנגודת, הלבלב מייצר יותר — <strong>היפראינסולינמיה</strong>.</p>"
                "<div class='blog-definition'><strong>אינסולין בצום:</strong> אופטימלי: 2–6 µIU/mL · תקין: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (אינסולין בצום × גלוקוז בצום) / 405<br>"
                "תקין: &lt; 1.0 · גבולי: 1.0–2.0 · תנגודת: &gt; 2.0 · משמעותית: &gt; 3.0</div>"
                "<p>HOMA-IR יכול לגלות הפרעות מטבוליות <strong>שנים לפני</strong> שגלוקוז בצום או HbA1c הופכים חריגים. שימושי במיוחד ב:</p>"
                "<ul>"
                "<li>תסמונת השחלות הפוליציסטיות (PCOS)</li>"
                "<li>תסמונת מטבולית</li>"
                "<li>כבד שומני לא אלכוהולי (NAFLD)</li>"
                "<li>היסטוריה משפחתית של סוכרת סוג 2</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="מבחן העמסת סוכר (OGTT)",
            body_html=(
                "<p>OGTT הוא תקן הזהב לאבחון <strong>סוכרת הריון</strong> ומשמש גם כשתוצאות הגלוקוז בצום או ה-HbA1c גבוליות.</p>"
                "<div class='blog-definition'><strong>ערכים בשעתיים (75 גרם גלוקוז):</strong><br>"
                "תקין: &lt; 140 mg/dL (7.8 mmol/L)<br>"
                "סבילות לקויה לגלוקוז (טרום-סוכרת): 140–199 mg/dL<br>"
                "סוכרת: ≥ 200 mg/dL (≥ 11.1 mmol/L)</div>"
                "<p>ה-OGTT רגיש יותר מגלוקוז בצום בלבד — הוא יכול לגלות סבילות לקויה לגלוקוז גם כשערכי הצום תקינים לחלוטין.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="גורמי סיכון ותסמינים של סוכר גבוה בדם",
            body_html=(
                "<p><strong>גורמי סיכון:</strong></p>"
                "<ul>"
                "<li>עודף משקל או השמנה (במיוחד שומן בטני)</li>"
                "<li>אורח חיים יושבני</li>"
                "<li>היסטוריה משפחתית של סוכרת</li>"
                "<li>גיל ≥ 45</li>"
                "<li>סוכרת הריון בעבר</li>"
                "<li>תסמונת שחלות פוליציסטיות (PCOS)</li>"
                "<li>לחץ דם גבוה</li>"
                "</ul>"
                "<p><strong>תסמינים של היפרגליקמיה:</strong></p>"
                "<ul>"
                "<li>צמא מוגזם (פולידיפסיה) והשתנה תכופה (פוליאוריה)</li>"
                "<li>ירידה בלתי מוסברת במשקל</li>"
                "<li>עייפות וחולשה</li>"
                "<li>ראייה מטושטשת</li>"
                "<li>ריפוי איטי של פצעים</li>"
                "<li>נימול או חוסר תחושה בידיים וברגליים</li>"
                "</ul>"
                "<div class='blog-example'><strong>אזהרה:</strong> סוכרת סוג 2 יכולה להיות <em>א-תסמינית</em> במשך שנים. בדיקות סקר סדירות חיוניות.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="תזונה ואורח חיים לסוכר בדם בריא",
            body_html=(
                "<p>אסטרטגיות מבוססות מחקר:</p>"
                "<ul>"
                "<li><strong>מזונות בעלי אינדקס גליקמי נמוך:</strong> דגנים מלאים, קטניות, ירקות לא עמילניים.</li>"
                "<li><strong>סיבים תזונתיים:</strong> 25-30 גרם ליום. מקורות: שיבולת שועל, עדשים, זרעי צ'יה, ירקות.</li>"
                "<li><strong>שילוב פחמימות עם חלבון או שומן בריא</strong> להפחתת קפיצות גליקמיות.</li>"
                "<li><strong>פעילות גופנית סדירה:</strong> 150 דקות שבועיות של פעילות מתונה משפרות את הרגישות לאינסולין.</li>"
                "<li><strong>שמירה על משקל בריא:</strong> ירידה של 5-7% ממשקל הגוף יכולה להפחית סיכון לסוכרת עד 58%.</li>"
                "<li><strong>ניהול מתח:</strong> קורטיזול מעלה סוכר בדם. מדיטציה, נשימה עמוקה ו-7-9 שעות שינה עוזרים.</li>"
                "<li><strong>תזונה ים-תיכונית:</strong> עשירה בשמן זית, ירקות, דגים ודגנים מלאים.</li>"
                "</ul>"
                "<div class='blog-example'><strong>טיפ מהיר:</strong> הליכה של 15 דקות אחרי ארוחות יכולה להפחית קפיצות גלוקוז ב-20-30%.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="כיצד NoryaAI מנתח את תוצאות הסוכר שלך",
            body_html=(
                "<p>NoryaAI קורא את דוח הדם המלא שלך — בין אם PDF או תמונה — ובאופן אוטומטי:</p>"
                "<ul>"
                "<li>מזהה גלוקוז בצום, HbA1c, אינסולין, HOMA-IR וערכי OGTT</li>"
                "<li>מסווג תוצאות לטווחים תקין, טרום-סוכרת או סוכרת</li>"
                "<li>מזהה תנגודת לאינסולין גם כשהגלוקוז תקין</li>"
                "<li>מספק הסברים ברורים לכל סמן</li>"
                "<li>מפיק סיכום מוכן לרופא עם מעקב מגמות</li>"
                "</ul>"
                "<p>העלה את דוח המעבדה שלך וקבל ניתוח סוכר בדם תוך דקות.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Hindi
# ---------------------------------------------------------------------------

def _bs_sections_hi() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="रक्त शर्करा परीक्षण क्या मापते हैं?",
            body_html=(
                "<p>रक्त शर्करा (ब्लड ग्लूकोज़) परीक्षण आपके रक्तप्रवाह में <strong>ग्लूकोज़</strong> — शरीर के प्रमुख ऊर्जा स्रोत — की मात्रा मापते हैं। "
                "ग्लूकोज़ भोजन से आता है और अग्न्याशय (pancreas) द्वारा उत्पादित हार्मोन <strong>इंसुलिन</strong> द्वारा नियंत्रित होता है।</p>"
                "<p>कई प्रकार के रक्त शर्करा परीक्षण होते हैं:</p>"
                "<ul>"
                "<li><strong>फास्टिंग ब्लड ग्लूकोज़ (FBG)</strong> — 8-12 घंटे के उपवास के बाद मापा जाता है; मानक स्क्रीनिंग परीक्षण।</li>"
                "<li><strong>रैंडम ग्लूकोज़</strong> — किसी भी समय लिया जाता है; आपातकालीन स्थितियों में उपयोगी।</li>"
                "<li><strong>ओरल ग्लूकोज़ टॉलरेंस टेस्ट (OGTT)</strong> — 75 ग्राम ग्लूकोज़ घोल पीने से पहले और 2 घंटे बाद मापा जाता है।</li>"
                "<li><strong>HbA1c (ग्लाइकेटेड हीमोग्लोबिन)</strong> — पिछले 2-3 महीनों की औसत रक्त शर्करा दर्शाता है।</li>"
                "<li><strong>फास्टिंग इंसुलिन और HOMA-IR</strong> — ग्लूकोज़ बढ़ने से पहले ही इंसुलिन प्रतिरोध का आकलन करते हैं।</li>"
                "</ul>"
                "<p>WHO का अनुमान है कि दुनिया भर में <strong>422 मिलियन से अधिक</strong> लोग मधुमेह (diabetes) के साथ जी रहे हैं।</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="फास्टिंग ब्लड ग्लूकोज़: सामान्य, प्रीडायबिटीज़ और डायबिटीज़ रेंज",
            body_html=(
                "<p>फास्टिंग ब्लड ग्लूकोज़ रात भर कम से कम 8 घंटे के उपवास के बाद मापा जाता है।</p>"
                "<div class='blog-definition'><strong>संदर्भ सीमाएँ (शिरापरक प्लाज़्मा):</strong><br>"
                "सामान्य: 70–99 mg/dL (3.9–5.5 mmol/L)<br>"
                "प्रीडायबिटीज़: 100–125 mg/dL (5.6–6.9 mmol/L)<br>"
                "डायबिटीज़: ≥ 126 mg/dL (≥ 7.0 mmol/L) दो अलग-अलग अवसरों पर</div>"
                "<p><strong>हाइपोग्लाइसीमिया</strong> — 70 mg/dL से नीचे — कंपन, पसीना, भ्रम और गंभीर मामलों में चेतना की हानि का कारण बन सकता है।</p>"
                "<p><strong>ऊँचा फास्टिंग ग्लूकोज़</strong> यह दर्शाता है कि शरीर पर्याप्त इंसुलिन नहीं बना रहा या कोशिकाएँ इंसुलिन का ठीक से जवाब नहीं दे रहीं (इंसुलिन प्रतिरोध)।</p>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c: आपकी 3 महीने की रक्त शर्करा औसत",
            body_html=(
                "<p>HbA1c आपकी लाल रक्त कोशिकाओं में ग्लूकोज़ से जुड़े हीमोग्लोबिन का प्रतिशत मापता है। "
                "चूँकि लाल रक्त कोशिकाएँ लगभग 120 दिन जीवित रहती हैं, HbA1c पिछले <strong>2-3 महीनों की औसत रक्त शर्करा</strong> दर्शाता है।</p>"
                "<div class='blog-definition'><strong>संदर्भ सीमाएँ:</strong><br>"
                "सामान्य: &lt; 5.7%<br>"
                "प्रीडायबिटीज़: 5.7–6.4%<br>"
                "डायबिटीज़: ≥ 6.5%</div>"
                "<p><strong>मधुमेह रोगियों के लिए लक्ष्य:</strong></p>"
                "<ul>"
                "<li>सामान्य लक्ष्य: &lt; 7.0% (ADA अनुशंसा)</li>"
                "<li>कठोर लक्ष्य: &lt; 6.5% — बिना जटिलताओं वाले युवा रोगियों के लिए</li>"
                "<li>लचीला लक्ष्य: &lt; 8.0% — वृद्ध रोगियों या हाइपोग्लाइसीमिया जोखिम वालों के लिए</li>"
                "</ul>"
                "<p>HbA1c में हर 1% की कमी माइक्रोवैस्कुलर जटिलताओं के जोखिम को लगभग <strong>35-40%</strong> तक कम करती है।</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="फास्टिंग इंसुलिन और HOMA-IR: इंसुलिन प्रतिरोध की जल्दी पहचान",
            body_html=(
                "<p><strong>इंसुलिन</strong> ग्लूकोज़ को कोशिकाओं में प्रवेश कराता है। जब कोशिकाएँ प्रतिरोधी हो जाती हैं, "
                "अग्न्याशय क्षतिपूर्ति के लिए अधिक इंसुलिन बनाता है — <strong>हाइपरइंसुलिनेमिया</strong>।</p>"
                "<div class='blog-definition'><strong>फास्टिंग इंसुलिन:</strong> इष्टतम: 2–6 µIU/mL · सामान्य: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (फास्टिंग इंसुलिन × फास्टिंग ग्लूकोज़) / 405<br>"
                "सामान्य: &lt; 1.0 · सीमावर्ती: 1.0–2.0 · प्रतिरोध: &gt; 2.0 · महत्वपूर्ण: &gt; 3.0</div>"
                "<p>HOMA-IR मेटाबोलिक विकार को फास्टिंग ग्लूकोज़ या HbA1c असामान्य होने से <strong>वर्षों पहले</strong> पकड़ सकता है।</p>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="ओरल ग्लूकोज़ टॉलरेंस टेस्ट (OGTT)",
            body_html=(
                "<p>OGTT <strong>गर्भकालीन मधुमेह (gestational diabetes)</strong> के निदान का गोल्ड स्टैंडर्ड है।</p>"
                "<div class='blog-definition'><strong>2 घंटे के OGTT मान (75 g ग्लूकोज़):</strong><br>"
                "सामान्य: &lt; 140 mg/dL (7.8 mmol/L)<br>"
                "बिगड़ी ग्लूकोज़ सहनशीलता (प्रीडायबिटीज़): 140–199 mg/dL<br>"
                "डायबिटीज़: ≥ 200 mg/dL (≥ 11.1 mmol/L)</div>"
                "<p>OGTT अकेले फास्टिंग ग्लूकोज़ से अधिक संवेदनशील है — यह फास्टिंग मान सामान्य होने पर भी बिगड़ी ग्लूकोज़ सहनशीलता का पता लगा सकता है।</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="जोखिम कारक और उच्च रक्त शर्करा के लक्षण",
            body_html=(
                "<p><strong>जोखिम कारक:</strong></p>"
                "<ul>"
                "<li>अधिक वजन या मोटापा (विशेषकर पेट की चर्बी)</li>"
                "<li>गतिहीन जीवनशैली</li>"
                "<li>मधुमेह का पारिवारिक इतिहास</li>"
                "<li>उम्र ≥ 45 वर्ष</li>"
                "<li>गर्भकालीन मधुमेह का इतिहास</li>"
                "<li>पॉलीसिस्टिक ओवरी सिंड्रोम (PCOS)</li>"
                "<li>उच्च रक्तचाप</li>"
                "</ul>"
                "<p><strong>हाइपरग्लाइसीमिया के लक्षण:</strong></p>"
                "<ul>"
                "<li>अत्यधिक प्यास (पॉलीडिप्सिया) और बार-बार पेशाब (पॉलीयूरिया)</li>"
                "<li>अस्पष्ट वजन घटना</li>"
                "<li>थकान और कमज़ोरी</li>"
                "<li>धुंधली दृष्टि</li>"
                "<li>धीमी गति से भरने वाले घाव</li>"
                "<li>हाथ-पैरों में झुनझुनी या सुन्नपन</li>"
                "</ul>"
                "<div class='blog-example'><strong>चेतावनी:</strong> टाइप 2 डायबिटीज़ वर्षों तक <em>लक्षणहीन</em> रह सकती है। नियमित जाँच आवश्यक है।</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="स्वस्थ रक्त शर्करा के लिए आहार और जीवनशैली सुझाव",
            body_html=(
                "<p>साक्ष्य-आधारित रणनीतियाँ:</p>"
                "<ul>"
                "<li><strong>कम ग्लाइसेमिक इंडेक्स वाले खाद्य पदार्थ:</strong> साबुत अनाज, दालें, स्टार्च-रहित सब्ज़ियाँ।</li>"
                "<li><strong>फाइबर को प्राथमिकता दें:</strong> 25-30 ग्राम/दिन। स्रोत: ओट्स, दाल, चिया बीज, सब्ज़ियाँ।</li>"
                "<li><strong>कार्बोहाइड्रेट को प्रोटीन या स्वस्थ वसा के साथ मिलाएँ</strong> ताकि ग्लाइसेमिक स्पाइक कम हो।</li>"
                "<li><strong>नियमित व्यायाम:</strong> प्रति सप्ताह 150 मिनट मध्यम व्यायाम इंसुलिन संवेदनशीलता में सुधार करता है।</li>"
                "<li><strong>स्वस्थ वजन बनाए रखें:</strong> शरीर के वजन का केवल 5-7% कम करने से मधुमेह का जोखिम 58% तक घट सकता है।</li>"
                "<li><strong>तनाव प्रबंधन:</strong> कोर्टिसोल रक्त शर्करा बढ़ाता है। ध्यान, गहरी साँस और 7-9 घंटे की नींद मदद करती है।</li>"
                "<li><strong>मेडिटेरेनियन डाइट:</strong> जैतून का तेल, सब्ज़ियाँ, मछली और साबुत अनाज से भरपूर।</li>"
                "</ul>"
                "<div class='blog-example'><strong>त्वरित सुझाव:</strong> भोजन के बाद 15 मिनट की सैर पोस्ट-मील ग्लूकोज़ स्पाइक को 20-30% तक कम कर सकती है।</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="NoryaAI आपके रक्त शर्करा परिणामों का विश्लेषण कैसे करता है",
            body_html=(
                "<p>NoryaAI आपकी पूरी रक्त रिपोर्ट — चाहे PDF हो या फोटो — पढ़ता है और स्वचालित रूप से:</p>"
                "<ul>"
                "<li>फास्टिंग ग्लूकोज़, HbA1c, इंसुलिन, HOMA-IR और OGTT मान पहचानता है</li>"
                "<li>परिणामों को सामान्य, प्रीडायबिटीज़ या डायबिटीज़ श्रेणियों में वर्गीकृत करता है</li>"
                "<li>ग्लूकोज़ सामान्य होने पर भी इंसुलिन प्रतिरोध को चिह्नित करता है</li>"
                "<li>प्रत्येक मार्कर के लिए स्पष्ट व्याख्या प्रदान करता है</li>"
                "<li>ट्रेंड ट्रैकिंग के साथ डॉक्टर-तैयार सारांश तैयार करता है</li>"
                "</ul>"
                "<p>अपनी लैब रिपोर्ट अपलोड करें और मिनटों में अपना रक्त शर्करा विश्लेषण प्राप्त करें।</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Arabic
# ---------------------------------------------------------------------------

def _bs_sections_ar() -> List[Section]:
    return [
        Section(
            id="section-what-is-blood-sugar",
            level=2,
            heading="ماذا تقيس اختبارات سكر الدم؟",
            body_html=(
                "<p>تقيس اختبارات سكر الدم (جلوكوز الدم) كمية <strong>الجلوكوز</strong> — مصدر الطاقة الرئيسي للجسم — في مجرى الدم. "
                "يأتي الجلوكوز من الطعام وينظمه هرمون <strong>الأنسولين</strong> الذي يُنتجه البنكرياس.</p>"
                "<p>توجد عدة أنواع من اختبارات سكر الدم:</p>"
                "<ul>"
                "<li><strong>جلوكوز الصيام (FBG)</strong> — يُقاس بعد صيام 8-12 ساعة؛ اختبار الفحص المعياري.</li>"
                "<li><strong>الجلوكوز العشوائي</strong> — يُؤخذ في أي وقت؛ مفيد في حالات الطوارئ.</li>"
                "<li><strong>اختبار تحمل الجلوكوز الفموي (OGTT)</strong> — يقيس الجلوكوز قبل وبعد ساعتين من شرب محلول 75 غرام جلوكوز.</li>"
                "<li><strong>HbA1c (الهيموغلوبين السكري)</strong> — يعكس متوسط سكر الدم خلال الشهرين إلى الثلاثة الأخيرة.</li>"
                "<li><strong>أنسولين الصيام و HOMA-IR</strong> — يُقيّمان مقاومة الأنسولين حتى قبل ارتفاع الجلوكوز.</li>"
                "</ul>"
                "<p>تُقدّر منظمة الصحة العالمية أن أكثر من <strong>422 مليون شخص</strong> حول العالم يعيشون مع مرض السكري.</p>"
            ),
        ),
        Section(
            id="section-fasting-glucose",
            level=2,
            heading="جلوكوز الصيام: المعدلات الطبيعية وما قبل السكري والسكري",
            body_html=(
                "<p>يُقاس جلوكوز الصيام بعد صيام ليلي لا يقل عن 8 ساعات.</p>"
                "<div class='blog-definition'><strong>النطاقات المرجعية (بلازما وريدية):</strong><br>"
                "طبيعي: 70–99 mg/dL (3.9–5.5 mmol/L)<br>"
                "ما قبل السكري: 100–125 mg/dL (5.6–6.9 mmol/L)<br>"
                "السكري: ≥ 126 mg/dL (≥ 7.0 mmol/L) في قياسين منفصلين</div>"
                "<p><strong>نقص سكر الدم (Hypoglycemia)</strong> — أقل من 70 mg/dL — قد يسبب الرعشة والتعرق والارتباك وفقدان الوعي في الحالات الشديدة.</p>"
                "<p><strong>ارتفاع جلوكوز الصيام</strong> يشير إلى أن الجسم لا ينتج كمية كافية من الأنسولين أو أن الخلايا لا تستجيب بشكل صحيح (مقاومة الأنسولين).</p>"
            ),
        ),
        Section(
            id="section-hba1c",
            level=2,
            heading="HbA1c: متوسط السكر في 3 أشهر",
            body_html=(
                "<p>يقيس HbA1c نسبة الهيموغلوبين المرتبط بالجلوكوز. بما أن خلايا الدم الحمراء تعيش حوالي 120 يوماً، "
                "فإن HbA1c يعكس <strong>متوسط سكر الدم خلال الشهرين إلى الثلاثة الأخيرة</strong>.</p>"
                "<div class='blog-definition'><strong>النطاقات المرجعية:</strong><br>"
                "طبيعي: &lt; 5.7%<br>"
                "ما قبل السكري: 5.7–6.4%<br>"
                "السكري: ≥ 6.5%</div>"
                "<p><strong>أهداف لمرضى السكري:</strong></p>"
                "<ul>"
                "<li>الهدف العام: &lt; 7.0% (توصية ADA)</li>"
                "<li>هدف أكثر صرامة: &lt; 6.5% للمرضى الشباب بدون مضاعفات</li>"
                "<li>هدف أكثر مرونة: &lt; 8.0% لكبار السن أو المعرضين لنقص السكر</li>"
                "</ul>"
                "<p>كل انخفاض بنسبة 1% في HbA1c يقلل خطر المضاعفات الوعائية الدقيقة بنحو <strong>35-40%</strong>.</p>"
            ),
        ),
        Section(
            id="section-insulin-homa-ir",
            level=2,
            heading="أنسولين الصيام و HOMA-IR: الكشف المبكر عن مقاومة الأنسولين",
            body_html=(
                "<p><strong>الأنسولين</strong> يسمح للجلوكوز بدخول الخلايا. عند مقاومة الأنسولين، يُنتج البنكرياس المزيد — <strong>فرط أنسولين الدم</strong>.</p>"
                "<div class='blog-definition'><strong>أنسولين الصيام:</strong> المثالي: 2–6 µIU/mL · الطبيعي: &lt; 25 µIU/mL<br>"
                "<strong>HOMA-IR</strong> = (أنسولين الصيام × جلوكوز الصيام) / 405<br>"
                "طبيعي: &lt; 1.0 · حدّي: 1.0–2.0 · مقاومة: &gt; 2.0 · مقاومة ملحوظة: &gt; 3.0</div>"
                "<p>يمكن لـ HOMA-IR اكتشاف الخلل الأيضي <strong>قبل سنوات</strong> من ارتفاع جلوكوز الصيام أو HbA1c. مفيد بشكل خاص في:</p>"
                "<ul>"
                "<li>متلازمة المبيض متعدد الكيسات (PCOS)</li>"
                "<li>المتلازمة الأيضية</li>"
                "<li>مرض الكبد الدهني غير الكحولي (NAFLD)</li>"
                "<li>تاريخ عائلي لمرض السكري من النوع 2</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ogtt",
            level=2,
            heading="اختبار تحمل الجلوكوز الفموي (OGTT)",
            body_html=(
                "<p>يُعتبر OGTT المعيار الذهبي لتشخيص <strong>سكري الحمل</strong> ويُستخدم أيضاً عندما تكون نتائج جلوكوز الصيام أو HbA1c حدّية.</p>"
                "<div class='blog-definition'><strong>قيم الساعتين (75 غرام جلوكوز):</strong><br>"
                "طبيعي: &lt; 140 mg/dL (7.8 mmol/L)<br>"
                "ضعف تحمل الجلوكوز (ما قبل السكري): 140–199 mg/dL<br>"
                "السكري: ≥ 200 mg/dL (≥ 11.1 mmol/L)</div>"
                "<p>OGTT أكثر حساسية من جلوكوز الصيام وحده — يمكنه اكتشاف ضعف تحمل الجلوكوز حتى مع قيم صيام طبيعية تماماً.</p>"
            ),
        ),
        Section(
            id="section-risk-factors-symptoms",
            level=2,
            heading="عوامل الخطر وأعراض ارتفاع سكر الدم",
            body_html=(
                "<p><strong>عوامل الخطر:</strong></p>"
                "<ul>"
                "<li>زيادة الوزن أو السمنة (خاصة الدهون الحشوية / البطنية)</li>"
                "<li>نمط حياة خامل</li>"
                "<li>تاريخ عائلي لمرض السكري</li>"
                "<li>العمر ≥ 45 سنة</li>"
                "<li>تاريخ سكري الحمل</li>"
                "<li>متلازمة المبيض متعدد الكيسات (PCOS)</li>"
                "<li>ارتفاع ضغط الدم</li>"
                "</ul>"
                "<p><strong>أعراض فرط سكر الدم:</strong></p>"
                "<ul>"
                "<li>العطش المفرط (عُطاش) والتبول المتكرر (بُوال)</li>"
                "<li>فقدان الوزن غير المبرر</li>"
                "<li>التعب والضعف</li>"
                "<li>تشوش الرؤية</li>"
                "<li>بطء التئام الجروح</li>"
                "<li>وخز أو تنميل في اليدين والقدمين</li>"
                "</ul>"
                "<div class='blog-example'><strong>تحذير:</strong> يمكن أن يكون السكري من النوع 2 <em>بدون أعراض</em> لسنوات. الفحص المنتظم ضروري.</div>"
            ),
        ),
        Section(
            id="section-diet-lifestyle",
            level=2,
            heading="نصائح غذائية ونمط حياة لسكر دم صحي",
            body_html=(
                "<p>استراتيجيات مبنية على الأدلة:</p>"
                "<ul>"
                "<li><strong>أطعمة ذات مؤشر غلايسيمي منخفض:</strong> الحبوب الكاملة، البقوليات، الخضروات غير النشوية.</li>"
                "<li><strong>الألياف:</strong> 25-30 غرام/يوم. المصادر: الشوفان، العدس، بذور الشيا، الخضروات.</li>"
                "<li><strong>اقرن الكربوهيدرات بالبروتين أو الدهون الصحية</strong> لتقليل ارتفاعات السكر.</li>"
                "<li><strong>النشاط البدني المنتظم:</strong> 150 دقيقة أسبوعياً من التمارين المعتدلة تحسن حساسية الأنسولين.</li>"
                "<li><strong>الحفاظ على وزن صحي:</strong> فقدان 5-7% فقط من وزن الجسم يمكن أن يقلل خطر السكري بنسبة تصل إلى 58%.</li>"
                "<li><strong>إدارة التوتر:</strong> الكورتيزول يرفع سكر الدم. التأمل والتنفس العميق و7-9 ساعات نوم تساعد.</li>"
                "<li><strong>حمية البحر الأبيض المتوسط:</strong> غنية بزيت الزيتون والخضروات والأسماك والحبوب الكاملة.</li>"
                "</ul>"
                "<div class='blog-example'><strong>نصيحة سريعة:</strong> المشي 15 دقيقة بعد الوجبات يمكن أن يقلل ارتفاعات الجلوكوز بعد الأكل بنسبة 20-30%.</div>"
            ),
        ),
        Section(
            id="section-norya-blood-sugar",
            level=2,
            heading="كيف يحلل NoryaAI نتائج سكر الدم لديك",
            body_html=(
                "<p>يقرأ NoryaAI تقرير الدم الكامل — سواء كان PDF أو صورة — ويقوم تلقائياً بـ:</p>"
                "<ul>"
                "<li>تحديد جلوكوز الصيام وHbA1c والأنسولين وHOMA-IR وقيم OGTT</li>"
                "<li>تصنيف النتائج في نطاقات طبيعية أو ما قبل السكري أو السكري</li>"
                "<li>الكشف عن مقاومة الأنسولين حتى مع جلوكوز طبيعي</li>"
                "<li>توفير شروحات واضحة لكل مؤشر</li>"
                "<li>إنشاء ملخص جاهز للطبيب مع تتبع الاتجاهات</li>"
                "</ul>"
                "<p>ارفع تقرير مختبرك واحصل على تحليل سكر الدم خلال دقائق.</p>"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------

def build_blood_sugar_article() -> Article:
    """Build the Blood Sugar Pillar Article. Called from blog_i18n.py."""
    return Article(
        id="blood-sugar-levels-guide",
        published_at=date(2026, 3, 25),
        read_minutes=14,
        cover_image="/static/images/blog/hba1c-hero.jpg",
        category={
            "en": "Blood Sugar",
            "tr": "Kan Şekeri",
            "de": "Blutzucker",
            "es": "Glucosa",
            "fr": "Glycémie",
            "it": "Glicemia",
            "he": "סוכר בדם",
            "hi": "रक्त शर्करा",
            "ar": "سكر الدم",
        },
        slugs=slugs,
        titles={
            "en": "Understanding Blood Sugar: Glucose, HbA1c & Insulin Resistance Guide",
            "tr": "Kan Şekeri Rehberi: Glukoz, HbA1c ve İnsülin Direnci",
            "de": "Blutzuckerwerte verstehen: Glukose, HbA1c & Insulinresistenz",
            "es": "Guía de niveles de azúcar en sangre: Glucosa, HbA1c y resistencia a la insulina",
            "fr": "Comprendre la glycémie : Glucose, HbA1c et résistance à l'insuline",
            "it": "Guida alla glicemia: Glucosio, HbA1c e resistenza all'insulina",
            "he": "מדריך רמות סוכר בדם: גלוקוז, HbA1c ותנגודת לאינסולין",
            "hi": "रक्त शर्करा स्तर गाइड: ग्लूकोज़, HbA1c और इंसुलिन प्रतिरोध",
            "ar": "دليل مستويات السكر في الدم: الجلوكوز، HbA1c ومقاومة الأنسولين",
        },
        subtitles={
            "en": "Everything you need to know about fasting glucose, HbA1c, insulin resistance (HOMA-IR), and glucose tolerance tests — with normal ranges and practical advice.",
            "tr": "Açlık glukozu, HbA1c, insülin direnci (HOMA-IR) ve glukoz tolerans testleri hakkında bilmeniz gereken her şey — normal aralıklar ve pratik önerilerle.",
            "de": "Alles über Nüchternglukose, HbA1c, Insulinresistenz (HOMA-IR) und Glukosetoleranztests — mit Normwerten und praktischen Tipps.",
            "es": "Todo lo que necesita saber sobre glucosa en ayunas, HbA1c, resistencia a la insulina (HOMA-IR) y pruebas de tolerancia a la glucosa.",
            "fr": "Tout ce que vous devez savoir sur la glycémie à jeun, l'HbA1c, la résistance à l'insuline (HOMA-IR) et les tests de tolérance au glucose.",
            "it": "Tutto quello che c'è da sapere su glicemia a digiuno, HbA1c, resistenza insulinica (HOMA-IR) e test di tolleranza al glucosio.",
            "he": "כל מה שצריך לדעת על גלוקוז בצום, HbA1c, תנגודת לאינסולין (HOMA-IR) ומבחני סבילות לגלוקוז — עם טווחים תקינים ועצות מעשיות.",
            "hi": "फास्टिंग ग्लूकोज़, HbA1c, इंसुलिन प्रतिरोध (HOMA-IR) और ग्लूकोज़ सहनशीलता परीक्षणों के बारे में सब कुछ — सामान्य सीमाओं और व्यावहारिक सलाह के साथ।",
            "ar": "كل ما تحتاج معرفته عن جلوكوز الصيام، HbA1c، مقاومة الأنسولين (HOMA-IR)، واختبارات تحمل الجلوكوز — مع النطاقات الطبيعية ونصائح عملية.",
        },
        excerpts={
            "en": "A comprehensive guide to understanding blood sugar tests: fasting glucose, HbA1c, insulin, HOMA-IR, and OGTT explained with ranges and lifestyle tips.",
            "tr": "Kan şekeri testlerini anlamak için kapsamlı rehber: açlık glukozu, HbA1c, insülin, HOMA-IR ve OGTT — aralıklar ve yaşam tarzı önerileriyle.",
            "de": "Ein umfassender Leitfaden zu Blutzuckertests: Nüchternglukose, HbA1c, Insulin, HOMA-IR und oGTT mit Normwerten und Lebensstil-Tipps.",
            "es": "Guía completa de pruebas de azúcar en sangre: glucosa en ayunas, HbA1c, insulina, HOMA-IR y PTOG con rangos y consejos de estilo de vida.",
            "fr": "Guide complet des tests de glycémie : glycémie à jeun, HbA1c, insuline, HOMA-IR et HGPO avec valeurs normales et conseils pratiques.",
            "it": "Guida completa agli esami della glicemia: glicemia a digiuno, HbA1c, insulina, HOMA-IR e OGTT con valori normali e consigli pratici.",
            "he": "מדריך מקיף לבדיקות סוכר בדם: גלוקוז בצום, HbA1c, אינסולין, HOMA-IR ו-OGTT עם טווחים תקינים וטיפים לאורח חיים.",
            "hi": "रक्त शर्करा परीक्षणों को समझने की व्यापक गाइड: फास्टिंग ग्लूकोज़, HbA1c, इंसुलिन, HOMA-IR और OGTT।",
            "ar": "دليل شامل لفهم اختبارات سكر الدم: جلوكوز الصيام، HbA1c، الأنسولين، HOMA-IR وOGTT مع النطاقات ونصائح نمط الحياة.",
        },
        seo_titles={
            "en": "Blood Sugar Levels Guide: Glucose, HbA1c & Insulin Resistance 2026 | NoryaAI",
            "tr": "Kan Şekeri Rehberi: Glukoz, HbA1c ve İnsülin Direnci 2026 | NoryaAI",
            "de": "Blutzuckerwerte Leitfaden: Glukose, HbA1c & Insulinresistenz 2026 | NoryaAI",
            "es": "Guía niveles de azúcar: Glucosa, HbA1c y resistencia a la insulina 2026 | NoryaAI",
            "fr": "Guide glycémie : Glucose, HbA1c et résistance à l'insuline 2026 | NoryaAI",
            "it": "Guida glicemia: Glucosio, HbA1c e resistenza all'insulina 2026 | NoryaAI",
            "he": "מדריך סוכר בדם: גלוקוז, HbA1c ותנגודת לאינסולין 2026 | NoryaAI",
            "hi": "रक्त शर्करा गाइड: ग्लूकोज़, HbA1c और इंसुलिन प्रतिरोध 2026 | NoryaAI",
            "ar": "دليل مستويات السكر: الجلوكوز، HbA1c ومقاومة الأنسولين 2026 | NoryaAI",
        },
        seo_descriptions={
            "en": "Understand fasting glucose, HbA1c, insulin resistance (HOMA-IR), and OGTT. Learn normal ranges, prediabetes vs diabetes thresholds, and lifestyle tips for healthy blood sugar.",
            "tr": "Açlık glukozu, HbA1c, insülin direnci (HOMA-IR) ve OGTT'yi anlayın. Normal aralıklar, prediyabet-diyabet eşikleri ve sağlıklı kan şekeri için yaşam tarzı önerileri.",
            "de": "Verstehen Sie Nüchternglukose, HbA1c, Insulinresistenz (HOMA-IR) und oGTT. Normwerte, Prädiabetes- vs. Diabetes-Schwellen und Tipps für gesunde Blutzuckerwerte.",
            "es": "Comprenda la glucosa en ayunas, HbA1c, resistencia a la insulina (HOMA-IR) y PTOG. Rangos normales, umbrales de prediabetes vs diabetes y consejos de estilo de vida.",
            "fr": "Comprenez la glycémie à jeun, l'HbA1c, la résistance à l'insuline (HOMA-IR) et l'HGPO. Valeurs normales, seuils prédiabète vs diabète et conseils pratiques.",
            "it": "Comprendi la glicemia a digiuno, HbA1c, resistenza insulinica (HOMA-IR) e OGTT. Valori normali, soglie prediabete vs diabete e consigli sullo stile di vita.",
            "he": "הבינו גלוקוז בצום, HbA1c, תנגודת לאינסולין (HOMA-IR) ו-OGTT. טווחים תקינים, סיפי טרום-סוכרת לעומת סוכרת וטיפים לאורח חיים בריא.",
            "hi": "फास्टिंग ग्लूकोज़, HbA1c, इंसुलिन प्रतिरोध (HOMA-IR) और OGTT को समझें। सामान्य सीमाएँ, प्रीडायबिटीज़ बनाम डायबिटीज़ और स्वस्थ रक्त शर्करा के सुझाव।",
            "ar": "افهم جلوكوز الصيام، HbA1c، مقاومة الأنسولين (HOMA-IR) وOGTT. النطاقات الطبيعية وعتبات ما قبل السكري مقابل السكري ونصائح نمط الحياة.",
        },
        sections_by_lang={
            "en": _bs_sections_en(),
            "tr": _bs_sections_tr(),
            "de": _bs_sections_de(),
            "es": _bs_sections_es(),
            "fr": _bs_sections_fr(),
            "it": _bs_sections_it(),
            "he": _bs_sections_he(),
            "hi": _bs_sections_hi(),
            "ar": _bs_sections_ar(),
        },
        last_updated=date(2026, 3, 25),
        faq_schema_qa={
            "en": [
                {"question": "What is a normal fasting blood sugar level?", "answer": "A normal fasting blood glucose level is 70-99 mg/dL (3.9-5.5 mmol/L). Values of 100-125 mg/dL indicate prediabetes, and 126 mg/dL or higher on two occasions indicates diabetes."},
                {"question": "What does HbA1c measure?", "answer": "HbA1c measures the percentage of hemoglobin with glucose attached, reflecting your average blood sugar over the past 2-3 months. Normal is below 5.7%, prediabetes is 5.7-6.4%, and diabetes is 6.5% or higher."},
                {"question": "What is HOMA-IR and why is it important?", "answer": "HOMA-IR (Homeostatic Model Assessment of Insulin Resistance) is calculated from fasting insulin and glucose. It detects insulin resistance years before glucose levels become abnormal, making it valuable for early intervention."},
                {"question": "What are the symptoms of high blood sugar?", "answer": "Symptoms include excessive thirst, frequent urination, unexplained weight loss, fatigue, blurred vision, slow-healing wounds, and tingling in hands and feet. However, type 2 diabetes can be asymptomatic for years."},
            ],
            "tr": [
                {"question": "Normal açlık kan şekeri seviyesi nedir?", "answer": "Normal açlık kan şekeri 70-99 mg/dL (3,9-5,5 mmol/L) arasıdır. 100-125 mg/dL prediyabeti, iki ayrı ölçümde 126 mg/dL ve üzeri diyabeti gösterir."},
                {"question": "HbA1c neyi ölçer?", "answer": "HbA1c, glukoz bağlanmış hemoglobin yüzdesini ölçerek son 2-3 aylık ortalama kan şekerinizi yansıtır. Normal %5,7 altı, prediyabet %5,7-6,4, diyabet %6,5 ve üzeridir."},
                {"question": "HOMA-IR nedir ve neden önemlidir?", "answer": "HOMA-IR, açlık insülini ve glukozundan hesaplanır. Glukoz seviyeleri anormalleşmeden yıllar önce insülin direncini tespit eder, bu da erken müdahale için değerlidir."},
                {"question": "Yüksek kan şekerinin belirtileri nelerdir?", "answer": "Belirtiler arasında aşırı susama, sık idrara çıkma, açıklanamayan kilo kaybı, yorgunluk, bulanık görme, yavaş iyileşen yaralar ve el-ayaklarda karıncalanma yer alır."},
            ],
            "de": [
                {"question": "Was ist ein normaler Nüchternblutzucker?", "answer": "Ein normaler Nüchternblutzucker liegt bei 70-99 mg/dL (3,9-5,5 mmol/L). Werte von 100-125 mg/dL deuten auf Prädiabetes hin, ab 126 mg/dL bei zwei Messungen auf Diabetes."},
                {"question": "Was misst der HbA1c-Wert?", "answer": "HbA1c misst den Anteil des mit Glukose verbundenen Hämoglobins und spiegelt den durchschnittlichen Blutzucker der letzten 2-3 Monate wider. Normal ist unter 5,7 %, Prädiabetes 5,7-6,4 %, Diabetes ab 6,5 %."},
                {"question": "Was ist HOMA-IR?", "answer": "HOMA-IR wird aus Nüchterninsulin und -glukose berechnet und erkennt Insulinresistenz Jahre bevor Glukosewerte ansteigen — wertvoll für die Früherkennung."},
                {"question": "Welche Symptome hat ein erhöhter Blutzucker?", "answer": "Symptome sind übermäßiger Durst, häufiges Wasserlassen, Gewichtsverlust, Müdigkeit, verschwommenes Sehen und schlecht heilende Wunden. Typ-2-Diabetes kann jahrelang symptomlos verlaufen."},
            ],
            "es": [
                {"question": "¿Cuál es el nivel normal de glucosa en ayunas?", "answer": "La glucosa en ayunas normal es 70-99 mg/dL. Valores de 100-125 mg/dL indican prediabetes y 126 mg/dL o más en dos ocasiones indica diabetes."},
                {"question": "¿Qué mide la HbA1c?", "answer": "La HbA1c mide el porcentaje de hemoglobina unida a glucosa, reflejando su glucemia promedio de los últimos 2-3 meses. Normal es menos de 5,7 %, prediabetes 5,7-6,4 %, diabetes 6,5 % o más."},
                {"question": "¿Qué es el HOMA-IR?", "answer": "El HOMA-IR se calcula a partir de la insulina y glucosa en ayunas. Detecta resistencia a la insulina años antes de que la glucosa se altere."},
                {"question": "¿Cuáles son los síntomas de la hiperglucemia?", "answer": "Los síntomas incluyen sed excesiva, micción frecuente, pérdida de peso, fatiga, visión borrosa y heridas que cicatrizan lentamente. La diabetes tipo 2 puede ser asintomática durante años."},
            ],
            "fr": [
                {"question": "Quel est le taux normal de glycémie à jeun ?", "answer": "La glycémie à jeun normale est de 70-99 mg/dL. Des valeurs de 100-125 mg/dL indiquent un prédiabète, et 126 mg/dL ou plus lors de deux mesures indique un diabète."},
                {"question": "Que mesure l'HbA1c ?", "answer": "L'HbA1c mesure le pourcentage d'hémoglobine liée au glucose, reflétant votre glycémie moyenne des 2-3 derniers mois. Normal : moins de 5,7 %, prédiabète : 5,7-6,4 %, diabète : 6,5 % ou plus."},
                {"question": "Qu'est-ce que le HOMA-IR ?", "answer": "Le HOMA-IR est calculé à partir de l'insuline et du glucose à jeun. Il détecte la résistance à l'insuline des années avant que la glycémie ne s'élève."},
                {"question": "Quels sont les symptômes de l'hyperglycémie ?", "answer": "Les symptômes comprennent une soif excessive, des mictions fréquentes, une perte de poids, de la fatigue, une vision floue et une cicatrisation lente. Le diabète de type 2 peut rester asymptomatique pendant des années."},
            ],
            "it": [
                {"question": "Qual è il livello normale di glicemia a digiuno?", "answer": "La glicemia a digiuno normale è 70-99 mg/dL. Valori di 100-125 mg/dL indicano prediabete, 126 mg/dL o più in due misurazioni indica diabete."},
                {"question": "Cosa misura l'HbA1c?", "answer": "L'HbA1c misura la percentuale di emoglobina legata al glucosio, riflettendo la glicemia media degli ultimi 2-3 mesi. Normale: sotto 5,7 %, prediabete: 5,7-6,4 %, diabete: 6,5 % o più."},
                {"question": "Cos'è il HOMA-IR?", "answer": "Il HOMA-IR si calcola da insulina e glicemia a digiuno. Rileva la resistenza insulinica anni prima che la glicemia diventi anomala."},
                {"question": "Quali sono i sintomi dell'iperglicemia?", "answer": "I sintomi includono sete eccessiva, minzione frequente, perdita di peso, stanchezza, visione offuscata e ferite che guariscono lentamente. Il diabete di tipo 2 può essere asintomatico per anni."},
            ],
            "he": [
                {"question": "מהי רמת סוכר תקינה בצום?", "answer": "רמת גלוקוז בצום תקינה היא 70-99 mg/dL. ערכים של 100-125 mg/dL מעידים על טרום-סוכרת, ו-126 mg/dL ומעלה בשני מדידות מעידים על סוכרת."},
                {"question": "מה מודד HbA1c?", "answer": "HbA1c מודד את אחוז ההמוגלובין הקשור לגלוקוז ומשקף את ממוצע הסוכר בדם ב-2-3 החודשים האחרונים. תקין: מתחת ל-5.7%, טרום-סוכרת: 5.7-6.4%, סוכרת: 6.5% ומעלה."},
                {"question": "מהו HOMA-IR ולמה הוא חשוב?", "answer": "HOMA-IR מחושב מאינסולין וגלוקוז בצום. הוא מגלה תנגודת לאינסולין שנים לפני שרמות הגלוקוז הופכות חריגות."},
                {"question": "מהם תסמיני סוכר גבוה בדם?", "answer": "התסמינים כוללים צמא מוגזם, השתנה תכופה, ירידה במשקל, עייפות, ראייה מטושטשת וריפוי איטי של פצעים. סוכרת סוג 2 יכולה להיות א-תסמינית במשך שנים."},
            ],
            "hi": [
                {"question": "सामान्य फास्टिंग ब्लड शुगर स्तर क्या है?", "answer": "सामान्य फास्टिंग ब्लड ग्लूकोज़ 70-99 mg/dL है। 100-125 mg/dL प्रीडायबिटीज़ दर्शाता है, और दो अवसरों पर 126 mg/dL या अधिक डायबिटीज़ दर्शाता है।"},
                {"question": "HbA1c क्या मापता है?", "answer": "HbA1c ग्लूकोज़ से जुड़े हीमोग्लोबिन का प्रतिशत मापता है, जो पिछले 2-3 महीनों की औसत रक्त शर्करा दर्शाता है। सामान्य: 5.7% से कम, प्रीडायबिटीज़: 5.7-6.4%, डायबिटीज़: 6.5% या अधिक।"},
                {"question": "HOMA-IR क्या है और यह महत्वपूर्ण क्यों है?", "answer": "HOMA-IR फास्टिंग इंसुलिन और ग्लूकोज़ से गणना किया जाता है। यह ग्लूकोज़ स्तर असामान्य होने से वर्षों पहले इंसुलिन प्रतिरोध का पता लगाता है।"},
                {"question": "उच्च रक्त शर्करा के लक्षण क्या हैं?", "answer": "लक्षणों में अत्यधिक प्यास, बार-बार पेशाब, अस्पष्ट वजन घटना, थकान, धुंधली दृष्टि और धीमे भरने वाले घाव शामिल हैं। टाइप 2 डायबिटीज़ वर्षों तक लक्षणहीन हो सकती है।"},
            ],
            "ar": [
                {"question": "ما هو المستوى الطبيعي لسكر الدم الصائم؟", "answer": "جلوكوز الصيام الطبيعي هو 70-99 mg/dL. قيم 100-125 mg/dL تشير إلى ما قبل السكري، و126 mg/dL أو أعلى في قياسين تشير إلى السكري."},
                {"question": "ماذا يقيس HbA1c؟", "answer": "يقيس HbA1c نسبة الهيموغلوبين المرتبط بالجلوكوز، ويعكس متوسط سكر الدم خلال 2-3 أشهر الأخيرة. طبيعي: أقل من 5.7%، ما قبل السكري: 5.7-6.4%، السكري: 6.5% أو أعلى."},
                {"question": "ما هو HOMA-IR ولماذا هو مهم؟", "answer": "يُحسب HOMA-IR من أنسولين وجلوكوز الصيام. يكشف مقاومة الأنسولين قبل سنوات من ارتفاع مستويات الجلوكوز."},
                {"question": "ما أعراض ارتفاع سكر الدم؟", "answer": "تشمل الأعراض العطش المفرط والتبول المتكرر وفقدان الوزن والتعب وتشوش الرؤية وبطء التئام الجروح. يمكن أن يكون السكري من النوع 2 بدون أعراض لسنوات."},
            ],
        },
    )
