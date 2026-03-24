"""Pillar blog article: Complete Blood Count (CBC) Explained — comprehensive guide.

Registered in blog_i18n.py as a pillar content piece for SEO.
"""
from datetime import date
from typing import Dict, List

# Reuse the same Section/Article types from blog_i18n
# (imported and registered there; this file only provides the builder)


def _cbc_sections_en():
    from app.blog_i18n import Section
    return [
        Section(id="section-what-is-cbc", level=2, heading="What Is a Complete Blood Count (CBC)?",
                body_html="<p>A Complete Blood Count (CBC) is one of the most commonly ordered blood tests worldwide. It measures the major components of your blood: <strong>red blood cells</strong> (RBCs), <strong>white blood cells</strong> (WBCs), <strong>platelets</strong>, <strong>hemoglobin</strong>, and <strong>hematocrit</strong>. Doctors use it as a general screening tool to evaluate your overall health, detect infections, diagnose anemia, and monitor existing conditions.</p><p>Understanding your CBC results can feel overwhelming — there are typically 15-20 values on a single report. This guide breaks down each component so you can walk into your next doctor's appointment prepared and informed.</p>"),
        Section(id="section-rbc", level=2, heading="Red Blood Cells (RBC)",
                body_html="<p>Red blood cells carry oxygen from your lungs to every cell in your body and transport carbon dioxide back. The RBC count measures how many red blood cells are in a microliter of blood.</p><div class='blog-definition'><strong>Normal ranges:</strong> Male: 4.7–6.1 million/µL · Female: 4.2–5.4 million/µL</div><p><strong>High RBC</strong> (polycythemia) can be caused by dehydration, smoking, living at high altitude, or bone marrow disorders. <strong>Low RBC</strong> (anemia) may indicate iron deficiency, vitamin B12 deficiency, chronic disease, or blood loss.</p>"),
        Section(id="section-hemoglobin", level=2, heading="Hemoglobin (Hb / Hgb)",
                body_html="<p>Hemoglobin is the iron-containing protein inside red blood cells that actually binds and carries oxygen. It's one of the most important markers in your CBC.</p><div class='blog-definition'><strong>Normal ranges:</strong> Male: 14–18 g/dL · Female: 12–16 g/dL</div><p><strong>Low hemoglobin</strong> is the hallmark of anemia. Symptoms include fatigue, weakness, shortness of breath, and pale skin. <strong>High hemoglobin</strong> can occur with dehydration, chronic lung disease, or polycythemia vera.</p>"),
        Section(id="section-hematocrit", level=2, heading="Hematocrit (Hct)",
                body_html="<p>Hematocrit measures the percentage of your blood volume that is occupied by red blood cells. It's closely related to hemoglobin and RBC count.</p><div class='blog-definition'><strong>Normal ranges:</strong> Male: 40–54% · Female: 36–48%</div><p>High hematocrit can indicate dehydration or polycythemia. Low hematocrit usually accompanies anemia and has similar causes to low hemoglobin.</p>"),
        Section(id="section-mcv-mch-mchc", level=2, heading="RBC Indices: MCV, MCH, MCHC",
                body_html="<p>These indices describe the <em>characteristics</em> of your red blood cells and help classify the type of anemia:</p><ul><li><strong>MCV (Mean Corpuscular Volume)</strong>: Average size of your red blood cells. Normal: 80–100 fL. Low MCV (microcytic) = iron deficiency; High MCV (macrocytic) = B12/folate deficiency.</li><li><strong>MCH (Mean Corpuscular Hemoglobin)</strong>: Average amount of hemoglobin per RBC. Normal: 27–33 pg.</li><li><strong>MCHC (Mean Corpuscular Hemoglobin Concentration)</strong>: Average concentration of hemoglobin in each RBC. Normal: 32–36 g/dL.</li></ul><div class='blog-example'><strong>Example:</strong> If your MCV is 72 fL (low) and MCH is 24 pg (low), this pattern suggests <em>iron deficiency anemia</em> — the most common type worldwide.</div>"),
        Section(id="section-rdw", level=2, heading="RDW (Red Cell Distribution Width)",
                body_html="<p>RDW measures how much variation there is in the size of your red blood cells. Normal range is typically 11.5–14.5%.</p><p>A <strong>high RDW</strong> means your red blood cells vary significantly in size (anisocytosis), which can indicate iron deficiency, vitamin deficiency, or mixed anemias. RDW is especially useful when combined with MCV to classify anemias.</p>"),
        Section(id="section-wbc", level=2, heading="White Blood Cells (WBC)",
                body_html="<p>White blood cells are your immune system's soldiers. The total WBC count tells you how active your immune system is.</p><div class='blog-definition'><strong>Normal range:</strong> 4,500–11,000 cells/µL</div><p><strong>High WBC</strong> (leukocytosis) often indicates infection, inflammation, stress, allergic reactions, or in rare cases, leukemia. <strong>Low WBC</strong> (leukopenia) can be caused by viral infections, autoimmune diseases, bone marrow problems, or certain medications.</p>"),
        Section(id="section-differential", level=2, heading="WBC Differential: Types of White Blood Cells",
                body_html="<p>The differential breaks down WBCs into five types, each with a specific role:</p><ul><li><strong>Neutrophils (40–70%)</strong>: First responders to bacterial infections. High = bacterial infection; Low = risk of infection.</li><li><strong>Lymphocytes (20–40%)</strong>: Fight viral infections and produce antibodies. High = viral infection, chronic inflammation; Low = HIV, immunodeficiency.</li><li><strong>Monocytes (2–8%)</strong>: Clean up dead cells and fight chronic infections. High = chronic inflammation, autoimmune disease.</li><li><strong>Eosinophils (1–4%)</strong>: Fight parasites and involved in allergic reactions. High = allergies, asthma, parasitic infections.</li><li><strong>Basophils (0–1%)</strong>: Involved in allergic and inflammatory responses. Rarely elevated on their own.</li></ul>"),
        Section(id="section-platelets", level=2, heading="Platelets (PLT)",
                body_html="<p>Platelets are tiny cell fragments essential for blood clotting. They rush to the site of a wound and form a plug to stop bleeding.</p><div class='blog-definition'><strong>Normal range:</strong> 150,000–400,000/µL</div><p><strong>Low platelets</strong> (thrombocytopenia) can cause easy bruising, prolonged bleeding, and petechiae (tiny red spots). Causes include viral infections, medications, autoimmune disorders, and liver disease. <strong>High platelets</strong> (thrombocytosis) can be reactive (infection, iron deficiency) or indicate a bone marrow disorder.</p>"),
        Section(id="section-mpv", level=2, heading="MPV (Mean Platelet Volume)",
                body_html="<p>MPV measures the average size of your platelets. Normal range is typically 7.5–11.5 fL.</p><p>A <strong>high MPV</strong> with low platelet count suggests your bone marrow is producing young, large platelets to compensate for destruction (as in ITP). A <strong>low MPV</strong> may indicate bone marrow suppression.</p>"),
        Section(id="section-when-to-worry", level=2, heading="When Should You Worry?",
                body_html="<p>Most CBC abnormalities are mild and temporary. However, you should consult your doctor promptly if:</p><ul><li>Hemoglobin is below 10 g/dL (moderate anemia)</li><li>WBC is above 20,000 or below 2,000</li><li>Platelets are below 50,000 (bleeding risk)</li><li>Multiple values are significantly abnormal</li><li>Abnormalities persist across multiple tests</li></ul><div class='blog-example'><strong>Pro tip:</strong> A single abnormal value often means nothing in isolation. Trends over time and the combination of values matter more than any single number.</div>"),
        Section(id="section-norya-cbc", level=2, heading="How NoryaAI Helps With Your CBC",
                body_html="<p>NoryaAI reads your complete CBC report — whether it's a PDF from your lab or a photo — and automatically:</p><ul><li>Identifies all 15-20+ CBC markers</li><li>Compares each value to age and sex-specific reference ranges</li><li>Flags abnormal values with clear explanations</li><li>Generates a structured, doctor-ready summary</li><li>Provides a health score based on your overall results</li></ul><p>No manual data entry needed. Upload your report and get your analysis in minutes.</p>"),
    ]


