from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class PxFQueryEvent:
    timestamp: str
    layer: str
    stage: str
    level: str
    message: str
    details: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class EventLog:
    """Small non-secret event logger for stage reports, warnings, and errors."""

    def __init__(self, *, enabled: bool = True, stream=None, style: str = "json") -> None:
        self.enabled = enabled
        self.stream = stream if stream is not None else sys.stderr
        self.style = style
        self.events: list[PxFQueryEvent] = []

    def stage(self, layer: str, stage: str, message: str, **details: Any) -> PxFQueryEvent:
        return self._emit(layer, stage, "stage", message, details)

    def warning(self, layer: str, stage: str, message: str, **details: Any) -> PxFQueryEvent:
        return self._emit(layer, stage, "warning", message, details)

    def error(self, layer: str, stage: str, message: str, **details: Any) -> PxFQueryEvent:
        return self._emit(layer, stage, "error", message, details)

    def to_list(self) -> list[dict[str, Any]]:
        return [event.to_dict() for event in self.events]

    def _emit(
        self,
        layer: str,
        stage: str,
        level: str,
        message: str,
        details: dict[str, Any],
    ) -> PxFQueryEvent:
        event = PxFQueryEvent(
            timestamp=datetime.now(timezone.utc).isoformat(),
            layer=layer,
            stage=stage,
            level=level,
            message=message,
            details=_redact(details),
        )
        self.events.append(event)
        if self.enabled:
            if self.style == "text":
                print(_text_line(event), file=self.stream)
            else:
                print(json.dumps(event.to_dict(), ensure_ascii=False, sort_keys=True), file=self.stream)
        return event


def _redact(value: Any) -> Any:
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if any(token in str(key).lower() for token in ("key", "token", "secret", "authorization", "password")):
                out[key] = "<redacted>"
            else:
                out[key] = _redact(item)
        return out
    if isinstance(value, list):
        return [_redact(item) for item in value]
    return value


def _text_line(event: PxFQueryEvent) -> str:
    stage = _public_stage(event.stage or event.layer)
    prefix = "ERROR" if event.level == "error" else "WARN" if event.level == "warning" else stage
    details = []
    for key, value in event.details.items():
        if value in (None, "", [], {}):
            continue
        details.append(f"{key}={value}")
    suffix = f" | {'; '.join(details)}" if details else ""
    return f"[{prefix}] {event.message}{suffix}"


def _public_stage(stage: str) -> str:
    text = stage.lower()
    if "parse" in text or "intent" in text:
        return "Parsing"
    if "route" in text or "match" in text:
        return "Matching"
    if "matrix" in text or "query" in text:
        return "Matrix"
    if "evidence" in text or "assemble" in text:
        return "Evidence"
    if "answer" in text or "render" in text:
        return "Answer"
    return "Status"
