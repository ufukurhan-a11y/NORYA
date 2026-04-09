# NoryaAI International SEO Optimization Guide

## 🎯 Objective

Achieve first-page rankings in all target countries through comprehensive international SEO optimization.

## 🌍 Target Languages & Countries

| Language | Code | Target Countries |
|----------|------|------------------|
| Turkish | tr | Turkey 🇹🇷 |
| English | en | USA 🇺🇸, UK 🇬🇧, Canada 🇨🇦, Australia 🇦🇺 |
| Spanish | es | Spain 🇪🇸, Latin America 🌎 |
| German | de | Germany 🇩🇪, Austria 🇦🇹, Switzerland 🇨🇭 |
| French | fr | France 🇫🇷, Belgium 🇧🇪, Switzerland 🇨🇭 |
| Italian | it | Italy 🇮🇹 |
| Hebrew | he | Israel 🇮🇱 |
| Hindi | hi | India 🇮🇳 |
| Arabic | ar | Middle East 🌍 |

## ✅ Implemented Features

### 1. Hreflang Tags

All enterprise pages now include proper hreflang tags for all 9 languages:

```html
<link rel="alternate" hreflang="x-default" href="https://noryaai.com/hastaneler-icin?lang=en" />
<link rel="alternate" hreflang="tr" href="https://noryaai.com/hastaneler-icin?lang=tr" />
<link rel="alternate" hreflang="en" href="https://noryaai.com/hastaneler-icin?lang=en" />
<link rel="alternate" hreflang="es" href="https://noryaai.com/hastaneler-icin?lang=es" />
<link rel="alternate" hreflang="de" href="https://noryaai.com/hastaneler-icin?lang=de" />
<link rel="alternate" hreflang="fr" href="https://noryaai.com/hastaneler-icin?lang=fr" />
<link rel="alternate" hreflang="it" href="https://noryaai.com/hastaneler-icin?lang=it" />
<link rel="alternate" hreflang="he" href="https://noryaai.com/hastaneler-icin?lang=he" />
<link rel="alternate" hreflang="hi" href="https://noryaai.com/hastaneler-icin?lang=hi" />
<link rel="alternate" hreflang="ar" href="https://noryaai.com/hastaneler-icin?lang=ar" />
<link rel="canonical" href="https://noryaai.com/hastaneler-icin?lang=tr" />
```

### 2. Open Graph & Social Media SEO

Enhanced social media sharing with proper locale tags:

```html
<meta property="og:locale" content="tr_TR" />
<meta property="og:title" content="..." />
<meta property="og:description" content="..." />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="NoryaAI" />
```

### 3. Schema.org Structured Data

Added comprehensive structured data for better search engine understanding:

- **Organization Schema**: Company information, founder, contact details
- **MedicalOrganization Schema**: Medical service descriptions
- **AvailableService**: AI blood test analysis service

### 4. Canonical URLs

Each language variant has its own canonical URL to prevent duplicate content issues.

### 5. Meta Titles & Descriptions

All 9 languages have optimized meta titles and descriptions with:
- Target keywords in native language
- Proper length (50-60 chars for title, 150-160 for description)
- Call-to-action elements
- Brand consistency

## 📊 Key Metrics for Success

### Target Keywords by Market

#### Turkey (TR)
- "kan tahlili akıllı analiz"
- "hastane akıllı analiz çözümleri"
- "laboratuvar rapor analizi"
- "klinik karar destek sistemi"

#### Germany (DE)
- "bluttest KI analyse"
- "krankenhaus künstliche intelligenz"
- "laborbericht analyse software"
- "klinische entscheidungsunterstützung"

#### USA/UK (EN)
- "AI blood test analysis"
- "hospital AI solutions"
- "laboratory report interpretation"
- "clinical decision support system"

#### Spain (ES)
- "análisis IA análisis de sangre"
- "soluciones IA hospitales"
- "interpretación resultados laboratorio"

#### France (FR)
- "analyse IA prise de sang"
- "solutions IA hôpitaux"
- "interprétation résultats laboratoire"

### Core Web Vitals Targets

- **LCP (Largest Contentful Paint)**: < 2.5s
- **FID (First Input Delay)**: < 100ms
- **CLS (Cumulative Layout Shift)**: < 0.1
- **FCP (First Contentful Paint)**: < 1.8s

## 🔧 Technical Implementation

