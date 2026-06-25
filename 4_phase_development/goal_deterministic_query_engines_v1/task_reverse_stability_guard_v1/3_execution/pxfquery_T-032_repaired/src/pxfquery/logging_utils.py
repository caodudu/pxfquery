"""
logging_utils.py — unified logging setup for PxFquery.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


VERBOSITY_LEVEL_MAP = {
    "quiet": logging.WARNING,
    "normal": logging.INFO,
    "debug": logging.DEBUG,
}


@dataclass
class LoggingSettings:
    verbosity: str = "normal"
    level: Optional[str] = None
    enabled: bool = True
    log_to_file: bool = False
    log_dir: str = "report/04_management/logs"
    file_prefix: str = "pxfquery"
    human_readable: bool = False


class QueryIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if not hasattr(record, "query_id"):
            record.query_id = "-"
        return True


def resolve_log_level(verbosity: str = "normal", level: Optional[str] = None) -> int:
    if level:
        return getattr(logging, str(level).upper(), logging.INFO)
    return VERBOSITY_LEVEL_MAP.get(str(verbosity).lower(), logging.INFO)


def configure_logger(name: str, settings: LoggingSettings) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.propagate = False

    if not settings.enabled:
        logger.disabled = True
        return logger

    logger.disabled = False
    logger.setLevel(resolve_log_level(settings.verbosity, settings.level))
    log_filter = QueryIdFilter()
    if settings.human_readable:
        fmt = "%(asctime)s | %(levelname)s | %(message)s | qid=%(query_id)s"
    else:
        fmt = "%(asctime)s | %(levelname)s | %(name)s | qid=%(query_id)s | %(message)s"
    formatter = logging.Formatter(fmt=fmt, datefmt="%Y-%m-%d %H:%M:%S")

    stream_handler = logging.StreamHandler()
    stream_handler.addFilter(log_filter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if settings.log_to_file:
        Path(settings.log_dir).mkdir(parents=True, exist_ok=True)
        day = datetime.now().strftime("%Y-%m-%d")
        log_path = Path(settings.log_dir) / f"{settings.file_prefix}_{day}.log"
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.addFilter(log_filter)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
