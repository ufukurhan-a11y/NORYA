from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Dict, List, Optional


# Blog'un desteklediği diller (mevcut sistemle uyumlu)
BLOG_LANGS = frozenset({"tr", "en", "de", "it", "es", "fr", "he", "ar", "hi", "el", "cs", "sr"})
# Premium blog: sadece bu dillerde route açılır; varsayılan İngilizce
BLOG_LANGS_PREMIUM = ("en", "de", "fr", "it")
DEFAULT_BLOG_LANG = "en"

# Blog arayüzü çevirileri (liste sayfası, detay CTA, vb.) — en, de, fr, it
BLOG_UI = {
    "en": {
        "hero_badge": "Health insights",
        "hero_title": "Norya Blog",
        "hero_desc": "Clear, evidence-based content to help you understand your lab results and biomarkers.",
        "search_placeholder": "Search articles…",
        "category_all": "All",
        "read_article": "Read article",
        "read_min": "min read",
        "cta_title": "Understand your blood test more clearly",
        "cta_text": "Use Norya to turn biomarker values into a more structured and easier-to-read health summary.",
        "cta_button": "Start analysis",
        "toc_title": "On this page",
        "other_languages": "Other languages",
        "back_to_blog": "Back to blog",
        "home_link": "Norya",
        "seo_title": "Norya Blog — Health analysis and lab results",
        "meta_description": "Evidence-based articles to help you understand blood tests, biomarkers and lab reports.",
        "no_results": "No articles match your search.",
        "last_updated": "Last updated",
    },
    "de": {
        "hero_badge": "Gesundheitswissen",
        "hero_title": "Norya Blog",
        "hero_desc": "Klare, evidenzbasierte Inhalte, die Ihnen helfen, Laborergebnisse und Biomarker besser zu verstehen.",
        "search_placeholder": "Artikel suchen…",
        "category_all": "Alle",
        "read_article": "Artikel lesen",
        "read_min": "Min. Lesezeit",
        "cta_title": "Ihr Blutbild klarer verstehen",
        "cta_text": "Mit Norya werden Ihre Biomarker-Werte in eine strukturierte, gut lesbare Gesundheitszusammenfassung übersetzt.",
        "cta_button": "Analyse starten",
        "toc_title": "Auf dieser Seite",
        "other_languages": "Andere Sprachen",
        "back_to_blog": "Zurück zum Blog",
        "home_link": "Norya",
        "seo_title": "Norya Blog — Gesundheitsanalyse und Laborergebnisse",
        "meta_description": "Evidenzbasierte Artikel zu Blutwerten, Biomarkern und Laborbefunden.",
        "no_results": "Keine Artikel entsprechen Ihrer Suche.",
        "last_updated": "Zuletzt aktualisiert",
    },
    "fr": {
        "hero_badge": "Santé & analyses",
        "hero_title": "Blog Norya",
        "hero_desc": "Des contenus clairs et fondés sur les preuves pour mieux comprendre vos résultats de laboratoire et biomarqueurs.",
        "search_placeholder": "Rechercher un article…",
        "category_all": "Tout",
        "read_article": "Lire l'article",
        "read_min": "min de lecture",
        "cta_title": "Comprenez mieux votre bilan sanguin",
        "cta_text": "Avec Norya, transformez vos valeurs de biomarqueurs en un résumé de santé structuré et lisible.",
        "cta_button": "Lancer l'analyse",
        "toc_title": "Sur cette page",
        "other_languages": "Autres langues",
        "back_to_blog": "Retour au blog",
        "home_link": "Norya",
        "seo_title": "Blog Norya — Analyses santé et résultats de laboratoire",
        "meta_description": "Articles fondés sur les preuves pour comprendre bilans sanguins, biomarqueurs et comptes-rendus de laboratoire.",
        "no_results": "Aucun article ne correspond à votre recherche.",
        "last_updated": "Dernière mise à jour",
    },
    "it": {
        "hero_badge": "Salute e analisi",
        "hero_title": "Blog Norya",
        "hero_desc": "Contenuti chiari e basati su evidenze per capire meglio i tuoi risultati di laboratorio e i biomarcatori.",
        "search_placeholder": "Cerca articoli…",
        "category_all": "Tutti",
        "read_article": "Leggi l'articolo",
        "read_min": "min di lettura",
        "cta_title": "Comprendi meglio le tue analisi del sangue",
        "cta_text": "Con Norya trasformi i valori dei biomarcatori in un riepilogo di salute strutturato e facile da leggere.",
        "cta_button": "Avvia analisi",
        "toc_title": "In questa pagina",
        "other_languages": "Altre lingue",
        "back_to_blog": "Torna al blog",
        "home_link": "Norya",
        "seo_title": "Blog Norya — Analisi della salute e risultati di laboratorio",
        "meta_description": "Articoli basati su evidenze per capire esami del sangue, biomarcatori e referti di laboratorio.",
        "no_results": "Nessun articolo corrisponde alla ricerca.",
        "last_updated": "Ultimo aggiornamento",
    },
}


@dataclass(frozen=True)
class Section:
    id: str
    level: int  # 2 = H2, 3 = H3
    heading: str
    body_html: str  # Güvenli, önceden yazılmış HTML


@dataclass(frozen=True)
class Article:
    id: str
    published_at: date
    read_minutes: int
    cover_image: str
    category: Dict[str, str]  # lang -> kategori adı
    slugs: Dict[str, str]  # lang -> slug
    titles: Dict[str, str]  # lang -> H1
    subtitles: Dict[str, str]  # lang -> alt açıklama
    excerpts: Dict[str, str]  # lang -> liste kartı kısa açıklama
    seo_titles: Dict[str, str]
    seo_descriptions: Dict[str, str]
    sections_by_lang: Dict[str, List[Section]]  # lang -> bölümler
    cover_alt: Optional[Dict[str, str]] = None  # lang -> alt text for cover image
    last_updated: Optional[date] = None  # display "Last updated"; if None, use published_at


