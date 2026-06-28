from __future__ import annotations

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from pxfquery.l1_intent import QueryIntent
from pxfquery.l2_routing.combination import route_combinations
from pxfquery.l2_routing.index import CellLineIndex, DrugIndex, FunctionIndex


MAX_CELL_CANDIDATES = 6
MAX_PERTURBATION_PROXIES = 5
MAX_FUZZY_CANDIDATES = 5
MAX_FUNCTION_FORWARD = 5
MAX_REVERSE_INTERPRETATION_SETS = 3
MAX_REVERSE_FUNCTIONS_PER_SET = 3
MAX_PAIR_CHECKS = 25
MAX_SELECTED_ROUTES = 3
MAX_EXPANDED_CELL_CANDIDATES = 25
MAX_EXPANDED_PERTURBATION_PROXIES = 50
MODALITIES = ("cp", "sh", "xpr")


@dataclass
class RoutePlan:
    intent: QueryIntent
    route_status: str
    required_capabilities: list[str]
    reason: str = ""
    resource_status: dict[str, Any] = field(default_factory=dict)
    cell_route: dict[str, Any] = field(default_factory=dict)
    perturbation_route: dict[str, Any] = field(default_factory=dict)
    function_route: dict[str, Any] = field(default_factory=dict)
    combination_route: dict[str, Any] = field(default_factory=dict)
    llm_calls: list[dict[str, Any]] = field(default_factory=list)
    selected_route: dict[str, Any] = field(default_factory=dict)
    rejected_candidates: list[dict[str, Any]] = field(default_factory=list)
    unresolved_dimensions: list[str] = field(default_factory=list)
    handoff_payload: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": "l2-route-plan/v2",
            "query_id": _query_id(self.intent),
            "route_status": self.route_status,
            "required_capabilities": list(self.required_capabilities),
            "reason": self.reason,
            "intent": self.intent.to_dict(),
            "resource_status": dict(self.resource_status),
            "cell_route": dict(self.cell_route),
            "perturbation_route": dict(self.perturbation_route),
            "function_route": dict(self.function_route),
            "combination_route": dict(self.combination_route),
            "llm_calls": list(self.llm_calls),
            "selected_route": dict(self.selected_route),
            "rejected_candidates": list(self.rejected_candidates),
            "unresolved_dimensions": list(self.unresolved_dimensions),
            "handoff_payload": dict(self.handoff_payload),
        }


@dataclass
class ResourcePaths:
    root: Path | None = None
    cellline_index: Path | None = None
    cellline_neighbors: Path | None = None
    cellline_tree: Path | None = None
    drug_index: Path | None = None
    drug_neighbors: Path | None = None
    gene_index: Path | None = None
    gene_index_simple: Path | None = None
    gene_neighbors: Path | None = None
    gene_neighbors_simple: Path | None = None
    function_index: Path | None = None
    cp_obs: Path | None = None
    sh_obs: Path | None = None
    xpr_obs: Path | None = None

    def status(self) -> dict[str, Any]:
        paths = {
            "cellline_index": self.cellline_index,
            "cellline_neighbors": self.cellline_neighbors,
            "cellline_tree": self.cellline_tree,
            "drug_index": self.drug_index,
            "drug_neighbors": self.drug_neighbors,
            "gene_index": self.gene_index,
            "gene_index_simple": self.gene_index_simple,
            "gene_neighbors": self.gene_neighbors,
            "gene_neighbors_simple": self.gene_neighbors_simple,
            "function_index": self.function_index,
            "cp_obs": self.cp_obs,
            "sh_obs": self.sh_obs,
            "xpr_obs": self.xpr_obs,
        }
        return {
            "root": str(self.root) if self.root else None,
            "available": {key: str(path) for key, path in paths.items() if path and path.exists()},
            "missing": [key for key, path in paths.items() if path is None or not path.exists()],
        }


def route_intent(
    intent: QueryIntent,
    *,
    assets: Any | None = None,
    index_dir: str | Path | None = None,
    llm_provider: Any | None = None,
    forward_engines: dict[str, Any] | None = None,
    reverse_engines: dict[str, Any] | None = None,
    pair_policy: str = "observed",
) -> RoutePlan:
    base_status = classify_route(intent)
    if base_status == "needs-intent-completion":
        return RoutePlan(
            intent=intent,
            route_status=base_status,
            required_capabilities=_required_capabilities(intent),
            reason=_route_reason(intent, base_status),
        )

    resources = _resolve_resource_paths(assets=assets, index_dir=index_dir)
    resource_status = resources.status()
    if not resource_status["available"]:
        return RoutePlan(
            intent=intent,
            route_status="resource-missing",
            required_capabilities=_required_capabilities(intent),
            reason="no L2 resource indexes are registered; call pxf.resources.use(...) or pxf.resources.use_manifest(...)",
            resource_status=resource_status,
        )

    cell_route, cell_calls, perturbation_route, perturbation_calls, function_route, function_calls = _route_dimensions_parallel(
        intent,
        resources,
        llm_provider,
    )
    llm_calls: list[dict[str, Any]] = [*cell_calls, *perturbation_calls, *function_calls]
    combination_route = route_combinations(
        intent,
        cell_route,
        perturbation_route,
        function_route,
        forward_engines=forward_engines,
        reverse_engines=reverse_engines,
        resources=resources,
        pair_policy=pair_policy,
    )
    status = _combine_status(cell_route, perturbation_route, function_route, combination_route, llm_calls)
    selected_route = _selected_route(intent, cell_route, perturbation_route, function_route, combination_route)
    rejected_candidates = _rejected_candidates(cell_route, perturbation_route, function_route, combination_route)
    unresolved_dimensions = _unresolved_dimensions(cell_route, perturbation_route, function_route, combination_route, llm_calls)
    handoff_payload = _handoff_payload(intent, selected_route, cell_route, perturbation_route, function_route, combination_route)

    return RoutePlan(
        intent=intent,
        route_status=status,
        required_capabilities=_required_capabilities(intent),
        reason=_route_reason(intent, status),
        resource_status=resource_status,
        cell_route=cell_route,
        perturbation_route=perturbation_route,
        function_route=function_route,
        combination_route=combination_route,
        llm_calls=llm_calls,
        selected_route=selected_route,
        rejected_candidates=rejected_candidates,
        unresolved_dimensions=unresolved_dimensions,
        handoff_payload=handoff_payload,
    )


def _route_dimensions_parallel(
    intent: QueryIntent,
    resources: ResourcePaths,
    llm_provider: Any | None,
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any], list[dict[str, Any]], dict[str, Any], list[dict[str, Any]]]:
    def run_cell() -> tuple[dict[str, Any], list[dict[str, Any]]]:
        calls: list[dict[str, Any]] = []
        return _route_cell(intent, resources, calls, llm_provider), calls

    def run_perturbation() -> tuple[dict[str, Any], list[dict[str, Any]]]:
        calls: list[dict[str, Any]] = []
        return _route_perturbation(intent, resources, calls, llm_provider), calls

    def run_function() -> tuple[dict[str, Any], list[dict[str, Any]]]:
        calls: list[dict[str, Any]] = []
        return _route_functions(intent, resources, calls, llm_provider), calls

    with ThreadPoolExecutor(max_workers=3) as executor:
        cell_future = executor.submit(run_cell)
        perturbation_future = executor.submit(run_perturbation)
        function_future = executor.submit(run_function)
        cell_route, cell_calls = cell_future.result()
        perturbation_route, perturbation_calls = perturbation_future.result()
        function_route, function_calls = function_future.result()
    return cell_route, cell_calls, perturbation_route, perturbation_calls, function_route, function_calls


def classify_route(intent: QueryIntent) -> str:
    if intent.missing_fields:
        return "needs-intent-completion"
    if intent.query_type == "forward" and not intent.pert_desc:
        return "needs-intent-completion"
    if intent.query_type == "reverse" and not (intent.function_desc or intent.activate or intent.suppress or intent.pert_desc or intent.raw_query):
        return "needs-intent-completion"
    return "requires-resource-routing"


