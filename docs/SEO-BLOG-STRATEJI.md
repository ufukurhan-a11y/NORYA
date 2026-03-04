# SEO Blog Stratejisi — Ultra Premium, Stealth Tarzı

## Ayda ne kadar trafik beklenir?

| Dönem | Beklenti (organik arama) | Not |
|--------|---------------------------|-----|
| **İlk 1–3 ay** | 50–300 ziyaret/ay | Google indeksleme, sıralama henüz oturmadı |
| **3–6 ay** | 300–1.500 ziyaret/ay | 5–10 kaliteli makale + düzenli içerik, uzun kuyruk kelimeler |
| **6–12 ay** | 1.000–5.000+ ziyaret/ay | 15–25 makale, otorite artışı, backlink ve paylaşımlar |
| **12+ ay** | 3.000–15.000+ ziyaret/ay | Güçlü site otoritesi, çok dil, güvenilir kaynak olarak görülme |

**Önemli:** Rakamlar alan (sağlık), rekabet ve dil sayısına göre değişir. Reklamsız organik trafik sabır ister; kaliteli, “ultra premium” içerik uzun vadede sıralamayı ve paylaşımı artırır.

---

## Nereden başlamalı?

### 1. İlk 5 makale (öncelik sırasıyla)

| # | Konu (TR) | Hedef anahtar | Niyet | Zorluk |
|---|-----------|----------------|--------|--------|
| 1 | **Kan tahlili nasıl okunur?** | kan tahlili nasıl okunur, tahlil sonucu yorumlama | Bilgi + “benim raporum” | Orta |
| 2 | **LDL kolesterol** (mevcut) | ldl kolesterol kaç olmalı, ldl yüksek | Bilgi + hedef değer | Var |
| 3 | **Referans aralığı ne demek?** | referans aralığı, normal değer nedir | Bilgi | Düşük |
| 4 | **Hemoglobin ve anemi** | hemoglobin kaç olmalı, kansızlık belirtileri | Bilgi + semptom | Orta |
| 5 | **B12 ve D vitamini** | b12 eksikliği, d vitamini kaç olmalı | Bilgi + takviye | Orta |

### 2. Sonraki 5 makale

- CRP ve inflamasyon
- Açlık kan şekeri ve HbA1c
- Karaciğer enzimleri (ALT, AST, GGT)
- Böbrek fonksiyonu (kreatinin, eGFR)
- Demir ve ferritin

### 3. Stealth / ultra premium kurallar

- **Sade, güvenilir dil** — Tıbbi iddia yok, “bilgilendirme amaçlı” vurgusu.
- **Tanım kutuları** — Terimler (LDL, referans aralığı, hemoglobin) kısa bir cümleyle açıklanır.
- **Örnekler** — “Örnek: Sonuç kâğıdında 145 mg/dL görüyorsanız…” gibi somut cümleler.
- **Görseller** — Kapak + makale içi 1–2 şema/grafik (ör. referans aralığı şeması); gerçek hasta verisi yok.
- **Yapı** — Net H2/H3, içindekiler, okunabilir paragraflar (2–4 cümle).
- **CTA** — Sadece makale sonunda tek blok: “Tahlilinizi Norya ile analiz edin.”

---

## Teknik SEO (mevcut + kontrol)

- [x] Canonical URL
- [x] Meta description, OG etiketleri
- [x] Sitemap’te blog URL’leri
- [x] Article / MedicalWebPage schema (blog detail)
- [ ] Her makalede 1–2 internal link (diğer blog veya /analyze)
- [ ] Görseller: `alt` metni, mümkünse lazy loading (var)

---

## İçerik şablonu (ultra premium makale)

1. **Başlık (H1)** — Anahtar kelime + fayda (örn. “Kan Tahlili Nasıl Okunur? Adım Adım Rehber”).
2. **Kısa giriş** — 2–3 cümle, niyet: “Bu yazıda … öğreneceksiniz.”
3. **İçindekiler** — H2’lere link (mevcut template’te var).
4. **Bölümler** — Her H2’de:
   - 1–2 paragraf
   - Gerekirse **tanım kutusu** (terim açıklaması)
   - Gerekirse **örnek kutusu** (sayı veya senaryo)
   - Gerekirse **görsel** (şema, örnek rapor çizimi) + caption
5. **Kapanış** — 1 paragraf özet + tek CTA (Norya analiz).

---

## Özet

- **Trafik:** İlk aylar 50–300, 6–12 ay içinde 1.000–5.000+ organik ziyaret/ay hedeflenebilir.
- **Başlangıç:** “Kan tahlili nasıl okunur” + “Referans aralığı” + “Hemoglobin” ile ilk 3 ultra premium makale.
- **Stil:** Stealth = sade, kurumsal, tanım + örnek + görsel; teşhis/tedavi önerisi yok.

---

## Teknik notlar (yapılanlar)

- **Blog makale bileşenleri** (`blog/detail.html`): `.blog-definition`, `.blog-example`, `.blog-figure` stilleri eklendi. Makale içinde bu sınıflarla tanım kutusu, örnek kutusu ve resim+caption kullanılabilir.
- **İlk ultra premium makale:** “Kan tahlili nasıl okunur” (`blog_i18n.py`) — TR ve EN tam metin; tanım ve örnek kutuları kullanıldı. Kapak görseli: `/static/images/blog/kan-tahlili-nasil-okunur.png` (dosyayı eklemeniz gerekir; yoksa placeholder veya mevcut bir blog görseli kullanılabilir).
