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
from difflib import SequenceMatcher
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional

from openai import OpenAI

from ..index import CellLineIndex, DrugIndex, FunctionIndex, GeneIndex
from ..llm import prompts as llm_prompts
from ..logging_utils import LoggingSettings, configure_logger
from .forward import ForwardResult


@dataclass
class ResolverConfig:
    provider: str = "minimax"
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
    use_fast_path: bool = False
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
        prompt_hooks: Optional[dict[str, Callable]] = None,
    ):
        self.forward_engines = forward_engines
        self.reverse_engines = reverse_engines
        self.index_dir = Path(index_dir)
        self.config = config or ResolverConfig()
        self.model = self._resolve_model(self.config)
        self.prompt_hooks = prompt_hooks or {}
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
        self._logger = configure_logger(
            "pxfquery.resolver",
            LoggingSettings(
                verbosity=self.config.verbosity,
                level=self.config.log_level,
                enabled=self.config.log_enabled,
                log_to_file=self.config.log_to_file,
                log_dir=self.config.log_dir,
                file_prefix=self.config.log_file_prefix,
                human_readable=self.config.log_human_readable,
            ),
        )
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
                intent = None
                if self.config.use_fast_path:
                    intent = self._fast_parse_intent(user_input)
                if intent is None:
                    intent = self._call_prompt("llm_parse_intent", user_input)
                if not self._is_valid_intent(intent):
                    self._log_warning("LLM intent invalid, fallback to fast parser.")
                    fast_intent = self._fast_parse_intent(user_input)
                    if fast_intent is not None:
                        intent = fast_intent
                self._intent_cache[user_input] = dict(intent or {})
            query_type = (intent.get("query_type") or "").lower()
            k = int(intent.get("top_n") or top_n or self.config.default_top_n)
            self._log_info(
                "Step 2/3 Intent parsed | query_type=%s pert_class=%s bio_context=%s pert_desc=%s",
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
                result.resolver_intent = intent
                meta = getattr(result, "resolver_meta", {}) or {}
                meta["llm_call_stats"] = self._finalize_llm_stats()
                meta["query_id"] = self._active_query_id
                result.resolver_meta = meta
                self._log_info(
                    "Step 3/3 Reverse query done | found=%s | llm_calls=%s",
                    getattr(result, "found", False),
                    meta["llm_call_stats"]["query"],
                )
                return result

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
            self._log_info(
                "Step 3/3 Forward query done | found=%s hit=%s pert_type=%s | llm_calls=%s",
                getattr(result, "found", False),
                meta.get("hit_level"),
                meta.get("pert_type"),
                meta["llm_call_stats"]["query"],
            )
            return result
        finally:
            self._active_query_id = "-"

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

    def _fast_parse_intent(self, user_input: str) -> Optional[dict]:
        text = str(user_input or "").strip()
        low = text.lower()
        if not text:
            return None
        reverse_cues = ("which perturb", "recommend perturb", "what perturbation", "find perturb")
        if any(c in low for c in reverse_cues):
            return None
        forward_cues = ("pathway", "perturb", "knockdown", "knockout", "inhibitor", "treatment", "suppressed")
        if not any(c in low for c in forward_cues):
            return None
        cell = self._extract_cell_from_text(text)
        if not cell:
            m = re.search(r"\bin\s+([^,?.;]+)", text, flags=re.IGNORECASE)
            if m:
                ctx = m.group(1).strip()
                if ctx:
                    cell = ctx
        if not cell:
            m = re.search(r"\bfor\s+([^,?.;]+)(?:\s+context)?(?:,|\\?|$)", text, flags=re.IGNORECASE)
            if m:
                ctx = m.group(1).strip()
                if ctx:
                    cell = ctx
        gene = self._fast_gene_from_text(text)
        pert_class, pert_desc = self._infer_pert_class_and_desc(text, gene)
        if cell and pert_desc:
            return {
                "query_type": "forward",
                "bio_context": cell,
                "pert_desc": pert_desc,
                "pert_class": pert_class,
                "function_desc": None,
                "activate": [],
                "suppress": [],
                "top_n": None,
            }
        return None

    def _infer_pert_class_and_desc(self, text: str, gene_candidate: Optional[str]) -> tuple[str, Optional[str]]:
        low = text.lower()
        drug_cues = (" inhibitor", " drug", " compound", " treatment", " treated", "small molecule", " erlotinib", " gefitinib", " tarceva")
        genetic_cues = ("knockdown", "knockout", "crispr", "overexpression", "suppressed", "silencing", "perturbation")
        brd = re.search(r"\bBRD-[A-Za-z0-9-]+\b", text, flags=re.IGNORECASE)
        if brd:
            return "drug", brd.group(0).upper()

        # Try direct token lookup in drug index.
        for tok in re.findall(r"[A-Za-z0-9-]{2,40}", text):
            hit = self.drug_index.lookup(tok)
            if hit:
                return "drug", tok

        has_drug_cue = any(c in f" {low}" for c in drug_cues)
        has_genetic_cue = any(c in low for c in genetic_cues)

        if has_drug_cue and not has_genetic_cue:
            return "drug", text
        if gene_candidate:
            return "genetic", gene_candidate
        if has_genetic_cue:
            return "genetic", text
        if has_drug_cue:
            return "drug", text
        return "genetic", gene_candidate

    def _extract_cell_from_text(self, text: str) -> Optional[str]:
        # Prefer longest exact cell token match to avoid partial collisions.
        candidates = sorted(self.cellline_index.valid_cells(), key=len, reverse=True)
        for c in candidates:
            if not c:
                continue
            if re.search(rf"(?<![A-Za-z0-9]){re.escape(c)}(?![A-Za-z0-9])", text, flags=re.IGNORECASE):
                return self.cellline_index.canonical(c)
        return None

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
                if self.config.must_answer:
                    forced = self._force_forward_evidence(plan, engine)
                    if forced is not None:
                        result = engine.query(forced["query_name"], cell_line=forced["used_cell"], top_n=top_n)
                        result.resolver_meta = self._forward_meta(
                            plan,
                            forced["hit_level"],
                            forced["used_cell"],
                            forced["used_perturbation"],
                        )
                        result.resolver_meta["forced_fallback"] = True
                        result.resolver_meta["forced_reason"] = forced["forced_reason"]
                        result.resolver_meta["evidence_candidates"] = [forced]
                        return result
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

    @staticmethod
    def _name_similarity(a: str, b: str) -> float:
        ta = re.sub(r"[^A-Za-z0-9]+", "", str(a or "").upper())
        tb = re.sub(r"[^A-Za-z0-9]+", "", str(b or "").upper())
        if not ta or not tb:
            return 0.0
        if ta == tb:
            return 1.0
        return float(SequenceMatcher(None, ta, tb).ratio())

    def _force_forward_evidence(self, plan: ForwardPlan, engine) -> Optional[dict]:
        """
        Must-answer fallback:
        pick the most text-similar available perturbation token in candidate cells.
        """
        lookup = self._get_engine_pair_lookup(engine)
        if not lookup:
            return None

        candidate_cells: list[str] = []
        if plan.exact_cell:
            candidate_cells.append(plan.exact_cell)
        candidate_cells.extend([c for c in plan.proxy_cells if c not in candidate_cells])
        if not candidate_cells:
            candidate_cells = list(lookup.keys())

        targets: list[str] = [str(plan.base_pert)] + [str(x) for x in plan.pert_neighbors[:50]]
        targets = [t for t in targets if t]
        if not targets:
            targets = [str(plan.base_pert)]

        best = None
        best_score = -1.0
        for cell in candidate_cells:
            token_map = lookup.get(str(cell), {})
            if not token_map:
                continue
            for t in targets:
                if t in token_map:
                    qname = token_map.get(t, t)
                    return {
                        "hit_level": "FORCED_MATCH",
                        "used_cell": str(cell),
                        "used_perturbation": str(t),
                        "query_name": str(qname),
                        "forced_reason": "must_answer_token_match",
                    }
            available = list(dict.fromkeys(list(token_map.keys()) + list(token_map.values())))
            for t in targets:
                for cand in available:
                    s = self._name_similarity(t, cand)
                    if s > best_score:
                        best_score = s
                        qn = token_map.get(cand, cand)
                        best = (cell, t, cand, qn)

        if best is None:
            return None
        cell, t, cand, qn = best
        return {
            "hit_level": "FORCED_FALLBACK",
            "used_cell": str(cell),
            "used_perturbation": str(cand),
            "query_name": str(qn),
            "forced_reason": f"must_answer_similarity:{round(best_score, 3)} target={t}",
        }

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
        if self.config.use_fast_path:
            fast = self._fast_choose_option(desc, options)
            if fast is not None:
                return fast
        return self._call_prompt("llm_map_cell_line", desc, options, level)

    @staticmethod
    def _fast_choose_option(desc: str, options: list[str]) -> Optional[str]:
        if not options:
            return None
        d = (desc or "").strip().lower()
        d = d.replace("-", " ")
        d = d.replace("_", " ")
        d = d.replace("'", " ")
        d = d.replace("nsclc", "non small cell lung carcinoma")
        d = d.replace("tnbc", "triple negative breast cancer")
        d = d.replace("colorectal", "large intestine")
        d = d.replace("colon", "large intestine")
        if not d:
            return None
        generic_opts = {"carcinoma", "adenocarcinoma", "cancer", "unknown", "normal"}
        for opt in options:
            ol = opt.lower().replace("-", " ").replace("_", " ").replace("'", " ")
            if ol == d or ol in d or d in ol:
                if ol in generic_opts and ol != d:
                    continue
                return opt
        # Token overlap scoring.
        words = re.findall(r"[a-z0-9]+", d)
        if not words:
            return None
        stop = {"cell", "cells", "context", "in", "of", "the", "and"}
        dw = Counter([w for w in words if w not in stop])
        best = None
        best_score = 0
        for opt in options:
            ow = Counter(re.findall(r"[a-z0-9]+", opt.lower()))
            score = sum((dw & ow).values())
            if score > best_score:
                best_score = score
                best = opt
        if best is not None and best_score > 0:
            return best
        return None

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
            fast = self._fast_gene_from_text(pert_desc) or self._fast_gene_from_text(user_input)
            if fast:
                base = fast
        if not base:
            cands = self._call_prompt("llm_map_gene", pert_desc, None)
            hit = self.gene_index.lookup_candidates(cands) if cands else None
            base = hit[0] if hit else pert_desc
        neighbors = [x[0] for x in self.gene_index.neighbors(base, min_cosine=0.5, top_n=20)]
        return base, neighbors

    def _fast_gene_from_text(self, text: str) -> Optional[str]:
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

        hook = self.prompt_hooks.get(name)
        if hook is not None:
            if self._log_llm_io and name.startswith("llm_"):
                self._log_debug(
                    "LLM hook input | name=%s | args=%s | kwargs=%s",
                    name,
                    self._preview_payload(args),
                    self._preview_payload(kwargs),
                )
            out = hook(*args, **kwargs)
            if self._log_llm_io and name.startswith("llm_"):
                self._log_debug("LLM hook output | name=%s | out=%s", name, self._preview_payload(out))
            if cache_key is not None:
                self._prompt_cache[cache_key] = out
            return out
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
        if name in ("llm_parse_intent",):
            try:
                out = fn(self.client, self.model, *args, **kwargs)
                if is_llm_prompt:
                    self._accumulate_llm_call(name, time.perf_counter() - t0)
            except Exception as e:
                if self.config.use_fast_path:
                    self._log_warning("LLM call failed for %s, fallback to fast path: %s", name, e)
                    out = self._llm_error_fallback(name, *args, **kwargs)
                else:
                    raise
            if self._log_llm_io and is_llm_prompt:
                self._log_debug("LLM output | name=%s | out=%s", name, self._preview_payload(out))
            if cache_key is not None:
                self._prompt_cache[cache_key] = out
            return out
        if name in ("llm_map_cell_line", "llm_map_gene", "llm_map_drug", "llm_normalize_drug", "llm_map_function"):
            try:
                out = fn(self.client, self.model, *args, **kwargs)
                if is_llm_prompt:
                    self._accumulate_llm_call(name, time.perf_counter() - t0)
            except Exception as e:
                if self.config.use_fast_path:
                    self._log_warning("LLM call failed for %s, fallback to fast path: %s", name, e)
                    out = self._llm_error_fallback(name, *args, **kwargs)
                else:
                    raise
            if self._log_llm_io and is_llm_prompt:
                self._log_debug("LLM output | name=%s | out=%s", name, self._preview_payload(out))
            if cache_key is not None:
                self._prompt_cache[cache_key] = out
            return out
        if name in ("llm_summarize_forward", "llm_summarize_reverse"):
            try:
                out = fn(self.client, self.model, *args, **kwargs)
                if is_llm_prompt:
                    self._accumulate_llm_call(name, time.perf_counter() - t0)
                if self._log_llm_io and is_llm_prompt:
                    self._log_debug("LLM output | name=%s | out=%s", name, self._preview_payload(out))
                return out
            except Exception as e:
                if self.config.use_fast_path:
                    self._log_warning("LLM summary failed, fallback to template summary: %s", e)
                    if name == "llm_summarize_forward":
                        return llm_prompts._fallback_forward_summary(args[0])  # type: ignore[attr-defined]
                    return llm_prompts._fallback_reverse_summary(args[0])  # type: ignore[attr-defined]
                raise
        return fn(*args, **kwargs)

    def _accumulate_llm_call(self, name: str, seconds: float) -> None:
        for target in (self._llm_call_stats_query, self._llm_call_stats_total):
            item = target.setdefault(name, {"count": 0.0, "seconds": 0.0})
            item["count"] += 1.0
            item["seconds"] += float(seconds)

    def _llm_error_fallback(self, name: str, *args, **kwargs):
        if name == "llm_parse_intent":
            return self._fast_parse_intent(str(args[0] if args else "")) or {
                "query_type": "forward",
                "bio_context": None,
                "pert_desc": str(args[0] if args else ""),
                "pert_class": "genetic",
                "function_desc": None,
                "activate": [],
                "suppress": [],
                "top_n": None,
            }
        if name == "llm_map_cell_line":
            opts = list(args[1] if len(args) > 1 else [])
            return opts[0] if opts else ""
        if name in ("llm_map_gene", "llm_map_drug", "llm_normalize_drug", "llm_map_function"):
            return []
        return None

    @staticmethod
    def _resolve_model(config: ResolverConfig) -> str:
        if config.model:
            return config.model
        provider = (config.provider or "minimax").lower()
        if provider == "siliconflow":
            return os.getenv("SILICONFLOW_MODEL") or "Qwen/Qwen2.5-72B-Instruct"
        if provider == "mock":
            return "mock-model"
        return os.getenv("MINIMAX_MODEL") or "MiniMax-M2.7"

    @staticmethod
    def _build_client(config: ResolverConfig):
        provider = (config.provider or "minimax").lower()
        if provider == "mock":
            return None
        api_key = config.api_key
        base_url = config.base_url

        if provider == "siliconflow":
            api_key = api_key or os.getenv("SILICONFLOW_API_KEY") or os.getenv("OPENAI_API_KEY")
            base_url = base_url or os.getenv("SILICONFLOW_BASE_URL") or "https://api.siliconflow.cn/v1"
        else:
            api_key = api_key or os.getenv("MINIMAX_API_KEY") or os.getenv("OPENAI_API_KEY")
            base_url = base_url or os.getenv("MINIMAX_BASE_URL") or "https://api.minimax.chat/v1"

        if not api_key:
            raise ValueError(
                "Resolver API key missing. Set MINIMAX_API_KEY or SILICONFLOW_API_KEY in workspace/.env."
            )
        return OpenAI(api_key=api_key, base_url=base_url)
