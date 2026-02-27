"""
Stability Pack v1 — Logging configuration.
Uvicorn ve app logger seviyeleri; OpenAI hatalarında logger.exception kullanılır (app/services/analyze.py).
"""
import logging
import sys


def setup_logging(
    level: int | str = logging.INFO,
    format_string: str | None = None,
) -> None:
    if format_string is None:
        format_string = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(
        level=level,
        format=format_string,
        stream=sys.stdout,
        force=True,
    )
    # Uvicorn loggers: access ve error seviyelerini uyumlu tut
    for name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        log = logging.getLogger(name)
        if level is not None:
            log.setLevel(level)
    # app loggers
    logging.getLogger("norya").setLevel(level)
    logging.getLogger("app").setLevel(level)
