# -*- coding: utf-8 -*-
"""Tüm template key'lerini kontrol et"""
import sys
sys.path.insert(0, '/Users/ufukurhan/norya')

from app.enterprise_i18n import ENTERPRISE_UI

he = ENTERPRISE_UI.get("he", {})

# Template'de kullanılan ve eksik olabilecek tüm key'ler
required_keys = [
    # Enterprise features section
    "enterprise_features_title",
    "hospital_operations_ai_desc",
    
    # Stats at bottom
    "uptime_sla",
    "api_response",
    
    # Teams section
    "teams_title",
    "teams_subtitle",
]

print("=== Eksik Olabilecek Key'ler ===\n")
for key in required_keys:
    val = he.get(key)
    if val is None or val.strip() == "":
        print(f"❌ MISSING/EMPTY: {key}")
    else:
        print(f"✅ OK: {key} = {val[:50]}...")
