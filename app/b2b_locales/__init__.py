# Full B2B audience page translations (non-EN/TR).
from __future__ import annotations

from app.b2b_locales import ar as ar_locale
from app.b2b_locales import de as de_locale
from app.b2b_locales import es as es_locale
from app.b2b_locales import fr as fr_locale
from app.b2b_locales import he as he_locale
from app.b2b_locales import hi as hi_locale
from app.b2b_locales import it as it_locale

LOCALE_BUILDERS = {
    "de": de_locale.build_pages,
    "fr": fr_locale.build_pages,
    "it": it_locale.build_pages,
    "es": es_locale.build_pages,
    "he": he_locale.build_pages,
    "hi": hi_locale.build_pages,
    "ar": ar_locale.build_pages,
}


def get_full_locale_pages(lang: str, pages_en: dict) -> dict:
    builder = LOCALE_BUILDERS.get(lang)
    if not builder:
        return {}
    return builder(pages_en)
