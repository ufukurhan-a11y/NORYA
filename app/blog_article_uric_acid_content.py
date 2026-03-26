# -*- coding: utf-8 -*-
"""
Uric acid blog article — full body content for all 9 languages.
Used by blog_i18n._article_uric_acid().
Sections: intro, what-is-uric-acid, normal-ranges, high-uric-acid-causes,
gout-connection, kidney-stones, uric-acid-and-diet, medications,
when-to-see-doctor, how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# ENGLISH
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="High uric acid: what your blood test result means",
            body_html=(
                "<p><strong>Uric acid</strong> is a natural waste product formed when the body breaks down <em>purines</em>&mdash;substances found "
                "in certain foods and also produced by the body during normal cell turnover. Under healthy conditions, uric acid dissolves in the blood, "
                "passes through the kidneys, and is excreted in urine. However, when the body produces too much uric acid or the kidneys cannot "
                "excrete enough, blood levels rise&mdash;a condition called <strong>hyperuricemia</strong>.</p>"
                "<p>Elevated uric acid is best known for causing <strong>gout</strong>, a painful form of inflammatory arthritis, but it is also "
                "linked to kidney stones, chronic kidney disease, hypertension, and cardiovascular risk. Conversely, very low uric acid levels are "
                "uncommon but can occur in certain liver or kidney disorders. Understanding your uric acid level helps you and your doctor assess "
                "metabolic health and take preventive measures.</p>"
                "<p>This guide is educational and does not replace medical advice. Always discuss your lab results with a qualified healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="What is uric acid and how is it produced?",
            body_html=(
                "<p>Purines are nitrogen-containing compounds found in every cell in the body and in many foods. When cells die and their DNA is "
                "recycled, or when you eat purine-rich foods, the purines are metabolized by the enzyme <strong>xanthine oxidase</strong> into "
                "uric acid. In most mammals, uric acid is further broken down into a more soluble compound called allantoin by the enzyme uricase, "
                "but humans lack this enzyme due to a mutation that occurred millions of years ago. As a result, uric acid is the final breakdown "
                "product of purine metabolism in humans and must be excreted by the kidneys and, to a lesser extent, the gut.</p>"
                "<p>Approximately two-thirds of uric acid is eliminated by the kidneys, while the remaining one-third is excreted via the "
                "gastrointestinal tract. The kidneys filter uric acid from the blood, reabsorb most of it in the proximal tubule, and then "
                "secrete a portion back into the tubular fluid for excretion. This complex handling means that kidney function has a profound "
                "impact on uric acid levels. Transporters such as <strong>URAT1</strong> and <strong>GLUT9</strong> play key roles and are targets "
                "for some uric-acid-lowering medications.</p>"
                "<p>Interestingly, uric acid also functions as an <strong>antioxidant</strong> in the blood, accounting for roughly half of the "
                "antioxidant capacity of plasma. Some researchers believe this antioxidant role may explain why the uricase gene was lost during "
                "human evolution&mdash;higher uric acid levels may have conferred a survival advantage. However, the benefits are limited, and "
                "chronically elevated levels clearly cause harm.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal uric acid ranges",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal range (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal range (&micro;mol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Men</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 &ndash; 7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 &ndash; 6.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr>'
                "</tbody></table>"
                "<p>Women generally have lower uric acid levels than men because estrogen promotes uric acid excretion by the kidneys. After "
                "menopause, women's uric acid levels tend to rise and approach those of men. Children typically have lower levels than adults.</p>"
                "<p>The solubility limit of uric acid in body fluids at normal body temperature is approximately <strong>6.8&nbsp;mg/dL</strong>. "
                "Above this concentration, monosodium urate crystals can form in joints and tissues, potentially leading to gout. For patients "
                "with gout, treatment guidelines recommend a target uric acid level below 6.0&nbsp;mg/dL to dissolve existing crystals and "
                "prevent future attacks.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Causes of high uric acid (hyperuricemia)",
            body_html=(
                "<p>Hyperuricemia results from either <strong>overproduction</strong> of uric acid, <strong>underexcretion</strong> by the kidneys, "
                "or a combination of both. Underexcretion accounts for about 90% of cases:</p>"
                "<p><strong>Dietary and lifestyle factors:</strong></p>"
                "<ul>"
                "<li><strong>Purine-rich diet</strong> &ndash; organ meats (liver, kidney, sweetbreads), red meat, shellfish (shrimp, lobster, mussels), "
                "and certain fish (anchovies, sardines, herring) are high in purines.</li>"
                "<li><strong>Alcohol</strong> &ndash; beer is particularly problematic because it contains guanosine, a purine. Alcohol also increases "
                "uric acid production while reducing renal excretion. Spirits and wine have a smaller but still significant effect.</li>"
                "<li><strong>Fructose and sugar-sweetened beverages</strong> &ndash; fructose metabolism generates purines as a byproduct, directly "
                "increasing uric acid production. High-fructose corn syrup is a major contributor.</li>"
                "<li><strong>Obesity</strong> &ndash; excess body fat increases purine production and reduces renal uric acid clearance.</li>"
                "</ul>"
                "<p><strong>Medical conditions:</strong></p>"
                "<ul>"
                "<li><strong>Chronic kidney disease</strong> &ndash; impaired kidney function reduces uric acid excretion. "
                "For more on kidney markers, see our guide on <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR</a>.</li>"
                "<li><strong>Metabolic syndrome and insulin resistance</strong> &ndash; insulin reduces renal uric acid clearance.</li>"
                "<li><strong>Myeloproliferative and lymphoproliferative disorders</strong> &ndash; conditions with rapid cell turnover (leukemia, lymphoma, "
                "psoriasis) produce excess purines.</li>"
                "<li><strong>Hypothyroidism, lead toxicity, and pre-eclampsia</strong> can also elevate uric acid.</li>"
                "</ul>"
                "<p><strong>Medications:</strong> Thiazide and loop diuretics, low-dose aspirin, cyclosporine, pyrazinamide, and ethambutol "
                "reduce renal uric acid excretion. Chemotherapy drugs can cause tumor lysis syndrome with dramatic uric acid spikes.</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="Uric acid and gout",
            body_html=(
                "<p><strong>Gout</strong> is an inflammatory arthritis caused by the deposition of monosodium urate (MSU) crystals in joints and "
                "surrounding tissues. It is the most common inflammatory arthritis in men and increasingly prevalent worldwide, partly due to rising "
                "rates of obesity, metabolic syndrome, and dietary changes.</p>"
                "<p>The classic gout attack presents as sudden, excruciating pain, swelling, redness, and warmth in a single joint&mdash;most "
                "commonly the base of the big toe (<em>podagra</em>). Attacks often begin at night and peak within 12&ndash;24 hours. Without "
                "treatment, an attack typically resolves in 1&ndash;2 weeks but tends to recur and may involve more joints over time.</p>"
                "<p>Not everyone with hyperuricemia develops gout. Population studies show that only about 20&ndash;25% of people with uric acid "
                "above 9&nbsp;mg/dL develop gout over a 5-year period. However, the risk increases sharply with higher levels and longer duration "
                "of hyperuricemia. Chronic untreated gout can lead to <strong>tophi</strong> (hard deposits of urate crystals under the skin), "
                "joint erosion, and permanent joint damage.</p>"
                "<p>Management of gout involves treating acute flares with NSAIDs, colchicine, or corticosteroids, and long-term urate-lowering "
                "therapy (usually allopurinol or febuxostat) for patients with recurrent attacks or complications.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Uric acid and kidney stones",
            body_html=(
                "<p>Uric acid kidney stones account for approximately <strong>10% of all kidney stones</strong> in developed countries and up to "
                "40% in some Middle Eastern and Mediterranean populations. They form when urine is persistently <strong>acidic (low pH)</strong>, "
                "concentrated, and contains excess uric acid.</p>"
                "<p>Unlike calcium-based kidney stones, uric acid stones are <strong>radiolucent</strong>&mdash;they do not show up on standard "
                "X-rays and require CT scan or ultrasound for detection. Risk factors include chronic diarrhea (which causes bicarbonate loss and "
                "acidic urine), type 2 diabetes (associated with low urine pH), obesity, high-purine diets, and dehydration.</p>"
                "<p>Prevention of uric acid stones focuses on <strong>urinary alkalinization</strong> (raising urine pH to 6.0&ndash;6.5 with "
                "potassium citrate), adequate hydration (at least 2&ndash;2.5 liters of fluid daily), dietary purine restriction, and, when "
                "necessary, allopurinol to reduce uric acid production. Unlike calcium stones, uric acid stones can often be <strong>dissolved</strong> "
                "with medical therapy alone, avoiding the need for surgical intervention.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Dietary recommendations for managing uric acid",
            body_html=(
                "<p>Diet plays a meaningful role in uric acid management, though it typically accounts for only about a 1&ndash;2&nbsp;mg/dL change "
                "in serum uric acid. Nevertheless, dietary modifications are an important complement to medication when needed:</p>"
                "<p><strong>Foods to limit or avoid:</strong></p>"
                "<ul>"
                "<li><strong>Organ meats</strong> &ndash; liver, kidney, sweetbreads are extremely high in purines.</li>"
                "<li><strong>Certain seafood</strong> &ndash; anchovies, sardines, herring, mussels, scallops, and shrimp.</li>"
                "<li><strong>Red meat</strong> &ndash; beef, lamb, and pork in large quantities.</li>"
                "<li><strong>Alcohol</strong> &ndash; especially beer and spirits.</li>"
                "<li><strong>Sugar-sweetened beverages and high-fructose foods</strong> &ndash; sodas, fruit juices, candy.</li>"
                "</ul>"
                "<p><strong>Foods that may help:</strong></p>"
                "<ul>"
                "<li><strong>Low-fat dairy products</strong> &ndash; milk and yogurt have been shown to lower uric acid levels.</li>"
                "<li><strong>Cherries and cherry extract</strong> &ndash; several studies suggest they reduce gout flare frequency.</li>"
                "<li><strong>Coffee</strong> &ndash; regular coffee consumption is associated with lower uric acid levels.</li>"
                "<li><strong>Vitamin C</strong> &ndash; modest uricosuric effect at doses of 500&nbsp;mg/day or more.</li>"
                "<li><strong>Plenty of water</strong> &ndash; adequate hydration helps the kidneys excrete uric acid.</li>"
                "</ul>"
                "<p>Vegetable purines (from spinach, mushrooms, asparagus) do not appear to increase gout risk and need not be restricted. "
                "A balanced diet emphasizing whole grains, vegetables, fruits, and lean proteins is recommended.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medications for high uric acid",
            body_html=(
                "<p>Medications to lower uric acid are primarily used in patients with gout, uric acid kidney stones, or very high uric acid levels. "
                "They fall into two main categories:</p>"
                "<p><strong>Xanthine oxidase inhibitors (reduce production):</strong></p>"
                "<ul>"
                "<li><strong>Allopurinol</strong> &ndash; the most widely used urate-lowering drug. Started at a low dose and titrated to achieve "
                "a target serum uric acid below 6.0&nbsp;mg/dL. Generally well tolerated; rare but serious hypersensitivity reactions are associated "
                "with the HLA-B*5801 allele, which should be tested in high-risk populations (Southeast Asian, African American).</li>"
                "<li><strong>Febuxostat</strong> &ndash; a selective xanthine oxidase inhibitor alternative for patients who cannot tolerate allopurinol. "
                "More potent but carries a cardiovascular safety warning.</li>"
                "</ul>"
                "<p><strong>Uricosuric agents (increase excretion):</strong></p>"
                "<ul>"
                "<li><strong>Probenecid</strong> &ndash; increases renal uric acid excretion. Requires adequate kidney function and hydration; "
                "contraindicated in patients with a history of uric acid kidney stones.</li>"
                "<li><strong>Lesinurad</strong> &ndash; a newer URAT1 inhibitor used in combination with a xanthine oxidase inhibitor.</li>"
                "</ul>"
                "<p>When initiating urate-lowering therapy, gout flares can paradoxically increase during the first months as crystal deposits dissolve. "
                "Prophylactic colchicine or low-dose NSAIDs are often prescribed during this transition period. Treatment is typically lifelong.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult your doctor about your uric acid levels in the following situations:</p>"
                "<ul>"
                "<li>Your uric acid is <strong>above 7.0&nbsp;mg/dL (men) or 6.0&nbsp;mg/dL (women)</strong> on repeated testing.</li>"
                "<li>You have symptoms of <strong>gout</strong>: sudden, severe joint pain with swelling, redness, and warmth, especially in the big toe.</li>"
                "<li>You have a history of <strong>kidney stones</strong>, especially if they are uric acid stones.</li>"
                "<li>You are taking medications known to raise uric acid (diuretics, low-dose aspirin).</li>"
                "<li>You have <strong>chronic kidney disease</strong> with elevated uric acid, which may accelerate kidney damage.</li>"
                "<li>You notice <strong>tophi</strong>&mdash;firm, chalky nodules under the skin near joints or on the ears.</li>"
                "</ul>"
                "<p>Asymptomatic hyperuricemia (elevated uric acid without gout or stones) is common and does not always require treatment. "
                "However, it warrants lifestyle modifications and monitoring, especially when accompanied by other metabolic risk factors "
                "such as obesity, diabetes, or hypertension.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your uric acid results",
            body_html=(
                "<p>Interpreting uric acid in the context of your complete blood panel can be complex. <strong>Norya</strong> makes it simple: "
                "upload your blood test results and receive a clear, structured health summary within minutes. Norya evaluates your uric acid "
                "alongside kidney function markers, glucose, lipids, and inflammation indicators to give you a comprehensive metabolic picture.</p>"
                "<p>The report flags abnormal values, explains their significance in everyday language, and prepares you with the right questions "
                "for your doctor visit. <a href=\"/analyze\">Start your free analysis with Norya</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace medical advice or diagnosis.</strong> '
                'Always discuss your results with a healthcare professional. <a href="/analyze">Start analysis with Norya</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# TURKISH
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Yüksek ürik asit: kan testi sonucunuz ne anlama geliyor?",
            body_html=(
                "<p><strong>Ürik asit</strong>, vücudun <em>pürinleri</em>&mdash;belirli besinlerde bulunan ve normal hücre döngüsü sırasında "
                "vücut tarafından da üretilen maddeler&mdash;parçalamasıyla oluşan doğal bir atık üründür. Sağlıklı koşullarda ürik asit kanda "
                "çözülür, böbreklerden geçer ve idrarla atılır. Ancak vücut çok fazla ürik asit ürettiğinde veya böbrekler yeterince atamadığında "
                "kan düzeyleri yükselir&mdash;bu duruma <strong>hiperürisemi</strong> denir.</p>"
                "<p>Yüksek ürik asit en çok <strong>gut</strong> (damla hastalığı)&mdash;ağrılı bir iltihaplı artrit formu&mdash;ile bilinir, "
                "ancak böbrek taşları, kronik böbrek hastalığı, hipertansiyon ve kardiyovasküler riskle de bağlantılıdır.</p>"
                "<p>Bu rehber eğitim amaçlıdır, tıbbi tavsiye yerine geçmez. Sonuçlarınızı mutlaka doktorunuzla tartışın.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="Ürik asit nedir ve nasıl üretilir?",
            body_html=(
                "<p>Pürinler vücuttaki her hücrede ve birçok besinde bulunan azot içeren bileşiklerdir. Hücreler öldüğünde ve DNA'ları geri "
                "dönüştürüldüğünde veya pürinden zengin besinler yediğinizde, pürinler <strong>ksantin oksidaz</strong> enzimi tarafından "
                "ürik aside metabolize edilir. Çoğu memelide ürik asit, ürikaz enzimi tarafından daha çözünür bir bileşik olan allantoine dönüştürülür "
                "ancak insanlar milyonlarca yıl önce meydana gelen bir mutasyon nedeniyle bu enzimden yoksundur.</p>"
                "<p>Ürik asidin yaklaşık üçte ikisi böbrekler tarafından, kalan üçte biri gastrointestinal yoldan atılır. Böbrekler ürik asidi kandan "
                "filtreler, çoğunu proksimal tübülde geri emer ve bir kısmını atılmak üzere tübüler sıvıya geri salgılar. <strong>URAT1</strong> "
                "ve <strong>GLUT9</strong> gibi taşıyıcılar kilit roller oynar.</p>"
                "<p>İlginç bir şekilde, ürik asit kanda bir <strong>antioksidan</strong> olarak da işlev görür ve plazmanın antioksidan kapasitesinin "
                "yaklaşık yarısını oluşturur. Ancak kronik olarak yüksek düzeyler açıkça zarar verir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal ürik asit aralıkları",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal aralık (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal aralık (&micro;mol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkekler</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 &ndash; 7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadınlar</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 &ndash; 6,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr>'
                "</tbody></table>"
                "<p>Kadınlarda östrojen böbreklerden ürik asit atılımını desteklediği için genellikle daha düşük düzeyler görülür. "
                "Menopoz sonrası kadınlardaki ürik asit düzeyleri yükselir ve erkeklerinkine yaklaşır.</p>"
                "<p>Ürik asidin vücut sıvılarındaki çözünürlük sınırı yaklaşık <strong>6,8&nbsp;mg/dL</strong>'dir. Bu konsantrasyonun üzerinde "
                "monosodyum ürat kristalleri eklemlerde ve dokularda oluşabilir. Gut hastalarında tedavi hedefi 6,0&nbsp;mg/dL'nin altıdır.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Yüksek ürik asit (hiperürisemi) nedenleri",
            body_html=(
                "<p>Hiperürisemi, ürik asidin <strong>aşırı üretimi</strong>, böbreklerden <strong>yetersiz atılımı</strong> veya her ikisinin "
                "kombinasyonundan kaynaklanır. Vakaların yaklaşık %90'ından yetersiz atılım sorumludur:</p>"
                "<p><strong>Diyet ve yaşam tarzı faktörleri:</strong></p>"
                "<ul>"
                "<li><strong>Pürinden zengin diyet</strong> &ndash; sakatat (karaciğer, böbrek), kırmızı et, kabuklu deniz ürünleri (karides, midye).</li>"
                "<li><strong>Alkol</strong> &ndash; özellikle bira, guanozin içerdiği için sorunludur. Alkol ayrıca ürik asit üretimini artırır.</li>"
                "<li><strong>Fruktoz ve şekerli içecekler</strong> &ndash; fruktoz metabolizması yan ürün olarak pürin üretir.</li>"
                "<li><strong>Obezite</strong> &ndash; fazla vücut yağı pürin üretimini artırır ve renal klirensı azaltır.</li>"
                "</ul>"
                "<p><strong>Tıbbi durumlar:</strong> Kronik böbrek hastalığı (böbrek belirteçleri hakkında daha fazla bilgi için "
                "<a href=\"/tr/blog/creatinine-egfr-what-it-means\">kreatinin ve eGFR rehberimize</a> bakın), metabolik sendrom, "
                "miyeloproliferatif hastalıklar, hipotiroidizm.</p>"
                "<p><strong>İlaçlar:</strong> Tiazid ve loop diüretikler, düşük doz aspirin, siklosporin, pirazinamid.</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="Ürik asit ve gut hastalığı",
            body_html=(
                "<p><strong>Gut</strong>, monosodyum ürat (MSU) kristallerinin eklemlere ve çevre dokulara birikmesiyle oluşan iltihaplı bir artrittir. "
                "Erkeklerde en sık görülen iltihaplı artrit türüdür ve obezite, metabolik sendrom ve diyet değişiklikleri nedeniyle dünya genelinde "
                "giderek artan bir prevalansa sahiptir.</p>"
                "<p>Klasik gut atağı, genellikle ayak başparmağı tabanında (<em>podagra</em>) ani, dayanılmaz ağrı, şişlik, kızarıklık ve sıcaklık "
                "olarak ortaya çıkar. Ataklar genellikle gece başlar ve 12&ndash;24 saat içinde zirveye ulaşır.</p>"
                "<p>Hiperürisemisi olan herkes gut geliştirmez. Ancak risk daha yüksek düzeylerde ve daha uzun süreli hiperürisemide belirgin "
                "şekilde artar. Kronik tedavi edilmemiş gut, <strong>tofüs</strong> (deri altında sert ürat birikintileri), eklem erozyonu ve "
                "kalıcı eklem hasarına yol açabilir.</p>"
                "<p>Gut yönetimi; akut alevlenmelerin NSAİİ, kolşisin veya kortikosteroidlerle tedavisini ve tekrarlayan ataklarda uzun süreli "
                "ürat düşürücü tedaviyi (genellikle allopürinol veya febuksostat) içerir.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Ürik asit ve böbrek taşları",
            body_html=(
                "<p>Ürik asit böbrek taşları, gelişmiş ülkelerde tüm böbrek taşlarının yaklaşık <strong>%10'unu</strong> oluşturur. İdrar sürekli "
                "<strong>asidik (düşük pH)</strong>, konsantre olduğunda ve aşırı ürik asit içerdiğinde oluşurlar.</p>"
                "<p>Kalsiyum bazlı taşlardan farklı olarak ürik asit taşları <strong>radyolüsenttir</strong>&mdash;standart röntgenlerde görünmezler "
                "ve BT taraması veya ultrason gerektirir. Risk faktörleri arasında kronik ishal, tip 2 diyabet, obezite, yüksek pürinli diyetler "
                "ve dehidratasyon yer alır.</p>"
                "<p>Ürik asit taşlarının önlenmesi <strong>idrar alkalizasyonu</strong> (potasyum sitratla idrar pH'ını 6,0&ndash;6,5'e yükseltme), "
                "yeterli hidrasyon (günde en az 2&ndash;2,5 litre sıvı), diyet pürin kısıtlaması ve gerektiğinde allopürinol ile ürik asit "
                "üretimini azaltmaya odaklanır. Kalsiyum taşlarından farklı olarak ürik asit taşları genellikle yalnızca tıbbi tedaviyle "
                "<strong>eritilebilir</strong>.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Ürik asit yönetimi için diyet önerileri",
            body_html=(
                "<p>Diyet, ürik asit yönetiminde anlamlı bir rol oynar ancak genellikle serum ürik asidinde yalnızca 1&ndash;2&nbsp;mg/dL'lik "
                "bir değişikliğe karşılık gelir. Yine de diyet değişiklikleri gerektiğinde ilaca önemli bir tamamlayıcıdır:</p>"
                "<p><strong>Sınırlanması veya kaçınılması gereken besinler:</strong></p>"
                "<ul>"
                "<li><strong>Sakatat</strong> &ndash; karaciğer, böbrek, uykuluk bezi son derece yüksek pürin içerir.</li>"
                "<li><strong>Bazı deniz ürünleri</strong> &ndash; hamsi, sardalya, ringa, midye, karides.</li>"
                "<li><strong>Kırmızı et</strong> &ndash; büyük miktarlarda sığır, kuzu ve domuz eti.</li>"
                "<li><strong>Alkol</strong> &ndash; özellikle bira ve distile içkiler.</li>"
                "<li><strong>Şekerli içecekler</strong> &ndash; gazlı içecekler, meyve suları.</li>"
                "</ul>"
                "<p><strong>Yardımcı olabilecek besinler:</strong></p>"
                "<ul>"
                "<li><strong>Az yağlı süt ürünleri</strong> &ndash; süt ve yoğurdun ürik asit düzeylerini düşürdüğü gösterilmiştir.</li>"
                "<li><strong>Kiraz ve kiraz özütü</strong> &ndash; gut alevlenmelerini azalttığı gösterilmiştir.</li>"
                "<li><strong>Kahve</strong> &ndash; düzenli kahve tüketimi daha düşük ürik asit düzeyleriyle ilişkilidir.</li>"
                "<li><strong>C vitamini</strong> &ndash; 500&nbsp;mg/gün veya üzerinde mütevazı ürikozürik etki.</li>"
                "<li><strong>Bol su</strong> &ndash; yeterli hidrasyon böbreklerin ürik asit atmasına yardımcı olur.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Yüksek ürik asit için ilaçlar",
            body_html=(
                "<p>Ürik asit düşürücü ilaçlar ağırlıklı olarak gut, ürik asit böbrek taşları veya çok yüksek ürik asit düzeyleri olan hastalarda kullanılır:</p>"
                "<p><strong>Ksantin oksidaz inhibitörleri (üretimi azaltır):</strong></p>"
                "<ul>"
                "<li><strong>Allopürinol</strong> &ndash; en yaygın kullanılan ürat düşürücü ilaçtır. Düşük dozda başlanır ve serum ürik asit "
                "hedefi 6,0&nbsp;mg/dL altına düşene kadar titre edilir.</li>"
                "<li><strong>Febuksostat</strong> &ndash; allopürinolü tolere edemeyen hastalar için selektif bir alternatiftir.</li>"
                "</ul>"
                "<p><strong>Ürikozürik ajanlar (atılımı artırır):</strong></p>"
                "<ul>"
                "<li><strong>Probenesid</strong> &ndash; renal ürik asit atılımını artırır. Yeterli böbrek fonksiyonu gerektirir.</li>"
                "<li><strong>Lesinurad</strong> &ndash; ksantin oksidaz inhibitörü ile kombinasyonda kullanılan yeni bir URAT1 inhibitörüdür.</li>"
                "</ul>"
                "<p>Ürat düşürücü tedavi başlatıldığında kristal birikintileri çözüldükçe ilk aylarda paradoksal olarak gut alevlenmeleri artabilir. "
                "Bu geçiş döneminde profilaktik kolşisin veya düşük doz NSAİİ reçete edilir. Tedavi genellikle ömür boyudur.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda ürik asit düzeyleriniz hakkında doktorunuza danışın:</p>"
                "<ul>"
                "<li>Ürik asidiniz tekrarlanan testlerde <strong>erkeklerde 7,0&nbsp;mg/dL, kadınlarda 6,0&nbsp;mg/dL'nin üzerinde</strong>.</li>"
                "<li><strong>Gut</strong> belirtileriniz var: özellikle ayak başparmağında ani, şiddetli eklem ağrısı, şişlik ve kızarıklık.</li>"
                "<li><strong>Böbrek taşı</strong> öykünüz var.</li>"
                "<li>Ürik asidi yükselten ilaçlar (diüretikler, düşük doz aspirin) kullanıyorsunuz.</li>"
                "<li>Yüksek ürik asitli <strong>kronik böbrek hastalığınız</strong> var.</li>"
                "<li><strong>Tofüs</strong>&mdash;eklemler yakınında veya kulaklarda deri altında sert, tebeşirimsi nodüller&mdash;fark ediyorsunuz.</li>"
                "</ul>"
                "<p>Asemptomatik hiperürisemi (gut veya taş olmadan yüksek ürik asit) yaygındır ve her zaman tedavi gerektirmez. Ancak yaşam "
                "tarzı değişiklikleri ve takip gerektirir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya ürik asit sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Ürik asidi tam kan paneliniz bağlamında yorumlamak karmaşık olabilir. <strong>Norya</strong> bunu basitleştirir: "
                "kan testi sonuçlarınızı yükleyin ve dakikalar içinde net, yapılandırılmış bir sağlık özeti alın. Norya, ürik asidinizi "
                "böbrek fonksiyon belirteçleri, glikoz, lipidler ve iltihap göstergeleriyle birlikte değerlendirir.</p>"
                "<p>Rapor anormal değerleri işaretler, anlaşılır dilde açıklar ve doktor ziyaretiniz için doğru soruları hazırlamanıza "
                "yardımcı olur. <a href=\"/analyze\">Norya ile ücretsiz analizinizi başlatın</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                'Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. <a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# SPANISH
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Ácido úrico alto: qué significa su resultado de análisis de sangre",
                body_html="<p>El <strong>ácido úrico</strong> es un producto de desecho natural que se forma cuando el cuerpo descompone las <em>purinas</em>, sustancias presentes en ciertos alimentos y producidas durante el recambio celular. En condiciones normales, el ácido úrico se disuelve en la sangre, pasa por los riñones y se excreta en la orina. Cuando el cuerpo produce demasiado o los riñones no excretan suficiente, los niveles se elevan: <strong>hiperuricemia</strong>.</p><p>El ácido úrico elevado es conocido por causar <strong>gota</strong>, una forma dolorosa de artritis inflamatoria, pero también está vinculado a cálculos renales, enfermedad renal crónica e hipertensión. Esta guía es educativa y no sustituye el consejo médico.</p>"),
        Section(id="what-is-uric-acid", level=2, heading="¿Qué es el ácido úrico y cómo se produce?",
                body_html="<p>Las purinas son compuestos nitrogenados presentes en cada célula y en muchos alimentos. Cuando las células mueren o se consumen alimentos ricos en purinas, estas se metabolizan por la enzima <strong>xantina oxidasa</strong> en ácido úrico. Los humanos carecen de la enzima uricasa, por lo que el ácido úrico es el producto final del metabolismo de purinas.</p><p>Aproximadamente dos tercios del ácido úrico se eliminan por los riñones y el tercio restante por el tracto gastrointestinal. Los transportadores <strong>URAT1</strong> y <strong>GLUT9</strong> son clave en este proceso y diana de algunos medicamentos.</p><p>El ácido úrico también funciona como <strong>antioxidante</strong> en la sangre, representando cerca de la mitad de la capacidad antioxidante del plasma.</p>"),
        Section(id="normal-ranges", level=2, heading="Rangos normales de ácido úrico",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal (mg/dL)</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal (&micro;mol/L)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 &ndash; 7,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 &ndash; 6,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr></tbody></table><p>Las mujeres generalmente tienen niveles más bajos porque los estrógenos promueven la excreción renal de ácido úrico. Después de la menopausia, los niveles tienden a igualarse. El límite de solubilidad es aproximadamente <strong>6,8&nbsp;mg/dL</strong>; por encima pueden formarse cristales de urato.</p>'),
        Section(id="high-uric-acid-causes", level=2, heading="Causas de ácido úrico alto",
                body_html="<p>La hiperuricemia resulta de <strong>sobreproducción</strong>, <strong>infraexcreción</strong> renal, o ambas. La infraexcreción es responsable del 90% de los casos.</p><p><strong>Factores dietéticos y de estilo de vida:</strong> dieta rica en purinas (vísceras, mariscos, carnes rojas), alcohol (especialmente cerveza), bebidas azucaradas con fructosa y obesidad.</p><p><strong>Condiciones médicas:</strong> enfermedad renal crónica (consulte nuestra guía sobre <a href=\"/es/blog/creatinine-egfr-what-it-means\">creatinina y eGFR</a>), síndrome metabólico, trastornos mieloproliferativos, hipotiroidismo.</p><p><strong>Medicamentos:</strong> diuréticos tiazídicos, aspirina a dosis bajas, ciclosporina.</p>"),
        Section(id="gout-connection", level=2, heading="Ácido úrico y gota",
                body_html="<p>La <strong>gota</strong> es una artritis inflamatoria causada por depósito de cristales de urato monosódico en las articulaciones. Es la artritis inflamatoria más frecuente en hombres. El ataque clásico se presenta como dolor súbito, intenso, hinchazón y enrojecimiento, generalmente en la base del dedo gordo del pie (<em>podagra</em>).</p><p>No todas las personas con hiperuricemia desarrollan gota. Sin embargo, el riesgo aumenta con niveles más altos. La gota crónica no tratada puede causar <strong>tofos</strong>, erosión articular y daño permanente.</p><p>El manejo incluye tratamiento de ataques agudos con AINE, colchicina o corticosteroides, y terapia hipouricemiante a largo plazo con alopurinol o febuxostat.</p>"),
        Section(id="kidney-stones", level=2, heading="Ácido úrico y cálculos renales",
                body_html="<p>Los cálculos de ácido úrico representan aproximadamente el <strong>10% de todos los cálculos renales</strong>. Se forman cuando la orina es persistentemente ácida, concentrada y con exceso de ácido úrico.</p><p>A diferencia de los cálculos de calcio, los de ácido úrico son <strong>radiolúcidos</strong> y requieren TC o ecografía para su detección. La prevención incluye alcalinización urinaria, hidratación adecuada, restricción de purinas y, cuando sea necesario, alopurinol.</p>"),
        Section(id="uric-acid-and-diet", level=2, heading="Recomendaciones dietéticas para el ácido úrico",
                body_html="<p><strong>Alimentos a limitar:</strong> vísceras, ciertos mariscos (anchoas, sardinas, mejillones), carnes rojas en grandes cantidades, alcohol (especialmente cerveza) y bebidas azucaradas.</p><p><strong>Alimentos beneficiosos:</strong> lácteos bajos en grasa, cerezas, café, vitamina C y abundante agua. Las purinas vegetales (espinacas, champiñones, espárragos) no parecen aumentar el riesgo de gota.</p>"),
        Section(id="medications", level=2, heading="Medicamentos para el ácido úrico alto",
                body_html="<p><strong>Inhibidores de xantina oxidasa:</strong> alopurinol (el más utilizado, se titula hasta lograr ácido úrico &lt;6,0&nbsp;mg/dL) y febuxostat. <strong>Uricosúricos:</strong> probenecid y lesinurad, que aumentan la excreción renal.</p><p>Al iniciar terapia hipouricemiante, pueden aumentar paradójicamente los ataques de gota durante los primeros meses. Se prescribe colchicina profiláctica durante este periodo.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Cuándo consultar al médico",
                body_html="<p>Consulte a su médico si: ácido úrico &gt;7,0&nbsp;mg/dL (hombres) o &gt;6,0&nbsp;mg/dL (mujeres) en pruebas repetidas; síntomas de gota; antecedentes de cálculos renales; toma de medicamentos que elevan el ácido úrico; enfermedad renal crónica con hiperuricemia; o presencia de tofos.</p><p>La hiperuricemia asintomática es frecuente y no siempre requiere tratamiento, pero sí modificaciones del estilo de vida y seguimiento.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo Norya le ayuda a entender sus resultados de ácido úrico",
                body_html="<p>Interpretar el ácido úrico en el contexto de su panel completo puede ser complejo. <strong>Norya</strong> lo simplifica: suba sus resultados y reciba en minutos un resumen de salud claro y estructurado. <a href=\"/analyze\">Inicie su análisis gratuito con Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Hohe Harnsäure: Was Ihr Blutergebnis bedeutet",
                body_html="<p><strong>Harnsäure</strong> ist ein natürliches Abfallprodukt, das beim Abbau von <em>Purinen</em> entsteht&mdash;Substanzen, die in bestimmten Lebensmitteln vorkommen und beim normalen Zellumsatz produziert werden. Unter gesunden Bedingungen löst sich Harnsäure im Blut, passiert die Nieren und wird mit dem Urin ausgeschieden. Wenn der Körper zu viel produziert oder die Nieren nicht genug ausscheiden, steigen die Blutspiegel&mdash;<strong>Hyperurikämie</strong>.</p><p>Erhöhte Harnsäure ist vor allem als Ursache der <strong>Gicht</strong> bekannt, steht aber auch in Verbindung mit Nierensteinen, chronischer Nierenerkrankung und kardiovaskulärem Risiko. Dieser Leitfaden ist informativ und ersetzt keine ärztliche Beratung.</p>"),
        Section(id="what-is-uric-acid", level=2, heading="Was ist Harnsäure und wie wird sie produziert?",
                body_html="<p>Purine sind stickstoffhaltige Verbindungen, die in jeder Zelle und vielen Lebensmitteln vorkommen. Sie werden durch das Enzym <strong>Xanthinoxidase</strong> zu Harnsäure abgebaut. Menschen fehlt das Enzym Urikase, weshalb Harnsäure das Endprodukt des Purinabbaus ist.</p><p>Etwa zwei Drittel werden über die Nieren, ein Drittel über den Darm ausgeschieden. Transporter wie <strong>URAT1</strong> und <strong>GLUT9</strong> spielen Schlüsselrollen.</p><p>Harnsäure dient auch als <strong>Antioxidans</strong> im Blut und macht etwa die Hälfte der antioxidativen Kapazität des Plasmas aus.</p>"),
        Section(id="normal-ranges", level=2, heading="Normale Harnsäurewerte",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich (mg/dL)</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich (&micro;mol/L)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 &ndash; 7,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frauen</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 &ndash; 6,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr></tbody></table><p>Frauen haben dank Östrogen niedrigere Werte. Die Löslichkeitsgrenze liegt bei etwa <strong>6,8&nbsp;mg/dL</strong>&mdash;darüber können Uratkristalle entstehen.</p>'),
        Section(id="high-uric-acid-causes", level=2, heading="Ursachen hoher Harnsäure",
                body_html="<p><strong>Lebensstilfaktoren:</strong> purinreiche Ernährung (Innereien, Meeresfrüchte), Alkohol (besonders Bier), fruktosehaltige Getränke und Adipositas. <strong>Medizinische Ursachen:</strong> chronische Nierenerkrankung (siehe <a href=\"/de/blog/creatinine-egfr-what-it-means\">Kreatinin und eGFR</a>), metabolisches Syndrom, Zellzerfall bei Tumoren, Hypothyreose. <strong>Medikamente:</strong> Thiazid-/Schleifendiuretika, niedrig dosiertes Aspirin, Ciclosporin.</p>"),
        Section(id="gout-connection", level=2, heading="Harnsäure und Gicht",
                body_html="<p><strong>Gicht</strong> entsteht durch Ablagerung von Mononatriumurat-Kristallen in Gelenken. Der klassische Gichtanfall zeigt sich als plötzlicher, heftiger Schmerz mit Schwellung und Rötung, meist am Großzehengrundgelenk (<em>Podagra</em>).</p><p>Nicht jeder mit Hyperurikämie entwickelt Gicht, aber das Risiko steigt mit höheren Werten. Chronische unbehandelte Gicht führt zu <strong>Tophi</strong>, Gelenkerosion und dauerhaften Gelenkschäden.</p><p>Behandlung: Akuttherapie mit NSAR, Colchicin oder Kortikosteroiden; Langzeittherapie mit Allopurinol oder Febuxostat.</p>"),
        Section(id="kidney-stones", level=2, heading="Harnsäure und Nierensteine",
                body_html="<p>Harnsäuresteine machen etwa <strong>10% aller Nierensteine</strong> aus. Sie bilden sich bei dauerhaft saurem Urin. Anders als Kalziumsteine sind sie <strong>röntgennegativ</strong>. Prävention: Urinalkalisierung, Hydratation, Purinrestriktion und ggf. Allopurinol. Harnsäuresteine können oft medikamentös <strong>aufgelöst</strong> werden.</p>"),
        Section(id="uric-acid-and-diet", level=2, heading="Ernährungsempfehlungen bei hoher Harnsäure",
                body_html="<p><strong>Einschränken:</strong> Innereien, bestimmte Meeresfrüchte, rotes Fleisch in großen Mengen, Alkohol (besonders Bier), zuckerhaltige Getränke. <strong>Empfehlenswert:</strong> fettarme Milchprodukte, Kirschen, Kaffee, Vitamin C und viel Wasser. Pflanzliche Purine (Spinat, Pilze) müssen nicht eingeschränkt werden.</p>"),
        Section(id="medications", level=2, heading="Medikamente bei hoher Harnsäure",
                body_html="<p><strong>Xanthinoxidase-Hemmer:</strong> Allopurinol (am häufigsten), Febuxostat. <strong>Urikosurika:</strong> Probenecid, Lesinurad. Bei Therapiebeginn können Gichtanfälle paradox zunehmen; prophylaktisch wird Colchicin gegeben.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann Sie einen Arzt aufsuchen sollten",
                body_html="<p>Konsultieren Sie Ihren Arzt bei: Harnsäure &gt;7,0&nbsp;mg/dL (Männer) oder &gt;6,0&nbsp;mg/dL (Frauen); Gichtsymptomen; Nierensteinhistorie; Einnahme harnsäureerhöhender Medikamente; chronischer Nierenerkrankung; oder Tophi.</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie Norya Ihnen hilft, Ihre Harnsäure-Ergebnisse zu verstehen",
                body_html="<p><strong>Norya</strong> vereinfacht die Interpretation: Laden Sie Ihre Blutergebnisse hoch und erhalten Sie in Minuten einen klaren Gesundheitsbericht. <a href=\"/analyze\">Starten Sie Ihre Analyse mit Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Acide urique élevé : que signifie votre résultat d'analyse de sang ?",
                body_html="<p>L'<strong>acide urique</strong> est un déchet naturel produit lors de la dégradation des <em>purines</em>, des substances présentes dans certains aliments et produites lors du renouvellement cellulaire. Lorsque le corps en produit trop ou que les reins n'en excrètent pas assez, les niveaux sanguins augmentent&mdash;c'est l'<strong>hyperuricémie</strong>.</p><p>L'acide urique élevé est surtout connu pour causer la <strong>goutte</strong>, mais il est aussi lié aux calculs rénaux, à l'insuffisance rénale chronique et au risque cardiovasculaire. Ce guide est éducatif et ne remplace pas un avis médical.</p>"),
        Section(id="what-is-uric-acid", level=2, heading="Qu'est-ce que l'acide urique ?",
                body_html="<p>Les purines sont métabolisées par l'enzyme <strong>xanthine oxydase</strong> en acide urique. Les humains ne possèdent pas l'enzyme uricase, ce qui fait de l'acide urique le produit final du métabolisme des purines.</p><p>Environ deux tiers sont éliminés par les reins, le reste par le tractus gastro-intestinal. Les transporteurs <strong>URAT1</strong> et <strong>GLUT9</strong> jouent des rôles clés. L'acide urique a aussi un rôle d'<strong>antioxydant</strong> plasmatique.</p>"),
        Section(id="normal-ranges", level=2, heading="Valeurs normales d'acide urique",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normale (mg/dL)</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normale (&micro;mol/L)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 &ndash; 7,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 &ndash; 6,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr></tbody></table><p>La limite de solubilité est d\'environ <strong>6,8&nbsp;mg/dL</strong>. Au-dessus, des cristaux d\'urate peuvent se former.</p>'),
        Section(id="high-uric-acid-causes", level=2, heading="Causes de l'acide urique élevé",
                body_html="<p><strong>Facteurs alimentaires :</strong> régime riche en purines (abats, fruits de mer, viande rouge), alcool (surtout bière), boissons sucrées au fructose, obésité. <strong>Conditions médicales :</strong> insuffisance rénale chronique (voir <a href=\"/fr/blog/creatinine-egfr-what-it-means\">créatinine et DFG</a>), syndrome métabolique, troubles myéloprolifératifs. <strong>Médicaments :</strong> diurétiques, aspirine à faible dose, ciclosporine.</p>"),
        Section(id="gout-connection", level=2, heading="Acide urique et goutte",
                body_html="<p>La <strong>goutte</strong> est une arthrite inflammatoire causée par le dépôt de cristaux d'urate monosodique. La crise classique se manifeste par une douleur soudaine, intense, un gonflement et une rougeur, souvent au gros orteil (<em>podagre</em>). La goutte chronique non traitée peut entraîner des <strong>tophus</strong> et des dommages articulaires permanents.</p>"),
        Section(id="kidney-stones", level=2, heading="Acide urique et calculs rénaux",
                body_html="<p>Les calculs d'acide urique représentent environ <strong>10% de tous les calculs rénaux</strong>. Ils sont <strong>radiotransparents</strong> et nécessitent un scanner ou une échographie. La prévention repose sur l'alcalinisation urinaire, l'hydratation, la restriction des purines et l'allopurinol si nécessaire.</p>"),
        Section(id="uric-acid-and-diet", level=2, heading="Recommandations alimentaires pour l'acide urique",
                body_html="<p><strong>À limiter :</strong> abats, certains fruits de mer, viande rouge, alcool, boissons sucrées. <strong>Recommandés :</strong> produits laitiers allégés, cerises, café, vitamine C, eau en abondance. Les purines végétales ne semblent pas augmenter le risque de goutte.</p>"),
        Section(id="medications", level=2, heading="Médicaments pour l'acide urique élevé",
                body_html="<p><strong>Inhibiteurs de la xanthine oxydase :</strong> allopurinol, fébuxostat. <strong>Uricosuriques :</strong> probénécide, lésinurad. Au début du traitement, les crises de goutte peuvent augmenter paradoxalement; la colchicine prophylactique est alors prescrite.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter un médecin",
                body_html="<p>Consultez si : acide urique &gt;7,0 mg/dL (hommes) ou &gt;6,0 mg/dL (femmes) ; symptômes de goutte ; antécédents de calculs rénaux ; prise de médicaments hyperuricémiants ; insuffisance rénale chronique ; ou présence de tophus.</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment Norya vous aide à comprendre vos résultats d'acide urique",
                body_html="<p><strong>Norya</strong> simplifie l'interprétation : téléchargez vos résultats et recevez un rapport de santé clair en quelques minutes. <a href=\"/analyze\">Commencez votre analyse avec Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Acido urico alto: cosa significa il risultato delle analisi del sangue",
                body_html="<p>L'<strong>acido urico</strong> è un prodotto di scarto naturale che si forma quando il corpo scompone le <em>purine</em>, sostanze presenti in certi alimenti e prodotte durante il ricambio cellulare. Quando il corpo ne produce troppo o i reni non ne eliminano a sufficienza, i livelli nel sangue si alzano&mdash;<strong>iperuricemia</strong>.</p><p>L'acido urico elevato è noto per causare la <strong>gotta</strong>, ma è anche collegato a calcoli renali, nefropatia cronica e rischio cardiovascolare. Questa guida è educativa e non sostituisce il parere medico.</p>"),
        Section(id="what-is-uric-acid", level=2, heading="Cos'è l'acido urico?",
                body_html="<p>Le purine vengono metabolizzate dall'enzima <strong>xantina ossidasi</strong> in acido urico. Gli esseri umani mancano dell'enzima uricasi, rendendo l'acido urico il prodotto finale del metabolismo delle purine.</p><p>Circa due terzi vengono eliminati dai reni, il resto dal tratto gastrointestinale. I trasportatori <strong>URAT1</strong> e <strong>GLUT9</strong> svolgono ruoli chiave. L'acido urico agisce anche come <strong>antiossidante</strong> plasmatico.</p>"),
        Section(id="normal-ranges", level=2, heading="Valori normali di acido urico",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normale (mg/dL)</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normale (&micro;mol/L)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 &ndash; 7,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 &ndash; 6,0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr></tbody></table><p>Il limite di solubilità è circa <strong>6,8&nbsp;mg/dL</strong>; oltre possono formarsi cristalli di urato.</p>'),
        Section(id="high-uric-acid-causes", level=2, heading="Cause dell'acido urico alto",
                body_html="<p><strong>Fattori alimentari:</strong> dieta ricca di purine (frattaglie, frutti di mare, carne rossa), alcol (soprattutto birra), bevande zuccherate con fruttosio, obesità. <strong>Condizioni mediche:</strong> nefropatia cronica (vedi <a href=\"/it/blog/creatinine-egfr-what-it-means\">creatinina ed eGFR</a>), sindrome metabolica, disordini mieloproliferativi. <strong>Farmaci:</strong> diuretici tiazidici, aspirina a basse dosi, ciclosporina.</p>"),
        Section(id="gout-connection", level=2, heading="Acido urico e gotta",
                body_html="<p>La <strong>gotta</strong> è un'artrite infiammatoria causata dal deposito di cristalli di urato monosodico. L'attacco classico si presenta con dolore improvviso e intenso, gonfiore e rossore, spesso all'alluce (<em>podagra</em>). La gotta cronica non trattata può causare <strong>tofi</strong> e danni articolari permanenti.</p>"),
        Section(id="kidney-stones", level=2, heading="Acido urico e calcoli renali",
                body_html="<p>I calcoli di acido urico rappresentano circa il <strong>10% di tutti i calcoli renali</strong>. Sono <strong>radiotrasparenti</strong> e richiedono TC o ecografia. La prevenzione include alcalinizzazione urinaria, idratazione, restrizione delle purine e allopurinolo se necessario.</p>"),
        Section(id="uric-acid-and-diet", level=2, heading="Raccomandazioni dietetiche per l'acido urico",
                body_html="<p><strong>Da limitare:</strong> frattaglie, alcuni frutti di mare, carne rossa, alcol, bevande zuccherate. <strong>Consigliati:</strong> latticini magri, ciliegie, caffè, vitamina C, abbondante acqua. Le purine vegetali non sembrano aumentare il rischio di gotta.</p>"),
        Section(id="medications", level=2, heading="Farmaci per l'acido urico alto",
                body_html="<p><strong>Inibitori della xantina ossidasi:</strong> allopurinolo, febuxostat. <strong>Uricosurici:</strong> probenecid, lesinurad. All'inizio della terapia, gli attacchi di gotta possono paradossalmente aumentare; si prescrive colchicina profilattica.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico",
                body_html="<p>Consultate il medico se: acido urico &gt;7,0&nbsp;mg/dL (uomini) o &gt;6,0&nbsp;mg/dL (donne); sintomi di gotta; storia di calcoli renali; assunzione di farmaci iperuricemizzanti; nefropatia cronica; o presenza di tofi.</p>"),
        Section(id="how-norya-helps", level=2, heading="Come Norya ti aiuta a capire i risultati dell'acido urico",
                body_html="<p><strong>Norya</strong> semplifica l'interpretazione: caricate i risultati e ricevete in minuti un report sanitario chiaro. <a href=\"/analyze\">Iniziate l'analisi con Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="חומצת שתן גבוהה: מה המשמעות של תוצאת בדיקת הדם שלך",
                body_html="<p><strong>חומצת שתן</strong> היא תוצר פסולת טבעי שנוצר כאשר הגוף מפרק <em>פורינים</em>&mdash;חומרים הנמצאים במזונות מסוימים ומיוצרים גם על ידי הגוף. כאשר הגוף מייצר יותר מדי חומצת שתן או שהכליות לא מפרישות מספיק, הרמות בדם עולות&mdash;<strong>היפראוריצמיה</strong>.</p><p>חומצת שתן גבוהה ידועה בעיקר כגורמת ל<strong>שיגדון (גאוט)</strong>, אך קשורה גם לאבני כליה, מחלת כליות כרונית וסיכון קרדיווסקולרי.</p>"),
        Section(id="what-is-uric-acid", level=2, heading="מהי חומצת שתן?",
                body_html="<p>פורינים מפורקים על ידי האנזים <strong>קסנטין אוקסידאז</strong> לחומצת שתן. בני אדם חסרים את האנזים אוריקאז, ולכן חומצת שתן היא התוצר הסופי של חילוף חומרים של פורינים.</p><p>כשני שלישים מופרשים דרך הכליות והשליש הנותר דרך מערכת העיכול. חומצת שתן גם משמשת כ<strong>נוגד חמצון</strong> בדם.</p>"),
        Section(id="normal-ranges", level=2, heading="טווחים תקינים של חומצת שתן",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">קבוצה</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח תקין (mg/dL)</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח תקין (&micro;mol/L)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 &ndash; 7.0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 &ndash; 6.0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr></tbody></table><p>גבול המסיסות הוא כ-<strong>6.8 mg/dL</strong>. מעל ריכוז זה עלולים להיווצר גבישי אוראט.</p>'),
        Section(id="high-uric-acid-causes", level=2, heading="גורמים לחומצת שתן גבוהה",
                body_html="<p><strong>גורמי תזונה:</strong> תזונה עשירה בפורינים (איברים פנימיים, פירות ים, בשר אדום), אלכוהול (במיוחד בירה), משקאות ממותקים בפרוקטוז, השמנה. <strong>מצבים רפואיים:</strong> מחלת כליות כרונית (ראו <a href=\"/he/blog/creatinine-egfr-what-it-means\">קריאטינין ו-eGFR</a>), תסמונת מטבולית, הפרעות מיאלופרוליפרטיביות. <strong>תרופות:</strong> משתנים, אספירין במינון נמוך.</p>"),
        Section(id="gout-connection", level=2, heading="חומצת שתן ושיגדון",
                body_html="<p><strong>שיגדון (גאוט)</strong> הוא דלקת פרקים גבישית הנגרמת מהצטברות גבישי אוראט מונוסודיום במפרקים. ההתקף הקלאסי מתבטא בכאב פתאומי, עז, נפיחות ואדמומיות, בדרך כלל בבוהן הגדולה. שיגדון כרוני לא מטופל עלול לגרום ל<strong>טופי</strong> ולנזק קבוע למפרקים.</p>"),
        Section(id="kidney-stones", level=2, heading="חומצת שתן ואבני כליה",
                body_html="<p>אבני חומצת שתן מהוות כ-<strong>10% מכל אבני הכליה</strong>. הן <strong>שקופות לצילום רנטגן</strong> ודורשות CT או אולטרסאונד. מניעה כוללת אלקלוז השתן, שתייה מרובה, הגבלת פורינים ואלופורינול במידת הצורך.</p>"),
        Section(id="uric-acid-and-diet", level=2, heading="המלצות תזונתיות לניהול חומצת שתן",
                body_html="<p><strong>להגביל:</strong> איברים פנימיים, פירות ים מסוימים, בשר אדום, אלכוהול, משקאות ממותקים. <strong>מומלצים:</strong> מוצרי חלב דלי שומן, דובדבנים, קפה, ויטמין C, שתייה מרובה. פורינים צמחיים אינם מגבירים סיכון לשיגדון.</p>"),
        Section(id="medications", level=2, heading="תרופות לחומצת שתן גבוהה",
                body_html="<p><strong>מעכבי קסנטין אוקסידאז:</strong> אלופורינול, פבוקסוסטט. <strong>אוריקוזורים:</strong> פרובנציד, לסינוראד. בתחילת הטיפול התקפי שיגדון עלולים לגבור באופן פרדוקסלי; ניתנת קולכיצין מניעתית.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא",
                body_html="<p>פנו לרופא אם: חומצת שתן מעל 7.0 mg/dL (גברים) או 6.0 mg/dL (נשים); תסמיני שיגדון; היסטוריה של אבני כליה; נטילת תרופות מעלות חומצת שתן; מחלת כליות כרונית; או טופי.</p>"),
        Section(id="how-norya-helps", level=2, heading="כיצד Norya עוזרת לך להבין את תוצאות חומצת השתן",
                body_html="<p><strong>Norya</strong> מפשטת את הפרשנות: העלו את תוצאות בדיקת הדם וקבלו דוח בריאות ברור תוך דקות. <a href=\"/analyze\">התחילו ניתוח עם Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="उच्च यूरिक एसिड: आपकी रक्त जांच के परिणाम का क्या अर्थ है",
                body_html="<p><strong>यूरिक एसिड</strong> एक प्राकृतिक अपशिष्ट उत्पाद है जो शरीर द्वारा <em>प्यूरीन</em> के विघटन से बनता है। जब शरीर बहुत अधिक यूरिक एसिड बनाता है या गुर्दे पर्याप्त मात्रा में इसे बाहर नहीं निकाल पाते, तो रक्त स्तर बढ़ जाता है&mdash;<strong>हाइपरयूरिसीमिया</strong>।</p><p>उच्च यूरिक एसिड <strong>गठिया (गाउट)</strong> का सबसे ज्ञात कारण है, लेकिन यह गुर्दे की पथरी, क्रोनिक किडनी रोग और हृदय जोखिम से भी जुड़ा है।</p>"),
        Section(id="what-is-uric-acid", level=2, heading="यूरिक एसिड क्या है?",
                body_html="<p>प्यूरीन <strong>ज़ैन्थिन ऑक्सिडेज़</strong> एंजाइम द्वारा यूरिक एसिड में बदले जाते हैं। मनुष्यों में यूरिकेज़ एंजाइम नहीं होता, इसलिए यूरिक एसिड प्यूरीन चयापचय का अंतिम उत्पाद है।</p><p>लगभग दो-तिहाई गुर्दों द्वारा और शेष एक-तिहाई जठरांत्र पथ द्वारा उत्सर्जित होता है। यूरिक एसिड रक्त में <strong>एंटीऑक्सीडेंट</strong> के रूप में भी कार्य करता है।</p>"),
        Section(id="normal-ranges", level=2, heading="सामान्य यूरिक एसिड सीमाएँ",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य सीमा (mg/dL)</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य सीमा (&micro;mol/L)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">पुरुष</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 &ndash; 7.0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">महिलाएँ</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 &ndash; 6.0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr></tbody></table><p>घुलनशीलता सीमा लगभग <strong>6.8 mg/dL</strong> है। इससे ऊपर यूरेट क्रिस्टल बन सकते हैं।</p>'),
        Section(id="high-uric-acid-causes", level=2, heading="उच्च यूरिक एसिड के कारण",
                body_html="<p><strong>आहार कारक:</strong> प्यूरीन-समृद्ध आहार (अंग मांस, समुद्री भोजन, लाल मांस), शराब (विशेषकर बीयर), फ्रुक्टोज युक्त पेय, मोटापा। <strong>चिकित्सा स्थितियाँ:</strong> क्रोनिक किडनी रोग (<a href=\"/hi/blog/creatinine-egfr-what-it-means\">क्रिएटिनिन और eGFR</a> देखें), मेटाबोलिक सिंड्रोम। <strong>दवाएँ:</strong> मूत्रवर्धक, कम खुराक एस्पिरिन।</p>"),
        Section(id="gout-connection", level=2, heading="यूरिक एसिड और गठिया (गाउट)",
                body_html="<p><strong>गाउट</strong> मोनोसोडियम यूरेट क्रिस्टल के जोड़ों में जमा होने से होने वाला सूजन वाला गठिया है। क्लासिक हमला अचानक, तीव्र दर्द, सूजन और लालिमा के रूप में प्रकट होता है, आमतौर पर पैर के अंगूठे में। अनुपचारित क्रोनिक गाउट <strong>टोफी</strong> और स्थायी जोड़ क्षति का कारण बन सकता है।</p>"),
        Section(id="kidney-stones", level=2, heading="यूरिक एसिड और गुर्दे की पथरी",
                body_html="<p>यूरिक एसिड की पथरी सभी गुर्दे की पथरी का लगभग <strong>10%</strong> है। ये <strong>रेडियोल्यूसेंट</strong> होती हैं। रोकथाम में मूत्र क्षारीकरण, पर्याप्त जलयोजन, प्यूरीन प्रतिबंध और एलोप्यूरिनॉल शामिल हैं।</p>"),
        Section(id="uric-acid-and-diet", level=2, heading="यूरिक एसिड प्रबंधन के लिए आहार संबंधी सिफारिशें",
                body_html="<p><strong>सीमित करें:</strong> अंग मांस, कुछ समुद्री भोजन, लाल मांस, शराब, मीठे पेय। <strong>सहायक:</strong> कम वसा वाले डेयरी उत्पाद, चेरी, कॉफी, विटामिन C, पर्याप्त पानी। सब्जियों के प्यूरीन गाउट जोखिम नहीं बढ़ाते।</p>"),
        Section(id="medications", level=2, heading="उच्च यूरिक एसिड के लिए दवाएँ",
                body_html="<p><strong>ज़ैन्थिन ऑक्सिडेज़ अवरोधक:</strong> एलोप्यूरिनॉल, फेबक्सोस्टैट। <strong>यूरिकोसुरिक:</strong> प्रोबेनेसिड, लेसिनुराड। उपचार शुरू होने पर गाउट के हमले विरोधाभासी रूप से बढ़ सकते हैं; रोगनिरोधी कोल्चिसिन दी जाती है।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर को कब दिखाएँ",
                body_html="<p>डॉक्टर से परामर्श करें यदि: यूरिक एसिड पुरुषों में &gt;7.0 mg/dL या महिलाओं में &gt;6.0 mg/dL; गाउट के लक्षण; गुर्दे की पथरी का इतिहास; यूरिक एसिड बढ़ाने वाली दवाएँ; क्रोनिक किडनी रोग; या टोफी।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya यूरिक एसिड परिणामों को समझने में कैसे मदद करता है",
                body_html="<p><strong>Norya</strong> व्याख्या को सरल बनाता है: अपनी रक्त जांच के परिणाम अपलोड करें और मिनटों में स्पष्ट स्वास्थ्य रिपोर्ट प्राप्त करें। <a href=\"/analyze\">Norya के साथ विश्लेषण शुरू करें</a>।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="حمض اليوريك المرتفع: ماذا تعني نتيجة تحليل الدم",
                body_html="<p><strong>حمض اليوريك (حمض البول)</strong> هو ناتج طبيعي عن تحلل <em>البيورينات</em> في الجسم. عندما ينتج الجسم كمية كبيرة أو لا تتمكن الكلى من إخراجها بكفاية، ترتفع المستويات في الدم&mdash;<strong>فرط حمض يوريك الدم</strong>.</p><p>حمض اليوريك المرتفع معروف بأنه يسبب <strong>النقرس</strong>، وهو شكل مؤلم من التهاب المفاصل، كما أنه مرتبط بحصى الكلى وأمراض الكلى المزمنة والمخاطر القلبية الوعائية.</p>"),
        Section(id="what-is-uric-acid", level=2, heading="ما هو حمض اليوريك؟",
                body_html="<p>البيورينات يتم تحويلها بواسطة إنزيم <strong>زانثين أوكسيداز</strong> إلى حمض اليوريك. البشر يفتقرون لإنزيم اليوريكاز، لذا حمض اليوريك هو الناتج النهائي. يُفرز ثلثاه عبر الكلى والثلث عبر الجهاز الهضمي. يعمل أيضاً ك<strong>مضاد أكسدة</strong> في الدم.</p>"),
        Section(id="normal-ranges", level=2, heading="النطاقات الطبيعية لحمض اليوريك",
                body_html='<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"><thead><tr><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المجموعة</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الطبيعي (mg/dL)</th><th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الطبيعي (&micro;mol/L)</th></tr></thead><tbody><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الرجال</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 &ndash; 7.0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">200 &ndash; 420</td></tr><tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">النساء</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 &ndash; 6.0</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">140 &ndash; 360</td></tr></tbody></table><p>حد الذوبان حوالي <strong>6.8 mg/dL</strong>. فوق ذلك قد تتكون بلورات اليورات.</p>'),
        Section(id="high-uric-acid-causes", level=2, heading="أسباب ارتفاع حمض اليوريك",
                body_html="<p><strong>عوامل غذائية:</strong> نظام غذائي غني بالبيورينات (أحشاء، مأكولات بحرية، لحوم حمراء)، الكحول (خاصة البيرة)، مشروبات الفركتوز، السمنة. <strong>حالات طبية:</strong> أمراض الكلى المزمنة (انظر <a href=\"/ar/blog/creatinine-egfr-what-it-means\">الكرياتينين ومعدل الترشيح الكبيبي</a>)، المتلازمة الأيضية. <strong>أدوية:</strong> مدرات البول، الأسبرين بجرعة منخفضة.</p>"),
        Section(id="gout-connection", level=2, heading="حمض اليوريك والنقرس",
                body_html="<p><strong>النقرس</strong> التهاب مفاصل بلوري ناتج عن ترسب بلورات يورات أحادية الصوديوم. النوبة الكلاسيكية تتجلى بألم مفاجئ شديد وتورم واحمرار، عادة في إصبع القدم الكبير. النقرس المزمن غير المعالج يمكن أن يسبب <strong>توفي</strong> وأضراراً دائمة بالمفاصل.</p>"),
        Section(id="kidney-stones", level=2, heading="حمض اليوريك وحصى الكلى",
                body_html="<p>حصى حمض اليوريك تشكل حوالي <strong>10% من جميع حصى الكلى</strong>. هي <strong>شفافة للأشعة</strong> وتتطلب أشعة مقطعية أو تصويراً بالموجات فوق الصوتية. الوقاية تشمل قلونة البول والترطيب وتقييد البيورينات والألوبيورينول عند الحاجة.</p>"),
        Section(id="uric-acid-and-diet", level=2, heading="توصيات غذائية لإدارة حمض اليوريك",
                body_html="<p><strong>للتقليل:</strong> أحشاء، بعض المأكولات البحرية، لحوم حمراء، كحول، مشروبات محلاة. <strong>مفيدة:</strong> منتجات ألبان قليلة الدسم، كرز، قهوة، فيتامين C، ماء وفير. البيورينات النباتية لا تزيد خطر النقرس.</p>"),
        Section(id="medications", level=2, heading="أدوية لحمض اليوريك المرتفع",
                body_html="<p><strong>مثبطات زانثين أوكسيداز:</strong> ألوبيورينول، فيبوكسوستات. <strong>محفزات الإخراج:</strong> بروبنسيد، ليسينوراد. عند بدء العلاج قد تزداد نوبات النقرس بشكل متناقض؛ يُوصف كولشيسين وقائي.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى يجب مراجعة الطبيب",
                body_html="<p>استشر طبيبك إذا: حمض اليوريك أعلى من 7.0 mg/dL (رجال) أو 6.0 mg/dL (نساء)؛ أعراض نقرس؛ تاريخ حصى كلى؛ تناول أدوية ترفع حمض اليوريك؛ مرض كلوي مزمن؛ أو وجود توفي.</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف تساعدك Norya في فهم نتائج حمض اليوريك",
                body_html="<p><strong>Norya</strong> تبسّط التفسير: ارفع نتائج تحليل الدم واحصل على تقرير صحي واضح خلال دقائق. <a href=\"/analyze\">ابدأ التحليل مع Norya</a>.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# PUBLIC GETTERS
# ---------------------------------------------------------------------------
def get_uric_acid_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_uric_acid_faq_schema_qa() -> dict:
    return {
        "en": [
            {"question": "What is a normal uric acid level?",
             "answer": "Normal uric acid levels are 3.4-7.0 mg/dL for men and 2.4-6.0 mg/dL for women. The solubility limit is about 6.8 mg/dL, above which urate crystals can form."},
            {"question": "What causes high uric acid?",
             "answer": "High uric acid is caused by purine-rich diets (organ meats, shellfish), alcohol (especially beer), fructose-sweetened beverages, obesity, kidney disease, certain medications (diuretics), and genetic factors."},
            {"question": "Can high uric acid cause gout?",
             "answer": "Yes. Gout is caused by deposition of urate crystals in joints when uric acid exceeds its solubility limit. However, not everyone with high uric acid develops gout."},
            {"question": "What foods should I avoid with high uric acid?",
             "answer": "Limit organ meats, shellfish, red meat, beer, spirits, and sugar-sweetened beverages. Low-fat dairy, cherries, coffee, and adequate water may help lower levels."},
            {"question": "Does high uric acid cause kidney stones?",
             "answer": "Yes. Uric acid kidney stones account for about 10% of all kidney stones. They form when urine is persistently acidic and concentrated."},
        ],
        "tr": [
            {"question": "Normal ürik asit düzeyi nedir?",
             "answer": "Normal ürik asit erkeklerde 3,4-7,0 mg/dL, kadınlarda 2,4-6,0 mg/dL'dir. Çözünürlük sınırı yaklaşık 6,8 mg/dL'dir."},
            {"question": "Yüksek ürik aside ne sebep olur?",
             "answer": "Pürinden zengin diyet (sakatat, kabuklu deniz ürünleri), alkol (özellikle bira), şekerli içecekler, obezite, böbrek hastalığı ve diüretik gibi ilaçlar."},
            {"question": "Yüksek ürik asit gut hastalığına neden olur mu?",
             "answer": "Evet. Gut, ürik asit çözünürlük sınırını aştığında ürat kristallerinin eklemlere birikmesiyle oluşur. Ancak yüksek ürik asidi olan herkes gut geliştirmez."},
            {"question": "Yüksek ürik asitli hangi besinlerden kaçınmalıyım?",
             "answer": "Sakatat, kabuklu deniz ürünleri, kırmızı et, bira ve şekerli içecekleri sınırlayın. Az yağlı süt ürünleri, kiraz, kahve ve bol su yardımcı olabilir."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de ácido úrico?",
             "answer": "Normal: hombres 3,4-7,0 mg/dL, mujeres 2,4-6,0 mg/dL. El límite de solubilidad es aproximadamente 6,8 mg/dL."},
            {"question": "¿Qué causa el ácido úrico alto?",
             "answer": "Dieta rica en purinas, alcohol (especialmente cerveza), bebidas con fructosa, obesidad, enfermedad renal, y medicamentos como diuréticos."},
            {"question": "¿Qué alimentos debo evitar con ácido úrico alto?",
             "answer": "Limite vísceras, mariscos, carnes rojas, cerveza y bebidas azucaradas. Los lácteos bajos en grasa, cerezas, café y agua abundante pueden ayudar."},
        ],
        "de": [
            {"question": "Was ist ein normaler Harnsäurewert?",
             "answer": "Normal: Männer 3,4-7,0 mg/dL, Frauen 2,4-6,0 mg/dL. Die Löslichkeitsgrenze liegt bei etwa 6,8 mg/dL."},
            {"question": "Was verursacht hohe Harnsäure?",
             "answer": "Purinreiche Ernährung, Alkohol (besonders Bier), Fruktosegetränke, Adipositas, Nierenerkrankung und Medikamente wie Diuretika."},
            {"question": "Welche Lebensmittel sollte man bei hoher Harnsäure meiden?",
             "answer": "Innereien, Meeresfrüchte, rotes Fleisch, Bier und Süßgetränke einschränken. Fettarme Milchprodukte, Kirschen, Kaffee und viel Wasser können helfen."},
        ],
        "fr": [
            {"question": "Quel est le taux normal d'acide urique ?",
             "answer": "Normal : hommes 3,4-7,0 mg/dL, femmes 2,4-6,0 mg/dL. La limite de solubilité est d'environ 6,8 mg/dL."},
            {"question": "Qu'est-ce qui cause l'acide urique élevé ?",
             "answer": "Régime riche en purines, alcool (surtout bière), boissons au fructose, obésité, maladie rénale et médicaments comme les diurétiques."},
            {"question": "Quels aliments éviter en cas d'acide urique élevé ?",
             "answer": "Limiter abats, fruits de mer, viande rouge, bière et boissons sucrées. Produits laitiers allégés, cerises, café et eau abondante peuvent aider."},
        ],
        "it": [
            {"question": "Qual è il livello normale di acido urico?",
             "answer": "Normale: uomini 3,4-7,0 mg/dL, donne 2,4-6,0 mg/dL. Il limite di solubilità è circa 6,8 mg/dL."},
            {"question": "Cosa causa l'acido urico alto?",
             "answer": "Dieta ricca di purine, alcol (soprattutto birra), bevande al fruttosio, obesità, nefropatia e farmaci come diuretici."},
            {"question": "L'acido urico alto può causare la gotta?",
             "answer": "Sì. La gotta è causata dal deposito di cristalli di urato quando l'acido urico supera il limite di solubilità."},
        ],
        "he": [
            {"question": "מהי רמת חומצת שתן תקינה?",
             "answer": "תקין: גברים 3.4-7.0 mg/dL, נשים 2.4-6.0 mg/dL. גבול המסיסות כ-6.8 mg/dL."},
            {"question": "מה גורם לחומצת שתן גבוהה?",
             "answer": "תזונה עשירה בפורינים, אלכוהול (במיוחד בירה), משקאות ממותקים, השמנה, מחלת כליות ותרופות כמו משתנים."},
            {"question": "האם חומצת שתן גבוהה גורמת לשיגדון?",
             "answer": "כן. שיגדון נגרם מהצטברות גבישי אוראט במפרקים. עם זאת, לא כל מי עם חומצת שתן גבוהה מפתח שיגדון."},
        ],
        "hi": [
            {"question": "सामान्य यूरिक एसिड स्तर क्या है?",
             "answer": "सामान्य: पुरुष 3.4-7.0 mg/dL, महिलाएँ 2.4-6.0 mg/dL। घुलनशीलता सीमा लगभग 6.8 mg/dL है।"},
            {"question": "उच्च यूरिक एसिड का क्या कारण है?",
             "answer": "प्यूरीन-समृद्ध आहार, शराब (विशेषकर बीयर), फ्रुक्टोज पेय, मोटापा, गुर्दे की बीमारी और मूत्रवर्धक जैसी दवाएँ।"},
            {"question": "उच्च यूरिक एसिड से गठिया हो सकता है?",
             "answer": "हाँ। गाउट यूरेट क्रिस्टल के जोड़ों में जमा होने से होता है। हालांकि, उच्च यूरिक एसिड वाले सभी लोगों को गाउट नहीं होता।"},
        ],
        "ar": [
            {"question": "ما هو المستوى الطبيعي لحمض اليوريك؟",
             "answer": "طبيعي: الرجال 3.4-7.0 mg/dL، النساء 2.4-6.0 mg/dL. حد الذوبان حوالي 6.8 mg/dL."},
            {"question": "ما أسباب ارتفاع حمض اليوريك؟",
             "answer": "نظام غذائي غني بالبيورينات، الكحول (خاصة البيرة)، مشروبات الفركتوز، السمنة، أمراض الكلى وأدوية مثل مدرات البول."},
            {"question": "هل يسبب حمض اليوريك المرتفع النقرس؟",
             "answer": "نعم. النقرس ناتج عن ترسب بلورات اليورات في المفاصل عندما يتجاوز حمض اليوريك حد ذوبانه."},
        ],
    }
