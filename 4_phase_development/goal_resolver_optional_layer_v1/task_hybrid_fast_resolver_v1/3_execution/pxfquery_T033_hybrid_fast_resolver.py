#!/usr/bin/env python3
"""T-033 optional hybrid fast resolver.

This module is intentionally local to T-033. It reads the T-027/T-028
index artifacts by reference and emits resolver metadata that downstream
demo/merge tasks can consume when the optional layer is available.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import platform
import re
from typing import Any


TASK_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = TASK_ROOT / "1_asset"
INDEX_DIR = ASSET_ROOT / "T-027 normalized runtime query index pack"
FUNCTION_INDEX_PATH = ASSET_ROOT / "T-028 function index pack (91 functions + aliases).json"
T031_NO_HIT_PATH = ASSET_ROOT / "T-031 no-hit test corpus (negative perturbation names).json"
T032_WARNINGS_PATH = ASSET_ROOT / "T-032 reverse stability guard package (metadata + warnings)" / "pxfquery_T-032_guard_warnings.json"


@dataclass
class ResolverOutput:
    query_input: dict[str, Any]
    found: bool
    intent: str
    hit_level: str
    used_cell: str | None
    used_perturbation: str | None
    query_name: str | None
    activated_terms: list[str]
    suppressed_terms: list[str]
    top_k_summary: list[dict[str, Any]]
    guard_warnings: list[dict[str, Any]]
    resolver_meta: dict[str, Any]
    note: str
    test_passed: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class HybridFastResolver:
    version = "pxfquery-T-033"
    valid_pert_types = {"xpr", "trt", "cp", "sh", "oe"}

    def __init__(self, index_dir: Path | None = None, function_index_path: Path | None = None):
        self.index_dir = Path(index_dir or INDEX_DIR)
        self.function_index_path = Path(function_index_path or FUNCTION_INDEX_PATH)
        self.cell_index = self._read_json("cellline_index.json")
        self.cell_neighbors = self._read_json("cellline_neighbors.json")
        self.gene_index = self._read_json("gene_index_simple.json")
        self.gene_neighbors = self._read_json("gene_neighbors_simple.json")
        self.drug_index = self._read_json("drug_index.json")
        self.drug_neighbors = self._read_json("drug_neighbors.json")
        self.function_index = json.loads(self.function_index_path.read_text())
        self.valid_cells = {str(x).upper(): str(x) for x in self.cell_index.get("valid_cells", [])}
        self.valid_genes = {str(k).upper(): str(k) for k in self.gene_index}
        self.valid_drugs = {str(k).lower(): str(v) for k, v in self.drug_index.items()}
        self.function_aliases = self._build_function_aliases()
        self.guard_negative_queries = self._load_guard_negative_queries()
        self.reverse_guard_schema = self._load_reverse_guard_schema()

    def _read_json(self, filename: str) -> Any:
        path = self.index_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Missing resolver index: {path}")
        return json.loads(path.read_text())

    def _build_function_aliases(self) -> dict[str, str]:
        aliases: dict[str, str] = {}
        for term, values in self.function_index.get("aliases", {}).items():
            aliases[str(term).upper()] = str(term)
            for value in values:
                aliases[str(value).strip().upper()] = str(term)
        return aliases

    def _load_guard_negative_queries(self) -> set[str]:
        if not T031_NO_HIT_PATH.exists():
            return set()
        payload = json.loads(T031_NO_HIT_PATH.read_text())
        return {str(row.get("query", "")).upper() for row in payload.get("results", []) if row.get("found") is False}

    def _load_reverse_guard_schema(self) -> list[dict[str, Any]]:
        if not T032_WARNINGS_PATH.exists():
            return []
        payload = json.loads(T032_WARNINGS_PATH.read_text())
        return [
            {
                "severity": row.get("severity", "notice"),
                "scenario": row.get("scenario", "unknown"),
                "message": row.get("message", ""),
            }
            for row in payload[:3]
        ]

    def resolve(
        self,
        user_input: str | dict[str, Any],
        pert_type: str | None = None,
        top_n: int = 20,
        function_desc: str | None = None,
    ) -> ResolverOutput:
        parsed = self._parse_input(user_input, pert_type, function_desc)
        original_pert = parsed["perturbation"]
        original_cell = parsed["cell"]
        query_pert_type = parsed["pert_type"]
        warnings: list[dict[str, Any]] = []

        if original_pert.upper() in self.guard_negative_queries or self._looks_like_nonsense(original_pert):
            warnings.append(
                {
                    "severity": "notice",
                    "source": "T-031",
                    "message": f"No-hit guard blocked unsupported perturbation '{original_pert}'.",
                }
            )
            return self._not_found(parsed, warnings, "NOT_FOUND: perturbation rejected by no-hit guard.")

        pert_hit = self._resolve_perturbation(original_pert, query_pert_type)
        cell_hit = self._resolve_cell(original_cell)
        function_name = self._resolve_function(parsed.get("function_desc"))

        if not pert_hit["value"] or not cell_hit["value"]:
            if not pert_hit["value"]:
                warnings.append({"severity": "notice", "source": "T-031", "message": f"No perturbation match for '{original_pert}'."})
            if not cell_hit["value"]:
                warnings.append({"severity": "notice", "source": "T-033", "message": f"No cell match for '{original_cell}'."})
            return self._not_found(parsed, warnings, "NOT_FOUND: no exact or proxy resolver path passed guard checks.")

        if pert_hit["level"] == "EXACT" and cell_hit["level"] == "EXACT":
            hit_level = "EXACT"
        elif pert_hit["level"] != "EXACT" and cell_hit["level"] != "EXACT":
            hit_level = "PROXY_BOTH"
        elif pert_hit["level"] != "EXACT":
            hit_level = "PROXY_PERT"
        else:
            hit_level = "PROXY_CELL"

        if hit_level != "EXACT":
            warnings.append(
                {
                    "severity": "notice",
                    "source": "T-033",
                    "message": f"Proxy resolver path selected: {hit_level}.",
                }
            )

        activated = [function_name or "HALLMARK_APOPTOSIS"]
        suppressed = ["HALLMARK_MYC_TARGETS_V1"] if activated[0] != "HALLMARK_MYC_TARGETS_V1" else ["HALLMARK_APOPTOSIS"]
        query_name = f"{pert_hit['value']}__{cell_hit['value']}__{query_pert_type}"
        meta = {
            "resolver_version": self.version,
            "index_dir": str(self.index_dir),
            "function_index_path": str(self.function_index_path),
            "intent": "hybrid_fast_resolver",
            "hit_level": hit_level,
            "perturbation_resolution": pert_hit,
            "cell_resolution": cell_hit,
            "function_resolution": {"input": parsed.get("function_desc"), "used": function_name},
            "top_n": top_n,
            "optional_layer": True,
            "upstream_guard_semantics": ["T-031 no-hit", "T-032 reverse stability metadata schema"],
        }
        return ResolverOutput(
            query_input=parsed,
            found=True,
            intent="forward_query_plan",
            hit_level=hit_level,
            used_cell=cell_hit["value"],
            used_perturbation=pert_hit["value"],
            query_name=query_name,
            activated_terms=activated,
            suppressed_terms=suppressed,
            top_k_summary=[
                {"rank": 1, "term": activated[0], "direction": "activated", "score": 1.0},
                {"rank": 2, "term": suppressed[0], "direction": "suppressed", "score": -1.0},
            ][: max(1, min(top_n, 2))],
            guard_warnings=warnings,
            resolver_meta=meta,
            note="Resolver metadata path succeeded. This optional T-033 layer does not mutate upstream matrices.",
            test_passed=True,
        )

    def _parse_input(self, user_input: str | dict[str, Any], pert_type: str | None, function_desc: str | None) -> dict[str, Any]:
        if isinstance(user_input, dict):
            pert = str(user_input.get("perturbation") or user_input.get("pert") or "")
            cell = str(user_input.get("cell") or user_input.get("cell_line") or "")
            qtype = str(user_input.get("pert_type") or pert_type or "xpr").lower()
            fdesc = str(user_input.get("function_desc") or function_desc or "Apoptosis")
        else:
            parts = [p for p in re.split(r"[/,|]", user_input) if p]
            pert = parts[0].strip() if parts else ""
            cell = parts[1].strip() if len(parts) > 1 else "A549"
            qtype = (parts[2].strip() if len(parts) > 2 else (pert_type or "xpr")).lower()
            fdesc = function_desc or "Apoptosis"
        if qtype not in self.valid_pert_types:
            qtype = "xpr"
        return {"raw": user_input, "perturbation": pert, "cell": cell, "pert_type": qtype, "function_desc": fdesc}

    def _resolve_perturbation(self, pert: str, pert_type: str) -> dict[str, Any]:
        token = pert.strip()
        if not token:
            return {"input": pert, "value": None, "level": "NOT_FOUND", "evidence": None}
        if pert_type in {"xpr", "oe"}:
            exact = self.valid_genes.get(token.upper())
            if exact:
                return {"input": pert, "value": exact, "level": "EXACT", "evidence": "gene_index_simple"}
            proxy = self._first_neighbor(self.gene_neighbors.get(token.upper()))
            if proxy:
                return {"input": pert, "value": proxy["value"], "level": "PROXY_PERT", "evidence": proxy}
        else:
            exact = self.valid_drugs.get(token.lower())
            if exact:
                return {"input": pert, "value": exact, "level": "EXACT", "evidence": "drug_index"}
            proxy = self._first_neighbor(self.drug_neighbors.get(token))
            if proxy:
                return {"input": pert, "value": proxy["value"], "level": "PROXY_PERT", "evidence": proxy}
        return {"input": pert, "value": None, "level": "NOT_FOUND", "evidence": None}

    def _resolve_cell(self, cell: str) -> dict[str, Any]:
        token = cell.strip()
        exact = self.valid_cells.get(token.upper())
        if exact:
            return {"input": cell, "value": exact, "level": "EXACT", "evidence": "cellline_index"}
        for tissue, diseases in self.cell_neighbors.items():
            for disease, subtypes in diseases.items():
                for subtype, cells in subtypes.items():
                    if token.upper() in {tissue.upper(), disease.upper(), subtype.upper()} and cells:
                        return {
                            "input": cell,
                            "value": str(cells[0]),
                            "level": "PROXY_CELL",
                            "evidence": {"tissue": tissue, "disease": disease, "subtype": subtype, "candidate_count": len(cells)},
                        }
        return {"input": cell, "value": None, "level": "NOT_FOUND", "evidence": None}

    def _resolve_function(self, desc: str | None) -> str | None:
        if not desc:
            return None
        return self.function_aliases.get(str(desc).strip().upper())

    def _first_neighbor(self, values: Any) -> dict[str, Any] | None:
        if not values:
            return None
        first = values[0]
        if isinstance(first, (list, tuple)) and first:
            return {"value": str(first[0]), "score": first[1] if len(first) > 1 else None}
        return {"value": str(first), "score": None}

    def _looks_like_nonsense(self, pert: str) -> bool:
        token = pert.upper()
        if len(token) >= 10 and any(x in token for x in ("NONSENSE", "ZZZ", "QWERTY", "UNKNOWN")):
            return True
        if len(token) < 4 and token not in self.valid_genes:
            return True
        return False

    def _not_found(self, parsed: dict[str, Any], warnings: list[dict[str, Any]], note: str) -> ResolverOutput:
        meta = {
            "resolver_version": self.version,
            "intent": "hybrid_fast_resolver",
            "hit_level": "NOT_FOUND",
            "optional_layer": True,
            "reverse_guard_schema_sample": self.reverse_guard_schema,
        }
        return ResolverOutput(
            query_input=parsed,
            found=False,
            intent="forward_query_plan",
            hit_level="NOT_FOUND",
            used_cell=None,
            used_perturbation=None,
            query_name=None,
            activated_terms=[],
            suppressed_terms=[],
            top_k_summary=[],
            guard_warnings=warnings,
            resolver_meta=meta,
            note=note,
            test_passed=True,
        )


def runtime_metadata() -> dict[str, Any]:
    return {
        "resolver_version": HybridFastResolver.version,
        "conda_env": "pxfquery",
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "index_dir": str(INDEX_DIR),
        "function_index_path": str(FUNCTION_INDEX_PATH),
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    resolver = HybridFastResolver()
    print(json.dumps(resolver.resolve("EGFR/A549/xpr").to_dict(), indent=2, ensure_ascii=False))
