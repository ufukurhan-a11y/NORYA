"""Pillar blog article: Thyroid Panel Explained — comprehensive guide.

Registered in blog_i18n.py as a pillar content piece for SEO.
"""
from datetime import date


def _thyroid_sections_en():
    from app.blog_i18n import Section
    return [
        Section(id="section-what-is-thyroid-panel", level=2, heading="What Is a Thyroid Panel?",
                body_html="<p>A thyroid panel is a group of blood tests that evaluate how well your thyroid gland is functioning. The thyroid is a small, butterfly-shaped gland in your neck that produces hormones controlling metabolism, energy, body temperature, heart rate, and more.</p><p>A standard thyroid panel typically includes <strong>TSH</strong>, <strong>Free T4</strong>, and sometimes <strong>Free T3</strong>, <strong>Total T4</strong>, <strong>TPO antibodies</strong>, and <strong>thyroglobulin antibodies</strong>. Understanding these values is crucial because thyroid disorders affect an estimated 200 million people worldwide.</p>"),
        Section(id="section-tsh", level=2, heading="TSH (Thyroid Stimulating Hormone)",
                body_html="<p>TSH is produced by the pituitary gland and tells your thyroid how much hormone to make. It's the <strong>most important screening test</strong> for thyroid function.</p><div class='blog-definition'><strong>Normal range:</strong> 0.4–4.0 mIU/L (may vary by lab)</div><p><strong>High TSH</strong> means your thyroid is underactive (hypothyroidism) — your pituitary is working harder to stimulate a sluggish thyroid. Symptoms: fatigue, weight gain, cold intolerance, dry skin, constipation.</p><p><strong>Low TSH</strong> means your thyroid is overactive (hyperthyroidism) — your pituitary is suppressed because thyroid hormone levels are already too high. Symptoms: weight loss, anxiety, rapid heartbeat, heat intolerance, tremor.</p><div class='blog-example'><strong>Important:</strong> TSH works inversely to thyroid hormones. High TSH = low thyroid function. Low TSH = high thyroid function. This confuses many patients.</div>"),
        Section(id="section-free-t4", level=2, heading="Free T4 (Thyroxine)",
                body_html="<p>T4 is the main hormone produced by the thyroid. \"Free\" T4 measures the unbound, active form available for your body to use.</p><div class='blog-definition'><strong>Normal range:</strong> 0.8–1.8 ng/dL (or 10–23 pmol/L)</div><p><strong>Low Free T4</strong> with high TSH confirms <strong>hypothyroidism</strong>. <strong>High Free T4</strong> with low TSH confirms <strong>hyperthyroidism</strong>. When Free T4 is normal but TSH is abnormal, it's called <em>subclinical</em> thyroid disease.</p>"),
        Section(id="section-free-t3", level=2, heading="Free T3 (Triiodothyronine)",
                body_html="<p>T3 is the more biologically active thyroid hormone. Most T3 is converted from T4 in your body's tissues. Free T3 measures the unbound, active form.</p><div class='blog-definition'><strong>Normal range:</strong> 2.3–4.2 pg/mL (or 3.5–6.5 pmol/L)</div><p>T3 is especially important in diagnosing hyperthyroidism, as some patients have elevated T3 even when T4 is normal (<em>T3 thyrotoxicosis</em>). Low T3 can occur with severe illness, malnutrition, or certain medications.</p>"),
        Section(id="section-antibodies", level=2, heading="Thyroid Antibodies: TPO & Thyroglobulin",
                body_html="<p>Thyroid antibodies indicate autoimmune thyroid disease — the most common cause of thyroid disorders in developed countries.</p><ul><li><strong>TPO Antibodies (Anti-TPO)</strong>: Present in ~95% of Hashimoto's thyroiditis (autoimmune hypothyroidism) and ~75% of Graves' disease. Normal: &lt; 35 IU/mL.</li><li><strong>Thyroglobulin Antibodies (Anti-Tg)</strong>: Present in 60-80% of Hashimoto's and used to monitor thyroid cancer recurrence.</li><li><strong>TSH Receptor Antibodies (TRAb/TSI)</strong>: Specific for Graves' disease (autoimmune hyperthyroidism).</li></ul><p>Having positive antibodies doesn't always mean you have active disease — some people have elevated antibodies for years before developing thyroid dysfunction.</p>"),
        Section(id="section-hypothyroid", level=2, heading="Understanding Hypothyroidism",
                body_html="<p>Hypothyroidism (underactive thyroid) is the most common thyroid disorder. Your thyroid doesn't produce enough hormones.</p><p><strong>Key lab pattern:</strong> High TSH + Low Free T4</p><p><strong>Common symptoms:</strong></p><ul><li>Fatigue and sluggishness</li><li>Weight gain despite normal eating</li><li>Cold intolerance</li><li>Dry skin and hair</li><li>Constipation</li><li>Depression</li><li>Muscle weakness</li><li>Elevated cholesterol</li></ul><p><strong>Common causes:</strong> Hashimoto's thyroiditis (autoimmune), iodine deficiency, thyroid surgery, radiation therapy, certain medications (lithium, amiodarone).</p>"),
        Section(id="section-hyperthyroid", level=2, heading="Understanding Hyperthyroidism",
                body_html="<p>Hyperthyroidism (overactive thyroid) means your thyroid produces too much hormone, speeding up your metabolism.</p><p><strong>Key lab pattern:</strong> Low TSH + High Free T4 (and/or high Free T3)</p><p><strong>Common symptoms:</strong></p><ul><li>Unintended weight loss</li><li>Rapid or irregular heartbeat</li><li>Anxiety and irritability</li><li>Tremor in hands and fingers</li><li>Increased sweating and heat intolerance</li><li>Frequent bowel movements</li><li>Difficulty sleeping</li></ul><p><strong>Common causes:</strong> Graves' disease (autoimmune), toxic nodular goiter, thyroiditis, excessive iodine intake.</p>"),
        Section(id="section-subclinical", level=2, heading="Subclinical Thyroid Disease",
                body_html="<p>Subclinical thyroid disease is when TSH is abnormal but Free T4 and T3 are still in the normal range. It's extremely common and often debated among endocrinologists.</p><p><strong>Subclinical hypothyroidism:</strong> TSH 4.5–10 mIU/L with normal Free T4. Affects 5-10% of the population. May or may not require treatment — discuss with your doctor.</p><p><strong>Subclinical hyperthyroidism:</strong> TSH below 0.4 mIU/L with normal Free T4/T3. Less common. May increase risk of atrial fibrillation and osteoporosis.</p>"),
        Section(id="section-when-to-test", level=2, heading="When Should You Get a Thyroid Panel?",
                body_html="<p>Consider thyroid testing if you experience:</p><ul><li>Unexplained fatigue or energy changes</li><li>Significant weight changes</li><li>Temperature sensitivity (always cold or always hot)</li><li>Hair loss or skin changes</li><li>Family history of thyroid disease</li><li>Pregnancy or planning pregnancy</li><li>Age over 60 (routine screening recommended)</li><li>History of autoimmune disease</li></ul><p>Women are 5-8 times more likely to develop thyroid disease than men.</p>"),
        Section(id="section-norya-thyroid", level=2, heading="How NoryaAI Analyzes Your Thyroid Panel",
                body_html="<p>NoryaAI reads your complete thyroid panel and provides:</p><ul><li>Clear interpretation of TSH, Free T4, Free T3, and antibody levels</li><li>Pattern recognition (hypothyroid vs hyperthyroid vs subclinical)</li><li>Comparison against age-specific reference ranges</li><li>Plain-language explanations of what your results mean</li><li>Doctor-ready summary with flagged abnormal values</li></ul><p>Upload your lab results and get your thyroid panel analysis in minutes — no medical jargon, just clear answers.</p>"),
    ]


