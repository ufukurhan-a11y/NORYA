# -*- coding: utf-8 -*-
"""
Uric acid blog article — full body content for all 9 languages.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Ürik Asit: Kanda Ne Anlama Gelir?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>ürik asit</strong> değeri yüksek veya düşük çıktığında ne anlama geldiğini merak etmeniz doğal. "
                "Ürik asit, vücudunuzun pürinleri parçalaması sırasında oluşan doğal bir atık ürünüdür ve normalde böbrekler aracılığıyla vücuttan uzaklaştırılır. "
                "Ancak düzeyi çok yükseldiğinde gut hastalığından böbrek taşlarına kadar ciddi sağlık sorunlarına yol açabilir.</p>"
                "<p>Bu rehber, ürik asidin ne olduğunu, normal referans aralıklarını, yüksekliğinin nedenlerini, gut ve böbrek taşı bağlantısını, beslenme önerilerini "
                "ve ne zaman doktora başvurmanız gerektiğini sade bir dille açıklamaktadır. Amacımız sizi hekiminizle yapacağınız görüşmeye hazırlamaktır; "
                "buradaki bilgiler teşhis yerine geçmez.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="Ürik Asit Nedir?",
            body_html=(
                "<p>Ürik asit, vücuttaki hücrelerin doğal yenilenmesi ve besinlerle alınan <strong>pürinlerin</strong> metabolizması sonucunda ortaya çıkan bir kimyasal bileşiktir. "
                "Pürinler hem vücut hücrelerinde hem de kırmızı et, sakatat, kabuklu deniz ürünleri ve bazı baklagiller gibi gıdalarda bulunur.</p>"
                "<p>Normal koşullarda ürik asit kanda çözünmüş hâlde dolaşır, böbreklerden süzülerek idrarla atılır. "
                "Üretim-atım dengesi bozulduğunda kanda ürik asit seviyesi yükselir; buna tıp dilinde <em>hiperürisemi</em> denir. "
                "Hiperürisemi her zaman belirti vermez, ancak uzun süre devam ettiğinde eklemlerde kristal birikmesine (gut) veya böbreklerde taş oluşumuna zemin hazırlayabilir.</p>"
                "<p>Ürik asit ölçümü basit bir kan testiyle yapılır ve genellikle böbrek fonksiyon testleri, <a href=\"/tr/blog/kreatinin-ve-egfr-nedir\">kreatinin/eGFR</a> "
                "ile birlikte istenir. Sonuçların doğru yorumlanması için yaş, cinsiyet, beslenme alışkanlıkları ve mevcut hastalıklar göz önünde bulundurulmalıdır.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Ürik Asit Normal Değerleri",
            body_html=(
                "<p>Ürik asit referans aralıkları laboratuvara göre küçük farklılıklar gösterebilir; ancak genel kabul gören aralıklar aşağıdaki tablodadır:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grup</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 – 7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 – 6,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>Menopoz sonrası kadınlarda östrojen düşüşüyle birlikte ürik asit düzeyi erkeklere yaklaşabilir. "
                "Çocuklarda ise referans aralıkları daha düşüktür. Laboratuvarınızın kendi raporunda belirttiği aralığı esas almanız önerilir.</p>"
                "<p>Tek bir yüksek sonuç her zaman hastalık anlamına gelmez; ancak kalıcı yükseklik araştırılmalıdır. "
                "Sonuçlarınızı mutlaka bir sağlık profesyoneliyle değerlendirin.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Ürik Asit Yüksekliğinin Nedenleri (Hiperürisemi)",
            body_html=(
                "<p><strong>Hiperürisemi</strong> birçok farklı nedene bağlı gelişebilir. En sık karşılaşılan faktörler şunlardır:</p>"
                "<p><strong>Beslenme:</strong> Pürin açısından zengin gıdalar (sakatat, kırmızı et, kabuklu deniz ürünleri, sardalye, hamsi) aşırı tüketildiğinde ürik asit üretimi artar. "
                "Fruktoz bakımından zengin içecekler ve alkol (özellikle bira) da ürik asit düzeyini yükseltir.</p>"
                "<p><strong>Böbrek fonksiyon bozukluğu:</strong> Böbrekler ürik asidi yeterince atamazsa kanda birikim olur. "
                "Kronik böbrek hastalığında <a href=\"/tr/blog/kreatinin-ve-egfr-nedir\">kreatinin ve eGFR</a> değerleri de bozulur ve ürik asit yüksekliği sıklıkla eşlik eder.</p>"
                "<p><strong>Diğer nedenler:</strong> Obezite, insülin direnci, hipertansiyon, hipotiroidi, bazı ilaçlar (tiyazid diüretikler, düşük doz aspirin, siklosporin), "
                "genetik yatkınlık ve hücre yıkımını artıran durumlar (lösemi tedavisi, tümör lizis sendromu) da ürik asidi yükseltebilir.</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="Ürik Asit ve Gut Hastalığı İlişkisi",
            body_html=(
                "<p><strong>Gut</strong>, kanda aşırı biriken ürik asidin monosodyum ürat kristalleri hâlinde eklemlere çökmesiyle ortaya çıkan inflamatuar bir artrit türüdür. "
                "En sık ayak başparmağı eklemi etkilenir; ancak ayak bileği, diz, bilek ve parmak eklemlerinde de görülebilir.</p>"
                "<p>Gut atağı genellikle gece ani başlayan şiddetli ağrı, şişlik, kızarıklık ve ısı artışı ile kendini gösterir. "
                "Tedavi edilmezse ataklar sıklaşabilir ve eklemlerde kalıcı hasar (tofüs oluşumu) meydana gelebilir. "
                "Hiperürisemisi olan herkes gut geliştirmez; ancak kan ürik asit düzeyi ne kadar yüksek ve ne kadar uzun sürerse risk o kadar artar.</p>"
                "<p>Gut tanısı sadece ürik asit düzeyiyle konmaz; eklem sıvısı analizi, klinik bulgular ve görüntüleme yöntemleri de değerlendirilir. "
                "Gut şüpheniz varsa bir romatoloji uzmanına başvurmanız önerilir.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Ürik Asit ve Böbrek Taşları",
            body_html=(
                "<p>Yüksek ürik asit düzeyi böbreklerde ürik asit kristallerinin birikmesine ve zamanla taş oluşumuna yol açabilir. "
                "Ürik asit taşları tüm böbrek taşlarının yaklaşık %5-10'unu oluşturur ve asidik idrarda (pH &lt; 5,5) daha kolay çökelir.</p>"
                "<p>Belirtiler arasında böğür veya sırt ağrısı, idrar yaparken yanma, kanlı idrar ve bulantı sayılabilir. "
                "Küçük taşlar kendiliğinden düşebilirken, büyük taşlar tıbbi veya cerrahi müdahale gerektirebilir.</p>"
                "<p>Böbrek taşı riskini azaltmak için bol su içmek (günde en az 2-3 litre), idrarı alkalize edecek beslenme düzenlemeleri yapmak ve "
                "ürik asit düzeyini kontrol altında tutmak önemlidir. "
                "<a href=\"/tr/blog/kreatinin-ve-egfr-nedir\">Kreatinin ve eGFR</a> takibi de böbrek sağlığının değerlendirilmesinde kritik bir yere sahiptir.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Ürik Asit ve Beslenme Önerileri",
            body_html=(
                "<p>Beslenme düzenlemeleri ürik asit kontrolünde kilit rol oynar. <strong>Düşük pürinli diyet</strong> ilkesi, "
                "sakatat, kabuklu deniz ürünleri, hamsi, sardalye ve yüksek fruktozlu içeceklerin sınırlandırılmasını içerir.</p>"
                "<p><strong>Önerilen gıdalar:</strong> Düşük yağlı süt ürünleri, yumurta, tam tahıllar, sebzeler (ıspanak ve kuşkonmaz ılımlı tüketilebilir), meyveler ve bol su. "
                "Araştırmalar, düşük yağlı süt ürünlerinin ürik asit atılımını artırabileceğini göstermektedir. C vitamini takviyesinin de hafif düşürücü etkisi olabilir.</p>"
                "<p><strong>Alkol:</strong> Bira en yüksek pürin içeriğine sahip alkollü içecektir ve ürik asit düzeyini belirgin şekilde artırır. "
                "Şarap daha az etkili olsa da aşırı tüketimden kaçınılmalıdır. Alkolsüz bira da pürin içerdiği için dikkatli olunmalıdır.</p>"
                "<p><strong>Hidrasyon:</strong> Günde en az 2-3 litre su içmek, böbreklerin ürik asidi etkili şekilde atmasına yardımcı olur ve taş oluşum riskini azaltır.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Ürik Asit İçin İlaç Tedavisi",
            body_html=(
                "<p>Yaşam tarzı değişiklikleri tek başına yeterli olmadığında veya tekrarlayan gut atakları ya da böbrek taşları söz konusu olduğunda "
                "doktor ilaç tedavisi başlayabilir. İlaçlar iki ana gruba ayrılır:</p>"
                "<p><strong>Ürik asit üretimini azaltanlar:</strong> Allopurinol ve febuksostat, ksantin oksidaz enzimini inhibe ederek ürik asit oluşumunu düşürür. "
                "Bu ilaçlar uzun süreli kullanılır ve doktorun belirlediği dozda alınmalıdır.</p>"
                "<p><strong>Ürik asit atılımını artıranlar (ürikozürikler):</strong> Probenesid ve lesinurad gibi ilaçlar böbreklerden ürik asit atılımını hızlandırır. "
                "Bu grup ilaçlar kullanılırken yeterli sıvı alımı ve böbrek fonksiyonlarının takibi önemlidir.</p>"
                "<p>Gut atağı sırasında anti-inflamatuar ilaçlar (NSAİİ), kolşisin veya kısa süreli kortikosteroidler kullanılabilir. "
                "İlaç tedavisi her zaman bir hekimin gözetiminde başlanmalı ve sürdürülmelidir; kendi kendinize ilaç ayarlaması yapmayın.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne Zaman Doktora Başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlardan herhangi biri varsa bir sağlık profesyoneline danışmanız önerilir:</p>"
                "<p>Kan tahlilinde ürik asit düzeyiniz referans aralığının üzerinde çıktıysa; eklemlerinizde ani, şiddetli ağrı, şişlik veya kızarıklık varsa; "
                "böğür veya sırt ağrısı, idrar yaparken yanma gibi böbrek taşı belirtileri yaşıyorsanız; ailede gut veya böbrek taşı öyküsü varsa; "
                "ya da mevcut tedavinize rağmen ürik asit düzeyiniz düşmüyorsa mutlaka hekiminize başvurun.</p>"
                "<p>Ürik asit yüksekliği tek başına her zaman tedavi gerektirmez; ancak altta yatan nedenlerin araştırılması ve risk faktörlerinin belirlenmesi için "
                "klinik değerlendirme önemlidir. Erken tanı ve yaşam tarzı düzenlemeleri, gut ve böbrek taşı gibi komplikasyonların önlenmesinde büyük fark yaratır.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya Bu Süreçte Size Nasıl Yardımcı Olur?",
            body_html=(
                "<p>Norya'da teşhis koymuyoruz; sizi hekiminizle yapacağınız görüşmeye hazırlıyoruz. "
                "<a href=\"/analyze\">Kan tahlili raporunuzu yükleyerek</a> ürik asit dahil tüm değerlerinizin sade dilde, "
                "referans aralıklarıyla birlikte açıklandığı yapılandırılmış bir sağlık özeti alabilirsiniz—birkaç dakika içinde.</p>"
                "<p>Bu özet sayesinde hekiminize doğru soruları sorabilir, sonuçlarınızı bağlamında anlayabilir ve randevunuzdan en iyi verimi alabilirsiniz. "
                "Seçenekler ve fiyatlar için <a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                'Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. '
                '<a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Uric Acid: What Your Blood Test Result Means",
            body_html=(
                "<p>If your blood work shows an abnormal <strong>uric acid</strong> level, you may wonder what it means for your health. "
                "Uric acid is a natural waste product formed when the body breaks down purines—substances found in certain foods and in your own cells. "
                "Normally, uric acid dissolves in the blood, passes through the kidneys, and leaves the body in urine.</p>"
                "<p>When uric acid builds up—a condition called <em>hyperuricemia</em>—it can lead to gout, kidney stones, and other complications. "
                "This guide explains what uric acid is, what normal levels look like, why levels rise, and what you can do about it. "
                "It is designed to help you prepare for a conversation with your doctor, not to replace medical advice.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="What Is Uric Acid?",
            body_html=(
                "<p>Uric acid is a chemical compound produced when the body metabolises <strong>purines</strong>. "
                "Purines occur naturally as part of cell turnover and are also present in foods such as red meat, organ meats, shellfish, and certain legumes. "
                "Under normal circumstances, uric acid travels through the bloodstream, is filtered by the kidneys, and is excreted in urine.</p>"
                "<p>Problems arise when the body produces too much uric acid or the kidneys cannot excrete enough. "
                "The excess can form needle-like monosodium urate crystals that deposit in joints (causing gout) or in the urinary tract (causing kidney stones). "
                "Not everyone with high uric acid develops symptoms, but sustained elevation increases the risk over time.</p>"
                "<p>A uric acid test is a simple blood draw, often ordered alongside kidney function markers such as "
                "<a href=\"/en/blog/creatinine-and-egfr-explained\">creatinine and eGFR</a>. "
                "Interpreting the result requires context: age, sex, diet, medications, and existing conditions all play a role.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal Uric Acid Levels",
            body_html=(
                "<p>Reference ranges may vary slightly between laboratories, but the generally accepted values are shown below:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Group</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Men</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 – 7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 – 6.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>After menopause, women's uric acid levels tend to rise and approach those of men, primarily due to the decline in oestrogen, "
                "which normally promotes uric acid excretion. In children, reference ranges are generally lower.</p>"
                "<p>A single elevated result does not necessarily mean disease, but persistently high levels should be investigated. "
                "Always use the reference range printed on your own lab report and discuss the results with your doctor.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Causes of High Uric Acid (Hyperuricemia)",
            body_html=(
                "<p><strong>Hyperuricemia</strong> can result from increased production of uric acid, decreased excretion, or both. "
                "The most common contributing factors include:</p>"
                "<p><strong>Diet:</strong> A purine-rich diet—organ meats (liver, kidney), red meat, shellfish, sardines, anchovies—drives up uric acid production. "
                "Beverages high in fructose (sweetened soft drinks, fruit juices) and alcohol (especially beer) also raise levels significantly.</p>"
                "<p><strong>Kidney impairment:</strong> When kidney function declines, the kidneys cannot clear uric acid efficiently, leading to accumulation. "
                "Chronic kidney disease is often accompanied by elevated <a href=\"/en/blog/creatinine-and-egfr-explained\">creatinine and reduced eGFR</a>, "
                "and hyperuricemia frequently coexists.</p>"
                "<p><strong>Other factors:</strong> Obesity and insulin resistance, hypertension, hypothyroidism, certain medications "
                "(thiazide diuretics, low-dose aspirin, cyclosporine), genetic predisposition, and conditions that accelerate cell breakdown "
                "(e.g. chemotherapy, tumour lysis syndrome) can all contribute to elevated uric acid.</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="The Link Between Uric Acid and Gout",
            body_html=(
                "<p><strong>Gout</strong> is an inflammatory arthritis caused by the deposition of monosodium urate crystals in joints. "
                "It occurs when blood uric acid levels remain high long enough for crystals to form and trigger an immune response. "
                "The big toe is the most classic site, but gout can also affect the ankles, knees, wrists, and fingers.</p>"
                "<p>A gout attack typically begins suddenly—often at night—with intense pain, swelling, redness, and warmth in the affected joint. "
                "Without treatment, attacks can become more frequent and may lead to chronic joint damage and the formation of tophi "
                "(hard deposits of urate crystals under the skin).</p>"
                "<p>Not everyone with hyperuricemia develops gout; however, the higher and longer the uric acid elevation, the greater the risk. "
                "Diagnosis is not based solely on blood uric acid levels—joint fluid analysis, clinical findings, and imaging are also considered. "
                "If you suspect gout, consulting a rheumatologist is recommended.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Uric Acid and Kidney Stones",
            body_html=(
                "<p>Elevated uric acid can lead to the formation of uric acid crystals in the kidneys, which may grow into stones over time. "
                "Uric acid stones account for approximately 5–10 % of all kidney stones and are more likely to form in acidic urine (pH &lt; 5.5).</p>"
                "<p>Symptoms can include flank or back pain, burning during urination, blood in the urine, and nausea. "
                "Small stones may pass on their own, while larger ones may require medical or surgical intervention such as lithotripsy.</p>"
                "<p>To reduce kidney stone risk, adequate hydration is essential—aim for at least 2–3 litres of water daily. "
                "Dietary adjustments to alkalise the urine and keeping uric acid levels in check are also important. "
                "Monitoring <a href=\"/en/blog/creatinine-and-egfr-explained\">creatinine and eGFR</a> helps assess overall kidney health alongside uric acid.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Diet and Uric Acid: What to Eat and Avoid",
            body_html=(
                "<p>Dietary changes are a cornerstone of uric acid management. A <strong>low-purine diet</strong> means limiting organ meats, "
                "shellfish, anchovies, sardines, and high-fructose beverages while emphasising foods that support healthy uric acid levels.</p>"
                "<p><strong>Recommended foods:</strong> Low-fat dairy products, eggs, whole grains, vegetables (spinach and asparagus can be consumed in moderation), "
                "fruits, and plenty of water. Research suggests that low-fat dairy may actually promote uric acid excretion. "
                "Vitamin C supplementation may also have a mild lowering effect.</p>"
                "<p><strong>Alcohol:</strong> Beer has the highest purine content among alcoholic beverages and raises uric acid levels markedly. "
                "Wine has a smaller effect but should still be consumed in moderation. Even non-alcoholic beer contains purines and warrants caution.</p>"
                "<p><strong>Hydration:</strong> Drinking at least 2–3 litres of water per day helps the kidneys excrete uric acid effectively "
                "and reduces the risk of crystal and stone formation.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medications for High Uric Acid",
            body_html=(
                "<p>When lifestyle changes alone are not sufficient—or when recurrent gout attacks or kidney stones occur—your doctor may prescribe medication. "
                "Uric acid–lowering drugs fall into two main categories:</p>"
                "<p><strong>Xanthine oxidase inhibitors:</strong> Allopurinol and febuxostat reduce uric acid production by blocking the enzyme xanthine oxidase. "
                "These are typically used as long-term maintenance therapy and must be dosed by your doctor.</p>"
                "<p><strong>Uricosuric agents:</strong> Probenecid and lesinurad increase renal excretion of uric acid. "
                "Adequate fluid intake and monitoring of kidney function are important while taking these drugs.</p>"
                "<p>During an acute gout flare, anti-inflammatory medications (NSAIDs), colchicine, or short courses of corticosteroids may be used to manage pain and swelling. "
                "All medication decisions should be made under medical supervision—never adjust doses on your own.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When Should You See a Doctor?",
            body_html=(
                "<p>You should consult a healthcare professional if any of the following apply:</p>"
                "<p>Your blood test shows a uric acid level above the reference range; you experience sudden, severe joint pain, swelling, or redness; "
                "you have symptoms of kidney stones such as flank pain or burning urination; there is a family history of gout or kidney stones; "
                "or your uric acid level remains elevated despite treatment.</p>"
                "<p>High uric acid does not always require medication, but identifying the underlying cause and assessing risk factors through a clinical evaluation is important. "
                "Early detection and lifestyle modifications can make a significant difference in preventing complications like gout and kidney stones.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya Helps You Understand Your Results",
            body_html=(
                "<p>At Norya, we do not diagnose—we help you prepare. "
                "<a href=\"/analyze\">Upload your blood test report</a> and receive a structured, easy-to-understand health summary "
                "that explains your values—including uric acid—in plain language, complete with reference ranges and context, within minutes.</p>"
                "<p>This summary helps you ask the right questions when you meet your doctor and get the most out of your appointment. "
                "For options and pricing, visit our <a href=\"/pricing\">pricing page</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace medical advice or diagnosis.</strong> '
                'Always discuss your results with a healthcare professional. '
                '<a href="/analyze">Start analysis with Norya</a></p>'
            ),
        ),
    ]


def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Ácido úrico: qué significa en su análisis de sangre",
            body_html=(
                "<p>Si su análisis de sangre muestra un nivel anormal de <strong>ácido úrico</strong>, es natural preguntarse qué implica para su salud. "
                "El ácido úrico es un producto de desecho que se forma cuando el cuerpo descompone las purinas, sustancias presentes en ciertos alimentos y en las propias células. "
                "Normalmente, se disuelve en la sangre, pasa por los riñones y se elimina con la orina.</p>"
                "<p>Cuando el ácido úrico se acumula en exceso —un trastorno llamado <em>hiperuricemia</em>— puede provocar gota, cálculos renales y otras complicaciones. "
                "Esta guía explica qué es el ácido úrico, cuáles son los rangos normales, por qué sube y qué puede hacer al respecto. "
                "Su objetivo es prepararle para la consulta con su médico, no sustituir el consejo profesional.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="¿Qué es el ácido úrico?",
            body_html=(
                "<p>El ácido úrico es un compuesto químico que se produce cuando el organismo metaboliza las <strong>purinas</strong>. "
                "Las purinas se generan de forma natural durante la renovación celular y también están presentes en alimentos como la carne roja, "
                "las vísceras, los mariscos y algunas legumbres.</p>"
                "<p>En condiciones normales, el ácido úrico viaja por el torrente sanguíneo, es filtrado por los riñones y se excreta en la orina. "
                "Cuando se produce demasiado o los riñones no lo eliminan correctamente, puede cristalizar en forma de urato monosódico, "
                "depositándose en las articulaciones (gota) o en las vías urinarias (cálculos renales).</p>"
                "<p>La prueba de ácido úrico es una simple extracción de sangre que suele solicitarse junto con marcadores de función renal como "
                "<a href=\"/es/blog/creatinina-y-egfr-que-significan\">creatinina y eGFR</a>. "
                "Para interpretar el resultado se tienen en cuenta la edad, el sexo, la dieta, la medicación y las enfermedades existentes.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de ácido úrico",
            body_html=(
                "<p>Los rangos de referencia pueden variar ligeramente entre laboratorios; los valores generalmente aceptados son:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Grupo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango normal (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hombres</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 – 7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Mujeres</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 – 6,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>Tras la menopausia, los niveles de ácido úrico en mujeres tienden a subir y acercarse a los masculinos, debido a la caída de estrógenos "
                "que normalmente favorece su excreción. En niños, los rangos de referencia suelen ser más bajos.</p>"
                "<p>Un único resultado elevado no siempre significa enfermedad, pero valores persistentemente altos deben investigarse. "
                "Utilice siempre el rango que aparece en su propio informe de laboratorio y coméntelo con su médico.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Causas del ácido úrico alto (hiperuricemia)",
            body_html=(
                "<p>La <strong>hiperuricemia</strong> puede deberse a un aumento en la producción de ácido úrico, una disminución en su excreción o ambos. "
                "Los factores más frecuentes son:</p>"
                "<p><strong>Dieta:</strong> Una alimentación rica en purinas —vísceras, carne roja, mariscos, sardinas, anchoas— incrementa la producción. "
                "Las bebidas con alto contenido de fructosa y el alcohol (sobre todo la cerveza) también elevan los niveles de forma significativa.</p>"
                "<p><strong>Insuficiencia renal:</strong> Cuando la función renal disminuye, los riñones no pueden depurar el ácido úrico de manera eficiente. "
                "La enfermedad renal crónica suele acompañarse de <a href=\"/es/blog/creatinina-y-egfr-que-significan\">creatinina elevada y eGFR reducido</a>.</p>"
                "<p><strong>Otros factores:</strong> Obesidad, resistencia a la insulina, hipertensión, hipotiroidismo, ciertos medicamentos "
                "(diuréticos tiazídicos, aspirina a dosis bajas, ciclosporina), predisposición genética y situaciones de destrucción celular acelerada "
                "(p. ej. quimioterapia, síndrome de lisis tumoral).</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="Relación entre ácido úrico y gota",
            body_html=(
                "<p>La <strong>gota</strong> es una artritis inflamatoria provocada por el depósito de cristales de urato monosódico en las articulaciones. "
                "Aparece cuando el ácido úrico en sangre se mantiene alto el tiempo suficiente para que se formen cristales y desencadenen una respuesta inmunitaria. "
                "La articulación del dedo gordo del pie es la localización más clásica, aunque también puede afectar tobillos, rodillas, muñecas y dedos.</p>"
                "<p>Un ataque de gota suele comenzar de forma repentina —a menudo por la noche— con dolor intenso, hinchazón, enrojecimiento y calor en la articulación afectada. "
                "Sin tratamiento, las crisis pueden hacerse más frecuentes y causar daño articular crónico y formación de tofos.</p>"
                "<p>No todas las personas con hiperuricemia desarrollan gota, pero cuanto más alto y prolongado sea el nivel, mayor será el riesgo. "
                "El diagnóstico no se basa solo en la analítica; también se valora el líquido articular, los hallazgos clínicos y las pruebas de imagen.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Ácido úrico y cálculos renales",
            body_html=(
                "<p>Un nivel elevado de ácido úrico favorece la formación de cristales en los riñones que, con el tiempo, pueden convertirse en piedras. "
                "Los cálculos de ácido úrico representan entre el 5 y el 10 % de todos los cálculos renales y precipitan con mayor facilidad en orina ácida (pH &lt; 5,5).</p>"
                "<p>Los síntomas incluyen dolor en el flanco o la espalda, ardor al orinar, sangre en la orina y náuseas. "
                "Las piedras pequeñas pueden expulsarse solas; las más grandes pueden requerir tratamiento médico o quirúrgico, como la litotricia.</p>"
                "<p>Para reducir el riesgo, es fundamental beber abundante agua (al menos 2-3 litros diarios), seguir pautas dietéticas que alcalinicen la orina "
                "y mantener controlados los niveles de ácido úrico. "
                "El seguimiento de <a href=\"/es/blog/creatinina-y-egfr-que-significan\">creatinina y eGFR</a> es igualmente importante para evaluar la salud renal.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Alimentación y ácido úrico: qué comer y qué evitar",
            body_html=(
                "<p>Los cambios en la alimentación son clave para controlar el ácido úrico. Una <strong>dieta baja en purinas</strong> implica "
                "limitar vísceras, mariscos, anchoas, sardinas y bebidas azucaradas, y priorizar alimentos que favorezcan niveles saludables.</p>"
                "<p><strong>Alimentos recomendados:</strong> Lácteos bajos en grasa, huevos, cereales integrales, verduras (las espinacas y los espárragos pueden consumirse con moderación), "
                "frutas y abundante agua. Estudios sugieren que los lácteos desnatados pueden favorecer la excreción de ácido úrico. "
                "La suplementación con vitamina C puede tener un efecto reductor leve.</p>"
                "<p><strong>Alcohol:</strong> La cerveza es la bebida alcohólica con mayor contenido de purinas y eleva el ácido úrico de forma notable. "
                "El vino tiene menor efecto, pero debe consumirse con moderación. Incluso la cerveza sin alcohol contiene purinas.</p>"
                "<p><strong>Hidratación:</strong> Beber al menos 2-3 litros de agua al día ayuda a los riñones a excretar el ácido úrico y reduce el riesgo de cálculos.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Tratamiento farmacológico del ácido úrico alto",
            body_html=(
                "<p>Cuando los cambios de estilo de vida no bastan, o ante ataques de gota recurrentes o cálculos renales, "
                "el médico puede recetar medicación. Los fármacos se dividen en dos grupos principales:</p>"
                "<p><strong>Inhibidores de la xantina oxidasa:</strong> Alopurinol y febuxostat reducen la producción de ácido úrico al bloquear la enzima xantina oxidasa. "
                "Se usan como tratamiento de mantenimiento a largo plazo y la dosis debe ser ajustada por el médico.</p>"
                "<p><strong>Uricosúricos:</strong> Probenecid y lesinurad aumentan la excreción renal de ácido úrico. "
                "Es importante mantener una buena hidratación y controlar la función renal durante su uso.</p>"
                "<p>Durante una crisis aguda de gota, se emplean antiinflamatorios (AINE), colchicina o ciclos cortos de corticoides para aliviar el dolor y la inflamación. "
                "Toda decisión sobre medicación debe tomarse bajo supervisión médica; nunca ajuste las dosis por su cuenta.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Consulte a un profesional de la salud si se da alguna de estas situaciones:</p>"
                "<p>Su analítica muestra ácido úrico por encima del rango de referencia; experimenta dolor articular intenso, hinchazón o enrojecimiento repentinos; "
                "presenta síntomas de cálculos renales como dolor en el costado o ardor al orinar; tiene antecedentes familiares de gota o cálculos renales; "
                "o su ácido úrico sigue alto a pesar del tratamiento.</p>"
                "<p>Un nivel elevado no siempre requiere medicación, pero es importante investigar la causa subyacente y evaluar los factores de riesgo. "
                "La detección precoz y las modificaciones del estilo de vida pueden marcar una gran diferencia en la prevención de complicaciones.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya le ayuda a entender sus resultados",
            body_html=(
                "<p>En Norya no hacemos diagnósticos; le ayudamos a prepararse. "
                "<a href=\"/analyze\">Suba su informe de análisis de sangre</a> y obtenga un resumen de salud estructurado y fácil de entender "
                "que explica sus valores —incluido el ácido úrico— en lenguaje claro, con rangos de referencia, en pocos minutos.</p>"
                "<p>Con este resumen podrá formular las preguntas adecuadas en la consulta y aprovechar al máximo su cita médica. "
                "Consulte opciones y precios en nuestra <a href=\"/pricing\">página de precios</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> '
                'Consulte siempre sus resultados con un profesional sanitario. '
                '<a href="/analyze">Iniciar análisis con Norya</a></p>'
            ),
        ),
    ]


def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Harnsäure: Was Ihr Blutwert bedeutet",
            body_html=(
                "<p>Zeigt Ihr Blutbild einen auffälligen <strong>Harnsäurewert</strong>, fragen Sie sich vermutlich, was das für Ihre Gesundheit bedeutet. "
                "Harnsäure ist ein natürliches Abbauprodukt, das bei der Verstoffwechselung von Purinen entsteht—Stoffe, die in bestimmten Lebensmitteln und in den eigenen Zellen vorkommen. "
                "Normalerweise löst sich Harnsäure im Blut, wird von den Nieren gefiltert und über den Urin ausgeschieden.</p>"
                "<p>Steigt die Harnsäure dauerhaft an—eine sogenannte <em>Hyperurikämie</em>—kann das zu Gicht, Nierensteinen und weiteren Komplikationen führen. "
                "Dieser Ratgeber erklärt, was Harnsäure ist, welche Werte normal sind, warum sie ansteigt und was Sie tun können. "
                "Er soll Sie auf das Gespräch mit Ihrem Arzt vorbereiten, nicht ärztlichen Rat ersetzen.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="Was ist Harnsäure?",
            body_html=(
                "<p>Harnsäure ist eine chemische Verbindung, die beim Abbau von <strong>Purinen</strong> entsteht. "
                "Purine werden im Rahmen des natürlichen Zellstoffwechsels freigesetzt und sind auch in Lebensmitteln wie rotem Fleisch, Innereien, "
                "Meeresfrüchten und bestimmten Hülsenfrüchten enthalten.</p>"
                "<p>Unter normalen Umständen gelangt die Harnsäure über das Blut zu den Nieren und wird mit dem Urin ausgeschieden. "
                "Wenn der Körper zu viel produziert oder die Nieren zu wenig ausscheiden, kann sich der Überschuss in Form von Mononatriumurat-Kristallen "
                "in Gelenken (Gicht) oder in den Harnwegen (Nierensteine) ablagern.</p>"
                "<p>Die Bestimmung erfolgt über eine einfache Blutentnahme und wird häufig zusammen mit Nierenfunktionswerten wie "
                "<a href=\"/de/blog/kreatinin-und-egfr-erklaert\">Kreatinin und eGFR</a> angeordnet. "
                "Für die korrekte Interpretation spielen Alter, Geschlecht, Ernährung, Medikamente und Vorerkrankungen eine Rolle.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Harnsäurewerte",
            body_html=(
                "<p>Die Referenzbereiche können von Labor zu Labor leicht variieren; allgemein anerkannt sind folgende Werte:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normalbereich (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Männer</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 – 7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Frauen</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 – 6,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>Nach der Menopause steigen die Harnsäurewerte bei Frauen tendenziell an und nähern sich denen von Männern, "
                "da Östrogen—das die Ausscheidung normalerweise fördert—abnimmt. Bei Kindern liegen die Referenzbereiche in der Regel niedriger.</p>"
                "<p>Ein einzelner erhöhter Wert bedeutet nicht zwingend eine Erkrankung, aber dauerhaft hohe Werte sollten abgeklärt werden. "
                "Verwenden Sie stets den Referenzbereich Ihres eigenen Labors und besprechen Sie die Ergebnisse mit Ihrem Arzt.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Ursachen für erhöhte Harnsäure (Hyperurikämie)",
            body_html=(
                "<p>Eine <strong>Hyperurikämie</strong> kann durch vermehrte Harnsäurebildung, verminderte Ausscheidung oder beides entstehen. "
                "Die häufigsten Faktoren sind:</p>"
                "<p><strong>Ernährung:</strong> Purinreiche Kost—Innereien, rotes Fleisch, Meeresfrüchte, Sardinen, Anchovis—steigert die Harnsäureproduktion. "
                "Fruktosehaltige Getränke und Alkohol (besonders Bier) erhöhen den Wert ebenfalls deutlich.</p>"
                "<p><strong>Eingeschränkte Nierenfunktion:</strong> Können die Nieren die Harnsäure nicht effizient ausscheiden, kommt es zur Anhäufung. "
                "Chronische Nierenerkrankung geht oft mit erhöhtem <a href=\"/de/blog/kreatinin-und-egfr-erklaert\">Kreatinin und verringerter eGFR</a> einher.</p>"
                "<p><strong>Weitere Faktoren:</strong> Adipositas, Insulinresistenz, Bluthochdruck, Schilddrüsenunterfunktion, bestimmte Medikamente "
                "(Thiazid-Diuretika, niedrig dosierte Acetylsalicylsäure, Ciclosporin), genetische Veranlagung sowie Zustände mit beschleunigtem Zellabbau "
                "(z. B. Chemotherapie, Tumorlyse-Syndrom).</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="Der Zusammenhang zwischen Harnsäure und Gicht",
            body_html=(
                "<p><strong>Gicht</strong> ist eine entzündliche Arthritis, die durch Ablagerung von Mononatriumurat-Kristallen in Gelenken entsteht. "
                "Sie tritt auf, wenn die Harnsäure im Blut lange genug erhöht bleibt, damit Kristalle entstehen und eine Immunreaktion auslösen. "
                "Der große Zeh ist die klassischste Stelle, aber auch Sprunggelenk, Knie, Handgelenk und Finger können betroffen sein.</p>"
                "<p>Ein Gichtanfall beginnt typischerweise plötzlich—häufig nachts—mit starken Schmerzen, Schwellung, Rötung und Überwärmung im betroffenen Gelenk. "
                "Ohne Behandlung können Anfälle häufiger werden und zu chronischem Gelenkschaden und zur Bildung von Tophi führen.</p>"
                "<p>Nicht jeder mit Hyperurikämie entwickelt Gicht; doch je höher und länger die Erhöhung, desto größer das Risiko. "
                "Die Diagnose stützt sich nicht allein auf den Harnsäurewert—auch Gelenkpunktat, klinische Befunde und Bildgebung werden herangezogen.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Harnsäure und Nierensteine",
            body_html=(
                "<p>Erhöhte Harnsäure kann zur Bildung von Harnsäurekristallen in den Nieren führen, die sich mit der Zeit zu Steinen entwickeln. "
                "Harnsäuresteine machen etwa 5–10 % aller Nierensteine aus und bilden sich bevorzugt in saurem Urin (pH &lt; 5,5).</p>"
                "<p>Symptome können Flanken- oder Rückenschmerzen, Brennen beim Wasserlassen, Blut im Urin und Übelkeit sein. "
                "Kleine Steine können von selbst abgehen; größere erfordern eventuell eine Stoßwellentherapie (Lithotripsie) oder einen operativen Eingriff.</p>"
                "<p>Um das Risiko zu senken, ist ausreichende Flüssigkeitszufuhr entscheidend—mindestens 2–3 Liter Wasser täglich. "
                "Ernährungsumstellungen zur Alkalisierung des Urins und eine Kontrolle der Harnsäurewerte sind ebenso wichtig. "
                "Die Überwachung von <a href=\"/de/blog/kreatinin-und-egfr-erklaert\">Kreatinin und eGFR</a> hilft, die Nierengesundheit insgesamt zu beurteilen.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Ernährung und Harnsäure: Was essen, was meiden?",
            body_html=(
                "<p>Ernährungsänderungen sind ein Grundpfeiler der Harnsäurekontrolle. Eine <strong>purinarme Diät</strong> bedeutet, Innereien, Meeresfrüchte, "
                "Anchovis, Sardinen und fruktosehaltige Getränke einzuschränken und Lebensmittel zu bevorzugen, die gesunde Werte unterstützen.</p>"
                "<p><strong>Empfohlene Lebensmittel:</strong> Fettarme Milchprodukte, Eier, Vollkornprodukte, Gemüse (Spinat und Spargel können in Maßen verzehrt werden), "
                "Obst und reichlich Wasser. Studien deuten darauf hin, dass fettarme Milchprodukte die Harnsäureausscheidung fördern können. "
                "Vitamin-C-Supplemente können einen leicht senkenden Effekt haben.</p>"
                "<p><strong>Alkohol:</strong> Bier hat den höchsten Puringehalt unter den alkoholischen Getränken und hebt den Harnsäurewert deutlich an. "
                "Wein hat einen geringeren Effekt, sollte aber ebenfalls maßvoll getrunken werden. Auch alkoholfreies Bier enthält Purine.</p>"
                "<p><strong>Flüssigkeitszufuhr:</strong> Mindestens 2–3 Liter Wasser täglich helfen den Nieren, Harnsäure wirksam auszuscheiden, "
                "und verringern das Risiko für Kristall- und Steinbildung.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Medikamentöse Behandlung bei erhöhter Harnsäure",
            body_html=(
                "<p>Reichen Lebensstiländerungen nicht aus—oder treten wiederholt Gichtanfälle oder Nierensteine auf—kann der Arzt Medikamente verordnen. "
                "Harnsäuresenkende Mittel lassen sich in zwei Hauptgruppen einteilen:</p>"
                "<p><strong>Xanthinoxidase-Hemmer:</strong> Allopurinol und Febuxostat senken die Harnsäureproduktion, indem sie das Enzym Xanthinoxidase blockieren. "
                "Sie werden in der Regel als Langzeittherapie eingesetzt und vom Arzt dosiert.</p>"
                "<p><strong>Urikosurika:</strong> Probenecid und Lesinurad steigern die renale Harnsäureausscheidung. "
                "Eine ausreichende Trinkmenge und die Überwachung der Nierenfunktion sind bei diesen Medikamenten besonders wichtig.</p>"
                "<p>Während eines akuten Gichtanfalls können entzündungshemmende Medikamente (NSAR), Colchicin oder kurzzeitig Kortikosteroide eingesetzt werden. "
                "Alle Medikamenten-Entscheidungen sollten unter ärztlicher Aufsicht getroffen werden—verstellen Sie die Dosis niemals eigenmächtig.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenden Sie sich an einen Arzt, wenn einer der folgenden Punkte zutrifft:</p>"
                "<p>Ihr Bluttest zeigt einen Harnsäurewert über dem Referenzbereich; Sie haben plötzliche, starke Gelenkschmerzen, Schwellung oder Rötung; "
                "Sie bemerken Symptome von Nierensteinen wie Flankenschmerzen oder Brennen beim Wasserlassen; es gibt eine Familiengeschichte mit Gicht oder Nierensteinen; "
                "oder Ihr Harnsäurewert bleibt trotz Therapie erhöht.</p>"
                "<p>Ein hoher Wert erfordert nicht immer Medikamente, doch die Abklärung der Ursache und die Bewertung der Risikofaktoren "
                "durch eine klinische Untersuchung sind wichtig. Früherkennung und Lebensstilanpassungen können Komplikationen wirksam vorbeugen.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen beim Verstehen hilft",
            body_html=(
                "<p>Bei Norya stellen wir keine Diagnosen—wir helfen Ihnen, sich vorzubereiten. "
                "<a href=\"/analyze\">Laden Sie Ihren Blutbefund hoch</a> und erhalten Sie innerhalb von Minuten eine strukturierte, verständliche Zusammenfassung, "
                "die Ihre Werte—einschließlich Harnsäure—in einfacher Sprache mit Referenzbereichen erklärt.</p>"
                "<p>So können Sie im Arztgespräch die richtigen Fragen stellen und Ihren Termin optimal nutzen. "
                "Optionen und Preise finden Sie auf unserer <a href=\"/pricing\">Preisseite</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> '
                'Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. '
                '<a href="/analyze">Analyse mit Norya starten</a></p>'
            ),
        ),
    ]


def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Acide urique : que signifie votre résultat sanguin ?",
            body_html=(
                "<p>Si votre bilan sanguin révèle un taux anormal d'<strong>acide urique</strong>, il est naturel de vous interroger sur ses implications. "
                "L'acide urique est un déchet naturel produit lorsque l'organisme dégrade les purines, des substances présentes dans certains aliments et dans vos propres cellules. "
                "En temps normal, il se dissout dans le sang, passe par les reins et est éliminé dans les urines.</p>"
                "<p>Lorsque l'acide urique s'accumule — on parle d'<em>hyperuricémie</em> — il peut entraîner la goutte, des calculs rénaux et d'autres complications. "
                "Ce guide explique ce qu'est l'acide urique, quels sont les taux normaux, pourquoi ils augmentent et ce que vous pouvez faire. "
                "Il vise à vous préparer pour votre consultation médicale, pas à remplacer l'avis d'un professionnel.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="Qu'est-ce que l'acide urique ?",
            body_html=(
                "<p>L'acide urique est un composé chimique produit lors du métabolisme des <strong>purines</strong>. "
                "Les purines sont libérées naturellement lors du renouvellement cellulaire et sont également présentes dans la viande rouge, "
                "les abats, les fruits de mer et certaines légumineuses.</p>"
                "<p>Dans des conditions normales, l'acide urique circule dans le sang, est filtré par les reins et excrété dans les urines. "
                "Quand l'organisme en produit trop ou que les reins n'en éliminent pas assez, l'excès peut cristalliser sous forme d'urate monosodique, "
                "se déposant dans les articulations (goutte) ou dans les voies urinaires (calculs rénaux).</p>"
                "<p>Le dosage de l'acide urique se fait par une simple prise de sang, souvent demandée en même temps que des marqueurs de la fonction rénale "
                "comme la <a href=\"/fr/blog/creatinine-et-egfr-expliques\">créatinine et le DFGe</a>. "
                "Son interprétation nécessite de prendre en compte l'âge, le sexe, l'alimentation, les médicaments et les pathologies existantes.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales de l'acide urique",
            body_html=(
                "<p>Les intervalles de référence peuvent varier légèrement d'un laboratoire à l'autre ; les valeurs généralement admises sont :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Groupe</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Plage normale (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Plage normale (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Hommes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 – 7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Femmes</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 – 6,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>Après la ménopause, les taux féminins tendent à se rapprocher de ceux des hommes en raison de la baisse des œstrogènes, "
                "qui favorisent normalement l'excrétion de l'acide urique. Chez l'enfant, les valeurs de référence sont généralement plus basses.</p>"
                "<p>Un résultat isolé élevé ne signifie pas forcément une maladie, mais des taux durablement élevés doivent être explorés. "
                "Utilisez toujours l'intervalle indiqué sur votre propre rapport et discutez-en avec votre médecin.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Causes d'un acide urique élevé (hyperuricémie)",
            body_html=(
                "<p>L'<strong>hyperuricémie</strong> peut résulter d'une production excessive, d'une excrétion insuffisante ou des deux à la fois. "
                "Les principaux facteurs sont :</p>"
                "<p><strong>Alimentation :</strong> Un régime riche en purines — abats, viande rouge, fruits de mer, sardines, anchois — augmente la production. "
                "Les boissons riches en fructose et l'alcool (surtout la bière) élèvent également les taux de façon significative.</p>"
                "<p><strong>Insuffisance rénale :</strong> Lorsque la fonction rénale décline, les reins ne parviennent plus à éliminer efficacement l'acide urique. "
                "L'insuffisance rénale chronique s'accompagne souvent d'une <a href=\"/fr/blog/creatinine-et-egfr-expliques\">créatinine élevée et d'un DFGe réduit</a>.</p>"
                "<p><strong>Autres facteurs :</strong> Obésité, résistance à l'insuline, hypertension, hypothyroïdie, certains médicaments "
                "(diurétiques thiazidiques, aspirine à faible dose, ciclosporine), prédisposition génétique et situations de destruction cellulaire accélérée "
                "(chimiothérapie, syndrome de lyse tumorale).</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="Le lien entre acide urique et goutte",
            body_html=(
                "<p>La <strong>goutte</strong> est une arthrite inflammatoire causée par le dépôt de cristaux d'urate monosodique dans les articulations. "
                "Elle survient lorsque le taux sanguin d'acide urique reste suffisamment élevé pour que des cristaux se forment et déclenchent une réaction immunitaire. "
                "Le gros orteil est le site le plus classique, mais la goutte peut aussi toucher les chevilles, les genoux, les poignets et les doigts.</p>"
                "<p>Une crise de goutte débute en général brutalement — souvent la nuit — avec une douleur intense, un gonflement, une rougeur et une sensation de chaleur "
                "dans l'articulation atteinte. Sans traitement, les crises peuvent devenir plus fréquentes et entraîner des lésions articulaires chroniques et la formation de tophus.</p>"
                "<p>Toutes les personnes présentant une hyperuricémie ne développent pas la goutte, mais plus le taux est élevé et prolongé, plus le risque augmente. "
                "Le diagnostic ne repose pas uniquement sur le taux sanguin ; l'analyse du liquide articulaire, les données cliniques et l'imagerie sont également prises en compte.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Acide urique et calculs rénaux",
            body_html=(
                "<p>Un taux élevé d'acide urique peut favoriser la formation de cristaux dans les reins, susceptibles de se transformer en calculs avec le temps. "
                "Les calculs d'acide urique représentent environ 5 à 10 % de tous les calculs rénaux et se forment plus facilement dans les urines acides (pH &lt; 5,5).</p>"
                "<p>Les symptômes possibles incluent des douleurs lombaires ou dans le flanc, des brûlures à la miction, du sang dans les urines et des nausées. "
                "Les petits calculs peuvent être éliminés spontanément ; les plus gros peuvent nécessiter un traitement médical ou chirurgical (lithotritie).</p>"
                "<p>Pour réduire le risque, il est essentiel de bien s'hydrater — au moins 2 à 3 litres d'eau par jour —, d'adapter son alimentation pour alcaliniser les urines "
                "et de maintenir l'acide urique sous contrôle. "
                "Le suivi de la <a href=\"/fr/blog/creatinine-et-egfr-expliques\">créatinine et du DFGe</a> aide également à évaluer la santé rénale globale.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Alimentation et acide urique : que manger et qu'éviter",
            body_html=(
                "<p>L'alimentation joue un rôle central dans le contrôle de l'acide urique. Un <strong>régime pauvre en purines</strong> consiste à limiter "
                "les abats, fruits de mer, anchois, sardines et boissons sucrées, tout en favorisant les aliments bénéfiques.</p>"
                "<p><strong>Aliments recommandés :</strong> Produits laitiers allégés, œufs, céréales complètes, légumes (les épinards et asperges peuvent être consommés avec modération), "
                "fruits et beaucoup d'eau. Des études suggèrent que les produits laitiers allégés favoriseraient l'excrétion de l'acide urique. "
                "La supplémentation en vitamine C pourrait exercer un léger effet réducteur.</p>"
                "<p><strong>Alcool :</strong> La bière est la boisson alcoolisée la plus riche en purines et élève nettement le taux d'acide urique. "
                "Le vin a un effet moindre mais doit rester modéré. Même la bière sans alcool contient des purines.</p>"
                "<p><strong>Hydratation :</strong> Boire au moins 2 à 3 litres d'eau par jour aide les reins à excréter l'acide urique efficacement "
                "et réduit le risque de cristallisation et de calculs.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Traitements médicamenteux de l'hyperuricémie",
            body_html=(
                "<p>Lorsque les mesures hygiéno-diététiques ne suffisent pas, ou en cas de crises de goutte récurrentes ou de calculs rénaux, "
                "le médecin peut prescrire un traitement. Les médicaments se répartissent en deux grandes catégories :</p>"
                "<p><strong>Inhibiteurs de la xanthine oxydase :</strong> L'allopurinol et le fébuxostat réduisent la production d'acide urique en bloquant l'enzyme xanthine oxydase. "
                "Ils sont généralement utilisés en traitement de fond au long cours et dosés par le médecin.</p>"
                "<p><strong>Uricosuriques :</strong> Le probénécide et le lésinurad augmentent l'excrétion rénale de l'acide urique. "
                "Un apport hydrique suffisant et la surveillance de la fonction rénale sont essentiels avec ces médicaments.</p>"
                "<p>Lors d'une crise aiguë de goutte, des anti-inflammatoires (AINS), de la colchicine ou de courtes cures de corticoïdes peuvent être utilisés. "
                "Toute décision médicamenteuse doit être prise sous supervision médicale — n'ajustez jamais les doses par vous-même.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez un professionnel de santé dans les situations suivantes :</p>"
                "<p>Votre bilan sanguin révèle un acide urique au-dessus de l'intervalle de référence ; vous ressentez une douleur articulaire soudaine et intense, "
                "un gonflement ou une rougeur ; vous présentez des symptômes de calculs rénaux (douleur lombaire, brûlures mictionnelles) ; "
                "il existe des antécédents familiaux de goutte ou de calculs rénaux ; ou votre taux reste élevé malgré un traitement.</p>"
                "<p>Un acide urique élevé ne nécessite pas toujours un médicament, mais il est important d'en rechercher la cause et d'évaluer les facteurs de risque. "
                "Un dépistage précoce et des ajustements du mode de vie peuvent faire une réelle différence dans la prévention des complications.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre vos résultats",
            body_html=(
                "<p>Chez Norya, nous ne posons pas de diagnostic — nous vous aidons à vous préparer. "
                "<a href=\"/analyze\">Téléversez votre bilan sanguin</a> et recevez en quelques minutes un résumé de santé structuré et facile à comprendre "
                "qui explique vos valeurs — dont l'acide urique — en termes simples, avec les intervalles de référence.</p>"
                "<p>Ce résumé vous permet de poser les bonnes questions lors de votre consultation et de tirer le meilleur parti de votre rendez-vous. "
                "Pour les options et les tarifs, consultez notre <a href=\"/pricing\">page tarifs</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> '
                'Discutez toujours de vos résultats avec un professionnel de santé. '
                '<a href="/analyze">Commencer l\'analyse avec Norya</a></p>'
            ),
        ),
    ]


def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Acido urico: cosa significa il risultato delle analisi",
            body_html=(
                "<p>Se le analisi del sangue mostrano un livello anomalo di <strong>acido urico</strong>, è naturale chiedersi cosa significhi per la propria salute. "
                "L'acido urico è un prodotto di scarto che si forma quando l'organismo scompone le purine, sostanze presenti in determinati alimenti e nelle cellule stesse. "
                "In condizioni normali, si scioglie nel sangue, viene filtrato dai reni ed eliminato con le urine.</p>"
                "<p>Quando l'acido urico si accumula in eccesso — una condizione chiamata <em>iperuricemia</em> — può causare gotta, calcoli renali e altre complicanze. "
                "Questa guida spiega cos'è l'acido urico, quali sono i valori normali, perché aumenta e cosa si può fare. "
                "L'obiettivo è prepararvi al colloquio con il medico, non sostituire il parere professionale.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="Cos'è l'acido urico?",
            body_html=(
                "<p>L'acido urico è un composto chimico prodotto dal metabolismo delle <strong>purine</strong>. "
                "Le purine vengono rilasciate naturalmente durante il ricambio cellulare e sono presenti anche in alimenti come carne rossa, "
                "frattaglie, frutti di mare e alcuni legumi.</p>"
                "<p>In condizioni normali, l'acido urico viaggia nel sangue, viene filtrato dai reni e viene escreto nelle urine. "
                "Quando l'organismo ne produce troppo o i reni non ne eliminano a sufficienza, l'eccesso può cristallizzare sotto forma di urato monosodico, "
                "depositandosi nelle articolazioni (gotta) o nelle vie urinarie (calcoli renali).</p>"
                "<p>Il dosaggio dell'acido urico si effettua con un semplice prelievo di sangue, spesso richiesto insieme ai marcatori della funzione renale "
                "come <a href=\"/it/blog/creatinina-e-egfr-spiegati\">creatinina ed eGFR</a>. "
                "L'interpretazione del risultato richiede di considerare età, sesso, alimentazione, farmaci e patologie preesistenti.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali dell'acido urico",
            body_html=(
                "<p>Gli intervalli di riferimento possono variare leggermente tra i laboratori; i valori generalmente accettati sono:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Gruppo</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo normale (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Uomini</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3,4 – 7,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Donne</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,4 – 6,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>Dopo la menopausa, i livelli femminili tendono ad avvicinarsi a quelli maschili a causa del calo degli estrogeni, "
                "che normalmente favoriscono l'escrezione dell'acido urico. Nei bambini, gli intervalli di riferimento sono generalmente più bassi.</p>"
                "<p>Un singolo valore elevato non significa necessariamente malattia, ma livelli persistentemente alti vanno indagati. "
                "Utilizzate sempre l'intervallo riportato sul vostro referto e discutete i risultati con il medico.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="Cause dell'acido urico alto (iperuricemia)",
            body_html=(
                "<p>L'<strong>iperuricemia</strong> può derivare da un aumento della produzione, da una ridotta escrezione o da entrambi. "
                "I fattori più comuni sono:</p>"
                "<p><strong>Alimentazione:</strong> Una dieta ricca di purine — frattaglie, carne rossa, frutti di mare, sardine, acciughe — aumenta la produzione. "
                "Le bevande ricche di fruttosio e l'alcol (soprattutto la birra) innalzano i livelli in modo significativo.</p>"
                "<p><strong>Insufficienza renale:</strong> Quando la funzione renale diminuisce, i reni non riescono a eliminare efficacemente l'acido urico. "
                "La malattia renale cronica è spesso accompagnata da <a href=\"/it/blog/creatinina-e-egfr-spiegati\">creatinina elevata e eGFR ridotto</a>.</p>"
                "<p><strong>Altri fattori:</strong> Obesità, insulino-resistenza, ipertensione, ipotiroidismo, alcuni farmaci "
                "(diuretici tiazidici, aspirina a basso dosaggio, ciclosporina), predisposizione genetica e condizioni di accelerato turnover cellulare "
                "(chemioterapia, sindrome da lisi tumorale).</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="Il legame tra acido urico e gotta",
            body_html=(
                "<p>La <strong>gotta</strong> è un'artrite infiammatoria causata dal deposito di cristalli di urato monosodico nelle articolazioni. "
                "Si verifica quando il livello ematico di acido urico rimane elevato abbastanza a lungo da permettere la formazione di cristalli e scatenare una risposta immunitaria. "
                "L'alluce è la sede più classica, ma possono essere colpite anche caviglie, ginocchia, polsi e dita.</p>"
                "<p>Un attacco di gotta inizia tipicamente all'improvviso — spesso di notte — con dolore intenso, gonfiore, arrossamento e calore nell'articolazione interessata. "
                "Senza trattamento, gli attacchi possono diventare più frequenti e causare danni articolari cronici e formazione di tofi.</p>"
                "<p>Non tutte le persone con iperuricemia sviluppano la gotta, ma più il livello è alto e protratto, maggiore è il rischio. "
                "La diagnosi non si basa solo sull'uricemia: vengono valutati anche il liquido articolare, i riscontri clinici e le indagini di imaging.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="Acido urico e calcoli renali",
            body_html=(
                "<p>Un livello elevato di acido urico può favorire la formazione di cristalli nei reni che, nel tempo, possono trasformarsi in calcoli. "
                "I calcoli di acido urico rappresentano circa il 5-10 % di tutti i calcoli renali e precipitano più facilmente in urine acide (pH &lt; 5,5).</p>"
                "<p>I sintomi possono includere dolore al fianco o alla schiena, bruciore durante la minzione, sangue nelle urine e nausea. "
                "I calcoli piccoli possono essere espulsi spontaneamente; quelli più grandi possono richiedere trattamento medico o chirurgico (litotrissia).</p>"
                "<p>Per ridurre il rischio è fondamentale una buona idratazione — almeno 2-3 litri di acqua al giorno —, adeguamenti dietetici per alcalinizzare le urine "
                "e il controllo dei livelli di acido urico. "
                "Il monitoraggio di <a href=\"/it/blog/creatinina-e-egfr-spiegati\">creatinina ed eGFR</a> è altrettanto importante per valutare la salute renale complessiva.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="Alimentazione e acido urico: cosa mangiare e cosa evitare",
            body_html=(
                "<p>I cambiamenti alimentari sono un pilastro del controllo dell'acido urico. Una <strong>dieta a basso contenuto di purine</strong> prevede "
                "la limitazione di frattaglie, frutti di mare, acciughe, sardine e bevande zuccherate, privilegiando alimenti che favoriscono livelli sani.</p>"
                "<p><strong>Alimenti consigliati:</strong> Latticini a basso contenuto di grassi, uova, cereali integrali, verdure (spinaci e asparagi possono essere consumati con moderazione), "
                "frutta e molta acqua. Studi suggeriscono che i latticini scremati possano promuovere l'escrezione dell'acido urico. "
                "L'integrazione con vitamina C potrebbe avere un lieve effetto riducente.</p>"
                "<p><strong>Alcol:</strong> La birra è la bevanda alcolica con il più alto contenuto di purine e innalza notevolmente l'uricemia. "
                "Il vino ha un effetto minore ma va comunque consumato con moderazione. Anche la birra analcolica contiene purine.</p>"
                "<p><strong>Idratazione:</strong> Bere almeno 2-3 litri di acqua al giorno aiuta i reni a eliminare efficacemente l'acido urico "
                "e riduce il rischio di formazione di cristalli e calcoli.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="Terapia farmacologica per l'acido urico alto",
            body_html=(
                "<p>Quando le modifiche dello stile di vita non bastano, o in caso di attacchi di gotta ricorrenti o calcoli renali, "
                "il medico può prescrivere farmaci. I farmaci ipouricemizzanti si dividono in due categorie principali:</p>"
                "<p><strong>Inibitori della xantina ossidasi:</strong> Allopurinolo e febuxostat riducono la produzione di acido urico bloccando l'enzima xantina ossidasi. "
                "Vengono generalmente utilizzati come terapia di mantenimento a lungo termine e dosati dal medico.</p>"
                "<p><strong>Uricosurici:</strong> Probenecid e lesinurad aumentano l'escrezione renale dell'acido urico. "
                "Durante l'assunzione è importante un adeguato apporto idrico e il monitoraggio della funzione renale.</p>"
                "<p>Durante un attacco acuto di gotta possono essere impiegati antinfiammatori (FANS), colchicina o brevi cicli di corticosteroidi. "
                "Ogni decisione terapeutica deve essere presa sotto supervisione medica — non modificate mai i dosaggi autonomamente.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando rivolgersi al medico?",
            body_html=(
                "<p>Consultate un professionista sanitario se si verifica una delle seguenti situazioni:</p>"
                "<p>Le analisi mostrano un acido urico sopra l'intervallo di riferimento; avvertite dolore articolare improvviso e intenso, gonfiore o arrossamento; "
                "presentate sintomi di calcoli renali come dolore lombare o bruciore alla minzione; avete familiarità per gotta o calcoli renali; "
                "oppure il vostro livello resta elevato nonostante il trattamento.</p>"
                "<p>Un valore alto non richiede sempre farmaci, ma è importante identificare la causa sottostante e valutare i fattori di rischio. "
                "La diagnosi precoce e le modifiche dello stile di vita possono fare una grande differenza nella prevenzione delle complicanze.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya vi aiuta a capire i risultati",
            body_html=(
                "<p>Da Norya non facciamo diagnosi — vi aiutiamo a prepararvi. "
                "<a href=\"/analyze\">Caricate il vostro referto</a> e ricevete in pochi minuti un riepilogo sanitario strutturato e di facile comprensione "
                "che spiega i vostri valori — compreso l'acido urico — in linguaggio semplice, con intervalli di riferimento.</p>"
                "<p>Questo riepilogo vi permette di porre le domande giuste al medico e sfruttare al meglio il vostro appuntamento. "
                "Per opzioni e prezzi, visitate la nostra <a href=\"/pricing\">pagina prezzi</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> '
                'Discutete sempre i risultati con un professionista sanitario. '
                '<a href="/analyze">Inizia l\'analisi con Norya</a></p>'
            ),
        ),
    ]


def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="חומצת שתן: מה המשמעות של תוצאת בדיקת הדם?",
            body_html=(
                "<p>אם בדיקת הדם שלכם מראה רמה חריגה של <strong>חומצת שתן</strong>, טבעי לתהות מה זה אומר על הבריאות שלכם. "
                "חומצת שתן היא תוצר פסולת טבעי הנוצר כאשר הגוף מפרק פורינים — חומרים הנמצאים במאכלים מסוימים ובתאי הגוף עצמם. "
                "בדרך כלל, היא נמסה בדם, עוברת דרך הכליות ומסולקת בשתן.</p>"
                "<p>כאשר חומצת השתן מצטברת — מצב הנקרא <em>היפראוריצמיה</em> — עלולות להופיע סיבוכים כמו שיגדון (גאוט), אבנים בכליות ובעיות נוספות. "
                "מדריך זה מסביר מהי חומצת שתן, מהם הערכים התקינים, מדוע הרמה עולה ומה אפשר לעשות. "
                "המטרה היא להכין אתכם לשיחה עם הרופא, לא להחליף ייעוץ מקצועי.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="מהי חומצת שתן?",
            body_html=(
                "<p>חומצת שתן היא תרכובת כימית הנוצרת כאשר הגוף מפרק <strong>פורינים</strong>. "
                "פורינים משתחררים באופן טבעי כחלק מחידוש התאים ונמצאים גם במאכלים כמו בשר אדום, קרביים, פירות ים וקטניות מסוימות.</p>"
                "<p>בתנאים תקינים, חומצת השתן נעה בזרם הדם, מסוננת על ידי הכליות ומופרשת בשתן. "
                "כאשר הגוף מייצר יותר מדי או שהכליות אינן מפרישות מספיק, העודף עלול להתגבש לגבישי מונוסודיום אוראט, "
                "המתמקמים במפרקים (גאוט) או בדרכי השתן (אבני כליות).</p>"
                "<p>בדיקת חומצת השתן נעשית בדגימת דם פשוטה ולעיתים קרובות מבוצעת יחד עם בדיקות תפקוד כלייתי כמו "
                "<a href=\"/he/blog/creatinine-and-egfr-explained\">קריאטינין ו-eGFR</a>. "
                "פירוש התוצאה מחייב התייחסות לגיל, מין, תזונה, תרופות ומצבים רפואיים קיימים.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכים תקינים של חומצת שתן",
            body_html=(
                "<p>טווחי ההתייחסות עשויים להשתנות מעט בין מעבדות; הערכים המקובלים בדרך כלל הם:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">קבוצה</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">טווח תקין (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">טווח תקין (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">גברים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 – 7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">נשים</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 – 6.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>לאחר גיל המעבר, רמות חומצת השתן בנשים נוטות לעלות ולהתקרב לאלו של גברים, בעיקר בשל ירידה באסטרוגן, "
                "שבמצב רגיל מקדם את הפרשת חומצת השתן. בילדים, טווחי ההתייחסות בדרך כלל נמוכים יותר.</p>"
                "<p>תוצאה מוגברת בודדת אינה בהכרח מעידה על מחלה, אך רמות גבוהות באופן מתמשך מצריכות בירור. "
                "השתמשו תמיד בטווח ההתייחסות שמופיע בדו\"ח המעבדה שלכם ודונו בתוצאות עם הרופא.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="גורמים לחומצת שתן גבוהה (היפראוריצמיה)",
            body_html=(
                "<p><strong>היפראוריצמיה</strong> יכולה לנבוע מייצור מוגבר של חומצת שתן, מהפרשה מופחתת, או משניהם גם יחד. "
                "הגורמים השכיחים ביותר כוללים:</p>"
                "<p><strong>תזונה:</strong> דיאטה עשירה בפורינים — קרביים, בשר אדום, פירות ים, סרדינים, אנשובי — מגבירה את הייצור. "
                "משקאות עשירים בפרוקטוז ואלכוהול (במיוחד בירה) מעלים את הרמות באופן משמעותי.</p>"
                "<p><strong>פגיעה בתפקוד הכלייתי:</strong> כאשר תפקוד הכליות יורד, הכליות אינן מסוגלות לסלק חומצת שתן ביעילות. "
                "מחלת כליות כרונית מלווה לעיתים קרובות בעליית <a href=\"/he/blog/creatinine-and-egfr-explained\">קריאטינין וירידה ב-eGFR</a>.</p>"
                "<p><strong>גורמים נוספים:</strong> השמנה ותנגודת לאינסולין, יתר לחץ דם, תת-פעילות בלוטת התריס, תרופות מסוימות "
                "(משתנים תיאזידיים, אספירין במינון נמוך, ציקלוספורין), נטייה גנטית ומצבים של פירוק תאים מואץ "
                "(כימותרפיה, תסמונת פירוק גידול).</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="הקשר בין חומצת שתן ושיגדון (גאוט)",
            body_html=(
                "<p><strong>שיגדון (גאוט)</strong> הוא דלקת מפרקים דלקתית הנגרמת בשל שקיעת גבישי מונוסודיום אוראט במפרקים. "
                "הוא מתרחש כאשר רמת חומצת השתן בדם נשארת גבוהה מספיק זמן ליצירת גבישים המפעילים תגובה חיסונית. "
                "הבוהן הגדולה היא המקום הקלאסי ביותר, אך גאוט יכול לפגוע גם בקרסוליים, ברכיים, בפרקי כף היד ובאצבעות.</p>"
                "<p>התקף גאוט מתחיל בדרך כלל בפתאומיות — לעיתים קרובות בלילה — עם כאב עז, נפיחות, אדמומיות וחום מקומי במפרק הפגוע. "
                "ללא טיפול, ההתקפים עלולים להתרחש בתדירות גבוהה יותר ולגרום לנזק מפרקי כרוני וליצירת טופי (משקעים קשים של גבישי אוראט מתחת לעור).</p>"
                "<p>לא כל מי שסובל מהיפראוריצמיה מפתח גאוט, אולם ככל שהרמה גבוהה יותר ולאורך זמן — כך הסיכון גדל. "
                "האבחנה אינה מבוססת רק על רמת חומצת שתן בדם; נשקלים גם ניתוח נוזל מפרקי, ממצאים קליניים והדמיה.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="חומצת שתן ואבנים בכליות",
            body_html=(
                "<p>רמה גבוהה של חומצת שתן עלולה לגרום ליצירת גבישים בכליות, שעם הזמן עשויים להפוך לאבנים. "
                "אבני חומצת שתן מהוות כ-5–10% מכלל אבני הכליות ונוטות להיווצר בשתן חומצי (pH &lt; 5.5).</p>"
                "<p>התסמינים עשויים לכלול כאב במותן או בגב, צריבה בזמן מתן שתן, דם בשתן ובחילות. "
                "אבנים קטנות עשויות לצאת בעצמן, בעוד שאבנים גדולות עלולות לדרוש טיפול רפואי או ניתוחי כמו ליתוטריפסיה.</p>"
                "<p>להפחתת הסיכון, שתייה מרובה חיונית — לפחות 2–3 ליטר מים ביום. "
                "שינויים תזונתיים להמרצת pH השתן ושמירה על רמות חומצת שתן תקינות חשובים אף הם. "
                "מעקב אחר <a href=\"/he/blog/creatinine-and-egfr-explained\">קריאטינין ו-eGFR</a> מסייע להעריך את בריאות הכליות הכוללת.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="תזונה וחומצת שתן: מה לאכול ומה להימנע",
            body_html=(
                "<p>שינויים תזונתיים הם אבן יסוד בניהול רמות חומצת שתן. <strong>דיאטה דלת פורינים</strong> משמעה צמצום צריכת קרביים, "
                "פירות ים, אנשובי, סרדינים ומשקאות ממותקים, ובמקביל הדגשת מזונות התומכים ברמות בריאות.</p>"
                "<p><strong>מזונות מומלצים:</strong> מוצרי חלב דלי שומן, ביצים, דגנים מלאים, ירקות (תרד ואספרגוס ניתן לצרוך במתינות), "
                "פירות ומים בשפע. מחקרים מצביעים על כך שמוצרי חלב דלי שומן עשויים לקדם הפרשת חומצת שתן. "
                "תוספי ויטמין C עשויים להשפיע לירידה קלה ברמות.</p>"
                "<p><strong>אלכוהול:</strong> בירה היא המשקה האלכוהולי העשיר ביותר בפורינים ומעלה את רמת חומצת השתן באופן ניכר. "
                "ליין יש השפעה קטנה יותר, אך יש לצרוך אותו במתינות. גם בירה ללא אלכוהול מכילה פורינים.</p>"
                "<p><strong>הידרציה:</strong> שתייה של לפחות 2–3 ליטר מים ביום מסייעת לכליות להפריש חומצת שתן ביעילות "
                "ומפחיתה את הסיכון ליצירת גבישים ואבנים.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="טיפול תרופתי בחומצת שתן גבוהה",
            body_html=(
                "<p>כאשר שינויים באורח החיים אינם מספיקים, או במקרה של התקפי גאוט חוזרים או אבני כליות, "
                "הרופא עשוי לרשום תרופות. תרופות להורדת חומצת שתן מתחלקות לשתי קבוצות עיקריות:</p>"
                "<p><strong>מעכבי קסנטין אוקסידאז:</strong> אלופורינול ופבוקסוסטאט מפחיתים את ייצור חומצת השתן על ידי חסימת האנזים קסנטין אוקסידאז. "
                "הם משמשים בדרך כלל כטיפול תחזוקתי ארוך טווח ומינונם נקבע על ידי הרופא.</p>"
                "<p><strong>תרופות אוריקוזוריות:</strong> פרובנציד ולסינוראד מגבירים את ההפרשה הכלייתית של חומצת שתן. "
                "חשוב להקפיד על שתייה מספקת ולעקוב אחר תפקוד הכליות בזמן הנטילה.</p>"
                "<p>במהלך התקף גאוט חריף ניתן להשתמש בנוגדי דלקת (NSAIDs), קולכיצין או קורסים קצרים של קורטיקוסטרואידים. "
                "כל החלטה תרופתית צריכה להתקבל בפיקוח רפואי — אל תשנו מינונים בעצמכם.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>יש לפנות לאיש מקצוע רפואי אם מתקיים אחד מהמצבים הבאים:</p>"
                "<p>בדיקת הדם מראה חומצת שתן מעל טווח ההתייחסות; אתם חווים כאב מפרקי פתאומי וחמור, נפיחות או אדמומיות; "
                "מופיעים תסמינים של אבני כליות כמו כאב מותני או צריבה במתן שתן; קיימת היסטוריה משפחתית של גאוט או אבני כליות; "
                "או שהרמה נשארת גבוהה למרות טיפול.</p>"
                "<p>חומצת שתן גבוהה לא תמיד מחייבת תרופות, אך חשוב לזהות את הגורם הבסיסי ולהעריך את גורמי הסיכון. "
                "גילוי מוקדם ושינויים באורח החיים יכולים לעשות הבדל משמעותי במניעת סיבוכים כמו גאוט ואבני כליות.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד Norya עוזרת לכם להבין את התוצאות",
            body_html=(
                "<p>ב-Norya אנחנו לא מאבחנים — אנחנו עוזרים לכם להתכונן. "
                "<a href=\"/analyze\">העלו את תוצאות בדיקת הדם שלכם</a> וקבלו תוך דקות סיכום בריאותי מובנה וברור "
                "המסביר את הערכים שלכם — כולל חומצת שתן — בשפה פשוטה, עם טווחי התייחסות.</p>"
                "<p>הסיכום הזה מאפשר לכם לשאול את השאלות הנכונות כשאתם פוגשים את הרופא ולהפיק את המרב מהפגישה. "
                "לאפשרויות ומחירים, בקרו ב<a href=\"/pricing\">עמוד המחירים</a> שלנו.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הודעה",
            body_html=(
                '<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> '
                'דונו תמיד בתוצאות עם איש מקצוע רפואי. '
                '<a href="/analyze">התחל ניתוח עם Norya</a></p>'
            ),
        ),
    ]


def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="यूरिक एसिड: ब्लड टेस्ट रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p>अगर आपकी ब्लड रिपोर्ट में <strong>यूरिक एसिड</strong> का स्तर असामान्य दिख रहा है, तो यह जानना स्वाभाविक है कि इसका सेहत पर क्या असर हो सकता है। "
                "यूरिक एसिड एक प्राकृतिक अपशिष्ट पदार्थ है जो शरीर में प्यूरीन के टूटने से बनता है — प्यूरीन कुछ खाद्य पदार्थों और शरीर की कोशिकाओं में पाए जाते हैं। "
                "सामान्य स्थिति में यह खून में घुला रहता है, किडनी द्वारा छानकर मूत्र में बाहर निकल जाता है।</p>"
                "<p>जब यूरिक एसिड ज़रूरत से ज़्यादा जमा हो जाता है — जिसे <em>हाइपरयूरिसीमिया</em> कहते हैं — तो गाउट (गठिया), "
                "किडनी स्टोन और अन्य जटिलताएँ हो सकती हैं। यह गाइड बताती है कि यूरिक एसिड क्या है, नॉर्मल रेंज क्या होती है, "
                "यह क्यों बढ़ता है और आप क्या कर सकते हैं। उद्देश्य है कि आप डॉक्टर से बात करने के लिए तैयार रहें — यह मेडिकल सलाह का विकल्प नहीं है।</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="यूरिक एसिड क्या है?",
            body_html=(
                "<p>यूरिक एसिड एक रासायनिक यौगिक है जो शरीर में <strong>प्यूरीन</strong> के चयापचय (मेटाबॉलिज़्म) से बनता है। "
                "प्यूरीन कोशिकाओं के प्राकृतिक टर्नओवर के दौरान रिलीज़ होते हैं और रेड मीट, ऑर्गन मीट (कलेजी आदि), शेलफ़िश और कुछ दालों जैसे खाद्य पदार्थों में भी पाए जाते हैं।</p>"
                "<p>सामान्य परिस्थितियों में यूरिक एसिड ब्लडस्ट्रीम में घूमता है, किडनी से फ़िल्टर होता है और मूत्र के ज़रिये बाहर निकलता है। "
                "जब शरीर बहुत ज़्यादा बनाता है या किडनी पर्याप्त मात्रा में नहीं निकाल पाती, तो अतिरिक्त यूरिक एसिड मोनोसोडियम यूरेट क्रिस्टल बनाकर "
                "जोड़ों (गाउट) या मूत्र पथ (किडनी स्टोन) में जमा हो सकता है।</p>"
                "<p>यूरिक एसिड टेस्ट एक साधारण ब्लड टेस्ट है जो अक्सर किडनी फ़ंक्शन मार्कर जैसे "
                "<a href=\"/hi/blog/creatinine-and-egfr-explained\">क्रिएटिनिन और eGFR</a> के साथ करवाया जाता है। "
                "रिज़ल्ट को सही ढंग से समझने के लिए उम्र, लिंग, आहार, दवाइयाँ और मौजूदा बीमारियाँ — सबको ध्यान में रखना ज़रूरी है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="यूरिक एसिड की नॉर्मल रेंज",
            body_html=(
                "<p>रेफरेंस रेंज लैब के अनुसार थोड़ी भिन्न हो सकती है; आम तौर पर स्वीकृत मान नीचे दिए गए हैं:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">समूह</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">नॉर्मल रेंज (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">नॉर्मल रेंज (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">पुरुष</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 – 7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">महिला</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 – 6.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>मेनोपॉज़ के बाद महिलाओं में यूरिक एसिड का स्तर बढ़कर पुरुषों के करीब पहुँच सकता है, क्योंकि एस्ट्रोजन — "
                "जो सामान्यत: यूरिक एसिड के उत्सर्जन में मदद करता है — कम हो जाता है। बच्चों में रेफरेंस रेंज आमतौर पर कम होती है।</p>"
                "<p>एक बार का ऊँचा रिज़ल्ट हमेशा बीमारी नहीं दर्शाता, लेकिन लगातार बना रहने पर जाँच ज़रूरी है। "
                "अपनी रिपोर्ट में दी गई रेफरेंस रेंज का इस्तेमाल करें और रिज़ल्ट पर डॉक्टर से बात करें।</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="यूरिक एसिड बढ़ने के कारण (हाइपरयूरिसीमिया)",
            body_html=(
                "<p><strong>हाइपरयूरिसीमिया</strong> यूरिक एसिड के ज़्यादा बनने, कम निकलने, या दोनों कारणों से हो सकता है। "
                "सबसे आम कारक हैं:</p>"
                "<p><strong>आहार:</strong> प्यूरीन से भरपूर खाद्य पदार्थ — ऑर्गन मीट (कलेजी, गुर्दा), रेड मीट, शेलफ़िश, सार्डिन, एन्कोवी — "
                "यूरिक एसिड उत्पादन बढ़ाते हैं। फ्रुक्टोज़ वाले पेय (सॉफ्ट ड्रिंक्स, फ्रूट जूस) और शराब (ख़ासकर बीयर) भी स्तर काफ़ी बढ़ाते हैं।</p>"
                "<p><strong>किडनी की समस्या:</strong> जब किडनी ठीक से काम नहीं करती, तो वह यूरिक एसिड को पर्याप्त मात्रा में बाहर नहीं निकाल पाती। "
                "क्रोनिक किडनी डिज़ीज़ में <a href=\"/hi/blog/creatinine-and-egfr-explained\">क्रिएटिनिन बढ़ा और eGFR कम</a> होता है, "
                "और हाइपरयूरिसीमिया भी अक्सर साथ में दिखता है।</p>"
                "<p><strong>अन्य कारण:</strong> मोटापा और इंसुलिन रेज़िस्टेंस, हाइपरटेंशन, हाइपोथायरॉइडिज़्म, कुछ दवाइयाँ "
                "(थायज़ाइड डाइयूरेटिक्स, लो-डोज़ एस्पिरिन, साइक्लोस्पोरिन), आनुवंशिक प्रवृत्ति और कोशिका विघटन बढ़ाने वाली स्थितियाँ "
                "(जैसे कीमोथेरेपी, ट्यूमर लाइसिस सिंड्रोम)।</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="यूरिक एसिड और गाउट (गठिया) का संबंध",
            body_html=(
                "<p><strong>गाउट</strong> एक सूजनकारी गठिया (इन्फ्लेमेटरी आर्थराइटिस) है जो जोड़ों में मोनोसोडियम यूरेट क्रिस्टल जमा होने से होता है। "
                "यह तब होता है जब ब्लड में यूरिक एसिड इतने समय तक ऊँचा रहता है कि क्रिस्टल बन जाएँ और इम्यून रिस्पॉन्स शुरू हो। "
                "पैर के अँगूठे का जोड़ सबसे आम जगह है, लेकिन टखना, घुटना, कलाई और उँगलियाँ भी प्रभावित हो सकती हैं।</p>"
                "<p>गाउट का अटैक आमतौर पर अचानक शुरू होता है — अक्सर रात में — प्रभावित जोड़ में तेज़ दर्द, सूजन, लालिमा और गर्माहट के साथ। "
                "इलाज न हो तो अटैक बार-बार आ सकते हैं और जोड़ों को स्थायी नुकसान (टोफ़ाई) हो सकता है।</p>"
                "<p>हाइपरयूरिसीमिया वाले हर व्यक्ति को गाउट नहीं होता, लेकिन जितना ज़्यादा और जितने लंबे समय तक यूरिक एसिड ऊँचा रहे, उतना ख़तरा बढ़ता है। "
                "निदान केवल ब्लड यूरिक एसिड पर आधारित नहीं होता — जॉइंट फ़्लूइड एनालिसिस, क्लिनिकल फ़ाइंडिंग्स और इमेजिंग भी देखी जाती है।</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="यूरिक एसिड और किडनी स्टोन",
            body_html=(
                "<p>यूरिक एसिड की उच्च रमत किडनी में क्रिस्टल बनने का कारण बन सकती है, जो समय के साथ पथरी (स्टोन) में बदल सकते हैं। "
                "यूरिक एसिड स्टोन सभी किडनी स्टोन का लगभग 5–10% होते हैं और अम्लीय मूत्र (pH &lt; 5.5) में अधिक आसानी से बनते हैं।</p>"
                "<p>लक्षणों में कमर या पीठ में दर्द, पेशाब करते समय जलन, पेशाब में ख़ून और मतली शामिल हो सकते हैं। "
                "छोटी पथरी अपने आप निकल सकती है, जबकि बड़ी पथरी के लिए मेडिकल या सर्जिकल ट्रीटमेंट (जैसे लिथोट्रिप्सी) की ज़रूरत पड़ सकती है।</p>"
                "<p>किडनी स्टोन का ख़तरा कम करने के लिए पर्याप्त पानी पीना ज़रूरी है — दिन में कम से कम 2–3 लीटर। "
                "आहार में बदलाव ताकि मूत्र का pH बढ़े और यूरिक एसिड कंट्रोल में रहे, यह भी महत्वपूर्ण है। "
                "<a href=\"/hi/blog/creatinine-and-egfr-explained\">क्रिएटिनिन और eGFR</a> की निगरानी किडनी की समग्र सेहत जानने में मदद करती है।</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="यूरिक एसिड और आहार: क्या खाएँ, क्या बचें",
            body_html=(
                "<p>खान-पान में बदलाव यूरिक एसिड नियंत्रण की आधारशिला है। <strong>लो-प्यूरीन डाइट</strong> का मतलब है — "
                "ऑर्गन मीट, शेलफ़िश, एन्कोवी, सार्डिन और मीठे पेय कम करना और ऐसे खाद्य पदार्थ अपनाना जो स्वस्थ स्तर बनाए रखें।</p>"
                "<p><strong>सुझाए गए खाद्य पदार्थ:</strong> लो-फ़ैट डेयरी, अंडे, साबुत अनाज, सब्ज़ियाँ (पालक और शतावरी सीमित मात्रा में ले सकते हैं), "
                "फल और ख़ूब पानी। शोध बताते हैं कि लो-फ़ैट डेयरी यूरिक एसिड के उत्सर्जन को बढ़ा सकती है। "
                "विटामिन C सप्लीमेंट का भी हल्का कम करने वाला प्रभाव हो सकता है।</p>"
                "<p><strong>शराब:</strong> बीयर सबसे ज़्यादा प्यूरीन वाला अल्कोहलिक ड्रिंक है और यूरिक एसिड को काफ़ी बढ़ाती है। "
                "वाइन का असर कम है लेकिन सीमित ही रखें। नॉन-अल्कोहलिक बीयर में भी प्यूरीन होते हैं।</p>"
                "<p><strong>हाइड्रेशन:</strong> दिन में कम से कम 2–3 लीटर पानी पीना किडनी को यूरिक एसिड प्रभावी ढंग से बाहर निकालने में मदद करता है "
                "और क्रिस्टल व पथरी बनने का ख़तरा कम करता है।</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="यूरिक एसिड बढ़ने पर दवाइयाँ",
            body_html=(
                "<p>जब जीवनशैली में बदलाव अकेले काफ़ी नहीं होते, या बार-बार गाउट अटैक या किडनी स्टोन हो, "
                "तो डॉक्टर दवाई लिख सकते हैं। यूरिक एसिड कम करने वाली दवाइयाँ दो मुख्य श्रेणियों में आती हैं:</p>"
                "<p><strong>ज़ैन्थिन ऑक्सीडेज़ इन्हिबिटर:</strong> एलोप्यूरिनॉल और फ़ेबक्सोस्टैट ज़ैन्थिन ऑक्सीडेज़ एंज़ाइम को ब्लॉक करके यूरिक एसिड उत्पादन घटाते हैं। "
                "ये आमतौर पर लंबे समय तक ली जाने वाली दवाइयाँ हैं और इनकी ख़ुराक डॉक्टर तय करते हैं।</p>"
                "<p><strong>यूरिकोसुरिक एजेंट:</strong> प्रोबेनेसिड और लेसिन्यूरैड किडनी से यूरिक एसिड का उत्सर्जन बढ़ाते हैं। "
                "इन दवाइयों के दौरान पर्याप्त पानी पीना और किडनी फ़ंक्शन की निगरानी रखना ज़रूरी है।</p>"
                "<p>गाउट के तीव्र अटैक में एंटी-इन्फ्लेमेटरी दवाइयाँ (NSAIDs), कोल्चिसिन या शॉर्ट कोर्स कॉर्टिकोस्टेरॉइड्स दर्द और सूजन से राहत दे सकते हैं। "
                "दवाई से जुड़ा हर फ़ैसला डॉक्टर की देखरेख में होना चाहिए — ख़ुद से ख़ुराक न बदलें।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>इनमें से कोई भी स्थिति हो तो स्वास्थ्य विशेषज्ञ से परामर्श लें:</p>"
                "<p>ब्लड टेस्ट में यूरिक एसिड रेफरेंस रेंज से ऊपर है; जोड़ों में अचानक तेज़ दर्द, सूजन या लालिमा है; "
                "कमर दर्द या पेशाब में जलन जैसे किडनी स्टोन के लक्षण हैं; परिवार में गाउट या किडनी स्टोन का इतिहास है; "
                "या इलाज के बावजूद यूरिक एसिड ऊँचा बना हुआ है।</p>"
                "<p>हाई यूरिक एसिड हमेशा दवाई की ज़रूरत नहीं दर्शाता, लेकिन कारण पता करना और जोखिम कारकों का आकलन ज़रूरी है। "
                "जल्दी पता लगाना और जीवनशैली में सुधार, गाउट और किडनी स्टोन जैसी जटिलताओं से बचाने में बड़ा फ़र्क़ ला सकता है।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपकी कैसे मदद करता है",
            body_html=(
                "<p>Norya पर हम निदान नहीं करते — हम आपको डॉक्टर से मिलने के लिए तैयार करते हैं। "
                "<a href=\"/analyze\">अपनी ब्लड टेस्ट रिपोर्ट अपलोड करें</a> और कुछ ही मिनटों में एक स्ट्रक्चर्ड, आसान भाषा में लिखी हेल्थ समरी पाएँ "
                "जो आपकी वैल्यू — यूरिक एसिड सहित — को रेफरेंस रेंज और संदर्भ के साथ समझाती है।</p>"
                "<p>इस समरी से आप डॉक्टर से सही सवाल पूछ सकते हैं और अपनी अपॉइंटमेंट का पूरा फ़ायदा उठा सकते हैं। "
                "विकल्प और कीमतों के लिए <a href=\"/pricing\">प्राइसिंग पेज</a> देखें।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> '
                'अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। '
                '<a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
            ),
        ),
    ]


def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="حمض اليوريك: ماذا تعني نتيجة فحص الدم؟",
            body_html=(
                "<p>إذا أظهر تحليل الدم مستوى غير طبيعي من <strong>حمض اليوريك</strong>، فمن الطبيعي أن تتساءل عمّا يعنيه ذلك لصحتك. "
                "حمض اليوريك هو ناتج فضلات طبيعي يتكوّن عندما يكسر الجسم البيورينات — وهي مواد موجودة في بعض الأطعمة وفي خلايا الجسم نفسه. "
                "في الحالة الطبيعية، يذوب في الدم ويمرّ عبر الكلى ويُطرح مع البول.</p>"
                "<p>عندما يتراكم حمض اليوريك — وهي حالة تُسمى <em>فرط حمض يوريك الدم</em> — يمكن أن يؤدي إلى النقرس وحصوات الكلى ومضاعفات أخرى. "
                "يشرح هذا الدليل ماهية حمض اليوريك والمعدلات الطبيعية وأسباب الارتفاع وما يمكنك فعله. "
                "الهدف هو تحضيرك لمحادثة مع طبيبك، وليس أن يحلّ محلّ المشورة الطبية.</p>"
            ),
        ),
        Section(
            id="what-is-uric-acid", level=2,
            heading="ما هو حمض اليوريك؟",
            body_html=(
                "<p>حمض اليوريك مركّب كيميائي يتكوّن عندما يُستقلب الجسم <strong>البيورينات</strong>. "
                "تُطلق البيورينات بشكل طبيعي أثناء تجدّد الخلايا، وتتواجد أيضاً في أطعمة مثل اللحوم الحمراء والأحشاء والمحار وبعض البقوليات.</p>"
                "<p>في الظروف الطبيعية، ينتقل حمض اليوريك عبر مجرى الدم، تُرشّحه الكلى ويُطرح في البول. "
                "عندما يُنتج الجسم كمية كبيرة جداً أو لا تستطيع الكلى إخراجه بكفاءة، يمكن أن يتبلور الفائض على شكل يورات أحادية الصوديوم، "
                "مترسّباً في المفاصل (النقرس) أو في المسالك البولية (حصوات الكلى).</p>"
                "<p>يتمّ قياس حمض اليوريك بسحب دم بسيط وغالباً يُطلب مع مؤشرات وظائف الكلى مثل "
                "<a href=\"/ar/blog/creatinine-and-egfr-explained\">الكرياتينين ومعدل الترشيح الكبيبي (eGFR)</a>. "
                "يتطلب تفسير النتيجة مراعاة العمر والجنس والنظام الغذائي والأدوية والحالات الصحية القائمة.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدلات الطبيعية لحمض اليوريك",
            body_html=(
                "<p>قد تختلف نطاقات الإسناد قليلاً بين المختبرات؛ القيم المقبولة عموماً هي:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">المجموعة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">النطاق الطبيعي (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">النطاق الطبيعي (µmol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الرجال</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">3.4 – 7.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">200 – 420</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">النساء</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.4 – 6.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">140 – 360</td></tr>'
                "</tbody></table>"
                "<p>بعد انقطاع الطمث، تميل مستويات حمض اليوريك لدى النساء إلى الارتفاع والاقتراب من مستويات الرجال، "
                "ويعود ذلك أساساً إلى انخفاض الإستروجين الذي يعزز عادةً إفراز حمض اليوريك. عند الأطفال، تكون النطاقات المرجعية أقل بشكل عام.</p>"
                "<p>نتيجة واحدة مرتفعة لا تعني بالضرورة مرضاً، لكن المستويات المرتفعة باستمرار يجب أن تُبحث. "
                "استخدم دائماً النطاق المرجعي المطبوع في تقرير مختبرك وناقش النتائج مع طبيبك.</p>"
            ),
        ),
        Section(
            id="high-uric-acid-causes", level=2,
            heading="أسباب ارتفاع حمض اليوريك (فرط حمض يوريك الدم)",
            body_html=(
                "<p>قد ينتج <strong>فرط حمض يوريك الدم</strong> عن زيادة في الإنتاج أو نقص في الإفراز أو كليهما. "
                "أبرز العوامل المسببة:</p>"
                "<p><strong>النظام الغذائي:</strong> الأغذية الغنية بالبيورينات — الأحشاء (الكبد، الكلى)، اللحوم الحمراء، المحار، السردين، الأنشوفة — "
                "تزيد إنتاج حمض اليوريك. المشروبات الغنية بالفركتوز والكحول (خاصة البيرة) ترفع المستويات أيضاً بشكل ملحوظ.</p>"
                "<p><strong>ضعف وظائف الكلى:</strong> عندما تتراجع وظيفة الكلى، لا تستطيع تصفية حمض اليوريك بكفاءة. "
                "مرض الكلى المزمن غالباً يترافق مع ارتفاع <a href=\"/ar/blog/creatinine-and-egfr-explained\">الكرياتينين وانخفاض eGFR</a>.</p>"
                "<p><strong>عوامل أخرى:</strong> السمنة ومقاومة الأنسولين، ارتفاع ضغط الدم، قصور الغدة الدرقية، بعض الأدوية "
                "(مدرّات البول الثيازيدية، الأسبرين بجرعات منخفضة، السيكلوسبورين)، الاستعداد الوراثي والحالات التي تسرّع تحلل الخلايا "
                "(العلاج الكيميائي، متلازمة انحلال الورم).</p>"
            ),
        ),
        Section(
            id="gout-connection", level=2,
            heading="العلاقة بين حمض اليوريك والنقرس",
            body_html=(
                "<p><strong>النقرس</strong> هو التهاب مفصلي ناتج عن ترسّب بلورات يورات أحادية الصوديوم في المفاصل. "
                "يحدث عندما يبقى مستوى حمض اليوريك في الدم مرتفعاً لفترة كافية لتتكوّن البلورات وتُثير استجابة مناعية. "
                "إصبع القدم الكبير هو الموقع الأكثر شيوعاً، لكن النقرس قد يصيب أيضاً الكاحلين والركبتين والمعصمين والأصابع.</p>"
                "<p>تبدأ نوبة النقرس عادةً بشكل مفاجئ — غالباً في الليل — بألم شديد وتورم واحمرار ودفء في المفصل المصاب. "
                "بدون علاج، قد تصبح النوبات أكثر تكراراً وتؤدي إلى تلف مفصلي مزمن وتكوّن التوفات (رواسب صلبة من بلورات اليورات تحت الجلد).</p>"
                "<p>لا يصاب كل من لديه فرط حمض يوريك الدم بالنقرس، لكن كلما ارتفعت الرمة واستمرت لفترة أطول، زاد الخطر. "
                "التشخيص لا يعتمد فقط على مستوى الدم — يُؤخذ في الاعتبار أيضاً تحليل سائل المفصل والموجودات السريرية والتصوير.</p>"
            ),
        ),
        Section(
            id="kidney-stones", level=2,
            heading="حمض اليوريك وحصوات الكلى",
            body_html=(
                "<p>ارتفاع حمض اليوريك قد يؤدي إلى تكوّن بلورات في الكلى يمكن أن تنمو لتصبح حصوات مع الوقت. "
                "تُشكّل حصوات حمض اليوريك نحو 5–10% من جميع حصوات الكلى وتتكوّن بسهولة أكبر في البول الحمضي (pH &lt; 5.5).</p>"
                "<p>قد تشمل الأعراض ألماً في الخاصرة أو الظهر، وحرقة عند التبول، ودماً في البول، وغثياناً. "
                "الحصوات الصغيرة قد تخرج تلقائياً، بينما الأكبر قد تحتاج إلى تدخل طبي أو جراحي مثل التفتيت بالموجات الصادمة.</p>"
                "<p>لتقليل الخطر، يُعدّ الإماهة الكافية أمراً أساسياً — اشرب على الأقل 2–3 لترات من الماء يومياً. "
                "التعديلات الغذائية لقلونة البول والحفاظ على مستوى حمض اليوريك تحت السيطرة مهمان أيضاً. "
                "متابعة <a href=\"/ar/blog/creatinine-and-egfr-explained\">الكرياتينين و eGFR</a> تساعد في تقييم صحة الكلى بشكل شامل.</p>"
            ),
        ),
        Section(
            id="uric-acid-and-diet", level=2,
            heading="النظام الغذائي وحمض اليوريك: ماذا تأكل وماذا تتجنب",
            body_html=(
                "<p>التغييرات الغذائية ركيزة أساسية في إدارة حمض اليوريك. <strong>نظام غذائي قليل البيورينات</strong> يعني الحدّ من الأحشاء "
                "والمحار والأنشوفة والسردين والمشروبات المحلّاة، مع التركيز على الأطعمة التي تدعم مستويات صحية.</p>"
                "<p><strong>الأطعمة الموصى بها:</strong> منتجات الألبان قليلة الدسم، البيض، الحبوب الكاملة، الخضروات (السبانخ والهليون يمكن تناولهما باعتدال)، "
                "الفواكه والكثير من الماء. تشير الأبحاث إلى أن منتجات الألبان قليلة الدسم قد تُعزّز إفراز حمض اليوريك. "
                "مكمّلات فيتامين C قد يكون لها تأثير خافض طفيف.</p>"
                "<p><strong>الكحول:</strong> البيرة هي المشروب الكحولي الأغنى بالبيورينات وترفع مستوى حمض اليوريك بشكل ملحوظ. "
                "النبيذ أقل تأثيراً لكن يجب شربه باعتدال. حتى البيرة الخالية من الكحول تحتوي على بيورينات.</p>"
                "<p><strong>الإماهة:</strong> شرب لترين إلى ثلاثة لترات من الماء يومياً على الأقل يساعد الكلى على طرح حمض اليوريك بفعالية "
                "ويقلّل خطر تكوّن البلورات والحصوات.</p>"
            ),
        ),
        Section(
            id="medications", level=2,
            heading="العلاج الدوائي لارتفاع حمض اليوريك",
            body_html=(
                "<p>عندما لا تكفي تغييرات نمط الحياة وحدها، أو في حالة نوبات نقرس متكررة أو حصوات كلوية، "
                "قد يصف الطبيب أدوية. تنقسم الأدوية الخافضة لحمض اليوريك إلى فئتين رئيسيتين:</p>"
                "<p><strong>مثبّطات أوكسيداز الزانثين:</strong> الوبيورينول وفيبوكسوستات يقلّلان إنتاج حمض اليوريك عن طريق تثبيط إنزيم أوكسيداز الزانثين. "
                "يُستخدمان عادة كعلاج صيانة طويل الأمد بجرعة يحدّدها الطبيب.</p>"
                "<p><strong>الأدوية المدرّة لحمض اليوريك (يوريكوزوريك):</strong> البروبينسيد واللسينوراد يزيدان الإفراز الكلوي لحمض اليوريك. "
                "من الضروري الحفاظ على ترطيب كافٍ ومراقبة وظائف الكلى أثناء تناولها.</p>"
                "<p>خلال نوبة نقرس حادة، قد تُستخدم مضادات الالتهاب (NSAIDs) أو الكولشيسين أو دورات قصيرة من الكورتيكوستيرويدات لتخفيف الألم والتورم. "
                "يجب اتخاذ جميع قرارات العلاج تحت إشراف طبي — لا تعدّل الجرعات بنفسك أبداً.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>استشر مختصاً في الرعاية الصحية إذا انطبق عليك أيٌّ مما يلي:</p>"
                "<p>يُظهر فحص الدم مستوى حمض يوريك أعلى من النطاق المرجعي؛ تشعر بألم مفصلي مفاجئ وشديد أو تورم أو احمرار؛ "
                "لديك أعراض حصوات كلوية كألم الخاصرة أو حرقة التبول؛ هناك تاريخ عائلي بالنقرس أو حصوات الكلى؛ "
                "أو أن مستوى حمض اليوريك يظلّ مرتفعاً رغم العلاج.</p>"
                "<p>لا يستلزم ارتفاع حمض اليوريك دائماً أدوية، لكن تحديد السبب الأساسي وتقييم عوامل الخطر عبر تقييم سريري أمر مهم. "
                "الكشف المبكر وتعديلات نمط الحياة يمكن أن يُحدثا فرقاً كبيراً في الوقاية من المضاعفات كالنقرس وحصوات الكلى.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم نتائجك",
            body_html=(
                "<p>في Norya لا نُشخّص — بل نساعدك على الاستعداد. "
                "<a href=\"/analyze\">ارفع تقرير فحص الدم</a> واحصل خلال دقائق على ملخص صحي منظّم وسهل الفهم "
                "يشرح قيمك — بما فيها حمض اليوريك — بلغة بسيطة مع نطاقات مرجعية.</p>"
                "<p>يساعدك هذا الملخص على طرح الأسئلة الصحيحة عند مقابلة الطبيب والاستفادة القصوى من موعدك. "
                "للخيارات والأسعار، تفضل بزيارة <a href=\"/pricing\">صفحة الأسعار</a>.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> '
                'ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. '
                '<a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


def get_uric_acid_sections_by_lang() -> dict:
    builders = {"tr": _sections_tr, "en": _sections_en, "es": _sections_es, "de": _sections_de, "fr": _sections_fr, "it": _sections_it, "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar}
    return {lang: fn() for lang, fn in builders.items()}


def get_uric_acid_faq_schema_qa() -> dict:
    return {
        "en": [
            {"question": "What is a normal uric acid level?", "answer": "Normal uric acid levels are generally 3.4–7.0 mg/dL for men and 2.4–6.0 mg/dL for women. Ranges may vary slightly between laboratories, and post-menopausal women may have higher levels approaching those of men."},
            {"question": "What causes high uric acid?", "answer": "High uric acid (hyperuricemia) can be caused by a purine-rich diet (organ meats, shellfish, red meat), alcohol (especially beer), obesity, kidney disease, certain medications (diuretics, low-dose aspirin), genetic factors, and conditions that increase cell breakdown."},
            {"question": "What is the connection between uric acid and gout?", "answer": "When blood uric acid stays high for a prolonged time, it can form monosodium urate crystals that deposit in joints, triggering the intense pain and inflammation known as gout. The big toe is the most commonly affected joint."},
            {"question": "Can diet help lower uric acid?", "answer": "Yes. A low-purine diet—limiting organ meats, shellfish, and fructose-sweetened beverages while increasing water intake and low-fat dairy—can help reduce uric acid levels. Vitamin C supplements may also have a mild lowering effect."},
            {"question": "When should I see a doctor about high uric acid?", "answer": "Consult a doctor if your uric acid is above the reference range, you have sudden severe joint pain or swelling, symptoms of kidney stones, a family history of gout, or if levels remain high despite treatment."},
        ],
        "tr": [
            {"question": "Normal ürik asit değeri kaçtır?", "answer": "Ürik asit normal aralığı erkeklerde 3,4–7,0 mg/dL, kadınlarda 2,4–6,0 mg/dL'dir. Laboratuvara göre küçük farklar olabilir; menopoz sonrası kadınlarda değerler erkeklere yaklaşabilir."},
            {"question": "Ürik asit neden yükselir?", "answer": "Hiperürisemi; pürin açısından zengin beslenme (sakatat, kabuklu deniz ürünleri, kırmızı et), alkol (özellikle bira), obezite, böbrek hastalığı, bazı ilaçlar (diüretikler, düşük doz aspirin), genetik faktörler ve hücre yıkımını artıran durumlardan kaynaklanabilir."},
            {"question": "Ürik asit ve gut hastalığı arasındaki ilişki nedir?", "answer": "Kanda ürik asit uzun süre yüksek kaldığında eklemlerde monosodyum ürat kristalleri oluşabilir; bu kristaller şiddetli ağrı ve iltihaplanmaya yol açar — buna gut denir. En sık ayak başparmağı eklemi etkilenir."},
            {"question": "Beslenme ile ürik asit düşürülebilir mi?", "answer": "Evet. Düşük pürinli diyet — sakatat, kabuklu deniz ürünleri ve fruktozlu içecekleri sınırlamak, bol su ve düşük yağlı süt ürünleri tüketmek — ürik asidi düşürmeye yardımcı olabilir. C vitamini takviyesinin de hafif düşürücü etkisi olabilir."},
            {"question": "Ürik asit yüksekliğinde ne zaman doktora gitmeliyim?", "answer": "Ürik asit referans aralığının üzerindeyse, ani şiddetli eklem ağrısı veya şişlik varsa, böbrek taşı belirtileri yaşıyorsanız, ailede gut öyküsü varsa veya tedaviye rağmen değer düşmüyorsa doktora başvurun."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de ácido úrico?", "answer": "Los niveles normales son generalmente 3,4–7,0 mg/dL en hombres y 2,4–6,0 mg/dL en mujeres. Los rangos pueden variar ligeramente entre laboratorios y las mujeres posmenopáusicas pueden tener valores más altos."},
            {"question": "¿Qué causa el ácido úrico alto?", "answer": "La hiperuricemia puede deberse a una dieta rica en purinas (vísceras, mariscos, carne roja), alcohol (sobre todo cerveza), obesidad, enfermedad renal, ciertos medicamentos (diuréticos, aspirina a dosis bajas), factores genéticos y situaciones de destrucción celular acelerada."},
            {"question": "¿Cuál es la relación entre el ácido úrico y la gota?", "answer": "Cuando el ácido úrico permanece alto durante suficiente tiempo, puede formar cristales de urato monosódico que se depositan en las articulaciones, provocando el dolor intenso y la inflamación conocidos como gota. El dedo gordo del pie es la localización más frecuente."},
            {"question": "¿Puede la dieta ayudar a bajar el ácido úrico?", "answer": "Sí. Una dieta baja en purinas — limitando vísceras, mariscos y bebidas azucaradas, aumentando el agua y los lácteos bajos en grasa — puede ayudar a reducir los niveles. Los suplementos de vitamina C también pueden tener un efecto leve."},
        ],
        "de": [
            {"question": "Welcher Harnsäurewert ist normal?", "answer": "Normalwerte liegen bei Männern bei 3,4–7,0 mg/dL und bei Frauen bei 2,4–6,0 mg/dL. Nach der Menopause können die Werte bei Frauen ansteigen und sich den männlichen nähern."},
            {"question": "Was verursacht erhöhte Harnsäure?", "answer": "Hyperurikämie kann durch purinreiche Ernährung (Innereien, Meeresfrüchte, rotes Fleisch), Alkohol (besonders Bier), Adipositas, Nierenerkrankung, bestimmte Medikamente (Diuretika, niedrig dosierte ASS), genetische Veranlagung und beschleunigten Zellabbau verursacht werden."},
            {"question": "Was hat Harnsäure mit Gicht zu tun?", "answer": "Bleibt die Harnsäure dauerhaft erhöht, können sich Mononatriumurat-Kristalle in Gelenken ablagern und die starken Schmerzen und Entzündungen der Gicht auslösen. Der große Zeh ist am häufigsten betroffen."},
            {"question": "Kann die Ernährung die Harnsäure senken?", "answer": "Ja. Eine purinarme Diät — weniger Innereien, Meeresfrüchte und fruktosehaltige Getränke, mehr Wasser und fettarme Milchprodukte — kann helfen. Vitamin-C-Supplemente können einen leicht senkenden Effekt haben."},
        ],
        "fr": [
            {"question": "Quel est le taux normal d'acide urique ?", "answer": "Les taux normaux sont généralement de 3,4 à 7,0 mg/dL chez les hommes et de 2,4 à 6,0 mg/dL chez les femmes. Les valeurs peuvent varier légèrement selon les laboratoires et augmenter chez les femmes ménopausées."},
            {"question": "Quelles sont les causes d'un acide urique élevé ?", "answer": "L'hyperuricémie peut résulter d'une alimentation riche en purines (abats, fruits de mer, viande rouge), de l'alcool (surtout la bière), de l'obésité, d'une insuffisance rénale, de certains médicaments (diurétiques, aspirine à faible dose), de facteurs génétiques et de situations de destruction cellulaire accélérée."},
            {"question": "Quel est le lien entre l'acide urique et la goutte ?", "answer": "Lorsque l'acide urique reste élevé suffisamment longtemps, des cristaux d'urate monosodique se déposent dans les articulations, provoquant la douleur et l'inflammation intenses de la goutte. Le gros orteil est le plus souvent touché."},
            {"question": "L'alimentation peut-elle aider à baisser l'acide urique ?", "answer": "Oui. Un régime pauvre en purines — en limitant abats, fruits de mer et boissons sucrées et en augmentant l'eau et les produits laitiers allégés — peut contribuer à réduire les taux. La vitamine C en complément peut avoir un léger effet réducteur."},
        ],
        "it": [
            {"question": "Qual è il livello normale di acido urico?", "answer": "I valori normali sono generalmente 3,4–7,0 mg/dL per gli uomini e 2,4–6,0 mg/dL per le donne. Gli intervalli possono variare leggermente tra i laboratori e le donne in post-menopausa possono avere valori più alti."},
            {"question": "Quali sono le cause dell'acido urico alto?", "answer": "L'iperuricemia può essere causata da una dieta ricca di purine (frattaglie, frutti di mare, carne rossa), alcol (soprattutto birra), obesità, malattia renale, alcuni farmaci (diuretici, aspirina a basso dosaggio), fattori genetici e condizioni che accelerano il ricambio cellulare."},
            {"question": "Qual è il legame tra acido urico e gotta?", "answer": "Quando l'acido urico resta elevato a lungo, può formare cristalli di urato monosodico che si depositano nelle articolazioni, scatenando il dolore intenso e l'infiammazione tipici della gotta. L'alluce è la sede più comune."},
            {"question": "La dieta può aiutare ad abbassare l'acido urico?", "answer": "Sì. Una dieta a basso contenuto di purine — limitando frattaglie, frutti di mare e bevande zuccherate e aumentando acqua e latticini magri — può contribuire a ridurre i livelli. L'integrazione con vitamina C può avere un lieve effetto riducente."},
        ],
        "he": [
            {"question": "מהו ערך חומצת שתן תקין?", "answer": "ערכים תקינים הם בדרך כלל 3.4–7.0 mg/dL לגברים ו-2.4–6.0 mg/dL לנשים. הטווחים עשויים להשתנות מעט בין מעבדות, ולאחר גיל המעבר ערכי הנשים עשויים להתקרב לאלו של גברים."},
            {"question": "מה גורם לחומצת שתן גבוהה?", "answer": "היפראוריצמיה יכולה לנבוע מתזונה עשירה בפורינים (קרביים, פירות ים, בשר אדום), אלכוהול (בעיקר בירה), השמנה, מחלת כליות, תרופות מסוימות (משתנים, אספירין במינון נמוך), נטייה גנטית ומצבים המגבירים פירוק תאים."},
            {"question": "מה הקשר בין חומצת שתן לגאוט?", "answer": "כאשר חומצת השתן בדם נשארת גבוהה לאורך זמן, עלולים להיווצר גבישי מונוסודיום אוראט המתמקמים במפרקים וגורמים לכאב ודלקת חזקים — שיגדון. המפרק הנפוץ ביותר הוא הבוהן הגדולה."},
            {"question": "האם תזונה יכולה לעזור להוריד חומצת שתן?", "answer": "כן. דיאטה דלת פורינים — צמצום קרביים, פירות ים ומשקאות ממותקים, הגברת שתיית מים ומוצרי חלב דלי שומן — עשויה לסייע. תוספי ויטמין C עשויים גם להשפיע לירידה קלה."},
        ],
        "hi": [
            {"question": "नॉर्मल यूरिक एसिड लेवल कितना होता है?", "answer": "सामान्य मान पुरुषों में 3.4–7.0 mg/dL और महिलाओं में 2.4–6.0 mg/dL होता है। लैब के अनुसार मामूली अंतर हो सकता है; मेनोपॉज़ के बाद महिलाओं में मान पुरुषों के करीब पहुँच सकता है।"},
            {"question": "यूरिक एसिड क्यों बढ़ता है?", "answer": "हाइपरयूरिसीमिया का कारण हो सकता है — प्यूरीन से भरपूर आहार (ऑर्गन मीट, शेलफ़िश, रेड मीट), शराब (विशेषकर बीयर), मोटापा, किडनी की बीमारी, कुछ दवाइयाँ (डाइयूरेटिक्स, लो-डोज़ एस्पिरिन), आनुवंशिक कारण और कोशिका विघटन बढ़ाने वाली स्थितियाँ।"},
            {"question": "यूरिक एसिड और गाउट में क्या संबंध है?", "answer": "जब ब्लड में यूरिक एसिड लंबे समय तक ऊँचा रहता है, तो मोनोसोडियम यूरेट क्रिस्टल बनकर जोड़ों में जमा हो सकते हैं, जिससे तेज़ दर्द और सूजन होती है — इसे गाउट कहते हैं। पैर का अँगूठा सबसे ज़्यादा प्रभावित होता है।"},
            {"question": "क्या डाइट से यूरिक एसिड कम हो सकता है?", "answer": "हाँ। लो-प्यूरीन डाइट — ऑर्गन मीट, शेलफ़िश और मीठे पेय सीमित करना, ख़ूब पानी पीना और लो-फ़ैट डेयरी लेना — मदद कर सकती है। विटामिन C सप्लीमेंट का भी हल्का असर हो सकता है।"},
        ],
        "ar": [
            {"question": "ما هو المستوى الطبيعي لحمض اليوريك؟", "answer": "المعدلات الطبيعية عموماً هي 3.4–7.0 ملغ/ديسيلتر للرجال و2.4–6.0 ملغ/ديسيلتر للنساء. قد تختلف النطاقات قليلاً بين المختبرات، وقد ترتفع عند النساء بعد انقطاع الطمث."},
            {"question": "ما أسباب ارتفاع حمض اليوريك؟", "answer": "قد ينجم فرط حمض يوريك الدم عن نظام غذائي غني بالبيورينات (الأحشاء، المحار، اللحوم الحمراء)، الكحول (خاصة البيرة)، السمنة، أمراض الكلى، بعض الأدوية (المدرّات، الأسبرين بجرعة منخفضة)، عوامل وراثية وحالات تزيد تحلل الخلايا."},
            {"question": "ما العلاقة بين حمض اليوريك والنقرس؟", "answer": "عندما يبقى حمض اليوريك مرتفعاً لفترة كافية، تتكوّن بلورات يورات أحادية الصوديوم تترسّب في المفاصل مسبّبة الألم الشديد والالتهاب المعروف بالنقرس. إصبع القدم الكبير هو الأكثر تأثراً."},
            {"question": "هل يمكن للنظام الغذائي خفض حمض اليوريك؟", "answer": "نعم. نظام غذائي قليل البيورينات — بتقليل الأحشاء والمحار والمشروبات المحلّاة وزيادة شرب الماء ومنتجات الألبان قليلة الدسم — يمكن أن يساعد. مكمّلات فيتامين C قد يكون لها تأثير خافض طفيف."},
        ],
    }
