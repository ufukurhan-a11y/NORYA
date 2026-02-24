from pypdf import PdfReader
from io import BytesIO


def extract_text_from_pdf(file_content: bytes) -> str:
    """PDF dosyasından metin çıkarır. En fazla ilk 50 sayfa."""
    reader = PdfReader(BytesIO(file_content))
    parts = []
    for i, page in enumerate(reader.pages):
        if i >= 50:
            break
        text = page.extract_text()
        if text:
            parts.append(text.strip())
    return "\n\n".join(parts).strip() or "PDF'den metin çıkarılamadı."
