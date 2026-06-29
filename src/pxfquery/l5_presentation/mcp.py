from __future__ import annotations

from pxfquery.l5_presentation.model import PxFQueryAnswer


def build_mcp_payload(answer: PxFQueryAnswer) -> dict:
    return {
        "schema_version": "pxfquery-l5-mcp/v1",
        "question": answer.question,
        "answer": {
            "headline": answer.headline,
            "summary": answer.summary,
            "summary_source": answer.summary_source,
            "limitations": answer.limitations,
        },
        "tables": answer.tables,
        "figure_specs": answer.figures,
        "evidence_contract": answer.rendering_contract,
        "l4_evidence": answer.structured_result,
        "assistant_instruction": (
            "Use the supplied L4 evidence and L5 rendering contract. Do not add candidates, "
            "change scores, invent citations, or upgrade weak/proxy/no-hit evidence."
        ),
    }
