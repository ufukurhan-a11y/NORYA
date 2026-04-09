# -*- coding: utf-8 -*-
"""
GGT (Gamma-Glutamyl Transferase) blog article — full body content for all 9 languages.
Used by blog_i18n._article_ggt().
Sections: intro, what-is-ggt, normal-ranges, high-ggt-causes, ggt-and-liver,
ggt-and-alcohol, ggt-vs-other-liver-enzymes, when-to-see-doctor,
how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# TURKISH
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="GGT yüksekliği ne anlama gelir? Gamma-Glutamil Transferaz rehberi",
            body_html=(
                "<p><strong>GGT (Gamma-Glutamil Transferaz)</strong>, karaciğer ve safra yolları sağlığını değerlendirmede "
                "kullanılan önemli bir enzimdir. Karaciğer fonksiyon testleri panelinin bir parçası olarak sıklıkla istenir ve "
                "özellikle <strong>alkol kullanımı, karaciğer hastalığı ve safra yolu tıkanıklığı</strong> konusunda yüksek "
                "duyarlılığa sahiptir.</p>"
                "<p>GGT tek başına spesifik bir hastalığa işaret etmez; ancak ALT, AST ve ALP gibi diğer karaciğer enzimleriyle "
                "birlikte değerlendirildiğinde karaciğer patolojisinin türünü ve şiddetini anlamaya yardımcı olur. "
                "Bu rehber, GGT yüksekliğinin olası nedenlerini, diğer karaciğer enzimleriyle ilişkisini ve ne zaman "
                "doktora başvurmanız gerektiğini açıklar.</p>"
                "<p>Bu makale bilgilendirme amaçlıdır ve tıbbi tavsiye yerine geçmez.</p>"
            ),
        ),
        Section(
            id="what-is-ggt", level=2,
            heading="GGT nedir ve vücutta ne işe yarar?",
            body_html=(
                "<p><strong>Gamma-Glutamil Transferaz (GGT)</strong>, hücre zarlarında bulunan ve glutatyon metabolizmasında rol oynayan "
                "bir enzimdir. Aminoasitlerin hücre içine taşınmasını kolaylaştırır ve vücudun en güçlü antioksidanı olan "
                "<strong>glutatyonun</strong> yıkımında anahtar görev üstlenir.</p>"
                "<p>GGT en yüksek konsantrasyonda <strong>karaciğer</strong> ve <strong>safra kanalı</strong> hücrelerinde bulunur; "
                "ayrıca böbrek, pankreas, dalak ve ince bağırsakta da mevcuttur. Ancak kanda ölçülen GGT ağırlıklı olarak "
                "karaciğer kaynaklıdır.</p>"
                "<p>GGT&rsquo;nin klinik önemi, karaciğer ve safra yolu hasarına karşı <strong>son derece duyarlı</strong> olmasıdır. "
                "Hatta diğer karaciğer enzimleri normal iken bile GGT yükselebilir; bu da onu erken dönem karaciğer hasarının "
                "hassas bir göstergesi yapar. Ancak bu yüksek duyarlılık düşük özgüllükle birlikte gelir&mdash;birçok farklı "
                "durum GGT&rsquo;yi yükseltebilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal GGT değerleri",
            body_html=(
                "<p>GGT referans aralıkları cinsiyete ve laboratuvara göre değişir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Cinsiyet</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Erkek</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">8&ndash;61 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Kadın</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">5&ndash;36 U/L</td></tr>'
                "</tbody></table>"
                "<p>GGT düzeyi yaşla birlikte fizyolojik olarak yükselebilir. Ayrıca obezite, metabolik sendrom ve "
                "bazı ilaçlar GGT&rsquo;yi normalin üst sınırına yakın değerlere çıkarabilir. "
                "Tek bir yüksek değer mutlaka patoloji anlamına gelmez; klinik bağlamda değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="high-ggt-causes", level=2,
            heading="GGT yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Yüksek GGT</strong> birçok farklı duruma bağlı olabilir:</p>"
                "<ul>"
                "<li><strong>Karaciğer hastalıkları</strong> &ndash; hepatit (viral, otoimmün, toksik), yağlı karaciğer (steatoz), "
                "siroz, karaciğer tümörleri.</li>"
                "<li><strong>Alkol kullanımı</strong> &ndash; GGT alkole en duyarlı enzimlerden biridir. Düzenli alkol tüketimi "
                "GGT&rsquo;yi diğer karaciğer enzimleri henüz normal iken bile yükseltebilir.</li>"
                "<li><strong>İlaçlar</strong> &ndash; antikonvülzanlar (fenitoin, karbamazepin), NSAİİ&rsquo;ler, bazı antibiyotikler, "
                "statinler ve antiretroviral ilaçlar GGT enzim indüksiyonuna neden olabilir.</li>"
                "<li><strong>Safra yolu tıkanıklığı</strong> &ndash; safra taşları, safra kanalı darlığı veya tümörü. "
                "Bu durumda GGT ve ALP birlikte yükselir.</li>"
                "<li><strong>Pankreatit</strong> &ndash; pankreas karaciğere komşu olduğundan pankreatit GGT&rsquo;yi etkileyebilir.</li>"
                "<li><strong>Kalp yetmezliği</strong> &ndash; sağ kalp yetmezliği karaciğerde konjesyona yol açarak GGT&rsquo;yi artırabilir.</li>"
                "<li><strong>Metabolik sendrom ve obezite</strong> &ndash; non-alkolik yağlı karaciğer hastalığı (NAFLD) ile ilişkili.</li>"
                "</ul>"
                "<p>GGT yüksekliğinin derecesi de önemlidir: hafif yükseklik (normalin 1&ndash;3 katı) genellikle ilaçlar veya "
                "yağlı karaciğer ile ilişkilidir; belirgin yükseklik (&gt;5&times; normal) safra yolu tıkanıklığını "
                "veya ciddi karaciğer hasarını düşündürür.</p>"
            ),
        ),
        Section(
            id="ggt-and-liver", level=2,
            heading="GGT ve karaciğer sağlığı",
            body_html=(
                "<p>GGT, karaciğer hasarının en erken göstergelerinden biridir. <strong>Non-alkolik yağlı karaciğer hastalığı (NAFLD)</strong>, "
                "gelişmiş ülkelerde en yaygın kronik karaciğer hastalığıdır ve genellikle obezite, tip 2 diyabet ve metabolik sendromla "
                "birlikte görülür. NAFLD&rsquo;li hastaların önemli bir kısmında ALT ve AST normal olabilirken GGT yüksek olabilir.</p>"
                "<p>GGT ayrıca karaciğer fibrozisinin ilerleyişiyle de ilişkili bulunmuştur. Bazı araştırmalar yüksek GGT&rsquo;nin "
                "kardiyovasküler hastalık ve tip 2 diyabet riski ile bağımsız bir şekilde ilişkili olduğunu göstermektedir; "
                "bu muhtemelen GGT&rsquo;nin oksidatif stres belirteci olarak rolünden kaynaklanmaktadır.</p>"
                "<p>Karaciğer hastalığı değerlendirmesinde GGT tek başına değil, ALT, AST, ALP, bilirubin ve albümin ile birlikte "
                "yorumlanır. Bu kombine değerlendirme hasarın hepatosellüler (ALT/AST ağırlıklı) mi yoksa kolestatik (ALP/GGT ağırlıklı) "
                "mi olduğunu ayırt etmeye yardımcı olur.</p>"
            ),
        ),
        Section(
            id="ggt-and-alcohol", level=2,
            heading="GGT ve alkol: neden bu kadar duyarlı?",
            body_html=(
                "<p>GGT, alkol tüketiminin en hassas biyokimyasal belirteçlerinden biridir. Düzenli alkol kullanımı (günde 2&ndash;3 "
                "standart içkiden fazla) birkaç hafta içinde GGT&rsquo;yi yükseltebilir. Bu yüksekliğin mekanizması çift yönlüdür:</p>"
                "<ul>"
                "<li><strong>Enzim indüksiyonu</strong> &ndash; alkol, karaciğer hücrelerinde GGT üretimini doğrudan uyarır.</li>"
                "<li><strong>Karaciğer hasarı</strong> &ndash; kronik alkol kullanımı alkolik hepatit ve steatoza yol açar, "
                "bu da hücre hasarıyla GGT salınımını artırır.</li>"
                "</ul>"
                "<p>Alkolün bırakılmasından sonra GGT genellikle 2&ndash;6 hafta içinde normale döner; bu özellik "
                "GGT&rsquo;yi alkol tedavi takibinde kullanışlı bir belirteç yapar. Ancak GGT yalnız başına alkol kullanımını "
                "kanıtlamaz; ilaçlar ve diğer karaciğer hastalıkları da aynı etkiye sahip olabilir.</p>"
                "<p>Alkol bağımlılığı tarama ve izleminde GGT sıklıkla <strong>CDT (karbonhidrat eksik transferrin)</strong> ile birlikte "
                "kullanılır. Her iki belirtecin birlikte yükselmesi kronik ağır alkol kullanımı için daha özgüldür.</p>"
            ),
        ),
        Section(
            id="ggt-vs-other-liver-enzymes", level=2,
            heading="GGT vs. diğer karaciğer enzimleri (ALT, AST, ALP)",
            body_html=(
                "<p>Karaciğer fonksiyon testleri panelinde birden fazla enzim birlikte değerlendirilir. Her birinin farklı klinik anlamı vardır:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Enzim</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Kaynak</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Klinik Anlam</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ALT</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Ağırlıklı karaciğer</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hepatosellüler hasar</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">AST</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Karaciğer, kalp, kas</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hepatosellüler hasar (daha az spesifik)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ALP</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Karaciğer, kemik</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Kolestatik hasar, kemik hastalığı</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">GGT</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Karaciğer, safra yolları</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Kolestaz, alkol, enzim indüksiyonu</td></tr>'
                "</tbody></table>"
                "<p><strong>ALP yüksek + GGT yüksek</strong> = ALP yüksekliğinin karaciğer kaynaklı olduğunu destekler (kemik "
                "değil). <strong>ALP yüksek + GGT normal</strong> = ALP yüksekliği muhtemelen kemik kaynaklıdır "
                "(örneğin büyüme çağı, Paget hastalığı).</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Doktora ne zaman başvurmalısınız?",
            body_html=(
                "<p>GGT yüksekliği saptandığında doktora başvurun, özellikle:</p>"
                "<ul>"
                "<li>GGT normalin 3 katından fazla yüksekse</li>"
                "<li>ALT, AST veya ALP ile birlikte yüksekse</li>"
                "<li>Sarılık (cilt veya gözlerde sararma), koyu idrar veya açık renkli dışkı varsa</li>"
                "<li>Sağ üst karın ağrısı, bulantı veya iştahsızlık yaşıyorsanız</li>"
                "<li>Düzenli alkol kullanım öykünüz varsa</li>"
                "</ul>"
                "<p>İzole hafif GGT yüksekliği sıklıkla ilaç etkisi veya yağlı karaciğer ile ilişkilidir ve panik gerektirmez; "
                "ancak nedeni araştırmak için doktorunuza danışmanız önemlidir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;doktor ziyaretinize hazırlanmanıza yardımcı olur. "
                "Kan tahlili raporunuzu <a href=\"/analyze\">noryaai.com/analyze</a> sayfasına yükleyin; analiz motorumuz "
                "GGT, ALT, AST, ALP, bilirubin ve diğer karaciğer belirteçlerini otomatik olarak çıkarır, referans aralıklarıyla "
                "karşılaştırır ve anlaşılır bir rapor oluşturur.</p>"
                "<p>Abonelik seçenekleri için <a href=\"/pricing\">fiyatlandırma sayfamızı</a> ziyaret edin.</p>"
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


# ---------------------------------------------------------------------------
# ENGLISH
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="High GGT: what does elevated Gamma-Glutamyl Transferase mean?",
            body_html=(
                "<p><strong>GGT (Gamma-Glutamyl Transferase)</strong> is a liver enzyme frequently included in liver function "
                "test panels. It is one of the most sensitive biochemical markers for liver and bile duct disease, and is "
                "particularly responsive to <strong>alcohol use, hepatobiliary disease, and enzyme-inducing medications</strong>.</p>"
                "<p>GGT alone is not specific to any single disease; however, when interpreted alongside ALT, AST, and ALP, "
                "it helps clinicians characterise the type and severity of liver injury. This guide explains what high GGT means, "
                "its relationship with alcohol, how it compares with other liver enzymes, and when to seek medical advice.</p>"
                "<p>This article is educational and does not replace medical advice.</p>"
            ),
        ),
        Section(
            id="what-is-ggt", level=2,
            heading="What is GGT and what does it do?",
            body_html=(
                "<p><strong>Gamma-Glutamyl Transferase (GGT)</strong> is a cell-membrane enzyme involved in glutathione metabolism. "
                "It facilitates the transfer of amino acids across cell membranes and plays a key role in the breakdown of "
                "<strong>glutathione</strong>, the body&rsquo;s most powerful intracellular antioxidant.</p>"
                "<p>GGT is found in highest concentrations in the <strong>liver</strong> and <strong>bile ducts</strong>, "
                "but also in the kidneys, pancreas, spleen, and small intestine. The GGT measured in blood is predominantly "
                "of hepatic origin.</p>"
                "<p>Clinically, GGT is valued because it is <strong>extremely sensitive</strong> to liver and biliary damage&mdash;"
                "it can rise before other liver enzymes become abnormal, making it an early indicator of hepatobiliary injury. "
                "This high sensitivity, however, comes with low specificity: many different conditions can elevate GGT.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal GGT ranges",
            body_html=(
                "<p>GGT reference ranges differ by sex and laboratory:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Sex</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Men</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">8&ndash;61 U/L</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Women</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">5&ndash;36 U/L</td></tr>'
                "</tbody></table>"
                "<p>GGT tends to rise physiologically with age. Obesity, metabolic syndrome, and certain medications can also "
                "push GGT toward the upper end of normal. A single mildly elevated result does not necessarily indicate "
                "pathology and must be interpreted in clinical context.</p>"
            ),
        ),
        Section(
            id="high-ggt-causes", level=2,
            heading="Causes of high GGT",
            body_html=(
                "<p><strong>Elevated GGT</strong> can result from many conditions:</p>"
                "<ul>"
                "<li><strong>Liver disease</strong> &ndash; hepatitis (viral, autoimmune, toxic), fatty liver disease (steatosis), "
                "cirrhosis, and liver tumours.</li>"
                "<li><strong>Alcohol use</strong> &ndash; GGT is one of the most sensitive enzymes to alcohol. Regular consumption "
                "(more than 2&ndash;3 standard drinks per day) can elevate GGT even when other liver enzymes remain normal.</li>"
                "<li><strong>Medications</strong> &ndash; anticonvulsants (phenytoin, carbamazepine), NSAIDs, certain antibiotics, "
                "statins, and antiretrovirals can induce GGT production through hepatic enzyme induction.</li>"
                "<li><strong>Bile duct obstruction</strong> &ndash; gallstones, bile duct strictures, or tumours. In this setting, "
                "GGT and ALP rise together.</li>"
                "<li><strong>Pancreatitis</strong> &ndash; proximity of the pancreas to the liver and bile ducts means pancreatic "
                "inflammation can affect GGT.</li>"
                "<li><strong>Heart failure</strong> &ndash; right-sided heart failure causes hepatic congestion, elevating GGT.</li>"
                "<li><strong>Metabolic syndrome and obesity</strong> &ndash; associated with non-alcoholic fatty liver disease (NAFLD).</li>"
                "</ul>"
                "<p>The magnitude of GGT elevation matters: mild elevation (1&ndash;3&times; normal) often relates to medications "
                "or fatty liver; marked elevation (&gt;5&times; normal) suggests bile duct obstruction or significant liver damage.</p>"
            ),
        ),
        Section(
            id="ggt-and-liver", level=2,
            heading="GGT and liver health",
            body_html=(
                "<p>GGT is one of the earliest markers of liver damage. <strong>Non-alcoholic fatty liver disease (NAFLD)</strong> "
                "is the most common chronic liver disease in developed countries, frequently coexisting with obesity, type 2 diabetes, "
                "and metabolic syndrome. In many NAFLD patients, ALT and AST may be normal while GGT is already elevated.</p>"
                "<p>Research has also linked elevated GGT to increased risk of <strong>cardiovascular disease</strong> and "
                "<strong>type 2 diabetes</strong>, independent of alcohol use. This association may reflect GGT&rsquo;s role as a "
                "marker of oxidative stress and its involvement in glutathione metabolism.</p>"
                "<p>In evaluating liver disease, GGT is interpreted alongside ALT, AST, ALP, bilirubin, and albumin. This combined "
                "assessment helps distinguish hepatocellular injury (ALT/AST predominant) from cholestatic injury "
                "(ALP/GGT predominant).</p>"
            ),
        ),
        Section(
            id="ggt-and-alcohol", level=2,
            heading="GGT and alcohol: why is it so sensitive?",
            body_html=(
                "<p>GGT is one of the most sensitive biochemical markers of alcohol consumption. Regular drinking (more than 2&ndash;3 "
                "standard drinks per day) can elevate GGT within a few weeks. The mechanism is twofold:</p>"
                "<ul>"
                "<li><strong>Enzyme induction</strong> &ndash; alcohol directly stimulates GGT production in hepatocytes.</li>"
                "<li><strong>Liver damage</strong> &ndash; chronic alcohol use causes alcoholic hepatitis and steatosis, leading to "
                "cell damage and GGT release.</li>"
                "</ul>"
                "<p>After alcohol cessation, GGT typically normalises within 2&ndash;6 weeks, making it a useful marker for monitoring "
                "alcohol treatment compliance. However, GGT alone does not prove alcohol use&mdash;medications and other liver diseases "
                "can produce the same effect.</p>"
                "<p>In alcohol dependency screening, GGT is often combined with <strong>CDT (carbohydrate-deficient transferrin)</strong>. "
                "When both markers are elevated together, specificity for chronic heavy alcohol use is substantially higher.</p>"
            ),
        ),
        Section(
            id="ggt-vs-other-liver-enzymes", level=2,
            heading="GGT vs. other liver enzymes (ALT, AST, ALP)",
            body_html=(
                "<p>The liver function test panel includes several enzymes, each with distinct clinical significance:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Enzyme</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Primary Source</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Clinical Significance</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ALT</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Liver (predominantly)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hepatocellular damage</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">AST</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Liver, heart, muscle</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hepatocellular damage (less specific)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ALP</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Liver, bone</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Cholestasis, bone disease</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">GGT</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Liver, bile ducts</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Cholestasis, alcohol, enzyme induction</td></tr>'
                "</tbody></table>"
                "<p><strong>High ALP + high GGT</strong> = supports a hepatic origin for the ALP elevation (not bone). "
                "<strong>High ALP + normal GGT</strong> = the ALP elevation is likely from bone (e.g. growth, Paget disease).</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>See your doctor if your GGT is elevated, especially when:</p>"
                "<ul>"
                "<li>GGT is more than 3 times the upper limit of normal</li>"
                "<li>It is elevated alongside ALT, AST, or ALP</li>"
                "<li>You notice jaundice (yellowing of skin or eyes), dark urine, or pale stools</li>"
                "<li>You have right upper abdominal pain, nausea, or loss of appetite</li>"
                "<li>You have a history of regular alcohol use</li>"
                "</ul>"
                "<p>An isolated mildly elevated GGT is frequently related to medication effects or fatty liver and does not require "
                "panic, but it is important to discuss with your doctor to identify the underlying cause.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare for your doctor visit. Upload your blood test report at "
                "<a href=\"/analyze\">noryaai.com/analyze</a> and our AI engine automatically extracts GGT, ALT, AST, ALP, "
                "bilirubin, and other liver markers, compares them against reference ranges, and generates a clear report.</p>"
                "<p>For subscription options, visit our <a href=\"/pricing\">pricing page</a>.</p>"
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


# ---------------------------------------------------------------------------
# SPANISH
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="GGT alta: ¿qué significa la Gamma-Glutamil Transferasa elevada?",
                body_html="<p>La <strong>GGT (Gamma-Glutamil Transferasa)</strong> es una enzima hepática incluida habitualmente en el panel de función hepática. Es uno de los marcadores más sensibles de enfermedad hepática y biliar, y responde especialmente al <strong>consumo de alcohol, la enfermedad hepatobiliar y ciertos medicamentos</strong>.</p><p>La GGT por sí sola no es específica de una enfermedad; sin embargo, interpretada junto con ALT, AST y ALP, ayuda a caracterizar el tipo y gravedad del daño hepático.</p><p>Esta guía es educativa y no sustituye el consejo médico.</p>"),
        Section(id="what-is-ggt", level=2, heading="¿Qué es la GGT?",
                body_html="<p>La <strong>GGT</strong> es una enzima de membrana celular involucrada en el metabolismo del glutatión, el antioxidante intracelular más potente del cuerpo. Se encuentra en mayor concentración en el <strong>hígado</strong> y los <strong>conductos biliares</strong>. Es extremadamente sensible al daño hepatobiliar, pudiendo elevarse antes que otras enzimas hepáticas.</p>"),
        Section(id="normal-ranges", level=2, heading="Valores normales de GGT",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Sexo</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Rango normal</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Hombres</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">8&ndash;61 U/L</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Mujeres</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">5&ndash;36 U/L</td></tr></tbody></table><p>La GGT aumenta fisiológicamente con la edad. La obesidad, el síndrome metabólico y algunos medicamentos también pueden elevarla.</p>"),
        Section(id="high-ggt-causes", level=2, heading="Causas de GGT alta",
                body_html="<p>Causas frecuentes: enfermedades hepáticas (hepatitis, esteatosis, cirrosis), consumo de alcohol, medicamentos (anticonvulsivos, AINEs, estatinas), obstrucción biliar, pancreatitis, insuficiencia cardíaca y síndrome metabólico/NAFLD. Elevación leve (1&ndash;3&times;) suele asociarse a fármacos o hígado graso; marcada (&gt;5&times;) sugiere obstrucción biliar.</p>"),
        Section(id="ggt-and-liver", level=2, heading="GGT y salud hepática",
                body_html="<p>La GGT es uno de los marcadores más tempranos de daño hepático. En la NAFLD, ALT y AST pueden ser normales mientras que la GGT ya está elevada. Estudios recientes asocian la GGT elevada con riesgo cardiovascular y diabetes tipo 2, posiblemente por su relación con el estrés oxidativo.</p>"),
        Section(id="ggt-and-alcohol", level=2, heading="GGT y alcohol",
                body_html="<p>La GGT es uno de los marcadores más sensibles al alcohol. El consumo regular (&gt;2&ndash;3 bebidas/día) la eleva en semanas mediante inducción enzimática y daño hepático directo. Tras el cese del alcohol, se normaliza en 2&ndash;6 semanas. Se combina con <strong>CDT</strong> para mayor especificidad.</p>"),
        Section(id="ggt-vs-other-liver-enzymes", level=2, heading="GGT vs. otras enzimas hepáticas",
                body_html="<p><strong>ALT</strong>: daño hepatocelular (más específica del hígado). <strong>AST</strong>: hígado, corazón, músculo. <strong>ALP</strong>: colestasis o enfermedad ósea. <strong>GGT</strong>: colestasis, alcohol, inducción enzimática. ALP alta + GGT alta = origen hepático de la ALP. ALP alta + GGT normal = origen óseo probable.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Cuándo consultar al médico",
                body_html="<p>Consulte si la GGT supera 3 veces el límite superior, si se acompaña de ALT/AST/ALP elevadas, ictericia, dolor abdominal derecho o antecedentes de consumo de alcohol.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo ayuda Norya",
                body_html="<p>Suba su análisis en <a href=\"/analyze\">noryaai.com/analyze</a> y nuestra IA extraerá GGT, ALT, AST, ALP, bilirrubina y otros marcadores hepáticos. <a href=\"/pricing\">Página de precios</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="GGT erhöht: Was bedeutet ein hoher Gamma-GT-Wert?",
                body_html="<p>Die <strong>GGT (Gamma-Glutamyl-Transferase)</strong> ist ein Leberenzym, das häufig im Leberfunktionstest bestimmt wird. Sie ist einer der empfindlichsten Marker für Leber- und Gallenwegserkrankungen und reagiert besonders auf <strong>Alkoholkonsum, hepatobiliäre Erkrankungen und enzyminduzierender Medikamente</strong>.</p><p>Die GGT allein ist nicht spezifisch; zusammen mit ALT, AST und ALP hilft sie, Art und Schwere der Leberschädigung einzuordnen.</p><p>Dieser Leitfaden dient der Information und ersetzt keine ärztliche Beratung.</p>"),
        Section(id="what-is-ggt", level=2, heading="Was ist die GGT?",
                body_html="<p>Die <strong>GGT</strong> ist ein Membranenzym des Glutathion-Stoffwechsels. Höchste Konzentration: Leber und Gallenwege. Extrem empfindlich für hepatobiliäre Schäden; kann vor anderen Enzymen ansteigen.</p>"),
        Section(id="normal-ranges", level=2, heading="Normale GGT-Werte",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Geschlecht</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Normalbereich</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Männer</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">8&ndash;61 U/L</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Frauen</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">5&ndash;36 U/L</td></tr></tbody></table><p>GGT steigt physiologisch mit dem Alter. Adipositas und metabolisches Syndrom können ebenfalls zu Erhöhungen führen.</p>"),
        Section(id="high-ggt-causes", level=2, heading="Ursachen für erhöhte GGT",
                body_html="<p>Lebererkrankungen, Alkoholkonsum, Medikamente (Antiepileptika, NSAR, Statine), Gallenwegsobstruktion, Pankreatitis, Herzinsuffizienz und metabolisches Syndrom/NAFLD. Leichte Erhöhung (1&ndash;3&times;): oft Medikamente oder Fettleber. Deutliche Erhöhung (&gt;5&times;): Gallenwegsobstruktion.</p>"),
        Section(id="ggt-and-liver", level=2, heading="GGT und Lebergesundheit",
                body_html="<p>GGT ist ein Frühmarker für Leberschäden. Bei NAFLD können ALT/AST normal sein, während GGT bereits erhöht ist. Erhöhte GGT wurde auch mit kardiovaskulärem Risiko und Typ-2-Diabetes assoziiert.</p>"),
        Section(id="ggt-and-alcohol", level=2, heading="GGT und Alkohol",
                body_html="<p>GGT ist einer der empfindlichsten Alkoholmarker. Regelmäßiger Konsum (&gt;2&ndash;3 Standardgetränke/Tag) erhöht sie innerhalb von Wochen durch Enzyminduktion und Leberzellschaden. Nach Abstinenz normalisiert sie sich in 2&ndash;6 Wochen. Kombiniert mit <strong>CDT</strong> steigt die Spezifität.</p>"),
        Section(id="ggt-vs-other-liver-enzymes", level=2, heading="GGT vs. andere Leberenzyme",
                body_html="<p>ALT: hepatozellulärer Schaden. AST: Leber, Herz, Muskel. ALP: Cholestase, Knochen. GGT: Cholestase, Alkohol, Enzyminduktion. ALP hoch + GGT hoch = hepatischer Ursprung. ALP hoch + GGT normal = wahrscheinlich Knochen.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann zum Arzt?",
                body_html="<p>Suchen Sie einen Arzt auf bei GGT &gt;3&times; Obergrenze, begleitender ALT/AST/ALP-Erhöhung, Gelbsucht, rechtsseitigem Oberbauchschmerz oder Alkoholanamnese.</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie Norya hilft",
                body_html="<p>Laden Sie Ihren Befund unter <a href=\"/analyze\">noryaai.com/analyze</a> hoch. Unsere KI extrahiert GGT, ALT, AST, ALP, Bilirubin und weitere Lebermarker. <a href=\"/pricing\">Preisseite</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="GGT élevée : que signifie la Gamma-Glutamyl Transférase ?",
                body_html="<p>La <strong>GGT (Gamma-Glutamyl Transférase)</strong> est une enzyme hépatique fréquemment dosée dans le bilan hépatique. C&rsquo;est l&rsquo;un des marqueurs les plus sensibles de maladie du foie et des voies biliaires, répondant particulièrement à la <strong>consommation d&rsquo;alcool, aux pathologies hépatobiliaires et à certains médicaments</strong>.</p><p>Ce guide est informatif et ne remplace pas un avis médical.</p>"),
        Section(id="what-is-ggt", level=2, heading="Qu&rsquo;est-ce que la GGT ?",
                body_html="<p>La <strong>GGT</strong> est une enzyme membranaire du métabolisme du glutathion. Concentration la plus élevée : foie et voies biliaires. Extrêmement sensible aux lésions hépatobiliaires, elle peut s&rsquo;élever avant les autres enzymes hépatiques.</p>"),
        Section(id="normal-ranges", level=2, heading="Valeurs normales de la GGT",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Sexe</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Valeur normale</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Hommes</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">8&ndash;61 U/L</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Femmes</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">5&ndash;36 U/L</td></tr></tbody></table><p>La GGT augmente physiologiquement avec l&rsquo;âge. L&rsquo;obésité et le syndrome métabolique peuvent aussi l&rsquo;élever.</p>"),
        Section(id="high-ggt-causes", level=2, heading="Causes de GGT élevée",
                body_html="<p>Maladies hépatiques, alcool, médicaments (antiépileptiques, AINS, statines), obstruction biliaire, pancréatite, insuffisance cardiaque et syndrome métabolique/NAFLD.</p>"),
        Section(id="ggt-and-liver", level=2, heading="GGT et santé du foie",
                body_html="<p>La GGT est un marqueur précoce de lésion hépatique. Dans la NAFLD, elle peut être élevée alors que ALT/AST restent normales. Une GGT élevée est aussi associée au risque cardiovasculaire et au diabète de type 2.</p>"),
        Section(id="ggt-and-alcohol", level=2, heading="GGT et alcool",
                body_html="<p>La GGT est un des marqueurs les plus sensibles de la consommation d&rsquo;alcool. Normalisation en 2&ndash;6 semaines après l&rsquo;arrêt. Combinée au <strong>CDT</strong> pour une spécificité accrue.</p>"),
        Section(id="ggt-vs-other-liver-enzymes", level=2, heading="GGT vs. autres enzymes hépatiques",
                body_html="<p>ALT : lésion hépatocellulaire. AST : foie, cœur, muscle. PAL : cholestase, os. GGT : cholestase, alcool, induction enzymatique. PAL élevée + GGT élevée = origine hépatique. PAL élevée + GGT normale = origine osseuse probable.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter ?",
                body_html="<p>Consultez si la GGT dépasse 3&times; la limite supérieure, si ALT/AST/PAL sont aussi élevées, en cas d&rsquo;ictère ou d&rsquo;antécédents de consommation d&rsquo;alcool.</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment Norya peut vous aider",
                body_html="<p>Téléchargez votre bilan sur <a href=\"/analyze\">noryaai.com/analyze</a>. Notre IA extraira GGT, ALT, AST, PAL, bilirubine et autres marqueurs hépatiques. <a href=\"/pricing\">Page tarifs</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="GGT alta: cosa significa la Gamma-Glutamil Transferasi elevata?",
                body_html="<p>La <strong>GGT (Gamma-Glutamil Transferasi)</strong> è un enzima epatico frequentemente incluso nel pannello epatico. È uno dei marcatori più sensibili di malattia epatica e biliare, particolarmente reattivo a <strong>alcol, patologia epatobiliare e farmaci induttori enzimatici</strong>.</p><p>Questa guida è informativa e non sostituisce il parere medico.</p>"),
        Section(id="what-is-ggt", level=2, heading="Cos&rsquo;è la GGT?",
                body_html="<p>La <strong>GGT</strong> è un enzima di membrana coinvolto nel metabolismo del glutatione. Massima concentrazione: fegato e vie biliari. Estremamente sensibile al danno epatobiliare.</p>"),
        Section(id="normal-ranges", level=2, heading="Valori normali della GGT",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Sesso</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Intervallo normale</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Uomini</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">8&ndash;61 U/L</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Donne</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">5&ndash;36 U/L</td></tr></tbody></table><p>La GGT aumenta fisiologicamente con l&rsquo;età. Obesità e sindrome metabolica possono elevarla.</p>"),
        Section(id="high-ggt-causes", level=2, heading="Cause di GGT alta",
                body_html="<p>Epatopatie, alcol, farmaci (antiepilettici, FANS, statine), ostruzione biliare, pancreatite, insufficienza cardiaca e sindrome metabolica/NAFLD.</p>"),
        Section(id="ggt-and-liver", level=2, heading="GGT e salute del fegato",
                body_html="<p>La GGT è un marcatore precoce di danno epatico. Nella NAFLD può essere elevata con ALT/AST normali. Associata anche a rischio cardiovascolare e diabete tipo 2.</p>"),
        Section(id="ggt-and-alcohol", level=2, heading="GGT e alcol",
                body_html="<p>La GGT è uno dei marcatori più sensibili al consumo di alcol. Si normalizza in 2&ndash;6 settimane dopo la sospensione. Combinata con <strong>CDT</strong> per maggiore specificità.</p>"),
        Section(id="ggt-vs-other-liver-enzymes", level=2, heading="GGT vs. altri enzimi epatici",
                body_html="<p>ALT: danno epatocellulare. AST: fegato, cuore, muscolo. ALP: colestasi, osso. GGT: colestasi, alcol, induzione enzimatica. ALP alta + GGT alta = origine epatica. ALP alta + GGT normale = probabile origine ossea.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico",
                body_html="<p>Consultate il medico se la GGT supera 3&times; il limite superiore, se ALT/AST/ALP sono elevate, in caso di ittero o anamnesi di consumo di alcol.</p>"),
        Section(id="how-norya-helps", level=2, heading="Come Norya può aiutarti",
                body_html="<p>Caricate il vostro esame su <a href=\"/analyze\">noryaai.com/analyze</a>. La nostra IA estrarrà GGT, ALT, AST, ALP, bilirubina e altri marcatori epatici. <a href=\"/pricing\">Pagina prezzi</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="GGT גבוה: מה המשמעות של גמא-גלוטמיל טרנספראז מוגבה?",
                body_html="<p><strong>GGT (גמא-גלוטמיל טרנספראז)</strong> הוא אנזים כבד הנכלל לעיתים קרובות בפאנל תפקודי כבד. הוא אחד הסמנים הרגישים ביותר למחלות כבד ודרכי מרה, ומגיב במיוחד ל<strong>צריכת אלכוהול, מחלות הפטוביליאריות ותרופות מעוררות אנזים</strong>.</p><p>מדריך זה חינוכי בלבד ואינו מחליף ייעוץ רפואי.</p>"),
        Section(id="what-is-ggt", level=2, heading="מהו GGT?",
                body_html="<p><strong>GGT</strong> הוא אנזים ממברנלי המעורב במטבוליזם של גלוטתיון. ריכוז מרבי: כבד ודרכי מרה. רגיש במיוחד לנזק הפטוביליארי.</p>"),
        Section(id="normal-ranges", level=2, heading="טווחי GGT תקינים",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">מין</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">טווח תקין</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">גברים</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">8&ndash;61 U/L</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">נשים</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">5&ndash;36 U/L</td></tr></tbody></table><p>GGT עולה פיזיולוגית עם הגיל. השמנה ותסמונת מטבולית עלולות להעלותו.</p>"),
        Section(id="high-ggt-causes", level=2, heading="גורמים ל-GGT גבוה",
                body_html="<p>מחלות כבד, אלכוהול, תרופות (נוגדי פרכוס, NSAIDs, סטטינים), חסימת דרכי מרה, דלקת לבלב, אי-ספיקת לב ותסמונת מטבולית/NAFLD.</p>"),
        Section(id="ggt-and-liver", level=2, heading="GGT ובריאות הכבד",
                body_html="<p>GGT הוא סמן מוקדם לנזק כבדי. ב-NAFLD הוא עלול להיות מוגבה כש-ALT/AST תקינים. GGT מוגבה קשור גם לסיכון קרדיווסקולרי וסוכרת סוג 2.</p>"),
        Section(id="ggt-and-alcohol", level=2, heading="GGT ואלכוהול",
                body_html="<p>GGT הוא מהסמנים הרגישים ביותר לצריכת אלכוהול. מתנרמל תוך 2&ndash;6 שבועות לאחר הפסקה. משולב עם <strong>CDT</strong> לספציפיות גבוהה יותר.</p>"),
        Section(id="ggt-vs-other-liver-enzymes", level=2, heading="GGT מול אנזימי כבד אחרים",
                body_html="<p>ALT: נזק הפטוצלולרי. AST: כבד, לב, שריר. ALP: כולסטאזיס, עצם. GGT: כולסטאזיס, אלכוהול, אינדוקציה. ALP גבוה + GGT גבוה = מקור כבדי. ALP גבוה + GGT תקין = מקור עצמי סביר.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא?",
                body_html="<p>פנו לרופא אם GGT מעל פי 3 מהגבול העליון, אם ALT/AST/ALP גם מוגבהים, בצהבת או באנמנזה של צריכת אלכוהול.</p>"),
        Section(id="how-norya-helps", level=2, heading="איך Norya עוזרת",
                body_html="<p>העלו את הבדיקה ב-<a href=\"/analyze\">noryaai.com/analyze</a>. ה-AI שלנו יחלץ GGT, ALT, AST, ALP, בילירובין ועוד. <a href=\"/pricing\">עמוד תמחור</a>.</p>"),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="GGT उच्च: गामा-ग्लूटामिल ट्रांसफ़ेरेज़ बढ़ने का क्या मतलब है?",
                body_html="<p><strong>GGT (गामा-ग्लूटामिल ट्रांसफ़ेरेज़)</strong> एक यकृत एंज़ाइम है जो लिवर फ़ंक्शन टेस्ट पैनल में शामिल होता है। यह लिवर और पित्त नली की बीमारी के सबसे संवेदनशील मार्करों में से एक है, विशेषकर <strong>शराब, हेपेटोबिलियरी रोग और एंज़ाइम-इंड्यूसिंग दवाओं</strong> के प्रति।</p><p>यह गाइड शैक्षणिक है और चिकित्सा सलाह का विकल्प नहीं है।</p>"),
        Section(id="what-is-ggt", level=2, heading="GGT क्या है?",
                body_html="<p><strong>GGT</strong> ग्लूटाथायोन मेटाबॉलिज़्म में शामिल एक मेम्ब्रेन एंज़ाइम है। सर्वाधिक सांद्रता: यकृत और पित्त नलिकाएँ। हेपेटोबिलियरी क्षति के प्रति अत्यंत संवेदनशील।</p>"),
        Section(id="normal-ranges", level=2, heading="सामान्य GGT मान",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">लिंग</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">सामान्य सीमा</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">पुरुष</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">8&ndash;61 U/L</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">महिला</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">5&ndash;36 U/L</td></tr></tbody></table><p>GGT उम्र के साथ शारीरिक रूप से बढ़ सकता है। मोटापा और मेटाबॉलिक सिंड्रोम भी इसे बढ़ा सकते हैं।</p>"),
        Section(id="high-ggt-causes", level=2, heading="GGT बढ़ने के कारण",
                body_html="<p>यकृत रोग, शराब, दवाएँ (एंटीकॉन्वल्सेंट, NSAIDs, स्टैटिन), पित्त नली अवरोध, अग्नाशयशोथ, हृदय विफलता और मेटाबॉलिक सिंड्रोम/NAFLD।</p>"),
        Section(id="ggt-and-liver", level=2, heading="GGT और लिवर स्वास्थ्य",
                body_html="<p>GGT लिवर क्षति का प्रारंभिक मार्कर है। NAFLD में ALT/AST सामान्य हो सकते हैं जबकि GGT पहले से बढ़ा होता है। उच्च GGT हृदय रोग और टाइप 2 डायबिटीज़ जोखिम से भी जुड़ा है।</p>"),
        Section(id="ggt-and-alcohol", level=2, heading="GGT और शराब",
                body_html="<p>GGT शराब सेवन के सबसे संवेदनशील मार्करों में से एक है। छोड़ने के 2&ndash;6 सप्ताह में सामान्य हो जाता है। <strong>CDT</strong> के साथ मिलाकर अधिक विशिष्टता।</p>"),
        Section(id="ggt-vs-other-liver-enzymes", level=2, heading="GGT बनाम अन्य लिवर एंज़ाइम",
                body_html="<p>ALT: हेपेटोसेल्युलर क्षति। AST: लिवर, हृदय, मांसपेशी। ALP: कोलेस्टेसिस, हड्डी। GGT: कोलेस्टेसिस, शराब, एंज़ाइम इंडक्शन। ALP उच्च + GGT उच्च = यकृत स्रोत। ALP उच्च + GGT सामान्य = हड्डी स्रोत।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें?",
                body_html="<p>GGT सामान्य सीमा से 3 गुना अधिक होने, ALT/AST/ALP भी बढ़े होने, पीलिया या शराब सेवन इतिहास होने पर डॉक्टर से मिलें।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya कैसे मदद करता है",
                body_html="<p>अपनी रिपोर्ट <a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें। हमारा AI GGT, ALT, AST, ALP, बिलीरुबिन और अन्य लिवर मार्कर निकालेगा। <a href=\"/pricing\">मूल्य निर्धारण</a>।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="GGT مرتفع: ماذا يعني ارتفاع غاما-غلوتاميل ترانسفيراز؟",
                body_html="<p><strong>GGT (غاما-غلوتاميل ترانسفيراز)</strong> إنزيم كبدي يُطلب كجزء من فحوصات وظائف الكبد. يُعدّ من أكثر المؤشرات حساسية لأمراض الكبد والقنوات الصفراوية، ويستجيب بشكل خاص <strong>للكحول والأمراض الكبدية الصفراوية والأدوية المحفّزة للإنزيمات</strong>.</p><p>هذا الدليل تثقيفي ولا يحل محل الاستشارة الطبية.</p>"),
        Section(id="what-is-ggt", level=2, heading="ما هو GGT؟",
                body_html="<p><strong>GGT</strong> إنزيم غشائي مشارك في أيض الغلوتاثيون. أعلى تركيز: الكبد والقنوات الصفراوية. حساس للغاية للضرر الكبدي الصفراوي.</p>"),
        Section(id="normal-ranges", level=2, heading="المعدلات الطبيعية لـ GGT",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">الجنس</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">الطبيعي</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">رجال</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">8&ndash;61 U/L</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">نساء</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">5&ndash;36 U/L</td></tr></tbody></table><p>يرتفع GGT فسيولوجياً مع العمر. السمنة والمتلازمة الأيضية قد ترفعه أيضاً.</p>"),
        Section(id="high-ggt-causes", level=2, heading="أسباب ارتفاع GGT",
                body_html="<p>أمراض كبدية، كحول، أدوية (مضادات صرع، مضادات التهاب، ستاتينات)، انسداد صفراوي، التهاب بنكرياس، قصور قلب ومتلازمة أيضية/NAFLD.</p>"),
        Section(id="ggt-and-liver", level=2, heading="GGT وصحة الكبد",
                body_html="<p>GGT مؤشر مبكر لتلف الكبد. في NAFLD قد يرتفع بينما ALT/AST طبيعيان. يرتبط أيضاً بالخطر القلبي الوعائي والسكري النوع 2.</p>"),
        Section(id="ggt-and-alcohol", level=2, heading="GGT والكحول",
                body_html="<p>GGT من أكثر المؤشرات حساسية للكحول. يعود طبيعياً خلال 2&ndash;6 أسابيع بعد التوقف. يُدمج مع <strong>CDT</strong> لنوعية أعلى.</p>"),
        Section(id="ggt-vs-other-liver-enzymes", level=2, heading="GGT مقابل إنزيمات الكبد الأخرى",
                body_html="<p>ALT: ضرر كبدي خلوي. AST: كبد، قلب، عضلات. ALP: ركود صفراوي، عظام. GGT: ركود صفراوي، كحول، تحفيز إنزيمي. ALP مرتفع + GGT مرتفع = أصل كبدي. ALP مرتفع + GGT طبيعي = أصل عظمي مرجّح.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى تراجع الطبيب؟",
                body_html="<p>راجع الطبيب إذا تجاوز GGT ثلاثة أضعاف الحد الأعلى، أو ارتفعت ALT/AST/ALP، أو ظهر يرقان أو كان هناك تاريخ لاستهلاك الكحول.</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف تساعدك Norya",
                body_html="<p>ارفع تقريرك على <a href=\"/analyze\">noryaai.com/analyze</a> وسيستخرج الذكاء الاصطناعي GGT وALT وAST وALP والبيليروبين وغيرها. <a href=\"/pricing\">صفحة الأسعار</a>.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ============================================================================
# Public API
# ============================================================================

def get_ggt_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for GGT article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_ggt_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for GGT article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal GGT level?",
             "answer": "Normal GGT is 8–61 U/L for men and 5–36 U/L for women. Values increase with age and may be elevated by obesity, metabolic syndrome, and certain medications."},
            {"question": "What causes high GGT?",
             "answer": "Common causes include liver disease (hepatitis, fatty liver, cirrhosis), alcohol use, medications (anticonvulsants, NSAIDs), bile duct obstruction, pancreatitis, heart failure, and metabolic syndrome."},
            {"question": "Why is GGT sensitive to alcohol?",
             "answer": "Alcohol directly induces GGT production in liver cells and causes liver cell damage that releases GGT. After stopping alcohol, GGT typically normalises within 2–6 weeks."},
            {"question": "What does high ALP with high GGT mean?",
             "answer": "When both ALP and GGT are elevated, the ALP rise is likely of liver/bile duct origin rather than bone. If ALP is high but GGT is normal, the ALP is probably from bone."},
        ],
        "tr": [
            {"question": "Normal GGT değeri nedir?",
             "answer": "Erkeklerde 8–61 U/L, kadınlarda 5–36 U/L normaldir. Yaş, obezite ve bazı ilaçlar değeri etkileyebilir."},
            {"question": "GGT yüksekliğinin nedenleri nelerdir?",
             "answer": "Karaciğer hastalığı, alkol, ilaçlar (antikonvülzanlar, NSAİİ), safra yolu tıkanıklığı, pankreatit, kalp yetmezliği ve metabolik sendrom."},
            {"question": "GGT neden alkole duyarlıdır?",
             "answer": "Alkol GGT üretimini doğrudan uyarır ve karaciğer hasarı yapar. Bırakıldıktan sonra 2–6 haftada normale döner."},
            {"question": "ALP ve GGT birlikte yüksekse ne anlama gelir?",
             "answer": "İkisi birlikte yüksekse ALP kaynağı muhtemelen karaciğerdir. ALP yüksek ama GGT normalse kaynak muhtemelen kemiktir."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de GGT?",
             "answer": "Hombres: 8–61 U/L. Mujeres: 5–36 U/L."},
            {"question": "¿Qué causa la GGT alta?",
             "answer": "Enfermedad hepática, alcohol, medicamentos, obstrucción biliar, pancreatitis e insuficiencia cardíaca."},
            {"question": "¿Por qué la GGT es sensible al alcohol?",
             "answer": "El alcohol induce la producción de GGT y causa daño hepático. Se normaliza en 2–6 semanas tras la abstinencia."},
        ],
        "de": [
            {"question": "Was ist ein normaler GGT-Wert?",
             "answer": "Männer: 8–61 U/L. Frauen: 5–36 U/L."},
            {"question": "Was verursacht erhöhte GGT?",
             "answer": "Lebererkrankungen, Alkohol, Medikamente, Gallenwegsobstruktion, Pankreatitis und Herzinsuffizienz."},
            {"question": "Warum ist die GGT empfindlich gegenüber Alkohol?",
             "answer": "Alkohol induziert die GGT-Produktion direkt und verursacht Leberzellschäden. Normalisierung in 2–6 Wochen nach Abstinenz."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de GGT ?",
             "answer": "Hommes : 8–61 U/L. Femmes : 5–36 U/L."},
            {"question": "Quelles sont les causes d'une GGT élevée ?",
             "answer": "Maladie hépatique, alcool, médicaments, obstruction biliaire, pancréatite et insuffisance cardiaque."},
            {"question": "Pourquoi la GGT est-elle sensible à l'alcool ?",
             "answer": "L'alcool induit la production de GGT et cause des lésions hépatiques. Normalisation en 2–6 semaines après l'arrêt."},
        ],
        "it": [
            {"question": "Qual è il valore normale della GGT?",
             "answer": "Uomini: 8–61 U/L. Donne: 5–36 U/L."},
            {"question": "Cosa causa la GGT alta?",
             "answer": "Epatopatie, alcol, farmaci, ostruzione biliare, pancreatite e insufficienza cardiaca."},
            {"question": "Perché la GGT è sensibile all'alcol?",
             "answer": "L'alcol induce la produzione di GGT e causa danno epatocellulare. Si normalizza in 2–6 settimane dall'astinenza."},
        ],
        "he": [
            {"question": "מהו ערך GGT תקין?",
             "answer": "גברים: 8–61 U/L. נשים: 5–36 U/L."},
            {"question": "מה גורם ל-GGT גבוה?",
             "answer": "מחלות כבד, אלכוהול, תרופות, חסימת דרכי מרה, דלקת לבלב ואי-ספיקת לב."},
            {"question": "למה GGT רגיש לאלכוהול?",
             "answer": "אלכוהול מעורר ישירות ייצור GGT וגורם נזק להפטוציטים. מתנרמל תוך 2–6 שבועות לאחר הפסקה."},
        ],
        "hi": [
            {"question": "सामान्य GGT कितना होना चाहिए?",
             "answer": "पुरुष: 8–61 U/L। महिला: 5–36 U/L।"},
            {"question": "GGT बढ़ने के कारण क्या हैं?",
             "answer": "यकृत रोग, शराब, दवाएँ, पित्त नली अवरोध, अग्नाशयशोथ और हृदय विफलता।"},
            {"question": "GGT शराब के प्रति इतना संवेदनशील क्यों है?",
             "answer": "शराब सीधे GGT उत्पादन बढ़ाती है और लिवर कोशिका क्षति करती है। छोड़ने के 2–6 सप्ताह में सामान्य होता है।"},
        ],
        "ar": [
            {"question": "ما هو مستوى GGT الطبيعي؟",
             "answer": "رجال: 8–61 U/L. نساء: 5–36 U/L."},
            {"question": "ما أسباب ارتفاع GGT؟",
             "answer": "أمراض كبدية، كحول، أدوية، انسداد صفراوي، التهاب بنكرياس وقصور قلب."},
            {"question": "لماذا GGT حساس للكحول؟",
             "answer": "الكحول يحفّز إنتاج GGT مباشرة ويسبب تلف خلايا الكبد. يعود طبيعياً خلال 2–6 أسابيع بعد التوقف."},
        ],
    }
