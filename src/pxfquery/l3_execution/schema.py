from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class L3RouteExecutionResult:
    route_id: str
    query_type: str
    modality: str | None
    status: str
    cell: str | None = None
    route_metadata: dict[str, Any] = field(default_factory=dict)
    row_match: dict[str, Any] = field(default_factory=dict)
    scores: dict[str, Any] = field(default_factory=dict)
    rankings: dict[str, Any] = field(default_factory=dict)
    diagnostics: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class L3ExecutionResult:
    query_id: str | None
    query_type: str | None
    execution_status: str
    source_route_schema: str | None = None
    resource_pack: dict[str, Any] = field(default_factory=dict)
    executed_routes: list[dict[str, Any]] = field(default_factory=list)
    skipped_routes: list[dict[str, Any]] = field(default_factory=list)
    errors: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[dict[str, Any]] = field(default_factory=list)
    matrix_summary: dict[str, Any] = field(default_factory=dict)
    schema_version: str = "l3-matrix-execution/v1"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
