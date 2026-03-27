# Norya — prod build with WeasyPrint (PDF) system deps.
# Render: Use this Dockerfile so PDF raporu çalışır (cairo/pango gerekli).
FROM python:3.12-slim

# WeasyPrint için sistem kütüphaneleri (PDF oluşturma)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PORT=8000
EXPOSE $PORT
CMD gunicorn app.main:app -w ${WEB_CONCURRENCY:-1} -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