def _thyroid_sections_tr():
    from app.blog_i18n import Section
    return [
        Section(id="section-what-is-thyroid-panel", level=2, heading="Tiroid Panel Testi Nedir?",
                body_html="<p>Tiroid paneli, tiroid bezinizin ne kadar iyi çalıştığını değerlendiren bir grup kan testidir. Tiroid, boynunuzdaki kelebek şeklinde küçük bir bezdir ve metabolizma, enerji, vücut ısısı, kalp hızı ve daha fazlasını kontrol eden hormonlar üretir.</p><p>Standart bir tiroid paneli genellikle <strong>TSH</strong>, <strong>Serbest T4</strong> ve bazen <strong>Serbest T3</strong>, <strong>TPO antikorları</strong> ve <strong>tiroglobulin antikorlarını</strong> içerir.</p>"),
        Section(id="section-tsh", level=2, heading="TSH (Tiroid Uyarıcı Hormon)",
                body_html="<p>TSH, hipofiz bezi tarafından üretilir ve tiroidinize ne kadar hormon üretmesi gerektiğini söyler. Tiroid fonksiyonu için <strong>en önemli tarama testidir</strong>.</p><div class='blog-definition'><strong>Normal aralık:</strong> 0,4–4,0 mIU/L</div><p><strong>Yüksek TSH</strong> tiroidinizin az çalıştığını (hipotiroidizm) gösterir. Belirtiler: yorgunluk, kilo alma, soğuk hassasiyeti, kuru cilt.</p><p><strong>Düşük TSH</strong> tiroidinizin aşırı çalıştığını (hipertiroidizm) gösterir. Belirtiler: kilo kaybı, anksiyete, hızlı kalp atışı, sıcak hassasiyeti.</p>"),
        Section(id="section-free-t4", level=2, heading="Serbest T4 (Tiroksin)",
                body_html="<p>T4, tiroid tarafından üretilen ana hormondur. Serbest T4, vücudunuzun kullanabildiği bağlanmamış aktif formu ölçer.</p><div class='blog-definition'><strong>Normal aralık:</strong> 0,8–1,8 ng/dL</div><p>Düşük Serbest T4 + Yüksek TSH = <strong>Hipotiroidizm</strong>. Yüksek Serbest T4 + Düşük TSH = <strong>Hipertiroidizm</strong>.</p>"),
        Section(id="section-free-t3", level=2, heading="Serbest T3 (Triiyodotironin)",
                body_html="<p>T3, biyolojik olarak daha aktif tiroid hormonudur. Çoğu T3, vücut dokularında T4'ten dönüştürülür.</p><div class='blog-definition'><strong>Normal aralık:</strong> 2,3–4,2 pg/mL</div><p>T3, özellikle hipertiroidizm tanısında önemlidir.</p>"),
        Section(id="section-antibodies", level=2, heading="Tiroid Antikorları: TPO ve Tiroglobulin",
                body_html="<p>Tiroid antikorları, otoimmün tiroid hastalığını gösterir.</p><ul><li><strong>Anti-TPO</strong>: Hashimoto tiroiditinin %95'inde bulunur. Normal: &lt; 35 IU/mL.</li><li><strong>Anti-Tiroglobulin</strong>: Hashimoto'nun %60-80'inde bulunur.</li></ul><p>Pozitif antikorlara sahip olmak her zaman aktif hastalık anlamına gelmez.</p>"),
        Section(id="section-hypothyroid", level=2, heading="Hipotiroidizmi Anlamak",
                body_html="<p>Hipotiroidizm (az çalışan tiroid), en yaygın tiroid bozukluğudur.</p><p><strong>Laboratuvar paterni:</strong> Yüksek TSH + Düşük Serbest T4</p><p><strong>Yaygın belirtiler:</strong> Yorgunluk, kilo alma, soğuk hassasiyeti, kuru cilt ve saç, kabızlık, depresyon, kas güçsüzlüğü.</p><p><strong>Yaygın nedenler:</strong> Hashimoto tiroiditi (otoimmün), iyot eksikliği, tiroid ameliyatı, radyasyon tedavisi.</p>"),
        Section(id="section-hyperthyroid", level=2, heading="Hipertiroidizmi Anlamak",
                body_html="<p>Hipertiroidizm (aşırı çalışan tiroid), tiroidinizin çok fazla hormon ürettiği anlamına gelir.</p><p><strong>Laboratuvar paterni:</strong> Düşük TSH + Yüksek Serbest T4</p><p><strong>Yaygın belirtiler:</strong> İstem dışı kilo kaybı, hızlı veya düzensiz kalp atışı, anksiyete, el titremesi, aşırı terleme.</p><p><strong>Yaygın nedenler:</strong> Graves hastalığı (otoimmün), toksik nodüler guatr, tiroidit.</p>"),
        Section(id="section-norya-thyroid", level=2, heading="NoryaAI Tiroid Panelinizi Nasıl Analiz Eder?",
                body_html="<p>NoryaAI tiroid panelinizin tamamını okur ve şunları sağlar:</p><ul><li>TSH, Serbest T4, Serbest T3 ve antikor seviyelerinin net yorumu</li><li>Hipotiroid / hipertiroid / subklinik patern tanıma</li><li>Yaşa özel referans aralıklarıyla karşılaştırma</li><li>Anormal değerlerin işaretlendiği doktora hazır özet</li></ul><p>Lab sonuçlarınızı yükleyin ve tiroid panel analizinizi dakikalar içinde alın.</p>"),
    ]


