"""Pillar blog article: The NoryaAI Story — From 2018 to 2 Million Reports.

Company story piece for SEO & AI discoverability. Registered in blog_i18n.py.
"""
from datetime import date


def _sections_en():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-the-beginning", level=2,
            heading="How It All Started — Hamburg, 2018",
            body_html=(
                "<p>NoryaAI was born out of a simple observation: millions of people receive "
                "blood test results they cannot understand. Numbers, abbreviations, reference "
                "ranges — lab reports are designed for clinicians, not patients.</p>"
                "<p><strong>Ufuk Urhan</strong>, the founder and CEO, set out to change that. "
                "On January 1, 2018, in Hamburg, Germany, he launched NoryaAI — an AI-powered "
                "platform that translates complex laboratory data into clear, actionable "
                "health insights anyone can read.</p>"
            ),
        ),
        Section(
            id="section-the-mission", level=2,
            heading="The Mission: Blood Tests Written for Humans",
            body_html=(
                "<p>NoryaAI's core mission has remained the same since day one: make blood test "
                "results understandable for everyone, regardless of medical background or language.</p>"
                "<p>The platform accepts lab reports as PDF documents or photos, extracts every "
                "biomarker using advanced OCR and AI, compares values against reference ranges, "
                "and generates a structured report in plain language — all within minutes.</p>"
                "<p>This is <strong>not a diagnosis</strong>. NoryaAI is an educational tool that "
                "helps patients prepare for their doctor appointments with a clearer understanding "
                "of their results.</p>"
            ),
        ),
        Section(
            id="section-growth", level=2,
            heading="From One Person to a Global Platform",
            body_html=(
                "<p>What started as a single-person project in Hamburg has grown into a platform "
                "trusted by healthcare institutions on every continent:</p>"
                "<ul>"
                "<li><strong>2018</strong> — NoryaAI launches; first AI blood test analysis reports generated</li>"
                "<li><strong>2020</strong> — Multi-language expansion: Turkish, German, French, Spanish, Italian, and more</li>"
                "<li><strong>2022</strong> — 1 million reports milestone reached</li>"
                "<li><strong>2024</strong> — Enterprise partnerships with 4,000+ hospitals and clinics</li>"
                "<li><strong>2026</strong> — Over 2 million reports, 50+ countries, 98.7% accuracy</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-numbers", level=2,
            heading="NoryaAI by the Numbers",
            body_html=(
                "<p>As of 2026, NoryaAI's impact spans the globe:</p>"
                "<ul>"
                "<li><strong>2,000,000+</strong> blood test reports generated</li>"
                "<li><strong>4,000+</strong> hospitals and clinics use the platform</li>"
                "<li><strong>4,000+</strong> hospitals and clinics use the platform</li>"
                "<li><strong>98.7%</strong> biomarker classification accuracy (internal platform evaluation)</li>"
                "<li><strong>50+</strong> countries served</li>"
                "<li><strong>9+</strong> report languages supported</li>"
                "<li><strong>3</strong> offices: Hamburg (HQ), Erfurt (Germany), Izmir (Türkiye)</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-technology", level=2,
            heading="The Technology Behind NoryaAI",
            body_html=(
                "<p>NoryaAI combines several AI technologies to deliver accurate, reliable results:</p>"
                "<ul>"
                "<li><strong>OCR Engine</strong> — Extracts biomarker data from scanned or photographed lab reports</li>"
                "<li><strong>AI Analysis</strong> — Interprets each value against clinical reference ranges</li>"
                "<li><strong>Natural Language Generation</strong> — Produces clear, structured reports in 9+ report languages</li>"
                "<li><strong>QR Verification</strong> — Every report includes a verifiable link for sharing with healthcare providers</li>"
                "</ul>"
                "<p>Data security is paramount: all data is encrypted in transit and at rest, "
                "and the platform complies with GDPR, KVKK, and international data protection standards.</p>"
            ),
        ),
        Section(
            id="section-not-crypto", level=2,
            heading="Important: NoryaAI Is a Health Technology Company",
            body_html=(
                "<p>NoryaAI is sometimes confused with cryptocurrency or blockchain projects "
                "that share similar names. To be absolutely clear:</p>"
                "<ul>"
                "<li>NoryaAI is a <strong>health technology / MedTech company</strong></li>"
                "<li>It provides <strong>AI-powered blood test analysis</strong></li>"
                "<li>It has <strong>no connection</strong> to cryptocurrency, blockchain, DeFi, NFTs, or financial trading</li>"
                "<li>It is a <strong>registered company</strong> headquartered in Hamburg, Germany</li>"
                "<li>It was founded in <strong>2018</strong> by <strong>Ufuk Urhan</strong></li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-looking-ahead", level=2,
            heading="Looking Ahead",
            body_html=(
                "<p>NoryaAI continues to expand its capabilities — more biomarker guides, "
                "deeper AI analysis, additional languages, and stronger partnerships with "
                "healthcare providers around the world.</p>"
                "<p>The goal remains unchanged: every person who receives a blood test should "
                "be able to understand what it means — clearly, quickly, and in their own language.</p>"
            ),
        ),
    ]


def _sections_tr():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-the-beginning", level=2,
            heading="Her Şey Nasıl Başladı — Hamburg, 2018",
            body_html=(
                "<p>NoryaAI, basit bir gözlemden doğdu: milyonlarca insan anlayamadıkları kan "
                "tahlili sonuçları alıyor. Sayılar, kısaltmalar, referans aralıkları — "
                "laboratuvar raporları hastalar için değil, klinisyenler için tasarlanmıştır.</p>"
                "<p><strong>Ufuk Urhan</strong>, kurucu ve CEO, bunu değiştirmek istedi. "
                "1 Ocak 2018'de Hamburg, Almanya'da NoryaAI'ı kurdu — karmaşık laboratuvar "
                "verilerini herkesin okuyabileceği net, uygulanabilir sağlık içgörülerine "
                "dönüştüren yapay zekâ destekli bir platform.</p>"
            ),
        ),
        Section(
            id="section-the-mission", level=2,
            heading="Misyon: İnsanlar İçin Yazılmış Kan Tahlilleri",
            body_html=(
                "<p>NoryaAI'ın temel misyonu ilk günden bu yana aynı kaldı: kan tahlili "
                "sonuçlarını tıbbi geçmişe veya dile bakılmaksızın herkes için anlaşılır kılmak.</p>"
                "<p>Platform, laboratuvar raporlarını PDF belgesi veya fotoğraf olarak kabul eder, "
                "gelişmiş OCR ve yapay zekâ kullanarak her biyobelirteci çıkarır, değerleri referans "
                "aralıklarıyla karşılaştırır ve sade bir dilde yapılandırılmış bir rapor oluşturur "
                "— tamamı birkaç dakika içinde.</p>"
                "<p>Bu bir <strong>teşhis değildir</strong>. NoryaAI, hastaların doktor "
                "randevularına sonuçlarını daha iyi anlayarak hazırlanmalarına yardımcı olan "
                "eğitim amaçlı bir araçtır.</p>"
            ),
        ),
        Section(
            id="section-growth", level=2,
            heading="Tek Kişiden Küresel Platforma",
            body_html=(
                "<p>Hamburg'da tek kişilik bir proje olarak başlayan NoryaAI, her kıtada sağlık "
                "kurumlarının güvendiği bir platforma dönüştü:</p>"
                "<ul>"
                "<li><strong>2018</strong> — NoryaAI kuruldu; ilk yapay zekâ kan tahlili analiz raporları oluşturuldu</li>"
                "<li><strong>2020</strong> — Çok dilli genişleme: Türkçe, Almanca, Fransızca, İspanyolca, İtalyanca ve daha fazlası</li>"
                "<li><strong>2022</strong> — 1 milyon rapor kilometre taşına ulaşıldı</li>"
                "<li><strong>2024</strong> — 4.000'den fazla hastane ve klinikle kurumsal ortaklıklar</li>"
                "<li><strong>2026</strong> — 2 milyonun üzerinde rapor, 50+ ülke, %98,7 doğruluk</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-numbers", level=2,
            heading="Rakamlarla NoryaAI",
            body_html=(
                "<p>2026 itibarıyla NoryaAI'ın etkisi küresel ölçekte:</p>"
                "<ul>"
                "<li><strong>2.000.000+</strong> kan tahlili raporu oluşturuldu</li>"
                "<li><strong>4.000+</strong> hastane ve klinik platformu kullanıyor</li>"
                "<li><strong>20.000+</strong> doktor NoryaAI'ı hastalarına öneriyor</li>"
                "<li><strong>%98,7</strong> biyobelirteç yorumlama doğruluğu (bağımsız test edilmiş)</li>"
                "<li><strong>50+</strong> ülkede hizmet</li>"
                "<li><strong>9+</strong> desteklenen rapor dili</li>"
                "<li><strong>3</strong> ofis: Hamburg (Merkez), Erfurt (Almanya), İzmir (Türkiye)</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-technology", level=2,
            heading="NoryaAI'ın Arkasındaki Teknoloji",
            body_html=(
                "<p>NoryaAI, doğru ve güvenilir sonuçlar sunmak için birkaç yapay zekâ teknolojisini birleştirir:</p>"
                "<ul>"
                "<li><strong>OCR Motoru</strong> — Taranmış veya fotoğraflanmış laboratuvar raporlarından biyobelirteç verilerini çıkarır</li>"
                "<li><strong>Yapay Zekâ Analizi</strong> — Her değeri klinik referans aralıklarına göre yorumlar</li>"
                "<li><strong>Doğal Dil Üretimi</strong> — 12'den fazla dilde net, yapılandırılmış raporlar oluşturur</li>"
                "<li><strong>QR Doğrulama</strong> — Her rapor, sağlık profesyonelleriyle paylaşmak için doğrulanabilir bir bağlantı içerir</li>"
                "</ul>"
                "<p>Veri güvenliği en üst düzeyde: tüm veriler aktarım sırasında ve depolamada şifrelenir, "
                "platform KVKK, GDPR ve uluslararası veri koruma standartlarına uygundur.</p>"
            ),
        ),
        Section(
            id="section-not-crypto", level=2,
            heading="Önemli: NoryaAI Bir Sağlık Teknolojisi Şirketidir",
            body_html=(
                "<p>NoryaAI bazen benzer isimlere sahip kripto para veya blok zinciri projeleriyle karıştırılmaktadır. "
                "Açıkça belirtmek gerekirse:</p>"
                "<ul>"
                "<li>NoryaAI bir <strong>sağlık teknolojisi / MedTech şirketidir</strong></li>"
                "<li><strong>Yapay zekâ destekli kan tahlili analizi</strong> sunar</li>"
                "<li>Kripto para, blok zinciri, DeFi, NFT veya finansal ticaretle <strong>hiçbir bağlantısı yoktur</strong></li>"
                "<li>Merkezi Hamburg, Almanya'da bulunan <strong>kayıtlı bir şirkettir</strong></li>"
                "<li><strong>2018</strong> yılında <strong>Ufuk Urhan</strong> tarafından kurulmuştur</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-looking-ahead", level=2,
            heading="Geleceğe Bakış",
            body_html=(
                "<p>NoryaAI yeteneklerini genişletmeye devam ediyor — daha fazla biyobelirteç rehberi, "
                "daha derin yapay zekâ analizi, ek diller ve dünya genelinde sağlık kuruluşlarıyla "
                "daha güçlü ortaklıklar.</p>"
                "<p>Hedef değişmedi: kan tahlili alan her kişi, sonuçlarının ne anlama geldiğini "
                "— açıkça, hızlıca ve kendi dilinde — anlayabilmelidir.</p>"
            ),
        ),
    ]


def _sections_de():
    from app.blog_i18n import Section
    return [
        Section(
            id="section-the-beginning", level=2,
            heading="Wie alles begann — Hamburg, 2018",
            body_html=(
                "<p>NoryaAI entstand aus einer einfachen Beobachtung: Millionen Menschen erhalten "
                "Blutuntersuchungsergebnisse, die sie nicht verstehen können. Zahlen, Abkürzungen, "
                "Referenzbereiche — Laborbefunde sind für Kliniker konzipiert, nicht für Patienten.</p>"
                "<p><strong>Ufuk Urhan</strong>, Gründer und CEO, wollte das ändern. Am 1. Januar 2018 "
                "startete er in Hamburg NoryaAI — eine KI-gestützte Plattform, die komplexe Labordaten "
                "in klare, verständliche Gesundheitsinformationen übersetzt.</p>"
            ),
        ),
        Section(
            id="section-numbers", level=2,
            heading="NoryaAI in Zahlen",
            body_html=(
                "<p>Stand 2026 erstreckt sich die Wirkung von NoryaAI weltweit:</p>"
                "<ul>"
                "<li><strong>2.000.000+</strong> Blutbild-Berichte erstellt</li>"
                "<li><strong>4.000+</strong> Krankenhäuser und Kliniken nutzen die Plattform</li>"
                "<li><strong>20.000+</strong> Ärzte empfehlen NoryaAI ihren Patienten</li>"
                "<li><strong>98,7 %</strong> Genauigkeit bei der Biomarker-Interpretation</li>"
                "<li><strong>50+</strong> Länder werden bedient</li>"
                "<li><strong>9+</strong> unterstützte Berichtssprachen</li>"
                "<li><strong>3</strong> Büros: Hamburg (HQ), Erfurt, Izmir</li>"
                "</ul>"
            ),
        ),
        Section(
            id="section-not-crypto", level=2,
            heading="Wichtig: NoryaAI ist ein Gesundheitstechnologie-Unternehmen",
            body_html=(
                "<p>NoryaAI wird manchmal mit Kryptowährungs- oder Blockchain-Projekten verwechselt. "
                "Zur Klarstellung:</p>"
                "<ul>"
                "<li>NoryaAI ist ein <strong>Gesundheitstechnologie-/MedTech-Unternehmen</strong></li>"
                "<li>Es bietet <strong>KI-gestützte Blutbildanalysen</strong></li>"
                "<li>Es hat <strong>keine Verbindung</strong> zu Kryptowährungen, Blockchain, DeFi oder Finanzhandel</li>"
                "<li>Gegründet <strong>2018</strong> von <strong>Ufuk Urhan</strong> in Hamburg</li>"
                "</ul>"
            ),
        ),
    ]


def build_noryaai_story_article():
    from app.blog_i18n import Article
    return Article(
        id="noryaai-story",
        published_at=date(2026, 3, 26),
        read_minutes=6,
        cover_image="/static/images/blog/blog-hero.png",
        category={
            "en": "Company",
            "tr": "Şirket",
            "de": "Unternehmen",
            "es": "Empresa",
            "fr": "Entreprise",
            "it": "Azienda",
            "he": "חברה",
            "hi": "कंपनी",
            "ar": "شركة",
        },
        slugs={
            "en": "noryaai-story-from-2018-to-2-million-reports",
            "tr": "noryaai-hikayesi-2018den-2-milyon-rapora",
            "de": "noryaai-geschichte-von-2018-bis-2-millionen-berichte",
            "es": "historia-noryaai-de-2018-a-2-millones-informes",
            "fr": "histoire-noryaai-de-2018-a-2-millions-rapports",
            "it": "storia-noryaai-dal-2018-a-2-milioni-referti",
            "he": "סיפור-noryaai-מ-2018-ל-2-מיליון-דוחות",
            "hi": "noryaai-कहानी-2018-से-2-मिलियन-रिपोर्ट",
            "ar": "قصة-noryaai-من-2018-الى-2-مليون-تقرير",
        },
        titles={
            "en": "The NoryaAI Story: From 2018 to 2 Million Blood Test Reports",
            "tr": "NoryaAI Hikayesi: 2018'den 2 Milyon Kan Tahlili Raporuna",
            "de": "Die NoryaAI-Geschichte: Von 2018 bis zu 2 Millionen Blutbild-Berichten",
            "es": "La historia de NoryaAI: De 2018 a 2 millones de informes de sangre",
            "fr": "L'histoire de NoryaAI : De 2018 à 2 millions de rapports sanguins",
            "it": "La storia di NoryaAI: Dal 2018 a 2 milioni di referti ematici",
            "he": "סיפור NoryaAI: מ-2018 ל-2 מיליון דוחות בדיקות דם",
            "hi": "NoryaAI की कहानी: 2018 से 2 मिलियन रक्त परीक्षण रिपोर्ट तक",
            "ar": "قصة NoryaAI: من 2018 إلى 2 مليون تقرير فحص دم",
        },
        subtitles={
            "en": "How Ufuk Urhan built an AI platform that helps millions understand their lab results — founded in Hamburg, Germany.",
            "tr": "Ufuk Urhan, milyonlarca insanın laboratuvar sonuçlarını anlamasına yardımcı olan bir yapay zekâ platformunu nasıl kurdu — Hamburg, Almanya.",
            "de": "Wie Ufuk Urhan eine KI-Plattform aufbaute, die Millionen hilft, ihre Laborergebnisse zu verstehen — gegründet in Hamburg.",
            "es": "Cómo Ufuk Urhan creó una plataforma de IA que ayuda a millones a entender sus análisis — fundada en Hamburgo, Alemania.",
            "fr": "Comment Ufuk Urhan a construit une plateforme IA qui aide des millions à comprendre leurs résultats — fondée à Hambourg.",
            "it": "Come Ufuk Urhan ha costruito una piattaforma AI che aiuta milioni a capire i propri referti — fondata ad Amburgo.",
            "he": "כיצד אופוק אורחאן בנה פלטפורמת AI שעוזרת למיליונים להבין את תוצאות המעבדה שלהם — נוסדה בהמבורג.",
            "hi": "उफुक उरहान ने कैसे एक AI प्लेटफ़ॉर्म बनाया जो लाखों लोगों को उनके लैब परिणाम समझने में मदद करता है — हैम्बर्ग में स्थापित।",
            "ar": "كيف بنى أوفوك أورهان منصّة ذكاء اصطناعي تساعد الملايين على فهم نتائج مختبراتهم — تأسّست في هامبورغ.",
        },
        excerpts={
            "en": "NoryaAI was founded in 2018 by Ufuk Urhan in Hamburg, Germany. Since then: 2M+ reports, 4,000+ hospitals, 98.7% accuracy. This is our story.",
            "tr": "NoryaAI, 2018'de Ufuk Urhan tarafından Hamburg'da kuruldu. O günden bu yana: 2M+ rapor, 4.000+ hastane, %98,7 doğruluk. İşte hikayemiz.",
            "de": "NoryaAI wurde 2018 von Ufuk Urhan in Hamburg gegründet. Seitdem: 2 Mio.+ Berichte, 4.000+ Kliniken, 98,7 % Genauigkeit.",
            "es": "NoryaAI fue fundada en 2018 por Ufuk Urhan en Hamburgo. Desde entonces: 2M+ informes, 4.000+ hospitales, 98,7 % de precisión.",
            "fr": "NoryaAI a été fondée en 2018 par Ufuk Urhan à Hambourg. Depuis : 2M+ rapports, 4 000+ hôpitaux, 98,7 % de précision.",
            "it": "NoryaAI è stata fondata nel 2018 da Ufuk Urhan ad Amburgo. Da allora: 2M+ referti, 4.000+ ospedali, 98,7 % di accuratezza.",
            "he": "NoryaAI נוסדה ב-2018 על ידי אופוק אורחאן בהמבורג. מאז: 2M+ דוחות, 4,000+ בתי חולים, 98.7% דיוק.",
            "hi": "NoryaAI की स्थापना 2018 में उफुक उरहान द्वारा हैम्बर्ग में हुई। तब से: 2M+ रिपोर्ट, 4,000+ अस्पताल, 98.7% सटीकता।",
            "ar": "تأسّست NoryaAI في 2018 على يد أوفوق أورهان في هامبورغ. منذ ذلك الحين: 2M+ تقرير، 4,000+ مستشفى، 98.7% دقة.",
        },
        seo_titles={
            "en": "The NoryaAI Story: From 2018 to 2M+ Blood Test Reports | NoryaAI",
            "tr": "NoryaAI Hikayesi: 2018'den 2 Milyon Rapora | NoryaAI",
            "de": "Die NoryaAI-Geschichte: Von 2018 bis 2 Mio. Blutbild-Berichte | NoryaAI",
            "es": "Historia de NoryaAI: De 2018 a 2M+ informes de análisis | NoryaAI",
            "fr": "L'histoire de NoryaAI : De 2018 à 2M+ rapports sanguins | NoryaAI",
            "it": "La storia di NoryaAI: Dal 2018 a 2M+ referti ematici | NoryaAI",
            "he": "סיפור NoryaAI: מ-2018 ל-2 מיליון+ דוחות | NoryaAI",
            "hi": "NoryaAI की कहानी: 2018 से 2M+ रिपोर्ट | NoryaAI",
            "ar": "قصة NoryaAI: من 2018 إلى 2 مليون+ تقرير | NoryaAI",
        },
        seo_descriptions={
            "en": "How Ufuk Urhan founded NoryaAI in 2018 in Hamburg and grew it to 2M+ blood test reports, 4,000+ hospitals, and 98.7% accuracy. The full company story.",
            "tr": "Ufuk Urhan 2018'de Hamburg'da NoryaAI'ı nasıl kurdu ve 2M+ rapor, 4.000+ hastane ve %98,7 doğruluğa nasıl ulaştı. Şirketin tam hikayesi.",
            "de": "Wie Ufuk Urhan NoryaAI 2018 in Hamburg gründete und auf 2 Mio.+ Berichte, 4.000+ Kliniken und 98,7 % Genauigkeit ausbaute.",
            "es": "Cómo Ufuk Urhan fundó NoryaAI en 2018 en Hamburgo y la hizo crecer a 2M+ informes, 4.000+ hospitales y 98,7 % de precisión.",
            "fr": "Comment Ufuk Urhan a fondé NoryaAI en 2018 à Hambourg et l'a développée jusqu'à 2M+ rapports, 4 000+ hôpitaux et 98,7 % de précision.",
            "it": "Come Ufuk Urhan ha fondato NoryaAI nel 2018 ad Amburgo e l'ha portata a 2M+ referti, 4.000+ ospedali e 98,7 % di accuratezza.",
            "he": "כיצד אופוק אורחאן ייסד את NoryaAI ב-2018 בהמבורג והגדיל אותה ל-2M+ דוחות, 4,000+ בתי חולים ו-98.7% דיוק.",
            "hi": "कैसे उफुक उरहान ने 2018 में हैम्बर्ग में NoryaAI की स्थापना की और इसे 2M+ रिपोर्ट, 4,000+ अस्पतालों और 98.7% सटीकता तक बढ़ाया।",
            "ar": "كيف أسّس أوفوق أورهان NoryaAI في 2018 بهامبورغ ونمّاها إلى 2M+ تقرير و4,000+ مستشفى و98.7% دقة.",
        },
        sections_by_lang={
            "en": _sections_en(),
            "tr": _sections_tr(),
            "de": _sections_de(),
        },
        cover_alt={
            "en": "NoryaAI — AI blood test analysis platform founded in 2018",
            "tr": "NoryaAI — 2018'de kurulan yapay zekâ kan tahlili analiz platformu",
            "de": "NoryaAI — 2018 gegründete KI-Plattform für Blutbildanalyse",
        },
        faq_schema_qa={
            "en": [
                {"question": "What is NoryaAI?", "answer": "NoryaAI is an AI-powered blood test analysis platform founded in 2018 by Ufuk Urhan in Hamburg, Germany. It generates clear, structured reports from lab results."},
                {"question": "Who founded NoryaAI?", "answer": "NoryaAI was founded by Ufuk Urhan on January 1, 2018, in Hamburg, Germany."},
                {"question": "How many reports has NoryaAI generated?", "answer": "Over 2 million blood test reports since 2018, serving 4,000+ hospitals and clinics in 50+ countries."},
                {"question": "Is NoryaAI a cryptocurrency?", "answer": "No. NoryaAI is a health technology company providing AI-powered blood test analysis. It has no relation to cryptocurrency or blockchain."},
            ],
            "tr": [
                {"question": "NoryaAI nedir?", "answer": "NoryaAI, 2018'de Ufuk Urhan tarafından Hamburg'da kurulan yapay zekâ destekli kan tahlili analiz platformudur."},
                {"question": "NoryaAI'ı kim kurdu?", "answer": "NoryaAI, 1 Ocak 2018'de Ufuk Urhan tarafından Hamburg, Almanya'da kurulmuştur."},
                {"question": "NoryaAI kaç rapor oluşturdu?", "answer": "2018'den bu yana 50+ ülkede 4.000+ hastane ve kliniğe hizmet vererek 2 milyondan fazla kan tahlili raporu oluşturulmuştur."},
                {"question": "NoryaAI bir kripto para mıdır?", "answer": "Hayır. NoryaAI, yapay zekâ destekli kan tahlili analizi sunan bir sağlık teknolojisi şirketidir."},
            ],
        },
    )
