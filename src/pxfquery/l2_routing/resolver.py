"""
resolver.py — Resolver pipeline with forward-first proxy logic.

Forward search policy:
  L1 EXACT:       exact cell + exact perturbation
  L2 PROXY_PERT:  exact cell + perturbation neighbors
  L3 PROXY_CELL:  proxy cells + exact perturbation
  L4 PROXY_BOTH:  proxy cells + perturbation neighbors
"""

from __future__ import annotations

import os
import re
import time
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from openai import OpenAI

from pxfquery.l2_routing.index import CellLineIndex, DrugIndex, FunctionIndex, GeneIndex
from pxfquery.l2_routing import llm_prompts
from pxfquery.l3_execution.forward import ForwardResult


@dataclass
class ResolverConfig:
    provider: str = "openai_compatible"
    model: Optional[str] = None
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    default_top_n: int = 20
    summary_include_numbers: bool = False
    genetic_multi_source: bool = True
    genetic_sources: tuple[str, ...] = ("xpr", "sh")
    forward_collect_all_evidence: bool = True
    max_forward_evidence: int = 15
    forward_budget_exact: int = 1
    forward_budget_proxy_pert: int = 4
    forward_budget_proxy_cell: int = 4
    forward_budget_proxy_both: int = 6
    must_answer: bool = True
    verbosity: str = "normal"
    log_level: Optional[str] = None
    log_enabled: bool = True
    log_to_file: bool = False
    log_dir: str = "report/04_management/logs"
    log_file_prefix: str = "pxfquery"
    log_llm_io: Optional[bool] = None
    log_human_readable: bool = False


@dataclass
class ForwardPlan:
    pert_type: str
    pert_class: str
    base_pert: str
    pert_neighbors: list[str] = field(default_factory=list)
    exact_cell: Optional[str] = None
    proxy_cells: list[str] = field(default_factory=list)
    cell_reason: str = ""


