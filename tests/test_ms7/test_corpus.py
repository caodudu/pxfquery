from pathlib import Path

from pxfquery.query import run_corpus, summarize_records


CORPUS = Path(__file__).resolve().parents[1] / "fixtures" / "ms7_execution_corpus_v20260627.yaml"


def test_ms7_full_corpus_routes_match_expected():
    records = run_corpus(CORPUS)
    summary = summarize_records(records)
    assert summary["total"] == 32
    assert summary["failed"] == 0
    assert summary["families"]["forward_drug"]["total"] == 6
    assert summary["families"]["forward_genetic"]["total"] == 6
    assert summary["families"]["reverse_drug"]["total"] == 6
    assert summary["families"]["reverse_genetic"]["total"] == 6
    assert summary["families"]["route_fallback_provider_honesty"]["total"] == 8
