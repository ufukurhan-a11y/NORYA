#!/usr/bin/env python3
"""Generate remaining sections for vitamin deficiency article."""

sections = []

# ============================================================
# GERMAN (_sections_de)
# ============================================================
sections.append('''
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
''')

with open('/Users/ufukurhan/norya/app/blog_article_vitamin_deficiency_content.py', 'a') as f:
    f.write(sections[0])

print("German sections written")
