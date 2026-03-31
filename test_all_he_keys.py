# -*- coding: utf-8 -*-
"""Tüm kart ve feature key'lerini kontrol et"""
import sys
sys.path.insert(0, '/Users/ufukurhan/norya')

from app.enterprise_i18n import ENTERPRISE_UI

he = ENTERPRISE_UI.get("he", {})
en = ENTERPRISE_UI.get("en", {})

# Template'de kullanılan tüm kart/feature key'leri
required_keys = [
    # Hospital cards (neden bölümü)
    "card_hospital_1_title",
    "card_hospital_1_desc",
    "card_hospital_2_title",
    "card_hospital_2_desc",
    "card_hospital_3_title",
    "card_hospital_3_desc",
    
    # Enterprise features (AI banner sonrası)
    "feature_analytics_title",
    "feature_analytics_desc",
    "feature_monitoring_title",
    "feature_monitoring_desc",
    "feature_integration_title",
    "feature_integration_desc",
    "feature_compliance_title",
    "feature_compliance_desc",
    
    # Badges
    "ai_powered_badge",
    "realtime_badge",
    "custom_badge",
    "certified_badge",
    
    # Feature lists
    "analytics_feature_1",
    "analytics_feature_2",
    "analytics_feature_3",
    "monitoring_feature_1",
    "monitoring_feature_2",
    "monitoring_feature_3",
    
    # Integration items
    "restful_api",
    "webhook_support_label",
    
    # Compliance items
    "hipaa_compliant_badge",
    "audit_trail_label",
    
    # AI technology chips
    "feature_ml",
    "feature_pattern_recognition",
    "feature_predictive_analytics",
]

print("=== İbranice (he) vs İngilizce (en) Karşılaştırma ===\n")
missing_he = []
empty_he = []

for key in required_keys:
    he_val = he.get(key)
    en_val = en.get(key, "N/A")
    
    if he_val is None:
        missing_he.append(key)
        print(f"❌ MISSING (he): {key}")
        print(f"   EN: {en_val}")
    elif he_val.strip() == "":
        empty_he.append(key)
        print(f"⚠️  EMPTY (he): {key}")
        print(f"   EN: {en_val}")
    else:
        # print(f"✅ OK: {key}")
        pass

print(f"\n=== Özet ===")
print(f"Missing in Hebrew: {len(missing_he)}")
print(f"Empty in Hebrew: {len(empty_he)}")

if missing_he:
    print(f"\n=== Eksik Key'ler (İbranice) ===")
    for key in missing_he:
        print(f"  - {key}")
        print(f"    EN: {en.get(key, 'N/A')}")

if empty_he:
    print(f"\n=== Boş Key'ler (İbranice) ===")
    for key in empty_he:
        print(f"  - {key}")