def _resolve_resource_paths(*, assets: Any | None, index_dir: str | Path | None) -> ResourcePaths:
    paths = ResourcePaths()
    if index_dir is not None:
        paths.root = Path(index_dir).expanduser().resolve()
    if assets is not None:
        for attr, key in {
            "cellline_index": "index.cellline_index",
            "cellline_neighbors": "index.cellline_neighbors",
            "cellline_tree": "index.cellline_tree",
            "drug_index": "index.drug_index",
            "drug_neighbors": "index.drug_neighbors",
            "gene_index": "index.gene_index",
            "gene_index_simple": "index.gene_index_simple",
            "gene_neighbors": "index.gene_neighbors",
            "gene_neighbors_simple": "index.gene_neighbors_simple",
            "function_index": "index.function_index",
        }.items():
            try:
                ref = assets.get(key)
            except KeyError:
                continue
            if ref.exists:
                setattr(paths, attr, Path(ref.path))
        for attr, keys in {
            "cp_obs": ("l3_functional_scores.cp.obs", "matrix.cp_obs_min", "metadata.cp_obs_min"),
            "sh_obs": ("l3_functional_scores.sh.obs", "matrix.sh_obs_min", "metadata.sh_obs_min"),
            "xpr_obs": ("l3_functional_scores.xpr.obs", "matrix.xpr_obs_min", "metadata.xpr_obs_min"),
        }.items():
            for key in keys:
                try:
                    ref = assets.get(key)
                except KeyError:
                    continue
                if ref.exists:
                    setattr(paths, attr, Path(ref.path))
                    break
    if paths.root is not None:
        for attr, filename in {
            "cellline_index": "cellline_index.json",
            "cellline_neighbors": "cellline_neighbors.json",
            "cellline_tree": "cellline_tree.json",
            "drug_index": "drug_index.json",
            "drug_neighbors": "drug_neighbors.json",
            "gene_index": "gene_index.json",
            "gene_index_simple": "gene_index_simple.json",
            "gene_neighbors": "gene_neighbors.json",
            "gene_neighbors_simple": "gene_neighbors_simple.json",
            "function_index": "function_index.json",
        }.items():
            if getattr(paths, attr) is None:
                setattr(paths, attr, paths.root / filename)
        for modality in MODALITIES:
            attr = f"{modality}_obs"
            if getattr(paths, attr) is None:
                setattr(paths, attr, _find_resource(paths.root, [f"{modality}_obs_min.parquet", f"{modality}_obs_min.csv"]))
    return paths


def _route_cell(
    intent: QueryIntent,
    resources: ResourcePaths,
    llm_calls: list[dict[str, Any]],
    llm_provider: Any | None,
) -> dict[str, Any]:
    if not intent.bio_context:
        return {"status": "not-requested", "selected": [], "candidates": []}
    if not (resources.cellline_index and resources.cellline_neighbors and resources.cellline_index.exists() and resources.cellline_neighbors.exists()):
        return {"status": "resource-missing", "reason": "cellline_index.json or cellline_neighbors.json is missing", "selected": [], "candidates": []}

    cell_index = CellLineIndex(resources.cellline_index, resources.cellline_neighbors)
    tree_data = _load_json(resources.cellline_tree) if resources.cellline_tree and resources.cellline_tree.exists() else {}
    alias_hit = _cell_alias_lookup(intent.bio_context, tree_data) or cell_index.canonical(intent.bio_context)
    if alias_hit and cell_index.is_valid(alias_hit):
        proxies = cell_index.proxy_cells_for(alias_hit)
        candidates = [{"cell": alias_hit, "role": "exact", "rank": 1}]
        candidates.extend(_limited_cell_proxies(proxies, start_rank=2))
        expanded_candidates = [{"cell": alias_hit, "role": "exact", "rank": 1, "cell_expansion_scope": "exact", "cell_route_distance": 0}]
        expanded_candidates.extend(_expanded_cell_proxies(proxies, start_rank=2))
        return {
            "status": "resolved",
            "mode": "exact-cell-with-lineage-proxies",
            "selected": [alias_hit],
            "candidates": candidates[:MAX_CELL_CANDIDATES],
            "expanded_candidates": expanded_candidates[:MAX_EXPANDED_CELL_CANDIDATES],
            "lineage_path": cell_index.get_cell_path(alias_hit),
            "limits": {"max_candidates": MAX_CELL_CANDIDATES, "max_expanded_candidates": MAX_EXPANDED_CELL_CANDIDATES},
        }

    if llm_provider is not None and tree_data.get("tree"):
        llm_route = _llm_route_cell(intent.bio_context, tree_data, cell_index, llm_provider)
        llm_calls.extend(llm_route.pop("llm_calls"))
        return llm_route

    llm_calls.append(
        {
            "stage": "cell_tree_selection",
            "status": "required",
            "reason": "non-exact biological context must be mapped through the cell lineage tree by LLM, not by local string rules",
        }
    )
    return {
        "status": "llm-required",
        "mode": "tree-selection-required",
        "selected": [],
        "candidates": [],
        "input": intent.bio_context,
        "limits": {"max_candidates": MAX_CELL_CANDIDATES},
    }


def _route_perturbation(
    intent: QueryIntent,
    resources: ResourcePaths,
    llm_calls: list[dict[str, Any]],
    llm_provider: Any | None,
) -> dict[str, Any]:
    if intent.query_type != "forward" or not intent.pert_desc:
        return {"status": "not-requested", "selected": [], "proxies": []}
    if intent.pert_class == "drug":
        return _route_drug(intent.pert_desc, resources, llm_calls, llm_provider)
    if intent.pert_class == "genetic":
        return _route_gene(intent.pert_desc, resources, llm_calls, llm_provider)
    return {
        "status": "llm-required",
        "mode": "perturbation-class-required",
        "selected": [],
        "proxies": [],
        "input": intent.pert_desc,
    }


def _route_drug(
    term: str,
    resources: ResourcePaths,
    llm_calls: list[dict[str, Any]],
    llm_provider: Any | None,
) -> dict[str, Any]:
    if not (resources.drug_index and resources.drug_neighbors and resources.drug_index.exists() and resources.drug_neighbors.exists()):
        return {"status": "resource-missing", "reason": "drug_index.json or drug_neighbors.json is missing", "selected": [], "proxies": []}
    drug_index = DrugIndex(resources.drug_index, resources.drug_neighbors)
    brd_id = _lookup_drug(term, drug_index)
    if brd_id:
        expanded_neighbors = drug_index.neighbors(brd_id, top_n=MAX_EXPANDED_PERTURBATION_PROXIES)
        return {
            "status": "resolved",
            "entity_type": "drug",
            "mode": "exact-drug-alias",
            "input": term,
            "selected": [{"id": brd_id, "role": "exact", "rank": 1}],
            "proxies": [
                {"id": neighbor, "similarity": score, "role": "structural-proxy", "rank": i + 1}
                for i, (neighbor, score) in enumerate(expanded_neighbors[:MAX_PERTURBATION_PROXIES])
            ],
            "expanded_proxies": [
                {"id": neighbor, "similarity": score, "role": "structural-proxy", "rank": i + 1}
                for i, (neighbor, score) in enumerate(expanded_neighbors)
            ],
            "limits": {"max_proxies": MAX_PERTURBATION_PROXIES, "max_expanded_proxies": MAX_EXPANDED_PERTURBATION_PROXIES},
        }
    aliases = _json_keys(resources.drug_index)
    candidates = _fuzzy_candidates(term, aliases, MAX_FUZZY_CANDIDATES)
    if llm_provider is not None:
        llm_route = _llm_route_drug(term, candidates, aliases, drug_index, llm_provider)
        llm_calls.extend(llm_route.pop("llm_calls"))
        return llm_route
    llm_calls.append(
        {
            "stage": "drug_normalization",
            "status": "required",
            "reason": "non-exact drug names need LLM normalization against retrieved candidate aliases",
            "candidate_count": len(candidates),
        }
    )
    return {
        "status": "llm-required",
        "entity_type": "drug",
        "mode": "candidate-retrieval-only",
        "input": term,
        "selected": [],
        "retrieved_candidates": candidates,
        "proxies": [],
    }


