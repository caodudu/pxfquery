#!/usr/bin/env bash
# T-044 package_skeleton_m1 — execution script
# Date: 2026-06-24
# Description: Creates the M1 Python package skeleton and runs smoke tests.
# Run from the task working directory.

set -euo pipefail
TASK_DIR="/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1"
CONDA_PYTHON="/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python"

# Step 1: Create pyproject.toml
cat > "$TASK_DIR/pyproject.toml" << 'TOML'
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pxfquery"
version = "0.1.0"
description = "PxFquery: LINCS-based perturbation-to-function bioinformatics workflow"
readme = "README_TASK.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [
    {name = "PxFquery Team"},
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

[tool.hatch.build.targets.wheel]
packages = ["src/pxfquery"]
TOML
echo "pyproject.toml created"

# Step 2: Create directory structure
mkdir -p "$TASK_DIR/src/pxfquery/data"
mkdir -p "$TASK_DIR/src/pxfquery/query"
mkdir -p "$TASK_DIR/src/pxfquery/index"
mkdir -p "$TASK_DIR/src/pxfquery/llm"
mkdir -p "$TASK_DIR/src/pxfquery/viz"
mkdir -p "$TASK_DIR/src/pxfquery/cli"
echo "Directory structure created"

# Step 3: Create __init__.py with version and PxFquery export
cat > "$TASK_DIR/src/pxfquery/__init__.py" << 'PY'
__version__ = "0.1.0"

from pxfquery.core import PxFquery
PY

# Step 4: Create core.py
cat > "$TASK_DIR/src/pxfquery/core.py" << 'PY'
class PxFquery:
    def __init__(self, config=None):
        self.config = config or {}
PY

# Step 5: Create data subpackage
cat > "$TASK_DIR/src/pxfquery/data/__init__.py" << 'PY'
PY
cat > "$TASK_DIR/src/pxfquery/data/loader.py" << 'PY'
class DataLoader:
    pass
PY

# Step 6: Create query subpackage
cat > "$TASK_DIR/src/pxfquery/query/__init__.py" << 'PY'
class ForwardQuery:
    pass


class ForwardResult:
    pass
PY
cat > "$TASK_DIR/src/pxfquery/query/forward.py" << 'PY'
class ForwardQuery:
    pass


class ForwardResult:
    pass
PY
cat > "$TASK_DIR/src/pxfquery/query/reverse.py" << 'PY'
class ReverseQuery:
    pass


class ReverseResult:
    pass
PY

# Step 7: Create index subpackage
cat > "$TASK_DIR/src/pxfquery/index/__init__.py" << 'PY'
class CellLineIndex:
    pass


class DrugIndex:
    pass


class GeneIndex:
    pass


class FunctionIndex:
    pass
PY
cat > "$TASK_DIR/src/pxfquery/index/cellline_index.py" << 'PY'
class CellLineIndex:
    pass
PY
cat > "$TASK_DIR/src/pxfquery/index/drug_index.py" << 'PY'
class DrugIndex:
    pass
PY
cat > "$TASK_DIR/src/pxfquery/index/gene_index.py" << 'PY'
class GeneIndex:
    pass
PY
cat > "$TASK_DIR/src/pxfquery/index/function_index.py" << 'PY'
class FunctionIndex:
    pass
PY

# Step 8: Create llm subpackage
cat > "$TASK_DIR/src/pxfquery/llm/__init__.py" << 'PY'
def build_parse_prompt(user_query):
    pass


def build_cell_mapping_prompt(user_query):
    pass


def build_drug_mapping_prompt(user_query):
    pass


def build_gene_mapping_prompt(user_query):
    pass


def build_function_mapping_prompt(user_query):
    pass


def build_summary_prompt(query_result):
    pass
PY
cat > "$TASK_DIR/src/pxfquery/llm/prompts.py" << 'PY'
def build_parse_prompt(user_query):
    pass


def build_cell_mapping_prompt(user_query):
    pass


def build_drug_mapping_prompt(user_query):
    pass


def build_gene_mapping_prompt(user_query):
    pass


def build_function_mapping_prompt(user_query):
    pass


def build_summary_prompt(query_result):
    pass
PY

# Step 9: Create viz subpackage
cat > "$TASK_DIR/src/pxfquery/viz/__init__.py" << 'PY'
def plot_forward_bar(result, out_path=None):
    pass


def plot_reverse_table(result, out_path=None):
    pass


def plot_heatmap(matrix, out_path=None):
    pass
PY
cat > "$TASK_DIR/src/pxfquery/viz/plots.py" << 'PY'
def plot_forward_bar(result, out_path=None):
    pass


def plot_reverse_table(result, out_path=None):
    pass


def plot_heatmap(matrix, out_path=None):
    pass
PY

# Step 10: Create cli subpackage
cat > "$TASK_DIR/src/pxfquery/cli/__init__.py" << 'PY'
PY

# Step 11: Run smoke tests
echo "=== Smoke Test 1: Minimal import + version ==="
PYTHONPATH="$TASK_DIR/src" $CONDA_PYTHON -c "import pxfquery; print(pxfquery.__version__)"

echo "=== Smoke Test 2: from pxfquery import PxFquery ==="
PYTHONPATH="$TASK_DIR/src" $CONDA_PYTHON -c "from pxfquery import PxFquery; print('PxFquery:', PxFquery)"

echo "=== Smoke Test 3: Full imports ==="
PYTHONPATH="$TASK_DIR/src" $CONDA_PYTHON -c "
from pxfquery import PxFquery
from pxfquery.data.loader import DataLoader
from pxfquery.query.forward import ForwardQuery, ForwardResult
from pxfquery.query.reverse import ReverseQuery, ReverseResult
from pxfquery.index.cellline_index import CellLineIndex
from pxfquery.index.drug_index import DrugIndex
from pxfquery.index.gene_index import GeneIndex
from pxfquery.index.function_index import FunctionIndex
from pxfquery.llm.prompts import build_parse_prompt, build_summary_prompt
from pxfquery.viz.plots import plot_forward_bar, plot_reverse_table, plot_heatmap
import pxfquery.cli
print('ALL IMPORTS PASSED')
"

echo "=== All smoke tests passed ==="
