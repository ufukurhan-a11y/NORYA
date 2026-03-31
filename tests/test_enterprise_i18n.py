# -*- coding: utf-8 -*-
"""Test enterprise i18n translations for hospitals page."""

import pytest
from app.enterprise_i18n import (
    ENTERPRISE_UI,
    ENTERPRISE_LANGS,
    get_enterprise_ui,
    get_hastaneler_ui,
)


# Hospitals page-specific keys that must exist in TR and EN
HOSPITALS_REQUIRED_KEYS = [
    # Navigation
    "nav_hospitals",
    "subnav_general",
    "subnav_why",
    "subnav_teams",
    "subnav_usage",
    "subnav_pilot",
    "mobile_menu_title",
    "hospitals_breadcrumb",
    # Dashboard & Trust
    "dashboard_live",
    "dashboard_stat_1",
    "dashboard_stat_2",
    "dashboard_stat_3",
    "trust_badge_1",
    "trust_badge_2",
    "trust_badge_3",
    "trust_chip_1",
    "trust_chip_2",
    "trust_chip_3",
    "trust_chip_4",
    "trust_chip_5",
    # Pilot & Contact
    "pilot_badge",
    "pilot_subtitle",
    "contact_title",
]


class TestEnterpriseI18nTR:
    """Test Turkish translations."""

    def test_tr_dictionary_exists(self):
        """TR dictionary should exist."""
        assert "tr" in ENTERPRISE_UI

    def test_tr_has_all_hospitals_keys(self):
        """TR should have all hospitals page keys."""
        tr_dict = ENTERPRISE_UI["tr"]
        for key in HOSPITALS_REQUIRED_KEYS:
            assert key in tr_dict, f"TR dictionary missing key: {key}"

    def test_tr_values_not_empty(self):
        """TR values should not be empty strings."""
        tr_dict = ENTERPRISE_UI["tr"]
        for key in HOSPITALS_REQUIRED_KEYS:
            value = tr_dict.get(key, "")
            assert value, f"TR value empty for key: {key}"
            assert len(value.strip()) > 0, f"TR value whitespace for key: {key}"

    def test_tr_nav_hospitals_value(self):
        """TR nav_hospitals should be 'Hastaneler'."""
        assert ENTERPRISE_UI["tr"]["nav_hospitals"] == "Hastaneler"

    def test_tr_subnav_general_value(self):
        """TR subnav_general should be 'Genel'."""
        assert ENTERPRISE_UI["tr"]["subnav_general"] == "Genel"


class TestEnterpriseI18nEN:
    """Test English translations."""

    def test_en_dictionary_exists(self):
        """EN dictionary should exist."""
        assert "en" in ENTERPRISE_UI

    def test_en_has_all_hospitals_keys(self):
        """EN should have all hospitals page keys."""
        en_dict = ENTERPRISE_UI["en"]
        for key in HOSPITALS_REQUIRED_KEYS:
            assert key in en_dict, f"EN dictionary missing key: {key}"

    def test_en_values_not_empty(self):
        """EN values should not be empty strings."""
        en_dict = ENTERPRISE_UI["en"]
        for key in HOSPITALS_REQUIRED_KEYS:
            value = en_dict.get(key, "")
            assert value, f"EN value empty for key: {key}"
            assert len(value.strip()) > 0, f"EN value whitespace for key: {key}"

    def test_en_nav_hospitals_value(self):
        """EN nav_hospitals should be 'Hospitals'."""
        assert ENTERPRISE_UI["en"]["nav_hospitals"] == "Hospitals"

    def test_en_subnav_general_value(self):
        """EN subnav_general should be 'Overview'."""
        assert ENTERPRISE_UI["en"]["subnav_general"] == "Overview"


class TestEnterpriseI18nOtherLangs:
    """Test other languages have fallback values."""

    @pytest.mark.parametrize("lang", ["de", "fr", "es", "it", "he", "hi", "ar"])
    def test_lang_exists(self, lang):
        """Language dictionary should exist."""
        assert lang in ENTERPRISE_UI

    @pytest.mark.parametrize("lang", ["de", "fr", "es", "it", "he", "hi", "ar"])
    def test_lang_has_nav_hospitals(self, lang):
        """Language should have nav_hospitals key with non-empty value."""
        lang_dict = ENTERPRISE_UI[lang]
        assert "nav_hospitals" in lang_dict, f"{lang} missing nav_hospitals"
        value = lang_dict["nav_hospitals"]
        assert value, f"{lang} nav_hospitals is empty"
        assert len(value.strip()) > 0, f"{lang} nav_hospitals is whitespace"

    @pytest.mark.parametrize("lang", ["de", "fr", "es", "it", "he", "hi", "ar"])
    def test_lang_has_dashboard_keys(self, lang):
        """Language should have dashboard keys with non-empty values."""
        lang_dict = ENTERPRISE_UI[lang]
        for key in ["dashboard_live", "dashboard_stat_1", "trust_badge_1"]:
            assert key in lang_dict, f"{lang} missing {key}"
            value = lang_dict[key]
            assert value, f"{lang} {key} is empty"


class TestGetEnterpriseUI:
    """Test get_enterprise_ui helper function."""

    def test_returns_tr_for_tr(self):
        """Should return TR dict for tr lang."""
        result = get_enterprise_ui("tr")
        assert result["nav_home"] == "Ana Sayfa"
        assert result["nav_hospitals"] == "Hastaneler"

    def test_returns_en_for_en(self):
        """Should return EN dict for en lang."""
        result = get_enterprise_ui("en")
        assert result["nav_home"] == "Home"
        assert result["nav_hospitals"] == "Hospitals"

    def test_fallback_for_unknown_lang(self):
        """Should fallback to EN for unknown language."""
        result = get_enterprise_ui("xyz")
        # Unknown lang should fallback to EN
        assert result["nav_home"] == "Home"

    def test_all_supported_langs_return_dict(self):
        """All supported langs should return a dict."""
        for lang in ENTERPRISE_LANGS:
            result = get_enterprise_ui(lang)
            assert isinstance(result, dict)
            # Should have at least nav_home
            assert "nav_home" in result


class TestGetHastanelerUI:
    """Test get_hastaneler_ui helper function."""

    def test_returns_tr_for_tr(self):
        """Should return TR dict for tr lang."""
        result = get_hastaneler_ui("tr")
        assert result["nav_hospitals"] == "Hastaneler"

    def test_returns_en_for_en(self):
        """Should return EN dict for en lang."""
        result = get_hastaneler_ui("en")
        assert result["nav_hospitals"] == "Hospitals"

    def test_fallback_for_unknown_lang(self):
        """Should fallback to EN for unknown language."""
        result = get_hastaneler_ui("xyz")
        # Unknown lang should fallback to EN
        assert result["nav_hospitals"] == "Hospitals"
