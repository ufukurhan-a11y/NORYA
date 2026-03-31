# -*- coding: utf-8 -*-
"""Tüm teams section key'lerini kontrol et"""
import sys
sys.path.insert(0, '/Users/ufukurhan/norya')

from app.enterprise_i18n import ENTERPRISE_UI

he = ENTERPRISE_UI.get("he", {})

# Teams section için gereken tüm key'ler
required_keys = [
    "teams_title",
    "teams_subtitle",
    "team_1_title",
    "team_1_desc",
    "team_2_title",
    "team_2_desc",
    "team_3_title",
    "team_3_desc",
    "team_4_title",
    "team_4_desc",
]

print("=== Teams Section Key Kontrolü (İbranice) ===\n")
missing = []
for key in required_keys:
    val = he.get(key)
    if val is None or val.strip() == "":
        missing.append(key)
        print(f"❌ MISSING/EMPTY: {key}")
    else:
        print(f"✅ OK: {key} = {val[:50]}...")

print(f"\n=== Özet ===")
print(f"Missing/Empty: {len(missing)}")
if missing:
    print(f"\nEksikler: {missing}")
