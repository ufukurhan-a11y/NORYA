#!/usr/bin/env python3
"""4 blog makalesini admin API üzerinden ekler (4 konu × 9 dil = 36 post).
Kullanım: python scripts/add_blog_posts.py --url http://localhost:8000 --admin-secret YOUR_KEY
"""
import requests, json, sys, argparse
from datetime import datetime

def sec(i, h, b, l=2):
    return {"id": i, "level": l, "heading": h, "body_html": b}

TS = 'class="w-full border border-slate-200 text-sm my-4" style="border-collapse: collapse;"'
THL = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
THR = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:right;"'
TD = 'style="border:1px solid #cbd5e1;padding:8px 12px;"'

def tbl(hs, rows, rtl=False):
    th = THR if rtl else THL
    h = "<thead><tr>" + "".join(f"<th {th}>{x}</th>" for x in hs) + "</tr></thead>"
    b = "<tbody>" + "".join("<tr>" + "".join(f"<td {TD}>{x}</td>" for x in r) + "</tr>" for r in rows) + "</tbody>"
    return f'<table {TS}>{h}{b}</table>'

COVERAGE_NOTE = "<p><em>Bu bilgi bilgilendirme amaçlıdır ve tıbbi tavsiye değildir. Sonuçlarınızı doktorunuzla görüşün.</em></p>"

CATS = {"tr":"Kalp Sağlığı","en":"Heart Health","de":"Herzgesundheit","fr":"Santé cardiaque","it":"Salute del cuore","es":"Salud cardíaca","he":"בריאות הלב","hi":"हृदय स्वास्थ्य","ar":"صحة القلب"}
CATS2 = {"tr":"Genel Sağlık","en":"General Health","de":"Allgemeine Gesundheit","fr":"Santé générale","it":"Salute generale","es":"Salud general","he":"בריאות כללית","hi":"सामान्य स्वास्थ्य","ar":"الصحة العامة"}

ALL_POSTS = []