class QueryResolver:
    """
    Query resolver that orchestrates intent parsing and index-backed resolution.
    """

    def __init__(
        self,
        *,
        forward_engines: dict,
        reverse_engines: dict,
        index_dir: str | Path,
        config: Optional[ResolverConfig] = None,
    ):
        self.forward_engines = forward_engines
        self.reverse_engines = reverse_engines
        self.index_dir = Path(index_dir)
        self.config = config or ResolverConfig()
        self.model = self._resolve_model(self.config)
        self.client = self._build_client(self.config)

        self.cellline_index = CellLineIndex(
            self.index_dir / "cellline_index.json",
            self.index_dir / "cellline_neighbors.json",
        )
        self.gene_index = GeneIndex(
            self.index_dir / "gene_index_simple.json",
            self.index_dir / "gene_neighbors_simple.json",
        )
        self.drug_index = DrugIndex(
            self.index_dir / "drug_index.json",
            self.index_dir / "drug_neighbors.json",
        )
        self.function_index = FunctionIndex(self.index_dir / "function_index.json")
        self._engine_pair_lookup_cache: dict[int, dict[str, dict[str, str]]] = {}
        self._intent_cache: dict[str, dict] = {}
        self._prompt_cache: dict[tuple, object] = {}
        self._llm_call_stats_total: dict[str, dict[str, float]] = {}
        self._llm_call_stats_query: dict[str, dict[str, float]] = {}
        self._query_counter = 0
        self._active_query_id = "-"
        self._logger = logging.getLogger("pxfquery.resolver")
        if self.config.log_llm_io is None:
            self._log_llm_io = str(self.config.verbosity).lower() == "debug"
        else:
            self._log_llm_io = bool(self.config.log_llm_io)

    def resolve_and_query(
        self,
        user_input: str,
        pert_type: Optional[str] = None,
        top_n: Optional[int] = None,
        summarize: bool = True,
    ):
        self._active_query_id = self._next_query_id()
        self._log_info("Step 1/3 Start resolve | summarize=%s | user_input=%s", summarize, user_input[:160])
        try:
            self._llm_call_stats_query = {}
            intent = self._intent_cache.get(user_input)
            if intent is None:
                intent = self._call_prompt("llm_parse_intent", user_input)
                if not self._is_valid_intent(intent):
                    raise ValueError(f"LLM intent is invalid: {intent!r}")
                self._intent_cache[user_input] = dict(intent or {})
            return self.execute_intent(
                intent,
                user_input=user_input,
                pert_type=pert_type,
                top_n=top_n,
                summarize=summarize,
            )
        finally:
            self._active_query_id = "-"

    def execute_intent(
        self,
        intent: dict,
        *,
        user_input: str,
        pert_type: Optional[str] = None,
        top_n: Optional[int] = None,
        summarize: bool = False,
    ):
        if not self._is_valid_intent(intent):
            raise ValueError(f"Resolver received invalid intent: {intent!r}")
        query_type = (intent.get("query_type") or "").lower()
        k = int(intent.get("top_n") or top_n or self.config.default_top_n)
        self._llm_call_stats_query = {}
        self._log_info(
            "Intent routed | query_type=%s pert_class=%s bio_context=%s pert_desc=%s",
            query_type,
            intent.get("pert_class"),
            intent.get("bio_context"),
            intent.get("pert_desc"),
        )
        if query_type == "reverse":
            result = self._run_reverse(intent, user_input, pert_type=pert_type, top_k=k)
            if summarize:
                result.summary = self._call_prompt(
                    "llm_summarize_reverse",
                    result,
                    include_numbers=self.config.summary_include_numbers,
                )
        else:
            result = self._run_forward(intent, user_input, pert_type=pert_type, top_n=k)
            if summarize:
                result.summary = self._call_prompt(
                    "llm_summarize_forward",
                    result,
                    include_numbers=self.config.summary_include_numbers,
                )
        result.resolver_intent = intent
        meta = getattr(result, "resolver_meta", {}) or {}
        meta["llm_call_stats"] = self._finalize_llm_stats()
        meta["query_id"] = self._active_query_id
        result.resolver_meta = meta
        return result

    @staticmethod
    def _is_valid_intent(intent: Optional[dict]) -> bool:
        if not isinstance(intent, dict):
            return False
        qt = str(intent.get("query_type") or "").lower().strip()
        if qt not in ("forward", "reverse"):
            return False
        return True

    def _next_query_id(self) -> str:
        self._query_counter += 1
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        return f"q{ts}-{self._query_counter:04d}"

    def _log_info(self, message: str, *args) -> None:
        self._logger.info(message, *args, extra={"query_id": self._active_query_id})

    def _log_warning(self, message: str, *args) -> None:
        self._logger.warning(message, *args, extra={"query_id": self._active_query_id})

    def _log_debug(self, message: str, *args) -> None:
        self._logger.debug(message, *args, extra={"query_id": self._active_query_id})

    @staticmethod
    def _preview_payload(value, max_len: int = 360) -> str:
        text = repr(value)
        if len(text) <= max_len:
            return text
        return text[: max_len - 3] + "..."

    def _finalize_llm_stats(self) -> dict:
        return {
            "query": {
                k: {"count": int(v["count"]), "seconds": round(v["seconds"], 3)}
                for k, v in sorted(self._llm_call_stats_query.items())
            },
            "total": {
                k: {"count": int(v["count"]), "seconds": round(v["seconds"], 3)}
                for k, v in sorted(self._llm_call_stats_total.items())
            },
        }

    def _run_forward(
        self,
        intent: dict,
        user_input: str,
        pert_type: Optional[str],
        top_n: int,
    ):
        if self._should_use_genetic_multi(intent, pert_type):
            return self._run_forward_genetic_multi(intent, user_input, top_n=top_n)
        return self._run_forward_single(intent, user_input, pert_type=pert_type, top_n=top_n)

    def _run_forward_single(
        self,
        intent: dict,
        user_input: str,
        pert_type: Optional[str],
        top_n: int,
    ):
        plan = self._build_forward_plan(intent, user_input, pert_type)
        return self._run_forward_from_plan(plan, top_n)

    def _run_forward_from_plan(self, plan: ForwardPlan, top_n: int):
        engine = self.forward_engines[plan.pert_type]

        if self.config.forward_collect_all_evidence:
            evidences = self._collect_forward_evidences(plan, engine)
            if not evidences:
                result = ForwardResult.empty(
                    plan.base_pert,
                    note="No exact/proxy evidence found in current matrix for this (B, P) query.",
                )
                result.resolver_meta = self._forward_meta(plan, "NOT_FOUND", None, None)
                result.resolver_meta["evidence_candidates"] = []
                return result
            primary = evidences[0]
            result = engine.query(primary["query_name"], cell_line=primary["used_cell"], top_n=top_n)
            result.resolver_meta = self._forward_meta(
                plan,
                primary["hit_level"],
                primary["used_cell"],
                primary["used_perturbation"],
            )
            result.resolver_meta["evidence_candidates"] = evidences
            return result

        # L1: EXACT (exact cell + exact perturbation)
        if plan.exact_cell and self._has_pair(engine, plan.base_pert, plan.exact_cell):
            qname = self._query_name_for_pair(engine, plan.base_pert, plan.exact_cell)
            result = engine.query(qname, cell_line=plan.exact_cell, top_n=top_n)
            result.resolver_meta = self._forward_meta(plan, "EXACT", plan.exact_cell, plan.base_pert)
            return result

        # L2: PROXY_PERT (exact cell + perturbation neighbors)
        if plan.exact_cell:
            for nbr in plan.pert_neighbors:
                if self._has_pair(engine, nbr, plan.exact_cell):
                    qname = self._query_name_for_pair(engine, nbr, plan.exact_cell)
                    result = engine.query(qname, cell_line=plan.exact_cell, top_n=top_n)
                    result.resolver_meta = self._forward_meta(plan, "PROXY_PERT", plan.exact_cell, nbr)
                    return result

        # L3: PROXY_CELL (proxy cells + exact perturbation)
        for proxy_cell in plan.proxy_cells:
            if self._has_pair(engine, plan.base_pert, proxy_cell):
                qname = self._query_name_for_pair(engine, plan.base_pert, proxy_cell)
                result = engine.query(qname, cell_line=proxy_cell, top_n=top_n)
                result.resolver_meta = self._forward_meta(plan, "PROXY_CELL", proxy_cell, plan.base_pert)
                return result

        # L4: PROXY_BOTH (proxy cells + perturbation neighbors)
        for proxy_cell in plan.proxy_cells:
            for nbr in plan.pert_neighbors:
                if self._has_pair(engine, nbr, proxy_cell):
                    qname = self._query_name_for_pair(engine, nbr, proxy_cell)
                    result = engine.query(qname, cell_line=proxy_cell, top_n=top_n)
                    result.resolver_meta = self._forward_meta(plan, "PROXY_BOTH", proxy_cell, nbr)
                    return result

        # Fallback: no supported evidence found
        result = ForwardResult.empty(
            plan.base_pert,
            note="No exact/proxy evidence found in current matrix for this (B, P) query.",
        )
        result.resolver_meta = self._forward_meta(plan, "NOT_FOUND", None, None)
        return result

    def _collect_forward_evidences(self, plan: ForwardPlan, engine) -> list[dict]:
        out: list[dict] = []
        seen: set[tuple[str, str, str]] = set()
        level_count: dict[str, int] = {
            "EXACT": 0,
            "PROXY_PERT": 0,
            "PROXY_CELL": 0,
            "PROXY_BOTH": 0,
        }
        level_budget = {
            "EXACT": max(0, int(self.config.forward_budget_exact)),
            "PROXY_PERT": max(0, int(self.config.forward_budget_proxy_pert)),
            "PROXY_CELL": max(0, int(self.config.forward_budget_proxy_cell)),
            "PROXY_BOTH": max(0, int(self.config.forward_budget_proxy_both)),
        }
        global_budget = max(1, int(self.config.max_forward_evidence))

        def add(level: str, cell: str, pert: str):
            if level_count.get(level, 0) >= level_budget.get(level, global_budget):
                return
            if len(out) >= global_budget:
                return
            qname = self._query_name_for_pair(engine, pert, cell)
            key = (level, cell, str(pert))
            if key in seen:
                return
            seen.add(key)
            level_count[level] = level_count.get(level, 0) + 1
            out.append(
                {
                    "hit_level": level,
                    "used_cell": cell,
                    "used_perturbation": str(pert),
                    "query_name": qname,
                }
            )

        if plan.exact_cell and self._has_pair(engine, plan.base_pert, plan.exact_cell):
            add("EXACT", plan.exact_cell, plan.base_pert)

        if plan.exact_cell:
            for nbr in plan.pert_neighbors:
                if self._has_pair(engine, nbr, plan.exact_cell):
                    add("PROXY_PERT", plan.exact_cell, nbr)
                if len(out) >= global_budget:
                    break

        for proxy_cell in plan.proxy_cells:
            if self._has_pair(engine, plan.base_pert, proxy_cell):
                add("PROXY_CELL", proxy_cell, plan.base_pert)
            if len(out) >= global_budget:
                break

        for proxy_cell in plan.proxy_cells:
            for nbr in plan.pert_neighbors:
                if self._has_pair(engine, nbr, proxy_cell):
                    add("PROXY_BOTH", proxy_cell, nbr)
                if len(out) >= global_budget:
                    break
            if len(out) >= global_budget:
                break

        rank = {"EXACT": 0, "PROXY_PERT": 1, "PROXY_CELL": 2, "PROXY_BOTH": 3}
        out.sort(key=lambda x: rank.get(x["hit_level"], 9))
        return out[:global_budget]

    def _run_forward_genetic_multi(self, intent: dict, user_input: str, top_n: int):
        sources = [s for s in self.config.genetic_sources if s in self.forward_engines]
        if not sources:
            return self._run_forward_single(intent, user_input, pert_type=None, top_n=top_n)

        # Build mapping once to avoid duplicated LLM cost across xpr/sh.
        base_plan = self._build_forward_plan(intent, user_input, pert_type=sources[0])
        candidates: list[ForwardResult] = []
        for src in sources:
            plan = ForwardPlan(
                pert_type=src,
                pert_class=base_plan.pert_class,
                base_pert=base_plan.base_pert,
                pert_neighbors=list(base_plan.pert_neighbors),
                exact_cell=base_plan.exact_cell,
                proxy_cells=list(base_plan.proxy_cells),
                cell_reason=base_plan.cell_reason,
            )
            candidates.append(self._run_forward_from_plan(plan, top_n=top_n))
        if not candidates:
            return self._run_forward_single(intent, user_input, pert_type=None, top_n=top_n)

        def rank(r: ForwardResult):
            meta = getattr(r, "resolver_meta", {}) or {}
            level = meta.get("hit_level", "NOT_FOUND")
            order = {
                "EXACT": 0,
                "PROXY_PERT": 1,
                "PROXY_CELL": 2,
                "PROXY_BOTH": 3,
                "FORCED_MATCH": 4,
                "FORCED_FALLBACK": 5,
                "NOT_FOUND": 6,
            }
            return (order.get(level, 9), -int(getattr(r, "n_obs", 0)))

        selected = sorted(candidates, key=rank)[0]
        bundle = []
        for r in candidates:
            m = getattr(r, "resolver_meta", {}) or {}
            bundle.append(
                {
                    "pert_type": m.get("pert_type"),
                    "hit_level": m.get("hit_level"),
                    "used_cell": m.get("used_cell"),
                    "used_perturbation": m.get("used_perturbation"),
                    "found": bool(getattr(r, "found", False)),
                    "n_obs": int(getattr(r, "n_obs", 0)),
                    "note": str(getattr(r, "note", "")),
                }
            )
        selected.resolver_meta = dict(getattr(selected, "resolver_meta", {}) or {})
        selected.resolver_meta["composite_mode"] = "genetic_multi_source"
        selected.resolver_meta["evidence_bundle"] = bundle
        selected.resolver_meta["selected_source"] = selected.resolver_meta.get("pert_type")
        selected.resolver_meta["source_overview"] = " | ".join(
            f"{b.get('pert_type')}:{b.get('hit_level')}:{b.get('n_obs')}" for b in bundle
        )
        return selected

    def _should_use_genetic_multi(self, intent: dict, pert_type: Optional[str]) -> bool:
        if pert_type is not None:
            return False
        if not self.config.genetic_multi_source:
            return False
        cls = (intent.get("pert_class") or "").lower().strip()
        return cls in ("", "genetic")

    def _build_forward_plan(self, intent: dict, user_input: str, pert_type: Optional[str]) -> ForwardPlan:
        pert_class = (intent.get("pert_class") or "").lower().strip()
        if pert_class not in ("genetic", "drug"):
            pert_class = "genetic"
        pt = pert_type or self._choose_pert_type(pert_class, mode="forward")

        bio_desc = (intent.get("bio_context") or "").strip()
        exact_cell, proxy_cells, reason = self._resolve_forward_cells(bio_desc)

        pert_desc = (intent.get("pert_desc") or user_input).strip()
        base_pert, neighbors = self._resolve_forward_perturbation(pert_desc, pert_class, user_input)
        return ForwardPlan(
            pert_type=pt,
            pert_class=pert_class,
            base_pert=base_pert,
            pert_neighbors=neighbors,
            exact_cell=exact_cell,
            proxy_cells=proxy_cells,
            cell_reason=reason,
        )

    def _resolve_forward_cells(self, bio_desc: str) -> tuple[Optional[str], list[str], str]:
        if not bio_desc:
            return None, [], "no_bio_context"
        if self.cellline_index.is_valid(bio_desc):
            exact = self.cellline_index.canonical(bio_desc)
            proxies = self.cellline_index.proxy_cells_for(exact)
            merged = proxies["same_subtype"] + proxies["same_disease"] + proxies["same_lineage"]
            return exact, merged, "exact_cell_name"

        # disease/context description -> tree traversal
        candidates = self.cellline_index.traverse(
            bio_context=bio_desc,
            llm_choose_fn=lambda desc, options, level: self._smart_choose_cell_node(desc, options, level),
        )
        return None, candidates, "bio_context_proxy"

    def _smart_choose_cell_node(self, desc: str, options: list[str], level: str) -> str:
        return self._call_prompt("llm_map_cell_line", desc, options, level)

    def _resolve_forward_perturbation(
        self,
        pert_desc: str,
        pert_class: str,
        user_input: str,
    ) -> tuple[str, list[str]]:
        if pert_class == "drug":
            base = self.drug_index.lookup(pert_desc)
            if not base:
                cands = self._call_prompt("llm_normalize_drug", pert_desc)
                base = self.drug_index.lookup_aliases(cands) if cands else None
            if not base:
                cands = self._call_prompt("llm_map_drug", user_input)
                base = self.drug_index.lookup_aliases(cands) if cands else None
            base = base or pert_desc
            neighbors = [x[0] for x in self.drug_index.neighbors(base, min_tanimoto=0.3, top_n=20)] if base.startswith("BRD-") else []
            return base, neighbors

        hit = self.gene_index.lookup(pert_desc)
        base = hit[0] if hit else None
        if not base:
            indexed_symbol = self._gene_symbol_from_index_tokens(pert_desc) or self._gene_symbol_from_index_tokens(user_input)
            if indexed_symbol:
                base = indexed_symbol
        if not base:
            cands = self._call_prompt("llm_map_gene", pert_desc, None)
            hit = self.gene_index.lookup_candidates(cands) if cands else None
            base = hit[0] if hit else pert_desc
        neighbors = [x[0] for x in self.gene_index.neighbors(base, min_cosine=0.5, top_n=20)]
        return base, neighbors

    def _gene_symbol_from_index_tokens(self, text: str) -> Optional[str]:
        tokens = re.findall(r"[A-Za-z0-9-]{2,24}", text or "")
        if not tokens:
            return None
        # Prefer uppercase-like symbols first (e.g., EGFR, BRCA1).
        preferred = sorted(tokens, key=lambda t: (not re.fullmatch(r"[A-Z0-9-]{2,24}", t), len(t)))
        for tok in preferred:
            hit = self.gene_index.lookup(tok)
            if hit:
                return hit[0]
        return None

    def _has_pair(self, engine, pert_query: str, cell_line: str) -> bool:
        try:
            lookup = self._get_engine_pair_lookup(engine)
            tokens = lookup.get(str(cell_line), {})
            return str(pert_query).strip() in tokens
        except Exception:
            return False

    def _query_name_for_pair(self, engine, pert_query: str, cell_line: str) -> str:
        """
        Return a query name guaranteed to exist in the target cell subset.
        Prefer cmap_name for forward engine query stability.
        """
        try:
            lookup = self._get_engine_pair_lookup(engine)
            pert_q = str(pert_query).strip()
            tokens = lookup.get(str(cell_line), {})
            return tokens.get(pert_q, pert_q)
        except Exception:
            return str(pert_query)

    def _get_engine_pair_lookup(self, engine) -> dict[str, dict[str, str]]:
        key = id(engine)
        cached = self._engine_pair_lookup_cache.get(key)
        if cached is not None:
            return cached
        obs = engine._obs  # pylint: disable=protected-access
        lookup: dict[str, dict[str, str]] = {}
        for row in obs.itertuples(index=False):
            cell = str(getattr(row, "cell_iname", "")).strip()
            if not cell:
                continue
            pert = str(getattr(row, "pert_id", "")).strip()
            cmap = str(getattr(row, "cmap_name", "")).strip()
            cell_map = lookup.setdefault(cell, {})
            if pert:
                if cmap and cmap.lower() != "nan":
                    cell_map.setdefault(pert, cmap)
                else:
                    cell_map.setdefault(pert, pert)
            if cmap and cmap.lower() != "nan":
                cell_map.setdefault(cmap, cmap)
        self._engine_pair_lookup_cache[key] = lookup
        return lookup

    def _forward_meta(
        self,
        plan: ForwardPlan,
        hit_level: str,
        used_cell: Optional[str],
        used_pert: Optional[str],
    ) -> dict:
        return {
            "query_type": "forward",
            "hit_level": hit_level,
            "pert_type": plan.pert_type,
            "selected_source": plan.pert_type,
            "pert_class": plan.pert_class,
            "evidence_policy": {
                "max_forward_evidence": int(self.config.max_forward_evidence),
                "budget_exact": int(self.config.forward_budget_exact),
                "budget_proxy_pert": int(self.config.forward_budget_proxy_pert),
                "budget_proxy_cell": int(self.config.forward_budget_proxy_cell),
                "budget_proxy_both": int(self.config.forward_budget_proxy_both),
            },
            "cell_resolution_reason": plan.cell_reason,
            "requested_cell": plan.exact_cell,
            "used_cell": used_cell,
            "requested_perturbation": plan.base_pert,
            "used_perturbation": used_pert,
            "proxy_cells_checked": plan.proxy_cells[:20],
            "proxy_perts_checked": plan.pert_neighbors[:20],
        }

    def _run_reverse(
        self,
        intent: dict,
        user_input: str,
        pert_type: Optional[str],
        top_k: int,
    ):
        pt = pert_type or self._choose_pert_type(intent.get("pert_class"), mode="reverse")
        engine = self.reverse_engines[pt]
        bio_desc = intent.get("bio_context") or ""
        cell_line = self._resolve_cell_line_for_reverse(bio_desc) if bio_desc else None
        activate, suppress = self._resolve_functions(intent, user_input)
        result = engine.query(
            activate=activate,
            suppress=suppress,
            cell_line=cell_line,
            top_k=top_k,
        )
        result.resolver_meta = {
            "query_type": "reverse",
            "pert_type": pt,
            "resolved_cell_line": cell_line,
            "activate": activate,
            "suppress": suppress,
        }
        return result

    def _resolve_cell_line_for_reverse(self, bio_desc: str) -> Optional[str]:
        if not bio_desc:
            return None
        if self.cellline_index.is_valid(bio_desc):
            return self.cellline_index.canonical(bio_desc)
        candidates = self.cellline_index.traverse(
            bio_context=bio_desc,
            llm_choose_fn=lambda desc, options, level: self._call_prompt(
                "llm_map_cell_line", desc, options, level
            ),
        )
        return candidates[0] if candidates else None

    def _resolve_functions(self, intent: dict, user_input: str) -> tuple[list[str], list[str]]:
        activate_raw = list(intent.get("activate") or [])
        suppress_raw = list(intent.get("suppress") or [])
        fn_desc = intent.get("function_desc") or user_input

        activate = self._map_function_terms(activate_raw)
        suppress = self._map_function_terms(suppress_raw)

        if not activate and not suppress:
            mapped = self._call_prompt(
                "llm_map_function",
                fn_desc,
                self.function_index.for_llm(),
                3,
            )
            suppress = [v for v in mapped if self.function_index.validate(v)]
        return activate, suppress

    def _map_function_terms(self, terms: list[str]) -> list[str]:
        out: list[str] = []
        for t in terms:
            hit = self.function_index.lookup(t)
            if hit and hit not in out:
                out.append(hit)
                continue
            mapped = self._call_prompt(
                "llm_map_function",
                t,
                self.function_index.for_llm(),
                2,
            )
            for m in mapped:
                if self.function_index.validate(m) and m not in out:
                    out.append(m)
        return out

    def _choose_pert_type(self, pert_class: Optional[str], mode: str) -> str:
        cls = (pert_class or "").lower().strip()
        available = self.forward_engines if mode == "forward" else self.reverse_engines
        keys = list(available.keys())
        if not keys:
            raise RuntimeError("No data loaded for resolver.")
        if cls == "drug":
            if "cp" in available:
                return "cp"
        else:
            if "xpr" in available:
                return "xpr"
            if "sh" in available:
                return "sh"
        return keys[0]

    def _call_prompt(self, name: str, *args, **kwargs):
        cacheable = {
            "llm_parse_intent",
            "llm_map_cell_line",
            "llm_map_gene",
            "llm_map_drug",
            "llm_normalize_drug",
            "llm_map_function",
        }
        cache_key = None
        if name in cacheable:
            cache_key = (name, repr(args), repr(sorted(kwargs.items())))
            if cache_key in self._prompt_cache:
                return self._prompt_cache[cache_key]

        fn = getattr(llm_prompts, name)
        is_llm_prompt = name in {
            "llm_parse_intent",
            "llm_map_cell_line",
            "llm_map_gene",
            "llm_map_drug",
            "llm_normalize_drug",
            "llm_map_function",
            "llm_summarize_forward",
            "llm_summarize_reverse",
        }
        t0 = time.perf_counter()
        if self._log_llm_io and is_llm_prompt:
            self._log_debug(
                "LLM input | name=%s | args=%s | kwargs=%s",
                name,
                self._preview_payload(args),
                self._preview_payload(kwargs),
            )
        elif is_llm_prompt:
            self._log_debug("LLM call | name=%s", name)
        if is_llm_prompt:
            out = fn(self.client, self.model, *args, **kwargs)
            self._accumulate_llm_call(name, time.perf_counter() - t0)
        else:
            out = fn(*args, **kwargs)
        if self._log_llm_io and is_llm_prompt:
            self._log_debug("LLM output | name=%s | out=%s", name, self._preview_payload(out))
        if cache_key is not None:
            self._prompt_cache[cache_key] = out
        return out

    def _accumulate_llm_call(self, name: str, seconds: float) -> None:
        for target in (self._llm_call_stats_query, self._llm_call_stats_total):
            item = target.setdefault(name, {"count": 0.0, "seconds": 0.0})
            item["count"] += 1.0
            item["seconds"] += float(seconds)

    @staticmethod
    def _resolve_model(config: ResolverConfig) -> str:
        if config.model:
            return config.model
        return os.getenv("PXFQUERY_LLM_MODEL") or "deepseek-ai/deepseek-v4-flash"

    @staticmethod
    def _build_client(config: ResolverConfig):
        api_key = config.api_key
        base_url = config.base_url
        api_key = api_key or os.getenv("PXFQUERY_LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
        base_url = base_url or os.getenv("PXFQUERY_LLM_BASE_URL") or "http://localhost:3000/v1"

        if not api_key:
            raise ValueError("Resolver API key missing. Set PXFQUERY_LLM_API_KEY.")
        return OpenAI(api_key=api_key, base_url=base_url)
