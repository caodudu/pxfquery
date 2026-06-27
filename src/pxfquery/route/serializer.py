from __future__ import annotations

import json
from enum import Enum
from typing import Any

import yaml

from pxfquery.route.models import EvidenceRouteResponse




def _to_plain(obj: Any) -> Any:
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, dict):
        return {k: _to_plain(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [_to_plain(item) for item in obj if item is not None]
    if isinstance(obj, tuple):
        return tuple(_to_plain(item) for item in obj if item is not None)
    if hasattr(obj, "__dataclass_fields__"):
        result = {}
        for field_name in obj.__dataclass_fields__:
            value = getattr(obj, field_name)
            output_name = "from" if field_name == "from_" else field_name
            result[output_name] = _to_plain(value)
        return result
    return obj


def response_to_dict(resp: EvidenceRouteResponse) -> dict:
    return _to_plain(resp)


def response_to_yaml(resp: EvidenceRouteResponse) -> str:
    return yaml.dump(response_to_dict(resp), default_flow_style=False, sort_keys=False, allow_unicode=True)


def response_to_json(resp: EvidenceRouteResponse) -> str:
    return json.dumps(response_to_dict(resp), indent=2, ensure_ascii=False)
