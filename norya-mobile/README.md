# Norya Mobil

Norya kan tahlili analizi uygulamasının React Native (Expo) ile yazılmış mobil sürümü.

## Gereksinimler

- Node.js 18+
- npm veya yarn
- Expo Go (telefonda test için) veya iOS Simulator / Android Emulator

### Node.js yüklü değilse (macOS)

Terminalde `npm` veya `npx` "command not found" hatası alıyorsanız Node.js kurulu değildir. Şu yollardan biriyle kurun:

1. **Resmi site (en kolay):** [nodejs.org](https://nodejs.org) → "LTS" sürümünü indirip kurun. Kurulum bitince **yeni bir terminal** açın.
2. **Homebrew varsa:** `brew install node` — ardından yeni terminal açın.

Kontrol: `node -v` ve `npm -v` yazıp sürüm numarası görünmeli.

## Kurulum

Terminalde **Norya proje kökünde** olduğunuzdan emin olun (Cursor’da açtığınız NORYA klasörü). Sonra:

```bash
cd norya-mobile
npm install
```

## API adresi (opsiyonel)

Varsayılan olarak uygulama canlı API kullanır: `https://noryaai.com`

Yerel backend kullanmak için:

- **Android emülatör:** `EXPO_PUBLIC_API_URL=http://10.0.2.2:8000`
- **iOS simülatör:** `EXPO_PUBLIC_API_URL=http://localhost:8000`
- **Fiziksel cihaz:** Bilgisayarınızın yerel IP’si, örn. `EXPO_PUBLIC_API_URL=http://192.168.1.10:8000`

`.env` dosyası oluşturup şunu yazabilirsiniz:

```
EXPO_PUBLIC_API_URL=http://192.168.1.10:8000
```

## Çalıştırma

```bash
npm run start
```

QR kodu Expo Go ile tarayıp telefonda açın veya `i` (iOS) / `a` (Android) ile emülatörde açın.

### Telefon "sunucuya bağlanamıyor" diyorsa (tünel)

Bilgisayar ve telefon aynı Wi‑Fi’de olsa bile bazen bağlantı kurulamaz. **Tünel modu** kullanın; telefon internetten bağlansın:

```bash
npm run start:tunnel
```

Çıkan **yeni QR kodu** Expo Go ile tekrar tarayın. İlk açılış biraz yavaş olabilir.

## Özellikler

- **Giriş / Kayıt** — E-posta, şifre, ad, telefon, ülke
- **Analiz** — Tahlil metnini yapıştırma veya galeri/kamera ile fotoğraf yükleme
- **Rapor** — Analiz sonucunu okuma
- **Geçmiş** — Daha önceki analizlere erişim

Backend ile aynı API kullanılır: `/auth/login`, `/auth/register`, `/auth/me`, `/analyze`, `/analyze/upload`, `/analyze/history`, `/analyze/history/:id`.
