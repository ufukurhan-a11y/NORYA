from datetime import datetime

from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    text: str
    doctor_notes: str | None = None  # İsteğe bağlı: doktorunuzun notu / ek bilgi
    lang: str | None = None  # Rapor dili: tr, en, it, es, fr, de, he, ar, hi (yoksa Türkçe)


class AnalyzeResponse(BaseModel):
    sonuc: str
    notu: str = "Norya AI yorumladı."
    analiz_id: int | None = None


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
