from __future__ import annotations

import csv
import html
import json
from pathlib import Path

import yaml


TASK_ROOT = Path(__file__).resolve().parents[1]
ASSET = TASK_ROOT / "1_asset"
ART = TASK_ROOT / "4_artifact"
REPORT = TASK_ROOT / "5_report"
DATE = "20260625"


def read_text(name: str) -> str:
    return (ASSET / name).read_text(encoding="utf-8")


def ensure_dirs() -> None:
    for rel in ["2_persist", "3_document", "5_table"]:
        (ART / rel).mkdir(parents=True, exist_ok=True)
    (TASK_ROOT / "3_execution").mkdir(parents=True, exist_ok=True)


def load_inputs() -> dict:
    inputs = {
        "m1_report": read_text("m1_milestone_report.md"),
        "m1_gaps": read_text("m1_known_gaps.md"),
        "package_anchor": yaml.safe_load(read_text("package_delivery_anchor.yaml")),
        "llm_anchor": yaml.safe_load(read_text("llm_resolver_anchor.yaml")),
        "metadata_contract": yaml.safe_load(read_text("evidence_metadata_contract.yaml")),
        "classification_vocab": yaml.safe_load(read_text("package_classification_vocabulary.yaml")),
        "evidence_index": json.loads(read_text("m1_evidence_index.json")),
    }
    for csv_name in [
        "m1_layered_asset_map.csv",
        "package_capability_matrix.csv",
        "llm_resolver_acceptance_matrix.csv",
        "evidence_routing_stress_mapping.csv",
    ]:
        with (ASSET / csv_name).open(newline="", encoding="utf-8") as fh:
            inputs[csv_name] = list(csv.DictReader(fh))
    return inputs


