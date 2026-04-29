#!/usr/bin/env python3
"""Generate Spanish sections for vitamin deficiency article."""

content = '''

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
'''

with open('/Users/ufukurhan/norya/app/blog_article_vitamin_deficiency_content.py', 'a') as f:
    f.write(content)

print("Spanish sections written")