def _route_gene(
    term: str,
    resources: ResourcePaths,
    llm_calls: list[dict[str, Any]],
    llm_provider: Any | None,
) -> dict[str, Any]:
    if not (resources.gene_index and resources.gene_neighbors and resources.gene_index.exists() and resources.gene_neighbors.exists()):
        return {"status": "resource-missing", "reason": "gene_index.json or gene_neighbors.json is missing", "selected": [], "proxies": []}
    gene_index = _load_json(resources.gene_index)
    gene_neighbors = _load_json(resources.gene_neighbors)
    simple_index = _load_json(resources.gene_index_simple) if resources.gene_index_simple and resources.gene_index_simple.exists() else {}
    hit = _lookup_full_gene(term, gene_index) or _lookup_simple_gene(term, simple_index)
    if hit:
        symbol = hit["symbol"]
        expanded_neighbors = _gene_neighbors(symbol, gene_neighbors, top_n=MAX_EXPANDED_PERTURBATION_PROXIES)
        neighbors = expanded_neighbors[:MAX_PERTURBATION_PROXIES]
        proxy_role = "semantic-proxy" if not hit["in_matrix"] else "supporting-semantic-neighbor"
        return {
            "status": "resolved" if hit["in_matrix"] or neighbors else "unresolved",
            "entity_type": "gene",
            "mode": "exact-gene-symbol",
            "input": term,
            "selected": [{"symbol": symbol, "gene_type": hit["gene_type"], "in_matrix": hit["in_matrix"], "role": "exact", "rank": 1}],
            "proxies": [
                {"symbol": neighbor, "similarity": score, "role": proxy_role, "rank": i + 1}
                for i, (neighbor, score) in enumerate(neighbors)
            ],
            "expanded_proxies": [
                {"symbol": neighbor, "similarity": score, "role": proxy_role, "rank": i + 1}
                for i, (neighbor, score) in enumerate(expanded_neighbors)
            ],
            "noncoding_supported": hit["gene_type"] != "protein_coding",
            "limits": {"max_proxies": MAX_PERTURBATION_PROXIES, "max_expanded_proxies": MAX_EXPANDED_PERTURBATION_PROXIES},
        }
    symbols = [v.get("symbol", k) for k, v in gene_index.items()]
    candidates = _fuzzy_candidates(term, symbols, MAX_FUZZY_CANDIDATES)
    if llm_provider is not None:
        llm_route = _llm_route_gene(term, candidates, symbols, gene_index, gene_neighbors, llm_provider)
        llm_calls.extend(llm_route.pop("llm_calls"))
        return llm_route
    llm_calls.append(
        {
            "stage": "gene_normalization",
            "status": "required",
            "reason": "non-exact gene names need LLM normalization against retrieved candidate symbols",
            "candidate_count": len(candidates),
        }
    )
    return {
        "status": "llm-required",
        "entity_type": "gene",
        "mode": "candidate-retrieval-only",
        "input": term,
        "selected": [],
        "retrieved_candidates": candidates,
        "proxies": [],
    }


def _route_functions(
    intent: QueryIntent,
    resources: ResourcePaths,
    llm_calls: list[dict[str, Any]],
    llm_provider: Any | None,
) -> dict[str, Any]:
    operation_terms = _forward_operation_terms(intent)
    if operation_terms:
        return {
            "status": "resolved",
            "mode": "forward-operation-no-function-filter",
            "selected": [],
            "interpretation_sets": [],
            "scope_terms": operation_terms,
            "scope_policy": "forward query terms describe perturbation operation or requested output breadth, not a fixed function-index filter",
            "ambiguity_level": "broad",
            "broad_function_route": True,
            "limits": {
                "forward_max_functions": MAX_FUNCTION_FORWARD,
                "reverse_interpretation_sets": MAX_REVERSE_INTERPRETATION_SETS,
                "reverse_functions_per_set": MAX_REVERSE_FUNCTIONS_PER_SET,
            },
        }
    terms = _function_terms(intent)
    if not terms and intent.query_type == "reverse" and llm_provider is not None and intent.raw_query:
        extracted, calls = _llm_extract_reverse_function_terms(intent, llm_provider)
        llm_calls.extend(calls)
        terms = extracted
    if not terms:
        return {"status": "not-requested", "selected": [], "interpretation_sets": []}
    if not (resources.function_index and resources.function_index.exists()):
        return {"status": "resource-missing", "reason": "function_index.json is missing", "selected": [], "interpretation_sets": []}
    function_index = FunctionIndex(resources.function_index)
    selected: list[dict[str, Any]] = []
    unresolved: list[str] = []
    for direction, term in terms:
        var_name = function_index.lookup(term)
        if var_name:
            selected.append(
                {
                    "var_name": var_name,
                    "label": function_index.label(var_name),
                    "source": function_index.source(var_name),
                    "direction": direction,
                    "input": term,
                    "rank": len(selected) + 1,
                }
            )
        else:
            unresolved.append(term)

    if unresolved and intent.query_type == "forward" and not selected and _is_forward_scope_only_terms(unresolved):
        return {
            "status": "resolved",
            "mode": "forward-result-scope-no-function-filter",
            "selected": [],
            "unresolved_terms": [],
            "scope_terms": list(unresolved),
            "scope_policy": "forward query asks for broad functional outputs, so L2 does not force a fixed function-index filter",
            "ambiguity_level": "broad",
            "broad_function_route": True,
            "limits": {
                "forward_max_functions": MAX_FUNCTION_FORWARD,
                "reverse_interpretation_sets": MAX_REVERSE_INTERPRETATION_SETS,
                "reverse_functions_per_set": MAX_REVERSE_FUNCTIONS_PER_SET,
            },
        }
    if unresolved and llm_provider is not None:
        llm_route = _llm_route_functions(intent, selected, unresolved, function_index, llm_provider)
        llm_calls.extend(llm_route.pop("llm_calls"))
        return llm_route
    if unresolved:
        llm_calls.append(
            {
                "stage": "function_mapping",
                "status": "required",
                "reason": "ambiguous function descriptions must be selected from the fixed 91-function index by LLM",
                "unresolved_terms": unresolved,
            }
        )

    selected = selected[:MAX_FUNCTION_FORWARD]
    route = {
        "status": "resolved" if selected and not unresolved else ("llm-required" if unresolved else "unresolved"),
        "mode": "exact-function-alias" if selected and not unresolved else "partial-exact-needs-llm",
        "selected": selected,
        "unresolved_terms": unresolved,
        "ambiguity_level": _function_ambiguity_level(intent, selected),
        "broad_function_route": len(selected) >= MAX_FUNCTION_FORWARD,
        "limits": {
            "forward_max_functions": MAX_FUNCTION_FORWARD,
            "reverse_interpretation_sets": MAX_REVERSE_INTERPRETATION_SETS,
            "reverse_functions_per_set": MAX_REVERSE_FUNCTIONS_PER_SET,
        },
    }
    if intent.query_type == "reverse":
        if unresolved:
            route["interpretation_sets"] = []
            route["reverse_mapping_policy"] = "run 3 independent LLM mappings, each validated against the fixed 91-function index"
        else:
            route["interpretation_sets"] = [
                {"set_id": "exact", "status": "resolved-without-llm", "functions": selected[:MAX_REVERSE_FUNCTIONS_PER_SET]}
            ]
    return route


