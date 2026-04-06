"""Blog yönetimi router — Jinja2 template + CRUD API."""
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlmodel import Session, select

from app.admin.deps import require_admin_secret_or_cookie
from app.core.database import get_db
from app.core.templating import Jinja2Templates
from app.models import BlogPost

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


# ─────────────────────────────────────────────────────────────────────────────
# HTML sayfası
# ─────────────────────────────────────────────────────────────────────────────

@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def blog_management_page(
    request: Request,
    _: dict = Depends(require_admin_secret_or_cookie),
):
    """Blog yönetim sayfası (HTML)."""
    return templates.TemplateResponse(
        "admin/blog_list.html",
        {"request": request},
    )


# ─────────────────────────────────────────────────────────────────────────────
# Blog API: listeleme
# ─────────────────────────────────────────────────────────────────────────────

@router.get("/api/posts")
async def list_blog_posts(
    _=Depends(require_admin_secret_or_cookie),
    db: Session = Depends(get_db),
    lang: str | None = Query(None),
    is_published: bool | None = Query(None),
    limit: int = Query(100, le=500),
    offset: int = Query(0, ge=0),
) -> JSONResponse:
    """Blog yazıları listesi (JSON)."""
    stmt = select(BlogPost).order_by(BlogPost.created_at.desc()).offset(offset).limit(limit)

    if lang:
        stmt = stmt.where(BlogPost.lang == lang[:2].lower())
    if is_published is not None:
        stmt = stmt.where(BlogPost.is_published == is_published)

    posts = list(db.exec(stmt).all())
    return JSONResponse([
        {
            "id": p.id,
            "slug": p.slug,
            "lang": p.lang,
            "title": p.title,
            "meta_title": p.meta_title,
            "meta_description": p.meta_description,
            "category": p.category,
            "author_name": p.author_name,
            "cover_image": p.cover_image,
            "is_published": p.is_published,
            "is_featured": p.is_featured,
            "published_at": p.published_at.isoformat() if p.published_at else None,
            "updated_at": p.updated_at.isoformat() if p.updated_at else None,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "reading_time_minutes": p.reading_time_minutes,
        }
        for p in posts
    ])


# ─────────────────────────────────────────────────────────────────────────────
# Blog API: tekil blog yazısı
# ─────────────────────────────────────────────────────────────────────────────