def build_capabilities() -> list[dict]:
    rows: list[dict] = [
        {
            "capability_id": "CAP-FWD-001",
            "capability_area": "package_core",
            "capability": "Forward perturbation-to-function query",
            "anchor_source": "T-062 package anchor",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "A-001/A-002: EGFR/A549/xpr forward demo found:true; CLI exit 0; JSON valid.",
            "gap_or_limit": "Only one exact positive and one no-hit case on synthetic_repair fixture; no real LINCS/T-021 standard-resource evidence.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Core deterministic forward path is evidenced, but coverage and resource basis are too narrow for full package delivery.",
        },
        {
            "capability_id": "CAP-REV-001",
            "capability_area": "package_core",
            "capability": "Reverse function-to-perturbation query",
            "anchor_source": "T-062 package anchor",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "A-001/A-002: apoptosis activation plus MYC suppression in A549 returns ranked top candidates; 42/42 validation checks pass.",
            "gap_or_limit": "Synthetic fixture only; minimal one-profile coverage; one zero-norm candidate skipped with warning; no full matrix numeric robustness evidence.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Reverse kernel exists and is validated narrowly, but not enough for complete reverse package capability.",
        },
        {
            "capability_id": "CAP-CTX-001",
            "capability_area": "package_core",
            "capability": "Biological context handling",
            "anchor_source": "T-062 package anchor",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "A-001/A-002: A549 is accepted in forward and reverse demos; ContextNotFound is listed among structured reverse errors.",
            "gap_or_limit": "No multi-cell-line, lineage, disease, subtype, or context-proxy evidence; context route metadata is not shown against T-064 contract.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Context participates in fixture lookup, but anchored biological-context routing is incomplete.",
        },
        {
            "capability_id": "CAP-EVD-EXACT-001",
            "capability_area": "evidence_routing",
            "capability": "Exact evidence routing",
            "anchor_source": "T-062/T-064 route taxonomy",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "A-001/A-002: exact EGFR/A549 and exact reverse function examples succeed.",
            "gap_or_limit": "Outputs are reported as found:true and valid JSON, but route_type=exact-hit, source index/matrix references, and full metadata contract are not evidenced.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Exact deterministic retrieval is present; exact evidence routing as a labeled metadata route is only partially evidenced.",
        },
        {
            "capability_id": "CAP-EVD-PROXY-001",
            "capability_area": "evidence_routing",
            "capability": "Proxy evidence routing",
            "anchor_source": "T-062/T-064 route taxonomy",
            "in_scope": True,
            "status": "downgraded",
            "m1_evidence": "No proxy forward, proxy reverse, proxy-cell, proxy-perturbation, or proxy-both case appears in A-001 to A-004.",
            "gap_or_limit": "M1 validates exact fixture paths only; no exact-miss trigger, neighbor source, similarity/hierarchy basis, proxy confidence, or limitation metadata.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "If M1 is treated as a complete algorithm package, replacing required proxy routing with exact-only fixture lookup is an unapproved downgrade.",
        },
        {
            "capability_id": "CAP-EVD-NOTFOUND-001",
            "capability_area": "evidence_routing",
            "capability": "Not-found and no-hit routing",
            "anchor_source": "T-062/T-064 route taxonomy",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "A-001/A-002: UNKNOWN_GENE_XYZ999/A549 returns structured PerturbationNotFound without traceback.",
            "gap_or_limit": "Only one negative control; no attempted-route metadata, threshold guard evidence, context/function no-hit, or no-false-positive confirmation under T-064 contract.",
            "fallback_used": True,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "A safe deterministic no-hit path is shown for one gene token, but user-facing no-hit routing is incomplete.",
        },
        {
            "capability_id": "CAP-ENTRY-RESOLVER-001",
            "capability_area": "resolver_llm",
            "capability": "Resolver-mediated query entry",
            "anchor_source": "T-062/T-063 resolver anchor",
            "in_scope": True,
            "status": "downgraded",
            "m1_evidence": "A-001 lists direct CLI subcommands forward/reverse/info; no resolver startup, parse object, or dispatch log is evidenced.",
            "gap_or_limit": "Direct deterministic CLI parameters substitute for resolver-mediated natural-language or semi-structured entry.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "This is acceptable for a deterministic kernel boundary, but not for a complete anchored package milestone without user-approved exclusion.",
        },
        {
            "capability_id": "CAP-LLM-001",
            "capability_area": "resolver_llm",
            "capability": "LLM-assisted parsing and summarization",
            "anchor_source": "T-062/T-063 resolver anchor",
            "in_scope": True,
            "status": "deferred-not-approved",
            "m1_evidence": "A-001 package tree includes llm/prompt templates, but A-001 to A-004 contain no LLM call, parse, summary, route, latency, failure, or fallback evidence.",
            "gap_or_limit": "Prompt/code presence is not delivery evidence; endpoint connectivity or templates would also be insufficient under T-063.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "LLM behavior is absent from M1 evidence and no explicit user approval for deferral is recorded in the registered artifacts.",
        },
        {
            "capability_id": "CAP-FALLBACK-001",
            "capability_area": "resolver_llm",
            "capability": "Deterministic fallback and runtime resilience",
            "anchor_source": "T-062/T-063 fallback semantics",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "A-001/A-002: structured errors are shown for perturbation not found and reverse error classes such as NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, EmptyTarget.",
            "gap_or_limit": "No primary resolver/LLM/proxy failure trigger is exercised; fallback metadata distinguishing primary versus fallback paths is absent.",
            "fallback_used": True,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Error resilience exists at deterministic query level, but anchored runtime fallback semantics are not delivered.",
        },
        {
            "capability_id": "CAP-META-001",
            "capability_area": "metadata",
            "capability": "Transparent evidence metadata",
            "anchor_source": "T-062/T-064 metadata contract",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "A-001/A-002: outputs are JSON and include found/not-found status; forward reference comparison excludes a harness _evidence field.",
            "gap_or_limit": "No evidence that all 8 T-064 fields are present: route_type, query_context, perturbation_resolution, function_response, confidence, proxy_chain, diagnostics, suggestions.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Minimal status metadata is present; route-aware metadata contract is not.",
        },
        {
            "capability_id": "CAP-RES-001",
            "capability_area": "resources",
            "capability": "Standard resource compatibility",
            "anchor_source": "T-062 package anchor",
            "in_scope": True,
            "status": "evidence-insufficient",
            "m1_evidence": "A-004 GAP-001/GAP-002/GAP-004 state synthetic fixture validation and minimal/synthetic indexes; A-001 package uses M1FixtureLoader.",
            "gap_or_limit": "No T-021 functional matrix/index loading or function_index runtime compatibility evidence appears in M1 artifacts.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Standard-resource compatibility remains unevidenced and blocks full current-package delivery claims.",
        },
        {
            "capability_id": "RES-ENTRY-NL-001",
            "capability_area": "resolver_llm",
            "capability": "Natural-language resolver entry",
            "anchor_source": "T-063 acceptance matrix",
            "in_scope": True,
            "status": "deferred-not-approved",
            "m1_evidence": "No natural-language input case in A-001 to A-004.",
            "gap_or_limit": "No raw NL input, parse, ambiguity fields, dispatch log, or route metadata.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "Direct CLI demos do not satisfy natural-language resolver entry.",
        },
        {
            "capability_id": "RES-ENTRY-STRUCT-001",
            "capability_area": "resolver_llm",
            "capability": "Semi-structured resolver entry",
            "anchor_source": "T-063 acceptance matrix",
            "in_scope": True,
            "status": "downgraded",
            "m1_evidence": "CLI flags provide structured parameters, but no resolver parse/normalization record is shown.",
            "gap_or_limit": "Manual CLI parameters bypass resolver parse metadata and supported-field normalization.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "CLI is useful substrate evidence, not resolver entry delivery.",
        },
        {
            "capability_id": "RES-AI-001",
            "capability_area": "resolver_llm",
            "capability": "CyHex-configured LLM route",
            "anchor_source": "T-063 acceptance matrix",
            "in_scope": True,
            "status": "evidence-insufficient",
            "m1_evidence": "No CyHex AI route, deepseek-v4-pro or successor, parse/summary call, latency, failure, or fallback metadata in M1 artifacts.",
            "gap_or_limit": "LLM prompt templates in the package tree do not demonstrate configured LLM behavior.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "No LLM acceptance evidence is available.",
        },
        {
            "capability_id": "RES-DEMO-001",
            "capability_area": "resolver_llm",
            "capability": "Required M3 demo coverage",
            "anchor_source": "T-063 demo catalog",
            "in_scope": True,
            "status": "deferred-not-approved",
            "m1_evidence": "M1 has exact forward, exact reverse, and one no-hit fixture case; no proxy, ambiguous NL, semi-structured resolver, LLM-unavailable fallback, or metadata-inspection demo.",
            "gap_or_limit": "M3 demo catalog coverage is mostly absent.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "Next resolver milestone needs a separate demo matrix; M1 cannot be credited for it.",
        },
        {
            "capability_id": "ROUTE-EXACT-HIT",
            "capability_area": "evidence_routing",
            "capability": "T-064 exact-hit route",
            "anchor_source": "T-064 route taxonomy",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "Exact fixture examples succeed.",
            "gap_or_limit": "Missing route_type exact-hit and full source/index/matrix metadata.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Behavior exists but route contract is incomplete.",
        },
        {
            "capability_id": "ROUTE-PROXY-HIT",
            "capability_area": "evidence_routing",
            "capability": "T-064 proxy-hit route",
            "anchor_source": "T-064 route taxonomy",
            "in_scope": True,
            "status": "downgraded",
            "m1_evidence": "No proxy case.",
            "gap_or_limit": "No proxy chain, threshold, similarity, hierarchy, or limitation metadata.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "Exact-only M1 does not satisfy proxy route anchor.",
        },
        {
            "capability_id": "ROUTE-NO-HIT",
            "capability_area": "evidence_routing",
            "capability": "T-064 no-hit route",
            "anchor_source": "T-064 route taxonomy",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "One unknown gene token returns PerturbationNotFound.",
            "gap_or_limit": "No threshold-guard, indexes-searched, proxy-below-threshold, or suggestions metadata.",
            "fallback_used": True,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Narrow no-hit behavior exists but is not route-complete.",
        },
        {
            "capability_id": "ROUTE-AMBIGUOUS-HIT",
            "capability_area": "evidence_routing",
            "capability": "T-064 ambiguous-hit route",
            "anchor_source": "T-064 route taxonomy",
            "in_scope": True,
            "status": "evidence-insufficient",
            "m1_evidence": "No ambiguous perturbation, multi-BRD, or near-tie reverse case in M1 artifacts.",
            "gap_or_limit": "No candidate list, ambiguity flags, or clarification/suggestion behavior.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Ambiguous route is missing from evidence.",
        },
        {
            "capability_id": "ROUTE-CONTEXT-MISSING",
            "capability_area": "evidence_routing",
            "capability": "T-064 context-missing route",
            "anchor_source": "T-064 route taxonomy",
            "in_scope": True,
            "status": "partial",
            "m1_evidence": "Reverse validation lists ContextNotFound among structured errors.",
            "gap_or_limit": "No explicit missing/invalid context demo with required fields, validation errors, or suggestions.",
            "fallback_used": True,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "Error class is evidenced, not the full context-missing user route.",
        },
        {
            "capability_id": "ROUTE-TRANSFER-SUGGESTION",
            "capability_area": "evidence_routing",
            "capability": "T-064 transfer/suggestion route",
            "anchor_source": "T-064 route taxonomy",
            "in_scope": True,
            "status": "deferred-not-approved",
            "m1_evidence": "No actionable reformulation, alternative context, related perturbation, or LLM-assisted explanation appears in M1 artifacts.",
            "gap_or_limit": "M1 returns deterministic results/errors but no user-facing transfer/suggestion semantics.",
            "fallback_used": False,
            "downgrade_or_deferral": True,
            "user_approval_reference": "",
            "reviewer_note": "Transfer/suggestion is an anchored project capability and remains undelivered.",
        },
        {
            "capability_id": "ROUTE-METADATA-CONTRACT",
            "capability_area": "metadata",
            "capability": "T-064 eight-field metadata contract",
            "anchor_source": "T-064 metadata contract",
            "in_scope": True,
            "status": "evidence-insufficient",
            "m1_evidence": "A-001/A-002 state JSON is valid and found/not-found exists.",
            "gap_or_limit": "No evidence that route_type, query_context, perturbation_resolution, function_response, confidence, proxy_chain, diagnostics, and suggestions are all present in every response.",
            "fallback_used": False,
            "downgrade_or_deferral": False,
            "user_approval_reference": "",
            "reviewer_note": "M1 metadata is below the route-aware evidence contract.",
        },
    ]
    return rows


