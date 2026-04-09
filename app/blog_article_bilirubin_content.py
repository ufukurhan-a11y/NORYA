# -*- coding: utf-8 -*-
"""
Bilirubin blog article — full body content for all 9 languages.
Used by blog_i18n._article_bilirubin().
Sections: intro, what-is-bilirubin, direct-vs-indirect, normal-ranges,
high-bilirubin-causes, jaundice-connection, gilbert-syndrome,
newborn-bilirubin, related-tests, when-to-see-doctor,
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
            heading="Bilirubin yüksekliği ne anlama gelir? Kapsamlı rehber",
            body_html=(
                "<p><strong>Bilirubin</strong>, hemoglobin yıkımı sonucu oluşan sarı-turuncu renkli bir pigmenttir. "
                "Karaciğer fonksiyon testlerinin temel bileşenlerinden biri olan bilirubin, karaciğer, safra yolları ve "
                "kırmızı kan hücresi yıkımı hakkında değerli bilgi sağlar. Kanda bilirubin seviyesinin yükselmesi "
                "<strong>hiperbilirubinemi</strong> olarak adlandırılır ve cilt ile gözlerde sararma "
                "(<strong>sarılık/ikter</strong>) ile kendini gösterebilir.</p>"
                "<p>Bilirubin yüksekliğinin nedenleri karaciğer hastalığından hemolitik anemiye, safra yolu tıkanıklığından "
                "genetik durumlara (Gilbert sendromu) kadar geniş bir yelpazeyi kapsar. Ayrıca yenidoğan döneminde "
                "fizyolojik sarılık son derece yaygındır.</p>"
                "<p>Bu rehber bilgilendirme amaçlıdır ve tıbbi tavsiye yerine geçmez.</p>"
            ),
        ),
        Section(
            id="what-is-bilirubin", level=2,
            heading="Bilirubin nedir ve nasıl oluşur?",
            body_html=(
                "<p><strong>Bilirubin</strong>, yaşlanan kırmızı kan hücrelerinin dalak ve karaciğerdeki retiküloendotelyal sistem "
                "tarafından parçalanması sırasında <em>hem</em> grubunun yıkımından oluşur. Günlük bilirubin üretiminin yaklaşık "
                "%80&rsquo;i eritrosit hemoglobininden gelir; kalan %20 miyoglobin, sitokromlar ve diğer hem proteinlerinden kaynaklanır.</p>"
                "<p>Bilirubin metabolizmasının temel adımları:</p>"
                "<ul>"
                "<li><strong>Üretim</strong> &ndash; hem, hem oksijenaz enzimi ile biliverdin&rsquo;e, ardından biliverdin reduktaz "
                "ile <strong>indirekt (konjuge olmamış) bilirubin</strong>&rsquo;e dönüştürülür.</li>"
                "<li><strong>Taşınma</strong> &ndash; indirekt bilirubin suda çözünmez; kanda albümine bağlı olarak taşınır.</li>"
                "<li><strong>Konjugasyon</strong> &ndash; karaciğer hepatositlerinde UDP-glukuronil transferaz (UGT1A1) enzimi "
                "tarafından glukuronik asitle konjuge edilerek <strong>direkt (konjuge) bilirubin</strong>&rsquo;e dönüştürülür.</li>"
                "<li><strong>Atılım</strong> &ndash; direkt bilirubin safra ile bağırsağa atılır, burada bakteriler tarafından "
                "ürobilinojen&rsquo;e dönüştürülür. Bir kısmı feçesle sterkobilin olarak atılırken bir kısmı emilip böbreklerden "
                "ürobilin olarak idrara geçer.</li>"
                "</ul>"
                "<p>Bu metabolizma zincirinin herhangi bir aşamasındaki bozukluk bilirubin yükselmesine neden olabilir.</p>"
            ),
        ),
        Section(
            id="direct-vs-indirect", level=2,
            heading="Direkt ve indirekt bilirubin farkı",
            body_html=(
                "<p>Bilirubin iki ana formda ölçülür:</p>"
                "<ul>"
                "<li><strong>İndirekt (konjuge olmamış) bilirubin</strong> &ndash; karaciğerde henüz işlenmemiş, suda çözünmeyen form. "
                "Yükselmesi genellikle aşırı kırmızı kan hücresi yıkımını (hemoliz) veya karaciğerin konjugasyon kapasitesinin "
                "yetersizliğini (Gilbert sendromu) gösterir.</li>"
                "<li><strong>Direkt (konjuge) bilirubin</strong> &ndash; karaciğerde işlenmiş, suda çözünür form. "
                "Yükselmesi genellikle karaciğer hasarını veya safra yolu tıkanıklığını (kolestaz) gösterir; "
                "çünkü konjuge bilirubin karaciğerden safra ile atılamaz hale gelmiştir.</li>"
                "</ul>"
                "<p><strong>Toplam bilirubin</strong> = direkt + indirekt. Laboratuvar sonuçlarında genellikle toplam ve direkt "
                "bilirubin rapor edilir; indirekt değer farktan hesaplanır. Hangi fraksiyonun yüksek olduğu, bilirubinin yükselme "
                "nedenini anlamak için kritik önem taşır.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal bilirubin değerleri",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parametre</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Aralık</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Toplam bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1&ndash;1,2 mg/dL (1,7&ndash;20,5 &micro;mol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Direkt (konjuge) bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0,3 mg/dL (0&ndash;5,1 &micro;mol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">İndirekt (konjuge olmamış) bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,1&ndash;0,9 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Bilirubin 2,5&ndash;3&nbsp;mg/dL&rsquo;nin üzerine çıktığında klinik olarak sarılık (ikter) belirginleşir. "
                "Referans aralıkları laboratuvarlar arasında hafif farklılık gösterebilir.</p>"
            ),
        ),
        Section(
            id="high-bilirubin-causes", level=2,
            heading="Bilirubin yüksekliğinin nedenleri",
            body_html=(
                "<p>Bilirubin yüksekliği üç ana kategoride sınıflandırılır:</p>"
                "<p><strong>1. Pre-hepatik (hemolitik) nedenler &ndash; indirekt bilirubin yüksek:</strong></p>"
                "<ul>"
                "<li>Hemolitik anemiler (otoimmün, orak hücreli anemi, G6PD eksikliği, talasemi)</li>"
                "<li>Kan transfüzyon reaksiyonları</li>"
                "<li>Büyük hematomların emilimi</li>"
                "<li>İnefektif eritropoez (B12 eksikliği, miyelodisplastik sendrom)</li>"
                "</ul>"
                "<p><strong>2. Hepatik nedenler &ndash; karma veya direkt/indirekt yüksek:</strong></p>"
                "<ul>"
                "<li>Viral hepatitler (A, B, C, E)</li>"
                "<li>Alkolik hepatit ve siroz</li>"
                "<li>İlaç kaynaklı karaciğer hasarı (parasetamol, izoniazid, statinler)</li>"
                "<li>Otoimmün hepatit</li>"
                "<li>Wilson hastalığı, hemokromatozis</li>"
                "<li>Gilbert sendromu ve Crigler-Najjar sendromu (konjugasyon bozuklukları)</li>"
                "</ul>"
                "<p><strong>3. Post-hepatik (obstrüktif) nedenler &ndash; direkt bilirubin yüksek:</strong></p>"
                "<ul>"
                "<li>Safra taşları (kolelitiyazis)</li>"
                "<li>Safra kanalı darlığı veya tümörü</li>"
                "<li>Pankreas başı tümörü</li>"
                "<li>Primer sklerozan kolanjit</li>"
                "</ul>"
                "<p>Hangi fraksiyonun baskın olarak yükseldiği, doktorun tanıya yönelik araştırmasını yönlendirir.</p>"
            ),
        ),
        Section(
            id="jaundice-connection", level=2,
            heading="Sarılık (ikter) ve bilirubin",
            body_html=(
                "<p><strong>Sarılık</strong>, bilirubinin cilt, mukoza ve göz aklarında (sklera) birikmesi sonucu oluşan "
                "sarı-yeşil renk değişimidir. Genellikle toplam bilirubin 2,5&ndash;3&nbsp;mg/dL&rsquo;nin üzerine çıktığında "
                "klinik olarak görünür hale gelir. İlk bulgu genellikle <strong>skleral ikter</strong> (göz beyazlarının sararması) "
                "olup bilirubin daha da yükseldiğinde cilt de sararır.</p>"
                "<p>Sarılığa eşlik edebilecek diğer bulgular:</p>"
                "<ul>"
                "<li><strong>Koyu renkli idrar (çay rengi)</strong> &ndash; direkt bilirubin böbreklerden atılır</li>"
                "<li><strong>Açık renkli (akolik) dışkı</strong> &ndash; safra yolu tıkanıklığında sterkobilinin olmaması</li>"
                "<li><strong>Kaşıntı (pruritus)</strong> &ndash; kolestazda safra asitlerinin deride birikmesi</li>"
                "<li><strong>Karın ağrısı</strong> &ndash; özellikle safra taşlarında sağ üst kadran ağrısı</li>"
                "</ul>"
                "<p>Yenidoğanlarda fizyolojik sarılık doğumun 2&ndash;3. gününde başlar ve genellikle 1&ndash;2 hafta "
                "içinde kendiliğinden düzelir. Ancak çok yüksek seviyelerde (>20&nbsp;mg/dL) nörotoksisite (kernikterus) "
                "riski nedeniyle fototerapi veya exchange transfüzyon gerekebilir.</p>"
            ),
        ),
        Section(
            id="gilbert-syndrome", level=2,
            heading="Gilbert sendromu",
            body_html=(
                "<p><strong>Gilbert sendromu</strong>, UGT1A1 enzim aktivitesinin genetik olarak azalması sonucu ortaya çıkan, "
                "en yaygın kalıtsal bilirubin metabolizma bozukluğudur. Genel popülasyonun yaklaşık <strong>%3&ndash;7</strong>&rsquo;sini "
                "etkiler ve genellikle ergenlik döneminde keşfedilir.</p>"
                "<p>Temel özellikleri:</p>"
                "<ul>"
                "<li>Hafif, tekrarlayan indirekt bilirubin yüksekliği (genellikle 1&ndash;3&nbsp;mg/dL, bazen 5&nbsp;mg/dL&rsquo;ye kadar)</li>"
                "<li>Açlık, stres, egzersiz veya hastalık dönemlerinde alevlenmeler</li>"
                "<li>Karaciğer fonksiyon testleri (ALT, AST, ALP) normaldir</li>"
                "<li>Hemoliz bulgusu yoktur (retikülosit, haptoglobin, LDH normal)</li>"
                "<li>Tedavi gerektirmez; prognoz mükemmeldir</li>"
                "</ul>"
                "<p>Gilbert sendromu iyi huylu bir durumdur ve karaciğer hasarına yol açmaz. Ancak bazı ilaçların "
                "(özellikle irinotekan gibi UGT1A1 ile metabolize edilen ilaçlar) metabolizmasını etkileyebilir; "
                "bu nedenle doktorunuzun durumdan haberdar olması önemlidir.</p>"
            ),
        ),
        Section(
            id="newborn-bilirubin", level=2,
            heading="Yenidoğan sarılığı (neonatal hiperbilirubinemi)",
            body_html=(
                "<p>Yenidoğanlarda sarılık son derece yaygındır ve term bebeklerin yaklaşık <strong>%60&rsquo;ında</strong>, "
                "prematüre bebeklerin %80&rsquo;inde görülür. Nedenleri arasında fetal hemoglobinin (HbF) hızlı yıkımı, "
                "karaciğerin henüz olgunlaşmamış konjugasyon kapasitesi ve artmış enterohepatik dolaşım sayılabilir.</p>"
                "<p><strong>Fizyolojik sarılık</strong> yaşamın 2&ndash;3. gününde başlar, 4&ndash;5. günde zirve yapar ve "
                "genellikle 1&ndash;2 hafta içinde düzelir. <strong>Patolojik sarılık</strong> ise ilk 24 saatte başlayan, "
                "çok hızlı yükselen veya uzun süre devam eden sarılığı kapsar.</p>"
                "<p>Çok yüksek bilirubin seviyeleri (&gt;20&ndash;25&nbsp;mg/dL) yenidoğanda <strong>kernikterus</strong> "
                "(bilirubin ensefalopatisi) riskini artırır&mdash;bilirubinin beyin dokusunda birikmesi sonucu kalıcı "
                "nörolojik hasara yol açabilir. Tedavi seçenekleri arasında <strong>fototerapi</strong> (mavi ışık) ve "
                "ağır vakalarda <strong>exchange transfüzyon</strong> yer alır.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="İlgili testler",
            body_html=(
                "<p>Bilirubin yüksekliğinin nedeni araştırılırken aşağıdaki testler de değerlendirilir:</p>"
                "<ul>"
                "<li><strong>ALT ve AST</strong> &ndash; hepatosellüler hasar belirteçleri</li>"
                "<li><strong>ALP</strong> &ndash; kolestatik hasar belirteci</li>"
                "<li><strong>GGT</strong> &ndash; ALP yüksekliğinin kaynağını ayırt etmeye yardımcı</li>"
                "<li><strong>Albümin</strong> &ndash; karaciğerin sentez fonksiyonunu gösterir</li>"
                "<li><strong>Tam kan sayımı</strong> &ndash; hemoliz araştırması</li>"
                "<li><strong>Retikülosit sayısı</strong> &ndash; hemolitik anemi araştırması</li>"
                "<li><strong>Haptoglobin ve LDH</strong> &ndash; hemoliz belirteçleri</li>"
                "<li><strong>Direkt ve indirekt Coombs testi</strong> &ndash; otoimmün hemoliz araştırması</li>"
                "<li><strong>Abdominal ultrason</strong> &ndash; safra taşları ve safra yolu dilatasyonu araştırması</li>"
                "</ul>"
                "<p>Bu testlerin kombinasyonu bilirubinin yükselme nedenini pre-hepatik, hepatik veya post-hepatik olarak "
                "sınıflandırmaya yardımcı olur.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Doktora ne zaman başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda doktora başvurun:</p>"
                "<ul>"
                "<li>Bilirubin değeriniz yüksek çıktıysa</li>"
                "<li>Cildinizde veya gözlerinizde sararma fark ettiyseniz</li>"
                "<li>İdrarınız koyu çay renginde ise</li>"
                "<li>Dışkınız normalden açık renkli veya beyaz ise</li>"
                "<li>Sağ üst karında ağrı, bulantı veya kaşıntı varsa</li>"
                "</ul>"
                "<p><strong>Acil durum:</strong> Ateş ile birlikte sarılık, şiddetli karın ağrısı, mental durum değişikliği "
                "veya yenidoğanda derin sarılık acil tıbbi değerlendirme gerektirir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya nasıl yardımcı olur?",
            body_html=(
                "<p>Norya teşhis koymaz&mdash;doktor ziyaretinize hazırlanmanıza yardımcı olur. "
                "Kan tahlili raporunuzu <a href=\"/analyze\">noryaai.com/analyze</a> sayfasına yükleyin; analiz motorumuz "
                "toplam, direkt ve indirekt bilirubin ile ALT, AST, ALP, GGT ve diğer karaciğer belirteçlerini otomatik "
                "olarak çıkarır, referans aralıklarıyla karşılaştırır ve yapılandırılmış bir rapor oluşturur.</p>"
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
            heading="High bilirubin: what does it mean? A comprehensive guide",
            body_html=(
                "<p><strong>Bilirubin</strong> is a yellow-orange pigment produced from the breakdown of haemoglobin in ageing red "
                "blood cells. It is a core component of liver function tests and provides valuable insight into the health of the "
                "<strong>liver, bile ducts, and red blood cell turnover</strong>. Elevated bilirubin in the blood is called "
                "<strong>hyperbilirubinaemia</strong> and may manifest as yellowing of the skin and eyes (<strong>jaundice</strong>).</p>"
                "<p>The causes of high bilirubin range from liver disease and haemolytic anaemia to bile duct obstruction and "
                "genetic conditions such as Gilbert syndrome. Neonatal jaundice is also extremely common in newborns.</p>"
                "<p>This guide is educational and does not replace medical advice.</p>"
            ),
        ),
        Section(
            id="what-is-bilirubin", level=2,
            heading="What is bilirubin and how is it produced?",
            body_html=(
                "<p><strong>Bilirubin</strong> is formed when the <em>haem</em> component of haemoglobin is broken down by the "
                "reticuloendothelial system (primarily in the spleen and liver). Approximately 80% of daily bilirubin production "
                "comes from red blood cell haemoglobin; the remaining 20% comes from myoglobin, cytochromes, and other haem proteins.</p>"
                "<p>The key steps in bilirubin metabolism are:</p>"
                "<ul>"
                "<li><strong>Production</strong> &ndash; haem is converted to biliverdin by haem oxygenase, then to "
                "<strong>unconjugated (indirect) bilirubin</strong> by biliverdin reductase.</li>"
                "<li><strong>Transport</strong> &ndash; unconjugated bilirubin is water-insoluble and travels in the blood bound "
                "to albumin.</li>"
                "<li><strong>Conjugation</strong> &ndash; in hepatocytes, the enzyme UDP-glucuronosyltransferase (UGT1A1) conjugates "
                "bilirubin with glucuronic acid, producing <strong>conjugated (direct) bilirubin</strong>.</li>"
                "<li><strong>Excretion</strong> &ndash; conjugated bilirubin is excreted into bile, enters the intestine, and is "
                "converted by bacteria to urobilinogen. Some is excreted as stercobilin in faeces (brown colour); some is "
                "reabsorbed and excreted as urobilin in urine (yellow colour).</li>"
                "</ul>"
                "<p>A disruption at any step of this pathway can cause bilirubin to rise.</p>"
            ),
        ),
        Section(
            id="direct-vs-indirect", level=2,
            heading="Direct vs. indirect bilirubin",
            body_html=(
                "<p>Bilirubin is measured in two main fractions:</p>"
                "<ul>"
                "<li><strong>Indirect (unconjugated) bilirubin</strong> &ndash; the form that has not yet been processed by the liver. "
                "It is water-insoluble. Elevation typically indicates excessive red blood cell destruction (haemolysis) or impaired "
                "hepatic conjugation (e.g. Gilbert syndrome).</li>"
                "<li><strong>Direct (conjugated) bilirubin</strong> &ndash; the liver-processed, water-soluble form. Elevation usually "
                "indicates liver damage or bile duct obstruction (cholestasis), because the conjugated bilirubin cannot be excreted "
                "normally.</li>"
                "</ul>"
                "<p><strong>Total bilirubin</strong> = direct + indirect. Laboratory reports typically provide total and direct "
                "values; indirect is calculated by subtraction. Knowing which fraction is elevated is critical for determining "
                "the underlying cause.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal bilirubin ranges",
            body_html=(
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Parameter</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Normal Range</th>'
                "</tr></thead><tbody>"
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Total bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1&ndash;1.2 mg/dL (1.7&ndash;20.5 &micro;mol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Direct (conjugated) bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0&ndash;0.3 mg/dL (0&ndash;5.1 &micro;mol/L)</td></tr>'
                '<tr><td style="border:1px solid #cbd5e1;padding:8px 12px;">Indirect (unconjugated) bilirubin</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.1&ndash;0.9 mg/dL</td></tr>'
                "</tbody></table>"
                "<p>Clinical jaundice typically becomes apparent when total bilirubin exceeds 2.5&ndash;3&nbsp;mg/dL. "
                "Reference ranges may vary slightly between laboratories.</p>"
            ),
        ),
        Section(
            id="high-bilirubin-causes", level=2,
            heading="Causes of high bilirubin",
            body_html=(
                "<p>Elevated bilirubin is classified into three main categories:</p>"
                "<p><strong>1. Pre-hepatic (haemolytic) causes &ndash; indirect bilirubin elevated:</strong></p>"
                "<ul>"
                "<li>Haemolytic anaemias (autoimmune, sickle cell, G6PD deficiency, thalassaemia)</li>"
                "<li>Blood transfusion reactions</li>"
                "<li>Resorption of large haematomas</li>"
                "<li>Ineffective erythropoiesis (B12 deficiency, myelodysplastic syndrome)</li>"
                "</ul>"
                "<p><strong>2. Hepatic causes &ndash; mixed or direct/indirect elevation:</strong></p>"
                "<ul>"
                "<li>Viral hepatitis (A, B, C, E)</li>"
                "<li>Alcoholic hepatitis and cirrhosis</li>"
                "<li>Drug-induced liver injury (paracetamol, isoniazid, statins)</li>"
                "<li>Autoimmune hepatitis</li>"
                "<li>Wilson disease, haemochromatosis</li>"
                "<li>Gilbert syndrome and Crigler-Najjar syndrome (conjugation defects)</li>"
                "</ul>"
                "<p><strong>3. Post-hepatic (obstructive) causes &ndash; direct bilirubin elevated:</strong></p>"
                "<ul>"
                "<li>Gallstones (cholelithiasis)</li>"
                "<li>Bile duct stricture or tumour</li>"
                "<li>Pancreatic head tumour</li>"
                "<li>Primary sclerosing cholangitis</li>"
                "</ul>"
                "<p>Identifying which fraction is predominantly elevated guides the clinician&rsquo;s diagnostic workup.</p>"
            ),
        ),
        Section(
            id="jaundice-connection", level=2,
            heading="Jaundice and bilirubin",
            body_html=(
                "<p><strong>Jaundice (icterus)</strong> is the yellow-green discolouration of the skin, mucous membranes, and "
                "sclerae (whites of the eyes) caused by bilirubin accumulation in tissues. It typically becomes clinically visible "
                "when total bilirubin exceeds 2.5&ndash;3&nbsp;mg/dL. The first sign is usually <strong>scleral icterus</strong>.</p>"
                "<p>Associated findings may include:</p>"
                "<ul>"
                "<li><strong>Dark urine (tea-coloured)</strong> &ndash; direct bilirubin is excreted by the kidneys</li>"
                "<li><strong>Pale (acholic) stools</strong> &ndash; absence of stercobilin due to bile duct obstruction</li>"
                "<li><strong>Pruritus (itching)</strong> &ndash; bile acid deposition in the skin during cholestasis</li>"
                "<li><strong>Abdominal pain</strong> &ndash; especially right upper quadrant pain in gallstone disease</li>"
                "</ul>"
                "<p>In newborns, physiological jaundice begins around day 2&ndash;3 of life and usually resolves within 1&ndash;2 "
                "weeks. However, very high levels (&gt;20&nbsp;mg/dL) carry a risk of neurotoxicity (kernicterus) and may require "
                "phototherapy or exchange transfusion.</p>"
            ),
        ),
        Section(
            id="gilbert-syndrome", level=2,
            heading="Gilbert syndrome",
            body_html=(
                "<p><strong>Gilbert syndrome</strong> is the most common inherited disorder of bilirubin metabolism, caused by "
                "reduced activity of the UGT1A1 enzyme. It affects approximately <strong>3&ndash;7%</strong> of the general "
                "population and is typically discovered in adolescence or early adulthood.</p>"
                "<p>Key features:</p>"
                "<ul>"
                "<li>Mild, intermittent unconjugated (indirect) hyperbilirubinaemia (usually 1&ndash;3&nbsp;mg/dL, occasionally "
                "up to 5&nbsp;mg/dL)</li>"
                "<li>Exacerbations triggered by fasting, stress, exercise, or illness</li>"
                "<li>Liver function tests (ALT, AST, ALP) are normal</li>"
                "<li>No evidence of haemolysis (reticulocytes, haptoglobin, LDH are normal)</li>"
                "<li>No treatment required; prognosis is excellent</li>"
                "</ul>"
                "<p>Gilbert syndrome is benign and does not cause liver damage. However, it can affect the metabolism of certain "
                "drugs (particularly those metabolised by UGT1A1, such as irinotecan), so it is important for your doctor to be "
                "aware of the condition.</p>"
            ),
        ),
        Section(
            id="newborn-bilirubin", level=2,
            heading="Newborn jaundice (neonatal hyperbilirubinaemia)",
            body_html=(
                "<p>Neonatal jaundice is extremely common, occurring in approximately <strong>60%</strong> of term infants and "
                "80% of preterm infants. Contributing factors include the rapid breakdown of foetal haemoglobin (HbF), the "
                "immature conjugation capacity of the newborn liver, and increased enterohepatic circulation.</p>"
                "<p><strong>Physiological jaundice</strong> appears on day 2&ndash;3 of life, peaks around day 4&ndash;5, and "
                "resolves within 1&ndash;2 weeks. <strong>Pathological jaundice</strong> is jaundice that appears within the first "
                "24 hours, rises rapidly, or persists beyond two weeks.</p>"
                "<p>Very high bilirubin levels (&gt;20&ndash;25&nbsp;mg/dL) in newborns increase the risk of "
                "<strong>kernicterus</strong> (bilirubin encephalopathy)&mdash;permanent neurological damage caused by bilirubin "
                "deposition in brain tissue. Treatment options include <strong>phototherapy</strong> (blue light) and, in severe "
                "cases, <strong>exchange transfusion</strong>.</p>"
            ),
        ),
        Section(
            id="related-tests", level=2,
            heading="Related tests",
            body_html=(
                "<p>When investigating elevated bilirubin, the following tests are commonly ordered:</p>"
                "<ul>"
                "<li><strong>ALT and AST</strong> &ndash; hepatocellular damage markers</li>"
                "<li><strong>ALP</strong> &ndash; cholestatic damage marker</li>"
                "<li><strong>GGT</strong> &ndash; helps distinguish the source of ALP elevation</li>"
                "<li><strong>Albumin</strong> &ndash; reflects liver synthetic function</li>"
                "<li><strong>Complete blood count</strong> &ndash; to investigate haemolysis</li>"
                "<li><strong>Reticulocyte count</strong> &ndash; elevated in haemolytic anaemia</li>"
                "<li><strong>Haptoglobin and LDH</strong> &ndash; haemolysis markers</li>"
                "<li><strong>Direct and indirect Coombs test</strong> &ndash; to investigate autoimmune haemolysis</li>"
                "<li><strong>Abdominal ultrasound</strong> &ndash; to evaluate gallstones and bile duct dilatation</li>"
                "</ul>"
                "<p>The combination of these tests helps classify the cause of elevated bilirubin as pre-hepatic, "
                "hepatic, or post-hepatic.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>See your doctor if:</p>"
                "<ul>"
                "<li>Your bilirubin level is elevated</li>"
                "<li>You notice yellowing of your skin or eyes</li>"
                "<li>Your urine is dark (tea-coloured)</li>"
                "<li>Your stools are unusually pale or clay-coloured</li>"
                "<li>You have right upper abdominal pain, nausea, or itching</li>"
                "</ul>"
                "<p><strong>Emergency:</strong> Jaundice with fever, severe abdominal pain, altered mental status, or deep "
                "jaundice in a newborn requires emergency medical evaluation.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>Norya does not diagnose&mdash;we help you prepare for your doctor visit. Upload your blood test report at "
                "<a href=\"/analyze\">noryaai.com/analyze</a> and our AI engine automatically extracts total, direct, and indirect "
                "bilirubin along with ALT, AST, ALP, GGT, and other liver markers, compares them against reference ranges, "
                "and generates a clear, structured report.</p>"
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
        Section(id="intro", level=2, heading="Bilirrubina alta: ¿qué significa? Guía completa",
                body_html="<p>La <strong>bilirrubina</strong> es un pigmento amarillo-anaranjado producido por la degradación de la hemoglobina. Es un componente esencial de las pruebas de función hepática. La elevación se denomina <strong>hiperbilirrubinemia</strong> y puede causar coloración amarilla de la piel y los ojos (<strong>ictericia</strong>).</p><p>Las causas van desde enfermedad hepática y anemia hemolítica hasta obstrucción biliar y síndrome de Gilbert. La ictericia neonatal también es muy frecuente.</p><p>Esta guía es educativa y no sustituye el consejo médico.</p>"),
        Section(id="what-is-bilirubin", level=2, heading="¿Qué es la bilirrubina?",
                body_html="<p>La <strong>bilirrubina</strong> se forma al degradarse el grupo <em>hemo</em> de la hemoglobina. El 80% procede de los eritrocitos; el 20% restante de mioglobina y citocromos. Pasos: producción (bilirrubina indirecta), transporte (unida a albúmina), conjugación hepática (bilirrubina directa) y excreción biliar (urobilinógeno intestinal).</p>"),
        Section(id="direct-vs-indirect", level=2, heading="Bilirrubina directa vs. indirecta",
                body_html="<p><strong>Indirecta (no conjugada):</strong> no procesada por el hígado, insoluble en agua. Elevación sugiere hemólisis o defectos de conjugación (Gilbert). <strong>Directa (conjugada):</strong> procesada, soluble. Elevación sugiere daño hepático u obstrucción biliar. <strong>Total</strong> = directa + indirecta.</p>"),
        Section(id="normal-ranges", level=2, heading="Valores normales de bilirrubina",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Parámetro</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Rango normal</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Bilirrubina total</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0,1&ndash;1,2 mg/dL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Bilirrubina directa</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0&ndash;0,3 mg/dL</td></tr></tbody></table><p>La ictericia clínica aparece cuando la bilirrubina total supera 2,5&ndash;3 mg/dL.</p>"),
        Section(id="high-bilirubin-causes", level=2, heading="Causas de bilirrubina alta",
                body_html="<p><strong>Prehepáticas (indirecta ↑):</strong> anemia hemolítica, transfusiones, reabsorción de hematomas. <strong>Hepáticas (mixta):</strong> hepatitis viral, alcohólica, cirrosis, fármacos, Gilbert, Crigler-Najjar. <strong>Posthepáticas (directa ↑):</strong> cálculos biliares, estenosis o tumor de conducto biliar, tumor pancreático.</p>"),
        Section(id="jaundice-connection", level=2, heading="Ictericia y bilirrubina",
                body_html="<p>La <strong>ictericia</strong> se manifiesta como coloración amarilla de piel, mucosas y escleróticas. Primer signo: ictericia escleral. Hallazgos asociados: orina oscura, heces acólicas, prurito y dolor en hipocondrio derecho.</p>"),
        Section(id="gilbert-syndrome", level=2, heading="Síndrome de Gilbert",
                body_html="<p>Trastorno hereditario más frecuente del metabolismo de la bilirrubina (3&ndash;7% de la población). Hiperbilirrubinemia indirecta leve e intermitente (1&ndash;3 mg/dL). Exacerbaciones con ayuno, estrés, ejercicio. Pruebas hepáticas normales. Benigno, sin tratamiento necesario.</p>"),
        Section(id="newborn-bilirubin", level=2, heading="Ictericia neonatal",
                body_html="<p>Afecta al ~60% de los recién nacidos a término y al 80% de prematuros. Ictericia fisiológica: día 2&ndash;3, pico día 4&ndash;5, resolución en 1&ndash;2 semanas. Niveles muy altos (&gt;20 mg/dL) pueden causar <strong>kernícterus</strong>. Tratamiento: fototerapia o exanguinotransfusión.</p>"),
        Section(id="related-tests", level=2, heading="Pruebas relacionadas",
                body_html="<p>ALT, AST, ALP, GGT, albúmina, hemograma, reticulocitos, haptoglobina, LDH, Coombs directo/indirecto y ecografía abdominal.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Cuándo consultar al médico",
                body_html="<p>Consulte si la bilirrubina está elevada, si observa ictericia, orina oscura, heces pálidas o dolor abdominal. <strong>Urgencia:</strong> ictericia con fiebre, dolor intenso o alteración del estado mental.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo ayuda Norya",
                body_html="<p>Suba su análisis en <a href=\"/analyze\">noryaai.com/analyze</a>. Nuestra IA extraerá bilirrubina total, directa e indirecta junto con ALT, AST, ALP y GGT. <a href=\"/pricing\">Página de precios</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# GERMAN
# ---------------------------------------------------------------------------
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirubin erhöht: Was bedeutet ein hoher Bilirubinwert?",
                body_html="<p><strong>Bilirubin</strong> ist ein gelb-oranges Pigment aus dem Abbau von Hämoglobin. Es ist ein zentraler Bestandteil der Leberfunktionstests. Ein erhöhter Wert (<strong>Hyperbilirubinämie</strong>) kann zu Gelbfärbung von Haut und Augen (<strong>Ikterus</strong>) führen.</p><p>Ursachen reichen von Lebererkrankungen über hämolytische Anämie bis zu Gallenwegsobstruktion und Gilbert-Syndrom.</p><p>Dieser Leitfaden dient der Information und ersetzt keine ärztliche Beratung.</p>"),
        Section(id="what-is-bilirubin", level=2, heading="Was ist Bilirubin?",
                body_html="<p><strong>Bilirubin</strong> entsteht beim Abbau von Häm. 80% aus Erythrozyten-Hämoglobin, 20% aus Myoglobin/Cytochromen. Schritte: Produktion (indirektes Bilirubin), Transport (albumingebunden), Konjugation in der Leber (direktes Bilirubin), Ausscheidung über die Galle.</p>"),
        Section(id="direct-vs-indirect", level=2, heading="Direktes vs. indirektes Bilirubin",
                body_html="<p><strong>Indirekt (unkonjugiert):</strong> wasserunlöslich, nicht hepatisch verarbeitet. Erhöhung bei Hämolyse oder Konjugationsdefekten (Gilbert). <strong>Direkt (konjugiert):</strong> wasserlöslich. Erhöhung bei Leberschaden oder Cholestase. <strong>Gesamt</strong> = direkt + indirekt.</p>"),
        Section(id="normal-ranges", level=2, heading="Normale Bilirubinwerte",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Parameter</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Normalbereich</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Gesamtbilirubin</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0,1&ndash;1,2 mg/dL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Direktes Bilirubin</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0&ndash;0,3 mg/dL</td></tr></tbody></table><p>Ikterus wird ab ca. 2,5&ndash;3 mg/dL klinisch sichtbar.</p>"),
        Section(id="high-bilirubin-causes", level=2, heading="Ursachen für erhöhtes Bilirubin",
                body_html="<p><strong>Prähepatisch (indirekt ↑):</strong> hämolytische Anämien, Transfusionsreaktionen, Hämatom-Resorption. <strong>Hepatisch (gemischt):</strong> Virushepatitis, alkoholische Hepatitis, Zirrhose, Medikamente, Gilbert, Crigler-Najjar. <strong>Posthepatisch (direkt ↑):</strong> Gallensteine, Gallengangsstenose/-tumor, Pankreaskopftumor.</p>"),
        Section(id="jaundice-connection", level=2, heading="Ikterus und Bilirubin",
                body_html="<p><strong>Ikterus</strong> zeigt sich als Gelbfärbung von Haut, Schleimhäuten und Skleren. Begleitbefunde: dunkler Urin, acholischer Stuhl, Pruritus und rechter Oberbauchschmerz.</p>"),
        Section(id="gilbert-syndrome", level=2, heading="Gilbert-Syndrom",
                body_html="<p>Häufigste erbliche Störung des Bilirubinstoffwechsels (3&ndash;7% der Bevölkerung). Milde intermittierende indirekte Hyperbilirubinämie. Exazerbation bei Fasten, Stress, Sport. Leberwerte normal. Benigne, keine Therapie nötig.</p>"),
        Section(id="newborn-bilirubin", level=2, heading="Neugeborenenikterus",
                body_html="<p>Betrifft ~60% der reifen und 80% der frühgeborenen Säuglinge. Physiologischer Ikterus: Tag 2&ndash;3, Peak Tag 4&ndash;5, Rückbildung in 1&ndash;2 Wochen. Sehr hohe Werte (&gt;20 mg/dL) bergen Kernikterus-Risiko. Therapie: Phototherapie oder Austauschtransfusion.</p>"),
        Section(id="related-tests", level=2, heading="Verwandte Untersuchungen",
                body_html="<p>ALT, AST, ALP, GGT, Albumin, Blutbild, Retikulozyten, Haptoglobin, LDH, Coombs-Test und Abdomensonographie.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann zum Arzt?",
                body_html="<p>Suchen Sie einen Arzt auf bei erhöhtem Bilirubin, Ikterus, dunklem Urin, hellem Stuhl oder Oberbauchschmerz. <strong>Notfall:</strong> Ikterus mit Fieber, starken Bauchschmerzen oder Bewusstseinsveränderung.</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie Norya hilft",
                body_html="<p>Laden Sie Ihren Befund unter <a href=\"/analyze\">noryaai.com/analyze</a> hoch. Unsere KI extrahiert Gesamt-, direktes und indirektes Bilirubin sowie ALT, AST, ALP und GGT. <a href=\"/pricing\">Preisseite</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ---------------------------------------------------------------------------
# FRENCH
# ---------------------------------------------------------------------------
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirubine élevée : que signifie un taux élevé ?",
                body_html="<p>La <strong>bilirubine</strong> est un pigment jaune-orangé issu de la dégradation de l&rsquo;hémoglobine. C&rsquo;est un composant clé du bilan hépatique. L&rsquo;élévation (<strong>hyperbilirubinémie</strong>) peut se manifester par un ictère (jaunisse).</p><p>Les causes vont de la maladie hépatique à l&rsquo;anémie hémolytique, en passant par l&rsquo;obstruction biliaire et le syndrome de Gilbert.</p><p>Ce guide est informatif et ne remplace pas un avis médical.</p>"),
        Section(id="what-is-bilirubin", level=2, heading="Qu&rsquo;est-ce que la bilirubine ?",
                body_html="<p>La <strong>bilirubine</strong> provient de la dégradation de l&rsquo;hème. 80% des érythrocytes, 20% de la myoglobine/cytochromes. Étapes : production (bilirubine indirecte), transport (liée à l&rsquo;albumine), conjugaison hépatique (bilirubine directe), excrétion biliaire.</p>"),
        Section(id="direct-vs-indirect", level=2, heading="Bilirubine directe vs. indirecte",
                body_html="<p><strong>Indirecte (non conjuguée) :</strong> insoluble, non traitée par le foie. Élévation = hémolyse ou défaut de conjugaison. <strong>Directe (conjuguée) :</strong> soluble. Élévation = atteinte hépatique ou cholestase. <strong>Totale</strong> = directe + indirecte.</p>"),
        Section(id="normal-ranges", level=2, heading="Valeurs normales de la bilirubine",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Paramètre</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Valeur normale</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Bilirubine totale</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0,1&ndash;1,2 mg/dL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Bilirubine directe</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0&ndash;0,3 mg/dL</td></tr></tbody></table><p>L&rsquo;ictère clinique apparaît au-dessus de 2,5&ndash;3 mg/dL.</p>"),
        Section(id="high-bilirubin-causes", level=2, heading="Causes de bilirubine élevée",
                body_html="<p><strong>Préhépatiques (indirecte ↑) :</strong> anémies hémolytiques, transfusions, résorption d&rsquo;hématomes. <strong>Hépatiques (mixte) :</strong> hépatites virales, alcooliques, cirrhose, médicaments, Gilbert, Crigler-Najjar. <strong>Posthépatiques (directe ↑) :</strong> calculs biliaires, sténose ou tumeur du cholédoque, tumeur pancréatique.</p>"),
        Section(id="jaundice-connection", level=2, heading="Ictère et bilirubine",
                body_html="<p>L&rsquo;<strong>ictère</strong> se manifeste par une coloration jaune de la peau, des muqueuses et des sclères. Signes associés : urines foncées, selles décolorées, prurit et douleur de l&rsquo;hypocondre droit.</p>"),
        Section(id="gilbert-syndrome", level=2, heading="Syndrome de Gilbert",
                body_html="<p>Trouble héréditaire le plus fréquent du métabolisme de la bilirubine (3&ndash;7% de la population). Hyperbilirubinémie indirecte légère et intermittente. Exacerbations : jeûne, stress, exercice. Bilan hépatique normal. Bénin.</p>"),
        Section(id="newborn-bilirubin", level=2, heading="Ictère néonatal",
                body_html="<p>Touche ~60% des nouveau-nés à terme et 80% des prématurés. Ictère physiologique : J2&ndash;J3, pic J4&ndash;J5, résolution en 1&ndash;2 semaines. Taux très élevés (&gt;20 mg/dL) : risque d&rsquo;ictère nucléaire. Traitement : photothérapie ou exsanguino-transfusion.</p>"),
        Section(id="related-tests", level=2, heading="Examens associés",
                body_html="<p>ALT, AST, PAL, GGT, albumine, NFS, réticulocytes, haptoglobine, LDH, test de Coombs et échographie abdominale.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter ?",
                body_html="<p>Consultez si la bilirubine est élevée, en cas d&rsquo;ictère, urines foncées, selles décolorées ou douleur abdominale. <strong>Urgence :</strong> ictère avec fièvre, douleur intense ou confusion.</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment Norya peut vous aider",
                body_html="<p>Téléchargez votre bilan sur <a href=\"/analyze\">noryaai.com/analyze</a>. Notre IA extraira bilirubine totale, directe et indirecte, ALT, AST, PAL et GGT. <a href=\"/pricing\">Page tarifs</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ITALIAN
# ---------------------------------------------------------------------------
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Bilirubina alta: cosa significa? Guida completa",
                body_html="<p>La <strong>bilirubina</strong> è un pigmento giallo-arancio derivante dalla degradazione dell&rsquo;emoglobina. È un componente chiave degli esami epatici. L&rsquo;aumento (<strong>iperbilirubinemia</strong>) può causare ittero.</p><p>Le cause spaziano dalle epatopatie all&rsquo;anemia emolitica, dall&rsquo;ostruzione biliare alla sindrome di Gilbert.</p><p>Questa guida è informativa e non sostituisce il parere medico.</p>"),
        Section(id="what-is-bilirubin", level=2, heading="Cos&rsquo;è la bilirubina?",
                body_html="<p>La <strong>bilirubina</strong> deriva dalla degradazione dell&rsquo;eme. 80% dagli eritrociti, 20% da mioglobina/citocromi. Fasi: produzione (indiretta), trasporto (legata all&rsquo;albumina), coniugazione epatica (diretta), escrezione biliare.</p>"),
        Section(id="direct-vs-indirect", level=2, heading="Bilirubina diretta vs. indiretta",
                body_html="<p><strong>Indiretta (non coniugata):</strong> insolubile, non processata dal fegato. Aumento = emolisi o difetti di coniugazione. <strong>Diretta (coniugata):</strong> solubile. Aumento = danno epatico o colestasi. <strong>Totale</strong> = diretta + indiretta.</p>"),
        Section(id="normal-ranges", level=2, heading="Valori normali della bilirubina",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Parametro</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">Intervallo normale</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Bilirubina totale</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0,1&ndash;1,2 mg/dL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">Bilirubina diretta</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0&ndash;0,3 mg/dL</td></tr></tbody></table><p>L&rsquo;ittero clinico appare sopra 2,5&ndash;3 mg/dL.</p>"),
        Section(id="high-bilirubin-causes", level=2, heading="Cause di bilirubina alta",
                body_html="<p><strong>Preepatiche (indiretta ↑):</strong> anemie emolitiche, trasfusioni, riassorbimento ematomi. <strong>Epatiche (miste):</strong> epatiti virali, alcoliche, cirrosi, farmaci, Gilbert, Crigler-Najjar. <strong>Postepatiche (diretta ↑):</strong> calcoli, stenosi o neoplasia del coledoco, tumore pancreatico.</p>"),
        Section(id="jaundice-connection", level=2, heading="Ittero e bilirubina",
                body_html="<p>L&rsquo;<strong>ittero</strong> si manifesta come colorazione gialla di cute, mucose e sclere. Segni associati: urine scure, feci acoliche, prurito e dolore in ipocondrio destro.</p>"),
        Section(id="gilbert-syndrome", level=2, heading="Sindrome di Gilbert",
                body_html="<p>Disordine ereditario più comune del metabolismo della bilirubina (3&ndash;7% della popolazione). Iperbilirubinemia indiretta lieve e intermittente. Esacerbazioni: digiuno, stress, esercizio. Esami epatici normali. Benigna.</p>"),
        Section(id="newborn-bilirubin", level=2, heading="Ittero neonatale",
                body_html="<p>Colpisce ~60% dei neonati a termine e 80% dei pretermine. Ittero fisiologico: giorno 2&ndash;3, picco giorno 4&ndash;5, risoluzione in 1&ndash;2 settimane. Livelli molto alti (&gt;20 mg/dL): rischio di kernittero. Terapia: fototerapia o exsanguinotrasfusione.</p>"),
        Section(id="related-tests", level=2, heading="Esami correlati",
                body_html="<p>ALT, AST, ALP, GGT, albumina, emocromo, reticolociti, aptoglobina, LDH, test di Coombs ed ecografia addominale.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando consultare il medico",
                body_html="<p>Consultate il medico se la bilirubina è elevata, in caso di ittero, urine scure, feci chiare o dolore addominale. <strong>Emergenza:</strong> ittero con febbre, dolore intenso o alterazione dello stato mentale.</p>"),
        Section(id="how-norya-helps", level=2, heading="Come Norya può aiutarti",
                body_html="<p>Caricate il vostro esame su <a href=\"/analyze\">noryaai.com/analyze</a>. La nostra IA estrarrà bilirubina totale, diretta e indiretta, ALT, AST, ALP e GGT. <a href=\"/pricing\">Pagina prezzi</a>.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HEBREW
# ---------------------------------------------------------------------------
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="בילירובין גבוה: מה המשמעות? מדריך מקיף",
                body_html="<p><strong>בילירובין</strong> הוא פיגמנט צהוב-כתום הנוצר מפירוק המוגלובין. הוא מרכיב מרכזי בבדיקות תפקודי כבד. עלייה (<strong>היפרבילירובינמיה</strong>) עלולה לגרום לצהבת.</p><p>הגורמים נעים ממחלות כבד ואנמיה המוליטית ועד חסימת דרכי מרה ותסמונת גילברט. צהבת יילודים גם שכיחה מאוד.</p><p>מדריך זה חינוכי בלבד ואינו מחליף ייעוץ רפואי.</p>"),
        Section(id="what-is-bilirubin", level=2, heading="מהו בילירובין?",
                body_html="<p><strong>בילירובין</strong> נוצר מפירוק ההם. 80% מהמוגלובין של כדוריות אדומות, 20% ממיוגלובין/ציטוכרומים. שלבים: ייצור (בילירובין עקיף), הובלה (קשור לאלבומין), צימוד בכבד (בילירובין ישיר), הפרשה במרה.</p>"),
        Section(id="direct-vs-indirect", level=2, heading="בילירובין ישיר לעומת עקיף",
                body_html="<p><strong>עקיף (לא מצומד):</strong> לא מעובד בכבד, לא מסיס במים. עלייה = המוליזה או פגם בצימוד (גילברט). <strong>ישיר (מצומד):</strong> מסיס. עלייה = נזק כבדי או כולסטאזיס. <strong>סה\"כ</strong> = ישיר + עקיף.</p>"),
        Section(id="normal-ranges", level=2, heading="טווחי בילירובין תקינים",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">פרמטר</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">טווח תקין</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">בילירובין כולל</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0.1&ndash;1.2 mg/dL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">בילירובין ישיר</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0&ndash;0.3 mg/dL</td></tr></tbody></table><p>צהבת קלינית מופיעה מעל 2.5&ndash;3 mg/dL.</p>"),
        Section(id="high-bilirubin-causes", level=2, heading="גורמים לבילירובין גבוה",
                body_html="<p><strong>טרום-כבדי (עקיף ↑):</strong> אנמיות המוליטיות, עירויים, ספיגת המטומות. <strong>כבדי (מעורב):</strong> הפטיטיס, שחמת, תרופות, גילברט, קריגלר-נג'ר. <strong>אחרי-כבדי (ישיר ↑):</strong> אבני מרה, היצרות/גידול בדרכי המרה, גידול בלבלב.</p>"),
        Section(id="jaundice-connection", level=2, heading="צהבת ובילירובין",
                body_html="<p><strong>צהבת</strong> מתבטאת בצביעה צהובה של העור, הריריות והסקלרות. ממצאים נלווים: שתן כהה, צואה אכולית, גירוד וכאב בהיפוכונדריום ימני.</p>"),
        Section(id="gilbert-syndrome", level=2, heading="תסמונת גילברט",
                body_html="<p>ההפרעה התורשתית השכיחה ביותר במטבוליזם הבילירובין (3&ndash;7% מהאוכלוסייה). היפרבילירובינמיה עקיפה קלה ולסירוגין. החמרות: צום, סטרס, מאמץ. תפקודי כבד תקינים. שפירה.</p>"),
        Section(id="newborn-bilirubin", level=2, heading="צהבת יילודים",
                body_html="<p>פוגעת ב~60% מפגי טרם ו-80% מפגים. צהבת פיזיולוגית: יום 2&ndash;3, שיא יום 4&ndash;5, חלוף תוך 1&ndash;2 שבועות. רמות גבוהות מאוד (&gt;20 mg/dL): סיכון לקרניקטרוס. טיפול: פוטותרפיה או עירוי חילופי.</p>"),
        Section(id="related-tests", level=2, heading="בדיקות קשורות",
                body_html="<p>ALT, AST, ALP, GGT, אלבומין, ספירת דם, רטיקולוציטים, הפטוגלובין, LDH, קומבס וUS בטן.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא?",
                body_html="<p>פנו לרופא אם הבילירובין מוגבה, בצהבת, שתן כהה, צואה בהירה או כאב בטן. <strong>חירום:</strong> צהבת עם חום, כאב חמור או שינוי במצב ההכרה.</p>"),
        Section(id="how-norya-helps", level=2, heading="איך Norya עוזרת",
                body_html="<p>העלו את הבדיקה ב-<a href=\"/analyze\">noryaai.com/analyze</a>. ה-AI שלנו יחלץ בילירובין כולל, ישיר ועקיף יחד עם ALT, AST, ALP ו-GGT. <a href=\"/pricing\">עמוד תמחור</a>.</p>"),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ---------------------------------------------------------------------------
# HINDI
# ---------------------------------------------------------------------------
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="बिलीरुबिन उच्च: इसका क्या मतलब है? व्यापक गाइड",
                body_html="<p><strong>बिलीरुबिन</strong> हीमोग्लोबिन के टूटने से बनने वाला पीला-नारंगी रंगद्रव्य है। यह लिवर फ़ंक्शन टेस्ट का मुख्य घटक है। बढ़ा हुआ स्तर (<strong>हाइपरबिलीरुबिनेमिया</strong>) त्वचा और आँखों में पीलापन (<strong>पीलिया</strong>) पैदा कर सकता है।</p><p>कारणों में लिवर रोग, हीमोलिटिक एनीमिया, पित्त नली अवरोध और गिल्बर्ट सिंड्रोम शामिल हैं। नवजात पीलिया भी बहुत आम है।</p><p>यह गाइड शैक्षणिक है और चिकित्सा सलाह का विकल्प नहीं है।</p>"),
        Section(id="what-is-bilirubin", level=2, heading="बिलीरुबिन क्या है?",
                body_html="<p><strong>बिलीरुबिन</strong> हीम के टूटने से बनता है। 80% एरिथ्रोसाइट हीमोग्लोबिन से, 20% मायोग्लोबिन/साइटोक्रोम से। चरण: उत्पादन (अप्रत्यक्ष बिलीरुबिन), परिवहन (एल्ब्यूमिन-बद्ध), यकृत में संयुग्मन (प्रत्यक्ष बिलीरुबिन), पित्त में उत्सर्जन।</p>"),
        Section(id="direct-vs-indirect", level=2, heading="प्रत्यक्ष बनाम अप्रत्यक्ष बिलीरुबिन",
                body_html="<p><strong>अप्रत्यक्ष (असंयुग्मित):</strong> जल-अघुलनशील, लिवर में अप्रसंस्कृत। बढ़ना = हीमोलिसिस या संयुग्मन दोष। <strong>प्रत्यक्ष (संयुग्मित):</strong> जल-घुलनशील। बढ़ना = लिवर क्षति या कोलेस्टेसिस। <strong>कुल</strong> = प्रत्यक्ष + अप्रत्यक्ष।</p>"),
        Section(id="normal-ranges", level=2, heading="सामान्य बिलीरुबिन मान",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">पैरामीटर</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:left;\">सामान्य सीमा</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">कुल बिलीरुबिन</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0.1&ndash;1.2 mg/dL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">प्रत्यक्ष बिलीरुबिन</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0&ndash;0.3 mg/dL</td></tr></tbody></table><p>कुल बिलीरुबिन 2.5&ndash;3 mg/dL से ऊपर होने पर नैदानिक पीलिया दिखता है।</p>"),
        Section(id="high-bilirubin-causes", level=2, heading="बिलीरुबिन बढ़ने के कारण",
                body_html="<p><strong>प्री-हेपैटिक (अप्रत्यक्ष ↑):</strong> हीमोलिटिक एनीमिया, रक्ताधान, हेमेटोमा अवशोषण। <strong>हेपैटिक (मिश्रित):</strong> वायरल हेपेटाइटिस, अल्कोहलिक, सिरोसिस, दवाएँ, गिल्बर्ट, क्रिगलर-नज्जर। <strong>पोस्ट-हेपैटिक (प्रत्यक्ष ↑):</strong> पित्त की पथरी, पित्त नली संकुचन/ट्यूमर, अग्नाशय ट्यूमर।</p>"),
        Section(id="jaundice-connection", level=2, heading="पीलिया और बिलीरुबिन",
                body_html="<p><strong>पीलिया</strong> त्वचा, श्लेष्मा झिल्ली और स्क्लेरा में पीलापन के रूप में प्रकट होता है। संबद्ध लक्षण: गहरे रंग का मूत्र, हल्के रंग का मल, खुजली और दाएँ ऊपरी पेट में दर्द।</p>"),
        Section(id="gilbert-syndrome", level=2, heading="गिल्बर्ट सिंड्रोम",
                body_html="<p>बिलीरुबिन चयापचय का सबसे आम वंशानुगत विकार (जनसंख्या का 3&ndash;7%)। हल्की, रुक-रुक कर अप्रत्यक्ष हाइपरबिलीरुबिनेमिया। उपवास, तनाव, व्यायाम से बढ़ता है। लिवर टेस्ट सामान्य। सौम्य, उपचार अनावश्यक।</p>"),
        Section(id="newborn-bilirubin", level=2, heading="नवजात पीलिया",
                body_html="<p>~60% पूर्ण अवधि और 80% अपरिपक्व शिशुओं को प्रभावित करता है। शारीरिक पीलिया: दिन 2&ndash;3, शिखर दिन 4&ndash;5, 1&ndash;2 सप्ताह में ठीक। बहुत अधिक स्तर (&gt;20 mg/dL): कर्निक्टेरस का जोखिम। उपचार: फ़ोटोथेरेपी या एक्सचेंज ट्रांसफ़्यूज़न।</p>"),
        Section(id="related-tests", level=2, heading="संबंधित परीक्षण",
                body_html="<p>ALT, AST, ALP, GGT, एल्ब्यूमिन, CBC, रेटिकुलोसाइट, हैप्टोग्लोबिन, LDH, कूम्ब्स टेस्ट और पेट का अल्ट्रासाउंड।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर से कब मिलें?",
                body_html="<p>बिलीरुबिन बढ़ा होने, पीलिया, गहरे मूत्र, हल्के मल या पेट दर्द होने पर डॉक्टर से मिलें। <strong>आपातकाल:</strong> बुखार के साथ पीलिया, तीव्र दर्द या मानसिक स्थिति बदलाव।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya कैसे मदद करता है",
                body_html="<p>अपनी रिपोर्ट <a href=\"/analyze\">noryaai.com/analyze</a> पर अपलोड करें। हमारा AI कुल, प्रत्यक्ष और अप्रत्यक्ष बिलीरुबिन के साथ ALT, AST, ALP और GGT निकालेगा। <a href=\"/pricing\">मूल्य निर्धारण</a>।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ---------------------------------------------------------------------------
# ARABIC
# ---------------------------------------------------------------------------
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="البيليروبين المرتفع: ماذا يعني؟ دليل شامل",
                body_html="<p><strong>البيليروبين</strong> صبغة صفراء-برتقالية تنتج عن تحلل الهيموغلوبين. يُعدّ مكوناً أساسياً في فحوصات وظائف الكبد. الارتفاع (<strong>فرط بيليروبين الدم</strong>) قد يسبب اصفرار الجلد والعينين (<strong>اليرقان</strong>).</p><p>الأسباب تتراوح بين أمراض الكبد وفقر الدم الانحلالي وانسداد القنوات الصفراوية ومتلازمة جيلبرت. يرقان حديثي الولادة شائع جداً أيضاً.</p><p>هذا الدليل تثقيفي ولا يحل محل الاستشارة الطبية.</p>"),
        Section(id="what-is-bilirubin", level=2, heading="ما هو البيليروبين؟",
                body_html="<p><strong>البيليروبين</strong> ينتج من تحلل الهيم. 80% من هيموغلوبين الكريات الحمراء، 20% من الميوغلوبين/السيتوكرومات. المراحل: إنتاج (غير مباشر)، نقل (مرتبط بالألبومين)، اقتران في الكبد (مباشر)، إفراز في المرارة.</p>"),
        Section(id="direct-vs-indirect", level=2, heading="البيليروبين المباشر مقابل غير المباشر",
                body_html="<p><strong>غير مباشر (غير مقترن):</strong> غير ذواب في الماء، لم يُعالج في الكبد. ارتفاعه = انحلال دم أو خلل في الاقتران. <strong>مباشر (مقترن):</strong> ذواب. ارتفاعه = تلف كبدي أو ركود صفراوي. <strong>الكلي</strong> = مباشر + غير مباشر.</p>"),
        Section(id="normal-ranges", level=2, heading="المعدلات الطبيعية للبيليروبين",
                body_html="<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\"><thead><tr><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">المعيار</th><th style=\"border:1px solid #cbd5e1;padding:8px 12px;text-align:right;\">الطبيعي</th></tr></thead><tbody><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">بيليروبين كلي</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0.1&ndash;1.2 mg/dL</td></tr><tr><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">بيليروبين مباشر</td><td style=\"border:1px solid #cbd5e1;padding:8px 12px;\">0&ndash;0.3 mg/dL</td></tr></tbody></table><p>اليرقان السريري يظهر عند تجاوز 2.5&ndash;3 mg/dL.</p>"),
        Section(id="high-bilirubin-causes", level=2, heading="أسباب ارتفاع البيليروبين",
                body_html="<p><strong>ما قبل الكبد (غير مباشر ↑):</strong> فقر دم انحلالي، نقل دم، امتصاص ورم دموي. <strong>كبدي (مختلط):</strong> التهاب كبد فيروسي، كحولي، تشمع، أدوية، جيلبرت، كريغلر-نجار. <strong>ما بعد الكبد (مباشر ↑):</strong> حصوات مرارية، تضيّق/ورم في القناة الصفراوية، ورم رأس البنكرياس.</p>"),
        Section(id="jaundice-connection", level=2, heading="اليرقان والبيليروبين",
                body_html="<p><strong>اليرقان</strong> يظهر كاصفرار الجلد والأغشية المخاطية والصلبة. علامات مصاحبة: بول داكن، براز شاحب، حكة وألم في الربع العلوي الأيمن.</p>"),
        Section(id="gilbert-syndrome", level=2, heading="متلازمة جيلبرت",
                body_html="<p>أكثر اضطرابات استقلاب البيليروبين الوراثية شيوعاً (3&ndash;7% من السكان). فرط بيليروبين غير مباشر خفيف ومتقطع. يزداد مع الصيام والإجهاد. وظائف الكبد طبيعية. حميدة.</p>"),
        Section(id="newborn-bilirubin", level=2, heading="يرقان حديثي الولادة",
                body_html="<p>يصيب ~60% من المواليد الأتمة و80% من الخدّج. اليرقان الفسيولوجي: يوم 2&ndash;3، ذروة يوم 4&ndash;5، يتلاشى خلال 1&ndash;2 أسبوع. مستويات عالية جداً (&gt;20 mg/dL): خطر اليرقان النووي. العلاج: معالجة ضوئية أو تبديل الدم.</p>"),
        Section(id="related-tests", level=2, heading="فحوصات ذات صلة",
                body_html="<p>ALT، AST، ALP، GGT، ألبومين، تعداد دم، خلايا شبكية، هابتوغلوبين، LDH، اختبار كومبس وتصوير بطن بالموجات فوق الصوتية.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى تراجع الطبيب؟",
                body_html="<p>راجع الطبيب عند ارتفاع البيليروبين، يرقان، بول داكن، براز فاتح أو ألم بطني. <strong>طوارئ:</strong> يرقان مع حمى، ألم شديد أو تغيّر بالوعي.</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف تساعدك Norya",
                body_html="<p>ارفع تقريرك على <a href=\"/analyze\">noryaai.com/analyze</a> وسيستخرج الذكاء الاصطناعي البيليروبين الكلي والمباشر وغير المباشر مع ALT وAST وALP وGGT. <a href=\"/pricing\">صفحة الأسعار</a>.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
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
            {"question": "What is a normal bilirubin level?",
             "answer": "Normal total bilirubin is 0.1–1.2 mg/dL. Direct (conjugated) bilirubin is 0–0.3 mg/dL. Clinical jaundice typically becomes visible when total bilirubin exceeds 2.5–3 mg/dL."},
            {"question": "What causes high bilirubin?",
             "answer": "Causes include haemolytic anaemia (pre-hepatic), liver diseases like hepatitis and cirrhosis (hepatic), and bile duct obstruction such as gallstones (post-hepatic). Gilbert syndrome is a common benign cause of mildly elevated indirect bilirubin."},
            {"question": "What is the difference between direct and indirect bilirubin?",
             "answer": "Indirect (unconjugated) bilirubin has not been processed by the liver and is water-insoluble. Direct (conjugated) bilirubin has been processed and is water-soluble. The ratio helps identify whether the cause is haemolytic, hepatic, or obstructive."},
            {"question": "What is Gilbert syndrome?",
             "answer": "Gilbert syndrome is a common, benign inherited condition affecting 3–7% of the population. It causes mild, intermittent elevations in unconjugated bilirubin, typically triggered by fasting, stress, or illness. No treatment is needed."},
            {"question": "When is newborn jaundice dangerous?",
             "answer": "Neonatal jaundice is dangerous when bilirubin exceeds 20–25 mg/dL, as it can cause kernicterus (bilirubin encephalopathy)—permanent brain damage. Phototherapy or exchange transfusion may be required."},
        ],
        "tr": [
            {"question": "Normal bilirubin değeri nedir?",
             "answer": "Toplam bilirubin 0,1–1,2 mg/dL, direkt bilirubin 0–0,3 mg/dL normaldir. 2,5–3 mg/dL üzerinde klinik sarılık görülür."},
            {"question": "Bilirubin yüksekliğinin nedenleri nelerdir?",
             "answer": "Hemolitik anemi (pre-hepatik), hepatit ve siroz (hepatik), safra taşları (post-hepatik). Gilbert sendromu yaygın, iyi huylu bir nedendir."},
            {"question": "Direkt ve indirekt bilirubin farkı nedir?",
             "answer": "İndirekt bilirubin karaciğerde henüz işlenmemiş, suda çözünmez formudur. Direkt bilirubin karaciğerde konjuge edilmiş, suda çözünür formudur. Hangi fraksiyonun yüksek olduğu nedenin belirlenmesinde kritiktir."},
            {"question": "Gilbert sendromu nedir?",
             "answer": "Popülasyonun %3–7'sini etkileyen yaygın, iyi huylu kalıtsal bir durumdur. Hafif, tekrarlayan indirekt bilirubin yüksekliğine neden olur. Tedavi gerektirmez."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de bilirrubina?",
             "answer": "Bilirrubina total: 0,1–1,2 mg/dL. Directa: 0–0,3 mg/dL. La ictericia clínica aparece sobre 2,5–3 mg/dL."},
            {"question": "¿Qué causa la bilirrubina alta?",
             "answer": "Anemia hemolítica, enfermedades hepáticas, obstrucción biliar y síndrome de Gilbert."},
            {"question": "¿Qué es el síndrome de Gilbert?",
             "answer": "Trastorno hereditario benigno (3–7% de la población) con hiperbilirrubinemia indirecta leve e intermitente. Sin tratamiento necesario."},
        ],
        "de": [
            {"question": "Was ist ein normaler Bilirubinwert?",
             "answer": "Gesamtbilirubin: 0,1–1,2 mg/dL. Direktes Bilirubin: 0–0,3 mg/dL. Ikterus ab ca. 2,5–3 mg/dL."},
            {"question": "Was verursacht erhöhtes Bilirubin?",
             "answer": "Hämolytische Anämie, Lebererkrankungen, Gallenwegsobstruktion und Gilbert-Syndrom."},
            {"question": "Was ist das Gilbert-Syndrom?",
             "answer": "Häufigste erbliche Störung des Bilirubinstoffwechsels (3–7%). Milde intermittierende indirekte Hyperbilirubinämie. Benigne."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de bilirubine ?",
             "answer": "Bilirubine totale : 0,1–1,2 mg/dL. Directe : 0–0,3 mg/dL. Ictère clinique au-dessus de 2,5–3 mg/dL."},
            {"question": "Quelles sont les causes d'une bilirubine élevée ?",
             "answer": "Anémie hémolytique, maladies hépatiques, obstruction biliaire et syndrome de Gilbert."},
            {"question": "Qu'est-ce que le syndrome de Gilbert ?",
             "answer": "Trouble héréditaire bénin le plus fréquent (3–7%). Hyperbilirubinémie indirecte légère et intermittente. Sans traitement nécessaire."},
        ],
        "it": [
            {"question": "Qual è il valore normale della bilirubina?",
             "answer": "Bilirubina totale: 0,1–1,2 mg/dL. Diretta: 0–0,3 mg/dL. Ittero clinico sopra 2,5–3 mg/dL."},
            {"question": "Cosa causa la bilirubina alta?",
             "answer": "Anemia emolitica, epatopatie, ostruzione biliare e sindrome di Gilbert."},
            {"question": "Cos'è la sindrome di Gilbert?",
             "answer": "Disordine ereditario benigno più comune (3–7%). Iperbilirubinemia indiretta lieve e intermittente. Non richiede trattamento."},
        ],
        "he": [
            {"question": "מהו ערך בילירובין תקין?",
             "answer": "בילירובין כולל: 0.1–1.2 mg/dL. ישיר: 0–0.3 mg/dL. צהבת קלינית מעל 2.5–3 mg/dL."},
            {"question": "מה גורם לבילירובין גבוה?",
             "answer": "אנמיה המוליטית, מחלות כבד, חסימת דרכי מרה ותסמונת גילברט."},
            {"question": "מהי תסמונת גילברט?",
             "answer": "ההפרעה התורשתית השכיחה ביותר (3–7%). היפרבילירובינמיה עקיפה קלה ולסירוגין. שפירה, ללא צורך בטיפול."},
        ],
        "hi": [
            {"question": "सामान्य बिलीरुबिन कितना होना चाहिए?",
             "answer": "कुल बिलीरुबिन: 0.1–1.2 mg/dL। प्रत्यक्ष: 0–0.3 mg/dL। 2.5–3 mg/dL से ऊपर पीलिया दिखता है।"},
            {"question": "बिलीरुबिन बढ़ने के कारण क्या हैं?",
             "answer": "हीमोलिटिक एनीमिया, लिवर रोग, पित्त नली अवरोध और गिल्बर्ट सिंड्रोम।"},
            {"question": "गिल्बर्ट सिंड्रोम क्या है?",
             "answer": "सबसे आम वंशानुगत सौम्य विकार (3–7% जनसंख्या)। हल्की, रुक-रुक कर अप्रत्यक्ष हाइपरबिलीरुबिनेमिया। उपचार अनावश्यक।"},
        ],
        "ar": [
            {"question": "ما هو مستوى البيليروبين الطبيعي؟",
             "answer": "البيليروبين الكلي: 0.1–1.2 mg/dL. المباشر: 0–0.3 mg/dL. اليرقان السريري فوق 2.5–3 mg/dL."},
            {"question": "ما أسباب ارتفاع البيليروبين؟",
             "answer": "فقر دم انحلالي، أمراض كبدية، انسداد صفراوي ومتلازمة جيلبرت."},
            {"question": "ما هي متلازمة جيلبرت؟",
             "answer": "أكثر اضطرابات استقلاب البيليروبين الوراثية شيوعاً (3–7%). فرط بيليروبين غير مباشر خفيف ومتقطع. حميدة ولا تحتاج علاجاً."},
        ],
    }
