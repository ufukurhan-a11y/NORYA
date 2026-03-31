# -*- coding: utf-8 -*-
"""Tüm dillerde teams section key'lerini kontrol et"""
import sys
sys.path.insert(0, '/Users/ufukurhan/norya')

from app.enterprise_i18n import ENTERPRISE_UI

LANGS = ["tr", "en", "es", "de", "fr", "it", "he", "hi", "ar"]

required_keys = [
    "teams_title",
    "teams_subtitle",
    "team_1_title",
    "team_2_title",
    "team_3_title",
    "team_3_desc",
    "team_4_title",
]

print("=== Tüm Dillerde Teams Section Kontrolü ===\n")

for lang in LANGS:
    data = ENTERPRISE_UI.get(lang, {})
    missing = []
    
    for key in required_keys:
        val = data.get(key)
        if val is None or val.strip() == "":
            missing.append(key)
    
    if missing:
        print(f"❌ {lang.upper()} - Eksik: {len(missing)}")
        for key in missing:
            print(f"   - {key}")
    else:
        print(f"✅ {lang.upper()} - Tüm key'ler mevcut!")
    
    print()