### Backend (Python/FastAPI)

```python
@app.get("/hastaneler-icin", response_class=HTMLResponse)
def hastaneler_icin_page(request: Request, lang: str = "tr"):
    from app.enterprise_i18n import (
        ENTERPRISE_LANGS, 
        get_hastaneler_ui, 
        get_hastaneler_hreflang_tags
    )
    
    lang = _enterprise_lang_from_request(request)
    t = get_hastaneler_ui(lang)
    base_url = str(request.base_url).rstrip("/")
    hreflang_tags = get_hastaneler_hreflang_tags(base_url, lang)
    
    return templates.TemplateResponse(
        "enterprise/hastaneler.html",
        {
            "request": request,
            "lang": lang,
            "t": t,
            "canonical_url": f"{base_url}/hastaneler-icin",
            "hreflang_tags": hreflang_tags,
        },
    )
```

### Frontend (HTML Template)

Key SEO elements in template:
1. Language-specific `<html lang="{{ lang }}">`
2. RTL support for Arabic and Hebrew
3. Dynamic meta tags from i18n
4. Hreflang tags for all language variants
5. Schema.org JSON-LD structured data

## 📈 Monitoring & Analytics

### Google Search Console

- Monitor impressions, clicks, CTR by country
- Track keyword rankings per language
- Identify indexing issues
- Submit sitemaps per language

### Key Metrics to Track

1. **Organic Traffic by Country**
   - Turkey: Target 40% of total
   - DACH (DE/AT/CH): Target 20%
   - North America: Target 15%
   - Other EU: Target 15%
   - Middle East & Asia: Target 10%

2. **Keyword Rankings**
   - Top 3 positions for branded terms
   - Top 10 for "AI + blood test + [language]"
   - Top 10 for "hospital AI solutions + [country]"

3. **Click-Through Rate (CTR)**
   - Target CTR: >3% for informational queries
   - Target CTR: >5% for branded queries

## 🚀 Next Steps

### Phase 1: Content Localization (Week 1-2)
- [ ] Create country-specific landing pages
- [ ] Add local case studies and testimonials
- [ ] Implement local phone numbers and addresses
- [ ] Create region-specific blog content

### Phase 2: Technical SEO (Week 3-4)
- [ ] Optimize images with WebP format
- [ ] Implement lazy loading for images
- [ ] Add preconnect hints for third-party resources
- [ ] Minify CSS and JavaScript
- [ ] Enable gzip/brotli compression

### Phase 3: Link Building (Week 5-8)
- [ ] Submit to local medical directories
- [ ] Create shareable research and statistics
- [ ] Partner with local medical associations
- [ ] Guest posting on medical technology blogs
- [ ] Press releases in target countries

### Phase 4: Performance Optimization (Ongoing)
- [ ] Monitor Core Web Vitals weekly
- [ ] A/B test meta titles and descriptions
- [ ] Optimize for featured snippets
- [ ] Implement FAQ schema for common questions
- [ ] Add video schema for demo content

## 📝 Best Practices

### Do's ✅
- Use native speakers for content translation
- Include local phone numbers and addresses
- Create country-specific case studies
- Optimize for local search engines (Yandex, Baidu if expanding)
- Use local domain extensions if possible (noryaai.de, noryaai.fr)
- Implement proper hreflang for all pages
- Create XML sitemaps per language
- Add local structured data (LocalBusiness)

### Don'ts ❌
- Don't use auto-translate for medical content
- Don't mix languages on the same page
- Don't forget mobile optimization
- Don't ignore local regulations (GDPR, HIPAA)
- Don't use generic stock images
- Don't duplicate content across languages
- Don't forget to validate schema markup

## 🔍 Validation Tools

- **Google Search Console**: Monitor indexing and performance
- **Schema Markup Validator**: https://validator.schema.org/
- **Rich Results Test**: https://search.google.com/test/rich-results
- **Mobile-Friendly Test**: https://search.google.com/test/mobile-friendly
- **PageSpeed Insights**: https://pagespeed.web.dev/
- **Hreflang Tags Testing**: https://www.sistrix.com/hreflang-validator/

## 📞 Support

For SEO questions or issues:
- Email: support@noryaai.com
- Technical: info@noryaai.com

---

**Last Updated**: March 31, 2026  
**Version**: 1.0  
**Next Review**: April 30, 2026
