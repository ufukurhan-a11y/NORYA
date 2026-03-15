from datetime import datetime

from sqlmodel import Field, SQLModel


# Sonuç akışında paket tipi: tek analiz / aylık / yıllık (feature gating için)
# Backward compat: mevcut kayıtlar için varsayılan "single" kullanılır.
PLAN_TYPE_DEFAULT = "single"


class AnalysisRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    input_text: str
    result_text: str
    source: str = "text"  # "text" | "pdf" | "image"
    doctor_notes: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    # Yüklenen orijinal belge (PDF/görsel) — admin panelinde "hastanın gönderdiği" ile rapor yan yana
    original_filename: str | None = None  # örn. "tahlil.pdf"
    original_stored_path: str | None = None  # örn. "42.pdf" (data/uploads/ altında)
    is_favorite: bool = False  # Kullanıcının "favori" veya "doktora göstereceğim" işareti
    # Paket tipi: "single" | "monthly" | "yearly" — analiz hangi ürünle üretildi (sonuç ekranı/PDF feature gating)
    plan_type: str = Field(default=PLAN_TYPE_DEFAULT, max_length=16, index=True)
