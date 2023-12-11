from typing import Any, get_origin


def origin_of(of: Any) -> Any:
    origin = get_origin(of)
    if origin is None:
        return of
    return origin


__all__ = ["origin_of"]
