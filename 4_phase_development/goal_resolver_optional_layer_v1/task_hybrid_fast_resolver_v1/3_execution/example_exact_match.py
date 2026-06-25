#!/usr/bin/env python3
from pathlib import Path
from pxfquery_T033_hybrid_fast_resolver import HybridFastResolver, write_json

out_path = Path(__file__).resolve().parents[1] / "4_artifact/5_table/pxfquery_T033_example_exact.json"
result = HybridFastResolver().resolve("EGFR/A549/xpr", function_desc="Apoptosis").to_dict()
assert result["found"] is True
assert result["hit_level"] == "EXACT"
assert result["used_cell"] == "A549"
assert result["used_perturbation"] == "EGFR"
assert result["activated_terms"]
write_json(out_path, result)
print(out_path)
