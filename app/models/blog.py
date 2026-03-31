"""Blog post modeli — admin panelinden yönetilebilir blog yazıları."""
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class BlogPost(SQLModel, table=True):
    """Admin panelinden eklenen blog yazıları için model."""
    
    __tablename__ = "blog_posts"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Slug ve dil
    slug: str = Field(unique=True, index=True, description="URL slug (örn: ldh-kan-testi)")
    lang: str = Field(default="tr", index=True, description="Dil kodu: tr, en, de, fr, es, it, he, ar, hi")
    
    # Başlık ve içerik
    title: str = Field(description="Makale başlığı")
    meta_title: Optional[str] = Field(default=None, description="SEO meta title")
    meta_description: Optional[str] = Field(default=None, description="SEO meta description")
    
    # İçerik bölümleri (JSON olarak saklanacak)
    # Her bölüm: {"id": "intro", "level": 2, "heading": "...", "body_html": "..."}
    content_json: str = Field(description="Makale içeriği (JSON array)")
    
    # Kapak görseli
    cover_image: Optional[str] = Field(default=None, description="Kapak görseli yolu (/static/images/blog/...)")
    
    # Kategori ve etiketler
    category: Optional[str] = Field(default=None, index=True, description="Kategori (örn: 'Genel Sağlık', 'Kan Testleri')")
    tags_json: Optional[str] = Field(default=None, description="Etiketler JSON array")
    
    # Yazar ve zaman
    author_name: Optional[str] = Field(default=None, description="Yazar adı")
    published_at: Optional[datetime] = Field(default=None, index=True, description="Yayın tarihi")
    updated_at: Optional[datetime] = Field(default=None, description="Son güncelleme")
    
    # Durum
    is_published: bool = Field(default=False, index=True, description="Yayında mı?")
    is_featured: bool = Field(default=False, description="Öne çıkan mı?")
    
    # SEO
    canonical_url: Optional[str] = Field(default=None, description="Canonical URL")
    
    # Okuma süresi (otomatik hesaplanabilir)
    reading_time_minutes: Optional[int] = Field(default=None, description="Tahmini okuma süresi (dk)")
    
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
