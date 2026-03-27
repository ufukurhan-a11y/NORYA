# Render / Heroku uyumlu başlatma (PORT ortam değişkeni ile)
web: gunicorn app.main:app -w ${WEB_CONCURRENCY:-1} -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT:-8000}
