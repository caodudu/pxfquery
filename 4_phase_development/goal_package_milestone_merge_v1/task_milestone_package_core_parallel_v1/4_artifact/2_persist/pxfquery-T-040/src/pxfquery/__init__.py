"""
PxFquery — Perturbation × Function Query Toolkit

A query tool for exploring functional consequences of perturbations
using pre-computed GSEA score matrices from LINCS L1000.

Two query directions:
  - pert2func: Given a perturbation → retrieve functional pathway changes
  - func2pert: Given a functional target → recommend perturbation candidates

Usage
-----
from pxfquery import PxFquery

pxf = PxFquery()
pxf.load_data("path/to/xpr_func_ad.h5ad")
pxf.load_llm(api_key="...", base_url="...", model="...")

# Forward query
result = pxf.pert2func("EGFR", cell_line="A549", top_n=20)

# Reverse query
result = pxf.func2pert(
    activate=["HALLMARK_APOPTOSIS"],
    suppress=["HALLMARK_MYC_TARGETS_V1"],
    cell_line="MCF7",
    top_k=20
)
"""

from .core import PxFquery
from .package_core import (
    NoHitGuardForwardQuery,
    PACKAGE_CORE_VERSION,
    create_forward_engine,
    forward_result_to_frame,
    load_bundle,
    load_standard_matrix,
    run_forward_demo,
)

__version__ = "0.1.0"
__all__ = [
    "NoHitGuardForwardQuery",
    "PACKAGE_CORE_VERSION",
    "PxFquery",
    "create_forward_engine",
    "forward_result_to_frame",
    "load_bundle",
    "load_standard_matrix",
    "run_forward_demo",
]
