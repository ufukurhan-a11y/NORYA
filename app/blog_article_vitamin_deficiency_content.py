"""Blog article for Vitamin Deficiency Blood Test Guide."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what vitamin deficiency testing covers",
            body_html=(
                "<p>A <strong>vitamin deficiency blood test</strong> measures the levels of key vitamins in your blood, "
                "including <strong>Vitamin D, B12, Folate (B9), A, E, and K</strong>. These vitamins play essential roles "
                "in energy, immunity, bone health, nerve function, and blood clotting.</p>"
                "<p>Testing helps identify whether your levels are <strong>deficient, borderline, or adequate</strong>. "
                "Clinicians use these results alongside your symptoms, diet, and medical history to decide on next steps.</p>"
                "<p>If you have recent lab results, you can <a href=\"/en/upload\">upload your blood test results</a> for a "
                "structured overview, then review them with the "
                "<a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a> and your clinician.</p>"
            ),
        ),
        Section(
            id="vitamin-d",
            level=2,
            heading="Vitamin D: the sunshine vitamin",
            body_html=(
                "<p><strong>Vitamin D</strong> is unique among vitamins because your body can produce it when your skin is "
                "exposed to sunlight. It is also found in fatty fish, fortified dairy products, and supplements. "
                "The most common test measures <strong>25-hydroxyvitamin D [25(OH)D]</strong>, which reflects your total "
                "vitamin D from both sun exposure and diet.</p>"
                "<p>Vitamin D supports <strong>calcium absorption, bone mineralization, immune function, and muscle health</strong>. "
                "Deficiency is widespread globally, particularly in people with limited sun exposure, darker skin tones, "
                "older adults, and those living at higher latitudes.</p>"
                "<p><strong>Common signs of low Vitamin D</strong> may include fatigue, frequent infections, bone or back pain, "
                "muscle weakness, and mood changes. However, many people have no obvious symptoms, which is why testing "
                "is often the only way to know your status.</p>"
                "<p>Clinicians interpret Vitamin D levels using lab-specific reference ranges. Generally, values below "
                "the reference range may prompt discussion about supplementation, dietary changes, and safe sun exposure. "
                "Your clinician decides the right approach based on your full health picture.</p>"
            ),
        ),
        Section(
            id="vitamin-b12",
            level=2,
            heading="Vitamin B12: energy and nerve health",
            body_html=(
                "<p><strong>Vitamin B12 (cobalamin)</strong> is essential for <strong>red blood cell formation, nerve function, "
                "DNA synthesis, and energy metabolism</strong>. It is found naturally in animal products such as meat, fish, "
                "eggs, and dairy, making deficiency more common in people following strict vegan or vegetarian diets.</p>"
                "<p>B12 absorption is a complex process that requires adequate stomach acid and intrinsic factor. "
                "Conditions like <strong>pernicious anemia, celiac disease, Crohn's disease, gastric bypass surgery</strong>, "
                "and long-term use of certain medications (such as proton pump inhibitors or metformin) can all reduce B12 absorption.</p>"
                "<p><strong>Symptoms that may suggest low B12</strong> include fatigue, weakness, numbness or tingling in "
                "hands and feet, memory problems, balance issues, and a smooth or swollen tongue. Because B12 deficiency can "
                "affect the nervous system, early detection through testing is important.</p>"
                "<p>When B12 is low, clinicians may also check <strong>methylmalonic acid (MMA)</strong> and "
                "<strong>homocysteine</strong> levels for a more complete picture. Treatment options depend on the cause "
                "and severity, and may include oral supplements, sublingual tablets, or injections.</p>"
            ),
        ),
        Section(
            id="folate",
            level=2,
            heading="Folate (B9): cell division and blood health",
            body_html=(
                "<p><strong>Folate (Vitamin B9)</strong> is critical for <strong>DNA synthesis, cell division, red blood cell "
                "production, and healthy neural tube development during pregnancy</strong>. It works closely with Vitamin B12, "
                "and deficiencies in either can cause similar types of anemia.</p>"
                "<p>Folate is found in <strong>leafy green vegetables, legumes, citrus fruits, fortified grains, and liver</strong>. "
                "Unlike B12, folate stores in the body are limited, so deficiency can develop within weeks of inadequate intake.</p>"
                "<p><strong>Factors that increase folate deficiency risk</strong> include poor diet, alcohol use disorder, "
                "malabsorption conditions (celiac disease, inflammatory bowel disease), certain medications (methotrexate, "
                "some anti-seizure drugs), pregnancy, and dialysis.</p>"
                "<p>Folate testing typically measures <strong>serum folate</strong> and sometimes <strong>red blood cell (RBC) folate</strong>, "
                "which reflects longer-term status. Adequate folate is especially important for women of childbearing age, "
                "as deficiency during early pregnancy can lead to neural tube defects.</p>"
            ),
        ),
        Section(
            id="vitamin-a",
            level=2,
            heading="Vitamin A: vision and immune function",
            body_html=(
                "<p><strong>Vitamin A</strong> is a fat-soluble vitamin essential for <strong>vision, immune function, "
                "reproduction, and cellular communication</strong>. It exists in two main forms: <strong>preformed Vitamin A "
                "(retinol)</strong> from animal sources and <strong>provitamin A carotenoids (like beta-carotene)</strong> "
                "from plant sources.</p>"
                "<p>Vitamin A plays a critical role in maintaining the <strong>cornea, retina, and mucous membranes</strong> "
                "that serve as barriers against infection. It also supports the production and function of white blood cells.</p>"
                "<p><strong>Vitamin A deficiency</strong> is a leading cause of preventable blindness worldwide, particularly "
                "in developing countries. In developed nations, deficiency is less common but can occur in people with "
                "fat malabsorption disorders, liver disease, or very restricted diets.</p>"
                "<p>Testing for Vitamin A measures <strong>serum retinol</strong> levels. Because Vitamin A is stored in the "
                "liver, blood levels may not drop until stores are significantly depleted. Both deficiency and excess "
                "(hypervitaminosis A) can cause health problems, so testing helps clinicians find the right balance.</p>"
            ),
        ),
        Section(
            id="vitamin-e",
            level=2,
            heading="Vitamin E: antioxidant protection",
            body_html=(
                "<p><strong>Vitamin E</strong> is a powerful <strong>fat-soluble antioxidant</strong> that protects cell "
                "membranes from oxidative damage. It supports <strong>immune function, skin health, and blood vessel "
                "integrity</strong>, and helps prevent the formation of blood clots.</p>"
                "<p>Vitamin E is found in <strong>nuts, seeds, vegetable oils, spinach, broccoli, and fortified cereals</strong>. "
                "True deficiency is rare in healthy individuals but can occur in people with fat malabsorption conditions "
                "such as cystic fibrosis, Crohn's disease, or liver disease.</p>"
                "<p><strong>Signs that may suggest low Vitamin E</strong> include nerve and muscle damage, loss of body "
                "movement control, vision problems, and weakened immune response. Because Vitamin E works alongside other "
                "antioxidants, clinicians consider the broader nutritional picture when evaluating levels.</p>"
                "<p>Vitamin E testing measures <strong>serum alpha-tocopherol</strong>, the most biologically active form. "
                "Results are interpreted in the context of your lipid levels, since Vitamin E travels with lipoproteins "
                "in the bloodstream.</p>"
            ),
        ),
        Section(
            id="vitamin-k",
            level=2,
            heading="Vitamin K: blood clotting and bone health",
            body_html=(
                "<p><strong>Vitamin K</strong> is essential for <strong>blood clotting and bone metabolism</strong>. "
                "It exists in two main forms: <strong>Vitamin K1 (phylloquinone)</strong> from plant sources and "
                "<strong>Vitamin K2 (menaquinone)</strong> produced by gut bacteria and found in fermented foods.</p>"
                "<p>Vitamin K activates proteins needed for <strong>blood coagulation</strong>, which is why people taking "
                "blood-thinning medications like warfarin need to maintain consistent Vitamin K intake. It also activates "
                "<strong>osteocalcin</strong>, a protein important for bone mineralization and strength.</p>"
                "<p><strong>Vitamin K deficiency</strong> is uncommon in healthy adults but can occur in people with "
                "malabsorption disorders, liver disease, or those on long-term antibiotics. Newborns are at particular "
                "risk, which is why Vitamin K injections are standard practice at birth in many countries.</p>"
                "<p>Testing may measure <strong>serum phylloquinone</strong> or assess clotting function through "
                "<strong>prothrombin time (PT/INR)</strong>. Your clinician interprets these results alongside your "
                "medications, diet, and overall health status.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Who should consider vitamin testing",
            body_html=(
                "<p>Vitamin testing may be useful for people in several situations:</p>"
                "<ul>"
                "<li><strong>Fatigue or unexplained low energy</strong> — B12, D, and folate deficiencies are common contributors</li>"
                "<li><strong>Vegetarian or vegan diets</strong> — higher risk of B12 deficiency without animal products</li>"
                "<li><strong>Limited sun exposure</strong> — office workers, people in northern latitudes, or those who cover their skin</li>"
                "<li><strong>Digestive or malabsorption conditions</strong> — celiac disease, Crohn's, IBS, gastric bypass</li>"
                "<li><strong>Pregnancy or planning pregnancy</strong> — folate is critical for fetal development</li>"
                "<li><strong>Older adults</strong> — absorption of B12 and Vitamin D synthesis decline with age</li>"
                "<li><strong>Long-term medication use</strong> — PPIs, metformin, anti-seizure medications, and blood thinners</li>"
                "<li><strong>Recurrent infections or slow healing</strong> — may reflect Vitamin D, A, or E status</li>"
                "</ul>"
                "<p>Your clinician can help determine which specific vitamin tests are appropriate based on your symptoms, "
                "diet, medical history, and risk factors.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs deficient: quick pattern guide",
            body_html=(
                "<div class=\"blog-example\"><strong>Vitamin D — In range:</strong> typically means adequate levels for bone and immune health. Your clinician may recommend maintaining current habits.</div>"
                "<div class=\"blog-example\"><strong>Vitamin D — Low:</strong> often leads to discussion about supplementation, dietary adjustments, and safe sun exposure strategies.</div>"
                "<div class=\"blog-example\"><strong>Vitamin B12 — In range:</strong> generally suggests adequate intake and absorption. Borderline results may prompt additional MMA or homocysteine testing.</div>"
                "<div class=\"blog-example\"><strong>Vitamin B12 — Low:</strong> may lead to investigation of absorption issues and consideration of supplements or injections.</div>"
                "<div class=\"blog-example\"><strong>Folate — In range:</strong> suggests adequate intake. For women planning pregnancy, clinicians often recommend continued supplementation regardless.</div>"
                "<div class=\"blog-example\"><strong>Folate — Low:</strong> typically prompts dietary review and supplementation, with particular urgency during pregnancy.</div>"
                "<div class=\"blog-example\"><strong>Vitamin A — In range:</strong> indicates adequate stores. Both deficiency and excess can cause problems, so staying within range is important.</div>"
                "<div class=\"blog-example\"><strong>Vitamin E — In range:</strong> suggests adequate antioxidant protection. Deficiency is rare but may indicate malabsorption.</div>"
                "<div class=\"blog-example\"><strong>Vitamin K — In range:</strong> normal clotting function. If on blood thinners, consistent intake is key for medication management.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="What to do next (with your clinician)",
            body_html=(
                "<p>If you are wondering how your vitamin levels fit into your overall health picture, start by reviewing "
                "them together with your broader lab results. If you want a structured summary, you can "
                "<a href=\"/en/upload\">upload your blood test results</a> for an organized overview.</p>"
                "<p>Start with <a href=\"/en/blood-test-results-explained\">blood test results explained</a> for a clear "
                "framework, and then use the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a> to review "
                "the explanation together with your clinician.</p>"
                "<p>Remember that vitamin levels are just one piece of your health puzzle. Your clinician will consider "
                "your symptoms, diet, lifestyle, medications, and other lab markers to create a personalized plan.</p>"
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
            heading="Kısa cevap: Vitamin eksikliği testi neyi kapsar?",
            body_html=(
                "<p><strong>Vitamin eksikliği kan testi</strong>, kanınızdaki temel vitamin düzeylerini ölçer: "
                "<strong>Vitamin D, B12, Folat (B9), A, E ve K</strong>. Bu vitaminler enerji, bağışıklık, kemik sağlığı, "
                "sinir fonksiyonu ve kan pıhtılaşmasında hayati rol oynar.</p>"
                "<p>Test, düzeylerinizin <strong>eksik, sınırda veya yeterli</strong> olup olmadığını gösterir. "
                "Doktorlar bu sonuçları belirtileriniz, beslenmeniz ve tıbbi geçmişinizle birlikte değerlendirir.</p>"
                "<p>Son test sonuçlarınız varsa, yapılandırılmış bir genel bakış için "
                "<a href=\"/tr/upload\">kan tahlili sonuçlarınızı yükleyin</a>, ardından "
                "<a href=\"/tr/ai-blood-test-analyzer\">AI blood test analyzer</a> ile doktorunuzla birlikte gözden geçirin.</p>"
            ),
        ),
        Section(
            id="vitamin-d",
            level=2,
            heading="Vitamin D: güneş vitamini",
            body_html=(
                "<p><strong>Vitamin D</strong>, cildiniz güneş ışığına maruz kaldığında vücudunuzun üretebildiği "
                "tek vitamindir. Yağlı balıklar, zenginleştirilmiş süt ürünleri ve takviyelerde de bulunur. "
                "En yaygın test, hem güneş maruziyetinden hem de beslenmeden gelen toplam Vitamin D'yi yansıtan "
                "<strong>25-hidroksivitamin D [25(OH)D]</strong> düzeyini ölçer.</p>"
                "<p>Vitamin D <strong>kalsiyum emilimi, kemik mineralizasyonu, bağışıklık fonksiyonu ve kas sağlığı</strong> "
                "için önemlidir. Yetersizlik dünya çapında yaygındır; özellikle güneş maruziyeti sınırlı olanlarda, "
                "koyu cilt tonlarında, yaşlı yetişkinlerde ve yüksek enlemlerde yaşayanlarda daha sık görülür.</p>"
                "<p><strong>Düşük Vitamin D'nin yaygın belirtileri</strong> arasında yorgunluk, sık enfeksiyonlar, "
                "kemik veya sırt ağrısı, kas zayıflığı ve ruh hali değişiklikleri sayılabilir. Ancak birçok insanda "
                "belirgin belirti yoktur, bu nedenle test genellikle durumu bilmenin tek yoludur.</p>"
                "<p>Doktorlar Vitamin D düzeylerini laboratuvara özgü referans aralıklarıyla yorumlar. Genel olarak, "
                "referans aralığının altındaki değerler takviye, diyet değişiklikleri ve güvenli güneş maruziyeti "
                "hakkında tartışmaya yol açabilir.</p>"
            ),
        ),
        Section(
            id="vitamin-b12",
            level=2,
            heading="Vitamin B12: enerji ve sinir sağlığı",
            body_html=(
                "<p><strong>Vitamin B12 (kobalamin)</strong> <strong>kırmızı kan hücresi oluşumu, sinir fonksiyonu, "
                "DNA sentezi ve enerji metabolizması</strong> için gereklidir. Et, balık, yumurta ve süt ürünlerinde "
                "doğal olarak bulunur, bu nedenle sıkı vegan veya vejetaryen beslenenlerde eksiklik daha yaygındır.</p>"
                "<p>B12 emilimi yeterli mide asidi ve intrinsik faktör gerektiren karmaşık bir süreçtir. "
                "<strong>Perisiyöz anemi, çölyak hastalığı, Crohn hastalığı, gastrik bypass ameliyatı</strong> "
                "ve belirli ilaçların uzun süreli kullanımı (proton pompa inhibitörleri veya metformin gibi) "
                "B12 emilimini azaltabilir.</p>"
                "<p><strong>Düşük B12'yi düşündürebilecek belirtiler</strong> arasında yorgunluk, halsizlik, el ve "
                "ayaklarda uyuşma veya karıncalanma, hafıza sorunları, denge problemleri ve pürüzsüz veya şiş dil "
                "sayılabilir. B12 eksikliği sinir sistemini etkileyebileceğinden testle erken tespit önemlidir.</p>"
                "<p>B12 düşük olduğunda doktorlar daha eksiksiz bir tablo için <strong>metilmalonik asit (MMA)</strong> "
                "ve <strong>homosistein</strong> düzeylerini de kontrol edebilir. Tedavi seçenekleri nedene ve "
                "şiddete bağlı olarak oral takviyeler, sublingual tabletler veya enjeksiyonları içerebilir.</p>"
            ),
        ),
        Section(
            id="folate",
            level=2,
            heading="Folat (B9): hücre bölünmesi ve kan sağlığı",
            body_html=(
                "<p><strong>Folat (Vitamin B9)</strong> <strong>DNA sentezi, hücre bölünmesi, kırmızı kan hücresi "
                "üretimi ve gebelik sırasında sağlıklı nöral tüp gelişimi</strong> için kritik öneme sahiptir. "
                "Vitamin B12 ile yakın çalışır ve herhangi birinin eksikliği benzer anemi türlerine yol açabilir.</p>"
                "<p>Folat <strong>yapraklı yeşil sebzeler, baklagiller, narenciye meyveleri, zenginleştirilmiş tahıllar "
                "ve karaciğer</strong>de bulunur. B12'nin aksine folat depoları sınırlıdır, bu nedenle yetersiz alımda "
                "eksiklik haftalar içinde gelişebilir.</p>"
                "<p><strong>Folat eksikliği riskini artıran faktörler</strong> arasında kötü beslenme, alkol kullanım "
                "bozukluğu, emilim bozuklukları (çölyak hastalığı, inflamatuar bağırsak hastalığı), belirli ilaçlar "
                "(metotreksat, bazı nöbet ilaçları), gebelik ve diyaliz sayılabilir.</p>"
                "<p>Folat testi genellikle <strong>serum folat</strong> ve bazen daha uzun vadeli durumu yansıtan "
                "<strong>kırmızı kan hücresi (RBC) folat</strong> düzeyini ölçer. Yeterli folat özellikle çocuk "
                "doğurma çağındaki kadınlar için önemlidir, çünkü gebeliğin erken dönemlerinde eksiklik nöral tüp "
                "defektlerine yol açabilir.</p>"
            ),
        ),
        Section(
            id="vitamin-a",
            level=2,
            heading="Vitamin A: görme ve bağışıklık fonksiyonu",
            body_html=(
                "<p><strong>Vitamin A</strong> <strong>görme, bağışıklık fonksiyonu, üreme ve hücresel iletişim</strong> "
                "için gerekli yağda çözünen bir vitamindir. İki ana formda bulunur: hayvansal kaynaklardan gelen "
                "<strong>hazır Vitamin A (retinol)</strong> ve bitkisel kaynaklardan gelen "
                "<strong>provitamin A karotenoidleri (beta-karoten gibi)</strong>.</p>"
                "<p>Vitamin A <strong>kornea, retina ve enfeksiyonlara karşı bariyer görevi gören müköz zarların</strong> "
                "korunmasında kritik rol oynar. Ayrıca beyaz kan hücrelerinin üretimini ve fonksiyonunu destekler.</p>"
                "<p><strong>Vitamin A eksikliği</strong> dünya çapında önlenebilir körlüğün önde gelen nedenidir, "
                "özellikle gelişmekte olan ülkelerde. Gelişmiş ülkelerde eksiklik daha az yaygındır ancak yağ "
                "emilim bozuklukları, karaciğer hastalığı veya çok kısıtlı diyeti olanlarda görülebilir.</p>"
                "<p>Vitamin A testi <strong>serum retinol</strong> düzeylerini ölçer. Vitamin A karaciğerde "
                "depolandığından, kan düzeyleri depolar önemli ölçüde tükenene kadar düşmeyebilir. Hem eksiklik "
                "hem de fazlalık (hipervitaminoz A) sağlık sorunlarına yol açabileceğinden test doktorların doğru "
                "dengeyi bulmasına yardımcı olur.</p>"
            ),
        ),
        Section(
            id="vitamin-e",
            level=2,
            heading="Vitamin E: antioksidan koruma",
            body_html=(
                "<p><strong>Vitamin E</strong> hücre zarlarını oksidatif hasardan koruyan güçlü bir "
                "<strong>yağda çözünen antioksidandır</strong>. <strong>Bağışıklık fonksiyonu, cilt sağlığı ve kan "
                "damarı bütünlüğünü</strong> destekler ve kan pıhtıları oluşumunu önlemeye yardımcı olur.</p>"
                "<p>Vitamin E <strong>kuruyemişler, tohumlar, bitkisel yağlar, ıspanak, brokoli ve zenginleştirilmiş "
                "tahıllar</strong>da bulunur. Gerçek eksiklik sağlıklı bireylerde nadirdir ancak kistik fibroz, "
                "Crohn hastalığı veya karaciğer hastalığı gibi yağ emilim bozuklukları olanlarda görülebilir.</p>"
                "<p><strong>Düşük Vitamin E'yi düşündürebilecek belirtiler</strong> arasında sinir ve kas hasarı, "
                "vücut hareket kontrolünün kaybı, görme sorunları ve zayıflamış bağışıklık yanıtı sayılabilir. "
                "Vitamin E diğer antioksidanlarla birlikte çalıştığından doktorlar düzeyleri değerlendirirken "
                "daha geniş beslenme tablosunu göz önünde bulundurur.</p>"
                "<p>Vitamin E testi en biyolojik aktif form olan <strong>serum alfa-tokoferol</strong> düzeyini ölçer. "
                "Sonuçlar, Vitamin E kanda lipoproteinlerle taşındığından lipid düzeyleriniz bağlamında yorumlanır.</p>"
            ),
        ),
        Section(
            id="vitamin-k",
            level=2,
            heading="Vitamin K: kan pıhtılaşması ve kemik sağlığı",
            body_html=(
                "<p><strong>Vitamin K</strong> <strong>kan pıhtılaşması ve kemik metabolizması</strong> için gereklidir. "
                "İki ana formda bulunur: bitkisel kaynaklardan gelen <strong>Vitamin K1 (filokinon)</strong> ve "
                "bağırsak bakterileri tarafından üretilen ile fermente gıdalarda bulunan "
                "<strong>Vitamin K2 (menakinon)</strong>.</p>"
                "<p>Vitamin K <strong>kan pıhtılaşması</strong> için gerekli proteinleri aktive eder, bu nedenle "
                "warfarin gibi kan sulandırıcı ilaç kullanan kişilerin tutarlı Vitamin K alımını sürdürmesi gerekir. "
                "Ayrıca kemik mineralizasyonu ve gücü için önemli bir protein olan "
                "<strong>osteokalsini</strong> de aktive eder.</p>"
                "<p><strong>Vitamin K eksikliği</strong> sağlıklı yetişkinlerde nadirdir ancak emilim bozuklukları, "
                "karaciğer hastalığı olanlarda veya uzun süreli antibiyotik kullananlarda görülebilir. Yenidoğanlar "
                "özellikle risk altındadır, bu nedenle birçok ülkede doğumda Vitamin K enjeksiyonu standart uygulamadır.</p>"
                "<p>Test <strong>serum filokinon</strong> düzeyini ölçebilir veya <strong>protrombin zamanı (PT/INR)</strong> "
                "ile pıhtılaşma fonksiyonunu değerlendirebilir. Doktorunuz bu sonuçları ilaçlarınız, beslenmeniz "
                "ve genel sağlık durumunuzla birlikte yorumlar.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Kimler vitamin testi yaptırmayı düşünmeli?",
            body_html=(
                "<p>Vitamin testi şu durumlardaki kişiler için yararlı olabilir:</p>"
                "<ul>"
                "<li><strong>Yorgunluk veya açıklanamayan düşük enerji</strong> — B12, D ve folat eksiklikleri yaygın nedenlerdir</li>"
                "<li><strong>Vejetaryen veya vegan beslenme</strong> — hayvansal ürünler olmadan B12 eksikliği riski daha yüksektir</li>"
                "<li><strong>Sınırlı güneş maruziyeti</strong> — ofis çalışanları, kuzey enlemlerde yaşayanlar veya cildini kapatanlar</li>"
                "<li><strong>Sindirim veya emilim bozuklukları</strong> — çölyak hastalığı, Crohn, IBS, gastrik bypass</li>"
                "<li><strong>Gebelik veya gebelik planlama</strong> — folat fetal gelişim için kritik öneme sahiptir</li>"
                "<li><strong>Yaşlı yetişkinler</strong> — B12 emilimi ve Vitamin D sentezi yaşla birlikte azalır</li>"
                "<li><strong>Uzun süreli ilaç kullanımı</strong> — PPI'lar, metformin, nöbet ilaçları ve kan sulandırıcılar</li>"
                "<li><strong>Tekrarlayan enfeksiyonlar veya yavaş iyileşme</strong> — Vitamin D, A veya E durumunu yansıtabilir</li>"
                "</ul>"
                "<p>Doktorunuz belirtilerinize, beslenmenize, tıbbi geçmişinize ve risk faktörlerinize dayanarak "
                "hangi spesifik vitamin testlerinin uygun olduğunu belirlemenize yardımcı olabilir.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs eksik: hızlı desen rehberi",
            body_html=(
                "<div class=\"blog-example\"><strong>Vitamin D — Normal aralık:</strong> genellikle kemik ve bağışıklık sağlığı için yeterli düzeyleri ifade eder. Doktorunuz mevcut alışkanlıklarınızı sürdürmenizi önerebilir.</div>"
                "<div class=\"blog-example\"><strong>Vitamin D — Düşük:</strong> genellikle takviye, diyet ayarlamaları ve güvenli güneş maruziyeti stratejileri hakkında tartışmaya yol açar.</div>"
                "<div class=\"blog-example\"><strong>Vitamin B12 — Normal aralık:</strong> genellikle yeterli alım ve emilimi gösterir. Sınır sonuçlar ek MMA veya homosistein testini gerektirebilir.</div>"
                "<div class=\"blog-example\"><strong>Vitamin B12 — Düşük:</strong> emilim sorunlarının araştırılmasına ve takviye veya enjeksiyonların değerlendirilmesine yol açabilir.</div>"
                "<div class=\"blog-example\"><strong>Folat — Normal aralık:</strong> yeterli alımı gösterir. Gebelik planlayan kadınlar için doktorlar genellikle takviyeye devam edilmesini önerir.</div>"
                "<div class=\"blog-example\"><strong>Folat — Düşük:</strong> genellikle diyet incelemesi ve takviyeyi gerektirir, özellikle gebelik sırasında acil öncelik taşır.</div>"
                "<div class=\"blog-example\"><strong>Vitamin A — Normal aralık:</strong> yeterli depoları gösterir. Hem eksiklik hem fazlalık sorun yaratabilir, bu nedenle aralıkta kalmak önemlidir.</div>"
                "<div class=\"blog-example\"><strong>Vitamin E — Normal aralık:</strong> yeterli antioksidan korumayı gösterir. Eksiklik nadirdir ancak emilim bozukluğunu işaret edebilir.</div>"
                "<div class=\"blog-example\"><strong>Vitamin K — Normal aralık:</strong> normal pıhtılaşma fonksiyonu. Kan sulandırıcı kullanıyorsanız, ilaç yönetimi için tutarlı alım anahtardır.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Sıradaki adımlar (doktorunuzla)",
            body_html=(
                "<p>Vitamin düzeylerinizin genel sağlığınıza nasıl uyduğunu merak ediyorsanız, "
                "genel laboratuvar sonuçlarınızla birlikte gözden geçirin. Yapılandırılmış bir özet isterseniz "
                "düzenli bir genel bakış için <a href=\"/tr/upload\">kan tahlili sonuçlarınızı yükleyin</a>.</p>"
                "<p>Net bir çerçeve için önce <a href=\"/tr/blood-test-results-explained\">blood test results explained</a> "
                "ile hızlı bir bakış edinin, ardından açıklamanı doktorunuzla birlikte gözden geçirmek için "
                "<a href=\"/tr/ai-blood-test-analyzer\">AI blood test analyzer</a>'ı kullanın.</p>"
                "<p>Unutmayın ki vitamin düzeyleri sağlık bulmacanızın yalnızca bir parçasıdır. Doktorunuz "
                "belirtilerinizi, beslenmenizi, yaşam tarzınızı, ilaçlarınızı ve diğer laboratuvar belirteçlerinizi "
                "dikkate alarak kişiselleştirilmiş bir plan oluşturacaktır.</p>"
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
            heading="Kurz erklärt: Was ein Vitaminmangel-Test zeigt",
            body_html=(
                "<p>Ein <strong>Vitaminmangel-Bluttest</strong> misst die Spiegel wichtiger Vitamine in Ihrem Blut, "
                "darunter <strong>Vitamin D, B12, Folat (B9), A, E und K</strong>. Diese Vitamine spielen wesentliche "
                "Rollen bei Energie, Immunität, Knochengesundheit, Nervenfunktion und Blutgerinnung.</p>"
                "<p>Der Test zeigt, ob Ihre Werte <strong>mangelhaft, grenzwertig oder ausreichend</strong> sind. "
                "Ärztinnen und Ärzte werten diese Ergebnisse zusammen mit Ihren Symptomen, Ihrer Ernährung und "
                "Ihrer Krankengeschichte aus.</p>"
                "<p>Wenn Sie aktuelle Laborergebnisse haben, können Sie "
                "<a href=\"/de/upload\">Ihre Bluttest-Ergebnisse hochladen</a> für eine strukturierte Übersicht "
                "und sie dann mit dem <a href=\"/de/ai-blood-test-analyzer\">AI blood test analyzer</a> "
                "und Ihrer Ärztin/Ihrem Arzt durchgehen.</p>"
            ),
        ),
        Section(
            id="vitamin-d",
            level=2,
            heading="Vitamin D: das Sonnenvitamin",
            body_html=(
                "<p><strong>Vitamin D</strong> ist einzigartig, weil Ihr Körper es bei Sonneneinstrahlung auf der Haut "
                "selbst produzieren kann. Es ist auch in fettem Fisch, angereicherten Milchprodukten und Nahrungsergänzungsmitteln "
                "enthalten. Der häufigste Test misst <strong>25-Hydroxyvitamin D [25(OH)D]</strong>, das Ihr Gesamt-Vitamin D "
                "aus Sonne und Ernährung widerspiegelt.</p>"
                "<p>Vitamin D unterstützt <strong>Kalziumaufnahme, Knochenmineralisierung, Immunfunktion und Muskelgesundheit</strong>. "
                "Ein Mangel ist weltweit verbreitet, besonders bei Menschen mit begrenzter Sonneneinstrahlung, "
                "dunkleren Hauttönen, älteren Erwachsenen und Bewohnern höherer Breitengrade.</p>"
                "<p><strong>Häufige Anzeichen für niedrige Vitamin-D-Werte</strong> können Müdigkeit, häufige Infektionen, "
                "Knochen- oder Rückenschmerzen, Muskelschwäche und Stimmungsschwankungen sein. Viele Menschen haben jedoch "
                "keine offensichtlichen Symptome, weshalb der Test oft der einzige Weg ist, den Status zu kennen.</p>"
                "<p>Ärztinnen und Ärzte interpretieren Vitamin-D-Werte mit laborspezifischen Referenzbereichen. Werte unter "
                "dem Referenzbereich können Diskussionen über Supplementierung, Ernährungsumstellung und sichere "
                "Sonnenexposition auslösen.</p>"
            ),
        ),
        Section(
            id="vitamin-b12",
            level=2,
            heading="Vitamin B12: Energie und Nervengesundheit",
            body_html=(
                "<p><strong>Vitamin B12 (Cobalamin)</strong> ist essenziell für <strong>rote Blutkörperchen, Nervenfunktion, "
                "DNA-Synthese und Energiestoffwechsel</strong>. Es kommt natürlich in tierischen Produkten wie Fleisch, Fisch, "
                "Eiern und Milchprodukten vor, weshalb ein Mangel bei streng vegan oder vegetarisch lebenden Menschen häufiger ist.</p>"
                "<p>Die B12-Aufnahme ist ein komplexer Prozess, der ausreichend Magensäure und Intrinsic Factor erfordert. "
                "Erkrankungen wie <strong>perniziöse Anämie, Zöliakie, Morbus Crohn, Magenbypass-Operationen</strong> "
                "und die langfristige Einnahme bestimmter Medikamente (Protonenpumpenhemmer oder Metformin) können "
                "die B12-Aufnahme verringern.</p>"
                "<p><strong>Symptome, die auf niedrige B12-Werte hindeuten können</strong>, sind Müdigkeit, Schwäche, "
                "Taubheit oder Kribbeln in Händen und Füßen, Gedächtnisprobleme, Gleichgewichtsstörungen und eine "
                "glatte oder geschwollene Zunge. Da B12-Mangel das Nervensystem beeinträchtigen kann, ist eine "
                "frühe Erkennung durch Tests wichtig.</p>"
                "<p>Bei niedrigem B12 können Ärztinnen und Ärzte auch <strong>Methylmalonsäure (MMA)</strong> und "
                "<strong>Homocystein</strong> messen. Behandlungsoptionen hängen von Ursache und Schweregrad ab "
                "und können orale Supplemente, sublinguale Tabletten oder Injektionen umfassen.</p>"
            ),
        ),
        Section(
            id="folate",
            level=2,
            heading="Folat (B9): Zellteilung und Blutgesundheit",
            body_html=(
                "<p><strong>Folat (Vitamin B9)</strong> ist kritisch für <strong>DNA-Synthese, Zellteilung, Produktion "
                "roter Blutkörperchen und gesunde Neuralrohr-Entwicklung während der Schwangerschaft</strong>. "
                "Es arbeitet eng mit Vitamin B12 zusammen, und Mängel in beiden können ähnliche Anämie-Formen verursachen.</p>"
                "<p>Folat findet sich in <strong>blattgrünem Gemüse, Hülsenfrüchten, Zitrusfrüchten, angereicherten "
                "Getreiden und Leber</strong>. Im Gegensatz zu B12 sind die Folatspeicher begrenzt, sodass ein Mangel "
                "innerhalb von Wochen unzureichender Aufnahme entstehen kann.</p>"
                "<p><strong>Faktoren, die das Folatmangel-Risiko erhöhen</strong>, sind schlechte Ernährung, "
                "Alkoholabhängigkeit, Malabsorptionserkrankungen (Zöliakie, chronisch-entzündliche Darmerkrankungen), "
                "bestimmte Medikamente (Methotrexat, einige Antiepileptika), Schwangerschaft und Dialyse.</p>"
                "<p>Die Folat-Testung misst typischerweise <strong>Serumfolat</strong> und manchmal "
                "<strong>Erythrozyten-Folat (RBC-Folat)</strong>, das den Langzeitstatus widerspiegelt. "
                "Ausreichend Folat ist besonders für Frauen im gebärfähigen Alter wichtig.</p>"
            ),
        ),
        Section(
            id="vitamin-a",
            level=2,
            heading="Vitamin A: Sehkraft und Immunfunktion",
            body_html=(
                "<p><strong>Vitamin A</strong> ist ein fettlösliches Vitamin, das für <strong>Sehkraft, Immunfunktion, "
                "Fortpflanzung und zelluläre Kommunikation</strong> essenziell ist. Es existiert in zwei Hauptformen: "
                "<strong>vorformiertes Vitamin A (Retinol)</strong> aus tierischen Quellen und "
                "<strong>Provitamin-A-Carotinoide (wie Beta-Carotin)</strong> aus pflanzlichen Quellen.</p>"
                "<p>Vitamin A spielt eine kritische Rolle bei der Erhaltung von <strong>Hornhaut, Netzhaut und "
                "Schleimhäuten</strong>, die als Barrieren gegen Infektionen dienen. Es unterstützt auch die "
                "Produktion und Funktion weißer Blutkörperchen.</p>"
                "<p><strong>Vitamin-A-Mangel</strong> ist weltweit eine führende Ursache für vermeidbare Blindheit, "
                "besonders in Entwicklungsländern. In entwickelten Ländern ist Mangel seltener, kann aber bei "
                "Fettmalabsorptionsstörungen, Lebererkrankungen oder sehr eingeschränkten Diäten auftreten.</p>"
                "<p>Die Testung misst <strong>Serum-Retinol</strong>. Da Vitamin A in der Leber gespeichert wird, "
                "sinken die Blutwerte erst, wenn die Speicher deutlich erschöpft sind. Sowohl Mangel als auch "
                "Überschuss (Hypervitaminose A) können Probleme verursachen.</p>"
            ),
        ),
        Section(
            id="vitamin-e",
            level=2,
            heading="Vitamin E: Antioxidativer Schutz",
            body_html=(
                "<p><strong>Vitamin E</strong> ist ein starkes <strong>fettlösliches Antioxidans</strong>, das "
                "Zellmembranen vor oxidativen Schäden schützt. Es unterstützt <strong>Immunfunktion, Hautgesundheit "
                "und Blutgefäß-Integrität</strong> und hilft bei der Vorbeugung von Blutgerinnseln.</p>"
                "<p>Vitamin E findet sich in <strong>Nüssen, Samen, Pflanzenölen, Spinat, Brokkoli und angereicherten "
                "Cerealien</strong>. Echter Mangel ist bei gesunden Menschen selten, kann aber bei Fettmalabsorptions-"
                "erkrankungen wie Mukoviszidose, Morbus Crohn oder Lebererkrankungen auftreten.</p>"
                "<p><strong>Anzeichen für niedriges Vitamin E</strong> können Nerven- und Muskelschäden, Verlust der "
                "Bewegungskontrolle, Sehprobleme und geschwächte Immunantwort sein. Da Vitamin E mit anderen "
                "Antioxidantien zusammenarbeitet, betrachten Ärztinnen und Ärzte das breitere Ernährungsbild.</p>"
                "<p>Der Test misst <strong>Serum-Alpha-Tocopherol</strong>, die biologisch aktivste Form. "
                "Ergebnisse werden im Kontext Ihrer Lipidwerte interpretiert, da Vitamin E mit Lipoproteinen "
                "im Blut transportiert wird.</p>"
            ),
        ),
        Section(
            id="vitamin-k",
            level=2,
            heading="Vitamin K: Blutgerinnung und Knochengesundheit",
            body_html=(
                "<p><strong>Vitamin K</strong> ist essenziell für <strong>Blutgerinnung und Knochenstoffwechsel</strong>. "
                "Es existiert in zwei Hauptformen: <strong>Vitamin K1 (Phyllochinon)</strong> aus pflanzlichen Quellen "
                "und <strong>Vitamin K2 (Menachinon)</strong>, produziert von Darmbakterien und in fermentierten Lebensmitteln.</p>"
                "<p>Vitamin K aktiviert Proteine, die für die <strong>Blutgerinnung</strong> benötigt werden. Deshalb "
                "müssen Menschen, die blutverdünnende Medikamente wie Warfarin einnehmen, eine konstante Vitamin-K-Aufnahme "
                "aufrechterhalten. Es aktiviert auch <strong>Osteocalcin</strong>, ein Protein für die Knochenmineralisierung.</p>"
                "<p><strong>Vitamin-K-Mangel</strong> ist bei gesunden Erwachsenen selten, kann aber bei Malabsorptions-"
                "störungen, Lebererkrankungen oder langfristiger Antibiotika-Einnahme auftreten. Neugeborene sind "
                "besonders gefährdet, weshalb Vitamin-K-Injektionen bei der Geburt in vielen Ländern Standard sind.</p>"
                "<p>Die Testung kann <strong>Serum-Phyllochinon</strong> messen oder die Gerinnungsfunktion über "
                "<strong>Prothrombinzeit (PT/INR)</strong> bewerten.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Wer sollte einen Vitamin-Test in Betracht ziehen?",
            body_html=(
                "<p>Vitamin-Tests können in folgenden Situationen sinnvoll sein:</p>"
                "<ul>"
                "<li><strong>Müdigkeit oder unerklärte Energielosigkeit</strong> — B12-, D- und Folatmangel sind häufige Ursachen</li>"
                "<li><strong>Vegetarische oder vegane Ernährung</strong> — höheres B12-Mangel-Risiko ohne tierische Produkte</li>"
                "<li><strong>Begrenzte Sonnenexposition</strong> — Büroarbeitende, Menschen in nördlichen Breiten</li>"
                "<li><strong>Verdauungs- oder Malabsorptionserkrankungen</strong> — Zöliakie, Morbus Crohn, Reizdarm, Magenbypass</li>"
                "<li><strong>Schwangerschaft oder Schwangerschaftsplanung</strong> — Folat ist kritisch für die fetale Entwicklung</li>"
                "<li><strong>Ältere Erwachsene</strong> — B12-Aufnahme und Vitamin-D-Synthese nehmen mit dem Alter ab</li>"
                "<li><strong>Langfristige Medikamenteneinnahme</strong> — PPIs, Metformin, Antiepileptika, Blutverdünner</li>"
                "<li><strong>Wiederkehrende Infektionen oder langsame Heilung</strong> — kann Vitamin-D-, A- oder E-Status widerspiegeln</li>"
                "</ul>"
                "<p>Ihre Ärztin/Ihr Arzt kann helfen, die passenden Tests basierend auf Ihren Symptomen und "
                "Risikofaktoren zu bestimmen.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs. Mangel: schnelle Orientierung",
            body_html=(
                "<div class=\"blog-example\"><strong>Vitamin D — Im Bereich:</strong> bedeutet typischerweise ausreichende Werte für Knochen- und Immungesundheit.</div>"
                "<div class=\"blog-example\"><strong>Vitamin D — Niedrig:</strong> führt oft zu Diskussionen über Supplementierung und Ernährungsumstellung.</div>"
                "<div class=\"blog-example\"><strong>Vitamin B12 — Im Bereich:</strong> deutet auf ausreichende Aufnahme und Absorption hin. Grenzwerte können zusätzliche MMA-Tests erfordern.</div>"
                "<div class=\"blog-example\"><strong>Vitamin B12 — Niedrig:</strong> kann Untersuchung von Absorptionsproblemen und Supplement-Überlegung auslösen.</div>"
                "<div class=\"blog-example\"><strong>Folat — Im Bereich:</strong> zeigt ausreichende Aufnahme. Bei Schwangerschaftsplanung wird oft weiter supplementiert.</div>"
                "<div class=\"blog-example\"><strong>Folat — Niedrig:</strong> erfordert typischerweise Diät-Review und Supplementierung, besonders in der Schwangerschaft.</div>"
                "<div class=\"blog-example\"><strong>Vitamin A — Im Bereich:</strong> zeigt ausreichende Speicher. Sowohl Mangel als auch Überschuss können Probleme verursachen.</div>"
                "<div class=\"blog-example\"><strong>Vitamin E — Im Bereich:</strong> deutet auf ausreichenden antioxidativen Schutz hin. Mangel ist selten.</div>"
                "<div class=\"blog-example\"><strong>Vitamin K — Im Bereich:</strong> normale Gerinnungsfunktion. Bei Blutverdünnern ist konstante Aufnahme wichtig.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Was als Nächstes tun (mit Ihrer Ärztin/Arzt)",
            body_html=(
                "<p>Wenn Sie verstehen möchten, wie Ihre Vitaminwerte in Ihre Gesamtgesundheit passen, betrachten "
                "Sie sie zusammen mit Ihren übrigen Laborergebnissen. Für eine strukturierte Übersicht können Sie "
                "<a href=\"/de/upload\">Ihre Bluttest-Ergebnisse hochladen</a>.</p>"
                "<p>Nutzen Sie <a href=\"/de/blood-test-results-explained\">blood test results explained</a> für eine "
                "schnelle Orientierung und anschließend den <a href=\"/de/ai-blood-test-analyzer\">AI blood test analyzer</a>, "
                "um die Erklärung mit Ihrer Ärztin/Ihrem Arzt durchzugehen.</p>"
                "<p>Vitaminwerte sind nur ein Teil Ihres Gesundheitsbildes. Ihre Ärztin/Ihr Arzt berücksichtigt "
                "Ihre Symptome, Ernährung, Lebensstil, Medikamente und andere Laborwerte für einen persönlichen Plan.</p>"
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
            heading="Respuesta rápida: qué cubre el análisis de deficiencia de vitaminas",
            body_html=(
                "<p>Un <strong>análisis de sangre para deficiencia de vitaminas</strong> mide los niveles de vitaminas "
                "clave en la sangre, incluyendo <strong>Vitamina D, B12, Folato (B9), A, E y K</strong>. Estas vitaminas "
                "desempeñan roles esenciales en energía, inmunidad, salud ósea, función nerviosa y coagulación sanguínea.</p>"
                "<p>El análisis ayuda a identificar si sus niveles son <strong>deficientes, fronterizos o adecuados</strong>. "
                "Los clínicos usan estos resultados junto con sus síntomas, dieta e historial médico para decidir los siguientes pasos.</p>"
                "<p>Si tiene resultados recientes, puede <a href=\"/es/upload\">subir sus resultados de análisis de sangre</a> "
                "para un resumen estructurado y luego revisarlos con el "
                "<a href=\"/es/ai-blood-test-analyzer\">AI blood test analyzer</a> y su clínico.</p>"
            ),
        ),
        Section(
            id="vitamin-d",
            level=2,
            heading="Vitamina D: la vitamina del sol",
            body_html=(
                "<p>La <strong>Vitamina D</strong> es única porque su cuerpo puede producirla cuando la piel se expone "
                "a la luz solar. También se encuentra en pescados grasos, productos lácteos enriquecidos y suplementos. "
                "La prueba más común mide <strong>25-hidroxivitamina D [25(OH)D]</strong>, que refleja su vitamina D total "
                "del sol y la dieta.</p>"
                "<p>La Vitamina D apoya la <strong>absorción de calcio, mineralización ósea, función inmune y salud muscular</strong>. "
                "La deficiencia es generalizada a nivel mundial, particularmente en personas con exposición solar limitada, "
                "tonos de piel más oscuros, adultos mayores y quienes viven en latitudes más altas.</p>"
                "<p><strong>Signos comunes de Vitamina D baja</strong> pueden incluir fatiga, infecciones frecuentes, "
                "dolor óseo o de espalda, debilidad muscular y cambios de humor. Sin embargo, muchas personas no tienen "
                "síntomas evidentes, por lo que el análisis es a menudo la única forma de conocer su estado.</p>"
                "<p>Los clínicos interpretan los niveles de Vitamina D usando rangos de referencia del laboratorio. "
                "Valores por debajo del rango de referencia pueden llevar a discutir suplementación, cambios dietéticos "
                "y exposición solar segura.</p>"
            ),
        ),
        Section(
            id="vitamin-b12",
            level=2,
            heading="Vitamina B12: energía y salud nerviosa",
            body_html=(
                "<p>La <strong>Vitamina B12 (cobalamina)</strong> es esencial para la <strong>formación de glóbulos rojos, "
                "función nerviosa, síntesis de ADN y metabolismo energético</strong>. Se encuentra naturalmente en productos "
                "animales como carne, pescado, huevos y lácteos, por lo que la deficiencia es más común en personas con "
                "dietas estrictamente veganas o vegetarianas.</p>"
                "<p>La absorción de B12 es un proceso complejo que requiere ácido estomacal adecuado y factor intrínseco. "
                "Condiciones como <strong>anemia perniciosa, enfermedad celíaca, enfermedad de Crohn, cirugía de bypass gástrico</strong> "
                "y el uso prolongado de ciertos medicamentos (inhibidores de la bomba de protones o metformina) pueden "
                "reducir la absorción de B12.</p>"
                "<p><strong>Síntomas que pueden sugerir B12 baja</strong> incluyen fatiga, debilidad, entumecimiento u "
                "hormigueo en manos y pies, problemas de memoria, problemas de equilibrio y lengua lisa o hinchada. "
                "Dado que la deficiencia de B12 puede afectar el sistema nervioso, la detección temprana mediante análisis es importante.</p>"
                "<p>Cuando la B12 es baja, los clínicos pueden también verificar <strong>ácido metilmalónico (MMA)</strong> "
                "y <strong>homocisteína</strong> para una imagen más completa. Las opciones de tratamiento dependen de la "
                "causa y severidad, e incluyen suplementos orales, tabletas sublinguales o inyecciones.</p>"
            ),
        ),
        Section(
            id="folate",
            level=2,
            heading="Folato (B9): división celular y salud sanguínea",
            body_html=(
                "<p>El <strong>Folato (Vitamina B9)</strong> es crítico para la <strong>síntesis de ADN, división celular, "
                "producción de glóbulos rojos y desarrollo saludable del tubo neural durante el embarazo</strong>. "
                "Trabaja estrechamente con la Vitamina B12, y deficiencias en cualquiera pueden causar tipos similares de anemia.</p>"
                "<p>El folato se encuentra en <strong>vegetales de hoja verde, legumbres, cítricos, granos enriquecidos e hígado</strong>. "
                "A diferencia de la B12, las reservas de folato son limitadas, por lo que la deficiencia puede desarrollarse "
                "en semanas de ingesta inadecuada.</p>"
                "<p><strong>Factores que aumentan el riesgo de deficiencia de folato</strong> incluyen mala alimentación, "
                "trastorno por consumo de alcohol, condiciones de malabsorción (enfermedad celíaca, enfermedad inflamatoria "
                "intestinal), ciertos medicamentos (metotrexato, algunos anticonvulsivos), embarazo y diálisis.</p>"
                "<p>El análisis de folato mide típicamente <strong>folato sérico</strong> y a veces <strong>folato en "
                "glóbulos rojos (RBC)</strong>, que refleja el estado a largo plazo. El folato adecuado es especialmente "
                "importante para mujeres en edad fértil.</p>"
            ),
        ),
        Section(
            id="vitamin-a",
            level=2,
            heading="Vitamina A: visión y función inmune",
            body_html=(
                "<p>La <strong>Vitamina A</strong> es una vitamina liposoluble esencial para la <strong>visión, función "
                "inmune, reproducción y comunicación celular</strong>. Existe en dos formas principales: "
                "<strong>Vitamina A preformada (retinol)</strong> de fuentes animales y "
                "<strong>carotenoides provitamina A (como beta-caroteno)</strong> de fuentes vegetales.</p>"
                "<p>La Vitamina A juega un papel crítico en el mantenimiento de la <strong>córnea, retina y membranas "
                "mucosas</strong> que sirven como barreras contra infecciones. También apoya la producción y función "
                "de glóbulos blancos.</p>"
                "<p><strong>La deficiencia de Vitamina A</strong> es una causa líder de ceguera prevenible en el mundo, "
                "particularmente en países en desarrollo. En naciones desarrolladas es menos común pero puede ocurrir "
                "en personas con trastornos de malabsorción de grasas, enfermedad hepática o dietas muy restrictivas.</p>"
                "<p>El análisis mide <strong>retinol sérico</strong>. Dado que la Vitamina A se almacena en el hígado, "
                "los niveles sanguíneos pueden no bajar hasta que las reservas estén significativamente agotadas. "
                "Tanto la deficiencia como el exceso (hipervitaminosis A) pueden causar problemas.</p>"
            ),
        ),
        Section(
            id="vitamin-e",
            level=2,
            heading="Vitamina E: protección antioxidante",
            body_html=(
                "<p>La <strong>Vitamina E</strong> es un poderoso <strong>antioxidante liposoluble</strong> que protege "
                "las membranas celulares del daño oxidativo. Apoya la <strong>función inmune, salud de la piel e "
                "integridad de los vasos sanguíneos</strong> y ayuda a prevenir la formación de coágulos.</p>"
                "<p>La Vitamina E se encuentra en <strong>nueces, semillas, aceites vegetales, espinacas, brócoli y "
                "cereales enriquecidos</strong>. La deficiencia verdadera es rara en personas sanas pero puede ocurrir "
                "en personas con condiciones de malabsorción de grasas como fibrosis quística, enfermedad de Crohn o enfermedad hepática.</p>"
                "<p><strong>Signos que pueden sugerir Vitamina E baja</strong> incluyen daño nervioso y muscular, pérdida "
                "del control del movimiento corporal, problemas de visión y respuesta inmune debilitada. Dado que la "
                "Vitamina E trabaja junto con otros antioxidantes, los clínicos consideran el panorama nutricional más amplio.</p>"
                "<p>El análisis mide <strong>alfa-tocoferol sérico</strong>, la forma más biológicamente activa. "
                "Los resultados se interpretan en el contexto de sus niveles lipídicos, ya que la Vitamina E viaja "
                "con lipoproteínas en el torrente sanguíneo.</p>"
            ),
        ),
        Section(
            id="vitamin-k",
            level=2,
            heading="Vitamina K: coagulación sanguínea y salud ósea",
            body_html=(
                "<p>La <strong>Vitamina K</strong> es esencial para la <strong>coagulación sanguínea y el metabolismo óseo</strong>. "
                "Existe en dos formas principales: <strong>Vitamina K1 (filoquinona)</strong> de fuentes vegetales y "
                "<strong>Vitamina K2 (menaquinona)</strong> producida por bacterias intestinales y encontrada en alimentos fermentados.</p>"
                "<p>La Vitamina K activa proteínas necesarias para la <strong>coagulación sanguínea</strong>, por lo que "
                "las personas que toman anticoagulantes como warfarina necesitan mantener una ingesta consistente de Vitamina K. "
                "También activa la <strong>osteocalcina</strong>, una proteína importante para la mineralización y fortaleza ósea.</p>"
                "<p><strong>La deficiencia de Vitamina K</strong> es poco común en adultos sanos pero puede ocurrir en "
                "personas con trastornos de malabsorción, enfermedad hepática o uso prolongado de antibióticos. Los "
                "recién nacidos están en riesgo particular, por lo que las inyecciones de Vitamina K al nacer son "
                "práctica estándar en muchos países.</p>"
                "<p>El análisis puede medir <strong>filoquinona sérica</strong> o evaluar la función de coagulación "
                "mediante <strong>tiempo de protrombina (PT/INR)</strong>.</p>"
            ),
        ),
        Section(
            id="who-should-test",
            level=2,
            heading="Quién debería considerar análisis de vitaminas",
            body_html=(
                "<p>Los análisis de vitaminas pueden ser útiles para personas en varias situaciones:</p>"
                "<ul>"
                "<li><strong>Fatiga o energía baja inexplicable</strong> — deficiencias de B12, D y folato son causas comunes</li>"
                "<li><strong>Dietas vegetarianas o veganas</strong> — mayor riesgo de deficiencia de B12 sin productos animales</li>"
                "<li><strong>Exposición solar limitada</strong> — trabajadores de oficina, personas en latitudes norteñas</li>"
                "<li><strong>Condiciones digestivas o de malabsorción</strong> — enfermedad celíaca, Crohn, SII, bypass gástrico</li>"
                "<li><strong>Embarazo o planificación de embarazo</strong> — el folato es crítico para el desarrollo fetal</li>"
                "<li><strong>Adultos mayores</strong> — la absorción de B12 y síntesis de Vitamina D disminuyen con la edad</li>"
                "<li><strong>Uso prolongado de medicamentos</strong> — IBP, metformina, anticonvulsivos, anticoagulantes</li>"
                "<li><strong>Infecciones recurrentes o cicatrización lenta</strong> — puede reflejar estado de Vitamina D, A o E</li>"
                "</ul>"
                "<p>Su clínico puede ayudar a determinar qué análisis específicos son apropiados según sus síntomas "
                "y factores de riesgo.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs deficiente: guía rápida de patrones",
            body_html=(
                "<div class=\"blog-example\"><strong>Vitamina D — En rango:</strong> típicamente significa niveles adecuados para salud ósea e inmune.</div>"
                "<div class=\"blog-example\"><strong>Vitamina D — Baja:</strong> a menudo lleva a discutir suplementación y ajustes dietéticos.</div>"
                "<div class=\"blog-example\"><strong>Vitamina B12 — En rango:</strong> generalmente sugiere ingesta y absorción adecuadas. Resultados fronterizos pueden requerir pruebas adicionales de MMA.</div>"
                "<div class=\"blog-example\"><strong>Vitamina B12 — Baja:</strong> puede llevar a investigar problemas de absorción y considerar suplementos o inyecciones.</div>"
                "<div class=\"blog-example\"><strong>Folato — En rango:</strong> sugiere ingesta adecuada. Para mujeres planificando embarazo, a menudo se recomienda continuar suplementación.</div>"
                "<div class=\"blog-example\"><strong>Folato — Bajo:</strong> típicamente requiere revisión dietética y suplementación, con urgencia particular durante el embarazo.</div>"
                "<div class=\"blog-example\"><strong>Vitamina A — En rango:</strong> indica reservas adecuadas. Tanto deficiencia como exceso pueden causar problemas.</div>"
                "<div class=\"blog-example\"><strong>Vitamina E — En rango:</strong> sugiere protección antioxidante adecuada. La deficiencia es rara.</div>"
                "<div class=\"blog-example\"><strong>Vitamina K — En rango:</strong> función de coagulación normal. Con anticoagulantes, la ingesta consistente es clave.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Qué hacer después (con su clínico)",
            body_html=(
                "<p>Si se pregunta cómo sus niveles de vitaminas encajan en su salud general, revíselos junto con "
                "el resto de sus resultados de laboratorio. Para un resumen estructurado, puede "
                "<a href=\"/es/upload\">subir sus resultados de análisis de sangre</a>.</p>"
                "<p>Use <a href=\"/es/blood-test-results-explained\">blood test results explained</a> para un marco claro "
                "y luego el <a href=\"/es/ai-blood-test-analyzer\">AI blood test analyzer</a> para revisar la explicación "
                "junto con su clínico.</p>"
                "<p>Los niveles de vitaminas son solo una pieza de su panorama de salud. Su clínico considerará "
                "sus síntomas, dieta, estilo de vida, medicamentos y otros marcadores de laboratorio para crear un plan personalizado.</p>"
                "<p>Esta guía es educativa y no sustituye la evaluación médica.</p>"
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
