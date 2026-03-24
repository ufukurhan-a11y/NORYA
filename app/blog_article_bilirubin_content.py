# -*- coding: utf-8 -*-
"""
Bilirubin high meaning blog article — full body content for all 9 languages.
Used by blog_i18n._article_bilirubin().
Sections: intro, what-is-bilirubin, direct-vs-indirect, normal-ranges,
high-bilirubin-causes, jaundice-connection, gilbert-syndrome,
newborn-bilirubin, related-tests, when-to-see-doctor, how-norya-helps,
disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ---------------------------------------------------------------------------
# English
# ---------------------------------------------------------------------------
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Bilirubin high: what does it mean?",
            body_html=(
                "<p>Bilirubin is a yellow pigment that shows up on liver-function panels, and an elevated result can be unsettling&mdash;especially if no one explains what it means. "
                "Is it a sign of liver disease? Could it be harmless? The answer depends on <em>which</em> type of bilirubin is raised, by how much, and what other markers look like.</p>"
                "<p>This guide explains what bilirubin is, the difference between direct and indirect forms, normal reference ranges, the most common causes of elevated bilirubin, "
                "and when you should see a doctor. It is educational, not diagnostic&mdash;always discuss your results with a healthcare professional.</p>"
            ),
        ),
        Section(
            id="what-is-bilirubin", level=2,
            heading="What is bilirubin?",
            body_html=(
                "<p><strong>Bilirubin</strong> is a yellow-orange compound produced during the normal breakdown of haem&mdash;the iron-containing part of haemoglobin in red blood cells. "
                "When old or damaged red cells are recycled by the spleen and liver, the haem is converted first to biliverdin and then to bilirubin. "
                "This &ldquo;unconjugated&rdquo; (indirect) bilirubin travels through the bloodstream bound to albumin until it reaches the liver.</p>"
                "<p>Inside the liver, the enzyme UDP-glucuronosyltransferase conjugates bilirubin with glucuronic acid, making it water-soluble. "
                "This &ldquo;conjugated&rdquo; (direct) bilirubin is excreted into bile, passes into the intestine, and is eventually eliminated in stool (giving it its characteristic brown colour) "
                "or, in small amounts, reabsorbed and excreted by the kidneys in urine.</p>"
                "<p>Bilirubin is measured in milligrams per decilitre (mg/dL) or micromoles per litre (&mu;mol/L). "
                "Most labs report <strong>total bilirubin</strong> and <strong>direct (conjugated) bilirubin</strong>; indirect bilirubin is calculated by subtraction.</p>"
            ),
        ),
        Section(
            id="direct-vs-indirect", level=2,
            heading="Direct vs. indirect bilirubin",
            body_html=(
                "<p>Distinguishing between the two forms is clinically important because each points to a different set of causes:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Type</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Also called</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Elevated when&hellip;</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Indirect (unconjugated)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Unconjugated bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Increased RBC breakdown (haemolysis), impaired conjugation (Gilbert&rsquo;s syndrome, neonatal jaundice)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Direct (conjugated)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Conjugated bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Impaired bile flow (gallstones, tumours, hepatitis, cirrhosis, drug-induced cholestasis)</td></tr>'
                "</tbody></table>"
                "<p>When <strong>indirect bilirubin</strong> is predominantly elevated, the problem is usually <em>before</em> the liver (pre-hepatic)&mdash;too many red cells being destroyed, "
                "or the liver&rsquo;s conjugation machinery working slowly. When <strong>direct bilirubin</strong> is high, the problem is <em>at</em> or <em>after</em> the liver "
                "(hepatic or post-hepatic)&mdash;the liver cannot excrete conjugated bilirubin properly, often because of bile duct obstruction or liver-cell damage.</p>"
                "<p>A mixed pattern (both types elevated) is common in hepatitis and advanced liver disease, where both conjugation and excretion are impaired.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal bilirubin ranges",
            body_html=(
                "<p>Reference ranges may vary slightly between laboratories. The values below are widely accepted for adults.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parameter</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typical range (mg/dL)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Typical range (&mu;mol/L)</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Total bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1&ndash;1.2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.7&ndash;20.5</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Direct (conjugated)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0.3</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;5.1</td></tr>'
                "</tbody></table>"
                "<p>Indirect bilirubin is not measured directly; it is calculated as total minus direct. "
                "Values in newborns are substantially higher and are evaluated using age-specific charts. "
                "Fasting can transiently raise unconjugated bilirubin, especially in individuals with Gilbert&rsquo;s syndrome.</p>"
            ),
        ),
        Section(
            id="high-bilirubin-causes", level=2,
            heading="Common causes of high bilirubin",
            body_html=(
                "<p>Elevated bilirubin (hyperbilirubinaemia) can be grouped by mechanism:</p>"
                "<p><strong>Increased production (pre-hepatic):</strong> any condition that accelerates red blood cell destruction raises unconjugated bilirubin. "
                "Examples include <strong>haemolytic anemias</strong> (autoimmune, sickle cell, thalassemia, G6PD deficiency), transfusion reactions, and large haematomas being reabsorbed.</p>"
                "<p><strong>Impaired conjugation (hepatic):</strong> <strong>Gilbert&rsquo;s syndrome</strong> (the most common cause of mild, isolated unconjugated hyperbilirubinaemia) "
                "results from reduced activity of the conjugating enzyme. Neonatal jaundice is caused by the immaturity of the same enzyme. "
                "Certain drugs and hepatitis can also impair conjugation.</p>"
                "<p><strong>Impaired excretion (hepatic / post-hepatic):</strong> <strong>liver diseases</strong> (hepatitis, cirrhosis, alcoholic liver disease, drug-induced liver injury) "
                "reduce the liver&rsquo;s ability to excrete conjugated bilirubin into bile. <strong>Bile duct obstruction</strong> (gallstones, pancreatic head tumours, cholangiocarcinoma, strictures) "
                "blocks the outflow of bile, causing conjugated bilirubin to back up into the blood. Certain medications (e.g.&nbsp;some antibiotics, oral contraceptives) can also cause cholestasis.</p>"
            ),
        ),
        Section(
            id="jaundice-connection", level=2,
            heading="Bilirubin and jaundice",
            body_html=(
                "<p><strong>Jaundice</strong> (icterus) is the visible yellowing of the skin, whites of the eyes (sclerae), and mucous membranes that occurs when bilirubin levels rise above "
                "approximately 2.5&ndash;3.0&nbsp;mg/dL (43&ndash;51&nbsp;&mu;mol/L). It is one of the earliest and most recognisable clinical signs of hyperbilirubinaemia.</p>"
                "<p>The pattern of jaundice can offer clues about the cause. <strong>Pre-hepatic jaundice</strong> (haemolysis) often presents with an unconjugated bilirubin rise, "
                "dark-coloured urine may be absent (unconjugated bilirubin is not water-soluble and not excreted by the kidneys), and stools remain normal or dark. "
                "<strong>Hepatic jaundice</strong> (hepatitis, cirrhosis) produces a mixed picture with both conjugated and unconjugated fractions elevated. "
                "<strong>Post-hepatic (obstructive) jaundice</strong> leads to high conjugated bilirubin, dark urine (conjugated bilirubin spills into the urine), "
                "and pale or clay-coloured stools (bilirubin cannot reach the intestine).</p>"
                "<p>Not everyone with mildly elevated bilirubin develops visible jaundice. Conversely, in some people (e.g.&nbsp;those with dark skin), "
                "subtle jaundice may be easier to detect by examining the sclerae or the underside of the tongue.</p>"
            ),
        ),
        Section(
            id="gilbert-syndrome", level=2,
            heading="Gilbert's syndrome: a common and benign cause",
            body_html=(
                "<p><strong>Gilbert&rsquo;s syndrome</strong> is a genetic condition affecting roughly 5&ndash;10&nbsp;% of the population (some estimates go higher). "
                "It results from a variant in the UGT1A1 gene that reduces the activity of the enzyme responsible for conjugating bilirubin. "
                "The hallmark is a mild, fluctuating elevation of unconjugated bilirubin&mdash;typically between 1.0 and 3.0&nbsp;mg/dL&mdash;that can increase during fasting, "
                "illness, stress, or vigorous exercise.</p>"
                "<p>Gilbert&rsquo;s syndrome is <strong>benign</strong>: it does not cause liver damage, does not progress to liver disease, and requires no treatment. "
                "However, it is important to recognise because it can cause mild jaundice during periods of stress or fasting, "
                "which might otherwise trigger unnecessary investigations. If your doctor suspects Gilbert&rsquo;s, they will typically confirm it by showing that liver enzymes (ALT, AST, ALP, GGT) "
                "are normal, the direct bilirubin fraction is low, and no other cause of haemolysis is present.</p>"
                "<p>One clinical consideration: the reduced UGT1A1 activity in Gilbert&rsquo;s can affect the metabolism of certain drugs "
                "(e.g.&nbsp;irinotecan, atazanavir), so it is worth mentioning to your doctor before starting new medications.</p>"
            ),
        ),
        Section(
            id="newborn-bilirubin", level=2,
            heading="Bilirubin in newborns (neonatal jaundice)",
            body_html=(
                "<p>Neonatal jaundice is extremely common, affecting more than 60&nbsp;% of term newborns and an even higher proportion of premature babies. "
                "It occurs because newborns have a high rate of red-cell turnover, and their liver enzyme (UGT1A1) is immature, "
                "so unconjugated bilirubin accumulates faster than the liver can process it.</p>"
                "<p>In most cases, neonatal jaundice is <strong>physiological</strong> (normal)&mdash;it appears on day 2&ndash;3 of life, peaks around day 3&ndash;5, "
                "and resolves within 1&ndash;2 weeks. <strong>Breastfeeding jaundice</strong> can prolong the course. "
                "However, very high unconjugated bilirubin in newborns can be dangerous because it can cross the blood&ndash;brain barrier and cause kernicterus (bilirubin encephalopathy), "
                "a form of brain damage. That is why hospitals monitor newborn bilirubin closely and may use <strong>phototherapy</strong> (blue-light treatment) "
                "or, in severe cases, <strong>exchange transfusion</strong> to bring levels down.</p>"
                "<p>Jaundice appearing within the first 24&nbsp;hours of life, a rapid rise in bilirubin, or a prolonged course beyond 2&ndash;3 weeks "
                "always warrants medical evaluation to rule out pathological causes such as haemolytic disease, biliary atresia, or metabolic disorders.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests your doctor may review",
            body_html=(
                "<p>Bilirubin is part of the liver-function panel, which typically includes <strong>ALT</strong>, <strong>AST</strong>, "
                "<strong><a href=\"/en/blog/alp-high-meaning\">ALP</a></strong>, <strong><a href=\"/en/blog/ggt-high-meaning\">GGT</a></strong>, "
                "<strong>albumin</strong>, and <strong>total protein</strong>. Together they help the doctor determine whether the bilirubin elevation is hepatocellular, cholestatic, or haemolytic.</p>"
                "<p>If haemolysis is suspected, the doctor may add a <strong>reticulocyte count</strong>, <strong>haptoglobin</strong>, <strong>LDH</strong>, and a <strong>direct Coombs test</strong>. "
                "For obstruction, <strong>abdominal ultrasound</strong> or <strong>MRCP</strong> (magnetic resonance cholangiopancreatography) can visualise the bile ducts. "
                "A <strong>peripheral blood smear</strong> may show fragmented red cells in haemolytic conditions. "
                "For suspected Gilbert&rsquo;s, the diagnosis is usually clinical: mildly elevated unconjugated bilirubin with otherwise normal liver tests.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>See your doctor if bilirubin is elevated on your blood test, even if you feel well. "
                "Seek <strong>prompt</strong> attention if you notice jaundice (yellow skin or eyes), dark urine, pale stools, "
                "abdominal pain (especially in the upper right area), fever, or unexplained fatigue and weight loss.</p>"
                "<p>In newborns, notify the paediatrician if jaundice appears within the first 24&nbsp;hours, deepens quickly, "
                "or persists beyond two weeks. A mildly elevated bilirubin in an otherwise healthy adult is often Gilbert&rsquo;s syndrome, "
                "but this should be confirmed by a doctor rather than assumed.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare. Upload your blood test at <a href=\"/analyze\">noryaai.com/analyze</a> and receive a clear, "
                "structured summary that explains your bilirubin (total, direct, indirect) and other liver markers in plain language, with reference ranges and context. "
                "This makes it easier to understand the numbers and discuss them productively with your doctor.</p>"
                "<p>Whether you are monitoring a known Gilbert&rsquo;s syndrome or seeing &ldquo;Total Bilirubin 1.8 mg/dL&rdquo; for the first time, "
                "Norya organises your results so you can ask the right questions. For plans and pricing, visit our <a href=\"/pricing\">pricing page</a>.</p>"
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
# Turkish
# ---------------------------------------------------------------------------
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirubin yüksekliği ne anlama gelir?",
                body_html=(
                    "<p>Bilirubin, karaciğer fonksiyon panellerinde yer alan sarı bir pigmenttir. Yüksek çıktığında ilk soru şudur: <em>karaciğerimde bir sorun mu var?</em> "
                    "Yanıt, hangi tip bilirubinin yüksek olduğuna, ne kadar yüksek olduğuna ve diğer belirteçlerin durumuna bağlıdır.</p>"
                    "<p>Bu rehber bilirubinin ne olduğunu, direkt-indirekt farkını, normal aralıkları, yükseklik nedenlerini ve ne zaman hekime başvurmanız gerektiğini anlatır.</p>")),
        Section(id="what-is-bilirubin", level=2, heading="Bilirubin nedir?",
                body_html=(
                    "<p><strong>Bilirubin</strong>, kırmızı kan hücrelerindeki hemoglobinin demir içeren kısmı olan hem&rsquo;in normal yıkımı sırasında üretilen sarı-turuncu bir bileşiktir. "
                    "Yaşlı veya hasarlı kırmızı hücreler dalak ve karaciğer tarafından geri dönüştürüldüğünde hem önce biliverdin&rsquo;e, sonra bilirubin&rsquo;e dönüştürülür.</p>"
                    "<p>Bu &ldquo;konjüge olmamış&rdquo; (indirekt) bilirubin, albumine bağlı olarak karaciğere ulaşana kadar kan dolaşımında taşınır. "
                    "Karaciğerde glükuronik asitle konjüge edilerek suda çözünür hale gelir (direkt bilirubin), safra yoluyla bağırsağa atılır.</p>"
                    "<p>Bilirubin mg/dL veya &mu;mol/L cinsinden ölçülür. Laboratuvarlar genellikle <strong>toplam bilirubin</strong> ve <strong>direkt bilirubin</strong> raporlar; indirekt farkla hesaplanır.</p>")),
        Section(id="direct-vs-indirect", level=2, heading="Direkt ve indirekt bilirubin farkı",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tip</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Diğer adı</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Yükselme durumu</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">İndirekt</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Konjüge olmamış</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Artmış RBC yıkımı (hemoliz), bozulmuş konjügasyon (Gilbert sendromu, neonatal sarılık)</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Direkt</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Konjüge</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Bozulmuş safra akışı (safra taşları, tümörler, hepatit, siroz, ilaçlara bağlı kolestaz)</td></tr>'
                    "</tbody></table>"
                    "<p>İndirekt bilirubin ağırlıklı yüksekse sorun genellikle karaciğer <em>öncesindedir</em> (pre-hepatik). "
                    "Direkt bilirubin yüksekse sorun karaciğerde veya <em>sonrasındadır</em> (hepatik/post-hepatik). "
                    "Her ikisi de yüksekse (karma patern) hepatit ve ilerlemiş karaciğer hastalığında görülür.</p>")),
        Section(id="normal-ranges", level=2, heading="Normal bilirubin aralıkları",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parametre</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tipik aralık (mg/dL)</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Tipik aralık (&mu;mol/L)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Toplam bilirubin</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1&ndash;1,2</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,7&ndash;20,5</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Direkt (konjüge)</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0,3</td>'
                    '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;5,1</td></tr>'
                    "</tbody></table>"
                    "<p>Yenidoğanlarda değerler belirgin şekilde yüksektir ve yaşa özgü çizelgelerle değerlendirilir. "
                    "Açlık, özellikle Gilbert sendromlu kişilerde indirekt bilirubini geçici olarak yükseltebilir.</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="Bilirubin yüksekliğinin yaygın nedenleri",
                body_html=(
                    "<p><strong>Artmış üretim (pre-hepatik):</strong> hemolitik anemiler (otoimmün, orak hücre, talasemi, G6PD eksikliği), transfüzyon reaksiyonları.</p>"
                    "<p><strong>Bozulmuş konjügasyon (hepatik):</strong> <strong>Gilbert sendromu</strong> (en yaygın neden), neonatal sarılık, bazı ilaçlar.</p>"
                    "<p><strong>Bozulmuş atılım (hepatik/post-hepatik):</strong> hepatit, siroz, alkolik karaciğer hastalığı, ilaçlara bağlı hasar, "
                    "safra yolu tıkanıklığı (safra taşları, pankreas başı tümörleri, kolanjiyokarsinom).</p>")),
        Section(id="jaundice-connection", level=2, heading="Bilirubin ve sarılık",
                body_html=(
                    "<p><strong>Sarılık</strong> (ikter), bilirubin seviyesi yaklaşık 2,5&ndash;3,0&nbsp;mg/dL&rsquo;yi aştığında cildin, göz aklarının ve mukoza zarlarının sararmasıdır. "
                    "Hiperbilirubinemiatin en erken klinik bulgularından biridir.</p>"
                    "<p>Pre-hepatik sarılıkta indirekt bilirubin yükselir; idrar koyu olmayabilir. Hepatik sarılıkta karma tablo görülür. "
                    "Post-hepatik (obstrüktif) sarılıkta direkt bilirubin yükselir, idrar koyulaşır, dışkı soluklaşır.</p>")),
        Section(id="gilbert-syndrome", level=2, heading="Gilbert sendromu: yaygın ve iyi huylu bir neden",
                body_html=(
                    "<p><strong>Gilbert sendromu</strong>, popülasyonun yaklaşık %5&ndash;10&rsquo;unu etkileyen genetik bir durumdur. "
                    "UGT1A1 genindeki bir varyant, konjügasyon enziminin aktivitesini azaltır. "
                    "Hafif, dalgalanan indirekt bilirubin yüksekliği (genellikle 1,0&ndash;3,0&nbsp;mg/dL arası) karakteristiktir; açlık, hastalık veya streste artabilir.</p>"
                    "<p>Gilbert sendromu <strong>iyi huyludur</strong>: karaciğer hasarına yol açmaz, tedavi gerektirmez. "
                    "Ancak stres veya açlıkta hafif sarılığa neden olabileceğinden tanınması önemlidir&mdash;gereksiz araştırmaları önler.</p>"
                    "<p>Gilbert sendromunda azalmış UGT1A1 bazı ilaçların (irinotekan, atazanavir gibi) metabolizmasını etkileyebilir; "
                    "yeni ilaç başlamadan önce doktorunuza bildirmek yararlıdır.</p>")),
        Section(id="newborn-bilirubin", level=2, heading="Yenidoğanlarda bilirubin (neonatal sarılık)",
                body_html=(
                    "<p>Neonatal sarılık son derece yaygındır; zamanında doğan bebeklerin %60&rsquo;ından fazlasını, prematürelerin daha yüksek bir oranını etkiler. "
                    "Yenidoğanların yüksek kırmızı hücre döngüsü ve olgunlaşmamış karaciğer enzimi nedeniyle indirekt bilirubin birikir.</p>"
                    "<p>Çoğu durumda neonatal sarılık <strong>fizyolojiktir</strong>&mdash;yaşamın 2&ndash;3. gününde başlar, 3&ndash;5. günde zirve yapar, 1&ndash;2 haftada çözülür. "
                    "Ancak çok yüksek indirekt bilirubin kernikterusa (bilirubin ensefalopatisi) neden olabilir; bu nedenle hastaneler bilirubin düzeylerini yakından izler "
                    "ve gerekirse <strong>fototerapi</strong> veya <strong>kan değişimi</strong> uygular.</p>"
                    "<p>İlk 24 saat içinde ortaya çıkan sarılık, hızlı yükselme veya 2&ndash;3 haftayı aşan süre patolojik nedenleri dışlamak için değerlendirilmelidir.</p>")),
        Section(id="related-tests", level=2, heading="Hekimin değerlendirebileceği ilişkili testler",
                body_html=(
                    "<p>Bilirubin, karaciğer fonksiyon panelinin bir parçasıdır; genellikle <strong>ALT</strong>, <strong>AST</strong>, "
                    "<strong><a href=\"/tr/blog/alp-yuksekligi-ne-anlama-gelir\">ALP</a></strong>, <strong><a href=\"/tr/blog/ggt-yuksekligi-ne-anlama-gelir\">GGT</a></strong>, "
                    "<strong>albümin</strong> ve <strong>total protein</strong> ile birlikte raporlanır.</p>"
                    "<p>Hemoliz şüphesinde retikülosit sayımı, haptoglobin, LDH ve direkt Coombs testi istenebilir. "
                    "Tıkanıklık için karın ultrasonu veya MRCP yapılabilir. Gilbert sendromu şüphesinde tanı genellikle kliniktir.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="Ne zaman hekime başvurmalısınız?",
                body_html=(
                    "<p>Bilirubin yüksekse, kendinizi iyi hissetseniz bile hekiminizle görüşün. "
                    "Sarılık, koyu idrar, açık renkli dışkı, karın ağrısı, ateş veya açıklanamayan yorgunluk durumunda <strong>acil</strong> değerlendirme alın.</p>"
                    "<p>Yenidoğanlarda ilk 24 saatte ortaya çıkan, hızla derinleşen veya 2 haftayı aşan sarılık için pediatrist bilgilendirilmelidir.</p>")),
        Section(id="how-norya-helps", level=2, heading="Norya nasıl yardımcı olur?",
                body_html=(
                    "<p>Norya teşhis koymaz&mdash;randevunuza hazırlanmanıza yardımcı olur. Raporunuzu <a href=\"/analyze\">noryaai.com/analyze</a> adresinden yükleyin "
                    "ve bilirubin (toplam, direkt, indirekt) ile diğer karaciğer belirteçlerinizi sade dilde açıklayan net bir özet alın.</p>"
                    "<p>Plan ve fiyatlar: <a href=\"/pricing\">fiyatlandırma sayfası</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Uyarı",
                body_html=(
                    '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> '
                    'Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. <a href="/analyze">Norya ile analiz başlat</a></p>')),
    ]


# ---------------------------------------------------------------------------
# Spanish
# ---------------------------------------------------------------------------
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirrubina alta: ¿qué significa?",
                body_html=(
                    "<p>La bilirrubina es un pigmento amarillo que aparece en los paneles hepáticos. Cuando está elevada, la pregunta es: ¿hay un problema en el hígado? "
                    "La respuesta depende de qué tipo de bilirrubina está elevada, de cuánto y de los demás marcadores.</p>"
                    "<p>Esta guía explica qué es la bilirrubina, la diferencia entre directa e indirecta, rangos normales, causas de elevación y cuándo consultar.</p>")),
        Section(id="what-is-bilirubin", level=2, heading="¿Qué es la bilirrubina?",
                body_html=(
                    "<p><strong>La bilirrubina</strong> es un compuesto amarillo-anaranjado producido durante la degradación normal del grupo hemo de la hemoglobina. "
                    "La bilirrubina indirecta (no conjugada) viaja unida a la albúmina hasta el hígado, donde se conjuga y se excreta en la bilis.</p>"
                    "<p>Se mide en mg/dL o &mu;mol/L. Los laboratorios suelen reportar bilirrubina total y directa; la indirecta se calcula por diferencia.</p>")),
        Section(id="direct-vs-indirect", level=2, heading="Bilirrubina directa vs. indirecta",
                body_html=(
                    "<p><strong>Indirecta</strong> elevada: hemólisis, síndrome de Gilbert, ictericia neonatal.</p>"
                    "<p><strong>Directa</strong> elevada: obstrucción biliar, hepatitis, cirrosis, colestasis por fármacos.</p>"
                    "<p>Patrón mixto: hepatitis y enfermedad hepática avanzada.</p>")),
        Section(id="normal-ranges", level=2, heading="Rangos normales de bilirrubina",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parámetro</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango (mg/dL)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Total</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1&ndash;1,2</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Directa</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0,3</td></tr>'
                    "</tbody></table>"
                    "<p>En neonatos los valores son mucho más altos. El ayuno puede elevar transitoriamente la bilirrubina indirecta, especialmente en Gilbert.</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="Causas frecuentes de bilirrubina alta",
                body_html=(
                    "<p><strong>Producción aumentada:</strong> anemias hemolíticas, reacciones transfusionales.</p>"
                    "<p><strong>Conjugación alterada:</strong> síndrome de Gilbert, ictericia neonatal, ciertos fármacos.</p>"
                    "<p><strong>Excreción alterada:</strong> hepatitis, cirrosis, obstrucción biliar (cálculos, tumores).</p>")),
        Section(id="jaundice-connection", level=2, heading="Bilirrubina e ictericia",
                body_html=(
                    "<p>La <strong>ictericia</strong> es la coloración amarilla visible cuando la bilirrubina supera ~2,5&ndash;3,0 mg/dL. "
                    "El patrón (orina oscura, heces pálidas) orienta sobre la causa.</p>"
                    "<p>Pre-hepática: orina normal, heces oscuras. Hepática: mixto. Post-hepática: orina oscura, heces pálidas.</p>")),
        Section(id="gilbert-syndrome", level=2, heading="Síndrome de Gilbert: causa frecuente y benigna",
                body_html=(
                    "<p>Afecta al 5&ndash;10 % de la población. Produce una elevación leve y fluctuante de bilirrubina indirecta (1,0&ndash;3,0 mg/dL). "
                    "Es benigno: no causa daño hepático ni requiere tratamiento.</p>"
                    "<p>La actividad reducida de UGT1A1 puede afectar el metabolismo de ciertos fármacos (irinotecán, atazanavir).</p>")),
        Section(id="newborn-bilirubin", level=2, heading="Bilirrubina en recién nacidos",
                body_html=(
                    "<p>La ictericia neonatal afecta a más del 60 % de los neonatos a término. Suele ser fisiológica: aparece al 2.°&ndash;3.er día y se resuelve en 1&ndash;2 semanas.</p>"
                    "<p>Niveles muy altos pueden causar kernicterus. La fototerapia y, en casos graves, la exanguinotransfusión son los tratamientos estándar.</p>")),
        Section(id="related-tests", level=2, heading="Pruebas relacionadas",
                body_html=(
                    "<p>ALT, AST, <a href=\"/es/blog/fosfatasa-alcalina-alta\">ALP</a>, <a href=\"/es/blog/ggt-alta-significado\">GGT</a>, albúmina, proteínas totales.</p>"
                    "<p>Si se sospecha hemólisis: reticulocitos, haptoglobina, LDH, Coombs directo. Para obstrucción: ecografía abdominal o CPRM.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="¿Cuándo acudir al médico?",
                body_html=(
                    "<p>Consulta si la bilirrubina está elevada, aunque te sientas bien. Busca atención urgente si aparece ictericia, orina oscura, heces pálidas o dolor abdominal.</p>"
                    "<p>En neonatos, notificar si la ictericia aparece en las primeras 24 h, empeora rápidamente o dura más de 2 semanas.</p>")),
        Section(id="how-norya-helps", level=2, heading="Cómo ayuda Norya",
                body_html=(
                    "<p>Norya no diagnostica&mdash;te ayuda a prepararte. Sube tu analítica en <a href=\"/analyze\">noryaai.com/analyze</a>.</p>"
                    "<p>Opciones y precios: <a href=\"/pricing\">página de precios</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html=(
                    '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> '
                    'Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>')),
    ]


# ---------------------------------------------------------------------------
# German
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirubin erhöht: Was bedeutet das?",
                body_html=(
                    "<p>Bilirubin ist ein gelbes Pigment im Leberfunktionspanel. Ein erhöhter Wert wirft die Frage auf: Stimmt etwas mit der Leber nicht? "
                    "Die Antwort hängt davon ab, welcher Typ erhöht ist und wie stark.</p>"
                    "<p>Dieser Ratgeber erklärt Bilirubin, direkt vs. indirekt, Normwerte, Ursachen und wann Sie zum Arzt sollten.</p>")),
        Section(id="what-is-bilirubin", level=2, heading="Was ist Bilirubin?",
                body_html=(
                    "<p><strong>Bilirubin</strong> entsteht beim Abbau von Häm aus Hämoglobin. Indirektes (unkonjugiertes) Bilirubin wird in der Leber konjugiert, "
                    "in die Galle ausgeschieden und über den Darm eliminiert.</p>"
                    "<p>Es wird in mg/dL oder &mu;mol/L gemessen. Labore berichten Gesamt- und direktes Bilirubin; indirektes wird errechnet.</p>")),
        Section(id="direct-vs-indirect", level=2, heading="Direktes vs. indirektes Bilirubin",
                body_html=(
                    "<p><strong>Indirektes</strong> erhöht: Hämolyse, Morbus Gilbert, Neugeborenenikterus.</p>"
                    "<p><strong>Direktes</strong> erhöht: Gallenstau, Hepatitis, Zirrhose, medikamentöse Cholestase.</p>"
                    "<p>Mischbild: Hepatitis und fortgeschrittene Lebererkrankung.</p>")),
        Section(id="normal-ranges", level=2, heading="Normale Bilirubin-Bereiche",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parameter</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Bereich (mg/dL)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Gesamtbilirubin</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1&ndash;1,2</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Direktes</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0,3</td></tr>'
                    "</tbody></table>"
                    "<p>Bei Neugeborenen gelten altersabhängige Normogramme. Fasten kann indirektes Bilirubin vorübergehend erhöhen, besonders bei M. Gilbert.</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="Häufige Ursachen erhöhten Bilirubins",
                body_html=(
                    "<p><strong>Erhöhte Produktion:</strong> hämolytische Anämien, Transfusionsreaktionen.</p>"
                    "<p><strong>Gestörte Konjugation:</strong> Morbus Gilbert, Neugeborenenikterus, bestimmte Medikamente.</p>"
                    "<p><strong>Gestörte Ausscheidung:</strong> Hepatitis, Zirrhose, Gallengangsobstruktion (Steine, Tumoren).</p>")),
        Section(id="jaundice-connection", level=2, heading="Bilirubin und Gelbsucht",
                body_html=(
                    "<p><strong>Ikterus</strong> wird sichtbar ab ca. 2,5&ndash;3,0 mg/dL. Das Muster (dunkler Urin, heller Stuhl) gibt Hinweise auf die Ursache.</p>"
                    "<p>Prä-hepatisch: Urin normal, Stuhl dunkel. Hepatisch: Mischbild. Post-hepatisch: dunkler Urin, entfärbter Stuhl.</p>")),
        Section(id="gilbert-syndrome", level=2, heading="Morbus Gilbert: häufig und harmlos",
                body_html=(
                    "<p>Betrifft ca. 5&ndash;10 % der Bevölkerung. Milde, schwankende indirekte Hyperbilirubinämie (1,0&ndash;3,0 mg/dL). "
                    "Harmlos, kein Leberschaden, keine Behandlung nötig.</p>"
                    "<p>Die reduzierte UGT1A1-Aktivität kann den Abbau bestimmter Medikamente beeinflussen.</p>")),
        Section(id="newborn-bilirubin", level=2, heading="Bilirubin bei Neugeborenen",
                body_html=(
                    "<p>Neugeborenenikterus betrifft &gt; 60 % der Reifgeborenen. Meist physiologisch: Beginn am 2.&ndash;3. Tag, Rückgang in 1&ndash;2 Wochen.</p>"
                    "<p>Sehr hohe Werte können einen Kernikterus verursachen. Phototherapie und ggf. Austauschtransfusion sind Standardmaßnahmen.</p>")),
        Section(id="related-tests", level=2, heading="Verwandte Tests",
                body_html=(
                    "<p>ALT, AST, <a href=\"/de/blog/alkalische-phosphatase-hoch\">ALP</a>, <a href=\"/de/blog/ggt-erhoht-bedeutung\">GGT</a>, Albumin, Gesamtprotein.</p>"
                    "<p>Bei Hämolyse-Verdacht: Retikulozyten, Haptoglobin, LDH, direkter Coombs. Bei Obstruktion: Sonographie oder MRCP.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="Wann zum Arzt?",
                body_html=(
                    "<p>Sprechen Sie mit Ihrem Arzt, wenn das Bilirubin erhöht ist. Suchen Sie dringend Hilfe bei Ikterus, dunklem Urin, hellem Stuhl oder Oberbauchschmerzen.</p>"
                    "<p>Bei Neugeborenen: Kinderarzt informieren, wenn Ikterus in den ersten 24 h auftritt, rasch zunimmt oder &gt; 2 Wochen anhält.</p>")),
        Section(id="how-norya-helps", level=2, heading="Wie Norya hilft",
                body_html=(
                    "<p>Norya stellt keine Diagnosen. Laden Sie Ihren Bericht unter <a href=\"/analyze\">noryaai.com/analyze</a> hoch.</p>"
                    "<p>Optionen und Preise: <a href=\"/pricing\">Preisseite</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html=(
                    '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> '
                    'Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>')),
    ]


# ---------------------------------------------------------------------------
# French
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirubine élevée : qu'est-ce que cela signifie ?",
                body_html=(
                    "<p>La bilirubine est un pigment jaune du bilan hépatique. Quand elle est élevée, la question est : y a-t-il un problème de foie ?</p>"
                    "<p>Ce guide explique la bilirubine, la différence entre directe et indirecte, les fourchettes, les causes et quand consulter.</p>")),
        Section(id="what-is-bilirubin", level=2, heading="Qu'est-ce que la bilirubine ?",
                body_html=(
                    "<p><strong>La bilirubine</strong> provient de la dégradation de l&rsquo;hème de l&rsquo;hémoglobine. "
                    "La forme indirecte est conjuguée dans le foie puis excrétée dans la bile.</p>"
                    "<p>Elle se mesure en mg/dL ou &mu;mol/L. Les laboratoires reportent bilirubine totale et directe.</p>")),
        Section(id="direct-vs-indirect", level=2, heading="Bilirubine directe vs indirecte",
                body_html=(
                    "<p><strong>Indirecte</strong> élevée : hémolyse, syndrome de Gilbert, ictère néonatal.</p>"
                    "<p><strong>Directe</strong> élevée : obstruction biliaire, hépatite, cirrhose, cholestase médicamenteuse.</p>")),
        Section(id="normal-ranges", level=2, heading="Valeurs normales de la bilirubine",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Paramètre</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fourchette (mg/dL)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Totale</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1&ndash;1,2</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Directe</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0,3</td></tr>'
                    "</tbody></table>"
                    "<p>Chez le nouveau-né, les valeurs sont nettement plus élevées. Le jeûne peut augmenter transitoirement la bilirubine indirecte.</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="Causes fréquentes de bilirubine élevée",
                body_html=(
                    "<p><strong>Production accrue :</strong> anémies hémolytiques. <strong>Conjugaison altérée :</strong> syndrome de Gilbert, ictère néonatal.</p>"
                    "<p><strong>Excrétion altérée :</strong> hépatite, cirrhose, obstruction biliaire (calculs, tumeurs).</p>")),
        Section(id="jaundice-connection", level=2, heading="Bilirubine et ictère",
                body_html=(
                    "<p>L&rsquo;<strong>ictère</strong> est visible dès ~2,5&ndash;3,0 mg/dL. Le profil (urines foncées, selles décolorées) oriente sur la cause.</p>")),
        Section(id="gilbert-syndrome", level=2, heading="Syndrome de Gilbert : fréquent et bénin",
                body_html=(
                    "<p>Touche 5&ndash;10 % de la population. Élévation légère et fluctuante de la bilirubine indirecte. "
                    "Bénin : pas de dommage hépatique, pas de traitement requis.</p>")),
        Section(id="newborn-bilirubin", level=2, heading="Bilirubine chez le nouveau-né",
                body_html=(
                    "<p>L&rsquo;ictère néonatal touche &gt; 60 % des nouveau-nés à terme. Souvent physiologique. "
                    "Des taux très élevés peuvent causer un ictère nucléaire. Photothérapie ou exsanguino-transfusion si nécessaire.</p>")),
        Section(id="related-tests", level=2, heading="Examens complémentaires",
                body_html=(
                    "<p>ALT, AST, <a href=\"/fr/blog/phosphatase-alcaline-elevee\">ALP</a>, <a href=\"/fr/blog/ggt-elevee-signification\">GGT</a>, albumine, protéines totales.</p>"
                    "<p>Hémolyse suspectée : réticulocytes, haptoglobine, LDH, Coombs direct. Obstruction : échographie ou CPRM.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter ?",
                body_html=(
                    "<p>Consultez si la bilirubine est élevée. Urgence en cas d&rsquo;ictère, urines foncées, selles décolorées ou douleur abdominale.</p>"
                    "<p>Nouveau-nés : alerter si ictère &lt; 24 h, progression rapide ou persistance &gt; 2 semaines.</p>")),
        Section(id="how-norya-helps", level=2, heading="Comment Norya vous aide",
                body_html=(
                    "<p>Norya ne diagnostique pas. Envoyez votre bilan sur <a href=\"/analyze\">noryaai.com/analyze</a>.</p>"
                    "<p>Tarifs : <a href=\"/pricing\">page tarifs</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html=(
                    '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> '
                    "Discutez toujours de vos résultats avec un professionnel de santé. <a href=\"/analyze\">Commencer l'analyse avec Norya</a></p>")),
    ]


# ---------------------------------------------------------------------------
# Italian
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirubina alta: cosa significa?",
                body_html=(
                    "<p>La bilirubina è un pigmento giallo nel pannello epatico. Quando è alta, la domanda è: c&rsquo;è un problema al fegato?</p>"
                    "<p>Questa guida spiega cos&rsquo;è la bilirubina, la differenza tra diretta e indiretta, i valori normali, le cause e quando consultare il medico.</p>")),
        Section(id="what-is-bilirubin", level=2, heading="Cos'è la bilirubina?",
                body_html=(
                    "<p><strong>La bilirubina</strong> deriva dalla degradazione dell&rsquo;eme dell&rsquo;emoglobina. La forma indiretta viene coniugata nel fegato, poi escreta nella bile.</p>"
                    "<p>Si misura in mg/dL o &mu;mol/L. I laboratori riportano bilirubina totale e diretta.</p>")),
        Section(id="direct-vs-indirect", level=2, heading="Diretta vs indiretta",
                body_html=(
                    "<p><strong>Indiretta</strong> elevata: emolisi, sindrome di Gilbert, ittero neonatale.</p>"
                    "<p><strong>Diretta</strong> elevata: ostruzione biliare, epatite, cirrosi, colestasi da farmaci.</p>")),
        Section(id="normal-ranges", level=2, heading="Valori normali della bilirubina",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parametro</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo (mg/dL)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Totale</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1&ndash;1,2</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Diretta</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0,3</td></tr>'
                    "</tbody></table>"
                    "<p>Nei neonati i valori sono molto più alti. Il digiuno può alzare temporaneamente la bilirubina indiretta.</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="Cause frequenti di bilirubina alta",
                body_html=(
                    "<p><strong>Produzione aumentata:</strong> anemie emolitiche. <strong>Coniugazione alterata:</strong> sindrome di Gilbert, ittero neonatale.</p>"
                    "<p><strong>Escrezione alterata:</strong> epatite, cirrosi, ostruzione biliare (calcoli, tumori).</p>")),
        Section(id="jaundice-connection", level=2, heading="Bilirubina e ittero",
                body_html=(
                    "<p>L&rsquo;<strong>ittero</strong> è visibile da ~2,5&ndash;3,0 mg/dL. Il profilo (urine scure, feci pallide) orienta sulla causa.</p>")),
        Section(id="gilbert-syndrome", level=2, heading="Sindrome di Gilbert: frequente e benigna",
                body_html=(
                    "<p>Colpisce il 5&ndash;10 % della popolazione. Elevazione lieve e fluttuante della bilirubina indiretta. "
                    "Benigna: nessun danno epatico, nessun trattamento necessario.</p>")),
        Section(id="newborn-bilirubin", level=2, heading="Bilirubina nei neonati",
                body_html=(
                    "<p>L&rsquo;ittero neonatale colpisce &gt; 60 % dei nati a termine. Di solito fisiologico. "
                    "Livelli molto alti possono causare kernittero. Fototerapia o exsanguinotrasfusione se necessario.</p>")),
        Section(id="related-tests", level=2, heading="Esami correlati",
                body_html=(
                    "<p>ALT, AST, <a href=\"/it/blog/fosfatasi-alcalina-alta\">ALP</a>, <a href=\"/it/blog/ggt-alta-significato\">GGT</a>, albumina, proteine totali.</p>"
                    "<p>Sospetta emolisi: reticolociti, aptoglobina, LDH, Coombs diretto. Ostruzione: ecografia o MRCP.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="Quando rivolgersi al medico",
                body_html=(
                    "<p>Parla con il medico se la bilirubina è alta. Urgenza in caso di ittero, urine scure, feci pallide o dolore addominale.</p>"
                    "<p>Nei neonati: avvisare se ittero &lt; 24 h, peggioramento rapido o durata &gt; 2 settimane.</p>")),
        Section(id="how-norya-helps", level=2, heading="Come Norya ti aiuta",
                body_html=(
                    "<p>Norya non fa diagnosi. Carica il referto su <a href=\"/analyze\">noryaai.com/analyze</a>.</p>"
                    "<p>Opzioni e prezzi: <a href=\"/pricing\">pagina prezzi</a>.</p>")),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html=(
                    '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> '
                    'Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>')),
    ]


# ---------------------------------------------------------------------------
# Hebrew
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="בילירובין גבוה: מה המשמעות?",
                body_html=(
                    "<p>בילירובין הוא פיגמנט צהוב בפאנל תפקודי כבד. כשהוא גבוה, השאלה: האם יש בעיה בכבד?</p>"
                    "<p>מדריך זה מסביר מהו בילירובין, ההבדל בין ישיר לעקיף, טווחים, גורמים לעלייה ומתי לפנות לרופא.</p>")),
        Section(id="what-is-bilirubin", level=2, heading="מהו בילירובין?",
                body_html=(
                    "<p><strong>בילירובין</strong> נוצר מפירוק ההם של ההמוגלובין. הצורה העקיפה מגיעה לכבד, מצומדת ומופרשת למרה.</p>"
                    "<p>נמדד ב-mg/dL או &mu;mol/L. המעבדה מדווחת בילירובין כולל וישיר; העקיף מחושב בהפחתה.</p>")),
        Section(id="direct-vs-indirect", level=2, heading="ישיר מול עקיף",
                body_html=(
                    "<p><strong>עקיף</strong> גבוה: המוליזה, תסמונת גילברט, צהבת יילודים.</p>"
                    "<p><strong>ישיר</strong> גבוה: חסימת דרכי מרה, דלקת כבד, שחמת, כולסטזיס תרופתי.</p>")),
        Section(id="normal-ranges", level=2, heading="טווחים תקינים של בילירובין",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">פרמטר</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח (mg/dL)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">כולל</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1&ndash;1.2</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">ישיר</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0.3</td></tr>'
                    "</tbody></table>"
                    "<p>ביילודים הערכים גבוהים בהרבה. צום יכול להעלות זמנית בילירובין עקיף, במיוחד בגילברט.</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="גורמים שכיחים לבילירובין גבוה",
                body_html=(
                    "<p><strong>ייצור מוגבר:</strong> אנמיות המוליטיות. <strong>צימוד לקוי:</strong> תסמונת גילברט, צהבת יילודים.</p>"
                    "<p><strong>הפרשה לקויה:</strong> דלקת כבד, שחמת, חסימת דרכי מרה (אבני מרה, גידולים).</p>")),
        Section(id="jaundice-connection", level=2, heading="בילירובין וצהבת",
                body_html=(
                    "<p><strong>צהבת</strong> נראית מ~2.5&ndash;3.0 mg/dL. הדפוס (שתן כהה, צואה בהירה) מכוון לגורם.</p>")),
        Section(id="gilbert-syndrome", level=2, heading="תסמונת גילברט: שכיחה ושפירה",
                body_html=(
                    "<p>פוגעת ב-5&ndash;10% מהאוכלוסייה. עליית בילירובין עקיף קלה ותנודתית. שפירה: אין נזק כבדי, אין צורך בטיפול.</p>")),
        Section(id="newborn-bilirubin", level=2, heading="בילירובין ביילודים",
                body_html=(
                    "<p>צהבת יילודים שכיחה מאוד (&gt;60% מלידות בזמן). בדרך כלל פיזיולוגית. "
                    "רמות גבוהות מאוד יכולות לגרום לקרניקטרוס. פוטותרפיה או עירוי חילופי לפי הצורך.</p>")),
        Section(id="related-tests", level=2, heading="בדיקות קשורות",
                body_html=(
                    "<p>ALT, AST, <a href=\"/he/blog/alp-high-meaning\">ALP</a>, <a href=\"/he/blog/ggt-high-meaning\">GGT</a>, אלבומין, חלבון כולל.</p>"
                    "<p>חשד להמוליזה: רטיקולוציטים, הפטוגלובין, LDH, קומבס ישיר. חסימה: אולטרסאונד בטן או MRCP.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא?",
                body_html=(
                    "<p>דברו עם הרופא אם הבילירובין גבוה. פנו בדחיפות בצהבת, שתן כהה, צואה בהירה או כאב בטן.</p>"
                    "<p>יילודים: דווחו אם צהבת &lt;24 שעות, מחמירה מהר או נמשכת &gt;2 שבועות.</p>")),
        Section(id="how-norya-helps", level=2, heading="איך Norya עוזרת",
                body_html=(
                    "<p>Norya לא מאבחנת. העלו את הדוח ב-<a href=\"/analyze\">noryaai.com/analyze</a>.</p>"
                    "<p>אפשרויות ומחירים: <a href=\"/pricing\">עמוד מחירים</a>.</p>")),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html=(
                    '<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> '
                    'דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>')),
    ]


# ---------------------------------------------------------------------------
# Hindi
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="बिलीरुबिन हाई: इसका क्या मतलब है?",
                body_html=(
                    "<p>बिलीरुबिन लिवर फ़ंक्शन पैनल में दिखने वाला एक पीला पिगमेंट है। हाई होने पर सवाल उठता है: क्या लिवर में समस्या है?</p>"
                    "<p>यह गाइड बताती है कि बिलीरुबिन क्या है, डायरेक्ट-इनडायरेक्ट का फ़र्क, नॉर्मल रेंज, बढ़ने के कारण और कब डॉक्टर से मिलें।</p>")),
        Section(id="what-is-bilirubin", level=2, heading="बिलीरुबिन क्या है?",
                body_html=(
                    "<p><strong>बिलीरुबिन</strong> हीमोग्लोबिन के हीम हिस्से के सामान्य टूटने से बनता है। "
                    "इनडायरेक्ट (अनकॉन्जुगेटेड) फ़ॉर्म लिवर में कॉन्जुगेट होकर बाइल में उत्सर्जित होता है।</p>"
                    "<p>mg/dL या &mu;mol/L में मापा जाता है। लैब टोटल और डायरेक्ट बिलीरुबिन रिपोर्ट करती है; इनडायरेक्ट घटाकर निकाला जाता है।</p>")),
        Section(id="direct-vs-indirect", level=2, heading="डायरेक्ट बनाम इनडायरेक्ट बिलीरुबिन",
                body_html=(
                    "<p><strong>इनडायरेक्ट</strong> हाई: हेमोलिसिस, गिल्बर्ट सिंड्रोम, नवजात पीलिया।</p>"
                    "<p><strong>डायरेक्ट</strong> हाई: बाइल डक्ट ऑब्स्ट्रक्शन, हेपेटाइटिस, सिरोसिस, ड्रग-इंड्यूस्ड कोलेस्टेसिस।</p>")),
        Section(id="normal-ranges", level=2, heading="सामान्य बिलीरुबिन रेंज",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">पैरामीटर</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">रेंज (mg/dL)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">टोटल</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1&ndash;1.2</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">डायरेक्ट</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0.3</td></tr>'
                    "</tbody></table>"
                    "<p>नवजातों में मान काफ़ी ज़्यादा होते हैं। उपवास इनडायरेक्ट बिलीरुबिन अस्थायी रूप से बढ़ा सकता है।</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="हाई बिलीरुबिन के कारण",
                body_html=(
                    "<p><strong>बढ़ा हुआ उत्पादन:</strong> हेमोलिटिक एनीमिया। <strong>लिवर कॉन्जुगेशन ख़राब:</strong> गिल्बर्ट सिंड्रोम, नवजात पीलिया।</p>"
                    "<p><strong>उत्सर्जन ख़राब:</strong> हेपेटाइटिस, सिरोसिस, बाइल डक्ट ऑब्स्ट्रक्शन (गॉलस्टोन, ट्यूमर)।</p>")),
        Section(id="jaundice-connection", level=2, heading="बिलीरुबिन और पीलिया",
                body_html=(
                    "<p><strong>पीलिया</strong> (जॉन्डिस) ~2.5&ndash;3.0 mg/dL से ऊपर दिखाई देता है। पैटर्न (डार्क यूरिन, पेल स्टूल) कारण की ओर इशारा करता है।</p>")),
        Section(id="gilbert-syndrome", level=2, heading="गिल्बर्ट सिंड्रोम: आम और हानिरहित",
                body_html=(
                    "<p>~5&ndash;10% आबादी को प्रभावित करता है। हल्की, उतार-चढ़ाव वाली इनडायरेक्ट बिलीरुबिन बढ़त। "
                    "हानिरहित: लिवर डैमेज नहीं, इलाज ज़रूरी नहीं।</p>")),
        Section(id="newborn-bilirubin", level=2, heading="नवजातों में बिलीरुबिन",
                body_html=(
                    "<p>नवजात पीलिया &gt;60% टर्म बेबीज़ को प्रभावित करता है। आमतौर पर फ़िज़ियोलॉजिकल। "
                    "बहुत ज़्यादा लेवल कर्निक्टेरस कर सकते हैं। फ़ोटोथेरेपी या एक्सचेंज ट्रांसफ़्यूज़न ज़रूरत पड़ने पर।</p>")),
        Section(id="related-tests", level=2, heading="संबंधित टेस्ट",
                body_html=(
                    "<p>ALT, AST, <a href=\"/hi/blog/alp-high-meaning\">ALP</a>, <a href=\"/hi/blog/ggt-high-meaning\">GGT</a>, एल्ब्यूमिन, टोटल प्रोटीन।</p>"
                    "<p>हेमोलिसिस शक: रेटिकुलोसाइट्स, हैप्टोग्लोबिन, LDH, डायरेक्ट कूम्ब्स। ऑब्स्ट्रक्शन: अल्ट्रासाउंड या MRCP।</p>")),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें?",
                body_html=(
                    "<p>बिलीरुबिन हाई हो तो डॉक्टर से बात करें। पीलिया, डार्क यूरिन, पेल स्टूल या पेट दर्द होने पर तुरंत अटेंशन लें।</p>"
                    "<p>नवजातों में: पीलिया &lt;24 घंटे, तेज़ी से बढ़ना या &gt;2 हफ़्ते बने रहना &mdash; पीडियाट्रिशन को सूचित करें।</p>")),
        Section(id="how-norya-helps", level=2, heading="Norya कैसे मदद करता है",
                body_html=(
                    "<p>Norya डायग्नोज़ नहीं करता। रिपोर्ट <a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें।</p>"
                    "<p>प्लान और कीमत: <a href=\"/pricing\">प्राइसिंग पेज</a>।</p>")),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html=(
                    '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> '
                    'अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>')),
    ]


# ---------------------------------------------------------------------------
# Arabic
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="البيليروبين مرتفع: ماذا يعني؟",
                body_html=(
                    "<p>البيليروبين صبغة صفراء في لوحة وظائف الكبد. حين يكون مرتفعاً، السؤال: هل هناك مشكلة في الكبد؟</p>"
                    "<p>يشرح هذا الدليل ما هو البيليروبين، الفرق بين المباشر وغير المباشر، النطاقات، الأسباب ومتى تستشير الطبيب.</p>")),
        Section(id="what-is-bilirubin", level=2, heading="ما هو البيليروبين؟",
                body_html=(
                    "<p><strong>البيليروبين</strong> ينتج من تحلل الهيم في الهيموغلوبين. الشكل غير المباشر يصل للكبد حيث يُقترن ويُفرز في الصفراء.</p>"
                    "<p>يُقاس بـ mg/dL أو &mu;mol/L. المختبر يبلغ عن الكلي والمباشر؛ غير المباشر يُحسب بالطرح.</p>")),
        Section(id="direct-vs-indirect", level=2, heading="مباشر مقابل غير مباشر",
                body_html=(
                    "<p><strong>غير المباشر</strong> مرتفع: انحلال دم، متلازمة جيلبرت، يرقان حديثي الولادة.</p>"
                    "<p><strong>المباشر</strong> مرتفع: انسداد قنوات صفراوية، التهاب كبد، تشمع، ركود صفراوي دوائي.</p>")),
        Section(id="normal-ranges", level=2, heading="النطاقات الطبيعية للبيليروبين",
                body_html=(
                    '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                    "<thead><tr>"
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">المعامل</th>'
                    '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">النطاق (mg/dL)</th>'
                    "</tr></thead><tbody>"
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">الكلي</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1&ndash;1.2</td></tr>'
                    '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">المباشر</td><td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0.3</td></tr>'
                    "</tbody></table>"
                    "<p>عند حديثي الولادة القيم أعلى بكثير. الصيام يمكن أن يرفع البيليروبين غير المباشر مؤقتاً.</p>")),
        Section(id="high-bilirubin-causes", level=2, heading="أسباب شائعة لارتفاع البيليروبين",
                body_html=(
                    "<p><strong>إنتاج زائد:</strong> فقر دم انحلالي. <strong>اقتران معطل:</strong> متلازمة جيلبرت، يرقان وليدي.</p>"
                    "<p><strong>إفراز معطل:</strong> التهاب كبد، تشمع، انسداد قنوات صفراوية (حصى، أورام).</p>")),
        Section(id="jaundice-connection", level=2, heading="البيليروبين واليرقان",
                body_html=(
                    "<p><strong>اليرقان</strong> يظهر من ~2.5&ndash;3.0 mg/dL. النمط (بول داكن، براز شاحب) يوجه للسبب.</p>")),
        Section(id="gilbert-syndrome", level=2, heading="متلازمة جيلبرت: شائعة وحميدة",
                body_html=(
                    "<p>تصيب 5&ndash;10% من السكان. ارتفاع خفيف ومتذبذب في البيليروبين غير المباشر. حميدة: لا ضرر كبدي ولا حاجة لعلاج.</p>")),
        Section(id="newborn-bilirubin", level=2, heading="البيليروبين عند حديثي الولادة",
                body_html=(
                    "<p>يرقان حديثي الولادة يصيب &gt;60% من المواليد بأوانهم. عادة فسيولوجي. "
                    "مستويات عالية جداً قد تسبب اليرقان النووي. العلاج الضوئي أو نقل الدم التبادلي عند الحاجة.</p>")),
        Section(id="related-tests", level=2, heading="فحوصات ذات صلة",
                body_html=(
                    "<p>ALT، AST، <a href=\"/ar/blog/alp-high-meaning\">ALP</a>، <a href=\"/ar/blog/ggt-high-meaning\">GGT</a>، ألبومين، بروتين كلي.</p>"
                    "<p>اشتباه انحلال: خلايا شبكية، هابتوغلوبين، LDH، كومبس مباشر. انسداد: تصوير بالأمواج أو MRCP.</p>")),
        Section(id="when-to-see-doctor", level=2, heading="متى تراجع الطبيب؟",
                body_html=(
                    "<p>تحدث مع طبيبك إذا كان البيليروبين مرتفعاً. اطلب مساعدة عاجلة عند يرقان أو بول داكن أو براز شاحب أو ألم بطن.</p>"
                    "<p>حديثو الولادة: أبلغ الطبيب إذا اليرقان &lt;24 ساعة أو يتفاقم بسرعة أو يستمر &gt;أسبوعين.</p>")),
        Section(id="how-norya-helps", level=2, heading="كيف تساعد Norya",
                body_html=(
                    "<p>Norya لا تُشخّص. ارفع تقريرك على <a href=\"/analyze\">noryaai.com/analyze</a>.</p>"
                    "<p>الخيارات والأسعار: <a href=\"/pricing\">صفحة الأسعار</a>.</p>")),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html=(
                    '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> '
                    'ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>')),
    ]


# ============================================================================
# Public API
# ============================================================================

def get_bilirubin_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for bilirubin article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_bilirubin_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for bilirubin article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a normal bilirubin level?", "answer": "Normal total bilirubin is roughly 0.1–1.2 mg/dL (1.7–20.5 μmol/L) and direct bilirubin is 0–0.3 mg/dL. Ranges may vary between labs."},
            {"question": "What causes high bilirubin?", "answer": "Common causes include haemolytic anaemia (increased RBC breakdown), liver diseases (hepatitis, cirrhosis), bile duct obstruction (gallstones, tumours), Gilbert's syndrome, and certain medications."},
            {"question": "What is Gilbert's syndrome?", "answer": "Gilbert's syndrome is a common, benign genetic condition affecting 5–10% of the population. It causes mild, fluctuating elevation of unconjugated bilirubin due to reduced activity of the conjugating enzyme. It requires no treatment."},
            {"question": "What is the difference between direct and indirect bilirubin?", "answer": "Indirect (unconjugated) bilirubin has not yet been processed by the liver and rises with haemolysis or impaired conjugation. Direct (conjugated) bilirubin has been processed and rises when bile flow is obstructed or the liver is damaged."},
            {"question": "When should I worry about high bilirubin?", "answer": "See a doctor if bilirubin is elevated on your blood test. Seek prompt attention if you notice jaundice (yellow skin/eyes), dark urine, pale stools, or abdominal pain."},
        ],
        "tr": [
            {"question": "Normal bilirubin değeri nedir?", "answer": "Toplam bilirubin yaklaşık 0,1–1,2 mg/dL, direkt bilirubin 0–0,3 mg/dL normal kabul edilir."},
            {"question": "Bilirubin yüksekliğine ne sebep olur?", "answer": "Hemolitik anemi, karaciğer hastalıkları, safra yolu tıkanıklığı, Gilbert sendromu ve bazı ilaçlar yaygın nedenlerdir."},
            {"question": "Gilbert sendromu nedir?", "answer": "Popülasyonun %5–10'unu etkileyen yaygın, iyi huylu genetik bir durumdur. Konjügasyon enziminin azalmış aktivitesi nedeniyle hafif, dalgalanan indirekt bilirubin yüksekliğine neden olur. Tedavi gerektirmez."},
            {"question": "Direkt ve indirekt bilirubin farkı nedir?", "answer": "İndirekt bilirubin henüz karaciğer tarafından işlenmemiştir; hemoliz veya bozulmuş konjügasyonda yükselir. Direkt bilirubin işlenmiş formudur; safra akışı tıkandığında veya karaciğer hasar gördüğünde yükselir."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de bilirrubina?", "answer": "Total: 0,1–1,2 mg/dL. Directa: 0–0,3 mg/dL. Puede variar según el laboratorio."},
            {"question": "¿Qué causa la bilirrubina alta?", "answer": "Anemia hemolítica, enfermedades hepáticas, obstrucción biliar, síndrome de Gilbert y ciertos fármacos."},
            {"question": "¿Qué es el síndrome de Gilbert?", "answer": "Condición genética benigna que afecta al 5–10% de la población. Causa elevación leve y fluctuante de la bilirrubina indirecta. No requiere tratamiento."},
        ],
        "de": [
            {"question": "Was ist ein normaler Bilirubinwert?", "answer": "Gesamt: ca. 0,1–1,2 mg/dL. Direkt: 0–0,3 mg/dL. Laborabhängig."},
            {"question": "Was verursacht erhöhtes Bilirubin?", "answer": "Hämolytische Anämien, Lebererkrankungen, Gallengangsobstruktion, Morbus Gilbert und bestimmte Medikamente."},
            {"question": "Was ist Morbus Gilbert?", "answer": "Eine häufige, harmlose genetische Störung (5–10% der Bevölkerung). Verursacht leichte, schwankende indirekte Hyperbilirubinämie. Keine Behandlung nötig."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de bilirubine ?", "answer": "Totale : environ 0,1–1,2 mg/dL. Directe : 0–0,3 mg/dL. Variable selon le laboratoire."},
            {"question": "Quelles sont les causes d'une bilirubine élevée ?", "answer": "Anémies hémolytiques, maladies hépatiques, obstruction biliaire, syndrome de Gilbert et certains médicaments."},
            {"question": "Qu'est-ce que le syndrome de Gilbert ?", "answer": "Affection génétique bénigne touchant 5–10 % de la population. Élévation légère de la bilirubine indirecte. Pas de traitement nécessaire."},
        ],
        "it": [
            {"question": "Qual è il valore normale della bilirubina?", "answer": "Totale: circa 0,1–1,2 mg/dL. Diretta: 0–0,3 mg/dL. Può variare tra laboratori."},
            {"question": "Cosa causa la bilirubina alta?", "answer": "Anemie emolitiche, malattie epatiche, ostruzione biliare, sindrome di Gilbert e alcuni farmaci."},
            {"question": "Cos'è la sindrome di Gilbert?", "answer": "Condizione genetica benigna che colpisce il 5–10% della popolazione. Causa elevazione lieve della bilirubina indiretta. Non richiede trattamento."},
        ],
        "he": [
            {"question": "מהו ערך בילירובין תקין?", "answer": "כולל: כ-0.1–1.2 mg/dL. ישיר: 0–0.3 mg/dL. עשוי להשתנות בין מעבדות."},
            {"question": "מה גורם לבילירובין גבוה?", "answer": "אנמיות המוליטיות, מחלות כבד, חסימת דרכי מרה, תסמונת גילברט ותרופות מסוימות."},
            {"question": "מהי תסמונת גילברט?", "answer": "מצב גנטי שפיר שפוגע ב-5–10% מהאוכלוסייה. גורם לעלייה קלה ותנודתית בבילירובין עקיף. אין צורך בטיפול."},
        ],
        "hi": [
            {"question": "सामान्य बिलीरुबिन कितना होना चाहिए?", "answer": "टोटल: लगभग 0.1–1.2 mg/dL। डायरेक्ट: 0–0.3 mg/dL। लैब के अनुसार भिन्न हो सकता है।"},
            {"question": "हाई बिलीरुबिन किससे होता है?", "answer": "हेमोलिटिक एनीमिया, लिवर डिजीज़, बाइल डक्ट ऑब्स्ट्रक्शन, गिल्बर्ट सिंड्रोम और कुछ दवाएं।"},
            {"question": "गिल्बर्ट सिंड्रोम क्या है?", "answer": "~5–10% आबादी को प्रभावित करने वाला हानिरहित जेनेटिक कंडीशन। इनडायरेक्ट बिलीरुबिन हल्का बढ़ता है। इलाज ज़रूरी नहीं।"},
        ],
        "ar": [
            {"question": "ما هو مستوى البيليروبين الطبيعي؟", "answer": "الكلي: حوالي 0.1–1.2 mg/dL. المباشر: 0–0.3 mg/dL. قد يختلف بين المختبرات."},
            {"question": "ما أسباب ارتفاع البيليروبين؟", "answer": "فقر دم انحلالي، أمراض كبد، انسداد قنوات صفراوية، متلازمة جيلبرت وبعض الأدوية."},
            {"question": "ما هي متلازمة جيلبرت؟", "answer": "حالة وراثية حميدة تصيب 5–10% من السكان. ارتفاع خفيف ومتذبذب في البيليروبين غير المباشر. لا تحتاج علاجاً."},
        ],
    }