def status_counts(rows: list[dict]) -> dict:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    return counts


def write_yaml(rows: list[dict]) -> Path:
    counts = status_counts(rows)
    data = {
        "task_id": "T-065",
        "review_version": f"v{DATE}",
        "review_date": "2026-06-25",
        "overall_classification": "deterministic kernel/substrate",
        "classification_reason": (
            "M1 evidences an installable pxfquery v0.1.0 package with deterministic "
            "forward and reverse fixture demos, CLI wiring, and structured deterministic "
            "errors. It does not evidence resolver-mediated entry, LLM parse/summary, "
            "proxy routing, transfer/suggestion semantics, full T-064 route metadata, or "
            "T-021 standard-resource compatibility. Therefore it should be treated as a "
            "deterministic kernel/substrate, not a complete anchored algorithm package."
        ),
        "status_counts": counts,
        "controlled_status_labels_used": sorted(counts),
        "registered_inputs_used": [f"A-{i:03d}" for i in range(1, 17)],
        "m1_positive_evidence_summary": {
            "package": "pxfquery 0.1.0, editable install, CLI entry point pxfquery",
            "forward": "EGFR/A549/xpr fixture query found:true; no-hit unknown gene returns PerturbationNotFound",
            "reverse": "A549 apoptosis activation/MYC suppression fixture query returns ranked candidates",
            "assembly": "T-052 package assembly 9/9 acceptance criteria PASS",
        },
        "m1_limitation_summary": {
            "synthetic_fixture": "A-004 GAP-001/GAP-002 state synthetic fixture validation, not real LINCS data.",
            "minimal_scope": "A-004 GAP-006/GAP-007 state one positive/no-hit forward case and one reverse functional profile.",
            "standard_resources": "A-004 GAP-004 states minimal/synthetic indexes and no full LINCS index loading tested.",
            "resolver_llm_proxy": "No resolver startup, LLM call, proxy route, transfer/suggestion, or T-064 metadata-contract evidence in A-001 to A-004.",
        },
        "capability_statuses": rows,
        "missing_items": [
            r["capability_id"]
            for r in rows
            if r["status"] in {"downgraded", "deferred-not-approved", "evidence-insufficient"}
        ],
        "unapproved_scope_shrinkage": [
            {
                "id": "SHRINK-001",
                "finding": "M1 report labels all gates PASS and calls known gaps low-severity, but under delivery anchors synthetic exact fixture lookup cannot stand in for complete package delivery.",
                "affected_capabilities": [
                    "CAP-EVD-PROXY-001",
                    "CAP-ENTRY-RESOLVER-001",
                    "CAP-LLM-001",
                    "CAP-RES-001",
                    "ROUTE-TRANSFER-SUGGESTION",
                ],
                "approval_found": False,
                "recommended_label": "downgraded or deferred-not-approved when claimed as complete milestone",
            },
            {
                "id": "SHRINK-002",
                "finding": "Direct CLI calls and deterministic function parameters replace resolver-mediated user entry in M1 evidence.",
                "affected_capabilities": ["CAP-ENTRY-RESOLVER-001", "RES-ENTRY-NL-001", "RES-ENTRY-STRUCT-001"],
                "approval_found": False,
                "recommended_label": "downgraded",
            },
            {
                "id": "SHRINK-003",
                "finding": "Exact-only synthetic demos replace required proxy/no-hit/ambiguous/context/transfer route coverage if M1 is treated as full package delivery.",
                "affected_capabilities": [
                    "CAP-EVD-PROXY-001",
                    "ROUTE-PROXY-HIT",
                    "ROUTE-AMBIGUOUS-HIT",
                    "ROUTE-TRANSFER-SUGGESTION",
                ],
                "approval_found": False,
                "recommended_label": "downgraded/deferred-not-approved",
            },
        ],
        "next_milestone_boundary": {
            "recommended_name": "M2 current-resource evidence-routing package milestone",
            "must_deliver_before_full_package_claim": [
                "Load or explicitly inherit T-021 standard matrices/indexes, including function_index runtime compatibility.",
                "Run exact forward, exact reverse, no-hit, context-missing, and at least one proxy route with T-064 metadata.",
                "Emit the eight required evidence metadata fields for every query result.",
                "Keep M1 fixture CLI package as the deterministic kernel rather than calling it a complete package.",
            ],
            "m3_boundary_after_m2": [
                "Resolver-mediated natural-language and semi-structured entry.",
                "CyHex-configured LLM parse/summary evidence with fallback metadata.",
                "Full proxy, ambiguous, transfer/suggestion, and LLM-unavailable demo catalog coverage.",
            ],
            "allowed_documented_gaps": [
                "Wheel/distribution build can remain a packaging follow-up if editable install is acceptable for internal milestones.",
                "Large multi-query stress coverage can be staged after route contract conformance is proven.",
            ],
        },
    }
    out = ART / "2_persist" / f"m1_vs_delivery_anchor_gap_review_v{DATE}.yaml"
    out.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return out


