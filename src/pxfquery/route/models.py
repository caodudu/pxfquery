from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from pxfquery.route.types import (
    CellLineSource,
    Confidence,
    Direction,
    FunctionStatus,
    LlmMode,
    PerturbationType,
    ProxyDimension,
    ResolutionMethod,
    RouteType,
    SimilarityUnit,
    SuggestionType,
    SourceIndex,
)


@dataclass
class QueryContext:
    cell_line: Optional[str] = None
    cell_line_source: Optional[CellLineSource] = None
    tissue_lineage: Optional[str] = None
    disease: Optional[str] = None
    subtype: Optional[str] = None
    perturbation_type: Optional[PerturbationType] = None
    direction: Optional[Direction] = None
    normalization_state: Optional[str] = None


@dataclass
class PerturbationResolution:
    method: ResolutionMethod = ResolutionMethod.NOT_APPLICABLE
    resolved_name: Optional[str] = None
    resolved_id: Optional[str] = None
    original_query: Optional[str] = None
    source_index: Optional[SourceIndex] = None
    perturbation_type: Optional[PerturbationType] = None


ScoreVector = dict[str, float]


@dataclass
class RankedCandidate:
    pert_id: Optional[str] = None
    cmap_name: Optional[str] = None
    score: Optional[float] = None
    rank: Optional[int] = None


@dataclass
class FunctionResponse:
    status: FunctionStatus = FunctionStatus.NO_RETRIEVAL
    matrix_source: Optional[str] = None
    sig_id: Optional[str] = None
    scores: ScoreVector | list[RankedCandidate] | None = None
    function_terms: Optional[list[str]] = None


@dataclass
class ProxyStep:
    dimension: Optional[ProxyDimension] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    via: Optional[str] = None
    similarity: Optional[float] = None
    similarity_unit: Optional[SimilarityUnit] = None
    threshold_applied: Optional[float] = None

    def __post_init__(self):
        if self.from_ is not None:
            object.__setattr__(self, "from_", self.from_)


@dataclass
class FuzzyCandidateBlocked:
    candidate: Optional[str] = None
    reason: Optional[str] = None
    threshold_applied: Optional[str] = None


@dataclass
class NearTieInfo:
    score_difference: Optional[float] = None
    top_candidates: Optional[list[RankedCandidate]] = None


@dataclass
class Diagnostics:
    warnings: Optional[list[str]] = None
    missing_fields: Optional[list[str]] = None
    invalid_fields: Optional[list[dict]] = None
    indexes_searched: Optional[list[str]] = None
    matrices_searched: Optional[list[str]] = None
    perturbation_not_found: Optional[bool] = None
    free_text_query: Optional[bool] = None
    fuzzy_candidate_blocked: Optional[FuzzyCandidateBlocked] = None
    ambiguous_perturbation: Optional[bool] = None
    candidates: Optional[list[str]] = None
    candidate_count: Optional[int] = None
    near_tie: Optional[bool] = None
    near_tie_info: Optional[NearTieInfo] = None
    multiple_brd_ids: Optional[bool] = None
    note: Optional[str] = None
    llm_mode: Optional[LlmMode] = None


@dataclass
class Suggestion:
    type: Optional[SuggestionType] = None
    text: Optional[str] = None
    action: Optional[str] = None
    required_field: Optional[str] = None
    examples: Optional[list[str]] = None
    options: Optional[list[str]] = None
    llm_mode: Optional[LlmMode] = None


@dataclass
class EvidenceRouteResponse:
    route_type: Optional[RouteType] = None
    query_context: Optional[QueryContext] = None
    perturbation_resolution: Optional[PerturbationResolution] = None
    function_response: Optional[FunctionResponse] = None
    confidence: Optional[Confidence] = None
    proxy_chain: list[ProxyStep] = field(default_factory=list)
    diagnostics: Optional[Diagnostics] = None
    suggestions: list[Suggestion] = field(default_factory=list)
