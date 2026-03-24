# -*- coding: utf-8 -*-
"""
AMH (Anti-Müllerian Hormone) blog article — full body content for all 9 languages.
Used by blog_i18n._article_amh().
Sections: intro, normal-ranges, causes, when-to-see-doctor.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_AMH_TABLE_TR = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Yaş</th><th>AMH Aralığı (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25</td><td>3,0 – 7,0</td></tr>"
    "<tr><td>28</td><td>2,5 – 6,3</td></tr>"
    "<tr><td>30</td><td>2,0 – 5,5</td></tr>"
    "<tr><td>33</td><td>1,5 – 4,5</td></tr>"
    "<tr><td>35</td><td>1,0 – 3,5</td></tr>"
    "<tr><td>38</td><td>0,7 – 2,5</td></tr>"
    "<tr><td>40</td><td>0,5 – 2,1</td></tr>"
    "<tr><td>43</td><td>0,2 – 1,0</td></tr>"
    "<tr><td>45</td><td>0,1 – 0,5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_EN = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Age</th><th>AMH Range (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25</td><td>3.0 – 7.0</td></tr>"
    "<tr><td>28</td><td>2.5 – 6.3</td></tr>"
    "<tr><td>30</td><td>2.0 – 5.5</td></tr>"
    "<tr><td>33</td><td>1.5 – 4.5</td></tr>"
    "<tr><td>35</td><td>1.0 – 3.5</td></tr>"
    "<tr><td>38</td><td>0.7 – 2.5</td></tr>"
    "<tr><td>40</td><td>0.5 – 2.1</td></tr>"
    "<tr><td>43</td><td>0.2 – 1.0</td></tr>"
    "<tr><td>45</td><td>0.1 – 0.5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_ES = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Edad</th><th>Rango de AMH (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25 años</td><td>3,0 – 7,0</td></tr>"
    "<tr><td>28 años</td><td>2,5 – 6,3</td></tr>"
    "<tr><td>30 años</td><td>2,0 – 5,5</td></tr>"
    "<tr><td>33 años</td><td>1,5 – 4,5</td></tr>"
    "<tr><td>35 años</td><td>1,0 – 3,5</td></tr>"
    "<tr><td>38 años</td><td>0,7 – 2,5</td></tr>"
    "<tr><td>40 años</td><td>0,5 – 2,1</td></tr>"
    "<tr><td>43 años</td><td>0,2 – 1,0</td></tr>"
    "<tr><td>45 años</td><td>0,1 – 0,5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_DE = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Alter</th><th>AMH-Bereich (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25 Jahre</td><td>3,0 – 7,0</td></tr>"
    "<tr><td>28 Jahre</td><td>2,5 – 6,3</td></tr>"
    "<tr><td>30 Jahre</td><td>2,0 – 5,5</td></tr>"
    "<tr><td>33 Jahre</td><td>1,5 – 4,5</td></tr>"
    "<tr><td>35 Jahre</td><td>1,0 – 3,5</td></tr>"
    "<tr><td>38 Jahre</td><td>0,7 – 2,5</td></tr>"
    "<tr><td>40 Jahre</td><td>0,5 – 2,1</td></tr>"
    "<tr><td>43 Jahre</td><td>0,2 – 1,0</td></tr>"
    "<tr><td>45 Jahre</td><td>0,1 – 0,5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_FR = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Âge</th><th>Taux AMH (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25 ans</td><td>3,0 – 7,0</td></tr>"
    "<tr><td>28 ans</td><td>2,5 – 6,3</td></tr>"
    "<tr><td>30 ans</td><td>2,0 – 5,5</td></tr>"
    "<tr><td>33 ans</td><td>1,5 – 4,5</td></tr>"
    "<tr><td>35 ans</td><td>1,0 – 3,5</td></tr>"
    "<tr><td>38 ans</td><td>0,7 – 2,5</td></tr>"
    "<tr><td>40 ans</td><td>0,5 – 2,1</td></tr>"
    "<tr><td>43 ans</td><td>0,2 – 1,0</td></tr>"
    "<tr><td>45 ans</td><td>0,1 – 0,5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_IT = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>Età</th><th>Intervallo AMH (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25 anni</td><td>3,0 – 7,0</td></tr>"
    "<tr><td>28 anni</td><td>2,5 – 6,3</td></tr>"
    "<tr><td>30 anni</td><td>2,0 – 5,5</td></tr>"
    "<tr><td>33 anni</td><td>1,5 – 4,5</td></tr>"
    "<tr><td>35 anni</td><td>1,0 – 3,5</td></tr>"
    "<tr><td>38 anni</td><td>0,7 – 2,5</td></tr>"
    "<tr><td>40 anni</td><td>0,5 – 2,1</td></tr>"
    "<tr><td>43 anni</td><td>0,2 – 1,0</td></tr>"
    "<tr><td>45 anni</td><td>0,1 – 0,5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_HE = (
    '<table class="table table-bordered table-sm mt-3 mb-3" dir="rtl">'
    "<thead><tr><th>גיל</th><th>טווח AMH&rlm; (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25</td><td>3.0 – 7.0</td></tr>"
    "<tr><td>28</td><td>2.5 – 6.3</td></tr>"
    "<tr><td>30</td><td>2.0 – 5.5</td></tr>"
    "<tr><td>33</td><td>1.5 – 4.5</td></tr>"
    "<tr><td>35</td><td>1.0 – 3.5</td></tr>"
    "<tr><td>38</td><td>0.7 – 2.5</td></tr>"
    "<tr><td>40</td><td>0.5 – 2.1</td></tr>"
    "<tr><td>43</td><td>0.2 – 1.0</td></tr>"
    "<tr><td>45</td><td>0.1 – 0.5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_HI = (
    '<table class="table table-bordered table-sm mt-3 mb-3">'
    "<thead><tr><th>उम्र</th><th>AMH रेंज (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25</td><td>3.0 – 7.0</td></tr>"
    "<tr><td>28</td><td>2.5 – 6.3</td></tr>"
    "<tr><td>30</td><td>2.0 – 5.5</td></tr>"
    "<tr><td>33</td><td>1.5 – 4.5</td></tr>"
    "<tr><td>35</td><td>1.0 – 3.5</td></tr>"
    "<tr><td>38</td><td>0.7 – 2.5</td></tr>"
    "<tr><td>40</td><td>0.5 – 2.1</td></tr>"
    "<tr><td>43</td><td>0.2 – 1.0</td></tr>"
    "<tr><td>45</td><td>0.1 – 0.5</td></tr>"
    "</tbody></table>"
)

_AMH_TABLE_AR = (
    '<table class="table table-bordered table-sm mt-3 mb-3" dir="rtl">'
    "<thead><tr><th>العمر</th><th>نطاق AMH&rlm; (ng/mL)</th></tr></thead>"
    "<tbody>"
    "<tr><td>25</td><td>3.0 – 7.0</td></tr>"
    "<tr><td>28</td><td>2.5 – 6.3</td></tr>"
    "<tr><td>30</td><td>2.0 – 5.5</td></tr>"
    "<tr><td>33</td><td>1.5 – 4.5</td></tr>"
    "<tr><td>35</td><td>1.0 – 3.5</td></tr>"
    "<tr><td>38</td><td>0.7 – 2.5</td></tr>"
    "<tr><td>40</td><td>0.5 – 2.1</td></tr>"
    "<tr><td>43</td><td>0.2 – 1.0</td></tr>"
    "<tr><td>45</td><td>0.1 – 0.5</td></tr>"
    "</tbody></table>"
)


# ─────────────────────────────────────────────────────────────────────
# TURKISH
# ─────────────────────────────────────────────────────────────────────
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="AMH kan testi: yumurtalık rezerviniz hakkında ne söylüyor?",
            body_html=(
                "<p><strong>AMH testi</strong> (anti-Müllerian hormon), yumurtalıklarda kalan yumurta "
                "havuzunun dolaylı bir göstergesi olan <strong>yumurtalık rezervi</strong>ni değerlendirmek "
                "için kullanılan bir kan testidir. Anti-Müllerian hormon, over foliküllerindeki granüloza "
                "hücreleri tarafından üretilir ve kandaki düzeyi gelişmekte olan küçük antral folikül "
                "sayısıyla orantılıdır. Bu nedenle <strong>AMH fertilitesi testi</strong> olarak da "
                "bilinir ve üreme endokrinolojisinde yaygın şekilde kullanılır.</p>"
                "<p>Menstrüel döngü boyunca nispeten sabit kalan AMH, herhangi bir döngü gününde "
                "ölçülebilir; bu özellik onu FSH veya östradiol gibi döngüye bağlı hormonlardan ayırır. "
                "<strong>AMH düzeyleri</strong> yaşla birlikte doğal olarak azalır ve menopozda sıfıra "
                "yaklaşır. Düşük veya yüksek AMH değerleri fertilite planlaması, IVF (tüp bebek) "
                "protokollerinin belirlenmesi ve polikistik over sendromu (PKOS) gibi durumların "
                "değerlendirilmesinde kritik bilgi sağlar.</p>"
                "<p>Bu rehberde <strong>yaşa göre AMH değerleri</strong>, <strong>düşük AMH</strong> "
                "veya yüksek AMH nedenlerini ve sonuçlarınız hakkında ne zaman bir uzmana başvurmanız "
                "gerektiğini öğreneceksiniz.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="AMH normal değerleri (yaşa göre)",
            body_html=(
                "<p><strong>AMH düzeyleri</strong> kadının yaşına bağlı olarak fizyolojik bir düşüş "
                "gösterir. Yumurtalık rezervi doğumda en yüksek düzeydedir; puberteden itibaren folikül "
                "havuzu sürekli küçülür ve bu süreç 35 yaşından sonra belirgin şekilde hızlanır. "
                "Aşağıdaki tabloda <strong>yaşa göre AMH normal aralıkları</strong> özetlenmiştir.</p>"
                + _AMH_TABLE_TR +
                "<p>Bu değerler genel referanslardır; laboratuvarlar arasında küçük farklılıklar "
                "görülebilir. AMH sonucunuzu kendi laboratuvarınızın referans aralığıyla "
                "karşılaştırmanız önemlidir. 1,0&nbsp;ng/mL altındaki değerler genellikle "
                "<strong>düşük yumurtalık rezervi</strong> olarak değerlendirilirken, "
                "3,5&nbsp;ng/mL üzeri değerler PKOS olasılığı açısından incelenmelidir.</p>"
                "<p>IVF planlayan hastalarda AMH düzeyi, gonadotropin dozunun ayarlanması ve beklenen "
                "oosit sayısının tahmin edilmesinde yol gösterici olur. Düşük AMH, mutlaka gebelik "
                "şansının sıfır olduğu anlamına gelmez; ancak zaman planlaması ve tedavi stratejisi "
                "açısından önemli bir veri sunar.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="AMH düşüklüğü veya yüksekliğinin nedenleri",
            body_html=(
                "<p><strong>Düşük AMH</strong> birçok farklı klinik durumla ilişkilendirilebilir. "
                "En sık karşılaşılan nedenler şunlardır:</p>"
                "<ul>"
                "<li><strong>Yaşa bağlı over rezerv azalması:</strong> En yaygın nedendir; 35 yaşından "
                "sonra folikül kaybı hızlanır.</li>"
                "<li><strong>Over cerrahisi:</strong> Endometrioma eksizyonu veya over kist "
                "operasyonları sağlıklı dokuyu azaltarak AMH düşüşüne neden olabilir.</li>"
                "<li><strong>Otoimmün ooforit:</strong> Bağışıklık sisteminin over dokusuna saldırması "
                "erken folikül kaybına yol açar.</li>"
                "<li><strong>Kemoterapi / radyoterapi:</strong> Gonadotoksik tedaviler folikül havuzunu "
                "kalıcı olarak küçültebilir.</li>"
                "<li><strong>Genetik faktörler:</strong> Frajil X premutasyonu veya Turner sendromu "
                "mozaikliği erken over yetmezliğine katkıda bulunabilir.</li>"
                "<li><strong>Sigara:</strong> Kronik sigara kullanımı over yaşlanmasını hızlandıran "
                "bilinen bir risk faktörüdür.</li>"
                "</ul>"
                "<p><strong>Yüksek AMH</strong> ise çoğunlukla <strong>polikistik over sendromu "
                "(PKOS)</strong> ile ilişkilidir. PKOS'ta çok sayıda küçük antral folikül bulunur ve "
                "bu foliküller yüksek düzeyde AMH üretir. Yüksek AMH ayrıca over hiperstimülasyon "
                "sendromu (OHSS) riski açısından IVF öncesi değerlendirmede dikkate alınır.</p>"
                "<p>AMH düzeyini yorumlarken tek başına bir değer yeterli olmayabilir; antral folikül "
                "sayısı (AFC), FSH, östradiol ve klinik öykü ile birlikte bütüncül bir değerlendirme "
                "yapılmalıdır.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlarda bir üreme endokrinolojisi uzmanına veya jinekolog "
                "danışmanız önerilir:</p>"
                "<ul>"
                "<li>Altı aydan uzun süredir düzenli ilişkiye rağmen gebe kalamıyorsanız ve 35 yaş "
                "üzerindeyseniz (35 yaş altı için bir yıl)</li>"
                "<li>AMH sonucunuz yaşınıza göre düşük çıktıysa ve fertilite planınız varsa</li>"
                "<li>Düzensiz adet döngüleri, anovülasyon şüphesi veya PKOS belirtileri yaşıyorsanız</li>"
                "<li>Kemoterapi veya over cerrahisi öncesinde fertilite koruma seçeneklerini "
                "değerlendirmek istiyorsanız</li>"
                "<li>IVF veya diğer yardımcı üreme tekniklerini planlıyorsanız</li>"
                "</ul>"
                "<p>Hekiminiz <strong>AMH testi</strong> yanında ultrason ile antral folikül sayısı, "
                "FSH, LH, östradiol ve gerekirse genetik testler isteyerek kapsamlı bir yumurtalık "
                "rezervi değerlendirmesi yapacaktır. Düşük AMH tek başına infertilite anlamına gelmez; "
                "tedavi stratejisinin zamanlaması ve bireyselleştirilmesi açısından önemli bir "
                "yol göstericidir.</p>"
                "<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi teşhis veya tedavi yerine "
                "geçmez.</strong> Tahlil sonuçlarınızı mutlaka bir sağlık profesyoneli ile değerlendirin.</p>"
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
            heading="AMH blood test: what it reveals about your ovarian reserve",
            body_html=(
                "<p>The <strong>AMH test</strong> (anti-Müllerian hormone) is a blood test used to "
                "assess <strong>ovarian reserve</strong> — an indirect measure of the remaining egg "
                "supply in the ovaries. Anti-Müllerian hormone is produced by granulosa cells in "
                "ovarian follicles, and its blood level correlates with the number of small antral "
                "follicles available for recruitment. This is why the test is widely known as an "
                "<strong>AMH fertility test</strong> and plays a central role in reproductive "
                "endocrinology.</p>"
                "<p>Unlike FSH or estradiol, <strong>AMH levels</strong> remain relatively stable "
                "throughout the menstrual cycle, so the test can be performed on any cycle day. "
                "AMH declines naturally with age and approaches zero at menopause. Both low and high "
                "values provide critical information for fertility planning, determining IVF "
                "stimulation protocols, and evaluating conditions such as polycystic ovary syndrome "
                "(PCOS).</p>"
                "<p>In this guide you will learn about the <strong>AMH normal range</strong>, "
                "<strong>AMH levels by age</strong>, the meaning of <strong>low AMH</strong> or "
                "elevated AMH, and when you should consult a specialist about your results.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="AMH normal range by age",
            body_html=(
                "<p><strong>AMH levels</strong> show a physiological decline that mirrors the gradual "
                "depletion of the ovarian follicle pool. Ovarian reserve is at its peak at birth; "
                "from puberty onward the pool steadily shrinks, and the decline accelerates notably "
                "after age 35. The table below summarises typical <strong>AMH levels by age</strong>.</p>"
                + _AMH_TABLE_EN +
                "<p>These figures are general reference values; slight differences may exist between "
                "laboratories. Always compare your result with the reference range printed on your "
                "own report. Values below 1.0&nbsp;ng/mL are generally considered indicative of "
                "<strong>low ovarian reserve</strong>, while values above 3.5&nbsp;ng/mL may warrant "
                "evaluation for PCOS.</p>"
                "<p>For patients planning IVF, the AMH level helps guide gonadotropin dosing and "
                "predict the expected oocyte yield. A <strong>low AMH</strong> result does not mean "
                "pregnancy is impossible; however, it provides valuable data for timing and "
                "individualising treatment strategy.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes of low or high AMH levels",
            body_html=(
                "<p><strong>Low AMH</strong> can be associated with a variety of clinical scenarios. "
                "The most common causes include:</p>"
                "<ul>"
                "<li><strong>Age-related decline in ovarian reserve:</strong> The most frequent cause; "
                "follicle loss accelerates after age 35.</li>"
                "<li><strong>Ovarian surgery:</strong> Excision of endometriomas or ovarian cyst "
                "removal can reduce healthy tissue and lower AMH.</li>"
                "<li><strong>Autoimmune oophoritis:</strong> The immune system attacking ovarian "
                "tissue leads to premature follicle depletion.</li>"
                "<li><strong>Chemotherapy / radiotherapy:</strong> Gonadotoxic treatments can "
                "permanently shrink the follicle pool.</li>"
                "<li><strong>Genetic factors:</strong> Fragile X premutation or Turner syndrome "
                "mosaicism may contribute to premature ovarian insufficiency.</li>"
                "<li><strong>Smoking:</strong> Chronic tobacco use is a well-established risk factor "
                "that accelerates ovarian ageing.</li>"
                "</ul>"
                "<p><strong>High AMH</strong> is most commonly associated with <strong>polycystic "
                "ovary syndrome (PCOS)</strong>. In PCOS the ovaries contain an excess of small "
                "antral follicles, each producing AMH, which drives the total level upward. Elevated "
                "AMH is also considered during pre-IVF assessment as a risk factor for ovarian "
                "hyperstimulation syndrome (OHSS).</p>"
                "<p>When interpreting AMH, a single value may not be sufficient. Antral follicle "
                "count (AFC) on ultrasound, FSH, estradiol, and clinical history should all be "
                "evaluated together for a comprehensive picture.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When should you see a doctor?",
            body_html=(
                "<p>Consider consulting a reproductive endocrinologist or gynaecologist in the "
                "following situations:</p>"
                "<ul>"
                "<li>You are over 35 and have been trying to conceive for six months without success "
                "(one year if under 35)</li>"
                "<li>Your AMH result is low for your age and you are planning a pregnancy</li>"
                "<li>You experience irregular cycles, suspected anovulation, or symptoms of PCOS</li>"
                "<li>You want to explore fertility preservation options before chemotherapy or "
                "ovarian surgery</li>"
                "<li>You are planning IVF or other assisted reproductive techniques</li>"
                "</ul>"
                "<p>Your doctor will typically order an <strong>AMH fertility test</strong> alongside "
                "an ultrasound for antral follicle count, FSH, LH, estradiol, and — if indicated — "
                "genetic testing, to build a complete ovarian reserve profile. A low AMH alone does "
                "not equal infertility; it is a guide for timing and personalising your treatment "
                "plan.</p>"
                "<p><strong>This content is for informational purposes only and does not replace "
                "medical diagnosis or treatment.</strong> Always discuss your test results with a "
                "qualified healthcare professional.</p>"
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
            heading="Prueba de AMH en sangre: qué dice sobre tu reserva ovárica",
            body_html=(
                "<p>La <strong>prueba de AMH</strong> (hormona antimülleriana) es un análisis de "
                "sangre que evalúa la <strong>reserva ovárica</strong>, es decir, una estimación "
                "indirecta del número de óvulos disponibles en los ovarios. La hormona antimülleriana "
                "es producida por las células de la granulosa de los folículos ováricos y su nivel "
                "en sangre se correlaciona con la cantidad de folículos antrales pequeños. Por ello, "
                "esta prueba se conoce como <strong>prueba de fertilidad AMH</strong> y desempeña un "
                "papel fundamental en la endocrinología reproductiva.</p>"
                "<p>A diferencia de la FSH o el estradiol, los <strong>niveles de AMH</strong> se "
                "mantienen relativamente estables a lo largo del ciclo menstrual, por lo que el "
                "análisis puede realizarse cualquier día del ciclo. La AMH disminuye de forma natural "
                "con la edad y se aproxima a cero en la menopausia. Tanto los valores bajos como los "
                "altos aportan información clave para la planificación de la fertilidad, la "
                "determinación de protocolos de estimulación en FIV y la evaluación de trastornos "
                "como el síndrome de ovario poliquístico (SOP).</p>"
                "<p>En esta guía aprenderás sobre el <strong>rango normal de AMH</strong>, los "
                "<strong>niveles de AMH por edad</strong>, el significado de una <strong>AMH "
                "baja</strong> o elevada y cuándo debes consultar a un especialista.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de AMH por edad",
            body_html=(
                "<p>Los <strong>niveles de AMH</strong> muestran una disminución fisiológica que "
                "refleja la reducción progresiva del pool de folículos ováricos. La reserva ovárica "
                "alcanza su punto máximo al nacer; desde la pubertad el pool se reduce de forma "
                "constante y la caída se acelera notablemente después de los 35 años. La siguiente "
                "tabla resume los <strong>niveles de AMH por edad</strong> habituales.</p>"
                + _AMH_TABLE_ES +
                "<p>Estos valores son referencias generales; pueden existir pequeñas diferencias "
                "entre laboratorios. Compara siempre tu resultado con el rango de referencia de tu "
                "propio informe. Valores por debajo de 1,0&nbsp;ng/mL suelen considerarse indicativos "
                "de <strong>reserva ovárica baja</strong>, mientras que valores superiores a "
                "3,5&nbsp;ng/mL pueden requerir evaluación para SOP.</p>"
                "<p>En pacientes que planifican FIV, el nivel de AMH ayuda a ajustar la dosis de "
                "gonadotropinas y predecir la cantidad de ovocitos esperada. Una <strong>AMH "
                "baja</strong> no implica que el embarazo sea imposible; sin embargo, proporciona "
                "datos valiosos para la planificación temporal y la individualización de la "
                "estrategia de tratamiento.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causas de niveles bajos o altos de AMH",
            body_html=(
                "<p>La <strong>AMH baja</strong> puede asociarse a diversos escenarios clínicos. "
                "Las causas más frecuentes son:</p>"
                "<ul>"
                "<li><strong>Disminución de la reserva ovárica por la edad:</strong> Es la causa más "
                "común; la pérdida folicular se acelera después de los 35 años.</li>"
                "<li><strong>Cirugía ovárica:</strong> La extirpación de endometriomas o quistes "
                "ováricos puede reducir el tejido sano y disminuir la AMH.</li>"
                "<li><strong>Ooforitis autoinmune:</strong> El sistema inmunitario ataca el tejido "
                "ovárico, provocando una depleción folicular prematura.</li>"
                "<li><strong>Quimioterapia / radioterapia:</strong> Los tratamientos gonadotóxicos "
                "pueden reducir permanentemente el pool folicular.</li>"
                "<li><strong>Factores genéticos:</strong> La premutación del X frágil o el mosaicismo "
                "del síndrome de Turner pueden contribuir a la insuficiencia ovárica prematura.</li>"
                "<li><strong>Tabaquismo:</strong> El consumo crónico de tabaco es un factor de riesgo "
                "reconocido que acelera el envejecimiento ovárico.</li>"
                "</ul>"
                "<p>La <strong>AMH elevada</strong> se asocia con mayor frecuencia al <strong>síndrome "
                "de ovario poliquístico (SOP)</strong>. En el SOP los ovarios contienen un exceso de "
                "folículos antrales pequeños, cada uno productor de AMH, lo que eleva el nivel total. "
                "La AMH alta también se tiene en cuenta en la evaluación pre-FIV como factor de "
                "riesgo de síndrome de hiperestimulación ovárica (SHO).</p>"
                "<p>Al interpretar la AMH, un solo valor puede no ser suficiente. El recuento de "
                "folículos antrales (RFA) por ecografía, la FSH, el estradiol y la historia clínica "
                "deben evaluarse de forma conjunta para obtener un panorama completo.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo debes consultar al médico?",
            body_html=(
                "<p>Se recomienda consultar a un especialista en reproducción o ginecólogo en las "
                "siguientes situaciones:</p>"
                "<ul>"
                "<li>Tienes más de 35 años y llevas seis meses intentando concebir sin éxito "
                "(un año si eres menor de 35)</li>"
                "<li>Tu resultado de AMH es bajo para tu edad y planeas un embarazo</li>"
                "<li>Presentas ciclos irregulares, sospecha de anovulación o síntomas de SOP</li>"
                "<li>Deseas evaluar opciones de preservación de la fertilidad antes de quimioterapia "
                "o cirugía ovárica</li>"
                "<li>Estás planificando FIV u otras técnicas de reproducción asistida</li>"
                "</ul>"
                "<p>Tu médico solicitará la <strong>prueba de fertilidad AMH</strong> junto con "
                "ecografía para el recuento de folículos antrales, FSH, LH, estradiol y, si está "
                "indicado, pruebas genéticas, para construir un perfil completo de reserva ovárica. "
                "Una AMH baja por sí sola no equivale a infertilidad; es una guía para planificar y "
                "personalizar tu tratamiento.</p>"
                "<p><strong>Este contenido es solo informativo y no sustituye el diagnóstico ni el "
                "tratamiento médico.</strong> Consulta siempre tus resultados con un profesional "
                "de la salud cualificado.</p>"
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
            heading="AMH-Bluttest: Was er über Ihre ovarielle Reserve aussagt",
            body_html=(
                "<p>Der <strong>AMH-Test</strong> (Anti-Müller-Hormon) ist eine Blutuntersuchung zur "
                "Beurteilung der <strong>ovariellen Reserve</strong> — ein indirektes Maß für den "
                "verbliebenen Eizellvorrat in den Eierstöcken. Das Anti-Müller-Hormon wird von "
                "Granulosazellen der Ovarialfollikel produziert; sein Blutspiegel korreliert mit "
                "der Anzahl kleiner Antralfollikel. Deshalb ist der Test weithin als "
                "<strong>AMH-Fertilitätstest</strong> bekannt und spielt in der "
                "Reproduktionsendokrinologie eine zentrale Rolle.</p>"
                "<p>Anders als FSH oder Östradiol bleiben die <strong>AMH-Werte</strong> während "
                "des gesamten Menstruationszyklus relativ stabil, sodass die Blutabnahme an jedem "
                "Zyklustag erfolgen kann. AMH sinkt mit zunehmendem Alter auf natürliche Weise und "
                "nähert sich in der Menopause dem Nullwert. Sowohl niedrige als auch hohe AMH-Werte "
                "liefern entscheidende Informationen für die Fertilitätsplanung, die Festlegung von "
                "IVF-Stimulationsprotokollen und die Abklärung von Erkrankungen wie dem polyzystischen "
                "Ovarialsyndrom (PCOS).</p>"
                "<p>In diesem Ratgeber erfahren Sie alles über den <strong>AMH-Normalbereich</strong>, "
                "<strong>AMH-Werte nach Alter</strong>, die Bedeutung von <strong>niedrigem AMH</strong> "
                "oder erhöhtem AMH und wann Sie einen Spezialisten aufsuchen sollten.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="AMH-Normwerte nach Alter",
            body_html=(
                "<p>Die <strong>AMH-Werte</strong> zeigen einen physiologischen Rückgang, der die "
                "fortschreitende Abnahme des ovariellen Follikelpools widerspiegelt. Die ovarielle "
                "Reserve ist bei der Geburt am höchsten; ab der Pubertät schrumpft der Pool stetig, "
                "und der Rückgang beschleunigt sich nach dem 35.&nbsp;Lebensjahr deutlich. Die "
                "folgende Tabelle fasst die typischen <strong>AMH-Werte nach Alter</strong> zusammen.</p>"
                + _AMH_TABLE_DE +
                "<p>Diese Werte sind allgemeine Referenzwerte; zwischen Laboren können geringfügige "
                "Unterschiede bestehen. Vergleichen Sie Ihr Ergebnis stets mit dem Referenzbereich "
                "auf Ihrem eigenen Befund. Werte unter 1,0&nbsp;ng/mL gelten in der Regel als Hinweis "
                "auf eine <strong>niedrige ovarielle Reserve</strong>, während Werte über "
                "3,5&nbsp;ng/mL eine Abklärung hinsichtlich PCOS nahelegen können.</p>"
                "<p>Bei Patientinnen, die eine IVF planen, hilft der AMH-Wert bei der Dosierung der "
                "Gonadotropine und der Einschätzung der erwarteten Eizellausbeute. Ein <strong>niedriger "
                "AMH-Wert</strong> bedeutet nicht, dass eine Schwangerschaft unmöglich ist; er liefert "
                "jedoch wertvolle Daten für die zeitliche Planung und Individualisierung der "
                "Behandlungsstrategie.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Ursachen für niedrige oder hohe AMH-Werte",
            body_html=(
                "<p><strong>Niedriges AMH</strong> kann mit verschiedenen klinischen Situationen "
                "zusammenhängen. Die häufigsten Ursachen sind:</p>"
                "<ul>"
                "<li><strong>Altersbedingte Abnahme der ovariellen Reserve:</strong> Die häufigste "
                "Ursache; der Follikelverlust beschleunigt sich nach dem 35.&nbsp;Lebensjahr.</li>"
                "<li><strong>Ovarialchirurgie:</strong> Die Exzision von Endometriomen oder "
                "Ovarialzysten kann gesundes Gewebe reduzieren und den AMH-Wert senken.</li>"
                "<li><strong>Autoimmune Oophoritis:</strong> Ein Angriff des Immunsystems auf "
                "Eierstockgewebe führt zu vorzeitigem Follikelverlust.</li>"
                "<li><strong>Chemotherapie / Strahlentherapie:</strong> Gonadotoxische Behandlungen "
                "können den Follikelpool dauerhaft verkleinern.</li>"
                "<li><strong>Genetische Faktoren:</strong> Die Fragile-X-Prämutation oder ein "
                "Turner-Syndrom-Mosaik können zu einer vorzeitigen Ovarialinsuffizienz "
                "beitragen.</li>"
                "<li><strong>Rauchen:</strong> Chronischer Tabakkonsum ist ein nachgewiesener "
                "Risikofaktor, der die ovarielle Alterung beschleunigt.</li>"
                "</ul>"
                "<p><strong>Hohe AMH-Werte</strong> werden am häufigsten mit dem "
                "<strong>polyzystischen Ovarialsyndrom (PCOS)</strong> in Verbindung gebracht. "
                "Bei PCOS enthalten die Eierstöcke eine übermäßige Anzahl kleiner Antralfollikel, "
                "die jeweils AMH produzieren und so den Gesamtwert in die Höhe treiben. Erhöhtes "
                "AMH wird auch bei der Bewertung vor einer IVF als Risikofaktor für ein ovarielles "
                "Hyperstimulationssyndrom (OHSS) berücksichtigt.</p>"
                "<p>Bei der Interpretation des AMH-Wertes reicht ein einzelner Wert möglicherweise "
                "nicht aus. Der Antralfollikelzählung (AFC) im Ultraschall, FSH, Östradiol und die "
                "klinische Vorgeschichte sollten gemeinsam für ein umfassendes Bild bewertet "
                "werden.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie zum Arzt gehen?",
            body_html=(
                "<p>In folgenden Situationen sollten Sie einen Reproduktionsmediziner oder "
                "Gynäkologen aufsuchen:</p>"
                "<ul>"
                "<li>Sie sind über 35 und versuchen seit sechs Monaten erfolglos schwanger zu werden "
                "(ein Jahr bei unter 35)</li>"
                "<li>Ihr AMH-Ergebnis liegt für Ihr Alter niedrig und Sie planen eine "
                "Schwangerschaft</li>"
                "<li>Sie haben unregelmäßige Zyklen, Verdacht auf Anovulation oder Symptome "
                "von PCOS</li>"
                "<li>Sie möchten vor einer Chemotherapie oder Ovarialoperation "
                "Fertilitätserhaltungsoptionen prüfen</li>"
                "<li>Sie planen eine IVF oder andere assistierte Reproduktionstechniken</li>"
                "</ul>"
                "<p>Ihr Arzt wird neben dem <strong>AMH-Fertilitätstest</strong> einen Ultraschall "
                "zur Antralfollikelzählung, FSH, LH, Östradiol und — falls angezeigt — genetische "
                "Tests anordnen, um ein vollständiges Profil der ovariellen Reserve zu erstellen. "
                "Ein niedriges AMH allein bedeutet nicht Unfruchtbarkeit; es ist ein Wegweiser für "
                "die zeitliche Planung und Individualisierung Ihres Behandlungsplans.</p>"
                "<p><strong>Dieser Inhalt dient nur zu Informationszwecken und ersetzt keine "
                "ärztliche Diagnose oder Behandlung.</strong> Besprechen Sie Ihre Testergebnisse "
                "stets mit einem qualifizierten Gesundheitsexperten.</p>"
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
            heading="Test AMH : que révèle-t-il sur votre réserve ovarienne ?",
            body_html=(
                "<p>Le <strong>test AMH</strong> (hormone anti-müllérienne) est une prise de sang "
                "permettant d'évaluer la <strong>réserve ovarienne</strong>, c'est-à-dire une "
                "estimation indirecte du nombre d'ovocytes restants dans les ovaires. L'hormone "
                "anti-müllérienne est produite par les cellules de la granulosa des follicules "
                "ovariens ; son taux sanguin est corrélé au nombre de petits follicules antraux "
                "disponibles. C'est pourquoi cette analyse est connue comme un <strong>test de "
                "fertilité AMH</strong> et occupe une place centrale en endocrinologie de la "
                "reproduction.</p>"
                "<p>Contrairement à la FSH ou à l'œstradiol, les <strong>niveaux d'AMH</strong> "
                "restent relativement stables tout au long du cycle menstruel, ce qui permet de "
                "réaliser le test n'importe quel jour du cycle. L'AMH diminue naturellement avec "
                "l'âge et s'approche de zéro à la ménopause. Des valeurs basses comme élevées "
                "fournissent des informations essentielles pour la planification de la fertilité, "
                "la définition des protocoles de stimulation en FIV et l'évaluation de troubles "
                "comme le syndrome des ovaires polykystiques (SOPK).</p>"
                "<p>Dans ce guide, vous découvrirez le <strong>taux normal d'AMH</strong>, les "
                "<strong>niveaux d'AMH par âge</strong>, la signification d'une <strong>AMH "
                "basse</strong> ou élevée et quand consulter un spécialiste.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales d'AMH selon l'âge",
            body_html=(
                "<p>Les <strong>niveaux d'AMH</strong> présentent une baisse physiologique qui "
                "reflète l'amenuisement progressif du pool de follicules ovariens. La réserve "
                "ovarienne est à son maximum à la naissance ; à partir de la puberté, le pool "
                "diminue régulièrement et le déclin s'accélère nettement après 35 ans. Le tableau "
                "ci-dessous récapitule les <strong>niveaux d'AMH par âge</strong> habituels.</p>"
                + _AMH_TABLE_FR +
                "<p>Ces chiffres sont des valeurs de référence générales ; de légères variations "
                "peuvent exister d'un laboratoire à l'autre. Comparez toujours votre résultat avec "
                "l'intervalle de référence figurant sur votre propre compte rendu. Les valeurs "
                "inférieures à 1,0&nbsp;ng/mL sont généralement considérées comme indicatrices "
                "d'une <strong>réserve ovarienne basse</strong>, tandis que les valeurs supérieures "
                "à 3,5&nbsp;ng/mL peuvent justifier un bilan pour SOPK.</p>"
                "<p>Chez les patientes envisageant une FIV, le taux d'AMH guide le dosage des "
                "gonadotrophines et permet de prédire le rendement ovocytaire attendu. Un résultat "
                "d'<strong>AMH basse</strong> ne signifie pas que la grossesse est impossible ; "
                "il fournit cependant des données précieuses pour planifier et personnaliser la "
                "stratégie de traitement.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Causes d'un taux d'AMH bas ou élevé",
            body_html=(
                "<p>Un <strong>taux d'AMH bas</strong> peut être associé à divers tableaux cliniques. "
                "Les causes les plus fréquentes sont :</p>"
                "<ul>"
                "<li><strong>Déclin lié à l'âge de la réserve ovarienne :</strong> Cause la plus "
                "courante ; la perte folliculaire s'accélère après 35 ans.</li>"
                "<li><strong>Chirurgie ovarienne :</strong> L'exérèse d'endométriomes ou de kystes "
                "ovariens peut réduire le tissu sain et abaisser l'AMH.</li>"
                "<li><strong>Ovarite auto-immune :</strong> L'attaque du tissu ovarien par le "
                "système immunitaire entraîne une déplétion folliculaire prématurée.</li>"
                "<li><strong>Chimiothérapie / radiothérapie :</strong> Les traitements gonadotoxiques "
                "peuvent réduire définitivement le pool folliculaire.</li>"
                "<li><strong>Facteurs génétiques :</strong> La prémutation de l'X fragile ou un "
                "mosaïcisme du syndrome de Turner peuvent contribuer à une insuffisance ovarienne "
                "prématurée.</li>"
                "<li><strong>Tabagisme :</strong> La consommation chronique de tabac est un facteur "
                "de risque reconnu qui accélère le vieillissement ovarien.</li>"
                "</ul>"
                "<p>Un <strong>taux d'AMH élevé</strong> est le plus souvent lié au <strong>syndrome "
                "des ovaires polykystiques (SOPK)</strong>. Dans le SOPK, les ovaires contiennent un "
                "excès de petits follicules antraux, chacun producteur d'AMH, ce qui fait grimper "
                "le taux total. Un AMH élevé est également pris en compte lors du bilan pré-FIV "
                "comme facteur de risque de syndrome d'hyperstimulation ovarienne (SHO).</p>"
                "<p>Pour interpréter l'AMH, une seule valeur peut ne pas suffire. Le comptage des "
                "follicules antraux (CFA) à l'échographie, la FSH, l'œstradiol et l'histoire "
                "clinique doivent être évalués conjointement pour un tableau complet.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Il est recommandé de consulter un spécialiste de la reproduction ou un "
                "gynécologue dans les situations suivantes :</p>"
                "<ul>"
                "<li>Vous avez plus de 35 ans et essayez de concevoir depuis six mois sans succès "
                "(un an si vous avez moins de 35 ans)</li>"
                "<li>Votre résultat d'AMH est bas pour votre âge et vous envisagez une grossesse</li>"
                "<li>Vous présentez des cycles irréguliers, une suspicion d'anovulation ou des "
                "symptômes de SOPK</li>"
                "<li>Vous souhaitez évaluer les options de préservation de la fertilité avant une "
                "chimiothérapie ou une chirurgie ovarienne</li>"
                "<li>Vous planifiez une FIV ou d'autres techniques de procréation médicalement "
                "assistée</li>"
                "</ul>"
                "<p>Votre médecin prescrira un <strong>test de fertilité AMH</strong> accompagné "
                "d'une échographie pour le comptage des follicules antraux, d'un dosage de la FSH, "
                "LH, œstradiol et, le cas échéant, de tests génétiques, afin d'établir un profil "
                "complet de la réserve ovarienne. Un AMH bas seul ne signifie pas infertilité ; "
                "c'est un guide pour planifier et personnaliser votre prise en charge.</p>"
                "<p><strong>Ce contenu est fourni à titre informatif uniquement et ne remplace pas "
                "un diagnostic ou un traitement médical.</strong> Discutez toujours de vos résultats "
                "avec un professionnel de santé qualifié.</p>"
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
            heading="Test AMH: cosa rivela sulla tua riserva ovarica",
            body_html=(
                "<p>Il <strong>test AMH</strong> (ormone anti-mülleriano) è un esame del sangue "
                "utilizzato per valutare la <strong>riserva ovarica</strong>, ossia una stima "
                "indiretta del numero di ovociti residui nelle ovaie. L'ormone anti-mülleriano è "
                "prodotto dalle cellule della granulosa dei follicoli ovarici e il suo livello "
                "ematico è correlato al numero di piccoli follicoli antrali disponibili. Per questo "
                "il test è noto anche come <strong>test di fertilità AMH</strong> e riveste un ruolo "
                "centrale nell'endocrinologia riproduttiva.</p>"
                "<p>A differenza di FSH o estradiolo, i <strong>livelli di AMH</strong> restano "
                "relativamente stabili durante il ciclo mestruale, pertanto l'esame può essere "
                "eseguito in qualsiasi giorno del ciclo. L'AMH diminuisce naturalmente con l'età e "
                "si avvicina allo zero in menopausa. Valori bassi o alti forniscono informazioni "
                "cruciali per la pianificazione della fertilità, la definizione dei protocolli di "
                "stimolazione nella fecondazione in vitro (FIV) e la valutazione di condizioni come "
                "la sindrome dell'ovaio policistico (PCOS).</p>"
                "<p>In questa guida scoprirai il <strong>range normale dell'AMH</strong>, i "
                "<strong>livelli di AMH per età</strong>, il significato di un <strong>AMH "
                "basso</strong> o elevato e quando è opportuno consultare uno specialista.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali di AMH per età",
            body_html=(
                "<p>I <strong>livelli di AMH</strong> mostrano un declino fisiologico che rispecchia "
                "la progressiva riduzione del pool follicolare ovarico. La riserva ovarica è al suo "
                "apice alla nascita; dalla pubertà in poi il pool si riduce costantemente e il calo "
                "si accelera in modo significativo dopo i 35 anni. La tabella seguente riassume i "
                "<strong>livelli di AMH per età</strong> tipici.</p>"
                + _AMH_TABLE_IT +
                "<p>Questi valori sono riferimenti generali; possono esistere lievi differenze tra "
                "laboratori. Confronta sempre il tuo risultato con l'intervallo di riferimento "
                "riportato sul tuo referto. Valori inferiori a 1,0&nbsp;ng/mL sono generalmente "
                "considerati indicativi di <strong>bassa riserva ovarica</strong>, mentre valori "
                "superiori a 3,5&nbsp;ng/mL possono richiedere un approfondimento per PCOS.</p>"
                "<p>Nelle pazienti che pianificano la FIV, il livello di AMH aiuta a calibrare il "
                "dosaggio delle gonadotropine e a prevedere la resa ovocitaria attesa. Un risultato "
                "di <strong>AMH basso</strong> non significa che la gravidanza sia impossibile; "
                "offre tuttavia dati preziosi per la tempistica e la personalizzazione della "
                "strategia terapeutica.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="Cause di livelli di AMH bassi o alti",
            body_html=(
                "<p>Un <strong>AMH basso</strong> può essere associato a diversi quadri clinici. "
                "Le cause più comuni sono:</p>"
                "<ul>"
                "<li><strong>Riduzione della riserva ovarica legata all'età:</strong> La causa più "
                "frequente; la perdita follicolare si accelera dopo i 35 anni.</li>"
                "<li><strong>Chirurgia ovarica:</strong> L'escissione di endometriomi o la rimozione "
                "di cisti ovariche può ridurre il tessuto sano e abbassare l'AMH.</li>"
                "<li><strong>Ooforite autoimmune:</strong> L'attacco del sistema immunitario al "
                "tessuto ovarico provoca una deplezione follicolare prematura.</li>"
                "<li><strong>Chemioterapia / radioterapia:</strong> I trattamenti gonadotossici "
                "possono ridurre permanentemente il pool follicolare.</li>"
                "<li><strong>Fattori genetici:</strong> La premutazione dell'X fragile o il "
                "mosaicismo della sindrome di Turner possono contribuire a un'insufficienza "
                "ovarica prematura.</li>"
                "<li><strong>Fumo:</strong> Il consumo cronico di tabacco è un fattore di rischio "
                "riconosciuto che accelera l'invecchiamento ovarico.</li>"
                "</ul>"
                "<p>Un <strong>AMH elevato</strong> è associato più comunemente alla <strong>sindrome "
                "dell'ovaio policistico (PCOS)</strong>. Nella PCOS le ovaie contengono un eccesso "
                "di piccoli follicoli antrali, ciascuno produttore di AMH, il che innalza il livello "
                "totale. Un AMH alto viene considerato anche nella valutazione pre-FIV come fattore "
                "di rischio per la sindrome da iperstimolazione ovarica (OHSS).</p>"
                "<p>Nell'interpretazione dell'AMH, un singolo valore può non essere sufficiente. "
                "Il conteggio dei follicoli antrali (AFC) ecografico, FSH, estradiolo e storia "
                "clinica devono essere valutati congiuntamente per un quadro completo.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Si consiglia di consultare uno specialista in medicina della riproduzione o un "
                "ginecologo nelle seguenti situazioni:</p>"
                "<ul>"
                "<li>Hai più di 35 anni e stai cercando una gravidanza da sei mesi senza successo "
                "(un anno se hai meno di 35 anni)</li>"
                "<li>Il tuo risultato di AMH è basso per la tua età e stai pianificando una "
                "gravidanza</li>"
                "<li>Presenti cicli irregolari, sospetta anovulazione o sintomi di PCOS</li>"
                "<li>Desideri valutare opzioni di preservazione della fertilità prima di "
                "chemioterapia o chirurgia ovarica</li>"
                "<li>Stai pianificando FIV o altre tecniche di procreazione medicalmente "
                "assistita</li>"
                "</ul>"
                "<p>Il tuo medico prescriverà un <strong>test di fertilità AMH</strong> affiancato "
                "da ecografia per il conteggio dei follicoli antrali, FSH, LH, estradiolo e, se "
                "indicato, test genetici, per costruire un profilo completo della riserva ovarica. "
                "Un AMH basso da solo non equivale a infertilità; è una guida per la tempistica e "
                "la personalizzazione del piano terapeutico.</p>"
                "<p><strong>Questo contenuto è a solo scopo informativo e non sostituisce una "
                "diagnosi o un trattamento medico.</strong> Discuti sempre i tuoi risultati con un "
                "professionista sanitario qualificato.</p>"
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
            heading="בדיקת AMH בדם: מה היא מגלה על הרזרבה השחלתית שלך?",
            body_html=(
                "<p><strong>בדיקת AMH</strong> (הורמון אנטי-מילריאני) היא בדיקת דם המשמשת "
                "להערכת <strong>הרזרבה השחלתית</strong> — מדד עקיף למספר הביציות הנותרות "
                "בשחלות. ההורמון האנטי-מילריאני מיוצר על ידי תאי גרנולוזה בזקיקי השחלה, "
                "ורמתו בדם מתואמת עם מספר הזקיקים האנטרליים הקטנים הזמינים לגיוס. לכן "
                "הבדיקה מוכרת כ<strong>בדיקת פוריות AMH</strong> וממלאת תפקיד מרכזי "
                "באנדוקרינולוגיה של הפריון.</p>"
                "<p>בשונה מ-FSH או אסטרדיול, <strong>רמות AMH</strong> נותרות יציבות יחסית "
                "לאורך המחזור החודשי, כך שניתן לבצע את הבדיקה בכל יום של המחזור. AMH יורד "
                "באופן טבעי עם הגיל ומתקרב לאפס בגיל המעבר. ערכים נמוכים או גבוהים מספקים "
                "מידע קריטי לתכנון פוריות, לקביעת פרוטוקולי גירוי ב-IVF ולהערכת מצבים כמו "
                "תסמונת השחלות הפוליציסטיות (PCOS).</p>"
                "<p>במדריך זה תלמדו על <strong>טווח הנורמה של AMH</strong>, "
                "<strong>רמות AMH לפי גיל</strong>, המשמעות של <strong>AMH נמוך</strong> "
                "או מוגבר ומתי כדאי להתייעץ עם מומחה.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי נורמה של AMH לפי גיל",
            body_html=(
                "<p><strong>רמות AMH</strong> מראות ירידה פיזיולוגית המשקפת את הדלדול "
                "ההדרגתי של מאגר הזקיקים השחלתי. הרזרבה השחלתית נמצאת בשיאה בלידה; "
                "מגיל ההתבגרות המאגר מצטמצם בהתמדה, והירידה מואצת באופן ניכר לאחר גיל "
                "35. הטבלה שלהלן מסכמת את <strong>רמות AMH לפי גיל</strong> האופייניות.</p>"
                + _AMH_TABLE_HE +
                "<p>ערכים אלה הם ייחוס כללי; עשויים להיות הבדלים קלים בין מעבדות. השוו תמיד "
                "את התוצאה שלכם לטווח הייחוס שבדוח שלכם. ערכים מתחת ל-1.0&nbsp;ng/mL נחשבים "
                "בדרך כלל כמעידים על <strong>רזרבה שחלתית נמוכה</strong>, בעוד ערכים מעל "
                "3.5&nbsp;ng/mL עשויים להצדיק בירור ל-PCOS.</p>"
                "<p>בחולות המתכננות IVF, רמת ה-AMH מסייעת בהתאמת מינון הגונדוטרופינים "
                "ובחיזוי תפוקת הביציות הצפויה. תוצאת <strong>AMH נמוך</strong> אינה אומרת "
                "שהריון בלתי אפשרי; אולם היא מספקת נתונים חשובים לתזמון ולהתאמה אישית של "
                "אסטרטגיית הטיפול.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="גורמים לרמות AMH נמוכות או גבוהות",
            body_html=(
                "<p><strong>AMH נמוך</strong> עשוי להיות קשור למגוון מצבים קליניים. "
                "הגורמים השכיחים ביותר כוללים:</p>"
                "<ul>"
                "<li><strong>ירידה ברזרבה השחלתית הקשורה לגיל:</strong> הגורם השכיח ביותר; "
                "אובדן הזקיקים מואץ לאחר גיל 35.</li>"
                "<li><strong>ניתוח שחלתי:</strong> הסרת אנדומטריומות או ציסטות שחלתיות עלולה "
                "לצמצם רקמה בריאה ולהוריד את ה-AMH.</li>"
                "<li><strong>דלקת שחלות אוטואימונית:</strong> תקיפת מערכת החיסון ברקמת השחלה "
                "מובילה לדלדול זקיקים מוקדם.</li>"
                "<li><strong>כימותרפיה / הקרנות:</strong> טיפולים גונדוטוקסיים עלולים לצמצם "
                "את מאגר הזקיקים באופן קבוע.</li>"
                "<li><strong>גורמים גנטיים:</strong> פרה-מוטציה של X שביר או מוזאיציזם של "
                "תסמונת טרנר עלולים לתרום לאי-ספיקה שחלתית מוקדמת.</li>"
                "<li><strong>עישון:</strong> שימוש כרוני בטבק הוא גורם סיכון מוכח המאיץ את "
                "הזדקנות השחלות.</li>"
                "</ul>"
                "<p><strong>AMH גבוה</strong> קשור בדרך כלל ל<strong>תסמונת השחלות "
                "הפוליציסטיות (PCOS)</strong>. ב-PCOS השחלות מכילות עודף של זקיקים אנטרליים "
                "קטנים, שכל אחד מהם מייצר AMH ובכך מעלה את הרמה הכוללת. AMH מוגבר נלקח "
                "בחשבון גם בהערכה לפני IVF כגורם סיכון לתסמונת היפרסטימולציה שחלתית "
                "(OHSS).</p>"
                "<p>בפרשנות AMH, ערך בודד עשוי שלא להספיק. ספירת זקיקים אנטרליים (AFC) "
                "באולטרסאונד, FSH, אסטרדיול והיסטוריה רפואית צריכים להיות מוערכים יחד לתמונה "
                "מקיפה.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>מומלץ להתייעץ עם רופא מומחה לפריון או גינקולוג במצבים הבאים:</p>"
                "<ul>"
                "<li>אתן מעל גיל 35 ומנסות להיכנס להריון שישה חודשים ללא הצלחה "
                "(שנה אם מתחת ל-35)</li>"
                "<li>תוצאת ה-AMH שלכן נמוכה ביחס לגילכן ואתן מתכננות הריון</li>"
                "<li>יש לכן מחזורים לא סדירים, חשד לחוסר ביוץ או תסמינים של PCOS</li>"
                "<li>אתן רוצות לבחון אפשרויות לשימור פוריות לפני כימותרפיה או ניתוח "
                "שחלתי</li>"
                "<li>אתן מתכננות IVF או טכניקות פריון מסייעות אחרות</li>"
                "</ul>"
                "<p>הרופא שלכן יזמין <strong>בדיקת פוריות AMH</strong> לצד אולטרסאונד "
                "לספירת זקיקים אנטרליים, FSH, LH, אסטרדיול ובמידת הצורך בדיקות גנטיות, "
                "לבניית פרופיל מלא של הרזרבה השחלתית. AMH נמוך בלבד אינו שווה לאי-פוריות; "
                "הוא מדריך לתזמון ולהתאמה אישית של תוכנית הטיפול שלכן.</p>"
                "<p><strong>תוכן זה מיועד למטרות מידע בלבד ואינו מחליף אבחנה או טיפול "
                "רפואי.</strong> דונו תמיד בתוצאות הבדיקות שלכן עם איש מקצוע רפואי "
                "מוסמך.</p>"
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
            heading="AMH ब्लड टेस्ट: यह आपकी ओवेरियन रिज़र्व के बारे में क्या बताता है?",
            body_html=(
                "<p><strong>AMH टेस्ट</strong> (एंटी-मुलेरियन हार्मोन) एक ब्लड टेस्ट है जिसका "
                "उपयोग <strong>ओवेरियन रिज़र्व</strong> — यानी अंडाशय में बचे अंडों की अनुमानित "
                "संख्या — का आकलन करने के लिए किया जाता है। एंटी-मुलेरियन हार्मोन ओवेरियन "
                "फ़ॉलिकल्स की ग्रैनुलोसा कोशिकाओं द्वारा बनाया जाता है और इसका ब्लड लेवल "
                "उपलब्ध छोटे एंट्रल फ़ॉलिकल्स की संख्या से संबंधित होता है। इसी कारण इसे "
                "<strong>AMH फ़र्टिलिटी टेस्ट</strong> भी कहा जाता है और रिप्रोडक्टिव "
                "एंडोक्रिनोलॉजी में इसकी केंद्रीय भूमिका है।</p>"
                "<p>FSH या एस्ट्राडायोल के विपरीत, <strong>AMH लेवल</strong> मासिक चक्र के "
                "दौरान अपेक्षाकृत स्थिर रहते हैं, इसलिए यह टेस्ट चक्र के किसी भी दिन किया जा "
                "सकता है। AMH उम्र के साथ स्वाभाविक रूप से घटता है और मेनोपॉज़ में शून्य के "
                "करीब पहुँच जाता है। कम या ज़्यादा AMH वैल्यू फ़र्टिलिटी प्लानिंग, IVF "
                "स्टिमुलेशन प्रोटोकॉल तय करने और पॉलीसिस्टिक ओवरी सिंड्रोम (PCOS) जैसी "
                "स्थितियों के मूल्यांकन में महत्वपूर्ण जानकारी देते हैं।</p>"
                "<p>इस गाइड में आप <strong>AMH का नॉर्मल रेंज</strong>, <strong>उम्र के "
                "अनुसार AMH लेवल</strong>, <strong>कम AMH</strong> या बढ़े हुए AMH का अर्थ "
                "और कब किसी विशेषज्ञ से मिलना चाहिए, यह जानेंगे।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="उम्र के अनुसार AMH के नॉर्मल वैल्यू",
            body_html=(
                "<p><strong>AMH लेवल</strong> में एक फ़िज़ियोलॉजिकल गिरावट होती है जो ओवेरियन "
                "फ़ॉलिकल पूल के क्रमिक क्षरण को दर्शाती है। ओवेरियन रिज़र्व जन्म के समय "
                "अपने उच्चतम स्तर पर होती है; प्यूबर्टी के बाद से पूल लगातार सिकुड़ता है और "
                "35 साल की उम्र के बाद गिरावट तेज़ हो जाती है। नीचे दी गई तालिका में "
                "<strong>उम्र के अनुसार AMH लेवल</strong> के सामान्य मान दिए गए हैं।</p>"
                + _AMH_TABLE_HI +
                "<p>ये सामान्य रेफ़रेंस वैल्यू हैं; लैब के बीच मामूली अंतर हो सकते हैं। "
                "अपनी रिपोर्ट पर छपी रेफ़रेंस रेंज से हमेशा तुलना करें। 1.0&nbsp;ng/mL "
                "से कम वैल्यू आमतौर पर <strong>कम ओवेरियन रिज़र्व</strong> मानी जाती है, "
                "जबकि 3.5&nbsp;ng/mL से ज़्यादा वैल्यू में PCOS का मूल्यांकन ज़रूरी हो "
                "सकता है।</p>"
                "<p>IVF प्लान करने वाली मरीज़ों में AMH लेवल गोनैडोट्रोपिन की डोज़ तय करने "
                "और अपेक्षित ऊसाइट यील्ड का अनुमान लगाने में मदद करता है। <strong>कम "
                "AMH</strong> का मतलब यह नहीं कि प्रेगनेंसी असंभव है; हालाँकि यह ट्रीटमेंट "
                "स्ट्रैटजी की टाइमिंग और पर्सनलाइज़ेशन के लिए महत्वपूर्ण डेटा देता है।</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="कम या ज़्यादा AMH लेवल के कारण",
            body_html=(
                "<p><strong>कम AMH</strong> कई क्लिनिकल स्थितियों से जुड़ा हो सकता है। "
                "सबसे आम कारणों में शामिल हैं:</p>"
                "<ul>"
                "<li><strong>उम्र से संबंधित ओवेरियन रिज़र्व में कमी:</strong> सबसे सामान्य "
                "कारण; 35 साल के बाद फ़ॉलिकल लॉस तेज़ हो जाता है।</li>"
                "<li><strong>ओवेरियन सर्जरी:</strong> एंडोमेट्रिओमा या ओवेरियन सिस्ट "
                "हटाने से स्वस्थ टिशू कम हो सकता है और AMH गिर सकता है।</li>"
                "<li><strong>ऑटोइम्यून ऊफ़ोराइटिस:</strong> इम्यून सिस्टम का ओवेरियन "
                "टिशू पर हमला करना समय से पहले फ़ॉलिकल डिप्लीशन का कारण बनता है।</li>"
                "<li><strong>कीमोथेरेपी / रेडियोथेरेपी:</strong> गोनैडोटॉक्सिक उपचार "
                "फ़ॉलिकल पूल को स्थायी रूप से छोटा कर सकते हैं।</li>"
                "<li><strong>आनुवंशिक कारक:</strong> फ़्रैजाइल X प्रीम्यूटेशन या टर्नर "
                "सिंड्रोम मोज़ेसिज़्म प्रीमैच्योर ओवेरियन इनसफ़िशिएंसी में योगदान कर "
                "सकते हैं।</li>"
                "<li><strong>धूम्रपान:</strong> लंबे समय तक तंबाकू का उपयोग एक सिद्ध "
                "जोखिम कारक है जो ओवेरियन एजिंग को तेज़ करता है।</li>"
                "</ul>"
                "<p><strong>ज़्यादा AMH</strong> सबसे अधिक <strong>पॉलीसिस्टिक ओवरी "
                "सिंड्रोम (PCOS)</strong> से जुड़ा होता है। PCOS में अंडाशय में अत्यधिक "
                "छोटे एंट्रल फ़ॉलिकल्स होते हैं, जिनमें से प्रत्येक AMH बनाता है, जिससे "
                "कुल लेवल बढ़ जाता है। बढ़ा हुआ AMH IVF से पहले के मूल्यांकन में ओवेरियन "
                "हाइपरस्टिमुलेशन सिंड्रोम (OHSS) के जोखिम कारक के रूप में भी देखा "
                "जाता है।</p>"
                "<p>AMH की व्याख्या करते समय अकेला एक वैल्यू पर्याप्त नहीं हो सकता। "
                "अल्ट्रासाउंड पर एंट्रल फ़ॉलिकल काउंट (AFC), FSH, एस्ट्राडायोल और "
                "क्लिनिकल हिस्ट्री — सभी को मिलाकर समग्र मूल्यांकन किया जाना चाहिए।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>निम्नलिखित स्थितियों में किसी रिप्रोडक्टिव एंडोक्रिनोलॉजिस्ट या "
                "गायनेकोलॉजिस्ट से परामर्श लें:</p>"
                "<ul>"
                "<li>आप 35 से ज़्यादा उम्र की हैं और छह महीने से गर्भधारण की कोशिश कर "
                "रही हैं बिना सफलता के (35 से कम उम्र में एक साल)</li>"
                "<li>आपकी AMH वैल्यू आपकी उम्र के लिए कम है और आप प्रेगनेंसी प्लान कर "
                "रही हैं</li>"
                "<li>अनियमित पीरियड्स, एनोव्यूलेशन का संदेह या PCOS के लक्षण हैं</li>"
                "<li>कीमोथेरेपी या ओवेरियन सर्जरी से पहले फ़र्टिलिटी प्रिज़र्वेशन के "
                "विकल्प जानना चाहती हैं</li>"
                "<li>IVF या अन्य असिस्टेड रिप्रोडक्टिव तकनीकों की योजना बना रही हैं</li>"
                "</ul>"
                "<p>आपके डॉक्टर <strong>AMH फ़र्टिलिटी टेस्ट</strong> के साथ-साथ एंट्रल "
                "फ़ॉलिकल काउंट के लिए अल्ट्रासाउंड, FSH, LH, एस्ट्राडायोल और ज़रूरत "
                "पड़ने पर जेनेटिक टेस्ट कराएँगे ताकि ओवेरियन रिज़र्व का पूरा प्रोफ़ाइल "
                "बन सके। अकेले कम AMH का मतलब इनफ़र्टिलिटी नहीं है; यह ट्रीटमेंट प्लान "
                "की टाइमिंग और पर्सनलाइज़ेशन के लिए एक गाइड है।</p>"
                "<p><strong>यह सामग्री केवल जानकारी के उद्देश्य से है; यह चिकित्सा निदान "
                "या उपचार का विकल्प नहीं है।</strong> अपनी टेस्ट रिपोर्ट हमेशा किसी "
                "योग्य स्वास्थ्य पेशेवर से चर्चा करें।</p>"
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
            heading="تحليل AMH في الدم: ماذا يكشف عن مخزون المبيض لديك؟",
            body_html=(
                "<p><strong>تحليل AMH</strong> (الهرمون المضاد لمولر) هو فحص دم يُستخدم لتقييم "
                "<strong>مخزون المبيض</strong> — وهو مقياس غير مباشر لعدد البويضات المتبقية في "
                "المبيضين. يُنتَج الهرمون المضاد لمولر من قِبل خلايا الحبيبية في الجُريبات "
                "المبيضية، ويرتبط مستواه في الدم بعدد الجريبات الغارّية الصغيرة المتاحة. لذلك "
                "يُعرف هذا الفحص أيضاً بـ<strong>اختبار خصوبة AMH</strong> ويلعب دوراً محورياً "
                "في طب الغدد الصماء التناسلية.</p>"
                "<p>على عكس FSH أو الإستراديول، تبقى <strong>مستويات AMH</strong> مستقرة نسبياً "
                "طوال الدورة الشهرية، مما يتيح إجراء الفحص في أي يوم من أيام الدورة. ينخفض "
                "AMH بشكل طبيعي مع التقدم في العمر ويقترب من الصفر عند انقطاع الطمث. تقدم "
                "القيم المنخفضة والمرتفعة على حدٍّ سواء معلومات حيوية لتخطيط الخصوبة وتحديد "
                "بروتوكولات تحفيز أطفال الأنابيب (IVF) وتقييم حالات مثل متلازمة تكيّس المبايض "
                "(PCOS).</p>"
                "<p>في هذا الدليل ستتعرفون على <strong>النطاق الطبيعي لـ AMH</strong>، "
                "<strong>مستويات AMH حسب العمر</strong>، معنى <strong>AMH المنخفض</strong> "
                "أو المرتفع ومتى يجب استشارة أخصائي.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية لـ AMH حسب العمر",
            body_html=(
                "<p>تُظهر <strong>مستويات AMH</strong> انخفاضاً فسيولوجياً يعكس النضوب "
                "التدريجي لمخزون الجريبات المبيضية. يبلغ مخزون المبيض ذروته عند الولادة؛ "
                "ومن سن البلوغ يتقلّص المخزون باستمرار، ويتسارع الانخفاض بشكل ملحوظ بعد "
                "سن 35. يلخّص الجدول أدناه <strong>مستويات AMH حسب العمر</strong> "
                "النموذجية.</p>"
                + _AMH_TABLE_AR +
                "<p>هذه الأرقام هي قيم مرجعية عامة؛ قد توجد اختلافات طفيفة بين المختبرات. "
                "قارني دائماً نتيجتك بالنطاق المرجعي المطبوع في تقريرك. تُعتبر القيم الأقل "
                "من 1.0&nbsp;ng/mL عادةً مؤشراً على <strong>مخزون مبيضي منخفض</strong>، "
                "بينما القيم الأعلى من 3.5&nbsp;ng/mL قد تستدعي تقييماً لمتلازمة تكيّس "
                "المبايض.</p>"
                "<p>بالنسبة للمريضات اللواتي يخططن لأطفال الأنابيب، يساعد مستوى AMH في "
                "تعديل جرعة الغونادوتروبينات والتنبؤ بعدد البويضات المتوقع. نتيجة "
                "<strong>AMH منخفض</strong> لا تعني أن الحمل مستحيل؛ لكنها توفر بيانات "
                "قيّمة للتوقيت وتخصيص استراتيجية العلاج.</p>"
            ),
        ),
        Section(
            id="causes", level=2,
            heading="أسباب انخفاض أو ارتفاع مستويات AMH",
            body_html=(
                "<p>قد يرتبط <strong>AMH المنخفض</strong> بمجموعة متنوعة من السيناريوهات "
                "السريرية. تشمل الأسباب الأكثر شيوعاً:</p>"
                "<ul>"
                "<li><strong>انخفاض مخزون المبيض المرتبط بالعمر:</strong> السبب الأكثر شيوعاً؛ "
                "تتسارع خسارة الجريبات بعد سن 35.</li>"
                "<li><strong>جراحة المبيض:</strong> استئصال الأورام البطانية الرحمية أو أكياس "
                "المبيض قد يقلل من الأنسجة السليمة ويخفض AMH.</li>"
                "<li><strong>التهاب المبيض المناعي الذاتي:</strong> مهاجمة الجهاز المناعي "
                "لأنسجة المبيض تؤدي إلى نضوب مبكر للجريبات.</li>"
                "<li><strong>العلاج الكيميائي / الإشعاعي:</strong> العلاجات السامة للغدد "
                "التناسلية قد تقلّص مخزون الجريبات بشكل دائم.</li>"
                "<li><strong>عوامل وراثية:</strong> الطفرة الأولية للكروموسوم X الهش أو "
                "فسيفساء متلازمة تيرنر قد تساهم في قصور المبيض المبكر.</li>"
                "<li><strong>التدخين:</strong> الاستخدام المزمن للتبغ عامل خطر ثابت يُسرّع "
                "شيخوخة المبيض.</li>"
                "</ul>"
                "<p>يرتبط <strong>AMH المرتفع</strong> غالباً بـ<strong>متلازمة تكيّس "
                "المبايض (PCOS)</strong>. في PCOS يحتوي المبيضان على فائض من الجريبات "
                "الغارّية الصغيرة، ينتج كلٌّ منها AMH مما يرفع المستوى الكلي. يُؤخذ AMH "
                "المرتفع بالاعتبار أيضاً في التقييم قبل أطفال الأنابيب كعامل خطر لمتلازمة "
                "فرط تحفيز المبيض (OHSS).</p>"
                "<p>عند تفسير AMH، قد لا يكون قيمة واحدة كافية. يجب تقييم عدد الجريبات "
                "الغارّية (AFC) بالموجات فوق الصوتية وFSH والإستراديول والتاريخ السريري "
                "معاً للحصول على صورة شاملة.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>يُنصح باستشارة أخصائي طب الإنجاب أو طبيب النساء والتوليد في الحالات "
                "التالية:</p>"
                "<ul>"
                "<li>عمرك أكثر من 35 سنة وتحاولين الحمل منذ ستة أشهر دون نجاح "
                "(سنة إذا كنتِ أقل من 35)</li>"
                "<li>نتيجة AMH لديكِ منخفضة بالنسبة لعمرك وتخططين للحمل</li>"
                "<li>تعانين من دورات غير منتظمة أو اشتباه بانعدام الإباضة أو أعراض PCOS</li>"
                "<li>ترغبين في استكشاف خيارات حفظ الخصوبة قبل العلاج الكيميائي أو جراحة "
                "المبيض</li>"
                "<li>تخططين لأطفال الأنابيب أو تقنيات إنجابية مساعدة أخرى</li>"
                "</ul>"
                "<p>سيطلب طبيبك <strong>اختبار خصوبة AMH</strong> إلى جانب تصوير بالموجات "
                "فوق الصوتية لعدّ الجريبات الغارّية، وتحاليل FSH وLH والإستراديول، وعند "
                "الحاجة فحوصات وراثية، لبناء ملف شامل لمخزون المبيض. AMH منخفض وحده لا "
                "يعني العقم؛ إنه دليل لتوقيت وتخصيص خطة العلاج الخاصة بك.</p>"
                "<p><strong>هذا المحتوى لأغراض إعلامية فقط ولا يحلّ محلّ التشخيص أو العلاج "
                "الطبي.</strong> ناقشي دائماً نتائج فحوصاتك مع متخصص رعاية صحية مؤهل.</p>"
            ),
        ),
    ]


# ═════════════════════════════════════════════════════════════════════
# PUBLIC HELPERS
# ═════════════════════════════════════════════════════════════════════

def get_amh_sections_by_lang() -> dict:
    """Returns sections_by_lang dict for AMH article (all 9 languages)."""
    builders = {
        "tr": _sections_tr, "en": _sections_en, "es": _sections_es,
        "de": _sections_de, "fr": _sections_fr, "it": _sections_it,
        "he": _sections_he, "hi": _sections_hi, "ar": _sections_ar,
    }
    return {lang: fn() for lang, fn in builders.items()}


def get_amh_faq_schema_qa() -> dict:
    """Returns faq_schema_qa dict for AMH article (all 9 languages, 3 Q&A each)."""
    return {
        "tr": [
            {"question": "AMH testi nedir ve neden yapılır?",
             "answer": "AMH testi, kandaki anti-Müllerian hormon düzeyini ölçerek yumurtalık rezervini değerlendiren bir kan testidir. Fertilite planlaması, IVF öncesi değerlendirme, PKOS tanısı ve over cerrahisi öncesi yumurtalık kapasitesinin belirlenmesi için sıklıkla istenir."},
            {"question": "Yaşa göre normal AMH değeri nedir?",
             "answer": "AMH düzeyleri yaşla birlikte düşer. 25 yaşında ortalama 3,0–7,0 ng/mL, 30 yaşında 2,0–5,5 ng/mL, 35 yaşında 1,0–3,5 ng/mL, 40 yaşında 0,5–2,1 ng/mL ve 45 yaşında 0,1–0,5 ng/mL civarındadır. Sonuçlar laboratuvarın referans aralığıyla karşılaştırılmalıdır."},
            {"question": "Düşük AMH ne anlama gelir?",
             "answer": "Düşük AMH, yumurtalık rezervinin azaldığını gösterir. Yaşa bağlı doğal azalma, over cerrahisi, kemoterapi, otoimmün durumlar veya genetik faktörler nedeniyle olabilir. Düşük AMH gebelik şansını ortadan kaldırmaz ancak tedavi stratejisinin zamanlama ve bireyselleştirilmesi açısından klinisyeniniz için önemli bir veridir."},
        ],
        "en": [
            {"question": "What is an AMH test and why is it done?",
             "answer": "An AMH test measures the level of anti-Müllerian hormone in the blood to assess ovarian reserve — the estimated number of eggs remaining in the ovaries. It is commonly ordered for fertility planning, pre-IVF assessment, PCOS evaluation, and to gauge ovarian capacity before surgery or chemotherapy."},
            {"question": "What is a normal AMH level by age?",
             "answer": "AMH levels decline with age. Typical ranges are approximately 3.0–7.0 ng/mL at age 25, 2.0–5.5 ng/mL at 30, 1.0–3.5 ng/mL at 35, 0.5–2.1 ng/mL at 40, and 0.1–0.5 ng/mL at 45. Results should always be compared with your laboratory's reference range."},
            {"question": "What does a low AMH level mean?",
             "answer": "A low AMH level indicates diminished ovarian reserve. It can result from natural age-related decline, ovarian surgery, chemotherapy, autoimmune conditions, or genetic factors. Low AMH does not eliminate the chance of pregnancy but is an important data point for timing and personalising treatment."},
        ],
        "es": [
            {"question": "¿Qué es la prueba de AMH y por qué se realiza?",
             "answer": "La prueba de AMH mide el nivel de la hormona antimülleriana en sangre para evaluar la reserva ovárica, es decir, la cantidad estimada de óvulos que quedan en los ovarios. Se solicita habitualmente para planificación de la fertilidad, evaluación pre-FIV, diagnóstico de SOP y para valorar la capacidad ovárica antes de cirugía o quimioterapia."},
            {"question": "¿Cuál es un nivel normal de AMH según la edad?",
             "answer": "Los niveles de AMH disminuyen con la edad. Los rangos típicos son aproximadamente 3,0–7,0 ng/mL a los 25 años, 2,0–5,5 ng/mL a los 30, 1,0–3,5 ng/mL a los 35, 0,5–2,1 ng/mL a los 40 y 0,1–0,5 ng/mL a los 45. Compara siempre tu resultado con el rango de referencia de tu laboratorio."},
            {"question": "¿Qué significa un nivel bajo de AMH?",
             "answer": "Un nivel bajo de AMH indica una reserva ovárica disminuida. Puede deberse al declive natural por la edad, cirugía ovárica, quimioterapia, afecciones autoinmunes o factores genéticos. Una AMH baja no elimina la posibilidad de embarazo, pero es un dato importante para la planificación temporal y la personalización del tratamiento."},
        ],
        "de": [
            {"question": "Was ist ein AMH-Test und warum wird er durchgeführt?",
             "answer": "Ein AMH-Test misst den Spiegel des Anti-Müller-Hormons im Blut, um die ovarielle Reserve zu beurteilen — die geschätzte Anzahl verbleibender Eizellen in den Eierstöcken. Er wird häufig zur Fertilitätsplanung, vor einer IVF, zur PCOS-Abklärung und zur Einschätzung der Eierstockkapazität vor Operationen oder Chemotherapie angeordnet."},
            {"question": "Was ist ein normaler AMH-Wert nach Alter?",
             "answer": "Die AMH-Werte sinken mit dem Alter. Typische Bereiche liegen bei etwa 3,0–7,0 ng/mL mit 25 Jahren, 2,0–5,5 ng/mL mit 30, 1,0–3,5 ng/mL mit 35, 0,5–2,1 ng/mL mit 40 und 0,1–0,5 ng/mL mit 45. Vergleichen Sie Ihr Ergebnis stets mit dem Referenzbereich Ihres Labors."},
            {"question": "Was bedeutet ein niedriger AMH-Wert?",
             "answer": "Ein niedriger AMH-Wert weist auf eine verminderte ovarielle Reserve hin. Ursachen können der natürliche altersbedingte Rückgang, Ovarialoperation, Chemotherapie, Autoimmunerkrankungen oder genetische Faktoren sein. Niedriges AMH schließt eine Schwangerschaft nicht aus, ist aber ein wichtiger Datenpunkt für die zeitliche Planung und Individualisierung der Behandlung."},
        ],
        "fr": [
            {"question": "Qu'est-ce que le test AMH et pourquoi est-il réalisé ?",
             "answer": "Le test AMH mesure le taux de l'hormone anti-müllérienne dans le sang afin d'évaluer la réserve ovarienne — le nombre estimé d'ovocytes restants dans les ovaires. Il est couramment prescrit pour la planification de la fertilité, le bilan pré-FIV, le diagnostic du SOPK et l'évaluation de la capacité ovarienne avant chirurgie ou chimiothérapie."},
            {"question": "Quel est un taux normal d'AMH selon l'âge ?",
             "answer": "Les taux d'AMH diminuent avec l'âge. Les fourchettes typiques sont d'environ 3,0–7,0 ng/mL à 25 ans, 2,0–5,5 ng/mL à 30 ans, 1,0–3,5 ng/mL à 35 ans, 0,5–2,1 ng/mL à 40 ans et 0,1–0,5 ng/mL à 45 ans. Comparez toujours votre résultat avec l'intervalle de référence de votre laboratoire."},
            {"question": "Que signifie un taux bas d'AMH ?",
             "answer": "Un taux bas d'AMH indique une réserve ovarienne diminuée. Il peut résulter du déclin naturel lié à l'âge, d'une chirurgie ovarienne, d'une chimiothérapie, de maladies auto-immunes ou de facteurs génétiques. Un AMH bas n'élimine pas la possibilité de grossesse mais est une donnée essentielle pour le calendrier et la personnalisation du traitement."},
        ],
        "it": [
            {"question": "Cos'è il test AMH e perché viene eseguito?",
             "answer": "Il test AMH misura il livello dell'ormone anti-mülleriano nel sangue per valutare la riserva ovarica — il numero stimato di ovociti rimasti nelle ovaie. Viene comunemente prescritto per la pianificazione della fertilità, la valutazione pre-FIV, la diagnosi di PCOS e per valutare la capacità ovarica prima di interventi chirurgici o chemioterapia."},
            {"question": "Qual è un valore normale di AMH per età?",
             "answer": "I livelli di AMH diminuiscono con l'età. I range tipici sono circa 3,0–7,0 ng/mL a 25 anni, 2,0–5,5 ng/mL a 30, 1,0–3,5 ng/mL a 35, 0,5–2,1 ng/mL a 40 e 0,1–0,5 ng/mL a 45. Confronta sempre il tuo risultato con l'intervallo di riferimento del tuo laboratorio."},
            {"question": "Cosa significa un livello basso di AMH?",
             "answer": "Un livello basso di AMH indica una riserva ovarica ridotta. Può derivare dal naturale declino legato all'età, da chirurgia ovarica, chemioterapia, condizioni autoimmuni o fattori genetici. Un AMH basso non esclude la possibilità di gravidanza ma è un dato importante per la tempistica e la personalizzazione del trattamento."},
        ],
        "he": [
            {"question": "מהי בדיקת AMH ולמה היא מבוצעת?",
             "answer": "בדיקת AMH מודדת את רמת ההורמון האנטי-מילריאני בדם כדי להעריך את הרזרבה השחלתית — המספר המשוער של ביציות שנותרו בשחלות. היא מבוצעת לתכנון פוריות, הערכה לפני IVF, אבחון PCOS ולהערכת כושר השחלות לפני ניתוח או כימותרפיה."},
            {"question": "מהי רמת AMH תקינה לפי גיל?",
             "answer": "רמות AMH יורדות עם הגיל. טווחים אופייניים הם כ-3.0–7.0 ng/mL בגיל 25, 2.0–5.5 ng/mL בגיל 30, 1.0–3.5 ng/mL בגיל 35, 0.5–2.1 ng/mL בגיל 40 ו-0.1–0.5 ng/mL בגיל 45. יש להשוות תמיד את התוצאה לטווח הייחוס של המעבדה שלכם."},
            {"question": "מה המשמעות של AMH נמוך?",
             "answer": "AMH נמוך מעיד על רזרבה שחלתית מופחתת. הוא יכול לנבוע מירידה טבעית הקשורה לגיל, ניתוח שחלתי, כימותרפיה, מצבים אוטואימוניים או גורמים גנטיים. AMH נמוך אינו שולל אפשרות להריון אך הוא נתון חשוב לתזמון ולהתאמה אישית של הטיפול."},
        ],
        "hi": [
            {"question": "AMH टेस्ट क्या है और यह क्यों किया जाता है?",
             "answer": "AMH टेस्ट ब्लड में एंटी-मुलेरियन हार्मोन के लेवल को मापता है ताकि ओवेरियन रिज़र्व — अंडाशय में बचे अंडों की अनुमानित संख्या — का आकलन किया जा सके। इसे आमतौर पर फ़र्टिलिटी प्लानिंग, IVF से पहले मूल्यांकन, PCOS निदान और सर्जरी या कीमोथेरेपी से पहले ओवेरियन क्षमता जानने के लिए कराया जाता है।"},
            {"question": "उम्र के अनुसार सामान्य AMH लेवल क्या है?",
             "answer": "AMH लेवल उम्र के साथ घटता है। सामान्य रेंज लगभग 25 साल में 3.0–7.0 ng/mL, 30 में 2.0–5.5 ng/mL, 35 में 1.0–3.5 ng/mL, 40 में 0.5–2.1 ng/mL और 45 में 0.1–0.5 ng/mL होती है। अपनी रिपोर्ट पर छपी रेफ़रेंस रेंज से हमेशा तुलना करें।"},
            {"question": "कम AMH लेवल का क्या मतलब है?",
             "answer": "कम AMH लेवल ओवेरियन रिज़र्व में कमी का संकेत देता है। यह उम्र संबंधी प्राकृतिक गिरावट, ओवेरियन सर्जरी, कीमोथेरेपी, ऑटोइम्यून स्थितियों या आनुवंशिक कारकों के कारण हो सकता है। कम AMH प्रेगनेंसी की संभावना को ख़त्म नहीं करता, लेकिन ट्रीटमेंट की टाइमिंग और पर्सनलाइज़ेशन के लिए एक महत्वपूर्ण डेटा पॉइंट है।"},
        ],
        "ar": [
            {"question": "ما هو تحليل AMH ولماذا يُجرى؟",
             "answer": "تحليل AMH يقيس مستوى الهرمون المضاد لمولر في الدم لتقييم مخزون المبيض — العدد التقديري للبويضات المتبقية في المبيضين. يُطلب عادةً لتخطيط الخصوبة، وتقييم ما قبل أطفال الأنابيب، وتشخيص تكيّس المبايض، ولتقدير قدرة المبيض قبل الجراحة أو العلاج الكيميائي."},
            {"question": "ما هو المستوى الطبيعي لـ AMH حسب العمر؟",
             "answer": "تنخفض مستويات AMH مع التقدم في العمر. النطاقات النموذجية هي تقريباً 3.0–7.0 ng/mL في سن 25، و2.0–5.5 ng/mL في سن 30، و1.0–3.5 ng/mL في سن 35، و0.5–2.1 ng/mL في سن 40، و0.1–0.5 ng/mL في سن 45. قارني دائماً نتيجتك بالنطاق المرجعي الخاص بمختبرك."},
            {"question": "ماذا يعني انخفاض مستوى AMH؟",
             "answer": "يشير انخفاض AMH إلى تراجع مخزون المبيض. قد ينتج عن الانخفاض الطبيعي المرتبط بالعمر أو جراحة المبيض أو العلاج الكيميائي أو حالات مناعية ذاتية أو عوامل وراثية. انخفاض AMH لا يلغي فرصة الحمل لكنه نقطة بيانات مهمة لتوقيت وتخصيص خطة العلاج."},
        ],
    }
