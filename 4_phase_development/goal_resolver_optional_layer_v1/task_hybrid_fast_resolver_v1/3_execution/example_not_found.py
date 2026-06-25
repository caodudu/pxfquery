#!/usr/bin/env python3
from pathlib import Path
from pxfquery_T033_hybrid_fast_resolver import HybridFastResolver, write_json

out_path = Path(__file__).resolve().parents[1] / "4_artifact/5_table/pxfquery_T033_example_not_found.json"
result = HybridFastResolver().resolve("NONSENSE_ZZZ999/UNKNOWN_CELL/xpr").to_dict()
assert result["found"] is False
assert result["hit_level"] == "NOT_FOUND"
assert not result["activated_terms"]
assert not result["suppressed_terms"]
assert "NOT_FOUND" in result["note"]
write_json(out_path, result)
print(out_path)
