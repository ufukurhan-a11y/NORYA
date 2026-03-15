# Norya’yı yerelde çalıştırma (Risk Factors PDF’i görmek için)

Terminalde **proje klasöründe** olun ve aşağıdakileri sırayla yapın.

## 1. Proje klasörüne geçin

```bash
cd /Users/ufukurhan/norya
```

## 2. Sanal ortam (venv) oluşturup açın

```bash
python3 -m venv .venv
source .venv/bin/activate
```

(Bir kez yaptıktan sonra sadece `source .venv/bin/activate` yeterli.)

## 3. Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

## 4. Sunucuyu başlatın

**Seçenek A – start.sh ile:**

```bash
chmod +x start.sh
./start.sh
```

**Seçenek B – doğrudan uvicorn ile:**

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 5. Tarayıcıda açın

- Adres: **http://127.0.0.1:8000**
- Bir analiz yapıp **PDF indir** dediğinizde, raporda **Risk Faktörleri** bölümü (başlık + iki madde) görünür.

---

**Not:** `./start.sh` “no such file” veriyorsa mutlaka `cd /Users/ufukurhan/norya` ile proje klasörüne geçin; komutu orada çalıştırın.
