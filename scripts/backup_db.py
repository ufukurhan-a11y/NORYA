#!/usr/bin/env python3
"""
SQLite veritabanı için basit yedek alma script'i.

KURALLAR:
- Eski yedekler ASLA silinmez.
- Yedekler `backups/YYYY/MM/` klasörlerine ayrılır.
- Yedek dosya adı: `norya-YYYYMMDD-HHMMSS.db` (benzersiz).

Kullanım:
    python scripts/backup_db.py

Not:
- Varsayılan veritabanı yolu proje kökündeki `norya.db` dosyasıdır.
- İsterseniz `DB_PATH` ortam değişkeni ile farklı bir SQLite dosyası verebilirsiniz.
"""

from __future__ import annotations

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    # Ortam değişkeni ile özelleştirilebilir; yoksa proje kökündeki norya.db kullanılır.
    db_path_str = os.getenv("DB_PATH", str(root / "norya.db"))
    db_path = Path(db_path_str)

    if not db_path.exists():
        print(f"ERROR: Veritabanı bulunamadı: {db_path}", file=sys.stderr)
        return 1

    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    ts = now.strftime("%Y%m%d-%H%M%S")

    backups_root = root / "backups" / year / month
    backups_root.mkdir(parents=True, exist_ok=True)

    target = backups_root / f"norya-{ts}.db"
    tmp_target = target.with_suffix(target.suffix + ".tmp")

    try:
        # Atomic'e yakın kopyalama: önce .tmp'ye yaz, sonra rename.
        shutil.copy2(db_path, tmp_target)
        tmp_target.replace(target)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: Yedek alınamadı: {exc}", file=sys.stderr)
        # Geçici dosya kaldıysa temizle (hepsi silinmeyebilir; önemli olan hata kodu).
        try:
            if tmp_target.exists():
                tmp_target.unlink()
        except Exception:
            pass
        return 1

    print(f"OK: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

