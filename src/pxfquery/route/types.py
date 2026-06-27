from enum import Enum


class RouteType(str, Enum):
    EXACT_HIT = "exact-hit"
    PROXY_HIT = "proxy-hit"
    NO_HIT = "no-hit"
    AMBIGUOUS_HIT = "ambiguous-hit"
    CONTEXT_MISSING = "context-missing"
    TRANSFER_SUGGESTION = "transfer/suggestion"


class Confidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    N_A = "n/a"


class PerturbationType(str, Enum):
    COMPOUND = "compound"
    SHRNA = "shRNA"
    ORF_OVEREXPRESSION = "orf_overexpression"
    GENE = "gene"
    UNKNOWN = "unknown"
    UNRESOLVED = "unresolved"


class Direction(str, Enum):
    FORWARD = "forward"
    REVERSE = "reverse"


class CellLineSource(str, Enum):
    EXACT = "exact"
    PROXY = "proxy"
    UNRESOLVED = "unresolved"


class ResolutionMethod(str, Enum):
    EXACT_MATCH = "exact_match"
    PROXY_NEIGHBOR = "proxy_neighbor"
    AMBIGUOUS = "ambiguous"
    UNMATCHED = "unmatched"
    NOT_APPLICABLE = "not_applicable"


class FunctionStatus(str, Enum):
    OK = "OK"
    NO_HIT = "NO_HIT"
    NO_RETRIEVAL = "NO_RETRIEVAL"
    AMBIGUOUS = "AMBIGUOUS"
    NO_RANKING = "NO_RANKING"


class SuggestionType(str, Enum):
    REFORMULATED_QUERY = "reformulated_query"
    RELATED_PERTURBATION = "related_perturbation"
    ALTERNATIVE_CONTEXT = "alternative_context"
    DISAMBIGUATION = "disambiguation"
    MISSING_FIELD = "missing_field"
    LLM_EXPLANATION = "llm_explanation"
    DIAGNOSTIC = "diagnostic"


class ProxyDimension(str, Enum):
    PERTURBATION = "perturbation"
    CELL_LINE = "cell_line"


class SimilarityUnit(str, Enum):
    TANIMOTO = "Tanimoto"
    COSINE = "cosine"
    LINEAGE = "lineage"


class LlmMode(str, Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"


class SourceIndex(str, Enum):
    DRUG_INDEX = "drug_index.json"
    GENE_INDEX = "gene_index.json"
    GENE_INDEX_SIMPLE = "gene_index_simple.json"
    DRUG_NEIGHBORS = "drug_neighbors.json"
    GENE_NEIGHBORS = "gene_neighbors.json"
    GENE_NEIGHBORS_SIMPLE = "gene_neighbors_simple.json"
    NULL = "null"
