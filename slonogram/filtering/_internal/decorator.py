import functools
import typing as t

from slonogram.filtering.extended import Filter
from slonogram.filtering.filter import FilterFn

from slonogram.utils.omit import Omittable, OMIT

P = t.ParamSpec("P")
D = t.TypeVar("D")

def filter(pure: Omittable[bool] = OMIT) -> t.Callable[[FilterFn[D]], Filter[D]]:
    return lambda f: Filter(f, pure=pure)

def lift_filter(pure: Omittable[bool] = OMIT) -> t.Callable[[t.Callable[P, FilterFn[D]]], t.Callable[P, Filter[D]]]:
    def _step(factory: t.Callable[P, FilterFn[D]]) -> t.Callable[P, Filter[D]]:
        @functools.wraps(factory)
        def inner(*args: P.args, **kwargs: P.kwargs) -> Filter[D]:
            return Filter(factory(*args, **kwargs), pure=pure)
        return inner

    return _step

__all__ = ["filter", "lift_filter"]


