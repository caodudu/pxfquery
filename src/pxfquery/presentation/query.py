from pxfquery.nlu import parse_query
from pxfquery.evidence.pipeline import run_query_pipeline


def query(text: str) -> dict:
    return run_query_pipeline(text)


def parse(text: str) -> dict:
    return parse_query(text).to_dict()