def _cbc_sections_tr():
    from app.blog_i18n import Section
    return [
        Section(id="section-what-is-cbc", level=2, heading="Tam Kan Sayımı (CBC) Nedir?",
                body_html="<p>Tam Kan Sayımı (CBC veya hemogram), dünya çapında en sık istenen kan testlerinden biridir. Kanınızdaki temel bileşenleri ölçer: <strong>kırmızı kan hücreleri</strong> (RBC), <strong>beyaz kan hücreleri</strong> (WBC), <strong>trombositler</strong>, <strong>hemoglobin</strong> ve <strong>hematokrit</strong>. Doktorlar bunu genel sağlık taraması, enfeksiyon tespiti, anemi tanısı ve mevcut durumların takibi için kullanır.</p><p>CBC sonuçlarını anlamak zorlu olabilir — tek bir raporda genellikle 15-20 değer bulunur. Bu rehber her bir bileşeni açıklar, böylece bir sonraki doktor randevunuza hazırlıklı gidebilirsiniz.</p>"),
        Section(id="section-rbc", level=2, heading="Kırmızı Kan Hücreleri (RBC / Eritrosit)",
                body_html="<p>Kırmızı kan hücreleri, akciğerlerinizden vücudunuzun her hücresine oksijen taşır ve karbondioksiti geri getirir.</p><div class='blog-definition'><strong>Normal aralıklar:</strong> Erkek: 4,7–6,1 milyon/µL · Kadın: 4,2–5,4 milyon/µL</div><p><strong>Yüksek RBC</strong> (polisitemi) dehidrasyon, sigara, yüksek rakımda yaşama veya kemik iliği bozukluklarından kaynaklanabilir. <strong>Düşük RBC</strong> (anemi) demir eksikliği, B12 eksikliği, kronik hastalık veya kan kaybına işaret edebilir.</p>"),
        Section(id="section-hemoglobin", level=2, heading="Hemoglobin (Hb / Hgb)",
                body_html="<p>Hemoglobin, kırmızı kan hücrelerinin içindeki, oksijeni bağlayıp taşıyan demir içerikli proteindir. CBC'nizdeki en önemli belirteçlerden biridir.</p><div class='blog-definition'><strong>Normal aralıklar:</strong> Erkek: 14–18 g/dL · Kadın: 12–16 g/dL</div><p><strong>Düşük hemoglobin</strong> aneminin başlıca göstergesidir. Belirtileri yorgunluk, halsizlik, nefes darlığı ve soluk cilt olabilir. <strong>Yüksek hemoglobin</strong> dehidrasyon, kronik akciğer hastalığı veya polisitemi vera ile görülebilir.</p>"),
        Section(id="section-hematocrit", level=2, heading="Hematokrit (Hct)",
                body_html="<p>Hematokrit, kan hacminizin yüzde kaçının kırmızı kan hücreleri tarafından oluşturulduğunu ölçer.</p><div class='blog-definition'><strong>Normal aralıklar:</strong> Erkek: %40–54 · Kadın: %36–48</div><p>Yüksek hematokrit dehidrasyon veya polisitemiye işaret edebilir. Düşük hematokrit genellikle anemiyle birlikte görülür.</p>"),
        Section(id="section-mcv-mch-mchc", level=2, heading="RBC İndeksleri: MCV, MCH, MCHC",
                body_html="<p>Bu indeksler kırmızı kan hücrelerinizin <em>özelliklerini</em> tanımlar ve anemi tipini sınıflandırmaya yardımcı olur:</p><ul><li><strong>MCV (Ortalama Eritrosit Hacmi)</strong>: Kırmızı kan hücrelerinin ortalama boyutu. Normal: 80–100 fL. Düşük MCV (mikrositik) = demir eksikliği; Yüksek MCV (makrositik) = B12/folat eksikliği.</li><li><strong>MCH (Ortalama Eritrosit Hemoglobini)</strong>: Her RBC'deki ortalama hemoglobin miktarı. Normal: 27–33 pg.</li><li><strong>MCHC (Ortalama Eritrosit Hemoglobin Konsantrasyonu)</strong>: Her RBC'deki ortalama hemoglobin yoğunluğu. Normal: 32–36 g/dL.</li></ul>"),
        Section(id="section-wbc", level=2, heading="Beyaz Kan Hücreleri (WBC / Lökosit)",
                body_html="<p>Beyaz kan hücreleri bağışıklık sisteminizin savaşçılarıdır. Toplam WBC sayısı bağışıklık sisteminizin ne kadar aktif olduğunu gösterir.</p><div class='blog-definition'><strong>Normal aralık:</strong> 4.500–11.000 hücre/µL</div><p><strong>Yüksek WBC</strong> (lökositoz) genellikle enfeksiyon, inflamasyon, stres veya alerjik reaksiyonlara işaret eder. <strong>Düşük WBC</strong> (lökopeni) viral enfeksiyonlar, otoimmün hastalıklar veya bazı ilaçlardan kaynaklanabilir.</p>"),
        Section(id="section-differential", level=2, heading="WBC Diferansiyeli: Beyaz Kan Hücresi Tipleri",
                body_html="<p>Diferansiyel, WBC'leri her biri belirli bir göreve sahip beş tipe ayırır:</p><ul><li><strong>Nötrofiller (%40–70)</strong>: Bakteriyel enfeksiyonlara ilk müdahale edenler.</li><li><strong>Lenfositler (%20–40)</strong>: Viral enfeksiyonlarla savaşır ve antikor üretir.</li><li><strong>Monositler (%2–8)</strong>: Ölü hücreleri temizler ve kronik enfeksiyonlarla mücadele eder.</li><li><strong>Eozinofiller (%1–4)</strong>: Parazitlerle savaşır ve alerjik reaksiyonlarda rol oynar.</li><li><strong>Bazofiller (%0–1)</strong>: Alerjik ve inflamatuar yanıtlarda görev alır.</li></ul>"),
        Section(id="section-platelets", level=2, heading="Trombositler (PLT)",
                body_html="<p>Trombositler, kan pıhtılaşması için gerekli küçük hücre parçacıklarıdır.</p><div class='blog-definition'><strong>Normal aralık:</strong> 150.000–400.000/µL</div><p><strong>Düşük trombosit</strong> (trombositopeni) kolay morarma, uzun süreli kanama ve peteşiye (küçük kırmızı noktalar) neden olabilir. <strong>Yüksek trombosit</strong> (trombositoz) reaktif olabilir veya kemik iliği bozukluğuna işaret edebilir.</p>"),
        Section(id="section-norya-cbc", level=2, heading="NoryaAI Tam Kan Sayımınızda Nasıl Yardımcı Olur?",
                body_html="<p>NoryaAI, CBC raporunuzun tamamını — ister laboratuvarınızdan bir PDF ister fotoğraf olsun — okur ve otomatik olarak:</p><ul><li>15-20+ CBC belirtecinin tamamını tanımlar</li><li>Her değeri yaş ve cinsiyete özel referans aralıklarıyla karşılaştırır</li><li>Anormal değerleri net açıklamalarla işaretler</li><li>Yapılandırılmış, doktora hazır bir özet oluşturur</li><li>Genel sonuçlarınıza dayalı bir sağlık skoru sağlar</li></ul><p>Manuel veri girişi gerekmez. Raporunuzu yükleyin ve dakikalar içinde analizinizi alın.</p>"),
    ]


