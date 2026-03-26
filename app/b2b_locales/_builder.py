from __future__ import annotations

import copy
from typing import Any


def mk(
    en_page: dict[str, Any],
    *,
    faq: list[dict[str, Any]],
    faq_title: str,
    patch: dict[str, Any],
) -> dict[str, Any]:
    out = copy.deepcopy(en_page)
    out.update(patch)
    out["faq"] = faq
    out["faq_title"] = faq_title
    return out
