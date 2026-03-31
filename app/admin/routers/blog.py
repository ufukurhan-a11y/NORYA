"""Blog yönetimi router — Jinja2 template ile."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from app.admin.deps import require_admin_secret_or_cookie

router = APIRouter()

@router.get("/blog", response_class=HTMLResponse)
async def blog_management_page(
    request: Request,
    _: dict = Depends(require_admin_secret_or_cookie),
):
    """Blog yönetim sayfası."""
    return request.app.state.templates.TemplateResponse(
        "admin/blog_list.html",
        {"request": request},
    )