def _article_ldl() -> Article:
    """LDL kolesterol yazısı — tüm dillerde çeviri içeren örnek makale."""
    published = date(2025, 1, 5)
    cover = "/static/images/blog/ldl-cholesterol-hero.png"

    return Article(
        id="ldl-target-values",
        published_at=published,
        read_minutes=7,
        cover_image=cover,
        category={
            "tr": "Kolesterol",
            "en": "Cholesterol",
            "de": "Cholesterin",
            "it": "Colesterolo",
            "es": "Colesterol",
            "fr": "Cholestérol",
            "he": "כולסטרול",
            "ar": "الكوليسترول",
            "hi": "कोलेस्ट्रॉल",
            "el": "Χοληστερόλη",
            "cs": "Cholesterol",
            "sr": "Холестерол",
        },
        slugs={
            "tr": "ldl-kolesterol-kac-olmali",
            "en": "ldl-cholesterol-level",
            "de": "ldl-cholesterin",
            "it": "valori-ldl-colesterolo",
            "es": "niveles-colesterol-ldl",
            "fr": "taux-de-ldl-cholesterol",
            "he": "ldl-cholesterol-target",
            "ar": "ldl-cholesterol-normal-range",
            "hi": "ldl-cholesterol-kitna-hona-chahiye",
            "el": "ldl-cholesterol-target-values",
            "cs": "hodnoty-ldl-cholesterolu",
            "sr": "ciljne-vrednosti-ldl-holesterola",
        },
        titles={
            "tr": "LDL kolesterol kaç olmalı? Hangi seviye riskli?",
            "en": "What should your LDL cholesterol level be?",
            "de": "Wie hoch sollte Ihr LDL‑Cholesterin sein?",
            "it": "Quanto dovrebbe essere il colesterolo LDL?",
            "es": "¿Cuál debería ser tu nivel de colesterol LDL?",
            "fr": "Quel devrait être votre taux de LDL‑cholestérol ?",
            "he": "מהו ערך LDL כולסטרול תקין ולמי יש סיכון?",
            "ar": "كم يجب أن يكون مستوى كوليسترول LDL وما الذي يعتبر خطيراً؟",
            "hi": "एलडीएल (LDL) कोलेस्ट्रॉल कितना होना चाहिए और कब जोखिम artar?",
            "el": "Ποια πρέπει να είναι τα επίπεδα LDL χοληστερόλης σας;",
            "cs": "Jaké by měly být hodnoty LDL cholesterolu?",
            "sr": "Колико треба да буде LDL холестерол и када постаје ризичан?",
        },
        subtitles={
            "tr": "LDL kolesterol için hedef aralıkları, risk gruplarına göre hedefler ve tetkik sonucunuzda gördüğünüz değerleri adım adım açıklıyoruz.",
            "en": "Understand target LDL ranges, how risk factors change your goal values, and what your lab report number really means.",
            "de": "Zielbereiche für LDL, Einfluss von Risikofaktoren und was der Wert in Ihrem Laborbefund praktisch bedeutet.",
            "it": "Scopri i valori obiettivo di LDL, come cambiano con i fattori di rischio e come leggere correttamente il tuo referto.",
            "es": "Conoce los rangos objetivo de LDL, cómo cambian según tus factores de riesgo y cómo interpretar tu informe de laboratorio.",
            "fr": "Comprenez les valeurs cibles de LDL, l’impact de vos facteurs de risque et comment interpréter votre résultat de laboratoire.",
            "he": "הסבר פשוט על טווחי היעד של LDL, איך גורמי סיכון משפיעים עליהם ומה אומר המספר שמופיע בבדיקת הדם.",
            "ar": "شرح مبسط لقيم الهدف من LDL، وكيف تؤثر عوامل الخطر على هذه القيم، وكيف تفهم الرقم في نتيجة التحليل.",
            "hi": "LDL के सामान्य लक्ष्य रेंज, जोखिम कारक होने पर लक्ष्य कैसे बदलते हैं और आपकी रिपोर्ट में दिखने वाला नंबर क्या बताता है।",
            "el": "Στόχοι για LDL, πώς τους αλλάζουν οι παράγοντες κινδύνου και πώς να διαβάζετε σωστά το αποτέλεσμα στο χαρτί εξετάσεων.",
            "cs": "Cílové hodnoty LDL, vliv rizikových faktorů a návod, jak číst váš laboratorní výsledek.",
            "sr": "Циљне вредности LDL‑а, утицај фактора ризика и како да правилно тумачите број у лабораторијском извештају.",
        },
        excerpts={
            "tr": "LDL kolesterol için 'normal' tek bir sayı yoktur. Kardiyovasküler riskinize göre hedef değerler değişir.",
            "en": "There is no single “normal” LDL value. Targets depend on your overall cardiovascular risk.",
            "de": "Es gibt keinen einen „normalen“ LDL‑Wert – Zielbereiche hängen von Ihrem kardiovaskulären Risiko ab.",
            "it": "Non esiste un unico valore “normale” di LDL: il target dipende dal tuo rischio cardiovascolare.",
            "es": "No hay un único valor “normal” de LDL: el objetivo depende de tu riesgo cardiovascular global.",
            "fr": "Il n’existe pas une seule valeur « normale » de LDL ; la cible dépend de votre risque cardiovasculaire.",
            "he": "אין מספר אחד ״נורמלי״ ל‑LDL – ערך היעד נקבע לפי רמת הסיכון הלבבי הכוללת.",
            "ar": "لا يوجد رقم واحد «طبيعي» لـ LDL، فالقيمة المستهدفة تختلف حسب مستوى خطر أمراض القلب لديك.",
            "hi": "LDL के लिए एक ही ‘नॉर्मल’ वैल्यू नहीं होती, आपका समग्र हार्ट‑रिस्क तय करता है कि लक्ष्य कितना होना चाहिए।",
            "el": "Δεν υπάρχει μία «φυσιολογική» τιμή LDL – ο στόχος εξαρτάται από το συνολικό καρδιαγγειακό σας κίνδυνο.",
            "cs": "Neexistuje jedno univerzální „normální“ číslo LDL – cíle se určují podle vašeho kardiovaskulárního rizika.",
            "sr": "Не постоји једна „нормална“ вредност LDL‑а – циљ зависи од укупног кардиоваскуларног ризика.",
        },
        seo_titles={
            "tr": "LDL Kolesterol Kaç Olmalı? Normal ve Yüksek Değerler",
            "en": "LDL Cholesterol: Normal, High and Target Levels Explained",
            "de": "LDL‑Cholesterin: Normwerte, Zielbereiche und hohes Risiko",
            "it": "LDL Colesterolo: Valori Normali, Alti e Obiettivo",
            "es": "Colesterol LDL: Valores Normales, Altos y Objetivo",
            "fr": "LDL‑cholestérol : valeurs normales, élevées et objectifs",
            "he": "ערכי LDL כולסטרול: תקין, גבוה וערכי יעד",
            "ar": "كوليسترول LDL: القيم الطبيعية، المرتفعة وقيم الهدف",
            "hi": "LDL कोलेस्ट्रॉल: सामान्य, बढ़ा हुआ और लक्ष्य स्तर",
            "el": "LDL χοληστερόλη: φυσιολογικές, υψηλές και στόχοι",
            "cs": "LDL cholesterol: normální, zvýšené a cílové hodnoty",
            "sr": "LDL холестерол: нормалне, повишене и циљне вредности",
        },
        seo_descriptions={
            "tr": "LDL kolesterol için yaşa göre değil risk düzeyine göre hedefler kullanılır. Kendi raporunuzdaki değeri bu rehberle daha iyi anlayın.",
            "en": "LDL targets are set by cardiovascular risk, not age alone. Learn how to interpret your LDL value with practical examples.",
            "de": "LDL‑Zielwerte richten sich nach Ihrem kardiovaskulären Risiko. Erfahren Sie, wie Sie Ihren Laborwert richtig einordnen.",
            "it": "I target di LDL si definiscono in base al rischio cardiovascolare. Scopri come interpretare il valore riportato nel tuo referto.",
            "es": "Los objetivos de LDL se fijan según el riesgo cardiovascular. Aprende a interpretar tu valor de LDL con ejemplos claros.",
            "fr": "Les objectifs de LDL dépendent de votre risque cardiovasculaire. Découvrez comment lire et comprendre votre résultat.",
            "he": "ערכי היעד של LDL נקבעים לפי רמת הסיכון הלבבי. מדריך קצר שיעזור לך להבין טוב יותר את התוצאה בבדיקת הדם.",
            "ar": "قيم الهدف لـ LDL تُحدد حسب خطر أمراض القلب لديك. دليل مبسط لفهم نتيجتك في تحليل الدم.",
            "hi": "LDL का लक्ष्य सिर्फ उम्र से नहीं बल्कि हार्ट‑रिस्क से तय होता है. उदाहरणों के साथ अपनी रिपोर्ट को समझें।",
            "el": "Οι στόχοι για LDL ορίζονται με βάση τον καρδιαγγειακό κίνδυνο. Δείτε πώς να ερμηνεύσετε τη δική σας τιμή.",
            "cs": "Cílové hodnoty LDL vycházejí z vašeho kardiovaskulárního rizika. Podívejte se, jak si správně vyložit svůj výsledek.",
            "sr": "Циљне вредности LDL‑а одређују се према кардиоваскуларном ризику. Сазнајте како да протумачите свој резултат.",
        },
        sections_by_lang={
            "tr": [
                Section(
                    id="ldl-nedir",
                    level=2,
                    heading="LDL kolesterol nedir?",
                    body_html="""
<p>Kolesterol, vücudunuzun hormon üretimi ve hücre zarı yapımı için ihtiyaç duyduğu yağ benzeri bir maddedir. Kanda taşınırken
“lipoprotein” adı verilen paketler içinde dolaşır. LDL (low density lipoprotein), kolesterolü damar duvarına taşıyan partiküldür
ve bu yüzden genellikle “kötü kolesterol” olarak anılır.</p>
<p>LDL seviyesi uzun süre yüksek kaldığında, damar duvarında yağ birikimi (ateroskleroz) artar. Bu süreç kalp krizi ve inme gibi
kardiyovasküler olayların temel nedenlerinden biridir.</p>
""",
                ),
                Section(
                    id="ldl-hedef-degerler",
                    level=2,
                    heading="LDL için hedef değerler nelerdir?",
                    body_html="""
<p>Güncel kılavuzlarda LDL için <strong>tek bir “normal” değer yerine risk düzeyine göre hedef aralıklar</strong> kullanılır.
Basitleştirerek özetlersek:</p>
<ul>
  <li><strong>Düşük / orta riskli bireyler</strong>: LDL genellikle <strong>130 mg/dL&apos;nin altında</strong> tutulur.</li>
  <li><strong>Yüksek riskli bireyler</strong> (hipertansiyon, diyabet, sigara, ailede erken kalp hastalığı vb.): Hedef çoğunlukla
      <strong>100 mg/dL&apos;nin altı</strong>dır.</li>
  <li><strong>Çok yüksek riskli bireyler</strong> (geçirilmiş kalp krizi, stent, inme vb.): Hedef <strong>70 mg/dL, hatta 55 mg/dL</strong>
      altına çekilebilir.</li>
</ul>
<p>Sonuç kâğıdınızda gördüğünüz “referans aralığı” genellikle herkese ortak bir aralığı gösterir. Oysa sizin için uygun hedef,
kişisel risk profilinize göre daha düşük olabilir. Bu nedenle LDL yorumunun mutlaka hekiminizle birlikte yapılması gerekir.</p>
""",
                ),
                Section(
                    id="ldl-yuksekse-ne-olur",
                    level=2,
                    heading="LDL yüksekse ne anlama gelir?",
                    body_html="""
<p>LDL sonucunuz, yaşınıza ve cinsiyetinize bakılmaksızın, <strong>diğer risk faktörlerinizle birlikte</strong> değerlendirilir.
Örneğin 140 mg/dL LDL değeri:</p>
<ul>
  <li>Hiçbir ek risk faktörü olmayan genç bir bireyde <strong>sınırlı risk artışı</strong> anlamına gelebilir.</li>
  <li>Hipertansiyon, diyabet ve sigara öyküsü olan bir kişide ise <strong>agresif tedavi gerektiren belirgin bir risk</strong> göstergesi olabilir.</li>
</ul>
<p>Bu yüzden, sadece “yüksek” veya “düşük” etiketine değil, <strong>toplam kardiyovasküler riskinize</strong> odaklanmak önemlidir.</p>
""",
                ),
                Section(
                    id="ldl-nasil-dusurulur",
                    level=2,
                    heading="LDL kolesterol nasıl düşürülür?",
                    body_html="""
<p>Hedef LDL düzeyine ulaşmak için genellikle üç eksen birlikte kullanılır:</p>
<ol>
  <li><strong>Beslenme düzeni</strong>: Doymuş yağ (işlenmiş et ürünleri, tereyağı, bazı paketli gıdalar) ve trans yağları azaltmak,
      sebze, tam tahıl ve zeytinyağı ağırlıklı Akdeniz tipi beslenmeyi öne çıkarmak.</li>
  <li><strong>Hareket</strong>: Haftada en az 150 dakika orta tempolu egzersiz (hızlı yürüyüş gibi) hem LDL&apos;yi düşürmeye
      hem de HDL&apos;yi (iyi kolesterol) desteklemeye yardımcı olabilir.</li>
  <li><strong>Gerektiğinde ilaç tedavisi</strong>: Statinler ve hekiminizin seçeceği diğer ilaçlar, özellikle yüksek ve çok yüksek
      riskli gruplarda LDL hedeflerine ulaşmada kritik rol oynar.</li>
</ol>
<p>Herhangi bir ilaç veya takviye başlamadan önce mutlaka doktorunuza danışın. Bu yazı, tıbbi değerlendirme ve tedavinin yerini
almak için değil, raporunuzu <strong>daha bilinçli şekilde</strong> okumanız için hazırlanmıştır.</p>
""",
                ),
            ],
            # Diğer diller için içerikler, Türkçe metnin anlamını koruyacak şekilde kısaltılmış ve sadeleştirilmiş versiyonlardır.
            "en": [
                Section(
                    id="ldl-what",
                    level=2,
                    heading="What is LDL cholesterol?",
                    body_html="""
<p>Cholesterol is a fat‑like substance your body uses to build cell membranes and hormones. In the bloodstream it travels inside
lipoprotein particles. LDL (low‑density lipoprotein) delivers cholesterol towards the artery wall and is therefore often called
the “bad cholesterol”.</p>
<p>When LDL stays high for many years it accelerates atherosclerosis – fatty build‑up in the arteries – which increases the risk of
heart attack and stroke.</p>
""",
                ),
                Section(
                    id="ldl-targets",
                    level=2,
                    heading="Target LDL levels by risk group",
                    body_html="""
<p>Modern guidelines do not use a single “normal” LDL value. Instead they define <strong>target ranges based on overall cardiovascular risk</strong>:</p>
<ul>
  <li><strong>Low / moderate risk</strong>: often aim for LDL <strong>below 130 mg/dL</strong>.</li>
  <li><strong>High risk</strong> (diabetes, hypertension, smoking, strong family history): usually aim for
      <strong>below 100 mg/dL</strong>.</li>
  <li><strong>Very high risk</strong> (previous heart attack, stent, stroke): targets may be <strong>below 70 mg/dL or even 55 mg/dL</strong>.</li>
</ul>
<p>The reference range printed on your report is usually a generic interval. Your personal goal can be lower than that, which is
why LDL must always be interpreted together with your doctor.</p>
""",
                ),
                Section(
                    id="ldl-high",
                    level=2,
                    heading="What if your LDL is high?",
                    body_html="""
<p>An LDL value is never interpreted in isolation. The same number – for example <strong>140 mg/dL</strong> – can mean different things:</p>
<ul>
  <li>In a young person with no other risk factors it may represent a <strong>modest risk</strong>.</li>
  <li>In someone with diabetes, high blood pressure and smoking it may signal a <strong>clearly increased risk requiring aggressive treatment</strong>.</li>
</ul>
<p>Rather than focusing only on “high” or “low”, discuss your <strong>global cardiovascular risk</strong> and target range with your clinician.</p>
""",
                ),
                Section(
                    id="ldl-lower",
                    level=2,
                    heading="How to lower LDL cholesterol",
                    body_html="""
<p>Reaching your LDL target usually involves three pillars:</p>
<ol>
  <li><strong>Nutrition</strong>: reduce saturated and trans fats, favour vegetables, whole grains and olive‑oil‑based meals (Mediterranean pattern).</li>
  <li><strong>Physical activity</strong>: at least 150 minutes of moderate exercise per week can help lower LDL and support HDL (“good” cholesterol).</li>
  <li><strong>Medication when needed</strong>: statins and other drugs chosen by your doctor are essential in high and very‑high‑risk groups.</li>
</ol>
<p>This article is for information only and <strong>does not replace medical advice</strong>. Always consult your doctor before
starting or changing any treatment.</p>
""",
                ),
            ],
            # Diğer diller için daha kısa ama anlamdaş içerikler
            "de": [
                Section(
                    id="ldl-was",
                    level=2,
                    heading="Was ist LDL‑Cholesterin?",
                    body_html="""
<p>LDL transportiert Cholesterin in Richtung Gefäßwand und wird deshalb oft als „schlechtes Cholesterin“ bezeichnet.
Bleibt der Wert über Jahre erhöht, fördert dies Ablagerungen in den Arterien und steigert das Risiko für Herzinfarkt und Schlaganfall.</p>
""",
                ),
                Section(
                    id="ldl-zielwerte",
                    level=2,
                    heading="Typische Zielwerte nach Risikogruppe",
                    body_html="""
<ul>
  <li><strong>Niedriges / mittleres Risiko</strong>: häufig Ziel <strong>&lt; 130 mg/dL</strong></li>
  <li><strong>Hohes Risiko</strong>: meist Ziel <strong>&lt; 100 mg/dL</strong></li>
  <li><strong>Sehr hohes Risiko</strong>: Ziel <strong>&lt; 70 mg/dL</strong>, teils sogar <strong>&lt; 55 mg/dL</strong></li>
</ul>
<p>Ihr persönliches Ziel hängt von Begleiterkrankungen und Vorerkrankungen ab und sollte mit der behandelnden Ärztin / dem Arzt besprochen werden.</p>
""",
                ),
            ],
            # Kalan diller için EN içeriğini sadeleştirilmiş şekilde kullanıyoruz
        },
    )


_LDL_ARTICLE = _article_ldl()


