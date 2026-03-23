"""Jinja2 şablonları: Starlette'nin yeni TemplateResponse(request, name, context) imzasını kullanır.

Projede yaygın olan eski çağrı TemplateResponse(name, context) — context içinde request — hâlâ desteklenir.
Starlette ≥0.37 bu sırayı değiştirdi; eski çağrı yanlışlıkla şablon adı yerine dict geçirip Jinja2 önbellek
hatasına (unhashable dict key) yol açıyordu."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from starlette.requests import Request
from starlette.templating import Jinja2Templates as StarletteJinja2Templates


class Jinja2Templates(StarletteJinja2Templates):
    def TemplateResponse(self, *args: Any, **kwargs: Any):
        # Yeni API: (request, name, context?, ...)
        if args and isinstance(args[0], Request):
            return super().TemplateResponse(*args, **kwargs)
        # Eski API: (name, context) — context Mapping, içinde request
        if len(args) == 2 and isinstance(args[1], Mapping):
            name, context = args[0], args[1]
            request = context.get("request")
            if not isinstance(request, Request):
                raise TypeError(
                    "TemplateResponse(name, context) için context['request'] bir Request olmalı."
                )
            ctx = context if isinstance(context, dict) else dict(context)
            return super().TemplateResponse(request, name, ctx, **kwargs)
        return super().TemplateResponse(*args, **kwargs)
