"""Blog article for metabolic panel / CMP / BMP intent."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what a metabolic panel tells you",
            body_html=(
                "<p>A <strong>metabolic panel</strong> is a blood test that groups together "
                "markers related to blood sugar, electrolytes, kidney function, and in the "
                "case of a <strong>Comprehensive Metabolic Panel (CMP)</strong>, liver and "
                "protein markers as well. A <strong>Basic Metabolic Panel (BMP)</strong> is "
                "shorter and usually focuses on glucose, sodium, potassium, chloride, "
                "bicarbonate/CO<sub>2</sub>, calcium, BUN, and creatinine.</p>"
                "<p>Doctors do not interpret the panel as a single score. They compare each "
                "marker with the others to decide whether the pattern looks more related to "
                "hydration, kidney function, glucose control, acid-base balance, liver "
                "stress, or a temporary lab variation.</p>"
            ),
        ),
        Section(
            id="cmp-vs-bmp",
            level=2,
            heading="CMP vs BMP: what is the difference?",
            body_html=(
                "<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\">"
                "<thead><tr class=\"bg-slate-50\">"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Panel</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">What it usually includes</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Typical use</th>"
                "</tr></thead><tbody>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>BMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Glucose, electrolytes, calcium, BUN, creatinine, CO<sub>2</sub>/bicarbonate</td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Hydration, kidney function, electrolyte or acid-base checks</td></tr>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>CMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Everything in a BMP plus albumin, total protein, ALP, ALT, AST, and bilirubin</td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Broader metabolic overview including liver and protein markers</td></tr>"
                "</tbody></table>"
                "<p>If your report says <strong>CMP</strong>, you are usually getting a broader "
                "chemistry overview than a BMP. The exact panel can still vary by lab, so the "
                "best reference is the list of markers shown on your own report.</p>"
            ),
        ),
        Section(
            id="how-doctors-read-it",
            level=2,
            heading="How doctors read a metabolic panel in real life",
            body_html=(
                "<p>Most of the value comes from the <strong>pattern</strong>, not one isolated number. "
                "Examples:</p>"
                "<ul>"
                "<li><strong>Glucose</strong> is often compared with <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c</a> and sometimes fasting insulin or <a href=\"/en/blog/what-is-homa-ir\">HOMA-IR</a>.</li>"
                "<li><strong>BUN, creatinine, and eGFR</strong> are reviewed together to understand kidney function and hydration. See <a href=\"/en/blog/creatinine-egfr-what-it-means\">creatinine and eGFR explained</a>.</li>"
                "<li><strong>Sodium, potassium, chloride, and bicarbonate</strong> help doctors think about fluid balance, medications, and acid-base patterns. Related guides: <a href=\"/en/blog/sodium-low-meaning\">low sodium</a> and <a href=\"/en/blog/potassium-high-meaning\">high potassium</a>.</li>"
                "<li><strong>ALT, AST, ALP, bilirubin, albumin, and total protein</strong> give liver and protein context. Start with <a href=\"/en/blog/what-do-high-alt-and-ast-levels-mean\">high ALT/AST</a>, <a href=\"/en/blog/albumin-low-meaning\">low albumin</a>, and <a href=\"/en/blog/total-protein-high-or-low\">total protein</a>.</li>"
                "</ul>"
                "<p>This is why a metabolic panel is often one of the most useful first-step blood "
                "tests: it connects several systems at once rather than looking at only one biomarker.</p>"
            ),
        ),
        Section(
            id="normal-high-low",
            level=2,
            heading="Normal, mildly abnormal, and clearly abnormal patterns",
            body_html=(
                "<div class=\"blog-example\"><strong>Mostly in range:</strong> Often reassuring, but doctors still compare with symptoms, trend, and why the test was ordered.</div>"
                "<div class=\"blog-example\"><strong>One mild out-of-range result:</strong> Can reflect dehydration, fasting status, medication effect, or lab variation. Repeat testing is common before drawing conclusions.</div>"
                "<div class=\"blog-example\"><strong>Several related markers move together:</strong> More likely to prompt a focused kidney, glucose, liver, or electrolyte work-up.</div>"
                "<div class=\"blog-example\"><strong>Clearly abnormal or symptomatic pattern:</strong> Needs faster review, especially with high potassium, very low sodium, markedly high glucose, or worsening kidney markers.</div>"
            ),
        ),
        Section(
            id="fasting-prep",
            level=2,
            heading="Do you need to fast before a metabolic panel?",
            body_html=(
                "<p>For many labs, a metabolic panel itself does <strong>not always require fasting</strong>, "
                "but fasting may be recommended if the same blood draw also includes glucose-focused or lipid testing. "
                "If your clinician wants fasting glucose, lipid values, or insulin resistance markers interpreted "
                "together, following the lab instructions matters.</p>"
                "<p>Also tell your clinician about supplements, creatine, diuretics, blood pressure medicines, "
                "or recent vomiting, diarrhea, intense exercise, or dehydration, because these can influence results.</p>"
            ),
        ),
        Section(
            id="follow-up",
            level=2,
            heading="What follow-up is common after an abnormal metabolic panel?",
            body_html=(
                "<p>Common next steps depend on which part of the panel is abnormal:</p>"
                "<ul>"
                "<li>Repeat the same chemistry panel if the result may be temporary or affected by hydration.</li>"
                "<li>Add kidney follow-up such as <a href=\"/en/tools/egfr-calculator\">eGFR calculation</a>, <a href=\"/en/blog/urine-acr-microalbumin-meaning\">urine ACR</a>, or blood pressure review.</li>"
                "<li>Add glucose follow-up such as <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c</a>, fasting glucose review, or insulin resistance context.</li>"
                "<li>Add liver or protein-focused follow-up if ALT, AST, ALP, bilirubin, albumin, or total protein are off.</li>"
                "</ul>"
                "<p>An abnormal panel is a signal to interpret in context, not a diagnosis by itself.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="How to use this with your own report",
            body_html=(
                "<p>If your lab report includes a BMP or CMP and you want the full picture, "
                "start with <a href=\"/en/blood-test-results-explained\">blood test results explained</a> "
                "or <a href=\"/en/upload-blood-test-results\">upload your blood test results</a> for a "
                "structured summary. If you are comparing general-purpose AI tools, see the "
                "<a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a> page for how NoryaAI "
                "is tailored to lab reports rather than generic prompting.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This guide is for educational purposes only.</strong> A metabolic panel "
                "cannot diagnose a condition on its own. Always review abnormal results with a "
                "qualified clinician, especially if you have symptoms, repeat abnormalities, or "
                "multiple markers moving together.</p>"
            ),
        ),
    ]


def _sections_tr():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Kısa cevap: metabolik panel ne gösterir?",
            body_html=(
                "<p><strong>Metabolik panel</strong>, kan şekeri, elektrolitler, böbrek fonksiyonu "
                "ve <strong>Kapsamlı Metabolik Panel (CMP)</strong> söz konusuysa karaciğer ile protein "
                "belirteçlerini birlikte gösteren bir kan testidir. <strong>Temel Metabolik Panel "
                "(BMP)</strong> daha kısa bir versiyondur; genelde glukoz, sodyum, potasyum, klor, "
                "bikarbonat/CO<sub>2</sub>, kalsiyum, üre ve kreatinin gibi değerleri içerir.</p>"
                "<p>Doktorlar bu paneli tek bir puan gibi yorumlamaz. Değerleri birlikte okuyarak "
                "tablonun daha çok hidrasyon, böbrek fonksiyonu, glukoz kontrolü, asit-baz dengesi, "
                "karaciğer stresi veya geçici laboratuvar değişkenliği ile mi ilişkili olduğuna bakarlar.</p>"
            ),
        ),
        Section(
            id="cmp-vs-bmp",
            level=2,
            heading="CMP ile BMP arasındaki fark nedir?",
            body_html=(
                "<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\">"
                "<thead><tr class=\"bg-slate-50\">"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Panel</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Genelde neleri içerir?</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Ne için kullanılır?</th>"
                "</tr></thead><tbody>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>BMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Glukoz, elektrolitler, kalsiyum, üre, kreatinin, bikarbonat/CO<sub>2</sub></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Hidrasyon, böbrek fonksiyonu, elektrolit ve asit-baz dengesi</td></tr>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>CMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">BMP içeriğine ek olarak albümin, total protein, ALP, ALT, AST ve bilirubin</td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Karaciğer ve protein belirteçleriyle daha geniş metabolik değerlendirme</td></tr>"
                "</tbody></table>"
                "<p>Raporunuzda <strong>CMP</strong> yazıyorsa, çoğu zaman BMP'ye göre daha geniş "
                "bir biyokimya özeti alıyorsunuz demektir. Yine de paneller laboratuvara göre "
                "değişebileceğinden en doğru referans kendi raporunuzdaki parametre listesidir.</p>"
            ),
        ),
        Section(
            id="how-doctors-read-it",
            level=2,
            heading="Doktorlar metabolik paneli pratikte nasıl okur?",
            body_html=(
                "<p>Asıl değer çoğu zaman tek bir sayıda değil, <strong>örüntüde</strong> yatar. Örnekler:</p>"
                "<ul>"
                "<li><strong>Glukoz</strong> genelde <a href=\"/tr/blog/hba1c-sonucu-ne-anlama-gelir\">HbA1c</a> ve bazen <a href=\"/tr/blog/homa-ir-nedir\">HOMA-IR</a> ile birlikte değerlendirilir.</li>"
                "<li><strong>Üre, kreatinin ve eGFR</strong> böbrek fonksiyonu ile hidrasyonu anlamak için birlikte okunur. Bkz. <a href=\"/tr/blog/creatinine-egfr-what-it-means\">kreatinin ve eGFR</a>.</li>"
                "<li><strong>Sodyum, potasyum, klor ve bikarbonat</strong> sıvı dengesi, ilaç etkisi ve asit-baz tablosu hakkında fikir verir. İlgili içerikler: <a href=\"/tr/blog/sodium-low-meaning\">düşük sodyum</a> ve <a href=\"/tr/blog/potassium-high-meaning\">yüksek potasyum</a>.</li>"
                "<li><strong>ALT, AST, ALP, bilirubin, albümin ve total protein</strong> karaciğer ve protein bağlamı sağlar. Başlangıç için <a href=\"/tr/blog/alt-ve-ast-yuksekligi-neyi-gosterir\">ALT/AST yüksekliği</a>, <a href=\"/tr/blog/albumin-low-meaning\">düşük albümin</a> ve <a href=\"/tr/blog/total-protein-high-or-low\">total protein</a> içeriklerine bakabilirsiniz.</li>"
                "</ul>"
                "<p>Bu yüzden metabolik panel, tek bir biyobelirtece bakmak yerine birden fazla sistemi "
                "aynı anda bağlayan en yararlı ilk basamak testlerden biridir.</p>"
            ),
        ),
        Section(
            id="normal-high-low",
            level=2,
            heading="Normal, hafif anormal ve belirgin anormal örüntüler",
            body_html=(
                "<div class=\"blog-example\"><strong>Değerlerin çoğu normal:</strong> Genelde rahatlatıcıdır; yine de belirtiler, trend ve testin neden istendiği önemlidir.</div>"
                "<div class=\"blog-example\"><strong>Tek bir değer hafif sapmış:</strong> Susuzluk, açlık durumu, ilaç etkisi veya laboratuvar değişkenliği ile ilişkili olabilir. Sonuca atlamadan tekrar test sık görülür.</div>"
                "<div class=\"blog-example\"><strong>İlişkili birkaç belirteç birlikte değişmiş:</strong> Böbrek, glukoz, karaciğer veya elektrolit odaklı daha yakın değerlendirme olasılığını artırır.</div>"
                "<div class=\"blog-example\"><strong>Belirgin anormallik veya semptom eşliği:</strong> Özellikle yüksek potasyum, çok düşük sodyum, belirgin yüksek glukoz veya kötüleşen böbrek değerlerinde daha hızlı değerlendirme gerekir.</div>"
            ),
        ),
        Section(
            id="fasting-prep",
            level=2,
            heading="Metabolik panel için aç olmak gerekir mi?",
            body_html=(
                "<p>Birçok laboratuvarda metabolik panelin kendisi <strong>her zaman açlık gerektirmez</strong>; "
                "ama aynı kan alımında glukoz veya lipid değerlendirmesi de yapılacaksa açlık istenebilir. "
                "Doktorunuz açlık glukozu, lipidler veya insülin direnci belirteçlerini birlikte okuyacaksa "
                "laboratuvar talimatına uymak önemlidir.</p>"
                "<p>Ayrıca kreatin, diüretik, tansiyon ilacı, kusma, ishal, yoğun egzersiz veya "
                "susuzluk gibi etkenleri doktorunuza söylemeniz gerekir; bunlar sonucu etkileyebilir.</p>"
            ),
        ),
        Section(
            id="follow-up",
            level=2,
            heading="Anormal metabolik panel sonrası sık görülen takipler",
            body_html=(
                "<p>Bir sonraki adım, panelin hangi kısmının anormal olduğuna göre değişir:</p>"
                "<ul>"
                "<li>Geçici bir etkiden şüpheleniliyorsa aynı biyokimya paneli tekrar edilir.</li>"
                "<li>Böbrek odaklı takipte <a href=\"/en/tools/egfr-calculator\">eGFR hesaplama</a>, kan basıncı değerlendirmesi veya idrar testi istenebilir.</li>"
                "<li>Glukoz odaklı takipte <a href=\"/tr/blog/hba1c-sonucu-ne-anlama-gelir\">HbA1c</a>, açlık glukozu veya insülin direnci bağlamı eklenebilir.</li>"
                "<li>ALT, AST, ALP, bilirubin, albümin veya total protein sapmışsa karaciğer ve protein odaklı ileri değerlendirme yapılabilir.</li>"
                "</ul>"
                "<p>Anormal bir panel tek başına tanı değildir; klinik bağlam içinde yorumlanacak bir sinyaldir.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="Kendi raporunuzla birlikte nasıl kullanılır?",
            body_html=(
                "<p>Raporunuzda BMP veya CMP varsa ve bütün resmi görmek istiyorsanız "
                "<a href=\"/tr/kan-tahlili-sonucu\">kan tahlili sonucu açıklaması</a> sayfasından "
                "başlayabilir veya <a href=\"/tr/kan-tahlili-yukle\">kan tahlili sonucunuzu yükleyebilirsiniz</a>. "
                "Böylece değerleri tek tek değil, yapılandırılmış bir özet içinde okuyabilirsiniz.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Uyarı",
            body_html=(
                "<p><strong>Bu rehber yalnızca eğitim amaçlıdır.</strong> Metabolik panel tek başına "
                "bir hastalık tanısı koydurmaz. Özellikle belirtiler, tekrarlayan anormallikler veya "
                "birlikte hareket eden birden fazla parametre varsa sonuçlarınızı mutlaka hekimle değerlendirin.</p>"
            ),
        ),
    ]


def _sections_de():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Kurze Antwort: Was zeigt ein Stoffwechselpanel?",
            body_html=(
                "<p>Ein <strong>Stoffwechselpanel</strong> ist ein Bluttest, der Marker zu Blutzucker, "
                "Elektrolyten und Nierenfunktion zusammenfasst. Beim <strong>Comprehensive Metabolic Panel "
                "(CMP)</strong> kommen meist auch Leber- und Proteinmarker hinzu. Ein <strong>Basic "
                "Metabolic Panel (BMP)</strong> ist kürzer und umfasst typischerweise Glukose, Natrium, "
                "Kalium, Chlorid, Bikarbonat/CO<sub>2</sub>, Kalzium, Harnstoff und Kreatinin.</p>"
                "<p>Ärzte lesen das Panel nicht als einen einzigen Score. Sie vergleichen die Werte "
                "untereinander, um zu erkennen, ob das Muster eher zu Hydrierung, Nierenfunktion, "
                "Glukosekontrolle, Säure-Basen-Haushalt, Leberstress oder einer vorübergehenden "
                "Laborschwankung passt.</p>"
            ),
        ),
        Section(
            id="cmp-vs-bmp",
            level=2,
            heading="CMP vs. BMP: Was ist der Unterschied?",
            body_html=(
                "<table class=\"w-full border border-slate-200 text-sm my-4\" style=\"border-collapse: collapse;\">"
                "<thead><tr class=\"bg-slate-50\">"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Panel</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Typischer Inhalt</th>"
                "<th class=\"border border-slate-200 px-3 py-2 text-left\">Wofür es oft genutzt wird</th>"
                "</tr></thead><tbody>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>BMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Glukose, Elektrolyte, Kalzium, Harnstoff, Kreatinin, Bikarbonat/CO<sub>2</sub></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Hydrierung, Nierenfunktion, Elektrolyt- und Säure-Basen-Lage</td></tr>"
                "<tr><td class=\"border border-slate-200 px-3 py-2\"><strong>CMP</strong></td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Alles aus dem BMP plus Albumin, Gesamtprotein, ALP, ALT, AST und Bilirubin</td>"
                "<td class=\"border border-slate-200 px-3 py-2\">Breiterer metabolischer Überblick mit Leber- und Proteinmarkern</td></tr>"
                "</tbody></table>"
                "<p>Wenn auf Ihrem Befund <strong>CMP</strong> steht, erhalten Sie meist einen "
                "breiteren Chemie-Überblick als mit einem BMP. Je nach Labor kann die genaue "
                "Zusammensetzung aber variieren; die sicherste Referenz ist immer Ihre eigene Liste von Markern.</p>"
            ),
        ),
        Section(
            id="how-doctors-read-it",
            level=2,
            heading="Wie Ärzte ein Stoffwechselpanel in der Praxis lesen",
            body_html=(
                "<p>Der eigentliche Nutzen liegt meist im <strong>Muster</strong>, nicht in einer einzelnen Zahl. Beispiele:</p>"
                "<ul>"
                "<li><strong>Glukose</strong> wird oft zusammen mit <a href=\"/de/blog/hba1c-verstehen-was-bedeutet-der-wert\">HbA1c</a> und manchmal mit <a href=\"/de/blog/homa-ir-was-bedeutet-das\">HOMA-IR</a> bewertet.</li>"
                "<li><strong>Harnstoff, Kreatinin und eGFR</strong> werden gemeinsam betrachtet, um Nierenfunktion und Hydrierung besser einzuordnen. Siehe <a href=\"/de/blog/creatinine-egfr-what-it-means\">Kreatinin und eGFR</a>.</li>"
                "<li><strong>Natrium, Kalium, Chlorid und Bikarbonat</strong> helfen bei der Einordnung von Flüssigkeitshaushalt, Medikamenteneffekt und Säure-Basen-Muster. Relevante Seiten: <a href=\"/de/blog/sodium-low-meaning\">niedriges Natrium</a> und <a href=\"/de/blog/potassium-high-meaning\">hohes Kalium</a>.</li>"
                "<li><strong>ALT, AST, ALP, Bilirubin, Albumin und Gesamtprotein</strong> liefern Leber- und Proteinkontext. Starten Sie mit <a href=\"/de/blog/was-bedeuten-erhoehte-alt-und-ast-werte\">hohen ALT/AST</a>, <a href=\"/de/blog/albumin-low-meaning\">niedrigem Albumin</a> und <a href=\"/de/blog/total-protein-high-or-low\">Gesamtprotein</a>.</li>"
                "</ul>"
                "<p>Darum ist ein Stoffwechselpanel oft einer der nützlichsten ersten Bluttests: "
                "Es verbindet mehrere Systeme gleichzeitig statt nur einen Marker isoliert zu betrachten.</p>"
            ),
        ),
        Section(
            id="normal-high-low",
            level=2,
            heading="Normale, leicht abweichende und deutlich abweichende Muster",
            body_html=(
                "<div class=\"blog-example\"><strong>Überwiegend im Normbereich:</strong> meist beruhigend, aber Symptome, Verlauf und Fragestellung bleiben wichtig.</div>"
                "<div class=\"blog-example\"><strong>Ein Wert leicht außerhalb:</strong> kann zu Hydrierung, Nüchternstatus, Medikamenten oder Laborschwankung passen. Eine Wiederholung ist häufig.</div>"
                "<div class=\"blog-example\"><strong>Mehrere zusammenhängende Marker verändert:</strong> erhöht die Wahrscheinlichkeit einer gezielteren Abklärung zu Niere, Glukose, Leber oder Elektrolyten.</div>"
                "<div class=\"blog-example\"><strong>Deutlich abnormal oder mit Symptomen:</strong> braucht meist schnellere ärztliche Bewertung, vor allem bei hohem Kalium, sehr niedrigem Natrium, stark erhöhter Glukose oder schlechter werdenden Nierenwerten.</div>"
            ),
        ),
        Section(
            id="fasting-prep",
            level=2,
            heading="Muss man für ein Stoffwechselpanel nüchtern sein?",
            body_html=(
                "<p>In vielen Laboren erfordert das Stoffwechselpanel selbst <strong>nicht immer Nüchternheit</strong>; "
                "sie kann aber empfohlen werden, wenn im selben Blutabnahmetermin auch Glukose- oder Lipidwerte "
                "beurteilt werden sollen. Wenn Ihr Arzt Nüchternglukose, Lipide oder Insulinresistenz gemeinsam "
                "bewerten möchte, sind die Laborhinweise wichtig.</p>"
                "<p>Berichten Sie auch über Kreatin, Diuretika, Blutdruckmittel, Erbrechen, Durchfall, "
                "intensiven Sport oder Dehydrierung, weil diese Faktoren Ergebnisse beeinflussen können.</p>"
            ),
        ),
        Section(
            id="follow-up",
            level=2,
            heading="Welche Folgeuntersuchungen sind häufig?",
            body_html=(
                "<p>Die nächsten Schritte hängen davon ab, welcher Teil des Panels auffällig ist:</p>"
                "<ul>"
                "<li>Wiederholung desselben Chemiepanels, wenn ein vorübergehender Effekt oder Hydrierung eine Rolle spielen könnte.</li>"
                "<li>Nierenfokussierte Nachverfolgung mit <a href=\"/en/tools/egfr-calculator\">eGFR-Berechnung</a>, Blutdruckbeurteilung oder Urintests.</li>"
                "<li>Glukosebezogene Nachverfolgung mit <a href=\"/de/blog/hba1c-verstehen-was-bedeutet-der-wert\">HbA1c</a>, Nüchternglukose oder Insulinresistenz-Kontext.</li>"
                "<li>Leber- oder proteinbezogene Abklärung, wenn ALT, AST, ALP, Bilirubin, Albumin oder Gesamtprotein auffällig sind.</li>"
                "</ul>"
                "<p>Ein auffälliges Panel ist kein Diagnosenachweis, sondern ein Signal, das im Kontext gelesen werden muss.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="Wie Sie das mit Ihrem eigenen Befund nutzen",
            body_html=(
                "<p>Wenn Ihr Laborbefund ein BMP oder CMP enthält und Sie das Gesamtbild besser verstehen möchten, "
                "beginnen Sie mit <a href=\"/de/blood-test-results\">Blutwerte verstehen</a> oder nutzen Sie "
                "<a href=\"/analyze\">Analyse starten</a>, um die Werte als strukturierte Zusammenfassung statt "
                "als einzelne Zahlen zu sehen.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Hinweis",
            body_html=(
                "<p><strong>Dieser Leitfaden dient nur der Information.</strong> Ein Stoffwechselpanel "
                "stellt allein keine Diagnose. Besprechen Sie auffällige Werte immer mit einem Arzt, "
                "besonders bei Symptomen, wiederholten Auffälligkeiten oder mehreren gemeinsam veränderten Markern.</p>"
            ),
        ),
    ]


def _sections_es():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="Respuesta rápida: qué muestra un panel metabólico", body_html=(
            "<p>Un <strong>panel metabólico</strong> es un análisis de sangre que agrupa marcadores de glucosa, electrólitos y función renal. En el caso del <strong>panel metabólico completo (CMP)</strong>, también suele incluir marcadores hepáticos y proteicos. El <strong>panel metabólico básico (BMP)</strong> es una versión más corta.</p>"
            "<p>Los médicos no leen este panel como una sola puntuación. Comparan los valores entre sí para entender si el patrón apunta más a hidratación, riñón, control de glucosa, equilibrio ácido-base, hígado o una variación temporal.</p>"
        )),
        Section(id="cmp-vs-bmp", level=2, heading="CMP vs BMP: cuál es la diferencia", body_html=(
            "<p>El <strong>BMP</strong> suele incluir glucosa, sodio, potasio, cloro, bicarbonato/CO<sub>2</sub>, calcio, urea y creatinina. El <strong>CMP</strong> añade habitualmente albúmina, proteína total, ALT, AST, ALP y bilirrubina.</p>"
            "<p>En general, el CMP ofrece una visión química más amplia que el BMP, pero la composición exacta puede variar según el laboratorio.</p>"
        )),
        Section(id="how-doctors-read-it", level=2, heading="Cómo interpretan los médicos un panel metabólico", body_html=(
            "<p>Lo más útil suele ser el <strong>patrón</strong> más que un número aislado:</p>"
            "<ul>"
            "<li>La <strong>glucosa</strong> suele compararse con <a href=\"/es/blog/hba1c-que-significa-el-resultado\">HbA1c</a> y a veces con <a href=\"/es/blog/que-es-homa-ir\">HOMA-IR</a>.</li>"
            "<li><strong>Urea, creatinina y eGFR</strong> ayudan a valorar función renal e hidratación. Véase <a href=\"/es/blog/creatinine-egfr-what-it-means\">creatinina y eGFR</a>.</li>"
            "<li><strong>Sodio, potasio, cloro y bicarbonato</strong> orientan sobre líquidos, medicación y equilibrio ácido-base.</li>"
            "<li><strong>ALT, AST, ALP, bilirrubina, albúmina y proteína total</strong> aportan contexto hepático y proteico.</li>"
            "</ul>"
        )),
        Section(id="normal-high-low", level=2, heading="Patrones normales y anormales", body_html=(
            "<div class=\"blog-example\"><strong>La mayoría en rango:</strong> suele ser tranquilizador, pero los síntomas y la evolución siguen importando.</div>"
            "<div class=\"blog-example\"><strong>Una alteración leve:</strong> puede relacionarse con hidratación, ayuno, fármacos o variación del laboratorio. La repetición es frecuente.</div>"
            "<div class=\"blog-example\"><strong>Varios marcadores relacionados alterados:</strong> aumenta la probabilidad de un estudio dirigido a riñón, glucosa, hígado o electrólitos.</div>"
        )),
        Section(id="fasting-prep", level=2, heading="¿Hace falta ayuno?", body_html=(
            "<p>No siempre. Algunos laboratorios permiten panel metabólico sin ayuno, pero puede recomendarse si en la misma extracción también se valoran glucosa en ayunas, lípidos o resistencia a la insulina.</p>"
        )),
        Section(id="follow-up", level=2, heading="Qué seguimiento suele hacerse", body_html=(
            "<p>Depende de qué parte del panel esté alterada: repetir la química, ampliar estudio renal, añadir contexto de glucosa o revisar el hígado y las proteínas.</p>"
            "<p>Un panel anormal es una señal que debe interpretarse en contexto, no un diagnóstico por sí solo.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="Cómo usarlo con tu informe", body_html=(
            "<p>Si tu informe incluye un BMP o CMP, puedes empezar por <a href=\"/es/blood-test-results\">resultados de análisis</a> o <a href=\"/es/upload-blood-test-results\">subir tus resultados</a> para ver los valores en un resumen estructurado.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Aviso", body_html=(
            "<p><strong>Esta guía es solo informativa.</strong> Un panel metabólico no establece un diagnóstico por sí solo. Revisa siempre los resultados con un profesional sanitario.</p>"
        )),
    ]


def _sections_fr():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="Réponse rapide : que montre un bilan métabolique ?", body_html=(
            "<p>Un <strong>bilan métabolique</strong> regroupe des marqueurs liés au glucose, aux électrolytes et à la fonction rénale. Le <strong>bilan métabolique complet (CMP)</strong> ajoute souvent des marqueurs du foie et des protéines. Le <strong>BMP</strong> est une version plus courte.</p>"
            "<p>Les médecins ne lisent pas ce bilan comme un score unique. Ils comparent les valeurs entre elles pour voir si le profil évoque plutôt l'hydratation, le rein, le glucose, l'équilibre acido-basique, le foie ou une variation temporaire.</p>"
        )),
        Section(id="cmp-vs-bmp", level=2, heading="CMP vs BMP : quelle différence ?", body_html=(
            "<p>Le <strong>BMP</strong> comprend généralement le glucose, le sodium, le potassium, le chlorure, le bicarbonate/CO<sub>2</sub>, le calcium, l'urée et la créatinine. Le <strong>CMP</strong> ajoute souvent l'albumine, les protéines totales, l'ALT, l'AST, les PAL et la bilirubine.</p>"
            "<p>Le CMP donne donc en général une vue plus large que le BMP, même si la composition exacte varie selon le laboratoire.</p>"
        )),
        Section(id="how-doctors-read-it", level=2, heading="Comment les médecins lisent ce bilan", body_html=(
            "<p>L'intérêt principal vient souvent du <strong>profil global</strong>, pas d'un seul chiffre :</p>"
            "<ul>"
            "<li>Le <strong>glucose</strong> est souvent comparé à <a href=\"/fr/blog/hba1c-comprendre-resultat\">l'HbA1c</a> et parfois à <a href=\"/fr/blog/quest-ce-que-homa-ir\">HOMA-IR</a>.</li>"
            "<li><strong>Urée, créatinine et eGFR</strong> aident à interpréter la fonction rénale et l'hydratation. Voir <a href=\"/fr/blog/creatinine-egfr-what-it-means\">créatinine et eGFR</a>.</li>"
            "<li><strong>Sodium, potassium, chlorure et bicarbonate</strong> donnent un contexte sur les liquides, les médicaments et l'équilibre acido-basique.</li>"
            "<li><strong>ALT, AST, PAL, bilirubine, albumine et protéines totales</strong> apportent un contexte hépatique et protéique.</li>"
            "</ul>"
        )),
        Section(id="normal-high-low", level=2, heading="Profils normaux et anormaux", body_html=(
            "<div class=\"blog-example\"><strong>La plupart des valeurs sont normales :</strong> c'est souvent rassurant, mais les symptômes et l'évolution restent importants.</div>"
            "<div class=\"blog-example\"><strong>Une anomalie légère :</strong> elle peut être liée à l'hydratation, au jeûne, aux médicaments ou à une variation du laboratoire.</div>"
            "<div class=\"blog-example\"><strong>Plusieurs marqueurs liés sont anormaux :</strong> cela oriente davantage vers un bilan ciblé rein, glucose, foie ou électrolytes.</div>"
        )),
        Section(id="fasting-prep", level=2, heading="Faut-il être à jeun ?", body_html=(
            "<p>Pas toujours. Certains laboratoires acceptent un bilan métabolique non à jeun, mais le jeûne peut être demandé si le prélèvement sert aussi à évaluer la glycémie à jeun, les lipides ou la résistance à l'insuline.</p>"
        )),
        Section(id="follow-up", level=2, heading="Quel suivi est fréquent ?", body_html=(
            "<p>Le suivi dépend de la partie anormale du bilan : répétition de la chimie, contrôle rénal, ajout de contexte glycémique ou bilan hépatique/protéique.</p>"
            "<p>Un bilan anormal est un signal à interpréter dans son contexte, pas un diagnostic isolé.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="Comment l'utiliser avec votre compte rendu", body_html=(
            "<p>Si votre compte rendu mentionne un BMP ou un CMP, vous pouvez commencer par <a href=\"/fr/blood-test-results\">résultats d'analyses</a> ou <a href=\"/fr/upload-blood-test-results\">télécharger vos résultats</a> pour obtenir un résumé structuré.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Avertissement", body_html=(
            "<p><strong>Ce guide est purement informatif.</strong> Un bilan métabolique ne pose pas de diagnostic à lui seul. Discutez toujours des résultats avec un professionnel de santé.</p>"
        )),
    ]


def _sections_it():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="Risposta rapida: cosa mostra un pannello metabolico", body_html=(
            "<p>Un <strong>pannello metabolico</strong> raggruppa valori relativi a glucosio, elettroliti e funzione renale. Nel <strong>pannello metabolico completo (CMP)</strong> si aggiungono spesso anche marker epatici e proteici. Il <strong>BMP</strong> è una versione più corta.</p>"
            "<p>I medici non lo leggono come un singolo punteggio. Confrontano i valori tra loro per capire se il quadro suggerisce più idratazione, rene, controllo del glucosio, equilibrio acido-base, fegato o una variazione temporanea.</p>"
        )),
        Section(id="cmp-vs-bmp", level=2, heading="CMP vs BMP: qual è la differenza?", body_html=(
            "<p>Il <strong>BMP</strong> include di solito glucosio, sodio, potassio, cloro, bicarbonato/CO<sub>2</sub>, calcio, urea e creatinina. Il <strong>CMP</strong> aggiunge spesso albumina, proteine totali, ALT, AST, ALP e bilirubina.</p>"
            "<p>In pratica il CMP offre una visione più ampia del BMP, anche se la composizione precisa può cambiare da laboratorio a laboratorio.</p>"
        )),
        Section(id="how-doctors-read-it", level=2, heading="Come viene letto nella pratica", body_html=(
            "<p>Il valore principale sta spesso nel <strong>pattern</strong>, non in un numero isolato:</p>"
            "<ul>"
            "<li>Il <strong>glucosio</strong> viene spesso confrontato con <a href=\"/it/blog/hba1c-cosa-significa-il-valore\">HbA1c</a> e talvolta con <a href=\"/it/blog/cos-e-homa-ir\">HOMA-IR</a>.</li>"
            "<li><strong>Urea, creatinina ed eGFR</strong> aiutano a capire funzione renale e idratazione. Vedi <a href=\"/it/blog/creatinine-egfr-what-it-means\">creatinina ed eGFR</a>.</li>"
            "<li><strong>Sodio, potassio, cloro e bicarbonato</strong> danno contesto su liquidi, farmaci ed equilibrio acido-base.</li>"
            "<li><strong>ALT, AST, ALP, bilirubina, albumina e proteine totali</strong> aggiungono contesto epatico e proteico.</li>"
            "</ul>"
        )),
        Section(id="normal-high-low", level=2, heading="Pattern normali e anomali", body_html=(
            "<div class=\"blog-example\"><strong>La maggior parte dei valori è nei limiti:</strong> spesso rassicurante, ma sintomi e andamento restano importanti.</div>"
            "<div class=\"blog-example\"><strong>Una lieve alterazione:</strong> può dipendere da idratazione, digiuno, farmaci o variabilità del laboratorio.</div>"
            "<div class=\"blog-example\"><strong>Più marker correlati alterati:</strong> rende più probabile un approfondimento su rene, glucosio, fegato o elettroliti.</div>"
        )),
        Section(id="fasting-prep", level=2, heading="Serve il digiuno?", body_html=(
            "<p>Non sempre. Alcuni laboratori consentono un pannello metabolico senza digiuno, ma il digiuno può essere richiesto se nello stesso prelievo si valutano glicemia a digiuno, lipidi o resistenza insulinica.</p>"
        )),
        Section(id="follow-up", level=2, heading="Quale follow-up è comune?", body_html=(
            "<p>Dipende dalla parte alterata del pannello: ripetizione della chimica, controllo renale, contesto glicemico aggiuntivo oppure approfondimento epatico/proteico.</p>"
            "<p>Un pannello anomalo è un segnale da interpretare nel contesto, non una diagnosi da solo.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="Come usarlo con il tuo referto", body_html=(
            "<p>Se il tuo referto include un BMP o un CMP, puoi iniziare da <a href=\"/it/blood-test-results\">risultati esami</a> oppure <a href=\"/it/upload-blood-test-results\">caricare i risultati</a> per ottenere un riepilogo strutturato.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Disclaimer", body_html=(
            "<p><strong>Questa guida è solo informativa.</strong> Un pannello metabolico non fa diagnosi da solo. Discute sempre i risultati con un professionista sanitario.</p>"
        )),
    ]


def _sections_he():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="תשובה קצרה: מה מראה פאנל מטבולי", body_html=(
            "<p><strong>פאנל מטבולי</strong> הוא בדיקת דם שמרכזת מדדי גלוקוז, אלקטרוליטים ותפקוד כליות. ב-<strong>CMP</strong> יש בדרך כלל גם מדדי כבד וחלבונים, בעוד <strong>BMP</strong> הוא גרסה קצרה יותר.</p>"
            "<p>הרופאים לא מסתכלים על ציון אחד, אלא על <strong>התבנית</strong> בין הערכים כדי להבין אם הכיוון מתאים יותר לנוזלים, כליה, גלוקוז, חומצה-בסיס או כבד.</p>"
        )),
        Section(id="cmp-vs-bmp", level=2, heading="מה ההבדל בין CMP ל-BMP?", body_html=(
            "<p>בדרך כלל <strong>BMP</strong> כולל גלוקוז, נתרן, אשלגן, כלוריד, ביקרבונט/CO<sub>2</sub>, סידן, אוראה וקריאטינין. <strong>CMP</strong> מוסיף לעיתים גם אלבומין, חלבון כללי, ALT, AST, ALP ובילירובין.</p>"
        )),
        Section(id="how-doctors-read-it", level=2, heading="איך מפרשים את התוצאות בפועל", body_html=(
            "<ul>"
            "<li><strong>גלוקוז</strong> נותן הקשר מטבולי, ולעיתים משווים אותו גם ל-<a href=\"/he/blog/מה-זה-homa-ir\">HOMA-IR</a>.</li>"
            "<li><strong>אוראה, קריאטינין ו-eGFR</strong> עוזרים להבין תפקוד כלייתי ומצב נוזלים. ראו <a href=\"/he/blog/creatinine-egfr-what-it-means\">קריאטינין ו-eGFR</a>.</li>"
            "<li><strong>נתרן, אשלגן, כלוריד וביקרבונט</strong> נותנים רמזים על איזון נוזלים וחומצה-בסיס.</li>"
            "<li><strong>ALT, AST, ALP, בילירובין, אלבומין וחלבון כללי</strong> מוסיפים הקשר כבד וחלבונים.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="דפוסים תקינים וחריגים", body_html=(
            "<div class=\"blog-example\"><strong>רוב הערכים בטווח:</strong> לרוב זה מרגיע, אבל עדיין חשוב להבין תסמינים והקשר קליני.</div>"
            "<div class=\"blog-example\"><strong>חריגה קלה בודדת:</strong> יכולה להיות קשורה לנוזלים, צום, תרופות או שינוי זמני.</div>"
            "<div class=\"blog-example\"><strong>כמה מדדים קשורים חריגים יחד:</strong> מעלה יותר חשד לצורך בבירור ממוקד של כליה, גלוקוז, כבד או אלקטרוליטים.</div>"
        )),
        Section(id="use-with-your-report", level=2, heading="איך להשתמש בזה עם הדוח שלך", body_html=(
            "<p>אם יש אצלך BMP או CMP, אפשר להתחיל ב-<a href=\"/he/blood-test-results\">תוצאות בדיקות דם</a> או <a href=\"/he/upload-blood-test-results\">להעלות את התוצאות</a> כדי לראות סיכום מסודר.</p>"
        )),
        Section(id="disclaimer", level=2, heading="הבהרה", body_html=(
            "<p><strong>המדריך למידע בלבד.</strong> פאנל מטבולי אינו אבחנה בפני עצמו, ותמיד צריך לפרש אותו עם רופא.</p>"
        )),
    ]


def _sections_hi():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="संक्षिप्त उत्तर: मेटाबोलिक पैनल क्या दिखाता है", body_html=(
            "<p><strong>मेटाबोलिक पैनल</strong> एक ब्लड टेस्ट समूह है जिसमें ग्लूकोज, इलेक्ट्रोलाइट और किडनी फ़ंक्शन मार्कर होते हैं। <strong>CMP</strong> में अक्सर लिवर और प्रोटीन मार्कर भी शामिल होते हैं, जबकि <strong>BMP</strong> छोटा संस्करण है।</p>"
            "<p>डॉक्टर इसे एक नंबर की तरह नहीं पढ़ते; वे <strong>पूरा पैटर्न</strong> देखते हैं कि संकेत ग्लूकोज, किडनी, फ्लूड बैलेंस, एसिड-बेस या लिवर की ओर तो नहीं जा रहा।</p>"
        )),
        Section(id="cmp-vs-bmp", level=2, heading="CMP और BMP में क्या फर्क है?", body_html=(
            "<p><strong>BMP</strong> में आमतौर पर ग्लूकोज, सोडियम, पोटैशियम, क्लोराइड, बाइकार्बोनेट/CO<sub>2</sub>, कैल्शियम, यूरिया और क्रिएटिनिन होते हैं। <strong>CMP</strong> में अक्सर एल्बुमिन, टोटल प्रोटीन, ALT, AST, ALP और बिलीरुबिन भी जुड़ते हैं।</p>"
        )),
        Section(id="how-doctors-read-it", level=2, heading="डॉक्टर इसे कैसे समझते हैं", body_html=(
            "<ul>"
            "<li><strong>ग्लूकोज</strong> मेटाबोलिक संदर्भ देता है, और कभी-कभी इसे <a href=\"/hi/blog/homa-ir-kya-hai\">HOMA-IR</a> के साथ देखा जाता है।</li>"
            "<li><strong>यूरिया, क्रिएटिनिन और eGFR</strong> किडनी फ़ंक्शन और हाइड्रेशन का संकेत देते हैं। देखें <a href=\"/hi/blog/creatinine-egfr-what-it-means\">क्रिएटिनिन और eGFR</a>.</li>"
            "<li><strong>सोडियम, पोटैशियम, क्लोराइड और बाइकार्बोनेट</strong> फ्लूड बैलेंस और एसिड-बेस स्थिति समझने में मदद करते हैं।</li>"
            "<li><strong>ALT, AST, ALP, बिलीरुबिन, एल्बुमिन और टोटल प्रोटीन</strong> लिवर और प्रोटीन पैटर्न का संदर्भ देते हैं।</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="सामान्य और असामान्य पैटर्न", body_html=(
            "<div class=\"blog-example\"><strong>ज़्यादातर वैल्यू सामान्य:</strong> अक्सर आश्वस्त करने वाला, लेकिन लक्षण और संदर्भ फिर भी मायने रखते हैं।</div>"
            "<div class=\"blog-example\"><strong>एक हल्का बदलाव:</strong> यह हाइड्रेशन, फास्टिंग, दवा या अस्थायी बदलाव से जुड़ा हो सकता है।</div>"
            "<div class=\"blog-example\"><strong>कई जुड़े मार्कर बदले हुए:</strong> इससे किडनी, ग्लूकोज, लिवर या इलेक्ट्रोलाइट पर और ध्यान देने की ज़रूरत बढ़ती है।</div>"
        )),
        Section(id="use-with-your-report", level=2, heading="अपनी रिपोर्ट के साथ इसे कैसे इस्तेमाल करें", body_html=(
            "<p>अगर आपकी रिपोर्ट में BMP या CMP है, तो आप <a href=\"/hi/blood-test-results\">blood test results</a> या <a href=\"/hi/upload-blood-test-results\">results upload</a> से शुरू कर सकते हैं ताकि संरचित सारांश मिल सके।</p>"
        )),
        Section(id="disclaimer", level=2, heading="डिस्क्लेमर", body_html=(
            "<p><strong>यह गाइड केवल जानकारी के लिए है.</strong> मेटाबोलिक पैनल अकेले किसी बीमारी का निदान नहीं करता। सही व्याख्या डॉक्टर के साथ करें।</p>"
        )),
    ]


def _sections_ar():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="إجابة سريعة: ماذا تُظهر لوحة الأيض؟", body_html=(
            "<p><strong>لوحة الأيض</strong> هي مجموعة تحاليل دم تشمل الجلوكوز والكهارل ومؤشرات وظيفة الكلى. أما <strong>CMP</strong> فيضيف غالباً مؤشرات الكبد والبروتينات، بينما <strong>BMP</strong> نسخة أقصر.</p>"
            "<p>لا يقرأ الأطباء هذه اللوحة كرقم واحد، بل ينظرون إلى <strong>النمط العام</strong> بين القيم لمعرفة ما إذا كان الاتجاه يتعلق بالسوائل أو الكلى أو الجلوكوز أو التوازن الحمضي القاعدي أو الكبد.</p>"
        )),
        Section(id="cmp-vs-bmp", level=2, heading="ما الفرق بين CMP وBMP؟", body_html=(
            "<p>غالباً يشمل <strong>BMP</strong> الجلوكوز والصوديوم والبوتاسيوم والكلوريد والبيكربونات/CO<sub>2</sub> والكالسيوم واليوريا والكرياتينين. أما <strong>CMP</strong> فيضيف عادة الألبومين والبروتين الكلي وALT وAST وALP والبيليروبين.</p>"
        )),
        Section(id="how-doctors-read-it", level=2, heading="كيف يفسر الأطباء النتائج", body_html=(
            "<ul>"
            "<li><strong>الجلوكوز</strong> يعطي سياقاً أيضياً، وأحياناً يُقارن مع <a href=\"/ar/blog/ما-هو-homa-ir\">HOMA-IR</a>.</li>"
            "<li><strong>اليوريا والكرياتينين وeGFR</strong> تساعد على فهم وظيفة الكلى وحالة السوائل. راجع <a href=\"/ar/blog/creatinine-egfr-what-it-means\">الكرياتينين وeGFR</a>.</li>"
            "<li><strong>الصوديوم والبوتاسيوم والكلوريد والبيكربونات</strong> تعطي فكرة عن توازن السوائل والحالة الحمضية القاعدية.</li>"
            "<li><strong>ALT وAST وALP والبيليروبين والألبومين والبروتين الكلي</strong> تضيف سياقاً للكبد والبروتينات.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="أنماط طبيعية ومرتفعة أو منخفضة", body_html=(
            "<div class=\"blog-example\"><strong>معظم القيم ضمن الطبيعي:</strong> يكون ذلك مطمئناً غالباً، لكن الأعراض والسياق ما زالا مهمين.</div>"
            "<div class=\"blog-example\"><strong>ارتفاع أو انخفاض بسيط منفرد:</strong> قد يرتبط بالسوائل أو الصيام أو الأدوية أو تغير مؤقت.</div>"
            "<div class=\"blog-example\"><strong>عدة مؤشرات مترابطة غير طبيعية:</strong> يزيد هذا الحاجة إلى تقييم موجه للكلى أو الجلوكوز أو الكبد أو الكهارل.</div>"
        )),
        Section(id="use-with-your-report", level=2, heading="كيف تستخدم هذا مع تقريرك", body_html=(
            "<p>إذا كان تقريرك يحتوي على BMP أو CMP، يمكنك البدء من <a href=\"/ar/blood-test-results\">نتائج التحاليل</a> أو <a href=\"/ar/upload-blood-test-results\">رفع النتائج</a> لرؤية ملخص منظم.</p>"
        )),
        Section(id="disclaimer", level=2, heading="تنبيه", body_html=(
            "<p><strong>هذا الدليل للمعلومات فقط.</strong> لوحة الأيض لا تعطي تشخيصاً بمفردها، ويجب دائماً مناقشة النتائج مع الطبيب.</p>"
        )),
    ]


def build_metabolic_panel_article():
    """Build a dedicated metabolic panel article."""
    from app.blog_i18n import Article

    return Article(
        id="metabolic-panel-results-explained",
        published_at=date(2026, 3, 26),
        last_updated=date(2026, 3, 26),
        read_minutes=8,
        cover_image="/static/images/blog/how-to-read-blood-test-results.png",
        category={"en": "Metabolic Panel", "tr": "Metabolik Panel", "de": "Stoffwechselpanel", "es": "Panel metabólico", "fr": "Bilan métabolique", "it": "Pannello metabolico", "he": "פאנל מטבולי", "hi": "मेटाबोलिक पैनल", "ar": "لوحة الأيض"},
        slugs={
            "en": "metabolic-panel-results-explained",
            "tr": "metabolik-panel-sonuclari-nasil-yorumlanir",
            "de": "stoffwechselpanel-cmp-bmp-verstehen",
            "es": "panel-metabolico-cmp-bmp-explicado",
            "fr": "bilan-metabolique-cmp-bmp-explication",
            "it": "pannello-metabolico-cmp-bmp-spiegato",
            "he": "פענוח-פאנל-מטבולי-cmp-bmp",
            "hi": "metabolic-panel-cmp-bmp-samjhein",
            "ar": "شرح-لوحة-الأيض-cmp-bmp",
        },
        titles={
            "en": "Metabolic Panel Results Explained: CMP vs BMP, Normal, High, and Low Patterns",
            "tr": "Metabolik Panel Sonuçları: CMP, BMP, Normal, Yüksek ve Düşük Örüntüler",
            "de": "Stoffwechselpanel verstehen: CMP, BMP, normale und auffällige Muster",
            "es": "Panel metabólico explicado: CMP, BMP y patrones normales o alterados",
            "fr": "Bilan métabolique expliqué : CMP, BMP et profils normaux ou anormaux",
            "it": "Pannello metabolico spiegato: CMP, BMP e pattern normali o alterati",
            "he": "פאנל מטבולי מוסבר: CMP, BMP ודפוסים תקינים או חריגים",
            "hi": "मेटाबोलिक पैनल समझें: CMP, BMP और सामान्य या बदले हुए पैटर्न",
            "ar": "شرح لوحة الأيض: CMP وBMP والأنماط الطبيعية أو غير الطبيعية",
        },
        subtitles={
            "en": "Understand what a metabolic panel includes, how doctors read CMP and BMP results, and which combinations of markers usually drive follow-up.",
            "tr": "Metabolik panelin neleri içerdiğini, doktorların CMP ve BMP sonuçlarını nasıl yorumladığını ve hangi kombinasyonların ileri değerlendirmeyi yönlendirdiğini öğrenin.",
            "de": "Verstehen Sie, was ein Stoffwechselpanel umfasst, wie Ärzte CMP- und BMP-Ergebnisse lesen und welche Kombinationen typischerweise weitere Abklärung auslösen.",
            "es": "Aprende qué incluye un panel metabólico, cómo se interpretan los resultados de CMP y BMP y qué combinaciones suelen guiar el seguimiento.",
            "fr": "Comprenez ce que contient un bilan métabolique, comment sont lus les résultats de CMP et BMP et quelles combinaisons orientent le suivi.",
            "it": "Scopri cosa include un pannello metabolico, come vengono letti i risultati di CMP e BMP e quali combinazioni guidano di solito il follow-up.",
            "he": "הבינו מה כולל פאנל מטבולי, איך מפרשים CMP ו-BMP ואילו שילובים של מדדים בדרך כלל מכוונים את המשך הבירור.",
            "hi": "जानें कि मेटाबोलिक पैनल में क्या शामिल होता है, डॉक्टर CMP और BMP को कैसे पढ़ते हैं और किन मार्कर संयोजनों पर आगे की जांच निर्भर करती है.",
            "ar": "تعرّف على ما تتضمنه لوحة الأيض، وكيف يقرأ الأطباء نتائج CMP وBMP، وما هي التركيبات التي تدفع عادة إلى المتابعة.",
        },
        excerpts={
            "en": "Clear guide to metabolic panel results, including CMP vs BMP, common markers, normal vs abnormal patterns, and what doctors usually compare next.",
            "tr": "CMP ile BMP farkı, sık görülen belirteçler, normal ve anormal örüntüler ve doktorların bir sonraki adımda neyi karşılaştırdığına dair net rehber.",
            "de": "Klarer Leitfaden zu CMP vs. BMP, typischen Markern, normalen und auffälligen Mustern sowie den häufigsten ärztlichen Vergleichsschritten.",
            "es": "Guía clara sobre panel metabólico, diferencias entre CMP y BMP, marcadores habituales y patrones que suelen llevar a más estudio.",
            "fr": "Guide clair du bilan métabolique : CMP vs BMP, marqueurs fréquents et profils qui conduisent souvent à un suivi.",
            "it": "Guida chiara al pannello metabolico: CMP vs BMP, marker comuni e pattern che portano spesso a ulteriori controlli.",
            "he": "מדריך ברור לפאנל מטבולי: ההבדל בין CMP ל-BMP, המדדים המרכזיים והדפוסים שמובילים לעיתים להמשך בירור.",
            "hi": "मेटाबोलिक पैनल के लिए साफ गाइड: CMP बनाम BMP, आम मार्कर और वे पैटर्न जो आगे की जांच की जरूरत दिखा सकते हैं.",
            "ar": "دليل واضح لنتائج لوحة الأيض: الفرق بين CMP وBMP وأهم المؤشرات والأنماط التي قد تستدعي متابعة.",
        },
        seo_titles={
            "en": "Metabolic Panel Results Explained: CMP vs BMP, Normal, High, Low | NoryaAI",
            "tr": "Metabolik Panel Sonuçları: CMP, BMP, Normal ve Yüksek Değerler | NoryaAI",
            "de": "Stoffwechselpanel verstehen: CMP, BMP, normale und hohe Werte | NoryaAI",
            "es": "Panel metabólico explicado: CMP, BMP y valores normales o altos | NoryaAI",
            "fr": "Bilan métabolique expliqué : CMP, BMP et valeurs normales ou élevées | NoryaAI",
            "it": "Pannello metabolico spiegato: CMP, BMP e valori normali o alti | NoryaAI",
            "he": "פענוח פאנל מטבולי: CMP, BMP וערכים תקינים או חריגים | NoryaAI",
            "hi": "मेटाबोलिक पैनल समझें: CMP, BMP और सामान्य या ऊंची वैल्यू | NoryaAI",
            "ar": "شرح لوحة الأيض: CMP وBMP والقيم الطبيعية أو المرتفعة | NoryaAI",
        },
        seo_descriptions={
            "en": "Learn how to read metabolic panel results, including CMP vs BMP, glucose, electrolytes, kidney markers, liver markers, and common follow-up patterns.",
            "tr": "Metabolik panel sonuçlarını nasıl okuyacağınızı öğrenin: CMP ve BMP farkı, glukoz, elektrolitler, böbrek ve karaciğer belirteçleri ile sık görülen takip örüntüleri.",
            "de": "Erfahren Sie, wie Stoffwechselpanel-Ergebnisse gelesen werden: CMP vs. BMP, Glukose, Elektrolyte, Nieren- und Lebermarker sowie typische Verlaufsmuster.",
            "es": "Aprende a leer un panel metabólico: CMP vs BMP, glucosa, electrólitos, marcadores renales y hepáticos, y patrones habituales de seguimiento.",
            "fr": "Apprenez à lire un bilan métabolique : CMP vs BMP, glucose, électrolytes, marqueurs rénaux et hépatiques, et schémas fréquents de suivi.",
            "it": "Scopri come leggere un pannello metabolico: CMP vs BMP, glucosio, elettroliti, marker renali ed epatici e pattern comuni di follow-up.",
            "he": "למדו איך לקרוא פאנל מטבולי: CMP לעומת BMP, גלוקוז, אלקטרוליטים, מדדי כליה וכבד ודפוסי המשך נפוצים.",
            "hi": "सीखें मेटाबोलिक पैनल कैसे पढ़ें: CMP बनाम BMP, ग्लूकोज, इलेक्ट्रोलाइट, किडनी और लिवर मार्कर और सामान्य फॉलो-अप पैटर्न.",
            "ar": "تعرّف على كيفية قراءة لوحة الأيض: CMP مقابل BMP، الجلوكوز، الكهارل، مؤشرات الكلى والكبد وأنماط المتابعة الشائعة.",
        },
        sections_by_lang={"en": _sections_en(), "tr": _sections_tr(), "de": _sections_de(), "es": _sections_es(), "fr": _sections_fr(), "it": _sections_it(), "he": _sections_he(), "hi": _sections_hi(), "ar": _sections_ar()},
        cover_alt={
            "en": "Blood test report overview for metabolic panel interpretation",
            "tr": "Metabolik panel yorumu için kan tahlili raporu özeti",
            "de": "Übersicht eines Blutbefunds zur Interpretation des Stoffwechselpanels",
            "es": "Resumen de informe analítico para interpretar un panel metabólico",
            "fr": "Vue d'ensemble d'un bilan sanguin pour interpréter un bilan métabolique",
            "it": "Panoramica di un referto ematico per interpretare un pannello metabolico",
            "he": "סקירת דוח בדיקות דם לפענוח פאנל מטבולי",
            "hi": "मेटाबोलिक पैनल समझने के लिए ब्लड टेस्ट रिपोर्ट का सारांश",
            "ar": "نظرة عامة على تقرير تحليل دم لتفسير لوحة الأيض",
        },
        faq_schema_qa={
            "en": [
                {
                    "question": "What is the difference between a CMP and a BMP?",
                    "answer": "A BMP usually covers glucose, electrolytes, calcium, BUN, creatinine, and bicarbonate/CO2. A CMP includes those plus albumin, total protein, ALT, AST, ALP, and bilirubin for a broader chemistry overview.",
                },
                {
                    "question": "Does one abnormal metabolic panel result mean disease?",
                    "answer": "Not necessarily. A single mild abnormality can reflect hydration, fasting status, medication effect, or temporary variation. Doctors usually interpret the result together with symptoms, trend, and the rest of the panel.",
                },
                {
                    "question": "Do I need to fast before a metabolic panel?",
                    "answer": "Not always. Some labs allow non-fasting metabolic panels, but fasting may still be advised if glucose-focused tests, lipids, or insulin-related markers are being checked in the same blood draw.",
                },
                {
                    "question": "What do doctors compare with a metabolic panel?",
                    "answer": "Common comparisons include HbA1c for glucose context, creatinine and eGFR for kidney function, sodium and potassium for fluid balance, and ALT/AST, ALP, albumin, or total protein for liver and protein patterns.",
                },
            ],
            "tr": [
                {
                    "question": "CMP ile BMP arasındaki fark nedir?",
                    "answer": "BMP genelde glukoz, elektrolitler, kalsiyum, üre, kreatinin ve bikarbonatı içerir. CMP ise bunlara ek olarak albümin, total protein, ALT, AST, ALP ve bilirubini de kapsar.",
                },
                {
                    "question": "Metabolik panelde tek bir anormallik hastalık anlamına gelir mi?",
                    "answer": "Her zaman değil. Hafif bir sapma hidrasyon, açlık durumu, ilaç etkisi veya geçici bir değişkenlikle ilişkili olabilir. Doktorlar sonucu semptomlar, trend ve panelin geri kalanıyla birlikte yorumlar.",
                },
                {
                    "question": "Metabolik panel için açlık gerekir mi?",
                    "answer": "Her zaman gerekmez. Ancak aynı kan alımında glukoz, lipid veya insülinle ilişkili değerlendirme yapılacaksa açlık istenebilir.",
                },
            ],
            "de": [
                {
                    "question": "Was ist der Unterschied zwischen CMP und BMP?",
                    "answer": "Ein BMP umfasst meist Glukose, Elektrolyte, Kalzium, Harnstoff, Kreatinin und Bikarbonat. Ein CMP enthält diese Werte plus Albumin, Gesamtprotein, ALT, AST, ALP und Bilirubin.",
                },
                {
                    "question": "Bedeutet ein einzelner auffälliger Wert im Stoffwechselpanel sofort eine Krankheit?",
                    "answer": "Nicht unbedingt. Eine leichte Abweichung kann zu Hydrierung, Nüchternstatus, Medikamenten oder einer vorübergehenden Schwankung passen. Ärzte bewerten den Wert zusammen mit Symptomen, Verlauf und dem restlichen Panel.",
                },
                {
                    "question": "Muss man für ein Stoffwechselpanel nüchtern sein?",
                    "answer": "Nicht immer. Nüchternheit kann aber empfohlen werden, wenn im selben Blutabnahmetermin auch Glukose-, Lipid- oder insulinbezogene Werte beurteilt werden sollen.",
                },
            ],
            "es": [
                {"question": "¿Cuál es la diferencia entre un CMP y un BMP?", "answer": "Un BMP suele incluir glucosa, electrólitos, calcio, urea, creatinina y bicarbonato. Un CMP añade además albúmina, proteína total, ALT, AST, ALP y bilirrubina."},
                {"question": "¿Un solo valor alterado significa enfermedad?", "answer": "No necesariamente. Una alteración leve puede deberse a hidratación, ayuno, medicación o una variación temporal. Debe interpretarse junto con el resto del panel y los síntomas."},
            ],
            "fr": [
                {"question": "Quelle est la différence entre un CMP et un BMP ?", "answer": "Le BMP comprend généralement le glucose, les électrolytes, le calcium, l'urée, la créatinine et le bicarbonate. Le CMP ajoute souvent l'albumine, les protéines totales, l'ALT, l'AST, les PAL et la bilirubine."},
                {"question": "Un seul résultat anormal signifie-t-il une maladie ?", "answer": "Pas forcément. Une légère anomalie peut être liée à l'hydratation, au jeûne, aux médicaments ou à une variation temporaire. Le résultat doit être lu avec le reste du bilan et le contexte clinique."},
            ],
            "it": [
                {"question": "Qual è la differenza tra CMP e BMP?", "answer": "Il BMP comprende di solito glucosio, elettroliti, calcio, urea, creatinina e bicarbonato. Il CMP aggiunge spesso albumina, proteine totali, ALT, AST, ALP e bilirubina."},
                {"question": "Un solo valore alterato significa malattia?", "answer": "Non necessariamente. Una lieve alterazione può dipendere da idratazione, digiuno, farmaci o variazioni temporanee. Va interpretata insieme al resto del pannello e al contesto clinico."},
            ],
            "he": [
                {"question": "מה ההבדל בין CMP ל-BMP?", "answer": "BMP כולל לרוב גלוקוז, אלקטרוליטים, סידן, אוראה, קריאטינין וביקרבונט. CMP מוסיף בדרך כלל אלבומין, חלבון כללי, ALT, AST, ALP ובילירובין."},
                {"question": "האם חריגה בערך אחד אומרת שיש מחלה?", "answer": "לא בהכרח. חריגה קלה יכולה להיות קשורה לנוזלים, צום, תרופות או שינוי זמני. צריך לפרש אותה יחד עם שאר הפאנל וההקשר הקליני."},
            ],
            "hi": [
                {"question": "CMP और BMP में क्या अंतर है?", "answer": "BMP में आमतौर पर ग्लूकोज, इलेक्ट्रोलाइट, कैल्शियम, यूरिया, क्रिएटिनिन और बाइकार्बोनेट होते हैं। CMP में अक्सर एल्बुमिन, टोटल प्रोटीन, ALT, AST, ALP और बिलीरुबिन भी जुड़ते हैं."},
                {"question": "क्या एक बदली हुई वैल्यू का मतलब बीमारी है?", "answer": "ज़रूरी नहीं. हल्का बदलाव हाइड्रेशन, फास्टिंग, दवा या अस्थायी कारणों से हो सकता है. इसे पूरे पैनल और क्लिनिकल संदर्भ के साथ समझना चाहिए."},
            ],
            "ar": [
                {"question": "ما الفرق بين CMP وBMP؟", "answer": "يشمل BMP غالباً الجلوكوز والكهارل والكالسيوم واليوريا والكرياتينين والبيكربونات. أما CMP فيضيف عادة الألبومين والبروتين الكلي وALT وAST وALP والبيليروبين."},
                {"question": "هل يعني تغير قيمة واحدة وجود مرض؟", "answer": "ليس بالضرورة. قد يرتبط التغير البسيط بالسوائل أو الصيام أو الأدوية أو سبب مؤقت. يجب تفسيره مع بقية اللوحة والسياق السريري."},
            ],
        },
    )