###############################################################################
# APOB - 9 dil
###############################################################################
APOB_SECTIONS = {
"en": [
    sec("intro","What is ApoB and why does it matter?","<p><strong>Apolipoprotein B (ApoB)</strong> is a structural protein found on the surface of all atherogenic lipoprotein particles (LDL, VLDL, IDL). Because each atherogenic particle carries exactly <strong>one ApoB molecule</strong>, measuring ApoB gives a direct count of particles capable of depositing cholesterol in artery walls.</p><p>Unlike traditional lipid panels measuring cholesterol content (LDL-C, non-HDL-C), ApoB measures the <strong>total number of atherogenic particles</strong>. Two people can have identical LDL-C but very different ApoB counts—meaning different cardiovascular risk.</p>"),
    sec("understanding","Understanding ApoB: particle count approach","<p>Every cholesterol-carrying particle contributing to atherosclerosis carries exactly one ApoB molecule: LDL particles (~90%), VLDL, IDL, and Lp(a). Because ApoB quantifies total particle number, it provides a <strong>more accurate cardiovascular risk assessment</strong> than cholesterol concentration alone.</p>"),
    sec("ranges","Normal and optimal ApoB ranges",tbl(["Risk Category","ApoB (mg/dL)"],[("Optimal","&lt; 65"),("Low risk","65–80"),("Moderate risk","80–100"),("High risk","100–130"),("Very high risk","&gt; 130")])+"<p>Target levels depend on individual risk. For high-risk patients (diabetes, established CVD), guidelines recommend ApoB &lt; 65–80 mg/dL.</p>"),
    sec("causes","What causes high ApoB?","<p>Elevated ApoB can result from: genetic predisposition (familial hypercholesterolemia), high saturated/trans fat intake, metabolic syndrome, obesity, physical inactivity, hypothyroidism, and chronic kidney disease. Even with normal LDL-C, ApoB can be elevated—called <strong>discordance</strong>, common in metabolic syndrome.</p>"),
    sec("treatment","How to lower ApoB","<ul><li><strong>Statin therapy</strong> — 20–50% reduction</li><li><strong>Ezetimibe</strong> — additional 15–20%</li><li><strong>PCSK9 inhibitors</strong> — 50–60% reduction</li><li><strong>Diet</strong> — reduce saturated fats, increase soluble fiber</li><li><strong>Exercise</strong> — ≥150 min/week moderate aerobic activity</li><li><strong>Weight management</strong> — reducing visceral fat lowers VLDL/ApoB</li></ul>"),
    sec("testing","When should ApoB be tested?","<p>Recommended for: routine cardiovascular risk assessment, discordant LDL-C/risk, metabolic syndrome, type 2 diabetes, monitoring lipid therapy, familial hypercholesterolemia, and strong family history of premature CVD.</p><p><strong>Norya</strong> can analyze your blood test results and help interpret your lipid markers. Upload your report for free AI-powered review.</p>"+COVERAGE_NOTE),
],
"tr": [
    sec("intro","ApoB nedir ve neden önemlidir?","<p><strong>Apolipoprotein B (ApoB)</strong>, LDL, VLDL ve IDL dahil tüm aterojenik lipoprotein parçacıklarının yüzeyinde bulunan yapısal bir proteindir. Her aterojenik parçacık tam olarak <strong>bir ApoB molekülü</strong> taşımaktadır, bu nedenle ApoB ölçümü kolesterolü arter duvarlarına biriktirebilecek parçacıkların doğrudan sayısını verir.</p><p>Geleneksel lipid panelleri parçacık içindeki kolesterol içeriğini ölçerken, ApoB <strong>aterojenik parçacıkların toplam sayısını</strong> ölçer. İki kişinin LDL-Kolesterol düzeyleri aynı olabilir ancak ApoB sayıları farklı olabilir.</p>"),
    sec("understanding","ApoB'yi anlamak","<p>Ateroskleroz'a katkıda bulunabilen her kolesterol parçacığı bir ApoB molekülü taşır: LDL parçacıkları (%90), VLDL, IDL ve Lp(a). ApoB toplam parçacık sayısını belirlediğinden, <strong>kolesterol konsantrasyonundan daha doğru bir risk değerlendirmesi</strong> sağlar.</p>"),
    sec("ranges","Normal ve optimal ApoB değerleri",tbl(["Risk Kategorisi","ApoB (mg/dL)"],[("Optimal","&lt; 65"),("Düşük risk","65–80"),("Orta risk","80–100"),("Yüksek risk","100–130"),("Çok yüksek risk","&gt; 130")])+"<p>Yüksek riskli hastalar için kılavuzlar ApoB &lt; 65–80 mg/dL önerir. Referans aralıkları laboratuvara göre farklılık gösterebilir.</p>"),
    sec("causes","Yüksek ApoB nedenleri?","<p>Genetik yatkınlık (ailesel hiperkolesterolemi), yüksek doymuş/trans yağ alımı, metabolik sendrom, obezite, hareketsiz yaşam, hipotiroidi ve kronik böbrek hastalığı. Normal LDL-Kolesterol ile bile ApoB yüksek olabilir—<strong>diskordans</strong> olarak adlandırılır ve metabolik sendromda sık görülür.</p>"),
    sec("treatment","ApoB nasıl düşürülür?","<ul><li><strong>Statin tedavisi</strong> — %20–50 düşüş</li><li><strong>Ezetimib</strong> — ek %15–20</li><li><strong>PCSK9 inhibitörleri</strong> — %50–60 düşüş</li><li><strong>Beslenme</strong> — doymuş yağları azaltın, çözünür lifi artırın</li><li><strong>Egzersiz</strong> — haftada ≥150 dk orta şiddette aktivite</li><li><strong>Kilo yönetimi</strong> — visseral yağın azaltılması VLDL/ApoB üretimi düşürür</li></ul>"),
    sec("testing","ApoB ne zaman test edilmeli?","<p>Rutin kardiyovasküler risk değerlendirmesi, uyumsuz LDL/risk profili, metabolik sendrom, tip 2 diyabet, lipid tedavisi takibi, ailesel hiperkolesterolemi ve güçlü aile öyküsü olanlarda önerilir.</p><p><strong>Norya</strong> ile kan tahlili sonuçlarınızı ücretsiz yapay zeka ile yorumlayın.</p>"+COVERAGE_NOTE.replace("tıbbi","tıbbi").replace("doktorunuzla","hekiminizle görüşün."),
],
"de": [
    sec("intro","Was ist ApoB und warum ist es wichtig?","<p><strong>Apolipoprotein B (ApoB)</strong> ist ein Strukturprotein auf der Oberfläche aller atherogenen Lipoproteinpartikel (LDL, VLDL, IDL). Jedes atherogene Partikel trägt genau <strong>ein ApoB-Molekül</strong>, sodass ApoB die Anzahl der Partikel misst, die Cholesterin in Arterien ablagern können.</p>"),
    sec("understanding","ApoB verstehen","<p>Da ApoB die Gesamtzahl atherogener Partikel quantifiziert, bietet es eine <strong>genauere kardiovaskuläre Risikobewertung</strong> als die alleinige Cholesterinmessung.</p>"),
    sec("ranges","Normale ApoB-Werte",tbl(["Risikokategorie","ApoB (mg/dL)"],[("Optimal","&lt; 65"),("Niedrig","65–80"),("Mittel","80–100"),("Hoch","100–130"),("Sehr hoch","&gt; 130")])+"<p>Bei Hochrisikopatienten: &lt; 65–80 mg/dL empfohlen.</p>"),
    sec("causes","Ursachen erhöhter Werte","<p>Genetische Veranlagung, gesättigte Fette, metabolisches Syndrom, Adipositas, Bewegungsmangel, Hypothyreose und chronische Nierenerkrankung.</p>"),
    sec("treatment","ApoB senken","<ul><li><strong>Statine</strong> — 20–50%</li><li><strong>Ezetimib</strong> — 15–20% zusätzlich</li><li><strong>PCSK9-Inhibitoren</strong> — 50–60%</li><li><strong>Ernährung</strong> — weniger gesättigte Fette, mehr Ballaststoffe</li><li><strong>Bewegung</strong> — ≥150 Min./Woche</li></ul>"),
    sec("testing","Wann testen?","<p>Empfohlen bei kardiovaskulärer Risikobewertung, metabolischem Syndrom, Diabetes Typ 2, familiärer Hypercholesterinämie und starker familiärer Vorgeschichte.</p>"+COVERAGE_NOTE.replace("tıbbi","ärztlichen").replace("hekiminizle","Arzt"),
],
"fr": [
    sec("intro","Qu'est-ce que l'ApoB et pourquoi est-elle importante?","<p>L'<strong>apolipoprotéine B (ApoB)</strong> est une protéine structurelle à la surface de toutes les lipoprotéines athérogènes (LDL, VLDL, IDL). Chaque particule porte exactement <strong>une molécule d'ApoB</strong>, permettant de comptabiliser les particules capables de déposer du cholestérol dans les artères.</p>"),
    sec("understanding","Comprendre l'ApoB","<p>L'ApoB quantifie le nombre total de particules athérogènes, offrant une <strong>évaluation plus précise du risque cardiovasculaire</strong> que la seule mesure du cholestérol.</p>"),
    sec("ranges","Plages normales d'ApoB",tbl(["Catégorie","ApoB (mg/dL)"],[("Optimal","&lt; 65"),("Faible","65–80"),("Modéré","80–100"),("Élevé","100–130"),("Très élevé","&gt; 130")])+"<p>Pour les patients à haut risque : &lt; 65–80 mg/dL.</p>"),
    sec("causes","Causes de l'ApoB élevée","<p>Prédisposition génétique, graisses saturées, syndrome métabolique, obésité, sédentarité, hypothyroïdie et maladie rénale chronique.</p>"),
    sec("treatment","Réduire l'ApoB","<ul><li><strong>Statines</strong> — réduction de 20-50%</li><li><strong>Ézétimibe</strong> — 15-20% supplémentaires</li><li><strong>Inhibiteurs PCSK9</strong> — 50-60%</li><li><strong>Alimentation</strong> — moins de graisses saturées, plus de fibres</li><li><strong>Exercice</strong> — ≥150 min/semaine</li></ul>"),
    sec("testing","Quand tester l'ApoB?","<p>Recommandé pour : évaluation du risque cardiovasculaire, syndrome métabolique, diabète de type 2, hypercholestérolémie familiale et antécédents familiaux.</p>"+COVERAGE_NOTE.replace("doktorunuzla","votre médecin"),
],
"it": [
    sec("intro","Cos'è l'ApoB e perché è importante?","<p>L'<strong>apolipoproteina B (ApoB)</strong> è una proteina strutturale sulla superficie di tutte le lipoproteine aterogeniche (LDL, VLDL, IDL). Ogni particella trasporta esattamente <strong>una molecola di ApoB</strong>, permettendo di contare le particelle che possono depositare colesterolo nelle arterie.</p>"),
    sec("understanding","Capire l'ApoB","<p>L'ApoB quantifica il numero totale di particelle aterogeniche, offrendo una <strong>valutazione più accurata del rischio cardiovascolare</strong> rispetto alla sola misurazione del colesterolo.</p>"),
    sec("ranges","Valori normali di ApoB",tbl(["Categoria","ApoB (mg/dL)"],[("Ottimale","&lt; 65"),("Basso","65–80"),("Moderato","80–100"),("Alto","100–130"),("Molto alto","&gt; 130")])+"<p>Per pazienti ad alto rischio: &lt; 65-80 mg/dL.</p>"),
    sec("causes","Cause di ApoB elevata","<p>Predisposizione genetica, grassi saturi, sindrome metabolica, obesità, sedentarietà, ipotiroidismo e malattia renale cronica.</p>"),
    sec("treatment","Abbassare l'ApoB","<ul><li><strong>Statine</strong> — riduzione del 20-50%</li><li><strong>Ezetimibe</strong> — ulteriore 15-20%</li><li><strong>Inibitori PCSK9</strong> — 50-60%</li><li><strong>Dieta</strong> — meno grassi saturi, più fibre</li><li><strong>Esercizio</strong> — ≥150 min/settimana</li></ul>"),
    sec("testing","Quando testare l'ApoB?","<p>Raccomandato per valutazione del rischio cardiovascolare, sindrome metabolica, diabete di tipo 2, ipercolesterolemia familiare e forte storia familiare.</p>"+COVERAGE_NOTE.replace("doktorunuzla","il vostro medico"),
],
"es": [
    sec("intro","¿Qué es la ApoB y por qué es importante?","<p>La <strong>apolipoproteína B (ApoB)</strong> es una proteína estructural en la superficie de todas las lipoproteínas aterogénicas (LDL, VLDL, IDL). Cada partícula lleva exactamente <strong>una molécula de ApoB</strong>, lo que permite contar las partículas que pueden depositar colesterol en las arterias.</p>"),
    sec("understanding","Entender la ApoB","<p>La ApoB cuantifica el número total de partículas aterogénicas, ofreciendo una <strong>evaluación más precisa del riesgo cardiovascular</strong> que la medición aislada del colesterol.</p>"),
    sec("ranges","Rangos normales de ApoB",tbl(["Categoría","ApoB (mg/dL)"],[("Óptimo","&lt; 65"),("Bajo","65–80"),("Moderado","80–100"),("Alto","100–130"),("Muy alto","&gt; 130")])+"<p>Para pacientes de alto riesgo: &lt; 65-80 mg/dL.</p>"),
    sec("causes","Causas de ApoB elevada","<p>Predisposición genética, grasas saturadas, síndrome metabólico, obesidad, sedentarismo, hipotiroidismo y enfermedad renal crónica.</p>"),
    sec("treatment","Reducir la ApoB","<ul><li><strong>Estatinas</strong> — reducción del 20-50%</li><li><strong>Ezetimiba</strong> — 15-20% adicional</li><li><strong>Inhibidores PCSK9</strong> — 50-60%</li><li><strong>Dieta</strong> — menos grasas saturadas, más fibra</li><li><strong>Ejercicio</strong> — ≥150 min/semana</li></ul>"),
    sec("testing","¿Cuándo analizar la ApoB?","<p>Recomendado para evaluación de riesgo cardiovascular, síndrome metabólico, diabetes tipo 2, hipercolesterolemia familiar y antecedentes familiares fuertes.</p>"+COVERAGE_NOTE.replace("doktorunuzla","su médico"),
],
"he": [
    sec("intro","מהו ApoB ולמה זה חשוב?","<p><strong>אפוליפופרוטאין B (ApoB)</strong> הוא חלבון מבני על פני השטח של כל חלקיקי הליפופרוטאין הטרשתיים (LDL, VLDL, IDL). כל חלקיק נושא בדיוק <strong>מולקולת ApoB אחת</strong>, כך שמדידת ApoB נותנת ספירה ישירה של החלקיקים שיכולים לשקע כולסטרול בדפנות העורקים.</p>"),
    sec("understanding","הבנת ApoB","<p>ApoB מודד את המספר הכולל של חלקיקים טרשתיים, ומספק <strong>הערכת סיכון לבבי-כלי מדויקת יותר</strong> ממדידת כולסטרול בלבד.</p>"),
    sec("ranges","טווחי ApoB נורמליים",tbl(["קטגוריית סיכון","ApoB (mg/dL)"],[("אופטימלי","&lt; 65"),("נמוך","65–80"),("מתון","80–100"),("גבוה","100–130"),("גבוה מאוד","&gt; 130")],rtl=True)+"<p>לחולים בסיכון גבוה: &lt; 65-80 mg/dL.</p>"),
    sec("causes","גורמים לרמות ApoB גבוהות","<p>נטייה גנטית, שומנים רוויים, תסמונת מטבולית, השמנת יתר, חוסר פעילות, תת-פעילות בלוטת התריס ומחלת כליות כרונית.</p>"),
    sec("treatment","הורדת רמות ApoB","<ul><li><strong>סטטינים</strong> — 20-50%</li><li><strong>אזטימיב</strong> — 15-20% נוספים</li><li><strong>מעכבי PCSK9</strong> — 50-60%</li><li><strong>תזונה</strong> — פחות שומנים רוויים, יותר סיבים</li><li><strong>פעילות גופנית</strong> — ≥150 דקות/שבוע</li></ul>"),
    sec("testing","מתי לבדוק ApoB?","<p>מומלץ עבור הערכת סיכון לבבי-כלי, תסמונת מטבולית, סוכרת סוג 2, היפרכולסטרולמיה משפחתית והיסטוריה משפחתית.</p>"+COVERAGE_NOTE.replace("tıbbi","רפואי").replace("hekiminizle","הרופא"),
],
"hi": [
    sec("intro","ApoB क्या है और यह क्यों महत्वपूर्ण है?","<p><strong>एपोलिपोप्रोटीन B (ApoB)</strong> सभी एथेरोजेनिक लिपोप्रोटीन कणों (LDL, VLDL, IDL) की सतह पर पाया जाने वाला संरचनात्मक प्रोटीन है। प्रत्येक एथेरोजेनिक कण में ठीक <strong>एक ApoB अणु</strong> होता है, इसलिए ApoB मापन उन कणों की सीधी गिनती देता है जो धमनियों में कोलेस्ट्रॉल जमा कर सकते हैं।</p>"),
    sec("understanding","ApoB को समझना","<p>ApoB एथेरोजेनिक कणों की कुल संख्या को मापता है, जो केवल कोलेस्ट्रॉल मापन से <strong>अधिक सटीक हृदय जोखिम मूल्यांकन</strong> प्रदान करता है।</p>"),
    sec("ranges","सामान्य ApoB सीमाएँ",tbl(["जोखिम श्रेणी","ApoB (mg/dL)"],[("इष्टतम","&lt; 65"),("कम","65–80"),("मध्यम","80–100"),("उच्च","100–130"),("बहुत उच्च","&gt; 130")])+"<p>उच्च जोखिम रोगियों के लिए: &lt; 65-80 mg/dL।</p>"),
    sec("causes","उच्च ApoB के कारण","<p>आनुवंशिक प्रवृत्ति, संतृप्त वसा, मेटाबॉलिक सिंड्रोम, मोटापा, शारीरिक निष्क्रियता, हाइपोथायरायडिज्म और पुरानी किडनी की बीमारी।</p>"),
    sec("treatment","ApoB कैसे कम करें","<ul><li><strong>स्टैटिन</strong> — 20-50% कमी</li><li><strong>एज़ेटिमाइब</strong> — 15-20% अतिरिक्त</li><li><strong>PCSK9 इनहिबिटर्स</strong> — 50-60%</li><li><strong>आहार</strong> — कम संतृप्त वसा, अधिक फाइबर</li><li><strong>व्यायाम</strong> — ≥150 मिनट/सप्ताह</li></ul>"),
    sec("testing","ApoB कब टेस्ट करें?","<p>हृदय जोखिम मूल्यांकन, मेटाबॉलिक सिंड्रोम, टाइप 2 डायबिटीज, फैमिलियल हाइपरकोलेस्ट्रोलेमिया और मजबूत पारिवारिक इतिहास के लिए अनुशंसित।</p>"+COVERAGE_NOTE.replace("tıbbi","चिकित्सा").replace("hekiminizle","अपने डॉक्टर"),
],
"ar": [
    sec("intro","ما هو ApoB ولماذا هو مهم؟","<p><strong>أبوليبوبروتين B (ApoB)</strong> هو بروتين هيكلي موجود على سطح جميع جسيمات البروتين الدهني المسببة لتصلب الشرايين (LDL, VLDL, IDL). يحمل كل جسيم <strong>جزيء ApoB واحد بالضبط</strong>، لذا فإن قياس ApoB يعطي عدداً مباشراً للجسيمات القادرة على ترسيب الكوليسترول في جدران الشرايين.</p>"),
    sec("understanding","فهم ApoB","<p>يقيس ApoB العدد الإجمالي للجسيمات المسببة لتصلب الشرايين، مما يوفر <strong>تقييماً أكثر دقة لمخاطر القلب والأوعية الدموية</strong> من قياس الكوليسترول وحده.</p>"),
    sec("ranges","مستويات ApoB الطبيعية",tbl(["فئة المخاطر","ApoB (mg/dL)"],[("مثالي","&lt; 65"),("منخفض","65–80"),("متوسط","80–100"),("عالي","100–130"),("عالي جداً","&gt; 130")],rtl=True)+"<p>للمرضى عالي الخطورة: &lt; 65-80 ملغ/دل.</p>"),
    sec("causes","أسباب ارتفاع ApoB","<p>الاستعداد الوراثي، الدهون المشبعة، المتلازمة الأيضية، السمنة، قلة النشاط البدني، قصور الغدة الدرقية ومرض الكلى المزمن.</p>"),
    sec("treatment":"كيفية خفض ApoB","<ul><li><strong>الستاتينات</strong> — خفض 20-50%</li><li><strong>إيزيتيميب</strong> — 15-20% إضافي</li><li><strong>مثبطات PCSK9</strong> — 50-60%</li><li><strong>النظام الغذائي</strong> — تقليل الدهون المشبعة، زيادة الألياف</li><li><strong>التمرين</strong> — ≥150 دقيقة/أسبوع</li></ul>"),