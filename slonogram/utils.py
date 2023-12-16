from typing import Any, get_origin
import json


def parse_json(s: str | bytes) -> Any:
    return json.loads(s)


def dump_json(j: Any) -> str:
    return json.dumps(j, ensure_ascii=False)


def origin_of(of: Any) -> Any:
    origin = get_origin(of)
    if origin is None:
        return of
    return origin


__all__ = ["origin_of"]
