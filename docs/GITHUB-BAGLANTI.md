# Norya — GitHub'a Bağlanma ve Push

Proje zaten GitHub remote'a bağlı: `https://github.com/ufukurhan-a11y/NORYA.git`  
Push atarken **"Password authentication is not supported"** hatası alıyorsan aşağıdakileri uygula.

---

## 1. GitHub'da Personal Access Token (PAT) oluştur

1. **GitHub.com** → sağ üst **profil fotoğrafı** → **Settings**
2. Sol menü en altta → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)** veya **Fine-grained tokens**
4. **Generate new token (classic)** seç
5. **Note:** örn. `Norya push`
6. **Expiration:** 90 days veya No expiration (tercihine göre)
7. **Scopes:** `repo` işaretle (tüm kutucuklar altında "repo" tek başına yeterli)
8. **Generate token** → Çıkan token'ı **bir yere kopyala** (bir daha gösterilmez)

---

## 2. Token ile push (terminalde)

### Yöntem A — Sadece bu seferlik (komutla)

```bash
cd /Users/ufukurhan/norya
git push https://KULLANICI_ADIN:TOKEN@github.com/ufukurhan-a11y/NORYA.git main
```

- `KULLANICI_ADIN` → GitHub kullanıcı adın (örn. ufukurhan-a11y)
- `TOKEN` → Az önce kopyaladığın token (ghp_ ile başlar)

### Yöntem B — Her push'ta sorar (önerilen)

```bash
cd /Users/ufukurhan/norya
git push -u origin main
```

- **Username:** GitHub kullanıcı adın
- **Password:** Buraya **şifreni değil**, oluşturduğun **token'ı** yapıştır

Token'ı bir kez girdikten sonra (macOS Keychain / Windows Credential Manager) genelde tekrar sormaz.

### Yöntem C — Remote URL'e token göm (dikkatli kullan)

```bash
cd /Users/ufukurhan/norya
git remote set-url origin https://ufukurhan-a11y:TOKEN_BURAYA@github.com/ufukurhan-a11y/NORYA.git
git push -u origin main
```

Bu şekilde token repo içinde veya komut geçmişinde kalabilir; güvenlik için Yöntem B daha iyi.

---

## 3. İlk kez repo yoksa (GitHub'da yeni repo)

1. GitHub → **New repository**
2. **Repository name:** NORYA (veya norya)
3. **Public** seç, README ekleme (projede zaten var)
4. **Create repository**
5. Sonra terminalde:

```bash
cd /Users/ufukurhan/norya
git remote add origin https://github.com/KULLANICI_ADIN/NORYA.git
git branch -M main
git push -u origin main
```

Şifre sorduğunda **token** gir.

---

## Özet

- Remote zaten var: `origin` → `https://github.com/ufukurhan-a11y/NORYA.git`
- Sorun: GitHub şifre kabul etmiyor → **Personal Access Token** oluştur
- Push: `git push -u origin main` → Username + **Password alanına token** yapıştır

Token oluşturma: **GitHub → Settings → Developer settings → Personal access tokens → Generate new token (classic) → repo işaretle**