def _article_kan_tahlili_nasil_okunur() -> Article:
    """Kan tahlili nasıl okunur — ultra premium: tanım kutuları, örnekler, stealth tarzı."""
    published = date(2025, 3, 4)
    cover = "/static/images/blog/how-to-read-blood-test-results.png"

    return Article(
        id="kan-tahlili-nasil-okunur",
        published_at=published,
        read_minutes=8,
        cover_image=cover,
        category={
            "tr": "Rehber",
            "en": "Guide",
            "de": "Leitfaden",
            "it": "Guida",
            "es": "Guía",
            "fr": "Guide",
            "he": "מדריך",
            "ar": "دليل",
            "hi": "गाइड",
            "el": "Οδηγός",
            "cs": "Průvodce",
            "sr": "Водич",
        },
        slugs={
            "tr": "kan-tahlili-nasil-okunur",
            "en": "how-to-read-blood-test-results",
            "de": "blutwerte-lesen",
            "it": "come-leggere-esami-del-sangue",
            "es": "como-leer-analisis-sangre",
            "fr": "lire-resultats-prise-de-sang",
            "he": "how-to-read-blood-test",
            "ar": "how-to-read-blood-test",
            "hi": "blood-test-kaise-padhe",
            "el": "how-to-read-blood-test",
            "cs": "jak-cist-vysledky-krve",
            "sr": "kako-citati-krvnu-analizu",
        },
        titles={
            "tr": "Kan tahlili nasıl okunur? Adım adım rehber",
            "en": "How to Read a Blood Test Report",
            "de": "Blutbefund lesen: Schritt-für-Schritt",
            "it": "Come leggere gli esami del sangue",
            "es": "Cómo leer un análisis de sangre",
            "fr": "Comment lire une prise de sang",
            "he": "איך לקרוא תוצאות בדיקת דם",
            "ar": "كيف تقرأ تحليل الدم",
            "hi": "ब्लड टेस्ट रिपोर्ट कैसे पढ़ें",
            "el": "Πώς να διαβάσετε τα αποτελέσματα αίματος",
            "cs": "Jak číst výsledky krevního testu",
            "sr": "Како читати крвну анализу",
        },
        subtitles={
            "tr": "Tahlil sonucu kâğıdındaki terimleri, referans aralıklarını ve değerlerin ne anlama geldiğini sade bir dille açıklıyoruz.",
            "en": "A step-by-step guide to understanding values, units, and reference ranges.",
            "de": "Verständliche Erklärung von Begriffen, Referenzbereichen und Werten im Laborbefund.",
            "it": "Guida chiara a termini, intervalli di riferimento e valori sul referto.",
            "es": "Guía clara de términos, rangos de referencia y valores en el informe.",
            "fr": "Guide clair des termes, fourchettes de référence et valeurs sur le résultat.",
            "he": "הסבר ברור על המונחים, טווחי הנורמה והמספרים בתוצאות הבדיקה.",
            "ar": "دليل واضح للمصطلحات ونطاقات المرجع والقيم في التقرير.",
            "hi": "रिपोर्ट में दिखने वाले शब्दों, रेफरेंस रेंज और संख्याओं की सरल व्याख्या।",
            "el": "Ξεκάθαρος οδηγός για τους όρους, τα διαστήματα αναφοράς και τις τιμές στην ανακοίνωση.",
            "cs": "Přehled pojmů, referenčních rozmezí a hodnot na laboratorním protokolu.",
            "sr": "Јасан водич кроз појмове, референтне вредности и бројеве на извештају.",
        },
        excerpts={
            "tr": "Referans aralığı, birimler ve sonuç kâğıdındaki sütunlar: tahlilinizi doğru yorumlamak için bilmeniz gerekenler.",
            "en": "Blood test reports can look confusing at first—numbers, abbreviations, and reference ranges everywhere. This guide explains what you’re seeing, how to interpret high/low flags, and what to check before you worry.",
            "de": "Referenzbereiche, Einheiten und Spalten im Befund – das Wichtigste für die Einordnung Ihrer Werte.",
            "it": "Intervalli di riferimento, unità e colonne del referto: cosa serve per leggere bene le analisi.",
            "es": "Rangos de referencia, unidades y columnas del informe: lo esencial para interpretar tu análisis.",
            "fr": "Fourchettes de référence, unités et colonnes du résultat : l’essentiel pour interpréter votre bilan.",
            "he": "טווחי נורמה, יחידות ועמודות בדף התוצאות – מה שצריך כדי להבין את הבדיקה.",
            "ar": "نطاقات المرجع والوحدات والأعمدة في التقرير: ما تحتاج معرفته لفهم التحليل.",
            "hi": "रेफरेंस रेंज, यूनिट और रिपोर्ट के कॉलम: ब्लड टेस्ट समझने के लिए जरूरी बातें।",
            "el": "Διαστήματα αναφοράς, μονάδες και στήλες στην ανακοίνωση: ό,τι χρειάζεστε για να ερμηνεύσετε τη διαζήτηση.",
            "cs": "Referenční rozmezí, jednotky a sloupce na protokolu: co potřebujete k interpretaci výsledků.",
            "sr": "Референтни опсези, јединице и колоне у извештају: све што треба да протумачите анализу.",
        },
        seo_titles={
            "tr": "Kan Tahlili Nasıl Okunur? Referans Aralığı ve Değerler Rehberi",
            "en": "How to Read Blood Test Results (Step-by-Step) | NoryaAl",
            "de": "Blutbefund lesen: Referenzbereich und Werte verstehen",
            "it": "Come leggere gli esami del sangue | Guida valori e riferimenti",
            "es": "Cómo leer un análisis de sangre | Guía de valores y referencia",
            "fr": "Comment lire une prise de sang | Guide des valeurs et références",
            "he": "איך לקרוא תוצאות בדיקת דם | מדריך טווחי נורמה",
            "ar": "كيف تقرأ تحليل الدم | دليل القيم ونطاق المرجع",
            "hi": "ब्लड टेस्ट रिपोर्ट कैसे पढ़ें | रेफरेंस रेंज गाइड",
            "el": "Πώς να διαβάσετε τα εξεταστικά αίματος | Οδηγός τιμών",
            "cs": "Jak číst krevní výsledky | Referenční rozmezí a hodnoty",
            "sr": "Како читати крвну анализу | Водич референтних вредности",
        },
        seo_descriptions={
            "tr": "Kan tahlili sonucu kâğıdında referans aralığı, birimler ve değerlerin anlamı. Adım adım, sade dilde rehber.",
            "en": "Learn how to read a blood test report: values, units, reference ranges, high/low flags, and common panels like CBC and lipids. A clear, step-by-step guide.",
            "de": "Was Referenzbereich, Einheiten und Werte im Blutbefund bedeuten. Schritt-für-Schritt, verständlich.",
            "it": "Cosa significano intervallo di riferimento, unità e valori sul referto. Guida passo passo in linguaggio semplice.",
            "es": "Qué significan rango de referencia, unidades y valores en el análisis. Guía paso a paso en lenguaje claro.",
            "fr": "Fourchette de référence, unités et valeurs sur la prise de sang : explications. Guide pas à pas en langage simple.",
            "he": "מה משמעות טווח הנורמה, היחידות והערכים בתוצאות הבדיקה. מדריך שלב-אחר-שלב בשפה פשוטה.",
            "ar": "معنى نطاق المرجع والوحدات والقيم في تحليل الدم. دليل خطوة بخطوة بلغة واضحة.",
            "hi": "ब्लड टेस्ट रिपोर्ट में रेफरेंस रेंज, यूनिट और वैल्यू का मतलब। सरल भाषा में स्टेप-बाय-स्टेप गाइड।",
            "el": "Τι σημαίνουν το διάστημα αναφοράς, οι μονάδες και οι τιμές στο αποτέλεσμα. Οδηγός βήμα-βήμα με απλή γλώσσα.",
            "cs": "Co znamená referenční rozmezí, jednotky a hodnoty na protokolu. Přehledný krok-za-krokem průvodce.",
            "sr": "Шта значи референтни опсег, јединице и вредности на анализи. Водич корак-по-корак јасним језиком.",
        },
        sections_by_lang={
            "tr": [
                Section(
                    id="tahlil-sonucu-nedir",
                    level=2,
                    heading="Kan tahlili sonucu nedir?",
                    body_html="""
<p>Kan tahlili (laboratuvar testi), kandaki belirli maddelerin miktarını veya varlığını ölçer. Sonuç kâğıdında her parametre için
bir <strong>sayı</strong>, çoğu zaman bir <strong>birim</strong> (ör. mg/dL, mmol/L) ve sıklıkla bir <strong>referans aralığı</strong> yer alır.</p>
<div class="blog-definition">
  <p><strong>Kan tahlili:</strong> Alınan kan örneğinin laboratuvarda incelenmesiyle elde edilen; şeker, kolesterol, vitamin, mineral,
  enzim veya hormon gibi değerlerin sayısal sonuçlarını gösteren rapor. Teşhis koymak için tek başına yeterli değildir;
  hekimin klinik değerlendirmesiyle birlikte yorumlanır.</p>
</div>
<p>Bu yazıda, sonuç kâğıdını okurken karşınıza çıkan terimleri ve sayıları nasıl anlayacağınızı adım adım ele alıyoruz.</p>
""",
                ),
                Section(
                    id="referans-araligi",
                    level=2,
                    heading="Referans aralığı ne anlama gelir?",
                    body_html="""
<p>Referans aralığı (normal aralık), sağlıklı bir popülasyonda o parametre için kabul edilen alt ve üst sınırlardır. Sonuç bu
aralığın <strong>içindeyse</strong> çoğu kılavuzda “normal sınırlarda” kabul edilir; <strong>dışındaysa</strong> düşük veya yüksek olarak işaretlenebilir.</p>
<div class="blog-definition">
  <p><strong>Referans aralığı:</strong> Laboratuvarın veya kılavuzların, “sağlıklı” kabul edilen bir grupta yapılan ölçümlere dayanarak
  belirlediği alt ve üst sınırlar. Örneğin “LDL 70–130 mg/dL” yazıyorsa, bu aralık o laboratuvar için kullanılan referans değerleridir.</p>
</div>
<div class="blog-example">
  <p><strong>Örnek:</strong> Sonuç kâğıdında <strong>Hemoglobin: 14,2 g/dL</strong> ve yanında <strong>Referans: 12–16 g/dL</strong> görüyorsanız,
  14,2 bu aralığın içinde olduğu için değer “normal sınırlarda” kabul edilir. 10 g/dL yazsaydı, referansın altında kalırdı ve
  “düşük” olarak yorumlanırdı.</p>
</div>
<p>Referans aralıkları laboratuvardan laboratuvara, cinsiyet ve yaş gruplarına göre hafifçe değişebilir. Bu yüzden her zaman
kâğıtta yazan aralığa göre yorum yapılır.</p>
""",
                ),
                Section(
                    id="sonuc-kagidinda-neler-var",
                    level=2,
                    heading="Sonuç kâğıdında neler bulunur?",
                    body_html="""
<p>Tipik bir kan tahlili sonuç sayfasında şu sütunlar yer alır:</p>
<ul>
  <li><strong>Parametre adı</strong>: Ölçülen değerin adı (örn. LDL kolesterol, Açlık glukozu, Hemoglobin).</li>
  <li><strong>Sonuç / Değer</strong>: Sizin ölçümünüz (sayı + birim).</li>
  <li><strong>Referans aralığı</strong>: O laboratuvar için kullanılan normal alt–üst sınırlar.</li>
  <li><strong>Birim</strong>: mg/dL, mmol/L, g/dL, U/L vb. Değeri doğru yorumlamak için birime bakmak gerekir.</li>
</ul>
<p>Bazı laboratuvarlar “Normal / Düşük / Yüksek” gibi bir etiket de ekler. Bu etiket, sonucun referans aralığına göre otomatik
üretilir; ancak sizin için “hedef” değer risk faktörlerinize göre farklı olabileceği için, nihai yorumu hekiminizle yapmanız önemlidir.</p>
""",
                ),
                Section(
                    id="yuksek-dusuk-deger",
                    level=2,
                    heading="Değer yüksek veya düşük çıkarsa",
                    body_html="""
<p>Bir değer referans aralığının <strong>dışında</strong> çıktığında, bu mutlaka “hastalık” anlamına gelmez. Geçici enfeksiyon, açlık süresi,
kullanılan ilaçlar veya laboratuvar tekniği gibi faktörler sonucu etkileyebilir. Hekiminiz, sizin öykünüz ve diğer tetkiklerle birlikte
bu sonucun anlamını değerlendirir; gerekirse tekrar test veya ek inceleme önerebilir.</p>
<p>Bu rehber, tahlil kâğıdındaki terimleri ve sayıları <strong>daha iyi anlamanız</strong> için hazırlanmıştır. Teşhis veya tedavi kararı yerine
geçmez; tüm sağlık kararlarında hekiminize danışınız.</p>
""",
                ),
            ],
            "en": [
                Section(
                    id="safety-note",
                    level=2,
                    heading="Before you start: safety note",
                    body_html="""
<section>
  <p><strong>Important:</strong> This guide is educational and does not replace medical advice. If you have severe symptoms, very abnormal values, or concerns, contact a clinician.</p>
</section>
""",
                ),
                Section(
                    id="what-is-report",
                    level=2,
                    heading="What is a blood test report?",
                    body_html="""
<section>
  <p>A blood test report (lab report) lists measurements from your blood sample. Each line usually includes: a <strong>test name</strong>, your <strong>value</strong>, the <strong>unit</strong>, and a <strong>reference range</strong> (sometimes called “normal range”).</p>
  <p>Different labs may use different methods and ranges, so always interpret results <strong>with the lab’s own reference range</strong>.</p>
</section>
""",
                ),
                Section(
                    id="step-1-context",
                    level=2,
                    heading="Step 1 — Start with the context",
                    body_html="""
<section>
  <ul>
    <li><strong>Why was the test ordered?</strong> Screening, symptoms, follow-up, medication monitoring?</li>
    <li><strong>Were you fasting?</strong> Lipids and glucose-related tests may be affected.</li>
    <li><strong>Recent illness, exercise, alcohol, supplements?</strong> These can shift values.</li>
    <li><strong>Timing matters:</strong> A single result is a snapshot—trends are often more meaningful.</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="step-2-four-things",
                    level=2,
                    heading="Step 2 — Understand the four things on each line",
                    body_html="""
<section>
  <ol>
    <li><strong>Test name:</strong> what was measured (e.g., Hemoglobin, ALT, Ferritin).</li>
    <li><strong>Your value:</strong> the number reported.</li>
    <li><strong>Unit:</strong> how it’s measured (e.g., mg/dL, mmol/L, U/L).</li>
    <li><strong>Reference range:</strong> expected range for a population under lab conditions.</li>
  </ol>
  <blockquote>
    <p><strong>Pro tip:</strong> Being slightly outside the range doesn’t automatically mean disease. It can reflect hydration, recent activity, timing, or lab variation.</p>
  </blockquote>
</section>
""",
                ),
                Section(
                    id="step-3-reference-range",
                    level=2,
                    heading="Step 3 — What does “reference range” actually mean?",
                    body_html="""
<section>
  <p>A reference range is often built so that most healthy people fall inside it (commonly around 95%). That means some healthy people will naturally fall slightly below or above.</p>
  <p>Reference ranges also vary by <strong>age</strong>, <strong>sex</strong>, pregnancy status, altitude, and lab method.</p>
</section>
""",
                ),
                Section(
                    id="step-4-flags",
                    level=2,
                    heading="Step 4 — High / Low flags: when to pay attention",
                    body_html="""
<section>
  <p>Reports may show flags like <strong>H</strong> (high) or <strong>L</strong> (low). Use these flags as a signal to look closer, not a diagnosis.</p>
  <ul>
    <li><strong>Mild:</strong> close to the range — often re-check or consider context.</li>
    <li><strong>Moderate:</strong> clearly out of range — consider repeat plus clinical correlation.</li>
    <li><strong>Severe:</strong> far out of range — follow lab or clinician instructions promptly.</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="step-5-panels",
                    level=2,
                    heading="Step 5 — Learn the common panels first",
                    body_html="""
<section>
  <h3>Complete Blood Count (CBC)</h3>
  <p>CBC describes blood cells and oxygen-carrying capacity. Common items include:</p>
  <ul>
    <li><strong>WBC:</strong> white blood cells (immune response)</li>
    <li><strong>RBC / HGB / HCT:</strong> red cells and oxygen transport</li>
    <li><strong>PLT:</strong> platelets (clotting)</li>
    <li><strong>MCV / MCH / MCHC / RDW:</strong> red cell size and hemoglobin patterns</li>
  </ul>

  <h3>Basic metabolic / chemistry</h3>
  <ul>
    <li><strong>Glucose:</strong> blood sugar</li>
    <li><strong>Creatinine / eGFR:</strong> kidney function indicators</li>
    <li><strong>Sodium / Potassium:</strong> electrolytes</li>
  </ul>

  <h3>Liver enzymes</h3>
  <ul>
    <li><strong>ALT / AST:</strong> liver cell stress or injury markers (non-specific)</li>
    <li><strong>ALP / GGT / Bilirubin:</strong> bile flow and related pathways</li>
  </ul>

  <h3>Lipids</h3>
  <ul>
    <li><strong>Total Cholesterol, LDL, HDL, Triglycerides</strong></li>
    <li>Interpret in the context of risk factors and fasting status.</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="step-6-units",
                    level=2,
                    heading="Step 6 — Units and conversions",
                    body_html="""
<section>
  <p>Some results appear in different units depending on the country or lab (for example, glucose in mg/dL versus mmol/L). If you compare results between reports, confirm units match before assuming there is a change.</p>
</section>
""",
                ),
                Section(
                    id="step-7-trends",
                    level=2,
                    heading="Step 7 — Trends beat single numbers",
                    body_html="""
<section>
  <p>If you have multiple tests over time, look for:</p>
  <ul>
    <li><strong>Direction:</strong> improving, stable, or worsening</li>
    <li><strong>Speed:</strong> sudden shifts usually matter more</li>
    <li><strong>Consistency:</strong> repeat abnormal results are more significant than a one-off outlier</li>
  </ul>
</section>
""",
                ),
                Section(
                    id="when-to-seek-help",
                    level=2,
                    heading="When to seek medical advice urgently",
                    body_html="""
<section>
  <p>Seek urgent care if you have severe symptoms such as chest pain, fainting, shortness of breath, or confusion, or if your lab result is marked as critical and the lab or clinic advises immediate action.</p>
</section>
""",
                ),
                Section(
                    id="try-clearer-report",
                    level=2,
                    heading="Try a clearer report view",
                    body_html="""
<section>
  <p>If you want a more structured overview, you can upload your lab PDF and get a clean, readable summary with key terms and reference ranges.</p>
  <p><a href="/analyze">Analyze your blood test →</a></p>
</section>
""",
                ),
            ],
        },
    )


_KAN_TAHLILI_ARTICLE = _article_kan_tahlili_nasil_okunur()


def _article_ferritin() -> Article:
    """Ferritin: low/high meaning, reference ranges, when to see a doctor."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/ferritin-hero.png"
    return Article(
        id="ferritin-what-it-means",
        published_at=published,
        read_minutes=10,
        cover_image=cover,
        category={
            "en": "Biomarkers",
            "de": "Biomarker",
            "it": "Biomarcatori",
            "fr": "Biomarqueurs",
        },
        slugs={
            "en": "ferritin-what-it-means",
            "de": "ferritin-verstehen",
            "it": "ferritina-cosa-significa",
            "fr": "ferritine-taux-bas-eleves",
        },
        titles={
            "en": "Ferritin Explained: What Low or High Levels Mean (and What to Do Next)",
            "de": "Ferritin verstehen: Was niedrige oder hohe Werte bedeuten",
            "it": "Ferritina: cosa significa averla bassa o alta",
            "fr": "Ferritine : que signifient des taux bas ou élevés",
        },
        subtitles={
            "en": "A clear guide to ferritin, iron stores, reference ranges, common causes of low or high results, and when to see a doctor.",
            "de": "Ein Überblick über Ferritin, Eisenspeicher, Referenzbereiche, häufige Ursachen für niedrige oder hohe Werte und wann Sie zum Arzt sollten.",
            "it": "Guida chiara su ferritina, riserve di ferro, intervalli di riferimento, cause comuni di valori bassi o alti e quando rivolgersi al medico.",
            "fr": "Guide clair sur la ferritine, les réserves en fer, les fourchettes de référence, les causes fréquentes de taux bas ou élevés et quand consulter.",
        },
        excerpts={
            "en": "Ferritin reflects your body’s iron stores. Low or high levels can have many causes; interpretation should be done with a clinician and other tests.",
            "de": "Ferritin spiegelt die Eisenspeicher wider. Niedrige oder hohe Werte können viele Ursachen haben; die Einordnung erfolgt mit dem Arzt und weiteren Tests.",
            "it": "La ferritina riflette le riserve di ferro. Valori bassi o alti possono avere molte cause; l’interpretazione va fatta con il medico e altri esami.",
            "fr": "La ferritine reflète les réserves en fer. Un taux bas ou élevé peut avoir de nombreuses causes ; l’interprétation se fait avec un médecin et d’autres examens.",
        },
        seo_titles={
            "en": "Ferritin Explained: Low vs High Levels, Reference Ranges & Next Steps",
            "de": "Ferritin: Niedrige und hohe Werte, Referenzbereich, Ursachen",
            "it": "Ferritina: valori bassi e alti, intervalli di riferimento e cosa fare",
            "fr": "Ferritine : taux bas ou élevé, fourchettes de référence et suites",
        },
        seo_descriptions={
            "en": "Understand ferritin and iron stores. What low or high ferritin means, common causes, reference ranges, when to see a doctor, and what to do next.",
            "de": "Ferritin und Eisenspeicher verstehen. Bedeutung niedriger/hoher Werte, Ursachen, Referenzbereich, wann zum Arzt und was Sie tun können.",
            "it": "Capire ferritina e riserve di ferro. Cosa significano valori bassi o alti, cause comuni, intervalli di riferimento, quando rivolgersi al medico.",
            "fr": "Comprendre la ferritine et les réserves en fer. Taux bas ou élevé, causes fréquentes, fourchettes de référence, quand consulter et quoi faire.",
        },
        sections_by_lang={
            "en": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="What is ferritin?",
                    body_html="""
<p>Ferritin is a protein that stores iron and releases it in a controlled way when the body needs it. Measured in blood, ferritin is the most practical indicator of your body’s <strong>iron stores</strong>. It is not the same as “serum iron” (the iron circulating in the blood at the moment of the test), which can vary with meals and time of day.</p>
<p>Low ferritin usually suggests depleted iron stores and may point to iron deficiency if other causes are ruled out. High ferritin can reflect excess iron storage, but it is also an <strong>acute-phase reactant</strong>: it often rises with inflammation, infection, or liver conditions, so a high value does not automatically mean too much iron. Interpretation should always be done together with your doctor and, when needed, additional tests.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritin vs iron vs transferrin vs TSAT",
                    body_html="""
<p>These tests are often ordered together to assess iron status. A short overview:</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Test</th><th class="border border-slate-300 px-3 py-2 text-left">What it reflects</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritin</strong></td><td class="border border-slate-300 px-3 py-2">Iron stores (storage form). Best single marker for deficiency.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Serum iron</strong></td><td class="border border-slate-300 px-3 py-2">Iron in circulation at time of draw. Varies with diet and time of day.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrin / TIBC</strong></td><td class="border border-slate-300 px-3 py-2">Iron-carrying capacity. Often high when stores are low.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>TSAT</strong></td><td class="border border-slate-300 px-3 py-2">Transferrin saturation. Low in deficiency; very high may suggest overload.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Low ferritin: causes and symptoms",
                    body_html="""
<p><strong>Common causes</strong> of low ferritin include: blood loss (heavy periods, digestive bleeding, surgery), low dietary intake or poor absorption (e.g. coeliac disease, gastric surgery), increased needs (pregnancy, growth, intense training), and chronic inflammation affecting absorption. More than one factor can apply at once.</p>
<p><strong>Common symptoms</strong> that may be associated with low iron stores include fatigue, weakness, pale skin, shortness of breath on exertion, dizziness, cold hands and feet, brittle nails, and hair loss. These are non-specific: they can have many other causes. <strong>Symptoms alone do not establish a diagnosis</strong>; they must be interpreted together with blood tests and clinical history by a doctor.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="High ferritin: causes and acute-phase reaction",
                    body_html="""
<p><strong>Common causes</strong> of elevated ferritin include: inflammation or infection (ferritin is an acute-phase reactant and often rises even when iron stores are normal), fatty liver disease, alcohol use, metabolic syndrome, obesity, and in some cases hereditary haemochromatosis or other iron overload conditions. Liver damage or chronic disease can also raise ferritin.</p>
<p>Because <strong>ferritin is an acute-phase reactant</strong>, it often increases during illness, infection, or inflammation. A high result does not necessarily mean excess iron; your doctor will consider CRP, serum iron, TIBC, TSAT, and sometimes imaging or genetic testing to clarify.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="What ranges are “normal”?",
                    body_html="""
<p>Reference ranges for ferritin <strong>differ by laboratory</strong> (method and population). Always use the range printed on your own report. As a rough guide only: in many labs, approximate ranges are around <strong>12–150 ng/mL for adult women</strong> and <strong>30–300 ng/mL (or higher) for adult men</strong>. Values may be lower in menstruating women and higher in older adults. These figures are illustrative; your lab’s reference is the one that applies to your result.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="When to see a doctor",
                    body_html="""
<p>See a doctor if: ferritin is very low or very high; you have low haemoglobin (anaemia) or symptoms such as unexplained fatigue, shortness of breath, or dizziness; you have fever, weight loss, or signs of liver disease; or other blood tests (e.g. liver enzymes) are abnormal. Early discussion with a clinician allows proper work-up (e.g. CBC, CRP, serum iron, TIBC, TSAT, B12, folate) and, if needed, treatment or referral.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="What might happen next",
                    body_html="""
<p>Depending on your result and history, your doctor may order further tests: full blood count (CBC), CRP, serum iron, TIBC, TSAT, vitamin B12, folate, and sometimes tests for coeliac disease or digestive bleeding. <strong>Lifestyle and diet</strong>: if deficiency is confirmed, iron-rich foods and, if prescribed, supplements can help; avoid self-dosing high amounts. For high ferritin, the cause must be clarified first (inflammation, liver, metabolic, or genetic); diet and lifestyle advice will depend on that. Always follow your doctor’s recommendations.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Frequently asked questions",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">What is a “normal” ferritin level?</h3>
<p>“Normal” depends on your lab’s reference range, age, and sex. Use the range on your report; your doctor can say whether your value is appropriate for you.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can low ferritin cause hair loss?</h3>
<p>Low iron stores are sometimes associated with hair thinning or loss, but many other factors (hormones, stress, diet) also play a role. Correcting deficiency may help in some people; a doctor can advise.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What raises ferritin besides iron?</h3>
<p>Inflammation, infection, liver disease, alcohol, metabolic syndrome, and certain medications can raise ferritin without true iron overload. That’s why high ferritin is interpreted together with other tests.</p>
<h3 class="text-base font-semibold mt-4 mb-1">How long until supplements affect ferritin?</h3>
<p>If you are prescribed iron for deficiency, ferritin may start to rise over several weeks; full repletion can take months. Follow your doctor’s dosing and repeat-test schedule.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is ferritin tested fasting?</h3>
<p>Ferritin is usually not strongly affected by a recent meal, but your lab may request fasting for a panel that includes glucose or lipids. Follow the instructions given for your blood draw.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can I interpret ferritin alone?</h3>
<p>Ferritin is best interpreted with clinical context and often with serum iron, TIBC, TSAT, and sometimes CRP or other tests. Your doctor can give a proper interpretation.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Disclaimer",
                    body_html="""
<p><strong>This content is for information only and does not constitute medical advice.</strong> Always discuss your results and symptoms with a doctor. Do not start or change supplements or treatment based solely on this article.</p>
""",
                ),
            ],
            "de": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="Was ist Ferritin?",
                    body_html="""
<p>Ferritin ist ein Speichereiweiß für Eisen, das bei Bedarf kontrolliert abgegeben wird. Im Blut gemessen, ist Ferritin der praktischste Indikator für Ihre <strong>Eisenspeicher</strong>. Es ist nicht dasselbe wie „Serumeisen“ (das zum Zeitpunkt der Abnahme zirkulierende Eisen), das mit Mahlzeiten und Tageszeit schwanken kann.</p>
<p>Niedriges Ferritin spricht oft für leere Eisenspeicher und kann auf einen Eisenmangel hindeuten, wenn andere Ursachen ausgeschlossen sind. Hohes Ferritin kann auf zu viel gespeichertes Eisen hindeuten, ist aber auch ein <strong>Akute-Phase-Protein</strong>: Es steigt oft bei Entzündung, Infektion oder Lebererkrankung – ein hoher Wert bedeutet also nicht automatisch Eisenüberladung. Die Einordnung erfolgt immer gemeinsam mit dem Arzt und gegebenenfalls weiteren Tests.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritin vs. Eisen vs. Transferrin vs. TSAT",
                    body_html="""
<p>Diese Werte werden oft gemeinsam bestimmt. Kurzüberblick:</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Parameter</th><th class="border border-slate-300 px-3 py-2 text-left">Bedeutung</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritin</strong></td><td class="border border-slate-300 px-3 py-2">Eisenspeicher. Bester Einzelmarker bei Mangel.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Serumeisen</strong></td><td class="border border-slate-300 px-3 py-2">Zirkulierendes Eisen zum Abnahmezeitpunkt. Variiert mit Ernährung und Tageszeit.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrin / TIBC</strong></td><td class="border border-slate-300 px-3 py-2">Eisentransportkapazität. Oft erhöht bei niedrigen Speichern.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>TSAT</strong></td><td class="border border-slate-300 px-3 py-2">Transferrinsättigung. Niedrig bei Mangel; sehr hoch kann auf Überladung hindeuten.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Niedriges Ferritin: Ursachen und Symptome",
                    body_html="""
<p><strong>Häufige Ursachen</strong> sind: Blutverlust (starke Regelblutung, Magen-Darm-Blutungen, OP), geringe Aufnahme oder schlechte Resorption (z. B. Zöliakie, Magen-OP), erhöhter Bedarf (Schwangerschaft, Wachstum, intensiver Sport), chronische Entzündung. Mehrere Faktoren können zusammenspielen.</p>
<p><strong>Mögliche Symptome</strong> bei niedrigen Eisenspeichern: Müdigkeit, Schwäche, blasse Haut, Atemnot bei Belastung, Schwindel, kalte Hände/Füße, brüchige Nägel, Haarausfall. Diese sind unspezifisch und können viele andere Ursachen haben. <strong>Symptome allein stellen keine Diagnose</strong>; die Bewertung erfolgt durch den Arzt anhand von Blutwerten und Anamnese.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="Hohes Ferritin: Ursachen und Akute-Phase-Reaktion",
                    body_html="""
<p><strong>Häufige Ursachen</strong> erhöhten Ferritins: Entzündung oder Infektion (Ferritin ist ein Akute-Phase-Protein und steigt oft auch bei normalen Speichern), Fettleber, Alkohol, metabolisches Syndrom, Adipositas, in Einzelfällen hereditäre Hämochromatose oder andere Eisenüberladung. Auch Leberschaden oder chronische Erkrankung können Ferritin anheben.</p>
<p>Da <strong>Ferritin ein Akute-Phase-Protein ist</strong>, steigt es bei Krankheit, Infekt oder Entzündung oft an. Ein hoher Wert bedeutet nicht zwingend Eisenüberschuss; der Arzt zieht CRP, Serumeisen, TIBC, TSAT und ggf. Bildgebung oder Genetik zur Klärung heran.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="Welche Bereiche gelten als „normal“?",
                    body_html="""
<p>Referenzbereiche für Ferritin <strong>unterscheiden sich je nach Labor</strong> (Methode und Population). Orientieren Sie sich immer am Bereich auf Ihrem Befund. Nur zur groben Einordnung: In vielen Laboren liegen die Bereiche etwa bei <strong>12–150 ng/mL für erwachsene Frauen</strong> und <strong>30–300 ng/mL (oder höher) für Männer</strong>. Bei menstruierenden Frauen oft niedriger, bei Älteren teils höher. Diese Angaben sind nur Richtwerte; maßgeblich ist der Referenzbereich Ihres Labors.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Wann zum Arzt?",
                    body_html="""
<p>Gehen Sie zum Arzt, wenn: Ferritin stark erniedrigt oder stark erhöht ist; Sie niedrigen Hämoglobinwert (Anämie) oder Symptome wie unklare Müdigkeit, Atemnot oder Schwindel haben; Fieber, Gewichtsverlust oder Hinweise auf Lebererkrankung bestehen; oder andere Blutwerte (z. B. Leberenzyme) auffällig sind. Eine zeitige Abklärung (z. B. Blutbild, CRP, Serumeisen, TIBC, TSAT, B12, Folsäure) ermöglicht bei Bedarf gezielte Therapie oder Überweisung.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="Was kann als Nächstes passieren?",
                    body_html="""
<p>Je nach Befund und Vorgeschichte kann der Arzt weitere Tests veranlassen: großes Blutbild, CRP, Serumeisen, TIBC, TSAT, Vitamin B12, Folsäure, ggf. Zöliakie- oder Blutungsabklärung. <strong>Lebensstil und Ernährung:</strong> Bei bestätigtem Mangel können eisenreiche Ernährung und ggf. vom Arzt verordnete Präparate helfen; hohe Dosen nicht auf eigene Faust. Bei hohem Ferritin muss zuerst die Ursache geklärt werden (Entzündung, Leber, Stoffwechsel, Genetik); darauf basieren dann Empfehlungen. Bitte folgen Sie den Anweisungen Ihres Arztes.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Häufige Fragen",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Was ist ein „normaler“ Ferritin-Wert?</h3>
<p>„Normal“ hängt vom Referenzbereich des Labors, Alter und Geschlecht ab. Verwenden Sie den Bereich auf Ihrem Befund; Ihr Arzt kann einschätzen, ob Ihr Wert für Sie passend ist.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann niedriges Ferritin Haarausfall verursachen?</h3>
<p>Niedrige Eisenspeicher werden manchmal mit dünner werdendem oder ausfallendem Haar in Verbindung gebracht, aber auch Hormone, Stress und Ernährung spielen eine Rolle. Die Korrektur eines Mangels kann bei einigen helfen; der Arzt berät.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Was erhöht Ferritin außer Eisen?</h3>
<p>Entzündung, Infektion, Lebererkrankung, Alkohol, metabolisches Syndrom und bestimmte Medikamente können Ferritin anheben, ohne echte Eisenüberladung. Daher wird hohes Ferritin immer mit anderen Werten zusammen beurteilt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wie lange dauert es, bis Eisenpräparate wirken?</h3>
<p>Bei verordneter Eisensubstitution kann Ferritin über einige Wochen ansteigen; die Auffüllung der Speicher kann Monate dauern. Halten Sie Dosis und Kontrolltermine ein.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wird Ferritin nüchtern gemessen?</h3>
<p>Ferritin wird durch eine Mahlzeit meist wenig beeinflusst; das Labor kann aber Nüchternheit für ein Profil mit Glukose/Lipiden verlangen. Bitte die Anweisungen zur Blutabnahme beachten.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann ich Ferritin allein interpretieren?</h3>
<p>Ferritin wird am besten im klinischen Kontext und oft zusammen mit Serumeisen, TIBC, TSAT und ggf. CRP beurteilt. Ihr Arzt kann es fachgerecht einordnen.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Hinweis",
                    body_html="""
<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung.</strong> Besprechen Sie Ihre Ergebnisse und Beschwerden immer mit einem Arzt. Setzen Sie keine Präparate ein oder ändern Sie die Therapie nicht nur aufgrund dieses Artikels.</p>
""",
                ),
            ],
            "it": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="Cos’è la ferritina?",
                    body_html="""
<p>La ferritina è una proteina che immagazzina il ferro e lo rilascia in modo controllato quando l’organismo ne ha bisogno. Misurata nel sangue, è l’indicatore più utile delle <strong>riserve di ferro</strong>. Non va confusa con il “ferro sierico” (il ferro in circolo al momento del prelievo), che può variare con i pasti e l’ora del giorno.</p>
<p>Una ferritina bassa suggerisce spesso riserve ridotte e può indicare carenza di ferro se altre cause sono escluse. Una ferritina alta può riflettere un eccesso di ferro accumulato, ma è anche un <strong>reattante di fase acuta</strong>: aumenta spesso con infiammazione, infezione o patologie epatiche, quindi un valore alto non significa automaticamente sovraccarico. L’interpretazione va sempre fatta con il medico e, se necessario, con altri esami.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritina vs ferro vs transferrina vs TSAT",
                    body_html="""
<p>Questi esami sono spesso richiesti insieme per valutare il ferro. In sintesi:</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Esame</th><th class="border border-slate-300 px-3 py-2 text-left">Cosa riflette</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritina</strong></td><td class="border border-slate-300 px-3 py-2">Riserve di ferro. Miglior marcatore singolo in caso di carenza.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferro sierico</strong></td><td class="border border-slate-300 px-3 py-2">Ferro in circolo al prelievo. Varia con dieta e orario.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrina / TIBC</strong></td><td class="border border-slate-300 px-3 py-2">Capacità di trasporto del ferro. Spesso alta quando le riserve sono basse.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>TSAT</strong></td><td class="border border-slate-300 px-3 py-2">Saturazione della transferrina. Bassa in carenza; molto alta può far sospettare sovraccarico.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Ferritina bassa: cause e sintomi",
                    body_html="""
<p><strong>Cause comuni</strong> di ferritina bassa: perdite di sangue (mestruazioni abbondanti, sanguinamento digestivo, interventi), scarso apporto o malassorbimento (es. celiachia, chirurgia gastrica), aumentato fabbisogno (gravidanza, crescita, sport intenso), infiammazione cronica. Più fattori possono coesistere.</p>
<p><strong>Sintomi comuni</strong> associati a riserve basse: stanchezza, debolezza, pallore, fiato corto sotto sforzo, capogiri, mani e piedi freddi, unghie fragili, caduta dei capelli. Sono aspecifici e possono dipendere da molte altre cause. <strong>I sintomi da soli non consentono la diagnosi</strong>; vanno interpretati dal medico insieme agli esami e alla storia clinica.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="Ferritina alta: cause e reattante di fase acuta",
                    body_html="""
<p><strong>Cause comuni</strong> di ferritina elevata: infiammazione o infezione (la ferritina è un reattante di fase acuta e sale spesso anche con riserve normali), steatosi epatica, alcol, sindrome metabolica, obesità, in alcuni casi emocromatosi ereditaria o altro sovraccarico. Anche danno epatico o malattia cronica possono alzare la ferritina.</p>
<p>Poiché <strong>la ferritina è un reattante di fase acuta</strong>, aumenta spesso in corso di malattia, infezione o infiammazione. Un valore alto non significa necessariamente eccesso di ferro; il medico valuterà CRP, ferro sierico, TIBC, TSAT e eventualmente imaging o genetica per chiarire.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="Quali intervalli sono “normali”?",
                    body_html="""
<p>Gli intervalli di riferimento per la ferritina <strong>variano da laboratorio a laboratorio</strong>. Usate sempre quello indicato sul vostro referto. Solo a titolo orientativo: in molti laboratori si usano intervalli approssimativi di circa <strong>12–150 ng/mL per le donne adulte</strong> e <strong>30–300 ng/mL (o più) per gli uomini</strong>. I valori possono essere più bassi nelle donne in età fertile e più alti negli anziani. Queste cifre sono indicative; fa fede l’intervallo del vostro laboratorio.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quando rivolgersi al medico",
                    body_html="""
<p>Consultate il medico se: la ferritina è molto bassa o molto alta; avete emoglobina bassa (anemia) o sintomi come stanchezza inspiegabile, fiato corto o capogiri; avete febbre, perdita di peso o segni di malattia epatica; oppure altri esami (es. enzimi epatici) sono alterati. Una valutazione tempestiva (es. emocromo, CRP, ferro sierico, TIBC, TSAT, B12, folati) permette eventuale terapia o invio allo specialista.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="Cosa può succedere dopo",
                    body_html="""
<p>In base al risultato e alla storia, il medico può prescrivere altri esami: emocromo, CRP, ferro sierico, TIBC, TSAT, vitamina B12, folati, e a volte test per celiachia o sanguinamento digestivo. <strong>Stile di vita e dieta:</strong> in caso di carenza accertata, alimenti ricchi di ferro e, se prescritti, integratori possono aiutare; evitate dosi elevate fai-da-te. Per ferritina alta va prima chiarita la causa (infiammazione, fegato, metabolismo, genetica); le indicazioni dipendono da quella. Seguite sempre le indicazioni del medico.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Domande frequenti",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Qual è un livello “normale” di ferritina?</h3>
<p>“Normale” dipende dall’intervallo del laboratorio, dall’età e dal sesso. Usate l’intervallo sul referto; il medico può dirvi se il valore è adeguato per voi.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritina bassa può causare caduta dei capelli?</h3>
<p>Riserve di ferro basse sono a volte associate a diradamento o caduta; anche ormoni, stress e dieta contano. Correggere la carenza può aiutare in alcuni casi; il medico può consigliare.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Cosa alza la ferritina oltre al ferro?</h3>
<p>Infiammazione, infezione, malattia epatica, alcol, sindrome metabolica e alcuni farmaci possono alzare la ferritina senza vero sovraccarico. Per questo la ferritina alta si interpreta con altri esami.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Quanto tempo prima che gli integratori influenzino la ferritina?</h3>
<p>Se vi viene prescritto ferro per carenza, la ferritina può iniziare a salire in alcune settimane; il ripristino completo può richiedere mesi. Rispettate dosi e controlli indicati dal medico.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritina si misura a digiuno?</h3>
<p>La ferritina di solito non è influenzata dal pasto; il laboratorio può richiedere il digiuno per un pannello che include glucosio o lipidi. Seguite le istruzioni per il prelievo.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Posso interpretare la ferritina da solo?</h3>
<p>La ferritina si interpreta meglio con il contesto clinico e spesso con ferro sierico, TIBC, TSAT e a volte CRP. Il medico può dare un’interpretazione corretta.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Nota",
                    body_html="""
<p><strong>Questo contenuto è solo informativo e non costituisce consulenza medica.</strong> Discutete sempre risultati e sintomi con un medico. Non iniziare o modificare integratori o cure solo in base a questo articolo.</p>
""",
                ),
            ],
            "fr": [
                Section(
                    id="what-is-ferritin",
                    level=2,
                    heading="Qu’est-ce que la ferritine ?",
                    body_html="""
<p>La ferritine est une protéine qui stocke le fer et le libère de façon contrôlée lorsque l’organisme en a besoin. Dosée dans le sang, elle est le meilleur indicateur pratique de vos <strong>réserves en fer</strong>. Elle ne doit pas être confondue avec le « fer sérique » (fer circulant au moment du prélèvement), qui varie avec les repas et l’heure.</p>
<p>Une ferritine basse suggère souvent des réserves diminuées et peut indiquer une carence en fer si les autres causes sont écartées. Une ferritine élevée peut refléter un excès de stockage, mais c’est aussi un <strong>réactant de phase aiguë</strong> : elle augmente souvent avec l’inflammation, l’infection ou une atteinte hépatique, donc un taux élevé ne signifie pas automatiquement surcharge en fer. L’interprétation doit toujours se faire avec un médecin et, si besoin, d’autres examens.</p>
""",
                ),
                Section(
                    id="ferritin-vs-iron",
                    level=2,
                    heading="Ferritine vs fer vs transferrine vs CST",
                    body_html="""
<p>Ces paramètres sont souvent demandés ensemble pour évaluer le statut martial. En bref :</p>
<table class="w-full border-collapse border border-slate-300 my-4 text-sm">
  <thead><tr class="bg-slate-100"><th class="border border-slate-300 px-3 py-2 text-left">Paramètre</th><th class="border border-slate-300 px-3 py-2 text-left">Signification</th></tr></thead>
  <tbody>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Ferritine</strong></td><td class="border border-slate-300 px-3 py-2">Réserves en fer. Meilleur marqueur isolé en cas de carence.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Fer sérique</strong></td><td class="border border-slate-300 px-3 py-2">Fer en circulation au moment du prélèvement. Varie avec l’alimentation et l’heure.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>Transferrine / CCT</strong></td><td class="border border-slate-300 px-3 py-2">Capacité de transport du fer. Souvent élevée quand les réserves sont basses.</td></tr>
    <tr><td class="border border-slate-300 px-3 py-2"><strong>CST</strong></td><td class="border border-slate-300 px-3 py-2">Saturation de la transferrine. Basse en carence ; très élevée peut évoquer une surcharge.</td></tr>
  </tbody>
</table>
""",
                ),
                Section(
                    id="low-ferritin",
                    level=2,
                    heading="Ferritine basse : causes et symptômes",
                    body_html="""
<p><strong>Causes fréquentes</strong> : pertes de sang (règles abondantes, saignements digestifs, chirurgie), faible apport ou mauvaise absorption (maladie cœliaque, chirurgie gastrique), besoins accrus (grossesse, croissance, sport intense), inflammation chronique. Plusieurs facteurs peuvent s’associer.</p>
<p><strong>Symptômes fréquents</strong> possibles en cas de réserves basses : fatigue, faiblesse, pâleur, essoufflement à l’effort, vertiges, mains et pieds froids, ongles fragiles, chute de cheveux. Ils sont non spécifiques et peuvent avoir bien d’autres causes. <strong>Les symptômes seuls ne permettent pas de poser un diagnostic</strong> ; ils doivent être interprétés par un médecin avec les examens et l’histoire clinique.</p>
""",
                ),
                Section(
                    id="high-ferritin",
                    level=2,
                    heading="Ferritine élevée : causes et réaction de phase aiguë",
                    body_html="""
<p><strong>Causes fréquentes</strong> de ferritine élevée : inflammation ou infection (la ferritine est un réactant de phase aiguë et monte souvent même avec des réserves normales), stéatose hépatique, alcool, syndrome métabolique, obésité, et parfois hémochromatose héréditaire ou autre surcharge. Une atteinte hépatique ou une maladie chronique peut aussi élever la ferritine.</p>
<p>Comme <strong>la ferritine est un réactant de phase aiguë</strong>, elle augmente souvent en cas de maladie, d’infection ou d’inflammation. Un taux élevé ne signifie pas forcément excès de fer ; le médecin s’appuiera sur la CRP, le fer sérique, la CCT, la CST et éventuellement l’imagerie ou la génétique pour préciser.</p>
""",
                ),
                Section(
                    id="reference-ranges",
                    level=2,
                    heading="Quelles fourchettes sont « normales » ?",
                    body_html="""
<p>Les fourchettes de référence pour la ferritine <strong>varient selon le laboratoire</strong>. Utilisez toujours celle indiquée sur votre résultat. À titre indicatif seulement : dans beaucoup de laboratoires, les fourchettes sont environ <strong>12–150 ng/mL pour les femmes adultes</strong> et <strong>30–300 ng/mL (ou plus) pour les hommes</strong>. Les valeurs peuvent être plus basses chez les femmes réglées et plus hautes chez les personnes âgées. Ces chiffres sont indicatifs ; c’est la fourchette de votre laboratoire qui s’applique.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quand consulter un médecin",
                    body_html="""
<p>Consultez si : la ferritine est très basse ou très élevée ; vous avez une hémoglobine basse (anémie) ou des symptômes comme une fatigue inexpliquée, un essoufflement ou des vertiges ; vous avez de la fièvre, une perte de poids ou des signes d’atteinte hépatique ; ou d’autres examens (ex. enzymes hépatiques) sont anormaux. Un avis médical précoce permet un bilan adapté (NFS, CRP, fer sérique, CCT, CST, B12, folates) et, si besoin, un traitement ou une orientation.</p>
""",
                ),
                Section(
                    id="next-steps",
                    level=2,
                    heading="Que peut-il se passer ensuite ?",
                    body_html="""
<p>Selon le résultat et l’histoire, le médecin peut prescrire d’autres examens : NFS, CRP, fer sérique, CCT, CST, vitamine B12, folates, et parfois dépistage de maladie cœliaque ou de saignement digestif. <strong>Hygiène de vie et alimentation :</strong> en cas de carence confirmée, aliments riches en fer et, si prescrits, compléments peuvent aider ; évitez les fortes doses en automédication. Pour une ferritine élevée, la cause doit d’abord être précisée (inflammation, foie, métabolisme, génétique) ; les conseils en dépendent. Suivez toujours les recommandations de votre médecin.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Questions fréquentes",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Quel est un taux « normal » de ferritine ?</h3>
<p>« Normal » dépend du laboratoire, de l’âge et du sexe. Utilisez la fourchette sur votre résultat ; votre médecin peut dire si la valeur vous convient.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritine basse peut-elle causer une chute de cheveux ?</h3>
<p>Des réserves basses sont parfois associées à une chute ou une perte de cheveux, mais d’autres facteurs (hormones, stress, alimentation) jouent aussi. Corriger la carence peut aider dans certains cas ; le médecin peut conseiller.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Qu’est-ce qui élève la ferritine en dehors du fer ?</h3>
<p>L’inflammation, l’infection, une maladie du foie, l’alcool, le syndrome métabolique et certains médicaments peuvent élever la ferritine sans vraie surcharge. C’est pourquoi un taux élevé est interprété avec d’autres examens.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Combien de temps avant que les compléments n’agissent sur la ferritine ?</h3>
<p>Si du fer vous est prescrit pour une carence, la ferritine peut commencer à remonter en quelques semaines ; le remplissage complet peut prendre des mois. Respectez la posologie et les contrôles prescrits.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La ferritine se dose-t-elle à jeun ?</h3>
<p>La ferritine est en général peu influencée par un repas récent, mais le laboratoire peut demander le jeûne pour un bilan incluant glucose ou lipides. Suivez les consignes du prélèvement.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Puis-je interpréter la ferritine seul ?</h3>
<p>La ferritine s’interprète au mieux dans le contexte clinique et souvent avec le fer sérique, la CCT, la CST et parfois la CRP. Votre médecin peut en donner une interprétation adaptée.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Avertissement",
                    body_html="""
<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis médical.</strong> Discutez toujours de vos résultats et symptômes avec un médecin. Ne commencez ni ne modifiez un complément ou un traitement sur la seule base de cet article.</p>
""",
                ),
            ],
        },
    )


_FERRITIN_ARTICLE = _article_ferritin()


def _article_crp() -> Article:
    """CRP: what it is, hs-CRP difference, when high, when to see a doctor. en, de, it, fr."""
    published = date(2026, 3, 5)
    cover = "/static/images/blog/crp-hero.png"
    cover_alt_text = {
        "en": "CRP blood test and inflammation dashboard — NoryaAI",
        "de": "CRP-Bluttest und Entzündungs-Dashboard — NoryaAI",
        "it": "Esame CRP e dashboard infiammazione — NoryaAI",
        "fr": "Dosage CRP et tableau de bord inflammation — NoryaAI",
    }
    return Article(
        id="crp-what-it-means",
        published_at=published,
        last_updated=published,
        read_minutes=11,
        cover_image=cover,
        cover_alt=cover_alt_text,
        category={
            "en": "Inflammation / Biomarkers",
            "de": "Entzündung / Biomarker",
            "it": "Infiammazione / Biomarcatori",
            "fr": "Inflammation / Biomarqueurs",
        },
        slugs={
            "en": "crp-what-it-means",
            "de": "crp-what-it-means",
            "it": "crp-what-it-means",
            "fr": "crp-what-it-means",
        },
        titles={
            "en": "CRP Explained: What Elevated Levels Can Mean (and When to Follow Up)",
            "de": "CRP verstehen: Was erhöhte Werte bedeuten",
            "it": "CRP: cosa significa se è alto",
            "fr": "CRP : que signifie un taux élevé",
        },
        subtitles={
            "en": "A clear guide to C-reactive protein, hs-CRP, infection vs inflammation, reference ranges, and when to see a doctor.",
            "de": "Überblick über C-reaktives Protein, hs-CRP, Infektion vs. Entzündung, Referenzbereiche und wann Sie zum Arzt sollten.",
            "it": "Guida chiara su proteina C-reattiva, hs-CRP, infezione vs infiammazione, intervalli di riferimento e quando rivolgersi al medico.",
            "fr": "Guide clair sur la CRP, hs-CRP, infection vs inflammation, fourchettes de référence et quand consulter.",
        },
        excerpts={
            "en": "CRP is a marker of inflammation produced by the liver. High levels can point to infection or chronic inflammation; interpretation should be done with a clinician.",
            "de": "CRP ist ein Entzündungsmarker, der in der Leber gebildet wird. Erhöhte Werte können auf Infektion oder chronische Entzündung hindeuten.",
            "it": "La CRP è un marcatore dell’infiammazione prodotto dal fegato. Valori alti possono indicare infezione o infiammazione cronica.",
            "fr": "La CRP est un marqueur d’inflammation produit par le foie. Un taux élevé peut indiquer une infection ou une inflammation chronique.",
        },
        seo_titles={
            "en": "CRP Explained: What Elevated Levels Can Mean (and When to Follow Up)",
            "de": "CRP verstehen: Was erhöhte Werte bedeuten",
            "it": "CRP: cosa significa se è alto",
            "fr": "CRP : que signifie un taux élevé",
        },
        seo_descriptions={
            "en": "Understand CRP and hs-CRP: what they measure, why levels rise, when values are high, and when to see a doctor. Informational guide only.",
            "de": "CRP und hs-CRP verstehen: Bedeutung, Ursachen erhöhter Werte, Referenzbereiche und wann Sie zum Arzt sollten.",
            "it": "Capire CRP e hs-CRP: cosa misurano, perché aumentano, quando i valori sono alti e quando rivolgersi al medico.",
            "fr": "Comprendre la CRP et la hs-CRP : ce qu’elles mesurent, pourquoi le taux monte, quand consulter. Guide informatif uniquement.",
        },
        sections_by_lang={
            "en": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="What is CRP?",
                    body_html="""
<p>C-reactive protein (CRP) is a protein produced by the liver in response to inflammation anywhere in the body. It is one of the best-known <strong>acute-phase reactants</strong>: its level in the blood rises when tissue is damaged or when the immune system is activated by infection, injury, or chronic inflammatory conditions. CRP does not tell you <em>where</em> the inflammation is or <em>what</em> caused it; it only indicates that some inflammatory process is active. For that reason, it is always interpreted together with your symptoms, other tests, and a doctor’s assessment.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs hs-CRP",
                    body_html="""
<p><strong>Standard CRP</strong> is typically used to monitor infection or acute inflammation (e.g. after surgery, in sepsis, or in autoimmune flares). It is reported in mg/L and can rise into the tens or hundreds in serious infection.</p>
<p><strong>High-sensitivity CRP (hs-CRP)</strong> uses a more sensitive assay and is mainly used to assess <strong>cardiovascular risk</strong> in otherwise stable adults. It measures the same protein but at lower levels (often under 10 mg/L). Guidelines use hs-CRP ranges such as &lt;1 mg/L (low risk), 1–3 mg/L (moderate risk), and &gt;3 mg/L (higher risk) when evaluating heart disease risk—always in combination with other factors and under a doctor’s guidance.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Why does CRP rise?",
                    body_html="""
<p>Common causes of elevated CRP include:</p>
<ul>
  <li><strong>Infections</strong> (bacterial or viral): colds, flu, urinary tract infections, pneumonia, and more serious infections can raise CRP, often sharply in bacterial cases.</li>
  <li><strong>Chronic inflammation</strong>: conditions such as rheumatoid arthritis, inflammatory bowel disease, or chronic kidney disease.</li>
  <li><strong>Autoimmune disease</strong>: flares in lupus, vasculitis, or other autoimmune disorders.</li>
  <li><strong>Injury, surgery, or trauma</strong>: tissue damage triggers an acute-phase response.</li>
  <li><strong>Lifestyle factors</strong>: smoking, obesity, and a sedentary lifestyle can keep CRP mildly elevated over time.</li>
</ul>
<p>CRP is non-specific: a high value does not diagnose a condition. Your doctor will use it together with your history, examination, and other tests to narrow down the cause.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="What counts as “high”?",
                    body_html="""
<p>Reference ranges <strong>vary by laboratory</strong> and by assay. Always use the range printed on your own report. The following are rough, illustrative ranges in mg/L (not a substitute for your lab’s reference):</p>
<ul>
  <li><strong>Standard CRP</strong>: &lt;5 often considered normal; 5–10 mild elevation; 10–40 moderate; &gt;40 marked elevation; &gt;100 often seen in serious bacterial infection. These figures are approximate and method-dependent.</li>
  <li><strong>hs-CRP</strong> (for cardiovascular risk context): &lt;1 mg/L low risk; 1–3 mg/L moderate risk; &gt;3 mg/L higher risk. Again, this is used together with other risk factors and only under clinical guidance.</li>
</ul>
<p>Do not self-diagnose from these numbers. Interpretation must be done by a doctor who can consider your full picture.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="What can you do to lower CRP?",
                    body_html="""
<p>There is no single “treatment for high CRP”—the goal is to address the underlying cause. In general, healthy lifestyle measures can support lower background inflammation:</p>
<ul>
  <li>Quality sleep, weight management if needed, avoiding smoking, a balanced anti-inflammatory-style diet (e.g. Mediterranean), and regular moderate exercise.</li>
</ul>
<p>If your CRP is elevated because of an infection, autoimmune condition, or other illness, your doctor will recommend specific treatments or referrals. Do not start or change supplements or medication based on CRP alone; always follow your doctor’s evaluation and advice.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="When should you see a doctor?",
                    body_html="""
<p>See a doctor if you have:</p>
<ul>
  <li>High CRP together with <strong>fever</strong>, severe pain, shortness of breath, or feeling very unwell.</li>
  <li>Unexplained <strong>weight loss</strong> or fatigue with elevated CRP.</li>
  <li>CRP that stays <strong>elevated for a long time</strong> without a clear explanation.</li>
  <li>Other blood tests or symptoms that suggest infection, inflammation, or an autoimmune condition.</li>
</ul>
<p>Seek urgent care for severe symptoms (e.g. difficulty breathing, chest pain, confusion, or if your lab or doctor has advised immediate follow-up).</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="What tests might come next?",
                    body_html="""
<p>Depending on your result and history, your doctor may order further tests to find the cause of inflammation or to assess risk. These can include:</p>
<ul>
  <li><strong>Full blood count (CBC)</strong>, <strong>ESR</strong> (erythrocyte sedimentation rate), <strong>ferritin</strong>.</li>
  <li><strong>Procalcitonin</strong> (often used to help distinguish bacterial infection from other causes).</li>
  <li><strong>Liver function tests (LFT)</strong>, <strong>urinalysis</strong>, or imaging (e.g. X-ray, ultrasound) when appropriate.</li>
</ul>
<p>Which tests are needed is a clinical decision made by your doctor; this list is for information only.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Frequently asked questions",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">If CRP is high, do I need antibiotics?</h3>
<p>Not necessarily. CRP can rise with viral infections (e.g. colds, flu), where antibiotics are not indicated. Only your doctor can decide whether an infection is bacterial and whether antibiotics are appropriate.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Does a cold raise CRP?</h3>
<p>Yes. Viral upper respiratory infections, including the common cold, can cause a mild to moderate rise in CRP. This does not mean you have a bacterial infection.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can exercise raise CRP?</h3>
<p>Intense or unaccustomed exercise can cause a temporary, small rise in CRP due to muscle micro-injury. Regular moderate exercise is generally associated with lower background inflammation over time.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Is CRP tested fasting?</h3>
<p>CRP is usually not strongly affected by a recent meal. Your lab may still ask for fasting if the sample is used for a panel that includes glucose or lipids; follow the instructions you are given.</p>
<h3 class="text-base font-semibold mt-4 mb-1">What is the difference between CRP and ESR?</h3>
<p>Both are markers of inflammation. CRP often rises and falls more quickly; ESR can stay elevated longer. Doctors sometimes use them together to get a fuller picture.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Can stress raise CRP?</h3>
<p>Chronic stress may be associated with slightly higher CRP in some people. Stress alone does not explain very high CRP; other causes (infection, inflammation) are usually considered first.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Disclaimer",
                    body_html="""
<p><strong>This content is for information only and does not constitute medical advice or diagnosis.</strong> Always discuss your results and symptoms with a doctor. Do not start or change treatment or supplements based solely on this article. If you have concerns about your health, seek professional medical care.</p>
""",
                ),
            ],
            "de": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="Was ist CRP?",
                    body_html="""
<p>C-reaktives Protein (CRP) wird in der Leber als Reaktion auf Entzündungen im Körper gebildet. Es zählt zu den bekanntesten <strong>Akute-Phase-Proteinen</strong>: Der Spiegel im Blut steigt bei Gewebeschäden oder bei Aktivierung des Immunsystems durch Infektion, Verletzung oder chronische Entzündung. CRP sagt nicht, <em>wo</em> die Entzündung sitzt oder <em>was</em> sie verursacht hat; es zeigt nur an, dass ein entzündlicher Prozess aktiv ist. Die Einordnung erfolgt daher immer gemeinsam mit Beschwerden, weiteren Befunden und der ärztlichen Beurteilung.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs. hs-CRP",
                    body_html="""
<p><strong>Standard-CRP</strong> dient typischerweise der Verlaufskontrolle bei Infektion oder akuter Entzündung (z. B. nach OP, bei Sepsis oder Schüben autoimmuner Erkrankungen). Es wird in mg/L angegeben und kann bei schweren Infektionen stark ansteigen.</p>
<p><strong>High-sensitivity CRP (hs-CRP)</strong> wird mit einer empfindlicheren Methode gemessen und vor allem zur Einschätzung des <strong>kardiovaskulären Risikos</strong> bei stabilen Erwachsenen genutzt. Es misst dasselbe Protein in niedrigeren Bereichen (oft unter 10 mg/L). In Leitlinien werden z. B. &lt;1 mg/L (niedriges Risiko), 1–3 mg/L (mittleres Risiko) und &gt;3 mg/L (höheres Risiko) verwendet – stets zusammen mit anderen Faktoren und in ärztlicher Absprache.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Warum steigt CRP?",
                    body_html="""
<p>Häufige Ursachen erhöhten CRP sind:</p>
<ul>
  <li><strong>Infektionen</strong> (bakteriell oder viral): Erkältung, Grippe, Harnwegsinfekte, Lungenentzündung oder schwerere Infektionen können CRP anheben, bei bakteriellen oft stark.</li>
  <li><strong>Chronische Entzündung</strong>: z. B. rheumatoide Arthritis, chronisch-entzündliche Darmerkrankungen, Nierenerkrankung.</li>
  <li><strong>Autoimmunerkrankungen</strong>: Schübe bei Lupus, Vaskulitis oder anderen Erkrankungen.</li>
  <li><strong>Verletzung, Operation, Trauma</strong>: Gewebeschaden löst eine Akute-Phase-Reaktion aus.</li>
  <li><strong>Lebensstil</strong>: Rauchen, Übergewicht, Bewegungsmangel können CRP leicht erhöht halten.</li>
</ul>
<p>CRP ist unspezifisch: Ein hoher Wert stellt keine Diagnose. Der Arzt ordnet ihn gemeinsam mit Anamnese, Untersuchung und weiteren Tests ein.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="Wann gilt CRP als „erhöht“?",
                    body_html="""
<p>Referenzbereiche <strong>unterscheiden sich je nach Labor und Methode</strong>. Orientieren Sie sich am Bereich auf Ihrem Befund. Zur groben Einordnung (in mg/L, nur Richtwerte):</p>
<ul>
  <li><strong>Standard-CRP</strong>: &lt;5 oft als normal; 5–10 leicht erhöht; 10–40 mäßig; &gt;40 deutlich erhöht; &gt;100 oft bei schwerer bakterieller Infektion. Die Werte sind methodenabhängig.</li>
  <li><strong>hs-CRP</strong> (im kardiovaskulären Kontext): &lt;1 mg/L niedriges Risiko; 1–3 mg/L mittleres; &gt;3 mg/L höheres Risiko. Auch hier nur in Verbindung mit anderen Faktoren und nach ärztlicher Bewertung.</li>
</ul>
<p>Bitte keine Selbstdiagnose. Die Einordnung muss durch einen Arzt erfolgen.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="Was kann man tun, um CRP zu senken?",
                    body_html="""
<p>Es gibt keine einzelne „Therapie gegen hohes CRP“ – Ziel ist die Behandlung der Ursache. Allgemein können gesunder Schlaf, Gewichtsnormalisierung, Nichtrauchen, ausgewogene Ernährung (z. B. mediterran) und regelmäßige moderate Bewegung die Entzündungsaktivität günstig beeinflussen.</p>
<p>Bei Infektion, Autoimmunerkrankung oder anderer Ursache wird der Arzt gezielte Maßnahmen oder Überweisungen empfehlen. Setzen Sie keine Präparate oder Medikamente allein wegen CRP ein; folgen Sie der ärztlichen Einschätzung.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Wann zum Arzt?",
                    body_html="""
<p>Gehen Sie zum Arzt, wenn Sie hohes CRP haben und z. B. Fieber, starke Schmerzen, Atemnot oder starkes Unwohlsein; ungewollten Gewichtsverlust oder anhaltende Müdigkeit; oder wenn CRP über längere Zeit ohne klare Erklärung erhöht bleibt. Auch bei anderen auffälligen Werten oder Symptomen, die auf Infektion oder Entzündung hindeuten, ist eine Abklärung nötig. Bei schweren Symptomen (z. B. Atemnot, Brustschmerz, Verwirrtheit) oder wenn Labor/Arzt sofortige Kontrolle angeraten haben, suchen Sie zeitnah ärztliche Hilfe.</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="Welche Tests können folgen?",
                    body_html="""
<p>Je nach Befund und Vorgeschichte kann der Arzt weitere Tests veranlassen: z. B. großes Blutbild (CBC), Blutkörperchensenkung (ESR), Ferritin, Procalcitonin (zur Abgrenzung bakterieller Infektion), Leberwerte, Urinuntersuchung oder Bildgebung. Welche Tests nötig sind, entscheidet der Arzt; diese Auflistung dient nur der Information.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Häufige Fragen",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Brauche ich bei hohem CRP Antibiotika?</h3>
<p>Nicht zwingend. CRP kann auch bei viralen Infekten (z. B. Erkältung, Grippe) ansteigen, bei denen keine Antibiotika angezeigt sind. Ob eine bakterielle Infektion vorliegt und ob Antibiotika sinnvoll sind, entscheidet der Arzt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Erhöht eine Erkältung das CRP?</h3>
<p>Ja. Virusbedingte Atemwegsinfekte können CRP leicht bis mäßig anheben. Das bedeutet nicht, dass eine bakterielle Infektion vorliegt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann Sport CRP erhöhen?</h3>
<p>Intensive oder ungewohnte Belastung kann durch Mikroverletzungen der Muskulatur kurzfristig leicht CRP anheben. Regelmäßige moderate Bewegung geht langfristig oft mit niedrigerer Entzündungsaktivität einher.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Wird CRP nüchtern gemessen?</h3>
<p>CRP wird durch eine Mahlzeit meist wenig beeinflusst. Das Labor kann trotzdem Nüchternheit verlangen, wenn das Blut für ein Profil mit Glukose/Lipiden verwendet wird; bitte die Anweisungen beachten.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Was ist der Unterschied zwischen CRP und BKS (ESR)?</h3>
<p>Beide sind Entzündungsmarker. CRP steigt und fällt oft rascher; die BKS kann länger erhöht bleiben. Sie werden teils gemeinsam beurteilt.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Kann Stress CRP erhöhen?</h3>
<p>Dauerhafter Stress kann bei manchen Menschen mit leicht erhöhtem CRP einhergehen. Sehr hohes CRP erklärt sich dadurch nicht; andere Ursachen (Infektion, Entzündung) werden zuerst geprüft.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Hinweis",
                    body_html="""
<p><strong>Dieser Inhalt dient nur der Information und ersetzt keine medizinische Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse und Beschwerden immer mit einem Arzt. Setzen Sie keine Behandlung oder Präparate nur aufgrund dieses Artikels ein. Bei gesundheitlichen Sorgen wenden Sie sich an Fachpersonal.</p>
""",
                ),
            ],
            "it": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="Cos’è la CRP?",
                    body_html="""
<p>La proteina C-reattiva (CRP) è prodotta dal fegato in risposta a un’infiammazione in qualsiasi parte del corpo. È uno dei più noti <strong>reattanti di fase acuta</strong>: il suo livello nel sangue aumenta quando i tessuti sono danneggiati o quando il sistema immunitario è attivato da infezione, trauma o condizioni infiammatorie croniche. La CRP non indica <em>dove</em> sia l’infiammazione né <em>cosa</em> l’abbia causata; indica solo che è in corso un processo infiammatorio. Va quindi sempre interpretata insieme a sintomi, altri esami e al giudizio del medico.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs hs-CRP",
                    body_html="""
<p>La <strong>CRP standard</strong> si usa tipicamente per monitorare infezioni o infiammazione acuta (es. dopo intervento, sepsi, riacutizzazioni autoimmuni). Si esprime in mg/L e può salire molto in caso di infezione grave.</p>
<p>La <strong>CRP ad alta sensibilità (hs-CRP)</strong> usa un test più sensibile ed è usata soprattutto per valutare il <strong>rischio cardiovascolare</strong> in adulti stabili. Misura la stessa proteina a livelli più bassi (spesso sotto 10 mg/L). Nelle linee guida si usano intervalli come &lt;1 mg/L (rischio basso), 1–3 mg/L (moderato), &gt;3 mg/L (più alto), sempre insieme ad altri fattori e sotto guida medica.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Perché la CRP aumenta?",
                    body_html="""
<p>Cause comuni di CRP elevata: <strong>infezioni</strong> (batteriche o virali), <strong>infiammazione cronica</strong> (es. artrite reumatoide, malattie intestinali croniche), <strong>malattie autoimmuni</strong>, <strong>trauma, intervento chirurgico</strong>, <strong>fumo, obesità, sedentarietà</strong>. La CRP è aspecifica: un valore alto non fa diagnosi; il medico la valuta con anamnesi, visita e altri esami.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="Quando si considera “alta”?",
                    body_html="""
<p>I range di riferimento <strong>variano da laboratorio a laboratorio</strong>. Usate sempre quello sul vostro referto. Solo a titolo orientativo (mg/L): CRP standard: &lt;5 spesso normale; 5–10 lieve; 10–40 moderata; &gt;40 marcata; &gt;100 spesso in infezione batterica seria. hs-CRP (contesto cardiovascolare): &lt;1 rischio basso; 1–3 moderato; &gt;3 più alto. L’interpretazione spetta al medico.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="Cosa si può fare per abbassarla?",
                    body_html="""
<p>Non esiste un unico “trattamento per la CRP alta”; l’obiettivo è agire sulla causa. In generale, sonno adeguato, peso nella norma, niente fumo, dieta equilibrata (es. mediterranea) e attività fisica moderata regolare possono aiutare a ridurre l’infiammazione di base. Per infezione o altra causa il medico indicherà cure o invii. Non iniziare o modificare integratori/terapie solo in base alla CRP; seguire sempre il medico.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quando rivolgersi al medico?",
                    body_html="""
<p>Consultate il medico se avete CRP alta con febbre, dolore forte, mancanza di respiro o malessere intenso; perdita di peso inspiegabile o stanchezza con CRP elevata; CRP che resta alta a lungo senza spiegazione; altri esami o sintomi che suggeriscono infezione o infiammazione. In caso di sintomi gravi (difficoltà respiratoria, dolore al petto, confusione) o se il laboratorio/medico consigliano controllo urgente, recatevi subito a un medico.</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="Quali esami possono seguire?",
                    body_html="""
<p>In base al risultato e alla storia, il medico può prescrivere altri esami: emocromo, VES, ferritina, procalcitonina, esami epatici, urinocoltura o imaging. La scelta spetta al medico; questo elenco è solo informativo.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Domande frequenti",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">Con CRP alta servono antibiotici?</h3>
<p>Non necessariamente. La CRP può salire anche con infezioni virali (raffreddore, influenza), per cui gli antibiotici non sono indicati. Solo il medico può stabilire se c’è un’infezione batterica e se servono antibiotici.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Il raffreddore fa salire la CRP?</h3>
<p>Sì. Le infezioni virali delle vie respiratorie possono far aumentare lievemente o moderatamente la CRP. Non significa che ci sia un’infezione batterica.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Lo sport può alzare la CRP?</h3>
<p>L’esercizio intenso o non abituale può causare un piccolo aumento temporaneo per microlesioni muscolari. L’attività moderata regolare è in genere associata a minore infiammazione di base.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La CRP si misura a digiuno?</h3>
<p>La CRP di solito non è influenzata dal pasto. Il laboratorio può comunque richiedere il digiuno se il prelievo è per un pannello con glucosio o lipidi; seguite le istruzioni.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Qual è la differenza tra CRP e VES?</h3>
<p>Entrambi sono marker di infiammazione. La CRP spesso sale e scende più rapidamente; la VES può restare elevata più a lungo. A volte si usano insieme.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Lo stress può alzare la CRP?</h3>
<p>Lo stress cronico può essere associato a CRP leggermente più alta in alcune persone. Lo stress da solo non spiega valori molto alti; si considerano prima altre cause (infezione, infiammazione).</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Nota",
                    body_html="""
<p><strong>Questo contenuto è solo informativo e non costituisce consulenza o diagnosi medica.</strong> Discutete sempre risultati e sintomi con un medico. Non iniziare o modificare cure o integratori solo in base a questo articolo. In caso di dubbi sulla salute, rivolgetevi a un professionista.</p>
""",
                ),
            ],
            "fr": [
                Section(
                    id="what-is-crp",
                    level=2,
                    heading="Qu’est-ce que la CRP ?",
                    body_html="""
<p>La protéine C-réactive (CRP) est produite par le foie en réponse à une inflammation n’importe où dans l’organisme. C’est l’un des <strong>réactants de phase aiguë</strong> les plus connus : son taux sanguin augmente en cas de lésion tissulaire ou d’activation du système immunitaire (infection, traumatisme, maladie inflammatoire chronique). La CRP ne indique pas <em>où</em> est l’inflammation ni <em>quelle</em> en est la cause ; elle signale seulement qu’un processus inflammatoire est actif. Elle est donc toujours interprétée avec les symptômes, les autres examens et l’avis du médecin.</p>
""",
                ),
                Section(
                    id="crp-vs-hscrp",
                    level=2,
                    heading="CRP vs hs-CRP",
                    body_html="""
<p>La <strong>CRP standard</strong> sert typiquement à surveiller une infection ou une inflammation aiguë (après chirurgie, sepsis, poussée autoimmune). Elle est exprimée en mg/L et peut monter beaucoup en cas d’infection grave.</p>
<p>La <strong>CRP ultra-sensible (hs-CRP)</strong> utilise une technique plus sensible et sert surtout à évaluer le <strong>risque cardiovasculaire</strong> chez l’adulte stable. Elle mesure la même protéine à des niveaux plus bas (souvent &lt;10 mg/L). Les recommandations utilisent des fourchettes comme &lt;1 mg/L (risque faible), 1–3 mg/L (modéré), &gt;3 mg/L (plus élevé), toujours avec d’autres facteurs et sous suivi médical.</p>
""",
                ),
                Section(
                    id="why-crp-rises",
                    level=2,
                    heading="Pourquoi la CRP monte-t-elle ?",
                    body_html="""
<p>Causes fréquentes d’élévation : <strong>infections</strong> (bactériennes ou virales), <strong>inflammation chronique</strong> (polyarthrite, maladie inflammatoire intestinale, etc.), <strong>maladies auto-immunes</strong>, <strong>traumatisme ou chirurgie</strong>, <strong>tabac, obésité, sédentarité</strong>. La CRP est non spécifique : un taux élevé ne fait pas à lui seul un diagnostic ; le médecin l’interprète avec l’histoire, l’examen et d’autres examens.</p>
""",
                ),
                Section(
                    id="what-counts-as-high",
                    level=2,
                    heading="À partir de quand c’est « élevé » ?",
                    body_html="""
<p>Les fourchettes de référence <strong>varient selon le laboratoire</strong>. Utilisez toujours celle indiquée sur votre résultat. À titre indicatif (mg/L) : CRP standard : &lt;5 souvent normal ; 5–10 légère ; 10–40 modérée ; &gt;40 marquée ; &gt;100 souvent en cas d’infection bactérienne sévère. hs-CRP (contexte cardiovasculaire) : &lt;1 risque faible ; 1–3 modéré ; &gt;3 plus élevé. L’interprétation relève du médecin.</p>
""",
                ),
                Section(
                    id="how-to-lower-crp",
                    level=2,
                    heading="Que faire pour faire baisser la CRP ?",
                    body_html="""
<p>Il n’y a pas de « traitement du taux de CRP » unique ; l’objectif est de traiter la cause. En général, un bon sommeil, un poids correct, l’arrêt du tabac, une alimentation équilibrée (type méditerranéen) et une activité physique modérée régulière peuvent aider à limiter l’inflammation de fond. En cas d’infection ou d’autre cause, le médecin proposera un traitement ou une orientation. Ne pas modifier seul son traitement ou ses compléments à cause de la CRP ; suivre l’avis du médecin.</p>
""",
                ),
                Section(
                    id="when-to-see-doctor",
                    level=2,
                    heading="Quand consulter un médecin ?",
                    body_html="""
<p>Consultez si vous avez un taux de CRP élevé avec fièvre, douleur intense, essoufflement ou malaise important ; perte de poids inexpliquée ou fatigue avec CRP élevée ; CRP qui reste élevée longtemps sans explication ; ou d’autres examens/symptômes évocateurs d’infection ou d’inflammation. En cas de symptômes graves (difficulté à respirer, douleur thoracique, confusion) ou si le laboratoire ou le médecin a conseillé un suivi urgent, consultez sans tarder.</p>
""",
                ),
                Section(
                    id="next-step-tests",
                    level=2,
                    heading="Quels examens peuvent suivre ?",
                    body_html="""
<p>Selon le résultat et l’histoire, le médecin peut prescrire d’autres examens : NFS, VS, ferritine, procalcitonine, bilan hépatique, examen urinaire ou imagerie. Le choix des examens est médical ; cette liste est informative.</p>
""",
                ),
                Section(
                    id="faq",
                    level=2,
                    heading="Questions fréquentes",
                    body_html="""
<h3 class="text-base font-semibold mt-4 mb-1">En cas de CRP élevée, faut-il des antibiotiques ?</h3>
<p>Pas forcément. La CRP peut monter lors d’infections virales (rhume, grippe), pour lesquelles les antibiotiques ne sont pas indiqués. Seul le médecin peut juger si une infection bactérienne est présente et si des antibiotiques sont nécessaires.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Un rhume fait-il monter la CRP ?</h3>
<p>Oui. Les infections virales des voies respiratoires peuvent faire monter un peu la CRP. Cela ne signifie pas une infection bactérienne.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Le sport peut-il faire monter la CRP ?</h3>
<p>Un effort intense ou inhabituel peut entraîner une légère hausse temporaire (micro-lésions musculaires). Une activité modérée régulière est en général associée à une inflammation de fond plus basse.</p>
<h3 class="text-base font-semibold mt-4 mb-1">La CRP se dose-t-elle à jeun ?</h3>
<p>La CRP est en général peu influencée par le repas. Le laboratoire peut quand même demander le jeûne pour un bilan incluant glucose ou lipides ; suivez les consignes.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Quelle est la différence entre CRP et VS ?</h3>
<p>Les deux sont des marqueurs d’inflammation. La CRP monte et descend souvent plus vite ; la VS peut rester élevée plus longtemps. Ils sont parfois utilisés ensemble.</p>
<h3 class="text-base font-semibold mt-4 mb-1">Le stress peut-il faire monter la CRP ?</h3>
<p>Le stress chronique peut être associé à une CRP un peu plus élevée chez certaines personnes. Le stress seul n’explique pas une CRP très élevée ; d’autres causes (infection, inflammation) sont d’abord envisagées.</p>
""",
                ),
                Section(
                    id="disclaimer",
                    level=2,
                    heading="Avertissement",
                    body_html="""
<p><strong>Ce contenu est à titre informatif uniquement et ne constitue pas un avis médical ni un diagnostic.</strong> Discutez toujours de vos résultats et symptômes avec un médecin. Ne commencez ni ne modifiez un traitement ou des compléments sur la seule base de cet article. En cas de doute sur votre santé, consultez un professionnel.</p>
""",
                ),
            ],
        },
    )


