"""Blog article for urine ACR / microalbumin intent."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what urine ACR measures",
            body_html=(
                "<p><strong>Urine ACR</strong> stands for <strong>albumin-to-creatinine ratio</strong>. "
                "It measures how much albumin is leaking into the urine compared with creatinine, "
                "which helps adjust for how concentrated or diluted the urine sample is. It is "
                "often used to look for <strong>early kidney damage</strong>, especially in people "
                "with diabetes, high blood pressure, or chronic kidney disease risk.</p>"
            ),
        ),
        Section(
            id="microalbumin-vs-acr",
            level=2,
            heading="Is urine ACR the same as a microalbumin test?",
            body_html=(
                "<p>People often use the terms <strong>microalbumin</strong> and <strong>urine ACR</strong> "
                "interchangeably. In practice, a urine ACR is the more useful report format because it "
                "relates albumin to creatinine, which makes the result easier to compare between samples. "
                "This is why many labs now report an albumin-to-creatinine ratio rather than albumin alone.</p>"
            ),
        ),
        Section(
            id="what-high-acr-means",
            level=2,
            heading="What a high urine ACR may mean",
            body_html=(
                "<p>A higher urine ACR can mean the kidneys are allowing more albumin to pass into the urine "
                "than expected. Doctors often think about <strong>diabetes, blood pressure, kidney disease risk, "
                "and cardiovascular risk</strong> when they see this pattern. The result still needs context: "
                "exercise, fever, infection, menstruation, dehydration, and temporary illness can also affect "
                "a urine sample.</p>"
                "<p>Because of that, one abnormal ACR usually leads to <strong>repeat testing</strong> or wider "
                "kidney review rather than an immediate diagnosis.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-it",
            level=2,
            heading="How doctors compare urine ACR with blood tests",
            body_html=(
                "<p>Urine ACR is often interpreted together with:</p>"
                "<ul>"
                "<li><a href=\"/en/blog/creatinine-egfr-what-it-means\">Creatinine and eGFR</a> to understand overall kidney filtration.</li>"
                "<li><a href=\"/en/blog/how-to-read-fasting-blood-sugar-results\">Fasting glucose</a> and <a href=\"/en/blog/what-does-an-hba1c-result-mean\">HbA1c</a> when diabetes or prediabetes is relevant.</li>"
                "<li>Blood pressure history, swelling, and medication review.</li>"
                "<li><a href=\"/en/blog/metabolic-panel-results-explained\">Metabolic panel markers</a> when the kidney pattern sits inside a wider chemistry panel.</li>"
                "</ul>"
                "<p>That combined view helps separate a temporary urine finding from a pattern that deserves closer kidney follow-up.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevated: quick pattern guide",
            body_html=(
                "<div class=\"blog-example\"><strong>In range:</strong> usually reassuring, especially if creatinine, eGFR, and blood pressure are also stable.</div>"
                "<div class=\"blog-example\"><strong>Mildly elevated:</strong> often leads to repeat urine ACR and a review of glucose, blood pressure, exercise, and temporary causes.</div>"
                "<div class=\"blog-example\"><strong>Persistently elevated:</strong> makes doctors think more seriously about early kidney damage and long-term kidney or cardiovascular risk reduction.</div>"
                "<div class=\"blog-example\"><strong>Elevated plus worsening creatinine/eGFR:</strong> usually needs a more focused kidney work-up.</div>"
            ),
        ),
        Section(
            id="when-repeat-testing-happens",
            level=2,
            heading="Why repeat testing is common",
            body_html=(
                "<p>A urine ACR can change from day to day. Clinicians often repeat it because a single "
                "sample can be affected by recent exercise, illness, hydration changes, or collection factors. "
                "Persistent elevation across repeated samples matters more than one isolated abnormal result.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="How to use this with your own report",
            body_html=(
                "<p>If your blood work and urine tests are spread across multiple pages, start with "
                "<a href=\"/en/blood-test-results-explained\">blood test results explained</a> or "
                "<a href=\"/en/upload-blood-test-results\">upload your blood test results</a> to turn "
                "the numbers into a single structured summary. That makes it easier to compare urine ACR "
                "with creatinine, eGFR, glucose, and blood pressure-related context before your appointment.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Disclaimer",
            body_html=(
                "<p><strong>This guide is educational only.</strong> Urine ACR does not diagnose kidney disease "
                "on its own. A clinician should interpret it with repeat testing, symptoms, blood pressure, blood "
                "tests, and your overall medical history.</p>"
            ),
        ),
    ]


def _sections_tr():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Kısa cevap: idrar ACR neyi ölçer?",
            body_html=(
                "<p><strong>İdrar ACR</strong>, <strong>albümin/kreatinin oranı</strong> anlamına gelir. "
                "İdrardaki albümin miktarını kreatinine göre değerlendirir; böylece örneğin ne kadar "
                "yoğun veya seyreltilmiş olduğunun etkisini azaltır. Özellikle diyabet, yüksek tansiyon "
                "veya kronik böbrek hastalığı riski olan kişilerde <strong>erken böbrek hasarını</strong> "
                "araştırmak için kullanılır.</p>"
            ),
        ),
        Section(
            id="microalbumin-vs-acr",
            level=2,
            heading="İdrar ACR ile mikroalbümin testi aynı şey mi?",
            body_html=(
                "<p>Günlük kullanımda <strong>mikroalbümin</strong> ve <strong>idrar ACR</strong> "
                "ifadeleri sık sık birbirinin yerine kullanılır. Pratikte ACR daha kullanışlıdır; "
                "çünkü albümini aynı örnekteki kreatinin ile karşılaştırır ve farklı örnekler arasında "
                "sonucu daha anlamlı hale getirir. Bu nedenle birçok laboratuvar artık tek başına "
                "albümin yerine albümin/kreatinin oranını raporlar.</p>"
            ),
        ),
        Section(
            id="what-high-acr-means",
            level=2,
            heading="Yüksek idrar ACR ne anlama gelebilir?",
            body_html=(
                "<p>İdrar ACR yüksek olduğunda böbrekler beklenenden fazla albümini idrara geçiriyor "
                "olabilir. Doktorlar bu tabloda özellikle <strong>diyabet, tansiyon, böbrek hastalığı "
                "riski ve kardiyovasküler risk</strong> açısından düşünür. Ancak sonuç her zaman bağlamla "
                "yorumlanmalıdır: egzersiz, ateş, enfeksiyon, adet dönemi, susuzluk veya geçici hastalıklar "
                "idrar örneğini etkileyebilir.</p>"
                "<p>Bu yüzden tek bir yüksek ACR çoğu zaman doğrudan tanı koydurmaz; tekrar test ve daha "
                "geniş böbrek değerlendirmesi istenir.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-it",
            level=2,
            heading="Doktorlar idrar ACR'yi kan testleriyle nasıl karşılaştırır?",
            body_html=(
                "<p>İdrar ACR sıklıkla şu değerlerle birlikte yorumlanır:</p>"
                "<ul>"
                "<li><a href=\"/tr/blog/creatinine-egfr-what-it-means\">Kreatinin ve eGFR</a>: genel böbrek süzme fonksiyonunu görmek için.</li>"
                "<li><a href=\"/tr/blog/aclik-kan-sekeri-sonucu-nasil-degerlendirilir\">Açlık glukozu</a> ve <a href=\"/tr/blog/hba1c-sonucu-ne-anlama-gelir\">HbA1c</a>: diyabet veya prediyabet bağlamında.</li>"
                "<li>Tansiyon öyküsü, ödem ve ilaç değerlendirmesi.</li>"
                "<li><a href=\"/tr/blog/metabolik-panel-sonuclari-nasil-yorumlanir\">Metabolik panel belirteçleri</a>: böbrek örüntüsü daha geniş biyokimya paneli içinde görülüyorsa.</li>"
                "</ul>"
                "<p>Bu birlikte okuma, geçici bir idrar bulgusunu daha kalıcı böbrek riski örüntüsünden ayırmaya yardımcı olur.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal ve yüksek örüntüler: hızlı rehber",
            body_html=(
                "<div class=\"blog-example\"><strong>Normal aralıkta:</strong> Özellikle kreatinin, eGFR ve tansiyon da stabilse genelde rahatlatıcıdır.</div>"
                "<div class=\"blog-example\"><strong>Hafif yüksek:</strong> Genellikle tekrar idrar ACR, glukoz, tansiyon, egzersiz ve geçici nedenlerin gözden geçirilmesini gerektirir.</div>"
                "<div class=\"blog-example\"><strong>Kalıcı yüksek:</strong> Doktorları erken böbrek hasarı ve uzun vadeli böbrek-kalp damar riski açısından daha fazla düşündürür.</div>"
                "<div class=\"blog-example\"><strong>Yüksek ACR + bozulan kreatinin/eGFR:</strong> Daha odaklı böbrek incelemesi gerektirme olasılığı artar.</div>"
            ),
        ),
        Section(
            id="when-repeat-testing-happens",
            level=2,
            heading="Neden tekrar test sık istenir?",
            body_html=(
                "<p>İdrar ACR günler arasında değişebilir. Tek bir örnek son egzersiz, hastalık, hidrasyon "
                "veya örnek toplama koşullarından etkilenebilir. Bu yüzden kalıcı yükseklik, tek bir "
                "anormal sonuçtan daha anlamlı kabul edilir.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="Kendi raporunuzla birlikte nasıl kullanılır?",
            body_html=(
                "<p>Kan ve idrar sonuçlarınız raporun farklı yerlerine yayılmışsa, "
                "<a href=\"/tr/kan-tahlili-sonucu\">kan tahlili sonucu açıklaması</a> sayfasından başlayabilir "
                "veya <a href=\"/tr/kan-tahlili-yukle\">sonucunuzu yükleyebilirsiniz</a>. Böylece idrar ACR'yi "
                "kreatinin, eGFR, glukoz ve tansiyon bağlamıyla tek bir yapıda görmek kolaylaşır.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Uyarı",
            body_html=(
                "<p><strong>Bu rehber yalnızca eğitim amaçlıdır.</strong> İdrar ACR tek başına böbrek "
                "hastalığı tanısı koydurmaz. Sonuç; tekrar test, semptomlar, tansiyon, kan testleri ve "
                "kişisel tıbbi öykü ile birlikte doktor tarafından değerlendirilmelidir.</p>"
            ),
        ),
    ]


def _sections_de():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Kurze Antwort: Was misst der Urin-ACR?",
            body_html=(
                "<p><strong>Urin-ACR</strong> steht für <strong>Albumin-Kreatinin-Quotient</strong>. "
                "Er setzt die Albuminmenge im Urin ins Verhältnis zum Kreatinin und gleicht dadurch "
                "besser aus, wie konzentriert oder verdünnt die Probe ist. Er wird häufig genutzt, "
                "um nach <strong>frühen Nierenschäden</strong> zu suchen, besonders bei Diabetes, "
                "Bluthochdruck oder erhöhtem Risiko für chronische Nierenerkrankungen.</p>"
            ),
        ),
        Section(
            id="microalbumin-vs-acr",
            level=2,
            heading="Ist Urin-ACR dasselbe wie ein Mikroalbumin-Test?",
            body_html=(
                "<p>Im Alltag werden <strong>Mikroalbumin</strong> und <strong>Urin-ACR</strong> oft "
                "gleichgesetzt. Praktisch ist der ACR aber aussagekräftiger, weil Albumin im Verhältnis "
                "zum Kreatinin derselben Probe bewertet wird. Dadurch lassen sich unterschiedliche "
                "Urinproben besser vergleichen. Deshalb berichten viele Labore heute den "
                "Albumin-Kreatinin-Quotienten statt Albumin allein.</p>"
            ),
        ),
        Section(
            id="what-high-acr-means",
            level=2,
            heading="Was kann ein hoher Urin-ACR bedeuten?",
            body_html=(
                "<p>Ein erhöhter Urin-ACR kann bedeuten, dass die Nieren mehr Albumin als erwartet in "
                "den Urin gelangen lassen. Ärzte denken dabei oft an <strong>Diabetes, Blutdruck, "
                "Nierenrisiko und kardiovaskuläres Risiko</strong>. Trotzdem braucht der Wert immer "
                "Kontext: Sport, Fieber, Infekte, Menstruation, Dehydrierung oder vorübergehende "
                "Erkrankungen können eine Urinprobe ebenfalls beeinflussen.</p>"
                "<p>Darum führt ein einzelner erhöhter ACR meist eher zu <strong>Kontrollmessungen</strong> "
                "oder einer breiteren Nierenabklärung als direkt zu einer Diagnose.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-it",
            level=2,
            heading="Wie Ärzte den Urin-ACR mit Blutwerten vergleichen",
            body_html=(
                "<p>Der Urin-ACR wird oft zusammen mit folgenden Werten gelesen:</p>"
                "<ul>"
                "<li><a href=\"/de/blog/creatinine-egfr-what-it-means\">Kreatinin und eGFR</a>, um die gesamte Nierenfiltration besser einzuordnen.</li>"
                "<li><a href=\"/de/blog/nuechternblutzucker-verstehen\">Nüchternglukose</a> und <a href=\"/de/blog/hba1c-verstehen-was-bedeutet-der-wert\">HbA1c</a>, wenn Diabetes oder Prädiabetes im Raum steht.</li>"
                "<li>Blutdruck, Schwellungen und Medikamentenanamnese.</li>"
                "<li><a href=\"/de/blog/stoffwechselpanel-cmp-bmp-verstehen\">Marker aus dem Stoffwechselpanel</a>, wenn das Nierenmuster Teil eines breiteren Chemiebefunds ist.</li>"
                "</ul>"
                "<p>Diese kombinierte Sicht hilft dabei, einen vorübergehenden Urinbefund von einem "
                "Muster zu unterscheiden, das eher für ein erhöhtes Nierenrisiko spricht.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normale und erhöhte Muster: schneller Überblick",
            body_html=(
                "<div class=\"blog-example\"><strong>Im Normbereich:</strong> meist beruhigend, vor allem wenn Kreatinin, eGFR und Blutdruck ebenfalls stabil sind.</div>"
                "<div class=\"blog-example\"><strong>Leicht erhöht:</strong> führt häufig zu einer Wiederholung des Urin-ACR und zur Überprüfung von Glukose, Blutdruck, Sport und vorübergehenden Ursachen.</div>"
                "<div class=\"blog-example\"><strong>Anhaltend erhöht:</strong> lässt eher an frühen Nierenschaden und langfristige Nieren- oder Herz-Kreislauf-Risiken denken.</div>"
                "<div class=\"blog-example\"><strong>Erhöht plus verschlechtertes Kreatinin/eGFR:</strong> spricht eher für eine gezielte Nierenabklärung.</div>"
            ),
        ),
        Section(
            id="when-repeat-testing-happens",
            level=2,
            heading="Warum Wiederholungstests so häufig sind",
            body_html=(
                "<p>Ein Urin-ACR kann sich von Tag zu Tag verändern. Eine einzelne Probe kann durch "
                "Sport, Infekt, Hydrierung oder die Probengewinnung beeinflusst werden. Eine anhaltende "
                "Erhöhung über mehrere Messungen ist deshalb aussagekräftiger als ein einmaliger Ausreißer.</p>"
            ),
        ),
        Section(
            id="use-with-your-report",
            level=2,
            heading="Wie Sie das mit Ihrem eigenen Befund nutzen",
            body_html=(
                "<p>Wenn Blut- und Urinwerte auf verschiedene Seiten Ihres Befunds verteilt sind, "
                "beginnen Sie mit <a href=\"/de/blood-test-results\">Blutwerte verstehen</a> oder "
                "<a href=\"/analyze\">starten Sie eine Analyse</a>. So lassen sich Urin-ACR, Kreatinin, eGFR, Glukose und Blutdruck "
                "im selben Zusammenhang besser überblicken.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Hinweis",
            body_html=(
                "<p><strong>Dieser Leitfaden dient nur der Information.</strong> Ein erhöhter Urin-ACR "
                "stellt für sich keine Diagnose einer Nierenerkrankung dar. Der Wert sollte zusammen mit "
                "Kontrolltests, Symptomen, Blutdruck, Blutwerten und Ihrer Krankengeschichte ärztlich "
                "eingeordnet werden.</p>"
            ),
        ),
    ]


def _sections_es():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="Respuesta rápida: qué mide el ACR urinario", body_html=(
            "<p>El <strong>ACR urinario</strong> es la <strong>relación albúmina/creatinina</strong> en una muestra de orina. Ayuda a detectar pérdida de albúmina por el riñón y corrige mejor la concentración de la muestra.</p>"
        )),
        Section(id="microalbumin-vs-acr", level=2, heading="¿Es lo mismo que una microalbuminuria?", body_html=(
            "<p>En la práctica, muchas personas usan ambos términos como si fueran lo mismo. El ACR suele ser más útil porque compara albúmina con creatinina en la misma muestra.</p>"
        )),
        Section(id="what-high-acr-means", level=2, heading="Qué puede significar un ACR urinario alto", body_html=(
            "<p>Un ACR alto puede sugerir que el riñón deja pasar más albúmina de la esperada. Los médicos piensan en diabetes, presión arterial, riesgo renal y riesgo cardiovascular, pero el resultado siempre necesita contexto.</p>"
            "<p>Ejercicio, infección, fiebre, deshidratación o una situación temporal también pueden alterar la muestra.</p>"
        )),
        Section(id="how-doctors-compare-it", level=2, heading="Cómo se compara con análisis de sangre", body_html=(
            "<ul>"
            "<li><a href=\"/es/blog/creatinine-egfr-what-it-means\">Creatinina y eGFR</a> para valorar la filtración renal.</li>"
            "<li><a href=\"/es/blog/como-leer-glucosa-en-ayunas\">Glucosa en ayunas</a> y <a href=\"/es/blog/hba1c-que-significa-el-resultado\">HbA1c</a> si se sospecha diabetes o prediabetes.</li>"
            "<li>Presión arterial, edemas y revisión de medicación.</li>"
            "<li><a href=\"/es/blog/panel-metabolico-cmp-bmp-explicado\">Marcadores del panel metabólico</a> si el patrón renal forma parte de una química más amplia.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="Patrones normales y elevados", body_html=(
            "<div class=\"blog-example\"><strong>En rango:</strong> suele ser tranquilizador, especialmente si creatinina, eGFR y presión arterial también están estables.</div>"
            "<div class=\"blog-example\"><strong>Elevación leve:</strong> suele llevar a repetir la prueba y revisar glucosa, tensión, ejercicio y causas temporales.</div>"
            "<div class=\"blog-example\"><strong>Elevación persistente:</strong> hace pensar más en daño renal precoz o mayor riesgo renal/cardiovascular.</div>"
        )),
        Section(id="when-repeat-testing-happens", level=2, heading="Por qué se repite con frecuencia", body_html=(
            "<p>El ACR urinario puede cambiar entre días. Por eso una elevación persistente en varias muestras suele ser más importante que un resultado aislado.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="Cómo usarlo con tu informe", body_html=(
            "<p>Puedes empezar por <a href=\"/es/blood-test-results\">resultados de análisis</a> o <a href=\"/es/upload-blood-test-results\">subir tus resultados</a> para comparar el ACR con creatinina, eGFR y glucosa en un solo resumen.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Aviso", body_html=(
            "<p><strong>Este contenido es informativo.</strong> Un ACR urinario alto no diagnostica por sí solo una enfermedad renal. Debe valorarse con repetición, otros análisis y contexto clínico.</p>"
        )),
    ]


def _sections_fr():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="Réponse rapide : que mesure l'ACR urinaire ?", body_html=(
            "<p>L'<strong>ACR urinaire</strong> est le <strong>rapport albumine/créatinine</strong> dans un échantillon d'urine. Il aide à détecter une fuite d'albumine par le rein tout en corrigeant mieux la concentration de l'échantillon.</p>"
        )),
        Section(id="microalbumin-vs-acr", level=2, heading="Est-ce la même chose qu'une microalbuminurie ?", body_html=(
            "<p>Dans le langage courant, les deux termes sont souvent confondus. En pratique, l'ACR est plus utile car il compare l'albumine à la créatinine dans le même prélèvement.</p>"
        )),
        Section(id="what-high-acr-means", level=2, heading="Que peut signifier un ACR urinaire élevé ?", body_html=(
            "<p>Un ACR élevé peut suggérer que le rein laisse passer plus d'albumine que prévu. Les médecins pensent alors au diabète, à la tension artérielle, au risque rénal et cardiovasculaire, mais le résultat doit toujours être replacé dans son contexte.</p>"
            "<p>L'exercice, la fièvre, une infection, la déshydratation ou une situation temporaire peuvent aussi modifier le résultat.</p>"
        )),
        Section(id="how-doctors-compare-it", level=2, heading="Comment il est comparé aux analyses sanguines", body_html=(
            "<ul>"
            "<li><a href=\"/fr/blog/creatinine-egfr-what-it-means\">Créatinine et eGFR</a> pour la filtration rénale.</li>"
            "<li><a href=\"/fr/blog/comment-lire-glycemie-a-jeun\">Glycémie à jeun</a> et <a href=\"/fr/blog/hba1c-comprendre-resultat\">HbA1c</a> en cas de contexte diabétique.</li>"
            "<li>Tension artérielle, oedèmes et médicaments.</li>"
            "<li><a href=\"/fr/blog/bilan-metabolique-cmp-bmp-explication\">Marqueurs du bilan métabolique</a> si le profil rénal s'inscrit dans une chimie plus large.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="Profils normaux et élevés", body_html=(
            "<div class=\"blog-example\"><strong>Dans la norme :</strong> plutôt rassurant, surtout si la créatinine, l'eGFR et la tension sont stables.</div>"
            "<div class=\"blog-example\"><strong>Légèrement élevé :</strong> conduit souvent à répéter le test et à revoir glycémie, tension, exercice et causes transitoires.</div>"
            "<div class=\"blog-example\"><strong>Élévation persistante :</strong> fait davantage penser à une atteinte rénale précoce ou à un risque rénal/cardiovasculaire plus élevé.</div>"
        )),
        Section(id="when-repeat-testing-happens", level=2, heading="Pourquoi répéter le test est fréquent", body_html=(
            "<p>L'ACR urinaire peut varier d'un jour à l'autre. Une élévation confirmée sur plusieurs prélèvements est donc plus importante qu'un seul résultat isolé.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="Comment l'utiliser avec votre compte rendu", body_html=(
            "<p>Vous pouvez commencer par <a href=\"/fr/blood-test-results\">résultats d'analyses</a> ou <a href=\"/fr/upload-blood-test-results\">télécharger vos résultats</a> pour voir l'ACR, la créatinine, l'eGFR et le glucose dans un résumé structuré.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Avertissement", body_html=(
            "<p><strong>Ce contenu est informatif.</strong> Un ACR urinaire élevé ne suffit pas à diagnostiquer une maladie rénale. Il doit être interprété avec des contrôles répétés et le contexte clinique.</p>"
        )),
    ]


def _sections_it():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="Risposta rapida: cosa misura l'ACR urinario", body_html=(
            "<p>L'<strong>ACR urinario</strong> è il <strong>rapporto albumina/creatinina</strong> in un campione di urina. Aiuta a rilevare la perdita di albumina dal rene correggendo meglio la concentrazione del campione.</p>"
        )),
        Section(id="microalbumin-vs-acr", level=2, heading="È la stessa cosa della microalbuminuria?", body_html=(
            "<p>Nell'uso comune i due termini vengono spesso sovrapposti. In pratica l'ACR è più utile perché confronta albumina e creatinina nello stesso campione.</p>"
        )),
        Section(id="what-high-acr-means", level=2, heading="Cosa può significare un ACR urinario alto", body_html=(
            "<p>Un ACR alto può suggerire che il rene stia lasciando passare più albumina del previsto. I medici pensano spesso a diabete, pressione, rischio renale e cardiovascolare, ma il dato va sempre letto nel contesto.</p>"
            "<p>Esercizio, febbre, infezioni, disidratazione o situazioni temporanee possono influenzare il risultato.</p>"
        )),
        Section(id="how-doctors-compare-it", level=2, heading="Come viene confrontato con gli esami del sangue", body_html=(
            "<ul>"
            "<li><a href=\"/it/blog/creatinine-egfr-what-it-means\">Creatinina ed eGFR</a> per la filtrazione renale.</li>"
            "<li><a href=\"/it/blog/come-leggere-glicemia-a-digiuno\">Glicemia a digiuno</a> e <a href=\"/it/blog/hba1c-cosa-significa-il-valore\">HbA1c</a> se c'è contesto diabetico.</li>"
            "<li>Pressione arteriosa, edemi e farmaci.</li>"
            "<li><a href=\"/it/blog/pannello-metabolico-cmp-bmp-spiegato\">Marker del pannello metabolico</a> se il quadro renale fa parte di una chimica più ampia.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="Pattern normali ed elevati", body_html=(
            "<div class=\"blog-example\"><strong>Nei limiti:</strong> spesso rassicurante, soprattutto se creatinina, eGFR e pressione sono stabili.</div>"
            "<div class=\"blog-example\"><strong>Lievemente alto:</strong> porta spesso a ripetere il test e rivedere glucosio, pressione, esercizio e cause temporanee.</div>"
            "<div class=\"blog-example\"><strong>Persistente:</strong> fa pensare di più a danno renale precoce o a maggior rischio renale/cardiovascolare.</div>"
        )),
        Section(id="when-repeat-testing-happens", level=2, heading="Perché si ripete spesso", body_html=(
            "<p>L'ACR urinario può cambiare da un giorno all'altro. Un'alterazione confermata in più campioni conta più di un singolo valore isolato.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="Come usarlo con il tuo referto", body_html=(
            "<p>Puoi iniziare da <a href=\"/it/blood-test-results\">risultati esami</a> oppure <a href=\"/it/upload-blood-test-results\">caricare i risultati</a> per vedere ACR, creatinina, eGFR e glucosio nello stesso riepilogo.</p>"
        )),
        Section(id="disclaimer", level=2, heading="Disclaimer", body_html=(
            "<p><strong>Questo contenuto è informativo.</strong> Un ACR urinario alto non basta da solo per diagnosticare una malattia renale. Va interpretato con controlli ripetuti e contesto clinico.</p>"
        )),
    ]


def _sections_he():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="תשובה קצרה: מה מודד ACR בשתן", body_html=(
            "<p><strong>ACR בשתן</strong> הוא <strong>יחס אלבומין לקריאטינין</strong> בדגימת שתן. הוא עוזר לזהות דליפה של אלבומין דרך הכליה ומתקן טוב יותר את ריכוז הדגימה.</p>"
        )),
        Section(id="what-high-acr-means", level=2, heading="מה יכולה לרמוז תוצאה גבוהה?", body_html=(
            "<p>ACR גבוה יכול לרמוז שהכליה מעבירה יותר אלבומין מהצפוי. הרופאים משווים זאת לסוכרת, לחץ דם, סיכון כלייתי וסיכון לבבי, אבל תמיד צריך לפרש את התוצאה בהקשר.</p>"
            "<p>גם מאמץ, חום, זיהום, התייבשות או מצב זמני יכולים להשפיע על המדידה.</p>"
        )),
        Section(id="how-doctors-compare-it", level=2, heading="איך משווים את זה לבדיקות אחרות", body_html=(
            "<ul>"
            "<li><a href=\"/he/blog/creatinine-egfr-what-it-means\">קריאטינין ו-eGFR</a> להבנת סינון הכליה.</li>"
            "<li>סוכר, לחץ דם ותרופות נותנים את התמונה הרחבה יותר.</li>"
            "<li><a href=\"/he/blog/פענוח-פאנל-מטבולי-cmp-bmp\">הפאנל המטבולי</a> עוזר כאשר יש גם הקשר כימי רחב יותר.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="דפוסים שכיחים", body_html=(
            "<div class=\"blog-example\"><strong>בתחום התקין:</strong> לרוב מרגיע, במיוחד אם קריאטינין ו-eGFR יציבים.</div>"
            "<div class=\"blog-example\"><strong>עלייה קלה:</strong> לעיתים מובילה לחזרה על הבדיקה ולבדיקת לחץ דם, סוכר וסיבות זמניות.</div>"
            "<div class=\"blog-example\"><strong>עלייה מתמשכת:</strong> מחזקת יותר את הצורך בבירור של סיכון כלייתי מוקדם.</div>"
        )),
        Section(id="repeat-testing", level=2, heading="למה חוזרים על הבדיקה", body_html=(
            "<p>ACR בשתן יכול להשתנות בין ימים שונים, ולכן כמה דגימות חריגות חשובות יותר מתוצאה בודדת.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="איך להשתמש בזה עם הדוח שלך", body_html=(
            "<p>אפשר להתחיל ב-<a href=\"/he/blood-test-results\">תוצאות בדיקות דם</a> או <a href=\"/he/upload-blood-test-results\">להעלות תוצאות</a> כדי לראות ACR לצד קריאטינין ו-eGFR.</p>"
        )),
        Section(id="disclaimer", level=2, heading="הבהרה", body_html=(
            "<p><strong>המידע כאן כללי בלבד.</strong> ACR גבוה אינו מאבחן לבדו מחלת כליה, וצריך לפרש אותו יחד עם בדיקות נוספות והקשר קליני.</p>"
        )),
    ]


def _sections_hi():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="संक्षिप्त उत्तर: यूरिन ACR क्या मापता है", body_html=(
            "<p><strong>यूरिन ACR</strong> यानी <strong>albumin-creatinine ratio</strong> एक यूरिन सैंपल में एल्बुमिन और क्रिएटिनिन का अनुपात है। इससे पता चलता है कि किडनी एल्बुमिन लीक तो नहीं कर रही.</p>"
        )),
        Section(id="what-high-acr-means", level=2, heading="ऊंचा ACR क्या संकेत दे सकता है", body_html=(
            "<p>ऊंचा ACR यह दिखा सकता है कि किडनी जरूरत से ज्यादा एल्बुमिन बाहर जाने दे रही है। डॉक्टर इसे डायबिटीज, ब्लड प्रेशर, किडनी रिस्क और कार्डियोवैस्कुलर रिस्क के संदर्भ में देखते हैं.</p>"
            "<p>व्यायाम, बुखार, इन्फेक्शन, डिहाइड्रेशन या अस्थायी कारण भी रिज़ल्ट को बदल सकते हैं.</p>"
        )),
        Section(id="how-doctors-compare-it", level=2, heading="इसे किन टेस्ट के साथ देखा जाता है", body_html=(
            "<ul>"
            "<li><a href=\"/hi/blog/creatinine-egfr-what-it-means\">क्रिएटिनिन और eGFR</a> किडनी फ़िल्ट्रेशन के लिए.</li>"
            "<li>ब्लड शुगर, ब्लड प्रेशर और दवाओं की जानकारी.</li>"
            "<li><a href=\"/hi/blog/metabolic-panel-cmp-bmp-samjhein\">मेटाबोलिक पैनल</a> अगर व्यापक केमिस्ट्री पैटर्न भी देखना हो.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="सामान्य और बढ़े हुए पैटर्न", body_html=(
            "<div class=\"blog-example\"><strong>नॉर्मल रेंज:</strong> अक्सर आश्वस्त करने वाला, खासकर जब क्रिएटिनिन और eGFR भी स्थिर हों.</div>"
            "<div class=\"blog-example\"><strong>हल्का बढ़ा हुआ:</strong> अक्सर टेस्ट दोहराया जाता है और शुगर, प्रेशर व अस्थायी कारण देखे जाते हैं.</div>"
            "<div class=\"blog-example\"><strong>बार-बार बढ़ा हुआ:</strong> शुरुआती किडनी डैमेज या बढ़े हुए किडनी-रिस्क की ओर ज्यादा संकेत दे सकता है.</div>"
        )),
        Section(id="repeat-testing", level=2, heading="टेस्ट दोहराना क्यों आम है", body_html=(
            "<p>यूरिन ACR दिन-प्रतिदिन बदल सकता है. इसलिए कई नमूनों में बना रहने वाला बदलाव, एक अकेले रिज़ल्ट से ज्यादा मायने रखता है.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="अपनी रिपोर्ट में इसे कैसे देखें", body_html=(
            "<p>आप <a href=\"/hi/blood-test-results\">blood test results</a> या <a href=\"/hi/upload-blood-test-results\">results upload</a> से शुरू कर सकते हैं ताकि ACR, क्रिएटिनिन और eGFR साथ दिखें.</p>"
        )),
        Section(id="disclaimer", level=2, heading="डिस्क्लेमर", body_html=(
            "<p><strong>यह सामग्री केवल जानकारी के लिए है.</strong> ऊंचा यूरिन ACR अकेले किडनी रोग का निदान नहीं करता. सही व्याख्या डॉक्टर के साथ करें.</p>"
        )),
    ]


def _sections_ar():
    from app.blog_i18n import Section

    return [
        Section(id="quick-answer", level=2, heading="إجابة سريعة: ماذا يقيس ACR في البول؟", body_html=(
            "<p><strong>ACR البول</strong> هو <strong>نسبة الألبومين إلى الكرياتينين</strong> في عينة بول. يساعد هذا الفحص على كشف تسرب الألبومين من الكلى مع تصحيح أفضل لتركيز العينة.</p>"
        )),
        Section(id="what-high-acr-means", level=2, heading="ماذا قد تعني النتيجة المرتفعة؟", body_html=(
            "<p>قد تشير النتيجة المرتفعة إلى أن الكلى تسمح بمرور كمية أكبر من الألبومين. يفكر الأطباء هنا في السكري وضغط الدم ومخاطر الكلى والمخاطر القلبية الوعائية، لكن النتيجة تحتاج دائماً إلى سياق.</p>"
            "<p>كما يمكن للرياضة أو الحمى أو العدوى أو الجفاف أو سبب مؤقت أن يغير النتيجة.</p>"
        )),
        Section(id="how-doctors-compare-it", level=2, heading="كيف يُقارن مع تحاليل أخرى", body_html=(
            "<ul>"
            "<li><a href=\"/ar/blog/creatinine-egfr-what-it-means\">الكرياتينين وeGFR</a> لفهم ترشيح الكلى.</li>"
            "<li>سكر الدم وضغط الدم والأدوية تعطي السياق الأوسع.</li>"
            "<li><a href=\"/ar/blog/شرح-لوحة-الأيض-cmp-bmp\">لوحة الأيض</a> مفيدة إذا كانت الصورة جزءاً من تحاليل كيمياء أوسع.</li>"
            "</ul>"
        )),
        Section(id="pattern-guide", level=2, heading="أنماط شائعة", body_html=(
            "<div class=\"blog-example\"><strong>ضمن الطبيعي:</strong> يكون مطمئناً غالباً، خاصة إذا كانت الكرياتينين وeGFR مستقرين.</div>"
            "<div class=\"blog-example\"><strong>ارتفاع بسيط:</strong> يؤدي كثيراً إلى إعادة الفحص ومراجعة السكر والضغط والأسباب المؤقتة.</div>"
            "<div class=\"blog-example\"><strong>ارتفاع مستمر:</strong> يزيد الشك بوجود خطر كلوي مبكر أو ارتفاع في الخطر الكلوي والقلب الوعائي.</div>"
        )),
        Section(id="repeat-testing", level=2, heading="لماذا يُعاد الفحص كثيراً", body_html=(
            "<p>قد يتغير ACR البول من يوم لآخر، لذلك تكون النتائج المرتفعة المتكررة أهم من قراءة واحدة منفردة.</p>"
        )),
        Section(id="use-with-your-report", level=2, heading="كيف تستخدم هذا مع تقريرك", body_html=(
            "<p>يمكنك البدء من <a href=\"/ar/blood-test-results\">نتائج التحاليل</a> أو <a href=\"/ar/upload-blood-test-results\">رفع النتائج</a> لرؤية ACR مع الكرياتينين وeGFR في ملخص واحد.</p>"
        )),
        Section(id="disclaimer", level=2, heading="تنبيه", body_html=(
            "<p><strong>هذه المادة للمعلومات فقط.</strong> ارتفاع ACR البول لا يشخص مرض الكلى بمفرده، ويجب تفسيره مع فحوص أخرى والسياق السريري.</p>"
        )),
    ]


def build_urine_acr_article():
    """Build a dedicated urine ACR / microalbumin article."""
    from app.blog_i18n import Article

    return Article(
        id="urine-acr-microalbumin-meaning",
        published_at=date(2026, 3, 26),
        last_updated=date(2026, 3, 26),
        read_minutes=7,
        cover_image="/static/images/blog/how-to-read-blood-test-results.png",
        category={"en": "Kidney & Metabolic Health", "tr": "Böbrek ve Metabolik Sağlık", "de": "Nieren- & Stoffwechselgesundheit", "es": "Riñón y salud metabólica", "fr": "Reins et santé métabolique", "it": "Reni e salute metabolica", "he": "כליות ובריאות מטבולית", "hi": "किडनी और मेटाबोलिक हेल्थ", "ar": "الكلى والصحة الأيضية"},
        slugs={
            "en": "urine-acr-microalbumin-meaning",
            "tr": "idrar-acr-mikroalbumin-ne-anlama-gelir",
            "de": "urin-acr-mikroalbumin-bedeutung",
            "es": "acr-urinario-microalbumina-significado",
            "fr": "acr-urinaire-microalbuminurie-signification",
            "it": "acr-urinario-microalbumina-significato",
            "he": "acr-שתן-מיקרואלבומין-משמעות",
            "hi": "urine-acr-microalbumin-kya-hai",
            "ar": "acr-البول-ميكروألبومين-المعنى",
        },
        titles={
            "en": "Urine ACR / Microalbumin Meaning: What a High Albumin-Creatinine Ratio Can Suggest",
            "tr": "İdrar ACR / Mikroalbümin Ne Anlama Gelir? Yüksek Albümin-Kreatinin Oranı Ne Gösterebilir?",
            "de": "Urin-ACR / Mikroalbumin: Was ein hoher Albumin-Kreatinin-Quotient bedeuten kann",
            "es": "ACR urinario / microalbúmina: qué puede significar una relación albúmina-creatinina alta",
            "fr": "ACR urinaire / microalbuminurie : ce qu'un rapport albumine-créatinine élevé peut suggérer",
            "it": "ACR urinario / microalbumina: cosa può indicare un rapporto albumina-creatinina alto",
            "he": "ACR בשתן / מיקרואלבומין: מה יכולה לרמוז תוצאה גבוהה",
            "hi": "यूरिन ACR / माइक्रोएल्बुमिन: ऊंचा albumin-creatinine ratio क्या बता सकता है",
            "ar": "ACR البول / الميكروألبومين: ماذا قد تعني نسبة الألبومين إلى الكرياتينين المرتفعة",
        },
        subtitles={
            "en": "Understand what urine ACR measures, how it differs from a simple microalbumin result, and why doctors compare it with creatinine, eGFR, glucose, and blood pressure.",
            "tr": "İdrar ACR'nin neyi ölçtüğünü, mikroalbümin sonucundan nasıl farklılaştığını ve doktorların bunu neden kreatinin, eGFR, glukoz ve tansiyonla birlikte yorumladığını öğrenin.",
            "de": "Verstehen Sie, was der Urin-ACR misst, wie er sich von einem einfachen Mikroalbumin-Wert unterscheidet und warum Ärzte ihn mit Kreatinin, eGFR, Glukose und Blutdruck vergleichen.",
            "es": "Aprende qué mide el ACR urinario, en qué se diferencia de una simple microalbuminuria y por qué se compara con creatinina, eGFR, glucosa y tensión arterial.",
            "fr": "Comprenez ce que mesure l'ACR urinaire, en quoi il diffère d'une simple microalbuminurie et pourquoi il est comparé à la créatinine, à l'eGFR, au glucose et à la tension.",
            "it": "Scopri cosa misura l'ACR urinario, in cosa differisce da un semplice valore di microalbumina e perché viene confrontato con creatinina, eGFR, glucosio e pressione.",
            "he": "הבינו מה מודד ACR בשתן, איך הוא שונה ממיקרואלבומין פשוט ולמה משווים אותו לקריאטינין, eGFR, סוכר ולחץ דם.",
            "hi": "जानें कि यूरिन ACR क्या मापता है, यह साधारण माइक्रोएल्बुमिन रिज़ल्ट से कैसे अलग है और डॉक्टर इसे क्रिएटिनिन, eGFR, शुगर और ब्लड प्रेशर के साथ क्यों देखते हैं.",
            "ar": "تعرّف على ما يقيسه ACR البول، وكيف يختلف عن نتيجة الميكروألبومين البسيطة، ولماذا يقارنه الأطباء بالكرياتينين وeGFR والجلوكوز وضغط الدم.",
        },
        excerpts={
            "en": "Plain-language guide to urine ACR and microalbumin, including what high results may suggest, when repeat testing is common, and how doctors connect the result to kidney risk.",
            "tr": "İdrar ACR ve mikroalbümini sade dille açıklayan rehber: yüksek sonucun ne düşündürebileceği, neden tekrar test istendiği ve böbrek riskiyle nasıl ilişkilendirildiği.",
            "de": "Verständlicher Leitfaden zu Urin-ACR und Mikroalbumin: was hohe Werte nahelegen können, warum Kontrolltests häufig sind und wie Ärzte das Ergebnis mit Nierenrisiken verknüpfen.",
            "es": "Guía clara sobre ACR urinario y microalbúmina: qué pueden sugerir los valores altos, por qué se repiten y cómo se relacionan con el riesgo renal.",
            "fr": "Guide clair sur l'ACR urinaire et la microalbuminurie : ce que peuvent évoquer des valeurs élevées, pourquoi elles sont souvent répétées et leur lien avec le risque rénal.",
            "it": "Guida chiara su ACR urinario e microalbumina: cosa possono suggerire valori alti, perché si ripetono spesso e come si collegano al rischio renale.",
            "he": "מדריך ברור ל-ACR בשתן ומיקרואלבומין: מה יכולה לרמוז תוצאה גבוהה, למה חוזרים על הבדיקה ואיך זה קשור לסיכון כלייתי.",
            "hi": "यूरिन ACR और माइक्रोएल्बुमिन पर सरल गाइड: ऊंचा रिज़ल्ट क्या दिखा सकता है, टेस्ट क्यों दोहराया जाता है और इसका किडनी रिस्क से क्या संबंध है.",
            "ar": "دليل واضح عن ACR البول والميكروألبومين: ماذا قد تعني النتيجة المرتفعة، ولماذا يُعاد الفحص كثيراً، وكيف يرتبط ذلك بخطر الكلى.",
        },
        seo_titles={
            "en": "Urine ACR / Microalbumin Meaning: High Albumin-Creatinine Ratio | NoryaAI",
            "tr": "İdrar ACR / Mikroalbümin: Yüksek Albümin-Kreatinin Oranı | NoryaAI",
            "de": "Urin-ACR / Mikroalbumin: hoher Albumin-Kreatinin-Quotient | NoryaAI",
            "es": "ACR urinario / microalbúmina: relación albúmina-creatinina alta | NoryaAI",
            "fr": "ACR urinaire / microalbuminurie : rapport albumine-créatinine élevé | NoryaAI",
            "it": "ACR urinario / microalbumina: rapporto albumina-creatinina alto | NoryaAI",
            "he": "ACR בשתן / מיקרואלבומין: יחס אלבומין-קריאטינין גבוה | NoryaAI",
            "hi": "यूरिन ACR / माइक्रोएल्बुमिन: ऊंचा albumin-creatinine ratio | NoryaAI",
            "ar": "ACR البول / الميكروألبومين: ارتفاع نسبة الألبومين إلى الكرياتينين | NoryaAI",
        },
        seo_descriptions={
            "en": "Learn what urine ACR or microalbumin means, why doctors use albumin-creatinine ratio, and how high results are compared with creatinine, eGFR, and glucose.",
            "tr": "İdrar ACR veya mikroalbümin ne demektir? Doktorların neden albümin-kreatinin oranını kullandığını ve yüksek sonuçları kreatinin, eGFR ve glukoz ile nasıl karşılaştırdığını öğrenin.",
            "de": "Erfahren Sie, was Urin-ACR oder Mikroalbumin bedeutet, warum Ärzte den Albumin-Kreatinin-Quotienten nutzen und wie hohe Werte mit Kreatinin, eGFR und Glukose verglichen werden.",
            "es": "Aprende qué significa el ACR urinario o la microalbúmina, por qué se usa la relación albúmina-creatinina y cómo se compara con creatinina, eGFR y glucosa.",
            "fr": "Découvrez ce que signifie l'ACR urinaire ou la microalbuminurie, pourquoi le rapport albumine-créatinine est utilisé et comment il est comparé à la créatinine, à l'eGFR et au glucose.",
            "it": "Scopri cosa significa ACR urinario o microalbumina, perché si usa il rapporto albumina-creatinina e come viene confrontato con creatinina, eGFR e glucosio.",
            "he": "למדו מה המשמעות של ACR בשתן או מיקרואלבומין, למה משתמשים ביחס אלבומין-קריאטינין ואיך משווים תוצאה גבוהה לקריאטינין, eGFR וסוכר.",
            "hi": "जानें यूरिन ACR या माइक्रोएल्बुमिन का क्या मतलब है, डॉक्टर albumin-creatinine ratio क्यों इस्तेमाल करते हैं और ऊंचे रिज़ल्ट को क्रिएटिनिन, eGFR और शुगर से कैसे जोड़ते हैं.",
            "ar": "تعرّف على معنى ACR البول أو الميكروألبومين، ولماذا يستخدم الأطباء نسبة الألبومين إلى الكرياتينين، وكيف تُقارن النتائج المرتفعة بالكرياتينين وeGFR والجلوكوز.",
        },
        sections_by_lang={"en": _sections_en(), "tr": _sections_tr(), "de": _sections_de(), "es": _sections_es(), "fr": _sections_fr(), "it": _sections_it(), "he": _sections_he(), "hi": _sections_hi(), "ar": _sections_ar()},
        cover_alt={
            "en": "Kidney-focused blood and urine test interpretation overview",
            "tr": "Böbrek odaklı kan ve idrar testi yorumlama özeti",
            "de": "Überblick zur nierenbezogenen Interpretation von Blut- und Urintests",
            "es": "Resumen de interpretación renal de análisis de sangre y orina",
            "fr": "Vue d'ensemble de l'interprétation rénale des analyses de sang et d'urine",
            "it": "Panoramica dell'interpretazione renale di esami del sangue e delle urine",
            "he": "סקירה של פירוש בדיקות דם ושתן בהקשר כלייתי",
            "hi": "किडनी-केंद्रित ब्लड और यूरिन टेस्ट व्याख्या का सारांश",
            "ar": "نظرة عامة على تفسير تحاليل الدم والبول المرتبطة بالكلى",
        },
        faq_schema_qa={
            "en": [
                {
                    "question": "What is urine ACR?",
                    "answer": "Urine ACR is the albumin-to-creatinine ratio in a urine sample. It is used to detect albumin leakage from the kidneys and helps adjust for how concentrated the urine is.",
                },
                {
                    "question": "Is urine ACR the same as microalbumin?",
                    "answer": "They are closely related. Many people say microalbumin test, but urine ACR is the more informative report format because it compares albumin with creatinine in the same sample.",
                },
                {
                    "question": "Does a high urine ACR always mean kidney disease?",
                    "answer": "Not always. Temporary illness, exercise, infection, dehydration, and collection factors can affect the result. Doctors usually confirm with repeat testing and compare it with blood tests and blood pressure history.",
                },
                {
                    "question": "What is compared with urine ACR?",
                    "answer": "Doctors often compare urine ACR with creatinine, eGFR, fasting glucose, HbA1c, blood pressure, and sometimes other chemistry markers to understand whether the pattern suggests early kidney damage or a temporary finding.",
                },
            ],
            "tr": [
                {
                    "question": "İdrar ACR nedir?",
                    "answer": "İdrar ACR, idrar örneğindeki albümin ile kreatinin arasındaki orandır. Böbreklerden albümin kaçağını saptamak için kullanılır ve örneğin yoğunluğunu daha iyi dengelemeye yardımcı olur.",
                },
                {
                    "question": "İdrar ACR ile mikroalbümin aynı şey midir?",
                    "answer": "Yakından ilişkilidir. Halk arasında mikroalbümin testi denir, ancak ACR çoğu zaman daha kullanışlıdır çünkü aynı örnekte albümini kreatininle karşılaştırır.",
                },
                {
                    "question": "Yüksek idrar ACR her zaman böbrek hastalığı anlamına gelir mi?",
                    "answer": "Hayır. Geçici hastalık, egzersiz, enfeksiyon, susuzluk ve örnek toplama koşulları sonucu etkileyebilir. Bu nedenle doktorlar genelde tekrar test ve diğer kan değerleriyle birlikte yorumlar.",
                },
            ],
            "de": [
                {
                    "question": "Was ist der Urin-ACR?",
                    "answer": "Der Urin-ACR ist der Albumin-Kreatinin-Quotient in einer Urinprobe. Er hilft, Albuminverluste über die Niere zu erkennen und gleicht die Konzentration der Probe besser aus.",
                },
                {
                    "question": "Ist Urin-ACR dasselbe wie Mikroalbumin?",
                    "answer": "Beides ist eng verwandt. Im Alltag spricht man oft vom Mikroalbumin-Test, aber der ACR ist meist aussagekräftiger, weil Albumin mit Kreatinin derselben Probe verglichen wird.",
                },
                {
                    "question": "Bedeutet ein hoher Urin-ACR immer eine Nierenerkrankung?",
                    "answer": "Nicht unbedingt. Vorübergehende Erkrankungen, Sport, Infektionen, Dehydrierung oder die Probengewinnung können das Ergebnis beeinflussen. Deshalb wird häufig mit Kontrolltests und Blutwerten verglichen.",
                },
            ],
            "es": [
                {"question": "¿Qué es el ACR urinario?", "answer": "Es la relación albúmina/creatinina en una muestra de orina. Se usa para detectar pérdida de albúmina por el riñón y ajustar mejor la concentración de la muestra."},
                {"question": "¿Un ACR alto siempre significa enfermedad renal?", "answer": "No necesariamente. Ejercicio, infección, deshidratación o situaciones temporales pueden alterar el resultado. Por eso suele confirmarse con repetición y otros análisis."},
            ],
            "fr": [
                {"question": "Qu'est-ce que l'ACR urinaire ?", "answer": "C'est le rapport albumine/créatinine dans une urine. Il sert à détecter une fuite d'albumine par le rein tout en corrigeant mieux la concentration de l'échantillon."},
                {"question": "Un ACR élevé signifie-t-il toujours une maladie rénale ?", "answer": "Pas forcément. Exercice, infection, déshydratation ou situation transitoire peuvent modifier le résultat. C'est pourquoi il est souvent contrôlé à nouveau et comparé à d'autres analyses."},
            ],
            "it": [
                {"question": "Che cos'è l'ACR urinario?", "answer": "È il rapporto albumina/creatinina in un campione di urina. Serve a rilevare la perdita di albumina dal rene correggendo meglio la concentrazione del campione."},
                {"question": "Un ACR alto significa sempre malattia renale?", "answer": "Non necessariamente. Esercizio, infezioni, disidratazione o situazioni temporanee possono alterare il risultato. Per questo viene spesso confermato con ripetizione e altri esami."},
            ],
            "he": [
                {"question": "מהו ACR בשתן?", "answer": "זהו יחס אלבומין לקריאטינין בדגימת שתן. הבדיקה עוזרת לזהות דליפה של אלבומין מהכליה ומנטרלת חלק מהשפעת ריכוז הדגימה."},
                {"question": "האם ACR גבוה אומר בוודאות מחלת כליה?", "answer": "לא בהכרח. מאמץ, זיהום, התייבשות או סיבה זמנית יכולים להשפיע על התוצאה. לכן לעיתים קרובות חוזרים על הבדיקה ומשווים לבדיקות נוספות."},
            ],
            "hi": [
                {"question": "यूरिन ACR क्या है?", "answer": "यह यूरिन सैंपल में albumin-creatinine ratio है. इससे किडनी से एल्बुमिन लीक होने के संकेत का बेहतर आकलन किया जाता है."},
                {"question": "क्या ऊंचा ACR हमेशा किडनी बीमारी बताता है?", "answer": "ज़रूरी नहीं. व्यायाम, इन्फेक्शन, डिहाइड्रेशन या अस्थायी कारण रिज़ल्ट बदल सकते हैं. इसलिए टेस्ट दोहराया जाता है और दूसरे मार्कर से तुलना की जाती है."},
            ],
            "ar": [
                {"question": "ما هو ACR البول؟", "answer": "هو نسبة الألبومين إلى الكرياتينين في عينة بول. يساعد على كشف تسرب الألبومين من الكلى مع تصحيح أفضل لتركيز العينة."},
                {"question": "هل يعني ارتفاع ACR دائماً وجود مرض كلوي؟", "answer": "ليس بالضرورة. قد تؤثر الرياضة أو العدوى أو الجفاف أو الأسباب المؤقتة على النتيجة. لذلك يُعاد الفحص كثيراً ويُقارن مع مؤشرات أخرى."},
            ],
        },
    )
