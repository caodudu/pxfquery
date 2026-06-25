from __future__ import annotations

from pathlib import Path

import anndata as ad

from pxfquery.data.m1_loader import M1FixtureLoader
from pxfquery.query.forward import forward_query


class PxFquery:
    """M1 deterministic query entry point."""

    def __init__(
        self,
        matrix_path: str | None = None,
        matrix_type: str | None = None,
        manifest_path: str | None = None,
        fixture_root: str | None = None,
        config: dict | None = None,
    ):
        self.config = config or {}
        self.matrix_type = matrix_type or self.config.get("matrix_type") or "xpr"
        self.matrix = None
        self._matrices = {}
        self.loader = None
        self.matrix_path = None
        if manifest_path is not None:
            self.load_fixture(manifest_path, fixture_root=fixture_root)
        if matrix_path is not None:
            self.load_data(matrix_path, matrix_type=matrix_type)

    def load_data(self, path: str, matrix_type: str | None = None):
        matrix_path = Path(path)
        if not matrix_path.exists():
            raise FileNotFoundError(str(matrix_path))
        if matrix_path.suffix.lower() in {".yaml", ".yml"}:
            self.load_fixture(str(matrix_path))
            return self.matrix
        try:
            self.matrix = ad.read_h5ad(matrix_path)
        except Exception as exc:  # pragma: no cover - exact backend exceptions vary.
            raise ValueError(f"InvalidMatrix: {matrix_path}: {exc}") from exc
        self.matrix_type = matrix_type or self._infer_matrix_type(matrix_path)
        self._matrices[self.matrix_type] = self.matrix
        self.matrix_path = str(matrix_path)
        return self.matrix

    def load_fixture(self, manifest_path: str, fixture_root: str | None = None):
        self.loader = M1FixtureLoader(manifest_path, fixture_root=fixture_root)
        fixture = self.loader.fixture
        self._matrices = {"cp": fixture.cp, "sh": fixture.sh, "xpr": fixture.xpr}
        self.matrix = self._matrices.get(self.matrix_type) or fixture.xpr
        return fixture

    def load_data_dir(self, directory: str, pattern: str = "*.h5ad"):
        raise NotImplementedError(
            {
                "error": "NotImplemented",
                "message": f"Directory loading is outside T-059 M1 forward repair scope: {directory}/{pattern}",
                "query_type": "system",
            }
        )

    def pert2func(
        self,
        perturbation: str,
        cell_line: str,
        matrix_type: str | None = None,
        top_k: int = 20,
    ) -> dict:
        selected_type = matrix_type or self.matrix_type
        matrix = self._matrices.get(selected_type, self.matrix)
        return forward_query(
            matrix,
            perturbation=perturbation,
            cell_line=cell_line,
            matrix_type=selected_type,
            top_k=top_k,
        )

    def func2pert(
        self,
        activate,
        suppress,
        cell_line: str,
        matrix_type: str | None = None,
        top_n: int = 10,
        low_confidence_threshold: float = 0.05,
    ) -> dict:
        return {
            "error": "NotImplemented",
            "message": "Reverse query is outside the T-059 forward repair scope.",
            "query_type": "system",
        }

    def query(
        self,
        perturbation: str | None = None,
        cell_line: str | None = None,
        activate=None,
        suppress=None,
        top_k: int = 20,
        top_n: int = 10,
    ) -> dict:
        has_forward = perturbation is not None
        has_reverse = bool(activate) or bool(suppress)
        if has_forward and has_reverse:
            return {
                "error": "AmbiguousQuery",
                "message": "Both perturbation and functional targets were provided.",
                "query_type": "unknown",
            }
        if not has_forward and not has_reverse:
            return {
                "error": "UnsupportedQuery",
                "message": "Provide either perturbation or activate/suppress targets.",
                "query_type": "unknown",
            }
        if has_forward:
            return self.pert2func(perturbation=perturbation, cell_line=cell_line or "", top_k=top_k)
        return self.func2pert(activate=activate, suppress=suppress, cell_line=cell_line or "", top_n=top_n)

    @staticmethod
    def _infer_matrix_type(path: Path) -> str:
        name = path.name.lower()
        for candidate in ("xpr", "sh", "cp"):
            if candidate in name:
                return candidate
        return "xpr"
