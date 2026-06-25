#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import json
from pxfquery_T033_hybrid_fast_resolver import runtime_metadata, write_json

root = Path(__file__).resolve().parents[1]
example_files = {
    "exact": root / "3_execution/example_exact_match.py",
    "proxy": root / "3_execution/example_proxy_match.py",
    "not_found": root / "3_execution/example_not_found.py",
}
evidence_files = {
    "exact": root / "4_artifact/5_table/pxfquery_T033_example_exact.json",
    "proxy": root / "4_artifact/5_table/pxfquery_T033_example_proxy.json",
    "not_found": root / "4_artifact/5_table/pxfquery_T033_example_not_found.json",
}

results = {}
for name, path in example_files.items():
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    evidence_path = evidence_files[name]
    if not evidence_path.exists():
        raise AssertionError(f"Missing expected evidence: {evidence_path}")
    results[name] = json.loads(evidence_path.read_text())

payload = runtime_metadata()
payload["seed_inputs"] = {
    "exact": "EGFR/A549/xpr",
    "proxy": "TP53/breast/xpr",
    "not_found": "NONSENSE_ZZZ999/UNKNOWN_CELL/xpr",
}
payload["examples"] = {
    name: {
        "found": row["found"],
        "hit_level": row["hit_level"],
        "test_passed": bool(row["test_passed"]),
        "used_cell": row["used_cell"],
        "used_perturbation": row["used_perturbation"],
        "guard_warnings": row["guard_warnings"],
    }
    for name, row in results.items()
}
payload["all_passed"] = all(row["test_passed"] for row in results.values())
write_json(root / "4_artifact/5_table/pxfquery_T033_examples_metadata.json", payload)
print(root / "4_artifact/5_table/pxfquery_T033_examples_metadata.json")
