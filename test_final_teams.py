# -*- coding: utf-8 -*-
"""Final test - tüm teams key'leri"""
import sys
sys.path.insert(0, '/Users/ufukurhan/norya')

from app.enterprise_i18n import ENTERPRISE_UI

he = ENTERPRISE_UI.get("he", {})

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

print("=== Final Test - Teams Section (İbranice) ===\n")
all_ok = True
for key in required_keys:
    val = he.get(key)
    if val is None or val.strip() == "":
        print(f"❌ MISSING/EMPTY: {key}")
        all_ok = False
    else:
        print(f"✅ OK: {key} = {val}")

print(f"\n{'='*50}")
if all_ok:
    print("✅ TÜM KEY'LER DOLU!")
else:
    print("❌ Hala eksik key'ler var!")
