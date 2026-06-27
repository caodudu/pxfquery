from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import yaml

from pxfquery.parser import parse_query
from pxfquery.resolver import resolve_intent


def query(text: str, *, provider_mode: str = "disabled") -> dict:
    intent = parse_query(text, ai_route_used=provider_mode == "real", fallback_used=provider_mode != "real")
    return resolve_intent(intent, provider_mode=provider_mode)


def parse(text: str, *, provider_mode: str = "disabled") -> dict:
    return parse_query(text, ai_route_used=provider_mode == "real", fallback_used=provider_mode != "real").to_dict()


def load_corpus(path: str | Path) -> list[dict]:
    payload = yaml.safe_load(Path(path).read_text())
    cases = payload.get("cases", [])
    if not isinstance(cases, list):
        raise ValueError("corpus cases must be a list")
    return cases


def run_corpus(corpus_path: str | Path, *, families: Iterable[str] | None = None, provider_mode: str = "disabled") -> list[dict]:
    allowed = set(families or [])
    records: list[dict] = []
    for case in load_corpus(corpus_path):
        if allowed and case.get("family") not in allowed:
            continue
        result = query(case["raw_nl"], provider_mode=_case_provider_mode(case, provider_mode))
        expected_route = _normalize_expected_route(case.get("route"))
        passed = result["route_type"] == expected_route
        records.append(
            {
                "case_id": case.get("case_id"),
                "family": case.get("family"),
                "raw_nl": case.get("raw_nl"),
                "expected_route_type": expected_route,
                "observed_route_type": result["route_type"],
                "passed": passed,
                "intent": result.get("intent"),
                "result": result,
                "diagnostics": result.get("diagnostics"),
            }
        )
    return records


def summarize_records(records: list[dict]) -> dict:
    total = len(records)
    passed = sum(1 for record in records if record.get("passed"))
    families: dict[str, dict[str, int]] = {}
    routes: dict[str, int] = {}
    for record in records:
        family = record.get("family") or "unknown"
        stats = families.setdefault(family, {"total": 0, "passed": 0})
        stats["total"] += 1
        stats["passed"] += 1 if record.get("passed") else 0
        routes[record.get("observed_route_type") or "unknown"] = routes.get(record.get("observed_route_type") or "unknown", 0) + 1
    return {"total": total, "passed": passed, "failed": total - passed, "families": families, "observed_routes": routes}


def write_jsonl(records: list[dict], path: str | Path) -> None:
    with Path(path).open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def _case_provider_mode(case: dict, default_mode: str) -> str:
    expected_intent = case.get("expected_intent") or {}
    mode = expected_intent.get("provider_mode")
    if mode in {"real", "disabled", "fallback"}:
        return mode
    return default_mode


def _normalize_expected_route(route: str | None) -> str | None:
    if route == "fallback":
        return "no-hit"
    if route == "real_provider_or_not_verified":
        return "exact-hit"
    if route == "hard-negative":
        return "context-missing"
    return route