_CRP_ARTICLE = _article_crp()


ARTICLES: List[Article] = [
    _LDL_ARTICLE,
    _KAN_TAHLILI_ARTICLE,
    _FERRITIN_ARTICLE,
    _CRP_ARTICLE,
]


def _normalize_lang(lang: str | None) -> str:
    if not lang:
        return DEFAULT_BLOG_LANG
    lang = lang.lower()[:5]
    if lang in BLOG_LANGS:
        return lang
    short = lang.split("-")[0]
    return short if short in BLOG_LANGS else DEFAULT_BLOG_LANG


def list_articles_for_lang(lang: str) -> List[dict]:
    """Belirli bir dil için blog listesinde kullanılacak kart verilerini döner."""
    lang = _normalize_lang(lang)
    items: List[dict] = []
    for art in ARTICLES:
        if lang not in art.slugs:
            continue
        items.append(
            {
                "id": art.id,
                "slug": art.slugs[lang],
                "title": art.titles.get(lang, art.titles.get(DEFAULT_BLOG_LANG)),
                "excerpt": art.excerpts.get(lang, art.excerpts.get(DEFAULT_BLOG_LANG, "")),
                "category": art.category.get(lang, art.category.get(DEFAULT_BLOG_LANG, "")),
                "cover_image": art.cover_image,
                "read_minutes": art.read_minutes,
                "published_at": art.published_at,
            }
        )
    # Yayın tarihine göre yeni -> eski
    items.sort(key=lambda x: x["published_at"], reverse=True)
    return items


