import json
import sqlite3
from typing import Any, Optional

from app.cache_utils import is_expired, now_iso


def get_conn(db_path: str = "norya.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_cache(conn: sqlite3.Connection) -> None:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS ai_cache (
      cache_key TEXT PRIMARY KEY,
      created_at TEXT NOT NULL,
      expires_at TEXT,
      model TEXT NOT NULL,
      input_summary TEXT NOT NULL,
      response_json TEXT NOT NULL
    );
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_ai_cache_expires ON ai_cache(expires_at);")
    conn.commit()


def cache_get(conn: sqlite3.Connection, cache_key: str) -> Optional[dict[str, Any]]:
    row = conn.execute("SELECT * FROM ai_cache WHERE cache_key = ?", (cache_key,)).fetchone()
    if not row:
        return None
    if is_expired(row["expires_at"]):
        conn.execute("DELETE FROM ai_cache WHERE cache_key = ?", (cache_key,))
        conn.commit()
        return None
    return json.loads(row["response_json"])


def cache_set(
    conn: sqlite3.Connection,
    *,
    cache_key: str,
    created_at: str,
    expires_at: str | None,
    model: str,
    input_summary: dict,
    response_obj: dict,
) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO ai_cache (cache_key, created_at, expires_at, model, input_summary, response_json)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            cache_key,
            created_at,
            expires_at,
            model,
            json.dumps(input_summary, ensure_ascii=False),
            json.dumps(response_obj, ensure_ascii=False),
        ),
    )
    conn.commit()


def purge_expired(conn: sqlite3.Connection) -> int:
    now = now_iso()
    cur = conn.execute(
        "DELETE FROM ai_cache WHERE expires_at IS NOT NULL AND expires_at <= ?",
        (now,),
    )
    conn.commit()
    return cur.rowcount