def build_thyroid_article():
    """Build the Thyroid Panel Pillar Article. Called from blog_i18n.py."""
    from app.blog_i18n import Article
    return Article(
        id="thyroid-panel-guide",
        published_at=date(2026, 3, 24),
        read_minutes=14,
        cover_image="/static/images/blog/rdw-hero.jpg",
        category={"en": "Thyroid", "tr": "Tiroid"},
        slugs={"en": "thyroid-panel-explained-guide", "tr": "tiroid-panel-rehberi"},
        titles={
            "en": "Thyroid Panel Explained: TSH, T3, T4 & Antibodies Guide",
            "tr": "Tiroid Panel Testi Rehberi: TSH, T3, T4 ve Antikorlar",
        },
        subtitles={
            "en": "Understand your thyroid panel results — TSH, Free T4, Free T3, TPO antibodies — and learn what they mean for your health.",
            "tr": "Tiroid panel sonuçlarınızı anlayın — TSH, Serbest T4, Serbest T3, TPO antikorları — ve sağlığınız için ne anlama geldiklerini öğrenin.",
        },
        excerpts={
            "en": "A complete guide to understanding your thyroid panel: TSH, Free T4, Free T3, antibodies, hypothyroidism, and hyperthyroidism explained.",
            "tr": "Tiroid panelinizi anlamak için kapsamlı rehber: TSH, Serbest T4, T3, antikorlar, hipotiroidizm ve hipertiroidizm açıklandı.",
        },
        seo_titles={
            "en": "Thyroid Panel Explained: TSH, T3, T4, Antibodies Guide 2026 | NoryaAI",
            "tr": "Tiroid Panel Testi Rehberi: TSH, T3, T4, Antikorlar 2026 | NoryaAI",
        },
        seo_descriptions={
            "en": "Complete guide to thyroid panel tests. Understand TSH, Free T4, Free T3, TPO antibodies, hypothyroidism, and hyperthyroidism with normal ranges.",
            "tr": "Tiroid panel testleri rehberi. TSH, Serbest T4, Serbest T3, TPO antikorları, hipotiroidizm ve hipertiroidizm hakkında bilgi edinin.",
        },
        sections_by_lang={
            "en": _thyroid_sections_en(),
            "tr": _thyroid_sections_tr(),
        },
        last_updated=date(2026, 3, 24),
        faq_schema_qa={
            "en": [
                {"question": "What is a normal TSH level?", "answer": "Normal TSH is typically 0.4-4.0 mIU/L. High TSH indicates hypothyroidism (underactive thyroid), while low TSH indicates hyperthyroidism (overactive thyroid)."},
                {"question": "What is the difference between T3 and T4?", "answer": "T4 (thyroxine) is the main hormone produced by the thyroid. T3 (triiodothyronine) is more biologically active. Most T3 is converted from T4 in body tissues."},
                {"question": "What do thyroid antibodies mean?", "answer": "Positive thyroid antibodies (TPO, thyroglobulin) indicate autoimmune thyroid disease, most commonly Hashimoto's thyroiditis. They can be present years before symptoms develop."},
                {"question": "How often should thyroid be checked?", "answer": "Adults over 35 should be screened every 5 years. Those with symptoms, family history, or known thyroid disease may need more frequent testing."},
            ],
            "tr": [
                {"question": "Normal TSH değeri nedir?", "answer": "Normal TSH genellikle 0,4-4,0 mIU/L arasıdır. Yüksek TSH hipotiroidizmi, düşük TSH hipertiroidizmi gösterir."},
                {"question": "T3 ve T4 arasındaki fark nedir?", "answer": "T4 tiroid tarafından üretilen ana hormondur. T3 biyolojik olarak daha aktiftir. Çoğu T3, vücut dokularında T4'ten dönüştürülür."},
                {"question": "Tiroid antikorları ne anlama gelir?", "answer": "Pozitif tiroid antikorları (TPO, tiroglobulin) otoimmün tiroid hastalığını, en yaygın olarak Hashimoto tiroiditini gösterir."},
            ],
        },
    )