def _llm_route_cell(
    bio_context: str,
    tree_data: dict[str, Any],
    cell_index: CellLineIndex,
    llm_provider: Any,
) -> dict[str, Any]:
    node = tree_data["tree"]
    llm_calls: list[dict[str, Any]] = []
    path: list[str] = []
    for level in ["lineage", "disease", "subtype"]:
        if not isinstance(node, dict) or not node:
            break
        options = list(node.keys())
        selected, call = _llm_choose_option(
            llm_provider,
            stage=f"cell_tree_{level}",
            user_text=bio_context,
            level=level,
            options=options,
        )
        llm_calls.append(call)
        if selected not in node:
            return {
                "status": "llm-required",
                "mode": "tree-selection-failed-validation",
                "selected": [],
                "candidates": [],
                "input": bio_context,
                "llm_calls": llm_calls,
                "limits": {"max_candidates": MAX_CELL_CANDIDATES},
            }
        path.append(selected)
        node = node[selected]
    cells = [c for c in node if cell_index.is_valid(c)] if isinstance(node, list) else []
    candidates = [{"cell": c, "role": "llm-tree-leaf", "rank": i + 1} for i, c in enumerate(cells[:MAX_CELL_CANDIDATES])]
    expanded_candidates = _expanded_tree_cells(cells, cell_index)
    return {
        "status": "resolved" if candidates else "unresolved",
        "mode": "llm-cell-tree-selection",
        "selected": [candidates[0]["cell"]] if candidates else [],
        "candidates": candidates,
        "expanded_candidates": expanded_candidates,
        "input": bio_context,
        "lineage_path": tuple(path),
        "llm_calls": llm_calls,
        "limits": {"max_candidates": MAX_CELL_CANDIDATES, "max_expanded_candidates": MAX_EXPANDED_CELL_CANDIDATES},
    }


def _llm_route_drug(
    term: str,
    candidates: list[dict[str, Any]],
    aliases: list[str],
    drug_index: DrugIndex,
    llm_provider: Any,
) -> dict[str, Any]:
    mechanism_class = _is_mechanism_class_drug_query(term)
    payload, evidence = _llm_json(
        llm_provider,
        stage="drug_normalization",
        system_prompt=(
            "You are PxFquery L2 drug normalization. Return one JSON object. "
            "Choose selected_alias only from candidate_aliases if one matches the user drug. "
            "If none is good, return selected_alias=null and up to five hypothesis_names. "
            "If the user input is a mechanism class rather than a named compound, hypothesize concrete representative compound names instead of generic class labels. "
            "Do not invent evidence or IDs."
        ),
        user_payload={"user_drug": term, "input_is_mechanism_class": mechanism_class, "candidate_aliases": [c["value"] for c in candidates]},
    )
    selected_alias = payload.get("selected_alias") if isinstance(payload, dict) else None
    brd_id = drug_index.lookup(selected_alias) if isinstance(selected_alias, str) else None
    hypothesis_names = payload.get("hypothesis_names", []) if isinstance(payload, dict) else []
    if brd_id is None and isinstance(hypothesis_names, list):
        brd_id = drug_index.lookup_aliases([str(x) for x in hypothesis_names])
        selected_alias = next((str(x) for x in hypothesis_names if drug_index.lookup(str(x)) == brd_id), None)
    if brd_id is None and isinstance(hypothesis_names, list):
        for hypothesis in hypothesis_names[:5]:
            fuzzy = _fuzzy_candidates(str(hypothesis), aliases, 1)
            if fuzzy:
                candidate_alias = fuzzy[0]["value"]
                candidate_id = drug_index.lookup(candidate_alias)
                if candidate_id:
                    selected_alias = candidate_alias
                    brd_id = candidate_id
                    break
    call = _llm_call_record("drug_normalization", "ok" if brd_id else "failed", evidence, payload)
    if not brd_id:
        return {
            "status": "llm-required",
            "entity_type": "drug",
            "mode": "llm-normalization-failed-validation",
            "input": term,
            "selected": [],
            "retrieved_candidates": candidates,
            "input_is_mechanism_class": mechanism_class,
            "proxies": [],
            "llm_calls": [call],
        }
    role = "mechanism-class-proxy" if mechanism_class else "llm-normalized"
    expanded_neighbors = drug_index.neighbors(brd_id, top_n=MAX_EXPANDED_PERTURBATION_PROXIES)
    return {
        "status": "resolved",
        "entity_type": "drug",
        "mode": "llm-normalized-drug",
        "input": term,
        "selected": [{"id": brd_id, "alias": selected_alias, "role": role, "rank": 1}],
        "retrieved_candidates": candidates,
        "input_is_mechanism_class": mechanism_class,
        "proxies": [
            {"id": neighbor, "similarity": score, "role": "structural-proxy", "rank": i + 1}
            for i, (neighbor, score) in enumerate(expanded_neighbors[:MAX_PERTURBATION_PROXIES])
        ],
        "expanded_proxies": [
            {"id": neighbor, "similarity": score, "role": "structural-proxy", "rank": i + 1}
            for i, (neighbor, score) in enumerate(expanded_neighbors)
        ],
        "llm_calls": [call],
        "limits": {"max_proxies": MAX_PERTURBATION_PROXIES, "max_expanded_proxies": MAX_EXPANDED_PERTURBATION_PROXIES},
    }


def _llm_route_gene(
    term: str,
    candidates: list[dict[str, Any]],
    symbols: list[str],
    gene_index: dict[str, Any],
    gene_neighbors: dict[str, Any],
    llm_provider: Any,
) -> dict[str, Any]:
    payload, evidence = _llm_json(
        llm_provider,
        stage="gene_normalization",
        system_prompt=(
            "You are PxFquery L2 gene normalization. Return one JSON object. "
            "Choose selected_symbol only from candidate_symbols if one matches the user gene. "
            "If none is good, return selected_symbol=null and up to five hypothesis_symbols. "
            "Use official gene symbols when hypothesizing. Do not answer biology."
        ),
        user_payload={"user_gene": term, "candidate_symbols": [c["value"] for c in candidates]},
    )
    selected_symbol = payload.get("selected_symbol") if isinstance(payload, dict) else None
    hit = _lookup_full_gene(selected_symbol, gene_index) if isinstance(selected_symbol, str) else None
    hypotheses = payload.get("hypothesis_symbols", []) if isinstance(payload, dict) else []
    if hit is None and isinstance(hypotheses, list):
        for hypothesis in hypotheses[:5]:
            hit = _lookup_full_gene(str(hypothesis), gene_index)
            if hit:
                selected_symbol = hit["symbol"]
                break
    if hit is None and isinstance(hypotheses, list):
        for hypothesis in hypotheses[:5]:
            fuzzy = _fuzzy_candidates(str(hypothesis), symbols, 1)
            if fuzzy:
                hit = _lookup_full_gene(fuzzy[0]["value"], gene_index)
                if hit:
                    selected_symbol = hit["symbol"]
                    break
    call = _llm_call_record("gene_normalization", "ok" if hit else "failed", evidence, payload)
    if hit is None:
        return {
            "status": "llm-required",
            "entity_type": "gene",
            "mode": "llm-normalization-failed-validation",
            "input": term,
            "selected": [],
            "retrieved_candidates": candidates,
            "proxies": [],
            "llm_calls": [call],
        }
    expanded_neighbors = _gene_neighbors(hit["symbol"], gene_neighbors, top_n=MAX_EXPANDED_PERTURBATION_PROXIES)
    neighbors = expanded_neighbors[:MAX_PERTURBATION_PROXIES]
    proxy_role = "semantic-proxy" if not hit["in_matrix"] else "supporting-semantic-neighbor"
    return {
        "status": "resolved" if hit["in_matrix"] or neighbors else "unresolved",
        "entity_type": "gene",
        "mode": "llm-normalized-gene",
        "input": term,
        "selected": [{"symbol": hit["symbol"], "gene_type": hit["gene_type"], "in_matrix": hit["in_matrix"], "role": "llm-normalized", "rank": 1}],
        "retrieved_candidates": candidates,
        "proxies": [
            {"symbol": neighbor, "similarity": score, "role": proxy_role, "rank": i + 1}
            for i, (neighbor, score) in enumerate(neighbors)
        ],
        "expanded_proxies": [
            {"symbol": neighbor, "similarity": score, "role": proxy_role, "rank": i + 1}
            for i, (neighbor, score) in enumerate(expanded_neighbors)
        ],
        "noncoding_supported": hit["gene_type"] != "protein_coding",
        "llm_calls": [call],
        "limits": {"max_proxies": MAX_PERTURBATION_PROXIES, "max_expanded_proxies": MAX_EXPANDED_PERTURBATION_PROXIES},
    }


