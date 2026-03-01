"""
MinIO (S3 uyumlu) object storage: PDF raporları yüklenir, presigned URL ile indirme.
"""
import io
from datetime import timedelta

from app.core.config import settings

_MINIO_CLIENT = None


def _minio_client():
    """Lazy MinIO client; None if not configured."""
    global _MINIO_CLIENT
    if _MINIO_CLIENT is not None:
        return _MINIO_CLIENT
    if not (settings.minio_endpoint and settings.minio_access_key and settings.minio_secret_key):
        return None
    try:
        from minio import Minio

        endpoint = (settings.minio_endpoint or "").strip()
        for prefix in ("https://", "http://"):
            if endpoint.startswith(prefix):
                endpoint = endpoint[len(prefix) :]
        _MINIO_CLIENT = Minio(
            endpoint,
            access_key=settings.minio_access_key,
            secret_key=settings.minio_secret_key,
            secure=settings.minio_secure,
        )
        return _MINIO_CLIENT
    except Exception:
        return None


def ensure_bucket(client, bucket: str) -> None:
    """Bucket yoksa oluşturur."""
    try:
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)
    except Exception:
        pass


def upload_report_pdf(
    analysis_id: int,
    pdf_bytes: bytes,
    filename: str,
    presigned_expiry_seconds: int = 3600,
) -> str | None:
    """
    PDF'i MinIO'ya yükler, indirme için presigned URL döner.
    MinIO yapılandırılmamışsa None döner.
    """
    if not settings.minio_use_for_pdf:
        return None
    client = _minio_client()
    if not client:
        return None
    bucket = (settings.minio_bucket or "norya-pdf").strip()
    if not bucket:
        return None
    ensure_bucket(client, bucket)
    object_name = f"reports/{analysis_id}/{filename}"
    data = io.BytesIO(pdf_bytes)
    try:
        client.put_object(
            bucket,
            object_name,
            data,
            length=len(pdf_bytes),
            content_type="application/pdf",
        )
    except Exception:
        return None
    try:
        from minio.helpers import HTTPQueryDict

        disposition = f'attachment; filename="{filename}"'
        url = client.get_presigned_url(
            "GET",
            bucket_name=bucket,
            object_name=object_name,
            expires=timedelta(seconds=presigned_expiry_seconds),
            extra_query_params=HTTPQueryDict(
                {"response-content-disposition": disposition}
            ),
        )
        return url
    except Exception:
        return None
