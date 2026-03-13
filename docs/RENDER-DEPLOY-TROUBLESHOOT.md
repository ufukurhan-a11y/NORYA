# Render dağıtım hatası giderme (d8011aa / i18n)

## Hata mesajını görme

1. **Render Dashboard** → Projeniz → **Logs**
2. **Build logs**: `pip install` veya derleme hatası (örn. WeasyPrint sistem kütüphaneleri)
3. **Deploy logs** / **Runtime logs**: Uygulama başlarken (örn. `uvicorn` / `gunicorn`) veya ilk istekte oluşan hata

Sık görülenler:

- **ImportError / ModuleNotFoundError**: Eksik paket veya yanlış Python path
- **SyntaxError**: İlgili commit’teki bir dosyada sözdizimi hatası
- **KeyError / AttributeError**: Şablona gönderilen `blog_ui` veya `legal` objesinde eksik anahtar
- **Application failed to start**: Genelde `app.main:app` import edilirken veya lifespan sırasında hata

## Yapılan iyileştirmeler (d8011aa sonrası)

- **Blog index**: `blog_ui` artık `dict(BLOG_UI.get(lang, BLOG_UI[DEFAULT_BLOG_LANG]))` ile oluşturuluyor; şablonda eksik anahtar riski azaltıldı.
- **Blog detail**: Aynı mantıkla `blog_ui` güvenli fallback ile set ediliyor.

## Yerelde test

```bash
cd /Users/ufukurhan/norya
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Uygulama açılıyorsa sorun büyük ihtimalle Render ortamına özgü (env, build, sistem kütüphaneleri). Log’taki tam hata mesajını paylaşırsanız nedeni netleştirilebilir.
