# Norya Fatura Rehberi (e-Arşiv / e-Fatura)

## e-Arşiv mi, e-Fatura mı?

| | e-Arşiv | e-Fatura |
|---|--------|----------|
| **Kime** | Bireysel (şahıs) müşteri | Kurumsal (şirket) müşteri |
| **Ne zaman zorunlu** | Vergi mükellefi olmayan alıcıya KDV dahil 9.900 TL’yi aşan satış (2025); 2026’dan itibaren tüm B2C satışlar | e-Fatura mükellefi şirketlere yapılan satışlar |
| **Norya** | ✅ Uygun — B2C (bireysel kullanıcı) satış yapıyorsanız **e-arşiv** kullanın | Sadece e-Fatura mükellefi bir firmaya satış yaparsanız e-Fatura gerekir |

**Özet:** Norya gibi bireysel abonelik/tek analiz satan uygulamalar için **e-arşiv fatura** doğru tercihtir.

---

## Nasıl kesilir?

1. **GİB e-Arşiv Portal (manuel)**  
   [earsivportal.efatura.gov.tr](https://earsivportal.efatura.gov.tr) — İnteraktif vergi dairesi bilgilerinizle giriş, fatura tek tek elle oluşturulur. e-imza gerekmez; onay “GİB İmza” (SMS) ile yapılır.
2. **Yazılımla (Norya entegrasyonu)**  
   Admin panelinden tamamlanan siparişe tıklayıp “E-arşiv fatura kes” ile GİB’e otomatik gönderim. Alıcı TC kimlik no ve ad/soyad girmeniz yeterli.

---

## Norya’da kurulum

1. **.env** içinde GİB ve firma bilgilerini doldurun (aşağıdaki “Config” bölümü).
2. GİB e-Arşiv Portal şifrenizi (ve varsa test modu) ayarlayın.
3. Admin → Ödemeler → ilgili sipariş → “E-arşiv fatura kes” ile fatura oluşturun.  
   Fatura GİB’e gider; onay için cep telefonunuza gelen SMS kodunu girmeniz istenebilir (GİB İmza).

---

## Tutar: EUR / TL

- Norya ödemeleri **EUR** (PayTR) ile alınıyor.
- GİB e-arşiv fatura tutarı **TL** olarak girilir.
- `.env` içinde `INVOICE_EUR_TO_TRY_RATE` ile 1 EUR = kaç TL kullanılacağını belirleyin (örn. `35.50`).  
  Günlük kur kullanmak isterseniz bu değeri düzenli güncellemeniz veya ileride kuru bir API’den çekmeniz gerekir.

---

## Config (.env) özeti

```
# GİB e-Arşiv (e-arşiv fatura kesmek için)
GIB_EARSIV_USER=          # Vergi/TC kimlik no (10 veya 11 hane)
GIB_EARSIV_PASSWORD=       # e-Arşiv portal şifresi
GIB_EARSIV_TEST_MODE=1     # 1 = test, 0 = canlı

# Firma bilgileri (faturada görünecek)
INVOICE_COMPANY_TITLE=     # Ünvan (örn. Norya Teknoloji A.Ş.)
INVOICE_COMPANY_TAX_OFFICE=
INVOICE_COMPANY_ADDRESS=
INVOICE_COMPANY_CITY=
INVOICE_COMPANY_EMAIL=

# 1 EUR = X TL (fatura tutarını TL’ye çevirmek için)
INVOICE_EUR_TO_TRY_RATE=35.50
```

Bu alanlar boşsa “E-arşiv fatura kes” butonu çalışmaz veya uyarı verir; doldurduktan sonra kullanabilirsiniz.
