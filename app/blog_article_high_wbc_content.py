# -*- coding: utf-8 -*-
"""
High WBC (white blood cells) blog article — full body content for all 9 languages.
Used by blog_i18n._article_high_wbc(). Sections: intro, what-is-wbc, what-high-means,
infection-vs-inflammation, common-causes, temporary, result-alone, other-tests,
when-to-see-doctor, how-norya-helps, cta, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")


def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="High WBC: infection or inflammation?",
                body_html="<p>A high white blood cell count (WBC) on your lab report often raises one question: could this be an infection, or is it inflammation? The answer matters for your peace of mind and for your doctor’s next steps—but the number alone cannot tell the full story. This guide explains what WBC measures, what a high result can mean, and how to use it in context.</p>"),
        Section(id="what-is-wbc", level=2, heading="What is WBC and what does it measure?",
                body_html="<p><strong>WBC</strong> (white blood cells, or leukocytes) is the total number of white blood cells in a given volume of blood. These cells are part of your immune system: they help fight infections and respond to inflammation, injury, or stress. A routine <a href=\"/en/blog/how-to-understand-wbc-rbc-hgb-and-hct\">complete blood count (CBC)</a> almost always includes WBC; sometimes the lab also reports a &ldquo;differential&rdquo; (neutrophils, lymphocytes, monocytes, etc.), which gives more detail.</p>"),
        Section(id="what-high-means", level=2, heading="What can a high WBC mean?",
                body_html="<p>A high WBC count means your body is making or releasing more white blood cells than usual. That often happens when the immune system is activated—for example by a bacterial or viral infection, inflammation (from injury, illness, or chronic conditions), certain medicines, stress, or even vigorous exercise. So a high WBC is a <em>signal</em>, not a diagnosis: it suggests something is engaging your immune system, but it does not say what.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="Infection vs inflammation: what’s the difference?",
                body_html="<p><strong>Infection</strong> usually means a germ (bacteria, virus, fungus, or parasite) is present and your immune system is responding. Symptoms might include fever, fatigue, or localised pain, depending on the site. <strong>Inflammation</strong> is the body’s general response to injury or irritation—it can occur with or without infection (e.g. after surgery, with autoimmune conditions, or with chronic disease). Both can raise WBC. Your doctor will use your symptoms, history, and sometimes the WBC <em>differential</em> (e.g. high neutrophils vs high lymphocytes) and other tests to narrow down the cause.</p>"),
        Section(id="common-causes", level=2, heading="Common causes of high WBC",
                body_html="<p>Typical reasons for an elevated WBC include: <strong>acute infections</strong> (e.g. urinary, respiratory, or skin); <strong>inflammation</strong> (e.g. after surgery, with arthritis or inflammatory bowel disease); <strong>medications</strong> (e.g. steroids or some drugs that stimulate the bone marrow); <strong>stress or intense exercise</strong> (temporary); <strong>smoking</strong>; and sometimes <strong>pregnancy</strong>. Less often, blood or bone marrow conditions can cause a high WBC; that is something your doctor would consider if the picture does not fit infection or inflammation.</p>"),
        Section(id="temporary", level=2, heading="When can a high WBC be temporary?",
                body_html="<p>WBC can go up briefly with physical stress, a recent workout, emotional stress, dehydration, or right after a meal in some people. If you had one of these around the time of the blood draw, a mildly high result might normalise on a repeat test. Your doctor can advise whether a repeat is needed.</p>"),
        Section(id="result-alone", level=2, heading="Is the result enough on its own?",
                body_html="<p>No. A single high WBC does not tell you whether you have an infection, inflammation, or something else—and it never replaces a clinical assessment. Your doctor will combine it with your symptoms, history, examination, and often other blood work (e.g. <a href=\"/en/blog/what-do-low-or-high-platelets-mean\">platelets</a>, <a href=\"/en/blog/lymphocytes-high-or-low\">lymphocytes</a>, <a href=\"/en/blog/monocytes-high-meaning\">monocytes</a>, or markers like CRP) to decide what to do next.</p>"),
        Section(id="other-tests", level=2, heading="What other tests might doctors look at?",
                body_html="<p>Depending on the situation, the doctor may order a <strong>WBC differential</strong> (breakdown of neutrophil, lymphocyte, monocyte, etc.), <strong>CRP</strong> or other inflammation markers, <strong>blood cultures</strong> if infection is suspected, or further imaging or specialist tests. The goal is to match the results to your clinical picture.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="When should I see a doctor?",
                body_html="<p>If you have symptoms such as fever, severe fatigue, unexplained weight loss, night sweats, or pain—or if your report says your WBC is very high or you have other abnormal counts—you should have a clinical review. Even without symptoms, it’s wise to share an abnormal result with your doctor so they can interpret it in context and suggest follow-up if needed.</p>"),
        Section(id="how-norya-helps", level=2, heading="How Norya makes this result easier to understand",
                body_html="<p>At Norya, we don’t diagnose—we help you prepare. You can <a href=\"/analyze\">upload your lab report</a> and get a clear, structured summary that explains your values (including WBC) in plain language, with reference ranges and context. That can make it easier to discuss results with your doctor and to ask the right questions. For options and pricing, see our <a href=\"/pricing\">pricing page</a>.</p>"),
        Section(id="cta", level=2, heading="Next step",
                body_html="<p>If you’d like a clear, organised view of your blood test—including WBC and other CBC results—you can <a href=\"/analyze\">start an analysis</a> with Norya. Use it to prepare for your appointment, not as a substitute for medical advice.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html="<p><strong>This content is for information only and does not replace medical advice or diagnosis.</strong> A high WBC can have many causes; only a healthcare professional who knows your history and context can interpret your result properly. Always discuss your lab results with a doctor.</p>"),
    ]


def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="WBC yüksek: enfeksiyon mu, iltihap mı?",
                body_html="<p>Laboratuvar raporunuzda beyaz küre (WBC) sayısının yüksek çıkması sıklıkla tek bir soruyu getirir: Bu enfeksiyona mı yoksa iltihaba mı işaret? Cevap hem sizin için hem de hekiminizin sonraki adımları için önemli—ancak tek başına sayı her şeyi anlatmaz. Bu rehber, WBC’nin ne ölçtüğünü, yüksek sonucun ne anlama gelebileceğini ve bunu nasıl bağlamında kullanacağınızı anlatıyor.</p>"),
        Section(id="what-is-wbc", level=2, heading="WBC nedir, neyi ölçer?",
                body_html="<p><strong>WBC</strong> (beyaz kan hücreleri, lökosit) belirli bir kan hacminde bulunan beyaz kan hücrelerinin toplam sayısıdır. Bu hücreler bağışıklık sisteminizin bir parçasıdır: enfeksiyonlarla savaşmaya ve iltihap, yaralanma veya strese yanıt vermeye yardım eder. Rutin bir <a href=\"/tr/blog/wbc-rbc-hgb-hct-nasil-okunur\">tam kan sayımında (CBC)</a> neredeyse her zaman WBC bulunur; bazen laboratuvar &ldquo;lökosit formülü&rdquo; (nötrofil, lenfosit, monosit vb.) de verir ve bu daha fazla ayrıntı sağlar.</p>"),
        Section(id="what-high-means", level=2, heading="WBC yüksekliği ne anlama gelebilir?",
                body_html="<p>WBC yüksekliği, vücudunuzun normalden daha fazla beyaz kan hücresi ürettiği veya dolaşıma saldığı anlamına gelir. Bu genellikle bağışıklık sistemi uyarıldığında olur—örneğin bakteriyel veya viral enfeksiyon, iltihap (yaralanma, hastalık veya kronik durumlardan), bazı ilaçlar, stres veya yoğun egzersiz. Yani yüksek WBC bir <em>sinyal</em>dir, teşhis değil: bağışıklığınızı harekete geçiren bir şey olduğunu gösterir ama ne olduğunu söylemez.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="Enfeksiyon ve iltihap farkı",
                body_html="<p><strong>Enfeksiyon</strong> genelde bir mikrobun (bakteri, virüs, mantar veya parazit) varlığı ve buna karşı bağışıklık yanıtı demektir. Belirtiler enfeksiyon yerine göre ateş, yorgunluk veya bölgesel ağrı olabilir. <strong>İltihap</strong> ise vücudun yaralanma veya tahrişe genel yanıtıdır—enfeksiyon olsun olmasın ortaya çıkabilir (ameliyat sonrası, otoimmün durumlar veya kronik hastalıkta). İkisi de WBC’yi yükseltebilir. Hekiminiz belirtilerinizi, öykünüzü ve bazen WBC <em>formülünü</em> (örn. yüksek nötrofil vs yüksek lenfosit) ve diğer testleri kullanarak nedeni daraltır.</p>"),
        Section(id="common-causes", level=2, heading="WBC yüksekliğinin yaygın nedenleri",
                body_html="<p>Yüksek WBC’nin sık nedenleri: <strong>akut enfeksiyonlar</strong> (idrar yolu, solunum veya cilt); <strong>iltihap</strong> (ameliyat sonrası, artrit veya inflamatuar bağırsak hastalığı); <strong>ilaçlar</strong> (kortikosteroidler veya kemik iliğini uyaran bazı ilaçlar); <strong>stres veya yoğun egzersiz</strong> (geçici); <strong>sigara</strong>; bazen <strong>hamilelik</strong>. Daha seyrek olarak kan veya kemik iliği hastalıkları WBC’yi yükseltebilir; hekiminiz tablo enfeksiyon veya iltihapla uyuşmazsa bunu değerlendirir.</p>"),
        Section(id="temporary", level=2, heading="Ne zaman geçici yükseklik olabilir?",
                body_html="<p>Fiziksel stres, son yapılan egzersiz, duygusal stres, sıvı kaybı veya bazı kişilerde yemek sonrası WBC kısa süreli yükselebilir. Kan alımına yakın böyle bir durumunuz varsa hafif yüksek sonuç tekrarda normale dönebilir. Tekrar gerekip gerekmediğini hekiminiz söyleyebilir.</p>"),
        Section(id="result-alone", level=2, heading="Sonuç tek başına yeterli mi?",
                body_html="<p>Hayır. Tek bir yüksek WBC enfeksiyon mu, iltihap mı yoksa başka bir şey mi olduğunu göstermez—ve klinik değerlendirmenin yerini almaz. Hekiminiz bunu belirtileriniz, öykü, muayene ve sıklıkla diğer kan sonuçlarıyla (<a href=\"/tr/blog/trombosit-yuksekligi-ve-dusuklugu-ne-demek\">trombosit</a>, <a href=\"/tr/blog/lymphocytes-high-or-low\">lenfosit</a>, <a href=\"/tr/blog/monocytes-high-meaning\">monosit</a> veya CRP gibi belirteçler) bir arada yorumlayarak sonraki adımı belirler.</p>"),
        Section(id="other-tests", level=2, heading="Hekimler hangi ek testlere bakar?",
                body_html="<p>Duruma göre <strong>lökosit formülü</strong> (nötrofil, lenfosit, monosit dağılımı), <strong>CRP</strong> veya diğer iltihap belirteçleri, enfeksiyon düşünülüyorsa <strong>kan kültürü</strong> veya ek görüntüleme / uzman tetkikleri istenebilir. Amaç, sonuçları klinik tablonuzla eşleştirmektir.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Ne zaman hekime gitmeliyim?",
                body_html="<p>Ateş, ciddi yorgunluk, açıklanamayan kilo kaybı, gece terlemesi veya ağrı gibi belirtileriniz varsa—veya raporunuzda WBC’nin çok yüksek olduğu veya başka anormal sayımlar yazıyorsa—klinik değerlendirme yaptırmalısınız. Belirti olmasa bile anormal sonucu hekiminizle paylaşmak, bağlamında yorumlaması ve gerekirse takip önermesi için doğru adımdır.</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya bu sonucu nasıl anlaşılır kılar?",
                body_html="<p>Norya’da teşhis koymuyoruz—randevunuza hazırlanmanıza yardım ediyoruz. <a href=\"/analyze\">Laboratuvar raporunuzu yükleyerek</a> değerlerinizi (WBC dahil) sade dilde, referans aralıkları ve bağlamıyla açıklayan net, yapılandırılmış bir özet alabilirsiniz. Böylece hekiminizle sonuçları konuşmak ve doğru soruları sormak kolaylaşır. Seçenekler ve fiyatlar için <a href=\"/pricing\">fiyatlandırma sayfamıza</a> bakın.</p>"),
        Section(id="cta", level=2, heading="Sonraki adım",
                body_html="<p>Kan tahlilinizi—WBC ve diğer CBC değerleri dahil—net ve düzenli bir şekilde görmek isterseniz Norya ile <a href=\"/analyze\">analiz başlatabilirsiniz</a>. Bunu randevunuza hazırlık için kullanın; tıbbi tavsiyenin yerine koymayın.</p>"),
        Section(id="disclaimer", level=2, heading="Uyarı",
                body_html="<p><strong>Bu içerik yalnızca bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.</strong> WBC yüksekliğinin birçok nedeni olabilir; sonucunuzu ancak öykünüzü ve bağlamını bilen bir sağlık profesyoneli doğru yorumlayabilir. Laboratuvar sonuçlarınızı her zaman bir hekimle görüşün.</p>"),
    ]


def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Glóbulos blancos altos: ¿infección o inflamación?",
                body_html="<p>Un recuento alto de glóbulos blancos (WBC) en el análisis suele plantear una duda: ¿será infección o inflamación? La respuesta importa para tu tranquilidad y para los siguientes pasos del médico; pero el número solo no cuenta toda la historia. Esta guía explica qué mide el WBC, qué puede significar un valor alto y cómo contextualizarlo.</p>"),
        Section(id="what-is-wbc", level=2, heading="¿Qué es el WBC y qué mide?",
                body_html="<p>El <strong>WBC</strong> (glóbulos blancos o leucocitos) es el número total de glóbulos blancos en un volumen de sangre. Forman parte de tu sistema inmunitario: ayudan a combatir infecciones y a responder a inflamación, lesión o estrés. Un <a href=\"/es/blog/como-entender-wbc-rbc-hgb-y-hct\">hemograma</a> suele incluir el WBC; a veces el laboratorio da también la fórmula leucocitaria (neutrófilos, linfocitos, monocitos, etc.).</p>"),
        Section(id="what-high-means", level=2, heading="¿Qué puede significar un WBC alto?",
                body_html="<p>Un WBC alto indica que el cuerpo produce o libera más glóbulos blancos de lo habitual. Suele ocurrir cuando se activa el sistema inmunitario—por una infección bacteriana o viral, inflamación (por lesión, enfermedad o procesos crónicos), ciertos medicamentos, estrés o ejercicio intenso. Así que un WBC alto es una <em>señal</em>, no un diagnóstico: sugiere que algo activa tus defensas, pero no dice qué.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="Infección frente a inflamación",
                body_html="<p><strong>Infección</strong> suele implicar un germen (bacteria, virus, hongo o parásito) y una respuesta inmunitaria. Pueden aparecer fiebre, cansancio o dolor local. <strong>Inflamación</strong> es la respuesta del cuerpo a daño o irritación—con o sin infección (p. ej. tras cirugía, en enfermedades autoinmunes o crónicas). Ambas pueden subir el WBC. El médico usará tus síntomas, historia y a veces la fórmula (p. ej. neutrófilos vs linfocitos) y otras pruebas para acotar la causa.</p>"),
        Section(id="common-causes", level=2, heading="Causas frecuentes de WBC alto",
                body_html="<p>Entre las causas habituales: <strong>infecciones agudas</strong> (urinarias, respiratorias, cutáneas); <strong>inflamación</strong> (posoperatoria, artritis, enfermedad inflamatoria intestinal); <strong>medicamentos</strong> (corticoides o algunos que estimulan la médula); <strong>estrés o ejercicio intenso</strong> (transitorio); <strong>tabaco</strong>; a veces <strong>embarazo</strong>. Con menos frecuencia, alteraciones de sangre o médula pueden elevar el WBC; el médico lo valorará si el cuadro no encaja con infección o inflamación.</p>"),
        Section(id="temporary", level=2, heading="¿Cuándo puede ser transitorio?",
                body_html="<p>El WBC puede subir de forma breve por estrés físico, ejercicio reciente, estrés emocional, deshidratación o tras comer en algunas personas. Si algo de esto coincidió con la extracción, un valor algo alto puede normalizarse en un nuevo análisis. Tu médico puede indicar si conviene repetir.</p>"),
        Section(id="result-alone", level=2, heading="¿El resultado basta por sí solo?",
                body_html="<p>No. Un WBC alto aislado no indica si hay infección, inflamación u otra cosa, y no sustituye la valoración clínica. El médico lo combinará con síntomas, historia, exploración y otras pruebas (<a href=\"/es/blog/plaquetas-altas-o-bajas-que-significa\">plaquetas</a>, <a href=\"/es/blog/lymphocytes-high-or-low\">linfocitos</a>, <a href=\"/es/blog/monocytes-high-meaning\">monocitos</a>, PCR, etc.) para decidir los siguientes pasos.</p>"),
        Section(id="other-tests", level=2, heading="¿Qué otras pruebas puede pedir el médico?",
                body_html="<p>Según el caso: <strong>fórmula leucocitaria</strong>, <strong>PCR</strong> u otros marcadores de inflamación, <strong>hemocultivos</strong> si se sospecha infección, o más pruebas o imagen. El objetivo es encajar los resultados con tu cuadro clínico.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="¿Cuándo debo ir al médico?",
                body_html="<p>Si tienes fiebre, cansancio intenso, pérdida de peso sin explicación, sudoración nocturna o dolor—o si el informe indica un WBC muy alto u otras alteraciones—debes hacer una valoración clínica. Aunque no haya síntomas, es recomendable comentar un resultado anormal con tu médico para que lo interprete en contexto y proponga seguimiento si hace falta.</p>"),
        Section(id="how-norya-helps", level=2, heading="Cómo Norya hace más comprensible este resultado",
                body_html="<p>En Norya no hacemos diagnósticos; te ayudamos a prepararte. Puedes <a href=\"/analyze\">subir tu informe</a> y obtener un resumen claro que explica tus valores (incluido el WBC) en lenguaje sencillo, con rangos de referencia. Así te resultará más fácil hablar con tu médico. Para opciones y precios, consulta nuestra <a href=\"/pricing\">página de precios</a>.</p>"),
        Section(id="cta", level=2, heading="Siguiente paso",
                body_html="<p>Si quieres una visión ordenada de tu análisis—incluido el WBC y el resto del hemograma—puedes <a href=\"/analyze\">iniciar un análisis</a> con Norya. Úsalo para preparar la consulta, no como sustituto del criterio médico.</p>"),
        Section(id="disclaimer", level=2, heading="Aviso",
                body_html="<p><strong>Este contenido es solo informativo y no sustituye el consejo ni el diagnóstico médico.</strong> Un WBC alto puede deberse a muchas causas; solo un profesional que conozca tu historia puede interpretarlo bien. Comenta siempre tus resultados con un médico.</p>"),
    ]


def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Leukozyten erhöht: Infektion oder Entzündung?",
                body_html="<p>Ein erhöhter Leukozytenwert (WBC) auf dem Laborbericht wirft oft eine Frage auf: Könnte das eine Infektion sein oder eine Entzündung? Die Antwort ist für Sie und die nächsten Schritte des Arztes wichtig—aber der Wert allein sagt nicht alles. Dieser Ratgeber erklärt, was der WBC misst, was ein erhöhter Befund bedeuten kann und wie man ihn einordnet.</p>"),
        Section(id="what-is-wbc", level=2, heading="Was ist der WBC und was wird gemessen?",
                body_html="<p>Der <strong>WBC</strong> (weiße Blutkörperchen, Leukozyten) ist die Gesamtzahl der weißen Blutkörperchen in einem bestimmten Blutvolumen. Sie gehören zum Immunsystem und bekämpfen Infektionen bzw. reagieren auf Entzündung, Verletzung oder Stress. Ein kleines <a href=\"/de/blog/wbc-rbc-und-hct-verstehen\">Blutbild</a> enthält fast immer den WBC; manchmal liefert das Labor auch ein Differentialblutbild (Neutrophile, Lymphozyten, Monozyten usw.).</p>"),
        Section(id="what-high-means", level=2, heading="Was kann ein erhöhter WBC bedeuten?",
                body_html="<p>Ein erhöhter WBC bedeutet, dass der Körper mehr weiße Blutkörperchen bildet oder freisetzt als üblich. Das passiert oft, wenn das Immunsystem aktiviert ist—z. B. durch bakterielle oder virale Infektion, Entzündung (nach Verletzung, bei Erkrankung oder chronischen Prozessen), bestimmte Medikamente, Stress oder starke körperliche Belastung. Ein hoher WBC ist also ein <em>Hinweis</em>, keine Diagnose: Er zeigt, dass etwas das Immunsystem beschäftigt, aber nicht was.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="Infektion vs. Entzündung",
                body_html="<p>Eine <strong>Infektion</strong> bedeutet in der Regel, dass ein Keim (Bakterium, Virus, Pilz oder Parasit) vorliegt und das Immunsystem reagiert. Es können Fieber, Müdigkeit oder lokale Schmerzen auftreten. <strong>Entzündung</strong> ist die Reaktion des Körpers auf Schaden oder Reiz—mit oder ohne Infektion (z. B. nach OP, bei Autoimmunerkrankungen oder chronischen Leiden). Beides kann den WBC erhöhen. Der Arzt nutzt Symptome, Anamnese und ggf. das Differentialblutbild und weitere Tests zur Einordnung.</p>"),
        Section(id="common-causes", level=2, heading="Häufige Ursachen für erhöhten WBC",
                body_html="<p>Typische Gründe: <strong>akute Infektionen</strong> (z. B. Harnwegs-, Atemwegs-, Hautinfektionen); <strong>Entzündung</strong> (z. B. nach OP, bei Arthritis oder chronisch-entzündlicher Darmerkrankung); <strong>Medikamente</strong> (z. B. Kortison oder bestimmte Substanzen, die das Knochenmark anregen); <strong>Stress oder intensive körperliche Belastung</strong> (vorübergehend); <strong>Rauchen</strong>; manchmal <strong>Schwangerschaft</strong>. Seltener können Blut- oder Knochenmarkerkrankungen den WBC erhöhen; das prüft der Arzt, wenn das Gesamtbild nicht zu Infektion oder Entzündung passt.</p>"),
        Section(id="temporary", level=2, heading="Wann kann die Erhöhung vorübergehend sein?",
                body_html="<p>Der WBC kann kurzfristig durch körperlichen oder emotionalen Stress, kürzliche körperliche Anstrengung, Dehydratation oder bei manchen nach dem Essen ansteigen. Bei leichter Erhöhung kann eine Kontrolle normieren. Ob eine Wiederholung sinnvoll ist, entscheidet der Arzt.</p>"),
        Section(id="result-alone", level=2, heading="Reicht der Befund allein?",
                body_html="<p>Nein. Ein einzelner erhöhter WBC sagt nicht, ob eine Infektion, Entzündung oder etwas anderes vorliegt—und ersetzt keine klinische Beurteilung. Der Arzt wird ihn mit Symptomen, Anamnese, Untersuchung und oft weiteren Werten (<a href=\"/de/blog/thrombozyten-zu-hoch-oder-zu-niedrig\">Thrombozyten</a>, <a href=\"/de/blog/lymphocytes-high-or-low\">Lymphozyten</a>, <a href=\"/de/blog/monocytes-high-meaning\">Monozyten</a>, CRP o. Ä.) zusammen auswerten.</p>"),
        Section(id="other-tests", level=2, heading="Welche weiteren Tests kann der Arzt anordnen?",
                body_html="<p>Je nach Situation: <strong>Differentialblutbild</strong>, <strong>CRP</strong> oder andere Entzündungsmarker, <strong>Blutkulturen</strong> bei Verdacht auf Infektion, oder weitere Diagnostik. Ziel ist, die Befunde mit dem klinischen Bild in Einklang zu bringen.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Wann sollte ich zum Arzt?",
                body_html="<p>Bei Fieber, starker Müdigkeit, ungewolltem Gewichtsverlust, Nachtschweiß oder Schmerzen—oder wenn der Bericht einen sehr hohen WBC oder andere Auffälligkeiten zeigt—sollten Sie sich klinisch abklären lassen. Auch ohne Beschwerden ist es sinnvoll, einen auffälligen Wert mit dem Arzt zu besprechen.</p>"),
        Section(id="how-norya-helps", level=2, heading="Wie Norya diesen Befund verständlicher macht",
                body_html="<p>Bei Norya stellen wir keine Diagnosen—wir helfen bei der Vorbereitung. Sie können Ihren <a href=\"/analyze\">Laborbericht hochladen</a> und eine klare, strukturierte Auswertung erhalten, die Ihre Werte (inkl. WBC) verständlich erklärt. So fällt das Gespräch mit dem Arzt leichter. Optionen und Preise: <a href=\"/pricing\">Preise</a>.</p>"),
        Section(id="cta", level=2, heading="Nächster Schritt",
                body_html="<p>Wenn Sie Ihre Blutwerte—inkl. WBC und restliches Blutbild—klar geordnet sehen möchten, können Sie bei Norya <a href=\"/analyze\">eine Analyse starten</a>. Nutzen Sie sie zur Vorbereitung auf den Arzttermin, nicht als Ersatz für medizinische Beratung.</p>"),
        Section(id="disclaimer", level=2, heading="Hinweis",
                body_html="<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung oder Diagnose.</strong> Ein erhöhter WBC kann viele Ursachen haben; nur eine Fachperson mit Kenntnis Ihrer Anamnese kann ihn einordnen. Besprechen Sie Laborergebnisse immer mit einem Arzt.</p>"),
    ]


def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Globules blancs élevés : infection ou inflammation ?",
                body_html="<p>Un taux élevé de globules blancs (GB) sur votre bilan sanguin pose souvent une question : est-ce une infection ou une inflammation ? La réponse compte pour vous et pour la suite que prendra le médecin—mais le chiffre seul ne dit pas tout. Ce guide explique ce que mesure le taux de GB, ce qu’un résultat élevé peut signifier et comment le replacer dans le contexte.</p>"),
        Section(id="what-is-wbc", level=2, heading="Qu’est-ce que le taux de GB et que mesure-t-on ?",
                body_html="<p>Le <strong>taux de GB</strong> (globules blancs ou leucocytes) est le nombre total de globules blancs dans un volume de sang donné. Ils font partie de votre système immunitaire : ils aident à lutter contre les infections et à réagir à l’inflammation, à une blessure ou au stress. Une <a href=\"/fr/blog/comprendre-globules-blancs-rouges-hgb-hct\">numération formule sanguine (NFS)</a> inclut presque toujours les GB ; parfois le laboratoire donne aussi la formule (neutrophiles, lymphocytes, monocytes, etc.).</p>"),
        Section(id="what-high-means", level=2, heading="Que peut signifier un taux de GB élevé ?",
                body_html="<p>Un taux élevé signifie que l’organisme produit ou libère plus de globules blancs que la normale. Cela arrive souvent quand le système immunitaire est activé—par une infection bactérienne ou virale, une inflammation (blessure, maladie ou affection chronique), certains médicaments, le stress ou un effort intense. Un taux élevé est donc un <em>signal</em>, pas un diagnostic : il indique que quelque chose mobilise vos défenses, mais ne dit pas quoi.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="Infection ou inflammation : quelle différence ?",
                body_html="<p>Une <strong>infection</strong> signifie en général qu’un germe (bactérie, virus, champignon ou parasite) est présent et que le système immunitaire réagit. Les symptômes peuvent inclure fièvre, fatigue ou douleur localisée. L’<strong>inflammation</strong> est la réaction de l’organisme à une agression ou une irritation—avec ou sans infection (après chirurgie, maladie auto-immune, maladie chronique). Les deux peuvent faire monter les GB. Le médecin s’appuie sur vos symptômes, votre histoire et parfois la formule (neutrophiles vs lymphocytes) et d’autres examens pour préciser la cause.</p>"),
        Section(id="common-causes", level=2, heading="Causes fréquentes de GB élevés",
                body_html="<p>Causes typiques : <strong>infections aiguës</strong> (urinaires, respiratoires, cutanées) ; <strong>inflammation</strong> (post-opératoire, arthrite, maladie inflammatoire intestinale) ; <strong>médicaments</strong> (corticoïdes ou certains qui stimulent la moelle) ; <strong>stress ou effort intense</strong> (transitoire) ; <strong>tabac</strong> ; parfois <strong>grossesse</strong>. Plus rarement, des affections du sang ou de la moelle peuvent augmenter les GB ; le médecin y pensera si le tableau ne correspond pas à une infection ou une inflammation.</p>"),
        Section(id="temporary", level=2, heading="Quand l’élévation peut-elle être transitoire ?",
                body_html="<p>Le taux peut monter brièvement avec le stress physique, un effort récent, le stress émotionnel, la déshydratation ou après un repas chez certaines personnes. Si l’un de ces facteurs coïncide avec la prise de sang, une légère élévation peut se normaliser à la répétition. Le médecin vous dira s’il faut refaire le bilan.</p>"),
        Section(id="result-alone", level=2, heading="Le résultat suffit-il à lui seul ?",
                body_html="<p>Non. Un taux élevé isolé ne dit pas s’il s’agit d’une infection, d’une inflammation ou d’autre chose—et ne remplace pas l’évaluation clinique. Le médecin le combinera à vos symptômes, antécédents, examen et souvent à d’autres résultats (<a href=\"/fr/blog/plaquettes-trop-hautes-ou-basses\">plaquettes</a>, <a href=\"/fr/blog/lymphocytes-high-or-low\">lymphocytes</a>, <a href=\"/fr/blog/monocytes-high-meaning\">monocytes</a>, CRP, etc.) pour décider de la suite.</p>"),
        Section(id="other-tests", level=2, heading="Quels autres examens le médecin peut-il demander ?",
                body_html="<p>Selon le cas : <strong>formule sanguine</strong> (détail neutrophiles, lymphocytes, etc.), <strong>CRP</strong> ou autres marqueurs d’inflammation, <strong>hémocultures</strong> en cas de suspicion d’infection, ou examens complémentaires. L’objectif est de faire correspondre les résultats à votre tableau clinique.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quand consulter ?",
                body_html="<p>En cas de fièvre, fatigue importante, perte de poids inexpliquée, sueurs nocturnes ou douleurs—ou si le compte rendu indique un taux très élevé ou d’autres anomalies—il faut une évaluation clinique. Même sans symptômes, il est utile de montrer un résultat anormal à votre médecin pour qu’il l’interprète en contexte et propose un suivi si besoin.</p>"),
        Section(id="how-norya-helps", level=2, heading="Comment Norya rend ce résultat plus lisible",
                body_html="<p>Chez Norya, nous ne posons pas de diagnostic—nous vous aidons à vous préparer. Vous pouvez <a href=\"/analyze\">envoyer votre bilan</a> et obtenir un résumé clair qui explique vos valeurs (dont les GB) en langage simple, avec les fourchettes de référence. Cela facilite le dialogue avec le médecin. Pour les options et tarifs : <a href=\"/pricing\">tarifs</a>.</p>"),
        Section(id="cta", level=2, heading="Prochaine étape",
                body_html="<p>Pour avoir une vue claire et structurée de votre bilan—GB et reste de la NFS inclus—vous pouvez <a href=\"/analyze\">lancer une analyse</a> avec Norya. À utiliser pour préparer la consultation, pas en remplacement d’un avis médical.</p>"),
        Section(id="disclaimer", level=2, heading="Avertissement",
                body_html="<p><strong>Ce contenu est à titre informatif uniquement et ne remplace pas un avis ou un diagnostic médical.</strong> Un taux de GB élevé peut avoir de nombreuses causes ; seul un professionnel qui connaît votre contexte peut l’interpréter. Discutez toujours de vos résultats avec un médecin.</p>"),
    ]


def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="Globuli bianchi alti: infezione o infiammazione?",
                body_html="<p>Un valore alto di globuli bianchi (WBC) sul referto spesso fa venire una domanda: potrebbe essere un’infezione o un’infiammazione? La risposta conta per te e per i prossimi passi del medico—ma il numero da solo non dice tutto. Questa guida spiega cosa misura il WBC, cosa può significare un valore alto e come inquadrarlo.</p>"),
        Section(id="what-is-wbc", level=2, heading="Cos’è il WBC e cosa si misura?",
                body_html="<p>Il <strong>WBC</strong> (globuli bianchi o leucociti) è il numero totale di globuli bianchi in un dato volume di sangue. Fanno parte del sistema immunitario: aiutano a combattere le infezioni e a rispondere a infiammazione, trauma o stress. Un <a href=\"/it/blog/come-leggere-wbc-rbc-hgb-hct\">emocromo</a> include quasi sempre il WBC; a volte il laboratorio fornisce anche la formula leucocitaria (neutrofili, linfociti, monociti, ecc.).</p>"),
        Section(id="what-high-means", level=2, heading="Cosa può significare un WBC alto?",
                body_html="<p>Un WBC alto significa che l’organismo produce o rilascia più globuli bianchi del solito. Succede spesso quando il sistema immunitario è attivato—da un’infezione batterica o virale, un’infiammazione (post-operatoria, da malattia cronica), alcuni farmaci, stress o esercizio intenso. Quindi un WBC alto è un <em>segnale</em>, non una diagnosi: indica che qualcosa sta attivando le difese, ma non dice cosa.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="Infezione vs infiammazione",
                body_html="<p>Un’<strong>infezione</strong> di solito implica un germe (batterio, virus, fungo o parassita) e una risposta immunitaria. I sintomi possono includere febbre, stanchezza o dolore localizzato. L’<strong>infiammazione</strong> è la risposta dell’organismo a danno o irritazione—con o senza infezione (es. dopo intervento, in malattie autoimmuni o croniche). Entrambe possono alzare il WBC. Il medico userà sintomi, anamnesi e a volte la formula (neutrofili vs linfociti) e altri esami per inquadrare la causa.</p>"),
        Section(id="common-causes", level=2, heading="Cause comuni di WBC alto",
                body_html="<p>Cause tipiche: <strong>infezioni acute</strong> (urinarie, respiratorie, cutanee); <strong>infiammazione</strong> (post-operatoria, artrite, malattia infiammatoria intestinale); <strong>farmaci</strong> (cortisonici o altri che stimolano il midollo); <strong>stress o esercizio intenso</strong> (transitorio); <strong>fumo</strong>; a volte <strong>gravidanza</strong>. Più raramente, condizioni del sangue o del midollo possono alzare il WBC; il medico lo valuterà se il quadro non rientra in infezione o infiammazione.</p>"),
        Section(id="temporary", level=2, heading="Quando l’innalzamento può essere transitorio?",
                body_html="<p>Il WBC può salire brevemente per stress fisico, esercizio recente, stress emotivo, disidratazione o dopo i pasti in alcune persone. Se uno di questi fattori coincide con il prelievo, un valore leggermente alto può normalizzarsi al controllo. Il medico indicherà se ripetere l’esame.</p>"),
        Section(id="result-alone", level=2, heading="Il risultato da solo basta?",
                body_html="<p>No. Un singolo WBC alto non dice se c’è un’infezione, un’infiammazione o altro—e non sostituisce la valutazione clinica. Il medico lo combinerà con sintomi, anamnesi, visita e spesso altri esami (<a href=\"/it/blog/piastrine-alte-o-basse-cosa-significa\">piastrine</a>, <a href=\"/it/blog/lymphocytes-high-or-low\">linfociti</a>, <a href=\"/it/blog/monocytes-high-meaning\">monociti</a>, PCR, ecc.) per decidere i passi successivi.</p>"),
        Section(id="other-tests", level=2, heading="Quali altri esami può richiedere il medico?",
                body_html="<p>A seconda del caso: <strong>formula leucocitaria</strong>, <strong>PCR</strong> o altri marcatori di infiammazione, <strong>emocolture</strong> in sospetto di infezione, o altri accertamenti. L’obiettivo è far combaciare i risultati con il quadro clinico.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="Quando devo rivolgermi al medico?",
                body_html="<p>In caso di febbre, stanchezza marcata, perdita di peso inspiegabile, sudorazione notturna o dolore—o se il referto indica un WBC molto alto o altre alterazioni—è opportuna una valutazione clinica. Anche senza sintomi, è utile mostrare un risultato alterato al medico per interpretarlo in contesto e proporre eventuale follow-up.</p>"),
        Section(id="how-norya-helps", level=2, heading="Come Norya rende più comprensibile questo risultato",
                body_html="<p>In Norya non facciamo diagnosi—ti aiutiamo a prepararti. Puoi <a href=\"/analyze\">caricare il referto</a> e ottenere un riepilogo chiaro che spiega i tuoi valori (incluso il WBC) in linguaggio semplice, con intervalli di riferimento. Così è più facile parlarne con il medico. Per opzioni e prezzi: <a href=\"/pricing\">prezzi</a>.</p>"),
        Section(id="cta", level=2, heading="Prossimo passo",
                body_html="<p>Se vuoi una visione chiara e ordinata del tuo esame del sangue—WBC e resto dell’emocromo incluso—puoi <a href=\"/analyze\">avviare un’analisi</a> con Norya. Usala per prepararti alla visita, non come sostituto del parere medico.</p>"),
        Section(id="disclaimer", level=2, heading="Disclaimer",
                body_html="<p><strong>Questo contenuto è solo a scopo informativo e non sostituisce consulenza o diagnosi medica.</strong> Un WBC alto può avere molte cause; solo un professionista che conosce la tua storia può interpretarlo. Discuti sempre i risultati con un medico.</p>"),
    ]


def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="לויקוציטים גבוהים: זיהום או דלקת?",
                body_html="<p>ספירת דם לבנים (WBC) גבוהה בדו\"ח המעבדה מעלה לא פעם שאלה אחת: האם זה זיהום או דלקת? התשובה חשובה לשקט הנפשי שלך ולצעדים הבאים של הרופא—אבל המספר לבדו לא מספר את כל הסיפור. מדריך זה מסביר מה WBC מודד, מה עלול להעיד ערך גבוה, ואיך להבין אותו בהקשר.</p>"),
        Section(id="what-is-wbc", level=2, heading="מהו WBC ומה נמדד?",
                body_html="<p><strong>WBC</strong> (תאי דם לבנים, לויקוציטים) הוא המספר הכולל של תאי דם לבנים בנפח דם נתון. התאים האלה חלק ממערכת החיסון: הם עוזרים להילחם בזיהומים ולהגיב לדלקת, לפציעה או למתח. ב<a href=\"/he/blog/how-to-understand-wbc-rbc-hgb-and-hct\">ספירת דם מלאה</a> כמעט תמיד נכלל WBC; לעיתים המעבדה נותנת גם נוסחת דם (נויטרופילים, לימפוציטים, מונוציטים וכו').</p>"),
        Section(id="what-high-means", level=2, heading="מה יכול להעיד WBC גבוה?",
                body_html="<p>WBC גבוה משמע שהגוף מייצר או משחרר יותר תאי דם לבנים מהרגיל. זה קורה לא פעם כשמערכת החיסון מופעלת—למשל בזיהום חיידקי או נגיפי, דלקת (מפציעה, מחלה או מצב כרוני), תרופות מסוימות, מתח או פעילות גופנית מאומצת. לכן WBC גבוה הוא <em>סימן</em>, לא אבחנה: הוא מרמז שמשהו מפעיל את מערכת החיסון, אבל לא אומר מה.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="זיהום מול דלקת",
                body_html="<p><strong>זיהום</strong> בדרך כלל משמע שחיידק, נגיף, פטרייה או טפיל נוכחים והמערכת החיסונית מגיבה. תסמינים יכולים לכלול חום, עייפות או כאב מקומי. <strong>דלקת</strong> היא התגובה הכללית של הגוף לפציעה או גירוי—עם או בלי זיהום (למשל אחרי ניתוח, במחלה אוטואימונית או כרונית). שני המצבים יכולים להעלות את ה-WBC. הרופא ישתמש בתסמינים, באנמנזה ולעיתים בנוסחת הדם (למשל נויטרופילים מול לימפוציטים) ובבדיקות נוספות כדי לצמצם את הסיבה.</p>"),
        Section(id="common-causes", level=2, heading="סיבות נפוצות ל-WBC גבוה",
                body_html="<p>סיבות טיפוסיות: <strong>זיהומים חריפים</strong> (שתן, דרכי נשימה, עור); <strong>דלקת</strong> (לאחר ניתוח, דלקת מפרקים או מחלת מעי דלקתית); <strong>תרופות</strong> (סטרואידים או חומרים שמגרים את מח העצם); <strong>מתח או פעילות מאומצת</strong> (זמני); <strong>עישון</strong>; לעיתים <strong>הריון</strong>. פחות שכיח, מצבים של הדם או מח העצם יכולים להעלות WBC; הרופא ישקול זאת אם התמונה לא מתאימה לזיהום או דלקת.</p>"),
        Section(id="temporary", level=2, heading="מתי העלייה יכולה להיות זמנית?",
                body_html="<p>WBC יכול לעלות לזמן קצר עם מתח גופני, אימון אחרון, מתח נפשי, התייבשות או אחרי ארוחה אצל חלק מהאנשים. אם אחד מהגורמים האלה חל בסמוך לדגימת הדם, ערך מעט גבוה עשוי להתייצב בבדיקה חוזרת. הרופא יוכל לומר אם יש צורך בחזרה.</p>"),
        Section(id="result-alone", level=2, heading="האם התוצאה מספיקה לבדה?",
                body_html="<p>לא. WBC גבוה בודד לא אומר אם יש זיהום, דלקת או משהו אחר—והוא לא מחליף הערכה קלינית. הרופא ישלב אותו עם התסמינים, האנמנזה, הבדיקה הגופנית ולעיתים בדיקות דם נוספות (<a href=\"/he/blog/what-do-low-or-high-platelets-mean\">טסיות</a>, <a href=\"/he/blog/lymphocytes-high-or-low\">לימפוציטים</a>, <a href=\"/he/blog/monocytes-high-meaning\">מונוציטים</a>, CRP וכו') כדי להחליט על הצעד הבא.</p>"),
        Section(id="other-tests", level=2, heading="אילו בדיקות נוספות הרופא עשוי להפנות?",
                body_html="<p>בהתאם למצב: <strong>נוסחת דם</strong>, <strong>CRP</strong> או סמני דלקת אחרים, <strong>תרביות דם</strong> בחשד לזיהום, או בדיקות הדמיה וכו'. המטרה היא להתאים את התוצאות לתמונה הקלינית.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="מתי לפנות לרופא?",
                body_html="<p>אם יש חום, עייפות קשה, ירידה במשקל בלתי מוסברת, הזעות לילה או כאב—או אם בדו\"ח מופיע WBC גבוה מאוד או ספירות חריגות אחרות—יש לבצע הערכה קלינית. גם בלי תסמינים, כדאי לחלוק תוצאה חריגה עם הרופא כדי שיוכל לפרש בהקשר ולהציע מעקב אם צריך.</p>"),
        Section(id="how-norya-helps", level=2, heading="איך Norya הופכת את התוצאה הזו למובנת יותר",
                body_html="<p>ב-Norya אנחנו לא מאבחנים—אנחנו עוזרים לך להתכונן. אפשר <a href=\"/analyze\">להעלות את דו\"ח המעבדה</a> ולקבל סיכום ברור ומסודר שמסביר את הערכים (כולל WBC) בשפה פשוטה, עם טווחי ייחוס. כך קל יותר לשוחח עם הרופא. לאפשרויות ומחירים: <a href=\"/pricing\">מחירים</a>.</p>"),
        Section(id="cta", level=2, heading="הצעד הבא",
                body_html="<p>אם תרצה לראות את בדיקת הדם שלך—כולל WBC ושאר ספירת הדם—בצורה ברורה ומסודרת, אפשר <a href=\"/analyze\">להתחיל ניתוח</a> עם Norya. השתמש בזה כדי להתכונן לפגישה, לא כתחליף לייעוץ רפואי.</p>"),
        Section(id="disclaimer", level=2, heading="הודעה",
                body_html="<p><strong>התוכן כאן למידע בלבד ואינו מחליף ייעוץ או אבחנה רפואית.</strong> WBC גבוה יכול לנבוע מסיבות רבות; רק איש מקצוע שמכיר את ההקשר שלך יכול לפרש נכון. תמיד יש לדון בתוצאות המעבדה עם רופא.</p>"),
    ]


def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="हाई WBC: इन्फेक्शन या इन्फ्लेमेशन?",
                body_html="<p>रिपोर्ट में वाइट ब्लड सेल काउंट (WBC) हाई आने पर अक्सर एक सवाल उठता है: यह इन्फेक्शन हो सकता है या सूजन? जवाब आपकी शांति और डॉक्टर के अगले कदमों के लिए मायने रखता है—लेकिन अकेले नंबर पूरी कहानी नहीं बताता। यह गाइड बताती है कि WBC क्या मापता है, हाई रिज़ल्ट का क्या मतलब हो सकता है और उसे कैसे संदर्भ में लें।</p>"),
        Section(id="what-is-wbc", level=2, heading="WBC क्या है और क्या मापा जाता है?",
                body_html="<p><strong>WBC</strong> (वाइट ब्लड सेल, ल्यूकोसाइट्स) खून की एक निश्चित मात्रा में वाइट ब्लड सेल की कुल संख्या होती है। ये सेल इम्यून सिस्टम का हिस्सा हैं: इन्फेक्शन से लड़ने और सूजन, चोट या तनाव पर रिस्पॉन्स करने में मदद करते हैं। रूटीन <a href=\"/hi/blog/how-to-understand-wbc-rbc-hgb-and-hct\">कंप्लीट ब्लड काउंट (CBC)</a> में लगभग हमेशा WBC होता है; कभी लैब डिफरेंशियल (न्यूट्रोफिल, लिम्फोसाइट्स, मोनोसाइट्स आदि) भी देता है।</p>"),
        Section(id="what-high-means", level=2, heading="हाई WBC का क्या मतलब हो सकता है?",
                body_html="<p>हाई WBC का मतलब है कि शरीर सामान्य से ज़्यादा वाइट ब्लड सेल बना या छोड़ रहा है। ऐसा अक्सर तब होता है जब इम्यून सिस्टम एक्टिव हो—जैसे बैक्टीरियल/वायरल इन्फेक्शन, सूजन (चोट, बीमारी या क्रॉनिक कंडीशन), कुछ दवाएं, स्ट्रेस या एक्सरसाइज। तो हाई WBC एक <em>सिग्नल</em> है, निदान नहीं: यह बताता है कि कुछ इम्यूनिटी को ट्रिगर कर रहा है, पर क्या—यह नहीं बताता।</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="इन्फेक्शन बनाम इन्फ्लेमेशन",
                body_html="<p><strong>इन्फेक्शन</strong> का मतलब आम तौर पर कीटाणु (बैक्टीरिया, वायरस, फंगस या पैरासाइट) मौजूद है और इम्यून सिस्टम रिस्पॉन्ड कर रहा है। लक्षणों में बुखार, थकान या लोकल दर्द हो सकते हैं। <strong>इन्फ्लेमेशन</strong> चोट या इरिटेशन पर बॉडी का जनरल रिस्पॉन्स है—इन्फेक्शन के बिना भी (सर्जरी के बाद, ऑटोइम्यून या क्रॉनिक डिजीज)। दोनों WBC बढ़ा सकते हैं। डॉक्टर लक्षण, हिस्ट्री और कभी WBC डिफरेंशियल (जैसे न्यूट्रोफिल बनाम लिम्फोसाइट्स) और दूसरे टेस्ट से कारण सीमित करेंगे।</p>"),
        Section(id="common-causes", level=2, heading="हाई WBC के आम कारण",
                body_html="<p>आम कारण: <strong>एक्यूट इन्फेक्शन</strong> (यूरिनरी, रेस्पिरेटरी, स्किन); <strong>इन्फ्लेमेशन</strong> (सर्जरी के बाद, अर्थराइटिस या IBD); <strong>दवाएं</strong> (स्टेरॉइड या कुछ दवाएं जो बोन मैरो उत्तेजित करती हैं); <strong>स्ट्रेस या एक्सरसाइज</strong> (अस्थायी); <strong>धूम्रपान</strong>; कभी <strong>प्रेग्नेंसी</strong>। कम अक्सर ब्लड या बोन मैरो कंडीशन WBC बढ़ा सकती हैं; डॉक्टर इन्फेक्शन/इन्फ्लेमेशन से मेल न खाने पर इसे देखेंगे।</p>"),
        Section(id="temporary", level=2, heading="कब हाई WBC अस्थायी हो सकता है?",
                body_html="<p>फिजिकल स्ट्रेस, हाल की एक्सरसाइज, इमोशनल स्ट्रेस, डिहाइड्रेशन या कुछ लोगों में खाने के बाद WBC थोड़ी देर के लिए बढ़ सकता है। अगर ब्लड ड्रॉ के समय ऐसा कुछ था तो हल्का हाई रिज़ल्ट दोबारा टेस्ट में नॉर्मल आ सकता है। डॉक्टर बता सकते हैं कि दोबारा करवाना ज़रूरी है या नहीं।</p>"),
        Section(id="result-alone", level=2, heading="क्या रिज़ल्ट अकेले काफी है?",
                body_html="<p>नहीं। एक हाई WBC यह नहीं बताता कि इन्फेक्शन है, सूजन है या कुछ और—और क्लिनिकल असेसमेंट की जगह नहीं लेता। डॉक्टर इसे लक्षण, हिस्ट्री, जांच और अक्सर दूसरे टेस्ट (<a href=\"/hi/blog/what-do-low-or-high-platelets-mean\">प्लेटलेट्स</a>, <a href=\"/hi/blog/lymphocytes-high-or-low\">लिम्फोसाइट्स</a>, <a href=\"/hi/blog/monocytes-high-meaning\">मोनोसाइट्स</a>, CRP आदि) के साथ मिलाकर अगला कदम तय करेंगे।</p>"),
        Section(id="other-tests", level=2, heading="डॉक्टर और कौन से टेस्ट देख सकते हैं?",
                body_html="<p>स्थिति के हिसाब से: <strong>WBC डिफरेंशियल</strong>, <strong>CRP</strong> या दूसरे इन्फ्लेमेशन मार्कर, इन्फेक्शन शक हो तो <strong>ब्लड कल्चर</strong>, या और इमेजिंग/टेस्ट। मकसद रिज़ल्ट को आपकी क्लिनिकल तस्वीर से मिलाना है।</p>"),
        Section(id="when-to-see-doctor", level=2, heading="डॉक्टर के पास कब जाऊं?",
                body_html="<p>बुखार, बहुत थकान, बिना वजह वजन कम होना, रात को पसीना या दर्द हो—या रिपोर्ट में WBC बहुत हाई या दूसरे अबनॉर्मल काउंट हों—तो क्लिनिकल रिव्यू करवाना चाहिए। लक्षण न भी हों तो अबनॉर्मल रिज़ल्ट डॉक्टर को दिखाना और संदर्भ में समझना सही रहता है।</p>"),
        Section(id="how-norya-helps", level=2, heading="Norya यह रिज़ल्ट कैसे आसान बनाता है",
                body_html="<p>Norya पर हम निदान नहीं करते—आपको तैयारी में मदद करते हैं। आप <a href=\"/analyze\">अपनी लैब रिपोर्ट अपलोड</a> कर सकते हैं और WBC समेत सभी वैल्यू का साफ, संरचित सार पा सकते हैं—साधारण भाषा और रेफरेंस रेंज के साथ। इससे डॉक्टर से बात करना आसान हो जाता है। ऑप्शन और कीमत के लिए <a href=\"/pricing\">प्राइसिंग पेज</a> देखें।</p>"),
        Section(id="cta", level=2, heading="अगला कदम",
                body_html="<p>अगर आप अपने ब्लड टेस्ट—WBC और बाकी CBC—को साफ और ऑर्गनाइज़्ड देखना चाहते हैं तो Norya से <a href=\"/analyze\">विश्लेषण शुरू</a> कर सकते हैं। इसे अपॉइंटमेंट की तैयारी के लिए इस्तेमाल करें, मेडिकल सलाह की जगह नहीं।</p>"),
        Section(id="disclaimer", level=2, heading="अस्वीकरण",
                body_html="<p><strong>यह सामग्री केवल जानकारी के लिए है और मेडिकल सलाह या निदान की जगह नहीं लेती।</strong> हाई WBC के कई कारण हो सकते हैं; केवल वही स्वास्थ्यकर्मी जो आपकी हिस्ट्री और संदर्भ जानता है, रिज़ल्ट की सही व्याख्या कर सकता है। हमेशा लैब रिज़ल्ट डॉक्टर से चर्चा करें।</p>"),
    ]


def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(id="intro", level=2, heading="ارتفاع كريات الدم البيضاء: عدوى أم التهاب؟",
                body_html="<p>ارتفاع عدد كريات الدم البيضاء (WBC) في التقرير المخبري يطرح غالباً سؤالاً واحداً: هل هذا عدوى أم التهاب؟ الجواب يهم لراحتك وللخطوات التالية للطبيب—لكن الرقم وحده لا يروي القصة كاملة. هذا الدليل يوضح ما يقيسه WBC، وما قد يعنيه ارتفاعه، وكيف تضع النتيجة في سياقها.</p>"),
        Section(id="what-is-wbc", level=2, heading="ما هو WBC وماذا يُقاس؟",
                body_html="<p><strong>WBC</strong> (كريات الدم البيضاء أو الكريات البيض) هو العدد الكلي لكرات الدم البيضاء في حجم معين من الدم. هذه الخلايا جزء من جهازك المناعي: تساعد في مكافحة العدوى والاستجابة للالتهاب أو الجرح أو التوتر. تحليل <a href=\"/ar/blog/how-to-understand-wbc-rbc-hgb-and-hct\">عدّ الدم الكامل</a> يتضمن WBC في الغالب؛ أحياناً يعطي المختبر أيضاً التفريق (العدلات، اللمفاويات، الوحيدات، إلخ).</p>"),
        Section(id="what-high-means", level=2, heading="ماذا يمكن أن يعني ارتفاع WBC؟",
                body_html="<p>ارتفاع WBC يعني أن الجسم ينتج أو يطلق كريات بيضاء أكثر من المعتاد. يحدث ذلك غالباً عندما يُفعَّل الجهاز المناعي—بعدوى جرثومية أو فيروسية، أو التهاب (من جرح أو مرض أو حالة مزمنة)، أو أدوية معينة، أو توتر، أو جهد بدني شديد. إذن ارتفاع WBC هو <em>إشارة</em> وليس تشخيصاً: يوحي بأن شيئاً ما يفعّل المناعة، لكنه لا يحدد ماذا.</p>"),
        Section(id="infection-vs-inflammation", level=2, heading="العدوى مقابل الالتهاب",
                body_html="<p><strong>العدوى</strong> تعني عادة وجود جرثوم (بكتيريا، فيروس، فطر أو طفيلي) واستجابة مناعية. قد تظهر حمى أو تعب أو ألم موضعي. <strong>الالتهاب</strong> هو استجابة الجسم العامة للجرح أو التهيّج—قد يكون مع أو بدون عدوى (مثلاً بعد جراحة، في أمراض مناعية ذاتية أو مزمنة). كلا الحالتين قد يرفعان WBC. الطبيب يستخدم الأعراض والتاريخ وأحياناً تفريق الكريات (مثلاً العدلات مقابل اللمفاويات) وفحوص أخرى لتضييق السبب.</p>"),
        Section(id="common-causes", level=2, heading="أسباب شائعة لارتفاع WBC",
                body_html="<p>من الأسباب النموذجية: <strong>العدوى الحادة</strong> (بولية، تنفسية، جلدية)؛ <strong>الالتهاب</strong> (بعد جراحة، التهاب مفاصل، داء أمعاء التهابي)؛ <strong>أدوية</strong> (كورتيكوستيرويدات أو أدوية تحفز نقي العظم)؛ <strong>التوتر أو الجهد الشديد</strong> (مؤقت)؛ <strong>التدخين</strong>؛ أحياناً <strong>الحمل</strong>. أقل شيوعاً، أمراض الدم أو نقي العظم قد ترفع WBC؛ الطبيب يقيّم ذلك إن لم ينطبق الوصف على عدوى أو التهاب.</p>"),
        Section(id="temporary", level=2, heading="متى يمكن أن يكون الارتفاع مؤقتاً؟",
                body_html="<p>قد يرتفع WBC لفترة قصيرة مع التوتر الجسدي، تمرين حديث، توتر نفسي، جفاف، أو بعد وجبة عند بعض الناس. إن تزامن أحد ذلك مع سحب الدم، قد يعود ارتفاع خفيف إلى طبيعته في إعادة الفحص. الطبيب يحدد إن كانت إعادة الفحص ضرورية.</p>"),
        Section(id="result-alone", level=2, heading="هل النتيجة وحدها كافية؟",
                body_html="<p>لا. ارتفاع WBC منفرد لا يحدد إن كانت هناك عدوى أو التهاب أو غيره—ولا يحل محل التقييم السريري. الطبيب يجمعه مع الأعراض والتاريخ والفحص وغالباً فحوص أخرى (<a href=\"/ar/blog/what-do-low-or-high-platelets-mean\">الصفيحات</a>، <a href=\"/ar/blog/lymphocytes-high-or-low\">اللمفاويات</a>، <a href=\"/ar/blog/monocytes-high-meaning\">الوحيدات</a>، CRP، إلخ) لاتخاذ الخطوة التالية.</p>"),
        Section(id="other-tests", level=2, heading="أي فحوص إضافية قد يطلب الطبيب؟",
                body_html="<p>حسب الحالة: <strong>تفريق الكريات</strong>، <strong>CRP</strong> أو مؤشرات التهاب أخرى، <strong>مزارع الدم</strong> عند الاشتباه بعدوى، أو تصوير وفحوص أخرى. الهدف مطابقة النتائج مع الصورة السريرية.</p>"),
        Section(id="when-to-see-doctor", level=2, heading="متى أراجع الطبيب؟",
                body_html="<p>إن كان لديك حمى أو تعب شديد أو نقص وزن غير مفسر أو تعرق ليلي أو ألم—أو إن التقرير يذكر WBC مرتفعاً جداً أو أعداداً شاذة أخرى—يُنصح بتقييم سريري. حتى دون أعراض، من المفيد مناقشة أي نتيجة شاذة مع الطبيب لتفسيرها في السياق واقتراح متابعة إن لزم.</p>"),
        Section(id="how-norya-helps", level=2, heading="كيف تجعل Norya هذه النتيجة أوضح",
                body_html="<p>في Norya لا نضع التشخيص—نساعدك على التحضير. يمكنك <a href=\"/analyze\">رفع تقرير المختبر</a> والحصول على ملخص واضح منظم يشرح قيمك (بما فيها WBC) بلغة بسيطة مع نطاقات مرجعية. هكذا يسهل النقاش مع الطبيب. للخيارات والأسعار: <a href=\"/pricing\">صفحة الأسعار</a>.</p>"),
        Section(id="cta", level=2, heading="الخطوة التالية",
                body_html="<p>إن أردت رؤية تحليل دمك—بما فيه WBC وباقي عدّ الدم—بطريقة واضحة ومنظمة، يمكنك <a href=\"/analyze\">بدء تحليل</a> مع Norya. استخدمه للتحضير للموعد، وليس بديلاً عن الاستشارة الطبية.</p>"),
        Section(id="disclaimer", level=2, heading="إخلاء المسؤولية",
                body_html="<p><strong>هذا المحتوى لأغراض إعلامية فقط ولا يغني عن الاستشارة أو التشخيص الطبي.</strong> ارتفاع WBC قد يكون له أسباب كثيرة؛ فقط من يعرف سياقك يمكنه تفسيره. ناقش دائماً نتائج المختبر مع الطبيب.</p>"),
    ]


def get_high_wbc_sections_by_lang():
    """Returns sections_by_lang dict for High WBC article (all 9 languages)."""
    return {
        "tr": _sections_tr(),
        "en": _sections_en(),
        "es": _sections_es(),
        "de": _sections_de(),
        "fr": _sections_fr(),
        "it": _sections_it(),
        "he": _sections_he(),
        "hi": _sections_hi(),
        "ar": _sections_ar(),
    }


def get_high_wbc_faq_schema_qa():
    """Returns faq_schema_qa dict for High WBC article (all 9 languages)."""
    return {
        "en": [
            {"question": "What does high WBC mean?", "answer": "A high white blood cell count means your body is making or releasing more white blood cells than usual, often in response to infection, inflammation, stress, certain medications, or other triggers. It is a signal, not a diagnosis—your doctor interprets it with your symptoms and other tests."},
            {"question": "Is high WBC infection or inflammation?", "answer": "Both infection and inflammation can raise WBC. Your doctor uses your symptoms, history, and sometimes the WBC differential (e.g. neutrophils vs lymphocytes) and other tests to tell them apart."},
            {"question": "When should I worry about high white blood cells?", "answer": "Discuss any abnormal WBC with a doctor. Seek prompt review if you have fever, severe fatigue, unexplained weight loss, night sweats, or pain, or if the result is very high."},
        ],
        "tr": [
            {"question": "WBC yüksekliği ne anlama gelir?", "answer": "Beyaz küre sayısının yüksek olması, vücudunuzun enfeksiyon, iltihap, stres, bazı ilaçlar veya başka tetikleyicilere yanıt olarak normalden fazla beyaz kan hücresi ürettiği veya dolaşıma saldığı anlamına gelebilir. Bu bir sinyaldir, teşhis değildir—hekiminiz bunu belirtileriniz ve diğer testlerle yorumlar."},
            {"question": "WBC yüksekliği enfeksiyon mu iltihap mı?", "answer": "Hem enfeksiyon hem iltihap WBC’yi yükseltebilir. Hekiminiz belirtilerinizi, öykünüzü ve bazen lökosit formülünü (nötrofil/lenfosit vb.) ve diğer testleri kullanarak ayırım yapar."},
            {"question": "Yüksek beyaz küre için ne zaman endişelenmeliyim?", "answer": "Anormal WBC sonucunu mutlaka bir hekimle görüşün. Ateş, ciddi yorgunluk, açıklanamayan kilo kaybı, gece terlemesi veya ağrı varsa veya sonuç çok yüksekse zaman kaybetmeden değerlendirme yaptırın."},
        ],
        "es": [
            {"question": "¿Qué significa tener los glóbulos blancos altos?", "answer": "Un recuento alto de glóbulos blancos indica que el cuerpo produce o libera más de lo habitual, a menudo por infección, inflamación, estrés, ciertos medicamentos u otros desencadenantes. Es una señal, no un diagnóstico; el médico lo interpreta con síntomas y otras pruebas."},
            {"question": "¿Glóbulos blancos altos es infección o inflamación?", "answer": "Tanto la infección como la inflamación pueden subir los glóbulos blancos. El médico usa sus síntomas, historia y a veces la fórmula leucocitaria y otras pruebas para distinguirlas."},
            {"question": "¿Cuándo debo preocuparme por glóbulos blancos altos?", "answer": "Comente cualquier WBC anormal con un médico. Pida valoración pronto si tiene fiebre, fatiga intensa, pérdida de peso sin explicación, sudores nocturnos o dolor, o si el valor es muy alto."},
        ],
        "de": [
            {"question": "Was bedeutet ein erhöhter Leukozytenwert?", "answer": "Ein erhöhter Wert bedeutet, dass der Körper mehr weiße Blutkörperchen bildet oder freisetzt—oft bei Infektion, Entzündung, Stress, bestimmten Medikamenten oder anderen Auslösern. Es ist ein Signal, keine Diagnose; der Arzt wertet es mit Symptomen und weiteren Befunden aus."},
            {"question": "Erhöhte Leukozyten: Infektion oder Entzündung?", "answer": "Sowohl Infektion als auch Entzündung können die Leukozyten erhöhen. Der Arzt nutzt Symptome, Anamnese und oft das Differentialblutbild und weitere Tests zur Einordnung."},
            {"question": "Wann sollte ich bei hohen Leukozyten zum Arzt?", "answer": "Besprechen Sie jeden auffälligen Wert mit einem Arzt. Lassen Sie zeitnah abklären bei Fieber, starker Müdigkeit, ungewolltem Gewichtsverlust, Nachtschweiß oder Schmerzen bzw. bei sehr hohem Wert."},
        ],
        "fr": [
            {"question": "Que signifie un taux de globules blancs élevé ?", "answer": "Un taux élevé signifie que l'organisme produit ou libère plus de globules blancs que la normale, souvent en réaction à une infection, une inflammation, un stress, certains médicaments ou d'autres facteurs. C'est un signal, pas un diagnostic ; le médecin l'interprète avec les symptômes et d'autres examens."},
            {"question": "Globules blancs élevés : infection ou inflammation ?", "answer": "L'infection et l'inflammation peuvent toutes deux augmenter les globules blancs. Le médecin s'appuie sur les symptômes, l'anamnèse et parfois la formule leucocytaire et d'autres examens pour faire la part des choses."},
            {"question": "Quand s'inquiéter des globules blancs élevés ?", "answer": "Discutez de tout résultat anormal avec un médecin. Consultez sans tarder en cas de fièvre, fatigue importante, perte de poids inexpliquée, sueurs nocturnes ou douleurs, ou si le taux est très élevé."},
        ],
        "it": [
            {"question": "Cosa significa avere i globuli bianchi alti?", "answer": "Un valore alto indica che l'organismo produce o rilascia più globuli bianchi del solito, spesso in risposta a infezione, infiammazione, stress, alcuni farmaci o altri fattori. È un segnale, non una diagnosi; il medico lo interpreta con sintomi e altri esami."},
            {"question": "Globuli bianchi alti: infezione o infiammazione?", "answer": "Sia l'infezione sia l'infiammazione possono alzare i globuli bianchi. Il medico usa sintomi, anamnesi e a volte la formula leucocitaria e altri esami per distinguere."},
            {"question": "Quando preoccuparsi dei globuli bianchi alti?", "answer": "Discuti con un medico qualsiasi valore alterato. Richiedi una valutazione tempestiva in caso di febbre, forte stanchezza, perdita di peso inspiegabile, sudorazione notturna o dolore, o se il valore è molto alto."},
        ],
        "he": [
            {"question": "מה המשמעות של ספירת דם לבנים גבוהה?", "answer": "ספירה גבוהה משמעה שהגוף מייצר או משחרר יותר תאי דם לבנים מהרגיל—לעיתים בתגובה לזיהום, דלקת, מתח, תרופות מסוימות או טריגרים אחרים. זהו סימן, לא אבחנה; הרופא יפרש יחד עם התסמינים ובדיקות נוספות."},
            {"question": "לויקוציטים גבוהים – זיהום או דלקת?", "answer": "גם זיהום וגם דלקת יכולים להעלות את ספירת התאים הלבנים. הרופא משתמש בתסמינים, באנמנזה ולעיתים בנוסחת הדם ובדיקות נוספות כדי להבחין."},
            {"question": "מתי לפנות לרופא בגלל תאי דם לבנים גבוהים?", "answer": "יש לדון בכל ערך חריג עם רופא. פנה בהקדם להערכה אם יש חום, עייפות קשה, ירידה במשקל בלתי מוסברת, הזעות לילה או כאב, או אם הערך גבוה מאוד."},
        ],
        "hi": [
            {"question": "हाई WBC का क्या मतलब है?", "answer": "हाई वाइट ब्लड सेल काउंट का मतलब है कि शरीर सामान्य से ज़्यादा वाइट ब्लड सेल बना या छोड़ रहा है—अक्सर इन्फेक्शन, सूजन, तनाव, कुछ दवाएं या दूसरे ट्रिगर की वजह से। यह एक संकेत है, निदान नहीं; डॉक्टर इसे आपके लक्षणों और दूसरे टेस्ट के साथ देखेंगे।"},
            {"question": "हाई WBC इन्फेक्शन है या इन्फ्लेमेशन?", "answer": "इन्फेक्शन और इन्फ्लेमेशन दोनों WBC बढ़ा सकते हैं। डॉक्टर लक्षण, इतिहास और कभी-कभी WBC डिफरेंशियल और दूसरे टेस्ट से फर्क बताते हैं।"},
            {"question": "हाई वाइट ब्लड सेल पर कब चिंता करूं?", "answer": "किसी भी अन normal WBC को डॉक्टर से ज़रूर बताएं। बुखार, बहुत थकान, बिना वजह वजन कम होना, रात को पसीना या दर्द हो तो जल्दी चेकअप करवाएं।"},
        ],
        "ar": [
            {"question": "ماذا يعني ارتفاع عدد كريات الدم البيضاء؟", "answer": "العدد المرتفع يعني أن الجسم ينتج أو يطلق كريات بيضاء أكثر من المعتاد—غالباً استجابة لعدوى أو التهاب أو توتر أو أدوية معينة أو محفزات أخرى. إنه إشارة وليس تشخيصاً؛ الطبيب يفسره مع الأعراض والفحوص الأخرى."},
            {"question": "ارتفاع الكريات البيض: عدوى أم التهاب؟", "answer": "كل من العدوى والالتهاب قد يرفعان عدد الكريات البيضاء. الطبيب يستخدم الأعراض والتاريخ وأحياناً تفريق الكريات وفحوص أخرى للتمييز."},
            {"question": "متى أقلق من ارتفاع كريات الدم البيضاء؟", "answer": "ناقش أي نتيجة غير طبيعية مع الطبيب. اطلب تقييماً عاجلاً عند وجود حمى أو تعب شديد أو نقص وزن غير مفسر أو تعرق ليلي أو ألم، أو إذا كان الرقم مرتفعاً جداً."},
        ],
    }
