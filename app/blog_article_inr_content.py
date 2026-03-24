# -*- coding: utf-8 -*-
"""
INR & Prothrombin Time (PT) blog article — full body content for all 9 languages.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_TBL = '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
_TH = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
_TD = 'style="border:1px solid #cbd5e1;padding:8px 12px;"'


# ─────────────────────────────────────────────────────────────────────
# TURKISH
# ─────────────────────────────────────────────────────────────────────
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR ve Protrombin Zamanı (PT): Sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p><strong>INR (International Normalized Ratio — Uluslararası Normalleştirilmiş Oran)</strong> ve "
                "<strong>Protrombin Zamanı (PT)</strong>, kanınızın ne kadar sürede pıhtılaştığını ölçen "
                "laboratuvar testleridir. Bu testler, pıhtılaşma kaskadının <em>ekstrinsik</em> ve <em>ortak</em> "
                "yollarını değerlendirerek kanama veya tromboz riskini belirlemeye yardımcı olur. Özellikle "
                "varfarin gibi antikoagülan (kan sulandırıcı) ilaç kullanan hastalar için düzenli INR takibi "
                "hayati öneme sahiptir.</p>"
                "<p>INR ve PT testleri yalnızca antikoagülan kullanan hastalarda değil, aynı zamanda karaciğer "
                "fonksiyonlarının değerlendirilmesinde, kanama bozukluklarının tanısında ve cerrahi öncesi "
                "hazırlıkta da sıklıkla istenir. Sonuçlar, pıhtılaşma faktörlerinin yeterli düzeyde çalışıp "
                "çalışmadığını anlamak için kritik bilgiler sunar.</p>"
                "<p>Bu rehber, INR ve PT testlerinin ne anlama geldiğini, normal ve terapötik aralıkları, "
                "yüksek ve düşük değerlerin olası nedenlerini sade bir dille açıklamayı amaçlamaktadır. "
                "Amacımız teşhis koymak değil — sonuçlarınızı daha iyi anlayarak hekiminizle verimli bir "
                "görüşme yapmanıza yardımcı olmaktır.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="PT ve INR nedir?",
            body_html=(
                "<p><strong>Protrombin Zamanı (PT)</strong>, plazmanın pıhtılaşması için geçen süreyi saniye "
                "cinsinden ölçer. Teste, kan örneğine doku faktörü (tromboplastin) ve kalsiyum eklenmesiyle "
                "başlanır. PT, özellikle pıhtılaşma faktörleri I (fibrinojen), II (protrombin), V, VII ve X'u "
                "değerlendirir. Farklı laboratuvarlar farklı tromboplastin reaktifleri kullandığından, "
                "ham PT değerleri laboratuvarlar arasında değişebilir.</p>"
                "<p><strong>INR</strong>, PT sonuçlarını dünya genelinde standartlaştırmak amacıyla "
                "geliştirilmiştir. INR hesaplamasında, kullanılan tromboplastin reaktifinin hassasiyetini "
                "gösteren <em>ISI (International Sensitivity Index)</em> değeri dikkate alınır. Formül: "
                "<em>INR = (Hasta PT / Ortalama Normal PT)<sup>ISI</sup></em>. Bu sayede farklı "
                "laboratuvarlardaki INR sonuçları birbiriyle karşılaştırılabilir hale gelir.</p>"
                "<p>Yüksek INR değeri kanın daha yavaş pıhtılaştığını (kanama riski), düşük INR değeri ise "
                "kanın daha hızlı pıhtılaştığını (tromboz riski) gösterir. INR, özellikle varfarin "
                "tedavisindeki hastaların doz ayarlaması için altın standart olarak kabul edilmektedir.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Pıhtılaşma (koagülasyon) nasıl çalışır?",
            body_html=(
                "<p>Kan pıhtılaşması, bir damar yaralandığında kanamayı durdurmak için devreye giren karmaşık "
                "bir biyolojik süreçtir. Bu süreç, birbirine bağlı üç yol üzerinden işler: <strong>ekstrinsik "
                "yol</strong> (doku hasarı ile başlar, Faktör VII aracılığıyla), <strong>intrinsik yol</strong> "
                "(kan-yüzey teması ile başlar, Faktör XII, XI, IX, VIII) ve <strong>ortak yol</strong> "
                "(Faktör X, V, protrombin ve fibrinojen).</p>"
                "<p>PT/INR testi, ekstrinsik ve ortak yolları değerlendirir. Doku faktörü (tromboplastin) "
                "kan örneğine eklendiğinde, Faktör VII aktive olur ve pıhtılaşma kaskadı başlar. Sonuçta "
                "protrombin, <em>trombin</em>'e dönüşür ve trombin de fibrinojeni <em>fibrin</em> ağına "
                "çevirir — bu ağ, pıhtının iskeletini oluşturur. Bu süreçteki herhangi bir faktörün "
                "eksikliği veya inhibisyonu, PT'nin uzamasına ve INR'nin yükselmesine yol açar.</p>"
                "<p>K vitamini, Faktör II, VII, IX ve X ile Protein C ve Protein S'nin karaciğerde "
                "sentezlenmesi için gereklidir. Varfarin gibi vitamin K antagonistleri, bu faktörlerin "
                "üretimini azaltarak pıhtılaşmayı yavaşlatır ve INR'yi yükseltir. Bu mekanizma, "
                "antikoagülan tedavinin temelini oluşturur.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="INR ve PT normal değerleri",
            body_html=(
                "<p>Aşağıdaki tablo, INR ve PT için genel kabul gören referans aralıklarını özetlemektedir. "
                "Laboratuvarlar arasında küçük farklılıklar olabilir; sonuçlarınızı her zaman kendi "
                "laboratuvarınızın referans aralıklarıyla birlikte değerlendirin.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Durum</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>PT (saniye)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Antikoagülan kullanmayan</td>'
                f'<td {_TD}>0,8 – 1,1</td>'
                f'<td {_TD}>11 – 13,5</td></tr>'
                f'<tr><td {_TD}>Varfarin tedavisi (çoğu endikasyon)</td>'
                f'<td {_TD}>2,0 – 3,0</td>'
                f'<td {_TD}>Değişken</td></tr>'
                f'<tr><td {_TD}>Mekanik kalp kapağı</td>'
                f'<td {_TD}>2,5 – 3,5</td>'
                f'<td {_TD}>Değişken</td></tr>'
                f'<tr><td {_TD}>Yüksek riskli durumlar (tekrarlayan tromboemboli)</td>'
                f'<td {_TD}>3,0 – 4,0</td>'
                f'<td {_TD}>Değişken</td></tr>'
                f'</tbody></table>'
                "<p>Antikoagülan kullanmayan bir kişide normal INR değeri <strong>0,8–1,1</strong> aralığındadır. "
                "1,1'in üzerindeki değerler karaciğer hastalığı, K vitamini eksikliği veya pıhtılaşma faktörü "
                "eksikliği gibi durumları düşündürür. Varfarin tedavisi altındaki hastalarda hedef INR genellikle "
                "<strong>2,0–3,0</strong>'tür; mekanik mitral kapak veya tekrarlayan tromboembolizm gibi "
                "durumlarda hedef <strong>2,5–3,5</strong>'e çıkabilir.</p>"
                "<p>PT değeri laboratuvarlar arasında farklılık gösterebilir; bu nedenle klinisyenler "
                "genellikle standartlaştırılmış INR değerini tercih eder. PT'nin uzamış olması (normal "
                "aralığın üzerinde), pıhtılaşma sürecinde bir sorun olduğuna işaret eder.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Yüksek INR (uzamış PT) nedenleri",
            body_html=(
                "<p><strong>Yüksek INR</strong>, kanın normalden daha yavaş pıhtılaştığı ve kanama riskinin "
                "arttığı anlamına gelir. En yaygın nedenler şunlardır:</p>"
                "<p><strong>Varfarin / antikoagülan tedavi:</strong> Varfarin, beklenen terapötik etkisi "
                "olarak INR'yi yükseltir. Ancak dozun fazla olması, ilaç etkileşimleri (özellikle NSAİİ'ler, "
                "antibiyotikler, antifungaller) veya diyetteki K vitamini alımındaki ani azalma INR'nin "
                "terapötik aralığın üzerine çıkmasına yol açabilir. INR &gt; 4,0 ciddi kanama riski taşır; "
                "INR &gt; 9,0 ise acil tıbbi müdahale gerektirir.</p>"
                "<p><strong>Karaciğer hastalıkları:</strong> Karaciğer, pıhtılaşma faktörlerinin büyük "
                "çoğunluğunu sentezler. Siroz, hepatit, karaciğer yetmezliği veya akut karaciğer hasarı "
                "durumlarında faktör üretimi azalır ve INR yükselir. Bu hastalarda INR, karaciğer "
                "fonksiyonunun ciddiyetini değerlendirmek için de kullanılır (örn. MELD skoru).</p>"
                "<p><strong>K vitamini eksikliği:</strong> K vitamini, Faktör II, VII, IX ve X'un "
                "karaciğerde sentezlenmesi için gereklidir. Yetersiz diyet alımı, malabsorbsiyon sendromları "
                "(çölyak, Crohn), uzun süreli antibiyotik kullanımı (bağırsak florasının bozulması) veya "
                "safra yolu tıkanıklıkları K vitamini eksikliğine yol açabilir. <strong>DIC (Yaygın Damar "
                "İçi Pıhtılaşma):</strong> Pıhtılaşma faktörlerinin ve trombositlerin aşırı tüketildiği "
                "bu ağır klinik tabloda hem INR yükselir hem de kanama eğilimi artar.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Düşük INR nedenleri",
            body_html=(
                "<p><strong>Düşük INR</strong>, kanın normalden daha hızlı pıhtılaştığı ve tromboz (pıhtı "
                "oluşumu) riskinin artabileceği anlamına gelir. Antikoagülan kullanmayan bireylerde düşük "
                "INR (0,8 altı) nadirdir ve genellikle klinik olarak anlamlı değildir. Ancak varfarin "
                "tedavisi altındaki hastalarda hedef INR aralığının altında kalmak ciddi riskler taşır.</p>"
                "<p><strong>Yetersiz antikoagülan dozu:</strong> Varfarin dozunun yetersiz olması, INR'nin "
                "terapötik aralığın altında kalmasına neden olur. Bu durumda derin ven trombozu (DVT), "
                "pulmoner emboli veya iskemik inme riski artar. Doz ayarlaması mutlaka hekim gözetiminde "
                "yapılmalıdır.</p>"
                "<p><strong>Aşırı K vitamini alımı:</strong> K vitamini bakımından zengin gıdalar (koyu "
                "yeşil yapraklı sebzeler, brokoli, karnabahar) veya K vitamini takviyeleri varfarin "
                "etkisini antagonize ederek INR'yi düşürür. Bu nedenle varfarin kullanan hastalara diyette "
                "tutarlı K vitamini alımı önerilir — ani artış veya azalışlardan kaçınılmalıdır.</p>"
                "<p><strong>İlaç etkileşimleri:</strong> Bazı ilaçlar (rifampisin, karbamazepin, "
                "barbitüratlar, St. John's Wort) karaciğerde CYP2C9 ve CYP3A4 enzimlerini indükleyerek "
                "varfarin metabolizmasını hızlandırır ve INR'yi düşürür. Taze donmuş plazma (TDP) "
                "transfüzyonu da pıhtılaşma faktörlerini doğrudan yerine koyarak INR'yi hızla düşürebilir.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR ve varfarin tedavisi",
            body_html=(
                "<p>Varfarin (Coumadin), en yaygın kullanılan oral antikoagülan ilaçtır ve K vitamini "
                "antagonisti olarak çalışır. Atriyal fibrilasyon, derin ven trombozu, pulmoner emboli, "
                "mekanik kalp kapağı ve tekrarlayan tromboembolik olaylarda reçete edilir. Varfarin "
                "tedavisinin etkinliği ve güvenliği, düzenli INR monitörizasyonu ile sağlanır.</p>"
                "<p>Tedavi başlangıcında INR genellikle her <strong>2–3 günde</strong> bir kontrol edilir; "
                "değerler stabil hale geldiğinde kontrol sıklığı <strong>2–4 haftaya</strong> uzatılabilir. "
                "Hedef INR aralığı, endikasyona göre belirlenir: çoğu durumda 2,0–3,0, mekanik kapak "
                "hastalarında 2,5–3,5. INR hedef aralığın üzerine çıkarsa kanama riski artar; altına "
                "düşerse tromboz riski artar.</p>"
                "<p>Varfarin tedavisi sırasında diyetteki K vitamini alımı, ilaç etkileşimleri, alkol "
                "tüketimi ve akut hastalıklar INR değerini önemli ölçüde etkileyebilir. Hasta eğitimi, "
                "düzenli takip ve iyi iletişim başarılı antikoagülan yönetiminin temel unsurlarıdır. "
                "Doğrudan etkili oral antikoagülanlar (DOAK — rivaroksaban, apiksaban, dabigatran) rutin "
                "INR takibi gerektirmez ancak belirli endikasyonlarda hâlâ varfarin tercih edilmektedir.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR ve karaciğer fonksiyonları",
            body_html=(
                "<p>Karaciğer, pıhtılaşma kaskadında görev alan hemen tüm faktörlerin (Faktör I, II, V, "
                "VII, IX, X, XI, XII, XIII ve Protein C, S) sentezlendiği merkezi organdır. Bu nedenle "
                "karaciğer hastalıkları pıhtılaşma fonksiyonunu doğrudan etkiler ve INR/PT değerlerinde "
                "belirgin uzamaya yol açar.</p>"
                "<p><strong>Siroz</strong> hastalarında INR yüksekliği hastalığın ciddiyetiyle doğru "
                "orantılıdır. Child-Pugh ve MELD skorlama sistemlerinde INR, karaciğer fonksiyonunun "
                "değerlendirilmesinde ve transplantasyon önceliğinin belirlenmesinde kilit parametrelerden "
                "biridir. Akut karaciğer yetmezliğinde INR hızla yükselir ve prognostik değer taşır.</p>"
                "<p>Karaciğer hastalıklarında INR yüksekliği, varfarin kaynaklı yükseklikten farklı bir "
                "mekanizmaya sahiptir: burada sorun K vitamininin yetersizliği değil, karaciğerin "
                "pıhtılaşma faktörlerini sentezleyememesidir. Bu nedenle K vitamini verilmesi genellikle "
                "etkisizdir. Tedavide altta yatan karaciğer hastalığının yönetimi, gerektiğinde TDP veya "
                "pıhtılaşma faktörü konsantreleri kullanılması söz konusu olabilir. Karaciğer "
                "fonksiyonlarını değerlendiren diğer testler (ALT, AST, bilirubin, albümin) ile birlikte "
                "yorumlamak önemlidir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda mutlaka bir sağlık profesyoneline danışın:</p>"
                "<p><strong>Kanama belirtileri (yüksek INR):</strong> Açıklanamayan morluklar, uzun süren "
                "kanamalar, diş eti kanaması, burun kanaması, idrar veya dışkıda kan, aşırı adet kanaması, "
                "öksürükle kan gelmesi. <strong>Acil durum belirtileri:</strong> şiddetli baş ağrısı ile "
                "bilinç bulanıklığı, görme bozuklukları veya konuşma güçlüğü (intrakraniyal kanama "
                "şüphesi), ciddi karın ağrısı (iç kanama olasılığı).</p>"
                "<p><strong>Tromboz belirtileri (düşük INR):</strong> Bacakta şişlik, kızarıklık ve ağrı "
                "(DVT şüphesi), ani nefes darlığı ve göğüs ağrısı (pulmoner emboli), yüzde düşme, kol "
                "güçsüzlüğü veya konuşma bozukluğu (inme). Bu belirtiler acil tıbbi yardım gerektirir.</p>"
                "<p>Varfarin tedavisi altındaysanız ve INR değeriniz hedef aralığın dışındaysa, dozu "
                "kendi başınıza ayarlamayın — mutlaka doktorunuza danışın. Ayrıca cerrahi veya diş çekimi "
                "gibi işlemlerden önce INR kontrolü yaptırmanız önemlidir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızı <a href=\"/analyze\">Norya'ya yükleyerek</a> INR, PT ve "
                "ilişkili biyobelirteçlerin yapılandırılmış, anlaşılır bir özetini dakikalar içinde "
                "alabilirsiniz. Norya, değerlerinizi referans aralıklarıyla karşılaştırır, anormal "
                "sonuçları vurgular ve hekim görüşmenize hazırlanmanız için net bir sağlık raporu oluşturur.</p>"
                "<p>Norya teşhis koymaz veya tedavi önermez — amacı, karmaşık laboratuvar verilerini "
                "sade bir dile çevirerek sizi bilinçli bir hasta yapmaktır. Sonuçlarınızı doktorunuzla "
                "paylaşarak daha verimli bir görüşme gerçekleştirebilirsiniz. "
                "<a href=\"/analyze\">Hemen analizi başlatın</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Uyarı",
                body_html='<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. <a href="/analyze">Norya ile analiz başlat</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# ENGLISH
# ─────────────────────────────────────────────────────────────────────
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR and Prothrombin Time (PT): What your results mean",
            body_html=(
                "<p>The <strong>INR (International Normalized Ratio)</strong> and <strong>Prothrombin Time "
                "(PT)</strong> are blood tests that measure how long it takes your blood to form a clot. "
                "They evaluate the <em>extrinsic</em> and <em>common</em> pathways of the coagulation "
                "cascade &mdash; a complex chain reaction of clotting factors that stops bleeding when a "
                "blood vessel is injured. These tests are essential for patients on anticoagulant therapy, "
                "but are also widely used to assess liver function, diagnose bleeding disorders, and "
                "prepare for surgery.</p>"
                "<p>INR is especially important for patients taking warfarin (Coumadin). Regular INR "
                "monitoring ensures the dose keeps blood thin enough to prevent clots but not so thin that "
                "dangerous bleeding occurs. For patients not on anticoagulants, an elevated INR may signal "
                "liver disease, vitamin K deficiency, or clotting factor deficiencies that require further "
                "investigation.</p>"
                "<p>This guide explains what PT and INR measure, their normal and therapeutic ranges, "
                "common causes of abnormal results, and the relationship between INR, warfarin therapy, "
                "and liver function. It is educational only and does not replace professional medical advice.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="What are PT and INR?",
            body_html=(
                "<p><strong>Prothrombin Time (PT)</strong> measures the time, in seconds, for plasma to "
                "clot after adding tissue factor (thromboplastin) and calcium to a blood sample. It "
                "primarily assesses clotting factors I (fibrinogen), II (prothrombin), V, VII, and X. "
                "Because different laboratories use different thromboplastin reagents, raw PT results can "
                "vary between facilities &mdash; making direct comparisons unreliable.</p>"
                "<p>The <strong>INR</strong> was introduced by the World Health Organization to standardize "
                "PT results worldwide. It uses a mathematical formula that accounts for the sensitivity "
                "of the thromboplastin reagent: <em>INR = (patient PT / mean normal PT)<sup>ISI</sup></em>, "
                "where ISI (International Sensitivity Index) reflects the reagent's responsiveness. This "
                "standardization ensures an INR of 2.5 means the same thing regardless of which laboratory "
                "performed the test &mdash; critical for patients on warfarin who may have blood drawn "
                "at different facilities.</p>"
                "<p>A higher INR means the blood takes longer to clot (more &ldquo;thin&rdquo;), while a "
                "lower INR means the blood clots faster. In clinical practice, INR is the preferred "
                "metric for anticoagulant monitoring, while PT in seconds is used more commonly in "
                "emergency and surgical settings.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="How blood coagulation works",
            body_html=(
                "<p>Blood coagulation (clotting) is the body's mechanism to stop bleeding when a vessel "
                "is damaged. It involves three interconnected pathways: the <strong>extrinsic pathway</strong> "
                "(initiated by tissue damage, via Factor VII and tissue factor), the <strong>intrinsic "
                "pathway</strong> (initiated by blood-surface contact, via Factors XII, XI, IX, and VIII), "
                "and the <strong>common pathway</strong> (Factor X, V, prothrombin, and fibrinogen). "
                "PT/INR specifically evaluates the extrinsic and common pathways.</p>"
                "<p>When tissue factor is released from damaged cells, it binds Factor VII to form a "
                "complex that activates Factor X. Activated Factor X, together with Factor V, converts "
                "prothrombin (Factor II) into <em>thrombin</em>. Thrombin then converts fibrinogen (Factor I) "
                "into <em>fibrin</em> strands, which cross-link to form a stable clot. Any deficiency "
                "or inhibition of these factors prolongs PT and raises INR.</p>"
                "<p>Vitamin K is essential for the liver's synthesis of Factors II, VII, IX, and X, as "
                "well as anticoagulant proteins C and S. Vitamin K antagonists like warfarin block the "
                "recycling of vitamin K, reducing the production of these factors and thereby slowing "
                "coagulation. This mechanism underpins anticoagulant therapy and explains why dietary "
                "vitamin K intake affects INR in patients on warfarin.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal INR and PT ranges",
            body_html=(
                "<p>The table below summarizes commonly accepted reference ranges for INR and PT. Keep in "
                "mind that slight variations exist between laboratories; always interpret your results "
                "alongside your lab's specific reference intervals.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Clinical Situation</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>PT (seconds)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Not on anticoagulants</td>'
                f'<td {_TD}>0.8 &ndash; 1.1</td>'
                f'<td {_TD}>11 &ndash; 13.5</td></tr>'
                f'<tr><td {_TD}>Warfarin therapy (most indications)</td>'
                f'<td {_TD}>2.0 &ndash; 3.0</td>'
                f'<td {_TD}>Varies</td></tr>'
                f'<tr><td {_TD}>Mechanical heart valves</td>'
                f'<td {_TD}>2.5 &ndash; 3.5</td>'
                f'<td {_TD}>Varies</td></tr>'
                f'<tr><td {_TD}>High-risk cases (recurrent thromboembolism)</td>'
                f'<td {_TD}>3.0 &ndash; 4.0</td>'
                f'<td {_TD}>Varies</td></tr>'
                f'</tbody></table>'
                "<p>For patients <strong>not on anticoagulants</strong>, a normal INR is 0.8&ndash;1.1. "
                "Any value above 1.1 in this population warrants investigation for liver disease, vitamin K "
                "deficiency, or clotting factor abnormalities. For patients <strong>on warfarin</strong>, "
                "the therapeutic target is usually 2.0&ndash;3.0, though conditions such as mechanical "
                "mitral valves or recurrent thromboembolism may require a higher target of 2.5&ndash;3.5.</p>"
                "<p>An INR above the therapeutic range increases bleeding risk; below it increases "
                "clotting risk. PT is reported in seconds and varies with the reagent used, which is "
                "precisely why INR was created &mdash; to provide a universal, comparable value.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Causes of high INR (prolonged PT)",
            body_html=(
                "<p><strong>High INR</strong> indicates the blood is clotting more slowly than normal, "
                "increasing the risk of bleeding. The most common causes include:</p>"
                "<p><strong>Warfarin / anticoagulant therapy:</strong> This is the intended therapeutic "
                "effect of warfarin. However, over-dosing, drug interactions (especially NSAIDs, "
                "antibiotics such as metronidazole and fluconazole, amiodarone), or a sudden decrease "
                "in dietary vitamin K can push INR above the target range. An INR &gt; 4.0 carries "
                "significant bleeding risk; INR &gt; 9.0 is a medical emergency requiring urgent "
                "reversal. Newer direct oral anticoagulants (DOACs) do not affect PT/INR in the same "
                "predictable manner.</p>"
                "<p><strong>Liver disease:</strong> The liver synthesizes the majority of clotting factors. "
                "Cirrhosis, hepatitis, acute liver failure, and hepatocellular carcinoma all impair factor "
                "production and elevate INR. In liver disease, INR is also used prognostically &mdash; it "
                "is a component of the MELD (Model for End-Stage Liver Disease) score used to prioritize "
                "liver transplant candidates.</p>"
                "<p><strong>Vitamin K deficiency:</strong> Insufficient dietary intake, malabsorption "
                "syndromes (celiac disease, Crohn's disease, short bowel syndrome), prolonged antibiotic "
                "use (disrupting gut flora that produces vitamin K), or biliary obstruction can lead to "
                "vitamin K deficiency and elevated INR. <strong>DIC (Disseminated Intravascular "
                "Coagulation):</strong> This severe condition involves the widespread activation and "
                "subsequent depletion of clotting factors and platelets, leading to both thrombosis and "
                "bleeding with markedly elevated INR.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Causes of low INR",
            body_html=(
                "<p><strong>Low INR</strong> means the blood is clotting faster than normal, which may "
                "increase thrombotic risk. In patients not on anticoagulants, a low INR (below 0.8) is "
                "uncommon and usually clinically insignificant. However, in patients on warfarin, an INR "
                "below the therapeutic target is clinically important as it indicates insufficient "
                "anticoagulation.</p>"
                "<p><strong>Inadequate anticoagulant dose:</strong> If the warfarin dose is too low, INR "
                "stays below the therapeutic range, leaving the patient at risk for deep vein thrombosis "
                "(DVT), pulmonary embolism, or ischemic stroke. Dose adjustments must always be made "
                "under medical supervision.</p>"
                "<p><strong>Excessive vitamin K intake:</strong> Foods rich in vitamin K (dark leafy "
                "greens, broccoli, Brussels sprouts, liver) or vitamin K supplements counteract warfarin's "
                "effect and lower INR. Patients on warfarin should maintain consistent vitamin K intake "
                "rather than avoiding it altogether &mdash; sudden increases or decreases in consumption "
                "can destabilize INR.</p>"
                "<p><strong>Drug interactions:</strong> Certain medications (rifampin, carbamazepine, "
                "barbiturates, phenytoin, St. John's Wort) induce hepatic CYP2C9 and CYP3A4 enzymes, "
                "accelerating warfarin metabolism and lowering INR. Fresh frozen plasma (FFP) transfusion "
                "also directly replaces clotting factors and rapidly lowers INR. Additionally, some "
                "herbal supplements and high doses of vitamin C can interfere with warfarin's effect.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR monitoring and warfarin therapy",
            body_html=(
                "<p>Warfarin (Coumadin) is the most widely prescribed oral anticoagulant and works as "
                "a vitamin K antagonist. It is indicated for atrial fibrillation, deep vein thrombosis, "
                "pulmonary embolism, mechanical heart valves, and recurrent thromboembolic events. "
                "The safety and efficacy of warfarin therapy depend entirely on regular INR monitoring.</p>"
                "<p>At the start of therapy, INR is typically checked every <strong>2&ndash;3 days</strong> "
                "until values stabilize within the target range. Once stable, monitoring frequency can be "
                "extended to every <strong>2&ndash;4 weeks</strong>. The target INR is determined by "
                "indication: 2.0&ndash;3.0 for most conditions, 2.5&ndash;3.5 for mechanical valve "
                "patients. If INR rises above the target, bleeding risk increases; if it falls below, "
                "thrombotic risk increases.</p>"
                "<p>Several factors influence INR stability during warfarin therapy: dietary vitamin K "
                "intake, concurrent medications, alcohol consumption, acute illness, and changes in liver "
                "or kidney function. Patient education about dietary consistency, avoidance of herbal "
                "supplements without medical advice, and prompt reporting of bleeding signs are "
                "cornerstones of successful anticoagulant management. While direct oral anticoagulants "
                "(DOACs &mdash; rivaroxaban, apixaban, dabigatran, edoxaban) have largely replaced "
                "warfarin for many indications and do not require routine INR monitoring, warfarin "
                "remains the standard for mechanical heart valves and some specific conditions.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR and liver function",
            body_html=(
                "<p>The liver is the central organ responsible for synthesizing nearly all coagulation "
                "factors (Factors I, II, V, VII, IX, X, XI, XII, XIII, and proteins C and S). Consequently, "
                "liver disease directly impairs coagulation function and leads to prolonged PT/INR. Unlike "
                "warfarin-induced INR elevation, which responds to vitamin K administration, liver-related "
                "INR elevation often does not improve with vitamin K because the problem is the liver's "
                "inability to produce factors, not a substrate deficiency.</p>"
                "<p>In <strong>cirrhosis</strong>, INR correlates with disease severity. Both the "
                "Child-Pugh classification and the MELD (Model for End-Stage Liver Disease) score "
                "incorporate INR as a key parameter for assessing hepatic function and transplant "
                "priority. In <strong>acute liver failure</strong>, INR rises rapidly and serves as an "
                "important prognostic indicator &mdash; an INR &gt; 6.5 in acetaminophen-induced liver "
                "failure is one of the King's College criteria for emergency transplantation.</p>"
                "<p>When evaluating an elevated INR, clinicians consider liver function tests (ALT, AST, "
                "bilirubin, albumin) alongside PT/INR to differentiate hepatic causes from other "
                "etiologies. In patients with both liver disease and a need for anticoagulation, INR "
                "interpretation becomes particularly complex, as the baseline INR is already elevated. "
                "Specialized hematology consultation is often required in these cases.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult a healthcare professional if any of the following apply:</p>"
                "<p><strong>Bleeding signs (high INR):</strong> Unexplained bruising, prolonged bleeding "
                "from cuts, gum bleeding, nosebleeds, blood in urine or stool, unusually heavy menstrual "
                "periods, or coughing up blood. <strong>Emergency signs:</strong> severe headache with "
                "confusion, visual disturbances, or speech difficulty (possible intracranial hemorrhage); "
                "severe abdominal pain with lightheadedness (possible internal bleeding).</p>"
                "<p><strong>Thrombotic signs (low INR on warfarin):</strong> Leg swelling, redness, and "
                "pain (possible DVT); sudden shortness of breath and chest pain (possible pulmonary "
                "embolism); facial drooping, arm weakness, or speech slurring (possible stroke). These "
                "symptoms require emergency medical attention.</p>"
                "<p>If you are on warfarin and your INR is outside the target range, never adjust your "
                "dose on your own &mdash; contact your doctor. Additionally, have your INR checked before "
                "any surgical or dental procedure.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your results",
            body_html=(
                "<p>Upload your blood test report to <a href=\"/analyze\">Norya</a> and receive a "
                "structured, easy-to-understand summary of your INR, PT, and related biomarkers within "
                "minutes. Norya compares your values against reference ranges, highlights abnormalities, "
                "and generates a clear health report to help you prepare for your doctor visit.</p>"
                "<p>Norya does not diagnose or recommend treatment &mdash; its purpose is to translate "
                "complex lab data into plain language so you become a more informed patient. Share your "
                "report with your physician for a more productive consultation. "
                "<a href=\"/analyze\">Start your analysis now</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>This guide is for informational purposes only and does not replace medical advice or diagnosis.</strong> Always discuss your results with a healthcare professional. <a href="/analyze">Start analysis with Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# SPANISH
# ─────────────────────────────────────────────────────────────────────
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR y Tiempo de Protrombina (TP): ¿qué significan tus resultados?",
            body_html=(
                "<p>El <strong>INR (Ratio Internacional Normalizado)</strong> y el <strong>Tiempo de "
                "Protrombina (TP)</strong> son análisis de sangre que miden cuánto tarda la sangre en "
                "coagularse. Evalúan las vías <em>extrínseca</em> y <em>común</em> de la cascada de "
                "coagulación, una reacción en cadena compleja de factores de coagulación que detiene "
                "el sangrado cuando un vaso sanguíneo se daña.</p>"
                "<p>El INR es especialmente importante para pacientes que toman anticoagulantes como la "
                "warfarina (Sintrom/Aldocumar). La monitorización regular garantiza que la dosis mantenga "
                "la sangre lo suficientemente diluida para prevenir coágulos, pero no tanto como para "
                "causar sangrado peligroso. También se solicita para evaluar la función hepática, "
                "diagnosticar trastornos hemorrágicos o antes de intervenciones quirúrgicas.</p>"
                "<p>Esta guía explica qué miden el TP y el INR, sus rangos normales y terapéuticos, y "
                "las causas más comunes de resultados anormales. Es solo educativa y no sustituye "
                "el consejo médico profesional.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="¿Qué son el TP y el INR?",
            body_html=(
                "<p>El <strong>Tiempo de Protrombina (TP)</strong> mide, en segundos, el tiempo que tarda "
                "el plasma en coagularse tras añadir tromboplastina tisular y calcio a una muestra de "
                "sangre. Evalúa principalmente los factores de coagulación I (fibrinógeno), II "
                "(protrombina), V, VII y X. Dado que cada laboratorio utiliza reactivos de tromboplastina "
                "diferentes, los resultados brutos de TP pueden variar entre centros.</p>"
                "<p>El <strong>INR</strong> se creó para estandarizar los resultados de TP a nivel mundial. "
                "Utiliza una fórmula matemática que tiene en cuenta la sensibilidad del reactivo: "
                "<em>INR = (TP del paciente / TP medio normal)<sup>ISI</sup></em>. Así, un INR de 2,5 "
                "significa lo mismo independientemente del laboratorio que haya realizado la prueba.</p>"
                "<p>Un INR más alto indica coagulación más lenta (mayor riesgo de sangrado); un INR más "
                "bajo indica coagulación más rápida (mayor riesgo de trombosis). En la práctica clínica, "
                "el INR es la métrica preferida para el control de anticoagulantes, mientras que el TP "
                "en segundos se utiliza más en urgencias y contextos quirúrgicos.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Cómo funciona la coagulación sanguínea",
            body_html=(
                "<p>La coagulación sanguínea es el mecanismo del cuerpo para detener el sangrado cuando "
                "un vaso se daña. Involucra tres vías interconectadas: la <strong>vía extrínseca</strong> "
                "(iniciada por el daño tisular, a través del Factor VII y el factor tisular), la "
                "<strong>vía intrínseca</strong> (iniciada por el contacto sangre-superficie, vía Factores "
                "XII, XI, IX y VIII) y la <strong>vía común</strong> (Factor X, V, protrombina y "
                "fibrinógeno). El TP/INR evalúa específicamente las vías extrínseca y común.</p>"
                "<p>Cuando el factor tisular se libera de células dañadas, se une al Factor VII para "
                "activar el Factor X. El Factor X activado, junto con el Factor V, convierte la "
                "protrombina en <em>trombina</em>, que a su vez transforma el fibrinógeno en hebras de "
                "<em>fibrina</em> que se entrelazan formando un coágulo estable. Cualquier deficiencia "
                "o inhibición de estos factores prolonga el TP y eleva el INR.</p>"
                "<p>La vitamina K es esencial para la síntesis hepática de los Factores II, VII, IX y X, "
                "así como de las proteínas anticoagulantes C y S. Los antagonistas de la vitamina K como "
                "la warfarina bloquean el reciclaje de la vitamina K, reduciendo la producción de estos "
                "factores y, por tanto, enlenteciendo la coagulación.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos normales de INR y TP",
            body_html=(
                "<p>La siguiente tabla resume los rangos de referencia generalmente aceptados.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Situación clínica</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>TP (segundos)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Sin anticoagulantes</td>'
                f'<td {_TD}>0,8 – 1,1</td>'
                f'<td {_TD}>11 – 13,5</td></tr>'
                f'<tr><td {_TD}>Warfarina (mayoría de indicaciones)</td>'
                f'<td {_TD}>2,0 – 3,0</td>'
                f'<td {_TD}>Variable</td></tr>'
                f'<tr><td {_TD}>Válvulas mecánicas</td>'
                f'<td {_TD}>2,5 – 3,5</td>'
                f'<td {_TD}>Variable</td></tr>'
                f'</tbody></table>'
                "<p>Un INR por encima de 1,1 en personas sin anticoagulantes sugiere enfermedad hepática, "
                "deficiencia de vitamina K o anomalías de factores de coagulación. En pacientes bajo "
                "warfarina, el objetivo es habitualmente 2,0–3,0; en válvulas mecánicas, 2,5–3,5.</p>"
                "<p>Un INR por encima del rango terapéutico aumenta el riesgo de sangrado; por debajo, "
                "aumenta el riesgo de trombosis. El TP varía según el reactivo utilizado, razón por la "
                "cual se creó el INR como valor universal y comparable.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Causas de INR alto (TP prolongado)",
            body_html=(
                "<p><strong>Un INR alto</strong> indica que la sangre coagula más lentamente de lo normal, "
                "lo que aumenta el riesgo de sangrado. Las causas más frecuentes son:</p>"
                "<p><strong>Tratamiento con warfarina:</strong> El efecto terapéutico esperado. Sin embargo, "
                "sobredosificación, interacciones medicamentosas (AINEs, antibióticos, antifúngicos) o una "
                "disminución brusca de vitamina K en la dieta pueden elevar el INR por encima del rango "
                "objetivo. Un INR &gt; 4,0 conlleva un riesgo hemorrágico significativo; un INR &gt; 9,0 "
                "es una emergencia médica.</p>"
                "<p><strong>Enfermedad hepática:</strong> El hígado sintetiza la mayoría de los factores de "
                "coagulación. La cirrosis, hepatitis, insuficiencia hepática o carcinoma hepatocelular "
                "alteran la producción de factores y elevan el INR. En la enfermedad hepática, el INR se "
                "utiliza pronósticamente como componente del score MELD.</p>"
                "<p><strong>Deficiencia de vitamina K:</strong> Ingesta dietética insuficiente, síndromes "
                "malabsortivos (enfermedad celíaca, enfermedad de Crohn), uso prolongado de antibióticos o "
                "obstrucción biliar. <strong>CID (Coagulación Intravascular Diseminada):</strong> Activación "
                "y consumo masivo de factores de coagulación y plaquetas, con elevación marcada del INR.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Causas de INR bajo",
            body_html=(
                "<p><strong>Un INR bajo</strong> significa que la sangre coagula más rápido de lo normal, "
                "lo que puede aumentar el riesgo trombótico. En personas sin anticoagulantes, un INR bajo "
                "es infrecuente y generalmente no significativo. En pacientes con warfarina, un INR por "
                "debajo del objetivo indica anticoagulación insuficiente.</p>"
                "<p><strong>Dosis insuficiente de anticoagulante:</strong> Un INR por debajo del rango "
                "terapéutico deja al paciente expuesto a trombosis venosa profunda (TVP), embolia pulmonar "
                "o ictus isquémico. El ajuste de dosis siempre debe realizarse bajo supervisión médica.</p>"
                "<p><strong>Exceso de vitamina K:</strong> Alimentos ricos en vitamina K (verduras de hoja "
                "verde oscuro, brócoli, coles de Bruselas) o suplementos antagonizan el efecto de la "
                "warfarina y reducen el INR. Se recomienda mantener una ingesta consistente.</p>"
                "<p><strong>Interacciones farmacológicas:</strong> Rifampicina, carbamazepina, barbitúricos, "
                "fenitoína e hipérico inducen enzimas hepáticas CYP2C9 y CYP3A4, acelerando el "
                "metabolismo de la warfarina. La transfusión de plasma fresco congelado (PFC) también "
                "reduce rápidamente el INR al reponer factores de coagulación.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR y tratamiento con warfarina",
            body_html=(
                "<p>La warfarina es el anticoagulante oral más utilizado y actúa como antagonista de la "
                "vitamina K. Se indica en fibrilación auricular, trombosis venosa profunda, embolia "
                "pulmonar, válvulas cardíacas mecánicas y eventos tromboembólicos recurrentes. La seguridad "
                "y eficacia del tratamiento dependen de la monitorización regular del INR.</p>"
                "<p>Al inicio del tratamiento, el INR se controla cada <strong>2–3 días</strong> hasta "
                "estabilizarse. Una vez estable, los controles se espacian a cada <strong>2–4 semanas</strong>. "
                "El objetivo de INR depende de la indicación: 2,0–3,0 para la mayoría de condiciones; "
                "2,5–3,5 para válvulas mecánicas.</p>"
                "<p>La dieta, medicación concomitante, consumo de alcohol, enfermedades agudas y cambios en "
                "la función hepática influyen en la estabilidad del INR. La educación al paciente sobre "
                "consistencia dietética y comunicación temprana de signos de sangrado son pilares del manejo "
                "exitoso. Los anticoagulantes orales directos (ACOD) no requieren monitorización de INR, "
                "pero la warfarina sigue siendo la opción estándar para válvulas mecánicas.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR y función hepática",
            body_html=(
                "<p>El hígado sintetiza casi todos los factores de la coagulación. Por ello, la enfermedad "
                "hepática deteriora directamente la coagulación y prolonga PT/INR. A diferencia de la "
                "elevación del INR por warfarina, la debida a enfermedad hepática generalmente no responde "
                "a la administración de vitamina K, ya que el problema es la incapacidad del hígado para "
                "producir factores, no un déficit de sustrato.</p>"
                "<p>En la <strong>cirrosis</strong>, el INR se correlaciona con la gravedad. Tanto la "
                "clasificación de Child-Pugh como la puntuación MELD incorporan el INR como parámetro "
                "clave. En la <strong>insuficiencia hepática aguda</strong>, el INR se eleva rápidamente "
                "y tiene valor pronóstico — un INR &gt; 6,5 en la hepatotoxicidad por paracetamol es uno "
                "de los criterios de King's College para trasplante urgente.</p>"
                "<p>Al evaluar un INR elevado, los clínicos consideran las pruebas de función hepática "
                "(ALT, AST, bilirrubina, albúmina) junto con el PT/INR para diferenciar las causas "
                "hepáticas de otras etiologías.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Cuándo consultar al médico",
            body_html=(
                "<p>Consulta a un profesional de la salud si se aplica alguna de las siguientes situaciones:</p>"
                "<p><strong>Signos de sangrado (INR alto):</strong> moretones inexplicables, sangrado "
                "prolongado de cortes, sangrado de encías, epistaxis, sangre en orina o heces, "
                "menstruaciones abundantes, hemoptisis. <strong>Signos de emergencia:</strong> cefalea "
                "intensa con confusión, alteraciones visuales o dificultad para hablar.</p>"
                "<p><strong>Signos de trombosis (INR bajo bajo warfarina):</strong> hinchazón, enrojecimiento "
                "y dolor en la pierna (sospecha de TVP); disnea súbita y dolor torácico (embolia pulmonar); "
                "caída facial, debilidad en el brazo o dificultad del habla (ictus). Estos síntomas "
                "requieren atención médica de urgencia.</p>"
                "<p>Si estás en tratamiento con warfarina y tu INR está fuera del rango objetivo, nunca "
                "ajustes la dosis por tu cuenta — contacta con tu médico.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya te ayuda a entender tus resultados",
            body_html=(
                "<p>Sube tu informe de análisis de sangre a <a href=\"/analyze\">Norya</a> y recibe un "
                "resumen estructurado y fácil de entender de tu INR, TP y biomarcadores relacionados "
                "en cuestión de minutos. Norya compara tus valores con los rangos de referencia, destaca "
                "las anomalías y genera un informe claro para preparar tu visita médica.</p>"
                "<p>Norya no diagnostica ni recomienda tratamiento — su objetivo es traducir datos "
                "complejos de laboratorio a un lenguaje sencillo para que seas un paciente más informado. "
                "<a href=\"/analyze\">Comienza tu análisis ahora</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html='<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# GERMAN
# ─────────────────────────────────────────────────────────────────────
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR und Prothrombinzeit (PT): Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Der <strong>INR (International Normalized Ratio)</strong> und die <strong>Prothrombinzeit "
                "(PT)</strong> sind Bluttests, die messen, wie lange Ihr Blut zum Gerinnen braucht. Sie "
                "bewerten den <em>extrinsischen</em> und <em>gemeinsamen</em> Weg der Gerinnungskaskade "
                "&mdash; eine komplexe Kettenreaktion von Gerinnungsfaktoren, die Blutungen stoppt, wenn "
                "ein Blutgefäß verletzt wird.</p>"
                "<p>Der INR ist besonders wichtig für Patienten, die Antikoagulanzien wie Warfarin "
                "(Marcumar/Falithrom) einnehmen. Regelmäßige INR-Kontrollen stellen sicher, dass die "
                "Dosis das Blut ausreichend verdünnt, um Gerinnsel zu verhindern, aber nicht so stark, "
                "dass gefährliche Blutungen auftreten. INR wird auch zur Beurteilung der Leberfunktion, "
                "zur Diagnose von Blutungsstörungen und vor Operationen angefordert.</p>"
                "<p>Dieser Leitfaden erklärt, was PT und INR messen, ihre normalen und therapeutischen "
                "Bereiche sowie die häufigsten Ursachen abnormaler Ergebnisse. Er dient ausschließlich "
                "der Aufklärung und ersetzt keine ärztliche Beratung.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="Was sind PT und INR?",
            body_html=(
                "<p>Die <strong>Prothrombinzeit (PT)</strong> misst in Sekunden die Zeit, die Plasma zum "
                "Gerinnen benötigt, nachdem Gewebefaktor (Thromboplastin) und Calcium zur Blutprobe "
                "hinzugefügt wurden. Sie bewertet vor allem die Gerinnungsfaktoren I (Fibrinogen), "
                "II (Prothrombin), V, VII und X.</p>"
                "<p>Der <strong>INR</strong> wurde von der WHO eingeführt, um PT-Ergebnisse weltweit zu "
                "standardisieren. Die Formel lautet: <em>INR = (Patienten-PT / mittlere Normal-PT)"
                "<sup>ISI</sup></em>. So bedeutet ein INR von 2,5 weltweit dasselbe, unabhängig vom "
                "verwendeten Labor.</p>"
                "<p>Ein höherer INR bedeutet langsamere Gerinnung (Blutungsrisiko); ein niedrigerer INR "
                "bedeutet schnellere Gerinnung (Thromboserisiko). In der klinischen Praxis ist der INR "
                "die bevorzugte Kennzahl für die Antikoagulanzien-Überwachung.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Wie die Blutgerinnung funktioniert",
            body_html=(
                "<p>Die Blutgerinnung ist der Mechanismus des Körpers, um Blutungen bei Gefäßverletzungen "
                "zu stoppen. Sie umfasst drei Wege: den <strong>extrinsischen Weg</strong> (durch "
                "Gewebeschaden über Faktor VII), den <strong>intrinsischen Weg</strong> (durch "
                "Blut-Oberflächen-Kontakt über Faktoren XII, XI, IX, VIII) und den <strong>gemeinsamen "
                "Weg</strong> (Faktor X, V, Prothrombin, Fibrinogen). PT/INR bewertet den extrinsischen "
                "und gemeinsamen Weg.</p>"
                "<p>Wenn Gewebefaktor freigesetzt wird, aktiviert er Faktor VII, der Faktor X aktiviert. "
                "Aktivierter Faktor X wandelt mit Faktor V Prothrombin in <em>Thrombin</em> um. Thrombin "
                "wandelt Fibrinogen in <em>Fibrin</em>-Fäden um, die ein stabiles Gerinnsel bilden. "
                "Jeder Mangel an diesen Faktoren verlängert die PT und erhöht den INR.</p>"
                "<p>Vitamin K ist für die Lebersynthese der Faktoren II, VII, IX und X sowie der "
                "Proteine C und S unerlässlich. Vitamin-K-Antagonisten wie Warfarin hemmen das Recycling "
                "von Vitamin K und verringern so die Produktion dieser Faktoren.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale INR- und PT-Werte",
            body_html=(
                "<p>Die folgende Tabelle fasst die allgemein anerkannten Referenzbereiche zusammen.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Klinische Situation</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>PT (Sekunden)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Ohne Antikoagulanzien</td>'
                f'<td {_TD}>0,8 – 1,1</td>'
                f'<td {_TD}>11 – 13,5</td></tr>'
                f'<tr><td {_TD}>Warfarin-Therapie (meiste Indikationen)</td>'
                f'<td {_TD}>2,0 – 3,0</td>'
                f'<td {_TD}>Variabel</td></tr>'
                f'<tr><td {_TD}>Mechanische Herzklappen</td>'
                f'<td {_TD}>2,5 – 3,5</td>'
                f'<td {_TD}>Variabel</td></tr>'
                f'</tbody></table>'
                "<p>Ohne Antikoagulanzien liegt der normale INR bei <strong>0,8–1,1</strong>. Werte über "
                "1,1 erfordern eine Abklärung auf Lebererkrankung, Vitamin-K-Mangel oder "
                "Gerinnungsfaktor-Mangel.</p>"
                "<p>Unter Warfarin ist das therapeutische Ziel meist 2,0–3,0, bei mechanischen Klappen "
                "2,5–3,5. Ein INR über dem Zielbereich erhöht das Blutungsrisiko; darunter das "
                "Thromboserisiko.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Ursachen für einen hohen INR (verlängerte PT)",
            body_html=(
                "<p><strong>Ein hoher INR</strong> bedeutet, dass das Blut langsamer gerinnt als normal "
                "und das Blutungsrisiko erhöht ist. Häufige Ursachen:</p>"
                "<p><strong>Warfarin-Therapie:</strong> Der erwartete therapeutische Effekt. Überdosierung, "
                "Arzneimittelinteraktionen (NSAIDs, Antibiotika, Antimykotika) oder ein plötzlicher "
                "Rückgang der Vitamin-K-Aufnahme können den INR über den Zielbereich hinaus anheben. "
                "Ein INR &gt; 4,0 birgt ein erhebliches Blutungsrisiko; INR &gt; 9,0 ist ein Notfall.</p>"
                "<p><strong>Lebererkrankung:</strong> Die Leber synthetisiert die Mehrzahl der "
                "Gerinnungsfaktoren. Zirrhose, Hepatitis und Leberversagen beeinträchtigen die "
                "Faktorenproduktion und erhöhen den INR. In der Leberdiagnostik ist INR Teil des "
                "MELD-Scores zur Transplantationspriorisierung.</p>"
                "<p><strong>Vitamin-K-Mangel:</strong> Unzureichende Aufnahme, Malabsorption (Zöliakie, "
                "Morbus Crohn), langfristige Antibiotikatherapie oder Gallengangsobstruktion. "
                "<strong>DIC (Disseminierte Intravasale Gerinnung):</strong> Massive Aktivierung und "
                "Verbrauch von Gerinnungsfaktoren mit gleichzeitig erhöhtem Blutungs- und Thromboserisiko.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Ursachen für einen niedrigen INR",
            body_html=(
                "<p><strong>Ein niedriger INR</strong> bedeutet, dass das Blut schneller gerinnt als "
                "normal, was das Thromboserisiko erhöhen kann. Bei Patienten ohne Antikoagulanzien ist "
                "ein niedriger INR selten und meist klinisch unbedeutend.</p>"
                "<p><strong>Unzureichende Antikoagulanziendosis:</strong> Bei Warfarin-Patienten führt "
                "eine zu niedrige Dosis dazu, dass der INR unter dem therapeutischen Bereich bleibt. "
                "Das Risiko für tiefe Venenthrombose (TVT), Lungenembolie oder ischämischen Schlaganfall "
                "steigt.</p>"
                "<p><strong>Übermäßige Vitamin-K-Zufuhr:</strong> Lebensmittel, die reich an Vitamin K "
                "sind (dunkelgrünes Blattgemüse, Brokkoli), oder Nahrungsergänzungsmittel wirken dem "
                "Warfarin-Effekt entgegen und senken den INR.</p>"
                "<p><strong>Medikamenteninteraktionen:</strong> Rifampicin, Carbamazepin, Barbiturate "
                "und Johanniskraut induzieren Leberenzyme (CYP2C9, CYP3A4), beschleunigen den "
                "Warfarin-Metabolismus und senken den INR. Frischplasma-Transfusionen senken den INR "
                "ebenfalls rasch durch direkte Faktorsubstitution.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR-Monitoring und Warfarin-Therapie",
            body_html=(
                "<p>Warfarin (Marcumar/Falithrom) ist das am häufigsten verschriebene orale "
                "Antikoagulans und wirkt als Vitamin-K-Antagonist. Es wird bei Vorhofflimmern, tiefer "
                "Venenthrombose, Lungenembolie, mechanischen Herzklappen und rezidivierenden "
                "thromboembolischen Ereignissen eingesetzt.</p>"
                "<p>Zu Therapiebeginn wird der INR alle <strong>2–3 Tage</strong> kontrolliert, bis "
                "stabile Werte erreicht sind. Danach wird die Häufigkeit auf <strong>2–4 Wochen</strong> "
                "reduziert. Das INR-Ziel hängt von der Indikation ab: 2,0–3,0 für die meisten "
                "Erkrankungen, 2,5–3,5 für mechanische Klappen.</p>"
                "<p>Ernährung, Begleitmedikation, Alkohol, akute Erkrankungen und Veränderungen der "
                "Leberfunktion beeinflussen die INR-Stabilität. Patientenaufklärung über "
                "Ernährungskonstanz und frühzeitiges Melden von Blutungszeichen sind entscheidend "
                "für ein erfolgreiches Antikoagulanzien-Management.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR und Leberfunktion",
            body_html=(
                "<p>Die Leber ist das zentrale Organ für die Synthese nahezu aller Gerinnungsfaktoren. "
                "Lebererkrankungen beeinträchtigen daher direkt die Gerinnungsfunktion und verlängern "
                "PT/INR. Anders als die warfarinbedingte INR-Erhöhung spricht die leberbedingte "
                "Erhöhung meist nicht auf Vitamin-K-Gabe an.</p>"
                "<p>Bei <strong>Zirrhose</strong> korreliert der INR mit der Krankheitsschwere. Sowohl "
                "die Child-Pugh-Klassifikation als auch der MELD-Score verwenden den INR als "
                "Schlüsselparameter. Bei <strong>akutem Leberversagen</strong> steigt der INR rasch "
                "an und hat prognostische Bedeutung.</p>"
                "<p>Bei der Beurteilung eines erhöhten INR berücksichtigen Kliniker die Leberfunktionstests "
                "(ALT, AST, Bilirubin, Albumin) zusammen mit PT/INR, um hepatische von anderen Ursachen "
                "zu unterscheiden.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann Sie einen Arzt aufsuchen sollten",
            body_html=(
                "<p>Konsultieren Sie einen Arzt in folgenden Situationen:</p>"
                "<p><strong>Blutungszeichen (hoher INR):</strong> Unerklärliche Blutergüsse, anhaltende "
                "Blutungen aus Schnitten, Zahnfleischbluten, Nasenbluten, Blut im Urin oder Stuhl, "
                "starke Menstruationsblutungen, Bluthusten. <strong>Notfallzeichen:</strong> Starke "
                "Kopfschmerzen mit Verwirrtheit, Sehstörungen oder Sprachschwierigkeiten.</p>"
                "<p><strong>Thrombosezeichen (niedriger INR unter Warfarin):</strong> Beinschwellung, "
                "Rötung und Schmerzen (TVT-Verdacht); plötzliche Atemnot und Brustschmerzen "
                "(Lungenembolie); Gesichtslähmung, Armschwäche oder Sprachstörungen (Schlaganfall).</p>"
                "<p>Wenn Sie Warfarin einnehmen und Ihr INR außerhalb des Zielbereichs liegt, passen "
                "Sie die Dosis niemals eigenständig an — sprechen Sie mit Ihrem Arzt.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihre Ergebnisse zu verstehen",
            body_html=(
                "<p>Laden Sie Ihren Bluttest-Bericht bei <a href=\"/analyze\">Norya</a> hoch und erhalten "
                "Sie innerhalb von Minuten eine strukturierte, leicht verständliche Zusammenfassung Ihrer "
                "INR-, PT- und verwandter Biomarkerwerte. Norya vergleicht Ihre Werte mit Referenzbereichen, "
                "hebt Auffälligkeiten hervor und erstellt einen klaren Gesundheitsbericht für Ihren "
                "Arztbesuch.</p>"
                "<p>Norya diagnostiziert nicht und empfiehlt keine Behandlung — es übersetzt komplexe "
                "Labordaten in verständliche Sprache. <a href=\"/analyze\">Starten Sie jetzt Ihre "
                "Analyse</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html='<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# FRENCH
# ─────────────────────────────────────────────────────────────────────
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR et Temps de Prothrombine (TP) : que signifient vos résultats ?",
            body_html=(
                "<p>L'<strong>INR (International Normalized Ratio)</strong> et le <strong>Temps de "
                "Prothrombine (TP)</strong> sont des analyses de sang qui mesurent le temps de coagulation "
                "du sang. Ils évaluent les voies <em>extrinsèque</em> et <em>commune</em> de la cascade "
                "de coagulation, une réaction en chaîne complexe de facteurs de coagulation qui arrête "
                "le saignement lors d'une lésion vasculaire.</p>"
                "<p>L'INR est particulièrement important pour les patients sous anticoagulants comme la "
                "warfarine (Coumadine/Préviscan). Une surveillance régulière garantit que la dose est "
                "suffisante pour prévenir les caillots sans provoquer de saignement dangereux. L'INR est "
                "aussi prescrit pour évaluer la fonction hépatique, diagnostiquer les troubles "
                "hémorragiques ou avant une intervention chirurgicale.</p>"
                "<p>Ce guide est éducatif et ne remplace pas l'avis d'un professionnel de santé.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="Que sont le TP et l'INR ?",
            body_html=(
                "<p>Le <strong>Temps de Prothrombine (TP)</strong> mesure en secondes le temps de "
                "coagulation du plasma après ajout de thromboplastine tissulaire et de calcium. Il évalue "
                "principalement les facteurs I (fibrinogène), II (prothrombine), V, VII et X. Les résultats "
                "bruts de TP varient entre laboratoires en raison des différents réactifs utilisés.</p>"
                "<p>L'<strong>INR</strong> a été créé par l'OMS pour standardiser les résultats de TP dans "
                "le monde entier. La formule est : <em>INR = (TP du patient / TP moyen normal)"
                "<sup>ISI</sup></em>. Un INR de 2,5 a donc la même signification quel que soit le "
                "laboratoire.</p>"
                "<p>Un INR plus élevé signifie une coagulation plus lente (risque hémorragique) ; un INR "
                "plus bas signifie une coagulation plus rapide (risque thrombotique). En pratique clinique, "
                "l'INR est la mesure de référence pour le suivi des anticoagulants.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Comment fonctionne la coagulation sanguine",
            body_html=(
                "<p>La coagulation sanguine est le mécanisme qui arrête le saignement lors d'une lésion "
                "vasculaire. Elle implique trois voies : la <strong>voie extrinsèque</strong> (déclenchée "
                "par le facteur tissulaire et le Facteur VII), la <strong>voie intrinsèque</strong> "
                "(Facteurs XII, XI, IX, VIII) et la <strong>voie commune</strong> (Facteur X, V, "
                "prothrombine, fibrinogène). Le TP/INR évalue les voies extrinsèque et commune.</p>"
                "<p>Le facteur tissulaire active le Facteur VII, qui active le Facteur X. Le Facteur X "
                "activé, avec le Facteur V, convertit la prothrombine en <em>thrombine</em>. La thrombine "
                "transforme le fibrinogène en <em>fibrine</em>, formant un caillot stable. Tout déficit "
                "de ces facteurs prolonge le TP et élève l'INR.</p>"
                "<p>La vitamine K est essentielle pour la synthèse hépatique des Facteurs II, VII, IX et X "
                "et des protéines C et S. Les antagonistes de la vitamine K comme la warfarine bloquent "
                "le recyclage de la vitamine K, réduisant la production de ces facteurs et ralentissant "
                "la coagulation.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales d'INR et de TP",
            body_html=(
                "<p>Le tableau suivant résume les valeurs de référence généralement acceptées.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Situation clinique</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>TP (secondes)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Sans anticoagulant</td>'
                f'<td {_TD}>0,8 – 1,1</td>'
                f'<td {_TD}>11 – 13,5</td></tr>'
                f'<tr><td {_TD}>Warfarine (plupart des indications)</td>'
                f'<td {_TD}>2,0 – 3,0</td>'
                f'<td {_TD}>Variable</td></tr>'
                f'<tr><td {_TD}>Valves mécaniques</td>'
                f'<td {_TD}>2,5 – 3,5</td>'
                f'<td {_TD}>Variable</td></tr>'
                f'</tbody></table>'
                "<p>Sans anticoagulant, un INR normal est de <strong>0,8–1,1</strong>. Toute valeur "
                "supérieure à 1,1 nécessite une investigation pour maladie hépatique, carence en "
                "vitamine K ou anomalie des facteurs de coagulation.</p>"
                "<p>Sous warfarine, l'objectif est habituellement 2,0–3,0 ; pour les valves mécaniques, "
                "2,5–3,5. Un INR au-dessus de la cible augmente le risque hémorragique ; en dessous, "
                "le risque thrombotique.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Causes d'un INR élevé (TP prolongé)",
            body_html=(
                "<p><strong>Un INR élevé</strong> indique que le sang coagule plus lentement, augmentant "
                "le risque de saignement. Causes fréquentes :</p>"
                "<p><strong>Traitement par warfarine :</strong> Effet thérapeutique attendu. Un surdosage, "
                "des interactions médicamenteuses (AINS, antibiotiques, antifongiques) ou une baisse "
                "soudaine de la vitamine K alimentaire peuvent pousser l'INR au-delà de la cible. "
                "Un INR &gt; 4,0 est à risque hémorragique significatif ; un INR &gt; 9,0 est une "
                "urgence médicale.</p>"
                "<p><strong>Maladie hépatique :</strong> Le foie synthétise la majorité des facteurs de "
                "coagulation. Cirrhose, hépatite, insuffisance hépatique altèrent la production et "
                "élèvent l'INR. L'INR fait partie du score MELD pour la priorisation de la greffe "
                "hépatique.</p>"
                "<p><strong>Carence en vitamine K :</strong> Apport insuffisant, malabsorption (maladie "
                "cœliaque, maladie de Crohn), antibiothérapie prolongée, obstruction biliaire. "
                "<strong>CIVD :</strong> Activation et consommation massives des facteurs avec élévation "
                "marquée de l'INR.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Causes d'un INR bas",
            body_html=(
                "<p><strong>Un INR bas</strong> signifie que le sang coagule plus vite que la normale, "
                "pouvant augmenter le risque thrombotique. Sans anticoagulant, un INR bas est rare et "
                "généralement non significatif. Sous warfarine, un INR sous la cible indique une "
                "anticoagulation insuffisante.</p>"
                "<p><strong>Dose insuffisante d'anticoagulant :</strong> Le patient reste exposé au risque "
                "de thrombose veineuse profonde (TVP), d'embolie pulmonaire ou d'AVC ischémique. "
                "L'ajustement de dose doit se faire sous contrôle médical.</p>"
                "<p><strong>Excès de vitamine K :</strong> Aliments riches en vitamine K (légumes verts "
                "foncés, brocoli) ou suppléments antagonisent l'effet de la warfarine.</p>"
                "<p><strong>Interactions médicamenteuses :</strong> Rifampicine, carbamazépine, "
                "barbituriques, millepertuis induisent les enzymes hépatiques CYP2C9 et CYP3A4, "
                "accélérant le métabolisme de la warfarine. La transfusion de plasma frais congelé (PFC) "
                "abaisse aussi rapidement l'INR en apportant directement des facteurs de coagulation.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR et traitement par warfarine",
            body_html=(
                "<p>La warfarine est l'anticoagulant oral le plus prescrit et agit comme antagoniste de "
                "la vitamine K. Elle est indiquée dans la fibrillation auriculaire, la TVP, l'embolie "
                "pulmonaire, les valves mécaniques et les événements thromboemboliques récidivants.</p>"
                "<p>En début de traitement, l'INR est contrôlé tous les <strong>2–3 jours</strong> "
                "jusqu'à stabilisation. Ensuite, les contrôles sont espacés à <strong>2–4 semaines</strong>. "
                "L'objectif dépend de l'indication : 2,0–3,0 pour la plupart ; 2,5–3,5 pour les valves "
                "mécaniques.</p>"
                "<p>L'alimentation, les médicaments concomitants, l'alcool, les maladies aiguës et les "
                "variations de la fonction hépatique influencent la stabilité de l'INR. L'éducation "
                "thérapeutique du patient sur la régularité alimentaire et le signalement précoce des "
                "signes de saignement sont essentiels. Les anticoagulants oraux directs (AOD) ne "
                "nécessitent pas de surveillance de l'INR, mais la warfarine reste le standard pour "
                "les valves mécaniques.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR et fonction hépatique",
            body_html=(
                "<p>Le foie est l'organe central de la synthèse de presque tous les facteurs de "
                "coagulation. La maladie hépatique altère donc directement la coagulation et prolonge "
                "PT/INR. Contrairement à l'élévation de l'INR par warfarine, l'élévation liée à une "
                "maladie hépatique ne répond généralement pas à l'administration de vitamine K.</p>"
                "<p>Dans la <strong>cirrhose</strong>, l'INR est corrélé à la sévérité. Les scores "
                "de Child-Pugh et MELD intègrent l'INR comme paramètre clé. Dans l'<strong>insuffisance "
                "hépatique aiguë</strong>, l'INR s'élève rapidement et a une valeur pronostique — un "
                "INR &gt; 6,5 dans l'hépatotoxicité au paracétamol est l'un des critères de King's "
                "College pour la greffe en urgence.</p>"
                "<p>Les tests hépatiques (ALT, AST, bilirubine, albumine) sont évalués conjointement "
                "avec le PT/INR pour distinguer les causes hépatiques des autres étiologies.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin",
            body_html=(
                "<p>Consultez un professionnel de santé dans les situations suivantes :</p>"
                "<p><strong>Signes de saignement (INR élevé) :</strong> Ecchymoses inexpliquées, "
                "saignements prolongés, gingivorragies, épistaxis, sang dans les urines ou les selles, "
                "règles abondantes, hémoptysie. <strong>Signes d'urgence :</strong> Céphalées sévères "
                "avec confusion, troubles visuels ou difficulté à parler.</p>"
                "<p><strong>Signes de thrombose (INR bas sous warfarine) :</strong> Gonflement, rougeur "
                "et douleur d'un membre inférieur (TVP) ; dyspnée soudaine et douleur thoracique "
                "(embolie pulmonaire) ; paralysie faciale, faiblesse d'un bras ou trouble de la parole "
                "(AVC). Ces symptômes nécessitent une prise en charge urgente.</p>"
                "<p>Si vous prenez de la warfarine et que votre INR est en dehors de la cible, n'ajustez "
                "jamais la dose vous-même — contactez votre médecin.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre vos résultats",
            body_html=(
                "<p>Téléchargez votre bilan sanguin sur <a href=\"/analyze\">Norya</a> et recevez en "
                "quelques minutes un résumé structuré et clair de votre INR, TP et biomarqueurs associés. "
                "Norya compare vos valeurs aux plages de référence, met en évidence les anomalies et "
                "génère un rapport de santé pour préparer votre consultation médicale.</p>"
                "<p>Norya ne diagnostique pas et ne recommande aucun traitement — son but est de traduire "
                "des données de laboratoire complexes en langage simple. "
                "<a href=\"/analyze\">Commencez votre analyse maintenant</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html='<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel de santé. <a href="/analyze">Commencer l\'analyse avec Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# ITALIAN
# ─────────────────────────────────────────────────────────────────────
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR e Tempo di Protrombina (PT): cosa significano i tuoi risultati",
            body_html=(
                "<p>L'<strong>INR (International Normalized Ratio)</strong> e il <strong>Tempo di "
                "Protrombina (PT)</strong> sono esami del sangue che misurano quanto tempo impiega il "
                "sangue a coagulare. Valutano le vie <em>estrinseca</em> e <em>comune</em> della cascata "
                "coagulativa, una reazione a catena complessa dei fattori della coagulazione che arresta "
                "il sanguinamento in caso di lesione vascolare.</p>"
                "<p>L'INR è particolarmente importante per i pazienti in terapia con anticoagulanti come "
                "il warfarin (Coumadin). Il monitoraggio regolare assicura che il dosaggio mantenga il "
                "sangue sufficientemente fluido per prevenire i trombi, ma non così tanto da causare "
                "emorragie pericolose. L'INR viene richiesto anche per valutare la funzionalità epatica, "
                "diagnosticare disturbi emorragici o prima di interventi chirurgici.</p>"
                "<p>Questa guida spiega cosa misurano PT e INR, i loro intervalli normali e terapeutici, "
                "e le cause più comuni di risultati anomali. È solo a scopo educativo e non sostituisce "
                "il parere medico.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="Cosa sono PT e INR?",
            body_html=(
                "<p>Il <strong>Tempo di Protrombina (PT)</strong> misura in secondi il tempo di "
                "coagulazione del plasma dopo l'aggiunta di tromboplastina tissutale e calcio. Valuta "
                "principalmente i fattori I (fibrinogeno), II (protrombina), V, VII e X. Poiché ogni "
                "laboratorio utilizza reagenti di tromboplastina diversi, i risultati grezzi del PT "
                "possono variare.</p>"
                "<p>L'<strong>INR</strong> è stato introdotto dall'OMS per standardizzare i risultati del "
                "PT a livello mondiale. La formula è: <em>INR = (PT paziente / PT medio normale)"
                "<sup>ISI</sup></em>. Un INR di 2,5 ha lo stesso significato indipendentemente dal "
                "laboratorio che ha eseguito l'esame.</p>"
                "<p>Un INR più alto indica coagulazione più lenta (rischio emorragico); un INR più basso "
                "indica coagulazione più rapida (rischio trombotico). Nella pratica clinica, l'INR è la "
                "misura di riferimento per il monitoraggio degli anticoagulanti.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Come funziona la coagulazione del sangue",
            body_html=(
                "<p>La coagulazione sanguigna è il meccanismo dell'organismo per arrestare il sanguinamento "
                "quando un vaso è danneggiato. Coinvolge tre vie: la <strong>via estrinseca</strong> "
                "(innescata dal fattore tissutale e dal Fattore VII), la <strong>via intrinseca</strong> "
                "(Fattori XII, XI, IX, VIII) e la <strong>via comune</strong> (Fattore X, V, protrombina, "
                "fibrinogeno). Il PT/INR valuta le vie estrinseca e comune.</p>"
                "<p>Il fattore tissutale attiva il Fattore VII, che attiva il Fattore X. Il Fattore X "
                "attivato, insieme al Fattore V, converte la protrombina in <em>trombina</em>. La trombina "
                "trasforma il fibrinogeno in <em>fibrina</em>, formando un coagulo stabile. Qualsiasi "
                "deficit di questi fattori prolunga il PT e aumenta l'INR.</p>"
                "<p>La vitamina K è essenziale per la sintesi epatica dei Fattori II, VII, IX e X e delle "
                "proteine C e S. Gli antagonisti della vitamina K come il warfarin bloccano il riciclaggio "
                "della vitamina K, riducendo la produzione di questi fattori e rallentando la "
                "coagulazione.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di INR e PT",
            body_html=(
                "<p>La tabella seguente riassume gli intervalli di riferimento generalmente accettati.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>Situazione clinica</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>PT (secondi)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>Senza anticoagulanti</td>'
                f'<td {_TD}>0,8 – 1,1</td>'
                f'<td {_TD}>11 – 13,5</td></tr>'
                f'<tr><td {_TD}>Warfarin (maggior parte delle indicazioni)</td>'
                f'<td {_TD}>2,0 – 3,0</td>'
                f'<td {_TD}>Variabile</td></tr>'
                f'<tr><td {_TD}>Valvole meccaniche</td>'
                f'<td {_TD}>2,5 – 3,5</td>'
                f'<td {_TD}>Variabile</td></tr>'
                f'</tbody></table>'
                "<p>Senza anticoagulanti, un INR normale è <strong>0,8–1,1</strong>. Valori superiori a "
                "1,1 richiedono un'indagine per epatopatia, deficit di vitamina K o anomalie dei fattori "
                "di coagulazione.</p>"
                "<p>Con warfarin, l'obiettivo è solitamente 2,0–3,0; per le valvole meccaniche, 2,5–3,5. "
                "Un INR sopra il target aumenta il rischio emorragico; sotto il target, il rischio "
                "trombotico.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Cause di INR alto (PT prolungato)",
            body_html=(
                "<p><strong>Un INR alto</strong> indica che il sangue coagula più lentamente del normale, "
                "aumentando il rischio di sanguinamento. Le cause più comuni:</p>"
                "<p><strong>Terapia con warfarin:</strong> Effetto terapeutico atteso. Sovradosaggio, "
                "interazioni farmacologiche (FANS, antibiotici, antimicotici) o una diminuzione improvvisa "
                "dell'assunzione di vitamina K possono spingere l'INR oltre il target. Un INR &gt; 4,0 "
                "comporta un rischio emorragico significativo; INR &gt; 9,0 è un'emergenza medica.</p>"
                "<p><strong>Epatopatia:</strong> Il fegato sintetizza la maggior parte dei fattori della "
                "coagulazione. Cirrosi, epatite e insufficienza epatica compromettono la produzione dei "
                "fattori e alzano l'INR. L'INR è parte del punteggio MELD per la priorità di "
                "trapianto.</p>"
                "<p><strong>Deficit di vitamina K:</strong> Apporto dietetico insufficiente, malassorbimento "
                "(celiachia, morbo di Crohn), antibioticoterapia prolungata, ostruzione biliare. "
                "<strong>CID (Coagulazione Intravascolare Disseminata):</strong> Attivazione e consumo "
                "massivi dei fattori con INR marcatamente elevato.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Cause di INR basso",
            body_html=(
                "<p><strong>Un INR basso</strong> significa che il sangue coagula più rapidamente del "
                "normale, con potenziale aumento del rischio trombotico. Senza anticoagulanti, un INR "
                "basso è raro e generalmente non significativo. Con warfarin, un INR sotto il target "
                "indica anticoagulazione insufficiente.</p>"
                "<p><strong>Dose insufficiente di anticoagulante:</strong> Il paziente resta esposto al "
                "rischio di trombosi venosa profonda (TVP), embolia polmonare o ictus ischemico. "
                "L'aggiustamento della dose deve essere effettuato sotto supervisione medica.</p>"
                "<p><strong>Eccesso di vitamina K:</strong> Alimenti ricchi di vitamina K (verdure a foglia "
                "verde scuro, broccoli) o integratori antagonizzano l'effetto del warfarin.</p>"
                "<p><strong>Interazioni farmacologiche:</strong> Rifampicina, carbamazepina, barbiturici, "
                "iperico inducono gli enzimi epatici CYP2C9 e CYP3A4, accelerando il metabolismo del "
                "warfarin. La trasfusione di plasma fresco congelato (PFC) abbassa rapidamente l'INR "
                "sostituendo direttamente i fattori della coagulazione.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR e terapia con warfarin",
            body_html=(
                "<p>Il warfarin (Coumadin) è l'anticoagulante orale più prescritto e agisce come "
                "antagonista della vitamina K. È indicato per fibrillazione atriale, TVP, embolia "
                "polmonare, valvole cardiache meccaniche ed eventi tromboembolici ricorrenti.</p>"
                "<p>All'inizio della terapia, l'INR viene controllato ogni <strong>2–3 giorni</strong> "
                "fino a stabilizzazione. Successivamente, i controlli si distanziano a <strong>2–4 "
                "settimane</strong>. L'obiettivo dipende dall'indicazione: 2,0–3,0 per la maggior parte "
                "delle condizioni; 2,5–3,5 per le valvole meccaniche.</p>"
                "<p>Dieta, farmaci concomitanti, alcol, malattie acute e variazioni della funzionalità "
                "epatica influenzano la stabilità dell'INR. L'educazione del paziente sulla costanza "
                "alimentare e la segnalazione precoce di segni di sanguinamento sono fondamentali. "
                "I DOAC (anticoagulanti orali diretti) non richiedono monitoraggio dell'INR, ma il "
                "warfarin resta lo standard per le valvole meccaniche.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR e funzionalità epatica",
            body_html=(
                "<p>Il fegato è l'organo centrale per la sintesi di quasi tutti i fattori della "
                "coagulazione. Le epatopatie compromettono direttamente la coagulazione e prolungano "
                "PT/INR. A differenza dell'elevazione dell'INR da warfarin, quella da epatopatia "
                "generalmente non risponde alla somministrazione di vitamina K.</p>"
                "<p>Nella <strong>cirrosi</strong>, l'INR è correlato alla gravità della malattia. Sia "
                "la classificazione di Child-Pugh che il punteggio MELD includono l'INR come parametro "
                "chiave. Nell'<strong>insufficienza epatica acuta</strong>, l'INR si eleva rapidamente "
                "e ha valore prognostico.</p>"
                "<p>I test di funzionalità epatica (ALT, AST, bilirubina, albumina) vengono valutati "
                "insieme al PT/INR per distinguere le cause epatiche da altre eziologie.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico",
            body_html=(
                "<p>Consultate un medico nelle seguenti situazioni:</p>"
                "<p><strong>Segni di sanguinamento (INR alto):</strong> Lividi inspiegabili, sanguinamento "
                "prolungato da tagli, sanguinamento gengivale, epistassi, sangue nelle urine o nelle feci, "
                "mestruazioni abbondanti, emottisi. <strong>Segni di emergenza:</strong> cefalea severa "
                "con confusione, disturbi visivi o difficoltà nel parlare.</p>"
                "<p><strong>Segni di trombosi (INR basso con warfarin):</strong> Gonfiore, arrossamento "
                "e dolore a una gamba (TVP); dispnea improvvisa e dolore toracico (embolia polmonare); "
                "caduta del viso, debolezza di un braccio o difficoltà nel parlare (ictus). Questi "
                "sintomi richiedono cure urgenti.</p>"
                "<p>Se siete in terapia con warfarin e il vostro INR è fuori dal range target, non "
                "modificate mai il dosaggio autonomamente — contattate il medico.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a capire i tuoi risultati",
            body_html=(
                "<p>Carica il tuo referto di analisi del sangue su <a href=\"/analyze\">Norya</a> e "
                "ricevi in pochi minuti un riepilogo strutturato e chiaro di INR, PT e biomarcatori "
                "correlati. Norya confronta i tuoi valori con gli intervalli di riferimento, evidenzia "
                "le anomalie e genera un report sanitario per preparare la tua visita medica.</p>"
                "<p>Norya non diagnostica né raccomanda trattamenti — traduce dati di laboratorio "
                "complessi in linguaggio semplice. <a href=\"/analyze\">Inizia l'analisi ora</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html='<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR וזמן פרותרומבין (PT): מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p><strong>INR (International Normalized Ratio)</strong> ו<strong>זמן פרותרומבין "
                "(PT)</strong> הן בדיקות דם המודדות כמה זמן לוקח לדם שלך להיקרש. הן מעריכות את "
                "המסלולים ה<em>אקסטרינזי</em> וה<em>משותף</em> של מפל הקרישה — שרשרת תגובות מורכבת "
                "של גורמי קרישה שעוצרת דימום כאשר כלי דם נפגע.</p>"
                "<p>ה-INR חשוב במיוחד לחולים הנוטלים תרופות נוגדות קרישה כמו וורפרין (קומדין). ניטור "
                "סדיר מבטיח שהמינון שומר על הדם מדולל מספיק למניעת קרישים, אך לא כל כך מדולל שיגרום "
                "לדימום מסוכן. INR נבדק גם להערכת תפקודי כבד, אבחון הפרעות דימום ולפני ניתוחים.</p>"
                "<p>מדריך זה מסביר מה מודדים PT ו-INR, את הטווחים התקינים והטיפוליים, וגורמים נפוצים "
                "לתוצאות חריגות. הוא חינוכי בלבד ואינו מחליף ייעוץ רפואי מקצועי.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="מהם PT ו-INR?",
            body_html=(
                "<p><strong>זמן פרותרומבין (PT)</strong> מודד בשניות את הזמן שלוקח לפלזמה להיקרש לאחר "
                "הוספת גורם רקמתי (תרומבופלסטין) וסידן לדגימת דם. הוא מעריך בעיקר את גורמי הקרישה "
                "I (פיברינוגן), II (פרותרומבין), V, VII ו-X. מכיוון שמעבדות שונות משתמשות בריאגנטים "
                "שונים, תוצאות PT גולמיות עשויות להשתנות בין מעבדות.</p>"
                "<p><strong>INR</strong> פותח כדי לתקנן תוצאות PT ברחבי העולם. הנוסחה: <em>INR = (PT "
                "מטופל / PT ממוצע תקין)<sup>ISI</sup></em>. כך INR של 2.5 משמעו אותו דבר בכל מעבדה "
                "בעולם — קריטי למטופלים תחת וורפרין שנבדקים במעבדות שונות.</p>"
                "<p>INR גבוה יותר = קרישה איטית יותר (סיכון לדימום); INR נמוך יותר = קרישה מהירה "
                "יותר (סיכון לקריש). בפרקטיקה הקלינית, INR הוא המדד המועדף לניטור נוגדי קרישה.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="כיצד פועלת מערכת קרישת הדם",
            body_html=(
                "<p>קרישת דם היא מנגנון הגוף לעצירת דימום כאשר כלי דם נפגע. היא כוללת שלושה מסלולים: "
                "ה<strong>מסלול האקסטרינזי</strong> (מופעל על ידי נזק רקמתי דרך פקטור VII), "
                "ה<strong>מסלול האינטרינזי</strong> (פקטורים XII, XI, IX, VIII) וה<strong>מסלול "
                "המשותף</strong> (פקטור X, V, פרותרומבין, פיברינוגן). PT/INR מעריך את המסלולים "
                "האקסטרינזי והמשותף.</p>"
                "<p>כאשר גורם רקמתי משתחרר מתאים פגועים, הוא מפעיל את פקטור VII, שמפעיל את פקטור X. "
                "פקטור X מופעל, יחד עם פקטור V, ממיר פרותרומבין ל<em>תרומבין</em>. תרומבין ממיר "
                "פיברינוגן לסיבי <em>פיברין</em>, היוצרים קריש יציב. כל חסר בגורמים אלו מאריך את "
                "ה-PT ומעלה את ה-INR.</p>"
                "<p>ויטמין K חיוני לסינתזה בכבד של פקטורים II, VII, IX ו-X וכן של חלבוני C ו-S. "
                "אנטגוניסטים של ויטמין K כמו וורפרין חוסמים את מיחזור ויטמין K, מפחיתים ייצור גורמים "
                "אלו ומאטים את הקרישה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי INR ו-PT תקינים",
            body_html=(
                "<p>הטבלה הבאה מסכמת את טווחי הייחוס המקובלים.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>מצב קליני</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>PT (שניות)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>ללא נוגדי קרישה</td>'
                f'<td {_TD}>0.8 – 1.1</td>'
                f'<td {_TD}>11 – 13.5</td></tr>'
                f'<tr><td {_TD}>וורפרין (רוב ההתוויות)</td>'
                f'<td {_TD}>2.0 – 3.0</td>'
                f'<td {_TD}>משתנה</td></tr>'
                f'<tr><td {_TD}>מסתמים מכניים</td>'
                f'<td {_TD}>2.5 – 3.5</td>'
                f'<td {_TD}>משתנה</td></tr>'
                f'</tbody></table>'
                "<p>ללא נוגדי קרישה, INR תקין הוא <strong>0.8–1.1</strong>. ערך מעל 1.1 מצריך בירור "
                "למחלת כבד, חסר ויטמין K או הפרעות בגורמי קרישה.</p>"
                "<p>תחת וורפרין, היעד הוא בדרך כלל 2.0–3.0; למסתמים מכניים, 2.5–3.5. INR מעל היעד "
                "מגביר סיכון לדימום; מתחתיו — סיכון לקריש.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="גורמים ל-INR גבוה (PT מוארך)",
            body_html=(
                "<p><strong>INR גבוה</strong> מצביע על כך שהדם נקרש לאט יותר מהרגיל, עם עלייה "
                "בסיכון לדימום. הגורמים הנפוצים:</p>"
                "<p><strong>טיפול בוורפרין:</strong> ההשפעה הטיפולית המצופה. מינון יתר, אינטראקציות "
                "תרופתיות (NSAIDs, אנטיביוטיקות, אנטי-פטרייתיים) או ירידה פתאומית בצריכת ויטמין K "
                "עלולים להעלות INR מעבר ליעד. INR &gt; 4.0 מהווה סיכון דימומי משמעותי; INR &gt; 9.0 "
                "הוא מצב חירום רפואי.</p>"
                "<p><strong>מחלת כבד:</strong> הכבד מסנתז את רוב גורמי הקרישה. שחמת, הפטיטיס ואי "
                "ספיקת כבד פוגעים בייצור הגורמים ומעלים INR. INR הוא חלק מציון MELD לתעדוף "
                "השתלות כבד.</p>"
                "<p><strong>חסר ויטמין K:</strong> צריכה תזונתית לקויה, תת-ספיגה (צליאק, קרוהן), "
                "אנטיביוטיקה ממושכת, חסימת דרכי המרה. <strong>DIC:</strong> הפעלה וצריכה מסיבית של "
                "גורמי קרישה עם INR מוגבר בולט.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="גורמים ל-INR נמוך",
            body_html=(
                "<p><strong>INR נמוך</strong> פירושו שהדם נקרש מהר יותר מהרגיל, מה שעלול להגביר את "
                "הסיכון לקרישי דם. ללא נוגדי קרישה, INR נמוך הוא נדיר ולרוב לא משמעותי קלינית. "
                "תחת וורפרין, INR מתחת ליעד מצביע על טיפול נוגד קרישה לא מספיק.</p>"
                "<p><strong>מינון לא מספיק של נוגד קרישה:</strong> המטופל חשוף לסיכון לפקקת ורידים "
                "עמוקים (DVT), תסחיף ריאתי או שבץ איסכמי. התאמת המינון חייבת להתבצע תחת פיקוח "
                "רפואי.</p>"
                "<p><strong>צריכה מוגזמת של ויטמין K:</strong> מזונות עשירים בויטמין K (ירקות עלים "
                "כהים, ברוקולי) או תוספים סותרים את השפעת הוורפרין ומורידים INR.</p>"
                "<p><strong>אינטראקציות תרופתיות:</strong> ריפמפיצין, קרבמזפין, ברביטורטים, סנט ג'ון "
                "וורט מזרזים אנזימי כבד CYP2C9 ו-CYP3A4, מאיצים פירוק וורפרין ומורידים INR. עירוי "
                "פלזמה טרייה קפואה (FFP) גם מוריד INR במהירות על ידי החלפה ישירה של גורמי קרישה.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR וטיפול בוורפרין",
            body_html=(
                "<p>וורפרין (קומדין) הוא נוגד הקרישה הפומי הנפוץ ביותר ופועל כאנטגוניסט של ויטמין K. "
                "הוא ניתן בפרפור פרוזדורים, DVT, תסחיף ריאתי, מסתמי לב מכניים ואירועים "
                "תרומבואמבוליים חוזרים.</p>"
                "<p>בתחילת הטיפול, INR נבדק כל <strong>2–3 ימים</strong> עד להתייצבות. לאחר מכן, "
                "הבדיקות מרווחות ל<strong>2–4 שבועות</strong>. יעד ה-INR נקבע לפי ההתוויה: 2.0–3.0 "
                "לרוב המצבים; 2.5–3.5 למסתמים מכניים.</p>"
                "<p>תזונה, תרופות נלוות, אלכוהול, מחלות חריפות ושינויים בתפקוד הכבד משפיעים על "
                "יציבות ה-INR. חינוך המטופל לגבי עקביות תזונתית ודיווח מוקדם על סימני דימום הם "
                "אבני יסוד בניהול מוצלח של טיפול נוגד קרישה.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR ותפקוד הכבד",
            body_html=(
                "<p>הכבד הוא האיבר המרכזי לסינתזה של כמעט כל גורמי הקרישה. מחלות כבד פוגעות ישירות "
                "בקרישה ומאריכות PT/INR. בניגוד לעליית INR מוורפרין, עלייה הנגרמת ממחלת כבד בדרך "
                "כלל אינה מגיבה למתן ויטמין K.</p>"
                "<p>ב<strong>שחמת</strong>, ה-INR מתואם עם חומרת המחלה. סיווג Child-Pugh וציון MELD "
                "כוללים INR כפרמטר מפתח. ב<strong>אי ספיקת כבד חריפה</strong>, INR עולה במהירות "
                "ונושא ערך פרוגנוסטי — INR &gt; 6.5 בהרעלת פרצטמול הוא אחד מקריטריוני King's "
                "College להשתלה דחופה.</p>"
                "<p>בהערכת INR מוגבר, הרופאים בודקים גם בדיקות תפקודי כבד (ALT, AST, בילירובין, "
                "אלבומין) לצד PT/INR להבדלה בין גורמים כבדיים לאטיולוגיות אחרות.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא",
            body_html=(
                "<p>פנו לרופא במצבים הבאים:</p>"
                "<p><strong>סימני דימום (INR גבוה):</strong> חבורות בלתי מוסברות, דימום ממושך מחתכים, "
                "דימום מחניכיים, דימום מהאף, דם בשתן או בצואה, וסתות כבדות, כיח דמי. <strong>סימני "
                "חירום:</strong> כאב ראש עז עם בלבול, הפרעות ראייה או קשיי דיבור.</p>"
                "<p><strong>סימני קריש (INR נמוך תחת וורפרין):</strong> נפיחות, אדמומיות וכאב ברגל "
                "(DVT); קוצר נשימה פתאומי וכאב בחזה (תסחיף ריאתי); צניחת פנים, חולשת יד או קשיי "
                "דיבור (שבץ). תסמינים אלו דורשים טיפול חירום.</p>"
                "<p>אם אתם נוטלים וורפרין וה-INR מחוץ לטווח היעד, לעולם אל תשנו את המינון בעצמכם — "
                "פנו לרופא.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד Norya עוזרת לכם להבין את התוצאות",
            body_html=(
                "<p>העלו את תוצאות בדיקת הדם שלכם ל<a href=\"/analyze\">Norya</a> וקבלו תוך דקות "
                "סיכום מובנה וברור של ה-INR, PT וסמנים ביולוגיים נלווים. Norya משווה את הערכים שלכם "
                "לטווחי הייחוס, מדגישה ממצאים חריגים ומייצרת דוח בריאות ברור להכנה לביקור אצל "
                "הרופא.</p>"
                "<p>Norya אינה מאבחנת ואינה ממליצה על טיפול — מטרתה לתרגם נתוני מעבדה מורכבים "
                "לשפה פשוטה. <a href=\"/analyze\">התחילו את הניתוח עכשיו</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html='<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> דונו תמיד בתוצאות עם איש מקצוע רפואי. <a href="/analyze">התחל ניתוח עם Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR और प्रोथ्रोम्बिन टाइम (PT): आपके परिणामों का क्या मतलब है?",
            body_html=(
                "<p><strong>INR (International Normalized Ratio)</strong> और <strong>प्रोथ्रोम्बिन टाइम "
                "(PT)</strong> रक्त परीक्षण हैं जो मापते हैं कि आपका रक्त जमने में कितना समय लेता है। "
                "ये परीक्षण कोएगुलेशन कैस्केड के <em>एक्सट्रिन्सिक</em> और <em>कॉमन</em> पाथवे का "
                "मूल्यांकन करते हैं — क्लॉटिंग फैक्टरों की एक जटिल श्रृंखला जो रक्त वाहिका के "
                "क्षतिग्रस्त होने पर रक्तस्राव को रोकती है।</p>"
                "<p>INR विशेष रूप से उन रोगियों के लिए महत्वपूर्ण है जो वारफ़ारिन (कुमैडिन) जैसी "
                "एंटीकोगुलेंट दवाएं ले रहे हैं। नियमित INR निगरानी यह सुनिश्चित करती है कि खुराक "
                "रक्त को थक्कों से बचाने के लिए पर्याप्त पतला रखे, लेकिन इतना पतला नहीं कि "
                "खतरनाक रक्तस्राव हो। INR का उपयोग लिवर फंक्शन, ब्लीडिंग डिसऑर्डर और सर्जरी "
                "से पहले मूल्यांकन के लिए भी किया जाता है।</p>"
                "<p>यह गाइड शैक्षिक है और पेशेवर चिकित्सा सलाह का विकल्प नहीं है।</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="PT और INR क्या हैं?",
            body_html=(
                "<p><strong>प्रोथ्रोम्बिन टाइम (PT)</strong> रक्त नमूने में टिश्यू फैक्टर "
                "(थ्रोम्बोप्लास्टिन) और कैल्शियम मिलाने के बाद प्लाज़्मा के जमने का समय सेकंड में "
                "मापता है। यह मुख्य रूप से क्लॉटिंग फैक्टर I (फाइब्रिनोजन), II (प्रोथ्रोम्बिन), "
                "V, VII और X का मूल्यांकन करता है।</p>"
                "<p><strong>INR</strong> को WHO द्वारा PT परिणामों को विश्व स्तर पर मानकीकृत करने के "
                "लिए विकसित किया गया था। सूत्र: <em>INR = (रोगी PT / औसत सामान्य PT)<sup>ISI</sup></em>। "
                "इससे INR 2.5 का मतलब दुनिया की किसी भी लैब में एक जैसा होता है — यह वारफ़ारिन पर "
                "रोगियों के लिए महत्वपूर्ण है।</p>"
                "<p>उच्च INR = धीमी जमावट (रक्तस्राव का जोखिम); कम INR = तेज़ जमावट (थ्रोम्बोसिस "
                "का जोखिम)। क्लिनिकल प्रैक्टिस में INR एंटीकोगुलेंट मॉनिटरिंग के लिए पसंदीदा "
                "मापदंड है।</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="रक्त जमावट (कोएगुलेशन) कैसे काम करती है",
            body_html=(
                "<p>रक्त जमावट शरीर का वह तंत्र है जो रक्त वाहिका क्षतिग्रस्त होने पर रक्तस्राव "
                "को रोकता है। इसमें तीन मार्ग शामिल हैं: <strong>एक्सट्रिन्सिक पाथवे</strong> (टिश्यू "
                "डैमेज द्वारा शुरू, फैक्टर VII के माध्यम से), <strong>इंट्रिन्सिक पाथवे</strong> "
                "(फैक्टर XII, XI, IX, VIII) और <strong>कॉमन पाथवे</strong> (फैक्टर X, V, प्रोथ्रोम्बिन, "
                "फाइब्रिनोजन)। PT/INR एक्सट्रिन्सिक और कॉमन पाथवे का मूल्यांकन करता है।</p>"
                "<p>टिश्यू फैक्टर फैक्टर VII को सक्रिय करता है, जो फैक्टर X को सक्रिय करता है। "
                "सक्रिय फैक्टर X, फैक्टर V के साथ मिलकर प्रोथ्रोम्बिन को <em>थ्रोम्बिन</em> में "
                "बदलता है। थ्रोम्बिन फिर फाइब्रिनोजन को <em>फाइब्रिन</em> धागों में बदलता है, "
                "जो एक स्थिर थक्का बनाते हैं।</p>"
                "<p>विटामिन K लिवर में फैक्टर II, VII, IX और X तथा प्रोटीन C और S के संश्लेषण के "
                "लिए आवश्यक है। वारफ़ारिन जैसे विटामिन K एंटागोनिस्ट विटामिन K की रीसाइक्लिंग "
                "को रोकते हैं, इन फैक्टरों का उत्पादन घटाते हैं और जमावट को धीमा करते हैं।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य INR और PT स्तर",
            body_html=(
                "<p>नीचे दी गई तालिका सामान्य रूप से स्वीकृत संदर्भ सीमाओं का सारांश प्रस्तुत "
                "करती है।</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>क्लिनिकल स्थिति</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>PT (सेकंड)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>एंटीकोगुलेंट के बिना</td>'
                f'<td {_TD}>0.8 – 1.1</td>'
                f'<td {_TD}>11 – 13.5</td></tr>'
                f'<tr><td {_TD}>वारफ़ारिन थेरेपी (अधिकांश संकेत)</td>'
                f'<td {_TD}>2.0 – 3.0</td>'
                f'<td {_TD}>परिवर्तनशील</td></tr>'
                f'<tr><td {_TD}>मैकेनिकल हार्ट वाल्व</td>'
                f'<td {_TD}>2.5 – 3.5</td>'
                f'<td {_TD}>परिवर्तनशील</td></tr>'
                f'</tbody></table>'
                "<p>एंटीकोगुलेंट के बिना, सामान्य INR <strong>0.8–1.1</strong> है। 1.1 से ऊपर का मान "
                "लिवर रोग, विटामिन K की कमी या क्लॉटिंग फैक्टर असामान्यताओं की जांच की "
                "आवश्यकता बताता है।</p>"
                "<p>वारफ़ारिन पर, लक्ष्य आमतौर पर 2.0–3.0 है; मैकेनिकल वाल्व के लिए 2.5–3.5। "
                "INR लक्ष्य सीमा से ऊपर होने पर रक्तस्राव का जोखिम बढ़ता है; नीचे होने पर "
                "थ्रोम्बोसिस का जोखिम बढ़ता है।</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="उच्च INR (बढ़ा हुआ PT) के कारण",
            body_html=(
                "<p><strong>उच्च INR</strong> इंगित करता है कि रक्त सामान्य से धीमी गति से जम रहा "
                "है, जिससे रक्तस्राव का जोखिम बढ़ जाता है। सामान्य कारण:</p>"
                "<p><strong>वारफ़ारिन थेरेपी:</strong> अपेक्षित चिकित्सीय प्रभाव। ओवरडोज़, दवा "
                "इंटरैक्शन (NSAIDs, एंटीबायोटिक्स, एंटीफंगल) या आहार में विटामिन K की अचानक कमी "
                "INR को लक्ष्य सीमा से ऊपर ले जा सकती है। INR &gt; 4.0 गंभीर रक्तस्राव जोखिम "
                "रखता है; INR &gt; 9.0 चिकित्सा आपातकाल है।</p>"
                "<p><strong>लिवर रोग:</strong> लिवर अधिकांश क्लॉटिंग फैक्टरों को संश्लेषित करता है। "
                "सिरोसिस, हेपेटाइटिस और लिवर फेल्योर फैक्टर उत्पादन को बाधित करते हैं और INR "
                "बढ़ाते हैं। INR, MELD स्कोर का हिस्सा है।</p>"
                "<p><strong>विटामिन K की कमी:</strong> अपर्याप्त आहार, मैलएब्सॉर्प्शन (सीलिएक, "
                "क्रोहन), लंबे समय तक एंटीबायोटिक उपयोग, पित्त नली अवरोध। <strong>DIC:</strong> "
                "क्लॉटिंग फैक्टरों की व्यापक सक्रियता और क्षय के साथ INR में उल्लेखनीय वृद्धि।</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="कम INR के कारण",
            body_html=(
                "<p><strong>कम INR</strong> का मतलब है कि रक्त सामान्य से तेज़ी से जम रहा है, "
                "जिससे थ्रोम्बोटिक जोखिम बढ़ सकता है। एंटीकोगुलेंट के बिना, कम INR दुर्लभ है "
                "और आमतौर पर चिकित्सकीय रूप से महत्वहीन है। वारफ़ारिन पर, लक्ष्य से कम INR "
                "अपर्याप्त एंटीकोगुलेशन का संकेत है।</p>"
                "<p><strong>अपर्याप्त एंटीकोगुलेंट खुराक:</strong> रोगी DVT, पल्मोनरी एम्बोलिज़्म "
                "या इस्केमिक स्ट्रोक के जोखिम में रहता है। खुराक समायोजन हमेशा चिकित्सा "
                "पर्यवेक्षण में होना चाहिए।</p>"
                "<p><strong>अत्यधिक विटामिन K सेवन:</strong> विटामिन K से भरपूर खाद्य पदार्थ "
                "(गहरे हरे पत्तेदार सब्जियां, ब्रोकोली) या सप्लीमेंट वारफ़ारिन के प्रभाव "
                "को प्रतिरोधित करते हैं और INR कम करते हैं।</p>"
                "<p><strong>दवा इंटरैक्शन:</strong> रिफ़ैम्पिसिन, कार्बमेज़ेपिन, बार्बिट्यूरेट्स, "
                "सेंट जॉन्स वॉर्ट लिवर एंजाइम CYP2C9 और CYP3A4 को प्रेरित करते हैं, वारफ़ारिन "
                "मेटाबॉलिज़्म को तेज़ करते हैं और INR कम करते हैं। FFP ट्रांसफ़्यूज़न भी INR "
                "को तेज़ी से कम करता है।</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR और वारफ़ारिन थेरेपी",
            body_html=(
                "<p>वारफ़ारिन (कुमैडिन) सबसे व्यापक रूप से निर्धारित ओरल एंटीकोगुलेंट है और "
                "विटामिन K एंटागोनिस्ट के रूप में काम करता है। यह एट्रियल फ़िब्रिलेशन, DVT, "
                "पल्मोनरी एम्बोलिज़्म, मैकेनिकल हार्ट वाल्व और पुनरावर्ती थ्रोम्बोएम्बोलिक "
                "घटनाओं के लिए दिया जाता है।</p>"
                "<p>थेरेपी की शुरुआत में, INR हर <strong>2–3 दिन</strong> में जांचा जाता है जब तक "
                "मान स्थिर न हो जाएं। स्थिर होने के बाद, निगरानी <strong>2–4 सप्ताह</strong> तक "
                "बढ़ाई जा सकती है। INR लक्ष्य संकेत पर निर्भर करता है: अधिकांश स्थितियों के "
                "लिए 2.0–3.0; मैकेनिकल वाल्व के लिए 2.5–3.5।</p>"
                "<p>आहार, सह-दवाएं, शराब, तीव्र बीमारी और लिवर फंक्शन में परिवर्तन INR स्थिरता "
                "को प्रभावित करते हैं। आहार स्थिरता और रक्तस्राव संकेतों की शीघ्र रिपोर्टिंग पर "
                "रोगी शिक्षा सफल एंटीकोगुलेंट प्रबंधन की नींव है।</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR और लिवर फंक्शन",
            body_html=(
                "<p>लिवर लगभग सभी कोएगुलेशन फैक्टरों के संश्लेषण के लिए जिम्मेदार केंद्रीय "
                "अंग है। लिवर रोग सीधे कोएगुलेशन को प्रभावित करता है और PT/INR को बढ़ाता है। "
                "वारफ़ारिन-प्रेरित INR वृद्धि के विपरीत, लिवर-संबंधित INR वृद्धि आमतौर पर "
                "विटामिन K से सुधार नहीं होती।</p>"
                "<p><strong>सिरोसिस</strong> में, INR रोग की गंभीरता से सहसंबद्ध होता है। "
                "Child-Pugh और MELD दोनों में INR एक प्रमुख पैरामीटर है। <strong>एक्यूट लिवर "
                "फेल्योर</strong> में, INR तेज़ी से बढ़ता है और प्रागनोस्टिक मूल्य रखता है।</p>"
                "<p>बढ़े हुए INR का मूल्यांकन करते समय, चिकित्सक लिवर फंक्शन टेस्ट (ALT, AST, "
                "बिलीरुबिन, एल्बुमिन) को PT/INR के साथ मिलाकर देखते हैं ताकि हेपेटिक कारणों "
                "को अन्य कारणों से अलग किया जा सके।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें",
            body_html=(
                "<p>निम्नलिखित स्थितियों में स्वास्थ्य पेशेवर से परामर्श करें:</p>"
                "<p><strong>रक्तस्राव के संकेत (उच्च INR):</strong> अस्पष्टीकृत नीलापन, कटने से "
                "लंबे समय तक रक्तस्राव, मसूड़ों से खून, नाक से खून, पेशाब या मल में खून, अत्यधिक "
                "मासिक रक्तस्राव, खांसी में खून। <strong>आपातकालीन संकेत:</strong> तीव्र सिरदर्द "
                "के साथ भ्रम, दृष्टि गड़बड़ी या बोलने में कठिनाई।</p>"
                "<p><strong>थ्रोम्बोसिस के संकेत (वारफ़ारिन पर कम INR):</strong> पैर में सूजन, "
                "लालिमा और दर्द (DVT); अचानक सांस फूलना और सीने में दर्द (पल्मोनरी एम्बोलिज़्म); "
                "चेहरे का झुकना, बांह में कमज़ोरी या बोलने में लड़खड़ाहट (स्ट्रोक)।</p>"
                "<p>यदि आप वारफ़ारिन पर हैं और आपका INR लक्ष्य सीमा से बाहर है, तो कभी भी "
                "अपनी खुराक स्वयं न बदलें — अपने डॉक्टर से संपर्क करें।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके परिणामों को समझने में कैसे मदद करता है",
            body_html=(
                "<p>अपनी रक्त परीक्षण रिपोर्ट <a href=\"/analyze\">Norya</a> पर अपलोड करें और "
                "मिनटों में अपने INR, PT और संबंधित बायोमार्करों का एक संरचित, समझने में आसान "
                "सारांश प्राप्त करें। Norya आपके मानों की तुलना संदर्भ सीमाओं से करता है, "
                "असामान्यताओं को हाइलाइट करता है और डॉक्टर विज़िट की तैयारी के लिए स्पष्ट "
                "स्वास्थ्य रिपोर्ट बनाता है।</p>"
                "<p>Norya निदान या उपचार की सिफ़ारिश नहीं करता — यह जटिल लैब डेटा को सरल भाषा "
                "में अनुवादित करता है। <a href=\"/analyze\">अभी अपना विश्लेषण शुरू करें</a>।</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html='<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। <a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="INR وزمن البروثرومبين (PT): ماذا تعني نتائجك؟",
            body_html=(
                "<p><strong>INR (النسبة المعيارية الدولية)</strong> و<strong>زمن البروثرومبين "
                "(PT)</strong> هما تحليلان يقيسان المدة التي يستغرقها دمك للتخثر. يقيّمان المسارين "
                "<em>الخارجي</em> و<em>المشترك</em> لسلسلة التخثر — سلسلة تفاعلات معقدة من عوامل "
                "التخثر تعمل على وقف النزيف عند إصابة وعاء دموي.</p>"
                "<p>يُعد INR مهمًا بشكل خاص للمرضى الذين يتناولون مضادات التخثر مثل الوارفارين "
                "(كومادين). تضمن المراقبة المنتظمة أن الجرعة تحافظ على الدم مخففًا بما يكفي لمنع "
                "الجلطات، ولكن ليس بحيث يسبب نزيفًا خطيرًا. يُطلب INR أيضًا لتقييم وظائف الكبد، "
                "تشخيص اضطرابات النزيف، أو قبل الجراحة.</p>"
                "<p>هذا الدليل تعليمي ولا يحل محل الاستشارة الطبية المتخصصة.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="ما هما PT و INR؟",
            body_html=(
                "<p><strong>زمن البروثرومبين (PT)</strong> يقيس بالثواني الوقت اللازم لتخثر البلازما "
                "بعد إضافة العامل النسيجي (الثرومبوبلاستين) والكالسيوم لعينة الدم. يقيّم أساسًا "
                "عوامل التخثر I (الفيبرينوجين)، II (البروثرومبين)، V، VII و X. تختلف نتائج PT الخام "
                "بين المختبرات بسبب اختلاف الكواشف المستخدمة.</p>"
                "<p>تم تطوير <strong>INR</strong> من قبل منظمة الصحة العالمية لتوحيد نتائج PT عالميًا. "
                "المعادلة: <em>INR = (PT المريض / PT المتوسط الطبيعي)<sup>ISI</sup></em>. بهذا، INR "
                "بقيمة 2.5 يحمل نفس المعنى بغض النظر عن المختبر.</p>"
                "<p>INR أعلى = تخثر أبطأ (خطر نزيف)؛ INR أقل = تخثر أسرع (خطر تجلط). في الممارسة "
                "السريرية، INR هو المقياس المفضل لمراقبة مضادات التخثر.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="كيف يعمل تخثر الدم",
            body_html=(
                "<p>تخثر الدم هو آلية الجسم لوقف النزيف عند تلف وعاء دموي. يشمل ثلاثة مسارات: "
                "<strong>المسار الخارجي</strong> (يبدأ بتلف الأنسجة عبر العامل VII)، "
                "<strong>المسار الداخلي</strong> (العوامل XII، XI، IX، VIII) و<strong>المسار "
                "المشترك</strong> (العامل X، V، البروثرومبين، الفيبرينوجين). يقيّم PT/INR المسارين "
                "الخارجي والمشترك تحديدًا.</p>"
                "<p>عندما يُطلق العامل النسيجي من الخلايا المتضررة، ينشط العامل VII الذي ينشط "
                "العامل X. العامل X المنشط، مع العامل V، يحوّل البروثرومبين إلى <em>ثرومبين</em>. "
                "الثرومبين يحوّل الفيبرينوجين إلى خيوط <em>فيبرين</em> تتشابك مكونة خثرة مستقرة. "
                "أي نقص في هذه العوامل يطيل PT ويرفع INR.</p>"
                "<p>فيتامين K ضروري لتخليق العوامل II، VII، IX و X والبروتينات C و S في الكبد. "
                "مضادات فيتامين K مثل الوارفارين تمنع إعادة تدوير فيتامين K، مما يقلل إنتاج هذه "
                "العوامل ويبطئ التخثر.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="المعدلات الطبيعية لـ INR و PT",
            body_html=(
                "<p>يلخص الجدول التالي نطاقات المرجعية المقبولة عمومًا.</p>"
                f'{_TBL}<thead><tr>'
                f'<th {_TH}>الحالة السريرية</th>'
                f'<th {_TH}>INR</th>'
                f'<th {_TH}>PT (ثوانٍ)</th>'
                f'</tr></thead><tbody>'
                f'<tr><td {_TD}>بدون مضادات تخثر</td>'
                f'<td {_TD}>0.8 – 1.1</td>'
                f'<td {_TD}>11 – 13.5</td></tr>'
                f'<tr><td {_TD}>وارفارين (معظم الاستطبابات)</td>'
                f'<td {_TD}>2.0 – 3.0</td>'
                f'<td {_TD}>متغير</td></tr>'
                f'<tr><td {_TD}>صمامات ميكانيكية</td>'
                f'<td {_TD}>2.5 – 3.5</td>'
                f'<td {_TD}>متغير</td></tr>'
                f'</tbody></table>'
                "<p>بدون مضادات تخثر، INR الطبيعي هو <strong>0.8–1.1</strong>. أي قيمة أعلى من 1.1 "
                "تستدعي التحقيق في مرض كبدي، نقص فيتامين K أو شذوذ عوامل التخثر.</p>"
                "<p>تحت الوارفارين، الهدف عادةً 2.0–3.0؛ للصمامات الميكانيكية 2.5–3.5. INR فوق "
                "النطاق العلاجي يزيد خطر النزيف؛ تحته يزيد خطر التجلط.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="أسباب INR المرتفع (PT المطوّل)",
            body_html=(
                "<p><strong>INR المرتفع</strong> يشير إلى أن الدم يتخثر أبطأ من الطبيعي، مما يزيد "
                "خطر النزيف. الأسباب الشائعة:</p>"
                "<p><strong>العلاج بالوارفارين:</strong> التأثير العلاجي المتوقع. الجرعة الزائدة، "
                "التفاعلات الدوائية (مضادات الالتهاب غير الستيرويدية، المضادات الحيوية، مضادات "
                "الفطريات) أو الانخفاض المفاجئ في تناول فيتامين K قد ترفع INR فوق الهدف. "
                "INR &gt; 4.0 يحمل خطر نزيف كبير؛ INR &gt; 9.0 حالة طوارئ طبية.</p>"
                "<p><strong>مرض الكبد:</strong> الكبد يصنّع معظم عوامل التخثر. التليف الكبدي، التهاب "
                "الكبد والفشل الكبدي يعطلون إنتاج العوامل ويرفعون INR. INR جزء من نقاط MELD "
                "لتحديد أولوية زراعة الكبد.</p>"
                "<p><strong>نقص فيتامين K:</strong> سوء التغذية، سوء الامتصاص (الداء البطني، كرون)، "
                "المضادات الحيوية المطولة، انسداد القنوات المرارية. <strong>التخثر المنتشر داخل "
                "الأوعية (DIC):</strong> تنشيط واستهلاك هائل لعوامل التخثر مع ارتفاع ملحوظ "
                "في INR.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="أسباب INR المنخفض",
            body_html=(
                "<p><strong>INR المنخفض</strong> يعني أن الدم يتخثر أسرع من الطبيعي، مما قد يزيد "
                "خطر التجلط. بدون مضادات تخثر، INR المنخفض نادر وغالبًا غير مهم سريريًا. تحت "
                "الوارفارين، INR أقل من الهدف يشير إلى أن مضاد التخثر غير كافٍ.</p>"
                "<p><strong>جرعة غير كافية من مضاد التخثر:</strong> يبقى المريض معرضًا لخطر تخثر "
                "الأوردة العميقة (DVT)، الانسداد الرئوي أو السكتة الدماغية الإقفارية. يجب تعديل "
                "الجرعة تحت إشراف طبي فقط.</p>"
                "<p><strong>الإفراط في تناول فيتامين K:</strong> الأطعمة الغنية بفيتامين K (الخضروات "
                "الورقية الداكنة، البروكلي) أو المكملات تعاكس تأثير الوارفارين وتخفض INR.</p>"
                "<p><strong>التفاعلات الدوائية:</strong> ريفامبيسين، كاربامازيبين، الباربيتورات، "
                "نبتة القديس يوحنا تحفز إنزيمات الكبد CYP2C9 و CYP3A4، مسرعةً أيض الوارفارين. "
                "نقل البلازما الطازجة المجمدة (FFP) يخفض INR بسرعة أيضًا.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR والعلاج بالوارفارين",
            body_html=(
                "<p>الوارفارين (كومادين) هو مضاد التخثر الفموي الأكثر وصفًا ويعمل كمضاد لفيتامين K. "
                "يُوصف للرجفان الأذيني، تخثر الأوردة العميقة، الانسداد الرئوي، الصمامات القلبية "
                "الميكانيكية والأحداث الانصمامية الخثارية المتكررة.</p>"
                "<p>في بداية العلاج، يُفحص INR كل <strong>2–3 أيام</strong> حتى الاستقرار. بعد ذلك، "
                "تُباعد الفحوصات إلى <strong>2–4 أسابيع</strong>. هدف INR يعتمد على الاستطباب: "
                "2.0–3.0 لمعظم الحالات؛ 2.5–3.5 للصمامات الميكانيكية.</p>"
                "<p>النظام الغذائي، الأدوية المصاحبة، الكحول، الأمراض الحادة وتغيرات وظائف الكبد "
                "تؤثر على استقرار INR. تثقيف المريض حول ثبات النظام الغذائي والإبلاغ المبكر عن "
                "علامات النزيف أساسيان للإدارة الناجحة. مضادات التخثر الفموية المباشرة (DOACs) لا "
                "تتطلب مراقبة INR، لكن الوارفارين يبقى المعيار للصمامات الميكانيكية.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR ووظائف الكبد",
            body_html=(
                "<p>الكبد هو العضو المركزي المسؤول عن تخليق جميع عوامل التخثر تقريبًا. لذلك، "
                "أمراض الكبد تؤثر مباشرةً على التخثر وتطيل PT/INR. على عكس ارتفاع INR الناتج "
                "عن الوارفارين، فإن الارتفاع المرتبط بمرض الكبد عادةً لا يستجيب لإعطاء "
                "فيتامين K.</p>"
                "<p>في <strong>التليف الكبدي</strong>، يرتبط INR بشدة المرض. تصنيف Child-Pugh "
                "ونقاط MELD يتضمنان INR كعامل رئيسي. في <strong>الفشل الكبدي الحاد</strong>، يرتفع "
                "INR بسرعة ويحمل قيمة تنبؤية — INR &gt; 6.5 في تسمم الباراسيتامول أحد معايير "
                "King's College للزراعة الطارئة.</p>"
                "<p>عند تقييم INR المرتفع، يأخذ الأطباء بعين الاعتبار اختبارات وظائف الكبد (ALT، "
                "AST، البيليروبين، الألبومين) إلى جانب PT/INR للتفريق بين الأسباب الكبدية "
                "والأسباب الأخرى.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى تراجع الطبيب",
            body_html=(
                "<p>استشر طبيبًا في الحالات التالية:</p>"
                "<p><strong>علامات النزيف (INR مرتفع):</strong> كدمات غير مبررة، نزيف مطول من "
                "الجروح، نزيف اللثة، الرعاف، دم في البول أو البراز، نزيف حيضي غزير، نفث الدم. "
                "<strong>علامات الطوارئ:</strong> صداع شديد مع تشوش، اضطرابات بصرية أو صعوبة "
                "في الكلام.</p>"
                "<p><strong>علامات التجلط (INR منخفض تحت الوارفارين):</strong> تورم واحمرار وألم "
                "في الساق (DVT)؛ ضيق تنفس مفاجئ وألم صدري (انسداد رئوي)؛ تدلي الوجه، ضعف "
                "الذراع أو صعوبة الكلام (سكتة دماغية). هذه الأعراض تتطلب رعاية طارئة.</p>"
                "<p>إذا كنت تتناول الوارفارين و INR خارج النطاق المستهدف، لا تعدّل الجرعة بنفسك "
                "أبدًا — اتصل بطبيبك.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya في فهم نتائجك",
            body_html=(
                "<p>ارفع تقرير تحليل الدم على <a href=\"/analyze\">Norya</a> واحصل خلال دقائق على "
                "ملخص منظم وسهل الفهم لـ INR و PT والمؤشرات الحيوية المرتبطة. تقارن Norya قيمك "
                "بالنطاقات المرجعية، تبرز الشذوذات وتنشئ تقريرًا صحيًا واضحًا للتحضير لزيارة "
                "الطبيب.</p>"
                "<p>Norya لا تشخّص ولا توصي بعلاج — هدفها ترجمة بيانات المختبر المعقدة إلى لغة "
                "بسيطة. <a href=\"/analyze\">ابدأ تحليلك الآن</a>.</p>"
            ),
        ),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html='<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. <a href="/analyze">ابدأ التحليل مع Norya</a></p>'),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_inr_sections_by_lang() -> dict:
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_inr_faq_schema_qa() -> dict:
    return {
        "tr": [
            {"question": "Normal INR değeri nedir?",
             "answer": "Antikoagülan kullanmayan kişilerde normal INR 0,8–1,1'dir. Varfarin tedavisi altındaki hastalarda terapötik hedef genellikle 2,0–3,0; mekanik kalp kapağı hastalarında 2,5–3,5'tir. Normal PT süresi 11–13,5 saniyedir."},
            {"question": "Yüksek INR ne anlama gelir?",
             "answer": "Yüksek INR, kanın normalden daha yavaş pıhtılaştığı ve kanama riskinin arttığı anlamına gelir. Yaygın nedenler arasında varfarin tedavisi, karaciğer hastalığı, K vitamini eksikliği ve DIC yer alır."},
            {"question": "Düşük INR varfarin tedavisinde ne anlama gelir?",
             "answer": "Düşük INR, kanın çok hızlı pıhtılaştığı ve antikoagülan tedavinin yetersiz kaldığı anlamına gelir. DVT, pulmoner emboli veya inme riski artabilir."},
            {"question": "Varfarin tedavisinde INR ne sıklıkla kontrol edilmelidir?",
             "answer": "Tedavi başlangıcında her 2–3 günde bir, değerler stabil olduktan sonra 2–4 haftada bir kontrol edilir."},
            {"question": "INR ile karaciğer fonksiyonu arasındaki ilişki nedir?",
             "answer": "Karaciğer pıhtılaşma faktörlerini sentezler. Siroz ve karaciğer yetmezliğinde INR yükselir ve MELD skorunun önemli bir bileşenidir."},
        ],
        "en": [
            {"question": "What is a normal INR level?",
             "answer": "Without anticoagulants: 0.8–1.1. On warfarin therapy: 2.0–3.0. Mechanical heart valves: 2.5–3.5. Normal PT: 11–13.5 seconds."},
            {"question": "What does a high INR mean?",
             "answer": "A high INR means blood takes longer to clot, increasing bleeding risk. Common causes include warfarin therapy, liver disease, vitamin K deficiency, and DIC."},
            {"question": "What does a low INR mean on warfarin?",
             "answer": "A low INR on warfarin means blood is clotting too fast and the anticoagulant is not providing adequate protection. This increases risk of DVT, pulmonary embolism, or stroke."},
            {"question": "How often should INR be checked on warfarin?",
             "answer": "Initially every 2–3 days until values stabilize, then every 2–4 weeks. More frequent testing may be needed after dose changes, new medications, or dietary changes."},
            {"question": "What is the relationship between INR and liver function?",
             "answer": "The liver synthesizes most clotting factors. In cirrhosis and liver failure, INR rises and is a key component of the MELD score used for transplant prioritization."},
        ],
        "es": [
            {"question": "¿Cuál es el nivel normal de INR?",
             "answer": "Sin anticoagulantes: 0,8–1,1. Con warfarina: 2,0–3,0. Válvulas mecánicas: 2,5–3,5. TP normal: 11–13,5 segundos."},
            {"question": "¿Qué significa un INR alto?",
             "answer": "Un INR alto indica que la sangre coagula más lentamente, aumentando el riesgo de sangrado. Causas: warfarina, enfermedad hepática, déficit de vitamina K, CID."},
            {"question": "¿Qué significa un INR bajo con warfarina?",
             "answer": "La sangre coagula demasiado rápido y la protección anticoagulante es insuficiente. Aumenta el riesgo de TVP, embolia pulmonar o ictus."},
            {"question": "¿Con qué frecuencia hay que controlar el INR bajo warfarina?",
             "answer": "Al inicio cada 2–3 días hasta estabilización, luego cada 2–4 semanas."},
        ],
        "de": [
            {"question": "Was ist ein normaler INR-Wert?",
             "answer": "Ohne Antikoagulanzien: 0,8–1,1. Unter Warfarin: 2,0–3,0. Mechanische Klappen: 2,5–3,5. Normale PT: 11–13,5 Sekunden."},
            {"question": "Was bedeutet ein hoher INR?",
             "answer": "Ein hoher INR bedeutet langsamere Gerinnung und erhöhtes Blutungsrisiko. Ursachen: Warfarin, Lebererkrankung, Vitamin-K-Mangel, DIC."},
            {"question": "Was bedeutet ein niedriger INR unter Warfarin?",
             "answer": "Das Blut gerinnt zu schnell und der Schutz vor Thrombosen ist unzureichend. Erhöhtes Risiko für TVT, Lungenembolie oder Schlaganfall."},
            {"question": "Wie oft sollte der INR unter Warfarin kontrolliert werden?",
             "answer": "Anfangs alle 2–3 Tage bis zur Stabilisierung, dann alle 2–4 Wochen."},
        ],
        "fr": [
            {"question": "Quel est le niveau normal d'INR ?",
             "answer": "Sans anticoagulant : 0,8–1,1. Sous warfarine : 2,0–3,0. Valves mécaniques : 2,5–3,5. TP normal : 11–13,5 secondes."},
            {"question": "Que signifie un INR élevé ?",
             "answer": "Le sang met plus de temps à coaguler. Causes : warfarine, maladie hépatique, carence en vitamine K ou CIVD. Risque hémorragique accru."},
            {"question": "Que signifie un INR bas sous warfarine ?",
             "answer": "Le sang coagule trop vite, la protection contre les caillots est insuffisante. Risque accru de TVP, embolie pulmonaire ou AVC."},
            {"question": "À quelle fréquence contrôler l'INR sous warfarine ?",
             "answer": "Au début tous les 2–3 jours jusqu'à stabilisation, puis toutes les 2–4 semaines."},
        ],
        "it": [
            {"question": "Qual è l'INR normale?",
             "answer": "Senza anticoagulanti: 0,8–1,1. In terapia con warfarin: 2,0–3,0. Valvole meccaniche: 2,5–3,5. PT normale: 11–13,5 secondi."},
            {"question": "Cosa significa un INR alto?",
             "answer": "Il sangue impiega più tempo a coagulare. Cause: warfarin, epatopatia, carenza di vitamina K o CID. Rischio emorragico aumentato."},
            {"question": "Cosa significa un INR basso sotto warfarin?",
             "answer": "Il sangue coagula troppo rapidamente, la protezione dai trombi è insufficiente. Aumenta il rischio di TVP, embolia polmonare o ictus."},
            {"question": "Quanto spesso va controllato l'INR sotto warfarin?",
             "answer": "All'inizio ogni 2–3 giorni fino a stabilizzazione, poi ogni 2–4 settimane."},
        ],
        "he": [
            {"question": "מהו ערך INR תקין?",
             "answer": "ללא נוגדי קרישה: 0.8–1.1. תחת וורפרין: 2.0–3.0. מסתמים מכניים: 2.5–3.5. PT תקין: 11–13.5 שניות."},
            {"question": "מה המשמעות של INR גבוה?",
             "answer": "הדם לוקח יותר זמן להיקרש. גורמים: וורפרין, מחלת כבד, חסר ויטמין K או DIC. סיכון מוגבר לדימום."},
            {"question": "מה המשמעות של INR נמוך תחת וורפרין?",
             "answer": "הדם נקרש מהר מדי והתרופה לא מגנה מספיק מפני קרישים. סיכון מוגבר ל-DVT, תסחיף ריאתי או שבץ."},
            {"question": "כמה פעמים צריך לבדוק INR תחת וורפרין?",
             "answer": "בהתחלה כל 2–3 ימים עד יציבות, אחר כך כל 2–4 שבועות."},
        ],
        "hi": [
            {"question": "सामान्य INR स्तर क्या है?",
             "answer": "एंटीकोगुलेंट के बिना: 0.8–1.1। वारफ़ारिन पर: 2.0–3.0। मैकेनिकल वाल्व: 2.5–3.5। सामान्य PT: 11–13.5 सेकंड।"},
            {"question": "उच्च INR का क्या मतलब है?",
             "answer": "रक्त को जमने में अधिक समय लगता है। कारण: वारफ़ारिन, लिवर रोग, विटामिन K की कमी या DIC। रक्तस्राव का जोखिम बढ़ता है।"},
            {"question": "वारफ़ारिन पर कम INR का क्या मतलब है?",
             "answer": "रक्त बहुत तेज़ी से जम रहा है और दवा पर्याप्त सुरक्षा नहीं दे रही। DVT, पल्मोनरी एम्बोलिज़्म या स्ट्रोक का जोखिम बढ़ता है।"},
            {"question": "वारफ़ारिन पर INR कितनी बार जाँचा जाना चाहिए?",
             "answer": "शुरू में हर 2–3 दिन स्थिर होने तक, फिर हर 2–4 सप्ताह।"},
        ],
        "ar": [
            {"question": "ما هو مستوى INR الطبيعي؟",
             "answer": "بدون مضادات تخثر: 0.8–1.1. تحت الوارفارين: 2.0–3.0. صمامات ميكانيكية: 2.5–3.5. PT طبيعي: 11–13.5 ثانية."},
            {"question": "ماذا يعني INR مرتفع؟",
             "answer": "يعني أن الدم يستغرق وقتاً أطول للتخثر. الأسباب: وارفارين، مرض كبدي، نقص فيتامين K أو DIC. يزيد خطر النزيف."},
            {"question": "ماذا يعني INR منخفض تحت الوارفارين؟",
             "answer": "الدم يتخثر بسرعة كبيرة والدواء لا يوفر حماية كافية من الجلطات. يزيد خطر DVT والانسداد الرئوي والسكتة الدماغية."},
            {"question": "كم مرة يجب فحص INR تحت الوارفارين؟",
             "answer": "في البداية كل 2–3 أيام حتى الاستقرار، ثم كل 2–4 أسابيع."},
        ],
    }