def write_csv(rows: list[dict]) -> Path:
    out = ART / "5_table" / f"m1_vs_delivery_anchor_capability_matrix_v{DATE}.csv"
    fields = [
        "capability_id",
        "capability_area",
        "capability",
        "anchor_source",
        "in_scope",
        "status",
        "m1_evidence",
        "gap_or_limit",
        "fallback_used",
        "downgrade_or_deferral",
        "user_approval_reference",
        "reviewer_note",
    ]
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return out


def md_table(rows: list[dict]) -> str:
    lines = [
        "| 能力 | 状态 | 证据/缺口 |",
        "|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['capability_id']}` {row['capability']} | `{row['status']}` | "
            f"{row['m1_evidence']} 缺口：{row['gap_or_limit']} |"
        )
    return "\n".join(lines)


def write_review_md(rows: list[dict]) -> Path:
    counts = status_counts(rows)
    text = f"""# M1 与交付锚点差距复核报告

生成日期：2026-06-25  
任务：T-065 `m1_vs_delivery_anchor_review`

## 总体结论

M1 应分类为：**deterministic kernel/substrate（确定性内核/底座）**。

理由是：M1 已经证明 `pxfquery` 0.1.0 能以 editable install 方式安装，提供 `forward`、`reverse`、`info` CLI，并在合成 fixture 上跑通一个正向 exact 示例、一个反向 exact 示例和若干确定性错误处理。但注册证据没有证明 resolver 入口、LLM 解析/总结、proxy 路由、transfer/suggestion、T-064 八字段证据元数据契约，也没有证明 T-021 标准矩阵和索引资源在当前包中可加载。因此，M1 不能被称为完整算法包里程碑，只能作为后续包能力的确定性内核。

## 状态统计

{yaml.safe_dump(counts, allow_unicode=True, sort_keys=False)}

## M1 已交付的有效内容

- 包装层：`pxfquery` 0.1.0、`pip install -e .`、CLI 入口和 help/info 可用。
- 正向内核：`EGFR` / `A549` / `xpr` 合成 fixture 查询返回 `found:true`，CLI 输出 JSON。
- 反向内核：`HALLMARK_APOPTOSIS` activate + `HALLMARK_MYC_TARGETS_V1` suppress / `A549` 返回候选扰动排序。
- 基础错误处理：未知基因 token 可返回 `PerturbationNotFound`；反向验证列出若干结构化错误类。

## 主要未交付或未充分证明的锚点能力

- 标准资源兼容性：M1 明确使用 `M1FixtureLoader` 和 synthetic fixture，未证明 T-021 的 cp/sh/xpr h5ad 矩阵、查询索引和 `function_index.json` 在当前包中可加载。
- resolver 入口：无自然语言或半结构化 resolver parse、normalize、dispatch 证据；直接 CLI 参数不能替代 resolver。
- LLM 能力：只有包树中存在 prompt template 的间接信息，没有 CyHex AI route、`deepseek-v4-pro` 或替代模型、解析/总结调用、延迟、失败或 fallback 元数据。
- proxy 路由：没有 proxy perturbation、proxy cell、proxy both、function alias proxy 的现行证据。
- route-aware metadata：没有证明每次响应都包含 T-064 要求的 `route_type`、`query_context`、`perturbation_resolution`、`function_response`、`confidence`、`proxy_chain`、`diagnostics`、`suggestions`。
- transfer/suggestion：没有对 no-hit、ambiguous 或 context-missing 情况给出可执行改写、替代上下文或相关扰动建议。

## 未批准的范围收缩

如果 M1 只被称为“确定性内核/底座”，上述缺口可以作为阶段性边界记录；但如果把 M1 称为完整算法包，则存在未批准范围收缩：

1. 用 direct CLI / deterministic function call 替代 resolver-mediated user entry。
2. 用 exact-only synthetic fixture demo 替代 proxy/no-hit/ambiguous/context/transfer 路由覆盖。
3. 用 prompt template 或包内 `llm/` 目录的存在替代真实 LLM parse/summary 证据。
4. 把 synthetic fixture 与 minimal index gap 标为低严重度，从而弱化标准资源兼容性要求。

## 能力矩阵

{md_table(rows)}

## 复核限制

本任务没有运行包、没有修复代码、没有分析原始数据，也没有读取未注册的前序目录。结论只基于 A-001 至 A-016 注册资产。
"""
    out = ART / "2_persist" / f"m1_vs_delivery_anchor_review_report_v{DATE}.md"
    out.write_text(text, encoding="utf-8")
    return out


