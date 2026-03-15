#!/usr/bin/env python3
"""Yerel SQLite veritabanında auditlog tablosuna country ve city sütunlarını ekler.
Kullanım (proje kökünden): python -m scripts.add_auditlog_columns
"""
import sys
from pathlib import Path

# Proje kökünü path'e ekle
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sqlalchemy import inspect, text
from app.core.database import DATABASE_URL, engine


def main():
    if not DATABASE_URL.startswith("sqlite"):
        print("Bu script yalnızca SQLite için. DATABASE_URL:", DATABASE_URL[:50], "...")
        return
    insp = inspect(engine)
    if not insp.has_table("auditlog"):
        print("auditlog tablosu yok; önce uygulamayı bir kez çalıştırın.")
        return
    cols = [c["name"] for c in insp.get_columns("auditlog")]
    for col in ("country", "city"):
        if col in cols:
            print(f"auditlog.{col} zaten var, atlanıyor.")
            continue
        try:
            with engine.connect() as conn:
                conn.execute(text(f"ALTER TABLE auditlog ADD COLUMN {col} TEXT"))
                conn.commit()
            print(f"auditlog.{col} eklendi.")
        except Exception as e:
            print(f"auditlog.{col} eklenirken hata: {e}")
            raise
    print("Bitti. Tekrar kayıt deneyebilirsiniz.")


if __name__ == "__main__":
    main()
