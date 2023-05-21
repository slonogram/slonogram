try:
    from orjson import loads, dumps as _dumps

    def dumps(d: dict) -> str:
        return _dumps(d).decode()

except ImportError:
    from json import loads, dumps  # type: ignore

__all__ = ["loads", "dumps"]
