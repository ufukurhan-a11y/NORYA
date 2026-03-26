"""Blog article for Lp(a) intent."""

from __future__ import annotations

from datetime import date


def _sections_en():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Quick answer: what Lp(a) represents",
            body_html=(
                "<p><strong>Lp(a)</strong> stands for <strong>lipoprotein(a)</strong>. "
                "It is a cholesterol-related blood marker that is often influenced by genetics. "
                "In many cases, clinicians use Lp(a) to understand a person’s cardiovascular risk context "
                "beyond standard cholesterol tests.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="What a high Lp(a) may mean (educational context)",
            body_html=(
                "<p>A higher Lp(a) can be one signal in a broader risk picture. "
                "It is generally not something you “tune” with short-term lifestyle changes alone, "
                "so clinicians often interpret it together with your overall profile, family history, "
                "and other lipid-related results.</p>"
                "<p>Because labs and reporting formats vary, a single result should be reviewed with "
                "your clinician, especially if you also have other abnormal cholesterol markers.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) vs LDL cholesterol: how they relate",
            body_html=(
                "<p><strong>LDL cholesterol</strong> describes cholesterol carried in LDL particles. "
                "<strong>Lp(a)</strong> is a different marker related to lipoprotein(a). "
                "Clinicians may look at both because they provide different pieces of the cardiovascular risk story.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="How clinicians often place Lp(a) in context",
            body_html=(
                "<p>In practice, Lp(a) may be reviewed alongside:</p>"
                "<ul>"
                "<li>LDL cholesterol, non-HDL cholesterol, and triglycerides</li>"
                "<li>Family history of early cardiovascular disease (when relevant)</li>"
                "<li>Other risk markers such as inflammation context (for example, CRP) if used in your care plan</li>"
                "<li>Blood pressure and diabetes markers when assessing overall risk</li>"
                "</ul>"
                "<p>This combined view helps clinicians decide what follow-up or discussion makes sense for you.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevated: quick pattern guide",
            body_html=(
                "<div class=\"blog-example\"><strong>In range:</strong> usually means your result is near what the lab expects in many contexts.</div>"
                "<div class=\"blog-example\"><strong>Elevated:</strong> often leads to a clinician discussion of your broader cardiovascular risk profile.</div>"
                "<div class=\"blog-example\"><strong>Unclear range due to lab format:</strong> clinicians may interpret it with context and any units your lab reports.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="What to do next (with your clinician)",
            body_html=(
                "<p>If you are wondering how Lp(a) fits your report, start by reviewing it with your other lipid results. "
                "If you want a structured summary, you can <a href=\"/en/upload\">upload your blood test results</a>. "
                "Use <a href=\"/en/blood-test-results-explained\">blood test results explained</a> for a quick overview, "
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
            heading="Kısa cevap: Lp(a) neyi temsil eder?",
            body_html=(
                "<p><strong>Lp(a)</strong>, <strong>lipoprotein(a)</strong> ifadesinin kısaltmasıdır. "
                "Kolesterolle ilişkili bir kan belirtecidir ve çoğu zaman genetik etkilerden etkilenir. "
                "Bazı durumlarda klinisyenler Lp(a)’yı, standart kolesterol testlerinin ötesinde "
                "kardiyovasküler risk bağlamını anlamak için kullanır.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="Yüksek Lp(a) ne anlama gelebilir? (bilgilendirici bağlam)",
            body_html=(
                "<p>Yüksek Lp(a), daha geniş bir risk tablosunun içinde bir işaret olabilir. "
                "Bu değer genellikle kısa vadeli yaşam tarzı değişiklikleriyle tek başına “düzeltilecek” "
                "bir şey olarak ele alınmaz; bu yüzden klinisyenler çoğu zaman genel profilinizi, aile öykünüzü "
                "ve diğer lipid sonuçlarınızı birlikte değerlendirir.</p>"
                "<p>Laboratuvarlar ve raporlama formatları değişebildiği için tek bir sonuç, "
                "birlikte değerlendirme amacıyla doktorunuzla birlikte incelenmelidir.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) vs LDL kolesterol: nasıl ilişkilidir?",
            body_html=(
                "<p><strong>LDL kolesterol</strong>, LDL partiküllerinde taşınan kolesterolü anlatır. "
                "<strong>Lp(a)</strong> ise lipoprotein(a) ile ilişkili farklı bir belirteçtir. "
                "Klinisyenler her ikisine de bakabilir çünkü farklı risk parçalarını tamamlar.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="Klinisyenler Lp(a)’yı hangi bağlamda yorumlar?",
            body_html=(
                "<p>Uygulamada Lp(a) şu bilgilerle birlikte gözden geçirilebilir:</p>"
                "<ul>"
                "<li>LDL kolesterol, non-HDL kolesterol ve trigliserid</li>"
                "<li>(gerektiğinde) erken kardiyovasküler hastalık aile öyküsü</li>"
                "<li>İnflamasyon bağlamı gibi başka risk belirteçleri (yaklaşımınza göre, ör. CRP)</li>"
                "<li>Genel risk değerlendirmesinde tansiyon ve diyabetle ilgili belirteçler</li>"
                "</ul>"
                "<p>Bu birlikte değerlendirme, sizin için hangi takip veya görüşmenin anlamlı olacağına karar vermeye yardımcı olur.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs yüksek: hızlı desen rehberi",
            body_html=(
                "<div class=\"blog-example\"><strong>Referans aralığında:</strong> genellikle laboratuvarın birçok bağlamda beklediğine yakın bir sonuç anlamına gelir.</div>"
                "<div class=\"blog-example\"><strong>Yüksek:</strong> çoğu zaman daha geniş bir kardiyovasküler risk tartışmasına yol açar.</div>"
                "<div class=\"blog-example\"><strong>Rapor formatı nedeniyle aralık belirsizse:</strong> doktorunuz birimler ve bağlamla birlikte yorumlayabilir.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Sıradaki adımlar (doktorunuzla)",
            body_html=(
                "<p>Lp(a)’nın raporunuzdaki yerine dair bir çerçeve arıyorsanız, onu diğer lipid sonuçlarınızla birlikte inceleyin. "
                "Yapılandırılmış bir özet isterseniz <a href=\"/tr/upload\">kan tahlili sonuçlarınızı yükleyin</a>. "
                "Önce <a href=\"/tr/blood-test-results-explained\">blood test results explained</a> ile hızlı bir genel görünüm edinin, "
                "sonra da <a href=\"/tr/ai-blood-test-analyzer\">AI blood test analyzer</a> ile açıklamayı doktorunuzla birlikte gözden geçirin.</p>"
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
            heading="Kurz erklärt: Was Lp(a) bedeutet",
            body_html=(
                "<p><strong>Lp(a)</strong> steht für <strong>Lipoprotein(a)</strong>. "
                "Es ist ein blutbasierter Marker, der mit Cholesterin zusammenhängt und häufig durch Genetik beeinflusst wird. "
                "Ärztinnen/Ärzte nutzen Lp(a) in vielen Fällen, um den kardiovaskulären Risikokontext "
                "über Standard-Cholesterinwerte hinaus besser einordnen zu können.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="Was ein hoher Lp(a)-Wert bedeuten kann (Lernkontext)",
            body_html=(
                "<p>Ein höheres Lp(a) kann ein Hinweis im Rahmen eines breiteren Risikobildes sein. "
                "Oft ist es nicht allein durch kurzfristige Lebensstilmaßnahmen „zielbar“, "
                "sondern wird zusammen mit Ihrem Gesamtprofil, Ihrer Familienanamnese und anderen Lipidwerten interpretiert.</p>"
                "<p>Da Laborwerte und Bericht-Formate variieren, sollte ein einzelner Wert mit Ihrer Ärztin/Ihrem Arzt "
                "und im Kontext weiterer Befunde besprochen werden.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) vs LDL-Cholesterin: wie hängen sie zusammen?",
            body_html=(
                "<p><strong>LDL-Cholesterin</strong> beschreibt den Cholesteringehalt in LDL-Partikeln. "
                "<strong>Lp(a)</strong> ist ein anderer Marker, der mit Lipoprotein(a) verbunden ist. "
                "Beide können gemeinsam betrachtet werden, weil sie unterschiedliche Teile der Risikogeschichte liefern.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="Wie Ärztinnen/Ärzte Lp(a) meist einordnen",
            body_html=(
                "<p>In der Praxis wird Lp(a) häufig zusammen mit:</p>"
                "<ul>"
                "<li>LDL-Cholesterin, Non-HDL und Triglyceriden</li>"
                "<li>(falls relevant) Familienanamnese für frühe Herz-Kreislauf-Erkrankungen</li>"
                "<li>Weitere Risikomarker wie Entzündungs-Kontext (z. B. CRP), je nach Ansatz</li>"
                "<li>Blutdruck- und Diabetes-Markern zur Gesamtrisikobewertung</li>"
                "</ul>"
                "<p>Dieses Gesamtbild hilft bei der Entscheidung, welche Nachsorge oder Diskussion sinnvoll ist.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs. erhöht: schnelle Orientierung",
            body_html=(
                "<div class=\"blog-example\"><strong>Im Referenzbereich:</strong> bedeutet meist, dass der Wert in vielen Kontexten nahe dem liegt, was das Labor erwartet.</div>"
                "<div class=\"blog-example\"><strong>Erhöht:</strong> führt oft zu einer Diskussion Ihres breiteren kardiovaskulären Risikoprofils.</div>"
                "<div class=\"blog-example\"><strong>Unklare Einordnung durch Laborformat:</strong> Ärztinnen/Ärzte interpretieren mit Einheiten und Kontext.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Was als Nächstes tun (mit Ihrer Ärztin/Arzt)",
            body_html=(
                "<p>Wenn Sie wissen möchten, wo Lp(a) in Ihrem Befund einzuordnen ist, betrachten Sie es mit Ihren anderen Lipidwerten. "
                "Für eine strukturierte Übersicht können Sie <a href=\"/de/upload\">Ihre Bluttest-Ergebnisse hochladen</a>. "
                "Nutzen Sie <a href=\"/de/blood-test-results-explained\">blood test results explained</a> für eine schnelle Orientierung "
                "und anschließend den <a href=\"/de/ai-blood-test-analyzer\">AI blood test analyzer</a> zur Durchsicht der Erklärung mit Ihrer Ärztin/Ihrem Arzt.</p>"
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
            heading="Respuesta rápida: qué representa Lp(a)",
            body_html=(
                "<p><strong>Lp(a)</strong> significa <strong>lipoproteína(a)</strong>. "
                "Es un marcador relacionado con el colesterol y a menudo influido por la genética. "
                "En muchos casos, se usa para entender el contexto del riesgo cardiovascular más allá de "
                "las pruebas de colesterol estándar.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="Qué podría significar un Lp(a) alto (contexto educativo)",
            body_html=(
                "<p>Un Lp(a) más alto puede ser una señal dentro de una imagen de riesgo más amplia. "
                "En general no se “ajusta” solo con cambios de estilo de vida a corto plazo. "
                "Por eso, los profesionales suelen interpretarlo junto con su perfil general, "
                "antecedentes familiares y otros resultados lipídicos.</p>"
                "<p>Como varían los laboratorios y los formatos de reporte, conviene revisar el resultado "
                "con su clínico en conjunto con el resto de la información.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) vs colesterol LDL: relación",
            body_html=(
                "<p><strong>El LDL</strong> describe colesterol en las partículas LDL. "
                "<strong>Lp(a)</strong> es un marcador distinto relacionado con lipoproteína(a). "
                "Se pueden mirar ambos porque aportan piezas diferentes del riesgo cardiovascular.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="Cómo suelen contextualizar Lp(a)",
            body_html=(
                "<p>En práctica, Lp(a) puede revisarse con:</p>"
                "<ul>"
                "<li>LDL, non-HDL y triglicéridos</li>"
                "<li>Antecedentes familiares de enfermedad cardiovascular temprana (si aplica)</li>"
                "<li>Otros marcadores de riesgo según el plan (por ejemplo, inflamación/CRP)</li>"
                "<li>Presión arterial y marcadores de diabetes para evaluar el riesgo global</li>"
                "</ul>"
                "<p>Esta visión combinada ayuda a decidir qué seguimiento o conversación tiene sentido.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs elevado: guía rápida",
            body_html=(
                "<div class=\"blog-example\"><strong>En rango:</strong> suele significar que el resultado está cerca de lo que el laboratorio espera en muchos contextos.</div>"
                "<div class=\"blog-example\"><strong>Elevado:</strong> a menudo lleva a una discusión sobre el perfil de riesgo cardiovascular.</div>"
                "<div class=\"blog-example\"><strong>Formato y unidades:</strong> la interpretación puede depender de cómo reporta su laboratorio.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Qué hacer después (con su clínico)",
            body_html=(
                "<p>Si quiere entender cómo encaja Lp(a) en su informe, revíselo con sus otros resultados lipídicos. "
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
                "<p><strong>Este artículo es solo para fines informativos.</strong> No ofrece consejo médico, "
                "diagnóstico ni tratamiento. Hable siempre sus resultados con un profesional cualificado.</p>"
            ),
        ),
    ]


def _sections_fr():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Réponse rapide : que représente Lp(a)",
            body_html=(
                "<p><strong>Lp(a)</strong> signifie <strong>lipoprotéine(a)</strong>. "
                "C’est un marqueur sanguin lié au cholestérol et influencé par la génétique. "
                "Dans de nombreux cas, on l’utilise pour comprendre le contexte du risque cardiovasculaire "
                "au-delà des tests de cholestérol standards.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="Que peut indiquer un Lp(a) élevé ? (contexte éducatif)",
            body_html=(
                "<p>Un Lp(a) plus élevé peut être un signal dans une image de risque plus large. "
                "En général, on ne peut pas le modifier facilement uniquement avec des changements de style de vie à court terme. "
                "C’est pourquoi il est souvent interprété avec l’ensemble de votre profil, vos antécédents familiaux "
                "et d’autres résultats lipidiques.</p>"
                "<p>Comme les laboratoires et les formats de rapport varient, discutez le résultat avec votre clinicien "
                "en tenant compte des unités et du contexte.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) vs LDL : comprendre la différence",
            body_html=(
                "<p><strong>LDL</strong> décrit la quantité de cholestérol dans les particules LDL. "
                "<strong>Lp(a)</strong> est un marqueur distinct lié à la lipoprotéine(a). "
                "Les deux peuvent être utilisés ensemble car ils apportent des informations complémentaires sur le risque.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="Comment les cliniciens replacent Lp(a) dans le contexte",
            body_html=(
                "<p>En pratique, Lp(a) peut être revu avec :</p>"
                "<ul>"
                "<li>LDL, non-HDL et triglycérides</li>"
                "<li>Antécédents familiaux de maladie cardiovasculaire précoce (si pertinent)</li>"
                "<li>Autres marqueurs selon votre prise en charge (par exemple inflammation/CRP)</li>"
                "<li>Tension artérielle et marqueurs du diabète pour évaluer le risque global</li>"
                "</ul>"
                "<p>Cette vue combinée aide à décider quel suivi ou échange est le plus utile.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normal vs élevé : repères rapides",
            body_html=(
                "<div class=\"blog-example\"><strong>Dans la norme :</strong> le résultat est généralement proche de ce que le laboratoire attend dans de nombreux contextes.</div>"
                "<div class=\"blog-example\"><strong>Élevé :</strong> peut conduire à une discussion sur le profil de risque cardiovasculaire.</div>"
                "<div class=\"blog-example\"><strong>Unités et format :</strong> l’interprétation dépend aussi de la façon dont votre laboratoire reporte la valeur.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Et ensuite (avec votre clinicien)",
            body_html=(
                "<p>Pour comprendre comment Lp(a) s’intègre à votre bilan, regardez-la avec vos autres résultats lipidiques. "
                "Si vous souhaitez un résumé structuré, vous pouvez <a href=\"/fr/upload\">téléverser vos résultats</a>. "
                "Commencez par <a href=\"/fr/blood-test-results-explained\">blood test results explained</a> pour une vue rapide, "
                "puis utilisez le <a href=\"/fr/ai-blood-test-analyzer\">AI blood test analyzer</a> pour relire l’explication avec votre clinicien.</p>"
                "<p>Ce guide est éducatif et ne remplace pas une évaluation médicale.</p>"
            ),
        ),
        Section(
            id="disclaimer",
            level=2,
            heading="Avertissement",
            body_html=(
                "<p><strong>Ce contenu est uniquement informatif.</strong> Il ne constitue pas un avis médical, "
                "un diagnostic ou un traitement. Discutez toujours vos résultats avec un professionnel qualifié.</p>"
            ),
        ),
    ]


def _sections_it():
    from app.blog_i18n import Section

    return [
        Section(
            id="quick-answer",
            level=2,
            heading="Risposta rapida: cosa rappresenta Lp(a)",
            body_html=(
                "<p><strong>Lp(a)</strong> significa <strong>lipoproteina(a)</strong>. "
                "È un marcatore legato al colesterolo e spesso influenzato dalla genetica. "
                "In molti casi viene usato per capire il contesto del rischio cardiovascolare "
                "oltre ai test standard del colesterolo.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="Cosa può significare un Lp(a) alto (contesto educativo)",
            body_html=(
                "<p>Un Lp(a) più alto può essere un segnale dentro un quadro di rischio più ampio. "
                "In genere non è qualcosa che si modifica facilmente solo con cambiamenti di breve periodo dello stile di vita. "
                "Per questo viene spesso interpretato insieme al profilo complessivo, alla storia familiare "
                "e ad altri risultati lipidi.</p>"
                "<p>Poiché laboratori e formati di referto possono variare, è importante rivedere il risultato "
                "con il tuo medico insieme alle unità riportate.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) vs LDL: come si collegano",
            body_html=(
                "<p><strong>LDL</strong> descrive il colesterolo nelle particelle LDL. "
                "<strong>Lp(a)</strong> è un marcatore diverso legato alla lipoproteina(a). "
                "Guardare entrambi può aiutare a completare il racconto del rischio cardiovascolare.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="Come spesso i clinici contestualizzano Lp(a)",
            body_html=(
                "<p>In pratica, Lp(a) può essere valutata insieme a:</p>"
                "<ul>"
                "<li>LDL, non-HDL e trigliceridi</li>"
                "<li>Storia familiare di malattia cardiovascolare precoce (se rilevante)</li>"
                "<li>Altri marcatori di rischio secondo il piano di cura (ad es. infiammazione/CRP)</li>"
                "<li>Pressione arteriosa e marcatori del diabete per la valutazione complessiva</li>"
                "</ul>"
                "<p>Questa visione combinata aiuta a capire quale follow-up o discussione è sensata per te.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="Normale vs elevata: guida rapida",
            body_html=(
                "<div class=\"blog-example\"><strong>Nel range:</strong> di solito indica che il risultato è vicino a ciò che il laboratorio si aspetta in molti contesti.</div>"
                "<div class=\"blog-example\"><strong>Elevata:</strong> spesso porta a una discussione sul profilo di rischio cardiovascolare.</div>"
                "<div class=\"blog-example\"><strong>Formato/unità:</strong> l’interpretazione può dipendere dal modo in cui il laboratorio riporta la misura.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="Prossimi passi (con il medico)",
            body_html=(
                "<p>Per capire come Lp(a) si collega al tuo referto, rivedila con gli altri risultati lipidi. "
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
            heading="תשובה מהירה: מה משקפת Lp(a)",
            body_html=(
                "<p><strong>Lp(a)</strong> מייצגת <strong>ליפופרוטאין(a)</strong>. "
                "זהו סמן בדם שקשור לכולסטרול, ובמקרים רבים הוא מושפע מגנטיקה. "
                "לעיתים משתמשים בו כדי להבין את הקשר של הסיכון הלבבי-כלי הדם "
                "מעבר למה שבדיקות כולסטרול סטנדרטיות מראות.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="מה יכול להעיד ערך גבוה של Lp(a) (הקשר לימודי)",
            body_html=(
                "<p>ערך גבוה יותר של Lp(a) יכול להיות חלק מתמונה רחבה יותר של סיכון. "
                "ברוב המקרים זה לא משהו שמשתנה בקלות רק בעקבות שינוי קצר טווח באורח חיים, "
                "ולכן נוטים לפרש אותו יחד עם הפרופיל הכללי, היסטוריה משפחתית ותוצאות שומנים נוספות.</p>"
                "<p>מאחר שלמעבדות יש פורמטים ויחידות שונות, כדאי לעבור על התוצאה יחד עם הרופא/ה ולהסתכל על ההקשר.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) לעומת LDL: איך זה קשור",
            body_html=(
                "<p><strong>LDL</strong> מתאר את הכולסטרול בתוך חלקיקי LDL. "
                "<strong>Lp(a)</strong> הוא סמן אחר הקשור לליפופרוטאין(a). "
                "שני המדדים יחד יכולים להשלים את התמונה של הסיכון הקרדיווסקולרי.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="איך קלינאים לרוב משייכים את Lp(a) להקשר",
            body_html=(
                "<p>בפועל, Lp(a) עשויה להיבדק יחד עם:</p>"
                "<ul>"
                "<li>LDL, non-HDL וטריגליצרידים</li>"
                "<li>היסטוריה משפחתית של מחלה לבבית מוקדמת (אם רלוונטי)</li>"
                "<li>סמנים נוספים לפי תכנית הטיפול (למשל דלקת/CRP)</li>"
                "<li>לחץ דם ומדדי סוכרת כחלק מהערכת הסיכון הכוללת</li>"
                "</ul>"
                "<p>השילוב הזה עוזר להחליט מה המשך הדיון או המעקב המתאים.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="בטווח מול גבוה: מדריך קצר",
            body_html=(
                "<div class=\"blog-example\"><strong>בטווח:</strong> לרוב זה אומר שהבדיקה קרובה למה שמצפים במגוון הקשרים.</div>"
                "<div class=\"blog-example\"><strong>גבוה:</strong> בדרך כלל מוביל לשיחה על פרופיל הסיכון הקרדיווסקולרי.</div>"
                "<div class=\"blog-example\"><strong>יחידות/פורמט:</strong> ייתכן שהפרשנות תלויה באופן שבו המעבדה מדווחת את הערך.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="מה עושים הלאה (עם קלינאי)",
            body_html=(
                "<p>אם את/ה תוהה איך Lp(a) משתלבת בדוח שלך, התחילו בבדיקתה יחד עם שאר תוצאות השומנים. "
                "לסיכום מובנה אפשר <a href=\"/he/upload\">להעלות את תוצאות בדיקות הדם</a>. "
                "התחל/י עם <a href=\"/he/blood-test-results-explained\">blood test results explained</a> כדי לקבל תמונה מהירה, "
                "ואז השתמש/י ב-<a href=\"/he/ai-blood-test-analyzer\">AI blood test analyzer</a> כדי לעבור על ההסבר יחד עם הרופא/ה.</p>"
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
            heading="क्विक उत्तर: Lp(a) क्या बताती है",
            body_html=(
                "<p><strong>Lp(a)</strong> का मतलब <strong>लिपोप्रोटीन(a)</strong> है। "
                "यह खून में मौजूद एक ऐसा मार्कर है जो कोलेस्ट्रॉल से जुड़ा होता है और कई मामलों में यह जेनेटिक्स से प्रभावित होता है। "
                "डॉक्टर इसे अक्सर स्टैंडर्ड कोलेस्ट्रॉल टेस्ट के अलावा कार्डियोवैस्कुलर जोखिम के संदर्भ को समझने के लिए देखते हैं।</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="उच्च Lp(a) का क्या मतलब हो सकता है (शैक्षिक संदर्भ)",
            body_html=(
                "<p>उच्च Lp(a) एक व्यापक जोखिम तस्वीर का हिस्सा हो सकती है। "
                "अक्सर इसे सिर्फ़ अल्पकालिक लाइफस्टाइल बदलावों से आसानी से “ठीक” किया जा सकने वाली चीज़ नहीं माना जाता, "
                "इसलिए डॉक्टर पूरे लिपिड प्रोफाइल, फैमिली हिस्ट्री और अन्य संबंधित टेस्ट के साथ इसका मूल्यांकन करते हैं।</p>"
                "<p>क्योंकि अलग-अलग लैब के फ़ॉर्मैट और यूनिट अलग हो सकते हैं, "
                "इसलिए एक ही वैल्यू को अपने क्लिनिशियन के साथ संदर्भ में देखें।</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) बनाम LDL: रिश्ता कैसे समझें",
            body_html=(
                "<p><strong>LDL</strong> LDL पार्टिकल्स में मौजूद कोलेस्ट्रॉल को दिखाता है। "
                "<strong>Lp(a)</strong> लिपोप्रोटीन(a) से जुड़ा अलग मार्कर है। "
                "दोनों को साथ देखना अक्सर कार्डियोवैस्कुलर जोखिम की पूरी कहानी बनाने में मदद करता है।</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="डॉक्टर आम तौर पर Lp(a) को किस संदर्भ में रखते हैं",
            body_html=(
                "<p>प्रैक्टिस में Lp(a) कई बार इनके साथ देखी जाती है:</p>"
                "<ul>"
                "<li>LDL, non-HDL और ट्राइग्लिसराइड्स</li>"
                "<li>(अगर लागू हो) जल्दी दिल की बीमारी की फैमिली हिस्ट्री</li>"
                "<li>कुछ केयर प्लान में इस्तेमाल होने वाले अन्य जोखिम संकेत (जैसे इन्फ्लेमेशन/CRP)</li>"
                "<li>समग्र जोखिम के लिए ब्लड प्रेशर और डायबिटीज मार्कर</li>"
                "</ul>"
                "<p>यह संयुक्त दृष्टिकोण आगे कौन-सा फॉलो-अप/चर्चा उपयुक्त है, तय करने में मदद करता है।</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="नॉर्मल बनाम ऊंचा: त्वरित गाइड",
            body_html=(
                "<div class=\"blog-example\"><strong>रेंज में:</strong> आम तौर पर इसका मतलब है कि रिपोर्ट कई संदर्भों में लैब की उम्मीद के आसपास है।</div>"
                "<div class=\"blog-example\"><strong>ऊंचा:</strong> अक्सर कार्डियोवैस्कुलर जोखिम प्रोफाइल पर चर्चा की ओर ले जाता है।</div>"
                "<div class=\"blog-example\"><strong>फ़ॉर्मैट/यूनिट:</strong> व्याख्या लैब के अनुसार बदल सकती है।</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="आगे क्या करें (क्लिनिशियन के साथ)",
            body_html=(
                "<p>यदि आप जानना चाहते हैं कि Lp(a) आपकी रिपोर्ट में कहाँ फिट होती है, तो उसे अन्य लिपिड नतीजों के साथ देखें। "
                "यदि आप संरचित सार चाहते हैं, तो <a href=\"/hi/upload\">अपनी ब्लड टेस्ट रिपोर्ट अपलोड</a> कर सकते हैं। "
                "पहले <a href=\"/hi/blood-test-results-explained\">blood test results explained</a> से त्वरित overview लें, "
                "फिर <a href=\"/hi/ai-blood-test-analyzer\">AI blood test analyzer</a> के साथ डॉक्टर के संदर्भ में समझें।</p>"
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
            heading="إجابة سريعة: ما معنى Lp(a)",
            body_html=(
                "<p><strong>Lp(a)</strong> تعني <strong>ليبوبروتين(a)</strong>. "
                "هو مؤشر مرتبط بالكلسترول في الدم وغالباً يتأثر بعوامل وراثية. "
                "في كثير من الحالات يستخدمه الأطباء لفهم سياق الخطر القلبي الوعائي "
                "بجانب اختبارات الكوليسترول القياسية.</p>"
            ),
        ),
        Section(
            id="what-high-lpa-means",
            level=2,
            heading="ماذا قد يعني ارتفاع Lp(a)؟ (سياق تعليمي)",
            body_html=(
                "<p>قد يشير ارتفاع Lp(a) إلى جزء من صورة مخاطر أوسع. "
                "وغالباً لا يُنظر إليه على أنه شيء يتغير بسهولة عبر تغييرات نمط حياة قصيرة المدى فقط. "
                "لذلك يتم تفسيره عادةً مع ملف الدهون العام لديك، وتاريخ العائلة، "
                "وبقية النتائج ذات الصلة.</p>"
                "<p>وبما أن المختبرات تختلف في طريقة التقرير والوحدات، فمن الأفضل مناقشة النتيجة "
                "مع طبيبك ضمن السياق.</p>"
            ),
        ),
        Section(
            id="lpa-vs-ldl",
            level=2,
            heading="Lp(a) مقابل LDL: كيف يرتبطان",
            body_html=(
                "<p><strong>LDL</strong> يصف الكوليسترول الموجود داخل جسيمات LDL. "
                "<strong>Lp(a)</strong> هو مؤشر مختلف مرتبط بليبوبروتين(a). "
                "قد ينظر الأطباء إلى الاثنين معاً لأنهما يعطيان أجزاء مختلفة من قصة الخطر.</p>"
            ),
        ),
        Section(
            id="how-doctors-compare-lpa",
            level=2,
            heading="كيف يضع الأطباء Lp(a) في السياق",
            body_html=(
                "<p>في الممارسة، قد تتم مراجعة Lp(a) مع:</p>"
                "<ul>"
                "<li>LDL وnon-HDL والدهون الثلاثية</li>"
                "<li>(عند الحاجة) تاريخ عائلي لمرض قلبي مبكر</li>"
                "<li>مؤشرات خطر أخرى بحسب خطة الرعاية (مثل الالتهاب/CRP)</li>"
                "<li>قياس ضغط الدم ومؤشرات السكري لتقييم الخطر الكلي</li>"
                "</ul>"
                "<p>هذا التقييم المجمّع يساعد على تحديد ما إذا كانت مناقشة أو متابعة معينة هي الأنسب.</p>"
            ),
        ),
        Section(
            id="pattern-guide",
            level=2,
            heading="ضمن النطاق أم مرتفع: إرشاد سريع",
            body_html=(
                "<div class=\"blog-example\"><strong>ضمن النطاق:</strong> غالباً تعني أن النتيجة قريبة مما يتوقعه المختبر في سياقات عديدة.</div>"
                "<div class=\"blog-example\"><strong>مرتفع:</strong> غالباً يؤدي إلى نقاش حول ملف الخطر القلبي الوعائي.</div>"
                "<div class=\"blog-example\"><strong>الوحدات/طريقة التقرير:</strong> قد تعتمد التفسيرات على كيفية عرض المختبر للقيمة.</div>"
            ),
        ),
        Section(
            id="next-steps",
            level=2,
            heading="ما الخطوة التالية؟ (مع الطبيب)",
            body_html=(
                "<p>لفهم مكان Lp(a) في تقريرك، راجعها مع بقية نتائج ملف الدهون. "
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


def build_lpa_article():
    from app.blog_i18n import Article, Section

    published = date(2026, 3, 26)
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
        "en": "lpa-meaning",
        "tr": "lpa-anlama-gelir",
        "de": "lpa-bedeutung",
        "es": "significado-lpa",
        "fr": "signification-lpa",
        "it": "significato-lpa",
        "he": "פירוש-lpa",
        "hi": "lpa-का-मतलब",
        "ar": "معنى-lpa",
    }

    titles = {
        "en": "What does Lp(a) mean in a blood test?",
        "tr": "Kan tahlilinde Lp(a) ne anlama gelir?",
        "de": "Was bedeutet Lp(a) im Bluttest?",
        "es": "¿Qué significa Lp(a) en un análisis de sangre?",
        "fr": "Que signifie Lp(a) dans une prise de sang ?",
        "it": "Cosa significa Lp(a) in un esame del sangue?",
        "he": "מה המשמעות של Lp(a) בבדיקת דם?",
        "hi": "ब्लड टेस्ट में Lp(a) का मतलब क्या है?",
        "ar": "ما معنى Lp(a) في تحليل الدم؟",
    }

    subtitles = {
        "en": "A plain-language guide to Lp(a) and how clinicians use it in cardiovascular risk context.",
        "tr": "Lp(a)’ya sade bir bakış ve klinisyenlerin kardiyovasküler risk bağlamında nasıl kullandığı.",
        "de": "Eine verständliche Erklärung zu Lp(a) und wie Ärztinnen/Ärzte es im kardiovaskulären Risikokontext nutzen.",
        "es": "Guía en lenguaje sencillo sobre Lp(a) y cómo los profesionales lo usan en el contexto de riesgo cardiovascular.",
        "fr": "Guide simple sur Lp(a) et sur la façon dont les cliniciens l’utilisent dans le contexte du risque cardiovasculaire.",
        "it": "Guida semplice su Lp(a) e su come viene usato dai clinici nel contesto del rischio cardiovascolare.",
        "he": "מדריך פשוט ל-Lp(a) ואיך קלינאים משתמשים בו בהקשר של סיכון לבבי-כלי דם.",
        "hi": "Lp(a) के बारे में सरल गाइड और डॉक्टर इसे कार्डियोवैस्कुलर जोखिम के संदर्भ में कैसे देखते हैं।",
        "ar": "دليل مبسط حول Lp(a) وكيف يستخدمه الأطباء ضمن سياق الخطر القلبي الوعائي.",
    }

    excerpts = {
        "en": "Learn what Lp(a) represents and how it is often discussed alongside other lipid and risk markers.",
        "tr": "Lp(a)’nın neyi temsil ettiğini ve çoğu zaman diğer lipid ve risk belirteçleriyle birlikte nasıl konuşulduğunu öğrenin.",
        "de": "Erfahren Sie, was Lp(a) bedeutet und wie es oft zusammen mit anderen Lipid- und Risikomarkern eingeordnet wird.",
        "es": "Aprende qué representa Lp(a) y cómo suele comentarse junto con otros marcadores lipídicos y de riesgo.",
        "fr": "Découvrez ce que représente Lp(a) et comment il est souvent mis en discussion avec d’autres marqueurs lipidiques et de risque.",
        "it": "Scopri cosa rappresenta Lp(a) e come spesso viene discusso insieme ad altri marcatori lipidici e di rischio.",
        "he": "למדו מה משקפת Lp(a) ואיך נוהגים לשלב אותה בשיחה עם סמני שומנים וסיכון נוספים.",
        "hi": "Lp(a) क्या बताती है और इसे अक्सर अन्य लिपिड व रिस्क मार्करों के साथ कैसे देखा/समझा जाता है—जानें।",
        "ar": "تعرّف على ما الذي تمثّله Lp(a) وكيف يتم مناقشتها غالباً مع مؤشرات أخرى للدهون والخطر.",
    }

    seo_titles = {
        "en": "Lp(a) in a Blood Test: Meaning & Interpretation",
        "tr": "Lp(a) Kan Tahlili: Ne Anlama Gelir? (Yorum Rehberi)",
        "de": "Lp(a) im Bluttest: Bedeutung & Einordnung",
        "es": "Lp(a) en el análisis de sangre: significado y guía",
        "fr": "Lp(a) dans une prise de sang : signification et repères",
        "it": "Lp(a) nell’esame del sangue: significato e guida",
        "he": "Lp(a) בבדיקת דם: משמעות והסבר",
        "hi": "ब्लड टेस्ट में Lp(a): मतलब और समझ",
        "ar": "Lp(a) في تحليل الدم: المعنى وإرشادات",
    }

    seo_descriptions = {
        "en": "Understand what Lp(a) represents, why clinicians may interpret it in cardiovascular risk context, and how to review it with your other lipid markers. Educational only.",
        "tr": "Lp(a)’nın neyi temsil ettiğini, klinisyenlerin bunu kardiyovasküler risk bağlamında neden yorumlayabildiğini ve diğer lipid belirteçlerinizle birlikte nasıl ele alacağınızı öğrenin. Yalnızca bilgilendirme.",
        "de": "Verstehen Sie, was Lp(a) bedeutet, warum Ärztinnen/Ärzte es im kardiovaskulären Risikokontext interpretieren können, und wie Sie es mit Ihren anderen Lipidwerten besprechen. Nur zu Informationszwecken.",
        "es": "Aprende qué representa Lp(a), por qué los profesionales lo interpretan en el contexto de riesgo cardiovascular y cómo revisarlo con tus otros marcadores lipídicos. Solo informativo.",
        "fr": "Découvrez ce que représente Lp(a), pourquoi les cliniciens peuvent l’interpréter dans le contexte du risque cardiovasculaire et comment le revoir avec vos autres marqueurs lipidiques. À titre informatif.",
        "it": "Scopri cosa rappresenta Lp(a), perché i clinici lo interpretano nel contesto del rischio cardiovascolare e come rivederlo con gli altri marcatori lipidici. Solo informativo.",
        "he": "הבינו מה משקפת Lp(a), מדוע קלינאים מפרשים זאת בהקשר של סיכון לבבי-כלי דם ואיך לשלב אותה עם שאר סמני השומנים. מידע בלבד.",
        "hi": "Lp(a) क्या बताती है, डॉक्टर इसे कार्डियोवैस्कुलर जोखिम के संदर्भ में क्यों देखते हैं, और इसे आपके दूसरे लिपिड मार्करों के साथ कैसे रिव्यू करें—जानें। केवल शैक्षिक।",
        "ar": "تعرّف على ما الذي تمثّله Lp(a)، ولماذا قد يفسّرها الأطباء ضمن سياق الخطر القلبي الوعائي، وكيف تراجعها مع مؤشرات الدهون الأخرى. معلومات فقط.",
    }

    cover_alt = {
        "en": "Lp(a) guide for blood test interpretation",
        "tr": "Lp(a): kan tahlili yorumlama rehberi",
        "de": "Lp(a)-Leitfaden zur Interpretation von Blutwerten",
        "es": "Guía de Lp(a) para interpretar un análisis de sangre",
        "fr": "Guide Lp(a) pour interpréter une prise de sang",
        "it": "Guida di Lp(a) per interpretare l’esame del sangue",
        "he": "מדריך Lp(a) לפירוש בדיקות דם",
        "hi": "Lp(a) गाइड: ब्लड टेस्ट समझें",
        "ar": "دليل Lp(a) لتفسير تحليل الدم",
    }

    return Article(
        id="lpa-meaning",
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
                {"question": "What is Lp(a)?", "answer": "Lp(a) stands for lipoprotein(a). It is a cholesterol-related blood marker that is often influenced by genetics."},
                {"question": "Is Lp(a) the same as LDL cholesterol?", "answer": "No. LDL cholesterol reflects the cholesterol content in LDL particles, while Lp(a) is a different marker related to lipoprotein(a)."},
                {"question": "Does a high Lp(a) always mean heart disease?", "answer": "Not necessarily. It can be a signal within a broader risk picture. Clinicians interpret it together with your overall lipid and risk factors."},
                {"question": "Do I need fasting for an Lp(a) test?", "answer": "Lab instructions vary. Many clinicians follow the lab’s instructions; discuss with your clinician if you are unsure."},
            ],
            "tr": [
                {"question": "Lp(a) nedir?", "answer": "Lp(a), lipoprotein(a) ifadesinin kısaltmasıdır. Kolesterolle ilişkili bir kan belirtecidir ve çoğu zaman genetikten etkilenir."},
                {"question": "Lp(a) LDL kolesterol ile aynı şey mi?", "answer": "Hayır. LDL kolesterol, LDL partiküllerindeki kolesterol içeriğini anlatırken Lp(a) farklı bir belirteçtir ve lipoprotein(a) ile ilişkilidir."},
                {"question": "Yüksek Lp(a) her zaman kalp hastalığı demek midir?", "answer": "Her zaman değil. Daha geniş bir risk tablosu içinde bir işaret olabilir; klinisyenler bunu lipid sonuçlarınız ve risk faktörlerinizle birlikte yorumlar."},
                {"question": "Lp(a) testi için aç olmak gerekir mi?", "answer": "Laboratuvar talimatları değişebilir. Genelde laboratuvarın verdiği yönergeler izlenir; emin değilseniz doktorunuzla görüşün."},
            ],
            "de": [
                {"question": "Was ist Lp(a)?", "answer": "Lp(a) steht für Lipoprotein(a). Es ist ein cholesterolbezogener Blutmarker, der häufig genetisch beeinflusst ist."},
                {"question": "Ist Lp(a) dasselbe wie LDL-Cholesterin?", "answer": "Nein. LDL-Cholesterin beschreibt den Cholesteringehalt in LDL-Partikeln, während Lp(a) ein anderer Marker ist, der mit Lipoprotein(a) zusammenhängt."},
                {"question": "Bedeutet ein hoher Lp(a)-Wert immer Herzerkrankungen?", "answer": "Nicht unbedingt. Es kann ein Signal innerhalb eines breiteren Risikobildes sein. Ärztinnen/Ärzte interpretieren es zusammen mit Ihren Lipid- und Risikofaktoren."},
                {"question": "Muss man für einen Lp(a)-Test fasten?", "answer": "Die Laborempfehlungen variieren. Viele orientieren sich an den Angaben des Labors; bei Unsicherheit mit Ihrer Ärztin/Ihrem Arzt sprechen."},
            ],
            "es": [
                {"question": "¿Qué es Lp(a)?", "answer": "Lp(a) significa lipoproteína(a). Es un marcador sanguíneo relacionado con el colesterol y a menudo influido por la genética."},
                {"question": "¿Lp(a) es lo mismo que el LDL colesterol?", "answer": "No. El LDL describe el colesterol en las partículas LDL; Lp(a) es un marcador distinto relacionado con lipoproteína(a)."},
                {"question": "¿Un Lp(a) alto significa siempre enfermedad cardíaca?", "answer": "No necesariamente. Puede ser una señal dentro de un panorama de riesgo más amplio. Los profesionales lo interpretan junto con tus factores lipídicos y de riesgo."},
                {"question": "¿Se necesita ayuno para un test de Lp(a)?", "answer": "Varía según el laboratorio. Muchas veces se siguen las indicaciones del laboratorio; si tienes dudas, coméntalo con tu clínico."},
            ],
            "fr": [
                {"question": "Qu’est-ce que Lp(a) ?", "answer": "Lp(a) signifie lipoprotéine(a). C’est un marqueur sanguin lié au cholestérol, souvent influencé par la génétique."},
                {"question": "Lp(a) est-elle la même chose que le LDL ?", "answer": "Non. Le LDL reflète le cholestérol dans les particules LDL, tandis que Lp(a) est un marqueur différent lié à la lipoprotéine(a)."},
                {"question": "Un Lp(a) élevé signifie-t-il toujours une maladie cardiaque ?", "answer": "Pas nécessairement. C’est un signal dans un contexte de risque plus large, interprété avec vos autres facteurs lipidiques et de risque."},
                {"question": "Faut-il être à jeun pour un test Lp(a) ?", "answer": "Les consignes varient selon le laboratoire. Suivez les indications du laboratoire et demandez conseil à votre clinicien si besoin."},
            ],
            "it": [
                {"question": "Che cos’è Lp(a)?", "answer": "Lp(a) significa lipoproteina(a). È un marcatore collegato al colesterolo e spesso influenzato dalla genetica."},
                {"question": "Lp(a) è la stessa cosa dell’LDL?", "answer": "No. L’LDL descrive il contenuto di colesterolo nelle particelle LDL, mentre Lp(a) è un marcatore diverso collegato alla lipoproteina(a)."},
                {"question": "Un Lp(a) alto significa sempre malattia cardiaca?", "answer": "Non necessariamente. Può essere un segnale nel quadro più ampio del rischio. L’interpretazione dipende da profilo lipidico e altri fattori di rischio."},
                {"question": "Serve il digiuno per un test Lp(a)?", "answer": "Le indicazioni possono variare. Segui le istruzioni del laboratorio e, se hai dubbi, parla con il medico."},
            ],
            "he": [
                {"question": "מה זה Lp(a)?", "answer": "Lp(a) מייצגת lipoprotein(a). זהו סמן בדם שקשור לכולסטרול, ולעיתים קרובות הוא מושפע מגנטיקה."},
                {"question": "האם Lp(a) זהה לכולסטרול LDL?", "answer": "לא. LDL משקף את הכולסטרול בתוך חלקיקי LDL, בעוד ש-Lp(a) הוא סמן אחר הקשור לליפופרוטאין(a)."},
                {"question": "האם Lp(a) גבוה תמיד אומר מחלת לב?", "answer": "לא בהכרח. זה יכול להיות אות בתוך תמונת סיכון רחבה יותר. קלינאים מפרשים זאת יחד עם פרופיל השומנים וגורמי הסיכון שלך."},
                {"question": "צריך צום לפני בדיקת Lp(a)?", "answer": "ההנחיות משתנות בין מעבדות. במקרים רבים פועלים לפי הוראות המעבדה; אם יש ספק, להתייעץ עם הרופא/ה."},
            ],
            "hi": [
                {"question": "Lp(a) क्या है?", "answer": "Lp(a) का मतलब lipoprotein(a) है। यह कोलेस्ट्रॉल से जुड़ा रक्त मार्कर है और कई बार यह जेनेटिक्स से प्रभावित होता है।"},
                {"question": "क्या Lp(a), LDL कोलेस्ट्रॉल जैसा ही है?", "answer": "नहीं। LDL LDL पार्टिकल्स में मौजूद कोलेस्ट्रॉल बताता है, जबकि Lp(a) lipoprotein(a) से जुड़ा अलग मार्कर है।"},
                {"question": "क्या Lp(a) हाई होने का मतलब हमेशा हार्ट डिजीज है?", "answer": "ज़रूरी नहीं। यह व्यापक जोखिम तस्वीर का एक संकेत हो सकता है। डॉक्टर इसे आपके कुल लिपिड और रिस्क फैक्टर्स के साथ देखते हैं।"},
                {"question": "Lp(a) टेस्ट के लिए क्या फास्ट/अवधि ज़रूरी है?", "answer": "लैब के निर्देश बदल सकते हैं। आम तौर पर लैब के निर्देश फॉलो किए जाते हैं; संदेह हो तो डॉक्टर से पूछें।"},
            ],
            "ar": [
                {"question": "ما هي Lp(a)؟", "answer": "Lp(a) تعني lipoprotein(a). وهو مؤشر مرتبط بالكوليسترول في الدم وغالباً يتأثر بالوراثة."},
                {"question": "هل Lp(a) هي نفسها كوليسترول LDL؟", "answer": "لا. كوليسترول LDL يعكس الكوليسترول داخل جسيمات LDL، بينما Lp(a) مؤشر مختلف مرتبط بليبوبروتين(a)."},
                {"question": "هل ارتفاع Lp(a) يعني دائماً مرض القلب؟", "answer": "ليس بالضرورة. قد يكون إشارة ضمن صورة مخاطر أوسع. الأطباء يفسرونه مع عوامل الخطر والدهون الأخرى."},
                {"question": "هل يجب الصيام قبل تحليل Lp(a)؟", "answer": "قد تختلف التوصيات حسب المختبر. اتبع تعليمات المختبر وتحدث مع طبيبك إذا كنت غير متأكد."},
            ],
        },
        icon=None,
        last_updated=published,
    )

