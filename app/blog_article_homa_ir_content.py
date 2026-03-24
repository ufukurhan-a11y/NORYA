# -*- coding: utf-8 -*-
"""
HOMA-IR blog article — full body content for all 9 languages.
Used by blog_i18n._article_homa_ir().
Sections: intro, what-is-homa-ir, how-calculated, fasting-glucose-relation,
fasting-insulin-relation, insulin-resistance-connection, not-enough-alone,
evaluating-results, when-to-see-doctor, how-norya-helps, disclaimer.
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
            heading="HOMA-IR nedir ve neden önemlidir?",
            body_html=(
                "<p>Laboratuvar raporunuzda <strong>HOMA-IR</strong> değerini gördüğünüzde "
                "ilk akla gelen soru genellikle şu olur: Bu sayı ne anlama geliyor ve endişelenmeli "
                "miyim? HOMA-IR, vücudunuzun insüline ne kadar duyarlı olduğunu gösteren hesaplanmış "
                "bir indekstir. Doğrudan ölçülen bir parametre değildir; açlık kan şekeri ve açlık "
                "insülin düzeylerinden yola çıkılarak elde edilir. Son yıllarda metabolik sağlık "
                "değerlendirmesinde giderek daha sık kullanılmakta ve özellikle insülin direnci riski "
                "taşıyan bireylerde erken uyarı aracı olarak değer kazanmaktadır.</p>"
                "<p>Bu rehber HOMA-IR&rsquo;nin ne olduğunu, nasıl hesaplandığını, hangi durumlarda "
                "yükselebileceğini ve tek başına yeterli bir gösterge olup olmadığını sade bir dille "
                "açıklamayı amaçlıyor. Amacımız teşhis koymak değil; sonucunuzu daha iyi anlayarak "
                "hekiminizle verimli bir görüşme yapmanıza yardımcı olmaktır.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="HOMA-IR tam olarak nedir?",
            body_html=(
                "<p><strong>HOMA-IR</strong> (Homeostatic Model Assessment for Insulin Resistance), "
                "1985 yılında Matthews ve arkadaşları tarafından geliştirilen ve insülin direncini "
                "dolaylı yoldan değerlendirmeye yarayan matematiksel bir modeldir. Açlık durumunda "
                "kanda bulunan insülin ve glukoz miktarlarının birbirleriyle olan ilişkisinden yola "
                "çıkar. Sağlıklı bir metabolizmada pankreas yeterli miktarda insülin üretir ve "
                "hücreler bu insüline yanıt vererek glukozu enerjiye dönüştürür. Ancak hücreler "
                "insüline karşı duyarsızlaşmaya başladığında pankreas daha fazla insülin salgılamak "
                "zorunda kalır; işte HOMA-IR bu dengesizliği sayısal olarak ifade eder.</p>"
                "<p>Klinik pratikte HOMA-IR, özellikle hiperinsülinemik öglisemik klemp gibi karmaşık "
                "ve pahalı testlere gerek kalmadan insülin direncini taramak amacıyla kullanılır. "
                "Tam kan sayımı veya biyokimya paneli kadar yaygın olmasa da, metabolik sendrom, "
                "tip 2 diyabet riski, polikistik over sendromu (PKOS) ve alkole bağlı olmayan "
                "yağlı karaciğer hastalığı (NAYKH) değerlendirmesinde hekimler tarafından sıklıkla "
                "istenmektedir. Değerin tek başına tanı koydurucu olmadığını, klinik bağlamla "
                "birlikte yorumlanması gerektiğini baştan belirtmek gerekir.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="HOMA-IR nasıl hesaplanır?",
            body_html=(
                "<p>HOMA-IR hesaplaması oldukça basit bir formüle dayanır:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Birim sistemi</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Formül</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL (Türkiye&rsquo;de yaygın)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Açlık insülini (μU/mL) &times; Açlık glukozu (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Açlık insülini (μU/mL) &times; Açlık glukozu (mmol/L) &divide; 22,5</td>'
                "</tr></tbody></table>"
                "<p>Formüldeki sabitler (405 ve 22,5) sağlıklı bireylerin ortalamasından elde edilen "
                "kalibrasyon değerleridir. Her iki formül de aynı sonucu verir; fark yalnızca "
                "glukozun hangi birimle ölçüldüğüne bağlıdır. Türkiye&rsquo;deki laboratuvarlar "
                "genellikle mg/dL kullandığından 405&rsquo;e bölme formülü daha sık karşınıza çıkar.</p>"
                "<p>Örneğin açlık insülininiz 10&nbsp;μU/mL, açlık glukozunuz 90&nbsp;mg/dL ise: "
                "HOMA-IR&nbsp;=&nbsp;(10&nbsp;&times;&nbsp;90)&nbsp;/&nbsp;405&nbsp;=&nbsp;2,22. "
                "Bu değerin ne anlama geldiğini ilerleyen bölümlerde ele alacağız; ancak hesaplamanın "
                "doğru olabilmesi için kan örneğinin en az 8&ndash;12 saatlik açlık sonrası "
                "alınmış olması gerektiğini hatırlatmak isteriz.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="Açlık kan şekeri ile ilişkisi",
            body_html=(
                "<p><strong>Açlık kan şekeri (glukoz)</strong>, en az 8 saat boyunca yeme içme "
                "yapılmadan ölçülen kan şekeri düzeyidir. Normal bireylerde bu değer genellikle "
                "70&ndash;100&nbsp;mg/dL arasında seyreder. Açlık glukozu HOMA-IR formülünün iki "
                "bileşeninden biridir; dolayısıyla açlık kan şekeri tek başına normal aralıkta "
                "görünse bile insülin düzeyi yüksekse HOMA-IR yükselir.</p>"
                "<p>Bu neden önemli? Çünkü insülin direncinin erken evrelerinde açlık kan şekeri "
                "uzun süre normal kalabilir. Pankreas, glukozu normal sınırda tutmak için fazla "
                "insülin salgılar; bu durumda yalnızca açlık kan şekerine bakarsanız bir sorun "
                "göremezsiniz. HOMA-IR, insülin ve glukozu birlikte değerlendirdiği için bu "
                "&ldquo;gizli&rdquo; dengesizliği daha erken yakalayabilir. Açlık kan şekeri "
                "konusunda daha fazla bilgi için "
                '<a href="/tr/blog/aclik-kan-sekeri-sonucu-nasil-degerlendirilir">açlık kan şekeri rehberimiz</a>e '
                "göz atabilirsiniz.</p>"
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="Açlık insülini ile ilişkisi",
            body_html=(
                "<p><strong>Açlık insülini</strong>, yine en az 8&ndash;12 saatlik açlık sonrası "
                "ölçülen insülin düzeyidir. Sağlıklı bireylerde genellikle 2&ndash;25&nbsp;μU/mL "
                "aralığında beklenir, ancak laboratuvarlar arasında referans aralıkları "
                "farklılık gösterebilir. Açlık insülini HOMA-IR formülünün ikinci temel bileşenidir "
                "ve aslında insülin direncinin en doğrudan yansımasıdır.</p>"
                "<p>Hücreler insüline karşı duyarsızlaşmaya başladığında pankreas, kan şekerini "
                "kontrol altında tutabilmek için daha fazla insülin üretir. Bu durum "
                "<em>kompansatuvar hiperinsülinemi</em> olarak adlandırılır. Açlık insülin düzeyi "
                "yükseldiğinde—kan şekeri henüz normal aralıkta bile olsa—HOMA-IR değeri artar ve "
                "insülin direncine işaret edebilir. Dolayısıyla açlık insülini, metabolik sağlık "
                "değerlendirmesinde açlık glukozunun gösteremediği erken uyarıyı verebilir.</p>"
                "<p>Ancak insülin ölçümünde dikkat edilmesi gereken noktalar vardır: stres, "
                "uykusuzluk, bazı ilaçlar ve hatta ölçüm sırasında kullanılan laboratuvar yöntemi "
                "sonucu etkileyebilir. Bu nedenle tek bir değer yerine klinik tablonun bütünü "
                "değerlendirilmelidir.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="İnsülin direnci ile bağlantısı",
            body_html=(
                "<p><strong>İnsülin direnci</strong>, hücrelerin insüline normalden daha az yanıt "
                "vermesi durumudur. Bu süreçte pankreas daha fazla insülin üreterek kan şekerini "
                "dengelemeye çalışır; ancak zamanla bu telafi mekanizması yetersiz kalabilir ve "
                "kan şekeri yükselmeye başlar. İnsülin direnci; metabolik sendrom, tip&nbsp;2 "
                "diyabet, kardiyovasküler hastalık, PKOS ve NAYKH ile yakından ilişkilidir.</p>"
                "<p>HOMA-IR, bu sürecin erken evrelerini yakalamaya yardımcı olabilir. Pek çok "
                "kaynakta HOMA-IR değerinin 1,0&rsquo;ın altında olması optimal kabul edilirken, "
                "2,5&ndash;2,9 üzeri değerler insülin direncine işaret edebilir. Ancak bu eşik "
                "değerleri popülasyona, etnik yapıya, yaş grubuna ve laboratuvara göre "
                "farklılık gösterir; evrensel tek bir kesim noktası yoktur.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">HOMA-IR aralığı</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Genel yorum (referans amaçlı)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Optimal insülin duyarlılığı</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,0 &ndash; 2,4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal / sınırda — klinik bağlam önemli</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2,5 &ndash; 2,9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">İnsülin direnci olasılığı artar</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Belirgin insülin direnci düşündürür</td>'
                "</tr></tbody></table>"
                "<p>Yukarıdaki tablo yalnızca genel bir yönlendirme amacı taşır. Hekiminiz bu "
                "değeri sizin klinik tablonuz, aile öykünüz, vücut kitle indeksiniz ve diğer "
                "laboratuvar bulgularınız ışığında yorumlayacaktır.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="HOMA-IR tek başına yeterli mi?",
            body_html=(
                "<p>Kısa yanıt: <strong>hayır</strong>. HOMA-IR, insülin direncini taramak için "
                "kullanışlı bir araçtır; ancak kesinlikle tek başına tanı koydurmaz. Birkaç "
                "önemli kısıtlaması vardır:</p>"
                "<ul>"
                "<li>Formül yalnızca açlık değerlerine dayanır; yemek sonrası insülin ve glukoz "
                "dinamiklerini yansıtmaz.</li>"
                "<li>Stres, uykusuzluk, akut hastalık veya ölçümden önceki yoğun egzersiz "
                "sonucu geçici olarak değiştirebilir.</li>"
                "<li>Pankreas beta-hücre fonksiyonu ileri derecede bozulmuş kişilerde (örneğin "
                "ilerlemiş tip&nbsp;2 diyabet) insülin üretimi zaten azalmış olacağından HOMA-IR "
                "düşük çıkabilir ve yanıltıcı olabilir.</li>"
                "<li>Laboratuvarlar arası insülin ölçüm farklılıkları sonucu etkileyebilir.</li>"
                "</ul>"
                "<p>Bu nedenlerle HOMA-IR; açlık kan şekeri, HbA1c, lipid profili, karaciğer "
                "enzimleri ve klinik değerlendirmeyle birlikte yorumlanmalıdır. "
                '<a href="/tr/blog/hba1c-sonucu-ne-anlama-gelir">HbA1c yazımız</a> da '
                "uzun dönemli kan şekeri kontrolü hakkında ek bilgi sunar.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="Sonuçları değerlendirirken nelere dikkat etmeli?",
            body_html=(
                "<p>HOMA-IR sonucunuzu değerlendirirken aşağıdaki noktaları göz önünde "
                "bulundurmanız yararlı olacaktır:</p>"
                "<ul>"
                "<li><strong>Açlık süresi:</strong> Kan örneği en az 8&ndash;12 saatlik açlıktan "
                "sonra alınmalıdır. Yetersiz açlık, hem glukozu hem insülini etkileyerek sonucu "
                "bozabilir.</li>"
                "<li><strong>Stres ve uyku:</strong> Akut stres ve uyku bozuklukları kortizol "
                "düzeyini artırarak insülin ve glukoz dengesini geçici olarak değiştirebilir.</li>"
                "<li><strong>İlaçlar:</strong> Kortikosteroidler, bazı antipsikotikler ve diğer "
                "ilaçlar insülin duyarlılığını etkileyebilir. Kullandığınız ilaçları hekiminize "
                "mutlaka bildirin.</li>"
                "<li><strong>Beslenme ve egzersiz:</strong> Son günlerde alışılmadık diyet "
                "değişiklikleri veya yoğun fiziksel aktivite sonucu geçici olarak etkileyebilir.</li>"
                "<li><strong>Tek ölçüm vs. trend:</strong> Tek bir HOMA-IR değeri bir anlık "
                "fotoğraftır. Zaman içindeki değişim (trend) çok daha anlamlıdır.</li>"
                "<li><strong>Bireysel farklılıklar:</strong> Yaş, cinsiyet, etnik köken ve vücut "
                "kitle indeksi, &ldquo;normal&rdquo; kabul edilen aralığı değiştirebilir.</li>"
                "</ul>"
                "<p>Tüm bu faktörler nedeniyle, HOMA-IR sonucunuzu rapordaki tek bir sayı olarak "
                "değil, klinik tablonuzun bir parçası olarak görmeniz en doğrusudur.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman hekime başvurmalı?",
            body_html=(
                "<p>Aşağıdaki durumlardan herhangi biri varsa HOMA-IR sonucunuzu bir hekimle "
                "görüşmeniz önerilir:</p>"
                "<ul>"
                "<li>HOMA-IR değeriniz laboratuvarın referans aralığının üzerinde çıktıysa.</li>"
                "<li>Ailede tip&nbsp;2 diyabet, metabolik sendrom veya kardiyovasküler hastalık "
                "öyküsü varsa.</li>"
                "<li>Kilo almada zorluk yaşıyor veya açıklanamayan kilo artışı fark ediyorsanız.</li>"
                "<li>PKOS tanısı aldıysanız veya menstrüel düzensizlik yaşıyorsanız.</li>"
                "<li>Yorgunluk, aşırı susama, sık idrara çıkma gibi belirtiler varsa.</li>"
                "<li>Karaciğer enzimlerinde yükselme veya yağlı karaciğer bulgusu saptandıysa.</li>"
                "</ul>"
                "<p>Belirtiniz olmasa bile, HOMA-IR değeriniz yüksek çıktıysa bunu hekiminizle "
                "paylaşmak doğru adımdır. Erken müdahale—beslenme düzenlemesi, fiziksel aktivite "
                "artışı, gerekirse ilaç tedavisi—insülin direncinin ilerlemesini yavaşlatabilir "
                "veya geri döndürebilir.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI bu süreçte nasıl yardımcı olur?",
            body_html=(
                "<p>NoryaAI&rsquo;da teşhis koymuyoruz; amacımız laboratuvar raporunuzu daha "
                "anlaşılır hale getirmek ve hekim randevunuza hazırlanmanızı kolaylaştırmaktır. "
                '<a href="/analyze">Analiz sayfamıza</a> raporunuzu yükleyerek HOMA-IR dahil '
                "tüm değerlerinizin sade dilde, referans aralıkları ve bağlamıyla açıklandığı "
                "yapılandırılmış bir özet alabilirsiniz.</p>"
                "<p>Bu özet sayesinde hekiminize doğru soruları sorabilir, hangi değerlerin "
                "takip gerektirdiğini daha iyi anlayabilirsiniz. Teşhis veya tedavi önerisi "
                "vermiyoruz—sonuçlarınızı anlamanıza yardım ediyoruz. Seçenekler ve ücretler "
                'için <a href="/pricing">fiyatlandırma</a> sayfamızı inceleyebilirsiniz.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Yasal uyarı",
            body_html=(
                "<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye veya "
                "teşhis yerine geçmez.</strong> HOMA-IR değeriniz dahil tüm laboratuvar "
                "sonuçlarınızı mutlaka bir sağlık profesyoneli ile görüşün. Bireysel sağlık "
                "durumunuzu ancak öykünüzü ve klinik tablonuzu bilen bir hekim doğru "
                "değerlendirebilir.</p>"
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
            heading="What is HOMA-IR and why does it matter?",
            body_html=(
                "<p>If your lab report includes a value labelled <strong>HOMA-IR</strong>, you "
                "may be wondering what it means and whether you should be concerned. HOMA-IR is "
                "a calculated index that estimates how sensitive your body is to insulin. It is "
                "not measured directly; instead, it is derived from two routine blood tests—fasting "
                "glucose and fasting insulin. Over the past two decades it has become one of the "
                "most widely used surrogate markers for insulin resistance in clinical research "
                "and, increasingly, in everyday practice.</p>"
                "<p>This guide explains what HOMA-IR is, how the number is produced, what it can "
                "and cannot tell you, and when you should talk to your doctor about it. Our aim "
                "is not to diagnose anything—it is to help you walk into your next appointment "
                "with a clearer understanding of what this value represents.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="What exactly is HOMA-IR?",
            body_html=(
                "<p><strong>HOMA-IR</strong> stands for <em>Homeostatic Model Assessment for "
                "Insulin Resistance</em>. It was first described in 1985 by Matthews and "
                "colleagues as a way to estimate insulin resistance from a simple fasting blood "
                "sample, avoiding the complexity and cost of the gold-standard hyperinsulinaemic–"
                "euglycaemic clamp. The model works on a straightforward principle: in a healthy "
                "metabolism, the pancreas releases just enough insulin to keep blood glucose in "
                "a narrow range. When cells start resisting insulin&rsquo;s signal, the pancreas "
                "compensates by producing more. HOMA-IR captures that imbalance as a single number.</p>"
                "<p>Clinicians and researchers use HOMA-IR to screen for insulin resistance in "
                "contexts such as metabolic syndrome, pre-diabetes and type&nbsp;2 diabetes risk "
                "assessment, polycystic ovary syndrome (PCOS), and non-alcoholic fatty liver "
                "disease (NAFLD). It is important to understand from the outset that HOMA-IR is "
                "a <em>screening</em> tool, not a diagnostic test. A single value does not confirm "
                "or rule out any disease; it must always be interpreted alongside your clinical "
                "history, symptoms, and other laboratory findings.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="How is HOMA-IR calculated?",
            body_html=(
                "<p>The calculation is straightforward. Two formulas are in common use, depending "
                "on which unit your lab uses for glucose:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Glucose unit</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Formula</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Fasting insulin (μU/mL) &times; Fasting glucose (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Fasting insulin (μU/mL) &times; Fasting glucose (mmol/L) &divide; 22.5</td>'
                "</tr></tbody></table>"
                "<p>The constants 405 and 22.5 are calibration factors derived from population "
                "averages of healthy individuals. Both formulas yield the same result; the "
                "difference is purely in the glucose unit. For the calculation to be valid, the "
                "blood sample must be drawn after an overnight fast of at least 8–12 hours.</p>"
                "<p>As an example: if your fasting insulin is 8&nbsp;μU/mL and your fasting "
                "glucose is 95&nbsp;mg/dL, then HOMA-IR&nbsp;=&nbsp;(8&nbsp;&times;&nbsp;95)&nbsp;"
                "/&nbsp;405&nbsp;&asymp;&nbsp;1.88. We will discuss what that number means in "
                "subsequent sections.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="The relationship with fasting glucose",
            body_html=(
                "<p><strong>Fasting glucose</strong> (also called fasting blood sugar) is the "
                "concentration of glucose in your blood after at least 8 hours without food. In "
                "most laboratories, a normal fasting glucose is roughly 70–100&nbsp;mg/dL "
                "(3.9–5.6&nbsp;mmol/L). It is one of the two inputs to the HOMA-IR formula.</p>"
                "<p>A critical point is that fasting glucose can remain within the normal range "
                "for years even as insulin resistance develops. This happens because the pancreas "
                "increases insulin output to compensate—keeping glucose in check at the cost of "
                "higher insulin levels. If you look only at fasting glucose, you may miss this "
                "early metabolic shift. HOMA-IR, by incorporating insulin alongside glucose, can "
                "reveal the strain before glucose itself rises. For a deeper look at fasting "
                "blood sugar, see our "
                '<a href="/en/blog/how-to-read-fasting-blood-sugar-results">fasting blood sugar guide</a>.</p>'
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="The relationship with fasting insulin",
            body_html=(
                "<p><strong>Fasting insulin</strong> is the level of insulin circulating in your "
                "blood after an overnight fast. Typical reference ranges vary between labs but "
                "often fall between 2 and 25&nbsp;μU/mL. It is the second input to the HOMA-IR "
                "formula and, arguably, the more informative one in the context of early insulin "
                "resistance.</p>"
                "<p>When cells become less responsive to insulin, the pancreas compensates by "
                "secreting more—a state sometimes called <em>compensatory hyperinsulinaemia</em>. "
                "This elevated insulin keeps glucose levels stable, so fasting glucose may still "
                "look normal. The elevated fasting insulin, however, pushes the HOMA-IR value "
                "upward and may be one of the earliest detectable signs of metabolic trouble.</p>"
                "<p>It is worth noting that insulin assays vary between laboratories, and factors "
                "such as stress, poor sleep, medications (e.g. corticosteroids, certain "
                "antipsychotics), and even the timing of the blood draw can influence insulin "
                "levels. A single measurement is therefore a snapshot, not a verdict, and should "
                "be considered as part of the broader clinical picture.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="The connection to insulin resistance",
            body_html=(
                "<p><strong>Insulin resistance</strong> occurs when cells in muscle, fat, and "
                "liver respond less effectively to insulin&rsquo;s signal to take up glucose. The "
                "pancreas compensates by producing more insulin, but over time it may be unable "
                "to keep up, and blood glucose begins to rise. Insulin resistance is closely "
                "linked to metabolic syndrome, type&nbsp;2 diabetes, cardiovascular disease, "
                "PCOS, and NAFLD.</p>"
                "<p>Many references consider a HOMA-IR below 1.0 as optimal. Values above "
                "2.5–2.9 are often cited as suggestive of insulin resistance. However, these "
                "cut-offs are population-dependent; they can vary by ethnicity, age, sex, "
                "and the laboratory method used to measure insulin. There is no single universal "
                "threshold.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">HOMA-IR range</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">General interpretation (for reference)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Optimal insulin sensitivity</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.0 – 2.4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal / borderline — clinical context matters</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2.5 – 2.9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Increased likelihood of insulin resistance</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Strongly suggestive of insulin resistance</td>'
                "</tr></tbody></table>"
                "<p>The table above is a general guide only. Your doctor will interpret your "
                "value in the context of your full clinical picture, family history, BMI, and "
                "other lab findings.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Why HOMA-IR alone is not enough",
            body_html=(
                "<p>HOMA-IR is a useful screening tool, but it has important limitations:</p>"
                "<ul>"
                "<li>It is based solely on fasting values and does not capture post-meal insulin "
                "and glucose dynamics.</li>"
                "<li>Acute stress, illness, poor sleep, or intense exercise shortly before the "
                "blood draw can temporarily alter the result.</li>"
                "<li>In people with advanced beta-cell dysfunction (e.g. long-standing "
                "type&nbsp;2 diabetes), insulin production may already be reduced, which can "
                "make HOMA-IR misleadingly low.</li>"
                "<li>Insulin assay variability between labs means the same person may get "
                "slightly different results from different laboratories.</li>"
                "</ul>"
                "<p>For these reasons, HOMA-IR should always be considered alongside fasting "
                "glucose, HbA1c, lipid profile, liver enzymes, and a thorough clinical "
                "assessment. Our "
                '<a href="/en/blog/what-does-an-hba1c-result-mean">HbA1c article</a> provides '
                "additional context on long-term blood sugar control.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="What to consider when evaluating your result",
            body_html=(
                "<p>Before drawing conclusions from a single HOMA-IR value, keep the following "
                "factors in mind:</p>"
                "<ul>"
                "<li><strong>Fasting duration:</strong> The blood sample should be drawn after "
                "at least 8–12 hours of fasting. An insufficient fast will affect both glucose "
                "and insulin, distorting the result.</li>"
                "<li><strong>Stress and sleep:</strong> Acute stress and sleep deprivation raise "
                "cortisol, which in turn influences insulin and glucose balance.</li>"
                "<li><strong>Medications:</strong> Corticosteroids, certain antipsychotics, and "
                "other drugs can affect insulin sensitivity. Always tell your doctor what you "
                "are taking.</li>"
                "<li><strong>Diet and exercise:</strong> Unusual dietary changes or intense "
                "physical activity in the days before the test can temporarily shift results.</li>"
                "<li><strong>Single value vs. trend:</strong> A single HOMA-IR is a snapshot. "
                "The trend over time is far more meaningful.</li>"
                "<li><strong>Individual variation:</strong> Age, sex, ethnicity, and BMI can "
                "all influence what is considered a &ldquo;normal&rdquo; range for you.</li>"
                "</ul>"
                "<p>For all these reasons, treat your HOMA-IR as one piece of a larger puzzle, "
                "not as a standalone verdict on your metabolic health.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>Consider discussing your HOMA-IR result with a doctor if any of the "
                "following apply:</p>"
                "<ul>"
                "<li>Your HOMA-IR is above the laboratory&rsquo;s reference range.</li>"
                "<li>You have a family history of type&nbsp;2 diabetes, metabolic syndrome, or "
                "cardiovascular disease.</li>"
                "<li>You are experiencing unexplained weight gain or difficulty losing weight.</li>"
                "<li>You have been diagnosed with or are being evaluated for PCOS.</li>"
                "<li>You notice symptoms such as fatigue, excessive thirst, or frequent urination.</li>"
                "<li>Your liver enzymes are elevated or fatty liver has been noted on imaging.</li>"
                "</ul>"
                "<p>Even in the absence of symptoms, a raised HOMA-IR is worth mentioning to "
                "your doctor. Early intervention—dietary adjustments, increased physical activity, "
                "and sometimes medication—can slow or even reverse the progression of insulin "
                "resistance.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How NoryaAI can help",
            body_html=(
                "<p>At NoryaAI, we do not diagnose—we help you understand. You can "
                '<a href="/analyze">upload your lab report</a> and receive a clear, structured '
                "summary that explains your values—including HOMA-IR—in plain language, with "
                "reference ranges and context. This makes it easier to prepare for your "
                "doctor&rsquo;s appointment and to ask the right questions.</p>"
                "<p>We do not offer treatment recommendations or diagnostic conclusions. Our "
                "goal is to bridge the gap between a confusing lab report and a productive "
                "conversation with your healthcare provider. For options and pricing, see our "
                '<a href="/pricing">pricing</a> page.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This content is for information only and does not replace medical "
                "advice or diagnosis.</strong> HOMA-IR and all other lab values should always "
                "be discussed with a qualified healthcare professional. Only a doctor who knows "
                "your history and clinical context can interpret your results properly.</p>"
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
            heading="Was ist der HOMA-IR und warum ist er wichtig?",
            body_html=(
                "<p>Wenn auf Ihrem Laborbefund der Wert <strong>HOMA-IR</strong> auftaucht, "
                "fragen Sie sich vielleicht: Was sagt diese Zahl aus, und muss ich mir Sorgen "
                "machen? Der HOMA-IR ist ein rechnerischer Index, der abschätzt, wie empfindlich "
                "Ihr Körper auf Insulin reagiert. Er wird nicht direkt im Blut gemessen, sondern "
                "aus zwei Routinewerten berechnet — dem Nüchternblutzucker und dem "
                "Nüchterninsulin. In der metabolischen Diagnostik hat er sich als einfaches "
                "Screening-Instrument etabliert, insbesondere zur Früherkennung einer "
                "Insulinresistenz.</p>"
                "<p>Dieser Ratgeber erklärt, was der HOMA-IR misst, wie er berechnet wird, "
                "welche Grenzen er hat und wann ein Arztgespräch sinnvoll ist. Unser Ziel ist "
                "nicht die Diagnose, sondern ein besseres Verständnis Ihrer Laborwerte, damit "
                "Sie gut vorbereitet in Ihr nächstes Arztgespräch gehen.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="Was genau ist der HOMA-IR?",
            body_html=(
                "<p><strong>HOMA-IR</strong> steht für <em>Homeostatic Model Assessment for "
                "Insulin Resistance</em>. Das Modell wurde 1985 von Matthews und Kollegen "
                "veröffentlicht und ermöglicht eine Abschätzung der Insulinresistenz anhand "
                "einer einfachen Nüchternblutprobe — ohne den aufwändigen und teuren "
                "hyperinsulinämisch-euglykämischen Clamp-Test. Das Prinzip ist einleuchtend: "
                "Im gesunden Stoffwechsel schüttet die Bauchspeicheldrüse genau so viel Insulin "
                "aus, wie nötig ist, um den Blutzucker in einem engen Bereich zu halten. Werden "
                "die Zellen zunehmend insulinresistent, muss die Bauchspeicheldrüse mehr Insulin "
                "produzieren. Der HOMA-IR bildet dieses Ungleichgewicht als Zahlenwert ab.</p>"
                "<p>In der Praxis wird der HOMA-IR bei der Abklärung von metabolischem Syndrom, "
                "Typ-2-Diabetes-Risiko, polyzystischem Ovarialsyndrom (PCOS) und "
                "nicht-alkoholischer Fettlebererkrankung (NAFLD) eingesetzt. Wichtig: Der "
                "HOMA-IR ist ein <em>Screening</em>-Instrument, kein diagnostischer Test. Ein "
                "einzelner Wert bestätigt oder schließt keine Erkrankung aus — er muss immer im "
                "klinischen Gesamtzusammenhang bewertet werden.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="Wie wird der HOMA-IR berechnet?",
            body_html=(
                "<p>Die Berechnung ist unkompliziert. Je nach Einheit des Blutzuckers gibt es "
                "zwei gebräuchliche Formeln:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Glukose-Einheit</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Formel</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Nüchterninsulin (μU/mL) &times; Nüchternglukose (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L (in Deutschland üblich)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Nüchterninsulin (μU/mL) &times; Nüchternglukose (mmol/L) &divide; 22,5</td>'
                "</tr></tbody></table>"
                "<p>Die Konstanten 405 und 22,5 sind Kalibrierfaktoren, die aus Durchschnittswerten "
                "gesunder Probanden abgeleitet wurden. Beide Formeln liefern dasselbe Ergebnis; der "
                "Unterschied liegt allein in der Glukose-Einheit. In Deutschland verwenden viele "
                "Labore mmol/L, weshalb die Formel mit 22,5 häufiger anzutreffen ist.</p>"
                "<p>Beispiel: Nüchterninsulin 9&nbsp;μU/mL, Nüchternglukose 5,2&nbsp;mmol/L — "
                "HOMA-IR&nbsp;=&nbsp;(9&nbsp;&times;&nbsp;5,2)&nbsp;/&nbsp;22,5&nbsp;&asymp;&nbsp;2,08. "
                "Was diese Zahl bedeutet, erfahren Sie in den folgenden Abschnitten. Voraussetzung "
                "für ein zuverlässiges Ergebnis ist eine Nüchternperiode von mindestens "
                "8–12&nbsp;Stunden vor der Blutentnahme.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="Der Zusammenhang mit dem Nüchternblutzucker",
            body_html=(
                "<p>Der <strong>Nüchternblutzucker</strong> ist die Glukosekonzentration im Blut "
                "nach mindestens 8 Stunden ohne Nahrungsaufnahme. Im Normalbereich liegt er bei "
                "etwa 3,9–5,6&nbsp;mmol/L (70–100&nbsp;mg/dL). Er ist einer der beiden Werte, "
                "die in die HOMA-IR-Formel eingehen.</p>"
                "<p>Ein wichtiger Punkt: Der Nüchternblutzucker kann über Jahre im Normbereich "
                "bleiben, obwohl sich bereits eine Insulinresistenz entwickelt. Die "
                "Bauchspeicheldrüse gleicht die verminderte Insulinwirkung durch Mehrproduktion "
                "aus — der Blutzucker bleibt stabil, aber der Insulinspiegel steigt. Schaut man "
                "nur auf den Nüchternblutzucker, entgeht einem diese frühe Verschiebung. Der "
                "HOMA-IR kombiniert beide Werte und kann deshalb die Belastung des Systems "
                "früher sichtbar machen. Mehr zum Nüchternblutzucker finden Sie in unserem "
                '<a href="/de/blog/nuechternblutzucker-verstehen">Nüchternblutzucker-Ratgeber</a>.</p>'
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="Der Zusammenhang mit dem Nüchterninsulin",
            body_html=(
                "<p>Das <strong>Nüchterninsulin</strong> wird ebenfalls nach mindestens "
                "8–12&nbsp;Stunden Nahrungskarenz bestimmt. Übliche Referenzbereiche liegen "
                "bei etwa 2–25&nbsp;μU/mL, können aber je nach Labor variieren. Es ist der "
                "zweite Baustein der HOMA-IR-Formel — und oft der aussagekräftigere, wenn es "
                "um die Früherkennung einer Insulinresistenz geht.</p>"
                "<p>Reagieren die Zellen schwächer auf Insulin, steigert die Bauchspeicheldrüse "
                "die Ausschüttung — eine <em>kompensatorische Hyperinsulinämie</em>. Das hält "
                "den Blutzucker zunächst stabil, erhöht aber den HOMA-IR und kann ein frühes "
                "Zeichen für metabolische Belastung sein.</p>"
                "<p>Zu beachten ist, dass Insulin-Assays zwischen Laboren variieren und Faktoren "
                "wie Stress, Schlafmangel, Medikamente (z.&nbsp;B. Kortikosteroide, bestimmte "
                "Antipsychotika) sowie der Zeitpunkt der Blutentnahme die Messung beeinflussen "
                "können. Ein einzelner Wert ist daher eine Momentaufnahme und sollte im "
                "Gesamtkontext betrachtet werden.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="Der Zusammenhang mit Insulinresistenz",
            body_html=(
                "<p><strong>Insulinresistenz</strong> bedeutet, dass Muskel-, Fett- und "
                "Leberzellen vermindert auf Insulin ansprechen. Die Bauchspeicheldrüse "
                "kompensiert zunächst durch Mehrproduktion; gelingt das auf Dauer nicht mehr, "
                "steigt der Blutzucker. Insulinresistenz ist eng mit dem metabolischen Syndrom, "
                "Typ-2-Diabetes, kardiovaskulären Erkrankungen, PCOS und NAFLD verknüpft.</p>"
                "<p>Viele Quellen betrachten einen HOMA-IR unter 1,0 als optimal. Werte über "
                "2,5–2,9 gelten häufig als Hinweis auf eine Insulinresistenz. Diese Grenzwerte "
                "sind allerdings populations-, alters- und laborabhängig — einen universellen "
                "Schwellenwert gibt es nicht.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">HOMA-IR-Bereich</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Allgemeine Einordnung (zur Orientierung)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Optimale Insulinempfindlichkeit</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,0 – 2,4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal / grenzwertig — klinischer Kontext entscheidet</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2,5 – 2,9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Erhöhte Wahrscheinlichkeit einer Insulinresistenz</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Deutlicher Hinweis auf Insulinresistenz</td>'
                "</tr></tbody></table>"
                "<p>Die Tabelle dient nur der Orientierung. Ihr Arzt wird den Wert im Kontext "
                "Ihres Gesamtbefundes, Ihrer Familienanamnese, Ihres BMI und weiterer "
                "Laborergebnisse interpretieren.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Warum der HOMA-IR allein nicht ausreicht",
            body_html=(
                "<p>Der HOMA-IR ist ein nützliches Screening-Instrument, hat aber klare Grenzen:</p>"
                "<ul>"
                "<li>Er basiert ausschließlich auf Nüchternwerten und bildet die Insulin- und "
                "Glukosedynamik nach dem Essen nicht ab.</li>"
                "<li>Akuter Stress, Schlafmangel, eine akute Erkrankung oder intensiver Sport "
                "kurz vor der Blutentnahme können das Ergebnis vorübergehend verfälschen.</li>"
                "<li>Bei Patienten mit fortgeschrittener Betazell-Dysfunktion (z.&nbsp;B. "
                "langjährigem Typ-2-Diabetes) kann die Insulinproduktion bereits vermindert "
                "sein, was den HOMA-IR fälschlich niedrig erscheinen lässt.</li>"
                "<li>Unterschiedliche Insulin-Assays zwischen Laboren können zu leicht "
                "abweichenden Ergebnissen führen.</li>"
                "</ul>"
                "<p>Deshalb sollte der HOMA-IR stets zusammen mit Nüchternblutzucker, HbA1c, "
                "Lipidprofil, Leberenzymen und einer ärztlichen Beurteilung betrachtet werden. "
                "Unser "
                '<a href="/de/blog/hba1c-verstehen-was-bedeutet-der-wert">HbA1c-Artikel</a> '
                "bietet weitere Informationen zur langfristigen Blutzuckerkontrolle.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="Worauf Sie bei der Bewertung achten sollten",
            body_html=(
                "<p>Bevor Sie aus einem einzelnen HOMA-IR-Wert Schlüsse ziehen, bedenken Sie "
                "folgende Punkte:</p>"
                "<ul>"
                "<li><strong>Nüchternzeit:</strong> Die Blutentnahme sollte nach mindestens "
                "8–12 Stunden Nahrungskarenz erfolgen. Eine unzureichende Nüchternheit "
                "verfälscht sowohl Glukose als auch Insulin.</li>"
                "<li><strong>Stress und Schlaf:</strong> Akuter Stress und Schlafmangel erhöhen "
                "den Cortisolspiegel und beeinflussen Insulin- und Glukosehaushalt.</li>"
                "<li><strong>Medikamente:</strong> Kortikosteroide, bestimmte Antipsychotika und "
                "andere Arzneimittel können die Insulinempfindlichkeit verändern. Informieren "
                "Sie Ihren Arzt über alle Medikamente, die Sie einnehmen.</li>"
                "<li><strong>Ernährung und Bewegung:</strong> Ungewöhnliche Ernährungsänderungen "
                "oder intensiver Sport in den Tagen vor dem Test können das Ergebnis "
                "vorübergehend beeinflussen.</li>"
                "<li><strong>Einzelwert vs. Verlauf:</strong> Ein einzelner HOMA-IR ist eine "
                "Momentaufnahme. Der Verlauf über die Zeit ist wesentlich aussagekräftiger.</li>"
                "<li><strong>Individuelle Unterschiede:</strong> Alter, Geschlecht, Ethnie und "
                "BMI beeinflussen, was als &bdquo;normal&ldquo; gilt.</li>"
                "</ul>"
                "<p>Betrachten Sie Ihren HOMA-IR daher als einen Baustein im Gesamtbild — nicht "
                "als alleinige Aussage über Ihren Stoffwechsel.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie zum Arzt?",
            body_html=(
                "<p>Sprechen Sie Ihren HOMA-IR-Wert mit einem Arzt, wenn einer der folgenden "
                "Punkte zutrifft:</p>"
                "<ul>"
                "<li>Ihr HOMA-IR liegt über dem Referenzbereich des Labors.</li>"
                "<li>In Ihrer Familie gibt es Fälle von Typ-2-Diabetes, metabolischem Syndrom "
                "oder Herz-Kreislauf-Erkrankungen.</li>"
                "<li>Sie nehmen unerklärlich an Gewicht zu oder haben Schwierigkeiten, Gewicht "
                "zu verlieren.</li>"
                "<li>Bei Ihnen wurde ein PCOS diagnostiziert oder es wird abgeklärt.</li>"
                "<li>Sie bemerken Symptome wie Müdigkeit, übermäßigen Durst oder häufiges "
                "Wasserlassen.</li>"
                "<li>Ihre Leberwerte sind erhöht oder eine Fettleber wurde festgestellt.</li>"
                "</ul>"
                "<p>Auch ohne Beschwerden lohnt es sich, einen erhöhten HOMA-IR ärztlich "
                "einordnen zu lassen. Frühe Maßnahmen — Ernährungsumstellung, mehr Bewegung, "
                "gegebenenfalls medikamentöse Therapie — können die Entwicklung einer "
                "Insulinresistenz verlangsamen oder umkehren.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie NoryaAI dabei helfen kann",
            body_html=(
                "<p>Bei NoryaAI stellen wir keine Diagnosen — wir helfen Ihnen, Ihre Laborwerte "
                "besser zu verstehen. Laden Sie Ihren Befund auf unserer "
                '<a href="/analyze">Analyse</a>-Seite hoch und erhalten Sie eine übersichtliche '
                "Zusammenfassung, die Ihre Werte — einschließlich HOMA-IR — in verständlicher "
                "Sprache mit Referenzbereichen und Kontext erklärt.</p>"
                "<p>So können Sie sich gezielt auf Ihr Arztgespräch vorbereiten und die richtigen "
                "Fragen stellen. Wir geben keine Therapieempfehlungen und keine diagnostischen "
                "Einschätzungen ab. Informationen zu unseren Optionen finden Sie auf der "
                '<a href="/pricing">Preise</a>-Seite.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Haftungsausschluss",
            body_html=(
                "<p><strong>Dieser Inhalt dient ausschließlich der Information und ersetzt "
                "keine ärztliche Beratung oder Diagnose.</strong> Besprechen Sie Ihren HOMA-IR "
                "und alle weiteren Laborwerte immer mit einem qualifizierten Arzt. Nur ein Arzt, "
                "der Ihre Vorgeschichte und Ihren klinischen Kontext kennt, kann Ihre Ergebnisse "
                "richtig einordnen.</p>"
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
            heading="¿Qué es el HOMA-IR y por qué importa?",
            body_html=(
                "<p>Si en tu analítica aparece un valor llamado <strong>HOMA-IR</strong>, es "
                "natural preguntarse qué significa y si hay motivo de preocupación. El HOMA-IR "
                "es un índice calculado que estima la sensibilidad de tu cuerpo a la insulina. "
                "No se mide directamente en sangre, sino que se obtiene a partir de dos análisis "
                "rutinarios: la glucosa en ayunas y la insulina en ayunas. En la evaluación "
                "metabólica actual, se ha convertido en una herramienta de cribado sencilla y "
                "ampliamente utilizada, sobre todo para detectar de forma temprana la resistencia "
                "a la insulina.</p>"
                "<p>Esta guía explica qué es el HOMA-IR, cómo se calcula, qué puede y qué no "
                "puede decirnos, y cuándo conviene consultar con el médico. No pretendemos "
                "diagnosticar nada; queremos ayudarte a entender tu resultado para que vayas "
                "a la consulta con información clara.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="¿Qué es exactamente el HOMA-IR?",
            body_html=(
                "<p><strong>HOMA-IR</strong> son las siglas de <em>Homeostatic Model Assessment "
                "for Insulin Resistance</em> (evaluación del modelo homeostático para la "
                "resistencia a la insulina). Fue descrito en 1985 por Matthews y colaboradores "
                "como una forma de estimar la resistencia a la insulina a partir de una muestra "
                "de sangre en ayunas, sin necesidad de recurrir a pruebas complejas y costosas "
                "como el clamp euglucémico hiperinsulinémico. El principio es sencillo: en un "
                "metabolismo sano, el páncreas libera la cantidad justa de insulina para mantener "
                "la glucosa en un rango estrecho. Cuando las células empiezan a responder peor "
                "a la insulina, el páncreas compensa produciendo más. El HOMA-IR expresa ese "
                "desequilibrio en una cifra.</p>"
                "<p>En la práctica clínica, se utiliza en el estudio del síndrome metabólico, "
                "el riesgo de diabetes tipo&nbsp;2, el síndrome de ovario poliquístico (SOP) y "
                "la enfermedad por hígado graso no alcohólico (EHGNA). Es fundamental tener "
                "claro desde el inicio que el HOMA-IR es una herramienta de <em>cribado</em>, "
                "no una prueba diagnóstica. Un solo valor no confirma ni descarta ninguna "
                "enfermedad; siempre debe interpretarse junto con la historia clínica, los "
                "síntomas y otros datos de laboratorio.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="¿Cómo se calcula el HOMA-IR?",
            body_html=(
                "<p>El cálculo es bastante directo. Existen dos fórmulas, según la unidad de "
                "la glucosa:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Unidad de glucosa</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Fórmula</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL (habitual en España y Latinoamérica)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Insulina en ayunas (μU/mL) &times; Glucosa en ayunas (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Insulina en ayunas (μU/mL) &times; Glucosa en ayunas (mmol/L) &divide; 22,5</td>'
                "</tr></tbody></table>"
                "<p>Las constantes 405 y 22,5 son factores de calibración derivados de promedios "
                "de individuos sanos. Ambas fórmulas dan el mismo resultado; la diferencia es "
                "solo la unidad de glucosa. En España y en la mayoría de los países "
                "latinoamericanos se usa mg/dL, por lo que la fórmula con 405 es la más "
                "habitual.</p>"
                "<p>Ejemplo: insulina en ayunas 11&nbsp;μU/mL, glucosa en ayunas 92&nbsp;mg/dL "
                "— HOMA-IR&nbsp;=&nbsp;(11&nbsp;&times;&nbsp;92)&nbsp;/&nbsp;405&nbsp;&asymp;&nbsp;2,50. "
                "Para que el cálculo sea fiable, la muestra debe tomarse tras un ayuno de al "
                "menos 8–12 horas.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="Relación con la glucosa en ayunas",
            body_html=(
                "<p>La <strong>glucosa en ayunas</strong> (o glucemia basal) es la concentración "
                "de glucosa en sangre tras al menos 8 horas sin ingerir alimentos. Los valores "
                "normales suelen situarse entre 70 y 100&nbsp;mg/dL. Es uno de los dos "
                "componentes de la fórmula HOMA-IR.</p>"
                "<p>Un dato clave: la glucosa en ayunas puede mantenerse dentro del rango normal "
                "durante años mientras la resistencia a la insulina ya está desarrollándose. Esto "
                "sucede porque el páncreas compensa produciendo más insulina para mantener la "
                "glucosa bajo control. Si solo miramos la glucosa, ese desequilibrio temprano "
                "pasa desapercibido. El HOMA-IR, al combinar glucosa e insulina, puede revelar "
                "esa tensión metabólica antes de que la glucosa se eleve. Para más información "
                "sobre la glucosa en ayunas, consulta nuestra "
                '<a href="/es/blog/como-leer-glucosa-en-ayunas">guía de glucosa en ayunas</a>.</p>'
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="Relación con la insulina en ayunas",
            body_html=(
                "<p>La <strong>insulina en ayunas</strong> es el nivel de insulina en sangre "
                "tras un ayuno nocturno de al menos 8–12 horas. Los rangos de referencia varían "
                "entre laboratorios, pero suelen oscilar entre 2 y 25&nbsp;μU/mL. Es el segundo "
                "componente de la fórmula HOMA-IR y, en el contexto de la resistencia temprana "
                "a la insulina, puede ser el más revelador.</p>"
                "<p>Cuando las células responden peor a la insulina, el páncreas aumenta su "
                "secreción — un fenómeno llamado <em>hiperinsulinemia compensatoria</em>. La "
                "glucosa permanece estable, pero la insulina sube, elevando el HOMA-IR. Este "
                "aumento puede ser una de las primeras señales detectables de problema "
                "metabólico.</p>"
                "<p>Conviene saber que los análisis de insulina varían entre laboratorios, y "
                "factores como el estrés, la falta de sueño, ciertos medicamentos (corticoides, "
                "algunos antipsicóticos) e incluso el momento de la extracción pueden influir "
                "en la medición. Un solo resultado es una instantánea, no un veredicto, y debe "
                "interpretarse dentro del cuadro clínico completo.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="Conexión con la resistencia a la insulina",
            body_html=(
                "<p>La <strong>resistencia a la insulina</strong> se produce cuando las células "
                "de músculo, grasa e hígado responden con menor eficacia a la señal de la "
                "insulina para captar glucosa. El páncreas compensa produciendo más insulina, "
                "pero con el tiempo puede no ser suficiente y la glucosa comienza a subir. La "
                "resistencia a la insulina se asocia al síndrome metabólico, la diabetes "
                "tipo&nbsp;2, la enfermedad cardiovascular, el SOP y la EHGNA.</p>"
                "<p>Muchas referencias consideran un HOMA-IR por debajo de 1,0 como óptimo. "
                "Valores por encima de 2,5–2,9 suelen interpretarse como indicativos de "
                "resistencia a la insulina. No obstante, estos umbrales dependen de la población, "
                "la etnia, la edad, el sexo y el método de laboratorio empleado. No existe un "
                "punto de corte universal.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Rango HOMA-IR</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretación general (orientativa)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Sensibilidad óptima a la insulina</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,0 – 2,4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal / límite — el contexto clínico importa</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2,5 – 2,9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Mayor probabilidad de resistencia a la insulina</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Altamente sugestivo de resistencia a la insulina</td>'
                "</tr></tbody></table>"
                "<p>Esta tabla es solo orientativa. Tu médico interpretará el resultado en el "
                "contexto de tu historial, tu IMC y otros hallazgos analíticos.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="¿Por qué el HOMA-IR solo no basta?",
            body_html=(
                "<p>El HOMA-IR es una herramienta útil de cribado, pero tiene limitaciones "
                "importantes:</p>"
                "<ul>"
                "<li>Se basa exclusivamente en valores en ayunas y no refleja la dinámica de "
                "insulina y glucosa tras las comidas.</li>"
                "<li>El estrés agudo, la enfermedad, la falta de sueño o el ejercicio intenso "
                "antes de la extracción pueden alterar temporalmente el resultado.</li>"
                "<li>En personas con disfunción avanzada de células beta (p.&nbsp;ej., diabetes "
                "tipo&nbsp;2 de larga evolución), la producción de insulina ya puede estar "
                "reducida, lo que hace que el HOMA-IR resulte engañosamente bajo.</li>"
                "<li>La variabilidad entre laboratorios en el análisis de insulina puede "
                "producir resultados ligeramente distintos.</li>"
                "</ul>"
                "<p>Por todo ello, el HOMA-IR debe valorarse junto con la glucosa en ayunas, "
                "la HbA1c, el perfil lipídico, las enzimas hepáticas y una evaluación clínica "
                "completa. Nuestro "
                '<a href="/es/blog/hba1c-que-significa-el-resultado">artículo sobre HbA1c</a> '
                "ofrece más contexto sobre el control glucémico a largo plazo.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="Qué tener en cuenta al evaluar tus resultados",
            body_html=(
                "<p>Antes de sacar conclusiones de un solo valor de HOMA-IR, ten en cuenta lo "
                "siguiente:</p>"
                "<ul>"
                "<li><strong>Duración del ayuno:</strong> La muestra debe tomarse tras al menos "
                "8–12 horas de ayuno. Un ayuno insuficiente altera tanto la glucosa como la "
                "insulina.</li>"
                "<li><strong>Estrés y sueño:</strong> El estrés agudo y la falta de sueño elevan "
                "el cortisol, lo que a su vez modifica el equilibrio entre insulina y glucosa.</li>"
                "<li><strong>Medicación:</strong> Corticoides, ciertos antipsicóticos y otros "
                "fármacos pueden afectar la sensibilidad a la insulina. Informa siempre a tu "
                "médico de lo que tomas.</li>"
                "<li><strong>Dieta y ejercicio:</strong> Cambios dietéticos inusuales o "
                "actividad física intensa en los días previos pueden modificar temporalmente "
                "el resultado.</li>"
                "<li><strong>Valor puntual vs. tendencia:</strong> Un solo HOMA-IR es una "
                "foto fija. La evolución a lo largo del tiempo es mucho más informativa.</li>"
                "<li><strong>Variación individual:</strong> Edad, sexo, etnia e IMC pueden "
                "influir en lo que se considera un rango &laquo;normal&raquo;.</li>"
                "</ul>"
                "<p>Por todas estas razones, considera tu HOMA-IR como una pieza más del "
                "rompecabezas, no como un veredicto aislado sobre tu salud metabólica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Valora hablar con tu médico sobre el HOMA-IR si se da alguna de estas "
                "circunstancias:</p>"
                "<ul>"
                "<li>Tu HOMA-IR supera el rango de referencia del laboratorio.</li>"
                "<li>Hay antecedentes familiares de diabetes tipo&nbsp;2, síndrome metabólico "
                "o enfermedad cardiovascular.</li>"
                "<li>Notas un aumento de peso inexplicable o dificultad para adelgazar.</li>"
                "<li>Te han diagnosticado SOP o tienes irregularidades menstruales.</li>"
                "<li>Experimentas cansancio, sed excesiva o necesidad frecuente de orinar.</li>"
                "<li>Tienes las enzimas hepáticas elevadas o se ha detectado hígado graso.</li>"
                "</ul>"
                "<p>Aunque no tengas síntomas, un HOMA-IR elevado merece comentarse con tu "
                "médico. La intervención temprana — ajustes en la alimentación, más actividad "
                "física y, si es necesario, medicación — puede frenar o revertir la progresión "
                "de la resistencia a la insulina.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo puede ayudarte NoryaAI",
            body_html=(
                "<p>En NoryaAI no diagnosticamos; te ayudamos a entender. Puedes "
                '<a href="/analyze">subir tu analítica</a> y obtener un resumen claro y '
                "estructurado que explica tus valores — incluido el HOMA-IR — en un lenguaje "
                "sencillo, con rangos de referencia y contexto. Así es más fácil preparar tu "
                "consulta con el médico y hacer las preguntas adecuadas.</p>"
                "<p>No ofrecemos recomendaciones de tratamiento ni conclusiones diagnósticas. "
                "Nuestro objetivo es tender un puente entre el informe de laboratorio y una "
                "conversación productiva con tu profesional de la salud. Para opciones y "
                'tarifas, visita nuestra página de <a href="/pricing">precios</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso legal",
            body_html=(
                "<p><strong>Este contenido es solo informativo y no sustituye el consejo "
                "médico ni el diagnóstico profesional.</strong> Consulta siempre a un "
                "profesional sanitario cualificado para interpretar tu HOMA-IR y cualquier "
                "otro resultado de laboratorio. Solo un médico que conozca tu historial y "
                "contexto clínico puede valorar correctamente tus resultados.</p>"
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
            heading="Qu'est-ce que le HOMA-IR et pourquoi est-il important ?",
            body_html=(
                "<p>Si votre bilan sanguin mentionne un indice appelé <strong>HOMA-IR</strong>, "
                "vous vous demandez peut-être ce que ce chiffre signifie et s'il y a lieu de "
                "s'inquiéter. Le HOMA-IR est un indice calculé qui estime la sensibilité de "
                "votre organisme à l'insuline. Il n'est pas mesuré directement ; il est dérivé "
                "de deux dosages courants : la glycémie à jeun et l'insulinémie à jeun. Au cours "
                "des dernières décennies, il s'est imposé comme un outil de dépistage simple de "
                "l'insulinorésistance, en particulier dans l'évaluation du risque métabolique.</p>"
                "<p>Ce guide explique ce que mesure le HOMA-IR, comment il est calculé, quelles "
                "sont ses limites et à quel moment consulter votre médecin. Notre objectif n'est "
                "pas de poser un diagnostic, mais de vous aider à mieux comprendre vos résultats "
                "pour en discuter de manière éclairée avec votre praticien.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="Qu'est-ce que le HOMA-IR exactement ?",
            body_html=(
                "<p><strong>HOMA-IR</strong> signifie <em>Homeostatic Model Assessment for "
                "Insulin Resistance</em> (évaluation du modèle homéostatique pour "
                "l'insulinorésistance). Le modèle a été publié en 1985 par Matthews et ses "
                "collègues. Il permet d'estimer l'insulinorésistance à partir d'un simple "
                "prélèvement sanguin à jeun, sans recourir au clamp euglycémique "
                "hyperinsulinémique, méthode de référence mais coûteuse et complexe. Le "
                "principe est logique : dans un métabolisme sain, le pancréas sécrète juste "
                "assez d'insuline pour maintenir la glycémie dans une fourchette étroite. "
                "Lorsque les cellules deviennent résistantes à l'insuline, le pancréas doit "
                "en produire davantage. Le HOMA-IR traduit ce déséquilibre en un seul chiffre.</p>"
                "<p>En pratique, les médecins l'utilisent dans l'évaluation du syndrome "
                "métabolique, du risque de diabète de type&nbsp;2, du syndrome des ovaires "
                "polykystiques (SOPK) et de la stéatose hépatique non alcoolique (NAFLD). "
                "Il est essentiel de comprendre dès le départ que le HOMA-IR est un outil de "
                "<em>dépistage</em>, pas un test diagnostique. Une seule valeur ne confirme ni "
                "n'exclut une maladie ; elle doit toujours être interprétée avec l'ensemble du "
                "contexte clinique.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="Comment le HOMA-IR est-il calculé ?",
            body_html=(
                "<p>Le calcul est simple. Deux formules sont utilisées, selon l'unité de la "
                "glycémie :</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Unité de glucose</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Formule</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Insuline à jeun (μU/mL) &times; Glycémie à jeun (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L (courant en France)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Insuline à jeun (μU/mL) &times; Glycémie à jeun (mmol/L) &divide; 22,5</td>'
                "</tr></tbody></table>"
                "<p>Les constantes 405 et 22,5 sont des facteurs d'étalonnage issus de moyennes "
                "de sujets sains. Les deux formules donnent le même résultat ; seule l'unité "
                "de la glycémie change. En France, où le mmol/L est courant, la formule avec "
                "22,5 est souvent employée, bien que le mg/dL reste aussi utilisé.</p>"
                "<p>Exemple : insuline à jeun 10&nbsp;μU/mL, glycémie à jeun 5,0&nbsp;mmol/L "
                "— HOMA-IR&nbsp;=&nbsp;(10&nbsp;&times;&nbsp;5,0)&nbsp;/&nbsp;22,5&nbsp;&asymp;&nbsp;2,22. "
                "Ce résultat sera mis en perspective dans les sections suivantes. La fiabilité "
                "du calcul repose sur un jeûne d'au moins 8 à 12 heures avant la prise de "
                "sang.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="Le lien avec la glycémie à jeun",
            body_html=(
                "<p>La <strong>glycémie à jeun</strong> est la concentration de glucose dans "
                "le sang après au moins 8 heures sans manger. Les valeurs normales se situent "
                "généralement entre 3,9 et 5,6&nbsp;mmol/L (70–100&nbsp;mg/dL). C'est l'un "
                "des deux éléments de la formule HOMA-IR.</p>"
                "<p>Un point capital : la glycémie à jeun peut rester normale pendant des "
                "années alors qu'une insulinorésistance se développe déjà en coulisses. Le "
                "pancréas compense en sécrétant plus d'insuline, ce qui maintient la glycémie "
                "dans les normes — mais au prix d'un effort accru. Si l'on ne regarde que la "
                "glycémie, cette dérive métabolique précoce passe inaperçue. Le HOMA-IR, en "
                "intégrant l'insuline dans l'équation, peut la révéler plus tôt. Pour "
                "approfondir le sujet, consultez notre "
                '<a href="/fr/blog/comment-lire-glycemie-a-jeun">guide glycémie à jeun</a>.</p>'
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="Le lien avec l'insulinémie à jeun",
            body_html=(
                "<p>L'<strong>insulinémie à jeun</strong> correspond au taux d'insuline "
                "circulant dans le sang après un jeûne nocturne d'au moins 8 à 12 heures. "
                "Les valeurs de référence varient selon les laboratoires mais se situent "
                "habituellement entre 2 et 25&nbsp;μU/mL. C'est le deuxième élément de la "
                "formule HOMA-IR et, dans le contexte d'une insulinorésistance débutante, "
                "souvent le plus informatif.</p>"
                "<p>Lorsque les cellules répondent moins bien à l'insuline, le pancréas "
                "augmente sa sécrétion — c'est l'<em>hyperinsulinisme compensatoire</em>. La "
                "glycémie reste stable mais l'insuline monte, ce qui élève le HOMA-IR et "
                "peut constituer l'un des premiers signes détectables d'un trouble "
                "métabolique.</p>"
                "<p>Il faut savoir que les dosages d'insuline varient d'un laboratoire à "
                "l'autre, et que le stress, le manque de sommeil, certains médicaments "
                "(corticoïdes, certains antipsychotiques) ainsi que l'heure du prélèvement "
                "peuvent influer sur le résultat. Une seule mesure est donc un instantané, "
                "pas un verdict, et doit être replacée dans le tableau clinique global.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="Le lien avec l'insulinorésistance",
            body_html=(
                "<p>L'<strong>insulinorésistance</strong> se produit lorsque les cellules "
                "musculaires, adipeuses et hépatiques répondent moins efficacement au signal "
                "de l'insuline pour capter le glucose. Le pancréas compense en produisant "
                "davantage, mais à terme il peut ne plus suffire et la glycémie commence à "
                "monter. L'insulinorésistance est étroitement liée au syndrome métabolique, "
                "au diabète de type&nbsp;2, aux maladies cardiovasculaires, au SOPK et à la "
                "NAFLD.</p>"
                "<p>De nombreuses références considèrent un HOMA-IR inférieur à 1,0 comme "
                "optimal. Des valeurs supérieures à 2,5–2,9 sont souvent citées comme "
                "évocatrices d'une insulinorésistance. Cependant, ces seuils dépendent de la "
                "population étudiée, de l'origine ethnique, de l'âge, du sexe et de la méthode "
                "de dosage. Il n'existe pas de seuil universel.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Plage HOMA-IR</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interprétation générale (à titre indicatif)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Sensibilité optimale à l&rsquo;insuline</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,0 – 2,4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normal / limite — le contexte clinique est déterminant</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2,5 – 2,9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Probabilité accrue d&rsquo;insulinorésistance</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Fortement évocateur d&rsquo;insulinorésistance</td>'
                "</tr></tbody></table>"
                "<p>Ce tableau n'est qu'un repère. Votre médecin interprétera votre valeur au "
                "regard de votre dossier complet, de vos antécédents familiaux, de votre IMC "
                "et d'autres résultats biologiques.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Pourquoi le HOMA-IR seul ne suffit pas",
            body_html=(
                "<p>Le HOMA-IR est un outil de dépistage utile, mais il présente des limites "
                "importantes :</p>"
                "<ul>"
                "<li>Il repose uniquement sur des valeurs à jeun et ne reflète pas la dynamique "
                "insuline-glucose après les repas.</li>"
                "<li>Un stress aigu, un manque de sommeil, une maladie intercurrente ou un "
                "effort physique intense avant la prise de sang peuvent fausser temporairement "
                "le résultat.</li>"
                "<li>Chez les patients dont les cellules bêta sont fortement altérées (p.&nbsp;ex. "
                "diabète de type&nbsp;2 ancien), la production d'insuline peut être réduite, ce "
                "qui rend le HOMA-IR faussement bas.</li>"
                "<li>Les variations entre dosages d'insuline d'un laboratoire à l'autre peuvent "
                "conduire à des résultats légèrement différents.</li>"
                "</ul>"
                "<p>C'est pourquoi le HOMA-IR doit toujours être interprété avec la glycémie "
                "à jeun, l'HbA1c, le bilan lipidique, les enzymes hépatiques et une évaluation "
                "clinique complète. Notre "
                '<a href="/fr/blog/hba1c-comprendre-resultat">article HbA1c</a> apporte un '
                "éclairage complémentaire sur le contrôle glycémique à long terme.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="Ce qu'il faut prendre en compte pour évaluer vos résultats",
            body_html=(
                "<p>Avant de tirer des conclusions d'une seule valeur de HOMA-IR, gardez à "
                "l'esprit les éléments suivants :</p>"
                "<ul>"
                "<li><strong>Durée du jeûne :</strong> Le prélèvement doit être effectué après "
                "au moins 8 à 12 heures de jeûne. Un jeûne insuffisant fausse la glycémie et "
                "l'insuline.</li>"
                "<li><strong>Stress et sommeil :</strong> Le stress aigu et le manque de sommeil "
                "augmentent le cortisol, ce qui modifie l'équilibre insuline-glucose.</li>"
                "<li><strong>Médicaments :</strong> Corticoïdes, certains antipsychotiques et "
                "d'autres traitements peuvent influencer la sensibilité à l'insuline. Signalez "
                "tous vos médicaments à votre médecin.</li>"
                "<li><strong>Alimentation et exercice :</strong> Des changements alimentaires "
                "inhabituels ou une activité physique intense dans les jours précédant le test "
                "peuvent modifier temporairement le résultat.</li>"
                "<li><strong>Valeur ponctuelle vs. tendance :</strong> Un seul HOMA-IR est un "
                "instantané. L'évolution dans le temps est bien plus parlante.</li>"
                "<li><strong>Variations individuelles :</strong> L'âge, le sexe, l'origine "
                "ethnique et l'IMC influencent ce qui est considéré comme &laquo;&nbsp;normal&nbsp;&raquo;.</li>"
                "</ul>"
                "<p>Pour toutes ces raisons, considérez votre HOMA-IR comme une pièce d'un "
                "puzzle plus vaste, et non comme un jugement isolé sur votre santé "
                "métabolique.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand faut-il consulter un médecin ?",
            body_html=(
                "<p>Pensez à discuter de votre HOMA-IR avec votre médecin si l'une des "
                "situations suivantes s'applique :</p>"
                "<ul>"
                "<li>Votre HOMA-IR dépasse l'intervalle de référence du laboratoire.</li>"
                "<li>Il existe des antécédents familiaux de diabète de type&nbsp;2, de syndrome "
                "métabolique ou de maladie cardiovasculaire.</li>"
                "<li>Vous constatez une prise de poids inexpliquée ou des difficultés à en "
                "perdre.</li>"
                "<li>Vous avez un diagnostic de SOPK ou des irrégularités menstruelles.</li>"
                "<li>Vous ressentez une fatigue persistante, une soif excessive ou un besoin "
                "fréquent d'uriner.</li>"
                "<li>Vos enzymes hépatiques sont élevées ou une stéatose hépatique a été "
                "constatée à l'imagerie.</li>"
                "</ul>"
                "<p>Même en l'absence de symptômes, un HOMA-IR élevé mérite d'être discuté "
                "avec votre médecin. Une intervention précoce — rééquilibrage alimentaire, "
                "augmentation de l'activité physique et, si nécessaire, traitement "
                "médicamenteux — peut ralentir voire inverser la progression de "
                "l'insulinorésistance.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment NoryaAI peut vous aider",
            body_html=(
                "<p>Chez NoryaAI, nous ne posons pas de diagnostic — nous vous aidons à "
                "comprendre. Vous pouvez "
                '<a href="/analyze">télécharger votre bilan</a> et recevoir un résumé clair '
                "et structuré qui explique vos valeurs — y compris le HOMA-IR — dans un langage "
                "accessible, avec les intervalles de référence et le contexte nécessaire. Cela "
                "facilite la préparation de votre rendez-vous médical et vous aide à poser "
                "les bonnes questions.</p>"
                "<p>Nous ne formulons ni recommandations thérapeutiques ni conclusions "
                "diagnostiques. Notre ambition est de faire le lien entre un compte-rendu de "
                "laboratoire parfois complexe et une conversation constructive avec votre "
                "professionnel de santé. Pour découvrir nos formules, consultez notre page "
                '<a href="/pricing">tarifs</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                "<p><strong>Ce contenu est fourni à titre informatif uniquement et ne remplace "
                "ni un avis médical ni un diagnostic.</strong> Discutez toujours de votre "
                "HOMA-IR et de tous vos résultats de laboratoire avec un professionnel de "
                "santé qualifié. Seul un médecin connaissant vos antécédents et votre contexte "
                "clinique peut interpréter correctement vos résultats.</p>"
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
            heading="Cos'è l'HOMA-IR e perché è importante?",
            body_html=(
                "<p>Se nel referto delle analisi del sangue compare un valore chiamato "
                "<strong>HOMA-IR</strong>, è naturale chiedersi cosa significhi e se ci sia "
                "motivo di preoccupazione. L'HOMA-IR è un indice calcolato che stima la "
                "sensibilità del corpo all'insulina. Non viene misurato direttamente; si "
                "ricava da due esami di routine: la glicemia a digiuno e l'insulinemia a "
                "digiuno. Negli ultimi anni si è affermato come strumento di screening "
                "semplice e diffuso, soprattutto per individuare precocemente la resistenza "
                "insulinica.</p>"
                "<p>Questa guida spiega cos'è l'HOMA-IR, come si calcola, quali informazioni "
                "può e non può fornire, e quando è opportuno parlarne con il medico. Non "
                "intendiamo formulare diagnosi, ma aiutarvi a comprendere il risultato per "
                "presentarvi al prossimo appuntamento con maggiore consapevolezza.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="Che cos'è esattamente l'HOMA-IR?",
            body_html=(
                "<p><strong>HOMA-IR</strong> sta per <em>Homeostatic Model Assessment for "
                "Insulin Resistance</em>. Il modello è stato descritto nel 1985 da Matthews e "
                "colleghi come metodo per stimare la resistenza insulinica a partire di un "
                "semplice prelievo a digiuno, evitando la complessità e i costi del clamp "
                "euglicemico iperinsulinemico. Il principio di base è intuitivo: in un "
                "metabolismo sano il pancreas rilascia la quantità di insulina necessaria a "
                "mantenere la glicemia entro limiti stretti. Quando le cellule iniziano a "
                "rispondere meno all'insulina, il pancreas ne produce di più per compensare. "
                "L'HOMA-IR esprime questo squilibrio in un unico numero.</p>"
                "<p>Nella pratica clinica l'HOMA-IR viene utilizzato nella valutazione della "
                "sindrome metabolica, del rischio di diabete di tipo&nbsp;2, della sindrome "
                "dell'ovaio policistico (PCOS) e della steatosi epatica non alcolica (NAFLD). "
                "È fondamentale capire fin da subito che l'HOMA-IR è uno strumento di "
                "<em>screening</em>, non un test diagnostico. Un singolo valore non conferma "
                "né esclude alcuna patologia; va sempre interpretato nel contesto della storia "
                "clinica, dei sintomi e di altri esami.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="Come si calcola l'HOMA-IR?",
            body_html=(
                "<p>Il calcolo è piuttosto semplice. Esistono due formule, a seconda dell'unità "
                "usata per la glicemia:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Unità glicemia</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Formula</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL (in Italia il più usato)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Insulinemia a digiuno (μU/mL) &times; Glicemia a digiuno (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Insulinemia a digiuno (μU/mL) &times; Glicemia a digiuno (mmol/L) &divide; 22,5</td>'
                "</tr></tbody></table>"
                "<p>Le costanti 405 e 22,5 sono fattori di calibrazione derivati dalle medie di "
                "soggetti sani. Le due formule danno lo stesso risultato; cambia solo l'unità "
                "della glicemia. In Italia si utilizza prevalentemente il mg/dL, per cui la "
                "formula con 405 è quella più frequente nei referti.</p>"
                "<p>Esempio: insulinemia a digiuno 12&nbsp;μU/mL, glicemia a digiuno "
                "88&nbsp;mg/dL — HOMA-IR&nbsp;=&nbsp;(12&nbsp;&times;&nbsp;88)&nbsp;/&nbsp;405&nbsp;"
                "&asymp;&nbsp;2,61. Nelle sezioni successive vedremo come interpretare questo "
                "numero. Per un calcolo affidabile, il prelievo deve avvenire dopo almeno "
                "8–12 ore di digiuno.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="Il rapporto con la glicemia a digiuno",
            body_html=(
                "<p>La <strong>glicemia a digiuno</strong> è la concentrazione di glucosio nel "
                "sangue dopo almeno 8 ore senza assumere cibo. I valori normali si collocano "
                "generalmente tra 70 e 100&nbsp;mg/dL (3,9–5,6&nbsp;mmol/L). È uno dei due "
                "elementi della formula HOMA-IR.</p>"
                "<p>Un aspetto cruciale: la glicemia a digiuno può restare nella norma per anni "
                "anche se la resistenza insulinica si sta sviluppando. Il pancreas compensa "
                "producendo più insulina per mantenere stabile la glicemia — ma con un impegno "
                "crescente. Se si guarda solo la glicemia, questa alterazione precoce sfugge. "
                "L'HOMA-IR, combinando glicemia e insulina, può portarla alla luce prima che "
                "la glicemia stessa salga. Per approfondire, consultate la nostra "
                '<a href="/it/blog/come-leggere-glicemia-a-digiuno">guida glicemia a digiuno</a>.</p>'
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="Il rapporto con l'insulinemia a digiuno",
            body_html=(
                "<p>L'<strong>insulinemia a digiuno</strong> è il livello di insulina nel "
                "sangue dopo un digiuno notturno di almeno 8–12 ore. I valori di riferimento "
                "variano tra laboratori ma di solito rientrano tra 2 e 25&nbsp;μU/mL. È il "
                "secondo componente della formula HOMA-IR e, nel contesto della resistenza "
                "insulinica iniziale, spesso il più rivelatore.</p>"
                "<p>Quando le cellule rispondono meno all'insulina, il pancreas ne aumenta "
                "la secrezione — una condizione detta <em>iperinsulinemia compensatoria</em>. "
                "La glicemia rimane stabile, ma l'insulina sale, facendo salire l'HOMA-IR e "
                "potenzialmente segnalando un problema metabolico in fase iniziale.</p>"
                "<p>È bene sapere che i dosaggi dell'insulina variano da laboratorio a "
                "laboratorio, e che stress, carenza di sonno, alcuni farmaci (corticosteroidi, "
                "certi antipsicotici) e persino l'orario del prelievo possono influenzare il "
                "risultato. Un singolo valore è dunque un'istantanea, non un verdetto, e "
                "va inserito nel quadro clinico complessivo.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="Il collegamento con la resistenza insulinica",
            body_html=(
                "<p>La <strong>resistenza insulinica</strong> si verifica quando le cellule "
                "muscolari, adipose ed epatiche rispondono meno efficacemente al segnale "
                "dell'insulina per assorbire il glucosio. Il pancreas compensa producendone "
                "di più, ma col tempo potrebbe non bastare e la glicemia inizia a salire. La "
                "resistenza insulinica è strettamente legata alla sindrome metabolica, al "
                "diabete di tipo&nbsp;2, alle malattie cardiovascolari, alla PCOS e alla "
                "NAFLD.</p>"
                "<p>Molte fonti considerano un HOMA-IR inferiore a 1,0 come ottimale. Valori "
                "superiori a 2,5–2,9 vengono spesso indicati come suggestivi di resistenza "
                "insulinica. Tuttavia, queste soglie dipendono dalla popolazione, dall'etnia, "
                "dall'età, dal sesso e dal metodo di dosaggio; non esiste un unico valore "
                "soglia universale.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Intervallo HOMA-IR</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">Interpretazione generale (indicativa)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Sensibilità insulinica ottimale</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1,0 – 2,4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Normale / al limite — il contesto clinico è determinante</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2,5 – 2,9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Probabilità aumentata di resistenza insulinica</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3,0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">Fortemente indicativo di resistenza insulinica</td>'
                "</tr></tbody></table>"
                "<p>La tabella ha valore puramente orientativo. Il medico interpreterà il "
                "risultato nel contesto del quadro clinico completo, della storia familiare, "
                "dell'IMC e di altri esami.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="Perché l'HOMA-IR da solo non basta",
            body_html=(
                "<p>L'HOMA-IR è uno strumento di screening utile, ma ha limiti importanti:</p>"
                "<ul>"
                "<li>Si basa unicamente su valori a digiuno e non riflette la dinamica di "
                "insulina e glucosio dopo i pasti.</li>"
                "<li>Stress acuto, malattia intercorrente, carenza di sonno o esercizio "
                "intenso prima del prelievo possono alterare temporaneamente il risultato.</li>"
                "<li>Nei pazienti con disfunzione avanzata delle cellule beta (ad es. diabete "
                "di tipo&nbsp;2 di lunga data), la produzione di insulina può essere già "
                "ridotta, rendendo l'HOMA-IR falsamente basso.</li>"
                "<li>Le differenze tra i dosaggi di insulina nei vari laboratori possono "
                "portare a risultati leggermente diversi.</li>"
                "</ul>"
                "<p>Per queste ragioni, l'HOMA-IR va sempre considerato insieme a glicemia a "
                "digiuno, HbA1c, profilo lipidico, enzimi epatici e valutazione clinica "
                "completa. Il nostro "
                '<a href="/it/blog/hba1c-cosa-significa-il-valore">articolo HbA1c</a> offre '
                "ulteriori informazioni sul controllo glicemico a lungo termine.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="Cosa considerare nella valutazione dei risultati",
            body_html=(
                "<p>Prima di trarre conclusioni da un singolo valore di HOMA-IR, tenete a "
                "mente i seguenti aspetti:</p>"
                "<ul>"
                "<li><strong>Durata del digiuno:</strong> Il prelievo deve avvenire dopo "
                "almeno 8–12 ore di digiuno. Un digiuno insufficiente altera sia la glicemia "
                "sia l'insulina.</li>"
                "<li><strong>Stress e sonno:</strong> Lo stress acuto e la carenza di sonno "
                "aumentano il cortisolo, influenzando l'equilibrio insulina-glucosio.</li>"
                "<li><strong>Farmaci:</strong> Corticosteroidi, alcuni antipsicotici e altri "
                "medicinali possono modificare la sensibilità insulinica. Comunicate sempre "
                "al medico i farmaci che assumete.</li>"
                "<li><strong>Alimentazione e attività fisica:</strong> Cambiamenti "
                "alimentari insoliti o attività fisica intensa nei giorni precedenti il test "
                "possono influire temporaneamente.</li>"
                "<li><strong>Singolo valore vs. andamento:</strong> Un solo HOMA-IR è una "
                "fotografia. L'andamento nel tempo è molto più significativo.</li>"
                "<li><strong>Variabilità individuale:</strong> Età, sesso, etnia e IMC "
                "possono influenzare ciò che viene considerato &laquo;normale&raquo;.</li>"
                "</ul>"
                "<p>Per tutte queste ragioni, considerate il vostro HOMA-IR come un tassello "
                "di un quadro più ampio, non come un giudizio definitivo sulla vostra salute "
                "metabolica.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Valutate di parlare con il vostro medico del HOMA-IR se si verifica una "
                "di queste condizioni:</p>"
                "<ul>"
                "<li>Il vostro HOMA-IR supera l'intervallo di riferimento del laboratorio.</li>"
                "<li>In famiglia ci sono casi di diabete di tipo&nbsp;2, sindrome metabolica "
                "o malattie cardiovascolari.</li>"
                "<li>Notate un aumento di peso inspiegabile o difficoltà a perdere peso.</li>"
                "<li>Avete ricevuto una diagnosi di PCOS o avete irregolarità mestruali.</li>"
                "<li>Provate stanchezza persistente, sete eccessiva o bisogno frequente "
                "di urinare.</li>"
                "<li>Gli enzimi epatici sono elevati o è stata riscontrata steatosi "
                "epatica.</li>"
                "</ul>"
                "<p>Anche in assenza di sintomi, un HOMA-IR elevato merita di essere "
                "discusso con il medico. Un intervento precoce — modifiche alimentari, "
                "aumento dell'attività fisica e, se necessario, terapia farmacologica — "
                "può rallentare o invertire la progressione della resistenza insulinica.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come può aiutarvi NoryaAI",
            body_html=(
                "<p>Noi di NoryaAI non formuliamo diagnosi — vi aiutiamo a capire. Potete "
                '<a href="/analyze">caricare il vostro referto</a> e ottenere un riepilogo '
                "chiaro e strutturato che spiega i vostri valori — HOMA-IR incluso — in un "
                "linguaggio semplice, con intervalli di riferimento e contesto. Questo rende "
                "più facile prepararsi alla visita medica e porre le domande giuste.</p>"
                "<p>Non offriamo indicazioni terapeutiche né conclusioni diagnostiche. Il "
                "nostro scopo è collegare un referto di laboratorio spesso complesso a una "
                "conversazione produttiva con il vostro medico. Per conoscere le nostre "
                'opzioni, visitate la pagina <a href="/pricing">prezzi</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avvertenza",
            body_html=(
                "<p><strong>Questo contenuto ha finalità esclusivamente informativa e non "
                "sostituisce il parere medico né la diagnosi.</strong> Discutete sempre "
                "l'HOMA-IR e tutti gli altri valori di laboratorio con un professionista "
                "sanitario qualificato. Solo un medico che conosce la vostra storia e il "
                "contesto clinico può interpretare correttamente i risultati.</p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW  (RTL)
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="מהו HOMA-IR ולמה הוא חשוב?",
            body_html=(
                "<p>אם בתוצאות בדיקות הדם שלכם מופיע ערך בשם <strong>HOMA-IR</strong>, "
                "סביר שתשאלו מה הוא אומר ואם יש סיבה לדאגה. HOMA-IR הוא מדד מחושב "
                "שמעריך את רגישות הגוף לאינסולין. הוא אינו נמדד ישירות בדם אלא מחושב "
                "משני ערכים שגרתיים: גלוקוז בצום ואינסולין בצום. בשנים האחרונות הוא הפך "
                "לכלי סינון פשוט ונפוץ, בעיקר לגילוי מוקדם של עמידות לאינסולין.</p>"
                "<p>מדריך זה מסביר מהו HOMA-IR, כיצד הוא מחושב, מה הוא יכול ומה הוא לא "
                "יכול לספר, ומתי כדאי לפנות לרופא. המטרה שלנו אינה לאבחן — אלא לעזור לכם "
                "להבין את התוצאה כדי שתגיעו לפגישה עם הרופא מוכנים יותר.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="מהו HOMA-IR בדיוק?",
            body_html=(
                "<p><strong>HOMA-IR</strong> הוא ראשי תיבות של <em>Homeostatic Model "
                "Assessment for Insulin Resistance</em> (הערכת מודל הומאוסטטי לעמידות "
                "לאינסולין). המודל פורסם ב-1985 על ידי Matthews ועמיתיו, ומאפשר להעריך "
                "עמידות לאינסולין מדגימת דם פשוטה בצום — ללא צורך בבדיקת הקלאמפ היקרה "
                "והמורכבת. העיקרון ברור: במטבוליזם תקין, הלבלב מפריש כמות מספקת של "
                "אינסולין כדי לשמור על רמת הגלוקוז בטווח צר. כאשר התאים מתחילים להגיב "
                "פחות לאינסולין, הלבלב מפצה על ידי ייצור כמות גדולה יותר. ה-HOMA-IR מבטא "
                "את חוסר האיזון הזה כמספר אחד.</p>"
                "<p>בפרקטיקה הקלינית, הרופאים משתמשים ב-HOMA-IR בהערכת תסמונת מטבולית, "
                "סיכון לסוכרת סוג&nbsp;2, תסמונת שחלות פוליציסטיות (PCOS) ומחלת כבד "
                "שומני לא אלכוהולי (NAFLD). חשוב להבין כבר עכשיו: HOMA-IR הוא כלי "
                "<em>סינון</em>, לא בדיקה אבחנתית. ערך יחיד אינו מאשר או שולל מחלה — "
                "יש לפרש אותו תמיד בהקשר הקליני הרחב.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="איך מחשבים HOMA-IR?",
            body_html=(
                "<p>החישוב פשוט למדי. יש שתי נוסחאות, בהתאם ליחידת המדידה של הגלוקוז:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">יחידת גלוקוז</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">נוסחה</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL (נפוץ בישראל)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">אינסולין בצום (μU/mL) &times; גלוקוז בצום (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">אינסולין בצום (μU/mL) &times; גלוקוז בצום (mmol/L) &divide; 22.5</td>'
                "</tr></tbody></table>"
                "<p>הקבועים 405 ו-22.5 הם גורמי כיול שנגזרו ממוצעי אוכלוסייה בריאה. שתי "
                "הנוסחאות נותנות אותה תוצאה; ההבדל הוא רק ביחידת הגלוקוז. בישראל נפוץ "
                "השימוש ב-mg/dL, ולכן הנוסחה עם 405 מוכרת יותר.</p>"
                "<p>דוגמה: אינסולין בצום 9&nbsp;μU/mL, גלוקוז בצום 95&nbsp;mg/dL — "
                "HOMA-IR&nbsp;=&nbsp;(9&nbsp;&times;&nbsp;95)&nbsp;/&nbsp;405&nbsp;&asymp;&nbsp;2.11. "
                "כדי שהחישוב יהיה אמין, הדגימה חייבת להילקח לאחר צום של 8–12 שעות "
                "לפחות.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="הקשר עם גלוקוז בצום",
            body_html=(
                "<p><strong>גלוקוז בצום</strong> הוא ריכוז הסוכר בדם לאחר לפחות 8 שעות "
                "ללא אכילה. ערכים תקינים נעים בדרך כלל בין 70 ל-100&nbsp;mg/dL. זהו אחד "
                "משני הרכיבים בנוסחת HOMA-IR.</p>"
                "<p>נקודה מרכזית: גלוקוז בצום יכול להישאר בטווח התקין במשך שנים גם כשעמידות "
                "לאינסולין כבר מתפתחת. הלבלב מפצה על ידי הפרשת יותר אינסולין כדי לשמור על "
                "הגלוקוז יציב — אך במחיר של מאמץ גובר. אם בוחנים רק את הגלוקוז, השינוי "
                "המטבולי המוקדם הזה נשאר מוסתר. HOMA-IR, ששילוב גם את האינסולין, יכול "
                "לחשוף אותו מוקדם יותר.</p>"
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="הקשר עם אינסולין בצום",
            body_html=(
                "<p><strong>אינסולין בצום</strong> הוא רמת האינסולין בדם לאחר צום לילי של "
                "8–12 שעות לפחות. טווחי הייחוס משתנים בין מעבדות אך בדרך כלל נעים בין "
                "2 ל-25&nbsp;μU/mL. זהו הרכיב השני בנוסחת HOMA-IR, ולעיתים קרובות "
                "המידע שהוא מספק הוא המשמעותי ביותר בהקשר של עמידות מוקדמת לאינסולין.</p>"
                "<p>כאשר התאים מגיבים פחות לאינסולין, הלבלב מגביר את ההפרשה — מצב "
                "המכונה <em>היפראינסולינמיה מפצה</em>. הגלוקוז נשאר יציב, אך האינסולין "
                "עולה, מה שמעלה את ה-HOMA-IR ועשוי להוות סימן מוקדם לבעיה מטבולית.</p>"
                "<p>חשוב לדעת שבדיקות אינסולין משתנות בין מעבדות, וגורמים כמו מתח, חוסר "
                "שינה, תרופות מסוימות (קורטיקוסטרואידים, תרופות אנטי-פסיכוטיות מסוימות) "
                "ואפילו שעת הדגימה יכולים להשפיע על התוצאה. מדידה בודדת היא תמונת מצב, "
                "לא פסק דין, ויש לשלב אותה בתמונה הקלינית הכוללת.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="הקשר עם עמידות לאינסולין",
            body_html=(
                "<p><strong>עמידות לאינסולין</strong> מתרחשת כאשר תאי שריר, שומן וכבד "
                "מגיבים פחות ביעילות לאות האינסולין לקלוט גלוקוז. הלבלב מפצה בייצור "
                "מוגבר, אך עם הזמן ייתכן שלא יספיק, והגלוקוז בדם מתחיל לעלות. עמידות "
                "לאינסולין קשורה קשר הדוק לתסמונת מטבולית, סוכרת סוג&nbsp;2, מחלות "
                "לב וכלי דם, PCOS ו-NAFLD.</p>"
                "<p>מקורות רבים רואים ב-HOMA-IR מתחת ל-1.0 ערך אופטימלי. ערכים מעל "
                "2.5–2.9 נחשבים לעיתים קרובות כמצביעים על עמידות לאינסולין. עם זאת, "
                "ערכי הסף תלויים באוכלוסייה, במוצא האתני, בגיל, במין ובשיטת המעבדה. "
                "אין ערך סף אוניברסלי אחד.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">טווח HOMA-IR</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">פרשנות כללית (לצורך התמצאות)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">רגישות אופטימלית לאינסולין</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.0 – 2.4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">תקין / גבולי — ההקשר הקליני קובע</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2.5 – 2.9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">סבירות מוגברת לעמידות לאינסולין</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">מצביע בבירור על עמידות לאינסולין</td>'
                "</tr></tbody></table>"
                "<p>הטבלה משמשת להתמצאות בלבד. הרופא שלכם יפרש את הערך בהקשר התמונה "
                "הקלינית המלאה, ההיסטוריה המשפחתית, ה-BMI ותוצאות נוספות.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="למה HOMA-IR לבדו אינו מספיק?",
            body_html=(
                "<p>HOMA-IR הוא כלי סינון שימושי, אך יש לו מגבלות חשובות:</p>"
                "<ul>"
                "<li>הוא מבוסס רק על ערכים בצום ואינו משקף את הדינמיקה של אינסולין "
                "וגלוקוז לאחר הארוחות.</li>"
                "<li>מתח חד, מחלה, חוסר שינה או פעילות גופנית אינטנסיבית לפני הדגימה "
                "יכולים לשנות את התוצאה באופן זמני.</li>"
                "<li>אצל אנשים עם פגיעה מתקדמת בתאי הבטא (למשל סוכרת סוג&nbsp;2 "
                "ותיקה), ייצור האינסולין כבר מופחת, מה שעלול לגרום ל-HOMA-IR נמוך "
                "ומטעה.</li>"
                "<li>הבדלים בבדיקות אינסולין בין מעבדות עלולים להניב תוצאות מעט "
                "שונות.</li>"
                "</ul>"
                "<p>לכן, יש לשקול את HOMA-IR תמיד לצד גלוקוז בצום, HbA1c, פרופיל "
                "שומנים, אנזימי כבד והערכה קלינית מקיפה.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="מה יש לקחת בחשבון בהערכת התוצאות?",
            body_html=(
                "<p>לפני שמסיקים מסקנות מערך HOMA-IR בודד, זכרו את הנקודות הבאות:</p>"
                "<ul>"
                "<li><strong>משך הצום:</strong> הדגימה צריכה להילקח לאחר צום של "
                "8–12 שעות לפחות. צום לא מספיק משבש הן את הגלוקוז והן את האינסולין.</li>"
                "<li><strong>מתח ושינה:</strong> מתח חד וחוסר שינה מעלים קורטיזול, "
                "מה שמשפיע על האיזון בין אינסולין לגלוקוז.</li>"
                "<li><strong>תרופות:</strong> קורטיקוסטרואידים, תרופות אנטי-פסיכוטיות "
                "מסוימות ותרופות אחרות עלולים להשפיע על רגישות לאינסולין. ספרו לרופא "
                "על כל תרופה שאתם נוטלים.</li>"
                "<li><strong>תזונה ופעילות גופנית:</strong> שינויים תזונתיים חריגים או "
                "פעילות גופנית מאומצת בימים שלפני הבדיקה יכולים להשפיע באופן זמני.</li>"
                "<li><strong>ערך בודד מול מגמה:</strong> HOMA-IR בודד הוא תמונת רגע. "
                "המגמה לאורך זמן הרבה יותר משמעותית.</li>"
                "<li><strong>שונות אישית:</strong> גיל, מין, מוצא אתני ו-BMI "
                "משפיעים על מה שנחשב &laquo;תקין&raquo;.</li>"
                "</ul>"
                "<p>מכל הסיבות האלה, התייחסו ל-HOMA-IR כחלק אחד מתמונה רחבה יותר, "
                "ולא כפסק דין על הבריאות המטבולית שלכם.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>שקלו לדבר עם הרופא על ה-HOMA-IR אם מתקיים אחד מהמצבים הבאים:</p>"
                "<ul>"
                "<li>ה-HOMA-IR שלכם חורג מטווח הייחוס של המעבדה.</li>"
                "<li>יש היסטוריה משפחתית של סוכרת סוג&nbsp;2, תסמונת מטבולית או "
                "מחלות לב וכלי דם.</li>"
                "<li>אתם חווים עלייה בלתי מוסברת במשקל או קושי לרדת במשקל.</li>"
                "<li>אובחנתם עם PCOS או שיש לכם אי-סדירות במחזור.</li>"
                "<li>אתם מרגישים עייפות מתמשכת, צמא מוגבר או צורך תכוף במתן שתן.</li>"
                "<li>אנזימי הכבד מוגברים או נמצאה כבד שומני בהדמיה.</li>"
                "</ul>"
                "<p>גם בהיעדר תסמינים, HOMA-IR מוגבר ראוי לדיון עם הרופא. התערבות "
                "מוקדמת — שינויים תזונתיים, הגברת פעילות גופנית ובמקרה הצורך טיפול "
                "תרופתי — יכולה להאט או אף להפוך את התקדמות העמידות לאינסולין.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="איך NoryaAI יכול לעזור?",
            body_html=(
                "<p>ב-NoryaAI אנחנו לא מאבחנים — אנחנו עוזרים לכם להבין. אתם יכולים "
                '<a href="/analyze">להעלות את תוצאות הבדיקה</a> ולקבל סיכום ברור ומסודר '
                "שמסביר את הערכים שלכם — כולל HOMA-IR — בשפה פשוטה, עם טווחי ייחוס "
                "והקשר. כך קל יותר להתכונן לפגישה עם הרופא ולשאול את השאלות הנכונות.</p>"
                "<p>אנחנו לא מציעים המלצות טיפוליות ולא מסקנות אבחנתיות. המטרה שלנו "
                "היא לגשר בין דו\"ח מעבדה מורכב לשיחה פרודוקטיבית עם הרופא שלכם. "
                'לפרטים על מסלולים ומחירים, בקרו ב<a href="/pricing">מחירון</a> שלנו.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הבהרה",
            body_html=(
                "<p><strong>תוכן זה מיועד למטרות מידע בלבד ואינו מחליף ייעוץ רפואי "
                "או אבחנה.</strong> שוחחו תמיד עם איש מקצוע רפואי מוסמך לגבי ה-HOMA-IR "
                "ושאר תוצאות המעבדה שלכם. רק רופא המכיר את ההיסטוריה וההקשר הקליני שלכם "
                "יכול לפרש את התוצאות כראוי.</p>"
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
            heading="HOMA-IR क्या है और यह क्यों ज़रूरी है?",
            body_html=(
                "<p>अगर आपकी ब्लड रिपोर्ट में <strong>HOMA-IR</strong> नाम का कोई वैल्यू "
                "दिखता है, तो स्वाभाविक है कि आप जानना चाहेंगे कि इसका मतलब क्या है और "
                "क्या चिंता करनी चाहिए। HOMA-IR एक कैलकुलेटेड इंडेक्स है जो बताता है कि "
                "आपका शरीर इंसुलिन के प्रति कितना संवेदनशील है। यह सीधे खून में नहीं मापा "
                "जाता; बल्कि दो रूटीन टेस्ट — फ़ास्टिंग ग्लूकोज़ और फ़ास्टिंग इंसुलिन — "
                "से कैलकुलेट किया जाता है। पिछले कुछ दशकों में इसे इंसुलिन रेज़िस्टेंस की "
                "स्क्रीनिंग के लिए एक सरल और व्यापक रूप से इस्तेमाल होने वाला टूल माना "
                "जाने लगा है।</p>"
                "<p>यह गाइड बताती है कि HOMA-IR क्या है, इसकी गणना कैसे होती है, यह क्या "
                "बता सकता है और क्या नहीं, और डॉक्टर से कब बात करनी चाहिए। हमारा उद्देश्य "
                "डायग्नोसिस देना नहीं है — बल्कि आपको अपनी रिपोर्ट बेहतर समझने में मदद "
                "करना है ताकि आप अपने डॉक्टर से सही सवाल पूछ सकें।</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="HOMA-IR वास्तव में क्या है?",
            body_html=(
                "<p><strong>HOMA-IR</strong> का पूरा नाम है <em>Homeostatic Model Assessment "
                "for Insulin Resistance</em> (इंसुलिन रेज़िस्टेंस के लिए होमियोस्टैटिक "
                "मॉडल असेसमेंट)। इसे 1985 में Matthews और उनके सहयोगियों ने विकसित किया "
                "था। इसका मकसद एक सामान्य फ़ास्टिंग ब्लड सैंपल से इंसुलिन रेज़िस्टेंस का "
                "अंदाज़ा लगाना है — बिना महंगे और जटिल क्लैम्प टेस्ट के। सिद्धांत सरल है: "
                "स्वस्थ मेटाबॉलिज़्म में पैंक्रियास उतना ही इंसुलिन बनाता है जितना ब्लड "
                "शुगर को एक तय सीमा में रखने के लिए ज़रूरी हो। जब कोशिकाएं इंसुलिन के "
                "प्रति कम संवेदनशील होने लगती हैं, तो पैंक्रियास ज़्यादा इंसुलिन बनाकर "
                "भरपाई करता है। HOMA-IR इस असंतुलन को एक संख्या में व्यक्त करता है।</p>"
                "<p>क्लिनिकल प्रैक्टिस में HOMA-IR का उपयोग मेटाबॉलिक सिंड्रोम, "
                "टाइप&nbsp;2 डायबिटीज़ के जोखिम, पॉलीसिस्टिक ओवेरी सिंड्रोम (PCOS) और "
                "नॉन-अल्कोहॉलिक फ़ैटी लिवर डिज़ीज़ (NAFLD) के मूल्यांकन में होता है। "
                "शुरू में ही समझ लें: HOMA-IR एक <em>स्क्रीनिंग</em> टूल है, डायग्नोस्टिक "
                "टेस्ट नहीं। एक अकेला वैल्यू किसी बीमारी की पुष्टि या खंडन नहीं करता; "
                "इसे हमेशा क्लिनिकल हिस्ट्री, लक्षणों और अन्य लैब फ़ाइंडिंग्स के साथ "
                "पढ़ना चाहिए।</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="HOMA-IR की गणना कैसे होती है?",
            body_html=(
                "<p>गणना काफ़ी सीधी है। ग्लूकोज़ की यूनिट के आधार पर दो फ़ॉर्मूले "
                "इस्तेमाल होते हैं:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">ग्लूकोज़ यूनिट</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">फ़ॉर्मूला</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL (भारत में सामान्य)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">फ़ास्टिंग इंसुलिन (μU/mL) &times; फ़ास्टिंग ग्लूकोज़ (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">फ़ास्टिंग इंसुलिन (μU/mL) &times; फ़ास्टिंग ग्लूकोज़ (mmol/L) &divide; 22.5</td>'
                "</tr></tbody></table>"
                "<p>405 और 22.5 कैलिब्रेशन फ़ैक्टर हैं जो स्वस्थ व्यक्तियों के "
                "औसत से निकाले गए हैं। दोनों फ़ॉर्मूले एक ही रिज़ल्ट देते हैं; फ़र्क "
                "सिर्फ़ ग्लूकोज़ की यूनिट का है। भारत में ज़्यादातर लैब mg/dL इस्तेमाल "
                "करती हैं, इसलिए 405 वाला फ़ॉर्मूला अधिक दिखता है।</p>"
                "<p>उदाहरण: फ़ास्टिंग इंसुलिन 10&nbsp;μU/mL, फ़ास्टिंग ग्लूकोज़ "
                "100&nbsp;mg/dL — HOMA-IR&nbsp;=&nbsp;(10&nbsp;&times;&nbsp;100)&nbsp;/&nbsp;"
                "405&nbsp;&asymp;&nbsp;2.47। कैलकुलेशन सही आए इसके लिए ब्लड सैंपल कम "
                "से कम 8–12 घंटे की फ़ास्टिंग के बाद लिया जाना चाहिए।</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="फ़ास्टिंग ग्लूकोज़ से संबंध",
            body_html=(
                "<p><strong>फ़ास्टिंग ग्लूकोज़</strong> (फ़ास्टिंग ब्लड शुगर) कम से कम "
                "8 घंटे बिना खाए-पिए खून में ग्लूकोज़ की मात्रा है। सामान्य रेंज आमतौर पर "
                "70–100&nbsp;mg/dL होती है। यह HOMA-IR फ़ॉर्मूले के दो इनपुट में से "
                "एक है।</p>"
                "<p>एक अहम बात: इंसुलिन रेज़िस्टेंस विकसित होने के बावजूद फ़ास्टिंग "
                "ग्लूकोज़ सालों तक नॉर्मल रह सकता है। पैंक्रियास ज़्यादा इंसुलिन बनाकर "
                "ग्लूकोज़ को काबू में रखता है — लेकिन बढ़े हुए इंसुलिन की क़ीमत पर। "
                "अगर सिर्फ़ फ़ास्टिंग ग्लूकोज़ देखें, तो यह शुरुआती बदलाव छूट सकता है। "
                "HOMA-IR, इंसुलिन को भी शामिल करने की वजह से, इस तनाव को पहले उजागर "
                "कर सकता है।</p>"
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="फ़ास्टिंग इंसुलिन से संबंध",
            body_html=(
                "<p><strong>फ़ास्टिंग इंसुलिन</strong> रात भर के उपवास (8–12 घंटे) के "
                "बाद खून में इंसुलिन का स्तर है। रेफ़रेंस रेंज लैब के अनुसार अलग-अलग "
                "होती है, पर आमतौर पर 2–25&nbsp;μU/mL के बीच होती है। यह HOMA-IR "
                "फ़ॉर्मूले का दूसरा इनपुट है और शुरुआती इंसुलिन रेज़िस्टेंस के संदर्भ "
                "में अक्सर अधिक जानकारीपूर्ण होता है।</p>"
                "<p>जब कोशिकाएं इंसुलिन पर कम प्रतिक्रिया देती हैं, तो पैंक्रियास और "
                "ज़्यादा इंसुलिन बनाता है — इसे <em>कम्पेंसेटरी हाइपरइंसुलिनीमिया</em> "
                "कहते हैं। ग्लूकोज़ स्थिर रहता है, लेकिन इंसुलिन बढ़ता है, जिससे HOMA-IR "
                "ऊपर जाता है और यह मेटाबॉलिक समस्या का शुरुआती संकेत हो सकता है।</p>"
                "<p>ध्यान रहे कि इंसुलिन की जांच अलग-अलग लैब में अलग-अलग तरीके से होती "
                "है, और तनाव, नींद की कमी, कुछ दवाएं (जैसे कॉर्टिकोस्टेरॉइड्स) और "
                "सैंपल लेने का समय — ये सब रिज़ल्ट को प्रभावित कर सकते हैं। इसलिए एक "
                "अकेली वैल्यू को अंतिम फ़ैसला न मानें; इसे पूरी क्लिनिकल तस्वीर में "
                "देखें।</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="इंसुलिन रेज़िस्टेंस से जुड़ाव",
            body_html=(
                "<p><strong>इंसुलिन रेज़िस्टेंस</strong> तब होती है जब मांसपेशी, फ़ैट "
                "और लिवर की कोशिकाएं इंसुलिन के संकेत पर ग्लूकोज़ को सही से अवशोषित "
                "नहीं कर पातीं। पैंक्रियास ज़्यादा इंसुलिन बनाकर मुआवज़ा करता है, लेकिन "
                "समय के साथ यह नाकाफ़ी हो सकता है और ब्लड शुगर बढ़ने लगता है। इंसुलिन "
                "रेज़िस्टेंस का गहरा संबंध मेटाबॉलिक सिंड्रोम, टाइप&nbsp;2 डायबिटीज़, "
                "हृदय रोग, PCOS और NAFLD से है।</p>"
                "<p>कई संदर्भों में HOMA-IR 1.0 से कम को बेहतरीन माना जाता है। 2.5–2.9 "
                "से ऊपर की वैल्यू अक्सर इंसुलिन रेज़िस्टेंस की ओर इशारा करती है। हालांकि, "
                "ये कट-ऑफ़ जनसंख्या, जातीयता, उम्र, लिंग और लैब मेथड के अनुसार बदलते "
                "हैं — कोई एक सार्वभौमिक सीमा नहीं है।</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">HOMA-IR रेंज</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;">सामान्य व्याख्या (संदर्भ के लिए)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">इंसुलिन के प्रति बेहतरीन संवेदनशीलता</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.0 – 2.4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">सामान्य / सीमावर्ती — क्लिनिकल संदर्भ ज़रूरी</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2.5 – 2.9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">इंसुलिन रेज़िस्टेंस की बढ़ी संभावना</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">इंसुलिन रेज़िस्टेंस की प्रबल संभावना</td>'
                "</tr></tbody></table>"
                "<p>ऊपर दी गई टेबल केवल मार्गदर्शन के लिए है। आपके डॉक्टर इस वैल्यू को "
                "आपकी पूरी क्लिनिकल तस्वीर, पारिवारिक इतिहास, BMI और अन्य लैब "
                "रिज़ल्ट्स के साथ मिलाकर समझेंगे।</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="HOMA-IR अकेला काफ़ी क्यों नहीं?",
            body_html=(
                "<p>HOMA-IR एक उपयोगी स्क्रीनिंग टूल है, लेकिन इसकी कुछ अहम सीमाएं "
                "हैं:</p>"
                "<ul>"
                "<li>यह सिर्फ़ फ़ास्टिंग वैल्यू पर आधारित है और खाने के बाद इंसुलिन-ग्लूकोज़ "
                "डायनामिक्स को नहीं दर्शाता।</li>"
                "<li>तनाव, बीमारी, नींद की कमी या ब्लड सैंपल से पहले तेज़ एक्सरसाइज़ "
                "रिज़ल्ट को अस्थायी रूप से बदल सकते हैं।</li>"
                "<li>जिन लोगों में बीटा-सेल की कार्यक्षमता गंभीर रूप से कम हो चुकी है "
                "(जैसे पुरानी टाइप&nbsp;2 डायबिटीज़), उनमें इंसुलिन उत्पादन पहले से "
                "कम होता है, जिससे HOMA-IR भ्रामक रूप से कम आ सकता है।</li>"
                "<li>अलग-अलग लैब में इंसुलिन मापने के तरीकों में फ़र्क होने से रिज़ल्ट "
                "थोड़ा अलग आ सकता है।</li>"
                "</ul>"
                "<p>इन कारणों से HOMA-IR को हमेशा फ़ास्टिंग ग्लूकोज़, HbA1c, लिपिड "
                "प्रोफ़ाइल, लिवर एंज़ाइम्स और डॉक्टर के क्लिनिकल असेसमेंट के साथ "
                "मिलाकर देखना चाहिए।</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="रिज़ल्ट का मूल्यांकन करते समय किन बातों का ध्यान रखें?",
            body_html=(
                "<p>एक अकेली HOMA-IR वैल्यू से कोई निष्कर्ष निकालने से पहले ये बातें "
                "याद रखें:</p>"
                "<ul>"
                "<li><strong>फ़ास्टिंग की अवधि:</strong> ब्लड सैंपल कम से कम 8–12 घंटे "
                "की फ़ास्टिंग के बाद लिया जाना चाहिए। अधूरी फ़ास्टिंग ग्लूकोज़ और "
                "इंसुलिन दोनों को प्रभावित करती है।</li>"
                "<li><strong>तनाव और नींद:</strong> तीव्र तनाव और नींद की कमी कॉर्टिसोल "
                "बढ़ाते हैं, जो इंसुलिन-ग्लूकोज़ संतुलन को प्रभावित करता है।</li>"
                "<li><strong>दवाइयां:</strong> कॉर्टिकोस्टेरॉइड्स, कुछ एंटीसाइकोटिक्स "
                "और अन्य दवाएं इंसुलिन सेंसिटिविटी बदल सकती हैं। डॉक्टर को अपनी "
                "सभी दवाओं के बारे में ज़रूर बताएं।</li>"
                "<li><strong>खानपान और व्यायाम:</strong> टेस्ट से पहले के दिनों में "
                "असामान्य डाइट या भारी एक्सरसाइज़ रिज़ल्ट अस्थायी रूप से बदल "
                "सकती है।</li>"
                "<li><strong>एक वैल्यू बनाम ट्रेंड:</strong> एक अकेला HOMA-IR एक "
                "स्नैपशॉट है। समय के साथ बदलाव (ट्रेंड) कहीं ज़्यादा मायने रखता है।</li>"
                "<li><strong>व्यक्तिगत भिन्नता:</strong> उम्र, लिंग, जातीयता और BMI — "
                "ये सब प्रभावित करते हैं कि &laquo;सामान्य&raquo; रेंज आपके लिए क्या "
                "है।</li>"
                "</ul>"
                "<p>इन सभी कारणों से HOMA-IR को अपनी मेटाबॉलिक सेहत की बड़ी तस्वीर "
                "का एक हिस्सा मानें, अकेला फ़ैसला नहीं।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>इनमें से कोई भी स्थिति हो तो HOMA-IR पर डॉक्टर से बात करें:</p>"
                "<ul>"
                "<li>आपका HOMA-IR लैब की रेफ़रेंस रेंज से ऊपर है।</li>"
                "<li>परिवार में टाइप&nbsp;2 डायबिटीज़, मेटाबॉलिक सिंड्रोम या हृदय रोग "
                "का इतिहास है।</li>"
                "<li>बिना किसी स्पष्ट कारण वज़न बढ़ रहा है या वज़न कम करना मुश्किल हो "
                "रहा है।</li>"
                "<li>PCOS का निदान हुआ है या पीरियड्स अनियमित हैं।</li>"
                "<li>थकान, ज़्यादा प्यास या बार-बार पेशाब जैसे लक्षण महसूस हो रहे हैं।</li>"
                "<li>लिवर एंज़ाइम्स बढ़े हुए हैं या फ़ैटी लिवर पाया गया है।</li>"
                "</ul>"
                "<p>लक्षण न भी हों, तो भी बढ़ा हुआ HOMA-IR डॉक्टर को बताना सही "
                "कदम है। शुरुआती कदम — खानपान में सुधार, शारीरिक गतिविधि बढ़ाना और "
                "ज़रूरत पड़ने पर दवाई — इंसुलिन रेज़िस्टेंस की प्रगति को धीमा या "
                "उलट सकते हैं।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="NoryaAI कैसे मदद कर सकता है?",
            body_html=(
                "<p>NoryaAI में हम डायग्नोसिस नहीं देते — हम आपको समझने में मदद करते हैं। "
                "आप अपनी लैब रिपोर्ट "
                '<a href="/analyze">विश्लेषण पेज</a> पर अपलोड कर सकते हैं और एक साफ़, '
                "व्यवस्थित सारांश पा सकते हैं जो आपकी वैल्यूज़ — HOMA-IR सहित — सरल "
                "भाषा में, रेफ़रेंस रेंज और संदर्भ के साथ समझाता है। इससे डॉक्टर की "
                "अपॉइंटमेंट की तैयारी आसान हो जाती है।</p>"
                "<p>हम इलाज की सलाह या डायग्नोस्टिक निष्कर्ष नहीं देते। हमारा लक्ष्य "
                "एक जटिल लैब रिपोर्ट और डॉक्टर के साथ एक उपयोगी बातचीत के बीच का "
                "पुल बनना है। विकल्पों और कीमतों के लिए हमारा "
                '<a href="/pricing">प्राइसिंग</a> पेज देखें।</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                "<p><strong>यह सामग्री केवल जानकारी के लिए है और चिकित्सा सलाह या "
                "निदान का विकल्प नहीं है।</strong> अपने HOMA-IR और अन्य सभी लैब "
                "रिज़ल्ट्स के बारे में हमेशा एक योग्य स्वास्थ्य पेशेवर से चर्चा करें। "
                "केवल वही डॉक्टर जो आपकी हिस्ट्री और क्लिनिकल संदर्भ जानते हैं, "
                "आपके रिज़ल्ट्स की सही व्याख्या कर सकते हैं।</p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC  (RTL)
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="ما هو HOMA-IR ولماذا هو مهم؟",
            body_html=(
                "<p>إذا ظهر في تقرير تحاليلك قيمة تُسمى <strong>HOMA-IR</strong>، فمن "
                "الطبيعي أن تتساءل عن معناها وما إذا كان هناك ما يدعو للقلق. HOMA-IR هو "
                "مؤشر محسوب يُقدّر مدى حساسية جسمك للأنسولين. لا يُقاس مباشرة في الدم بل "
                "يُحسب من تحليلين روتينيين: الغلوكوز الصائم والأنسولين الصائم. خلال العقود "
                "الأخيرة أصبح أداة فحص بسيطة وشائعة الاستخدام، خاصة للكشف المبكر عن "
                "مقاومة الأنسولين.</p>"
                "<p>يشرح هذا الدليل ماهية HOMA-IR وكيفية حسابه وما يستطيع وما لا يستطيع "
                "إخبارك به، ومتى ينبغي مراجعة الطبيب. هدفنا ليس التشخيص — بل مساعدتك "
                "على فهم نتيجتك كي تذهب إلى موعدك الطبي بمعلومات أوضح.</p>"
            ),
        ),
        Section(
            id="what-is-homa-ir", level=2,
            heading="ما هو HOMA-IR بالتحديد؟",
            body_html=(
                "<p><strong>HOMA-IR</strong> اختصار لـ <em>Homeostatic Model Assessment for "
                "Insulin Resistance</em> (تقييم النموذج الاستتبابي لمقاومة الأنسولين). "
                "نُشر هذا النموذج عام 1985 على يد Matthews وزملائه، ويتيح تقدير مقاومة "
                "الأنسولين من عيّنة دم بسيطة تُؤخذ صائماً — دون الحاجة لاختبار الـ Clamp "
                "المعقد والمكلف. المبدأ واضح: في الاستقلاب السليم يُفرز البنكرياس كمية "
                "كافية من الأنسولين للحفاظ على الغلوكوز ضمن نطاق ضيق. عندما تبدأ الخلايا "
                "بالاستجابة أقل للأنسولين، يعوّض البنكرياس بإنتاج المزيد. يُعبّر HOMA-IR "
                "عن هذا الاختلال بعدد واحد.</p>"
                "<p>في الممارسة السريرية يُستخدم HOMA-IR في تقييم المتلازمة الأيضية "
                "(الاستقلابية)، وخطر الإصابة بالسكري من النوع&nbsp;2، ومتلازمة تكيّس "
                "المبايض (PCOS)، ومرض الكبد الدهني غير الكحولي (NAFLD). من المهم أن "
                "تفهم منذ البداية أن HOMA-IR أداة <em>فحص</em> وليس اختباراً تشخيصياً. "
                "قيمة واحدة لا تؤكد ولا تنفي أي مرض؛ يجب دائماً تفسيرها مع السياق "
                "السريري الكامل.</p>"
            ),
        ),
        Section(
            id="how-calculated", level=2,
            heading="كيف يُحسب HOMA-IR؟",
            body_html=(
                "<p>الحساب بسيط. هناك صيغتان حسب وحدة قياس الغلوكوز:</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">وحدة الغلوكوز</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">الصيغة</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mg/dL (شائع في الدول العربية)</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">أنسولين صائم (μU/mL) &times; غلوكوز صائم (mg/dL) &divide; 405</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">mmol/L</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">أنسولين صائم (μU/mL) &times; غلوكوز صائم (mmol/L) &divide; 22.5</td>'
                "</tr></tbody></table>"
                "<p>الثابتان 405 و22.5 عوامل معايرة مشتقة من متوسطات أفراد أصحاء. كلتا "
                "الصيغتين تعطيان النتيجة نفسها؛ الفرق فقط في وحدة الغلوكوز. في معظم "
                "الدول العربية يُستخدم mg/dL، لذا الصيغة مع 405 هي الأكثر شيوعاً.</p>"
                "<p>مثال: أنسولين صائم 11&nbsp;μU/mL، غلوكوز صائم 94&nbsp;mg/dL — "
                "HOMA-IR&nbsp;=&nbsp;(11&nbsp;&times;&nbsp;94)&nbsp;/&nbsp;405&nbsp;&asymp;&nbsp;2.55. "
                "لكي يكون الحساب موثوقاً، يجب أن تُؤخذ العيّنة بعد صيام لا يقل عن "
                "8–12 ساعة.</p>"
            ),
        ),
        Section(
            id="fasting-glucose-relation", level=2,
            heading="العلاقة مع الغلوكوز الصائم",
            body_html=(
                "<p><strong>الغلوكوز الصائم</strong> (سكر الدم الصائم) هو تركيز الغلوكوز "
                "في الدم بعد الامتناع عن الأكل لمدة 8 ساعات على الأقل. القيم الطبيعية "
                "عادةً تتراوح بين 70 و100&nbsp;mg/dL. هو أحد مكوّني معادلة HOMA-IR.</p>"
                "<p>نقطة جوهرية: يمكن أن يبقى الغلوكوز الصائم ضمن النطاق الطبيعي لسنوات "
                "حتى مع تطوّر مقاومة الأنسولين. يعوّض البنكرياس بإفراز المزيد من الأنسولين "
                "للحفاظ على الغلوكوز مستقراً — لكن بثمن ارتفاع مستويات الأنسولين. إذا "
                "نظرت فقط إلى الغلوكوز، فقد يفوتك هذا التحوّل الأيضي المبكر. HOMA-IR، "
                "بدمجه الأنسولين مع الغلوكوز، يمكنه كشف هذا العبء قبل أن يرتفع "
                "الغلوكوز نفسه.</p>"
            ),
        ),
        Section(
            id="fasting-insulin-relation", level=2,
            heading="العلاقة مع الأنسولين الصائم",
            body_html=(
                "<p><strong>الأنسولين الصائم</strong> هو مستوى الأنسولين في الدم بعد "
                "صيام ليلي لا يقل عن 8–12 ساعة. نطاقات المرجع تختلف بين المختبرات لكنها "
                "عادةً بين 2 و25&nbsp;μU/mL. هو المكوّن الثاني في معادلة HOMA-IR، وغالباً "
                "الأكثر دلالة في سياق مقاومة الأنسولين المبكرة.</p>"
                "<p>عندما تستجيب الخلايا أقل للأنسولين، يزيد البنكرياس إفرازه — وهي حالة "
                "تُسمى <em>فرط الأنسولين التعويضي</em>. يبقى الغلوكوز مستقراً لكن "
                "الأنسولين يرتفع، مما يرفع HOMA-IR وقد يكون من أبكر العلامات القابلة "
                "للكشف عن مشكلة أيضية.</p>"
                "<p>تجدر الإشارة إلى أن اختبارات الأنسولين تختلف بين المختبرات، وعوامل "
                "مثل التوتر وقلة النوم وبعض الأدوية (كورتيكوستيرويدات، بعض مضادات "
                "الذهان) وحتى توقيت سحب العيّنة يمكن أن تؤثر على القراءة. لذا فإن "
                "قياساً واحداً هو لقطة وليس حكماً نهائياً، ويجب وضعه في سياق الصورة "
                "السريرية الكاملة.</p>"
            ),
        ),
        Section(
            id="insulin-resistance-connection", level=2,
            heading="الصلة بمقاومة الأنسولين",
            body_html=(
                "<p><strong>مقاومة الأنسولين</strong> تحدث عندما تستجيب خلايا العضلات "
                "والدهون والكبد بشكل أقل فعالية لإشارة الأنسولين لامتصاص الغلوكوز. "
                "يعوّض البنكرياس بإنتاج المزيد، لكن مع الوقت قد لا يكفي ذلك ويبدأ "
                "الغلوكوز بالارتفاع. ترتبط مقاومة الأنسولين ارتباطاً وثيقاً بالمتلازمة "
                "الأيضية وداء السكري من النوع&nbsp;2 وأمراض القلب والأوعية الدموية "
                "وPCOS وNAFLD.</p>"
                "<p>تعتبر كثير من المراجع أن HOMA-IR أقل من 1.0 هو القيمة المثلى. "
                "قيم فوق 2.5–2.9 غالباً ما تُفسَّر كمؤشر على مقاومة الأنسولين. لكن "
                "نقاط القطع هذه تعتمد على السكان والعرق والعمر والجنس وطريقة "
                "المختبر. لا يوجد حدّ واحد عالمي.</p>"
                '<table class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;">'
                "<thead><tr>"
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">نطاق HOMA-IR</th>'
                '<th style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;">التفسير العام (استرشادي)</th>'
                "</tr></thead><tbody>"
                "<tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&lt;&nbsp;1.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">حساسية مثالية للأنسولين</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">1.0 – 2.4</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">طبيعي / حدّي — السياق السريري يحسم</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&ge; 2.5 – 2.9</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">احتمالية متزايدة لمقاومة الأنسولين</td>'
                "</tr><tr>"
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">&gt;&nbsp;3.0</td>'
                '<td style="border:1px solid #cbd5e1;padding:8px 12px;">مؤشر واضح على مقاومة الأنسولين</td>'
                "</tr></tbody></table>"
                "<p>الجدول أعلاه للاسترشاد فقط. سيُفسّر طبيبك القيمة في ضوء صورتك "
                "السريرية الكاملة وتاريخك العائلي ومؤشر كتلة الجسم ونتائج أخرى.</p>"
            ),
        ),
        Section(
            id="not-enough-alone", level=2,
            heading="لماذا لا يكفي HOMA-IR وحده؟",
            body_html=(
                "<p>HOMA-IR أداة فحص مفيدة، لكن لها حدود مهمة:</p>"
                "<ul>"
                "<li>يعتمد فقط على قيم الصيام ولا يعكس ديناميكية الأنسولين والغلوكوز "
                "بعد الوجبات.</li>"
                "<li>التوتر الحاد أو المرض أو قلة النوم أو التمارين المكثفة قبل "
                "سحب العيّنة قد تغيّر النتيجة مؤقتاً.</li>"
                "<li>عند من يعانون من خلل متقدم في خلايا بيتا (مثل السكري من "
                "النوع&nbsp;2 المزمن) قد يكون إنتاج الأنسولين منخفضاً أصلاً، مما "
                "يجعل HOMA-IR منخفضاً بشكل مضلل.</li>"
                "<li>الاختلافات في اختبارات الأنسولين بين المختبرات قد تنتج نتائج "
                "مختلفة قليلاً.</li>"
                "</ul>"
                "<p>لذلك يجب دائماً تقييم HOMA-IR إلى جانب الغلوكوز الصائم وHbA1c "
                "وملف الدهون وإنزيمات الكبد والتقييم السريري الشامل.</p>"
            ),
        ),
        Section(
            id="evaluating-results", level=2,
            heading="ما يجب مراعاته عند تقييم النتائج",
            body_html=(
                "<p>قبل أن تستخلص استنتاجات من قيمة HOMA-IR واحدة، ضع في اعتبارك "
                "النقاط التالية:</p>"
                "<ul>"
                "<li><strong>مدة الصيام:</strong> يجب سحب العيّنة بعد صيام لا يقل عن "
                "8–12 ساعة. الصيام غير الكافي يؤثر على الغلوكوز والأنسولين معاً.</li>"
                "<li><strong>التوتر والنوم:</strong> التوتر الحاد وقلة النوم يرفعان "
                "الكورتيزول مما يؤثر على توازن الأنسولين والغلوكوز.</li>"
                "<li><strong>الأدوية:</strong> الكورتيكوستيرويدات وبعض مضادات الذهان "
                "وأدوية أخرى قد تغيّر حساسية الأنسولين. أخبر طبيبك دائماً بجميع "
                "أدويتك.</li>"
                "<li><strong>النظام الغذائي والنشاط البدني:</strong> تغييرات غذائية غير "
                "معتادة أو تمارين مكثفة في الأيام السابقة للتحليل قد تؤثر مؤقتاً على "
                "النتيجة.</li>"
                "<li><strong>قيمة واحدة مقابل الاتجاه:</strong> HOMA-IR واحد هو لقطة "
                "آنية. الاتجاه عبر الزمن أكثر دلالة بكثير.</li>"
                "<li><strong>الاختلافات الفردية:</strong> العمر والجنس والعرق ومؤشر "
                "كتلة الجسم تؤثر على ما يُعتبر &laquo;طبيعياً&raquo;.</li>"
                "</ul>"
                "<p>لكل هذه الأسباب، اعتبر HOMA-IR قطعة واحدة في لوحة أكبر، وليس "
                "حكماً منفرداً على صحتك الأيضية.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>فكّر في مناقشة نتيجة HOMA-IR مع طبيبك إذا انطبق أي مما يلي:</p>"
                "<ul>"
                "<li>HOMA-IR أعلى من النطاق المرجعي للمختبر.</li>"
                "<li>هناك تاريخ عائلي للسكري من النوع&nbsp;2 أو المتلازمة الأيضية "
                "أو أمراض القلب والأوعية الدموية.</li>"
                "<li>تلاحظ زيادة وزن غير مبررة أو صعوبة في إنقاص الوزن.</li>"
                "<li>شُخّصت بمتلازمة تكيّس المبايض أو تعانين من عدم انتظام الدورة "
                "الشهرية.</li>"
                "<li>تشعر بإرهاق مستمر أو عطش مفرط أو كثرة التبول.</li>"
                "<li>إنزيمات الكبد مرتفعة أو تبيّن وجود كبد دهني بالتصوير.</li>"
                "</ul>"
                "<p>حتى في غياب الأعراض، HOMA-IR المرتفع يستحق المناقشة مع الطبيب. "
                "التدخل المبكر — تعديل النظام الغذائي وزيادة النشاط البدني وأحياناً "
                "العلاج الدوائي — يمكن أن يُبطئ أو يعكس تقدّم مقاومة الأنسولين.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يمكن لـ NoryaAI مساعدتك؟",
            body_html=(
                "<p>في NoryaAI لا نُشخّص — بل نساعدك على الفهم. يمكنك "
                '<a href="/analyze">رفع تقرير تحاليلك</a> والحصول على ملخص واضح '
                "ومنظّم يشرح قيمك — بما فيها HOMA-IR — بلغة مبسّطة مع النطاقات "
                "المرجعية والسياق. هذا يسهّل تحضيرك لموعد الطبيب وطرح الأسئلة "
                "المناسبة.</p>"
                "<p>لا نقدّم توصيات علاجية ولا استنتاجات تشخيصية. هدفنا جسر الفجوة "
                "بين تقرير مخبري قد يبدو معقداً وحوار بنّاء مع طبيبك. للاطّلاع على "
                'خياراتنا وأسعارنا، زُر صفحة <a href="/pricing">الأسعار</a>.</p>'
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء مسؤولية",
            body_html=(
                "<p><strong>هذا المحتوى لأغراض المعلومات فقط ولا يحل محل الاستشارة "
                "الطبية أو التشخيص.</strong> ناقش دائماً HOMA-IR وجميع نتائج تحاليلك "
                "مع مختص رعاية صحية مؤهل. الطبيب الذي يعرف تاريخك وسياقك السريري "
                "هو وحده القادر على تفسير نتائجك بشكل صحيح.</p>"
            ),
        ),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_homa_ir_sections_by_lang():
    """Returns sections_by_lang dict for HOMA-IR article (all 9 languages)."""
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


def get_homa_ir_faq_schema_qa():
    """Returns faq_schema_qa dict for HOMA-IR article (all 9 languages)."""
    return {
        "en": [
            {"question": "What is HOMA-IR?",
             "answer": "HOMA-IR (Homeostatic Model Assessment for Insulin Resistance) is a calculated index that estimates insulin resistance from fasting insulin and fasting glucose levels. It is a screening tool, not a diagnostic test, and should be interpreted by a doctor alongside other clinical information."},
            {"question": "How is HOMA-IR calculated?",
             "answer": "HOMA-IR is calculated as fasting insulin (μU/mL) multiplied by fasting glucose (mg/dL), divided by 405. If glucose is in mmol/L, divide by 22.5 instead. Both formulas give the same result."},
            {"question": "What is a normal HOMA-IR value?",
             "answer": "Many references consider a HOMA-IR below 1.0 as optimal. Values above 2.5–2.9 are often cited as suggestive of insulin resistance, but cut-offs vary by population, age, sex, and laboratory method. Always discuss your result with your doctor."},
        ],
        "tr": [
            {"question": "HOMA-IR nedir?",
             "answer": "HOMA-IR (Homeostatic Model Assessment for Insulin Resistance), açlık insülini ve açlık glukozu düzeylerinden insülin direncini tahmin eden hesaplanmış bir indekstir. Tanı koydurma aracı değil, tarama aracıdır ve diğer klinik bilgilerle birlikte hekim tarafından yorumlanmalıdır."},
            {"question": "HOMA-IR nasıl hesaplanır?",
             "answer": "Açlık insülini (μU/mL) ile açlık glukozu (mg/dL) çarpılıp 405'e bölünür. Glukoz mmol/L ise 22,5'e bölünür. Her iki formül de aynı sonucu verir."},
            {"question": "Normal HOMA-IR değeri nedir?",
             "answer": "Pek çok kaynakta 1,0'ın altı optimal kabul edilir. 2,5–2,9 üzeri değerler insülin direncine işaret edebilir, ancak eşik değerleri popülasyona, yaşa, cinsiyete ve laboratuvar yöntemine göre değişir. Sonucunuzu mutlaka hekiminizle görüşün."},
        ],
        "es": [
            {"question": "¿Qué es el HOMA-IR?",
             "answer": "El HOMA-IR (Homeostatic Model Assessment for Insulin Resistance) es un índice calculado que estima la resistencia a la insulina a partir de la insulina y la glucosa en ayunas. Es una herramienta de cribado, no un test diagnóstico, y debe interpretarse por un médico junto con otra información clínica."},
            {"question": "¿Cómo se calcula el HOMA-IR?",
             "answer": "Se multiplica la insulina en ayunas (μU/mL) por la glucosa en ayunas (mg/dL) y se divide entre 405. Si la glucosa está en mmol/L, se divide entre 22,5. Ambas fórmulas dan el mismo resultado."},
            {"question": "¿Cuál es un valor normal de HOMA-IR?",
             "answer": "Muchas referencias consideran óptimo un HOMA-IR inferior a 1,0. Valores por encima de 2,5–2,9 suelen indicar resistencia a la insulina, pero los umbrales varían según la población, la edad, el sexo y el método de laboratorio. Consulta siempre con tu médico."},
        ],
        "de": [
            {"question": "Was ist der HOMA-IR?",
             "answer": "Der HOMA-IR (Homeostatic Model Assessment for Insulin Resistance) ist ein rechnerischer Index, der die Insulinresistenz anhand von Nüchterninsulin und Nüchternglukose schätzt. Er ist ein Screening-Instrument, kein diagnostischer Test, und muss vom Arzt im klinischen Gesamtkontext bewertet werden."},
            {"question": "Wie wird der HOMA-IR berechnet?",
             "answer": "Nüchterninsulin (μU/mL) wird mit Nüchternglukose (mg/dL) multipliziert und durch 405 geteilt. Bei mmol/L teilt man durch 22,5. Beide Formeln liefern dasselbe Ergebnis."},
            {"question": "Was ist ein normaler HOMA-IR-Wert?",
             "answer": "Viele Quellen betrachten einen HOMA-IR unter 1,0 als optimal. Werte über 2,5–2,9 gelten häufig als Hinweis auf Insulinresistenz, wobei die Grenzwerte je nach Population, Alter, Geschlecht und Labormethode variieren. Besprechen Sie Ihr Ergebnis immer mit Ihrem Arzt."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le HOMA-IR ?",
             "answer": "Le HOMA-IR (Homeostatic Model Assessment for Insulin Resistance) est un indice calculé qui estime l'insulinorésistance à partir de l'insuline et de la glycémie à jeun. C'est un outil de dépistage, pas un test diagnostique, et il doit être interprété par un médecin en tenant compte du contexte clinique."},
            {"question": "Comment le HOMA-IR est-il calculé ?",
             "answer": "On multiplie l'insuline à jeun (μU/mL) par la glycémie à jeun (mg/dL) et on divise par 405. Si la glycémie est en mmol/L, on divise par 22,5. Les deux formules donnent le même résultat."},
            {"question": "Quelle est la valeur normale du HOMA-IR ?",
             "answer": "De nombreuses références considèrent un HOMA-IR inférieur à 1,0 comme optimal. Des valeurs supérieures à 2,5–2,9 sont souvent évocatrices d'insulinorésistance, mais les seuils varient selon la population, l'âge, le sexe et la méthode de dosage. Discutez toujours de votre résultat avec votre médecin."},
        ],
        "it": [
            {"question": "Cos'è l'HOMA-IR?",
             "answer": "L'HOMA-IR (Homeostatic Model Assessment for Insulin Resistance) è un indice calcolato che stima la resistenza insulinica a partire dall'insulinemia e dalla glicemia a digiuno. È uno strumento di screening, non un test diagnostico, e va interpretato dal medico nel contesto clinico complessivo."},
            {"question": "Come si calcola l'HOMA-IR?",
             "answer": "Si moltiplica l'insulinemia a digiuno (μU/mL) per la glicemia a digiuno (mg/dL) e si divide per 405. Se la glicemia è in mmol/L, si divide per 22,5. Entrambe le formule danno lo stesso risultato."},
            {"question": "Qual è un valore normale di HOMA-IR?",
             "answer": "Molte fonti considerano ottimale un HOMA-IR inferiore a 1,0. Valori superiori a 2,5–2,9 vengono spesso interpretati come indicativi di resistenza insulinica, ma le soglie variano in base a popolazione, età, sesso e metodo di laboratorio. Discutete sempre il risultato con il vostro medico."},
        ],
        "he": [
            {"question": "מהו HOMA-IR?",
             "answer": "HOMA-IR (Homeostatic Model Assessment for Insulin Resistance) הוא מדד מחושב שמעריך עמידות לאינסולין מרמות אינסולין וגלוקוז בצום. זהו כלי סינון, לא בדיקה אבחנתית, ויש לפרש אותו על ידי רופא בהקשר הקליני המלא."},
            {"question": "איך מחשבים HOMA-IR?",
             "answer": "מכפילים אינסולין בצום (μU/mL) בגלוקוז בצום (mg/dL) ומחלקים ב-405. אם הגלוקוז ב-mmol/L, מחלקים ב-22.5. שתי הנוסחאות נותנות אותה תוצאה."},
            {"question": "מהו ערך HOMA-IR תקין?",
             "answer": "מקורות רבים רואים ב-HOMA-IR מתחת ל-1.0 ערך אופטימלי. ערכים מעל 2.5–2.9 נחשבים לעיתים קרובות כמצביעים על עמידות לאינסולין, אך ערכי הסף משתנים לפי אוכלוסייה, גיל, מין ושיטת מעבדה. שוחחו תמיד עם הרופא."},
        ],
        "hi": [
            {"question": "HOMA-IR क्या है?",
             "answer": "HOMA-IR (Homeostatic Model Assessment for Insulin Resistance) एक कैलकुलेटेड इंडेक्स है जो फ़ास्टिंग इंसुलिन और फ़ास्टिंग ग्लूकोज़ से इंसुलिन रेज़िस्टेंस का अनुमान लगाता है। यह एक स्क्रीनिंग टूल है, डायग्नोस्टिक टेस्ट नहीं, और इसे डॉक्टर को क्लिनिकल संदर्भ में पढ़ना चाहिए।"},
            {"question": "HOMA-IR कैसे कैलकुलेट होता है?",
             "answer": "फ़ास्टिंग इंसुलिन (μU/mL) को फ़ास्टिंग ग्लूकोज़ (mg/dL) से गुणा करें और 405 से भाग दें। अगर ग्लूकोज़ mmol/L में है तो 22.5 से भाग दें। दोनों फ़ॉर्मूले एक ही रिज़ल्ट देते हैं।"},
            {"question": "सामान्य HOMA-IR वैल्यू क्या है?",
             "answer": "कई संदर्भों में 1.0 से कम HOMA-IR को बेहतरीन माना जाता है। 2.5–2.9 से ऊपर अक्सर इंसुलिन रेज़िस्टेंस का संकेत होता है, लेकिन कट-ऑफ़ जनसंख्या, उम्र, लिंग और लैब मेथड के अनुसार बदलते हैं। अपनी रिपोर्ट हमेशा डॉक्टर से दिखाएं।"},
        ],
        "ar": [
            {"question": "ما هو HOMA-IR؟",
             "answer": "HOMA-IR (تقييم النموذج الاستتبابي لمقاومة الأنسولين) هو مؤشر محسوب يُقدّر مقاومة الأنسولين من مستويات الأنسولين والغلوكوز الصائمين. هو أداة فحص وليس اختباراً تشخيصياً، ويجب أن يُفسّره الطبيب ضمن السياق السريري الكامل."},
            {"question": "كيف يُحسب HOMA-IR؟",
             "answer": "يُضرب الأنسولين الصائم (μU/mL) في الغلوكوز الصائم (mg/dL) ويُقسم على 405. إذا كان الغلوكوز بوحدة mmol/L يُقسم على 22.5. كلتا الصيغتين تعطيان النتيجة نفسها."},
            {"question": "ما القيمة الطبيعية لـ HOMA-IR؟",
             "answer": "تعتبر كثير من المراجع أن HOMA-IR أقل من 1.0 هو الأمثل. قيم فوق 2.5–2.9 غالباً تُشير إلى مقاومة الأنسولين، لكن نقاط القطع تختلف حسب السكان والعمر والجنس وطريقة المختبر. ناقش نتيجتك دائماً مع طبيبك."},
        ],
    }