def build_cbc_article():
    """Build the CBC Pillar Article. Called from blog_i18n.py."""
    from app.blog_i18n import Article, Section
    return Article(
        id="cbc-complete-guide",
        published_at=date(2026, 3, 24),
        read_minutes=15,
        cover_image="/static/images/blog/hematocrit-hero.jpg",
        category={"en": "Blood Tests", "tr": "Kan Testleri"},
        slugs={"en": "complete-blood-count-cbc-guide", "tr": "tam-kan-sayimi-rehberi"},
        titles={
            "en": "Complete Blood Count (CBC) Explained: The Ultimate Guide",
            "tr": "Tam Kan Sayımı (Hemogram) Rehberi: Tüm Değerler Açıklandı",
        },
        subtitles={
            "en": "Everything you need to know about your CBC results — RBC, WBC, hemoglobin, platelets, and more — explained in plain language.",
            "tr": "CBC sonuçlarınız hakkında bilmeniz gereken her şey — RBC, WBC, hemoglobin, trombositler ve daha fazlası — anlaşılır dilde.",
        },
        excerpts={
            "en": "A comprehensive guide to understanding your Complete Blood Count (CBC) results, from red blood cells to platelets.",
            "tr": "Tam Kan Sayımı (CBC) sonuçlarınızı anlamak için kapsamlı bir rehber.",
        },
        seo_titles={
            "en": "Complete Blood Count (CBC) Explained — Ultimate Guide 2026 | NoryaAI",
            "tr": "Tam Kan Sayımı (Hemogram) Rehberi — Tüm Değerler 2026 | NoryaAI",
        },
        seo_descriptions={
            "en": "Understand every value in your CBC report. Learn about RBC, WBC, hemoglobin, hematocrit, MCV, MCH, platelets, and more with normal ranges and explanations.",
            "tr": "CBC raporunuzdaki her değeri anlayın. RBC, WBC, hemoglobin, hematokrit, MCV, MCH, trombositler ve daha fazlası hakkında normal aralıklar ve açıklamalar.",
        },
        sections_by_lang={
            "en": _cbc_sections_en(),
            "tr": _cbc_sections_tr(),
        },
        last_updated=date(2026, 3, 24),
        faq_schema_qa={
            "en": [
                {"question": "What does CBC stand for?", "answer": "CBC stands for Complete Blood Count. It measures red blood cells, white blood cells, hemoglobin, hematocrit, and platelets in your blood."},
                {"question": "What is a normal CBC result?", "answer": "Normal CBC values vary by age and sex. Generally: Hemoglobin 12-18 g/dL, WBC 4,500-11,000/µL, Platelets 150,000-400,000/µL, Hematocrit 36-54%."},
                {"question": "When should I worry about my CBC results?", "answer": "Consult your doctor if hemoglobin is below 10 g/dL, WBC is above 20,000 or below 2,000, platelets are below 50,000, or if multiple values are significantly abnormal."},
                {"question": "How often should I get a CBC?", "answer": "For healthy adults, a CBC is typically recommended annually as part of a routine check-up. Your doctor may order it more frequently if you have certain health conditions."},
            ],
            "tr": [
                {"question": "CBC (hemogram) ne anlama gelir?", "answer": "CBC, Tam Kan Sayımı anlamına gelir. Kanınızdaki kırmızı kan hücreleri, beyaz kan hücreleri, hemoglobin, hematokrit ve trombositleri ölçer."},
                {"question": "Normal CBC sonuçları nelerdir?", "answer": "Normal CBC değerleri yaş ve cinsiyete göre değişir. Genel olarak: Hemoglobin 12-18 g/dL, WBC 4.500-11.000/µL, Trombositler 150.000-400.000/µL."},
                {"question": "CBC sonuçlarım ne zaman endişe verici?", "answer": "Hemoglobin 10 g/dL'nin altındaysa, WBC 20.000'in üstünde veya 2.000'in altındaysa, trombositler 50.000'in altındaysa doktorunuza başvurun."},
            ],
        },
    )
