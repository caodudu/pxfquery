"""smoke_endpoint.py — Reproducible endpoint smoke check for pxfquery-T-034.

Usage:
    python smoke_endpoint.py [--provider deepseek-flash] [--base-url URL] [--model NAME]
                             [--no-traffic] [--strict]

The script NEVER raises on endpoint failure: it always writes a structured
JSON record and exits 0. ``--strict`` is opt-in and only upgrades the exit
code to 2 when the reason is "endpoint_unreachable" (so CI can be configured
to alert without breaking the deterministic pipeline).

This script is intentionally standalone; it does not import any legacy
pxfquery code so it keeps running even when the upstream workspace is broken.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import socket
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

# The script lives under <task>/3_execution/. The T-034 workspace lives under
# <task>/4_artifact/2_persist/workspace/. We scrub competing pxfquery trees
# leaving the conda environment prefix alone, then we put ``src`` first so the
# adapter is importable without an editable install.

TASK_ROOT = HERE.parent
WORKSPACE_SRC = TASK_ROOT / "4_artifact" / "2_persist" / "workspace" / "src"


def _purge_legacy_pxfquery_trees(keep: str) -> None:
    """Drop only directories that look like legacy pxfquery workspaces.

    Important: do NOT match the conda environment path itself even if it
    happens to contain the substring "pxfquery". We restrict the purge to
    project-tree paths (anything whose parent components include
    "task_workspace_package_v1", "pxfquery-T", or ends with "/src" and is
    not the keep path).
    """
    keep_resolved = str(Path(keep).resolve())
    for key in list(sys.modules):
        if key == "pxfquery" or key.startswith("pxfquery."):
            sys.modules.pop(key, None)
    drop_markers = (
        "task_workspace_package_v1",
        "goal_resolver_optional_layer_v1",
        "legacy_flat_asset_library",
    )
    cleaned = []
    for p in sys.path:
        pl = str(p)
        if pl == keep_resolved:
            cleaned.append(p)
            continue
        if any(m in pl for m in drop_markers):
            continue
        cleaned.append(p)
    sys.path[:] = cleaned


_purge_legacy_pxfquery_trees(str(WORKSPACE_SRC))
sys.path.insert(0, str(WORKSPACE_SRC))


def _ts() -> str:
    return _dt.datetime.now().isoformat(timespec="seconds")


def _resolve_output_path(arg: str | None) -> Path:
    if arg:
        return Path(arg).expanduser().resolve()
    dated = _dt.date.today().strftime("%Y%m%d")
    return (TASK_ROOT / "4_artifact" / "2_persist" / f"deepseek_flash_smoke_v{dated}.json").resolve()


def _probe_endpoint(base_url: str, timeout: float) -> dict:
    """Best-effort TCP probe so we can pre-classify 'host unreachable' vs 'auth fail'."""
    from urllib.parse import urlparse
    parsed = urlparse(base_url)
    host = parsed.hostname or "api.deepseek.com"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    sock_t0 = time.monotonic()
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            sock_latency = int((time.monotonic() - sock_t0) * 1000)
            return {
                "tcp_ok": True,
                "tcp_error_type": None,
                "tcp_error_message": None,
                "tcp_latency_ms": sock_latency,
                "tcp_host": host,
                "tcp_port": port,
            }
    except Exception as e:  # pragma: no cover - network errors are environment-specific
        return {
            "tcp_ok": False,
            "tcp_error_type": type(e).__name__,
            "tcp_error_message": str(e),
            "tcp_latency_ms": int((time.monotonic() - sock_t0) * 1000),
            "tcp_host": host,
            "tcp_port": port,
        }


def _build_record(provider: str, base_url: str, model: str, no_traffic: bool) -> dict:
    record = {
        "recorded_at": _ts(),
        "task_id": "T-034",
        "provider": provider,
        "model": model,
        "base_url": base_url,
        "no_traffic": no_traffic,
        "transport": "tcp_probe_then_optional_http",
        "status": None,
        "ok": False,
        "reason": None,
        "error_type": None,
        "error_message": None,
        "reply": None,
        "latency_ms": None,
    }

    tcp = _probe_endpoint(base_url, timeout=3.0)
    record["tcp"] = tcp

    if not tcp["tcp_ok"]:
        record["status"] = "unavailable"
        record["reason"] = "endpoint_unreachable"
        record["error_type"] = tcp["tcp_error_type"]
        record["error_message"] = tcp["tcp_error_message"]
        record["latency_ms"] = tcp["tcp_latency_ms"]
        # Mark the api-key presence so human reviewers can distinguish "no key" vs "no route".
        record["api_key_present"] = bool(
            os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
        )
        return record

    if no_traffic:
        record["status"] = "reachable_no_traffic"
        record["reason"] = "skipped_by_flag"
        record["ok"] = True
        record["latency_ms"] = tcp["tcp_latency_ms"]
        record["api_key_present"] = bool(
            os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
        )
        return record

    # Real chat-completions call. We always catch and convert.
    t0 = time.monotonic()
    try:
        from pxfquery.llm import DeepSeekFlashAdapter  # noqa: WPS433
        adapter = DeepSeekFlashAdapter(base_url=base_url, model=model)
        probe = adapter.health_check()
        record["status"] = "ok" if probe.get("ok") else "unavailable"
        record["ok"] = bool(probe.get("ok"))
        record["reason"] = probe.get("reason") or probe.get("error_type")
        record["error_type"] = probe.get("error_type")
        record["error_message"] = probe.get("error_message")
        record["reply"] = probe.get("reply")
        record["latency_ms"] = probe.get("latency_ms") or int((time.monotonic() - t0) * 1000)
    except Exception as e:  # pragma: no cover - any unexpected bootstrap failure
        record["status"] = "unavailable"
        record["reason"] = "bootstrap_failed"
        record["error_type"] = type(e).__name__
        record["error_message"] = str(e)
        record["latency_ms"] = int((time.monotonic() - t0) * 1000)
    finally:
        record["api_key_present"] = bool(
            os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
        )
    return record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", default="deepseek-flash")
    parser.add_argument("--base-url", default="https://api.deepseek.com/v1")
    parser.add_argument("--model", default="deepseek-v4-flash")
    parser.add_argument("--no-traffic", action="store_true",
                        help="skip the real chat-completions call; only probe TCP.")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero if endpoint_unreachable.")
    parser.add_argument("--out", default=None,
                        help="override the smoke-record output path.")
    args = parser.parse_args(argv)

    record = _build_record(args.provider, args.base_url, args.model, args.no_traffic)
    out_path = _resolve_output_path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[smoke_endpoint] provider={record['provider']} status={record['status']} "
          f"reason={record['reason']} latency_ms={record['latency_ms']}")
    print(f"[smoke_endpoint] wrote {out_path}")

    if args.strict and record["status"] == "unavailable" and record["reason"] == "endpoint_unreachable":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
