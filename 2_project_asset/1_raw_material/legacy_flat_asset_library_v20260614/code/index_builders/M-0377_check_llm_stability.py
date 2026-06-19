from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path


def _load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    if str(workspace / "script") not in sys.path:
        sys.path.insert(0, str(workspace / "script"))
    _load_env(workspace / ".env")

    from openai import OpenAI
    from PxFquery.llm.prompts import llm_parse_intent

    client = OpenAI(
        api_key=os.getenv("MINIMAX_API_KEY"),
        base_url=os.getenv("MINIMAX_BASE_URL", "https://api.minimax.chat/v1"),
    )
    model = os.getenv("MINIMAX_MODEL", "MiniMax-M2.7")

    cases = [
        "In A549, what pathways are affected by EGFR knockdown?",
        "In A549, what pathways are affected by an EGFR inhibitor?",
        "For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown?",
    ]
    rounds = 3
    rows = []
    ok = 0
    total = len(cases) * rounds
    for _ in range(rounds):
        for q in cases:
            t0 = time.perf_counter()
            try:
                intent = llm_parse_intent(client, model, q)
                dt = time.perf_counter() - t0
                valid = str(intent.get("query_type") or "").lower() in ("forward", "reverse")
                ok += int(valid)
                rows.append(
                    {
                        "query": q,
                        "ok": valid,
                        "latency_sec": round(dt, 3),
                        "intent": intent,
                    }
                )
            except Exception as e:
                dt = time.perf_counter() - t0
                rows.append(
                    {
                        "query": q,
                        "ok": False,
                        "latency_sec": round(dt, 3),
                        "error": f"{type(e).__name__}: {e}",
                    }
                )

    payload = {
        "time": datetime.now().isoformat(timespec="seconds"),
        "model": model,
        "rounds": rounds,
        "total": total,
        "ok": ok,
        "success_rate": round(ok / max(1, total), 3),
        "rows": rows,
    }
    out_json = workspace / "output/store/resolver_demo/llm_stability_check.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    out_md = workspace / "report/6_llm_resovler_llm_stability_check.md"
    lines = [
        "# LLM Stability Check",
        "",
        f"- Time: {payload['time']}",
        f"- Model: {model}",
        f"- Success Rate: {payload['ok']}/{payload['total']} = {payload['success_rate']}",
        "",
        "```json",
        json.dumps(payload, ensure_ascii=False, indent=2),
        "```",
    ]
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"json: {out_json}")
    print(f"report: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

