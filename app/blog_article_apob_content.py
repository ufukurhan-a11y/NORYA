"""Blog article for ApoB intent."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what ApoB represents",
            body_html=(
                "<p><strong>ApoB</strong> stands for <strong>apolipoprotein B</strong>. "
                "It is a protein found on the surface of several blood particles that can contribute "
                "to atherosclerosis. In simple terms, ApoB can reflect the <strong>number of "
                "atherogenic particles</strong> moving in the bloodstream.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="What a high ApoB may mean (educational context)",
            body_html=(
                "<p>When clinicians see ApoB higher than expected, they may interpret it as "
                "a signal that more cholesterol-carrying particles are present. Interpretation depends "
                "on your full lipid profile and overall cardiovascular risk factors.</p>"
                "<p>Because lab results can be affected by timing, diet, and other context, one value is "
                "usually not the whole story—your clinician decides whether repeat testing or a broader "
                "risk review is useful.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB vs LDL cholesterol: what is the difference?",
            body_html=(
                "<p><strong>LDL cholesterol</strong> describes the amount of cholesterol carried in LDL particles. "
                "<strong>ApoB</strong> describes the number of particle units that contain ApoB. "
                "Depending on the situation, clinicians may use one or both markers to understand risk patterns.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="How doctors often interpret ApoB with other tests",
            body_html=(
                "<p>In practice, ApoB is often reviewed together with:</p>"
                "<ul>"
                "<li>LDL cholesterol and non-HDL cholesterol targets</li>"
                "<li>Triglycerides and HDL cholesterol</li>"
                "<li>Diabetes markers (when relevant) and blood pressure history</li>"
                "<li>Inflammation context (for example, CRP) depending on the clinician’s approach</li>"
                "</ul>"
                "<p>This combined view helps place ApoB into a broader lipid and cardiovascular picture.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevated: quick pattern guide",
            body_html=(
                "<div class=\"blog-example\"><strong>In range:</strong> typically means your ApoB value is close to what the lab expects for many risk contexts.</div>"
                "<div class=\"blog-example\"><strong>Moderately elevated:</strong> often leads clinicians to review the rest of your lipid profile and consider follow-up.</div>"
                "<div class=\"blog-example\"><strong>Clearly elevated:</strong> may prompt a more focused cardiovascular risk discussion and repeat testing decisions.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="What to do next (with your clinician)",
            body_html=(
                "<p>If you are wondering how ApoB fits your report, start by reviewing it together with your broader lipid results. "
                "If you want a structured summary, you can <a href=\"/en/upload\">upload your blood test results</a>. "
                "Start with <a href=\"/en/blood-test-results-explained\">blood test results explained</a>, "
                "and then use the <a href=\"/en/ai-blood-test-analyzer\">AI blood test analyzer</a> to review the explanation with your clinician.</p>"
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
            heading="Kısa cevap: ApoB neyi anlatır?",
            body_html=(
                "<p><strong>ApoB</strong>, <strong>apolipoprotein B</strong> anlamına gelir. "
                "Aterosklerozla ilişkili olabilen bazı kan partiküllerinin yüzeyinde bulunan bir proteindir. "
                "Basitçe söylemek gerekirse ApoB, kanda dolaşan <strong>aterojenik partikül sayısını</strong> yansıtabilen "
                "bir biyobelirteç olarak değerlendirilir.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="Yüksek ApoB ne anlama gelebilir?",
            body_html=(
                "<p>Doktorlar ApoB değerinin beklendiğinden yüksek olduğunu gördüğünde, "
                "kolesterol taşıyan partiküllerin daha fazla olabileceğini işaret olarak değerlendirebilir. "
                "Ancak yorum, lipid profilinizin tamamı ve kardiyovasküler risk faktörlerinizin birlikte "
                "ele alınmasına bağlıdır.</p>"
                "<p>Laboratuvar sonuçları örnek alma zamanı, beslenme ve başka bağlamlardan etkilenebileceği için "
                "tek bir değer her şey değildir; doktorunuzun tekrar test veya daha geniş bir risk değerlendirmesi "
                "planlayıp planlamayacağına o karar verir.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB vs LDL kolesterol: fark nedir?",
            body_html=(
                "<p><strong>LDL kolesterol</strong> LDL partiküllerinin taşıdığı kolesterol miktarını anlatır. "
                "<strong>ApoB</strong> ise ApoB içeren partikül birimlerinin sayısını temsil eder. "
                "Bazı durumlarda doktorlar risk paternini anlamak için birini veya ikisini birlikte kullanabilir.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="Doktorlar ApoB’yi hangi testlerle birlikte yorumlar?",
            body_html=(
                "<p>Uygulamada ApoB çoğu zaman şu testlerle birlikte gözden geçirilir:</p>"
                "<ul>"
                "<li>LDL ve non-HDL hedefleri / değerleri</li>"
                "<li>Trigliserid ve HDL kolesterol</li>"
                "<li>(Gerekirse) diyabetle ilgili testler ve tansiyon geçmişi</li>"
                "<li>Doktorun yaklaşımına göre inflamasyon bağlamı (ör. CRP)</li>"
                "</ul>"
                "<p>Bu bütüncül bakış ApoB’yi daha geniş bir lipid ve kardiyovasküler çerçeveye yerleştirir.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs yüksek: hızlı desen rehberi",
            body_html=(
                "<div class=\"blog-example\"><strong>Normal aralık:</strong> çoğu risk bağlamında laboratuvarın beklediğine yakın bir ApoB değeri olabileceğini ifade eder.</div>"
                "<div class=\"blog-example\"><strong>Orta düzey yüksek:</strong> doktorların lipid profilinizin geri kalanını gözden geçirmesine ve takip düşünmesine yol açabilir.</div>"
                "<div class=\"blog-example\"><strong>Daha belirgin yüksek:</strong> daha odaklı bir kardiyovasküler risk değerlendirmesi ve tekrar test kararları gündeme gelebilir.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Sıradaki adımlar (doktorunuzla)",
            body_html=(
                "<p>ApoB değerinin raporunuzdaki yerini merak ediyorsanız, "
                "lipid sonuçlarınızın tamamıyla birlikte değerlendirin. Yapılandırılmış bir özet isterseniz "
                "<a href=\"/tr/upload\">kan tahlili sonuçlarınızı yükleyin</a>. "
                "Önce <a href=\"/tr/blood-test-results-explained\">blood test results explained</a> ile hızlı bir çerçeve edinin, "
                "sonra da <a href=\"/tr/ai-blood-test-analyzer\">AI blood test analyzer</a> ile doktorunuzla açıklamayı gözden geçirin.</p>"
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
            heading="Kurz erklärt: Was ApoB zeigt",
            body_html=(
                "<p><strong>ApoB</strong> steht für <strong>Apolipoprotein B</strong>. "
                "Es ist ein Protein, das auf der Oberfläche verschiedener Blutpartikel vorkommt, die mit "
                "Atherosklerose in Zusammenhang stehen können. Vereinfacht gesagt kann ApoB die "
                "<strong>Anzahl atherogener Partikel</strong> im Blut widerspiegeln.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="Was ein hoher ApoB-Wert bedeuten kann",
            body_html=(
                "<p>Wenn Ärztinnen und Ärzte ApoB höher als erwartet sehen, kann das als Hinweis gewertet werden, "
                "dass mehr cholesterintransportierende Partikel vorhanden sind. Die Einordnung hängt jedoch immer "
                "von Ihrem gesamten Lipidprofil und Ihren kardiovaskulären Risikofaktoren ab.</p>"
                "<p>Labwerte können durch Timing, Ernährung und weitere Umstände beeinflusst werden. Deshalb ist "
                "ein einzelner Wert in der Regel nicht die ganze Geschichte—die Ärztin/der Arzt entscheidet, "
                "ob Wiederholungsmessungen oder eine umfassendere Risiko-Einschätzung sinnvoll sind.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB vs. LDL-Cholesterin: der Unterschied",
            body_html=(
                "<p><strong>LDL-Cholesterin</strong> beschreibt die Menge an Cholesterin in LDL-Partikeln. "
                "<strong>ApoB</strong> steht für die Anzahl der Partikel-Einheiten mit ApoB. "
                "Je nach Situation kann daher ein Marker oder auch beides gemeinsam verwendet werden.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="Wie ApoB meist gemeinsam interpretiert wird",
            body_html=(
                "<p>In der Praxis wird ApoB häufig zusammen betrachtet mit:</p>"
                "<ul>"
                "<li>LDL- und Non-HDL-Zielen</li>"
                "<li>Triglyceriden und HDL-Cholesterin</li>"
                "<li>(falls relevant) Diabetes-Markern und der Blutdruck-Historie</li>"
                "<li>Entzündungs-Kontext (z. B. CRP) je nach Ansatz</li>"
                "</ul>"
                "<p>Dieses Gesamtbild ordnet ApoB in ein breiteres Lipid- und Herz-Kreislauf-Profil ein.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs. erhöht: schnelle Orientierung",
            body_html=(
                "<div class=\"blog-example\"><strong>Im Referenzbereich:</strong> bedeutet typischerweise, dass Ihr ApoB-Wert nahe dem liegt, "
                "was das Labor für viele Risikokontexte erwartet.</div>"
                "<div class=\"blog-example\"><strong>Moderat erhöht:</strong> führt oft dazu, dass das übrige Lipidprofil geprüft wird und "
                "Follow-up erwogen wird.</div>"
                "<div class=\"blog-example\"><strong>Deutlich erhöht:</strong> kann eine intensivere Risiko-Diskussion und "
                "Entscheidungen zu Wiederholungsmessungen auslösen.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Was als Nächstes tun (mit Ihrer Ärztin/Arzt)",
            body_html=(
                "<p>Wenn Sie verstehen möchten, wie ApoB zu Ihrem Befund passt, schauen Sie es zusammen mit "
                "Ihrem restlichen Lipidprofil an. Für eine strukturierte Übersicht können Sie "
                "<a href=\"/de/upload\">Ihre Bluttest-Ergebnisse hochladen</a>. "
                "Nutzen Sie <a href=\"/de/blood-test-results-explained\">blood test results explained</a> für eine schnelle Orientierung "
                "und anschließend den <a href=\"/de/ai-blood-test-analyzer\">AI blood test analyzer</a>, um die Erklärung mit Ihrer Ärztin/Ihrem Arzt durchzugehen.</p>"
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
            heading="Respuesta rápida: ¿qué representa la ApoB?",
            body_html=(
                "<p><strong>ApoB</strong> significa <strong>apolipoproteína B</strong>. "
                "Es una proteína que aparece en varios tipos de partículas sanguíneas que pueden contribuir a la aterosclerosis. "
                "En términos simples, ApoB puede reflejar el <strong>número de partículas aterogénicas</strong> presentes en la sangre.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="¿Qué podría significar una ApoB alta?",
            body_html=(
                "<p>Cuando se observa ApoB por encima de lo esperado, los profesionales pueden interpretarlo como una señal de que "
                "hay más partículas que transportan colesterol. La valoración depende del perfil lipídico completo y del riesgo cardiovascular general.</p>"
                "<p>Los resultados de laboratorio pueden variar según el contexto. Por eso, normalmente una única medición no lo explica todo; "
                "su clínico decide si conviene repetir la prueba o revisar el riesgo de forma más amplia.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB vs LDL: ¿en qué se diferencian?",
            body_html=(
                "<p><strong>El colesterol LDL</strong> describe la cantidad de colesterol en las partículas LDL. "
                "<strong>ApoB</strong> describe el número de unidades de partículas que contienen ApoB. "
                "Según la situación, se puede usar uno o ambos marcadores.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="Cómo suelen interpretar la ApoB junto con otras pruebas",
            body_html=(
                "<p>En la práctica, ApoB suele revisarse junto con:</p>"
                "<ul>"
                "<li>Colesterol LDL y objetivos de non-HDL</li>"
                "<li>Triglicéridos y colesterol HDL</li>"
                "<li>Marcadores de diabetes (si aplica) e historial de presión arterial</li>"
                "<li>Contexto inflamatorio (por ejemplo, PCR) según el enfoque del clínico</li>"
                "</ul>"
                "<p>Este conjunto ayuda a encajar la ApoB en una imagen más amplia de lípidos y riesgo cardiovascular.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevada: guía rápida",
            body_html=(
                "<div class=\"blog-example\"><strong>En rango:</strong> suele indicar que su ApoB está cerca de lo esperado para muchos contextos de riesgo.</div>"
                "<div class=\"blog-example\"><strong>Elevación moderada:</strong> a menudo lleva a revisar el resto del perfil lipídico y a considerar seguimiento.</div>"
                "<div class=\"blog-example\"><strong>Elevación clara:</strong> puede motivar una conversación más centrada sobre riesgo cardiovascular y decisiones sobre repetición.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Qué hacer después (con su clínico)",
            body_html=(
                "<p>Si quiere entender cómo encaja la ApoB en su informe, revísela junto con el resto de su perfil lipídico. "
                "Si desea un resumen estructurado, puede <a href=\"/es/upload\">subir sus resultados</a>. "
                "Use <a href=\"/es/blood-test-results-explained\">blood test results explained</a> para una visión rápida "
                "y luego la <a href=\"/es/ai-blood-test-analyzer\">AI blood test analyzer</a> para revisar la explicación con su clínico.</p>"
                "<p>Este contenido es educativo y no sustituye la evaluación médica.</p>"
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
            heading="Réponse rapide : que représente l’ApoB ?",
            body_html=(
                "<p><strong>ApoB</strong> signifie <strong>apolipoprotéine B</strong>. "
                "C’est une protéine présente sur la surface de plusieurs particules circulant dans le sang, "
                "qui peuvent contribuer à l’athérosclérose. En termes simples, l’ApoB peut refléter le "
                "<strong>nombre de particules athérogènes</strong> présentes.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="Que peut indiquer une ApoB élevée (contexte éducatif) ?",
            body_html=(
                "<p>Quand l’ApoB est plus élevée que prévu, les cliniciens peuvent l’interpréter comme un signal "
                "qu’il y a davantage de particules transportant le cholestérol. L’évaluation dépend du profil lipidique complet "
                "et de vos facteurs de risque cardiovasculaire.</p>"
                "<p>Les résultats peuvent varier selon le contexte. Un seul résultat ne raconte donc pas toute l’histoire : "
                "votre clinicien décidera s’il faut répéter le test ou faire une évaluation du risque plus large.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB vs cholestérol LDL : quelle différence ?",
            body_html=(
                "<p><strong>Le LDL</strong> renseigne sur la quantité de cholestérol dans les particules LDL. "
                "<strong>ApoB</strong> correspond au nombre d’unités de particules portant l’ApoB. "
                "Selon la situation, on peut utiliser l’un ou l’autre (ou les deux) pour comprendre le profil.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="Comment on interprète souvent l’ApoB avec d’autres analyses",
            body_html=(
                "<p>En pratique, l’ApoB est souvent examinée avec :</p>"
                "<ul>"
                "<li>LDL et cibles de non-HDL</li>"
                "<li>Triglycérides et HDL</li>"
                "<li>Marqueurs de diabète (si pertinent) et historique de tension artérielle</li>"
                "<li>Contexte inflammatoire (par exemple CRP) selon l’approche</li>"
                "</ul>"
                "<p>Ce point de vue combiné aide à situer l’ApoB dans une image plus large des lipides et du risque cardiovasculaire.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs élevé : repères rapides",
            body_html=(
                "<div class=\"blog-example\"><strong>Dans la norme :</strong> signifie généralement que votre valeur d’ApoB est proche de ce que le laboratoire attend pour de nombreux contextes de risque.</div>"
                "<div class=\"blog-example\"><strong>Légèrement élevée :</strong> mène souvent à revoir le reste du profil lipidique et à envisager un suivi.</div>"
                "<div class=\"blog-example\"><strong>Bien élevée :</strong> peut déclencher une discussion plus centrée sur le risque cardiovasculaire et des décisions de répétition.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Et ensuite (avec votre clinicien)",
            body_html=(
                "<p>Pour comprendre comment l’ApoB s’intègre à votre bilan, regardez-la avec l’ensemble de votre profil lipidique. "
                "Si vous souhaitez un résumé structuré, vous pouvez <a href=\"/fr/upload\">téléverser vos résultats</a>. "
                "Commencez par <a href=\"/fr/blood-test-results-explained\">blood test results explained</a> pour une vue d’ensemble rapide, "
                "puis utilisez le <a href=\"/fr/ai-blood-test-analyzer\">AI blood test analyzer</a> pour relire l’explication avec votre clinicien.</p>"
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
            heading="Risposta rapida: cosa rappresenta ApoB",
            body_html=(
                "<p><strong>ApoB</strong> è <strong>apolipoproteina B</strong>. "
                "È una proteina presente sulla superficie di diverse particelle nel sangue che possono contribuire all’aterosclerosi. "
                "In parole semplici, ApoB può riflettere il <strong>numero di particelle aterogene</strong> in circolo.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="Cosa può significare un valore di ApoB alto",
            body_html=(
                "<p>Se l’ApoB risulta più alta del previsto, i clinici possono interpretarlo come un segnale che ci sono più particelle "
                "che trasportano colesterolo. L’interpretazione dipende dal profilo lipidico completo e dal rischio cardiovascolare generale.</p>"
                "<p>Poiché i risultati di laboratorio possono variare in base al contesto, una singola misurazione non è tutto. "
                "Il tuo medico decide se ripetere il test o rivedere il rischio in modo più ampio.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB vs LDL: differenza essenziale",
            body_html=(
                "<p><strong>Colesterolo LDL</strong> descrive la quantità di colesterolo nelle particelle LDL. "
                "<strong>ApoB</strong> descrive il numero di unità di particelle che contengono ApoB. "
                "A seconda della situazione, possono essere usati uno o entrambi.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="Come si valuta ApoB con altri esami",
            body_html=(
                "<p>In genere ApoB viene considerata insieme a:</p>"
                "<ul>"
                "<li>LDL e obiettivi di non-HDL</li>"
                "<li>Trigliceridi e HDL</li>"
                "<li>(se rilevante) marcatori del diabete e storia della pressione</li>"
                "<li>contesto infiammatorio (ad es. CRP) a seconda dell’approccio</li>"
                "</ul>"
                "<p>Questa visione combinata aiuta a inserirla in un quadro più ampio di lipidi e rischio cardiovascolare.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normale vs elevata: guida rapida",
            body_html=(
                "<div class=\"blog-example\"><strong>Nel range:</strong> significa spesso che il valore di ApoB è vicino a quanto atteso per molti contesti di rischio.</div>"
                "<div class=\"blog-example\"><strong>Elevazione moderata:</strong> porta spesso a rivedere il resto del profilo lipidico e valutare un follow-up.</div>"
                "<div class=\"blog-example\"><strong>Elevazione chiara:</strong> può richiedere una discussione più focalizzata sul rischio e decisioni su eventuali ripetizioni.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Prossimi passi (con il medico)",
            body_html=(
                "<p>Per capire come ApoB si collega al tuo referto, rivedila insieme al resto del profilo lipidico. "
                "Se vuoi un riepilogo strutturato, puoi <a href=\"/it/upload\">caricare i risultati</a>. "
                "Inizia con <a href=\"/it/blood-test-results-explained\">blood test results explained</a> per una rapida panoramica, "
                "e poi usa l’<a href=\"/it/ai-blood-test-analyzer\">AI blood test analyzer</a> per rivedere l’interpretazione con il tuo medico.</p>"
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


def _sections_he():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="תשובה מהירה: מה משקפת ApoB",
            body_html=(
                "<p><strong>ApoB</strong> היא <strong>אפו־B (Apolipoprotein B)</strong>. "
                "זה חלבון שמופיע על פני חלקיקים שונים בדם שיכולים להיות קשורים להתפתחות טרשת עורקים. "
                "במילים פשוטות, ApoB עשויה לשקף את <strong>מספר החלקיקים הטרשתיים</strong> שנמצאים במחזור הדם.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="מה יכול להעיד ערך גבוה של ApoB (הקשר לימודי)",
            body_html=(
                "<p>כאשר קלינאים רואים ApoB גבוה מהצפוי, הם עשויים לפרש זאת כאיתות שיש יותר חלקיקים הנושאים כולסטרול. "
                "עם זאת, המשמעות תלויה בפרופיל השומנים המלא ובגורמי הסיכון הקרדיווסקולריים שלך.</p>"
                "<p>תוצאות מעבדה מושפעות גם מהקשר. לכן ערך בודד לרוב לא מסביר הכול—הרופא/ה מחליטים האם לבצע בדיקה חוזרת "
                "או סקירה רחבה יותר של הסיכון.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB לעומת LDL: מה ההבדל?",
            body_html=(
                "<p><strong>LDL</strong> מתאר את כמות הכולסטרול בתוך חלקיקי LDL. "
                "<strong>ApoB</strong> מתאר את מספר יחידות החלקיקים הנושאות ApoB. "
                "במצבים שונים ייתכן שימוש באחד או בשניהם כדי להבין דפוסי סיכון.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="איך מקשרים את ApoB עם בדיקות נוספות",
            body_html=(
                "<p>בפועל, ApoB נבדקת לעתים קרובות יחד עם:</p>"
                "<ul>"
                "<li>יעדי LDL ו־Non-HDL</li>"
                "<li>טריגליצרידים ו־HDL</li>"
                "<li>(אם רלוונטי) סמנים לסוכרת והיסטוריית לחץ דם</li>"
                "<li>הקשר דלקתי (למשל CRP) לפי גישת הקלינאי</li>"
                "</ul>"
                "<p>הסתכלות משולבת עוזרת לשים את ApoB בתוך תמונה רחבה יותר של שומנים וסיכון לבבי.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="נורמה לעומת גבוה: מדריך קצר",
            body_html=(
                "<div class=\"blog-example\"><strong>בטווח:</strong> לרוב אומר שהערך קרוב למה שמצפים לראות בהקשרים רבים של סיכון.</div>"
                "<div class=\"blog-example\"><strong>גבוה במידה מתונה:</strong> לעתים מוביל לבדיקה של שאר פרופיל השומנים ולשיקול המשך.</div>"
                "<div class=\"blog-example\"><strong>גבוה באופן ברור:</strong> עשוי לגרום לשיחה ממוקדת יותר על סיכון קרדיווסקולרי ולקבל החלטות לגבי בדיקה חוזרת.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="מה עושים הלאה (עם קלינאי)",
            body_html=(
                "<p>כדי להבין איפה ApoB משתלבת בדוח שלך, כדאי להסתכל עליה יחד עם שאר תוצאות השומנים. "
                "אם תרצה/י סיכום מובנה, אפשר <a href=\"/he/upload\">להעלות את תוצאות בדיקות הדם</a> ולהיעזר בהסבר יחד עם הרופא/ה. "
                "אפשר להתחיל עם <a href=\"/he/blood-test-results-explained\">blood test results explained</a> ואחר כך עם <a href=\"/he/ai-blood-test-analyzer\">AI blood test analyzer</a>.</p>"
                "<p>המדריך הזה הוא למטרות לימוד בלבד ואינו מחליף הערכה רפואית.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="הבהרה",
            body_html=(
                "<p><strong>המידע כאן הוא לצורכי מידע בלבד.</strong> הוא אינו ייעוץ רפואי, אבחון או טיפול. "
                "יש לדון תמיד בתוצאות עם איש מקצוע מוסמך.</p>"
            ),
        ),
    ]


def _sections_hi():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="क्विक उत्तर: ApoB क्या दिखाता है",
            body_html=(
                "<p><strong>ApoB</strong> का मतलब <strong>एपोलीपोप्रोटीन B (Apolipoprotein B)</strong> है। "
                "यह एक ऐसा प्रोटीन है जो खून में मौजूद कुछ कणों की सतह पर पाया जाता है, जो एथेरोस्क्लेरोसिस से जुड़े हो सकते हैं। "
                "सरल शब्दों में, ApoB <strong>atherogenic कणों की संख्या</strong> का संकेत दे सकता है।</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="ApoB बढ़ा हुआ हो तो क्या मतलब हो सकता है (शैक्षिक संदर्भ)",
            body_html=(
                "<p>जब ApoB अपेक्षा से अधिक दिखता है, डॉक्टर इसे यह संकेत मान सकते हैं कि कोलेस्ट्रॉल ले जाने वाले कण अधिक मौजूद हैं। "
                "लेकिन इसका निष्कर्ष आपके पूरे लिपिड प्रोफाइल और आपके कुल कार्डियोवैस्कुलर जोखिम कारकों पर निर्भर करता है।</p>"
                "<p>लैब परिणाम संदर्भ से प्रभावित हो सकते हैं, इसलिए एक ही वैल्यू पूरी कहानी नहीं होती। "
                "डॉक्टर तय करते हैं कि दोबारा टेस्ट या व्यापक जोखिम समीक्षा उपयोगी होगी या नहीं।</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB बनाम LDL: फर्क क्या है?",
            body_html=(
                "<p><strong>LDL कोलेस्ट्रॉल</strong> LDL कणों में मौजूद कोलेस्ट्रॉल की मात्रा बताता है। "
                "<strong>ApoB</strong> ApoB वाले कणों की इकाइयों/संख्या को दर्शाता है। "
                "कई स्थितियों में डॉक्टर एक या दोनों का उपयोग करके जोखिम का पैटर्न समझते हैं।</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="डॉक्टर अक्सर ApoB को किन टेस्टों के साथ देखते हैं",
            body_html=(
                "<p>प्रैक्टिस में ApoB अक्सर साथ में देखी जाती है:</p>"
                "<ul>"
                "<li>LDL और non-HDL से जुड़े लक्ष्य/वैल्यू</li>"
                "<li>ट्राइग्लिसराइड्स और HDL</li>"
                "<li>(जरूरत हो तो) डायबिटीज से जुड़े टेस्ट और BP हिस्ट्री</li>"
                "<li>इन्फ्लेमेशन संदर्भ (जैसे CRP) डॉक्टर की रणनीति के अनुसार</li>"
                "</ul>"
                "<p>यह संयुक्त दृष्टिकोण ApoB को एक व्यापक लिपिड और कार्डियोवैस्कुलर तस्वीर में रखता है।</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="नॉर्मल बनाम ऊंचा: त्वरित गाइड",
            body_html=(
                "<div class=\"blog-example\"><strong>रेंज में:</strong> आमतौर पर इसका मतलब है कि ApoB वैल्यू कई जोखिम संदर्भों में अपेक्षित के करीब है।</div>"
                "<div class=\"blog-example\"><strong>मध्यम बढ़ोतरी:</strong> अक्सर बाकी लिपिड प्रोफाइल की समीक्षा और फॉलो-अप पर विचार की ओर ले जाती है।</div>"
                "<div class=\"blog-example\"><strong>स्पष्ट बढ़ोतरी:</strong> अधिक फोकस्ड जोखिम चर्चा और दोबारा टेस्ट के फैसले की ओर ले जा सकती है।</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="आगे क्या करें (क्लिनिशियन के साथ)",
            body_html=(
                "<p>अगर आपको समझना है कि ApoB आपके रिपोर्ट में कैसे फिट होता है, तो उसे अपने पूरे लिपिड प्रोफाइल के साथ देखें। "
                "अगर आप एक संरचित सार चाहते हैं, तो <a href=\"/hi/upload\">अपनी ब्लड टेस्ट रिपोर्ट अपलोड</a> कर सकते हैं. "
                "पहले <a href=\"/hi/blood-test-results-explained\">blood test results explained</a> से त्वरित overview लें, "
                "फिर <a href=\"/hi/ai-blood-test-analyzer\">AI blood test analyzer</a> के साथ डॉक्टर के साथ explanation दोबारा देखें.</p>"
                "<p>यह गाइड केवल शैक्षिक है और मेडिकल मूल्यांकन का विकल्प नहीं है।</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="डिस्क्लेमर",
            body_html=(
                "<p><strong>यह सामग्री केवल जानकारी के लिए है।</strong> यह मेडिकल सलाह, डायग्नोसिस या इलाज प्रदान नहीं करती। "
                "अपनी रिपोर्ट हमेशा योग्य क्लिनिशियन से चर्चा करें।</p>"
            ),
        ),
    ]


def _sections_ar():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="إجابة سريعة: ما الذي تمثّله ApoB؟",
            body_html=(
                "<p><strong>ApoB</strong> تعني <strong>أبوليبوبروتين B</strong>. "
                "هي بروتين يوجد على سطح بعض الجسيمات في الدم والتي قد ترتبط بتطور تصلب الشرايين. "
                "بعبارات مبسطة، يمكن أن تعكس ApoB <strong>عدد الجسيمات القابلة للتسبب في تصلب الشرايين</strong> المتحركة في الدم.</p>"
            ),
        ),
        Section(
            id="what-high-apob-means",
            level=2,
            heading="ماذا قد يعني ارتفاع ApoB؟ (سياق تعليمي)",
            body_html=(
                "<p>عندما يلاحظ الأطباء أن ApoB أعلى من المتوقع، فقد يعتبرونه إشارة إلى وجود جسيمات أكثر تنقل الكوليسترول. "
                "لكن التفسير يعتمد على ملف الدهون الكامل وعوامل الخطورة القلبية الوعائية لديك.</p>"
                "<p>قد تتأثر نتائج المختبر بالسياق، لذلك غالباً لا تكفي قيمة واحدة وحدها. "
                "قرار تكرار التحليل أو إجراء تقييم أوسع للمخاطر يكون لدى الطبيب.</p>"
            ),
        ),
        Section(
            id="apob-vs-ldl",
            level=2,
            heading="ApoB مقابل LDL: ما الفرق؟",
            body_html=(
                "<p><strong>LDL</strong> يصف كمية الكوليسترول داخل جسيمات LDL. "
                "<strong>ApoB</strong> يصف عدد وحدات الجسيمات التي تحمل ApoB. "
                "وفي حالات مختلفة، قد يستخدم الأطباء واحداً أو كليهما لفهم نمط الخطورة.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-apob",
            level=2,
            heading="كيف يربط الأطباء ApoB بالتحاليل الأخرى؟",
            body_html=(
                "<p>غالباً ما تتم مراجعة ApoB مع:</p>"
                "<ul>"
                "<li>LDL و/أو أهداف non-HDL</li>"
                "<li>الدهون الثلاثية (Triglycerides) وHDL</li>"
                "<li>(إن لزم) مؤشرات السكري وتاريخ ضغط الدم</li>"
                "<li>سياق الالتهاب (مثل CRP) حسب نهج الطبيب</li>"
                "</ul>"
                "<p>هذه النظرة المجمعة تساعد على وضع ApoB ضمن صورة أوسع للدهون والخطر القلبي الوعائي.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="طبيعي أم مرتفع: إرشاد سريع",
            body_html=(
                "<div class=\"blog-example\"><strong>ضمن النطاق:</strong> غالباً يعني أن قيمة ApoB قريبة مما يتوقعه المختبر في سياقات خطورة متعددة.</div>"
                "<div class=\"blog-example\"><strong>ارتفاع متوسط:</strong> قد يؤدي إلى مراجعة بقية ملف الدهون والتفكير بمتابعة.</div>"
                "<div class=\"blog-example\"><strong>ارتفاع واضح:</strong> قد يدفع إلى نقاش أكثر تركيزاً حول الخطورة وخيارات تكرار التحليل.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="ما الخطوة التالية؟ (مع الطبيب)",
            body_html=(
                "<p>لفهم مكان ApoB في تقريرك، راجعها مع بقية نتائج ملف الدهون. "
                "إذا كنت تريد ملخصاً منظماً، يمكنك <a href=\"/ar/upload\">رفع نتائج تحاليل الدم</a>. "
                "ابدأ بـ <a href=\"/ar/blood-test-results-explained\">blood test results explained</a> للحصول على نظرة سريعة، "
                "ثم استخدم <a href=\"/ar/ai-blood-test-analyzer\">AI blood test analyzer</a> لمراجعة التفسير مع طبيبك.</p>"
                "<p>هذا الدليل تعليمي فقط ولا يغني عن التقييم الطبي.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="تنبيه",
            body_html=(
                "<p><strong>هذا المحتوى معلوماتي فقط.</strong> لا يقدم نصيحة طبية ولا تشخيصاً ولا علاجاً. "
                "ناقش نتائجك دائماً مع مختص مؤهل.</p>"
            ),
        ),
    ]


def build_apob_article():
    from app.blog_i18n import Article, Section

    published = date(2026, 3, 26)
    # ApoB is closely related to LDL particle information; use the existing LDL/HDL hero.
    cover = "/static/images/blog/ldl-hdl-hero.png"

    cat = {
        "en": "Lipids",
        "tr": "Kolesterol",
        "de": "Cholesterin",
        "es": "Lípidos",
        "fr": "Lipides",
        "it": "Lipidi",
        "he": "שומנים",
        "hi": "लिपिड्स",
        "ar": "الدهون",
    }

    slugs = {
        "en": "apob-meaning",
        "tr": "apob-anlama-gelir",
        "de": "apob-bedeutung",
        "es": "significado-apob",
        "fr": "signification-apob",
        "it": "significato-apob",
        "he": "פירוש-apob",
        "hi": "apob-का-मतलब",
        "ar": "معنى-apob",
    }

    titles = {
        "en": "What does ApoB mean in a blood test?",
        "tr": "Kan tahlilinde ApoB ne anlama gelir?",
        "de": "Was bedeutet ApoB im Bluttest?",
        "es": "¿Qué significa la ApoB en un análisis de sangre?",
        "fr": "Que signifie l’ApoB dans une prise de sang ?",
        "it": "Cosa significa ApoB in un esame del sangue?",
        "he": "מה המשמעות של ApoB בבדיקת דם?",
        "hi": "ब्लड टेस्ट में ApoB का मतलब क्या है?",
        "ar": "ما معنى ApoB في تحليل الدم؟",
    }

    subtitles = {
        "en": "A plain-language guide to ApoB and how clinicians place it in your lipid picture.",
        "tr": "ApoB’ye sade bir bakış ve doktorların lipid profilinizde nasıl yorumladığı.",
        "de": "Eine verständliche Erklärung zu ApoB und wie Ärztinnen/Ärzte es in Ihr Lipidbild einordnen.",
        "es": "Guía en lenguaje sencillo sobre la ApoB y cómo los profesionales la interpretan en tu perfil lipídico.",
        "fr": "Guide simple sur l’ApoB et la façon dont les cliniciens l’intègrent à votre profil lipidique.",
        "it": "Guida semplice su ApoB e su come viene interpretata nel tuo profilo lipidico.",
        "he": "מדריך פשוט על ApoB ואיך רופאים משבצים אותו בתמונה השומנית שלך.",
        "hi": "ApoB के बारे में सरल गाइड और डॉक्टर इसे आपके लिपिड प्रोफाइल में कैसे रखते हैं।",
        "ar": "دليل مبسط حول ApoB وكيف يضعه الأطباء ضمن صورة الدهون لديك.",
    }

    excerpts = {
        "en": "Learn what ApoB represents, how it relates to LDL, and what clinicians typically consider next.",
        "tr": "ApoB’nin neyi gösterdiğini, LDL ile ilişkisini ve doktorların genelde sıradaki adım olarak neye baktığını öğrenin.",
        "de": "Was ApoB bedeutet, wie es zu LDL passt und welche nächsten Schritte Ärztinnen/Ärzte meist erwägen.",
        "es": "Qué representa la ApoB, cómo se relaciona con el LDL y qué suelen considerar como siguiente paso.",
        "fr": "Ce que représente l’ApoB, sa relation avec le LDL et ce que les cliniciens envisagent ensuite.",
        "it": "Cosa rappresenta ApoB, il rapporto con LDL e cosa viene spesso considerato come passo successivo.",
        "he": "מה ApoB משקפת, איך היא קשורה ל־LDL ומה לרוב שוקלים בהמשך.",
        "hi": "ApoB क्या बताती है, LDL से उसका संबंध, और आगे डॉक्टर क्या देखते हैं।",
        "ar": "ما الذي تعنيه ApoB، وكيف ترتبط بـ LDL، وما الذي يفكر به الأطباء عادةً بعد ذلك.",
    }

    seo_titles = {
        "en": "ApoB in a Blood Test: Meaning & Interpretation",
        "tr": "ApoB Kan Tahlili: Ne Anlama Gelir? (Yorum Rehberi)",
        "de": "ApoB im Bluttest: Bedeutung & Einordnung",
        "es": "ApoB en el análisis de sangre: significado y guía",
        "fr": "ApoB dans la prise de sang : signification et repères",
        "it": "ApoB nell’esame del sangue: significato e guida",
        "he": "ApoB בבדיקת דם: משמעות והסבר",
        "hi": "ब्लड टेस्ट में ApoB: मतलब और समझ",
        "ar": "ApoB في تحليل الدم: المعنى وإرشادات",
    }

    seo_descriptions = {
        "en": "Understand what ApoB means, how it relates to LDL, and how clinicians often interpret it within your overall lipid picture. Educational only.",
        "tr": "ApoB’nin ne anlama geldiğini, LDL ile ilişkisini ve doktorların lipid tablosunda nasıl yorumladığını öğrenin. Yalnızca bilgilendirme.",
        "de": "Verstehen Sie, was ApoB bedeutet, wie es zu LDL passt und wie Ärztinnen/Ärzte es in Ihr Lipidbild einordnen. Nur zu Informationszwecken.",
        "es": "Aprende qué significa la ApoB, cómo se relaciona con el LDL y cómo suelen interpretarla según tu perfil lipídico. Solo informativo.",
        "fr": "Découvrez ce que signifie l’ApoB, sa relation avec le LDL et comment les cliniciens l’intègrent à votre profil lipidique. À titre informatif.",
        "it": "Scopri cosa significa ApoB, il rapporto con LDL e come spesso viene interpretata nel tuo profilo lipidico. Solo informativo.",
        "he": "הבינו מה המשמעות של ApoB, איך היא קשורה ל־LDL ואיך קלינאים משייכים אותה לתמונה השומנית שלך. מידע בלבד.",
        "hi": "जानें ApoB का मतलब क्या है, इसका LDL से क्या संबंध है और डॉक्टर इसे आपके लिपिड प्रोफाइल में कैसे समझते हैं। केवल जानकारी।",
        "ar": "تعرّف على معنى ApoB، وكيف يرتبط بـ LDL، وكيف يفسّره الأطباء ضمن صورة الدهون لديك. معلومات فقط.",
    }

    cover_alt = {
        "en": "ApoB guide for blood test interpretation",
        "tr": "ApoB: kan tahlili yorumlama rehberi",
        "de": "ApoB-Leitfaden für die Interpretation von Blutwerten",
        "es": "Guía de ApoB para interpretar un análisis de sangre",
        "fr": "Guide ApoB pour interpréter une prise de sang",
        "it": "Guida ApoB per interpretare l’esame del sangue",
        "he": "מדריך ApoB לפירוש בדיקות דם",
        "hi": "ApoB गाइड: ब्लड टेस्ट समझें",
        "ar": "دليل ApoB لتفسير تحليل الدم",
    }

    return Article(
        id="apob-meaning",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang={
            "en": _sections_en(),
            "tr": _sections_tr(),
            "de": _sections_de(),
            "es": _sections_es(),
            "fr": _sections_fr(),
            "it": _sections_it(),
            "he": _sections_he(),
            "hi": _sections_hi(),
            "ar": _sections_ar(),
        },
        faq_schema_qa={
            "en": [
                {
                    "question": "What is ApoB?",
                    "answer": "ApoB is an apolipoprotein found on several cholesterol-carrying particles. It can be used as a marker to reflect the number of atherogenic particles in the bloodstream."
                },
                {
                    "question": "Is ApoB the same as LDL cholesterol?",
                    "answer": "Not exactly. LDL cholesterol describes the cholesterol content in LDL particles, while ApoB reflects particle units carrying ApoB. Clinicians may use one or both depending on your context."
                },
                {
                    "question": "Does a high ApoB always mean heart disease?",
                    "answer": "No. A higher value can be one signal within a broader picture. Your clinician will interpret it together with your overall risk factors and other test results."
                },
                {
                    "question": "Do I need fasting for an ApoB test?",
                    "answer": "Lab instructions vary. In practice, many clinicians follow the lab’s instructions, and if ApoB is part of a broader lipid panel, fasting may be recommended depending on triglycerides."
                },
            ],
            "tr": [
                {
                    "question": "ApoB nedir?",
                    "answer": "ApoB, kolesterol taşıyan bazı kan partiküllerinin üzerinde bulunan bir apolipoproteindir. Aterojenik partikül sayısını yansıtmak için biyobelirteç olarak kullanılabilir."
                },
                {
                    "question": "ApoB ile LDL kolesterol aynı şey mi?",
                    "answer": "Tam olarak aynı değildir. LDL kolesterol, LDL partiküllerindeki kolesterol miktarını anlatırken ApoB, ApoB taşıyan partikül birimlerini temsil eder. Doktorlar bağlama göre birini ya da ikisini birlikte kullanabilir."
                },
                {
                    "question": "Yüksek ApoB her zaman kalp hastalığı demek mi?",
                    "answer": "Hayır. Yüksek değer tek başına tanı koymaz; daha geniş bir risk tablosu içinde yorumlanır. Doktorunuz diğer testleriniz ve risk faktörlerinizle birlikte değerlendirir."
                },
                {
                    "question": "ApoB testi için aç olmak gerekir mi?",
                    "answer": "Laboratuvar talimatları değişebilir. Uygulamada doktorlar genelde laboratuvarın verdiği yönergeleri takip eder; ApoB aynı anda lipid panelinin parçasıysa trigliseridlere göre açlık gerekebilir."
                },
            ],
            "de": [
                {
                    "question": "Was ist ApoB?",
                    "answer": "ApoB ist ein Apolipoprotein auf mehreren cholesterintransportierenden Partikeln. Es kann helfen, die Anzahl atherogener Partikel im Blut zu beschreiben."
                },
                {
                    "question": "Ist ApoB dasselbe wie LDL-Cholesterin?",
                    "answer": "Nicht genau. LDL-Cholesterin beschreibt den Cholesteringehalt in LDL-Partikeln, während ApoB die Partikel-Einheiten widerspiegelt, die ApoB tragen. Ärztinnen/Ärzte nutzen je nach Situation ein oder beide Marker."
                },
                {
                    "question": "Bedeutet ein hoher ApoB-Wert immer eine Herzerkrankung?",
                    "answer": "Nein. Ein höherer Wert kann ein Hinweis im Gesamtkontext sein. Ihre Ärztin/Ihr Arzt interpretiert ihn gemeinsam mit den Risikofaktoren und anderen Laborwerten."
                },
                {
                    "question": "Muss man für einen ApoB-Test fasten?",
                    "answer": "Die Laboranweisungen können variieren. In der Praxis orientiert man sich an den Angaben des Labors; falls ApoB Teil eines größeren Lipidprofils ist, kann Fasten je nach Triglyceriden empfohlen werden."
                },
            ],
            "es": [
                {
                    "question": "¿Qué es la ApoB?",
                    "answer": "ApoB es una apolipoproteína presente en varias partículas que transportan colesterol. Puede utilizarse para reflejar el número de partículas aterogénicas en la sangre."
                },
                {
                    "question": "¿ApoB es lo mismo que el LDL colesterol?",
                    "answer": "No exactamente. El LDL describe el contenido de colesterol en las partículas LDL, mientras que ApoB refleja unidades de partículas que transportan ApoB. El profesional puede usar uno o ambos según tu contexto."
                },
                {
                    "question": "¿Una ApoB alta significa siempre enfermedad cardíaca?",
                    "answer": "No. Un valor más alto es una señal dentro de un panorama más amplio. Se interpreta junto con tus factores de riesgo y otros resultados."
                },
                {
                    "question": "¿Necesito ayunar para una prueba de ApoB?",
                    "answer": "Las instrucciones del laboratorio pueden variar. Si ApoB forma parte de un panel lipídico, el ayuno puede recomendarse según los triglicéridos y las indicaciones del laboratorio."
                },
            ],
            "fr": [
                {
                    "question": "Qu’est-ce que l’ApoB ?",
                    "answer": "L’ApoB est une apolipoprotéine présente sur plusieurs particules qui transportent le cholestérol. Elle peut servir de marqueur pour refléter le nombre de particules athérogènes dans le sang."
                },
                {
                    "question": "L’ApoB est-elle la même chose que le LDL ?",
                    "answer": "Pas exactement. Le LDL décrit la quantité de cholestérol dans les particules LDL, tandis que l’ApoB reflète les unités de particules portant l’ApoB. Les cliniciens peuvent utiliser l’un ou les deux selon le contexte."
                },
                {
                    "question": "Un ApoB élevé signifie-t-il toujours une maladie cardiaque ?",
                    "answer": "Non. Un ApoB plus élevé est un signal à interpréter dans l’ensemble. Votre clinicien le met en perspective avec vos facteurs de risque et vos autres analyses."
                },
                {
                    "question": "Faut-il être à jeun pour un test ApoB ?",
                    "answer": "Les consignes du laboratoire varient. En pratique, on suit les instructions du laboratoire; si ApoB fait partie d’un bilan lipidique, le jeûne peut être recommandé selon les triglycérides."
                },
            ],
            "it": [
                {
                    "question": "Che cos’è ApoB?",
                    "answer": "ApoB è un’apolipoproteina presente su diverse particelle che trasportano il colesterolo. Può essere usata per riflettere il numero di particelle aterogene nel sangue."
                },
                {
                    "question": "ApoB è uguale al colesterolo LDL?",
                    "answer": "Non esattamente. Il LDL descrive la quantità di colesterolo nelle particelle LDL, mentre ApoB riflette le unità di particelle che trasportano ApoB. Il medico può usare uno o entrambi in base al contesto."
                },
                {
                    "question": "Un ApoB alto significa sempre una malattia cardiaca?",
                    "answer": "No. Un valore più alto è un segnale dentro un quadro più ampio. L’interpretazione dipende dai fattori di rischio e da altri esami."
                },
                {
                    "question": "Serve il digiuno per un test ApoB?",
                    "answer": "Le indicazioni possono variare. In genere si seguono le istruzioni del laboratorio; se ApoB fa parte di un pannello lipidico, il digiuno può essere consigliato in base ai trigliceridi."
                },
            ],
            "he": [
                {
                    "question": "מה זה ApoB?",
                    "answer": "ApoB הוא אפוליפופרוטאין שמופיע על כמה חלקיקים הנושאים כולסטרול. הוא יכול לשמש כסמן שמייצג את מספר החלקיקים הטרשתיים בדם."
                },
                {
                    "question": "האם ApoB זהה ל־LDL?",
                    "answer": "לא בדיוק. LDL מתאר את כמות הכולסטרול בתוך חלקיקי LDL, בעוד ש־ApoB משקף יחידות של חלקיקים הנושאות ApoB. קלינאים יכולים להשתמש באחד או בשניהם לפי ההקשר."
                },
                {
                    "question": "האם ApoB גבוה תמיד אומר מחלת לב?",
                    "answer": "לא. ערך גבוה הוא אות בתוך תמונה רחבה יותר. הרופא/ה מפרשים זאת יחד עם גורמי הסיכון ותוצאות נוספות."
                },
                {
                    "question": "צריך צום כדי לבצע בדיקת ApoB?",
                    "answer": "ההנחיות של המעבדה עשויות להשתנות. בפועל פועלים לפי הוראות המעבדה; אם ApoB חלק מבדיקת שומנים רחבה, ייתכן שימליצו על צום בהתאם לטריגליצרידים."
                },
            ],
            "hi": [
                {
                    "question": "ApoB क्या है?",
                    "answer": "ApoB एक apolipoprotein है जो कई ऐसे कणों पर पाया जाता है जो कोलेस्ट्रॉल ले जाते हैं। इसे रक्त में atherogenic कणों की संख्या/संकेत देने वाले मार्कर की तरह उपयोग किया जा सकता है।"
                },
                {
                    "question": "क्या ApoB, LDL कोलेस्ट्रॉल जैसा ही है?",
                    "answer": "नहीं। LDL कोलेस्ट्रॉल LDL कणों में मौजूद कोलेस्ट्रॉल की मात्रा बताता है, जबकि ApoB ApoB ले जाने वाले particle units को दर्शाता है। डॉक्टर स्थिति के अनुसार एक या दोनों का उपयोग कर सकते हैं।"
                },
                {
                    "question": "क्या ApoB बढ़ा हुआ हमेशा हृदय रोग ही दर्शाता है?",
                    "answer": "नहीं। यह वैल्यू एक संकेत हो सकती है, पर व्याख्या आपके कुल जोखिम और अन्य टेस्ट पर निर्भर करती है।"
                },
                {
                    "question": "ApoB टेस्ट के लिए क्या फास्ट/अवधि ज़रूरी है?",
                    "answer": "लैब की हिदायतें अलग हो सकती हैं। आम तौर पर लैब के निर्देशों का पालन किया जाता है; अगर ApoB लिपिड पैनल का हिस्सा है, तो ट्राइग्लिसराइड्स के आधार पर फास्ट की सलाह हो सकती है।"
                },
            ],
            "ar": [
                {
                    "question": "ما هي ApoB؟",
                    "answer": "ApoB هو أبوليبوبروتين موجود على عدة جسيمات تنقل الكوليسترول. يمكن استخدامه كعلامة تعكس عدد الجسيمات المسببة لتصلب الشرايين في الدم."
                },
                {
                    "question": "هل ApoB هي نفسها LDL؟",
                    "answer": "ليس تماماً. LDL يصف كمية الكوليسترول داخل جسيمات LDL، بينما ApoB يعكس وحدات الجسيمات التي تحمل ApoB. قد يستخدم الأطباء واحداً أو كليهما حسب السياق."
                },
                {
                    "question": "هل ارتفاع ApoB يعني دائماً مرض قلب؟",
                    "answer": "لا. ارتفاعها قد يكون إشارة ضمن صورة أوسع. الطبيب يفسرها مع عوامل الخطورة ونتائج التحاليل الأخرى."
                },
                {
                    "question": "هل يجب الصيام قبل تحليل ApoB؟",
                    "answer": "تعليمات المختبر قد تختلف. عملياً يُتبع إرشاد المختبر؛ إذا كانت ApoB جزءاً من لوحة دهون، فقد يُوصى بالصيام حسب الدهون الثلاثية."
                },
            ],
        },
        icon=None,
        last_updated=published,
    )