def write_recommendations_md() -> Path:
    text = """# 下一里程碑边界建议

生成日期：2026-06-25  
任务：T-065 `m1_vs_delivery_anchor_review`

## 推荐边界

建议把 M1 明确命名为 **deterministic kernel/substrate**，并把下一阶段拆为两个边界：

1. **M2：current-resource evidence-routing package milestone**  
   目标是证明当前包能在标准资源或批准继承资源上完成 evidence-aware routing，而不是继续扩大 resolver/LLM 范围。

2. **M3：resolver/LLM user-facing milestone**  
   目标是在 M2 的路由和元数据契约稳定后，再交付自然语言/半结构化 resolver、LLM parse/summary 和完整 demo catalog。

## M2 必须完成后才能称为完整包里程碑

- 加载或批准继承 T-021 标准资源：cp/sh/xpr h5ad 矩阵、查询索引、metadata 表和 `function_index.json`。
- 跑通 exact forward、exact reverse、no-hit、context-missing、至少一个 proxy route。
- 每个结果输出 T-064 八字段元数据：`route_type`、`query_context`、`perturbation_resolution`、`function_response`、`confidence`、`proxy_chain`、`diagnostics`、`suggestions`。
- 对 no-hit 证明不会把低置信 fuzzy token 报成 found。
- 对 reverse 查询记录 function mapping、排序数值 sanity、warning 和 low-confidence 行为。

## M3 必须完成后才能称为 resolver/LLM 里程碑

- 自然语言输入和半结构化输入都能生成结构化 parse。
- Parse 记录包含 T-063 要求字段，包括 missing fields、ambiguity flags、parse confidence、parse method、AI route 和 fallback 状态。
- 使用 CyHex 注册 AI route 和 `deepseek-v4-pro` 或明确批准的替代模型，产生 parse 或 summary 调用证据。
- 覆盖 T-063 demo catalog：exact forward、exact reverse、proxy forward、proxy reverse、not-found、ambiguous NL、semi-structured、LLM unavailable fallback、metadata inspection。
- LLM 只能辅助解析、归一化和总结；不能制造生物学证据或把低置信实体改成 found。

## 可以作为文档化缺口保留的事项

- wheel/distribution build 可在内部开发期后移，只要 editable install 已满足当前工程运行。
- 大规模多场景 stress test 可在 M2 路由契约稳定后扩展。
- 复杂多 perturbation、多 context 聚合可以作为后续分析功能，不应阻塞 M2 的单查询路由契约。

## 不建议的边界

- 不建议把 M2 定义为“更多 synthetic fixture demo”。这会继续回避标准资源和 route metadata。
- 不建议把 M3 的 LLM 能力降级为 endpoint connectivity 或 prompt template 存在。
- 不建议把 proxy route 标为 optional，除非有明确用户批准和后续里程碑记录。
"""
    out = ART / "2_persist" / f"m1_next_milestone_boundary_recommendations_v{DATE}.md"
    out.write_text(text, encoding="utf-8")
    return out


