THRESHOLD_DRUG_TANIMOTO: float = 0.40
THRESHOLD_GENE_COSINE: float = 0.50
THRESHOLD_CELL_LINE: str = "same_lineage_disease_subtype"

STANDARD_MATRICES: tuple[str, ...] = (
    "cp_func_ad.h5ad",
    "sh_func_ad.h5ad",
    "xpr_func_ad.h5ad",
)

STANDARD_INDEXES: tuple[str, ...] = (
    "cellline_index.json",
    "cellline_neighbors.json",
    "cellline_tree.json",
    "drug_index.json",
    "drug_neighbors.json",
    "gene_index.json",
    "gene_index_simple.json",
    "gene_neighbors.json",
    "gene_neighbors_simple.json",
    "function_index.json",
)

STANDARD_METADATA_TABLES: tuple[str, ...] = (
    "cellline_meta_standard.csv",
    "compound_meta_standard.csv",
    "gene_info_standard.csv",
)

EXPECTED_FUNCTION_TERM_COUNT: int = 91
