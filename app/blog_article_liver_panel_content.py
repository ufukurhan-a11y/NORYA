"""Pillar blog article: Complete Guide to Liver Function Tests — comprehensive guide.

Covers ALT, AST, ALP, GGT, Bilirubin, AST/ALT ratio, common liver conditions,
and how NoryaAI can help interpret results.

Registered in blog_i18n.py as a pillar content piece for SEO.
"""
from datetime import date
from typing import Dict, List


def _sections_en():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="What Are Liver Function Tests?",
            body_html=(
                "<p>Liver function tests (LFTs), also called a hepatic panel, are a group of blood tests that measure enzymes, proteins, and substances produced or processed by the liver. They help doctors assess liver health, detect liver damage, and monitor the progression of liver diseases.</p>"
                "<p>A standard liver panel typically includes <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>bilirubin</strong>, <strong>albumin</strong>, and <strong>total protein</strong>. Abnormal results don't always mean liver disease — medications, intense exercise, and other factors can temporarily affect these values.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (Alanine Aminotransferase)",
            body_html=(
                "<p>ALT is an enzyme found primarily in liver cells. When liver cells are damaged, ALT leaks into the bloodstream, making it one of the most specific markers for liver injury.</p>"
                "<div class='blog-definition'><strong>Normal range:</strong> 7–56 U/L (may vary by lab)</div>"
                "<p><strong>High ALT</strong> can indicate:</p>"
                "<ul>"
                "<li>Non-alcoholic fatty liver disease (NAFLD)</li>"
                "<li>Hepatitis (viral, alcoholic, or autoimmune)</li>"
                "<li>Medication-induced liver injury (e.g. acetaminophen, statins)</li>"
                "<li>Cirrhosis</li>"
                "</ul>"
                "<p><strong>Mildly elevated ALT</strong> (up to 2× the upper limit) is common and may result from obesity, certain medications, or vigorous exercise. Persistently elevated ALT warrants further investigation.</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (Aspartate Aminotransferase)",
            body_html=(
                "<p>AST is an enzyme found in the liver, heart, muscles, and kidneys. Because it's not liver-specific, AST is usually interpreted alongside ALT for a clearer picture.</p>"
                "<div class='blog-definition'><strong>Normal range:</strong> 10–40 U/L</div>"
                "<p><strong>High AST</strong> can result from:</p>"
                "<ul>"
                "<li>Liver disease (hepatitis, cirrhosis)</li>"
                "<li>Heart attack (myocardial infarction)</li>"
                "<li>Muscle damage or intense exercise</li>"
                "<li>Hemolysis (red blood cell breakdown)</li>"
                "</ul>"
                "<p>The <strong>AST/ALT ratio</strong> (De Ritis ratio) provides additional diagnostic value. A ratio &gt;2 suggests alcoholic liver disease, while a ratio &lt;1 is more typical of non-alcoholic fatty liver disease or viral hepatitis.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP and GGT — Cholestatic Markers",
            body_html=(
                "<p><strong>ALP (Alkaline Phosphatase)</strong> is an enzyme found in the liver, bile ducts, and bone. Elevated ALP can indicate bile duct obstruction, bone disorders, or liver disease.</p>"
                "<div class='blog-definition'><strong>ALP normal range:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (Gamma-Glutamyl Transferase)</strong> is an enzyme concentrated in the liver and bile ducts. It is especially sensitive to alcohol use and bile duct problems.</p>"
                "<div class='blog-definition'><strong>GGT normal range:</strong> 9–48 U/L</div>"
                "<p>When <strong>both ALP and GGT are elevated</strong>, the source is most likely hepatobiliary (liver/bile duct). If ALP is elevated but GGT is normal, the elevation is more likely from bone.</p>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="Bilirubin — Total, Direct, and Indirect",
            body_html=(
                "<p>Bilirubin is a yellow pigment produced when the body breaks down old red blood cells. The liver processes bilirubin so it can be excreted. Elevated bilirubin causes <strong>jaundice</strong> (yellowing of skin and eyes).</p>"
                "<div class='blog-definition'><strong>Total bilirubin:</strong> 0.1–1.2 mg/dL<br><strong>Direct (conjugated):</strong> 0–0.3 mg/dL<br><strong>Indirect (unconjugated):</strong> 0.1–0.8 mg/dL</div>"
                "<ul>"
                "<li><strong>High indirect bilirubin</strong>: hemolysis, Gilbert syndrome (benign), ineffective erythropoiesis</li>"
                "<li><strong>High direct bilirubin</strong>: bile duct obstruction (gallstones, tumors), hepatitis, cirrhosis</li>"
                "<li><strong>High total bilirubin</strong>: may result from either pre-hepatic, hepatic, or post-hepatic causes</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="Common Conditions Detected by Liver Tests",
            body_html=(
                "<p>Liver function tests can help identify or monitor several conditions:</p>"
                "<ul>"
                "<li><strong>Non-Alcoholic Fatty Liver Disease (NAFLD)</strong>: Mildly elevated ALT and AST with AST/ALT ratio &lt;1. Often associated with obesity and metabolic syndrome.</li>"
                "<li><strong>Hepatitis</strong>: Significantly elevated ALT and AST (often &gt;10× normal). Can be viral (A, B, C), autoimmune, or drug-induced.</li>"
                "<li><strong>Cirrhosis</strong>: Advanced scarring of the liver. AST/ALT ratio &gt;1, low albumin, elevated bilirubin, and prolonged INR are typical findings.</li>"
                "<li><strong>Gallstones / Bile duct obstruction</strong>: Markedly elevated ALP, GGT, and direct bilirubin with relatively normal ALT and AST.</li>"
                "<li><strong>Alcoholic Liver Disease</strong>: AST/ALT ratio &gt;2, elevated GGT, and elevated MCV are characteristic findings.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="When Should You See a Doctor?",
            body_html=(
                "<p>Consult your doctor promptly if:</p>"
                "<ul>"
                "<li>ALT or AST is more than <strong>3× the upper limit of normal</strong></li>"
                "<li>Bilirubin is above <strong>2.0 mg/dL</strong> with jaundice symptoms</li>"
                "<li>ALP is significantly elevated with abdominal pain</li>"
                "<li>You notice <strong>yellowing of skin or eyes</strong>, dark urine, or pale stools</li>"
                "<li>Liver enzyme abnormalities <strong>persist across multiple tests</strong></li>"
                "<li>You have risk factors such as heavy alcohol use, obesity, or chronic hepatitis</li>"
                "</ul>"
                "<p>A single mildly abnormal value is often not concerning, but patterns and trends over time carry diagnostic significance.</p>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="How NoryaAI Helps Analyze Your Liver Panel",
            body_html=(
                "<p>NoryaAI reads your liver function test results — whether from a PDF, lab printout, or photo — and automatically:</p>"
                "<ul>"
                "<li>Identifies ALT, AST, ALP, GGT, bilirubin, albumin, and total protein</li>"
                "<li>Compares each value to reference ranges adjusted for age and sex</li>"
                "<li>Calculates the AST/ALT ratio and interprets its significance</li>"
                "<li>Flags abnormal values with clear, easy-to-understand explanations</li>"
                "<li>Generates a structured, doctor-ready health summary</li>"
                "</ul>"
                "<p>Upload your blood test report and get your liver panel analysis in minutes — no manual data entry required.</p>"
            ),
        ),
    ]


def _sections_tr():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="Karaciğer Fonksiyon Testleri Nedir?",
            body_html=(
                "<p>Karaciğer fonksiyon testleri (KCFT), karaciğer tarafından üretilen veya işlenen enzimleri, proteinleri ve maddeleri ölçen bir grup kan testidir. Doktorların karaciğer sağlığını değerlendirmesine, karaciğer hasarını tespit etmesine ve karaciğer hastalıklarının seyrini izlemesine yardımcı olur.</p>"
                "<p>Standart bir karaciğer paneli genellikle <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>bilirubin</strong>, <strong>albümin</strong> ve <strong>total protein</strong> içerir. Anormal sonuçlar her zaman karaciğer hastalığı anlamına gelmez — ilaçlar, yoğun egzersiz ve diğer faktörler bu değerleri geçici olarak etkileyebilir.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (Alanin Aminotransferaz)",
            body_html=(
                "<p>ALT, esas olarak karaciğer hücrelerinde bulunan bir enzimdir. Karaciğer hücreleri hasar gördüğünde ALT kana sızar ve bu da onu karaciğer hasarı için en spesifik belirteçlerden biri yapar.</p>"
                "<div class='blog-definition'><strong>Normal aralık:</strong> 7–56 U/L (laboratuvara göre değişebilir)</div>"
                "<p><strong>Yüksek ALT</strong> nedenleri:</p>"
                "<ul>"
                "<li>Non-alkolik yağlı karaciğer hastalığı (NAYKH)</li>"
                "<li>Hepatit (viral, alkolik veya otoimmün)</li>"
                "<li>İlaca bağlı karaciğer hasarı (ör. asetaminofen, statinler)</li>"
                "<li>Siroz</li>"
                "</ul>"
                "<p><strong>Hafif yüksek ALT</strong> (üst sınırın 2 katına kadar) yaygındır ve obezite, bazı ilaçlar veya yoğun egzersizden kaynaklanabilir.</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (Aspartat Aminotransferaz)",
            body_html=(
                "<p>AST, karaciğer, kalp, kaslar ve böbreklerde bulunan bir enzimdir. Karaciğere özgü olmadığı için AST genellikle ALT ile birlikte değerlendirilir.</p>"
                "<div class='blog-definition'><strong>Normal aralık:</strong> 10–40 U/L</div>"
                "<p><strong>Yüksek AST</strong> nedenleri:</p>"
                "<ul>"
                "<li>Karaciğer hastalığı (hepatit, siroz)</li>"
                "<li>Kalp krizi (miyokard enfarktüsü)</li>"
                "<li>Kas hasarı veya yoğun egzersiz</li>"
                "<li>Hemoliz (kırmızı kan hücresi yıkımı)</li>"
                "</ul>"
                "<p><strong>AST/ALT oranı</strong> (De Ritis oranı) ek tanı değeri sağlar. Oran &gt;2 alkolik karaciğer hastalığını, oran &lt;1 ise non-alkolik yağlı karaciğer veya viral hepatiti düşündürür.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP ve GGT — Kolestatik Belirteçler",
            body_html=(
                "<p><strong>ALP (Alkalen Fosfataz)</strong>, karaciğer, safra kanalları ve kemikte bulunan bir enzimdir. Yüksek ALP safra kanalı tıkanıklığı, kemik hastalıkları veya karaciğer hastalığına işaret edebilir.</p>"
                "<div class='blog-definition'><strong>ALP normal aralık:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (Gama-Glutamil Transferaz)</strong>, karaciğer ve safra kanallarında yoğunlaşan bir enzimdir. Özellikle alkol kullanımı ve safra kanalı sorunlarına karşı hassastır.</p>"
                "<div class='blog-definition'><strong>GGT normal aralık:</strong> 9–48 U/L</div>"
                "<p><strong>Hem ALP hem GGT yüksekse</strong> kaynak büyük olasılıkla hepatobiliyer (karaciğer/safra kanalı) sistemidir. ALP yüksek ama GGT normalse yükseklik büyük olasılıkla kemik kaynaklıdır.</p>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="Bilirubin — Total, Direkt ve İndirekt",
            body_html=(
                "<p>Bilirubin, vücut eski kırmızı kan hücrelerini parçaladığında üretilen sarı bir pigmenttir. Karaciğer bilirubini işler ve atılmasını sağlar. Yüksek bilirubin <strong>sarılık</strong> (cilt ve gözlerin sararması) neden olur.</p>"
                "<div class='blog-definition'><strong>Total bilirubin:</strong> 0,1–1,2 mg/dL<br><strong>Direkt (konjuge):</strong> 0–0,3 mg/dL<br><strong>İndirekt (konjuge olmayan):</strong> 0,1–0,8 mg/dL</div>"
                "<ul>"
                "<li><strong>Yüksek indirekt bilirubin</strong>: hemoliz, Gilbert sendromu (iyi huylu), inefektif eritropoez</li>"
                "<li><strong>Yüksek direkt bilirubin</strong>: safra kanalı tıkanıklığı (safra taşları, tümörler), hepatit, siroz</li>"
                "<li><strong>Yüksek total bilirubin</strong>: pre-hepatik, hepatik veya post-hepatik nedenlerden kaynaklanabilir</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="Karaciğer Testleriyle Saptanan Yaygın Durumlar",
            body_html=(
                "<p>Karaciğer fonksiyon testleri birçok durumun tanı ve takibinde yardımcı olur:</p>"
                "<ul>"
                "<li><strong>Non-Alkolik Yağlı Karaciğer Hastalığı (NAYKH)</strong>: Hafif yüksek ALT ve AST, AST/ALT oranı &lt;1. Obezite ve metabolik sendromla ilişkilidir.</li>"
                "<li><strong>Hepatit</strong>: Belirgin yüksek ALT ve AST (genellikle normalin &gt;10 katı). Viral (A, B, C), otoimmün veya ilaca bağlı olabilir.</li>"
                "<li><strong>Siroz</strong>: Karaciğerin ileri derecede skarlaşması. AST/ALT oranı &gt;1, düşük albümin, yüksek bilirubin tipik bulgulardır.</li>"
                "<li><strong>Safra taşları / Safra kanalı tıkanıklığı</strong>: Belirgin yüksek ALP, GGT ve direkt bilirubin ile nispeten normal ALT ve AST.</li>"
                "<li><strong>Alkolik Karaciğer Hastalığı</strong>: AST/ALT oranı &gt;2, yüksek GGT ve yüksek MCV karakteristik bulgulardır.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="Ne Zaman Doktora Gitmelisiniz?",
            body_html=(
                "<p>Şu durumlarda derhal doktorunuza başvurun:</p>"
                "<ul>"
                "<li>ALT veya AST <strong>üst sınırın 3 katından</strong> fazlaysa</li>"
                "<li>Bilirubin <strong>2,0 mg/dL</strong> üzerinde ve sarılık belirtileri varsa</li>"
                "<li>ALP belirgin yüksek ve karın ağrısı varsa</li>"
                "<li><strong>Cilt veya gözlerde sararma</strong>, koyu idrar veya açık renkli dışkı fark ettiyseniz</li>"
                "<li>Karaciğer enzim anormallikleri <strong>birden fazla testte devam ediyorsa</strong></li>"
                "<li>Ağır alkol kullanımı, obezite veya kronik hepatit gibi risk faktörleriniz varsa</li>"
                "</ul>"
                "<p>Tek başına hafif bir anormal değer genellikle endişe verici değildir, ancak zaman içindeki örüntüler ve eğilimler tanısal önem taşır.</p>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="NoryaAI Karaciğer Panelinizi Nasıl Analiz Eder?",
            body_html=(
                "<p>NoryaAI, karaciğer fonksiyon test sonuçlarınızı — ister PDF, ister laboratuvar çıktısı, ister fotoğraf olsun — okur ve otomatik olarak:</p>"
                "<ul>"
                "<li>ALT, AST, ALP, GGT, bilirubin, albümin ve total proteini tanımlar</li>"
                "<li>Her değeri yaş ve cinsiyete göre ayarlanmış referans aralıklarıyla karşılaştırır</li>"
                "<li>AST/ALT oranını hesaplar ve önemini yorumlar</li>"
                "<li>Anormal değerleri anlaşılır açıklamalarla işaretler</li>"
                "<li>Yapılandırılmış, doktora hazır bir sağlık özeti oluşturur</li>"
                "</ul>"
                "<p>Kan testi raporunuzu yükleyin ve karaciğer paneli analizinizi dakikalar içinde alın — manuel veri girişi gerekmez.</p>"
            ),
        ),
    ]


def _sections_de():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="Was sind Leberfunktionstests?",
            body_html=(
                "<p>Leberfunktionstests (LFTs) sind eine Gruppe von Bluttests, die Enzyme, Proteine und Substanzen messen, die von der Leber produziert oder verarbeitet werden. Sie helfen Ärzten, die Lebergesundheit zu beurteilen, Leberschäden zu erkennen und den Verlauf von Lebererkrankungen zu überwachen.</p>"
                "<p>Ein Standard-Leberpanel umfasst typischerweise <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>Bilirubin</strong>, <strong>Albumin</strong> und <strong>Gesamtprotein</strong>. Abnorme Ergebnisse bedeuten nicht immer eine Lebererkrankung — Medikamente, intensive Bewegung und andere Faktoren können diese Werte vorübergehend beeinflussen.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (Alanin-Aminotransferase) — GPT",
            body_html=(
                "<p>ALT ist ein Enzym, das hauptsächlich in Leberzellen vorkommt. Bei Leberzellschäden gelangt ALT ins Blut und ist damit einer der spezifischsten Marker für Leberschäden.</p>"
                "<div class='blog-definition'><strong>Normalbereich:</strong> 7–56 U/L</div>"
                "<p><strong>Erhöhte ALT</strong> kann auf folgende Ursachen hinweisen:</p>"
                "<ul>"
                "<li>Nicht-alkoholische Fettlebererkrankung (NAFLD)</li>"
                "<li>Hepatitis (viral, alkoholisch oder autoimmun)</li>"
                "<li>Medikamenteninduzierte Leberschäden</li>"
                "<li>Leberzirrhose</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (Aspartat-Aminotransferase) — GOT",
            body_html=(
                "<p>AST ist ein Enzym, das in Leber, Herz, Muskeln und Nieren vorkommt. Da es nicht leberspezifisch ist, wird AST normalerweise zusammen mit ALT interpretiert.</p>"
                "<div class='blog-definition'><strong>Normalbereich:</strong> 10–40 U/L</div>"
                "<p>Das <strong>AST/ALT-Verhältnis</strong> (De-Ritis-Quotient) hat zusätzlichen diagnostischen Wert. Ein Verhältnis &gt;2 deutet auf alkoholische Lebererkrankung hin, während ein Verhältnis &lt;1 eher auf NAFLD oder virale Hepatitis hindeutet.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP und GGT — Cholestase-Marker",
            body_html=(
                "<p><strong>ALP (Alkalische Phosphatase)</strong> ist ein Enzym in Leber, Gallenwegen und Knochen. Erhöhte ALP kann auf Gallenwegsobstruktion, Knochenerkrankungen oder Lebererkrankungen hinweisen.</p>"
                "<div class='blog-definition'><strong>ALP Normalbereich:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (Gamma-Glutamyltransferase)</strong> ist ein Enzym, das in Leber und Gallenwegen konzentriert ist. Es reagiert besonders empfindlich auf Alkoholkonsum und Gallenwegs­probleme.</p>"
                "<div class='blog-definition'><strong>GGT Normalbereich:</strong> 9–48 U/L</div>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="Bilirubin — Gesamt, direkt und indirekt",
            body_html=(
                "<p>Bilirubin ist ein gelbes Pigment, das beim Abbau alter roter Blutkörperchen entsteht. Erhöhtes Bilirubin verursacht <strong>Gelbsucht</strong> (Ikterus).</p>"
                "<div class='blog-definition'><strong>Gesamtbilirubin:</strong> 0,1–1,2 mg/dL<br><strong>Direktes (konjugiertes):</strong> 0–0,3 mg/dL<br><strong>Indirektes (unkonjugiertes):</strong> 0,1–0,8 mg/dL</div>"
                "<ul>"
                "<li><strong>Hohes indirektes Bilirubin</strong>: Hämolyse, Gilbert-Syndrom, ineffektive Erythropoese</li>"
                "<li><strong>Hohes direktes Bilirubin</strong>: Gallenwegsobstruktion, Hepatitis, Zirrhose</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="Häufige durch Lebertests erkannte Erkrankungen",
            body_html=(
                "<p>Leberfunktionstests können bei der Erkennung und Überwachung verschiedener Erkrankungen helfen:</p>"
                "<ul>"
                "<li><strong>NAFLD</strong>: Leicht erhöhte ALT und AST mit AST/ALT-Verhältnis &lt;1.</li>"
                "<li><strong>Hepatitis</strong>: Deutlich erhöhte ALT und AST (oft &gt;10× normal).</li>"
                "<li><strong>Zirrhose</strong>: AST/ALT-Verhältnis &gt;1, niedriges Albumin, erhöhtes Bilirubin.</li>"
                "<li><strong>Gallensteine</strong>: Deutlich erhöhte ALP, GGT und direktes Bilirubin.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Suchen Sie umgehend einen Arzt auf, wenn:</p>"
                "<ul>"
                "<li>ALT oder AST mehr als <strong>3× den oberen Normalwert</strong> übersteigt</li>"
                "<li>Bilirubin über <strong>2,0 mg/dL</strong> liegt mit Gelbsucht-Symptomen</li>"
                "<li>Sie eine <strong>Gelbfärbung von Haut oder Augen</strong>, dunklen Urin oder hellen Stuhl bemerken</li>"
                "<li>Leberenzym-Auffälligkeiten <strong>über mehrere Tests hinweg bestehen bleiben</strong></li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="Wie NoryaAI bei Ihrer Leberanalyse hilft",
            body_html=(
                "<p>NoryaAI liest Ihre Leberfunktionstest-Ergebnisse — ob PDF, Laborausdruck oder Foto — und analysiert automatisch:</p>"
                "<ul>"
                "<li>Erkennt ALT, AST, ALP, GGT, Bilirubin, Albumin und Gesamtprotein</li>"
                "<li>Vergleicht jeden Wert mit alters- und geschlechts­spezifischen Referenzbereichen</li>"
                "<li>Berechnet das AST/ALT-Verhältnis und interpretiert seine Bedeutung</li>"
                "<li>Markiert auffällige Werte mit verständlichen Erklärungen</li>"
                "</ul>"
                "<p>Laden Sie Ihren Bluttest-Bericht hoch und erhalten Sie Ihre Leberanalyse in wenigen Minuten.</p>"
            ),
        ),
    ]


def _sections_es():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="¿Qué son las pruebas de función hepática?",
            body_html=(
                "<p>Las pruebas de función hepática (PFH) son un grupo de análisis de sangre que miden enzimas, proteínas y sustancias producidas o procesadas por el hígado. Ayudan a los médicos a evaluar la salud hepática, detectar daño hepático y monitorizar enfermedades del hígado.</p>"
                "<p>Un panel hepático estándar incluye <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>bilirrubina</strong>, <strong>albúmina</strong> y <strong>proteína total</strong>.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (Alanina Aminotransferasa)",
            body_html=(
                "<p>ALT es una enzima que se encuentra principalmente en las células hepáticas. Cuando estas se dañan, la ALT se libera al torrente sanguíneo.</p>"
                "<div class='blog-definition'><strong>Rango normal:</strong> 7–56 U/L</div>"
                "<p><strong>ALT elevada</strong> puede indicar: hígado graso no alcohólico, hepatitis, daño hepático por medicamentos o cirrosis.</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (Aspartato Aminotransferasa)",
            body_html=(
                "<p>AST es una enzima presente en el hígado, corazón, músculos y riñones. Se interpreta junto con la ALT para mayor precisión diagnóstica.</p>"
                "<div class='blog-definition'><strong>Rango normal:</strong> 10–40 U/L</div>"
                "<p>La <strong>relación AST/ALT</strong> (ratio de De Ritis) aporta valor diagnóstico adicional. Una relación &gt;2 sugiere enfermedad hepática alcohólica; &lt;1 es más típica de hígado graso no alcohólico.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP y GGT — Marcadores colestásicos",
            body_html=(
                "<p><strong>ALP (Fosfatasa Alcalina)</strong> se encuentra en el hígado, las vías biliares y los huesos.</p>"
                "<div class='blog-definition'><strong>ALP rango normal:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (Gamma-Glutamil Transferasa)</strong> es especialmente sensible al consumo de alcohol y a problemas de las vías biliares.</p>"
                "<div class='blog-definition'><strong>GGT rango normal:</strong> 9–48 U/L</div>"
                "<p>Cuando <strong>tanto ALP como GGT están elevadas</strong>, el origen es probablemente hepatobiliar.</p>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="Bilirrubina — Total, directa e indirecta",
            body_html=(
                "<p>La bilirrubina es un pigmento amarillo producido al descomponer los glóbulos rojos viejos. Los niveles elevados causan <strong>ictericia</strong>.</p>"
                "<div class='blog-definition'><strong>Bilirrubina total:</strong> 0,1–1,2 mg/dL<br><strong>Directa (conjugada):</strong> 0–0,3 mg/dL<br><strong>Indirecta (no conjugada):</strong> 0,1–0,8 mg/dL</div>"
                "<ul>"
                "<li><strong>Bilirrubina indirecta alta</strong>: hemólisis, síndrome de Gilbert</li>"
                "<li><strong>Bilirrubina directa alta</strong>: obstrucción biliar, hepatitis, cirrosis</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="Enfermedades detectadas con pruebas hepáticas",
            body_html=(
                "<ul>"
                "<li><strong>Hígado graso no alcohólico (EHGNA)</strong>: ALT y AST ligeramente elevadas, relación AST/ALT &lt;1.</li>"
                "<li><strong>Hepatitis</strong>: ALT y AST significativamente elevadas (a menudo &gt;10× lo normal).</li>"
                "<li><strong>Cirrosis</strong>: relación AST/ALT &gt;1, albúmina baja, bilirrubina elevada.</li>"
                "<li><strong>Cálculos biliares</strong>: ALP, GGT y bilirrubina directa muy elevadas.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Consulte a su médico si:</p>"
                "<ul>"
                "<li>ALT o AST superan <strong>3× el límite superior normal</strong></li>"
                "<li>La bilirrubina es superior a <strong>2,0 mg/dL</strong> con síntomas de ictericia</li>"
                "<li>Nota <strong>coloración amarillenta</strong> en piel u ojos, orina oscura o heces claras</li>"
                "<li>Las anomalías enzimáticas <strong>persisten en múltiples análisis</strong></li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="Cómo NoryaAI analiza su panel hepático",
            body_html=(
                "<p>NoryaAI lee sus resultados de función hepática — ya sea un PDF, impreso de laboratorio o foto — y automáticamente:</p>"
                "<ul>"
                "<li>Identifica ALT, AST, ALP, GGT, bilirrubina, albúmina y proteína total</li>"
                "<li>Compara cada valor con rangos de referencia ajustados por edad y sexo</li>"
                "<li>Calcula la relación AST/ALT e interpreta su significado</li>"
                "<li>Señala valores anormales con explicaciones claras</li>"
                "</ul>"
                "<p>Suba su análisis de sangre y obtenga su análisis hepático en minutos.</p>"
            ),
        ),
    ]


def _sections_fr():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="Que sont les tests hépatiques ?",
            body_html=(
                "<p>Les tests de la fonction hépatique (bilan hépatique) sont un ensemble d'analyses sanguines qui mesurent les enzymes, protéines et substances produites ou traitées par le foie. Ils aident les médecins à évaluer la santé du foie, détecter les lésions hépatiques et surveiller l'évolution des maladies du foie.</p>"
                "<p>Un bilan hépatique standard comprend généralement <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>bilirubine</strong>, <strong>albumine</strong> et <strong>protéines totales</strong>.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (Alanine Aminotransférase) — SGPT",
            body_html=(
                "<p>L'ALT est une enzyme principalement présente dans les cellules hépatiques. Lorsque le foie est endommagé, l'ALT est libérée dans le sang.</p>"
                "<div class='blog-definition'><strong>Valeurs normales :</strong> 7–56 U/L</div>"
                "<p><strong>ALT élevée</strong> peut indiquer : stéatose hépatique non alcoolique, hépatite, toxicité médicamenteuse ou cirrhose.</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (Aspartate Aminotransférase) — SGOT",
            body_html=(
                "<p>L'AST est une enzyme présente dans le foie, le cœur, les muscles et les reins. Elle est interprétée conjointement avec l'ALT.</p>"
                "<div class='blog-definition'><strong>Valeurs normales :</strong> 10–40 U/L</div>"
                "<p>Le <strong>rapport AST/ALT</strong> (rapport de De Ritis) a une valeur diagnostique. Un rapport &gt;2 évoque une hépatopathie alcoolique ; &lt;1 est plus typique d'une stéatose non alcoolique.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP et GGT — Marqueurs de cholestase",
            body_html=(
                "<p><strong>ALP (Phosphatase Alcaline)</strong> est présente dans le foie, les voies biliaires et les os.</p>"
                "<div class='blog-definition'><strong>ALP valeurs normales :</strong> 44–147 U/L</div>"
                "<p><strong>GGT (Gamma-Glutamyl Transférase)</strong> est particulièrement sensible à la consommation d'alcool et aux problèmes des voies biliaires.</p>"
                "<div class='blog-definition'><strong>GGT valeurs normales :</strong> 9–48 U/L</div>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="Bilirubine — Totale, directe et indirecte",
            body_html=(
                "<p>La bilirubine est un pigment jaune produit lors de la dégradation des globules rouges. Des taux élevés provoquent un <strong>ictère</strong> (jaunisse).</p>"
                "<div class='blog-definition'><strong>Bilirubine totale :</strong> 0,1–1,2 mg/dL<br><strong>Directe (conjuguée) :</strong> 0–0,3 mg/dL<br><strong>Indirecte (non conjuguée) :</strong> 0,1–0,8 mg/dL</div>"
                "<ul>"
                "<li><strong>Bilirubine indirecte élevée</strong> : hémolyse, syndrome de Gilbert</li>"
                "<li><strong>Bilirubine directe élevée</strong> : obstruction biliaire, hépatite, cirrhose</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="Maladies détectées par les tests hépatiques",
            body_html=(
                "<ul>"
                "<li><strong>Stéatose hépatique non alcoolique (NAFLD)</strong> : ALT et AST légèrement élevées, rapport AST/ALT &lt;1.</li>"
                "<li><strong>Hépatite</strong> : ALT et AST très élevées (souvent &gt;10× la normale).</li>"
                "<li><strong>Cirrhose</strong> : rapport AST/ALT &gt;1, albumine basse, bilirubine élevée.</li>"
                "<li><strong>Calculs biliaires</strong> : ALP, GGT et bilirubine directe nettement élevées.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez votre médecin si :</p>"
                "<ul>"
                "<li>ALT ou AST dépasse <strong>3× la limite supérieure normale</strong></li>"
                "<li>La bilirubine est supérieure à <strong>2,0 mg/dL</strong> avec des symptômes d'ictère</li>"
                "<li>Vous remarquez une <strong>coloration jaune</strong> de la peau ou des yeux</li>"
                "<li>Les anomalies hépatiques <strong>persistent sur plusieurs analyses</strong></li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="Comment NoryaAI analyse votre bilan hépatique",
            body_html=(
                "<p>NoryaAI lit vos résultats de tests hépatiques — PDF, relevé de laboratoire ou photo — et analyse automatiquement :</p>"
                "<ul>"
                "<li>Identifie ALT, AST, ALP, GGT, bilirubine, albumine et protéines totales</li>"
                "<li>Compare chaque valeur aux intervalles de référence ajustés selon l'âge et le sexe</li>"
                "<li>Calcule le rapport AST/ALT et interprète sa signification</li>"
                "<li>Signale les valeurs anormales avec des explications claires</li>"
                "</ul>"
                "<p>Téléchargez votre bilan sanguin et obtenez votre analyse hépatique en quelques minutes.</p>"
            ),
        ),
    ]


def _sections_it():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="Cosa sono i test di funzionalità epatica?",
            body_html=(
                "<p>I test di funzionalità epatica (LFT) sono un gruppo di esami del sangue che misurano enzimi, proteine e sostanze prodotte o elaborate dal fegato. Aiutano i medici a valutare la salute epatica, rilevare danni al fegato e monitorare le malattie epatiche.</p>"
                "<p>Un pannello epatico standard include tipicamente <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>bilirubina</strong>, <strong>albumina</strong> e <strong>proteine totali</strong>.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (Alanina Aminotransferasi) — GPT",
            body_html=(
                "<p>L'ALT è un enzima presente principalmente nelle cellule epatiche. Quando il fegato è danneggiato, l'ALT viene rilasciata nel sangue.</p>"
                "<div class='blog-definition'><strong>Intervallo normale:</strong> 7–56 U/L</div>"
                "<p><strong>ALT elevata</strong> può indicare: steatosi epatica non alcolica, epatite, danno epatico da farmaci o cirrosi.</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (Aspartato Aminotransferasi) — GOT",
            body_html=(
                "<p>L'AST è un enzima presente nel fegato, cuore, muscoli e reni. Viene interpretata insieme all'ALT per un quadro più chiaro.</p>"
                "<div class='blog-definition'><strong>Intervallo normale:</strong> 10–40 U/L</div>"
                "<p>Il <strong>rapporto AST/ALT</strong> (rapporto di De Ritis) fornisce valore diagnostico aggiuntivo. Un rapporto &gt;2 suggerisce epatopatia alcolica; &lt;1 è più tipico della steatosi non alcolica.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP e GGT — Marcatori colestatici",
            body_html=(
                "<p><strong>ALP (Fosfatasi Alcalina)</strong> si trova nel fegato, nelle vie biliari e nelle ossa.</p>"
                "<div class='blog-definition'><strong>ALP intervallo normale:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (Gamma-Glutamil Transferasi)</strong> è particolarmente sensibile al consumo di alcol e ai problemi delle vie biliari.</p>"
                "<div class='blog-definition'><strong>GGT intervallo normale:</strong> 9–48 U/L</div>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="Bilirubina — Totale, diretta e indiretta",
            body_html=(
                "<p>La bilirubina è un pigmento giallo prodotto dalla degradazione dei globuli rossi vecchi. Livelli elevati causano <strong>ittero</strong>.</p>"
                "<div class='blog-definition'><strong>Bilirubina totale:</strong> 0,1–1,2 mg/dL<br><strong>Diretta (coniugata):</strong> 0–0,3 mg/dL<br><strong>Indiretta (non coniugata):</strong> 0,1–0,8 mg/dL</div>"
                "<ul>"
                "<li><strong>Bilirubina indiretta elevata</strong>: emolisi, sindrome di Gilbert</li>"
                "<li><strong>Bilirubina diretta elevata</strong>: ostruzione biliare, epatite, cirrosi</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="Condizioni rilevate dai test epatici",
            body_html=(
                "<ul>"
                "<li><strong>Steatosi epatica non alcolica (NAFLD)</strong>: ALT e AST lievemente elevate, rapporto AST/ALT &lt;1.</li>"
                "<li><strong>Epatite</strong>: ALT e AST significativamente elevate (spesso &gt;10× il normale).</li>"
                "<li><strong>Cirrosi</strong>: rapporto AST/ALT &gt;1, albumina bassa, bilirubina elevata.</li>"
                "<li><strong>Calcoli biliari</strong>: ALP, GGT e bilirubina diretta marcatamente elevate.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="Quando consultare un medico?",
            body_html=(
                "<p>Consulti il medico se:</p>"
                "<ul>"
                "<li>ALT o AST superano <strong>3× il limite superiore normale</strong></li>"
                "<li>La bilirubina è superiore a <strong>2,0 mg/dL</strong> con sintomi di ittero</li>"
                "<li>Nota <strong>colorazione gialla</strong> di pelle o occhi, urine scure o feci chiare</li>"
                "<li>Le anomalie enzimatiche <strong>persistono in più esami</strong></li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="Come NoryaAI analizza il pannello epatico",
            body_html=(
                "<p>NoryaAI legge i risultati dei test epatici — PDF, referto di laboratorio o foto — e automaticamente:</p>"
                "<ul>"
                "<li>Identifica ALT, AST, ALP, GGT, bilirubina, albumina e proteine totali</li>"
                "<li>Confronta ogni valore con gli intervalli di riferimento per età e sesso</li>"
                "<li>Calcola il rapporto AST/ALT e ne interpreta il significato</li>"
                "<li>Segnala i valori anomali con spiegazioni chiare</li>"
                "</ul>"
                "<p>Carichi il suo referto ematico e ottenga l'analisi epatica in pochi minuti.</p>"
            ),
        ),
    ]


def _sections_he():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="מהן בדיקות תפקודי כבד?",
            body_html=(
                "<p>בדיקות תפקודי כבד (LFTs) הן קבוצה של בדיקות דם המודדות אנזימים, חלבונים וחומרים המיוצרים או מעובדים על ידי הכבד. הן עוזרות לרופאים להעריך את בריאות הכבד, לזהות נזק לכבד ולעקוב אחר מחלות כבד.</p>"
                "<p>פאנל כבד סטנדרטי כולל בדרך כלל <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>בילירובין</strong>, <strong>אלבומין</strong> ו<strong>חלבון כולל</strong>.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (אלנין אמינוטרנספראז)",
            body_html=(
                "<p>ALT הוא אנזים הנמצא בעיקר בתאי הכבד. כאשר תאי הכבד נפגעים, ALT משתחרר לזרם הדם.</p>"
                "<div class='blog-definition'><strong>טווח תקין:</strong> 7–56 U/L</div>"
                "<p><strong>ALT גבוה</strong> עשוי להצביע על: כבד שומני לא אלכוהולי, דלקת כבד, נזק לכבד מתרופות או שחמת.</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (אספרטאט אמינוטרנספראז)",
            body_html=(
                "<p>AST הוא אנזים הנמצא בכבד, בלב, בשרירים ובכליות. מכיוון שאינו ספציפי לכבד, הוא מפורש יחד עם ALT.</p>"
                "<div class='blog-definition'><strong>טווח תקין:</strong> 10–40 U/L</div>"
                "<p><strong>יחס AST/ALT</strong> (יחס דה ריטיס) מספק ערך אבחנתי נוסף. יחס &gt;2 מרמז על מחלת כבד אלכוהולית; &lt;1 אופייני יותר לכבד שומני לא אלכוהולי.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP ו-GGT — סמני כולסטזיס",
            body_html=(
                "<p><strong>ALP (פוספטאז אלקליין)</strong> נמצא בכבד, בדרכי המרה ובעצמות.</p>"
                "<div class='blog-definition'><strong>ALP טווח תקין:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (גמא-גלוטמיל טרנספראז)</strong> רגיש במיוחד לצריכת אלכוהול ובעיות בדרכי המרה.</p>"
                "<div class='blog-definition'><strong>GGT טווח תקין:</strong> 9–48 U/L</div>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="בילירובין — כולל, ישיר ועקיף",
            body_html=(
                "<p>בילירובין הוא פיגמנט צהוב המיוצר בפירוק תאי דם אדומים ישנים. רמות גבוהות גורמות ל<strong>צהבת</strong>.</p>"
                "<div class='blog-definition'><strong>בילירובין כולל:</strong> 0.1–1.2 mg/dL<br><strong>ישיר (מצומד):</strong> 0–0.3 mg/dL<br><strong>עקיף (לא מצומד):</strong> 0.1–0.8 mg/dL</div>"
                "<ul>"
                "<li><strong>בילירובין עקיף גבוה</strong>: המוליזה, תסמונת גילברט</li>"
                "<li><strong>בילירובין ישיר גבוה</strong>: חסימת דרכי מרה, דלקת כבד, שחמת</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="מצבים שכיחים המתגלים בבדיקות כבד",
            body_html=(
                "<ul>"
                "<li><strong>כבד שומני לא אלכוהולי (NAFLD)</strong>: ALT ו-AST מוגברים קלות, יחס AST/ALT &lt;1.</li>"
                "<li><strong>דלקת כבד (הפטיטיס)</strong>: ALT ו-AST מוגברים משמעותית (לעיתים &gt;10× הנורמה).</li>"
                "<li><strong>שחמת</strong>: יחס AST/ALT &gt;1, אלבומין נמוך, בילירובין מוגבר.</li>"
                "<li><strong>אבני מרה</strong>: ALP, GGT ובילירובין ישיר מוגברים בולטות.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>פנו לרופא אם:</p>"
                "<ul>"
                "<li>ALT או AST גבוהים <strong>פי 3 מהגבול העליון של הנורמה</strong></li>"
                "<li>בילירובין מעל <strong>2.0 mg/dL</strong> עם תסמיני צהבת</li>"
                "<li>אתם מבחינים ב<strong>הצהבה של העור או העיניים</strong></li>"
                "<li>חריגות באנזימי כבד <strong>נמשכות לאורך מספר בדיקות</strong></li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="איך NoryaAI עוזר בניתוח פאנל הכבד שלכם",
            body_html=(
                "<p>NoryaAI קורא את תוצאות בדיקות הכבד שלכם — PDF, דוח מעבדה או צילום — ומנתח אוטומטית:</p>"
                "<ul>"
                "<li>מזהה ALT, AST, ALP, GGT, בילירובין, אלבומין וחלבון כולל</li>"
                "<li>משווה כל ערך לטווחי ייחוס מותאמי גיל ומין</li>"
                "<li>מחשב את יחס AST/ALT ומפרש את משמעותו</li>"
                "<li>מסמן ערכים חריגים עם הסברים ברורים</li>"
                "</ul>"
                "<p>העלו את דוח בדיקת הדם שלכם וקבלו את ניתוח הכבד שלכם תוך דקות.</p>"
            ),
        ),
    ]


def _sections_hi():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="लिवर फंक्शन टेस्ट क्या हैं?",
            body_html=(
                "<p>लिवर फंक्शन टेस्ट (LFTs) रक्त परीक्षणों का एक समूह है जो लिवर द्वारा उत्पादित या संसाधित एंजाइम, प्रोटीन और पदार्थों को मापता है। ये डॉक्टरों को लिवर के स्वास्थ्य का आकलन करने, लिवर की क्षति का पता लगाने और लिवर रोगों की प्रगति की निगरानी करने में मदद करते हैं।</p>"
                "<p>एक मानक लिवर पैनल में आमतौर पर <strong>ALT</strong>, <strong>AST</strong>, <strong>ALP</strong>, <strong>GGT</strong>, <strong>बिलीरुबिन</strong>, <strong>एल्ब्यूमिन</strong> और <strong>कुल प्रोटीन</strong> शामिल होते हैं।</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (एलानिन एमिनोट्रांसफेरेज़)",
            body_html=(
                "<p>ALT एक एंजाइम है जो मुख्य रूप से लिवर कोशिकाओं में पाया जाता है। जब लिवर कोशिकाएं क्षतिग्रस्त होती हैं, तो ALT रक्तप्रवाह में लीक हो जाता है।</p>"
                "<div class='blog-definition'><strong>सामान्य सीमा:</strong> 7–56 U/L</div>"
                "<p><strong>उच्च ALT</strong> के कारण: नॉन-अल्कोहलिक फैटी लिवर डिज़ीज़, हेपेटाइटिस, दवा से लिवर की क्षति या सिरोसिस।</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (एस्पार्टेट एमिनोट्रांसफेरेज़)",
            body_html=(
                "<p>AST एक एंजाइम है जो लिवर, हृदय, मांसपेशियों और गुर्दों में पाया जाता है। यह लिवर-विशिष्ट नहीं है, इसलिए इसे ALT के साथ मिलाकर देखा जाता है।</p>"
                "<div class='blog-definition'><strong>सामान्य सीमा:</strong> 10–40 U/L</div>"
                "<p><strong>AST/ALT अनुपात</strong> (डी रिटिस अनुपात) अतिरिक्त नैदानिक मूल्य प्रदान करता है। अनुपात &gt;2 अल्कोहलिक लिवर डिज़ीज़ का सुझाव देता है; &lt;1 नॉन-अल्कोहलिक फैटी लिवर के लिए अधिक विशिष्ट है।</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP और GGT — कोलेस्टेटिक मार्कर",
            body_html=(
                "<p><strong>ALP (एल्कलाइन फॉस्फेटेज़)</strong> लिवर, पित्त नलिकाओं और हड्डियों में पाया जाता है।</p>"
                "<div class='blog-definition'><strong>ALP सामान्य सीमा:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (गामा-ग्लूटामिल ट्रांसफरेज़)</strong> शराब के सेवन और पित्त नली की समस्याओं के प्रति विशेष रूप से संवेदनशील है।</p>"
                "<div class='blog-definition'><strong>GGT सामान्य सीमा:</strong> 9–48 U/L</div>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="बिलीरुबिन — कुल, प्रत्यक्ष और अप्रत्यक्ष",
            body_html=(
                "<p>बिलीरुबिन एक पीला पिगमेंट है जो पुरानी लाल रक्त कोशिकाओं के टूटने पर बनता है। उच्च बिलीरुबिन <strong>पीलिया</strong> (त्वचा और आंखों का पीला होना) का कारण बनता है।</p>"
                "<div class='blog-definition'><strong>कुल बिलीरुबिन:</strong> 0.1–1.2 mg/dL<br><strong>प्रत्यक्ष (संयुग्मित):</strong> 0–0.3 mg/dL<br><strong>अप्रत्यक्ष (असंयुग्मित):</strong> 0.1–0.8 mg/dL</div>"
                "<ul>"
                "<li><strong>उच्च अप्रत्यक्ष बिलीरुबिन</strong>: हेमोलिसिस, गिल्बर्ट सिंड्रोम</li>"
                "<li><strong>उच्च प्रत्यक्ष बिलीरुबिन</strong>: पित्त नली में रुकावट, हेपेटाइटिस, सिरोसिस</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="लिवर टेस्ट से पता चलने वाली सामान्य स्थितियां",
            body_html=(
                "<ul>"
                "<li><strong>नॉन-अल्कोहलिक फैटी लिवर डिज़ीज़ (NAFLD)</strong>: हल्का उच्च ALT और AST, AST/ALT अनुपात &lt;1।</li>"
                "<li><strong>हेपेटाइटिस</strong>: ALT और AST काफी ऊंचे (अक्सर सामान्य से &gt;10 गुना)।</li>"
                "<li><strong>सिरोसिस</strong>: AST/ALT अनुपात &gt;1, कम एल्ब्यूमिन, उच्च बिलीरुबिन।</li>"
                "<li><strong>पित्त पथरी</strong>: ALP, GGT और प्रत्यक्ष बिलीरुबिन स्पष्ट रूप से ऊंचे।</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>अपने डॉक्टर से संपर्क करें यदि:</p>"
                "<ul>"
                "<li>ALT या AST <strong>सामान्य ऊपरी सीमा से 3 गुना</strong> से अधिक है</li>"
                "<li>बिलीरुबिन <strong>2.0 mg/dL</strong> से ऊपर है और पीलिया के लक्षण हैं</li>"
                "<li>आप <strong>त्वचा या आंखों का पीलापन</strong>, गहरे रंग का मूत्र या हल्के रंग का मल देख रहे हैं</li>"
                "<li>लिवर एंजाइम की असामान्यताएं <strong>कई परीक्षणों में बनी हुई हैं</strong></li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="NoryaAI आपके लिवर पैनल का विश्लेषण कैसे करता है",
            body_html=(
                "<p>NoryaAI आपके लिवर फंक्शन टेस्ट के परिणामों को पढ़ता है — चाहे PDF हो, लैब प्रिंटआउट हो या फोटो — और स्वचालित रूप से:</p>"
                "<ul>"
                "<li>ALT, AST, ALP, GGT, बिलीरुबिन, एल्ब्यूमिन और कुल प्रोटीन की पहचान करता है</li>"
                "<li>प्रत्येक मान की तुलना उम्र और लिंग-विशिष्ट संदर्भ सीमाओं से करता है</li>"
                "<li>AST/ALT अनुपात की गणना करता है और इसके महत्व की व्याख्या करता है</li>"
                "<li>असामान्य मानों को स्पष्ट व्याख्याओं के साथ चिह्नित करता है</li>"
                "</ul>"
                "<p>अपनी रक्त रिपोर्ट अपलोड करें और मिनटों में अपना लिवर पैनल विश्लेषण प्राप्त करें।</p>"
            ),
        ),
    ]


def _sections_ar():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-what-are-lfts", level=2,
            heading="ما هي اختبارات وظائف الكبد؟",
            body_html=(
                "<p>اختبارات وظائف الكبد (LFTs) هي مجموعة من تحاليل الدم التي تقيس الإنزيمات والبروتينات والمواد التي ينتجها أو يعالجها الكبد. تساعد الأطباء في تقييم صحة الكبد واكتشاف تلف الكبد ومراقبة أمراض الكبد.</p>"
                "<p>يشمل فحص الكبد القياسي عادةً <strong>ALT</strong> و<strong>AST</strong> و<strong>ALP</strong> و<strong>GGT</strong> و<strong>البيليروبين</strong> و<strong>الألبومين</strong> و<strong>البروتين الكلي</strong>.</p>"
            ),
        ),
        Section(
            id="section-alt", level=2,
            heading="ALT (ألانين أمينوترانسفيراز)",
            body_html=(
                "<p>ALT هو إنزيم يوجد بشكل رئيسي في خلايا الكبد. عندما تتضرر خلايا الكبد، يتسرب ALT إلى مجرى الدم.</p>"
                "<div class='blog-definition'><strong>المعدل الطبيعي:</strong> 7–56 U/L</div>"
                "<p><strong>ارتفاع ALT</strong> قد يشير إلى: مرض الكبد الدهني غير الكحولي، التهاب الكبد، تلف الكبد بسبب الأدوية أو تليف الكبد.</p>"
            ),
        ),
        Section(
            id="section-ast", level=2,
            heading="AST (أسبارتات أمينوترانسفيراز)",
            body_html=(
                "<p>AST هو إنزيم موجود في الكبد والقلب والعضلات والكلى. نظرًا لأنه غير مخصص للكبد، يتم تفسيره مع ALT.</p>"
                "<div class='blog-definition'><strong>المعدل الطبيعي:</strong> 10–40 U/L</div>"
                "<p><strong>نسبة AST/ALT</strong> (نسبة دي ريتيس) توفر قيمة تشخيصية إضافية. نسبة &gt;2 تشير إلى مرض الكبد الكحولي؛ &lt;1 أكثر شيوعًا في الكبد الدهني غير الكحولي.</p>"
            ),
        ),
        Section(
            id="section-alp-ggt", level=2,
            heading="ALP و GGT — مؤشرات الركود الصفراوي",
            body_html=(
                "<p><strong>ALP (الفوسفاتاز القلوي)</strong> يوجد في الكبد والقنوات الصفراوية والعظام.</p>"
                "<div class='blog-definition'><strong>ALP المعدل الطبيعي:</strong> 44–147 U/L</div>"
                "<p><strong>GGT (غاما غلوتاميل ترانسفيراز)</strong> حساس بشكل خاص لاستهلاك الكحول ومشاكل القنوات الصفراوية.</p>"
                "<div class='blog-definition'><strong>GGT المعدل الطبيعي:</strong> 9–48 U/L</div>"
            ),
        ),
        Section(
            id="section-bilirubin", level=2,
            heading="البيليروبين — الكلي والمباشر وغير المباشر",
            body_html=(
                "<p>البيليروبين هو صبغة صفراء تنتج عند تحلل خلايا الدم الحمراء القديمة. المستويات المرتفعة تسبب <strong>اليرقان</strong> (اصفرار الجلد والعينين).</p>"
                "<div class='blog-definition'><strong>البيليروبين الكلي:</strong> 0.1–1.2 mg/dL<br><strong>المباشر (المقترن):</strong> 0–0.3 mg/dL<br><strong>غير المباشر (غير المقترن):</strong> 0.1–0.8 mg/dL</div>"
                "<ul>"
                "<li><strong>ارتفاع البيليروبين غير المباشر</strong>: انحلال الدم، متلازمة جيلبرت</li>"
                "<li><strong>ارتفاع البيليروبين المباشر</strong>: انسداد القنوات الصفراوية، التهاب الكبد، تليف الكبد</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-common-conditions", level=2,
            heading="الحالات الشائعة التي تكشفها اختبارات الكبد",
            body_html=(
                "<ul>"
                "<li><strong>مرض الكبد الدهني غير الكحولي (NAFLD)</strong>: ارتفاع طفيف في ALT وAST، نسبة AST/ALT &lt;1.</li>"
                "<li><strong>التهاب الكبد</strong>: ارتفاع كبير في ALT وAST (غالبًا &gt;10× الطبيعي).</li>"
                "<li><strong>تليف الكبد</strong>: نسبة AST/ALT &gt;1، ألبومين منخفض، بيليروبين مرتفع.</li>"
                "<li><strong>حصوات المرارة</strong>: ارتفاع ملحوظ في ALP وGGT والبيليروبين المباشر.</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>راجع طبيبك إذا:</p>"
                "<ul>"
                "<li>كان ALT أو AST أعلى من <strong>3 أضعاف الحد الأعلى الطبيعي</strong></li>"
                "<li>كان البيليروبين أعلى من <strong>2.0 mg/dL</strong> مع أعراض اليرقان</li>"
                "<li>لاحظت <strong>اصفرار الجلد أو العينين</strong> أو بول داكن أو براز فاتح اللون</li>"
                "<li><strong>استمرت</strong> اضطرابات إنزيمات الكبد عبر عدة فحوصات</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-norya-liver", level=2,
            heading="كيف يساعد NoryaAI في تحليل فحص الكبد",
            body_html=(
                "<p>يقرأ NoryaAI نتائج اختبارات وظائف الكبد — سواء كانت PDF أو مطبوعة من المختبر أو صورة — ويحلل تلقائيًا:</p>"
                "<ul>"
                "<li>يحدد ALT وAST وALP وGGT والبيليروبين والألبومين والبروتين الكلي</li>"
                "<li>يقارن كل قيمة بالنطاقات المرجعية المعدلة حسب العمر والجنس</li>"
                "<li>يحسب نسبة AST/ALT ويفسر أهميتها</li>"
                "<li>يحدد القيم غير الطبيعية مع شروحات واضحة</li>"
                "</ul>"
                "<p>ارفع تقرير فحص الدم الخاص بك واحصل على تحليل الكبد في دقائق.</p>"
            ),
        ),
    ]


def get_liver_panel_sections_by_lang() -> dict:
    return {
        "en": _sections_en(),
        "tr": _sections_tr(),
        "de": _sections_de(),
        "es": _sections_es(),
        "fr": _sections_fr(),
        "it": _sections_it(),
        "he": _sections_he(),
        "hi": _sections_hi(),
        "ar": _sections_ar(),
    }


def get_liver_panel_faq_schema_qa() -> dict:
    return {
        "en": [
            {"question": "What do liver function tests measure?",
             "answer": "Liver function tests measure enzymes (ALT, AST, ALP, GGT), bilirubin, albumin, and total protein to assess liver health, detect liver damage, and monitor liver diseases."},
            {"question": "What is a normal ALT level?",
             "answer": "A normal ALT level is typically 7–56 U/L. Mildly elevated ALT (up to 2× the upper limit) can result from obesity, medications, or intense exercise."},
            {"question": "What does the AST/ALT ratio mean?",
             "answer": "The AST/ALT ratio (De Ritis ratio) helps differentiate liver conditions. A ratio greater than 2 suggests alcoholic liver disease, while a ratio less than 1 is more typical of non-alcoholic fatty liver disease."},
            {"question": "What causes high bilirubin?",
             "answer": "High bilirubin can be caused by liver disease (hepatitis, cirrhosis), bile duct obstruction (gallstones), hemolysis (red blood cell breakdown), or benign conditions like Gilbert syndrome."},
        ],
        "tr": [
            {"question": "Karaciğer fonksiyon testleri neyi ölçer?",
             "answer": "Karaciğer fonksiyon testleri, karaciğer sağlığını değerlendirmek için enzimleri (ALT, AST, ALP, GGT), bilirubin, albümin ve total proteini ölçer."},
            {"question": "Normal ALT seviyesi nedir?",
             "answer": "Normal ALT seviyesi genellikle 7–56 U/L'dir. Hafif yüksek ALT (üst sınırın 2 katına kadar) obezite, ilaçlar veya yoğun egzersizden kaynaklanabilir."},
            {"question": "AST/ALT oranı ne anlama gelir?",
             "answer": "AST/ALT oranı (De Ritis oranı) karaciğer hastalıklarını ayırt etmeye yardımcı olur. 2'den büyük oran alkolik karaciğer hastalığını, 1'den küçük oran non-alkolik yağlı karaciğeri düşündürür."},
            {"question": "Yüksek bilirubin nedenleri nelerdir?",
             "answer": "Yüksek bilirubin karaciğer hastalığı (hepatit, siroz), safra kanalı tıkanıklığı (safra taşları), hemoliz veya Gilbert sendromu gibi iyi huylu durumlardan kaynaklanabilir."},
        ],
        "de": [
            {"question": "Was messen Leberfunktionstests?",
             "answer": "Leberfunktionstests messen Enzyme (ALT, AST, ALP, GGT), Bilirubin, Albumin und Gesamtprotein zur Beurteilung der Lebergesundheit."},
            {"question": "Was ist ein normaler ALT-Wert?",
             "answer": "Ein normaler ALT-Wert liegt typischerweise bei 7–56 U/L. Leicht erhöhte ALT-Werte können durch Übergewicht, Medikamente oder intensives Training verursacht werden."},
            {"question": "Was bedeutet das AST/ALT-Verhältnis?",
             "answer": "Das AST/ALT-Verhältnis (De-Ritis-Quotient) hilft bei der Differenzierung von Lebererkrankungen. Ein Verhältnis über 2 deutet auf alkoholische Lebererkrankung hin."},
            {"question": "Was verursacht erhöhtes Bilirubin?",
             "answer": "Erhöhtes Bilirubin kann durch Lebererkrankung, Gallenwegsobstruktion, Hämolyse oder gutartige Zustände wie das Gilbert-Syndrom verursacht werden."},
        ],
        "es": [
            {"question": "¿Qué miden las pruebas de función hepática?",
             "answer": "Las pruebas de función hepática miden enzimas (ALT, AST, ALP, GGT), bilirrubina, albúmina y proteína total para evaluar la salud del hígado."},
            {"question": "¿Cuál es el nivel normal de ALT?",
             "answer": "Un nivel normal de ALT es típicamente 7–56 U/L. La ALT ligeramente elevada puede ser causada por obesidad, medicamentos o ejercicio intenso."},
            {"question": "¿Qué significa la relación AST/ALT?",
             "answer": "La relación AST/ALT (ratio de De Ritis) ayuda a diferenciar enfermedades hepáticas. Una relación mayor a 2 sugiere enfermedad hepática alcohólica."},
            {"question": "¿Qué causa la bilirrubina alta?",
             "answer": "La bilirrubina alta puede ser causada por enfermedad hepática, obstrucción biliar, hemólisis o condiciones benignas como el síndrome de Gilbert."},
        ],
        "fr": [
            {"question": "Que mesurent les tests hépatiques ?",
             "answer": "Les tests hépatiques mesurent les enzymes (ALT, AST, ALP, GGT), la bilirubine, l'albumine et les protéines totales pour évaluer la santé du foie."},
            {"question": "Quel est le niveau normal d'ALT ?",
             "answer": "Un niveau normal d'ALT est typiquement de 7–56 U/L. Une ALT légèrement élevée peut résulter de l'obésité, de médicaments ou d'un exercice intense."},
            {"question": "Que signifie le rapport AST/ALT ?",
             "answer": "Le rapport AST/ALT (rapport de De Ritis) aide à différencier les maladies du foie. Un rapport supérieur à 2 évoque une hépatopathie alcoolique."},
            {"question": "Qu'est-ce qui cause une bilirubine élevée ?",
             "answer": "Une bilirubine élevée peut être causée par une maladie du foie, une obstruction biliaire, une hémolyse ou des conditions bénignes comme le syndrome de Gilbert."},
        ],
        "it": [
            {"question": "Cosa misurano i test di funzionalità epatica?",
             "answer": "I test di funzionalità epatica misurano gli enzimi (ALT, AST, ALP, GGT), la bilirubina, l'albumina e le proteine totali per valutare la salute del fegato."},
            {"question": "Qual è il livello normale di ALT?",
             "answer": "Un livello normale di ALT è tipicamente 7–56 U/L. Un'ALT leggermente elevata può essere causata da obesità, farmaci o esercizio intenso."},
            {"question": "Cosa significa il rapporto AST/ALT?",
             "answer": "Il rapporto AST/ALT (rapporto di De Ritis) aiuta a differenziare le malattie epatiche. Un rapporto superiore a 2 suggerisce epatopatia alcolica."},
            {"question": "Cosa causa la bilirubina alta?",
             "answer": "La bilirubina alta può essere causata da malattia epatica, ostruzione biliare, emolisi o condizioni benigne come la sindrome di Gilbert."},
        ],
        "he": [
            {"question": "מה מודדות בדיקות תפקודי כבד?",
             "answer": "בדיקות תפקודי כבד מודדות אנזימים (ALT, AST, ALP, GGT), בילירובין, אלבומין וחלבון כולל כדי להעריך את בריאות הכבד."},
            {"question": "מהי רמת ALT תקינה?",
             "answer": "רמת ALT תקינה היא בדרך כלל 7–56 U/L. ALT מוגבר קלות עשוי לנבוע מהשמנה, תרופות או פעילות גופנית אינטנסיבית."},
            {"question": "מה משמעות יחס AST/ALT?",
             "answer": "יחס AST/ALT (יחס דה ריטיס) מסייע להבדיל בין מחלות כבד. יחס מעל 2 מרמז על מחלת כבד אלכוהולית."},
            {"question": "מה גורם לבילירובין גבוה?",
             "answer": "בילירובין גבוה יכול להיגרם ממחלת כבד, חסימת דרכי מרה, המוליזה או מצבים שפירים כמו תסמונת גילברט."},
        ],
        "hi": [
            {"question": "लिवर फंक्शन टेस्ट क्या मापते हैं?",
             "answer": "लिवर फंक्शन टेस्ट एंजाइम (ALT, AST, ALP, GGT), बिलीरुबिन, एल्ब्यूमिन और कुल प्रोटीन को मापते हैं ताकि लिवर के स्वास्थ्य का आकलन किया जा सके।"},
            {"question": "सामान्य ALT स्तर क्या है?",
             "answer": "सामान्य ALT स्तर आमतौर पर 7–56 U/L होता है। हल्का ऊंचा ALT मोटापे, दवाओं या तीव्र व्यायाम के कारण हो सकता है।"},
            {"question": "AST/ALT अनुपात का क्या मतलब है?",
             "answer": "AST/ALT अनुपात (डी रिटिस अनुपात) लिवर रोगों को विभेदित करने में मदद करता है। 2 से अधिक अनुपात अल्कोहलिक लिवर डिज़ीज़ का सुझाव देता है।"},
            {"question": "उच्च बिलीरुबिन का कारण क्या है?",
             "answer": "उच्च बिलीरुबिन लिवर रोग, पित्त नली में रुकावट, हेमोलिसिस या गिल्बर्ट सिंड्रोम जैसी सौम्य स्थितियों के कारण हो सकता है।"},
        ],
        "ar": [
            {"question": "ماذا تقيس اختبارات وظائف الكبد؟",
             "answer": "تقيس اختبارات وظائف الكبد الإنزيمات (ALT، AST، ALP، GGT) والبيليروبين والألبومين والبروتين الكلي لتقييم صحة الكبد."},
            {"question": "ما هو المستوى الطبيعي لـ ALT؟",
             "answer": "المستوى الطبيعي لـ ALT عادة 7–56 U/L. قد ينتج ارتفاع ALT الطفيف عن السمنة أو الأدوية أو التمارين المكثفة."},
            {"question": "ماذا تعني نسبة AST/ALT؟",
             "answer": "نسبة AST/ALT (نسبة دي ريتيس) تساعد في التمييز بين أمراض الكبد. نسبة أكبر من 2 تشير إلى مرض الكبد الكحولي."},
            {"question": "ما الذي يسبب ارتفاع البيليروبين؟",
             "answer": "يمكن أن يحدث ارتفاع البيليروبين بسبب أمراض الكبد أو انسداد القنوات الصفراوية أو انحلال الدم أو حالات حميدة مثل متلازمة جيلبرت."},
        ],
    }


def build_liver_panel_article():
    """Build the Liver Function Tests Pillar Article. Called from blog_i18n.py."""
    from app.blog_i18n import Article, Section
    published = date(2026, 3, 25)
    cover = "/static/images/blog/ggt-high-hero.png"
    slugs = {
        "en": "liver-function-tests-guide",
        "tr": "karaciger-fonksiyon-testleri-rehberi",
        "de": "leberfunktionstest-leitfaden",
        "es": "guia-pruebas-hepaticas",
        "fr": "guide-tests-hepatiques",
        "it": "guida-test-epatici",
        "he": "liver-function-tests-guide",
        "hi": "liver-function-tests-guide",
        "ar": "liver-function-tests-guide",
    }
    cat = {
        "tr": "Karaciğer",
        "en": "Liver",
        "de": "Leber",
        "es": "Hígado",
        "fr": "Foie",
        "it": "Fegato",
        "he": "כבד",
        "hi": "लिवर",
        "ar": "الكبد",
    }
    titles = {
        "en": "Complete Guide to Liver Function Tests",
        "tr": "Karaciğer Fonksiyon Testleri Rehberi",
        "de": "Leberfunktionstests — Der vollständige Leitfaden",
        "es": "Guía completa de pruebas de función hepática",
        "fr": "Guide complet des tests hépatiques",
        "it": "Guida completa ai test di funzionalità epatica",
        "he": "מדריך מקיף לבדיקות תפקודי כבד",
        "hi": "लिवर फंक्शन टेस्ट की पूरी गाइड",
        "ar": "الدليل الشامل لاختبارات وظائف الكبد",
    }
    subtitles = {
        "en": "ALT, AST, ALP, GGT, bilirubin — understand every marker in your liver panel with normal ranges and clinical significance.",
        "tr": "ALT, AST, ALP, GGT, bilirubin — karaciğer panelinizin her belirtecini normal aralıklar ve klinik önemleriyle anlayın.",
        "de": "ALT, AST, ALP, GGT, Bilirubin — verstehen Sie jeden Marker Ihres Leberpanels mit Normalbereichen und klinischer Bedeutung.",
        "es": "ALT, AST, ALP, GGT, bilirrubina — comprenda cada marcador de su panel hepático con rangos normales y significado clínico.",
        "fr": "ALT, AST, ALP, GGT, bilirubine — comprenez chaque marqueur de votre bilan hépatique avec les valeurs normales et leur signification clinique.",
        "it": "ALT, AST, ALP, GGT, bilirubina — comprendi ogni marcatore del tuo pannello epatico con intervalli normali e significato clinico.",
        "he": "ALT, AST, ALP, GGT, בילירובין — הבינו כל סמן בפאנל הכבד שלכם עם טווחים תקינים ומשמעות קלינית.",
        "hi": "ALT, AST, ALP, GGT, बिलीरुबिन — सामान्य सीमाओं और नैदानिक महत्व के साथ अपने लिवर पैनल के हर मार्कर को समझें।",
        "ar": "ALT، AST، ALP، GGT، البيليروبين — افهم كل مؤشر في فحص الكبد مع النطاقات الطبيعية والأهمية السريرية.",
    }
    excerpts = {
        "en": "A comprehensive guide to understanding liver function tests — ALT, AST, ALP, GGT, and bilirubin explained with normal ranges.",
        "tr": "Karaciğer fonksiyon testlerini anlamak için kapsamlı bir rehber — ALT, AST, ALP, GGT ve bilirubin normal aralıklarıyla açıklandı.",
        "de": "Ein umfassender Leitfaden zum Verständnis der Leberfunktionstests — ALT, AST, ALP, GGT und Bilirubin erklärt.",
        "es": "Guía completa para entender las pruebas de función hepática — ALT, AST, ALP, GGT y bilirrubina explicadas.",
        "fr": "Guide complet pour comprendre les tests hépatiques — ALT, AST, ALP, GGT et bilirubine expliqués.",
        "it": "Guida completa per comprendere i test epatici — ALT, AST, ALP, GGT e bilirubina spiegati.",
        "he": "מדריך מקיף להבנת בדיקות תפקודי כבד — ALT, AST, ALP, GGT ובילירובין מוסברים.",
        "hi": "लिवर फंक्शन टेस्ट को समझने के लिए व्यापक गाइड — ALT, AST, ALP, GGT और बिलीरुबिन की व्याख्या।",
        "ar": "دليل شامل لفهم اختبارات وظائف الكبد — ALT و AST و ALP و GGT والبيليروبين موضحة.",
    }
    seo_titles = {k: v + " | NoryaAI" for k, v in titles.items()}
    seo_descriptions = {
        "en": "Understand ALT, AST, ALP, GGT, and bilirubin in your liver panel. Normal ranges, high/low causes, AST/ALT ratio, and common liver conditions explained.",
        "tr": "Karaciğer panelinizdeki ALT, AST, ALP, GGT ve bilirubini anlayın. Normal aralıklar, yüksek/düşük nedenleri, AST/ALT oranı ve yaygın karaciğer hastalıkları.",
        "de": "Verstehen Sie ALT, AST, ALP, GGT und Bilirubin in Ihrem Leberpanel. Normalbereiche, Ursachen für hohe/niedrige Werte und häufige Lebererkrankungen.",
        "es": "Comprenda ALT, AST, ALP, GGT y bilirrubina en su panel hepático. Rangos normales, causas y enfermedades hepáticas comunes.",
        "fr": "Comprenez ALT, AST, ALP, GGT et bilirubine dans votre bilan hépatique. Valeurs normales, causes et maladies hépatiques courantes.",
        "it": "Comprendi ALT, AST, ALP, GGT e bilirubina nel tuo pannello epatico. Intervalli normali, cause e malattie epatiche comuni.",
        "he": "הבינו ALT, AST, ALP, GGT ובילירובין בפאנל הכבד שלכם. טווחים תקינים, סיבות לערכים גבוהים/נמוכים ומחלות כבד שכיחות.",
        "hi": "अपने लिवर पैनल में ALT, AST, ALP, GGT और बिलीरुबिन को समझें। सामान्य सीमाएं, उच्च/निम्न कारण और सामान्य लिवर स्थितियां।",
        "ar": "افهم ALT وAST وALP وGGT والبيليروبين في فحص الكبد. النطاقات الطبيعية والأسباب وأمراض الكبد الشائعة.",
    }
    cover_alt = {
        "en": "Liver function test results with ALT, AST, ALP, GGT and bilirubin values",
        "tr": "ALT, AST, ALP, GGT ve bilirubin değerlerini gösteren karaciğer fonksiyon testi sonuçları",
        "de": "Leberfunktionstest-Ergebnisse mit ALT, AST, ALP, GGT und Bilirubin-Werten",
        "es": "Resultados de pruebas de función hepática con valores de ALT, AST, ALP, GGT y bilirrubina",
        "fr": "Résultats des tests hépatiques avec valeurs d'ALT, AST, ALP, GGT et bilirubine",
        "it": "Risultati dei test epatici con valori di ALT, AST, ALP, GGT e bilirubina",
        "he": "תוצאות בדיקות תפקודי כבד עם ערכי ALT, AST, ALP, GGT ובילירובין",
        "hi": "ALT, AST, ALP, GGT और बिलीरुबिन मानों के साथ लिवर फंक्शन टेस्ट के परिणाम",
        "ar": "نتائج اختبارات وظائف الكبد مع قيم ALT وAST وALP وGGT والبيليروبين",
    }
    return Article(
        id="liver-function-tests-guide",
        published_at=published,
        read_minutes=10,
        cover_image=cover,
        category=cat,
        slugs=slugs,
        titles=titles,
        subtitles=subtitles,
        excerpts=excerpts,
        seo_titles=seo_titles,
        seo_descriptions=seo_descriptions,
        cover_alt=cover_alt,
        sections_by_lang=get_liver_panel_sections_by_lang(),
        last_updated=published,
        faq_schema_qa=get_liver_panel_faq_schema_qa(),
    )
