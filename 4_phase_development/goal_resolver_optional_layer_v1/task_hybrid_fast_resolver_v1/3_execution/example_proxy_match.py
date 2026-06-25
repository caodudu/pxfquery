#!/usr/bin/env python3
from pathlib import Path
from pxfquery_T033_hybrid_fast_resolver import HybridFastResolver, write_json

out_path = Path(__file__).resolve().parents[1] / "4_artifact/5_table/pxfquery_T033_example_proxy.json"
result = HybridFastResolver().resolve("TP53/breast/xpr", function_desc="MYC Targets V1").to_dict()
assert result["found"] is True
assert result["hit_level"] in {"PROXY_PERT", "PROXY_CELL", "PROXY_BOTH"}
assert result["used_cell"]
assert result["used_perturbation"] == "TP53"
assert result["resolver_meta"]["cell_resolution"]["level"] == "PROXY_CELL"
write_json(out_path, result)
print(out_path)
