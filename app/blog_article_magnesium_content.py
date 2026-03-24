# -*- coding: utf-8 -*-
"""
Magnesium blog article — full body content for all 9 languages.
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
            heading="Magnezyum kan testi: sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p>Kan tahlili raporunuzda <strong>magnezyum</strong> değerini gördüğünüzde bu sayının "
                "sağlığınız hakkında ne söylediğini merak etmeniz doğaldır. Magnezyum, vücuttaki "
                "300&rsquo;den fazla enzimatik reaksiyonda rol oynayan esansiyel bir mineraldir ve "
                "kas fonksiyonundan kalp ritmine, kemik sağlığından enerji metabolizmasına kadar pek "
                "çok hayati süreci doğrudan etkiler.</p>"
                "<p>Bu rehber magnezyum kan testinin ne anlama geldiğini, referans aralıklarını, "
                "düşük veya yüksek çıkmasının olası nedenlerini ve ne zaman doktora başvurmanız "
                "gerektiğini sade bir dille açıklamayı amaçlıyor. Amacımız teşhis koymak değil; "
                "sonuçlarınızı daha iyi anlayarak hekiminizle verimli bir görüşme yapmanıza "
                "yardımcı olmaktır.</p>"
                "<p>Magnezyum eksikliği dünya genelinde yaygın olmasına rağmen sıklıkla göz ardı "
                "edilir. Erken fark edilmesi ve uygun beslenme veya takviye ile düzeltilmesi, "
                "ciddi sağlık sorunlarının önüne geçebilir.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="Magnezyum nedir?",
            body_html=(
                "<p><strong>Magnezyum (Mg)</strong>, periyodik tabloda 12. sırada yer alan, insan "
                "vücudundaki en bol dördüncü mineraldir. Vücuttaki toplam magnezyumun yaklaşık "
                "%60&rsquo;ı kemiklerde, %39&rsquo;u kas ve yumuşak dokularda, yalnızca %1&rsquo;i "
                "ise kanda bulunur. Kan testlerinde ölçülen değer bu küçük fraksiyonu yansıtır; "
                "dolayısıyla serum magnezyumu normal çıksa bile doku depolarında eksiklik olabilir.</p>"
                "<p>Magnezyum dışarıdan, yani besinler veya takviyeler yoluyla alınması gereken "
                "bir mineraldir; vücut tarafından sentezlenemez. Koyu yeşil yapraklı sebzeler, "
                "kuruyemişler, tohumlar ve tam tahıllar başlıca kaynaklarıdır. Günlük ihtiyaç "
                "yetişkin erkeklerde yaklaşık 400&ndash;420&nbsp;mg, kadınlarda ise "
                "310&ndash;320&nbsp;mg olarak kabul edilir.</p>"
                "<p>Magnezyum iyonları hücre zarı potansiyelini düzenler, sinir iletimini sağlar "
                "ve ATP&rsquo;nin (adenozin trifosfat) aktif formunu oluşturur. Kısacası enerji "
                "üretiminden kas kasılmasına kadar vücutta neredeyse hiçbir biyokimyasal süreç "
                "magnezyumsuz verimli çalışamaz.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="Magnezyumun vücuttaki rolü",
            body_html=(
                "<p>Magnezyum, <strong>300&rsquo;den fazla enzim reaksiyonunda</strong> kofaktör "
                "olarak görev yapar. Bu reaksiyonlar protein sentezi, kas ve sinir fonksiyonu, "
                "kan şekeri kontrolü ve kan basıncı düzenlemesini kapsar. Ayrıca DNA ve RNA "
                "sentezi ile hücre bölünmesi için de gereklidir.</p>"
                "<p>Kardiyovasküler sistemde magnezyum, kalp kasının düzenli kasılmasını ve "
                "damar duvarlarının gevşemesini destekler. Yeterli magnezyum düzeyi, sağlıklı "
                "bir kalp ritmi sürdürülmesine yardımcı olur; eksikliğinde <em>aritmi</em> "
                "riski artar. Ayrıca magnezyum, <strong>kalsiyum</strong> ve <strong>potasyum</strong> "
                "gibi diğer elektrolitlerin hücre içi ve dışı dengesini düzenleyen bir "
                "\"kapı bekçisi\" işlevi görür.</p>"
                "<p>Kemik sağlığı açısından magnezyum, kalsiyumun kemiklere yerleşmesini "
                "kolaylaştırır ve D vitamininin aktif formuna dönüşümünde rol oynar. "
                "Araştırmalar yeterli magnezyum alımının osteoporoz riskini azaltabileceğini "
                "göstermektedir. Ek olarak magnezyum, insülin duyarlılığını artırarak tip&nbsp;2 "
                "diyabet riskini düşürmede de etkili olabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Magnezyum referans aralıkları",
            body_html=(
                "<p>Serum magnezyum düzeyi basit bir kan testiyle ölçülür. Aşağıdaki tablo yaygın "
                "olarak kabul edilen referans aralıklarını göstermektedir; ancak değerler "
                "laboratuvarlar arasında hafif farklılık gösterebilir.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Durum</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Düşük (Hipomagnezemi)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0,70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,7 &ndash; 2,2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0,70 &ndash; 0,90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,4 &ndash; 1,8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Yüksek (Hipermagnezemi)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2,2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0,90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1,8</td>'
                "</tr></tbody></table>"
                "<p><strong>Normal serum magnezyum aralığı 1,7&ndash;2,2&nbsp;mg/dL</strong> "
                "(0,70&ndash;0,90&nbsp;mmol/L) olarak kabul edilir. Bu aralığın altı "
                "<em>hipomagnezemi</em>, üstü ise <em>hipermagnezemi</em> olarak adlandırılır. "
                "Sonuçlarınızı değerlendirirken laboratuvarınızın kendi referans aralığını "
                "dikkate almanız önemlidir.</p>"
                "<p>Serum magnezyumunun toplam vücut magnezyumunun yalnızca %1&rsquo;ini "
                "yansıttığını unutmayın. Bazı uzmanlar, doku düzeyinde eksikliği daha iyi "
                "saptamak için eritrosit (kırmızı kan hücresi) magnezyumu veya 24 saatlik idrar "
                "magnezyumu gibi ek testleri önerebilir.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Düşük magnezyum (hipomagnezemi) nedenleri",
            body_html=(
                "<p>Serum magnezyum düzeyinin 1,7&nbsp;mg/dL&rsquo;nin altına düşmesi "
                "<strong>hipomagnezemi</strong> olarak tanımlanır. En sık karşılaşılan nedenler "
                "arasında yetersiz beslenme, bağırsaklardan emilim bozukluğu ve aşırı böbrek "
                "yoluyla kayıp yer alır.</p>"
                "<p><strong>Başlıca nedenler:</strong> magnezyumdan fakir diyet, kronik ishal "
                "veya kusma, çölyak hastalığı ve Crohn hastalığı gibi malabsorpsiyon sendromları, "
                "kronik alkolizm, kontrolsüz diyabet (özellikle poliüri nedeniyle), uzun süreli "
                "diüretik kullanımı (tiyazid ve loop diüretikler) ve proton pompa inhibitörleri "
                "(PPI) gibi mide asidi baskılayıcı ilaçlar. Ayrıca gebelik döneminde artan "
                "ihtiyaç da eksikliğe yol açabilir.</p>"
                "<p>Magnezyum eksikliği sıklıkla <strong>hipokalsemi</strong> ve "
                "<strong>hipokalemi</strong> ile birlikte görülür çünkü magnezyum bu minerallerin "
                "emilimini ve böbreklerden geri kazanımını düzenler. Dolayısıyla kalsiyum veya "
                "potasyum düşüklüğü düzeltilmek isteniyorsa öncelikle magnezyum eksikliğinin "
                "giderilmesi gerekebilir.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Yüksek magnezyum (hipermagnezemi) nedenleri",
            body_html=(
                "<p><strong>Hipermagnezemi</strong>, serum magnezyumunun 2,2&nbsp;mg/dL&rsquo;nin "
                "üzerine çıkmasıdır. Sağlıklı böbreklere sahip bireylerde oldukça nadir görülür "
                "çünkü böbrekler fazla magnezyumu idrarla etkin şekilde atar.</p>"
                "<p>En sık neden <strong>böbrek yetmezliği</strong>dir; glomerüler filtrasyon hızı "
                "düştüğünde magnezyum atılımı yetersiz kalır ve kanda birikir. Aşırı dozda "
                "magnezyum takviyesi almak, magnezyum içeren antiasitler (örn. magnezyum "
                "hidroksit) veya laksatifler de hipermagnezemi riskini artırır, özellikle "
                "böbrek fonksiyonu sınırda olan hastalarda.</p>"
                "<p>Daha az görülen nedenler arasında Addison hastalığı, hipotiroidizm, lityum "
                "kullanımı ve masif doku hasarı (rabdomiyoliz, yanık) sayılabilir. Ciddi "
                "hipermagnezemi yaşamı tehdit edebilir; kas felci, solunum yetmezliği ve "
                "kardiyak arreste neden olabilir. Bu nedenle böbrek hastaları magnezyum "
                "içeren ilaç ve takviyeler konusunda dikkatli olmalıdır.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Magnezyum dengesizliği belirtileri",
            body_html=(
                "<p><strong>Eksiklik belirtileri:</strong> Hafif magnezyum eksikliği uzun süre "
                "belirti vermeyebilir. İlerledikçe en sık görülen şikâyetler kas krampları, "
                "seğirmeler, kronik yorgunluk, iştahsızlık ve bulantıdır. Daha ileri "
                "düzeylerde uyuşma ve karıncalanma, <em>aritmi</em> (düzensiz kalp atışı), "
                "kişilik değişiklikleri ve hatta nöbetler ortaya çıkabilir.</p>"
                "<p>Magnezyum eksikliğinin sinsi bir yönü, semptomların genellikle özgül "
                "olmamasıdır; yorgunluk ve kas ağrısı birçok durumda görülebildiği için "
                "eksiklik kolaylıkla atlanabilir. Bu nedenle risk grubundaki bireylerden "
                "(kronik alkol kullanımı, diüretik tedavisi, gastrointestinal hastalıklar) "
                "düzenli olarak magnezyum kontrolü istenmesi önerilir.</p>"
                "<p><strong>Fazlalık belirtileri:</strong> Hipermagnezemi ilerledikçe bulantı, "
                "kusma, yüzde kızarma, düşük tansiyon, bradikardi (yavaş kalp atışı), "
                "derin tendon reflekslerinin kaybı ve kas güçsüzlüğü gelişebilir. Çok yüksek "
                "düzeylerde solunum depresyonu ve kalp durması riski vardır. Böbrek "
                "fonksiyonu normal olan kişilerde oral magnezyum alımıyla toksisiteye "
                "ulaşmak oldukça zordur; asıl risk intravenöz veya böbrek yetmezliği "
                "zemininde ortaya çıkar.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Magnezyum açısından zengin besinler",
            body_html=(
                "<p>Yeterli magnezyum alımı öncelikle dengeli bir beslenmeyle sağlanmalıdır. "
                "Aşağıdaki besinler magnezyum bakımından en zengin kaynaklardandır:</p>"
                "<p><strong>Koyu yeşil yapraklı sebzeler</strong> (ıspanak, pazı, kara lahana), "
                "<strong>kuruyemişler</strong> (badem, kaju, fıstık), <strong>tohumlar</strong> "
                "(kabak çekirdeği, çiya tohumu, keten tohumu), <strong>tam tahıllar</strong> "
                "(yulaf, kinoa, esmer pirinç), <strong>baklagiller</strong> (siyah fasulye, "
                "mercimek, nohut), <strong>bitter çikolata</strong> (%70+ kakao), "
                "<strong>avokado</strong> ve <strong>muz</strong>. Bir porsiyon kabak "
                "çekirdeği (28&nbsp;g) yaklaşık 150&nbsp;mg magnezyum içerir ve günlük "
                "ihtiyacın önemli bir bölümünü tek başına karşılayabilir.</p>"
                "<p>İşlenmiş gıdalar ve rafine tahıllar magnezyum kaybına uğrar; bu nedenle "
                "modern Batı diyetinde magnezyum yetersizliği yaygındır. İçme suyunun "
                "magnezyum içeriği de bölgeye göre değişir ve ek bir kaynak olabilir. "
                "Takviye kullanmayı düşünüyorsanız magnezyum sitrat, glisinit ve taurat "
                "formlarının biyoyararlanımının daha yüksek olduğunu, magnezyum oksidin ise "
                "daha düşük emilime sahip olduğunu bilmek yararlı olacaktır; takviye "
                "kullanmadan önce mutlaka doktorunuza danışın.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Magnezyum düzeyiniz referans aralığının dışındaysa veya açıklanamayan "
                "kas krampları, kronik yorgunluk, kalp çarpıntısı ya da uyuşma/karıncalanma "
                "gibi belirtiler yaşıyorsanız bir sağlık uzmanına başvurmanızı öneririz. "
                "Özellikle böbrek hastalığı, diyabet, gastrointestinal hastalık veya kronik "
                "alkol kullanımı öyküsü varsa magnezyum değerlerinizin düzenli takibi "
                "önemlidir.</p>"
                "<p>Diüretik, PPI veya digoksin gibi ilaçlar kullanıyorsanız, magnezyum "
                "düzeyinizi etkileyebileceğinden doktorunuzla düzenli kontrol planı "
                "oluşturmalısınız. Magnezyum eksikliği tedavi edilmeden bırakıldığında "
                "kalp ritim bozuklukları, osteoporoz ve insülin direnci gibi ciddi "
                "komplikasyonlara yol açabilir.</p>"
                "<p>Ayrıca hipokalsemi veya hipokalemi tedavisine yanıt vermeyen hastalarda "
                "altta yatan magnezyum eksikliğinin araştırılması önerilir. Magnezyum "
                "düzeyiniz hakkında endişeleriniz varsa kan tahlili sonuçlarınızı bir "
                "dahiliye veya endokrinoloji uzmanına gösterebilirsiniz.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya ile kan tahlillerinizi anlayın",
            body_html=(
                "<p><strong>Norya</strong>, kan tahlili sonuçlarınızı yüklemenize ve dakikalar "
                "içinde yapılandırılmış, anlaşılır bir sağlık özet raporu almanıza olanak tanır. "
                "Magnezyum, kalsiyum, potasyum ve diğer tüm parametreleriniz açık bir dille "
                "yorumlanarak doktor randevunuza hazırlıklı gitmenizi sağlar.</p>"
                "<p>Raporunuzu yükleyin, sonuçlarınızın ne anlama geldiğini öğrenin ve "
                "hekiminizle paylaşabileceğiniz özet raporu birkaç dakikada oluşturun. "
                '<a href="/analyze">Norya ile analize başlayın</a>.</p>'
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
            heading="Magnesium blood test: what your results mean",
            body_html=(
                "<p>When you see a <strong>magnesium</strong> value on your blood test report, it is "
                "natural to wonder what that number says about your health. Magnesium is an essential "
                "mineral involved in more than 300 enzymatic reactions in the body, influencing everything "
                "from muscle function and heart rhythm to bone health and energy metabolism.</p>"
                "<p>This guide explains what a magnesium blood test measures, the reference ranges you "
                "should know, possible causes of low or high levels, and when to talk to your doctor. "
                "Our goal is not to diagnose but to help you understand your results so you can have a "
                "more informed conversation with your healthcare provider.</p>"
                "<p>Magnesium deficiency is surprisingly common worldwide yet often overlooked. Catching "
                "it early and addressing it through diet or supplementation can prevent serious health "
                "complications down the road.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="What is magnesium?",
            body_html=(
                "<p><strong>Magnesium (Mg)</strong> is the fourth most abundant mineral in the human "
                "body. Approximately 60% of the body&rsquo;s magnesium is stored in bones, 39% in "
                "muscles and soft tissues, and only about 1% circulates in the blood. A standard "
                "blood test measures this small circulating fraction, so serum levels can appear "
                "normal even when tissue stores are depleted.</p>"
                "<p>Magnesium is an essential nutrient&mdash;meaning the body cannot produce it&mdash; "
                "and must be obtained through food or supplements. Dark leafy greens, nuts, seeds, and "
                "whole grains are among the richest dietary sources. The recommended daily intake is "
                "about 400&ndash;420&nbsp;mg for adult men and 310&ndash;320&nbsp;mg for adult women.</p>"
                "<p>At the cellular level magnesium regulates membrane potential, supports nerve "
                "transmission, and forms the active complex of ATP (adenosine triphosphate)&mdash;the "
                "body&rsquo;s primary energy currency. In short, almost no biochemical process in the "
                "body runs efficiently without adequate magnesium.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="Role of magnesium in the body",
            body_html=(
                "<p>Magnesium acts as a cofactor in <strong>over 300 enzyme reactions</strong>. These "
                "reactions include protein synthesis, muscle and nerve function, blood sugar regulation, "
                "and blood pressure management. It is also essential for DNA and RNA synthesis and for "
                "cell division.</p>"
                "<p>In the cardiovascular system magnesium supports regular contraction of the heart "
                "muscle and helps blood vessel walls relax. Adequate magnesium helps maintain a healthy "
                "heart rhythm; deficiency increases the risk of <em>arrhythmia</em>. Magnesium also "
                "acts as a gatekeeper for other electrolytes such as <strong>calcium</strong> and "
                "<strong>potassium</strong>, regulating their movement into and out of cells.</p>"
                "<p>For bone health magnesium facilitates calcium deposition into bone and plays a role "
                "in converting vitamin&nbsp;D to its active form. Research suggests that sufficient "
                "magnesium intake may reduce the risk of osteoporosis. Additionally, magnesium improves "
                "insulin sensitivity and may help lower the risk of type&nbsp;2 diabetes.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Magnesium reference ranges",
            body_html=(
                "<p>Serum magnesium is measured with a simple blood draw. The table below shows "
                "commonly accepted reference ranges, though values may vary slightly between "
                "laboratories.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Status</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Low (Hypomagnesemia)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0.70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.7 &ndash; 2.2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0.70 &ndash; 0.90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.4 &ndash; 1.8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">High (Hypermagnesemia)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2.2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0.90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1.8</td>'
                "</tr></tbody></table>"
                "<p>The <strong>normal serum magnesium range is 1.7&ndash;2.2&nbsp;mg/dL</strong> "
                "(0.70&ndash;0.90&nbsp;mmol/L). Values below this range are termed "
                "<em>hypomagnesemia</em> and values above it <em>hypermagnesemia</em>. Always "
                "check the specific reference range printed on your lab report.</p>"
                "<p>Keep in mind that serum magnesium reflects only about 1% of total body stores. "
                "Some clinicians may order additional tests such as red blood cell (RBC) magnesium "
                "or a 24-hour urine magnesium to better assess tissue-level status.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Causes of low magnesium (hypomagnesemia)",
            body_html=(
                "<p>A serum magnesium level below 1.7&nbsp;mg/dL is classified as "
                "<strong>hypomagnesemia</strong>. The most common causes include inadequate dietary "
                "intake, poor intestinal absorption, and excessive renal losses.</p>"
                "<p><strong>Key causes:</strong> magnesium-poor diet, chronic diarrhea or vomiting, "
                "malabsorption syndromes such as celiac disease and Crohn&rsquo;s disease, chronic "
                "alcoholism, poorly controlled diabetes (particularly due to polyuria), prolonged use "
                "of diuretics (thiazides and loop diuretics), and proton pump inhibitors (PPIs). "
                "Increased demand during pregnancy can also lead to deficiency.</p>"
                "<p>Magnesium deficiency frequently coexists with <strong>hypocalcemia</strong> and "
                "<strong>hypokalemia</strong> because magnesium regulates the absorption and renal "
                "reabsorption of these minerals. If calcium or potassium levels remain stubbornly low "
                "despite treatment, an underlying magnesium deficit should be investigated.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Causes of high magnesium (hypermagnesemia)",
            body_html=(
                "<p><strong>Hypermagnesemia</strong> is defined as a serum magnesium level above "
                "2.2&nbsp;mg/dL. It is quite rare in individuals with healthy kidneys because the "
                "kidneys efficiently excrete excess magnesium in urine.</p>"
                "<p>The most common cause is <strong>kidney failure</strong>. When the glomerular "
                "filtration rate drops, magnesium excretion becomes inadequate and blood levels rise. "
                "Excessive magnesium supplementation, magnesium-containing antacids (e.g., magnesium "
                "hydroxide), and laxatives also increase risk, especially in patients with borderline "
                "renal function.</p>"
                "<p>Less common causes include Addison&rsquo;s disease, hypothyroidism, lithium use, "
                "and massive tissue injury (rhabdomyolysis, burns). Severe hypermagnesemia can be "
                "life-threatening, potentially causing muscle paralysis, respiratory failure, and "
                "cardiac arrest. Patients with kidney disease should exercise caution with "
                "magnesium-containing medications and supplements.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of magnesium imbalance",
            body_html=(
                "<p><strong>Deficiency symptoms:</strong> Mild magnesium deficiency may be "
                "asymptomatic for a long time. As it progresses the most common complaints include "
                "muscle cramps, twitching, chronic fatigue, loss of appetite, and nausea. In more "
                "advanced stages numbness and tingling, <em>arrhythmia</em> (irregular heartbeat), "
                "personality changes, and even seizures can develop.</p>"
                "<p>One challenge with magnesium deficiency is that symptoms are often nonspecific; "
                "fatigue and muscle pain overlap with many other conditions, making it easy to miss. "
                "For this reason routine magnesium monitoring is recommended for individuals in "
                "high-risk groups (chronic alcohol use, diuretic therapy, gastrointestinal diseases).</p>"
                "<p><strong>Excess symptoms:</strong> As hypermagnesemia worsens, nausea, vomiting, "
                "facial flushing, low blood pressure, bradycardia (slow heart rate), loss of deep "
                "tendon reflexes, and muscle weakness may develop. At very high levels respiratory "
                "depression and cardiac arrest are possible. Toxicity from oral magnesium alone is "
                "extremely rare in people with normal kidney function; the main risks arise from "
                "intravenous administration or renal impairment.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Food sources rich in magnesium",
            body_html=(
                "<p>Adequate magnesium intake should primarily come from a balanced diet. The "
                "following foods are among the richest sources of magnesium:</p>"
                "<p><strong>Dark leafy greens</strong> (spinach, Swiss chard, kale), "
                "<strong>nuts</strong> (almonds, cashews, peanuts), <strong>seeds</strong> "
                "(pumpkin seeds, chia seeds, flaxseeds), <strong>whole grains</strong> "
                "(oats, quinoa, brown rice), <strong>legumes</strong> (black beans, lentils, "
                "chickpeas), <strong>dark chocolate</strong> (70%+ cocoa), <strong>avocados</strong>, "
                "and <strong>bananas</strong>. A single serving of pumpkin seeds (28&nbsp;g) provides "
                "roughly 150&nbsp;mg of magnesium, covering a significant portion of the daily "
                "requirement.</p>"
                "<p>Processed foods and refined grains lose much of their magnesium content, which "
                "is one reason magnesium insufficiency is common in modern Western diets. Drinking "
                "water can also be a variable source depending on local mineral content. If you are "
                "considering supplementation, note that magnesium citrate, glycinate, and taurate "
                "forms have higher bioavailability than magnesium oxide; always consult your doctor "
                "before starting any supplement.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>If your magnesium level falls outside the reference range, or if you experience "
                "unexplained muscle cramps, chronic fatigue, heart palpitations, or numbness and "
                "tingling, we recommend consulting a healthcare professional. Regular monitoring is "
                "especially important if you have a history of kidney disease, diabetes, "
                "gastrointestinal disorders, or chronic alcohol use.</p>"
                "<p>If you are taking medications such as diuretics, PPIs, or digoxin, your "
                "magnesium levels may be affected; work with your doctor to establish a routine "
                "monitoring plan. Untreated magnesium deficiency can lead to serious complications "
                "including cardiac arrhythmias, osteoporosis, and insulin resistance.</p>"
                "<p>Additionally, patients with hypocalcemia or hypokalemia that does not respond to "
                "treatment should be evaluated for underlying magnesium deficiency. If you have "
                "concerns about your magnesium level, consider discussing your blood test results "
                "with an internist or endocrinologist.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Understand your blood tests with Norya",
            body_html=(
                "<p><strong>Norya</strong> lets you upload your blood test results and receive a "
                "structured, easy-to-understand health summary report within minutes. Your magnesium, "
                "calcium, potassium, and every other parameter are explained in plain language, "
                "preparing you for a more productive doctor visit.</p>"
                "<p>Upload your report, learn what your results mean, and generate a shareable summary "
                "for your doctor in just a few minutes. "
                '<a href="/analyze">Start your analysis with Norya</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace '
                'medical advice or diagnosis.</strong> Always discuss your results with a healthcare '
                'professional. <a href="/analyze">Start analysis with Norya</a></p>'
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
            heading="Análisis de magnesio en sangre: qué significan tus resultados",
            body_html=(
                "<p>Cuando ves el valor de <strong>magnesio</strong> en tu análisis de sangre, es "
                "normal preguntarse qué dice ese número sobre tu salud. El magnesio es un mineral "
                "esencial que participa en más de 300 reacciones enzimáticas del organismo, influyendo "
                "en todo, desde la función muscular y el ritmo cardíaco hasta la salud ósea y el "
                "metabolismo energético.</p>"
                "<p>Esta guía explica qué mide el análisis de magnesio en sangre, los rangos de "
                "referencia que debes conocer, las posibles causas de niveles bajos o altos y cuándo "
                "consultar a tu médico. Nuestro objetivo no es diagnosticar, sino ayudarte a "
                "comprender tus resultados para que tengas una conversación más informada con tu "
                "profesional de salud.</p>"
                "<p>La deficiencia de magnesio es sorprendentemente común en todo el mundo, pero a "
                "menudo pasa desapercibida. Detectarla a tiempo y corregirla mediante la dieta o "
                "suplementación puede prevenir complicaciones graves.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="¿Qué es el magnesio?",
            body_html=(
                "<p>El <strong>magnesio (Mg)</strong> es el cuarto mineral más abundante en el cuerpo "
                "humano. Aproximadamente el 60&nbsp;% se almacena en los huesos, el 39&nbsp;% en "
                "músculos y tejidos blandos, y solo alrededor del 1&nbsp;% circula en la sangre. "
                "Los análisis de sangre miden esta pequeña fracción circulante, por lo que los niveles "
                "séricos pueden parecer normales incluso cuando las reservas tisulares están agotadas.</p>"
                "<p>El magnesio es un nutriente esencial&mdash;el cuerpo no puede sintetizarlo&mdash; "
                "y debe obtenerse a través de los alimentos o suplementos. Las verduras de hoja verde "
                "oscura, los frutos secos, las semillas y los cereales integrales son las fuentes "
                "dietéticas más ricas. La ingesta diaria recomendada es de unos 400&ndash;420&nbsp;mg "
                "para hombres adultos y 310&ndash;320&nbsp;mg para mujeres adultas.</p>"
                "<p>A nivel celular, el magnesio regula el potencial de membrana, apoya la "
                "transmisión nerviosa y forma el complejo activo del ATP (adenosín trifosfato), "
                "la principal moneda energética del organismo. En resumen, prácticamente ningún "
                "proceso bioquímico funciona eficientemente sin magnesio adecuado.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="Papel del magnesio en el cuerpo",
            body_html=(
                "<p>El magnesio actúa como cofactor en <strong>más de 300 reacciones "
                "enzimáticas</strong>. Estas reacciones incluyen la síntesis de proteínas, la "
                "función muscular y nerviosa, la regulación del azúcar en sangre y el control "
                "de la presión arterial. También es esencial para la síntesis de ADN y ARN y "
                "para la división celular.</p>"
                "<p>En el sistema cardiovascular, el magnesio favorece la contracción regular del "
                "músculo cardíaco y ayuda a que las paredes de los vasos sanguíneos se relajen. "
                "Niveles adecuados contribuyen a mantener un ritmo cardíaco saludable; su déficit "
                "aumenta el riesgo de <em>arritmia</em>. Además, el magnesio actúa como regulador "
                "del movimiento de otros electrolitos como el <strong>calcio</strong> y el "
                "<strong>potasio</strong> dentro y fuera de las células.</p>"
                "<p>Para la salud ósea, el magnesio facilita la deposición de calcio en los huesos "
                "y participa en la conversión de la vitamina&nbsp;D a su forma activa. Las "
                "investigaciones sugieren que una ingesta suficiente de magnesio puede reducir el "
                "riesgo de osteoporosis. Además, el magnesio mejora la sensibilidad a la insulina "
                "y puede ayudar a reducir el riesgo de diabetes tipo&nbsp;2.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Rangos de referencia del magnesio",
            body_html=(
                "<p>El magnesio sérico se mide mediante una simple extracción de sangre. La tabla "
                "siguiente muestra los rangos de referencia comúnmente aceptados, aunque los valores "
                "pueden variar ligeramente entre laboratorios.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Estado</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Bajo (Hipomagnesemia)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0,70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,7 &ndash; 2,2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0,70 &ndash; 0,90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,4 &ndash; 1,8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto (Hipermagnesemia)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2,2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0,90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1,8</td>'
                "</tr></tbody></table>"
                "<p>El <strong>rango normal de magnesio sérico es de 1,7&ndash;2,2&nbsp;mg/dL</strong> "
                "(0,70&ndash;0,90&nbsp;mmol/L). Los valores por debajo se denominan "
                "<em>hipomagnesemia</em> y los superiores <em>hipermagnesemia</em>. Comprueba "
                "siempre el rango de referencia específico de tu laboratorio.</p>"
                "<p>Ten en cuenta que el magnesio sérico refleja solo aproximadamente el 1&nbsp;% "
                "de las reservas totales del cuerpo. Algunos médicos pueden solicitar pruebas "
                "adicionales como el magnesio intraeritrocitario o el magnesio en orina de "
                "24&nbsp;horas para evaluar mejor el estado a nivel tisular.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Causas de magnesio bajo (hipomagnesemia)",
            body_html=(
                "<p>Un nivel de magnesio sérico inferior a 1,7&nbsp;mg/dL se clasifica como "
                "<strong>hipomagnesemia</strong>. Las causas más frecuentes son la ingesta "
                "dietética insuficiente, la mala absorción intestinal y las pérdidas renales "
                "excesivas.</p>"
                "<p><strong>Causas principales:</strong> dieta pobre en magnesio, diarrea crónica "
                "o vómitos, síndromes de malabsorción como la enfermedad celíaca y la enfermedad "
                "de Crohn, alcoholismo crónico, diabetes mal controlada (especialmente por poliuria), "
                "uso prolongado de diuréticos (tiazidas y diuréticos de asa) e inhibidores de la "
                "bomba de protones (IBP). El aumento de la demanda durante el embarazo también "
                "puede provocar déficit.</p>"
                "<p>La deficiencia de magnesio coexiste frecuentemente con <strong>hipocalcemia</strong> "
                "e <strong>hipopotasemia</strong>, ya que el magnesio regula la absorción y la "
                "reabsorción renal de estos minerales. Si los niveles de calcio o potasio permanecen "
                "bajos a pesar del tratamiento, debe investigarse un déficit subyacente de magnesio.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Causas de magnesio alto (hipermagnesemia)",
            body_html=(
                "<p>La <strong>hipermagnesemia</strong> se define como un nivel de magnesio sérico "
                "superior a 2,2&nbsp;mg/dL. Es bastante rara en personas con riñones sanos, ya que "
                "estos excretan eficientemente el exceso de magnesio por la orina.</p>"
                "<p>La causa más común es la <strong>insuficiencia renal</strong>. Cuando la tasa de "
                "filtración glomerular disminuye, la excreción de magnesio resulta insuficiente y los "
                "niveles en sangre aumentan. La suplementación excesiva de magnesio, los antiácidos "
                "con magnesio (p.&nbsp;ej., hidróxido de magnesio) y los laxantes también incrementan "
                "el riesgo, especialmente en pacientes con función renal límite.</p>"
                "<p>Causas menos frecuentes incluyen la enfermedad de Addison, el hipotiroidismo, "
                "el uso de litio y la lesión tisular masiva (rabdomiólisis, quemaduras). La "
                "hipermagnesemia grave puede ser potencialmente mortal, causando parálisis "
                "muscular, insuficiencia respiratoria y paro cardíaco. Los pacientes con "
                "enfermedad renal deben tener precaución con los medicamentos y suplementos "
                "que contienen magnesio.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas del desequilibrio de magnesio",
            body_html=(
                "<p><strong>Síntomas de deficiencia:</strong> La deficiencia leve puede ser "
                "asintomática durante mucho tiempo. A medida que progresa, las quejas más comunes "
                "son calambres musculares, fasciculaciones, fatiga crónica, pérdida de apetito y "
                "náuseas. En etapas avanzadas pueden aparecer entumecimiento y hormigueo, "
                "<em>arritmia</em>, cambios de personalidad e incluso convulsiones.</p>"
                "<p>Uno de los retos de la deficiencia de magnesio es que los síntomas suelen "
                "ser inespecíficos; la fatiga y el dolor muscular se solapan con muchas otras "
                "afecciones, lo que facilita pasar por alto el déficit. Por ello se recomienda "
                "el control rutinario de magnesio en personas de alto riesgo (consumo crónico "
                "de alcohol, tratamiento con diuréticos, enfermedades gastrointestinales).</p>"
                "<p><strong>Síntomas de exceso:</strong> Con el avance de la hipermagnesemia "
                "pueden desarrollarse náuseas, vómitos, rubor facial, hipotensión, bradicardia, "
                "pérdida de reflejos tendinosos profundos y debilidad muscular. A niveles muy "
                "altos existe riesgo de depresión respiratoria y paro cardíaco. La toxicidad "
                "por magnesio oral es extremadamente rara en personas con función renal normal; "
                "el riesgo principal surge con la administración intravenosa o la insuficiencia "
                "renal.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Alimentos ricos en magnesio",
            body_html=(
                "<p>La ingesta adecuada de magnesio debe provenir principalmente de una dieta "
                "equilibrada. Los siguientes alimentos se encuentran entre las fuentes más ricas:</p>"
                "<p><strong>Verduras de hoja verde oscura</strong> (espinacas, acelgas, col rizada), "
                "<strong>frutos secos</strong> (almendras, anacardos, cacahuetes), "
                "<strong>semillas</strong> (calabaza, chía, lino), <strong>cereales integrales</strong> "
                "(avena, quinoa, arroz integral), <strong>legumbres</strong> (frijoles negros, "
                "lentejas, garbanzos), <strong>chocolate negro</strong> (70&nbsp;%+ cacao), "
                "<strong>aguacates</strong> y <strong>plátanos</strong>. Una porción de semillas "
                "de calabaza (28&nbsp;g) proporciona aproximadamente 150&nbsp;mg de magnesio, "
                "cubriendo una parte significativa del requerimiento diario.</p>"
                "<p>Los alimentos procesados y los cereales refinados pierden gran parte de su "
                "contenido de magnesio, lo que explica por qué la insuficiencia es frecuente en "
                "dietas occidentales modernas. El agua potable también puede ser una fuente "
                "variable según el contenido mineral local. Si consideras la suplementación, "
                "ten en cuenta que las formas de citrato, glicinato y taurato de magnesio "
                "tienen mayor biodisponibilidad que el óxido de magnesio; consulta siempre "
                "a tu médico antes de empezar cualquier suplemento.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debes acudir al médico?",
            body_html=(
                "<p>Si tu nivel de magnesio está fuera del rango de referencia, o si experimentas "
                "calambres musculares inexplicables, fatiga crónica, palpitaciones o "
                "entumecimiento y hormigueo, te recomendamos consultar a un profesional sanitario. "
                "El seguimiento regular es especialmente importante si tienes antecedentes de "
                "enfermedad renal, diabetes, trastornos gastrointestinales o consumo crónico "
                "de alcohol.</p>"
                "<p>Si tomas medicamentos como diuréticos, IBP o digoxina, tus niveles de "
                "magnesio pueden verse afectados; trabaja con tu médico para establecer un plan "
                "de control periódico. La deficiencia de magnesio no tratada puede provocar "
                "complicaciones graves como arritmias cardíacas, osteoporosis y resistencia "
                "a la insulina.</p>"
                "<p>Asimismo, los pacientes con hipocalcemia o hipopotasemia que no responde al "
                "tratamiento deberían ser evaluados para detectar un déficit subyacente de "
                "magnesio. Si tienes dudas sobre tu nivel de magnesio, plantéaselo a tu médico "
                "de atención primaria o a un endocrinólogo.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Entiende tus análisis de sangre con Norya",
            body_html=(
                "<p><strong>Norya</strong> te permite subir tus resultados de análisis de sangre "
                "y recibir en minutos un informe de salud estructurado y fácil de entender. Tu "
                "magnesio, calcio, potasio y todos los demás parámetros se explican en un lenguaje "
                "claro, preparándote para una consulta médica más productiva.</p>"
                "<p>Sube tu informe, descubre qué significan tus resultados y genera un resumen "
                "que puedas compartir con tu médico en pocos minutos. "
                '<a href="/analyze">Inicia tu análisis con Norya</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico '
                'médico.</strong> Consulte siempre sus resultados con un profesional sanitario. '
                '<a href="/analyze">Iniciar análisis con Norya</a></p>'
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
            heading="Magnesium-Bluttest: Was Ihre Ergebnisse bedeuten",
            body_html=(
                "<p>Wenn Sie auf Ihrem Blutbild den <strong>Magnesium</strong>-Wert sehen, fragen "
                "Sie sich natürlich, was diese Zahl über Ihre Gesundheit aussagt. Magnesium ist ein "
                "essenzieller Mineralstoff, der an mehr als 300 enzymatischen Reaktionen im Körper "
                "beteiligt ist und alles beeinflusst – von der Muskelfunktion und dem Herzrhythmus "
                "bis hin zur Knochengesundheit und zum Energiestoffwechsel.</p>"
                "<p>Dieser Leitfaden erklärt, was ein Magnesium-Bluttest misst, welche "
                "Referenzbereiche gelten, welche Ursachen niedrige oder hohe Werte haben können "
                "und wann Sie einen Arzt aufsuchen sollten. Unser Ziel ist keine Diagnosestellung, "
                "sondern Ihnen zu helfen, Ihre Ergebnisse besser zu verstehen, damit Sie ein "
                "informierteres Gespräch mit Ihrem Arzt führen können.</p>"
                "<p>Magnesiummangel ist weltweit überraschend häufig und wird dennoch oft übersehen. "
                "Eine frühzeitige Erkennung und Korrektur durch Ernährung oder Nahrungsergänzung "
                "kann schwerwiegende gesundheitliche Komplikationen verhindern.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="Was ist Magnesium?",
            body_html=(
                "<p><strong>Magnesium (Mg)</strong> ist das vierthäufigste Mineral im menschlichen "
                "Körper. Etwa 60&nbsp;% des Magnesiums befinden sich in den Knochen, 39&nbsp;% in "
                "Muskeln und Weichgeweben und nur rund 1&nbsp;% zirkuliert im Blut. Bluttests "
                "messen diesen kleinen zirkulierenden Anteil, sodass die Serumwerte normal "
                "erscheinen können, obwohl die Gewebespeicher erschöpft sind.</p>"
                "<p>Magnesium ist ein essenzieller Nährstoff – der Körper kann es nicht selbst "
                "herstellen – und muss über die Nahrung oder Nahrungsergänzungsmittel aufgenommen "
                "werden. Dunkelgrünes Blattgemüse, Nüsse, Samen und Vollkornprodukte gehören zu "
                "den reichhaltigsten Quellen. Die empfohlene tägliche Zufuhr liegt bei etwa "
                "400&ndash;420&nbsp;mg für erwachsene Männer und 310&ndash;320&nbsp;mg für "
                "erwachsene Frauen.</p>"
                "<p>Auf zellulärer Ebene reguliert Magnesium das Membranpotenzial, unterstützt "
                "die Nervenübertragung und bildet den aktiven ATP-Komplex (Adenosintriphosphat) "
                "– die primäre Energiewährung des Körpers. Kurz gesagt: Fast kein biochemischer "
                "Prozess im Körper läuft ohne ausreichend Magnesium effizient ab.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="Rolle von Magnesium im Körper",
            body_html=(
                "<p>Magnesium dient als Cofaktor in <strong>über 300 Enzymreaktionen</strong>. "
                "Dazu gehören die Proteinsynthese, die Muskel- und Nervenfunktion, die "
                "Blutzuckerregulierung und die Blutdruckkontrolle. Es ist außerdem für die "
                "DNA- und RNA-Synthese sowie die Zellteilung unerlässlich.</p>"
                "<p>Im Herz-Kreislauf-System unterstützt Magnesium die regelmäßige Kontraktion "
                "des Herzmuskels und hilft den Blutgefäßwänden, sich zu entspannen. Ein "
                "ausreichender Magnesiumspiegel trägt zur Aufrechterhaltung eines gesunden "
                "Herzrhythmus bei; ein Mangel erhöht das Risiko für <em>Arrhythmien</em>. "
                "Magnesium fungiert außerdem als Türhüter für andere Elektrolyte wie "
                "<strong>Kalzium</strong> und <strong>Kalium</strong> und reguliert deren "
                "Transport in und aus den Zellen.</p>"
                "<p>Für die Knochengesundheit erleichtert Magnesium die Kalziumeinlagerung in "
                "den Knochen und spielt eine Rolle bei der Umwandlung von Vitamin&nbsp;D in "
                "seine aktive Form. Studien deuten darauf hin, dass eine ausreichende "
                "Magnesiumzufuhr das Osteoporoserisiko senken kann. Darüber hinaus verbessert "
                "Magnesium die Insulinsensitivität und kann das Risiko für Typ-2-Diabetes "
                "verringern.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Magnesium-Referenzbereiche",
            body_html=(
                "<p>Der Magnesiumspiegel im Serum wird durch eine einfache Blutabnahme bestimmt. "
                "Die folgende Tabelle zeigt die allgemein anerkannten Referenzbereiche; die Werte "
                "können jedoch je nach Labor leicht variieren.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Status</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Niedrig (Hypomagnesiämie)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0,70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,7 &ndash; 2,2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0,70 &ndash; 0,90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,4 &ndash; 1,8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Hoch (Hypermagnesiämie)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2,2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0,90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1,8</td>'
                "</tr></tbody></table>"
                "<p>Der <strong>normale Serummagnesiumbereich liegt bei 1,7&ndash;2,2&nbsp;mg/dL</strong> "
                "(0,70&ndash;0,90&nbsp;mmol/L). Werte unterhalb dieses Bereichs werden als "
                "<em>Hypomagnesiämie</em> bezeichnet, Werte darüber als <em>Hypermagnesiämie</em>. "
                "Beachten Sie immer den spezifischen Referenzbereich Ihres Labors.</p>"
                "<p>Bedenken Sie, dass das Serummagnesium nur etwa 1&nbsp;% des gesamten "
                "Körpermagnesiums widerspiegelt. Einige Ärzte veranlassen daher zusätzliche Tests "
                "wie Erythrozyten-Magnesium oder 24-Stunden-Urin-Magnesium, um den Status auf "
                "Gewebeebene besser einzuschätzen.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Ursachen für niedrigen Magnesiumspiegel (Hypomagnesiämie)",
            body_html=(
                "<p>Ein Serummagnesiumspiegel unter 1,7&nbsp;mg/dL wird als "
                "<strong>Hypomagnesiämie</strong> eingestuft. Die häufigsten Ursachen sind eine "
                "unzureichende Nahrungsaufnahme, eine gestörte Darmresorption und ein übermäßiger "
                "renaler Verlust.</p>"
                "<p><strong>Hauptursachen:</strong> magnesiumarme Ernährung, chronischer Durchfall "
                "oder Erbrechen, Malabsorptionssyndrome wie Zöliakie und Morbus Crohn, chronischer "
                "Alkoholismus, schlecht eingestellter Diabetes (insbesondere durch Polyurie), "
                "langfristige Einnahme von Diuretika (Thiazide und Schleifendiuretika) sowie "
                "Protonenpumpenhemmer (PPI). Auch der erhöhte Bedarf in der Schwangerschaft "
                "kann zu einem Mangel führen.</p>"
                "<p>Magnesiummangel tritt häufig zusammen mit <strong>Hypokalzämie</strong> und "
                "<strong>Hypokaliämie</strong> auf, da Magnesium die Aufnahme und renale "
                "Rückresorption dieser Mineralstoffe reguliert. Wenn Kalzium- oder Kaliumwerte "
                "trotz Behandlung niedrig bleiben, sollte ein zugrunde liegender "
                "Magnesiummangel abgeklärt werden.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Ursachen für hohen Magnesiumspiegel (Hypermagnesiämie)",
            body_html=(
                "<p><strong>Hypermagnesiämie</strong> liegt vor, wenn der Serummagnesiumwert "
                "über 2,2&nbsp;mg/dL steigt. Bei Personen mit gesunden Nieren ist sie sehr selten, "
                "da die Nieren überschüssiges Magnesium effizient über den Urin ausscheiden.</p>"
                "<p>Die häufigste Ursache ist <strong>Nierenversagen</strong>. Bei abnehmender "
                "glomerulärer Filtrationsrate reicht die Magnesiumausscheidung nicht mehr aus "
                "und der Blutspiegel steigt. Übermäßige Magnesiumsupplementierung, "
                "magnesiumhaltige Antazida (z.&nbsp;B. Magnesiumhydroxid) und Laxantien "
                "erhöhen ebenfalls das Risiko, insbesondere bei Patienten mit eingeschränkter "
                "Nierenfunktion.</p>"
                "<p>Seltenere Ursachen umfassen Morbus Addison, Hypothyreose, Lithiumeinnahme "
                "und massive Gewebeschäden (Rhabdomyolyse, Verbrennungen). Schwere "
                "Hypermagnesiämie kann lebensbedrohlich sein und Muskellähmung, Atemversagen "
                "und Herzstillstand verursachen. Patienten mit Nierenerkrankung sollten bei "
                "magnesiumhaltigen Medikamenten und Nahrungsergänzungsmitteln Vorsicht "
                "walten lassen.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome eines Magnesium-Ungleichgewichts",
            body_html=(
                "<p><strong>Mangelsymptome:</strong> Ein leichter Magnesiummangel kann lange "
                "asymptomatisch bleiben. Bei Fortschreiten sind die häufigsten Beschwerden "
                "Muskelkrämpfe, Zuckungen, chronische Müdigkeit, Appetitlosigkeit und Übelkeit. "
                "In fortgeschrittenen Stadien können Taubheitsgefühl und Kribbeln, "
                "<em>Arrhythmien</em>, Persönlichkeitsveränderungen und sogar Krampfanfälle "
                "auftreten.</p>"
                "<p>Eine Herausforderung beim Magnesiummangel ist, dass die Symptome oft "
                "unspezifisch sind; Müdigkeit und Muskelschmerzen überschneiden sich mit vielen "
                "anderen Erkrankungen, sodass ein Mangel leicht übersehen wird. Daher wird eine "
                "routinemäßige Magnesiumkontrolle bei Risikopersonen empfohlen (chronischer "
                "Alkoholkonsum, Diuretikatherapie, gastrointestinale Erkrankungen).</p>"
                "<p><strong>Symptome eines Überschusses:</strong> Bei zunehmender "
                "Hypermagnesiämie können Übelkeit, Erbrechen, Gesichtsrötung, niedriger "
                "Blutdruck, Bradykardie, Verlust der tiefen Sehnenreflexe und Muskelschwäche "
                "auftreten. Bei sehr hohen Spiegeln besteht die Gefahr einer Atemdepression "
                "und eines Herzstillstands. Eine Toxizität durch orale Magnesiumzufuhr allein "
                "ist bei Personen mit normaler Nierenfunktion äußerst selten; das Hauptrisiko "
                "besteht bei intravenöser Gabe oder Niereninsuffizienz.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Magnesiumreiche Lebensmittel",
            body_html=(
                "<p>Eine ausreichende Magnesiumzufuhr sollte in erster Linie über eine "
                "ausgewogene Ernährung erfolgen. Folgende Lebensmittel gehören zu den "
                "reichhaltigsten Quellen:</p>"
                "<p><strong>Dunkelgrünes Blattgemüse</strong> (Spinat, Mangold, Grünkohl), "
                "<strong>Nüsse</strong> (Mandeln, Cashews, Erdnüsse), <strong>Samen</strong> "
                "(Kürbiskerne, Chiasamen, Leinsamen), <strong>Vollkornprodukte</strong> "
                "(Hafer, Quinoa, brauner Reis), <strong>Hülsenfrüchte</strong> (schwarze "
                "Bohnen, Linsen, Kichererbsen), <strong>dunkle Schokolade</strong> "
                "(70&nbsp;%+ Kakao), <strong>Avocados</strong> und <strong>Bananen</strong>. "
                "Eine Portion Kürbiskerne (28&nbsp;g) liefert etwa 150&nbsp;mg Magnesium "
                "und deckt damit einen erheblichen Teil des Tagesbedarfs.</p>"
                "<p>Verarbeitete Lebensmittel und raffinierte Getreideprodukte verlieren "
                "einen Großteil ihres Magnesiumgehalts, weshalb ein Magnesiummangel in der "
                "modernen westlichen Ernährung verbreitet ist. Auch das Trinkwasser kann je "
                "nach lokalem Mineralgehalt eine variable Quelle sein. Falls Sie eine "
                "Supplementierung in Betracht ziehen, beachten Sie, dass Magnesiumcitrat, "
                "-glycinat und -taurat eine höhere Bioverfügbarkeit als Magnesiumoxid "
                "aufweisen; sprechen Sie immer zuerst mit Ihrem Arzt.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Wenn Ihr Magnesiumspiegel außerhalb des Referenzbereichs liegt oder "
                "Sie unter unerklärlichen Muskelkrämpfen, chronischer Müdigkeit, "
                "Herzrhythmusstörungen oder Taubheitsgefühl und Kribbeln leiden, "
                "empfehlen wir Ihnen, einen Arzt aufzusuchen. Regelmäßige Kontrollen "
                "sind besonders wichtig bei Nierenerkrankungen, Diabetes, Magen-Darm-"
                "Erkrankungen oder chronischem Alkoholkonsum in der Vorgeschichte.</p>"
                "<p>Wenn Sie Medikamente wie Diuretika, PPI oder Digoxin einnehmen, "
                "können Ihre Magnesiumwerte beeinflusst werden; erstellen Sie gemeinsam "
                "mit Ihrem Arzt einen Kontrollplan. Unbehandelter Magnesiummangel kann "
                "zu schwerwiegenden Komplikationen wie Herzrhythmusstörungen, Osteoporose "
                "und Insulinresistenz führen.</p>"
                "<p>Auch Patienten mit Hypokalzämie oder Hypokaliämie, die nicht auf die "
                "Behandlung ansprechen, sollten auf einen zugrunde liegenden Magnesiummangel "
                "untersucht werden. Wenn Sie Bedenken bezüglich Ihres Magnesiumspiegels "
                "haben, besprechen Sie Ihre Blutergebnisse mit einem Internisten oder "
                "Endokrinologen.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Verstehen Sie Ihre Blutwerte mit Norya",
            body_html=(
                "<p><strong>Norya</strong> ermöglicht es Ihnen, Ihre Blutergebnisse hochzuladen "
                "und innerhalb weniger Minuten einen strukturierten, leicht verständlichen "
                "Gesundheitsbericht zu erhalten. Ihr Magnesium, Kalzium, Kalium und alle "
                "weiteren Parameter werden in klarer Sprache erklärt und bereiten Sie auf "
                "einen produktiven Arztbesuch vor.</p>"
                "<p>Laden Sie Ihren Befund hoch, erfahren Sie, was Ihre Ergebnisse bedeuten, "
                "und erstellen Sie in wenigen Minuten eine Zusammenfassung für Ihren Arzt. "
                '<a href="/analyze">Analyse mit Norya starten</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine '
                'ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse '
                'immer mit einem Arzt. <a href="/analyze">Analyse mit Norya starten</a></p>'
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
            heading="Analyse sanguine du magnésium : que signifient vos résultats ?",
            body_html=(
                "<p>Lorsque vous voyez la valeur du <strong>magnésium</strong> sur votre bilan "
                "sanguin, il est naturel de se demander ce que ce chiffre dit de votre santé. Le "
                "magnésium est un minéral essentiel impliqué dans plus de 300 réactions enzymatiques "
                "de l&rsquo;organisme, influençant aussi bien la fonction musculaire et le rythme "
                "cardiaque que la santé osseuse et le métabolisme énergétique.</p>"
                "<p>Ce guide explique ce que mesure l&rsquo;analyse sanguine du magnésium, les "
                "valeurs de référence à connaître, les causes possibles de taux bas ou élevés et "
                "quand consulter votre médecin. Notre objectif n&rsquo;est pas de poser un "
                "diagnostic, mais de vous aider à comprendre vos résultats afin d&rsquo;avoir "
                "un échange plus éclairé avec votre professionnel de santé.</p>"
                "<p>La carence en magnésium est étonnamment fréquente dans le monde entier mais "
                "reste souvent méconnue. La détecter tôt et la corriger par l&rsquo;alimentation "
                "ou la supplémentation peut prévenir de graves complications.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="Qu&rsquo;est-ce que le magnésium ?",
            body_html=(
                "<p>Le <strong>magnésium (Mg)</strong> est le quatrième minéral le plus abondant "
                "dans le corps humain. Environ 60&nbsp;% se trouvent dans les os, 39&nbsp;% dans "
                "les muscles et tissus mous, et seul 1&nbsp;% environ circule dans le sang. "
                "L&rsquo;analyse sanguine mesure cette petite fraction circulante ; les taux "
                "sériques peuvent donc sembler normaux même si les réserves tissulaires sont "
                "épuisées.</p>"
                "<p>Le magnésium est un nutriment essentiel &mdash; l&rsquo;organisme ne peut pas "
                "le synthétiser &mdash; et doit être apporté par l&rsquo;alimentation ou les "
                "compléments. Les légumes à feuilles vert foncé, les noix, les graines et les "
                "céréales complètes figurent parmi les sources les plus riches. L&rsquo;apport "
                "journalier recommandé est d&rsquo;environ 400&ndash;420&nbsp;mg pour les hommes "
                "et 310&ndash;320&nbsp;mg pour les femmes.</p>"
                "<p>Au niveau cellulaire, le magnésium régule le potentiel membranaire, soutient "
                "la transmission nerveuse et forme le complexe actif de l&rsquo;ATP (adénosine "
                "triphosphate), la principale monnaie énergétique de l&rsquo;organisme. En bref, "
                "pratiquement aucun processus biochimique ne fonctionne efficacement sans un "
                "apport adéquat en magnésium.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="Rôle du magnésium dans l&rsquo;organisme",
            body_html=(
                "<p>Le magnésium agit comme cofacteur dans <strong>plus de 300 réactions "
                "enzymatiques</strong>. Ces réactions incluent la synthèse des protéines, la "
                "fonction musculaire et nerveuse, la régulation de la glycémie et le contrôle "
                "de la pression artérielle. Il est également essentiel à la synthèse de l&rsquo;ADN "
                "et de l&rsquo;ARN ainsi qu&rsquo;à la division cellulaire.</p>"
                "<p>Dans le système cardiovasculaire, le magnésium favorise la contraction régulière "
                "du muscle cardiaque et aide les parois vasculaires à se relâcher. Des taux "
                "adéquats contribuent au maintien d&rsquo;un rythme cardiaque sain ; une carence "
                "augmente le risque d&rsquo;<em>arythmie</em>. Le magnésium joue aussi le rôle "
                "de gardien pour d&rsquo;autres électrolytes tels que le <strong>calcium</strong> "
                "et le <strong>potassium</strong>, régulant leur passage à travers les membranes "
                "cellulaires.</p>"
                "<p>Pour la santé osseuse, le magnésium facilite le dépôt de calcium dans les os "
                "et intervient dans la conversion de la vitamine&nbsp;D en sa forme active. Les "
                "recherches suggèrent qu&rsquo;un apport suffisant en magnésium peut réduire le "
                "risque d&rsquo;ostéoporose. Par ailleurs, le magnésium améliore la sensibilité "
                "à l&rsquo;insuline et peut contribuer à diminuer le risque de diabète de "
                "type&nbsp;2.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs de référence du magnésium",
            body_html=(
                "<p>Le magnésium sérique est mesuré par une simple prise de sang. Le tableau "
                "ci-dessous présente les valeurs de référence communément admises ; les chiffres "
                "peuvent toutefois varier légèrement d&rsquo;un laboratoire à l&rsquo;autre.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">État</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Bas (Hypomagnésémie)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0,70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normal</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,7 &ndash; 2,2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0,70 &ndash; 0,90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,4 &ndash; 1,8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Élevé (Hypermagnésémie)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2,2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0,90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1,8</td>'
                "</tr></tbody></table>"
                "<p>La <strong>plage normale du magnésium sérique est de 1,7&ndash;2,2&nbsp;mg/dL</strong> "
                "(0,70&ndash;0,90&nbsp;mmol/L). Les valeurs inférieures sont appelées "
                "<em>hypomagnésémie</em> et les valeurs supérieures <em>hypermagnésémie</em>. "
                "Vérifiez toujours la plage de référence indiquée sur votre compte-rendu de "
                "laboratoire.</p>"
                "<p>N&rsquo;oubliez pas que le magnésium sérique ne reflète qu&rsquo;environ "
                "1&nbsp;% des réserves totales de l&rsquo;organisme. Certains médecins peuvent "
                "prescrire des tests complémentaires comme le magnésium intra-érythrocytaire ou "
                "le magnésium urinaire des 24&nbsp;heures pour mieux évaluer le statut tissulaire.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Causes d&rsquo;un magnésium bas (hypomagnésémie)",
            body_html=(
                "<p>Un taux de magnésium sérique inférieur à 1,7&nbsp;mg/dL est classé comme "
                "<strong>hypomagnésémie</strong>. Les causes les plus fréquentes sont un apport "
                "alimentaire insuffisant, une mauvaise absorption intestinale et des pertes "
                "rénales excessives.</p>"
                "<p><strong>Causes principales :</strong> alimentation pauvre en magnésium, "
                "diarrhée chronique ou vomissements, syndromes de malabsorption comme la maladie "
                "cœliaque et la maladie de Crohn, alcoolisme chronique, diabète mal contrôlé "
                "(notamment en raison de la polyurie), prise prolongée de diurétiques (thiazidiques "
                "et de l&rsquo;anse) et d&rsquo;inhibiteurs de la pompe à protons (IPP). Les "
                "besoins accrus pendant la grossesse peuvent aussi entraîner un déficit.</p>"
                "<p>La carence en magnésium coexiste fréquemment avec une "
                "<strong>hypocalcémie</strong> et une <strong>hypokaliémie</strong>, car le "
                "magnésium régule l&rsquo;absorption et la réabsorption rénale de ces minéraux. "
                "Si les taux de calcium ou de potassium restent bas malgré le traitement, un "
                "déficit en magnésium sous-jacent doit être recherché.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Causes d&rsquo;un magnésium élevé (hypermagnésémie)",
            body_html=(
                "<p>L&rsquo;<strong>hypermagnésémie</strong> est définie par un taux de magnésium "
                "sérique supérieur à 2,2&nbsp;mg/dL. Elle est assez rare chez les personnes dont "
                "les reins fonctionnent normalement, car ceux-ci excrètent efficacement "
                "l&rsquo;excès de magnésium dans l&rsquo;urine.</p>"
                "<p>La cause la plus courante est l&rsquo;<strong>insuffisance rénale</strong>. "
                "Lorsque le débit de filtration glomérulaire diminue, l&rsquo;excrétion du "
                "magnésium devient insuffisante et les taux sanguins augmentent. Une "
                "supplémentation excessive en magnésium, les antiacides contenant du magnésium "
                "(p.&nbsp;ex. hydroxyde de magnésium) et les laxatifs augmentent également le "
                "risque, surtout chez les patients dont la fonction rénale est limite.</p>"
                "<p>Parmi les causes plus rares figurent la maladie d&rsquo;Addison, "
                "l&rsquo;hypothyroïdie, l&rsquo;utilisation du lithium et les lésions "
                "tissulaires massives (rhabdomyolyse, brûlures). Une hypermagnésémie sévère "
                "peut être mortelle, provoquant une paralysie musculaire, une insuffisance "
                "respiratoire et un arrêt cardiaque. Les patients atteints d&rsquo;une "
                "maladie rénale doivent faire preuve de prudence avec les médicaments et "
                "compléments contenant du magnésium.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes d&rsquo;un déséquilibre en magnésium",
            body_html=(
                "<p><strong>Symptômes de carence :</strong> Une carence légère peut rester "
                "asymptomatique pendant longtemps. À mesure qu&rsquo;elle progresse, les plaintes "
                "les plus courantes sont les crampes musculaires, les fasciculations, la fatigue "
                "chronique, la perte d&rsquo;appétit et les nausées. À un stade avancé, des "
                "engourdissements, des picotements, une <em>arythmie</em>, des changements de "
                "personnalité et même des convulsions peuvent apparaître.</p>"
                "<p>L&rsquo;un des défis de la carence en magnésium est que les symptômes sont "
                "souvent non spécifiques ; la fatigue et les douleurs musculaires se recoupent "
                "avec de nombreuses autres affections, ce qui facilite le passage à côté du "
                "déficit. C&rsquo;est pourquoi un contrôle de routine est recommandé chez les "
                "personnes à risque (consommation chronique d&rsquo;alcool, traitement par "
                "diurétiques, maladies gastro-intestinales).</p>"
                "<p><strong>Symptômes d&rsquo;excès :</strong> Avec l&rsquo;aggravation de "
                "l&rsquo;hypermagnésémie, des nausées, vomissements, rougeurs du visage, "
                "hypotension, bradycardie, perte des réflexes ostéotendineux et faiblesse "
                "musculaire peuvent se développer. À des taux très élevés, une dépression "
                "respiratoire et un arrêt cardiaque sont possibles. La toxicité par voie "
                "orale est extrêmement rare chez les personnes dont la fonction rénale est "
                "normale ; le risque principal provient de l&rsquo;administration intraveineuse "
                "ou de l&rsquo;insuffisance rénale.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Aliments riches en magnésium",
            body_html=(
                "<p>Un apport adéquat en magnésium doit provenir en priorité d&rsquo;une "
                "alimentation équilibrée. Voici les aliments parmi les plus riches en "
                "magnésium :</p>"
                "<p><strong>Légumes à feuilles vert foncé</strong> (épinards, blettes, chou "
                "frisé), <strong>noix</strong> (amandes, noix de cajou, cacahuètes), "
                "<strong>graines</strong> (courge, chia, lin), <strong>céréales complètes</strong> "
                "(avoine, quinoa, riz complet), <strong>légumineuses</strong> (haricots noirs, "
                "lentilles, pois chiches), <strong>chocolat noir</strong> (70&nbsp;%+ cacao), "
                "<strong>avocats</strong> et <strong>bananes</strong>. Une portion de graines "
                "de courge (28&nbsp;g) fournit environ 150&nbsp;mg de magnésium, couvrant une "
                "part significative des besoins quotidiens.</p>"
                "<p>Les aliments transformés et les céréales raffinées perdent une grande partie "
                "de leur magnésium, ce qui explique la fréquence de l&rsquo;insuffisance dans "
                "les régimes occidentaux modernes. L&rsquo;eau potable peut également constituer "
                "une source variable selon la teneur minérale locale. Si vous envisagez une "
                "supplémentation, sachez que le citrate, le glycinate et le taurate de magnésium "
                "ont une meilleure biodisponibilité que l&rsquo;oxyde de magnésium ; consultez "
                "toujours votre médecin avant de commencer un complément.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Si votre taux de magnésium se situe en dehors de la plage de référence, "
                "ou si vous présentez des crampes musculaires inexpliquées, une fatigue "
                "chronique, des palpitations ou des engourdissements et picotements, nous "
                "vous recommandons de consulter un professionnel de santé. Un suivi régulier "
                "est particulièrement important si vous avez des antécédents de maladie rénale, "
                "de diabète, de troubles gastro-intestinaux ou de consommation chronique "
                "d&rsquo;alcool.</p>"
                "<p>Si vous prenez des médicaments tels que des diurétiques, des IPP ou de "
                "la digoxine, vos taux de magnésium peuvent être affectés ; établissez avec "
                "votre médecin un plan de surveillance régulier. Une carence en magnésium non "
                "traitée peut entraîner des complications graves telles que des arythmies "
                "cardiaques, l&rsquo;ostéoporose et la résistance à l&rsquo;insuline.</p>"
                "<p>Par ailleurs, les patients souffrant d&rsquo;hypocalcémie ou "
                "d&rsquo;hypokaliémie ne répondant pas au traitement devraient être évalués "
                "pour un éventuel déficit en magnésium sous-jacent. Si vous avez des "
                "préoccupations concernant votre taux de magnésium, discutez de vos résultats "
                "avec un interniste ou un endocrinologue.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comprenez vos analyses de sang avec Norya",
            body_html=(
                "<p><strong>Norya</strong> vous permet de télécharger vos résultats d&rsquo;analyses "
                "sanguines et de recevoir en quelques minutes un rapport de santé structuré et "
                "facile à comprendre. Votre magnésium, calcium, potassium et tous les autres "
                "paramètres sont expliqués dans un langage clair, vous préparant à une "
                "consultation médicale plus productive.</p>"
                "<p>Téléchargez votre bilan, découvrez ce que vos résultats signifient et "
                "générez un résumé à partager avec votre médecin en quelques minutes. "
                '<a href="/analyze">Commencer l&rsquo;analyse avec Norya</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace '
                'pas un avis ou un diagnostic médical.</strong> Discutez toujours de vos '
                'résultats avec un professionnel de santé. '
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
            heading="Analisi del magnesio nel sangue: cosa significano i tuoi risultati",
            body_html=(
                "<p>Quando vedi il valore del <strong>magnesio</strong> nel tuo referto del sangue, "
                "è naturale chiedersi cosa significhi quel numero per la tua salute. Il magnesio "
                "è un minerale essenziale coinvolto in oltre 300 reazioni enzimatiche "
                "dell&rsquo;organismo, influenzando la funzione muscolare, il ritmo cardiaco, "
                "la salute delle ossa e il metabolismo energetico.</p>"
                "<p>Questa guida spiega cosa misura l&rsquo;analisi del magnesio nel sangue, "
                "i range di riferimento da conoscere, le possibili cause di livelli bassi o "
                "alti e quando consultare il medico. Il nostro obiettivo non è fare diagnosi, "
                "ma aiutarti a comprendere i tuoi risultati per avere un confronto più "
                "consapevole con il tuo professionista sanitario.</p>"
                "<p>La carenza di magnesio è sorprendentemente comune in tutto il mondo eppure "
                "spesso viene trascurata. Individuarla precocemente e correggerla tramite "
                "l&rsquo;alimentazione o l&rsquo;integrazione può prevenire complicazioni "
                "gravi.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="Cos&rsquo;è il magnesio?",
            body_html=(
                "<p>Il <strong>magnesio (Mg)</strong> è il quarto minerale più abbondante nel "
                "corpo umano. Circa il 60&nbsp;% è immagazzinato nelle ossa, il 39&nbsp;% nei "
                "muscoli e nei tessuti molli e solo l&rsquo;1&nbsp;% circa circola nel sangue. "
                "Le analisi del sangue misurano questa piccola frazione circolante, per cui i "
                "livelli sierici possono apparire normali anche quando le riserve tissutali "
                "sono esaurite.</p>"
                "<p>Il magnesio è un nutriente essenziale&mdash;il corpo non può sintetizzarlo"
                "&mdash;e deve essere assunto attraverso gli alimenti o gli integratori. Le "
                "verdure a foglia verde scuro, la frutta secca, i semi e i cereali integrali "
                "sono tra le fonti più ricche. L&rsquo;assunzione giornaliera raccomandata è "
                "di circa 400&ndash;420&nbsp;mg per gli uomini adulti e 310&ndash;320&nbsp;mg "
                "per le donne adulte.</p>"
                "<p>A livello cellulare, il magnesio regola il potenziale di membrana, supporta "
                "la trasmissione nervosa e forma il complesso attivo dell&rsquo;ATP (adenosina "
                "trifosfato), la principale valuta energetica dell&rsquo;organismo. In sintesi, "
                "praticamente nessun processo biochimico funziona in modo efficiente senza un "
                "adeguato apporto di magnesio.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="Ruolo del magnesio nell&rsquo;organismo",
            body_html=(
                "<p>Il magnesio funge da cofattore in <strong>oltre 300 reazioni "
                "enzimatiche</strong>. Queste reazioni comprendono la sintesi proteica, la "
                "funzione muscolare e nervosa, la regolazione della glicemia e il controllo "
                "della pressione arteriosa. È inoltre essenziale per la sintesi di DNA e RNA "
                "e per la divisione cellulare.</p>"
                "<p>Nel sistema cardiovascolare, il magnesio favorisce la contrazione regolare "
                "del muscolo cardiaco e aiuta le pareti vascolari a rilassarsi. Livelli "
                "adeguati contribuiscono a mantenere un ritmo cardiaco sano; la carenza "
                "aumenta il rischio di <em>aritmia</em>. Il magnesio agisce inoltre come "
                "guardiano di altri elettroliti quali <strong>calcio</strong> e "
                "<strong>potassio</strong>, regolandone il passaggio attraverso le membrane "
                "cellulari.</p>"
                "<p>Per la salute delle ossa, il magnesio facilita la deposizione di calcio "
                "nelle ossa e partecipa alla conversione della vitamina&nbsp;D nella sua forma "
                "attiva. Le ricerche suggeriscono che un apporto sufficiente di magnesio possa "
                "ridurre il rischio di osteoporosi. Inoltre, il magnesio migliora la sensibilità "
                "all&rsquo;insulina e può contribuire a ridurre il rischio di diabete di "
                "tipo&nbsp;2.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori di riferimento del magnesio",
            body_html=(
                "<p>Il magnesio sierico viene misurato con un semplice prelievo di sangue. "
                "La tabella seguente mostra i range di riferimento comunemente accettati, "
                "sebbene i valori possano variare leggermente tra i laboratori.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Stato</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Basso (Ipomagnesiemia)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0,70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>Normale</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,7 &ndash; 2,2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0,70 &ndash; 0,90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1,4 &ndash; 1,8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Alto (Ipermagnesiemia)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2,2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0,90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1,8</td>'
                "</tr></tbody></table>"
                "<p>Il <strong>range normale del magnesio sierico è 1,7&ndash;2,2&nbsp;mg/dL</strong> "
                "(0,70&ndash;0,90&nbsp;mmol/L). Valori al di sotto sono definiti "
                "<em>ipomagnesiemia</em>, quelli al di sopra <em>ipermagnesiemia</em>. "
                "Verificate sempre il range di riferimento specifico del vostro laboratorio.</p>"
                "<p>Ricordate che il magnesio sierico riflette solo circa l&rsquo;1&nbsp;% "
                "delle riserve totali dell&rsquo;organismo. Alcuni medici possono richiedere "
                "esami aggiuntivi come il magnesio eritrocitario o il magnesio urinario delle "
                "24&nbsp;ore per valutare meglio lo stato a livello tissutale.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="Cause del magnesio basso (ipomagnesiemia)",
            body_html=(
                "<p>Un livello di magnesio sierico inferiore a 1,7&nbsp;mg/dL è classificato "
                "come <strong>ipomagnesiemia</strong>. Le cause più comuni includono un apporto "
                "alimentare insufficiente, un malassorbimento intestinale e perdite renali "
                "eccessive.</p>"
                "<p><strong>Cause principali:</strong> dieta povera di magnesio, diarrea cronica "
                "o vomito, sindromi da malassorbimento come celiachia e morbo di Crohn, "
                "alcolismo cronico, diabete scarsamente controllato (in particolare per la "
                "poliuria), uso prolungato di diuretici (tiazidici e dell&rsquo;ansa) e "
                "inibitori di pompa protonica (IPP). L&rsquo;aumento del fabbisogno durante "
                "la gravidanza può anch&rsquo;esso portare a un deficit.</p>"
                "<p>La carenza di magnesio coesiste spesso con <strong>ipocalcemia</strong> e "
                "<strong>ipokaliemia</strong>, poiché il magnesio regola l&rsquo;assorbimento "
                "e il riassorbimento renale di questi minerali. Se i livelli di calcio o potassio "
                "restano bassi nonostante il trattamento, dovrebbe essere indagato un deficit "
                "di magnesio sottostante.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="Cause del magnesio alto (ipermagnesiemia)",
            body_html=(
                "<p>L&rsquo;<strong>ipermagnesiemia</strong> è definita da un livello di magnesio "
                "sierico superiore a 2,2&nbsp;mg/dL. È piuttosto rara in soggetti con reni sani, "
                "poiché i reni eliminano efficacemente l&rsquo;eccesso di magnesio nelle urine.</p>"
                "<p>La causa più comune è l&rsquo;<strong>insufficienza renale</strong>. Quando "
                "la velocità di filtrazione glomerulare diminuisce, l&rsquo;escrezione di "
                "magnesio diventa insufficiente e i livelli ematici aumentano. "
                "L&rsquo;integrazione eccessiva di magnesio, gli antiacidi contenenti magnesio "
                "(ad es. idrossido di magnesio) e i lassativi aumentano anch&rsquo;essi il "
                "rischio, soprattutto nei pazienti con funzionalità renale ai limiti.</p>"
                "<p>Cause meno comuni includono la malattia di Addison, l&rsquo;ipotiroidismo, "
                "l&rsquo;uso di litio e il danno tissutale massivo (rabdomiolisi, ustioni). "
                "Un&rsquo;ipermagnesiemia grave può essere pericolosa per la vita, causando "
                "paralisi muscolare, insufficienza respiratoria e arresto cardiaco. I pazienti "
                "con malattia renale dovrebbero prestare attenzione ai farmaci e integratori "
                "contenenti magnesio.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi dello squilibrio di magnesio",
            body_html=(
                "<p><strong>Sintomi da carenza:</strong> Una carenza lieve può rimanere "
                "asintomatica a lungo. Con il progredire, i disturbi più comuni sono crampi "
                "muscolari, fascicolazioni, stanchezza cronica, perdita di appetito e nausea. "
                "Negli stadi avanzati possono comparire intorpidimento e formicolio, "
                "<em>aritmia</em>, cambiamenti della personalità e persino convulsioni.</p>"
                "<p>Una delle sfide della carenza di magnesio è che i sintomi sono spesso "
                "aspecifici; stanchezza e dolori muscolari si sovrappongono a molte altre "
                "condizioni, rendendo facile trascurare il deficit. Per questo motivo il "
                "controllo routinario del magnesio è raccomandato nei soggetti a rischio "
                "(consumo cronico di alcol, terapia diuretica, malattie gastrointestinali).</p>"
                "<p><strong>Sintomi da eccesso:</strong> Con l&rsquo;aggravarsi "
                "dell&rsquo;ipermagnesiemia possono svilupparsi nausea, vomito, rossore "
                "facciale, ipotensione, bradicardia, perdita dei riflessi tendinei profondi "
                "e debolezza muscolare. A livelli molto elevati sono possibili depressione "
                "respiratoria e arresto cardiaco. La tossicità da magnesio per via orale è "
                "estremamente rara in soggetti con funzionalità renale normale; il rischio "
                "principale deriva dalla somministrazione endovenosa o dall&rsquo;insufficienza "
                "renale.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="Alimenti ricchi di magnesio",
            body_html=(
                "<p>Un apporto adeguato di magnesio dovrebbe provenire innanzitutto da "
                "un&rsquo;alimentazione equilibrata. I seguenti alimenti sono tra le fonti "
                "più ricche:</p>"
                "<p><strong>Verdure a foglia verde scuro</strong> (spinaci, bietole, cavolo "
                "riccio), <strong>frutta secca</strong> (mandorle, anacardi, arachidi), "
                "<strong>semi</strong> (zucca, chia, lino), <strong>cereali integrali</strong> "
                "(avena, quinoa, riso integrale), <strong>legumi</strong> (fagioli neri, "
                "lenticchie, ceci), <strong>cioccolato fondente</strong> (70&nbsp;%+ cacao), "
                "<strong>avocado</strong> e <strong>banane</strong>. Una porzione di semi di "
                "zucca (28&nbsp;g) fornisce circa 150&nbsp;mg di magnesio, coprendo una parte "
                "significativa del fabbisogno giornaliero.</p>"
                "<p>Gli alimenti trasformati e i cereali raffinati perdono gran parte del loro "
                "contenuto di magnesio, il che spiega perché l&rsquo;insufficienza è comune "
                "nelle diete occidentali moderne. L&rsquo;acqua potabile può essere una fonte "
                "variabile a seconda del contenuto minerale locale. Se pensate "
                "all&rsquo;integrazione, sappiate che il citrato, il glicinato e il taurato di "
                "magnesio hanno una biodisponibilità superiore rispetto all&rsquo;ossido di "
                "magnesio; consultate sempre il medico prima di iniziare qualsiasi integratore.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare un medico?",
            body_html=(
                "<p>Se il vostro livello di magnesio è fuori dal range di riferimento, o se "
                "avvertite crampi muscolari inspiegabili, stanchezza cronica, palpitazioni o "
                "intorpidimento e formicolio, vi consigliamo di consultare un professionista "
                "sanitario. Il monitoraggio regolare è particolarmente importante se avete una "
                "storia di malattia renale, diabete, disturbi gastrointestinali o consumo "
                "cronico di alcol.</p>"
                "<p>Se assumete farmaci come diuretici, IPP o digossina, i vostri livelli di "
                "magnesio possono essere influenzati; concordate con il medico un piano di "
                "controllo periodico. Una carenza di magnesio non trattata può portare a "
                "complicazioni gravi come aritmie cardiache, osteoporosi e resistenza "
                "insulinica.</p>"
                "<p>Inoltre, i pazienti con ipocalcemia o ipokaliemia che non rispondono al "
                "trattamento dovrebbero essere valutati per un eventuale deficit di magnesio "
                "sottostante. Se avete dubbi sul vostro livello di magnesio, discutete i "
                "risultati con un internista o un endocrinologo.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comprendi le tue analisi del sangue con Norya",
            body_html=(
                "<p><strong>Norya</strong> ti permette di caricare i risultati delle tue analisi "
                "del sangue e di ricevere in pochi minuti un report sanitario strutturato e "
                "facile da capire. Il tuo magnesio, calcio, potassio e tutti gli altri parametri "
                "vengono spiegati in un linguaggio chiaro, preparandoti per una visita medica "
                "più produttiva.</p>"
                "<p>Carica il tuo referto, scopri cosa significano i tuoi risultati e genera "
                "un riepilogo da condividere con il tuo medico in pochi minuti. "
                '<a href="/analyze">Inizia l&rsquo;analisi con Norya</a>.</p>'
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
            heading="בדיקת מגנזיום בדם: מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>כשאתם רואים את ערך ה<strong>מגנזיום</strong> בתוצאות בדיקת הדם, טבעי לתהות "
                "מה המספר הזה אומר על בריאותכם. מגנזיום הוא מינרל חיוני המעורב ביותר מ-300 תגובות "
                "אנזימטיות בגוף, ומשפיע על תפקוד השרירים, קצב הלב, בריאות העצמות ומטבוליזם "
                "האנרגיה.</p>"
                "<p>מדריך זה מסביר מה מודדת בדיקת מגנזיום בדם, מהם טווחי הייחוס שחשוב להכיר, "
                "מהם הגורמים האפשריים לרמות נמוכות או גבוהות ומתי כדאי לפנות לרופא. מטרתנו "
                "אינה לאבחן, אלא לעזור לכם להבין את התוצאות כדי שתוכלו לנהל שיחה מושכלת יותר "
                "עם הרופא שלכם.</p>"
                "<p>מחסור במגנזיום נפוץ באופן מפתיע בעולם אך לעתים קרובות מתעלמים ממנו. "
                "גילוי מוקדם ותיקון באמצעות תזונה או תוספים יכולים למנוע סיבוכים בריאותיים "
                "חמורים.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="מהו מגנזיום?",
            body_html=(
                "<p><strong>מגנזיום (Mg)</strong> הוא המינרל הרביעי בשכיחותו בגוף האדם. כ-60% "
                "מהמגנזיום מאוחסן בעצמות, כ-39% בשרירים וברקמות רכות, ורק כ-1% מסתובב בדם. "
                "בדיקות דם מודדות את החלק הקטן הזה, כך שרמות בסרום עשויות להיראות תקינות גם "
                "כשמאגרי הרקמות מדולדלים.</p>"
                "<p>מגנזיום הוא מרכיב תזונתי חיוני – הגוף אינו מסוגל לייצר אותו – ויש לקבל "
                "אותו דרך מזון או תוספים. ירקות עליים ירוקים כהים, אגוזים, זרעים ודגנים מלאים "
                "הם מהמקורות העשירים ביותר. הצריכה היומית המומלצת היא כ-400–420 מ\"ג לגברים "
                "בוגרים וכ-310–320 מ\"ג לנשים בוגרות.</p>"
                "<p>ברמה התאית, מגנזיום מווסת את פוטנציאל הממברנה, תומך בהולכה עצבית ויוצר את "
                "הקומפלקס הפעיל של ATP (אדנוזין טריפוספט) – מטבע האנרגיה העיקרי של הגוף. "
                "בקיצור, כמעט אף תהליך ביוכימי בגוף אינו פועל ביעילות ללא מגנזיום מספק.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="תפקיד המגנזיום בגוף",
            body_html=(
                "<p>מגנזיום משמש כקו-פקטור ב<strong>יותר מ-300 תגובות אנזימטיות</strong>. "
                "תגובות אלו כוללות סינתזת חלבונים, תפקוד שרירים ועצבים, ויסות רמת הסוכר "
                "בדם ובקרת לחץ דם. הוא גם חיוני לסינתזת DNA ו-RNA ולחלוקת תאים.</p>"
                "<p>במערכת הלב וכלי הדם, מגנזיום תומך בהתכווצות סדירה של שריר הלב ומסייע "
                "לדפנות כלי הדם להירגע. רמות מספקות מסייעות לשמור על קצב לב תקין; מחסור "
                "מגביר את הסיכון ל<em>הפרעת קצב</em>. מגנזיום גם פועל כ\"שומר סף\" "
                "לאלקטרוליטים אחרים כמו <strong>סידן</strong> ו<strong>אשלגן</strong>, "
                "ומווסת את תנועתם פנימה והחוצה מהתאים.</p>"
                "<p>לבריאות העצמות, מגנזיום מקל על שקיעת סידן בעצמות ומשחק תפקיד בהמרת "
                "ויטמין D לצורתו הפעילה. מחקרים מצביעים על כך שצריכה מספקת של מגנזיום "
                "עשויה להפחית את הסיכון לאוסטאופורוזיס. בנוסף, מגנזיום משפר את הרגישות "
                "לאינסולין ועשוי לסייע בהפחתת הסיכון לסוכרת סוג 2.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="טווחי ייחוס של מגנזיום",
            body_html=(
                "<p>רמת המגנזיום בסרום נמדדת באמצעות בדיקת דם פשוטה. הטבלה הבאה מציגה את "
                "טווחי הייחוס המקובלים, אם כי הערכים עשויים להשתנות מעט בין מעבדות.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">מצב</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">נמוך (היפומגנזמיה)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0.70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>תקין</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.7 &ndash; 2.2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0.70 &ndash; 0.90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.4 &ndash; 1.8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">גבוה (היפרמגנזמיה)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2.2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0.90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1.8</td>'
                "</tr></tbody></table>"
                "<p><strong>טווח המגנזיום התקין בסרום הוא 1.7–2.2 mg/dL</strong> "
                "(0.70–0.90 mmol/L). ערכים מתחת לטווח זה נקראים <em>היפומגנזמיה</em> "
                "וערכים מעליו <em>היפרמגנזמיה</em>. בדקו תמיד את טווח הייחוס הספציפי "
                "המודפס בדוח המעבדה שלכם.</p>"
                "<p>זכרו שמגנזיום בסרום משקף רק כ-1% ממאגרי הגוף הכוללים. חלק מהרופאים "
                "עשויים להזמין בדיקות נוספות כמו מגנזיום תוך-אריתרוציטי או מגנזיום בשתן "
                "24 שעות כדי להעריך טוב יותר את המצב ברמת הרקמות.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="גורמים למגנזיום נמוך (היפומגנזמיה)",
            body_html=(
                "<p>רמת מגנזיום בסרום מתחת ל-1.7 mg/dL מסווגת כ<strong>היפומגנזמיה</strong>. "
                "הגורמים השכיחים ביותר כוללים צריכה תזונתית לא מספקת, ספיגה לקויה במעי "
                "ואיבוד מוגבר דרך הכליות.</p>"
                "<p><strong>גורמים עיקריים:</strong> תזונה דלה במגנזיום, שלשולים כרוניים או "
                "הקאות, תסמונות חוסר ספיגה כמו צליאק ומחלת קרוהן, אלכוהוליזם כרוני, סוכרת "
                "שאינה מאוזנת (במיוחד בשל פוליאוריה), שימוש ממושך במשתנים (תיאזידים ומשתני "
                "לולאה) ומעכבי משאבת פרוטונים (PPI). הצורך המוגבר בהריון עשוי גם הוא להוביל "
                "למחסור.</p>"
                "<p>מחסור במגנזיום מתלווה לעתים קרובות ל<strong>היפוקלצמיה</strong> "
                "ול<strong>היפוקלמיה</strong>, מכיוון שמגנזיום מווסת את ספיגת מינרלים אלו "
                "ואת ספיגתם מחדש בכליות. אם רמות הסידן או האשלגן נשארות נמוכות למרות הטיפול, "
                "יש לבדוק חשד למחסור בסיסי במגנזיום.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="גורמים למגנזיום גבוה (היפרמגנזמיה)",
            body_html=(
                "<p><strong>היפרמגנזמיה</strong> מוגדרת כרמת מגנזיום בסרום מעל 2.2 mg/dL. "
                "היא נדירה למדי באנשים עם כליות תקינות, מכיוון שהכליות מפרישות ביעילות עודפי "
                "מגנזיום בשתן.</p>"
                "<p>הגורם השכיח ביותר הוא <strong>אי-ספיקת כליות</strong>. כאשר קצב הסינון "
                "הגלומרולרי יורד, הפרשת המגנזיום הופכת ללא מספקת ורמות הדם עולות. נטילת "
                "תוספי מגנזיום במינון מופרז, סותרי חומצה המכילים מגנזיום (למשל מגנזיום "
                "הידרוקסיד) ומשלשלים מגבירים אף הם את הסיכון, במיוחד בחולים עם תפקוד "
                "כלייתי גבולי.</p>"
                "<p>גורמים פחות שכיחים כוללים מחלת אדיסון, תת-פעילות של בלוטת התריס, שימוש "
                "בליתיום ונזק רקמתי מסיבי (רבדומיוליזיס, כוויות). היפרמגנזמיה חמורה עלולה "
                "לסכן חיים ולגרום לשיתוק שרירים, אי-ספיקת נשימה ודום לב. חולי כליות צריכים "
                "לנקוט זהירות עם תרופות ותוספים המכילים מגנזיום.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של חוסר איזון במגנזיום",
            body_html=(
                "<p><strong>תסמיני מחסור:</strong> מחסור קל במגנזיום עשוי להיות "
                "א-סימפטומטי לאורך זמן רב. ככל שהוא מתקדם, התלונות השכיחות ביותר הן "
                "התכווצויות שרירים, פרפורים, עייפות כרונית, ירידה בתיאבון ובחילות. "
                "בשלבים מתקדמים יותר עלולים להופיע חוסר תחושה ועקצוצים, <em>הפרעת קצב</em>, "
                "שינויי אישיות ואפילו פרכוסים.</p>"
                "<p>אחד האתגרים עם מחסור במגנזיום הוא שהתסמינים לעתים קרובות אינם "
                "ספציפיים; עייפות וכאבי שרירים חופפים למצבים רבים אחרים, מה שמקל על "
                "החמצת המחסור. לכן מומלץ ניטור שגרתי של מגנזיום בקרב אוכלוסיות בסיכון "
                "(שימוש כרוני באלכוהול, טיפול במשתנים, מחלות מערכת העיכול).</p>"
                "<p><strong>תסמיני עודף:</strong> עם החמרת ההיפרמגנזמיה עלולים להתפתח "
                "בחילות, הקאות, סמקה בפנים, לחץ דם נמוך, ברדיקרדיה (קצב לב איטי), "
                "אובדן רפלקסים גידיים עמוקים וחולשת שרירים. ברמות גבוהות מאוד קיים סיכון "
                "לדיכוי נשימתי ודום לב. רעילות ממגנזיום אוראלי בלבד נדירה ביותר באנשים "
                "עם תפקוד כלייתי תקין; הסיכון העיקרי נובע ממתן תוך-ורידי או מפגיעה "
                "כלייתית.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="מקורות תזונתיים עשירים במגנזיום",
            body_html=(
                "<p>צריכה מספקת של מגנזיום צריכה לנבוע בראש ובראשונה מתזונה מאוזנת. "
                "המאכלים הבאים הם מהמקורות העשירים ביותר:</p>"
                "<p><strong>ירקות עליים ירוקים כהים</strong> (תרד, סלק עלים, קייל), "
                "<strong>אגוזים</strong> (שקדים, קשיו, בוטנים), <strong>זרעים</strong> "
                "(גרעיני דלעת, צ׳יה, פשתן), <strong>דגנים מלאים</strong> (שיבולת שועל, "
                "קינואה, אורז מלא), <strong>קטניות</strong> (שעועית שחורה, עדשים, חומוס), "
                "<strong>שוקולד מריר</strong> (70%+ קקאו), <strong>אבוקדו</strong> "
                "ו<strong>בננות</strong>. מנה אחת של גרעיני דלעת (28 גרם) מספקת כ-150 מ\"ג "
                "מגנזיום, ומכסה חלק משמעותי מהצורך היומי.</p>"
                "<p>מזון מעובד ודגנים מזוקקים מאבדים חלק ניכר ממגנזיום שלהם, מה שמסביר "
                "מדוע מחסור שכיח בתזונה המערבית המודרנית. מי שתייה יכולים להיות מקור "
                "משתנה בהתאם לתכולת המינרלים המקומית. אם אתם שוקלים תוסף, דעו כי ציטראט, "
                "גליצינאט וטאוראט מגנזיום בעלי זמינות ביולוגית גבוהה יותר ממגנזיום אוקסיד; "
                "התייעצו תמיד עם הרופא לפני תחילת נטילת תוסף.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>אם רמת המגנזיום שלכם מחוץ לטווח הייחוס, או אם אתם חווים התכווצויות "
                "שרירים בלתי מוסברות, עייפות כרונית, דפיקות לב או חוסר תחושה ועקצוצים, "
                "אנו ממליצים להתייעץ עם איש מקצוע רפואי. ניטור סדיר חשוב במיוחד אם יש "
                "לכם היסטוריה של מחלת כליות, סוכרת, הפרעות במערכת העיכול או שימוש כרוני "
                "באלכוהול.</p>"
                "<p>אם אתם נוטלים תרופות כגון משתנים, PPI או דיגוקסין, רמות המגנזיום "
                "שלכם עלולות להיות מושפעות; קבעו עם הרופא תוכנית ניטור סדירה. מחסור "
                "במגנזיום שאינו מטופל עלול להוביל לסיבוכים חמורים כולל הפרעות קצב, "
                "אוסטאופורוזיס ועמידות לאינסולין.</p>"
                "<p>בנוסף, חולים עם היפוקלצמיה או היפוקלמיה שאינה מגיבה לטיפול צריכים "
                "להיבדק לאיתור מחסור בסיסי במגנזיום. אם יש לכם חששות לגבי רמת המגנזיום, "
                "שקלו לדון בתוצאות בדיקת הדם עם רופא פנימי או אנדוקרינולוג.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="הבינו את בדיקות הדם שלכם עם Norya",
            body_html=(
                "<p><strong>Norya</strong> מאפשרת לכם להעלות את תוצאות בדיקות הדם ולקבל תוך "
                "דקות דוח בריאות מובנה וקל להבנה. המגנזיום, הסידן, האשלגן וכל שאר הפרמטרים "
                "שלכם מוסברים בשפה פשוטה, ומכינים אתכם לביקור רופא פרודוקטיבי יותר.</p>"
                "<p>העלו את הדוח שלכם, גלו מה המשמעות של התוצאות, וצרו סיכום שתוכלו "
                "לשתף עם הרופא תוך דקות ספורות. "
                '<a href="/analyze">התחילו את הניתוח עם Norya</a>.</p>'
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
            heading="मैग्नीशियम ब्लड टेस्ट: आपके रिज़ल्ट का क्या मतलब है?",
            body_html=(
                "<p>जब आप अपनी ब्लड टेस्ट रिपोर्ट में <strong>मैग्नीशियम</strong> का मान देखते हैं, "
                "तो यह स्वाभाविक है कि आप सोचें कि यह संख्या आपकी सेहत के बारे में क्या कहती है। "
                "मैग्नीशियम एक आवश्यक खनिज है जो शरीर में 300 से अधिक एंज़ाइमेटिक प्रतिक्रियाओं में "
                "शामिल होता है और मांसपेशियों की कार्यप्रणाली, हृदय की लय, हड्डियों के स्वास्थ्य और "
                "ऊर्जा चयापचय को प्रभावित करता है।</p>"
                "<p>यह गाइड बताती है कि मैग्नीशियम ब्लड टेस्ट क्या मापता है, कौन से रेफ़रेंस रेंज "
                "जानने ज़रूरी हैं, कम या ज़्यादा रहने के संभावित कारण क्या हैं और डॉक्टर से कब मिलना "
                "चाहिए। हमारा उद्देश्य निदान करना नहीं, बल्कि आपको आपके रिज़ल्ट समझने में मदद करना "
                "है ताकि आप अपने डॉक्टर के साथ एक बेहतर बातचीत कर सकें।</p>"
                "<p>मैग्नीशियम की कमी दुनिया भर में आश्चर्यजनक रूप से आम है, फिर भी इसे अक्सर "
                "नज़रअंदाज़ कर दिया जाता है। इसे जल्दी पहचानना और आहार या सप्लीमेंट से ठीक करना "
                "गंभीर स्वास्थ्य जटिलताओं को रोक सकता है।</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="मैग्नीशियम क्या है?",
            body_html=(
                "<p><strong>मैग्नीशियम (Mg)</strong> मानव शरीर में चौथा सबसे प्रचुर खनिज है। "
                "शरीर का लगभग 60% मैग्नीशियम हड्डियों में, 39% मांसपेशियों और कोमल ऊतकों में "
                "संग्रहीत होता है और केवल लगभग 1% रक्त में प्रवाहित होता है। ब्लड टेस्ट इसी "
                "छोटे प्रवाहित अंश को मापते हैं, इसलिए सीरम स्तर सामान्य दिख सकते हैं जबकि "
                "ऊतक भंडार समाप्त हो चुके हों।</p>"
                "<p>मैग्नीशियम एक आवश्यक पोषक तत्व है – शरीर इसे स्वयं नहीं बना सकता – और "
                "इसे भोजन या सप्लीमेंट के ज़रिये प्राप्त करना होता है। गहरे हरे पत्तेदार "
                "सब्ज़ियाँ, मेवे, बीज और साबुत अनाज सबसे समृद्ध आहार स्रोतों में हैं। "
                "अनुशंसित दैनिक सेवन वयस्क पुरुषों के लिए लगभग 400–420&nbsp;mg और वयस्क "
                "महिलाओं के लिए 310–320&nbsp;mg है।</p>"
                "<p>कोशिकीय स्तर पर मैग्नीशियम झिल्ली विभव को नियंत्रित करता है, तंत्रिका "
                "संचरण को सहारा देता है और ATP (एडेनोसिन ट्राइफ़ॉस्फेट) – शरीर की प्रमुख "
                "ऊर्जा मुद्रा – का सक्रिय रूप बनाता है। संक्षेप में, शरीर में लगभग कोई भी "
                "जैव रासायनिक प्रक्रिया पर्याप्त मैग्नीशियम के बिना कुशलतापूर्वक नहीं "
                "चलती।</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="शरीर में मैग्नीशियम की भूमिका",
            body_html=(
                "<p>मैग्नीशियम <strong>300 से अधिक एंज़ाइम प्रतिक्रियाओं</strong> में "
                "कोफ़ैक्टर के रूप में कार्य करता है। इन प्रतिक्रियाओं में प्रोटीन संश्लेषण, "
                "मांसपेशी और तंत्रिका कार्य, रक्त शर्करा नियंत्रण और रक्तचाप प्रबंधन शामिल "
                "हैं। यह DNA और RNA संश्लेषण तथा कोशिका विभाजन के लिए भी आवश्यक है।</p>"
                "<p>हृदय प्रणाली में मैग्नीशियम हृदय की मांसपेशी के नियमित संकुचन का समर्थन "
                "करता है और रक्त वाहिका की दीवारों को शिथिल होने में मदद करता है। पर्याप्त "
                "मैग्नीशियम स्वस्थ हृदय लय बनाए रखने में सहायक होता है; कमी से "
                "<em>अतालता</em> (arrhythmia) का ख़तरा बढ़ जाता है। मैग्नीशियम "
                "<strong>कैल्शियम</strong> और <strong>पोटैशियम</strong> जैसे अन्य "
                "इलेक्ट्रोलाइट्स के लिए \"द्वारपाल\" का काम भी करता है।</p>"
                "<p>हड्डियों के स्वास्थ्य के लिए मैग्नीशियम कैल्शियम को हड्डियों में "
                "जमा करने में सहायता करता है और विटामिन D को उसके सक्रिय रूप में बदलने "
                "में भूमिका निभाता है। शोध बताते हैं कि पर्याप्त मैग्नीशियम सेवन "
                "ऑस्टियोपोरोसिस का जोखिम कम कर सकता है। इसके अतिरिक्त, मैग्नीशियम "
                "इंसुलिन संवेदनशीलता में सुधार करता है और टाइप 2 मधुमेह के जोखिम को "
                "कम करने में मदद कर सकता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="मैग्नीशियम रेफ़रेंस रेंज",
            body_html=(
                "<p>सीरम मैग्नीशियम एक साधारण ब्लड ड्रॉ से मापा जाता है। नीचे दी गई तालिका "
                "सामान्यतः स्वीकृत रेफ़रेंस रेंज दिखाती है, हालाँकि मान प्रयोगशालाओं के बीच "
                "थोड़ा भिन्न हो सकते हैं।</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">स्थिति</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">कम (हाइपोमैग्नेसीमिया)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0.70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>सामान्य</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.7 &ndash; 2.2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0.70 &ndash; 0.90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.4 &ndash; 1.8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">अधिक (हाइपरमैग्नेसीमिया)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2.2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0.90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1.8</td>'
                "</tr></tbody></table>"
                "<p><strong>सामान्य सीरम मैग्नीशियम रेंज 1.7–2.2&nbsp;mg/dL</strong> "
                "(0.70–0.90&nbsp;mmol/L) मानी जाती है। इस रेंज से नीचे के मानों को "
                "<em>हाइपोमैग्नेसीमिया</em> और ऊपर के मानों को <em>हाइपरमैग्नेसीमिया</em> "
                "कहते हैं। हमेशा अपनी लैब रिपोर्ट पर छपी विशिष्ट रेफ़रेंस रेंज देखें।</p>"
                "<p>ध्यान रखें कि सीरम मैग्नीशियम कुल शरीर भंडार का केवल लगभग 1% दर्शाता "
                "है। कुछ चिकित्सक ऊतक स्तर पर बेहतर मूल्यांकन के लिए RBC मैग्नीशियम या "
                "24-घंटे यूरिन मैग्नीशियम जैसे अतिरिक्त टेस्ट लिख सकते हैं।</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="कम मैग्नीशियम (हाइपोमैग्नेसीमिया) के कारण",
            body_html=(
                "<p>1.7&nbsp;mg/dL से नीचे सीरम मैग्नीशियम स्तर को "
                "<strong>हाइपोमैग्नेसीमिया</strong> के रूप में वर्गीकृत किया जाता है। "
                "सबसे आम कारणों में अपर्याप्त आहार सेवन, आँतों में ख़राब अवशोषण और "
                "गुर्दों द्वारा अत्यधिक हानि शामिल हैं।</p>"
                "<p><strong>प्रमुख कारण:</strong> मैग्नीशियम-रहित आहार, दीर्घकालिक दस्त या "
                "उल्टी, सीलिएक रोग और क्रोहन रोग जैसी कुअवशोषण बीमारियाँ, दीर्घकालिक "
                "शराब सेवन, अनियंत्रित मधुमेह (विशेषकर पॉल्यूरिया के कारण), मूत्रवर्धक "
                "दवाओं (थायज़ाइड और लूप डाइयुरेटिक्स) का लंबे समय तक उपयोग और प्रोटॉन "
                "पंप इनहिबिटर (PPI)। गर्भावस्था में बढ़ी हुई माँग भी कमी का कारण बन "
                "सकती है।</p>"
                "<p>मैग्नीशियम की कमी अक्सर <strong>हाइपोकैल्सीमिया</strong> और "
                "<strong>हाइपोकैलीमिया</strong> के साथ होती है क्योंकि मैग्नीशियम इन "
                "खनिजों के अवशोषण और गुर्दों में पुनःअवशोषण को नियंत्रित करता है। अगर "
                "उपचार के बावजूद कैल्शियम या पोटैशियम का स्तर कम बना रहता है, तो "
                "अंतर्निहित मैग्नीशियम की कमी की जाँच होनी चाहिए।</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="अधिक मैग्नीशियम (हाइपरमैग्नेसीमिया) के कारण",
            body_html=(
                "<p><strong>हाइपरमैग्नेसीमिया</strong> तब होती है जब सीरम मैग्नीशियम "
                "2.2&nbsp;mg/dL से ऊपर चला जाता है। स्वस्थ गुर्दों वाले लोगों में यह "
                "काफ़ी दुर्लभ है क्योंकि गुर्दे अतिरिक्त मैग्नीशियम को मूत्र में कुशलता "
                "से निकाल देते हैं।</p>"
                "<p>सबसे आम कारण <strong>गुर्दे की विफलता</strong> है। जब ग्लोमेरुलर "
                "फ़िल्ट्रेशन रेट गिरता है, तो मैग्नीशियम का उत्सर्जन अपर्याप्त हो जाता "
                "है और रक्त स्तर बढ़ जाता है। अत्यधिक मैग्नीशियम सप्लीमेंट, मैग्नीशियम "
                "युक्त एंटासिड (जैसे मैग्नीशियम हाइड्रॉक्साइड) और लैक्सेटिव भी जोखिम "
                "बढ़ाते हैं, विशेषकर सीमारेखा गुर्दा कार्य वाले रोगियों में।</p>"
                "<p>कम सामान्य कारणों में एडिसन रोग, हाइपोथायरॉइडिज़्म, लिथियम का उपयोग "
                "और बड़े पैमाने पर ऊतक क्षति (रैब्डोमायोलिसिस, जलन) शामिल हैं। गंभीर "
                "हाइपरमैग्नेसीमिया जीवन-घातक हो सकती है, जिससे मांसपेशी पक्षाघात, "
                "श्वसन विफलता और कार्डियक अरेस्ट हो सकता है। गुर्दे की बीमारी वाले "
                "मरीज़ों को मैग्नीशियम युक्त दवाओं और सप्लीमेंट्स के साथ सावधानी "
                "बरतनी चाहिए।</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="मैग्नीशियम असंतुलन के लक्षण",
            body_html=(
                "<p><strong>कमी के लक्षण:</strong> हल्की मैग्नीशियम की कमी लंबे समय तक "
                "लक्षणहीन हो सकती है। जैसे-जैसे यह बढ़ती है, सबसे आम शिकायतों में "
                "मांसपेशियों में ऐंठन, फड़कन, दीर्घकालिक थकान, भूख न लगना और मतली शामिल "
                "हैं। अधिक गंभीर अवस्थाओं में सुन्नपन और झुनझुनी, <em>अतालता</em> "
                "(अनियमित दिल की धड़कन), व्यक्तित्व परिवर्तन और यहाँ तक कि दौरे भी "
                "पड़ सकते हैं।</p>"
                "<p>मैग्नीशियम की कमी की एक चुनौती यह है कि लक्षण अक्सर गैर-विशिष्ट होते "
                "हैं; थकान और मांसपेशी दर्द कई अन्य स्थितियों के साथ मिलते-जुलते हैं, "
                "जिससे कमी को पहचानना कठिन हो जाता है। इसलिए उच्च जोखिम वाले व्यक्तियों "
                "(दीर्घकालिक शराब सेवन, मूत्रवर्धक चिकित्सा, जठरांत्र संबंधी रोग) में "
                "नियमित मैग्नीशियम निगरानी की सिफ़ारिश की जाती है।</p>"
                "<p><strong>अधिकता के लक्षण:</strong> हाइपरमैग्नेसीमिया बढ़ने पर मतली, "
                "उल्टी, चेहरे पर लालिमा, निम्न रक्तचाप, ब्रैडीकार्डिया (धीमी हृदय गति), "
                "गहरे कण्डरा प्रतिवर्तों का नुकसान और मांसपेशी कमज़ोरी हो सकती है। बहुत "
                "उच्च स्तर पर श्वसन अवसाद और कार्डियक अरेस्ट का ख़तरा होता है। सामान्य "
                "गुर्दा कार्य वाले लोगों में मौखिक मैग्नीशियम से विषाक्तता अत्यंत दुर्लभ "
                "है; मुख्य जोखिम अंतःशिरा प्रशासन या गुर्दे की दुर्बलता से उत्पन्न "
                "होता है।</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="मैग्नीशियम से भरपूर खाद्य स्रोत",
            body_html=(
                "<p>पर्याप्त मैग्नीशियम सेवन मुख्य रूप से संतुलित आहार से होना चाहिए। "
                "निम्नलिखित खाद्य पदार्थ मैग्नीशियम के सबसे समृद्ध स्रोतों में हैं:</p>"
                "<p><strong>गहरी हरी पत्तेदार सब्ज़ियाँ</strong> (पालक, स्विस चार्ड, केल), "
                "<strong>मेवे</strong> (बादाम, काजू, मूँगफली), <strong>बीज</strong> "
                "(कद्दू के बीज, चिया बीज, अलसी), <strong>साबुत अनाज</strong> "
                "(जई, क्विनोआ, ब्राउन राइस), <strong>फलियाँ</strong> (काली फलियाँ, "
                "मसूर, छोले), <strong>डार्क चॉकलेट</strong> (70%+ कोको), "
                "<strong>एवोकाडो</strong> और <strong>केले</strong>। कद्दू के बीजों की "
                "एक सर्विंग (28&nbsp;g) लगभग 150&nbsp;mg मैग्नीशियम प्रदान करती है, "
                "जो दैनिक आवश्यकता का एक महत्वपूर्ण हिस्सा पूरा करती है।</p>"
                "<p>प्रोसेस्ड फ़ूड और रिफ़ाइंड अनाज में मैग्नीशियम की काफ़ी मात्रा नष्ट "
                "हो जाती है, यही कारण है कि आधुनिक पश्चिमी आहार में कमी आम है। पीने का "
                "पानी स्थानीय खनिज सामग्री के अनुसार एक परिवर्तनशील स्रोत हो सकता है। "
                "यदि आप सप्लीमेंट लेने पर विचार कर रहे हैं, तो जान लें कि मैग्नीशियम "
                "साइट्रेट, ग्लाइसिनेट और टॉरेट की बायोअवेलेबिलिटी मैग्नीशियम ऑक्साइड "
                "से अधिक होती है; कोई भी सप्लीमेंट शुरू करने से पहले हमेशा अपने डॉक्टर "
                "से सलाह लें।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अगर आपका मैग्नीशियम स्तर रेफ़रेंस रेंज से बाहर है, या अगर आप "
                "अकारण मांसपेशी ऐंठन, दीर्घकालिक थकान, दिल की धड़कन या सुन्नपन और "
                "झुनझुनी का अनुभव कर रहे हैं, तो हम स्वास्थ्य विशेषज्ञ से परामर्श "
                "लेने की सलाह देते हैं। नियमित निगरानी विशेष रूप से तब ज़रूरी है जब "
                "आपको गुर्दे की बीमारी, मधुमेह, जठरांत्र संबंधी विकार या दीर्घकालिक "
                "शराब सेवन का इतिहास हो।</p>"
                "<p>अगर आप मूत्रवर्धक, PPI या डिगॉक्सिन जैसी दवाएँ ले रहे हैं, तो "
                "आपके मैग्नीशियम स्तर प्रभावित हो सकते हैं; अपने डॉक्टर के साथ एक "
                "नियमित निगरानी योजना बनाएँ। अनुपचारित मैग्नीशियम की कमी हृदय "
                "अतालता, ऑस्टियोपोरोसिस और इंसुलिन प्रतिरोध सहित गंभीर जटिलताओं "
                "का कारण बन सकती है।</p>"
                "<p>इसके अतिरिक्त, जिन रोगियों में उपचार के बावजूद हाइपोकैल्सीमिया या "
                "हाइपोकैलीमिया ठीक नहीं हो रहा, उनमें अंतर्निहित मैग्नीशियम की कमी "
                "की जाँच होनी चाहिए। अगर आपको अपने मैग्नीशियम स्तर को लेकर चिंता है, "
                "तो अपनी ब्लड टेस्ट रिपोर्ट किसी इंटर्निस्ट या एंडोक्राइनोलॉजिस्ट "
                "को दिखाएँ।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya से अपनी ब्लड टेस्ट रिपोर्ट समझें",
            body_html=(
                "<p><strong>Norya</strong> आपको अपनी ब्लड टेस्ट रिपोर्ट अपलोड करने और "
                "कुछ ही मिनटों में एक संरचित, समझने में आसान स्वास्थ्य सारांश रिपोर्ट प्राप्त "
                "करने की सुविधा देता है। आपके मैग्नीशियम, कैल्शियम, पोटैशियम और अन्य सभी "
                "पैरामीटर सरल भाषा में समझाए जाते हैं, जिससे आप डॉक्टर की विज़िट के लिए "
                "बेहतर तैयार होते हैं।</p>"
                "<p>अपनी रिपोर्ट अपलोड करें, जानें कि आपके रिज़ल्ट का क्या मतलब है, और "
                "कुछ ही मिनटों में अपने डॉक्टर के साथ साझा करने योग्य सारांश बनाएँ। "
                '<a href="/analyze">Norya से विश्लेषण शुरू करें</a>।</p>'
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
            heading="تحليل المغنيسيوم في الدم: ماذا تعني نتائجك؟",
            body_html=(
                "<p>عندما ترى قيمة <strong>المغنيسيوم</strong> في تقرير فحص الدم، من الطبيعي أن "
                "تتساءل عمّا يعنيه هذا الرقم لصحتك. المغنيسيوم معدن أساسي يشارك في أكثر من 300 "
                "تفاعل إنزيمي في الجسم، ويؤثر على وظائف العضلات ونظم القلب وصحة العظام "
                "والتمثيل الغذائي للطاقة.</p>"
                "<p>يشرح هذا الدليل ما يقيسه تحليل المغنيسيوم في الدم، والنطاقات المرجعية التي "
                "يجب أن تعرفها، والأسباب المحتملة للمستويات المنخفضة أو المرتفعة، ومتى يجب "
                "مراجعة الطبيب. هدفنا ليس التشخيص، بل مساعدتك على فهم نتائجك حتى تتمكن من "
                "إجراء محادثة أكثر وعياً مع طبيبك.</p>"
                "<p>نقص المغنيسيوم شائع بشكل مدهش حول العالم لكنه غالباً ما يُتجاهل. اكتشافه "
                "مبكراً ومعالجته عبر النظام الغذائي أو المكملات يمكن أن يمنع مضاعفات صحية "
                "خطيرة.</p>"
            ),
        ),
        Section(
            id="what-is-magnesium", level=2,
            heading="ما هو المغنيسيوم؟",
            body_html=(
                "<p><strong>المغنيسيوم (Mg)</strong> هو رابع أكثر المعادن وفرة في جسم الإنسان. "
                "يُخزَّن حوالي 60% منه في العظام، و39% في العضلات والأنسجة الرخوة، ونحو 1% فقط "
                "يدور في الدم. تقيس تحاليل الدم هذا الجزء الصغير المتداول، لذا قد تبدو مستويات "
                "المصل طبيعية حتى عندما تكون مخازن الأنسجة مستنفدة.</p>"
                "<p>المغنيسيوم عنصر غذائي أساسي — لا يستطيع الجسم تصنيعه — ويجب الحصول عليه من "
                "الطعام أو المكملات. الخضروات الورقية الداكنة والمكسرات والبذور والحبوب الكاملة "
                "هي من أغنى المصادر الغذائية. الجرعة اليومية الموصى بها حوالي "
                "400–420&nbsp;ملغ للرجال البالغين و310–320&nbsp;ملغ للنساء البالغات.</p>"
                "<p>على المستوى الخلوي، ينظّم المغنيسيوم جهد الغشاء، ويدعم النقل العصبي، "
                "ويشكّل المركّب النشط لـ ATP (أدينوسين ثلاثي الفوسفات) — عملة الطاقة الرئيسية "
                "في الجسم. باختصار، لا تعمل أي عملية كيميائية حيوية تقريباً بكفاءة بدون "
                "مغنيسيوم كافٍ.</p>"
            ),
        ),
        Section(
            id="role-in-body", level=2,
            heading="دور المغنيسيوم في الجسم",
            body_html=(
                "<p>يعمل المغنيسيوم كعامل مساعد في <strong>أكثر من 300 تفاعل إنزيمي</strong>. "
                "تشمل هذه التفاعلات تخليق البروتين، ووظائف العضلات والأعصاب، وتنظيم سكر الدم، "
                "والتحكم في ضغط الدم. كما أنه ضروري لتخليق الحمض النووي DNA وRNA "
                "وللانقسام الخلوي.</p>"
                "<p>في الجهاز القلبي الوعائي، يدعم المغنيسيوم الانقباض المنتظم لعضلة القلب "
                "ويساعد جدران الأوعية الدموية على الاسترخاء. تساعد المستويات الكافية في "
                "الحفاظ على نظم قلب صحي؛ ويزيد النقص من خطر <em>اضطراب النظم</em>. يعمل "
                "المغنيسيوم أيضاً كـ\"حارس بوابة\" لشوارد أخرى مثل <strong>الكالسيوم</strong> "
                "و<strong>البوتاسيوم</strong>، منظّماً حركتها داخل الخلايا وخارجها.</p>"
                "<p>لصحة العظام، يسهّل المغنيسيوم ترسيب الكالسيوم في العظام ويلعب دوراً في "
                "تحويل فيتامين د إلى شكله النشط. تشير الأبحاث إلى أن تناول المغنيسيوم الكافي "
                "قد يقلل خطر الإصابة بهشاشة العظام. بالإضافة إلى ذلك، يحسّن المغنيسيوم "
                "حساسية الأنسولين وقد يساعد في تقليل خطر مرض السكري من النوع الثاني.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="النطاقات المرجعية للمغنيسيوم",
            body_html=(
                "<p>يُقاس مستوى المغنيسيوم في المصل بسحب دم بسيط. يعرض الجدول أدناه "
                "النطاقات المرجعية المقبولة عموماً، وإن كانت القيم قد تختلف قليلاً بين "
                "المختبرات.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الحالة</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mg/dL</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mmol/L</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">mEq/L</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">منخفض (نقص مغنيسيوم الدم)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.7</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;0.70</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.4</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>طبيعي</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.7 &ndash; 2.2</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>0.70 &ndash; 0.90</strong></td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;"><strong>1.4 &ndash; 1.8</strong></td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">مرتفع (فرط مغنيسيوم الدم)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;2.2</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;0.90</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;1.8</td>'
                "</tr></tbody></table>"
                "<p><strong>النطاق الطبيعي للمغنيسيوم في المصل هو 1.7–2.2&nbsp;mg/dL</strong> "
                "(0.70–0.90&nbsp;mmol/L). تُسمّى القيم الأقل <em>نقص مغنيسيوم الدم</em> "
                "والأعلى <em>فرط مغنيسيوم الدم</em>. تحقق دائماً من النطاق المرجعي "
                "المطبوع في تقرير مختبرك.</p>"
                "<p>تذكّر أن المغنيسيوم في المصل يعكس حوالي 1% فقط من إجمالي مخازن "
                "الجسم. قد يطلب بعض الأطباء اختبارات إضافية مثل المغنيسيوم داخل كريات "
                "الدم الحمراء أو المغنيسيوم في بول 24 ساعة لتقييم أفضل للحالة على "
                "مستوى الأنسجة.</p>"
            ),
        ),
        Section(
            id="low-magnesium-causes", level=2,
            heading="أسباب انخفاض المغنيسيوم (نقص مغنيسيوم الدم)",
            body_html=(
                "<p>يُصنَّف مستوى المغنيسيوم في المصل الأقل من 1.7&nbsp;mg/dL على أنه "
                "<strong>نقص مغنيسيوم الدم</strong>. تشمل الأسباب الأكثر شيوعاً نقص "
                "المدخول الغذائي، وسوء الامتصاص المعوي، والفقد الكلوي المفرط.</p>"
                "<p><strong>الأسباب الرئيسية:</strong> نظام غذائي فقير بالمغنيسيوم، إسهال "
                "مزمن أو قيء، متلازمات سوء الامتصاص مثل الداء البطني ومرض كرون، إدمان "
                "الكحول المزمن، السكري غير المنضبط (خاصة بسبب البوال)، الاستخدام المطوّل "
                "لمدرّات البول (الثيازيدات ومدرّات الحلقة) ومثبطات مضخة البروتون (PPI). "
                "كما قد يؤدي ازدياد الاحتياج أثناء الحمل إلى نقص.</p>"
                "<p>غالباً ما يتزامن نقص المغنيسيوم مع <strong>نقص كلس الدم</strong> "
                "و<strong>نقص بوتاسيوم الدم</strong> لأن المغنيسيوم ينظّم امتصاص هذين "
                "المعدنين وإعادة امتصاصهما في الكلى. إذا ظلت مستويات الكالسيوم أو "
                "البوتاسيوم منخفضة رغم العلاج، يجب البحث عن نقص مغنيسيوم أساسي.</p>"
            ),
        ),
        Section(
            id="high-magnesium-causes", level=2,
            heading="أسباب ارتفاع المغنيسيوم (فرط مغنيسيوم الدم)",
            body_html=(
                "<p><strong>فرط مغنيسيوم الدم</strong> يُعرَّف بمستوى مغنيسيوم مصلي أعلى "
                "من 2.2&nbsp;mg/dL. وهو نادر جداً لدى الأشخاص ذوي الكلى السليمة لأن "
                "الكلى تطرح الفائض بكفاءة في البول.</p>"
                "<p>السبب الأكثر شيوعاً هو <strong>الفشل الكلوي</strong>. عندما ينخفض معدل "
                "الترشيح الكبيبي، يصبح إفراز المغنيسيوم غير كافٍ وترتفع مستويات الدم. "
                "تناول جرعات مفرطة من مكملات المغنيسيوم، ومضادات الحموضة المحتوية على "
                "المغنيسيوم (مثل هيدروكسيد المغنيسيوم)، والملينات يزيد أيضاً من الخطر، "
                "خاصة لدى المرضى ذوي الوظيفة الكلوية الحدّية.</p>"
                "<p>من الأسباب الأقل شيوعاً داء أديسون، وقصور الغدة الدرقية، واستخدام "
                "الليثيوم، وتلف الأنسجة الواسع (انحلال الربيدات، الحروق). فرط مغنيسيوم "
                "الدم الشديد قد يهدد الحياة مسبباً شللاً عضلياً وفشلاً تنفسياً وسكتة "
                "قلبية. يجب على مرضى الكلى توخي الحذر مع الأدوية والمكملات المحتوية "
                "على المغنيسيوم.</p>"
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض اختلال توازن المغنيسيوم",
            body_html=(
                "<p><strong>أعراض النقص:</strong> قد يكون نقص المغنيسيوم الخفيف بلا أعراض "
                "لفترة طويلة. مع تقدّمه، تشمل الشكاوى الأكثر شيوعاً تشنجات العضلات "
                "والارتعاش والتعب المزمن وفقدان الشهية والغثيان. في المراحل المتقدمة قد "
                "يظهر خدر وتنميل و<em>اضطراب النظم</em> (ضربات قلب غير منتظمة) وتغيرات "
                "في الشخصية وحتى نوبات صرعية.</p>"
                "<p>أحد تحديات نقص المغنيسيوم أن الأعراض غالباً غير نوعية؛ فالتعب وآلام "
                "العضلات يتداخلان مع حالات عديدة أخرى، مما يسهّل إغفال النقص. لهذا يُوصى "
                "بمراقبة روتينية للمغنيسيوم لدى الفئات عالية الخطورة (استهلاك الكحول المزمن، "
                "العلاج بمدرّات البول، أمراض الجهاز الهضمي).</p>"
                "<p><strong>أعراض الفرط:</strong> مع تفاقم فرط مغنيسيوم الدم، قد يتطور "
                "الغثيان والقيء واحمرار الوجه وانخفاض ضغط الدم وبطء القلب وفقدان المنعكسات "
                "الوترية العميقة وضعف العضلات. عند مستويات عالية جداً يوجد خطر تثبيط "
                "التنفس والسكتة القلبية. التسمم من المغنيسيوم الفموي وحده نادر للغاية "
                "لدى أصحاب الوظيفة الكلوية الطبيعية؛ الخطر الرئيسي ينشأ من الإعطاء "
                "الوريدي أو القصور الكلوي.</p>"
            ),
        ),
        Section(
            id="dietary-sources", level=2,
            heading="مصادر غذائية غنية بالمغنيسيوم",
            body_html=(
                "<p>يجب أن يأتي تناول المغنيسيوم الكافي بشكل رئيسي من نظام غذائي متوازن. "
                "الأطعمة التالية هي من أغنى المصادر:</p>"
                "<p><strong>الخضروات الورقية الداكنة</strong> (السبانخ، السلق، الكيل)، "
                "<strong>المكسرات</strong> (اللوز، الكاجو، الفول السوداني)، "
                "<strong>البذور</strong> (بذور القرع، بذور الشيا، بذور الكتان)، "
                "<strong>الحبوب الكاملة</strong> (الشوفان، الكينوا، الأرز البني)، "
                "<strong>البقوليات</strong> (الفاصوليا السوداء، العدس، الحمص)، "
                "<strong>الشوكولاتة الداكنة</strong> (70%+ كاكاو)، "
                "<strong>الأفوكادو</strong> و<strong>الموز</strong>. حصة واحدة من بذور "
                "القرع (28 غرام) توفر حوالي 150 ملغ من المغنيسيوم، وتغطي جزءاً كبيراً "
                "من الاحتياج اليومي.</p>"
                "<p>الأطعمة المصنّعة والحبوب المكررة تفقد الكثير من محتواها من المغنيسيوم، "
                "وهذا يفسر شيوع النقص في الأنظمة الغذائية الغربية الحديثة. مياه الشرب "
                "يمكن أن تكون مصدراً متغيراً حسب المحتوى المعدني المحلي. إذا كنت تفكر "
                "في تناول مكملات، اعلم أن سيترات وغليسينات وتاورات المغنيسيوم لديها "
                "توافر حيوي أعلى من أكسيد المغنيسيوم؛ استشر طبيبك دائماً قبل البدء "
                "بأي مكمل.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>إذا كان مستوى المغنيسيوم لديك خارج النطاق المرجعي، أو إذا كنت تعاني "
                "من تشنجات عضلية غير مفسّرة أو تعب مزمن أو خفقان قلب أو خدر وتنميل، "
                "ننصحك بمراجعة متخصص في الرعاية الصحية. المراقبة المنتظمة مهمة بشكل خاص "
                "إذا كان لديك تاريخ من أمراض الكلى أو السكري أو اضطرابات الجهاز الهضمي "
                "أو استهلاك الكحول المزمن.</p>"
                "<p>إذا كنت تتناول أدوية مثل مدرّات البول أو مثبطات مضخة البروتون أو "
                "الديجوكسين، فقد تتأثر مستويات المغنيسيوم لديك؛ ضع مع طبيبك خطة مراقبة "
                "منتظمة. نقص المغنيسيوم غير المعالَج يمكن أن يؤدي إلى مضاعفات خطيرة تشمل "
                "اضطرابات نظم القلب وهشاشة العظام ومقاومة الأنسولين.</p>"
                "<p>بالإضافة إلى ذلك، يجب فحص المرضى الذين يعانون من نقص كلس الدم أو نقص "
                "بوتاسيوم الدم الذي لا يستجيب للعلاج بحثاً عن نقص مغنيسيوم أساسي. إذا "
                "كانت لديك مخاوف بشأن مستوى المغنيسيوم، ناقش نتائج تحاليل الدم مع طبيب "
                "باطنية أو اختصاصي غدد صمّاء.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="افهم تحاليل دمك مع Norya",
            body_html=(
                "<p><strong>Norya</strong> تتيح لك رفع نتائج تحاليل الدم والحصول خلال "
                "دقائق على تقرير صحي مُنظّم وسهل الفهم. يُشرح المغنيسيوم والكالسيوم "
                "والبوتاسيوم وجميع المعايير الأخرى بلغة واضحة، مما يُعدّك لزيارة "
                "طبيب أكثر إنتاجية.</p>"
                "<p>ارفع تقريرك، اكتشف ما تعنيه نتائجك، وأنشئ ملخصاً يمكنك مشاركته "
                "مع طبيبك في دقائق معدودة. "
                '<a href="/analyze">ابدأ التحليل مع Norya</a>.</p>'
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


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_magnesium_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for Magnesium article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_magnesium_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for Magnesium article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is a magnesium blood test?",
             "answer": "A magnesium blood test measures the level of magnesium in your blood serum. Magnesium is an essential mineral involved in over 300 enzymatic reactions, including muscle function, heart rhythm, and energy metabolism. The normal range is typically 1.7–2.2 mg/dL."},
            {"question": "What causes low magnesium levels?",
             "answer": "Common causes of low magnesium (hypomagnesemia) include poor dietary intake, malabsorption conditions like celiac or Crohn's disease, chronic alcoholism, poorly controlled diabetes, and long-term use of certain medications such as diuretics and proton pump inhibitors (PPIs)."},
            {"question": "What are the symptoms of magnesium deficiency?",
             "answer": "Symptoms may include muscle cramps, twitching, chronic fatigue, numbness and tingling, irregular heartbeat (arrhythmia), loss of appetite, and nausea. Severe deficiency can lead to seizures and personality changes."},
            {"question": "What foods are high in magnesium?",
             "answer": "Magnesium-rich foods include dark leafy greens (spinach, kale), nuts (almonds, cashews), seeds (pumpkin seeds, chia seeds), whole grains, legumes, dark chocolate (70%+ cocoa), avocados, and bananas."},
        ],
        "tr": [
            {"question": "Magnezyum kan testi nedir?",
             "answer": "Magnezyum kan testi, kan serumunuzdaki magnezyum düzeyini ölçer. Magnezyum, kas fonksiyonu, kalp ritmi ve enerji metabolizması dahil 300'den fazla enzimatik reaksiyonda yer alan esansiyel bir mineraldir. Normal aralık genellikle 1,7–2,2 mg/dL'dir."},
            {"question": "Düşük magnezyumun nedenleri nelerdir?",
             "answer": "Hipomagnezemi nedenleri arasında yetersiz diyet alımı, çölyak veya Crohn hastalığı gibi emilim bozuklukları, kronik alkolizm, kontrol altına alınamamış diyabet ve diüretik ile PPI gibi ilaçların uzun süreli kullanımı yer alır."},
            {"question": "Magnezyum eksikliğinin belirtileri nelerdir?",
             "answer": "Belirtiler arasında kas krampları, seğirmeler, kronik yorgunluk, uyuşma ve karıncalanma, düzensiz kalp atışı (aritmi), iştahsızlık ve bulantı sayılabilir. Ciddi eksiklikte nöbetler ve kişilik değişiklikleri görülebilir."},
            {"question": "Hangi besinler magnezyum açısından zengindir?",
             "answer": "Koyu yeşil yapraklı sebzeler (ıspanak, kara lahana), kuruyemişler (badem, kaju), tohumlar (kabak çekirdeği, çiya tohumu), tam tahıllar, baklagiller, bitter çikolata (%70+ kakao), avokado ve muz magnezyumdan zengin besinlerdir."},
        ],
        "es": [
            {"question": "¿Qué es un análisis de magnesio en sangre?",
             "answer": "Es un análisis que mide el nivel de magnesio en el suero sanguíneo. El magnesio es un mineral esencial que interviene en más de 300 reacciones enzimáticas, incluyendo la función muscular, el ritmo cardíaco y el metabolismo energético. El rango normal suele ser 1,7–2,2 mg/dL."},
            {"question": "¿Qué causa niveles bajos de magnesio?",
             "answer": "Las causas comunes incluyen ingesta dietética insuficiente, malabsorción (enfermedad celíaca, Crohn), alcoholismo crónico, diabetes mal controlada y uso prolongado de diuréticos e inhibidores de la bomba de protones (IBP)."},
            {"question": "¿Cuáles son los síntomas de la deficiencia de magnesio?",
             "answer": "Los síntomas pueden incluir calambres musculares, fasciculaciones, fatiga crónica, entumecimiento y hormigueo, arritmia, pérdida de apetito y náuseas. La deficiencia grave puede provocar convulsiones y cambios de personalidad."},
            {"question": "¿Qué alimentos son ricos en magnesio?",
             "answer": "Verduras de hoja verde oscura (espinacas, col rizada), frutos secos (almendras, anacardos), semillas (calabaza, chía), cereales integrales, legumbres, chocolate negro (70%+ cacao), aguacates y plátanos."},
        ],
        "de": [
            {"question": "Was ist ein Magnesium-Bluttest?",
             "answer": "Ein Magnesium-Bluttest misst den Magnesiumspiegel im Blutserum. Magnesium ist ein essenzieller Mineralstoff, der an über 300 Enzymreaktionen beteiligt ist, darunter Muskelfunktion, Herzrhythmus und Energiestoffwechsel. Der Normalbereich liegt typischerweise bei 1,7–2,2 mg/dL."},
            {"question": "Was verursacht niedrige Magnesiumwerte?",
             "answer": "Häufige Ursachen sind unzureichende Nahrungsaufnahme, Malabsorption (Zöliakie, Morbus Crohn), chronischer Alkoholismus, schlecht eingestellter Diabetes und langfristige Einnahme von Diuretika und Protonenpumpenhemmern (PPI)."},
            {"question": "Was sind die Symptome eines Magnesiummangels?",
             "answer": "Symptome können Muskelkrämpfe, Zuckungen, chronische Müdigkeit, Taubheitsgefühl und Kribbeln, Arrhythmie, Appetitlosigkeit und Übelkeit umfassen. Schwerer Mangel kann zu Krampfanfällen und Persönlichkeitsveränderungen führen."},
            {"question": "Welche Lebensmittel sind magnesiumreich?",
             "answer": "Dunkelgrünes Blattgemüse (Spinat, Grünkohl), Nüsse (Mandeln, Cashews), Samen (Kürbiskerne, Chiasamen), Vollkornprodukte, Hülsenfrüchte, dunkle Schokolade (70 %+ Kakao), Avocados und Bananen."},
        ],
        "fr": [
            {"question": "Qu'est-ce qu'une analyse de magnésium sanguin ?",
             "answer": "C'est une analyse qui mesure le taux de magnésium dans le sérum sanguin. Le magnésium est un minéral essentiel impliqué dans plus de 300 réactions enzymatiques, dont la fonction musculaire, le rythme cardiaque et le métabolisme énergétique. La plage normale est généralement de 1,7–2,2 mg/dL."},
            {"question": "Quelles sont les causes d'un taux bas de magnésium ?",
             "answer": "Les causes courantes comprennent un apport alimentaire insuffisant, des troubles de la malabsorption (maladie cœliaque, maladie de Crohn), l'alcoolisme chronique, un diabète mal contrôlé et l'utilisation prolongée de diurétiques et d'inhibiteurs de la pompe à protons (IPP)."},
            {"question": "Quels sont les symptômes d'une carence en magnésium ?",
             "answer": "Les symptômes peuvent inclure des crampes musculaires, des fasciculations, une fatigue chronique, des engourdissements et picotements, une arythmie, une perte d'appétit et des nausées. Une carence sévère peut entraîner des convulsions et des changements de personnalité."},
            {"question": "Quels aliments sont riches en magnésium ?",
             "answer": "Les légumes à feuilles vert foncé (épinards, chou frisé), les noix (amandes, noix de cajou), les graines (courge, chia), les céréales complètes, les légumineuses, le chocolat noir (70 %+ cacao), les avocats et les bananes."},
        ],
        "it": [
            {"question": "Cos'è un'analisi del magnesio nel sangue?",
             "answer": "È un esame che misura il livello di magnesio nel siero sanguigno. Il magnesio è un minerale essenziale coinvolto in oltre 300 reazioni enzimatiche, tra cui funzione muscolare, ritmo cardiaco e metabolismo energetico. Il range normale è tipicamente 1,7–2,2 mg/dL."},
            {"question": "Quali sono le cause del magnesio basso?",
             "answer": "Le cause comuni includono scarso apporto alimentare, malassorbimento (celiachia, morbo di Crohn), alcolismo cronico, diabete scarsamente controllato e uso prolungato di diuretici e inibitori di pompa protonica (IPP)."},
            {"question": "Quali sono i sintomi della carenza di magnesio?",
             "answer": "I sintomi possono includere crampi muscolari, fascicolazioni, stanchezza cronica, intorpidimento e formicolio, aritmia, perdita di appetito e nausea. La carenza grave può provocare convulsioni e cambiamenti della personalità."},
            {"question": "Quali alimenti sono ricchi di magnesio?",
             "answer": "Verdure a foglia verde scuro (spinaci, cavolo riccio), frutta secca (mandorle, anacardi), semi (zucca, chia), cereali integrali, legumi, cioccolato fondente (70%+ cacao), avocado e banane."},
        ],
        "he": [
            {"question": "מהי בדיקת מגנזיום בדם?",
             "answer": "בדיקת מגנזיום בדם מודדת את רמת המגנזיום בסרום הדם. מגנזיום הוא מינרל חיוני המעורב ביותר מ-300 תגובות אנזימטיות, כולל תפקוד שרירים, קצב לב ומטבוליזם אנרגיה. הטווח התקין הוא בדרך כלל 1.7–2.2 mg/dL."},
            {"question": "מה גורם לרמות מגנזיום נמוכות?",
             "answer": "גורמים שכיחים כוללים צריכה תזונתית לא מספקת, הפרעות ספיגה (צליאק, קרוהן), אלכוהוליזם כרוני, סוכרת לא מאוזנת ושימוש ממושך במשתנים ומעכבי משאבת פרוטונים (PPI)."},
            {"question": "מהם התסמינים של מחסור במגנזיום?",
             "answer": "התסמינים עשויים לכלול התכווצויות שרירים, פרפורים, עייפות כרונית, חוסר תחושה ועקצוצים, הפרעת קצב, ירידה בתיאבון ובחילות. מחסור חמור עלול לגרום לפרכוסים ושינויי אישיות."},
            {"question": "אילו מאכלים עשירים במגנזיום?",
             "answer": "ירקות עליים ירוקים כהים (תרד, קייל), אגוזים (שקדים, קשיו), זרעים (גרעיני דלעת, צ'יה), דגנים מלאים, קטניות, שוקולד מריר (70%+ קקאו), אבוקדו ובננות."},
        ],
        "hi": [
            {"question": "मैग्नीशियम ब्लड टेस्ट क्या है?",
             "answer": "मैग्नीशियम ब्लड टेस्ट आपके रक्त सीरम में मैग्नीशियम के स्तर को मापता है। मैग्नीशियम एक आवश्यक खनिज है जो 300 से अधिक एंज़ाइमेटिक प्रतिक्रियाओं में शामिल होता है, जिसमें मांसपेशी कार्य, हृदय लय और ऊर्जा चयापचय शामिल हैं। सामान्य रेंज आमतौर पर 1.7–2.2 mg/dL होती है।"},
            {"question": "कम मैग्नीशियम के कारण क्या हैं?",
             "answer": "सामान्य कारणों में अपर्याप्त आहार सेवन, सीलिएक और क्रोहन जैसी कुअवशोषण बीमारियाँ, दीर्घकालिक शराब सेवन, अनियंत्रित मधुमेह और मूत्रवर्धक व PPI का लंबे समय तक उपयोग शामिल हैं।"},
            {"question": "मैग्नीशियम की कमी के लक्षण क्या हैं?",
             "answer": "लक्षणों में मांसपेशियों में ऐंठन, फड़कन, दीर्घकालिक थकान, सुन्नपन और झुनझुनी, अनियमित दिल की धड़कन (अतालता), भूख न लगना और मतली शामिल हो सकती है। गंभीर कमी से दौरे और व्यक्तित्व परिवर्तन हो सकते हैं।"},
            {"question": "कौन से खाद्य पदार्थ मैग्नीशियम से भरपूर हैं?",
             "answer": "गहरी हरी पत्तेदार सब्ज़ियाँ (पालक, केल), मेवे (बादाम, काजू), बीज (कद्दू के बीज, चिया), साबुत अनाज, फलियाँ, डार्क चॉकलेट (70%+ कोको), एवोकाडो और केले।"},
        ],
        "ar": [
            {"question": "ما هو تحليل المغنيسيوم في الدم؟",
             "answer": "تحليل المغنيسيوم في الدم يقيس مستوى المغنيسيوم في مصل الدم. المغنيسيوم معدن أساسي يشارك في أكثر من 300 تفاعل إنزيمي، بما في ذلك وظيفة العضلات ونظم القلب والتمثيل الغذائي للطاقة. النطاق الطبيعي عادة 1.7–2.2 mg/dL."},
            {"question": "ما أسباب انخفاض مستويات المغنيسيوم؟",
             "answer": "الأسباب الشائعة تشمل نقص المدخول الغذائي، اضطرابات سوء الامتصاص (الداء البطني، كرون)، إدمان الكحول المزمن، السكري غير المنضبط والاستخدام المطوّل لمدرات البول ومثبطات مضخة البروتون (PPI)."},
            {"question": "ما أعراض نقص المغنيسيوم؟",
             "answer": "قد تشمل الأعراض تشنجات العضلات والارتعاش والتعب المزمن والخدر والتنميل واضطراب نظم القلب وفقدان الشهية والغثيان. النقص الشديد قد يسبب نوبات صرعية وتغيرات في الشخصية."},
            {"question": "ما الأطعمة الغنية بالمغنيسيوم؟",
             "answer": "الخضروات الورقية الداكنة (السبانخ، الكيل)، المكسرات (اللوز، الكاجو)، البذور (بذور القرع، الشيا)، الحبوب الكاملة، البقوليات، الشوكولاتة الداكنة (70%+ كاكاو)، الأفوكادو والموز."},
        ],
    }
