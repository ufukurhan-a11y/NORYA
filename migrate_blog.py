#!/usr/bin/env python3
"""Blog tablosunu oluşturur."""
import sys
from pathlib import Path

# Project root'u path'e ekle
root = Path(__file__).resolve().parent
sys.path.insert(0, str(root))

from sqlmodel import SQLModel, create_engine
from app.models.blog import BlogPost
from app.core.config import settings

# Database URL
DATABASE_URL = settings.database_url or "sqlite:///./data/norya.db"

engine = create_engine(DATABASE_URL)

print(f"Database: {DATABASE_URL}")
print("Blog tablosu oluşturuluyor...")

# Sadece BlogPost tablosunu oluştur
SQLModel.metadata.create_all(engine, tables=[BlogPost.__table__])

print("✓ Blog tablosu başarıyla oluşturuldu!")
