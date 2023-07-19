from typing import Callable, Any

loads: Callable[[bytes], Any]

try:
    import orjson

    loads = orjson.loads

    def dumps(d: Any) -> str:
        return orjson.dumps(d).decode()

except ImportError:
    from json import loads, dumps  # type: ignore


__all__ = ["loads", "dumps"]
