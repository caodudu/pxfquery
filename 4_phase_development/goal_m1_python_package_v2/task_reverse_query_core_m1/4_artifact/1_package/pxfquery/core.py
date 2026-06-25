from __future__ import annotations

from typing import Any

from pxfquery.data.m1_loader import M1FixtureLoader
from pxfquery.query.reverse import ReverseQueryCore


class PxFquery:
    def __init__(
        self,
        matrix_path: str | None = None,
        matrix_type: str | None = None,
        fixture_root: str | None = None,
        low_confidence_threshold: float = 0.05,
    ):
        self.matrix_path = matrix_path
        self.matrix_type = matrix_type or "xpr"
        self.fixture_root = fixture_root
        self.low_confidence_threshold = low_confidence_threshold
        self.loader: M1FixtureLoader | None = None
        self.fixture: Any | None = None
        if matrix_path:
            self.load_data(matrix_path)

    def load_data(self, path: str) -> dict[str, Any]:
        self.matrix_path = path
        self.loader = M1FixtureLoader(path, fixture_root=self.fixture_root)
        try:
            self.fixture = self.loader.fixture
        except FileNotFoundError as exc:
            self.fixture = None
            return {
                "error": "FileNotFound",
                "message": str(exc),
                "query_type": "system",
            }
        return {
            "found": True,
            "message": "M1 fixture loaded.",
            "query_type": "system",
        }

    def load_data_dir(self, directory: str, pattern: str = "*.h5ad") -> dict[str, Any]:
        return {
            "error": "NotImplemented",
            "message": "load_data_dir is not implemented for the M1 fixture package.",
            "query_type": "system",
        }

    def func2pert(
        self,
        activate: list[str],
        suppress: list[str],
        cell_line: str,
        matrix_type: str | None = None,
        top_n: int = 10,
    ) -> dict[str, Any]:
        core = ReverseQueryCore(
            fixture=self.fixture,
            low_confidence_threshold=self.low_confidence_threshold,
        )
        return core.func2pert(
            activate=activate,
            suppress=suppress,
            cell_line=cell_line,
            matrix_type=matrix_type or self.matrix_type,
            top_n=top_n,
        )

    def pert2func(
        self,
        perturbation: str,
        cell_line: str,
        matrix_type: str | None = None,
        top_k: int = 20,
    ) -> dict[str, Any]:
        return {
            "error": "NotImplemented",
            "message": "Forward query is outside T-049 reverse-core implementation scope.",
            "query_type": "forward",
        }

    def query(
        self,
        perturbation: str | None = None,
        cell_line: str | None = None,
        activate: list[str] | None = None,
        suppress: list[str] | None = None,
        top_k: int = 20,
        top_n: int = 10,
    ) -> dict[str, Any]:
        has_forward = perturbation is not None
        has_reverse = bool(activate or suppress)
        if has_forward and has_reverse:
            return {
                "error": "AmbiguousQuery",
                "message": "Both perturbation and functional targets were provided.",
                "query_type": "unknown",
            }
        if not has_forward and not has_reverse:
            return {
                "error": "UnsupportedQuery",
                "message": "Neither perturbation nor activate/suppress targets were provided.",
                "query_type": "unknown",
            }
        if has_forward:
            return self.pert2func(
                perturbation=perturbation or "",
                cell_line=cell_line or "",
                matrix_type=self.matrix_type,
                top_k=top_k,
            )
        return self.func2pert(
            activate=activate or [],
            suppress=suppress or [],
            cell_line=cell_line or "",
            matrix_type=self.matrix_type,
            top_n=top_n,
        )

