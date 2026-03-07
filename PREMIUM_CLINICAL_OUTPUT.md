# Premium Clinical Output — Tamamlanan Özellikler

## Değişen Dosyalar

| Dosya | Değişiklik |
|-------|------------|
| `app/schemas/analyze.py` | `HealthScoreSchema`, `UiHintsSchema`, `PdfInfoSchema`; `AnalyzeResponse` alanları: `premium`, `health_score`, `trend`, `ui_hints`, `pdf` |
| `app/services/risk_engine.py` | Ağırlıklı `overall_score` (cardio 0.35, metabolic 0.30, inflammation 0.15, vitamin 0.20); level 0-33 low, 34-66 mid, 67-100 high |
| `app/services/report_pdf.py` | `_gauge_svg` stroke-dasharray; `_trend_svg()`, `extract_trend_from_results()`, `_build_premium_context(trend_data)`; `build_report_pdf(trend_data=)`; i18n: report_health_score_title, report_risk_indicator_title, report_trend_title, report_trend_need_more, report_upgrade, report_premium_badge, report_disclaimer_* (TR/EN/DE/FR/ES/IT/AR/HE/HI/EL/CS/SR) |
| `app/main.py` | `_build_analyze_response()`, `_get_trend_for_user()`; `/analyze` ve upload yanıtları yeni şema; PDF indirme: `plan_name="premium"` + `trend_data` |
| `app/templates/report_premium.html` | Trend bölümü: `trend_svg` \| safe veya trend_bars (date, ldl_pct, glucose_pct, crp_pct) |
| `static/index.html` | `buildPremiumClinicalBlock`: health_score, trend, locked overlay, "Premium'a Geç" CTA; renderReport opts: health_score, trend, ui_hints, premium |
| `static/css/report.css` | .premium-clinical-wrap, .report-premium-locked, .premium-locked-overlay, .premium-cta-btn, .trend-chart bar stilleri |
| `static/report_premium.css` | .trend-svg |

---

## Örnek API Response

### Premium (plan: monthly veya yearly)

```json
{
  "sonuc": "**Özet**\n...",
  "notu": "Norya AI yorumladı.",
  "analiz_id": 42,
  "cached": false,
  "premium": true,
  "risk_summary": {
    "overall": { "level": "mid", "score": 72 },
    "domains": {
      "cardio": { "level": "mid", "score": 58, "reasons": [], "flags": [] },
      "metabolic": { "level": "low", "score": 18, "reasons": [], "flags": [] },
      "inflammation": { "level": "low", "score": 18, "reasons": [], "flags": [] },
      "vitamin": { "level": "mid", "score": 50, "reasons": [], "flags": [] }
    },
    "highlights": []
  },
  "health_score": { "score": 72, "level": "mid" },
  "trend": {
    "dates": ["01.02.2025", "15.02.2025", "01.03.2025"],
    "ldl": [110, 105, 98],
    "glucose": [95, 92, 90],
    "crp": [2.1, 1.8, 1.5]
  },
  "ui_hints": { "locked": false },
  "pdf": { "template": "premium", "available": true }
}
```

### Free / Basic

```json
{
  "sonuc": "**Özet**\n...",
  "notu": "Norya AI yorumladı.",
  "analiz_id": 43,
  "cached": false,
  "premium": false,
  "risk_summary": { "overall": { "level": "mid", "score": 72 }, "domains": { ... }, "highlights": [] },
  "health_score": { "score": 72, "level": "mid" },
  "trend": null,
  "ui_hints": { "locked": true },
  "pdf": { "template": "basic", "available": true }
}
```

---

## Davranış Özeti

- **Plan kuralları (net):**
  - **premiumPdf** = plan in ("single", "monthly", "yearly") → Premium PDF şablonu, gauge + health score PDF’de ve UI’da açık.
  - **premiumTrend** = plan in ("monthly", "yearly") → Trend verisi ve trend grafiği sadece bu planlarda açık.
  - **premiumUI** = premiumPdf → Gauge + health score UI’da kilitli değil; trend sadece premiumTrend’de açık.
  - **Free plan:** Locked overlay + "Premium'a Geç" → `/pay?from=report`.
- **Risk engine:** `overall_score` ağırlıklı ortalama; `overall_level`: 0-33 low, 34-66 mid, 67-100 high. Domain skorları 0-100.
- **Trend:** Premium kullanıcı için son 3 analiz (mevcut hariç) çekilir; `dates`, `ldl`, `glucose`, `crp` doldurulur. Yoksa `trend: null` ve metin: "Trend için daha fazla analiz gerekli."
- **Frontend:** Premium ise skor kartı, gauge ve trend tam görünür. Free ise aynı alanlar blur + kilit overlay + "Premium'a Geç" → `/pay?from=report`.
- **PDF:** Premium plan için `report_premium.html` (Sağlık Skoru, Risk Göstergesi, Trend Analizi); gauge stroke-dasharray; trend mini bar SVG. Basic için `report_pdf.html`. Header/footer running element, break-inside: avoid, tüm başlıklar i18n.
- **RTL:** ` report_premium.html` ve `report_premium.css` içinde `dir="{{ 'rtl' if lang in ['ar','he'] else 'ltr' }}"` ve `[dir="rtl"]` mevcut.
- **i18n:** İstenen key’ler TR/EN/DE/FR/ES/IT/AR/HE/HI/EL/CS/SR için PDF_LABELS ve (TR/EN için) frontend T’ye eklendi.

---

## Premium PDF Görünümü (Screenshot Yerine Açıklama)

Premium PDF’de sırayla:

1. **Header (running):** PREMIUM badge, logo, "Kan Tahlili Analiz Raporu", Rapor No / Kullanıcı / Tarih / Dil.
2. **Uyarı kutusu:** "Bilgilendirme amaçlıdır. Bu rapor tıbbi teşhis veya tedavi yerine geçmez..."
3. **Sağlık Skoru:** Başlık (i18n), büyük skor (örn. 72 / 100), band etiketi (Düşük/Orta/İyi).
4. **Risk Göstergesi:** Yarım daire SVG gauge (stroke-dasharray ile doluluk), ortada skor.
5. **Trend Analizi:** Varsa trend SVG (3 tarih, LDL/Glucose/CRP barlar); yoksa "Trend için daha fazla analiz gerekli."
6. **Risk Özeti:** 4 risk kartı (Kardiyovasküler, Metabolik, Vitamin, Enflamasyon).
7. **Öne Çıkan Bulgular**, **Test Sonuçları** tablosu, **Klinik Notlar** (Özet, Bulgular, Nedenler, Öneriler, Takip, Doktora Not).
8. **Footer (running):** "Norya • Bilgilendirme amaçlıdır • support@noryaai.com"

Gerçek görüntü için tarayıcıdan veya uygulama içinden Premium kullanıcı ile analiz yapıp "Raporu İndir" ile PDF alıp açabilirsiniz.
