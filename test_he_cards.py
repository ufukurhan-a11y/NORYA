# -*- coding: utf-8 -*-
"""Test İbranice kart key'leri"""
import sys
sys.path.insert(0, '/Users/ufukurhan/norya')

from app.enterprise_i18n import ENTERPRISE_UI

he = ENTERPRISE_UI.get("he", {})

# Kartlar için gereken key'ler
required_keys = [
    "card_hospital_1_title",
    "card_hospital_1_desc",
    "card_hospital_2_title",
    "card_hospital_2_desc",
    "card_hospital_3_title",
    "card_hospital_3_desc",
    "feature_analytics_title",
    "feature_analytics_desc",
    "feature_monitoring_title",
    "feature_monitoring_desc",
    "feature_integration_title",
    "feature_integration_desc",
    "feature_compliance_title",
    "feature_compliance_desc",
    "ai_powered_badge",
    "realtime_badge",
    "custom_badge",
    "certified_badge",
    "analytics_feature_1",
    "analytics_feature_2",
    "analytics_feature_3",
    "monitoring_feature_1",
    "monitoring_feature_2",
    "monitoring_feature_3",
    "restful_api",
    "webhook_support_label",
    "hipaa_compliant_badge",
    "audit_trail_label",
]

print("=== İbranice (he) Kart Key Kontrolü ===\n")
missing = []
empty = []
for key in required_keys:
    value = he.get(key)
    if value is None:
        missing.append(key)
        print(f"❌ EXMISSING: {key}")
    elif value.strip() == "":
        empty.append(key)
        print(f"⚠️  EMPTY: {key}")
    else:
        print(f"✅ OK: {key} = {value[:60]}...")

print(f"\n=== Özet ===")
print(f"Missing: {len(missing)}")
print(f"Empty: {len(empty)}")
if missing:
    print(f"\nEksik key'ler: {missing}")
if empty:
    print(f"\nBoş key'ler: {empty}")
