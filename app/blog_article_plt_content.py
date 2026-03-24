# -*- coding: utf-8 -*-
"""
PLT (Platelet) blog article — full body content for all 9 languages.
Sections: intro, what-are-platelets, role-in-clotting, normal-ranges,
high-platelet-causes, low-platelet-causes, mpv-connection, symptoms,
when-to-see-doctor, how-norya-helps, disclaimer.
"""
from __future__ import annotations

LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")

_TABLE_STYLE = (
    '<table class="w-full border border-slate-200 text-sm my-4" '
    'style="border-collapse: collapse;">'
)
_TH = 'style="border:1px solid #cbd5e1;padding:8px 12px;text-align:left;"'
_TD = 'style="border:1px solid #cbd5e1;padding:8px 12px;"'


# ─────────────────────────────────────────────────────────────────────
# TURKISH
# ─────────────────────────────────────────────────────────────────────
def _sections_tr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="PLT (Trombosit) testi: Sonuçlarınız ne anlama geliyor?",
            body_html=(
                "<p>Tam kan sayımınızda (CBC) yer alan <strong>PLT (trombosit)</strong> değeri, kanınızdaki "
                "trombosit sayısını gösterir. Trombositler, kanamayı durduran pıhtılaşma sürecinin baş aktörleridir; "
                "bir damar hasarlandığında hızla bölgeye yığılarak geçici bir tıkaç oluşturur ve ardından pıhtılaşma "
                "faktörleriyle birlikte çalışarak kalıcı bir pıhtı meydana getirirler.</p>"
                "<p>Trombosit sayısının normalden yüksek (trombositoz) veya düşük (trombositopeni) çıkması "
                "çeşitli sağlık durumlarına işaret edebilir. Enfeksiyonlar, iltihabi hastalıklar, demir eksikliği, "
                "karaciğer sorunları, otoimmün hastalıklar ve kemik iliği bozuklukları trombosit sayısını "
                "doğrudan etkileyen faktörler arasındadır.</p>"
                "<p>Bu rehber, trombosit sayınızı nasıl yorumlayacağınızı, yüksek ve düşük değerlerin olası "
                "nedenlerini, MPV ile ilişkisini ve ne zaman hekime başvurmanız gerektiğini kapsamlı biçimde "
                "açıklamaktadır. <em>Bu makale eğitim amaçlıdır; tıbbi teşhis veya tedavi yerine geçmez.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="Trombositler (plateletler) nedir?",
            body_html=(
                "<p><strong>Trombositler (plateletler)</strong>, kemik iliğindeki megakaryosit adı verilen dev "
                "hücrelerden koparak kan dolaşımına katılan küçük, çekirdeksiz hücre parçacıklarıdır. Her bir "
                "megakaryosit binlerce trombosit üretebilir. Trombositlerin çapı yalnızca 2–3 mikrometre olup "
                "kırmızı ve beyaz kan hücrelerinden çok daha küçüktürler; ancak vücuttaki rolleri son derece "
                "kritiktir.</p>"
                "<p>Kan dolaşımında yaklaşık 7–10 gün yaşayan trombositler, ömürlerini tamamladıktan sonra "
                "ağırlıklı olarak dalak tarafından temizlenir. Dalak aynı zamanda toplam trombositlerin "
                "yaklaşık üçte birini depolayan bir rezervuar görevi görür; bu nedenle dalak büyümesi "
                "(splenomegali) dolaşımdaki trombosit sayısını düşürebilir.</p>"
                "<p>Trombositler yalnızca pıhtılaşma ile sınırlı kalmayıp, bağışıklık yanıtında, iltihabi "
                "süreçlerde, anjiyogenezde (yeni damar oluşumu) ve yara iyileşmesinde de aktif rol oynarlar. "
                "İçerdikleri granüller büyüme faktörleri, sitokinler ve vazoaktif maddeler salgılayarak "
                "doku onarımını destekler.</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="Trombositlerin pıhtılaşmadaki rolü",
            body_html=(
                "<p>Bir damar duvarı hasar gördüğünde, subendotelyal kollajen açığa çıkar ve trombositler "
                "bu yüzeye <strong>adezyon</strong> (yapışma) gerçekleştirir. Bu ilk temas, von Willebrand "
                "faktörü (vWF) aracılığıyla sağlanır. Yapışan trombositler aktive olur; şekillerini değiştirerek "
                "yalancı ayak (pseudopod) uzantıları oluştururlar ve granüllerinden ADP, tromboksan A2 ve "
                "serotonin gibi maddeler salgılarlar.</p>"
                "<p>Bu salgılanan maddeler çevredeki diğer trombositleri çekerek <strong>agregasyonu</strong> "
                "(kümelenme) başlatır. Trombosit yüzeyindeki GP IIb/IIIa reseptörleri fibrinojen köprüleri "
                "aracılığıyla birbirine bağlanır ve böylece <em>birincil hemostatik tıkaç</em> oluşur. Bu "
                "geçici tıkaç, küçük damar yaralanmalarında kanamayı birkaç dakika içinde durdurabilir.</p>"
                "<p>Ardından koagülasyon kaskadı devreye girer; trombin oluşumu fibrinojeni fibrine dönüştürerek "
                "trombosit tıkacını güçlendirir. Sonuçta oluşan <strong>stabil pıhtı</strong> (sekonder hemostaz), "
                "damar onarımı tamamlanana kadar bölgeyi korur. Trombosit sayısı veya işlevindeki bozukluklar, "
                "bu hassas dengeyi bozarak aşırı kanamaya ya da istenmeyen pıhtı oluşumuna yol açabilir.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal trombosit (PLT) değerleri",
            body_html=(
                "<p>Trombosit sayısı tam kan sayımı (CBC) ile ölçülür ve sonuçlar genellikle "
                "bin/μL (×10³/μL) veya hücre/μL cinsinden raporlanır:</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>Parametre</th><th {_TH}>Normal aralık</th>'
                f'<th {_TH}>Not</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (Yetişkin)</td><td {_TD}>150.000–400.000/μL</td>'
                f'<td {_TD}>Her iki cinsiyet için aynı</td></tr>'
                f'<tr><td {_TD}>PLT (Yenidoğan)</td><td {_TD}>150.000–450.000/μL</td>'
                f'<td {_TD}>İlk haftalarda biraz daha geniş aralık</td></tr>'
                f'<tr><td {_TD}>MPV (Ortalama Trombosit Hacmi)</td><td {_TD}>7,5–12,0 fL</td>'
                f'<td {_TD}>Trombosit boyutunu gösterir</td></tr>'
                '</tbody></table>'
                "<p>Trombosit sayısı gün içinde fizyolojik dalgalanma gösterebilir. Yoğun egzersiz sonrası "
                "geçici artış, menstrüasyon döneminde hafif düşüş ve yüksek rakımlarda artış gözlenebilir. "
                "Bazı kişilerde <strong>psödotrombositopeni</strong> (EDTA'ya bağlı in-vitro trombosit "
                "kümelenmesi) nedeniyle yanlışlıkla düşük sayı raporlanabilir; bu durumda sitrat tüpünde "
                "tekrar ölçüm yapılmalıdır.</p>"
                "<p>Laboratuvarlar arasında referans aralıkları az da olsa farklılık gösterebilir; bu nedenle "
                "sonuçlarınızı her zaman raporunuzdaki referans aralığıyla karşılaştırmanız önerilir.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="Yüksek trombosit (trombositoz) nedenleri",
            body_html=(
                "<p><strong>Trombositoz</strong>, trombosit sayısının 400.000/μL'nin üzerinde olması durumudur. "
                "İki ana kategoride incelenir:</p>"
                "<p><strong>1. Reaktif (sekonder) trombositoz:</strong> Altta yatan başka bir duruma tepki olarak "
                "trombosit üretiminin artmasıdır ve vakaların büyük çoğunluğunu oluşturur. Başlıca nedenleri:</p>"
                "<ul>"
                "<li><strong>Enfeksiyonlar</strong> — Akut bakteriyel, viral veya fungal enfeksiyonlar sırasında "
                "IL-6 gibi sitokinler megakaryopoezi uyarır.</li>"
                "<li><strong>Kronik iltihabi hastalıklar</strong> — Romatoid artrit, inflamatuvar bağırsak "
                "hastalığı (IBD), vaskülitler.</li>"
                "<li><strong>Demir eksikliği anemisi</strong> — Demir eksikliğinde trombopoetin reseptör "
                "çapraz reaktivitesi trombosit üretimini artırır.</li>"
                "<li><strong>Cerrahi ve travma</strong> — Postoperatif dönemde akut faz yanıtı olarak geçici artış.</li>"
                "<li><strong>Splenektomi</strong> — Dalak çıkarıldığında, normalde dalakta depolanan trombositler "
                "dolaşıma katılır ve kalıcı trombositoz gelişebilir.</li>"
                "<li><strong>Malignite</strong> — Bazı kanser türlerinde paraneoplastik trombositoz görülebilir.</li>"
                "</ul>"
                "<p><strong>2. Primer (klonal) trombositoz:</strong> Kemik iliğindeki kök hücre düzeyinde bir "
                "bozukluktan kaynaklanır. Miyeloproliferatif neoplazmlar (esansiyel trombositemi, polisitemia "
                "vera, kronik miyeloid lösemi) bu gruba girer. Primer trombositozda JAK2, CALR veya MPL "
                "mutasyonları sıklıkla saptanır ve hem tromboz hem de kanama riski artar.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="Düşük trombosit (trombositopeni) nedenleri",
            body_html=(
                "<p><strong>Trombositopeni</strong>, trombosit sayısının 150.000/μL'nin altında olması "
                "durumudur. Üç ana mekanizmayla gelişir:</p>"
                "<p><strong>1. Üretim azalması (kemik iliği baskılanması):</strong></p>"
                "<ul>"
                "<li><strong>Aplastik anemi</strong> — Kemik iliği yetersizliği tüm kan hücre serilerini etkiler.</li>"
                "<li><strong>Lösemi, lenfoma ve metastatik kanser</strong> — Kemik iliğini infiltre eden "
                "malign hücreler normal megakaryopoezi baskılar.</li>"
                "<li><strong>Miyelodisplastik sendrom (MDS)</strong> — Anormal hematopoez sonucu düşük ve "
                "işlevsel olmayan trombositler üretilir.</li>"
                "<li><strong>B12/folat eksikliği</strong> — Megaloblastik anemi trombositopeni ile birlikte olabilir.</li>"
                "<li><strong>Kemoterapi/radyoterapi</strong> — Kemik iliği baskılayıcı tedaviler geçici "
                "trombositopeniye yol açar.</li>"
                "</ul>"
                "<p><strong>2. Yıkım artışı (periferik tüketim):</strong></p>"
                "<ul>"
                "<li><strong>İmmün trombositopenik purpura (ITP)</strong> — Otoimmün antikorlar trombositleri "
                "hedef alarak dalakta yıkımlarını hızlandırır. Çocuklarda viral enfeksiyon sonrası akut, "
                "yetişkinlerde çoğunlukla kroniktir.</li>"
                "<li><strong>Trombotik trombositopenik purpura (TTP)</strong> — ADAMTS13 eksikliğine bağlı "
                "mikroanjiyopatik hemolitik anemi ve trombositopeni.</li>"
                "<li><strong>Heparine bağlı trombositopeni (HIT)</strong> — Heparin tedavisi sırasında "
                "gelişen antikor aracılı paradoks tromboz ve trombositopeni.</li>"
                "<li><strong>Dissemine intravasküler koagülasyon (DIC)</strong> — Yaygın pıhtılaşma "
                "aktivasyonu trombositleri tüketir.</li>"
                "</ul>"
                "<p><strong>3. Dalakta tutulma (sekestrasyon):</strong> Karaciğer sirozu, portal hipertansiyon "
                "veya diğer nedenlerle dalak büyüdüğünde (hipersplenizm), trombositlerin dalakta tutulma "
                "oranı artar ve dolaşımdaki sayı düşer. İlaç kaynaklı trombositopeni de (kinidin, valproik "
                "asit, sülfanomidler, bazı antibiyotikler) sık görülen bir nedendir.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="MPV (Ortalama Trombosit Hacmi) ile ilişkisi",
            body_html=(
                "<p><strong>MPV (Mean Platelet Volume — Ortalama Trombosit Hacmi)</strong>, trombositlerin "
                "ortalama boyutunu femtolitre (fL) cinsinden ölçer. Normal MPV aralığı genellikle "
                "7,5–12,0 fL arasındadır. MPV değeri, trombosit üretiminin hızı ve kemik iliğinin durumu "
                "hakkında bilgi verir.</p>"
                "<p><strong>Yüksek MPV + düşük PLT:</strong> Kemik iliği trombosit kaybını telafi etmek için "
                "daha büyük, daha genç trombositler ürettiğini gösterir. Bu durum ITP gibi periferik yıkım "
                "nedenlerinde tipiktir. Genç, büyük trombositler daha fazla granül içerir ve hemostatik "
                "olarak daha aktiftir.</p>"
                "<p><strong>Düşük MPV + düşük PLT:</strong> Kemik iliğinin yeterli trombosit üretemediğine "
                "işaret edebilir (aplastik anemi, kemoterapi sonrası baskılanma, miyelodisplastik sendrom). "
                "Kemik iliğinin kompansatuar yanıt veremediği durumlarda hem sayı hem boyut düşer.</p>"
                "<p>Yüksek MPV ayrıca kardiyovasküler risk ile de ilişkilendirilmiştir. Büyük trombositler "
                "daha agregasyona yatkındır ve miyokard enfarktüsü, inme gibi trombotik olaylarda bağımsız "
                "bir risk faktörü olarak öne çıkmaktadır. MPV ile ilgili ayrıntılı bilgi için "
                '<a href="/blog/mpv-blood-test">MPV makalemize</a> göz atabilirsiniz.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Yüksek ve düşük trombosit belirtileri",
            body_html=(
                "<p><strong>Trombositopeni (düşük PLT) belirtileri:</strong></p>"
                "<ul>"
                "<li><strong>Peteşi</strong> — Ciltte iğne ucu büyüklüğünde kırmızı-mor lekeler; basınçla solmaz.</li>"
                "<li><strong>Purpura</strong> — Daha geniş çaplı morumsu cilt altı kanamalar.</li>"
                "<li><strong>Ekimoz</strong> — Küçük travmalarla orantısız morluklar.</li>"
                "<li><strong>Diş eti kanaması</strong> — Fırçalama sırasında aşırı kanama.</li>"
                "<li><strong>Burun kanaması (epistaksis)</strong> — Sık tekrarlayan ve durdurulamayan burun kanamaları.</li>"
                "<li><strong>Ağır menstrüel kanama (menoraji)</strong> — Normalden çok daha uzun ve yoğun adet dönemleri.</li>"
                "<li><strong>Gastrointestinal kanama</strong> — Ciddi trombositopenide melena veya hematemez.</li>"
                "</ul>"
                "<p><strong>Trombositoz (yüksek PLT) belirtileri:</strong> Reaktif trombositoz genellikle "
                "asemptomatiktir ve altta yatan hastalığın belirtileri ön plandadır. Ancak primer "
                "trombositozda (esansiyel trombositemi gibi) aşağıdaki belirtiler görülebilir:</p>"
                "<ul>"
                "<li><strong>Eritromelalji</strong> — El ve ayaklarda yanıcı ağrı, kızarıklık ve sıcaklık.</li>"
                "<li><strong>Baş ağrısı ve görme bozuklukları</strong> — Mikrodolaşım bozukluklarına bağlı.</li>"
                "<li><strong>Tromboz</strong> — Derin ven trombozu (DVT), pulmoner emboli, inme veya miyokard enfarktüsü riski.</li>"
                "<li><strong>Paradoks kanama</strong> — Çok yüksek trombosit sayılarında (>1.000.000/μL) edinsel von Willebrand hastalığı gelişebilir.</li>"
                "</ul>"
                "<p>Trombosit sayısı 50.000/μL'nin altına düştüğünde spontan kanama riski artar; "
                "10.000–20.000/μL altında ise hayatı tehdit eden iç kanamalar gelişebilir.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Ne zaman doktora başvurmalısınız?",
            body_html=(
                "<p>Aşağıdaki durumlardan herhangi biri varsa en kısa sürede bir hekime başvurmanız "
                "önerilir:</p>"
                "<ul>"
                "<li>Trombosit sayınız <strong>150.000/μL altında veya 400.000/μL üzerinde</strong> çıktıysa.</li>"
                "<li>Cildinizde açıklanamayan peteşi, purpura veya morluklar fark ediyorsanız.</li>"
                "<li>Sık tekrarlayan veya durdurulamayan burun ya da diş eti kanaması yaşıyorsanız.</li>"
                "<li>Ameliyat veya diş çekimi sonrası uzun süre kanama devam ediyorsa.</li>"
                "<li>El ve ayaklarınızda açıklanamayan yanma, ağrı veya kızarıklık (eritromelalji) varsa.</li>"
                "<li>Daha önceki testlerinize göre trombosit sayınızda belirgin bir artış veya düşüş trendi görülüyorsa.</li>"
                "</ul>"
                "<p>Doktorunuz gerekli gördüğü takdirde periferik yayma, kemik iliği biyopsisi, retiküle "
                "trombosit sayısı, trombopoietin düzeyi veya genetik testler (JAK2, CALR, MPL mutasyonları) "
                "gibi ileri tetkikler isteyebilir. Erken tanı, özellikle hematolojik hastalıklarda tedavi "
                "başarısını doğrudan etkileyen kritik bir faktördür.</p>"
                "<p>Trombosit sayısı çok düşükse (<20.000/μL) ve aktif kanama belirtileri varsa, "
                "bu bir <strong>tıbbi acildir</strong> ve derhal acil servise başvurulmalıdır.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya sonuçlarınızı anlamanıza nasıl yardımcı olur?",
            body_html=(
                "<p>Kan tahlili sonuçlarınızı <a href=\"/analyze\">Norya'ya yükleyerek</a> PLT, MPV ve diğer "
                "hematolojik parametrelerinizin yapılandırılmış, anlaşılır bir özetini dakikalar içinde "
                "alabilirsiniz. Norya, değerlerinizi referans aralıklarıyla karşılaştırır, olası sapmaları "
                "vurgular ve sonuçlarınızı bütüncül bir perspektifle sunar.</p>"
                "<p>Bu özet, hekim randevunuza hazırlanmanız için ideal bir araçtır: hangi değerlerin "
                "dikkat gerektirdiğini, birbiriyle ilişkili parametreleri ve genel tablonuzu net biçimde "
                "görebilirsiniz. <strong>Norya teşhis koymaz</strong>, ancak sonuçlarınızı anlamanızı "
                "ve doktorunuzla daha verimli bir görüşme yapmanızı sağlar.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Uyarı",
            body_html=(
                '<p><strong>Bu rehber bilgilendirme amaçlıdır; tıbbi tavsiye veya teşhis yerine geçmez.'
                '</strong> Sonuçlarınızı mutlaka bir sağlık uzmanıyla değerlendirin. '
                '<a href="/analyze">Norya ile analiz başlat</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ENGLISH
# ─────────────────────────────────────────────────────────────────────
def _sections_en() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="PLT (Platelet) test: What your results mean",
            body_html=(
                "<p>Your <strong>PLT (platelet count)</strong> is one of the key values reported on a complete "
                "blood count (CBC). Platelets — also called thrombocytes — are tiny, disc-shaped cell fragments "
                "produced by megakaryocytes in the bone marrow. Their primary job is to stop bleeding by forming "
                "clots at the site of vascular injury.</p>"
                "<p>A platelet count that is higher than normal (thrombocytosis) or lower than normal "
                "(thrombocytopenia) can signal a wide range of medical conditions — from infections and "
                "iron deficiency to autoimmune diseases and bone marrow disorders. Understanding your "
                "platelet count in context is essential for identifying potential health concerns early.</p>"
                "<p>This comprehensive guide explains what platelets are, how they work, what normal "
                "values look like, causes of abnormal counts, the relationship between PLT and MPV, "
                "symptoms to watch for, and when to consult a doctor. <em>This article is for educational "
                "purposes only and does not replace professional medical advice.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="What are platelets (thrombocytes)?",
            body_html=(
                "<p><strong>Platelets (thrombocytes)</strong> are small, anucleate cell fragments that circulate "
                "in the bloodstream. They are produced in the bone marrow by giant precursor cells called "
                "<strong>megakaryocytes</strong>. A single megakaryocyte can shed thousands of platelets into "
                "the circulation. Each platelet is only about 2–3 micrometres in diameter — far smaller than "
                "red or white blood cells — yet they play an outsized role in maintaining vascular integrity.</p>"
                "<p>Platelets have a lifespan of approximately 7–10 days. Once they age, they are removed "
                "primarily by the spleen, which also serves as a reservoir holding roughly one-third of the "
                "body's total platelet pool. This is why conditions that enlarge the spleen (splenomegaly) "
                "can sequester platelets and reduce the circulating count.</p>"
                "<p>Beyond hemostasis, platelets contribute to innate immunity by releasing antimicrobial "
                "peptides and interacting with leukocytes. They also secrete growth factors (e.g., PDGF, TGF-β) "
                "that promote wound healing, tissue repair, and angiogenesis. Platelet-rich plasma (PRP) "
                "therapy leverages these regenerative properties in orthopedic and dermatologic medicine.</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="How platelets work in blood clotting",
            body_html=(
                "<p>When a blood vessel is damaged, the underlying collagen is exposed, and platelets immediately "
                "<strong>adhere</strong> to the injured surface. This initial contact is mediated by "
                "<strong>von Willebrand factor (vWF)</strong>, a glycoprotein that acts as molecular glue between "
                "platelet receptors (GP Ib/IX/V) and collagen. Upon adhesion, platelets become activated: they "
                "change from smooth discs to spiny spheres with pseudopodia that interlock with one another.</p>"
                "<p>Activated platelets release the contents of their dense granules — ADP, thromboxane A2 (TXA2), "
                "and serotonin — which recruit additional platelets to the site. Simultaneously, the GP IIb/IIIa "
                "receptors on the platelet surface undergo a conformational change that allows them to bind "
                "fibrinogen, cross-linking adjacent platelets. This process is called <strong>aggregation</strong> "
                "and produces the <em>primary hemostatic plug</em>, which can stop bleeding from small vessels "
                "within minutes.</p>"
                "<p>The coagulation cascade then reinforces this initial plug. Tissue factor activates a chain of "
                "clotting factors that ultimately generates <strong>thrombin</strong>, which converts soluble "
                "fibrinogen into insoluble fibrin strands. The fibrin mesh stabilizes the platelet plug, forming "
                "the definitive <strong>secondary hemostatic clot</strong>. Any defect in platelet number or "
                "function — whether too few, too many, or dysfunctional — can tip the balance toward excessive "
                "bleeding or pathologic thrombosis.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normal platelet (PLT) ranges",
            body_html=(
                "<p>Platelet count is measured as part of the complete blood count (CBC) and is reported in "
                "thousands per microlitre (×10³/μL) or cells per microlitre:</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>Parameter</th><th {_TH}>Normal range</th>'
                f'<th {_TH}>Note</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (Adults)</td><td {_TD}>150,000–400,000/μL</td>'
                f'<td {_TD}>Same for both sexes</td></tr>'
                f'<tr><td {_TD}>PLT (Neonates)</td><td {_TD}>150,000–450,000/μL</td>'
                f'<td {_TD}>Slightly wider range in the first weeks</td></tr>'
                f'<tr><td {_TD}>MPV (Mean Platelet Volume)</td><td {_TD}>7.5–12.0 fL</td>'
                f'<td {_TD}>Indicates platelet size</td></tr>'
                '</tbody></table>'
                "<p>Platelet counts can fluctuate physiologically throughout the day. Transient increases "
                "occur after vigorous exercise, stress, and epinephrine release. A mild decrease may be "
                "observed during menstruation. High altitude living can also elevate counts. Some "
                "individuals may exhibit <strong>pseudothrombocytopenia</strong> — a falsely low count "
                "caused by EDTA-dependent platelet clumping in the collection tube. If suspected, a repeat "
                "sample drawn into a citrate tube usually resolves the discrepancy.</p>"
                "<p>Reference intervals can vary slightly between laboratories; always compare your result "
                "to the reference range printed on your specific lab report.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="Causes of high platelets (thrombocytosis)",
            body_html=(
                "<p><strong>Thrombocytosis</strong> is defined as a platelet count exceeding 400,000/μL. "
                "It is classified into two major categories:</p>"
                "<p><strong>1. Reactive (secondary) thrombocytosis</strong> accounts for the vast majority "
                "of cases and occurs as a response to an underlying condition:</p>"
                "<ul>"
                "<li><strong>Infections</strong> — Acute bacterial, viral, or fungal infections stimulate "
                "megakaryopoiesis through cytokines such as IL-6 and thrombopoietin.</li>"
                "<li><strong>Chronic inflammatory diseases</strong> — Rheumatoid arthritis, inflammatory "
                "bowel disease (IBD), and vasculitis drive sustained platelet production.</li>"
                "<li><strong>Iron deficiency anemia</strong> — Iron deficiency stimulates thrombopoiesis "
                "through cross-reactivity of thrombopoietin receptors with erythropoietin pathways.</li>"
                "<li><strong>Surgery and trauma</strong> — Postoperative acute-phase response causes "
                "transient thrombocytosis, typically peaking 1–2 weeks after the event.</li>"
                "<li><strong>Splenectomy</strong> — Removal of the spleen releases sequestered platelets "
                "and removes the primary site of platelet clearance, often causing persistent elevation.</li>"
                "<li><strong>Malignancy</strong> — Some cancers (lung, ovarian, GI) can cause "
                "paraneoplastic thrombocytosis.</li>"
                "</ul>"
                "<p><strong>2. Primary (clonal) thrombocytosis</strong> arises from a stem-cell-level defect "
                "in the bone marrow. Myeloproliferative neoplasms — essential thrombocythemia (ET), polycythemia "
                "vera (PV), and chronic myeloid leukemia (CML) — fall into this category. Mutations in "
                "<em>JAK2</em>, <em>CALR</em>, or <em>MPL</em> genes are commonly identified. Primary "
                "thrombocytosis carries a heightened risk of both thrombotic and hemorrhagic complications.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="Causes of low platelets (thrombocytopenia)",
            body_html=(
                "<p><strong>Thrombocytopenia</strong> is defined as a platelet count below 150,000/μL. "
                "It can result from three broad mechanisms:</p>"
                "<p><strong>1. Decreased production (bone marrow suppression):</strong></p>"
                "<ul>"
                "<li><strong>Aplastic anemia</strong> — Bone marrow failure affecting all cell lineages.</li>"
                "<li><strong>Leukemia, lymphoma, and metastatic cancer</strong> — Malignant infiltration "
                "crowds out normal megakaryopoiesis.</li>"
                "<li><strong>Myelodysplastic syndrome (MDS)</strong> — Abnormal hematopoiesis produces "
                "low and dysfunctional platelets.</li>"
                "<li><strong>Vitamin B12/folate deficiency</strong> — Megaloblastic anemia may present "
                "with concurrent thrombocytopenia due to ineffective platelet production.</li>"
                "<li><strong>Chemotherapy/radiation</strong> — Myelosuppressive treatments cause transient "
                "thrombocytopenia, often nadir at 7–14 days post-treatment.</li>"
                "</ul>"
                "<p><strong>2. Increased destruction (peripheral consumption):</strong></p>"
                "<ul>"
                "<li><strong>Immune thrombocytopenic purpura (ITP)</strong> — Autoimmune antibodies target "
                "platelet surface glycoproteins, leading to accelerated splenic destruction. Acute ITP is "
                "common in children following viral illness; chronic ITP predominates in adults.</li>"
                "<li><strong>Thrombotic thrombocytopenic purpura (TTP)</strong> — ADAMTS13 deficiency causes "
                "microangiopathic hemolytic anemia and severe thrombocytopenia.</li>"
                "<li><strong>Heparin-induced thrombocytopenia (HIT)</strong> — An antibody-mediated paradoxical "
                "prothrombotic state triggered by heparin therapy.</li>"
                "<li><strong>Disseminated intravascular coagulation (DIC)</strong> — Widespread activation of "
                "clotting cascades consumes platelets and clotting factors simultaneously.</li>"
                "</ul>"
                "<p><strong>3. Splenic sequestration:</strong> When the spleen enlarges due to liver cirrhosis, "
                "portal hypertension, or infiltrative diseases (e.g., Gaucher disease), it traps a larger "
                "proportion of platelets, reducing the circulating count. Drug-induced thrombocytopenia "
                "(quinidine, valproic acid, sulfonamides, certain antibiotics, and chemotherapy agents) is "
                "also a frequently encountered cause that should not be overlooked.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="MPV (Mean Platelet Volume) and its connection to PLT",
            body_html=(
                "<p><strong>MPV (Mean Platelet Volume)</strong> measures the average size of platelets in "
                "femtolitres (fL). The normal range is typically 7.5–12.0 fL. MPV provides insight into "
                "the rate of platelet production and the state of the bone marrow.</p>"
                "<p><strong>High MPV + low PLT:</strong> This pattern suggests that the bone marrow is "
                "compensating for peripheral platelet loss by releasing younger, larger platelets. It is "
                "characteristically seen in <strong>immune thrombocytopenic purpura (ITP)</strong> and other "
                "consumptive causes. Young platelets contain more granules and are hemostatically more active "
                "than older, smaller ones.</p>"
                "<p><strong>Low MPV + low PLT:</strong> This combination may indicate that the bone marrow "
                "itself is failing to produce adequate platelets — as seen in aplastic anemia, post-chemotherapy "
                "suppression, and myelodysplastic syndromes. When the marrow cannot mount a compensatory "
                "response, both count and size remain depressed.</p>"
                "<p>Elevated MPV has also been linked to increased cardiovascular risk. Larger platelets "
                "are more prone to aggregation and have been identified as an independent risk factor for "
                "myocardial infarction, stroke, and venous thromboembolism. For more details on MPV, see "
                'our <a href="/blog/mpv-blood-test">MPV article</a>.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptoms of high and low platelet counts",
            body_html=(
                "<p><strong>Thrombocytopenia (low PLT) symptoms:</strong></p>"
                "<ul>"
                "<li><strong>Petechiae</strong> — Pinpoint, flat red-purple spots on the skin that do not blanch with pressure.</li>"
                "<li><strong>Purpura</strong> — Larger areas of subcutaneous bleeding, appearing as purple patches.</li>"
                "<li><strong>Easy bruising (ecchymosis)</strong> — Bruises that appear from minor or no trauma.</li>"
                "<li><strong>Gum bleeding</strong> — Excessive bleeding during brushing or flossing.</li>"
                "<li><strong>Nosebleeds (epistaxis)</strong> — Frequent and hard-to-stop nasal bleeding.</li>"
                "<li><strong>Heavy menstrual bleeding (menorrhagia)</strong> — Abnormally prolonged or heavy periods.</li>"
                "<li><strong>GI or urinary bleeding</strong> — In severe thrombocytopenia, melena, hematuria, or hematemesis may occur.</li>"
                "</ul>"
                "<p><strong>Thrombocytosis (high PLT) symptoms:</strong> Reactive thrombocytosis is usually "
                "asymptomatic; the symptoms of the underlying condition dominate. However, in primary "
                "thrombocytosis (e.g., essential thrombocythemia), the following may occur:</p>"
                "<ul>"
                "<li><strong>Erythromelalgia</strong> — Burning pain, warmth, and redness in the hands and feet.</li>"
                "<li><strong>Headache and visual disturbances</strong> — Due to microvascular occlusion.</li>"
                "<li><strong>Thrombosis</strong> — Deep vein thrombosis (DVT), pulmonary embolism, stroke, or myocardial infarction.</li>"
                "<li><strong>Paradoxical bleeding</strong> — At very high counts (>1,000,000/μL), acquired von Willebrand disease can develop, causing bleeding rather than clotting.</li>"
                "</ul>"
                "<p>Spontaneous bleeding risk increases significantly when the platelet count drops below "
                "50,000/μL. Below 10,000–20,000/μL, life-threatening internal hemorrhage — including "
                "intracranial bleeding — becomes a serious concern requiring urgent medical attention.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="When to see a doctor",
            body_html=(
                "<p>Consult a healthcare professional promptly if any of the following apply:</p>"
                "<ul>"
                "<li>Your platelet count is <strong>below 150,000/μL or above 400,000/μL</strong>.</li>"
                "<li>You notice unexplained petechiae, purpura, or bruises on your skin.</li>"
                "<li>You experience frequent or prolonged nosebleeds or gum bleeding.</li>"
                "<li>Post-surgical or post-dental bleeding takes an unusually long time to stop.</li>"
                "<li>You have unexplained burning, pain, or redness in your hands or feet (erythromelalgia).</li>"
                "<li>Your platelet count shows a significant upward or downward trend compared to previous tests.</li>"
                "</ul>"
                "<p>Your doctor may order additional investigations, including a peripheral blood smear, bone "
                "marrow biopsy, immature platelet fraction (IPF), thrombopoietin levels, or genetic testing "
                "(JAK2, CALR, MPL mutations) to determine the underlying cause. Early diagnosis is particularly "
                "important in hematologic malignancies, where timely treatment can significantly improve outcomes.</p>"
                "<p>If your platelet count is critically low (<20,000/μL) and you have signs of active "
                "bleeding, this is a <strong>medical emergency</strong> — seek immediate care at the nearest "
                "emergency department.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="How Norya helps you understand your results",
            body_html=(
                "<p>By <a href=\"/analyze\">uploading your blood test to Norya</a>, you can receive a "
                "structured, easy-to-understand health summary of your PLT, MPV, and other hematologic "
                "parameters within minutes. Norya compares your values against reference ranges, highlights "
                "potential deviations, and presents your results in a holistic perspective.</p>"
                "<p>This summary is an ideal tool for preparing for your doctor's appointment: you can "
                "clearly see which values need attention, how related parameters connect, and what your "
                "overall picture looks like. <strong>Norya does not diagnose</strong> — but it empowers "
                "you to understand your results and have a more productive conversation with your physician.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>This guide is for informational purposes only and does not replace medical '
                'advice or diagnosis.</strong> Always discuss your results with a healthcare professional. '
                '<a href="/analyze">Start analysis with Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# SPANISH
# ─────────────────────────────────────────────────────────────────────
def _sections_es() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Análisis de PLT (plaquetas): ¿Qué significan tus resultados?",
            body_html=(
                "<p>El valor de <strong>PLT (plaquetas)</strong> en tu hemograma completo (CBC) indica "
                "el número de plaquetas en tu sangre. Las plaquetas, también llamadas trombocitos, son "
                "pequeños fragmentos celulares producidos en la médula ósea que desempeñan un papel "
                "fundamental en la coagulación sanguínea y la reparación de los vasos dañados.</p>"
                "<p>Un recuento de plaquetas por encima de lo normal (trombocitosis) o por debajo "
                "(trombocitopenia) puede indicar diversas condiciones médicas, desde infecciones e "
                "inflamaciones hasta enfermedades autoinmunes y trastornos de la médula ósea. Interpretar "
                "correctamente este valor es clave para detectar posibles problemas de salud a tiempo.</p>"
                "<p>Esta guía completa explica qué son las plaquetas, cómo funcionan, los valores normales, "
                "las causas de recuentos anormales, la relación entre PLT y VPM (MPV), los síntomas de alerta "
                "y cuándo consultar al médico. <em>Este artículo es educativo y no sustituye el consejo médico "
                "profesional.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="¿Qué son las plaquetas (trombocitos)?",
            body_html=(
                "<p>Las <strong>plaquetas (trombocitos)</strong> son fragmentos celulares pequeños y sin "
                "núcleo que circulan en el torrente sanguíneo. Se producen en la médula ósea a partir de "
                "células gigantes precursoras llamadas <strong>megacariocitos</strong>. Un solo megacariocito "
                "puede generar miles de plaquetas. Cada plaqueta mide apenas 2–3 micrómetros de diámetro, "
                "mucho menos que los glóbulos rojos o blancos, pero su papel en el mantenimiento de la "
                "integridad vascular es enorme.</p>"
                "<p>Las plaquetas tienen una vida media de aproximadamente 7–10 días. Tras envejecer, son "
                "eliminadas principalmente por el bazo, que también actúa como reservorio de alrededor de "
                "un tercio del total de plaquetas. Por ello, las condiciones que agrandan el bazo "
                "(esplenomegalia) pueden secuestrar plaquetas y reducir el recuento circulante.</p>"
                "<p>Además de la hemostasia, las plaquetas contribuyen a la inmunidad innata liberando "
                "péptidos antimicrobianos e interactuando con los leucocitos. También secretan factores de "
                "crecimiento (PDGF, TGF-β) que promueven la cicatrización, la reparación tisular y la "
                "angiogénesis, propiedades aprovechadas en la terapia con plasma rico en plaquetas (PRP).</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="Papel de las plaquetas en la coagulación",
            body_html=(
                "<p>Cuando un vaso sanguíneo se daña, el colágeno subyacente queda expuesto y las plaquetas "
                "se <strong>adhieren</strong> rápidamente a la superficie lesionada. Este primer contacto "
                "está mediado por el <strong>factor de von Willebrand (FvW)</strong>, que actúa como pegamento "
                "molecular entre los receptores plaquetarios (GP Ib/IX/V) y el colágeno. Las plaquetas "
                "adheridas se activan, cambiando de disco liso a esfera espinosa con pseudópodos.</p>"
                "<p>Las plaquetas activadas liberan el contenido de sus gránulos densos — ADP, tromboxano A2 "
                "y serotonina — que reclutan más plaquetas al sitio de la lesión. Los receptores GP IIb/IIIa "
                "cambian su conformación para unir fibrinógeno, interconectando plaquetas adyacentes. Este "
                "proceso de <strong>agregación</strong> forma el <em>tapón hemostático primario</em>, capaz "
                "de detener el sangrado de vasos pequeños en minutos.</p>"
                "<p>Posteriormente, la cascada de coagulación refuerza este tapón. La trombina convierte el "
                "fibrinógeno soluble en fibrina insoluble, formando una malla que estabiliza el tapón. "
                "Cualquier defecto en el número o la función plaquetaria puede desequilibrar el sistema, "
                "causando sangrado excesivo o trombosis patológica.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valores normales de plaquetas (PLT)",
            body_html=(
                "<p>El recuento de plaquetas se mide en el hemograma completo y se expresa en miles por "
                "microlitro (×10³/μL):</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>Parámetro</th><th {_TH}>Rango normal</th>'
                f'<th {_TH}>Nota</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (Adultos)</td><td {_TD}>150.000–400.000/μL</td>'
                f'<td {_TD}>Igual para ambos sexos</td></tr>'
                f'<tr><td {_TD}>PLT (Neonatos)</td><td {_TD}>150.000–450.000/μL</td>'
                f'<td {_TD}>Rango ligeramente más amplio</td></tr>'
                f'<tr><td {_TD}>VPM (Volumen Plaquetario Medio)</td><td {_TD}>7,5–12,0 fL</td>'
                f'<td {_TD}>Indica el tamaño plaquetario</td></tr>'
                '</tbody></table>'
                "<p>El recuento plaquetario puede fluctuar fisiológicamente durante el día. Tras ejercicio "
                "intenso o estrés se observan aumentos transitorios. Durante la menstruación puede haber "
                "un ligero descenso. La <strong>pseudotrombocitopenia</strong> — un recuento falsamente bajo "
                "por agregación plaquetaria inducida por EDTA — debe descartarse repitiendo la muestra en "
                "tubo de citrato.</p>"
                "<p>Los intervalos de referencia pueden variar ligeramente entre laboratorios; compare siempre "
                "su resultado con el rango de referencia impreso en su informe.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="Causas de plaquetas altas (trombocitosis)",
            body_html=(
                "<p>La <strong>trombocitosis</strong> se define como un recuento plaquetario superior a "
                "400.000/μL y se clasifica en dos categorías:</p>"
                "<p><strong>1. Trombocitosis reactiva (secundaria):</strong> Representa la gran mayoría de "
                "los casos y ocurre como respuesta a una condición subyacente:</p>"
                "<ul>"
                "<li><strong>Infecciones</strong> — Las citocinas como IL-6 estimulan la megacariocitopoyesis.</li>"
                "<li><strong>Enfermedades inflamatorias crónicas</strong> — Artritis reumatoide, EII, vasculitis.</li>"
                "<li><strong>Anemia ferropénica</strong> — La deficiencia de hierro estimula la trombopoyesis.</li>"
                "<li><strong>Cirugía y trauma</strong> — Elevación transitoria por respuesta de fase aguda.</li>"
                "<li><strong>Esplenectomía</strong> — Tras la extirpación del bazo, las plaquetas secuestradas "
                "se liberan al torrente, causando elevación persistente.</li>"
                "<li><strong>Neoplasias</strong> — Trombocitosis paraneoplásica en ciertos cánceres.</li>"
                "</ul>"
                "<p><strong>2. Trombocitosis primaria (clonal):</strong> Se origina por defectos a nivel de "
                "células madre en la médula ósea. Las neoplasias mieloproliferativas (trombocitemia esencial, "
                "policitemia vera, leucemia mieloide crónica) pertenecen a este grupo. Las mutaciones en "
                "<em>JAK2</em>, <em>CALR</em> o <em>MPL</em> son frecuentes y conllevan un riesgo elevado "
                "tanto de trombosis como de hemorragia.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="Causas de plaquetas bajas (trombocitopenia)",
            body_html=(
                "<p>La <strong>trombocitopenia</strong> se define como un recuento plaquetario inferior a "
                "150.000/μL y puede deberse a tres mecanismos:</p>"
                "<p><strong>1. Producción disminuida:</strong></p>"
                "<ul>"
                "<li><strong>Anemia aplásica</strong> — Insuficiencia medular que afecta todas las líneas celulares.</li>"
                "<li><strong>Leucemia, linfoma y cáncer metastásico</strong> — Infiltración maligna que desplaza "
                "la megacariocitopoyesis normal.</li>"
                "<li><strong>Síndrome mielodisplásico (SMD)</strong> — Hematopoyesis anormal con plaquetas "
                "disfuncionales.</li>"
                "<li><strong>Deficiencia de B12/folato</strong> — La anemia megaloblástica puede cursar con "
                "trombocitopenia.</li>"
                "<li><strong>Quimioterapia/radioterapia</strong> — Supresión medular transitoria.</li>"
                "</ul>"
                "<p><strong>2. Destrucción aumentada:</strong></p>"
                "<ul>"
                "<li><strong>Púrpura trombocitopénica inmune (PTI)</strong> — Anticuerpos autoinmunes destruyen "
                "plaquetas en el bazo.</li>"
                "<li><strong>Púrpura trombocitopénica trombótica (PTT)</strong> — Deficiencia de ADAMTS13 con "
                "anemia hemolítica microangiopática.</li>"
                "<li><strong>Trombocitopenia inducida por heparina (TIH)</strong> — Estado protrombótico "
                "paradójico mediado por anticuerpos.</li>"
                "<li><strong>Coagulación intravascular diseminada (CID)</strong> — Consumo masivo de plaquetas.</li>"
                "</ul>"
                "<p><strong>3. Secuestro esplénico:</strong> La esplenomegalia por cirrosis, hipertensión portal "
                "u otras causas atrapa un mayor porcentaje de plaquetas. La trombocitopenia inducida por "
                "fármacos (quinidina, ácido valproico, sulfonamidas, ciertos antibióticos) también es una "
                "causa frecuente.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="Relación entre VPM (MPV) y PLT",
            body_html=(
                "<p>El <strong>VPM (Volumen Plaquetario Medio)</strong> mide el tamaño promedio de las "
                "plaquetas en femtolitros (fL). El rango normal es típicamente 7,5–12,0 fL. El VPM aporta "
                "información sobre la tasa de producción plaquetaria y el estado de la médula ósea.</p>"
                "<p><strong>VPM alto + PLT bajo:</strong> Indica que la médula ósea compensa la pérdida "
                "periférica de plaquetas liberando plaquetas más jóvenes y grandes. Este patrón es típico "
                "de la PTI y otras causas de consumo. Las plaquetas jóvenes contienen más gránulos y son "
                "hemostáticamente más activas.</p>"
                "<p><strong>VPM bajo + PLT bajo:</strong> Sugiere que la médula ósea no puede producir "
                "plaquetas adecuadas, como en la anemia aplásica, tras quimioterapia o en síndromes "
                "mielodisplásicos.</p>"
                "<p>Un VPM elevado también se ha asociado con mayor riesgo cardiovascular. Las plaquetas "
                "más grandes son más propensas a la agregación y se han identificado como factor de riesgo "
                "independiente para infarto de miocardio, ictus y tromboembolismo venoso. Para más detalles, "
                'consulte nuestro <a href="/blog/mpv-blood-test">artículo sobre VPM</a>.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Síntomas de plaquetas altas y bajas",
            body_html=(
                "<p><strong>Síntomas de trombocitopenia (PLT bajo):</strong></p>"
                "<ul>"
                "<li><strong>Petequias</strong> — Puntos rojos-morados diminutos en la piel que no desaparecen con presión.</li>"
                "<li><strong>Púrpura</strong> — Áreas más amplias de hemorragia subcutánea.</li>"
                "<li><strong>Hematomas fáciles</strong> — Moretones desproporcionados por traumas menores.</li>"
                "<li><strong>Sangrado gingival</strong> — Sangrado excesivo al cepillarse.</li>"
                "<li><strong>Epistaxis</strong> — Sangrados nasales frecuentes y difíciles de detener.</li>"
                "<li><strong>Menorragia</strong> — Períodos menstruales anormalmente abundantes y prolongados.</li>"
                "<li><strong>Sangrado GI o urinario</strong> — En trombocitopenia grave, melena o hematuria.</li>"
                "</ul>"
                "<p><strong>Síntomas de trombocitosis (PLT alto):</strong> La trombocitosis reactiva suele "
                "ser asintomática. En la trombocitosis primaria pueden presentarse:</p>"
                "<ul>"
                "<li><strong>Eritromelalgia</strong> — Dolor ardiente, calor y enrojecimiento en manos y pies.</li>"
                "<li><strong>Cefalea y alteraciones visuales</strong> — Por oclusión microvascular.</li>"
                "<li><strong>Trombosis</strong> — TVP, embolia pulmonar, ictus o infarto de miocardio.</li>"
                "<li><strong>Sangrado paradójico</strong> — Con recuentos >1.000.000/μL puede desarrollarse "
                "enfermedad de von Willebrand adquirida.</li>"
                "</ul>"
                "<p>El riesgo de sangrado espontáneo aumenta por debajo de 50.000/μL. Por debajo de "
                "10.000–20.000/μL, la hemorragia interna potencialmente mortal requiere atención urgente.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="¿Cuándo consultar al médico?",
            body_html=(
                "<p>Consulte a un profesional de la salud si:</p>"
                "<ul>"
                "<li>Su recuento plaquetario es <strong>inferior a 150.000/μL o superior a 400.000/μL</strong>.</li>"
                "<li>Nota petequias, púrpura o hematomas inexplicables.</li>"
                "<li>Experimenta sangrados nasales o gingivales frecuentes o prolongados.</li>"
                "<li>El sangrado postquirúrgico o postdental tarda demasiado en detenerse.</li>"
                "<li>Tiene dolor ardiente, enrojecimiento o calor inexplicable en manos o pies.</li>"
                "<li>Su recuento plaquetario muestra una tendencia significativa al alza o a la baja.</li>"
                "</ul>"
                "<p>El médico puede solicitar estudios adicionales como frotis sanguíneo periférico, biopsia "
                "de médula ósea, fracción de plaquetas inmaduras, niveles de trombopoyetina o pruebas "
                "genéticas (mutaciones JAK2, CALR, MPL). El diagnóstico precoz en enfermedades hematológicas "
                "puede mejorar significativamente el pronóstico.</p>"
                "<p>Si el recuento es críticamente bajo (<20.000/μL) con signos de sangrado activo, se "
                "trata de una <strong>emergencia médica</strong> que requiere atención inmediata.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Cómo Norya te ayuda a entender tus resultados",
            body_html=(
                '<p>Al <a href="/analyze">subir tu análisis de sangre a Norya</a>, recibirás un resumen '
                "estructurado y fácil de entender de tu PLT, VPM y otros parámetros hematológicos en "
                "minutos. Norya compara tus valores con los rangos de referencia, destaca posibles "
                "desviaciones y presenta tus resultados desde una perspectiva integral.</p>"
                "<p>Este resumen es ideal para preparar tu cita médica: verás claramente qué valores "
                "requieren atención, cómo se relacionan entre sí y cuál es tu panorama general. "
                "<strong>Norya no diagnostica</strong>, pero te permite comprender tus resultados y "
                "tener una conversación más productiva con tu médico.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Aviso",
            body_html=(
                '<p><strong>Esta guía es solo informativa; no sustituye el consejo ni el diagnóstico '
                'médico.</strong> Consulte siempre sus resultados con un profesional sanitario. '
                '<a href="/analyze">Iniciar análisis con Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# GERMAN
# ─────────────────────────────────────────────────────────────────────
def _sections_de() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="PLT (Thrombozyten)-Test: Was bedeuten Ihre Ergebnisse?",
            body_html=(
                "<p>Der <strong>PLT (Thrombozytenwert)</strong> ist einer der wichtigsten Parameter im "
                "großen Blutbild (CBC). Thrombozyten — auch Blutplättchen genannt — sind winzige, "
                "scheibenförmige Zellfragmente, die im Knochenmark von Megakaryozyten gebildet werden. "
                "Ihre Hauptaufgabe ist es, Blutungen zu stoppen, indem sie an der Stelle einer "
                "Gefäßverletzung Gerinnsel bilden.</p>"
                "<p>Eine Thrombozytenzahl über dem Normalwert (Thrombozytose) oder darunter "
                "(Thrombozytopenie) kann auf verschiedenste Erkrankungen hinweisen — von Infektionen "
                "und Eisenmangel bis hin zu Autoimmunerkrankungen und Knochenmarkstörungen. Das Verständnis "
                "Ihres Thrombozytenwertes ist entscheidend für die frühzeitige Erkennung möglicher "
                "Gesundheitsprobleme.</p>"
                "<p>Dieser umfassende Leitfaden erklärt, was Thrombozyten sind, wie sie funktionieren, "
                "welche Normalwerte gelten, Ursachen abnormaler Werte, die Beziehung zwischen PLT und MPV, "
                "auf welche Symptome zu achten ist und wann ein Arzt aufgesucht werden sollte. <em>Dieser "
                "Artikel dient der Aufklärung und ersetzt keine professionelle medizinische Beratung.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="Was sind Thrombozyten (Blutplättchen)?",
            body_html=(
                "<p><strong>Thrombozyten (Blutplättchen)</strong> sind kleine, kernlose Zellfragmente im "
                "Blutkreislauf. Sie werden im Knochenmark von riesigen Vorläuferzellen, den "
                "<strong>Megakaryozyten</strong>, gebildet. Ein einzelner Megakaryozyt kann Tausende von "
                "Thrombozyten freisetzen. Mit einem Durchmesser von nur 2–3 Mikrometern sind sie viel "
                "kleiner als rote oder weiße Blutkörperchen, spielen aber eine überragende Rolle für die "
                "vaskuläre Integrität.</p>"
                "<p>Thrombozyten haben eine Lebensdauer von etwa 7–10 Tagen. Nach ihrer Alterung werden "
                "sie hauptsächlich von der Milz abgebaut, die gleichzeitig als Reservoir für etwa ein "
                "Drittel des gesamten Thrombozyten-Pools dient. Deshalb kann eine vergrößerte Milz "
                "(Splenomegalie) Thrombozyten sequestrieren und die Zahl im Blutkreislauf verringern.</p>"
                "<p>Neben der Hämostase tragen Thrombozyten zur angeborenen Immunität bei, indem sie "
                "antimikrobielle Peptide freisetzen und mit Leukozyten interagieren. Sie sezernieren "
                "Wachstumsfaktoren (PDGF, TGF-β), die Wundheilung, Gewebereparatur und Angiogenese "
                "fördern — Eigenschaften, die in der PRP-Therapie (plättchenreiches Plasma) genutzt werden.</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="Rolle der Thrombozyten bei der Blutgerinnung",
            body_html=(
                "<p>Wenn ein Blutgefäß verletzt wird, wird das darunterliegende Kollagen freigelegt. "
                "Thrombozyten <strong>adhärieren</strong> sofort an die verletzte Oberfläche. Dieser erste "
                "Kontakt wird durch den <strong>von-Willebrand-Faktor (vWF)</strong> vermittelt, ein "
                "Glykoprotein, das als molekularer Klebstoff zwischen Thrombozytenrezeptoren (GP Ib/IX/V) "
                "und Kollagen fungiert. Adhärierte Thrombozyten werden aktiviert: Sie wechseln von glatten "
                "Scheiben zu stachelförmigen Kugeln mit Pseudopodien.</p>"
                "<p>Aktivierte Thrombozyten setzen den Inhalt ihrer dichten Granula frei — ADP, "
                "Thromboxan A2 (TXA2) und Serotonin — die weitere Thrombozyten zum Ort der Verletzung "
                "rekrutieren. Gleichzeitig ermöglicht eine Konformationsänderung der GP-IIb/IIIa-Rezeptoren "
                "die Bindung von Fibrinogen, das benachbarte Thrombozyten verknüpft. Dieser Vorgang der "
                "<strong>Aggregation</strong> bildet den <em>primären hämostatischen Pfropf</em>.</p>"
                "<p>Anschließend verstärkt die Gerinnungskaskade diesen Pfropf. Thrombin wandelt lösliches "
                "Fibrinogen in unlösliche Fibrinfäden um, die das Thrombozyten-Netzwerk stabilisieren. "
                "Jede Störung der Thrombozytenzahl oder -funktion kann dieses empfindliche Gleichgewicht "
                "kippen und zu übermäßigen Blutungen oder pathologischer Thrombose führen.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Normale Thrombozytenwerte (PLT)",
            body_html=(
                "<p>Die Thrombozytenzahl wird im Rahmen des großen Blutbildes bestimmt und in "
                "Tausend pro Mikroliter (×10³/μL) angegeben:</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>Parameter</th><th {_TH}>Normalbereich</th>'
                f'<th {_TH}>Hinweis</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (Erwachsene)</td><td {_TD}>150.000–400.000/μL</td>'
                f'<td {_TD}>Gleich für beide Geschlechter</td></tr>'
                f'<tr><td {_TD}>PLT (Neugeborene)</td><td {_TD}>150.000–450.000/μL</td>'
                f'<td {_TD}>Etwas breiterer Bereich</td></tr>'
                f'<tr><td {_TD}>MPV (Mittleres Plättchenvolumen)</td><td {_TD}>7,5–12,0 fL</td>'
                f'<td {_TD}>Zeigt die Plättchengröße</td></tr>'
                '</tbody></table>'
                "<p>Die Thrombozytenzahl kann im Tagesverlauf physiologisch schwanken. Nach intensivem "
                "Sport oder Stress treten vorübergehende Anstiege auf. Während der Menstruation kann ein "
                "leichter Abfall beobachtet werden. Eine <strong>Pseudothrombozytopenie</strong> — ein "
                "falsch niedriger Wert durch EDTA-bedingte Thrombozytenverklumpung — sollte durch eine "
                "Wiederholung mit Zitrat-Röhrchen ausgeschlossen werden.</p>"
                "<p>Referenzbereiche können zwischen Laboren leicht variieren; vergleichen Sie Ihr "
                "Ergebnis stets mit dem auf Ihrem Laborbericht angegebenen Referenzbereich.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="Ursachen hoher Thrombozyten (Thrombozytose)",
            body_html=(
                "<p>Eine <strong>Thrombozytose</strong> liegt vor, wenn die Thrombozytenzahl 400.000/μL "
                "übersteigt. Sie wird in zwei Hauptkategorien unterteilt:</p>"
                "<p><strong>1. Reaktive (sekundäre) Thrombozytose:</strong> Macht die große Mehrheit der "
                "Fälle aus und tritt als Reaktion auf eine Grunderkrankung auf:</p>"
                "<ul>"
                "<li><strong>Infektionen</strong> — Akute Infektionen stimulieren die Megakaryopoese über "
                "Zytokine wie IL-6.</li>"
                "<li><strong>Chronisch-entzündliche Erkrankungen</strong> — Rheumatoide Arthritis, CED, "
                "Vaskulitis.</li>"
                "<li><strong>Eisenmangelanämie</strong> — Eisenmangel stimuliert die Thrombopoese.</li>"
                "<li><strong>Operation und Trauma</strong> — Vorübergehender Anstieg durch "
                "Akute-Phase-Reaktion.</li>"
                "<li><strong>Splenektomie</strong> — Nach Milzentfernung werden sequestrierte Thrombozyten "
                "freigesetzt.</li>"
                "<li><strong>Malignome</strong> — Paraneoplastische Thrombozytose bei bestimmten Krebsarten.</li>"
                "</ul>"
                "<p><strong>2. Primäre (klonale) Thrombozytose:</strong> Entsteht durch einen Stammzelldefekt "
                "im Knochenmark. Myeloproliferative Neoplasien (essenzielle Thrombozythämie, Polycythaemia "
                "vera, chronische myeloische Leukämie) gehören hierzu. Mutationen in <em>JAK2</em>, "
                "<em>CALR</em> oder <em>MPL</em> werden häufig nachgewiesen und erhöhen sowohl das "
                "Thrombose- als auch das Blutungsrisiko.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="Ursachen niedriger Thrombozyten (Thrombozytopenie)",
            body_html=(
                "<p>Eine <strong>Thrombozytopenie</strong> liegt vor, wenn die Thrombozytenzahl unter "
                "150.000/μL fällt. Drei Hauptmechanismen kommen in Betracht:</p>"
                "<p><strong>1. Verminderte Produktion:</strong></p>"
                "<ul>"
                "<li><strong>Aplastische Anämie</strong> — Knochenmarkversagen aller Zellreihen.</li>"
                "<li><strong>Leukämie, Lymphom, metastasierende Tumoren</strong> — Maligne Infiltration "
                "verdrängt die normale Megakaryopoese.</li>"
                "<li><strong>Myelodysplastisches Syndrom (MDS)</strong> — Abnorme Hämatopoese mit "
                "dysfunktionalen Thrombozyten.</li>"
                "<li><strong>Vitamin-B12-/Folsäuremangel</strong> — Megaloblastäre Anämie kann mit "
                "Thrombozytopenie einhergehen.</li>"
                "<li><strong>Chemotherapie/Bestrahlung</strong> — Vorübergehende Myelosuppression.</li>"
                "</ul>"
                "<p><strong>2. Erhöhter Verbrauch:</strong></p>"
                "<ul>"
                "<li><strong>Immunthrombozytopenie (ITP)</strong> — Autoantikörper beschleunigen den "
                "Thrombozytenabbau in der Milz.</li>"
                "<li><strong>Thrombotisch-thrombozytopenische Purpura (TTP)</strong> — ADAMTS13-Mangel mit "
                "mikroangiopathischer Hämolyse.</li>"
                "<li><strong>Heparin-induzierte Thrombozytopenie (HIT)</strong> — Antikörper-vermittelter "
                "paradoxer prothrombotischer Zustand.</li>"
                "<li><strong>Disseminierte intravasale Gerinnung (DIC)</strong> — Massiver "
                "Thrombozytenverbrauch.</li>"
                "</ul>"
                "<p><strong>3. Milzsequestration:</strong> Bei Splenomegalie durch Leberzirrhose, portale "
                "Hypertension oder infiltrative Erkrankungen werden mehr Thrombozyten in der Milz "
                "zurückgehalten. Medikamenteninduzierte Thrombozytopenie (Chinidin, Valproinsäure, "
                "Sulfonamide, bestimmte Antibiotika) ist ebenfalls häufig.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="MPV (Mittleres Plättchenvolumen) und sein Zusammenhang mit PLT",
            body_html=(
                "<p>Das <strong>MPV (Mittleres Plättchenvolumen)</strong> misst die durchschnittliche "
                "Größe der Thrombozyten in Femtolitern (fL). Der Normalbereich liegt bei 7,5–12,0 fL. "
                "Das MPV gibt Aufschluss über die Produktionsrate und den Zustand des Knochenmarks.</p>"
                "<p><strong>Hohes MPV + niedriges PLT:</strong> Dieses Muster deutet darauf hin, dass "
                "das Knochenmark den peripheren Verlust durch die Freisetzung jüngerer, größerer "
                "Thrombozyten kompensiert — typisch für ITP und andere konsumtive Ursachen. Junge "
                "Thrombozyten enthalten mehr Granula und sind hämostatisch aktiver.</p>"
                "<p><strong>Niedriges MPV + niedriges PLT:</strong> Kann darauf hindeuten, dass das "
                "Knochenmark selbst keine ausreichenden Thrombozyten produziert — wie bei aplastischer "
                "Anämie, nach Chemotherapie oder bei myelodysplastischen Syndromen.</p>"
                "<p>Ein erhöhtes MPV wurde auch mit einem erhöhten kardiovaskulären Risiko in Verbindung "
                "gebracht. Größere Thrombozyten neigen stärker zur Aggregation und gelten als unabhängiger "
                "Risikofaktor für Herzinfarkt, Schlaganfall und venöse Thromboembolien. Weitere Informationen "
                'finden Sie in unserem <a href="/blog/mpv-blood-test">MPV-Artikel</a>.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptome hoher und niedriger Thrombozytenwerte",
            body_html=(
                "<p><strong>Symptome der Thrombozytopenie (niedriges PLT):</strong></p>"
                "<ul>"
                "<li><strong>Petechien</strong> — Stecknadelkopfgroße rot-violette Punkte auf der Haut.</li>"
                "<li><strong>Purpura</strong> — Größere subkutane Blutungen.</li>"
                "<li><strong>Leichte Blutergüsse (Ekchymosen)</strong> — Blaue Flecken bei minimalem Trauma.</li>"
                "<li><strong>Zahnfleischbluten</strong> — Übermäßiges Bluten beim Zähneputzen.</li>"
                "<li><strong>Nasenbluten (Epistaxis)</strong> — Häufiges und schwer stillbares Nasenbluten.</li>"
                "<li><strong>Starke Menstruationsblutung (Menorrhagie)</strong> — Ungewöhnlich starke und lange Perioden.</li>"
                "<li><strong>GI- oder Harnwegsblutungen</strong> — Melena, Hämaturie bei schwerer Thrombozytopenie.</li>"
                "</ul>"
                "<p><strong>Symptome der Thrombozytose (hohes PLT):</strong> Reaktive Thrombozytose ist "
                "meist asymptomatisch. Bei primärer Thrombozytose können auftreten:</p>"
                "<ul>"
                "<li><strong>Erythromelalgie</strong> — Brennender Schmerz, Wärme und Rötung an Händen und Füßen.</li>"
                "<li><strong>Kopfschmerzen und Sehstörungen</strong> — Durch mikrovaskuläre Okklusion.</li>"
                "<li><strong>Thrombose</strong> — TVT, Lungenembolie, Schlaganfall oder Herzinfarkt.</li>"
                "<li><strong>Paradoxe Blutung</strong> — Bei sehr hohen Werten (>1.000.000/μL) kann ein "
                "erworbenes von-Willebrand-Syndrom entstehen.</li>"
                "</ul>"
                "<p>Das Risiko spontaner Blutungen steigt signifikant unter 50.000/μL. Unter "
                "10.000–20.000/μL drohen lebensbedrohliche innere Blutungen, die sofortige Behandlung erfordern.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Wann sollten Sie einen Arzt aufsuchen?",
            body_html=(
                "<p>Suchen Sie umgehend einen Arzt auf, wenn Folgendes zutrifft:</p>"
                "<ul>"
                "<li>Ihre Thrombozytenzahl liegt <strong>unter 150.000/μL oder über 400.000/μL</strong>.</li>"
                "<li>Sie bemerken unerklärliche Petechien, Purpura oder Blutergüsse.</li>"
                "<li>Häufiges oder anhaltendes Nasen- oder Zahnfleischbluten.</li>"
                "<li>Postoperative oder zahnärztliche Blutungen stoppen ungewöhnlich langsam.</li>"
                "<li>Unerklärliches Brennen, Schmerzen oder Rötung an Händen oder Füßen.</li>"
                "<li>Ihre Thrombozytenzahl zeigt einen signifikanten Auf- oder Abwärtstrend.</li>"
                "</ul>"
                "<p>Ihr Arzt kann weiterführende Untersuchungen anordnen: peripherer Blutausstrich, "
                "Knochenmarkbiopsie, unreife Plättchenfraktion (IPF), Thrombopoietin-Spiegel oder "
                "Gentests (JAK2, CALR, MPL). Eine frühzeitige Diagnose ist besonders bei hämatologischen "
                "Erkrankungen entscheidend.</p>"
                "<p>Bei kritisch niedrigen Werten (<20.000/μL) mit aktiven Blutungszeichen handelt es "
                "sich um einen <strong>medizinischen Notfall</strong> — suchen Sie sofort die nächste "
                "Notaufnahme auf.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Wie Norya Ihnen hilft, Ihre Ergebnisse zu verstehen",
            body_html=(
                '<p>Indem Sie <a href="/analyze">Ihr Blutbild bei Norya hochladen</a>, erhalten Sie '
                "innerhalb von Minuten eine strukturierte, leicht verständliche Zusammenfassung Ihrer "
                "PLT-, MPV- und anderer hämatologischer Werte. Norya vergleicht Ihre Werte mit "
                "Referenzbereichen, hebt mögliche Abweichungen hervor und präsentiert Ihre Ergebnisse "
                "in einer ganzheitlichen Perspektive.</p>"
                "<p>Diese Zusammenfassung ist ein ideales Werkzeug zur Vorbereitung auf Ihren Arzttermin: "
                "Sie sehen klar, welche Werte Aufmerksamkeit erfordern, wie verwandte Parameter "
                "zusammenhängen und wie Ihr Gesamtbild aussieht. <strong>Norya stellt keine Diagnosen</strong> "
                "— befähigt Sie aber, Ihre Ergebnisse zu verstehen und ein produktiveres Gespräch mit "
                "Ihrem Arzt zu führen.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Hinweis",
            body_html=(
                '<p><strong>Dieser Leitfaden dient nur zur Information und ersetzt keine ärztliche '
                'Beratung oder Diagnose.</strong> Besprechen Sie Ihre Ergebnisse immer mit einem Arzt. '
                '<a href="/analyze">Analyse mit Norya starten</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# FRENCH
# ─────────────────────────────────────────────────────────────────────
def _sections_fr() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Analyse PLT (plaquettes) : Que signifient vos résultats ?",
            body_html=(
                "<p>La valeur <strong>PLT (plaquettes)</strong> de votre numération formule sanguine (NFS) "
                "indique le nombre de plaquettes dans votre sang. Les plaquettes, également appelées "
                "thrombocytes, sont de minuscules fragments cellulaires produits dans la moelle osseuse "
                "qui jouent un rôle essentiel dans la coagulation sanguine et la réparation des vaisseaux "
                "endommagés.</p>"
                "<p>Un nombre de plaquettes supérieur à la normale (thrombocytose) ou inférieur "
                "(thrombocytopénie) peut signaler diverses pathologies — des infections et carences en fer "
                "aux maladies auto-immunes et troubles de la moelle osseuse. Comprendre correctement ce "
                "paramètre est essentiel pour détecter les problèmes de santé à un stade précoce.</p>"
                "<p>Ce guide complet explique ce que sont les plaquettes, comment elles fonctionnent, les "
                "valeurs normales, les causes d'anomalies, la relation entre PLT et VPM (MPV), les "
                "symptômes à surveiller et quand consulter. <em>Cet article est éducatif et ne remplace "
                "pas un avis médical professionnel.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="Que sont les plaquettes (thrombocytes) ?",
            body_html=(
                "<p>Les <strong>plaquettes (thrombocytes)</strong> sont de petits fragments cellulaires "
                "anucléés circulant dans le sang. Elles sont produites dans la moelle osseuse par de "
                "grandes cellules précurseurs appelées <strong>mégacaryocytes</strong>. Un seul mégacaryocyte "
                "peut libérer des milliers de plaquettes. Chaque plaquette ne mesure que 2–3 micromètres "
                "de diamètre — bien moins que les globules rouges ou blancs — mais leur rôle dans le "
                "maintien de l'intégrité vasculaire est considérable.</p>"
                "<p>Les plaquettes ont une durée de vie d'environ 7–10 jours. Après vieillissement, elles "
                "sont éliminées principalement par la rate, qui sert également de réservoir pour environ un "
                "tiers du pool plaquettaire total. C'est pourquoi les pathologies qui augmentent le volume "
                "de la rate (splénomégalie) peuvent séquestrer les plaquettes et réduire le nombre circulant.</p>"
                "<p>Au-delà de l'hémostase, les plaquettes contribuent à l'immunité innée en libérant des "
                "peptides antimicrobiens et en interagissant avec les leucocytes. Elles sécrètent des "
                "facteurs de croissance (PDGF, TGF-β) favorisant la cicatrisation, la réparation tissulaire "
                "et l'angiogenèse — propriétés exploitées dans la thérapie PRP (plasma riche en plaquettes).</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="Rôle des plaquettes dans la coagulation",
            body_html=(
                "<p>Lorsqu'un vaisseau sanguin est endommagé, le collagène sous-endothélial est exposé et "
                "les plaquettes <strong>adhèrent</strong> immédiatement à la surface lésée. Ce premier "
                "contact est médié par le <strong>facteur de von Willebrand (FvW)</strong>, une glycoprotéine "
                "agissant comme colle moléculaire entre les récepteurs plaquettaires (GP Ib/IX/V) et le "
                "collagène. Les plaquettes adhérées s'activent, passant d'un disque lisse à une sphère "
                "hérissée de pseudopodes.</p>"
                "<p>Les plaquettes activées libèrent le contenu de leurs granules denses — ADP, thromboxane "
                "A2 et sérotonine — qui recrutent davantage de plaquettes. Les récepteurs GP IIb/IIIa "
                "changent de conformation pour lier le fibrinogène, reliant les plaquettes adjacentes. Ce "
                "processus d'<strong>agrégation</strong> forme le <em>clou plaquettaire primaire</em>, "
                "capable d'arrêter le saignement des petits vaisseaux en quelques minutes.</p>"
                "<p>La cascade de coagulation renforce ensuite ce clou. La thrombine convertit le fibrinogène "
                "soluble en fibrine insoluble, formant un réseau qui stabilise l'agrégat plaquettaire. "
                "Tout défaut du nombre ou de la fonction plaquettaire peut perturber cet équilibre, "
                "entraînant un saignement excessif ou une thrombose pathologique.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valeurs normales des plaquettes (PLT)",
            body_html=(
                "<p>Le nombre de plaquettes est mesuré dans la NFS et exprimé en milliers par microlitre "
                "(×10³/μL) :</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>Paramètre</th><th {_TH}>Plage normale</th>'
                f'<th {_TH}>Note</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (Adultes)</td><td {_TD}>150 000–400 000/μL</td>'
                f'<td {_TD}>Identique pour les deux sexes</td></tr>'
                f'<tr><td {_TD}>PLT (Nouveau-nés)</td><td {_TD}>150 000–450 000/μL</td>'
                f'<td {_TD}>Plage légèrement plus large</td></tr>'
                f'<tr><td {_TD}>VPM (Volume Plaquettaire Moyen)</td><td {_TD}>7,5–12,0 fL</td>'
                f'<td {_TD}>Indique la taille des plaquettes</td></tr>'
                '</tbody></table>'
                "<p>Le nombre de plaquettes peut fluctuer physiologiquement au cours de la journée. Des "
                "élévations transitoires surviennent après un exercice intense ou un stress. Une légère "
                "baisse peut être observée pendant les menstruations. La <strong>pseudothrombocytopénie</strong> "
                "— un résultat faussement bas dû à l'agrégation plaquettaire induite par l'EDTA — doit "
                "être exclue en répétant le prélèvement sur tube citraté.</p>"
                "<p>Les intervalles de référence peuvent varier légèrement entre les laboratoires ; "
                "comparez toujours votre résultat avec la plage indiquée sur votre rapport.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="Causes des plaquettes élevées (thrombocytose)",
            body_html=(
                "<p>La <strong>thrombocytose</strong> est définie par un nombre de plaquettes supérieur à "
                "400 000/μL et se classe en deux catégories :</p>"
                "<p><strong>1. Thrombocytose réactive (secondaire) :</strong> Représente la grande majorité "
                "des cas et survient en réponse à une pathologie sous-jacente :</p>"
                "<ul>"
                "<li><strong>Infections</strong> — Les cytokines comme l'IL-6 stimulent la mégacaryopoïèse.</li>"
                "<li><strong>Maladies inflammatoires chroniques</strong> — Polyarthrite rhumatoïde, MICI, vascularite.</li>"
                "<li><strong>Anémie ferriprive</strong> — La carence en fer stimule la thrombopoïèse.</li>"
                "<li><strong>Chirurgie et traumatisme</strong> — Élévation transitoire par réponse de phase aiguë.</li>"
                "<li><strong>Splénectomie</strong> — La libération des plaquettes séquestrées et la suppression "
                "du site de clairance causent une élévation persistante.</li>"
                "<li><strong>Cancers</strong> — Thrombocytose paranéoplasique dans certaines tumeurs.</li>"
                "</ul>"
                "<p><strong>2. Thrombocytose primaire (clonale) :</strong> Résulte d'un défaut au niveau "
                "des cellules souches de la moelle osseuse. Les néoplasies myéloprolifératives (thrombocytémie "
                "essentielle, polyglobulie de Vaquez, leucémie myéloïde chronique) en font partie. Les "
                "mutations <em>JAK2</em>, <em>CALR</em> ou <em>MPL</em> sont fréquentes et augmentent le "
                "risque thrombotique et hémorragique.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="Causes des plaquettes basses (thrombocytopénie)",
            body_html=(
                "<p>La <strong>thrombocytopénie</strong> est définie par un nombre de plaquettes inférieur "
                "à 150 000/μL. Trois mécanismes principaux sont en cause :</p>"
                "<p><strong>1. Diminution de la production :</strong></p>"
                "<ul>"
                "<li><strong>Anémie aplasique</strong> — Insuffisance médullaire touchant toutes les lignées.</li>"
                "<li><strong>Leucémie, lymphome, cancer métastatique</strong> — Infiltration maligne de la moelle.</li>"
                "<li><strong>Syndrome myélodysplasique (SMD)</strong> — Hématopoïèse anormale.</li>"
                "<li><strong>Carence en B12/folates</strong> — Anémie mégaloblastique avec thrombocytopénie.</li>"
                "<li><strong>Chimiothérapie/radiothérapie</strong> — Myélosuppression transitoire.</li>"
                "</ul>"
                "<p><strong>2. Destruction accrue :</strong></p>"
                "<ul>"
                "<li><strong>Purpura thrombocytopénique immunologique (PTI)</strong> — Auto-anticorps accélérant "
                "la destruction splénique des plaquettes.</li>"
                "<li><strong>Purpura thrombotique thrombocytopénique (PTT)</strong> — Déficit en ADAMTS13.</li>"
                "<li><strong>Thrombocytopénie induite par l'héparine (TIH)</strong> — État prothrombotique "
                "paradoxal médié par des anticorps.</li>"
                "<li><strong>CIVD (Coagulation intravasculaire disséminée)</strong> — Consommation massive.</li>"
                "</ul>"
                "<p><strong>3. Séquestration splénique :</strong> L'augmentation de volume de la rate "
                "(cirrhose, hypertension portale) piège davantage de plaquettes. La thrombocytopénie "
                "médicamenteuse (quinidine, acide valproïque, sulfamides, certains antibiotiques) est "
                "également fréquente.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="Relation entre VPM (MPV) et PLT",
            body_html=(
                "<p>Le <strong>VPM (Volume Plaquettaire Moyen)</strong> mesure la taille moyenne des "
                "plaquettes en femtolitres (fL). La plage normale est de 7,5–12,0 fL. Le VPM renseigne "
                "sur le taux de production plaquettaire et l'état de la moelle osseuse.</p>"
                "<p><strong>VPM élevé + PLT bas :</strong> La moelle compense la perte périphérique en "
                "libérant des plaquettes plus jeunes et plus grandes — schéma typique du PTI et des causes "
                "de consommation. Les jeunes plaquettes contiennent plus de granules et sont hémostatiquement "
                "plus actives.</p>"
                "<p><strong>VPM bas + PLT bas :</strong> Suggère que la moelle ne peut produire suffisamment "
                "de plaquettes — comme dans l'anémie aplasique, après chimiothérapie ou dans les SMD.</p>"
                "<p>Un VPM élevé a également été associé à un risque cardiovasculaire accru. Les plaquettes "
                "plus grandes sont plus sujettes à l'agrégation et constituent un facteur de risque "
                "indépendant d'infarctus, d'AVC et de thromboembolie veineuse. Pour plus de détails, "
                'consultez notre <a href="/blog/mpv-blood-test">article sur le VPM</a>.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Symptômes des plaquettes hautes et basses",
            body_html=(
                "<p><strong>Symptômes de thrombocytopénie (PLT bas) :</strong></p>"
                "<ul>"
                "<li><strong>Pétéchies</strong> — Petits points rouge-violets sur la peau ne s'effaçant pas à la pression.</li>"
                "<li><strong>Purpura</strong> — Zones plus larges d'hémorragie sous-cutanée.</li>"
                "<li><strong>Ecchymoses faciles</strong> — Bleus disproportionnés pour des traumatismes mineurs.</li>"
                "<li><strong>Saignement gingival</strong> — Saignement excessif au brossage.</li>"
                "<li><strong>Épistaxis</strong> — Saignements de nez fréquents et difficiles à arrêter.</li>"
                "<li><strong>Ménorragie</strong> — Règles anormalement abondantes et prolongées.</li>"
                "<li><strong>Saignement GI ou urinaire</strong> — Méléna, hématurie dans les cas sévères.</li>"
                "</ul>"
                "<p><strong>Symptômes de thrombocytose (PLT élevé) :</strong> La thrombocytose réactive est "
                "généralement asymptomatique. Dans la thrombocytose primaire :</p>"
                "<ul>"
                "<li><strong>Érythromélalgie</strong> — Douleur brûlante, chaleur et rougeur des mains et pieds.</li>"
                "<li><strong>Céphalées et troubles visuels</strong> — Par occlusion microvasculaire.</li>"
                "<li><strong>Thrombose</strong> — TVP, embolie pulmonaire, AVC ou infarctus du myocarde.</li>"
                "<li><strong>Saignement paradoxal</strong> — Avec des taux >1 000 000/μL, une maladie de "
                "von Willebrand acquise peut se développer.</li>"
                "</ul>"
                "<p>Le risque de saignement spontané augmente en dessous de 50 000/μL. En dessous de "
                "10 000–20 000/μL, une hémorragie interne mettant en jeu le pronostic vital nécessite "
                "une prise en charge urgente.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quand consulter un médecin ?",
            body_html=(
                "<p>Consultez un professionnel de santé si :</p>"
                "<ul>"
                "<li>Votre nombre de plaquettes est <strong>inférieur à 150 000/μL ou supérieur à 400 000/μL</strong>.</li>"
                "<li>Vous remarquez des pétéchies, purpura ou ecchymoses inexpliquées.</li>"
                "<li>Vous avez des saignements de nez ou gingivaux fréquents ou prolongés.</li>"
                "<li>Le saignement postopératoire ou dentaire met anormalement longtemps à s'arrêter.</li>"
                "<li>Brûlure, douleur ou rougeur inexpliquée aux mains ou aux pieds.</li>"
                "<li>Votre numération plaquettaire montre une tendance significative à la hausse ou à la baisse.</li>"
                "</ul>"
                "<p>Votre médecin peut prescrire des examens complémentaires : frottis sanguin, biopsie "
                "médullaire, fraction plaquettaire immature, thrombopoïétine ou tests génétiques (JAK2, "
                "CALR, MPL). Un diagnostic précoce est crucial dans les pathologies hématologiques.</p>"
                "<p>Si le taux est critique (<20 000/μL) avec des signes de saignement actif, il s'agit "
                "d'une <strong>urgence médicale</strong> nécessitant une prise en charge immédiate.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Comment Norya vous aide à comprendre vos résultats",
            body_html=(
                '<p>En <a href="/analyze">téléchargeant votre analyse sanguine sur Norya</a>, vous recevez '
                "en quelques minutes un résumé structuré et facile à comprendre de votre PLT, VPM et "
                "autres paramètres hématologiques. Norya compare vos valeurs aux plages de référence, "
                "met en évidence les écarts potentiels et présente vos résultats dans une perspective "
                "globale.</p>"
                "<p>Ce résumé est un outil idéal pour préparer votre rendez-vous médical : vous voyez "
                "clairement quels paramètres nécessitent attention, comment les valeurs sont liées entre "
                "elles et quel est votre bilan général. <strong>Norya ne pose pas de diagnostic</strong> "
                "— mais vous aide à comprendre vos résultats et à avoir une consultation plus productive.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Avertissement",
            body_html=(
                '<p><strong>Ce guide est fourni à titre informatif uniquement et ne remplace pas un avis '
                "ou un diagnostic médical.</strong> Discutez toujours de vos résultats avec un professionnel "
                "de santé. <a href=\"/analyze\">Commencer l'analyse avec Norya</a></p>"
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ITALIAN
# ─────────────────────────────────────────────────────────────────────
def _sections_it() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="Esame PLT (piastrine): Cosa significano i tuoi risultati?",
            body_html=(
                "<p>Il valore <strong>PLT (piastrine)</strong> nell'emocromo completo (CBC) indica il "
                "numero di piastrine nel sangue. Le piastrine, dette anche trombociti, sono piccoli "
                "frammenti cellulari prodotti nel midollo osseo che svolgono un ruolo fondamentale nella "
                "coagulazione del sangue e nella riparazione dei vasi danneggiati.</p>"
                "<p>Un conteggio piastrinico superiore alla norma (trombocitosi) o inferiore "
                "(trombocitopenia) può segnalare diverse condizioni mediche — dalle infezioni e carenze "
                "di ferro alle malattie autoimmuni e disturbi del midollo osseo. Interpretare correttamente "
                "questo valore è essenziale per identificare precocemente potenziali problemi di salute.</p>"
                "<p>Questa guida completa spiega cosa sono le piastrine, come funzionano, i valori normali, "
                "le cause di conteggi anomali, la relazione tra PLT e MPV, i sintomi da monitorare e "
                "quando consultare il medico. <em>Questo articolo è educativo e non sostituisce il parere "
                "medico professionale.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="Cosa sono le piastrine (trombociti)?",
            body_html=(
                "<p>Le <strong>piastrine (trombociti)</strong> sono piccoli frammenti cellulari privi di "
                "nucleo che circolano nel sangue. Vengono prodotte nel midollo osseo da grandi cellule "
                "precursori chiamate <strong>megacariociti</strong>. Un singolo megacariocita può generare "
                "migliaia di piastrine. Ogni piastrina misura appena 2–3 micrometri di diametro — molto "
                "meno dei globuli rossi o bianchi — ma il loro ruolo nel mantenimento dell'integrità "
                "vascolare è enorme.</p>"
                "<p>Le piastrine hanno una durata di vita di circa 7–10 giorni. Dopo l'invecchiamento, "
                "vengono eliminate principalmente dalla milza, che funge anche da serbatoio per circa un "
                "terzo del pool piastrinico totale. Per questo motivo, condizioni che ingrandiscono la "
                "milza (splenomegalia) possono sequestrare le piastrine e ridurre il conteggio circolante.</p>"
                "<p>Oltre all'emostasi, le piastrine contribuiscono all'immunità innata rilasciando peptidi "
                "antimicrobici e interagendo con i leucociti. Secernono fattori di crescita (PDGF, TGF-β) "
                "che promuovono la guarigione delle ferite, la riparazione tissutale e l'angiogenesi — "
                "proprietà sfruttate nella terapia PRP (plasma ricco di piastrine).</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="Ruolo delle piastrine nella coagulazione",
            body_html=(
                "<p>Quando un vaso sanguigno viene danneggiato, il collagene sottostante viene esposto e "
                "le piastrine <strong>aderiscono</strong> immediatamente alla superficie lesa. Questo primo "
                "contatto è mediato dal <strong>fattore di von Willebrand (vWF)</strong>, una glicoproteina "
                "che agisce da colla molecolare tra i recettori piastrinici (GP Ib/IX/V) e il collagene. "
                "Le piastrine adese si attivano, passando da dischi lisci a sfere spinose con pseudopodi.</p>"
                "<p>Le piastrine attivate rilasciano il contenuto dei loro granuli densi — ADP, trombossano "
                "A2 e serotonina — che reclutano altre piastrine nel sito della lesione. I recettori "
                "GP IIb/IIIa cambiano conformazione per legare il fibrinogeno, collegando le piastrine "
                "adiacenti. Questo processo di <strong>aggregazione</strong> forma il <em>tappo emostatico "
                "primario</em>, capace di arrestare il sanguinamento dei piccoli vasi in pochi minuti.</p>"
                "<p>La cascata coagulativa rinforza poi questo tappo. La trombina converte il fibrinogeno "
                "solubile in fibrina insolubile, formando una rete che stabilizza l'aggregato piastrinico. "
                "Qualsiasi difetto nel numero o nella funzione piastrinica può alterare questo equilibrio, "
                "causando sanguinamento eccessivo o trombosi patologica.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="Valori normali delle piastrine (PLT)",
            body_html=(
                "<p>Il conteggio piastrinico viene misurato nell'emocromo e riportato in migliaia per "
                "microlitro (×10³/μL):</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>Parametro</th><th {_TH}>Intervallo normale</th>'
                f'<th {_TH}>Nota</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (Adulti)</td><td {_TD}>150.000–400.000/μL</td>'
                f'<td {_TD}>Uguale per entrambi i sessi</td></tr>'
                f'<tr><td {_TD}>PLT (Neonati)</td><td {_TD}>150.000–450.000/μL</td>'
                f'<td {_TD}>Intervallo leggermente più ampio</td></tr>'
                f'<tr><td {_TD}>MPV (Volume Piastrinico Medio)</td><td {_TD}>7,5–12,0 fL</td>'
                f'<td {_TD}>Indica la dimensione piastrinica</td></tr>'
                '</tbody></table>'
                "<p>Il conteggio piastrinico può fluttuare fisiologicamente durante la giornata. Dopo "
                "esercizio intenso si osservano aumenti transitori. Durante le mestruazioni può verificarsi "
                "una leggera diminuzione. La <strong>pseudotrombocitopenia</strong> — un risultato falsamente "
                "basso per aggregazione piastrinica indotta da EDTA — va esclusa ripetendo il prelievo in "
                "provetta citratata.</p>"
                "<p>Gli intervalli di riferimento possono variare lievemente tra i laboratori; confronti "
                "sempre il suo risultato con l'intervallo indicato sul referto.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="Cause di piastrine alte (trombocitosi)",
            body_html=(
                "<p>La <strong>trombocitosi</strong> è definita da un conteggio piastrinico superiore a "
                "400.000/μL e si classifica in due categorie:</p>"
                "<p><strong>1. Trombocitosi reattiva (secondaria):</strong> Rappresenta la grande maggioranza "
                "dei casi e si verifica come risposta a una condizione sottostante:</p>"
                "<ul>"
                "<li><strong>Infezioni</strong> — Le citochine come l'IL-6 stimolano la megacariocitopoiesi.</li>"
                "<li><strong>Malattie infiammatorie croniche</strong> — Artrite reumatoide, IBD, vasculite.</li>"
                "<li><strong>Anemia sideropenica</strong> — La carenza di ferro stimola la trombopoiesi.</li>"
                "<li><strong>Chirurgia e trauma</strong> — Aumento transitorio per risposta di fase acuta.</li>"
                "<li><strong>Splenectomia</strong> — Dopo la rimozione della milza, le piastrine sequestrate "
                "vengono rilasciate nel circolo.</li>"
                "<li><strong>Neoplasie</strong> — Trombocitosi paraneoplastica in alcuni tumori.</li>"
                "</ul>"
                "<p><strong>2. Trombocitosi primaria (clonale):</strong> Origina da un difetto a livello "
                "delle cellule staminali del midollo osseo. Le neoplasie mieloproliferative (trombocitemia "
                "essenziale, policitemia vera, leucemia mieloide cronica) appartengono a questo gruppo. "
                "Mutazioni di <em>JAK2</em>, <em>CALR</em> o <em>MPL</em> sono frequenti e aumentano "
                "il rischio trombotico ed emorragico.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="Cause di piastrine basse (trombocitopenia)",
            body_html=(
                "<p>La <strong>trombocitopenia</strong> è definita da un conteggio piastrinico inferiore "
                "a 150.000/μL. Tre meccanismi principali sono responsabili:</p>"
                "<p><strong>1. Ridotta produzione:</strong></p>"
                "<ul>"
                "<li><strong>Anemia aplastica</strong> — Insufficienza midollare di tutte le linee cellulari.</li>"
                "<li><strong>Leucemia, linfoma, cancro metastatico</strong> — Infiltrazione maligna del midollo.</li>"
                "<li><strong>Sindrome mielodisplastica (SMD)</strong> — Ematopoiesi anomala.</li>"
                "<li><strong>Carenza di B12/folati</strong> — Anemia megaloblastica con trombocitopenia.</li>"
                "<li><strong>Chemioterapia/radioterapia</strong> — Mielosoppressione transitoria.</li>"
                "</ul>"
                "<p><strong>2. Distruzione aumentata:</strong></p>"
                "<ul>"
                "<li><strong>Porpora trombocitopenica immune (ITP)</strong> — Autoanticorpi che accelerano "
                "la distruzione splenica delle piastrine.</li>"
                "<li><strong>Porpora trombotica trombocitopenica (TTP)</strong> — Deficit di ADAMTS13.</li>"
                "<li><strong>Trombocitopenia da eparina (HIT)</strong> — Stato protrombotico paradossale "
                "mediato da anticorpi.</li>"
                "<li><strong>CID (Coagulazione intravascolare disseminata)</strong> — Consumo massiccio.</li>"
                "</ul>"
                "<p><strong>3. Sequestro splenico:</strong> La splenomegalia da cirrosi, ipertensione portale "
                "o malattie infiltrative intrappola più piastrine. La trombocitopenia da farmaci (chinidina, "
                "acido valproico, sulfonamidi, alcuni antibiotici) è anch'essa frequente.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="Relazione tra MPV e PLT",
            body_html=(
                "<p>L'<strong>MPV (Volume Piastrinico Medio)</strong> misura la dimensione media delle "
                "piastrine in femtolitri (fL). L'intervallo normale è 7,5–12,0 fL. L'MPV fornisce "
                "informazioni sulla velocità di produzione piastrinica e sullo stato del midollo osseo.</p>"
                "<p><strong>MPV alto + PLT basso:</strong> Indica che il midollo compensa la perdita "
                "periferica rilasciando piastrine più giovani e più grandi — tipico della ITP e altre "
                "cause di consumo. Le piastrine giovani contengono più granuli e sono emostaticamente "
                "più attive.</p>"
                "<p><strong>MPV basso + PLT basso:</strong> Suggerisce che il midollo non riesce a produrre "
                "piastrine adeguate — come nell'anemia aplastica, dopo chemioterapia o nelle sindromi "
                "mielodisplastiche.</p>"
                "<p>Un MPV elevato è stato anche associato a un maggiore rischio cardiovascolare. Le "
                "piastrine più grandi sono più inclini all'aggregazione e sono un fattore di rischio "
                "indipendente per infarto, ictus e tromboembolismo venoso. Per maggiori dettagli, consulti "
                'il nostro <a href="/blog/mpv-blood-test">articolo sull\'MPV</a>.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="Sintomi di piastrine alte e basse",
            body_html=(
                "<p><strong>Sintomi della trombocitopenia (PLT basso):</strong></p>"
                "<ul>"
                "<li><strong>Petecchie</strong> — Piccoli punti rosso-violacei sulla pelle che non scompaiono alla pressione.</li>"
                "<li><strong>Porpora</strong> — Aree più ampie di emorragia sottocutanea.</li>"
                "<li><strong>Ecchimosi facili</strong> — Lividi sproporzionati per traumi minimi.</li>"
                "<li><strong>Sanguinamento gengivale</strong> — Sanguinamento eccessivo durante lo spazzolamento.</li>"
                "<li><strong>Epistassi</strong> — Sangue dal naso frequente e difficile da arrestare.</li>"
                "<li><strong>Menorragia</strong> — Mestruazioni anormalmente abbondanti e prolungate.</li>"
                "<li><strong>Sanguinamento GI o urinario</strong> — Melena, ematuria nei casi gravi.</li>"
                "</ul>"
                "<p><strong>Sintomi della trombocitosi (PLT alto):</strong> La trombocitosi reattiva è "
                "generalmente asintomatica. Nella trombocitosi primaria possono presentarsi:</p>"
                "<ul>"
                "<li><strong>Eritromelalgia</strong> — Dolore urente, calore e rossore a mani e piedi.</li>"
                "<li><strong>Cefalea e disturbi visivi</strong> — Per occlusione microvascolare.</li>"
                "<li><strong>Trombosi</strong> — TVP, embolia polmonare, ictus o infarto del miocardio.</li>"
                "<li><strong>Sanguinamento paradossale</strong> — Con conteggi >1.000.000/μL può svilupparsi "
                "malattia di von Willebrand acquisita.</li>"
                "</ul>"
                "<p>Il rischio di sanguinamento spontaneo aumenta sotto 50.000/μL. Sotto 10.000–20.000/μL, "
                "l'emorragia interna potenzialmente fatale richiede cure urgenti.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="Quando consultare il medico?",
            body_html=(
                "<p>Consulti un professionista sanitario se:</p>"
                "<ul>"
                "<li>Il conteggio piastrinico è <strong>inferiore a 150.000/μL o superiore a 400.000/μL</strong>.</li>"
                "<li>Nota petecchie, porpora o lividi inspiegabili.</li>"
                "<li>Sanguinamenti nasali o gengivali frequenti o prolungati.</li>"
                "<li>Il sanguinamento post-chirurgico o post-dentale impiega troppo tempo ad arrestarsi.</li>"
                "<li>Dolore urente, rossore o calore inspiegabile a mani o piedi.</li>"
                "<li>Il conteggio piastrinico mostra una tendenza significativa al rialzo o al ribasso.</li>"
                "</ul>"
                "<p>Il medico può richiedere ulteriori esami: striscio di sangue periferico, biopsia "
                "midollare, frazione piastrinica immatura, trombopoietina o test genetici (JAK2, CALR, "
                "MPL). La diagnosi precoce nelle malattie ematologiche è determinante per il successo "
                "terapeutico.</p>"
                "<p>Se il conteggio è criticamente basso (<20.000/μL) con segni di sanguinamento attivo, "
                "si tratta di un'<strong>emergenza medica</strong> che richiede cure immediate.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Come Norya ti aiuta a comprendere i tuoi risultati",
            body_html=(
                '<p>Caricando <a href="/analyze">le tue analisi del sangue su Norya</a>, riceverai in '
                "pochi minuti un riepilogo strutturato e facile da capire dei tuoi valori PLT, MPV e "
                "altri parametri ematologici. Norya confronta i tuoi valori con gli intervalli di "
                "riferimento, evidenzia possibili deviazioni e presenta i risultati in una prospettiva "
                "olistica.</p>"
                "<p>Questo riepilogo è uno strumento ideale per prepararti alla visita medica: vedrai "
                "chiaramente quali valori richiedono attenzione, come i parametri correlati si collegano "
                "e qual è il tuo quadro generale. <strong>Norya non formula diagnosi</strong> — ma ti "
                "permette di comprendere i tuoi risultati e avere un colloquio più produttivo col medico.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="Disclaimer",
            body_html=(
                '<p><strong>Questa guida è solo a scopo informativo e non sostituisce il parere o la '
                'diagnosi medica.</strong> Discutete sempre i risultati con un professionista sanitario. '
                '<a href="/analyze">Inizia l\'analisi con Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HEBREW
# ─────────────────────────────────────────────────────────────────────
def _sections_he() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="בדיקת PLT (טסיות דם): מה המשמעות של התוצאות שלך?",
            body_html=(
                "<p>ערך <strong>PLT (טסיות דם)</strong> בספירת הדם המלאה (CBC) מציין את מספר הטסיות "
                "בדם שלך. טסיות — הנקראות גם תרומבוציטים — הן שברי תאים זעירים המיוצרים במח העצם "
                "שמשחקים תפקיד מרכזי בקרישת הדם ובתיקון כלי דם פגועים.</p>"
                "<p>ספירת טסיות גבוהה מהנורמה (תרומבוציטוזיס) או נמוכה ממנה (תרומבוציטופניה) עלולה "
                "להעיד על מגוון מצבים רפואיים — מזיהומים וחסר ברזל ועד למחלות אוטואימוניות "
                "והפרעות במח העצם. הבנת ספירת הטסיות שלך היא חיונית לזיהוי מוקדם של בעיות "
                "בריאותיות פוטנציאליות.</p>"
                "<p>מדריך מקיף זה מסביר מהן טסיות, כיצד הן פועלות, מהם הערכים התקינים, הגורמים "
                "לספירה חריגה, הקשר בין PLT ל-MPV, תסמינים שיש לעקוב אחריהם ומתי לפנות לרופא. "
                "<em>מאמר זה הוא חינוכי בלבד ואינו מחליף ייעוץ רפואי מקצועי.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="מהן טסיות דם (תרומבוציטים)?",
            body_html=(
                "<p><strong>טסיות דם (תרומבוציטים)</strong> הן שברי תאים קטנים וחסרי גרעין המסתובבים "
                "בזרם הדם. הן מיוצרות במח העצם על ידי תאי ענק הנקראים <strong>מגקריוציטים</strong>. "
                "מגקריוציט בודד יכול לשחרר אלפי טסיות. כל טסית בקוטר של 2–3 מיקרומטרים בלבד — "
                "קטנה בהרבה מכדוריות דם אדומות או לבנות — אך תפקידה בשמירה על שלמות כלי הדם הוא "
                "קריטי.</p>"
                "<p>לטסיות אורך חיים של כ-7–10 ימים. לאחר הזדקנותן, הן מסולקות בעיקר על ידי הטחול, "
                "המשמש גם כמאגר המחזיק כשליש ממאגר הטסיות הכולל. לכן, מצבים המגדילים את הטחול "
                "(ספלנומגליה) יכולים לכלוא טסיות ולהפחית את הספירה במחזור הדם.</p>"
                "<p>מעבר להמוסטזיס, טסיות תורמות לחסינות המולדת על ידי שחרור פפטידים אנטי-מיקרוביאליים "
                "ואינטראקציה עם לויקוציטים. הן גם מפרישות גורמי גדילה (PDGF, TGF-β) המקדמים "
                "ריפוי פצעים, תיקון רקמות ואנגיוגנזה — תכונות המנוצלות בטיפול PRP (פלזמה עשירת "
                "טסיות).</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="תפקיד הטסיות בקרישת הדם",
            body_html=(
                "<p>כאשר כלי דם נפגע, הקולגן התת-אנדותליאלי נחשף והטסיות <strong>נצמדות</strong> "
                "מיד למשטח הפגוע. מגע ראשוני זה מתווך על ידי <strong>גורם פון ווילברנד (vWF)</strong>, "
                "גליקופרוטאין הפועל כדבק מולקולרי בין קולטני הטסיות (GP Ib/IX/V) לקולגן. טסיות "
                "שנצמדו מופעלות: הן משנות צורה מדיסקיות חלקות לכדורים קוצניים עם פסאודופודיות.</p>"
                "<p>טסיות מופעלות משחררות את תוכן הגרנולות הצפופות שלהן — ADP, תרומבוקסן A2 "
                "וסרוטונין — המגייסים טסיות נוספות לאזור. קולטני GP IIb/IIIa משנים את קונפורמציתם "
                "ומאפשרים קשירת פיברינוגן, המחבר טסיות סמוכות. תהליך <strong>האגרגציה</strong> יוצר "
                "את <em>הפקק ההמוסטטי הראשוני</em>, המסוגל לעצור דימום מכלי דם קטנים תוך דקות.</p>"
                "<p>מפל הקרישה מחזק את הפקק הראשוני. תרומבין ממיר פיברינוגן מסיס לפיברין בלתי "
                "מסיס, ויוצר רשת המייצבת את מצבור הטסיות. כל פגם במספר הטסיות או בתפקודן יכול "
                "להפר את האיזון העדין, ולהוביל לדימום מוגזם או לקרישה פתולוגית.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="ערכי טסיות (PLT) תקינים",
            body_html=(
                "<p>ספירת הטסיות נמדדת כחלק מספירת הדם המלאה ומדווחת באלפים למיקרוליטר:</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>פרמטר</th><th {_TH}>טווח תקין</th>'
                f'<th {_TH}>הערה</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (מבוגרים)</td><td {_TD}>150,000–400,000/μL</td>'
                f'<td {_TD}>זהה לשני המינים</td></tr>'
                f'<tr><td {_TD}>PLT (יילודים)</td><td {_TD}>150,000–450,000/μL</td>'
                f'<td {_TD}>טווח רחב מעט יותר</td></tr>'
                f'<tr><td {_TD}>MPV (נפח טסית ממוצע)</td><td {_TD}>7.5–12.0 fL</td>'
                f'<td {_TD}>מציין את גודל הטסיות</td></tr>'
                '</tbody></table>'
                "<p>ספירת הטסיות יכולה לנוע פיזיולוגית במהלך היום. עליות חולפות מתרחשות לאחר "
                "פעילות גופנית אינטנסיבית או מתח. ירידה קלה עשויה להיצפות בזמן מחזור. "
                "<strong>פסאודותרומבוציטופניה</strong> — ספירה נמוכה באופן שגוי עקב הצטברות טסיות "
                "בתגובה ל-EDTA — צריכה להישלל על ידי חזרה על הדגימה בצינורית ציטרט.</p>"
                "<p>טווחי ההתייחסות עשויים להשתנות מעט בין מעבדות; השוו תמיד את תוצאתכם לטווח "
                "ההתייחסות בדוח המעבדה שלכם.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="גורמים לטסיות גבוהות (תרומבוציטוזיס)",
            body_html=(
                "<p><strong>תרומבוציטוזיס</strong> מוגדר כספירת טסיות מעל 400,000/μL ומסווג לשתי "
                "קטגוריות:</p>"
                "<p><strong>1. תרומבוציטוזיס ריאקטיבי (משני):</strong> מהווה את הרוב המוחלט של "
                "המקרים ומתרחש כתגובה למצב בסיסי:</p>"
                "<ul>"
                "<li><strong>זיהומים</strong> — ציטוקינים כמו IL-6 מעוררים מגקריופויאזיס.</li>"
                "<li><strong>מחלות דלקתיות כרוניות</strong> — דלקת מפרקים שגרונית, IBD, וסקוליטיס.</li>"
                "<li><strong>אנמיה מחסר ברזל</strong> — חסר ברזל מעורר תרומבופויאזיס.</li>"
                "<li><strong>ניתוח וטראומה</strong> — עלייה חולפת בתגובת שלב אקוטי.</li>"
                "<li><strong>כריתת טחול</strong> — שחרור טסיות שהיו כלואות.</li>"
                "<li><strong>ממאירות</strong> — תרומבוציטוזיס פרנאופלסטי בסוגי סרטן מסוימים.</li>"
                "</ul>"
                "<p><strong>2. תרומבוציטוזיס ראשוני (קלונלי):</strong> נובע מפגם ברמת תאי הגזע "
                "במח העצם. ניאופלזמות מיאלופרוליפרטיביות (תרומבוציטמיה אסנציאלית, פוליציטמיה ורה, "
                "לוקמיה מיאלואידית כרונית) שייכות לקבוצה זו. מוטציות ב-<em>JAK2</em>, <em>CALR</em> "
                "או <em>MPL</em> מזוהות בתדירות גבוהה ומעלות את הסיכון הן לקרישיות והן לדימום.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="גורמים לטסיות נמוכות (תרומבוציטופניה)",
            body_html=(
                "<p><strong>תרומבוציטופניה</strong> מוגדרת כספירת טסיות מתחת ל-150,000/μL. שלושה "
                "מנגנונים עיקריים אחראיים:</p>"
                "<p><strong>1. ייצור מופחת:</strong></p>"
                "<ul>"
                "<li><strong>אנמיה אפלסטית</strong> — כשל מח עצם של כל שורות התאים.</li>"
                "<li><strong>לוקמיה, לימפומה, סרטן גרורתי</strong> — חדירה ממאירה של מח העצם.</li>"
                "<li><strong>תסמונת מיאלודיספלסטית (MDS)</strong> — המטופויאזיס חריג.</li>"
                "<li><strong>חסר B12/פולאט</strong> — אנמיה מגלובלסטית עם תרומבוציטופניה.</li>"
                "<li><strong>כימותרפיה/הקרנות</strong> — דיכוי מח עצם חולף.</li>"
                "</ul>"
                "<p><strong>2. הרס מוגבר:</strong></p>"
                "<ul>"
                "<li><strong>פורפורה תרומבוציטופנית אימונית (ITP)</strong> — נוגדנים עצמיים מאיצים "
                "את הרס הטסיות בטחול.</li>"
                "<li><strong>פורפורה תרומבוטית תרומבוציטופנית (TTP)</strong> — חסר ADAMTS13.</li>"
                "<li><strong>תרומבוציטופניה מושרית הפרין (HIT)</strong> — מצב פרו-תרומבוטי "
                "פרדוקסלי בתיווך נוגדנים.</li>"
                "<li><strong>קרישה תוך-כלית מפושטת (DIC)</strong> — צריכה מסיבית של טסיות.</li>"
                "</ul>"
                "<p><strong>3. ספיגה טחולית:</strong> כאשר הטחול מוגדל עקב שחמת, יתר לחץ דם פורטלי "
                "או מחלות חדירתיות, הוא לוכד יותר טסיות. תרומבוציטופניה מושרית תרופות (קינידין, "
                "חומצה ולפרואית, סולפונאמידים, אנטיביוטיקות מסוימות) היא גם סיבה שכיחה.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="MPV (נפח טסית ממוצע) והקשר ל-PLT",
            body_html=(
                "<p><strong>MPV (נפח טסית ממוצע)</strong> מודד את הגודל הממוצע של הטסיות "
                "בפמטוליטרים (fL). הטווח התקין הוא 7.5–12.0 fL. MPV מספק מידע על קצב ייצור "
                "הטסיות ועל מצב מח העצם.</p>"
                "<p><strong>MPV גבוה + PLT נמוך:</strong> דפוס זה מרמז שמח העצם מפצה על אובדן "
                "היקפי על ידי שחרור טסיות צעירות וגדולות יותר — אופייני ל-ITP ולסיבות צריכה אחרות. "
                "טסיות צעירות מכילות יותר גרנולות ופעילות המוסטטית גבוהה יותר.</p>"
                "<p><strong>MPV נמוך + PLT נמוך:</strong> עשוי להעיד על כך שמח העצם עצמו אינו "
                "מסוגל לייצר טסיות מספקות — כפי שנראה באנמיה אפלסטית, לאחר כימותרפיה או "
                "בתסמונות מיאלודיספלסטיות.</p>"
                "<p>MPV מוגבר נקשר גם לסיכון קרדיווסקולרי מוגבר. טסיות גדולות יותר נוטות יותר "
                "לאגרגציה וזוהו כגורם סיכון עצמאי לאוטם שריר הלב, שבץ ותרומבואמבוליזם ורידי. "
                'לפרטים נוספים, ראו <a href="/blog/mpv-blood-test">מאמר ה-MPV שלנו</a>.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="תסמינים של טסיות גבוהות ונמוכות",
            body_html=(
                "<p><strong>תסמיני תרומבוציטופניה (PLT נמוך):</strong></p>"
                "<ul>"
                "<li><strong>פטקיות</strong> — נקודות אדומות-סגולות זעירות על העור שאינן נעלמות בלחץ.</li>"
                "<li><strong>פורפורה</strong> — אזורים רחבים יותר של דימום תת-עורי.</li>"
                "<li><strong>חבורות קלות</strong> — שטפי דם לא פרופורציונליים לטראומה מינורית.</li>"
                "<li><strong>דימום חניכיים</strong> — דימום מופרז בזמן צחצוח שיניים.</li>"
                "<li><strong>דימום מהאף (אפיסטקסיס)</strong> — דימומים תכופים וקשים לעצירה.</li>"
                "<li><strong>דימום וסתי כבד (מנוראגיה)</strong> — מחזורים ארוכים וכבדים באופן חריג.</li>"
                "<li><strong>דימום GI או שתן</strong> — מלנה, המטוריה במקרים חמורים.</li>"
                "</ul>"
                "<p><strong>תסמיני תרומבוציטוזיס (PLT גבוה):</strong> תרומבוציטוזיס ריאקטיבי הוא "
                "בדרך כלל א-סימפטומטי. בתרומבוציטוזיס ראשוני עשויים להופיע:</p>"
                "<ul>"
                "<li><strong>אריתרומלגיה</strong> — כאב צורב, חום ואודם בידיים וברגליים.</li>"
                "<li><strong>כאבי ראש והפרעות ראייה</strong> — עקב חסימה מיקרו-וסקולרית.</li>"
                "<li><strong>קרישיות</strong> — DVT, תסחיף ריאתי, שבץ או אוטם שריר הלב.</li>"
                "<li><strong>דימום פרדוקסלי</strong> — בספירות מעל 1,000,000/μL עלולה להתפתח "
                "מחלת פון ווילברנד נרכשת.</li>"
                "</ul>"
                "<p>הסיכון לדימום ספונטני עולה משמעותית כאשר ספירת הטסיות יורדת מתחת ל-50,000/μL. "
                "מתחת ל-10,000–20,000/μL, דימום פנימי מסכן חיים מהווה מצב חירום רפואי.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="מתי לפנות לרופא?",
            body_html=(
                "<p>פנו לרופא בהקדם אם:</p>"
                "<ul>"
                "<li>ספירת הטסיות שלכם <strong>מתחת ל-150,000/μL או מעל 400,000/μL</strong>.</li>"
                "<li>אתם מבחינים בפטקיות, פורפורה או חבורות לא מוסברות.</li>"
                "<li>דימומים מהאף או מהחניכיים תכופים או ממושכים.</li>"
                "<li>דימום לאחר ניתוח או טיפול שיניים נמשך זמן חריג.</li>"
                "<li>כאב צורב, אודם או חום לא מוסבר בידיים או ברגליים.</li>"
                "<li>ספירת הטסיות שלכם מראה מגמה משמעותית כלפי מעלה או מטה.</li>"
                "</ul>"
                "<p>הרופא עשוי להורות על בדיקות נוספות: משטח דם היקפי, ביופסיית מח עצם, שבר "
                "טסיות צעירות (IPF), רמות תרומבופויאטין או בדיקות גנטיות (JAK2, CALR, MPL). "
                "אבחון מוקדם חיוני במיוחד במחלות המטולוגיות.</p>"
                "<p>אם הספירה נמוכה באופן קריטי (<20,000/μL) עם סימני דימום פעיל, מדובר "
                "ב<strong>מצב חירום רפואי</strong> — פנו מיד לחדר מיון.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="כיצד Norya עוזרת לך להבין את התוצאות שלך",
            body_html=(
                '<p>על ידי <a href="/analyze">העלאת בדיקת הדם שלך ל-Norya</a>, תוכל לקבל תוך '
                "דקות סיכום בריאותי מובנה וקל להבנה של PLT, MPV ופרמטרים המטולוגיים נוספים. "
                "Norya משווה את ערכיך לטווחי ההתייחסות, מדגישה סטיות פוטנציאליות ומציגה את "
                "התוצאות בפרספקטיבה הוליסטית.</p>"
                "<p>סיכום זה הוא כלי אידיאלי להיערכות לתור הרופא: תראו בבירור אילו ערכים "
                "דורשים תשומת לב, כיצד פרמטרים קשורים מתחברים ומהי התמונה הכוללת שלכם. "
                "<strong>Norya אינה מאבחנת</strong> — אך מעצימה אתכם להבין את התוצאות ולקיים "
                "שיחה פרודוקטיבית יותר עם הרופא.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="הודעה",
            body_html=(
                '<p><strong>מדריך זה נועד למידע בלבד ואינו מחליף ייעוץ או אבחון רפואי.</strong> '
                'דונו תמיד בתוצאות עם איש מקצוע רפואי. '
                '<a href="/analyze">התחל ניתוח עם Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# HINDI
# ─────────────────────────────────────────────────────────────────────
def _sections_hi() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="PLT (प्लेटलेट) परीक्षण: आपके परिणामों का क्या मतलब है?",
            body_html=(
                "<p>आपकी पूर्ण रक्त गणना (CBC) में <strong>PLT (प्लेटलेट काउंट)</strong> रक्त में "
                "प्लेटलेट्स की संख्या को दर्शाता है। प्लेटलेट्स — जिन्हें थ्रॉम्बोसाइट्स भी कहते हैं — "
                "अस्थि मज्जा में बनने वाले छोटे, बिना नाभिक वाले कोशिका खंड हैं जो रक्त के थक्के "
                "बनाकर रक्तस्राव रोकने में महत्वपूर्ण भूमिका निभाते हैं।</p>"
                "<p>सामान्य से अधिक (थ्रॉम्बोसाइटोसिस) या कम (थ्रॉम्बोसाइटोपीनिया) प्लेटलेट काउंट "
                "विभिन्न चिकित्सा स्थितियों का संकेत दे सकता है — संक्रमण और आयरन की कमी से लेकर "
                "ऑटोइम्यून रोगों और अस्थि मज्जा विकारों तक। प्लेटलेट काउंट को सही संदर्भ में "
                "समझना संभावित स्वास्थ्य समस्याओं की शीघ्र पहचान के लिए आवश्यक है।</p>"
                "<p>यह व्यापक मार्गदर्शिका बताती है कि प्लेटलेट्स क्या हैं, कैसे काम करती हैं, "
                "सामान्य मान, असामान्य गणना के कारण, PLT और MPV का संबंध, ध्यान देने योग्य "
                "लक्षण और कब डॉक्टर से मिलना चाहिए। <em>यह लेख शैक्षिक है और पेशेवर चिकित्सा "
                "सलाह का विकल्प नहीं है।</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="प्लेटलेट्स (थ्रॉम्बोसाइट्स) क्या हैं?",
            body_html=(
                "<p><strong>प्लेटलेट्स (थ्रॉम्बोसाइट्स)</strong> छोटे, नाभिकहीन कोशिका खंड हैं जो "
                "रक्तप्रवाह में घूमते हैं। ये अस्थि मज्जा में <strong>मेगाकैरियोसाइट्स</strong> नामक "
                "विशाल पूर्ववर्ती कोशिकाओं से बनते हैं। एक मेगाकैरियोसाइट हजारों प्लेटलेट्स उत्पन्न "
                "कर सकता है। प्रत्येक प्लेटलेट केवल 2–3 माइक्रोमीटर व्यास की होती है — लाल या "
                "श्वेत रक्त कोशिकाओं से बहुत छोटी — लेकिन रक्तवाहिका अखंडता बनाए रखने में इनकी "
                "भूमिका अत्यंत महत्वपूर्ण है।</p>"
                "<p>प्लेटलेट्स का जीवनकाल लगभग 7–10 दिन होता है। पुरानी होने पर ये मुख्य रूप से "
                "तिल्ली (स्प्लीन) द्वारा हटा दी जाती हैं, जो कुल प्लेटलेट पूल का लगभग एक-तिहाई "
                "भंडार के रूप में भी रखती है। इसलिए, तिल्ली के बढ़ने (स्प्लेनोमेगाली) से प्लेटलेट्स "
                "फंस सकती हैं और रक्तप्रवाह में गिनती कम हो सकती है।</p>"
                "<p>हेमोस्टेसिस के अलावा, प्लेटलेट्स एंटीमाइक्रोबियल पेप्टाइड्स जारी करके और "
                "ल्यूकोसाइट्स के साथ बातचीत करके जन्मजात प्रतिरक्षा में योगदान देती हैं। ये "
                "वृद्धि कारक (PDGF, TGF-β) भी स्रावित करती हैं जो घाव भरने, ऊतक मरम्मत और "
                "एंजियोजेनेसिस को बढ़ावा देते हैं — PRP (प्लेटलेट-रिच प्लाज्मा) थेरेपी में "
                "इन गुणों का उपयोग किया जाता है।</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="रक्त के थक्के बनने में प्लेटलेट्स की भूमिका",
            body_html=(
                "<p>जब कोई रक्तवाहिका क्षतिग्रस्त होती है, तो अंतर्निहित कोलेजन उजागर होता है और "
                "प्लेटलेट्स तुरंत क्षतिग्रस्त सतह से <strong>चिपक जाती हैं (आसंजन)</strong>। यह "
                "प्रारंभिक संपर्क <strong>वॉन विलेब्रांड फैक्टर (vWF)</strong> द्वारा मध्यस्थ होता है, "
                "एक ग्लाइकोप्रोटीन जो प्लेटलेट रिसेप्टर्स (GP Ib/IX/V) और कोलेजन के बीच आणविक "
                "गोंद का काम करता है। चिपकी हुई प्लेटलेट्स सक्रिय हो जाती हैं: वे चिकनी डिस्क से "
                "कांटेदार गोलों में बदल जाती हैं।</p>"
                "<p>सक्रिय प्लेटलेट्स अपने सघन कणिकाओं की सामग्री — ADP, थ्रॉम्बोक्सेन A2 और "
                "सेरोटोनिन — छोड़ती हैं, जो अधिक प्लेटलेट्स को स्थल पर बुलाती हैं। GP IIb/IIIa "
                "रिसेप्टर्स फाइब्रिनोजन बांधने लगते हैं, आसपास की प्लेटलेट्स को जोड़ते हैं। "
                "यह <strong>एकत्रीकरण (एग्रीगेशन)</strong> प्रक्रिया <em>प्राथमिक हेमोस्टैटिक "
                "प्लग</em> बनाती है, जो छोटी वाहिकाओं से रक्तस्राव को मिनटों में रोक सकता है।</p>"
                "<p>इसके बाद जमावट कैस्केड इस प्लग को मजबूत करता है। थ्रॉम्बिन घुलनशील "
                "फाइब्रिनोजन को अघुलनशील फाइब्रिन में बदलता है, जो प्लेटलेट प्लग को स्थिर करता है। "
                "प्लेटलेट संख्या या कार्य में कोई भी दोष इस नाजुक संतुलन को बिगाड़ सकता है, "
                "जिससे अत्यधिक रक्तस्राव या रोगात्मक थ्रॉम्बोसिस हो सकता है।</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="सामान्य प्लेटलेट (PLT) मान",
            body_html=(
                "<p>प्लेटलेट काउंट CBC के भाग के रूप में मापा जाता है और हजारों प्रति माइक्रोलीटर "
                "(×10³/μL) में रिपोर्ट किया जाता है:</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>पैरामीटर</th><th {_TH}>सामान्य सीमा</th>'
                f'<th {_TH}>टिप्पणी</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (वयस्क)</td><td {_TD}>1,50,000–4,00,000/μL</td>'
                f'<td {_TD}>दोनों लिंगों के लिए समान</td></tr>'
                f'<tr><td {_TD}>PLT (नवजात)</td><td {_TD}>1,50,000–4,50,000/μL</td>'
                f'<td {_TD}>पहले हफ्तों में थोड़ी व्यापक सीमा</td></tr>'
                f'<tr><td {_TD}>MPV (मीन प्लेटलेट वॉल्यूम)</td><td {_TD}>7.5–12.0 fL</td>'
                f'<td {_TD}>प्लेटलेट का आकार दर्शाता है</td></tr>'
                '</tbody></table>'
                "<p>प्लेटलेट काउंट दिन भर शारीरिक रूप से उतार-चढ़ाव कर सकता है। तीव्र व्यायाम "
                "के बाद अस्थायी वृद्धि होती है। मासिक धर्म के दौरान हल्की गिरावट देखी जा सकती है। "
                "<strong>स्यूडोथ्रॉम्बोसाइटोपीनिया</strong> — EDTA-प्रेरित प्लेटलेट क्लंपिंग से "
                "झूठी कम गिनती — को सिट्रेट ट्यूब में दोबारा नमूना लेकर खारिज किया जाना चाहिए।</p>"
                "<p>संदर्भ सीमाएं प्रयोगशालाओं के बीच थोड़ी भिन्न हो सकती हैं; हमेशा अपने परिणाम "
                "की तुलना अपनी रिपोर्ट पर मुद्रित संदर्भ सीमा से करें।</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="उच्च प्लेटलेट (थ्रॉम्बोसाइटोसिस) के कारण",
            body_html=(
                "<p><strong>थ्रॉम्बोसाइटोसिस</strong> 4,00,000/μL से अधिक प्लेटलेट काउंट के रूप में "
                "परिभाषित है और दो मुख्य श्रेणियों में वर्गीकृत है:</p>"
                "<p><strong>1. प्रतिक्रियात्मक (द्वितीयक) थ्रॉम्बोसाइटोसिस:</strong> अधिकांश मामलों "
                "का कारण यही है और यह किसी अंतर्निहित स्थिति की प्रतिक्रिया में होता है:</p>"
                "<ul>"
                "<li><strong>संक्रमण</strong> — IL-6 जैसे साइटोकाइन्स मेगाकैरियोपोइएसिस को उत्तेजित करते हैं।</li>"
                "<li><strong>दीर्घकालिक सूजन संबंधी रोग</strong> — रुमेटॉइड आर्थराइटिस, IBD, वैस्कुलाइटिस।</li>"
                "<li><strong>आयरन की कमी से एनीमिया</strong> — आयरन की कमी थ्रॉम्बोपोइएसिस को उत्तेजित करती है।</li>"
                "<li><strong>सर्जरी और आघात</strong> — एक्यूट फेज रिस्पॉन्स द्वारा अस्थायी वृद्धि।</li>"
                "<li><strong>स्प्लेनेक्टॉमी</strong> — तिल्ली हटाने के बाद फंसी प्लेटलेट्स मुक्त होती हैं।</li>"
                "<li><strong>दुर्दमता</strong> — कुछ कैंसर में पैरानियोप्लास्टिक थ्रॉम्बोसाइटोसिस।</li>"
                "</ul>"
                "<p><strong>2. प्राथमिक (क्लोनल) थ्रॉम्बोसाइटोसिस:</strong> अस्थि मज्जा में स्टेम सेल "
                "स्तर पर दोष से उत्पन्न होता है। माइलोप्रोलिफेरेटिव नियोप्लाज्म (एसेंशियल "
                "थ्रॉम्बोसाइथीमिया, पॉलीसाइथीमिया वेरा, क्रोनिक माइलॉयड ल्यूकीमिया) इस श्रेणी में "
                "आते हैं। <em>JAK2</em>, <em>CALR</em>, या <em>MPL</em> म्यूटेशन सामान्यतः पाए "
                "जाते हैं और थ्रॉम्बोटिक तथा रक्तस्रावी दोनों जोखिम बढ़ाते हैं।</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="कम प्लेटलेट (थ्रॉम्बोसाइटोपीनिया) के कारण",
            body_html=(
                "<p><strong>थ्रॉम्बोसाइटोपीनिया</strong> 1,50,000/μL से कम प्लेटलेट काउंट के रूप में "
                "परिभाषित है। तीन मुख्य तंत्र जिम्मेदार हैं:</p>"
                "<p><strong>1. उत्पादन में कमी:</strong></p>"
                "<ul>"
                "<li><strong>अप्लास्टिक एनीमिया</strong> — सभी कोशिका वंशों का अस्थि मज्जा विफलता।</li>"
                "<li><strong>ल्यूकीमिया, लिम्फोमा, मेटास्टैटिक कैंसर</strong> — दुर्दम घुसपैठ।</li>"
                "<li><strong>माइलोडिसप्लास्टिक सिंड्रोम (MDS)</strong> — असामान्य हेमटोपोइएसिस।</li>"
                "<li><strong>B12/फोलेट की कमी</strong> — मेगालोब्लास्टिक एनीमिया।</li>"
                "<li><strong>कीमोथेरेपी/विकिरण</strong> — अस्थायी माइलोसप्रेशन।</li>"
                "</ul>"
                "<p><strong>2. बढ़ा हुआ विनाश:</strong></p>"
                "<ul>"
                "<li><strong>इम्यून थ्रॉम्बोसाइटोपेनिक पर्पुरा (ITP)</strong> — ऑटोइम्यून एंटीबॉडी "
                "तिल्ली में प्लेटलेट विनाश को तेज करती हैं।</li>"
                "<li><strong>थ्रॉम्बोटिक थ्रॉम्बोसाइटोपेनिक पर्पुरा (TTP)</strong> — ADAMTS13 की कमी।</li>"
                "<li><strong>हेपरिन-प्रेरित थ्रॉम्बोसाइटोपीनिया (HIT)</strong> — एंटीबॉडी-मध्यस्थ "
                "विरोधाभासी प्रोथ्रॉम्बोटिक स्थिति।</li>"
                "<li><strong>डिसेमिनेटेड इंट्रावैस्कुलर कोएगुलेशन (DIC)</strong> — भारी प्लेटलेट उपभोग।</li>"
                "</ul>"
                "<p><strong>3. स्प्लेनिक सीक्वेस्ट्रेशन:</strong> सिरोसिस, पोर्टल हाइपरटेंशन या "
                "अन्य कारणों से तिल्ली बढ़ने पर अधिक प्लेटलेट्स फंस जाती हैं। दवा-प्रेरित "
                "थ्रॉम्बोसाइटोपीनिया (क्विनिडिन, वैल्प्रोइक एसिड, सल्फोनामाइड्स, कुछ "
                "एंटीबायोटिक्स) भी एक सामान्य कारण है।</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="MPV (मीन प्लेटलेट वॉल्यूम) और PLT का संबंध",
            body_html=(
                "<p><strong>MPV (मीन प्लेटलेट वॉल्यूम)</strong> प्लेटलेट्स के औसत आकार को "
                "फेम्टोलीटर (fL) में मापता है। सामान्य सीमा 7.5–12.0 fL है। MPV प्लेटलेट "
                "उत्पादन दर और अस्थि मज्जा की स्थिति के बारे में जानकारी देता है।</p>"
                "<p><strong>उच्च MPV + कम PLT:</strong> यह पैटर्न दर्शाता है कि अस्थि मज्जा "
                "परिधीय प्लेटलेट हानि की भरपाई के लिए छोटी, बड़ी प्लेटलेट्स जारी कर रही है — "
                "ITP और अन्य उपभोग कारणों में विशिष्ट। युवा प्लेटलेट्स में अधिक कणिकाएं होती "
                "हैं और हेमोस्टैटिक रूप से अधिक सक्रिय होती हैं।</p>"
                "<p><strong>कम MPV + कम PLT:</strong> यह संकेत दे सकता है कि अस्थि मज्जा स्वयं "
                "पर्याप्त प्लेटलेट्स उत्पन्न नहीं कर पा रही है — जैसा अप्लास्टिक एनीमिया, "
                "कीमोथेरेपी के बाद या माइलोडिसप्लास्टिक सिंड्रोम में देखा जाता है।</p>"
                "<p>उच्च MPV को हृदय-संवहनी जोखिम में वृद्धि से भी जोड़ा गया है। बड़ी प्लेटलेट्स "
                "एकत्रीकरण (एग्रीगेशन) के लिए अधिक प्रवण होती हैं और मायोकार्डियल इन्फार्क्शन, "
                "स्ट्रोक और शिरापरक थ्रॉम्बोएम्बोलिज्म के लिए स्वतंत्र जोखिम कारक हैं। अधिक "
                'जानकारी के लिए हमारा <a href="/blog/mpv-blood-test">MPV लेख</a> देखें।</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="उच्च और निम्न प्लेटलेट काउंट के लक्षण",
            body_html=(
                "<p><strong>थ्रॉम्बोसाइटोपीनिया (कम PLT) के लक्षण:</strong></p>"
                "<ul>"
                "<li><strong>पेटीकिए</strong> — त्वचा पर सुई जैसे लाल-बैंगनी बिंदु जो दबाने पर नहीं मिटते।</li>"
                "<li><strong>पर्पुरा</strong> — त्वचा के नीचे अधिक व्यापक रक्तस्राव क्षेत्र।</li>"
                "<li><strong>आसान चोट (एक्किमोसिस)</strong> — मामूली या बिना आघात के असमान चोट।</li>"
                "<li><strong>मसूड़ों से खून आना</strong> — ब्रश करते समय अत्यधिक रक्तस्राव।</li>"
                "<li><strong>नकसीर (एपिस्टैक्सिस)</strong> — बार-बार और रोकने में कठिन नाक से खून।</li>"
                "<li><strong>भारी मासिक धर्म रक्तस्राव (मेनोरेजिया)</strong> — असामान्य रूप से लंबे और भारी पीरियड्स।</li>"
                "<li><strong>GI या मूत्र रक्तस्राव</strong> — गंभीर मामलों में मेलेना, हेमट्यूरिया।</li>"
                "</ul>"
                "<p><strong>थ्रॉम्बोसाइटोसिस (उच्च PLT) के लक्षण:</strong> प्रतिक्रियात्मक "
                "थ्रॉम्बोसाइटोसिस आमतौर पर लक्षणहीन होता है। प्राथमिक थ्रॉम्बोसाइटोसिस में "
                "ये लक्षण हो सकते हैं:</p>"
                "<ul>"
                "<li><strong>एरिथ्रोमेलाल्जिया</strong> — हाथों और पैरों में जलन दर्द, गर्मी और लालिमा।</li>"
                "<li><strong>सिरदर्द और दृष्टि गड़बड़ी</strong> — माइक्रोवैस्कुलर रुकावट के कारण।</li>"
                "<li><strong>थ्रॉम्बोसिस</strong> — DVT, पल्मोनरी एम्बोलिज्म, स्ट्रोक या हार्ट अटैक।</li>"
                "<li><strong>विरोधाभासी रक्तस्राव</strong> — >10,00,000/μL की गिनती पर अर्जित "
                "वॉन विलेब्रांड रोग विकसित हो सकता है।</li>"
                "</ul>"
                "<p>50,000/μL से नीचे प्लेटलेट काउंट गिरने पर सहज रक्तस्राव का जोखिम काफी बढ़ "
                "जाता है। 10,000–20,000/μL से नीचे, जीवन-खतरनाक आंतरिक रक्तस्राव — जिसमें "
                "इंट्राक्रैनियल रक्तस्राव भी शामिल है — एक गंभीर चिंता बन जाती है।</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="डॉक्टर से कब मिलें?",
            body_html=(
                "<p>यदि निम्नलिखित में से कोई भी लागू होता है तो शीघ्र चिकित्सक से परामर्श करें:</p>"
                "<ul>"
                "<li>आपका प्लेटलेट काउंट <strong>1,50,000/μL से कम या 4,00,000/μL से अधिक</strong> है।</li>"
                "<li>त्वचा पर बिना कारण पेटीकिए, पर्पुरा या चोट के निशान दिख रहे हैं।</li>"
                "<li>बार-बार या लंबे समय तक नकसीर या मसूड़ों से खून आता है।</li>"
                "<li>सर्जरी या दंत प्रक्रिया के बाद रक्तस्राव असामान्य रूप से देर तक जारी रहता है।</li>"
                "<li>हाथों या पैरों में बिना कारण जलन, दर्द या लालिमा है।</li>"
                "<li>पिछले परीक्षणों की तुलना में प्लेटलेट काउंट में उल्लेखनीय ऊपर या नीचे की प्रवृत्ति है।</li>"
                "</ul>"
                "<p>डॉक्टर अतिरिक्त जांच का आदेश दे सकते हैं: पेरिफेरल ब्लड स्मीयर, अस्थि मज्जा "
                "बायोप्सी, अपरिपक्व प्लेटलेट अंश (IPF), थ्रॉम्बोपोइएटिन स्तर या आनुवंशिक परीक्षण "
                "(JAK2, CALR, MPL म्यूटेशन)। हेमटोलॉजिकल रोगों में प्रारंभिक निदान विशेष रूप से "
                "महत्वपूर्ण है।</p>"
                "<p>यदि काउंट गंभीर रूप से कम है (<20,000/μL) और सक्रिय रक्तस्राव के संकेत हैं, "
                "तो यह एक <strong>चिकित्सा आपातकाल</strong> है — निकटतम आपातकालीन विभाग में "
                "तुरंत जाएं।</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="Norya आपके परिणामों को समझने में कैसे मदद करता है",
            body_html=(
                '<p><a href="/analyze">अपनी रक्त जांच Norya पर अपलोड करके</a> आप मिनटों में अपने '
                "PLT, MPV और अन्य हेमटोलॉजिकल पैरामीटर्स का एक संरचित, समझने में आसान स्वास्थ्य "
                "सारांश प्राप्त कर सकते हैं। Norya आपके मानों की संदर्भ सीमाओं से तुलना करता है, "
                "संभावित विचलन को हाइलाइट करता है और आपके परिणामों को समग्र दृष्टिकोण से प्रस्तुत "
                "करता है।</p>"
                "<p>यह सारांश डॉक्टर की अपॉइंटमेंट की तैयारी के लिए एक आदर्श उपकरण है: आप "
                "स्पष्ट रूप से देख सकते हैं कि किन मानों पर ध्यान देने की जरूरत है, संबंधित "
                "पैरामीटर कैसे जुड़े हैं और आपकी समग्र तस्वीर कैसी दिखती है। "
                "<strong>Norya निदान नहीं करता</strong> — लेकिन यह आपको अपने परिणामों को समझने "
                "और डॉक्टर के साथ अधिक उत्पादक बातचीत करने में सक्षम बनाता है।</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="अस्वीकरण",
            body_html=(
                '<p><strong>यह गाइड केवल सूचनार्थ है; यह चिकित्सा सलाह या निदान का विकल्प नहीं है।'
                '</strong> अपने परिणामों पर हमेशा डॉक्टर से चर्चा करें। '
                '<a href="/analyze">Norya से विश्लेषण शुरू करें</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# ARABIC
# ─────────────────────────────────────────────────────────────────────
def _sections_ar() -> list:
    from app.blog_i18n import Section
    return [
        Section(
            id="intro", level=2,
            heading="تحليل PLT (الصفائح الدموية): ماذا تعني نتائجك؟",
            body_html=(
                "<p>قيمة <strong>PLT (الصفائح الدموية)</strong> في فحص الدم الشامل (CBC) تشير إلى عدد "
                "الصفائح الدموية في دمك. الصفائح الدموية — وتُسمى أيضاً الخثريات — هي أجزاء خلوية "
                "صغيرة تُنتج في نخاع العظم وتلعب دوراً أساسياً في تخثر الدم وإصلاح الأوعية الدموية "
                "المتضررة.</p>"
                "<p>عدد الصفائح الأعلى من الطبيعي (كثرة الصفيحات) أو الأدنى (قلة الصفيحات) قد يدل "
                "على حالات طبية متنوعة — من العدوى ونقص الحديد إلى أمراض المناعة الذاتية واضطرابات "
                "نخاع العظم. فهم عدد صفائحك في السياق الصحيح ضروري للكشف المبكر عن مشكلات "
                "صحية محتملة.</p>"
                "<p>يشرح هذا الدليل الشامل ما هي الصفائح الدموية، كيف تعمل، القيم الطبيعية، أسباب "
                "الأعداد غير الطبيعية، العلاقة بين PLT وMPV، الأعراض التي يجب مراقبتها ومتى يجب "
                "استشارة الطبيب. <em>هذا المقال تعليمي ولا يحل محل المشورة الطبية المتخصصة.</em></p>"
            ),
        ),
        Section(
            id="what-are-platelets", level=2,
            heading="ما هي الصفائح الدموية (الخثريات)؟",
            body_html=(
                "<p><strong>الصفائح الدموية (الخثريات)</strong> هي أجزاء خلوية صغيرة خالية من النواة "
                "تدور في مجرى الدم. تُنتج في نخاع العظم بواسطة خلايا عملاقة تُسمى "
                "<strong>الخلايا النواءية الضخمة (ميغاكاريوسيت)</strong>. يمكن لخلية نواءية واحدة "
                "إطلاق آلاف الصفائح. يبلغ قطر كل صفيحة 2–3 ميكرومتر فقط — أصغر بكثير من "
                "الكريات الحمراء أو البيضاء — لكن دورها في الحفاظ على سلامة الأوعية الدموية "
                "بالغ الأهمية.</p>"
                "<p>عمر الصفائح الدموية حوالي 7–10 أيام. بعد تقادمها، يتم إزالتها بشكل رئيسي "
                "بواسطة الطحال، الذي يعمل أيضاً كمخزن يحتفظ بحوالي ثلث مجمل الصفائح. لذلك، "
                "الحالات التي تُكبّر الطحال (تضخم الطحال) يمكنها حجز الصفائح وتقليل العدد "
                "في الدورة الدموية.</p>"
                "<p>بالإضافة إلى الإرقاء، تساهم الصفائح في المناعة الفطرية بإطلاق ببتيدات مضادة "
                "للميكروبات والتفاعل مع الكريات البيضاء. كما تفرز عوامل نمو (PDGF، TGF-β) تعزز "
                "التئام الجروح وإصلاح الأنسجة وتولد الأوعية — خصائص تُستثمر في علاج البلازما "
                "الغنية بالصفائح (PRP).</p>"
            ),
        ),
        Section(
            id="role-in-clotting", level=2,
            heading="دور الصفائح الدموية في تخثر الدم",
            body_html=(
                "<p>عندما يتعرض وعاء دموي للتلف، ينكشف الكولاجين تحت البطانة وتلتصق الصفائح "
                "فوراً بالسطح المصاب (<strong>الالتصاق</strong>). هذا التلامس الأولي يتوسطه "
                "<strong>عامل فون ويلبراند (vWF)</strong>، وهو بروتين سكري يعمل كغراء جزيئي بين "
                "مستقبلات الصفائح (GP Ib/IX/V) والكولاجين. تتنشط الصفائح الملتصقة وتتحول من "
                "أقراص ملساء إلى كرات شوكية ذات أقدام كاذبة.</p>"
                "<p>تُطلق الصفائح المنشطة محتويات حبيباتها الكثيفة — ADP، ثرومبوكسان A2 "
                "والسيروتونين — التي تجتذب المزيد من الصفائح إلى الموقع. تتغير مستقبلات "
                "GP IIb/IIIa لتربط الفيبرينوجين رابطةً الصفائح المجاورة. هذه عملية "
                "<strong>التجمع (التكدس)</strong> التي تُشكّل <em>السدادة الإرقائية الأولية</em>، "
                "القادرة على وقف النزيف من الأوعية الصغيرة خلال دقائق.</p>"
                "<p>ثم يُعزز شلال التخثر هذه السدادة. يُحوّل الثرومبين الفيبرينوجين القابل "
                "للذوبان إلى خيوط فيبرين غير قابلة للذوبان، مُشكّلاً شبكة تُثبّت تجمع الصفائح. "
                "أي خلل في عدد الصفائح أو وظيفتها قد يُخل بهذا التوازن الدقيق، مسبباً نزيفاً "
                "مفرطاً أو تخثراً مرضياً.</p>"
            ),
        ),
        Section(
            id="normal-ranges", level=2,
            heading="القيم الطبيعية للصفائح الدموية (PLT)",
            body_html=(
                "<p>يُقاس عدد الصفائح ضمن فحص الدم الشامل ويُعبّر عنه بالألف لكل ميكروليتر:</p>"
                f'{_TABLE_STYLE}'
                f'<thead><tr><th {_TH}>المعامل</th><th {_TH}>النطاق الطبيعي</th>'
                f'<th {_TH}>ملاحظة</th></tr></thead><tbody>'
                f'<tr><td {_TD}>PLT (البالغون)</td><td {_TD}>150,000–400,000/μL</td>'
                f'<td {_TD}>متساوٍ لكلا الجنسين</td></tr>'
                f'<tr><td {_TD}>PLT (حديثو الولادة)</td><td {_TD}>150,000–450,000/μL</td>'
                f'<td {_TD}>نطاق أوسع قليلاً</td></tr>'
                f'<tr><td {_TD}>MPV (متوسط حجم الصفيحة)</td><td {_TD}>7.5–12.0 fL</td>'
                f'<td {_TD}>يشير إلى حجم الصفائح</td></tr>'
                '</tbody></table>'
                "<p>قد يتقلب عدد الصفائح فسيولوجياً خلال اليوم. تحدث ارتفاعات عابرة بعد التمارين "
                "الشاقة أو التوتر. قد يُلاحظ انخفاض طفيف أثناء الحيض. يجب استبعاد "
                "<strong>نقص الصفيحات الكاذب</strong> — عدد منخفض خطأً بسبب تكتل الصفائح "
                "المُحفّز بـ EDTA — بتكرار العينة في أنبوب سيترات.</p>"
                "<p>قد تختلف النطاقات المرجعية قليلاً بين المختبرات؛ قارن دائماً نتيجتك بالنطاق "
                "المرجعي المطبوع على تقريرك.</p>"
            ),
        ),
        Section(
            id="high-platelet-causes", level=2,
            heading="أسباب ارتفاع الصفائح الدموية (كثرة الصفيحات)",
            body_html=(
                "<p><strong>كثرة الصفيحات</strong> تُعرّف بعدد صفائح أعلى من 400,000/μL "
                "وتُصنّف في فئتين:</p>"
                "<p><strong>1. كثرة صفيحات تفاعلية (ثانوية):</strong> تُشكّل الغالبية العظمى من "
                "الحالات وتحدث استجابةً لحالة أساسية:</p>"
                "<ul>"
                "<li><strong>العدوى</strong> — السيتوكينات مثل IL-6 تُحفّز تكوّن الصفائح.</li>"
                "<li><strong>أمراض التهابية مزمنة</strong> — التهاب المفاصل الروماتويدي، IBD، التهاب الأوعية.</li>"
                "<li><strong>أنيميا نقص الحديد</strong> — نقص الحديد يُحفّز إنتاج الصفائح.</li>"
                "<li><strong>الجراحة والصدمات</strong> — ارتفاع عابر بسبب استجابة الطور الحاد.</li>"
                "<li><strong>استئصال الطحال</strong> — إطلاق الصفائح المحتجزة.</li>"
                "<li><strong>الأورام الخبيثة</strong> — كثرة صفيحات أباعد ورمية في بعض السرطانات.</li>"
                "</ul>"
                "<p><strong>2. كثرة صفيحات أولية (نسيلية):</strong> تنشأ من خلل على مستوى الخلايا "
                "الجذعية في نخاع العظم. الأورام التكاثرية النقوية (كثرة الصفيحات الأساسية، "
                "كثرة الحمر الحقيقية، ابيضاض الدم النقوي المزمن) تنتمي لهذه الفئة. طفرات "
                "<em>JAK2</em> و<em>CALR</em> أو <em>MPL</em> شائعة وترفع خطر التخثر والنزيف معاً.</p>"
            ),
        ),
        Section(
            id="low-platelet-causes", level=2,
            heading="أسباب انخفاض الصفائح الدموية (قلة الصفيحات)",
            body_html=(
                "<p><strong>قلة الصفيحات</strong> تُعرّف بعدد صفائح أقل من 150,000/μL. ثلاث "
                "آليات رئيسية مسؤولة:</p>"
                "<p><strong>1. انخفاض الإنتاج:</strong></p>"
                "<ul>"
                "<li><strong>فقر الدم اللاتنسجي</strong> — فشل نخاع العظم لجميع سلالات الخلايا.</li>"
                "<li><strong>ابيضاض الدم، اللمفوما، السرطان النقيلي</strong> — ارتشاح خبيث في النخاع.</li>"
                "<li><strong>متلازمة خلل التنسج النقوي (MDS)</strong> — تكوّن دم شاذ.</li>"
                "<li><strong>نقص B12/الفولات</strong> — أنيميا أرومية ضخمة مع قلة صفيحات.</li>"
                "<li><strong>العلاج الكيميائي/الإشعاعي</strong> — كبت نخاعي عابر.</li>"
                "</ul>"
                "<p><strong>2. زيادة التدمير:</strong></p>"
                "<ul>"
                "<li><strong>فرفرية نقص الصفيحات المناعية (ITP)</strong> — أجسام مضادة ذاتية تُسرّع "
                "تدمير الصفائح في الطحال.</li>"
                "<li><strong>فرفرية نقص الصفيحات التخثرية (TTP)</strong> — نقص ADAMTS13.</li>"
                "<li><strong>قلة الصفيحات المحرضة بالهيبارين (HIT)</strong> — حالة خثارية متناقضة "
                "بوساطة أجسام مضادة.</li>"
                "<li><strong>التخثر المنتشر داخل الأوعية (DIC)</strong> — استهلاك هائل للصفائح.</li>"
                "</ul>"
                "<p><strong>3. احتجاز طحالي:</strong> عند تضخم الطحال بسبب تشمع الكبد أو فرط ضغط "
                "الوريد البابي أو أمراض ارتشاحية، يحتجز نسبة أكبر من الصفائح. قلة الصفيحات "
                "الدوائية (كينيدين، حمض الفالبرويك، السلفوناميدات، بعض المضادات الحيوية) سبب "
                "شائع أيضاً.</p>"
            ),
        ),
        Section(
            id="mpv-connection", level=2,
            heading="MPV (متوسط حجم الصفيحة) وعلاقته بـ PLT",
            body_html=(
                "<p><strong>MPV (متوسط حجم الصفيحة)</strong> يقيس متوسط حجم الصفائح بالفيمتوليتر "
                "(fL). النطاق الطبيعي 7.5–12.0 fL. يوفر MPV معلومات عن معدل إنتاج الصفائح "
                "وحالة نخاع العظم.</p>"
                "<p><strong>MPV مرتفع + PLT منخفض:</strong> يُشير إلى أن نخاع العظم يُعوّض الفقد "
                "المحيطي بإطلاق صفائح شابة وأكبر حجماً — نمط نموذجي في ITP وأسباب الاستهلاك "
                "الأخرى. الصفائح الشابة تحتوي حبيبات أكثر وأكثر نشاطاً إرقائياً.</p>"
                "<p><strong>MPV منخفض + PLT منخفض:</strong> قد يُشير إلى أن نخاع العظم نفسه "
                "عاجز عن إنتاج صفائح كافية — كما في فقر الدم اللاتنسجي، بعد العلاج الكيميائي "
                "أو في متلازمات خلل التنسج النقوي.</p>"
                "<p>ارتبط MPV المرتفع أيضاً بزيادة خطر القلب والأوعية الدموية. الصفائح الأكبر "
                "أكثر ميلاً للتجمع وعُرّفت كعامل خطر مستقل لاحتشاء عضلة القلب والسكتة الدماغية "
                "والانصمام الخثاري الوريدي. لمزيد من التفاصيل، راجع "
                '<a href="/blog/mpv-blood-test">مقالنا عن MPV</a>.</p>'
            ),
        ),
        Section(
            id="symptoms", level=2,
            heading="أعراض ارتفاع وانخفاض الصفائح الدموية",
            body_html=(
                "<p><strong>أعراض قلة الصفيحات (PLT منخفض):</strong></p>"
                "<ul>"
                "<li><strong>حَبَرات (نمشات)</strong> — نقاط حمراء-بنفسجية دقيقة على الجلد لا تختفي بالضغط.</li>"
                "<li><strong>فرفرية</strong> — مناطق أوسع من النزيف تحت الجلد.</li>"
                "<li><strong>كدمات سهلة</strong> — كدمات غير متناسبة مع رضوض بسيطة.</li>"
                "<li><strong>نزيف اللثة</strong> — نزيف مفرط عند تنظيف الأسنان.</li>"
                "<li><strong>رعاف (نزيف الأنف)</strong> — نزيف متكرر وصعب الإيقاف.</li>"
                "<li><strong>غزارة الطمث</strong> — دورات حيض طويلة وغزيرة بشكل غير طبيعي.</li>"
                "<li><strong>نزيف معدي معوي أو بولي</strong> — براز أسود، بيلة دموية في الحالات الشديدة.</li>"
                "</ul>"
                "<p><strong>أعراض كثرة الصفيحات (PLT مرتفع):</strong> كثرة الصفيحات التفاعلية "
                "عادةً بدون أعراض. في كثرة الصفيحات الأولية قد تظهر:</p>"
                "<ul>"
                "<li><strong>ألم الأطراف الاحمراري</strong> — ألم حارق ودفء واحمرار في اليدين والقدمين.</li>"
                "<li><strong>صداع واضطرابات بصرية</strong> — بسبب انسداد الأوعية الدقيقة.</li>"
                "<li><strong>تخثر</strong> — DVT، انصمام رئوي، سكتة دماغية أو احتشاء عضلة القلب.</li>"
                "<li><strong>نزيف متناقض</strong> — عند أعداد >1,000,000/μL قد تتطور مرض فون ويلبراند المكتسب.</li>"
                "</ul>"
                "<p>يزداد خطر النزيف التلقائي بشكل ملحوظ عندما ينخفض العدد تحت 50,000/μL. "
                "تحت 10,000–20,000/μL، يصبح النزيف الداخلي المهدد للحياة مصدر قلق خطير.</p>"
            ),
        ),
        Section(
            id="when-to-see-doctor", level=2,
            heading="متى يجب مراجعة الطبيب؟",
            body_html=(
                "<p>راجع طبيبك فوراً إذا انطبق أي مما يلي:</p>"
                "<ul>"
                "<li>عدد صفائحك <strong>أقل من 150,000/μL أو أعلى من 400,000/μL</strong>.</li>"
                "<li>لاحظت حبرات أو فرفرية أو كدمات غير مبررة.</li>"
                "<li>تعاني من نزيف أنفي أو لثوي متكرر أو مطوّل.</li>"
                "<li>النزيف بعد الجراحة أو علاج الأسنان يستغرق وقتاً غير عادي للتوقف.</li>"
                "<li>ألم حارق أو احمرار أو دفء غير مبرر في اليدين أو القدمين.</li>"
                "<li>عدد صفائحك يُظهر اتجاهاً ملحوظاً نحو الارتفاع أو الانخفاض.</li>"
                "</ul>"
                "<p>قد يطلب طبيبك فحوصات إضافية: لطاخة دم محيطية، خزعة نخاع عظم، كسر "
                "الصفائح غير الناضجة (IPF)، مستوى الثرومبوبويتين أو اختبارات جينية (طفرات "
                "JAK2، CALR، MPL). التشخيص المبكر بالغ الأهمية خاصةً في أمراض الدم.</p>"
                "<p>إذا كان العدد منخفضاً بشكل حرج (<20,000/μL) مع علامات نزيف نشط، "
                "فهذه <strong>حالة طوارئ طبية</strong> — توجّه فوراً لأقرب قسم طوارئ.</p>"
            ),
        ),
        Section(
            id="how-norya-helps", level=2,
            heading="كيف يساعدك Norya في فهم نتائجك",
            body_html=(
                '<p>بـ<a href="/analyze">رفع تحليل دمك على Norya</a>، يمكنك الحصول خلال دقائق '
                "على ملخص صحي منظم وسهل الفهم لقيم PLT وMPV والمعاملات الدموية الأخرى. "
                "يقارن Norya قيمك بالنطاقات المرجعية، ويُبرز الانحرافات المحتملة ويعرض نتائجك "
                "من منظور شامل.</p>"
                "<p>هذا الملخص أداة مثالية للتحضير لموعد طبيبك: ترى بوضوح أي القيم تحتاج "
                "اهتماماً، وكيف ترتبط المعاملات ببعضها وما هي صورتك العامة. "
                "<strong>Norya لا يُشخّص</strong> — لكنه يُمكّنك من فهم نتائجك وإجراء حوار أكثر "
                "إنتاجية مع طبيبك.</p>"
            ),
        ),
        Section(
            id="disclaimer", level=2,
            heading="إخلاء المسؤولية",
            body_html=(
                '<p><strong>هذا الدليل لأغراض إعلامية فقط ولا يحل محل المشورة أو التشخيص الطبي.'
                '</strong> ناقش نتائجك دائماً مع متخصص في الرعاية الصحية. '
                '<a href="/analyze">ابدأ التحليل مع Norya</a></p>'
            ),
        ),
    ]


# ─────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────
def get_plt_sections_by_lang():
    """Returns sections_by_lang dict for PLT article (all 9 languages)."""
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


def get_plt_faq_schema_qa():
    """Returns faq_schema_qa dict for PLT article (all 9 languages)."""
    return {
        "tr": [
            {"question": "Normal trombosit (PLT) değeri nedir?",
             "answer": "Yetişkinlerde normal trombosit sayısı 150.000–400.000/μL'dir. Bu aralık her iki cinsiyet için de aynıdır. Yenidoğanlarda üst sınır 450.000/μL'ye kadar çıkabilir."},
            {"question": "Yüksek trombosit sayısının nedenleri nelerdir?",
             "answer": "Yüksek trombosit (trombositoz) genellikle reaktiftir: enfeksiyonlar, kronik iltihap, demir eksikliği anemisi, cerrahi sonrası veya splenektomi nedeniyle olabilir. Daha nadir olarak, esansiyel trombositemi gibi miyeloproliferatif hastalıklar primer trombositoza yol açar."},
            {"question": "Düşük trombosit sayısının nedenleri nelerdir?",
             "answer": "Düşük trombosit (trombositopeni) kemik iliği baskılanması (lösemi, kemoterapi, B12 eksikliği), periferik yıkım (ITP, TTP, HIT, DIC) veya dalakta sekestrasyon (siroz, portal hipertansiyon) ile ortaya çıkabilir."},
            {"question": "MPV ve PLT arasındaki ilişki nedir?",
             "answer": "MPV trombositlerin ortalama boyutunu ölçer. Yüksek MPV + düşük PLT periferik yıkımı (ITP gibi) düşündürür; düşük MPV + düşük PLT kemik iliği yetersizliğine işaret edebilir. Yüksek MPV ayrıca kardiyovasküler risk artışıyla ilişkilendirilmiştir."},
            {"question": "Trombositopeni belirtileri nelerdir?",
             "answer": "Peteşi (ciltte kırmızı-mor noktalar), purpura, kolay morarma, diş eti kanaması, sık burun kanaması, ağır menstrüel kanama ve ciddi vakalarda GI veya üriner kanama görülebilir. 50.000/μL altında spontan kanama riski artar."},
        ],
        "en": [
            {"question": "What is a normal platelet (PLT) count?",
             "answer": "The normal platelet count for adults is 150,000–400,000/μL, the same for both sexes. Neonates may have a slightly wider range up to 450,000/μL."},
            {"question": "What causes high platelet count?",
             "answer": "High platelets (thrombocytosis) are most often reactive: infections, chronic inflammation, iron deficiency anemia, post-surgery, or splenectomy. Less commonly, myeloproliferative neoplasms like essential thrombocythemia cause primary thrombocytosis."},
            {"question": "What causes low platelet count?",
             "answer": "Low platelets (thrombocytopenia) can result from decreased bone marrow production (leukemia, chemotherapy, B12 deficiency), increased peripheral destruction (ITP, TTP, HIT, DIC), or splenic sequestration (cirrhosis, portal hypertension)."},
            {"question": "What is the relationship between MPV and PLT?",
             "answer": "MPV measures average platelet size. High MPV with low PLT suggests peripheral destruction (e.g., ITP); low MPV with low PLT may indicate bone marrow failure. Elevated MPV has also been linked to increased cardiovascular risk."},
            {"question": "What are the symptoms of thrombocytopenia?",
             "answer": "Symptoms include petechiae (pinpoint red-purple spots), purpura, easy bruising, gum bleeding, frequent nosebleeds, heavy menstrual bleeding, and in severe cases GI or urinary bleeding. Spontaneous bleeding risk rises below 50,000/μL."},
        ],
        "es": [
            {"question": "¿Cuál es el recuento normal de plaquetas (PLT)?",
             "answer": "El recuento normal de plaquetas para adultos es de 150.000–400.000/μL, igual para ambos sexos. Los neonatos pueden tener un rango ligeramente más amplio, hasta 450.000/μL."},
            {"question": "¿Qué causa las plaquetas altas?",
             "answer": "Las plaquetas altas (trombocitosis) son con mayor frecuencia reactivas: infecciones, inflamación crónica, anemia ferropénica, postquirúrgica o esplenectomía. Menos frecuentemente, neoplasias mieloproliferativas como la trombocitemia esencial causan trombocitosis primaria."},
            {"question": "¿Qué causa las plaquetas bajas?",
             "answer": "Las plaquetas bajas (trombocitopenia) pueden deberse a producción medular disminuida (leucemia, quimioterapia, déficit de B12), destrucción periférica aumentada (PTI, PTT, TIH, CID) o secuestro esplénico (cirrosis, hipertensión portal)."},
            {"question": "¿Cuál es la relación entre VPM (MPV) y PLT?",
             "answer": "El VPM mide el tamaño promedio de las plaquetas. VPM alto con PLT bajo sugiere destrucción periférica (ej. PTI); VPM bajo con PLT bajo puede indicar insuficiencia medular. El VPM elevado también se ha asociado a mayor riesgo cardiovascular."},
            {"question": "¿Cuáles son los síntomas de la trombocitopenia?",
             "answer": "Petequias, púrpura, hematomas fáciles, sangrado gingival, epistaxis frecuente, menorragia y en casos severos sangrado GI o urinario. El riesgo de sangrado espontáneo aumenta por debajo de 50.000/μL."},
        ],
        "de": [
            {"question": "Was ist ein normaler Thrombozytenwert (PLT)?",
             "answer": "Der normale Thrombozytenwert für Erwachsene liegt bei 150.000–400.000/μL, gleich für beide Geschlechter. Bei Neugeborenen kann der Bereich bis 450.000/μL etwas breiter sein."},
            {"question": "Was verursacht hohe Thrombozytenwerte?",
             "answer": "Hohe Thrombozyten (Thrombozytose) sind meist reaktiv: Infektionen, chronische Entzündung, Eisenmangelanämie, postoperativ oder nach Splenektomie. Seltener verursachen myeloproliferative Neoplasien wie die essenzielle Thrombozythämie eine primäre Thrombozytose."},
            {"question": "Was verursacht niedrige Thrombozytenwerte?",
             "answer": "Niedrige Thrombozyten (Thrombozytopenie) können durch verminderte Knochenmarkproduktion (Leukämie, Chemotherapie, B12-Mangel), erhöhte periphere Destruktion (ITP, TTP, HIT, DIC) oder Milzsequestration (Zirrhose, portale Hypertension) entstehen."},
            {"question": "Was ist der Zusammenhang zwischen MPV und PLT?",
             "answer": "Das MPV misst die durchschnittliche Thrombozytengröße. Hohes MPV bei niedrigem PLT deutet auf peripheren Verbrauch hin (z.B. ITP); niedriges MPV bei niedrigem PLT kann auf Knochenmarkversagen hinweisen. Erhöhtes MPV wurde auch mit erhöhtem kardiovaskulärem Risiko assoziiert."},
            {"question": "Was sind die Symptome einer Thrombozytopenie?",
             "answer": "Petechien, Purpura, leichte Blutergüsse, Zahnfleischbluten, häufiges Nasenbluten, Menorrhagie und in schweren Fällen GI- oder Harnwegsblutungen. Das Risiko spontaner Blutungen steigt unter 50.000/μL."},
        ],
        "fr": [
            {"question": "Quel est le taux normal de plaquettes (PLT) ?",
             "answer": "Le taux normal de plaquettes pour les adultes est de 150 000–400 000/μL, identique pour les deux sexes. Les nouveau-nés peuvent avoir une plage légèrement plus large, jusqu'à 450 000/μL."},
            {"question": "Quelles sont les causes des plaquettes élevées ?",
             "answer": "Les plaquettes élevées (thrombocytose) sont le plus souvent réactives : infections, inflammation chronique, anémie ferriprive, post-chirurgicale ou splénectomie. Plus rarement, les néoplasies myéloprolifératives comme la thrombocytémie essentielle causent une thrombocytose primaire."},
            {"question": "Quelles sont les causes des plaquettes basses ?",
             "answer": "Les plaquettes basses (thrombocytopénie) peuvent résulter d'une production médullaire diminuée (leucémie, chimiothérapie, carence en B12), d'une destruction périphérique accrue (PTI, PTT, TIH, CIVD) ou d'une séquestration splénique (cirrhose, hypertension portale)."},
            {"question": "Quelle est la relation entre VPM (MPV) et PLT ?",
             "answer": "Le VPM mesure la taille moyenne des plaquettes. Un VPM élevé avec un PLT bas suggère une destruction périphérique (ex. PTI) ; un VPM bas avec un PLT bas peut indiquer une insuffisance médullaire. Un VPM élevé a aussi été associé à un risque cardiovasculaire accru."},
            {"question": "Quels sont les symptômes de la thrombocytopénie ?",
             "answer": "Pétéchies, purpura, ecchymoses faciles, saignement gingival, épistaxis fréquente, ménorragie et dans les cas graves saignement GI ou urinaire. Le risque de saignement spontané augmente en dessous de 50 000/μL."},
        ],
        "it": [
            {"question": "Qual è il conteggio normale delle piastrine (PLT)?",
             "answer": "Il conteggio piastrinico normale per gli adulti è 150.000–400.000/μL, uguale per entrambi i sessi. I neonati possono avere un intervallo leggermente più ampio, fino a 450.000/μL."},
            {"question": "Quali sono le cause delle piastrine alte?",
             "answer": "Le piastrine alte (trombocitosi) sono più spesso reattive: infezioni, infiammazione cronica, anemia sideropenica, post-chirurgica o splenectomia. Meno frequentemente, neoplasie mieloproliferative come la trombocitemia essenziale causano trombocitosi primaria."},
            {"question": "Quali sono le cause delle piastrine basse?",
             "answer": "Le piastrine basse (trombocitopenia) possono derivare da ridotta produzione midollare (leucemia, chemioterapia, carenza di B12), aumentata distruzione periferica (ITP, TTP, HIT, CID) o sequestro splenico (cirrosi, ipertensione portale)."},
            {"question": "Qual è la relazione tra MPV e PLT?",
             "answer": "L'MPV misura la dimensione media delle piastrine. MPV alto con PLT basso suggerisce distruzione periferica (es. ITP); MPV basso con PLT basso può indicare insufficienza midollare. Un MPV elevato è stato anche associato a maggiore rischio cardiovascolare."},
            {"question": "Quali sono i sintomi della trombocitopenia?",
             "answer": "Petecchie, porpora, ecchimosi facili, sanguinamento gengivale, epistassi frequente, menorragia e nei casi gravi sanguinamento GI o urinario. Il rischio di sanguinamento spontaneo aumenta sotto 50.000/μL."},
        ],
        "he": [
            {"question": "מהי ספירת טסיות (PLT) תקינה?",
             "answer": "ספירת טסיות תקינה למבוגרים היא 150,000–400,000/μL, זהה לשני המינים. ליילודים ייתכן טווח רחב מעט יותר, עד 450,000/μL."},
            {"question": "מה גורם לטסיות גבוהות?",
             "answer": "טסיות גבוהות (תרומבוציטוזיס) הן לרוב ריאקטיביות: זיהומים, דלקת כרונית, אנמיה מחסר ברזל, לאחר ניתוח או כריתת טחול. נדיר יותר, ניאופלזמות מיאלופרוליפרטיביות כמו תרומבוציטמיה אסנציאלית גורמות לתרומבוציטוזיס ראשוני."},
            {"question": "מה גורם לטסיות נמוכות?",
             "answer": "טסיות נמוכות (תרומבוציטופניה) יכולות לנבוע מייצור מופחת במח העצם (לוקמיה, כימותרפיה, חסר B12), הרס היקפי מוגבר (ITP, TTP, HIT, DIC) או ספיגה טחולית (שחמת, יתר לחץ דם פורטלי)."},
            {"question": "מה הקשר בין MPV ל-PLT?",
             "answer": "MPV מודד את גודל הטסיות הממוצע. MPV גבוה עם PLT נמוך מרמז על הרס היקפי (כמו ITP); MPV נמוך עם PLT נמוך עשוי להעיד על כשל מח עצם. MPV מוגבר נקשר גם לסיכון קרדיווסקולרי מוגבר."},
            {"question": "מהם תסמיני תרומבוציטופניה?",
             "answer": "פטקיות, פורפורה, חבורות קלות, דימום חניכיים, דימום אף תכוף, מנוראגיה ובמקרים חמורים דימום GI או שתן. סיכון לדימום ספונטני עולה מתחת ל-50,000/μL."},
        ],
        "hi": [
            {"question": "सामान्य प्लेटलेट (PLT) काउंट क्या है?",
             "answer": "वयस्कों के लिए सामान्य प्लेटलेट काउंट 1,50,000–4,00,000/μL है, दोनों लिंगों के लिए समान। नवजातों में 4,50,000/μL तक का थोड़ा व्यापक रेंज हो सकता है।"},
            {"question": "उच्च प्लेटलेट काउंट के कारण क्या हैं?",
             "answer": "उच्च प्लेटलेट्स (थ्रॉम्बोसाइटोसिस) अक्सर प्रतिक्रियात्मक होते हैं: संक्रमण, दीर्घकालिक सूजन, आयरन की कमी से एनीमिया, सर्जरी के बाद या स्प्लेनेक्टॉमी। अधिक दुर्लभ रूप से, माइलोप्रोलिफेरेटिव नियोप्लाज्म जैसे एसेंशियल थ्रॉम्बोसाइथीमिया प्राथमिक थ्रॉम्बोसाइटोसिस का कारण बनता है।"},
            {"question": "कम प्लेटलेट काउंट के कारण क्या हैं?",
             "answer": "कम प्लेटलेट्स (थ्रॉम्बोसाइटोपीनिया) कम अस्थि मज्जा उत्पादन (ल्यूकीमिया, कीमोथेरेपी, B12 की कमी), बढ़ा हुआ परिधीय विनाश (ITP, TTP, HIT, DIC) या स्प्लेनिक सीक्वेस्ट्रेशन (सिरोसिस, पोर्टल हाइपरटेंशन) के कारण हो सकते हैं।"},
            {"question": "MPV और PLT के बीच क्या संबंध है?",
             "answer": "MPV प्लेटलेट्स का औसत आकार मापता है। कम PLT के साथ उच्च MPV परिधीय विनाश (जैसे ITP) का सुझाव देता है; कम PLT के साथ कम MPV अस्थि मज्जा विफलता का संकेत दे सकता है। उच्च MPV को हृदय-संवहनी जोखिम वृद्धि से भी जोड़ा गया है।"},
            {"question": "थ्रॉम्बोसाइटोपीनिया के लक्षण क्या हैं?",
             "answer": "पेटीकिए, पर्पुरा, आसान चोट, मसूड़ों से खून, बार-बार नकसीर, मेनोरेजिया और गंभीर मामलों में GI या मूत्र रक्तस्राव। 50,000/μL से नीचे सहज रक्तस्राव का जोखिम बढ़ता है।"},
        ],
        "ar": [
            {"question": "ما هو العدد الطبيعي للصفائح الدموية (PLT)؟",
             "answer": "العدد الطبيعي للصفائح الدموية للبالغين هو 150,000–400,000/μL، متساوٍ لكلا الجنسين. قد يكون للمواليد نطاق أوسع قليلاً يصل إلى 450,000/μL."},
            {"question": "ما أسباب ارتفاع الصفائح الدموية؟",
             "answer": "ارتفاع الصفائح (كثرة الصفيحات) غالباً تفاعلي: عدوى، التهاب مزمن، أنيميا نقص الحديد، بعد الجراحة أو استئصال الطحال. أقل شيوعاً، الأورام التكاثرية النقوية مثل كثرة الصفيحات الأساسية تسبب كثرة صفيحات أولية."},
            {"question": "ما أسباب انخفاض الصفائح الدموية؟",
             "answer": "انخفاض الصفائح (قلة الصفيحات) قد ينتج عن نقص إنتاج نخاع العظم (ابيضاض الدم، العلاج الكيميائي، نقص B12)، زيادة التدمير المحيطي (ITP، TTP، HIT، DIC) أو احتجاز طحالي (تشمع، فرط ضغط بابي)."},
            {"question": "ما العلاقة بين MPV وPLT؟",
             "answer": "MPV يقيس متوسط حجم الصفائح. MPV مرتفع مع PLT منخفض يشير إلى تدمير محيطي (مثل ITP)؛ MPV منخفض مع PLT منخفض قد يدل على فشل نخاع العظم. ارتبط MPV المرتفع أيضاً بزيادة خطر أمراض القلب والأوعية."},
            {"question": "ما أعراض قلة الصفيحات؟",
             "answer": "حبرات (نمشات)، فرفرية، كدمات سهلة، نزيف اللثة، رعاف متكرر، غزارة الطمث وفي الحالات الشديدة نزيف معدي معوي أو بولي. يزداد خطر النزيف التلقائي تحت 50,000/μL."},
        ],
    }
