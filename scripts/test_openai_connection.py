#!/usr/bin/env python3
"""
OpenAI bağlantı testi: .env'deki anahtarı ve api.openai.com erişimini kontrol eder.
Kullanım: proje kökünden  .venv/bin/python scripts/test_openai_connection.py
"""
import os
import sys

# Proje kökünü path'e ekle
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

def main():
    print("1. .env ve OPENAI_API_KEY kontrolü...")
    from app.core.config import get_openai_keys, is_openai_configured

    if not is_openai_configured():
        print("   HATA: OPENAI_API_KEY .env'de yok veya sk- ile başlamıyor.")
        print("   .env dosyasına ekleyin: OPENAI_API_KEY=sk-...")
        return 1
    keys = get_openai_keys()
    print(f"   OK: {len(keys)} anahtar tanımlı (sk-...{keys[0][-4:]})")

    print("\n2. api.openai.com erişimi (basit TCP)...")
    try:
        import socket
        s = socket.create_connection(("api.openai.com", 443), timeout=5)
        s.close()
        print("   OK: 443 portu açık.")
    except OSError as e:
        print(f"   HATA: Sunucu api.openai.com:443'e ulaşamıyor: {e}")
        print("   Firewall, proxy veya ağ kısıtlaması olabilir.")
        return 1

    print("\n3. OpenAI API ping (gerçek istek)...")
    from app.services.analyze import ping_openai
    ok, latency_ms, err = ping_openai()
    if ok:
        print(f"   OK: Yanıt {latency_ms} ms.")
        return 0
    print(f"   HATA: {err or 'Bilinmeyen'}")
    print("\n   Olası nedenler:")
    print("   - API anahtarı iptal/geçersiz veya billing kapalı (platform.openai.com)")
    print("   - Proxy/VPN: HTTPS_PROXY ortam değişkeni gerekebilir")
    print("   - Ülke/ISP engeli: Farklı ağdan (örn. mobil) deneyin")
    return 1


if __name__ == "__main__":
    sys.exit(main())