@router.get("/api/posts/{post_id}")
async def get_blog_post(
    post_id: int,
    _=Depends(require_admin_secret_or_cookie),
    db: Session = Depends(get_db),
) -> JSONResponse:
    """Tek bir blog yazısını getir."""
    post = db.get(BlogPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog yazısı bulunamadı.")
    return JSONResponse({
        "id": post.id,
        "slug": post.slug,
        "lang": post.lang,
        "title": post.title,
        "meta_title": post.meta_title,
        "meta_description": post.meta_description,
        "content_json": post.content_json,
        "cover_image": post.cover_image,
        "category": post.category,
        "tags_json": post.tags_json,
        "author_name": post.author_name,
        "is_published": post.is_published,
        "is_featured": post.is_featured,
        "published_at": post.published_at.isoformat() if post.published_at else None,
        "updated_at": post.updated_at.isoformat() if post.updated_at else None,
        "created_at": post.created_at.isoformat() if post.created_at else None,
        "reading_time_minutes": post.reading_time_minutes,
        "canonical_url": post.canonical_url,
    })


# ─────────────────────────────────────────────────────────────────────────────
# Blog API: oluştur
# ─────────────────────────────────────────────────────────────────────────────

@router.post("/api/posts", response_class=JSONResponse)
async def create_blog_post(
    body: dict,
    _=Depends(require_admin_secret_or_cookie),
    db: Session = Depends(get_db),
) -> JSONResponse:
    """Yeni blog yazısı oluştur."""
    # Slug kontrolü
    slug = body.get("slug", "").strip()
    existing = db.exec(select(BlogPost).where(BlogPost.slug == slug)).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Slug '{slug}' zaten kullanılıyor.")

    now = datetime.utcnow()
    is_published = body.get("is_published", False)
    post = BlogPost(
        slug=slug,
        lang=(body.get("lang") or "tr")[:2].lower(),
        title=body.get("title", ""),
        meta_title=body.get("meta_title"),
        meta_description=body.get("meta_description"),
        content_json=body.get("content_json", "[]"),
        cover_image=body.get("cover_image"),
        category=body.get("category"),
        tags_json=body.get("tags_json"),
        author_name=body.get("author_name"),
        is_published=is_published,
        is_featured=body.get("is_featured", False),
        published_at=now if is_published else None,
        updated_at=now,
        reading_time_minutes=body.get("reading_time_minutes"),
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return JSONResponse({"ok": True, "id": post.id})


# ─────────────────────────────────────────────────────────────────────────────
# Blog API: güncelle
# ─────────────────────────────────────────────────────────────────────────────

@router.put("/api/posts/{post_id}", response_class=JSONResponse)
async def update_blog_post(
    post_id: int,
    body: dict,
    _=Depends(require_admin_secret_or_cookie),
    db: Session = Depends(get_db),
) -> JSONResponse:
    """Blog yazısını güncelle."""
    post = db.get(BlogPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog yazısı bulunamadı.")

    # Slug değişikliği kontrolü
    new_slug = body.get("slug")
    if new_slug and new_slug != post.slug:
        existing = db.exec(select(BlogPost).where(BlogPost.slug == new_slug)).first()
        if existing:
            raise HTTPException(status_code=400, detail=f"Slug '{new_slug}' zaten kullanılıyor.")
        post.slug = new_slug

    # Alanları güncelle
    if "lang" in body:
        post.lang = body["lang"][:2].lower()
    if "title" in body:
        post.title = body["title"]
    if "meta_title" in body:
        post.meta_title = body["meta_title"]
    if "meta_description" in body:
        post.meta_description = body["meta_description"]
    if "content_json" in body:
        post.content_json = body["content_json"]
    if "cover_image" in body:
        post.cover_image = body["cover_image"]
    if "category" in body:
        post.category = body["category"]
    if "tags_json" in body:
        post.tags_json = body["tags_json"]
    if "author_name" in body:
        post.author_name = body["author_name"]
    if "reading_time_minutes" in body:
        post.reading_time_minutes = body["reading_time_minutes"]

    # Yayın durumu değişikliği
    if "is_published" in body:
        was_published = post.is_published
        post.is_published = body["is_published"]
        if not was_published and post.is_published and not post.published_at:
            post.published_at = datetime.utcnow()

    if "is_featured" in body:
        post.is_featured = body["is_featured"]

    post.updated_at = datetime.utcnow()
    db.add(post)
    db.commit()
    db.refresh(post)
    return JSONResponse({"ok": True})


# ─────────────────────────────────────────────────────────────────────────────
# Blog API: sil
# ─────────────────────────────────────────────────────────────────────────────

@router.delete("/api/posts/{post_id}", response_class=JSONResponse)
async def delete_blog_post(
    post_id: int,
    _=Depends(require_admin_secret_or_cookie),
    db: Session = Depends(get_db),
) -> JSONResponse:
    """Blog yazısını sil."""
    post = db.get(BlogPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog yazısı bulunamadı.")
    db.delete(post)
    db.commit()
    return JSONResponse({"ok": True})


# ─────────────────────────────────────────────────────────────────────────────
# Blog API: yayın toggle
# ─────────────────────────────────────────────────────────────────────────────

@router.post("/api/posts/{post_id}/toggle-publish", response_class=JSONResponse)
async def toggle_publish_blog_post(
    post_id: int,
    _=Depends(require_admin_secret_or_cookie),
    db: Session = Depends(get_db),
) -> JSONResponse:
    """Blog yazısını yayınla / yayından kaldır."""
    post = db.get(BlogPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog yazısı bulunamadı.")

    post.is_published = not post.is_published
    if post.is_published and not post.published_at:
        post.published_at = datetime.utcnow()
    post.updated_at = datetime.utcnow()
    db.add(post)
    db.commit()
    db.refresh(post)
    return JSONResponse({"ok": True, "is_published": post.is_published})