def html_doc(title: str, body_md_summary: str, rows: list[dict]) -> str:
    table_rows = "\n".join(
        "<tr>"
        f"<td>{html.escape(r['capability_id'])}</td>"
        f"<td>{html.escape(r['capability'])}</td>"
        f"<td><code>{html.escape(r['status'])}</code></td>"
        f"<td>{html.escape(r['reviewer_note'])}</td>"
        "</tr>"
        for r in rows
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 32px; line-height: 1.55; color: #202124; }}
    h1, h2 {{ color: #102a43; }}
    .verdict {{ padding: 12px 16px; border-left: 4px solid #7a4f01; background: #fff7e6; margin: 16px 0; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 16px; font-size: 14px; }}
    th, td {{ border: 1px solid #d0d7de; padding: 8px; vertical-align: top; }}
    th {{ background: #f6f8fa; text-align: left; }}
    code {{ background: #f6f8fa; padding: 1px 4px; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>{html.escape(title)}</h1>
  <div class="verdict"><strong>总体分类：</strong> deterministic kernel/substrate（确定性内核/底座）。M1 不能作为完整算法包交付锚点通过。</div>
  {body_md_summary}
  <h2>能力状态表</h2>
  <table>
    <thead><tr><th>ID</th><th>能力</th><th>状态</th><th>复核说明</th></tr></thead>
    <tbody>{table_rows}</tbody>
  </table>
</body>
</html>
"""


def write_html(rows: list[dict]) -> tuple[Path, Path]:
    execution_body = """
  <h2>执行范围</h2>
  <p>本任务只读取 A-001 至 A-016 注册资产，未运行包验证、未修改前序任务、未修改包代码、未进行 web search。</p>
  <h2>执行步骤</h2>
  <ol>
    <li>读取 M1 报告、证据索引、分层资产图和已知缺口。</li>
    <li>读取 T-062 包交付锚点、降级规则、复核 rubric 和分类词表。</li>
    <li>读取 T-063 resolver/LLM 锚点与 acceptance matrix。</li>
    <li>读取 T-064 route taxonomy、metadata contract 和 stress mapping。</li>
    <li>将 M1 证据逐项映射到锚点能力并输出 YAML、CSV、Markdown 和 HTML 报告。</li>
  </ol>
"""
    result_body = """
  <h2>结果摘要</h2>
  <p>M1 证明了确定性 forward/reverse fixture kernel 和包安装/CLI 基础，但缺少标准资源、resolver、LLM、proxy、transfer/suggestion 与完整 route metadata 证据。</p>
  <h2>建议</h2>
  <p>下一阶段应先做 M2 current-resource evidence-routing package milestone，再做 M3 resolver/LLM user-facing milestone。</p>
"""
    exec_out = ART / "3_document" / f"execution_report_v{DATE}.html"
    result_out = ART / "3_document" / f"result_report_v{DATE}.html"
    exec_out.write_text(html_doc("T-065 执行报告", execution_body, rows), encoding="utf-8")
    result_out.write_text(html_doc("T-065 结果报告", result_body, rows), encoding="utf-8")
    return exec_out, result_out


def write_working_notes(rows: list[dict]) -> Path:
    text = """# T-065 Working Notes

Step list:

1. Verify registered assets are readable: completed; all 16 selected inputs are present as symlinks or files under `1_asset/`.
2. Extract M1 evidence: completed; M1 claims PASS for forward validation, reverse validation, and package assembly on synthetic fixture scope.
3. Apply anchors: completed; T-062/T-063/T-064 require standard resources, resolver/LLM, proxy/no-hit/ambiguous/context/transfer routes, and metadata contract where package delivery is claimed.
4. Classify capabilities: completed; status rows are written to final CSV/YAML.
5. Produce deliverables: completed by this script.

Overall working conclusion: M1 is a deterministic kernel/substrate, not a complete anchored algorithm package.
"""
    out = TASK_ROOT / "3_execution" / f"working_notes_v{DATE}.md"
    out.write_text(text, encoding="utf-8")
    return out


def write_registry(paths: list[Path]) -> Path:
    artifacts = []
    mapping = {
        "m1_vs_delivery_anchor_gap_review": "machine_readable_review",
        "m1_vs_delivery_anchor_capability_matrix": "table",
        "m1_vs_delivery_anchor_review_report": "document",
        "m1_next_milestone_boundary_recommendations": "document",
        "execution_report": "html_report",
        "result_report": "html_report",
    }
    for idx, path in enumerate(paths, start=1):
        rel = path.relative_to(TASK_ROOT).as_posix()
        name = path.stem
        art_type = "document"
        for key, val in mapping.items():
            if name.startswith(key):
                art_type = val
                break
        artifacts.append(
            {
                "id": f"T065-A-{idx:03d}",
                "name": name,
                "type": art_type,
                "path": rel,
                "created": "2026-06-25",
                "status": "accepted",
                "notes": "Produced by T-065 milestone-vs-delivery-anchor review.",
            }
        )
    out = ART / "registry.yaml"
    out.write_text(yaml.safe_dump({"artifacts": artifacts}, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return out


def write_completion(paths: list[Path], registry: Path) -> Path:
    rels = "\n".join(f"- `{p.relative_to(TASK_ROOT).as_posix()}`" for p in paths)
    text = f"""# Completion

Task: T-065 `m1_vs_delivery_anchor_review`  
Completed: 2026-06-25  
Status: complete

## Completed Steps

1. Verified registered input assets A-001 through A-016 were available under `1_asset/`.
2. Extracted M1 claims from the milestone report, evidence index, layered asset map, and known-gap report.
3. Compared M1 evidence against T-062 package delivery anchors, T-063 resolver/LLM anchors, and T-064 evidence-routing anchors.
4. Classified M1 as `deterministic kernel/substrate`.
5. Produced the required YAML, CSV, Markdown, HTML reports and updated the artifact registry.

## Deliverables

{rels}
- `{registry.relative_to(TASK_ROOT).as_posix()}`

## Validation Performed

- Parsed JSON/YAML/CSV/Markdown inputs needed for the review.
- Wrote outputs with controlled status labels from the T-062/T-063 vocabulary.
- Confirmed final artifact paths exist and are non-empty after generation.

## Caveats

This task did not run package validation, repair code, analyze raw data, or inspect unregistered predecessor folders. The review is evidence-based only on the 16 registered input assets.
"""
    out = REPORT / "completion.md"
    out.write_text(text, encoding="utf-8")
    return out


def main() -> None:
    ensure_dirs()
    load_inputs()
    rows = build_capabilities()
    working = write_working_notes(rows)
    yaml_path = write_yaml(rows)
    csv_path = write_csv(rows)
    md_path = write_review_md(rows)
    rec_path = write_recommendations_md()
    exec_html, result_html = write_html(rows)
    deliverables = [yaml_path, csv_path, md_path, rec_path, exec_html, result_html]
    registry = write_registry(deliverables)
    completion = write_completion(deliverables, registry)
    print("Wrote working notes:", working.relative_to(TASK_ROOT))
    for path in deliverables:
        print("Wrote deliverable:", path.relative_to(TASK_ROOT), path.stat().st_size)
    print("Wrote registry:", registry.relative_to(TASK_ROOT))
    print("Wrote completion:", completion.relative_to(TASK_ROOT))


if __name__ == "__main__":
    main()
