from pxfquery.query import query


def run(text: str, *, provider_mode: str = "disabled") -> dict:
    return query(text, provider_mode=provider_mode)
