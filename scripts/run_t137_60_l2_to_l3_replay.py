from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path

import pandas as pd

from pxfquery.l3_execution import execute_route_plan
from pxfquery.resources import ResourceManager


ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")
L2_REPORT = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_10_l2_resource_routing_repair/4_artifact/5_table/"
    "t137_60_l2_validation_latest.json"
)
L3_RESOURCES = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_11_l3_resource_pack_query_execution_repair/1_asset/"
    "l3_light_resource_pack"
)
OUT_DIR = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_11_l3_resource_pack_query_execution_repair/4_artifact/5_table"
)


def main() -> None:
    l2_report = Path(os.environ.get("PXFQUERY_L2_REPLAY_REPORT", str(L2_REPORT))).expanduser().resolve()
    report = json.loads(l2_report.read_text(encoding="utf-8"))
    records = report["records"]
    resources = ResourceManager()
    resources.use(L3_RESOURCES, strict=False)
    out_records = []
    for record in records:
        route = record["route"]
        l2_ok = record.get("l2_ok", record.get("ok"))
        execution = execute_route_plan(
            route,
            resources=resources,
            resource_dir=L3_RESOURCES,
            auto_download=False,
            top_n=10,
        ).to_dict()
        executed_routes = execution.get("executed_routes", [])
        skipped_routes = execution.get("skipped_routes", [])
        out_records.append(
            {
                "category": record.get("category"),
                "case_id": record.get("case_id"),
                "query": record.get("query"),
                "l2_ok": l2_ok,
                "l2_route_status": route.get("route_status"),
                "query_type": (route.get("intent") or {}).get("query_type"),
                "l3_execution_status": execution.get("execution_status"),
                "l3_executed_route_count": len(executed_routes),
                "l3_skipped_route_count": len(skipped_routes),
                "l3_error_codes": sorted({e.get("code") for e in execution.get("errors", []) if e.get("code")}),
                "executed_modalities": sorted({r.get("modality") for r in executed_routes if r.get("modality")}),
                "first_error": (execution.get("errors") or [{}])[0],
                "execution": execution,
            }
        )
    summary = {
        "source_l2_report": str(l2_report),
        "l3_resource_dir": str(L3_RESOURCES),
        "total": len(out_records),
        "l2_ok": sum(1 for r in out_records if r["l2_ok"]),
        "l3_executed": sum(1 for r in out_records if r["l3_execution_status"] == "executed"),
        "l3_partial": sum(1 for r in out_records if r["l3_execution_status"] == "partial"),
        "l3_failed": sum(1 for r in out_records if r["l3_execution_status"] not in {"executed", "partial"}),
        "status_counts": dict(Counter(r["l3_execution_status"] for r in out_records)),
        "error_code_counts": dict(Counter(code for r in out_records for code in r["l3_error_codes"])),
    }
    payload = {"summary": summary, "records": out_records}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = l2_report.stem.replace("_l2_validation", "_l2_to_l3_replay")
    json_path = OUT_DIR / f"{stem}.json"
    tsv_path = OUT_DIR / f"{stem}.tsv"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    flat_rows = [{k: v for k, v in row.items() if k != "execution"} for row in out_records]
    pd.DataFrame(flat_rows).to_csv(tsv_path, sep="\t", index=False)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(json_path)
    print(tsv_path)


if __name__ == "__main__":
    main()
