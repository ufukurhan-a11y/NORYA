# -*- coding: utf-8 -*-
"""
PT & INR (Prothrombin Time & International Normalized Ratio) blog article — full body content for all 9 languages.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


# ─────────────────────────────────────────────────────────────────────
# TURKISH
# ─────────────────────────────────────────────────────────────────────
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="PT ve INR nedir ve neden önemlidir?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>PT (Protrombin Zamanı)</strong> ve "
                "<strong>INR (Uluslararası Normalleştirilmiş Oran)</strong> değerlerini "
                "gördüğünüzde bunların ne anlama geldiğini merak etmeniz son derece doğaldır. "
                "PT, kanınızın pıhtılaşma sürecinin belirli bir yolağını—ekstrensek yolağı—ölçen "
                "bir laboratuvar testidir. INR ise farklı laboratuvarlar ve farklı reaktifler "
                "arasında PT sonuçlarını karşılaştırılabilir hale getirmek için geliştirilen "
                "standart bir orandır. Bu iki değer birlikte, vücudunuzun kanama ve pıhtılaşma "
                "dengesini değerlendirmek için hekimler tarafından sıklıkla istenmektedir.</p>"
                "<p>Özellikle varfarin gibi kan sulandırıcı kullanan hastalar, karaciğer "
                "hastalığı şüphesi olan bireyler ve ameliyat öncesi değerlendirmelerde PT/INR "
                "testleri kritik rol oynar. Bu rehber, PT ve INR&rsquo;nin ne olduğunu, pıhtılaşma "
                "mekanizmasının nasıl çalıştığını, referans aralıklarını ve sonuçlarınızın ne "
                "anlama gelebileceğini sade bir dille anlatmayı amaçlamaktadır. Amacımız teşhis "
                "koymak değil; hekiminizle yapacağınız görüşmeye hazırlanmanıza yardımcı olmaktır.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="PT ve INR tam olarak nedir?",
            body_html=(
                "<p><strong>Protrombin Zamanı (PT)</strong>, kanınıza doku faktörü (tromboplastin) "
                "eklendikten sonra pıhtı oluşmasının kaç saniye sürdüğünü ölçen bir testtir. "
                "Pıhtılaşma kaskadının <em>ekstrensek yolağını</em> ve <em>ortak yolağı</em> "
                "değerlendirir; bu yolakta Faktör VII, Faktör X, Faktör V, Faktör II (protrombin) "
                "ve fibrinojen yer alır. PT süresi uzadığında bu faktörlerden birinde veya "
                "birkaçında eksiklik ya da işlev bozukluğu olabileceği düşünülür.</p>"
                "<p><strong>INR (International Normalized Ratio)</strong>, PT sonucunu farklı "
                "laboratuvarlar ve reaktifler arasında karşılaştırılabilir kılmak için Dünya "
                "Sağlık Örgütü tarafından tanımlanan standart bir orandır. Her laboratuvarın "
                "kullandığı tromboplastin reaktifinin hassasiyeti farklı olduğundan, ham PT "
                "değerleri laboratuvardan laboratuvara değişebilir. INR, bu farkı ortadan "
                "kaldırarak hekimlerin hastanın pıhtılaşma durumunu evrensel bir ölçekle "
                "yorumlamasına olanak tanır. Özellikle varfarin kullanan hastalarda doz "
                "ayarlaması INR değerine göre yapılır.</p>"
                "<p>Kısacası PT ham süreyi saniye olarak verir; INR ise bu süreyi standartlaştırarak "
                "laboratuvardan bağımsız bir karşılaştırma imkânı sunar. Her iki değer de "
                "tek başına tanı koydurmaz, klinik bağlamla birlikte değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Pıhtılaşma mekanizması nasıl çalışır?",
            body_html=(
                "<p>Kanın pıhtılaşması, birbiriyle zincirleme etkileşen pek çok proteinin "
                "katıldığı karmaşık bir süreçtir ve <strong>pıhtılaşma kaskadı</strong> olarak "
                "adlandırılır. Bu kaskad iki ana yolaktan oluşur: <em>intrensek (iç) yolak</em> "
                "ve <em>ekstrensek (dış) yolak</em>. İntrensek yolak, kanın kollajen gibi "
                "yüzeylerle temasıyla başlar ve Faktör XII, XI, IX, VIII aracılığıyla ilerler. "
                "Ekstrensek yolak ise doku hasarı sonucu salınan doku faktörünün Faktör VII ile "
                "birleşmesiyle başlar. Her iki yolak da <em>ortak yolakta</em> birleşerek "
                "Faktör X&rsquo;u aktifler; aktif Faktör X, Faktör V ile birlikte protrombini "
                "(Faktör II) trombine dönüştürür.</p>"
                "<p>Trombin, fibrinojeni fibrin iplikçiklerine çevirir ve bu iplikçikler ağ "
                "oluşturarak kanama bölgesinde kararlı bir pıhtı meydana getirir. Faktör XIII "
                "ise fibrin ağını çapraz bağlayarak pıhtıyı daha dayanıklı hale getirir. "
                "PT testi özellikle ekstrensek yolak ve ortak yolaktaki faktörleri (VII, X, V, "
                "II, fibrinojen) değerlendirdiği için bu aşamalardaki herhangi bir aksaklık "
                "PT süresinin uzamasına neden olur.</p>"
                "<p>Pıhtılaşma kaskadı yalnızca pıhtı oluşumu ile sınırlı değildir; aynı zamanda "
                "antikoagülan yolaklar (protein C, protein S, antitrombin) aracılığıyla pıhtılaşmanın "
                "kontrol altında tutulması da bu sistemin ayrılmaz bir parçasıdır. Denge bozulduğunda "
                "ya aşırı kanama ya da istenmeyen pıhtı (tromboz) riski ortaya çıkar.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="PT ve INR referans aralıkları",
            body_html=(
                "<p>Normal PT ve INR değerleri, bireyin antikoagülan tedavi alıp almamasına göre "
                "farklılık gösterir. Aşağıdaki tablo, yaygın olarak kabul edilen referans "
                "aralıklarını özetlemektedir:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Durum</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PT (saniye)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Sağlıklı birey (antikoagülan yok)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,8 &ndash; 1,1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Varfarin tedavisi (genel)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,0 &ndash; 3,0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mekanik kalp kapağı</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5 &ndash; 3,5</td>'
                "</tr></tbody></table>"
                "<p>Tablodaki değerler genel kabul gören aralıklardır; ancak laboratuvarlar "
                "arasında küçük farklılıklar olabilir. Antikoagülan tedavi almayan bir bireyde "
                "PT genellikle 11&ndash;13,5 saniye ve INR 0,8&ndash;1,1 arasında beklenir. "
                "Varfarin kullanan hastalarda ise hedef INR, tedavi endikasyonuna göre belirlenir: "
                "derin ven trombozu veya atriyal fibrilasyon gibi genel endikasyonlarda 2,0&ndash;3,0, "
                "mekanik kalp kapağı gibi yüksek riskli durumlarda 2,5&ndash;3,5 hedeflenir.</p>"
                "<p>INR değeri hedefe ulaşana kadar varfarin dozu titre edilir; bu süreçte "
                "düzenli kan tahlili ile takip zorunludur. INR&rsquo;nin hedefin altında kalması "
                "tromboz riskini, üstünde kalması ise kanama riskini artırır. Referans aralıkları "
                "hakkındaki nihai yorum her zaman hekiminize aittir.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="INR yüksekliğinin nedenleri",
            body_html=(
                "<p>INR değerinin beklenen aralığın üzerine çıkması, kanın normalden daha yavaş "
                "pıhtılaştığı anlamına gelir ve kanama riskini artırabilir. En sık karşılaşılan "
                "neden <strong>varfarin veya diğer antikoagülan ilaçların kullanımı</strong>dır; "
                "aşırı doz veya ilaç etkileşimleri sonucu INR hedef aralığın üzerine çıkabilir. "
                "Varfarin dışında, bazı antibiyotikler (metronidazol, flukonazol, trimetoprim-sulfametoksazol) "
                "bağırsak florasını değiştirerek K vitamini üretimini azaltır ve dolaylı yoldan "
                "INR&rsquo;yi yükseltebilir.</p>"
                "<p><strong>Karaciğer hastalıkları</strong> yüksek INR&rsquo;nin bir diğer önemli "
                "nedenidir. Karaciğer, pıhtılaşma faktörlerinin büyük çoğunluğunu (Faktör II, VII, "
                "IX, X) sentezler; siroz, hepatit veya ileri karaciğer yetmezliğinde bu faktörlerin "
                "üretimi azalır ve PT/INR yükselir. Benzer şekilde, <strong>K vitamini "
                "eksikliği</strong>—yetersiz beslenme, malabsorpsiyon sendromları veya uzun süreli "
                "antibiyotik kullanımı sonucu—da K vitaminine bağımlı faktörlerin (II, VII, IX, X) "
                "sentezini bozar.</p>"
                "<p>Daha az sık görülen nedenler arasında <strong>yaygın damar içi pıhtılaşma "
                "(DIC)</strong>, konjenital pıhtılaşma faktörü eksiklikleri ve masif kan kaybı "
                "sayılabilir. Herhangi bir açıklanamamış INR yüksekliğinde hekiminize danışmanız "
                "önemlidir; çünkü kanama riski hızla değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="INR düşüklüğünün nedenleri",
            body_html=(
                "<p>Düşük INR, kanın normalden hızlı pıhtılaştığı anlamına gelir ve özellikle "
                "antikoagülan tedavi alan hastalarda tromboz riskini artırabilir. Varfarin kullanan "
                "hastalarda INR&rsquo;nin hedef aralığın altında kalmasının en yaygın nedeni "
                "<strong>K vitamini alımının artmasıdır</strong>. Koyu yeşil yapraklı sebzeler "
                "(ıspanak, kale, brokoli) yüksek miktarda K vitamini içerir; diyetteki ani artışlar "
                "varfarinin etkisini azaltarak INR&rsquo;yi düşürebilir.</p>"
                "<p>Bazı ilaçlar da INR&rsquo;yi düşürebilir. <strong>Rifampin</strong>, karaciğerde "
                "varfarinin metabolizmasını hızlandırarak etkisini azaltır. <strong>Barbitüratlar</strong> "
                "ve bazı antiepileptik ilaçlar benzer enzim indüksiyon mekanizması ile INR&rsquo;yi "
                "düşürebilir. Ayrıca K vitamini takviyesi alan veya K vitamini içeren multivitamin "
                "kullanan bireylerde de INR hedefin altına inebilir.</p>"
                "<p>Antikoagülan kullanmayan bireylerde düşük INR genellikle klinik olarak anlamlı "
                "değildir; normal aralıktaki küçük sapmalar çoğunlukla fizyolojik varyasyon olarak "
                "değerlendirilir. Ancak tekrarlayan tromboz öyküsü veya ailede pıhtılaşma "
                "bozukluğu varsa, pıhtılaşma eğilimini artıran durumlar (trombofili) araştırılmalıdır.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR ve varfarin tedavisi",
            body_html=(
                "<p><strong>Varfarin</strong>, dünya genelinde en yaygın kullanılan oral antikoagülan "
                "ilaçlardan biridir ve etkisini K vitaminine bağımlı pıhtılaşma faktörlerinin "
                "(II, VII, IX, X) sentezini baskılayarak gösterir. Varfarinin tedavi aralığı son "
                "derece dardır; bu nedenle hastaların INR değerlerinin düzenli olarak izlenmesi "
                "zorunludur. Hedef INR, tedavi endikasyonuna bağlı olarak değişir: atriyal "
                "fibrilasyon veya derin ven trombozunda genellikle 2,0&ndash;3,0, mekanik "
                "mitral veya aort kapak protezinde 2,5&ndash;3,5 aralığı hedeflenir.</p>"
                "<p>Varfarin kullanan hastalarda INR dengesini bozan pek çok faktör bulunur. "
                "<em>Diyet</em> bunların başında gelir: K vitamini açısından zengin gıdaların "
                "(ıspanak, lahana, brokoli, yeşil çay) miktarındaki ani değişiklikler INR&rsquo;yi "
                "önemli ölçüde etkileyebilir. <em>İlaç etkileşimleri</em> de kritiktir; "
                "antibiyotikler, antifungal ilaçlar, NSAİİ&rsquo;ler ve bazı bitkisel takviyeler "
                "varfarinin etkisini artırabilir veya azaltabilir.</p>"
                "<p>Varfarin tedavisinde başarı, hasta uyumu ve düzenli INR takibine bağlıdır. "
                "Doz değişiklikleri her zaman hekim tarafından yapılmalı, hasta kendi başına "
                "doz ayarlamamalıdır. Günümüzde bazı hastalara evde kullanılabilen taşınabilir "
                "INR ölçüm cihazları (point-of-care cihazları) önerilmektedir; bu cihazlar "
                "parmak ucundan alınan bir damla kan ile hızlı sonuç verir ve takip sıklığını "
                "artırarak daha iyi doz kontrolü sağlar.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR ve karaciğer fonksiyonu",
            body_html=(
                "<p>Karaciğer, pıhtılaşma sisteminin merkezinde yer alır; çünkü pıhtılaşma "
                "faktörlerinin büyük çoğunluğu—Faktör II (protrombin), VII, IX ve X gibi K "
                "vitaminine bağımlı faktörler dahil—karaciğerde sentezlenir. Bu nedenle karaciğer "
                "hasarı doğrudan pıhtılaşma fonksiyonunu etkileyerek PT süresinin uzamasına ve "
                "INR&rsquo;nin yükselmesine neden olabilir. Klinisyenler PT/INR değerini, "
                "karaciğerin sentez kapasitesini değerlendirmek için sıklıkla kullanır.</p>"
                "<p><strong>Siroz</strong>, kronik hepatit, alkole bağlı karaciğer hastalığı "
                "ve akut karaciğer yetmezliği gibi durumlarda karaciğer hücrelerinin hasar "
                "görmesiyle pıhtılaşma faktörü üretimi azalır. Özellikle Faktör VII&rsquo;nin "
                "yarılanma ömrü diğer faktörlere kıyasla çok kısa olduğundan (yaklaşık 6 saat), "
                "akut karaciğer hasarında INR en erken yükselen göstergelerden biri olabilir. "
                "Child-Pugh ve MELD skorları gibi karaciğer hastalığı şiddet sınıflamaları, "
                "bileşenlerinden biri olarak INR&rsquo;yi kullanır.</p>"
                "<p>Karaciğer hastalığına bağlı INR yüksekliği, varfarine bağlı yükseklikten "
                "farklı bir klinik yaklaşım gerektirir. Varfarin kaynaklı yükseklikte K vitamini "
                "verilmesi etkili olabilirken, karaciğer yetmezliğine bağlı durumlarda K vitamini "
                "genellikle yetersiz kalır çünkü sorun vitaminin eksikliği değil, faktör sentez "
                "kapasitesinin azalmasıdır. Bu ayrım tedavi planlamasında büyük önem taşır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman hekime başvurmalı?",
            body_html=(
                "<p>Aşağıdaki durumlardan herhangi birinde PT/INR sonuçlarınızı bir sağlık "
                "profesyoneli ile değerlendirmeniz önerilir:</p>"
                "<ul>"
                "<li>INR değeriniz laboratuvarın referans aralığının dışında çıktıysa.</li>"
                "<li>Varfarin veya başka bir antikoagülan kullanıyor ve INR hedefinizden sapma "
                "gözlemliyorsanız.</li>"
                "<li>Açıklanamayan morluklar, diş eti kanaması, burun kanaması veya uzun süren "
                "kanamalar yaşıyorsanız.</li>"
                "<li>Koyu renkli veya kanlı dışkı ya da idrar fark ettiyseniz.</li>"
                "<li>Karaciğer hastalığı tanınız varsa ve INR değeriniz yükseliyorsa.</li>"
                "<li>Yeni bir ilaç veya takviye kullanmaya başladıysanız.</li>"
                "</ul>"
                "<p>Kanama belirtileri acil müdahale gerektirebilir. Varfarin kullanan hastalar "
                "düzenli INR takibinin önemini bilmeli ve hekim tarafından belirlenen kontrol "
                "takvimini aksatmamalıdır. Herhangi bir şüphe durumunda hekiminize danışmak "
                "her zaman en doğru adımdır.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya bu süreçte nasıl yardımcı olur?",
            body_html=(
                "<p>Norya&rsquo;da teşhis koymuyoruz; amacımız laboratuvar raporunuzu daha "
                "anlaşılır hale getirmek ve hekim randevunuza hazırlanmanızı kolaylaştırmaktır. "
                '<a href="/analyze">Analiz sayfamıza</a> kan tahlili raporunuzu yükleyerek '
                "PT, INR ve diğer tüm değerlerinizin sade dilde, referans aralıkları ve "
                "bağlamıyla açıklandığı yapılandırılmış bir sağlık özeti alabilirsiniz.</p>"
                "<p>Bu özet sayesinde hekiminize doğru soruları sorabilir, hangi değerlerin "
                "takip gerektirdiğini daha iyi anlayabilirsiniz. Birkaç dakika içinde raporunuz "
                "hazır olur ve hekim görüşmenizi çok daha verimli hale getirir. Teşhis veya "
                "tedavi önerisi vermiyoruz—sonuçlarınızı anlamanıza yardım ediyoruz.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine '
                'geçmez.</strong> Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. '
                '<a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ENGLISH
# ─────────────────────────────────────────────────────────────────────
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="What are PT and INR, and why do they matter?",
            body_html=(
                "<p>If your blood test report includes <strong>PT (Prothrombin Time)</strong> and "
                "<strong>INR (International Normalized Ratio)</strong>, you may wonder what these "
                "numbers mean and whether you should be concerned. PT measures how long it takes "
                "your blood to form a clot through the <em>extrinsic pathway</em> of coagulation. "
                "INR is a standardised ratio derived from the PT result that allows comparison "
                "across different laboratories and reagent systems. Together, they provide a "
                "snapshot of your blood&rsquo;s clotting ability and are routinely ordered before "
                "surgeries, during anticoagulant therapy, and when liver disease is suspected.</p>"
                "<p>This guide explains the science behind PT and INR, walks you through reference "
                "ranges, discusses common causes of abnormal results, and describes their role in "
                "warfarin monitoring and liver function assessment. Our goal is not to diagnose—it "
                "is to help you understand your results so you can have a more productive "
                "conversation with your doctor.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="What exactly are PT and INR?",
            body_html=(
                "<p><strong>Prothrombin Time (PT)</strong> is a laboratory test that measures how "
                "many seconds it takes for your blood plasma to clot after tissue factor "
                "(thromboplastin) is added. It evaluates the <em>extrinsic</em> and <em>common</em> "
                "pathways of the coagulation cascade, which involve Factor VII, Factor X, Factor V, "
                "Factor II (prothrombin), and fibrinogen. A prolonged PT suggests a deficiency or "
                "dysfunction in one or more of these factors.</p>"
                "<p><strong>INR (International Normalized Ratio)</strong> was introduced by the "
                "World Health Organization to standardise PT results. Because each laboratory uses "
                "a different thromboplastin reagent with a different sensitivity, raw PT values can "
                "vary from lab to lab. The INR corrects for this variation using the International "
                "Sensitivity Index (ISI) of the reagent, enabling clinicians to interpret clotting "
                "status on a universal scale. This is especially critical for patients on warfarin, "
                "whose dosing is adjusted based on INR targets.</p>"
                "<p>In short, PT gives the raw clotting time in seconds, while INR standardises "
                "that time for cross-laboratory comparability. Neither value alone is diagnostic; "
                "both must be interpreted in clinical context alongside your medical history and "
                "other test results.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="How does the coagulation cascade work?",
            body_html=(
                "<p>Blood clotting is a tightly regulated process called the <strong>coagulation "
                "cascade</strong>, involving dozens of proteins that interact in a chain-reaction "
                "fashion. Two main pathways exist: the <em>intrinsic pathway</em>, triggered when "
                "blood contacts exposed collagen or other surfaces, and the <em>extrinsic pathway</em>, "
                "initiated when tissue factor released from injured tissue binds to Factor VII. "
                "Both pathways converge at the <em>common pathway</em>, where Factor X is activated "
                "and, together with Factor V, converts prothrombin (Factor II) into thrombin.</p>"
                "<p>Thrombin then cleaves fibrinogen into fibrin strands, which form a mesh that "
                "stabilises the platelet plug at the wound site. Factor XIII cross-links the fibrin "
                "strands to create a robust, insoluble clot. The PT test specifically assesses the "
                "extrinsic and common pathways (Factors VII, X, V, II, and fibrinogen); any "
                "deficiency along these steps will prolong the PT and raise the INR.</p>"
                "<p>Importantly, the body also has natural anticoagulant mechanisms—protein C, "
                "protein S, and antithrombin—that prevent excessive clotting. The balance between "
                "pro-coagulant and anticoagulant forces is essential: a shift in either direction "
                "can lead to haemorrhage or thrombosis. Understanding this balance is key to "
                "interpreting PT and INR results.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="PT and INR reference ranges",
            body_html=(
                "<p>Normal PT and INR values differ depending on whether an individual is receiving "
                "anticoagulant therapy. The table below summarises commonly accepted ranges:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Condition</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PT (seconds)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Healthy adult (no anticoagulant)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.8 &ndash; 1.1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Warfarin therapy (general)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.0 &ndash; 3.0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mechanical heart valve</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5 &ndash; 3.5</td>'
                "</tr></tbody></table>"
                "<p>For individuals not on anticoagulants, a PT of 11&ndash;13.5 seconds and an INR "
                "of 0.8&ndash;1.1 are generally considered normal. In patients taking warfarin, the "
                "target INR depends on the clinical indication: 2.0&ndash;3.0 for conditions such "
                "as atrial fibrillation or deep vein thrombosis, and 2.5&ndash;3.5 for high-risk "
                "situations like mechanical heart valves.</p>"
                "<p>Warfarin doses are titrated until the INR reaches the target range, requiring "
                "regular blood testing. An INR below the target increases the risk of blood clots, "
                "while an INR above it increases the risk of bleeding. Reference ranges may vary "
                "slightly between laboratories, so always compare your results with the ranges "
                "printed on your specific lab report.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Causes of a high INR",
            body_html=(
                "<p>A high INR indicates that the blood is clotting more slowly than normal, which "
                "increases the risk of bleeding. The most common cause is <strong>anticoagulant "
                "medication</strong>—particularly warfarin. An excessive dose, missed monitoring, "
                "or drug interactions (e.g., with antibiotics such as metronidazole, fluconazole, "
                "or trimethoprim-sulfamethoxazole) can push the INR above the therapeutic range. "
                "Some antibiotics alter gut flora and reduce bacterial synthesis of vitamin K, "
                "indirectly raising the INR.</p>"
                "<p><strong>Liver disease</strong> is another major cause. The liver synthesises "
                "the majority of clotting factors, including the vitamin-K-dependent factors II, "
                "VII, IX, and X. Cirrhosis, hepatitis, and acute liver failure impair this synthesis, "
                "prolonging PT and elevating INR. Similarly, <strong>vitamin K deficiency</strong>—due "
                "to malnutrition, malabsorption syndromes, or prolonged antibiotic use—reduces the "
                "production of these factors.</p>"
                "<p>Less common causes include <strong>disseminated intravascular coagulation "
                "(DIC)</strong>, inherited clotting factor deficiencies (e.g., Factor VII deficiency), "
                "and massive blood loss requiring transfusion. Any unexplained rise in INR warrants "
                "prompt medical evaluation, as the bleeding risk must be assessed quickly.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Causes of a low INR",
            body_html=(
                "<p>A low INR means that the blood is clotting faster than expected. In patients on "
                "warfarin, this raises the risk of thrombosis because the anticoagulant effect is "
                "insufficient. The most common cause is <strong>increased vitamin K intake</strong>. "
                "Dark-green leafy vegetables—spinach, kale, broccoli, and Brussels sprouts—are rich "
                "in vitamin K; a sudden increase in their consumption can counteract warfarin and "
                "lower the INR.</p>"
                "<p>Certain medications also reduce the INR. <strong>Rifampin</strong> accelerates "
                "warfarin metabolism through hepatic enzyme induction, dramatically lowering its "
                "effect. <strong>Barbiturates</strong>, carbamazepine, and some other antiepileptic "
                "drugs use the same mechanism. Vitamin K supplements or multivitamins containing "
                "vitamin K can also bring the INR below the therapeutic target.</p>"
                "<p>In individuals not taking anticoagulants, a low INR is usually of little clinical "
                "significance; minor fluctuations within the normal range are considered physiological. "
                "However, if there is a personal or family history of recurrent blood clots, "
                "conditions that increase clotting tendency (thrombophilias) may need to be "
                "investigated.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR and warfarin therapy",
            body_html=(
                "<p><strong>Warfarin</strong> is one of the most widely prescribed oral "
                "anticoagulants worldwide. It works by inhibiting the synthesis of vitamin-K-dependent "
                "clotting factors (II, VII, IX, and X). Because warfarin has a very "
                "<em>narrow therapeutic window</em>, regular INR monitoring is essential. The target "
                "INR depends on the indication: typically 2.0&ndash;3.0 for atrial fibrillation or "
                "venous thromboembolism, and 2.5&ndash;3.5 for mechanical heart valves.</p>"
                "<p>Many factors can destabilise the INR in warfarin users. <em>Diet</em> is a major "
                "one: fluctuations in vitamin-K-rich foods (spinach, kale, broccoli, green tea) can "
                "shift the INR significantly. <em>Drug interactions</em> are equally important—"
                "antibiotics, antifungals, NSAIDs, and certain herbal supplements (e.g., St John&rsquo;s "
                "wort, ginkgo biloba) can potentiate or diminish warfarin&rsquo;s effect. Even "
                "changes in alcohol consumption can affect metabolism.</p>"
                "<p>Successful warfarin therapy depends on patient adherence and consistent INR "
                "monitoring. Dose adjustments should only be made by a clinician. Point-of-care "
                "INR devices that use a fingertip blood sample are now available for home testing, "
                "allowing more frequent monitoring and tighter dose control. Patients should never "
                "adjust their warfarin dose independently.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR and liver function",
            body_html=(
                "<p>The liver sits at the heart of the coagulation system. It synthesises the "
                "majority of clotting factors—including the vitamin-K-dependent factors II, VII, "
                "IX, and X—as well as fibrinogen, antithrombin, and proteins C and S. When the "
                "liver is damaged, its synthetic capacity declines, leading to prolonged PT and "
                "elevated INR. Clinicians routinely use PT/INR as a surrogate marker for the "
                "liver&rsquo;s synthetic function.</p>"
                "<p>Conditions such as <strong>cirrhosis</strong>, chronic hepatitis, alcoholic "
                "liver disease, and acute liver failure all impair clotting-factor production. "
                "Factor VII, with a half-life of only about six hours, is the first to decline in "
                "acute liver injury, making INR one of the earliest laboratory markers of "
                "deteriorating liver function. Severity scoring systems such as the Child-Pugh "
                "classification and the MELD score include INR as one of their components.</p>"
                "<p>The clinical approach to an elevated INR caused by liver disease differs from "
                "that caused by warfarin. Vitamin K administration may improve warfarin-related "
                "elevation but is often ineffective in liver failure, because the problem is not "
                "a lack of vitamin K but an inability of damaged hepatocytes to produce clotting "
                "factors. This distinction is crucial for treatment planning.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>You should discuss your PT/INR results with a healthcare professional if any "
                "of the following apply:</p>"
                "<ul>"
                "<li>Your INR falls outside the laboratory&rsquo;s reference range.</li>"
                "<li>You are on warfarin or another anticoagulant and your INR deviates from the "
                "target.</li>"
                "<li>You experience unexplained bruising, bleeding gums, nosebleeds, or prolonged "
                "bleeding from cuts.</li>"
                "<li>You notice dark or bloody stools or urine.</li>"
                "<li>You have a liver condition and your INR is rising.</li>"
                "<li>You have recently started a new medication or supplement.</li>"
                "</ul>"
                "<p>Bleeding symptoms can be a medical emergency. Patients on warfarin should "
                "understand the importance of regular INR checks and should not skip appointments. "
                "When in doubt, consulting your doctor is always the right step.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps",
            body_html=(
                "<p>At Norya we do not diagnose—our goal is to make your lab report easier to "
                "understand and help you prepare for your doctor&rsquo;s appointment. "
                '<a href="/analyze">Upload your blood test</a> to receive a structured, '
                "plain-language health summary that explains your PT, INR, and all other values "
                "with reference ranges and context, ready in just a few minutes.</p>"
                "<p>With this summary in hand, you can ask your doctor the right questions and "
                "better understand which values need follow-up. We do not offer diagnoses or "
                "treatment recommendations—we help you make sense of your results.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace '
                'medical advice or diagnosis.</strong> Always discuss your results with a '
                'healthcare professional. <a href="/analyze">Start analysis with Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# SPANISH
# ─────────────────────────────────────────────────────────────────────
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="¿Qué son el TP y el INR y por qué importan?",
            body_html=(
                "<p>Si en su análisis de sangre aparecen los valores <strong>TP (Tiempo de "
                "Protrombina)</strong> e <strong>INR (Ratio Internacional Normalizado)</strong>, "
                "es normal preguntarse qué significan. El TP mide cuánto tarda la sangre en "
                "coagularse a través de la <em>vía extrínseca</em> de la cascada de coagulación. "
                "El INR es una ratio estandarizada que permite comparar los resultados del TP "
                "entre distintos laboratorios y reactivos. Ambos valores ofrecen una imagen de "
                "la capacidad de coagulación de su sangre y se solicitan habitualmente antes de "
                "cirugías, durante tratamientos anticoagulantes y ante sospechas de enfermedad hepática.</p>"
                "<p>Esta guía explica la ciencia detrás del TP y el INR, repasa los rangos de "
                "referencia, analiza las causas más frecuentes de resultados anormales y describe "
                "su papel en la monitorización de warfarina y la evaluación de la función hepática. "
                "Nuestro objetivo no es diagnosticar, sino ayudarle a comprender sus resultados "
                "para que pueda tener una conversación más productiva con su médico.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="¿Qué son exactamente el TP y el INR?",
            body_html=(
                "<p>El <strong>Tiempo de Protrombina (TP)</strong> es una prueba de laboratorio "
                "que mide cuántos segundos tarda el plasma sanguíneo en coagularse después de "
                "añadir factor tisular (tromboplastina). Evalúa la <em>vía extrínseca</em> y "
                "la <em>vía común</em> de la cascada de coagulación, donde intervienen el "
                "Factor VII, el Factor X, el Factor V, el Factor II (protrombina) y el "
                "fibrinógeno. Un TP prolongado sugiere deficiencia o disfunción en uno o varios "
                "de estos factores.</p>"
                "<p>El <strong>INR (International Normalized Ratio)</strong> fue introducido por "
                "la Organización Mundial de la Salud para estandarizar los resultados del TP. "
                "Dado que cada laboratorio utiliza un reactivo de tromboplastina con sensibilidad "
                "diferente, los valores brutos del TP pueden variar. El INR corrige esta variación "
                "mediante el Índice de Sensibilidad Internacional (ISI), permitiendo a los "
                "médicos interpretar el estado de coagulación en una escala universal, lo que es "
                "especialmente crítico para pacientes en tratamiento con warfarina.</p>"
                "<p>En resumen, el TP da el tiempo de coagulación en segundos, mientras que el "
                "INR estandariza ese tiempo para permitir la comparación entre laboratorios. "
                "Ninguno de los dos es diagnóstico por sí solo; deben interpretarse en contexto "
                "clínico junto con la historia médica del paciente.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="¿Cómo funciona la cascada de coagulación?",
            body_html=(
                "<p>La coagulación sanguínea es un proceso regulado llamado <strong>cascada de "
                "coagulación</strong>, en el que participan decenas de proteínas que interactúan "
                "en cadena. Existen dos vías principales: la <em>vía intrínseca</em>, que se "
                "activa cuando la sangre contacta con colágeno expuesto, y la <em>vía extrínseca</em>, "
                "que se inicia cuando el factor tisular liberado por el tejido lesionado se une "
                "al Factor VII. Ambas convergen en la <em>vía común</em>, donde el Factor X "
                "activado, junto con el Factor V, convierte la protrombina (Factor II) en trombina.</p>"
                "<p>La trombina transforma el fibrinógeno en hebras de fibrina que forman una red "
                "estabilizadora del tapón plaquetario en la herida. El Factor XIII entrecruza las "
                "hebras de fibrina para crear un coágulo firme e insoluble. La prueba del TP "
                "evalúa específicamente las vías extrínseca y común (Factores VII, X, V, II y "
                "fibrinógeno); cualquier déficit en estos pasos prolongará el TP y elevará el INR.</p>"
                "<p>Además, el organismo cuenta con mecanismos anticoagulantes naturales—proteína C, "
                "proteína S y antitrombina—que impiden la coagulación excesiva. El equilibrio entre "
                "factores procoagulantes y anticoagulantes es esencial: una desviación en cualquier "
                "dirección puede provocar hemorragia o trombosis.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos de referencia del TP e INR",
            body_html=(
                "<p>Los valores normales del TP y el INR varían según si la persona está recibiendo "
                "tratamiento anticoagulante. La siguiente tabla resume los rangos generalmente "
                "aceptados:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Situación</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">TP (segundos)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Adulto sano (sin anticoagulante)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,8 &ndash; 1,1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Tratamiento con warfarina (general)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,0 &ndash; 3,0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Válvula cardíaca mecánica</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5 &ndash; 3,5</td>'
                "</tr></tbody></table>"
                "<p>En personas sin anticoagulantes, un TP de 11&ndash;13,5 segundos y un INR de "
                "0,8&ndash;1,1 se consideran normales. En pacientes con warfarina, el INR objetivo "
                "depende de la indicación: 2,0&ndash;3,0 para fibrilación auricular o trombosis "
                "venosa profunda, y 2,5&ndash;3,5 para situaciones de alto riesgo como válvulas "
                "cardíacas mecánicas.</p>"
                "<p>La dosis de warfarina se ajusta hasta alcanzar el rango objetivo de INR, lo "
                "que requiere analíticas periódicas. Un INR por debajo del objetivo aumenta el "
                "riesgo de trombosis, mientras que uno por encima eleva el riesgo de sangrado. "
                "Consulte siempre con su médico para la interpretación correcta.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Causas de un INR elevado",
            body_html=(
                "<p>Un INR elevado indica que la sangre tarda más de lo normal en coagularse, "
                "lo que aumenta el riesgo de hemorragia. La causa más frecuente es el uso de "
                "<strong>anticoagulantes</strong>, especialmente warfarina. Una sobredosis, la "
                "falta de monitorización o interacciones farmacológicas (por ejemplo, con "
                "antibióticos como metronidazol, fluconazol o trimetoprima-sulfametoxazol) "
                "pueden elevar el INR por encima del rango terapéutico. Algunos antibióticos "
                "alteran la flora intestinal y reducen la síntesis bacteriana de vitamina K, "
                "elevando indirectamente el INR.</p>"
                "<p>Las <strong>enfermedades hepáticas</strong> son otra causa importante. El "
                "hígado sintetiza la mayoría de los factores de coagulación, incluidos los "
                "dependientes de vitamina K (II, VII, IX y X). La cirrosis, la hepatitis y la "
                "insuficiencia hepática aguda comprometen esta síntesis, prolongando el TP y "
                "elevando el INR. Del mismo modo, la <strong>deficiencia de vitamina K</strong>—por "
                "malnutrición, síndromes de malabsorción o antibioticoterapia prolongada—reduce "
                "la producción de estos factores.</p>"
                "<p>Otras causas menos frecuentes incluyen la <strong>coagulación intravascular "
                "diseminada (CID)</strong>, deficiencias congénitas de factores de coagulación y "
                "hemorragias masivas. Cualquier elevación inexplicada del INR requiere evaluación "
                "médica urgente.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Causas de un INR bajo",
            body_html=(
                "<p>Un INR bajo significa que la sangre coagula más rápido de lo esperado. En "
                "pacientes anticoagulados, esto aumenta el riesgo de trombosis al ser insuficiente "
                "el efecto del fármaco. La causa más habitual es un <strong>aumento en la ingesta "
                "de vitamina K</strong>: verduras de hoja verde oscura (espinacas, col rizada, "
                "brócoli) son ricas en vitamina K, y un incremento brusco en su consumo puede "
                "contrarrestar la warfarina y reducir el INR.</p>"
                "<p>Ciertos medicamentos también disminuyen el INR. La <strong>rifampicina</strong> "
                "acelera el metabolismo de la warfarina por inducción enzimática hepática. Los "
                "<strong>barbitúricos</strong> y algunos antiepilépticos actúan mediante el mismo "
                "mecanismo. Los suplementos de vitamina K o multivitamínicos que la contengan "
                "también pueden llevar el INR por debajo del objetivo terapéutico.</p>"
                "<p>En personas sin tratamiento anticoagulante, un INR bajo rara vez es clínicamente "
                "significativo. No obstante, si existe historial personal o familiar de trombosis "
                "recurrente, se deben investigar posibles trombofilias.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR y tratamiento con warfarina",
            body_html=(
                "<p>La <strong>warfarina</strong> es uno de los anticoagulantes orales más "
                "utilizados en el mundo. Actúa inhibiendo la síntesis de los factores de "
                "coagulación dependientes de vitamina K (II, VII, IX y X). Debido a su "
                "<em>estrecha ventana terapéutica</em>, es imprescindible monitorizar el INR "
                "con regularidad. El INR objetivo varía según la indicación: generalmente "
                "2,0&ndash;3,0 para fibrilación auricular o tromboembolismo venoso, y "
                "2,5&ndash;3,5 para válvulas cardíacas mecánicas.</p>"
                "<p>Muchos factores pueden desestabilizar el INR en pacientes con warfarina. "
                "La <em>dieta</em> ocupa el primer lugar: variaciones en alimentos ricos en "
                "vitamina K (espinacas, col rizada, brócoli, té verde) pueden alterar "
                "significativamente el INR. Las <em>interacciones farmacológicas</em> también "
                "son críticas: antibióticos, antifúngicos, AINE y ciertos suplementos herbales "
                "pueden potenciar o disminuir el efecto de la warfarina.</p>"
                "<p>El éxito del tratamiento depende de la adherencia del paciente y del "
                "seguimiento constante del INR. Los ajustes de dosis deben ser realizados "
                "exclusivamente por el médico. Hoy en día existen dispositivos portátiles "
                "de medición del INR que permiten la automonitorización domiciliaria mediante "
                "una gota de sangre del dedo.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR y función hepática",
            body_html=(
                "<p>El hígado ocupa un lugar central en el sistema de coagulación, ya que "
                "sintetiza la mayoría de los factores de coagulación, incluidos los dependientes "
                "de vitamina K (II, VII, IX y X), así como el fibrinógeno, la antitrombina y "
                "las proteínas C y S. Cuando el hígado se daña, su capacidad de síntesis "
                "disminuye, lo que se refleja en un TP prolongado y un INR elevado. Los "
                "médicos utilizan habitualmente el TP/INR como marcador de la función "
                "sintética hepática.</p>"
                "<p>Enfermedades como la <strong>cirrosis</strong>, la hepatitis crónica, la "
                "enfermedad hepática alcohólica y la insuficiencia hepática aguda comprometen "
                "la producción de factores de coagulación. El Factor VII, con una vida media "
                "de aproximadamente seis horas, es el primero en descender en el daño hepático "
                "agudo, convirtiendo al INR en uno de los marcadores de laboratorio más precoces "
                "de deterioro hepático. Sistemas de clasificación como Child-Pugh y el índice "
                "MELD incluyen el INR entre sus componentes.</p>"
                "<p>El abordaje clínico de un INR elevado por enfermedad hepática difiere del "
                "causado por warfarina. La administración de vitamina K puede mejorar la "
                "elevación relacionada con warfarina, pero suele ser ineficaz en la insuficiencia "
                "hepática, ya que el problema no es la falta de vitamina K sino la incapacidad "
                "del hígado para producir factores de coagulación.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debe consultar al médico?",
            body_html=(
                "<p>Debería comentar sus resultados de TP/INR con un profesional sanitario "
                "si se da alguna de las siguientes circunstancias:</p>"
                "<ul>"
                "<li>Su INR está fuera del rango de referencia del laboratorio.</li>"
                "<li>Toma warfarina u otro anticoagulante y su INR se desvía del objetivo.</li>"
                "<li>Presenta moratones inexplicados, sangrado de encías, hemorragias nasales "
                "o sangrado prolongado por cortes.</li>"
                "<li>Observa heces oscuras o con sangre, u orina sanguinolenta.</li>"
                "<li>Tiene una enfermedad hepática y su INR está aumentando.</li>"
                "<li>Ha comenzado recientemente un nuevo medicamento o suplemento.</li>"
                "</ul>"
                "<p>Los síntomas hemorrágicos pueden constituir una urgencia médica. Los pacientes "
                "en tratamiento con warfarina deben comprender la importancia del control periódico "
                "del INR y no faltar a las citas. Ante cualquier duda, consultar al médico es "
                "siempre la decisión correcta.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo le ayuda Norya",
            body_html=(
                "<p>En Norya no diagnosticamos: nuestro objetivo es hacer que su informe de "
                "laboratorio sea más comprensible y ayudarle a prepararse para la consulta médica. "
                '<a href="/analyze">Suba su análisis de sangre</a> y reciba en pocos minutos un '
                "resumen de salud estructurado y en lenguaje claro que explica su TP, INR y el "
                "resto de valores con rangos de referencia y contexto.</p>"
                "<p>Con este resumen podrá hacer las preguntas adecuadas a su médico y comprender "
                "mejor qué valores requieren seguimiento. No ofrecemos diagnósticos ni "
                "recomendaciones de tratamiento—le ayudamos a entender sus resultados.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el '
                'diagnóstico médico.</strong> Consulte siempre sus resultados con un profesional '
                'sanitario. <a href="/analyze">Iniciar análisis con Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# GERMAN
# ─────────────────────────────────────────────────────────────────────
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Was sind PT und INR und warum sind sie wichtig?",
            body_html=(
                "<p>Wenn in Ihrem Blutbild die Werte <strong>PT (Prothrombinzeit)</strong> und "
                "<strong>INR (International Normalized Ratio)</strong> auftauchen, fragen Sie sich "
                "vielleicht, was diese Zahlen bedeuten. Die PT misst, wie lange Ihr Blut braucht, "
                "um über den <em>extrinsischen Weg</em> der Gerinnungskaskade ein Gerinnsel zu "
                "bilden. Die INR ist ein standardisiertes Verhältnis, das PT-Ergebnisse zwischen "
                "verschiedenen Laboren und Reagenzien vergleichbar macht. Beide Werte geben "
                "Aufschluss über die Gerinnungsfähigkeit Ihres Blutes und werden routinemäßig "
                "vor Operationen, während der Antikoagulanzientherapie und bei Verdacht auf "
                "Lebererkrankungen angeordnet.</p>"
                "<p>Dieser Leitfaden erklärt die Hintergründe von PT und INR, erläutert "
                "Referenzbereiche, bespricht häufige Ursachen auffälliger Ergebnisse und "
                "beschreibt ihre Rolle bei der Warfarin-Überwachung sowie der Beurteilung der "
                "Leberfunktion. Unser Ziel ist nicht die Diagnose, sondern Ihnen zu helfen, "
                "Ihre Ergebnisse zu verstehen und gut vorbereitet in das Arztgespräch zu gehen.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="Was genau sind PT und INR?",
            body_html=(
                "<p>Die <strong>Prothrombinzeit (PT)</strong> ist ein Labortest, der misst, wie "
                "viele Sekunden Ihr Blutplasma nach Zugabe von Gewebefaktor (Thromboplastin) "
                "zum Gerinnen braucht. Sie bewertet den <em>extrinsischen</em> und den "
                "<em>gemeinsamen Weg</em> der Gerinnungskaskade, an denen Faktor VII, X, V, "
                "II (Prothrombin) und Fibrinogen beteiligt sind. Eine verlängerte PT deutet "
                "auf einen Mangel oder eine Funktionsstörung eines oder mehrerer dieser "
                "Faktoren hin.</p>"
                "<p>Die <strong>INR (International Normalized Ratio)</strong> wurde von der "
                "Weltgesundheitsorganisation eingeführt, um PT-Ergebnisse zu standardisieren. "
                "Da jedes Labor ein Thromboplastin-Reagenz mit unterschiedlicher Empfindlichkeit "
                "verwendet, können die rohen PT-Werte variieren. Die INR korrigiert diese "
                "Unterschiede mithilfe des Internationalen Sensitivitätsindex (ISI), sodass "
                "Ärzte den Gerinnungsstatus auf einer universellen Skala bewerten können. "
                "Dies ist besonders wichtig für Patienten unter Warfarin-Therapie.</p>"
                "<p>Zusammengefasst: Die PT gibt die rohe Gerinnungszeit in Sekunden an, die "
                "INR standardisiert diesen Wert für die laborübergreifende Vergleichbarkeit. "
                "Keiner der beiden Werte ist allein diagnostisch; beide müssen im klinischen "
                "Kontext zusammen mit der Krankengeschichte interpretiert werden.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Wie funktioniert die Gerinnungskaskade?",
            body_html=(
                "<p>Die Blutgerinnung ist ein streng regulierter Prozess, der als "
                "<strong>Gerinnungskaskade</strong> bezeichnet wird und Dutzende von Proteinen "
                "umfasst, die kettenartig interagieren. Es gibt zwei Hauptwege: den "
                "<em>intrinsischen Weg</em>, der durch den Kontakt des Blutes mit exponiertem "
                "Kollagen ausgelöst wird, und den <em>extrinsischen Weg</em>, der beginnt, "
                "wenn Gewebefaktor aus verletztem Gewebe an Faktor VII bindet. Beide Wege "
                "münden in den <em>gemeinsamen Weg</em>, wo aktivierter Faktor X zusammen "
                "mit Faktor V Prothrombin (Faktor II) in Thrombin umwandelt.</p>"
                "<p>Thrombin spaltet Fibrinogen in Fibrinfäden, die ein Netz bilden und den "
                "Thrombozytenpfropf an der Wundstelle stabilisieren. Faktor XIII vernetzt die "
                "Fibrinfäden zu einem stabilen, unlöslichen Gerinnsel. Der PT-Test prüft "
                "gezielt den extrinsischen und gemeinsamen Weg (Faktoren VII, X, V, II und "
                "Fibrinogen); ein Mangel an einem dieser Schritte verlängert die PT und "
                "erhöht die INR.</p>"
                "<p>Gleichzeitig besitzt der Körper natürliche Antikoagulansmechanismen—Protein C, "
                "Protein S und Antithrombin—, die übermäßige Gerinnung verhindern. Das "
                "Gleichgewicht zwischen gerinnungsfördernden und gerinnungshemmenden Kräften "
                "ist entscheidend: Eine Verschiebung in eine Richtung kann zu Blutungen oder "
                "Thrombosen führen.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Referenzbereiche für PT und INR",
            body_html=(
                "<p>Die Normalwerte für PT und INR hängen davon ab, ob der Patient "
                "Antikoagulanzien einnimmt. Die folgende Tabelle fasst die allgemein "
                "anerkannten Bereiche zusammen:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Zustand</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PT (Sekunden)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Gesunder Erwachsener (ohne Antikoagulans)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,8 &ndash; 1,1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Warfarin-Therapie (allgemein)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,0 &ndash; 3,0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mechanische Herzklappe</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5 &ndash; 3,5</td>'
                "</tr></tbody></table>"
                "<p>Für Personen ohne Antikoagulanzien gilt ein PT von 11&ndash;13,5 Sekunden "
                "und eine INR von 0,8&ndash;1,1 als normal. Bei Warfarin-Patienten richtet sich "
                "der INR-Zielwert nach der Indikation: 2,0&ndash;3,0 bei Vorhofflimmern oder "
                "tiefer Venenthrombose, 2,5&ndash;3,5 bei mechanischen Herzklappen.</p>"
                "<p>Die Warfarin-Dosis wird angepasst, bis die INR im Zielbereich liegt, was "
                "regelmäßige Blutuntersuchungen erfordert. Eine INR unterhalb des Ziels erhöht "
                "das Thromboserisiko, eine INR darüber das Blutungsrisiko. Referenzbereiche "
                "können zwischen Laboren leicht variieren.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Ursachen einer erhöhten INR",
            body_html=(
                "<p>Eine erhöhte INR bedeutet, dass das Blut langsamer gerinnt als normal, was "
                "das Blutungsrisiko steigert. Die häufigste Ursache ist die Einnahme von "
                "<strong>Antikoagulanzien</strong>, insbesondere Warfarin. Überdosierung, "
                "unzureichende Überwachung oder Arzneimittelwechselwirkungen (z.&nbsp;B. mit "
                "Antibiotika wie Metronidazol, Fluconazol oder Trimethoprim-Sulfamethoxazol) "
                "können die INR über den therapeutischen Bereich heben. Manche Antibiotika "
                "verändern die Darmflora und verringern die bakterielle Vitamin-K-Synthese.</p>"
                "<p><strong>Lebererkrankungen</strong> sind eine weitere wichtige Ursache. Die "
                "Leber synthetisiert die meisten Gerinnungsfaktoren, darunter die Vitamin-K-abhängigen "
                "Faktoren II, VII, IX und X. Zirrhose, Hepatitis und akutes Leberversagen "
                "beeinträchtigen diese Synthese und verlängern die PT. Ein <strong>Vitamin-K-"
                "Mangel</strong>—durch Mangelernährung, Malabsorption oder langfristige "
                "Antibiotikatherapie—hat eine vergleichbare Wirkung.</p>"
                "<p>Seltener kommen <strong>disseminierte intravasale Gerinnung (DIC)</strong>, "
                "angeborene Gerinnungsfaktormängel und massive Blutungen als Ursachen in Frage. "
                "Jede unerklärte INR-Erhöhung sollte umgehend ärztlich abgeklärt werden.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Ursachen einer niedrigen INR",
            body_html=(
                "<p>Eine niedrige INR zeigt an, dass das Blut schneller gerinnt als erwartet. "
                "Bei Warfarin-Patienten erhöht sich dadurch das Thromboserisiko. Die häufigste "
                "Ursache ist eine <strong>erhöhte Vitamin-K-Aufnahme</strong>: dunkelgrünes "
                "Blattgemüse wie Spinat, Grünkohl und Brokkoli ist reich an Vitamin K; ein "
                "plötzlicher Anstieg des Konsums kann Warfarin entgegenwirken und die INR senken.</p>"
                "<p>Bestimmte Medikamente senken ebenfalls die INR. <strong>Rifampicin</strong> "
                "beschleunigt den Warfarin-Metabolismus durch Enzyminduktion in der Leber. "
                "<strong>Barbiturate</strong> und einige Antiepileptika wirken über denselben "
                "Mechanismus. Vitamin-K-Präparate oder Multivitamine mit Vitamin K können die "
                "INR ebenfalls unter den Zielwert drücken.</p>"
                "<p>Bei Personen ohne Antikoagulanzientherapie ist eine niedrige INR selten "
                "klinisch bedeutsam. Bei wiederkehrenden Thrombosen in der Eigen- oder "
                "Familienanamnese sollten jedoch Thrombophilien abgeklärt werden.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR und Warfarin-Therapie",
            body_html=(
                "<p><strong>Warfarin</strong> ist eines der am häufigsten verschriebenen oralen "
                "Antikoagulanzien weltweit. Es hemmt die Synthese der Vitamin-K-abhängigen "
                "Gerinnungsfaktoren (II, VII, IX und X). Wegen seiner <em>engen therapeutischen "
                "Breite</em> ist eine regelmäßige INR-Kontrolle unerlässlich. Der INR-Zielwert "
                "hängt von der Indikation ab: 2,0&ndash;3,0 bei Vorhofflimmern oder venösen "
                "Thromboembolien, 2,5&ndash;3,5 bei mechanischen Herzklappen.</p>"
                "<p>Zahlreiche Faktoren können die INR bei Warfarin-Patienten destabilisieren. "
                "Die <em>Ernährung</em> steht an erster Stelle: Schwankungen bei Vitamin-K-reichen "
                "Lebensmitteln (Spinat, Grünkohl, Brokkoli, Grüntee) können die INR erheblich "
                "verändern. <em>Arzneimittelwechselwirkungen</em> sind ebenso kritisch—Antibiotika, "
                "Antimykotika, NSAR und pflanzliche Präparate wie Johanniskraut oder Ginkgo biloba "
                "können die Warfarin-Wirkung verstärken oder abschwächen.</p>"
                "<p>Der Therapieerfolg hängt von der Therapietreue und regelmäßigen INR-Kontrollen "
                "ab. Dosisanpassungen dürfen ausschließlich durch den Arzt erfolgen. "
                "Point-of-Care-INR-Geräte für die Selbstmessung zu Hause ermöglichen häufigere "
                "Kontrollen und eine engere Dosissteuerung.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR und Leberfunktion",
            body_html=(
                "<p>Die Leber steht im Zentrum des Gerinnungssystems. Sie synthetisiert die "
                "meisten Gerinnungsfaktoren—darunter die Vitamin-K-abhängigen Faktoren II, VII, "
                "IX und X—sowie Fibrinogen, Antithrombin und die Proteine C und S. Ist die Leber "
                "geschädigt, sinkt ihre Synthesekapazität, was zu einer verlängerten PT und "
                "erhöhten INR führt. Ärzte nutzen PT/INR routinemäßig als Surrogat-Marker "
                "der hepatischen Syntheseleistung.</p>"
                "<p>Bei <strong>Zirrhose</strong>, chronischer Hepatitis, alkoholischer "
                "Lebererkrankung und akutem Leberversagen ist die Gerinnungsfaktor-Produktion "
                "beeinträchtigt. Faktor VII mit einer Halbwertszeit von nur etwa sechs Stunden "
                "fällt bei akuten Leberschäden als Erstes ab, weshalb die INR zu den frühesten "
                "Labormarkern einer sich verschlechternden Leberfunktion gehört. "
                "Bewertungssysteme wie Child-Pugh und MELD beinhalten die INR als Komponente.</p>"
                "<p>Die Behandlung einer durch Lebererkrankung verursachten INR-Erhöhung "
                "unterscheidet sich von der Warfarin-bedingten. Vitamin K kann bei "
                "Warfarin-assoziierter Erhöhung helfen, ist bei Leberversagen jedoch oft "
                "wirkungslos, da das Problem nicht im Vitaminmangel, sondern in der reduzierten "
                "Synthesekapazität der Hepatozyten liegt.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Sie sollten Ihre PT/INR-Ergebnisse mit einem Arzt besprechen, wenn eine "
                "der folgenden Situationen zutrifft:</p>"
                "<ul>"
                "<li>Ihre INR liegt außerhalb des Referenzbereichs.</li>"
                "<li>Sie nehmen Warfarin oder ein anderes Antikoagulans und die INR weicht "
                "vom Zielwert ab.</li>"
                "<li>Sie bemerken unerklärliche Blutergüsse, Zahnfleischbluten, Nasenbluten "
                "oder langanhaltende Blutungen.</li>"
                "<li>Sie beobachten dunklen oder blutigen Stuhl oder Urin.</li>"
                "<li>Sie haben eine Lebererkrankung und Ihre INR steigt.</li>"
                "<li>Sie haben kürzlich ein neues Medikament oder Nahrungsergänzungsmittel "
                "begonnen.</li>"
                "</ul>"
                "<p>Blutungssymptome können einen Notfall darstellen. Warfarin-Patienten sollten "
                "die Bedeutung regelmäßiger INR-Kontrollen verstehen und Kontrolltermine nicht "
                "versäumen. Im Zweifelsfall ist der Gang zum Arzt immer der richtige Schritt.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft",
            body_html=(
                "<p>Bei Norya stellen wir keine Diagnosen – unser Ziel ist es, Ihren Laborbefund "
                "verständlicher zu machen und Sie auf das Arztgespräch vorzubereiten. "
                '<a href="/analyze">Laden Sie Ihren Bluttest hoch</a> und erhalten Sie in wenigen '
                "Minuten eine strukturierte Gesundheitszusammenfassung in einfacher Sprache, die "
                "Ihre PT-, INR- und alle weiteren Werte mit Referenzbereichen und Kontext erklärt.</p>"
                "<p>Mit dieser Zusammenfassung können Sie Ihrem Arzt die richtigen Fragen stellen "
                "und besser verstehen, welche Werte einer Nachsorge bedürfen. Wir geben keine "
                "Diagnosen oder Therapieempfehlungen—wir helfen Ihnen, Ihre Ergebnisse zu "
                "verstehen.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche '
                'Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem '
                'Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# FRENCH
# ─────────────────────────────────────────────────────────────────────
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Qu'est-ce que le TP et l'INR, et pourquoi sont-ils importants ?",
            body_html=(
                "<p>Si votre bilan sanguin comporte les valeurs <strong>TP (Temps de "
                "Prothrombine)</strong> et <strong>INR (International Normalized Ratio)</strong>, "
                "il est normal de se demander ce qu&rsquo;elles signifient. Le TP mesure le temps "
                "que met votre sang à coaguler via la <em>voie extrinsèque</em> de la cascade "
                "de coagulation. L&rsquo;INR est un ratio standardisé qui permet de comparer les "
                "résultats du TP entre différents laboratoires et réactifs. Ensemble, ils offrent "
                "un aperçu de la capacité de coagulation de votre sang et sont prescrits en "
                "routine avant les chirurgies, pendant un traitement anticoagulant et en cas de "
                "suspicion de maladie hépatique.</p>"
                "<p>Ce guide explique la science derrière le TP et l&rsquo;INR, présente les "
                "valeurs de référence, discute les causes fréquentes de résultats anormaux et "
                "décrit leur rôle dans la surveillance de la warfarine et l&rsquo;évaluation de "
                "la fonction hépatique. Notre objectif n&rsquo;est pas de diagnostiquer, mais de "
                "vous aider à comprendre vos résultats pour en discuter efficacement avec votre "
                "médecin.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="Qu'est-ce que le TP et l'INR exactement ?",
            body_html=(
                "<p>Le <strong>Temps de Prothrombine (TP)</strong> est un test de laboratoire qui "
                "mesure en combien de secondes votre plasma sanguin coagule après ajout de facteur "
                "tissulaire (thromboplastine). Il évalue la <em>voie extrinsèque</em> et la "
                "<em>voie commune</em> de la cascade de coagulation, impliquant les Facteurs VII, "
                "X, V, II (prothrombine) et le fibrinogène. Un TP allongé suggère un déficit ou "
                "un dysfonctionnement d&rsquo;un ou plusieurs de ces facteurs.</p>"
                "<p>L&rsquo;<strong>INR (International Normalized Ratio)</strong> a été introduit "
                "par l&rsquo;Organisation mondiale de la Santé pour standardiser les résultats du "
                "TP. Chaque laboratoire utilisant un réactif de thromboplastine de sensibilité "
                "différente, les valeurs brutes du TP peuvent varier. L&rsquo;INR corrige cette "
                "variabilité grâce à l&rsquo;Indice de Sensibilité International (ISI), permettant "
                "aux cliniciens d&rsquo;interpréter le statut de coagulation sur une échelle "
                "universelle, ce qui est essentiel pour les patients sous warfarine.</p>"
                "<p>En résumé, le TP fournit le temps brut de coagulation en secondes, tandis que "
                "l&rsquo;INR le standardise pour la comparaison inter-laboratoires. Aucun des deux "
                "n&rsquo;est diagnostique seul ; ils doivent être interprétés dans le contexte "
                "clinique global.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Comment fonctionne la cascade de coagulation ?",
            body_html=(
                "<p>La coagulation sanguine est un processus finement régulé appelé <strong>cascade "
                "de coagulation</strong>, impliquant des dizaines de protéines interagissant en "
                "chaîne. Deux voies principales existent : la <em>voie intrinsèque</em>, déclenchée "
                "lorsque le sang entre en contact avec du collagène exposé, et la <em>voie "
                "extrinsèque</em>, initiée lorsque le facteur tissulaire libéré par le tissu lésé "
                "se lie au Facteur VII. Les deux convergent dans la <em>voie commune</em>, où le "
                "Facteur X activé, avec le Facteur V, convertit la prothrombine (Facteur II) en "
                "thrombine.</p>"
                "<p>La thrombine clive le fibrinogène en brins de fibrine qui forment un maillage "
                "stabilisant le clou plaquettaire au site de la blessure. Le Facteur XIII relie "
                "les brins de fibrine entre eux pour créer un caillot solide et insoluble. Le test "
                "du TP évalue spécifiquement les voies extrinsèque et commune (Facteurs VII, X, V, "
                "II et fibrinogène) ; tout déficit prolonge le TP et élève l&rsquo;INR.</p>"
                "<p>L&rsquo;organisme dispose aussi de mécanismes anticoagulants naturels—protéine C, "
                "protéine S et antithrombine—qui empêchent la coagulation excessive. L&rsquo;équilibre "
                "entre les forces procoagulantes et anticoagulantes est essentiel : un déséquilibre "
                "dans l&rsquo;un ou l&rsquo;autre sens peut provoquer une hémorragie ou une thrombose.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs de référence du TP et de l'INR",
            body_html=(
                "<p>Les valeurs normales du TP et de l&rsquo;INR varient selon que le patient "
                "reçoit ou non un traitement anticoagulant. Le tableau ci-dessous résume les "
                "plages généralement acceptées :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Situation</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">TP (secondes)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Adulte sain (sans anticoagulant)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,8 &ndash; 1,1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Traitement warfarine (général)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,0 &ndash; 3,0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Valve cardiaque mécanique</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5 &ndash; 3,5</td>'
                "</tr></tbody></table>"
                "<p>Chez les personnes sans anticoagulant, un TP de 11&ndash;13,5 secondes et un "
                "INR de 0,8&ndash;1,1 sont considérés comme normaux. Chez les patients sous "
                "warfarine, l&rsquo;INR cible dépend de l&rsquo;indication : 2,0&ndash;3,0 pour "
                "la fibrillation auriculaire ou la thrombose veineuse profonde, 2,5&ndash;3,5 pour "
                "les valves cardiaques mécaniques.</p>"
                "<p>La dose de warfarine est ajustée jusqu&rsquo;à atteindre la cible d&rsquo;INR, "
                "ce qui nécessite des prises de sang régulières. Un INR inférieur à la cible "
                "augmente le risque de thrombose, tandis qu&rsquo;un INR supérieur augmente le "
                "risque hémorragique. Consultez toujours votre médecin pour l&rsquo;interprétation.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Causes d'un INR élevé",
            body_html=(
                "<p>Un INR élevé indique que le sang coagule plus lentement que la normale, "
                "augmentant le risque de saignement. La cause la plus fréquente est le traitement "
                "par <strong>anticoagulants</strong>, en particulier la warfarine. Un surdosage, "
                "un suivi insuffisant ou des interactions médicamenteuses (par exemple avec des "
                "antibiotiques tels que le métronidazole, le fluconazole ou le triméthoprime-"
                "sulfaméthoxazole) peuvent porter l&rsquo;INR au-dessus de la zone thérapeutique. "
                "Certains antibiotiques modifient la flore intestinale et réduisent la synthèse "
                "bactérienne de vitamine K, élevant indirectement l&rsquo;INR.</p>"
                "<p>Les <strong>maladies hépatiques</strong> constituent une autre cause majeure. "
                "Le foie synthétise la plupart des facteurs de coagulation, dont les facteurs "
                "vitamine-K-dépendants (II, VII, IX et X). La cirrhose, l&rsquo;hépatite et "
                "l&rsquo;insuffisance hépatique aiguë altèrent cette synthèse, allongeant le TP "
                "et élevant l&rsquo;INR. De même, une <strong>carence en vitamine K</strong>—due "
                "à la malnutrition, à des syndromes de malabsorption ou à une antibiothérapie "
                "prolongée—réduit la production de ces facteurs.</p>"
                "<p>Des causes plus rares incluent la <strong>coagulation intravasculaire "
                "disséminée (CIVD)</strong>, les déficits congénitaux en facteurs de coagulation "
                "et les hémorragies massives. Toute élévation inexpliquée de l&rsquo;INR nécessite "
                "une évaluation médicale rapide.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Causes d'un INR bas",
            body_html=(
                "<p>Un INR bas signifie que le sang coagule plus vite que prévu. Chez les patients "
                "sous warfarine, cela augmente le risque de thrombose car l&rsquo;effet "
                "anticoagulant est insuffisant. La cause la plus fréquente est une <strong>augmentation "
                "de l&rsquo;apport en vitamine K</strong> : les légumes à feuilles vert foncé "
                "(épinards, chou frisé, brocoli) sont riches en vitamine K ; une augmentation "
                "soudaine de leur consommation peut contrecarrer la warfarine et abaisser "
                "l&rsquo;INR.</p>"
                "<p>Certains médicaments réduisent également l&rsquo;INR. La <strong>rifampicine</strong> "
                "accélère le métabolisme de la warfarine par induction enzymatique hépatique. Les "
                "<strong>barbituriques</strong> et certains antiépileptiques agissent par le même "
                "mécanisme. Les suppléments de vitamine K ou les multivitamines en contenant "
                "peuvent aussi faire chuter l&rsquo;INR sous la cible thérapeutique.</p>"
                "<p>Chez les personnes ne prenant pas d&rsquo;anticoagulants, un INR bas est "
                "rarement significatif cliniquement. Toutefois, en cas d&rsquo;antécédents "
                "personnels ou familiaux de thromboses récurrentes, des thrombophilies doivent "
                "être recherchées.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR et traitement par warfarine",
            body_html=(
                "<p>La <strong>warfarine</strong> est l&rsquo;un des anticoagulants oraux les "
                "plus prescrits au monde. Elle agit en inhibant la synthèse des facteurs de "
                "coagulation vitamine-K-dépendants (II, VII, IX et X). En raison de sa "
                "<em>fenêtre thérapeutique étroite</em>, une surveillance régulière de l&rsquo;INR "
                "est indispensable. L&rsquo;INR cible varie selon l&rsquo;indication : "
                "généralement 2,0&ndash;3,0 pour la fibrillation auriculaire ou la maladie "
                "thromboembolique veineuse, et 2,5&ndash;3,5 pour les valves cardiaques "
                "mécaniques.</p>"
                "<p>De nombreux facteurs peuvent déstabiliser l&rsquo;INR chez les patients sous "
                "warfarine. L&rsquo;<em>alimentation</em> en premier lieu : des variations dans "
                "la consommation d&rsquo;aliments riches en vitamine K (épinards, chou frisé, "
                "brocoli, thé vert) peuvent modifier significativement l&rsquo;INR. Les "
                "<em>interactions médicamenteuses</em> sont tout aussi critiques—antibiotiques, "
                "antifongiques, AINS et certains compléments à base de plantes peuvent potentialiser "
                "ou diminuer l&rsquo;effet de la warfarine.</p>"
                "<p>Le succès du traitement repose sur l&rsquo;observance du patient et un suivi "
                "régulier de l&rsquo;INR. Les ajustements posologiques doivent être effectués "
                "uniquement par le médecin. Des appareils portables de mesure de l&rsquo;INR "
                "permettent aujourd&rsquo;hui l&rsquo;autocontrôle à domicile à partir d&rsquo;une "
                "goutte de sang capillaire.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR et fonction hépatique",
            body_html=(
                "<p>Le foie est au cœur du système de coagulation. Il synthétise la majorité "
                "des facteurs de coagulation—y compris les facteurs vitamine-K-dépendants II, "
                "VII, IX et X—ainsi que le fibrinogène, l&rsquo;antithrombine et les protéines C "
                "et S. Lorsque le foie est endommagé, sa capacité de synthèse diminue, entraînant "
                "un allongement du TP et une élévation de l&rsquo;INR. Les cliniciens utilisent "
                "régulièrement le TP/INR comme marqueur de la fonction synthétique hépatique.</p>"
                "<p>Des maladies telles que la <strong>cirrhose</strong>, l&rsquo;hépatite "
                "chronique, la maladie hépatique alcoolique et l&rsquo;insuffisance hépatique "
                "aiguë altèrent la production des facteurs de coagulation. Le Facteur VII, "
                "avec une demi-vie d&rsquo;environ six heures, est le premier à chuter lors "
                "d&rsquo;une atteinte hépatique aiguë, faisant de l&rsquo;INR l&rsquo;un des "
                "marqueurs biologiques les plus précoces d&rsquo;une détérioration de la fonction "
                "hépatique. Les scores de sévérité tels que Child-Pugh et MELD intègrent "
                "l&rsquo;INR parmi leurs composants.</p>"
                "<p>L&rsquo;approche clinique d&rsquo;un INR élevé dû à une maladie hépatique "
                "diffère de celle liée à la warfarine. L&rsquo;administration de vitamine K peut "
                "corriger l&rsquo;élévation liée à la warfarine mais est souvent inefficace en cas "
                "d&rsquo;insuffisance hépatique, car le problème n&rsquo;est pas un manque de "
                "vitamine K mais l&rsquo;incapacité des hépatocytes à produire les facteurs.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Vous devriez discuter de vos résultats de TP/INR avec un professionnel de "
                "santé si l&rsquo;une des situations suivantes s&rsquo;applique :</p>"
                "<ul>"
                "<li>Votre INR se situe en dehors de la plage de référence.</li>"
                "<li>Vous prenez de la warfarine ou un autre anticoagulant et votre INR "
                "s&rsquo;écarte de la cible.</li>"
                "<li>Vous présentez des ecchymoses inexpliquées, des saignements gingivaux, "
                "des épistaxis ou des saignements prolongés.</li>"
                "<li>Vous observez des selles foncées ou sanglantes, ou du sang dans les urines.</li>"
                "<li>Vous avez une maladie du foie et votre INR augmente.</li>"
                "<li>Vous avez récemment commencé un nouveau médicament ou complément alimentaire.</li>"
                "</ul>"
                "<p>Les symptômes hémorragiques peuvent constituer une urgence médicale. Les "
                "patients sous warfarine doivent comprendre l&rsquo;importance du suivi régulier "
                "de l&rsquo;INR et ne pas manquer les rendez-vous. En cas de doute, consulter "
                "votre médecin est toujours la bonne décision.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide",
            body_html=(
                "<p>Chez Norya, nous ne posons pas de diagnostic : notre objectif est de rendre "
                "votre bilan sanguin plus compréhensible et de vous préparer à votre rendez-vous "
                'médical. <a href="/analyze">Téléchargez votre analyse de sang</a> pour recevoir '
                "en quelques minutes un résumé de santé structuré, en langage clair, expliquant "
                "votre TP, votre INR et toutes vos autres valeurs avec les plages de référence "
                "et le contexte.</p>"
                "<p>Grâce à ce résumé, vous pourrez poser les bonnes questions à votre médecin "
                "et mieux comprendre quelles valeurs nécessitent un suivi. Nous ne proposons ni "
                "diagnostic ni recommandation thérapeutique—nous vous aidons à comprendre vos "
                "résultats.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas '
                'un avis ou un diagnostic médical.</strong> Discutez toujours de vos résultats '
                "avec un professionnel de santé. "
                '<a href="/analyze">Commencer l\'analyse avec Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ITALIAN
# ─────────────────────────────────────────────────────────────────────
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Cosa sono PT e INR e perché sono importanti?",
            body_html=(
                "<p>Se nel vostro referto del sangue compaiono i valori <strong>PT (Tempo di "
                "Protrombina)</strong> e <strong>INR (International Normalized Ratio)</strong>, "
                "è naturale chiedersi cosa significhino. Il PT misura il tempo necessario al "
                "sangue per coagulare attraverso la <em>via estrinseca</em> della cascata "
                "coagulativa. L&rsquo;INR è un rapporto standardizzato che rende confrontabili "
                "i risultati del PT tra laboratori e reagenti diversi. Insieme, offrono "
                "un&rsquo;istantanea della capacità di coagulazione del sangue e vengono "
                "richiesti di routine prima degli interventi chirurgici, durante la terapia "
                "anticoagulante e in caso di sospetta malattia epatica.</p>"
                "<p>Questa guida spiega la scienza alla base di PT e INR, illustra gli intervalli "
                "di riferimento, analizza le cause più frequenti di risultati anomali e descrive "
                "il loro ruolo nel monitoraggio del warfarin e nella valutazione della funzionalità "
                "epatica. Il nostro obiettivo non è formulare diagnosi, bensì aiutarvi a "
                "comprendere i risultati per preparare al meglio il colloquio con il medico.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="Cosa sono esattamente PT e INR?",
            body_html=(
                "<p>Il <strong>Tempo di Protrombina (PT)</strong> è un test di laboratorio che "
                "misura in quanti secondi il plasma sanguigno coagula dopo l&rsquo;aggiunta di "
                "fattore tissutale (tromboplastina). Valuta la <em>via estrinseca</em> e la "
                "<em>via comune</em> della cascata coagulativa, che coinvolgono il Fattore VII, "
                "il Fattore X, il Fattore V, il Fattore II (protrombina) e il fibrinogeno. Un "
                "PT prolungato suggerisce un deficit o una disfunzione di uno o più di questi "
                "fattori.</p>"
                "<p>L&rsquo;<strong>INR (International Normalized Ratio)</strong> è stato introdotto "
                "dall&rsquo;Organizzazione Mondiale della Sanità per standardizzare i risultati "
                "del PT. Poiché ogni laboratorio utilizza un reagente di tromboplastina con "
                "sensibilità diversa, i valori grezzi del PT possono variare. L&rsquo;INR corregge "
                "questa variabilità tramite l&rsquo;Indice di Sensibilità Internazionale (ISI), "
                "consentendo ai clinici di interpretare lo stato coagulativo su una scala "
                "universale—aspetto essenziale per i pazienti in terapia con warfarin.</p>"
                "<p>In sintesi, il PT fornisce il tempo grezzo di coagulazione in secondi, mentre "
                "l&rsquo;INR lo standardizza per il confronto inter-laboratorio. Nessuno dei due "
                "è diagnostico da solo; entrambi devono essere interpretati nel contesto clinico.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="Come funziona la cascata coagulativa?",
            body_html=(
                "<p>La coagulazione del sangue è un processo strettamente regolato denominato "
                "<strong>cascata coagulativa</strong>, che coinvolge decine di proteine interagenti "
                "a catena. Esistono due vie principali: la <em>via intrinseca</em>, innescata dal "
                "contatto del sangue con collagene esposto, e la <em>via estrinseca</em>, avviata "
                "quando il fattore tissutale rilasciato dal tessuto leso si lega al Fattore VII. "
                "Entrambe convergono nella <em>via comune</em>, dove il Fattore X attivato, "
                "insieme al Fattore V, converte la protrombina (Fattore II) in trombina.</p>"
                "<p>La trombina scinde il fibrinogeno in filamenti di fibrina che formano una rete "
                "stabilizzante il tappo piastrinico nella sede della lesione. Il Fattore XIII "
                "reticola i filamenti di fibrina per creare un coagulo solido e insolubile. Il "
                "test del PT valuta specificamente le vie estrinseca e comune (Fattori VII, X, V, "
                "II e fibrinogeno); qualsiasi deficit lungo questi passaggi prolunga il PT e "
                "aumenta l&rsquo;INR.</p>"
                "<p>L&rsquo;organismo dispone anche di meccanismi anticoagulanti naturali—proteina C, "
                "proteina S e antitrombina—che prevengono la coagulazione eccessiva. L&rsquo;equilibrio "
                "tra forze procoagulanti e anticoagulanti è fondamentale: uno squilibrio in "
                "qualsiasi direzione può causare emorragia o trombosi.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Intervalli di riferimento per PT e INR",
            body_html=(
                "<p>I valori normali di PT e INR variano a seconda che il paziente sia o meno in "
                "terapia anticoagulante. La tabella seguente riassume gli intervalli comunemente "
                "accettati:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Condizione</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PT (secondi)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Adulto sano (senza anticoagulante)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13,5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0,8 &ndash; 1,1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Terapia con warfarin (generale)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,0 &ndash; 3,0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Valvola cardiaca meccanica</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2,5 &ndash; 3,5</td>'
                "</tr></tbody></table>"
                "<p>Nelle persone senza anticoagulanti, un PT di 11&ndash;13,5 secondi e un INR "
                "di 0,8&ndash;1,1 sono considerati normali. Nei pazienti in terapia con warfarin, "
                "l&rsquo;INR target dipende dall&rsquo;indicazione: 2,0&ndash;3,0 per fibrillazione "
                "atriale o trombosi venosa profonda, 2,5&ndash;3,5 per valvole cardiache meccaniche.</p>"
                "<p>La dose di warfarin viene aggiustata fino al raggiungimento dell&rsquo;INR "
                "target, richiedendo prelievi periodici. Un INR sotto il target aumenta il rischio "
                "trombotico, uno sopra il target aumenta il rischio emorragico. Confrontate sempre "
                "i risultati con gli intervalli riportati sul referto del vostro laboratorio.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="Cause di un INR elevato",
            body_html=(
                "<p>Un INR elevato indica che il sangue coagula più lentamente del normale, "
                "aumentando il rischio di emorragia. La causa più comune è l&rsquo;uso di "
                "<strong>anticoagulanti</strong>, in particolare il warfarin. Un sovradosaggio, "
                "un monitoraggio insufficiente o interazioni farmacologiche (ad esempio con "
                "antibiotici come metronidazolo, fluconazolo o trimetoprim-sulfametossazolo) "
                "possono portare l&rsquo;INR oltre l&rsquo;intervallo terapeutico. Alcuni "
                "antibiotici alterano la flora intestinale e riducono la sintesi batterica di "
                "vitamina K, innalzando indirettamente l&rsquo;INR.</p>"
                "<p>Le <strong>malattie epatiche</strong> rappresentano un&rsquo;altra causa "
                "importante. Il fegato sintetizza la maggior parte dei fattori della coagulazione, "
                "compresi quelli vitamina-K-dipendenti (II, VII, IX e X). Cirrosi, epatite e "
                "insufficienza epatica acuta compromettono questa sintesi, allungando il PT e "
                "innalzando l&rsquo;INR. Allo stesso modo, la <strong>carenza di vitamina K</strong>"
                "—dovuta a malnutrizione, sindromi da malassorbimento o terapia antibiotica "
                "prolungata—riduce la produzione di questi fattori.</p>"
                "<p>Cause meno frequenti includono la <strong>coagulazione intravascolare "
                "disseminata (CID)</strong>, deficit congeniti di fattori della coagulazione ed "
                "emorragie massive. Qualsiasi innalzamento inspiegato dell&rsquo;INR richiede "
                "una valutazione medica tempestiva.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="Cause di un INR basso",
            body_html=(
                "<p>Un INR basso significa che il sangue coagula più velocemente del previsto. "
                "Nei pazienti in terapia anticoagulante, ciò aumenta il rischio di trombosi "
                "perché l&rsquo;effetto del farmaco è insufficiente. La causa più frequente è un "
                "<strong>aumento dell&rsquo;apporto di vitamina K</strong>: verdure a foglia verde "
                "scuro (spinaci, cavolo riccio, broccoli) sono ricche di vitamina K; un aumento "
                "improvviso del loro consumo può contrastare il warfarin e abbassare l&rsquo;INR.</p>"
                "<p>Alcuni farmaci riducono anch&rsquo;essi l&rsquo;INR. La <strong>rifampicina</strong> "
                "accelera il metabolismo del warfarin attraverso l&rsquo;induzione enzimatica "
                "epatica. I <strong>barbiturici</strong> e alcuni antiepilettici agiscono con lo "
                "stesso meccanismo. Gli integratori di vitamina K o i multivitaminici che la "
                "contengono possono anch&rsquo;essi portare l&rsquo;INR sotto il target.</p>"
                "<p>Nelle persone non in terapia anticoagulante, un INR basso è raramente "
                "significativo dal punto di vista clinico. Tuttavia, in caso di storia personale "
                "o familiare di trombosi ricorrenti, devono essere indagate eventuali "
                "trombofilie.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR e terapia con warfarin",
            body_html=(
                "<p>Il <strong>warfarin</strong> è uno degli anticoagulanti orali più prescritti "
                "al mondo. Agisce inibendo la sintesi dei fattori della coagulazione vitamina-K-"
                "dipendenti (II, VII, IX e X). A causa della sua <em>stretta finestra "
                "terapeutica</em>, il monitoraggio regolare dell&rsquo;INR è essenziale. "
                "L&rsquo;INR target varia in base all&rsquo;indicazione: generalmente 2,0&ndash;3,0 "
                "per fibrillazione atriale o tromboembolismo venoso, 2,5&ndash;3,5 per valvole "
                "cardiache meccaniche.</p>"
                "<p>Numerosi fattori possono destabilizzare l&rsquo;INR nei pazienti in terapia "
                "con warfarin. La <em>dieta</em> è il primo: variazioni nel consumo di alimenti "
                "ricchi di vitamina K (spinaci, cavolo riccio, broccoli, tè verde) possono "
                "modificare significativamente l&rsquo;INR. Anche le <em>interazioni "
                "farmacologiche</em> sono critiche—antibiotici, antifungini, FANS e alcuni "
                "integratori fitoterapici possono potenziare o ridurre l&rsquo;effetto del "
                "warfarin.</p>"
                "<p>Il successo della terapia dipende dall&rsquo;aderenza del paziente e dal "
                "monitoraggio costante dell&rsquo;INR. Gli aggiustamenti posologici devono "
                "essere effettuati esclusivamente dal medico. Oggi sono disponibili dispositivi "
                "portatili per la misurazione dell&rsquo;INR che consentono l&rsquo;autocontrollo "
                "a domicilio con una goccia di sangue capillare.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR e funzionalità epatica",
            body_html=(
                "<p>Il fegato è al centro del sistema coagulativo. Sintetizza la maggior parte "
                "dei fattori della coagulazione—compresi i fattori vitamina-K-dipendenti II, VII, "
                "IX e X—nonché il fibrinogeno, l&rsquo;antitrombina e le proteine C e S. Quando "
                "il fegato è danneggiato, la sua capacità di sintesi diminuisce, con conseguente "
                "allungamento del PT e aumento dell&rsquo;INR. I clinici utilizzano abitualmente "
                "PT/INR come marcatore della funzione sintetica epatica.</p>"
                "<p>Patologie come <strong>cirrosi</strong>, epatite cronica, malattia epatica "
                "alcolica e insufficienza epatica acuta compromettono la produzione di fattori "
                "della coagulazione. Il Fattore VII, con un&rsquo;emivita di circa sei ore, è il "
                "primo a diminuire nel danno epatico acuto, rendendo l&rsquo;INR uno dei "
                "marcatori di laboratorio più precoci di deterioramento epatico. Sistemi di "
                "classificazione come Child-Pugh e MELD includono l&rsquo;INR tra i loro "
                "componenti.</p>"
                "<p>L&rsquo;approccio clinico a un INR elevato da malattia epatica differisce da "
                "quello dovuto al warfarin. La somministrazione di vitamina K può migliorare "
                "l&rsquo;elevazione correlata al warfarin, ma è spesso inefficace "
                "nell&rsquo;insufficienza epatica, poiché il problema non è la carenza di "
                "vitamina K bensì l&rsquo;incapacità degli epatociti di produrre i fattori.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Dovreste discutere i risultati di PT/INR con un professionista sanitario se "
                "si verifica una delle seguenti situazioni:</p>"
                "<ul>"
                "<li>Il vostro INR è al di fuori dell&rsquo;intervallo di riferimento.</li>"
                "<li>Assumete warfarin o un altro anticoagulante e il vostro INR si discosta "
                "dal target.</li>"
                "<li>Avete lividi inspiegabili, sanguinamento gengivale, epistassi o "
                "sanguinamento prolungato da tagli.</li>"
                "<li>Notate feci scure o ematiche oppure sangue nelle urine.</li>"
                "<li>Avete una malattia epatica e il vostro INR sta aumentando.</li>"
                "<li>Avete recentemente iniziato un nuovo farmaco o integratore.</li>"
                "</ul>"
                "<p>I sintomi emorragici possono costituire un&rsquo;emergenza medica. I pazienti "
                "in terapia con warfarin devono comprendere l&rsquo;importanza dei controlli "
                "regolari dell&rsquo;INR e non saltare gli appuntamenti. Nel dubbio, consultare "
                "il medico è sempre la scelta giusta.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya vi aiuta",
            body_html=(
                "<p>Da Norya non facciamo diagnosi: il nostro obiettivo è rendere il vostro "
                "referto di laboratorio più comprensibile e prepararvi al colloquio con il medico. "
                '<a href="/analyze">Caricate il vostro esame del sangue</a> per ricevere in pochi '
                "minuti un riassunto di salute strutturato, in linguaggio chiaro, che spiega il "
                "vostro PT, INR e tutti gli altri valori con intervalli di riferimento e contesto.</p>"
                "<p>Con questo riassunto potrete fare le domande giuste al vostro medico e "
                "capire meglio quali valori richiedono un follow-up. Non offriamo diagnosi né "
                "raccomandazioni terapeutiche—vi aiutiamo a comprendere i vostri risultati.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere '
                'o la diagnosi medica.</strong> Discutete sempre i risultati con un professionista '
                'sanitario. <a href="/analyze">Inizia l\'analisi con Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="מה הם PT ו-INR ולמה הם חשובים?",
            body_html=(
                "<p>אם בדוח בדיקת הדם שלכם מופיעים הערכים <strong>PT (זמן פרותרומבין)</strong> "
                "ו-<strong>INR (יחס בינלאומי מנורמל)</strong>, טבעי לתהות מה המשמעות שלהם. "
                "PT מודד כמה זמן לוקח לדם שלכם ליצור קריש דרך <em>המסלול החיצוני</em> "
                "של מפל הקרישה. INR הוא יחס סטנדרטי שמאפשר השוואת תוצאות PT בין מעבדות "
                "וריאגנטים שונים. יחד, הם מספקים תמונה של יכולת הקרישה של הדם ומבוקשים "
                "באופן שגרתי לפני ניתוחים, בזמן טיפול נוגד קרישה ובחשד למחלת כבד.</p>"
                "<p>מדריך זה מסביר את המדע מאחורי PT ו-INR, סוקר טווחי ייחוס, דן בגורמים "
                "השכיחים לתוצאות חריגות ומתאר את תפקידם בניטור וורפרין ובהערכת תפקודי כבד. "
                "המטרה שלנו היא לא לאבחן, אלא לעזור לכם להבין את התוצאות כדי שתגיעו מוכנים "
                "לשיחה עם הרופא.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="מה הם PT ו-INR בדיוק?",
            body_html=(
                "<p><strong>זמן פרותרומבין (PT)</strong> הוא בדיקת מעבדה המודדת תוך כמה שניות "
                "הפלזמה בדם שלכם נקרשת לאחר הוספת פקטור רקמתי (תרומבופלסטין). הבדיקה מעריכה "
                "את <em>המסלול החיצוני</em> ואת <em>המסלול המשותף</em> של מפל הקרישה, "
                "המערבים פקטור VII, פקטור X, פקטור V, פקטור II (פרותרומבין) ופיברינוגן. "
                "PT מוארך מרמז על חסר או תפקוד לקוי של אחד או יותר מגורמים אלה.</p>"
                "<p><strong>INR (International Normalized Ratio)</strong> הוכנס על ידי ארגון "
                "הבריאות העולמי כדי לתקנן תוצאות PT. מכיוון שכל מעבדה משתמשת בריאגנט "
                "תרומבופלסטין ברגישות שונה, ערכי PT גולמיים עשויים להשתנות. ה-INR מתקן "
                "שונות זו באמצעות מדד הרגישות הבינלאומי (ISI), ומאפשר לרופאים לפרש את מצב "
                "הקרישה בסולם אוניברסלי—חיוני במיוחד לחולים המטופלים בוורפרין.</p>"
                "<p>לסיכום, PT נותן את זמן הקרישה הגולמי בשניות, בעוד INR מתקנן אותו "
                "להשוואה בין-מעבדתית. אף אחד מהם אינו אבחנתי כשלעצמו; שניהם חייבים "
                "להתפרש בהקשר הקליני.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="כיצד פועל מפל הקרישה?",
            body_html=(
                "<p>קרישת הדם היא תהליך מוסדר בקפדנות הנקרא <strong>מפל הקרישה</strong>, "
                "המערב עשרות חלבונים הפועלים בתגובת שרשרת. קיימים שני מסלולים עיקריים: "
                "<em>המסלול הפנימי (אינטרינזי)</em>, המופעל כשהדם בא במגע עם קולגן חשוף, "
                "ו-<em>המסלול החיצוני (אקסטרינזי)</em>, המתחיל כשפקטור רקמתי משתחרר מרקמה "
                "פגועה ונקשר לפקטור VII. שני המסלולים מתכנסים ב-<em>מסלול המשותף</em>, שם "
                "פקטור X מופעל ויחד עם פקטור V הופך פרותרומבין (פקטור II) לתרומבין.</p>"
                "<p>תרומבין מפרק פיברינוגן לחוטי פיברין היוצרים רשת המייצבת את פקק הטסיות "
                "באתר הפציעה. פקטור XIII מקשר בין חוטי הפיברין ליצירת קריש יציב. בדיקת PT "
                "מעריכה במיוחד את המסלולים החיצוני והמשותף (פקטורים VII, X, V, II ופיברינוגן); "
                "כל חוסר בשלבים אלו מאריך את ה-PT ומעלה את ה-INR.</p>"
                "<p>לגוף יש גם מנגנונים טבעיים נוגדי קרישה—חלבון C, חלבון S ואנטיתרומבין—"
                "המונעים קרישה מוגזמת. האיזון בין כוחות מקרישים ונוגדי קרישה חיוני: הפרה "
                "לכל כיוון עלולה לגרום לדימום או לתרומבוזה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ייחוס ל-PT ו-INR",
            body_html=(
                "<p>ערכי PT ו-INR תקינים משתנים בהתאם לשאלה האם המטופל מקבל טיפול נוגד "
                "קרישה. הטבלה להלן מסכמת את הטווחים המקובלים:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">מצב</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">PT (שניות)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">מבוגר בריא (ללא נוגד קרישה)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.8 &ndash; 1.1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">טיפול בוורפרין (כללי)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.0 &ndash; 3.0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">מסתם לב מכני</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5 &ndash; 3.5</td>'
                "</tr></tbody></table>"
                "<p>באנשים ללא טיפול נוגד קרישה, PT של 11–13.5 שניות ו-INR של 0.8–1.1 "
                "נחשבים תקינים. בחולים הנוטלים וורפרין, יעד ה-INR תלוי באינדיקציה: 2.0–3.0 "
                "לפרפור פרוזדורים או פקקת ורידים עמוקים, 2.5–3.5 למסתמי לב מכניים.</p>"
                "<p>מינון הוורפרין מותאם עד שה-INR מגיע לטווח היעד, מה שדורש בדיקות דם "
                "סדירות. INR מתחת ליעד מגביר סיכון לפקקת, מעל היעד מגביר סיכון לדימום. "
                "פרשו תמיד את התוצאות ביחד עם הרופא שלכם.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="גורמים ל-INR גבוה",
            body_html=(
                "<p>INR גבוה מצביע על כך שהדם נקרש לאט יותר מהרגיל, מה שמגביר סיכון "
                "לדימום. הגורם השכיח ביותר הוא <strong>תרופות נוגדות קרישה</strong>, בעיקר "
                "וורפרין. מנת יתר, ניטור לא מספק או אינטראקציות תרופתיות (למשל עם אנטיביוטיקות "
                "כמו מטרונידזול, פלוקונזול או טרימתופרים-סולפמתוקסזול) עלולים להעלות את "
                "ה-INR מעל הטווח הטיפולי. חלק מהאנטיביוטיקות משנות את פלורת המעי ומפחיתות "
                "את ייצור ויטמין K החיידקי.</p>"
                "<p><strong>מחלות כבד</strong> הן גורם מרכזי נוסף. הכבד מסנתז את רוב גורמי "
                "הקרישה, כולל הגורמים התלויים בוויטמין K (II, VII, IX ו-X). שחמת, דלקת כבד "
                "ואי ספיקת כבד חריפה פוגעים בסינתזה זו. באופן דומה, <strong>חוסר בוויטמין "
                "K</strong>—עקב תת-תזונה, תסמונות חוסר ספיגה או טיפול אנטיביוטי ממושך—"
                "מפחית את ייצור גורמים אלה.</p>"
                "<p>גורמים פחות שכיחים כוללים <strong>קרישה תוך-כלית מפושטת (DIC)</strong>, "
                "חסרים מולדים בגורמי קרישה ואיבוד דם מסיבי. כל עלייה בלתי מוסברת ב-INR "
                "מצריכה הערכה רפואית דחופה.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="גורמים ל-INR נמוך",
            body_html=(
                "<p>INR נמוך מעיד על כך שהדם נקרש מהר יותר מהצפוי. בחולים המטופלים בוורפרין, "
                "הדבר מגביר סיכון לפקקת כיוון שהאפקט נוגד הקרישה אינו מספיק. הגורם השכיח "
                "ביותר הוא <strong>עלייה בצריכת ויטמין K</strong>: ירקות עליים ירוקים כהים "
                "(תרד, קייל, ברוקולי) עשירים בוויטמין K; עלייה פתאומית בצריכתם יכולה "
                "לנטרל את הוורפרין ולהוריד את ה-INR.</p>"
                "<p>תרופות מסוימות גם מפחיתות את ה-INR. <strong>ריפמפין</strong> מאיצה את "
                "חילוף החומרים של וורפרין באמצעות אינדוקציה אנזימטית בכבד. <strong>ברביטורטים</strong> "
                "ותרופות אנטי-אפילפטיות מסוימות פועלים באותו מנגנון. תוספי ויטמין K או "
                "מולטי-ויטמינים המכילים אותו יכולים גם להוריד את ה-INR מתחת ליעד.</p>"
                "<p>באנשים שאינם נוטלים נוגדי קרישה, INR נמוך הוא לעיתים רחוקות משמעותי "
                "קלינית. עם זאת, בנוכחות היסטוריה אישית או משפחתית של פקקות חוזרות, יש "
                "לבדוק תרומבופיליות.</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR וטיפול בוורפרין",
            body_html=(
                "<p><strong>וורפרין</strong> היא אחת מנוגדות הקרישה הפומיות הנרשמות ביותר "
                "בעולם. היא פועלת על ידי עיכוב סינתזת גורמי קרישה תלויי ויטמין K "
                "(II, VII, IX ו-X). בשל <em>חלון טיפולי צר</em>, ניטור INR סדיר הוא "
                "חיוני. יעד ה-INR משתנה לפי האינדיקציה: בדרך כלל 2.0–3.0 לפרפור "
                "פרוזדורים או תרומבואמבוליזם ורידי, ו-2.5–3.5 למסתמי לב מכניים.</p>"
                "<p>גורמים רבים יכולים לערער את יציבות ה-INR בנוטלי וורפרין. <em>תזונה</em> "
                "בראש הרשימה: שינויים בצריכת מזונות עשירים בוויטמין K (תרד, קייל, ברוקולי, "
                "תה ירוק) יכולים לשנות את ה-INR באופן משמעותי. <em>אינטראקציות תרופתיות</em> "
                "חשובות לא פחות—אנטיביוטיקות, אנטי-פטרייתיים, NSAIDs ותוספי צמחים מסוימים "
                "עשויים להגביר או להפחית את השפעת הוורפרין.</p>"
                "<p>הצלחת הטיפול תלויה בהיענות המטופל ובניטור INR עקבי. התאמות מינון צריכות "
                "להתבצע אך ורק על ידי הרופא. מכשירי INR ניידים לבדיקה עצמית ביתית מאפשרים "
                "ניטור תכוף יותר ושליטה מדויקת יותר במינון.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR ותפקוד הכבד",
            body_html=(
                "<p>הכבד נמצא במרכז מערכת הקרישה. הוא מסנתז את רוב גורמי הקרישה—כולל "
                "הגורמים התלויים בוויטמין K (II, VII, IX ו-X)—וכן פיברינוגן, אנטיתרומבין "
                "וחלבונים C ו-S. כאשר הכבד ניזוק, כושר הסינתזה שלו יורד, מה שמוביל "
                "להארכת PT ועליית INR. רופאים משתמשים ב-PT/INR באופן שגרתי כסמן ליכולת "
                "הסינתזה של הכבד.</p>"
                "<p>מצבים כמו <strong>שחמת</strong>, דלקת כבד כרונית, מחלת כבד אלכוהולית "
                "ואי ספיקת כבד חריפה פוגעים בייצור גורמי הקרישה. פקטור VII, עם זמן מחצית "
                "חיים של כשש שעות בלבד, הוא הראשון לרדת בפגיעה כבדית חריפה, מה שהופך את "
                "ה-INR לאחד מסמני המעבדה המוקדמים ביותר להידרדרות תפקוד הכבד. סולמות "
                "דירוג חומרה כמו Child-Pugh ו-MELD כוללים INR כמרכיב.</p>"
                "<p>הגישה הטיפולית ל-INR מוגבה עקב מחלת כבד שונה מזו הנגרמת על ידי "
                "וורפרין. מתן ויטמין K עשוי לשפר עלייה הקשורה לוורפרין, אך לעיתים קרובות "
                "אינו יעיל באי ספיקת כבד, מכיוון שהבעיה אינה חוסר ויטמין K אלא חוסר "
                "יכולת של תאי הכבד הפגועים לייצר גורמי קרישה.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>מומלץ לדון בתוצאות PT/INR שלכם עם גורם רפואי מוסמך אם מתקיים אחד "
                "מהמצבים הבאים:</p>"
                "<ul>"
                "<li>ה-INR שלכם מחוץ לטווח הייחוס.</li>"
                "<li>אתם נוטלים וורפרין או נוגד קרישה אחר וה-INR חורג מהיעד.</li>"
                "<li>אתם חווים חבורות בלתי מוסברות, דימום חניכיים, דימום מהאף או דימום "
                "ממושך מחתכים.</li>"
                "<li>אתם מבחינים בצואה כהה או דמית, או דם בשתן.</li>"
                "<li>יש לכם מחלת כבד וה-INR עולה.</li>"
                "<li>התחלתם לאחרונה תרופה או תוסף חדש.</li>"
                "</ul>"
                "<p>תסמיני דימום עלולים להוות מצב חירום רפואי. חולים הנוטלים וורפרין צריכים "
                "להבין את חשיבות בדיקות INR סדירות ולא לדלג על תורים. במקרה של ספק, "
                "פנייה לרופא היא תמיד הצעד הנכון.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך Norya עוזרת",
            body_html=(
                "<p>ב-Norya אנחנו לא מאבחנים—המטרה שלנו היא להפוך את דוח המעבדה שלכם "
                "למובן יותר ולעזור לכם להתכונן לפגישה עם הרופא. "
                '<a href="/analyze">העלו את בדיקת הדם שלכם</a> וקבלו תוך דקות ספורות סיכום '
                "בריאות מובנה בשפה ברורה, המסביר את ה-PT, ה-INR וכל שאר הערכים עם טווחי "
                "ייחוס והקשר.</p>"
                "<p>עם סיכום זה בידכם, תוכלו לשאול את הרופא את השאלות הנכונות ולהבין טוב "
                "יותר אילו ערכים דורשים מעקב. אנחנו לא מציעים אבחנות או המלצות טיפוליות—"
                "אנחנו עוזרים לכם להבין את התוצאות שלכם.</p>"
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


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="PT और INR क्या हैं और ये क्यों महत्वपूर्ण हैं?",
            body_html=(
                "<p>अगर आपकी ब्लड टेस्ट रिपोर्ट में <strong>PT (प्रोथ्रोम्बिन टाइम)</strong> "
                "और <strong>INR (इंटरनेशनल नॉर्मलाइज़्ड रेशियो)</strong> के मान दिखाई देते हैं, "
                "तो यह सोचना स्वाभाविक है कि इन नंबरों का क्या मतलब है। PT मापता है कि आपके "
                "खून को <em>एक्सट्रिंसिक पाथवे</em> के ज़रिये क्लॉट बनने में कितना समय लगता है। "
                "INR एक मानकीकृत अनुपात है जो अलग-अलग प्रयोगशालाओं और रिएजेंट्स में PT के "
                "परिणामों की तुलना करने योग्य बनाता है। ये दोनों मिलकर आपके रक्त की क्लॉटिंग "
                "क्षमता की तस्वीर प्रस्तुत करते हैं और सर्जरी से पहले, एंटीकोगुलेंट थेरेपी "
                "के दौरान व लिवर रोग की आशंका में नियमित रूप से माँगे जाते हैं।</p>"
                "<p>यह गाइड PT और INR के पीछे के विज्ञान को समझाती है, रेफ़रेंस रेंज बताती है, "
                "असामान्य परिणामों के सामान्य कारणों पर चर्चा करती है और वार्फ़रिन मॉनिटरिंग व "
                "लिवर फ़ंक्शन मूल्यांकन में इनकी भूमिका का वर्णन करती है। हमारा उद्देश्य "
                "निदान करना नहीं, बल्कि आपको आपके रिजल्ट समझने में मदद करना है ताकि आप "
                "डॉक्टर से बेहतर बातचीत कर सकें।</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="PT और INR वास्तव में क्या हैं?",
            body_html=(
                "<p><strong>प्रोथ्रोम्बिन टाइम (PT)</strong> एक लैब टेस्ट है जो मापता है कि "
                "टिश्यू फ़ैक्टर (थ्रोम्बोप्लास्टिन) मिलाने के बाद आपके ब्लड प्लाज़्मा को "
                "क्लॉट होने में कितनी सेकंड लगते हैं। यह कोगुलेशन कैस्केड के <em>एक्सट्रिंसिक</em> "
                "और <em>कॉमन पाथवे</em> का मूल्यांकन करता है, जिसमें फ़ैक्टर VII, X, V, "
                "II (प्रोथ्रोम्बिन) और फ़ाइब्रिनोजन शामिल हैं। लंबा PT इन फ़ैक्टर्स में "
                "से किसी एक या एक से अधिक की कमी या दोष का संकेत देता है।</p>"
                "<p><strong>INR (International Normalized Ratio)</strong> विश्व स्वास्थ्य संगठन "
                "द्वारा PT परिणामों को मानकीकृत करने के लिए लाया गया था। चूँकि हर लैब अलग "
                "संवेदनशीलता वाला थ्रोम्बोप्लास्टिन रिएजेंट इस्तेमाल करती है, कच्चे PT मान "
                "लैब दर लैब बदल सकते हैं। INR इंटरनेशनल सेंसिटिविटी इंडेक्स (ISI) का उपयोग "
                "करके इस भिन्नता को ठीक करता है, जिससे डॉक्टर एक सार्वभौमिक पैमाने पर "
                "क्लॉटिंग स्थिति की व्याख्या कर सकते हैं—यह वार्फ़रिन के मरीज़ों के लिए "
                "विशेष रूप से ज़रूरी है।</p>"
                "<p>संक्षेप में, PT कच्चा क्लॉटिंग टाइम सेकंड में देता है, जबकि INR उसे "
                "क्रॉस-लैब तुलना के लिए मानकीकृत करता है। दोनों ही अकेले डायग्नोस्टिक नहीं "
                "हैं; दोनों को क्लिनिकल संदर्भ में समझना ज़रूरी है।</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="कोगुलेशन कैस्केड कैसे काम करता है?",
            body_html=(
                "<p>रक्त का थक्का जमना एक सख्ती से नियंत्रित प्रक्रिया है जिसे "
                "<strong>कोगुलेशन कैस्केड</strong> कहते हैं, जिसमें दर्जनों प्रोटीन चेन "
                "रिएक्शन में भाग लेते हैं। दो मुख्य मार्ग हैं: <em>इंट्रिंसिक पाथवे</em>, "
                "जो रक्त के उजागर कोलेजन से संपर्क होने पर शुरू होता है, और "
                "<em>एक्सट्रिंसिक पाथवे</em>, जो घायल ऊतक से निकले टिश्यू फ़ैक्टर के "
                "फ़ैक्टर VII से बंधने पर शुरू होता है। दोनों <em>कॉमन पाथवे</em> में "
                "मिलते हैं, जहाँ सक्रिय फ़ैक्टर X, फ़ैक्टर V के साथ मिलकर प्रोथ्रोम्बिन "
                "(फ़ैक्टर II) को थ्रोम्बिन में बदलता है।</p>"
                "<p>थ्रोम्बिन फ़ाइब्रिनोजन को फ़ाइब्रिन धागों में तोड़ता है, जो एक जाल "
                "बनाकर घाव स्थल पर प्लेटलेट प्लग को स्थिर करते हैं। फ़ैक्टर XIII फ़ाइब्रिन "
                "धागों को क्रॉस-लिंक करके एक मज़बूत, अघुलनशील क्लॉट बनाता है। PT टेस्ट "
                "विशेष रूप से एक्सट्रिंसिक और कॉमन पाथवे (फ़ैक्टर VII, X, V, II, "
                "फ़ाइब्रिनोजन) का आकलन करता है; इनमें से किसी भी चरण में कमी PT को "
                "बढ़ाएगी और INR को ऊँचा करेगी।</p>"
                "<p>शरीर में प्राकृतिक एंटीकोगुलेंट तंत्र भी हैं—प्रोटीन C, प्रोटीन S "
                "और एंटीथ्रोम्बिन—जो अत्यधिक क्लॉटिंग को रोकते हैं। प्रो-कोगुलेंट और "
                "एंटीकोगुलेंट ताकतों के बीच संतुलन ज़रूरी है: किसी भी दिशा में बदलाव "
                "रक्तस्राव या थ्रोम्बोसिस का कारण बन सकता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="PT और INR के रेफ़रेंस रेंज",
            body_html=(
                "<p>सामान्य PT और INR मान इस बात पर निर्भर करते हैं कि व्यक्ति एंटीकोगुलेंट "
                "थेरेपी ले रहा है या नहीं। नीचे दी गई तालिका सामान्य रूप से स्वीकृत "
                "रेंज का सारांश देती है:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">स्थिति</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">PT (सेकंड)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">स्वस्थ वयस्क (बिना एंटीकोगुलेंट)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.8 &ndash; 1.1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">वार्फ़रिन थेरेपी (सामान्य)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.0 &ndash; 3.0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">मैकेनिकल हार्ट वॉल्व</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5 &ndash; 3.5</td>'
                "</tr></tbody></table>"
                "<p>एंटीकोगुलेंट न लेने वालों में PT 11–13.5 सेकंड और INR 0.8–1.1 सामान्य "
                "माना जाता है। वार्फ़रिन लेने वाले मरीज़ों में लक्ष्य INR इंडिकेशन पर "
                "निर्भर करता है: एट्रियल फ़िब्रिलेशन या डीप वेन थ्रोम्बोसिस के लिए "
                "2.0–3.0 और मैकेनिकल हार्ट वॉल्व के लिए 2.5–3.5।</p>"
                "<p>वार्फ़रिन की खुराक तब तक एडजस्ट की जाती है जब तक INR लक्ष्य रेंज में "
                "न आ जाए, जिसके लिए नियमित ब्लड टेस्ट ज़रूरी हैं। लक्ष्य से नीचे INR "
                "थ्रोम्बोसिस का ख़तरा बढ़ाता है, जबकि ऊपर रहने पर ब्लीडिंग का ख़तरा "
                "बढ़ता है। परिणामों की व्याख्या हमेशा अपने डॉक्टर से करें।</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="INR बढ़ने के कारण",
            body_html=(
                "<p>ऊँचा INR दर्शाता है कि खून सामान्य से धीमी गति से जम रहा है, जिससे "
                "ब्लीडिंग का ख़तरा बढ़ता है। सबसे आम कारण <strong>एंटीकोगुलेंट दवाएँ</strong> "
                "हैं, विशेषकर वार्फ़रिन। अत्यधिक खुराक, अपर्याप्त मॉनिटरिंग या ड्रग "
                "इंटरैक्शन (जैसे मेट्रोनिडाज़ोल, फ्लूकोनाज़ोल, ट्राइमेथोप्रिम-"
                "सल्फ़ामेथोक्साज़ोल जैसी एंटीबायोटिक्स) INR को थेरेप्यूटिक रेंज से ऊपर "
                "ले जा सकती हैं। कुछ एंटीबायोटिक्स आँतों के फ़्लोरा को बदलकर विटामिन K "
                "के बैक्टीरियल उत्पादन को कम करती हैं।</p>"
                "<p><strong>लिवर रोग</strong> एक अन्य प्रमुख कारण है। लिवर अधिकतर क्लॉटिंग "
                "फ़ैक्टर्स का संश्लेषण करता है, जिसमें विटामिन-K-निर्भर फ़ैक्टर II, VII, IX "
                "और X शामिल हैं। सिरोसिस, हेपेटाइटिस और एक्यूट लिवर फ़ेल्योर इस संश्लेषण "
                "को प्रभावित करते हैं। इसी तरह, <strong>विटामिन K की कमी</strong>—कुपोषण, "
                "मैलैब्सॉर्प्शन सिंड्रोम या लंबे एंटीबायोटिक उपयोग के कारण—इन फ़ैक्टर्स "
                "का उत्पादन कम करती है।</p>"
                "<p>कम सामान्य कारणों में <strong>डिसेमिनेटेड इंट्रावैस्कुलर कोगुलेशन "
                "(DIC)</strong>, जन्मजात क्लॉटिंग फ़ैक्टर की कमी और भारी रक्तस्राव शामिल "
                "हैं। किसी भी अस्पष्ट INR वृद्धि के लिए तुरंत चिकित्सा मूल्यांकन ज़रूरी है।</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="INR कम होने के कारण",
            body_html=(
                "<p>कम INR का मतलब है कि खून अपेक्षा से तेज़ जम रहा है। वार्फ़रिन लेने "
                "वालों में यह थ्रोम्बोसिस का ख़तरा बढ़ाता है क्योंकि एंटीकोगुलेंट प्रभाव "
                "अपर्याप्त है। सबसे आम कारण <strong>विटामिन K की बढ़ी हुई खपत</strong> है: "
                "गहरे हरे पत्तेदार सब्ज़ियाँ (पालक, केल, ब्रोकोली) विटामिन K से भरपूर हैं; "
                "इनकी खपत में अचानक वृद्धि वार्फ़रिन को निष्प्रभावी कर INR घटा सकती है।</p>"
                "<p>कुछ दवाएँ भी INR कम करती हैं। <strong>रिफ़ैम्पिन</strong> लिवर में एंज़ाइम "
                "इंडक्शन के ज़रिये वार्फ़रिन मेटाबॉलिज़्म को तेज़ करती है। <strong>बार्बिट्यूरेट्स</strong> "
                "और कुछ एंटी-एपिलेप्टिक दवाएँ उसी तंत्र से काम करती हैं। विटामिन K सप्लीमेंट "
                "या इसे युक्त मल्टीविटामिन भी INR को लक्ष्य से नीचे ला सकते हैं।</p>"
                "<p>एंटीकोगुलेंट न लेने वालों में कम INR शायद ही कभी चिकित्सकीय रूप से "
                "महत्वपूर्ण होता है। हालाँकि, बार-बार थ्रोम्बोसिस का व्यक्तिगत या पारिवारिक "
                "इतिहास होने पर थ्रोम्बोफ़ीलिया की जाँच ज़रूरी हो सकती है।</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR और वार्फ़रिन थेरेपी",
            body_html=(
                "<p><strong>वार्फ़रिन</strong> दुनिया भर में सबसे अधिक प्रिस्क्राइब की जाने "
                "वाली ओरल एंटीकोगुलेंट दवाओं में से एक है। यह विटामिन-K-निर्भर क्लॉटिंग "
                "फ़ैक्टर्स (II, VII, IX, X) के संश्लेषण को रोककर काम करती है। इसकी "
                "<em>संकीर्ण थेरेप्यूटिक विंडो</em> के कारण नियमित INR मॉनिटरिंग अनिवार्य "
                "है। लक्ष्य INR इंडिकेशन के अनुसार अलग होता है: आम तौर पर एट्रियल "
                "फ़िब्रिलेशन या वीनस थ्रोम्बोएम्बोलिज़्म के लिए 2.0–3.0 और मैकेनिकल "
                "हार्ट वॉल्व के लिए 2.5–3.5।</p>"
                "<p>वार्फ़रिन यूज़र्स में INR को अस्थिर करने वाले कई कारक हैं। <em>आहार</em> "
                "सबसे प्रमुख है: विटामिन K युक्त खाद्य पदार्थों (पालक, केल, ब्रोकोली, "
                "ग्रीन टी) में उतार-चढ़ाव INR को काफ़ी बदल सकते हैं। <em>ड्रग इंटरैक्शन</em> "
                "भी उतने ही महत्वपूर्ण हैं—एंटीबायोटिक्स, एंटीफंगल, NSAIDs और कुछ हर्बल "
                "सप्लीमेंट वार्फ़रिन के प्रभाव को बढ़ा या घटा सकते हैं।</p>"
                "<p>सफल वार्फ़रिन थेरेपी मरीज़ की अनुपालना और लगातार INR मॉनिटरिंग पर "
                "निर्भर करती है। खुराक में बदलाव केवल डॉक्टर द्वारा किया जाना चाहिए। "
                "पॉइंट-ऑफ़-केयर INR डिवाइस अब घर पर फ़िंगरटिप ब्लड सैंपल से टेस्ट करने "
                "की सुविधा देते हैं।</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR और लिवर फ़ंक्शन",
            body_html=(
                "<p>लिवर कोगुलेशन सिस्टम के केंद्र में है। यह अधिकांश क्लॉटिंग फ़ैक्टर्स "
                "का संश्लेषण करता है—जिसमें विटामिन-K-निर्भर फ़ैक्टर II, VII, IX और X—"
                "साथ ही फ़ाइब्रिनोजन, एंटीथ्रोम्बिन और प्रोटीन C व S शामिल हैं। जब "
                "लिवर क्षतिग्रस्त होता है तो उसकी सिंथेटिक क्षमता कम हो जाती है, जिससे "
                "PT बढ़ता है और INR ऊँचा होता है। डॉक्टर PT/INR को लिवर की सिंथेटिक "
                "फ़ंक्शन के सरोगेट मार्कर के रूप में इस्तेमाल करते हैं।</p>"
                "<p><strong>सिरोसिस</strong>, क्रॉनिक हेपेटाइटिस, अल्कोहलिक लिवर डिज़ीज़ "
                "और एक्यूट लिवर फ़ेल्योर सभी क्लॉटिंग फ़ैक्टर उत्पादन को प्रभावित करते "
                "हैं। फ़ैक्टर VII, जिसकी हाफ़-लाइफ़ केवल लगभग छह घंटे है, एक्यूट लिवर "
                "इंजरी में सबसे पहले गिरता है, जिससे INR लिवर फ़ंक्शन बिगड़ने के शुरुआती "
                "लैब मार्करों में से एक बन जाता है। Child-Pugh और MELD स्कोर INR को अपने "
                "घटकों में शामिल करते हैं।</p>"
                "<p>लिवर रोग के कारण बढ़े INR का क्लिनिकल अप्रोच वार्फ़रिन-जनित INR "
                "वृद्धि से अलग है। विटामिन K देना वार्फ़रिन-संबंधित वृद्धि में मदद कर "
                "सकता है, लेकिन लिवर फ़ेल्योर में अक्सर अप्रभावी होता है क्योंकि समस्या "
                "विटामिन K की कमी नहीं बल्कि क्षतिग्रस्त हेपैटोसाइट्स की फ़ैक्टर उत्पादन "
                "में असमर्थता है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>आपको अपने PT/INR परिणामों पर किसी स्वास्थ्य पेशेवर से चर्चा करनी चाहिए "
                "अगर निम्न में से कोई भी स्थिति लागू होती है:</p>"
                "<ul>"
                "<li>आपका INR लैब की रेफ़रेंस रेंज से बाहर है।</li>"
                "<li>आप वार्फ़रिन या कोई अन्य एंटीकोगुलेंट ले रहे हैं और INR लक्ष्य से "
                "भटक रहा है।</li>"
                "<li>आपको अस्पष्ट नील, मसूड़ों से रक्तस्राव, नाक से खून या कटने पर लंबे "
                "समय तक ब्लीडिंग हो रही है।</li>"
                "<li>आप गहरे या खूनी मल या मूत्र में रक्त देख रहे हैं।</li>"
                "<li>आपको लिवर की बीमारी है और INR बढ़ रहा है।</li>"
                "<li>आपने हाल ही में कोई नई दवा या सप्लीमेंट शुरू किया है।</li>"
                "</ul>"
                "<p>ब्लीडिंग के लक्षण मेडिकल इमरजेंसी हो सकते हैं। वार्फ़रिन लेने वाले "
                "मरीज़ों को नियमित INR जाँच का महत्व समझना चाहिए और अपॉइंटमेंट नहीं "
                "छोड़ने चाहिए। शक होने पर डॉक्टर से परामर्श हमेशा सही कदम है।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya कैसे मदद करता है",
            body_html=(
                "<p>Norya में हम निदान नहीं करते—हमारा लक्ष्य आपकी लैब रिपोर्ट को समझने में "
                "आसान बनाना और डॉक्टर की अपॉइंटमेंट के लिए आपको तैयार करना है। "
                '<a href="/analyze">अपना ब्लड टेस्ट अपलोड करें</a> और कुछ ही मिनटों में एक '
                "स्ट्रक्चर्ड, सरल भाषा में हेल्थ समरी प्राप्त करें जो आपके PT, INR और बाकी "
                "सभी वैल्यू को रेफ़रेंस रेंज और संदर्भ के साथ समझाती है।</p>"
                "<p>इस समरी के साथ आप डॉक्टर से सही सवाल पूछ सकते हैं और बेहतर समझ सकते "
                "हैं कि किन वैल्यू पर फ़ॉलो-अप ज़रूरी है। हम न तो निदान देते हैं न उपचार "
                "की सिफ़ारिश—हम आपको आपके रिज़ल्ट समझने में मदद करते हैं।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प '
                'नहीं है।</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। '
                '<a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="ما هو PT و INR ولماذا هما مهمان؟",
            body_html=(
                "<p>إذا ظهرت في تقرير فحص الدم لديك القيمتان <strong>PT (زمن البروثرومبين)</strong> "
                "و<strong>INR (النسبة المعيارية الدولية)</strong>، فمن الطبيعي أن تتساءل عن "
                "معناهما. يقيس PT المدة التي يستغرقها دمك لتكوين خثرة عبر <em>المسار الخارجي</em> "
                "لسلسلة التخثر. أما INR فهو نسبة معيارية تتيح مقارنة نتائج PT بين مختبرات "
                "وكواشف مختلفة. معاً، يقدّمان صورة عن قدرة دمك على التخثر ويُطلبان بشكل "
                "روتيني قبل الجراحات وأثناء العلاج المضاد للتخثر وعند الاشتباه بأمراض الكبد.</p>"
                "<p>يشرح هذا الدليل العلم وراء PT وINR، ويستعرض نطاقات القيم المرجعية، "
                "ويناقش الأسباب الشائعة للنتائج غير الطبيعية، ويصف دورهما في مراقبة "
                "الوارفارين وتقييم وظائف الكبد. هدفنا ليس التشخيص، بل مساعدتك على فهم "
                "نتائجك لتكون مستعداً لمناقشتها مع طبيبك.</p>"
            ),
        ),
        Section(
            id="what-is-pt-inr", level=2,
            heading="ما هو PT و INR بالتحديد؟",
            body_html=(
                "<p><strong>زمن البروثرومبين (PT)</strong> هو فحص مخبري يقيس عدد الثواني "
                "التي يستغرقها بلازما الدم للتخثر بعد إضافة العامل النسيجي (الثرومبوبلاستين). "
                "يقيّم <em>المسار الخارجي</em> و<em>المسار المشترك</em> لسلسلة التخثر، "
                "والتي تشمل العامل VII والعامل X والعامل V والعامل II (البروثرومبين) "
                "والفيبرينوجين. يشير PT المطوّل إلى نقص أو خلل في واحد أو أكثر من هذه "
                "العوامل.</p>"
                "<p>أُدخل <strong>INR (International Normalized Ratio)</strong> بواسطة منظمة "
                "الصحة العالمية لتوحيد نتائج PT. بما أن كل مختبر يستخدم كاشف ثرومبوبلاستين "
                "بحساسية مختلفة، فقد تختلف قيم PT الخام. يصحح INR هذا الاختلاف باستخدام مؤشر "
                "الحساسية الدولي (ISI)، مما يمكّن الأطباء من تفسير حالة التخثر على مقياس "
                "عالمي—وهذا بالغ الأهمية للمرضى الذين يتناولون الوارفارين.</p>"
                "<p>باختصار، يعطي PT وقت التخثر الخام بالثواني، بينما يوحّده INR للمقارنة "
                "بين المختبرات. لا يُعدّ أيّ منهما تشخيصياً بمفرده؛ بل يجب تفسيرهما في "
                "السياق السريري الكامل.</p>"
            ),
        ),
        Section(
            id="how-coagulation-works", level=2,
            heading="كيف تعمل سلسلة التخثر؟",
            body_html=(
                "<p>تخثر الدم عملية منظّمة بدقة تُعرف بـ<strong>سلسلة التخثر</strong>، "
                "وتشمل عشرات البروتينات المتفاعلة بشكل متسلسل. يوجد مساران رئيسيان: "
                "<em>المسار الداخلي</em> الذي يبدأ عند ملامسة الدم للكولاجين المكشوف، "
                "و<em>المسار الخارجي</em> الذي ينطلق عندما يرتبط العامل النسيجي المتحرر "
                "من الأنسجة المصابة بالعامل VII. يلتقي المساران في <em>المسار المشترك</em>، "
                "حيث ينشّط العامل X مع العامل V تحويل البروثرومبين (العامل II) إلى ثرومبين.</p>"
                "<p>يحوّل الثرومبين الفيبرينوجين إلى خيوط فيبرين تشكّل شبكة تثبّت سدادة "
                "الصفائح الدموية في موقع الجرح. يربط العامل XIII خيوط الفيبرين معاً لإنشاء "
                "خثرة صلبة غير قابلة للذوبان. يقيّم فحص PT تحديداً المسارين الخارجي والمشترك "
                "(العوامل VII وX وV وII والفيبرينوجين)؛ وأي نقص يطيل PT ويرفع INR.</p>"
                "<p>يمتلك الجسم أيضاً آليات طبيعية مضادة للتخثر—البروتين C والبروتين S "
                "ومضاد الثرومبين—تمنع التخثر المفرط. التوازن بين القوى المحفّزة والمضادة "
                "للتخثر ضروري: أي خلل في أي اتجاه قد يسبب نزيفاً أو تخثراً.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="النطاقات المرجعية لـ PT و INR",
            body_html=(
                "<p>تختلف قيم PT وINR الطبيعية وفقاً لما إذا كان الشخص يتلقى علاجاً مضاداً "
                "للتخثر. يلخّص الجدول أدناه النطاقات المقبولة عموماً:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الحالة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">PT (ثوانٍ)</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">INR</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">بالغ سليم (بدون مضاد تخثر)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">11 &ndash; 13.5</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">0.8 &ndash; 1.1</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">علاج بالوارفارين (عام)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.0 &ndash; 3.0</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">صمام قلب ميكانيكي</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&mdash;</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">2.5 &ndash; 3.5</td>'
                "</tr></tbody></table>"
                "<p>لدى الأشخاص غير الخاضعين لمضادات التخثر، يُعتبر PT من 11 إلى 13.5 ثانية "
                "وINR من 0.8 إلى 1.1 طبيعيين. لدى المرضى الذين يتناولون الوارفارين، يعتمد "
                "INR المستهدف على دواعي الاستعمال: 2.0–3.0 للرجفان الأذيني أو تخثر الأوردة "
                "العميقة، و2.5–3.5 لصمامات القلب الميكانيكية.</p>"
                "<p>تُعدَّل جرعة الوارفارين حتى يصل INR إلى النطاق المستهدف، مما يتطلب "
                "فحوصات دم دورية. INR دون المستهدف يزيد خطر التخثر، وفوق المستهدف يزيد "
                "خطر النزيف. استشر طبيبك دائماً لتفسير النتائج.</p>"
            ),
        ),
        Section(
            id="high-inr-causes", level=2,
            heading="أسباب ارتفاع INR",
            body_html=(
                "<p>يشير INR المرتفع إلى أن الدم يتخثر أبطأ من الطبيعي، مما يزيد خطر "
                "النزيف. السبب الأكثر شيوعاً هو <strong>أدوية مضادات التخثر</strong>، وخاصة "
                "الوارفارين. الجرعة الزائدة أو المراقبة غير الكافية أو التداخلات الدوائية "
                "(مثل المضادات الحيوية كالميترونيدازول والفلوكونازول والتريميثوبريم-"
                "سلفاميثوكسازول) قد ترفع INR فوق النطاق العلاجي. بعض المضادات الحيوية "
                "تغيّر فلورا الأمعاء وتقلل إنتاج فيتامين K البكتيري.</p>"
                "<p><strong>أمراض الكبد</strong> سبب رئيسي آخر. يُنتج الكبد معظم عوامل "
                "التخثر، بما فيها العوامل المعتمدة على فيتامين K (II وVII وIX وX). يؤدي "
                "تليّف الكبد والتهاب الكبد والفشل الكبدي الحاد إلى إضعاف هذا الإنتاج. "
                "وبالمثل، فإن <strong>نقص فيتامين K</strong>—بسبب سوء التغذية أو متلازمات "
                "سوء الامتصاص أو العلاج الطويل بالمضادات الحيوية—يقلل إنتاج هذه العوامل.</p>"
                "<p>تشمل الأسباب الأقل شيوعاً <strong>التخثر المنتشر داخل الأوعية "
                "(DIC)</strong>، والنقص الخلقي في عوامل التخثر، والنزيف الكثيف. أي ارتفاع "
                "غير مفسّر في INR يستوجب تقييماً طبياً عاجلاً.</p>"
            ),
        ),
        Section(
            id="low-inr-causes", level=2,
            heading="أسباب انخفاض INR",
            body_html=(
                "<p>يعني INR المنخفض أن الدم يتخثر أسرع من المتوقع. لدى المرضى الذين "
                "يتناولون الوارفارين، يزيد ذلك خطر التخثر لأن التأثير المضاد للتخثر "
                "غير كافٍ. السبب الأكثر شيوعاً هو <strong>زيادة تناول فيتامين K</strong>: "
                "الخضروات الورقية الداكنة (السبانخ والكرنب الأجعد والبروكلي) غنية بفيتامين K؛ "
                "والزيادة المفاجئة في استهلاكها قد تعاكس الوارفارين وتخفض INR.</p>"
                "<p>بعض الأدوية تخفض INR أيضاً. يُسرّع <strong>الريفامبيسين</strong> استقلاب "
                "الوارفارين من خلال تحريض الإنزيمات الكبدية. تعمل <strong>الباربيتورات</strong> "
                "وبعض مضادات الصرع بالآلية ذاتها. مكملات فيتامين K أو الفيتامينات المتعددة "
                "التي تحتويه يمكن أن تخفض INR أيضاً دون المستهدف.</p>"
                "<p>لدى الأشخاص الذين لا يتناولون مضادات التخثر، نادراً ما يكون INR المنخفض "
                "ذا أهمية سريرية. ومع ذلك، في حال وجود تاريخ شخصي أو عائلي لتخثرات "
                "متكررة، ينبغي البحث عن أهبات التخثر (الثرومبوفيليا).</p>"
            ),
        ),
        Section(
            id="inr-and-warfarin", level=2,
            heading="INR والعلاج بالوارفارين",
            body_html=(
                "<p><strong>الوارفارين</strong> من أكثر مضادات التخثر الفموية وصفاً في العالم. "
                "يعمل عن طريق تثبيط تصنيع عوامل التخثر المعتمدة على فيتامين K (II وVII وIX "
                "وX). نظراً لـ<em>نافذته العلاجية الضيقة</em>، فإن مراقبة INR المنتظمة "
                "ضرورية. يختلف INR المستهدف وفقاً لدواعي الاستعمال: عادةً 2.0–3.0 للرجفان "
                "الأذيني أو الانصمام الخثاري الوريدي، و2.5–3.5 لصمامات القلب الميكانيكية.</p>"
                "<p>عوامل كثيرة قد تزعزع استقرار INR لدى مستخدمي الوارفارين. <em>النظام "
                "الغذائي</em> في المقدمة: تقلبات في تناول الأطعمة الغنية بفيتامين K (السبانخ، "
                "الكرنب الأجعد، البروكلي، الشاي الأخضر) يمكن أن تغيّر INR بشكل ملحوظ. "
                "<em>التداخلات الدوائية</em> لا تقل أهمية—المضادات الحيوية ومضادات الفطريات "
                "ومضادات الالتهاب غير الستيرويدية وبعض المكملات العشبية قد تعزز أو تضعف "
                "تأثير الوارفارين.</p>"
                "<p>يعتمد نجاح العلاج على التزام المريض والمراقبة المنتظمة لـ INR. يجب أن "
                "يُجري الطبيب وحده تعديلات الجرعة. أجهزة INR المحمولة للفحص الذاتي في "
                "المنزل تتيح مراقبة أكثر تواتراً وتحكماً أدق في الجرعة.</p>"
            ),
        ),
        Section(
            id="inr-and-liver", level=2,
            heading="INR ووظائف الكبد",
            body_html=(
                "<p>يقع الكبد في صميم جهاز التخثر. فهو يصنّع غالبية عوامل التخثر—بما فيها "
                "العوامل المعتمدة على فيتامين K (II وVII وIX وX)—فضلاً عن الفيبرينوجين "
                "ومضاد الثرومبين والبروتينين C وS. عندما يتضرر الكبد تنخفض قدرته التصنيعية، "
                "مما يؤدي إلى إطالة PT وارتفاع INR. يستخدم الأطباء PT/INR بشكل روتيني "
                "كمؤشر بديل لوظيفة الكبد التصنيعية.</p>"
                "<p>أمراض مثل <strong>التليف الكبدي</strong> والتهاب الكبد المزمن ومرض الكبد "
                "الكحولي والفشل الكبدي الحاد تُضعف إنتاج عوامل التخثر. العامل VII، بعمر "
                "نصفي يبلغ نحو ست ساعات فقط، هو أول ما ينخفض في إصابة الكبد الحادة، مما "
                "يجعل INR من أبكر المؤشرات المخبرية لتدهور وظائف الكبد. تتضمن أنظمة تصنيف "
                "الشدة مثل Child-Pugh وMELD قيمة INR ضمن مكوناتها.</p>"
                "<p>يختلف النهج السريري لارتفاع INR الناجم عن مرض الكبد عن ذلك الناجم عن "
                "الوارفارين. قد يحسّن إعطاء فيتامين K الارتفاع المرتبط بالوارفارين، لكنه "
                "غالباً غير فعّال في الفشل الكبدي، لأن المشكلة ليست نقص الفيتامين بل عجز "
                "الخلايا الكبدية التالفة عن إنتاج عوامل التخثر.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>يُنصح بمناقشة نتائج PT/INR مع مختص رعاية صحية في حال انطبق أيّ مما "
                "يلي:</p>"
                "<ul>"
                "<li>INR لديك خارج النطاق المرجعي.</li>"
                "<li>أنت تتناول الوارفارين أو مضاد تخثر آخر وINR ينحرف عن الهدف.</li>"
                "<li>تعاني من كدمات غير مبررة أو نزيف اللثة أو الأنف أو نزيف مطوّل من "
                "الجروح.</li>"
                "<li>تلاحظ برازاً داكناً أو دموياً أو دماً في البول.</li>"
                "<li>لديك مرض كبدي وINR في ارتفاع.</li>"
                "<li>بدأت مؤخراً دواءً أو مكملاً غذائياً جديداً.</li>"
                "</ul>"
                "<p>قد تشكّل أعراض النزيف حالة طوارئ طبية. يجب على مرضى الوارفارين إدراك "
                "أهمية فحوصات INR المنتظمة وعدم تفويت المواعيد. عند الشك، مراجعة الطبيب "
                "هي دائماً الخطوة الصحيحة.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف تساعدك Norya",
            body_html=(
                "<p>في Norya لا نقدّم تشخيصاً—هدفنا جعل تقرير مختبرك أسهل للفهم ومساعدتك "
                "على التحضير لموعدك مع الطبيب. "
                '<a href="/analyze">ارفع فحص الدم الخاص بك</a> واحصل خلال دقائق على ملخص '
                "صحي منظّم بلغة واضحة يشرح PT وINR وجميع قيمك الأخرى مع النطاقات المرجعية "
                "والسياق.</p>"
                "<p>بهذا الملخص يمكنك طرح الأسئلة المناسبة على طبيبك وفهم أيّ القيم تحتاج "
                "متابعة. لا نقدّم تشخيصات ولا توصيات علاجية—نساعدك على فهم نتائجك.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص '
                'الطبي.</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. '
                '<a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_inr_sections_by_lang():
    """Returns sections_by_lang dict for PT & INR article (all 9 languages)."""
    return {
        "tr": _sections_tr(),
        "en": _sections_en(),
        "es": _sections_es(),
        "de": _sections_de(),
        "fr": _sections_fr(),
        "it": _sections_it(),
        "he": _sections_he(),
        "hi": _sections_hi(),
        "ar": _sections_ar(),
    }


def get_inr_faq_schema_qa():
    """Returns faq_schema_qa dict for PT & INR article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is the difference between PT and INR?",
             "answer": "PT (Prothrombin Time) measures the raw time in seconds for blood to clot via the extrinsic pathway. INR (International Normalized Ratio) standardises the PT result so it can be compared across different laboratories and reagents. Both are used together to assess clotting function."},
            {"question": "What is a normal INR level?",
             "answer": "For individuals not taking anticoagulants, a normal INR is typically 0.8–1.1. For patients on warfarin, the target INR is usually 2.0–3.0 for most conditions, or 2.5–3.5 for mechanical heart valves. Always discuss your results with your doctor."},
            {"question": "What causes a high INR?",
             "answer": "Common causes include anticoagulant medications (especially warfarin), liver disease (cirrhosis, hepatitis), vitamin K deficiency, certain antibiotics that alter gut flora, and disseminated intravascular coagulation (DIC). A high INR means the blood clots more slowly and may increase bleeding risk."},
            {"question": "How often should INR be monitored on warfarin?",
             "answer": "When starting warfarin, INR is typically checked every few days until stable, then every 1–4 weeks. Frequency depends on dose stability and individual factors. Your doctor will determine the appropriate monitoring schedule."},
        ],
        "tr": [
            {"question": "PT ve INR arasındaki fark nedir?",
             "answer": "PT (Protrombin Zamanı) kanın ekstrensek yolak aracılığıyla pıhtılaşma süresini saniye cinsinden ölçer. INR (Uluslararası Normalleştirilmiş Oran) ise PT sonucunu farklı laboratuvarlar ve reaktifler arasında karşılaştırılabilir hale getirir. İkisi birlikte pıhtılaşma fonksiyonunu değerlendirmek için kullanılır."},
            {"question": "Normal INR değeri nedir?",
             "answer": "Antikoagülan almayan bireylerde normal INR genellikle 0,8–1,1 arasındadır. Varfarin kullanan hastalarda hedef INR çoğu durum için 2,0–3,0, mekanik kalp kapağı için 2,5–3,5'tir. Sonuçlarınızı mutlaka hekiminizle görüşün."},
            {"question": "INR yüksekliğine ne sebep olur?",
             "answer": "Yaygın nedenler arasında antikoagülan ilaçlar (özellikle varfarin), karaciğer hastalıkları (siroz, hepatit), K vitamini eksikliği, bağırsak florasını değiştiren bazı antibiyotikler ve yaygın damar içi pıhtılaşma (DIC) sayılabilir. Yüksek INR kanın daha yavaş pıhtılaştığı ve kanama riskinin artabileceği anlamına gelir."},
            {"question": "Varfarin kullanırken INR ne sıklıkla takip edilmeli?",
             "answer": "Varfarin başlandığında INR genellikle değer stabil olana kadar birkaç günde bir, ardından 1–4 haftada bir kontrol edilir. Sıklık, doz stabilitesine ve bireysel faktörlere bağlıdır. Uygun takip programını hekiminiz belirleyecektir."},
        ],
        "es": [
            {"question": "¿Cuál es la diferencia entre TP e INR?",
             "answer": "El TP (Tiempo de Protrombina) mide el tiempo bruto en segundos que tarda la sangre en coagularse por la vía extrínseca. El INR (Ratio Internacional Normalizado) estandariza el resultado del TP para poder compararlo entre distintos laboratorios y reactivos. Ambos se usan juntos para evaluar la función de coagulación."},
            {"question": "¿Cuál es un nivel normal de INR?",
             "answer": "En personas sin anticoagulantes, el INR normal suele ser 0,8–1,1. En pacientes con warfarina, el objetivo suele ser 2,0–3,0 para la mayoría de las indicaciones, o 2,5–3,5 para válvulas cardíacas mecánicas. Consulte siempre con su médico."},
            {"question": "¿Qué causa un INR elevado?",
             "answer": "Las causas más frecuentes incluyen medicamentos anticoagulantes (especialmente warfarina), enfermedades hepáticas (cirrosis, hepatitis), deficiencia de vitamina K, ciertos antibióticos que alteran la flora intestinal y la coagulación intravascular diseminada (CID). Un INR alto significa que la sangre coagula más lentamente y puede aumentar el riesgo de hemorragia."},
        ],
        "de": [
            {"question": "Was ist der Unterschied zwischen PT und INR?",
             "answer": "Die PT (Prothrombinzeit) misst die Rohzeit in Sekunden, die das Blut zum Gerinnen über den extrinsischen Weg benötigt. Die INR (International Normalized Ratio) standardisiert das PT-Ergebnis, um es zwischen verschiedenen Laboren und Reagenzien vergleichbar zu machen. Beide werden gemeinsam zur Beurteilung der Gerinnungsfunktion eingesetzt."},
            {"question": "Was ist ein normaler INR-Wert?",
             "answer": "Für Personen ohne Antikoagulanzien liegt die normale INR typischerweise bei 0,8–1,1. Bei Warfarin-Patienten beträgt der Zielwert meist 2,0–3,0 bzw. 2,5–3,5 bei mechanischen Herzklappen. Besprechen Sie Ihre Ergebnisse immer mit Ihrem Arzt."},
            {"question": "Was verursacht eine erhöhte INR?",
             "answer": "Häufige Ursachen sind Antikoagulanzien (insbesondere Warfarin), Lebererkrankungen (Zirrhose, Hepatitis), Vitamin-K-Mangel, bestimmte Antibiotika, die die Darmflora verändern, und disseminierte intravasale Gerinnung (DIC). Eine hohe INR bedeutet, dass das Blut langsamer gerinnt, was das Blutungsrisiko erhöhen kann."},
        ],
        "fr": [
            {"question": "Quelle est la différence entre TP et INR ?",
             "answer": "Le TP (Temps de Prothrombine) mesure le temps brut en secondes pour la coagulation du sang via la voie extrinsèque. L'INR (International Normalized Ratio) standardise le résultat du TP afin de le rendre comparable entre différents laboratoires et réactifs. Les deux sont utilisés ensemble pour évaluer la fonction de coagulation."},
            {"question": "Quel est un niveau d'INR normal ?",
             "answer": "Pour les personnes ne prenant pas d'anticoagulants, l'INR normal est généralement de 0,8 à 1,1. Chez les patients sous warfarine, la cible est habituellement de 2,0 à 3,0, ou de 2,5 à 3,5 pour les valves cardiaques mécaniques. Discutez toujours de vos résultats avec votre médecin."},
            {"question": "Quelles sont les causes d'un INR élevé ?",
             "answer": "Les causes fréquentes incluent les médicaments anticoagulants (surtout la warfarine), les maladies hépatiques (cirrhose, hépatite), la carence en vitamine K, certains antibiotiques modifiant la flore intestinale et la coagulation intravasculaire disséminée (CIVD). Un INR élevé signifie que le sang coagule plus lentement et peut augmenter le risque hémorragique."},
        ],
        "it": [
            {"question": "Qual è la differenza tra PT e INR?",
             "answer": "Il PT (Tempo di Protrombina) misura il tempo grezzo in secondi necessario al sangue per coagulare attraverso la via estrinseca. L'INR (International Normalized Ratio) standardizza il risultato del PT rendendolo confrontabile tra laboratori e reagenti diversi. Entrambi vengono utilizzati insieme per valutare la funzione coagulativa."},
            {"question": "Qual è un livello di INR normale?",
             "answer": "Nelle persone che non assumono anticoagulanti, l'INR normale è tipicamente 0,8–1,1. Nei pazienti in terapia con warfarin, il target è solitamente 2,0–3,0, o 2,5–3,5 per valvole cardiache meccaniche. Discutete sempre i risultati con il vostro medico."},
            {"question": "Cosa causa un INR elevato?",
             "answer": "Le cause comuni includono farmaci anticoagulanti (in particolare warfarin), malattie epatiche (cirrosi, epatite), carenza di vitamina K, alcuni antibiotici che alterano la flora intestinale e la coagulazione intravascolare disseminata (CID). Un INR elevato indica che il sangue coagula più lentamente e può aumentare il rischio emorragico."},
        ],
        "he": [
            {"question": "מה ההבדל בין PT ל-INR?",
             "answer": "PT (זמן פרותרומבין) מודד את הזמן הגולמי בשניות שלוקח לדם להיקרש דרך המסלול החיצוני. INR (יחס בינלאומי מנורמל) מתקנן את תוצאת ה-PT כך שניתן להשוות אותה בין מעבדות וריאגנטים שונים. שניהם משמשים יחד להערכת תפקוד הקרישה."},
            {"question": "מהו ערך INR תקין?",
             "answer": "באנשים שאינם נוטלים נוגדי קרישה, INR תקין הוא בדרך כלל 0.8–1.1. בחולים הנוטלים וורפרין, היעד הוא בדרך כלל 2.0–3.0, או 2.5–3.5 למסתמי לב מכניים. שוחחו תמיד על התוצאות עם הרופא."},
            {"question": "מה גורם ל-INR גבוה?",
             "answer": "גורמים שכיחים כוללים תרופות נוגדות קרישה (בעיקר וורפרין), מחלות כבד (שחמת, דלקת כבד), חוסר ויטמין K, אנטיביוטיקות מסוימות המשנות את פלורת המעי, וקרישה תוך-כלית מפושטת (DIC). INR גבוה פירושו שהדם נקרש לאט יותר ועלול להגביר סיכון לדימום."},
        ],
        "hi": [
            {"question": "PT और INR में क्या अंतर है?",
             "answer": "PT (प्रोथ्रोम्बिन टाइम) एक्सट्रिंसिक पाथवे के ज़रिये खून के क्लॉट होने में लगने वाले कच्चे समय को सेकंड में मापता है। INR (इंटरनेशनल नॉर्मलाइज़्ड रेशियो) PT रिज़ल्ट को मानकीकृत करता है ताकि विभिन्न लैब और रिएजेंट्स में इसकी तुलना की जा सके। दोनों का उपयोग क्लॉटिंग फ़ंक्शन के मूल्यांकन के लिए एक साथ किया जाता है।"},
            {"question": "सामान्य INR स्तर क्या है?",
             "answer": "एंटीकोगुलेंट न लेने वालों में सामान्य INR आमतौर पर 0.8–1.1 होता है। वार्फ़रिन लेने वालों में लक्ष्य INR अधिकतर स्थितियों में 2.0–3.0 या मैकेनिकल हार्ट वॉल्व के लिए 2.5–3.5 होता है। अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें।"},
            {"question": "INR बढ़ने का क्या कारण है?",
             "answer": "सामान्य कारणों में एंटीकोगुलेंट दवाएँ (विशेषकर वार्फ़रिन), लिवर रोग (सिरोसिस, हेपेटाइटिस), विटामिन K की कमी, आँतों के फ़्लोरा को बदलने वाली कुछ एंटीबायोटिक्स और DIC शामिल हैं। ऊँचा INR यानी खून धीमे जमता है और ब्लीडिंग का ख़तरा बढ़ सकता है।"},
        ],
        "ar": [
            {"question": "ما الفرق بين PT و INR؟",
             "answer": "يقيس PT (زمن البروثرومبين) الوقت الخام بالثواني لتخثر الدم عبر المسار الخارجي. يوحّد INR (النسبة المعيارية الدولية) نتيجة PT بحيث يمكن مقارنتها بين مختبرات وكواشف مختلفة. يُستخدم كلاهما معاً لتقييم وظيفة التخثر."},
            {"question": "ما مستوى INR الطبيعي؟",
             "answer": "لدى الأشخاص الذين لا يتناولون مضادات التخثر، يكون INR الطبيعي عادةً 0.8–1.1. لدى مرضى الوارفارين، يكون الهدف عادةً 2.0–3.0، أو 2.5–3.5 لصمامات القلب الميكانيكية. ناقش نتائجك دائماً مع طبيبك."},
            {"question": "ما أسباب ارتفاع INR؟",
             "answer": "تشمل الأسباب الشائعة أدوية مضادات التخثر (خاصة الوارفارين)، وأمراض الكبد (التليف، التهاب الكبد)، ونقص فيتامين K، وبعض المضادات الحيوية التي تغيّر فلورا الأمعاء، والتخثر المنتشر داخل الأوعية (DIC). يعني INR المرتفع أن الدم يتخثر أبطأ وقد يزيد خطر النزيف."},
        ],
    }
