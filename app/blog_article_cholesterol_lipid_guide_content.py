"""Blog article for cholesterol & lipid panel intent."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what a lipid panel measures",
            body_html=(
                "<p>A <strong>lipid panel</strong> (also called a lipid profile or cholesterol test) is a group of blood tests that measure "
                "the fats circulating in your bloodstream. It typically includes <strong>total cholesterol</strong>, "
                "<strong>LDL cholesterol</strong>, <strong>HDL cholesterol</strong>, and <strong>triglycerides</strong>. "
                "From these values, clinicians often calculate <strong>non-HDL cholesterol</strong> and the "
                "<strong>total/HDL ratio</strong> to get a fuller picture of cardiovascular risk.</p>"
                "<p>Each marker tells a different part of the story. Understanding them together—rather than in "
                "isolation—is how most clinicians approach lipid interpretation.</p>"
            ),
        ),
        Section(
            id="total-cholesterol",
            level=2,
            heading="Total cholesterol explained",
            body_html=(
                "<p><strong>Total cholesterol</strong> is the sum of all cholesterol carried in your blood across different "
                "particle types, including LDL, HDL, and VLDL. It gives a broad overview but does not tell the whole story "
                "on its own.</p>"
                "<p>For many years, total cholesterol was the primary screening number. Today, clinicians use it as a starting "
                "point and then look at the individual components—especially LDL and HDL—to understand risk more precisely. "
                "A total cholesterol value that looks \"normal\" can still mask an unfavorable LDL/HDL balance, which is why "
                "the full panel matters.</p>"
                "<p>Total cholesterol is affected by diet, genetics, physical activity, medications, and underlying health conditions. "
                "Because it is a composite measure, changes in any one component will shift the total.</p>"
            ),
        ),
        Section(
            id="ldl-cholesterol",
            level=2,
            heading="LDL cholesterol: the \"bad\" cholesterol",
            body_html=(
                "<p><strong>LDL (low-density lipoprotein) cholesterol</strong> is often called the \"bad\" cholesterol because "
                "LDL particles can deposit cholesterol in artery walls, contributing to plaque buildup over time. "
                "This process, called atherosclerosis, is a key driver of cardiovascular disease.</p>"
                "<p>LDL cholesterol is usually the primary target when clinicians discuss lipid management. "
                "Lower LDL levels are generally associated with lower cardiovascular risk, though the ideal target "
                "depends on your overall risk profile, including factors like blood pressure, diabetes status, and family history.</p>"
                "<p>It is worth noting that LDL cholesterol measures the <em>amount of cholesterol</em> inside LDL particles, "
                "not the <em>number of particles</em> themselves. Some clinicians also look at ApoB (apolipoprotein B) or "
                "LDL particle number for a more detailed view, especially when LDL cholesterol and other markers disagree.</p>"
            ),
        ),
        Section(
            id="hdl-cholesterol",
            level=2,
            heading="HDL cholesterol: the \"good\" cholesterol",
            body_html=(
                "<p><strong>HDL (high-density lipoprotein) cholesterol</strong> is often called the \"good\" cholesterol because "
                "HDL particles help carry cholesterol away from arteries and back to the liver for processing and removal. "
                "This \"reverse cholesterol transport\" is one reason higher HDL is generally viewed favorably.</p>"
                "<p>However, the relationship between HDL and cardiovascular risk is more nuanced than once thought. "
                "Very high HDL levels do not automatically mean lower risk, and raising HDL with medication has not "
                "consistently improved outcomes in clinical trials. Most clinicians now focus on HDL as one piece of "
                "a broader lipid picture rather than a standalone treatment target.</p>"
                "<p>Regular physical activity, not smoking, and a diet rich in healthy fats are among the lifestyle factors "
                "most consistently associated with healthier HDL levels.</p>"
            ),
        ),
        Section(
            id="triglycerides",
            level=2,
            heading="Triglycerides explained",
            body_html=(
                "<p><strong>Triglycerides</strong> are the most common type of fat in your body. They store excess energy "
                "from your diet and are carried in the blood within VLDL (very-low-density lipoprotein) particles.</p>"
                "<p>Elevated triglycerides can be influenced by a range of factors including high intake of refined carbohydrates "
                "and sugars, excess alcohol consumption, obesity, insulin resistance, hypothyroidism, and certain medications. "
                "They are also sensitive to recent meals, which is why fasting is often recommended before a lipid panel.</p>"
                "<p>When triglycerides are very high, clinicians may also consider the risk of pancreatitis in addition to "
                "cardiovascular risk. Managing triglycerides often involves dietary changes, physical activity, and sometimes "
                "medication depending on the level and overall risk context.</p>"
            ),
        ),
        Section(
            id="non-hdl",
            level=2,
            heading="Non-HDL cholesterol",
            body_html=(
                "<p><strong>Non-HDL cholesterol</strong> is calculated by subtracting HDL cholesterol from total cholesterol. "
                "It represents all the cholesterol carried by particles that are not HDL—essentially LDL, VLDL, IDL, "
                "and other atherogenic particles combined.</p>"
                "<p>Many guidelines now consider non-HDL cholesterol a useful secondary target because it captures "
                "all cholesterol-containing particles that can contribute to plaque, not just LDL. "
                "It is easy to calculate from a standard lipid panel and does not require an additional test.</p>"
                "<p>Non-HDL cholesterol is particularly helpful when triglycerides are elevated, because in that situation "
                "calculated LDL cholesterol can be less accurate. Non-HDL remains reliable regardless of triglyceride level.</p>"
            ),
        ),
        Section(
            id="total-hdl-ratio",
            level=2,
            heading="Total/HDL cholesterol ratio",
            body_html=(
                "<p>The <strong>total cholesterol to HDL ratio</strong> is calculated by dividing total cholesterol by HDL cholesterol. "
                "It provides a quick snapshot of the balance between all cholesterol and the \"protective\" HDL fraction.</p>"
                "<p>A lower ratio is generally considered more favorable. For example, a ratio around 3.5–4.0 or below is often "
                "viewed as lower risk, while a ratio above 5.0 may prompt closer review. However, the ratio is a simplification "
                "and should not replace a detailed look at each individual marker.</p>"
                "<p>Some clinicians use the ratio as a quick screening tool, while others prefer to focus on absolute LDL and "
                "non-HDL values. Both approaches have merit, and the ratio is best understood as one additional lens "
                "rather than a definitive risk measure.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Who should get a lipid panel",
            body_html=(
                "<p>Lipid panels are one of the most commonly ordered blood tests. General guidance includes:</p>"
                "<ul>"
                "<li><strong>Adults aged 20 and older:</strong> most guidelines recommend a baseline lipid panel and periodic "
                "re-testing, with frequency depending on your results and risk factors.</li>"
                "<li><strong>People with cardiovascular risk factors:</strong> including high blood pressure, diabetes, "
                "smoking history, obesity, or a family history of early heart disease—may need more frequent monitoring.</li>"
                "<li><strong>People on lipid-lowering therapy:</strong> regular testing helps track whether treatment is "
                "achieving its targets.</li>"
                "<li><strong>Children and adolescents:</strong> screening may be recommended for those with a family history "
                "of high cholesterol or early cardiovascular disease, or with certain health conditions.</li>"
                "</ul>"
                "<p>Your clinician can advise on the right testing schedule for your situation. Fasting for 9–12 hours "
                "is often recommended, especially if triglycerides are a focus, though some guidelines accept non-fasting "
                "panels for routine screening.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevated: quick pattern guide",
            body_html=(
                "<div class=\"blog-example\"><strong>Favorable pattern:</strong> LDL in range, HDL at a healthy level, triglycerides not elevated, and non-HDL within expected bounds. This combination is generally associated with lower cardiovascular risk.</div>"
                "<div class=\"blog-example\"><strong>Mixed pattern:</strong> LDL moderately elevated with borderline triglycerides. Clinicians often review diet, activity level, metabolic health, and family history before deciding on next steps.</div>"
                "<div class=\"blog-example\"><strong>Elevated triglycerides with low HDL:</strong> a common pairing seen in insulin resistance and metabolic syndrome. This pattern often prompts a closer look at carbohydrate intake, weight management, and glucose markers.</div>"
                "<div class=\"blog-example\"><strong>Clearly elevated LDL:</strong> may lead to a more focused cardiovascular risk discussion, possibly including medication options alongside lifestyle changes.</div>"
                "<p>Remember: reference ranges vary by lab, and your clinician interprets your results in the context of your full health picture.</p>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="What to do next",
            body_html=(
                "<p>If you have recent lipid panel results and want a clear, structured explanation, you can "
                "<a href=\"/en/upload\">upload your blood test results</a> to get a personalized overview. "
                "Start with <a href=\"/en/blood-test-results-explained\">blood test results explained</a> for a helpful introduction, "
                "and then use the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a> to review the explanation together with your clinician.</p>"
                "<p>Understanding your cholesterol, triglycerides, and HDL together gives you a much clearer picture than any single number alone. "
                "Bring your results to your next appointment and discuss what they mean for your individual risk profile.</p>"
                "<p>This guide is educational only and does not replace a medical assessment.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This article is for information only.</strong> It does not provide medical advice, diagnosis, "
                "or treatment. Always discuss your results with a qualified clinician and follow their guidance.</p>"
            ),
        ),
    ]


def _sections_tr():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Kısa cevap: Lipid paneli neyi ölçer?",
            body_html=(
                "<p><strong>Lid paneli</strong> (lipid profili veya kolesterol testi olarak da bilinir), "
                "kan dolaşımınızdaki yağları ölçen bir grup kan testidir. Genellikle <strong>total kolesterol</strong>, "
                "<strong>LDL kolesterol</strong>, <strong>HDL kolesterol</strong> ve <strong>trigliserid</strong> değerlerini içerir. "
                "Bu değerlerden yola çıkarak klinisyenler genellikle <strong>non-HDL kolesterol</strong> ve "
                "<strong>total/HDL oranını</strong> hesaplayarak kardiyovasküler riski daha kapsamlı değerlendirir.</p>"
                "<p>Her belirteç hikâyenin farklı bir parçasını anlatır. Çoğu klinisyen lipid yorumlamasında "
                "bu belirteçleri tek tek değil, birlikte ele almayı tercih eder.</p>"
            ),
        ),
        Section(
            id="total-cholesterol",
            level=2,
            heading="Total kolesterol açıklaması",
            body_html=(
                "<p><strong>Total kolesterol</strong>, LDL, HDL ve VLDL dahil olmak üzere farklı partikül tiplerinde "
                "taşınan tüm kolesterolün toplamıdır. Geniş bir genel bakış sunar ancak tek başına tüm hikâyeyi anlatmaz.</p>"
                "<p>Uzun yıllar total kolesterol birincil tarama değeri olarak kullanıldı. Günümüzde klinisyenler bunu "
                "bir başlangıç noktası olarak alıyor ve riski daha hassas anlamak için özellikle LDL ve HDL gibi "
                "bireşenlere bakıyor. \"Normal\" görünen bir total kolesterol değeri bile elverişsiz bir LDL/HDL dengesini "
                "gizleyebilir; bu yüzden tam panel önemlidir.</p>"
                "<p>Total kolesterol; beslenme, genetik, fiziksel aktivite, ilaçlar ve altta yatan sağlık durumlarından "
                "etkilenir. Bileşik bir ölçüm olduğu için bileşenlerden herhangi birindeki değişiklik total değeri de değiştirir.</p>"
            ),
        ),
        Section(
            id="ldl-cholesterol",
            level=2,
            heading="LDL kolesterol: \"kötü\" kolesterol",
            body_html=(
                "<p><strong>LDL (düşük yoğunluklu lipoprotein) kolesterol</strong>, LDL partiküllerinin arter duvarlarında "
                "kolesterol biriktirerek zamanla plak oluşumuna katkıda bulunabilmesi nedeniyle genellikle \"kötü\" kolesterol "
                "olarak adlandırılır. Ateroskleroz adı verilen bu süreç, kardiyovasküler hastalığın temel nedenlerinden biridir.</p>"
                "<p>LDL kolesterol, klinisyenler lipid yönetimi hakkında konuştuğunda genellikle birincil hedeftir. "
                "Düşük LDL seviyeleri genellikle daha düşük kardiyovasküler riskle ilişkilendirilir ancak ideal hedef; "
                "kan basıncı, diyabet durumu ve aile öyküsü gibi genel risk profilinize bağlıdır.</p>"
                "<p>LDL kolesterolün LDL partiküllerinin <em>içindeki</em> kolesterol miktarını ölçtüğünü, "
                "partikül <em>sayısını</em> ölçmediğini belirtmek önemlidir. Bazı klinisyenler özellikle LDL kolesterol "
                "ile diğer belirteçler uyuşmadığında daha detaylı bir görünüm için ApoB (apolipoprotein B) veya "
                "LDL partikül sayısına da bakabilir.</p>"
            ),
        ),
        Section(
            id="hdl-cholesterol",
            level=2,
            heading="HDL kolesterol: \"iyi\" kolesterol",
            body_html=(
                "<p><strong>HDL (yüksek yoğunluklu lipoprotein) kolesterol</strong>, HDL partikülleri kolesterolü "
                "arterlerden alıp işlenmek ve atılmak üzere karaciğere taşıdığı için genellikle \"iyi\" kolesterol "
                "olarak adlandırılır. Bu \"ters kolesterol taşıma\" işlemi, yüksek HDL'nin genellikle olumlu "
                "karşılanmasının nedenlerinden biridir.</p>"
                "<p>Ancak HDL ile kardiyovasküler risk arasındaki ilişki bir zamanlar düşünüldüğünden daha karmaşıktır. "
                "Çok yüksek HDL seviyeleri otomatik olarak daha düşük risk anlamına gelmez ve ilaçlarla HDL'yi yükseltmek "
                "klinik deneylerde tutarlı şekilde sonuçları iyileştirmemiştir. Çoğu klinisyen artık HDL'yi bağımsız "
                "bir tedavi hedefinden ziyade daha geniş bir lipid resminin parçası olarak değerlendiriyor.</p>"
                "<p>Düzenli fiziksel aktivite, sigara kullanmamak ve sağlıklı yağlardan zengin beslenme, daha sağlıklı "
                "HDL seviyeleriyle en tutarlı şekilde ilişkilendirilen yaşam tarzı faktörleri arasındadır.</p>"
            ),
        ),
        Section(
            id="triglycerides",
            level=2,
            heading="Trigliserid açıklaması",
            body_html=(
                "<p><strong>Trigliseridler</strong> vücudunuzdaki en yaygın yağ türüdür. Diyetinizden alınan fazla "
                "enerjiyi depolarlar ve kanda VLDL (çok düşük yoğunluklu lipoprotein) partikülleri içinde taşınırlar.</p>"
                "<p>Yüksek trigliserid seviyeleri; rafine karbonhidrat ve şeker alımı, aşırı alkol tüketimi, obezite, "
                "insülin direnci, hipotiroidi ve bazı ilaçlar gibi çeşitli faktörlerden etkilenebilir. Ayrıca son "
                "yemeklere karşı hassastırlar; bu nedenle lipid paneli öncesinde genellikle açlık önerilir.</p>"
                "<p>Trigliseridler çok yüksek olduğunda klinisyenler kardiyovasküler riske ek olarak pankreatit riskini "
                "de değerlendirebilir. Trigliserid yönetimi genellikle diyet değişiklikleri, fizikaktivite ve "
                "seviyeye ve genel risk bağlamına bağlı olarak bazen ilaç tedavisini içerir.</p>"
            ),
        ),
        Section(
            id="non-hdl",
            level=2,
            heading="Non-HDL kolesterol",
            body_html=(
                "<p><strong>Non-HDL kolesterol</strong>, total kolesterolün HDL kolesterolün çıkarılmasıyla hesaplanır. "
                "HDL olmayan partiküller tarafından taşınan tüm kolesterolü temsil eder; yani LDL, VLDL, IDL ve "
                "diğer aterojenik partiküllerin toplamıdır.</p>"
                "<p>Birçok güncel kılavuz, non-HDL kolesterolü yararlı bir ikincil hedef olarak değerlendiriyor çünkü "
                "sadece LDL'yi değil, plağa katkıda bulunabilen tüm kolesterol içeren partikülleri kapsıyor. "
                "Standart bir lipid panelinden kolayca hesaplanabilir ve ek bir test gerektirmez.</p>"
                "<p>Non-HDL kolesterol özellikle trigliseridler yüksek olduğunda faydalıdır çünkü bu durumda "
                "hesaplanan LDL kolesterolü daha az doğru olabilir. Non-HDL ise trigliserid seviyesinden "
                "bağımsız olarak güvenilir kalır.</p>"
            ),
        ),
        Section(
            id="total-hdl-ratio",
            level=2,
            heading="Total/HDL kolesterol oranı",
            body_html=(
                "<p><strong>Total kolesterolün HDL kolesterolüne oranı</strong>, total kolesterolün HDL kolesterolüne "
                "bölünmesiyle hesaplanır. Tüm kolesterol ile \"koruyucu\" HDL fraksiyonu arasındaki dengenin hızlı "
                "bir özetini sunar.</p>"
                "<p>Daha düşük oran genellikle daha olumlu kabul edilir. Örneğin 3,5-4,0 veya altındaki bir oran "
                "daha düşük risk olarak değerlendirilirken, 5,0'ın üzerindeki bir oran daha yakından incelemeyi "
                "gerektirebilir. Ancak oran bir basitleştirmedir ve her bir belirtecin ayrıntılı incelemesinin "
                "yerini almamalıdır.</p>"
                "<p>Bazı klinisyenler oranı hızlı bir tarama aracı olarak kullanırken, diğerleri mutlak LDL ve "
                "non-HDL değerlerine odaklanmayı tercih eder. Her iki yaklaşımın da geçerliliği vardır ve oran "
                "kesin bir risk ölçüsü yerine ek bir bakış açısı olarak en iyi şekilde anlaşılır.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Kimler lipid paneli yaptırmalı?",
            body_html=(
                "<p>Lid panelleri en sık istenen kan testlerinden biridir. Genel öneriler şunları içerir:</p>"
                "<ul>"
                "<li><strong>20 yaş ve üzeri yetişkinler:</strong> çoğu kılavuz temel bir lipid paneli ve "
                "sonuçlarınıza ve risk faktörlerinize bağlı olarak periyodik tekrar testlerini önerir.</li>"
                "<li><strong>Kardiyovasküler risk faktörleri olan kişiler:</strong> yüksek tansiyon, diyabet, "
                "sigara öyküsü, obezite veya erken kalp hastalığı aile öyküsü gibi faktörleri olanlar daha sık "
                "izlem gerektirebilir.</li>"
                "<li><strong>Lipid düşürücü tedavi gören kişiler:</strong> düzenli test, tedavinin hedeflerine "
                "ulaşıp ulaşmadığını takip etmeye yardımcı olur.</li>"
                "<li><strong>Çocuklar ve ergenler:</strong> yüksek kolesterol veya erken kardiyovasküler hastalık "
                "aile öyküsü olanlarda veya belirli sağlık durumlarında tarama önerilebilir.</li>"
                "</ul>"
                "<p>Klinisyeniniz durumunuza uygun test takvimi konusunda tavsiyede bulunabilir. Özellikle trigliseridler "
                "odak noktasıysa 9-12 saat açlık genellikle önerilir, ancak bazı kılavuzlar rutin tarama için "
                "açlık olmayan panelleri de kabul etmektedir.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs yüksek: hızlı desen rehberi",
            body_html=(
                "<div class=\"blog-example\"><strong>Olumlu desen:</strong> LDL aralıkta, HDL sağlıklı seviyede, trigliseridler yüksek değil ve non-HDL beklenen sınırlar içinde. Bu kombinasyon genellikle daha düşük kardiyovasküler riskle ilişkilendirilir.</div>"
                "<div class=\"blog-example\"><strong>Karışık desen:</strong> LDL orta düzeyde yüksek, trigliseridler sınırda. Klinisyenler genellikle sonraki adımlara karar vermeden önce beslenme, aktivite düzeyi, metabolik sağlık ve aile öyküsünü gözden geçirir.</div>"
                "<div class=\"blog-example\"><strong>Yüksek trigliserid ve düşük HDL:</strong> insülin direnci ve metabolik sendromda sık görülen bir eşleşme. Bu desen genellikle karbonhidrat alımı, kilo yönetimi ve glukoz belirteçlerine daha yakından bakılmasını gerektirir.</div>"
                "<div class=\"blog-example\"><strong>Belirgin yüksek LDL:</strong> yaşam tarzı değişikliklerinin yanı sıra ilaç seçeneklerini de içerebilecek daha odaklı bir kardiyovasküler risk değerlendirmesine yol açabilir.</div>"
                "<p>Unutmayın: referans aralıkları laboratuvara göre değişir ve klinisyeniniz sonuçlarınızı tam sağlık resminizin bağlamında yorumlar.</p>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Sıradaki adımlar",
            body_html=(
                "<p>Son lipid paneli sonuçlarınız varsa ve net, yapılandırılmış bir açıklama isterseniz "
                "kişiselleştirilmiş bir genel bakış almak için <a href=\"/tr/upload\">kan tahlili sonuçlarınızı yükleyebilirsiniz</a>. "
                "Yararlı bir giriş için <a href=\"/tr/blood-test-results-explained\">blood test results explained</a> ile başlayın "
                "ve ardından açıklamayı klinisyeninizle birlikte gözden geçirmek için "
                "<a href=\"/tr/ai-blood-test-analyzer\">AI blood test analyzer</a>'ı kullanın.</p>"
                "<p>Kolesterol, trigliserid ve HDL'nizi birlikte anlamak, tek bir sayıdan çok daha net bir resim sunar. "
                "Sonuçlarınızı bir sonraki randevunuza getirin ve bireysel risk profiliniz için ne anlama geldiklerini tartışın.</p>"
                "<p>Bu rehber yalnızca bilgilendirme amaçlıdır; tıbbi değerlendirme yerine geçmez.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Yasal/Medikal uyarı",
            body_html=(
                "<p><strong>Bu içerik sadece bilgilendirme amaçlıdır.</strong> Tıbbi tavsiye, tanı veya tedavi sunmaz. "
                "Sonuçlarınızı mutlaka yetkin bir klinisyenle görüşün ve önerilerine uyun.</p>"
            ),
        ),
    ]


def _sections_de():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Kurz erklärt: Was misst ein Lipidprofil?",
            body_html=(
                "<p>Ein <strong>Lipidprofil</strong> (auch Blutfettwerte oder Cholesterintest genannt) ist eine Gruppe "
                "von Bluttests, die die Fette in Ihrem Blutkreislauf messen. Es umfasst in der Regel "
                "<strong>Gesamtcholesterin</strong>, <strong>LDL-Cholesterin</strong>, <strong>HDL-Cholesterin</strong> "
                "und <strong>Triglyceride</strong>. Aus diesen Werten berechnen Kliniker häufig "
                "<strong>Non-HDL-Cholesterin</strong> und das <strong>Gesamt-/HDL-Verhältnis</strong>, um ein "
                "umfassenderes Bild des kardiovaskulären Risikos zu erhalten.</p>"
                "<p>Jeder Marker erzählt einen anderen Teil der Geschichte. Die meisten Kliniker bewerten diese Werte "
                "gemeinsam statt isoliert, um das Lipidprofil richtig einzuordnen.</p>"
            ),
        ),
        Section(
            id="total-cholesterol",
            level=2,
            heading="Gesamtcholesterin erklärt",
            body_html=(
                "<p><strong>Gesamtcholesterin</strong> ist die Summe des gesamten Cholesterins, das in Ihrem Blut "
                "über verschiedene Partikeltypen transportiert wird, einschließlich LDL, HDL und VLDL. Es bietet "
                "einen groben Überblick, erzählt aber allein nicht die ganze Geschichte.</p>"
                "<p>Lange Jahre war das Gesamtcholesterin der primäre Screening-Wert. Heute nutzen Ärztinnen und Ärzte "
                "ihn als Ausgangspunkt und betrachten dann die einzelnen Komponenten – insbesondere LDL und HDL –, "
                "um das Risiko genauer zu verstehen. Ein „normal“ wirkender Gesamtcholesterinwert kann dennoch ein "
                "ungünstiges LDL/HDL-Verhältnis verdecken, weshalb das gesamte Profil wichtig ist.</p>"
                "<p>Gesamtcholesterin wird durch Ernährung, Genetik, körperliche Aktivität, Medikamente und "
                "zugrundeliegende Gesundheitszustände beeinflusst. Da es sich um einen zusammengesetzten Wert handelt, "
                "verändert jede Änderung einer Komponente auch das Gesamtcholesterin.</p>"
            ),
        ),
        Section(
            id="ldl-cholesterol",
            level=2,
            heading="LDL-Cholesterin: das „schlechte“ Cholesterin",
            body_html=(
                "<p><strong>LDL (Low-Density-Lipoprotein)-Cholesterin</strong> wird oft als „schlechtes“ Cholesterin "
                "bezeichnet, weil LDL-Partikel Cholesterin in Arterienwänden ablagern und so im Laufe der Zeit zur "
                "Plaquebildung beitragen können. Dieser als Atherosklerose bezeichnete Prozess ist ein Haupttreiber "
                "kardiovaskulärer Erkrankungen.</p>"
                "<p>LDL-Cholesterin ist meist der primäre Zielwert, wenn Kliniker über Lipidmanagement sprechen. "
                "Niedrigere LDL-Werte sind im Allgemeinen mit einem geringeren kardiovaskulären Risiko verbunden, "
                "wobei das ideale Ziel von Ihrem Gesamtrisikoprofil abhängt – einschließlich Blutdruck, "
                "Diabetesstatus und Familiengeschichte.</p>"
                "<p>Es ist wichtig zu beachten, dass LDL-Cholesterin die <em>Menge an Cholesterin</em> innerhalb "
                "der LDL-Partikel misst, nicht die <em>Anzahl der Partikel</em> selbst. Manche Kliniker schauen "
                "sich zusätzlich ApoB (Apolipoprotein B) oder die LDL-Partikelanzahl an, besonders wenn LDL-Cholesterin "
                "und andere Marker voneinander abweichen.</p>"
            ),
        ),
        Section(
            id="hdl-cholesterol",
            level=2,
            heading="HDL-Cholesterin: das „gute“ Cholesterin",
            body_html=(
                "<p><strong>HDL (High-Density-Lipoprotein)-Cholesterin</strong> wird oft als „gutes“ Cholesterin "
                "bezeichnet, weil HDL-Partikel dabei helfen, Cholesterin aus den Arterien zurück zur Leber zu "
                "transportieren, wo es verarbeitet und ausgeschieden wird. Dieser „reverse Cholesterintransport“ "
                "ist ein Grund, warum höheres HDL generell positiv bewertet wird.</p>"
                "<p>Allerdings ist die Beziehung zwischen HDL und kardiovaskulärem Risiko komplexer als früher "
                "angenommen. Sehr hohe HDL-Werte bedeuten nicht automatisch ein niedrigeres Risiko, und das "
                "Anheben von HDL mit Medikamenten hat in klinischen Studien nicht durchgängig zu besseren "
                "Ergebnissen geführt. Die meisten Kliniker betrachten HDL heute als Teil eines größeren "
                "Lipidbildes statt als eigenständiges Behandlungsziel.</p>"
                "<p>Regelmäßige körperliche Aktivität, Nichtrauchen und eine Ernährung mit gesunden Fetten gehören "
                "zu den Lebensstilfaktoren, die am konsistentesten mit gesünderen HDL-Werten verbunden sind.</p>"
            ),
        ),
        Section(
            id="triglycerides",
            level=2,
            heading="Triglyceride erklärt",
            body_html=(
                "<p><strong>Triglyceride</strong> sind die häufigste Fettart in Ihrem Körper. Sie speichern "
                "überschüssige Energie aus Ihrer Ernährung und werden im Blut in VLDL-Partikeln (Very-Low-Density-"
                "Lipoprotein) transportiert.</p>"
                "<p>Erhöhte Triglyceride können durch verschiedene Faktoren beeinflusst werden, darunter hoher "
                "Konsum von raffinierten Kohlenhydraten und Zucker, übermäßiger Alkoholkonsum, Adipositas, "
                "Insulinresistenz, Schilddrüsenunterfunktion und bestimmte Medikamente. Sie reagieren auch "
                "empfindlich auf kürzliche Mahlzeiten, weshalb vor einem Lipidprofil oft Fasten empfohlen wird.</p>"
                "<p>Wenn die Triglyceride sehr hoch sind, können Kliniker zusätzlich zum kardiovaskulären Risiko "
                "auch das Pankreatitis-Risiko berücksichtigen. Das Management umfasst oft Ernährungsumstellung, "
                "körperliche Aktivität und je nach Wert und Gesamtrisikokontext manchmal auch Medikamente.</p>"
            ),
        ),
        Section(
            id="non-hdl",
            level=2,
            heading="Non-HDL-Cholesterin",
            body_html=(
                "<p><strong>Non-HDL-Cholesterin</strong> wird berechnet, indem HDL-Cholesterin vom Gesamtcholesterin "
                "abgezogen wird. Es repräsentiert das gesamte Cholesterin, das von Nicht-HDL-Partikeln getragen "
                "wird – also LDL, VLDL, IDL und andere atherogene Partikel zusammengefasst.</p>"
                "<p>Viele aktuelle Leitlinien betrachten Non-HDL-Cholesterin als nützliches sekundäres Ziel, "
                "da es alle cholesterinhaltigen Partikel erfasst, die zur Plaquebildung beitragen können, "
                "nicht nur LDL. Es lässt sich einfach aus einem Standard-Lipidprofil berechnen und erfordert "
                "keinen zusätzlichen Test.</p>"
                "<p>Non-HDL-Cholesterin ist besonders hilfreich, wenn die Triglyceride erhöht sind, da in dieser "
                "Situation das berechnete LDL-Cholesterin weniger genau sein kann. Non-HDL bleibt unabhängig "
                "vom Triglyceridspiegel zuverlässig.</p>"
            ),
        ),
        Section(
            id="total-hdl-ratio",
            level=2,
            heading="Gesamt-/HDL-Cholesterin-Verhältnis",
            body_html=(
                "<p>Das <strong>Gesamtcholesterin-zu-HDL-Verhältnis</strong> wird berechnet, indem das "
                "Gesamtcholesterin durch das HDL-Cholesterin geteilt wird. Es bietet eine schnelle Übersicht "
                "über die Balance zwischen dem gesamten Cholesterin und der „schützenden“ HDL-Fraktion.</p>"
                "<p>Ein niedrigeres Verhältnis gilt allgemein als günstiger. Ein Verhältnis von etwa 3,5–4,0 "
                "oder darunter wird oft als niedrigeres Risiko bewertet, während ein Verhältnis über 5,0 eine "
                "genauere Prüfung veranlassen kann. Das Verhältnis ist jedoch eine Vereinfachung und sollte "
                "nicht den detaillierten Blick auf jeden einzelnen Marker ersetzen.</p>"
                "<p>Manche Kliniker nutzen das Verhältnis als schnelles Screening-Instrument, andere bevorzugen "
                "absolute LDL- und Non-HDL-Werte. Beide Ansätze haben ihre Berechtigung, und das Verhältnis "
                "ist am besten als zusätzliche Perspektive zu verstehen, nicht als alleiniges Risikomaß.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Wer sollte ein Lipidprofil durchführen lassen?",
            body_html=(
                "<p>Lipidprofile gehören zu den am häufigsten angeordneten Bluttests. Allgemeine Empfehlungen "
                "umfassen:</p>"
                "<ul>"
                "<li><strong>Erwachsene ab 20 Jahren:</strong> Die meisten Leitlinien empfehlen ein Basis-Lipidprofil "
                "und regelmäßige Wiederholungen, abhängig von Ihren Werten und Risikofaktoren.</li>"
                "<li><strong>Personen mit kardiovaskulären Risikofaktoren:</strong> einschließlich Bluthochdruck, "
                "Diabetes, Rauchergeschichte, Adipositas oder familiärer Vorgeschichte von früher Herzkrankheit – "
                "können häufigere Kontrollen benötigen.</li>"
                "<li><strong>Personen unter lipidsenkender Therapie:</strong> Regelmäßige Tests helfen zu verfolgen, "
                "ob die Behandlung ihre Ziele erreicht.</li>"
                "<li><strong>Kinder und Jugendliche:</strong> Ein Screening kann bei familiärer Vorgeschichte von "
                "hohem Cholesterin oder früher kardiovaskulärer Erkrankung oder bei bestimmten Gesundheitszuständen "
                "empfohlen werden.</li>"
                "</ul>"
                "<p>Ihre Ärztin/Ihr Arzt kann den richtigen Testzeitplan für Ihre Situation empfehlen. "
                "9–12 Stunden Fasten wird oft empfohlen, besonders wenn Triglyceride im Fokus stehen, "
                "obwohl einige Leitlinien auch nicht-nüchterne Profile für das Routine-Screening akzeptieren.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs. erhöht: schnelle Orientierung",
            body_html=(
                "<div class=\"blog-example\"><strong>Günstiges Muster:</strong> LDL im Bereich, HDL auf gesundem Niveau, Triglyceride nicht erhöht und Non-HDL innerhalb der erwarteten Grenzen. Diese Kombination wird im Allgemeinen mit einem niedrigeren kardiovaskulären Risiko verbunden.</div>"
                "<div class=\"blog-example\"><strong>Gemischtes Muster:</strong> LDL mäßig erhöht mit grenzwertigen Triglyceriden. Kliniker prüfen oft Ernährung, Aktivitätsniveau, metabolische Gesundheit und Familiengeschichte, bevor sie nächste Schritte entscheiden.</div>"
                "<div class=\"blog-example\"><strong>Erhöhte Triglyceride mit niedrigem HDL:</strong> eine häufige Kombination bei Insulinresistenz und metabolischem Syndrom. Dieses Muster veranlasst oft einen genaueren Blick auf Kohlenhydratzufuhr, Gewichtsmanagement und Glukosemarker.</div>"
                "<div class=\"blog-example\"><strong>Deutlich erhöhtes LDL:</strong> kann zu einer fokussierteren kardiovaskulären Risikobesprechung führen, möglicherweise einschließlich Medikamentenoptionen neben Lebensstiländerungen.</div>"
                "<p>Beachten Sie: Referenzbereiche variieren je nach Labor, und Ihre Ärztin/Ihr Arzt interpretiert Ihre Werte im Kontext Ihres gesamten Gesundheitsbildes.</p>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Was als Nächstes tun",
            body_html=(
                "<p>Wenn Sie aktuelle Lipidwerte haben und eine klare, strukturierte Erklärung möchten, können Sie "
                "<a href=\"/de/upload\">Ihre Bluttest-Ergebnisse hochladen</a>, um eine personalisierte Übersicht zu erhalten. "
                "Beginnen Sie mit <a href=\"/de/blood-test-results-explained\">blood test results explained</a> für eine hilfreiche Einführung "
                "und nutzen Sie dann den <a href=\"/de/ai-blood-test-analyzer\">AI blood test analyzer</a>, um die Erklärung "
                "gemeinsam mit Ihrer Ärztin/Ihrem Arzt durchzugehen.</p>"
                "<p>Cholesterin, Triglyceride und HDL zusammen zu verstehen, gibt Ihnen ein viel klareres Bild als "
                "jede einzelne Zahl für sich. Bringen Sie Ihre Ergebnisse zum nächsten Termin und besprechen Sie, "
                "was sie für Ihr individuelles Risikoprofil bedeuten.</p>"
                "<p>Dieser Leitfaden ist nur zur Information gedacht und ersetzt keine medizinische Beurteilung.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Hinweis",
            body_html=(
                "<p><strong>Dieser Artikel dient nur der Information.</strong> Er ersetzt keine medizinische Beratung, "
                "keine Diagnose und keine Behandlung. Besprechen Sie Ihre Ergebnisse immer mit einer qualifizierten Fachperson.</p>"
            ),
        ),
    ]


def _sections_es():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Respuesta rápida: ¿qué mide un perfil lipídico?",
            body_html=(
                "<p>Un <strong>perfil lipídico</strong> (también llamado perfil de colesterol o prueba de colesterol) "
                "es un grupo de análisis de sangre que miden las grasas que circulan en el torrente sanguíneo. "
                "Normalmente incluye <strong>colesterol total</strong>, <strong>colesterol LDL</strong>, "
                "<strong>colesterol HDL</strong> y <strong>triglicéridos</strong>. A partir de estos valores, "
                "los profesionales suelen calcular el <strong>colesterol no-HDL</strong> y la "
                "<strong>relación colesterol total/HDL</strong> para obtener una visión más completa del riesgo cardiovascular.</p>"
                "<p>Cada marcador cuenta una parte distinta de la historia. La mayoría de los profesionales interpretan "
                "estos valores en conjunto, no de forma aislada.</p>"
            ),
        ),
        Section(
            id="total-cholesterol",
            level=2,
            heading="Colesterol total explicado",
            body_html=(
                "<p>El <strong>colesterol total</strong> es la suma de todo el colesterol transportado en la sangre "
                "a través de distintos tipos de partículas, incluidas LDL, HDL y VLDL. Ofrece una visión general "
                "pero no cuenta toda la historia por sí solo.</p>"
                "<p>Durante muchos años, el colesterol total fue el principal valor de cribado. Hoy en día, los "
                "profesionales lo usan como punto de partida y luego examinan los componentes individuales, "
                "especialmente LDL y HDL, para comprender el riesgo con mayor precisión. Un valor de colesterol "
                "total que parece «normal» puede ocultar un equilibrio desfavorable entre LDL y HDL, por eso "
                "es importante el panel completo.</p>"
                "<p>El colesterol total se ve afectado por la dieta, la genética, la actividad física, los medicamentos "
                "y las condiciones de salud subyacentes. Al ser una medida compuesta, cualquier cambio en uno de sus "
                "componentes modifica el total.</p>"
            ),
        ),
        Section(
            id="ldl-cholesterol",
            level=2,
            heading="Colesterol LDL: el colesterol «malo»",
            body_html=(
                "<p>El <strong>colesterol LDL (lipoproteína de baja densidad)</strong> se suele llamar colesterol «malo» "
                "porque las partículas LDL pueden depositar colesterol en las paredes arteriales, contribuyendo con el "
                "tiempo a la formación de placa. Este proceso, llamado aterosclerosis, es un motor clave de la "
                "enfermedad cardiovascular.</p>"
                "<p>El colesterol LDL suele ser el objetivo principal cuando los profesionales hablan de gestión lipídica. "
                "Niveles más bajos de LDL se asocian generalmente con un menor riesgo cardiovascular, aunque el objetivo "
                "ideal depende del perfil de riesgo general, incluyendo factores como la presión arterial, el estado de "
                "diabetes y los antecedentes familiares.</p>"
                "<p>Cabe señalar que el colesterol LDL mide la <em>cantidad de colesterol</em> dentro de las partículas "
                "LDL, no el <em>número de partículas</em> en sí. Algunos profesionales también observan la ApoB "
                "(apolipoproteína B) o el número de partículas LDL para una visión más detallada, especialmente cuando "
                "el colesterol LDL y otros marcadores no coinciden.</p>"
            ),
        ),
        Section(
            id="hdl-cholesterol",
            level=2,
            heading="Colesterol HDL: el colesterol «bueno»",
            body_html=(
                "<p>El <strong>colesterol HDL (lipoproteína de alta densidad)</strong> se suele llamar colesterol «bueno» "
                "porque las partículas HDL ayudan a transportar el colesterol desde las arterias de vuelta al hígado "
                "para su procesamiento y eliminación. Este «transporte reverso de colesterol» es una de las razones "
                "por las que un HDL más alto se considera generalmente favorable.</p>"
                "<p>Sin embargo, la relación entre HDL y riesgo cardiovascular es más matizada de lo que se pensaba. "
                "Niveles muy altos de HDL no significan automáticamente un menor riesgo, y elevar el HDL con "
                "medicamentos no ha mejorado consistentemente los resultados en ensayos clínicos. La mayoría de los "
                "profesionales ahora consideran el HDL como una pieza de un panorama lipídico más amplio en lugar de "
                "un objetivo de tratamiento independiente.</p>"
                "<p>La actividad física regular, no fumar y una dieta rica en grasas saludables están entre los factores "
                "de estilo de vida más consistentemente asociados con niveles más saludables de HDL.</p>"
            ),
        ),
        Section(
            id="triglycerides",
            level=2,
            heading="Triglicéridos explicados",
            body_html=(
                "<p>Los <strong>triglicéridos</strong> son el tipo de grasa más común en el cuerpo. Almacenan el exceso "
                "de energía de la dieta y se transportan en la sangre dentro de partículas VLDL (lipoproteína de muy "
                "baja densidad).</p>"
                "<p>Los triglicéridos elevados pueden estar influenciados por diversos factores, como un alto consumo de "
                "carbohidratos refinados y azúcares, consumo excesivo de alcohol, obesidad, resistencia a la insulina, "
                "hipotiroidismo y ciertos medicamentos. También son sensibles a las comidas recientes, por lo que "
                "normalmente se recomienda ayunar antes de un perfil lipídico.</p>"
                "<p>Cuando los triglicéridos son muy altos, los profesionales pueden considerar el riesgo de pancreatitis "
                "además del riesgo cardiovascular. El manejo suele incluir cambios dietéticos, actividad física y, "
                "dependiendo del nivel y el contexto de riesgo general, a veces medicación.</p>"
            ),
        ),
        Section(
            id="non-hdl",
            level=2,
            heading="Colesterol no-HDL",
            body_html=(
                "<p>El <strong>colesterol no-HDL</strong> se calcula restando el colesterol HDL del colesterol total. "
                "Representa todo el colesterol transportado por partículas que no son HDL: esencialmente LDL, VLDL, "
                "IDL y otras partículas aterogénicas combinadas.</p>"
                "<p>Muchas guías actuales consideran el colesterol no-HDL un objetivo secundario útil porque captura "
                "todas las partículas que contienen colesterol y pueden contribuir a la placa, no solo las LDL. "
                "Se calcula fácilmente a partir de un perfil lipídico estándar y no requiere una prueba adicional.</p>"
                "<p>El colesterol no-HDL es particularmente útil cuando los triglicéridos están elevados, ya que en esa "
                "situación el colesterol LDL calculado puede ser menos preciso. El no-HDL se mantiene fiable "
                "independientemente del nivel de triglicéridos.</p>"
            ),
        ),
        Section(
            id="total-hdl-ratio",
            level=2,
            heading="Relación colesterol total/HDL",
            body_html=(
                "<p>La <strong>relación colesterol total/HDL</strong> se calcula dividiendo el colesterol total entre "
                "el colesterol HDL. Proporciona una instantánea rápida del equilibrio entre todo el colesterol y la "
                "fracción HDL «protectora».</p>"
                "<p>Una relación más baja se considera generalmente más favorable. Por ejemplo, una relación de "
                "aproximadamente 3,5–4,0 o inferior se suele considerar de menor riesgo, mientras que una relación "
                "superior a 5,0 puede motivar una revisión más detallada. Sin embargo, la relación es una simplificación "
                "y no debe sustituir una mirada detallada a cada marcador individual.</p>"
                "<p>Algunos profesionales usan la relación como herramienta de cribado rápido, mientras que otros "
                "prefieren centrarse en los valores absolutos de LDL y no-HDL. Ambos enfoques tienen validez, y la "
                "relación se entiende mejor como una lente adicional más que como una medida definitiva de riesgo.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="¿Quién debería hacerse un perfil lipídico?",
            body_html=(
                "<p>Los perfiles lipídicos son uno de los análisis de sangre más solicitados. Las recomendaciones "
                "generales incluyen:</p>"
                "<ul>"
                "<li><strong>Adultos de 20 años o más:</strong> la mayoría de las guías recomiendan un perfil lipídico "
                "inicial y pruebas periódicas, con frecuencia según los resultados y los factores de riesgo.</li>"
                "<li><strong>Personas con factores de riesgo cardiovascular:</strong> incluyendo presión arterial alta, "
                "diabetes, tabaquismo, obesidad o antecedentes familiares de enfermedad cardíaca temprana, pueden "
                "necesitar un seguimiento más frecuente.</li>"
                "<li><strong>Personas en tratamiento hipolipemiante:</strong> las pruebas regulares ayudan a verificar "
                "si el tratamiento está alcanzando sus objetivos.</li>"
                "<li><strong>Niños y adolescentes:</strong> puede recomendarse un cribado para aquellos con antecedentes "
                "familiares de colesterol alto o enfermedad cardiovascular temprana, o con ciertas condiciones de salud.</li>"
                "</ul>"
                "<p>Su profesional puede aconsejar sobre el calendario de pruebas adecuado para su situación. Se recomienda "
                "ayuno de 9 a 12 horas, especialmente si los triglicéridos son el foco, aunque algunas guías aceptan "
                "paneles sin ayuno para el cribado rutinario.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevado: guía rápida de patrones",
            body_html=(
                "<div class=\"blog-example\"><strong>Patrón favorable:</strong> LDL en rango, HDL en nivel saludable, triglicéridos no elevados y no-HDL dentro de los límites esperados. Esta combinación se asocia generalmente con un menor riesgo cardiovascular.</div>"
                "<div class=\"blog-example\"><strong>Patrón mixto:</strong> LDL moderadamente elevado con triglicéridos en el límite. Los profesionales suelen revisar la dieta, el nivel de actividad, la salud metabólica y los antecedentes familiares antes de decidir los siguientes pasos.</div>"
                "<div class=\"blog-example\"><strong>Triglicéridos elevados con HDL bajo:</strong> una combinación frecuente en resistencia a la insulina y síndrome metabólico. Este patrón suele motivar una mirada más atenta al consumo de carbohidratos, la gestión del peso y los marcadores de glucosa.</div>"
                "<div class=\"blog-example\"><strong>LDL claramente elevado:</strong> puede llevar a una discusión más centrada sobre el riesgo cardiovascular, posiblemente incluyendo opciones de medicación junto con cambios en el estilo de vida.</div>"
                "<p>Recuerde: los rangos de referencia varían según el laboratorio, y su profesional interpreta sus resultados en el contexto de su panorama de salud completo.</p>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Qué hacer después",
            body_html=(
                "<p>Si tiene resultados recientes de un perfil lipídico y desea una explicación clara y estructurada, "
                "puede <a href=\"/es/upload\">subir sus resultados de análisis de sangre</a> para obtener una visión "
                "personalizada. Comience con <a href=\"/es/blood-test-results-explained\">blood test results explained</a> "
                "para una introducción útil y luego use el <a href=\"/es/ai-blood-test-analyzer\">AI blood test analyzer</a> "
                "para revisar la explicación junto con su profesional de salud.</p>"
                "<p>Entender su colesterol, triglicéridos y HDL en conjunto le da una imagen mucho más clara que "
                "cualquier número individual. Lleve sus resultados a su próxima cita y discuta qué significan para "
                "su perfil de riesgo individual.</p>"
                "<p>Esta guía es solo educativa y no sustituye la evaluación médica.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Aviso",
            body_html=(
                "<p><strong>Este artículo es solo para fines informativos.</strong> No ofrece consejo médico, diagnóstico ni tratamiento. "
                "Hable siempre sus resultados con un profesional cualificado.</p>"
            ),
        ),
    ]


def _sections_fr():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Réponse rapide : que mesure un bilan lipidique ?",
            body_html=(
                "<p>Un <strong>bilan lipidique</strong> (aussi appelé profil lipidique ou test de cholestérol) est un "
                "groupe d'analyses sanguines qui mesurent les graisses circulant dans votre sang. Il comprend "
                "généralement le <strong>cholestérol total</strong>, le <strong>cholestérol LDL</strong>, "
                "le <strong>cholestérol HDL</strong> et les <strong>triglycérides</strong>. À partir de ces valeurs, "
                "les cliniciens calculent souvent le <strong>cholestérol non-HDL</strong> et le "
                "<strong>rapport cholestérol total/HDL</strong> pour obtenir une image plus complète du risque cardiovasculaire.</p>"
                "<p>Chaque marqueur raconte une partie différente de l'histoire. La plupart des cliniciens interprètent "
                "ces valeurs ensemble plutôt que de manière isolée.</p>"
            ),
        ),
        Section(
            id="total-cholesterol",
            level=2,
            heading="Cholestérol total expliqué",
            body_html=(
                "<p>Le <strong>cholestérol total</strong> est la somme de tout le cholestérol transporté dans le sang "
                "par différents types de particules, y compris LDL, HDL et VLDL. Il donne une vue d'ensemble mais "
                "ne raconte pas toute l'histoire à lui seul.</p>"
                "<p>Pendant de nombreuses années, le cholestérol total a été la principale valeur de dépistage. "
                "Aujourd'hui, les cliniciens l'utilisent comme point de départ puis examinent les composants "
                "individuels – en particulier le LDL et le HDL – pour comprendre le risque plus précisément. "
                "Une valeur de cholestérol total qui semble « normale » peut masquer un déséquilibre défavorable "
                "entre LDL et HDL, d'où l'importance du bilan complet.</p>"
                "<p>Le cholestérol total est influencé par l'alimentation, la génétique, l'activité physique, les "
                "médicaments et les problèmes de santé sous-jacents. Comme il s'agit d'une mesure composite, "
                "tout changement dans l'un de ses composants modifie le total.</p>"
            ),
        ),
        Section(
            id="ldl-cholesterol",
            level=2,
            heading="Cholestérol LDL : le « mauvais » cholestérol",
            body_html=(
                "<p>Le <strong>cholestérol LDL (lipoprotéine de basse densité)</strong> est souvent appelé le « mauvais » "
                "cholestérol car les particules LDL peuvent déposer du cholestérol dans les parois artérielles, "
                "contribuant au fil du temps à la formation de plaques. Ce processus, appelé athérosclérose, est un "
                "facteur clé des maladies cardiovasculaires.</p>"
                "<p>Le cholestérol LDL est généralement la cible principale lorsque les cliniciens discutent de la "
                "gestion lipidique. Des niveaux plus bas de LDL sont généralement associés à un risque cardiovasculaire "
                "plus faible, bien que l'objectif idéal dépende de votre profil de risque global, y compris des facteurs "
                "comme la tension artérielle, le statut diabétique et les antécédents familiaux.</p>"
                "<p>Il est important de noter que le cholestérol LDL mesure la <em>quantité de cholestérol</em> à "
                "l'intérieur des particules LDL, pas le <em>nombre de particules</em> elles-mêmes. Certains cliniciens "
                "examinent également l'ApoB (apolipoprotéine B) ou le nombre de particules LDL pour une vue plus "
                "détaillée, surtout quand le cholestérol LDL et d'autres marqueurs ne concordent pas.</p>"
            ),
        ),
        Section(
            id="hdl-cholesterol",
            level=2,
            heading="Cholestérol HDL : le « bon » cholestérol",
            body_html=(
                "<p>Le <strong>cholestérol HDL (lipoprotéine de haute densité)</strong> est souvent appelé le « bon » "
                "cholestérol car les particules HDL aident à transporter le cholestérol des artères vers le foie pour "
                "son traitement et son élimination. Ce « transport inverse du cholestérol » est l'une des raisons pour "
                "lesquelles un HDL plus élevé est généralement considéré comme favorable.</p>"
                "<p>Cependant, la relation entre le HDL et le risque cardiovasculaire est plus nuancée qu'on ne le "
                "pensait. Des niveaux très élevés de HDL ne signifient pas automatiquement un risque plus faible, et "
                "augmenter le HDL avec des médicaments n'a pas systématiquement amélioré les résultats dans les essais "
                "cliniques. La plupart des cliniciens considèrent désormais le HDL comme une pièce d'un tableau lipidique "
                "plus large plutôt que comme une cible de traitement autonome.</p>"
                "<p>L'activité physique régulière, le fait de ne pas fumer et une alimentation riche en graisses saines "
                "font partie des facteurs de mode de vie les plus régulièrement associés à des niveaux de HDL plus sains.</p>"
            ),
        ),
        Section(
            id="triglycerides",
            level=2,
            heading="Triglycérides expliqués",
            body_html=(
                "<p>Les <strong>triglycérides</strong> sont le type de graisse le plus courant dans votre corps. Ils "
                "stockent l'excès d'énergie provenant de votre alimentation et sont transportés dans le sang au sein "
                "de particules VLDL (lipoprotéine de très basse densité).</p>"
                "<p>Des triglycérides élevés peuvent être influencés par divers facteurs, notamment une consommation "
                "élevée de glucides raffinés et de sucres, une consommation excessive d'alcool, l'obésité, la résistance "
                "à l'insuline, l'hypothyroïdie et certains médicaments. Ils sont également sensibles aux repas récents, "
                "c'est pourquoi le jeûne est souvent recommandé avant un bilan lipidique.</p>"
                "<p>Lorsque les triglycérides sont très élevés, les cliniciens peuvent également considérer le risque "
                "de pancréatite en plus du risque cardiovasculaire. La prise en charge implique souvent des changements "
                "alimentaires, de l'activité physique et parfois des médicaments selon le niveau et le contexte de risque global.</p>"
            ),
        ),
        Section(
            id="non-hdl",
            level=2,
            heading="Cholestérol non-HDL",
            body_html=(
                "<p>Le <strong>cholestérol non-HDL</strong> est calculé en soustrayant le cholestérol HDL du cholestérol "
                "total. Il représente tout le cholestérol transporté par des particules autres que le HDL – essentiellement "
                "LDL, VLDL, IDL et d'autres particules athérogènes combinées.</p>"
                "<p>De nombreuses lignes directrices considèrent désormais le cholestérol non-HDL comme une cible "
                "secondaire utile car il capture toutes les particules contenant du cholestérol pouvant contribuer à la "
                "plaque, pas seulement les LDL. Il se calcule facilement à partir d'un bilan lipidique standard et ne "
                "nécessite pas de test supplémentaire.</p>"
                "<p>Le cholestérol non-HDL est particulièrement utile lorsque les triglycérides sont élevés, car dans "
                "cette situation le cholestérol LDL calculé peut être moins précis. Le non-HDL reste fiable "
                "indépendamment du niveau de triglycérides.</p>"
            ),
        ),
        Section(
            id="total-hdl-ratio",
            level=2,
            heading="Rapport cholestérol total/HDL",
            body_html=(
                "<p>Le <strong>rapport cholestérol total/HDL</strong> est calculé en divisant le cholestérol total par "
                "le cholestérol HDL. Il offre un aperçu rapide de l'équilibre entre l'ensemble du cholestérol et la "
                "fraction HDL « protectrice ».</p>"
                "<p>Un rapport plus bas est généralement considéré comme plus favorable. Par exemple, un rapport "
                "d'environ 3,5 à 4,0 ou moins est souvent considéré comme un risque plus faible, tandis qu'un rapport "
                "supérieur à 5,0 peut justifier un examen plus approfondi. Cependant, le rapport est une simplification "
                "et ne doit pas remplacer un examen détaillé de chaque marqueur individuel.</p>"
                "<p>Certains cliniciens utilisent le rapport comme outil de dépistage rapide, tandis que d'autres "
                "préfèrent se concentrer sur les valeurs absolues de LDL et de non-HDL. Les deux approches sont "
                "valables, et le rapport se comprend mieux comme une perspective supplémentaire plutôt que comme "
                "une mesure définitive du risque.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Qui devrait faire un bilan lipidique ?",
            body_html=(
                "<p>Les bilans lipidiques font partie des analyses sanguines les plus prescrites. Les recommandations "
                "générales incluent :</p>"
                "<ul>"
                "<li><strong>Adultes de 20 ans et plus :</strong> la plupart des lignes directrices recommandent un bilan "
                "lipidique de base et des tests périodiques, avec une fréquence dépendant de vos résultats et facteurs de risque.</li>"
                "<li><strong>Personnes avec des facteurs de risque cardiovasculaire :</strong> incluant hypertension, "
                "diabète, tabagisme, obésité ou antécédents familiaux de maladie cardiaque précoce – peuvent nécessiter "
                "un suivi plus fréquent.</li>"
                "<li><strong>Personnes sous traitement hypolipémiant :</strong> des tests réguliers aident à vérifier "
                "si le traitement atteint ses objectifs.</li>"
                "<li><strong>Enfants et adolescents :</strong> un dépistage peut être recommandé pour ceux ayant des "
                "antécédents familiaux de cholestérol élevé ou de maladie cardiovasculaire précoce, ou certaines "
                "conditions de santé.</li>"
                "</ul>"
                "<p>Votre clinicien peut conseiller le calendrier de tests adapté à votre situation. Un jeûne de 9 à "
                "12 heures est souvent recommandé, surtout si les triglycérides sont au centre de l'attention, bien que "
                "certaines lignes directrices acceptent des bilans à jeun pour le dépistage de routine.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs élevé : repères rapides",
            body_html=(
                "<div class=\"blog-example\"><strong>Profil favorable :</strong> LDL dans la norme, HDL à un niveau sain, triglycérides non élevés et non-HDL dans les limites attendues. Cette combinaison est généralement associée à un risque cardiovasculaire plus faible.</div>"
                "<div class=\"blog-example\"><strong>Profil mixte :</strong> LDL modérément élevé avec des triglycérides limites. Les cliniciens examinent souvent l'alimentation, le niveau d'activité, la santé métabolique et les antécédents familiaux avant de décider des prochaines étapes.</div>"
                "<div class=\"blog-example\"><strong>Triglycérides élevés avec HDL bas :</strong> une combinaison fréquente dans la résistance à l'insuline et le syndrome métabolique. Ce profil motive souvent un regard plus attentif sur l'apport en glucides, la gestion du poids et les marqueurs de glucose.</div>"
                "<div class=\"blog-example\"><strong>LDL clairement élevé :</strong> peut mener à une discussion plus ciblée sur le risque cardiovasculaire, incluant éventuellement des options médicamenteuses en plus des changements de mode de vie.</div>"
                "<p>Rappelez-vous : les plages de référence varient selon le laboratoire, et votre clinicien interprète vos résultats dans le contexte de votre tableau de santé complet.</p>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Et ensuite",
            body_html=(
                "<p>Si vous avez des résultats lipidiques récents et souhaitez une explication claire et structurée, "
                "vous pouvez <a href=\"/fr/upload\">téléverser vos résultats d'analyses sanguines</a> pour obtenir un "
                "aperçu personnalisé. Commencez par <a href=\"/fr/blood-test-results-explained\">blood test results explained</a> "
                "pour une introduction utile, puis utilisez l'<a href=\"/fr/ai-blood-test-analyzer\">AI blood test analyzer</a> "
                "pour revoir l'explication avec votre clinicien.</p>"
                "<p>Comprendre votre cholestérol, vos triglycérides et votre HDL ensemble vous donne une image bien "
                "plus claire que n'importe quel chiffre isolé. Apportez vos résultats à votre prochain rendez-vous et "
                "discutez de ce qu'ils signifient pour votre profil de risque individuel.</p>"
                "<p>Ce guide est éducatif et ne remplace pas une évaluation médicale.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Avertissement",
            body_html=(
                "<p><strong>Ce contenu est uniquement informatif.</strong> Il ne constitue pas un avis médical, un diagnostic ou un traitement. "
                "Discutez toujours vos résultats avec un professionnel qualifié.</p>"
            ),
        ),
    ]


def _sections_it():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Risposta rapida: cosa misura un profilo lipidico?",
            body_html=(
                "<p>Un <strong>profilo lipidico</strong> (chiamato anche profilo del colesterolo o test del colesterolo) "
                "è un gruppo di esami del sangue che misurano i grassi circolanti nel sangue. Include tipicamente "
                "<strong>colesterolo totale</strong>, <strong>colesterolo LDL</strong>, <strong>colesterolo HDL</strong> "
                "e <strong>trigliceridi</strong>. Da questi valori, i clinici spesso calcolano il "
                "<strong>colesterolo non-HDL</strong> e il <strong>rapporto colesterolo totale/HDL</strong> per ottenere "
                "un quadro più completo del rischio cardiovascolare.</p>"
                "<p>Ogni marcatore racconta una parte diversa della storia. La maggior parte dei clinici interpreta "
                "questi valori insieme, non in modo isolato.</p>"
            ),
        ),
        Section(
            id="total-cholesterol",
            level=2,
            heading="Colesterolo totale spiegato",
            body_html=(
                "<p>Il <strong>colesterolo totale</strong> è la somma di tutto il colesterolo trasportato nel sangue "
                "attraverso diversi tipi di particelle, tra cui LDL, HDL e VLDL. Offre una panoramica generale ma "
                "non racconta tutta la storia da solo.</p>"
                "<p>Per molti anni il colesterolo totale è stato il principale valore di screening. Oggi i clinici "
                "lo usano come punto di partenza e poi esaminano i singoli componenti – in particolare LDL e HDL – "
                "per comprendere il rischio con maggiore precisione. Un valore di colesterolo totale che sembra "
                "«normale» può comunque nascondere un equilibrio sfavorevole tra LDL e HDL, ecco perché il profilo "
                "completo è importante.</p>"
                "<p>Il colesterolo totale è influenzato da dieta, genetica, attività fisica, farmaci e condizioni di "
                "salute sottostanti. Essendo una misura composita, qualsiasi cambiamento in uno dei suoi componenti "
                "modifica il totale.</p>"
            ),
        ),
        Section(
            id="ldl-cholesterol",
            level=2,
            heading="Colesterolo LDL: il colesterolo «cattivo»",
            body_html=(
                "<p>Il <strong>colesterolo LDL (lipoproteina a bassa densità)</strong> è spesso chiamato colesterolo "
                "«cattivo» perché le particelle LDL possono depositare colesterolo nelle pareti arteriose, contribuendo "
                "nel tempo alla formazione di placche. Questo processo, chiamato aterosclerosi, è un motore chiave "
                "delle malattie cardiovascolari.</p>"
                "<p>Il colesterolo LDL è solitamente l'obiettivo principale quando i clinici discutono la gestione "
                "lipidica. Livelli più bassi di LDL sono generalmente associati a un rischio cardiovascolare inferiore, "
                "anche se il target ideale dipende dal profilo di rischio complessivo, inclusi fattori come pressione "
                "arteriosa, stato di diabete e storia familiare.</p>"
                "<p>È importante notare che il colesterolo LDL misura la <em>quantità di colesterolo</em> all'interno "
                "delle particelle LDL, non il <em>numero di particelle</em> stesse. Alcuni clinici esaminano anche "
                "l'ApoB (apolipoproteina B) o il numero di particelle LDL per una visione più dettagliata, soprattutto "
                "quando il colesterolo LDL e altri marcatori non concordano.</p>"
            ),
        ),
        Section(
            id="hdl-cholesterol",
            level=2,
            heading="Colesterolo HDL: il colesterolo «buono»",
            body_html=(
                "<p>Il <strong>colesterolo HDL (lipoproteina ad alta densità)</strong> è spesso chiamato colesterolo "
                "«buono» perché le particelle HDL aiutano a trasportare il colesterolo dalle arterie al fegato per "
                "l'elaborazione e l'eliminazione. Questo «trasporto inverso del colesterolo» è uno dei motivi per cui "
                "un HDL più alto è generalmente considerato favorevole.</p>"
                "<p>Tuttavia, la relazione tra HDL e rischio cardiovascolare è più sfumata di quanto si pensasse. "
                "Livelli molto alti di HDL non significano automaticamente un rischio inferiore, e aumentare l'HDL con "
                "farmaci non ha migliorato costantemente gli esiti negli studi clinici. La maggior parte dei clinici "
                "considera ora l'HDL come un pezzo di un quadro lipidico più ampio piuttosto che come un obiettivo di "
                "trattamento autonomo.</p>"
                "<p>L'attività fisica regolare, il non fumare e una dieta ricca di grassi sani sono tra i fattori dello "
                "stile di vita più costantemente associati a livelli di HDL più sani.</p>"
            ),
        ),
        Section(
            id="triglycerides",
            level=2,
            heading="Trigliceridi spiegati",
            body_html=(
                "<p>I <strong>trigliceridi</strong> sono il tipo di grasso più comune nel corpo. Immagazzinano l'energia "
                "in eccesso dalla dieta e sono trasportati nel sangue all'interno di particelle VLDL (lipoproteina a "
                "molto bassa densità).</p>"
                "<p>I trigliceridi elevati possono essere influenzati da diversi fattori, tra cui un elevato consumo di "
                "carboidrati raffinati e zuccheri, consumo eccessivo di alcol, obesità, resistenza all'insulina, "
                "ipotiroidismo e alcuni farmaci. Sono anche sensibili ai pasti recenti, motivo per cui il digiuno è "
                "spesso raccomandato prima di un profilo lipidico.</p>"
                "<p>Quando i trigliceridi sono molto alti, i clinici possono considerare il rischio di pancreatite oltre "
                "al rischio cardiovascolare. La gestione spesso include cambiamenti dietetici, attività fisica e "
                "talvolta farmaci a seconda del livello e del contesto di rischio complessivo.</p>"
            ),
        ),
        Section(
            id="non-hdl",
            level=2,
            heading="Colesterolo non-HDL",
            body_html=(
                "<p>Il <strong>colesterolo non-HDL</strong> si calcola sottraendo il colesterolo HDL dal colesterolo "
                "totale. Rappresenta tutto il colesterolo trasportato da particelle diverse dall'HDL – essenzialmente "
                "LDL, VLDL, IDL e altre particelle aterogene combinate.</p>"
                "<p>Molte linee guida attuali considerano il colesterolo non-HDL un utile obiettivo secondario perché "
                "cattura tutte le particelle contenenti colesterolo che possono contribuire alla placca, non solo le LDL. "
                "Si calcola facilmente da un profilo lipidico standard e non richiede un test aggiuntivo.</p>"
                "<p>Il colesterolo non-HDL è particolarmente utile quando i trigliceridi sono elevati, poiché in quella "
                "situazione il colesterolo LDL calcolato può essere meno accurato. Il non-HDL rimane affidabile "
                "indipendentemente dal livello di trigliceridi.</p>"
            ),
        ),
        Section(
            id="total-hdl-ratio",
            level=2,
            heading="Rapporto colesterolo totale/HDL",
            body_html=(
                "<p>Il <strong>rapporto colesterolo totale/HDL</strong> si calcola dividendo il colesterolo totale per "
                "il colesterolo HDL. Fornisce un'istantanea rapida dell'equilibrio tra tutto il colesterolo e la "
                "frazione HDL «protettiva».</p>"
                "<p>Un rapporto più basso è generalmente considerato più favorevole. Ad esempio, un rapporto di circa "
                "3,5–4,0 o inferiore è spesso visto come rischio più basso, mentre un rapporto superiore a 5,0 può "
                "motivare una revisione più attenta. Tuttavia, il rapporto è una semplificazione e non dovrebbe "
                "sostituire uno sguardo dettagliato a ogni singolo marcatore.</p>"
                "<p>Alcuni clinici usano il rapporto come strumento di screening rapido, mentre altri preferiscono "
                "concentrarsi sui valori assoluti di LDL e non-HDL. Entrambi gli approcci hanno validità, e il rapporto "
                "si comprende meglio come una lente aggiuntiva piuttosto che come una misura definitiva del rischio.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Chi dovrebbe fare un profilo lipidico?",
            body_html=(
                "<p>I profili lipidici sono tra gli esami del sangue più richiesti. Le raccomandazioni generali includono:</p>"
                "<ul>"
                "<li><strong>Adulti dai 20 anni in su:</strong> la maggior parte delle linee guida raccomanda un profilo "
                "lipidico di base e test periodici, con frequenza in base ai risultati e ai fattori di rischio.</li>"
                "<li><strong>Persone con fattori di rischio cardiovascolare:</strong> tra cui pressione alta, diabete, "
                "fumo, obesità o storia familiare di malattia cardiaca precoce – potrebbero necessitare di un monitoraggio "
                "più frequente.</li>"
                "<li><strong>Persone in terapia ipolipemizzante:</strong> test regolari aiutano a verificare se il "
                "trattamento sta raggiungendo i suoi obiettivi.</li>"
                "<li><strong>Bambini e adolescenti:</strong> lo screening può essere raccomandato per chi ha una storia "
                "familiare di colesterolo alto o malattia cardiovascolare precoce, o determinate condizioni di salute.</li>"
                "</ul>"
                "<p>Il tuo clinico può consigliare il programma di test adatto alla tua situazione. Il digiuno di 9–12 "
                "ore è spesso raccomandato, soprattutto se i trigliceridi sono al centro dell'attenzione, anche se "
                "alcune linee guida accettano profili a digiuno per lo screening di routine.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normale vs elevato: guida rapida ai pattern",
            body_html=(
                "<div class=\"blog-example\"><strong>Pattern favorevole:</strong> LDL nel range, HDL a livello sano, trigliceridi non elevati e non-HDL entro i limiti previsti. Questa combinazione è generalmente associata a un rischio cardiovascolare inferiore.</div>"
                "<div class=\"blog-example\"><strong>Pattern misto:</strong> LDL moderatamente elevato con trigliceridi al limite. I clinici spesso rivedono dieta, livello di attività, salute metabolica e storia familiare prima di decidere i prossimi passi.</div>"
                "<div class=\"blog-example\"><strong>Trigliceridi elevati con HDL basso:</strong> una combinazione frequente nell'insulino-resistenza e nella sindrome metabolica. Questo pattern spesso motiva uno sguardo più attento all'apporto di carboidrati, alla gestione del peso e ai marcatori del glucosio.</div>"
                "<div class=\"blog-example\"><strong>LDL chiaramente elevato:</strong> può portare a una discussione più mirata sul rischio cardiovascolare, possibilmente includendo opzioni farmacologiche oltre ai cambiamenti dello stile di vita.</div>"
                "<p>Ricorda: i range di riferimento variano in base al laboratorio, e il tuo clinico interpreta i risultati nel contesto del tuo quadro di salute completo.</p>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Prossimi passi",
            body_html=(
                "<p>Se hai risultati lipidici recenti e desideri una spiegazione chiara e strutturata, puoi "
                "<a href=\"/it/upload\">caricare i risultati delle analisi del sangue</a> per ottenere una panoramica "
                "personalizzata. Inizia con <a href=\"/it/blood-test-results-explained\">blood test results explained</a> "
                "per un'introduzione utile e poi usa l'<a href=\"/it/ai-blood-test-analyzer\">AI blood test analyzer</a> "
                "per rivedere la spiegazione insieme al tuo medico.</p>"
                "<p>Capire colesterolo, trigliceridi e HDL insieme ti dà un'immagine molto più chiara di qualsiasi "
                "singolo numero. Porta i tuoi risultati al prossimo appuntamento e discuti cosa significano per il "
                "tuo profilo di rischio individuale.</p>"
                "<p>Questa guida è solo educativa e non sostituisce una valutazione medica.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>Questo articolo è solo informativo.</strong> Non fornisce consigli medici, diagnosi o trattamento. "
                "Discuti sempre i tuoi risultati con un professionista qualificato.</p>"
            ),
        ),
    ]
