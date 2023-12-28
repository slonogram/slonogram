import json
from typing import Any


def parse_json(s: str | bytes) -> Any:
    return json.loads(s)


def dump_json(j: Any) -> str:
    return json.dumps(j, ensure_ascii=False)


__all__ = ["dump_json", "parse_json"]
