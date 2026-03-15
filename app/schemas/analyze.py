from datetime import datetime

from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    text: str
    doctor_notes: str | None = None  # İsteğe bağlı: doktorunuzun notu / ek bilgi
    lang: str | None = None  # Rapor dili: tr, en, it, es, fr, de, he, ar, hi (yoksa Türkçe)


class HealthScoreSchema(BaseModel):
    score: int  # 0-100
    level: str  # low | mid | high


class UiHintsSchema(BaseModel):
    locked: bool  # True = free/basic, premium alanlar blur + CTA
    report_limited_preview: bool = False  # True = tek analiz/aylık: sadece önizleme + "hepsini görmek için aylık/yıllık alın" kapısı


class PdfInfoSchema(BaseModel):
    template: str  # "premium" | "basic"
    available: bool = True


class AnalyzeResponse(BaseModel):
    sonuc: str
    notu: str = "Norya AI yorumladı."
    analiz_id: int | None = None
    cached: bool | None = None  # True ise yanıt ai_cache'den döndü (OpenAI çağrılmadı)
    premium: bool = False  # premiumPdf: plan in (single, monthly, yearly) → gauge+score+PDF açık; trend sadece monthly/yearly
    risk_summary: dict | None = None  # overall, domains (cardio/metabolic/inflammation/vitamin)
    health_score: HealthScoreSchema | None = None  # score + level
    trend: dict | None = None  # { dates, ldl, glucose, crp } veya null
    ui_hints: UiHintsSchema | None = None  # locked -> blur + Upgrade CTA
    pdf: PdfInfoSchema | None = None  # template: premium|basic, available
    # Paket tipi: "single" | "monthly" | "yearly" — sonuç hangi planla üretildi (feature gating altyapısı; UI değişmez)
    plan_type: str | None = None


class UploadJsonRequest(BaseModel):
    """Dosyayı base64 ile göndermek için (multipart sorunlu tarayıcılar için yedek)."""
    file_base64: str | None = None  # boş/null gelirse endpoint 400 döner
    filename: str = "upload"
    lang: str | None = None


class AnalysisHistoryItem(BaseModel):
    id: int
    input_preview: str
    result_preview: str
    source: str
    created_at: str
    is_favorite: bool = False


class AnalysisDetail(BaseModel):
    id: int
    input_text: str
    result_text: str
    source: str
    created_at: str
    doctor_notes: str | None = None
    is_favorite: bool = False
    plan_type: str | None = None  # "single" | "monthly" | "yearly" — sonuç ekranı modül görünürlüğü için
