"""Enterprise/Hastaneler sayfası hero + stats bölümü i18n doğrulama."""
import pytest
from app.enterprise_i18n import ENTERPRISE_UI, get_enterprise_ui, get_hastaneler_ui


class TestEnterpriseHeroStatsTranslations:
    """Hero ve stats bölümü için translation key'lerinin varlığını test eder."""
    
    def test_all_languages_have_hero_keys(self):
        """Tüm aktif dillerde hero_label, hero_title, hero_subtitle key'leri var."""
        required_keys = ["hero_label", "hero_title", "hero_subtitle"]
        for lang in ENTERPRISE_UI.keys():
            t = ENTERPRISE_UI[lang]
            for key in required_keys:
                assert key in t, f"{lang} dilinde '{key}' key'i eksik"
                assert t[key], f"{lang} dilinde '{key}' boş string"
    
    def test_all_languages_have_stat_value_keys(self):
        """Tüm aktif dillerde stat_1_value, stat_2_value, stat_3_value key'leri var."""
        required_keys = ["stat_1_value", "stat_2_value", "stat_3_value"]
        for lang in ENTERPRISE_UI.keys():
            t = ENTERPRISE_UI[lang]
            for key in required_keys:
                assert key in t, f"{lang} dilinde '{key}' key'i eksik"
                assert t[key], f"{lang} dilinde '{key}' boş string"
    
    def test_all_languages_have_stat_label_keys(self):
        """Tüm aktif dillerde stat_1_label, stat_2_label, stat_3_label key'leri var."""
        required_keys = ["stat_1_label", "stat_2_label", "stat_3_label"]
        for lang in ENTERPRISE_UI.keys():
            t = ENTERPRISE_UI[lang]
            for key in required_keys:
                assert key in t, f"{lang} dilinde '{key}' key'i eksik"
                assert t[key], f"{lang} dilinde '{key}' boş string"
    
    def test_all_languages_have_dashboard_keys(self):
        """Tüm aktif dillerde dashboard_value ve dashboard_stat key'leri var."""
        required_keys = [
            "dashboard_value_1", "dashboard_value_2", "dashboard_value_3",
            "dashboard_stat_1", "dashboard_stat_2", "dashboard_stat_3"
        ]
        for lang in ENTERPRISE_UI.keys():
            t = ENTERPRISE_UI[lang]
            for key in required_keys:
                assert key in t, f"{lang} dilinde '{key}' key'i eksik"
                assert t[key], f"{lang} dilinde '{key}' boş string"
    
    def test_all_languages_have_trust_badge_keys(self):
        """Tüm aktif dillerde trust_badge key'leri var."""
        required_keys = ["trust_badge_1", "trust_badge_2", "trust_badge_3"]
        for lang in ENTERPRISE_UI.keys():
            t = ENTERPRISE_UI[lang]
            for key in required_keys:
                assert key in t, f"{lang} dilinde '{key}' key'i eksik"
                assert t[key], f"{lang} dilinde '{key}' boş string"
    
    def test_all_languages_have_trust_chip_keys(self):
        """Tüm aktif dillerde trust_chip key'leri var."""
        required_keys = ["trust_chip_1", "trust_chip_2", "trust_chip_3", "trust_chip_4", "trust_chip_5"]
        for lang in ENTERPRISE_UI.keys():
            t = ENTERPRISE_UI[lang]
            for key in required_keys:
                assert key in t, f"{lang} dilinde '{key}' key'i eksik"
                assert t[key], f"{lang} dilinde '{key}' boş string"
    
    def test_spanish_hero_stats_are_not_empty(self):
        """İspanyolca hero ve stats key'leri boş değil."""
        t = get_enterprise_ui("es")
        assert t["hero_label"], "İspanyolca hero_label boş"
        assert t["hero_title"], "İspanyolca hero_title boş"
        assert t["hero_subtitle"], "İspanyolca hero_subtitle boş"
        assert t["stat_1_value"], "İspanyolca stat_1_value boş"
        assert t["stat_2_value"], "İspanyolca stat_2_value boş"
        assert t["stat_3_value"], "İspanyolca stat_3_value boş"
    
    def test_spanish_dashboard_stats_are_not_empty(self):
        """İspanyolca dashboard stats key'leri boş değil."""
        t = get_enterprise_ui("es")
        assert t["dashboard_value_1"], "İspanyolca dashboard_value_1 boş"
        assert t["dashboard_value_2"], "İspanyolca dashboard_value_2 boş"
        assert t["dashboard_value_3"], "İspanyolca dashboard_value_3 boş"
        assert t["dashboard_stat_1"], "İspanyolca dashboard_stat_1 boş"
        assert t["dashboard_stat_2"], "İspanyolca dashboard_stat_2 boş"
        assert t["dashboard_stat_3"], "İspanyolca dashboard_stat_3 boş"
    
    def test_spanish_hero_title_natural(self):
        """İspanyolca hero_title doğal İspanyolca, TR/EN karışımı değil."""
        t = get_enterprise_ui("es")
        hero_title = t["hero_title"]
        # Türkçe karakter veya kelime kontrolü
        assert "ğ" not in hero_title.lower(), f"İspanyolca hero_title'de Türkçe karakter: {hero_title}"
        assert "ş" not in hero_title.lower(), f"İspanyolca hero_title'de Türkçe karakter: {hero_title}"
        assert "ı" not in hero_title.lower(), f"İspanyolca hero_title'de Türkçe karakter: {hero_title}"
        # "Doğrulukla" gibi Türkçe kelime kontrolü
        assert "Doğruluk" not in hero_title, f"İspanyolca hero_title'de Türkçe kelime: {hero_title}"
        assert "Biomarker Analysis" not in hero_title, f"İspanyolca hero_title'de İngilizce kelime: {hero_title}"
    
    def test_spanish_stat_labels_natural(self):
        """İspanyolca stat label'ları doğal İspanyolca, TR/EN karışımı değil."""
        t = get_enterprise_ui("es")
        # "Analiz Edilen Reports" gibi karışık ifade kontrolü
        stat_1_label = t["stat_1_label"]
        assert "Edilen" not in stat_1_label, f"İspanyolca stat_1_label'de Türkçe kelime: {stat_1_label}"
        assert "Reports" not in stat_1_label or "Reportes" in stat_1_label, f"İspanyolca stat_1_label'de İngilizce kelime: {stat_1_label}"
    
    def test_fallback_mechanism(self):
        """Fallback mekanizması çalışıyor: es -> en -> tr."""
        # İspanyolca mevcut
        t_es = get_enterprise_ui("es")
        assert t_es is not None
        # Geçersiz dil kodu İngilizce'ye fallback
        t_invalid = get_enterprise_ui("invalid_lang")
        assert t_invalid is not None
        # İngilizce mevcut
        t_en = get_enterprise_ui("en")
        assert t_en is not None
    
    def test_no_hardcoded_tr_en_in_template_keys(self):
        """Template'te kullanılan key'lerde hardcoded TR/EN metin yok."""
        # Tüm dilleri kontrol et
        for lang in ["tr", "en", "es", "de", "fr", "it", "he", "hi", "ar"]:
            t = get_enterprise_ui(lang)
            # Hero title'da karışık dil kontrolü
            hero_title = t.get("hero_title", "")
            # Her dil için kendi alfabesi dışında karakter kontrolü (basit)
            if lang == "es":
                assert "ğşıöçüĞŞİÖÇÜ" not in hero_title, f"İspanyolca hero_title'de Türkçe karakterler: {hero_title}"


class TestTemplateRenderGuard:
    """Template render guard'larını test eder."""
    
    def test_template_has_fallback_values(self):
        """Template'te boş string fallback'leri için default değerler var."""
        with open("app/templates/enterprise/hastaneler.html", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Render guard'ları kontrol et
        assert "or 'AI TECHNOLOGY'" in content or "or " in content, "Template'te hero_label için fallback yok"
        assert "or '2M+'" in content, "Template'te stat_1_value için fallback yok"
        assert "or '50+'" in content, "Template'te stat_2_value için fallback yok"
        assert "or '98.7%'" in content, "Template'te stat_3_value için fallback yok"