def _llm_route_functions(
    intent: QueryIntent,
    exact_selected: list[dict[str, Any]],
    unresolved: list[str],
    function_index: FunctionIndex,
    llm_provider: Any,
) -> dict[str, Any]:
    if intent.query_type == "reverse":
        return _llm_route_reverse_functions(intent, exact_selected, unresolved, function_index, llm_provider)
    payload, evidence = _llm_json(
        llm_provider,
        stage="function_mapping",
        system_prompt=(
            "You are PxFquery L2 function routing. Return one JSON object with selected_var_names. "
            "Select only exact var_name strings from the provided fixed_function_index. "
            "For narrow terms choose 1-2, for ambiguous terms choose up to 5. Do not create new functions."
        ),
        user_payload={
            "query_type": intent.query_type,
            "unresolved_terms": unresolved,
            "fixed_function_index": function_index.for_llm(),
            "max_selected": MAX_FUNCTION_FORWARD,
        },
    )
    mapped = _validate_function_payload(payload, function_index, MAX_FUNCTION_FORWARD)
    call = _llm_call_record("function_mapping", "ok" if mapped else "failed", evidence, payload)
    selected = exact_selected + [_function_record(v, function_index, "llm-mapped", len(exact_selected) + i + 1) for i, v in enumerate(mapped)]
    return {
        "status": "resolved" if selected else "llm-required",
        "mode": "llm-function-mapping",
        "selected": selected[:MAX_FUNCTION_FORWARD],
        "unresolved_terms": [] if mapped else unresolved,
        "ambiguity_level": _function_ambiguity_level(intent, selected[:MAX_FUNCTION_FORWARD]),
        "broad_function_route": len(selected[:MAX_FUNCTION_FORWARD]) >= MAX_FUNCTION_FORWARD,
        "llm_calls": [call],
        "limits": {
            "forward_max_functions": MAX_FUNCTION_FORWARD,
            "reverse_interpretation_sets": MAX_REVERSE_INTERPRETATION_SETS,
            "reverse_functions_per_set": MAX_REVERSE_FUNCTIONS_PER_SET,
        },
    }