def get_article(lang: str, slug: str) -> dict | None:
    """Dil + slug ile makale ve seçili dil içeriğini döner."""
    lang = _normalize_lang(lang)
    for art in ARTICLES:
        if art.slugs.get(lang) == slug:
            sections = art.sections_by_lang.get(lang) or art.sections_by_lang.get(DEFAULT_BLOG_LANG) or []
            cover_alt = None
            if getattr(art, "cover_alt", None) and isinstance(art.cover_alt, dict):
                cover_alt = art.cover_alt.get(lang) or art.cover_alt.get(DEFAULT_BLOG_LANG)
            last_updated = getattr(art, "last_updated", None) or art.published_at
            return {
                "id": art.id,
                "lang": lang,
                "slug": slug,
                "title": art.titles.get(lang, art.titles.get(DEFAULT_BLOG_LANG)),
                "subtitle": art.subtitles.get(lang, art.subtitles.get(DEFAULT_BLOG_LANG, "")),
                "excerpt": art.excerpts.get(lang, art.excerpts.get(DEFAULT_BLOG_LANG, "")),
                "seo_title": art.seo_titles.get(lang, art.seo_titles.get(DEFAULT_BLOG_LANG)),
                "seo_description": art.seo_descriptions.get(lang, art.seo_descriptions.get(DEFAULT_BLOG_LANG, "")),
                "cover_image": art.cover_image,
                "cover_alt": cover_alt,
                "category": art.category.get(lang, art.category.get(DEFAULT_BLOG_LANG, "")),
                "read_minutes": art.read_minutes,
                "published_at": art.published_at,
                "last_updated": last_updated,
                "sections": sections,
                "available_langs": {
                    l: art.slugs[l] for l in art.slugs.keys() if l in BLOG_LANGS
                },
            }
    return None


def iter_all_article_paths():
    """Sitemap için tüm dil+slug kombinasyonlarını döner."""
    for art in ARTICLES:
        for lang, slug in art.slugs.items():
            if lang not in BLOG_LANGS:
                continue
            yield {
                "lang": lang,
                "slug": slug,
                "published_at": art.published_at,
            }

