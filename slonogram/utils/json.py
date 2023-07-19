from typing import Callable, Mapping, Sequence

loads: Callable[[bytes], Mapping | Sequence]

try:
    import orjson

    loads = orjson.loads
    dumps = orjson.dumps
except ImportError:
    from json import loads, dumps


__all__ = ["loads", "dumps"]