def _llm_route_reverse_functions(
    intent: QueryIntent,
    exact_selected: list[dict[str, Any]],
    unresolved: list[str],
    function_index: FunctionIndex,
    llm_provider: Any,
) -> dict[str, Any]:
    perspectives = ["direct_pathway", "mechanism_or_program", "phenotype_or_state"]
    sets: list[dict[str, Any]] = []
    calls: list[dict[str, Any]] = []
    if exact_selected:
        sets.append(
            {
                "set_id": "exact",
                "status": "resolved-without-llm",
                "perspective": "exact_index_match",
                "functions": exact_selected[:MAX_REVERSE_FUNCTIONS_PER_SET],
            }
        )
    jobs = [(i, perspective, [0.0, 0.35, 0.7][i - 1]) for i, perspective in enumerate(perspectives, 1)]

    def run_mapping(job: tuple[int, str, float]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        i, perspective, temperature = job
        payload, evidence = _llm_json(
            llm_provider,
            stage=f"function_reverse_mapping_{perspective}",
            temperature=temperature,
            system_prompt=(
                "You are PxFquery L2 reverse function routing. Return one JSON object with selected_var_names. "
                "Use the requested perspective, but select only exact var_name strings from fixed_function_index. "
                "Select up to three functions. Do not create new functions."
            ),
            user_payload={
                "query_type": intent.query_type,
                "perspective": perspective,
                "function_desc": intent.function_desc,
                "activate": intent.activate,
                "suppress": intent.suppress,
                "unresolved_terms": unresolved,
                "fixed_function_index": function_index.for_llm(),
                "max_selected": MAX_REVERSE_FUNCTIONS_PER_SET,
            },
        )
        mapped = _validate_function_payload(payload, function_index, MAX_REVERSE_FUNCTIONS_PER_SET)
        call = _llm_call_record(f"function_reverse_mapping_{perspective}", "ok" if mapped else "empty", evidence, payload, temperature=temperature)
        if mapped:
            functions = [
                _function_record(v, function_index, "llm-mapped", rank + 1, direction=_direction_for_reverse(intent))
                for rank, v in enumerate(mapped)
            ]
            return call, {"set_id": f"llm_{i}_{perspective}", "status": "resolved", "perspective": perspective, "functions": functions}
        return call, None

    with ThreadPoolExecutor(max_workers=len(jobs)) as executor:
        for call, interpretation_set in executor.map(run_mapping, jobs):
            calls.append(call)
            if interpretation_set:
                sets.append(interpretation_set)
    selected = exact_selected[:MAX_REVERSE_FUNCTIONS_PER_SET]
    if not selected and sets:
        selected = sets[0]["functions"]
    convergence = _reverse_interpretation_convergence(sets)
    return {
        "status": "resolved" if selected or sets else "llm-required",
        "mode": "three-pass-llm-reverse-function-mapping",
        "selected": selected,
        "unresolved_terms": [] if sets else unresolved,
        "interpretation_sets": sets,
        "reverse_mapping_convergence": convergence,
        "reverse_mapping_policy": "three independent LLM mappings validated against the fixed 91-function index",
        "llm_calls": calls,
        "limits": {
            "forward_max_functions": MAX_FUNCTION_FORWARD,
            "reverse_interpretation_sets": MAX_REVERSE_INTERPRETATION_SETS,
            "reverse_functions_per_set": MAX_REVERSE_FUNCTIONS_PER_SET,
        },
    }


def _combine_status(
    cell_route: dict[str, Any],
    perturbation_route: dict[str, Any],
    function_route: dict[str, Any],
    combination_route: dict[str, Any],
    llm_calls: list[dict[str, Any]],
) -> str:
    routes = [cell_route, perturbation_route, function_route, combination_route]
    if any(r.get("status") == "resource-missing" for r in routes):
        return "resource-missing"
    if any(call.get("status") == "required" for call in llm_calls):
        return "llm_unavailable"
    if any(call.get("status") == "failed" for call in llm_calls):
        return "llm_output_invalid"
    if combination_route.get("status") == "no_pair_available":
        return "no_pair_available"
    if any(str(r.get("status", "")).startswith("blocked") for r in routes):
        return "unresolved"
    if any(r.get("status") == "unresolved" for r in routes):
        return "unresolved"
    return "routed"


def _required_capabilities(intent: QueryIntent) -> list[str]:
    capabilities = ["entity_resolution", "resource_pack_query"]
    if intent.query_type == "forward":
        capabilities.extend(["forward_query", "perturbation_resolution"])
    if intent.query_type == "reverse":
        capabilities.extend(["reverse_query", "function_resolution"])
    if intent.pert_class:
        capabilities.append(f"{intent.pert_class}_routing")
    if intent.bio_context:
        capabilities.append("context_resolution")
    return capabilities


def _route_reason(intent: QueryIntent, route_status: str) -> str:
    reasons = {
        "needs-intent-completion": "natural-language layer produced an incomplete intent",
        "resource-missing": "resource-backed routing could not start because required index files are missing",
        "llm_unavailable": "real LLM routing is required for at least one ambiguous dimension, but no usable provider completed that step",
        "llm_output_invalid": "real LLM routing ran, but at least one output failed resource-index validation or provider completion",
        "unresolved": "resource routing ran but did not find enough usable candidates",
        "no_pair_available": "resource routing found entity candidates but no checked route candidate is available in loaded matrix metadata",
        "routed": "resource indexes resolved the requested dimensions into bounded execution candidates",
    }
    return reasons.get(route_status, f"{intent.query_type} intent requires resource-backed routing and execution")


def _query_id(intent: QueryIntent) -> str:
    encoded = json.dumps(intent.to_dict(), ensure_ascii=True, sort_keys=True)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()[:16]


def _selected_route(
    intent: QueryIntent,
    cell_route: dict[str, Any],
    perturbation_route: dict[str, Any],
    function_route: dict[str, Any],
    combination_route: dict[str, Any],
) -> dict[str, Any]:
    selected: dict[str, Any] = {
        "query_type": intent.query_type,
        "cell": (cell_route.get("selected") or [None])[0],
        "combination_status": combination_route.get("status"),
        "selected_combination_routes": combination_route.get("selected_routes", []),
    }
    if intent.query_type == "forward":
        selected["perturbation"] = (perturbation_route.get("selected") or [None])[0]
        selected["perturbation_proxies"] = perturbation_route.get("proxies", [])[:MAX_PERTURBATION_PROXIES]
        selected["functions"] = function_route.get("selected", [])[:MAX_FUNCTION_FORWARD]
        selected["tier_order"] = combination_route.get("tier_order", [])
    else:
        selected["function_interpretation_sets"] = function_route.get("interpretation_sets", [])
        selected["functions"] = function_route.get("selected", [])
    return selected


def _rejected_candidates(
    cell_route: dict[str, Any],
    perturbation_route: dict[str, Any],
    function_route: dict[str, Any],
    combination_route: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    rejected: list[dict[str, Any]] = []
    for candidate in cell_route.get("candidates", [])[MAX_CELL_CANDIDATES:]:
        rejected.append({"dimension": "cell", "candidate": candidate, "reason": "exceeds max cell candidate limit"})
    for candidate in perturbation_route.get("retrieved_candidates", []):
        if not perturbation_route.get("selected"):
            rejected.append({"dimension": "perturbation", "candidate": candidate, "reason": "retrieved only; not validated as selected"})
    for term in function_route.get("unresolved_terms", []):
        rejected.append({"dimension": "function", "candidate": term, "reason": "not validated against function_index"})
    if combination_route:
        for check in combination_route.get("pair_availability", {}).get("checks", []):
            if check.get("available") is False:
                rejected.append({"dimension": "combination", "candidate": check, "reason": check.get("reject_reason", "combination unavailable")})
    return rejected


def _unresolved_dimensions(
    cell_route: dict[str, Any],
    perturbation_route: dict[str, Any],
    function_route: dict[str, Any],
    combination_route: dict[str, Any],
    llm_calls: list[dict[str, Any]],
) -> list[str]:
    unresolved: list[str] = []
    for name, route in [("cell", cell_route), ("perturbation", perturbation_route), ("function", function_route), ("combination", combination_route)]:
        if route.get("status") in {"llm-required", "unresolved", "resource-missing", "no_pair_available"} or str(route.get("status", "")).startswith("blocked"):
            unresolved.append(name)
    if any(call.get("status") in {"required", "failed"} for call in llm_calls):
        unresolved.append("llm")
    return sorted(set(unresolved))


def _handoff_payload(
    intent: QueryIntent,
    selected_route: dict[str, Any],
    cell_route: dict[str, Any],
    perturbation_route: dict[str, Any],
    function_route: dict[str, Any],
    combination_route: dict[str, Any],
) -> dict[str, Any]:
    return {
        "query_type": intent.query_type,
        "resolver_intent": intent.to_resolver_intent(),
        "cell_candidates": cell_route.get("candidates", []),
        "selected": selected_route,
        "perturbation_candidates": {
            "selected": perturbation_route.get("selected", []),
            "proxies": perturbation_route.get("proxies", []),
        },
        "function_candidates": {
            "selected": function_route.get("selected", []),
            "interpretation_sets": function_route.get("interpretation_sets", []),
        },
        "combination": combination_route,
    }


def _direction_for_reverse(intent: QueryIntent) -> str:
    if intent.activate and not intent.suppress:
        return "activate"
    if intent.suppress and not intent.activate:
        return "suppress"
    if intent.activate and intent.suppress:
        return "mixed"
    return "target"


def _function_ambiguity_level(intent: QueryIntent, selected: list[dict[str, Any]]) -> str:
    text = " ".join([intent.function_desc or "", *intent.activate, *intent.suppress]).lower()
    broad_words = {"phenotype", "state", "profile", "program", "differentiation", "invasive", "immune", "cycling", "growth"}
    if len(selected) >= MAX_FUNCTION_FORWARD or any(word in text for word in broad_words):
        return "broad"
    if len(selected) >= 3:
        return "medium"
    return "narrow"


def _load_json(path: Path | None) -> Any:
    if path is None:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _find_resource(root: Path | None, names: list[str]) -> Path | None:
    if root is None:
        return None
    for name in names:
        direct = root / name
        if direct.exists():
            return direct.resolve()
        matches = sorted(root.rglob(name))
        if matches:
            return matches[0].resolve()
    return None


def _json_keys(path: Path | None) -> list[str]:
    data = _load_json(path)
    return list(data.keys()) if isinstance(data, dict) else []


def _cell_alias_lookup(text: str, tree_data: dict[str, Any]) -> str | None:
    cell_index = tree_data.get("cell_index", {}) if isinstance(tree_data, dict) else {}
    return cell_index.get(text.strip().lower())


def _lookup_drug(term: str, drug_index: DrugIndex) -> str | None:
    stripped = term.strip()
    if stripped.upper().startswith("BRD-"):
        canonical = stripped.upper()
        aliases = getattr(drug_index, "_index", {})
        if canonical in set(aliases.values()) or drug_index.has_neighbors(canonical):
            return canonical
        return None
    return drug_index.lookup(stripped)


def _limited_cell_proxies(proxies: dict[str, list[str]], *, start_rank: int) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for role, limit in [("same_subtype", 3), ("same_disease", 2), ("same_lineage", 1)]:
        for cell in proxies.get(role, [])[:limit]:
            out.append({"cell": cell, "role": role, "rank": start_rank + len(out)})
            if len(out) >= MAX_CELL_CANDIDATES - 1:
                return out
    return out


def _expanded_cell_proxies(proxies: dict[str, list[str]], *, start_rank: int) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    scopes = {
        "same_subtype": ("same_subtype", 0),
        "same_disease": ("same_disease_sibling", 1),
        "same_lineage": ("same_lineage", 2),
    }
    for role in ["same_subtype", "same_disease", "same_lineage"]:
        for cell in proxies.get(role, []):
            key = str(cell).upper()
            if key in seen:
                continue
            seen.add(key)
            scope, distance = scopes[role]
            out.append({"cell": cell, "role": role, "rank": start_rank + len(out), "cell_expansion_scope": scope, "cell_route_distance": distance})
            if len(out) >= MAX_EXPANDED_CELL_CANDIDATES - 1:
                return out
    return out


def _expanded_tree_cells(cells: list[str], cell_index: CellLineIndex) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add(cell: str, role: str, scope: str, distance: int, source_path: tuple[str, str, str] | None = None) -> None:
        if len(out) >= MAX_EXPANDED_CELL_CANDIDATES:
            return
        canonical = cell_index.canonical(cell) or cell
        key = str(canonical).upper()
        if key in seen or not cell_index.is_valid(canonical):
            return
        candidate_path = cell_index.get_cell_path(canonical)
        seen.add(key)
        item = {
            "cell": canonical,
            "role": role,
            "rank": len(out) + 1,
            "cell_expansion_scope": scope,
            "cell_route_distance": distance,
        }
        if source_path:
            item["source_lineage"] = source_path[0]
            item["source_disease"] = source_path[1]
            item["source_subtype"] = source_path[2]
        if candidate_path:
            item["candidate_lineage"] = candidate_path[0]
            item["candidate_disease"] = candidate_path[1]
            item["candidate_subtype"] = candidate_path[2]
            if source_path and _is_cancer_label(source_path[1]) and not _is_cancer_label(candidate_path[1]):
                item["cell_expansion_scope"] = "normal_lineage_data_anchor"
                item["cell_route_distance"] = max(distance, 3)
                item["semantic_downgrade_reason"] = "source context is cancer-specific but candidate cell is normal/non-cancer lineage"
        out.append(item)

    if not cells:
        return out
    first_path = cell_index.get_cell_path(cells[0])
    if not first_path:
        return out
    source_path = tuple(first_path)
    for cell in cells:
        add(cell, "llm-tree-leaf", "selected_leaf", 0, source_path)
    lineage, disease, _subtype = first_path
    for candidate in cell_index.valid_cells():
        path = cell_index.get_cell_path(candidate)
        if path and path[0] == lineage and path[1] == disease:
            add(candidate, "same_disease_sibling", "same_disease_sibling", 1, source_path)
    for candidate in cell_index.valid_cells():
        path = cell_index.get_cell_path(candidate)
        if path and path[0] == lineage:
            add(candidate, "same_lineage", "same_lineage", 2, source_path)
    return out


def _is_cancer_label(label: str | None) -> bool:
    text = str(label or "").lower()
    return any(word in text for word in ("cancer", "carcinoma", "tumor", "melanoma", "leukemia", "lymphoma", "glioma", "sarcoma"))


def _llm_choose_option(
    llm_provider: Any,
    *,
    stage: str,
    user_text: str,
    level: str,
    options: list[str],
) -> tuple[str | None, dict[str, Any]]:
    payload, evidence = _llm_json(
        llm_provider,
        stage=stage,
        system_prompt=(
            "You are PxFquery L2 cell-context routing. Return one JSON object. "
            "Choose selected_option exactly from options. Do not invent options. "
            "Use null only if no option is defensible."
        ),
        user_payload={"bio_context": user_text, "level": level, "options": options},
    )
    selected = payload.get("selected_option") if isinstance(payload, dict) else None
    ok = isinstance(selected, str) and selected in options
    return selected if ok else None, _llm_call_record(stage, "ok" if ok else "failed", evidence, payload)


def _llm_json(llm_provider: Any, *, stage: str, system_prompt: str, user_payload: dict[str, Any], temperature: float = 0) -> tuple[Any, dict[str, Any]]:
    if not hasattr(llm_provider, "request_json"):
        raise TypeError("L2 LLM routing requires a provider exposing request_json(...)")
    try:
        payload, evidence = llm_provider.request_json(stage=stage, system_prompt=system_prompt, user_payload=user_payload, temperature=temperature)
    except Exception as exc:
        payload = {}
        config = getattr(llm_provider, "config", None)
        evidence = {
            "provider": getattr(config, "name", None),
            "base_url": getattr(config, "base_url", None),
            "model": getattr(config, "model", None),
            "started_at": datetime.now(timezone.utc).isoformat(),
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "attempts": [{"attempt": None, "ok": False, "error": f"{type(exc).__name__}: {exc}"[:500]}],
            "final_status": "failed",
            "error": f"{type(exc).__name__}: {exc}"[:500],
            "parsed_json_hash": None,
        }
    evidence["input_payload"] = _truncate_evidence_payload(user_payload)
    return payload, evidence


def _llm_call_record(stage: str, status: str, evidence: dict[str, Any], payload: Any, *, temperature: float = 0) -> dict[str, Any]:
    if evidence.get("final_status") == "failed":
        status = "failed"
    excerpt = json.dumps(payload, ensure_ascii=True, sort_keys=True)[:500] if payload is not None else ""
    validated = status in {"ok", "empty"}
    return {
        "stage": stage,
        "status": status,
        "provider": evidence.get("provider"),
        "base_url": evidence.get("base_url"),
        "model": evidence.get("model"),
        "temperature": temperature,
        "final_status": evidence.get("final_status"),
        "attempts": evidence.get("attempts", []),
        "parsed_json_hash": evidence.get("parsed_json_hash"),
        "raw_output": payload,
        "input_payload": evidence.get("input_payload"),
        "validated": validated,
        "discard_reason": None if validated else "LLM output failed index validation",
        "response_excerpt": excerpt,
    }


def _truncate_evidence_payload(payload: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in payload.items():
        if isinstance(value, list):
            out[key] = value[:10]
            out[f"{key}_count"] = len(value)
        elif isinstance(value, str) and len(value) > 2000:
            out[key] = value[:2000]
            out[f"{key}_truncated"] = True
        else:
            out[key] = value
    return out


def _lookup_full_gene(term: str, gene_index: dict[str, Any]) -> dict[str, Any] | None:
    if not term:
        return None
    hit = gene_index.get(term.strip().lower())
    if not isinstance(hit, dict):
        hit = gene_index.get(term.strip().upper())
    if not isinstance(hit, dict):
        return None
    return {
        "symbol": hit.get("symbol", term.strip().upper()),
        "gene_type": hit.get("gene_type"),
        "in_matrix": bool(hit.get("in_matrix")),
    }


def _lookup_simple_gene(term: str, simple_index: dict[str, Any]) -> dict[str, Any] | None:
    if not term or not simple_index:
        return None
    key = term.strip().upper()
    value = simple_index.get(key)
    if value is None:
        return None
    gene_type = value if isinstance(value, str) else value.get("gene_type")
    return {"symbol": key, "gene_type": gene_type, "in_matrix": True}


def _gene_neighbors(symbol: str, gene_neighbors: dict[str, Any], *, top_n: int) -> list[tuple[str, float]]:
    raw = gene_neighbors.get(symbol.upper()) or gene_neighbors.get(symbol)
    if not isinstance(raw, list):
        return []
    out: list[tuple[str, float]] = []
    for item in raw:
        if not isinstance(item, list | tuple) or len(item) < 2:
            continue
        score = float(item[1]) / 100.0
        out.append((str(item[0]), score))
        if len(out) >= top_n:
            break
    return out


def _function_terms(intent: QueryIntent) -> list[tuple[str, str]]:
    terms: list[tuple[str, str]] = []
    if intent.query_type == "reverse" and intent.pert_desc:
        terms.append((_reverse_direction_from_text(intent), intent.pert_desc))
    if intent.function_desc and not _is_reverse_operator_only(intent.function_desc):
        terms.append((_reverse_direction_from_text(intent) if intent.query_type == "reverse" else "target", intent.function_desc))
    for term in intent.activate:
        if not _forward_term_describes_perturbation(intent, term):
            terms.append(("activate", term))
    for term in intent.suppress:
        if not _forward_term_describes_perturbation(intent, term):
            terms.append(("suppress", term))
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, str]] = []
    for direction, term in terms:
        key = (direction, term.strip().lower())
        if term and key not in seen:
            out.append((direction, term))
            seen.add(key)
    return out


def _forward_operation_terms(intent: QueryIntent) -> list[str]:
    if intent.query_type != "forward":
        return []
    terms: list[str] = []
    if intent.function_desc and _is_reverse_operator_only(intent.function_desc):
        terms.append(intent.function_desc)
    for term in [*intent.activate, *intent.suppress]:
        if _forward_term_describes_perturbation(intent, term):
            terms.append(term)
    return terms


def _forward_term_describes_perturbation(intent: QueryIntent, term: str) -> bool:
    if intent.query_type != "forward" or not intent.pert_desc or not term:
        return False
    term_norm = _normalize_token(term)
    pert_norm = _normalize_token(intent.pert_desc)
    if not term_norm or not pert_norm:
        return False
    if term_norm == pert_norm or term_norm in pert_norm or pert_norm in term_norm:
        return True
    term_tokens = set(term_norm.split())
    pert_tokens = set(pert_norm.split())
    return bool(term_tokens and term_tokens <= pert_tokens)


def _llm_extract_reverse_function_terms(intent: QueryIntent, llm_provider: Any) -> tuple[list[tuple[str, str]], list[dict[str, Any]]]:
    payload, evidence = _llm_json(
        llm_provider,
        stage="reverse_function_term_extraction",
        system_prompt=(
            "You are PxFquery L2 reverse-query repair. Return one JSON object with activate and suppress arrays. "
            "Extract only biological functions or cell states from the user query. "
            "Do not extract cell context, perturbation modality, or words like genetic/drug/perturbation."
        ),
        user_payload={
            "raw_query": intent.raw_query,
            "bio_context": intent.bio_context,
            "pert_class": intent.pert_class,
            "genetic_modality": intent.genetic_modality,
            "function_desc": intent.function_desc,
            "activate": intent.activate,
            "suppress": intent.suppress,
        },
        temperature=0,
    )
    terms: list[tuple[str, str]] = []
    if isinstance(payload, dict):
        for term in payload.get("activate", []) if isinstance(payload.get("activate"), list) else []:
            if isinstance(term, str) and term.strip():
                terms.append(("activate", term.strip()))
        for term in payload.get("suppress", []) if isinstance(payload.get("suppress"), list) else []:
            if isinstance(term, str) and term.strip():
                terms.append(("suppress", term.strip()))
    call = _llm_call_record("reverse_function_term_extraction", "ok" if terms else "failed", evidence, payload)
    return terms, [call]


def _is_reverse_operator_only(text: str) -> bool:
    norm = _normalize_token(text)
    operators = {
        "enhance",
        "increase",
        "increased",
        "activate",
        "activation",
        "reduce",
        "decrease",
        "decreased",
        "suppress",
        "suppression",
        "inhibit",
        "inhibition",
        "loss of function",
        "gain of function",
    }
    return norm in operators


def _reverse_direction_from_text(intent: QueryIntent) -> str:
    text = _normalize_token(" ".join([intent.function_desc or "", intent.raw_query or ""]))
    activate_words = {"enhance", "increase", "activate", "boost", "promote", "upregulate"}
    suppress_words = {"reduce", "decrease", "suppress", "inhibit", "block", "downregulate"}
    has_activate = any(word in text for word in activate_words)
    has_suppress = any(word in text for word in suppress_words)
    if has_activate and not has_suppress:
        return "activate"
    if has_suppress and not has_activate:
        return "suppress"
    if has_activate and has_suppress:
        return "mixed"
    return "target"


def _is_forward_scope_only_terms(terms: list[str]) -> bool:
    if not terms:
        return False
    scope_tokens = {
        "broad",
        "functional",
        "function",
        "functions",
        "pathway",
        "pathways",
        "program",
        "programs",
        "hallmark",
        "hallmarks",
        "signature",
        "signatures",
        "readout",
        "readouts",
        "output",
        "outputs",
        "effect",
        "effects",
        "consequence",
        "consequences",
        "footprint",
        "profile",
        "profiles",
        "state",
        "states",
        "cell",
        "downstream",
        "change",
        "changes",
        "shift",
        "shifts",
        "alter",
        "altered",
        "affect",
        "affects",
        "affected",
        "report",
        "ask",
        "across",
        "level",
    }
    operation_tokens = {"loss", "gain", "of", "blocker", "inhibitor", "inhibition", "antagonist", "agonist"}
    stop_tokens = {"and", "or", "the", "a", "an", "to", "by", "after", "with", "in", "on"}
    for term in terms:
        norm = _normalize_token(term)
        tokens = set(norm.split()) - stop_tokens
        if not tokens:
            return False
        if tokens & operation_tokens and len(tokens - operation_tokens) <= 2:
            continue
        if tokens <= (scope_tokens | operation_tokens):
            continue
        if len(tokens & scope_tokens) >= 2 and len(tokens - scope_tokens - operation_tokens) <= 3:
            continue
        else:
            return False
    return True


def _reverse_interpretation_convergence(sets: list[dict[str, Any]]) -> dict[str, Any]:
    signatures: list[tuple[str, ...]] = []
    for item in sets:
        if item.get("set_id") == "exact":
            continue
        functions = tuple(f.get("var_name") for f in item.get("functions", []) if f.get("var_name"))
        if functions:
            signatures.append(functions)
    unique = sorted(set(signatures))
    return {
        "llm_nonempty_set_count": len(signatures),
        "unique_llm_set_count": len(unique),
        "converged": len(unique) <= 1 if signatures else None,
        "unique_sets": [list(item) for item in unique],
    }


def _validate_function_payload(payload: Any, function_index: FunctionIndex, limit: int) -> list[str]:
    if not isinstance(payload, dict):
        return []
    raw = payload.get("selected_var_names", [])
    if not isinstance(raw, list):
        return []
    out: list[str] = []
    for item in raw:
        if not isinstance(item, str):
            continue
        var_name = item if function_index.validate(item) else function_index.lookup(item)
        if var_name and var_name not in out:
            out.append(var_name)
        if len(out) >= limit:
            break
    return out


def _function_record(var_name: str, function_index: FunctionIndex, role: str, rank: int, *, direction: str = "target") -> dict[str, Any]:
    return {
        "var_name": var_name,
        "label": function_index.label(var_name),
        "source": function_index.source(var_name),
        "direction": direction,
        "input": role,
        "rank": rank,
    }


def _fuzzy_candidates(term: str, options: list[str], limit: int) -> list[dict[str, Any]]:
    term_norm = _normalize_token(term)
    term_tokens = set(term_norm.split())
    term_ngrams = _char_ngrams(term_norm)
    scored: list[tuple[float, str]] = []
    for option in options:
        option_norm = _normalize_token(str(option))
        if not option_norm:
            continue
        option_tokens = set(option_norm.split())
        option_ngrams = _char_ngrams(option_norm)
        edit = SequenceMatcher(None, term_norm, option_norm).ratio()
        token_overlap = len(term_tokens & option_tokens) / max(1, len(term_tokens | option_tokens))
        ngram_overlap = len(term_ngrams & option_ngrams) / max(1, len(term_ngrams | option_ngrams))
        prefix_suffix = 0.0
        if option_norm.startswith(term_norm) or term_norm.startswith(option_norm):
            prefix_suffix = 0.85
        elif option_norm.endswith(term_norm) or term_norm.endswith(option_norm):
            prefix_suffix = 0.75
        brd_bonus = 0.9 if term_norm.startswith("brd ") and option_norm.startswith("brd ") and term_norm.replace(" ", "-") == option_norm.replace(" ", "-") else 0.0
        score = max(edit, token_overlap, ngram_overlap, prefix_suffix, brd_bonus)
        if term_norm in option_norm or option_norm in term_norm:
            score = max(score, 0.75)
        if score >= 0.45:
            scored.append((score, str(option)))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [{"value": value, "similarity": round(score, 3), "rank": i + 1} for i, (score, value) in enumerate(scored[:limit])]


def _normalize_token(text: str) -> str:
    out = []
    for ch in text.strip().lower():
        out.append(ch if ch.isalnum() else " ")
    return " ".join("".join(out).split())


def _is_mechanism_class_drug_query(text: str) -> bool:
    norm = _normalize_token(text)
    if not norm:
        return False
    mechanism_words = {"inhibition", "inhibitor", "blocker", "antagonist", "agonist", "activator", "suppressor"}
    tokens = set(norm.split())
    return bool(tokens & mechanism_words) and not norm.startswith("brd ")


def _char_ngrams(text: str, n: int = 3) -> set[str]:
    compact = text.replace(" ", "")
    if len(compact) <= n:
        return {compact} if compact else set()
    return {compact[i : i + n] for i in range(len(compact) - n + 1)}
